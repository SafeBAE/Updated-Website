import sys
from PIL import Image
# slice a tall screenshot into chunks for viewing; scale to width
f=sys.argv[1]; h=int(sys.argv[2]) if len(sys.argv)>2 else 1800; scale=float(sys.argv[3]) if len(sys.argv)>3 else 0.5
im=Image.open(f); n=0
for y in range(0, im.height, h):
    c=im.crop((0,y,im.width,min(im.height,y+h)))
    c=c.resize((int(c.width*scale), int(c.height*scale)))
    o=f.replace('.png',f'_s{n}.jpg'); c.convert('RGB').save(o,quality=72); print(o, c.size); n+=1
