"""Site-wide QA: static link/asset check + browser overflow/console check.
usage: python3 tools/check.py [static|browser|all] [page ...]"""
import sys, os, glob, re, asyncio
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _sem import slot
from bs4 import BeautifulSoup
SITE = '/home/claude/v3/site'
mode = sys.argv[1] if len(sys.argv) > 1 else 'all'
pages = sys.argv[2:] or sorted(os.path.basename(p) for p in glob.glob(f'{SITE}/*.html'))

def static():
    ids = {}
    soups = {}
    for p in pages:
        s = BeautifulSoup(open(f'{SITE}/{p}', encoding='utf-8').read(), 'html.parser')
        soups[p] = s
        ids[p] = {t['id'] for t in s.find_all(attrs={'id': True})}
        dup = [i for i in ids[p] if len(s.find_all(attrs={'id': i})) > 1]
        if dup: print(f'{p}: duplicate ids {dup[:6]}')
    allpages = {os.path.basename(x) for x in glob.glob(f'{SITE}/*.html')}
    for p, s in soups.items():
        for a in s.find_all('a', href=True):
            h = a['href']
            if re.match(r'^(https?:|mailto:|tel:|sms:|javascript:)', h): continue
            if h.startswith('#'):
                if len(h) > 1 and h[1:] not in ids[p] and not h[1:].startswith(('tab-',)):
                    # tabs may be addressed by suffix
                    if not any(i == 'tab-' + h[1:] for i in ids[p]):
                        print(f'{p}: missing anchor {h}')
                continue
            f, _, frag = h.partition('#')
            if f not in allpages:
                print(f'{p}: broken link {h}'); continue
            if frag and f in ids and frag not in ids[f] and ('tab-' + frag) not in ids[f]:
                print(f'{p}: missing anchor {h}')
        for im in s.find_all(['img', 'source']):
            src = im.get('src') or ''
            if src and not src.startswith(('http', 'data:')) and not os.path.exists(f'{SITE}/{src}'):
                print(f'{p}: missing image {src}')
        for st in s.find_all(style=True):
            for u in re.findall(r"url\(['\"]?([^'\")]+)", st['style']):
                if not u.startswith(('http', 'data:')) and not os.path.exists(f'{SITE}/{u}'):
                    print(f'{p}: missing bg image {u}')

async def browser():
    from playwright.async_api import async_playwright
    async with async_playwright() as pw:
        b = await pw.chromium.launch(args=['--allow-file-access-from-files'])
        for w in (360, 400, 1440):
            pg = await b.new_page(viewport={'width': w, 'height': 900})
            msgs = []
            pg.on('console', lambda m: msgs.append(f'{m.type}: {m.text}') if m.type == 'error' else None)
            pg.on('pageerror', lambda e: msgs.append(f'PAGEERROR: {e}'))
            for p in pages:
                msgs.clear()
                await pg.goto(f'file://{SITE}/{p}', wait_until='load', timeout=60000)
                await pg.wait_for_timeout(250)
                sw = await pg.evaluate('document.documentElement.scrollWidth')
                culprits = []
                if sw > w:
                    culprits = await pg.evaluate(f'''(()=>{{const W={w};const out=[];document.querySelectorAll('main *, footer *, header *').forEach(el=>{{const r=el.getBoundingClientRect(); if(r.right>W+1 && r.width>0){{ let p=el.parentElement, clipped=false; while(p){{ const cs=getComputedStyle(p); if(/(hidden|auto|scroll|clip)/.test(cs.overflowX)){{ const pr=p.getBoundingClientRect(); if(pr.right<=W+1){{clipped=true;break;}} }} p=p.parentElement; }} if(!clipped) out.push((el.className&&el.className.baseVal===undefined?el.className:el.tagName)+' r='+Math.round(r.right)); }} }}); return out.slice(0,6); }})()''')
                if sw > w or msgs:
                    print(f'[{w}] {p}: scrollWidth={sw} {culprits} {msgs[:4]}')
            await pg.close()
        await b.close()

if mode in ('static', 'all'): static()
if mode in ('browser', 'all'):
    with slot():
        asyncio.run(browser())
print('check done')
