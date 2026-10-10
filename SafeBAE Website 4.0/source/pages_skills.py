"""skills-lab.html: the safebae.org landing page for the BAE Skills Lab (https://skills-lab.safebae.org/).
Facts come only from the Lab's own files in /home/claude/assets/skills-lab (README.md, index.html and each tool).
Visual world: the Lab's light, airy look (pale aqua surfaces, white cards with soft shadows, a teal-to-mint rule,
heavy tight Montserrat headings), inside the shared header and footer.
Screenshots: work/sl_capture.py + work/sl_images.py (captured from the local tool files)."""
from lib import *
import films_common as _fc
from films_common import vibe_band
VIBE_CSS = getattr(_fc, 'VIBE_CSS', '')

SKILLS = 'https://skills-lab.safebae.org/'
FEEDBACK = 'https://forms.gle/1cjdUCyw7XFQdkzM9'


def ico(paths, cls='sl-ico'):
    """The Lab's own line icons (from its landing page)."""
    return f'<span class="{cls}" aria-hidden="true"><svg viewBox="0 0 24 24">{paths}</svg></span>'


I_LABEL = '<rect x="5" y="2.5" width="14" height="19" rx="2.5"/><path d="M8.5 8h7M8.5 12h7M8.5 16h4"/>'
I_MUSIC = '<path d="M9 18V5.5l11-2V16"/><circle cx="6.5" cy="18" r="2.6"/><circle cx="17.5" cy="16" r="2.6"/>'
I_GRID = ('<rect x="3" y="4" width="7.2" height="7.2" rx="1.6"/><rect x="13.8" y="4" width="7.2" height="7.2" rx="1.6"/>'
          '<rect x="3" y="12.8" width="7.2" height="7.2" rx="1.6"/><rect x="13.8" y="12.8" width="7.2" height="7.2" rx="1.6"/>')
I_CLOCK = '<circle cx="12" cy="12" r="8.6"/><path d="M12 7.2V12l3.2 2"/>'

# The six tools, shortest first. Every line is from the Lab's landing page or the tool itself.
#  key, name, the tool's own tagline, time, minutes it fits in, crop of the capture (%), what you do, three facts about a round
TOOLS = [
  dict(k='reset-kit', n='Reset Kit', tag='Reset your body first.', time='Under 2 min', min=2, y=36,
       d='Guided breathing and grounding for when you’re overwhelmed, numb, or checked out. Pick one of six short exercises.',
       f=['Six exercises, 30 sec to 2 min each', 'Three paced breathing patterns', '5-4-3-2-1 grounding, body scan'],
       alt='Reset Kit running a box breathing exercise: a circle with a count and “Inhale”'),
  dict(k='supporting-a-survivor', n='Supporting a Survivor', tag='Helpful or Harmful?', full='Supporting a Survivor: Helpful or Harmful?',
       time='3 min', min=3, y=47,
       d='Swipe through things people actually say to survivors and sort what helps from what hurts, before you’re the one who has to say something.',
       f=['Five statements dealt at random', 'Swipe, tap, or use the arrow keys', '“Try saying this instead” tips'],
       alt='Supporting a Survivor showing a statement card with Harmful and Helpful buttons'),
  dict(k='nutrition-label', n='Partner Nutrition Label', tag='Relationship Facts', time='3–8 min', min=3, y=35,
       note=(8, '3 min without the lesson'),
       d='Every food has a label so you can decide what’s good for you. Relationships don’t, so build your own and keep it as a bookmark.',
       f=['Pick 8 ingredients, set a % for each', 'Optional 5-minute lesson first', 'Save as an image or print it'],
       alt='Partner Nutrition Label with five green flag ingredients picked out of eight'),
  dict(k='boundary-flags', n='Boundary Flags', tag='Where are your lines?', time='5 min', min=5, y=27,
       d='Sort 25 real situations into green, yellow, and red flags. This game helps you identify, sort, and understand your own boundaries.',
       f=['25 cards, no right answers', 'Lightning Round: 7 sec per card', 'Ends with your own boundary map'],
       alt='Boundary Flags showing a situation card above red, yellow and green flag buttons'),
  dict(k='listen-closer', n='Listen Closer', tag='Healthy or Unhealthy?', time='5 min', min=5, y=51,
       d='Spin the wheel, hear a clip from a song everyone knows, then decide together: are these lyrics healthy or unhealthy, and which trait do they show?',
       f=['30 songs on a 10-slot wheel', 'Two questions per song, plus a hint', '“Next player” passes the turn'],
       alt='Listen Closer asking whether a song’s lyrics reflect a healthy or unhealthy relationship'),
  dict(k='jeopardy', n='SafeBAE Jeopardy', tag='A 25-question game show', time='10–30 min', min=10, y=49,
       d='Test your knowledge of all things consent and healthy relationships with this 25-question game show style activity.',
       f=['Five categories, $100 to $500', 'Full screen mode for the board', 'Facilitator screen with answer key'],
       alt='SafeBAE Jeopardy with a $200 Consent clue open over the board'),
]

