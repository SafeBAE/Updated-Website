"""Group C: page height + section list (tag, class, id, h2, height) at a width. usage: groupC_measure.py width page..."""
import sys, os, asyncio
sys.path.insert(0, '/home/claude/v4/tools')
from _sem import slot
from playwright.async_api import async_playwright

JS = """() => { const out = [];
  for (const s of document.querySelectorAll('main > *')) {
    const r = s.getBoundingClientRect(); if (r.height < 2) continue;
    const h = s.querySelector('h1,h2'); const bg = getComputedStyle(s).backgroundColor;
    out.push([s.tagName.toLowerCase(), (s.className||'').toString().slice(0,48), s.id||'', h ? h.textContent.trim().slice(0,60) : '', Math.round(r.height), bg]);
  }
  return [document.documentElement.scrollHeight, out]; }"""

async def main(w, pages):
    async with async_playwright() as p:
        b = await p.chromium.launch(args=['--allow-file-access-from-files'])
        pg = await b.new_page(viewport={'width': w, 'height': 900})
        for f in pages:
            await pg.goto('file:///home/claude/v4/site/' + f, wait_until='load', timeout=60000)
            await pg.wait_for_timeout(700)
            h, secs = await pg.evaluate(JS)
            print(f'== {f} @{w}: {h}px, {len(secs)} blocks in main')
            for s in secs: print('  ', s)
        await b.close()

with slot():
    asyncio.run(main(int(sys.argv[1]), sys.argv[2:]))
