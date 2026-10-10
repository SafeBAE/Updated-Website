"""groupE: page height + section list at 1440 without a screenshot. usage: groupE_measure.py page.html [...]"""
import sys, asyncio, os
sys.path.insert(0, '/home/claude/v4/tools')
from _sem import slot
from playwright.async_api import async_playwright

JS = """() => { const out=[]; document.querySelectorAll('main > section, main > div > section').forEach(s=>{
  const r=s.getBoundingClientRect(); const h=s.querySelector('h1,h2'); const bg=getComputedStyle(s).backgroundColor;
  out.push([Math.round(r.height), (h?h.textContent.trim().slice(0,50):'(no head)'), bg]); });
  return {h: document.body.scrollHeight, secs: out}; }"""

async def main(pages, w):
    async with async_playwright() as p:
        b = await p.chromium.launch(args=['--allow-file-access-from-files'])
        pg = await b.new_page(viewport={'width': w, 'height': 900})
        for f in pages:
            await pg.goto('file:///home/claude/v4/site/' + f, wait_until='networkidle', timeout=60000)
            await pg.wait_for_timeout(400)
            r = await pg.evaluate(JS)
            print(f'{f}: {r["h"]}px, {len(r["secs"])} sections')
            for hh, t, bg in r['secs']:
                print(f'   {hh:5d}  {bg:22s} {t}')
        await b.close()

w = 1440
args = [x for x in sys.argv[1:]]
if args and args[0].isdigit():
    w = int(args.pop(0))
with slot():
    asyncio.run(main(args, w))
