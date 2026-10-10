import sys, asyncio, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _sem import slot
from playwright.async_api import async_playwright
# usage: vp.py page.html width height out [click||click] [scrollY]
async def main(pagef, w, h, out, click, sy):
    async with async_playwright() as p:
        b = await p.chromium.launch(args=['--allow-file-access-from-files'])
        pg = await b.new_page(viewport={'width':w,'height':h})
        msgs=[]
        pg.on('pageerror', lambda e: msgs.append(f'PAGEERROR: {e}'))
        await pg.goto('file:///home/claude/v4/site/'+pagef, wait_until='networkidle', timeout=60000)
        await pg.wait_for_timeout(800)
        if sy: await pg.evaluate(f'window.scrollTo(0,{sy})'); await pg.wait_for_timeout(500)
        if click:
            for c in click.split('||'):
                (await pg.hover(c[6:])) if c.startswith('hover:') else (await pg.click(c)); await pg.wait_for_timeout(700)
        await pg.screenshot(path=out)
        for m in msgs[:15]: print(m)
        await b.close()
a=sys.argv
with slot():
    asyncio.run(main(a[1], int(a[2]), int(a[3]), a[4], a[5] if len(a)>5 else '', int(a[6]) if len(a)>6 else 0))
print(a[4])
