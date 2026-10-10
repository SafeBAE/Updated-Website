import os, re, json, glob
from PIL import Image, ImageOps
RAW='/home/claude/raw'; OUT='/home/claude/v3/site/assets/img'
os.makedirs(OUT, exist_ok=True)
def slug(fn):
    b=os.path.basename(fn)
    b=re.sub(r'^\d{4}__\d{2}__','',b)
    b=re.sub(r'\.(jpe?g|png|webp|avif)$','',b,flags=re.I)
    b=b.replace('.jpg','').replace('.jpeg','')
    b=re.sub(r'-scaled|-rotated|_page-0001|-\d+x\d+$','',b)
    b=re.sub(r'[^A-Za-z0-9]+','-',b).strip('-').lower()
    return b[:60]
rules=[
 (r'/yt/', 1280, 74),
 (r'/sp/', 600, 80),
 (r'/us/', 1800, 72),
 (r'(Preview\d|Lesson-|Conclusion|Stats-Marginalized|OffCampus|/2026__07__\d-scaled|13\.-Title)', 1280, 80),
 (r'(poster|Poster|page-0001|no-means-no|baby-consent|relationships|HEALING|Dating-After|Everyone-Can|KnowB4Unude-1|knowb4unude\.png|Untitled-design-2020|what-not-to-say|Image-[345]|Module-One|Guide)', 1000, 80),
 (r'(Headshot|headshot|2025__01__|2025__03__|Adrian-Alie|Alan-Mejia|Armando|Ava-Maldonado|Ava-Ram|Brianna|Cayden|Cyra|David-Zamora|Dolly|Edwinah|Elle-Mone|Isaac-Smith|Isabella-Cabral|Jaclyn|Jada-Davis|Jada-Martinez|Luisa|Mimi-Ndiaye|Molly-Pines|Nick-Nied|Riley-Dev|Skyla|Sophia-Nguyen|Summer-Wilson|Sunny-Bry|Yareli|2026__06__|f9113b|b71bf6|59178f|b0f0eb|36ff73|6585fe|b9338b|35d9e4|7bb97e|AriZ|unnamed|Vanessa_head|9ea5aa|1517523|1735567|82bc85|4cec0c|90fc1a|e28111|8b5afefa|ddaf06be|df8aca6d|caa82df2|Dorie)', 700, 76),
 (r'(logo|Logo|Candid|rini|ChatGPT|Alliance|walogo|header-logo|Phillips|9e3895|637509|RIDOH|NOVA|Blue-and|mahperd|sml-logo|VRLC|nwlc|guardian|Vox|public\.avif|trendwatching|KYIX)', 520, 86),
]
manifest={}
files=[f for f in glob.glob(RAW+'/**/*',recursive=True) if os.path.isfile(f) and re.search(r'\.(jpe?g|png|webp|avif)$',f,re.I)]
for f in sorted(files):
    if 'vc-' in f: continue
    w,q=1600,72
    for pat,ww,qq in rules:
        if re.search(pat,f): w,q=ww,qq; break
    name=slug(f)
    if '/yt/' in f: name='yt-'+name
    if '/sp/' in f: name='sp-'+name
    if '/us/' in f: name='us-'+name
    try:
        im=Image.open(f); im=ImageOps.exif_transpose(im)
        has_alpha = im.mode in ('RGBA','LA','P') and ('transparency' in im.info or im.mode in ('RGBA','LA'))
        im = im.convert('RGBA' if has_alpha else 'RGB')
        if im.width>w: im=im.resize((w,int(im.height*w/im.width)),Image.LANCZOS)
        out=f'{OUT}/{name}.webp'
        im.save(out,'WEBP',quality=q,method=5)
        manifest[name]={'src':os.path.relpath(f,RAW),'w':im.width,'h':im.height,'kb':os.path.getsize(out)//1024}
    except Exception as e:
        print('ERR',f,e)
json.dump(manifest,open('/home/claude/v3/img_manifest.json','w'),indent=0)
tot=sum(v['kb'] for v in manifest.values())
print(len(manifest),'images',tot//1024,'MB')
