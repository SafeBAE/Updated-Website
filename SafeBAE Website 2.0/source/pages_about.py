"""ABOUT group: about, team, impact, partners & press, #ForDaisy, contact, photo credits."""
from lib import *
from data import LIB, PODCASTS
import json, os, re, glob

WP = 'https://www.safebae.org/wp-content/uploads/'
PAPER = 'https://www.tandfonline.com/doi/full/10.1080/10538712.2024.2385468'


def pod(eid):
    return next(p for p in PODCASTS if p[0] == eid)


def lib_item(i):
    return next(x for x in LIB if x['id'] == i)


def initials(name):
    parts = [p for p in re.split(r'[\s-]+', name) if p]
    return (parts[0][0] + (parts[-1][0] if len(parts) > 1 else '')).upper()



V2_CSS = """
main .eyebrow{color:var(--logo-teal)}
.v2-dark{position:relative; overflow:hidden; background-image:var(--grain)}
.v2-dark .eyebrow{color:var(--mint)}
.v2-dark .mk{background:none; color:var(--mint)}
.v2-dark > .wrap{position:relative; z-index:1}
.v2-light{position:relative; overflow:hidden}
.v2-light > .wrap{position:relative; z-index:1}
.v2-light .wm-daisy{color:var(--logo-teal); opacity:.06}
"""


def css(*parts):
    return '<style>' + V2_CSS + ''.join(parts) + '</style>'

# =====================================================================
# ABOUT
# =====================================================================
ABOUT_CSS = '''
.ab-hero{background-color:var(--slate); color:#fff}
.ab-hero__grid{display:grid; grid-template-columns:minmax(0,1.04fr) minmax(0,.96fr); gap:clamp(28px,5vw,72px); align-items:center; padding-block:clamp(44px,6vw,84px) clamp(56px,7vw,96px)}
.ab-hero h1{font-size:clamp(2.7rem,6.2vw,6rem); line-height:.88; font-weight:900; font-stretch:125%; text-transform:uppercase; letter-spacing:-.02em; margin:0 0 .45em}
.ab-hero h1 span{display:block}

.ab-hero .lede{color:rgba(255,255,255,.9); max-width:none}
.ab-hero .crumbs{margin-bottom:18px}
.ab-collage{position:relative; padding:0 0 18% 0}
.ab-collage__main img{width:100%; aspect-ratio:5/4; object-fit:cover; border-radius:var(--r-xl); box-shadow:0 30px 60px -30px rgba(0,0,0,.7)}
.ab-collage__sub{position:absolute; right:-3%; bottom:0; width:50%; border:6px solid var(--slate); border-radius:16px; overflow:hidden; transform:rotate(2.5deg); box-shadow:0 20px 40px -20px rgba(0,0,0,.6)}
.ab-collage__sub img{width:100%; aspect-ratio:4/3; object-fit:cover}
.ab-collage .sticker{position:absolute; left:-10px; top:20px; z-index:2}
.ab-collage .sticker--aqua{left:auto; top:auto; right:44%; bottom:6%}
@media (max-width:900px){.ab-hero__grid{grid-template-columns:1fr} .ab-collage{max-width:600px}}

.ab-bae{background:var(--mint); color:var(--slate); padding-block:clamp(40px,5vw,72px)}
.ab-bae__row{display:grid; grid-template-columns:repeat(3,minmax(0,1fr)); gap:clamp(10px,2vw,28px); align-items:end}
.ab-bae__l{display:block; font-family:var(--display); font-weight:900; font-size:clamp(5rem,15vw,13rem); line-height:.8; letter-spacing:-.03em; font-stretch:125%; transition:font-stretch 1.2s cubic-bezier(.2,.8,.2,1), letter-spacing 1.2s}
.js .ab-bae:not(.in) .ab-bae__l{font-stretch:62%; letter-spacing:-.06em}
.ab-bae__w{display:block; font-family:var(--display); font-weight:800; font-stretch:110%; font-size:clamp(1.1rem,2.4vw,2rem); text-transform:uppercase; border-top:4px solid var(--slate); padding-top:10px; margin-top:12px}
.ab-bae__row > div:nth-child(2) .ab-bae__l{transition-delay:.12s} .ab-bae__row > div:nth-child(3) .ab-bae__l{transition-delay:.24s}
.ab-bae p{margin:clamp(20px,3vw,34px) 0 0; font-family:var(--display); font-stretch:104%; font-weight:700; font-size:clamp(1.15rem,2vw,1.6rem); line-height:1.3}

.ab-statement{font-family:var(--display); font-stretch:104%; font-weight:700; font-size:clamp(1.35rem,2.5vw,2.15rem); line-height:1.25; margin:0 0 clamp(28px,4vw,48px); text-wrap:pretty}

.ab-story__grid{display:grid; grid-template-columns:minmax(0,1.15fr) minmax(0,.85fr); gap:clamp(22px,3.5vw,48px); align-items:stretch}
.ab-story__text{columns:2 260px; column-gap:clamp(22px,3vw,40px)}
.ab-story__text p{font-size:1.06rem; break-inside:avoid-column}
.ab-story__fig{margin:0; position:relative; min-height:300px; border-radius:var(--r-xl); overflow:hidden}
.ab-story__fig img{position:absolute; inset:0; width:100%; height:100%; object-fit:cover; object-position:30% 40%}
.ab-story__fig figcaption{position:absolute; left:12px; bottom:12px; font-family:var(--mono); font-size:.68rem; letter-spacing:.06em; text-transform:uppercase; color:#fff; background:rgba(22,53,64,.78); padding:5px 9px; border-radius:6px}
.ab-drop::first-letter{font-family:var(--display); font-weight:900; font-stretch:125%; float:left; font-size:4.6em; line-height:.78; margin:.06em .1em 0 0; color:var(--teal)}
.ab-pull{margin:clamp(30px,4vw,52px) 0 0; padding:clamp(22px,3vw,36px) clamp(22px,3vw,40px); background:var(--slate) var(--grain); color:#fff; border-radius:var(--r-xl); display:grid; grid-template-columns:auto minmax(0,1fr); gap:clamp(16px,3vw,36px); align-items:center}
.ab-pull .daisy{width:clamp(56px,7vw,88px); height:clamp(56px,7vw,88px); color:var(--mint)}
.ab-pull blockquote{margin:0; font-family:var(--display); font-weight:800; font-stretch:106%; font-size:clamp(1.3rem,2.6vw,2.2rem); line-height:1.18}
.ab-pull cite{display:block; margin-top:12px; font-style:normal; font-family:var(--mono); font-size:.74rem; letter-spacing:.08em; text-transform:uppercase; color:var(--aqua)}
.ab-after{margin-top:clamp(24px,3vw,36px); font-size:var(--fs-lede); line-height:1.55; font-weight:500}
@media (max-width:860px){.ab-story__grid{grid-template-columns:1fr} .ab-story__fig{min-height:0; aspect-ratio:16/10}}
@media (max-width:640px){.ab-pull{grid-template-columns:1fr}}

.ab-began{display:grid; grid-template-columns:minmax(0,.95fr) minmax(0,1.05fr); gap:clamp(28px,5vw,64px); align-items:center}
.ab-began .lede{color:rgba(255,255,255,.88)}
.ab-names{display:flex; flex-wrap:wrap; gap:8px; margin:20px 0 0; padding:0; list-style:none}
.ab-names li{margin:0; font-family:var(--display); font-weight:800; font-stretch:108%; padding:8px 14px; border-radius:999px; border:1.5px solid rgba(209,254,255,.35); color:#fff}
.ab-names li .daisy{width:1em; height:1em; color:var(--mint); margin-right:6px; vertical-align:-2px}
@media (max-width:900px){.ab-began{grid-template-columns:1fr}}

.ab-founders{display:grid; grid-template-columns:repeat(4,minmax(0,1fr)); gap:clamp(14px,2vw,24px)}
.ab-f{display:flex; flex-direction:column; text-decoration:none; color:var(--slate); background:#fff; border-radius:var(--r-xl); overflow:hidden; box-shadow:var(--shadow-soft); transition:transform .25s var(--ease)}
.ab-f:hover{transform:translateY(-5px)}
.ab-f__img{position:relative; aspect-ratio:3/4; overflow:hidden; background:var(--slate)}
.ab-f__img img{width:100%; height:100%; object-fit:cover; transition:transform .6s}
.ab-f:hover .ab-f__img img{transform:scale(1.04)}
.ab-f__badge{position:absolute; top:12px; right:12px; width:46px; height:46px; border-radius:50%; background:var(--slate); display:grid; place-items:center}
.ab-f__badge .daisy{width:30px; height:30px; color:var(--mint)}
.ab-f__body{padding:16px 18px 18px; display:flex; flex-direction:column; gap:4px; flex:1}
.ab-f__body small{font-family:var(--mono); font-size:.68rem; letter-spacing:.1em; text-transform:uppercase; color:var(--logo-teal); font-weight:600}
.ab-f__body b{font-family:var(--display); font-weight:900; font-stretch:112%; font-size:clamp(1.25rem,1.8vw,1.55rem); line-height:1.05}
.ab-f__body span{margin-top:auto; padding-top:10px; font-size:.88rem; font-weight:700; color:var(--logo-teal)}
.ab-f__body span::after{content:" \\2192"}
@media (max-width:960px){.ab-founders{grid-template-columns:repeat(2,minmax(0,1fr))}}

.ab-ed{display:grid; grid-template-columns:minmax(0,.7fr) minmax(0,1.3fr); gap:clamp(28px,5vw,64px); align-items:center}
.ab-ed__img{position:relative}
.ab-ed__img img{width:100%; aspect-ratio:4/5; object-fit:cover; border-radius:var(--r-xl)}
.ab-ed__img .sticker{position:absolute; right:-10px; bottom:22px}
.ab-ed h2{margin-bottom:.15em}
.ab-ed__role{font-family:var(--mono); font-size:.8rem; letter-spacing:.08em; text-transform:uppercase; color:var(--logo-teal); margin:0 0 18px; font-weight:600}
@media (max-width:860px){.ab-ed{grid-template-columns:1fr} .ab-ed__img{max-width:380px}}

.ab-tl{position:relative; margin:0; padding:0; list-style:none}
.ab-tl{--p:1}
.ab-tl::before{content:""; position:absolute; left:50%; top:0; bottom:0; width:3px; margin-left:-1.5px; background:rgba(21,255,200,.16); border-radius:3px}
.ab-tl::after{content:""; position:absolute; left:50%; top:0; width:3px; margin-left:-1.5px; height:calc(var(--p) * 100%); background:var(--mint); border-radius:3px; box-shadow:0 0 14px rgba(21,255,200,.55)}
.ab-tl li{position:relative; display:grid; grid-template-columns:minmax(0,1fr) minmax(0,1fr); gap:0 64px; margin:0 0 clamp(18px,2.5vw,30px)}
.ab-tl li::before{content:""; position:absolute; z-index:1; left:50%; top:16px; width:18px; height:18px; margin-left:-9px; border-radius:50%; background:var(--slate); border:4px solid rgba(21,255,200,.35); transition:border-color .4s var(--ease), background .4s var(--ease), box-shadow .4s var(--ease)}
.ab-tl li.lit::before{border-color:var(--mint)}
.ab-tl li.lit.is-key::before{background:var(--mint); box-shadow:0 0 0 6px rgba(21,255,200,.18)}
.ab-tl__y{transition:opacity .5s var(--ease)}
.js .ab-tl li:not(.lit) .ab-tl__y{opacity:.35}
.ab-tl__y{font-family:var(--display); font-weight:900; font-stretch:125%; font-size:clamp(2rem,4vw,3.4rem); line-height:1; color:var(--mint); text-align:right; padding-top:2px}
.ab-tl__c{background:rgba(255,255,255,.05); border:1px solid var(--line-dark); border-radius:14px; padding:16px 18px}
.ab-tl__c h3{font-size:1.15rem; margin:0 0 .3em; color:#fff}
.ab-tl__c p{margin:0; color:rgba(255,255,255,.8); font-size:.95rem}
.ab-tl__c a{color:var(--mint); font-weight:700}
.ab-tl li:nth-child(even) .ab-tl__y{order:2; text-align:left}
.ab-tl li:nth-child(even) .ab-tl__c{order:1}
@media (max-width:760px){
  .ab-tl::before,.ab-tl::after{left:9px}
  .ab-tl li{grid-template-columns:1fr; gap:6px; padding-left:36px}
  .ab-tl li::before{left:9px; top:8px}
  .ab-tl__y,.ab-tl li:nth-child(even) .ab-tl__y{order:0; text-align:left}
  .ab-tl li:nth-child(even) .ab-tl__c{order:1}
}

.ab-bento{display:grid; grid-template-columns:repeat(4,minmax(0,1fr)); grid-template-rows:repeat(2, minmax(300px,auto)) auto; gap:clamp(12px,1.6vw,18px)}
.ab-new{grid-column:span 2; position:relative; display:flex; flex-direction:column; gap:10px; padding:clamp(22px,2.6vw,32px); border-radius:var(--r-xl); text-decoration:none; overflow:hidden; transition:transform .25s var(--ease), box-shadow .25s var(--ease)}
.ab-new:hover{transform:translateY(-4px); box-shadow:var(--shadow-soft)}
.ab-new .chip{align-self:flex-start}
.ab-new h3{font-size:clamp(1.5rem,2.4vw,2.1rem); margin:0; line-height:1.05}
.ab-new p{margin:0; font-size:.95rem; line-height:1.5}
.ab-new__go{margin-top:auto; padding-top:6px; font-weight:800; font-family:var(--display); font-stretch:106%}
.ab-new--ai{background:var(--aqua); color:var(--slate); border:1px solid var(--line)}
.ab-new--ai .ab-new__go{color:var(--logo-teal)}
.ab-loop{position:relative; display:inline-block; padding:0 .12em}
.ab-loop{margin:0 .1em}
.ab-loop svg{position:absolute; left:-34%; top:-38%; width:168%; height:176%; color:var(--teal); pointer-events:none; overflow:visible}
.ab-loop svg path{stroke-width:2.4}
.ab-new--ch{background:var(--slate-deep) var(--grain); color:#fff}
.ab-new--ch p{color:rgba(255,255,255,.84)}
.ab-new--ch .ab-new__line{font-family:var(--display); font-weight:800; font-stretch:108%; font-size:clamp(1.15rem,1.8vw,1.45rem); color:var(--mint); line-height:1.2}
.ab-new--ch .ab-new__go{color:var(--mint)}
.ab-tile{position:relative; border-radius:var(--r-xl); overflow:hidden; color:#fff; text-decoration:none; display:flex; flex-direction:column; justify-content:flex-end; padding:20px; background:var(--slate); isolation:isolate; min-height:300px}
.ab-tile > img{position:absolute; inset:0; width:100%; height:100%; object-fit:cover; z-index:-2; transition:transform .6s}
.ab-tile::after{content:""; position:absolute; inset:0; z-index:-1; background:linear-gradient(180deg, rgba(22,53,64,0) 18%, rgba(22,53,64,.72) 48%, rgba(22,53,64,.96) 78%)}
.ab-tile:hover > img{transform:scale(1.05)}
.ab-tile h3{font-size:1.35rem; margin:0 0 .3em}
.ab-tile p{margin:0; font-size:.9rem; line-height:1.45; color:rgba(255,255,255,.88)}
.ab-tile .chip{position:absolute; top:16px; left:16px}
.ab-tile--vc{grid-column:span 2; grid-row:span 2; background:var(--teal); justify-content:space-between; padding:clamp(22px,3vw,36px)}
.ab-tile--vc::after{display:none}
.ab-tile--vc .ab-vc__mark{display:flex; align-items:center; gap:10px; font-family:var(--display); font-weight:900; font-stretch:115%; font-size:1.15rem; color:var(--mint)}
.ab-tile--vc .ab-vc__mark .daisy{width:34px; height:34px}
.ab-tile--vc h3{font-size:clamp(2rem,3.6vw,3.2rem); font-stretch:120%; line-height:.95; margin:.3em 0 .35em; max-width:11ch}
.ab-tile--vc p{font-size:1rem}
.ab-tile--vc > div:not(.ab-vc__phone){max-width:56%}
.ab-vc__phone{position:absolute; right:clamp(16px,2.6vw,34px); top:clamp(70px,7vw,96px); width:min(36%, 210px); border-radius:28px; border:8px solid #0b1f25; overflow:hidden; transform:rotate(4deg); box-shadow:0 30px 60px -20px rgba(0,0,0,.55); z-index:-1}
.ab-vc__phone img{width:100%; display:block}
@media (max-width:960px){.ab-bento{grid-template-columns:repeat(2,minmax(0,1fr)); grid-template-rows:none} .ab-tile--vc{grid-row:auto; min-height:420px}}
@media (max-width:560px){.ab-new{grid-column:auto}}
@media (max-width:560px){.ab-bento{grid-template-columns:1fr} .ab-tile--vc{grid-column:auto; min-height:0; padding-bottom:300px} .ab-tile--vc > div:not(.ab-vc__phone){max-width:none} .ab-vc__phone{top:auto; bottom:-70px; right:50%; margin-right:-80px; width:160px}}

.ab-more{display:grid; grid-template-columns:repeat(4,minmax(0,1fr)); gap:clamp(12px,1.6vw,18px)}
.ab-more a{display:grid; grid-template-rows:auto 1fr; text-decoration:none; color:var(--slate); background:#fff; border-radius:var(--r-xl); overflow:hidden; transition:transform .2s var(--ease), box-shadow .2s}
.ab-more a:hover{transform:translateY(-4px); box-shadow:var(--shadow)}
.ab-more img{width:100%; aspect-ratio:16/10; object-fit:cover}
.ab-more span{padding:16px 18px 18px; display:block}
.ab-more b{display:block; font-family:var(--display); font-weight:800; font-stretch:108%; font-size:1.2rem; color:var(--logo-teal)}
.ab-more b::after{content:" \\2192"; color:var(--logo-teal)}
.ab-more small{display:block; color:var(--ink-soft); font-size:.88rem; line-height:1.4; margin-top:4px}
@media (max-width:960px){.ab-more{grid-template-columns:repeat(2,minmax(0,1fr))}}
@media (max-width:480px){.ab-more{grid-template-columns:1fr} .ab-more a{grid-template-columns:120px minmax(0,1fr); grid-template-rows:none} .ab-more img{height:100%; aspect-ratio:auto; min-height:110px} .ab-more span{padding:12px 14px}}
'''

ABOUT_JS = '''<script>(function(){
  var el = document.querySelector('.ab-bae'); if(!el) return;
  if(!('IntersectionObserver' in window)){ el.classList.add('in'); return; }
  var io = new IntersectionObserver(function(es){ es.forEach(function(e){ if(e.isIntersecting){ el.classList.add('in'); io.disconnect(); } }); }, {threshold:.35});
  io.observe(el);
})();
(function(){
  var tl = document.querySelector('.ab-tl'); if(!tl) return;
  var items = tl.querySelectorAll('li'), ticking = false;
  function upd(){ ticking = false; var vh = window.innerHeight, mark = vh * 0.62, r = tl.getBoundingClientRect();
    var p = Math.min(1, Math.max(0, (mark - r.top) / r.height)); tl.style.setProperty('--p', p.toFixed(4));
    for(var i = 0; i < items.length; i++){ var t = items[i].getBoundingClientRect().top + 24; items[i].classList.toggle('lit', t < mark); } }
  window.addEventListener('scroll', function(){ if(!ticking){ ticking = true; requestAnimationFrame(upd); } }, {passive:true});
  window.addEventListener('resize', upd); upd();
})();</script>'''


