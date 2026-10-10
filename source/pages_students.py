"""STUDENTS group: students.html, peer-educator.html, clubs.html, reform-policy.html,
summer-institute.html, espanol.html.  Run: python3 -c "import pages_students; pages_students.build()" """
from lib import *
from films_common import help_inline, HELPLINE_CSS
from pages_home import cpet_player, film_strip, FILM_STRIP_CSS, film_font_link
import json

# ---------------------------------------------------------------- links
CPET_FORM = 'https://docs.google.com/forms/d/e/1FAIpQLSf5tlvO1pFmNl01tnrdSQCpPPaYB5djk81uu7eUyVTMzWj3kQ/viewform'
CLUB_FORM = 'https://docs.google.com/forms/d/e/1FAIpQLSfoQAsZ5bZpRyBpL1ELxoC0yk5ewm5mkpoz6wwR49IcGoKtLQ/viewform'
POLICY_FORM = 'https://docs.google.com/forms/d/e/1FAIpQLSdWO15lAjJlPeQd_nVJXyd_v0_XrnWWzjcV29rornyf4gFb_w/viewform'
ES_FORM = 'https://docs.google.com/forms/d/e/1FAIpQLScz_QD0Ms-xgeDe7C3S_3W8SK1fI-u5rflrffsmhOSh1S7B3g/viewform'
CLUB_HUB = 'https://clubs.safebae.org'
RESUME = 'https://learning.safebae.org/students'
SKILLS = 'https://skills-lab.safebae.org/'
VIBE = 'https://checkyourvibe.org/'
CALENDLY = 'https://calendly.com/clubsupport-safebae/30min'
CLUB_EMAIL = 'clubsupport@safebae.org'

def crumbs(*items):
    parts = [('Home', 'index.html')] + list(items)
    return '<nav class="crumbs" aria-label="Breadcrumb">' + '<span>/</span>'.join(a(esc(t), h) if h else f'<span>{esc(t)}</span>' for t, h in parts) + '</nav>'

def st_help():
    """Student-facing wording of the shared helpline strip."""
    return help_inline().replace('Share these 24/7, confidential resources with students', 'Need to talk to someone? Free, confidential and open 24/7')

def phero_alt(html_, media, alt):
    """phero() renders its media image with alt=""; give it real alt text."""
    return re.sub(r'(<img src="assets/img/' + re.escape(media) + r'\.webp"[^>]*?) alt=""', lambda m: m.group(1) + f' alt="{esc(alt)}"', html_, count=1)

def check_list(items, cls=''):
    return f'<ul class="st-check {cls}">' + ''.join(f'<li>{i}</li>' for i in items) + '</ul>'

# ---------------------------------------------------------------- the student journey
JOURNEY = [
    ('Learn', 'Watch the films', 'Youth-made films with discussion guides, plus the BAE Skills Lab.', 'library.html#films'),
    ('Train', 'Become a Certified Peer Educator', 'Free and self-paced: 16 modules and a certificate.', 'peer-educator.html'),
    ('Lead', 'Start or join a SafeBAE club', 'Start, affiliate or restart a chapter at your school.', 'clubs.html'),
    ('Change', 'Reform your school’s policy', 'A student guide to stronger sexual misconduct policies.', 'reform-policy.html'),
]

def journey(cur=None):
    lis = []
    for verb, title, desc, href in JOURNEY:
        on = verb == cur
        inner = (f'<span class="st-stop__dot" aria-hidden="true">{daisy() if on else "&rarr;"}</span>'
                 f'<span class="st-stop__verb">{esc(verb)}{" &middot; you are here" if on else ""}</span>'
                 f'<b>{esc(title)}</b><small>{esc(desc)}</small>')
        if on:
            lis.append(f'<li class="on"><span class="st-stop" aria-current="page">{inner}</span></li>')
        else:
            lis.append(f'<li><a class="st-stop" href="{href}">{inner}</a></li>')
    return '<ol class="st-path">' + ''.join(lis) + '</ol>'

# ---------------------------------------------------------------- shared CSS
CSS = HELPLINE_CSS + '''
.st-hero{background:var(--slate); color:#fff; position:relative; overflow:hidden}
.st-hero__grid{display:grid; grid-template-columns:minmax(0,1.05fr) minmax(0,.95fr); gap:clamp(28px,5vw,64px); align-items:center; padding-block:clamp(44px,6vw,84px)}
.st-hero__title{font-size:clamp(2.4rem,5vw,5.1rem); line-height:.88; font-weight:900; font-stretch:125%; text-transform:uppercase; letter-spacing:-.02em; margin:0 0 .4em}
.st-hero__title span{display:block}
.st-hero .lede{color:rgba(255,255,255,.9); max-width:none}
.st-proof{display:flex; flex-wrap:wrap; gap:8px 22px; margin-top:24px; font-weight:600; font-size:.9rem; color:var(--aqua)}
.st-proof span::before{content:""; display:inline-block; width:8px; height:8px; background:var(--mint); margin-right:8px; transform:rotate(45deg) translateY(-2px)}
.st-col{position:relative; width:100%; max-width:620px; aspect-ratio:1/1; margin-left:auto}
.st-col figure{position:absolute; margin:0; border:6px solid #fff; border-radius:12px; overflow:hidden; background:#fff; box-shadow:0 26px 50px -24px rgba(0,0,0,.75); transition:transform .35s cubic-bezier(.2,.7,.2,1)}
.st-col figure:hover{transform:rotate(0) scale(1.03); z-index:2}
.st-col img{width:100%; height:100%; object-fit:cover}
.st-col .f1{left:0; top:3%; width:60%; height:52%; transform:rotate(-3deg)}
.st-col .f2{right:0; top:0; width:42%; height:40%; transform:rotate(3deg)}
.st-col .f3{right:1%; top:43%; width:45%; height:28%; transform:rotate(-1.5deg)}
.st-col .f4{left:2%; top:58%; width:36%; height:40%; transform:rotate(2.5deg)}
.st-col .f5{left:41%; top:73%; width:57%; height:27%; transform:rotate(-2deg)}
.st-col .sticker{position:absolute; z-index:3}
@media (max-width:900px){ .st-hero__grid{grid-template-columns:1fr} .st-col{margin:0 auto; max-width:520px} }

.st .phero .eyebrow{color:var(--mint)} .st .phero--teal .eyebrow{color:var(--aqua)}
.st .phero .link{color:var(--mint)}
.st .phero--teal .crumbs{color:#fff}
.st .band--paper .eyebrow,.st .band--aqua .eyebrow,.st .band--mist .eyebrow{color:var(--logo-teal)}
.st .st-box--slate .eyebrow{color:var(--mint)} .st .st-box--mint .eyebrow{color:var(--slate)}
.st-clubs .phero h1,.st-pe .phero h1{font-size:clamp(2.3rem,4.7vw,4.3rem)}
/* journey path */
.st-path{list-style:none; margin:0; padding:0; display:grid; grid-template-columns:repeat(4,minmax(0,1fr)); gap:22px}
.st-path li{position:relative; margin:0; min-width:0}
.st-path li:not(:last-child)::after{content:""; position:absolute; top:27px; left:70px; right:-10px; height:4px; border-radius:2px; background:currentColor; opacity:.28}
.st-stop{display:flex; flex-direction:column; gap:4px; text-decoration:none; color:inherit; height:100%}
.st-stop__dot{width:58px; height:58px; border-radius:50%; border:3px solid currentColor; display:grid; place-items:center; font-weight:800; font-size:1.3rem; margin-bottom:10px; transition:background .2s, color .2s, transform .2s; background:transparent}
.st-stop__dot .daisy{width:30px; height:30px}
a.st-stop:hover .st-stop__dot{background:var(--slate); color:var(--mint); border-color:var(--slate); transform:translateX(4px)}
.band--slate a.st-stop:hover .st-stop__dot,.band--deep a.st-stop:hover .st-stop__dot{background:var(--mint); color:var(--slate); border-color:var(--mint)}
.st-path li.on .st-stop__dot{background:var(--slate); color:var(--mint); border-color:var(--slate)}
.band--slate .st-path li.on .st-stop__dot,.band--deep .st-path li.on .st-stop__dot{background:var(--mint); color:var(--slate); border-color:var(--mint)}
.st-stop__verb{font-family:var(--mono); font-size:.72rem; letter-spacing:.1em; text-transform:uppercase; font-weight:600; opacity:.8}
.st-stop b{font-family:var(--display); font-stretch:108%; font-size:1.18rem; line-height:1.15}
a.st-stop:hover b{text-decoration:underline; text-decoration-thickness:2px; text-underline-offset:3px}
.st-stop small{font-size:.9rem; line-height:1.4; opacity:.82}
@media (max-width:860px){
  .st-path{grid-template-columns:1fr; gap:0}
  .st-path li{padding-bottom:18px}
  .st-path li:not(:last-child)::after{top:62px; bottom:4px; left:27px; right:auto; width:4px; height:auto}
  .st-stop{display:grid; grid-template-columns:58px minmax(0,1fr); column-gap:16px; row-gap:2px}
  .st-stop__dot{grid-row:1/4; margin:0}
}

/* checklist */
.st-check{list-style:none; padding:0; margin:0 0 1.3em; display:grid; gap:10px}
.st-check--under{margin:22px 0 0}
.st-check li{position:relative; padding-left:34px; margin:0; font-weight:600; line-height:1.45}
.st-check li::before{content:""; position:absolute; left:0; top:0; width:23px; height:23px; border-radius:6px; background:var(--mint) url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 24 24'%3E%3Cpath d='M5 12.5l4.5 4.5L19 7.5' fill='none' stroke='%231d414e' stroke-width='3.2' stroke-linecap='round' stroke-linejoin='round'/%3E%3C/svg%3E") center/15px no-repeat}

/* equal-height boxes */
.st-duo{display:grid; grid-template-columns:repeat(2,minmax(0,1fr)); gap:clamp(16px,2vw,26px); align-items:stretch}
.st-box{border-radius:var(--r-lg); padding:clamp(24px,3.2vw,42px); display:flex; flex-direction:column; min-width:0}
.st-box > .btns{margin-top:auto; padding-top:22px}
.st-box--mint{background:var(--mint); color:var(--slate)}
.st-box--slate{background:var(--slate); color:#fff}
.st-box--white{background:#fff; border:1px solid var(--line)}
.st-box--aqua{background:var(--aqua); color:var(--slate)}
.st-box h2,.st-box h3{margin-bottom:.35em}
.st-box--slate .eyebrow{color:var(--mint)}
.st-box--mint .eyebrow{color:var(--slate)}
@media (max-width:860px){.st-duo{grid-template-columns:1fr}}

/* numbered vertical steps (real sequences) */
.st-vsteps{list-style:none; margin:0; padding:0; display:grid; gap:0}
.st-vsteps li{display:grid; grid-template-columns:52px minmax(0,1fr); gap:16px; padding:16px 0; border-top:1px solid var(--line); margin:0}
.st-vsteps li:last-child{border-bottom:1px solid var(--line)}
.st-vsteps .n{font-family:var(--display); font-weight:900; font-stretch:125%; font-size:2.2rem; line-height:1; color:var(--teal)}
.st-vsteps b{display:block; font-family:var(--display); font-stretch:106%; font-size:1.15rem; line-height:1.2; margin-bottom:3px}
.st-vsteps p{margin:0; color:var(--ink-soft); font-size:.95rem}

/* framed photo with sticker */
.st-photo{position:relative; margin:0}
.st-photo img{width:100%; border-radius:var(--r-lg); object-fit:cover; box-shadow:0 30px 60px -32px rgba(0,0,0,.6)}
.st-photo .sticker{position:absolute; left:-10px; bottom:20px}
.st-photo figcaption{font-size:.85rem; margin-top:10px; opacity:.8}
@media (max-width:860px){.st-photo .sticker{left:10px}}

/* quote */
.st-quote{border-left:6px solid var(--mint); padding:4px 0 4px clamp(18px,3vw,32px)}
.st-quote .quote::before{display:none}
.band--paper .st-quote,.band--aqua .st-quote,.band--mist .st-quote{border-color:var(--teal)}

/* embeds */
.st-embed .embed{background:#fff; border-radius:var(--r-lg); border:1px solid var(--line); padding:6px; box-shadow:var(--shadow)}
.st-embed .embed__fallback{border:0; background:var(--aqua); padding:clamp(22px,3vw,36px)}
.st-embed .embed__fallback p{font-family:var(--display); font-stretch:108%; font-size:1.25rem; margin-bottom:14px}

/* small link rows */
.st-links{display:grid; grid-template-columns:repeat(2,minmax(0,1fr)); column-gap:clamp(20px,3vw,40px)}
.st-links .rows:last-child{border-top-color:var(--line)}
@media (max-width:760px){.st-links{grid-template-columns:1fr} .st-links .rows + .rows{border-top:0}}

.st-reg{display:grid; grid-template-columns:minmax(0,.8fr) minmax(0,1.2fr); gap:clamp(24px,4vw,60px); align-items:start}
@media (max-width:900px){.st-reg{grid-template-columns:1fr}}
.st-note{display:flex; gap:16px 28px; align-items:center; justify-content:space-between; flex-wrap:wrap; padding:18px 22px; border-radius:14px; background:var(--mist); border:1px solid var(--line); margin-bottom:12px}
.st-note b{display:block; font-family:var(--display); font-stretch:106%}
.st-note p{margin:0; font-size:.94rem}
.st-college{margin-top:clamp(24px,3vw,34px); border-color:rgba(29,65,78,.25)}
.st-college .row{border-color:rgba(29,65,78,.25)}
.st-college .row:hover{background:rgba(255,255,255,.35)}
.st-college .go{background:var(--slate); color:var(--mint)}
.st-label{font-family:var(--mono); font-size:.72rem; letter-spacing:.1em; text-transform:uppercase; font-weight:600; color:var(--mint); margin:0 0 10px}
/* modules */
.st-mods{display:grid; grid-template-columns:repeat(4,minmax(0,1fr)); gap:10px; list-style:none; padding:0; margin:0}
.st-mod{display:flex; flex-direction:column; gap:8px; padding:16px; border-radius:12px; background:rgba(255,255,255,.05); border:1px solid var(--line-dark); margin:0; min-width:0; transition:background .2s, border-color .2s}
.st-mod:hover{background:rgba(21,255,200,.08); border-color:rgba(21,255,200,.45)}
.st-mod__n{font-family:var(--display); font-stretch:125%; font-weight:900; color:var(--mint); font-size:1.7rem; line-height:1}
.st-mod__t{font-weight:700; line-height:1.3; font-size:.98rem}
.st-mod a{margin-top:auto; font-family:var(--mono); font-size:.7rem; letter-spacing:.06em; text-transform:uppercase; color:var(--aqua); text-decoration:none; padding-top:6px}
.st-mod a:hover{color:var(--mint)}
@media (max-width:1000px){.st-mods{grid-template-columns:repeat(2,minmax(0,1fr))}}
@media (max-width:480px){.st-mods{grid-template-columns:1fr}}
'''

