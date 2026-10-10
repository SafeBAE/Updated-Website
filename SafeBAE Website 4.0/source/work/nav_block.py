# ---------------- navigation ----------------
# v3 information architecture: six tabs. Request a Program replaces 360° Schools as a tab
# (360° is the approach behind the programs, one page under that tab); the Library and the
# trainings sit under Resources; #ForDaisy stays a tab.
CAL_MEET = 'https://calendly.com/shaelnorris/60min'
NAV = [
  dict(label='About', key='about', href='about.html', blurb='Founded by teen survivors in 2015. Led by young people ever since.',
       feature=('safebae-executive-director-shael-norris', 'Our story', 'Survivor-founded and youth-led since 2015', 'about.html'),
       groups=[
         ('The organization', '', [
            ('About SafeBAE', 'about.html', 'Our mission and how we began'),
            ('Our Team', 'team.html', 'Staff, youth media team and board'),
            ('Data & Impact', 'impact.html', 'Published research, surveys and reports'),
         ]),
         ('Connect', '', [
            ('Partners & Press', 'partners-press.html', 'Podcasts, partner films and media'),
            ('Contact', 'contact.html', 'Reach the SafeBAE team'),
            ('Donate', 'donate.html', 'Keep prevention free for students'),
         ]),
       ]),
  dict(label='Students', key='students', href='students.html', blurb='Everything here is free for students, and built by students.',
       feature=('clubhero', 'SafeBAE Clubs', 'Start a SafeBAE club at your school', 'clubs.html'),
       groups=[
         ('Get involved', '', [
            ('For Students', 'students.html', 'Everything for high school students'),
            ('SafeBAE Clubs', 'clubs.html', 'Start, affiliate or restart a chapter'),
            ('Reform Your School’s Policy', 'reform-policy.html', 'A student guide to stronger policies'),
            ('Summer Activist Institute', 'summer-institute.html', 'Meet the fellows'),
         ]),
         ('Free trainings', '', [
            ('Peer Educator Training', 'peer-educator.html', 'Self-paced, 16 modules, certificate'),
            ('AI Literacy Training', 'ai-literacy.html', 'New: six modules on AI and relationships'),
            ('BAE Skills Lab', 'skills-lab.html', 'Short interactive activities'),
            ('En Español', 'espanol.html', 'Entrenamiento en español'),
         ]),
       ]),
  dict(label='Adults', key='adults', href='adults.html', blurb='For the parents, caregivers, educators and mentors in a young person’s life.',
       feature=('us-sometale-parent', 'Parents & caregivers', 'Start the conversation early, and keep talking', 'parents.html'),
       groups=[
         ('By role', '', [
            ('For Adults', 'adults.html', 'Start here if you support young people'),
            ('Parents & Caregivers', 'parents.html', 'Conversations, support and next steps'),
            ('Educators', 'educators.html', 'Classroom tools at every level of use'),
            ('College Students', 'college.html', 'Mentor high schoolers, start a campus club'),
         ]),
         ('What adults ask about', '', [
            ('Choking Hazard', 'choking-hazard.html', 'New: what adults should know about sexual choking'),
            ('Vibe Check for adults', 'vibe-check.html#adults', 'How to share it with a young person'),
            ('If a young person tells you', 'survivor-support.html#when-someone-tells-you', 'What to say, and what to avoid'),
            ('Bring SafeBAE to your school', 'request-a-program.html', 'Assemblies, trainings and pricing'),
         ]),
       ]),
  dict(label='Request a Program', key='programs', href='request-a-program.html', blurb='Assemblies, curriculum, training and policy support, each one built on the SafeBAE 360° approach.',
       feature=('066', 'Assemblies', 'Co-presented with youth leaders at your school', 'assemblies.html'),
       groups=[
         ('Start here', '', [
            ('Request a Program', 'request-a-program.html', 'Every program and the request form'),
            ('SafeBAE 360° Schools', '360-schools.html', 'The whole-school approach behind our programs'),
            ('Pricing', 'request-a-program.html#pricing', 'Flexible, sliding scale'),
         ]),
         ('Programs', '', [
            ('Assemblies', 'assemblies.html', 'One-time events, co-presented with youth leaders'),
            ('Consent Curriculum', 'consent-curriculum.html', '15 lessons aligned to NHES'),
            ('Faculty & Staff Training', 'professional-development.html', 'Trauma-informed professional development'),
         ]),
         ('', '', [
            ('Policy Reform Guide', 'policy-reform-guide.html', 'For administrators and districts'),
            ('Accountability Training', 'accountability-training.html', 'For students who have caused harm'),
            ('Sexual Strangulation Prevention', 'choking-hazard.html#schools', 'New: launches November 2026'),
         ]),
       ]),
  dict(label='Resources', key='resources', href='resources.html', blurb='Every SafeBAE resource is free.', wide=True,
       feature=('yt-ng8s3w1etru', 'Vibe Check', 'No judgment, just answers', 'vibe-check.html'),
       foot=('Resources Hub', 'resources.html', 'Every SafeBAE resource, sorted by who it’s for'),
       groups=[
         ('Trainings & tools', '', [
            ('Peer Educator Training', 'peer-educator.html', 'Free, self-paced, 16 modules'),
            ('AI Literacy Training', 'ai-literacy.html', 'New: free, for ages 13+'),
            ('Vibe Check', 'vibe-check.html', 'Anonymous reflection tool'),
            ('BAE Skills Lab', 'skills-lab.html', 'Interactive consent activities'),
            ('Entrenamiento en español', 'espanol.html', 'Peer Educator Training in Spanish'),
         ]),
         ('The Library', '', [
            ('Search the Library', 'library.html', 'Every film, podcast and guide'),
            ('Films & videos', 'library.html#films', 'Youth-made, with lesson plans'),
            ('Podcasts', 'library.html#podcasts', 'Conversations with SafeBAE leaders'),
            ('Teaching guides', 'library.html#guides', 'Ready-to-teach discussion guides'),
            ('Posters', 'posters.html', 'Free to download and print'),
         ]),
         ('Campaigns & series', '', [
            ('Choking Hazard', 'choking-hazard.html', 'There’s no safe way to choke someone'),
            ('#KnowB4UNude', 'film-knowb4unude.html', 'A PSA on nudes and online pressure'),
            ('It’s Giving Red Flags', 'film-its-giving-red-flags.html', 'A short film about consent'),
            ('BAEcode: Game On!', 'film-baecode-game-on.html', 'Bystander intervention'),
            ('Race, Rape Culture & Resistance', 'film-race-rape-culture-resistance.html', 'A four-lesson series'),
         ]),
         ('Support & answers', '', [
            ('Survivor Support', 'survivor-support.html', 'Hotlines, healing and how to help'),
            ('Title IX', 'title-ix.html', 'Your rights at school'),
            ('Myths & Facts', 'myths-facts.html', 'What the research says'),
            ('FAQ', 'faq.html', 'Straight answers to common questions'),
            ('Blog', 'blog.html', 'Stories, analysis and news'),
         ]),
       ]),
  dict(label='#ForDaisy', key='fordaisy', href='fordaisy.html', blurb='Remembering our co-founder, Daisy Coleman.',
       feature=('daisy-coleman', '#ForDaisy', 'Remembering our co-founder, Daisy Coleman', 'fordaisy.html'),
       groups=[
         ('Remembering Daisy', '', [
            ('Remembering Daisy', 'fordaisy.html', 'Her story, her statement and her legacy'),
            ('Tribute wall', 'fordaisy.html#wall', 'Messages from people Daisy reached'),
            ('Add your message', 'fordaisy.html#add', 'Share what Daisy meant to you'),
         ]),
         ('Her legacy', '', [
            ('Tattoos & Healing', 'fordaisy-tattoos.html', 'Daisy’s art, and a path some survivors take'),
            ('Peer Educator Training', 'peer-educator.html', 'Offered in Daisy’s memory'),
            ('About SafeBAE', 'about.html', 'The organization she co-founded'),
         ]),
       ]),
]
# older page modules pass these keys; they resolve to the v3 tabs
NAV_ALIAS = {'schools': 'programs', 'library': 'resources'}

