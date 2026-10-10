"""Group A: list each top-level section of <main> with its height, background and heading.
usage: python3 work/groupA_measure.py page.html [page.html ...] [--w=1440]"""
import sys, asyncio
sys.path.insert(0, '/home/claude/v4/tools')
from _sem import slot
from playwright.async_api import async_playwright

JS = r'''() => {
  const out = [];
  for (const s of document.querySelectorAll('main > *')) {
    const r = s.getBoundingClientRect();
    if (r.height < 2) continue;
    const h = s.querySelector('h1,h2');
    const bg = getComputedStyle(s).backgroundColor;
    out.push([Math.round(r.height), bg, (s.className || s.tagName).toString().slice(0, 40), h ? h.textContent.trim().slice(0, 60) : '']);
  }
  return [document.body.scrollHeight, document.querySelector('main').getBoundingClientRect().height, out];
}'''

async def main(pages, w):
    async with async_playwright() as p:
        b = await p.chromium.launch(args=['--allow-file-access-from-files'])
        pg = await b.new_page(viewport={'width': w, 'height': 900})
        for f in pages:
            await pg.goto('file:///home/claude/v4/site/' + f, wait_until='load', timeout=60000)
            await pg.wait_for_timeout(700)
            total, mainh, secs = await pg.evaluate(JS)
            print(f'== {f} @{w}: page {total}px, main {round(mainh)}px, {len(secs)} sections')
            for i, (h, bg, cls, t) in enumerate(secs):
                print(f'  {i+1:2d}. {h:5d}px  {bg:22s} {cls:40s} {t}')
        await b.close()

args = [a for a in sys.argv[1:] if not a.startswith('--')]
w = int(next((a.split('=')[1] for a in sys.argv[1:] if a.startswith('--w=')), 1440))
with slot():
    asyncio.run(main(args, w))
