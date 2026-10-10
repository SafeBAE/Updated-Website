"""Layout audit for one page: flags the things Drew calls out (blank zones, lopsided rows,
boxes that don't end level, orphan cards, narrow subtitles, tiny text).

usage: python3 tools/audit.py page.html [width=1440]
Writes shots/<page>_<w>_audit.jpg (the page as column strips, flagged zones boxed in coral and
numbered) and prints one line per finding. Findings are leads, not verdicts: look at each one.
"""
import sys, os, asyncio, json
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _sem import slot
from playwright.async_api import async_playwright
import numpy as np
from PIL import Image, ImageDraw, ImageFont

SITE = '/home/claude/v3/site'
pagef = sys.argv[1]
W = int(sys.argv[2]) if len(sys.argv) > 2 else 1440

DOM_JS = r'''
() => {
  const out = [];
  const main = document.querySelector('main');
  const path = el => { const p = []; let e = el; for (let i = 0; e && e !== main && i < 3; i++, e = e.parentElement) { p.unshift(e.tagName.toLowerCase() + (e.id ? '#' + e.id : '') + (e.classList.length ? '.' + [...e.classList].slice(0, 2).join('.') : '')); } return p.join(' > '); };
  const vis = el => { const r = el.getBoundingClientRect(); const cs = getComputedStyle(el); return r.width > 8 && r.height > 8 && cs.visibility !== 'hidden' && cs.display !== 'none' && cs.position !== 'absolute' && cs.position !== 'fixed'; };
  const boxy = el => { const cs = getComputedStyle(el); const bg = cs.backgroundColor; const hasBg = bg && bg !== 'rgba(0, 0, 0, 0)' && bg !== 'transparent'; return hasBg || parseFloat(cs.borderTopWidth) > 0 || cs.boxShadow !== 'none' || cs.backgroundImage !== 'none' || el.tagName === 'IMG' || el.tagName === 'FIGURE'; };
  const hidden = el => { let e = el; while (e && e !== document.body) { const cs = getComputedStyle(e); if (cs.display === 'none' || cs.visibility === 'hidden' || e.hidden) return true; e = e.parentElement; } return false; };
  const Y = r => Math.round(r.top + scrollY);
  main.querySelectorAll('*').forEach(el => {
    if (hidden(el)) return;
    const cs = getComputedStyle(el);
    const isGrid = cs.display.includes('grid'), isFlex = cs.display.includes('flex');
    if (!isGrid && !isFlex) return;
    if (isFlex && cs.flexDirection.startsWith('column')) return;
    const kids = [...el.children].filter(vis).map(k => ({ k, r: k.getBoundingClientRect() })).filter(o => o.r.height > 70);
    if (kids.length < 2) return;
    const er = el.getBoundingClientRect();
    if (er.width < 420) return;
    // rows by top edge
    const rows = [];
    kids.forEach(o => { let row = rows.find(R => Math.abs(R.top - o.r.top) < 8); if (!row) { row = { top: o.r.top, items: [] }; rows.push(row); } row.items.push(o); });
    rows.sort((a, b) => a.top - b.top);
    const ws = kids.map(o => o.r.width), wmin = Math.min(...ws), wmax = Math.max(...ws);
    const uniform = wmax - wmin < wmax * 0.09;
    if (uniform && rows.length > 1 && rows[0].items.length > 1) {
      const last = rows[rows.length - 1].items.length, first = rows[0].items.length;
      if (last < first) out.push({ t: 'ORPHAN', y: Y(er), y2: Y(er) + Math.round(er.height), x: er.left, x2: er.right, msg: `${kids.length} items in rows of ${first}; last row has ${last}`, el: path(el) });
    }
    const rowInfo = [];
    rows.forEach(row => {
      if (row.items.length < 2) return;
      row.items.sort((p, q) => p.r.left - q.r.left);
      const bots = row.items.map(o => o.r.bottom), hs = row.items.map(o => o.r.height);
      const dB = Math.max(...bots) - Math.min(...bots), hMax = Math.max(...hs), hMin = Math.min(...hs);
      const allBoxy = row.items.every(o => boxy(o.k));
      const y = Y({ top: row.top }), y2 = Math.round(Math.max(...bots) + scrollY);
      if (allBoxy && dB > 10) out.push({ t: 'UNLEVEL', y, y2, x: er.left, x2: er.right, msg: `side-by-side boxes end ${Math.round(dB)}px apart`, el: path(el) });
      else if (!allBoxy && hMax - hMin > 170 && hMin < hMax * 0.62) out.push({ t: 'LOPSIDED', y, y2, x: er.left, x2: er.right, msg: `columns are ${Math.round(hMin)}px and ${Math.round(hMax)}px tall`, el: path(el) });
      if (allBoxy) {
        const L = row.items[0].r.left, R = row.items[row.items.length - 1].r.right, mid = (L + R) / 2;
        const gut = []; for (let i = 0; i < row.items.length - 1; i++) gut.push((row.items[i].r.right + row.items[i + 1].r.left) / 2);
        const sym = gut.every(gx => gut.some(hx => Math.abs((2 * mid - gx) - hx) < 14));
        const rw = row.items.map(o => Math.round(o.r.width));
        if (!sym) out.push({ t: 'ASYM', y, y2, x: er.left, x2: er.right, msg: `row of boxes with unequal widths (${rw.join(' / ')}px); check it is a deliberate feature layout`, el: path(el) });
        rowInfo.push({ y, y2, gut, sym });
        const bgs = new Set(row.items.map(o => getComputedStyle(o.k).backgroundColor));
        if (bgs.size >= 3) out.push({ t: 'MIXED', y, y2, x: er.left, x2: er.right, msg: `${bgs.size} different box backgrounds side by side`, el: path(el) });
      }
    });
    for (let i = 0; i < rowInfo.length - 1; i++) {
      const A = rowInfo[i], B = rowInfo[i + 1];
      if (B.y - A.y2 > 60) continue;
      const sub = (P, Q) => P.every(gx => Q.some(hx => Math.abs(gx - hx) < 12));
      if (!(sub(A.gut, B.gut) || sub(B.gut, A.gut)) && !(A.sym && B.sym)) out.push({ t: 'MISALIGN', y: A.y, y2: B.y2, x: er.left, x2: er.right, msg: 'stacked rows whose column lines do not line up', el: path(el) });
    }
  });
  // hollow boxes: a card with a tall empty band inside it (above, between or below its content)
  main.querySelectorAll('*').forEach(el => {
    if (hidden(el) || !vis(el) || !boxy(el)) return;
    const r = el.getBoundingClientRect(); if (r.height < 190 || r.width < 200 || r.width > innerWidth * 0.98) return;
    const cs = getComputedStyle(el); if (cs.backgroundImage !== 'none' && cs.backgroundImage.includes('url(')) return;
    if (el.querySelector(':scope > img, :scope > picture') && cs.position !== 'static' && el.children.length < 3) return;
    const iv = [];
    const tw2 = document.createTreeWalker(el, NodeFilter.SHOW_TEXT); let tn;
    while ((tn = tw2.nextNode())) { if (!tn.textContent.trim()) continue; if (hidden(tn.parentElement)) continue; const rg = document.createRange(); rg.selectNodeContents(tn); for (const q of rg.getClientRects()) if (q.width > 1 && q.height > 1) iv.push([q.top, q.bottom]); }
    el.querySelectorAll('img,svg,video,iframe,input,textarea,select,button,canvas,[class*="btn"],[role="img"]').forEach(c => { if (hidden(c)) return; const q = c.getBoundingClientRect(); if (q.width > 4 && q.height > 4) iv.push([q.top, q.bottom]); });
    el.querySelectorAll('*').forEach(c => { if (c.children.length || hidden(c)) return; const k = getComputedStyle(c); if ((k.backgroundColor !== 'rgba(0, 0, 0, 0)' || k.backgroundImage !== 'none') ) { const q = c.getBoundingClientRect(); if (q.width > 12 && q.height > 12) iv.push([q.top, q.bottom]); } });
    if (iv.length < 2) return;
    iv.sort((p, q) => p[0] - q[0]);
    const pt = parseFloat(cs.paddingTop) || 0, pb = parseFloat(cs.paddingBottom) || 0;
    let cur = r.top + pt, best = 0, where = '';
    iv.forEach(([t0, b0]) => { if (t0 - cur > best) { best = t0 - cur; where = cur <= r.top + pt + 1 ? 'at the top' : 'in the middle'; } cur = Math.max(cur, b0); });
    if (r.bottom - pb - cur > best) { best = r.bottom - pb - cur; where = 'at the bottom'; }
    if (best > 76 && best > r.height * 0.17) out.push({ t: 'HOLLOW', y: Y(r), y2: Y(r) + Math.round(r.height), x: r.left, x2: r.right, msg: `box has a ${Math.round(best)}px blank band ${where}`, el: path(el) });
  });
  // narrow subtitles
  main.querySelectorAll('.lede, h1 + p, h2 + p').forEach(el => {
    if (hidden(el) || !vis(el)) return;
    const r = el.getBoundingClientRect(), pr = el.parentElement.getBoundingClientRect(), pcs = getComputedStyle(el.parentElement);
    const inner = pr.width - parseFloat(pcs.paddingLeft) - parseFloat(pcs.paddingRight);
    const cs = getComputedStyle(el); const capped = cs.maxWidth !== 'none' && parseFloat(cs.maxWidth) < inner - 4;
    const rng = document.createRange(); rng.selectNodeContents(el); const lines = rng.getClientRects().length;
    if (inner > 640 && capped && lines > 1 && r.width < inner * 0.86) out.push({ t: 'NARROW', y: Y(r), y2: Y(r) + Math.round(r.height), x: r.left, x2: pr.right, msg: `subtitle is ${Math.round(r.width)}px in a ${Math.round(inner)}px column (max-width cap)`, el: path(el) });
  });
  // tiny running text
  const tiny = {};
  const tw = document.createTreeWalker(main, NodeFilter.SHOW_TEXT);
  let n; while ((n = tw.nextNode())) { const t = n.textContent.trim(); if (t.length < 24) continue; const el = n.parentElement; if (hidden(el) || !vis(el)) continue; const cs = getComputedStyle(el); const fs = parseFloat(cs.fontSize); if (fs < 13 && cs.textTransform !== 'uppercase') { const k = path(el); (tiny[k] = tiny[k] || { fs, n: 0, y: Y(el.getBoundingClientRect()) }).n++; } }
  Object.entries(tiny).slice(0, 14).forEach(([k, v]) => out.push({ t: 'TINY', y: v.y, y2: v.y + 20, x: 0, x2: 0, msg: `${v.n} text block(s) at ${v.fs}px`, el: k }));
  const secs = [...main.children].filter(vis).map(s => { const r = s.getBoundingClientRect(); return { y: Y(r), y2: Y(r) + Math.round(r.height), el: path(s), bg: getComputedStyle(s).backgroundColor }; });
  const wrap = main.querySelector('.wrap'); const wr = wrap ? wrap.getBoundingClientRect() : { left: 40, right: innerWidth - 40 }; const wcs = wrap ? getComputedStyle(wrap) : null;
  return { out, secs, wl: wr.left + (wcs ? parseFloat(wcs.paddingLeft) : 0), wr: wr.right - (wcs ? parseFloat(wcs.paddingRight) : 0), H: document.documentElement.scrollHeight };
}
'''


