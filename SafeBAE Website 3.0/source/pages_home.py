from lib import *
import math
from urllib.parse import quote as _q

# ---- hand-drawn marks in the AI Literacy Training's style (same shapes as the AI page) ----
def _svg_uri(svg):
    return 'url("data:image/svg+xml,' + _q(svg, safe=" =:/'-.,()") + '")'

def _brush(fill, op):
    return _svg_uri(f"<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 1920 400' preserveAspectRatio='none'><g fill='{fill}' fill-opacity='{op}'>"
                    "<path d='M90 84Q960 -44 1812 84Q1834 88 1848 118Q1880 190 1891 288Q1893 312 1872 310Q960 230 152 310Q134 311 124 290Q92 205 78 112Q74 87 90 84Z'/>"
                    "<path d='M38 158Q900 32 1766 158Q1788 162 1802 192Q1832 262 1842 360Q1845 384 1822 382Q960 306 103 383Q84 384 74 362Q43 280 28 186Q24 161 38 158Z'/></g></svg>")

def _wave(stroke):
    return _svg_uri(f"<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 200 14' preserveAspectRatio='none'><path d='M2 8C20 2 34 2 52 8S84 14 102 8S134 2 152 8S184 14 198 7' fill='none' stroke='{stroke}' stroke-width='2.4' stroke-linecap='round' vector-effect='non-scaling-stroke'/></svg>")

# pen loop drawn around the launch date (inline so it can draw itself in)
NW_LOOP = '<svg class="nw-loop__svg" viewBox="0 0 400 120" preserveAspectRatio="none" aria-hidden="true"><path pathLength="1" d="M34 30C120 6 300 2 368 22C396 30 402 66 384 88C346 116 124 122 42 106C8 98 2 66 16 44C28 24 84 12 156 8" fill="none" stroke="currentColor" stroke-width="3" stroke-linecap="round" vector-effect="non-scaling-stroke"/></svg>'
NW_WARN = '<svg viewBox="0 0 48 42" aria-hidden="true"><path d="M24 4 45 39H3Z" fill="none" stroke="currentColor" stroke-width="5" stroke-linejoin="round"/><rect x="21.6" y="14.5" width="4.8" height="13.5" rx="1.2" fill="currentColor"/><circle cx="24" cy="33" r="2.8" fill="currentColor"/></svg>'

# ---- per-film type identities (shared with the film pages) ----
FILM_FONTS = {
  'red':  ('Tilt Neon', "'Tilt Neon', sans-serif"),
  'bae':  ('Silkscreen', "'Silkscreen', monospace"),
  'know': ('Rubik Mono One', "'Rubik Mono One', sans-serif"),
  'date': ('Nunito', "'Nunito', sans-serif"),
  'oh':   ('DotGothic16', "'DotGothic16', sans-serif"),
  'rc':   ('Zilla Slab', "'Zilla Slab', serif"),
  'men':  ('Saira Stencil One', "'Saira Stencil One', sans-serif"),
  'rrcr': ('DM Serif Display', "'DM Serif Display', serif"),
}
FILMS = [
  ('film-its-giving-red-flags.html', 'red', 'It’s Giving Red Flags', 'red-flags', 'Consent · red flags'),
  ('film-baecode-game-on.html', 'bae', 'BAEcode: Game On!', 'gameon8', 'Bystander intervention'),
  ('film-knowb4unude.html', 'know', '#knowB4Unude', 'knowb4unude', 'Nudes · digital safety'),
  ('film-race-rape-culture-resistance.html', 'rrcr', 'Race, Rape Culture & Resistance', '2l3a1960', 'Four-lesson series'),
  ('film-dating-after-sexual-assault.html', 'date', 'Intimacy & Dating After Assault', 'yt-rixb8vlmajy', 'Healing · partners'),
  ('film-online-harassment-of-survivors.html', 'oh', 'End Online Harassment of Survivors', 'qts-full-cast-copy-2', 'Online harassment'),
  ('film-rape-culture.html', 'rc', 'Rape Culture → Culture of Respect', 'yt-fsmycfjpws4', 'With Charlie Coleman'),
  ('film-sexual-assault-of-men.html', 'men', 'Supporting Male Survivors', 'safebae-14', 'Theo’s story'),
]