# ================================================================= students.html
HUB_CSS = FILM_STRIP_CSS.replace('#210658', '#1d414e') + '''
.st-vibe{display:grid; grid-template-columns:minmax(0,.95fr) minmax(0,1.05fr); gap:clamp(28px,5vw,72px); align-items:center}
.st-vibe__mark{display:flex; align-items:center; gap:12px; font-family:var(--display); font-weight:900; font-stretch:115%; font-size:1.25rem; color:var(--mint); margin-bottom:18px}
.st-vibe__mark .daisy{width:40px; height:40px}
.st-qs{position:relative; height:calc(clamp(2.2rem,4.6vw,4.1rem) * 2.1); overflow:hidden; margin:0 0 .4em}
.st-qs span{position:absolute; inset:0; display:flex; align-items:flex-end; font-family:var(--display); font-weight:900; font-stretch:118%; font-size:clamp(2.2rem,4.6vw,4.1rem); line-height:1; letter-spacing:-.02em; color:#fff; transform:translateY(110%); opacity:0; transition:transform .7s cubic-bezier(.2,.8,.2,1), opacity .7s}
.st-qs span.on{transform:none; opacity:1}
.st-qs span.out{transform:translateY(-110%); opacity:0}
.st-vibe__media{position:relative}
.st-vibe__media .sticker{position:absolute; z-index:3}
.st-vibe__phone{position:absolute; right:-10px; bottom:-34px; width:min(150px,28%); aspect-ratio:600/1298; border-radius:22px; border:6px solid #0b1f25; overflow:hidden; box-shadow:0 30px 60px -20px rgba(0,0,0,.6); transform:rotate(5deg); z-index:2; background:#0b1f25}
.st-vibe__phone img{width:100%; height:100%; object-fit:cover; object-position:top}
@media (max-width:900px){.st-vibe{grid-template-columns:1fr} .st-vibe__media{order:-1; margin-bottom:24px} .st-vibe__phone{right:8px; bottom:-26px; width:min(120px,26%)}}
.st-ways{display:grid; gap:10px; margin:0 0 22px}
.st-way{display:grid; grid-template-columns:minmax(0,1fr) auto; gap:4px 16px; align-items:center; padding:16px 18px; border-radius:12px; background:rgba(255,255,255,.06); border:1px solid var(--line-dark); text-decoration:none; color:#fff; transition:background .2s, border-color .2s}
.st-way:hover{background:rgba(21,255,200,.1); border-color:var(--mint)}
.st-way b{font-family:var(--display); font-stretch:108%; font-size:1.15rem; line-height:1.2}
.st-way small{grid-column:1; color:rgba(255,255,255,.75); font-size:.9rem}
.st-way .go{grid-row:1/3; grid-column:2; width:36px; height:36px; border-radius:50%; display:grid; place-items:center; background:var(--mint); color:var(--slate); font-weight:800}
.st-tabletop{position:relative}
.st-tabletop img{border-radius:var(--r-lg); width:100%; aspect-ratio:4/3.1; object-fit:cover}
.st-tabletop .sticker{position:absolute; right:14px; top:-14px}
.st-tabletop p{margin-top:12px; font-size:.86rem; color:rgba(255,255,255,.7)}
.st-lab{position:relative; overflow:hidden}
.st-lab__big{font-family:var(--display); font-weight:900; font-stretch:125%; text-transform:uppercase; font-size:clamp(2.6rem,5vw,4.4rem); line-height:.88; letter-spacing:-.02em; margin:0 0 .35em}
.st-lab__tags{display:flex; flex-wrap:wrap; gap:10px; margin:6px 0 4px}
.st-lab__tags .sticker:nth-child(2){transform:rotate(2deg)} .st-lab__tags .sticker:nth-child(3){transform:rotate(-1deg)}
.st-tix{display:grid; gap:0; margin:6px 0 0; border-top:1px solid var(--line-dark)}
.st-tix > div{padding:14px 0; border-bottom:1px solid var(--line-dark)}
.st-tix h4{color:var(--mint); margin:0 0 4px; font-size:1.05rem}
.st-tix p{margin:0; font-size:.94rem; color:rgba(255,255,255,.82)}
.st-faces{margin-top:clamp(28px,4vw,44px)}
.st-faces .marquee__track{gap:14px; animation-duration:70s}
.st-faces img{width:104px; height:104px; border-radius:50%; object-fit:cover; border:4px solid #fff; box-shadow:0 10px 24px -14px rgba(0,0,0,.5)}
.st-faces a{display:block; text-decoration:none}
.st-support{display:grid; grid-template-columns:minmax(0,.85fr) minmax(0,1.15fr); gap:clamp(22px,4vw,48px); align-items:center; background:#fff; border:3px solid var(--coral); border-radius:var(--r-lg); padding:clamp(22px,3.4vw,44px)}
.st-support h2{font-size:clamp(1.7rem,3vw,2.5rem)}
.st-lines{display:grid; grid-template-columns:repeat(2,minmax(0,1fr)); gap:10px}
.st-line{background:var(--mist); border-radius:12px; padding:14px 16px; min-width:0}
.st-line b{display:block; font-family:var(--display); font-stretch:106%; line-height:1.2}
.st-line span{display:block; font-family:var(--mono); font-weight:600; font-size:.86rem; color:var(--logo-teal); margin-top:4px}
.st-line small{display:block; color:var(--ink-soft); font-size:.82rem; margin-top:4px; line-height:1.35}
@media (max-width:900px){.st-support{grid-template-columns:1fr}}
@media (max-width:520px){.st-lines{grid-template-columns:1fr}}
'''

HUB_JS = r'''<script>
(function(){
  var qs = document.querySelectorAll('.st-qs span'), i = 0, reduce = window.matchMedia && matchMedia('(prefers-reduced-motion: reduce)').matches;
  if(qs.length > 1 && !reduce){ setInterval(function(){ var cur = qs[i]; cur.classList.remove('on'); cur.classList.add('out'); i = (i+1) % qs.length; var nx = qs[i]; nx.classList.remove('out'); void nx.offsetWidth; nx.classList.add('on'); setTimeout(function(){ cur.classList.remove('out'); }, 800); }, 2600); }
})();
</script>'''

F2025 = ['Adrian Alie', 'Alan Mejia', 'Armando Refcalbo', 'Ava Maldonado', 'Ava Ram', 'Brianna Benitev', 'Cayden Michaud', 'Cyra Wuthrich',
         'David Zamora', ('Dolly Barrat', 'dolly-barratt'), 'Edwinah Magloire', 'Elle Mone', ('Isaac Smith NJ', 'isaac-smith-nj'), 'Isabella Cabral', 'Jaclyn Verde',
         'Jada Davis', 'Jada Martinez', 'Luisa Palomares', 'Mimi Ndiaye', 'Molly Pines', 'Nick Niedbalski', 'Riley Devereaux', 'Skyla Vivar Rosado',
         'Sophia Nguyen', ('Summer Wilson NJ', 'summer-wilson-nj'), 'Sunny Brynildsen', 'Yareli Huerta']
F2025 = [(x, re.sub(r'[^a-z0-9]+', '-', x.lower())) if isinstance(x, str) else x for x in F2025]
F2024 = [('Lilliana Katz-Hollander', 'lilliana-kh', 'she/her'), ('Anna Yang', 'anna-yang', ''), ('Apollo Knapp', 'apollo-knapp-headshot', 'He/They'),
         ('Arturo Rosado Taveras', 'arturo-rosadot', 'Also a 2023 fellow'), ('August Chandler', 'august-chandler', ''), ('Cole Firshein', 'cole-firshein', ''),
         ('Matteo Netto', 'matteo-netto', ''), ('Kaylee Cuevas', 'kaylee-cuevas', ''), ('Anna Diegnan', 'anna-deignan', ''),
         ('Lucy Wells-Davies', 'lucy-wells-davies-headshot', 'she/her'), ('Mara Scott', 'mara-scott', ''), ('Jada Metcalf', 'jada-metcalf-headshot', 'she/they'),
         ('Taniyah Jackson', 'taniyah-jackson', ''), ('Tristan Greene', 'tristan-greene-headshot', 'he/him'), ('Val Odiembo', 'val-odiembo', '')]
F2023 = [('Alison Chang', 'alison-chang-headshot-alison-chang', ''), ('Arturo Rosado Taveras', 'ca49ee25-ce60-4a29-ad70-3a3b48de9d32-arturo-rosado', 'Also a 2024 fellow'),
         ('Ava Dare', '3d9b25eb-3bc8-4f20-b5f9-c33b417a21cf-ava-dare', ''), ('Britney Cunningham', 'img-4121-britney-cunningham', ''),
         ('Cathy Williams', '30125793-52af-484d-8046-f75d312bcfbe-cathy-w', ''), ('Claudia Cham', 'img-8130-claudia-kulee-cham', ''),
         ('Dorie McNamara', '878c21b1-e5e6-4cea-8b5a-bfa7808d2636-dorie-mcnamara', ''), ('Enetu Nelson', 'img-1031-enetu-nelson', ''),
         ('Hector Jaco', 'img-8426-hector-jaco', ''), ('Inanna Balkin', 'img-7930-inanna-balkin', ''), ('Isabella Ocejo', 'img-5684-isabella-ocejo', ''),
         ('Jully Myrthil', 'img-5326-jully-m', ''), ('Maria Muntean', 'mariamuntean-maria-muntean', ''), ('Mia (Mimi) Stewart', 'renderedimage-mia-stewart', ''),
         ('Mica Ormeno', 'img-8576-micaela-ormeno', '')]

