from lib import *
from data import *

POSTERS_ZIP = 'https://www.safebae.org/wp-content/uploads/2025/08/Posters.zip'
USES = ['Personal learning', 'Classroom lesson', 'School assembly or presentation', 'Staff / teacher training', 'Parent resource', 'Community program or event (non-school)']

def lib_item(i):
    return next(x for x in LIB if x['id'] == i)

# ---------------------------------------------------------------------------
# Film-page system (2.0).
# Every film page lives in its own visual world, but the parts they share
# (hero grammar, "Before you begin" + help line, teaching-guide band, related
# films, Vibe Check band) are one component set. Each page passes its palette
# and display face in through --f-* tokens on .film--<key>.
# ---------------------------------------------------------------------------

BEGIN_ITEMS = [
    ('Tell your counselors first', 'Let school counselors know before you teach this content and ask them to be available for students who may need support.'),
    ('Make it okay to step out', 'Let students know they can take a break or step out if the material feels overwhelming.'),
    ('Be clear about reporting', 'School staff are typically mandated reporters. Explain your school’s policies and state laws so students understand the limits of confidentiality before they share.'),
]

def film_crumbs(title):
    """Breadcrumb for every film page: Home / Resources / Library / <title>."""
    return ('<nav class="crumbs" aria-label="Breadcrumb"><a href="index.html">Home</a><span>/</span>'
            '<a href="resources.html">Resources</a><span>/</span><a href="library.html">Library</a><span>/</span>'
            f'<span>{esc(title)}</span></nav>')

def guide_panel(fid, cls='', title='Get the teaching guide', blurb=None):
    it = lib_item(fid); g = it['guide']

    blurb = blurb or 'Discussion prompts with brief answers, activities, facilitation tips and printable posters, ready to use in a classroom, club meeting or training.'
    stk = f'<span class="sticker">Free &middot; {g["pages"]} pages</span>' if g.get('pages') else '<span class="sticker">Free</span>'
    return f'''<section class="band gpanel {cls}" id="guide">
  <div class="wrap gpanel__grid">
    <div class="gpanel__cover">{img(g['cover'], 'Cover of the ' + it['title'] + ' teaching guide')}{stk}</div>
    <div class="gpanel__txt">
      <p class="eyebrow">Teaching guide &middot; PDF</p>
      <h2 class="fx-h">{esc(title)}</h2>
      <p class="lede">{esc(blurb)}</p>
      <div class="btns">{btn('Download the guide (PDF)', g['pdf'], 'mint')}{btn('Posters (.zip)', POSTERS_ZIP, 'ghost')}</div>
      <p class="gpanel__note">Used this guide with students? {a('Tell us how it went', GUIDE_SURVEY, 'link')} in a two-minute survey. It helps SafeBAE improve its guides.</p>
    </div>
  </div>
</section>'''

def begin_card(items=None, help_extra='', help_title='Share these 24/7, confidential resources with students'):
    """The shared prep checklist with the help line attached as its footer strip."""
    items = items or BEGIN_ITEMS
    lis = ''.join(f'<li><span class="fprep__tick" aria-hidden="true"></span><b>{esc(t)}</b><p>{esc(d)}</p></li>' for t, d in items)
    return f'''<div class="fprep"><ul class="fprep__list">{lis}</ul>
<div class="fprep__help"><div><b>{help_title}</b><span>love is respect: text LOVEIS to 22522 &middot; chat at loveisrespect.org &middot; call 1-866-331-9474</span>{help_extra}</div><button class="btn btn--slate btn--sm" type="button" data-open-help>All hotlines</button></div></div>'''

def begin(cls, lede, items=None, help_extra='', heading='Before you begin'):
    return f'''<section class="{cls} fbegin" id="begin"><div class="wrap">
<div class="fhead"><h2 class="fx-h">{esc(heading)}</h2><p class="lede">{lede}</p></div>
{begin_card(items, help_extra)}
</div></section>'''

