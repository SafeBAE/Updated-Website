import sys
from PIL import Image, ImageDraw
# ov2.py out.jpg cols scale page1 page2 ...   (uses shots/<page>_1440.png)
out=sys.argv[1]; cols=int(sys.argv[2]); sc=float(sys.argv[3]); pages=sys.argv[4:]
tiles=[]
for p in pages:
    im=Image.open(f'/home/claude/v4/shots/r/{p}_1440.png'); W,H=im.size
    colh=-(-H//cols); cw=int(W*sc); ch=int(colh*sc)
    c=Image.new('RGB',(cols*cw+(cols-1)*6, ch+22),'white')
    d=ImageDraw.Draw(c); d.text((4,4),p,fill=(200,0,0))
    for i in range(cols):
        part=im.crop((0,i*colh,W,min(H,(i+1)*colh))).convert('RGB')
        part=part.resize((cw,int(part.height*sc)))
        c.paste(part,(i*(cw+6),22))
    tiles.append(c)
w=sum(t.width for t in tiles)+12*(len(tiles)-1); h=max(t.height for t in tiles)
canvas=Image.new('RGB',(w,h),(120,120,120)); x=0
for t in tiles: canvas.paste(t,(x,0)); x+=t.width+12
canvas.save(out,quality=75); print(out, canvas.size)
