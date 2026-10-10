"""Capture the BAE Skills Lab tools from the local source files (/home/claude/assets/skills-lab).
usage: python3 work/sl_capture.py [name ...]      (no names = all)
Writes PNGs to work/slx/cap-*.png. sl_images.py turns them into site/assets/img/sl-*.webp."""
import sys, asyncio
sys.path.insert(0, '/home/claude/v3/tools')
from _sem import slot
from playwright.async_api import async_playwright
SRC = 'file:///home/claude/assets/skills-lab/'
OUT = '/home/claude/v3/work/slx/cap-'
PHONE = (390, 780)
WIDE = (1152, 720)     # 16:10, phone-style tools sit in a 540px column
DESK = (1280, 800)     # 16:10, board / wheel / landing page

BF_OK = ['asks before posting a photo', 'borrows your clothes', 'no pressure, but', 'checks in with you after a tough day',
         'keeps texting you', 'reads your private messages', 'share your notes', 'brings over guests']
SS_OK = ['I’m so sorry this happened to you', 'Take as much time as you need', 'You are not alone', 'What happened is not your fault']

async def new(b, size, scale=2):
    ctx = await b.new_context(viewport={'width': size[0], 'height': size[1]}, device_scale_factor=scale)
    pg = await ctx.new_page()
    await pg.route('**/*', lambda r: r.continue_() if r.request.url.startswith(('file:', 'data:', 'blob:', 'https://fonts.')) else r.abort())
    return ctx, pg

async def go(pg, path):
    await pg.goto(SRC + path, wait_until='load', timeout=60000)
    await pg.wait_for_timeout(1500)

async def top(pg, y=0):
    await pg.evaluate(f'window.scrollTo(0,{y})'); await pg.wait_for_timeout(350)

async def boundary(b, size, name):
    ctx, pg = await new(b, size)
    for attempt in range(60):
        await go(pg, 'boundary-flags/index.html')
        await pg.evaluate('try{localStorage.clear()}catch(e){}')
        await pg.reload(); await pg.wait_for_timeout(900)
        await pg.click('.btnPrimary'); await pg.wait_for_timeout(700)
        for c in ('.cGreen', '.cRed', '.cYellow', '.cGreen'):
            await pg.click('.choiceBtn' + c); await pg.wait_for_timeout(750)
        txt = await pg.evaluate("document.body.innerText")
        # the top card is the last statement block in the stack that is still in the deck
        cur = await pg.evaluate("""(()=>{const r=document.querySelector('.choiceBtn').getBoundingClientRect(); const el=document.elementFromPoint(innerWidth/2, r.top-150); const c=el&&el.closest('[class*=card],[class*=Card]'); return (c||el).innerText})()""")
        if any(k in cur for k in BF_OK):
            print('  boundary card:', cur.replace('\n', ' | ')[:90], f'(try {attempt+1})'); break
    await pg.mouse.move(5, 5); await top(pg)
    await pg.screenshot(path=OUT + name + '.png'); print(' ', name)
    await ctx.close()

async def label_flow(pg):
    await go(pg, 'nutrition-label/index.html')
    await pg.click('#startSkip'); await pg.wait_for_timeout(500)
    await pg.click('details.drop summary'); await pg.wait_for_timeout(300)

PICKS = [('Kindness', 100), ('Honesty', 100), ('Makes me laugh', 75), ('Good listener', 100),
         ('Respects my boundaries', 100), ('Trustworthy', 100), ('Supportive', 75), ('Patient', 50)]

async def label(b, size, name, step):
    ctx, pg = await new(b, size)
    await label_flow(pg)
    n = 5 if step == 1 else 8
    for t, _ in PICKS[:n]:
        await pg.click(f"#bankG .chip:has-text('{t}')"); await pg.wait_for_timeout(260)
    if step == 1:
        await pg.mouse.move(5, 5); await top(pg)
        await pg.screenshot(path=OUT + name + '.png'); print(' ', name); await ctx.close(); return
    await pg.click('#nextBtn'); await pg.wait_for_timeout(500)
    for i, (t, p) in enumerate(PICKS):
        if p != 100:
            await pg.click(f'.amt[data-i="{i}"] .seg button[data-p="{p}"]'); await pg.wait_for_timeout(200)
    await pg.click('#nextBtn'); await pg.wait_for_timeout(500)
    await pg.click("#sayChips .chip:has-text('Consent is the main ingredient.')"); await pg.wait_for_timeout(300)
    await pg.click('#nextBtn'); await pg.wait_for_timeout(900)
    await pg.mouse.move(5, 5); await top(pg)
    if step == 'card':
        await pg.locator('#card').screenshot(path=OUT + name + '.png')
    else:
        await pg.screenshot(path=OUT + name + '.png')
    print(' ', name); await ctx.close()

async def survivor(b, size, name):
    ctx, pg = await new(b, size)
    for attempt in range(60):
        await go(pg, 'supporting-a-survivor/index.html')
        await pg.click('#startBtn'); await pg.wait_for_timeout(900)
        cur = await pg.evaluate("document.querySelector('#card').innerText")
        if any(k in cur for k in SS_OK):
            print('  survivor card:', cur.replace('\n', ' | ')[:90], f'(try {attempt+1})'); break
    await pg.mouse.move(5, 5); await top(pg, 84 if size == PHONE else 0)
    await pg.screenshot(path=OUT + name + '.png'); print(' ', name)
    await ctx.close()