async def grab():
    async with async_playwright() as p:
        b = await p.chromium.launch(args=['--allow-file-access-from-files'])
        pg = await b.new_page(viewport={'width': W, 'height': 900})
        await pg.goto(f'file://{SITE}/{pagef}', wait_until='networkidle', timeout=60000)
        await pg.evaluate("document.querySelectorAll('img[loading=lazy]').forEach(i=>{i.loading='eager'; const s=i.src; i.src=''; i.src=s;})")
        await pg.wait_for_timeout(900)
        h = await pg.evaluate('document.body.scrollHeight'); y = 0
        while y < h:
            await pg.evaluate(f'window.scrollTo(0,{y})'); await pg.wait_for_timeout(90); y += 800
            h = await pg.evaluate('document.body.scrollHeight')
        await pg.evaluate("document.querySelectorAll('.reveal').forEach(e=>{e.classList.remove('pre');e.classList.add('in')})")
        await pg.evaluate("Promise.race([Promise.all([...document.images].map(i=>i.decode().catch(()=>0))), new Promise(r=>setTimeout(r,12000))])")
        await pg.evaluate('window.scrollTo(0,0)'); await pg.wait_for_timeout(900)
        await pg.add_style_tag(content='*{animation-play-state:paused!important}')
        data = await pg.evaluate(DOM_JS)
        png = f'/home/claude/v3/shots/_audit_{os.getpid()}.png'
        await pg.screenshot(path=png, full_page=True)
        await b.close()
        return data, png

