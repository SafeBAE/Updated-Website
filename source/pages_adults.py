"""Adults + Giving group: adults, parents, educators, college, request-a-program,
donate, chip-in, fundraise.  Content carried from the live safebae.org pages
(get-involved, parents, educators, college-students, request-a-program, donate,
chipin, justin, tuna, vanessa) plus the Check Their Vibe adult guide PDF and the
site FAQ answers already in data.py."""
from lib import *
from data import LIB, FAQ, PODCASTS, WP
from pages_home import FILMS, FILM_STRIP_CSS, film_font_link, film_strip, cpet_player, ring_svg
import json

GUIDE_PDF = WP + '2026/03/Check-Their-Vibe-A-Guide-to-Vibe-Check.pdf'
POSTERS_ZIP = WP + '2025/08/Posters.zip'
CALENDLY = 'https://calendly.com/shaelnorris/60min'
VENMO = 'https://venmo.com/safe-bae'
EMAIL = 'info@safebae.org'
ZEFFY_EMBED = 'https://www.zeffy.com/embed/donation-form/'
ZEFFY_PUBLIC = 'https://www.zeffy.com/en-US/donation-form/'


def mailto(subject):
    return f'mailto:{EMAIL}?subject=' + subject.replace(' ', '%20')


def copyable(text, shown=None):
    return f'<span class="copy">{esc(shown or text)}<button type="button" data-copy="{esc(text)}">Copy</button></span>'


def embed_box(src, link, label, button, height=720, title='Embedded form', kind='teal', extra='', cls=''):
    """Same contract as lib.embed (site.js swaps in the iframe on a live site) with our own fallback wording."""
    return (f'<div class="embed" data-embed="{esc(src)}" data-h="{height}" data-title="{esc(title)}">'
            f'<div class="embed__fallback ad-fallback {cls}"><p><b>{esc(label)}</b></p>{btn(button, link, kind)}{extra}</div></div>')


def faq(q):
    for _, items in FAQ:
        for qq, aa, link in items:
            if qq == q:
                return aa, link
    raise KeyError(q)


def film(key):
    return next(f for f in FILMS if f[1] == key)


def fcard(key, go='Watch together &rarr;'):
    href, k, title, im, tag = film(key)
    return (f'<a class="fcard fcard--{k}" href="{href}">{img(im, "")}<span class="fcard__shade"></span>'
            f'<span class="fcard__tag">{esc(tag)}</span><span class="fcard__title">{esc(title)}</span><span class="fcard__go">{go}</span></a>')


def static_form(fid, subject):
    return f'''<form class="form ad-form" data-static data-mailto="{EMAIL}" data-subject="{esc(subject)}" aria-label="Request a program">
  <div class="ad-form__row">
    <div class="field"><label for="{fid}-name">Name</label><input id="{fid}-name" name="Name" autocomplete="name" required></div>
    <div class="field"><label for="{fid}-org">School or organization</label><input id="{fid}-org" name="School or organization" autocomplete="organization" required></div>
  </div>
  <div class="ad-form__row">
    <div class="field"><label for="{fid}-email">Email address</label><input id="{fid}-email" name="Email" type="email" autocomplete="email" required></div>
    <div class="field"><label for="{fid}-phone">Cell phone</label><input id="{fid}-phone" name="Cell phone" type="tel" autocomplete="tel" required></div>
  </div>
  <div class="field"><label for="{fid}-msg">What are you hoping to book or learn more about?</label><textarea id="{fid}-msg" name="Request" placeholder="Share what you’re hoping to book or learn more about…"></textarea></div>
  <div class="btns"><button class="btn btn--slate" type="submit">Submit request</button><span class="form__note">Or email {a(EMAIL, 'mailto:' + EMAIL, 'link')}</span></div>
  <p class="form__done" role="status">Thank you. Your email app should open with your request ready to send. If it doesn’t, write to {EMAIL}.</p>
</form>'''


TABGO_JS = r'''<script>(function(){
  document.querySelectorAll('[data-tab-go]').forEach(function(l){ l.addEventListener('click', function(e){
    var t = document.getElementById(l.getAttribute('data-tab-go')); if(!t) return;
    e.preventDefault(); t.click(); var box = t.closest('[data-tabs]') || t; box.scrollIntoView({behavior: matchMedia('(prefers-reduced-motion: reduce)').matches ? 'auto' : 'smooth', block:'start'});
    try{ history.replaceState(null, '', '#' + t.id.replace(/^tab-/, '')); }catch(err){}
  }); });
})();</script>'''