# What three of the tools give someone running a group (from the tools' own facilitator screens).
ROOM = [
  ('SafeBAE Jeopardy', I_GRID, 'A board for the room, an answer key for you',
   'Put the board on full screen, read each clue aloud and let the team answer. The facilitator screen opens any clue with the answer already showing and prints the whole key on two sheets of paper. It is locked with a passphrase.',
   'jeopardy/'),
  ('Listen Closer', I_MUSIC, 'Choose which songs come up',
   'Facilitator Setup lists all 30 songs with their clip times. Play a song directly, block the ones you want to leave out, and reset the played songs to run the game again with a fresh group.',
   'listen-closer/'),
  ('Partner Nutrition Label', I_LABEL, 'Blank bookmarks for the room',
   'Under “For facilitators”, print a landscape page of five blank bookmarks at a true 2 × 6 inches, with dashed cut lines. Set the number of copies in your print dialog.',
   'nutrition-label/'),
]

PICKS = [(0, 'Any'), (2, '2 min'), (3, '3 min'), (5, '5 min'), (10, '10+ min')]

CSS = r'''
body.sl-page{--sl-bg:#f7fdfd; --sl-deep:#eaf8fa; --sl-line:#dbeaed; --sl-ph:#0b1f25;
  --sl-grad:linear-gradient(90deg,var(--teal),var(--mint));
  --sl-shadow:0 4px 16px rgba(29,65,78,.06), 0 1px 3px rgba(29,65,78,.05);
  --sl-shadow-hi:0 16px 40px rgba(29,65,78,.13), 0 3px 8px rgba(29,65,78,.07);
  --sl-head:"Montserrat","Avenir Next","Segoe UI",system-ui,sans-serif}
/* the Lab's heading voice: heavy, tight, mixed case */
body.sl-page main :is(h1,h2,h3){font-family:var(--sl-head); font-weight:800; font-stretch:100%; letter-spacing:-.022em; text-transform:none}
body.sl-page main h2{font-size:clamp(1.85rem,3.4vw,2.9rem); line-height:1.06}
.sl-page .section-head .lede{max-width:none}
.sl-ico{display:grid; place-items:center; flex:none; width:46px; height:46px; border-radius:14px; border:1px solid rgba(19,132,143,.2); background:linear-gradient(150deg, rgba(209,254,255,.85), rgba(21,255,200,.2))}
.sl-ico svg{width:23px; height:23px; fill:none; stroke:var(--logo-teal); stroke-width:1.9; stroke-linecap:round; stroke-linejoin:round}

/* ---------- hero ---------- */
.sl-hero{position:relative; overflow:hidden; color:var(--slate); --wm-o:.1;
  background:radial-gradient(1100px 620px at 50% -20%, rgba(209,254,255,.95), transparent 64%), radial-gradient(820px 480px at 88% 4%, rgba(21,255,200,.2), transparent 62%), linear-gradient(180deg, #e9fbfc 0%, var(--sl-deep) 100%)}
.sl-hero .wm-daisy{color:var(--teal); right:-10%; bottom:-30%}
.sl-hero .wrap{position:relative; z-index:2; display:grid; grid-template-columns:minmax(0,7fr) minmax(0,5fr); gap:clamp(28px,4vw,56px); align-items:center; padding-block:clamp(40px,5vw,68px) calc(clamp(40px,5vw,68px) + 30px)}
.sl-hero .crumbs{color:var(--ink-soft)} .sl-hero .crumbs a{color:var(--logo-teal)} .sl-hero .crumbs a:hover{color:var(--teal)}
.sl-hero h1{font-size:clamp(3.5rem,8.2vw,6.7rem); line-height:.94; letter-spacing:-.045em; color:var(--teal); margin:0}
.sl-hero h1 > span{display:block}
.sl-hero h1 .sl-pre{font-size:.44em; line-height:1.1; letter-spacing:-.03em; color:var(--logo-teal); margin-bottom:.14em}
.sl-hero h1 .mk{background:linear-gradient(transparent 64%, var(--mint) 64% 93%, transparent 93%); padding:0 .05em}
.sl-rule{display:block; width:64px; height:5px; border-radius:99px; background:var(--sl-grad); margin:clamp(18px,2.2vw,26px) 0; transform-origin:left; animation:sl-draw .9s .25s var(--ease) both}
@keyframes sl-draw{from{transform:scaleX(0)}}
.sl-hero .lede{color:var(--ink-soft); max-width:none; margin:0 0 1.3em}
.sl-facts-row{display:flex; flex-wrap:wrap; gap:10px 24px; margin-top:26px; padding-top:20px; border-top:1px solid var(--line)}
.sl-facts-row span{display:inline-flex; align-items:center; gap:9px; font-weight:700; font-size:.98rem; color:var(--logo-teal)}
.sl-facts-row span::before{content:""; width:20px; height:20px; border-radius:50%; flex:none; background:var(--mint) url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 24 24'%3E%3Cpath d='M5 12.5l4.5 4.5L19 7.5' fill='none' stroke='%231d414e' stroke-width='3.2' stroke-linecap='round' stroke-linejoin='round'/%3E%3C/svg%3E") center/13px no-repeat}
/* game pieces: each one opens its tool */
.sl-stage{position:relative; aspect-ratio:1/1.04}
.sl-pc{position:absolute; display:block; text-decoration:none; transform:rotate(var(--r)); transition:transform .4s var(--ease); animation:sl-deal .85s var(--ease) both}
.sl-pc:hover,.sl-pc:focus-visible{transform:rotate(0deg) translateY(-8px) scale(1.03); z-index:6}
.sl-pc:focus-visible{outline:3px solid var(--teal); outline-offset:5px; border-radius:22px}
.sl-piece{display:block; overflow:hidden; background:var(--sl-ph); border:7px solid var(--sl-ph); box-shadow:0 34px 60px -30px rgba(22,53,64,.6), 0 2px 6px rgba(22,53,64,.12)}
.sl-piece img{width:100%; height:100%; object-fit:cover; object-position:top}
.sl-pc--board{left:7%; right:0; top:2%; --r:2.2deg}
.sl-pc--board .sl-piece{aspect-ratio:16/10; border-radius:18px}
.sl-pc--p1{left:0; bottom:0; width:37%; --r:-5deg; z-index:1; animation-delay:.16s}
.sl-pc--p1 .sl-piece{aspect-ratio:390/780; border-radius:30px}
.sl-pc--p2{left:38%; bottom:4%; width:33%; --r:3deg; z-index:2; animation-delay:.28s}
.sl-pc--p2 .sl-piece{aspect-ratio:390/780; border-radius:28px}
.sl-pc--mark{right:1%; bottom:1%; width:22%; --r:7deg; z-index:3; animation-delay:.4s}
.sl-pc--mark .sl-piece{aspect-ratio:1/3; border:0; border-radius:6px; background:#fff; box-shadow:0 30px 50px -24px rgba(22,53,64,.65), 0 0 0 1px rgba(29,65,78,.12)}
@keyframes sl-deal{from{opacity:0; translate:0 30px; rotate:-7deg}}
.sl-tag{position:absolute; z-index:4; font-family:var(--mono); font-weight:600; font-size:.8rem; letter-spacing:.06em; text-transform:uppercase; white-space:nowrap; padding:.45em .75em; border-radius:99px; background:var(--mint); color:var(--slate); box-shadow:0 10px 20px -10px rgba(22,53,64,.6); animation:sl-tag .5s .75s var(--ease) both}
.sl-pc--board .sl-tag{right:5%; top:-14px; rotate:1deg}
.sl-pc--p1 .sl-tag{left:-9%; top:8%; rotate:-1deg; animation-delay:.85s}
.sl-pc--p2 .sl-tag{left:50%; bottom:-14px; translate:-50% 0; animation-delay:.95s}
.sl-pc--mark .sl-tag{right:-8%; top:-15px; animation-delay:1.05s}
@keyframes sl-tag{from{opacity:0; scale:.6}}
@media (max-width:960px){ .sl-hero .wrap{grid-template-columns:minmax(0,1fr)} .sl-stage{width:min(480px,100%); margin-inline:auto} }
@media (max-width:520px){ .sl-facts-row span{font-size:.92rem} .sl-tag{font-size:.72rem} .sl-pc--p1 .sl-tag{left:3%} .sl-pc--mark .sl-tag{right:-2%} .sl-piece{border-width:5px} .sl-pc--p1 .sl-piece{border-radius:22px} .sl-pc--p2 .sl-piece{border-radius:20px} }

/* ---------- the six tools + time picker ---------- */
.sl-tools{position:relative; z-index:3; margin-top:-30px; border-radius:30px 30px 0 0; background:linear-gradient(180deg,#fff 0%, #fff 40%, var(--sl-bg) 100%); padding-top:clamp(40px,4.6vw,64px); box-shadow:0 -20px 44px -30px rgba(22,53,64,.35)}
.sl-pick{position:relative; display:grid; grid-template-columns:auto minmax(0,1fr) minmax(200px,auto); align-items:center; gap:14px clamp(18px,2.4vw,32px); padding:16px clamp(16px,2vw,24px) 21px; margin-bottom:var(--gap); background:#fff; border:1px solid var(--sl-line); border-radius:var(--r-xl); box-shadow:var(--sl-shadow); overflow:hidden}
.sl-pick__q{display:flex; align-items:center; gap:12px; margin:0; font-family:var(--sl-head); font-weight:800; letter-spacing:-.018em; font-size:1.22rem; line-height:1.15; color:var(--logo-teal)}
.sl-pick__q .sl-ico{width:42px; height:42px; border-radius:12px}
.sl-pick__opts{position:relative; display:grid; grid-template-columns:repeat(5,minmax(0,1fr)); padding:5px; border-radius:14px; background:var(--sl-deep); border:1px solid var(--sl-line)}
.sl-pick__thumb{position:absolute; top:5px; bottom:5px; left:5px; width:calc((100% - 10px) / 5); border-radius:10px; background:var(--mint); box-shadow:0 6px 14px -8px rgba(22,53,64,.7), inset 0 0 0 1.5px rgba(29,65,78,.14); transition:transform .38s var(--ease)}
.sl-pick__opts button{position:relative; z-index:1; min-height:48px; padding:0 6px; border:0; border-radius:10px; background:none; cursor:pointer; font-family:var(--sl-head); font-weight:800; font-size:1rem; letter-spacing:-.01em; color:var(--logo-teal); white-space:nowrap; transition:color .2s}
.sl-pick__opts button:hover{color:var(--slate)}
.sl-pick__opts button[aria-checked="true"]{color:var(--slate)}
.sl-pick__opts button:focus-visible{outline:3px solid var(--teal); outline-offset:1px}
.sl-pick__out{display:flex; align-items:baseline; justify-content:flex-end; gap:10px; margin:0; font-weight:600; font-size:.95rem; line-height:1.25; color:var(--ink-soft)}
.sl-pick__out b{font-family:var(--sl-head); font-weight:800; font-size:2.3rem; line-height:1; letter-spacing:-.04em; color:var(--teal); font-variant-numeric:tabular-nums}
.sl-pick__meter{position:absolute; left:0; right:0; bottom:0; height:5px; background:var(--sl-deep)}
.sl-pick__meter i{display:block; height:100%; background:var(--sl-grad); transform-origin:left; transition:transform .55s var(--ease)}
html:not(.js) .sl-pick{display:none}
.sl-grid{display:grid; grid-template-columns:repeat(3,minmax(0,1fr)); grid-auto-rows:auto; gap:var(--gap)}
.sl-card{position:relative; display:grid; grid-template-rows:subgrid; grid-row:span 5; row-gap:0; min-width:0; background:#fff; color:var(--slate); border:1px solid var(--sl-line); border-radius:var(--r-xl); box-shadow:var(--sl-shadow); text-decoration:none; overflow:hidden; isolation:isolate; transition:transform .28s var(--ease), box-shadow .28s var(--ease), border-color .28s var(--ease), opacity .35s var(--ease), filter .35s var(--ease)}
.sl-card::after{content:""; position:absolute; left:0; right:0; top:0; height:4px; background:var(--sl-grad); transform:scaleX(0); transform-origin:left; transition:transform .32s var(--ease)}
.sl-card:hover,.sl-card:focus-visible{transform:translateY(-4px); border-color:rgba(19,132,143,.42); box-shadow:var(--sl-shadow-hi)}
.sl-card:hover::after,.sl-card:focus-visible::after{transform:scaleX(1)}
.sl-card:focus-visible{outline:3px solid var(--teal); outline-offset:3px}
.sl-card__shot{position:relative; margin:12px 12px 0; border-radius:14px; overflow:hidden; aspect-ratio:345/232; background:var(--slate)}
.sl-card__shot img{width:100%; height:100%; object-fit:cover; object-position:50% var(--y,20%); transition:transform .6s var(--ease)}
.sl-card:hover .sl-card__shot img{transform:scale(1.035)}
.sl-time{position:absolute; right:10px; bottom:10px; display:inline-flex; align-items:center; gap:7px; padding:.42em .8em .42em .6em; border-radius:99px; background:#fff; color:var(--slate); font-family:var(--mono); font-weight:600; font-size:.76rem; letter-spacing:.05em; text-transform:uppercase; box-shadow:0 8px 18px -8px rgba(11,31,37,.7); transition:background .3s var(--ease)}
.sl-time svg{width:15px; height:15px; fill:none; stroke:currentColor; stroke-width:2.2; stroke-linecap:round; stroke-linejoin:round}
.sl-card__name{display:block; padding:18px var(--pad-card) 0}
.sl-card__name h3{font-size:1.42rem; line-height:1.1; margin:0; color:var(--logo-teal)}
.sl-card__name p{margin:4px 0 0; font-weight:700; font-size:.98rem; line-height:1.2; color:var(--teal)}
.sl-card__d{margin:0; padding:12px var(--pad-card) 0; font-size:.97rem; line-height:1.5; color:var(--ink-soft)}
.sl-facts{list-style:none; margin:0; padding:14px var(--pad-card) 0; display:grid; gap:7px; align-content:start}
.sl-facts li{position:relative; margin:0; padding-left:21px; font-size:.92rem; line-height:1.35; font-weight:600; color:var(--slate)}
.sl-facts li::before{content:""; position:absolute; left:0; top:.36em; width:11px; height:11px; border-radius:4px; background:var(--mint); box-shadow:inset 0 0 0 1.5px rgba(29,65,78,.2)}
.sl-card__go{display:flex; align-items:center; justify-content:space-between; gap:12px; margin-top:18px; padding:13px var(--pad-card) 15px; border-top:1px solid var(--sl-line); font-family:var(--sl-head); font-weight:800; font-size:1rem; letter-spacing:-.01em; color:var(--logo-teal)}
.sl-card__go i{display:grid; place-items:center; flex:none; width:36px; height:36px; border-radius:50%; background:var(--aqua); color:var(--logo-teal); font-style:normal; font-family:var(--body); font-weight:700; transition:background .25s var(--ease), transform .25s var(--ease)}
.sl-card:hover .sl-card__go i{background:var(--mint); transform:translate(2px,-2px)}
/* picker states */
.sl-card.is-out{opacity:.4; filter:saturate(.3); box-shadow:none}
.sl-card.is-out:hover,.sl-card.is-out:focus-visible{opacity:1; filter:none}
.sl-card.is-in{border-color:rgba(19,132,143,.5)}
.sl-card.is-in .sl-time{background:var(--mint)}
.sl-card.is-pop{animation:sl-pop .5s var(--ease) both; animation-delay:calc(var(--i) * 55ms)}
@keyframes sl-pop{0%{transform:scale(.965)} 55%{transform:scale(1.018)} 100%{transform:none}}
.sl-help{display:flex; flex-wrap:wrap; align-items:center; justify-content:space-between; gap:12px 28px; margin-top:var(--gap); padding:16px clamp(16px,2vw,24px); border-radius:var(--r-xl)}
.sl-help p{margin:0; flex:1 1 520px; font-size:.98rem; line-height:1.5}
.sl-help b{font-family:var(--sl-head); font-weight:800; letter-spacing:-.01em}
@media (max-width:1100px){ .sl-grid{grid-template-columns:repeat(2,minmax(0,1fr))} .sl-pick{grid-template-columns:minmax(0,1fr) auto} .sl-pick__opts{grid-column:1/-1; grid-row:2} .sl-pick__out{min-width:0} }
@media (max-width:680px){ .sl-grid{grid-template-columns:minmax(0,1fr)} .sl-card{grid-row:auto; display:flex; flex-direction:column} .sl-card__go{margin-top:auto} .sl-facts{padding-bottom:18px} .sl-tools .section-head .btn{display:none} }
@media (max-width:560px){ .sl-pick{grid-template-columns:minmax(0,1fr); padding-inline:14px} .sl-pick__out{justify-content:flex-start} .sl-pick__opts button{font-size:.92rem; padding:0 2px} .sl-pick__q{font-size:1.12rem} .sl-help .btn{width:100%} }

/* ---------- with a group ---------- */
.sl-room__g{display:grid; grid-template-columns:repeat(3,minmax(0,1fr)); gap:var(--gap)}
.sl-room__c{display:flex; flex-direction:column; min-width:0; padding:var(--pad-card); border-radius:var(--r-xl); background:rgba(255,255,255,.05); border:1px solid var(--line-dark); position:relative; overflow:hidden}
.sl-room__r{display:flex; flex-direction:column; flex:1}
.sl-room__r a{margin-top:auto}
.sl-room__c::before{content:""; position:absolute; left:0; right:0; top:0; height:4px; background:var(--sl-grad)}
.sl-room__top{display:flex; align-items:center; gap:13px; margin-bottom:16px}
.sl-room__c .sl-ico{background:rgba(209,254,255,.12); border-color:rgba(209,254,255,.3)}
.sl-room__c .sl-ico svg{stroke:var(--mint)}
.sl-room__top span:last-child{font-family:var(--mono); font-size:.74rem; letter-spacing:.1em; text-transform:uppercase; font-weight:600; color:var(--mint)}
.sl-room__c h3{font-size:1.38rem; line-height:1.14; color:#fff; margin:0 0 .55em}
.sl-room__c p{margin:0 0 20px; font-size:.98rem; line-height:1.55; color:rgba(255,255,255,.84)}
.sl-room__c a{display:inline-flex; align-items:center; gap:.45em; align-self:flex-start; font-family:var(--sl-head); font-weight:800; color:var(--mint)!important; text-decoration:none; padding:6px 0; min-height:44px}
.sl-room__c a span{transition:transform .2s var(--ease)}
.sl-room__c a:hover span{transform:translate(2px,-2px)}
@media (max-width:1100px){ .sl-room__g{grid-template-columns:minmax(0,1fr)} .sl-room__c{display:grid; grid-template-columns:minmax(0,5fr) minmax(0,7fr); column-gap:clamp(20px,4vw,48px); align-items:start} .sl-room__c h3{margin:0; font-size:1.5rem} .sl-room__r p{margin-bottom:10px} }
@media (max-width:680px){ .sl-room__c{display:flex} .sl-room__c h3{margin:0 0 .55em; font-size:1.38rem} }

/* ---------- Vibe Check band (shared component, Lab heading voice) ---------- */
.sl-page .fvb .fx-h{font-family:var(--sl-head); font-weight:800; letter-spacing:-.022em; text-transform:none}

/* ---------- final CTA ---------- */
.sl-cta{text-align:center}
.sl-cta__url{display:block; font-family:var(--sl-head); font-weight:800; font-size:clamp(1.55rem,5.5vw,4.9rem); line-height:.95; letter-spacing:-.045em; color:var(--slate); text-decoration:none; margin:0 0 .3em; overflow-wrap:anywhere}
.sl-cta__url i{font-style:normal; color:var(--teal)}
.sl-cta__url:hover{color:var(--logo-teal)}
.sl-cta p{margin:0; font-weight:600; font-size:var(--fs-lede)}
.sl-cta .btns{justify-content:center; margin-top:24px}
.sl-cta p.sl-cta__more{max-width:none; margin:clamp(26px,3vw,36px) 0 0; padding-top:clamp(20px,2.4vw,28px); border-top:1px solid rgba(29,65,78,.25); font-size:1.02rem; font-weight:500}
.sl-cta__more a{font-weight:700; color:var(--slate)}
'''

