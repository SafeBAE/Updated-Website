import sys, asyncio, os, json
sys.path.insert(0, '/home/claude/v4/tools')
from _sem import slot
from playwright.async_api import async_playwright
# usage: sc2_box.py page.html width "sel1" "sel2" ...   -> prints x,y,w,h (+text) for every match
async def main(pagef, w, sels):
    async with async_playwright() as p:
        b = await p.chromium.launch(args=['--allow-file-access-from-files'])
        pg = await b.new_page(viewport={'width':w,'height':900})
        await pg.goto('file:///home/claude/v4/site/'+pagef, wait_until='networkidle', timeout=60000)
        await pg.wait_for_timeout(1500)
        for s in sels:
            r = await pg.evaluate('''(s)=>[...document.querySelectorAll(s)].slice(0,40).map(e=>{const r=e.getBoundingClientRect(); const cs=getComputedStyle(e); return [Math.round(r.left),Math.round(r.top+scrollY),Math.round(r.width),Math.round(r.height),cs.fontSize,(e.innerText||'').replace(/\\s+/g,' ').slice(0,40)]})''', s)
            print('##', s)
            for x in r: print('  ', x)
        await b.close()
with slot():
    asyncio.run(main(sys.argv[1], int(sys.argv[2]), sys.argv[3:]))
