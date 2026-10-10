"""Resources hub (resources.html) and the Vibe Check product page (vibe-check.html)."""
from lib import *
from data import LIB, PODCASTS, PODCASTS_EXTRA, FAQ, library_items
from pages_home import cpet_player
import json

WP = 'https://www.safebae.org/wp-content/uploads/'
CYV = 'https://checkyourvibe.org/'
GUIDE_PDF = WP + '2026/03/Check-Their-Vibe-A-Guide-to-Vibe-Check.pdf'
SKILLS = 'https://skills-lab.safebae.org/'

ARROW = '<span aria-hidden="true">&rarr;</span>'
NE = '<span aria-hidden="true">&#8599;</span>'


def go(href):
    return NE if href.startswith('http') else ARROW


def ext_attrs(href):
    return ' target="_blank" rel="noopener"' if href.startswith('http') else ''


# =====================================================================
#  RESOURCES HUB
# =====================================================================

def lib_counts():
    items = library_items()
    n_vid = sum(1 for d in items if d['kind'] in ('film', 'video', 'series'))
    n_pod = sum(1 for d in items if d['kind'] == 'podcast')
    n_gui = sum(1 for d in LIB if d.get('guide') and d['kind'] in ('film', 'series'))
    n_faq = sum(len(qs) for _, qs in FAQ)
    return n_vid, n_pod, n_gui, n_faq


def shelf_items():
    n_vid, n_pod, n_gui, n_faq = lib_counts()
    S, P, E = 'students', 'parents', 'educators'
    films = []
    for it in LIB:
        if it['kind'] != 'film':
            continue
        g = it['guide']
        films.append(dict(t=it['title'], d=it['sub'].replace(' · film + teaching guide', '').replace(' + teaching guide', '') + '.', h=it['href'], im=it['thumb'],
                          c=['Film', f'Guide · {g["pages"]} pp'], a=[S, E], k=' '.join(it['topics']) + ' ' + it['kw'] + ' video watch'))
    # tidy one-line descriptions for the films (taken from the library data)
    film_lines = {
        'film-its-giving-red-flags.html': 'A short film about red flags, coercion and consent in teen relationships.',
        'film-baecode-game-on.html': 'The centerpiece of BAEcode, SafeBAE’s bystander intervention campaign.',
        'film-knowb4unude.html': 'SafeBAE’s PSA on the pressures, risks and consequences of sharing nudes.',
        'film-dating-after-sexual-assault.html': 'Made with Teen Vogue: intimacy, triggers and boundaries after assault.',
        'film-online-harassment-of-survivors.html': 'Two films made by youth leaders to end the online revictimization of survivors.',
        'film-rape-culture.html': 'Charlie Coleman, with Teen Vogue, on rape culture and building a culture of respect.',
        'film-sexual-assault-of-men.html': 'Survivor and SafeBAE Board Member Theo Hutt shares his story.',
    }
    for f in films:
        f['d'] = film_lines.get(f['h'], f['d'])

    shelves = [
      ('tools', 'Interactive tools & training', 'Self-paced training, private reflection and short games you can do on your own or with a group.', [
        dict(t='Certified Peer Educator Training', d='A free, self-paced 16-module training that prepares students to lead sexual violence prevention in their schools and communities.', h='peer-educator.html', im='preview1', c=['16 modules', 'Self-paced', 'Free'], a=[S, E], k='cpet certification peer educator course online leadership'),
        dict(t='Vibe Check', d='A free and anonymous tool for young people who are worried they may have crossed a boundary or caused harm.', h='vibe-check.html', im='vc-step-start', c=['Anonymous', 'Nothing stored'], a=[S, P, E], k='checkyourvibe accountability reflection harm repair consent', feat='vibe'),
        dict(t='BAE Skills Lab', d='Interactive activities about consent, boundaries, and what a healthy relationship actually looks like.', h=SKILLS, im='sl-home', c=['6 activities', 'Games'], a=[S, E], k='games practice interactive skills lab'),
        dict(t='Boundary Flags', d='Sort 25 real situations into green, yellow and red flags to identify and understand your own boundaries.', h=SKILLS + 'boundary-flags/', im='sl-boundary-flags', c=['Skills Lab', '5 min'], a=[S, E], k='game boundaries red flags green flags'),
        dict(t='Partner Nutrition Label', d='Relationships don’t come with a label, so build your own and keep it as a bookmark.', h=SKILLS + 'nutrition-label/', im='sl-nutrition-label', c=['Skills Lab', '3–8 min'], a=[S], k='healthy relationship partner game'),
        dict(t='Supporting a Survivor: Helpful or Harmful?', d='Sort things people actually say to survivors into what helps and what hurts.', h=SKILLS + 'supporting-a-survivor/', im='sl-supporting-a-survivor', c=['Skills Lab', '3 min'], a=[S, P, E], k='support survivor disclosure what to say game'),
        dict(t='Reset Kit', d='Guided breathing and grounding for when you’re overwhelmed, numb, or checked out.', h=SKILLS + 'reset-kit/', im='sl-reset-kit', c=['Skills Lab', 'Under 2 min'], a=[S, P, E], k='breathing grounding calm self-care'),
        dict(t='Listen Closer', d='Hear a clip from a song everyone knows, then decide together: are these lyrics healthy or unhealthy?', h=SKILLS + 'listen-closer/', im='sl-listen-closer', c=['Skills Lab', '5 min'], a=[S, E], k='music lyrics song game classroom'),
        dict(t='SafeBAE Jeopardy', d='A 25-question game show on consent and healthy relationships.', h=SKILLS + 'jeopardy/', im='sl-jeopardy', c=['Skills Lab', '10–30 min'], a=[S, E], k='quiz trivia game classroom group'),
        dict(t='SafeBAE Clubs', d='Start or lead a student chapter and get access to materials, training, event ideas, direct support, and a national network of student leaders.', h='clubs.html', im='clubhero', c=['Free registration', 'Club Hub'], a=[S, E], k='club chapter organizing student group advisor'),
        dict(t='Entrenamiento en español', d='El entrenamiento para ser educadores certificados, en español: 16 módulos a su propio ritmo.', h='espanol.html', im='dsc01134', c=['Español', '16 módulos'], a=[S], k='spanish espanol peer educator training latam'),
        dict(t='Faculty & Staff Training', d='Trauma-informed professional development for teachers, staff and administrators, in person or virtually.', h='professional-development.html', im='us-gariev-teacher2', c=['In person', 'Virtual'], a=[E], k='professional development teachers staff training disclosure'),
      ]),
      ('watch', 'Watch, listen & read', 'Films envisioned, written, directed and performed by young people, plus podcasts and stories.', [
        dict(t='Films & videos', d='Every youth-created film in the Library, most paired with a ready-to-teach guide.', h='library.html#films', im='gameon8', c=['Video', f'{n_vid} films & videos'], a=[S, P, E], k='videos films youtube library watch'),
        dict(t='Podcasts', d='Conversations SafeBAE’s founders, staff and student leaders were invited into.', h='library.html#podcasts', im='sp-3h2vvayco9q0bkyphcasa3', c=['Audio', f'{n_pod} episodes'], a=[S, P, E], k='podcast listen audio spotify interview'),
        *films,
        dict(t='Vibe Check demo', d='A walkthrough of Vibe Check, the free, anonymous reflection tool.', h='vibe-check.html#demo', im='yt-ng8s3w1etru', c=['Video', 'Demo'], a=[S, P, E], k='vibe check demo walkthrough accountability'),
        dict(t='Blog', d='Stories from survivors, SafeBAE news, media analysis and policy updates.', h='blog.html', im='img-9509-1', c=['Articles'], a=[S, P, E], k='blog news stories articles read'),
      ]),
      ('classroom', 'Classroom materials', 'Guides, lessons and programs for classrooms, clubs and whole schools.', [
        dict(t='Teaching guides', d='Structured prompts, classroom activities and facilitation tips paired with each youth-led film.', h='library.html#guides', im='guide-red-flags', c=['PDF', f'{n_gui} guides', 'Free'], a=[E, P], k='teaching guide lesson plan discussion prompts activities pdf', cover=True),
        dict(t='Healthy Relationship & Consent Curriculum', d='15 interactive modules aligned with the National Health Education Standards, in English and Spanish.', h='consent-curriculum.html', im='preview5', c=['15 lessons', '45–60 min each', 'NHES'], a=[E], k='curriculum lessons nhes health class consent'),
        dict(t='Race, Rape Culture, and Resistance', d='A four-lesson learning series centered on Black youth.', h='film-race-rape-culture-resistance.html', im='2l3a1960', c=['Series', '4 lessons'], a=[S, E], k='racial justice black youth history lessons series'),
        dict(t='Posters', d='Free downloadable posters for classrooms, counseling offices, hallways and wellness centers.', h='posters.html', im='everyone-can-do-something-1', c=['Download', 'Print'], a=[S, E], k='posters print download classroom hallway', cover=True),
        dict(t='Request a Program', d='Bring SafeBAE to your school or community for workshops, assemblies, and comprehensive school programming.', h='request-a-program.html', im='066', c=['Assemblies', 'Workshops'], a=[E, P], k='assembly workshop booking school program speaker'),
        dict(t='SafeBAE 360° Schools', d='A comprehensive, survivor-centered prevention model with six components, adapted to each school.', h='360-schools.html', im='safebae-consent-summits', c=['6 components'], a=[E], k='360 schools whole school model prevention program'),
      ]),
      ('rights', 'Rights & facts', 'Know your rights at school and what the research says.', [
        dict(t='Title IX', d='The federal civil rights law that protects students from sex discrimination, harassment and assault in schools.', h='title-ix.html', im='13-title-ix-1', c=['Your rights', 'Timeline'], a=[S, P, E], k='title ix rights school law reporting supportive measures coordinator'),
        dict(t='Myths & Facts', d='The most common myths about sexual violence, what the research actually says, and who is most affected.', h='myths-facts.html', im='copy-of-6-mythsfacts', c=['Research', 'Statistics'], a=[S, P, E], k='myths facts statistics research data'),
        dict(t='Frequently Asked Questions', d='SafeBAE answers your questions about teen dating violence, sexual assault, consent, and healthy relationships.', h='faq.html', g='faq', c=[f'{n_faq} answers'], a=[S, P, E], k='faq questions answers consent coercion bystander'),
        dict(t='Reform Your School’s Policy', d='A step-by-step Student Policy Reform Guide for pushing your district toward safer, survivor-centered policies.', h='reform-policy.html', im='2024-updates-safebae-sexual-misconduct-policy-reform-a-stude', c=['Student guide', 'Free'], a=[S, P], k='policy reform title ix advocacy district student guide', cover=True),
        dict(t='School Policy Reform Guide', d='A step-by-step resource for administrators and district leaders to strengthen policies beyond the federal minimum.', h='policy-reform-guide.html', im='2024-safebae-sexual-misconduct-policy-reform-guide-for-schoo', c=['For administrators'], a=[E], k='policy reform administrators district title ix', logo=True),
      ]),
      ('support', 'Support', 'For survivors, the people supporting them, and anyone worried about harm they caused.', [
        dict(t='Talk to someone now', d='Free, confidential hotlines, most open 24/7. If you are in immediate danger, call 911.', h='survivor-support.html#hotlines', g='hotline', c=['24/7', 'Confidential'], a=[S, P, E], k='hotline crisis help call text loveis rainn 988 trevor emergency', help=True),
        dict(t='Supporting a Survivor', d='Learn how to respond to a disclosure and support a young survivor.', h='survivor-support.html', im='8x8-what-not-to-say-poster-pdf', c=['What to say', 'Healing'], a=[S, P, E], k='support survivor disclosure friend believe healing'),
        dict(t='Document what happened, privately', d='SafeBAE x REES: a free, private, encrypted space to document incidents of harm at your own pace.', h='https://safebae.reessecureus.com/en/Login', im='logo-horiz-rgb', c=['Private', 'Encrypted'], a=[S], k='rees report document anonymous record', logo=True),
        dict(t='Check Their Vibe: an adults’ guide', d='How to introduce Vibe Check to a young person, follow up with care, and keep it private.', h=GUIDE_PDF, im='guide-vibe-check', c=['PDF', '7 pages'], a=[P, E], k='parent guide vibe check adult caregiver pdf', cover=True),
        dict(t='Accountability Training', d='A multi-lesson virtual program for students who have harmed another student.', h='accountability-training.html', im='sumact5', c=['Virtual', 'Multi-lesson'], a=[E, P], k='accountability harm caused recidivism title ix respondent'),
      ]),
    ]
    return shelves


def tile(it):
    h = it['h']
    if it.get('g') == 'faq':
        media = '<span class="rs-tile__media rs-g rs-g--faq" aria-hidden="true"><b>?</b><i>FAQ</i></span>'
    elif it.get('g') == 'hotline':
        media = '<span class="rs-tile__media rs-g rs-g--help" aria-hidden="true"><b>24/7</b><i>Text LOVEIS to 22522</i></span>'
    else:
        cls = 'rs-tile__media'
        if it.get('cover'): cls += ' rs-tile__media--cover'
        if it.get('logo'): cls += ' rs-tile__media--logo'
        if it.get('feat') == 'vibe': cls += ' rs-tile__media--phone'
        media = f'<span class="{cls}">{img(it["im"], "")}</span>'
    chips_html = ''.join(f'<span>{esc(c)}</span>' for c in it['c'])
    q = ' '.join([it['t'], it['d'], ' '.join(it['c']), ' '.join(it['a']), it.get('k', '')]).lower()
    extra = ' data-open-help' if it.get('help') else ''
    cls = 'rs-tile' + (' rs-tile--vibe' if it.get('feat') == 'vibe' else '') + (' rs-tile--help' if it.get('help') else '')
    return (f'<a class="{cls}" href="{esc(h)}"{ext_attrs(h)}{extra} data-aud="{" ".join(it["a"])}" data-q="{esc(q)}" role="listitem">'
            f'{media}<span class="rs-tile__body"><b>{esc(it["t"])}</b><small>{esc(it["d"])}</small>'
            f'<span class="rs-tile__chips">{chips_html}</span></span><span class="rs-tile__go">{go(h)}</span></a>')


def shelves_html():
    out = []
    for key, title, desc, items in shelf_items():
        out.append(f'''<section class="rs-shelf" id="shelf-{key}" data-shelf aria-labelledby="sh-{key}">
  <div class="rs-shelf__head">
    <div><h3 id="sh-{key}">{esc(title)} <span class="rs-shelf__n" data-n>{len(items)}</span></h3><p>{esc(desc)}</p></div>
    <div class="rs-shelf__nav"><button type="button" data-dir="-1" aria-label="Scroll {esc(title)} left">&#8249;</button><button type="button" data-dir="1" aria-label="Scroll {esc(title)} right">&#8250;</button></div>
  </div>
  <div class="rs-shelf__row" role="list">{''.join(tile(i) for i in items)}</div>
  <div class="rs-shelf__ledge" aria-hidden="true"></div>
</section>''')
    return ''.join(out)


