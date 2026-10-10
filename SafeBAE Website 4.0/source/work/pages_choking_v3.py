"""choking-hazard.html: the safebae.org page for Choking Hazard, SafeBAE's campaign on sexual strangulation.
Facts: research_new_pages.md section A. Full citations checked against https://chokinghazard.org (9 Oct 2026).
Visual world: the campaign's warning label, moving hazard tape and clinical register, built in HTML/CSS.
Safety yellow (#FFD600) is the campaign's own accent and is used only for the label, stickers and tape."""
from lib import *
import films_common as _fc
from films_common import vibe_band
VIBE_CSS = getattr(_fc, 'VIBE_CSS', '')

CH = 'https://chokinghazard.org/'
CH_LEARN = CH + 'learn-more/'
CH_RATINGS = CH + 'media-ratings/'
CH_RES = CH + 'resources/'
CH_DL = CH + 'resources/#downloads'
CH_FILM = CH + 'film/'
MAIL = 'info@safebae.org'

# geometric warning triangle (rounded), ink + inner mark
TRI = ('<svg class="ch-tri" viewBox="0 0 48 42" aria-hidden="true" focusable="false">'
       '<path class="o" d="M21.4 3.5a3 3 0 0 1 5.2 0l19 33a3 3 0 0 1-2.6 4.5H5a3 3 0 0 1-2.6-4.5z"/>'
       '<rect class="i" x="21.6" y="13" width="4.8" height="15" rx="2.4"/><circle class="i" cx="24" cy="34" r="2.8"/></svg>')


def label(variant='', extra=''):
    """The campaign's warning label, drawn in HTML. Scales with its container (container query units)."""
    v = f' ch-label--{variant}' if variant else ''
    return (f'<div class="ch-lb{extra}"><div class="ch-label{v}">'
            f'<span class="ch-label__w">{TRI}<b>Warning</b></span>'
            f'<span class="ch-label__m">Choking is a hazard</span>'
            f'<span class="ch-label__s">May cause serious injury or death</span>'
            f'<span class="ch-label__u">chokinghazard.org</span></div></div>')


def tape(cls=''):
    unit = ''.join(f'<span>{TRI}Choking is a hazard</span><span>{TRI}chokinghazard.org</span>' for _ in range(4))
    return f'<div class="ch-tape {cls}"><div class="ch-tape__track">{unit}{unit}</div></div>'


def cite(t):
    return f'<p class="ch-cite">{t}</p>'


