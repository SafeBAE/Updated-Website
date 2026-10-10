import potrace, numpy as np, sys
from PIL import Image
src, out, thr, turd, tol, scale = sys.argv[1], sys.argv[2], int(sys.argv[3]), int(sys.argv[4]), float(sys.argv[5]), int(sys.argv[6])
im=Image.open(src).convert('RGBA')
A=im.split()[3].resize((im.width*scale, im.height*scale), Image.LANCZOS)
a=np.array(A)<=thr   # potracer fills False? invert so lines are traced
bm=potrace.Bitmap(~a if '--pos' in sys.argv else a)
pl=bm.trace(turdsize=turd, alphamax=1.2, opticurve=True, opttolerance=tol)
W,H=A.size
r=lambda v: str(int(round(v)))
parts=[]
for c in pl:
    s=c.start_point
    d=f'M{r(s.x)} {r(s.y)}'
    for seg in c.segments:
        if seg.is_corner:
            d+=f'L{r(seg.c.x)} {r(seg.c.y)}L{r(seg.end_point.x)} {r(seg.end_point.y)}'
        else:
            d+=f'C{r(seg.c1.x)} {r(seg.c1.y)} {r(seg.c2.x)} {r(seg.c2.y)} {r(seg.end_point.x)} {r(seg.end_point.y)}'
    parts.append(d+'Z')
svg=f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" fill="currentColor" fill-rule="evenodd"><path d="{"".join(parts)}"/></svg>'
open(out,'w').write(svg); print(len(svg), len(pl))