AUD = [
  ('students', 'Students', '1-000383-edited', 'Student resources', 'Free tools made by young people, for students.',
   'Free tools for understanding consent, finding support, reflecting on harm, and creating change at school.',
   [('Survivor Support', 'survivor-support.html'), ('FAQ', 'faq.html'), ('Title IX', 'title-ix.html'), ('Posters', 'posters.html')],
   [('Free certification', 'Certified Peer Educator Training', 'Build the knowledge and skills to lead prevention work with your peers.', 'peer-educator.html', 'preview1'),
    ('Games & practice', 'Skills Lab', 'Interactive activities about consent, boundaries, and what a healthy relationship actually looks like.', SKILLS, 'sl-boundary-flags'),
    ('Student organizing', 'SafeBAE Clubs', 'Start a chapter or bring prevention activities into an existing student group.', 'clubs.html', 'clubtabling'),
    ('Anonymous tool', 'Vibe Check', 'Look back privately at something you did or said, and learn how to take accountability and repair harm.', CYV, 'vc-step-start')]),
  ('parents', 'Parents & Caregivers', 'us-sometale-parent', 'Parent & caregiver resources', 'Support the young people in your life.',
   'Resources for answering questions, responding to disclosures, and connecting young people with help.',
   [('Myths & Facts', 'myths-facts.html'), ('Teaching Guides', 'library.html#guides'), ('Podcasts', 'library.html#podcasts'), ('Blog', 'blog.html')],
   [('Support & healing', 'Supporting a Survivor', 'Learn how to respond to a disclosure and support a young survivor.', 'survivor-support.html', '000263'),
    ('Learn more', 'Frequently Asked Questions', 'SafeBAE answers your questions about teen dating violence, sexual assault, consent, and healthy relationships.', 'faq.html', 'relationships-2-1'),
    ('Watch or listen together', 'Videos & Podcasts', 'Watch or listen to SafeBAE media with a young person and use it to start a conversation.', 'library.html#films', 'yt-rixb8vlmajy'),
    ('Resource to share', 'Vibe Check', 'Share an anonymous reflection tool with a young person worried about their own behavior.', 'vibe-check.html#adults', 'guide-vibe-check')]),
  ('educators', 'Educators', 'img-2395', 'Educator resources', 'Bring youth-led prevention to your school.',
   'Classroom materials, student leadership pathways, and support for strengthening prevention in your school.',
   [('Vibe Check', CYV), ('Posters', 'posters.html'), ('Title IX', 'title-ix.html'), ('Request a Program', 'request-a-program.html')],
   [('Classroom-ready', 'Teaching Guides', 'Use structured activities, prompts, and facilitation guidance with students.', 'library.html#guides', 'guide-baecode'),
    ('Youth-created media', 'Videos & Podcasts', 'Explore SafeBAE media to open real conversations about consent, harm, and relationships.', 'library.html#films', 'red-flags'),
    ('Student leadership', 'Certified Peer Educator Training', 'Connect students with SafeBAE’s free, self-paced youth leadership certification.', 'peer-educator.html', 'preview11'),
    ('School organizing', 'SafeBAE Clubs', 'Help students establish and sustain youth-led prevention work at school.', 'clubs.html', 'clubhero')]),
]


def audience_html():
    tabs, panels = [], []
    for i, (k, label, im, eb, h3, p, also, cards) in enumerate(AUD):
        sel = i == 0
        tabs.append(f'<button class="rs-aud__tab" role="tab" id="tab-{k}" aria-controls="p-{k}" aria-selected="{str(sel).lower()}" tabindex="{0 if sel else -1}">'
                    f'<span class="rs-aud__face">{img(im, "")}</span><span><small>For</small><b>{esc(label)}</b></span><em>{len(cards)} picks</em></button>')
        cards_html = ''.join(
            f'<a class="rs-acard" href="{esc(u)}"{ext_attrs(u)}><span class="rs-acard__img{" rs-acard__img--cover" if ci.startswith("guide-") else ""}">{img(ci, "")}</span>'
            f'<span class="rs-acard__body"><small>{esc(kick)}</small><b>{esc(t)}</b><span>{esc(d)}</span></span><span class="rs-acard__go">{go(u)}</span></a>'
            for kick, t, d, u, ci in cards)
        also_html = ''.join(f'<a href="{esc(u)}"{ext_attrs(u)}>{esc(t)}{" &#8599;" if u.startswith("http") else ""}</a>' for t, u in also)
        panels.append(f'''<div class="rs-aud__panel" role="tabpanel" id="p-{k}" aria-labelledby="tab-{k}"{'' if sel else ' hidden'}>
  <div class="rs-aud__intro">
    <div class="rs-aud__img">{img(im, '')}</div>
    <div class="rs-aud__txt"><p class="eyebrow">{esc(eb)}</p><h3>{esc(h3)}</h3><p>{esc(p)}</p>
    <div class="rs-also"><span>Also useful</span><div>{also_html}</div></div></div>
  </div>
  <div class="rs-aud__cards">{cards_html}</div>
</div>''')
    return f'<div data-tabs="rs-aud"><div class="rs-aud__tabs" role="tablist" aria-label="Browse by who you are">{"".join(tabs)}</div>{"".join(panels)}</div>'


