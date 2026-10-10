"""Square, consistently framed headshots for the team page (about builder).
Downloads the original portrait from safebae.org, finds the face, crops a square around it.
usage: python3 work/about_headshots.py   -> writes site/assets/img/hs-<key>.webp, ld-<key>.webp and contact sheets in shots/
Originals are fetched from safebae.org/wp-content/uploads (cached in a scratch folder); faces are found with the
MediaPipe short-range face detector (work/about_blaze_face.tflite); work/about_faces.json holds manual face boxes.
"""
import os, sys, json, subprocess, urllib.parse
import numpy as np
import mediapipe as mp
from PIL import Image, ImageOps, ImageDraw
SCR = '/tmp/claude-0/-home-claude/7affec13-ac9a-536e-9eb2-d4fd932bdfc2/scratchpad'
RAW = SCR + '/dl'; os.makedirs(RAW, exist_ok=True)
IMG = '/home/claude/v4/site/assets/img'
M = json.load(open('/home/claude/v4/img_manifest.json'))
_opts = mp.tasks.vision.FaceDetectorOptions(base_options=mp.tasks.BaseOptions(model_asset_path='/home/claude/v4/work/about_blaze_face.tflite'), min_detection_confidence=0.35)
DET = mp.tasks.vision.FaceDetector.create_from_options(_opts)
PEOPLE = {
 'shael-norris':'82bc8566-88a9-4a05-b13a-f02df3e64af9', 'drew-davis':'4cec0cfb-2d16-47d1-9aaa-8b797dd2ae15',
 'aela-mansmann':'90fc1a20-9104-456b-a0ef-df7f495a3f3f', 'val-odiembo':'e281116a-608f-4812-8e62-40567538668e',
 'bailey-brewer':'b-brewerheadshot', 'miwako-miki':'composite', 'inanna-balkin':'72295171-981d-4bfa-925b-5d7b6ec8e535-1-201-a-1-1',
 'mikayla-murphy':'dsc02351-1', 'ava-legeay':'img-7608-1', 'isa-ocejo':'img-3246', 'jack-quinn':'img-0956',
 'justine-wentzell-chang':'justine-wentzell-chang', 'len-eschweiler':'b71bf627-c760-48ca-9aae-6c43b1867b9c',
 'michelle-hope':'59178f58-dc22-4d34-80cf-5240a08d9304-1', 'dorie-mcnamara':'b0f0eb55-23cd-4dac-89eb-aff4bbc3ed3a',
 'joy-gorman-wettels':'36ff738f-68ee-4dee-8f50-1c70b4b9b011-1', 'arturo-rosado-taveras':'6585feed-8f00-43b2-83b0-5504d57e223c-1',
 'theo-hutt':'b9338b3f-75f1-4457-ab2c-efded5be05f0-1', 'apollo-knapp':'apollo-knapp-headshot', 'torrey-devitto':'35d9e43e-01d6-4059-a4d5-1f8442813ee7-1',
 'hector-jaco':'7bb97e5a-79d6-47d3-b1c4-942e51144247-1', 'ari-zeitlin':'ariz', 'joyce-onana':'unnamed',
 'vanessa-boudewyns':'vanessa-headshot-vanessa-boudewyns', 'samar-rafiqzad':'9ea5aa47-ab94-4190-aa9e-e4aa869eafa8-1',
 'lisa-hoopis':'1517523645026', 'will-rivera':'1735567805828',
}
# manual face boxes (fractions of the image: cx, cy, face height) where detection needs help
MANUAL = json.load(open('/home/claude/v4/work/about_faces.json')) if os.path.exists('/home/claude/v4/work/about_faces.json') else {}

def original(slug):
    m = M.get(slug)
    if m and m.get('src'):
        rel = m['src'].replace('__', '/')
        fn = RAW + '/' + m['src']
        if not (os.path.exists(fn) and os.path.getsize(fn) > 1000):
            url = 'https://www.safebae.org/wp-content/uploads/' + urllib.parse.quote(rel)
            r = subprocess.run(['curl', '-sS', '-L', '--max-time', '90', '-o', fn, '-w', '%{http_code}', url], capture_output=True, text=True)
            if r.stdout.strip() != '200':
                print('  download failed', slug, r.stdout); 
                if os.path.exists(fn): os.remove(fn)
        if os.path.exists(fn):
            try:
                return ImageOps.exif_transpose(Image.open(fn)).convert('RGB')
            except Exception as e:
                print('  bad original', slug, e)
    return Image.open(f'{IMG}/{slug}.webp').convert('RGB')