CSS = FILM_STRIP_CSS + '''
/* ---------- shared (adults + giving) ---------- */
.ad-h1{font-size:var(--fs-h1); font-stretch:122%; font-weight:900; text-transform:uppercase; line-height:.92; letter-spacing:-.02em; margin:0 0 .35em}
.ad-lede-light{color:rgba(255,255,255,.88)}
.ad-checks{list-style:none; padding:0; margin:0; display:grid; gap:10px}
.ad-checks li{position:relative; padding-left:28px; margin:0}
.ad-checks li::before{content:""; position:absolute; left:2px; top:.5em; width:11px; height:11px; background:var(--teal); transform:rotate(45deg); border-radius:2px}
.band--slate .ad-checks li::before,.band--deep .ad-checks li::before,.band--teal .ad-checks li::before,.ad-dark .ad-checks li::before{background:var(--mint)}
.ad-photo{position:relative; border-radius:var(--r-lg); overflow:hidden; min-height:340px; height:100%; background:var(--slate)}
.ad-photo img{position:absolute; inset:0; width:100%; height:100%; object-fit:cover}
.ad-photo .sticker{position:absolute; left:16px; bottom:18px}
.ad-fallback{border-radius:var(--r-lg); padding:28px 24px; background:var(--mist); border:1px dashed rgba(29,65,78,.35); display:grid; gap:12px; justify-items:start; min-height:220px; align-content:center}
.ad-fallback p{margin:0; font-family:var(--display); font-stretch:106%; font-size:1.15rem}
.ad-card{background:#fff; border:1px solid var(--line); border-radius:var(--r-lg); box-shadow:var(--shadow); padding:clamp(16px,2.4vw,28px)}
.ad-split{display:grid; grid-template-columns:minmax(0,1fr) minmax(0,1fr); gap:clamp(28px,5vw,72px); align-items:center}
.ad-split--top{align-items:start}
.ad-split--stretch{align-items:stretch}
.ad-chipline{display:flex; flex-wrap:wrap; gap:6px; margin:4px 0 14px}
.ad-chipline .chip{white-space:normal}
.ad-mini{font-family:var(--mono); font-size:.7rem; letter-spacing:.1em; text-transform:uppercase; font-weight:600; color:var(--logo-teal); display:block; margin-bottom:6px}
.band--slate .ad-mini,.band--deep .ad-mini,.ad-dark .ad-mini,.ad-say__avoid .ad-mini,.ad-offer--slate .ad-mini{color:var(--mint)}
.ad-hub .eyebrow,.ad-dhero .eyebrow,.ad-fhero .eyebrow{color:var(--mint)}
.ad-chipin .eyebrow{color:var(--logo-teal)}
.band--teal .ad-mini{color:var(--aqua)}
.ad-hl{background:var(--mint); color:var(--slate); border-radius:var(--r-lg); padding:18px 20px}
.ad-hl b{font-family:var(--display); font-stretch:108%; font-size:1.1rem; display:block; margin-bottom:4px}
.ad-hl p{margin:0}
@media (max-width:860px){.ad-split{grid-template-columns:1fr} .ad-photo{min-height:260px}}

/* ---------- adults hub ---------- */
.ad-hub{background:var(--slate); color:#fff; overflow:hidden}
.ad-hub__grid{display:grid; grid-template-columns:minmax(0,1fr) minmax(0,1fr); gap:clamp(28px,5vw,64px); align-items:center; padding-block:clamp(48px,6vw,84px)}
.ad-hub .crumbs{margin-bottom:18px}
.ad-hub .ad-h1{font-size:clamp(2.5rem,4.8vw,4.6rem)}
.phero--logo .crumbs{color:rgba(255,255,255,.9)}
.ad-mosaic{display:grid; grid-template-columns:minmax(0,1.25fr) minmax(0,.75fr); grid-template-rows:1fr 1fr; gap:12px; height:clamp(340px,38vw,520px)}
.ad-mosaic figure{margin:0; position:relative; border-radius:14px; overflow:hidden; background:var(--slate-deep)}
.ad-mosaic figure:first-child{grid-row:1/3}
.ad-mosaic img{width:100%; height:100%; object-fit:cover}
.ad-mosaic .sticker{position:absolute; left:12px; bottom:12px; font-size:.78rem}
.ad-routes{display:grid; grid-template-columns:repeat(3,minmax(0,1fr)); gap:clamp(16px,2vw,26px)}
.ad-route{display:flex; flex-direction:column; border-radius:var(--r-lg); overflow:hidden; background:#fff; border:1px solid var(--line); box-shadow:var(--shadow); min-width:0}
.ad-route__img{display:block; position:relative; aspect-ratio:4/3; overflow:hidden; background:var(--slate)}
.ad-route__img img{position:absolute; inset:0; width:100%; height:100%; object-fit:cover; transition:transform .6s}
.ad-route:hover .ad-route__img img{transform:scale(1.04)}
.ad-route__body{padding:22px 22px 24px; display:flex; flex-direction:column; gap:12px; flex:1}
.ad-route__body h3{margin:0; font-size:clamp(1.45rem,2vw,1.85rem)}
.ad-route__body > p{margin:0; color:var(--ink-soft); font-size:.97rem; line-height:1.5}
.ad-route__links{list-style:none; padding:0; margin:4px 0 0; border-top:1px solid var(--line)}
.ad-route__links li{margin:0}
.ad-route__links a{display:flex; justify-content:space-between; gap:12px; align-items:center; padding:11px 2px; border-bottom:1px solid var(--line); text-decoration:none; font-weight:700; font-size:.95rem; color:var(--logo-teal)}
.ad-route__links a::after{content:"\\2192"; color:var(--teal); transition:transform .2s}
.ad-route__links a[target]::after{content:"\\2197"}
.ad-route__links a:hover{background:var(--mist)}
.ad-route__links a:hover::after{transform:translateX(3px)}
.ad-route__foot{margin-top:auto; padding-top:8px}
@media (max-width:1000px){.ad-routes{grid-template-columns:1fr} .ad-route{display:grid; grid-template-columns:minmax(0,.8fr) minmax(0,1.2fr)} .ad-route__img{aspect-ratio:auto; min-height:260px}}
@media (max-width:860px){.ad-hub__grid{grid-template-columns:1fr} .ad-mosaic{height:320px}}
@media (max-width:620px){.ad-route{display:flex} .ad-route__img{aspect-ratio:16/10}}
.ad-libchips{display:flex; flex-wrap:wrap; gap:8px; margin-top:6px}
.ad-libchips a{font-family:var(--mono); font-size:.75rem; letter-spacing:.06em; text-transform:uppercase; text-decoration:none; padding:7px 11px; border-radius:6px; border:1.5px solid rgba(209,254,255,.35); color:var(--aqua)}
.ad-libchips a:hover{border-color:var(--mint); color:var(--mint)}
.ad-guidecover{position:relative; max-width:400px; margin-inline:auto}
.ad-guidecover img{width:100%; border-radius:8px; box-shadow:0 40px 70px -30px rgba(0,0,0,.6); transform:rotate(-3deg); background:#fff}
.ad-guidecover .sticker{position:absolute; right:-6px; bottom:28px}
.ad-q{margin:22px 0; padding-left:18px; border-left:4px solid var(--mint); font-family:var(--display); font-stretch:104%; font-weight:600; font-size:1.12rem; line-height:1.4}
.ad-q cite{display:block; margin-top:8px; font-style:normal; font-family:var(--mono); font-size:.74rem; letter-spacing:.06em; text-transform:uppercase}

/* ---------- vibe band ---------- */
.ad-vibe{display:grid; grid-template-columns:minmax(0,1.2fr) minmax(0,.8fr); gap:clamp(28px,5vw,72px); align-items:center}
.ad-vibe > div{min-width:0}
.ad-vmark{display:flex; align-items:center; gap:12px; font-family:var(--display); font-weight:900; font-stretch:115%; font-size:1.2rem; color:var(--mint); margin-bottom:16px}
.ad-vmark .daisy{width:38px; height:38px}
.ad-vibe h2{font-size:clamp(2.1rem,4vw,3.5rem); font-stretch:112%; font-weight:900; letter-spacing:-.02em; overflow-wrap:break-word}
@media (max-width:520px){.ad-vibe h2{font-size:1.95rem; font-stretch:110%}}
.ad-vibe .lede{color:#fff}
.ad-vfeats{display:grid; grid-template-columns:1fr 1fr; gap:10px; margin:22px 0 26px}
.ad-vfeats div{background:var(--slate-deep); border-radius:12px; padding:14px 16px}
.ad-vfeats b{display:block; color:var(--mint); font-family:var(--display); font-stretch:108%; font-size:1.05rem}
.ad-vfeats span{font-size:.9rem; color:#fff; line-height:1.4; display:block}
.ad-never{display:inline-block; font-family:var(--display); font-weight:900; font-stretch:115%; font-size:clamp(1.3rem,2.2vw,1.8rem); line-height:1.1; text-transform:uppercase; background:var(--mint); color:var(--slate); padding:.4em .6em .35em; border-radius:6px; transform:rotate(-1.5deg); box-shadow:4px 4px 0 var(--slate); margin:6px 0 20px}
.ad-phonewrap{position:relative}
.ad-phone{position:relative; width:min(300px,74vw); margin-inline:auto; aspect-ratio:390/800; border-radius:44px; border:11px solid #0b1f25; background:#0b1f25; box-shadow:0 50px 90px -30px rgba(0,0,0,.6); overflow:hidden; transform:rotate(-4deg)}
.ad-phone img{width:100%; height:100%; object-fit:cover; object-position:top}
.ad-phonewrap .sticker{position:absolute; z-index:2}
@media (max-width:860px){.ad-vibe{grid-template-columns:1fr} .ad-vfeats{grid-template-columns:1fr}}

/* ---------- parents ---------- */
.ad-pod{display:grid; grid-template-columns:auto minmax(0,1fr) minmax(0,.9fr); gap:clamp(20px,3vw,40px); align-items:center}
.ad-pod__art img{width:150px; height:150px; border-radius:14px; object-fit:cover; box-shadow:0 20px 40px -20px rgba(0,0,0,.7)}
.ad-pod h2{font-size:clamp(1.6rem,2.8vw,2.4rem); margin-bottom:.3em}
.ad-pod p{color:rgba(255,255,255,.85); margin:0 0 .6em}
.ad-pod .audio{background:rgba(255,255,255,.08); border:1px solid var(--line-dark)}
.ad-pod .tag-row{margin-top:12px; gap:16px; font-weight:600; font-size:.92rem}
@media (max-width:960px){.ad-pod{grid-template-columns:auto minmax(0,1fr)} .ad-pod__play{grid-column:1/-1}}
@media (max-width:560px){.ad-pod{grid-template-columns:1fr} .ad-pod__art img{width:110px; height:110px}}
.ad-early{display:grid; grid-template-columns:minmax(0,.42fr) minmax(0,1.58fr); gap:clamp(20px,3vw,40px); align-items:center; background:var(--mist); border-radius:var(--r-lg); padding:clamp(20px,3vw,36px); margin-top:clamp(30px,4vw,52px); border:1px solid var(--line)}
.ad-early__poster button{border:0; padding:0; background:none; cursor:zoom-in; display:block; width:100%}
.ad-early__poster img{width:100%; border-radius:10px; box-shadow:0 24px 40px -24px rgba(22,53,64,.6); transform:rotate(-2deg)}
.ad-early h3{font-size:clamp(1.4rem,2.2vw,1.9rem); margin-bottom:.25em}
.ad-early__items{display:grid; grid-template-columns:repeat(3,minmax(0,1fr)); gap:12px; margin:18px 0}
.ad-early__items > div{background:#fff; border-radius:12px; padding:16px 18px; border:1px solid var(--line)}
.ad-early__items b{display:block; font-family:var(--display); font-stretch:106%; font-size:1.08rem; margin-bottom:6px; color:var(--logo-teal); line-height:1.2}
.ad-early__items p{margin:0; font-size:.92rem; color:var(--ink-soft); line-height:1.5}
@media (max-width:1000px){.ad-early__items{grid-template-columns:1fr}}
@media (max-width:760px){.ad-early{grid-template-columns:1fr} .ad-early__poster{max-width:240px}}
.ad-topic{display:grid; grid-template-columns:minmax(0,1.3fr) minmax(0,.7fr); gap:clamp(20px,3vw,40px); align-items:stretch; background:#fff; border-radius:var(--r-lg); padding:clamp(20px,3vw,36px); border:1px solid var(--line); box-shadow:var(--shadow)}
.ad-topic h3{font-size:clamp(1.35rem,2vw,1.75rem); margin-bottom:.4em}
.ad-subq{font-size:1.15rem; color:var(--logo-teal); margin:1.1em 0 .4em}
.ad-topic .fcard{aspect-ratio:auto; min-height:300px; height:100%}
.ad-topic .fcard__title{font-size:1.9rem}
.ad-signs{display:grid; grid-template-columns:1fr 1fr; gap:14px; margin:6px 0 16px}
.ad-signs > div{border-radius:12px; padding:16px; background:var(--mist)}
.ad-signs > div:last-child{background:var(--slate); color:#fff}
.ad-signs h4{margin:0 0 10px; font-size:1rem}
.ad-signs .chip{white-space:normal; background:#fff}
.ad-signs > div:last-child .chip{background:rgba(255,255,255,.12); color:#fff}
@media (max-width:860px){.ad-topic{grid-template-columns:1fr} .ad-topic .fcard{min-height:240px}}
@media (max-width:560px){.ad-signs{grid-template-columns:1fr}}
.ad-acts{display:grid; grid-template-columns:1fr 1fr; gap:12px; margin:24px 0}
.ad-acts div{background:rgba(255,255,255,.06); border:1px solid var(--line-dark); border-radius:12px; padding:16px 18px}
.ad-acts b{display:block; font-family:var(--display); font-stretch:108%; font-size:1.18rem; color:var(--mint); margin-bottom:4px}
.ad-acts p{margin:0; font-size:.93rem; color:rgba(255,255,255,.84); line-height:1.5}
@media (max-width:560px){.ad-acts{grid-template-columns:1fr}}
.ad-poster{border:0; padding:0; background:none; cursor:zoom-in; display:block; width:100%}
.ad-poster img{border-radius:12px; width:100%; box-shadow:0 30px 60px -30px rgba(0,0,0,.6)}
.ad-poster small{display:block; text-align:left; margin-top:10px; color:var(--aqua); font-size:.82rem; font-weight:600}
.ad-helpcard{background:var(--coral); color:var(--slate); border-radius:var(--r-lg); padding:18px 20px; margin-top:18px; display:grid; gap:8px}
.ad-helpcard b{font-family:var(--display); font-stretch:108%; font-size:1.15rem}
.ad-helpcard span{font-weight:600; font-size:.93rem}
.ad-helpcard .btn{justify-self:start}
.ad-opts{display:grid; grid-template-columns:repeat(4,minmax(0,1fr)); gap:14px}
.ad-opt{border-radius:var(--r-lg); padding:20px; background:var(--mist); border:1px solid var(--line); display:flex; flex-direction:column; gap:6px; min-width:0}
.ad-opt b{font-family:var(--display); font-stretch:110%; font-size:1.3rem; color:var(--logo-teal); line-height:1.1}
.ad-opt p{margin:0; color:var(--ink-soft); font-size:.95rem}
.ad-opt .arrow-link{margin-top:auto; padding-top:8px; font-size:.9rem}
@media (max-width:960px){.ad-opts{grid-template-columns:1fr 1fr}} @media (max-width:520px){.ad-opts{grid-template-columns:1fr}}
.ad-alt{margin-top:clamp(28px,4vw,48px); display:grid; grid-template-columns:minmax(0,1.25fr) minmax(0,.75fr); gap:clamp(20px,4vw,48px); align-items:center; background:var(--aqua); border-radius:var(--r-lg); padding:clamp(22px,3.4vw,44px)}
.ad-alt h3{font-size:clamp(1.5rem,2.4vw,2.1rem)}
.ad-alt .ad-poster img{box-shadow:0 20px 40px -24px rgba(22,53,64,.5); background:#fff}
.ad-alt .ad-poster small{color:var(--ink-soft)}
@media (max-width:860px){.ad-alt{grid-template-columns:1fr} .ad-alt .ad-poster{max-width:360px}}
.ad-steps5{display:grid; grid-template-columns:repeat(5,minmax(0,1fr)); gap:12px}
.ad-steps5 .step{padding:20px 18px}
.ad-steps5 .step h3{font-size:1.08rem; margin-bottom:.4em}
.ad-steps5 .step p{font-size:.9rem}
.ad-steps5 .step__n{font-size:2.2rem}
@media (max-width:1100px){.ad-steps5{grid-template-columns:1fr} .ad-steps5 .step{display:grid; grid-template-columns:56px minmax(0,1fr); column-gap:14px} .ad-steps5 .step__n{grid-row:1/3; margin:0}}
.ad-say{display:grid; grid-template-columns:minmax(0,1.1fr) minmax(0,.9fr); gap:14px; margin-top:16px}
.ad-say > div{border-radius:var(--r-lg); padding:22px 24px}
.ad-say__try{background:#fff; border:1px solid var(--line)}
.ad-say__try p{font-family:var(--display); font-stretch:104%; font-weight:600; font-size:1.08rem; line-height:1.45; margin:0 0 .8em}
.ad-say__avoid{background:var(--slate); color:#fff}
.ad-say__avoid ul{list-style:none; padding:0; margin:0; display:grid; gap:8px}
.ad-say__avoid li{margin:0; padding:9px 12px; border-radius:8px; background:rgba(255,255,255,.07); text-decoration:line-through; text-decoration-color:rgba(254,113,113,.9); text-decoration-thickness:2px; color:rgba(255,255,255,.88)}
@media (max-width:760px){.ad-say{grid-template-columns:1fr}}
.ad-starters{display:grid; grid-template-columns:1fr 1fr; gap:14px}
.ad-starter{background:#fff; border-radius:var(--r-lg); padding:20px 22px; border:1px solid var(--line)}
.ad-starter h3{font-size:1.15rem; margin-bottom:.6em}
.ad-starter ul{list-style:none; padding:0; margin:0; display:grid; gap:8px}
.ad-starter li{margin:0; padding:10px 14px; background:var(--mist); border-radius:10px; font-weight:600; font-size:.95rem; line-height:1.45}
@media (max-width:760px){.ad-starters{grid-template-columns:1fr}}
.ad-reminder{margin-top:16px; display:flex; gap:16px 28px; align-items:center; justify-content:space-between; flex-wrap:wrap; background:var(--slate); color:#fff; border-radius:var(--r-lg); padding:18px 22px}
.ad-reminder p{margin:0; font-family:var(--display); font-stretch:104%; font-weight:700; font-size:1.1rem; flex:1 1 420px; min-width:0}
.ad-tabs2{display:flex; flex-wrap:wrap; gap:8px; margin-bottom:22px}

/* ---------- educators ---------- */
.ad-ladder{display:grid; grid-template-columns:repeat(4,minmax(0,1fr)); gap:10px; align-items:end; margin-bottom:18px}
.ad-rung{font:inherit; text-align:left; border:2px solid var(--line); background:#fff; color:var(--slate); border-radius:14px; padding:14px 16px 20px; cursor:pointer; display:flex; flex-direction:column; justify-content:flex-end; gap:4px; position:relative; overflow:hidden; transition:border-color .2s, background .2s, transform .2s}
.ad-rung:nth-child(1){min-height:104px} .ad-rung:nth-child(2){min-height:136px} .ad-rung:nth-child(3){min-height:168px} .ad-rung:nth-child(4){min-height:200px}
.ad-rung small{font-family:var(--mono); font-size:.68rem; letter-spacing:.08em; text-transform:uppercase; color:var(--logo-teal); line-height:1.3}
.ad-rung span{font-family:var(--display); font-weight:800; font-stretch:110%; font-size:clamp(1.05rem,1.6vw,1.35rem); line-height:1.1}
.ad-rung::after{content:""; position:absolute; left:0; right:0; bottom:0; height:7px; background:var(--aqua)}
.ad-rung:hover{border-color:var(--teal); transform:translateY(-2px)}
.ad-rung[aria-selected="true"]{background:var(--slate); color:#fff; border-color:var(--slate)}
.ad-rung[aria-selected="true"] small{color:var(--mint)}
.ad-rung[aria-selected="true"]::after{background:var(--mint)}
.ad-axis{display:flex; justify-content:space-between; gap:12px; font-family:var(--mono); font-size:.7rem; letter-spacing:.08em; text-transform:uppercase; color:var(--ink-soft); margin:0 0 22px; padding-top:10px; border-top:2px solid var(--line); position:relative}
.ad-axis::after{content:""; position:absolute; right:-2px; top:-7px; width:12px; height:12px; border-top:2px solid var(--line); border-right:2px solid var(--line); transform:rotate(45deg)}
@media (max-width:760px){.ad-ladder{grid-template-columns:1fr 1fr} .ad-rung:nth-child(n){min-height:96px}}
.ad-level{display:grid; grid-template-columns:minmax(0,.9fr) minmax(0,1.1fr); gap:clamp(24px,4vw,56px); align-items:center; background:var(--mist); border-radius:var(--r-lg); padding:clamp(20px,3.4vw,44px); border:1px solid var(--line)}
.ad-level h3{font-size:clamp(1.6rem,2.6vw,2.3rem); margin-bottom:.35em}
.ad-level > div{min-width:0}
@media (max-width:900px){.ad-level{grid-template-columns:1fr}}
.ad-covers{display:grid; grid-template-columns:repeat(4,minmax(0,1fr)); gap:12px}
.ad-covers a{display:block; border-radius:8px; overflow:hidden; box-shadow:0 14px 30px -18px rgba(22,53,64,.7); transition:transform .25s; aspect-ratio:587/917; background:var(--slate); position:relative; color:#fff; text-decoration:none}
.ad-covers img{width:100%; height:100%; object-fit:cover}
.ad-covers a:hover{transform:translateY(-5px) rotate(-1.5deg)}
.ad-covers .ad-rr span{position:absolute; inset:auto 0 0 0; padding:12px 10px; background:linear-gradient(transparent, rgba(8,24,30,.92)); font-family:var(--display); font-weight:800; font-stretch:104%; font-size:.95rem; line-height:1.15}
.ad-covers .ad-rr img{filter:saturate(.9)}
.ad-pgrid{display:grid; grid-template-columns:repeat(3,minmax(0,1fr)); gap:12px}
.ad-pgrid button{border:0; padding:8px; background:#fff; border-radius:12px; cursor:zoom-in; aspect-ratio:3/4; box-shadow:0 14px 30px -20px rgba(22,53,64,.6); transition:transform .25s}
.ad-pgrid button:hover{transform:translateY(-4px)}
.ad-pgrid img{width:100%; height:100%; object-fit:contain; border-radius:6px}
.ad-level__photo{position:relative; border-radius:14px; overflow:hidden; aspect-ratio:4/3}
.ad-level__photo img{width:100%; height:100%; object-fit:cover}
.ad-level__photo .sticker{position:absolute; left:14px; bottom:14px}
.ad-ringwrap{display:grid; grid-template-columns:minmax(0,.9fr) minmax(0,1.1fr); gap:18px; align-items:center}
.ad-ringwrap svg{width:100%; max-width:300px; display:block; margin-inline:auto; overflow:visible}
.ad-ringwrap ol{margin:0; padding-left:1.4em; display:grid; gap:4px; font-size:.92rem}
.ad-ringwrap li{margin:0}
.ad-ringwrap li a{font-weight:700; color:var(--logo-teal); text-decoration:none}
.ad-ringwrap li a:hover{text-decoration:underline}
@media (max-width:560px){.ad-ringwrap{grid-template-columns:1fr} .ad-covers{grid-template-columns:repeat(3,minmax(0,1fr))} .ad-covers a:nth-child(n+7){display:none} .ad-pgrid{grid-template-columns:1fr 1fr} .ad-pgrid button:nth-child(n+5){display:none}}
.ad-ideas{display:flex; flex-wrap:wrap; gap:8px; margin:6px 0 24px}
.ad-ideas span{background:var(--slate-deep); color:#fff; border-radius:999px; padding:8px 14px; font-weight:600; font-size:.92rem}
.ad-form__row{display:grid; grid-template-columns:1fr 1fr; gap:14px}
@media (max-width:560px){.ad-form__row{grid-template-columns:1fr}}

/* ---------- college ---------- */
.ad-dos{display:grid; grid-template-columns:repeat(3,minmax(0,1fr)); gap:10px; margin:20px 0}
.ad-dos div{border-radius:12px; padding:16px; background:var(--aqua); font-family:var(--display); font-stretch:106%; font-weight:800; font-size:1.05rem; line-height:1.2; color:var(--logo-teal)}
@media (max-width:620px){.ad-dos{grid-template-columns:1fr}}
.ad-mail{display:flex; flex-wrap:wrap; gap:12px; align-items:center; padding:16px 18px; border-radius:var(--r-lg); background:var(--slate); color:#fff; margin-top:22px}
.ad-mail b{font-family:var(--display); font-stretch:108%; font-size:1.15rem; flex:1 1 220px}
.ad-figure{margin:0}
.ad-figure img{border-radius:var(--r-lg); width:100%; box-shadow:var(--shadow)}
.ad-figure figcaption{margin-top:12px; font-family:var(--display); font-stretch:104%; font-weight:700; font-size:1.2rem; line-height:1.35; color:var(--logo-teal); border-left:4px solid var(--mint); padding-left:14px}

/* ---------- request ---------- */
.ad-offers{display:grid; grid-template-columns:1fr 1fr; gap:clamp(16px,2vw,26px); align-items:stretch}
.ad-offer{border-radius:var(--r-lg); overflow:hidden; display:flex; flex-direction:column; min-width:0}
.ad-offer--aqua{background:var(--aqua); color:var(--slate)}
.ad-offer--slate{background:var(--slate); color:#fff}
.ad-offer__media{aspect-ratio:12/5; overflow:hidden; position:relative}
.ad-offer__media img{width:100%; height:100%; object-fit:cover}
.ad-offer__media .sticker{position:absolute; left:16px; bottom:16px}
.ad-offer__body{padding:clamp(20px,3vw,34px); display:flex; flex-direction:column; gap:10px; flex:1}
.ad-offer__body h3{font-size:clamp(1.5rem,2.4vw,2.1rem); margin:0}
.ad-offer__body p{margin:0}
.ad-offer--slate .ad-offer__body p{color:rgba(255,255,255,.85)}
.ad-meta{display:grid; grid-template-columns:auto minmax(0,1fr); gap:8px 14px; align-items:center; margin:6px 0 4px; padding:14px 0; border-block:1px solid var(--line)}
.ad-offer--slate .ad-meta{border-color:var(--line-dark)}
.ad-meta dt{font-family:var(--mono); font-size:.68rem; letter-spacing:.1em; text-transform:uppercase; font-weight:600; color:var(--logo-teal)}
.ad-offer--slate .ad-meta dt{color:var(--mint)}
.ad-meta dd{margin:0; display:flex; flex-wrap:wrap; gap:6px}
.ad-meta .chip{white-space:normal}
.ad-offer--aqua .chip{background:#fff}
.ad-comps{list-style:none; padding:0; margin:6px 0 0; display:grid; gap:6px}
.ad-comps li{margin:0}
.ad-comps a{display:flex; justify-content:space-between; gap:12px; align-items:center; padding:11px 14px; border-radius:10px; background:rgba(255,255,255,.07); border:1px solid var(--line-dark); text-decoration:none; color:#fff; font-weight:700; font-size:.95rem}
.ad-comps a::after{content:"\\2192"; color:var(--mint)}
.ad-comps a:hover{background:rgba(21,255,200,.12); border-color:var(--mint)}
.ad-offer__foot{margin-top:auto; padding-top:10px}
@media (max-width:900px){.ad-offers{grid-template-columns:1fr} .ad-offer__media{aspect-ratio:16/9}}
.ad-factors{display:grid; grid-template-columns:repeat(3,minmax(0,1fr)); gap:12px; margin:24px 0 26px}
.ad-factors div{background:#fff; border-radius:var(--r-lg); padding:20px 22px; border:2px solid var(--slate); box-shadow:4px 4px 0 var(--slate)}
.ad-factors small{display:block; font-family:var(--mono); font-size:.68rem; letter-spacing:.1em; text-transform:uppercase; font-weight:600; color:var(--logo-teal)}
.ad-factors b{display:block; font-family:var(--display); font-weight:900; font-stretch:115%; font-size:clamp(1.3rem,2.2vw,1.8rem); line-height:1.05; margin-top:6px}
@media (max-width:760px){.ad-factors{grid-template-columns:1fr}}
.ad-startpanel{display:grid; grid-template-columns:minmax(0,.75fr) minmax(0,1.25fr); gap:clamp(24px,4vw,56px); align-items:start}
@media (max-width:900px){.ad-startpanel{grid-template-columns:1fr} .ad-startpanel .ad-photo{display:none}}

/* ---------- donate ---------- */
.ad-dhero{background:var(--slate); color:#fff; overflow:hidden; position:relative}
.ad-dhero__grid{display:grid; grid-template-columns:minmax(0,1.1fr) minmax(0,.9fr); gap:clamp(28px,5vw,64px); align-items:center; padding-block:clamp(48px,6vw,88px)}
.ad-dhero .ad-h1{font-size:clamp(2.4rem,4.6vw,4.4rem)}
.ad-dhero__photo{position:relative}
.ad-dhero__photo img{border-radius:var(--r-lg); width:100%; aspect-ratio:5/4; object-fit:cover; box-shadow:0 40px 70px -30px rgba(0,0,0,.65)}
.ad-dhero__photo .sticker{position:absolute}
@media (max-width:860px){.ad-dhero__grid{grid-template-columns:1fr} .ad-dhero__photo{max-width:560px}}
.ad-give{display:grid; grid-template-columns:minmax(0,.85fr) minmax(0,1.15fr); grid-template-areas:"head form" "rest form"; grid-template-rows:auto 1fr; column-gap:clamp(24px,4vw,56px); row-gap:18px; align-items:start}
.ad-give__head{grid-area:head} .ad-give__form{grid-area:form; min-width:0} .ad-give__rest{grid-area:rest; min-width:0}
.ad-give__head h2{font-size:clamp(1.9rem,3.4vw,3rem)}
.ad-fund{margin:16px 0 22px}
.ad-fund li{font-weight:600}
.ad-bigstat{display:flex; gap:16px; align-items:center; padding:16px 18px; border-radius:var(--r-lg); background:var(--aqua); margin-bottom:16px}
.ad-bigstat b{font-family:var(--display); font-weight:900; font-stretch:115%; font-size:clamp(2.2rem,3.6vw,3.2rem); line-height:.9; color:var(--logo-teal); flex:none}
.ad-bigstat span{font-weight:600; line-height:1.35}
.ad-zeffy{border-radius:var(--r-lg); border:1px solid var(--line); box-shadow:var(--shadow); background:#fff; padding:10px; min-width:0}
.ad-zeffy .ad-fallback{min-height:340px}
.ad-fallback--tall{min-height:620px!important; justify-items:center; text-align:center}
.ad-fallback--tall::before{content:""; width:76px; height:76px; background:var(--teal); -webkit-mask:url(assets/img/daisy.svg) center/contain no-repeat; mask:url(assets/img/daisy.svg) center/contain no-repeat; margin-bottom:6px}
.ad-fallback--tall p{max-width:24ch; font-size:1.4rem}
.ad-fb-alt{margin-top:18px; padding-top:16px; border-top:1px solid var(--line)}
.ad-fb-alt p{font-family:var(--body)!important; font-size:.95rem!important; max-width:none!important}
.ad-small{font-size:.9rem; color:var(--ink-soft); margin:12px 4px 0}
.ad-trust{display:flex; gap:14px; align-items:center; margin-top:16px; flex-wrap:wrap}
.ad-trust img{width:64px; height:64px; flex:none}
.ad-trust span{font-size:.88rem; line-height:1.45; flex:1 1 200px; min-width:0}
@media (max-width:900px){.ad-give{grid-template-columns:1fr; grid-template-areas:"head" "form" "rest"; row-gap:24px} .ad-fallback--tall{min-height:420px!important}}
.ad-story{display:grid; grid-template-columns:minmax(0,.9fr) minmax(0,1.1fr); gap:clamp(24px,5vw,72px); align-items:center}
.ad-story img{border-radius:var(--r-lg); width:100%; aspect-ratio:3/2; object-fit:cover}
@media (max-width:860px){.ad-story{grid-template-columns:1fr}}
.ad-ways{display:grid; grid-template-columns:minmax(0,.8fr) minmax(0,1.2fr); gap:clamp(16px,2.4vw,32px); align-items:start}
.ad-ways__list{display:grid; gap:8px; align-content:start}
.ad-way{font:inherit; text-align:left; padding:14px 16px; border-radius:12px; border:2px solid var(--line); background:#fff; color:var(--slate); cursor:pointer; display:grid; gap:2px; transition:border-color .2s}
.ad-way b{font-family:var(--display); font-stretch:108%; font-size:1.12rem; line-height:1.2}
.ad-way small{color:var(--ink-soft); font-size:.86rem; line-height:1.4}
.ad-way:hover{border-color:var(--teal)}
.ad-way[aria-selected="true"]{background:var(--slate); color:#fff; border-color:var(--slate)}
.ad-way[aria-selected="true"] small{color:var(--aqua)}
.ad-wpanel{background:var(--mist); border-radius:var(--r-lg); padding:clamp(22px,3.4vw,44px); border:1px solid var(--line)}
.ad-wpanel h3{font-size:clamp(1.6rem,2.6vw,2.3rem)}
.ad-wpanel ol{padding-left:1.3em; display:grid; gap:8px; margin:0 0 1.2em}
.ad-addr{font-family:var(--mono); font-weight:600; font-size:1.05rem; line-height:1.55; background:#fff; border:1px solid var(--line); border-radius:12px; padding:16px 18px; margin:0 0 14px; display:inline-block}
@media (max-width:860px){.ad-ways{grid-template-columns:1fr} .ad-ways__list{grid-template-columns:1fr 1fr}}
@media (max-width:560px){.ad-way small{display:none} .ad-way{padding:12px} .ad-way b{font-size:1rem}}
.ad-strip{display:flex; flex-wrap:wrap; gap:16px 32px; align-items:center; justify-content:space-between}
.ad-strip__txt{flex:1 1 420px; min-width:0}
.ad-strip__txt b{display:block; font-family:var(--display); font-stretch:108%; font-size:clamp(1.25rem,2vw,1.6rem); line-height:1.15}
.ad-strip__txt p{margin:4px 0 0; font-weight:500}

/* ---------- chip in ---------- */
.ad-chipin{background:var(--aqua); color:var(--slate)}
.ad-chipin .wrap{padding-block:clamp(44px,6vw,84px)}
.ad-chipin h1{font-size:clamp(2.2rem,4.6vw,4.1rem); font-stretch:115%; font-weight:900; letter-spacing:-.02em; line-height:.98; margin:0 0 .4em}
.ad-chipin .crumbs{color:var(--ink-soft)} .ad-chipin .crumbs a{color:var(--logo-teal)}
.ad-impact{list-style:none; padding:0; margin:18px 0 20px; display:grid; gap:10px}
.ad-impact li{margin:0; background:#fff; border-radius:12px; padding:14px 16px 14px 52px; position:relative; border:1px solid var(--line); line-height:1.45}
.ad-impact li::before{content:""; position:absolute; left:16px; top:14px; width:22px; height:22px; border-radius:50%; background:var(--mint) url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 24 24'%3E%3Cpath d='M6 12.5l4 4 8-9' fill='none' stroke='%231d414e' stroke-width='3' stroke-linecap='round' stroke-linejoin='round'/%3E%3C/svg%3E") center/14px no-repeat}
.ad-impact strong{color:var(--logo-teal)}
.ad-fill{display:flex; flex-direction:column; gap:14px; align-self:stretch; min-width:0}
.ad-fill > .ad-zeffy{flex:1; display:flex; flex-direction:column}
.ad-fill .embed{flex:1; display:flex; flex-direction:column}
.ad-fill .embed > *{flex:1}
.ad-fill .ad-fallback{justify-items:center; text-align:center}
.ad-fill .ad-fallback::before{content:""; width:64px; height:64px; background:var(--teal); -webkit-mask:url(assets/img/daisy.svg) center/contain no-repeat; mask:url(assets/img/daisy.svg) center/contain no-repeat}
.ad-fill .ad-raised .embed > *{flex:none}
.ad-fill .ad-raised .ad-fallback::before{display:none}
.ad-fill .ad-raised .ad-fallback{min-height:0; padding:18px; justify-items:start; text-align:left}
.ad-raised .note{display:flex; flex-wrap:wrap; gap:12px 20px; align-items:center; justify-content:space-between}
.ad-raised .note p{margin:0}

/* ---------- fundraise ---------- */
.ad-fhero{background:var(--slate); color:#fff; overflow:hidden}
.ad-fhero__grid{display:grid; grid-template-columns:minmax(0,1.05fr) minmax(0,.95fr); gap:clamp(28px,5vw,64px); align-items:center; padding-block:clamp(48px,6vw,84px)}
.ad-pols{position:relative; height:clamp(320px,32vw,440px)}
.ad-pol{position:absolute; width:44%; background:#fff; padding:10px 10px 40px; border-radius:4px; box-shadow:0 30px 50px -20px rgba(0,0,0,.6); text-decoration:none; color:var(--slate); transition:transform .3s}
.ad-pol img{width:100%; aspect-ratio:4/5; object-fit:cover; background:var(--aqua)}
.ad-pol span{position:absolute; left:0; right:0; bottom:10px; text-align:center; font-family:var(--display); font-weight:800; font-stretch:110%; font-size:1.1rem}
.ad-pol:nth-child(1){left:0; top:10%; transform:rotate(-6deg)}
.ad-pol:nth-child(2){left:28%; top:0; transform:rotate(3deg); z-index:2}
.ad-pol:nth-child(3){right:0; top:16%; transform:rotate(-2deg)}
.ad-pol:hover{transform:rotate(0) translateY(-6px); z-index:3}
.ad-pol--contain img{object-fit:contain; background:var(--teal)}
.ad-pol--v img{object-position:50% 30%}
.ad-ptab img[src*="copy-of-education"]{object-position:48% 26%}
@media (max-width:860px){.ad-fhero__grid{grid-template-columns:1fr} .ad-pols{height:300px; max-width:520px}}
.ad-ptabs{display:flex; flex-wrap:wrap; gap:10px; margin-bottom:24px}
.ad-ptab{display:flex; align-items:center; gap:10px; font:inherit; font-family:var(--display); font-weight:800; font-stretch:106%; font-size:1.05rem; padding:6px 18px 6px 6px; border-radius:999px; border:2px solid var(--line); background:#fff; color:var(--slate); cursor:pointer}
.ad-ptab img{width:40px; height:40px; border-radius:50%; object-fit:cover; background:var(--aqua)}
.ad-ptab:hover{border-color:var(--teal)}
.ad-ptab[aria-selected="true"]{background:var(--slate); color:#fff; border-color:var(--slate)}
.ad-fr{display:grid; grid-template-columns:minmax(0,1fr) minmax(0,1fr); gap:clamp(24px,4vw,56px); align-items:stretch}
.ad-fr h3{font-size:clamp(1.6rem,2.6vw,2.3rem); margin-bottom:.4em}
.ad-fr__photo{border-radius:var(--r-lg); overflow:hidden; aspect-ratio:4/3; background:var(--slate); margin-bottom:20px}
.ad-fr__photo img{width:100%; height:100%; object-fit:cover}
.ad-fr__photo--contain img{object-fit:contain}
.ad-venmo{margin-top:18px; padding:18px 20px; border-radius:var(--r-lg); background:var(--mist); border:1px solid var(--line)}
.ad-venmo p{margin:0 0 12px; font-size:.95rem}
.ad-venmo .btns{gap:10px}
.ad-raised h4{font-family:var(--mono); font-size:.72rem; letter-spacing:.12em; text-transform:uppercase; color:var(--logo-teal); margin:0 0 8px}
@media (max-width:900px){.ad-fr{grid-template-columns:1fr}}
.ad-acts4{display:grid; grid-template-columns:repeat(4,minmax(0,1fr)); gap:12px}
.ad-acts4 a{display:flex; flex-direction:column; gap:8px; padding:20px; border-radius:var(--r-lg); background:#fff; color:var(--slate); text-decoration:none; border:1px solid var(--line); transition:transform .2s, box-shadow .2s}
.ad-acts4 a:hover{transform:translateY(-3px); box-shadow:var(--shadow)}
.ad-acts4 b{font-family:var(--display); font-stretch:108%; font-size:1.15rem; line-height:1.2}
.ad-acts4 span{color:var(--ink-soft); font-size:.92rem}
.ad-acts4 i{font-style:normal; margin-top:auto; font-weight:700; color:var(--logo-teal); font-size:.9rem}
@media (max-width:960px){.ad-acts4{grid-template-columns:1fr 1fr}} @media (max-width:520px){.ad-acts4{grid-template-columns:1fr}}
.ad-moments{display:grid; grid-template-columns:repeat(2,minmax(0,1fr)); gap:10px; margin:18px 0 24px; max-width:520px}
.ad-moments span{font-family:var(--display); font-weight:900; font-stretch:115%; text-transform:uppercase; font-size:clamp(.88rem,1.3vw,1.1rem); padding:.5em .6em .45em; text-align:center; border:2.5px solid var(--slate); border-radius:8px; background:#fff; box-shadow:3px 3px 0 var(--slate)}
.ad-moments span{display:flex; align-items:center; justify-content:center; white-space:nowrap}
@media (max-width:520px){.ad-moments span{font-size:.78rem; font-stretch:105%}}
.ad-moments span:nth-child(2){background:var(--aqua)} .ad-moments span:nth-child(3){background:var(--mint)}
'''