def help_card(help_extra='', title='Free, confidential support, 24/7'):
    """Help line on its own, in the same strip style, for pages without a classroom checklist."""
    return f'''<div class="fprep fprep--solo"><div class="fprep__help"><div><b>{title}</b><span>love is respect: text LOVEIS to 22522 &middot; chat at loveisrespect.org &middot; call 1-866-331-9474</span>{help_extra}</div><button class="btn btn--slate btn--sm" type="button" data-open-help>All hotlines</button></div></div>'''

def frelated(ids, cls, heading='Teach these next', lede=''):
    cards = []
    for i in ids:
        it = lib_item(i)
        go = 'Open the series' if it['kind'] == 'series' else 'Watch and teach'
        cards.append(f'<a class="fcard" href="{it["href"]}"><span class="fcard__media">{img(it["thumb"], "")}</span><span class="fcard__body"><span class="fcard__sub">{esc(it["sub"])}</span><b class="fcard__t">{esc(it["title"])}</b><span class="fcard__d">{esc(it["desc"])}</span><span class="fcard__go">{go}<i aria-hidden="true">&rarr;</i></span></span></a>')
    lp = f'<p class="lede">{lede}</p>' if lede else ''
    return f'''<section class="{cls} frel"><div class="wrap"><div class="fhead"><h2 class="fx-h">{esc(heading)}</h2>{lp}</div><div class="frel__grid frel__grid--n{len(cards)}">{''.join(cards)}</div></div></section>'''

def tail(fid, rel_ids, rel_cls, rel_heading='Teach these next'):
    """Teaching-guide band followed by related films: the same close on every film page."""
    return guide_panel(fid) + '\n' + frelated(rel_ids, rel_cls, rel_heading)

# ---------------------------------------------------------------------------
# v4: "Teach it". The teaching guide, the facilitator notes ("Before you begin" + the help line)
# and, on pages that have them, the campaign posters, in one section. It takes the page's own
# surfaces through the --f-* tokens, so each film keeps its look to the end of the page.
# id="guide" sits on the section (hero buttons link there); id="begin" stays on the notes card.
# ---------------------------------------------------------------------------
BEGIN_LEDE = 'These conversations can surface strong emotions and may lead to disclosures of abuse.'

def teach(fid, cls, lede=BEGIN_LEDE, items=None, help_extra='', posters=None, title='Teach it', blurb=None, btn_kind='mint', deco=''):
    """posters: optional (heading, gallery_html) — the page's own poster wall, shown under the guide.
    deco: optional decorative markup placed first in the section (the page positions it)."""
    it = lib_item(fid); g = it['guide']
    items = items or BEGIN_ITEMS
    pages = f'{g["pages"]}-page ' if g.get('pages') else ''
    blurb = blurb or f'The free {pages}teaching guide has discussion prompts with brief answers, activities, facilitation tips and printable posters, ready to use in a classroom, club meeting or training.'
    stk = f'<span class="sticker">Free &middot; {g["pages"]} pages</span>' if g.get('pages') else '<span class="sticker">Free</span>'
    lis = ''.join(f'<li><span class="teach__tick" aria-hidden="true"></span><b>{esc(t)}</b><p>{esc(d)}</p></li>' for t, d in items)
    btns = btn('Download the guide (PDF)', g['pdf'], btn_kind)
    wall = ''
    if posters:
        ph, ghtml = posters
        wall = (f'<div class="teach__posters"><div class="teach__posters-h"><h3 class="fx-h">{esc(ph)}</h3>'
                f'{btn("Download all posters (.zip)", POSTERS_ZIP, "ghost", "sm")}</div>{ghtml}</div>')
    else:
        btns += btn('Posters (.zip)', POSTERS_ZIP, 'ghost')
    return f'''<section class="{cls} teach" id="guide">{deco}
  <div class="wrap">
    <div class="teach__g">
      <div class="teach__cover"><span class="teach__pic">{img(g['cover'], 'Cover of the ' + it['title'] + ' teaching guide')}</span>{stk}</div>
      <div class="teach__main">
        <p class="eyebrow">Teaching guide &middot; PDF</p>
        <h2 class="fx-h">{esc(title)}</h2>
        <p class="lede teach__lede">{esc(blurb)}</p>
        <div class="btns teach__btns">{btns}</div>
        <p class="teach__note">Used this guide with students? {a('Tell us how it went', GUIDE_SURVEY, 'link')} in a two-minute survey. It helps SafeBAE improve its guides.</p>
      </div>
      <div class="teach__prep" id="begin">
        <div class="teach__ph"><h3 class="fx-h">Before you begin</h3><p>{lede}</p></div>
        <ul class="teach__list">{lis}</ul>
        <div class="teach__help"><div><b>Share these 24/7, confidential resources with students</b><span>love is respect: text LOVEIS to 22522 &middot; chat at loveisrespect.org &middot; call 1-866-331-9474</span>{help_extra}</div><button class="btn btn--slate btn--sm" type="button" data-open-help>All hotlines</button></div>
      </div>
    </div>
    {wall}
  </div>
</section>'''

