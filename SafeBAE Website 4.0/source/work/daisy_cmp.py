import asyncio
from playwright.async_api import async_playwright
html='''<body style="margin:0;background:#1d414e;color:#15ffc8;font-family:sans-serif;padding:24px">
<style>.d{display:inline-block;background:currentColor;-webkit-mask:var(--m) center/contain no-repeat;mask:var(--m) center/contain no-repeat;margin:10px;vertical-align:middle}</style>
%s
<div style="background:#fff;color:#1d5a66;margin-top:20px;padding:10px">%s</div></body>'''
rows=''
for name in ['daisy.svg','daisy-line-mark.svg','daisy-line-bold.svg','daisy-line.svg']:
    r=f'<div><span style="display:inline-block;width:170px;color:#fff;font-size:12px">{name}</span>'
    for s in (16,20,28,44,72,120):
        ar = 1 if name=='daisy.svg' else 852/1100
        r+=f'<span class="d" style="--m:url(file:///home/claude/v4/site/assets/img/{name});width:{s}px;height:{int(s*ar)}px"></span>'
    rows+=r+'</div>'
async def main():
    async with async_playwright() as p:
        b=await p.chromium.launch(args=['--allow-file-access-from-files']); pg=await b.new_page(viewport={'width':760,'height':700},device_scale_factor=2)
        await pg.set_content(html%(rows,rows.replace('color:#fff','color:#333'))); await pg.wait_for_timeout(500)
        await pg.screenshot(path='shots/daisy_cmp.png',full_page=True); await b.close()
asyncio.run(main())