def about():
    founders = [
        ('Daisy Coleman', '8b5afefa-96d9-4520-9c75-48c07b648528', 'fordaisy.html', '#ForDaisy: remembering Daisy', True),
        ('Jada Smith', 'ddaf06be-f4a9-4097-affa-e0e361779475', 'film-race-rape-culture-resistance.html', 'Watch Jada’s Story', False),
        ('Ella Fairon', 'df8aca6d-675e-4a1c-8258-3c343c189d6d-1', 'film-dating-after-sexual-assault.html', 'Watch Ella in Intimacy & Dating After Sexual Assault', False),
        ('Charlie Coleman', 'caa82df2-41d5-48e8-aa8e-de750350486e', 'film-rape-culture.html', 'Watch Charlie on rape culture and respect', False),
    ]
    fcards = ''.join(
        f'<a class="ab-f reveal" href="{h}"><div class="ab-f__img">{img(im, "Portrait of SafeBAE co-founder " + n)}{'<span class="ab-f__badge">' + daisy() + '</span>' if d else ""}</div>'
        f'<div class="ab-f__body"><small>Co-Founder</small><b>{esc(n)}</b><span>{esc(lk)}</span></div></a>'
        for n, im, h, lk, d in founders)

    tl = [
        ('1999–2016', 'At V-Day', 'As a founding staffer at V-Day, Shael Norris oversees global productions of <i>The Vagina Monologues</i>.', False),
        ('2007', 'Campus Accountability Project', 'Shael launches the Campus Accountability Project to push for stronger prevention and response efforts on college campuses.', False),
        ('2015', 'SafeBAE is founded', 'Daisy Coleman, Ella Fairon, Jada Smith and Charlie Coleman found SafeBAE with Shael Norris, to bring prevention to middle and high school students.', True),
        ('2020', 'We lose Daisy', 'Co-founder Daisy Coleman passes away on August 4, 2020. More than 700 tribute messages are collected at her memorial service. <a href="fordaisy.html">#ForDaisy</a>', False),
        ('2020–23', 'National School Sexual Violence Climate Survey', 'SafeBAE surveys 849 students in 45 states about safety, support systems and accountability at their schools. <a href="impact.html#climate">See the findings</a>', False),
        ('2023', 'Peer Educator Training evaluated', '1,057 students take part in the Certified Peer Educator Training evaluated in SafeBAE’s 2023 efficacy data. <a href="impact.html#training">See the results</a>', False),
        ('2025', 'Youth Leading', 'The 2025 Annual Report, <i>SafeBAE’s Expanding Network for Change</i>, documents youth leaders creating safer schools across the country. <a href="impact.html#reports">Read the reports</a>', False),
        ('2026', 'Six years #ForDaisy', 'SafeBAE brings the tribute messages for Daisy together in one place, on the #ForDaisy Memorial Tribute Wall.', True),
    ]
    tl_html = ''.join(f'<li class="reveal{" is-key" if k else ""}"><div class="ab-tl__y">{y}</div><div class="ab-tl__c"><h3>{esc(t)}</h3><p>{d}</p></div></li>' for y, t, d, k in tl)

    more = [
        ('Our Team', 'team.html', 'dsc01134', 'Staff, our youth media team and a board that is at least two-thirds youth.'),
        ('Data & Impact', 'impact.html', 'img-3947', 'Published research, our climate survey, training data and annual reports.'),
        ('Partners & Press', 'partners-press.html', 'p1002709', 'Podcasts, press coverage and the films we partner on.'),
        ('#ForDaisy', 'fordaisy.html', 'daisy-coleman', 'Remembering our co-founder, Daisy Coleman.'),
    ]
    more_html = ''.join(f'<a href="{h}">{img(im, "")}<span><b>{esc(t)}</b><small>{esc(d)}</small></span></a>' for t, h, im, d in more)

    body = f'''
<section class="ab-hero v2-dark">
  <span class="wm-daisy" aria-hidden="true"></span>
  <div class="wrap ab-hero__grid">
    <div class="rise">
      <nav class="crumbs" aria-label="Breadcrumb"><a href="index.html">Home</a><span>/</span><span>About SafeBAE</span></nav>
      <p class="eyebrow">Our mission</p>
      <h1><span>Survivor-</span><span>founded.</span><span><span class="mk">Youth-led.</span></span></h1>
      <p class="lede">SafeBAE is the only survivor-founded, youth-led organization working to end sexual violence among middle and high school students nationwide. We equip young people with the tools to prevent harm, support their peers, and drive generational culture change, strengthening mental health, uplifting youth leadership, and creating safer school communities.</p>
      <div class="btns">{btn('Support our work', 'donate.html', 'mint', arrow=True)}{btn('See all resources', 'resources.html', 'ghost')}</div>
    </div>
    <div class="ab-collage">
      <div class="ab-collage__main">{img('safebae-executive-director-shael-norris', 'SafeBAE co-founders Daisy Coleman, Ella Fairon, Jada Smith and Charlie Coleman with Executive Director Shael Norris', loading='eager')}</div>
      <div class="ab-collage__sub">{img('founding-members-get-inovlved-page', 'SafeBAE founding members on a film set in front of a #QuitThisShit sign', loading='eager')}</div>
      <span class="sticker">Founded 2015</span>
      <span class="sticker sticker--aqua sticker--r">Survivor-founded</span>
    </div>
  </div>
</section>

<section class="ab-bae" aria-label="What BAE stands for">
  <div class="wrap">
    <div class="ab-bae__row" aria-hidden="true">
      <div><span class="ab-bae__l">B</span><span class="ab-bae__w">Before</span></div>
      <div><span class="ab-bae__l">A</span><span class="ab-bae__w">Anyone</span></div>
      <div><span class="ab-bae__l">E</span><span class="ab-bae__w">Else</span></div>
    </div>
    <p>The “BAE” in SafeBAE stands for Before Anyone Else, because we know prevention has to start early.</p>
  </div>
</section>

<section class="band band--paper" id="story">
  <div class="wrap">
    <p class="eyebrow">Our story</p>
    <h2>We built the education we <span class="mk">never had.</span></h2>
    <p class="ab-statement">At SafeBAE, we believe rape culture and sexual assault are among the most dangerous and life-altering issues facing young people today, compounded by a growing youth mental health crisis. Rates of sexual violence among youth are higher than any other age group, yet our schools continue to offer little in the way of education or tools to prevent it.</p>
    <div class="ab-story__grid">
      <div class="ab-story__text">
        <p class="ab-drop">We founded SafeBAE in 2015 because we knew that had to change. Daisy, Ella, and Jada, teen survivors of sexual assault, came together with Daisy’s brother, Charlie, and our Executive Director, Shael, to build something we never had: a way to stop what happened to us from happening to anyone else.</p>
        <p>The idea for SafeBAE began during the filming of the Peabody Award-winning Netflix documentary {a('<i>Audrie &amp; Daisy</i>', 'https://en.wikipedia.org/wiki/Audrie_%26_Daisy', 'link')}. As we shared our stories, one devastating truth became clear: none of us had ever received meaningful education about consent, Title IX, or how to recognize and prevent sexual violence. That knowledge gap was the common thread in our experiences, and it’s exactly what we set out to change.</p>
      </div>
      <figure class="ab-story__fig">{img('dsc04560', 'Daisy Coleman and others speaking to an audience from a panel table')}<figcaption>Daisy Coleman speaking on a panel</figcaption></figure>
    </div>
    <div class="ab-pull reveal">{daisy()}<div><blockquote>None of us had ever received meaningful education about consent, Title IX, or how to recognize and prevent sexual violence.</blockquote><cite>SafeBAE’s founders</cite></div></div>
    <p class="ab-after">We knew the work couldn’t wait until college. It had to begin earlier, in middle and high school, when beliefs about intimacy, boundaries, and safety are just beginning to form. SafeBAE exists to fill that gap: to reach young people before harm happens, and when it does, to make sure they have access to survivor-centered care, community, and lasting support.</p>
  </div>
</section>

<section class="band band--deep" id="how-we-began">
  <div class="wrap ab-began">
    <div>
      <p class="eyebrow">How we began</p>
      <h2>Survivors and their families, together.</h2>
      <p class="lede">These survivors and their families came together during the filming of the Netflix documentary <i>Audrie &amp; Daisy</i> to help prevent what happened to them from happening to anyone else.</p>
      <p style="color:rgba(255,255,255,.82)">Daisy Coleman, Ella Fairon, Jada Smith and Charlie Coleman have bravely spoken out about their sexual assaults, the public sharing of the assaults over social media, the community backlash they received, their schools’ mishandling of their ongoing harassment, and how they have fought for necessary change.</p>
      <ul class="ab-names"><li>{daisy()}Daisy Coleman</li><li>Ella Fairon</li><li>Jada Smith</li><li>Charlie Coleman</li><li>Shael Norris</li></ul>
    </div>
    <div>{yt('oKq44GSBSQU', 'SafeBAE overview', label='Watch')}</div>
  </div>
</section>

<section class="band band--aqua" id="co-founders">
  <div class="wrap">
    <div class="section-head"><div><p class="eyebrow">Founded 2015</p><h2>The co-founders</h2></div></div>
    <div class="ab-founders">{fcards}</div>
  </div>
</section>

<section class="band band--paper" id="executive-director">
  <div class="wrap ab-ed">
    <div class="ab-ed__img">{img('82bc8566-88a9-4a05-b13a-f02df3e64af9', 'Portrait of Shael Norris')}</div>
    <div>
      <h2>Shael Norris</h2>
      <p class="ab-ed__role">Co-Founder &middot; Executive Director</p>
      <p class="lede">Shael Norris has dedicated her career to ending sexual violence. She is passionate about helping young people become change agents in preventing violence.</p>
      <p>She was a founding staffer of V-Day, overseeing the College and Community Campaigns for 19 years. After decades of work focused on college sexual assault, she sought a grant to establish SafeBAE to focus specifically on younger students. Her three children and her dedication to making schools safer were the driving force behind the creation of SafeBAE.</p>
      <div class="btns" style="margin-top:22px">{btn('Meet the whole team', 'team.html', 'slate', arrow=True)}{btn('Shael on LinkedIn', 'https://www.linkedin.com/in/shaelnorris/', 'ghost')}</div>
    </div>
  </div>
</section>

<section class="band band--slate" id="milestones">
  <div class="wrap">
    <div class="section-head"><div><p class="eyebrow">Milestones, 1999–2026</p><h2>From one documentary to a national movement</h2></div></div>
    <ol class="ab-tl">{tl_html}</ol>
  </div>
</section>

<section class="band band--paper" id="what-we-do">
  <div class="wrap">
    <div class="section-head"><div><h2>Prevention led by young people, in their own schools</h2>
      <p class="lede lede--full muted">Our programs are free for students.</p></div></div>
    <div class="ab-bento">
      <a class="ab-tile ab-tile--vc" href="vibe-check.html">
        <div class="ab-vc__mark">{daisy()}Vibe Check by SafeBAE</div>
        <div><h3>Not sure if you crossed a line?</h3><p>CheckYourVibe.org is a free, anonymous reflection tool for young people who are questioning whether they may have crossed a boundary or caused harm. Nothing is stored.</p>
        <span class="btn btn--mint btn--sm" style="margin-top:18px">How Vibe Check works<span class="arr" aria-hidden="true">&rarr;</span></span></div>
        <div class="ab-vc__phone">{img('vc-screen', 'The Vibe Check home screen')}</div>
      </a>
      <a class="ab-tile" href="peer-educator.html">{img('1-000383-edited', '')}<span class="chip chip--mint">Free</span><h3>Certified Peer Educator Training</h3><p>Self-paced training that prepares students to lead conversations about consent and healthy relationships at their schools.</p></a>
      <a class="ab-tile" href="clubs.html">{img('clubtabling', '')}<span class="chip">Students</span><h3>SafeBAE Clubs</h3><p>Start, affiliate or restart a chapter and run prevention campaigns with your peers.</p></a>
      <a class="ab-tile" href="360-schools.html">{img('066', '')}<span class="chip">Schools</span><h3>SafeBAE 360° Schools</h3><p>Peer education, a consent curriculum, staff training and policy support in one whole-school model.</p></a>
      <a class="ab-tile" href="library.html">{img('gameon8', '')}<span class="chip">Library</span><h3>Films, podcasts &amp; guides</h3><p>Youth-made films with ready-to-teach guides, plus conversations with SafeBAE leaders.</p></a>
      <a class="ab-new ab-new--ai" href="ai-literacy.html">
        <span class="chip chip--slate">New &middot; launches Oct 26–30, 2026</span>
        <h3>SafeBAE <span class="ab-loop">AI<svg viewBox="0 0 120 60" aria-hidden="true"><path d="M14 36C10 20 34 7 62 7c28 0 50 11 50 25 0 15-26 24-54 23C30 54 8 46 10 31 12 19 34 11 66 10" fill="none" stroke="currentColor" stroke-linecap="round"/></svg></span> Literacy Training</h3>
        <p>Six free, self-paced modules on how AI works, how feeds shape what we believe, AI and healthy relationships, fake images and sextortion. For high school and college students; anyone 13 or older can take it.</p>
        <span class="ab-new__go">About the training &rarr;</span>
      </a>
      <a class="ab-new ab-new--ch" href="choking-hazard.html">
        <span class="chip chip--mint">Campaign</span>
        <h3>Choking Hazard</h3>
        <p class="ab-new__line">“There’s no safe way to choke someone.”</p>
        <p>SafeBAE’s campaign on sexual strangulation, which young people call “choking”: the evidence, myths and facts, signs that need medical care, and free warning posters.</p>
        <span class="ab-new__go">About the campaign &rarr;</span>
      </a>
    </div>
  </div>
</section>

<section class="band band--deep band--tight" id="more">
  <div class="wrap">
    <div class="section-head"><div><h2>Meet the people and the work</h2></div>{btn('Contact us', 'contact.html', 'mint', arrow=True)}</div>
    <div class="ab-more">{more_html}</div>
  </div>
</section>
{give_band()}
'''
    page('about.html', 'About SafeBAE · Survivor-founded, youth-led', 'SafeBAE is the only survivor-founded, youth-led organization working to end sexual violence among middle and high school students nationwide. Founded in 2015 by teen survivors.',
         body, active='about', body_class='pg-about', head_extra=css(ABOUT_CSS), scripts=ABOUT_JS)


# =====================================================================
# TEAM
# =====================================================================
TEAM_CSS = '''
.tm-hero{background-color:var(--logo-teal); color:#fff}
.tm-hero .wrap{padding-block:clamp(44px,5.5vw,80px); display:grid; grid-template-columns:minmax(0,1fr) minmax(0,1fr); gap:clamp(28px,5vw,72px); align-items:center}
.tm-mosaic{display:grid; grid-template-columns:repeat(6,minmax(0,1fr)); gap:clamp(6px,.7vw,10px); margin:0; padding:0; list-style:none}
.tm-mosaic li{margin:0; aspect-ratio:1; min-width:0; animation:sb-rise .7s var(--ease) both}
.tm-mosaic a,.tm-mosaic .tm-tile{position:relative; display:block; width:100%; height:100%; border-radius:12px; overflow:hidden; background:var(--slate); text-decoration:none; transition:transform .25s var(--ease), box-shadow .25s var(--ease)}
.tm-mosaic img{width:100%; height:100%; object-fit:cover; transition:transform .5s var(--ease), filter .3s}
.tm-mosaic a::after{content:attr(data-name); position:absolute; left:0; right:0; bottom:0; padding:14px 6px 5px; font-size:.66rem; font-weight:700; line-height:1.15; color:#fff; background:linear-gradient(transparent, rgba(22,53,64,.92)); opacity:0; transform:translateY(6px); transition:opacity .25s, transform .25s var(--ease)}
.tm-mosaic a:hover,.tm-mosaic a:focus-visible{transform:translateY(-3px) scale(1.04); box-shadow:0 0 0 3px var(--mint), 0 18px 30px -16px rgba(0,0,0,.6); z-index:2}
.tm-mosaic a:hover::after,.tm-mosaic a:focus-visible::after{opacity:1; transform:none}
.tm-mosaic a:hover img{transform:scale(1.06)}
.tm-tile{display:grid!important; place-items:center; text-align:center; font-family:var(--display); font-weight:900; font-stretch:122%; line-height:.95}
.tm-tile--daisy{background:var(--mint)!important; color:var(--slate)}
.tm-tile--daisy .daisy{width:62%; height:62%}
.tm-tile--third{background:var(--slate)!important; color:var(--mint); font-size:clamp(1.3rem,2.4vw,2.2rem)}
.tm-tile--third small{display:block; font-family:var(--mono); font-weight:600; font-stretch:100%; font-size:clamp(.5rem,.7vw,.62rem); letter-spacing:.08em; text-transform:uppercase; color:var(--aqua); margin-top:4px}
.tm-tile--year{background:var(--aqua)!important; color:var(--slate); font-size:clamp(.9rem,1.5vw,1.3rem)}
.tm-tile--year small{display:block; font-family:var(--mono); font-weight:600; font-stretch:100%; font-size:clamp(.5rem,.7vw,.62rem); letter-spacing:.08em; text-transform:uppercase; margin-bottom:3px}
.tm-mosaic li:nth-child(3n+2){animation-delay:.05s} .tm-mosaic li:nth-child(3n){animation-delay:.1s} .tm-mosaic li:nth-child(n+13){animation-duration:.9s}
@media (max-width:900px){.tm-hero .wrap{grid-template-columns:1fr}}
.tm-hero h1{font-size:var(--fs-h1); font-stretch:122%; font-weight:900; text-transform:uppercase; line-height:.92; letter-spacing:-.02em; margin:0 0 .35em}
.tm-hero .lede{color:rgba(255,255,255,.9); max-width:none}
.tm-ini{display:grid; place-items:center; width:100%; height:100%; aspect-ratio:1; font-family:var(--display); font-weight:900; font-stretch:125%; font-size:clamp(1.6rem,3vw,2.4rem); letter-spacing:.02em; background:var(--mint); color:var(--slate); border-radius:inherit}
.tm-ini--teal{background:var(--teal); color:#fff}

.tm-lead{display:grid; grid-template-columns:repeat(2,minmax(0,1fr)); gap:clamp(16px,2vw,24px)}
.tm-card{display:grid; grid-template-columns:minmax(0,160px) minmax(0,1fr); gap:clamp(16px,2vw,24px); background:#fff; border:1px solid var(--line); border-radius:var(--r-xl); padding:clamp(16px,2vw,22px); scroll-margin-top:110px}
.tm-card__img img{width:100%; aspect-ratio:3/4; object-fit:cover; border-radius:14px}
.tm-card__img .tm-li{display:inline-flex; margin-top:10px; font-size:.82rem; font-weight:700; color:var(--logo-teal); text-decoration:none}
.tm-card__img .tm-li::after{content:"\\2197"; margin-left:4px}
.tm-card h3{font-size:clamp(1.4rem,2vw,1.75rem); margin:0 0 .15em}
.tm-role{font-family:var(--mono); font-size:.72rem; letter-spacing:.08em; text-transform:uppercase; color:var(--logo-teal); font-weight:600; margin:0 0 12px}
.tm-card p{font-size:.96rem; line-height:1.6}
.tm-more summary{list-style:none; cursor:pointer; display:inline-flex; align-items:center; gap:8px; font-weight:800; font-family:var(--display); font-stretch:106%; color:var(--logo-teal); padding:6px 0}
.tm-more summary::-webkit-details-marker{display:none}
.tm-more summary::before{content:"+"; display:grid; place-items:center; width:24px; height:24px; border-radius:50%; background:var(--aqua); font-size:1rem; line-height:1}
.tm-more[open] summary::before{content:"\\2013"; background:var(--mint)}
.tm-more[open] summary span:first-child{display:none} .tm-more:not([open]) summary span:last-child{display:none}
.tm-more > div{padding-top:8px}
@media (max-width:1000px){.tm-lead{grid-template-columns:1fr}}
@media (max-width:520px){.tm-card{grid-template-columns:1fr} .tm-card__img{max-width:220px}}

.tm-media{display:flex; flex-wrap:wrap; justify-content:center; gap:22px 16px}
.tm-media .person{width:calc((100% - 6*16px)/7); min-width:0; scroll-margin-top:110px}
.tm-media .person img,.tm-media .person .tm-ini{border-radius:50%}
.tm-media .person b{text-align:center} .tm-media .person small{text-align:center; color:var(--slate); opacity:.8}
@media (max-width:1060px){.tm-media .person{width:calc((100% - 3*16px)/4)}}
@media (max-width:620px){
  .tm-media{display:grid; grid-template-columns:1fr; gap:0; border-top:1px solid rgba(29,65,78,.18)}
  .tm-media .person{width:auto; display:grid; grid-template-columns:64px minmax(0,1fr); grid-template-rows:auto auto; column-gap:14px; align-items:center; padding:10px 0; border-bottom:1px solid rgba(29,65,78,.18)}
  .tm-media .person img{grid-row:span 2; width:64px; height:64px; margin:0}
  .tm-media .person b,.tm-media .person small{text-align:left}
  .tm-media .person b{align-self:end} .tm-media .person small{align-self:start}
}

.tm-third{display:grid; grid-template-columns:minmax(0,1fr) minmax(0,1.1fr); gap:clamp(24px,4vw,56px); align-items:center; margin-bottom:clamp(30px,4vw,48px)}
.tm-third__bar{display:grid; grid-template-columns:repeat(3,minmax(0,1fr)); gap:8px}
.tm-third__bar span{height:clamp(84px,10vw,128px); border-radius:12px; display:flex; align-items:flex-end; padding:12px; font-family:var(--mono); font-size:.72rem; letter-spacing:.08em; text-transform:uppercase; font-weight:600}
.tm-third__bar span:nth-child(-n+2){background:var(--mint); color:var(--slate)}
.tm-third__bar span:nth-child(3){border:2px dashed rgba(209,254,255,.45); color:var(--aqua)}
.tm-third__big{display:flex; align-items:baseline; gap:14px; margin-top:14px}
.tm-third__big b{font-family:var(--display); font-weight:900; font-stretch:125%; font-size:clamp(3.4rem,7vw,6rem); line-height:.9; color:var(--mint)}
.tm-third__big span{font-family:var(--display); font-weight:800; font-stretch:108%; font-size:clamp(1.1rem,2vw,1.5rem); line-height:1.15}
@media (max-width:860px){.tm-third{grid-template-columns:1fr}}
.tm-board{display:grid; grid-template-columns:repeat(6,minmax(0,1fr)); gap:22px 16px}
.tm-board .person{scroll-margin-top:110px; min-width:0}
.tm-board .person img,.tm-board .person .tm-ini{border-radius:12px}
.tm-board .person b{color:#fff}
.tm-board .person small{color:var(--aqua)}
.tm-board .tm-x{display:inline-block; margin-top:4px; font-size:.78rem; font-weight:700; color:var(--mint); text-decoration:none}
.tm-board .tm-x:hover{text-decoration:underline}
.tm-board a.tm-p:hover b{color:var(--mint)}
.tm-board .tm-p{text-decoration:none; color:inherit; display:block}
@media (max-width:1060px){.tm-board{grid-template-columns:repeat(3,minmax(0,1fr))}}
@media (max-width:520px){.tm-board{grid-template-columns:repeat(2,minmax(0,1fr))}}
.tm-join{display:grid; grid-template-columns:repeat(3,minmax(0,1fr)); gap:clamp(12px,1.6vw,18px)}
.tm-join a{display:flex; flex-direction:column; gap:6px; padding:22px; border-radius:var(--r-xl); text-decoration:none; color:var(--slate); background:#fff; border:1px solid var(--line); transition:transform .2s, box-shadow .2s}
.tm-join a:hover{transform:translateY(-4px); box-shadow:var(--shadow)}
.tm-join a b{font-family:var(--display); font-weight:800; font-stretch:108%; font-size:1.25rem; color:var(--logo-teal)}
.tm-join a b::after{content:" \\2192"; color:var(--logo-teal)}
.tm-join a span{color:var(--ink-soft); font-size:.94rem}
@media (max-width:860px){.tm-join{grid-template-columns:1fr}}
'''

LEADERS = [
    dict(name='Shael Norris', role='Co-Founder & Executive Director', img='82bc8566-88a9-4a05-b13a-f02df3e64af9', link='https://www.linkedin.com/in/shaelnorris/', id='shael-norris',
         lead=['Shael Norris is the Founding Executive Director of SafeBAE, the only national, survivor-founded and youth-led organization in the U.S. dedicated to preventing sexual violence among teens. A lifelong advocate, she began her career as a founding staffer at V-Day, where she oversaw global productions of <i>The Vagina Monologues</i> from 1999 to 2016.'],
         more=['In 2007, she launched the Campus Accountability Project to push for stronger prevention and response efforts on college campuses. Recognizing the need for early, youth-led intervention, Shael founded SafeBAE in 2015 in partnership with Daisy and Charlie Coleman, Ella Fairon, and Jada Smith. She continues to lead the organization’s national efforts in youth leadership, consent education, and mental health advocacy.']),
    dict(name='Drew Davis', role='Director of Strategic Initiatives', img='4cec0cfb-2d16-47d1-9aaa-8b797dd2ae15', link='https://www.linkedin.com/in/drewthomasdavis/', id='drew-davis',
         lead=['Drew Davis is an applied researcher and development strategist dedicated to advancing survivor justice and dismantling systems of harm through youth-led, community-driven approaches. As Director of Strategic Initiatives at SafeBAE, Drew leads development and organizational strategy, building the infrastructure that sustains youth-led programs and expands the organization’s national impact.'],
         more=['He oversees major initiatives in prevention education and youth development, with a focus on rigorous data collection, program evaluation, and long-term sustainability, ensuring all initiatives are research-informed and responsive to young people’s needs.',
               'Drew holds a Master of Public Health and a Master of Public Affairs from Brown University, where he concentrated in Black Feminist Health Science Studies, and a B.A. in Individualized Studies and Women’s, Gender, and Sexuality Studies, along with a Graduate Certificate in WGS, from Miami University of Ohio.',
               'He is a fellow of the Vermont Network’s Amplify Leadership Lab and serves as an advisor to The Every Voice Coalition, shaping state policy and strengthening support systems for survivors nationwide. Drew has also held roles with Know Your IX, Visible &amp; Resilient, and the National Coalition for Sexual Health. His work on survivor justice and Title IX has been featured in <i>USA Today</i>, <i>YES! Magazine</i>, <i>Inside Higher Ed</i>, and <i>Governing</i>.']),
    dict(name='Aela Mansmann', role='Director of Programs', img='90fc1a20-9104-456b-a0ef-df7f495a3f3f', link='https://www.linkedin.com/in/aela-mansmann-a14706180/', id='aela-mansmann',
         lead=['Aela Mansmann is the Director of Programs and Outreach at SafeBAE, where she leads national prevention initiatives, strengthens partnerships with schools across the country, and mentors young leaders to create lasting culture change. With nearly a decade of experience in youth advocacy and nonprofit leadership, she brings a track record of building sustainable initiatives that amplify student voices.'],
         more=['At SafeBAE, Aela has expanded digital resources reaching more than 86,000 students, spearheaded peer-led prevention campaigns, and coordinated programming that embeds consent education into school communities nationwide. A two-term Student Body President at Manhattanville University, she revitalized and expanded the Student Government Association, fostering a culture of inclusion, representation, and student-led problem solving on campus.',
               'Her work is grounded in the belief that education, empathy, and grassroots empowerment are the foundation of safer, more equitable communities. She is dedicated to giving young people the tools, platforms, and confidence to lead the change they wish to see.']),
    dict(name='Val Odiembo', role='Youth Engagement Manager', img='e281116a-608f-4812-8e62-40567538668e', link='https://www.linkedin.com/in/vespr000/', id='val-odiembo',
         lead=['Val Odiembo is a first-year student at Rhode Island College, pursuing a double major in Nursing and Criminal Justice with a passion for public health and violence prevention. A longtime SafeBAE leader, Val is a SafeBAE Youth Board Member and serves as SafeBAE’s Youth Engagement Manager.'],
         more=['In that role she supports the Director of Programs in strengthening youth leadership, expanding student involvement, and supporting SafeBAE club leaders across the country. Val has led SafeBAE clubs at both the Rhode Island Nurses Institute and RIC, presented at statewide health education conferences, and facilitated workshops through the Rhode Island Community Justice Program. Currently, she is organizing a training seminar for Sexual Assault Nurse Examiners (SANEs), deepening her commitment to survivor-centered care and systems change.']),
]

MEDIA = [
    ('Bailey Brewer', 'Community Engagement Coordinator', 'b-brewerheadshot'),
    ('Miwako Miki', 'Social Media Coordinator', 'composite'),
    ('Inanna Balkin', 'Staff Writer', '72295171-981d-4bfa-925b-5d7b6ec8e535-1-201-a-1-1'),
    ('Mikayla Murphy', 'Social Media', 'dsc02351-1'),
    ('Ava Legeay', 'Social Media', 'img-7608-1'),
    ('Isa Ocejo', 'Social Media', 'img-3246'),
    ('Jack Quinn', 'Social Media', 'img-0956'),
]