RS_CSS = '''
/* ---------- hero ---------- */
.rs-hero{background:var(--slate-deep); color:#fff; position:relative; overflow:hidden}
.rs-hero::before{content:""; position:absolute; right:-160px; top:-160px; width:620px; height:620px; background:var(--logo-teal); opacity:.35; -webkit-mask:url(assets/img/daisy.svg) center/contain no-repeat; mask:url(assets/img/daisy.svg) center/contain no-repeat; animation:rs-spin 90s linear infinite}
@keyframes rs-spin{to{transform:rotate(360deg)}}
.rs-hero .wrap{position:relative; z-index:2; display:grid; grid-template-columns:minmax(0,1.05fr) minmax(0,.95fr); gap:clamp(28px,4vw,56px); align-items:center; padding-block:clamp(44px,5.5vw,76px) clamp(40px,5vw,64px)}
.rs-hero h1{font-size:clamp(2.6rem,5vw,5rem); font-stretch:125%; font-weight:900; text-transform:uppercase; line-height:.84; letter-spacing:-.03em; margin:0 0 .3em}
.rs-hero h1 em{font-style:normal; color:var(--mint); display:block}
.rs-hero .lede{color:rgba(255,255,255,.9); max-width:none}
.rs-search{display:flex; align-items:center; gap:12px; background:#fff; border-radius:14px; padding:6px 6px 6px 18px; box-shadow:0 20px 50px -20px rgba(0,0,0,.6); margin-top:6px}
.rs-search svg{width:24px; height:24px; color:var(--teal); flex:none}
.rs-search input{flex:1; min-width:0; border:0; outline:0; font:inherit; font-size:1.12rem; padding:12px 0; color:var(--slate); background:transparent}
.rs-search input::-webkit-search-cancel-button{cursor:pointer}
.rs-search .btn{box-shadow:none}
.rs-hint{display:inline-flex; margin-top:14px; font-weight:700; color:var(--mint); text-decoration:underline; text-underline-offset:3px}
.rs-searching .rs-who{display:none}
.rs-who{display:flex; flex-wrap:wrap; gap:8px; margin-top:18px; align-items:center}
.rs-who span{font-family:var(--mono); font-size:.72rem; letter-spacing:.1em; text-transform:uppercase; color:var(--aqua); margin-right:4px}
.rs-who button{font:inherit; font-weight:700; font-size:.9rem; color:#fff; background:rgba(255,255,255,.07); border:1.5px solid rgba(209,254,255,.3); border-radius:999px; padding:7px 14px; cursor:pointer}
.rs-who button:hover{border-color:var(--mint); color:var(--mint)}
/* pile of resource objects */
.rs-pile{position:relative; aspect-ratio:1/.92; width:100%; max-width:600px; margin-left:auto}
.rs-pile > *{position:absolute; border-radius:10px; overflow:hidden; box-shadow:0 26px 50px -22px rgba(0,0,0,.75); transition:transform .45s cubic-bezier(.2,.8,.2,1)}
.rs-pile img{width:100%; height:100%; object-fit:cover}
.rs-pile__a{left:0; top:4%; width:60%; aspect-ratio:16/10; transform:rotate(-5deg)}
.rs-pile__b{right:0; top:0; width:56%; aspect-ratio:16/9; transform:rotate(4deg)}
.rs-pile__c{left:6%; bottom:3%; width:30%; aspect-ratio:935/1210; transform:rotate(-7deg); background:#fff}
.rs-pile__d{left:36%; bottom:9%; width:27%; aspect-ratio:3/4; transform:rotate(3deg)}
.rs-pile__e{right:5%; bottom:0; width:27%; aspect-ratio:390/800; border-radius:26px; border:7px solid #0b1f25; background:#0b1f25; transform:rotate(7deg)}
.rs-pile__e img{object-position:top}
.rs-pile:hover > *{transform:rotate(0) translateY(-4px)}
.rs-pile .sticker{position:absolute; overflow:visible; box-shadow:3px 3px 0 var(--slate); border-radius:6px; z-index:3}
.rs-pile .s1{left:44%; top:38%; transform:rotate(-4deg)} .rs-pile .s2{right:30%; bottom:40%; transform:rotate(3deg)}
.rs-pile:hover .s1{transform:rotate(-4deg) translateY(-4px)} .rs-pile:hover .s2{transform:rotate(3deg) translateY(-4px)}
.rs-hero .wrap > *{min-width:0}
@media (max-width:900px){ .rs-hero .wrap{grid-template-columns:minmax(0,1fr)} .rs-pile{max-width:520px; margin:6px auto 0; aspect-ratio:1/.8} }
@media (max-width:520px){ .rs-pile .sticker{font-size:.72rem} }

/* ---------- support band ---------- */
.rs-help{background:var(--coral); color:var(--slate)}
.rs-help__in{display:grid; grid-template-columns:auto minmax(0,1fr) auto; gap:14px 28px; align-items:center; padding-block:20px}
.rs-help__t b{display:block; font-family:var(--display); font-stretch:112%; font-weight:900; font-size:clamp(1.25rem,1.8vw,1.5rem); line-height:.98; text-transform:uppercase; max-width:13ch}
.rs-help__t span{display:block; font-weight:600; font-size:.88rem; margin-top:6px}
.rs-help__nums{list-style:none; margin:0; padding:0; display:flex; flex-wrap:wrap; gap:12px 0; justify-content:space-evenly}
.rs-help__nums li{margin:0; padding:2px 16px; border-left:2px solid rgba(29,65,78,.28); min-width:0}
.rs-help__nums small{display:block; font-family:var(--mono); font-size:.64rem; letter-spacing:.08em; text-transform:uppercase; font-weight:600; margin-bottom:2px}
.rs-help__nums b, .rs-help__nums a{display:block; font-family:var(--display); font-stretch:106%; font-weight:900; font-size:clamp(1.02rem,1.3vw,1.2rem); line-height:1.1; color:var(--slate); text-decoration:none; white-space:nowrap}
.rs-help__nums a:hover{text-decoration:underline; text-decoration-thickness:2px}
.rs-help__act{display:flex; flex-direction:column; gap:8px; align-items:flex-start}
.rs-help__act a{font-weight:700; font-size:.9rem; color:var(--slate)}
@media (max-width:1180px){ .rs-help__in{grid-template-columns:minmax(0,1fr) auto} .rs-help__nums{grid-column:1/-1; grid-row:2; justify-content:flex-start} .rs-help__nums li:first-child{border-left:0; padding-left:0} }
@media (max-width:640px){ .rs-help__in{grid-template-columns:1fr} .rs-help__t b{max-width:none} .rs-help__nums{flex-direction:column; gap:10px; grid-row:auto} .rs-help__nums li{border-left:0; padding:0} .rs-help__act{flex-direction:row; align-items:center; gap:16px} }

/* ---------- search state ---------- */
.rs-searching .rs-hide-on-search{display:none}

/* ---------- featured bento ---------- */
.rs-bento{display:grid; grid-template-columns:repeat(12,minmax(0,1fr)); gap:18px}
.rs-f{position:relative; border-radius:20px; overflow:hidden; display:flex; flex-direction:column; min-width:0; text-decoration:none; color:inherit}
.rs-f h3{font-size:clamp(1.5rem,2.4vw,2.2rem); line-height:1; margin:0 0 .35em}
.rs-f p{margin:0}
.rs-kick{display:block; font-family:var(--mono); font-size:.7rem; letter-spacing:.12em; text-transform:uppercase; font-weight:600; margin-bottom:12px}
.rs-f--cpet{grid-column:span 7; background:var(--aqua); color:var(--slate); padding:clamp(22px,2.6vw,34px)}
.rs-f--cpet .rs-kick{color:var(--logo-teal)}
.rs-f--cpet .player{margin-top:22px; box-shadow:0 20px 40px -24px rgba(22,53,64,.6)}
.rs-f--cpet .chips{margin:14px 0 18px}
.rs-f--vibe{grid-column:span 5; background:var(--teal); color:#fff; padding:clamp(22px,2.6vw,34px) clamp(22px,2.6vw,34px) 0}
.rs-f--vibe .rs-kick{color:#fff}
.rs-vmark{display:flex; align-items:center; gap:10px; font-family:var(--display); font-weight:900; font-stretch:115%; font-size:1.1rem; color:#fff; margin-bottom:10px}
.rs-vmark .daisy{width:32px; height:32px; color:var(--mint)}
.rs-qs{position:relative; height:calc(clamp(1.9rem,3.3vw,2.9rem) * 2.1); overflow:hidden; margin:0 0 .4em}
.rs-qs span{position:absolute; inset:0; display:flex; align-items:flex-end; font-family:var(--display); font-weight:900; font-stretch:115%; font-size:clamp(1.9rem,3.3vw,2.9rem); line-height:1; letter-spacing:-.015em; color:#fff; transform:translateY(110%); opacity:0; transition:transform .7s cubic-bezier(.2,.8,.2,1), opacity .7s}
.rs-qs span.on{transform:none; opacity:1}
.rs-qs span.out{transform:translateY(-110%); opacity:0}
.rs-f--vibe p{color:#fff; font-weight:500}
.rs-f--vibe .btns{margin-top:18px}
.rs-vphone{flex:1; position:relative; min-height:250px; margin-top:22px}
.rs-vphone .ph{position:absolute; left:50%; top:0; width:min(240px,66%); aspect-ratio:390/800; transform:translateX(-50%) rotate(-3deg); border-radius:34px; border:9px solid #0b1f25; background:#0b1f25; overflow:hidden; box-shadow:0 30px 60px -20px rgba(0,0,0,.55)}
.rs-vphone .ph img{width:100%; height:100%; object-fit:cover; object-position:top}
.rs-vphone .sticker{position:absolute; z-index:2}
.rs-f--sm{grid-column:span 4; background:#fff; border:1px solid var(--line); transition:transform .2s, box-shadow .2s}
a.rs-f--sm:hover{transform:translateY(-4px); box-shadow:var(--shadow)}
.rs-f__media{aspect-ratio:16/10; overflow:hidden; background:var(--slate); position:relative}
.rs-f__media img{width:100%; height:100%; object-fit:cover; transition:transform .5s}
a.rs-f--sm:hover .rs-f__media img{transform:scale(1.04)}
.rs-f__body{padding:20px 22px 22px; display:flex; flex-direction:column; flex:1}
.rs-f__body .rs-kick{color:var(--teal)}
.rs-f__body h3{font-size:1.45rem}
.rs-f__body p{color:var(--ink-soft); font-size:.95rem; line-height:1.5}
.rs-f__links{margin-top:auto; padding-top:14px; display:flex; flex-wrap:wrap; gap:6px 18px}
.rs-f__links span, .rs-f__links a{font-weight:800; font-family:var(--display); font-stretch:106%; color:var(--logo-teal); text-decoration:none}
.rs-f__links a:hover{text-decoration:underline; text-decoration-color:var(--mint); text-decoration-thickness:2px; text-underline-offset:3px}
.rs-mosaic{display:grid; grid-template-columns:repeat(3,1fr); grid-template-rows:1fr 1fr; gap:3px; height:100%}
.rs-mosaic img{width:100%; height:100%; object-fit:cover}
.rs-mosaic .gc{grid-column:3; grid-row:1/3; background:var(--aqua); display:grid; place-items:center; padding:10px}
.rs-mosaic .gc img{width:auto; height:92%; object-fit:contain; box-shadow:0 10px 24px -10px rgba(0,0,0,.5); border-radius:3px; transform:rotate(3deg)}
.rs-f--lib{background:var(--slate); color:#fff; border-color:transparent}
.rs-f--lib .rs-f__body p{color:rgba(255,255,255,.8)} .rs-f--lib .rs-kick{color:var(--mint)} .rs-f--lib .rs-f__links a{color:var(--mint)}
.rs-f--req{grid-column:1/-1; display:grid; grid-template-columns:minmax(0,.9fr) minmax(0,1.1fr); background:var(--logo-teal); color:#fff}
.rs-f--req .rs-f__media{aspect-ratio:auto; min-height:260px}
.rs-f--req .rs-f__media img{position:absolute; inset:0}
.rs-f--req .rs-f__body{padding:clamp(24px,3vw,40px); justify-content:center}
.rs-f--req .rs-kick{color:var(--mint)} .rs-f--req .rs-f__body p{color:#fff; font-size:1.02rem}
.rs-f--req h3{font-size:clamp(1.7rem,3vw,2.6rem)}
@media (max-width:1060px){ .rs-f--cpet,.rs-f--vibe{grid-column:1/-1; display:grid; grid-template-columns:minmax(0,1fr) minmax(0,1fr); column-gap:32px; align-items:center}
  .rs-f--cpet .player{margin-top:0} .rs-f--vibe{padding-bottom:0; align-items:stretch} .rs-f--vibe .rs-ftxt{padding-bottom:30px; align-self:center} .rs-vphone{min-height:360px; margin-top:0} .rs-vphone .ph{top:30px; width:min(230px,70%)} }
@media (max-width:700px){ .rs-f--cpet,.rs-f--vibe{display:flex} .rs-f--cpet .player{margin-top:22px} .rs-f--vibe .rs-ftxt{padding-bottom:0} .rs-vphone{min-height:270px; margin-top:22px} .rs-vphone .ph{top:0} }
@media (max-width:860px){ .rs-f--sm{grid-column:span 6} .rs-f--sm.rs-f--skills{grid-column:1/-1} .rs-f--skills{display:grid; grid-template-columns:minmax(0,1fr) minmax(0,1fr)} .rs-f--skills .rs-f__media{aspect-ratio:auto; min-height:220px} .rs-f--skills .rs-f__media img{position:absolute; inset:0} .rs-f--req{grid-template-columns:1fr} .rs-f--req .rs-f__media{min-height:220px} }
@media (max-width:620px){ .rs-bento{gap:14px} .rs-f--sm,.rs-f--sm.rs-f--skills{grid-column:1/-1} .rs-f--skills{display:flex} .rs-f--skills .rs-f__media{aspect-ratio:16/10; min-height:0} .rs-f--skills .rs-f__media img{position:static} }

/* ---------- audience tabs ---------- */
.rs-aud__tabs{display:grid; grid-template-columns:repeat(3,minmax(0,1fr)); gap:12px; margin-bottom:22px}
.rs-aud__tab{font:inherit; text-align:left; display:flex; align-items:center; gap:14px; padding:12px 16px 12px 12px; border-radius:16px; border:2px solid var(--line); background:#fff; color:var(--slate); cursor:pointer; transition:border-color .2s, background .2s; min-width:0}
.rs-aud__face{width:58px; height:58px; border-radius:12px; overflow:hidden; flex:none; background:var(--mist)}
.rs-aud__face img{width:100%; height:100%; object-fit:cover}
.rs-aud__tab small{display:block; font-family:var(--mono); font-size:.66rem; letter-spacing:.12em; text-transform:uppercase; color:var(--teal)}
.rs-aud__tab b{display:block; font-family:var(--display); font-weight:800; font-stretch:110%; font-size:1.25rem; line-height:1.05}
.rs-aud__tab em{margin-left:auto; font-style:normal; font-family:var(--mono); font-size:.7rem; letter-spacing:.06em; text-transform:uppercase; color:var(--ink-soft); white-space:nowrap}
.rs-aud__tab:hover{border-color:var(--teal)}
.rs-aud__tab[aria-selected="true"]{background:var(--slate); color:#fff; border-color:var(--slate)}
.rs-aud__tab[aria-selected="true"] small{color:var(--mint)} .rs-aud__tab[aria-selected="true"] em{color:var(--aqua)}
.rs-aud__panel{display:grid; grid-template-columns:minmax(0,.82fr) minmax(0,1.18fr); gap:18px; align-items:stretch}
.rs-aud__intro{background:#fff; border-radius:18px; overflow:hidden; border:1px solid var(--line); display:flex; flex-direction:column}
.rs-aud__img{aspect-ratio:16/9; overflow:hidden}
.rs-aud__img img{width:100%; height:100%; object-fit:cover}
.rs-aud__txt{padding:22px 24px 24px; display:flex; flex-direction:column; flex:1}
.rs-aud__txt h3{font-size:clamp(1.5rem,2.3vw,2rem); margin-bottom:.35em}
.rs-aud__txt > p:not(.eyebrow){color:var(--ink-soft)}
.rs-aud__txt .eyebrow{margin-bottom:.6rem}
.rs-also{margin-top:auto; padding-top:16px; border-top:1px solid var(--line)}
.rs-also > span{display:block; font-family:var(--mono); font-size:.68rem; letter-spacing:.12em; text-transform:uppercase; color:var(--teal); font-weight:600; margin-bottom:8px}
.rs-also div{display:flex; flex-wrap:wrap; gap:6px}
.rs-also a{font-weight:700; font-size:.88rem; text-decoration:none; color:var(--slate); background:var(--aqua); border-radius:999px; padding:6px 12px}
.rs-also a:hover{background:var(--mint)}
.rs-aud__cards{display:grid; grid-template-columns:repeat(2,minmax(0,1fr)); grid-auto-rows:1fr; gap:14px}
.rs-acard{position:relative; display:flex; flex-direction:column; background:#fff; border:1px solid var(--line); border-radius:16px; overflow:hidden; text-decoration:none; color:var(--slate); transition:transform .2s, box-shadow .2s; min-width:0}
.rs-acard:hover{transform:translateY(-3px); box-shadow:var(--shadow)}
.rs-acard__img{aspect-ratio:2/1; overflow:hidden; background:var(--slate)}
.rs-acard__img img{width:100%; height:100%; object-fit:cover; transition:transform .5s}
.rs-acard__img--cover{background:var(--aqua); display:flex; justify-content:center; align-items:flex-end; padding-top:12px}
.rs-acard__img--cover img{width:auto; height:100%; max-width:60%; object-fit:cover; object-position:top; border-radius:4px 4px 0 0; box-shadow:0 -6px 18px -8px rgba(0,0,0,.4)}
.rs-acard:hover .rs-acard__img img{transform:scale(1.04)}
.rs-acard__body{padding:14px 16px 16px; display:flex; flex-direction:column; gap:4px; flex:1}
.rs-acard__body small{font-family:var(--mono); font-size:.66rem; letter-spacing:.1em; text-transform:uppercase; color:var(--teal); font-weight:600}
.rs-acard__body b{font-family:var(--display); font-stretch:106%; font-size:1.15rem; line-height:1.15; color:var(--logo-teal)}
.rs-acard__body span{font-size:.88rem; color:var(--ink-soft); line-height:1.45}
.rs-acard__go{position:absolute; right:12px; top:12px; width:34px; height:34px; border-radius:50%; display:grid; place-items:center; background:var(--mint); color:var(--slate); font-weight:800; box-shadow:0 4px 10px rgba(0,0,0,.2)}
@media (max-width:960px){ .rs-aud__tab em{display:none} .rs-aud__panel{grid-template-columns:1fr} .rs-aud__intro{display:grid; grid-template-columns:minmax(0,.8fr) minmax(0,1.2fr)} .rs-aud__img{aspect-ratio:auto; min-height:100%} }
@media (max-width:760px){ .rs-aud__tab em{display:inline} .rs-aud__tabs{grid-template-columns:1fr; gap:8px} .rs-aud__tab{padding:8px 14px 8px 8px} .rs-aud__face{width:44px; height:44px} .rs-aud__intro{display:flex} .rs-aud__img{aspect-ratio:16/9; min-height:0} }
@media (max-width:560px){ .rs-aud__cards{grid-template-columns:1fr; grid-auto-rows:auto} }

/* ---------- index bar ---------- */
.rs-ibar{position:sticky; top:calc(76px + env(safe-area-inset-top,0px)); z-index:20; background:rgba(255,255,255,.96); backdrop-filter:blur(8px); border-bottom:1px solid var(--line); border-top:1px solid var(--line)}
.rs-ibar .wrap{display:flex; flex-wrap:wrap; gap:10px 16px; align-items:center; padding-block:12px}
.rs-ibar__q{display:flex; align-items:center; gap:8px; flex:1 1 260px; min-width:0; border:2px solid var(--line); border-radius:10px; padding:0 12px; background:#fff}
.rs-ibar__q:focus-within{border-color:var(--teal)}
.rs-ibar__q svg{width:18px; height:18px; color:var(--teal); flex:none}
.rs-ibar__q input{flex:1; min-width:0; border:0; outline:0; font:inherit; font-size:.98rem; padding:10px 0; background:transparent; color:var(--slate)}
.rs-seg{display:flex; gap:4px; background:var(--mist); border-radius:10px; padding:4px; overflow-x:auto; max-width:100%; scrollbar-width:none}
.rs-seg button{font:inherit; font-family:var(--display); font-weight:800; font-stretch:106%; font-size:.92rem; border:0; background:transparent; padding:8px 13px; border-radius:7px; cursor:pointer; color:var(--slate); white-space:nowrap}
.rs-seg button[aria-pressed="true"]{background:var(--slate); color:#fff}
.rs-count{font-weight:700; font-size:.9rem; color:var(--ink-soft); margin:0; white-space:nowrap}
.rs-count button{font:inherit; font-weight:700; color:var(--logo-teal); background:none; border:0; cursor:pointer; text-decoration:underline; text-decoration-color:var(--mint); text-underline-offset:3px; padding:0; margin-left:8px}

/* ---------- shelves ---------- */
.rs-index{padding-top:0; padding-bottom:clamp(36px,4.5vw,60px)}
.rs-index .rs-shelf:last-of-type{margin-bottom:0}
.rs-index__in{padding-top:clamp(30px,3.5vw,48px)}
#index,#browse,#featured{scroll-margin-top:70px}
.rs-shelf{margin-bottom:clamp(30px,3.6vw,48px)}
.rs-shelf__head{display:flex; justify-content:space-between; align-items:flex-end; gap:12px 24px; margin-bottom:14px}
.rs-shelf__head > div:first-child{min-width:0}
.rs-shelf__head h3{font-size:clamp(1.45rem,2.4vw,2.05rem); margin:0 0 .2em; display:flex; align-items:center; gap:12px; flex-wrap:wrap}
.rs-shelf__head p{margin:0; color:var(--ink-soft); font-size:.95rem}
.rs-shelf__n{font-family:var(--mono); font-size:.8rem; font-weight:600; background:var(--mint); color:var(--slate); border-radius:999px; padding:3px 10px; letter-spacing:.04em}
.rs-shelf__nav{display:flex; gap:8px; flex:none}
.rs-shelf__nav button{width:42px; height:42px; border-radius:50%; border:2px solid var(--line); background:#fff; color:var(--slate); font-size:1.4rem; line-height:1; cursor:pointer; display:grid; place-items:center; padding-bottom:3px}
.rs-shelf__nav button:hover:not(:disabled){border-color:var(--slate); background:var(--slate); color:#fff}
.rs-shelf__nav button:disabled{opacity:.35; cursor:default}
.rs-shelf__row{display:flex; gap:16px; overflow-x:auto; scroll-snap-type:x mandatory; padding:6px 2px 16px; scrollbar-width:none; scroll-padding-left:2px}
.rs-shelf__row::-webkit-scrollbar{display:none}
.rs-shelf__ledge{height:14px; border-radius:4px; background:var(--slate); box-shadow:0 14px 20px -12px rgba(22,53,64,.55), inset 0 3px 0 rgba(21,255,200,.5); margin-top:-4px; position:relative}
.rs-tile{position:relative; flex:0 0 clamp(236px, 23.2%, 282px); scroll-snap-align:start; display:flex; flex-direction:column; background:#fff; color:var(--slate); border:1px solid var(--line); border-radius:14px; overflow:hidden; text-decoration:none; transition:transform .25s cubic-bezier(.2,.8,.2,1), box-shadow .25s; min-width:0}
.rs-tile:hover{transform:translateY(-6px); box-shadow:0 22px 34px -22px rgba(22,53,64,.6)}
.rs-tile__media{display:block; aspect-ratio:16/10; overflow:hidden; background:var(--slate); position:relative}
.rs-tile__media img{width:100%; height:100%; object-fit:cover; transition:transform .5s}
.rs-tile:hover .rs-tile__media img{transform:scale(1.05)}
.rs-tile__media--cover{background:var(--aqua); display:flex; justify-content:center; align-items:flex-end; padding-top:14px}
.rs-tile__media--cover img{width:auto; height:100%; max-width:62%; object-fit:cover; object-position:top; border-radius:4px 4px 0 0; box-shadow:0 -8px 22px -10px rgba(0,0,0,.45)}
.rs-tile:hover .rs-tile__media--cover img{transform:translateY(-4px)}
.rs-tile__media--logo{background:var(--aqua); display:grid; place-items:center; padding:20px 26px; border-bottom:1px solid var(--line)}
.rs-tile__media--logo img{object-fit:contain; height:auto; max-height:80%}
.rs-tile__media--phone{background:var(--teal)}
.rs-tile__media--phone img{width:46%; height:auto; margin:14px auto 0; border-radius:16px 16px 0 0; border:5px solid #0b1f25; border-bottom:0}
.rs-tile:hover .rs-tile__media--phone img{transform:translateY(-4px)}
.rs-g{display:flex; flex-direction:column; justify-content:center; align-items:flex-start; padding:16px 20px}
.rs-g b{font-family:var(--display); font-weight:900; font-stretch:125%; line-height:.9; font-size:4.2rem; letter-spacing:-.02em}
.rs-g i{font-style:normal; font-family:var(--mono); font-size:.7rem; letter-spacing:.1em; text-transform:uppercase; margin-top:8px}
.rs-g--faq{background:var(--logo-teal); color:var(--mint)} .rs-g--faq b{font-size:5.4rem} .rs-g--faq i{color:var(--aqua)}
.rs-g--help{background:var(--coral); color:var(--slate)}
.rs-tile__body{padding:14px 16px 16px; display:flex; flex-direction:column; gap:6px; flex:1}
.rs-tile__body b{font-family:var(--display); font-stretch:106%; font-size:1.08rem; line-height:1.18; color:var(--logo-teal); padding-right:26px}
.rs-tile__body small{font-size:.84rem; color:var(--ink-soft); line-height:1.45}
.rs-tile__chips{display:flex; flex-wrap:wrap; gap:5px; margin-top:auto; padding-top:8px}
.rs-tile__chips span{font-family:var(--mono); font-size:.64rem; letter-spacing:.06em; text-transform:uppercase; font-weight:600; padding:3px 7px; border-radius:4px; background:var(--aqua); color:var(--slate); white-space:nowrap}
.rs-tile__chips span:first-child{background:var(--slate); color:#fff}
.rs-tile__go{position:absolute; right:12px; bottom:14px; font-weight:800; color:var(--teal)}
.rs-tile__body{padding-bottom:16px}
.rs-tile--vibe{border-color:var(--teal); box-shadow:inset 0 0 0 1px var(--teal)}
.rs-tile--vibe .rs-tile__chips span:first-child{background:var(--logo-teal)}
.rs-tile--help .rs-tile__chips span:first-child{background:var(--coral); color:var(--slate)}
.rs-filtered .rs-shelf__row{flex-wrap:wrap; overflow:visible; scroll-snap-type:none}
.rs-filtered .rs-shelf__nav{display:none}
.rs-filtered .rs-tile{flex-basis:clamp(236px, calc(25% - 12px), 282px)}
.rs-empty{padding:48px 20px; text-align:center; border:2px dashed var(--line); border-radius:16px}
.rs-empty h3{margin-bottom:.3em}
@media (max-width:640px){ .rs-ibar{position:static} .rs-ibar .wrap{gap:10px} .rs-shelf__nav{display:none} .rs-tile{flex-basis:78%} .rs-filtered .rs-tile{flex-basis:100%} .rs-shelf__head{align-items:flex-start} }
'''

