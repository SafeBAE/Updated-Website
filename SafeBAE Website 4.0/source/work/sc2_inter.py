import sys, asyncio
sys.path.insert(0, '/home/claude/v4/tools')
from _sem import slot
from playwright.async_api import async_playwright
async def main():
    async with async_playwright() as p:
        b = await p.chromium.launch(args=['--allow-file-access-from-files'])
        pg = await b.new_page(viewport={'width':1440,'height':900})
        errs=[]; pg.on('pageerror', lambda e: errs.append(str(e))); pg.on('console', lambda m: errs.append(m.text) if m.type=='error' else None)
        base='file:///home/claude/v4/site/consent-curriculum.html'
        await pg.goto(base+'#lesson-9', wait_until='networkidle'); await pg.wait_for_timeout(900)
        print('hash lesson-9 ->', await pg.evaluate("[document.querySelector('[role=tab][aria-selected=true]').id, !!document.querySelector('#lesson-9.is-hl'), Math.round(document.querySelector('#lesson-9').getBoundingClientRect().top)]"))
        await pg.goto(base+'#healing', wait_until='networkidle'); await pg.wait_for_timeout(600)
        print('hash healing ->', await pg.evaluate("document.querySelector('[role=tab][aria-selected=true]').id"))
        await pg.goto(base, wait_until='networkidle'); await pg.wait_for_timeout(600)
        await pg.click('.s3-legend a[data-unit=justice]'); await pg.wait_for_timeout(900)
        print('legend justice ->', await pg.evaluate("[document.querySelector('[role=tab][aria-selected=true]').id, Math.round(document.querySelector('.s3-utabs').getBoundingClientRect().top), scrollY]"))
        await pg.evaluate("scrollTo(0,0)"); await pg.wait_for_timeout(300)
        await pg.click('.s3-tile[data-lesson=\"3\"]'); await pg.wait_for_timeout(900)
        print('tile 3 ->', await pg.evaluate("[document.querySelector('[role=tab][aria-selected=true]').id, !!document.querySelector('#lesson-3.is-hl'), Math.round(document.querySelector('#lesson-3').getBoundingClientRect().top)]"))
        # keyboard on tabs
        await pg.focus('#tab-core'); await pg.keyboard.press('ArrowRight'); await pg.wait_for_timeout(200)
        print('arrow ->', await pg.evaluate("document.querySelector('[role=tab][aria-selected=true]').id"))
        # copy button
        await pg.evaluate("document.querySelector('.s3-email__a button').scrollIntoView()"); await pg.click('.s3-email__a button'); await pg.wait_for_timeout(200)
        print('copy ->', await pg.evaluate("document.querySelector('.s3-email__a button').textContent"))
        # PD chart classes
        await pg.goto('file:///home/claude/v4/site/professional-development.html', wait_until='networkidle'); await pg.wait_for_timeout(500)
        print('chart pre ->', await pg.evaluate("[document.querySelector('.s3-chart').classList.contains('in'), getComputedStyle(document.querySelector('.s3-bar__track i')).width]"))
        await pg.evaluate("document.querySelector('.s3-chart').scrollIntoView({block:'center'})"); await pg.wait_for_timeout(2200)
        print('chart post ->', await pg.evaluate("[document.querySelector('.s3-chart').classList.contains('in'), [...document.querySelectorAll('.s3-bar__track i')].map(i=>Math.round(i.getBoundingClientRect().width)), [...document.querySelectorAll('.s3-tgrid [data-n]')].map(b=>b.textContent)]"))
        await pg.goto('file:///home/claude/v4/site/policy-reform-guide.html', wait_until='networkidle'); await pg.wait_for_timeout(500)
        await pg.evaluate("document.querySelector('.s3-shift').scrollIntoView({block:'center'})"); await pg.wait_for_timeout(2500)
        print('shift ->', await pg.evaluate("[document.querySelector('.s3-shift').classList.contains('in'), getComputedStyle(document.querySelector('.s3-shift__track svg')).clipPath]"))
        print('errors:', errs)
        await b.close()
with slot():
    asyncio.run(main())
