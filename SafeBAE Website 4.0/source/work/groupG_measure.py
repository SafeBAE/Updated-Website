"""Group G: list each page's main sections (height, background, h2) and total height at 1440."""
import sys, os, asyncio
sys.path.insert(0, '/home/claude/v4/tools')
from _sem import slot
from playwright.async_api import async_playwright

JS = """() => {
  const out = [];
  document.querySelectorAll('main > section, main > div').forEach(s => {
    const r = s.getBoundingClientRect();
    const h = s.querySelector('h1,h2');
    const bg = getComputedStyle(s).backgroundColor;
    out.push([s.className.slice(0,40), s.id, Math.round(r.height), bg, h ? h.textContent.trim().slice(0,60) : '']);
  });
  const m = document.querySelector('main').getBoundingClientRect().height;
  return {secs: out, main: Math.round(m), total: document.body.scrollHeight};
}"""

async def main(pages, w):
    async with async_playwright() as p:
        b = await p.chromium.launch(args=['--allow-file-access-from-files'])
        pg = await b.new_page(viewport={'width': w, 'height': 900})
        for f in pages:
            await pg.goto('file:///home/claude/v4/site/' + f, wait_until='load')
            await pg.wait_for_timeout(600)
            r = await pg.evaluate(JS)
            print(f'== {f} @{w}: {len(r["secs"])} sections, main {r["main"]}px, page {r["total"]}px')
            for c, i, h, bg, t in r['secs']:
                print(f'   {h:5d}  {bg:22s} #{i:22s} {c:40s} {t}')
        await b.close()

w = 1440
args = sys.argv[1:]
if args and args[0].isdigit():
    w = int(args[0]); args = args[1:]
with slot():
    asyncio.run(main(args, w))