def teach_tail(fid, cls, rel_ids, rel_cls, rel_heading='Teach these next', **kw):
    """The v4 close on every film page: Teach it, then Teach these next."""
    return teach(fid, cls, **kw) + '\n' + frelated(rel_ids, rel_cls, rel_heading)

TEACH_CSS = '''
.teach__g{--tc-w:clamp(200px,19vw,248px); display:grid; grid-template-columns:var(--tc-w) minmax(0,1fr); gap:clamp(36px,4.4vw,60px) clamp(36px,5vw,76px); align-items:stretch}
.teach__cover{position:relative; min-width:0; min-height:calc(var(--tc-w) * 1.3); margin:2px 6px 8px 0}
.teach__cover::before{content:""; position:absolute; inset:0; border-radius:8px; background:color-mix(in srgb, var(--f-acc) 32%, transparent); transform:translate(14px,6px) rotate(4deg)}
.teach__pic{position:absolute; inset:0; display:block; border-radius:8px; overflow:hidden; background:#fff; box-shadow:0 30px 60px -22px rgba(0,0,0,.6); transform:rotate(-3deg); transition:transform .5s var(--ease)}
.teach__pic img{width:100%; height:100%; object-fit:cover; object-position:50% 0}
.teach__cover:hover .teach__pic{transform:rotate(-1deg) translateY(-4px)}
.teach__cover .sticker{position:absolute; right:-18px; bottom:20px; z-index:1; transform:rotate(5deg); white-space:nowrap}
.teach__main{display:flex; flex-direction:column; align-items:flex-start; justify-content:center; min-width:0}
.teach__main > .eyebrow{margin:0 0 .9rem}
.teach__main > h2{margin:0 0 .42em}
.teach__lede{margin:0 0 1.1em; color:var(--f-ink)}
.teach__btns{gap:10px}
.teach__note{margin:14px 0 0; font-size:.95rem; line-height:1.5; color:var(--f-ink2)}
.teach__note a{color:var(--f-lab); font-weight:700}
.teach__prep{grid-column:1 / -1; border-radius:var(--f-r); border:var(--f-bw) solid var(--f-line); background:var(--f-card); color:var(--f-ink); overflow:hidden; box-shadow:var(--shadow-soft)}
.teach__ph{display:flex; flex-wrap:wrap; align-items:baseline; gap:6px 22px; padding:clamp(20px,2.3vw,28px) clamp(20px,2.4vw,28px) clamp(16px,1.6vw,20px); border-bottom:1px solid var(--f-line)}
.teach__ph h3{margin:0; font-size:clamp(1.35rem,2vw,1.7rem); line-height:1.1; color:var(--f-ink)}
.teach__ph p{margin:0; flex:1 1 320px; font-size:.98rem; line-height:1.5; color:var(--f-ink2)}
.teach__list{list-style:none; margin:0; padding:0; display:grid; grid-template-columns:repeat(3,minmax(0,1fr))}
.teach__list li{margin:0; padding:clamp(20px,2.4vw,28px); display:grid; grid-template-columns:30px minmax(0,1fr); gap:6px 14px; align-content:start}
.teach__list li + li{border-left:1px solid var(--f-line)}
.teach__tick{grid-row:span 2; width:30px; height:30px; border-radius:9px; background:var(--f-acc); display:grid; place-items:center}
.teach__tick::after{content:""; width:7px; height:13px; border:solid var(--f-acc-ink); border-width:0 3px 3px 0; transform:translateY(-2px) rotate(45deg)}
.teach__list b{font-family:var(--display); font-stretch:106%; font-weight:800; font-size:1.06rem; line-height:1.25; padding-top:5px}
.teach__list p{margin:0; font-size:.95rem; line-height:1.55; color:var(--f-ink2)}
.teach__help{display:flex; gap:12px 24px; align-items:center; justify-content:space-between; flex-wrap:wrap; padding:16px clamp(20px,2.4vw,28px); background:var(--coral); color:var(--slate)}
.teach__help > div{min-width:0; flex:1 1 380px}
.teach__help b{display:block; font-family:var(--display); font-stretch:106%; font-size:1rem; line-height:1.3}
.teach__help span{display:block; font-weight:700; font-size:.95rem; line-height:1.45}
.teach__posters{margin-top:clamp(48px,5.6vw,76px)}
.teach__posters-h{display:flex; align-items:center; justify-content:space-between; gap:12px 32px; flex-wrap:wrap; margin-bottom:clamp(18px,2.2vw,28px)}
.teach__posters-h h3{margin:0; font-size:clamp(1.5rem,2.7vw,2.2rem); line-height:1.05}
@media (max-width:860px){
  .teach__list{grid-template-columns:minmax(0,1fr)}
  .teach__list li + li{border-left:0; border-top:1px solid var(--f-line)}
}
@media (max-width:760px){
  .teach__g{--tc-w:96px; gap:0 22px; align-items:center}
  .teach__main{display:contents}
  .teach__cover{grid-row:1 / span 2; min-height:0; aspect-ratio:587/917; margin:0 8px 0 0; align-self:center}
  .teach__cover::before{transform:translate(7px,4px) rotate(4deg)}
  .teach__cover .sticker{display:none}
  .teach__main > .eyebrow{grid-column:2; align-self:end; margin:0 0 .5rem}
  .teach__main > h2{grid-column:2; align-self:start; margin:0}
  .teach__lede, .teach__btns, .teach__note, .teach__prep{grid-column:1 / -1}
  .teach__lede{margin-top:24px}
  .teach__btns .btn{flex:1 1 auto}
  .teach__note{margin-bottom:30px}
}
'''

