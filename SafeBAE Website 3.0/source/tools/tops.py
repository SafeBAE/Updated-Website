import asyncio, sys
from playwright.async_api import async_playwright
SITE = sys.argv[1]; OUT = sys.argv[2]; pages = sys.argv[3:]
async def main():
    async with async_playwright() as p:
        b = await p.chromium.launch(args=['--allow-file-access-from-files'])
        pg = await b.new_page(viewport={'width':1440,'height':1000})
        for f in pages:
            await pg.goto(f'file://{SITE}/{f}', wait_until='load'); await pg.wait_for_timeout(700)
            await pg.screenshot(path=f'{OUT}/{f[:-5]}.png')
        await b.close()
asyncio.run(main())