async def reset(b, size, name):
    ctx, pg = await new(b, size)
    await go(pg, 'reset-kit/index.html')
    await pg.click('.actCard >> nth=0'); await pg.wait_for_timeout(600)
    await pg.click('.protoBtn >> nth=2'); await pg.wait_for_timeout(4300)
    await pg.mouse.move(5, 5)
    await pg.screenshot(path=OUT + name + '.png'); print(' ', name)
    await ctx.close()

async def listen_wheel(b, size, name, el=False):
    ctx, pg = await new(b, size, 3 if el else 2)
    await go(pg, 'listen-closer/index.html')
    await pg.click('#startBtn'); await pg.wait_for_timeout(900)
    await pg.mouse.move(5, 5)
    if el:
        await pg.locator('.wheelstage').screenshot(path=OUT + name + '.png')
    else:
        # frame the wheel panel; the tool's own header stays out of the frame
        y = await pg.evaluate("Math.round(document.querySelector('.wheelstage').getBoundingClientRect().top + scrollY)")
        await top(pg, max(0, y - (150 if size == DESK else 60)))
        await pg.screenshot(path=OUT + name + '.png')
    print(' ', name); await ctx.close()

async def listen_q(b, size, name):
    ctx, pg = await new(b, size)
    await go(pg, 'listen-closer/index.html')
    await pg.click('#setupBtn'); await pg.wait_for_timeout(600)
    row = pg.locator("xpath=//*[normalize-space(text())='Levitating']/ancestor::*[.//button][1]")
    await row.locator('text=Play now').first.click(); await pg.wait_for_timeout(900)
    await pg.click('#toQ'); await pg.wait_for_timeout(900)
    await pg.mouse.move(5, 5)
    y = await pg.evaluate("(()=>{const e=[...document.querySelectorAll('h1,h2,h3,div,span')].find(x=>x.children.length===0 && x.textContent.trim()==='Levitating' && x.offsetParent); return e?Math.round(e.getBoundingClientRect().top+scrollY):0})()")
    await top(pg, max(0, y - 104))
    await pg.screenshot(path=OUT + name + '.png'); print(' ', name, 'slot y', y)
    await ctx.close()

async def jeopardy(b, size, name, clue=False):
    ctx, pg = await new(b, size)
    await go(pg, 'jeopardy/index.html')
    await pg.evaluate('try{localStorage.clear()}catch(e){}'); await pg.reload(); await pg.wait_for_timeout(1200)
    async def play(n, ok):
        await pg.click(f'.tile >> nth={n}'); await pg.wait_for_timeout(500)
        await pg.keyboard.press('Enter'); await pg.wait_for_timeout(500)
        await pg.keyboard.press('Enter' if ok else 'm'); await pg.wait_for_timeout(700)
    await play(0, True); await play(5, True); await play(10, False)
    if clue:
        await pg.click('.tile >> nth=6'); await pg.wait_for_timeout(800)
    await pg.mouse.move(5, 5); await top(pg)
    await pg.screenshot(path=OUT + name + '.png'); print(' ', name)
    await ctx.close()

async def home(b, size, name):
    ctx, pg = await new(b, size)
    await go(pg, 'index.html'); await pg.mouse.move(5, 5)
    await pg.screenshot(path=OUT + name + '.png'); print(' ', name)
    await ctx.close()

async def faq(b, size, name):
    ctx, pg = await new(b, size)
    await go(pg, 'faq/index.html'); await pg.mouse.move(5, 5)
    await pg.screenshot(path=OUT + name + '.png'); print(' ', name)
    await ctx.close()

JOBS = {
  # phone captures (used on skills-lab.html)
  'boundary-flags-m': lambda b: boundary(b, PHONE, 'boundary-flags-m'),
  'nutrition-label-m': lambda b: label(b, PHONE, 'nutrition-label-m', 1),
  'supporting-a-survivor-m': lambda b: survivor(b, PHONE, 'supporting-a-survivor-m'),
  'reset-kit-m': lambda b: reset(b, PHONE, 'reset-kit-m'),
  'listen-closer-m': lambda b: listen_q(b, PHONE, 'listen-closer-m'),
  'jeopardy-m': lambda b: jeopardy(b, PHONE, 'jeopardy-m', clue=True),
  # 16:10 captures (same slugs and shape as the thumbnails other pages already use)
  'boundary-flags': lambda b: boundary(b, WIDE, 'boundary-flags'),
  'nutrition-label': lambda b: label(b, WIDE, 'nutrition-label', 4),
  'supporting-a-survivor': lambda b: survivor(b, WIDE, 'supporting-a-survivor'),
  'reset-kit': lambda b: reset(b, WIDE, 'reset-kit'),
  'listen-closer': lambda b: listen_wheel(b, DESK, 'listen-closer'),
  'jeopardy': lambda b: jeopardy(b, DESK, 'jeopardy'),
  'home': lambda b: home(b, DESK, 'home'),
  # the finished bookmark (hero) and the Lab's FAQ page
  'label': lambda b: label(b, PHONE, 'label', 'card'),
  'faq': lambda b: faq(b, DESK, 'faq'),
}

async def main(names):
    async with async_playwright() as p:
        b = await p.chromium.launch(args=['--allow-file-access-from-files'])
        for n in names:
            try:
                await JOBS[n](b)
            except Exception as e:
                print('FAILED', n, str(e)[:300])
        await b.close()

if __name__ == '__main__':
    names = sys.argv[1:] or list(JOBS)
    with slot():
        asyncio.run(main(names))
