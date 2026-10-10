import sys, asyncio, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _sem import slot
from playwright.async_api import async_playwright
# usage: el.py page.html "css selector" [width] [out] [clickSelector]
async def main(pagef, sel, w, out, click):
    async with async_playwright() as p:
        b = await p.chromium.launch(args=['--allow-file-access-from-files'])
        pg = await b.new_page(viewport={'width':w,'height':900})
        msgs=[]
        pg.on('pageerror', lambda e: msgs.append(f'PAGEERROR: {e}'))
        pg.on('console', lambda m: msgs.append(f'{m.type}: {m.text}') if m.type=='error' else None)
        await pg.goto('file:///home/claude/v3/site/'+pagef, wait_until='networkidle', timeout=60000)
        await pg.evaluate("document.querySelectorAll('img[loading=lazy]').forEach(i=>{i.loading='eager'; const s=i.src; i.src=''; i.src=s;})")
        await pg.evaluate("document.querySelectorAll('.reveal').forEach(e=>e.classList.add('in'))")
        await pg.wait_for_timeout(1200)
        if click:
            for c in click.split('||'):
                await pg.click(c); await pg.wait_for_timeout(900)
        el = pg.locator(sel).first
        await el.scroll_into_view_if_needed(); await pg.wait_for_timeout(600)
        sw = await pg.evaluate('document.documentElement.scrollWidth')
        if sw > w: msgs.append(f'HORIZONTAL OVERFLOW: scrollWidth={sw} > {w}')
        await el.screenshot(path=out)
        for m in msgs[:15]: print(m)
        await b.close()
a=sys.argv
pagef=a[1]; sel=a[2]; w=int(a[3]) if len(a)>3 else 1440
out=a[4] if len(a)>4 and a[4] else '/home/claude/v3/shots/el.png'
click=a[5] if len(a)>5 else ''

with slot():
    asyncio.run(main(pagef,sel,w,out,click))
print(out)