RIBBON = [
  ('ai-literacy.html', 'New', 'The SafeBAE AI Literacy Training launches during Media Literacy Week, Oct 26–30'),
  ('choking-hazard.html', 'New', 'Choking Hazard: there’s no safe way to choke someone'),
]

def _navlink(t, h, d=''):
    ext = h.startswith('http')
    tgt = ' target="_blank" rel="noopener"' if ext else ''
    return f'<a href="{esc(h)}"{tgt}><span>{esc(t)}{" &#8599;" if ext else ""}</span>' + (f'<small>{esc(d)}</small>' if d else '') + '</a>'

def header(active=''):
    active = NAV_ALIAS.get(active, active)
    items, drawer = [], []
    for n in NAV:
        key = n['key']
        cur = ' aria-current="true"' if key == active else ''
        cols = ''
        for gt, gh, links in n['groups']:
            head = (f'<a class="mega__h" href="{gh}">{esc(gt)}<i aria-hidden="true">&rarr;</i></a>' if gh else f'<p class="mega__h">{esc(gt)}</p>') if gt else '<p class="mega__h mega__h--blank" aria-hidden="true">&nbsp;</p>'
            cols += f'<div class="mega__col">{head}' + ''.join(_navlink(t, h, d) for t, h, d in links) + '</div>'
        fimg, fkick, ftxt, fhref = n['feature']
        intro = '' if n.get('wide') else (f'<div class="mega__intro"><b>{esc(n["label"])}</b><p>{esc(n["blurb"])}</p>'
                                         f'<a class="mega__all" href="{n["href"]}">{"Start here" if key != "fordaisy" else "Remember Daisy"}<i aria-hidden="true">&rarr;</i></a></div>')
        foot = ''
        if n.get('foot'):
            ft, fh, fd = n['foot']
            foot = f'<a class="mega__foot" href="{fh}"><b>{esc(ft)}</b><span>{esc(fd)}</span><i aria-hidden="true">&rarr;</i></a>'
        dz = ' nav__top--daisy' if key == 'fordaisy' else ''
        lead = '<span class="daisy" aria-hidden="true"></span>' if key == 'fordaisy' else ''
        items.append(
            f'<div class="nav__item"><button class="nav__top{dz}" aria-expanded="false"{cur}>{lead}{esc(n["label"])}<span class="caret" aria-hidden="true"></span></button>'
            f'<div class="mega{" mega--wide" if n.get("wide") else ""}" style="--cols:{len(n["groups"])}"><div class="mega__in">{intro}<div class="mega__cols">{cols}</div>'
            f'<a class="mega__feature" href="{fhref}">{img(fimg, "")}<em>{esc(fkick)}</em><b>{esc(ftxt)}</b></a>{foot}</div></div></div>')
        dl = ''
        for gt, gh, links in n['groups']:
            if gt: dl += f'<p class="drawer__g">{esc(gt)}</p>'
            dl += ''.join(f'<a href="{esc(h)}"' + (' target="_blank" rel="noopener"' if h.startswith('http') else '') + f'>{esc(t)}</a>' for t, h, d in links)
        drawer.append(f'<details><summary>{esc(n["label"])}</summary>{dl}</details>')
    return f'''
<a class="skip" href="#main">Skip to content</a>
<div class="utility">
  <div class="wrap">
    <div class="utility__help"><span>Need to talk to someone?</span> <span><strong>Text LOVEIS</strong> to 22522</span> <span class="hide-sm"><strong>Call</strong> 800-656-HOPE (4673)</span> <button class="linkish" data-open-help>All hotlines</button></div>
    <div class="utility__right"><a href="contact.html" class="hide-sm">Contact</a><button class="quick-exit" data-quick-exit title="Leave this site quickly (press Esc twice)">Quick exit <kbd>Esc Esc</kbd></button></div>
  </div>
</div>
<header class="site-header" id="top">
  <div class="wrap">
    <a class="brand" href="index.html" aria-label="SafeBAE home">{LOGO_SVG}</a>
    <nav class="nav" aria-label="Main">{''.join(items)}</nav>
    <div class="header-actions">
      <button class="icon-btn" data-open-search aria-label="Search the site">{ICON_SEARCH}<kbd>&#8984;K</kbd></button>
      <button class="icon-btn help-btn" data-open-help><span class="daisy" aria-hidden="true" style="width:1.1em;height:1.1em"></span><span class="lbl">Get help</span></button>
      {btn('Donate', 'donate.html', 'mint', 'sm')}
      <button class="icon-btn menu-btn" data-open-menu aria-label="Open menu">{ICON_MENU}</button>
    </div>
  </div>
</header>
<div class="ribbon" id="sb-ribbon" role="region" aria-label="What's new at SafeBAE"><div class="wrap"><div class="ribbon__items">{''.join(f'<a href="{h}"><b>{esc(t)}</b><span>{esc(x)}</span><i aria-hidden="true">&rarr;</i></a>' for h, t, x in RIBBON)}</div><button class="ribbon__x" type="button" aria-label="Hide announcements" data-ribbon-x>&times;</button></div></div>
<div class="drawer" id="menu" aria-hidden="true">
  <div class="drawer__scrim" data-close></div>
  <div class="drawer__panel" role="dialog" aria-label="Menu">
    <div class="drawer__head"><span style="width:120px;color:var(--mint);display:block">{LOGO_SVG}</span><button class="close-x" data-close aria-label="Close menu">&times;</button></div>
    <a class="solo" href="index.html">Home</a>
    {''.join(drawer)}
    <a class="solo" href="contact.html">Contact</a>
    <div class="btns">{btn('Donate', 'donate.html', 'mint')}<button class="btn btn--coral" data-open-help>Get help now</button></div>
  </div>
</div>'''

