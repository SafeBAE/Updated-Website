"""Group D: section list + heights for my pages at one width (one browser).
usage: python3 work/groupD_measure.py [width] page.html ..."""
import sys, os, asyncio
sys.path.insert(0, '/home/claude/v4/tools')
from _sem import slot
from playwright.async_api import async_playwright

JS = r'''() => {
  const out = [];
  document.querySelectorAll('main > section, main > div, main > aside').forEach(s => {
    const r = s.getBoundingClientRect();
    const h = s.querySelector('h1,h2');
    const bg = getComputedStyle(s).backgroundColor;
    out.push([s.className.replace(/\s+/g,' ').slice(0,60), s.id || '', Math.round(r.height), (h ? h.textContent.trim().replace(/\s+/g,' ').slice(0,60) : '(no head)'), bg]);
  });
  return {h: document.documentElement.scrollHeight, main: Math.round(document.querySelector('main').getBoundingClientRect().height), secs: out};
}'''

async def main(w, pages):
    async with async_playwright() as p:
        b = await p.chromium.launch(args=['--allow-file-access-from-files'])
        pg = await b.new_page(viewport={'width': w, 'height': 900})
        for f in pages:
            await pg.goto('file:///home/claude/v4/site/' + f, wait_until='load', timeout=60000)
            await pg.evaluate("document.querySelectorAll('img[loading=lazy]').forEach(i=>i.loading='eager')")
            await pg.wait_for_timeout(700)
            r = await pg.evaluate(JS)
            print(f'== {f} @{w}: page {r["h"]}px, main {r["main"]}px, {len(r["secs"])} sections')
            for c, i, h, t, bg in r['secs']:
                print(f'   {h:5d}  #{i:<20} {t:<60} [{c}] {bg}')
        await b.close()

w = int(sys.argv[1]); pages = sys.argv[2:]
with slot():
    asyncio.run(main(w, pages))