HEAD = f'<style>{CSS}</style>'


# =====================================================================
# adults.html
# =====================================================================
def adults():
    routes = [
        ('us-reis-parent', 'A parent and teenager talking at home', 'For families', 'Parents & caregivers',
         'Start conversations about consent and boundaries early, know what to do if your child tells you something happened, and understand reporting and alternative justice options.',
         [('Early conversations about consent', 'parents.html#early'), ('If your child tells you something happened', 'parents.html#support'), ('Sharing Vibe Check with your child', 'parents.html#vibe-check')],
         'parents.html', 'Parents & caregivers'),
        ('img-3947', 'A SafeBAE session in a high school classroom', 'For teachers & staff', 'Educators',
         'Educators are asked to do a great deal in any given day, so SafeBAE offers tools for every level of use, from one class discussion to a whole-school model.',
         [('Films and teaching guides', 'library.html#guides'), ('Classroom posters', 'posters.html'), ('Consent Curriculum', 'consent-curriculum.html')],
         'educators.html', 'Educators'),
        ('us-colah-campus', 'Students walking across a college campus', 'For college students', 'College students',
         'Mentor high school students, start a SafeBAE club on your own campus, and become a Certified Peer Educator.',
         [('Become a college mentor', 'college.html#mentor'), ('Start a campus club', 'clubs.html'), ('Certified Peer Educator Training', 'peer-educator.html')],
         'college.html', 'College students'),
    ]
    rc = ''
    for im, alt, tag, h, p, links, href, lbl in routes:
        lk = ''.join(f'<li>{a(esc(t), u)}</li>' for t, u in links)
        rc += f'''<article class="ad-route"><a class="ad-route__img" href="{href}" tabindex="-1" aria-hidden="true">{img(im, '')}</a>
  <div class="ad-route__body"><span class="ad-mini">{esc(tag)}</span><h3>{a(esc(h), href, attrs=' style="text-decoration:none;color:inherit"')}</h3><p>{esc(p)}</p>
  <ul class="ad-route__links">{lk}</ul><div class="ad-route__foot">{btn('Go to ' + lbl, href, 'slate', 'sm', arrow=True)}</div></div></article>'''

    tools = [
        ('Request a program', 'Assemblies, events and sliding-scale pricing for school partners', 'request-a-program.html', ['Sliding scale']),
        ('SafeBAE 360° Schools', 'Six components, adapted to your school', '360-schools.html', ['Whole school']),
        ('Consent Curriculum', '15 modules aligned with the National Health Education Standards', 'consent-curriculum.html', ['NHES']),
        ('Faculty & Staff Training', 'Trauma-informed professional development', 'professional-development.html', None),
        ('Policy Reform Guide', 'For administrators and districts', 'policy-reform-guide.html', None),
        ('Accountability Training', 'For students who have caused harm', 'accountability-training.html', None),
    ]
    trows = ''.join(row(t, d, h, m) for t, d, h, m in tools)
    strip = '<div class="fstrip">' + ''.join(fcard(k, 'Four lessons &rarr;' if k == 'rrcr' else 'Film + guide &rarr;') for _h, k, *_r in FILMS) + '</div>'

    body = f'''
<section class="ad-hub">
  <div class="wrap ad-hub__grid">
    <div>
      <nav class="crumbs" aria-label="Breadcrumb"><a href="index.html">Home</a><span>/</span><span>For adults</span></nav>
      <p class="eyebrow">Parents &middot; caregivers &middot; educators &middot; college students</p>
      <h1 class="ad-h1">For adults who support young people</h1>
      <p class="lede ad-lede-light">Parents, caregivers and trusted adults play a critical role in shaping how young people understand safety, consent and relationships. SafeBAE’s work is youth-led, and prevention is a whole-community commitment. There’s more than one way to be part of it.</p>
      <div class="btns">{btn('Bring SafeBAE to your school', 'request-a-program.html', 'mint', arrow=True)}{btn('Adult guide to Vibe Check', GUIDE_PDF, 'ghost')}</div>
    </div>
    <div class="ad-mosaic">
      <figure>{img('us-sometale-parent', 'A mother and her teenage son walking together', loading='eager')}<span class="sticker">Parents</span></figure>
      <figure>{img('img-2395', 'SafeBAE educators leading a classroom presentation', loading='eager')}<span class="sticker sticker--aqua sticker--r">Educators</span></figure>
      <figure>{img('1-7c1d4302-803a-4154-b18a-3a64432a6c76', 'A group of college-age SafeBAE supporters', loading='eager')}<span class="sticker sticker--white">College</span></figure>
    </div>
  </div>
</section>

<section class="band band--paper">
  <div class="wrap">
    <div class="section-head"><div><p class="eyebrow">Start here</p><h2>Find what fits your role</h2></div></div>
    <div class="ad-routes">{rc}</div>
  </div>
</section>

<section class="band band--slate">
  <div class="wrap ad-split ad-split--top">
    <div>
      <p class="eyebrow">For schools &amp; communities</p>
      <h2>Bring SafeBAE to your school, campus or community</h2>
      <p class="lede ad-lede-light">Many school partners start with an assembly or awareness event, always co-presented with youth leaders. SafeBAE 360° Schools builds lasting prevention infrastructure across the whole school community, and every component can start small and grow over time.</p>
      <p class="muted">Pricing is on a flexible sliding scale, because cost should never be a barrier to prevention.</p>
      <div class="btns" style="margin-top:22px">{btn('Request a program', 'request-a-program.html', 'mint', arrow=True)}{btn('Explore 360° Schools', '360-schools.html', 'ghost')}</div>
    </div>
    <div class="rows">{trows}</div>
  </div>
</section>

<section class="band band--deep">
  <div class="wrap">
    <div class="section-head"><div><p class="eyebrow">The Library</p><h2>Youth-made films with ready-to-teach guides</h2>
      <p class="lede muted">Every film is paired with a teaching guide. Use them in a classroom, a club meeting or at home.</p></div>{btn('Open the Library', 'library.html', 'mint', arrow=True)}</div>
  </div>
  <div class="wrap wrap--wide">{strip}</div>
  <div class="wrap"><div class="ad-libchips"><a href="library.html#films">Films &amp; videos</a><a href="library.html#guides">Teaching guides</a><a href="library.html#podcasts">Podcasts</a><a href="posters.html">Posters</a><a href="film-race-rape-culture-resistance.html">Race, Rape Culture &amp; Resistance</a></div></div>
</section>

<section class="band band--teal" id="vibe-check">
  <div class="wrap ad-vibe">
    <div>
      <div class="ad-vmark"><span class="daisy"></span>Vibe Check by SafeBAE</div>
      <h2>Check Their Vibe: an adults’ guide to Vibe Check</h2>
      <p class="lede">Vibe Check is a free, private, self-guided reflection tool for young people navigating moments of sexual uncertainty. The guide helps you introduce it thoughtfully, follow up with care, and understand what it actually contains.</p>
      <p style="color:#fff">Vibe Check is designed to be used privately and voluntarily. It should never be assigned. No accounts, no names, and nothing is stored.</p>
      <blockquote class="ad-q">“As the founding Executive Director of SafeBAE and a mom, this might be the most important tool we’ve developed.”<cite>Shael Norris</cite></blockquote>
      <div class="btns">{btn('Read the adult guide (PDF)', GUIDE_PDF, 'mint')}{btn('Open Vibe Check', 'https://checkyourvibe.org/', 'white')}{btn('How Vibe Check works', 'vibe-check.html', 'ghost', arrow=True)}</div>
    </div>
    <div class="ad-guidecover">{img('guide-vibe-check', 'Cover of Check Their Vibe: An Adults’ Guide to Vibe Check')}<span class="sticker sticker--white sticker--r">For parents &amp; adult allies</span></div>
  </div>
</section>
{give_band('SafeBAE is a survivor-founded, youth-led organization working to end sexual violence before it starts. Your support helps us train peer educators, expand our school-based programming, and build a national network of youth leaders committed to prevention.')}
'''
    page('adults.html', 'For Adults · SafeBAE', 'Tools for parents, caregivers, educators and college students who support young people: conversations, classroom resources, mentoring and programs for schools.',
         body, active='adults', fonts=film_font_link(), head_extra=HEAD)