BOARD = [
    ('Justine Wentzell-Chang', 'Co-Chair', 'justine-wentzell-chang', 'https://www.linkedin.com/in/justine-wentzell-chang/', None),
    ('Aela Mansmann', 'Co-Chair', '90fc1a20-9104-456b-a0ef-df7f495a3f3f', 'https://www.linkedin.com/in/aela-mansmann-a14706180/', None),
    ('Len Eschweiler', 'Co-Chair', 'b71bf627-c760-48ca-9aae-6c43b1867b9c', 'https://www.linkedin.com/in/leneschweiler/', None),
    ('Michelle Hope', '', '59178f58-dc22-4d34-80cf-5240a08d9304-1', 'https://www.linkedin.com/in/missmichellehope/', None),
    ('Dorie McNamara', '', 'b0f0eb55-23cd-4dac-89eb-aff4bbc3ed3a', None, None),
    ('Joy Gorman Wettels', '', '36ff738f-68ee-4dee-8f50-1c70b4b9b011-1', 'https://www.linkedin.com/in/joy-gorman-wettels-3556a18b/', None),
    ('Arturo Rosado Taveras', '', '6585feed-8f00-43b2-83b0-5504d57e223c-1', 'https://www.linkedin.com/in/arturo-rosado-9455a82a1/', None),
    ('Theo Hutt', '', 'b9338b3f-75f1-4457-ab2c-efded5be05f0-1', 'https://www.linkedin.com/in/theo-hutt-2401a8125/', ('Watch Theo’s story', 'film-sexual-assault-of-men.html')),
    ('Apollo Knapp', '', 'apollo-knapp-headshot', None, None),
    ('Torrey DeVitto', '', '35d9e43e-01d6-4059-a4d5-1f8442813ee7-1', 'https://www.imdb.com/name/nm1722914/', ('On Celebrity Name That Tune', 'partners-press.html#torrey')),
    ('Hector Jaco', '', '7bb97e5a-79d6-47d3-b1c4-942e51144247-1', 'https://www.linkedin.com/in/hector-jaco-b51b51283/', None),
    ('Ari Zeitlin', '', 'ariz', 'https://www.linkedin.com/in/ari-zeitlin/', None),
    ('Joyce Onana', '', 'unnamed', 'https://www.linkedin.com/in/joyce-onana-mfege-/', None),
    ('Vanessa Boudewyns', '', 'vanessa-headshot-vanessa-boudewyns', 'https://www.linkedin.com/in/vboudewyns/', None),
    ('Samar Rafiqzad', '', '9ea5aa47-ab94-4190-aa9e-e4aa869eafa8-1', 'https://www.linkedin.com/in/samarrafiqzad/', None),
    ('Lisa Hoopis', '', '1517523645026', 'https://www.linkedin.com/in/lisa-hoopis-0093a343/', None),
    ('Val Odiembo', 'Youth Board Member', 'e281116a-608f-4812-8e62-40567538668e', 'https://www.linkedin.com/in/vespr000/', None),
    ('Will Rivera', '', '1735567805828', 'https://www.linkedin.com/in/riverawd/', None),
]


def slugify(s):
    return re.sub(r'[^a-z0-9]+', '-', s.lower()).strip('-')


def team():
    # face strip (unique people, linking to their entries)
    faces, seen = [], set()
    for L in LEADERS:
        faces.append((L['name'], L['img'], '#' + L['id'])); seen.add(L['name'])
    for n, r, im in MEDIA:
        faces.append((n, im, '#' + slugify(n)))
    for n, r, im, lk, x in BOARD:
        if n not in seen:
            faces.append((n, im, '#board-' + slugify(n)))
    tiles = [f'<li><a href="{h}" data-name="{esc(n)}" aria-label="{esc(n)}">{img(im, "", loading="eager") if im else f"<span class=tm-ini>{initials(n)}</span>"}</a></li>' for n, im, h in faces]
    brand = {4: f'<li aria-hidden="true"><span class="tm-tile tm-tile--daisy">{daisy()}</span></li>',
             14: '<li aria-hidden="true"><span class="tm-tile tm-tile--third"><span>⅔<small>youth board</small></span></span></li>',
             25: '<li aria-hidden="true"><span class="tm-tile tm-tile--year"><span><small>Since</small>2015</span></span></li>'}
    for i in sorted(brand):
        tiles.insert(i, brand[i])
    face_html = ''.join(tiles)

    lead_html = ''
    for L in LEADERS:
        lead = ''.join(f'<p>{p}</p>' for p in L['lead'])
        more = ''.join(f'<p>{p}</p>' for p in L['more'])
        lead_html += f'''<article class="tm-card" id="{L['id']}">
  <div class="tm-card__img">{img(L['img'], 'Portrait of ' + L['name'])}<a class="tm-li" href="{L['link']}" target="_blank" rel="noopener">LinkedIn</a></div>
  <div><h3>{esc(L['name'])}</h3><p class="tm-role">{esc(L['role'])}</p>{lead}
  <details class="tm-more"><summary><span>Read full bio</span><span>Show less</span></summary><div>{more}</div></details></div>
</article>'''

    media_html = ''.join(f'<div class="person" id="{slugify(n)}">{img(im, "Portrait of " + n)}<b>{esc(n)}</b><small>{esc(r)}</small></div>' for n, r, im in MEDIA)

    board_html = ''
    for n, r, im, lk, x in BOARD:
        pic = img(im, 'Portrait of ' + n) if im else f'<span class="tm-ini" role="img" aria-label="{esc(n)}" style="margin-bottom:10px">{initials(n)}</span>'
        role = f'<small>{esc(r)}</small>' if r else '<small>Board Member</small>'
        inner = f'{pic}<b>{esc(n)}</b>{role}'
        if lk:
            inner = f'<a class="tm-p" href="{lk}" target="_blank" rel="noopener">{inner}</a>'
        else:
            inner = f'<div class="tm-p">{inner}</div>'
        extra = f'<a class="tm-x" href="{x[1]}">{esc(x[0])} &rarr;</a>' if x else ''
        board_html += f'<div class="person" id="board-{slugify(n)}">{inner}{extra}</div>'

    body = f'''
<section class="tm-hero v2-dark">
  <span class="wm-daisy" aria-hidden="true"></span>
  <div class="wrap">
    <div class="rise">
      <nav class="crumbs" aria-label="Breadcrumb"><a href="index.html">Home</a><span>/</span><a href="about.html">About</a><span>/</span><span>Our Team</span></nav>
      <p class="eyebrow">Youth leaders, staff &amp; board</p>
      <h1>Our <span class="mk">team</span></h1>
      <p class="lede">SafeBAE is led by a committed team of youth leaders, staff, and board members who bring together lived experience, professional expertise, and a shared dedication to ending sexual violence. As a survivor-founded, youth-led organization, we center the leadership of young people while fostering cross-generational collaboration and advancing cultural change.</p>
    </div>
    <ul class="tm-mosaic" aria-label="Jump to a team member">{face_html}</ul>
  </div>
</section>

<section class="band band--paper" id="leadership">
  <div class="wrap">
    <div class="section-head"><div><p class="eyebrow">Leadership team</p><h2>The staff who run SafeBAE day to day</h2>
      <p class="lede lede--full muted">Our team includes students, educators, advocates, and professionals with backgrounds in public health, education, policy, research, media, and communications. Together, we work to create communities where safety and consent come first, before anything else.</p></div></div>
    <div class="tm-lead">{lead_html}</div>
  </div>
</section>

<section class="band band--aqua" id="youth-media">
  <div class="wrap">
    <div class="section-head"><div><h2>Youth media &amp; communications team</h2></div>{btn('Follow @safe_bae', 'https://www.instagram.com/safe_bae/', 'slate')}</div>
    <div class="tm-media">{media_html}</div>
  </div>
</section>

<section class="band band--slate" id="board">
  <div class="wrap">
    <div class="tm-third">
      <div><p class="eyebrow">Board of Directors</p><h2>A board that answers to young people</h2>
        <p class="lede" style="color:rgba(255,255,255,.88)">SafeBAE’s Board is intentionally composed of at least ⅔ youth, reflecting our deep commitment to youth leadership. This structure ensures that SafeBAE remains accountable to the young people leading this work, with youth playing a central role in all aspects of our governance, strategic planning, and decision-making.</p></div>
      <div aria-hidden="true">
        <div class="tm-third__bar"><span>Youth</span><span>Youth</span><span>&nbsp;</span></div>
        <div class="tm-third__big"><b>⅔</b><span>of the board, at minimum, is youth</span></div>
      </div>
    </div>
    <div class="tm-board">{board_html}</div>
  </div>
</section>

<section class="band band--paper band--tight">
  <div class="wrap">
    <div class="section-head"><div><h2>Ways to join this work</h2></div></div>
    <div class="tm-join">
      <a href="peer-educator.html"><b>Become a Peer Educator</b><span>Free, self-paced certification for high school students.</span></a>
      <a href="clubs.html"><b>Lead a SafeBAE club</b><span>Start, affiliate or restart a chapter at your school.</span></a>
      <a href="contact.html"><b>Contact the team</b><span>Reach our staff about programs, press or partnerships.</span></a>
    </div>
  </div>
</section>
{give_band()}
'''
    page('team.html', 'Our Team · SafeBAE', 'Meet SafeBAE’s leadership team, youth media team and board of directors, a team of youth leaders and professionals working to end sexual violence.',
         body, active='about', body_class='pg-team', head_extra=css(TEAM_CSS))


# =====================================================================
# IMPACT
# =====================================================================
IMPACT_CSS = '''
.im-hero{background-color:var(--slate-deep); color:#fff}
.im-hero .wrap{padding-block:clamp(44px,5.5vw,80px) clamp(40px,5vw,64px)}
.im-hero__top{display:grid; grid-template-columns:minmax(0,1.18fr) minmax(0,.82fr); gap:clamp(28px,4.5vw,60px); align-items:center}
.im-hero h1{font-size:clamp(2.4rem,4.4vw,4rem)!important}
.im-fig{position:relative; margin:0 0 18px; animation:sb-rise-r 1s .1s var(--ease) both}
.im-fig > img{width:100%; aspect-ratio:4/3; object-fit:cover; border-radius:var(--r-xl); box-shadow:0 30px 60px -30px rgba(0,0,0,.7)}
.im-fig .sticker{position:absolute; left:-12px; top:18px}
.im-datacard{position:absolute; right:-14px; bottom:-26px; width:min(300px,72%); background:#fff; color:var(--slate); border-radius:16px; padding:16px 18px; box-shadow:var(--shadow-soft), 0 10px 30px -12px rgba(0,0,0,.45)}
.im-datacard small{display:block; font-family:var(--mono); font-size:.64rem; letter-spacing:.08em; text-transform:uppercase; color:var(--logo-teal); font-weight:600}
.im-datacard b{display:block; font-family:var(--display); font-weight:900; font-stretch:120%; font-size:2.4rem; line-height:1; margin:4px 0 2px; color:var(--slate)}
.im-datacard span{display:block; font-size:.84rem; font-weight:600; line-height:1.35}
.im-datacard i{display:block; height:10px; border-radius:5px; background:var(--mist); margin-top:10px; overflow:hidden}
.im-datacard i::before{content:""; display:block; height:100%; width:70%; background:var(--coral); border-radius:0 5px 5px 0}
@media (max-width:900px){.im-hero__top{grid-template-columns:1fr} .im-fig{max-width:560px; margin-bottom:40px} .im-datacard{right:8px}}
.im-hero h1{font-size:var(--fs-h1); font-stretch:122%; font-weight:900; text-transform:uppercase; line-height:.92; letter-spacing:-.02em; margin:0 0 .35em}

.im-hero .lede{color:rgba(255,255,255,.88); max-width:none}
.im-hero .eyebrow{color:var(--mint)}

.im-kpis{display:grid; grid-template-columns:repeat(3,minmax(0,1fr)); gap:12px; margin-top:clamp(26px,3vw,40px)}
.im-kpi{background:rgba(255,255,255,.05); border:1px solid var(--line-dark); border-radius:14px; padding:18px 20px}
.im-kpi b{display:block; font-family:var(--display); font-weight:900; font-stretch:122%; font-size:clamp(2.4rem,4.6vw,4rem); line-height:.95; color:var(--mint); letter-spacing:-.02em}
.im-kpi span{display:block; margin-top:8px; font-weight:600; font-size:.95rem; color:rgba(255,255,255,.88); line-height:1.35}
.im-kpi small{display:block; margin-top:6px; font-family:var(--mono); font-size:.68rem; letter-spacing:.08em; text-transform:uppercase; color:var(--aqua)}
@media (max-width:760px){.im-kpis{grid-template-columns:1fr}}

.im-paper{display:grid; grid-template-columns:minmax(0,1fr) minmax(0,1fr); gap:clamp(24px,4vw,56px); align-items:start}
.im-paper__img{position:relative}
.im-paper__img img{width:100%; border-radius:var(--r-xl); box-shadow:var(--shadow-soft)}
.im-paper__img .sticker{position:absolute; left:-10px; bottom:-14px}
.im-journal{display:inline-flex; align-items:center; gap:10px; padding:8px 12px; border-radius:8px; background:var(--aqua); font-family:var(--mono); font-size:.74rem; letter-spacing:.06em; text-transform:uppercase; font-weight:600; margin-bottom:16px}
.im-authors{display:grid; grid-template-columns:repeat(3,minmax(0,1fr)); gap:10px; margin:0}
.im-authors div{border-top:3px solid var(--mint); padding-top:10px}
.im-authors b{display:block; font-family:var(--display); font-stretch:106%; line-height:1.15}
.im-authors small{display:block; color:var(--ink-soft); font-size:.8rem; line-height:1.35; margin-top:2px}
@media (max-width:860px){.im-paper{grid-template-columns:1fr} .im-paper > div:first-child{order:2} .im-authors{grid-template-columns:1fr}}

.im-split{display:grid; grid-template-columns:minmax(0,.85fr) minmax(0,1.15fr); gap:clamp(28px,5vw,64px); align-items:start}
@media (max-width:960px){.im-split{grid-template-columns:1fr}}
.im-meta{display:flex; flex-wrap:wrap; gap:8px; margin:18px 0 22px}
.im-meta span{font-family:var(--mono); font-size:.72rem; letter-spacing:.06em; text-transform:uppercase; padding:6px 10px; border-radius:6px; border:1.5px solid currentColor; opacity:.9}

.im-bars{list-style:none; margin:0; padding:0; display:grid; gap:12px}
.im-bars li{margin:0; display:grid; grid-template-columns:clamp(104px,10vw,136px) minmax(0,1fr); gap:4px 18px; align-items:center; padding:14px 16px; border-radius:14px; background:var(--bar-card, rgba(255,255,255,.05)); border:1px solid var(--bar-line, var(--line-dark))}
.im-bars__v{grid-row:span 2; font-family:var(--display); font-weight:900; font-stretch:118%; font-size:clamp(1.8rem,3vw,2.6rem); white-space:nowrap; line-height:1; letter-spacing:-.02em; color:var(--bar-num, #fff)}
.im-bars__t{font-weight:600; font-size:.95rem; line-height:1.35}
.im-bars__k{display:block; font-family:var(--mono); font-size:.66rem; letter-spacing:.1em; text-transform:uppercase; font-weight:600; color:var(--bar-k, var(--aqua)); margin-bottom:2px}
.im-bars__track{height:12px; border-radius:6px; background:var(--bar-track, rgba(255,255,255,.1)); overflow:hidden; margin-top:6px}
.im-bars__track i{display:block; height:100%; width:calc(var(--v) * 1%); background:var(--bar-fill, var(--coral)); border-radius:0 6px 6px 0; transition:width 1.1s cubic-bezier(.2,.8,.2,1)}
.js .im-bars:not(.in) .im-bars__track i{width:0}
.im-bars li:nth-child(2) i{transition-delay:.08s} .im-bars li:nth-child(3) i{transition-delay:.16s} .im-bars li:nth-child(4) i{transition-delay:.24s} .im-bars li:nth-child(5) i{transition-delay:.32s} .im-bars li:nth-child(6) i{transition-delay:.4s} .im-bars li:nth-child(7) i{transition-delay:.48s}
.im-scale{display:flex; justify-content:space-between; font-family:var(--mono); font-size:.64rem; letter-spacing:.08em; color:var(--bar-k, var(--aqua)); margin:10px 0 0 calc(clamp(104px,10vw,136px) + 34px); opacity:.8}
@media (max-width:520px){.im-bars li{grid-template-columns:1fr} .im-bars__v{grid-row:auto} .im-scale{margin-left:16px}}
.im-light{--bar-card:#fff; --bar-line:var(--line); --bar-num:var(--logo-teal); --bar-k:var(--logo-teal); --bar-track:var(--mist); --bar-fill:var(--teal)}
.im-light .im-bars__t{color:var(--slate)}

.im-train{display:grid; grid-template-columns:repeat(2,minmax(0,1fr)); gap:12px; margin:20px 0 24px}
.im-train div{background:#fff; border:1px solid var(--line); border-radius:14px; padding:16px 18px}
.im-train b{display:block; font-family:var(--display); font-weight:900; font-stretch:122%; font-size:clamp(2rem,3.6vw,3rem); line-height:1; color:var(--logo-teal)}
.im-train span{display:block; font-size:.9rem; font-weight:600; color:var(--ink-soft); margin-top:6px; line-height:1.35}
.im-quotes{display:grid; grid-template-columns:repeat(2,minmax(0,1fr)); gap:clamp(14px,2vw,22px); margin-top:clamp(28px,4vw,44px)}
.im-q{margin:0; background:var(--slate) var(--grain); color:#fff; border-radius:var(--r-xl); padding:clamp(20px,2.6vw,30px); display:flex; flex-direction:column}
.im-q p{font-family:var(--display); font-weight:700; font-stretch:103%; font-size:clamp(1.05rem,1.5vw,1.25rem); line-height:1.4; margin:0}
.im-q p::before{content:"\\201C"; display:block; font-size:3.4em; line-height:.6; color:var(--mint); font-stretch:125%; margin-bottom:.12em}
.im-q cite{margin-top:auto; padding-top:14px; font-style:normal; font-family:var(--mono); font-size:.72rem; letter-spacing:.08em; text-transform:uppercase; color:var(--aqua)}
@media (max-width:860px){.im-quotes{grid-template-columns:1fr}}

.im-annual{display:grid; grid-template-columns:minmax(0,1fr) minmax(0,1.1fr); gap:clamp(24px,4vw,56px); align-items:center; background:var(--teal); color:#fff; border-radius:var(--r-xl); padding:clamp(24px,4vw,48px); position:relative; overflow:hidden}
.im-annual__cover{aspect-ratio:8.5/11; max-width:330px; width:100%; margin-inline:auto; background:var(--mint); color:var(--slate); border-radius:8px; padding:26px 24px; display:flex; flex-direction:column; justify-content:space-between; box-shadow:0 30px 60px -20px rgba(0,0,0,.5); transform:rotate(-3deg)}
.im-annual__cover b{font-family:var(--display); font-weight:900; font-stretch:125%; font-size:clamp(3.6rem,7vw,5.4rem); line-height:.85; letter-spacing:-.03em}
.im-annual__cover span{font-family:var(--display); font-weight:800; font-stretch:110%; text-transform:uppercase; font-size:1.2rem; line-height:1.05}
.im-annual__cover small{font-family:var(--mono); font-size:.7rem; letter-spacing:.08em; text-transform:uppercase}
.im-annual .eyebrow{color:#fff}
.im-annual h3{font-size:clamp(1.6rem,2.8vw,2.4rem); margin:.1em 0 .4em}
.im-annual p{color:rgba(255,255,255,.9)}
@media (max-width:760px){.im-annual{grid-template-columns:1fr} .im-annual__cover{max-width:220px}}
.im-shelf{display:grid; grid-template-columns:repeat(7,minmax(0,1fr)); gap:10px; margin-top:clamp(26px,3vw,40px); align-items:end}
.im-book{display:flex; flex-direction:column; justify-content:space-between; text-decoration:none; color:#fff; background:var(--slate); border-radius:8px 8px 4px 4px; padding:14px 12px; min-height:230px; position:relative; transition:transform .25s; box-shadow:inset -6px 0 0 rgba(0,0,0,.14)}
.im-book:hover{transform:translateY(-10px)}
.im-book b{font-family:var(--display); font-weight:900; font-stretch:125%; font-size:clamp(1.6rem,2.6vw,2.3rem); line-height:.9; writing-mode:vertical-rl; transform:rotate(180deg); align-self:flex-start; letter-spacing:.02em}
.im-book span{font-family:var(--mono); font-size:.66rem; letter-spacing:.08em; text-transform:uppercase; line-height:1.35}
.im-book span::after{content:" \\2193"}
.im-book:nth-child(1){background:var(--logo-teal); min-height:250px}
.im-book:nth-child(2){background:var(--mint); color:var(--slate); min-height:240px}
.im-book:nth-child(3){background:var(--teal); min-height:262px}
.im-book:nth-child(4){background:var(--slate); min-height:236px}
.im-book:nth-child(5){background:var(--aqua); color:var(--slate); min-height:254px}
.im-book:nth-child(6){background:var(--logo-teal); min-height:228px}
.im-book:nth-child(7){background:var(--slate-deep); min-height:246px}
.im-shelf-base{height:10px; border-radius:0 0 6px 6px; background:var(--gray); margin-top:0}
@media (max-width:960px){.im-shelf{grid-template-columns:repeat(4,minmax(0,1fr)); gap:18px 10px} .im-book{min-height:190px!important; border-bottom:8px solid var(--gray); border-radius:8px 8px 0 0} .im-shelf-base{display:none}}
@media (max-width:520px){.im-book{min-height:160px!important; padding:12px 10px} .im-book b{font-size:1.5rem} .im-book span{font-size:.6rem}}
'''

IMPACT_JS = '''<script>(function(){
  var reduce = window.matchMedia && window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  if(!reduce) document.querySelectorAll('[data-count]').forEach(function(el, k){
    var n = +el.getAttribute('data-count'), pre = el.getAttribute('data-prefix') || '', suf = el.getAttribute('data-suffix') || '', t0 = null, dur = 1400 + k * 150;
    function fmt(v){ return pre + Math.round(v).toLocaleString('en-US') + suf; }
    el.textContent = fmt(0);
    function step(t){ if(t0 === null) t0 = t; var q = Math.min(1, (t - t0) / dur); el.textContent = fmt(n * (1 - Math.pow(1 - q, 3))); if(q < 1) requestAnimationFrame(step); }
    setTimeout(function(){ requestAnimationFrame(step); }, 350);
  });
})();
(function(){
  var els = document.querySelectorAll('.im-bars'); if(!els.length) return;
  if(!('IntersectionObserver' in window)){ els.forEach(function(e){ e.classList.add('in'); }); return; }
  var io = new IntersectionObserver(function(es){ es.forEach(function(e){ if(e.isIntersecting){ e.target.classList.add('in'); io.unobserve(e.target); } }); }, {threshold:.2});
  els.forEach(function(e){ io.observe(e); });
})();</script>'''


def bars(items, scale=True):
    li = ''.join(f'<li style="--v:{v}" title="{esc(lbl)}: {esc(shown)}"><span class="im-bars__v">{esc(shown)}</span><span class="im-bars__t"><span class="im-bars__k">{esc(k)}</span>{esc(t)}</span><span class="im-bars__track" aria-hidden="true"><i></i></span></li>'
                 for v, shown, k, t, lbl in items)
    sc = '<div class="im-scale" aria-hidden="true"><span>0%</span><span>50%</span><span>100%</span></div>' if scale else ''
    return f'<ul class="im-bars">{li}</ul>{sc}'