def students():
    collage = f'''<div class="st-col">
      <figure class="f1">{img('1-000383-edited', 'SafeBAE students in tie-dye shirts crowd together for a group photo', loading='eager')}</figure>
      <figure class="f2">{img('clubhero', 'SafeBAE club members together at the beach', loading='eager')}</figure>
      <figure class="f3">{img('000398', 'Two students in SafeBAE tie-dye shirts', loading='eager')}</figure>
      <figure class="f4">{img('img-9509-1', 'Students making hand-lettered consent posters', loading='eager')}</figure>
      <figure class="f5">{img('img-6834', 'A group of SafeBAE youth leaders at sunset', loading='eager')}</figure>
      <span class="sticker" style="left:44%;top:1%">Youth-led</span>
      <span class="sticker sticker--coral sticker--r" style="left:1%;top:51%">Founded by teen survivors</span>
      <span class="sticker sticker--aqua" style="right:1%;top:67%">Free for students</span>
    </div>'''

    ways = [('Start a new chapter', 'If there’s nothing like this at your school yet', 'clubs.html#new'),
            ('Affiliate a club you already run', 'Student council, a wellness club, an affinity group', 'clubs.html#affiliate'),
            ('Restart last year’s chapter', 'If your school used to have one', 'clubs.html#restart')]
    way_html = ''.join(f'<a class="st-way" href="{h}"><b>{esc(t)}</b><small>{esc(s)}</small><span class="go" aria-hidden="true">&rarr;</span></a>' for t, s, h in ways)

    faces = ''.join(f'<a href="summer-institute.html#fellows" tabindex="-1">{img(sl, "")}</a>' for n, sl in F2025)

    resources = [
        ('Myths & Facts', 'Common myths about assault, paired with the research-backed facts that debunk them.', 'myths-facts.html'),
        ('Posters', 'Free downloadable prevention posters on consent, boundaries, and online harassment.', 'posters.html'),
        ('Podcasts', 'Episodes featuring SafeBAE founders, staff, and youth leaders. Free to listen and share.', 'library.html#podcasts'),
        ('Videos', 'Short films made by young people, each paired with a ready-to-teach discussion guide.', 'library.html#films'),
        ('Survivor Support', 'Resources for survivors and loved ones, including crisis lines, survivor-centered media, and disclosure guidance.', 'survivor-support.html'),
        ('Blog', 'Survivor stories, media analysis, and policy news from the SafeBAE community.', 'blog.html'),
    ]
    res_l = ''.join(row(t, d, h) for t, d, h in resources[:3])
    res_r = ''.join(row(t, d, h) for t, d, h in resources[3:])

    lines = ''.join(f'<div class="st-line"><b>{esc(n)}</b><span>{esc(num)}</span><small>{esc(d)}</small></div>' for n, s, num, d, u in HOTLINES[:4])

    body = f'''
<section class="st-hero">
  <div class="wrap st-hero__grid">
    <div>
      {crumbs(('Students', None))}
      <p class="eyebrow" style="color:var(--mint)">For Students</p>
      <h1 class="st-hero__title"><span>For students,</span><span class="mint">by students.</span></h1>
      <p class="lede">SafeBAE was founded by teen survivors who wanted their schools to change. Everything on this site was built by students, for you. Become a Certified Peer Educator, start a SafeBAE club at your school, push your district to fix its policies, or find information and support for yourself or a friend.</p>
      <div class="btns">{btn('Become a Peer Educator', 'peer-educator.html', 'mint', arrow=True)}{btn('Start a club', 'clubs.html', 'ghost')}<button class="btn btn--coral" data-open-help>Get support now</button></div>
      <div class="st-proof"><span>3,000+ Certified Peer Educators</span><span>Open to high school students anywhere</span></div>
    </div>
    {collage}
  </div>
</section>

<section class="band band--mint band--tight">
  <div class="wrap">
    <div class="section-head"><div><h2>Pick a starting point</h2><p class="lede lede--full">Wherever you start, you are part of a national movement of students working to end sexual violence in schools.</p></div></div>
    {journey()}
    <div class="rows st-college">{row('In college?', 'Mentor high schoolers or start a SafeBAE club on your campus.', 'college.html')}</div>
  </div>
</section>

<section class="band band--paper" id="peer-educator">
  <div class="wrap split">
    <div>
      {eyebrow('For Daisy: Before Anyone Else', True)}
      <h2>Become a Certified Peer Educator</h2>
      <p class="lede">A free, self-paced training for students who want to lead prevention at their school. Sixteen online modules cover healthy relationships and boundaries, consent, bystander intervention, online safety, student rights under Title IX, how to support a survivor, and more.</p>
      <div class="btns">{btn('Get registered', 'peer-educator.html#register', 'slate', arrow=True)}{btn('See all 16 modules', 'peer-educator.html#modules', 'ghost')}{btn('Resume training', RESUME, 'ghost')}</div>
      <p class="small muted" style="margin-top:16px">Prefer Spanish? {a('Ver el entrenamiento en español', 'espanol.html', 'link')}</p>
    </div>
    <div>{cpet_player()}{check_list(['Free, self-paced, and open to high school students anywhere', 'Support from our team and a community of other peer educators', 'Finish the modules and the after survey to earn your certificate'], 'st-check--under')}</div>
  </div>
</section>

<section class="band band--deep" id="clubs">
  <div class="wrap split split--wide-r">
    <figure class="st-tabletop" style="margin:0">{img('clubtabling', 'A SafeBAE club table with red, yellow, and green flags, Can I Kiss You? buttons, and Vibe Check cards')}<span class="sticker">Free to register</span><p>A SafeBAE club table: red, yellow and green flags, “Can I Kiss You?” buttons and Vibe Check cards.</p></figure>
    <div>
      <p class="eyebrow">SafeBAE Clubs</p>
      <h2>Start a club at your school</h2>
      <p style="color:rgba(255,255,255,.86)">A SafeBAE club focused on consent and dating violence prevention can help shift the culture among your peers and build a safer school community. Start a new club, or bring SafeBAE programming into a group you already belong to.</p>
      {chips(['Any school', 'Members-only Club Hub', 'Virtual training sessions'], 'mint')}
      <p class="st-label" style="margin-top:22px">Three ways to do it</p>
      <div class="st-ways">{way_html}</div>
      <div class="btns">{btn('Register your club', CLUB_FORM, 'mint')}{btn('How clubs work', 'clubs.html', 'ghost', arrow=True)}</div>
    </div>
  </div>
</section>

<section class="band band--teal" id="vibe-check">
  <div class="wrap st-vibe">
    <div class="st-vibe__media">
      {yt('Ng8S3w1eTRU', 'Vibe Check demo', label='Demo')}
      <div class="st-vibe__phone">{img('vc-screen', 'The Vibe Check home screen on a phone')}</div>
      <span class="sticker" style="left:-8px;top:-14px">Anonymous</span>
      <span class="sticker sticker--white sticker--r" style="left:18px;bottom:-16px">No account needed</span>
    </div>
    <div>
      <div class="st-vibe__mark"><span class="daisy"></span>Vibe Check by SafeBAE</div>
      <div class="st-qs" aria-hidden="true"><span class="on">Did I cross a line?</span><span>Was that consent?</span><span>Did I harm someone?</span><span>Did my friend cross a line?</span></div>
      <p class="lede" style="color:#fff">A private, self-guided reflection tool for anyone questioning whether they, or a friend, may have crossed a line.</p>
      <p style="color:rgba(255,255,255,.88)">Nothing is ever reported and no account is required. Vibe Check walks you through what happened and what to do next, and connects you with real resources on consent, communication and accountability.</p>
      <div class="btns">{btn('Open Vibe Check', VIBE, 'mint')}{btn('How it works', 'vibe-check.html', 'white', arrow=True)}</div>
    </div>
  </div>
</section>

<section class="band band--paper">
  <div class="wrap st-duo">
    <div class="st-box st-box--mint st-lab">
      <p class="eyebrow">Practice</p>
      <p class="st-lab__big">BAE Skills Lab</p>
      <p>Short interactive activities about consent, boundaries, and healthy relationships. Put your learning into practice and strengthen your skills as a peer educator and club leader.</p>
      <div class="st-lab__tags"><span class="sticker sticker--white">Consent</span><span class="sticker sticker--white">Boundaries</span><span class="sticker sticker--white">Healthy relationships</span></div>
      <div class="btns">{btn('Open the Skills Lab', SKILLS, 'slate')}</div>
    </div>
    <div class="st-box st-box--slate">
      <p class="eyebrow">Your rights</p>
      <h2 style="font-size:clamp(1.7rem,2.8vw,2.4rem)">Title IX &amp; your school’s policy</h2>
      <p style="color:rgba(255,255,255,.86)">Title IX is the federal law that bars sex discrimination, including sexual harassment and assault, at any school that takes federal funding.</p>
      <div class="st-tix">
        <div><h4>Know your rights</h4><p>Your right to report, to supportive measures like a schedule change, and to a prompt, fair investigation.</p></div>
        <div><h4>Find your coordinator</h4><p>Learn whether your school is covered by Title IX, and how to find your school’s Title IX Coordinator.</p></div>
        <div><h4>Understand and change your school’s policy</h4><p>What your school’s sexual misconduct policy says, what a strong one should include, and how to advocate for change.</p></div>
      </div>
      <div class="btns">{btn('Title IX basics', 'title-ix.html', 'mint', arrow=True)}{btn('Policy reform guide', 'reform-policy.html', 'ghost')}</div>
    </div>
  </div>
</section>

<section class="band band--aqua" id="institute">
  <div class="wrap split">
    <div>
      <p class="eyebrow">Summer Activist Institute</p>
      <h2>Meet the fellows</h2>
      <p class="lede">Fellows from SafeBAE’s 2023, 2024 and 2025 Summer Activist Institutes. The 2024 institute covered theories of change, Title IX, sex education, policy reform, storytelling for change and engaging men in the conversation.</p>
      <div class="btns">{btn('Meet the 2025 fellows', 'summer-institute.html#fellows', 'slate', arrow=True)}{btn('See the 2024 schedule', 'summer-institute.html#schedule', 'ghost')}</div>
    </div>
    <figure class="st-photo">{img('sumact5', 'Summer Activist Institute fellows in a discussion circle')}<span class="sticker">27 fellows in 2025</span></figure>
  </div>
  <div class="st-faces marquee" aria-hidden="true"><div class="marquee__track">{faces}{faces}</div></div>
</section>

<section class="band band--deep" id="films">
  <div class="wrap">
    <div class="section-head"><div><p class="eyebrow">The Library</p><h2>Films made by young people</h2><p class="lede lede--full" style="color:rgba(255,255,255,.85)">Short films written, directed and performed by young people, each paired with a ready-to-teach discussion guide.</p></div>{btn('Open the library', 'library.html#films', 'mint', arrow=True)}</div>
  </div>
  <div class="wrap wrap--wide">{film_strip()}</div>
</section>

<section class="band band--paper">
  <div class="wrap">
    <div class="st-support" id="support">
      <div>
        <p class="eyebrow" style="color:var(--slate)"><span class="daisy" style="color:var(--coral)"></span>Support for you or a friend</p>
        <h2>If something happened, you don’t have to handle it alone.</h2>
        <p class="muted">Crisis lines, survivor-centered media, and guidance on how to tell someone, or how to respond when a friend tells you.</p>
        <div class="btns">{btn('Survivor support', 'survivor-support.html', 'slate', arrow=True)}<button class="btn btn--coral" data-open-help>All hotlines</button></div>
      </div>
      <div class="st-lines">{lines}</div>
    </div>
    <div class="section-head" style="margin-top:clamp(44px,6vw,72px)"><div><h2>More from SafeBAE</h2></div></div>
    <div class="st-links"><div class="rows">{res_l}</div><div class="rows">{res_r}</div></div>
  </div>
</section>
{give_band()}
'''
    page('students.html', 'For Students · SafeBAE', 'Become a youth leader with SafeBAE. Join peer educator training, start a club, and help prevent sexual violence in your school and community.',
         body, active='students', body_class='st st-hub', fonts=film_font_link(), head_extra=f'<style>{CSS}{HUB_CSS}</style>', scripts=HUB_JS)


# ================================================================= peer-educator.html
MODULES = [
    ('Rape Culture & Creating a Culture of Respect', ('Watch: Rape Culture to Respect', 'film-rape-culture.html')),
    ('Sexual Harassment, Assault, & Rape Defined', None),
    ('Consent is BAE (Before <i>Anything</i> Else)', ('Watch: It’s Giving Red Flags', 'film-its-giving-red-flags.html')),
    ('Healthy Relationships & Boundaries', ('Practice: BAE Skills Lab', SKILLS)),
    ('Male Identified Youth & Sexual Violence', ('Watch: Theo’s Story', 'film-sexual-assault-of-men.html')),
    ('Myths, Facts & Statistics', ('Read: Myths & Facts', 'myths-facts.html')),
    ('Sexual Violence & Relationships in Media', None),
    ('Online Safety & Sending Nudes', ('Watch: #knowB4Unude', 'film-knowb4unude.html')),
    ('How to Support A Survivor', ('Read: Survivor Support', 'survivor-support.html')),
    ('Reporting Options & Investigation Requirements', None),
    ('Your Rights in School (Title IX & Beyond)', ('Read: Title IX', 'title-ix.html')),
    ('Healing After Sexual Assault', None),
    ('Dating After Experiencing Sexual Violence', ('Watch: Intimacy & Dating', 'film-dating-after-sexual-assault.html')),
    ('Bystander Intervention (The BAEcode)', ('Watch: BAEcode: Game On!', 'film-baecode-game-on.html')),
    ('How to Respond If You’ve Been Accused', ('Reflect: Vibe Check', 'vibe-check.html')),
    ('Public Speaking & Leading as a Peer Educator', None),
]