# =====================================================================
# parents.html
# =====================================================================
def parents():
    pod = next(p for p in PODCASTS if p[0] == '4jjztQt08zjUR9guFgJ56x')
    early_items = [
        ('Offer alternatives to hugs', 'Encourage toddlers to greet adults in ways that feel comfortable to them: waving, blowing a kiss, or saying hello. This builds a lifelong foundation of bodily autonomy.'),
        ('Normalize consent in classrooms', 'Teachers can give elementary students options for how they’d like to be greeted, showing that personal boundaries matter everywhere.'),
        ('Use accurate words for anatomy', 'Avoid “cute” or made-up words. Real terms help children understand there is no shame in their bodies and equip them to clearly communicate if something inappropriate happens.'),
    ]
    ei = ''.join(f'<div><b>{esc(t)}</b><p>{esc(d)}</p></div>' for t, d in early_items)

    # topics to talk through together (answers are SafeBAE's FAQ text)
    c1, l1 = faq('What is consent?'); c2, _ = faq('Can someone give consent if they’re drunk or high?')
    n1, l3 = faq('What are the risks of sending nudes?')
    b1, l4 = faq('What is bystander intervention?')
    healthy = ['Open communication', 'Mutual respect', 'Trust', 'Shared decisions', 'Feeling safe', 'Healthy boundaries', 'Respectful disagreements', 'Enjoying time apart', 'Inspiring each other']
    warning = ['Guilt trips', 'Isolating you from family and friends', 'Unreasonable jealousy', 'Constant put-downs', '“If you love me, you will…”', 'Threats', 'Intimidation', 'Manipulation', 'Gaslighting', 'Love-bombing']
    topics = [
        ('consent', 'Consent', 'What is consent?', f'<p>{esc(c1)}</p><h4 class="ad-subq">Can someone give consent if they’re drunk or high?</h4><p>{esc(c2)}</p>', 'faq.html#q-what-is-consent', 'rc'),
        ('relationships', 'Healthy vs. unhealthy relationships', 'What does a healthy relationship look like, and what are the warning signs?',
         f'''<p>In a healthy relationship, partners respect each other and stay independent people. Look at the whole relationship, not one good or bad moment.</p>
         <div class="ad-signs"><div><h4>Healthy signs</h4><div class="chips">{''.join(f'<span class="chip">{esc(x)}</span>' for x in healthy)}</div></div>
         <div><h4>Warning signs</h4><div class="chips">{''.join(f'<span class="chip">{esc(x)}</span>' for x in warning)}</div></div></div>
         <p class="muted">Abuse can be physical, sexual, psychological, emotional, or financial. One out of three teens will be in an abusive relationship.</p>''', 'faq.html#q-what-are-the-signs-of-an-unhealthy-or-abusive-relationship', 'red'),
        ('nudes', 'Nudes & online safety', 'What are the risks of sending nudes?', f'<p>{esc(n1)}</p>', 'faq.html#q-what-are-the-risks-of-sending-nudes', 'know'),
        ('bystander', 'Speaking up', 'What is bystander intervention?', f'<p>{esc(b1)}</p>', 'faq.html#q-what-is-bystander-intervention', 'bae'),
    ]
    ttabs = ''.join(f'<button class="tab" role="tab" id="tt-{k}" aria-controls="tp-{k}" aria-selected="{str(i==0).lower()}" tabindex="{0 if i==0 else -1}">{esc(lbl)}</button>' for i, (k, lbl, *_r) in enumerate(topics))
    tpanels = ''.join(f'''<div role="tabpanel" id="tp-{k}" aria-labelledby="tt-{k}"{'' if i==0 else ' hidden'}><div class="ad-topic">
      <div><span class="ad-mini">From the SafeBAE FAQ</span><h3>{esc(q)}</h3>{ans}<p style="margin-top:14px">{a('Read the full answer in the FAQ', link, 'arrow-link')}</p></div>
      {fcard(fk)}</div></div>''' for i, (k, lbl, q, ans, link, fk) in enumerate(topics))

    acts = [('Believe first.', 'Validate their disclosure and let them know you are there for them unconditionally.'),
            ('Avoid blame.', 'Resist questions that shift responsibility onto your child (“Why were you there?” “What were you wearing?”).'),
            ('Seek support.', 'Connect with a rape crisis advocate, counselor, or support group to guide you and your child through options for care, reporting, and healing.'),
            ('Care for yourself.', 'Supporting a survivor can be emotionally heavy. Finding your own support system will strengthen your ability to show up for your child.')]
    ah = ''.join(f'<div><b>{esc(t)}</b><p>{esc(d)}</p></div>' for t, d in acts)

    opts = [('Confidential', 'Speaking with an advocate or peer educator.', None),
            ('Anonymous', 'To flag harm without formal investigation.', None),
            ('Law enforcement', 'Filing a police report.', None),
            ('Title IX', 'Filing a school complaint for investigation and safety planning.', ('Title IX rights', 'title-ix.html'))]
    oh = ''.join(f'<div class="ad-opt"><span class="ad-mini">Reporting option</span><b>{esc(t)}</b><p>{esc(d)}</p>{a(esc(l[0]), l[1], "arrow-link") if l else ""}</div>' for t, d, l in opts)

    steps = [('Pick the right moment, not the charged one', 'Wait until things have cooled down. Good windows: a car ride, a casual one-on-one moment, a follow-up conversation after things have settled.'),
             ('Lead with curiosity, not direction', 'If it sounds like a punishment or an assignment, they won’t engage honestly. Offer it as something genuinely useful, not something you’re making them do.'),
             ('Make the privacy real', 'Send them the link and step away. Don’t ask to see what they wrote or what path they took, and make it clear they can stop at any point.'),
             ('Tell them what it actually is', '“It’s not a test. You can’t get it ‘wrong.’ It asks you questions about a situation and how you’re feeling, and then shows you some tools and information based on that. Nothing gets saved anywhere. It disappears when you close it.”'),
             ('Give them space, and keep the door open', '“If anything comes up when you go through it — questions, things you want to talk through — I’m around. But you don’t have to tell me anything.”')]
    sh = ''.join(f'<div class="step"><span class="step__n">{i+1}</span><h3>{esc(t)}</h3><p>{esc(d)}</p></div>' for i, (t, d) in enumerate(steps))
    starters = [('Opening the conversation', ['“Did you get a chance to look at that thing I sent? No worries if not — just wondering what you thought.”', '“Is there anything from it that stuck with you, or anything you want to talk about?”', '“Did anything surprise you or feel off?”']),
                ('If they seem uncomfortable', ['“You don’t have to tell me anything about it. I just wanted to check in that you’re okay.”', '“If something came up that felt heavy, I want you to know you can talk to me — or someone else you trust.”', '“Sometimes that stuff brings up more questions than answers. That’s fine — it’s actually a good sign.”']),
                ('Going deeper, if they’re open', ['“What does consent actually mean to you? What do you think it looks like in real life?”', '“Have you ever been in a situation where you weren’t sure if someone was into it? What did you do?”', '“How do you think you’d react if a friend told you they’d been in a situation where someone didn’t stop when asked?”']),
                ('If they didn’t use it', ['“That’s okay — I’ll leave the link with you. It’s there whenever you want it.”', '“Is there a reason it felt weird? I can explain what it actually is if that would help.”', '“Even without the tool — is there anything on your mind about what we talked about?”'])]
    sth = ''.join(f'<div class="ad-starter"><h3>{esc(t)}</h3><ul>{"".join(f"<li>{esc(x)}</li>" for x in xs)}</ul></div>' for t, xs in starters)

    involve = [('Certified Peer Educator Training', 'Encourage your student to enroll in our free, virtual, self-paced training that equips them to educate peers on consent, bystander intervention, and digital safety.', 'peer-educator.html', ['Free', 'Virtual', 'Self-paced']),
               ('Bring SafeBAE to your school', 'Ask your school to partner with us through our SafeBAE 360° whole-school model, which includes curriculum, peer educator training, staff development, and policy support.', '360-schools.html', ['360° Schools']),
               ('Summer Activist Institute', 'Support your student to apply for our annual Summer Activist Institute, an intensive leadership program that prepares youth to lead prevention and advocacy efforts in their own communities.', 'summer-institute.html', ['Annual']),
               ('Start a school club', 'Students can register a new SafeBAE chapter, affiliate a club they already run, or restart last year’s.', 'clubs.html', ['Clubs'])]
    ih = ''.join(row(t, d, h, m) for t, d, h, m in involve)

    vfeats = [('Completely private', 'No accounts, no tracking, no history. Nothing is saved or sent anywhere.'),
              ('Non-punitive tone', 'Designed to build awareness and accountability, not to condemn, label, or shame.'),
              ('Self-paced & self-guided', 'There are no right or wrong answers and no pressure to finish.'),
              ('Practical next steps', 'Interactive activities, guided lessons, grounding exercises, and support resources.')]
    vf = ''.join(f'<div><b>{esc(t)}</b><span>{esc(d)}</span></div>' for t, d in vfeats)

    body = f'''
{phero('Parents &amp; caregivers', 'Support the young people in your life and in your community.', 'For adults', [('Home', 'index.html'), ('For adults', 'adults.html'), ('Parents & caregivers', None)], kind='aqua', media='us-reis-parent', sticker='Whole-community prevention',
  extra='<p>Parents, caregivers, and trusted adults play a critical role in shaping how young people understand safety, consent, and relationships. While SafeBAE’s work is youth-led, prevention is a whole-community commitment. These tools, resources and guidance can help you feel prepared to support the teens in your life.</p>',
  actions=btn('Start the conversation early', '#early', 'slate', arrow=True) + btn('If your child tells you something happened', '#support', 'ghost'))}

<section class="band band--slate band--tight" aria-label="Podcast">
  <div class="wrap ad-pod">
    <div class="ad-pod__art">{img('sp-' + pod[0].lower(), 'The Longest Shortest Time podcast artwork')}</div>
    <div>
      <p class="eyebrow">Listen &middot; The Longest Shortest Time</p>
      <h2>How to Not (Accidentally) Raise a Rapist</h2>
      <p>SafeBAE’s Executive Director Shael Norris on the award-winning parenting podcast with Hillary Frank: what works when talking to teens about consent, and how schools and parents can build a consent-conscious culture.</p>
      <div class="tag-row">{a('NYT Opinion piece', pod[7][0][1], 'ext')}{a('NYT companion podcast', pod[7][1][1], 'ext')}</div>
    </div>
    <div class="ad-pod__play">{spotify(pod[0], pod[1], pod[2])}</div>
  </div>
</section>

<section class="band band--paper" id="early">
  <div class="wrap">
    <div class="ad-split ad-split--stretch">
      <div>
        <p class="eyebrow">Prevention &amp; early conversations</p>
        <h2>Start early, and keep talking</h2>
        <p class="lede">Even if it doesn’t always feel like it, young people look to the adults in their lives for cues about healthy relationships, boundaries, and safety. Starting conversations at home, supporting youth leaders in your community, and advocating for safer schools all make a lasting difference.</p>
        <ul class="ad-checks">
          <li>Begin practicing lessons of bodily autonomy and respect from the earliest ages.</li>
          <li>Use everyday opportunities (TV shows, news stories, or social media) to spark conversations before harm happens.</li>
          <li>Model open, judgment-free dialogue so your child feels safe confiding in you if something does happen.</li>
        </ul>
        <div class="ad-hl" style="margin-top:20px"><b>Create a “safe call” policy.</b><p>Assure your child they can call you anytime they feel unsafe. Safety comes before punishment, no matter what.</p></div>
      </div>
      <div class="ad-photo">{img('us-annaselle-parent', 'Two teenagers relaxing and talking on a couch')}<span class="sticker">Safety before punishment</span></div>
    </div>
    <div class="ad-early">
      <div class="ad-early__poster" data-gallery><button data-src="{imgsrc('baby-consent-print-materials-1')}" data-cap="SafeBAE poster: smile, high five, fist bump, handshake or hug">{img('baby-consent-print-materials-1', 'SafeBAE poster offering greetings to choose from: smile, high five, fist bump, handshake or hug')}</button></div>
      <div>
        <h3>Early ways to teach consent</h3>
        <p class="muted" style="margin:0">Teaching consent can start at the youngest ages, through simple, everyday choices that reinforce respect and bodily autonomy.</p>
        <div class="ad-early__items">{ei}</div>
        <p style="margin:0">As children grow, lessons about consent should grow with them. SafeBAE provides age-appropriate tools and resources to help families and educators build on these early conversations year after year.</p>
      </div>
    </div>
  </div>
</section>

<section class="band band--mist" id="talk">
  <div class="wrap">
    <div class="section-head"><div><p class="eyebrow">Talk about it together</p><h2>Topics to talk through with your teen</h2>
      <p class="lede lede--full">TV shows, news stories and social media all open the door to these conversations. Watching one of SafeBAE’s short, youth-made films together is another way in.</p></div></div>
    <div data-tabs="parents-topics"><div class="ad-tabs2" role="tablist" aria-label="Topics">{ttabs}</div>{tpanels}</div>
  </div>
</section>

<section class="band band--slate" id="support">
  <div class="wrap ad-split ad-split--top">
    <div>
      <p class="eyebrow">Supporting a survivor</p>
      <h2>If your child tells you something happened</h2>
      <p class="lede ad-lede-light">Learning that your child has experienced sexual violence can be overwhelming, frightening, and heartbreaking. You may feel shock, anger, sadness, or even guilt, and all of these are normal reactions. In this moment, the most important thing you can do is to center your child’s needs.</p>
      <p class="muted">Believe your child and reassure them that the assault was not their fault. Help them access the healing services and support they need, and remember that you, too, may need community and resources to process your own feelings.</p>
      <div class="ad-acts">{ah}</div>
      <div class="btns">{btn('Support a survivor', 'survivor-support.html', 'mint', arrow=True)}{btn('Healing resources', 'survivor-support.html', 'ghost')}</div>
    </div>
    <div>
      <div data-gallery><button class="ad-poster" data-src="{imgsrc('8x8-what-not-to-say-poster-pdf')}" data-cap="What to say vs. what not to say to a friend who shares they have been assaulted">{img('8x8-what-not-to-say-poster-pdf', 'SafeBAE poster: what to say and what not to say to someone who shares they have been assaulted. Say: I’m so sorry this happened to you. You are not alone. How can I support you? It’s not your fault. I’m glad you felt safe to tell me. Avoid: Why were you there? It’s going to be fine. Were you drinking? What were you wearing?')}<small>What to say, and what not to say. Tap to enlarge.</small></button></div>
      <div class="ad-helpcard"><b>Talk to someone now</b><span>RAINN: call 800-656-HOPE (4673) &middot; love is respect: text LOVEIS to 22522</span><span style="font-weight:500">Free, confidential support for survivors and the people who love them, open 24/7.</span><button class="btn btn--slate btn--sm" data-open-help>All hotlines</button></div>
    </div>
  </div>
</section>

<section class="band band--paper" id="reporting">
  <div class="wrap">
    <div class="section-head"><div><p class="eyebrow">Navigating reporting &amp; rights</p><h2>Listen to your child’s wishes first</h2>
      <p class="lede lede--full">Your instinct may be to report immediately. Instead, listen to your child’s wishes. If they do choose to report, connect first with an advocate. Reporting options may include:</p></div></div>
    <div class="ad-opts">{oh}</div>
    <div class="ad-alt" id="alternative-justice">
      <div>
        <p class="eyebrow">Alternative justice approaches</p>
        <h3>Accountability outside a formal investigation</h3>
        <p>Some survivors want to avoid a full Title IX or police investigation but still hope for accountability. They may wish for the person who harmed them to reflect on their actions and understand the impact.</p>
        <p>This pathway offers an opportunity for individuals who have caused harm to more fully learn about consent, accountability, and the unintended consequences of their behavior, outside of a formal investigation process.</p>
        <div class="btns" style="margin-top:18px">{btn('Accountability Training', 'accountability-training.html', 'slate', arrow=True)}</div>
      </div>
      <div data-gallery><button class="ad-poster" data-src="{imgsrc('untitled-design')}" data-cap="Types and degrees of restorative justice practice (credit: www.iirp.edu)">{img('untitled-design', 'Diagram of the types and degrees of restorative justice practice, showing survivor reparations, communities of care and offender responsibility overlapping at restorative justice')}<small>Types and degrees of restorative justice practice. Tap to enlarge.</small></button></div>
    </div>
  </div>
</section>

<section class="band band--teal" id="vibe-check">
  <div class="wrap ad-vibe">
    <div>
      <div class="ad-vmark"><span class="daisy"></span>Introducing Vibe Check</div>
      <h2>CheckYourVibe.org</h2>
      <p class="lede">As parents and caregivers, we all find ourselves worrying and trying our best to make this world safe for our children. But society, technology, and social media messaging can sometimes make that feel impossible.</p>
      <p style="color:#fff">We all struggled to navigate our childhoods, and our kids are no different. The measure of our character is not that we never make a mistake, but how we respond to learning that we have caused unintended harm. Intimacy is one of the hardest things for anyone to navigate, and we need as many tools as possible to help this generation do it better. That’s why we built Vibe Check: to support kids in asking vulnerable questions, navigating relationships, and being the best partners they can be.</p>
      <div class="ad-vfeats">{vf}</div>
      <div class="btns">{btn('Explore the tool', 'https://checkyourvibe.org/', 'mint')}{btn('Check Their Vibe: parent guide (PDF)', GUIDE_PDF, 'white')}{btn('How it works', 'vibe-check.html', 'ghost', arrow=True)}</div>
    </div>
    <div class="ad-phonewrap">
      <div class="ad-phone">{img('vc-screen', 'The Vibe Check home screen on a phone')}</div>
      <span class="sticker" style="left:0;top:16%">No account. No names.</span>
      <span class="sticker sticker--white sticker--r" style="right:0;bottom:18%">Nothing is stored</span>
    </div>
  </div>
</section>

<section class="band band--aqua" id="share">
  <div class="wrap">
    <div class="section-head"><div><p class="eyebrow">From the Check Their Vibe guide</p><h2>Sharing Vibe Check with your child</h2>
      <p class="lede lede--full">The most common mistake is introducing a tool like this in a moment of frustration. The best time is before anything has happened at all, as part of a talk about dating or sex.</p></div>{btn('Read the full guide (PDF)', GUIDE_PDF, 'slate')}</div>
    <div data-tabs="parents-share">
      <div class="ad-tabs2" role="tablist" aria-label="Sharing Vibe Check"><button class="tab" role="tab" id="st-before" aria-controls="sp-before" aria-selected="true">How to bring it up</button><button class="tab" role="tab" id="st-after" aria-controls="sp-after" aria-selected="false" tabindex="-1">Talking about it afterward</button></div>
      <div role="tabpanel" id="sp-before" aria-labelledby="st-before">
        <div class="ad-steps5">{sh}</div>
        <div class="ad-say">
          <div class="ad-say__try"><span class="ad-mini">Try saying something like</span><p>“Hey, I came across this thing — it’s not a lecture, it’s more like a self-reflection tool. Private, nothing gets saved. I thought it might be useful to go through on your own when you have a minute. No pressure, but I think it’s worth a look.”</p><span class="ad-mini">Or, for a younger person</span><p style="margin:0">“There’s a tool I want to show you — it’s like a private check-in for yourself about relationships and situations. You don’t have to share anything with me. I just thought it might be helpful.”</p></div>
          <div class="ad-say__avoid"><span class="ad-mini">Avoid framing it as</span><ul><li>“You need to do this because of what happened.”</li><li>“This will help you understand why you were wrong.”</li><li>“We’re going to go through this together.”</li><li>“I want to see your answers afterward.”</li></ul></div>
        </div>
      </div>
      <div role="tabpanel" id="sp-after" aria-labelledby="st-after" hidden>
        <div class="ad-starters">{sth}</div>
        <div class="ad-reminder"><p>If a young person comes to you after using it, receive that with curiosity, not judgment. Your reaction to the first vulnerable thing they share determines whether they share anything again.</p><button class="btn btn--coral btn--sm" data-open-help>If it’s a crisis: hotlines</button></div>
      </div>
    </div>
  </div>
</section>

<section class="band band--paper" id="involved">
  <div class="wrap ad-split ad-split--top">
    <div>
      <p class="eyebrow">Support youth by getting them involved</p>
      <h2>Connect your student with SafeBAE</h2>
      <p class="lede">One of the most powerful things you can do as a parent or caregiver is to connect your student with SafeBAE’s programs. These opportunities allow young people to build leadership skills, learn about consent and healthy relationships, and create change in their schools and communities.</p>
      <div class="ad-photo" style="min-height:0;height:auto;aspect-ratio:16/10">{img('img-6834', 'A group of SafeBAE student leaders smiling together at sunset')}<span class="sticker sticker--aqua">Youth-led</span></div>
    </div>
    <div class="rows">{ih}</div>
  </div>
</section>
{give_band()}
'''
    page('parents.html', 'Parents & Caregivers · SafeBAE', 'Guidance for parents and caregivers on talking with teens about consent and healthy relationships, supporting a survivor, reporting options, and sharing Vibe Check.',
         body, active='adults', fonts=film_font_link(), head_extra=HEAD)