def impact():
    climate = [
        (53, '53%', 'Sexual violence', 'Agreed that sexual violence was a serious problem at their school', 'Sexual violence'),
        (59, '59%', 'Rape culture', 'Agreed that when students reported being assaulted, their peers didn’t believe them', 'Rape culture'),
        (33.3, '1/3', 'Support', 'Of students agreed that school staff didn’t help students who’d been assaulted', 'One third of students'),
        (56, '56%', 'Reporting', 'Agreed their school didn’t adequately teach them where or how to report sexual violence', 'Reporting'),
        (70, '70%', 'Title IX', 'Agreed that their school didn’t adequately teach their Title IX rights', 'Title IX'),
        (57, '57%', 'Bystander intervention', 'Agreed that their school didn’t adequately teach bystander intervention', 'Bystander intervention'),
        (20, '20%', 'Dress code', 'Agreed that their school’s dress code was applied unfairly', 'Dress code'),
    ]
    know = [
        (81, '+81%', 'Title IX', 'Increase in understanding Title IX rights', 'Title IX rights'),
        (66, '+66%', 'Bystander intervention', 'Increase in understanding how to be an active bystander', 'Active bystander'),
        (56, '+56%', 'Healing', 'Increase in understanding healing options after experiencing sexual violence', 'Healing options'),
        (43, '+43%', 'Reporting', 'Increase in understanding how to report sexual violence', 'Reporting'),
        (39, '+39%', 'Supporting a peer', 'Increase in understanding how to respond to a peer disclosing sexual violence', 'Responding to a disclosure'),
    ]
    act = [
        (38, '+38%', 'Pressure', 'Increase in stopping a partner who was pressuring sexually', 'Stopping a partner'),
        (30, '+30%', 'Unhealthy relationships', 'Increase in understanding steps to safely leave an unhealthy relationship', 'Leaving safely'),
        (26, '+26%', 'Rape culture', 'Increase in understanding all of the elements that contribute to rape culture', 'Rape culture'),
        (20, '+20%', 'Consent', 'Increase in discussing consent with a partner', 'Discussing consent'),
        (17, '+17%', 'Media', 'Increase in identifying negative actions, relationship models, or how sex is portrayed in the media', 'Media literacy'),
    ]
    reports = [
        ('2025', 'Midyear report', WP + '2025/08/2025-Mid-Year-Impact-Report-11.pdf'),
        ('2024', 'Annual report', WP + '2025/08/2024-Annual-Report-6.pdf'),
        ('2023', 'Annual report', WP + '2025/08/2023-Annual-Report-5.pdf'),
        ('2022', 'Annual report', WP + '2025/08/2022-Annual-Report-2.pdf'),
        ('2019', 'Annual report', WP + '2025/08/2019-annual-report-1.pdf'),
        ('2018', 'Annual report', WP + '2025/08/2018-annual-report-1.pdf'),
        ('2017', 'Annual report', WP + '2025/08/2017-annual-report-1-1.pdf'),
    ]
    shelf = ''.join(f'<a class="im-book" href="{u}" target="_blank" rel="noopener" aria-label="{y} {t.lower()} (PDF)"><b>{y}</b><span>{t}<br>PDF</span></a>' for y, t, u in reports)
    data_docs = ''.join(row(t, d, u, ['Google Doc']) for t, d, u in [
        ('2020 Virtual Summit Data', 'Findings gathered at SafeBAE’s 2020 virtual summit.', 'https://docs.google.com/document/d/1qjbGD9T-Vkvn4hCD6VNke9pGmvPMIqjr9owY0m5QCD4/edit'),
        ('2019 Student Survey Data Reports', 'Student survey results from 2019.', 'https://docs.google.com/document/d/1pLleAP3Cr2VWxoDQKCs5RTO2BgEjyM-KoQchHuDuoJc/edit'),
        ('2017/2018 Student Survey Data Report', 'Student survey results from the 2017/2018 school year.', 'https://docs.google.com/document/d/1dsZOUKgcveqjQzKrh7LUF8mr-d0QBewDPo-WJxr8RXM/edit'),
    ])
    p = pod('0JfMJbj7ZvISm8m7gp39YS')

    body = f'''
<section class="im-hero v2-dark">
  <span class="wm-daisy" aria-hidden="true"></span>
  <div class="wrap">
    <div class="im-hero__top">
      <div class="rise">
        <nav class="crumbs" aria-label="Breadcrumb"><a href="index.html">Home</a><span>/</span><a href="about.html">About</a><span>/</span><span>Data &amp; Impact</span></nav>
        <h1><span class="mk">Data,</span> findings &amp; learning</h1>
        <p class="lede">At SafeBAE, we believe sexual violence prevention should always be youth-led and evidence-driven. We collect data to understand our impact and to make sure we’re reaching students, shifting school culture, and building the skills and confidence young people need to create safer communities. Our findings come from ongoing evaluations, youth-designed surveys, internal assessments, and published research.</p>
      </div>
      <figure class="im-fig">{img('img-2400', 'Students and SafeBAE facilitators sitting in a circle during a workshop', loading='eager')}<span class="sticker">Youth-designed surveys</span>
        <figcaption class="im-datacard"><small>Climate survey, 2020–23</small><b>70%</b><span>agreed their school didn’t adequately teach their Title IX rights</span><i aria-hidden="true"></i></figcaption>
      </figure>
    </div>
    <div class="im-kpis">
      <div class="im-kpi"><b data-count="849">849</b><span>students in 45 states answered our school climate survey</span><small>2020–23</small></div>
      <div class="im-kpi"><b data-count="3000" data-suffix="+">3,000+</b><span>young people certified as Peer Educators</span><small>Certified Peer Educator Training</small></div>
      <div class="im-kpi"><b data-count="81" data-prefix="+" data-suffix="%">+81%</b><span>increase in students’ understanding of their Title IX rights after the training</span><small>2023 efficacy data</small></div>
    </div>
  </div>
</section>

<section class="band band--paper" id="research">
  <div class="wrap im-paper">
    <div>
      <div class="im-paper__img">{img('empowering-educators-2', 'Graphic: SafeBAE’s approach to preventing dating violence backed by newly published research')}<span class="sticker">Published research</span></div>
      <p class="eyebrow" style="margin-top:34px">Co-authors</p>
      <div class="im-authors">
        <div><b>Shael Norris</b><small>Executive Director, SafeBAE</small></div>
        <div><b>Dr. Lindsay Orchowski</b><small>Brown University, Rhode Island Hospital &amp; Lifespan</small></div>
        <div><b>Dr. Prachi Bhuptani</b><small>Brown University, Rhode Island Hospital &amp; Lifespan</small></div>
      </div>
    </div>
    <div>
      <p class="im-journal">Journal of Child Sexual Abuse</p>
      <h2>SafeBAE’s research, published</h2>
      <p>Most school-based sexual violence prevention programs are not evidence-based, and even fewer are designed with or by young people. SafeBAE’s prevention is rooted in youth leadership, survivor-centered programming, and real-world data. Our evaluation efforts make sure our model is effective, equitable, and responsive to the communities we serve.</p>
      <p>That commitment to rigor led to our research being published in the <i>Journal of Child Sexual Abuse</i>. Co-authored by our Executive Director, Shael Norris, with Dr. Lindsay Orchowski and Dr. Prachi Bhuptani of Brown University, Rhode Island Hospital, and Lifespan Hospital, the study shows that SafeBAE’s approach to preventing sexual violence is effective and transformative.</p>
      <div class="btns">{btn('Read the study', PAPER, 'slate')}{btn('Who we work with', 'partners-press.html', 'ghost', arrow=True)}</div>
      <div style="margin-top:18px">{spotify(p[0], 'Listen: ' + p[1], p[2])}</div>
    </div>
  </div>
</section>

<section class="band band--aqua band--tight" id="efficacy">
  <div class="wrap">
    <p class="eyebrow">2023 program efficacy data</p>
    <h2>What we measure, and what we found</h2>
    <p class="lede lede--full" style="margin:0">Since our founding in 2015, SafeBAE has collected and analyzed data across all programs and projects. With the guidance of our research partners, we have published dedicated evaluations and shared qualitative insights in our annual reports. Our most recent evaluation of the Certified Peer Educator Training shows its impact on both the knowledge and the actions of participating students.</p>
  </div>
</section>

<section class="band band--deep" id="climate">
  <div class="wrap im-split">
    <div>
      <p class="eyebrow">Climate survey</p>
      <h2>What students told us about their schools</h2>
      <div class="im-meta"><span>849 students surveyed</span><span>45 US states</span><span>2020–23</span></div>
      <p style="color:rgba(255,255,255,.86)">Since 2015, our work with thousands of students has confirmed what the data now makes undeniable: sexual violence is at crisis levels for teens across the country. The {a('CDC’s Youth Risk Behavior Survey', 'https://www.cdc.gov/yrbs/results/2023-yrbs-results.html', 'link')} underscores the severity of this issue, and SafeBAE set out to learn how it plays out in schools every day.</p>
      <p style="color:rgba(255,255,255,.86)">Through the <b>SafeBAE National School Sexual Violence Climate Survey (2020–23)</b>, we partnered with students and schools to capture the lived realities of school culture, focusing on safety, support systems, and institutional accountability. The findings reveal the dangerous environments many secondary students face, and provide evidence to drive system-level change and strengthen prevention.</p>
      <div class="btns" style="margin-top:22px">{btn('Download the climate survey', WP + '2023/06/climate-survey-data.pdf', 'mint')}</div>
      <p class="small" style="margin-top:10px;color:rgba(255,255,255,.65)">PDF, 159.69 KB</p>
    </div>
    <div>{bars(climate)}</div>
  </div>
</section>

<section class="band band--paper" id="training">
  <div class="wrap im-split">
    <div>
      <p class="eyebrow">Peer Educator Training data</p>
      <h2>Evidence that students learn, and act</h2>
      <p>As troubling as our Climate Survey findings are, the results from our {a('Certified Peer Educator Training', 'peer-educator.html', 'link')} offer hope and clear evidence of impact. More than 2,000 students across 45 states have completed the training, showing measurable growth in knowledge, attitudes, and confidence around consent and prevention.</p>
      <p>Grounded in youth experiences and aligned with the National Health Education Standards (NHES), the curriculum reflects best practices for school-based prevention while staying student-driven and survivor-centered. Developed over eight years, it has become one of the most comprehensive and authentic prevention resources available, endorsed by both students and educators.</p>
      <div class="im-train"><div><b>1,057</b><span>students took part in the training evaluated in 2023</span></div><div><b>179</b><span>of them completed both pre- and post-surveys</span></div></div>
      <div class="btns">{btn('Download the training data', WP + '2023/06/2023-BAE-training-data-top-sheet-1.pdf', 'slate')}{btn('Take the training', 'peer-educator.html', 'ghost', arrow=True)}</div>
      <p class="small muted" style="margin-top:10px">PDF, 178.39 KB</p>
    </div>
    <div class="im-light" data-tabs="impact-training">
      <div class="tabs" role="tablist" aria-label="Training results">
        <button class="tab" role="tab" id="tab-knowledge" aria-controls="panel-knowledge" aria-selected="true" tabindex="0">Knowledge</button>
        <button class="tab" role="tab" id="tab-actions" aria-controls="panel-actions" aria-selected="false" tabindex="-1">Actions &amp; results</button>
      </div>
      <div role="tabpanel" id="panel-knowledge" aria-labelledby="tab-knowledge">{bars(know, scale=False)}</div>
      <div role="tabpanel" id="panel-actions" aria-labelledby="tab-actions" hidden>{bars(act, scale=False)}</div>
    </div>
  </div>
  <div class="wrap">
    <div class="im-quotes">
      <figure class="im-q reveal"><p>As I went on in the training, I felt like I could be a more helpful and supportive person and that I would know what to do if something happened to me or anyone I know. I feel confident that I can help people in all sorts of situations and I am more educated on the effects of rape culture.</p><cite>Student participant</cite></figure>
      <figure class="im-q reveal"><p>This is an amazing experience and it was so beneficial for me. Your program has helped me know how to help my friend who experienced sexual assault, set boundaries with my own boyfriend and provoked some conversations about consent that we might not have had otherwise, and I have shared your program with my classmates and club members because I believe your program is something everyone should do.</p><cite>Student participant</cite></figure>
    </div>
  </div>
</section>

<section class="band band--slate" id="video">
  <div class="wrap split">
    <div>
      <p class="eyebrow">Peer Education Data Report, 2020–2022</p>
      <h2>Does prevention work?</h2>
      <p class="lede" style="color:rgba(255,255,255,.88)">A look at the findings of SafeBAE’s Peer Education Data Report (2020–2022) and what the data shows about the impact of peer-to-peer education.</p>
      <div class="btns">{btn('More films in the Library', 'library.html#films', 'ghost', arrow=True)}</div>
    </div>
    {yt('BmLIDyPsQz4', 'Does Prevention Work? SafeBAE’s Data & Impact Report', label='Watch')}
  </div>
</section>

<section class="band band--paper" id="reports">
  <div class="wrap">
    <div class="im-annual">
      <div class="im-annual__cover" aria-hidden="true"><small>SafeBAE Annual Report</small><b>2025</b><span>Youth<br>Leading</span></div>
      <div>
        <p class="eyebrow">Youth Leading: 2025 Annual Report</p>
        <h3>SafeBAE’s Expanding Network for Change</h3>
        <p>See how SafeBAE youth leaders created safer schools, supported their peers and shifted culture across the country this year. Read the full annual report and see how you can support the next decade of SafeBAE’s work.</p>
        <div class="btns" style="margin-top:20px">{btn('Download the 2025 report', WP + '2026/01/2025-Annual-Report.pdf', 'mint')}{btn('Support the next decade', 'donate.html', 'white', arrow=True)}</div>
      </div>
    </div>
    <div class="section-head" style="margin-top:clamp(40px,5vw,64px);margin-bottom:0"><div><h2>Past annual reports</h2></div></div>
    <div class="im-shelf">{shelf}</div>
    <div class="im-shelf-base" aria-hidden="true"></div>
    <div class="rows" style="margin-top:clamp(28px,3vw,40px)">{data_docs}</div>
  </div>
</section>
{give_band()}
'''
    page('impact.html', 'Data & Impact · SafeBAE', 'SafeBAE’s published research, National School Sexual Violence Climate Survey, Certified Peer Educator Training efficacy data and annual reports.',
         body, active='about', body_class='pg-impact', head_extra=css(IMPACT_CSS), scripts=IMPACT_JS)


# =====================================================================
# PARTNERS & PRESS
# =====================================================================
PP_CSS = '''
.pp-hero{background-color:var(--slate-deep); color:#fff}
.pp-hero .wrap{padding-block:clamp(44px,5.5vw,80px) clamp(36px,4.5vw,56px)}
.pp-hero__grid{display:grid; grid-template-columns:minmax(0,1.05fr) minmax(0,.95fr); gap:clamp(28px,5vw,64px); align-items:center}
.pp-hero h1{font-size:var(--fs-h1); font-stretch:122%; font-weight:900; text-transform:uppercase; line-height:.92; letter-spacing:-.02em; margin:0 0 .35em}
.pp-hero .lede{max-width:none; color:rgba(255,255,255,.88)}
.pp-stack{position:relative; aspect-ratio:1.18; animation:sb-rise-r 1s .1s var(--ease) both}
.pp-stack > *{position:absolute; display:block; overflow:hidden; box-shadow:0 26px 50px -24px rgba(0,0,0,.75); transition:transform .5s var(--ease)}
.pp-stack img{width:100%; height:100%; object-fit:cover}
.pp-stack__film{right:0; top:2%; width:80%; aspect-ratio:16/9; border-radius:var(--r-xl); transform:rotate(2.5deg)}
.pp-stack__c{width:37%; aspect-ratio:1; border-radius:14px; border:4px solid var(--slate-deep)}
.pp-stack__c:nth-of-type(2){left:0; bottom:5%; transform:rotate(-9deg)}
.pp-stack__c:nth-of-type(3){left:27%; bottom:0; transform:rotate(-1deg); z-index:2}
.pp-stack__c:nth-of-type(4){left:54%; bottom:7%; transform:rotate(8deg)}
.pp-stack:hover .pp-stack__c:nth-of-type(2){transform:rotate(-14deg) translate(-12px,-6px)}
.pp-stack:hover .pp-stack__c:nth-of-type(4){transform:rotate(13deg) translate(14px,-8px)}
.pp-stack:hover .pp-stack__film{transform:rotate(4deg) translateY(-8px)}
.pp-stack .sticker{position:absolute; left:4%; top:8%; overflow:visible; box-shadow:3px 3px 0 var(--slate); z-index:3}
@media (max-width:900px){.pp-hero__grid{grid-template-columns:1fr} .pp-stack{max-width:520px; width:100%}}
.pp-strip{display:flex; flex-wrap:wrap; align-items:center; gap:12px 14px; margin-top:clamp(28px,3.4vw,44px); padding-top:22px; border-top:1px solid var(--line-dark)}
.pp-strip .pp-chip img{filter:brightness(0) invert(1); opacity:.9}
.pp-strip .pp-chip--text{color:#fff; opacity:.9}
.pp-strip > span:first-child{font-family:var(--mono); font-size:.72rem; letter-spacing:.1em; text-transform:uppercase; font-weight:600; color:var(--mint); margin-right:6px}
.pp-chip{display:inline-flex; align-items:center; justify-content:center; background:transparent; border-radius:10px; padding:10px 6px; height:58px; text-decoration:none; color:var(--slate); font-family:var(--display); font-weight:800; font-stretch:100%}
.pp-chip img{height:34px; width:auto; max-width:150px; object-fit:contain}
.pp-chip--text{font-family:"Times New Roman", Georgia, serif; font-weight:700; font-size:1.05rem; letter-spacing:-.01em}

.pp-press{border-top:2px solid var(--slate)}
.pp-pr{display:grid; grid-template-columns:200px minmax(0,1fr) auto; gap:clamp(16px,3vw,40px); align-items:center; padding:clamp(18px,2.4vw,28px) 0; border-bottom:1px solid var(--line); text-decoration:none; color:var(--slate); transition:background .2s, padding .2s}
.pp-pr:hover{background:var(--mist); padding-inline:14px}
.pp-pr .pp-chip{height:72px; width:100%; justify-content:flex-start}
.pp-pr .pp-chip img{height:46px; max-width:160px}
.pp-pr h3{font-size:clamp(1.25rem,2.2vw,1.9rem); line-height:1.12; margin:0}
.pp-pr small{display:block; font-family:var(--mono); font-size:.7rem; letter-spacing:.08em; text-transform:uppercase; color:var(--logo-teal); margin-top:8px; font-weight:600}
.pp-pr .go{width:46px; height:46px; border-radius:50%; display:grid; place-items:center; background:var(--aqua); color:var(--logo-teal); font-weight:800; font-size:1.1rem}
.pp-pr:hover .go{background:var(--mint)}
@media (max-width:720px){.pp-pr{grid-template-columns:1fr auto} .pp-pr .pp-chip{grid-column:1/-1; width:180px}}

.pp-eps{display:grid; grid-template-columns:repeat(3,minmax(0,1fr)); gap:clamp(14px,2vw,22px)}
.pp-ep{background:rgba(255,255,255,.05); border:1px solid var(--line-dark); border-radius:var(--r-xl); overflow:hidden; display:flex; flex-direction:column}
.pp-ep__play{position:relative; display:block; aspect-ratio:16/9; overflow:hidden; background:#000; color:#fff; text-decoration:none}
.pp-ep__play img{width:100%; height:100%; object-fit:cover; opacity:.78; transition:transform .5s, opacity .3s}
.pp-ep__play:hover img{transform:scale(1.04); opacity:.6}
.pp-ep__play b{position:absolute; left:14px; bottom:14px; display:inline-flex; align-items:center; gap:8px; background:var(--mint); color:var(--slate); border-radius:999px; padding:8px 14px 8px 10px; font-family:var(--display); font-weight:800; font-size:.9rem}
.pp-ep__play b svg{width:16px; height:16px}
.pp-ep iframe{display:block; margin:0}
.pp-ep__body{padding:18px 20px 20px; display:flex; flex-direction:column; gap:8px; flex:1}
.pp-ep__body small{font-family:var(--mono); font-size:.68rem; letter-spacing:.08em; text-transform:uppercase; color:var(--mint); font-weight:600}
.pp-ep__body h3{font-size:1.3rem; margin:0; color:#fff}
.pp-ep__body p{margin:0; font-size:.92rem; color:rgba(255,255,255,.82); line-height:1.5}
.pp-ep__links{margin-top:auto; padding-top:8px; display:flex; flex-wrap:wrap; gap:6px 14px; font-size:.85rem; font-weight:700}
.pp-ep__links a{color:var(--aqua)}
@media (max-width:960px){.pp-eps{grid-template-columns:repeat(2,minmax(0,1fr))}}
@media (max-width:620px){.pp-eps{grid-template-columns:1fr}}

.pp-torrey{display:grid; grid-template-columns:minmax(0,1fr) minmax(0,1fr); gap:clamp(28px,5vw,64px); align-items:center}
.pp-money{display:flex; align-items:baseline; gap:14px; flex-wrap:wrap; margin:6px 0 18px}
.pp-money b{font-family:var(--display); font-weight:900; font-stretch:125%; font-size:clamp(3.4rem,8vw,6.6rem); line-height:.9; letter-spacing:-.03em}
.pp-money span{font-family:var(--display); font-weight:800; font-stretch:106%; font-size:clamp(1rem,1.6vw,1.25rem); max-width:16ch; line-height:1.15}
@media (max-width:860px){.pp-torrey{grid-template-columns:1fr}}

.pp-films{display:grid; grid-template-columns:repeat(3,minmax(0,1fr)); gap:clamp(14px,2vw,22px)}
.pp-film h3{font-size:1.25rem; margin:14px 0 2px; color:#fff}
.pp-film .vid__label{display:none}
.pp-film small{font-family:var(--mono); font-size:.68rem; letter-spacing:.08em; text-transform:uppercase; color:var(--aqua)}
.pp-film__link{position:relative; display:block; aspect-ratio:16/9; border-radius:var(--r-xl); overflow:hidden; box-shadow:0 26px 60px -30px rgba(0,0,0,.6)}
.pp-film__link img{width:100%; height:100%; object-fit:cover; transition:transform .5s}
.pp-film__link:hover img{transform:scale(1.04)}
.pp-film__link span{position:absolute; right:12px; bottom:12px; background:#fff; color:var(--slate); border-radius:999px; padding:6px 12px; font-weight:800; font-size:.82rem}
@media (max-width:860px){.pp-films{grid-template-columns:1fr}}
.pp-disf{display:grid; grid-template-columns:minmax(0,1.2fr) minmax(0,.8fr); gap:0; background:#0e252d; border-radius:var(--r-xl); overflow:hidden; margin-top:clamp(24px,3vw,40px)}
.pp-disf__img{position:relative; min-height:300px}
.pp-disf__img img{position:absolute; inset:0; width:100%; height:100%; object-fit:cover}
.pp-disf__body{padding:clamp(22px,3.4vw,44px)}
.pp-disf__body h3{font-size:clamp(1.8rem,3.4vw,2.8rem); font-stretch:120%; text-transform:uppercase; margin:.1em 0 .4em}
.pp-disf__body p{color:rgba(255,255,255,.86)}
@media (max-width:860px){.pp-disf{grid-template-columns:1fr} .pp-disf__img{min-height:220px}}

.pp-logos{display:grid; grid-template-columns:repeat(4,minmax(0,1fr)); gap:12px}
.pp-logo{background:transparent; border:0; border-radius:14px; height:120px; display:grid; place-items:center; padding:16px 22px}
.pp-logo img{max-height:84px; max-width:100%; width:auto; object-fit:contain}
@media (max-width:760px){.pp-logos{grid-template-columns:repeat(2,minmax(0,1fr))} .pp-logo{height:100px}}
.pp-news{display:grid; grid-template-columns:minmax(0,1.3fr) minmax(0,.7fr); gap:clamp(24px,4vw,56px); align-items:center; background:var(--mist); border:1px solid var(--line); border-radius:var(--r-xl); padding:clamp(24px,3.4vw,40px); margin-top:clamp(36px,4.5vw,60px); scroll-margin-top:120px}
@media (max-width:860px){.pp-news{grid-template-columns:1fr}}
'''


def pp_ep(eid, eyebrow_txt, title, desc, links=()):
    p = pod(eid)
    lk = ''.join(a(esc(t) + (' &#8599;' if u.startswith('http') else ''), u) for t, u in links)
    return f'''<article class="pp-ep">
  <a class="pp-ep__play" href="https://open.spotify.com/episode/{eid}" target="_blank" rel="noopener" data-spotify="episode/{eid}" aria-label="Listen: {esc(title)}">{img('sp-' + eid.lower(), '')}<b>{ICON_PLAY}Listen</b></a>
  <div class="pp-ep__body"><small>{esc(eyebrow_txt)}</small><h3>{esc(title)}</h3><p>{desc}</p>{f'<div class="pp-ep__links">{lk}</div>' if lk else ''}</div>
</article>'''