RS_JS = r'''
(function(){
  var d = document, main = d.getElementById('main');
  /* rotating questions in the Vibe Check tile */
  var qs = d.querySelectorAll('.rs-qs span'), qi = 0, reduce = matchMedia('(prefers-reduced-motion: reduce)').matches;
  if(qs.length && !reduce){ setInterval(function(){ var cur = qs[qi]; cur.classList.remove('on'); cur.classList.add('out'); qi = (qi+1) % qs.length; var nx = qs[qi]; nx.classList.remove('out'); void nx.offsetWidth; nx.classList.add('on'); setTimeout(function(){ cur.classList.remove('out'); }, 800); }, 2600); }

  /* shelf arrows */
  d.querySelectorAll('[data-shelf]').forEach(function(sh){
    var row = sh.querySelector('.rs-shelf__row'), btns = sh.querySelectorAll('[data-dir]');
    function upd(){ var max = row.scrollWidth - row.clientWidth - 2; btns[0].disabled = row.scrollLeft <= 2; btns[1].disabled = row.scrollLeft >= max; }
    btns.forEach(function(b){ b.addEventListener('click', function(){ row.scrollBy({left: (+b.dataset.dir) * row.clientWidth * .85, behavior: reduce ? 'auto' : 'smooth'}); }); });
    row.addEventListener('scroll', function(){ window.requestAnimationFrame(upd); }, {passive:true});
    window.addEventListener('resize', upd); upd();
  });

  /* search + audience filter */
  var tiles = Array.prototype.slice.call(d.querySelectorAll('.rs-tile')), shelves = d.querySelectorAll('[data-shelf]');
  var inputs = d.querySelectorAll('[data-rsq]'), count = d.getElementById('rs-count'), empty = d.getElementById('rs-empty'), idx = d.getElementById('index');
  var st = { q:'', aud:'' }, total = tiles.length;
  function norm(s){ return (s||'').toLowerCase().normalize('NFD').replace(/[̀-ͯ]/g,'').replace(/[’']/g,'').replace(/[^a-z0-9#+ ]/g,' '); }
  tiles.forEach(function(t){ t._q = norm(t.getAttribute('data-q')); t._a = t.getAttribute('data-aud'); });
  function esc(s){ return s.replace(/[&<>"]/g, function(c){ return {'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;'}[c]; }); }
  function render(){
    var terms = norm(st.q).split(/\s+/).filter(Boolean), shown = 0;
    tiles.forEach(function(t){ var ok = (!st.aud || t._a.indexOf(st.aud) >= 0) && terms.every(function(w){ return t._q.indexOf(w) >= 0; }); t.hidden = !ok; if(ok) shown++; });
    shelves.forEach(function(sh){ var n = sh.querySelectorAll('.rs-tile:not([hidden])').length; sh.hidden = !n; sh.querySelector('[data-n]').textContent = n; });
    var filtering = terms.length || st.aud;
    idx.classList.toggle('rs-filtered', !!filtering);
    main.classList.toggle('rs-searching', terms.length > 0);
    empty.hidden = shown > 0;
    if(!shown){ var q = st.q.trim(); empty.querySelector('[data-eq]').textContent = q ? '“' + q + '”' : 'this filter'; var lk = empty.querySelector('[data-lib]'); lk.href = 'library.html' + (/^[a-z0-9]+$/i.test(q) ? '#q-' + q : ''); }
    count.innerHTML = (filtering ? '<b>' + shown + '</b> of ' + total + ' resources' : '<b>' + total + '</b> resources') + (filtering ? '<button type="button" data-clear>Clear</button>' : '');
    var c = count.querySelector('[data-clear]'); if(c) c.addEventListener('click', clear);
    var hint = d.getElementById('rs-hint'); if(hint){ hint.hidden = !terms.length; hint.textContent = shown ? (shown + (shown === 1 ? ' resource matches' : ' resources match') + '. Show results \u2193') : 'No matches yet. Try another word.'; }
    d.querySelectorAll('[data-shelf]').forEach(function(sh){ var row = sh.querySelector('.rs-shelf__row'); row.scrollLeft = 0; row.dispatchEvent(new Event('scroll')); });
  }
  function clear(){ st.q = ''; st.aud = ''; inputs.forEach(function(i){ i.value = ''; }); syncSeg(); render(); }
  var tmr;
  inputs.forEach(function(inp){ inp.addEventListener('input', function(){ var v = inp.value; inputs.forEach(function(o){ if(o !== inp) o.value = v; }); clearTimeout(tmr); tmr = setTimeout(function(){ st.q = v; render(); }, 90); }); });
  var hn = d.getElementById('rs-hint'); if(hn) hn.addEventListener('click', function(e){ e.preventDefault(); idx.scrollIntoView({behavior: reduce ? 'auto' : 'smooth', block:'start'}); });
  var hf = d.getElementById('rs-hform');
  if(hf) hf.addEventListener('submit', function(e){ e.preventDefault(); st.q = hf.querySelector('input').value; render(); idx.scrollIntoView({behavior: reduce ? 'auto' : 'smooth', block:'start'}); });
  var seg = d.querySelectorAll('[data-aud-btn]');
  function syncSeg(){ seg.forEach(function(b){ b.setAttribute('aria-pressed', String(b.dataset.audBtn === st.aud)); }); }
  seg.forEach(function(b){ b.addEventListener('click', function(){ st.aud = b.dataset.audBtn; syncSeg(); render(); }); });
  render();

  /* hero audience shortcuts -> select tab and scroll */
  d.querySelectorAll('[data-go-aud]').forEach(function(b){ b.addEventListener('click', function(){ var t = d.getElementById('tab-' + b.dataset.goAud); if(t){ t.click(); d.getElementById('browse').scrollIntoView({behavior: reduce ? 'auto' : 'smooth', block:'start'}); setTimeout(function(){ t.focus({preventScroll:true}); }, 400); } }); });
})();
'''


def resources():
    n_vid, n_pod, n_gui, n_faq = lib_counts()
    pile = f'''<div class="rs-pile" aria-hidden="true">
      <div class="rs-pile__a">{img('sl-boundary-flags', '', loading='eager')}</div>
      <div class="rs-pile__b">{img('preview5', '', loading='eager')}</div>
      <div class="rs-pile__d">{img('everyone-can-do-something-1', '', loading='eager')}</div>
      <div class="rs-pile__c">{img('guide-red-flags', '', loading='eager')}</div>
      <div class="rs-pile__e">{img('vc-screen', '', loading='eager')}</div>
      <span class="sticker s1">Free for students</span>
      <span class="sticker sticker--aqua s2">Made by young people</span>
    </div>'''

    films4 = ''.join(img(n, '') for n in ['red-flags', 'gameon8', 'knowb4unude', 'yt-rixb8vlmajy'])

    body = f'''
<section class="rs-hero">
  <div class="wrap">
    <div>
      <nav class="crumbs" aria-label="Breadcrumb"><a href="index.html">Home</a><span>/</span><span>Resources</span></nav>
      <p class="eyebrow" style="color:var(--mint)">Free &middot; Created by youth &amp; survivors</p>
      <h1>SafeBAE <em>Resources</em></h1>
      <p class="lede">All of SafeBAE’s resources are free for students and created by young people, with support from adult allies and professionals. Find tools for learning about consent and healthy relationships, finding support, building skills, and creating change in your school or community.</p>
      <form class="rs-search" role="search" id="rs-hform"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" aria-hidden="true"><circle cx="10.5" cy="10.5" r="6.5"/><path d="M15.5 15.5 21 21"/></svg><label class="sr-only" for="rs-q">Search all resources</label><input id="rs-q" data-rsq type="search" placeholder="Try “consent” or “Title IX”" autocomplete="off"><button class="btn" type="submit">Search</button></form>
      <a class="rs-hint" id="rs-hint" href="#index" hidden></a>
      <div class="rs-who"><span>Browse as</span><button type="button" data-go-aud="students">a student</button><button type="button" data-go-aud="parents">a parent or caregiver</button><button type="button" data-go-aud="educators">an educator</button></div>
    </div>
    {pile}
  </div>
</section>

<section class="rs-help" aria-label="Support right now">
  <div class="wrap rs-help__in">
    <div class="rs-help__t"><b>Need support right now?</b><span>Free and confidential, 24/7.</span></div>
    <ul class="rs-help__nums">
      <li><small>Dating abuse &middot; love is respect</small><b>Text LOVEIS to 22522</b></li>
      <li><small>Sexual assault &middot; RAINN</small><a href="tel:18006564673">Call 800-656-HOPE</a></li>
      <li><small>Suicide &amp; crisis lifeline</small><a href="tel:988">Call or text 988</a></li>
    </ul>
    <div class="rs-help__act"><button class="btn btn--slate btn--sm" data-open-help>All hotlines</button><a href="survivor-support.html">Survivor support &rarr;</a></div>
  </div>
</section>

<section class="band band--paper rs-hide-on-search" id="featured">
  <div class="wrap">
    <div class="section-head"><div><p class="eyebrow">Featured</p><h2>Start with one of these</h2></div></div>
    <div class="rs-bento">
      <div class="rs-f rs-f--cpet">
        <div class="rs-ftxt">
        <span class="rs-kick">For student leaders</span>
        <h3>Certified Peer Educator Training</h3>
        <p class="lede" style="margin:0">A free, self-paced 16-module training that prepares students to lead sexual violence prevention in their schools and communities.</p>
        {chips(['16 modules', 'Self-paced', 'Free certificate'], 'mint')}
        <div class="btns">{btn('Explore the training', 'peer-educator.html', 'slate', arrow=True)}{btn('Register', 'peer-educator.html#register', 'ghost')}</div>
        </div>
        {cpet_player()}
      </div>
      <div class="rs-f rs-f--vibe">
        <div class="rs-ftxt">
        <span class="rs-kick">Reflection &amp; accountability</span>
        <div class="rs-vmark"><span class="daisy"></span>Vibe Check by SafeBAE</div>
        <div class="rs-qs" aria-hidden="true"><span class="on">Did I harm someone?</span><span>Was that consent?</span><span>Did I cross a boundary?</span><span>Am I a bad person?</span></div>
        <h3 class="sr-only">Vibe Check</h3>
        <p>A free and anonymous tool for young people who are worried they may have crossed a boundary or caused harm.</p>
        <div class="btns">{btn('Visit CheckYourVibe.org', CYV, 'mint')}{btn('How it works', 'vibe-check.html', 'ghost', arrow=True)}</div>
        </div>
        <div class="rs-vphone"><div class="ph">{img('vc-screen', 'The Vibe Check start screen on a phone')}</div><span class="sticker" style="left:4%;top:22%">Anonymous</span><span class="sticker sticker--white sticker--r" style="right:3%;top:52%">Nothing is stored</span></div>
      </div>
      <a class="rs-f rs-f--sm rs-f--clubs" href="clubs.html">
        <div class="rs-f__media">{img('clubhero', 'SafeBAE club members at a summer event')}</div>
        <div class="rs-f__body"><span class="rs-kick">Student-led action</span><h3>SafeBAE Clubs</h3><p>Start or lead a student chapter and get access to materials, training, event ideas, direct support, and a national network of student leaders.</p><div class="rs-f__links"><span>Explore SafeBAE Clubs &rarr;</span></div></div>
      </a>
      <div class="rs-f rs-f--sm rs-f--lib">
        <div class="rs-f__media"><div class="rs-mosaic">{films4}<span class="gc">{img('guide-red-flags', '')}</span></div></div>
        <div class="rs-f__body"><span class="rs-kick">Films + ready-to-use lessons</span><h3>Video Library &amp; Teaching Guides</h3><p>Pair youth-created films with activities, discussion prompts, and facilitation guidance for classrooms, clubs, and community programs.</p><div class="rs-f__links"><a href="library.html#films">Watch films &rarr;</a><a href="library.html#guides">Use teaching guides &rarr;</a></div></div>
      </div>
      <a class="rs-f rs-f--sm rs-f--skills" href="{SKILLS}" target="_blank" rel="noopener">
        <div class="rs-f__media">{img('sl-home', 'The BAE Skills Lab home page')}</div>
        <div class="rs-f__body"><span class="rs-kick">Games + practice</span><h3>Skills Lab</h3><p>Interactive activities about consent, boundaries, and what a healthy relationship actually looks like.</p><div class="rs-f__links"><span>Explore the Skills Lab &#8599;</span></div></div>
      </a>
      <div class="rs-f rs-f--req">
        <div class="rs-f__media">{img('066', 'SafeBAE presenters with students at a school assembly')}</div>
        <div class="rs-f__body"><span class="rs-kick">Work with SafeBAE</span><h3>Request a Program</h3><p>Bring SafeBAE to your school or community for workshops, assemblies, and comprehensive school programming.</p><div class="btns" style="margin-top:20px">{btn('Request a program', 'request-a-program.html', 'mint', arrow=True)}{btn('Explore 360° Schools', '360-schools.html', 'ghost', arrow=True)}</div></div>
      </div>
    </div>
  </div>
</section>

<section class="band band--mist rs-hide-on-search" id="browse">
  <div class="wrap">
    <div class="section-head"><div><p class="eyebrow">Browse by who you are</p><h2>Resources for you</h2></div></div>
    {audience_html()}
  </div>
</section>

<section class="band band--paper rs-index" id="index">
<div class="rs-ibar">
  <div class="wrap">
    <label class="rs-ibar__q"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" aria-hidden="true"><circle cx="10.5" cy="10.5" r="6.5"/><path d="M15.5 15.5 21 21"/></svg><span class="sr-only">Filter resources</span><input type="search" data-rsq placeholder="Filter every resource" autocomplete="off"></label>
    <div class="rs-seg" role="group" aria-label="Show resources for"><button type="button" data-aud-btn="" aria-pressed="true">Everyone</button><button type="button" data-aud-btn="students" aria-pressed="false">Students</button><button type="button" data-aud-btn="parents" aria-pressed="false">Parents &amp; caregivers</button><button type="button" data-aud-btn="educators" aria-pressed="false">Educators</button></div>
    <p class="rs-count" id="rs-count" aria-live="polite"></p>
  </div>
</div>
  <div class="wrap rs-index__in">
    <div class="section-head"><div><p class="eyebrow">Full index</p><h2>Every resource, by format</h2></div></div>
    {shelves_html()}
    <div class="rs-empty" id="rs-empty" hidden><h3>Nothing matches <span data-eq></span>.</h3><p class="muted">Try a broader word like <b>consent</b>, search the <a class="link" data-lib href="library.html">Library</a> for films and podcasts, or <a class="link" href="contact.html">tell us what you were looking for</a>.</p></div>
  </div>
</section>
{give_band()}
'''
    page('resources.html', 'Resources · SafeBAE',
         'Free sexual violence prevention resources for students, parents and educators: training, Vibe Check, the Skills Lab, films, teaching guides, Title IX and survivor support.',
         body, active='resources', head_extra=f'<style>{RS_CSS}</style>', scripts=f'<script>{RS_JS}</script>')


