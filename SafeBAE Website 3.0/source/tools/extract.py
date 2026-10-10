import json,re,os,sys,glob
from bs4 import BeautifulSoup
from markdownify import markdownify as md
base='/home/claude/crawl'
out={}
def imgs_of(el):
    res=[]
    for im in el.find_all('img'):
        src=im.get('data-src') or im.get('data-lazy-src') or im.get('src') or ''
        srcset=im.get('data-srcset') or im.get('srcset') or ''
        if src.startswith('data:') and srcset: src=srcset.split(',')[-1].strip().split(' ')[0]
        res.append({'src':src,'alt':im.get('alt',''),'w':im.get('width'),'h':im.get('height')})
    for e in el.find_all(style=True):
        for m in re.findall(r'url\(([^)]+)\)', e['style']):
            res.append({'src':m.strip('\'" '),'alt':'(bg)'})
    for e in el.find_all(attrs={'data-ultimate-bg':True}):
        for m in re.findall(r'url\(([^)]+)\)', e['data-ultimate-bg']):
            res.append({'src':m.strip('\'" '),'alt':'(ult-bg)'})
    return res
for f in sorted(glob.glob(base+'/pages/*.html')):
    slug=os.path.basename(f)[:-5]
    s=BeautifulSoup(open(f,encoding='utf-8',errors='ignore').read(),'lxml')
    content=s.find(id='content') or s.body
    # strip scripts/styles
    for t in content.find_all(['script','noscript']): t.decompose()
    styles=[st.get_text() for st in content.find_all('style')]
    for t in content.find_all('style'): t.decompose()
    iframes=[{'src':i.get('src') or i.get('data-src'),'title':i.get('title')} for i in content.find_all('iframe')]
    videos=[{'src':v.get('src') or (v.find('source').get('src') if v.find('source') else None),'poster':v.get('poster')} for v in content.find_all('video')]
    links=[]
    for a in content.find_all('a',href=True):
        links.append({'href':a['href'],'text':a.get_text(' ',strip=True)[:120]})
    text=md(str(content),heading_style='ATX',strip=['img'])
    text=re.sub(r'\n{3,}','\n\n',text)
    meta={}
    for m in s.find_all('meta'):
        if m.get('name') in ('description',) or (m.get('property') or '').startswith('og:'):
            meta[m.get('name') or m.get('property')]=m.get('content')
    out[slug]={'title':(s.title.string if s.title else ''),'meta':meta,'images':imgs_of(content),'iframes':iframes,'videos':videos,'links':links,'md':text}
    os.makedirs(base+'/md',exist_ok=True)
    open(base+f'/md/{slug}.md','w').write(f"# {out[slug]['title']}\n\nMETA: {json.dumps(meta)}\n\nIFRAMES: {json.dumps(iframes,indent=0)}\n\nVIDEOS: {json.dumps(videos)}\n\n"+text)
json.dump(out,open(base+'/inventory.json','w'),indent=1)
for k,v in out.items():
    print(f"{k:60s} md={len(v['md']):6d} img={len(v['images']):3d} ifr={len(v['iframes']):2d} links={len(v['links'])}")