def face(im, key):
    if key in MANUAL:
        cx, cy, fh = MANUAL[key]; W, H = im.size
        return cx * W, cy * H, fh * H
    W, H = im.size
    best = None
    # try the whole image, then upper-centre crops (the short-range model wants a large face)
    for (ax, ay, aw, ah) in ((0, 0, 1, 1), (.15, 0, .7, .7), (.25, .05, .5, .5), (0, 0, .6, .6), (.4, 0, .6, .6), (.35, .15, .45, .45)):
        x0, y0, cw, ch = int(ax * W), int(ay * H), int(aw * W), int(ah * H)
        c = im.crop((x0, y0, x0 + cw, y0 + ch)); sc = 640 / max(cw, ch); c = c.resize((int(cw * sc), int(ch * sc)))
        r = DET.detect(mp.Image(image_format=mp.ImageFormat.SRGB, data=np.ascontiguousarray(np.array(c))))
        if r.detections:
            d = max(r.detections, key=lambda d: d.bounding_box.width * d.bounding_box.height); b = d.bounding_box
            best = (x0 + b.origin_x / sc, y0 + b.origin_y / sc, b.width / sc, b.height / sc); break
    if best is None: return None
    x, y, w, h = best
    return x + w / 2, y + h / 2, h

rows = []
for key, slug in PEOPLE.items():
    im = original(slug)
    f = face(im, key)
    W, H = im.size
    if f is None:
        print('NO FACE', key, im.size); cx, cy, fh = W / 2, H * .38, min(W, H) * .42
    else:
        cx, cy, fh = f
    S = min(2.5 * fh, W, H)
    x0 = min(max(cx - S / 2, 0), W - S)
    y0 = min(max(cy - S * .46, 0), H - S)
    crop = im.crop((int(x0), int(y0), int(x0 + S), int(y0 + S)))
    out = crop.resize((520, 520), Image.LANCZOS) if S >= 300 else crop.resize((int(max(S, 200)), int(max(S, 200))), Image.LANCZOS)
    out.save(f'{IMG}/hs-{key}.webp', quality=82, method=6)
    rows.append((key, out, im.size, round(S), None if f is None else (round(cx / W, 3), round(cy / H, 3), round(fh / H, 3))))
    print(key, im.size, 'S=', round(S), rows[-1][4])
cols = 7; t = 200
sheet = Image.new('RGB', (cols * t, ((len(rows) + cols - 1) // cols) * (t + 16)), 'white'); d = ImageDraw.Draw(sheet)
for i, (key, out, sz, S, f) in enumerate(rows):
    x = (i % cols) * t; y = (i // cols) * (t + 16)
    sheet.paste(out.resize((t - 4, t - 4)), (x + 2, y + 2)); d.text((x + 4, y + t), f'{key} {S}', fill='black')
    d.line((x + 2, y + 2 + (t - 4) // 2, x + 12, y + 2 + (t - 4) // 2), fill='red')
sheet.save('/home/claude/v4/shots/about-hs-sheet.jpg', quality=80)

# leadership portraits: 4:5 crops with the head at one scale across the four (ld-<key>.webp)
lrows = []
for key in ('shael-norris', 'drew-davis', 'aela-mansmann', 'val-odiembo'):
    im = original(PEOPLE[key]); W, H = im.size
    cx, cy, fh = face(im, key)
    Hc = min(fh / 0.30, H); Wc = Hc * 0.8
    if Wc > W: Wc = W; Hc = Wc / 0.8
    x0 = min(max(cx - Wc / 2, 0), W - Wc); y0 = min(max(cy - Hc * .42, 0), H - Hc)
    crop = im.crop((int(x0), int(y0), int(x0 + Wc), int(y0 + Hc)))
    w = int(min(900, Wc)); out = crop.resize((w, int(w / 0.8)), Image.LANCZOS)
    out.save(f'{IMG}/ld-{key}.webp', quality=82, method=6); lrows.append(out)
    print('ld', key, out.size, 'head', round(fh / Hc, 2))
sheet = Image.new('RGB', (4 * 240, 300), 'white')
for i, o in enumerate(lrows): sheet.paste(o.resize((236, 295)), (i * 240 + 2, 2))
sheet.save('/home/claude/v4/shots/about-ld-sheet.jpg', quality=80)