FILM_CSS = '''
.film{--f-card:#fff; --f-line:var(--line); --f-ink:var(--slate); --f-ink2:var(--ink-soft); --f-acc:var(--teal); --f-acc-ink:#fff; --f-lab:var(--logo-teal); --f-r:var(--r-xl); --f-bw:1px; --f-disp:var(--display); --f-dw:800; --f-dt:none; --f-dl:-.01em; --f-ds:112%}
.fx-h{font-family:var(--f-disp); font-weight:var(--f-dw); text-transform:var(--f-dt); letter-spacing:var(--f-dl); font-stretch:var(--f-ds)}
/* film stills in the players stay in their original colour */
.film .vid img{opacity:1}
.film .vid:hover img{opacity:.8}
/* hero grammar for the custom film heroes */
.fhero{position:relative; overflow:hidden; isolation:isolate}
.fhero > .wrap{position:relative; z-index:1}
.fhero--dark .mk{background:none; color:var(--mint)}
.fhero--light .wm-daisy{color:var(--logo-teal)}
.fhero--dark .eyebrow{color:var(--mint)}
.fhero--light .eyebrow{color:var(--logo-teal)}
/* section heads inside shared parts */
.fhead{margin-bottom:clamp(20px,2.6vw,34px)}
.fhead h2{margin:0}
.fhead .lede{margin:.5em 0 0; color:var(--f-ink2)}
/* Before you begin + help line: one unit */
.fprep{border-radius:var(--f-r); border:var(--f-bw) solid var(--f-line); background:var(--f-card); color:var(--f-ink); overflow:hidden; box-shadow:var(--shadow-soft)}
.fprep__list{list-style:none; margin:0; padding:0; display:grid; grid-template-columns:repeat(3,minmax(0,1fr))}
.fprep__list li{margin:0; padding:clamp(20px,2.4vw,28px); display:grid; grid-template-columns:32px minmax(0,1fr); gap:6px 14px; align-content:start}
.fprep__list li + li{border-left:1px solid var(--f-line)}
.fprep__tick{grid-row:span 2; width:32px; height:32px; border-radius:10px; background:var(--f-acc); display:grid; place-items:center}
.fprep__tick::after{content:""; width:8px; height:14px; border:solid var(--f-acc-ink); border-width:0 3px 3px 0; transform:translateY(-2px) rotate(45deg)}
.fprep__list b{font-family:var(--display); font-stretch:106%; font-size:1.08rem; line-height:1.25; padding-top:5px}
.fprep__list p{margin:0; font-size:.95rem; line-height:1.55; color:var(--f-ink2)}
.fprep__help{display:flex; gap:14px 28px; align-items:center; justify-content:space-between; flex-wrap:wrap; padding:18px clamp(20px,2.4vw,28px); background:var(--coral); color:var(--slate)}
.fprep__help > div{min-width:0; flex:1 1 420px}
.fprep__help b{display:block; font-family:var(--display); font-stretch:106%; font-size:1.02rem}
.fprep__help span{display:block; font-weight:700; font-size:.96rem; line-height:1.45}
.fprep--solo{box-shadow:none}
@media (max-width:860px){.fprep__list{grid-template-columns:minmax(0,1fr)} .fprep__list li + li{border-left:0; border-top:1px solid var(--f-line)}}
/* teaching-guide band: Logo Teal on every film page. The cover takes the height of the text beside it, so the two end together. */
.gpanel{background:var(--logo-teal) var(--grain); color:#fff; overflow:hidden}
.gpanel__grid{--gp-w:clamp(190px,18vw,232px); display:grid; grid-template-columns:var(--gp-w) minmax(0,1fr); gap:clamp(32px,5vw,76px); align-items:stretch}
.gpanel__cover{position:relative; min-height:calc(var(--gp-w) * 1.3)}
.gpanel__cover::before{content:""; position:absolute; inset:0; border-radius:8px; background:rgba(209,254,255,.14); border:1px solid rgba(209,254,255,.2); transform:translate(14px,6px) rotate(4deg)}
.gpanel__cover img{position:absolute; inset:0; width:100%; height:100%; object-fit:cover; object-position:50% 0; border-radius:8px; box-shadow:0 30px 60px -22px rgba(0,0,0,.6); transform:rotate(-3deg); transition:transform .5s var(--ease)}
.gpanel__cover:hover img{transform:rotate(-1deg) translateY(-4px)}
.gpanel__cover .sticker{position:absolute; right:-16px; bottom:18px; transform:rotate(5deg); z-index:1; white-space:nowrap}
.gpanel__txt{display:flex; flex-direction:column; align-items:flex-start; min-width:0}
.gpanel h2{color:#fff; margin:0 0 .35em}
.gpanel .eyebrow{color:var(--mint)}
.gpanel .lede{color:#fff; margin:0 0 1.1em}
.gpanel .btns{margin-top:auto}
.gpanel .btn--ghost{color:#fff}
.gpanel__note{margin:16px 0 0; font-size:.95rem; line-height:1.5; color:#fff}
.gpanel__note a{color:var(--mint)}
@media (max-width:760px){
  .gpanel__grid{--gp-w:104px; grid-template-columns:var(--gp-w) minmax(0,1fr); gap:0 22px; align-items:center}
  .gpanel__txt{display:contents}
  .gpanel__cover{grid-row:1 / span 2; min-height:0; aspect-ratio:587/917; align-self:center}
  .gpanel__cover::before{transform:translate(7px,4px) rotate(4deg)}
  .gpanel__cover .sticker{display:none}
  .gpanel .eyebrow{grid-column:2; align-self:end; margin:0 0 .5rem}
  .gpanel h2{grid-column:2; align-self:start; margin:0}
  .gpanel .lede, .gpanel .btns, .gpanel__note{grid-column:1 / -1}
  .gpanel .lede{margin-top:26px}
  .gpanel .btns{margin-top:0}
  .gpanel .btns .btn{flex:1 1 auto}
}
/* related films: one card anatomy, parts line up across the row (media, label, title, text, action) */
.frel__grid{display:grid; grid-template-columns:repeat(3,minmax(0,1fr)); gap:var(--gap)}
.frel__grid--n2{grid-template-columns:repeat(2,minmax(0,1fr))}
.frel__grid--n4{grid-template-columns:repeat(4,minmax(0,1fr))}
.fcard{display:flex; flex-direction:column; min-width:0; border-radius:var(--f-r); border:var(--f-bw) solid var(--f-line); background:var(--f-card); color:var(--f-ink); overflow:hidden; text-decoration:none; transition:transform .25s var(--ease), box-shadow .25s var(--ease), border-color .25s}
.fcard:hover{transform:translateY(-4px); box-shadow:var(--shadow-soft); border-color:var(--f-acc)}
.fcard:focus-visible{outline-offset:4px}
.fcard__media{display:block; aspect-ratio:16/9; overflow:hidden; background:#000}
.fcard__media img{width:100%; height:100%; object-fit:cover; transition:transform .6s var(--ease)}
.fcard:hover .fcard__media img{transform:scale(1.04)}
.fcard__body{display:flex; flex-direction:column; gap:8px; flex:1; padding:20px 22px 22px}
.fcard__sub{font-family:var(--mono); font-size:.72rem; line-height:1.5; letter-spacing:.08em; text-transform:uppercase; font-weight:600; color:var(--f-lab)}
.fcard__t{display:block; font-family:var(--display); font-stretch:106%; font-weight:800; font-size:1.3rem; line-height:1.15; text-wrap:balance}
.fcard__d{font-size:.95rem; line-height:1.55; color:var(--f-ink2); display:-webkit-box; -webkit-line-clamp:3; -webkit-box-orient:vertical; overflow:hidden}
.fcard__go{display:inline-flex; gap:.45em; align-items:center; margin-top:auto; padding-top:8px; font-weight:800; font-size:.95rem; color:var(--f-lab)}
.fcard__go i{font-style:normal; transition:transform .2s var(--ease)}
.fcard:hover .fcard__go i{transform:translateX(4px)}
@supports (grid-template-rows:subgrid){ @media (min-width:861px){
  .fcard{display:grid; grid-template-rows:subgrid; grid-row:span 5; row-gap:0}
  .fcard__body{display:grid; grid-template-rows:subgrid; grid-row:span 4; row-gap:8px; align-content:start}
  .fcard__go{margin-top:0; align-self:end}
}}
@media (max-width:1080px){.frel__grid--n4{grid-template-columns:repeat(2,minmax(0,1fr))}}
@media (max-width:860px){.frel__grid, .frel__grid--n2, .frel__grid--n4{grid-template-columns:minmax(0,1fr)} .fcard{display:grid; grid-template-columns:minmax(0,.42fr) minmax(0,1fr)} .fcard__media{aspect-ratio:auto; height:100%; min-height:128px} .fcard__d{display:none} .fcard__body{padding:16px 18px; gap:6px} .fcard__t{font-size:1.15rem}}
@media (max-width:420px){.fcard{grid-template-columns:minmax(0,1fr)} .fcard__media{aspect-ratio:16/9; min-height:0}}
'''

