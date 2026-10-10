"""Group G: element shot after scrolling the whole page instantly (so scroll-driven states are complete).
usage: groupG_elshot.py page.html selector width out.png [scale]"""
import sys, asyncio
sys.path.insert(0, '/home/claude/v4/tools')
from _sem import slot
from playwright.async_api import async_playwright
from PIL import Image
pagef, sel, w, out = sys.argv[1], sys.argv[2], int(sys.argv[3]), sys.argv[4]
scale = float(sys.argv[5]) if len(sys.argv) > 5 else 0.55
async def main():
    async with async_playwright() as p:
        b = await p.chromium.launch(args=['--allow-file-access-from-files'])
        pg = await b.new_page(viewport={'width': w, 'height': 900})
        await pg.goto('file:///home/claude/v4/site/' + pagef, wait_until='load')
        await pg.evaluate("document.documentElement.style.scrollBehavior='auto'")
        h = await pg.evaluate('document.body.scrollHeight')
        for y in range(0, h + 900, 400):
            await pg.evaluate(f'window.scrollTo(0,{y})'); await pg.wait_for_timeout(60)
        await pg.evaluate("document.querySelectorAll('.reveal').forEach(e=>{e.classList.remove('pre');e.classList.add('in')})")
        await pg.evaluate("document.querySelector('.site-header').style.position='static'")
        await pg.wait_for_timeout(900)
        await pg.locator(sel).first.screenshot(path=out)
        await b.close()
with slot():
    asyncio.run(main())
im = Image.open(out); im = im.resize((int(im.width * scale), int(im.height * scale)))
jo = out.replace('.png', '.jpg'); im.convert('RGB').save(jo, quality=72); print(jo, im.size)