CSS = r'''
body.ch{--hz:#FFD600; --hz-ink:#0d0d0d; --hz-fold:#e0bc00}
.ch-tri{width:1.15em; height:1.01em; flex:none; display:inline-block; vertical-align:-.12em}
.ch-tri .o{fill:currentColor} .ch-tri .i{fill:var(--tri-in, var(--hz))}
.ch-cite{font-family:var(--mono); font-size:.82rem; letter-spacing:.01em; line-height:1.45; margin:14px 0 0; color:var(--ink-soft)}
:is(.band--slate,.band--deep,.ch-hero) .ch-cite{color:rgba(209,254,255,.72)}
.ch-k{font-family:var(--mono); font-size:.74rem; letter-spacing:.1em; text-transform:uppercase; font-weight:600; margin:0 0 8px; color:var(--logo-teal)}
:is(.band--slate,.band--deep) .ch-k{color:var(--mint)}
.ch .section-head .lede{max-width:none}

/* ---------- warning label ---------- */
.ch-lb{container-type:inline-size; width:100%}
.ch-label{aspect-ratio:1200/648; display:flex; flex-direction:column; align-items:center; justify-content:center; gap:1.2cqi; padding:3cqi 5cqi; background:var(--hz); color:var(--hz-ink); border:1.15cqi solid var(--hz-ink); border-radius:3.2cqi; font-family:var(--display); text-transform:uppercase; text-align:center; line-height:1; box-shadow:0 0 0 1.4cqi #fff, 0 30px 50px -18px rgba(0,0,0,.55); position:relative}
.ch-label__w{display:flex; align-items:center; gap:3.2cqi; font-weight:900; font-stretch:112%; font-size:13.2cqi; letter-spacing:.01em; margin-bottom:2.4cqi}
.ch-label__w .ch-tri{width:15.5cqi; height:13.6cqi}
.ch-label__m{font-weight:900; font-stretch:106%; font-size:7.3cqi; letter-spacing:.005em; white-space:nowrap}
.ch-label__s{font-weight:900; font-stretch:100%; font-size:3.95cqi; letter-spacing:.02em; white-space:nowrap}
.ch-label__u{font-weight:800; font-stretch:100%; text-transform:none; font-size:3.5cqi; margin-top:3.4cqi}
.ch-label--aqua{background:var(--aqua); color:var(--slate); border-color:var(--slate); --tri-in:var(--aqua)}
.ch-label--aqua .ch-label__w .ch-tri{color:var(--coral)}
.ch-label--aqua .ch-tri .i{fill:#fff}

/* ---------- hero ---------- */
.ch-hero{--wm-o:.13; position:relative; overflow:hidden; color:#fff; background-color:var(--slate); background-image:var(--grain), linear-gradient(rgba(209,254,255,.05) 1px, transparent 1px), linear-gradient(90deg, rgba(209,254,255,.05) 1px, transparent 1px); background-size:auto, 34px 34px, 34px 34px}
.ch-hero > .wrap{position:relative; z-index:1; display:grid; grid-template-columns:minmax(0,7fr) minmax(0,5fr); gap:clamp(28px,4vw,56px); align-items:center; padding-block:clamp(40px,5vw,72px) clamp(64px,7vw,104px)}
.ch-hero .wrap > *{min-width:0}
.ch-hero .crumbs{color:rgba(255,255,255,.78)}
.ch-hero .eyebrow{color:var(--mint)}
.ch-hero h1{font-size:clamp(2.45rem,5.3vw,5.2rem); font-stretch:120%; font-weight:900; text-transform:uppercase; line-height:.92; letter-spacing:-.02em; margin:0 0 .32em}
.ch-open{font-family:var(--display); font-weight:800; font-stretch:108%; font-size:clamp(1.2rem,1.9vw,1.62rem); line-height:1.2; color:var(--aqua); margin:0 0 .7em}
.ch-hero .lede{color:rgba(255,255,255,.88)}
.ch-hero .mk{background:none; color:var(--mint)}
.ch-cn{display:flex; gap:10px; align-items:baseline; flex-wrap:wrap; margin:22px 0 0; font-size:.9rem; color:rgba(255,255,255,.84)}
.ch-cn b{font-family:var(--mono); font-size:.7rem; letter-spacing:.1em; text-transform:uppercase; font-weight:600; color:var(--slate); background:var(--aqua); padding:3px 8px; border-radius:4px; flex:none}
.ch-hero__art{position:relative; padding:18% 0 4% 0}
.ch-lb--aqua{position:absolute; width:56%; right:-1%; top:0; transform:rotate(7deg); --r:7deg; animation:ch-slap .7s .35s var(--ease) both}
.ch-lb--main{position:relative; width:100%; transform:rotate(-4deg); --r:-4deg; animation:ch-slap .7s .1s var(--ease) both}
.ch-lb--main .ch-label::after{content:""; position:absolute; right:-1.15cqi; bottom:-1.15cqi; width:8cqi; height:8cqi; border-bottom-right-radius:3.2cqi; background:linear-gradient(135deg, var(--hz-fold) 0 49%, var(--slate) 51%); box-shadow:-3px -3px 8px rgba(0,0,0,.18)}
@keyframes ch-slap{0%{opacity:0; transform:rotate(calc(var(--r) - 6deg)) scale(1.22)} 65%{opacity:1; transform:rotate(var(--r)) scale(.97)} 100%{opacity:1; transform:rotate(var(--r)) scale(1)}}

/* ---------- hazard tape ---------- */
.ch-tapes{position:relative; z-index:3; height:clamp(84px,9vw,130px); margin-block:calc(clamp(84px,9vw,130px) / -2); overflow:hidden; pointer-events:none}
.ch-tape{position:absolute; left:-12%; width:124%; top:50%; height:clamp(36px,3.6vw,50px); margin-top:calc(clamp(36px,3.6vw,50px) / -2); background:var(--hz); color:var(--hz-ink); border-block:clamp(4px,.45vw,6px) solid var(--hz-ink); overflow:hidden; display:flex; align-items:center; box-shadow:0 10px 24px -10px rgba(0,0,0,.5)}
.ch-tape--a{transform:rotate(-2.2deg)}
.ch-tape--b{transform:rotate(1.6deg); filter:brightness(.96)}
.ch-tape__track{display:flex; width:max-content; animation:ch-roll 2.8s var(--ease) both}
.ch-tape--b .ch-tape__track{animation-name:ch-roll-b; animation-duration:3.2s}
.ch-tape__track span{display:inline-flex; align-items:center; gap:.5em; padding-inline:1.1em; font-family:var(--display); font-weight:900; font-stretch:110%; text-transform:uppercase; font-size:clamp(.82rem,1.25vw,1.1rem); letter-spacing:.02em; white-space:nowrap}
.ch-tape__track span:nth-child(even){text-transform:uppercase}
@keyframes ch-roll{from{transform:translateX(-2%)} to{transform:translateX(-9%)}}
@keyframes ch-roll-b{from{transform:translateX(-12%)} to{transform:translateX(-5%)}}

/* ---------- 1. how common ---------- */
.ch-common{display:grid; grid-template-columns:minmax(0,7fr) minmax(0,5fr); gap:var(--gap); align-items:stretch}
.ch-card{background:#fff; border:1px solid var(--line); border-radius:var(--r-xl); padding:var(--pad-card); margin:0; min-width:0}
.ch-chart{display:flex; flex-direction:column}
.ch-chart .ch-cols{flex:1 1 auto}
.ch-chart .ch-cite{margin-top:18px; padding-top:12px; border-top:1px solid var(--line)}
.ch-card figcaption b{display:block; font-family:var(--display); font-weight:800; font-stretch:106%; font-size:1.3rem; line-height:1.2; color:var(--slate)}
.ch-card figcaption span{display:block; font-size:.92rem; color:var(--ink-soft); margin-top:3px}
.ch-cols{position:relative; min-height:clamp(220px,22vw,290px); margin:44px 0 0 42px; border-bottom:2px solid var(--slate)}
.ch-cols__grid i{position:absolute; left:0; right:0; border-top:1px solid var(--line); font-style:normal}
.ch-cols__grid i span{position:absolute; left:-42px; width:34px; text-align:right; top:-.62em; font:500 .74rem/1 var(--mono); color:var(--ink-soft)}
.ch-cols__bars,.ch-cols__x{display:grid; grid-template-columns:repeat(3,minmax(0,1fr)); gap:clamp(14px,3vw,44px); padding-inline:clamp(6px,2vw,28px)}
.ch-cols__bars{position:absolute; inset:0; align-items:end}
.ch-col{position:relative; height:var(--h); background:var(--teal); border-radius:6px 6px 0 0; transition:height 1.1s var(--ease)}
.ch-col:first-child{background:var(--slate)}
.ch-pre .ch-col{height:0}
.ch-col b{position:absolute; bottom:100%; left:-10px; right:-10px; text-align:center; font-family:var(--display); font-weight:900; font-stretch:110%; font-size:clamp(1.3rem,2.4vw,2.1rem); line-height:1; padding-bottom:8px; color:var(--slate)}
.ch-cols__x{margin:12px 0 0 42px; text-align:center}
.ch-cols__x span{display:block; font-family:var(--display); font-weight:800; font-size:1.15rem; line-height:1.15; color:var(--slate)}
.ch-cols__x small{display:block; font-size:.9rem; line-height:1.3; color:var(--ink-soft); margin-top:3px}
.ch-cols__x small + small{margin-top:0}
.ch-first{display:flex; flex-direction:column; justify-content:space-between; gap:0; background:var(--slate); color:#fff; border-color:transparent; background-image:var(--grain)}
.ch-first .ch-cite{color:rgba(209,254,255,.72); margin-top:10px}
.ch-first__age{display:grid; grid-template-columns:auto minmax(0,1fr); gap:16px; align-items:center}
.ch-first__age b{font-family:var(--display); font-weight:900; font-stretch:125%; font-size:clamp(4rem,7vw,6rem); line-height:.8; color:var(--mint); letter-spacing:-.03em}
.ch-first__age p{margin:0; font-weight:600; font-size:1.1rem; line-height:1.35}
.ch-first hr{width:100%; border:0; border-top:1px solid var(--line-dark); margin:18px 0}
.ch-first .ch-k{color:var(--mint)}
.ch-hb{display:grid; grid-template-columns:minmax(0,112px) minmax(0,1fr) auto; gap:12px; align-items:center; margin:9px 0}
.ch-hb span{font-size:.98rem; font-weight:600}
.ch-hb em{font-style:normal; font-family:var(--display); font-size:1.1rem; font-weight:900; min-width:3.4em; text-align:right; color:var(--mint)}
.ch-hb__t{height:12px; background:rgba(209,254,255,.12); border-radius:3px; overflow:hidden}
.ch-hb__t i{display:block; height:100%; width:var(--w); background:var(--mint); border-radius:0 4px 4px 0; transition:width 1.1s var(--ease)}
.ch-pre .ch-hb__t i{width:0}
.ch-quarter{display:grid; grid-template-columns:auto minmax(0,1fr); gap:16px; align-items:center}
.ch-quarter__g{display:grid; grid-template-columns:repeat(2,22px); gap:5px}
.ch-quarter__g i{width:22px; height:22px; border-radius:5px; border:2px solid rgba(209,254,255,.45)}
.ch-quarter__g i:first-child{background:var(--mint); border-color:var(--mint)}
.ch-quarter p{margin:0; font-size:1rem; line-height:1.4}
.ch-quarter p b{font-family:var(--display); font-weight:900; font-stretch:115%; font-size:1.5rem; color:var(--mint)}

/* ---------- 2. body ---------- */
.ch-body{background-image:var(--grain), linear-gradient(rgba(209,254,255,.035) 1px, transparent 1px), linear-gradient(90deg, rgba(209,254,255,.035) 1px, transparent 1px); background-size:auto, 34px 34px, 34px 34px}
.ch-force{display:grid; grid-template-columns:minmax(0,7fr) minmax(0,5fr); gap:clamp(28px,4vw,56px); align-items:center}
.ch-force h2{font-size:clamp(2.2rem,4.6vw,4rem); font-stretch:118%; text-transform:uppercase; font-weight:900; line-height:.95}
.ch-force .lede{color:rgba(255,255,255,.88)}
.ch-ff{background:#fff; color:var(--hz-ink); border:3px solid var(--hz-ink); padding:14px 18px 12px; margin:0; box-shadow:0 30px 60px -30px rgba(0,0,0,.6); font-family:var(--body)}
.ch-ff__t{font-family:var(--display); font-weight:900; font-stretch:72%; font-size:clamp(2.4rem,4vw,3.3rem); line-height:.95; margin:0; letter-spacing:-.01em}
.ch-ff__sv{display:flex; justify-content:space-between; font-weight:700; font-size:.95rem; border-bottom:10px solid var(--hz-ink); padding:4px 0 6px; margin:4px 0 0}
.ch-ff__big{display:flex; justify-content:space-between; align-items:end; border-bottom:5px solid var(--hz-ink); padding:6px 0 6px}
.ch-ff__big span{font-weight:800; font-size:.9rem}
.ch-ff__big span b{display:block; font-family:var(--display); font-weight:900; font-stretch:80%; font-size:1.7rem; line-height:1}
.ch-ff__big > b{font-family:var(--display); font-weight:900; font-stretch:80%; font-size:2.4rem; line-height:1}
.ch-ff__dv{text-align:right; font-weight:800; font-size:.88rem; margin:4px 0 0; padding-bottom:4px; border-bottom:1px solid var(--hz-ink)}
.ch-ff__row{display:grid; grid-template-columns:minmax(0,1fr) auto 3.4em; gap:12px; align-items:baseline; padding:8px 0 4px; font-size:.95rem}
.ch-ff__row > b{font-weight:800; text-align:right}
.ch-ff__row > b:last-child{font-family:var(--display); font-weight:900}
.ch-ff__bar{height:16px; background:#f0f0f0; position:relative; border-bottom:1px solid var(--hz-ink); margin-bottom:2px}
.ch-ff__bar i{position:absolute; left:0; top:0; bottom:0; width:var(--w); background:var(--slate); transition:width 1.1s var(--ease)}
.ch-ff__bar--can i{background:var(--teal)}
.ch-pre .ch-ff__bar i{width:0}
.ch-ff__ax{position:relative; height:18px; border-bottom:5px solid var(--hz-ink); margin-top:2px}
.ch-ff__ax span{position:absolute; top:3px; transform:translateX(-50%); font:600 .7rem/1 var(--mono); white-space:nowrap}
.ch-ff__ax span:first-child{transform:none} .ch-ff__ax span:last-child{transform:translateX(-100%)}
.ch-ff__fn{font-size:.84rem; line-height:1.35; margin:8px 0 0}
.ch-mini{display:flex; gap:12px; align-items:center; margin-top:16px; background:var(--hz); color:var(--hz-ink); border:3px solid var(--hz-ink); border-radius:6px; padding:12px 16px; font-weight:700; font-size:.98rem; line-height:1.3; box-shadow:0 0 0 3px #fff}
.ch-mini .ch-tri{width:30px; height:26px}
.ch-mini b{font-family:var(--display); font-weight:900; text-transform:uppercase; letter-spacing:.02em}
/* the clock */
.ch-clock{margin-top:clamp(40px,5vw,64px); border:1px solid var(--line-dark); border-radius:var(--r-xl); background:rgba(8,26,32,.45); padding:clamp(20px,3vw,36px)}
.ch-clock__head{display:grid; grid-template-columns:minmax(0,1fr) auto; gap:20px 40px; align-items:end}
.ch-clock h3{font-size:clamp(1.7rem,3vw,2.5rem); font-stretch:118%; text-transform:uppercase; font-weight:900; margin:0 0 .3em}
.ch-clock__head p{margin:0; color:rgba(255,255,255,.9); font-size:1.08rem}
.ch-clock__ctl{display:flex; flex-direction:column; align-items:flex-end; gap:10px}
.ch-clock__n{font-family:var(--display); font-weight:900; font-stretch:125%; font-size:clamp(2.8rem,5vw,4.2rem); line-height:.9; color:var(--mint); font-variant-numeric:tabular-nums; letter-spacing:-.02em}
.ch-clock__n small{font-size:.42em; margin-left:.12em; color:rgba(209,254,255,.75); letter-spacing:0}
.ch-clock .btns{justify-content:flex-end}
.ch-track{position:relative; height:54px; margin:26px 0 0; border-radius:8px; background-color:rgba(209,254,255,.06); background-image:repeating-linear-gradient(90deg, rgba(209,254,255,.42) 0 2px, transparent 2px calc(1000% / 62)), repeating-linear-gradient(90deg, rgba(209,254,255,.16) 0 1px, transparent 1px calc(100% / 62)); background-size:100% 100%, 100% 40%; background-repeat:no-repeat; background-position:0 0, 0 100%; overflow:visible}
.ch-track__fill{position:absolute; left:0; top:0; bottom:0; width:0; background:linear-gradient(90deg, rgba(21,255,200,.16), rgba(21,255,200,.42)); border-right:3px solid var(--mint); border-radius:8px 0 0 8px}
.ch-track__fill[style*="width: 0"]{border-right-color:transparent}
.ch-track__band{position:absolute; top:-8px; bottom:-8px; left:calc(500% / 62); width:calc(500% / 62); background:rgba(21,255,200,.2); border-inline:2px solid var(--mint); border-radius:3px; transition:background .3s}
.ch-clock.past5 .ch-track__band{background:rgba(21,255,200,.5)}
.ch-track__mk{position:absolute; top:-14px; bottom:-14px; width:3px; margin-left:-1px; background:#fff; border-radius:2px}
.ch-track__mk--end{left:calc(100% - 3px); background:var(--coral)}
.ch-clock.done .ch-track__mk--end{box-shadow:0 0 0 4px rgba(254,113,113,.3)}
.ch-track__ax{position:relative; height:22px; margin-top:18px}
.ch-track__ax span{position:absolute; transform:translateX(-50%); font:500 .76rem/1 var(--mono); color:rgba(209,254,255,.75)}
.ch-track__ax span:first-child{transform:none}
.ch-legend{list-style:none; padding:0; margin:14px 0 0; display:flex; flex-wrap:wrap; gap:10px 26px; font-size:.98rem}
.ch-legend li{display:flex; gap:10px; align-items:center; margin:0}
.ch-legend i{flex:none; display:inline-block}
.ch-legend .k-band{width:22px; height:14px; background:rgba(21,255,200,.5); border-inline:2px solid var(--mint)}
.ch-legend .k-avg{width:3px; height:20px; background:#fff; border-radius:2px}
.ch-legend .k-end{width:3px; height:20px; background:var(--coral); border-radius:2px}
.ch-clock__status{min-height:1.3em; margin:22px 0 0; font-family:var(--display); font-weight:800; font-stretch:106%; font-size:clamp(1.1rem,1.6vw,1.35rem); line-height:1.25; color:var(--mint)}
.ch-clock [data-clock-go]{min-width:10.4em}

/* ---------- 3. myth vs fact ---------- */
.ch-mf{border-bottom:2px solid var(--slate)}
.ch-mf__head{display:grid; grid-template-columns:minmax(0,5fr) minmax(0,7fr); font-family:var(--mono); font-size:.74rem; letter-spacing:.1em; text-transform:uppercase; font-weight:600; color:var(--logo-teal); padding-bottom:10px}
.ch-mf__head span + span{padding-left:28px}
.ch-mf__row{display:grid; grid-template-columns:minmax(0,5fr) minmax(0,7fr); border-top:2px solid var(--slate)}
.ch-mf__myth{margin:0; padding:26px 26px 26px 0; font-family:var(--display); font-weight:800; font-stretch:108%; font-size:clamp(1.35rem,2.4vw,2.05rem); line-height:1.12; color:var(--slate)}
.ch-mf__myth span{background-image:linear-gradient(var(--coral),var(--coral)); background-size:0 5px; background-position:0 58%; background-repeat:no-repeat; -webkit-box-decoration-break:clone; box-decoration-break:clone; transition:background-size .55s .2s var(--ease), color .3s .2s}
.ch-mf__row.open .ch-mf__myth span{background-size:100% 5px; color:var(--ink-soft)}
.ch-mf__tag{display:block; height:0; font-style:normal}
.ch-mf__tag b{display:inline-block; font-family:var(--display); font-weight:900; font-stretch:120%; text-transform:uppercase; letter-spacing:.08em; font-size:.86rem; line-height:1; color:var(--slate); background:var(--coral); border-radius:5px; padding:6px 10px 5px; transform:translateY(16px) rotate(-5deg) scale(0); transform-origin:0 50%; transition:transform .45s .45s var(--ease)}
.ch-mf__row.open .ch-mf__tag b{transform:translateY(16px) rotate(-5deg) scale(1)}
.ch-mf__fact{position:relative; padding:20px 0 24px 28px; border-left:1px solid var(--line); min-height:132px}
.ch-mf__in{outline:none}
.ch-mf__in h3{font-size:clamp(1.5rem,2.6vw,2.2rem); font-stretch:112%; font-weight:900; text-transform:uppercase; line-height:1; margin:6px 0 .4em; color:var(--slate)}
.ch-mf__in p{margin:0 0 .6em; font-size:1.06rem; line-height:1.6}
.ch-mf__in .ch-cite{margin-top:10px}
.js .ch-mf__in{display:none}
.js .ch-mf__row.open .ch-mf__in{display:block; animation:ch-in .5s .12s var(--ease) both}
@keyframes ch-in{from{opacity:0; transform:translateY(8px)}}
.ch-peel{position:absolute; left:28px; right:0; top:16px; bottom:16px; display:none; align-items:center; justify-content:flex-start; gap:18px; padding:12px 22px; cursor:pointer; text-align:left; font:inherit; color:var(--hz-ink); background:var(--hz); border:3px solid var(--hz-ink); border-radius:8px; box-shadow:0 0 0 3px #fff, 0 14px 22px -14px rgba(0,0,0,.5); transform:rotate(-1deg); transform-origin:100% 0; transition:transform .65s var(--ease), opacity .5s .1s}
.js .ch-peel{display:flex}
.ch-mf__row:nth-child(odd) .ch-peel{transform:rotate(.8deg)}
.ch-peel:hover{transform:rotate(-2.2deg) translateY(-2px)}
.ch-peel:focus-visible{outline:3px solid var(--slate); outline-offset:5px}
.ch-peel::after{content:""; position:absolute; right:-3px; bottom:-3px; width:30px; height:30px; border-bottom-right-radius:8px; background:linear-gradient(135deg, var(--hz-fold) 0 49%, var(--aqua) 51%); transition:width .25s, height .25s}
.ch-peel:hover::after{width:44px; height:44px}
.ch-peel .ch-tri{width:46px; height:40px; --tri-in:var(--hz)}
.ch-peel b{display:block; font-family:var(--display); font-weight:900; font-stretch:112%; text-transform:uppercase; font-size:clamp(1.3rem,2.2vw,1.8rem); line-height:1}
.ch-peel small{display:block; font-family:var(--display); font-weight:800; text-transform:uppercase; letter-spacing:.03em; font-size:.9rem; margin-top:5px}
.ch-mf__row.open .ch-peel{transform:translate(18%,-55%) rotate(-28deg) scale(.9); opacity:0; pointer-events:none}
.ch-dots{display:grid; grid-template-columns:repeat(30,minmax(0,1fr)); gap:3px; max-width:560px; margin:14px 0 10px}
.ch-dots i{aspect-ratio:1; border-radius:50%; background:transparent; border:1.5px solid rgba(29,65,78,.4)}
.ch-dots i.a{background:var(--slate); border-color:var(--slate)}
.ch-dots i.b{background:var(--teal); border-color:var(--teal)}
.ch-dots__k{list-style:none; padding:0; margin:0; display:flex; flex-wrap:wrap; gap:6px 20px; font-size:.95rem}
.ch-dots__k li{display:flex; gap:8px; align-items:center; margin:0}
.ch-dots__k i{width:12px; height:12px; border-radius:50%; flex:none; border:1.5px solid rgba(29,65,78,.4)}
.ch-dots__k i.a{background:var(--slate); border-color:var(--slate)} .ch-dots__k i.b{background:var(--teal); border-color:var(--teal)}
.ch-dots__k b{font-family:var(--display); font-weight:900}
.ch-mf__more{display:flex; flex-wrap:wrap; gap:12px 20px; align-items:center; justify-content:space-between; margin-top:22px}
.ch-mf__more p{margin:0; font-size:1rem; font-weight:600; color:var(--slate)}

/* ---------- 4. consent ---------- */
.ch-cons{display:grid; grid-template-columns:minmax(0,7fr) minmax(0,5fr); gap:clamp(28px,4vw,56px); align-items:center}
.ch-cons h2{font-size:clamp(1.9rem,3.6vw,3.1rem)}
.ch-cons .lede{color:rgba(255,255,255,.86)}
.ch-cbars{margin:0; padding:clamp(20px,2.6vw,30px); border:1px solid var(--line-dark); border-radius:var(--r-xl); background:rgba(255,255,255,.04)}
.ch-cbars figcaption{font-family:var(--display); font-weight:800; font-stretch:106%; font-size:1.1rem; margin-bottom:18px}
.ch-cbar{margin:0 0 18px}
.ch-cbar > span{display:flex; justify-content:space-between; gap:12px; align-items:baseline; font-weight:600; font-size:.95rem; margin-bottom:6px}
.ch-cbar > span b{font-family:var(--display); font-weight:900; font-stretch:115%; font-size:clamp(1.6rem,2.6vw,2.2rem); line-height:1; color:var(--mint)}
.ch-cbar--b > span b{color:var(--aqua)}
.ch-cbar__t{height:18px; border-radius:3px; background:rgba(209,254,255,.08); overflow:hidden}
.ch-cbar__t i{display:block; height:100%; width:var(--w); background:var(--mint); border-radius:0 4px 4px 0; transition:width 1.1s var(--ease)}
.ch-cbar--b .ch-cbar__t i{background:var(--aqua)}
.ch-pre .ch-cbar__t i{width:0}
.ch-cbars__ax{display:flex; justify-content:space-between; font:500 .72rem/1 var(--mono); color:rgba(209,254,255,.65); border-top:1px solid var(--line-dark); padding-top:6px}
.ch-signal{display:grid; grid-template-columns:repeat(3,minmax(0,1fr)); gap:0; margin-top:clamp(28px,4vw,48px); border-block:1px solid var(--line-dark)}
.ch-signal > div{padding:22px 24px; border-left:1px solid var(--line-dark); min-width:0}
.ch-signal > div:first-child{border-left:0; padding-left:0}
.ch-signal b{display:block; font-family:var(--display); font-weight:900; font-stretch:118%; font-size:clamp(2.4rem,4vw,3.4rem); line-height:.95; color:var(--mint)}
.ch-signal p{margin:8px 0 0; font-weight:600; line-height:1.35}
.ch-signal .ch-dont{font-family:var(--display); font-weight:900; font-stretch:112%; text-transform:uppercase; font-size:clamp(1.2rem,2vw,1.6rem); line-height:1.05; margin:0; color:#fff; align-self:center}
.ch-signal .ch-dont em{font-style:normal; color:var(--mint)}
.ch-pillars-head{margin:clamp(36px,5vw,60px) 0 22px}
.ch-pillars-head h3{font-size:clamp(1.6rem,2.8vw,2.3rem); font-stretch:115%; font-weight:900; text-transform:uppercase; margin:0 0 .3em}
.ch-pillars-head p{margin:0; color:rgba(255,255,255,.86); font-size:var(--fs-lede); font-weight:500}
.ch-pillars{display:grid; grid-template-columns:repeat(4,minmax(0,1fr)); gap:var(--gap)}
.ch-pillar{position:relative; display:grid; grid-template-rows:subgrid; grid-row:span 4; row-gap:0; background:rgba(255,255,255,.05); border:1px solid var(--line-dark); border-radius:var(--r-xl); padding:22px 22px 24px; min-width:0}
.ch-pillar__L{display:block; font-family:var(--display); font-weight:900; font-stretch:125%; font-size:4.4rem; line-height:.85; color:transparent; -webkit-text-stroke:2px var(--mint); margin-bottom:12px}
.ch-pillar h4{font-family:var(--display); font-weight:900; font-stretch:115%; text-transform:uppercase; font-size:1.5rem; margin:0 0 .25em; color:#fff}
.ch-pillar p{margin:0; font-size:.97rem; color:rgba(255,255,255,.86); line-height:1.5}
.ch-pillar p.r{font-weight:700; color:var(--aqua); margin-bottom:.6em}
.ch-stamp{position:absolute; top:22px; right:18px; font-family:var(--display); font-weight:900; font-stretch:120%; text-transform:uppercase; letter-spacing:.08em; font-size:.82rem; color:var(--coral); border:2.5px solid var(--coral); border-radius:5px; padding:4px 8px 3px; transform:rotate(-8deg)}
.ch-movers{display:grid; grid-template-columns:minmax(0,1fr) auto; gap:12px 28px; align-items:center; margin-top:var(--gap); padding:18px 22px; border-radius:14px; background:rgba(21,255,200,.08); border:1px solid rgba(21,255,200,.28)}
.ch-movers p{margin:0; color:rgba(255,255,255,.9)}

/* ---------- 5. where it came from ---------- */
.ch-ex{display:grid; grid-template-columns:repeat(3,minmax(0,1fr)); gap:var(--gap)}
.ch-exh{position:relative; display:grid; grid-template-rows:subgrid; grid-row:span 4; row-gap:0; background:#fff; border:1px solid var(--line); border-radius:var(--r-xl); overflow:hidden; min-width:0; transition:transform .25s var(--ease), box-shadow .25s}
.ch-exh:hover{transform:translateY(-3px); box-shadow:var(--shadow-soft)}
.ch-exh__tag{display:flex; align-items:center; gap:10px; margin:0; background:var(--slate); color:var(--mint); font-family:var(--mono); font-size:.74rem; letter-spacing:.06em; text-transform:uppercase; font-weight:600; padding:10px 16px}
.ch-exh__tag::before{content:""; width:11px; height:11px; border-radius:50%; background:var(--paper); box-shadow:inset 0 0 0 2px rgba(0,0,0,.25); flex:none}
.ch-exh > :not(.ch-exh__tag){padding-inline:22px}
.ch-exh .ch-exh__fig{font-family:var(--display); font-weight:900; font-stretch:118%; font-size:clamp(2.2rem,3.6vw,3.1rem); line-height:.95; color:var(--teal); letter-spacing:-.015em; margin:0; padding-top:20px}
.ch-exh__fig small{font-size:.5em; letter-spacing:0; margin-left:.15em}
.ch-exh__t{margin:0; padding-top:10px; font-size:.98rem; line-height:1.5}
.ch-exh__t:last-child{grid-row:span 2; padding-bottom:22px}
.ch-exh .ch-cite{margin:0; padding-block:14px 20px; align-self:end}

/* ---------- 6. media ratings ---------- */
.ch-rate{display:grid; grid-template-columns:minmax(0,1fr) minmax(0,1fr); gap:var(--gap); align-items:stretch}
.ch-rc{position:relative; display:flex; flex-direction:column; padding:clamp(22px,3vw,34px); border:3px solid var(--hz-ink); outline:2px solid var(--hz-ink); outline-offset:-12px; color:var(--hz-ink); min-width:0}
.ch-rc--ch{background:var(--hz)}
.ch-rc--bae{background:var(--mint); border-color:var(--slate-deep); outline-color:var(--slate-deep); color:var(--slate-deep)}
.ch-rc__pre{font-family:var(--mono); font-size:.76rem; letter-spacing:.16em; text-transform:uppercase; font-weight:600; margin:6px 0 14px 6px}
.ch-rc__g{display:grid; grid-template-columns:auto minmax(0,1fr); gap:18px 22px; align-items:center; margin:0 6px}
.ch-rc__box{text-align:center}
.ch-rc__box b{display:block; border:6px solid currentColor; padding:4px 14px 2px; font-family:var(--display); font-weight:900; font-stretch:100%; font-size:clamp(3rem,5.4vw,4.6rem); line-height:1; letter-spacing:-.02em}
.ch-rc__box span{display:block; font-family:var(--mono); font-size:.7rem; letter-spacing:.16em; text-transform:uppercase; font-weight:600; margin-top:8px}
.ch-rc__d{border-left:3px solid currentColor; padding-left:18px; font-family:var(--mono); font-weight:600; text-transform:uppercase; letter-spacing:.05em; font-size:clamp(.82rem,1.1vw,.95rem); line-height:1.5}
.ch-rc__lbl{margin:24px 6px 0; font-family:var(--mono); font-size:.72rem; letter-spacing:.14em; text-transform:uppercase; font-weight:600}
.ch-rc__ex{flex:1 1 auto; list-style:none; padding:0; margin:8px 6px 0; display:grid; grid-auto-rows:1fr; gap:0 22px}
.ch-rc__ex--4{grid-template-columns:repeat(2,minmax(0,1fr))}
.ch-rc__ex li{margin:0; display:grid; grid-template-columns:minmax(0,1fr) auto; gap:10px; align-items:center; padding-block:11px; border-top:2px solid currentColor}
.ch-rc__ex b{display:block; font-family:var(--display); font-weight:900; font-stretch:106%; font-size:1.12rem; line-height:1.15}
.ch-rc__ex--4 b{text-transform:uppercase; letter-spacing:.02em; font-size:1.02rem}
.ch-rc__ex small{font-family:var(--mono); font-size:.72rem; letter-spacing:.06em; text-transform:uppercase}
.ch-rc__ex em{font-style:normal; font-family:var(--display); font-weight:800; font-size:.8rem; text-transform:uppercase; letter-spacing:.03em; padding:5px 9px; background:var(--slate-deep); color:var(--mint); border-radius:4px; white-space:nowrap}
.ch-rc__by{margin:0 6px; padding-top:14px; border-top:2px solid currentColor; font-family:var(--mono); font-size:.7rem; letter-spacing:.14em; text-transform:uppercase; text-align:right}
.ch-rate-foot{display:flex; flex-wrap:wrap; gap:14px 24px; align-items:center; justify-content:space-between; margin-top:26px}
.ch-rate-foot p{margin:0; color:rgba(255,255,255,.82)}

/* ---------- 7. film ---------- */
.ch-film{display:grid; grid-template-columns:repeat(2,minmax(0,1fr)); gap:clamp(28px,4vw,56px); align-items:center}
.ch-film .lede{max-width:none}
.ch-mail{display:flex; flex-wrap:wrap; gap:10px 14px; align-items:center; margin:18px 0 22px}
.ch-mail p{margin:0; font-weight:600}
.ch-screen{container-type:inline-size; min-width:0}
.ch-screen__mon{position:relative; aspect-ratio:16/10; background:var(--slate-deep); background-image:var(--grain); border:clamp(8px,1.6cqi,14px) solid #0b1f25; border-radius:clamp(12px,2.2cqi,20px); box-shadow:var(--shadow-soft); overflow:hidden}
.ch-screen__bar{position:absolute; left:0; right:0; top:0; height:6.2%; background:rgba(209,254,255,.08); display:flex; align-items:center; gap:1.4cqi; padding:0 2cqi; font:600 max(.66rem,1.9cqi)/1 var(--mono); color:rgba(209,254,255,.7); letter-spacing:.06em; text-transform:uppercase}
.ch-screen__bar i{width:1.3cqi; height:1.3cqi; border-radius:50%; background:rgba(209,254,255,.35)}
.ch-screen__bar span{margin-left:auto}
.ch-win{position:absolute; width:47%; height:41%; background:#0e2a33; border:1px solid rgba(209,254,255,.22); border-radius:1.4cqi; overflow:hidden; box-shadow:0 2cqi 4cqi -2cqi rgba(0,0,0,.6); transition:transform .5s var(--ease), border-color .4s, box-shadow .4s}
.ch-win:nth-child(2){left:3%; top:11%} .ch-win:nth-child(3){left:51.5%; top:9.5%} .ch-win:nth-child(4){left:3%; top:55%} .ch-win:nth-child(5){left:51.5%; top:53.5%}
.ch-win.on{border-color:var(--mint); box-shadow:0 0 0 2px var(--mint), 0 2cqi 5cqi -2cqi rgba(0,0,0,.7); transform:translateY(-1.2%) scale(1.03); z-index:2}
.ch-win__t{display:flex; align-items:center; gap:.9cqi; height:17%; padding:0 1.6cqi; background:rgba(209,254,255,.07); font:600 max(.66rem,2.1cqi)/1 var(--mono); letter-spacing:.07em; text-transform:uppercase; color:var(--aqua)}
.ch-win__t i{width:1cqi; height:1cqi; border-radius:50%; background:rgba(209,254,255,.35)}
.ch-win__t span{margin-left:.6cqi}
.ch-win__c{position:absolute; inset:17% 0 0 0; padding:2cqi}
.ch-g-play{position:absolute; left:50%; top:44%; width:7cqi; height:7cqi; margin:-3.5cqi 0 0 -3.5cqi; border-radius:50%; background:var(--mint)}
.ch-g-play::after{content:""; position:absolute; left:39%; top:28%; border-left:2.6cqi solid var(--slate); border-top:1.6cqi solid transparent; border-bottom:1.6cqi solid transparent}
.ch-g-prog{position:absolute; left:2cqi; right:2cqi; bottom:2.2cqi; height:.7cqi; border-radius:1cqi; background:rgba(209,254,255,.18)}
.ch-g-prog::before{content:""; position:absolute; left:0; top:0; bottom:0; width:38%; background:var(--mint); border-radius:1cqi}
.ch-g-wave{position:absolute; left:2cqi; right:2cqi; top:22%; bottom:22%; display:flex; align-items:center; gap:.55cqi}
.ch-g-wave i{flex:1; height:var(--h); background:var(--aqua); opacity:.8; border-radius:1cqi}
.ch-win.on .ch-g-wave i{animation:ch-wave .6s ease-in-out 4 alternate; animation-delay:var(--d)}
@keyframes ch-wave{to{transform:scaleY(.45)}}
.ch-g-live{position:absolute; left:2cqi; top:2cqi; font:800 1.7cqi/1 var(--display); letter-spacing:.08em; background:var(--coral); color:var(--slate); padding:.6cqi 1cqi; border-radius:.6cqi}
.ch-g-vid{position:absolute; left:2cqi; top:2cqi; bottom:2cqi; width:56%; border-radius:1cqi; background:rgba(209,254,255,.08)}
.ch-g-chat{position:absolute; right:2cqi; top:2cqi; bottom:2cqi; width:32%; display:flex; flex-direction:column; justify-content:flex-end; gap:1cqi}
.ch-g-chat i{display:block; height:1.3cqi; width:var(--w); border-radius:1cqi; background:rgba(209,254,255,.3)}
.ch-g-ad{position:absolute; left:2cqi; top:2cqi; font:800 1.7cqi/1 var(--display); letter-spacing:.08em; background:var(--aqua); color:var(--slate); padding:.6cqi 1cqi; border-radius:.6cqi}
.ch-g-skip{position:absolute; right:2cqi; bottom:2cqi; font:700 1.7cqi/1 var(--display); color:#fff; border:1px solid rgba(255,255,255,.6); padding:.9cqi 1.4cqi; border-radius:.6cqi}
.ch-g-prod{position:absolute; left:50%; top:46%; width:12cqi; height:12cqi; margin:-6cqi 0 0 -6cqi; border-radius:50%; border:1.2cqi solid rgba(209,254,255,.22); border-top-color:var(--mint)}
.ch-screen__stand{width:16%; height:clamp(18px,4cqi,34px); margin:0 auto; background:#0b1f25; clip-path:polygon(18% 0, 82% 0, 100% 100%, 0 100%)}
.ch-screen__foot{width:34%; height:clamp(6px,1.2cqi,10px); margin:0 auto; background:#0b1f25; border-radius:999px}

/* ---------- 8. ER ---------- */
.ch-er__g{display:grid; grid-template-columns:minmax(0,8fr) minmax(0,4fr); gap:var(--gap); align-items:stretch}
.ch-er__g > *{min-width:0}
.ch-ercard{position:relative; background:#fff; color:var(--slate); border-radius:var(--r-xl); overflow:hidden; display:flex; flex-direction:column; box-shadow:0 30px 60px -34px rgba(0,0,0,.7)}
.ch-ercard__tape{height:18px; flex:none; background:repeating-linear-gradient(-45deg, var(--hz) 0 12px, var(--hz-ink) 12px 24px)}
.ch-ercard__b{flex:1; display:flex; flex-direction:column; padding:var(--pad-card)}
.ch-ercard h3{font-size:clamp(1.5rem,2.5vw,2.1rem); font-stretch:114%; font-weight:900; text-transform:uppercase; line-height:1; margin:0 0 .3em}
.ch-ercard .sub{font-weight:700; font-size:1.08rem; color:var(--logo-teal); margin:0 0 18px}
.ch-erlist{flex:1; list-style:none; padding:0; margin:0; display:grid; grid-template-columns:repeat(2,minmax(0,1fr)); grid-auto-rows:1fr; gap:0 28px}
.ch-erlist li{position:relative; display:flex; align-items:center; margin:0; padding:12px 0 12px 36px; border-top:1.5px solid var(--line); font-size:1.1rem; line-height:1.36; font-weight:600}
.ch-erlist li:first-child{grid-column:1/-1}
.ch-erlist li::before{content:""; position:absolute; left:2px; top:50%; margin-top:-9px; width:20px; height:18px; background:var(--teal); clip-path:polygon(50% 0, 100% 100%, 0 100%)}
.ch-911{display:flex; flex-direction:column; background:var(--coral); color:var(--slate); border-radius:var(--r-xl); padding:var(--pad-card)}
.ch-911 h3{font-family:var(--display); font-size:clamp(2.2rem,4vw,3.4rem); font-stretch:122%; font-weight:900; text-transform:uppercase; margin:0 0 .12em; line-height:.95}
.ch-911 p{margin:0 0 10px; font-weight:800; font-size:1.12rem}
.ch-911 ul{list-style:none; margin:0; padding:0; font-weight:600; font-size:1.04rem; line-height:1.38}
.ch-911 li{position:relative; margin:0; padding:7px 0 7px 22px; border-top:1.5px solid rgba(29,65,78,.22)}
.ch-911 li::before{content:""; position:absolute; left:2px; top:.95em; width:9px; height:9px; border-radius:50%; background:var(--slate)}
.ch-911 .ch-911__later{margin:auto 0 0; padding-top:14px; border-top:2.5px solid var(--slate); font-weight:600; font-size:1rem; line-height:1.45}
.ch-911 ul{margin-bottom:16px}
.ch-say,.ch-u18{display:flex; flex-direction:column; justify-content:center; border:1px solid var(--line-dark); border-radius:var(--r-xl); padding:var(--pad-card); background:rgba(255,255,255,.05)}
.ch-say{container-type:inline-size}
.ch-say .ch-say__q{font-family:var(--display); font-weight:900; font-stretch:118%; font-size:clamp(1.7rem,7.2cqi,3.6rem); overflow-wrap:anywhere; line-height:1; color:var(--mint); margin:0 0 .28em; text-transform:uppercase}
.ch-say p:not([class]){color:rgba(255,255,255,.9); font-size:1.08rem; margin:0}
.ch-say .ch-k{margin-bottom:12px}
.ch-u18 h3{font-size:1.4rem; margin:0 0 .4em}
.ch-u18 p{margin:0; color:rgba(255,255,255,.9); font-size:1.02rem; line-height:1.55}
.ch-er__foot{display:flex; flex-wrap:wrap; gap:14px 24px; align-items:center; justify-content:space-between; margin-top:24px}
.ch-er__foot .ch-cite{margin:0; flex:1 1 420px; max-width:86ch}

/* ---------- 9. friend ---------- */
.ch-fr{display:grid; grid-template-columns:minmax(0,1fr) minmax(0,1fr); gap:0 var(--gap); align-items:stretch}
.ch-fr__col{display:grid; grid-template-rows:subgrid; grid-row:span 4; row-gap:10px; border-radius:var(--r-xl); padding:var(--pad-card); min-width:0}
.ch-fr__col ul{display:contents}
.ch-fr__col--do{background:var(--aqua)}
.ch-fr__col--dont{background:var(--mist); border:1px solid var(--line)}
.ch-fr__col h3{display:flex; align-items:center; gap:12px; font-size:1.5rem; font-stretch:115%; text-transform:uppercase; font-weight:900; margin:0 0 6px}
.ch-fr__col h3 i{width:34px; height:34px; border-radius:50%; flex:none; display:grid; place-items:center; position:relative}
.ch-fr__col--do h3 i{background:var(--teal)}
.ch-fr__col--do h3 i::after{content:""; width:12px; height:7px; border-left:3px solid #fff; border-bottom:3px solid #fff; transform:translateY(-2px) rotate(-45deg)}
.ch-fr__col--dont h3 i{background:var(--coral)}
.ch-fr__col--dont h3 i::before,.ch-fr__col--dont h3 i::after{content:""; position:absolute; width:16px; height:3px; background:var(--slate); border-radius:2px; transform:rotate(45deg)}
.ch-fr__col--dont h3 i::after{transform:rotate(-45deg)}
.ch-fr__col ul{list-style:none; margin:0; padding:0; display:grid; gap:10px}
.ch-fr__col li{display:flex; align-items:center; margin:0; padding:14px 18px; border-radius:16px 16px 16px 4px; background:#fff; font-family:var(--display); font-weight:700; font-stretch:104%; font-size:1.12rem; line-height:1.3; border:1px solid var(--line)}
.ch-fr__col--dont li{color:var(--ink-soft)}
.ch-fr__note{margin:var(--gap) 0 0; font-weight:600; font-size:1.06rem}

/* ---------- 10. hotlines ---------- */
.ch-hl{display:grid; grid-template-columns:repeat(4,minmax(0,1fr)); gap:14px}
.ch-hl > div{display:grid; grid-template-rows:subgrid; grid-row:span 3; row-gap:4px; background:#fff; border:1px solid var(--line); border-radius:16px; padding:18px 20px; min-width:0}
.ch-hl b{display:block; align-self:end; font-family:var(--display); font-weight:800; font-stretch:104%; font-size:1.08rem; line-height:1.2; padding-bottom:8px; margin-bottom:4px; border-bottom:1px solid var(--line); color:var(--slate)}
.ch-hl a{display:flex; gap:10px; align-items:center; min-height:32px; font-family:var(--display); font-weight:800; font-stretch:104%; font-size:1.08rem; line-height:1.25; color:var(--logo-teal); text-decoration:none}
.ch-hl a small{flex:none; width:3.4em; font-family:var(--mono); font-size:.7rem; letter-spacing:.08em; text-transform:uppercase; font-weight:600; color:var(--ink-soft)}
.ch-hl a:hover{text-decoration:underline; text-decoration-color:var(--mint); text-decoration-thickness:3px}
@media (pointer:coarse){ .ch-hl a{min-height:44px} }
.ch-hl__foot{display:flex; flex-wrap:wrap; gap:14px 24px; align-items:center; justify-content:space-between; margin-top:22px}
.ch-hl__foot p{margin:0; font-weight:600}

/* ---------- 11. posters ---------- */
.ch-post{display:grid; grid-template-columns:minmax(0,5fr) minmax(0,7fr); gap:clamp(28px,4vw,56px); align-items:center}
.ch-post .btns{align-items:center; gap:14px 22px}
.ch-post .lede{color:rgba(255,255,255,.88)}
.ch-lockers{position:relative; display:grid; grid-template-columns:repeat(3,minmax(0,1fr)); gap:6px; height:clamp(300px,30vw,420px)}
.ch-locker{position:relative; background:var(--logo-teal); border-radius:6px; box-shadow:inset 0 0 0 1px rgba(209,254,255,.12), inset 0 -40px 60px -40px rgba(0,0,0,.35)}
.ch-locker::before{content:""; position:absolute; left:22%; right:22%; top:7%; height:16%; background:repeating-linear-gradient(180deg, rgba(8,26,32,.75) 0 4px, transparent 4px 10px); border-radius:2px}
.ch-locker::after{content:""; position:absolute; right:12%; top:46%; width:9%; min-width:8px; height:15%; border-radius:4px; background:rgba(209,254,255,.32)}
.ch-lockers .ch-lb{position:absolute; z-index:2}
.ch-lockers .ch-lb--l1{width:60%; left:5%; top:43%; transform:rotate(-6deg); z-index:3}
.ch-lockers .ch-lb--l2{width:42%; right:3%; top:7%; transform:rotate(5deg)}
.ch-lockers .ch-label{box-shadow:0 0 0 1.2cqi #fff, 0 18px 30px -12px rgba(0,0,0,.6)}

/* ---------- 12. schools + sources ---------- */
.ch-sch{display:grid; grid-template-columns:minmax(0,1fr) auto; gap:20px 40px; align-items:center}
.ch-sch h2{margin:0 0 .25em}
.ch-sch p:not(.eyebrow){margin:0; font-size:var(--fs-lede); font-weight:500}
.ch-src{columns:2; column-gap:clamp(28px,4vw,56px); padding:18px 0 0 1.6em; margin:0; border-top:2px solid var(--slate); font-size:.92rem; line-height:1.5; color:var(--ink-soft)}
.ch-src li{break-inside:avoid; margin:0 0 12px; padding-left:4px}
.ch-src li::marker{font-family:var(--mono); font-size:.8rem; font-weight:600; color:var(--logo-teal)}
.ch-src li span{display:block; font-weight:700; color:var(--slate)}
.ch-src i{font-style:italic}
.ch-src b{color:var(--slate); font-weight:600}
.ch-srcfoot{display:flex; flex-wrap:wrap; gap:10px 24px; justify-content:space-between; align-items:center; margin-top:14px; padding-top:16px; border-top:1px solid var(--line); font-size:.92rem; color:var(--ink-soft)}
.ch-srcfoot p{margin:0}

/* ---------- responsive ---------- */
@media (max-width:1100px){ .ch-pillars{grid-template-columns:repeat(2,minmax(0,1fr))} .ch-hl{grid-template-columns:repeat(2,minmax(0,1fr))} }
@media (min-width:761px) and (max-width:1100px){ .ch-rc__ex--4{grid-template-columns:minmax(0,1fr)} }
@media (max-width:960px){
  .ch-common,.ch-force,.ch-cons,.ch-film,.ch-er__g,.ch-post{grid-template-columns:minmax(0,1fr)}
  .ch-ex{grid-template-columns:repeat(2,minmax(0,1fr))}
  .ch-signal{grid-template-columns:minmax(0,1fr) minmax(0,1fr)}
  .ch-signal > div:last-child{grid-column:1/-1; border-left:0; border-top:1px solid var(--line-dark); padding-left:0}
  .ch-film .ch-screen{max-width:620px}
}
@media (max-width:860px){
  .ch-hero > .wrap{grid-template-columns:minmax(0,1fr)}
  .ch-hero__art{order:-1; max-width:460px; padding-top:12%}
  .ch-clock__head{grid-template-columns:minmax(0,1fr)}
  .ch-clock__ctl{flex-direction:row; align-items:center; justify-content:space-between; flex-wrap:wrap}
}
@media (max-width:760px){
  .ch-mf__head{display:none}
  .ch-mf__row{grid-template-columns:minmax(0,1fr)}
  .ch-mf__myth{padding:20px 0 6px} .ch-mf__tag{display:none}
  .ch-mf__fact{border-left:0; padding:8px 0 22px; min-height:112px}
  .ch-peel{left:0; top:6px; bottom:16px}
  .ch-dots{grid-template-columns:repeat(20,minmax(0,1fr))}
  .ch-rate{grid-template-columns:minmax(0,1fr)}
  .ch-fr{grid-template-columns:minmax(0,1fr); gap:var(--gap)}
  .ch-fr__col{grid-row:auto; grid-template-rows:none}
  .ch-erlist{grid-template-columns:minmax(0,1fr); grid-auto-rows:auto}
  .ch-movers{grid-template-columns:minmax(0,1fr)}
  .ch-movers .btn{justify-self:start}
  .ch-sch{grid-template-columns:minmax(0,1fr)}
  .ch-src{columns:1}
}
@media (max-width:620px){
  .ch-ex,.ch-pillars,.ch-hl{grid-template-columns:minmax(0,1fr)}
  .ch-signal{grid-template-columns:minmax(0,1fr)}
  .ch-signal > div{border-left:0; border-top:1px solid var(--line-dark); padding:18px 0}
  .ch-signal > div:first-child{border-top:0}
  .ch-911 ul{columns:1}
  .ch-rc__g{grid-template-columns:minmax(0,1fr)}
  .ch-rc__box{justify-self:start; text-align:left}
  .ch-rc__d{border-left:0; border-top:3px solid currentColor; padding:12px 0 0}
  .ch-rc__ex li{grid-template-columns:minmax(0,1fr)}
  .ch-rc__ex em{justify-self:start}
  .ch-lockers{height:260px}
  .ch-pillar__L{font-size:3.6rem}
  .ch-cols{margin-left:32px} .ch-cols__x{margin-left:32px} .ch-cols__grid i span{left:-32px; width:26px}
  .ch-hb{grid-template-columns:minmax(0,100px) minmax(0,1fr) auto}
  .ch-pillar{grid-template-rows:none; grid-row:auto; grid-template-columns:auto minmax(0,1fr); column-gap:16px; padding:18px 18px 20px}
  .ch-exh,.ch-hl > div{grid-row:auto; grid-template-rows:none}
  .ch-pillar__L{grid-row:1 / span 3; font-size:3rem; margin:0}
  .ch-stamp{position:static; grid-column:2; justify-self:start; margin:2px 0 10px; transform:rotate(-4deg)}
  .ch-pillar__L{grid-row:1 / span 4}
  .ch-hl{gap:8px} .ch-hl > div{padding:12px 16px}
}
@media (prefers-reduced-motion:reduce){ .ch-lb--main,.ch-lb--aqua{animation:none} .ch-peel{transition:none} }
'''