# =====================================================================
#  VIBE CHECK
# =====================================================================

VC_STEPS = [
  ('vc-step-start', 'Start privately', 'The first screen says it plainly: this is a private space to think it through, and you can leave anytime. Vibe Check collects no names, no account info, and stores nothing.'),
  ('vc-step-brings', 'Say what brings you here', 'Something happened, someone told me, I already know, I need help understanding, or it’s about someone else. It’s okay to not have a clear answer yet.'),
  ('vc-step-closest', 'Get specific', 'Pick what feels closest to what happened, like “They froze or got quiet”, “We were drinking or using substances” or “Something happened digitally”. You don’t need to explain.'),
  ('vc-step-learn', 'Learn what may have been going on', 'Short guided explanations matched to your answer, such as how the freeze response works and why “just say no” isn’t always possible.'),
  ('vc-step-feel', 'Check in with how you feel', 'Guilt, defensive, confused, ashamed, anxious, angry, numb, sad and more. Pick the closest one. There’s no wrong answer.'),
  ('vc-step-move', 'Find the next right move', 'Guilt becomes useful when it turns into a concrete next step. Vibe Check walks through six steps, one at a time, starting with: pause.'),
  ('vc-step-next', 'Choose what to do next', 'Learn, prevent it from happening again, ground and reset, repair, shift your thinking, or talk to someone. You can come back and try others.'),
  ('vc-step-modules', 'Go deeper', 'Guided modules on the spectrum of harm, consent, rape culture, healthy relationships, men and masculinity, and digital safety and image consent.'),
]

ACCOUNT = [
  ('Self-reflection', 'Look honestly at what you did and what came up for you, without minimizing, comparing, or rushing past it. This is the part of the work that happens before anyone else is involved.'),
  ('Apologize', 'Name what you did specifically, center the other person, ask for nothing in return. Only if they want to hear it, and only after you’ve done part 1.'),
  ('Repair', 'Do what you can to make things as right as possible: whatever they need, not what feels best to you. Sometimes repair is space. Sometimes it’s silence.'),
  ('Change behavior', 'The load-bearing part. Preventing recurrence is the most meaningful thing anyone who’s caused harm can offer. Everything else is preparation for this.'),
]

SHATTUCK = [
  'Where are young people learning how to think about relationships, consent, accountability, and repair?',
  'Increasingly, many are turning to AI tools, Reddit forums, influencers, or online communities that frame these experiences through blame, defensiveness, misogyny, punishment, or emotional isolation. That concerns me deeply, especially for young men who are already struggling with loneliness, confusion, and a lack of healthy relational guidance.',
  'I recently came across Vibe Check, a new project from SafeBAE, and I think it represents something genuinely important.',
  'Vibe Check is a free and fully anonymous reflection tool designed for young people who are questioning whether they or a friend may have crossed a boundary, caused harm, or handled a situation poorly.',
  'Instead of escalating shame or encouraging denial, the tool walks users through reflection, accountability, empathy, communication, and repair. Importantly, it is intentionally not AI-generated. It was built from years of direct work with young people around consent, relationships, and sexual violence prevention.',
  'What I appreciate most is that it recognizes something many conversations miss: Accountability is relational.',
  'People rarely grow through humiliation alone. Growth often happens when individuals are given structured opportunities to reflect honestly, understand impact, reconnect to others, and move toward repair.',
  'That does not minimize harm. It creates conditions where accountability is more likely to happen.',
  'At a time when so many young people are searching online for answers about deeply human situations, I think tools like this matter.',
]
SHATTUCK_TAGS = '#MensHealth, #PublicHealth, #HealthyRelationships, #ConsentEducation, #RelationalHealth, #RelationalMasculinity, #YouthDevelopment, #DigitalWellbeing, #MentalHealth, #Belonging, #HealthyMasculinity, #SexualHealth, #Accountability, #Empathy, #ViolencePrevention, #TeenHealth, #SocialConnection, #OnlineSafety, #ConsentCulture, #YouthLeadership'

SUBSTACK = [
  ('Vibe Check by SafeBAE', 'A tool for perpetrators, from survivors', 'https://safebae.substack.com/p/vibe-check'),
  ('When you Ask AI for Advice, and It Just Agrees with You...', 'A new study shows why that is a problem.', 'https://safebae.substack.com/p/when-you-ask-ai-for-advice-and-it'),
  ('New York Just Passed a Bill to Protect Minors from Unsafe AI Chatbots.', 'Here is Why That Matters for Consent and Accountability.', 'https://safebae.substack.com/p/new-york-just-passed-a-bill-to-protect'),
]

GUIDE_TABS = [
  ('refer', 'How to refer', '''<ol class="vcp-gsteps">
<li><b>Pick the right moment, not the charged one.</b><span>Wait until things have cooled down. Good windows: a car ride, a casual one-on-one moment, a follow-up conversation after things have settled.</span></li>
<li><b>Lead with curiosity, not direction.</b><span>If it sounds like a punishment or an assignment, they won’t engage honestly, even if they do open it.</span></li>
<li><b>Make the privacy real.</b><span>Send them the link and step away. Don’t ask to see what they wrote or what path they took. Make it clear they can stop at any point.</span></li>
<li><b>Tell them what it actually is.</b><span>Young people are suspicious of anything that looks like a trap or feels fake. Being upfront about what the tool is, and isn’t, helps a lot.</span></li>
<li><b>Give them genuine space, and keep the door open.</b><span>Let them know you’re available to talk, but take the pressure off.</span></li>
</ol>
<p class="vcp-gnote">The perfect time is before anything has happened at all, as part of a talk about dating or sex.</p>'''),
  ('say', 'What to say', '''<div class="vcp-says">
<figure><figcaption>Try saying something like</figcaption><blockquote>“Hey, I came across this thing — it’s not a lecture, it’s more like a self-reflection tool. Private, nothing gets saved. I thought it might be useful to go through on your own when you have a minute. No pressure, but I think it’s worth a look.”</blockquote></figure>
<figure><figcaption>Or, for a younger person</figcaption><blockquote>“There’s a tool I want to show you — it’s like a private check-in for yourself about relationships and situations. You don’t have to share anything with me. I just thought it might be helpful.”</blockquote></figure>
<figure><figcaption>What you can tell them honestly</figcaption><blockquote>“It’s not a test. You can’t get it ‘wrong.’ It asks you questions about a situation and how you’re feeling, and then shows you some tools and information based on that. Nothing gets saved anywhere. It disappears when you close it.”</blockquote></figure>
<figure class="vcp-says__offer"><figcaption>A low-pressure follow-up offer</figcaption><blockquote>“If anything comes up when you go through it — questions, things you want to talk through — I’m around. But you don’t have to tell me anything.”</blockquote><p>This keeps a door open without making them feel like they owe you a debrief.</p></figure>
<figure class="vcp-avoid"><figcaption>Avoid framing it as</figcaption><ul><li>“You need to do this because of what happened.”</li><li>“This will help you understand why you were wrong.”</li><li>“We’re going to go through this together.”</li><li>“I want to see your answers afterward.”</li></ul></figure>
</div>'''),
  ('after', 'Talking after', '''<div class="vcp-after">
<div><b>Opening the conversation</b><p>“Did you get a chance to look at that thing I sent? No worries if not — just wondering what you thought.”</p><p>“Is there anything from it that stuck with you, or anything you want to talk about?”</p><p>“Did anything surprise you or feel off?”</p></div>
<div><b>If they seem uncomfortable</b><p>“You don’t have to tell me anything about it. I just wanted to check in that you’re okay.”</p><p>“If something came up that felt heavy, I want you to know you can talk to me — or someone else you trust.”</p><p>“Sometimes that stuff brings up more questions than answers. That’s fine — it’s actually a good sign.”</p></div>
<div><b>Going deeper (if they’re open)</b><p>“What does consent actually mean to you? What do you think it looks like in real life?”</p><p>“Have you ever been in a situation where you weren’t sure if someone was into it? What did you do?”</p><p>“How do you think you’d react if a friend told you they’d been in a situation where someone didn’t stop when asked?”</p></div>
<div><b>If they didn’t use it</b><p>“That’s okay — I’ll leave the link with you. It’s there whenever you want it.”</p><p>“Is there a reason it felt weird? I can explain what it actually is if that would help.”</p><p>“Even without the tool — is there anything on your mind about what we talked about?”</p></div>
</div>
<p class="vcp-gnote">If a young person comes to you after using it, receive that with curiosity, not judgment. Your reaction to the first vulnerable thing they share determines whether they share anything again.</p>'''),
  ('signals', 'Reading the signals', '''<div class="vcp-sig" role="table" aria-label="Reading the signals">
<div role="row" class="vcp-sig__h"><span role="columnheader">What you might notice</span><span role="columnheader">What it might mean, and how to respond</span></div>
<div role="row"><span role="cell">They bring it up unprompted</span><span role="cell">They engaged with it. Stay curious and follow their lead. Don’t pepper them with questions.</span></div>
<div role="row"><span role="cell">They’re quieter than usual, seem to be processing something</span><span role="cell">Give it time before asking. Something may have landed. Let them sit with it.</span></div>
<div role="row"><span role="cell">They dismiss it or say it was “stupid” or “not for them”</span><span role="cell">They may have engaged but felt defensive. Don’t push. The seed is planted.</span></div>
<div role="row"><span role="cell">They say they didn’t do it</span><span role="cell">Don’t make it a confrontation. Leave the link available, and come back differently another time.</span></div>
<div role="row"><span role="cell">They ask questions about consent, relationships, or something related</span><span role="cell">They’re processing. This is success. Engage with their question directly and honestly.</span></div>
<div role="row"><span role="cell">They become upset or shut down during the follow-up conversation</span><span role="cell">Back off. Let them know the door is open when they’re ready. Don’t force the conversation.</span></div>
</div>'''),
  ('avoid', 'What to avoid', '''<div class="vcp-avoids">
<div><b>Watching them use it</b><p>Your physical presence changes how honest someone is. Give them the link, explain what it is, and leave.</p></div>
<div><b>Treating it as evidence or confession</b><p>This tool is not a mechanism for extracting admissions. Using anything from it against them destroys the safety the tool requires.</p></div>
<div><b>Introducing it in a charged moment</b><p>A young person who is defensive, frightened, or angry cannot engage with this tool honestly.</p></div>
<div><b>Announcing it publicly or to their peer group</b><p>If other people know a young person is being referred to this tool, shame and humiliation take over. Keep it between you and them.</p></div>
<div><b>Following up like an interrogation</b><p>“What did you learn?” or “Did you understand what you did wrong?” puts a young person on the defensive. The goal is a conversation, not a report-back.</p></div>
</div>'''),
  ('faq', 'Common questions', '''<div class="acc vcp-acc">
<details><summary>Is this appropriate for my child specifically?</summary><div class="acc__body"><p>Vibe Check works best with young people who are at least 13–14 years old and have some emotional readiness to reflect. It is not designed as a crisis intervention and should not be the first or only response to a serious disclosure. Consider whether a counselor should be involved first.</p></div></details>
<details><summary>What if they’ve actually done something harmful to someone?</summary><div class="acc__body"><p>The tool is designed for young people who are in or near the grey zone of harmful behavior. It approaches accountability without shame spiraling. If the behavior is serious, involving assault, coercion, minors, or legal exposure, it is not a substitute for professional intervention, counseling, or legal process.</p></div></details>
<details><summary>Can I go through the tool myself first?</summary><div class="acc__body"><p>Yes, and you should. It helps you understand the tone, what the questions feel like, and what resources get offered. You can explore it as someone reflecting on a scenario, or skip ahead to the Next Steps page to see the resources, tools, and modules directly.</p></div></details>
<details><summary>What if they refuse to use it?</summary><div class="acc__body"><p>Don’t force it. Making this mandatory or punitive will guarantee it doesn’t work. Leave the link somewhere available and return to it casually later. The conversation you’re trying to open doesn’t have to start with the tool.</p></div></details>
<details><summary>Does this replace a conversation with a therapist or counselor?</summary><div class="acc__body"><p>No. This is a self-guided reflection tool, not therapy. It can be a useful complement to counseling or a first step toward self-awareness. It is not clinical support.</p></div></details>
<details><summary>What if something comes up that I don’t know how to handle?</summary><div class="acc__body"><p>“I don’t know the answer to that, but I can find out” is one of the most trust-building things you can say. If a young person discloses something serious, stay calm, validate that they told you, and help them access the right support. The Support section of the tool includes crisis resources.</p></div></details>
</div>'''),
]


