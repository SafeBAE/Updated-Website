"""Generate site/assets/js/search-index.js from the built pages + library + hotlines."""
import os, re, json, html, glob, sys
sys.path.insert(0, '/home/claude/v2/build')
from bs4 import BeautifulSoup
import data, lib

SITE = lib.SITE
SKIP = {'credits.html'}
FEATURED = {'vibe-check.html': 9, 'peer-educator.html': 8, 'library.html': 8, 'survivor-support.html': 8, 'title-ix.html': 6,
            'request-a-program.html': 6, 'clubs.html': 5, 'resources.html': 5, 'faq.html': 4, 'donate.html': 4,
            'ai-literacy.html': 8, 'choking-hazard.html': 8, 'fordaisy-tattoos.html': 6, 'fordaisy.html': 5}
CATS = [('film-', 'Film'), ('360', 'Schools'), ('consent-curriculum', 'Schools'), ('professional-development', 'Schools'),
        ('policy-reform-guide', 'Schools'), ('accountability-training', 'Schools')]


def e(s):
    return html.escape(re.sub(r'\s+', ' ', s or '').strip(), quote=False)


def clip(s, n=150):
    s = re.sub(r'\s+', ' ', s or '').strip()
    return s if len(s) <= n else s[:n].rsplit(' ', 1)[0] + '…'


def page_cat(fn):
    for p, c in CATS:
        if fn.startswith(p):
            return c
    return 'Page'


def build():
    items, seen = [], set()

    def add(t, d, u, c, k='', w=0, f=0):
        key = (t.lower(), u)
        if key in seen or not t:
            return
        seen.add(key)
        it = {'t': e(t), 'd': e(clip(d)), 'u': u, 'c': c}
        if k: it['k'] = e(k)[:400]
        if w: it['w'] = w
        if f: it['f'] = 1
        items.append(it)

    for path in sorted(glob.glob(f'{SITE}/*.html')):
        fn = os.path.basename(path)
        if fn in SKIP:
            continue
        soup = BeautifulSoup(open(path, encoding='utf-8').read(), 'html.parser')
        main = soup.find('main') or soup
        title = (soup.title.string if soup.title else fn).split('|')[0].split(' – ')[0].split(' - SafeBAE')[0].strip()
        desc = (soup.find('meta', attrs={'name': 'description'}) or {}).get('content', '')
        heads = [h.get_text(' ', strip=True) for h in main.find_all(['h2', 'h3'])]
        h1 = main.find('h1')
        ptitle = title if fn != 'index.html' else 'SafeBAE home'
        add(ptitle, desc, fn, page_cat(fn), k=' '.join([h1.get_text(' ', strip=True) if h1 else ''] + heads),
            w=FEATURED.get(fn, 2), f=1 if fn in FEATURED and FEATURED[fn] >= 5 else 0)
        # sections with ids
        for sec in main.find_all(attrs={'id': True}):
            sid = sec['id']
            if sid in ('main', 'top') or sid.startswith(('tab-', 'panel-')):
                continue
            if sec.name == 'details':
                sm = sec.find('summary')
                if not sm:
                    continue
                q = sm.get_text(' ', strip=True)
                ans = ' '.join(x.get_text(' ', strip=True) for x in sec.find_all(['p', 'li'])[:3])
                add(q, ans, f'{fn}#{sid}', 'Answer' if fn == 'faq.html' else 'Section', w=1)
                continue
            if sec.name not in ('section', 'div', 'article'):
                continue
            h = sec.find(['h2', 'h3'])
            if not h:
                continue
            ht = h.get_text(' ', strip=True)
            if len(ht) < 4 or len(ht) > 90:
                continue
            p = sec.find('p')
            add(ht, p.get_text(' ', strip=True) if p else '', f'{fn}#{sid}', 'Section', k=title)

    kind_label = {'film': 'Film', 'video': 'Video', 'podcast': 'Podcast', 'guide': 'Guide'}
    for it in data.library_items():
        u = it.get('href') or 'library.html'
        add(it['title'], it.get('desc', ''), u, kind_label.get(it['kind'], 'Library'),
            k=' '.join(it.get('topics', [])) + ' ' + it.get('kw', '') + ' ' + (it.get('sub') or ''), w=3 if it['kind'] == 'film' else 1)

    for n, sub, num, d, u in lib.HOTLINES:
        add(n, f'{sub} · {num}', 'survivor-support.html#hotlines', 'Hotline', k=d + ' help crisis support hotline', w=4)

    extra = [
        ('BAE Skills Lab', 'Short interactive activities about consent, boundaries and healthy relationships.', 'https://skills-lab.safebae.org/', 'Tool', 'games practice activities consent', 4),
        ('Vibe Check (checkyourvibe.org)', 'Free, anonymous reflection tool for anyone worried they crossed a line.', 'https://checkyourvibe.org/', 'Tool', 'accountability harm boundary crossed a line', 6),
        ('Club Hub', 'Members-only hub for SafeBAE club leaders.', 'https://clubs.safebae.org', 'Tool', 'club chapter leaders', 2),
        ('SafeBAE on Substack', 'Newsletter and long-form posts.', 'https://substack.com/@safebae', 'Newsletter', 'newsletter subscribe', 1),
        ('Shop educational products', 'Licensed trainings, guides and curricula on Podia.', 'https://safebae.podia.com/', 'Shop', 'buy purchase license', 1),
    ]
    for t, d, u, c, k, w in extra:
        add(t, d, u, c, k=k, w=w)

    out = f'{SITE}/assets/js/search-index.js'
    with open(out, 'w', encoding='utf-8') as fh:
        fh.write('window.SB_SEARCH=' + json.dumps(items, ensure_ascii=False, separators=(',', ':')) + ';\n')
    print('search index:', len(items), 'items', os.path.getsize(out) // 1024, 'KB')


if __name__ == '__main__':
    build()
