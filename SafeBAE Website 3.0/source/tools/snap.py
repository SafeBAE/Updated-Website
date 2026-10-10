import sys, asyncio, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _sem import slot
from playwright.async_api import async_playwright
# usage: snap.py page.html [width] [full|top] [outname]
async def main(pagef, w, mode, out):
    async with async_playwright() as p:
        b = await p.chromium.launch(args=['--allow-file-access-from-files'])
        pg = await b.new_page(viewport={'width':w,'height':900})
        msgs=[]
        pg.on('console', lambda m: msgs.append(f'{m.type}: {m.text}') if m.type in ('error','warning') else None)
        pg.on('pageerror', lambda e: msgs.append(f'PAGEERROR: {e}'))
        await pg.goto('file:///home/claude/v3/site/'+pagef, wait_until='networkidle', timeout=60000)
        await pg.evaluate("document.querySelectorAll('img[loading=lazy]').forEach(i=>{i.loading='eager'; const s=i.src; i.src=''; i.src=s;})")
        await pg.wait_for_timeout(1500)
        h = await pg.evaluate('document.body.scrollHeight')
        y=0
        while y < h:
            await pg.evaluate(f'window.scrollTo(0,{y})'); await pg.wait_for_timeout(120); y += 700
            h = await pg.evaluate('document.body.scrollHeight')
        await pg.evaluate("document.querySelectorAll('.reveal').forEach(e=>{e.classList.remove('pre');e.classList.add('in')})")
        await pg.evaluate("Promise.race([Promise.all([...document.images].map(i=>{i.loading='eager'; return i.decode().catch(()=>0)})), new Promise(r=>setTimeout(r,15000))])")
        await pg.evaluate('window.scrollTo(0,0)'); await pg.wait_for_timeout(1200)
        # stop animations for stable shot
        await pg.add_style_tag(content='*{animation-play-state:paused!important}')
        sw = await pg.evaluate('document.documentElement.scrollWidth')
        if sw > w: msgs.append(f'HORIZONTAL OVERFLOW: scrollWidth={sw} > {w}')
        await pg.screenshot(path=out, full_page=(mode=='full'))
        for m in msgs[:15]: print(m)
        await b.close()
pagef=sys.argv[1]; w=int(sys.argv[2]) if len(sys.argv)>2 else 1440; mode=sys.argv[3] if len(sys.argv)>3 else 'full'
out=sys.argv[4] if len(sys.argv)>4 else '/home/claude/v3/shots/'+pagef.replace('.html','')+f'_{w}.png'

with slot():
    asyncio.run(main(pagef,w,mode,out))
print(out)