PE_CSS = '''
.st-facts{display:grid; grid-template-columns:repeat(4,minmax(0,1fr)); gap:0}
.st-facts > div{padding:6px 22px; border-left:2px solid rgba(29,65,78,.22); min-width:0}
.st-facts > div:first-child{border-left:0; padding-left:0}
.st-facts b{display:block; font-family:var(--display); font-weight:900; font-stretch:118%; font-size:clamp(2.1rem,3.6vw,3.4rem); line-height:.95; letter-spacing:-.02em}
.st-facts span{display:block; font-weight:600; margin-top:6px; line-height:1.35}
@media (max-width:860px){.st-facts{grid-template-columns:1fr 1fr; row-gap:22px} .st-facts > div:nth-child(3){border-left:0; padding-left:0}}
.st-do{list-style:none; margin:0; padding:0; display:grid; gap:0}
.st-do li{display:flex; gap:14px; align-items:baseline; padding:13px 0; border-bottom:1px solid var(--line-dark); margin:0; font-weight:600}
.st-do li::before{content:""; flex:none; width:10px; height:10px; background:var(--mint); transform:rotate(45deg)}
.st-what{display:grid; grid-template-columns:minmax(0,1.1fr) minmax(0,.9fr); gap:clamp(24px,4vw,60px); align-items:stretch}
.st-what__img{border-radius:12px; width:100%; aspect-ratio:450/362; object-fit:cover; margin-bottom:18px}
@media (max-width:860px){.st-what{grid-template-columns:1fr}}
.st-prev{display:grid; grid-template-columns:minmax(0,1.5fr) minmax(0,.62fr); gap:clamp(18px,2.4vw,32px); align-items:start}
.st-chap{list-style:none; margin:0; padding:0; display:grid; gap:4px; counter-reset:none}
.st-chap button{width:100%; display:grid; grid-template-columns:30px minmax(0,1fr); gap:8px; text-align:left; font:inherit; font-size:.88rem; font-weight:600; line-height:1.3; padding:8px 10px; border-radius:8px; border:0; background:transparent; color:rgba(255,255,255,.78); cursor:pointer}
.st-chap button span{font-family:var(--mono); font-size:.72rem; color:var(--aqua); padding-top:2px}
.st-chap button:hover{background:rgba(255,255,255,.06); color:#fff}
.st-chap button[aria-current="true"]{background:var(--mint); color:var(--slate)}
.st-chap button[aria-current="true"] span{color:var(--slate)}
@media (max-width:960px){.st-prev{grid-template-columns:1fr} .st-chap{grid-template-columns:repeat(2,minmax(0,1fr))}}
@media (max-width:520px){.st-chap{grid-template-columns:1fr}}
'''

PE_JS = r'''<script>
(function(){
  var p = document.querySelector('.st-prev [data-player]'); if(!p) return;
  var slides = [].slice.call(p.querySelectorAll('.player__slide')), btns = [].slice.call(document.querySelectorAll('.st-chap button')), nx = p.querySelector('[data-next]');
  function cur(){ for(var i=0;i<slides.length;i++){ if(slides[i].classList.contains('on')) return i; } return 0; }
  function mark(){ var c = cur(); btns.forEach(function(b, i){ b.setAttribute('aria-current', String(i === c)); }); }
  btns.forEach(function(b, i){ b.addEventListener('click', function(){ var n = (i - cur() + slides.length) % slides.length; for(var k=0;k<n;k++){ nx.click(); } mark(); }); });
  if('MutationObserver' in window){ new MutationObserver(mark).observe(p, {subtree:true, attributes:true, attributeFilter:['class']}); }
  mark();
})();
</script>'''

CPET_CAPS = ['The only survivor-founded, youth-led org preventing sexual violence in schools', 'Why this training matters', 'Module 1 · Rape Culture & Shifting to a Culture of Respect', 'Consent starts way before sex. It starts when you’re a kid', 'The 6 Pillars of Consent', 'The foundation of a healthy relationship', 'BAEcode: real scripts for speaking up', 'Online safety & digital harassment', 'Supporting a partner who is a survivor', 'Wisdom from co-founder Daisy Coleman', 'Finish all 16 modules and become a Certified Peer Educator']

def peer_educator():
    mods = ''.join(f'<li class="st-mod"><span class="st-mod__n">{i+1}</span><span class="st-mod__t">{t}</span>' + (a(esc(rel[0]) + (' &#8599;' if rel[1].startswith('http') else ' &rarr;'), rel[1]) if rel else '') + '</li>' for i, (t, rel) in enumerate(MODULES))
    chap = ''.join(f'<li><button type="button" aria-current="{str(i==0).lower()}"><span>{i+1:02d}</span>{esc(c)}</button></li>' for i, c in enumerate(CPET_CAPS))
    steps = [
        ('Complete the registration form', f'Fill out a short interest form to get started. We’ll send you everything you need to begin the training. <a class="link" href="#register">Register below</a>'),
        ('Create your training portal account', 'Set up your secure account on Podia to unlock all 16 modules and additional resources.'),
        ('Complete 16 modules', 'Learn about consent, healthy relationships, digital safety, and more across 16 interactive modules, completed at your own pace.'),
        ('Complete the post-survey', 'Share feedback and reflect on what you’ve learned. Your responses help us improve the training and better support future Peer Educators.'),
        ('Earn your certificate', 'After completing all 16 modules and the post-training survey, you’ll receive your official SafeBAE Certified Peer Educator certificate.'),
        ('Start leading', f'Put your skills into action by leading presentations, organizing campaigns, or <a class="link" href="clubs.html">starting a SafeBAE Club</a>. You can also meet with the SafeBAE team to explore next steps.'),
    ]
    steps_html = ''.join(f'<div class="step"><span class="step__n">{i+1}</span><h3>{esc(t)}</h3><p>{d}</p></div>' for i, (t, d) in enumerate(steps))
    lede = 'SafeBAE’s Certified Peer Educator Training gives young people the knowledge, confidence and leadership skills to lead conversations about consent, healthy relationships and their lived experiences, and to drive prevention in their own schools and communities.'
    body = f'''
{phero_alt(phero('Certified Peer Educator Training', lede, 'For Daisy: Before Anyone Else', crumbs=[('Home','index.html'),('Students','students.html'),('Peer Educator Training',None)],
       media='dsc01134', sticker='Free · 16 modules',
       actions=btn('Register here', '#register', 'mint', arrow=True) + btn('Ver en Español', 'espanol.html', 'ghost') + btn('Resume training', RESUME, 'ghost'),
       extra='<p class="small" style="color:rgba(255,255,255,.75);margin:-.4em 0 1.4em">This training is offered in memory of our co-founder, Daisy Coleman, whose vision and leadership continue to inspire SafeBAE’s mission and youth nationwide. ' + a('#ForDaisy', 'fordaisy.html', 'link') + '</p>'), 'dsc01134', 'Certified Peer Educators in SafeBAE shirts gathered for a group photo')}

<section class="band band--mint band--tight">
  <div class="wrap st-facts">
    <div><b>16</b><span>interactive online modules</span></div>
    <div><b>$0</b><span>free for students, at their own pace</span></div>
    <div><b>1-on-1</b><span>support from SafeBAE’s team</span></div>
    <div><b>3,000+</b><span>young people certified</span></div>
  </div>
</section>

<section class="band band--paper">
  <div class="wrap st-what">
    <div>
      <p class="eyebrow">The certification</p>
      <h2>What is the Peer Educator Certification?</h2>
      <p class="lede">A free, self-paced training designed for high school students who want to lead sexual violence prevention in their schools and communities.</p>
      <p>Trauma-informed and accessible from anywhere, the program equips students to educate peers, challenge harmful norms, and build safer school environments. The certification includes 16 interactive online modules, plus one-on-one support from SafeBAE’s team. Upon completion, students receive an official certification, along with access to ongoing leadership, organizing, and advocacy opportunities.</p>
      <p>Educators looking to bring youth-led programming into their school can use the training too: it shifts school culture from the inside out. {a('Bring SafeBAE to your school', 'request-a-program.html', 'link')}</p>
    </div>
    <div class="st-box st-box--slate">
      {img('20240627-171417-646d14-4', 'Students raising their hands during a SafeBAE training session', cls='st-what__img')}
      <h3>What peer educators do</h3>
      <p style="color:rgba(255,255,255,.82)">Peer educators become trusted voices in their schools. This training creates a clear pathway for young people to drive cultural change.</p>
      <ul class="st-do"><li>Facilitate classroom discussions</li><li>Lead school clubs</li><li>Organize events</li><li>Run social media campaigns</li><li>Model what consent culture looks like in practice</li></ul>
    </div>
  </div>
</section>

<section class="band band--deep" id="preview">
  <div class="wrap">
    <div class="section-head"><div><p class="eyebrow">Preview the training</p><h2>Slides from inside the course</h2></div>{btn('Register here', '#register', 'mint', arrow=True)}</div>
    <div class="st-prev">{cpet_player()}<ol class="st-chap" aria-label="Jump to a slide">{chap}</ol></div>
  </div>
</section>

<section class="band band--slate" id="modules">
  <div class="wrap">
    <div class="section-head"><div><p class="eyebrow">Training modules</p><h2>What the 16 modules cover</h2><p class="lede lede--full" style="color:rgba(255,255,255,.85)">Consent, healthy relationships, digital safety, survivor support, your rights at school and more, completed at your own pace.</p></div></div>
    <ol class="st-mods">{mods}</ol>
  </div>
</section>

<section class="band band--paper" id="how">
  <div class="wrap">
    <div class="section-head"><div><p class="eyebrow">How it works</p><h2>Six steps to your certificate</h2><p class="lede lede--full">Becoming a Certified Peer Educator is simple, flexible, and fully supported. Students can register and complete the training entirely for free and at their own pace.</p></div></div>
    <div class="steps">{steps_html}</div>
    <div class="st-note" style="margin-top:clamp(22px,3vw,32px)"><div><b>Before you start</b><p class="muted">The modules include sensitive content that may be triggering. The training is self-paced and available any time after you register, so take breaks when you need them.</p></div></div>
    {st_help()}
  </div>
</section>

<section class="band band--teal">
  <div class="wrap split">
    <div>
      <p class="eyebrow">Why peer education matters</p>
      <h2>Students listen differently when students lead.</h2>
      <p style="color:rgba(255,255,255,.9)">Prevention only works when it feels real, and for most students, that means hearing it from someone they trust. Peer education brings authenticity, relatability, and lived experience into the conversation.</p>
      <p style="color:rgba(255,255,255,.9)">When youth lead, their peers ask more honest questions. They take ownership. They change behavior because they saw someone like them modeling something better, not because they were told to.</p>
      <p>{a('See the data on youth-led prevention', 'impact.html', 'arrow-link')}</p>
    </div>
    <figure class="st-photo">{img('img-3755', 'A group of SafeBAE students in a school hallway')}<span class="sticker">Youth-led</span></figure>
  </div>
  <div class="wrap" style="margin-top:clamp(32px,5vw,56px)">
    <div class="st-quote" style="border-color:var(--mint)"><blockquote class="quote">As I went on in the training, I felt like I could be a more helpful and supportive person and that I would know what to do if something happened to me or anyone I know. I feel confident that I can help people in all sorts of situations and I am more educated on the effects of rape culture.</blockquote><span class="cite" style="color:var(--aqua)">SafeBAE Certified Peer Educator</span></div>
  </div>
</section>

<section class="band band--mist" id="register">
  <div class="wrap st-reg">
    <div>
      <p class="eyebrow">Student registration</p>
      <h2>Register for the training</h2>
      <p class="lede">Fill out a short interest form to get started. We’ll send you everything you need to begin the training.</p>
      <div class="rows">
        {row('Already registered?', 'Pick up where you left off in the training portal.', RESUME)}
        {row('Entrenamiento en español', 'The full training is also available in Spanish.', 'espanol.html')}
        {row('Questions about the training?', 'Reach the SafeBAE team.', 'contact.html')}
      </div>
    </div>
    <div class="st-embed">{embed(CPET_FORM + '?embedded=true', CPET_FORM, 'Register for the Certified Peer Educator Training', height=1400, title='Certified Peer Educator Training registration')}</div>
  </div>
</section>

<section class="band band--paper">
  <div class="wrap">
    <div class="section-head"><div><p class="eyebrow">After you’re certified</p><h2>Put the training to work</h2><p class="lede lede--full">Certified Peer Educators lead presentations, run campaigns and start clubs. In college? Certified students are prioritized when paid mentorship opportunities become available. {a('College students', 'college.html', 'link')}</p></div></div>
    {journey('Train')}
  </div>
</section>
{give_band()}
'''
    page('peer-educator.html', 'Certified Peer Educator Training · SafeBAE', 'Become a certified peer educator with SafeBAE. Free, self-paced training for students to lead consent education and sexual violence prevention.',
         body, active='students', body_class='st st-pe', head_extra=f'<style>{CSS}{PE_CSS}</style>', scripts=PE_JS)