# ---------------------------------------------------------------- content
AGES = [('14–17', 'High school age', 'Sexually experienced girls', 11.9), ('18–24', 'College age', 'Women', 31.9), ('25–29', 'Twenties', 'Women', 40.6)]

MYTHS = [
  ('It’s just choking.', 'It’s strangulation.',
   '<p>“Choking” is the word people use. What happens is strangulation: pressure on the neck that cuts off blood to the brain.</p>'
   '<p>In abusive relationships it is one of the strongest warning signs that abuse will turn deadly. Women strangled by an abusive partner had 7.48 times the odds of later being killed by that partner.</p>',
   'Glass et al., 2008'),
  ('It’s safe if you do it right.', 'There’s no safe way.',
   '<p>The carotid arteries can close under about 11 pounds of force, less than the 20 it takes to open a can, and a person can pass out within 5 to 10 seconds. These are not safe limits.</p>',
   'Armstrong &amp; Strack, 2016; Rossen et al., 1943'),
  ('No marks, no harm.', 'No marks means no marks.',
   '<p>In a review of 300 cases, half had no visible neck injury and 35% had marks too small to photograph.</p>__DOTS__',
   'Strack, McClane &amp; Hawley, 2001'),
  ('They said yes, so it’s consent.', 'You’re still responsible for the harm.',
   '<p>Strangulation is a crime in every US state. All 50 states, Washington, D.C., and three US territories have added strangulation or suffocation to their criminal codes, most of them under aggravated assault. If a partner is accidentally hurt or killed, the person who choked them may be held legally and criminally responsible, even when both agreed to it. Laws differ from state to state.</p>',
   'Alliance for HOPE International, 2026'),
  ('They felt fine after, so they’re fine.', 'Some of it shows up later.',
   '<p>Swelling in the throat can develop hours later. A stroke from a torn artery can happen days or weeks later. If symptoms start or get worse, go back for care, even if you were already seen. <a class="link" href="#er">Signs that need the ER</a></p>',
   'Training Institute on Strangulation Prevention, rev. 2022'),
]

