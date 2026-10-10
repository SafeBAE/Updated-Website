"""Adults + Giving group (v3): educators.html, college.html, donate.html, chip-in.html, fundraise.html.
Content carried from the live safebae.org pages (educators, college-students, donate, chipin,
justin, tuna, vanessa).  adults.html and parents.html build from pages_adults.py and
request-a-program.html from pages_programs.py; this module shares their 12-column grid and card anatomy
so the audience pages read as one family.
v4: each page ends once. Educators: the two new programs are two links in the request band. College: the AI
Literacy band is one line under "Get certified". Donate, Chip In and Fundraise are the only pages with giving content.

The two giving embeds (Zeffy) have two states: on a live site site.js swaps an iframe into .embed, and
everywhere else (file://, a framed preview) the fallback card shows.  Each layout below is composed for
both: the grids re-place their areas with :has(.embed iframe)."""
from lib import *
from data import LIB, WP
from pages_home import cpet_player, ring_svg

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


def crumbs(*items):
    return ('<nav class="crumbs" aria-label="Breadcrumb">'
            + '<span>/</span>'.join(a(esc(t), h) if h else f'<span>{esc(t)}</span>' for t, h in items) + '</nav>')


def embed_box(src, fallback, height=900, title='Donation form powered by Zeffy', note=''):
    """Same contract as lib.embed (site.js swaps in the iframe on a live site); the fallback is a finished card.
    `note` is a line that sits under the live form, inside its frame (the fallback card carries the same line itself)."""
    foot = f'<p class="ad-fee">{note}</p>' if note else ''
    return (f'<div class="ad-zeffy"><div class="embed" data-embed="{esc(src)}" data-h="{height}" data-title="{esc(title)}">'
            f'<div class="embed__fallback">{fallback}</div></div>{foot}</div>')


def ratio(name):
    """width / height of a site image, for rows where every picture shares one height."""
    m = MANIFEST.get(name)
    if not m:
        from PIL import Image
        im = Image.open(f'{SITE}/assets/img/{name}.webp'); m = {'w': im.width, 'h': im.height}
    return round(m['w'] / m['h'], 4)


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
  <div class="field ad-form__grow"><label for="{fid}-msg">What are you hoping to book or learn more about?</label><textarea id="{fid}-msg" name="Request" placeholder="Share what you’re hoping to book or learn more about…"></textarea></div>
  <div class="btns"><button class="btn btn--slate" type="submit">Submit request</button><span class="form__note">Or email {a(EMAIL, 'mailto:' + EMAIL, 'link')}</span></div>
  <p class="form__done" role="status">Thank you. Your email app should open with your request ready to send. If it doesn’t, write to {EMAIL}.</p>
</form>'''


# a link elsewhere on the page that opens one tab of a tab set
TABGO_JS = r'''<script>(function(){
  document.querySelectorAll('[data-tab-go]').forEach(function(l){ l.addEventListener('click', function(e){
    var t = document.getElementById(l.getAttribute('data-tab-go')); if(!t) return;
    e.preventDefault(); t.click(); var box = t.closest('[data-tabs]') || t;
    var y = box.getBoundingClientRect().top + window.pageYOffset - 130;
    window.scrollTo({top: y, behavior: matchMedia('(prefers-reduced-motion: reduce)').matches ? 'auto' : 'smooth'});
    try{ history.replaceState(null, '', '#' + t.id.replace(/^tab-/, '')); }catch(err){}
  }); });
})();</script>'''

# one-shot entrances: [data-in] gets .in when it scrolls into view; [data-count] counts up once
IN_JS = r'''<script>(function(){
  var d = document, reduce = matchMedia('(prefers-reduced-motion: reduce)').matches;
  var els = [].slice.call(d.querySelectorAll('[data-in]'));
  function count(el){
    var b = el.querySelector('[data-count]'); if(!b || reduce) return;
    var to = +b.getAttribute('data-count'), suf = b.getAttribute('data-suffix') || '', t0 = null, dur = 1300;
    function fmt(n){ return Math.round(n).toLocaleString('en-US') + suf; }
    function step(t){ if(t0 === null) t0 = t; var k = Math.min(1, (t - t0) / dur); k = 1 - Math.pow(1 - k, 3); b.textContent = fmt(to * k); if(k < 1) requestAnimationFrame(step); else b.textContent = fmt(to); }
    requestAnimationFrame(step);
  }
  if(!('IntersectionObserver' in window)){ els.forEach(function(e){ e.classList.add('in'); }); return; }
  var io = new IntersectionObserver(function(es){ es.forEach(function(en){ if(en.isIntersecting){ en.target.classList.add('in'); count(en.target); io.unobserve(en.target); } }); }, {threshold: .2});
  els.forEach(function(e){ io.observe(e); });
})();</script>'''

CSS = r'''
/* ---------- grid: 12 columns inside the wrap (same as adults.html / parents.html) ---------- */
.ad-g{display:grid; grid-template-columns:repeat(12,minmax(0,1fr)); gap:var(--gap)}
.ad-g > *{min-width:0}
.ad-c4{grid-column:span 4} .ad-c5{grid-column:span 5} .ad-c6{grid-column:span 6} .ad-c7{grid-column:span 7} .ad-c8{grid-column:span 8}
.ad-pr{padding-right:clamp(0px,calc(6vw - 46px),40px)}
.ad-pl{padding-left:clamp(0px,calc(6vw - 46px),40px)}
.ad-col{display:flex; flex-direction:column}
.ad-col > .btns:last-child{margin-top:auto; padding-top:24px}
@media (max-width:900px){
  .ad-g{grid-template-columns:minmax(0,1fr)} .ad-g > *{grid-column:auto} .ad-pr{padding-right:0} .ad-pl{padding-left:0}
  /* small screens: heading, then media, then text, then actions */
  .ad-g.ad-g--m{display:flex; flex-direction:column; align-items:stretch; gap:0}
  .ad-g--m > .ad-txt{display:contents}
  .ad-g--m > .ad-txt > *{order:3}
  .ad-g--m > .ad-txt > :is(.crumbs,.eyebrow,h1,h2,.ad-vmark){order:1}
  .ad-g--m > .ad-txt > .eyebrow{align-self:flex-start}
  .ad-g--m > .ad-media{order:2; margin-block:10px 26px}
}

