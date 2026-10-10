import sys, asyncio
from playwright.async_api import async_playwright
async def main(svg, out, w, bg, color):
    async with async_playwright() as p:
        b = await p.chromium.launch()
        pg = await b.new_page(viewport={'width':w,'height':int(w*.8)})
        s = open(svg).read()
        await pg.set_content(f'<body style="margin:0;background:{bg};color:{color}"><div style="width:{w}px">{s}</div></body>')
        await pg.screenshot(path=out, full_page=True)
        await b.close()
asyncio.run(main(sys.argv[1], sys.argv[2], int(sys.argv[3]), sys.argv[4], sys.argv[5]))