# =====================================================================
# educators.html
# =====================================================================
def educators():
    guide_ids = ['red-flags', 'baecode', 'knowb4unude', 'dating', 'online-harassment', 'rape-culture', 'male-survivors']
    covers = ''
    for gid in guide_ids:
        it = next(x for x in LIB if x['id'] == gid)
        covers += f'<a href="{it["href"]}" title="{esc(it["title"])}">{img(it["guide"]["cover"], "Teaching guide: " + it["title"])}</a>'
    covers += f'<a class="ad-rr" href="film-race-rape-culture-resistance.html">{img("2l3a1960", "")}<span>Race, Rape Culture &amp; Resistance: four lessons</span></a>'
    posters = [('poster-consent-is-bae', 'Consent is BAE: mutual, ongoing, sober, enthusiastic, voluntary, revocable'),
               ('relationships-2-1', 'What goes into a healthy relationship?'),
               ('no-means-no-pdf', 'No means no, but so does silence, “maybe later”, “I’m not sure” and being drunk'),
               ('poster-sober', 'If you’ve had too much to drink to drive, the same is true for hooking up'),
               ('poster-ending-online-harassment', 'Ending online harassment is everyone’s responsibility'),
               ('poster-do-you-knowb4unude', 'Do you #knowB4Unude?')]
    ph = ''.join(f'<button data-src="{imgsrc(n)}" data-cap="{esc(c)}">{img(n, "SafeBAE poster: " + c)}</button>' for n, c in posters)
    svg, comps = ring_svg()
    svg = svg.replace(' tabindex="0" role="button"', '').replace('class="ring"', 'class="ring" role="img"')
    comp_li = ''.join(f'<li>{a(esc(t), h if not h.startswith("#") else "360-schools.html" + h)}</li>' for t, h, *_r in comps)

    levels = [
        ('guides', 'One class discussion', 'Teaching Guides', f'''<p>Our Teaching Guides are built for short, meaningful discussions. Each guide is paired with a youth-led educational video and includes discussion prompts and classroom activities.</p>
          <span class="ad-mini">Works well in</span><div class="ad-chipline">{chips(['Advisory', 'Health class', 'Homeroom', 'Clubs', 'Small groups'])}</div>
          <div class="btns">{btn('View teaching guides', 'library.html#guides', 'slate', arrow=True)}{btn('Browse every film', 'library.html#films', 'ghost')}</div>''', f'<div class="ad-covers">{covers}</div>'),
        ('posters', 'Around the building', 'Classroom Posters', f'''<p>Our posters are easy-to-share educational materials that help reinforce key messages around consent, healthy relationships, boundaries, and student support.</p>
          <span class="ad-mini">Put them up in</span><div class="ad-chipline">{chips(['Classrooms', 'Counseling offices', 'Hallways', 'Wellness centers', 'Student spaces'])}</div>
          <div class="btns">{btn('See all posters', 'posters.html', 'slate', arrow=True)}{btn('Download all (.zip)', POSTERS_ZIP, 'ghost')}</div>''', f'<div class="ad-pgrid" data-gallery>{ph}</div>'),
        ('curriculum', 'Across multiple class periods', 'Consent Curriculum', f'''<p>Our Consent Curriculum is designed for deeper, more sustained engagement across multiple class periods. It covers consent, healthy relationships, bystander intervention, and response, with structured lesson plans that can be adapted for different school contexts.</p>
          <div class="ad-chipline">{chips(['15 modules', 'Aligned with NHES', '45–60 minute lessons', 'English & Spanish'])}</div>
          <div class="btns">{btn('Learn more', 'consent-curriculum.html', 'slate', arrow=True)}{btn('Faculty & staff training', 'professional-development.html', 'ghost')}</div>''',
         f'<div class="ad-level__photo">{img("us-gariev-teacher", "A teacher leading a discussion with a class of students")}<span class="sticker">Teachers &amp; peer educators</span></div>'),
        ('360', 'Across the whole school', 'SafeBAE 360° Schools', f'''<p>Our 360° Schools program is a comprehensive, survivor-centered model that builds lasting prevention infrastructure across your whole school community. It spans education, youth leadership, policy reform, and staff training, and it is flexible enough to start small and grow over time.</p>
          <div class="btns">{btn('Explore 360° Schools', '360-schools.html', 'slate', arrow=True)}{btn('Request a program', '#request', 'ghost')}</div>''',
         f'<div class="ad-ringwrap">{svg}<ol>{comp_li}</ol></div>'),
    ]
    rungs = ''.join(f'<button class="ad-rung" role="tab" id="lv-{k}" aria-controls="lp-{k}" aria-selected="{str(i==0).lower()}" tabindex="{0 if i==0 else -1}"><small>{esc(s)}</small><span>{esc(t)}</span></button>' for i, (k, s, t, *_r) in enumerate(levels))
    lpanels = ''.join(f'<div role="tabpanel" id="lp-{k}" aria-labelledby="lv-{k}"{"" if i==0 else " hidden"}><div class="ad-level"><div><h3>{esc(t)}</h3>{txt}</div><div>{vis}</div></div></div>' for i, (k, s, t, txt, vis) in enumerate(levels))

    body = f'''
{phero('For educators', 'We know how very much educators are tasked with in any given day, so we have worked to provide tools for all levels of use. Start wherever you can. The most important part is helping your students feel engaged and invited into this work.', 'Classroom tools', [('Home', 'index.html'), ('For adults', 'adults.html'), ('Educators', None)], kind='logo', media='img-3947', sticker='Start wherever you can',
  actions=btn('See the tools', '#levels', 'mint', arrow=True) + btn('Request a program', '#request', 'ghost'))}

<section class="band band--paper" id="levels">
  <div class="wrap">
    <div class="section-head"><div><p class="eyebrow">Tools for all levels of use</p><h2>Classroom tools, from one lesson to the whole school</h2>
      <p class="lede lede--full">Pick the level that fits your time and your students, and add more when you’re ready.</p></div></div>
    <div data-tabs="edu-levels">
      <div class="ad-ladder" role="tablist" aria-label="Level of use">{rungs}</div>
      <div class="ad-axis" aria-hidden="true"><span>Short, meaningful discussions</span><span>Your whole school community</span></div>
      {lpanels}
    </div>
  </div>
</section>

<section class="band band--teal" id="vibe-check">
  <div class="wrap ad-vibe">
    <div>
      <div class="ad-vmark"><span class="daisy"></span>Introducing Vibe Check</div>
      <h2>CheckYourVibe.org</h2>
      <p class="lede">Vibe Check is a free, anonymous, self-guided tool that helps young people reflect on the health of their relationships. It is designed to be used privately and voluntarily.</p>
      <p class="ad-never">It should never be assigned to students.</p>
      <p style="color:#fff">Making it available as an optional resource allows students who may need it to access it on their own terms, before you know anything specific about their situation. Consider sharing the link where students can find it without being asked to engage publicly:</p>
      <div class="ad-ideas"><span>In your syllabus</span><span>On a resource wall</span><span>Anywhere students can find it on their own</span></div>
      <div class="btns">{btn('Explore the tool', 'https://checkyourvibe.org/', 'mint')}{btn('Adult guide (PDF)', GUIDE_PDF, 'white')}{btn('How it works', 'vibe-check.html', 'ghost', arrow=True)}</div>
    </div>
    <div class="ad-phonewrap">
      <div class="ad-phone">{img('vc-screen', 'The Vibe Check home screen on a phone')}</div>
      <span class="sticker" style="left:0;top:16%">Anonymous</span>
      <span class="sticker sticker--white sticker--r" style="right:0;bottom:18%">Optional, never assigned</span>
    </div>
  </div>
</section>

<section class="band band--paper" id="request">
  <div class="wrap ad-split ad-split--top">
    <div>
      <p class="eyebrow">Bring SafeBAE to your school</p>
      <h2>Ready to request a program?</h2>
      <p class="lede">Tell us what you’re looking for. Share key details about your needs and let us know how to follow up.</p>
      <ul class="ad-checks" style="margin-bottom:22px"><li>Assemblies and one-time events, always co-presented with youth leaders</li><li>Any component of SafeBAE 360° Schools, or the whole model</li><li>Flexible, sliding-scale pricing for school partners</li></ul>
      <div class="btns">{btn('Book a meeting', CALENDLY, 'teal')}{btn('Programs & pricing', 'request-a-program.html', 'ghost', arrow=True)}</div>
    </div>
    <div class="ad-card">{static_form('edu', 'Program request (educator)')}</div>
  </div>
</section>
{give_band()}
'''
    page('educators.html', 'For Educators · SafeBAE', 'Classroom tools for every level of use: youth-made films with teaching guides, prevention posters, the Consent Curriculum and SafeBAE 360° Schools.',
         body, active='adults', head_extra=HEAD)


