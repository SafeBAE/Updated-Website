import sys, numpy as np, potrace
from PIL import Image
src, out, w = sys.argv[1], sys.argv[2], int(sys.argv[3])
im = Image.open(src).convert('RGBA')
bb = im.getbbox(); im = im.crop(bb)
r = w / im.width; im = im.resize((w, int(im.height*r)), Image.LANCZOS)
a = ~(np.array(im)[:,:,3] > 128)
bm = potrace.Bitmap(a)
path = bm.trace(turdsize=4, alphamax=1.0, opticurve=True, opttolerance=0.3)
parts=[]
for curve in path:
    s = curve.start_point
    d = [f"M{s.x:.1f},{s.y:.1f}"]
    for seg in curve.segments:
        if seg.is_corner:
            d.append(f"L{seg.c.x:.1f},{seg.c.y:.1f}L{seg.end_point.x:.1f},{seg.end_point.y:.1f}")
        else:
            d.append(f"C{seg.c1.x:.1f},{seg.c1.y:.1f} {seg.c2.x:.1f},{seg.c2.y:.1f} {seg.end_point.x:.1f},{seg.end_point.y:.1f}")
    d.append('Z'); parts.append(''.join(d))
svg = f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {im.width} {im.height}" fill="currentColor" fill-rule="evenodd"><path d="{" ".join(parts)}"/></svg>'
open(out,'w').write(svg); print(out, len(svg), im.size)
