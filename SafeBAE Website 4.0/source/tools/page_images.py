"""usage: python3 tools/page_images.py <inventory-key>   e.g. about-us__our-team
Prints images from the original page that exist in the new site (manifest slug, size, original alt)."""
import json, re, sys, os
sys.path.insert(0, '/home/claude/tools')
def slug(fn):
    b = os.path.basename(fn.split('?')[0])
    b = re.sub(r'\.(jpe?g|png|webp|avif|gif)$', '', b, flags=re.I)
    b = re.sub(r'-scaled|-rotated|_page-0001|-\d+x\d+$', '', b)
    b = re.sub(r'[^A-Za-z0-9]+', '-', b).strip('-').lower()
    return b
M = json.load(open('/home/claude/v4/img_manifest.json'))
inv = json.load(open('/home/claude/crawl/inventory.json'))
key = sys.argv[1]
seen = set()
for im in inv[key]['images']:
    src = im['src']
    if 'ytimg' in src:
        vid = src.split('/vi/')[1].split('/')[0]
        s = 'yt-' + re.sub(r'[^a-z0-9]+', '-', vid.lower()).strip('-')
    else:
        s = slug(src)
    if s in seen: continue
    seen.add(s)
    ok = s in M or os.path.exists(f'/home/claude/v4/site/assets/img/{s}.webp')
    if ok:
        m = M.get(s, {})
        print(f"{s:60s} {m.get('w','?')}x{m.get('h','?')}  alt={im.get('alt','')!r}")
    else:
        print(f"  (not available) {src}")
