import sys
from PIL import Image
# ov.py shot.png out.jpg [cols] [colh_px_source] [scale]
f=sys.argv[1]; out=sys.argv[2]; cols=int(sys.argv[3]) if len(sys.argv)>3 else 4
im=Image.open(f); W,H=im.size
colh=int(sys.argv[4]) if len(sys.argv)>4 and int(sys.argv[4])>0 else -(-H//cols)
sc=float(sys.argv[5]) if len(sys.argv)>5 else 0.3
n=-(-H//colh)
cw=int(W*sc); ch=int(colh*sc)
canvas=Image.new('RGB',(n*cw+(n-1)*8, ch),'white')
for i in range(n):
    c=im.crop((0,i*colh,W,min(H,(i+1)*colh))).resize((cw,int(min(colh,H-i*colh)*sc)))
    canvas.paste(c.convert('RGB'),(i*(cw+8),0))
canvas.save(out,quality=78); print(out, canvas.size)