def partners():
    press = [
        ('the-guardian-logo-vector', 'The Guardian', 'Young people want to know whether they’ve perpetrated a sexual assault.', 'Read in The Guardian', 'https://www.theguardian.com/us-news/2026/may/06/sexual-consent-assault-online-tool'),
        ('vox-logo-svg-1', 'Vox', 'Teen boys are using ChatGPT as their wingman. What could go wrong?', 'Read on Vox', 'https://www.vox.com/technology/481444/ai-chatgpt-teen-boys-teenagers-dating-relationships'),
        ('trendwatching-logo', 'TrendWatching', 'When teens worry they crossed a boundary, Vibe Check helps them.', 'Read on TrendWatching', 'https://www.trendwatching.com/innovations/when-teens-worry-they-may-have-crossed-a-boundary-vibe-check-helps-them-think-it-through'),
        (None, 'The New York Times', 'Our Kids Cannot Learn About Sex Just From Squeamish Gym Teachers', 'Hillary Frank, New York Times Opinion', 'https://www.nytimes.com/2025/01/26/opinion/sex-education-consent-middle-school.html'),
        (None, 'The New York Times', 'The Most Important Lesson in Sex Ed Isn’t Actually Sex', 'New York Times Opinion podcast', 'https://www.nytimes.com/2025/02/27/opinion/sex-education-consent.html'),
    ]
    press_html = ''.join(
        f'<a class="pp-pr" href="{u}" target="_blank" rel="noopener"><span class="pp-chip{"" if im else " pp-chip--text"}">{img(im, outlet) if im else esc(outlet)}</span><span><h3>{esc(h)}</h3><small>{esc(sub)} &#8599;</small></span><span class="go" aria-hidden="true">&#8599;</span></a>'
        for im, outlet, h, sub, u in press)
    strip = ''.join(f'<span class="pp-chip">{img(im, n)}</span>' for im, n in [('the-guardian-logo-vector', 'The Guardian'), ('vox-logo-svg-1', 'Vox'), ('trendwatching-logo', 'TrendWatching')]) + '<span class="pp-chip pp-chip--text">The New York Times</span>'

    eps = ''.join([
        pp_ep('0v2G7MraWG1V2iyXgGKOUF', 'SafeBAE on The Longest Shortest Time', 'Preventing Teens from Joining the Manosphere',
              'SafeBAE returned to The Longest Shortest Time for a conversation with Hillary Frank about Vibe Check, SafeBAE’s free, anonymous reflection tool for young people who are worried they, or a friend, may have crossed a boundary or caused harm. Drew Davis, SafeBAE’s Director of Strategic Initiatives, talks about what happens when teens bring sensitive questions to Reddit, AI tools, or online spaces that can reinforce shame, denial, misogyny, or defensiveness, and how Vibe Check offers a different path toward reflection, accountability, and repair.',
              [('Episode page', 'https://longestshortesttime.com/episode-255-preventing-teens-from-joining-the-manosphere'), ('Vibe Check', 'vibe-check.html')]),
        pp_ep('042UsrG0aMabkTo66WQQWc', 'The She Matters Podcast', 'Centering Youth Voices: Youth-Led Prevention and Addressing Harm',
              'SafeBAE Founding Executive Director Shael Norris on youth-led sexual violence prevention, SafeBAE’s founding story, and what it means to meaningfully center young people in this work, including SafeBAE’s school-based prevention model, Certified Peer Educator Training, and Vibe Check.',
              [('Episode page', 'https://www.shematters.ca/podcasts/the-she-matters-podcast/episodes/2149218219'), ('Peer Educator Training', 'peer-educator.html')]),
        pp_ep('4jjztQt08zjUR9guFgJ56x', 'Shaping the national conversation', 'How to Not (Accidentally) Raise a Rapist',
              'The first episode of the relaunch of Hillary Frank’s parenting and culture podcast reframes one of her most downloaded episodes, <a href="https://longestshortesttime.com/episode-116-how-to-not-accidentally-raise-a-racist/" target="_blank" rel="noopener" style="color:var(--aqua)"><i>How to Not (Accidentally) Raise a Racist</i></a>, to spark dialogue about raising young people who respect boundaries and safety. Featuring Shael Norris, it explores what works when talking to teens about consent and how schools and parents can build a consent-conscious culture.',
              [('NYT Opinion piece', 'https://www.nytimes.com/2025/01/26/opinion/sex-education-consent-middle-school.html'), ('NYT podcast', 'https://www.nytimes.com/2025/02/27/opinion/sex-education-consent.html')]),
        pp_ep('0JfMJbj7ZvISm8m7gp39YS', 'The Measure of Everyday Life', 'Reducing Tolerance for Sexual Assault',
              'With host Dr. Brian Southwell, SafeBAE discussed the findings of our published research paper and announced the launch of CheckYourVibe.org, a free, anonymous reflection tool for young people who are questioning whether they may have caused harm.',
              [('The research', PAPER), ('Our data', 'impact.html')]),
        pp_ep('3ZUV9feb4NeuvydAQWdiao', 'The Totally Preventable Podcast', 'Blurred Lines, Parts 1 & 2',
              'A two-part conversation on the intersection of alcohol, drugs, and sexual assault with experts from RAINN, DanceSafe, Day One, and more. The podcast highlights local voices and prevention leaders working on behavioral health and social issues across Newport County, with insight, resources, and practical ways to support safer, healthier communities.',
              [('Listen to Part 2', 'https://open.spotify.com/episode/2itdYviCeALsZdo6SC64k8'), ('About the podcast', 'https://strategicprevention.org/totally-preventable/')]),
        pp_ep('5PzGRtkgUIBtCjVqhgstq7', 'Hosted by Freya Graf', 'Sexual Violence Prevention in Schools with SafeBAE',
              'A candid conversation about building authentic, youth-driven prevention and meeting young people where they are, and how partnering with students creates systemic change in school environments and fosters cultures of consent.',
              [('360° Schools', '360-schools.html')]),
    ])

    films = [
        ('Share', 'FaiaD8wRNV8', 'share-hbo-1920x1080', 127, 'Partner film'),
        ('Raising Voices (Ni una más)', '3ku4DRWdsBI', 'raising-1920x1080', None, 'Partner film'),
    ]
    film_html = ''.join(f'<div class="pp-film">{yt(v, t, thumb=th, label="Watch", start=s)}<h3>{esc(t)}</h3><small>{esc(k)}</small></div>' for t, v, th, s, k in films)
    film_html += f'<div class="pp-film"><a class="pp-film__link" href="https://www.lionsgate.com/movies/millers-girl" target="_blank" rel="noopener">{img("lionsgate-1920x1080", "Miller’s Girl resources page on Lionsgate, listing SafeBAE among partner organizations")}<span>Lionsgate &#8599;</span></a><h3>Miller’s Girl</h3><small>Partner film</small></div>'

    logos = [('ridoh-logo', 'Rhode Island Department of Health'), ('untitled-design-2023-07-29t212654-858-1920w', 'Illinois Coalition Against Sexual Assault (ICASA)'), ('logo-mahperd', 'MAHPERD'), ('hq720', 'OWL Taking Flight'),
             ('nova-logo', 'NOVA'), ('blue-and-orange-logo-transparent-background', 'SIECUS: Sex Ed for Social Change'), ('sml-logo-tag-long', 'Share My Lesson'), ('vrlc-logo-final-rgb-for-posters-white-on-blue', 'Victim Rights Law Center')]
    logo_html = ''.join(f'<div class="pp-logo">{img(im, n)}</div>' for im, n in logos)

    body = f'''
<section class="pp-hero v2-dark">
  <span class="wm-daisy" aria-hidden="true"></span>
  <div class="wrap">
    <div class="pp-hero__grid">
      <div class="rise">
        <nav class="crumbs" aria-label="Breadcrumb"><a href="index.html">Home</a><span>/</span><a href="about.html">About</a><span>/</span><span>Partners &amp; Press</span></nav>
        <h1>Partners &amp; <span class="mk">press</span></h1>
        <p class="lede">SafeBAE’s work is made possible by the partnerships we’ve built with schools, researchers, funders, creatives, and youth-serving organizations across the country. We’re proud to collaborate with those who share our commitment to ending sexual violence, amplifying youth leadership, and shifting culture through education, art, media, and policy.</p>
        <div class="btns">{btn('Request a program', 'request-a-program.html', 'mint', arrow=True)}{btn('Read our blog', 'blog.html', 'ghost')}</div>
      </div>
      <div class="pp-stack" aria-hidden="true">
        <span class="pp-stack__film">{img('disfluency-1920x1080', '', loading='eager')}</span>
        <span class="pp-stack__c">{img('sp-0v2g7mrawg1v2iyxggkouf', '', loading='eager')}</span>
        <span class="pp-stack__c">{img('sp-042usrg0amabkto66wqqwc', '', loading='eager')}</span>
        <span class="pp-stack__c">{img('sp-0jfmjbj7zvism8m7gp39ys', '', loading='eager')}</span>
        <span class="sticker">On the air</span>
      </div>
    </div>
    <div class="pp-strip"><span>Featured in</span>{strip}</div>
  </div>
</section>

<section class="band band--paper" id="press">
  <div class="wrap">
    <div class="section-head"><div><h2>SafeBAE and Vibe Check in the press</h2></div>{btn('About Vibe Check', 'vibe-check.html', 'slate', arrow=True)}</div>
    <div class="pp-press">{press_html}</div>
  </div>
</section>

<section class="band band--slate" id="podcasts">
  <div class="wrap">
    <div class="section-head"><div><h2>Podcast features</h2></div>{btn('All episodes in the Library', 'library.html#podcasts', 'mint', arrow=True)}</div>
    <div class="pp-eps">{eps}</div>
  </div>
</section>

<section class="band band--mint" id="torrey">
  <div class="wrap pp-torrey">
    <div>
      <p class="eyebrow">Streaming now</p>
      <h2>Torrey DeVitto on <i>Celebrity Name That Tune</i></h2>
      <div class="pp-money"><b>$29,000</b><span>donated to youth-led sexual violence prevention</span></div>
      <p>Longtime SafeBAE partner and Board Member Torrey DeVitto competed on <i>Celebrity Name That Tune</i> (Season 5, Episode 12) on FOX and chose SafeBAE as the beneficiary of her winnings. Torrey donated $29,000 to support youth-led sexual violence prevention, bringing SafeBAE’s mission to a national television audience.</p>
      <p>Her win reflects an ongoing commitment to our work and shows what trusted advocates can do when they use their platforms to invest directly in prevention, care, and youth leadership. We’re deeply grateful to Torrey for continuing to show up for SafeBAE, both publicly and behind the scenes.</p>
      <div class="btns">{btn('Meet our board', 'team.html#board', 'slate', arrow=True)}</div>
    </div>
    {yt('XFQeOEDbN4M', 'Torrey DeVitto on Celebrity Name That Tune', label='FOX')}
  </div>
</section>

<section class="band band--deep" id="films">
  <div class="wrap">
    <div class="section-head"><div><p class="eyebrow">Media collaborations &amp; partner films</p><h2>Stories that center survivors</h2>
      <p class="lede lede--full" style="color:rgba(255,255,255,.86)">SafeBAE believes in the power of media and storytelling to advance prevention and end sexual assault and dating violence. We’re proud to collaborate on films and creative projects that center survivors and shift culture.</p></div></div>
    <div class="pp-films">{film_html}</div>
    <div class="pp-disf">
      <a class="pp-disf__img" href="https://www.disfluencymovie.com/" target="_blank" rel="noopener">{img('disfluency-1920x1080', 'Disfluency, the award-winning feature film, in partnership with SafeBAE')}</a>
      <div class="pp-disf__body">
        <p class="eyebrow">Feature film partner</p>
        <h3>Disfluency</h3>
        <p><i>Disfluency</i> is an award-winning feature film written and directed by {a('Anna Baumgarten', 'https://www.annabaumgarten.com/', 'link')} that offers a survivor-centered portrayal of the aftermath of sexual assault, focusing on trauma, memory, and recovery without depicting the assault itself.</p>
        <p>SafeBAE partnered with the filmmakers to support the film’s educational impact, collaborating on school-based screenings and prevention and discussion resources for secondary and higher-education settings.</p>
        <div class="btns" style="margin-top:18px">{btn('Visit the film’s site', 'https://www.disfluencymovie.com/', 'mint')}</div>
      </div>
    </div>
  </div>
</section>

<section class="band band--paper" id="professionals">
  <div class="wrap">
    <div class="split split--top" style="margin-bottom:clamp(26px,3vw,40px)">
      <div><p class="eyebrow">Training &amp; education for professionals</p><h2>We train the adults around young people, too</h2></div>
      <div>
        <p class="lede" style="margin-bottom:.8em">SafeBAE’s commitment to prevention extends beyond students. We regularly work with educators, legal advocates, service providers, parents, caregivers, and community leaders to share our youth-led model and equip adults to support survivors and embed prevention into everyday practice.</p>
        <p class="muted">Through keynote presentations, workshops, and national webinars, we provide concrete strategies for engaging youth as leaders, building consent-conscious environments, and sustaining systemic change.</p>
        <div class="btns">{btn('Faculty & staff training', 'professional-development.html', 'slate', arrow=True)}{btn('Request a program', 'request-a-program.html', 'ghost')}</div>
      </div>
    </div>
    <p class="eyebrow">Selected collaborators</p>
    <div class="pp-logos">{logo_html}</div>
    <div class="pp-news" id="news">
      <div><p class="eyebrow">News and stories</p><h2>Read stories from survivors and updates from SafeBAE</h2>
        <p class="lede lede--full" style="margin:0">Stay updated with SafeBAE, and share what you learn with your friends.</p>
        <p class="small muted" style="margin-top:12px">Material posted may contain sensitive language. Reader discretion is advised.</p></div>
      <div class="btns" style="justify-content:flex-end">{btn('Read the blog', 'blog.html', 'slate', arrow=True)}{btn('Subscribe on Substack', 'https://substack.com/@safebae', 'ghost')}</div>
    </div>
  </div>
</section>
{give_band()}
'''
    page('partners-press.html', 'Partners & Press · SafeBAE', 'SafeBAE’s partnerships, press coverage, podcast features and partner films highlighting youth-led sexual violence prevention.',
         body, active='about', body_class='pg-partners', head_extra=css(PP_CSS))


# =====================================================================
# #FORDAISY
# =====================================================================
DZ_CSS = '''
.pg-daisy{--dz-ink:#1d414e; --dz-soft:#46646e; --dz-bg:#f6fefe}
.dz-hero{background:var(--dz-bg); color:var(--dz-ink); border-bottom:1px solid var(--line)}
.dz-hero__grid{display:grid; grid-template-columns:minmax(0,1.05fr) minmax(0,.95fr); gap:clamp(28px,5vw,72px); align-items:center; padding-block:clamp(44px,5.5vw,80px)}
.dz-hero .crumbs{color:var(--dz-soft)} .dz-hero .crumbs a{color:var(--logo-teal)}
.dz-mark{display:inline-flex; align-items:center; gap:10px; font-family:var(--mono); font-size:.74rem; letter-spacing:.14em; text-transform:uppercase; color:var(--logo-teal); font-weight:600; margin-bottom:18px}
.dz-mark .daisy{width:30px; height:30px; color:var(--teal)}
.dz-hero h1{font-size:clamp(3rem,7.4vw,7rem); font-weight:500; font-stretch:78%; letter-spacing:-.025em; line-height:.9; margin:0 0 .25em; color:var(--logo-teal)}
.dz-dates{font-family:var(--display); font-stretch:88%; font-weight:600; font-size:clamp(1.15rem,2vw,1.55rem); letter-spacing:.01em; margin:0 0 1.1em; color:var(--dz-ink)}
.dz-dates span{color:var(--teal); padding:0 .35em}
.dz-hero .lede{color:var(--dz-ink); font-weight:450}
.dz-portrait{position:relative; justify-self:center; width:min(100%, 520px); animation:sb-rise-r 1s .1s var(--ease) both}
.dz-portrait__frame{border-radius:999px 999px var(--r-xl) var(--r-xl); overflow:hidden; aspect-ratio:4/5; background:var(--aqua); box-shadow:0 40px 80px -40px rgba(22,53,64,.55)}
.dz-portrait__frame img{width:100%; height:100%; object-fit:cover; object-position:60% 30%}
.dz-portrait > .daisy{position:absolute; width:96px; height:96px; left:-28px; bottom:44px; color:var(--mint); filter:drop-shadow(0 6px 14px rgba(22,53,64,.35))}
@media (max-width:900px){.dz-hero__grid{grid-template-columns:1fr} .dz-portrait{width:min(100%,380px)} .dz-portrait > .daisy{left:-10px; width:70px; height:70px}}

.dz-h2{font-weight:600; font-stretch:84%}
.band--paper .dz-h2,.band--mist .dz-h2,.band--aqua .dz-h2{color:var(--logo-teal)}

.dz-life{display:grid; grid-template-columns:minmax(0,1fr) minmax(0,.9fr); gap:clamp(28px,5vw,72px); align-items:center}
.dz-life p{font-size:1.08rem; line-height:1.7}
.dz-life__pics{display:grid; grid-template-columns:1.1fr .9fr; gap:12px; align-items:end}
.dz-life__pics figure{margin:0}
.dz-life__pics img{width:100%; border-radius:var(--r-xl); object-fit:cover}
.dz-life__pics figure:first-child img{aspect-ratio:3/4}
.dz-life__pics figure:last-child img{aspect-ratio:4/5}
.dz-life__pics figcaption{font-family:var(--mono); font-size:.68rem; letter-spacing:.06em; text-transform:uppercase; color:var(--ink-soft); margin-top:8px}
.dz-teaser{display:grid; grid-template-columns:118px minmax(0,1fr) auto; gap:16px; align-items:center; margin-top:26px; padding:12px 16px 12px 12px; border-radius:var(--r-xl); background:var(--mist); border:1px solid var(--line); text-decoration:none; color:var(--slate); transition:transform .25s var(--ease), box-shadow .25s var(--ease)}
.dz-teaser:hover{transform:translateY(-3px); box-shadow:var(--shadow-soft)}
.dz-teaser img{width:118px; height:100px; object-fit:cover; border-radius:14px}
.dz-teaser small{display:block; font-family:var(--mono); font-size:.66rem; letter-spacing:.1em; text-transform:uppercase; color:var(--logo-teal); font-weight:600}
.dz-teaser b{display:block; font-family:var(--display); font-weight:700; font-stretch:88%; font-size:1.45rem; line-height:1.1; color:var(--logo-teal); margin:2px 0}
.dz-teaser span span{display:block; color:var(--ink-soft); font-size:.92rem; line-height:1.4}
.dz-teaser .go{width:42px; height:42px; border-radius:50%; display:grid; place-items:center; background:var(--aqua); color:var(--logo-teal); font-weight:800}
.dz-teaser:hover .go{background:var(--mint)}
@media (max-width:860px){.dz-life{grid-template-columns:1fr}}
@media (max-width:480px){.dz-teaser{grid-template-columns:84px minmax(0,1fr)} .dz-teaser img{width:84px; height:84px} .dz-teaser .go{display:none}}

.dz-cut{display:grid; grid-template-columns:auto minmax(0,1fr); gap:clamp(16px,3vw,36px); align-items:start; border-top:1px solid var(--line-dark); border-bottom:1px solid var(--line-dark); padding-block:clamp(26px,3.6vw,44px)}
.dz-cut__src{font-family:var(--mono); font-size:.72rem; letter-spacing:.1em; text-transform:uppercase; color:var(--mint); writing-mode:vertical-rl; transform:rotate(180deg); white-space:nowrap}
.dz-cut blockquote{margin:0; font-family:var(--display); font-weight:500; font-stretch:88%; font-size:clamp(1.45rem,3vw,2.5rem); line-height:1.2; color:#fff; text-wrap:pretty}
.dz-cut blockquote b{font-weight:700; color:var(--aqua)}
.dz-cut a{display:inline-block; margin-top:16px; color:var(--mint); font-weight:700}
@media (max-width:640px){.dz-cut{grid-template-columns:1fr} .dz-cut__src{writing-mode:horizontal-tb; transform:none}}

.dz-wallband{position:relative; overflow:hidden}
.dz-wallband::before{content:""; position:absolute; inset:0; background:radial-gradient(60% 40% at 20% 0%, rgba(21,255,200,.10), transparent 70%), radial-gradient(50% 40% at 90% 30%, rgba(209,254,255,.07), transparent 70%); pointer-events:none}
.dz-wallband > .wrap{position:relative}
.dz-wallhead{display:grid; grid-template-columns:minmax(0,1fr) minmax(0,1fr); gap:clamp(24px,4vw,56px); align-items:end; margin-bottom:clamp(28px,3vw,40px)}
.dz-wallhead h2{font-weight:600; font-stretch:82%; font-size:clamp(2.2rem,4.6vw,3.8rem); color:#fff; line-height:.95}
.dz-wallhead p{margin:0 0 .8em; color:rgba(255,255,255,.84)}
.dz-count{display:flex; align-items:baseline; gap:12px; margin-top:6px}
.dz-count b{font-family:var(--display); font-weight:600; font-stretch:80%; font-size:clamp(3.4rem,6vw,5rem); line-height:.9; color:var(--mint)}
.dz-count span{font-weight:600; color:#fff; line-height:1.3}
@media (max-width:860px){.dz-wallhead{grid-template-columns:1fr}}
.dz-wall{columns:4 250px; column-gap:14px}
.dz-card{break-inside:avoid; margin:0 0 14px; background:#fff; border-radius:14px; padding:18px 18px 16px; position:relative; box-shadow:0 0 0 1px rgba(209,254,255,.06), 0 18px 40px -28px rgba(0,0,0,.9); transition:box-shadow .45s var(--ease), transform .45s var(--ease)}
.dz-card:hover{transform:translateY(-2px); box-shadow:0 0 0 1px rgba(21,255,200,.4), 0 0 34px -6px rgba(21,255,200,.4)}
.dz-card:nth-child(5n+2){background:var(--aqua)}
.dz-card:nth-child(7n+4){background:#eefcfc}
.dz-card .daisy{width:20px; height:20px; color:var(--teal); opacity:.8; display:block; margin-bottom:10px}
.dz-card p{margin:0; font-size:.95rem; line-height:1.6; color:var(--dz-ink); white-space:pre-line; overflow-wrap:anywhere}
.dz-card.is-long p{max-height:9.6em; overflow:hidden; -webkit-mask-image:linear-gradient(#000 60%, transparent); mask-image:linear-gradient(#000 60%, transparent)}
.dz-card.is-long.open p{max-height:none; -webkit-mask-image:none; mask-image:none}
.dz-card button{margin-top:8px; background:none; border:0; padding:4px 0; font:inherit; font-size:.82rem; font-weight:700; color:var(--logo-teal); cursor:pointer; text-decoration:underline; text-decoration-color:var(--teal); text-decoration-thickness:2px; text-underline-offset:3px}
.dz-card.is-new{animation:dzIn .7s ease both}
@keyframes dzIn{from{opacity:0; transform:translateY(10px)}}
.dz-wall__foot{display:flex; flex-wrap:wrap; gap:12px 20px; align-items:center; justify-content:center; margin-top:clamp(18px,2.4vw,28px)}
.dz-wall__foot span{font-family:var(--mono); font-size:.74rem; letter-spacing:.06em; text-transform:uppercase; color:var(--aqua)}

.dz-add{display:grid; grid-template-columns:minmax(0,.9fr) minmax(0,1.1fr); gap:clamp(24px,4vw,56px); align-items:center; background:#fff; border-radius:var(--r-xl); padding:clamp(22px,3.6vw,44px); border:1px solid var(--line); box-shadow:var(--shadow-soft)}
#add{scroll-margin-top:110px}
.dz-add h2{font-weight:600; font-stretch:82%; color:var(--logo-teal); font-size:clamp(2rem,3.6vw,3rem)}
.dz-add .form__done{background:var(--aqua); display:none; align-items:center; gap:12px}
.dz-add .form.sent .form__done{display:flex}
.dz-add .form__done .daisy{width:34px; height:34px; color:var(--teal); animation:dzBloom 1.2s var(--ease) both}
@keyframes dzBloom{from{transform:scale(.2) rotate(-120deg); opacity:0}}
.dz-add textarea{min-height:170px}
@media (max-width:860px){.dz-add{grid-template-columns:1fr}}

.dz-letter{background:#fff; color:var(--dz-ink); border-radius:var(--r-xl); max-width:880px; margin:0 auto; border:1px solid var(--line); box-shadow:var(--shadow-soft); overflow:hidden}
.dz-letter summary{list-style:none; cursor:pointer; padding:clamp(20px,3vw,32px) clamp(22px,3.6vw,44px); display:flex; justify-content:space-between; align-items:center; gap:18px}
.dz-letter summary::-webkit-details-marker{display:none}
.dz-letter summary b{font-family:var(--display); font-weight:600; font-stretch:86%; font-size:clamp(1.3rem,2.4vw,1.8rem); line-height:1.15; color:var(--logo-teal)}
.dz-letter summary i{font-style:normal; flex:none; width:42px; height:42px; border-radius:50%; background:var(--aqua); display:grid; place-items:center; font-size:1.3rem; color:var(--slate); transition:transform .3s}
.dz-letter[open] summary i{transform:rotate(45deg); background:var(--mint)}
.dz-letter__body{padding:0 clamp(22px,3.6vw,44px) clamp(26px,3.6vw,44px); border-top:1px solid var(--line)}
.dz-letter__head{text-align:center; padding:26px 0 18px}
.dz-letter__head h3{font-family:var(--display); font-weight:600; font-stretch:80%; font-size:clamp(2rem,4vw,3rem); letter-spacing:.06em; margin:0; color:var(--slate)}
.dz-letter__head p{font-family:var(--mono); font-size:.78rem; letter-spacing:.12em; text-transform:uppercase; color:var(--logo-teal); margin:6px 0 0}
.dz-letter__body p{font-size:1.04rem; line-height:1.75}
.dz-sign{font-family:var(--display); font-stretch:86%; font-weight:600; font-size:1.2rem}
.dz-care{display:flex; flex-wrap:wrap; gap:12px 22px; align-items:center; justify-content:space-between; max-width:880px; margin:18px auto 0; padding:16px 20px; border-radius:14px; background:var(--mist); border:1px solid var(--line); color:var(--slate)}
.dz-care p{margin:0; font-size:.95rem}
.dz-care b{color:var(--logo-teal)}
.dz-care button{font:inherit; font-weight:800; background:var(--slate); color:#fff; border:0; border-radius:10px; padding:9px 14px; cursor:pointer}
.dz-care button:hover{background:var(--logo-teal)}

.dz-vids{display:grid; grid-template-columns:repeat(3,minmax(0,1fr)); gap:clamp(14px,2vw,22px)}
.dz-vids > div > h3{font-weight:600; font-stretch:88%; font-size:1.25rem; margin:14px 0 2px; color:var(--logo-teal)}
.dz-vids > div > small{font-family:var(--mono); font-size:.7rem; letter-spacing:.08em; text-transform:uppercase; color:var(--ink-soft)}
@media (max-width:860px){.dz-vids{grid-template-columns:1fr}}

.dz-gal.gallery{display:block; columns:5 180px; column-gap:12px}
.dz-gal.gallery button{display:block; width:100%; aspect-ratio:auto; margin:0 0 12px; break-inside:avoid; border-radius:12px; background:rgba(255,255,255,.06)}
.dz-gal.gallery button img{height:auto}
@media (max-width:520px){.dz-gal.gallery{columns:2; column-gap:10px} .dz-gal.gallery button{margin-bottom:10px}}

.dz-voice{display:grid; grid-template-columns:minmax(0,1fr) minmax(0,1fr); gap:clamp(24px,4vw,56px); align-items:center}
.dz-voice .audio{background:var(--logo-teal) var(--grain); border-radius:var(--r-xl)}
.dz-voice .audio + .audio{margin-top:12px}
@media (max-width:860px){.dz-voice{grid-template-columns:1fr}}
.dz-train{display:grid; grid-template-columns:auto minmax(0,1fr) auto; gap:clamp(18px,3vw,36px); align-items:center}
.dz-train > .daisy{width:clamp(64px,8vw,96px); height:clamp(64px,8vw,96px); color:var(--mint)}
.dz-train h2{font-weight:600; font-stretch:84%; margin-bottom:.2em}
@media (max-width:760px){.dz-train{grid-template-columns:1fr}}
'''