JS = r'''
(function(){
  var d = document, pick = d.querySelector('[data-sl-pick]'); if(!pick) return;
  var btns = [].slice.call(pick.querySelectorAll('[role="radio"]')), thumb = pick.querySelector('.sl-pick__thumb'),
      num = pick.querySelector('.sl-pick__out b'), txt = pick.querySelector('.sl-pick__out span'), meter = pick.querySelector('.sl-pick__meter i'),
      cards = [].slice.call(d.querySelectorAll('.sl-card')), shown = cards.length, tick;
  function count(to){ clearInterval(tick); var from = shown; shown = to; if(from === to){ num.textContent = to; return; } var v = from, step = to > from ? 1 : -1; tick = setInterval(function(){ v += step; num.textContent = v; if(v === to) clearInterval(tick); }, 70); }
  function set(i, focus){
    var t = +btns[i].getAttribute('data-t'), fit = 0, k = 0;
    btns.forEach(function(b, j){ b.setAttribute('aria-checked', String(j === i)); b.tabIndex = j === i ? 0 : -1; });
    if(focus) btns[i].focus();
    thumb.style.transform = 'translateX(' + (i * 100) + '%)';
    cards.forEach(function(c){
      var ok = !t || +c.getAttribute('data-min') <= t, lab = c.querySelector('.sl-time span'), under = +c.getAttribute('data-under') || 0;
      c.classList.remove('is-pop');
      c.classList.toggle('is-out', !ok); c.classList.toggle('is-in', !!t && ok);
      lab.textContent = (t && ok && under && t < under) ? c.getAttribute('data-note') : c.getAttribute('data-time');
      if(ok){ fit++; if(t){ c.style.setProperty('--i', k++); void c.offsetWidth; c.classList.add('is-pop'); } }
    });
    count(fit);
    txt.textContent = !t ? 'tools, whatever time you have' : 'of ' + cards.length + ' fit in ' + (t >= 10 ? '10 minutes or more' : t + ' minutes');
    meter.style.transform = 'scaleX(' + (fit / cards.length) + ')';
  }
  btns.forEach(function(b, i){
    b.addEventListener('click', function(){ set(i); });
    b.addEventListener('keydown', function(e){ var n = (e.key === 'ArrowRight' || e.key === 'ArrowDown') ? 1 : (e.key === 'ArrowLeft' || e.key === 'ArrowUp') ? -1 : 0; if(n){ e.preventDefault(); set((i + n + btns.length) % btns.length, true); } });
  });
  cards.forEach(function(c){ c.addEventListener('animationend', function(){ c.classList.remove('is-pop'); }); });
})();
'''


