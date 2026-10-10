import sys
from PIL import Image
f, x, y, w, h, out = sys.argv[1], *map(int, sys.argv[2:6]), sys.argv[6]
sc = float(sys.argv[7]) if len(sys.argv) > 7 else 1
im = Image.open(f).convert('RGB').crop((x, y, x + w, y + h))
if sc != 1: im = im.resize((int(im.width * sc), int(im.height * sc)))
im.save(out, quality=85); print(out, im.size)
