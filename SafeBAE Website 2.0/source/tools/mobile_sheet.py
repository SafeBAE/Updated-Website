"""Tile a tall mobile screenshot into side-by-side columns. usage: mobile_sheet.py shot.png [colh=2400] [scale=0.5] [cols=4]"""
import sys
from PIL import Image
f=sys.argv[1]; colh=int(sys.argv[2]) if len(sys.argv)>2 else 2400; sc=float(sys.argv[3]) if len(sys.argv)>3 else .5; cols=int(sys.argv[4]) if len(sys.argv)>4 else 4
im=Image.open(f).convert('RGB'); n=0; pieces=[im.crop((0,y,im.width,min(im.height,y+colh))) for y in range(0,im.height,colh)]
for s in range(0,len(pieces),cols):
    grp=pieces[s:s+cols]; W=im.width; out=Image.new('RGB',(W*len(grp)+12*(len(grp)-1),colh),(40,40,40))
    for i,p in enumerate(grp): out.paste(p,(i*(W+12),0))
    out=out.resize((int(out.width*sc),int(out.height*sc))); o=f.replace('.png',f'_m{n}.jpg'); out.save(o,quality=70); print(o,out.size); n+=1
