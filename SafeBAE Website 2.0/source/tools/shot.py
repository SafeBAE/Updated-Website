import sys, asyncio
from playwright.async_api import async_playwright
async def main(urls, outdir, w=1440, h=900, full=True):
    async with async_playwright() as p:
        b = await p.chromium.launch()
        pg = await b.new_page(viewport={'width':w,'height':h})
        for i,u in enumerate(urls):
            try:
                await pg.goto(u, wait_until='networkidle', timeout=60000)
            except Exception as e:
                print('ERR',u,e)
            await pg.wait_for_timeout(1500)
            name = u.rstrip('/').split('/')[-1] or 'home'
            name = name.replace('.html','')
            await pg.screenshot(path=f'{outdir}/{name}_{w}.png', full_page=full)
            print('ok', u)
        await b.close()
if __name__=='__main__':
    w=int(sys.argv[2]) if len(sys.argv)>2 else 1440
    asyncio.run(main(sys.argv[3:], sys.argv[1], w=w))
