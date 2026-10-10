"""groupE: list elements whose right edge passes the viewport. usage: groupE_overflow.py page.html width"""
import sys, asyncio
sys.path.insert(0, '/home/claude/v4/tools')
from _sem import slot
from playwright.async_api import async_playwright
JS = """(w) => { const out=[]; document.querySelectorAll('main *').forEach(e=>{ const r=e.getBoundingClientRect();
  if(r.right > w + 1 && r.width > 0){ const cs=getComputedStyle(e); out.push([Math.round(r.right), Math.round(r.width), e.tagName.toLowerCase()+'.'+(e.className&&e.className.baseVal===undefined?e.className:'').toString().split(' ').join('.'), e.closest('section')?.id||'']); } });
  return out.slice(0,25); }"""
async def main(f, w):
    async with async_playwright() as p:
        b = await p.chromium.launch(args=['--allow-file-access-from-files'])
        pg = await b.new_page(viewport={'width': w, 'height': 900})
        await pg.goto('file:///home/claude/v4/site/' + f, wait_until='networkidle')
        await pg.wait_for_timeout(600)
        for r in await pg.evaluate(JS, w): print(r)
        await b.close()
with slot(): asyncio.run(main(sys.argv[1], int(sys.argv[2])))