VC_CSS = '''
body.vcp{--vcp-ph:#0b1f25}
/* ---------- hero ---------- */
.vcp-hero{background:var(--teal); color:#fff; position:relative; overflow:hidden}
.vcp-hero::before{content:""; position:absolute; right:-10%; top:50%; width:min(980px,90vw); aspect-ratio:1; transform:translateY(-50%); background:var(--logo-teal); opacity:.32; -webkit-mask:url(assets/img/daisy.svg) center/contain no-repeat; mask:url(assets/img/daisy.svg) center/contain no-repeat; animation:vcp-spin 120s linear infinite}
@keyframes vcp-spin{to{transform:translateY(-50%) rotate(360deg)}}
.vcp-hero .wrap{position:relative; z-index:2; display:grid; grid-template-columns:minmax(0,1.1fr) minmax(0,.9fr); gap:clamp(24px,4vw,56px); align-items:center; padding-block:clamp(40px,5vw,72px) clamp(36px,4.5vw,64px)}
.vcp-hero .crumbs, .vcp-hero .crumbs a{color:#fff}
.vcp-mark{display:flex; align-items:center; gap:12px; font-family:var(--display); font-weight:900; font-stretch:115%; font-size:1.15rem; color:#fff; margin-bottom:14px}
.vcp-mark .daisy{width:40px; height:40px; color:var(--mint)}
.vcp-hero h1{font-size:clamp(3.6rem,9.4vw,8rem); font-stretch:125%; font-weight:900; text-transform:uppercase; line-height:.8; letter-spacing:-.035em; margin:0 0 .16em}
.vcp-hero h1 span{display:block}
.vcp-hero h1 span:last-child{color:var(--mint)}
.vcp-tag{display:inline-block; font-family:var(--display); font-weight:900; font-stretch:115%; text-transform:uppercase; font-size:clamp(1rem,1.7vw,1.35rem); background:var(--slate); color:#fff; padding:.5em .8em .42em; border-radius:6px; transform:rotate(-1.5deg); margin:0 0 22px; box-shadow:4px 4px 0 var(--mint)}
.vcp-hero .lede{color:#fff; max-width:none}
.vcp-hero .btns{margin-top:4px}
.vcp-privacy{display:flex; flex-wrap:wrap; gap:10px 22px; margin-top:28px; padding-top:20px; border-top:1px solid rgba(255,255,255,.28)}
.vcp-privacy span{display:inline-flex; align-items:center; gap:9px; font-weight:700; font-size:.95rem}
.vcp-privacy span::before{content:""; width:20px; height:20px; border-radius:50%; background:var(--mint) url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 24 24'%3E%3Cpath d='M5 12.5l4.5 4.5L19 7.5' fill='none' stroke='%231d414e' stroke-width='3.2' stroke-linecap='round' stroke-linejoin='round'/%3E%3C/svg%3E") center/13px no-repeat; flex:none}
.vcp-stage{position:relative; min-height:560px; display:grid; place-items:center}
.vcp-phone{position:relative; width:min(310px,72vw); aspect-ratio:390/800; border-radius:46px; border:11px solid var(--vcp-ph); background:var(--vcp-ph); box-shadow:0 60px 100px -40px rgba(0,0,0,.65), 0 0 0 2px rgba(255,255,255,.1); overflow:hidden; transform:rotate(-3deg); z-index:2}
.vcp-phone img{width:100%; height:100%; object-fit:cover; object-position:top}
.vcp-bub{position:absolute; z-index:3; background:#fff; color:var(--slate); font-family:var(--display); font-weight:800; font-stretch:106%; font-size:clamp(.92rem,1.3vw,1.08rem); padding:12px 16px; border-radius:18px; box-shadow:0 18px 30px -16px rgba(0,0,0,.5); white-space:nowrap; opacity:0; transform:translateY(10px) scale(.96); transition:opacity .5s, transform .5s cubic-bezier(.2,.8,.2,1)}
.vcp-bub.on{opacity:1; transform:none}
.vcp-bub::after{content:""; position:absolute; bottom:-7px; width:16px; height:16px; background:inherit; transform:rotate(45deg); border-radius:3px}
.vcp-bub--l::after{right:22px} .vcp-bub--r::after{left:22px}
.vcp-bub:nth-child(odd){background:var(--aqua)}
.vcp-stage .sticker{position:absolute; z-index:4}
@media (max-width:960px){ .vcp-hero .wrap{grid-template-columns:1fr} .vcp-stage{min-height:0; padding-block:30px 10px} .vcp-phone{width:min(270px,64vw)} }
@media (max-width:520px){ .vcp-bub{font-size:.8rem; padding:9px 12px} .vcp-privacy span{font-size:.88rem} }

/* ---------- why ---------- */
.vcp-why{display:grid; grid-template-columns:minmax(0,1.05fr) minmax(0,.95fr); gap:clamp(28px,5vw,72px); align-items:center}
.vcp-why h2{font-size:clamp(1.7rem,2.9vw,2.6rem)}
.vcp-why p{color:rgba(255,255,255,.86)}
.vcp-vs{display:grid; gap:14px}
.vcp-vs > div{border-radius:18px; padding:22px 24px; position:relative}
.vcp-vs small{display:block; font-family:var(--mono); font-size:.7rem; letter-spacing:.12em; text-transform:uppercase; font-weight:600; margin-bottom:8px}
.vcp-vs b{display:block; font-family:var(--display); font-weight:800; font-stretch:108%; font-size:clamp(1.2rem,1.9vw,1.55rem); line-height:1.2}
.vcp-vs__ai{background:rgba(255,255,255,.05); border:1.5px dashed rgba(209,254,255,.35); color:rgba(255,255,255,.8)}
.vcp-vs__ai small{color:var(--aqua)}
.vcp-vs__vc{background:var(--mint); color:var(--slate)}
.vcp-vs__vc .chips{margin-top:14px}
.vcp-vs__vc .chip{background:var(--slate); color:#fff}
.vcp-vs__arrow{display:grid; place-items:center; height:8px}
@media (max-width:860px){ .vcp-why{grid-template-columns:1fr} }

/* ---------- how it works ---------- */
.vcp-how{display:grid; grid-template-columns:minmax(0,1.1fr) minmax(0,.9fr); gap:clamp(28px,5vw,72px); align-items:center}
.vcp-steps{list-style:none; margin:0; padding:0; counter-reset:s; border-top:1px solid var(--line)}
.vcp-steps li{margin:0; border-bottom:1px solid var(--line)}
.vcp-steps button{all:unset; box-sizing:border-box; width:100%; cursor:pointer; display:grid; grid-template-columns:54px minmax(0,1fr); gap:0 14px; padding:14px 0; position:relative}
.vcp-steps button:focus-visible{outline:3px solid var(--teal); outline-offset:2px; border-radius:6px}
.vcp-steps .n{grid-row:1/3; font-family:var(--display); font-weight:900; font-stretch:125%; font-size:1.9rem; line-height:1; color:rgba(29,65,78,.28); transition:color .3s}
.vcp-steps .t{font-family:var(--display); font-weight:800; font-stretch:108%; font-size:1.18rem; line-height:1.25; color:var(--slate); padding-top:4px}
.vcp-steps .d{display:block; max-height:0; overflow:hidden; color:var(--ink-soft); font-size:.95rem; line-height:1.5; transition:max-height .45s ease, margin .3s; margin-top:0}
.vcp-steps .bar{position:absolute; left:0; bottom:-1px; height:3px; width:0; background:var(--teal)}
.vcp-steps li.on .n{color:var(--teal)}
.vcp-steps li.on .d{max-height:160px; margin-top:6px}
.vcp-steps li:hover .n{color:var(--teal)}
.vcp-howstage{position:relative; display:grid; place-items:center; padding:30px 0}
.vcp-howstage::before{content:""; position:absolute; inset:6% 4%; background:var(--aqua); border-radius:40px; transform:rotate(3deg)}
.vcp-howphone{position:relative; width:min(330px,74vw); aspect-ratio:390/800; border-radius:46px; border:11px solid var(--vcp-ph); background:var(--vcp-ph); overflow:hidden; box-shadow:0 50px 80px -36px rgba(22,53,64,.7)}
.vcp-howphone img{position:absolute; inset:0; width:100%; height:100%; object-fit:cover; object-position:top; opacity:0; transform:scale(1.03); transition:opacity .5s, transform .6s}
.vcp-howphone img.on{opacity:1; transform:none}
.vcp-howcap{position:absolute; left:50%; bottom:6px; transform:translateX(-50%); background:var(--slate); color:#fff; font-family:var(--mono); font-size:.72rem; letter-spacing:.1em; text-transform:uppercase; padding:6px 12px; border-radius:999px; white-space:nowrap; z-index:2}
.vcp-tools{display:flex; flex-wrap:wrap; gap:10px; align-items:center; margin-top:26px; padding:16px 18px; border-radius:14px; background:var(--mist); border:1px solid var(--line)}
.vcp-tools > b{font-family:var(--mono); font-size:.7rem; letter-spacing:.12em; text-transform:uppercase; color:var(--teal); margin-right:4px}
.vcp-tools span{font-weight:700; font-size:.88rem; padding:6px 11px; border-radius:999px; background:#fff; border:1.5px solid var(--line)}
.vcp-tools .x{background:var(--coral); border-color:var(--coral); color:var(--slate)}
.vcp-tools .c{border-color:var(--coral)}
.vcp-mdesc{display:none}
@media (max-width:900px){
  .vcp-how{grid-template-columns:minmax(0,1fr); gap:0}
  .vcp-howlist{display:contents}
  .vcp-steps{order:1; display:flex; gap:8px; overflow-x:auto; border:0; padding:2px 2px 10px; scrollbar-width:none; scroll-snap-type:x proximity}
  .vcp-steps::-webkit-scrollbar{display:none}
  .vcp-steps li{border:0; flex:none; scroll-snap-align:start}
  .vcp-steps button{display:flex; align-items:center; gap:8px; padding:8px 14px 8px 8px; border-radius:999px; border:2px solid var(--line); background:#fff; width:auto}
  .vcp-steps .n{font-size:1rem; width:26px; height:26px; border-radius:50%; display:grid; place-items:center; background:var(--mist); color:var(--teal)}
  .vcp-steps .t{font-size:.92rem; padding:0; white-space:nowrap}
  .vcp-steps .d, .vcp-steps .bar{display:none}
  .vcp-steps li.on button{background:var(--slate); border-color:var(--slate)}
  .vcp-steps li.on .t{color:#fff} .vcp-steps li.on .n{background:var(--mint); color:var(--slate)}
  .vcp-howstage{order:2; padding:14px 0 18px}
  .vcp-howphone{width:min(250px,62vw)}
  .vcp-mdesc{order:3; display:block; text-align:center; margin:4px 0 0; min-height:6.5em}
  .vcp-mdesc b{display:block; font-family:var(--display); font-stretch:108%; font-size:1.2rem; margin-bottom:4px}
  .vcp-mdesc span{display:block; color:var(--ink-soft); font-size:.95rem; line-height:1.5}
  .vcp-tools{order:4}
}
@media (max-width:520px){ .vcp-phone{width:min(240px,62vw)} .vcp-stage{padding-block:24px 0} }

/* ---------- demo ---------- */
.vcp-demo{display:grid; grid-template-columns:minmax(0,1.5fr) minmax(0,.7fr); gap:clamp(24px,4vw,56px); align-items:center}
.vcp-demo h2{font-size:clamp(1.8rem,3.2vw,2.8rem)}
.vcp-demo .vid{box-shadow:0 40px 80px -30px rgba(0,0,0,.8); outline:6px solid rgba(21,255,200,.25); outline-offset:0}
@media (max-width:860px){ .vcp-demo{grid-template-columns:1fr} }

/* ---------- accountability ---------- */
.vcp-acct{display:grid; grid-template-columns:repeat(4,minmax(0,1fr)); gap:0; counter-reset:a; position:relative}
.vcp-acct > div{position:relative; padding:24px 22px 26px; background:#fff; border:1px solid var(--line); margin-left:-1px}
.vcp-acct > div:first-child{border-radius:18px 0 0 18px; margin-left:0}
.vcp-acct > div:last-child{border-radius:0 18px 18px 0; background:var(--slate); color:#fff; border-color:var(--slate)}
.vcp-acct b{display:block; font-family:var(--display); font-weight:900; font-stretch:125%; font-size:3rem; line-height:1; color:var(--teal); margin-bottom:12px}
.vcp-acct > div:last-child b{color:var(--mint)}
.vcp-acct h3{font-size:1.3rem; margin-bottom:.4em}
.vcp-acct p{margin:0; font-size:.94rem; line-height:1.5; color:var(--ink-soft)}
.vcp-acct > div:last-child p{color:rgba(255,255,255,.82)}
.vcp-acct > div:not(:last-child)::after{content:""; position:absolute; right:-14px; top:34px; width:26px; height:26px; background:var(--mint) url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 24 24'%3E%3Cpath d='M8 5l7 7-7 7' fill='none' stroke='%231d414e' stroke-width='3' stroke-linecap='round' stroke-linejoin='round'/%3E%3C/svg%3E") center/14px no-repeat; border-radius:50%; z-index:2}
@media (max-width:960px){ .vcp-acct{grid-template-columns:1fr 1fr; gap:12px} .vcp-acct > div, .vcp-acct > div:first-child, .vcp-acct > div:last-child{border-radius:16px; margin:0} .vcp-acct > div::after{display:none} }
@media (max-width:560px){ .vcp-acct{grid-template-columns:1fr} }

/* ---------- privacy / is & isn't ---------- */
.vcp-big{font-size:clamp(3rem,9vw,8rem); font-stretch:125%; font-weight:900; text-transform:uppercase; line-height:.84; letter-spacing:-.03em; margin:0 0 .25em}
.vcp-big span{color:var(--mint)}
.vcp-isnt{display:grid; grid-template-columns:minmax(0,1fr) minmax(0,1fr); gap:18px; margin-top:34px; align-items:stretch}
.vcp-col{border-radius:20px; padding:clamp(22px,3vw,34px)}
.vcp-col h3{font-size:clamp(1.4rem,2.2vw,1.9rem); margin-bottom:.7em}
.vcp-col ul{list-style:none; padding:0; margin:0; display:grid; gap:14px}
.vcp-col li{margin:0; display:grid; grid-template-columns:28px minmax(0,1fr); gap:12px; align-items:start}
.vcp-col li::before{content:""; width:28px; height:28px; border-radius:50%; margin-top:1px}
.vcp-col li b{display:block; font-family:var(--display); font-stretch:106%; font-size:1.06rem; line-height:1.25}
.vcp-col li span{display:block; font-size:.92rem; line-height:1.45; margin-top:2px}
.vcp-col--is{background:var(--mint); color:var(--slate)}
.vcp-col--is li::before{background:var(--slate) url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 24 24'%3E%3Cpath d='M5 12.5l4.5 4.5L19 7.5' fill='none' stroke='%2315ffc8' stroke-width='3.2' stroke-linecap='round' stroke-linejoin='round'/%3E%3C/svg%3E") center/16px no-repeat}
.vcp-col--not{background:rgba(255,255,255,.05); border:1.5px solid var(--line-dark); color:#fff}
.vcp-col--not li::before{border:2px solid var(--aqua); background:url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 24 24'%3E%3Cpath d='M7 7l10 10M17 7L7 17' fill='none' stroke='%23d1feff' stroke-width='2.6' stroke-linecap='round'/%3E%3C/svg%3E") center/14px no-repeat}
.vcp-col--not li span{color:rgba(255,255,255,.75)}
.vcp-crisis{display:flex; gap:14px 26px; align-items:center; justify-content:space-between; flex-wrap:wrap; margin-top:18px; padding:16px 20px; border-radius:14px; background:var(--coral); color:var(--slate)}
.vcp-crisis p{margin:0; font-weight:600; max-width:none; flex:1 1 420px}
@media (max-width:860px){ .vcp-isnt{grid-template-columns:1fr} }

/* ---------- press ---------- */
.vcp-press{display:grid; grid-template-columns:repeat(6,minmax(0,1fr)); gap:16px}
.vcp-pr{position:relative; display:flex; flex-direction:column; gap:14px; padding:24px 26px; border-radius:18px; background:#fff; border:1px solid var(--line); text-decoration:none; color:var(--slate); transition:transform .2s, box-shadow .2s; min-width:0}
a.vcp-pr:hover{transform:translateY(-4px); box-shadow:var(--shadow)}
.vcp-pr__logo{height:44px; display:flex; align-items:center}
.vcp-pr__logo img{height:100%; width:auto; max-width:200px; object-fit:contain}
.vcp-pr h3{font-size:clamp(1.25rem,2vw,1.6rem); line-height:1.15; margin:0}
.vcp-pr__go{margin-top:auto; font-weight:800; font-family:var(--display); font-stretch:106%; color:var(--logo-teal)}
.vcp-pr__meta{font-family:var(--mono); font-size:.7rem; letter-spacing:.1em; text-transform:uppercase; color:var(--ink-soft)}
.vcp-pr--g{grid-column:span 3; grid-row:span 2; background:var(--slate); color:#fff; border-color:transparent; padding:clamp(26px,3.4vw,44px)}
.vcp-pr--g .vcp-pr__logo{height:74px; align-self:flex-start}
.vcp-pr--g h3{font-size:clamp(1.8rem,3.4vw,3rem); line-height:1.04; font-stretch:112%}
.vcp-pr--g h3::before{content:"\\201C"; display:block; font-size:2.4em; line-height:.55; color:var(--mint)}
.vcp-pr--g .vcp-pr__go{color:var(--mint)} .vcp-pr--g .vcp-pr__meta{color:var(--aqua)}
.vcp-pr--v, .vcp-pr--t{grid-column:span 3}
.vcp-pr--lst{grid-column:span 4; background:var(--aqua); border-color:transparent}
.vcp-pr--pn{grid-column:span 2; background:var(--logo-teal); color:#fff; border-color:transparent}
.vcp-pr--pn .vcp-pr__go{color:var(--mint)} .vcp-pr--pn .vcp-pr__meta{color:var(--aqua)}
.vcp-wm{font-family:var(--display); font-weight:900; line-height:.95; letter-spacing:-.01em}
.vcp-wm--lst{font-stretch:75%; font-size:1.5rem; text-transform:uppercase; color:var(--slate)}
.vcp-wm--lst i{font-style:normal; color:var(--teal)}
.vcp-wm--pn{font-stretch:125%; font-size:1.6rem; color:#fff}
.vcp-wm--pn i{font-style:normal; color:var(--mint)}
.vcp-lst{display:grid; grid-template-columns:minmax(0,1fr) minmax(0,1fr); gap:20px; align-items:center}
.vcp-lst .audio{background:var(--slate)}
.vcp-lst p{margin:0; font-size:.95rem}
.vcp-pods{display:grid; grid-template-columns:repeat(5,minmax(0,1fr)); gap:12px; margin-top:28px}
.vcp-pod{display:flex; gap:12px; align-items:center; text-decoration:none; color:var(--slate); padding:10px; border-radius:12px; border:1px solid var(--line); background:#fff; min-width:0}
.vcp-pod:hover{border-color:var(--teal)}
.vcp-pod img{width:58px; height:58px; border-radius:8px; object-fit:cover; flex:none}
.vcp-pod b{display:block; font-size:.84rem; line-height:1.25; font-weight:700}
.vcp-pod small{display:block; font-size:.72rem; color:var(--ink-soft); margin-top:2px; line-height:1.3}
@media (max-width:1100px){ .vcp-pods{grid-template-columns:repeat(3,minmax(0,1fr))} .vcp-pods .vcp-pod:nth-child(n+4){grid-column:span 1} }
@media (max-width:960px){ .vcp-press{grid-template-columns:1fr 1fr} .vcp-pr--g{grid-column:1/-1; grid-row:auto} .vcp-pr--v,.vcp-pr--t{grid-column:span 1} .vcp-pr--lst{grid-column:1/-1} .vcp-pr--pn{grid-column:1/-1} .vcp-lst{grid-template-columns:1fr} .vcp-pods{grid-template-columns:1fr 1fr} }
@media (max-width:620px){ .vcp-press{grid-template-columns:1fr} .vcp-pr--v,.vcp-pr--t{grid-column:1/-1} .vcp-pods{grid-template-columns:1fr} }

/* ---------- voices ---------- */
.vcp-pull{margin-bottom:clamp(22px,3vw,34px)}
.vcp-pull blockquote{margin:0; font-family:var(--display); font-weight:900; font-stretch:115%; font-size:clamp(2.2rem,5.4vw,5rem); line-height:.95; letter-spacing:-.025em; color:var(--slate)}
.vcp-pull blockquote::before{content:"\\201C"; display:inline-block; color:var(--teal); margin-right:.08em}
.vcp-pull .cite{color:var(--ink-soft)}
.vcp-note{background:#fff; border:1px solid var(--line); border-radius:20px; padding:clamp(22px,3vw,36px); box-shadow:var(--shadow)}
.vcp-note__body{columns:2 340px; column-gap:44px; column-rule:1px solid var(--line)}
.vcp-note__body p.hl{break-inside:avoid}
.vcp-note .tags{margin-top:18px; padding-top:14px; border-top:1px solid var(--line)}
.vcp-note__go{margin-left:auto}
.vcp-note__go .btn{box-shadow:none}
.vcp-note__head{display:flex; align-items:center; gap:12px; margin-bottom:16px}
.vcp-note__av{width:48px; height:48px; border-radius:50%; background:var(--slate); color:var(--mint); display:grid; place-items:center; font-family:var(--display); font-weight:900; font-stretch:115%; flex:none}
.vcp-note__head b{display:block; font-family:var(--display); font-stretch:106%; font-size:1.08rem}
.vcp-note__head small{display:block; color:var(--ink-soft); font-size:.82rem}
.vcp-note p{font-size:1rem; line-height:1.62}
.vcp-note p.hl{font-family:var(--display); font-weight:800; font-stretch:106%; font-size:1.18rem; background:var(--aqua); padding:10px 14px; border-radius:10px}
.vcp-note .tags{font-family:var(--mono); font-size:.7rem; color:var(--ink-soft); line-height:1.6; word-break:break-word}
.vcp-subs__lbl{margin:clamp(26px,3.2vw,40px) 0 14px}
.vcp-subs{display:grid; grid-template-columns:repeat(3,minmax(0,1fr)); gap:16px}
.vcp-sub{display:flex; flex-direction:column; gap:8px; padding:22px; border-radius:16px; background:var(--slate); color:#fff; text-decoration:none; transition:transform .2s, box-shadow .2s; border-top:6px solid var(--mint); min-width:0}
.vcp-sub:hover{transform:translateY(-4px); box-shadow:var(--shadow)}
.vcp-sub small{font-family:var(--mono); font-size:.68rem; letter-spacing:.1em; text-transform:uppercase; color:var(--mint)}
.vcp-sub b{font-family:var(--display); font-stretch:106%; font-size:1.22rem; line-height:1.18}
.vcp-sub span{color:rgba(255,255,255,.8); font-size:.92rem}
.vcp-sub em{margin-top:auto; padding-top:8px; font-style:normal; font-weight:800; color:var(--aqua); font-size:.9rem}
@media (max-width:900px){ .vcp-subs{grid-template-columns:1fr} }
@media (max-width:560px){ .vcp-note__head{flex-wrap:wrap} .vcp-note__go{margin-left:0; flex-basis:100%} }

/* ---------- adult guide ---------- */
.vcp-guide{display:grid; grid-template-columns:minmax(0,.62fr) minmax(0,1.38fr); gap:clamp(28px,5vw,64px); align-items:center}
.vcp-cover{position:relative}
.vcp-cover img{width:100%; max-width:340px; border-radius:6px; box-shadow:0 40px 70px -26px rgba(0,0,0,.7); transform:rotate(-4deg)}
.vcp-cover .sticker{position:absolute; right:4%; bottom:8%}
.vcp-guide .lede{color:#fff}
.vcp-shael{margin:22px 0 0; padding:18px 20px; border-left:4px solid var(--mint); background:rgba(255,255,255,.06); border-radius:0 12px 12px 0}
.vcp-shael p{font-family:var(--display); font-weight:700; font-stretch:104%; font-size:1.15rem; line-height:1.35; margin:0}
.vcp-shael cite{display:block; margin-top:8px; font-style:normal; font-family:var(--mono); font-size:.74rem; letter-spacing:.08em; text-transform:uppercase; color:var(--aqua)}
.vcp-gwrap{margin-top:clamp(28px,3.6vw,44px); background:#fff; color:var(--slate); border-radius:20px; padding:clamp(18px,2.6vw,30px)}
.vcp-gwrap .tabs{margin-bottom:20px}
.vcp-gwrap [role="tabpanel"]{min-height:300px}
.vcp-gsteps{list-style:none; margin:0; padding:0; counter-reset:g; display:grid; grid-template-columns:repeat(5,minmax(0,1fr)); gap:12px}
.vcp-gsteps li{margin:0; counter-increment:g; background:var(--mist); border-radius:14px; padding:18px; border:1px solid var(--line)}
.vcp-gsteps li::before{content:counter(g); display:block; font-family:var(--display); font-weight:900; font-stretch:125%; font-size:2.2rem; line-height:1; color:var(--teal); margin-bottom:10px}
.vcp-gsteps b{display:block; font-family:var(--display); font-stretch:106%; font-size:1.05rem; line-height:1.2; margin-bottom:6px}
.vcp-gsteps span{display:block; font-size:.88rem; color:var(--ink-soft); line-height:1.45}
.vcp-gnote{margin:18px 0 0; padding:14px 18px; border-radius:12px; background:var(--aqua); font-weight:600}
.vcp-says{display:grid; grid-template-columns:repeat(3,minmax(0,1fr)); gap:14px}
.vcp-says figure{margin:0; border-radius:16px; padding:20px; background:var(--slate); color:#fff}
.vcp-says figcaption{font-family:var(--mono); font-size:.68rem; letter-spacing:.12em; text-transform:uppercase; color:var(--mint); margin-bottom:10px; font-weight:600}
.vcp-says blockquote{margin:0; font-family:var(--display); font-weight:700; font-stretch:104%; font-size:1.06rem; line-height:1.4}
.vcp-says .vcp-avoid{grid-column:span 2}
.vcp-says__offer p{margin:12px 0 0; font-size:.92rem; color:var(--aqua)}
.vcp-says .vcp-avoid{background:var(--mist); color:var(--slate); border:1px solid var(--line)}
.vcp-says .vcp-avoid figcaption{color:var(--logo-teal)}
.vcp-says .vcp-avoid ul{margin:0; padding:0; list-style:none; display:grid; gap:12px}
.vcp-says .vcp-avoid li{font-size:1.04rem!important}
.vcp-says .vcp-avoid li{margin:0; padding-left:26px; position:relative; font-weight:600; font-size:.95rem; text-decoration:line-through; text-decoration-color:rgba(29,65,78,.45)}
.vcp-says .vcp-avoid li::before{content:""; position:absolute; left:0; top:4px; width:16px; height:16px; border-radius:50%; border:2px solid var(--logo-teal); background:url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 24 24'%3E%3Cpath d='M7 7l10 10M17 7L7 17' fill='none' stroke='%231d5a66' stroke-width='3' stroke-linecap='round'/%3E%3C/svg%3E") center/10px no-repeat}
.vcp-after{display:grid; grid-template-columns:repeat(4,minmax(0,1fr)); gap:12px}
.vcp-after > div{background:var(--mist); border:1px solid var(--line); border-radius:14px; padding:18px}
.vcp-after b{display:block; font-family:var(--display); font-stretch:106%; color:var(--logo-teal); margin-bottom:10px}
.vcp-after p{font-size:.92rem; line-height:1.45; margin:0 0 10px; padding-left:12px; border-left:3px solid var(--mint)}
.vcp-sig{display:grid; border:1px solid var(--line); border-radius:14px; overflow:hidden}
.vcp-sig > div{display:grid; grid-template-columns:minmax(0,.9fr) minmax(0,1.1fr)}
.vcp-sig > div > span{padding:12px 16px; border-top:1px solid var(--line); font-size:.94rem; line-height:1.45}
.vcp-sig > div > span:first-child{font-weight:700; background:var(--mist)}
.vcp-sig__h > span{background:var(--slate)!important; color:#fff; border-top:0!important; font-family:var(--mono); font-size:.7rem!important; letter-spacing:.1em; text-transform:uppercase; font-weight:600!important}
.vcp-avoids{display:grid; grid-template-columns:repeat(5,minmax(0,1fr)); gap:12px}
.vcp-avoids > div{border-radius:14px; padding:18px; background:var(--slate); color:#fff}
.vcp-avoids b{display:block; font-family:var(--display); font-stretch:106%; color:var(--mint); line-height:1.2; margin-bottom:8px}
.vcp-avoids p{margin:0; font-size:.88rem; line-height:1.45; color:rgba(255,255,255,.82)}
.vcp-acc summary{font-size:1.08rem}
@media (max-width:1100px){ .vcp-gsteps,.vcp-avoids{grid-template-columns:repeat(3,minmax(0,1fr))} .vcp-after{grid-template-columns:1fr 1fr} }
@media (max-width:860px){ .vcp-guide{grid-template-columns:1fr} .vcp-cover img{max-width:240px} .vcp-says{grid-template-columns:1fr} .vcp-says .vcp-avoid{grid-column:auto} }
@media (max-width:620px){ .vcp-gsteps,.vcp-avoids,.vcp-after{grid-template-columns:1fr} .vcp-sig > div{grid-template-columns:1fr} .vcp-sig > div > span:last-child{border-top:0; padding-top:0} .vcp-sig > div > span:first-child{background:transparent; padding-bottom:4px} .vcp-sig__h{display:none!important} .vcp-gwrap [role="tabpanel"]{min-height:0} .vcp-gwrap .tabs{flex-wrap:nowrap; overflow-x:auto; margin-inline:-4px; padding:0 4px 6px; scrollbar-width:none} .vcp-gwrap .tab{white-space:nowrap} }

/* ---------- final CTA ---------- */
.vcp-cta{text-align:center}
.vcp-cta__url{display:block; font-family:var(--display); font-weight:900; font-stretch:112%; font-size:clamp(1.9rem,6.6vw,6.4rem); line-height:.9; letter-spacing:-.035em; color:var(--slate); text-decoration:none; margin:0 0 .25em; overflow-wrap:anywhere}
.vcp-cta__url:hover{color:var(--logo-teal)}
.vcp-cta__url i{font-style:normal; color:var(--teal)}
.vcp-cta p{font-weight:600; font-size:var(--fs-lede); max-width:none}
.vcp-cta .btns{justify-content:center; margin-top:22px}
.vcp-cta .btn--slate{font-size:1.15rem; padding:.85em 1.6em}
'''