# legacy helpers (still imported by other modules; keep their output unchanged)
GPANEL_CSS = '''
.before{display:grid; grid-template-columns:repeat(3,minmax(0,1fr)); gap:14px}
.before > div{border-radius:14px; padding:18px; background:var(--b-bg, #fff); border:1px solid var(--b-line, var(--line))}
.before b{display:block; font-family:var(--display); font-stretch:106%; margin-bottom:6px}
.before p{margin:0; font-size:.93rem; opacity:.85}
@media (max-width:860px){.before{grid-template-columns:1fr}}
.qa details{border-top:1px solid var(--qa-line, var(--line))}
.qa details:last-child{border-bottom:1px solid var(--qa-line, var(--line))}
.qa summary{list-style:none; cursor:pointer; padding:16px 44px 16px 0; position:relative; font-weight:700; font-size:1.06rem; line-height:1.35}
.qa summary::-webkit-details-marker{display:none}
.qa summary::after{content:"Answer"; position:absolute; right:0; top:16px; font-family:var(--mono); font-size:.68rem; letter-spacing:.08em; text-transform:uppercase; opacity:.7}
.qa details[open] summary::after{content:"Hide"}
.qa .ans{padding:0 0 18px; opacity:.9}
.qa .ans p{margin:0}
.qa .q-only summary::after{content:""}
.related{display:grid; grid-template-columns:repeat(3,minmax(0,1fr)); gap:16px}
@media (max-width:860px){.related{grid-template-columns:1fr}}
'''

