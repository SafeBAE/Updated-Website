import sys, asyncio
sys.path.insert(0, '/home/claude/v4/tools')
from _sem import slot
from playwright.async_api import async_playwright
JS = r'''() => { const out = {}; const main = document.querySelector('main');
 const w = document.createTreeWalker(main, NodeFilter.SHOW_TEXT);
 while (w.nextNode()) { const n = w.currentNode; const t = n.textContent.trim(); if (t.length < 2) continue; const el = n.parentElement; const cs = getComputedStyle(el);
   if (cs.display === 'none' || cs.visibility === 'hidden') continue; const r = el.getBoundingClientRect(); if (r.width < 2 || r.height < 2) continue;
   let hid = false; for (let e = el; e && e !== main; e = e.parentElement) { const c = getComputedStyle(e); if (c.display === 'none' || e.hidden) { hid = true; break; } } if (hid) continue;
   const fs = parseFloat(cs.fontSize); const mono = /Plex Mono/.test(cs.fontFamily); const lim = mono ? 11.2 : 14;
   if (fs < lim - .05) { const k = fs.toFixed(1) + (mono ? ' mono ' : ' ') + el.tagName.toLowerCase() + '.' + [...el.classList].join('.') ; out[k] = out[k] || t.slice(0, 50); } }
 return out; }'''
async def main(pages, w):
    async with async_playwright() as p:
        b = await p.chromium.launch(args=['--allow-file-access-from-files'])
        for pagef in pages:
            pg = await b.new_page(viewport={'width': w, 'height': 900})
            await pg.goto('file:///home/claude/v4/site/' + pagef, wait_until='networkidle', timeout=60000)
            await pg.wait_for_timeout(800)
            r = await pg.evaluate(JS)
            print('##', pagef, w, len(r))
            for k, v in sorted(r.items()): print('   ', k, '|', v)
            await pg.close()
        await b.close()
with slot():
    asyncio.run(main(sys.argv[2:], int(sys.argv[1])))