PILLARS = [
  ('S', 'Sober', 'Consent needs a clear head.', 'Strangulation cuts off blood to the brain. The person being choked stops thinking clearly before they pass out.'),
  ('R', 'Revocable', 'Consent means you can stop it at any time.', 'In experiments, some people being strangled could not speak or move to say stop, and some forgot they could end it.'),
  ('O', 'Ongoing', 'Consent has to last the whole time.', 'A person can pass out 5 to 10 seconds after the carotid arteries close. Someone who is unconscious can’t agree to anything.'),
  ('E', 'Enthusiastic', 'Consent has to be clear and keep being shown.', 'You can’t tell by looking whether someone is enjoying it or passing out.'),
]

EXHIBITS = [
  # ordered so each row of three carries a similar amount of text
  ('Sold as merch', 'Thousands', 'of designs featuring phrases like “choke me” encourage the practice with no information about what it can actually do to the neck, and no designs with the correct phrase: strangulation.', ''),
  ('Shared as a meme', '316', 'choking memes analyzed by researchers. Common themes were confusion about communication and consent, and jokes about injury or death.', 'Herbenick et al., 2023'),
  ('Viewed in porn', '4,254', 'university students were studied, and pornography was one of the most commonly reported places they first saw sexual choking.', 'Herbenick et al., 2025'),
  ('Shelved as romance', '51<small>million</small>', 'print romance copies sold a year in the U.S. Sales more than doubled in four years.', 'Circana BookScan, 2025'),
  ('Written as fan fiction', '82,000+', 'works are listed under the “Choking” tag on Archive of Our Own, one of the largest fan-fiction sites.', 'Archive of Our Own, checked September 2026'),
  ('Charted at #1', '6<small>weeks</small>', 'at #1 on the Billboard Hot 100 for a song with a line about choking a partner.', 'Billboard, 2023–24'),
]

