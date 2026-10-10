import asyncio
from playwright.async_api import async_playwright
async def main():
    async with async_playwright() as p:
        b = await p.chromium.launch()
        ctx = await b.new_context(viewport={'width':390,'height':844}, device_scale_factor=2, is_mobile=True, has_touch=True)
        pg = await ctx.new_page()
        await pg.goto('https://checkyourvibe.org/', wait_until='networkidle', timeout=60000)
        await pg.wait_for_timeout(2500)
        await pg.screenshot(path='vc_mobile.png')
        await pg.screenshot(path='vc_mobile_full.png', full_page=True)
        ctx2 = await b.new_context(viewport={'width':1440,'height':900})
        pg2 = await ctx2.new_page()
        await pg2.goto('https://checkyourvibe.org/', wait_until='networkidle', timeout=60000)
        await pg2.wait_for_timeout(2500)
        await pg2.screenshot(path='vc_desktop.png')
        txt = await pg2.inner_text('body')
        open('vc_text.txt','w').write(txt)
        await b.close()
asyncio.run(main())
