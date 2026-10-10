"""Download an Unsplash photo into the site and record its credit.
usage: python3 tools/unsplash.py <image_url> <slug> "<Photographer Name>" <photographer_profile_url> <photo_page_url> [maxw]
- image_url: the photo's urls.regular / urls.raw from the Unsplash search result
- slug: name to use with lib.img('us-<slug>') — the file is saved as assets/img/us-<slug>.webp
Credits are appended to /home/claude/v4/build/credits.jsonl and rendered on credits.html.
"""
import sys, io, json, subprocess, os
from PIL import Image, ImageOps
url, slug, name, prof, page = sys.argv[1:6]
maxw = int(sys.argv[6]) if len(sys.argv) > 6 else 1600
if not slug.startswith('us-'):
    slug = 'us-' + slug
if 'images.unsplash.com' in url and 'w=' not in url:
    url += ('&' if '?' in url else '?') + 'w=2000&q=85&fm=jpg'
data = subprocess.run(['curl', '-sSL', '--max-time', '60', url], capture_output=True, check=True).stdout
im = Image.open(io.BytesIO(data)); im = ImageOps.exif_transpose(im).convert('RGB')
if im.width > maxw:
    im = im.resize((maxw, round(im.height * maxw / im.width)), Image.LANCZOS)
out = f'/home/claude/v4/site/assets/img/{slug}.webp'
im.save(out, 'WEBP', quality=78, method=6)
with open('/home/claude/v4/build/credits.jsonl', 'a') as f:
    f.write(json.dumps({'slug': slug, 'name': name, 'profile': prof, 'page': page}) + '\n')
print(slug, im.size, os.path.getsize(out) // 1024, 'KB')
