import sys, asyncio
sys.path.insert(0, '/home/claude/v4/tools')
from _sem import slot
from playwright.async_api import async_playwright
async def main():
    async with async_playwright() as p:
        b = await p.chromium.launch(args=['--allow-file-access-from-files'])
        pg = await b.new_page(viewport={'width':1440,'height':900})
        errs=[]
        pg.on('console', lambda m: errs.append(m.text))
        pg.on('pageerror', lambda e: errs.append(str(e)))
        await pg.goto('file:///home/claude/v4/site/about.html', wait_until='load')
        await pg.evaluate("document.documentElement.style.scrollBehavior='auto'")
        for y in range(0, 8000, 500):
            await pg.evaluate(f'window.scrollTo(0,{y})'); await pg.wait_for_timeout(100)
        print(await pg.evaluate("new Promise(r=>requestAnimationFrame(()=>r('raf ok')))"))
        print(await pg.evaluate("[window.scrollY, document.documentElement.scrollHeight, getComputedStyle(document.documentElement).scrollBehavior]"))
        r = await pg.evaluate("""() => { const w=document.querySelector('.ab-tlw'); return [w.style.getPropertyValue('--p'), w.className, [...document.querySelectorAll('.ab-tl li')].map(l=>l.className+' '+l.offsetTop)] }""")
        print(r, errs)
        await b.close()
with slot():
    asyncio.run(main())