# ================================================================= clubs.html
CLUB_CSS = '''
.st-choose{display:grid; grid-template-columns:repeat(3,minmax(0,1fr)); gap:12px; margin-bottom:22px}
.st-choose [role="tab"]{scroll-margin-top:130px; font:inherit; text-align:left; cursor:pointer; padding:18px 18px 16px; border-radius:14px; border:2px solid var(--line); background:#fff; color:var(--slate); display:flex; flex-direction:column; gap:6px; transition:border-color .2s, background .2s}
.st-choose [role="tab"] small{font-size:.86rem; font-weight:600; color:var(--ink-soft); line-height:1.35}
.st-choose [role="tab"] span{font-family:var(--display); font-weight:800; font-stretch:110%; font-size:clamp(1.15rem,1.7vw,1.45rem); line-height:1.1}
.st-choose [role="tab"]:hover{border-color:var(--teal)}
.st-choose [role="tab"][aria-selected="true"]{background:var(--slate); color:#fff; border-color:var(--slate)}
.st-choose [role="tab"][aria-selected="true"] small{color:var(--aqua)}
.st-choice{display:grid; grid-template-columns:minmax(0,1fr) minmax(0,1fr); gap:0; border-radius:var(--r-lg); overflow:hidden; background:var(--aqua); align-items:stretch}
.st-choice__body{padding:clamp(24px,3.4vw,44px)}
.st-choice__body h3{font-size:clamp(1.5rem,2.4vw,2.1rem)}
.st-choice__body .tag{font-style:italic; font-weight:600; color:var(--logo-teal); margin-bottom:.8em}
.st-choice__img{position:relative; min-height:300px}
.st-choice__img img{position:absolute; inset:0; width:100%; height:100%; object-fit:cover}
@media (max-width:860px){.st-choose{grid-template-columns:1fr} .st-choice{grid-template-columns:1fr} .st-choice__img{min-height:220px; order:-1}}
.st-hub{display:grid; grid-template-columns:minmax(0,1fr) minmax(0,1fr); gap:clamp(28px,5vw,72px); align-items:center}
.st-feats{display:grid; grid-template-columns:repeat(2,minmax(0,1fr)); gap:0 24px; margin:6px 0 24px}
.st-feats div{padding:14px 0; border-top:1px solid var(--line-dark)}
.st-feats b{display:block; font-family:var(--display); font-stretch:106%; color:var(--mint); line-height:1.2; margin-bottom:3px}
.st-feats p{margin:0; font-size:.92rem; color:rgba(255,255,255,.8); line-height:1.45}
.st-wins{position:relative; aspect-ratio:1/1.04}
.st-win{position:absolute; width:70%; padding:0; border:0; border-radius:12px; overflow:hidden; background:#fff; box-shadow:0 30px 60px -24px rgba(0,0,0,.7); cursor:zoom-in; transition:transform .35s cubic-bezier(.2,.7,.2,1); text-align:left}
.st-win:hover,.st-win:focus-visible{transform:rotate(0) scale(1.03); z-index:4}
.st-win__bar{display:flex; align-items:center; gap:10px; height:30px; padding:0 12px; background:var(--aqua); font-family:var(--mono); font-size:.7rem; color:var(--slate); letter-spacing:.04em}
.st-win__bar i{width:9px; height:9px; border-radius:50%; background:rgba(29,65,78,.3); flex:none}
.st-win img{width:100%; aspect-ratio:1200/894; object-fit:cover; object-position:top}
.st-win--1{left:0; top:0; transform:rotate(-3deg); z-index:1}
.st-win--2{right:0; top:21%; transform:rotate(2.5deg); z-index:2}
.st-win--3{left:7%; top:44%; transform:rotate(-1deg); z-index:3}
.st-win__cap{display:block; text-align:right; margin-top:4px; font-family:var(--mono); font-size:.7rem; letter-spacing:.08em; text-transform:uppercase; color:var(--aqua)}
@media (max-width:900px){.st-hub{grid-template-columns:1fr} .st-feats{grid-template-columns:1fr}}
.st-hof{display:grid; grid-template-columns:minmax(0,.55fr) minmax(0,1.45fr); gap:clamp(24px,5vw,72px); align-items:center}
.st-hof__img{position:relative}
.st-hof__img img{border-radius:var(--r-lg); width:100%; aspect-ratio:4/5; object-fit:cover}
.st-hof__img .daisy{position:absolute; right:-16px; top:-16px; width:70px; height:70px; color:var(--mint)}
@media (max-width:760px){.st-hof{grid-template-columns:1fr} .st-hof__img{max-width:300px}}
.st-email{display:flex; flex-wrap:wrap; gap:12px; align-items:center; margin:6px 0 0}
'''

def clubs():
    choices = [
        ('new', 'If there’s nothing like this at your school yet', 'Start a new chapter', 'Bring SafeBAE to your school for the first time',
         'Start a SafeBAE chapter from the ground up. Find an advisor, register your club, recruit your team, and use the Club Hub to plan meetings, activities, and events throughout the year.',
         'img-6834', 'A group of SafeBAE youth leaders together outdoors'),
        ('affiliate', 'Student council, a wellness club, an affinity group', 'Affiliate an existing club', 'Bring SafeBAE into a club that’s already active',
         'Add SafeBAE to the work your club is already doing. Register as an affiliate, get access to the Club Hub, and use our activities, campaigns, and resources as part of your existing programming.',
         'img-9509-1', 'Students making hand-lettered consent posters'),
        ('restart', 'If your school used to have one', 'Restart a previous chapter', 'Bring your school’s SafeBAE chapter back',
         'Pick up where a previous SafeBAE chapter left off. Re-register your chapter, reconnect with an advisor and students, and use the Club Hub to get meetings, activities, and events going again.',
         '000422', 'A large group of students in SafeBAE shirts on school steps'),
    ]
    tabs = ''.join(f'<button role="tab" id="{k}" aria-controls="p-{k}" aria-selected="{str(i==0).lower()}" tabindex="{0 if i==0 else -1}"><span>{esc(t)}</span><small>{esc(ifl)}</small></button>' for i, (k, ifl, t, *_r) in enumerate(choices))
    panels = ''.join(f'''<div class="st-choice" role="tabpanel" id="p-{k}" aria-labelledby="{k}"{'' if i==0 else ' hidden'}>
      <div class="st-choice__body"><h3>{esc(t)}</h3><p class="tag">{esc(tag)}</p><p>{esc(d)}</p><p class="small muted">All three register through the same form and get the same Hub access and support. {a('Register below', '#register', 'link')}.</p></div>
      <div class="st-choice__img">{img(im, alt)}</div></div>''' for i, (k, ifl, t, tag, d, im, alt) in enumerate(choices))
    feats = [
        ('Find Your Next Action', 'Figure out what your chapter should do next.'),
        ('Awareness Event Library', 'Event ideas, plus tools for planning your year.'),
        ('Step-By-Step Guides', 'For running meetings and organizing events.'),
        ('Prevention Poster Builder', 'Create posters with your school’s support resources.'),
        ('Guides for Running Your Chapter', 'From finding an advisor and recruiting members to getting media attention and preparing the next group of leaders.'),
        ('And more', 'New tools, activities, and resources are added to the Club Hub throughout the year.'),
    ]
    feats_html = ''.join(f'<div><b>{esc(t)}</b><p>{esc(d)}</p></div>' for t, d in feats)
    wins = [('clubhub1', 'Find Your Next Action'), ('clubhub2', 'Awareness Event Library'), ('clubhub3', 'Build Your Calendar of Engagement')]
    wins_html = ''.join(f'<button class="st-win st-win--{i+1}" data-src="{imgsrc(n)}" data-cap="Club Hub: {esc(c)}" aria-label="Enlarge screenshot: {esc(c)}"><span class="st-win__bar"><i></i><i></i><i></i>clubs.safebae.org</span>{img(n, "Club Hub screen: " + c)}</button>' for i, (n, c) in enumerate(wins))

    body = f'''
{phero_alt(phero('Start a SafeBAE club at your school', 'A SafeBAE club is a student-run chapter that brings consent and healthy relationship education to your school. You decide what your chapter does. We provide the training and materials, and our team is a quick email away when you need help. Registration is free.',
       'SafeBAE Clubs', crumbs=[('Home','index.html'),('Students','students.html'),('Clubs',None)], kind='teal', media='clubhero', sticker='Registration is free',
       actions=btn('Register your club', CLUB_FORM, 'mint') + btn('Already registered? Club Hub', CLUB_HUB, 'ghost')), 'clubhero', 'SafeBAE club members together at the beach')}

<section class="band band--paper" id="ways">
  <div class="wrap">
    <div class="section-head"><div><p class="eyebrow">Three ways a club joins</p><h2>Which one fits your school?</h2><p class="lede lede--full">Start from scratch, restart a previous chapter, or add SafeBAE to a club you already run. The Club Hub walks you through each one step by step.</p></div></div>
    <div data-tabs="clubway"><div class="st-choose" role="tablist" aria-label="Ways to join">{tabs}</div>{panels}</div>
  </div>
</section>

<section class="band band--slate" id="club-hub">
  <div class="wrap st-hub">
    <div>
      <p class="eyebrow">Members only</p>
      <h2>Registering unlocks the Club Hub</h2>
      <p style="color:rgba(255,255,255,.86)">The Club Hub is the members-only site for registered SafeBAE chapters. Access is free and renews with your registration each school year. Inside, you’ll find:</p>
      <div class="st-feats">{feats_html}</div>
      <div class="btns">{btn('Register to get access', CLUB_FORM, 'mint')}{btn('Open the Club Hub', CLUB_HUB, 'ghost')}</div>
    </div>
    <div data-gallery><div class="st-wins">{wins_html}</div><span class="st-win__cap">Tap a screen to enlarge</span></div>
  </div>
</section>

<section class="band band--aqua">
  <div class="wrap split">
    <figure class="st-photo">{img('clubtabling', 'A SafeBAE club table with red, yellow, and green flags, Can I Kiss You? buttons, and Vibe Check cards')}<span class="sticker sticker--coral" style="left:auto;right:16px;bottom:auto;top:-14px">Can I kiss you?</span><figcaption>A SafeBAE club table with red, yellow and green flags, “Can I Kiss You?” buttons and Vibe Check cards.</figcaption></figure>
    <div>
      <p class="eyebrow">What clubs do</p>
      <h2>You decide what your chapter does</h2>
      <p>Meetings, awareness events, campaigns, posters for your school: your chapter sets the plan. Members get the Club Hub, virtual training sessions with the SafeBAE team, and free materials.</p>
      <p>After an event, send us photos and a couple of sentences. We share chapters’ work with clubs at other schools and on our social media, and we credit your club and school.</p>
      <div class="rows" style="margin-top:18px">
        {row('Get your leaders certified', 'The free Certified Peer Educator Training, 16 modules.', 'peer-educator.html')}
        {row('Practice in the BAE Skills Lab', 'Interactive activities for peer educators and club leaders.', SKILLS)}
        {row('Free prevention posters', 'Download and print for your school.', 'posters.html')}
      </div>
    </div>
  </div>
</section>

<section class="band band--deep">
  <div class="wrap st-hof">
    <div class="st-hof__img">{img('dorie', 'Dorie McNamara')}<span class="daisy"></span></div>
    <div>
      <p class="eyebrow">From the Hall of Fame</p>
      <blockquote class="quote">So many of my own friends had no idea what their rights are under Title IX… Starting the club and getting more students started on the training has made a great impact on not just myself but my entire Central community.</blockquote>
      <span class="cite"><b style="color:#fff">Dorie McNamara</b> &middot; <span style="color:var(--aqua)">Former chapter lead and Certified Peer Educator at Central Catholic High School, now on SafeBAE’s Board of Directors</span></span>
    </div>
  </div>
</section>

<section class="band band--paper">
  <div class="wrap">
    <div class="section-head"><div><p class="eyebrow">Help from our team</p><h2>Questions, challenges or event ideas?</h2><p class="lede lede--full">Students and faculty advisors can both reach out to SafeBAE’s programming team.</p></div></div>
    <div class="st-duo">
      <div class="st-box st-box--white"><h3>Email the team</h3><p class="muted">Our team is a quick email away when you need help.</p>
        <div class="st-email"><span class="copy">{CLUB_EMAIL}<button data-copy="{CLUB_EMAIL}">Copy</button></span></div>
        <div class="btns">{btn('Email the team', 'mailto:' + CLUB_EMAIL, 'slate')}</div></div>
      <div class="st-box st-box--aqua"><h3>Book a virtual meeting</h3><p>Pick a 30-minute slot with our programming team to talk through your chapter’s plans.</p>
        <div class="btns">{btn('Book a meeting', CALENDLY, 'slate')}</div></div>
    </div>
  </div>
</section>

<section class="band band--mint" id="register">
  <div class="wrap split">
    <div>
      <h2>Registration takes a few minutes</h2>
      <p class="lede">It’s free and renews each school year. Once you register, you’ll get access to the Club Hub and be connected with your point of contact on the SafeBAE team.</p>
      <div class="btns">{btn('Register your club', CLUB_FORM, 'slate')}{btn('Already registered? Club Hub', CLUB_HUB, 'ghost')}</div>
    </div>
    <div class="st-box st-box--white">
      <h3>Joining a club that’s already registered?</h3>
      <p class="muted">You don’t need to register the club again. Create your own Club Hub account instead. Need help? Email {a(CLUB_EMAIL, 'mailto:' + CLUB_EMAIL, 'link')}.</p>
      <div class="btns">{btn('Create a Club Hub account', CLUB_HUB, 'teal')}</div>
    </div>
  </div>
</section>

<section class="band band--paper">
  <div class="wrap">
    <div class="section-head"><div><p class="eyebrow">Where clubs fit</p><h2>From learning to changing policy</h2><p class="lede lede--full">In college? {a('Start a SafeBAE club on your campus', 'college.html', 'link')} and mentor high school chapters.</p></div></div>
    {journey('Lead')}
  </div>
</section>
{give_band()}
'''
    page('clubs.html', 'SafeBAE Clubs · SafeBAE', 'Start a student club and lead sexual violence prevention at your school. Access free resources, trainings, and a national network of student leaders.',
         body, active='students', body_class='st st-clubs', head_extra=f'<style>{CSS}{CLUB_CSS}</style>')