DZ_JS = r'''<script>(function(){
  var wall = document.getElementById('dz-wall'), more = document.getElementById('dz-more'), shown = document.getElementById('dz-shown'), data = [];
  try { data = JSON.parse(document.getElementById('dz-data').textContent); } catch(e) { data = []; }
  var narrow = window.matchMedia && window.matchMedia('(max-width: 640px)').matches;
  var STEP = narrow ? 12 : 30, n = wall ? wall.children.length : 0, LONG = 300;
  if(wall && narrow && n > 12){ while(wall.children.length > 12) wall.removeChild(wall.lastElementChild); n = 12; }
  function wire(card){ var b = card.querySelector('button'); if(!b) return; b.addEventListener('click', function(){ var o = card.classList.toggle('open'); b.textContent = o ? 'Show less' : 'Read the full message'; b.setAttribute('aria-expanded', String(o)); }); }
  if(wall) Array.prototype.forEach.call(wall.children, wire);
  function card(t){
    var f = document.createElement('figure'); f.className = 'dz-card is-new' + (t.length > LONG ? ' is-long' : '');
    var d = document.createElement('span'); d.className = 'daisy'; d.setAttribute('aria-hidden','true'); f.appendChild(d);
    var p = document.createElement('p'); p.textContent = t; f.appendChild(p);
    if(t.length > LONG){ var b = document.createElement('button'); b.type = 'button'; b.textContent = 'Read the full message'; b.setAttribute('aria-expanded','false'); f.appendChild(b); }
    wire(f); return f;
  }
  function update(){ if(shown) shown.textContent = 'Showing ' + n + ' of ' + data.length + ' messages'; if(more && n >= data.length) more.hidden = true; }
  if(more) more.addEventListener('click', function(){ var frag = document.createDocumentFragment(), end = Math.min(n + STEP, data.length); for(var i = n; i < end; i++) frag.appendChild(card(data[i])); wall.appendChild(frag); n = end; update(); });
  update();
})();</script>'''

GALLERY_ALT = {
    1: 'Daisy smiling beside a tall window', 2: 'Daisy seated in an auditorium before a talk', 3: 'Daisy with SafeBAE team members in front of a student audience',
    4: 'Daisy smiling at a school event', 5: 'Daisy standing in a school gym during an event', 6: 'Daisy smiling and making a peace sign',
    7: 'Daisy with a group outdoors at dusk', 9: 'Daisy sitting outside against a white wall', 10: 'Daisy at a table with a cake',
    11: 'Daisy in a lecture hall', 12: 'Daisy with two others in a lecture hall', 13: 'Daisy on a bridge on a sunny day',
    14: 'Daisy laughing on a bridge on a sunny day', 15: 'Daisy in a rowboat on a lake', 16: 'Daisy smiling in a blue winter coat',
    17: 'Daisy smiling in a close-up photo with another person', 18: 'Daisy standing against a plain wall', 19: 'Daisy in a selfie under pink light',
    20: 'Daisy leaning against a tree beside a stone wall', 21: 'Daisy with two people, one wearing a SafeBAE shirt', 22: 'Daisy on set during a film shoot',
    23: 'Daisy leaning in a window frame', 24: 'Daisy with a large group of young advocates at an event', 25: 'Daisy at a tattoo studio',
    26: 'Daisy posing with a woman in a white top', 27: 'Daisy outside a comedy club at night', 28: 'Daisy tattooing a client',
    29: 'Daisy standing in a plaza lined with flags', 30: 'A selfie of Daisy and two others in a plaza lined with flags', 31: 'Daisy and two others in front of a Zero Tolerance for Sexual Exploitation and Abuse backdrop',
    32: 'Daisy with a woman in a formal hall',
}


def fordaisy():
    tributes = json.load(open('/home/claude/crawl/tributes.json'))
    tributes = [t.strip() for t in tributes if t and t.strip()]
    first = 30
    LONG = 300

    def card(t):
        long_ = len(t) > LONG
        return (f'<figure class="dz-card{" is-long" if long_ else ""}">{daisy()}<p>{esc(t)}</p>'
                + ('<button type="button" aria-expanded="false">Read the full message</button>' if long_ else '') + '</figure>')
    wall = ''.join(card(t) for t in tributes[:first])
    data_json = json.dumps(tributes, ensure_ascii=False).replace('</', '<\\/')

    gal_ids = [i for i in range(1, 33) if i != 8]
    gallery = ''.join(f'<button type="button" data-src="assets/img/fordaisy{i}.webp" data-cap="{esc(GALLERY_ALT.get(i, "Daisy Coleman"))}" aria-label="Open photo: {esc(GALLERY_ALT.get(i, "Daisy Coleman"))}">{img("fordaisy" + str(i), GALLERY_ALT.get(i, "Daisy Coleman"))}</button>' for i in gal_ids)

    vids = [('UcEcU6i6UdY', 'In Memory of Daisy Coleman', 'daisy4', 'Remembrance'),
            ('U1Lt7fK1UWk', 'Daisy’s Virtual Memorial Service', 'yt-u1lt7fk1uwk', 'August 18, 2020'),
            ('O-FPZphiDSc', 'Photos for Remembrance', 'yt-o-fpzphidsc', 'Picture collection, 2020')]
    vid_html = ''.join(f'<div>{yt(v, t, thumb=th, label="Watch")}<h3>{esc(t)}</h3><small>{esc(s)}</small></div>' for v, t, th, s in vids)

    gwf = pod('4A7XFCTULig0ZyOKaW3A9o')
    ngz = pod('3sIH5lMCEkeU0e298AsQe0')

    body = f'''
<section class="dz-hero v2-light">
  <span class="wm-daisy" aria-hidden="true"></span>
  <div class="wrap dz-hero__grid">
    <div class="rise">
      <nav class="crumbs" aria-label="Breadcrumb"><a href="index.html">Home</a><span>/</span><span>#ForDaisy</span></nav>
      <p class="dz-mark">{daisy()}In memoriam</p>
      <h1>#For<span class="mk">Daisy</span></h1>
      <p class="dz-dates">Daisy Coleman<span>&middot;</span>March 30, 1997 – August 4, 2020</p>
      <p class="lede">This August marks six years since the passing of Daisy Coleman, SafeBAE’s co-founder. As a teenage survivor, Daisy shared her story in the documentary <i>Audrie &amp; Daisy</i>, speaking openly about what had happened to her and bringing the realities facing young survivors to a national audience. Her vision became the foundation of SafeBAE and helped ignite our youth-led movement.</p>
      <div class="btns">{btn('Read the tribute wall', '#wall', 'slate')}{btn('Add your message', '#add', 'ghost')}</div>
    </div>
    <div class="dz-portrait"><div class="dz-portrait__frame">{img('fordaisy16', 'Daisy Coleman smiling in a blue winter coat', loading='eager')}</div>{daisy()}</div>
  </div>
</section>

<section class="band band--slate band--tight">
  <div class="wrap">
    <div class="dz-cut">
      <span class="dz-cut__src">The Cut</span>
      <div>
        <blockquote><b>“All the organizing that happened after Daisy spoke out may not necessarily be a direct result but is certainly a ripple effect:</b> the new campus anti-rape movement, followed by the backlash over Brock Turner, followed by the sudden ubiquity of MeToo as both a hashtag and a rallying cry.”</blockquote>
        {a('Read “What Daisy Coleman Changed” in The Cut &#8599;', 'https://www.thecut.com/2020/12/what-daisy-coleman-changed.html')}
      </div>
    </div>
  </div>
</section>

<section class="band band--paper" id="daisy">
  <div class="wrap dz-life">
    <div>
      <h2 class="dz-h2">Daisy was more than her advocacy.</h2>
      <p>She was a tattoo artist whose work people still carry with them, and she was loved deeply by her family and friends.</p>
      <p>Her example still guides how we show up for students, and her story is carried forward by us and by communities across the country.</p>
      <a class="dz-teaser" href="fordaisy-tattoos.html">{img('fordaisy25', '')}<span><small>#ForDaisy</small><b>Tattoos &amp; Healing</b><span>Daisy’s art, and tattoos as one path some survivors take to reclaim their bodies.</span></span><span class="go" aria-hidden="true">&rarr;</span></a>
    </div>
    <div class="dz-life__pics">
      <figure>{img('fordaisy28', 'Daisy Coleman tattooing a client')}<figcaption>Daisy at work as a tattoo artist</figcaption></figure>
      <figure>{img('fordaisy21', 'Daisy Coleman with two people, one wearing a SafeBAE shirt')}</figure>
    </div>
  </div>
</section>

<section class="band band--deep dz-wallband" id="wall">
  <div class="wrap">
    <div class="dz-wallhead">
      <div>
        <p class="eyebrow">#ForDaisy Memorial Tribute Wall</p>
        <h2>Daisy reached people she never met.</h2>
        <div class="dz-count"><b>700+</b><span>tribute messages collected at her memorial service</span></div>
      </div>
      <div>
        <p>Survivors who saw themselves in her story, students who felt less alone because she spoke first, parents and educators who changed how they show up for young people because of her. When she passed, we collected tribute messages at her memorial service, more than 700 of them, and we have held them close ever since.</p>
        <p>Her reach hasn’t stopped. Every year, hundreds of people still find their way to SafeBAE through Daisy’s story and tell us she is the reason they came to this work. Six years later, she is still bringing people in. This year we brought those messages together in one place.</p>
      </div>
    </div>
    <div class="dz-wall" id="dz-wall">{wall}</div>
    <div class="dz-wall__foot"><span id="dz-shown">Showing {first} of {len(tributes)} messages</span><button class="btn btn--mint" type="button" id="dz-more">Show more messages</button>{btn('Add your message', '#add', 'ghost')}</div>
    <script type="application/json" id="dz-data">{data_json}</script>
  </div>
</section>

<section class="band band--aqua" id="add">
  <div class="wrap">
    <div class="dz-add">
      <div>
        <h2>If Daisy touched your life</h2>
        <p>If you knew her, or knew her only through her work, we invite you to add your own message for Daisy.</p>
      </div>
      <form class="form" data-static data-mailto="info@safebae.org" data-subject="#ForDaisy tribute message">
        <div class="field"><label for="dz-msg">Your message</label><textarea id="dz-msg" name="Message for Daisy" placeholder="Write your message for Daisy…" required></textarea></div>
        <div><button class="btn btn--slate" type="submit">Send message</button></div>
        <p class="form__done" role="status">{daisy()}<span>Thank you for sharing your message for Daisy.</span></p>
      </form>
    </div>
  </div>
</section>

<section class="band band--paper" id="remembering">
  <div class="wrap">
    <div class="section-head"><div><p class="eyebrow">Remembering Daisy</p><h2 class="dz-h2">The words and images from those days</h2>
      <p class="lede lede--full">Here is the statement we shared with our community on the day Daisy passed, with the recordings and photos from those days, including her virtual memorial service. Together they hold both the grief and the celebration of her life. We’ve kept everything here for anyone who wants to return to it, including people who are only now finding Daisy’s story.</p></div></div>
    <details class="dz-letter">
      <summary><b>Read the statement we shared after Daisy’s passing</b><i aria-hidden="true">+</i></summary>
      <div class="dz-letter__body">
        <div class="dz-letter__head"><h3>DAISY COLEMAN</h3><p>March 30th, 1997 – August 4th, 2020</p></div>
        <p>Through our shock and sadness, we are releasing a statement about our loss of Daisy. As all of our supporters know, Daisy has fought for many years to both heal from her assault and prevent future sexual violence among teens. She was our sister in this work and much of the driving force behind it. We were not just a non-profit team, but a family. We are shattered and shocked by her passing from suicide. She had been in EMDR therapy for 2 years, working on her triggers and healing from the many traumas in her life. She had many coping demons and had been facing and overcoming them all, but as many of you know, healing is not a straight path or any easy one. She fought longer and harder than we will ever know. But we want to be mindful of all the young survivors who looked up to her. Please know that above ALL ELSE, she did this work for you. She loved talking to young people about changing the culture and taking care of one another. Much of her healing came from each of you. She was so proud of the work we’ve done and loved seeing so many fierce young activists push for change in their schools and among their friends.</p>
        <p>She would want young survivors to know they are heard, they matter, they are loved, and there are places for them to get the help they need. And she would want everyone else – peer allies, educators, parents, legislators, religious leaders – to come together to help stop sexual violence and help save teen lives.</p>
        <p>As advocates we know survivors of sexual assault are 10 times more likely to attempt suicide than those who haven’t experienced sexual assault, and that is why we will keep dedicating ourselves to this work in her legacy. There’s no question that she would want that.</p>
        <p class="dz-sign">All of our love,<br>SafeBAE</p>
      </div>
    </details>
    <div class="dz-care"><p>If you are struggling, you are heard and you matter. <b>Call or text 988</b> any time, or text HOME to 741741.</p><button type="button" data-open-help>See all free, confidential support</button></div>
    <div class="dz-vids" style="margin-top:clamp(32px,4vw,52px)">{vid_html}</div>
  </div>
</section>

<section class="band band--slate" id="photos">
  <div class="wrap">
    <div class="section-head"><div><p class="eyebrow">Photos for remembrance</p><h2 class="dz-h2">Daisy, in the pictures people gathered in her honor</h2></div></div>
    <div class="gallery dz-gal" data-gallery>{gallery}</div>
  </div>
</section>

<section class="band band--paper">
  <div class="wrap dz-voice">
    <div>
      <p class="eyebrow">Podcasts</p>
      <h2 class="dz-h2">Daisy’s voice, and her legacy</h2>
      <p>{esc(gwf[4])}</p>
      <p class="muted">{esc(ngz[4])}</p>
    </div>
    <div>{spotify(gwf[0], gwf[1], gwf[2])}{spotify(ngz[0], ngz[1], ngz[2])}</div>
  </div>
</section>

<section class="band band--logo band--tight">
  <div class="wrap dz-train">
    {daisy()}
    <div><p class="eyebrow">For Daisy: Before Anyone Else</p><h2>Certified Peer Educator Training</h2>
      <p style="margin:0;color:rgba(255,255,255,.86)">The training is offered in memory of our co-founder, Daisy Coleman, whose vision and leadership continue to inspire SafeBAE’s mission and young people nationwide.</p></div>
    <div class="btns">{btn('Become a Peer Educator', 'peer-educator.html', 'mint', arrow=True)}</div>
  </div>
</section>
{give_band()}
'''
    page('fordaisy.html', '#ForDaisy · Remembering Daisy Coleman · SafeBAE', 'Remembering SafeBAE co-founder Daisy Coleman (1997–2020): the #ForDaisy tribute wall, her memorial service, and photos gathered in her honor.',
         body, active='fordaisy', body_class='pg-daisy', head_extra=css(DZ_CSS), scripts=DZ_JS)


# =====================================================================
# #FORDAISY: TATTOOS & HEALING
# =====================================================================
TT_SOURCES = [
    ('maxwell', 'Maxwell, D., Leat, S. R., Thomas, J., Thomas, S. A., &amp; Coad, S. (2023). The tattoo environment as a therapeutic healing space for sexual assault survivors. <i>Deviant Behavior</i>.', 'https://doi.org/10.1080/01639625.2023.2250052', 'doi:10.1080/01639625.2023.2250052'),
    ('branco', 'Branco, P. (2017, April 3). Reclaiming the body after trauma: Can body art help abuse survivors heal? VAWnet, National Resource Center on Domestic Violence.', 'https://vawnet.org/news/reclaiming-body-after-trauma-can-body-art-help-abuse-survivors-heal', 'vawnet.org'),
    ('fletcher', 'Fletcher, A. A. (2026, March 2). Reclaiming the body after trauma. <i>Psychology Today</i>.', 'https://www.psychologytoday.com/us/blog/keeping-it-real-and-resilient/202603/reclaiming-the-body-after-trauma', 'psychologytoday.com'),
    ('weisenberger', 'Weisenberger, C. (2025, May 20). How to: Trauma-informed tattooing. Kingpin Tattoo Supply.', 'https://www.kingpintattoosupply.com/blogs/stories-and-articles/how-to-trauma-informed-tattooing', 'kingpintattoosupply.com'),
    ('npr', 'Nungesser, J. (2025, April 29). Ohio tattoo shop helps trauma and abuse survivors transform scars into art. Ideastream Public Media for NPR.', 'https://www.npr.org/2025/04/29/nx-s1-5342586/ohio-tattoo-shop-helps-trauma-and-abuse-survivors-transform-scars-into-art', 'npr.org'),
    ('olr', 'Connecticut Office of Legislative Research. (2013). Report 2013-R-0231 on state laws restricting tattooing of minors, citing the National Conference of State Legislatures.', 'https://www.cga.ct.gov/2013/rpt/2013-R-0231.htm', 'cga.ct.gov'),
]
TT_N = {k: i + 1 for i, (k, *_r) in enumerate(TT_SOURCES)}


def cite(*keys):
    return ''.join(f'<sup class="tt-cite"><a href="#src-{k}" aria-label="Source {TT_N[k]}">{TT_N[k]}</a></sup>' for k in keys)


# simple hand-drawn line motifs (brand colours, drawn for this page)
TT_ICONS = {
    'daisy': '<svg viewBox="0 0 64 64" aria-hidden="true"><g fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="32" cy="32" r="6.5"/><path d="M32 25.5c-3-7-3-14 0-19 3 5 3 12 0 19M32 38.5c3 7 3 14 0 19-3-5-3-12 0-19M25.5 32c-7 3-14 3-19 0 5-3 12-3 19 0M38.5 32c7-3 14-3 19 0-5 3-12 3-19 0M27.4 27.4c-6.6-3.7-10.4-9-10.6-14.6 5.6.2 10.9 4 14.6 10.6M36.6 36.6c6.6 3.7 10.4 9 10.6 14.6-5.6-.2-10.9-4-14.6-10.6M27.4 36.6c-3.7 6.6-9 10.4-14.6 10.6.2-5.6 4-10.9 10.6-14.6M36.6 27.4c3.7-6.6 9-10.4 14.6-10.6-.2 5.6-4 10.9-10.6 14.6"/></g></svg>',
    'heart': '<svg viewBox="0 0 64 64" aria-hidden="true"><g fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M32 54C18 44 8 35 8 23.5 8 15.5 14 10 21 10c5 0 8.6 2.8 11 6.6C34.4 12.8 38 10 43 10c7 0 13 5.5 13 13.5C56 35 46 44 32 54z"/><path d="M20 22c1-3 3-5 6-5.5"/></g></svg>',
    'sun': '<svg viewBox="0 0 64 64" aria-hidden="true"><g fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M8 46h48M14 54h36"/><path d="M18 46a14 14 0 0 1 28 0"/><path d="M32 18v8M17 25l5 5M47 25l-5 5M10 38h6M48 38h6"/></g></svg>',
    'vine': '<svg viewBox="0 0 64 64" aria-hidden="true"><g fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M10 44c10-2 14-10 22-12s14 6 22 2" stroke-dasharray="2 5"/><path d="M8 50c8-10 16-14 24-14s14 6 24-2"/><path d="M20 41c-1-6 3-10 8-10-1 6-4 9-8 10zM38 38c5-3 10-1 12 4-6 1-9-1-12-4z"/></g></svg>',
    'spark': '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M12 1c.8 6.4 3.6 9.2 10 10-6.4.8-9.2 3.6-10 10-.8-6.4-3.6-9.2-10-10 6.4-.8 9.2-3.6 10-10z" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linejoin="round"/></svg>',
}