def before_you_begin(extra=None):
    items = extra or BEGIN_ITEMS
    return '<div class="before">' + ''.join(f'<div><b>{esc(t)}</b><p>{esc(d)}</p></div>' for t, d in items) + '</div>'

def qa(pairs, cls='qa'):
    out = []
    for q, a_ in pairs:
        if a_:
            out.append(f'<details><summary>{esc(q)}</summary><div class="ans"><p>{esc(a_)}</p></div></details>')
        else:
            out.append(f'<details class="q-only" open><summary>{esc(q)}</summary></details>')
    return f'<div class="{cls}">' + ''.join(out) + '</div>'

def prompts(qs):
    return '<ul class="prompts">' + ''.join(f'<li>{esc(q)}</li>' for q in qs) + '</ul>'

def related(ids, cls=''):
    cards = []
    for i in ids:
        it = lib_item(i)
        cards.append(f'<a class="card {cls}" href="{it["href"]}"><div class="card__media">{img(it["thumb"], "")}</div><div class="card__body"><span class="chip" style="align-self:flex-start">Film + guide</span><h3>{esc(it["title"])}</h3><p>{esc(it["desc"][:150].rsplit(" ",1)[0])}…</p></div></a>')
    return '<div class="related">' + ''.join(cards) + '</div>'

