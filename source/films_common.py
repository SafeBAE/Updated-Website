from lib import *
from data import *

POSTERS_ZIP = 'https://www.safebae.org/wp-content/uploads/2025/08/Posters.zip'
USES = ['Personal learning', 'Classroom lesson', 'School assembly or presentation', 'Staff / teacher training', 'Parent resource', 'Community program or event (non-school)']

def lib_item(i):
    return next(x for x in LIB if x['id'] == i)

def guide_panel(fid, cls='', title='Get the teaching guide', blurb=None):
    it = lib_item(fid); g = it['guide']
    pages = f'{g["pages"]} pages · PDF' if g.get('pages') else 'PDF'
    blurb = blurb or 'Discussion prompts with brief answers, activities, facilitation tips and printable posters, ready to use in a classroom, club meeting or training.'
    return f'''<section class="band gpanel {cls}" id="guide">
  <div class="wrap gpanel__grid">
    <div class="gpanel__cover">{img(g['cover'], 'Cover of the ' + it['title'] + ' teaching guide')}</div>
    <div>
      <p class="eyebrow">Free teaching guide &middot; {pages}</p>
      <h2>{esc(title)}</h2>
      <p class="lede">{esc(blurb)}</p>
      <div class="btns" style="margin-top:6px">{btn('Download the guide (PDF)', g['pdf'], 'mint')}{btn('Posters (.zip)', POSTERS_ZIP, 'ghost')}</div>
      <p class="small gform__note">Used this guide with students? {a('Tell us how it went', GUIDE_SURVEY, 'link')} in a two-minute survey. It helps SafeBAE improve its guides.</p>
    </div>
  </div>
</section>'''

GPANEL_CSS = '''
.gpanel{background:var(--g-bg, var(--slate)); color:var(--g-ink, #fff)}
.gpanel__grid{display:grid; grid-template-columns:minmax(0,.55fr) minmax(0,1.45fr); gap:clamp(24px,4vw,64px); align-items:center}
.gpanel__cover img{width:100%; max-width:320px; border-radius:8px; box-shadow:0 30px 60px -20px rgba(0,0,0,.6); transform:rotate(-3deg)}
.gpanel .lede{color:inherit; opacity:.92}
.gpanel .eyebrow{color:var(--mint)}
.gpanel .gform__note{margin-top:16px; opacity:.85}
.gpanel .gform__note a{color:var(--mint)}
.gform{background:rgba(255,255,255,.08); border:1px solid rgba(255,255,255,.18); border-radius:14px; padding:18px; max-width:640px}
.gform label{font-weight:700; display:block; margin-bottom:8px}
.gform__row{display:flex; gap:10px; flex-wrap:wrap}
.gform select{flex:1 1 240px; min-width:0; max-width:100%; font:inherit; padding:12px; border-radius:8px; border:2px solid transparent; background:#fff; color:var(--slate)}
.gform__note{margin:10px 0 0; opacity:.75}
@media (max-width:760px){.gpanel__grid{grid-template-columns:minmax(0,1fr)} .gpanel__cover img{max-width:200px}}
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
    items = [
        ('Tell your counselors first', 'Let school counselors know before you teach this content and ask them to be available for students who may need support.'),
        ('Make it okay to step out', 'Let students know they can take a break or step out if the material feels overwhelming.'),
        ('Be clear about reporting', 'School staff are typically mandated reporters. Explain your school’s policies and state laws so students understand the limits of confidentiality before they share.'),
    ]
    if extra: items = extra
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
    return f'''<section class="band band--teal fvb">
<style>.fvb{{position:relative; overflow:hidden}} .fvb__g{{display:grid; grid-template-columns:minmax(0,1.25fr) minmax(0,.75fr); gap:clamp(24px,5vw,64px); align-items:center}}
.fvb__mark{{display:flex; align-items:center; gap:10px; font-family:var(--display); font-weight:900; font-stretch:115%; font-size:1.05rem; color:#fff; margin:0 0 14px}} .fvb__mark .daisy{{width:32px; height:32px; color:var(--mint)}}
.fvb h2{{color:#fff; margin:0 0 .35em}} .fvb .lede{{color:#fff}} .fvb__ph{{width:min(250px,64vw); margin-inline:auto; aspect-ratio:390/800; border-radius:38px; border:9px solid #0b1f25; background:#0b1f25; overflow:hidden; transform:rotate(-4deg); box-shadow:0 40px 80px -30px rgba(0,0,0,.6)}}
.fvb__ph img{{width:100%; height:100%; object-fit:cover; object-position:top}} .fvb__chips{{display:flex; flex-wrap:wrap; gap:8px; margin-top:18px}} .fvb__chips span{{font-family:var(--mono); font-size:.7rem; letter-spacing:.08em; text-transform:uppercase; font-weight:600; padding:5px 9px; border-radius:6px; background:var(--slate-deep); color:#fff}}
@media (max-width:760px){{.fvb__g{{grid-template-columns:minmax(0,1fr)}} .fvb__ph{{width:min(210px,56vw)}}}}</style>
<div class="wrap fvb__g"><div><p class="fvb__mark">{daisy()}Vibe Check by SafeBAE</p><h2>{esc(heading)}</h2><p class="lede">{esc(lede)}</p>
<div class="btns">{btn('Open Vibe Check', 'https://checkyourvibe.org/', 'mint')}{btn('How it works', 'vibe-check.html', 'white', arrow=True)}</div>
<div class="fvb__chips"><span>Anonymous</span><span>No account</span><span>Nothing stored</span></div></div>
<div class="fvb__ph">{img('vc-screen', 'The Vibe Check home screen on a phone')}</div></div></section>'''

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

def film_page(slug, title, desc, body, key, fonts, css):
    page(slug, title + ' · SafeBAE', desc, body, active='library', body_class=f'film film--{key}', fonts=fonts,
         head_extra=f'<style>{GPANEL_CSS}{HELPLINE_CSS}{css}</style>', scripts=GUIDE_JS)