with slot():
    data, png = asyncio.run(grab())

im = Image.open(png).convert('RGB'); os.remove(png)
g = np.asarray(im.convert('L'), dtype=np.int16)
H = g.shape[0]
wl, wr = int(max(0, data['wl'])), int(min(W, data['wr']))
finds = list(data['out'])
main_secs = data['secs']
y_main0 = main_secs[0]['y'] if main_secs else 0
y_main1 = main_secs[-1]['y2'] if main_secs else H


def sec_of(y):
    for s in main_secs:
        if s['y'] <= y < s['y2']:
            return s['el']
    return ''

if W >= 900 and wr - wl > 600:
    # pixel pass: split the content width into 6 cells; a cell-row is "busy" if it has contrast
    NC = 6; edges = np.linspace(wl, wr, NC + 1).astype(int)
    busy = np.zeros((H, NC), dtype=bool)
    for c in range(NC):
        cell = g[:, edges[c]:edges[c + 1]]
        busy[:, c] = (cell.max(axis=1) - cell.min(axis=1)) > 34
    k = 9  # close small gaps (line spacing) so text blocks read as solid
    for c in range(NC):
        col = busy[:, c].astype(np.int32); cs = np.cumsum(np.concatenate([[0], col]))
        win = cs[np.minimum(H, np.arange(H) + k)] - cs[np.maximum(0, np.arange(H) - k)]
        busy[:, c] = win > 0
    any_busy = busy.any(axis=1)
    rowmean = g[:, wl:wr].mean(axis=1)
    step = np.abs(np.diff(rowmean, prepend=rowmean[0])) > 4   # a background change ends a blank run

    def runs(mask, minlen):
        res = []; start = None
        for y in range(len(mask)):
            if mask[y] and start is None: start = y
            elif not mask[y] and start is not None:
                if y - start >= minlen: res.append((start, y))
                start = None
        if start is not None and len(mask) - start >= minlen: res.append((start, len(mask)))
        return res
    # full-width blank bands
    for a, b in runs(~any_busy & ~step, 150):
        if b <= y_main0 or a >= y_main1: continue
        finds.append({'t': 'GAP', 'y': a, 'y2': b, 'x': wl, 'x2': wr, 'msg': f'{b - a}px with nothing in it', 'el': sec_of((a + b) // 2)})
    # dead zones: a third of the width blank while the rest of the row has content
    for c0, c1, name in [(0, 2, 'left third'), (2, 4, 'middle third'), (4, 6, 'right third'), (3, 6, 'right half'), (0, 3, 'left half')]:
        blank = ~busy[:, c0:c1].any(axis=1)
        others = np.delete(busy, np.s_[c0:c1], axis=1).any(axis=1)
        for a, b in runs(blank & others, 210):
            if b <= y_main0 or a >= y_main1: continue
            if any(f['t'] == 'DEAD' and abs(f['y'] - a) < 60 and abs(f['y2'] - b) < 60 for f in finds): continue
            finds.append({'t': 'DEAD', 'y': a, 'y2': b, 'x': int(edges[c0]), 'x2': int(edges[c1]), 'msg': f'{name} is empty for {b - a}px beside content', 'el': sec_of((a + b) // 2)})

# adjacent sections with the same background
for s1, s2 in zip(main_secs, main_secs[1:]):
    if s1['bg'] == s2['bg'] and s1['bg'] not in ('rgba(0, 0, 0, 0)',):
        finds.append({'t': 'SAMEBG', 'y': s2['y'] - 40, 'y2': s2['y'] + 40, 'x': 0, 'x2': W, 'msg': f'two sections in a row share background {s1["bg"]}', 'el': s1['el'] + '  |  ' + s2['el']})

finds.sort(key=lambda f: (f['y'], f['t']))
# annotate
d = ImageDraw.Draw(im)
try: font = ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf', 30)
except Exception: font = ImageFont.load_default()
for i, f in enumerate(finds):
    if f['t'] == 'TINY': continue
    if f['x2'] - f['x'] < 4: continue
    x0, x1 = (f['x'], f['x2']) if f['x2'] > f['x'] else (wl, wr)
    col = (254, 113, 113) if f['t'] in ('GAP', 'DEAD', 'HOLLOW') else (255, 180, 0)
    for o in range(4): d.rectangle([x0 + o, f['y'] + o, x1 - o, f['y2'] - o], outline=col)
    d.rectangle([x0, f['y'], x0 + 62, f['y'] + 40], fill=col); d.text((x0 + 8, f['y'] + 3), str(i + 1), fill=(13, 13, 13), font=font)
colh = 3400; pieces = [im.crop((0, y, W, min(H, y + colh))) for y in range(0, H, colh)]
sc = min(0.34, 1900 / (len(pieces) * (W + 12)))
sheet = Image.new('RGB', (W * len(pieces) + 12 * (len(pieces) - 1), colh), (40, 40, 40))
for i, pc in enumerate(pieces): sheet.paste(pc, (i * (W + 12), 0))
sheet = sheet.resize((int(sheet.width * sc), int(sheet.height * sc)))
outp = f'/home/claude/v3/shots/{pagef.replace(".html", "")}_{W}_audit.jpg'
sheet.save(outp, quality=74)
print(f'{pagef} @ {W}: {len(finds)} finding(s). Annotated overview: {outp}  (page height {H}px)')
for i, f in enumerate(finds):
    print(f'{i + 1:>2}. {f["t"]:<8} y={f["y"]}-{f["y2"]}  {f["msg"]}   [{f["el"]}]')
