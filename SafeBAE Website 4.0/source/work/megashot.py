import asyncio, sys
from playwright.async_api import async_playwright
from PIL import Image
W=int(sys.argv[1]) if len(sys.argv)>1 else 1440
page=sys.argv[2] if len(sys.argv)>2 else 'about.html'
async def main():
    async with async_playwright() as p:
        b = await p.chromium.launch(args=['--allow-file-access-from-files'])
        pg = await b.new_page(viewport={'width':W,'height':900})
        await pg.goto('file:///home/claude/v4/site/'+page, wait_until='networkidle')
        await pg.wait_for_timeout(800)
        for i in range(6):
            await pg.hover(f'.nav__item:nth-child({i+1}) .nav__top'); await pg.wait_for_timeout(500)
            await pg.screenshot(path=f'shots/mega_{i}.png', clip={'x':0,'y':0,'width':W,'height':520})
        await b.close()
asyncio.run(main())
ims=[Image.open(f'shots/mega_{i}.png') for i in range(6)]
w,H=ims[0].size
sheet=Image.new('RGB',(w*2, H*3))
for i,im in enumerate(ims): sheet.paste(im,((i%2)*w,(i//2)*H))
sc=1780/(w*2)
sheet=sheet.resize((int(w*2*sc), int(H*3*sc))); sheet.save('shots/mega_sheet.jpg', quality=82); print(sheet.size)