def film_font_link(subset=True):
    fams = []
    for k, (fam, _) in FILM_FONTS.items():
        txt = ''.join(sorted(set(''.join(t for _, kk, t, _, _ in FILMS if kk == k) + 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'))) if subset else ''
        q = 'family=' + fam.replace(' ', '+') + (':wght@800' if fam == 'Nunito' else '') + (':wght@700' if fam == 'Zilla Slab' else '')
        fams.append(q)
    return '&'.join(fams)

def film_strip(cls=''):
    cards = []
    for href, k, title, im, tag in FILMS:
        cards.append(f'''<a class="fcard fcard--{k}" href="{href}">{img(im, '')}<span class="fcard__shade"></span><span class="fcard__tag">{esc(tag)}</span><span class="fcard__title">{esc(title)}</span><span class="fcard__go">Film + guide &rarr;</span></a>''')
    return f'<div class="fstrip {cls}">' + ''.join(cards) + '</div>'

FILM_STRIP_CSS = '''
.fstrip{display:grid; grid-auto-flow:column; grid-auto-columns:minmax(230px,1fr); gap:14px; overflow-x:auto; padding:4px 2px 18px; scroll-snap-type:x mandatory; scrollbar-width:thin}
.fcard{position:relative; aspect-ratio:3/4; border-radius:14px; overflow:hidden; color:#fff; text-decoration:none; scroll-snap-align:start; background:#000; display:block; isolation:isolate}
.fcard img{position:absolute; inset:0; width:100%; height:100%; object-fit:cover; transition:transform .6s}
.fcard:hover img{transform:scale(1.06)}
.fcard__shade{position:absolute; inset:0; background:linear-gradient(180deg, rgba(0,0,0,.05) 30%, rgba(8,24,30,.92))}
.fcard__tag{position:absolute; top:12px; left:12px; font-family:var(--mono); font-size:.7rem; letter-spacing:.1em; text-transform:uppercase; background:rgba(8,24,30,.65); padding:4px 8px; border-radius:4px}
.fcard__title{position:absolute; left:14px; right:14px; bottom:44px; font-size:1.55rem; line-height:1.02}
.fcard__go{position:absolute; left:14px; bottom:14px; font-family:var(--mono); font-size:.7rem; letter-spacing:.08em; text-transform:uppercase; color:var(--mint)}
.fcard--red .fcard__title{font-family:'Tilt Neon',sans-serif; color:#ffd9d9; text-shadow:0 0 6px #fe7171, 0 0 18px #fe7171, 0 0 36px rgba(254,113,113,.7); text-transform:uppercase; font-size:1.7rem}
.fcard--bae .fcard__title{font-family:'Silkscreen',monospace; color:#ffd2d2; text-shadow:3px 3px 0 #1d414e; font-size:1.45rem}
.fcard--know .fcard__title{font-family:'Rubik Mono One',sans-serif; color:var(--mint); font-size:1.35rem}
.fcard--date .fcard__title{font-family:'Nunito',sans-serif; font-weight:800; color:var(--aqua); text-transform:lowercase; font-size:1.6rem}
.fcard--oh .fcard__title{font-family:'DotGothic16',sans-serif; color:var(--mint); text-transform:uppercase; font-size:1.4rem}
.fcard--rc .fcard__title{font-family:'Zilla Slab',serif; font-weight:700; color:#fff; font-size:1.6rem}
.fcard--men .fcard__title{font-family:'Saira Stencil One',sans-serif; color:#fff; letter-spacing:.06em; text-transform:uppercase; font-size:1.5rem}
.fcard--rrcr .fcard__title{font-family:'DM Serif Display',serif; color:#fff; font-size:1.7rem}
'''

def ring_svg():
    comps = [
      ('Peer Educator Training & Youth Leadership', 'peer-educator.html', '#15ffc8', '#1d414e'),
      ('Healthy Relationship & Consent Curriculum', 'consent-curriculum.html', '#13848f', '#fff'),
      ('Faculty & Staff Training', 'professional-development.html', '#1d5a66', '#fff'),
      ('School Policy Support', 'policy-reform-guide.html', '#1d414e', '#fff'),
      ('Anonymous Reporting Tool (SafeBAE x REES)', '#rees', '#fe7171', '#1d414e'),
      ('Educational Resources to Reduce Recidivism', 'accountability-training.html', '#7dbbc1', '#1d414e'),
    ]
    cx = cy = 210; R = 200; r = 128; gap = 2.4
    paths = []
    for i, (t, h, fill, ink) in enumerate(comps):
        a0 = math.radians(-90 + i * 60 + gap / 2); a1 = math.radians(-90 + (i + 1) * 60 - gap / 2)
        p = lambda rad, ang: (cx + rad * math.cos(ang), cy + rad * math.sin(ang))
        x0, y0 = p(R, a0); x1, y1 = p(R, a1); x2, y2 = p(r, a1); x3, y3 = p(r, a0)
        d = f'M{x0:.1f},{y0:.1f} A{R},{R} 0 0 1 {x1:.1f},{y1:.1f} L{x2:.1f},{y2:.1f} A{r},{r} 0 0 0 {x3:.1f},{y3:.1f} Z'
        am = math.radians(-90 + i * 60 + 30); tx, ty = p((R + r) / 2, am)
        paths.append(f'<g class="seg" data-seg="{i}" tabindex="0" role="button" aria-label="{esc(t)}"><path d="{d}" fill="{fill}"/><text x="{tx:.1f}" y="{ty+9:.1f}" text-anchor="middle" fill="{ink}" font-family="Archivo" font-weight="900" font-size="26">{i+1}</text></g>')
    return f'<svg class="ring" viewBox="0 0 420 420" aria-label="SafeBAE 360 components">{"".join(paths)}<text x="210" y="205" text-anchor="middle" class="ring__c" font-family="Archivo" font-weight="900" font-size="64" fill="#1d414e" style="font-stretch:125%">360&deg;</text><text x="210" y="238" text-anchor="middle" font-family="IBM Plex Mono" font-weight="600" font-size="13" fill="#46646e" letter-spacing="2">SIX COMPONENTS</text></svg>', comps

COMP_TEXT = [
  'Students complete a self-paced, online certification to become Peer Educators. Youth leaders help shape implementation, lead presentations, co-facilitate curriculum sessions, organize campaigns through SafeBAE Clubs, and receive ongoing mentorship from our team.',
  'A trauma-informed curriculum aligned with the National Health Education Standards. Lessons cover consent, boundaries, communication, digital safety, healing, and accountability, with lesson plans, slides, activities, and printable resources.',
  'Professional development for teachers, staff, and administrators on trauma-informed response, supporting marginalized students, and building a school culture of consent and accountability. Flexible and tailored to each school.',
  'Hands-on consultation to audit and revise sexual misconduct and Title IX policies, with annotated audits, student-centered model language, communication templates, and rollout strategies.',
  'A secure, private space where students can document incidents of harm at their own pace, report anonymously or by name to their school, and connect with school-specific resources and support.',
  'Tools for students who have caused harm, supporting education, accountability, and behavior change. Includes the structured Accountability Training and Vibe Check, rooted in prevention, healing, and restorative justice rather than punishment.',
]


# =====================================================================
# Home page (v3). One 12-column grid inside the 1240px wrap; every row is equal columns
# or a named feature split, and side-by-side blocks end level.
# =====================================================================
_SEG_PUSH = ''.join(
    f'.tsx .seg[data-seg="{i}"].on{{transform:translate({11 * math.cos(math.radians(-60 + i * 60)):.1f}px,{11 * math.sin(math.radians(-60 + i * 60)):.1f}px)}}'
    for i in range(6))

HOME_CSS = FILM_STRIP_CSS + r'''
/* ---------- home: tokens + shared bits ---------- */
body.home{--hand:"Balsamiq Sans","Comic Neue",var(--body); --hz:#FFD600; --hz-ink:#0d0d0d;
  --wi:calc(min(100vw, var(--wrap)) - 2*var(--gutter)); --col:calc((var(--wi) - 11*var(--gap))/12)}
.home :is(.band--paper,.band--aqua,.band--mist) .eyebrow{color:var(--logo-teal)}
.home .player{border-radius:var(--r-xl)}
.hd{display:grid; grid-template-columns:minmax(0,1fr) auto; column-gap:clamp(20px,3vw,40px); align-items:end; margin-bottom:var(--head-gap)}
.hd > *{grid-column:1 / -1; min-width:0}
.hd > .eyebrow{justify-self:start}
.hd > h2{margin:0}
.hd--act > h2{grid-column:1}
.hd > .hd__act{grid-column:2; margin:0}
.hd > .lede{margin:.6em 0 0; max-width:none}
@media (max-width:760px){ .hd--act > h2{grid-column:1 / -1} .hd > .hd__act{grid-column:1 / -1; grid-row:99; margin-top:20px; justify-self:start} }

/* ---------- hero: title + a still photo wall that runs off the top, right and bottom ---------- */
.hero{position:relative; overflow:hidden; background-color:var(--slate); background-image:var(--grain); color:#fff;
  --wl:calc(50% - var(--wi)/2 + 8*var(--col) + 8*var(--gap))}
.hero__in{padding-block:clamp(30px,2.8vw,40px) clamp(34px,3.1vw,44px)}
.hero__head,.hero__body{position:relative; z-index:2; width:min(100%, calc(8*var(--col) + 7*var(--gap)))}
.hero .eyebrow{color:var(--mint); margin-bottom:.85rem}
.hero__title{font-size:clamp(2.8rem,6.5vw,6.6rem); line-height:.86; font-weight:900; font-stretch:125%; text-transform:uppercase; letter-spacing:-.02em; margin:0 0 .19em}
.hero__title span{display:block; white-space:nowrap}
.hero__title b{color:var(--mint); font-weight:900}
.hero__title i{font-style:normal; display:inline-block; animation:stretch 1.2s cubic-bezier(.2,.8,.2,1) both}
.hero__title span:nth-child(2) i{animation-delay:.12s} .hero__title span:nth-child(3) i{animation-delay:.24s} .hero__title span:nth-child(4) i{animation-delay:.36s}
@keyframes stretch{from{font-stretch:62%; opacity:.25; letter-spacing:-.06em} to{font-stretch:125%; opacity:1; letter-spacing:-.02em}}
.hero__key{display:flex; align-items:center; gap:10px; font-family:var(--mono); font-size:.8rem; letter-spacing:.06em; color:var(--aqua); margin:0 0 2.5em}
.hero__key b{color:var(--mint)}
.hero__key .daisy{color:var(--mint)}
.hero .lede{color:rgba(255,255,255,.92); max-width:none; margin-bottom:1.15em}
.hero__body.rise > *{animation-delay:.34s} .hero__body.rise > *:nth-child(2){animation-delay:.42s} .hero__body.rise > *:nth-child(3){animation-delay:.5s}
.hero__proof{list-style:none; margin:clamp(20px,1.8vw,26px) 0 0; padding:0; display:flex; flex-wrap:wrap; gap:14px 0}
.hero__proof li{margin:0; padding:1px 26px; border-left:2px solid rgba(209,254,255,.28); display:flex; flex-direction:column; gap:3px}
.hero__proof li:first-child{padding-left:0; border-left:0}
.hero__proof b{font-family:var(--display); font-weight:900; font-stretch:118%; font-size:1.45rem; line-height:1; color:var(--mint)}
.hero__proof span{font-size:.9rem; font-weight:600; line-height:1.3; color:var(--aqua)}
.hero .wm-daisy{--wm-o:.3; z-index:0; right:auto; bottom:auto; width:clamp(520px,57vw,830px); left:calc(var(--wl) - clamp(170px,19vw,275px)); top:clamp(-46px,-2vw,-14px)}
.hero__wall{position:absolute; z-index:1; top:0; bottom:0; left:calc(var(--wl) + 8px); right:-26px}
.hero__cols{position:absolute; inset:0; display:grid; grid-template-columns:repeat(3,minmax(0,1fr)); gap:12px; align-items:start}
.hero__col{display:flex; flex-direction:column; gap:12px; transform:translateY(calc(var(--y) + var(--s,0) * var(--k) * 1px)); transition:translate 1.4s var(--ease), opacity .7s ease}
.hero__col:nth-child(1){--y:-74px; --k:-.1}
.hero__col:nth-child(2){--y:-196px; --k:.07; transition-delay:.08s}
.hero__col:nth-child(3){--y:-22px; --k:-.17; transition-delay:.16s}
/* entrance runs on a class, not a keyframe animation, so it can never be caught at its first frame */
.js .hero__wall:not(.in) .hero__col{translate:0 90px; opacity:0}
.js .hero__wall:not(.in) .hero__col:nth-child(2){translate:0 -90px}
.hero__col img{width:100%; aspect-ratio:4/5; object-fit:cover; border-radius:14px; background:var(--slate-deep)}
.hero__wall .sticker{position:absolute; z-index:2; transition:opacity .5s ease .9s, translate .7s var(--ease) .9s}
.js .hero__wall:not(.in) .sticker{opacity:0; translate:0 16px}
.hero__wall .sticker:nth-of-type(1){left:-26px; top:19%}
.hero__wall .sticker:nth-of-type(2){right:54px; top:50%; transition-delay:1.05s}
.hero__wall .sticker:nth-of-type(3){left:17%; bottom:14%; transition-delay:1.2s}
@media (max-width:1200px){
  .hero__cols{grid-template-columns:repeat(2,minmax(0,1fr))}
  .hero__col:nth-child(3){display:none}
  .hero__wall .sticker:nth-of-type(2){right:40px}
  .hero__wall .sticker:nth-of-type(3){left:8%}
}
@media (max-width:1180px){
  .hero__btns{display:grid; grid-template-columns:auto auto; justify-content:start}
  .hero__btns .btn:first-child{grid-column:1 / -1}
  .hero__proof{display:grid; grid-template-columns:minmax(0,1fr); gap:8px}
  .hero__proof li{flex-direction:row; align-items:baseline; gap:12px; padding:0; border:0}
  .hero__proof b{font-size:1.25rem; min-width:6.5em}
}
@media (max-width:900px){
  .hero__in{display:flex; flex-direction:column; padding-block:30px 40px}
  .hero__head,.hero__body{width:100%}
  .hero__key{margin-bottom:1.3em}
  .hero__wall{position:relative; inset:auto; left:auto; right:auto; height:clamp(176px,42vw,320px); margin:0 calc(-1*var(--gutter)) 24px; overflow:hidden}
  .hero__cols{display:block}
  .hero__col{flex-direction:row; width:max-content; height:100%; gap:10px; --x:-46px; --k:-.3; transform:translateX(calc(var(--x) + var(--s,0) * var(--k) * 1px))}
  .js .hero__wall:not(.in) .hero__col, .js .hero__wall:not(.in) .hero__col:nth-child(2){translate:60px 0}
  .hero__col:nth-child(n+2){display:none}
  .hero__col img{width:auto; height:100%}
  .hero__wall .sticker:nth-of-type(1){left:var(--gutter); top:14px}
  .hero__wall .sticker:nth-of-type(2){right:var(--gutter); top:auto; bottom:14px}
  .hero__wall .sticker:nth-of-type(3){display:none}
  .hero .wm-daisy{--wm-o:.2; left:auto; right:-38%; top:-2%; width:118vw}
}
@media (max-width:480px){
  .hero__btns{grid-template-columns:minmax(0,1fr)}
}

/* ---------- who: five tabs and a panel on the same five column lines ---------- */
.who__tabs{display:grid; grid-template-columns:repeat(5,minmax(0,1fr)); gap:var(--gap); margin-bottom:var(--gap)}
.who__tab{font:inherit; text-align:left; padding:16px 18px 15px; border-radius:14px; border:2px solid var(--line); background:#fff; color:var(--slate); cursor:pointer; display:flex; flex-direction:column; justify-content:center; gap:5px; min-height:86px; transition:border-color .2s, background .2s, transform .2s var(--ease)}
.who__tab small{font-family:var(--mono); font-size:.72rem; letter-spacing:.1em; text-transform:uppercase; color:var(--logo-teal)}
.who__tab span{font-family:var(--display); font-weight:800; font-stretch:110%; font-size:1.2rem; line-height:1.1}
.who__tab:hover{border-color:var(--teal); transform:translateY(-2px)}
.who__tab[aria-selected="true"]{background:var(--slate); color:#fff; border-color:var(--slate)}
.who__tab[aria-selected="true"] small{color:var(--mint)}
.who__tab--help small{color:var(--slate)}
.who__tab--help{border-color:var(--coral)}
.who__panel{display:grid; grid-template-columns:repeat(5,minmax(0,1fr)); gap:var(--gap); align-items:stretch}
.who__img{grid-column:span 2; border-radius:var(--r-xl); overflow:hidden; min-height:340px; position:relative}
.who__img img{position:absolute; inset:0; width:100%; height:100%; object-fit:cover}
.who__img .sticker{position:absolute; left:18px; bottom:18px}
.who__txt{grid-column:span 3; min-width:0; display:flex; flex-direction:column}
.who__txt h3{font-size:clamp(1.5rem,2.4vw,2rem); margin-bottom:.35em}
.who__txt > p{margin-bottom:1.1em}
.who__txt .rows{flex:1; align-content:start}
.row--multi{position:relative}
.row__main{color:inherit; text-decoration:none}
.row__main::after{content:""; position:absolute; inset:0}
.row--multi small a{position:relative; z-index:1; font-weight:700; color:var(--logo-teal)}
@media (max-width:960px){
  .who__tabs{grid-template-columns:repeat(6,minmax(0,1fr)); gap:10px}
  .who__tab{grid-column:span 2; min-height:76px; padding:13px 14px}
  .who__tab:nth-child(n+4){grid-column:span 3}
  .who__panel{grid-template-columns:minmax(0,1fr)}
  .who__img,.who__txt{grid-column:auto}
  .who__img{min-height:0; aspect-ratio:16/10}
}
@media (max-width:520px){
  .who__tabs{grid-template-columns:repeat(2,minmax(0,1fr))}
  .who__tab,.who__tab:nth-child(n+4){grid-column:auto}
  .who__tab:last-child{grid-column:1 / -1}
  .who__tab span{font-size:1.08rem}
}

/* ---------- New from SafeBAE: a diptych. Each half keeps its program's own look; the six rows
   (kicker, visual, title, text, steps, actions) are shared so the halves line up row for row ---------- */
.nw{position:relative; display:grid; grid-template-columns:minmax(0,1fr) minmax(0,1fr); grid-template-rows:repeat(6,auto); --vis:clamp(168px,16.4vw,236px)}
.nw__tag.sticker{position:absolute; z-index:5; left:50%; top:0; margin:0; transform:translate(-50%,-58%) rotate(-3deg); font-size:clamp(1rem,1.45vw,1.3rem); line-height:1; letter-spacing:.01em; white-space:nowrap; padding:.55em .95em .5em}
.nw__half{position:relative; min-width:0; overflow:hidden; grid-row:1 / span 6; display:grid; grid-template-rows:subgrid; grid-template-columns:minmax(0,1fr); align-items:start; padding-block:clamp(64px,6.4vw,92px) clamp(52px,5.2vw,76px)}
.nw__half > *{position:relative; z-index:1; min-width:0}
.nw-ai{background-color:var(--aqua); background-image:radial-gradient(rgba(19,132,143,.22) 1.1px, transparent 1.5px); background-size:18px 18px; color:var(--slate);
  padding-inline:max(var(--gutter), calc(50vw - var(--wrap)/2 + var(--gutter))) clamp(28px,4vw,64px)}
.nw-ch{background-color:var(--slate); background-image:var(--grain); color:#fff;
  padding-inline:clamp(28px,4vw,64px) max(var(--gutter), calc(50vw - var(--wrap)/2 + var(--gutter)))}
.nw__kick{margin:0 0 20px; align-self:center}
.nw__vis{margin:0 0 30px; align-self:center}
.nw__half h3{margin:0 0 .4em}
.nw__text{font-size:1.04rem; line-height:1.6; margin:0 0 24px}
.nw__steps{list-style:none; margin:0 0 28px; padding:0; display:grid; gap:6px; position:relative}
.nw__steps li{margin:0}
.nw__half .btns{margin:0; align-self:end}

/* AI Literacy half: the training's hand-drawn look */
.nw-ai__facts{display:flex; flex-wrap:wrap; gap:7px; padding:0; list-style:none}
.nw-ai__facts li{margin:0; font-family:var(--hand); font-weight:700; font-size:.95rem; line-height:1; padding:7px 11px 8px; border-radius:10px; border:2px solid var(--slate); background:#fff}
.nw-ai__facts li:first-child{background:var(--mint)}
.nw-ai__vis{display:grid; grid-template-columns:auto minmax(0,1fr); gap:clamp(18px,2.2vw,30px); align-items:center}
.nw-ai__fig{margin:0; position:relative; transform:rotate(-2deg)}
.nw-ai__fig img{height:var(--vis); width:auto; aspect-ratio:1200/834; object-fit:cover; border-radius:16px; border:2px solid var(--slate); box-shadow:7px 7px 0 var(--teal)}
.nw-ai__fig figcaption{position:absolute; left:-10px; bottom:-13px; font-family:var(--hand); font-weight:700; font-size:.88rem; line-height:1; background:#fff; border:2px solid var(--slate); border-radius:8px; padding:6px 9px 7px; transform:rotate(-3deg)}
.nw-ai__launch{font-family:var(--hand); font-size:clamp(1.02rem,1.3vw,1.18rem); line-height:1.42; margin:0}
.nw-loop{position:relative; display:inline-block; font-weight:700; margin:.5em 0 0 .5em; white-space:nowrap}
.nw-loop__svg{position:absolute; left:-.6em; right:-.55em; top:-.4em; bottom:-.42em; width:calc(100% + 1.15em); height:calc(100% + .82em); color:var(--teal); overflow:visible; pointer-events:none}
.nw-loop__svg path{stroke-dasharray:1; stroke-dashoffset:0; transition:stroke-dashoffset 1.2s .25s var(--ease)}
.js .nw-ai__launch.reveal.pre .nw-loop__svg path{stroke-dashoffset:1}
.nw-ai h3{font-family:var(--hand); font-weight:700; font-stretch:100%; font-size:clamp(1.9rem,3.15vw,2.85rem); line-height:1.1; letter-spacing:-.005em}
.nw-ai h3 .br{background:__BRUSH__ center/100% 100% no-repeat; color:#fff; padding:.02em .24em .1em; margin:0 -.06em; white-space:nowrap; -webkit-box-decoration-break:clone; box-decoration-break:clone}
.nw-map{grid-template-columns:repeat(6,minmax(0,1fr)); counter-reset:m}
.nw-map::before{content:""; position:absolute; left:8%; right:8%; top:15px; height:12px; background:__WAVE__ center/100% 100% no-repeat}
.nw-map li{position:relative; display:flex; flex-direction:column; align-items:center; gap:7px; text-align:center; font-family:var(--hand); font-size:.9rem; line-height:1.15; font-weight:700; counter-increment:m}
.nw-map li::before{content:counter(m); display:grid; place-items:center; width:40px; height:40px; border-radius:50%; border:2px solid var(--slate); background:#fff; font-size:1.05rem; transition:transform .25s var(--ease), background .25s}
.nw-map li:hover::before{transform:translateY(-3px) rotate(-6deg); background:var(--mint)}

/* Choking Hazard half: the campaign's product warning label (safety yellow lives on the label only) */
.nw-ch .eyebrow{color:var(--mint)}
.ch-label{display:block; width:calc(var(--vis) * 1.93); max-width:100%; container-type:inline-size; background:var(--hz); color:var(--hz-ink); border-radius:14px; padding:2.4% 2.6%; text-decoration:none;
  box-shadow:0 26px 50px -26px rgba(0,0,0,.75); transform:rotate(-2.2deg); transition:transform .55s cubic-bezier(.3,1.45,.5,1), opacity .35s}
.ch-label__in{display:flex; flex-direction:column; align-items:center; text-align:center; border:max(2px,.55cqi) solid var(--hz-ink); border-radius:9px; padding:4.5cqi 4cqi 3.6cqi; font-family:var(--display); font-weight:900; font-stretch:108%; text-transform:uppercase; line-height:1}
.ch-label__w{display:flex; align-items:center; gap:3cqi; font-size:12.2cqi; letter-spacing:.01em; font-stretch:106%}
.ch-label__w, .ch-label__a, .ch-label__b{white-space:nowrap}
.ch-label__w svg{width:.95em; height:.84em; flex:none; transform:translateY(-.04em)}
.ch-label__a{font-size:6.6cqi; margin-top:4.6cqi; letter-spacing:.01em; font-stretch:100%}
.ch-label__b{font-size:3.72cqi; margin-top:1.8cqi; letter-spacing:.015em; font-stretch:100%}
.ch-label__c{font-size:3.9cqi; margin-top:5cqi; text-transform:none; font-weight:800; font-stretch:100%}
a.ch-label:hover{transform:rotate(0deg) scale(1.015)}
.js .ch-label.reveal.pre{transform:rotate(9deg) scale(1.16); opacity:0}
.nw-ch h3{font-size:clamp(1.8rem,3vw,2.7rem); font-weight:900; font-stretch:114%; line-height:1.02; letter-spacing:-.015em}
.nw-ch .nw__text{color:rgba(255,255,255,.9)}
.nw-gives{grid-template-columns:repeat(4,minmax(0,1fr))}
.nw-gives::before{content:""; position:absolute; left:12%; right:12%; top:19px; border-top:2px dashed rgba(21,255,200,.45)}
.nw-gives a{position:relative; display:flex; flex-direction:column; align-items:center; gap:7px; text-align:center; text-decoration:none; color:#fff; font-weight:700; font-size:.9rem; line-height:1.2}
.nw-gives a::before{content:"!"; display:grid; place-items:center; width:40px; height:40px; border-radius:50%; border:2px solid var(--mint); background:var(--slate); color:var(--mint); font-family:var(--display); font-weight:900; font-size:1.2rem; line-height:1; transition:transform .25s var(--ease), background .25s, color .25s}
.nw-gives a:hover::before, .nw-gives a:focus-visible::before{transform:translateY(-3px); background:var(--mint); color:var(--slate)}
.nw-gives a:hover{color:var(--mint)}
@supports not (grid-template-rows:subgrid){
  .nw__half{display:flex; flex-direction:column}
  .nw__kick,.nw__vis{align-self:flex-start}
  .nw__half .btns{margin-top:auto; align-self:flex-start}
}
@media (max-width:1180px) and (min-width:1001px){
  .nw__half .btns{flex-wrap:nowrap; gap:10px}
  .nw__half .btn{padding-inline:.95em; font-size:.95rem; white-space:nowrap}
}
@media (max-width:1000px){
  .nw{grid-template-columns:minmax(0,1fr); grid-template-rows:none; --vis:clamp(168px,30vw,236px)}
  .nw__half{grid-row:auto; display:flex; flex-direction:column; align-items:stretch; padding-block:64px 52px}
  .nw-ai, .nw-ch{padding-inline:var(--gutter)}
  .nw__kick,.nw__vis{align-self:flex-start}
  .nw__half .btns{align-self:flex-start}
  .nw__tag.sticker{left:var(--gutter); transform:translate(0,-58%) rotate(-3deg)}
}
@media (max-width:560px){
  .nw-ai__vis{grid-template-columns:minmax(0,1fr); gap:22px}
  .nw-ai__fig{justify-self:start; margin-left:4px}
  .nw-loop{margin:.2em .4em}
  .nw-map{grid-template-columns:repeat(3,minmax(0,1fr)); row-gap:16px}
  .nw-map::before{display:none}
  .nw-gives{grid-template-columns:repeat(2,minmax(0,1fr)); row-gap:16px}
  .nw-gives::before{display:none}
}

/* ---------- Vibe Check: the flagship tool, a full teal band ---------- */
.vb{overflow:hidden}
.vb__grid{display:grid; grid-template-columns:repeat(12,minmax(0,1fr)); column-gap:var(--gap); align-items:center}
.vb__copy{grid-column:1 / span 7; grid-row:1; min-width:0}
.vb__stage{grid-column:8 / span 5; grid-row:1; position:relative; display:grid; place-items:center; align-self:stretch}
.vb__mark{display:flex; align-items:center; gap:12px; font-family:var(--display); font-weight:900; font-stretch:115%; font-size:1.3rem; line-height:1; color:var(--mint); margin:0 0 22px}
.vb__mark .daisy{width:42px; height:42px}
.qs{position:relative; --qs:clamp(2.15rem,4.6vw,4.2rem); font-size:var(--qs); height:calc(var(--qs) * 2.12); overflow:hidden; margin:0 0 .34em}
.qs span{position:absolute; inset:0; display:flex; align-items:flex-end; padding-bottom:.07em; font-weight:900; font-stretch:118%; line-height:1; letter-spacing:-.02em; color:#fff; transform:translateY(110%); opacity:0; transition:transform .7s cubic-bezier(.2,.8,.2,1), opacity .7s}
.qs span.on{transform:none; opacity:1}
.qs span.out{transform:translateY(-110%); opacity:0}
.vb .lede{color:#fff}
.vb__more{color:rgba(255,255,255,.9); margin-bottom:1.5em}
.vb__btns{gap:12px 22px}
.vb .vb__pdf{display:inline-flex; gap:.4em; align-items:center; min-height:44px; color:#fff; font-family:var(--display); font-weight:800; font-stretch:106%; text-decoration:underline; text-decoration-color:var(--mint); text-decoration-thickness:2px; text-underline-offset:5px}
.vb .vb__pdf:hover{color:var(--mint)}
.vb__press{display:flex; flex-wrap:wrap; gap:16px 36px; align-items:center; margin-top:30px; padding-top:22px; border-top:1px solid rgba(255,255,255,.28)}
.vb__press img{height:32px; width:auto; filter:brightness(0) invert(1); opacity:.95}
.vb__press span{font-family:var(--mono); font-size:.74rem; letter-spacing:.1em; text-transform:uppercase; color:#fff}
.vb__disc{position:absolute; left:50%; top:50%; width:min(100%,500px); aspect-ratio:1; border-radius:50%; background:var(--logo-teal); transform:translate(-50%,-50%)}
.vb__disc::after{content:""; position:absolute; inset:-7%; border-radius:50%; border:2px dashed rgba(209,254,255,.4)}
.phone-wrap{position:relative; z-index:1}
.phone{position:relative; width:clamp(240px,25vw,338px); aspect-ratio:390/800; border-radius:46px; border:11px solid #0b1f25; background:#0b1f25; box-shadow:0 50px 90px -30px rgba(0,0,0,.6), 0 0 0 2px rgba(255,255,255,.08); overflow:hidden; transform:rotate(-4deg); transition:transform .6s var(--ease)}
.phone-wrap:hover .phone{transform:rotate(-1.5deg) translateY(-6px)}
.phone img{width:100%; height:100%; object-fit:cover; object-position:top}
.phone-wrap .sticker{position:absolute; z-index:2}
@media (max-width:900px){
  .vb__grid{display:flex; flex-direction:column; align-items:stretch}
  .vb__copy{display:contents}
  .vb__head{order:1} .vb__stage{order:2} .vb__body{order:3}
  .vb__stage{margin:14px 0 34px; padding-block:14px}
  .vb__disc{width:min(92%,440px)}
  .phone{width:min(270px,66vw)}
}
@media (max-width:560px){
  .vb__press{gap:12px 28px}
  .vb__press span{flex-basis:100%}
  .vb__press img{height:28px}
}

/* ---------- Certified Peer Educator Training ---------- */
.cp{display:grid; grid-template-columns:repeat(12,minmax(0,1fr)); gap:var(--gap); align-items:stretch}
.cp > .player{grid-column:span 7}
.cp__side{grid-column:span 5; min-width:0; display:flex; flex-direction:column; gap:var(--gap)}
.cp__facts{flex:1; list-style:none; margin:0; padding:0; display:grid; grid-template-rows:repeat(3,minmax(0,1fr)); background:#fff; border:1px solid var(--line); border-radius:var(--r-xl); overflow:hidden}
.cp__facts li{margin:0; display:grid; grid-template-columns:minmax(0,11.6rem) minmax(0,1fr); align-items:center; gap:18px; padding:10px var(--pad-card); border-top:1px solid var(--line)}
.cp__facts li:first-child{border-top:0}
.cp__facts b{font-family:var(--display); font-weight:900; font-stretch:122%; font-size:clamp(2rem,3vw,2.7rem); line-height:1; letter-spacing:-.02em; color:var(--logo-teal)}
.cp__facts span{font-weight:600; font-size:1.02rem; line-height:1.3}
.cp__btns{display:grid; grid-template-columns:repeat(2,minmax(0,1fr)); gap:12px}
.cp__btns .btn:first-child{grid-column:1 / -1}
.cp__note{display:flex; align-items:center; gap:12px; margin:var(--gap) 0 0; padding-top:18px; border-top:1px solid var(--line); font-size:.95rem; font-weight:500; color:var(--ink-soft)}
.cp__note .daisy{width:22px; height:22px; color:var(--teal)}
@media (max-width:960px){
  .cp{grid-template-columns:minmax(0,1fr)}
  .cp > .player,.cp__side{grid-column:auto}
  .cp__facts li{min-height:72px}
}
@media (max-width:480px){ .cp__btns{grid-template-columns:minmax(0,1fr)} .cp__facts li{grid-template-columns:minmax(0,8.4rem) minmax(0,1fr); gap:12px} .cp__facts b{font-size:1.9rem} }

/* ---------- Library ---------- */
.lib__nav{display:flex; gap:8px}
.lib__nav button{width:48px; height:48px; border-radius:50%; border:2px solid rgba(209,254,255,.4); background:transparent; color:#fff; font-size:1.35rem; line-height:1; cursor:pointer; transition:background .2s, color .2s, border-color .2s}
.lib__nav button:hover{background:var(--mint); border-color:var(--mint); color:var(--slate)}
.lib__nav button[disabled]{opacity:.35; cursor:default; background:transparent; border-color:rgba(209,254,255,.4); color:#fff}
.lib__tools{display:flex; flex-wrap:wrap; gap:14px var(--gap); align-items:center; min-width:0}
.libsearch{flex:1 1 min(380px,100%); min-width:0; display:flex; gap:10px; margin:0}
.libsearch input{flex:1; min-width:0; font:inherit; font-size:1.05rem; padding:13px 16px; border-radius:10px; border:2px solid rgba(255,255,255,.28); background:rgba(255,255,255,.06); color:#fff}
.libsearch input::placeholder{color:rgba(209,254,255,.75)}
.libsearch input:focus{outline:0; border-color:var(--mint)}
.libcounts{display:flex; flex-wrap:wrap; gap:8px}
.libcounts a{display:inline-flex; align-items:center; min-height:44px; font-family:var(--mono); font-size:.76rem; letter-spacing:.06em; text-transform:uppercase; text-decoration:none; padding:0 13px; border-radius:10px; border:1.5px solid rgba(209,254,255,.38); color:var(--aqua); transition:border-color .2s, color .2s}
.libcounts a:hover{border-color:var(--mint); color:var(--mint)}
.home .fstrip{margin-top:var(--head-gap); grid-auto-columns:clamp(216px,20.3vw,272px); gap:var(--gap); padding:4px var(--gutter) 20px max(var(--gutter), calc(50vw - var(--wrap)/2 + var(--gutter))); scroll-padding-left:max(var(--gutter), calc(50vw - var(--wrap)/2 + var(--gutter))); scrollbar-color:rgba(209,254,255,.4) transparent}
.home .fcard{border-radius:var(--r-xl)}
.home .fcard__tag{top:14px; left:14px}
.home .fcard__title{left:18px; right:18px; bottom:46px}
.home .fcard__go{left:18px; bottom:18px; font-size:.72rem}
@media (max-width:700px){ .lib__nav{display:none} }
@media (max-width:560px){
  .libcounts{display:grid; grid-template-columns:repeat(2,minmax(0,1fr)); width:100%}
  .libcounts a{padding:8px 12px; line-height:1.3}
}

/* ---------- SafeBAE 360: dial, selector and readout as one instrument ---------- */
.tsx{display:grid; grid-template-columns:4fr 3fr 5fr; border:1px solid var(--line); border-radius:var(--r-xl); overflow:hidden; background:#fff; box-shadow:var(--shadow-soft)}
.tsx__dial{display:grid; place-items:center; padding:clamp(22px,2.6vw,36px); background:var(--mist); border-right:1px solid var(--line)}
.ring{width:100%; max-width:330px; display:block; overflow:visible}
.seg{cursor:pointer; outline:none; transition:transform .35s var(--ease)}
.seg path{transition:opacity .25s}
.ring.has-active .seg:not(.on) path{opacity:.8}
.seg:focus-visible path{stroke:#1d414e; stroke-width:4}
__SEGPUSH__
.tsx__list{display:grid; grid-template-rows:repeat(6,minmax(0,1fr))}
.tsx__list button{display:grid; grid-template-columns:auto minmax(0,1fr); align-items:center; gap:13px; padding:10px 18px; min-height:60px; text-align:left; font:inherit; border:0; border-top:1px solid var(--line); background:#fff; color:var(--slate); cursor:pointer; transition:background .2s, color .2s}
.tsx__list button:first-child{border-top:0}
.tsx__list i{font-style:normal; width:32px; height:32px; border-radius:50%; background:var(--c); color:var(--k); display:grid; place-items:center; font-family:var(--display); font-weight:900; font-size:.98rem; line-height:1; transition:box-shadow .2s}
.tsx__list span{font-family:var(--display); font-weight:800; font-stretch:104%; font-size:1rem; line-height:1.2}
.tsx__list button:hover{background:var(--mist)}
.tsx__list button[aria-selected="true"]{background:var(--slate); color:#fff}
.tsx__list button[aria-selected="true"] i{box-shadow:0 0 0 2px #fff}
.tsx__list button:focus-visible{outline-offset:-3px}
.tsx__read{display:grid; gap:28px; background-color:var(--slate); background-image:var(--grain); color:#fff; padding:clamp(24px,2.8vw,38px)}
.tsx__pane{display:flex; flex-direction:column; align-items:flex-start}
/* with scripts on, the six panes share one cell so the unit keeps one height */
.js .tsx__pane{grid-area:1 / 1; visibility:hidden; opacity:0; transform:translateY(8px); transition:opacity .3s, transform .4s var(--ease), visibility 0s .3s}
.js .tsx__pane.on{visibility:visible; opacity:1; transform:none; transition:opacity .3s, transform .4s var(--ease), visibility 0s}
.tsx__n{display:block; font-family:var(--display); font-weight:900; font-stretch:125%; font-size:clamp(2.6rem,4vw,3.6rem); line-height:.9; color:var(--mint); margin-bottom:.22em}
.tsx__pane h3{font-size:clamp(1.3rem,1.9vw,1.6rem); margin:0 0 .5em}
.tsx__pane p{font-size:1rem; line-height:1.58; color:rgba(255,255,255,.9); margin:0 0 1.2em}
.tsx__pane .arrow-link{margin-top:auto; color:var(--mint); min-height:44px}
.tsx__foot{grid-column:1 / -1; display:flex; flex-wrap:wrap; align-items:center; justify-content:space-between; gap:14px 28px; padding:16px clamp(18px,2.4vw,30px); background:var(--mist); border-top:1px solid var(--line)}
.tsx__foot p{margin:0; flex:1 1 300px; font-weight:600; font-size:1.02rem; line-height:1.4; text-wrap:balance}
.tsx__foot .btns{margin:0}
@media (max-width:1100px){
  .tsx{grid-template-columns:minmax(0,5fr) minmax(0,7fr)}
  .tsx__dial{border-bottom:1px solid var(--line)}
  .tsx__list{order:3; grid-column:1 / -1; grid-template-rows:none; grid-template-columns:repeat(3,minmax(0,1fr))}
  .tsx__foot{order:4}
  .tsx__list button{border-top:1px solid var(--line); border-left:1px solid var(--line)}
  .tsx__list button:first-child{border-top:1px solid var(--line)}
  .tsx__list button:nth-child(3n+1){border-left:0}
  .tsx__list button:nth-child(-n+3){border-top:0}
}
@media (max-width:700px){
  .tsx{grid-template-columns:minmax(0,1fr)}
  .tsx__dial{border-right:0}
  .ring{max-width:270px}
  .tsx__list{order:0; grid-template-columns:minmax(0,1fr)}
  .tsx__list button, .tsx__list button:nth-child(3n+1){border-left:0}
  .tsx__list button:nth-child(-n+3){border-top:1px solid var(--line)}
  .tsx__list button:first-child{border-top:0}
}

/* ---------- SafeBAE x REES ---------- */
.rs{display:grid; grid-template-columns:minmax(0,7fr) minmax(0,5fr); gap:clamp(28px,4vw,56px); align-items:stretch}
.rs__copy{min-width:0; display:flex; flex-direction:column; justify-content:center; padding-block:6px}
.rs__copy .lede{color:rgba(255,255,255,.9); max-width:none}
.rs__card{min-width:0; display:flex; flex-direction:column; background:#fff; color:var(--slate); border-radius:var(--r-xl); overflow:hidden; box-shadow:0 34px 60px -34px rgba(0,0,0,.7)}
.rs__lock{display:flex; align-items:center; gap:16px; padding:18px var(--pad-card); background:var(--aqua); border-bottom:1px solid var(--line)}
.rs__lock svg{width:112px; height:auto; color:var(--logo-teal); flex:none}
.rs__lock i{font-style:normal; font-family:var(--mono); font-weight:600; font-size:1rem; color:var(--logo-teal)}
.rs__lock img{height:42px; width:auto}
.rs__lock em{margin-left:auto; font-style:normal; font-family:var(--mono); font-size:.72rem; font-weight:600; letter-spacing:.1em; text-transform:uppercase; color:var(--logo-teal); text-align:right; line-height:1.5; max-width:10em; text-wrap:balance}
.rs__feats{flex:1; list-style:none; margin:0; padding:0; display:grid; grid-template-rows:repeat(3,auto); align-content:stretch}
.rs__feats li{margin:0; padding:clamp(16px,1.7vw,22px) var(--pad-card); border-top:1px solid var(--line); display:grid; grid-template-columns:auto minmax(0,1fr); column-gap:16px; align-content:center}
.rs__feats li:first-child{border-top:0}
.rs__feats li::before{content:""; width:11px; height:11px; margin-top:.45em; background:var(--teal); transform:rotate(45deg); grid-row:1 / span 2}
.rs__feats b{font-family:var(--display); font-weight:800; font-stretch:106%; font-size:1.24rem; line-height:1.2; color:var(--logo-teal)}
.rs__feats p{margin:.3em 0 0; font-size:1rem; line-height:1.5; color:var(--ink-soft)}
@media (max-width:900px){ .rs{grid-template-columns:minmax(0,1fr)} }
@media (max-width:1180px){ .rs__lock em{display:none} }

/* ---------- stats ---------- */
.home .stat b{font-variant-numeric:tabular-nums}

/* ---------- partner voice: quote, a vertical video, the logos ---------- */
.pq{display:grid; grid-template-columns:repeat(12,minmax(0,1fr)); gap:var(--gap); align-items:stretch}
.pq__quote{grid-column:span 9; margin:0; min-width:0; display:flex; flex-direction:column; justify-content:center; background-color:var(--slate); background-image:var(--grain); color:#fff; border-radius:var(--r-xl); padding:clamp(26px,3.6vw,52px)}
.pq__quote .quote{font-size:clamp(1.22rem,2.02vw,1.82rem); line-height:1.28}
.pq__quote .quote::before{color:var(--mint); font-size:3.4em; line-height:.62}
.pq__quote .cite{margin-top:22px; color:var(--aqua); font-size:.8rem}
.home .pq__vid{grid-column:span 3; aspect-ratio:9/16; border-radius:var(--r-xl); align-self:stretch}
.pq__vid img{opacity:.92}
.pq__vid .vid__play span{width:72px; height:72px}
.pq__vid .vid__label{flex-direction:column; align-items:flex-start; gap:4px; padding:13px 16px 14px}
.pq__logos{margin-top:var(--head-gap); padding-top:var(--gap); border-top:1px solid var(--line); display:grid; grid-template-columns:repeat(7,minmax(0,1fr)); gap:6px 0; align-items:center}
.pq__logos .eyebrow{margin:0; padding-right:16px; line-height:1.55; text-wrap:balance}
.pq__strip{display:contents; list-style:none}
.pq__strip li{margin:0; height:88px; padding:14px 16px}
.pq__strip img{width:100%; height:100%; object-fit:contain; filter:grayscale(1) contrast(1.1); opacity:.82; mix-blend-mode:multiply; transition:filter .3s, opacity .3s}
.pq__strip li:hover img{filter:none; opacity:1}
@media (max-width:1000px){
  .pq__quote{grid-column:span 8} .home .pq__vid{grid-column:span 4}
  .pq__logos{display:block}
  .pq__logos .eyebrow{margin-bottom:6px; padding:0}
  .pq__strip{margin:0; padding:0; display:grid; grid-template-columns:repeat(10,minmax(0,1fr)); gap:6px 0; align-items:center}
  .pq__strip li{grid-column:span 2}
  .pq__strip li:nth-child(1),.pq__strip li:nth-child(10){grid-column:2 / span 2}
}
@media (max-width:700px){
  .pq{grid-template-columns:minmax(0,1fr)}
  .pq__quote,.home .pq__vid{grid-column:auto}
  .home .pq__vid{width:min(100%,300px); justify-self:center}
  .pq__strip{grid-template-columns:repeat(6,minmax(0,1fr))}
  .pq__strip li{height:76px; padding:12px 12px}
  .pq__strip li:nth-child(1),.pq__strip li:nth-child(10){grid-column:span 2}
  .pq__strip li:nth-child(4),.pq__strip li:nth-child(9){grid-column:2 / span 2}
}

/* ---------- podcasts ---------- */
.pods{display:grid; grid-template-columns:repeat(3,minmax(0,1fr)); gap:var(--gap)}
.pod{display:grid; grid-template-columns:104px minmax(0,1fr); gap:18px; align-items:center; padding:14px 18px 14px 14px; background:#fff; border:1px solid var(--line); border-radius:var(--r-xl); text-decoration:none; color:inherit; transition:transform .2s var(--ease), box-shadow .2s var(--ease)}
.pod:hover{transform:translateY(-4px); box-shadow:var(--shadow-soft)}
.pod__art{position:relative; display:block}
.pod img{width:104px; height:104px; object-fit:cover; border-radius:12px; background:var(--mist)}
.pod small{display:block; font-family:var(--mono); font-size:.72rem; font-weight:600; letter-spacing:.08em; text-transform:uppercase; color:var(--logo-teal); margin-bottom:6px; line-height:1.3}
.pod b{display:block; font-family:var(--display); font-weight:800; font-stretch:104%; font-size:1.1rem; line-height:1.2; color:var(--slate)}
.pod__go{position:absolute; right:-10px; bottom:-8px; width:38px; height:38px; border-radius:50%; display:grid; place-items:center; background:var(--mint); color:var(--slate); border:3px solid #fff; transition:transform .2s var(--ease)}
.pod__go svg{width:14px; height:14px; margin-left:2px}
.pod:hover .pod__go{transform:scale(1.12)}
@media (max-width:1100px){ .pods{grid-template-columns:repeat(2,minmax(0,1fr))} }
@media (max-width:700px){ .pods{grid-template-columns:minmax(0,1fr)} .pod{grid-template-columns:84px minmax(0,1fr); gap:18px} .pod img{width:84px; height:84px} }

/* ---------- #ForDaisy: her portrait at the heart of the drawn daisy ---------- */
.fdz{overflow:hidden}
.fd{display:grid; grid-template-columns:repeat(12,minmax(0,1fr)); column-gap:var(--gap); align-items:center}
.fd__art{grid-column:1 / span 6; grid-row:1; position:relative; width:144%; margin-left:-42%; aspect-ratio:1100/852}
.fd__copy{grid-column:7 / span 6; grid-row:1; min-width:0}
.fd__art .daisy-art{position:absolute; inset:0; color:var(--mint); opacity:.62}
.fd__face{position:absolute; left:48.6%; top:46.6%; width:37%; aspect-ratio:1; transform:translate(-50%,-50%); border-radius:50%; overflow:hidden; border:4px solid var(--mint); box-shadow:0 0 0 9px var(--slate-deep), 0 30px 60px -20px rgba(0,0,0,.6)}
.fd__face img{width:100%; height:100%; object-fit:cover; object-position:44% 18%}
.fd__work{position:absolute; left:63.5%; top:55%; width:19.5%; display:block; transform:rotate(5deg); transition:transform .35s var(--ease); text-decoration:none; z-index:2}
.fd__work img{width:100%; aspect-ratio:4/5; object-fit:cover; object-position:60% 40%; border-radius:14px; border:5px solid #fff; box-shadow:0 20px 40px -18px rgba(0,0,0,.7)}
.fd__work .sticker{position:absolute; left:-16px; bottom:14px; font-size:.78rem; white-space:nowrap}
.fd__work:hover{transform:rotate(1deg) scale(1.04)}
.fd__head h2{margin-bottom:.5em}
.home .nb{white-space:nowrap}
.fd__body .lede{color:rgba(255,255,255,.9); max-width:none; margin-bottom:.7em}
.fd__more{font-size:var(--fs-lede); line-height:1.55; font-weight:500; color:rgba(255,255,255,.9); margin:0}
.fd__quote{position:relative; font-family:var(--display); font-stretch:104%; font-weight:600; font-size:1.18rem; line-height:1.4; padding-left:48px; margin:24px 0 26px; color:var(--aqua)}
.fd__quote::before{content:"\201C"; position:absolute; left:0; top:-.12em; font-size:3.4rem; line-height:1; font-weight:900; color:var(--mint)}
.fd__quote cite{display:block; margin-top:8px; font-style:normal; font-family:var(--mono); font-size:.85rem; font-weight:500; color:rgba(255,255,255,.76)}
.fd__acts{gap:12px 22px}
.fd__acts .arrow-link{min-height:44px}
@media (max-width:1100px){
  .fd__art{grid-column:1 / span 5; width:150%; margin-left:-44%}
  .fd__work{width:23%; left:62%}
  .fd__work .sticker{left:-22px; bottom:10px}
  .fd__copy{grid-column:6 / span 7}
}
@media (max-width:1000px){
  .fd{display:flex; flex-direction:column; align-items:stretch}
  .fd__copy{display:contents}
  .fd__head{order:1} .fd__art{order:2} .fd__body{order:3}
  .fd__art{width:min(132%,640px); margin:0 0 6px calc(50% - min(66%,320px)); align-self:flex-start}
  .fd__work .sticker{font-size:.72rem; left:-12px; bottom:10px}
}
'''
HOME_CSS = (HOME_CSS.replace('__BRUSH__', _brush('#13848f', '0.88')).replace('__WAVE__', _wave('#1d414e'))
            .replace('__SEGPUSH__', _SEG_PUSH))

ICON_OUT = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.6" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M7 17 17 7M9 7h8v8"/></svg>'


# where the subject sits in each audience photo (the frame is tall on desktop, wide on phones)
WHO_POS = {'educator': 'object-position:24% 50%', 'parent': 'object-position:58% 40%', 'help': 'object-position:52% 60%', 'student': 'object-position:50% 40%'}


def _row_multi(title, desc_html, href, meta=None):
    """A row whose whole surface goes to `href` while a word in the description links elsewhere."""
    m = f'<div class="row__meta">{"".join(f"<span class=chip>{esc(x)}</span>" for x in meta)}</div>' if meta else ''
    return (f'<div class="row row--multi"><span><b><a class="row__main" href="{esc(href)}">{esc(title)}</a></b>'
            f'<small>{desc_html}</small>{m}</span><span class="go" aria-hidden="true">&rarr;</span></div>')


def home():
    wall_cols = [
      ['000422', 'clubhero', 'img-2395', 'dsc01134', '2023-institute-selfie', 'img-9509-1'],
      ['1-000383-edited', 'clubtabling', '000263', 'sumact5', 'p1002709', 'img-6620'],
      ['000398', '066', 'img-1286', '1-54982e7a-41f6-4540-a03d-2bd16547a2fa', 'img-3755', 'safebae-consent-summits'],
    ]
    cols = ''.join('<div class="hero__col">' + ''.join(img(n, '', loading='eager' if i < 4 else 'lazy') for i, n in enumerate(c)) + '</div>' for c in wall_cols)

    who = [
      ('student', 'I’m a', 'student', '1-000383-edited', 'Lead prevention at your school', 'SafeBAE was founded by teen survivors who wanted their schools to change. Everything here is free for students.', [
         ('Become a Certified Peer Educator', 'Free, self-paced, 16 online modules and an official certificate.', 'peer-educator.html', ['Free', '16 modules']),
         ('SafeBAE AI Literacy Training', 'Six free, self-paced modules on how AI works and what it means for relationships, consent and privacy. Launches October 26–30, 2026.', 'ai-literacy.html', ['New', 'Ages 13+']),
         ('Start or join a SafeBAE club', 'Register a new chapter, affiliate a club you already run, or restart last year’s.', 'clubs.html', ['Club Hub access']),
         ('Practice in the BAE Skills Lab', 'Short interactive activities about consent, boundaries and healthy relationships.', 'skills-lab.html', ['Games']),
         ('Know your rights under Title IX', 'What your school owes you, and how to find your Title IX Coordinator.', 'title-ix.html', ['Rights'])]),
      ('parent', 'I’m a', 'parent or caregiver', 'us-sometale-parent', 'Support the young people in your life', 'Young people look to the adults around them for cues about relationships, boundaries and safety.', [
         ('Parents & caregivers', 'Early conversations, supporting a survivor, reporting options and alternative justice.', 'parents.html', ['Start here']),
         ('Choking Hazard: what adults should know', 'SafeBAE’s campaign on sexual strangulation, which young people call “choking”: the evidence, myth vs. fact, and signs that need medical care.', 'choking-hazard.html', ['New']),
         ('Check Their Vibe: an adult’s guide', 'How to share Vibe Check with a young person and keep it voluntary.', 'https://www.safebae.org/wp-content/uploads/2026/03/Check-Their-Vibe-A-Guide-to-Vibe-Check.pdf', ['PDF guide']),
         ('Listen: How to Not (Accidentally) Raise a Rapist', 'Shael Norris on The Longest Shortest Time.', 'library.html#parenting', ['Podcast']),
         ('If your child tells you something happened', 'Believe first, avoid blame, seek support, and care for yourself.', 'survivor-support.html', ['Support'])]),
      ('educator', 'I’m an', 'educator', 'img-2395', 'Bring youth-led prevention to your classroom', 'Start wherever you can. Every film comes with a ready-to-teach guide built for short, meaningful discussions.', [
         ('Films & teaching guides', 'Youth-made films, each paired with discussion prompts and activities.', 'library.html#guides', ['8 guides']),
         ('Healthy Relationship & Consent Curriculum', '15 lessons aligned with the National Health Education Standards.', 'consent-curriculum.html', ['NHES']),
         ('SafeBAE AI Literacy Training', 'Six free modules for high school and college students. Educators can register for group access.', 'ai-literacy.html', ['New', 'Free']),
         ('Choking Hazard and Sexual Strangulation Prevention', 'Evidence and free warning posters from the campaign now. SafeBAE’s school program launches November 2026.', 'choking-hazard.html#schools', ['New']),
         ('Bring SafeBAE to your school', '<a href="assemblies.html">Assemblies</a>, staff training and the full 360° Schools model.', 'request-a-program.html', ['Sliding scale'], 'multi'),
         ('Free prevention posters', 'For classrooms, counseling offices, hallways and wellness centers.', 'posters.html', ['Download'])]),
      ('college', 'I’m in', 'college', '1-7c1d4302-803a-4154-b18a-3a64432a6c76', 'Change the schools you came from', 'Mentor high schoolers, start a campus chapter, and get certified.', [
         ('Become a college mentor', 'Help high school students build clubs and push for safer policies.', 'college.html', ['Mentorship']),
         ('Start a SafeBAE club on campus', 'Resources, training and support for events, campaigns and advocacy.', 'clubs.html', ['Clubs']),
         ('Certified Peer Educator Training', 'Certified students are prioritized for paid mentorship opportunities.', 'peer-educator.html', ['Free'])]),
      ('help', 'I', 'need support', '000263', 'You are not alone', 'If something happened to you or a friend, or you’re worried about something you did, start here.', [
         ('Talk to someone now', 'Free, confidential hotlines, most open 24/7.', 'survivor-support.html#hotlines', ['24/7']),
         ('How to support a friend', 'What to say, what to avoid, and how to let them lead.', 'survivor-support.html', ['Support']),
         ('If someone choked you', 'Signs that mean you should go to an ER today, even with no marks and even if you agreed to it.', 'choking-hazard.html#er', ['Medical care']),
         ('Worried you crossed a line?', 'Vibe Check is anonymous. Nothing is stored or reported.', 'https://checkyourvibe.org/', ['Anonymous']),
         ('Document what happened, privately', 'A free, encrypted record with REES, at your own pace.', 'https://safebae.reessecureus.com/en/Login', ['Private']),
         ('Your options at school', 'Title IX, supportive measures and reporting options.', 'title-ix.html', ['Rights'])]),
    ]

    def _rows(rows):
        return ''.join(_row_multi(*r[:4]) if len(r) > 4 else row(*r) for r in rows)

    tabs = ''.join(f'<button class="who__tab{" who__tab--help" if k=="help" else ""}" role="tab" id="who-{k}" aria-controls="whop-{k}" aria-selected="{str(i==0).lower()}" tabindex="{0 if i==0 else -1}"><small>{esc(pre)}</small><span>{esc(lbl)}</span></button>' for i, (k, pre, lbl, *_r) in enumerate(who))
    panels = ''.join(f'''<div class="who__panel" role="tabpanel" id="whop-{k}" aria-labelledby="who-{k}"{'' if i==0 else ' hidden'}>
      <div class="who__img">{img(im, '', style=WHO_POS.get(k, ''))}{'<span class="sticker sticker--coral">Free &amp; confidential</span>' if k=='help' else '<span class="sticker">Free for students</span>' if k=='student' else ''}</div>
      <div class="who__txt"><h3>{esc(h)}</h3><p class="muted">{esc(p)}</p><div class="rows">{_rows(rows)}</div></div></div>''' for i, (k, pre, lbl, im, h, p, rows) in enumerate(who))

    svg, comps = ring_svg()
    comp_tabs = ''.join(
        f'<button role="tab" id="tsx-t{i}" aria-controls="tsx-p{i}" aria-selected="{str(i==0).lower()}" tabindex="{0 if i==0 else -1}" data-seg="{i}">'
        f'<i style="--c:{fill};--k:{ink}" aria-hidden="true">{i+1}</i><span>{esc(t.split(" (")[0])}</span></button>'
        for i, (t, h, fill, ink) in enumerate(comps))
    comp_panes = ''.join(
        f'<div class="tsx__pane{" on" if i==0 else ""}" role="tabpanel" id="tsx-p{i}" aria-labelledby="tsx-t{i}">'
        f'<b class="tsx__n" aria-hidden="true">{i+1}</b><h3>{esc(t)}</h3><p>{esc(COMP_TEXT[i])}</p><a class="arrow-link" href="{h}">Learn more</a></div>'
        for i, (t, h, fill, ink) in enumerate(comps))

    pods = [('3h2vVAyCO9q0bKyPhcASa3', 'Psych Talk', 'Sexual Violence Prevention for Teens', 'sp-3h2vvayco9q0bkyphcasa3-sq'), ('0v2G7MraWG1V2iyXgGKOUF', 'The Longest Shortest Time', 'Preventing Teens from Joining the Manosphere', None),
            ('5xOYkKKsC9qZgeGGGO9WQW', 'When Dating Hurts', 'Shael Norris: Stopping Sexual Violence', None), ('042UsrG0aMabkTo66WQQWc', 'The She Matters Podcast', 'Centering Youth Voices', None),
            ('4jjztQt08zjUR9guFgJ56x', 'The Longest Shortest Time', 'How to Not (Accidentally) Raise a Rapist', None), ('0JfMJbj7ZvISm8m7gp39YS', 'The Measure of Everyday Life', 'Reducing Tolerance for Sexual Assault', None)]
    pod_html = ''.join(f'<a class="pod" href="https://open.spotify.com/episode/{i}" target="_blank" rel="noopener" aria-label="Listen on Spotify: {esc(t)}, {esc(s)}"><span class="pod__art">{img(th or "sp-"+i.lower(), "")}<span class="pod__go" aria-hidden="true">{ICON_PLAY}</span></span><span><small>{esc(s)}</small><b>{esc(t)}</b></span></a>' for i, s, t, th in pods)

    partner_logos = ['rini-color-01cbb034', 'alliance-logo-color-vertical', '6716423ef4c1138196fb7101-phillips-exeter-academy-lion', 'walogolg-3', 'header-logo-stacked-3', 'chatgpt-image-dec-10-2025-08-34-32-am', '9e389524-a5f5-4c66-aee6-395723e59586', '63750970-0a6d-4483-b1d7-351445fc2a67', 'ridoh-logo', 'nova-logo', 'logo-mahperd', 'vrlc-logo-final-rgb-for-posters-white-on-blue', 'sml-logo-tag-long']
    logos = ''.join(f'<li>{img(n, "")}</li>' for n in partner_logos)

    vc_pdf = 'https://www.safebae.org/wp-content/uploads/2026/03/Check-Their-Vibe-A-Guide-to-Vibe-Check.pdf'

    body = f'''
<section class="hero">
  <span class="wm-daisy" aria-hidden="true"></span>
  <div class="wrap hero__in">
    <div class="hero__head rise">
      <p class="eyebrow">Survivor-founded &middot; Youth-led &middot; Since 2015</p>
      <h1 class="hero__title" aria-label="Safe Before Anyone Else"><span>Safe</span><span><b>B</b><i>efore</i></span><span><b>A</b><i>nyone</i></span><span><b>E</b><i>lse.</i></span></h1>
      <p class="hero__key"><span class="daisy"></span><span>That’s what the <b>BAE</b> in SafeBAE stands for.</span></p>
    </div>
    <div class="hero__wall" aria-hidden="true">
      <div class="hero__cols">{cols}</div>
      <span class="sticker">Youth-led</span><span class="sticker sticker--coral sticker--r">Survivor-founded</span><span class="sticker sticker--aqua">Free for students</span>
    </div>
    <div class="hero__body rise">
      <p class="lede">SafeBAE is the only survivor-founded, youth-led organization working to end sexual violence among middle and high school students nationwide. Our programs are free for students and built to change school culture from the inside.</p>
      <div class="btns hero__btns">{btn('Become a Peer Educator', 'peer-educator.html', 'mint', arrow=True)}{btn('Bring SafeBAE to your school', 'request-a-program.html', 'ghost')}{btn('Donate', 'donate.html', 'ghost')}</div>
      <ul class="hero__proof"><li><b>3,000+</b><span>Certified Peer Educators</span></li><li><b>70+</b><span>clubs every year</span></li><li><b>Published</b><span>in the Journal of Child Sexual Abuse</span></li></ul>
    </div>
  </div>
</section>

<section class="band band--paper">
  <div class="wrap">
    <div class="hd"><h2>What brings you to SafeBAE?</h2></div>
    <div data-tabs="who"><div class="who__tabs" role="tablist" aria-label="Who are you?">{tabs}</div>{panels}</div>
  </div>
</section>

<section class="nw" aria-labelledby="nw-h">
  <h2 class="nw__tag sticker" id="nw-h">New from SafeBAE</h2>
  <article class="nw__half nw-ai" aria-label="SafeBAE AI Literacy Training">
    <ul class="nw__kick nw-ai__facts"><li>Free</li><li>Self-paced</li><li>Ages 13+</li></ul>
    <div class="nw__vis nw-ai__vis">
      <figure class="nw-ai__fig">{img('ai-illo-hello', 'A drawing of a computer screen with a smiling face made of code and a name tag that reads “Hello, my name is AI.”')}<figcaption>From the training</figcaption></figure>
      <p class="nw-ai__launch reveal">Launches during U.S. Media Literacy Week, <span class="nw-loop">Oct 26–30, 2026{NW_LOOP}</span></p>
    </div>
    <h3>SafeBAE <span class="br">AI Literacy</span> Training</h3>
    <p class="nw__text">Six modules for high school and college students on AI, how it works, where it can go wrong, and what it means for navigating relationships, consent, privacy, and a world increasingly shaped by algorithms.</p>
    <ol class="nw__steps nw-map" aria-label="The six modules"><li>how AI works</li><li>feeds and thinking</li><li>relation&shy;ships</li><li>using AI well</li><li>fake images</li><li>sextortion</li></ol>
    <div class="btns">{btn('See the training', 'ai-literacy.html', 'slate', arrow=True)}{btn('For educators', 'https://ai-literacy.safebae.org/educators.html', 'ghost')}</div>
  </article>
  <article class="nw__half nw-ch" aria-label="Choking Hazard">
    <p class="nw__kick eyebrow">A SafeBAE campaign</p>
    <a class="nw__vis ch-label reveal" href="choking-hazard.html" aria-label="Choking Hazard warning label: Choking is a hazard. May cause serious injury or death. chokinghazard.org"><span class="ch-label__in" aria-hidden="true"><span class="ch-label__w">{NW_WARN}Warning</span><span class="ch-label__a">Choking is a hazard</span><span class="ch-label__b">May cause serious injury or death</span><span class="ch-label__c">chokinghazard.org</span></span></a>
    <h3>There’s no safe way to choke someone.</h3>
    <p class="nw__text">Choking Hazard is SafeBAE’s campaign on sexual strangulation, which young people call “choking.” It gives young people, parents and educators the evidence, myth vs. fact, signs that need medical care, and free warning posters.</p>
    <ul class="nw__steps nw-gives" aria-label="What the campaign gives you"><li><a href="choking-hazard.html#how-common">The evidence</a></li><li><a href="choking-hazard.html#myths">Myth vs. fact</a></li><li><a href="choking-hazard.html#er">Signs that need medical care</a></li><li><a href="choking-hazard.html#posters">Free warning posters</a></li></ul>
    <div class="btns">{btn('About the campaign', 'choking-hazard.html', 'mint', arrow=True)}{btn('chokinghazard.org', 'https://chokinghazard.org', 'ghost')}</div>
  </article>
</section>

<section class="band band--teal vb" id="vibe-check">
  <div class="wrap vb__grid">
    <div class="vb__copy">
    <div class="vb__head">
      <p class="vb__mark"><span class="daisy"></span>Vibe Check by SafeBAE</p>
      <h2 class="qs" aria-label="Not sure if you crossed a line?"><span aria-hidden="true">Did I harm someone?</span><span aria-hidden="true">Was that consent?</span><span aria-hidden="true">Did I cross a boundary?</span><span aria-hidden="true">Am I a bad person?</span><span class="on" aria-hidden="true">Not sure if you crossed a line?</span></h2>
    </div>
    <div class="vb__body">
      <p class="lede">CheckYourVibe.org is a free, anonymous reflection tool for young people who are questioning whether they, or a friend, may have crossed a boundary or caused harm.</p>
      <p class="vb__more">Young people are increasingly turning to anonymous forums and AI chatbots to ask difficult questions about relationships and consent. AI is built to tell you what you want to hear. Vibe Check guides users through confusing situations and connects them with real, evidence-based resources on consent, communication and accountability. No names, no accounts, and nothing is&nbsp;stored.</p>
      <div class="btns vb__btns">{btn('Open Vibe Check', 'https://checkyourvibe.org/', 'mint')}{btn('How it works', 'vibe-check.html', 'white', arrow=True)}<a class="vb__pdf" href="{vc_pdf}" target="_blank" rel="noopener">Adult guide (PDF)<span aria-hidden="true">&#8599;</span></a></div>
      <div class="vb__press"><span>As covered by</span>{img('the-guardian-logo-vector', 'The Guardian')}{img('vox-logo-svg-1', 'Vox')}{img('trendwatching-logo', 'TrendWatching')}</div>
    </div>
    </div>
    <div class="vb__stage">
      <span class="vb__disc" aria-hidden="true"></span>
      <div class="phone-wrap">
        <div class="phone">{img('vc-screen', 'The Vibe Check home screen on a phone')}</div>
        <span class="sticker" style="left:-16%;top:17%">Anonymous</span>
        <span class="sticker sticker--white sticker--r" style="right:-20%;bottom:21%">Nothing is stored</span>
      </div>
    </div>
  </div>
</section>

<section class="band band--aqua">
  <div class="wrap">
    <div class="hd">
      {eyebrow('For Daisy: Before Anyone Else', True)}
      <h2>Certified Peer Educator Training</h2>
      <p class="lede">A free, self-paced training that prepares high school students to lead conversations about consent, healthy relationships and their lived experiences, and to drive prevention in their own schools.</p>
    </div>
    <div class="cp">
      {cpet_player()}
      <div class="cp__side">
        <ul class="cp__facts"><li><b>16</b><span>interactive modules</span></li><li><b>$0</b><span>for students, anywhere</span></li><li><b>3,000+</b><span>certified so far</span></li></ul>
        <div class="cp__btns">{btn('Register here', 'peer-educator.html#register', 'slate', arrow=True)}{btn('Ver en Español', 'espanol.html', 'ghost')}{btn('Resume training', 'https://learning.safebae.org/students', 'ghost')}</div>
      </div>
    </div>
    <p class="cp__note"><span class="daisy" aria-hidden="true"></span><span>Offered in memory of our co-founder, Daisy Coleman, whose vision and leadership continue to inspire SafeBAE’s mission. #ForDaisy</span></p>
  </div>
</section>

<section class="band band--deep">
  <div class="wrap">
    <div class="hd hd--act"><p class="eyebrow">The Library</p><h2>Films made by young people. Lessons ready to teach.</h2>
      <div class="hd__act lib__nav"><button type="button" data-strip="-1" aria-label="Previous films">&#8249;</button><button type="button" data-strip="1" aria-label="More films">&#8250;</button></div>
      <p class="lede muted">Every film, podcast and teaching guide SafeBAE has made, now in one searchable library.</p></div>
    <div class="lib__tools">
      <form class="libsearch" action="library.html" data-libsearch><label class="sr-only" for="home-q">Search the library</label><input id="home-q" name="q" type="search" placeholder="Try “bystander” or “nudes”"><button class="btn" type="submit">Search</button></form>
      <div class="libcounts"><a href="library.html#films">Films &amp; videos</a><a href="library.html#podcasts">17 podcasts</a><a href="library.html#guides">8 teaching guides</a><a href="film-race-rape-culture-resistance.html">Race, Rape Culture &amp; Resistance</a></div>
    </div>
  </div>
  {film_strip()}
</section>

<section class="band band--paper" id="rees-and-360">
  <div class="wrap">
    <div class="hd"><h2>SafeBAE 360° Schools</h2>
      <p class="lede">SafeBAE’s whole-school approach: a comprehensive, survivor-centered prevention model rooted in <span class="nb">trauma-informed</span> care.</p></div>
    <div class="tsx" id="tsx">
      <div class="tsx__dial">{svg}</div>
      <div class="tsx__list" role="tablist" aria-orientation="vertical" aria-label="The six components">{comp_tabs}</div>
      <div class="tsx__read">{comp_panes}</div>
      <div class="tsx__foot"><p>Schools can start with one component or build the whole model over time.</p><div class="btns">{btn('Request a program', 'request-a-program.html', 'slate', arrow=True)}{btn('How 360° Schools works', '360-schools.html', 'ghost')}</div></div>
    </div>
  </div>
</section>

<section class="band band--slate" id="rees">
  <div class="wrap rs">
    <div class="rs__copy">
      <p class="eyebrow">SafeBAE x REES</p>
      <h2>Document your experience, privately and securely.</h2>
      <p class="lede">A free tool that gives every student a private, encrypted space to document incidents of harm or violence at their own pace. Nothing is shared without your consent.</p>
      <div class="btns">{btn('Student access', 'https://safebae.reessecureus.com/en/Login', 'mint')}{btn('Become a partner school', 'request-a-program.html', 'ghost')}</div>
    </div>
    <div class="rs__card">
      <div class="rs__lock">{LOGO_SVG}<i aria-hidden="true">&times;</i>{img('logo-horiz-rgb', 'REES')}<em>Free for every student</em></div>
      <ul class="rs__feats"><li><b>Private documentation</b><p>Create a secure, encrypted record of what happened, on your own time, entirely for yourself.</p></li><li><b>At your own pace</b><p>Come back whenever you’re ready. Your documentation is saved, with no pressure and no deadline.</p></li><li><b>At partner schools</b><p>Students can choose to report anonymously to their school and access <span class="nb">school-specific</span> resources.</p></li></ul>
    </div>
  </div>
</section>

<section class="band band--mint band--tight">
  <div class="wrap stats">
    <div class="stat"><b data-count="3000" data-suffix="+">3,000+</b><span>Certified Peer Educators trained</span></div>
    <div class="stat"><b data-count="70" data-suffix="+">70+</b><span>active SafeBAE clubs each year</span></div>
    <div class="stat"><b data-count="86000" data-suffix="+">86,000+</b><span>students reached through our digital resources</span></div>
    <div class="stat"><b>2015</b><span>founded by teen survivors and their families</span></div>
  </div>
</section>

<section class="band band--paper">
  <div class="wrap pq">
    <figure class="pq__quote">
      <blockquote class="quote">…she has friends that are a couple, and they were in an unhealthy relationship and your presentation changed the way they now treat one another. She also said that she was able to look at herself and how she treated her partner and make changes as well.</blockquote>
      <figcaption class="cite">Dawn M. Keys, Newport Prevention Coalition Coordinator</figcaption>
    </figure>
    {yt('ur2b6V1Pipk', 'A school leader’s perspective', thumb='yt-ur2b6v1pipk-tall', label='2 min', cls='pq__vid')}
  </div>
  <div class="wrap"><div class="pq__logos"><p class="eyebrow">Recent partner schools &amp; collaborators</p><ul class="pq__strip">{logos}</ul></div></div>
</section>

<section class="band band--aqua">
  <div class="wrap">
    <div class="hd hd--act"><h2>SafeBAE in conversation</h2><div class="hd__act">{btn('All 17 episodes', 'library.html#podcasts', 'slate', arrow=True)}</div></div>
    <div class="pods">{pod_html}</div>
  </div>
</section>

<section class="band band--deep fdz">
  <div class="wrap fd">
    <div class="fd__copy">
    <div class="fd__head">
      <p class="eyebrow">#ForDaisy</p>
      <h2>Remembering our <span class="nb">co-founder,</span> <span class="mk">Daisy Coleman.</span></h2>
    </div>
    <div class="fd__body">
      <p class="lede">As a teenage survivor, Daisy shared her story in the documentary <i>Audrie &amp; Daisy</i>. Her vision became the foundation of SafeBAE and helped ignite a youth-led movement. Every year, hundreds of people still find their way to this work through her story.</p>
      <p class="fd__more">She was also a tattoo artist whose work people still carry with them.</p>
      <blockquote class="fd__quote">All the organizing that happened after Daisy spoke out may not necessarily be a direct result but is certainly a ripple effect. <cite>The Cut, “What Daisy Coleman Changed”</cite></blockquote>
      <div class="btns fd__acts">{btn('Visit the tribute wall', 'fordaisy.html', 'mint', arrow=True)}{btn('Tattoos & Healing', 'fordaisy-tattoos.html', 'ghost', arrow=True)}<a class="arrow-link" href="fordaisy.html#add">Add your message to the wall</a></div>
    </div>
    </div>
    <div class="fd__art">
      <span class="daisy-art" aria-hidden="true"></span>
      <div class="fd__face">{img('crazy-daisy', 'Daisy Coleman')}</div>
      <a class="fd__work" href="fordaisy-tattoos.html" aria-label="Tattoos and Healing: Daisy’s art">{img('fordaisy28', 'Daisy Coleman tattooing a client')}<span class="sticker sticker--white">Tattoo artist</span></a>
    </div>
  </div>
</section>
{give_band()}
'''
    page('index.html', 'SafeBAE', 'SafeBAE provides youth-led sexual violence prevention programs, consent education curriculum, and peer educator training for middle and high schools nationwide.',
         body, active='', body_class='home', fonts=film_font_link() + '&family=Balsamiq+Sans:wght@400;700', head_extra=f'<style>{HOME_CSS}</style>', scripts='<script>' + HOME_JS + '</script>')


def cpet_player(extra_cls=''):
    caps = ['The only survivor-founded, youth-led org preventing sexual violence in schools', 'Why this training matters', 'Module 1 · Rape Culture & Shifting to a Culture of Respect', 'Consent starts way before sex. It starts when you’re a kid', 'The 6 Pillars of Consent', 'The foundation of a healthy relationship', 'BAEcode: real scripts for speaking up', 'Online safety & digital harassment', 'Supporting a partner who is a survivor', 'Wisdom from co-founder Daisy Coleman', 'Finish all 16 modules and become a Certified Peer Educator']
    slides = ''.join(f'<div class="player__slide{" on" if i==0 else ""}" data-cap="{esc(c)}">{img("preview"+str(i+1), c, loading="eager" if i==0 else "lazy")}</div>' for i, c in enumerate(caps))
    return f'''<div class="player {extra_cls}" data-player data-zoom data-interval="4500" aria-roledescription="carousel" aria-label="Sample slides from the Certified Peer Educator Training"><div class="player__bar"><i></i></div>{slides}<div class="player__ctl"><button data-prev aria-label="Previous slide">&#8249;</button><span class="player__cap"></span><button data-next aria-label="Next slide">&#8250;</button></div></div>'''


HOME_JS = r'''
(function(){
  var d = document, reduce = matchMedia('(prefers-reduced-motion: reduce)').matches, hasIO = 'IntersectionObserver' in window;

  /* hero: the photo wall drifts a little as the page scrolls */
  var hero = d.querySelector('.hero'), wall = d.querySelector('.hero__wall');
  if(wall) requestAnimationFrame(function(){ requestAnimationFrame(function(){ wall.classList.add('in'); }); });
  if(hero && wall && !reduce){
    var queued = false;
    var upd = function(){ queued = false; wall.style.setProperty('--s', Math.min(window.scrollY, hero.offsetHeight + 300).toFixed(0)); };
    window.addEventListener('scroll', function(){ if(!queued){ queued = true; requestAnimationFrame(upd); } }, {passive: true});
  }

  /* Vibe Check: the questions run through once and rest on the tool's own headline */
  var qs = d.querySelector('.qs');
  if(qs && !reduce && hasIO){
    var sp = qs.querySelectorAll('span'), last = sp.length - 1;
    var show = function(n){ sp.forEach(function(s, k){ s.classList.toggle('on', k === n); s.classList.toggle('out', k < n); }); };
    show(0);
    var qio = new IntersectionObserver(function(es){ if(!es[0].isIntersecting) return; qio.disconnect(); var n = 0; var t = setInterval(function(){ n++; show(n); if(n >= last) clearInterval(t); }, 1500); }, {threshold: .7});
    qio.observe(qs);
  }

  /* 360: ring, list and readout stay in step */
  var tsx = d.getElementById('tsx');
  if(tsx){
    var ring = tsx.querySelector('.ring'), tabs = [].slice.call(tsx.querySelectorAll('.tsx__list button')), panes = tsx.querySelectorAll('.tsx__pane'), segs = tsx.querySelectorAll('.seg');
    var pick = function(n, focus){
      tabs.forEach(function(b, i){ b.setAttribute('aria-selected', String(i === n)); b.tabIndex = i === n ? 0 : -1; });
      panes.forEach(function(p, i){ p.classList.toggle('on', i === n); });
      segs.forEach(function(s){ s.classList.toggle('on', +s.dataset.seg === n); });
      if(ring) ring.classList.add('has-active');
      if(focus) tabs[n].focus();
    };
    tabs.forEach(function(b, i){
      b.addEventListener('click', function(){ pick(i); });
      b.addEventListener('keydown', function(e){ var k = e.key, n = -1; if(k === 'ArrowDown' || k === 'ArrowRight') n = (i + 1) % tabs.length; else if(k === 'ArrowUp' || k === 'ArrowLeft') n = (i + tabs.length - 1) % tabs.length; else if(k === 'Home') n = 0; else if(k === 'End') n = tabs.length - 1; if(n > -1){ e.preventDefault(); pick(n, true); } });
    });
    segs.forEach(function(s){ var n = +s.dataset.seg;
      s.addEventListener('click', function(){ pick(n); });
      s.addEventListener('mouseenter', function(){ pick(n); });
      s.addEventListener('keydown', function(e){ if(e.key === 'Enter' || e.key === ' '){ e.preventDefault(); pick(n); } });
    });
    pick(0);
  }

  /* library: search hand-off and the strip arrows */
  var f = d.querySelector('[data-libsearch]');
  if(f) f.addEventListener('submit', function(e){ e.preventDefault(); var q = f.querySelector('input').value.trim(); try{ sessionStorage.setItem('libq', q); }catch(err){} var dest = 'library.html' + (q && /^[a-z0-9]+$/i.test(q) ? '#q-' + q : ''); if(window.SB && window.SB.go) window.SB.go(dest); else location.href = dest; });
  var strip = d.querySelector('.home .fstrip'), nav = [].slice.call(d.querySelectorAll('[data-strip]'));
  if(strip && nav.length){
    var sync = function(){ var max = strip.scrollWidth - strip.clientWidth - 4; nav.forEach(function(b){ b.disabled = +b.dataset.strip < 0 ? strip.scrollLeft < 4 : strip.scrollLeft > max; }); };
    nav.forEach(function(b){ b.addEventListener('click', function(){ var c = strip.querySelector('.fcard'), step = c ? (c.offsetWidth + parseFloat(getComputedStyle(strip).columnGap || 16)) * 2 : 500; strip.scrollBy({left: step * +b.dataset.strip, behavior: reduce ? 'auto' : 'smooth'}); }); });
    strip.addEventListener('scroll', sync, {passive: true}); window.addEventListener('resize', sync); sync();
  }

  /* stats: count up once when the band comes into view */
  var nums = d.querySelectorAll('[data-count]');
  if(nums.length && !reduce && hasIO){
    var nio = new IntersectionObserver(function(es){ es.forEach(function(en){ if(!en.isIntersecting) return; nio.unobserve(en.target);
      var el = en.target, to = +el.dataset.count, suf = el.dataset.suffix || '', t0 = 0;
      var step = function(t){ if(!t0) t0 = t; var k = Math.min(1, (t - t0) / 1100), e = 1 - Math.pow(1 - k, 3); el.textContent = Math.round(to * e).toLocaleString('en-US') + suf; if(k < 1) requestAnimationFrame(step); };
      requestAnimationFrame(step); }); }, {threshold: .6});
    nums.forEach(function(n){ nio.observe(n); });
  }
})();
'''