VC_JS = r'''
(function(){
  var d = document, reduce = matchMedia('(prefers-reduced-motion: reduce)').matches;
  /* hero question bubbles */
  var bubs = d.querySelectorAll('.vcp-bub'), bi = 0;
  if(bubs.length){
    if(reduce){ bubs.forEach(function(b){ b.classList.add('on'); }); }
    else {
      bubs[0].classList.add('on');
      setInterval(function(){ var shown = d.querySelectorAll('.vcp-bub.on'); if(shown.length >= 3){ shown[0].classList.remove('on'); } bi = (bi + 1) % bubs.length; bubs[bi].classList.remove('on'); void bubs[bi].offsetWidth; bubs[bi].classList.add('on'); }, 1700);
    }
  }
  /* how-it-works stepper */
  var list = d.querySelector('.vcp-steps');
  if(list){
    var items = list.querySelectorAll('li'), shots = d.querySelectorAll('.vcp-howphone img'), cap = d.querySelector('.vcp-howcap'), cur = 0, auto = !reduce, t0 = 0, dur = 5200, paused = false, seen = false, md = d.querySelector('.vcp-mdesc');
    function show(n, user){ items[cur].classList.remove('on'); items[cur].querySelector('button').setAttribute('aria-expanded','false'); shots[cur].classList.remove('on'); items[cur].querySelector('.bar').style.width = '0';
      cur = (n + items.length) % items.length; items[cur].classList.add('on'); items[cur].querySelector('button').setAttribute('aria-expanded','true'); shots[cur].classList.add('on'); cap.textContent = 'Step ' + (cur+1) + ' of ' + items.length; if(md){ md.querySelector('b').textContent = items[cur].querySelector('.t').textContent; md.querySelector('span').textContent = items[cur].querySelector('.d').textContent; } if(list.scrollWidth > list.clientWidth + 4){ var li = items[cur]; list.scrollTo({left: li.offsetLeft - list.offsetLeft - 8, behavior: reduce ? 'auto' : 'smooth'}); } t0 = performance.now(); if(user) auto = false; }
    items.forEach(function(li, i){ li.querySelector('button').addEventListener('click', function(){ show(i, true); }); });
    var stage = d.querySelector('.vcp-how');
    stage.addEventListener('mouseenter', function(){ paused = true; }); stage.addEventListener('mouseleave', function(){ paused = false; t0 = performance.now() - (parseFloat(items[cur].querySelector('.bar').style.width)||0)/100*dur; });
    if('IntersectionObserver' in window){ new IntersectionObserver(function(es){ es.forEach(function(e){ seen = e.isIntersecting; if(seen) t0 = performance.now(); }); }, {threshold:.35}).observe(stage); } else seen = true;
    function tick(t){ if(auto && !paused && seen){ var k = (t - t0) / dur; if(k >= 1){ show(cur + 1); k = 0; } items[cur].querySelector('.bar').style.width = (k*100) + '%'; } requestAnimationFrame(tick); }
    show(0); requestAnimationFrame(tick);
  }
})();
'''