# ================================================================= reform-policy.html
RP_CSS = '''
.st-rhero{background:var(--aqua); color:var(--slate); position:relative; overflow:hidden}
.st-rhero .crumbs{color:var(--ink-soft)} .st-rhero .crumbs a{color:var(--logo-teal)}
.st-rhero .wrap{display:grid; grid-template-columns:minmax(0,1.3fr) minmax(0,.7fr); gap:clamp(28px,5vw,72px); align-items:center; padding-block:clamp(48px,6vw,88px)}
.st-rhero h1{font-size:clamp(2.3rem,5vw,4.6rem); font-stretch:122%; font-weight:900; text-transform:uppercase; line-height:.93; letter-spacing:-.02em; margin-bottom:.4em}
.st-rhero .eyebrow{color:var(--logo-teal)}
.st-cover{position:relative; max-width:360px; margin-inline:auto}
.st-cover img{width:100%; border-radius:6px; transform:rotate(3deg); box-shadow:0 34px 60px -24px rgba(22,53,64,.6), 0 0 0 1px rgba(29,65,78,.12)}
.st-cover .sticker{position:absolute; left:-18px; bottom:12%}
@media (max-width:860px){.st-rhero .wrap{grid-template-columns:1fr} .st-cover{max-width:240px; margin:8px 0 0 12px}}
.band--slate .tl__item h3{color:#fff}
.st-strong{margin-top:clamp(28px,4vw,44px); padding:clamp(22px,3vw,34px); border-radius:var(--r-lg); background:var(--mint); color:var(--slate); display:flex; flex-wrap:wrap; gap:14px 30px; align-items:center; justify-content:space-between}
.st-strong p{margin:0; font-family:var(--display); font-weight:800; font-stretch:110%; font-size:clamp(1.3rem,2.4vw,2rem); line-height:1.15; max-width:30ch}
.st-strong span{display:block; font-family:var(--body); font-weight:500; font-size:1rem; margin-top:8px}
.st-who{display:flex; flex-wrap:wrap; gap:8px; margin:6px 0 18px}
.st-who .chip{font-size:.78rem; padding:.45em .8em}
.st-rights{display:grid; grid-template-columns:repeat(3,minmax(0,1fr)); gap:clamp(14px,2vw,22px)}
@media (max-width:860px){.st-rights{grid-template-columns:1fr}}
'''

def reform_policy():
    body = f'''
<section class="st-rhero">
  <div class="wrap">
    <div>
      {crumbs(('Students', 'students.html'), ('Reform Your School’s Policy', None))}
      <p class="eyebrow">Student Policy Reform Guide</p>
      <h1>Reform your school’s sexual misconduct policy</h1>
      <p class="lede">Protecting your school community starts with strong, trauma-informed policies. SafeBAE’s Student Policy Reform Guide is a step-by-step resource to help you advocate for safer, trauma-informed and survivor-centered policies in your district.</p>
      <div class="btns">{btn('Register for the guide', '#register', 'slate', arrow=True)}{btn('Know your Title IX rights', 'title-ix.html', 'ghost')}</div>
    </div>
    <div class="st-cover">{img('2024-updates-safebae-sexual-misconduct-policy-reform-a-stude', 'Cover of the SafeBAE Sexual Misconduct Policy Reform Guide: A Guide for Students in How to Create a Model Policy, 2024 update', loading='eager')}<span class="sticker">Free for students</span></div>
  </div>
</section>

<section class="band band--slate">
  <div class="wrap">
    <div class="section-head"><div><p class="eyebrow">Why it matters now</p><h2>Federal protections keep shifting</h2><p class="lede lede--full" style="color:rgba(255,255,255,.85)">Since 2020, shifting federal Title IX rules have left survivors vulnerable and school districts facing legal risk.</p></div></div>
    <div class="tl">
      <div class="tl__item"><div class="tl__year">2020</div><div><h3>A harmful Title IX rule</h3><p>The 2020 Title IX rule issued by the Department of Education was widely recognized as harmful. It narrowed protections for survivors, restricted schools’ ability to respond effectively, and put students at greater risk of further harm.</p></div></div>
      <div class="tl__item"><div class="tl__year">2024</div><div><h3>New guidelines, challenged in court</h3><p>New guidelines were introduced in 2024 to restore protections. They were quickly challenged in court, and schools nationwide have been forced back under the restrictive 2020 rule.</p></div></div>
      <div class="tl__item"><div class="tl__year">Now</div><div><h3>Weak, inconsistent enforcement</h3><p>With the Department of Education weakened and inconsistent in its enforcement, survivors are left vulnerable and districts face heightened legal risks due to vague and harmful federal standards.</p></div></div>
    </div>
    <div class="st-strong"><p>Together, we can strengthen protections for students and make schools safer across the country.</p>{btn('Register for the guide', '#register', 'slate', arrow=True)}</div>
  </div>
</section>

<section class="band band--paper">
  <div class="wrap split split--top">
    <div>
      <p class="eyebrow">The guide</p>
      <h2>A step&#8209;by&#8209;step guide for students</h2>
      <p class="lede">SafeBAE created the Student Policy Reform Guide to help you advocate for safer, trauma-informed, and survivor-centered policies in your district.</p>
      <p class="st-label" style="color:var(--logo-teal)">Who can use it</p>
      <div class="st-who">{chips(['Students', 'Parents', 'Community stakeholders'], 'slate')}</div>
      <p>Use it to push for clarity, accountability, and real protection in your schools.</p>
    </div>
    <div>
      <p class="eyebrow">How it works</p>
      <ol class="st-vsteps">
        <li><span class="n">1</span><div><b>Register</b><p>Fill out the short form below to receive the guide.</p></div></li>
        <li><span class="n">2</span><div><b>Get the guide and adjoining resources</b><p>Free access to the guide, a resource for students on how to create a model policy.</p></div></li>
        <li><span class="n">3</span><div><b>Advocate in your district</b><p>Use the guide to push for clarity, accountability, and real protection in your schools.</p></div></li>
        <li><span class="n">4</span><div><b>Keep in touch</b><p>Let SafeBAE know about your progress as you work with your school or district.</p></div></li>
      </ol>
    </div>
  </div>
</section>

<section class="band band--mist" id="register">
  <div class="wrap st-reg">
    <div>
      <p class="eyebrow">Free for students</p>
      <h2>Register to get the guide</h2>
      <p class="lede">We ask only that you register to receive the guide and keep in touch with us about your progress.</p>
      <p class="muted">Administrator, teacher or district leader? SafeBAE has a separate {a('School Policy Reform Guide for administrators', 'policy-reform-guide.html', 'link')}.</p>
    </div>
    <div class="st-embed">{embed(POLICY_FORM + '?embedded=true', POLICY_FORM, 'Register to receive the Student Policy Reform Guide', height=1100, title='Student Policy Reform Guide registration')}</div>
  </div>
</section>

<section class="band band--paper">
  <div class="wrap">
    <div class="section-head"><div><p class="eyebrow">Start with your rights</p><h2>Know your rights under Title IX</h2><p class="lede lede--full">Title IX is the federal law that bars sex discrimination, including sexual harassment and assault, at any school that takes federal funding.</p></div>{btn('Title IX basics', 'title-ix.html', 'slate', arrow=True)}</div>
    <div class="st-rights">
      <a class="card" href="title-ix.html"><div class="card__body"><span class="chip" style="align-self:flex-start">Rights</span><h3>Know your rights</h3><p>Your right to report, to supportive measures like a schedule change, and to a prompt, fair investigation.</p><span class="card__foot arrow-link">Title IX</span></div></a>
      <a class="card" href="title-ix.html"><div class="card__body"><span class="chip" style="align-self:flex-start">Coverage</span><h3>Find your coordinator</h3><p>Learn whether your school is covered by Title IX, and how to find your school’s Title IX Coordinator.</p><span class="card__foot arrow-link">Title IX</span></div></a>
      <a class="card card--aqua" href="#register"><div class="card__body"><span class="chip chip--mint" style="align-self:flex-start">This guide</span><h3>Understand and change your school’s policy</h3><p>What your school’s sexual misconduct policy says, what a strong one should include, and how to advocate for change.</p><span class="card__foot arrow-link">Get the guide</span></div></a>
    </div>
    <div class="st-links" style="margin-top:clamp(28px,4vw,40px)">
      <div class="rows">{row('Learn it in the Peer Educator Training', 'Module 10 covers reporting options and investigation requirements; Module 11 covers your rights in school.', 'peer-educator.html#modules')}{row('Organize with a SafeBAE club', 'Campaigns, events and support from the Club Hub.', 'clubs.html')}</div>
      <div class="rows">{row('Policy Reform at the Summer Activist Institute', 'Title IX and Policy Reform were sessions at the 2024 institute.', 'summer-institute.html#schedule')}{row('Bring policy support to your school', 'SafeBAE 360° Schools includes hands-on policy consultation.', '360-schools.html')}</div>
    </div>
    <div style="margin-top:clamp(24px,3vw,34px)">{st_help()}</div>
  </div>
</section>

<section class="band band--mint band--tight">
  <div class="wrap">
    <div class="section-head"><div><p class="eyebrow">The student path</p><h2>Where policy change fits</h2></div></div>
    {journey('Change')}
  </div>
</section>
{give_band()}
'''
    page('reform-policy.html', 'Reform Your School’s Policy · SafeBAE', 'Advocate for school policy reform on sexual violence. Learn how to reform Title IX and misconduct policies with SafeBAE’s student-led guide.',
         body, active='students', body_class='st st-reform', head_extra=f'<style>{CSS}{RP_CSS}</style>')