# =====================================================================
# college.html
# =====================================================================
def college():
    body = f'''
{phero('For college students', 'Mentor high school students, start a SafeBAE club on your own campus, and become a Certified Peer Educator.', 'Get involved', [('Home', 'index.html'), ('For adults', 'adults.html'), ('College students', None)], media='1-7c1d4302-803a-4154-b18a-3a64432a6c76', sticker='Materials at no cost',
  actions=btn('Become a mentor', '#mentor', 'mint', arrow=True) + btn('Start a campus club', '#campus', 'ghost'))}

<section class="band band--paper" id="mentor">
  <div class="wrap ad-split">
    <div>
      <p class="eyebrow">Become a college student mentor</p>
      <h2>Mentor high school students</h2>
      <p class="lede">Our mentor opportunities are for college students who want to support SafeBAE by becoming Certified Peer Educators and connecting directly with high schools.</p>
      <span class="ad-mini">Mentors help students</span>
      <div class="ad-dos"><div>Build SafeBAE clubs</div><div>Advocate for safer policies</div><div>Transform their school culture</div></div>
      <p>Many college students who join us are also survivors themselves, motivated to create safer environments in the schools they came from. All student engagement materials are available to you at no cost, and our team is here to back you every step of the way.</p>
      <div class="ad-mail"><b>Interested? Email us to get started.</b>{copyable(EMAIL)}{btn('Email SafeBAE', mailto('College mentor'), 'mint', 'sm')}</div>
    </div>
    <figure class="ad-figure">{img('cc57083e-b9a4-48bf-bf9d-f4e4636d1447', 'A young advocate speaks at a rally in support of student survivors')}<figcaption>You know these communities best, and with our support, you can help lead meaningful change.</figcaption></figure>
  </div>
</section>

<section class="band band--aqua" id="campus">
  <div class="wrap ad-split ad-split--stretch">
    <div class="ad-photo">{img('us-colah-campus', 'Students walking across a college campus under the trees')}<span class="sticker sticker--white">Your campus</span></div>
    <div>
      <p class="eyebrow">Start a SafeBAE club on your campus</p>
      <h2>Bring SafeBAE to your own campus</h2>
      <p class="lede">Along with mentoring younger students, you can start a SafeBAE club on your own campus.</p>
      <p>Clubs bring together students to raise awareness, push for policy reform, and create a campus culture rooted in consent and accountability. We provide resources, training, and ongoing support to help you organize events, campaigns, and advocacy projects that make an impact.</p>
      <div class="ad-chipline">{chips(['Resources', 'Training', 'Ongoing support'], 'mint')}</div>
      <div class="btns">{btn('Start a campus club', 'clubs.html', 'slate', arrow=True)}{btn('Request a program', 'request-a-program.html', 'ghost')}</div>
    </div>
  </div>
</section>

<section class="band band--slate" id="certify">
  <div class="wrap ad-split">
    <div>
      <p class="eyebrow">Become a Certified Peer Educator</p>
      <h2>Get certified, then lead on your campus</h2>
      <p class="lede ad-lede-light">College students are encouraged to complete SafeBAE’s Certified Peer Educator Training to strengthen prevention on their own campuses and to collaborate with nearby high schools.</p>
      <div class="ad-hl" style="margin:0 0 22px"><b>Certified students are prioritized</b><p>when paid mentorship opportunities become available.</p></div>
      <div class="ad-chipline">{chips(['Free', 'Self-paced', '16 modules'], 'mint')}</div>
      <div class="btns">{btn('Become a Peer Educator', 'peer-educator.html', 'mint', arrow=True)}{btn('Register now', 'peer-educator.html#register', 'ghost')}</div>
    </div>
    {cpet_player()}
  </div>
</section>
{give_band()}
'''
    page('college.html', 'For College Students · SafeBAE', 'Mentor high school students, start a SafeBAE club on your campus, and become a Certified Peer Educator.',
         body, active='adults', head_extra=HEAD)