def vibe_check():
    vc_lib = next(x for x in LIB if x['id'] == 'vibe-demo')
    steps_li = ''.join(f'<li class="{"on" if i == 0 else ""}"><button type="button" aria-expanded="{str(i == 0).lower()}" aria-controls="vcp-shot"><span class="n">{i+1}</span><span class="t">{esc(t)}</span><span class="d">{esc(dsc)}</span><span class="bar"></span></button></li>'
                       for i, (im, t, dsc) in enumerate(VC_STEPS))
    shots = ''.join(img(im, f'Vibe Check screen: {t}', cls='on' if i == 0 else '', loading='eager' if i < 2 else 'lazy') for i, (im, t, dsc) in enumerate(VC_STEPS))
    acct = ''.join(f'<div><b>{i+1}</b><h3>{esc(t)}</h3><p>{esc(dsc)}</p></div>' for i, (t, dsc) in enumerate(ACCOUNT))

    # podcasts that discuss Vibe Check (from data.PODCASTS, excluding the featured Longest Shortest Time episode)
    vc_pods = [p for p in PODCASTS if any(h == 'vibe-check.html' for _, h in p[7]) and p[0] != '0v2G7MraWG1V2iyXgGKOUF']
    pods_html = ''.join(f'<a class="vcp-pod" href="https://open.spotify.com/episode/{sid}" target="_blank" rel="noopener">{img("us-velasquez-mic" if sid == "5FpaHdterTLr0j9XxK5TGH" else "sp-" + sid.lower(), "")}<span><b>{esc(title)}</b><small>{esc(show.split(" · ")[0])}</small></span></a>'
                        for sid, title, show, date, desc, topics, kw, links in vc_pods)

    note = ''.join(f'<p{" class=hl" if "Accountability is relational" in p else ""}>{esc(p)}</p>' for p in SHATTUCK)
    subs = ''.join(f'<a class="vcp-sub" href="{u}" target="_blank" rel="noopener"><b>{esc(t)}</b><span>{esc(s)}</span><em>Read on Substack &#8599;</em></a>' for t, s, u in SUBSTACK)

    gtabs = ''.join(f'<button class="tab" role="tab" id="tab-g-{k}" aria-controls="gp-{k}" aria-selected="{str(i == 0).lower()}" tabindex="{0 if i == 0 else -1}">{esc(lbl)}</button>' for i, (k, lbl, _) in enumerate(GUIDE_TABS))
    gpanels = ''.join(f'<div role="tabpanel" id="gp-{k}" aria-labelledby="tab-g-{k}"{"" if i == 0 else " hidden"}>{html_}</div>' for i, (k, lbl, html_) in enumerate(GUIDE_TABS))

    body = f'''
<section class="vcp-hero">
  <div class="wrap">
    <div>
      <nav class="crumbs" aria-label="Breadcrumb"><a href="index.html">Home</a><span>/</span><a href="resources.html">Resources</a><span>/</span><span>Vibe Check</span></nav>
      <div class="vcp-mark"><span class="daisy"></span>Vibe Check by SafeBAE</div>
      <h1 aria-label="Vibe Check"><span>Vibe</span><span>Check</span></h1>
      <p class="vcp-tag">No judgment. Just answers.</p>
      <p class="lede">CheckYourVibe.org is a free, anonymous reflection tool for young people who are questioning whether they, or a friend, may have crossed a boundary or caused harm.</p>
      <div class="btns">{btn('Open Vibe Check', CYV, 'mint', size='')}{btn('Watch the demo', '#demo', 'white', arrow=True)}{btn('Adult guide (PDF)', GUIDE_PDF, 'ghost')}</div>
      <div class="vcp-privacy"><span>No account</span><span>No names</span><span>Nothing stored</span><span>Free</span></div>
    </div>
    <div class="vcp-stage" aria-hidden="true">
      <span class="vcp-bub vcp-bub--l" style="left:0;top:9%">Did I harm someone?</span>
      <span class="vcp-bub vcp-bub--r" style="right:0;top:22%">Was that consent?</span>
      <span class="vcp-bub vcp-bub--l" style="left:2%;top:44%">Did I cross a boundary?</span>
      <span class="vcp-bub vcp-bub--r" style="right:2%;top:60%">Am I a bad person?</span>
      <span class="vcp-bub vcp-bub--l" style="left:6%;top:78%">Not sure if you crossed a line?</span>
      <div class="vcp-phone">{img('vc-screen', '', loading='eager')}</div>
      <span class="sticker sticker--coral" style="left:14%;bottom:6%">Quick exit on every screen</span>
    </div>
  </div>
</section>

<section class="band band--slate">
  <div class="wrap vcp-why">
    <div>
      <p class="eyebrow">Why Vibe Check exists</p>
      <h2>Young people are taking hard questions about consent to AI chatbots and anonymous forums.</h2>
      <p class="lede" style="color:#fff">AI is designed to tell you what you want to hear. It doesn’t help you reflect or take accountability.</p>
      <p>Vibe Check guides users through confusing situations and connects them with real, evidence-based resources on consent, communication, and accountability. It exists because many people have questions about situations that didn’t feel clear and want to do better, but aren’t sure where to start.</p>
      <div class="btns" style="margin-top:22px">{btn('Read: when AI just agrees with you', 'https://safebae.substack.com/p/when-you-ask-ai-for-advice-and-it', 'ghost', 'sm')}</div>
    </div>
    <div class="vcp-vs">
      <div class="vcp-vs__ai"><small>AI chatbots &amp; forums</small><b>Designed to tell you what you want to hear.</b></div>
      <div class="vcp-vs__vc"><small>Vibe Check</small><b>“We’re not here to judge you. We’re here to help you slow down, learn, and choose safer next steps.”</b>{chips(['Not AI advice', 'Evidence-based resources', 'Anonymous'])}</div>
    </div>
  </div>
</section>

<section class="band band--paper" id="how">
  <div class="wrap">
    <div class="section-head"><div><p class="eyebrow">How it works</p><h2>One step at a time, at your own pace</h2>
      <p class="lede lede--full muted">Vibe Check asks about a situation and how you’re feeling, then shows tools and information based on your answers. There are no right or wrong answers, no pressure to finish, and you can stop at any point.</p></div></div>
    <div class="vcp-how">
      <div class="vcp-howlist">
        <ol class="vcp-steps">{steps_li}</ol>
        <div class="vcp-tools"><b>On every screen</b><span class="x">Quick Exit</span><span class="c">In crisis? 988 &middot; text HOME to 741741</span><span>Resources</span><span>Restart</span><span>Breathe</span></div>
      </div>
      <div class="vcp-howstage"><div class="vcp-howphone" id="vcp-shot">{shots}</div><span class="vcp-howcap">Step 1 of {len(VC_STEPS)}</span></div>
      <div class="vcp-mdesc" aria-hidden="true"><b></b><span></span></div>
    </div>
  </div>
</section>

<section class="band band--deep" id="demo">
  <div class="wrap vcp-demo">
    {yt(vc_lib['yt'], 'Vibe Check Demo', label='Demo')}
    <div>
      <p class="eyebrow">See it in action</p>
      <h2>Watch the Vibe Check demo</h2>
      <p style="color:rgba(255,255,255,.85)">A walkthrough of CheckYourVibe.org, from the first screen to the next steps it offers.</p>
      <div class="btns" style="margin-top:20px">{btn('Try it yourself', CYV, 'mint')}</div>
    </div>
  </div>
</section>

<section class="band band--aqua">
  <div class="wrap">
    <div class="section-head"><div><p class="eyebrow">Built on a framework for accountability</p><h2>The four parts of accountability</h2>
      <p class="lede lede--full">Vibe Check follows a framework named by Mia Mingus, drawn from transformative justice. Accountability has four parts, and they go in order.</p></div></div>
    <div class="vcp-acct">{acct}</div>
  </div>
</section>

<section class="band band--slate">
  <div class="wrap">
    <p class="eyebrow">Privacy</p>
    <h2 class="vcp-big">Nothing is <span>stored.</span></h2>
    <p class="lede lede--full" style="color:rgba(255,255,255,.9)">No data is collected. Nothing is stored. It disappears when the browser closes. Vibe Check collects no names, no account info, and does not report anything to anyone.</p>
    <div class="vcp-isnt">
      <div class="vcp-col vcp-col--is"><h3>What Vibe Check is</h3><ul>
        <li><div><b>Completely private</b><span>No accounts, no tracking, no history. Nothing is saved or sent anywhere.</span></div></li>
        <li><div><b>Non-punitive</b><span>Designed to build awareness and accountability, not to condemn, label, or shame.</span></div></li>
        <li><div><b>Self-paced and self-guided</b><span>There are no right or wrong answers, and no pressure to finish.</span></div></li>
        <li><div><b>Practical next steps</b><span>Interactive activities, guided lessons, grounding exercises, and support resources.</span></div></li>
      </ul></div>
      <div class="vcp-col vcp-col--not"><h3>What it isn’t</h3><ul>
        <li><div><b>AI advice</b><span>It connects you with real, evidence-based resources on consent, communication, and accountability.</span></div></li>
        <li><div><b>Legal advice</b><span>It doesn’t make legal determinations, determine guilt, or assign labels.</span></div></li>
        <li><div><b>A replacement for professional support</b><span>It is a self-guided reflection tool, not therapy, and not a crisis intervention.</span></div></li>
        <li><div><b>Something to assign</b><span>Making it mandatory or punitive will guarantee it doesn’t work.</span></div></li>
      </ul></div>
    </div>
    <div class="vcp-crisis"><p>If a young person has been involved in a serious incident, experienced trauma, or is in crisis, please connect them with a qualified counselor or crisis service.</p><button class="btn btn--slate btn--sm" data-open-help>Get help now</button></div>
  </div>
</section>

<section class="band band--paper" id="press">
  <div class="wrap">
    <div class="section-head"><div><p class="eyebrow">In the press</p><h2>Vibe Check in the news</h2></div></div>
    <div class="vcp-press">
      <a class="vcp-pr vcp-pr--g" href="https://www.theguardian.com/us-news/2026/may/06/sexual-consent-assault-online-tool" target="_blank" rel="noopener">
        <span class="vcp-pr__logo">{img('the-guardian-logo-vector', 'The Guardian')}</span>
        <span class="vcp-pr__meta">The Guardian &middot; May 2026</span>
        <h3>Young people want to know whether they’ve perpetrated a sexual assault.</h3>
        <span class="vcp-pr__go">Read in The Guardian &#8599;</span>
      </a>
      <a class="vcp-pr vcp-pr--v" href="https://www.vox.com/technology/481444/ai-chatgpt-teen-boys-teenagers-dating-relationships" target="_blank" rel="noopener">
        <span class="vcp-pr__logo">{img('vox-logo-svg-1', 'Vox')}</span>
        <h3>Teen boys are using ChatGPT as their wingman. What could go wrong?</h3>
        <span class="vcp-pr__go">Read on Vox &#8599;</span>
      </a>
      <a class="vcp-pr vcp-pr--t" href="https://www.trendwatching.com/innovations/when-teens-worry-they-may-have-crossed-a-boundary-vibe-check-helps-them-think-it-through" target="_blank" rel="noopener">
        <span class="vcp-pr__logo">{img('public', 'TrendWatching')}</span>
        <h3>When teens worry they crossed a boundary, Vibe Check helps them.</h3>
        <span class="vcp-pr__go">Read on TrendWatching &#8599;</span>
      </a>
      <div class="vcp-pr vcp-pr--lst">
        <span class="vcp-wm vcp-wm--lst">The Longest <i>Shortest</i> Time</span>
        <div class="vcp-lst">
          <div><h3>“Preventing Teens from Joining the Manosphere”</h3><p style="margin-top:10px">Drew Davis joins Hillary Frank on <a class="link" href="https://longestshortesttime.com/episode-255-preventing-teens-from-joining-the-manosphere" target="_blank" rel="noopener">The Longest Shortest Time</a> to talk about Vibe Check, the rise of AI and online forums as relationship advice spaces, and why young people need better pathways to reflect, take accountability, and repair harm.</p></div>
          {spotify('0v2G7MraWG1V2iyXgGKOUF', 'Preventing Teens from Joining the Manosphere', 'The Longest Shortest Time')}
        </div>
      </div>
      <a class="vcp-pr vcp-pr--pn" href="https://www.positive.news/" target="_blank" rel="noopener">
        <span class="vcp-wm vcp-wm--pn">Positive <i>News</i></span>
        <span class="vcp-pr__meta">Print magazine &middot; Issue 127</span>
        <h3>A feature on Vibe Check in the October–December 2026 issue.</h3>
        <span class="vcp-pr__go">Visit Positive News &#8599;</span>
      </a>
    </div>
    <p class="eyebrow" style="margin-top:34px">Also heard on</p>
    <div class="vcp-pods" style="margin-top:0">{pods_html}</div>
  </div>
</section>

<section class="band band--mist">
  <div class="wrap">
    <div class="vcp-pull">
      <p class="eyebrow">What people are saying</p>
      <blockquote>Accountability is relational.</blockquote>
      <span class="cite">Dominick Shattuck, PhD, on Vibe Check</span>
    </div>
    <article class="vcp-note">
      <div class="vcp-note__head"><span class="vcp-note__av" aria-hidden="true">DS</span><div><b>Dominick Shattuck, PhD</b><small>Note on Substack</small></div><span class="vcp-note__go">{btn('Read on Substack', 'https://substack.com/@dominickmenshealth/note/c-255823866', 'slate', 'sm')}</span></div>
      <div class="vcp-note__body">{note}
      <p>Explore Vibe Check here: <a class="link" href="{CYV}" target="_blank" rel="noopener">https://checkyourvibe.org/</a></p></div>
      <p class="tags">{esc(SHATTUCK_TAGS)}</p>
    </article>
    <p class="eyebrow vcp-subs__lbl">From SafeBAE on Substack</p>
    <div class="vcp-subs">{subs}</div>
  </div>
</section>

<section class="band band--logo" id="adults">
  <div class="wrap">
    <div class="vcp-guide">
      <div class="vcp-cover">{img('guide-vibe-check', 'Cover of Check Their Vibe: An Adults’ Guide to Vibe Check')}<span class="sticker sticker--r">Free PDF &middot; 7 pages</span></div>
      <div>
        <p class="eyebrow">For parents, caregivers &amp; adult allies</p>
        <h2>Check Their Vibe: an adults’ guide</h2>
        <p class="lede">Vibe Check is a free, private, self-guided reflection tool for young people navigating moments of sexual uncertainty. This guide helps you introduce it thoughtfully, follow up with care, and understand what it actually contains.</p>
        <div class="btns">{btn('Download the guide (PDF)', GUIDE_PDF, 'mint')}{btn('Go through Vibe Check yourself', CYV, 'ghost')}</div>
        <blockquote class="vcp-shael"><p>“As the founding Executive Director of SafeBAE and a mom, this might be the most important tool we’ve developed.”</p><cite>Shael Norris, SafeBAE</cite></blockquote>
      </div>
    </div>
    <div class="vcp-gwrap" data-tabs="vcp-guide">
      <div class="tabs" role="tablist" aria-label="Inside the guide">{gtabs}</div>
      {gpanels}
    </div>
  </div>
</section>

<section class="band band--mint">
  <div class="wrap vcp-cta">
    <p class="eyebrow">Vibe Check by SafeBAE</p>
    <a class="vcp-cta__url" href="{CYV}" target="_blank" rel="noopener">checkyour<i>vibe</i>.org</a>
    <p>No account. No names. No judgment. Just unfiltered answers.</p>
    <div class="btns">{btn('Open Vibe Check', CYV, 'slate')}<button class="btn btn--coral" data-open-help>In crisis? Call or text 988</button></div>
  </div>
</section>
{give_band()}
'''
    page('vibe-check.html', 'Vibe Check · SafeBAE',
         'Vibe Check (CheckYourVibe.org) is a free, anonymous reflection tool for young people questioning whether they or a friend crossed a boundary or caused harm. No account, nothing stored.',
         body, active='resources', body_class='vcp', head_extra=f'<style>{VC_CSS}</style>', scripts=f'<script>{VC_JS}</script>')


def build():
    resources()
    vibe_check()


if __name__ == '__main__':
    build()
