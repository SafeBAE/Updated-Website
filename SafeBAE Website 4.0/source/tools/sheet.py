import sys, os, glob
from PIL import Image, ImageDraw, ImageFont, ImageOps
files = sys.argv[3:]
out = sys.argv[1]; cols=int(sys.argv[2])
tw, th = 300, 210
rows = (len(files)+cols-1)//cols
sheet = Image.new('RGB', (cols*tw, rows*(th+18)), 'white')
d = ImageDraw.Draw(sheet)
for i,f in enumerate(files):
    try:
        im = Image.open(f); im = ImageOps.exif_transpose(im).convert('RGB')
        im.thumbnail((tw-6, th-6))
        x=(i%cols)*tw; y=(i//cols)*(th+18)
        sheet.paste(im,(x+3+(tw-6-im.width)//2,y+3))
        d.text((x+4,y+th+2), f"{i}: {os.path.basename(f)[-38:]}", fill='black')
    except Exception as e:
        print('ERR', f, e)
sheet.save(out, quality=72)
print(out, sheet.size)