# =====================================================================
# request-a-program.html
# =====================================================================
def request():
    comps = [('Peer educator training & youth leadership', 'peer-educator.html'), ('Trauma-informed consent curriculum', 'consent-curriculum.html'),
             ('Faculty & staff professional development', 'professional-development.html'), ('School policy support', 'policy-reform-guide.html'),
             ('Anonymous reporting tool (SafeBAE x REES)', '360-schools.html#rees'), ('Educational resources to reduce recidivism', 'accountability-training.html')]
    cl = ''.join(f'<li>{a(esc(t), h)}</li>' for t, h in comps)
    cal = embed_box(CALENDLY + '?hide_gdpr_banner=1', CALENDLY, 'Pick a time that works for you on our Calendly page.', 'Book a meeting', height=760, title='Book a meeting with SafeBAE')
    body = f'''
{phero('Request a program', 'Bring SafeBAE to your school, campus or community.', 'For schools &amp; communities', [('Home', 'index.html'), ('For adults', 'adults.html'), ('Request a program', None)], image='066',
  actions=btn('Send a request', '#start', 'mint', arrow=True, attrs=' data-tab-go="tab-request"') + btn('Book a meeting', '#start', 'ghost', attrs=' data-tab-go="tab-book"'))}

<section class="band band--paper" id="programs">
  <div class="wrap">
    <div class="section-head"><div><p class="eyebrow">What we offer</p><h2>Start with one event, or build a whole-school program</h2></div></div>
    <div class="ad-offers">
      <article class="ad-offer ad-offer--aqua">
        <div class="ad-offer__media">{img('img-2395', 'Two SafeBAE presenters speaking to a group of students')}<span class="sticker">A first step</span></div>
        <div class="ad-offer__body">
          <h3>Assemblies &amp; one-time events</h3>
          <dl class="ad-meta"><dt>What</dt><dd>{chips(['Assemblies', 'Awareness events'])}</dd><dt>Who leads</dt><dd>{chips(['Co-presented with youth leaders'])}</dd><dt>Format</dt><dd>{chips(['One-time', 'Age-appropriate', 'Tailored to your school'])}</dd></dl>
          <p>Many school partners seek one-time assemblies or awareness events as an accessible first step, and we’re happy to offer them. While assemblies alone cannot replace sustained prevention work, they can spark critical conversations and open the door to deeper engagement.</p>
          <p>Our assemblies and school events are always co-presented with youth leaders and tailored to be age-appropriate, relevant, and impactful. They are a powerful entry point for schools beginning their partnership with us, and often serve as the starting place for longer-term collaboration.</p>
          <div class="ad-offer__foot">{btn('Request an assembly', '#start', 'slate', arrow=True, attrs=' data-tab-go="tab-request"')}</div>
        </div>
      </article>
      <article class="ad-offer ad-offer--slate">
        <div class="ad-offer__body">
          <span class="ad-mini">A comprehensive prevention model</span>
          <h3>SafeBAE 360° Schools</h3>
          <dl class="ad-meta"><dt>What</dt><dd>{chips(['Six core components'], 'mint')}</dd><dt>Who leads</dt><dd>{chips(['Youth-led'], 'mint')}</dd><dt>Format</dt><dd>{chips(['Individual components', 'Whole-school approach'], 'mint')}</dd></dl>
          <p>For schools seeking more than one-time events, SafeBAE’s comprehensive 360° Schools program offers a flexible, youth-led approach to building safer school communities.</p>
          <p>Each component can be delivered individually or be integrated as part of our whole-school approach, tailored to your school’s needs, goals, and capacity.</p>
          <ul class="ad-comps">{cl}</ul>
          <div class="ad-offer__foot">{btn('Learn more about 360° Schools', '360-schools.html', 'mint', arrow=True)}</div>
        </div>
      </article>
    </div>
  </div>
</section>

<section class="band band--deep">
  <div class="wrap ad-split">
    <div>
      <p class="eyebrow">From a school partner</p>
      <h2>What school leaders say about SafeBAE</h2>
      <p class="lede ad-lede-light">Hear from SafeBAE school partner Araceli Martinez, Community Schools Coordinator at Alliance Ted K. Tajima High School, as she reflects on why she brings SafeBAE to her campus and what she’s seen students gain from it.</p>
      <blockquote class="ad-q">“…I was talking with my intern from the school you visited and she informed me that the presentation that you did really affected the youth at the school. In fact, she has friends that are a couple, and they were in an unhealthy relationship and your presentation changed the way they now treat one another. She also said that she was able to look at herself and how she treated her partner and make changes as well.”<cite>Dawn M. Keys, Newport Prevention Coalition Coordinator</cite></blockquote>
    </div>
    {yt('ur2b6V1Pipk', 'A school leader’s perspective', label='Araceli Martinez')}
  </div>
</section>

<section class="band band--mint" id="pricing">
  <div class="wrap">
    <p class="eyebrow">Flexible pricing for school partners</p>
    <h2>Cost should never be a barrier to prevention</h2>
    <p class="lede lede--full">That’s why we offer a flexible, sliding-scale pricing model tailored to each school’s needs and capacity, always striving to meet partners where they are. We consider factors like:</p>
    <div class="ad-factors"><div><small>Factor</small><b>Program scope</b></div><div><small>Factor</small><b>Number of speakers</b></div><div><small>Factor</small><b>Travel requirements</b></div></div>
    <div class="btns">{btn('Book a meeting to learn more', '#start', 'slate', arrow=True, attrs=' data-tab-go="tab-book"')}{btn('Send a request', '#start', 'ghost', attrs=' data-tab-go="tab-request"')}</div>
  </div>
</section>

<section class="band band--paper" id="start">
  <div class="wrap">
    <div class="section-head"><div><p class="eyebrow">Get started</p><h2>Ready to request a program?</h2></div></div>
    <div data-tabs="request-start">
      <div class="ad-tabs2" role="tablist" aria-label="How would you like to start?"><button class="tab" role="tab" id="tab-request" aria-controls="rp-request" aria-selected="true">Send a request</button><button class="tab" role="tab" id="tab-book" aria-controls="rp-book" aria-selected="false" tabindex="-1">Book a meeting</button></div>
      <div role="tabpanel" id="rp-request" aria-labelledby="tab-request">
        <div class="ad-startpanel">
          <div><h3>Tell us what you’re looking for</h3><p class="muted">Share key details about your needs and let us know how to follow up.</p>
            <div class="ad-photo" style="min-height:240px;height:auto;aspect-ratio:4/3">{img('img-2400', 'Students listening during a SafeBAE session')}</div></div>
          <div class="ad-card">{static_form('req', 'Program request')}</div>
        </div>
      </div>
      <div role="tabpanel" id="rp-book" aria-labelledby="tab-book" hidden>
        <div class="ad-startpanel">
          <div><h3>Book a meeting with our team</h3><p class="muted">Book a meeting with us to learn more and get started. We’ll talk through your school’s needs, goals and capacity, and how our sliding-scale pricing applies.</p>{btn('Open Calendly', CALENDLY, 'teal')}</div>
          <div class="ad-card">{cal}</div>
        </div>
      </div>
    </div>
  </div>
</section>
{give_band('Your donation makes an immediate impact by enabling us to offer free consent education and resources to students across the US.')}
'''
    page('request-a-program.html', 'Request a Program · SafeBAE', 'Book SafeBAE assemblies, trainings and the 360° Schools model for your school, campus or community, with flexible sliding-scale pricing.',
         body, active='adults', head_extra=HEAD, scripts=TABGO_JS)


# =====================================================================
# donate.html
# =====================================================================
def donate():
    zeffy = embed_box(ZEFFY_EMBED + '1ac5fff7-3c20-45c1-95f1-f4fa34a07f88', ZEFFY_PUBLIC + '1ac5fff7-3c20-45c1-95f1-f4fa34a07f88',
                      'Give securely through Zeffy, as a one-time or monthly gift.', 'Open the donation form', height=900, title='Donation form powered by Zeffy', cls='ad-fallback--tall',
                      extra=f'<div class="ad-fb-alt"><span class="ad-mini">Other ways to give right now</span><p>Venmo {a("@Safe-BAE", VENMO, "link")} &middot; {a("Mail a check", "#ways", "link", attrs=' data-tab-go="wt-check"')} &middot; {a("Employer matching", "#ways", "link", attrs=' data-tab-go="wt-match"')}</p></div>')
    ways = [
        ('shop', 'Shop for a cause', 'Buy books, posters, and classroom tools. Every purchase funds prevention.',
         f'''<p>Browse curriculum materials, posters, and classroom tools in our educational shop, or buy your next read through our Bookshop.org storefront. A portion of every book purchase supports SafeBAE at no extra cost to you.</p>
         <div class="btns">{btn('Educational products', 'https://safebae.podia.com/', 'teal')}{btn('Our Bookshop', 'https://bookshop.org/shop/SafeBAE', 'ghost')}</div>'''),
        ('match', 'Double your gift', 'Employer matching can double or even triple your donation.',
         f'''<ol><li>Check your HR or giving portal to see if your employer matches donations.</li><li>List <b>SafeBAE</b>, a registered 501(c)(3), as the recipient. EIN {copyable('81-5451147')}</li><li>Need additional documentation? Use our contact form or email us at {a(EMAIL, mailto('Employer Matching'), 'link')}.</li></ol>
         <div class="btns">{btn('Contact form', 'contact.html', 'teal')}{btn('Email us', mailto('Employer Matching'), 'ghost')}</div>'''),
        ('fundraise', 'Fundraise for SafeBAE', 'Turn a birthday, run, or campus event into support for prevention.',
         f'''<p>Pick your moment (a birthday, a 5K, a class project, a campus event) and invite your community to give alongside you. Share your idea through our contact form or email us at {a(EMAIL, mailto('Fundraising for SafeBAE'), 'link')} and we’ll help you set everything up.</p>
         <div class="btns">{btn('See current fundraisers', 'fundraise.html', 'teal', arrow=True)}{btn('Contact form', 'contact.html', 'ghost')}{btn('Email us', mailto('Fundraising for SafeBAE'), 'ghost')}</div>'''),
        ('partner', 'Partner or give in-kind', 'Sponsorships and partnerships for companies, foundations and groups.',
         f'''<p>Support the work through sponsorship, in-kind donations, or a longer-term partnership. Reach out through our contact form or email us at {a(EMAIL, mailto('Partnership'), 'link')} to talk through what fits your organization.</p>
         <div class="btns">{btn('Contact form', 'contact.html', 'teal')}{btn('Email us', mailto('Partnership'), 'ghost')}</div>'''),
        ('check', 'Mail a check', 'Prefer to give by mail? We gladly accept checks.',
         f'''<p>Make checks payable to <b>SafeBAE</b> and mail to:</p>
         <p class="ad-addr">SafeBAE<br>7 Evelyn Drive<br>Bristol, RI 02809</p>
         <p>{copyable('SafeBAE, 7 Evelyn Drive, Bristol, RI 02809', 'Copy the address')}</p>
         <p class="muted">Include your email or return address if you’d like an acknowledgment for your records.</p>'''),
        ('other', 'Other ways to give', 'Gifts of stock, donor-advised funds and planned giving.',
         f'''<p>For gifts of stock, donor-advised fund grants, planned giving, or anything not covered here, use our contact form or email us at {a(EMAIL, mailto('Other Ways to Give'), 'link')} and we’ll point you in the right direction.</p>
         <div class="btns">{btn('Contact form', 'contact.html', 'teal')}{btn('Email us', mailto('Other Ways to Give'), 'ghost')}</div>'''),
    ]
    wl = ''.join(f'<button class="ad-way" role="tab" id="wt-{k}" aria-controls="wp-{k}" aria-selected="{str(i==0).lower()}" tabindex="{0 if i==0 else -1}"><b>{esc(t)}</b><small>{esc(s)}</small></button>' for i, (k, t, s, _d) in enumerate(ways))
    wp = ''.join(f'<div role="tabpanel" id="wp-{k}" aria-labelledby="wt-{k}"{"" if i==0 else " hidden"} class="ad-wpanel"><span class="ad-mini">More ways to give</span><h3>{esc(t)}</h3>{d}</div>' for i, (k, t, s, d) in enumerate(ways))

    body = f'''
<section class="ad-dhero">
  <div class="wrap ad-dhero__grid">
    <div>
      <nav class="crumbs" aria-label="Breadcrumb"><a href="index.html">Home</a><span>/</span><span>Donate</span></nav>
      <p class="eyebrow">Safe Before Anyone Else</p>
      <h1 class="ad-h1">Help end sexual violence before it starts.</h1>
      <p class="lede ad-lede-light">SafeBAE is a survivor-founded, youth-led organization dedicated to ending sexual violence before it starts. Our programs are free for students and designed to create lasting culture change in schools, backed by a growing body of evidence showing real impact.</p>
      <div class="btns">{btn('Make your gift', '#give', 'coral', arrow=True)}{btn('More ways to give', '#ways', 'ghost')}</div>
    </div>
    <div class="ad-dhero__photo">{img('dsc01134', 'SafeBAE youth leaders in SafeBAE t-shirts', loading='eager')}<span class="sticker" style="left:-12px;bottom:26px">Free for students</span><span class="sticker sticker--white sticker--r" style="right:-8px;top:22px">Survivor-founded</span></div>
  </div>
</section>

<section class="band band--paper" id="give">
  <div class="wrap ad-give">
    <div class="ad-give__head">
      <p class="eyebrow">Make your gift</p>
      <h2>Monthly gifts help most.</h2>
      <p class="lede" style="margin-bottom:0">They give us steady funding we can plan around.</p>
    </div>
    <div class="ad-give__form">
      <div class="ad-zeffy">{zeffy}</div>
      <p class="ad-small">Zeffy charges us no platform fees. Your full gift funds the work.</p>
    </div>
    <div class="ad-give__rest">
      <span class="ad-mini">Your gift funds</span>
      <ul class="ad-checks ad-fund">
        <li>Peer educator training for student leaders across the country</li>
        <li>360° Schools, our whole-school prevention program</li>
        <li>Free tools like Vibe Check that help teens reflect on their own behavior</li>
        <li>Survivor support and trauma-informed policy advocacy</li>
      </ul>
      <div class="ad-bigstat"><b>3,000+</b><span>young people trained as Certified Peer Educators so far</span></div>
      <p style="margin:0 0 6px"><b>Prefer Venmo?</b> Give to {a('@Safe-BAE', VENMO, 'link')}.</p>
      <p style="margin:0" class="small">Questions about your gift? Email {a(EMAIL, mailto('Donation Question'), 'link')}.</p>
      <div class="ad-trust">{img('candid-platinum-seal-of-transparency-1-0', 'Candid Platinum Seal of Transparency')}<span>SafeBAE is a registered 501(c)(3) nonprofit with a Candid Platinum Seal of Transparency. Gifts are tax-deductible.<br>EIN {copyable('81-5451147')}</span></div>
    </div>
  </div>
</section>

<section class="band band--deep">
  <div class="wrap ad-story">
    {img('000422', 'A large group of SafeBAE students in tie-dye SafeBAE shirts on the steps of a building')}
    <div>
      <p class="eyebrow">Born from lived experience</p>
      <h2>Founded by survivors, led by young people</h2>
      <p class="lede ad-lede-light">SafeBAE began when our co-founders met during the filming of Netflix’s <i>Audrie &amp; Daisy</i>, united by a shared goal: to prevent what happened to us from happening to anyone else.</p>
      <p class="muted">Today, we’re a national organization where young people lead the work of sexual violence prevention.</p>
      <div class="btns" style="margin-top:22px">{btn('Our story', 'about.html', 'mint', arrow=True)}{btn('See the data', 'impact.html', 'ghost')}{btn('#ForDaisy', 'fordaisy.html', 'ghost')}</div>
    </div>
  </div>
</section>

<section class="band band--paper" id="ways">
  <div class="wrap">
    <div class="section-head"><div><p class="eyebrow">Explore more ways to give</p><h2>Give in the way that works for you</h2></div></div>
    <div class="ad-ways" data-tabs="donate-ways"><div class="ad-ways__list" role="tablist" aria-label="Ways to give" aria-orientation="vertical">{wl}</div><div>{wp}</div></div>
  </div>
</section>

<section class="band band--aqua band--tight">
  <div class="wrap ad-strip">
    <div class="ad-strip__txt"><b>Found SafeBAE’s resources helpful?</b><p>Chip in any amount, or give through a supporter’s fundraiser.</p></div>
    <div class="btns">{btn('Chip in', 'chip-in.html', 'teal', arrow=True)}{btn('Peer-to-peer fundraisers', 'fundraise.html', 'ghost')}</div>
  </div>
</section>
'''
    page('donate.html', 'Donate · SafeBAE', 'Support SafeBAE’s youth-led work to prevent sexual violence. Your donation funds peer education, free resources, and safer school communities.',
         body, active='', head_extra=HEAD, scripts=TABGO_JS)