def vibe_band(lede, heading='Worried you crossed a line?'):
    """Full teal Vibe Check band for film pages (Drew wants Vibe Check featured as a full band)."""
    qs = ['Did I harm someone?', 'Was that consent?', 'Did I cross a boundary?']
    return f'''<section class="band band--teal fvb">
<div class="wrap fvb__g"><div><p class="fvb__mark">{daisy()}Vibe Check by SafeBAE</p><h2 class="fx-h">{esc(heading)}</h2><p class="lede">{esc(lede)}</p>
<div class="btns">{btn('Open Vibe Check', 'https://checkyourvibe.org/', 'mint')}{btn('How it works', 'vibe-check.html', 'white', arrow=True)}</div>
<div class="fvb__chips"><span>Anonymous</span><span>No account</span><span>Nothing stored</span></div></div>
<div class="fvb__art"><div class="fvb__ph">{img('vc-screen', 'The Vibe Check home screen on a phone')}</div>{''.join(f'<span class="fvb__q fvb__q--{i}">{esc(q)}</span>' for i, q in enumerate(qs))}</div></div></section>'''

VIBE_CSS = '''
.fvb{position:relative; overflow:hidden}
.fvb__g{display:grid; grid-template-columns:minmax(0,1.2fr) minmax(0,.8fr); gap:clamp(24px,5vw,64px); align-items:center}
.fvb__mark{display:flex; align-items:center; gap:10px; font-family:var(--display); font-weight:900; font-stretch:115%; font-size:1.05rem; color:#fff; margin:0 0 14px}
.fvb__mark .daisy{width:32px; height:32px; color:var(--mint)}
.fvb h2{color:#fff; margin:0 0 .35em}
.fvb .lede{color:#fff}
.fvb__art{position:relative; padding:12px 0}
.fvb__ph{width:min(240px,62vw); margin-inline:auto; aspect-ratio:390/800; border-radius:38px; border:9px solid #0b1f25; background:#0b1f25; overflow:hidden; transform:rotate(-4deg); box-shadow:0 40px 80px -30px rgba(0,0,0,.6)}
.fvb__ph img{width:100%; height:100%; object-fit:cover; object-position:top}
.fvb__q{position:absolute; font-family:var(--display); font-stretch:106%; font-weight:800; font-size:.95rem; line-height:1.2; padding:10px 14px; border-radius:16px 16px 16px 4px; background:#fff; color:var(--slate); box-shadow:0 18px 30px -18px rgba(0,0,0,.6); white-space:nowrap}
.fvb__q--0{left:2%; top:16%; transform:rotate(-3deg)}
.fvb__q--1{right:0; top:44%; background:var(--mint); border-radius:16px 16px 4px 16px; transform:rotate(2deg)}
.fvb__q--2{left:6%; bottom:14%; transform:rotate(-1deg)}
.fvb__chips{display:flex; flex-wrap:wrap; gap:8px; margin-top:18px}
.fvb__chips span{font-family:var(--mono); font-size:.7rem; letter-spacing:.08em; text-transform:uppercase; font-weight:600; padding:5px 9px; border-radius:6px; background:var(--slate-deep); color:#fff}
@media (max-width:760px){.fvb__g{grid-template-columns:minmax(0,1fr)} .fvb__ph{width:min(200px,52vw)} .fvb__q{font-size:.82rem; padding:8px 11px} .fvb__q--0{left:0} .fvb__q--2{left:2%}}
'''