ER_SIGNS = [
  'You passed out, even briefly, or can’t remember part of what happened',
  'Your breathing has changed',
  'Swallowing hurts or is difficult',
  'Your voice is hoarse, raspy or deeper, or it’s hard to speak',
  'Your neck hurts or is tender, or there’s a mark or bruise on it',
  'Your vision or hearing has changed, or your ears are ringing',
  'You have a headache, or feel dizzy or lightheaded',
  'There are small red spots in your eyes or on your face',
  'You lost control of your bladder or bowels',
]
CALL_911 = ['is unconscious', 'has trouble breathing', 'has a swelling neck', 'seems confused', 'has weakness or numbness on one side', 'has a seizure', 'shows signs of a stroke: a drooping face, a weak arm, slurred speech']

SAY = ['I’m really sorry that happened to you.', 'Are you hurt? Do you want me to go with you to get checked?', 'What can I do to help?']
DONT = ['Why didn’t you stop it?', 'Lots of people are into that.', 'You seem fine, so it probably wasn’t a big deal.']

LINES = [
  ('RAINN', [('Call', '800-656-4673', 'tel:8006564673'), ('Text', 'HOPE to 64673', 'sms:64673?&body=HOPE')]),
  ('988 Suicide &amp; Crisis Lifeline', [('Call', '988', 'tel:988'), ('Text', '988', 'sms:988')]),
  ('love is respect', [('Call', '1-866-331-9474', 'tel:18663319474'), ('Text', 'LOVEIS to 22522', 'sms:22522?&body=LOVEIS')]),
  ('National Domestic Violence Hotline', [('Call', '1-800-799-7233', 'tel:18007997233'), ('Text', 'START to 88788', 'sms:88788?&body=START')]),
  ('The Trevor Project', [('Call', '1-866-488-7386', 'tel:18664887386'), ('Text', 'START to 678-678', 'sms:678678?&body=START')]),
  ('Crisis Text Line', [('Text', 'HOME to 741741', 'sms:741741?&body=HOME')]),
  ('Childhelp', [('Call', '1-800-422-4453', 'tel:18004224453'), ('Text', '1-800-422-4453', 'sms:18004224453')]),
  ('StrongHearts Native Helpline', [('Call', '1-844-762-8483', 'tel:18447628483'), ('Text', '1-844-762-8483', 'sms:18447628483')]),
]