TT_CSS = '''
.pg-daisy{--dz-ink:#1d414e; --dz-soft:#46646e; --dz-bg:#f6fefe}
.tt-hero{background:var(--dz-bg); color:var(--dz-ink); border-bottom:1px solid var(--line)}
.tt-hero__grid{display:grid; grid-template-columns:minmax(0,1.05fr) minmax(0,.95fr); gap:clamp(28px,5vw,72px); align-items:center; padding-block:clamp(44px,5.5vw,80px)}
.tt-hero .crumbs{color:var(--dz-soft)} .tt-hero .crumbs a{color:var(--logo-teal)}
.tt-hero h1{font-size:clamp(2.8rem,6.6vw,6.2rem); font-weight:500; font-stretch:78%; letter-spacing:-.025em; line-height:.92; margin:0 0 .35em; color:var(--logo-teal)}
.tt-hero .lede{color:var(--dz-ink); font-weight:450}
.tt-comp{position:relative; justify-self:center; width:min(100%,520px); padding:0 12% 10% 0; animation:sb-rise-r 1s .1s var(--ease) both}
.tt-comp__main{border-radius:999px 999px var(--r-xl) var(--r-xl); overflow:hidden; aspect-ratio:4/5; box-shadow:0 40px 80px -40px rgba(22,53,64,.55)}
.tt-comp__main img{width:100%; height:100%; object-fit:cover}
.tt-comp__sub{position:absolute; right:0; bottom:0; width:46%; border-radius:16px; overflow:hidden; border:6px solid var(--dz-bg); box-shadow:var(--shadow-soft); transform:rotate(3deg)}
.tt-comp__sub img{width:100%; aspect-ratio:3/4; object-fit:cover}
.tt-comp .sticker{position:absolute; left:-12px; top:16%}
.tt-doodle{position:absolute; color:var(--teal); pointer-events:none}
.tt-doodle svg{width:100%; height:100%; display:block}
.tt-doodle--a{width:74px; height:74px; left:-40px; bottom:22%; color:var(--teal)}
.tt-doodle--b{width:28px; height:28px; right:8%; top:-6px; color:var(--teal)}
.tt-doodle--c{width:18px; height:18px; right:2%; top:28px; color:var(--mint)}
@media (max-width:900px){.tt-hero__grid{grid-template-columns:1fr} .tt-comp{width:min(100%,420px)} .tt-doodle--a{left:-8px; width:54px; height:54px}}

.tt-cite{font-size:.7em; line-height:0; margin-left:1px}
.tt-cite a{text-decoration:none; font-weight:700; color:inherit; padding:0 2px; border-radius:4px; background:rgba(21,255,200,.25)}
.band--paper .tt-cite a,.band--mist .tt-cite a,.band--aqua .tt-cite a{color:var(--logo-teal); background:var(--aqua)}
.band--aqua .tt-cite a{background:#fff}

.tt-carried{columns:3 280px; column-gap:16px}
.tt-q{break-inside:avoid; margin:0 0 16px; padding:20px 20px 18px; border-radius:16px; border:1.5px dashed rgba(209,254,255,.32); background:rgba(255,255,255,.04); position:relative}
.tt-q .chip{background:transparent; color:var(--mint); border:1.5px solid rgba(21,255,200,.5); margin-bottom:12px}
.tt-q p{margin:0; font-family:var(--display); font-weight:500; font-stretch:90%; font-size:clamp(1.12rem,1.6vw,1.32rem); line-height:1.35; color:#fff}
.tt-q svg{position:absolute; right:14px; top:14px; width:26px; height:26px; color:var(--mint); opacity:.55}
.tt-q--lead{background:rgba(21,255,200,.08); border-style:solid; border-color:rgba(21,255,200,.35)}
.tt-q--lead p{font-size:clamp(1.3rem,2vw,1.6rem)}
.tt-from{display:flex; flex-wrap:wrap; gap:10px 20px; align-items:center; justify-content:space-between; margin-top:clamp(14px,2vw,24px); padding-top:18px; border-top:1px solid var(--line-dark); font-size:.92rem; color:rgba(255,255,255,.78)}
.tt-from a{color:var(--mint); font-weight:700}

.tt-flash{display:grid; grid-template-columns:repeat(2,minmax(0,1fr)); gap:clamp(14px,2vw,22px)}
.tt-f{position:relative; display:grid; grid-template-columns:78px minmax(0,1fr); gap:18px; align-items:start; padding:clamp(20px,2.4vw,28px); border-radius:var(--r-xl); border:1.5px dashed rgba(29,90,102,.35); background:#fff}
.tt-f__icon{width:78px; height:78px; border-radius:50%; background:var(--aqua); color:var(--logo-teal); display:grid; place-items:center}
.tt-f__icon svg{width:52px; height:52px}
.tt-f h3{font-size:1.3rem; margin:2px 0 .4em}
.tt-f p{margin:0 0 .6em; color:var(--ink-soft); font-size:.98rem}
.tt-f p:last-child{margin:0}
@media (max-width:860px){.tt-flash{grid-template-columns:1fr}}
@media (max-width:480px){.tt-f{grid-template-columns:1fr} .tt-f__icon{width:64px; height:64px}}

.tt-path{display:grid; grid-template-columns:minmax(0,1fr) minmax(0,1fr) minmax(0,1fr); gap:clamp(14px,2vw,22px)}
.tt-path > div{background:#fff; border-radius:var(--r-xl); padding:clamp(20px,2.4vw,26px); border:1px solid var(--line)}
.tt-path h3{font-size:1.2rem; margin:0 0 .4em}
.tt-path p{margin:0; font-size:.97rem}
.tt-quote{margin:0 0 clamp(24px,3vw,36px); font-family:var(--display); font-weight:500; font-stretch:86%; font-size:clamp(1.6rem,3.4vw,2.8rem); line-height:1.12; color:var(--logo-teal)}
.tt-quote cite{display:block; margin-top:10px; font-style:normal; font-family:var(--mono); font-size:.72rem; letter-spacing:.08em; text-transform:uppercase; color:var(--dz-soft)}
.tt-minor{display:flex; gap:14px; align-items:flex-start; margin-top:clamp(16px,2vw,22px); padding:16px 20px; border-radius:16px; background:var(--slate); color:#fff}
.tt-minor b{color:var(--mint); white-space:nowrap; font-family:var(--display); font-stretch:106%}
.tt-minor p{margin:0; font-size:.96rem}
@media (max-width:860px){.tt-path{grid-template-columns:1fr} .tt-minor{flex-direction:column; gap:4px}}

.tt-check{background:#fff; border:1px solid var(--line); border-radius:var(--r-xl); box-shadow:var(--shadow-soft); overflow:hidden}
.tt-check__head{display:flex; flex-wrap:wrap; gap:12px 20px; align-items:center; justify-content:space-between; padding:18px clamp(18px,2.6vw,28px); background:var(--mist); border-bottom:1px solid var(--line)}
.tt-check__head b{font-family:var(--display); font-stretch:106%; font-size:1.1rem}
.tt-check__head span{font-family:var(--mono); font-size:.72rem; letter-spacing:.08em; text-transform:uppercase; color:var(--logo-teal); font-weight:600}
.tt-check ol{list-style:none; margin:0; padding:0; counter-reset:tt}
.tt-check li{margin:0; border-bottom:1px solid var(--line)}
.tt-check li:last-child{border-bottom:0}
.tt-check label{display:grid; grid-template-columns:30px minmax(0,1fr); gap:14px; padding:18px clamp(18px,2.6vw,28px); cursor:pointer; transition:background .2s}
.tt-check label:hover{background:#fbffff}
.tt-check input{appearance:none; -webkit-appearance:none; width:28px; height:28px; margin:2px 0 0; border-radius:8px; border:2px solid var(--logo-teal); display:grid; place-items:center; cursor:pointer; background:#fff; transition:background .2s}
.tt-check input::after{content:""; width:12px; height:7px; border-left:3px solid var(--slate); border-bottom:3px solid var(--slate); transform:rotate(-45deg) translate(1px,-1px) scale(0); transition:transform .2s var(--ease)}
.tt-check input:checked{background:var(--mint); border-color:var(--mint)}
.tt-check input:checked::after{transform:rotate(-45deg) translate(1px,-1px) scale(1)}
.tt-check strong{display:block; font-family:var(--display); font-stretch:104%; font-size:1.08rem; line-height:1.3}
.tt-check em{display:block; font-style:normal; margin-top:6px; color:var(--ink-soft); font-size:.94rem}
.tt-check em::before{content:"Ask: "; font-family:var(--mono); font-size:.7rem; letter-spacing:.08em; text-transform:uppercase; color:var(--logo-teal); font-weight:600}
.tt-check__foot{display:flex; flex-wrap:wrap; gap:10px 18px; align-items:center; justify-content:space-between; padding:14px clamp(18px,2.6vw,28px); border-top:1px solid var(--line); font-size:.88rem; color:var(--ink-soft)}
.tt-split{display:grid; grid-template-columns:minmax(0,.8fr) minmax(0,1.2fr); gap:clamp(24px,4vw,56px); align-items:start}
@media (max-width:900px){.tt-split{grid-template-columns:1fr}}

.tt-ex{display:grid; grid-template-columns:minmax(0,1.15fr) minmax(0,.85fr); gap:clamp(14px,2vw,22px); align-items:stretch}
.tt-ex > div{border-radius:var(--r-xl); padding:clamp(20px,2.6vw,30px); background:rgba(255,255,255,.05); border:1px solid var(--line-dark); display:flex; flex-direction:column}
.tt-ex h3{font-size:1.35rem; margin:.2em 0 .4em; color:#fff}
.tt-ex p{color:rgba(255,255,255,.84); font-size:.97rem}
.tt-ex ul{margin:0 0 1em; padding-left:1.1em; color:rgba(255,255,255,.84); font-size:.97rem}
.tt-ex small{margin-top:auto; font-family:var(--mono); font-size:.7rem; letter-spacing:.06em; text-transform:uppercase; color:var(--aqua)}
.tt-ex small a{color:var(--mint)}
.tt-note{margin-top:clamp(16px,2vw,22px); font-size:.92rem; color:rgba(255,255,255,.75)}
@media (max-width:860px){.tt-ex{grid-template-columns:1fr}}

.tt-heal{display:grid; grid-template-columns:minmax(0,1.1fr) minmax(0,.9fr); gap:clamp(24px,4vw,56px); align-items:center}
.tt-heal__box{background:var(--mist); border:1px solid var(--line); border-radius:var(--r-xl); padding:clamp(20px,2.6vw,28px); display:grid; gap:12px}
.tt-heal__box p{margin:0}
@media (max-width:860px){.tt-heal{grid-template-columns:1fr}}

.tt-return{display:grid; grid-template-columns:auto minmax(0,1fr) auto; gap:clamp(18px,3vw,36px); align-items:center}
.tt-return > .daisy{width:clamp(64px,8vw,96px); height:clamp(64px,8vw,96px); color:var(--mint)}
.tt-return h2{font-weight:600; font-stretch:84%; margin-bottom:.2em}
@media (max-width:760px){.tt-return{grid-template-columns:1fr}}

.tt-src{margin:0; padding:0; list-style:none; counter-reset:src; display:grid; gap:10px}
.tt-src li{margin:0; counter-increment:src; display:grid; grid-template-columns:34px minmax(0,1fr); gap:10px; font-size:.92rem; line-height:1.5; scroll-margin-top:120px}
.tt-src li::before{content:counter(src); font-family:var(--mono); font-weight:600; color:var(--logo-teal); background:var(--aqua); border-radius:8px; height:26px; display:grid; place-items:center; font-size:.78rem}
.tt-src li:target{background:#fff; border-radius:10px; box-shadow:0 0 0 2px var(--mint)}
.tt-src a{color:var(--logo-teal); font-weight:600; word-break:break-word}
.tt-h2{font-weight:600; font-stretch:84%}
.band--paper .tt-h2,.band--mist .tt-h2,.band--aqua .tt-h2{color:var(--logo-teal)}

@media print{
  body *{visibility:hidden}
  .tt-check, .tt-check *{visibility:visible}
  .tt-check{position:absolute; left:0; top:0; width:100%; box-shadow:none}
  .tt-check__foot{display:none}
}
'''

TT_JS = r'''<script>(function(){
  var KEY = 'sb-tattoo-check', box = document.querySelector('.tt-check'); if(!box) return;
  var inputs = box.querySelectorAll('input[type=checkbox]'), out = box.querySelector('[data-count]');
  function save(){ var v = []; inputs.forEach(function(i, k){ if(i.checked) v.push(k); }); try{ localStorage.setItem(KEY, JSON.stringify(v)); }catch(e){} if(out) out.textContent = v.length + ' of ' + inputs.length + ' checked'; }
  try{ var v = JSON.parse(localStorage.getItem(KEY) || '[]'); v.forEach(function(k){ if(inputs[k]) inputs[k].checked = true; }); }catch(e){}
  inputs.forEach(function(i){ i.addEventListener('change', save); });
  save();
  var p = box.querySelector('[data-print]'); if(p) p.addEventListener('click', function(){ window.print(); });
  var r = box.querySelector('[data-reset]'); if(r) r.addEventListener('click', function(){ inputs.forEach(function(i){ i.checked = false; }); save(); });
})();</script>'''


def fordaisy_tattoos():
    carried = [
        ('Carried on skin', '…you’ll always be in my heart and a piece of you forever tattooed on my hip.', 'heart', True),
        ('Carried on skin', '…look down at the tattoos you’ve put on my body, I’m constantly reminded of you and the impact just you as a person has put on my life.', 'daisy', False),
        ('In her honor', '…when she died I got a tattoo of a daisy in her honor', 'daisy', False),
        ('In her honor', 'I wanted to meet you and get a tattoo from you someday. now I will design a tattoo in your honor for myself.', 'spark', False),
        ('Hoped to be tattooed by her', 'I miss you daisy. I always wanted to be tattooed by you', 'spark', True),
        ('Hoped to be tattooed by her', 'I dreamt of one day being tatted by you.', 'spark', False),
        ('Hoped to be tattooed by her', 'I still wish to get the tattoo I planned to get done by you, in your memory.', 'heart', False),
        ('Hoped to be tattooed by her', 'I wish I had gotten the chance to meet you and be tattooed by you.', 'spark', False),
        ('Her other art', "she painted a picture of my cat for me and my cat has passed since. it's such a beautiful bittersweet piece of art!", 'heart', False),
        ('Her other art', 'You gave me strength, you made me laugh, you leveled me with your art and the magic you carried with you.', 'daisy', True),
    ]
    carried_html = ''.join(f'<figure class="tt-q{" tt-q--lead" if lead else ""}">{TT_ICONS[ic]}<span class="chip">{esc(tag)}</span><p>“{esc(q)}”</p></figure>' for tag, q, ic, lead in carried)

    flash = [
        ('daisy', 'Choice over your own body', [
            f'Trauma can take away a person’s control over their body, and healing often involves restoring choice. A tattoo is a sensation the person chose, for a set length of time, that they can pause or stop.{cite("fletcher")}',
            f'In interviews with survivors and tattoo artists, researchers found the tattoo setting supported survivors’ autonomy.{cite("maxwell")}']),
        ('heart', 'Ritual and belonging', [
            f'Researchers analyzed interviews with 10 survivors of sexual trauma and 7 tattoo artists. Rapport with the artist and the ritual of getting tattooed helped survivors feel they belonged, and the look and feel of the studio helped it feel comfortable and safe.{cite("maxwell")}']),
        ('sun', 'Marking a new chapter', [
            f'Some survivors describe a tattoo as a way to mark a new chapter. A survivor quoted by the National Resource Center on Domestic Violence put it this way: “My first tattoo gave me the strength to leave an abusive marriage.”{cite("branco")}']),
        ('vine', 'Covering a reminder', [
            f'Some marks are painful reminders, such as a scar, an abuser’s name or a brand used by traffickers. Artists can cover them or turn them into new art, and tattoo removal is another option.{cite("branco", "npr")}']),
    ]
    flash_html = ''.join(f'<article class="tt-f"><span class="tt-f__icon">{TT_ICONS[ic]}</span><div><h3>{esc(t)}</h3>' + ''.join(f'<p>{p}</p>' for p in ps) + '</div></article>' for ic, t, ps in flash)

    checks = [
        ('The artist doesn’t ask whether you’ve experienced trauma. You decide if, how and when to share anything personal.', 'Do you need to know anything about me before we start?'),
        ('They explain what they’re about to do and ask before touching, adjusting or moving you.', 'Will you tell me before you touch me or move my arm?'),
        ('They check in during the session and remind you that you can pause, stop or speak up at any time.', 'Can we take a break whenever I need one?'),
        ('They offer privacy: a private room if there is one, or sheets or coverings so only the area being tattooed is exposed.', 'Is there a private space, or a way to keep the rest of me covered?'),
        ('They avoid edgy jokes with clients they don’t know well, steer clear of topics like politics or religion, and never assume your boundaries or comfort level.', 'Can I tell you what I’m comfortable talking about?'),
        ('They let you warm up to them, without forcing a connection.', 'Is it okay if I’m quiet during the session?'),
    ]
    check_html = ''.join(f'<li><label><input type="checkbox" name="tt-{k}"><span><strong>{esc(t)}</strong><em>{esc(q)}</em></span></label></li>' for k, (t, q) in enumerate(checks))

    src_html = ''.join(f'<li id="src-{k}"><span>{text} <a href="{u}" target="_blank" rel="noopener">{esc(lbl)} &#8599;</a></span></li>' for k, text, u, lbl in TT_SOURCES)

    body = f'''
<section class="tt-hero v2-light">
  <span class="wm-daisy" aria-hidden="true"></span>
  <div class="wrap tt-hero__grid">
    <div class="rise">
      <nav class="crumbs" aria-label="Breadcrumb"><a href="index.html">Home</a><span>/</span><a href="fordaisy.html">#ForDaisy</a><span>/</span><span>Tattoos &amp; Healing</span></nav>
      <p class="dz-mark">{daisy()}#ForDaisy</p>
      <h1>Tattoos &amp; <span class="mk">healing</span></h1>
      <p class="lede">Daisy Coleman, SafeBAE’s co-founder, was a tattoo artist whose work people still carry with them. Some survivors of sexual violence describe getting tattooed as one way to reclaim their bodies. It is one path among many, and it isn’t right for everyone.</p>
      <div class="btns">{btn('What survivors describe', '#describe', 'slate')}{btn('Questions for a consultation', '#consultation', 'ghost')}</div>
    </div>
    <div class="tt-comp">
      <div class="tt-comp__main">{img('fordaisy28', 'Daisy Coleman tattooing a client', loading='eager')}</div>
      <div class="tt-comp__sub">{img('fordaisy25', 'Daisy Coleman at a tattoo studio', loading='eager')}</div>
      <span class="sticker sticker--aqua">Daisy at work</span>
      <span class="tt-doodle tt-doodle--a">{TT_ICONS['daisy']}</span>
      <span class="tt-doodle tt-doodle--b">{TT_ICONS['spark']}</span>
      <span class="tt-doodle tt-doodle--c">{TT_ICONS['spark']}</span>
    </div>
  </div>
</section>

<section class="band band--deep" id="carried">
  <div class="wrap">
    <div class="section-head"><div><p class="eyebrow">From the #ForDaisy tribute wall</p><h2 class="tt-h2">The people who carry her work</h2>
      <p class="lede lede--full" style="color:rgba(255,255,255,.86)">In their messages for Daisy, people wrote about tattoos she gave them and tattoos they got in her honor. Others wrote about the tattoo they had hoped she would give them.</p></div></div>
    <div class="tt-carried">{carried_html}</div>
    <div class="tt-from"><span>Excerpts from messages on the #ForDaisy Memorial Tribute Wall, quoted as written.</span>{a('Read the tribute wall &rarr;', 'fordaisy.html#wall')}</div>
  </div>
</section>

<section class="band band--paper" id="describe">
  <div class="wrap">
    <div class="section-head"><div><h2 class="tt-h2">What survivors and researchers describe</h2>
      <p class="lede lede--full muted">Research on tattooing and healing after sexual violence is limited.{cite("branco")} Survivors, tattoo artists and researchers describe a few reasons it can matter.</p></div></div>
    <div class="tt-flash">{flash_html}</div>
  </div>
</section>

<section class="band band--aqua" id="one-path">
  <div class="wrap">
    <blockquote class="tt-quote">“Tattoos are neither inherently pathological nor inherently therapeutic.”<cite>Adrian A. Fletcher, Psy.D., <i>Psychology Today</i>{cite("fletcher")}</cite></blockquote>
    <h2 class="tt-h2">Before you decide</h2>
    <div class="tt-path">
      <div><h3>It isn’t a treatment</h3><p>Tattoos should never be prescribed as treatment.{cite("fletcher")} Body art is one of many ways people heal, and it isn’t right for everyone.{cite("branco")}</p></div>
      <div><h3>Readiness matters</h3><p>Before getting tattooed, weigh medical safety, whether you feel ready, and whether you understand what you are agreeing to.{cite("fletcher")} A tattoo is permanent, so there is no rush.</p></div>
      <div><h3>Some marks hurt</h3><p>A tattoo can also become a painful reminder. If you carry one, covering it up or having it removed are options.{cite("branco")}</p></div>
    </div>
    <div class="tt-minor"><b>Under 18?</b><p>Tattoo laws for minors differ from state to state. In a 2013 review, 17 states banned tattooing anyone under 18 and 28 allowed it only with a parent’s consent.{cite("olr")} Check your state’s rules before you plan anything.</p></div>
  </div>
</section>

<section class="band band--paper" id="consultation">
  <div class="wrap tt-split">
    <div>
      <h2 class="tt-h2">What trauma-informed tattooing looks like</h2>
      <p class="lede">Tattoo artist Cora Weisenberger describes practices artists can use with every client.{cite("weisenberger")}</p>
      <p class="muted">Take this list to a consultation. Tick off what the studio already does, and use the questions to ask about the rest. Your ticks stay on this device.</p>
    </div>
    <div class="tt-check">
      <div class="tt-check__head"><b>Before you book</b><span data-count>0 of {len(checks)} checked</span></div>
      <ol>{check_html}</ol>
      <div class="tt-check__foot"><span>Source: Weisenberger (2025), Kingpin Tattoo Supply.</span><span class="btns"><button class="btn btn--slate btn--sm" type="button" data-print>Print this list</button><button class="btn btn--ghost btn--sm" type="button" data-reset>Clear</button></span></div>
    </div>
  </div>
</section>

<section class="band band--slate" id="cover-ups">
  <div class="wrap">
    <div class="section-head"><div><h2 class="tt-h2">Cover-up programs in the news</h2>
      <p class="lede lede--full" style="color:rgba(255,255,255,.86)">Some artists offer free or low-cost cover-ups for survivors. These are examples from reporting, not SafeBAE partners.</p></div></div>
    <div class="tt-ex">
      <div>
        <p class="eyebrow">Amherst, Ohio &middot; reported 2025</p>
        <h3>Phoenix Ink &amp; Beauty: the Art of Healing program</h3>
        <p>Co-owner Angelique Agnew’s studio covers scars from self-harm or surgery, and works with survivors of human trafficking.{cite("npr")}</p>
        <ul><li>People apply; if accepted, they pay only for the ink and tattooing supplies.</li><li>Artists donate their time and art.</li></ul>
        <small>Source: Ideastream Public Media for NPR</small>
      </div>
      <div>
        <p class="eyebrow">Reported 2017</p>
        <h3>Artists covering marks left by abuse</h3>
        <p>A 2017 overview from the National Resource Center on Domestic Violence described artists offering free cover-ups to survivors, such as Flavia Carvalho in Brazil, and Sacred Transformations, a Chicago organization that turns scars or marks left by abuse, neglect, rape or trafficking into art.{cite("branco")}</p>
        <small>Source: VAWnet</small>
      </div>
    </div>
    <p class="tt-note">Programs change. Check current details directly with any studio before you make plans.</p>
  </div>
</section>

<section class="band band--paper" id="other-ways">
  <div class="wrap tt-heal">
    <div>
      <h2 class="tt-h2">If a tattoo isn’t right for you, or not right now</h2>
      <p class="lede">Healing is long, nonlinear, and personal, and there is no right or wrong way to do it. Many survivors find strength in connection with peers, support groups, or professionals, and in practices that help them reconnect with their bodies and feelings.</p>
    </div>
    <div class="tt-heal__box">
      <p><b>Talk to someone now.</b> Free, confidential hotlines, most open 24/7.</p>
      <div class="btns"><button class="btn btn--slate" type="button" data-open-help>See support hotlines</button>{btn('Survivor support', 'survivor-support.html', 'ghost', arrow=True)}</div>
    </div>
  </div>
</section>

<section class="band band--logo band--tight">
  <div class="wrap tt-return">
    {daisy()}
    <div><h2>Back to #ForDaisy</h2>
      <p style="margin:0;color:rgba(255,255,255,.86)">Read the messages people wrote for Daisy, or add your own.</p></div>
    <div class="btns">{btn('Add your message', 'fordaisy.html#add', 'mint', arrow=True)}{btn('Tribute wall', 'fordaisy.html#wall', 'ghost')}</div>
  </div>
</section>

<section class="band band--mist band--tight" id="sources">
  <div class="wrap">
    <h2 class="tt-h2" style="font-size:clamp(1.5rem,2.4vw,2rem)">Sources</h2>
    <ol class="tt-src">{src_html}</ol>
  </div>
</section>
'''
    page('fordaisy-tattoos.html', 'Tattoos & Healing · #ForDaisy · SafeBAE', 'Daisy Coleman was a tattoo artist whose work people still carry with them. Tattoos as one path some survivors take to reclaim their bodies, and what trauma-informed tattooing looks like.',
         body, active='fordaisy', body_class='pg-daisy pg-tattoo', head_extra=css(DZ_CSS, TT_CSS), scripts=TT_JS)