def help_inline(extra='', title='Share these 24/7, confidential resources with students'):
    return f'''<div class="helpline"><div><b>{title}</b><span>love is respect: text LOVEIS to 22522 &middot; chat at loveisrespect.org &middot; call 1-866-331-9474</span>{extra}</div><button class="btn btn--coral btn--sm" data-open-help>All hotlines</button></div>'''

HELPLINE_CSS = '''.helpline{display:flex; gap:16px 28px; align-items:center; justify-content:space-between; flex-wrap:wrap; padding:18px 22px; border-radius:14px; background:var(--coral); color:var(--slate)}
.helpline b{display:block; font-family:var(--display); font-stretch:106%}
.helpline span{display:block; font-size:.98rem; font-weight:700}
.prompts{list-style:none; padding:0; margin:0; display:grid; gap:10px}
.prompts li{padding:14px 16px; border-radius:12px; background:var(--p-bg, rgba(255,255,255,.06)); border:1px solid var(--p-line, rgba(255,255,255,.14)); font-weight:600; margin:0}
'''

GUIDE_JS = r'''<script>
document.querySelectorAll('form[data-guide]').forEach(function(f){ f.addEventListener('submit', function(e){ e.preventDefault(); var s = f.querySelector('select'); if(!s.value){ s.focus(); s.reportValidity && s.reportValidity(); return; } try{ localStorage.setItem('sb-guide-use', s.value); }catch(err){} var a = document.createElement('a'); a.href = f.dataset.guide; a.target = '_blank'; a.rel = 'noopener'; document.body.appendChild(a); a.click(); a.remove(); f.querySelector('.gform__note').textContent = 'Thank you. The guide is opening in a new tab.'; }); });
</script>'''

# Breadcrumb used by every film hero: Home / Resources / Library / <title>. film_page() upgrades the older
# two-step crumb ("Home / Library / ...") wherever a film module still writes it by hand.
_CRUMB_OLD = '<a href="index.html">Home</a><span>/</span><a href="library.html">Library</a>'
_CRUMB_NEW = '<a href="index.html">Home</a><span>/</span><a href="resources.html">Resources</a><span>/</span><a href="library.html">Library</a>'

def film_page(slug, title, desc, body, key, fonts, css, js=''):
    body = body.replace(_CRUMB_OLD, _CRUMB_NEW)
    page(slug, title + ' · SafeBAE', desc, body, active='resources', body_class=f'film film--{key}', fonts=fonts,
         head_extra=f'<style>{FILM_CSS}{TEACH_CSS}{GPANEL_CSS}{VIBE_CSS}{HELPLINE_CSS}{css}</style>', scripts=GUIDE_JS + js)