SOURCES = [
  ('Herbenick et al.', '<i>Sexuality Research and Social Policy</i> (2026), ages 14–17; <i>Archives of Sexual Behavior</i> 54 (2025), ages 18–29.', 'Who has been choked, by age group (national U.S. survey, 2022)'),
  ('Herbenick et al.', '<i>Sexuality Research and Social Policy</i> (2025), 973 undergraduates.', 'Average age students first heard about choking'),
  ('Herbenick, Fu, Miller et al.', '<i>Sexuality Research and Social Policy</i> 22(3) (2025), 4,254 students.', 'Where students first heard about or saw choking'),
  ('Herbenick et al.', '<i>Archives of Sexual Behavior</i> (2022).', 'Age when college students were first choked'),
  ('Herbenick et al.', '<i>Sexuality Research and Social Policy</i> (2025), 3,780 students.', 'Agreed words or signals to stop'),
  ('Herbenick et al.', '“#ChokeMeDaddy,” <i>Archives of Sexual Behavior</i> 52 (2023).', '316 choking memes'),
  ('Sharman, Fitzgerald &amp; Douglas', '<i>Archives of Sexual Behavior</i> 54(2) (2025), 4,702 adults aged 18–35.', 'How each partner described consent'),
  ('Armstrong &amp; Strack', '<i>JAMA Otolaryngology–Head &amp; Neck Surgery</i> 142(9) (2016).', 'Force to close the carotid arteries'),
  ('Rossen, Kabat &amp; Anderson', '<i>Archives of Neurology and Psychiatry</i> 50(5) (1943).', 'Time to pass out'),
  ('Sauvageau et al.', '<i>American Journal of Forensic Medicine and Pathology</i> 32(2) (2011).', 'Time until breathing can stop'),
  ('Strack, McClane &amp; Hawley', '<i>Journal of Emergency Medicine</i> 21(3) (2001).', '300 strangulation cases'),
  ('Glass et al.', '<i>Journal of Emergency Medicine</i> 35(3) (2008).', 'Strangulation and later homicide'),
  ('Alliance for HOPE International', '(2026).', 'Strangulation in state criminal codes'),
  ('Smock, Green &amp; Sturgeon', 'Training Institute on Strangulation Prevention medical recommendations (rev. 2022); Institute for Addressing Strangulation (2024); Faculty of Forensic &amp; Legal Medicine (UK, 2023).', 'Signs that need medical care'),
  ('Circana BookScan', '(2025).', 'U.S. print romance sales'),
  ('Billboard', '(2023–24).', 'Billboard Hot 100'),
  ('Archive of Our Own', '“Choking” tag, checked September 2026.', 'Fan-fiction count'),
]


def dots():
    cells = ''.join('<i class="a"></i>' for _ in range(150)) + ''.join('<i class="b"></i>' for _ in range(105)) + ''.join('<i></i>' for _ in range(45))
    return (f'<div class="ch-dots" role="img" aria-label="300 dots, one for each case: 150 with no visible neck injury, 105 with marks too small to photograph, and 45 with injuries visible enough to photograph.">{cells}</div>'
            '<ul class="ch-dots__k"><li><i class="a"></i><span><b>150</b> no visible neck injury</span></li><li><i class="b"></i><span><b>105</b> marks too small to photograph</span></li><li><i></i><span><b>45</b> injuries visible enough to photograph</span></li></ul>')


