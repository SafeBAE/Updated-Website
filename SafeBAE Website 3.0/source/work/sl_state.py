"""Shoot one element of skills-lab.html after optional clicks, with the sticky header un-stuck.
usage: sl_state.py "<selector>" <width> <out.png> ["click1||click2"] [scale]"""
import sys, asyncio
sys.path.insert(0, '/home/claude/v3/tools')
from _sem import slot
from playwright.async_api import async_playwright
async def main(sel, w, out, clicks):
    async with async_playwright() as p:
        b = await p.chromium.launch(args=['--allow-file-access-from-files'])
        pg = await b.new_page(viewport={'width': w, 'height': 900})
        msgs = []
        pg.on('pageerror', lambda e: msgs.append(f'PAGEERROR: {e}'))
        pg.on('console', lambda m: msgs.append(f'{m.type}: {m.text}') if m.type == 'error' else None)
        await pg.goto('file:///home/claude/v3/site/skills-lab.html', wait_until='networkidle')
        await pg.add_style_tag(content='.site-header{position:static!important}')
        await pg.evaluate("document.querySelectorAll('img[loading=lazy]').forEach(i=>{i.loading='eager'})")
        await pg.evaluate("document.querySelectorAll('.reveal').forEach(e=>e.classList.add('in'))")
        await pg.wait_for_timeout(1500)
        for c in clicks:
            if c.startswith('key:'): await pg.keyboard.press(c[4:])
            elif c.startswith('hover:'): await pg.hover(c[6:])
            elif c.startswith('focus:'): await pg.focus(c[6:])
            else: await pg.click(c)
            await pg.wait_for_timeout(1100)
        el = pg.locator(sel).first
        await el.scroll_into_view_if_needed(); await pg.wait_for_timeout(500)
        await el.screenshot(path=out)
        for m in msgs[:10]: print(m)
        await b.close()
a = sys.argv
clicks = a[4].split('||') if len(a) > 4 and a[4] else []
with slot():
    asyncio.run(main(a[1], int(a[2]), a[3], clicks))
print(a[3])