/* ---------- shared pieces ---------- */
.ad main .eyebrow{color:var(--logo-teal)}
.ad main :is(.band--slate,.band--deep,.phero:not(.phero--aqua)) .eyebrow{color:var(--mint)}
.ad main .band--teal .eyebrow{color:#fff}
.ad-lede-light{color:rgba(255,255,255,.9)}
.ad-mini{font-family:var(--mono); font-size:.72rem; letter-spacing:.1em; text-transform:uppercase; font-weight:600; color:var(--logo-teal); display:block}
:is(.band--slate,.band--deep) .ad-mini{color:var(--mint)}
.ad-shot{margin:0}
.ad-shot .sticker{position:absolute; left:16px; bottom:18px; z-index:1; font-size:clamp(.74rem,1.05vw,.9rem); max-width:calc(100% - 32px)}
.ad-checks{list-style:none; padding:0; margin:0; display:grid; gap:10px}
.ad-checks li{position:relative; padding-left:28px; margin:0}
.ad-checks li::before{content:""; position:absolute; left:2px; top:.5em; width:11px; height:11px; background:var(--teal); transform:rotate(45deg); border-radius:2px}
:is(.band--slate,.band--deep,.band--teal) .ad-checks li::before{background:var(--mint)}
.ad .copy{font-size:.95rem; padding:7px 7px 7px 12px; border-radius:8px; max-width:100%; white-space:nowrap}
.ad .copy button{font-size:.78rem; padding:6px 10px; min-height:30px; border-radius:6px; transition:background .2s}
.ad .copy button:hover{background:var(--teal)}
@media (max-width:900px){.ad main .btn--sm{min-height:44px}}
@media (pointer:coarse){.ad .copy button{min-height:44px; padding-inline:14px}}

/* hero: 7/5, the photo takes the height of the text */
.ad-phero.phero--split .wrap{grid-template-columns:repeat(12,minmax(0,1fr)); gap:var(--gap); align-items:stretch}
.ad-phero h1{font-size:clamp(2.4rem,5.2vw,4.7rem)}
.ad-phero--long h1{font-size:clamp(2rem,3.75vw,2.9rem)}
.ad-phero .ad-txt{display:flex; flex-direction:column; justify-content:center}
.ad-phero .lede{margin-bottom:1.3em}
.ad-phero .phero__media{position:relative; align-self:stretch; min-height:clamp(300px,29vw,400px)}
.ad-phero.phero--split .phero__media img{position:absolute; inset:0; width:100%; height:100%; aspect-ratio:auto; object-fit:cover}
.ad-phero.phero--split .phero__media .sticker{left:-14px; bottom:26px}
.ad-phero .phero__wm{right:-14%; bottom:-46%}
.phero--logo .crumbs{color:rgba(255,255,255,.9)}
@media (max-width:900px){
  .ad-phero.phero--split .wrap{display:flex; flex-direction:column; gap:0}
  .ad-phero .ad-txt{display:contents}
  .ad-phero .ad-txt > *{order:3}
  .ad-phero .ad-txt > :is(.crumbs,.eyebrow,h1){order:1}
  .ad-phero .ad-txt > .eyebrow{align-self:flex-start}
  .ad-phero.phero--split .phero__media{order:2; align-self:stretch; width:100%; max-width:none; min-height:0; aspect-ratio:4/3; margin-block:6px 26px}
  .ad-phero.phero--split .phero__media .sticker{left:10px}
}
@media (max-width:520px){.ad-phero h1{font-size:clamp(2rem,10.4vw,2.6rem)} .ad-phero--long h1{font-size:clamp(1.8rem,8.8vw,2.4rem)}}

/* Vibe Check: full teal band */
.ad-vibe{align-items:center}
.ad-vmark{display:flex; align-items:center; gap:12px; font-family:var(--display); font-weight:900; font-stretch:115%; font-size:1.2rem; color:#fff; margin-bottom:16px}
.ad-vmark .daisy{width:38px; height:38px; color:var(--mint)}
.ad-vibe h2{font-size:clamp(2.1rem,4vw,3.5rem); font-stretch:112%; font-weight:900; letter-spacing:-.02em; overflow-wrap:break-word}
.ad-vibe .lede{color:#fff}
.ad-vibe p{color:#fff}
.ad-vibe .btns{margin-top:26px}
.ad-vibe .arrow-link{color:#fff; min-height:48px; padding-inline:6px}
.ad-vibe .arrow-link::after{color:var(--mint)}
.ad-never{display:inline-block; font-family:var(--display); font-weight:900; font-stretch:115%; font-size:clamp(1.3rem,2.2vw,1.8rem); line-height:1.1; text-transform:uppercase; background:var(--mint); color:var(--slate)!important; padding:.42em .6em .36em; border-radius:8px; transform:rotate(-1.5deg); box-shadow:4px 4px 0 var(--slate); margin:6px 0 22px}
.ad-places{margin:22px 0 0}
.ad-places .ad-mini{color:#fff; margin-bottom:10px}
.ad-places ul{list-style:none; margin:0; padding:0; display:grid; grid-template-columns:repeat(3,minmax(0,1fr)); gap:12px}
.ad-places li{margin:0; background:var(--slate-deep); border-radius:14px; padding:15px 18px; font-family:var(--display); font-stretch:106%; font-weight:800; font-size:1.08rem; line-height:1.25; color:var(--mint); display:flex; align-items:center}
.ad-phonewrap{position:relative; width:min(100%,400px); margin-inline:auto}
.ad-phone{position:relative; width:86%; margin-inline:auto; aspect-ratio:390/800; border-radius:46px; border:11px solid #0b1f25; background:#0b1f25; box-shadow:0 50px 90px -30px rgba(0,0,0,.6); overflow:hidden; transform:rotate(4deg)}
.ad-phone img{width:100%; height:100%; object-fit:cover; object-position:top}
.ad-phonewrap .sticker{position:absolute; z-index:2}
@media (max-width:900px){.ad-phonewrap{width:min(78%,300px)}}
@media (max-width:620px){.ad-places ul{grid-template-columns:minmax(0,1fr)}}
@media (max-width:520px){.ad-vibe h2{font-size:1.95rem; font-stretch:108%}}

/* date chip (college AI line) */
.ad-date{position:absolute; left:18px; top:18px; width:92px; border-radius:14px; overflow:hidden; text-align:center; background:#fff; color:var(--slate); border:2.5px solid var(--slate); box-shadow:4px 4px 0 var(--slate); transform:rotate(-3deg)}
.ad-date b{display:block; background:var(--slate); color:var(--mint); font-family:var(--mono); font-size:.74rem; letter-spacing:.14em; padding:5px 0 4px}
.ad-date span{display:block; font-family:var(--display); font-weight:900; font-stretch:115%; font-size:1.55rem; line-height:1; padding:10px 4px 11px; letter-spacing:-.02em}

/* link tiles on a dark band (chip-in and fundraise) */
.ad-acts4{display:grid; grid-template-columns:repeat(4,minmax(0,1fr)); gap:var(--gap)}
.ad-acts4 a{display:flex; flex-direction:column; gap:8px; padding:22px 22px 18px; border-radius:16px; background:rgba(255,255,255,.06); border:1px solid var(--line-dark); text-decoration:none; min-width:0; transition:background .2s, border-color .2s, transform .2s var(--ease)}
.ad-acts4 b{font-family:var(--display); font-weight:800; font-stretch:108%; font-size:clamp(1.12rem,1.6vw,1.3rem); line-height:1.15; color:#fff; overflow-wrap:anywhere}
.ad-acts4 span{color:rgba(255,255,255,.86); font-size:.98rem; line-height:1.45}
.ad-acts4 i{font-style:normal; margin-top:auto; padding-top:14px; display:flex; align-items:center; justify-content:space-between; gap:10px; font-family:var(--mono); font-size:.74rem; letter-spacing:.08em; text-transform:uppercase; font-weight:600; color:var(--mint)}
.ad-acts4 i::after{content:"\2192"; flex:none; width:38px; height:38px; border-radius:50%; display:grid; place-items:center; background:rgba(209,254,255,.14); font-family:var(--body); font-size:1rem; font-weight:800; transition:background .2s, color .2s, transform .2s var(--ease)}
.ad-acts4 a[target] i::after{content:"\2197"}
.ad-acts4 a:hover{background:rgba(21,255,200,.1); border-color:var(--mint); transform:translateY(-3px)}
.ad-acts4 a:hover i::after{background:var(--mint); color:var(--slate)}
@media (max-width:1100px){.ad-acts4{grid-template-columns:repeat(2,minmax(0,1fr))} .ad-acts4 b{font-size:1.3rem}}
@media (max-width:520px){.ad-acts4{grid-template-columns:minmax(0,1fr)} .ad-acts4 a{padding:18px 18px 14px}}

/* the giving card: what shows where the Zeffy form cannot load */
.ad-zeffy,.ad-zeffy .embed{display:flex; flex-direction:column; flex:1 1 auto; min-width:0}
.ad-zeffy:has(iframe){flex:none; background:#fff; border:1px solid var(--line); border-radius:var(--r-xl); box-shadow:var(--shadow-soft); padding:10px}
.ad-zeffy iframe{display:block}
.embed__fallback{flex:1 1 auto; display:flex; flex-direction:column}
.ad-gcard{position:relative; overflow:hidden; flex:1 1 auto; display:flex; flex-direction:column; gap:14px; background:var(--slate) var(--grain); color:#fff; border-radius:var(--r-xl); padding:clamp(24px,2.7vw,36px); box-shadow:var(--shadow-soft)}
.ad-gcard > *{position:relative; z-index:1}
.ad-gcard > .daisy-art{position:absolute; z-index:0; right:-38%; bottom:-34%; width:118%; color:var(--mint); opacity:.13}
.ad-gcard .ad-mini{color:var(--mint)}
.ad-gcard h3{font-size:clamp(1.5rem,2.2vw,1.9rem); margin:0; color:#fff}
.ad-gcard p{margin:0; color:rgba(255,255,255,.9)}
.ad .ad-gcard a:not(.btn){color:var(--mint); font-weight:700}
.ad-gcard .btn{align-self:stretch; min-height:54px; font-size:1.08rem; margin-top:6px}
.ad-gcard__alt{margin-top:auto; padding-top:10px}
.ad-gcard__alt .ad-mini{margin-bottom:10px}
.ad-gcard__alt ul{list-style:none; margin:0; padding:0; border-top:1px solid var(--line-dark)}
.ad-gcard__alt li{margin:0; border-bottom:1px solid var(--line-dark)}
.ad-gcard__alt li:last-child{border-bottom:0}
.ad .ad-gcard .ad-gcard__alt a{display:flex; align-items:center; justify-content:space-between; gap:12px; min-height:46px; padding:6px 2px; color:#fff; font-weight:700; text-decoration:none; transition:padding .2s var(--ease), color .2s}
.ad-gcard__alt a::after{content:"\2192"; color:var(--mint); transition:transform .2s var(--ease)}
.ad-gcard__alt a[target]::after{content:"\2197"}
.ad .ad-gcard .ad-gcard__alt a:hover{color:var(--mint); padding-inline:8px 2px}
.ad-gcard__alt a:hover::after{transform:translateX(3px)}
.ad-fee{display:none; margin:10px 8px 6px; font-size:.9rem; line-height:1.4; text-align:center; color:var(--ink-soft)}
.ad-zeffy:has(iframe) .ad-fee{display:block}
.ad-zeffy .embed:has(iframe){flex:none}

/* =====================================================================
   educators.html
   ===================================================================== */
/* the staircase: one more block at each level of use */
#levels .section-head{margin-bottom:28px}
.ad-stairs{display:grid; grid-template-columns:repeat(4,minmax(0,1fr)); gap:10px; align-items:end}
.ad-stair{font:inherit; color:var(--slate); text-align:left; background:none; border:0; padding:0; cursor:pointer; display:flex; flex-direction:column; gap:12px; min-width:0; border-radius:10px}
.ad-stair__txt{display:block; padding:0 4px}
.ad-stair small{display:block; font-family:var(--mono); font-size:.72rem; letter-spacing:.08em; text-transform:uppercase; font-weight:600; color:var(--logo-teal); line-height:1.3; margin-bottom:6px}
.ad-stair b{display:block; font-family:var(--display); font-weight:800; font-stretch:110%; font-size:clamp(1.15rem,1.75vw,1.5rem); line-height:1.12}
.ad-stair b span{background:linear-gradient(transparent 62%, var(--mint) 62% 94%, transparent 94%) no-repeat 0 0 / 0% 100%; padding:0 .06em; -webkit-box-decoration-break:clone; box-decoration-break:clone; transition:background-size .45s var(--ease)}
.ad-stair[aria-selected="true"] b span{background-size:100% 100%}
.ad-stair__blocks{display:flex; flex-direction:column-reverse; gap:5px}
.ad-stair__blocks i{display:block; height:24px; border-radius:8px; background:var(--aqua); box-shadow:inset 0 0 0 1.5px rgba(19,132,143,.3); transition:background .3s var(--ease), box-shadow .3s}
.ad-stair__blocks i:nth-child(2){transition-delay:.06s} .ad-stair__blocks i:nth-child(3){transition-delay:.12s} .ad-stair__blocks i:nth-child(4){transition-delay:.18s}
.ad-stair:hover .ad-stair__blocks i{background:rgba(19,132,143,.34)}
.ad-stair[aria-selected="true"] .ad-stair__blocks i{background:var(--slate); box-shadow:none}
.ad-stair[aria-selected="true"] .ad-stair__blocks i:last-child{box-shadow:inset 0 7px 0 var(--mint)}
.ad-axis{display:flex; justify-content:space-between; gap:12px; font-family:var(--mono); font-size:.74rem; letter-spacing:.08em; text-transform:uppercase; font-weight:500; color:var(--ink-soft); margin:5px 0 var(--gap); padding:10px 14px 0 0; border-top:3px solid var(--slate); position:relative}
.ad-axis::after{content:""; position:absolute; right:1px; top:-9px; width:13px; height:13px; border-top:3px solid var(--slate); border-right:3px solid var(--slate); transform:rotate(45deg)}
@media (max-width:760px){
  .ad-stairs{grid-template-columns:minmax(0,1fr); gap:8px}
  .ad-stair{flex-direction:row; align-items:center; justify-content:space-between; gap:14px; min-height:64px; padding:10px 16px; border:2px solid var(--line); border-radius:14px; background:#fff}
  .ad-stair__txt{padding:0}
  .ad-stair small{margin-bottom:3px}
  .ad-stair__blocks{flex-direction:row; gap:4px; flex:none; width:68px}
  .ad-stair__blocks i{width:14px; height:26px; border-radius:4px}
  .ad-stair[aria-selected="true"]{background:var(--slate); border-color:var(--slate); color:#fff}
  .ad-stair[aria-selected="true"] small{color:var(--mint)}
  .ad-stair[aria-selected="true"] b span{background:none}
  .ad-stair[aria-selected="true"] .ad-stair__blocks i, .ad-stair[aria-selected="true"] .ad-stair__blocks i:last-child{background:var(--mint); box-shadow:none}
  .ad-axis{display:none}
  .ad-stairs{margin-bottom:var(--gap)}
}
/* the panel for the chosen level */
.ad-level{background:var(--mist); border:1px solid var(--line); border-radius:var(--r-xl); padding:clamp(20px,3vw,40px)}
.ad-level h3{font-size:clamp(1.6rem,2.6vw,2.2rem); margin-bottom:.4em}
.ad-level p{margin:0; font-size:1.06rem}
.ad-level__fits{display:flex; flex-wrap:wrap; align-items:center; gap:8px 14px; margin-top:18px}
.ad-level .chips{gap:8px}
.ad-level .chip{background:#fff; border:1px solid var(--line); font-size:.74rem; padding:.5em .75em; white-space:normal}
.ad-level__acts{display:flex; flex-direction:column; justify-content:flex-end; gap:12px}
.ad-level__acts .btn{width:100%}
.ad-level .ad-col .chips{margin-top:18px}
@media (max-width:900px){.ad-level__acts{flex-direction:row; flex-wrap:wrap; justify-content:flex-start; margin-top:4px} .ad-level__acts .btn{width:auto}}
/* teaching guides stand on a shelf */
.ad-shelf{display:grid; grid-template-columns:repeat(8,minmax(0,1fr)); gap:clamp(8px,1.1vw,16px); align-items:end; margin-top:clamp(26px,3.2vw,40px); padding:0 clamp(6px,1.2vw,18px); border-bottom:8px solid var(--slate); border-radius:0 0 5px 5px}
.ad-book{position:relative; display:flex; flex-direction:column; aspect-ratio:587/917; border-radius:5px 5px 0 0; background:var(--slate); box-shadow:0 18px 22px -18px rgba(22,53,64,.85); transition:transform .3s var(--ease); transform-origin:50% 100%; text-decoration:none}
.ad .ad-book{color:#fff}
.ad-book img{flex:1 1 auto; min-height:0; width:100%; height:100%; object-fit:cover; border-radius:inherit; display:block}
.ad-book:hover,.ad-book:focus-visible{transform:translateY(-10px) rotate(-1.5deg); z-index:2}
.ad-book__tip{position:absolute; left:50%; bottom:calc(100% + 10px); transform:translate(-50%,6px); background:var(--slate); color:#fff; font-family:var(--display); font-weight:700; font-stretch:104%; font-size:.92rem; line-height:1.25; padding:8px 12px; border-radius:10px; width:max-content; max-width:230px; text-align:center; opacity:0; pointer-events:none; transition:opacity .2s, transform .2s var(--ease); z-index:3}
.ad-book:hover .ad-book__tip,.ad-book:focus-visible .ad-book__tip{opacity:1; transform:translate(-50%,0)}
.ad-book--rr{overflow:hidden}
.ad-book--rr img{flex:1 1 0; height:0; object-position:50% 12%; border-radius:0}
.ad-book__bar{flex:none; display:block; padding:9px 9px 10px; background:var(--slate-deep); border-top:3px solid var(--mint)}
.ad-book__bar small{display:block; font-family:var(--mono); font-size:.7rem; letter-spacing:.06em; text-transform:uppercase; color:var(--mint); margin-bottom:4px; line-height:1.2}
.ad-book__bar b{display:block; font-family:var(--display); font-weight:800; font-size:clamp(.875rem,1.05vw,.95rem); line-height:1.15}
.ad-book:nth-child(-n+2) .ad-book__tip{left:0; transform:translate(0,6px)} .ad-book:nth-child(-n+2):is(:hover,:focus-visible) .ad-book__tip{transform:none}
.ad-book:nth-last-child(-n+3) .ad-book__tip{left:auto; right:0; transform:translate(0,6px)} .ad-book:nth-last-child(-n+3):is(:hover,:focus-visible) .ad-book__tip{transform:none}
@media (hover:none){.ad-book__tip{display:none}}
@media (max-width:860px){.ad-shelf{grid-template-columns:repeat(4,minmax(0,1fr)); row-gap:0; border-bottom:0; padding:0} .ad-book{margin-bottom:16px; box-shadow:0 7px 0 var(--slate), 0 22px 22px -16px rgba(22,53,64,.7)} .ad-book__tip{display:none} .ad-book__bar{padding:6px 6px 7px} .ad-book__bar small{display:none} .ad-book__bar b{font-size:.875rem; font-stretch:72%; line-height:1.12; letter-spacing:.01em}}
/* posters: one row, one height */
.ad-prow{display:flex; gap:clamp(8px,1.1vw,16px); margin-top:clamp(26px,3.2vw,40px)}
.ad-prow__g{display:flex; gap:clamp(8px,1.1vw,16px); min-width:0}
.ad-prow button{flex:var(--ar) 1 0%; min-width:0; border:0; padding:0; background:#fff; border-radius:10px; overflow:hidden; cursor:zoom-in; box-shadow:0 16px 26px -18px rgba(22,53,64,.75); transition:transform .25s var(--ease)}
.ad-prow button:hover{transform:translateY(-5px) rotate(-1deg)}
.ad-prow img{display:block; width:100%; height:auto; aspect-ratio:var(--ar)}
.ad-level__hint{margin:14px 0 0!important; font-family:var(--mono); font-size:.74rem!important; letter-spacing:.08em; text-transform:uppercase; color:var(--ink-soft)}
@media (max-width:700px){.ad-prow{flex-direction:column}}
/* curriculum photo, 360 ring */
.ad-level .fill-img{min-height:300px}
.ad-level .fill-img img{object-position:40% 40%}
.ad-ringwrap{display:grid; grid-template-columns:minmax(0,236px) minmax(0,1fr); gap:clamp(18px,2.6vw,36px); align-items:center}
.ad-ringwrap svg{width:100%; display:block; overflow:visible}
.ad-ringwrap ol{list-style:none; counter-reset:c; margin:0; padding:0; border-top:1px solid var(--line)}
.ad-ringwrap li{counter-increment:c; margin:0; border-bottom:1px solid var(--line)}
.ad-ringwrap li a{display:grid; grid-template-columns:30px minmax(0,1fr) auto; gap:8px; align-items:center; min-height:46px; padding:8px 4px; font-weight:700; font-size:.98rem; line-height:1.3; color:var(--logo-teal); text-decoration:none; transition:background .15s, padding .2s var(--ease)}
.ad-ringwrap li a::before{content:counter(c); font-family:var(--display); font-weight:900; font-stretch:115%; font-size:1.2rem; color:var(--teal)}
.ad-ringwrap li a::after{content:"\2192"; color:var(--teal); transition:transform .2s var(--ease)}
.ad-ringwrap li a:hover{background:#fff; padding-inline:10px}
.ad-ringwrap li a:hover::after{transform:translateX(3px)}
@media (max-width:560px){.ad-ringwrap{grid-template-columns:minmax(0,1fr)} .ad-ringwrap svg{max-width:240px; margin-inline:auto}}
/* request */
.ad-req{align-items:stretch}
.ad-req .ad-checks{margin-top:4px}
.ad-req__new{grid-column:1/-1; margin-top:clamp(8px,1.4vw,18px)}
.ad-req__new .ad-mini{margin-bottom:10px}
.ad-req__new > div{display:grid; grid-template-columns:repeat(2,minmax(0,1fr)); gap:var(--gap)}
.ad-req__new a{position:relative; display:flex; flex-direction:column; gap:4px; padding:18px 70px 18px 22px; border-radius:14px; background:#fff; border:1px solid var(--line); text-decoration:none; color:var(--slate); min-width:0; transition:border-color .2s, transform .2s var(--ease)}
.ad-req__new em{font-style:normal; font-family:var(--mono); font-size:.72rem; letter-spacing:.1em; text-transform:uppercase; font-weight:600; color:var(--teal)}
.ad-req__new b{font-family:var(--display); font-weight:800; font-stretch:106%; font-size:1.15rem; line-height:1.15; color:var(--logo-teal)}
.ad-req__new small{font-size:.95rem; line-height:1.4; color:var(--ink-soft)}
.ad-req__new i{position:absolute; right:20px; top:50%; margin-top:-20px; width:40px; height:40px; border-radius:50%; display:grid; place-items:center; font-style:normal; font-weight:800; background:var(--aqua); color:var(--logo-teal); transition:background .2s, transform .2s var(--ease)}
.ad-req__new a:hover{border-color:var(--teal); transform:translateY(-2px)}
.ad-req__new a:hover i{background:var(--mint); transform:translateX(3px)}
@media (max-width:900px){.ad-req__new{margin-top:var(--gap)}}
@media (max-width:620px){.ad-req__new > div{grid-template-columns:minmax(0,1fr)}}
.ad-card{color:var(--slate); background:#fff; border-radius:var(--r-xl); box-shadow:var(--shadow-soft); padding:var(--pad-card); display:flex; flex-direction:column}
.ad .ad-card a:not(.btn){color:var(--logo-teal)}
.ad-form{flex:1 1 auto; grid-template-rows:auto auto minmax(0,1fr) auto}
.ad-form__row{display:grid; grid-template-columns:1fr 1fr; gap:14px}
.ad-form__grow{display:flex; flex-direction:column}
.ad-form__grow textarea{flex:1 1 auto; min-height:120px}
.ad-form.sent{grid-template-rows:auto auto minmax(0,1fr) auto auto}
@media (max-width:560px){.ad-form__row{grid-template-columns:1fr}}

/* =====================================================================
   college.html
   ===================================================================== */
.ad-fig{margin:0; display:flex; flex-direction:column; border-radius:var(--r-xl); overflow:hidden; background:var(--slate); box-shadow:var(--shadow-soft); min-width:0}
.ad-fig__img{position:relative; flex:1 1 auto; min-height:230px}
.ad-fig__img img{position:absolute; inset:0; width:100%; height:100%; object-fit:cover; object-position:64% 40%}
.ad-fig figcaption{padding:18px 22px 20px; border-top:4px solid var(--mint); color:#fff; font-family:var(--display); font-stretch:104%; font-weight:700; font-size:1.15rem; line-height:1.35}
/* the bridge: what a mentor and a high school build together */
.ad-bridge{margin-top:var(--gap); background:var(--mist); border:1px solid var(--line); border-radius:var(--r-xl); padding:var(--pad-card)}
.ad-bridge > .ad-mini{margin-bottom:14px}
.ad-bridge__in{display:grid; grid-template-columns:repeat(12,minmax(0,1fr)); align-items:stretch}
.ad-bridge__end{grid-column:span 3; display:flex; flex-direction:column; justify-content:center; gap:6px; border-radius:16px; padding:20px 22px; background:var(--slate); color:#fff; min-width:0}
.ad-bridge__end small{font-family:var(--mono); font-size:.72rem; letter-spacing:.1em; text-transform:uppercase; font-weight:600; color:var(--mint)}
.ad-bridge__end b{font-family:var(--display); font-weight:900; font-stretch:112%; font-size:clamp(1.3rem,2.1vw,1.75rem); line-height:1.05}
.ad-bridge__end--hs{background:var(--mint); color:var(--slate)}
.ad-bridge__end--hs small{color:var(--logo-teal)}
.ad-bridge__lanes{grid-column:span 6; list-style:none; margin:0; padding:6px 0; display:grid; gap:12px; align-content:center}
.ad-bridge__lanes li{position:relative; margin:0; display:flex; justify-content:center; align-items:center; min-height:54px}
.ad-bridge__lanes li::before{content:""; position:absolute; left:0; right:12px; top:50%; margin-top:-1.5px; border-top:3px dashed var(--slate); transform-origin:0 50%; transition:transform 1s var(--ease)}
.ad-bridge__lanes li::after{content:""; position:absolute; right:3px; top:50%; width:13px; height:13px; margin-top:-6.5px; border-top:3px solid var(--slate); border-right:3px solid var(--slate); transform:rotate(45deg); transition:opacity .3s .9s}
.ad-bridge__lanes li:nth-child(2)::before{transition-delay:.18s} .ad-bridge__lanes li:nth-child(3)::before{transition-delay:.36s}
.ad-bridge__lanes li:nth-child(2)::after{transition-delay:1.08s} .ad-bridge__lanes li:nth-child(3)::after{transition-delay:1.26s}
.ad-bridge__lanes span{position:relative; z-index:1; background:#fff; border:2.5px solid var(--slate); border-radius:999px; padding:9px 22px 8px; font-family:var(--display); font-weight:800; font-stretch:106%; font-size:clamp(1rem,1.4vw,1.15rem); line-height:1.2; text-align:center; box-shadow:3px 3px 0 var(--slate); transition:transform .5s var(--ease), opacity .4s}
.js .ad-bridge:not(.in) .ad-bridge__lanes li::before{transform:scaleX(0)}
.js .ad-bridge:not(.in) .ad-bridge__lanes li::after{opacity:0}
.js .ad-bridge:not(.in) .ad-bridge__lanes span{transform:scale(.92); opacity:0}
.ad-bridge__lanes li:nth-child(1) span{transition-delay:.3s} .ad-bridge__lanes li:nth-child(2) span{transition-delay:.48s} .ad-bridge__lanes li:nth-child(3) span{transition-delay:.66s}
@media (max-width:760px){
  .ad-bridge__in{grid-template-columns:minmax(0,1fr)}
  .ad-bridge__end,.ad-bridge__lanes{grid-column:auto}
  .ad-bridge__end{padding:16px 18px}
  .ad-bridge__lanes{padding:22px 0; gap:10px; position:relative}
  .ad-bridge__lanes::before{content:""; position:absolute; left:50%; top:0; bottom:0; margin-left:-1.5px; border-left:3px dashed var(--slate)}
  .ad-bridge__lanes li{min-height:0}
  .ad-bridge__lanes li::before,.ad-bridge__lanes li::after{display:none}
}
.ad-mail{margin-top:var(--gap); display:flex; flex-wrap:wrap; gap:14px 20px; align-items:center; background:var(--slate); color:#fff; border-radius:var(--r-xl); padding:20px var(--pad-card)}
.ad-mail b{font-family:var(--display); font-stretch:108%; font-weight:800; font-size:1.3rem; line-height:1.2; flex:1 1 300px; min-width:0}
/* campus club */
.ad-campus .fill-img{min-height:320px}
.ad-campus .fill-img img{object-position:62% 70%}
.ad-campus .lede{color:rgba(255,255,255,.92)}
.ad-campus p{color:rgba(255,255,255,.88)}
.ad-provide{margin-top:6px}
.ad-provide .ad-mini{margin-bottom:10px}
.ad-provide ul{list-style:none; margin:0; padding:0; display:grid; grid-template-columns:repeat(3,minmax(0,1fr)); gap:12px}
.ad-provide li{margin:0; padding:15px 18px; border-radius:14px; background:rgba(255,255,255,.06); border:1px solid var(--line-dark); border-left:5px solid var(--mint); font-family:var(--display); font-stretch:108%; font-weight:800; font-size:1.15rem; line-height:1.2; color:#fff; display:flex; align-items:center}
@media (max-width:520px){.ad-provide ul{grid-template-columns:minmax(0,1fr)}}
/* certification */
.ad-cert .player{border-radius:var(--r-xl)}
.ad-prio{flex:1 1 auto; background:var(--mint); color:var(--slate); border-radius:var(--r-xl); padding:var(--pad-card); display:flex; flex-direction:column; justify-content:center; gap:8px}
.ad-prio b{font-family:var(--display); font-weight:900; font-stretch:110%; font-size:clamp(1.5rem,2.5vw,2.15rem); line-height:1.06; letter-spacing:-.01em}
.ad-prio p{margin:0; font-size:1.15rem; font-weight:600; line-height:1.4}
.ad-facts{list-style:none; margin:var(--gap) 0 0; padding:0; display:grid; grid-template-columns:repeat(3,minmax(0,1fr)); gap:12px}
.ad-facts li{margin:0; border:1px solid var(--line); border-radius:14px; padding:14px 16px; background:var(--mist); font-family:var(--display); font-stretch:108%; font-weight:800; font-size:1.2rem; line-height:1.15; color:var(--logo-teal); display:flex; align-items:center}
.ad-cert .ad-col > .btns:last-child{padding-top:var(--gap)}
@media (max-width:520px){.ad-facts{grid-template-columns:repeat(3,auto); gap:8px} .ad-facts li{padding:12px 12px; font-size:1.05rem; white-space:nowrap}}
/* AI Literacy Training: one line under the certification */
.ad-ailine{margin-top:var(--gap); display:grid; grid-template-columns:auto minmax(0,1fr) auto; gap:16px 26px; align-items:center; padding:18px var(--pad-card) 18px 18px; border-radius:var(--r-xl); background:var(--mist); border:1px solid var(--line)}
.ad-ailine .ad-date{position:static; transform:rotate(-3deg); width:96px}
.ad-ailine .ad-date span{white-space:nowrap; font-size:1.45rem}
.ad-ailine p{margin:0; line-height:1.5}
.ad-ailine p b{font-family:var(--display); font-stretch:106%; color:var(--logo-teal)}
@media (max-width:760px){.ad-ailine{grid-template-columns:auto minmax(0,1fr)} .ad-ailine .btn{grid-column:1/-1; justify-self:start}}

/* =====================================================================
   donate.html
   ===================================================================== */
.ad-phero .ad-dphoto{align-self:center; aspect-ratio:5/4; min-height:0}
.ad-dphoto img{object-position:50% 30%}
.ad-phero.phero--split .ad-dphoto .sticker--r{left:auto; right:-10px; bottom:auto; top:22px}
/* the giving desk: fallback = head / (funds 7 | card 5) / proof; live = (head, funds, proof) 7 | form 5 */
.ad-give{display:grid; grid-template-columns:repeat(12,minmax(0,1fr)); gap:var(--gap)}
.ad-give > *{min-width:0}
.ad-give__head{grid-column:1/-1; grid-row:1; margin-bottom:calc(var(--head-gap) - var(--gap))}
.ad-give__head h2{margin:0}
.ad-give__head .lede{margin:.5em 0 0}
.ad-give__funds{grid-column:1/8; grid-row:2; display:flex; flex-direction:column}
.ad-give__funds > .ad-mini{margin-bottom:12px}
.ad-give__form{grid-column:8/-1; grid-row:2; display:flex; flex-direction:column}
.ad-give__proof{grid-column:1/-1; grid-row:3}
.ad-give:has(.embed iframe){grid-template-rows:auto minmax(0,1fr) auto}
.ad-give:has(.embed iframe) .ad-give__head{grid-column:1/8; grid-row:1; margin-bottom:0}
.ad-give:has(.embed iframe) .ad-give__funds{grid-row:2}
.ad-give:has(.embed iframe) .ad-give__proof{grid-column:1/8; grid-row:3}
.ad-give:has(.embed iframe) .ad-give__form{grid-row:1/4}
.ad-ft{list-style:none; margin:0; padding:0; flex:1 1 auto; display:grid; grid-template-columns:repeat(2,minmax(0,1fr)); grid-template-rows:minmax(118px,1fr) auto minmax(118px,1fr) auto; gap:0 var(--gap)}
.ad-ft li{margin:0; display:grid; grid-template-rows:subgrid; grid-row:span 2; border-radius:16px; overflow:hidden; background:var(--slate); color:#fff; min-width:0}
.ad-ft li:nth-child(n+3){margin-top:var(--gap)}
.ad-ft__img{position:relative; display:block; background:var(--slate-deep); overflow:hidden}
.ad-ft__img img{position:absolute; inset:0; width:100%; height:100%; object-fit:cover; transition:transform .6s var(--ease)}
.ad-ft li:hover .ad-ft__img img{transform:scale(1.04)}
.ad-ft__cap{display:block; padding:13px 16px 15px; border-top:3px solid var(--mint); font-weight:600; font-size:.98rem; line-height:1.35}
.ad-proof{display:grid; grid-template-columns:repeat(3,minmax(0,1fr)); border:1px solid var(--line); border-top:6px solid var(--mint); border-radius:var(--r-xl); background:var(--mist); overflow:hidden}
.ad-proof > div{padding:clamp(20px,2.1vw,28px) clamp(20px,2.1vw,30px); border-left:1px solid var(--line); min-width:0; display:flex}
.ad-proof > div:first-child{border-left:0}
.ad-proof__stat{flex-direction:column; justify-content:center; gap:8px}
.ad-proof__stat b{font-family:var(--display); font-weight:900; font-stretch:115%; font-size:clamp(2.6rem,4.6vw,4rem); line-height:.9; color:var(--logo-teal); letter-spacing:-.02em; font-variant-numeric:tabular-nums}
.ad-proof__stat span{font-weight:600; line-height:1.35}
.ad-proof__trust{gap:16px; align-items:center}
.ad-proof__trust img{width:64px; height:64px; flex:none; border-radius:8px}
.ad-proof__trust > div{display:flex; flex-wrap:wrap; align-items:center; gap:10px 18px; min-width:0}
.ad-proof__trust p{margin:0; font-size:.95rem; line-height:1.45; flex:1 1 250px; min-width:0}
.ad-proof__more{flex-direction:column; justify-content:center; gap:10px}
.ad-proof__more p{margin:0; line-height:1.45}
.ad-give:has(.embed iframe) .ad-proof{grid-template-columns:minmax(0,1fr)}
.ad-give:has(.embed iframe) .ad-proof > div{border-left:0; border-top:1px solid var(--line)}
.ad-give:has(.embed iframe) .ad-proof > div:first-child{border-top:0}
.ad-give:has(.embed iframe) .ad-proof__stat{flex-direction:row; align-items:center; justify-content:flex-start; gap:18px}
.ad-give:has(.embed iframe) .ad-proof__more{flex-direction:row; flex-wrap:wrap; justify-content:flex-start; gap:6px 30px}
@media (max-width:900px){
  .ad-give, .ad-give:has(.embed iframe){grid-template-columns:minmax(0,1fr); grid-template-rows:none}
  .ad-give > *, .ad-give:has(.embed iframe) > *{grid-column:auto!important; grid-row:auto!important}
  .ad-give__head{margin-bottom:0; order:1} .ad-give__form{order:2} .ad-give__funds{order:3} .ad-give__proof{order:4}
  .ad-proof, .ad-give:has(.embed iframe) .ad-proof{grid-template-columns:minmax(0,1fr)}
  .ad-proof > div{border-left:0; border-top:1px solid var(--line)} .ad-proof > div:first-child{border-top:0}
  .ad-proof__stat{flex-direction:row; align-items:center; gap:16px}
}
@media (max-width:520px){
  .ad-ft{grid-template-columns:minmax(0,1fr); grid-template-rows:none; gap:10px}
  .ad-ft li{grid-template-rows:none; grid-row:auto; grid-template-columns:38% minmax(0,1fr)}
  .ad-ft li:nth-child(n+3){margin-top:0}
  .ad-ft__img{min-height:96px}
  .ad-ft__cap{border-top:0; border-left:3px solid var(--mint); align-self:center; padding:12px 14px}
  .ad-ft li{align-items:stretch}
}
/* story */
.ad-story .fill-img{min-height:300px}
.ad-story .fill-img img{object-position:50% 45%}
.ad-story .btns{margin-top:24px}
/* more ways to give: list and panel end level */
.ad-ways{align-items:stretch}
.ad-ways__list{grid-column:span 5; display:grid; grid-auto-rows:1fr; gap:10px}
.ad-way{font:inherit; text-align:left; display:flex; align-items:center; justify-content:space-between; gap:14px; min-height:56px; padding:8px 12px 8px 20px; border-radius:14px; border:2px solid var(--line); background:#fff; color:var(--slate); cursor:pointer; transition:border-color .2s, background .2s, color .2s}
.ad-way b{font-family:var(--display); font-stretch:108%; font-weight:800; font-size:1.2rem; line-height:1.2}
.ad-way i{font-style:normal; flex:none; width:38px; height:38px; border-radius:50%; display:grid; place-items:center; background:var(--aqua); color:var(--logo-teal); font-weight:800; transition:background .2s, color .2s, transform .2s var(--ease)}
.ad-way:hover{border-color:var(--teal)}
.ad-way:hover i{transform:translateX(3px)}
.ad-way[aria-selected="true"]{background:var(--slate); color:#fff; border-color:var(--slate)}
.ad-way[aria-selected="true"] i{background:var(--mint); color:var(--slate)}
.ad-ways__panels{grid-column:span 7; display:flex; min-width:0}
.ad-wpanel{flex:1 1 auto; min-width:0; display:flex; flex-direction:column; background:var(--mist); border:1px solid var(--line); border-top:6px solid var(--mint); border-radius:var(--r-xl); padding:clamp(22px,3vw,40px)}
.ad-wpanel h3{font-size:clamp(1.6rem,2.6vw,2.2rem); margin:0 0 .35em}
.ad-wpanel__lede{font-family:var(--display); font-stretch:104%; font-weight:700; font-size:1.2rem; line-height:1.3; color:var(--logo-teal); margin:0 0 .8em}
.ad-wpanel p{margin:0 0 .8em}
.ad-wpanel ol{padding-left:1.3em; display:grid; gap:8px; margin:0}
.ad-wpanel ol li{margin:0}
.ad-wpanel .btns{margin-top:auto; padding-top:20px}
.ad-wpanel .muted{margin:auto 0 0; padding-top:14px}
.ad-addr{display:flex; flex-wrap:wrap; align-items:center; gap:14px 22px; margin:4px 0 0}
.ad-addr address{font-style:normal; font-family:var(--mono); font-weight:600; font-size:1.08rem; line-height:1.55; background:#fff; border:1px solid var(--line); border-radius:14px; padding:16px 22px}
@media (max-width:900px){.ad-ways__list,.ad-ways__panels{grid-column:auto} .ad-ways__list{grid-template-columns:repeat(2,minmax(0,1fr))}}
@media (max-width:560px){.ad-way{padding:8px 10px 8px 14px; gap:8px} .ad-way b{font-size:1.02rem} .ad-way i{width:30px; height:30px; font-size:.9rem}}
/* closing strip */
.ad-strip{margin-top:var(--gap); display:grid; grid-template-columns:minmax(0,1fr) auto; gap:16px 32px; align-items:center; background:var(--aqua); border-radius:var(--r-xl); padding:22px var(--pad-card)}
.ad-strip h3{font-size:clamp(1.3rem,2vw,1.6rem); margin:0 0 .2em}
.ad-strip p{margin:0; font-size:1.06rem; font-weight:500}
.ad-strip .btns{flex-wrap:nowrap}
@media (max-width:860px){.ad-strip{grid-template-columns:minmax(0,1fr)} .ad-strip .btns{flex-wrap:wrap}}

/* =====================================================================
   chip-in.html
   ===================================================================== */
.ad-chip h1{font-size:clamp(2.2rem,4.7vw,4.2rem); text-transform:none; font-stretch:116%; line-height:.98; letter-spacing:-.02em}
.ad-chip :focus-visible{outline-color:var(--teal)}
/* fallback = intro | card over photo; live = intro, impact, photo | form */
.ad-chip__grid{display:grid; grid-template-columns:repeat(12,minmax(0,1fr)); grid-template-rows:auto minmax(0,1fr) auto; gap:var(--gap)}
.ad-chip__grid > *{min-width:0}
.ad-chip__intro{grid-column:1/8; grid-row:1/3; padding-right:clamp(0px,calc(6vw - 46px),40px)}
.ad-chip__intro .lede{margin:0}
.ad-chip__impact{grid-column:1/8; grid-row:3; padding-right:clamp(0px,calc(6vw - 46px),40px)}
.ad-chip__form{grid-column:8/-1; grid-row:1; display:flex; flex-direction:column}
.ad-chip__photo{grid-column:8/-1; grid-row:2/4; min-height:280px}
.ad-chip__photo img{object-position:50% 38%}
.ad-chip__grid:has(.embed iframe){grid-template-rows:auto auto minmax(0,1fr)}
.ad-chip__grid:has(.embed iframe) .ad-chip__intro{grid-row:1}
.ad-chip__grid:has(.embed iframe) .ad-chip__impact{grid-row:2}
.ad-chip__grid:has(.embed iframe) .ad-chip__photo{grid-column:1/8; grid-row:3; min-height:200px; margin-right:clamp(0px,calc(6vw - 46px),40px)}
.ad-chip__grid:has(.embed iframe) .ad-chip__form{grid-row:1/4}
.ad-chip .ad-gcard .sticker{align-self:flex-start; margin-bottom:4px}
.ad-impact{list-style:none; padding:0; margin:12px 0 0; display:grid; gap:10px}
.ad-impact li{margin:0; background:#fff; border-radius:14px; padding:15px 18px 15px 56px; position:relative; border:1px solid var(--line); line-height:1.45; font-size:1.04rem}
.ad-impact li::before{content:""; position:absolute; left:16px; top:50%; width:26px; height:26px; margin-top:-13px; border-radius:50%; background:var(--mint) url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 24 24'%3E%3Cpath d='M6 12.5l4 4 8-9' fill='none' stroke='%231d414e' stroke-width='3' stroke-linecap='round' stroke-linejoin='round'/%3E%3C/svg%3E") center/15px no-repeat; transition:transform .5s var(--ease)}
.ad-impact strong{color:var(--logo-teal)}
.js .ad-impact:not(.in) li::before{transform:scale(0) rotate(-40deg)}
.ad-impact li:nth-child(2)::before{transition-delay:.14s} .ad-impact li:nth-child(3)::before{transition-delay:.28s} .ad-impact li:nth-child(4)::before{transition-delay:.42s}
@media (max-width:900px){
  .ad-chip__grid, .ad-chip__grid:has(.embed iframe){grid-template-columns:minmax(0,1fr); grid-template-rows:none}
  .ad-chip__grid > *, .ad-chip__grid:has(.embed iframe) > *{grid-column:auto!important; grid-row:auto!important; padding-right:0; margin-right:0}
  .ad-chip__photo{aspect-ratio:16/10; min-height:0!important}
}
/* the line the page turns on */
.ad-state .lede{color:rgba(255,255,255,.92)}
.ad-state .lede .mk{background:none; color:var(--mint); font-weight:700}

/* =====================================================================
   fundraise.html
   ===================================================================== */
.ad-pols{position:relative; align-self:center; grid-column:span 5; aspect-ratio:5/4; min-width:0; animation:sb-rise-r 1s .1s var(--ease) both}
.ad-pol{position:absolute; width:47%; background:#fff; padding:9px 9px 0; border-radius:4px; box-shadow:0 30px 50px -20px rgba(0,0,0,.6); text-decoration:none; transition:transform .35s var(--ease)}
.ad .ad-pol{color:var(--slate)}
.ad-pol__img{display:block; aspect-ratio:4/5; overflow:hidden; background:var(--aqua)}
.ad-pol img{width:100%; height:100%; object-fit:cover}
.ad-pol b{display:block; text-align:center; font-family:var(--display); font-weight:800; font-stretch:110%; font-size:clamp(1.05rem,1.5vw,1.3rem); line-height:1; padding:11px 0 13px}
.ad-pol:nth-child(1){left:0; top:11%; transform:rotate(-6deg)}
.ad-pol:nth-child(2){left:27%; top:0; transform:rotate(3deg); z-index:2}
.ad-pol:nth-child(3){right:0; top:17%; transform:rotate(-2deg)}
.ad-pol:hover,.ad-pol:focus-visible{transform:rotate(0) translateY(-8px); z-index:3}
.ad-pol--contain .ad-pol__img{background:var(--teal)}
.ad-pol--contain img{object-fit:contain}
.ad-pol--v img{transform:scale(1.42); transform-origin:50% 36%}
@media (max-width:900px){.ad-pols{order:2; width:min(100%,520px); margin:8px 0 30px}}
/* fundraiser tabs */
.ad-ptabs{display:flex; flex-wrap:wrap; gap:10px; margin-bottom:var(--gap)}
.ad-ptab{display:flex; align-items:center; gap:12px; font:inherit; font-family:var(--display); font-weight:800; font-stretch:106%; font-size:1.1rem; padding:6px 22px 6px 6px; border-radius:999px; border:2px solid var(--line); background:#fff; color:var(--slate); cursor:pointer; transition:background .2s, border-color .2s, color .2s}
.ad-ptab span{width:44px; height:44px; border-radius:50%; overflow:hidden; background:var(--aqua); flex:none; display:block}
.ad-ptab img{width:100%; height:100%; object-fit:cover}
.ad-ptab--v img{transform:scale(1.5); transform-origin:48% 30%}
.ad-ptab:hover{border-color:var(--teal)}
.ad-ptab[aria-selected="true"]{background:var(--slate); color:#fff; border-color:var(--slate)}
/* fallback = photo 5 | story, give card, Venmo 7; live = photo, story, Venmo 5 | form 7 */
.ad-fr{display:grid; grid-template-columns:repeat(12,minmax(0,1fr)); grid-template-rows:auto auto minmax(0,1fr); gap:var(--gap)}
.ad-fr > *{min-width:0}
.ad-fr__photo{grid-column:1/6; grid-row:1/4; position:relative; margin:0; border-radius:var(--r-xl); overflow:hidden; background:var(--slate); min-height:340px}
.ad-fr__photo img{position:absolute; inset:0; width:100%; height:100%; object-fit:cover}
.ad-fr__photo--print{background:var(--aqua); --pp:clamp(20px,2.6vw,34px)}
.ad-fr__photo--print img{inset:var(--pp); width:calc(100% - 2*var(--pp)); height:calc(100% - 2*var(--pp)); object-fit:contain; transform:rotate(-2.5deg); filter:drop-shadow(0 18px 20px rgba(22,53,64,.34))}
.ad-fr__txt{grid-column:6/-1; grid-row:1; padding-left:clamp(0px,calc(3vw - 23px),20px)}
.ad-fr__txt .ad-mini{margin-bottom:8px}
.ad-fr__txt h3{font-size:clamp(1.6rem,2.6vw,2.2rem); margin-bottom:.4em}
.ad-fr__txt p{margin:0; font-size:1.06rem}
.ad-fr__form{grid-column:6/-1; grid-row:2; display:flex; flex-direction:column; gap:var(--gap); padding-left:clamp(0px,calc(3vw - 23px),20px)}
.ad-fr__venmo{grid-column:6/-1; grid-row:3; align-self:end; margin-left:clamp(0px,calc(3vw - 23px),20px)}
.ad-fr:has(.ad-zeffy iframe){grid-template-rows:minmax(0,1fr) auto auto}
.ad-fr:has(.ad-zeffy iframe) .ad-fr__photo{grid-row:1; min-height:300px}
.ad-fr:has(.ad-zeffy iframe) .ad-fr__txt{grid-column:1/6; grid-row:2; padding-left:0}
.ad-fr:has(.ad-zeffy iframe) .ad-fr__venmo{grid-column:1/6; grid-row:3; margin-left:0}
.ad-fr:has(.ad-zeffy iframe) .ad-fr__form{grid-row:1/4}
.ad-gcard--bar{flex-direction:row; flex-wrap:wrap; align-items:center; gap:14px 24px; padding:22px var(--pad-card)}
.ad-gcard--bar b{flex:1 1 200px; min-width:0; font-family:var(--display); font-stretch:106%; font-weight:800; font-size:1.25rem; line-height:1.25}
.ad-gcard--bar .btn{align-self:center; margin:0; min-height:50px; font-size:1rem}
.ad-venmo{padding:20px var(--pad-card); border-radius:var(--r-xl); background:var(--mist); border:1px solid var(--line)}
.ad-venmo p{margin:0 0 14px}
.ad-venmo .btns{gap:10px 12px}
.ad-raised{border-radius:var(--r-xl); border:1px solid var(--line); background:#fff; padding:18px var(--pad-card)}
.ad-raised h4{font-family:var(--mono); font-size:.72rem; letter-spacing:.12em; text-transform:uppercase; color:var(--logo-teal); margin:0 0 10px}
.ad-raised .embed__fallback{flex-direction:row; flex-wrap:wrap; gap:12px 20px; align-items:center; justify-content:space-between; padding:0; background:none; border:0}
.ad-raised .embed__fallback p{margin:0; flex:1 1 240px}
@media (max-width:900px){
  .ad-fr, .ad-fr:has(.ad-zeffy iframe){grid-template-columns:minmax(0,1fr); grid-template-rows:none}
  .ad-fr > *, .ad-fr:has(.ad-zeffy iframe) > *{grid-column:auto!important; grid-row:auto!important}
  .ad-fr__txt,.ad-fr__form{padding-left:0} .ad-fr__venmo{margin-left:0}
  .ad-fr__photo, .ad-fr:has(.ad-zeffy iframe) .ad-fr__photo{aspect-ratio:4/3; min-height:0}
  .ad-fr__photo--print, .ad-fr:has(.ad-zeffy iframe) .ad-fr__photo--print{aspect-ratio:5/4}
}
/* start your own */
.ad-start .fill-img{min-height:320px}
.ad-start .fill-img img{object-position:50% 40%}
.ad-moments{list-style:none; padding:0; margin:6px 0 26px; display:grid; grid-template-columns:repeat(2,max-content); justify-items:start; gap:14px 18px}
.ad-moments li{margin:0; font-family:var(--display); font-weight:900; font-stretch:115%; text-transform:uppercase; font-size:clamp(.95rem,1.5vw,1.25rem); line-height:1; padding:.6em .8em .52em; border:2.5px solid var(--slate); border-radius:8px; background:#fff; box-shadow:3px 3px 0 var(--slate); transform:rotate(-2deg); white-space:nowrap}
.ad-moments li:nth-child(2){background:var(--aqua); transform:rotate(1.5deg)}
.ad-moments li:nth-child(3){background:var(--mint); transform:rotate(-1deg)}
.ad-moments li:nth-child(4){transform:rotate(2deg)}
@media (max-width:520px){.ad-moments{display:flex; flex-wrap:wrap; gap:12px 14px} .ad-moments li{font-size:.95rem}}
'''

HEAD = f'<style>{CSS}</style>'


# =====================================================================
# educators.html
# =====================================================================
def educators():
    guide_ids = ['red-flags', 'baecode', 'knowb4unude', 'dating', 'online-harassment', 'rape-culture', 'male-survivors']
    shelf = ''
    for gid in guide_ids:
        it = next(x for x in LIB if x['id'] == gid)
        shelf += (f'<a class="ad-book" href="{it["href"]}" aria-label="Teaching guide: {esc(it["title"])}">'
                  f'{img(it["guide"]["cover"], "")}<span class="ad-book__tip" aria-hidden="true">{esc(it["title"])}</span></a>')
    shelf += (f'<a class="ad-book ad-book--rr" href="film-race-rape-culture-resistance.html" aria-label="Race, Rape Culture &amp; Resistance: four lessons">'
              f'{img("2l3a1960", "")}<span class="ad-book__bar"><small>Four lessons</small><b>Race, Rape Culture &amp; Resistance</b></span></a>')
    posters = [('poster-consent-is-bae', 'Consent is BAE: mutual, ongoing, sober, enthusiastic, voluntary, revocable'),
               ('relationships-2-1', 'What goes into a healthy relationship?'),
               ('no-means-no-pdf', 'No means no, but so does silence, “maybe later”, “I’m not sure” and being drunk'),
               ('poster-sober', 'If you’ve had too much to drink to drive, the same is true for hooking up'),
               ('poster-ending-online-harassment', 'Ending online harassment is everyone’s responsibility'),
               ('poster-do-you-knowb4unude', 'Do you #knowB4Unude?')]

    def pgroup(items):
        tot = sum(ratio(n) for n, _c in items)
        return (f'<div class="ad-prow__g" style="flex:{tot:.4f} 1 0%">'
                + ''.join(f'<button style="--ar:{ratio(n)}" data-src="{imgsrc(n)}" data-cap="{esc(c)}">{img(n, "SafeBAE poster: " + c)}</button>' for n, c in items)
                + '</div>')
    prow = f'<div class="ad-prow" data-gallery>{pgroup(posters[:3])}{pgroup(posters[3:])}</div>'

    svg, comps = ring_svg()
    svg = svg.replace(' tabindex="0" role="button"', '').replace('class="ring"', 'class="ring" role="img"')
    # at this size the ring's small "SIX COMPONENTS" label would be unreadable; the list beside it names all six
    import re as _re
    svg = _re.sub(r'<text[^>]*letter-spacing="2">SIX COMPONENTS</text>', '', svg).replace('y="205" text-anchor="middle" class="ring__c"', 'y="232" text-anchor="middle" class="ring__c"')
    comp_li = ''.join(f'<li>{a(esc(t), h if not h.startswith("#") else "360-schools.html" + h)}</li>' for t, h, *_r in comps)

    def top(title, text, label, chip_items, buttons):
        return (f'<div class="ad-g"><div class="ad-c8 ad-pr"><h3>{title}</h3><p>{text}</p>'
                f'<div class="ad-level__fits"><span class="ad-mini">{label}</span>{chips(chip_items)}</div></div>'
                f'<div class="ad-c4 ad-level__acts">{buttons}</div></div>')

    levels = [
        ('guides', 'One class discussion', 'Teaching Guides', 1,
         top('Teaching Guides', 'Our Teaching Guides are built for short, meaningful discussions. Each guide is paired with a youth-led educational video and includes discussion prompts and classroom activities.',
             'Works well in', ['Advisory', 'Health class', 'Homeroom', 'Clubs', 'Small groups'],
             btn('View teaching guides', 'library.html#guides', 'slate', arrow=True) + btn('Browse every film', 'library.html#films', 'ghost'))
         + f'<div class="ad-shelf">{shelf}</div>'),
        ('posters', 'Around the building', 'Classroom Posters', 2,
         top('Classroom Posters', 'Our posters are easy-to-share educational materials that help reinforce key messages around consent, healthy relationships, boundaries, and student support.',
             'Put them up in', ['Classrooms', 'Counseling offices', 'Hallways', 'Wellness centers', 'Student spaces'],
             btn('See all posters', 'posters.html', 'slate', arrow=True) + btn('Download all (.zip)', POSTERS_ZIP, 'ghost'))
         + prow + '<p class="ad-level__hint">Tap a poster to enlarge it</p>'),
        ('curriculum', 'Across multiple class periods', 'Consent Curriculum', 3,
         f'''<div class="ad-g ad-g--m"><div class="ad-c7 ad-pr ad-txt ad-col"><h3>Consent Curriculum</h3>
          <p>Our Consent Curriculum is designed for deeper, more sustained engagement across multiple class periods. It covers consent, healthy relationships, bystander intervention, and response, with structured lesson plans that can be adapted for different school contexts.</p>
          {chips(['15 modules', 'Aligned with NHES', '45–60 minute lessons', 'English & Spanish'])}
          <div class="btns">{btn('About the curriculum', 'consent-curriculum.html', 'slate', arrow=True)}{btn('Faculty & staff training', 'professional-development.html', 'ghost')}</div></div>
          <figure class="ad-c5 ad-media ad-shot fill-img">{img('us-gariev-teacher', 'A teacher leading a discussion with a class of students')}<span class="sticker">Teachers &amp; peer educators</span></figure></div>'''),
        ('360', 'Across the whole school', 'SafeBAE 360° Schools', 4,
         f'''<div class="ad-g"><div class="ad-c6 ad-col"><h3>SafeBAE 360° Schools</h3>
          <p>SafeBAE 360° Schools is our whole-school approach: a comprehensive, survivor-centered model that builds lasting prevention infrastructure across your whole school community. It spans education, youth leadership, policy reform, and staff training, and it is flexible enough to start small and grow over time.</p>
          <div class="btns">{btn('How 360° Schools works', '360-schools.html', 'slate', arrow=True)}{btn('Request a program', 'request-a-program.html', 'ghost')}</div></div>
          <div class="ad-c6 ad-ringwrap">{svg}<ol>{comp_li}</ol></div></div>'''),
    ]
    stairs = ''.join(
        f'<button class="ad-stair" role="tab" id="lv-{k}" aria-controls="lp-{k}" aria-selected="{str(i==0).lower()}" tabindex="{0 if i==0 else -1}">'
        f'<span class="ad-stair__txt"><small>{esc(s)}</small><b><span>{esc(t)}</span></b></span>'
        f'<span class="ad-stair__blocks" aria-hidden="true">{"<i></i>" * n}</span></button>'
        for i, (k, s, t, n, _p) in enumerate(levels))
    lpanels = ''.join(f'<div role="tabpanel" id="lp-{k}" aria-labelledby="lv-{k}"{"" if i==0 else " hidden"}><div class="ad-level">{p}</div></div>'
                      for i, (k, s, t, n, p) in enumerate(levels))

    body = f'''
<section class="phero phero--logo phero--split ad-phero">
  <span class="phero__wm" aria-hidden="true"></span>
  <div class="wrap">
    <div class="ad-c7 ad-pr ad-txt">
      {crumbs(('Home', 'index.html'), ('Adults', 'adults.html'), ('Educators', None))}
      <h1>For <span class="mk">educators</span></h1>
      <p class="lede">We know how very much educators are tasked with in any given day, so we have worked to provide tools for all levels of use. Start wherever you can. The most important part is helping your students feel engaged and invited into this work.</p>
      <div class="btns">{btn('See the tools', '#levels', 'mint', arrow=True)}{btn('Request a program', '#request', 'ghost')}</div>
    </div>
    <div class="ad-c5 phero__media">{img('img-3947', 'A SafeBAE session in a high school classroom', loading='eager', style='object-position:58% 50%')}<span class="sticker">Start wherever you can</span></div>
  </div>
</section>

<section class="band band--paper" id="levels">
  <div class="wrap">
    <div class="section-head"><div><h2>Classroom tools, from one lesson to the whole school</h2>
      <p class="lede lede--full">Pick the level that fits your time and your students, and add more when you’re ready.</p></div></div>
    <div data-tabs="edu-levels">
      <div class="ad-stairs" role="tablist" aria-label="Level of use">{stairs}</div>
      <div class="ad-axis" aria-hidden="true"><span>Short, meaningful discussions</span><span>Your whole school community</span></div>
      {lpanels}
    </div>
  </div>
</section>

<section class="band band--teal" id="vibe-check">
  <div class="wrap ad-g ad-g--m ad-vibe">
    <div class="ad-c7 ad-pr ad-txt">
      <div class="ad-vmark"><span class="daisy"></span>Introducing Vibe Check</div>
      <h2>CheckYourVibe.org</h2>
      <p class="lede">Vibe Check is a free, anonymous, self-guided tool that helps young people reflect on the health of their relationships. It is designed to be used privately and voluntarily.</p>
      <p class="ad-never">It should never be assigned to students.</p>
      <p>Making it available as an optional resource allows students who may need it to access it on their own terms, before you know anything specific about their situation. Consider sharing the link where students can find it without being asked to engage publicly:</p>
      <div class="ad-places"><ul><li>In your syllabus</li><li>On a resource wall</li><li>Anywhere students can find it on their own</li></ul></div>
      <div class="btns">{btn('Explore the tool', 'https://checkyourvibe.org/', 'mint')}{btn('Adult guide (PDF)', GUIDE_PDF, 'white')}{a('How it works', 'vibe-check.html', 'arrow-link')}</div>
    </div>
    <div class="ad-c5 ad-media">
      <div class="ad-phonewrap">
        <div class="ad-phone">{img('vc-screen', 'The Vibe Check home screen on a phone')}</div>
        <span class="sticker" style="left:-4%;top:17%">Anonymous</span>
        <span class="sticker sticker--white sticker--r" style="right:-4%;bottom:17%">Optional, never assigned</span>
      </div>
    </div>
  </div>
</section>

<section class="band band--mist" id="request">
  <div class="wrap ad-g ad-req">
    <div class="ad-c6 ad-pr ad-col">
      <h2>Ready to request a program?</h2>
      <p class="lede">Tell us what you’re looking for. Share key details about your needs and let us know how to follow up.</p>
      <ul class="ad-checks"><li>{a('Assemblies', 'assemblies.html')} and one-time events, always co-presented with youth leaders</li><li>Any component of the {a('SafeBAE 360° Schools', '360-schools.html')} approach, or the whole-school model</li><li>Flexible, sliding-scale pricing for school partners</li></ul>
      <div class="btns">{btn('Programs & pricing', 'request-a-program.html', 'slate', arrow=True)}{btn('Book a meeting', CALENDLY, 'ghost')}</div>
    </div>
    <div class="ad-c6 ad-card">{static_form('edu', 'Program request (educator)')}</div>
    <div class="ad-req__new" id="new"><span class="ad-mini">New for schools</span>
      <div>{''.join(f'<a href="{h}"><em>{w}</em><b>{t}</b><small>{d}</small><i aria-hidden="true">&rarr;</i></a>' for w, t, d, h in [
          ('Oct 26&ndash;30, 2026', 'AI Literacy Training', 'Six free, self-paced modules. Educators can register for group access.', 'ai-literacy.html'),
          ('November 2026', 'Sexual Strangulation Prevention', 'A new program on sexual strangulation, which young people call “choking.”', 'choking-hazard.html#schools')])}</div></div>
  </div>
</section>
'''
    page('educators.html', 'For Educators · SafeBAE', 'Classroom tools for every level of use: youth-made films with teaching guides, prevention posters, the Consent Curriculum and SafeBAE 360° Schools.',
         body, active='adults', head_extra=HEAD, body_class='ad')


# =====================================================================
# college.html
# =====================================================================
def college():
    body = f'''
<section class="phero phero--split ad-phero">
  <span class="phero__wm" aria-hidden="true"></span>
  <div class="wrap">
    <div class="ad-c7 ad-pr ad-txt">
      {crumbs(('Home', 'index.html'), ('Adults', 'adults.html'), ('College Students', None))}
      <h1>For <span class="mk">college students</span></h1>
      <p class="lede">Mentor high school students, start a SafeBAE club on your own campus, and become a Certified Peer Educator.</p>
      <div class="btns">{btn('Become a mentor', '#mentor', 'mint', arrow=True)}{btn('Start a campus club', '#campus', 'ghost')}</div>
    </div>
    <div class="ad-c5 phero__media">{img('1-7c1d4302-803a-4154-b18a-3a64432a6c76', 'Five college-age SafeBAE supporters standing together outdoors', loading='eager', style='object-position:50% 38%')}<span class="sticker">Materials at no cost</span></div>
  </div>
</section>

<section class="band band--paper" id="mentor">
  <div class="wrap">
    <div class="ad-g ad-g--m">
      <div class="ad-c7 ad-pr ad-txt">
        <h2>Mentor high school students</h2>
        <p class="lede">Our mentor opportunities are for college students who want to support SafeBAE by becoming Certified Peer Educators and connecting directly with high schools.</p>
        <p>Many college students who join us are also survivors themselves, motivated to create safer environments in the schools they came from. All student engagement materials are available to you at no cost, and our team is here to back you every step of the way.</p>
      </div>
      <figure class="ad-c5 ad-media ad-fig"><div class="ad-fig__img">{img('cc57083e-b9a4-48bf-bf9d-f4e4636d1447', 'A young advocate speaks at a rally in support of student survivors')}</div><figcaption>You know these communities best, and with our support, you can help lead meaningful change.</figcaption></figure>
    </div>
    <div class="ad-bridge reveal" data-in role="group" aria-label="What mentors do">
      <span class="ad-mini">What mentors do</span>
      <div class="ad-bridge__in">
        <div class="ad-bridge__end"><small>You</small><b>College mentor</b></div>
        <ul class="ad-bridge__lanes"><li><span>Build SafeBAE clubs</span></li><li><span>Advocate for safer policies</span></li><li><span>Transform their school culture</span></li></ul>
        <div class="ad-bridge__end ad-bridge__end--hs"><small>With</small><b>High school students</b></div>
      </div>
    </div>
    <div class="ad-mail"><b>Interested? Email us to get started.</b>{copyable(EMAIL)}{btn('Email SafeBAE', mailto('College mentor'), 'mint')}</div>
  </div>
</section>

<section class="band band--deep ad-campus" id="campus">
  <div class="wrap ad-g ad-g--m">
    <figure class="ad-c5 ad-media ad-shot fill-img">{img('us-colah-campus', 'Students walking across a college campus under the trees')}<span class="sticker sticker--white">Your campus</span></figure>
    <div class="ad-c7 ad-pl ad-txt ad-col">
      <h2>Start a SafeBAE club on your campus</h2>
      <p class="lede">Along with mentoring younger students, you can start a SafeBAE club on your own campus.</p>
      <p>Clubs bring together students to raise awareness, push for policy reform, and create a campus culture rooted in consent and accountability. We provide resources, training, and ongoing support to help you organize events, campaigns, and advocacy projects that make an impact.</p>
      <div class="ad-provide"><span class="ad-mini">We provide</span><ul><li>Resources</li><li>Training</li><li>Ongoing support</li></ul></div>
      <div class="btns">{btn('Start a campus club', 'clubs.html', 'mint', arrow=True)}{btn('Request a program', 'request-a-program.html', 'ghost')}</div>
    </div>
  </div>
</section>

<section class="band band--paper ad-cert" id="certify">
  <div class="wrap">
    <div class="section-head"><div><p class="eyebrow">Certified Peer Educator Training</p><h2>Get certified, then lead on your campus</h2>
      <p class="lede lede--full">College students are encouraged to complete SafeBAE’s Certified Peer Educator Training to strengthen prevention on their own campuses and to collaborate with nearby high schools.</p></div></div>
    <div class="ad-g">
      <div class="ad-c6">{cpet_player()}</div>
      <div class="ad-c6 ad-col">
        <div class="ad-prio"><b>Certified students are prioritized</b><p>when paid mentorship opportunities become available.</p></div>
        <ul class="ad-facts"><li>Free</li><li>Self-paced</li><li>16 modules</li></ul>
        <div class="btns">{btn('Become a Peer Educator', 'peer-educator.html', 'slate', arrow=True)}{btn('Register now', 'peer-educator.html#register', 'ghost')}</div>
      </div>
    </div>
    <div class="ad-ailine" id="ai-literacy">
      <div class="ad-date" aria-hidden="true"><b>OCT</b><span>26&ndash;30</span></div>
      <p><b>New: SafeBAE AI Literacy Training.</b> Six free, self-paced modules for high school and college students, launching during U.S. Media Literacy Week, October 26&ndash;30, 2026. Create a free account and your progress saves as you go.</p>
      {btn('About the training', 'ai-literacy.html', 'slate', 'sm', arrow=True)}
    </div>
  </div>
</section>

'''
    page('college.html', 'For College Students · SafeBAE', 'Mentor high school students, start a SafeBAE club on your campus, and become a Certified Peer Educator.',
         body, active='adults', head_extra=HEAD, body_class='ad', scripts=IN_JS)


# =====================================================================
# donate.html
# =====================================================================
def donate():
    fid = '1ac5fff7-3c20-45c1-95f1-f4fa34a07f88'
    card = f'''<div class="ad-gcard"><span class="daisy-art" aria-hidden="true"></span>
      <span class="ad-mini">One-time or monthly</span>
      <h3>Give securely through Zeffy</h3>
      <p>Zeffy charges us no platform fees. Your full gift funds the work.</p>
      {btn('Open the donation form', ZEFFY_PUBLIC + fid, 'mint')}
      <div class="ad-gcard__alt"><span class="ad-mini">Other ways to give right now</span>
        <ul><li>{a('Venmo @Safe-BAE', VENMO)}</li><li>{a('Mail a check', '#ways', attrs=' data-tab-go="wt-check"')}</li><li>{a('Employer matching', '#ways', attrs=' data-tab-go="wt-match"')}</li></ul></div>
    </div>'''
    zeffy = embed_box(ZEFFY_EMBED + fid, card, height=1040, note='Zeffy charges us no platform fees. Your full gift funds the work.')
    funds = [
        ('sumact5', 'Students talking in a circle during a SafeBAE training', 'Peer educator training for student leaders across the country', '50% 30%'),
        ('066', 'SafeBAE speakers with a packed school auditorium', '360° Schools, our whole-school prevention program', '50% 55%'),
        ('vc-screen', 'The Vibe Check home screen', 'Free tools like Vibe Check that help teens reflect on their own behavior', '50% 31%'),
        ('cc57083e-b9a4-48bf-bf9d-f4e4636d1447', 'A young advocate speaking at a rally to support student survivors', 'Survivor support and trauma-informed policy advocacy', '70% 38%'),
    ]
    ft = ''.join(f'<li><span class="ad-ft__img">{img(n, alt, style="object-position:" + pos)}</span><span class="ad-ft__cap">{esc(cap)}</span></li>' for n, alt, cap, pos in funds)

    ways = [
        ('shop', 'Shop for a cause', 'Buy books, posters, and classroom tools. Every purchase funds prevention.',
         '<p>Browse curriculum materials, posters, and classroom tools in our educational shop, or buy your next read through our Bookshop.org storefront. A portion of every book purchase supports SafeBAE at no extra cost to you.</p>',
         btn('Educational products', 'https://safebae.podia.com/', 'teal') + btn('Our Bookshop', 'https://bookshop.org/shop/SafeBAE', 'ghost')),
        ('match', 'Double your gift', 'Employer matching can double or even triple your donation.',
         f'<ol><li>Check your HR or giving portal to see if your employer matches donations.</li><li>List <b>SafeBAE</b>, a registered 501(c)(3), as the recipient. EIN {copyable("81-5451147")}</li><li>Need additional documentation? Use our contact form or email us at {a(EMAIL, mailto("Employer Matching"), "link")}.</li></ol>',
         btn('Contact form', 'contact.html', 'teal') + btn('Email us', mailto('Employer Matching'), 'ghost')),
        ('fundraise', 'Fundraise for SafeBAE', 'Turn a birthday, run, or campus event into support for prevention.',
         f'<p>Pick your moment (a birthday, a 5K, a class project, a campus event) and invite your community to give alongside you. Share your idea through our contact form or email us at {a(EMAIL, mailto("Fundraising for SafeBAE"), "link")} and we’ll help you set everything up.</p>',
         btn('See current fundraisers', 'fundraise.html', 'teal', arrow=True) + btn('Contact form', 'contact.html', 'ghost') + btn('Email us', mailto('Fundraising for SafeBAE'), 'ghost')),
        ('partner', 'Partner or give in-kind', 'Sponsorships and partnerships for companies, foundations and groups.',
         f'<p>Support the work through sponsorship, in-kind donations, or a longer-term partnership. Reach out through our contact form or email us at {a(EMAIL, mailto("Partnership"), "link")} to talk through what fits your organization.</p>',
         btn('Contact form', 'contact.html', 'teal') + btn('Email us', mailto('Partnership'), 'ghost')),
        ('check', 'Mail a check', 'Prefer to give by mail? We gladly accept checks.',
         f'''<p>Make checks payable to <b>SafeBAE</b> and mail to:</p>
         <div class="ad-addr"><address>SafeBAE<br>7 Evelyn Drive<br>Bristol, RI 02809</address>{copyable('SafeBAE, 7 Evelyn Drive, Bristol, RI 02809', 'Copy the address')}</div>
         <p class="muted">Include your email or return address if you’d like an acknowledgment for your records.</p>''', ''),
        ('other', 'Other ways to give', 'Gifts of stock, donor-advised funds and planned giving.',
         f'<p>For gifts of stock, donor-advised fund grants, planned giving, or anything not covered here, use our contact form or email us at {a(EMAIL, mailto("Other Ways to Give"), "link")} and we’ll point you in the right direction.</p>',
         btn('Contact form', 'contact.html', 'teal') + btn('Email us', mailto('Other Ways to Give'), 'ghost')),
    ]
    wl = ''.join(f'<button class="ad-way" role="tab" id="wt-{k}" aria-controls="wp-{k}" aria-selected="{str(i==0).lower()}" tabindex="{0 if i==0 else -1}"><b>{esc(t)}</b><i aria-hidden="true">&rarr;</i></button>' for i, (k, t, *_r) in enumerate(ways))
    wp = ''.join(f'<div role="tabpanel" id="wp-{k}" aria-labelledby="wt-{k}"{"" if i==0 else " hidden"} class="ad-wpanel"><h3>{esc(t)}</h3><p class="ad-wpanel__lede">{esc(s)}</p>{d}{f"""<div class="btns">{acts}</div>""" if acts else ""}</div>' for i, (k, t, s, d, acts) in enumerate(ways))

    body = f'''
<section class="phero phero--split ad-phero ad-phero--long">
  <span class="phero__wm" aria-hidden="true"></span>
  <div class="wrap">
    <div class="ad-c7 ad-pr ad-txt">
      {crumbs(('Home', 'index.html'), ('Donate', None))}
      <h1>Help end sexual violence <span class="mk">before it starts.</span></h1>
      <p class="lede">SafeBAE is a survivor-founded, youth-led organization dedicated to ending sexual violence before it starts. Our programs are free for students and designed to create lasting culture change in schools, backed by a growing body of evidence showing real impact.</p>
      <div class="btns">{btn('Make your gift', '#give', 'coral', arrow=True)}{btn('More ways to give', '#ways', 'ghost')}</div>
    </div>
    <div class="ad-c5 phero__media ad-dphoto">{img('dsc01134', 'SafeBAE youth leaders in SafeBAE t-shirts', loading='eager')}<span class="sticker">Free for students</span><span class="sticker sticker--white sticker--r">Survivor-founded</span></div>
  </div>
</section>

<section class="band band--paper" id="give">
  <div class="wrap">
    <div class="ad-give">
      <div class="ad-give__head">
        <h2>Monthly gifts help most.</h2>
        <p class="lede">They give us steady funding we can plan around.</p>
      </div>
      <div class="ad-give__form">
        {zeffy}
      </div>
      <div class="ad-give__funds">
        <span class="ad-mini">Your gift funds</span>
        <ul class="ad-ft">{ft}</ul>
      </div>
      <div class="ad-give__proof">
        <div class="ad-proof reveal" data-in>
          <div class="ad-proof__stat"><b aria-hidden="true" data-count="3000" data-suffix="+">3,000+</b><span><span class="sr-only">3,000+ </span>young people trained as Certified Peer Educators so far</span></div>
          <div class="ad-proof__trust">{img('candid-platinum-seal-of-transparency-1-0', 'Candid Platinum Seal of Transparency')}<div><p>SafeBAE is a registered <span style="white-space:nowrap">501(c)(3)</span> nonprofit with a Candid Platinum Seal of Transparency. Gifts are tax-deductible.</p>{copyable('81-5451147', 'EIN 81-5451147')}</div></div>
          <div class="ad-proof__more"><p><b>Prefer Venmo?</b> Give to {a('@Safe-BAE', VENMO, 'link')}.</p><p><b>Questions about your gift?</b> Email {a(EMAIL, mailto('Donation Question'), 'link')}.</p></div>
        </div>
      </div>
    </div>
  </div>
</section>

<section class="band band--deep ad-story">
  <div class="wrap ad-g ad-g--m">
    <figure class="ad-c5 ad-media ad-shot fill-img">{img('000422', 'A large group of SafeBAE students in tie-dye SafeBAE shirts on the steps of a building')}<span class="sticker sticker--aqua">Youth-led</span></figure>
    <div class="ad-c7 ad-pl ad-txt ad-col">
      <h2>Founded by survivors, led by young people</h2>
      <p class="lede ad-lede-light">SafeBAE began when our co-founders met during the filming of Netflix’s <i>Audrie &amp; Daisy</i>, united by a shared goal: to prevent what happened to us from happening to anyone else.</p>
      <p class="muted">Today, we’re a national organization where young people lead the work of sexual violence prevention.</p>
      <div class="btns">{btn('Our story', 'about.html', 'mint', arrow=True)}{btn('See the data', 'impact.html', 'ghost')}{btn('#ForDaisy', 'fordaisy.html', 'ghost')}</div>
    </div>
  </div>
</section>

<section class="band band--paper" id="ways">
  <div class="wrap">
    <div class="section-head"><div><h2>More ways to give</h2></div></div>
    <div class="ad-g ad-ways" data-tabs="donate-ways"><div class="ad-ways__list" role="tablist" aria-label="Ways to give" aria-orientation="vertical">{wl}</div><div class="ad-ways__panels">{wp}</div></div>
    <div class="ad-strip">
      <div><h3>Found SafeBAE’s resources helpful?</h3><p>Chip in any amount, or give through a supporter’s fundraiser.</p></div>
      <div class="btns">{btn('Chip in', 'chip-in.html', 'slate', arrow=True)}{btn('Peer-to-peer fundraisers', 'fundraise.html', 'ghost')}</div>
    </div>
  </div>
</section>
'''
    page('donate.html', 'Donate · SafeBAE', 'Support SafeBAE’s youth-led work to prevent sexual violence. Your donation funds peer education, free resources, and safer school communities.',
         body, active='about', head_extra=HEAD, body_class='ad', scripts=TABGO_JS + IN_JS)


# =====================================================================
# chip-in.html
# =====================================================================
def chipin():
    card = f'''<div class="ad-gcard"><span class="daisy-art" aria-hidden="true"></span>
      <span class="sticker">Any amount</span>
      <h3>Chip in securely through Zeffy.</h3>
      <p>Zeffy charges us no platform fees. Your full gift funds the work.</p>
      {btn('Open the form', ZEFFY_PUBLIC + 'chip-in-2', 'coral')}
    </div>'''
    zeffy = embed_box(ZEFFY_EMBED + 'chip-in-2', card, height=1100, note='Zeffy charges us no platform fees. Your full gift funds the work.')
    body = f'''
<section class="phero phero--aqua ad-phero ad-chip">
  <span class="phero__wm" aria-hidden="true"></span>
  <div class="wrap">
    <div class="ad-chip__grid">
      <div class="ad-chip__intro">
        {crumbs(('Home', 'index.html'), ('Donate', 'donate.html'), ('Chip In', None))}
        <p class="eyebrow">{daisy()}Chip in</p>
        <h1>Did you find SafeBAE’s resources <span class="mk">helpful</span>?</h1>
        <p class="lede">We believe every young person deserves access to clear, honest, and practical information about consent, relationships, and safety, without barriers. If something you found here helped you, you can help us keep these resources free and accessible to young people everywhere.</p>
      </div>
      <div class="ad-chip__form">
        {zeffy}
      </div>
      <div class="ad-chip__impact">
        <span class="ad-mini">Your support helps make this possible</span>
        <ul class="ad-impact reveal" data-in>
          <li>Trained <strong>3,000+ young people</strong> as Certified Peer Educators</li>
          <li>Built a growing library of <strong>consent and healthy relationship resources</strong> used by students and educators nationwide</li>
          <li>Delivered <strong>workshops, classroom sessions, and peer-led trainings</strong> across the country</li>
          <li>Created <strong>youth-led media and tools</strong> that reach young people where they are, online and in their communities</li>
        </ul>
      </div>
      <figure class="ad-chip__photo ad-shot fill-img">{img('clubhero', 'SafeBAE club members taking a group selfie outdoors', loading='eager')}<span class="sticker">Led by young people</span></figure>
    </div>
  </div>
</section>

<section class="band band--slate ad-state">
  <div class="wrap">
    <div class="section-head"><div><h2>More ways to keep the resources free</h2>
      <p class="lede lede--full">Everything we create is led by young people, and <span class="mk">kept free for youth</span> so that everyone can access it when they need it.</p></div></div>
    <div class="ad-acts4 reveal">
      <a href="donate.html#give"><b>Give monthly</b><span>Steady funding we can plan around.</span><i>Donate</i></a>
      <a href="fundraise.html"><b>Fundraise</b><span>Turn a birthday, run or campus event into support.</span><i>Fundraisers</i></a>
      <a href="https://safebae.podia.com/" target="_blank" rel="noopener"><b>Shop educational products</b><span>Curriculum materials, posters and classroom tools.</span><i>Shop</i></a>
      <a href="https://bookshop.org/shop/SafeBAE" target="_blank" rel="noopener"><b>Buy a book</b><span>Bookshop.org purchases support SafeBAE at no extra cost.</span><i>Bookshop</i></a>
    </div>
  </div>
</section>
'''
    page('chip-in.html', 'Chip In · SafeBAE', 'Found SafeBAE’s resources helpful? Chip in to keep consent and healthy relationship resources free for young people everywhere.',
         body, active='about', head_extra=HEAD, body_class='ad', scripts=IN_JS)


# =====================================================================
# fundraise.html
# =====================================================================
def fundraise():
    def venmo_block(note_html, keyword=None):
        cp = copyable(keyword, f'Note: {keyword}') if keyword else ''
        return f'''<div class="ad-venmo ad-fr__venmo"><p>You can also support this fundraiser via Venmo. To help us properly track donations and giveaway entries, please include {note_html} in the payment note.</p><div class="btns">{btn('Venmo @Safe-BAE', VENMO, 'teal', 'sm')}{cp}</div></div>'''

    frs = [
        ('justin', 'Justin', 'img-4048', False, 'Justin, smiling in sunglasses and a cap, leaning on a porch railing outdoors',
         'Justin’s SafeBAE Fundraiser',
         '<p>This month, I’m using my platform to raise awareness and funds for SafeBAE, a survivor-founded, youth-led organization dedicated to ending sexual violence and supporting mental health among middle and high school students. As a longtime educator, I believe every young person deserves to be in an environment free from sexual violence, harassment, and abuse.</p>',
         venmo_block('<b>Justin</b>', 'Justin'), 'justins-safebae-fundraiser', ''),
        ('tuna', 'Tina', 'everyone-can-do-something-1', True, 'SafeBAE poster: No one can do everything but everyone can do something. End rape culture.',
         'Tina’s SafeBAE Fundraiser',
         '<p>For tonight’s livestream I’m using my platform to raise awareness and funds for SafeBAE, an organization I wish was around when I was a teenager. It is a survivor-founded, youth-led organization dedicated to ending sexual assault and dating violence among middle and high school students.</p>',
         venmo_block('<b>TUNA</b>', 'TUNA'), 'tunas-safebae-fundraiser',
         '<div class="ad-raised"><h4>Total raised so far</h4><div class="embed" data-embed="https://www.zeffy.com/embed/thermometer/tunas-safebae-fundraiser" data-h="120" data-title="Fundraiser progress powered by Zeffy">'
         f'<div class="embed__fallback"><p>The live total for Tina’s fundraiser appears here.</p>{btn("See the live total", ZEFFY_PUBLIC + "tunas-safebae-fundraiser", "teal", "sm")}</div></div></div>'),
        ('vanessa', 'Vanessa', 'copy-of-education-1', True, 'Polaroid-style photo captioned “Vanessa (Age 15)”: a teenage Vanessa looks back over her shoulder from a desk with a computer',
         'Vanessa’s SafeBAE Fundraiser',
         '<p>This month, I’m using my platform to raise awareness and funds for SafeBAE, an organization I wish was around when I was a teenager. It is a survivor-founded, youth-led organization dedicated to ending sexual violence and supporting mental health among middle and high school students.</p>',
         venmo_block('<b>your Instagram handle (username)</b>'), 'vanessa', ''),
    ]
    tabs = ''.join(f'<button class="ad-ptab{" ad-ptab--v" if k == "vanessa" else ""}" role="tab" id="tab-{k}" aria-controls="fp-{k}" aria-selected="{str(i==0).lower()}" tabindex="{0 if i==0 else -1}"><span>{img(im, "")}</span>{esc(n)}</button>' for i, (k, n, im, *_r) in enumerate(frs))
    panels = ''
    for i, (k, n, im, printed, alt, h, story, venmo, zslug, extra) in enumerate(frs):
        bar = f'<div class="ad-gcard ad-gcard--bar"><b>Give to {n}’s fundraiser securely through Zeffy.</b>{btn(f"Give to {n}’s fundraiser", ZEFFY_PUBLIC + zslug, "mint")}</div>'
        z = embed_box(ZEFFY_EMBED + zslug, bar, height=960)
        panels += f'''<div role="tabpanel" id="fp-{k}" aria-labelledby="tab-{k}"{'' if i==0 else ' hidden'}><div class="ad-fr">
      <figure class="ad-fr__photo{' ad-fr__photo--print' if printed else ''}">{img(im, alt, style='' if printed else 'object-position:38% 50%')}</figure>
      <div class="ad-fr__txt"><span class="ad-mini">Peer-to-peer fundraiser</span><h3>{esc(h)}</h3>{story}</div>
      <div class="ad-fr__form">{z}{extra}</div>
      {venmo}</div></div>'''

    body = f'''
<section class="phero phero--split ad-phero">
  <span class="phero__wm" aria-hidden="true"></span>
  <div class="wrap">
    <div class="ad-c7 ad-pr ad-txt">
      {crumbs(('Home', 'index.html'), ('Donate', 'donate.html'), ('Fundraise', None))}
      <h1><span class="mk">Fundraise</span> for SafeBAE</h1>
      <p class="lede">Turn a birthday, run, or campus event into support for prevention. Supporters use their own platforms to raise awareness and funds for SafeBAE, and invite their communities to give alongside them.</p>
      <div class="btns">{btn('Give to a fundraiser', '#fundraisers', 'coral', arrow=True)}{btn('Start your own', '#start', 'ghost')}</div>
    </div>
    <div class="ad-pols">
      <a class="ad-pol" href="#fundraisers" data-tab-go="tab-justin"><span class="ad-pol__img">{img('img-4048', 'Justin', loading='eager')}</span><b>Justin</b></a>
      <a class="ad-pol ad-pol--v" href="#fundraisers" data-tab-go="tab-vanessa"><span class="ad-pol__img">{img('copy-of-education-1', 'Vanessa at age 15', loading='eager')}</span><b>Vanessa</b></a>
      <a class="ad-pol ad-pol--contain" href="#fundraisers" data-tab-go="tab-tuna"><span class="ad-pol__img">{img('everyone-can-do-something-1', 'Tina’s fundraiser poster', loading='eager')}</span><b>Tina</b></a>
    </div>
  </div>
</section>

<section class="band band--paper" id="fundraisers">
  <div class="wrap">
    <div class="section-head"><div><h2>Give through a supporter’s fundraiser</h2></div></div>
    <div data-tabs="fundraisers"><div class="ad-ptabs" role="tablist" aria-label="Fundraisers">{tabs}</div>{panels}</div>
  </div>
</section>

<section class="band band--deep">
  <div class="wrap">
    <div class="section-head"><div><h2>Not ready to donate? You can still support SafeBAE</h2></div></div>
    <div class="ad-acts4 reveal">
      <a href="https://www.instagram.com/safe_bae/" target="_blank" rel="noopener"><b>Follow @safe_bae</b><span>Follow SafeBAE on Instagram.</span><i>Instagram</i></a>
      <a href="https://checkyourvibe.org/" target="_blank" rel="noopener"><b>Share CheckYourVibe.org</b><span>Share Vibe Check with someone.</span><i>Vibe Check</i></a>
      <a href="peer-educator.html"><b>Spread the word</b><span>Tell others about the Certified Peer Educator Training.</span><i>Peer Educator Training</i></a>
      <a href="mailto:{EMAIL}"><b>Get involved</b><span>Email {EMAIL} to get involved.</span><i>Email us</i></a>
    </div>
  </div>
</section>

<section class="band band--paper ad-start" id="start">
  <div class="wrap ad-g ad-g--m">
    <div class="ad-c7 ad-pr ad-txt ad-col">
      <p class="eyebrow">Start your own fundraiser</p>
      <h2>Pick your moment</h2>
      <ul class="ad-moments"><li>A birthday</li><li>A 5K</li><li>A class project</li><li>A campus event</li></ul>
      <p class="lede">Invite your community to give alongside you. Share your idea through our contact form or email us at {EMAIL} and we’ll help you set everything up.</p>
      <div class="btns">{btn('Contact form', 'contact.html', 'slate', arrow=True)}{btn('Email us', mailto('Fundraising for SafeBAE'), 'ghost')}</div>
    </div>
    <figure class="ad-c5 ad-media ad-shot fill-img">{img('img-9509-1', 'Hands decorating SafeBAE “yes means yes” consent stickers')}<span class="sticker sticker--aqua">Every gift funds prevention</span></figure>
  </div>
</section>
'''
    page('fundraise.html', 'Fundraise · SafeBAE', 'Give through a supporter’s peer-to-peer fundraiser for SafeBAE, or start your own for a birthday, run, class project or campus event.',
         body, active='about', head_extra=HEAD, body_class='ad', scripts=TABGO_JS)


def build():
    educators()
    college()
    donate()
    chipin()
    fundraise()


if __name__ == '__main__':
    build()