# ================================================================= summer-institute.html
SI_CSS = '''
.st-ihero{position:relative; overflow:hidden; background:var(--slate); color:#fff}
.st-ihero__bg{position:absolute; inset:0}
.st-ihero__bg img{width:100%; height:100%; object-fit:cover; opacity:.32}
.st-ihero__bg::after{content:""; position:absolute; inset:0; background:linear-gradient(90deg, var(--slate) 0%, rgba(29,65,78,.88) 48%, rgba(29,65,78,.4) 100%)}
.st-ihero .wrap{position:relative; z-index:2; padding-block:clamp(56px,7vw,100px) clamp(40px,5vw,64px)}
.st-ihero h1{font-size:clamp(2.6rem,6.4vw,6.2rem); font-stretch:125%; font-weight:900; text-transform:uppercase; line-height:.88; letter-spacing:-.02em; margin:0 0 .35em}
.st-ihero h1 span{display:block}
.st-ihero .lede{color:rgba(255,255,255,.9); max-width:none}
.st-count{display:flex; flex-wrap:wrap; gap:10px; margin-top:28px}
.st-count a{display:flex; align-items:baseline; gap:10px; padding:12px 16px; border-radius:12px; border:2px solid rgba(209,254,255,.3); text-decoration:none; color:#fff; transition:border-color .2s, background .2s}
.st-count a:hover{border-color:var(--mint); background:rgba(21,255,200,.08)}
.st-count b{font-family:var(--display); font-weight:900; font-stretch:120%; font-size:2rem; line-height:1; color:var(--mint)}
.st-count span{font-family:var(--mono); font-size:.72rem; letter-spacing:.08em; text-transform:uppercase}
.st-ftabs{display:flex; flex-wrap:wrap; gap:8px; margin-bottom:24px}
.st-fgrid{display:grid; grid-template-columns:repeat(var(--cols,5),minmax(0,1fr)); gap:20px 14px; list-style:none; padding:0; margin:0}
.st-fgrid--9{--cols:9}
.st-fellow{margin:0; min-width:0}
.st-fellow img{width:100%; aspect-ratio:4/5; object-fit:cover; object-position:center 28%; border-radius:12px; background:var(--mist); margin-bottom:9px; transition:transform .3s, box-shadow .3s}
.st-fellow:hover img{transform:translateY(-4px) rotate(-1.5deg); box-shadow:0 0 0 3px var(--mint), 0 18px 30px -18px rgba(0,0,0,.5)}
.st-fellow b{display:block; font-family:var(--display); font-stretch:104%; line-height:1.2; font-size:.98rem}
.st-fellow small{display:block; color:var(--ink-soft); font-size:.8rem; line-height:1.3; margin-top:2px}
.st-fellow small.ret{color:var(--teal); font-weight:700}
@media (max-width:1100px){.st-fgrid--9{--cols:6}}
@media (max-width:760px){.st-fgrid,.st-fgrid--9{--cols:3; gap:16px 10px} .st-fellow b{font-size:.88rem}}
.st-sched{display:grid; grid-template-columns:minmax(0,1.25fr) minmax(0,.75fr); gap:clamp(24px,4vw,56px); align-items:start}
.st-day{list-style:none; margin:0; padding:0; border-top:1px solid var(--line-dark)}
.st-day li{display:grid; grid-template-columns:92px minmax(0,1fr) auto; gap:6px 16px; align-items:center; padding:12px 0; border-bottom:1px solid var(--line-dark); margin:0}
.st-day time{font-family:var(--mono); font-size:.82rem; font-weight:600; color:var(--mint)}
.st-day b{font-family:var(--display); font-stretch:106%; font-size:1.12rem; line-height:1.2}
.st-day li.meal b{font-family:var(--body); font-weight:500; font-size:.98rem; color:rgba(255,255,255,.7)}
.st-day .t{display:flex; gap:6px; flex-wrap:wrap; justify-content:flex-end}
.st-day .t span{font-family:var(--mono); font-size:.66rem; letter-spacing:.06em; text-transform:uppercase; padding:3px 7px; border-radius:4px; border:1px solid rgba(209,254,255,.35); color:var(--aqua); white-space:nowrap}
.st-day .t a{font-family:var(--mono); font-size:.66rem; letter-spacing:.06em; text-transform:uppercase; padding:3px 7px; border-radius:4px; background:var(--mint); color:var(--slate); text-decoration:none; white-space:nowrap}
@media (max-width:620px){.st-day li{grid-template-columns:74px minmax(0,1fr)} .st-day .t{grid-column:2; justify-content:flex-start}}
.st-poster{display:block; width:100%; border:0; padding:0; background:none; cursor:zoom-in; border-radius:14px; overflow:hidden; box-shadow:0 30px 60px -28px rgba(0,0,0,.7); transform:rotate(2deg); transition:transform .3s}
.st-poster:hover{transform:rotate(0) scale(1.02)}
.st-poster img{width:100%}
@media (max-width:900px){.st-sched{grid-template-columns:1fr} .st-poster{max-width:340px}}
.st-ep{display:grid; grid-template-columns:minmax(0,1.2fr) minmax(0,.8fr); gap:clamp(24px,4vw,60px); align-items:center}
@media (max-width:860px){.st-ep{grid-template-columns:1fr}}
'''

SCHED = {
  'tue': ('Tuesday, June 25', '24sumact', [
      ('8:30 AM', 'Yoga', [], 1), ('9:20 AM', 'Breakfast', [], 0), ('10:35 AM', 'Introductions & Self Care', [], 1), ('11:10 AM', 'Theories of Change', ['Group debrief'], 1),
      ('12:30 PM', 'Lunch', [], 0), ('1:35 PM', 'Title IX', ['Group debrief', ('Title IX', 'title-ix.html')], 1), ('2:55 PM', 'Sex Education', ['Break'], 1),
      ('4:50 PM', 'Professional Development', ['Break'], 1), ('6:00 PM', 'Dinner', [], 0), ('7:00 PM', 'Fun Activity!', [], 1)]),
  'wed': ('Wednesday, June 26', '24sumact2', [
      ('8:30 AM', 'Lighthouse Walk', [], 1), ('9:20 AM', 'Breakfast', ['Group debrief'], 0), ('11:10 AM', 'Centering the Margins', ['Break'], 1),
      ('12:20 PM', 'Storytelling for Change', [], 1), ('1:30 PM', 'Lunch/Break', [], 0), ('2:35 PM', 'Policy Reform', ['Break', ('Guide', 'reform-policy.html')], 1),
      ('4:00 PM', 'Engaging Men in the Convo', ['Break & debrief'], 1), ('5:45 PM', 'Self Care (part 2)', [], 1), ('6:00 PM', 'Dinner', [], 0), ('7:00 PM', 'Fun Activity!', [], 1)]),
}

def fellow_card(name, slug, note=''):
    pos = {'lilliana-kh': 'center 20%', 'matteo-netto': 'center 22%', 'mara-scott': 'center 50%', 'tristan-greene-headshot': 'center 45%',
           'taniyah-jackson': 'center 40%', '30125793-52af-484d-8046-f75d312bcfbe-cathy-w': 'center 35%', 'img-4121-britney-cunningham': '60% center'}.get(slug)
    st = f'object-position:{pos}' if pos else ''
    cls = ' class="ret"' if note.startswith('Also') else ''
    return f'<li class="st-fellow">{img(slug, name, style=st)}<b>{esc(name)}</b>' + (f'<small{cls}>{esc(note)}</small>' if note else '') + '</li>'

def summer_institute():
    p25 = ''.join(fellow_card(n.replace(' NJ', ''), s, 'NJ' if n.endswith(' NJ') else '') for n, s in F2025)
    p24 = ''.join(fellow_card(*f) for f in F2024)
    p23 = ''.join(fellow_card(*f) for f in F2023)
    cohorts = [('f2025', '2025 Fellows', p25, 'st-fgrid--9', len(F2025)), ('f2024', '2024 Fellows', p24, 'st-fgrid--9', len(F2024)), ('f2023', '2023 Fellows', p23, 'st-fgrid--9', len(F2023))]
    tabs = ''.join(f'<button class="tab" role="tab" id="{k}" aria-controls="p-{k}" aria-selected="{str(i==0).lower()}" tabindex="{0 if i==0 else -1}">{esc(lbl)} <span class="mono" style="font-size:.75rem;opacity:.75">{n}</span></button>' for i, (k, lbl, _p, _c, n) in enumerate(cohorts))
    panels = ''.join(f'<div role="tabpanel" id="p-{k}" aria-labelledby="{k}"{"" if i==0 else " hidden"}><ul class="st-fgrid {c}">{p}</ul></div>' for i, (k, lbl, p, c, n) in enumerate(cohorts))

    def day_rows(rows):
        out = []
        for t, s, tags, sess in rows:
            tg = ''.join((f'<a href="{x[1]}">{esc(x[0])} &rarr;</a>' if isinstance(x, tuple) else f'<span>{esc(x)}</span>') for x in tags)
            out.append(f'<li class="{"" if sess else "meal"}"><time>{t}</time><b>{esc(s)}</b><span class="t">{tg}</span></li>')
        return '<ol class="st-day">' + ''.join(out) + '</ol>'
    stabs = ''.join(f'<button class="tab" role="tab" id="d-{k}" aria-controls="dp-{k}" aria-selected="{str(i==0).lower()}" tabindex="{0 if i==0 else -1}">{esc(v[0])}</button>' for i, (k, v) in enumerate(SCHED.items()))
    spanels = ''.join(f'''<div role="tabpanel" id="dp-{k}" aria-labelledby="d-{k}"{"" if i==0 else " hidden"}><div class="st-sched">{day_rows(v[2])}
      <div data-gallery><button class="st-poster" data-src="{imgsrc(v[1])}" data-cap="2024 Activist Institute schedule: {esc(v[0])}" aria-label="Enlarge the {esc(v[0])} schedule poster">{img(v[1], f"Activist Institute schedule poster for {v[0]}, 2024")}</button></div></div></div>''' for i, (k, v) in enumerate(SCHED.items()))

    body = f'''
<section class="st-ihero">
  <div class="st-ihero__bg">{img('sumact5', '', loading='eager')}</div>
  <div class="wrap">
    {crumbs(('Students', 'students.html'), ('Summer Activist Institute', None))}
    <p class="eyebrow" style="color:var(--mint)">SafeBAE Summer Activist Institute</p>
    <h1><span>Meet the</span><span class="mint">fellows</span></h1>
    <p class="lede">Fellows of SafeBAE’s Summer Activist Institute from 2023, 2024 and 2025. The 2024 institute ran two days of sessions on theories of change, Title IX, sex education, policy reform, storytelling for change and engaging men in the conversation.</p>
    <div class="st-count"><a href="#f2025"><b>{len(F2025)}</b><span>2025 fellows</span></a><a href="#f2024"><b>{len(F2024)}</b><span>2024 fellows</span></a><a href="#f2023"><b>{len(F2023)}</b><span>2023 fellows</span></a><a href="#episode"><b>&#9654;</b><span>Watch an episode</span></a></div>
  </div>
</section>

<section class="band band--paper" id="fellows">
  <div class="wrap">
    <div class="section-head"><div><p class="eyebrow">Cohorts</p><h2>The fellows</h2></div></div>
    <div data-tabs="fellows"><div class="tabs" role="tablist" aria-label="Fellows by year">{tabs}</div>{panels}</div>
  </div>
</section>

<section class="band band--slate" id="schedule">
  <div class="wrap">
    <div class="section-head"><div><p class="eyebrow">June 2024 &middot; Activist Institute</p><h2>Two days at the 2024 institute</h2><p class="lede lede--full" style="color:rgba(255,255,255,.85)">Each day started with yoga or a lighthouse walk and ended with dinner and a fun activity.</p></div></div>
    <div data-tabs="sched"><div class="tabs" role="tablist" aria-label="Schedule by day">{stabs}</div>{spanels}</div>
  </div>
</section>

<section class="band band--teal" id="episode">
  <div class="wrap st-ep">
    {yt('4sr3NAPzqs0', '2023 Summer Activist Institute: Episode 3', label='Episode 3')}
    <div>
      <p class="eyebrow">From the 2023 institute</p>
      <h2>Watch an episode</h2>
      <p class="lede" style="color:rgba(255,255,255,.9)">Episode 3 of SafeBAE’s 2023 Summer Activist Institute series.</p>
      <figure class="st-photo" style="margin-top:22px">{img('2023-institute-selfie', 'A group selfie of fellows at the 2023 Summer Activist Institute')}<figcaption style="color:#fff">The 2023 institute</figcaption></figure>
      <div class="btns" style="margin-top:20px">{btn('SafeBAE on YouTube', 'https://www.youtube.com/@SafeBAE', 'mint')}</div>
    </div>
  </div>
</section>

<section class="band band--paper">
  <div class="wrap">
    <div class="section-head"><div><p class="eyebrow">Lead at your school</p><h2>Ways to lead at your school</h2><p class="lede lede--full">The Peer Educator Training, SafeBAE clubs and the Student Policy Reform Guide are open to students now.</p></div></div>
    {journey()}
  </div>
</section>
{give_band()}
'''
    page('summer-institute.html', 'Summer Activist Institute · SafeBAE', 'Meet the fellows of the SafeBAE Summer Activist Institute and see the 2024 institute schedule.',
         body, active='students', body_class='st st-si', head_extra=f'<style>{CSS}{SI_CSS}</style>')


