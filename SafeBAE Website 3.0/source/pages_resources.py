"""Resources hub (resources.html): the landing page of the Resources tab."""
import os
from lib import *
from data import LIB, FAQ, library_items
from pages_home import cpet_player

WP = 'https://www.safebae.org/wp-content/uploads/'
CYV = 'https://checkyourvibe.org/'
GUIDE_PDF = WP + '2026/03/Check-Their-Vibe-A-Guide-to-Vibe-Check.pdf'
SKILLS = 'https://skills-lab.safebae.org/'
SKILLS_PAGE = 'skills-lab.html'

ARROW = '<span aria-hidden="true">&rarr;</span>'
NE = '<span aria-hidden="true">&#8599;</span>'


def go(href):
    return NE if href.startswith('http') else ARROW


def ext_attrs(href):
    return ' target="_blank" rel="noopener"' if href.startswith('http') else ''


# =====================================================================
#  RESOURCES HUB
# =====================================================================

# the Assemblies page's own photo if that page's builder has added it, else a SafeBAE assembly photo already in the set
ASSEMBLY_IMG = 'assembly-stage-group' if os.path.exists(f'{SITE}/assets/img/assembly-stage-group.webp') else 'img-2395'


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
        'film-rape-culture.html': 'Charlie Coleman, with Teen Vogue, on rape culture and how to shift it.',
        'film-sexual-assault-of-men.html': 'Survivor and SafeBAE Board Member Theo Hutt shares his story.',
    }
    for f in films:
        f['d'] = film_lines.get(f['h'], f['d'])

    shelves = [
      ('tools', 'Interactive tools & training', 'Self-paced training, private reflection and short games you can do on your own or with a group.', [
        dict(t='Certified Peer Educator Training', d='Prepares students to lead sexual violence prevention in their schools and communities.', h='peer-educator.html', im='preview1', c=['16 modules', 'Self-paced', 'Free'], a=[S, E], k='cpet certification peer educator course online leadership'),
        dict(t='SafeBAE AI Literacy Training', d='For high school and college students, from how AI works to fake images and sextortion. Launches October 26–30, 2026.', h='ai-literacy.html', im='ai-illo-hello', c=['New', '6 modules', 'Ages 13+'], a=[S, P, E], k='ai artificial intelligence chatbot media literacy week feeds algorithms deepfake nudify sextortion relationships', new=True),
        dict(t='Vibe Check', d='A free and anonymous tool for young people who are worried they may have crossed a boundary or caused harm.', h='vibe-check.html', im='vc-step-start', c=['Anonymous', 'Nothing stored'], a=[S, P, E], k='checkyourvibe accountability reflection harm repair consent', feat='vibe'),
        dict(t='BAE Skills Lab', d='Interactive activities about consent, boundaries, and what a healthy relationship actually looks like.', h=SKILLS_PAGE, im='sl-home', c=['6 activities', 'Games'], a=[S, E], k='games practice interactive skills lab'),
        dict(t='Boundary Flags', d='Sort 25 real situations into green, yellow and red flags to identify and understand your own boundaries.', h=SKILLS + 'boundary-flags/', im='sl-boundary-flags', c=['Skills Lab', '5 min'], a=[S, E], k='game boundaries red flags green flags'),
        dict(t='Partner Nutrition Label', d='Relationships don’t come with a label, so build your own and keep it as a bookmark.', h=SKILLS + 'nutrition-label/', im='sl-nutrition-label', c=['Skills Lab', '3–8 min'], a=[S], k='healthy relationship partner game'),
        dict(t='Supporting a Survivor: Helpful or Harmful?', d='Sort things people actually say to survivors into what helps and what hurts.', h=SKILLS + 'supporting-a-survivor/', im='sl-supporting-a-survivor', c=['Skills Lab', '3 min'], a=[S, P, E], k='support survivor disclosure what to say game'),
        dict(t='Reset Kit', d='Guided breathing and grounding for when you’re overwhelmed, numb, or checked out.', h=SKILLS + 'reset-kit/', im='sl-reset-kit', c=['Skills Lab', 'Under 2 min'], a=[S, P, E], k='breathing grounding calm self-care'),
        dict(t='Listen Closer', d='Hear a clip from a song everyone knows, then decide together: are these lyrics healthy or unhealthy?', h=SKILLS + 'listen-closer/', im='sl-listen-closer', c=['Skills Lab', '5 min'], a=[S, E], k='music lyrics song game classroom'),
        dict(t='SafeBAE Jeopardy', d='A 25-question game show on consent and healthy relationships.', h=SKILLS + 'jeopardy/', im='sl-jeopardy', c=['Skills Lab', '10–30 min'], a=[S, E], k='quiz trivia game classroom group'),
        dict(t='SafeBAE Clubs', d='Start or lead a student chapter, with materials, training, direct support and a national network of student leaders.', h='clubs.html', im='clubhero', c=['Free registration', 'Club Hub'], a=[S, E], k='club chapter organizing student group advisor'),
        dict(t='Entrenamiento en español', d='El entrenamiento para ser educadores certificados, en español: 16 módulos a su propio ritmo.', h='espanol.html', im='dsc01134', c=['Español', '16 módulos'], a=[S], k='spanish espanol peer educator training latam'),
        dict(t='Faculty & Staff Training', d='Trauma-informed professional development for teachers, staff and administrators, in person or virtually.', h='professional-development.html', im='us-gariev-teacher2', c=['In person', 'Virtual'], a=[E], k='professional development teachers staff training disclosure'),
      ]),
      ('watch', 'Watch, listen & read', 'Films envisioned, written, directed and performed by young people, plus podcasts and stories.', [
        dict(t='Films & videos', d='Every youth-created film in the Library, most paired with a ready-to-teach guide.', h='library.html#films', g='films', c=['Video', f'{n_vid} films & videos'], a=[S, P, E], k='videos films youtube library watch'),
        dict(t='Podcasts', d='Conversations SafeBAE’s founders, staff and student leaders were invited into.', h='library.html#podcasts', g='pods', c=['Audio', f'{n_pod} episodes'], a=[S, P, E], k='podcast listen audio spotify interview'),
        *films,
        dict(t='Vibe Check demo', d='A walkthrough of Vibe Check, the free, anonymous reflection tool.', h='vibe-check.html#demo', im='yt-ng8s3w1etru', c=['Video', 'Demo'], a=[S, P, E], k='vibe check demo walkthrough accountability'),
        dict(t='Blog', d='Stories from survivors, SafeBAE news, media analysis and policy updates.', h='blog.html', im='img-9509-1', c=['Articles'], a=[S, P, E], k='blog news stories articles read'),
      ]),
      ('classroom', 'Classroom materials', 'Guides, lessons and programs for classrooms, clubs and whole schools.', [
        dict(t='Teaching guides', d='Structured prompts, classroom activities and facilitation tips paired with each youth-led film.', h='library.html#guides', im='guide-red-flags', c=['PDF', f'{n_gui} guides', 'Free'], a=[E, P], k='teaching guide lesson plan discussion prompts activities pdf', cover=True),
        dict(t='Healthy Relationship & Consent Curriculum', d='15 interactive modules aligned with the National Health Education Standards, in English and Spanish.', h='consent-curriculum.html', im='preview5', c=['15 lessons', '45–60 min each', 'NHES'], a=[E], k='curriculum lessons nhes health class consent'),
        dict(t='Race, Rape Culture, and Resistance', d='A four-lesson learning series centered on Black youth.', h='film-race-rape-culture-resistance.html', im='2l3a1960', c=['Series', '4 lessons'], a=[S, E], k='racial justice black youth history lessons series'),
        dict(t='Choking Hazard warning posters', d='Free warning posters and the warning sticker from SafeBAE’s Choking Hazard campaign.', h='https://chokinghazard.org/resources/#downloads', g='poster', c=['New', 'Free posters'], a=[S, E], k='choking strangulation warning poster sticker download print campaign', new=True),
        dict(t='Posters', d='Free downloadable posters for classrooms, counseling offices, hallways and wellness centers.', h='posters.html', im='everyone-can-do-something-1', c=['Download', 'Print'], a=[S, E], k='posters print download classroom hallway', cover=True),
        dict(t='Request a Program', d='Bring SafeBAE to your school or community for workshops, assemblies, and comprehensive school programming.', h='request-a-program.html', im='066', c=['Workshops', 'Trainings'], a=[E, P], k='assembly workshop booking school program speaker pricing'),
        dict(t='Assemblies', d='One-time events at your school, co-presented with youth leaders.', h='assemblies.html', im=ASSEMBLY_IMG, c=['For schools', 'One-time event'], a=[E, P], k='assembly assemblies school event speaker presentation youth leaders booking'),
        dict(t='SafeBAE 360° Schools', d='SafeBAE’s whole-school approach: a survivor-centered prevention model with six components, adapted to each school.', h='360-schools.html', im='safebae-consent-summits', c=['Whole-school approach', '6 components'], a=[E], k='360 schools whole school model prevention program approach'),
      ]),
      ('rights', 'Rights & facts', 'Know your rights at school and what the research says.', [
        dict(t='Choking Hazard', d='SafeBAE’s campaign on sexual strangulation: the evidence, myth vs fact, and the signs that need medical care.', h='choking-hazard.html', g='hazard', c=['New', 'Myth vs fact'], a=[S, P, E], k='choking strangulation sex safety campaign medical er myth fact consent', new=True),
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
    g = it.get('g')
    if g == 'faq':
        media = '<span class="rs-tile__media rs-g rs-g--faq" aria-hidden="true"><b>?</b><i>FAQ</i></span>'
    elif g in ('hazard', 'poster'):
        media = f'<span class="rs-tile__media rs-g rs-g--hz" aria-hidden="true">{hz_label("hz--tilt")}</span>'
    elif g == 'hotline':
        media = '<span class="rs-tile__media rs-g rs-g--help" aria-hidden="true"><b>24/7</b><i>Text LOVEIS to 22522</i></span>'
    elif g == 'films':
        media = '<span class="rs-tile__media rs-tile__media--mosaic">' + ''.join(img(n, '') for n in FILM_STILLS) + '</span>'
    elif g == 'pods':
        media = '<span class="rs-tile__media rs-tile__media--covers">' + ''.join(img(n, '') for n in POD_COVERS) + '</span>'
    else:
        cls = 'rs-tile__media'
        if it.get('cover'): cls += ' rs-tile__media--cover'
        if it.get('logo'): cls += ' rs-tile__media--logo'
        if it.get('feat') == 'vibe': cls += ' rs-tile__media--phone'
        media = f'<span class="{cls}">{img(it["im"], "")}</span>'
    chips_html = ''.join(f'<span>{esc(c)}</span>' for c in it['c'])
    q = ' '.join([it['t'], it['d'], ' '.join(it['c']), ' '.join(it['a']), it.get('k', '')]).lower()
    extra = ' data-open-help' if it.get('help') else ''
    cls = 'rs-tile' + (' rs-tile--vibe' if it.get('feat') == 'vibe' else '') + (' rs-tile--help' if it.get('help') else '') + (' rs-tile--new' if it.get('new') else '')
    return (f'<a class="{cls}" href="{esc(h)}"{ext_attrs(h)}{extra} data-aud="{" ".join(it["a"])}" data-q="{esc(q)}" role="listitem">'
            f'{media}<b>{esc(it["t"])}</b><small>{esc(it["d"])}</small>'
            f'<span class="rs-tile__foot"><span class="rs-tile__chips">{chips_html}</span><span class="rs-tile__go">{go(h)}</span></span></a>')


# stills for the "Films & videos" tile (films further along the shelf, so no still repeats beside it)
FILM_STILLS = ['yt-rixb8vlmajy', 'qts-full-cast-copy-2', 'knowb4unude', 'yt-j50puimluv4']
# three show covers for the "Podcasts" tile
POD_COVERS = ['sp-042usrg0amabkto66wqqwc', 'sp-0v2g7mrawg1v2iyxggkouf', 'sp-0jfmjbj7zvism8m7gp39ys']


def shelves_html():
    out = []
    for key, title, desc, items in shelf_items():
        out.append(f'''<section class="rs-shelf" id="shelf-{key}" data-shelf aria-labelledby="sh-{key}">
  <div class="rs-shelf__head">
    <h3 id="sh-{key}">{esc(title)} <span class="rs-shelf__n" data-n>{len(items)}</span></h3>
    <div class="rs-shelf__nav"><button type="button" data-dir="-1" aria-label="Scroll {esc(title)} left">&#8249;</button><button type="button" data-dir="1" aria-label="Scroll {esc(title)} right">&#8250;</button></div>
    <p>{esc(desc)}</p>
  </div>
  <div class="rs-shelf__row" role="list">{''.join(tile(i) for i in items)}</div>
  <div class="rs-shelf__ledge" aria-hidden="true"><i></i></div>
</section>''')
    return ''.join(out)


AUD = [
  ('students', 'Students', '1-000383-edited', 'Student resources', 'Free tools made by young people, for students.',
   'Free tools for understanding consent, finding support, reflecting on harm, and creating change at school.',
   [('AI Literacy Training', 'ai-literacy.html'), ('Survivor Support', 'survivor-support.html'), ('FAQ', 'faq.html'), ('Title IX', 'title-ix.html'), ('Posters', 'posters.html')],
   [('Free certification', 'Certified Peer Educator Training', 'Build the knowledge and skills to lead prevention work with your peers.', 'peer-educator.html', 'preview1', ''),
    ('Games & practice', 'Skills Lab', 'Interactive activities about consent, boundaries, and what a healthy relationship actually looks like.', SKILLS_PAGE, 'sl-boundary-flags', 'top'),
    ('Student organizing', 'SafeBAE Clubs', 'Start a chapter or bring prevention activities into an existing student group.', 'clubs.html', 'clubtabling', ''),
    ('Anonymous tool', 'Vibe Check', 'Look back privately at something you did or said, and learn how to take accountability and repair harm.', CYV, 'vc-step-start', 'phone')]),
  ('parents', 'Parents & Caregivers', 'us-sometale-parent', 'Parent & caregiver resources', 'Support the young people in your life.',
   'Resources for answering questions, responding to disclosures, and connecting young people with help.',
   [('Choking Hazard', 'choking-hazard.html'), ('Myths & Facts', 'myths-facts.html'), ('Teaching Guides', 'library.html#guides'), ('Podcasts', 'library.html#podcasts'), ('Blog', 'blog.html')],
   [('Support & healing', 'Supporting a Survivor', 'Learn how to respond to a disclosure and support a young survivor.', 'survivor-support.html', '000263', ''),
    ('Learn more', 'Frequently Asked Questions', 'SafeBAE answers your questions about teen dating violence, sexual assault, consent, and healthy relationships.', 'faq.html', 'relationships-2-1', ''),
    ('Watch or listen together', 'Videos & Podcasts', 'Watch or listen to SafeBAE media with a young person and use it to start a conversation.', 'library.html#films', 'yt-rixb8vlmajy', ''),
    ('Resource to share', 'Vibe Check', 'Share an anonymous reflection tool with a young person worried about their own behavior.', 'vibe-check.html#adults', 'guide-vibe-check', 'cover')]),
  ('educators', 'Educators', 'img-2395', 'Educator resources', 'Bring <span class="nb">youth-led</span> prevention to your school.',
   'Classroom materials, student leadership pathways, and support for strengthening prevention in your school.',
   [('AI Literacy Training', 'ai-literacy.html'), ('Vibe Check', CYV), ('Posters', 'posters.html'), ('Title IX', 'title-ix.html'), ('Request a Program', 'request-a-program.html')],
   [('Classroom-ready', 'Teaching Guides', 'Use structured activities, prompts, and facilitation guidance with students.', 'library.html#guides', 'guide-baecode', 'cover'),
    ('Youth-created media', 'Videos & Podcasts', 'Explore SafeBAE media to open real conversations about consent, harm, and relationships.', 'library.html#films', 'yt-ett8bnlbwwg', ''),
    ('Student leadership', 'Certified Peer Educator Training', 'Connect students with SafeBAE’s free, self-paced youth leadership certification.', 'peer-educator.html', 'preview1', ''),
    ('School organizing', 'SafeBAE Clubs', 'Help students establish and sustain youth-led prevention work at school.', 'clubs.html', 'clubhero', '')]),
]


def audience_html():
    tabs, panels = [], []
    for i, (k, label, im, eb, h3, p, also, cards) in enumerate(AUD):
        sel = i == 0
        tabs.append(f'<button class="rs-aud__tab" role="tab" id="tab-{k}" aria-controls="p-{k}" aria-selected="{str(sel).lower()}" tabindex="{0 if sel else -1}">'
                    f'<span class="rs-aud__face">{img(im, "")}</span><span><small>For</small><b>{esc(label)}</b></span><em>{len(cards)} picks</em></button>')
        cards_html = ''.join(
            f'<a class="rs-acard" href="{esc(u)}"{ext_attrs(u)}><span class="rs-acard__img{(" rs-acard__img--" + kind) if kind else ""}">{img(ci, "")}</span>'
            f'<span class="rs-acard__body"><small>{esc(kick)}</small><b>{esc(t)}</b><span>{esc(d)}</span></span><span class="rs-acard__go">{go(u)}</span></a>'
            for kick, t, d, u, ci, kind in cards)
        also_html = ''.join(f'<a href="{esc(u)}"{ext_attrs(u)}>{esc(t)}{" &#8599;" if u.startswith("http") else ""}</a>' for t, u in also)
        panels.append(f'''<div class="rs-aud__panel" role="tabpanel" id="p-{k}" aria-labelledby="tab-{k}"{'' if sel else ' hidden'}>
  <div class="rs-aud__intro">
    <div class="rs-aud__img">{img(im, '')}</div>
    <div class="rs-aud__txt"><p class="eyebrow">{esc(eb)}</p><h3>{h3}</h3><p>{esc(p)}</p>
    <div class="rs-also"><span>Also useful</span><div>{also_html}</div></div></div>
  </div>
  <div class="rs-aud__cards">{cards_html}</div>
</div>''')
    return f'<div data-tabs="rs-aud"><div class="rs-aud__tabs" role="tablist" aria-label="Browse by who you are">{"".join(tabs)}</div>{"".join(panels)}</div>'


RS_CSS = '''
/* The whole page sits on one three-column grid: the bento, the audience panel and the shelves share its lines. */
/* ---------- hero ---------- */
.rs-hero{background:var(--slate-deep); background-image:var(--grain); color:#fff; position:relative; overflow:hidden}
.rs-hero .wm-daisy{right:-10%; bottom:-30%}
.rs-hero .wrap{position:relative; z-index:2; display:grid; grid-template-columns:minmax(0,1.05fr) minmax(0,.95fr); gap:clamp(28px,4vw,56px); align-items:center; padding-block:clamp(44px,5.5vw,76px) clamp(40px,5vw,64px)}
.rs-hero h1{font-size:clamp(2.6rem,5vw,5rem); font-stretch:125%; font-weight:900; text-transform:uppercase; line-height:.84; letter-spacing:-.03em; margin:0 0 .3em}
.rs-hero .mk{background:none; color:var(--mint); display:block; padding:0}
.rs-hero .eyebrow{color:var(--mint)}
.rs-hero .lede{color:rgba(255,255,255,.9); max-width:none}
.rs-search{display:flex; align-items:center; gap:12px; background:#fff; border-radius:14px; padding:6px 6px 6px 18px; box-shadow:0 20px 50px -20px rgba(0,0,0,.6); margin-top:6px}
.rs-search svg{width:24px; height:24px; color:var(--teal); flex:none}
.rs-search input{flex:1; min-width:0; border:0; outline:0; font:inherit; font-size:1.12rem; padding:12px 0; color:var(--slate); background:transparent}
.rs-search input::-webkit-search-cancel-button{cursor:pointer}
.rs-search .btn{box-shadow:none}
.rs-search:focus-within{box-shadow:0 0 0 3px var(--mint), 0 20px 50px -20px rgba(0,0,0,.6)}
.rs-hint{display:inline-flex; margin-top:14px; font-weight:700; color:var(--mint); text-decoration:underline; text-underline-offset:3px}
.rs-searching .rs-who{display:none}
.rs-who{display:flex; flex-wrap:wrap; gap:8px; margin-top:18px; align-items:center}
.rs-who span{font-family:var(--mono); font-size:.72rem; letter-spacing:.1em; text-transform:uppercase; color:var(--aqua); margin-right:4px}
.rs-who button{font:inherit; font-weight:700; font-size:.92rem; color:#fff; background:rgba(255,255,255,.07); border:1.5px solid rgba(209,254,255,.3); border-radius:999px; padding:8px 15px; min-height:40px; cursor:pointer; transition:border-color .2s, color .2s, background .2s}
.rs-who button:hover{border-color:var(--mint); color:var(--mint); background:rgba(21,255,200,.08)}
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
@media (max-width:520px){ .rs-pile .sticker{font-size:.72rem} .rs-who button{min-height:44px} }

/* ---------- support band ---------- */
.rs-help{background:var(--coral); color:var(--slate)}
.rs-help__in{display:grid; grid-template-columns:auto minmax(0,1fr) auto; gap:14px 28px; align-items:center; padding-block:20px}
.rs-help__t b{display:block; font-family:var(--display); font-stretch:112%; font-weight:900; font-size:clamp(1.25rem,1.8vw,1.5rem); line-height:.98; text-transform:uppercase; max-width:13ch}
.rs-help__t span{display:block; font-weight:600; font-size:.9rem; margin-top:6px}
.rs-help__nums{list-style:none; margin:0; padding:0; display:flex; flex-wrap:wrap; gap:12px 0; justify-content:space-evenly}
.rs-help__nums li{margin:0; padding:2px 16px; border-left:2px solid rgba(29,65,78,.28); min-width:0}
.rs-help__nums small{display:block; font-family:var(--mono); font-size:.7rem; letter-spacing:.06em; text-transform:uppercase; font-weight:600; margin-bottom:2px}
.rs-help__nums b, .rs-help__nums a{display:block; font-family:var(--display); font-stretch:106%; font-weight:900; font-size:clamp(1.02rem,1.3vw,1.2rem); line-height:1.1; color:var(--slate); text-decoration:none; white-space:nowrap}
.rs-help__nums a:hover{text-decoration:underline; text-decoration-thickness:2px}
.rs-help__act{display:flex; flex-direction:column; gap:8px; align-items:flex-start}
.rs-help__act a{font-weight:700; font-size:.92rem; color:var(--slate)}
@media (max-width:1180px){ .rs-help__in{grid-template-columns:minmax(0,1fr) auto} .rs-help__nums{grid-column:1/-1; grid-row:2; justify-content:flex-start} .rs-help__nums li:first-child{border-left:0; padding-left:0} }
@media (max-width:640px){ .rs-help__in{grid-template-columns:1fr} .rs-help__t b{max-width:none} .rs-help__nums{flex-direction:column; gap:10px; grid-row:auto} .rs-help__nums li{border-left:0; padding:0} .rs-help__act{flex-direction:row; align-items:center; gap:16px} .rs-help__act .btn{min-height:44px} }

/* ---------- search state ---------- */
.rs-searching .rs-hide-on-search{display:none}
#index,#browse,#featured{scroll-margin-top:70px}

/* ---------- start here: one bento on the three-column grid ----------
   Two surfaces only: white cards, and teal for Vibe Check. Leads read text first, media at the floor;
   the five smaller cards share one anatomy (media, label, title, text, links on the floor). */
.rs-jump{display:inline-flex; align-items:center; gap:.5em; font-family:var(--display); font-weight:800; font-stretch:106%; color:var(--logo-teal); text-decoration:none; padding:.5em 0; border-bottom:3px solid var(--mint)}
.rs-jump span{transition:transform .2s var(--ease)}
.rs-jump:hover span{transform:translateY(3px)}
.rs-bento{display:grid; grid-template-columns:repeat(3,minmax(0,1fr)); gap:var(--gap)}
.rs-f{position:relative; display:flex; flex-direction:column; min-width:0; border-radius:var(--r-xl); overflow:hidden; background:#fff; color:var(--slate); border:1px solid var(--line); transition:transform .25s var(--ease), box-shadow .25s var(--ease)}
.rs-f--sm:hover{transform:translateY(-4px); box-shadow:var(--shadow-soft)}
.rs-f h3{margin:0 0 .4em; font-size:1.42rem; line-height:1.1}
.rs-f h3 a{color:inherit; text-decoration:none}
.rs-f--sm h3 a::after{content:""; position:absolute; inset:0; z-index:1}
.rs-f--sm h3 a:focus-visible{outline:0}
.rs-f--sm:has(h3 a:focus-visible){outline:3px solid var(--teal); outline-offset:3px}
.rs-f p{margin:0}
.rs-kick{display:block; font-family:var(--mono); font-size:.72rem; letter-spacing:.12em; text-transform:uppercase; font-weight:600; margin-bottom:10px; color:var(--logo-teal)}
.rs-kick i{font-style:normal; background:var(--mint); color:var(--slate); padding:2px 7px; border-radius:4px; margin-right:.6em}
/* lead: Certified Peer Educator Training */
.rs-f--cpet{grid-column:1 / span 2}
.rs-cpet__txt{padding:var(--pad-card) var(--pad-card) 24px}
.rs-f--cpet h3{font-size:clamp(1.6rem,2.4vw,2.1rem); line-height:1.02}
.rs-f--cpet p{font-size:1.06rem; line-height:1.5; font-weight:500}
.rs-cpet__top{display:flex; flex-wrap:wrap; align-items:center; justify-content:space-between; gap:8px 20px; margin-bottom:12px}
.rs-cpet__top .rs-kick{margin:0}
.rs-f--cpet .btns{margin-top:20px}
/* the slide area keeps the slides' own 16:9, so no bars beside them; the control bar sits under it */
.rs-f--cpet .player{margin-top:auto; align-self:stretch; aspect-ratio:auto; height:0; padding-bottom:calc(56.25% + 56px); border-radius:0; box-shadow:none; border-top:1px solid var(--line)}
/* lead: Vibe Check, the teal tower */
.rs-f--vibe{grid-column:3; grid-row:1 / span 2; container-type:inline-size; background:var(--teal); color:#fff; border-color:transparent}
.rs-vibe__txt{padding:var(--pad-card) var(--pad-card) 0}
.rs-f--vibe .rs-kick{color:#fff}
.rs-vmark{display:flex; align-items:center; gap:10px; font-family:var(--display); font-weight:900; font-stretch:115%; font-size:1.1rem; color:#fff; margin-bottom:14px}
.rs-vmark .daisy{width:32px; height:32px; color:var(--mint)}
.rs-qs{position:relative; --q:clamp(1.9rem,11.4cqi,2.7rem); height:calc(var(--q) * 2.06); overflow:hidden; margin:0 0 .6em}
.rs-qs span{position:absolute; inset:0; display:flex; align-items:flex-end; font-family:var(--display); font-weight:900; font-stretch:115%; font-size:var(--q); line-height:1; letter-spacing:-.015em; color:#fff; transform:translateY(110%); opacity:0; transition:transform .7s cubic-bezier(.2,.8,.2,1), opacity .7s}
.rs-qs span.on{transform:none; opacity:1}
.rs-qs span.out{transform:translateY(-110%); opacity:0}
.rs-f--vibe p{color:#fff; font-weight:500; font-size:1.02rem; line-height:1.5}
.rs-vibe__btns{display:grid; gap:10px; padding:0 var(--pad-card) var(--pad-card)}
.rs-vibe__btns .btn{width:100%}
/* the phone takes whatever height the two rows leave, up to the width of the tower, and stays whole */
.rs-vphone{flex:1; position:relative; min-height:420px; margin:26px 0}
.rs-vphone__in{position:absolute; left:50%; top:50%; height:min(100%, 178cqi); aspect-ratio:390/800; transform:translate(-50%,-50%) rotate(-3deg)}
.rs-vphone .ph{position:absolute; inset:0; border-radius:12% / 5.85%; border:10px solid #0b1f25; background:#0b1f25; overflow:hidden; box-shadow:0 30px 60px -20px rgba(0,0,0,.55)}
.rs-vphone .ph img{width:100%; height:100%; object-fit:cover; object-position:top}
.rs-vphone .sticker{position:absolute; z-index:2}
.rs-vphone .s-a{left:-5%; top:11%} .rs-vphone .s-b{right:-3%; top:37%}
/* the five smaller cards */
.rs-f__media{aspect-ratio:16/9; overflow:hidden; background:var(--slate); position:relative; flex:none}
.rs-f__media img{width:100%; height:100%; object-fit:cover; transition:transform .5s var(--ease)}
.rs-f--sm:hover .rs-f__media > img{transform:scale(1.04)}
.rs-f__media--top img{object-position:top}
.rs-f__body{padding:20px var(--pad-card) 22px; display:flex; flex-direction:column; flex:1}
.rs-f__body p{color:var(--ink-soft); font-size:.97rem; line-height:1.5}
.rs-f__links{position:relative; z-index:2; margin-top:auto; padding-top:18px; display:grid}
.rs-f__links a{display:flex; align-items:center; justify-content:space-between; gap:12px; min-height:44px; border-top:1px solid var(--line); font-weight:800; font-family:var(--display); font-stretch:104%; font-size:1rem; color:var(--logo-teal); text-decoration:none}
.rs-f__links a > span:last-child{color:var(--teal); transition:transform .2s var(--ease)}
.rs-f__links a:hover > span:first-child{text-decoration:underline; text-decoration-color:var(--mint); text-decoration-thickness:3px; text-underline-offset:4px}
.rs-f__links a:hover > span:last-child{transform:translateX(4px)}
.rs-f__body{padding-bottom:12px}
.rs-f__media--ai{background:var(--teal)}
.rs-f__media--hz{background:var(--slate); background-image:var(--grain); display:grid; grid-template-columns:minmax(0,1.08fr) minmax(0,.92fr); align-items:center; gap:20px; padding:0 22px 0 26px}
.rs-f__media--hz .hz{transition:transform .4s var(--ease)}
.rs-f--sm:hover .rs-f__media--hz .hz{transform:rotate(0)}
.rs-f__media--hz q{quotes:none; font-family:var(--display); font-weight:800; font-stretch:108%; font-size:1.08rem; line-height:1.18; color:#fff}
.rs-mosaic{display:grid; grid-template-columns:repeat(3,1fr); grid-template-rows:1fr 1fr; gap:3px; height:100%}
.rs-mosaic img{width:100%; height:100%; object-fit:cover; min-height:0}
.rs-mosaic .gc{grid-column:3; grid-row:1/3; background:var(--aqua); display:grid; place-items:center; padding:10px; min-height:0}
.rs-mosaic .gc img{width:auto; height:92%; object-fit:contain; box-shadow:0 10px 24px -10px rgba(0,0,0,.5); border-radius:3px; transform:rotate(3deg)}
/* request a program: photo | pitch | what schools can book, on the same three column lines */
.rs-f--req{grid-column:1/-1; display:grid; grid-template-columns:calc((100% - 2 * var(--gap)) / 3 + var(--gap)) minmax(0,1fr) calc((100% - 2 * var(--gap)) / 3)}
.rs-f--req .rs-f__media{aspect-ratio:auto; min-height:300px}
.rs-f--req .rs-f__media img{position:absolute; inset:0; object-position:58% 40%}
.rs-f--req .rs-f__body{padding:var(--pad-card); justify-content:center}
.rs-f--req h3{font-size:clamp(1.6rem,2.4vw,2.1rem)}
.rs-f--req .rs-f__body p{font-size:1rem}
.rs-f--req .rs-f__body p a{color:var(--logo-teal); font-weight:700; text-decoration:underline; text-decoration-color:var(--mint); text-decoration-thickness:3px; text-underline-offset:3px}
.rs-f--req .btns{margin-top:20px}
.rs-book{border-left:1px solid var(--line); padding:var(--pad-card); display:flex; flex-direction:column; justify-content:center; min-width:0}
.rs-book ul{list-style:none; margin:0; padding:0; border-top:1px solid var(--line)}
.rs-book li{margin:0; border-bottom:1px solid var(--line)}
.rs-book a{display:grid; grid-template-columns:minmax(0,1fr) auto; gap:2px 12px; align-items:center; padding:11px 0; text-decoration:none; color:var(--slate)}
.rs-book a b{font-family:var(--display); font-stretch:106%; font-size:1.06rem; line-height:1.2; color:var(--logo-teal)}
.rs-book a small{grid-column:1; font-size:.9rem; line-height:1.35; color:var(--ink-soft)}
.rs-book a i{grid-column:2; grid-row:1 / span 2; font-style:normal; font-weight:800; color:var(--teal); transition:transform .2s var(--ease)}
.rs-book a:hover b{text-decoration:underline; text-decoration-color:var(--mint); text-decoration-thickness:3px; text-underline-offset:3px}
.rs-book a:hover i{transform:translateX(4px)}
@media (max-width:1000px){
  .rs-bento{grid-template-columns:repeat(2,minmax(0,1fr))}
  .rs-f--cpet{grid-column:1/-1}
  .rs-f--vibe{grid-column:1/-1; grid-row:auto; display:grid; grid-template-columns:minmax(0,1.15fr) minmax(0,.85fr); grid-template-rows:1fr auto}
  .rs-vibe__txt{grid-column:1; grid-row:1; align-self:end}
  .rs-vibe__btns{grid-column:1; grid-row:2; grid-template-columns:auto auto; justify-content:start; padding-top:22px; align-self:start}
  .rs-vibe__btns .btn{width:auto}
  .rs-vphone{grid-column:2; grid-row:1 / span 2; min-height:440px; margin:28px 0}
  .rs-vphone__in{height:100%}
  .rs-qs{--q:clamp(2rem,4.6vw,2.7rem)}
  .rs-f--lib{grid-column:1/-1; display:grid; grid-template-columns:minmax(0,1fr) minmax(0,1fr)}
  .rs-f--lib .rs-f__media{aspect-ratio:auto; min-height:260px}
  .rs-f--req{grid-template-columns:minmax(0,1fr) minmax(0,1fr)}
  .rs-f--req .rs-f__media{grid-row:1 / span 2}
  .rs-book{border-left:0; border-top:1px solid var(--line)}
}
@media (max-width:680px){
  .rs-bento{grid-template-columns:minmax(0,1fr)}
  .rs-f--vibe, .rs-f--lib, .rs-f--req{display:flex}
  .rs-qs{--q:clamp(1.9rem,9.4vw,2.6rem)}
  .rs-vibe__btns{grid-template-columns:1fr; padding-top:0} .rs-vibe__btns .btn{width:100%}
  .rs-vphone{min-height:0; height:min(118vw,520px); flex:none}
  .rs-f--lib .rs-f__media{aspect-ratio:16/9; min-height:0}
  .rs-f--req .rs-f__media{min-height:0; aspect-ratio:16/10}
  .rs-f--req .rs-f__media img{position:static}
  .rs-f__media--hz{padding:0 16px 0 20px; gap:14px}
  .rs-book a{min-height:48px}
}

/* ---------- audience tabs: tab row and panel share the three column lines ---------- */
.rs-aud__tabs{display:grid; grid-template-columns:repeat(3,minmax(0,1fr)); gap:var(--gap); margin-bottom:var(--gap)}
.rs-aud__tab{font:inherit; text-align:left; display:flex; align-items:center; gap:14px; padding:12px 18px 12px 12px; border-radius:16px; border:2px solid var(--line-dark); background:rgba(255,255,255,.06); color:#fff; cursor:pointer; transition:border-color .2s, background .2s, transform .2s var(--ease); min-width:0}
.rs-aud__face{width:58px; height:58px; border-radius:12px; overflow:hidden; flex:none; background:var(--mist)}
.rs-aud__face img{width:100%; height:100%; object-fit:cover}
.rs-aud__tab small{display:block; font-family:var(--mono); font-size:.7rem; letter-spacing:.12em; text-transform:uppercase; color:var(--mint)}
.rs-aud__tab b{display:block; font-family:var(--display); font-weight:800; font-stretch:110%; font-size:1.25rem; line-height:1.05}
.rs-aud__tab em{margin-left:auto; font-style:normal; font-family:var(--mono); font-size:.72rem; letter-spacing:.06em; text-transform:uppercase; color:var(--aqua); white-space:nowrap}
.rs-aud__tab:hover{border-color:var(--mint)}
.rs-aud__tab[aria-selected="true"]{background:var(--mint); border-color:var(--mint); color:var(--slate)}
.rs-aud__tab[aria-selected="true"] small, .rs-aud__tab[aria-selected="true"] em{color:var(--slate)}
.rs-aud__panel{display:grid; grid-template-columns:repeat(3,minmax(0,1fr)); gap:var(--gap); align-items:stretch}
.rs-aud__intro{background:#fff; color:var(--slate); border-radius:var(--r-xl); overflow:hidden; display:flex; flex-direction:column; min-width:0}
.rs-aud__img{aspect-ratio:16/10; overflow:hidden; flex:none}
.rs-aud__img img{width:100%; height:100%; object-fit:cover; object-position:50% 30%}
#p-parents .rs-aud__img img{object-position:50% 22%}
#p-educators .rs-aud__img img{object-position:50% 45%}
.rs-aud__txt{padding:22px var(--pad-card) var(--pad-card); display:flex; flex-direction:column; flex:1}
.rs-aud__txt h3{font-size:clamp(1.45rem,2vw,1.75rem); line-height:1.08; margin-bottom:.45em}
.rs-aud__txt h3 .nb{white-space:nowrap}
.rs-aud__txt > p:not(.eyebrow){color:var(--ink-soft); font-size:1rem; line-height:1.5}
.rs-aud__txt .eyebrow{margin-bottom:.6rem; color:var(--logo-teal)}
.rs-also{margin-top:auto; padding-top:16px; border-top:1px solid var(--line)}
.rs-aud__txt > p + .rs-also{margin-top:auto}
.rs-aud__txt > p:not(.eyebrow){margin-bottom:18px}
.rs-also > span{display:block; font-family:var(--mono); font-size:.7rem; letter-spacing:.12em; text-transform:uppercase; color:var(--logo-teal); font-weight:600; margin-bottom:10px}
.rs-also div{display:flex; flex-wrap:wrap; gap:7px}
.rs-also a{font-weight:700; font-size:.9rem; text-decoration:none; color:var(--slate); background:var(--aqua); border-radius:999px; padding:7px 13px; transition:background .2s}
.rs-also a:hover{background:var(--mint)}
.rs-browse .rs-also a, .rs-browse a.rs-acard{color:var(--slate)}
.rs-aud__cards{grid-column:2 / span 2; display:grid; grid-template-columns:repeat(2,minmax(0,1fr)); grid-auto-rows:1fr; gap:var(--gap); min-width:0}
.rs-acard{position:relative; display:flex; flex-direction:column; background:#fff; border-radius:var(--r-xl); overflow:hidden; text-decoration:none; color:var(--slate); transition:transform .25s var(--ease), box-shadow .25s var(--ease); min-width:0}
.rs-acard:hover{transform:translateY(-4px); box-shadow:0 24px 40px -24px rgba(0,0,0,.6)}
.rs-acard__img{aspect-ratio:2/1; overflow:hidden; background:var(--slate-deep); flex:none}
.rs-acard__img img{width:100%; height:100%; object-fit:cover; transition:transform .5s var(--ease)}
.rs-acard__img--top img{object-position:top}
.rs-acard__img--cover{background:var(--aqua); display:flex; justify-content:center; align-items:flex-end; padding-top:16px}
.rs-acard__img--cover img{width:auto; height:100%; max-width:60%; object-fit:cover; object-position:top; border-radius:4px 4px 0 0; box-shadow:0 -6px 18px -8px rgba(0,0,0,.4)}
.rs-acard__img--phone{background:var(--teal); display:flex; justify-content:center; align-items:flex-start; padding-top:18px}
.rs-acard__img--phone img{width:42%; height:auto; object-fit:initial; border-radius:18px 18px 0 0; border:6px solid #0b1f25; border-bottom:0; box-shadow:0 10px 30px -10px rgba(0,0,0,.5)}
.rs-acard:hover .rs-acard__img img{transform:scale(1.04)}
.rs-acard:hover .rs-acard__img--cover img, .rs-acard:hover .rs-acard__img--phone img{transform:translateY(-4px)}
.rs-acard__body{padding:16px 22px 20px; display:flex; flex-direction:column; gap:5px; flex:1}
.rs-acard__body small{font-family:var(--mono); font-size:.7rem; letter-spacing:.1em; text-transform:uppercase; color:var(--logo-teal); font-weight:600}
.rs-acard__body b{font-family:var(--display); font-stretch:106%; font-size:1.22rem; line-height:1.15; color:var(--logo-teal)}
.rs-acard__body span{font-size:.95rem; color:var(--ink-soft); line-height:1.45}
.rs-acard__go{position:absolute; right:14px; top:14px; width:36px; height:36px; border-radius:50%; display:grid; place-items:center; background:var(--mint); color:var(--slate); font-weight:800; box-shadow:0 4px 10px rgba(0,0,0,.2); transition:transform .25s var(--ease)}
.rs-acard:hover .rs-acard__go{transform:translate(2px,-2px)}
@media (max-width:1000px){ .rs-aud__tab em{display:none} .rs-aud__panel{grid-template-columns:minmax(0,1fr)} .rs-aud__cards{grid-column:auto} .rs-aud__intro{display:grid; grid-template-columns:minmax(0,.8fr) minmax(0,1.2fr)} .rs-aud__img{aspect-ratio:auto; min-height:100%} }
@media (max-width:760px){ .rs-aud__tab em{display:inline} .rs-aud__tabs{grid-template-columns:1fr; gap:8px} .rs-aud__tab{padding:8px 14px 8px 8px} .rs-aud__face{width:44px; height:44px} .rs-aud__intro{display:flex} .rs-aud__img{aspect-ratio:16/9; min-height:0} .rs-also a{padding:10px 14px} }
@media (max-width:560px){ .rs-aud__cards{grid-template-columns:1fr; grid-auto-rows:auto} }

/* ---------- index bar ---------- */
.rs-ibar{position:sticky; top:calc(76px + env(safe-area-inset-top,0px)); z-index:20; background:rgba(255,255,255,.96); backdrop-filter:blur(8px); border-bottom:1px solid var(--line); border-top:1px solid var(--line)}
.rs-ibar .wrap{display:flex; flex-wrap:wrap; gap:10px 16px; align-items:center; padding-block:12px}
.rs-ibar__q{display:flex; align-items:center; gap:8px; flex:1 1 260px; min-width:0; border:2px solid var(--line); border-radius:10px; padding:0 12px; background:#fff}
.rs-ibar__q:focus-within{border-color:var(--teal)}
.rs-ibar__q svg{width:18px; height:18px; color:var(--teal); flex:none}
.rs-ibar__q input{flex:1; min-width:0; border:0; outline:0; font:inherit; font-size:.98rem; padding:10px 0; background:transparent; color:var(--slate)}
.rs-seg{display:flex; gap:4px; background:var(--mist); border-radius:10px; padding:4px; overflow-x:auto; max-width:100%; scrollbar-width:none}
.rs-seg::-webkit-scrollbar{display:none}
.rs-seg button{font:inherit; font-family:var(--display); font-weight:800; font-stretch:106%; font-size:.92rem; border:0; background:transparent; padding:8px 13px; border-radius:7px; cursor:pointer; color:var(--slate); white-space:nowrap; transition:background .15s}
.rs-seg button:hover:not([aria-pressed="true"]){background:var(--aqua)}
.rs-seg button[aria-pressed="true"]{background:var(--slate); color:#fff}
.rs-count{font-weight:700; font-size:.9rem; color:var(--ink-soft); margin:0; white-space:nowrap}
.rs-count button{font:inherit; font-weight:700; color:var(--logo-teal); background:none; border:0; cursor:pointer; text-decoration:underline; text-decoration-color:var(--mint); text-decoration-thickness:2px; text-underline-offset:3px; padding:0; margin-left:8px}

/* ---------- shelves: three tiles to a view, on the page's column lines ---------- */
.rs-index{padding-top:0; padding-bottom:clamp(40px,5vw,68px)}
.rs-index .rs-shelf:last-of-type{margin-bottom:0}
.rs-index__in{padding-top:clamp(34px,4vw,56px)}
.rs-shelf{margin-bottom:clamp(34px,4vw,52px)}
.rs-shelf__head{display:grid; grid-template-columns:minmax(0,1fr) auto; align-items:center; gap:4px 24px; margin-bottom:14px}
.rs-shelf__head h3{font-size:clamp(1.45rem,2.4vw,2.05rem); margin:0; display:flex; align-items:center; gap:12px; flex-wrap:wrap}
.rs-shelf__head p{grid-column:1/-1; margin:0; color:var(--ink-soft); font-size:1rem}
.rs-shelf__n{font-family:var(--mono); font-size:.8rem; font-weight:600; font-stretch:100%; background:var(--mint); color:var(--slate); border-radius:999px; padding:4px 10px; letter-spacing:.04em; line-height:1.2}
.rs-shelf__nav{display:flex; gap:8px; flex:none}
.rs-shelf__nav button{width:44px; height:44px; border-radius:50%; border:2px solid var(--line); background:#fff; color:var(--slate); font-size:1.4rem; line-height:1; cursor:pointer; display:grid; place-items:center; padding:0 0 3px; transition:background .15s, color .15s, border-color .15s, opacity .15s}
.rs-shelf__nav button:hover:not(:disabled){border-color:var(--slate); background:var(--slate); color:#fff}
.rs-shelf__nav button:disabled{opacity:.3; cursor:default}
.rs-shelf.is-all .rs-shelf__nav{visibility:hidden}
.rs-shelf__row{--n:3; display:grid; grid-auto-flow:column; grid-template-rows:auto auto 1fr auto; grid-auto-columns:calc((100% - (var(--n) - 1) * var(--gap)) / var(--n)); gap:0 var(--gap); overflow-x:auto; overscroll-behavior-x:contain; scroll-snap-type:x mandatory; padding:8px 0 14px; margin-top:-8px; scrollbar-width:none}
.rs-shelf__row::-webkit-scrollbar{display:none}
/* the ledge is the shelf board and the scroll position: the mint strip is the part of the shelf in view */
.rs-shelf__ledge{position:relative; height:14px; border-radius:4px; background:var(--slate); box-shadow:0 14px 20px -12px rgba(22,53,64,.55); overflow:hidden}
.rs-shelf__ledge i{position:absolute; left:0; top:0; height:4px; width:100%; background:var(--mint); border-radius:0 0 4px 4px; transition:transform .25s var(--ease), width .25s var(--ease)}
/* every tile on a shelf shares the same four rows (media, title, text, foot), so titles, text and feet line up across the shelf */
.rs-tile{position:relative; grid-row:1 / span 4; display:grid; grid-template-rows:subgrid; scroll-snap-align:start; background:#fff; color:var(--slate); border:1px solid var(--line); border-radius:14px; overflow:hidden; text-decoration:none; transition:transform .25s cubic-bezier(.2,.8,.2,1), box-shadow .25s; min-width:0}
.rs-tile:hover{transform:translateY(-6px); box-shadow:0 22px 34px -22px rgba(22,53,64,.6)}
.rs-tile__media{display:block; aspect-ratio:16/9; overflow:hidden; background:var(--slate); position:relative}
.rs-tile__media img{width:100%; height:100%; object-fit:cover; transition:transform .5s}
.rs-tile:hover .rs-tile__media img{transform:scale(1.05)}
.rs-tile__media--cover{background:var(--aqua); display:flex; justify-content:center; align-items:flex-end; padding-top:18px}
.rs-tile__media--cover img{width:auto; height:100%; max-width:62%; object-fit:cover; object-position:top; border-radius:4px 4px 0 0; box-shadow:0 -8px 22px -10px rgba(0,0,0,.45)}
.rs-tile:hover .rs-tile__media--cover img{transform:translateY(-4px)}
.rs-tile__media--logo{background:var(--aqua); display:grid; place-items:center; padding:24px 40px; border-bottom:1px solid var(--line)}
.rs-tile__media--logo img{object-fit:contain; height:auto; max-height:80%}
.rs-tile__media--phone{background:var(--teal)}
.rs-tile__media--phone img{width:40%; height:auto; margin:18px auto 0; border-radius:18px 18px 0 0; border:6px solid #0b1f25; border-bottom:0}
.rs-tile:hover .rs-tile__media--phone img{transform:translateY(-4px)}
.rs-tile__media--mosaic{display:grid; grid-template-columns:1fr 1fr; grid-template-rows:1fr 1fr; gap:3px}
.rs-tile__media--mosaic img{min-height:0}
.rs-tile__media--covers{background:var(--slate); background-image:var(--grain); display:flex; align-items:center; justify-content:center; gap:5%}
.rs-tile__media--covers img{width:25%; height:auto; aspect-ratio:1; border-radius:10px; box-shadow:0 16px 26px -12px rgba(0,0,0,.7)}
.rs-tile__media--covers img:nth-child(2){width:31%}
.rs-tile:hover .rs-tile__media--covers img{transform:translateY(-4px)}
.rs-g{display:flex; flex-direction:column; justify-content:center; align-items:flex-start; padding:16px 26px}
.rs-g > b{font-family:var(--display); font-weight:900; font-stretch:125%; line-height:.9; font-size:5rem; letter-spacing:-.02em}
.rs-g > i{font-style:normal; font-family:var(--mono); font-size:.76rem; letter-spacing:.1em; text-transform:uppercase; margin-top:10px; font-weight:600}
.rs-g--faq{background:var(--logo-teal); color:var(--mint)} .rs-g--faq > b{font-size:6.4rem} .rs-g--faq > i{color:var(--aqua)}
.rs-g--help{background:var(--coral); color:var(--slate)}
.rs-tile__media.rs-g--hz{background:var(--slate); background-image:var(--grain); align-items:center; justify-content:center; padding:0 16%}
.rs-tile__media.rs-g--hz .hz{width:100%}
.rs-tile > b{padding:18px 20px 0; font-family:var(--display); font-stretch:106%; font-size:1.2rem; line-height:1.2; color:var(--logo-teal)}
.rs-tile > small{padding:7px 20px 16px; font-size:.95rem; color:var(--ink-soft); line-height:1.5}
.rs-tile__foot{display:flex; align-items:center; justify-content:space-between; gap:12px; margin:0 20px; padding:12px 0 14px; border-top:1px solid var(--line)}
.rs-tile__chips{display:flex; flex-wrap:wrap; gap:5px; min-width:0}
.rs-tile__chips span{font-family:var(--mono); font-size:.7rem; letter-spacing:.05em; text-transform:uppercase; font-weight:600; padding:3px 8px; border-radius:4px; background:var(--aqua); color:var(--slate); white-space:nowrap}
.rs-tile__chips span:first-child{background:var(--slate); color:#fff}
.rs-tile__go{flex:none; width:30px; height:30px; border-radius:50%; display:grid; place-items:center; background:var(--mist); font-weight:800; color:var(--logo-teal); transition:background .2s, transform .2s var(--ease)}
.rs-tile:hover .rs-tile__go{background:var(--mint); color:var(--slate); transform:translateX(3px)}
.rs-tile--vibe{border-color:var(--teal); box-shadow:inset 0 0 0 1px var(--teal)}
.rs-tile--vibe .rs-tile__chips span:first-child{background:var(--teal)}
.rs-tile--help .rs-tile__chips span:first-child{background:var(--coral); color:var(--slate)}
.rs-tile--new .rs-tile__chips span:first-child{background:var(--mint); color:var(--slate)}
.rs-filtered .rs-shelf__row{grid-auto-flow:row; grid-template-rows:none; grid-template-columns:repeat(3,minmax(0,1fr)); grid-auto-columns:auto; overflow:visible; scroll-snap-type:none; padding-bottom:0}
.rs-filtered .rs-tile{grid-row:span 4; margin-bottom:var(--gap)}
.rs-filtered .rs-shelf__nav{display:none}
.rs-empty{padding:48px 20px; text-align:center; border:2px dashed var(--line); border-radius:16px}
.rs-empty h3{margin-bottom:.3em}
@media (max-width:1180px) and (min-width:1001px){ .rs-f--req .btn{font-size:.95rem; padding-inline:1em; white-space:nowrap} }
@media (max-width:1100px){ .rs-shelf__row{--n:2} .rs-filtered .rs-shelf__row{grid-template-columns:repeat(2,minmax(0,1fr))} }
@media (max-width:640px){ .rs-ibar{position:static} .rs-ibar .wrap{gap:10px} .rs-seg button{min-height:44px} .rs-ibar__q input{padding:12px 0}
  .rs-shelf__nav{display:none} .rs-shelf__row{--n:1.16} .rs-tile{display:flex; flex-direction:column} .rs-tile > small{flex:1} .rs-filtered .rs-shelf__row{grid-template-columns:minmax(0,1fr)} .rs-g > b{font-size:4.2rem} .rs-g--faq > b{font-size:5.4rem} }
'''

RS_JS = r'''
(function(){
  var d = document, main = d.getElementById('main');
  /* rotating questions in the Vibe Check card */
  var qs = d.querySelectorAll('.rs-qs span'), qi = 0, reduce = matchMedia('(prefers-reduced-motion: reduce)').matches;
  if(qs.length && !reduce){ setInterval(function(){ var cur = qs[qi]; cur.classList.remove('on'); cur.classList.add('out'); qi = (qi+1) % qs.length; var nx = qs[qi]; nx.classList.remove('out'); void nx.offsetWidth; nx.classList.add('on'); setTimeout(function(){ cur.classList.remove('out'); }, 800); }, 2600); }

  /* shelf arrows + the ledge strip that shows which part of the shelf is in view */
  d.querySelectorAll('[data-shelf]').forEach(function(sh){
    var row = sh.querySelector('.rs-shelf__row'), btns = sh.querySelectorAll('[data-dir]'), strip = sh.querySelector('.rs-shelf__ledge i');
    function upd(){
      var max = row.scrollWidth - row.clientWidth - 2, all = max <= 2;
      btns[0].disabled = row.scrollLeft <= 2; btns[1].disabled = row.scrollLeft >= max;
      sh.classList.toggle('is-all', all);
      if(strip){ var f = all ? 1 : row.clientWidth / row.scrollWidth; strip.style.width = (f * 100) + '%'; strip.style.transform = 'translateX(' + (all ? 0 : row.scrollLeft / row.scrollWidth * row.clientWidth) + 'px)'; }
    }
    btns.forEach(function(b){ b.addEventListener('click', function(){ var gap = parseFloat(getComputedStyle(row).columnGap) || 0; row.scrollBy({left: (+b.dataset.dir) * (row.clientWidth + gap), behavior: reduce ? 'auto' : 'smooth'}); }); });
    row.addEventListener('scroll', function(){ window.requestAnimationFrame(upd); }, {passive:true});
    window.addEventListener('resize', upd); window.addEventListener('load', upd); upd();
  });

  /* search + audience filter */
  var tiles = Array.prototype.slice.call(d.querySelectorAll('.rs-tile')), shelves = d.querySelectorAll('[data-shelf]');
  var inputs = d.querySelectorAll('[data-rsq]'), count = d.getElementById('rs-count'), empty = d.getElementById('rs-empty'), idx = d.getElementById('index');
  var st = { q:'', aud:'' }, total = tiles.length;
  function norm(s){ return (s||'').toLowerCase().normalize('NFD').replace(/[\u0300-\u036f]/g,'').replace(/[’']/g,'').replace(/[^a-z0-9#+ ]/g,' '); }
  tiles.forEach(function(t){ t._q = norm(t.getAttribute('data-q')); t._a = t.getAttribute('data-aud'); });
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
    var hint = d.getElementById('rs-hint'); if(hint){ hint.hidden = !terms.length; hint.textContent = shown ? (shown + (shown === 1 ? ' resource matches' : ' resources match') + '. Show results ↓') : 'No matches yet. Try another word.'; }
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


# what a school can book, for the Request a Program panel (wording from the site navigation)
BOOK = [
  ('Assemblies', 'One-time events, co-presented with youth leaders', 'assemblies.html'),
  ('Consent Curriculum', '15 lessons aligned to NHES', 'consent-curriculum.html'),
  ('Faculty & Staff Training', 'Trauma-informed professional development', 'professional-development.html'),
  ('Accountability Training', 'For students who have caused harm', 'accountability-training.html'),
]


def card(key, media, kick, title, href, text, links, media_cls=''):
    """One of the five smaller cards in the bento: media, label, title, text, two links on the floor."""
    rows = ''.join(f'<a href="{esc(h)}"{ext_attrs(h)}><span>{esc(t)}</span>{go(h)}</a>' for t, h in links)
    return (f'<div class="rs-f rs-f--sm rs-f--{key}"><div class="rs-f__media {media_cls}">{media}</div>'
            f'<div class="rs-f__body"><span class="rs-kick">{kick}</span><h3><a href="{esc(href)}">{title}</a></h3><p>{esc(text)}</p>'
            f'<div class="rs-f__links">{rows}</div></div></div>')


def resources():
    n_vid, n_pod, n_gui, n_faq = lib_counts()
    n_all = sum(len(x[3]) for x in shelf_items())
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
    book = ''.join(f'<li><a href="{h}"><b>{esc(t)}</b><small>{esc(dsc)}</small><i aria-hidden="true">&rarr;</i></a></li>' for t, dsc, h in BOOK)

    body = f'''
<section class="rs-hero">
  <span class="wm-daisy" aria-hidden="true"></span>
  <div class="wrap">
    <div class="rise">
      <nav class="crumbs" aria-label="Breadcrumb"><a href="index.html">Home</a><span>/</span><span>Resources</span></nav>
      <p class="eyebrow">Free &middot; Created by youth &amp; survivors</p>
      <h1>SafeBAE <span class="mk">Resources</span></h1>
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

<section class="band band--mist rs-hide-on-search" id="featured">
  <div class="wrap">
    <div class="section-head"><div><h2>Start with one of these</h2></div><a class="rs-jump" href="#index">All {n_all} resources <span aria-hidden="true">&darr;</span></a></div>
    <div class="rs-bento">
      <div class="rs-f rs-f--cpet">
        <div class="rs-cpet__txt">
          <div class="rs-cpet__top"><span class="rs-kick">For student leaders</span>{chips(['16 modules', 'Self-paced', 'Free certificate'], 'mint')}</div>
          <h3>Certified Peer Educator Training</h3>
          <p>A free, self-paced 16-module training that prepares students to lead sexual violence prevention in their schools and communities.</p>
          <div class="btns">{btn('Explore the training', 'peer-educator.html', 'slate', arrow=True)}{btn('Register', 'peer-educator.html#register', 'ghost')}</div>
        </div>
        {cpet_player()}
      </div>
      <div class="rs-f rs-f--vibe">
        <div class="rs-vibe__txt">
          <span class="rs-kick">Reflection &amp; accountability</span>
          <div class="rs-vmark"><span class="daisy"></span>Vibe Check by SafeBAE</div>
          <div class="rs-qs" aria-hidden="true"><span class="on">Did I harm someone?</span><span>Was that consent?</span><span>Did I cross a boundary?</span><span>Am I a bad person?</span></div>
          <h3 class="sr-only">Vibe Check</h3>
          <p>A free and anonymous tool for young people who are worried they may have crossed a boundary or caused harm.</p>
        </div>
        <div class="rs-vphone"><div class="rs-vphone__in"><div class="ph">{img('vc-screen', 'The Vibe Check start screen on a phone')}</div><span class="sticker s-a">Anonymous</span><span class="sticker sticker--white sticker--r s-b">Nothing is stored</span></div></div>
        <div class="rs-vibe__btns">{btn('Visit CheckYourVibe.org', CYV, 'mint')}{btn('How it works', 'vibe-check.html', 'ghost', arrow=True)}</div>
      </div>
      {card('clubs', img('clubhero', 'SafeBAE club members at a summer event', style='object-position:50% 38%'), 'Student-led action', 'SafeBAE Clubs', 'clubs.html',
            'Start or lead a student chapter and get access to materials, training, event ideas, direct support, and a national network of student leaders.',
            [('Explore SafeBAE Clubs', 'clubs.html'), ('Club Hub', 'https://clubs.safebae.org')])}
      {card('skills', img('sl-home', 'The BAE Skills Lab home page'), 'Games + practice', 'BAE Skills Lab', SKILLS_PAGE,
            'Interactive activities about consent, boundaries, and what a healthy relationship actually looks like.',
            [('Explore the Skills Lab', SKILLS_PAGE), ('Open the Skills Lab', SKILLS)], media_cls='rs-f__media--top')}
      {card('ai', img('ai-illo-hello', 'A drawing from the training: a billboard with a smiling face in binary code and a name tag that reads “Hello, my name is AI”'), '<i>New</i>Launches Oct 26–30, 2026', 'SafeBAE AI Literacy Training', 'ai-literacy.html',
            'Six self-paced modules on AI for high school and college students, from how AI works to fake images and sextortion.',
            [('About the training', 'ai-literacy.html'), ('Start the training', 'https://ai-literacy.safebae.org/')], media_cls='rs-f__media--ai')}
      {card('ch', hz_label('hz--tilt') + '<q>There’s no safe way to choke someone.</q>', '<i>New</i>Campaign', 'Choking Hazard', 'choking-hazard.html',
            'SafeBAE’s campaign on sexual strangulation, which young people call “choking”: the evidence, myth vs fact, signs that need medical care, and free warning posters.',
            [('About the campaign', 'choking-hazard.html'), ('chokinghazard.org', 'https://chokinghazard.org')], media_cls='rs-f__media--hz')}
      {card('lib', f'<div class="rs-mosaic">{films4}<span class="gc">{img("guide-red-flags", "")}</span></div>', 'Films + ready-to-use lessons', 'Video Library &amp; Teaching Guides', 'library.html',
            'Pair youth-created films with activities, discussion prompts, and facilitation guidance for classrooms, clubs, and community programs.',
            [('Watch films', 'library.html#films'), ('Use teaching guides', 'library.html#guides')])}
      <div class="rs-f rs-f--req">
        <div class="rs-f__media">{img('066', 'SafeBAE presenters with students at a school assembly')}</div>
        <div class="rs-f__body"><span class="rs-kick">Work with SafeBAE</span><h3>Request a Program</h3><p>Bring SafeBAE to your school or community for workshops, <a href="assemblies.html">assemblies</a>, and comprehensive school programming. Each program is built on SafeBAE 360° Schools, our whole-school approach.</p><div class="btns">{btn('Request a program', 'request-a-program.html', 'mint', arrow=True)}{btn('How 360° Schools works', '360-schools.html', 'ghost', arrow=True)}</div></div>
        <div class="rs-book"><span class="rs-kick">Schools can book</span><ul>{book}</ul></div>
      </div>
    </div>
  </div>
</section>

<section class="band band--slate rs-hide-on-search rs-browse" id="browse">
  <div class="wrap">
    <div class="section-head"><div><h2>Browse by who you are</h2></div></div>
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
    <div class="section-head"><div><p class="eyebrow">Full index &middot; {n_all} resources</p><h2>Every resource, by format</h2></div></div>
    {shelves_html()}
    <div class="rs-empty" id="rs-empty" hidden><h3>Nothing matches <span data-eq></span>.</h3><p class="muted">Try a broader word like <b>consent</b>, search the <a class="link" data-lib href="library.html">Library</a> for films and podcasts, or <a class="link" href="contact.html">tell us what you were looking for</a>.</p></div>
  </div>
</section>
{give_band()}
'''
    page('resources.html', 'Resources · SafeBAE',
         'Free sexual violence prevention resources for students, parents and educators: training, Vibe Check, the Skills Lab, films, teaching guides, Title IX and survivor support.',
         body, active='resources', head_extra='<style>' + RS_CSS + '</style>', scripts=f'<script>{RS_JS}</script>')


def build():
    resources()


if __name__ == '__main__':
    build()