# =====================================================================
# chip-in.html
# =====================================================================
def chipin():
    zeffy = embed_box(ZEFFY_EMBED + 'chip-in-2', ZEFFY_PUBLIC + 'chip-in-2', 'Chip in securely through Zeffy.', 'Open the form', height=820, title='Donation form powered by Zeffy')
    body = f'''
<section class="ad-chipin">
  <div class="wrap ad-split ad-split--stretch">
    <div>
      <nav class="crumbs" aria-label="Breadcrumb"><a href="index.html">Home</a><span>/</span><a href="donate.html">Donate</a><span>/</span><span>Chip in</span></nav>
      <p class="eyebrow">{daisy()}Chip in</p>
      <h1>Did you find SafeBAE’s resources helpful?</h1>
      <p class="lede">We believe every young person deserves access to clear, honest, and practical information about consent, relationships, and safety, without barriers. If something you found here helped you, you can help us keep these resources free and accessible to young people everywhere.</p>
      <span class="ad-mini">Your support helps make this possible</span>
      <ul class="ad-impact">
        <li>Trained <strong>3,000+ young people</strong> as Certified Peer Educators</li>
        <li>Built a growing library of <strong>consent and healthy relationship resources</strong> used by students and educators nationwide</li>
        <li>Delivered <strong>workshops, classroom sessions, and peer-led trainings</strong> across the country</li>
        <li>Created <strong>youth-led media and tools</strong> that reach young people where they are, online and in their communities</li>
      </ul>
      <p style="font-family:var(--display);font-stretch:106%;font-weight:700;font-size:1.15rem;margin:0 0 20px">Everything we create is led by young people, and kept free for youth so that everyone can access it when they need it.</p>
      <div class="ad-photo" style="min-height:0;height:auto;aspect-ratio:16/9">{img('clubhero', 'SafeBAE club members taking a group selfie outdoors')}<span class="sticker">Led by young people</span></div>
    </div>
    <div class="ad-fill"><div class="ad-zeffy">{zeffy}</div></div>
  </div>
</section>

<section class="band band--paper band--tight">
  <div class="wrap">
    <div class="section-head"><div><p class="eyebrow">Other ways to help</p><h2>Keep the resources free</h2></div></div>
    <div class="ad-acts4">
      <a href="donate.html#give"><b>Give monthly</b><span>Steady funding we can plan around.</span><i>Donate &rarr;</i></a>
      <a href="fundraise.html"><b>Fundraise</b><span>Turn a birthday, run or campus event into support.</span><i>Fundraisers &rarr;</i></a>
      <a href="https://safebae.podia.com/" target="_blank" rel="noopener"><b>Shop educational products</b><span>Curriculum materials, posters and classroom tools.</span><i>Shop &#8599;</i></a>
      <a href="https://bookshop.org/shop/SafeBAE" target="_blank" rel="noopener"><b>Buy a book</b><span>Bookshop.org purchases support SafeBAE at no extra cost.</span><i>Bookshop &#8599;</i></a>
    </div>
  </div>
</section>
'''
    page('chip-in.html', 'Chip In · SafeBAE', 'Found SafeBAE’s resources helpful? Chip in to keep consent and healthy relationship resources free for young people everywhere.',
         body, active='', head_extra=HEAD)


# =====================================================================
# fundraise.html
# =====================================================================
def fundraise():
    def venmo_block(note_html, keyword=None):
        cp = copyable(keyword, f'Note: {keyword}') if keyword else ''
        return f'''<div class="ad-venmo"><p>You can also support this fundraiser via Venmo. To help us properly track donations and giveaway entries, please include {note_html} in the payment note.</p><div class="btns">{btn('Venmo @Safe-BAE', VENMO, 'teal', 'sm')}{cp}</div></div>'''

    frs = [
        ('justin', 'Justin', 'img-4048', False, 'Justin, smiling in sunglasses and a cap, leaning on a porch railing outdoors',
         'Justin’s SafeBAE Fundraiser',
         '<p>This month, I’m using my platform to raise awareness and funds for SafeBAE, a survivor-founded, youth-led organization dedicated to ending sexual violence and supporting mental health among middle and high school students. As a longtime educator, I believe every young person deserves to be in an environment free from sexual violence, harassment, and abuse.</p>',
         venmo_block('<b>Justin</b>', 'Justin'), 'justins-safebae-fundraiser', ''),
        ('tuna', 'Tina', 'everyone-can-do-something-1', True, 'SafeBAE poster: No one can do everything but everyone can do something. End rape culture.',
         'Tina’s SafeBAE Fundraiser',
         '<p>For tonight’s livestream I’m using my platform to raise awareness and funds for SafeBAE, an organization I wish was around when I was a teenager. It is a survivor-founded, youth-led organization dedicated to ending sexual assault and dating violence among middle and high school students.</p>',
         venmo_block('<b>TUNA</b>', 'TUNA'), 'tunas-safebae-fundraiser',
         '<div class="ad-raised"><h4>Total raised so far</h4>' + embed('https://www.zeffy.com/embed/thermometer/tunas-safebae-fundraiser', ZEFFY_PUBLIC + 'tunas-safebae-fundraiser', 'The live total for Tina’s fundraiser appears here.', height=120, title='Fundraiser progress powered by Zeffy', cta='See the live total') + '</div>'),
        ('vanessa', 'Vanessa', 'copy-of-education-1', True, 'Polaroid-style photo captioned “Vanessa (Age 15)”: a teenage Vanessa looks back over her shoulder from a desk with a computer',
         'Vanessa’s SafeBAE Fundraiser',
         '<p>This month, I’m using my platform to raise awareness and funds for SafeBAE, an organization I wish was around when I was a teenager. It is a survivor-founded, youth-led organization dedicated to ending sexual violence and supporting mental health among middle and high school students.</p>',
         venmo_block('<b>your Instagram handle (username)</b>'), 'vanessa', ''),
    ]
    avatars = {'justin': 'img-4048', 'tuna': 'everyone-can-do-something-1', 'vanessa': 'copy-of-education-1'}
    tabs = ''.join(f'<button class="ad-ptab" role="tab" id="tab-{k}" aria-controls="fp-{k}" aria-selected="{str(i==0).lower()}" tabindex="{0 if i==0 else -1}">{img(avatars[k], "")}{esc(n)}</button>' for i, (k, n, *_r) in enumerate(frs))
    panels = ''
    for i, (k, n, im, contain, alt, h, story, venmo, zslug, extra) in enumerate(frs):
        z = embed_box(ZEFFY_EMBED + zslug, ZEFFY_PUBLIC + zslug, f'Give to {n}’s fundraiser securely through Zeffy.', f'Give to {n}’s fundraiser', height=900, title='Donation form powered by Zeffy')
        panels += f'''<div role="tabpanel" id="fp-{k}" aria-labelledby="tab-{k}"{'' if i==0 else ' hidden'}><div class="ad-fr">
      <div><div class="ad-fr__photo{' ad-fr__photo--contain' if contain else ''}">{img(im, alt)}</div><span class="ad-mini">Peer-to-peer fundraiser</span><h3>{esc(h)}</h3>{story}{venmo}</div>
      <div class="ad-fill"><div class="ad-zeffy">{z}</div>{extra}</div></div></div>'''

    body = f'''
<section class="ad-fhero">
  <div class="wrap ad-fhero__grid">
    <div>
      <nav class="crumbs" aria-label="Breadcrumb"><a href="index.html">Home</a><span>/</span><a href="donate.html">Donate</a><span>/</span><span>Fundraise</span></nav>
      <p class="eyebrow">Peer-to-peer fundraising</p>
      <h1 class="ad-h1">Fundraise for SafeBAE</h1>
      <p class="lede ad-lede-light">Turn a birthday, run, or campus event into support for prevention. Supporters use their own platforms to raise awareness and funds for SafeBAE, and invite their communities to give alongside them.</p>
      <div class="btns">{btn('Give to a fundraiser', '#fundraisers', 'mint', arrow=True)}{btn('Start your own', '#start', 'ghost')}</div>
    </div>
    <div class="ad-pols">
      <a class="ad-pol" href="#fundraisers" data-tab-go="tab-justin">{img('img-4048', 'Justin', loading='eager')}<span>Justin</span></a>
      <a class="ad-pol ad-pol--v" href="#fundraisers" data-tab-go="tab-vanessa">{img('copy-of-education-1', 'Vanessa at age 15', loading='eager')}<span>Vanessa</span></a>
      <a class="ad-pol ad-pol--contain" href="#fundraisers" data-tab-go="tab-tuna">{img('everyone-can-do-something-1', 'Tina’s fundraiser poster', loading='eager')}<span>Tina</span></a>
    </div>
  </div>
</section>

<section class="band band--paper" id="fundraisers">
  <div class="wrap">
    <div class="section-head"><div><p class="eyebrow">Current fundraisers</p><h2>Give through a supporter’s fundraiser</h2></div></div>
    <div data-tabs="fundraisers"><div class="ad-ptabs" role="tablist" aria-label="Fundraisers">{tabs}</div>{panels}</div>
  </div>
</section>

<section class="band band--aqua">
  <div class="wrap">
    <div class="section-head"><div><p class="eyebrow">Not ready to donate?</p><h2>You can still support SafeBAE</h2></div></div>
    <div class="ad-acts4">
      <a href="https://www.instagram.com/safe_bae/" target="_blank" rel="noopener"><b>Follow @safe_bae</b><span>Follow SafeBAE on Instagram.</span><i>Instagram &#8599;</i></a>
      <a href="https://checkyourvibe.org/" target="_blank" rel="noopener"><b>Share CheckYourVibe.org</b><span>Share Vibe Check with someone.</span><i>Vibe Check &#8599;</i></a>
      <a href="peer-educator.html"><b>Spread the word</b><span>Tell others about the Certified Peer Educator Training.</span><i>Peer Educator Training &rarr;</i></a>
      <a href="mailto:{EMAIL}"><b>Get involved</b><span>Email {EMAIL} to get involved.</span><i>Email us &rarr;</i></a>
    </div>
  </div>
</section>

<section class="band band--paper" id="start">
  <div class="wrap ad-split">
    <div>
      <p class="eyebrow">Start your own fundraiser</p>
      <h2>Pick your moment</h2>
      <div class="ad-moments"><span>A birthday</span><span>A 5K</span><span>A class project</span><span>A campus event</span></div>
      <p class="lede">Invite your community to give alongside you. Share your idea through our contact form or email us at {EMAIL} and we’ll help you set everything up.</p>
      <div class="btns">{btn('Contact form', 'contact.html', 'teal', arrow=True)}{btn('Email us', mailto('Fundraising for SafeBAE'), 'ghost')}</div>
    </div>
    <div class="ad-photo" style="min-height:380px">{img('img-9509-1', 'Hands decorating SafeBAE “yes means yes” consent stickers')}<span class="sticker sticker--aqua">Every gift funds prevention</span></div>
  </div>
</section>
'''
    page('fundraise.html', 'Fundraise for SafeBAE', 'Give through a supporter’s peer-to-peer fundraiser for SafeBAE, or start your own for a birthday, run, class project or campus event.',
         body, active='', head_extra=HEAD, scripts=TABGO_JS)


def build():
    adults(); parents(); educators(); college(); request(); donate(); chipin(); fundraise()


if __name__ == '__main__':
    build()