def card(t, i):
    full = t.get('full', t['n'])
    note = t.get('note')
    na = f' data-under="{note[0]}" data-note="{esc(note[1])}"' if note else ''
    facts = ''.join(f'<li>{esc(x)}</li>' for x in t['f'])
    return (f'<a class="sl-card" href="{SKILLS}{t["k"]}/" target="_blank" rel="noopener" data-min="{t["min"]}" data-time="{esc(t["time"])}"{na} '
            f'aria-label="Open {esc(full)} in a new tab. {esc(t["time"])}." aria-describedby="sl-d-{t["k"]}">'
            f'<div class="sl-card__shot" style="--y:{t["y"]}%">{img("sl-" + t["k"] + "-m", t["alt"], loading="eager" if i < 3 else "lazy")}'
            f'<span class="sl-time"><svg viewBox="0 0 24 24" aria-hidden="true">{I_CLOCK}</svg><span>{esc(t["time"])}</span></span></div>'
            f'<div class="sl-card__name"><h3>{esc(t["n"])}</h3><p>{esc(t["tag"])}</p></div>'
            f'<p class="sl-card__d" id="sl-d-{t["k"]}">{esc(t["d"])}</p>'
            f'<ul class="sl-facts">{facts}</ul>'
            f'<div class="sl-card__go">Open {esc(t["n"])}<i aria-hidden="true">&#8599;</i></div></a>')