def build():
    # ---------- hero
    hero = f'''
<section class="ch-hero" aria-labelledby="ch-h1">
  <span class="wm-daisy" aria-hidden="true"></span>
  <div class="wrap">
    <div class="rise">
      <nav class="crumbs" aria-label="Breadcrumb"><a href="index.html">Home</a><span>/</span><a href="resources.html">Resources</a><span>/</span><span>Choking Hazard</span></nav>
      <p class="eyebrow">A SafeBAE campaign &middot; chokinghazard.org</p>
      <h1 id="ch-h1">There’s no <span class="mk">safe way</span> to choke someone.</h1>
      <p class="ch-open">Prevention has to start early, before the behavior does.</p>
      <p class="lede">Choking Hazard is SafeBAE’s campaign on sexual strangulation, which young people call “choking.” By college, many young people have already heard about choking or encountered it in sexual contexts. Waiting until after high school to talk about the impact and harm of sexual strangulation is too late.</p>
      <div class="btns">{btn('Visit chokinghazard.org', CH, 'mint')}{btn('If it already happened', '#er', 'ghost', arrow=True)}</div>
      <p class="ch-cn"><b>Content note</b><span>Sexual strangulation, injury and death. Press Esc twice to leave quickly.</span></p>
    </div>
    <div class="ch-hero__art" role="img" aria-label="The Choking Hazard warning label: Warning. Choking is a hazard. May cause serious injury or death. chokinghazard.org">
      {label('aqua', ' ch-lb--aqua')}
      {label('', ' ch-lb--main')}
    </div>
  </div>
</section>
<div class="ch-tapes" aria-hidden="true">{tape('ch-tape--a')}{tape('ch-tape--b')}</div>'''

    # ---------- how common
    grid = ''.join(f'<i style="bottom:{v*2}%"><span>{v}%</span></i>' for v in (0, 10, 20, 30, 40, 50))
    cols = ''.join(f'<div class="ch-col" style="--h:{v*2:.1f}%" title="Ages {a}: {v}%"><b>{v}%</b></div>' for a, g, w, v in AGES)
    xs = ''.join(f'<div><span>{a}</span><small>{g}</small><small>{w}</small></div>' for a, g, w, v in AGES)
    common = f'''
<section class="band band--paper" id="how-common">
  <div class="wrap">
    <div class="section-head"><div><p class="eyebrow">National U.S. survey &middot; 2022</p><h2>It starts before college.</h2>
      <p class="lede lede--full">In a 2022 national U.S. survey, 11.9% of sexually experienced girls aged 14 to 17 said a partner had choked them. Among women aged 18 to 24 it was 31.9%, and among women aged 25 to 29, 40.6%.</p></div></div>
    <div class="ch-common">
      <figure class="ch-card ch-chart" data-ch-anim aria-label="Bar chart. Said a partner had choked them: ages 14 to 17, 11.9%; ages 18 to 24, 31.9%; ages 25 to 29, 40.6%.">
        <figcaption><b>Said a partner had choked them</b><span>Lifetime, by age group. Scale 0–50%.</span></figcaption>
        <div class="ch-cols" aria-hidden="true"><div class="ch-cols__grid">{grid}</div><div class="ch-cols__bars">{cols}</div></div>
        <div class="ch-cols__x" aria-hidden="true">{xs}</div>
        {cite('Herbenick et al.')}
      </figure>
      <div class="ch-card ch-first" data-ch-anim>
        <div class="ch-first__age"><b>15</b><p>is the average age students first heard about choking during sex.</p></div>
        <hr>
        <p class="ch-k">Where they first heard about it</p>
        <div class="ch-hb"><span>Friends</span><span class="ch-hb__t"><i style="--w:35%"></i></span><em>35%</em></div>
        <div class="ch-hb"><span>Pornography</span><span class="ch-hb__t"><i style="--w:34.5%"></i></span><em>34.5%</em></div>
        {cite('Herbenick et al., 2025. Bars on a 0–100% scale.')}
        <hr>
        <div class="ch-quarter"><span class="ch-quarter__g" aria-hidden="true"><i></i><i></i><i></i><i></i></span><p><b>1 in 4</b> college students who had been choked were first choked between ages 10 and 17.</p></div>
        {cite('Herbenick et al., 2022')}
      </div>
    </div>
  </div>
</section>'''

    # ---------- what it does to the body
    track_ax = ''.join(f'<span style="left:{s/62*100:.3f}%">{s}{" s" if s == 0 else ""}</span>' for s in (0, 10, 20, 30, 40, 50, 60))
    body_sec = f'''
<section class="band band--slate ch-body" id="body">
  <div class="wrap">
    <div class="ch-force">
      <div>
        <h2>Less force than opening a <span class="mk">can</span>.</h2>
        <p class="lede">The carotid arteries carry blood to the brain. They can close under about 11 pounds of force. Pulling open the tab on a can takes about 20.</p>
        {cite('Armstrong &amp; Strack, 2016')}
      </div>
      <div>
        <figure class="ch-ff" data-ch-anim aria-label="Force Facts label. Opening a can: 20 pounds. Closing the carotid arteries: 11 pounds, 55 percent of the force it takes to open the can.">
          <p class="ch-ff__t">Force Facts</p>
          <p class="ch-ff__sv"><span>1 can</span><span>Amount per can</span></p>
          <div class="ch-ff__big"><span>Force to open</span><b>20 lb</b></div>
          <p class="ch-ff__dv">% of one can*</p>
          <div class="ch-ff__row"><span>The <b>carotid arteries</b> close</span><b>11 lb</b><b>55%</b></div>
          <div class="ch-ff__bar" aria-hidden="true"><i style="--w:55%"></i></div>
          <div class="ch-ff__row"><span>Opening the can</span><b>20 lb</b><b>100%</b></div>
          <div class="ch-ff__bar ch-ff__bar--can" aria-hidden="true"><i style="--w:100%"></i></div>
          <div class="ch-ff__ax" aria-hidden="true"><span style="left:0">0 lb</span><span style="left:25%">5</span><span style="left:50%">10</span><span style="left:75%">15</span><span style="left:100%">20 lb</span></div>
          <p class="ch-ff__fn">* Percent of the force it takes to open a can. Armstrong &amp; Strack, 2016.</p>
        </figure>
        <p class="ch-mini">{TRI}<span><b>These are not safe limits.</b> There is no safe amount of force.</span></p>
      </div>
    </div>

    <div class="ch-clock" id="seconds">
      <div class="ch-clock__head">
        <div><h3>Seconds matter.</h3><p>A person can pass out 5 to 10 seconds after the carotid arteries close. In one study the average was 6.8 seconds. Breathing can stop by about 62 seconds.</p></div>
        <div class="ch-clock__ctl"><span class="ch-clock__n" aria-hidden="true"><b>0.0</b><small>s</small></span><div class="btns">{'<button class="btn btn--mint btn--sm" type="button" data-clock-go>Start the clock</button>'}<button class="btn btn--ghost btn--sm" type="button" data-clock-reset>Reset</button></div></div>
      </div>
      <p class="ch-clock__status" aria-live="polite">Press start to feel how long that is.</p>
      <div class="ch-track" role="img" aria-label="Timeline from 0 to 62 seconds, drawn to scale. A person can pass out between 5 and 10 seconds, 6.8 seconds on average in one study. Breathing can stop by about 62 seconds.">
        <span class="ch-track__band"></span>
        <span class="ch-track__fill"></span>
        <i class="ch-track__mk" style="left:{6.8/62*100:.3f}%"></i>
        <i class="ch-track__mk ch-track__mk--end"></i>
      </div>
      <div class="ch-track__ax" aria-hidden="true">{track_ax}</div>
      <ul class="ch-legend"><li><i class="k-band"></i>5–10 s: a person can pass out</li><li><i class="k-avg"></i>6.8 s: the average in one study</li><li><i class="k-end"></i>62 s: breathing can stop</li></ul>
      {cite('Rossen, Kabat &amp; Anderson, 1943; Sauvageau et al., 2011. Timeline drawn to scale.')}
    </div>
  </div>
</section>'''

    # ---------- myth vs fact
    rows = []
    for i, (m, f, det, c) in enumerate(MYTHS):
        det = det.replace('__DOTS__', dots())
        rows.append(f'''<div class="ch-mf__row"><p class="ch-mf__myth"><span>“{esc(m)}”</span><i class="ch-mf__tag" aria-hidden="true"><b>Myth</b></i></p>
<div class="ch-mf__fact"><div class="ch-mf__in" id="mf-{i+1}" tabindex="-1"><h3>{esc(f)}</h3>{det}{cite(c)}</div>
<button class="ch-peel" type="button" aria-expanded="false" aria-controls="mf-{i+1}">{TRI}<span><b>Warning</b><small>Peel to see what’s true</small></span></button></div></div>''')
    myths = f'''
<section class="band band--aqua" id="myths">
  <div class="wrap">
    <div class="section-head"><div><p class="eyebrow">Myth vs. fact</p><h2>What you’ve heard. What’s actually true.</h2></div></div>
    <div class="ch-mf">
      <div class="ch-mf__head" aria-hidden="true"><span>What you’ve heard</span><span>What’s actually true</span></div>
      {''.join(rows)}
    </div>
    <div class="ch-mf__more"><p>Each fact, with the research behind it, is on chokinghazard.org.</p>{btn('Read the evidence', CH + '#myths', 'slate', 'sm')}</div>
  </div>
</section>'''

    # ---------- consent
    pill = ''.join(f'<article class="ch-pillar"><span class="ch-stamp">Fails</span><span class="ch-pillar__L" aria-hidden="true">{L}</span><h4>{n}</h4><p class="r">{esc(r)}</p><p>{esc(t)}</p></article>' for L, n, r, t in PILLARS)
    consent = f'''
<section class="band band--deep" id="consent">
  <div class="wrap">
    <div class="ch-cons">
      <div><p class="eyebrow">Consent</p><h2>The person doing it is more likely to think it was consensual.</h2>
        <p class="lede">A 2025 survey of 4,702 Australians aged 18 to 35 asked people who had choked a partner, and people who had been choked, how consent was given the last time it happened.</p></div>
      <figure class="ch-cbars" data-ch-anim aria-label="79.1% of people who choked a partner said the partner actively agreed. 56.6% of people who were choked said they actively agreed.">
        <figcaption>Said the person who was choked actively agreed</figcaption>
        <div class="ch-cbar"><span>People who did the choking <b>79.1%</b></span><div class="ch-cbar__t"><i style="--w:79.1%"></i></div></div>
        <div class="ch-cbar ch-cbar--b"><span>People who were choked <b>56.6%</b></span><div class="ch-cbar__t"><i style="--w:56.6%"></i></div></div>
        <div class="ch-cbars__ax" aria-hidden="true"><span>0%</span><span>25%</span><span>50%</span><span>75%</span><span>100%</span></div>
        {cite('Sharman, Fitzgerald &amp; Douglas, 2025')}
      </figure>
    </div>
    <div class="ch-signal">
      <div><b>1 in 2</b><p>U.S. college students choked during their most recent sex had no agreed word or signal to stop.</p></div>
      <div><b>38%</b><p>relied on body language alone.</p>{cite('Herbenick et al., 2025')}</div>
      <div><p class="ch-dont">If you’re the one choking someone, <em>don’t assume they agreed.</em></p></div>
    </div>
    <div class="ch-pillars-head"><h3>Choking can’t meet the pillars of consent.</h3><p>Even if two people agree to it beforehand, the pillars of consent can’t be met once the choking starts.</p></div>
    <div class="ch-pillars">{pill}</div>
    <div class="ch-movers"><p>These are four of SafeBAE’s six pillars of consent, MOVERS: Mutual, Ongoing, Voluntary, Enthusiastic, Revocable and Sober. The film <i>It’s Giving Red Flags</i> teaches all six.</p>{btn('It’s Giving Red Flags', 'film-its-giving-red-flags.html#movers', 'ghost', 'sm', arrow=True)}</div>
  </div>
</section>'''

    # ---------- where it came from
    ex = ''.join(f'<article class="ch-exh"><p class="ch-exh__tag">Exhibit &middot; {esc(t)}</p><p class="ch-exh__fig">{fig}</p><p class="ch-exh__t">{esc(d)}</p>{cite(c) if c else ""}</article>' for t, fig, d, c in EXHIBITS)
    where = f'''
<section class="band band--paper" id="where">
  <div class="wrap">
    <div class="section-head"><div><p class="eyebrow">Where it came from &middot; six exhibits</p><h2>It didn’t come out of nowhere.</h2>
      <p class="lede lede--full">It’s in your feed, sold as merch, shelved as romance, shared as a meme, written as fan fiction, and even on the Billboard Hot 100.</p></div></div>
    <div class="ch-ex">{ex}</div>
  </div>
</section>'''

    # ---------- media ratings
    ratings = f'''
<section class="band band--slate" id="ratings">
  <div class="wrap">
    <div class="section-head"><div><p class="eyebrow">Media ratings</p><h2>How screens and books show choking</h2>
      <p class="lede lede--full" style="color:rgba(255,255,255,.88)">SafeBAE rates TV, film, comedy and bestselling books that show choking. Scenes that play it as comedy, eroticize it, romanticize it or treat it as harmless are rated CH. Work that shows the harm or treats it as dangerous is rated BAE.</p></div></div>
    <div class="ch-rate">
      <div class="ch-rc ch-rc--ch">
        <p class="ch-rc__pre">The following is rated</p>
        <div class="ch-rc__g"><div class="ch-rc__box"><b>CH</b><span>Choking hazard</span></div><p class="ch-rc__d">Contains depictions of strangulation. There is no safe way to strangle someone.</p></div>
        <p class="ch-rc__lbl">Rated CH when a scene is</p>
        <ul class="ch-rc__ex ch-rc__ex--4"><li><b>Played as comedy</b></li><li><b>Eroticized</b></li><li><b>Romanticized</b></li><li><b>Treated as harmless</b></li></ul>
        <p class="ch-rc__by">Rated by chokinghazard.org</p>
      </div>
      <div class="ch-rc ch-rc--bae">
        <p class="ch-rc__pre">The following is rated</p>
        <div class="ch-rc__g"><div class="ch-rc__box"><b>BAE</b><span>Safe before anyone else</span></div><p class="ch-rc__d">Shows the harm of strangulation, or treats it as dangerous.</p></div>
        <p class="ch-rc__lbl">Rated BAE</p>
        <ul class="ch-rc__ex">
          <li><span><b>Big Little Lies</b><small>HBO &middot; 2017</small></span><em>Shows the harm</em></li>
          <li><span><b>Mary Beth Barone: Galaxy Brain</b><small>Netflix &middot; 2026 &middot; Stand-up</small></span><em>Treated as dangerous</em></li>
        </ul>
        <p class="ch-rc__by">Rated by chokinghazard.org</p>
      </div>
    </div>
    <div class="ch-rate-foot"><p>The full list covers TV, film, stand-up, songs and bestselling books.</p>{btn('See the media ratings', CH_RATINGS, 'mint')}</div>
  </div>
</section>'''

    # ---------- film
    wave = ''.join(f'<i style="--h:{h}%;--d:-{d}s"></i>' for h, d in [(30, .1), (62, .5), (44, .3), (80, .7), (54, .2), (92, .6), (38, .4), (70, .9), (48, .15), (86, .55), (34, .35), (64, .75), (42, .25), (76, .65), (28, .45), (58, .85)])
    chat = ''.join(f'<i style="--w:{w}%"></i>' for w in (70, 92, 56, 84, 64, 96, 48))
    film = f'''
<section class="band band--mist" id="film">
  <div class="wrap ch-film">
    <div>
      <p class="eyebrow">Short film &middot; in production</p>
      <h2>One boy’s evening at his computer</h2>
      <p class="lede">A screenlife short film from SafeBAE, told through the four videos he watches: a video essay, a podcast, a livestream and a commercial.</p>
      <div class="ch-mail"><p>To ask about a screening, email</p><span class="copy">{MAIL}<button type="button" data-copy="{MAIL}">Copy</button></span></div>
      <div class="btns">{btn('About the film', CH_FILM, 'teal')}{btn('Email SafeBAE', 'mailto:' + MAIL + '?subject=Choking%20Hazard%20film%20screening', 'ghost')}</div>
    </div>
    <div class="ch-screen" aria-hidden="true">
      <div class="ch-screen__mon">
        <div class="ch-screen__bar"><i></i><i></i><i></i><span>In production</span></div>
        <div class="ch-win on"><div class="ch-win__t"><i></i><i></i><i></i><span>Video essay</span></div><div class="ch-win__c"><span class="ch-g-play"></span><span class="ch-g-prog"></span></div></div>
        <div class="ch-win"><div class="ch-win__t"><i></i><i></i><i></i><span>Podcast</span></div><div class="ch-win__c"><div class="ch-g-wave">{wave}</div></div></div>
        <div class="ch-win"><div class="ch-win__t"><i></i><i></i><i></i><span>Livestream</span></div><div class="ch-win__c"><span class="ch-g-vid"></span><span class="ch-g-live">Live</span><span class="ch-g-chat">{chat}</span></div></div>
        <div class="ch-win"><div class="ch-win__t"><i></i><i></i><i></i><span>Commercial</span></div><div class="ch-win__c"><span class="ch-g-ad">Ad</span><span class="ch-g-prod"></span><span class="ch-g-skip">Skip &rsaquo;</span></div></div>
      </div>
      <div class="ch-screen__stand"></div><div class="ch-screen__foot"></div>
    </div>
  </div>
</section>'''

    # ---------- if it already happened
    er = f'''
<section class="band band--deep" id="er">
  <div class="wrap">
    <div class="section-head"><div><p class="eyebrow">If it has already happened</p><h2>Get medical help. Say what happened.</h2>
      <p class="lede lede--full" style="color:rgba(255,255,255,.88)">Some injuries show up later. Swelling in the throat can develop hours afterward, and a stroke from a torn artery can happen days or weeks later.</p></div></div>
    <div class="ch-er__g">
      <div class="ch-ercard"><span class="ch-ercard__tape" aria-hidden="true"></span><div class="ch-ercard__b">
        <h3>Go to an emergency room today if:</h3>
        <p class="sub">Even with no marks, and even if you agreed to it.</p>
        <ul class="ch-erlist">{''.join(f'<li>{esc(s)}</li>' for s in ER_SIGNS)}</ul>
      </div></div>
        <div class="ch-911"><h3>Call 911</h3><p>if someone:</p><ul>{''.join(f'<li>{esc(s)}</li>' for s in CALL_911)}</ul><p class="ch-911__later">If symptoms start or get worse later, go back, even if you were already seen. A drooping face, a weak arm or slurred speech at any time in the weeks after means call 911.</p></div>
        <div class="ch-say"><p class="ch-k">At the front desk, say</p><p class="ch-say__q">“I was strangled.”</p><p>Not only “my throat hurts.” The word tells staff which injuries to check for.</p></div>
        <div class="ch-u18"><h3>If you’re under 18</h3><p>You can still get medical care. Staff may be required to report abuse of a minor, and you can ask what they would report before you share more.</p></div>
    </div>
    <div class="ch-er__foot">{cite('Training Institute on Strangulation Prevention medical recommendations (Smock, Green &amp; Sturgeon, rev. 2022); Institute for Addressing Strangulation (2024); Faculty of Forensic &amp; Legal Medicine (UK, 2023)')}{btn('What to expect at the ER', CH_RES + '#er', 'mint')}</div>
  </div>
</section>'''

    friend = f'''
<section class="band band--paper" id="friend">
  <div class="wrap">
    <div class="section-head"><div><h2>If a friend tells you it happened</h2>
      <p class="lede lede--full">What you say first affects whether your friend tells anyone else and whether they get medical care.</p></div></div>
    <div class="ch-fr">
      <div class="ch-fr__col ch-fr__col--do"><h3><i aria-hidden="true"></i>Say</h3><ul role="list">{''.join(f'<li>“{esc(s)}”</li>' for s in SAY)}</ul></div>
      <div class="ch-fr__col ch-fr__col--dont"><h3><i aria-hidden="true"></i>Don’t say</h3><ul role="list">{''.join(f'<li>“{esc(s)}”</li>' for s in DONT)}</ul></div>
    </div>
    <p class="ch-fr__note">If your friend has any of the <a class="link" href="#er">warning signs</a>, go with them to an emergency room today. If they have trouble breathing, seem confused or pass out, call 911.</p>
  </div>
</section>'''

    vibe = vibe_band('If you strangled someone without their consent, pressured them, or went further than they agreed to, Vibe Check can help you reflect on what happened and what taking responsibility could look like.',
                     heading='Worried you hurt someone?')

    hl = ''.join('<div><b>' + n + '</b>' + ''.join(f'<a href="{h}"><small>{v}</small>{t}</a>' for v, t, h in ls) + '</div>' for n, ls in LINES)
    hotlines = f'''
<section class="band band--mist" id="hotlines">
  <div class="wrap">
    <div class="section-head"><div><h2>Talk to someone now</h2>
      <p class="lede lede--full">These lines are free and confidential. If someone is in immediate danger, call 911.</p></div></div>
    <div class="ch-hl">{hl}</div>
    <div class="ch-hl__foot"><p>More free lines, including a legal hotline and a directory of local rape crisis centers:</p><button class="btn btn--coral" type="button" data-open-help>All hotlines</button></div>
  </div>
</section>'''

    posters = f'''
<section class="band band--slate" id="posters">
  <div class="wrap ch-post">
    <div>
      <p class="eyebrow">Free to download and print</p>
      <h2>Put one up.</h2>
      <p class="lede">Free Choking Hazard warning posters, and the warning sticker in yellow or aqua. Download them, print them and put them up where young people will see them.</p>
      <div class="btns">{btn('Download posters and the sticker', CH_DL, 'mint')}<a class="arrow-link" href="posters.html">More SafeBAE posters</a></div>
    </div>
    <div class="ch-lockers" role="img" aria-label="The yellow and aqua warning stickers on a row of school lockers">
      <span class="ch-locker"></span><span class="ch-locker"></span><span class="ch-locker"></span>
      {label('', ' ch-lb--l1')}
      {label('aqua', ' ch-lb--l2')}
    </div>
  </div>
</section>'''

    schools = f'''
<section class="band band--aqua band--tight" id="schools">
  <div class="wrap ch-sch">
    <div><p class="eyebrow">For schools &middot; launches November 2026</p><h2>Sexual Strangulation Prevention</h2>
      <p>SafeBAE’s new program for schools on sexual strangulation, which young people call “choking,” launches in November 2026.</p></div>
    <div class="btns">{btn('Request a program', 'request-a-program.html#start', 'slate', arrow=True)}</div>
  </div>
</section>'''

    src = ''.join(f'<li><span>{t}</span>{a_}{" " if w.startswith("(") else ", "}{w}</li>' for a_, w, t in SOURCES)
    sources = f'''
<section class="band band--paper band--tight" id="sources">
  <div class="wrap">
    <h2 style="font-size:clamp(1.5rem,2.4vw,2rem)">Sources</h2>
    <ol class="ch-src">{src}</ol>
    <div class="ch-srcfoot"><p>This information is not medical or legal advice. If you are in immediate danger, call 911.</p><a class="arrow-link" href="{CH}" target="_blank" rel="noopener">Learn more at chokinghazard.org</a></div>
  </div>
</section>'''

    body = hero + common + body_sec + myths + consent + where + ratings + film + er + friend + vibe + hotlines + posters + schools + sources

    js = r'''<script>
(function(){
  var d = document, reduce = window.matchMedia && window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  /* charts grow into place the first time they are seen */
  var anims = [].slice.call(d.querySelectorAll('[data-ch-anim]'));
  if('IntersectionObserver' in window && !reduce){
    var io = new IntersectionObserver(function(es){ es.forEach(function(e){ if(e.isIntersecting){ e.target.classList.remove('ch-pre'); io.unobserve(e.target); } }); }, {rootMargin:'0px 0px -12% 0px'});
    anims.forEach(function(el){ if(el.getBoundingClientRect().top > window.innerHeight){ el.classList.add('ch-pre'); io.observe(el); } });
  }
  /* myth vs fact: peel the warning sticker */
  [].forEach.call(d.querySelectorAll('.ch-peel'), function(b){
    b.addEventListener('click', function(){
      var row = b.closest('.ch-mf__row'), t = d.getElementById(b.getAttribute('aria-controls'));
      row.classList.add('open'); b.setAttribute('aria-expanded', 'true');
      setTimeout(function(){ b.hidden = true; if(t){ try{ t.focus({preventScroll:true}); }catch(e){ t.focus(); } } }, reduce ? 0 : 650);
    });
  });
  /* seconds matter: a real-time clock to 62 seconds */
  var ck = d.querySelector('.ch-clock');
  if(ck){
    var n = ck.querySelector('.ch-clock__n b'), fill = ck.querySelector('.ch-track__fill'), go = ck.querySelector('[data-clock-go]'), rs = ck.querySelector('[data-clock-reset]'), st = ck.querySelector('.ch-clock__status');
    var T = 62, t = 0, run = false, last = 0, said = {}, PROMPT = st.textContent;
    var MS = [[5, '5 seconds. From here, a person can pass out.'], [6.8, '6.8 seconds. The average time to pass out in one study.'], [10, '10 seconds. Someone who has passed out can’t agree to anything.'], [62, '62 seconds. Breathing can stop.']];
    function draw(){ n.textContent = t.toFixed(1); fill.style.width = (t / T * 100) + '%'; ck.classList.toggle('past5', t >= 5); ck.classList.toggle('done', t >= T); MS.forEach(function(m){ if(t >= m[0] && !said[m[0]]){ said[m[0]] = 1; st.textContent = m[1]; } }); }
    function tick(now){ if(!run || !ck.isConnected) return; t = Math.min(T, t + (now - last) / 1000); last = now; draw(); if(t >= T){ run = false; go.textContent = 'Start again'; return; } requestAnimationFrame(tick); }
    go.addEventListener('click', function(){ if(run){ run = false; go.textContent = 'Resume'; return; } if(t >= T){ t = 0; said = {}; st.textContent = PROMPT; } run = true; go.textContent = 'Pause'; last = performance.now(); requestAnimationFrame(tick); });
    rs.addEventListener('click', function(){ run = false; t = 0; said = {}; st.textContent = PROMPT; go.textContent = 'Start the clock'; draw(); });
    /* the clock stops itself at 62 seconds, and pauses if it is scrolled out of view */
    if('IntersectionObserver' in window){ new IntersectionObserver(function(es){ es.forEach(function(e){ if(!e.isIntersecting && run){ run = false; go.textContent = 'Resume'; } }); }, {threshold:0}).observe(ck); }
  }
  /* the film: one window at a time comes forward */
  var wins = [].slice.call(d.querySelectorAll('.ch-win'));
  if(wins.length && !reduce && 'IntersectionObserver' in window){
    /* plays through the four videos once when the screen comes into view, then rests on the first */
    var fio = new IntersectionObserver(function(es){ es.forEach(function(e){ if(!e.isIntersecting) return; fio.disconnect();
      var k = 0, n = 0, iv = setInterval(function(){ if(!wins[0].isConnected){ clearInterval(iv); return; } wins[k].classList.remove('on'); k = (k + 1) % wins.length; wins[k].classList.add('on'); if(++n >= wins.length) clearInterval(iv); }, 2400); }); }, {threshold:.5});
    fio.observe(wins[0].parentNode);
  }
})();
</script>'''

    page('choking-hazard.html', 'Choking Hazard · SafeBAE',
         'Choking Hazard is SafeBAE’s campaign on sexual strangulation, which young people call “choking.” There’s no safe way to choke someone: the evidence, myth vs. fact, consent, signs that need medical care, and free warning posters.',
         body, active='resources', body_class='ch', head_extra=f'<style>{VIBE_CSS}{CSS}</style>', scripts=js)


if __name__ == '__main__':
    build()