# ================================================================= espanol.html
ES_MODULES = ['Cultura de la Violación y cómo puede ayudar a cambiar a una cultura de respeto', 'Definiendo: Acoso Sexual, Agresión y Violación', 'Consentimiento',
              'Relaciones Saludables', 'Jóvenes Identificados como hombres y Violencia Sexual', 'Mitos, Datos y Estadísticas', 'Relaciones y Violencia Sexual en los Medios',
              'Seguridad en Línea y el Envío de Fotos Íntimas', 'Si Has Sido Acusado', 'Cómo apoyar a un sobreviviente', 'Opciones para Denunciar y Requisitos de Investigación',
              'Recuperación después de Violencia Sexual', 'Título IX: Derechos en la Escuela', 'Intervención del Espectador',
              'Relaciones de Pareja Después de Experimentar Violencia Sexual', 'Hablar en Público: Consejos para Presentar']

ES_CSS = '''
.st-es{position:relative; overflow:hidden; background:var(--logo-teal); color:#fff}
.st-es__flower{position:absolute; right:-8%; top:-18%; width:min(640px,70vw); height:min(640px,70vw); color:rgba(21,255,200,.1); pointer-events:none}
.st-es__flower .daisy{width:100%; height:100%; animation:st-spin 90s linear infinite}
@keyframes st-spin{to{transform:rotate(360deg)}}
.st-es .wrap{position:relative; z-index:2; display:grid; grid-template-columns:minmax(0,1.15fr) minmax(0,.85fr); gap:clamp(28px,5vw,64px); align-items:center; padding-block:clamp(52px,7vw,96px)}
.st-es h1{font-size:clamp(2.6rem,6vw,5.6rem); font-stretch:125%; font-weight:900; text-transform:uppercase; line-height:.9; letter-spacing:-.02em; margin:0 0 .35em}
.st-es h1 span{display:block}
.st-es .lede{color:rgba(255,255,255,.92); max-width:none}
.st-es .link{color:var(--mint)}
.st-es__sub{font-family:var(--display); font-weight:800; font-stretch:112%; font-size:clamp(1.3rem,2.3vw,2rem); line-height:1.15; color:var(--mint); margin:-.2em 0 .8em}
.st-es .crumbs a{color:var(--aqua)}
@media (max-width:860px){.st-es .wrap{grid-template-columns:1fr}}
.st-track{list-style:none; margin:0; padding:0; display:grid; grid-template-columns:repeat(6,minmax(0,1fr)); gap:14px}
.st-track li{position:relative; margin:0; background:#fff; border:1px solid var(--line); border-radius:14px; padding:18px 16px; min-width:0; display:flex; flex-direction:column; gap:8px}
.st-track li:not(:last-child)::after{content:""; position:absolute; top:38px; right:-14px; width:14px; height:4px; background:var(--teal)}
.st-track .n{font-family:var(--display); font-weight:900; font-stretch:125%; font-size:2.4rem; line-height:1; color:var(--teal)}
.st-track b{font-family:var(--display); font-stretch:104%; font-size:1.05rem; line-height:1.22}
.st-track a{font-weight:700; color:var(--logo-teal)}
@media (max-width:1000px){.st-track{grid-template-columns:repeat(3,minmax(0,1fr))} .st-track li:nth-child(3)::after{display:none}}
@media (max-width:560px){.st-track{grid-template-columns:1fr; gap:8px} .st-track li{display:grid; grid-template-columns:44px minmax(0,1fr); align-items:center; gap:2px 12px; padding:14px 16px} .st-track li .n{grid-row:1/3; font-size:2rem} .st-track li::after{display:none}}
.st-facts3{display:grid; grid-template-columns:repeat(3,minmax(0,1fr)); gap:10px}
.st-facts3 div{background:#fff; border-radius:12px; padding:16px; border:1px solid var(--line)}
.st-facts3 b{display:block; font-family:var(--display); font-weight:900; font-stretch:120%; font-size:1.9rem; line-height:1; color:var(--logo-teal); margin-bottom:6px}
.st-facts3 span{font-size:.9rem; font-weight:600; color:var(--ink-soft)}
@media (max-width:620px){.st-facts3{grid-template-columns:1fr}}
.st-warn{display:flex; gap:16px; align-items:flex-start; padding:20px 22px; border-radius:14px; background:#fff1f1; border:2px solid var(--coral); margin-bottom:clamp(22px,3vw,30px)}
.st-warn b{display:block; font-family:var(--display); font-stretch:106%; font-size:1.1rem; margin-bottom:4px}
.st-warn p{margin:0}
'''

def espanol():
    mods = ''.join(f'<li class="st-mod"><span class="st-mod__n">{i+1}</span><span class="st-mod__t">{esc(t)}</span></li>' for i, t in enumerate(ES_MODULES))
    steps = ['<b>Registrarse.</b><a href="#registro">¡Haga clic aquí!</a>', '<b>Crear un usuario en el Portal de Educación.</b>', '<b>Realizar los 16 módulos a su propio ritmo.</b>',
             '<b>Tomar la Encuesta Final.</b>', '<b>Programar una reunión individual con los directores juveniles.</b>', '<b>¡Obtener el certificado y empezar a educar!</b>']
    steps_html = ''.join(f'<li><span class="n">{i+1}</span>{s}</li>' for i, s in enumerate(steps))
    es_embed = (f'<div class="embed" data-embed="{esc(ES_FORM)}?embedded=true" data-h="1300" data-title="Registro: entrenamiento en español">'
                f'<div class="embed__fallback note"><p><b>Registro para el entrenamiento en español</b></p>{btn("Abrir el formulario", ES_FORM + "?usp=sharing", "teal")}</div></div>')
    es_help = (f'<div class="helpline"><div><b>¿Necesita hablar con alguien ahora? Ayuda gratuita y confidencial, 24/7</b>'
               f'<span>Crisis Text Line: envíe HOLA al 741741 &middot; SAMHSA: 1-800-662-4357 (inglés y español) &middot; Si está en peligro inmediato, llame al 911.</span></div>'
               f'<button class="btn btn--coral btn--sm" data-open-help>Todas las líneas de ayuda (en inglés)</button></div>')
    body = f'''<div lang="es">
<section class="st-es">
  <div class="st-es__flower" aria-hidden="true"><span class="daisy"></span></div>
  <div class="wrap">
    <div>
      <nav class="crumbs" aria-label="Ruta de navegación"><a href="index.html">Inicio</a><span>/</span><a href="students.html">Estudiantes</a><span>/</span><span>En español</span></nav>
      <p class="eyebrow" style="color:var(--mint)">For Daisy: Antes que Nadie</p>
      <h1><span>Antes</span><span>que nadie</span></h1><p class="st-es__sub">El Entrenamiento de Educadores Certificados, ahora en español</p>
      <p class="lede">Estamos emocionados de anunciar que el Entrenamiento para ser educadores certificados de la cultura del consentimiento está disponible en español. Muchas gracias a Mariana Hernandez por dirigir este proyecto y a todos los demás que lo hicieron posible. ¡Los invitamos a completar el curso y expandir el impacto de SafeBAE en diferentes partes del mundo!</p>
      <div class="btns">{btn('Registrarse', '#registro', 'mint', arrow=True)}{btn('Ver la versión en inglés', 'peer-educator.html', 'ghost')}</div>
      <p class="small" style="color:rgba(255,255,255,.78);margin-top:18px">Esta capacitación se ofrece en memoria de nuestra cofundadora, Daisy Coleman, cuya visión y liderazgo continúan inspirando la misión de SafeBAE y a los jóvenes de todo el país. {a('#ForDaisy', 'fordaisy.html', 'link')}</p>
    </div>
    <figure class="st-photo">{img('1-54982e7a-41f6-4540-a03d-2bd16547a2fa', 'Jóvenes de SafeBAE con botellas de agua de SafeBAE en un parque', loading='eager')}<span class="sticker">16 módulos</span></figure>
  </div>
</section>

<section class="band band--aqua">
  <div class="wrap split">
    <div>
      <p class="eyebrow">El programa</p>
      <h2>¿Qué es el Entrenamiento BAE?</h2>
      <p class="lede">El entrenamiento BAE es el programa de educación de SafeBAE. Es nuestra primera capacitación de certificación disponible a nivel nacional en Estados Unidos para prevenir la violencia sexual entre adolescentes.</p>
      <p>El programa tiene 16 módulos, disponibles bajo demanda. Los estudiantes que buscan convertirse en educadores y defensores líderes realizan estos módulos a su propio ritmo.</p>
    </div>
    <div class="st-facts3"><div><b>16</b><span>módulos de capacitación</span></div><div><b>1:1</b><span>reunión individual con los directores juveniles</span></div><div><b>A su ritmo</b><span>módulos disponibles bajo demanda</span></div></div>
  </div>
</section>

<section class="band band--paper">
  <div class="wrap">
    <div class="section-head"><div><p class="eyebrow">Paso a paso</p><h2>Pasos para realizar el entrenamiento</h2></div></div>
    <div class="st-warn"><span class="daisy" style="color:var(--coral);width:28px;height:28px" aria-hidden="true"></span><div><b>Antes de registrarse</b><p>Por favor, tenga en cuenta que hay contenido desencadenante y sensible en los módulos. Cada nivel de la capacitación se realiza a su propio ritmo y está disponible para usted en cualquier momento después de que se registre, así que asegúrese de tomar tiempo para realizar descansos si los necesita.</p></div></div>
    <ol class="st-track">{steps_html}</ol>
  </div>
</section>

<section class="band band--slate">
  <div class="wrap">
    <div class="section-head"><div><p class="eyebrow">Los módulos</p><h2>El entrenamiento incluye</h2></div></div>
    <ol class="st-mods">{mods}</ol>
  </div>
</section>

<section class="band band--mist" id="registro">
  <div class="wrap st-reg">
    <div>
      <p class="eyebrow">Registro</p>
      <h2>Registrarse para el entrenamiento</h2>
      <p class="lede">Complete el formulario de registro para comenzar el entrenamiento en español.</p>
      <div class="rows">
        {row('¿Prefiere el entrenamiento en inglés?', 'Regístrese para la versión en inglés del entrenamiento.', 'peer-educator.html#register')}
        {row('¿Preguntas?', 'Comuníquese con el equipo de SafeBAE.', 'contact.html')}
      </div>
    </div>
    <div class="st-embed">{es_embed}</div>
  </div>
</section>

<section class="band band--paper band--tight">
  <div class="wrap">
    <div class="note" style="margin-bottom:18px"><p><b>Por favor, tenga en cuenta:</b> Nos enorgullecemos de ser aliados en todas las intersecciones, pero también sabemos que, a pesar de nuestros mejores esfuerzos, puede haber lugares donde lo podríamos haber hecho mejor. Buscamos y valoramos TODOS los comentarios y recomendaciones para seguir mejorando nuestro entrenamiento y ser lo más inclusivos posible. Sabemos que podemos y siempre buscaremos mejorar, ¡pero necesitamos SU ayuda y apoyo para lograrlo!</p></div>
    {es_help}
  </div>
</section>

<section class="band band--aqua band--tight"><div class="wrap give">
<div><p class="eyebrow">Su donación llega lejos</p><h2 style="margin:0 0 .3em">Mantenga la prevención gratuita para cada estudiante.</h2><p class="lede" style="margin:0">Su donación tiene un impacto inmediato: nos permite ofrecer educación sobre el consentimiento y recursos gratuitos a estudiantes y escuelas en todo Estados Unidos.</p></div>
<div class="btns" style="justify-content:flex-end">{btn('Donar hoy', 'donate.html', 'coral', arrow=True)}</div>
</div></section>
</div>'''
    page('espanol.html', 'Entrenamiento en español · SafeBAE', 'El Entrenamiento para ser educadores certificados de SafeBAE, disponible en español: 16 módulos a su propio ritmo.',
         body, active='students', body_class='st st-es-page', head_extra=f'<style>{CSS}{ES_CSS}</style>')


def build():
    students()
    peer_educator()
    clubs()
    reform_policy()
    summer_institute()
    espanol()

if __name__ == '__main__':
    build()