# =====================================================================
# CONTACT
# =====================================================================
CT_CSS = '''
.ct-hero{background:var(--teal); color:#fff; position:relative; overflow:hidden}
.ct-hero .wm-daisy{color:var(--aqua); opacity:.12}
.ct-hero .wrap{position:relative; z-index:1; padding-block:clamp(40px,5vw,72px) clamp(120px,11vw,160px); display:grid; grid-template-columns:minmax(0,1fr) minmax(0,1fr); gap:clamp(28px,5vw,72px); align-items:center}
.ct-hero h1{font-size:var(--fs-h1); font-stretch:122%; font-weight:900; text-transform:uppercase; line-height:.92; letter-spacing:-.02em; margin:0 0 .35em}
.ct-hero .mk{background:none; color:var(--aqua)}
.ct-hero .crumbs,.ct-hero .crumbs a{color:#fff}
.ct-hero .lede{color:#fff; max-width:none}
.ct-hero .btns{margin-top:6px}
.ct-comp{position:relative; padding:0 0 12% 8%; animation:sb-rise-r 1s .1s var(--ease) both}
.ct-comp > img{width:100%; aspect-ratio:4/3; object-fit:cover; border-radius:var(--r-xl); box-shadow:0 30px 60px -30px rgba(0,0,0,.55)}
.ct-post{position:absolute; left:0; bottom:0; width:min(360px,80%); background:#fff; color:var(--slate); border-radius:16px; padding:18px 20px 16px; transform:rotate(-3deg); box-shadow:0 26px 50px -22px rgba(0,0,0,.55); background-image:repeating-linear-gradient(90deg, transparent 0 calc(60% - 1px), var(--line) calc(60% - 1px) 60%, transparent 60% 100%)}
.ct-post__to{font-family:var(--mono); font-size:.66rem; letter-spacing:.1em; text-transform:uppercase; color:var(--logo-teal); font-weight:600; margin:0 0 6px}
.ct-post address{font-style:normal; font-family:var(--display); font-weight:800; font-stretch:104%; font-size:1.02rem; line-height:1.3; max-width:58%}
.ct-post .copy{margin-top:12px; font-size:.82rem}
.ct-stamp{position:absolute; right:16px; top:14px; width:58px; height:68px; background:var(--mint); border-radius:4px; display:grid; place-items:center; outline:3px dashed #fff; outline-offset:-6px}
.ct-stamp .daisy{width:36px; height:36px; color:var(--slate)}
.ct-postmark{position:absolute; right:52px; top:58px; width:84px; height:84px; border-radius:50%; border:2px solid rgba(29,65,78,.45); display:grid; place-items:center; text-align:center; font-family:var(--mono); font-size:.52rem; line-height:1.25; letter-spacing:.06em; text-transform:uppercase; color:rgba(29,65,78,.75); transform:rotate(14deg); font-weight:600; padding:8px}
@media (max-width:900px){.ct-hero .wrap{grid-template-columns:1fr} .ct-comp{max-width:540px}}
@media (max-width:480px){.ct-postmark{display:none} .ct-post{width:88%} .ct-post address{max-width:70%}}
.ct-route{display:grid; grid-template-columns:repeat(4,minmax(0,1fr)); gap:clamp(12px,1.6vw,18px); margin-top:clamp(-120px,-8vw,-80px); position:relative; z-index:2}
.ct-r{display:flex; flex-direction:column; gap:8px; padding:22px; border-radius:var(--r-xl); background:#fff; color:var(--slate); text-decoration:none; box-shadow:0 24px 50px -30px rgba(22,53,64,.7); border:0; font:inherit; text-align:left; cursor:pointer; transition:transform .2s}
.ct-r:hover{transform:translateY(-4px)}
.ct-r small{font-family:var(--mono); font-size:.68rem; letter-spacing:.1em; text-transform:uppercase; font-weight:600; color:var(--logo-teal)}
.ct-r b{font-family:var(--display); font-weight:900; font-stretch:112%; font-size:1.35rem; line-height:1.1}
.ct-r span{font-size:.92rem; color:var(--ink-soft); line-height:1.45}
.ct-r em{font-style:normal; margin-top:auto; padding-top:8px; font-weight:800; color:var(--logo-teal)}
.ct-r--mint{background:var(--mint)} .ct-r--mint small{color:var(--slate)} .ct-r--mint span{color:var(--slate)}
.ct-r--slate{background:var(--slate); color:#fff} .ct-r--slate small{color:var(--mint)} .ct-r--slate span{color:rgba(255,255,255,.8)} .ct-r--slate em{color:var(--mint)}
.ct-r--coral{background:var(--coral)} .ct-r--coral small,.ct-r--coral span,.ct-r--coral em{color:var(--slate)}
@media (max-width:960px){.ct-route{grid-template-columns:repeat(2,minmax(0,1fr))}}
@media (max-width:520px){.ct-route{grid-template-columns:1fr}}

.ct-main{display:grid; grid-template-columns:minmax(0,1.1fr) minmax(0,.9fr); gap:clamp(20px,3vw,40px); align-items:stretch}
.ct-dir{display:grid; gap:0; border-top:2px solid var(--slate)}
.ct-d{display:grid; grid-template-columns:minmax(0,190px) minmax(0,1fr); gap:8px 24px; padding:20px 0; border-bottom:1px solid var(--line); scroll-margin-top:110px}
.ct-d h3{font-size:1.2rem; margin:0}
.ct-d p{margin:0 0 10px; color:var(--ink-soft); font-size:.95rem}
.ct-d .copy{font-size:.9rem}
.ct-d .copy + .copy{margin-left:6px}
.ct-people{display:flex; flex-wrap:wrap; gap:10px 14px; margin-top:8px}
.ct-people div{display:flex; flex-direction:column; align-items:flex-start; gap:4px}
.ct-people small{font-weight:700; font-size:.82rem}
@media (max-width:640px){.ct-d{grid-template-columns:1fr}}
.ct-form{background:var(--mist); border:1px solid var(--line); border-radius:var(--r-xl); padding:clamp(20px,3vw,32px); display:flex; flex-direction:column}
.ct-form h2{font-size:clamp(1.6rem,2.6vw,2.2rem)}
.ct-form .form{flex:1; display:flex; flex-direction:column; margin-top:8px}
.ct-form .ct-grow{flex:1; display:flex; flex-direction:column}
.ct-form .ct-grow textarea{flex:1; min-height:160px}
.ct-two{display:grid; grid-template-columns:1fr 1fr; gap:14px}
@media (max-width:520px){.ct-two{grid-template-columns:1fr}}
.ct-req{display:grid; grid-template-columns:minmax(0,.85fr) minmax(0,1.15fr); gap:clamp(24px,4vw,56px); align-items:start}
.ct-req .form{background:rgba(255,255,255,.06); border:1px solid var(--line-dark); border-radius:var(--r-xl); padding:clamp(18px,2.6vw,28px)}
.ct-req label{color:#fff}
.ct-req .field input,.ct-req .field textarea{border-color:transparent}
.ct-req .form__note{color:rgba(255,255,255,.7)}
.ct-offer{display:flex; flex-wrap:wrap; gap:8px; margin:18px 0 22px; padding:0; list-style:none}
.ct-offer li{margin:0; padding:8px 14px; border-radius:999px; background:rgba(21,255,200,.12); border:1px solid rgba(21,255,200,.4); color:var(--aqua); font-weight:700; font-size:.9rem}
@media (max-width:860px){.ct-req,.ct-main{grid-template-columns:1fr}}
.ct-info{display:grid; grid-template-columns:repeat(3,minmax(0,1fr)); gap:clamp(12px,1.6vw,18px)}
.ct-info > div{background:var(--mist); border:1px solid var(--line); border-radius:var(--r-xl); padding:22px; display:flex; flex-direction:column; gap:8px}
.ct-info h3{font-size:1.15rem; margin:0}
.ct-info address{font-style:normal; font-weight:600; line-height:1.5}
.ct-soc{display:flex; flex-wrap:wrap; gap:8px}
.ct-soc a{padding:7px 12px; border-radius:8px; background:var(--aqua); color:var(--slate); font-weight:700; font-size:.88rem; text-decoration:none}
.ct-soc a:hover{background:var(--mint)}
@media (max-width:860px){.ct-info{grid-template-columns:1fr}}
'''


def copy_email(e):
    return f'<span class="copy">{esc(e)}<button type="button" data-copy="{esc(e)}" aria-label="Copy {esc(e)}">Copy</button></span>'


def contact():
    body = f'''
<section class="ct-hero">
  <span class="wm-daisy" aria-hidden="true"></span>
  <div class="wrap">
    <div class="rise">
      <nav class="crumbs" aria-label="Breadcrumb"><a href="index.html">Home</a><span>/</span><a href="about.html">About</a><span>/</span><span>Contact</span></nav>
      <h1><span class="mk">Contact</span> us</h1>
      <p class="lede">We respond to general inquiries within 2 to 3 business days. Journalists on deadline can reach our leadership directly.</p>
      <div class="btns">{btn('Write to the team', '#message', 'white', arrow=True)}{btn('Press contacts', '#press', 'ghost')}</div>
    </div>
    <div class="ct-comp">
      {img('img-6834', 'A group of SafeBAE youth leaders smiling together outdoors', loading='eager')}
      <div class="ct-post">
        <p class="ct-post__to">Write to</p>
        <address>SafeBAE<br>7 Evelyn Drive<br>Bristol, RI 02809</address>
        {copy_email('info@safebae.org')}
        <span class="ct-stamp" aria-hidden="true">{daisy()}</span>
        <span class="ct-postmark" aria-hidden="true">Replies in 2–3 business days</span>
      </div>
    </div>
  </div>
</section>

<section class="band band--paper" style="padding-top:0">
  <div class="wrap">
    <div class="ct-route">
      <a class="ct-r ct-r--mint" href="request-a-program.html"><small>Schools &amp; communities</small><b>Bring SafeBAE to your school</b><span>Student presentations, staff trainings, parent nights and club chapter support.</span><em>Request a program &rarr;</em></a>
      <a class="ct-r" href="mailto:clubsupport@safebae.org"><small>SafeBAE clubs</small><b>Club support</b><span>Students and faculty advisors can email clubsupport@safebae.org with questions, challenges or event ideas.</span><em>Email club support &rarr;</em></a>
      <a class="ct-r ct-r--slate" href="#press"><small>Journalists</small><b>Press &amp; media</b><span>Send your outlet, topic and deadline. On deadline, reach our leadership directly.</span><em>Press contacts &darr;</em></a>
      <button class="ct-r ct-r--coral" type="button" data-open-help><small>Free &amp; confidential</small><b>Need help now?</b><span>Hotlines for survivors, friends and anyone in crisis, most open 24/7. If you are in danger, call 911.</span><em>Open support resources &rarr;</em></button>
    </div>

    <div class="ct-main" style="margin-top:clamp(40px,5vw,64px)">
      <div>
        <h2>Reach the right person</h2>
        <div class="ct-dir">
          <div class="ct-d" id="general"><h3>General inquiries</h3><div><p>Email us or use the message form. We respond within 2 to 3 business days.</p>{copy_email('info@safebae.org')}</div></div>
          <div class="ct-d" id="press"><h3>Press &amp; media</h3><div><p>Email info@safebae.org with your outlet, topic, and deadline, or use the form. If you are on deadline, you can reach our leadership directly.</p>{copy_email('info@safebae.org')}
            <div class="ct-people"><div><small>Shael Norris, Executive Director</small>{copy_email('shael@safebae.org')}</div><div><small>Drew Davis, Director of Strategic Initiatives</small>{copy_email('drew@safebae.org')}</div></div></div></div>
          <div class="ct-d" id="partnerships"><h3>Partnerships</h3><div><p>We partner with schools, districts, nonprofits, brands, and funders. Email us a short description of your organization and what you have in mind.</p>{copy_email('info@safebae.org')}</div></div>
          <div class="ct-d" id="clubs"><h3>Club support</h3><div><p>Questions about starting, registering or running a SafeBAE club, or the Club Hub. You can also book a virtual meeting with our programming team.</p>{copy_email('clubsupport@safebae.org')} <a class="link" href="https://calendly.com/clubsupport-safebae/30min" target="_blank" rel="noopener" style="margin-left:8px;font-size:.92rem;white-space:nowrap;display:inline-block;margin-top:6px">Book a meeting &#8599;</a></div></div>
        </div>
      </div>
      <div class="ct-form" id="message">
        <h2>Send us a message</h2>
        <p class="muted">Messages sent here reach the same team as info@safebae.org.</p>
        <form class="form" data-static data-mailto="info@safebae.org" data-subject="Message from safebae.org">
          <div class="field"><label for="ct-name">Name</label><input id="ct-name" name="Name" autocomplete="name" required></div>
          <div class="field"><label for="ct-email">Email address</label><input id="ct-email" name="Email" type="email" autocomplete="email" required></div>
          <div class="field ct-grow"><label for="ct-msg">Message</label><textarea id="ct-msg" name="Message" required></textarea></div>
          <div><button class="btn btn--slate" type="submit">Send message</button></div>
          <p class="form__done" role="status">Thank you. Your message is on its way to the SafeBAE team.</p>
        </form>
      </div>
    </div>
  </div>
</section>

<section class="band band--slate" id="request">
  <div class="wrap ct-req">
    <div>
      <h2>Bring SafeBAE to your school or community</h2>
      <p class="lede" style="color:rgba(255,255,255,.88)">Want SafeBAE at your school or in your community? Fill out the form to tell us what you’d like to book or learn more about.</p>
      <ul class="ct-offer"><li>Student presentations</li><li>Staff trainings</li><li>Parent nights</li><li>Club chapter support</li></ul>
      <div class="btns">{btn('See programs & pricing', 'request-a-program.html', 'mint', arrow=True)}{btn('360° Schools', '360-schools.html', 'ghost')}</div>
    </div>
    <form class="form" data-static data-mailto="info@safebae.org" data-subject="Program request from safebae.org">
      <div class="ct-two"><div class="field"><label for="rq-name">Name</label><input id="rq-name" name="Name" autocomplete="name" required></div>
      <div class="field"><label for="rq-org">School or organization</label><input id="rq-org" name="School or organization" autocomplete="organization" required></div></div>
      <div class="ct-two"><div class="field"><label for="rq-email">Email address</label><input id="rq-email" name="Email" type="email" autocomplete="email" required></div>
      <div class="field"><label for="rq-phone">Cell phone</label><input id="rq-phone" name="Cell phone" type="tel" autocomplete="tel"></div></div>
      <div class="field"><label for="rq-msg">What are you hoping to book or learn more about?</label><textarea id="rq-msg" name="Request" placeholder="Share what you’re hoping to book or learn more about…" required></textarea></div>
      <div><button class="btn btn--mint" type="submit">Submit request</button></div>
      <p class="form__done" role="status">Thank you. Our team will be in touch about your request.</p>
    </form>
  </div>
</section>

<section class="band band--paper band--tight">
  <div class="wrap ct-info">
    <div><h3>Mailing address</h3><address>SafeBAE<br>7 Evelyn Drive<br>Bristol, RI 02809</address><p class="small muted" style="margin:0">SafeBAE is a registered 501(c)(3) nonprofit. EIN 81-5451147.</p></div>
    <div><h3>Follow us</h3><p class="muted" style="margin:0">New resources, campaigns, and youth organizing updates.</p>
      <div class="ct-soc">{a('Instagram', 'https://www.instagram.com/safe_bae/')}{a('TikTok', 'https://www.tiktok.com/@safe_bae')}{a('LinkedIn', 'https://www.linkedin.com/company/safebae/')}{a('YouTube', 'https://www.youtube.com/@SafeBAE')}{a('Facebook', 'https://www.facebook.com/www.safebae.org')}</div></div>
    <div><h3>Newsletter</h3><p class="muted" style="margin:0">Stories, analysis and news from SafeBAE, in your inbox.</p><div class="btns" style="margin-top:auto">{btn('Subscribe on Substack', 'https://substack.com/@safebae', 'slate', 'sm')}</div></div>
  </div>
</section>
{give_band()}
'''
    page('contact.html', 'Contact · SafeBAE', 'Contact SafeBAE: general inquiries, press and media, partnerships, club support, and requests to bring SafeBAE to your school or community.',
         body, active='about', body_class='pg-contact', head_extra=css(CT_CSS))


# =====================================================================
# PHOTO CREDITS
# =====================================================================
CR_CSS = '''
.cr-hero{background-color:var(--logo-teal); color:#fff}
.cr-hero .wrap{padding-block:clamp(44px,5.5vw,80px); display:grid; grid-template-columns:minmax(0,1fr) minmax(0,1fr); gap:clamp(28px,5vw,72px); align-items:center}
.cr-hero h1{font-size:var(--fs-h1); font-stretch:122%; font-weight:900; text-transform:uppercase; line-height:.92; letter-spacing:-.02em; margin:0 0 .35em}
.cr-hero .lede{color:rgba(255,255,255,.9); max-width:none}
.cr-sheet{position:relative; display:grid; grid-template-columns:repeat(3,minmax(0,1fr)); gap:10px; padding:26px 16px 34px; background:#0f2a33; border-radius:var(--r-xl); box-shadow:0 30px 60px -30px rgba(0,0,0,.7); transform:rotate(-1.5deg); animation:sb-rise-r 1s .1s var(--ease) both}
.cr-sheet::before,.cr-sheet::after{content:""; position:absolute; left:16px; right:16px; height:8px; background:repeating-linear-gradient(90deg, rgba(209,254,255,.28) 0 10px, transparent 10px 22px); border-radius:2px}
.cr-sheet::before{top:9px} .cr-sheet::after{bottom:9px}
.cr-frame{position:relative; display:block; aspect-ratio:4/3; overflow:hidden; border-radius:4px; background:#000}
.cr-frame img{width:100%; height:100%; object-fit:cover; filter:saturate(.9)}
.cr-frame i{position:absolute; left:6px; bottom:4px; font-style:normal; font-family:var(--mono); font-size:.6rem; color:#fff; text-shadow:0 1px 3px rgba(0,0,0,.8)}
.cr-loop{position:absolute; left:calc(33.3% + 2px); top:14px; width:calc(33.3% + 14px); height:calc(50% + 2px); color:var(--mint); overflow:visible; pointer-events:none; filter:drop-shadow(0 0 6px rgba(21,255,200,.45))}
.cr-sheet__label{position:absolute; right:18px; bottom:-16px; font-family:var(--mono); font-size:.66rem; letter-spacing:.1em; text-transform:uppercase; background:var(--mint); color:var(--slate); padding:5px 9px; border-radius:6px; font-weight:600; transform:rotate(1.5deg)}
@media (max-width:900px){.cr-hero .wrap{grid-template-columns:1fr} .cr-sheet{max-width:560px}}
.cr-grid{--g:clamp(12px,1.6vw,18px); display:flex; flex-wrap:wrap; justify-content:center; gap:var(--g)}
.cr{margin:0; background:#fff; border:1px solid var(--line); border-radius:var(--r-xl); overflow:hidden; display:flex; flex-direction:column; width:calc((100% - 3*var(--g))/4); min-width:0}
.cr img{width:100%; aspect-ratio:4/3; object-fit:cover; background:var(--mist)}
.cr figcaption{padding:14px 16px 16px; font-size:.9rem; line-height:1.45; display:flex; flex-direction:column; gap:6px; flex:1}
.cr figcaption a{color:var(--logo-teal); font-weight:700}
.cr small{font-family:var(--mono); font-size:.66rem; letter-spacing:.06em; text-transform:uppercase; color:var(--ink-soft); margin-top:auto}
.cr small a{color:var(--ink-soft); font-weight:600}
@media (max-width:1000px){.cr{width:calc((100% - 2*var(--g))/3)}}
@media (max-width:720px){.cr{width:calc((100% - var(--g))/2)}}
@media (max-width:420px){.cr{width:100%}}
.cr-note{display:grid; grid-template-columns:repeat(3,minmax(0,1fr)); gap:clamp(12px,1.6vw,18px)}
.cr-note > div{background:#fff; border:1px solid var(--line); border-radius:var(--r-xl); padding:20px}
.cr-note h3{font-size:1.1rem}
.cr-note p{margin:0; color:var(--ink-soft); font-size:.94rem}
@media (max-width:860px){.cr-note{grid-template-columns:1fr}}
'''

PAGE_NAMES = {}


def _page_label(fn):
    if os.path.basename(fn) == 'index.html':
        return 'Home'
    try:
        t = re.search(r'<title>(.*?)</title>', open(fn, encoding='utf-8').read(), re.S).group(1)
        t = html_unescape(t).split(' · ')[0].strip()
        return t or os.path.basename(fn)
    except Exception:
        return os.path.basename(fn)


def html_unescape(s):
    import html as _h
    return _h.unescape(s)


def credits():
    P = '/home/claude/v2/build/credits.jsonl'
    entries = {}
    if os.path.exists(P):
        for line in open(P, encoding='utf-8'):
            line = line.strip()
            if not line:
                continue
            try:
                d = json.loads(line)
            except Exception:
                continue
            if d.get('slug'):
                entries[d['slug']] = d
    # where each photo is used (scan built pages)
    pages = sorted(glob.glob(f'{SITE}/*.html'))
    used = {s: [] for s in entries}
    page_txt = {}
    for fn in pages:
        if fn.endswith('credits.html'):
            continue
        try:
            t = open(fn, encoding='utf-8').read()
            i, j = t.find('<main'), t.find('</main>')
            page_txt[fn] = t[i:j] if i >= 0 and j > i else t
        except Exception:
            pass
    for s in entries:
        for fn, t in page_txt.items():
            if f'assets/img/{s}.webp' in t:
                used[s].append(os.path.basename(fn))
    cards = []
    for s, d in sorted(entries.items(), key=lambda kv: (kv[1].get('name', '').lower(), kv[0])):
        has = os.path.exists(f'{SITE}/assets/img/{s}.webp') or s in MANIFEST
        pic = img(s, f'Photo by {d.get("name", "")}') if has else ''
        where = ''
        if used.get(s):
            where = '<small>Used on: ' + ', '.join(f'<a href="{u}">{esc(_page_label(os.path.join(SITE, u)))}</a>' for u in used[s][:4]) + ('…' if len(used[s]) > 4 else '') + '</small>'
        cards.append(f'<figure class="cr">{pic}<figcaption><span>Photo by <a href="{esc(d.get("profile", "https://unsplash.com"))}" target="_blank" rel="noopener">{esc(d.get("name", "Unknown"))}</a> on <a href="{esc(d.get("page", "https://unsplash.com"))}" target="_blank" rel="noopener">Unsplash</a></span>{where}</figcaption></figure>')
    grid = f'<div class="cr-grid">{"".join(cards)}</div>' if cards else '<p class="note">No stock photography is in use on this site.</p>'
    n = len(cards)
    sheet = ''.join(f'<span class="cr-frame">{img(x, "", loading="eager")}<i>{k + 1:02d}</i></span>' for k, x in enumerate(['1-000383-edited', 'clubtabling', '2023-institute-selfie', 'img-1286', 'sumact5', '000398']))

    body = f'''
<section class="cr-hero v2-dark">
  <span class="wm-daisy" aria-hidden="true"></span>
  <div class="wrap">
    <div class="rise">
      <nav class="crumbs" aria-label="Breadcrumb"><a href="index.html">Home</a><span>/</span><span>Photo credits</span></nav>
      <h1>Photo <span class="mk">credits</span></h1>
      <p class="lede">Most photographs on this site come from SafeBAE’s own programs, events and partners. Where a page needed a photo we didn’t have, we used images from Unsplash, credited here with thanks to the photographers.</p>
    </div>
    <div class="cr-sheet" aria-hidden="true">
      {sheet}
      <svg class="cr-loop" viewBox="0 0 100 100" preserveAspectRatio="none"><path d="M12 52C8 26 30 9 54 9c24 0 38 16 36 38-2 24-24 42-48 41C20 87 6 72 9 50 11 33 27 18 48 16" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" vector-effect="non-scaling-stroke"/></svg>
      <span class="cr-sheet__label">SafeBAE &middot; programs &amp; events</span>
    </div>
  </div>
</section>
<section class="band band--paper">
  <div class="wrap">
    <div class="section-head"><div><p class="eyebrow">Unsplash photography</p><h2>{n} photo{"s" if n != 1 else ""} from Unsplash</h2></div>{btn('About the Unsplash License', 'https://unsplash.com/license', 'ghost')}</div>
    {grid}
  </div>
</section>
<section class="band band--mist band--tight">
  <div class="wrap cr-note">
    <div><h3>SafeBAE photos</h3><p>Photos of SafeBAE students, clubs, events, staff and board come from SafeBAE and the young people and families we work with. Please ask before reusing them: {a('info@safebae.org', 'mailto:info@safebae.org', 'link')}.</p></div>
    <div><h3>Partner films &amp; media</h3><p>Film stills, video thumbnails and podcast artwork belong to the films, channels and shows they come from.</p></div>
    <div><h3>Logos</h3><p>Logos of partners, schools and publications belong to their organizations and appear to identify them.</p></div>
  </div>
</section>
'''
    page('credits.html', 'Photo credits · SafeBAE', 'Credits for the photography used on safebae.org, including photos from Unsplash.',
         body, active='', body_class='pg-credits', head_extra=css(CR_CSS))


def build():
    about()
    team()
    impact()
    partners()
    fordaisy()
    fordaisy_tattoos()
    contact()
    credits()  # last, so it can see which pages use each photo


if __name__ == '__main__':
    build()
