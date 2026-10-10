"""Group D: shoot a section with the live Zeffy iframe in place (site served over http, external requests blocked).
usage: python3 work/groupD_live.py page.html "<selector>" width out.png"""
import sys, asyncio, threading, http.server, socketserver, functools
sys.path.insert(0, '/home/claude/v4/tools')
from _sem import slot
from playwright.async_api import async_playwright

page, sel, w, out = sys.argv[1], sys.argv[2], int(sys.argv[3]), sys.argv[4]
class Q(http.server.SimpleHTTPRequestHandler):
    def log_message(self, *a): pass
srv = socketserver.TCPServer(('127.0.0.1', 0), functools.partial(Q, directory='/home/claude/v4/site'))
port = srv.server_address[1]
threading.Thread(target=srv.serve_forever, daemon=True).start()

async def main():
    async with async_playwright() as p:
        b = await p.chromium.launch()
        pg = await b.new_page(viewport={'width': w, 'height': 900})
        await pg.route('**/*', lambda r: r.continue_() if r.request.url.startswith(f'http://127.0.0.1:{port}') else r.abort())
        await pg.goto(f'http://127.0.0.1:{port}/{page}', wait_until='load')
        await pg.wait_for_timeout(800)
        await pg.add_style_tag(content='.site-header{position:static!important} *{animation-play-state:paused!important}')
        n = await pg.evaluate("document.querySelectorAll('.embed iframe').length")
        el = await pg.query_selector(sel)
        await el.scroll_into_view_if_needed()
        await pg.wait_for_timeout(400)
        await el.screenshot(path=out)
        print(out, 'iframes:', n)
        await b.close()

with slot():
    asyncio.run(main())
srv.shutdown()