def build():
    cards = ''.join(card(t, i) for i, t in enumerate(TOOLS))
    opts = ''.join(f'<button type="button" role="radio" aria-checked="{str(i == 0).lower()}" tabindex="{0 if i == 0 else -1}" data-t="{t}">{esc(lbl)}</button>'
                   for i, (t, lbl) in enumerate(PICKS))
    room = ''.join(f'<div class="sl-room__c"><div class="sl-room__l"><div class="sl-room__top">{ico(ic)}<span>{esc(tool)}</span></div><h3>{esc(h)}</h3></div>'
                   f'<div class="sl-room__r"><p>{esc(p)}</p><a href="{SKILLS}{path}" target="_blank" rel="noopener">Open {esc(tool)} <span aria-hidden="true">&#8599;</span></a></div></div>'
                   for tool, ic, h, p, path in ROOM)
    vibe = vibe_band('Vibe Check is a private, self-guided space for anyone wondering whether they, or a friend, may have caused harm. It walks through what accountability and repair can look like. Boundary Flags and Reset Kit are part of it.',
                     heading='A private place to think things through')

    body = f'''
<section class="sl-hero">
  <span class="wm-daisy" aria-hidden="true"></span>
  <div class="wrap">
    <div class="rise">
      <nav class="crumbs" aria-label="Breadcrumb"><a href="index.html">Home</a><span>/</span><a href="resources.html">Resources</a><span>/</span><span>BAE Skills Lab</span></nav>
      <h1><span class="sl-pre">Before Anyone Else</span> <span class="sl-lab"><span class="mk">Skills Lab</span></span></h1>
      <span class="sl-rule" aria-hidden="true"></span>
      <p class="lede">A collection of short, interactive tools about consent, boundaries, and what a healthy relationship actually looks like.</p>
      <div class="btns">{btn('Open the Skills Lab', SKILLS, 'teal')}{btn('See the six tools', '#tools', 'white', arrow=True)}</div>
      <div class="sl-facts-row"><span>Six tools</span><span>Under 2 to 30 minutes each</span><span>Free</span></div>
    </div>
    <div class="sl-stage">
      <a class="sl-pc sl-pc--board" href="{SKILLS}jeopardy/" target="_blank" rel="noopener" aria-label="Open SafeBAE Jeopardy in a new tab"><span class="sl-piece">{img('sl-jeopardy', '', loading='eager')}</span><span class="sl-tag">10–30 min</span></a>
      <a class="sl-pc sl-pc--p1" href="{SKILLS}boundary-flags/" target="_blank" rel="noopener" aria-label="Open Boundary Flags in a new tab"><span class="sl-piece">{img('sl-boundary-flags-m', '', loading='eager')}</span><span class="sl-tag">5 min</span></a>
      <a class="sl-pc sl-pc--p2" href="{SKILLS}supporting-a-survivor/" target="_blank" rel="noopener" aria-label="Open Supporting a Survivor: Helpful or Harmful? in a new tab"><span class="sl-piece">{img('sl-supporting-a-survivor-m', '', loading='eager')}</span><span class="sl-tag">3 min</span></a>
      <a class="sl-pc sl-pc--mark" href="{SKILLS}nutrition-label/" target="_blank" rel="noopener" aria-label="Open Partner Nutrition Label in a new tab"><span class="sl-piece">{img('sl-label', '', loading='eager')}</span><span class="sl-tag">3–8 min</span></a>
    </div>
  </div>
</section>

<section class="band sl-tools" id="tools">
  <div class="wrap">
    <div class="section-head"><div><h2>Pick a tool by the time you have</h2>
      <p class="lede lede--full muted">The shortest is a 30-second reset. The longest is a 25-question game show. Each one opens in a new tab.</p></div>
      {btn('Open the Skills Lab', SKILLS, 'slate')}</div>
    <div class="sl-pick" data-sl-pick>
      <p class="sl-pick__q" id="sl-pick-q">{ico(I_CLOCK)}How long do you have?</p>
      <div class="sl-pick__opts" role="radiogroup" aria-labelledby="sl-pick-q"><span class="sl-pick__thumb" aria-hidden="true"></span>{opts}</div>
      <p class="sl-pick__out" aria-live="polite"><b>6</b><span>tools, whatever time you have</span></p>
      <span class="sl-pick__meter" aria-hidden="true"><i></i></span>
    </div>
    <div class="sl-grid">{cards}</div>
    <div class="sl-help note note--coral"><p><b>Need to talk to someone now?</b> Reset Kit and Supporting a Survivor deal with hard moments. Text LOVEIS to 22522 or call 800-656-HOPE (4673). Both lines are free and confidential, 24/7.</p><button class="btn btn--slate" data-open-help>All hotlines</button></div>
  </div>
</section>

<section class="band band--slate sl-room" id="groups">
  <div class="wrap">
    <div class="section-head"><div><h2>Running one with a <span class="mk">group</span></h2>
      <p class="lede lede--full">Listen Closer and SafeBAE Jeopardy are played together, and Partner Nutrition Label can be printed for a whole room.</p></div>
      {btn('For educators', 'educators.html', 'ghost', arrow=True)}</div>
    <div class="sl-room__g">{room}</div>
  </div>
</section>

{vibe}

<section class="band band--mint">
  <div class="wrap sl-cta">
    <a class="sl-cta__url" href="{SKILLS}" target="_blank" rel="noopener">skills-lab<i>.safebae.org</i></a>
    <p>Six short tools about consent, boundaries, and what a healthy relationship actually looks like.</p>
    <div class="btns">{btn('Open the Skills Lab', SKILLS, 'slate')}{btn('Send feedback or a suggestion', FEEDBACK, 'ghost')}</div>
    <p class="sl-cta__more">Go deeper with the free, 16-module {a('Certified Peer Educator Training', 'peer-educator.html')}, or the Lab’s {a('FAQ', SKILLS + 'faq/')}: straight answers to the fifteen questions students ask SafeBAE most.</p>
  </div>
</section>
'''
    page('skills-lab.html', 'BAE Skills Lab · SafeBAE',
         'The BAE Skills Lab is SafeBAE’s collection of short, interactive tools about consent, boundaries, and what a healthy relationship actually looks like. Six tools, from under 2 minutes to 30.',
         body, active='resources', body_class='sl-page', head_extra=f'<style>{VIBE_CSS}{CSS}</style>', scripts=f'<script>{JS}</script>')


if __name__ == '__main__':
    build()
