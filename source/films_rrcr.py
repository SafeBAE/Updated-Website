from films_common import *

BRICK = "url(\"data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='64' height='32'%3E%3Cpath d='M0 .5H64M0 16.5H64M.5 0V16M32.5 16V32' stroke='%23aeeaec' stroke-width='1.2' fill='none'/%3E%3C/svg%3E\")"

CSS = '''
.film--rrcr{--serif:'DM Serif Display',Georgia,serif}
.film--rrcr main{background:#fff; color:var(--slate)}
.film--rrcr h1,.film--rrcr h2,.film--rrcr h3{font-family:var(--serif); font-weight:400; font-stretch:100%; letter-spacing:-.005em}
.brick{background:''' + BRICK + ''' , var(--aqua)}
.rr-hero .wrap{display:grid; grid-template-columns:minmax(0,1.1fr) minmax(0,.9fr); gap:clamp(24px,5vw,64px); align-items:center; padding-block:clamp(48px,7vw,96px)}
.rr-hero .crumbs{color:var(--ink-soft)} .rr-hero .crumbs a{color:var(--logo-teal)}
.rr-title{font-size:clamp(3rem,7vw,6.6rem); line-height:.95; margin:0 0 .3em; color:var(--slate)}
.rr-title span{display:block}
.rr-title span:nth-child(2){color:var(--logo-teal)} .rr-title span:nth-child(3){color:var(--slate); width:fit-content; max-width:100%; background:linear-gradient(transparent 58%, var(--coral) 58% 88%, transparent 88%)}
.rr-photo{position:relative}
.rr-photo img{width:100%; aspect-ratio:4/5; object-fit:cover; border-radius:18px; box-shadow:0 30px 60px -30px rgba(29,65,78,.6)}
.rr-photo .sticker{position:absolute; left:-12px; bottom:28px}
.rr-band{padding-block:var(--band)}
.rr-band--slate{background:var(--slate); color:#fff}
.rr-band h2{font-size:clamp(2.2rem,4.6vw,3.8rem); line-height:1.02}
.rr-band .eyebrow{color:var(--teal)} .rr-band--slate .eyebrow{color:var(--mint)}
.spot{display:grid; grid-template-columns:minmax(0,.85fr) minmax(0,1.15fr); gap:clamp(24px,5vw,64px); align-items:center}
.jq{font-family:var(--serif); font-size:clamp(1.6rem,3.2vw,2.6rem); line-height:1.2; margin:24px 0 0; color:#fff}
.tags{display:flex; flex-wrap:wrap; gap:10px; margin-top:22px}
.tags span{font-family:var(--display); font-weight:900; font-stretch:115%; padding:8px 12px; border-radius:6px; background:var(--mint); color:var(--slate); transform:rotate(-2deg)}
.tags span:nth-child(even){background:var(--coral); transform:rotate(2deg)}
@media (max-width:900px){.rr-hero .wrap,.spot{grid-template-columns:1fr}}
.ltabs{display:grid; grid-template-columns:repeat(4,minmax(0,1fr)); gap:10px; margin:24px 0 20px}
.ltabs button{font:inherit; cursor:pointer; text-align:left; padding:16px; border-radius:14px; border:2px solid var(--line); background:#fff; color:var(--slate)}
.ltabs button small{display:block; font-family:var(--mono); font-size:.68rem; letter-spacing:.1em; text-transform:uppercase; color:var(--teal)}
.ltabs button span{display:block; font-family:var(--serif); font-size:1.2rem; line-height:1.15; margin-top:4px}
.ltabs button[aria-selected="true"]{background:var(--slate); color:#fff; border-color:var(--slate)} .ltabs button[aria-selected="true"] small{color:var(--mint)}
.lpanel{display:grid; grid-template-columns:minmax(0,1.1fr) minmax(0,.9fr); gap:clamp(20px,4vw,48px); align-items:start}
.lpanel h3{font-size:clamp(1.6rem,2.8vw,2.3rem)}
.lpanel ul{padding-left:1.1em}
@media (max-width:900px){.ltabs{grid-template-columns:1fr 1fr} .lpanel{grid-template-columns:1fr}}
.tline{position:relative; display:grid; gap:0; margin-top:28px}
.tline::before{content:""; position:absolute; left:118px; top:8px; bottom:8px; width:3px; background:var(--teal)}
.tl2{display:grid; grid-template-columns:100px 40px minmax(0,1fr); gap:0 0; align-items:start; padding:14px 0}
.tl2 b{font-family:var(--mono); font-size:.74rem; font-weight:600; letter-spacing:.08em; text-transform:uppercase; color:var(--logo-teal); text-align:right; line-height:1.1; padding-top:9px}
.tl2 i{width:18px; height:18px; border-radius:50%; background:var(--coral); border:4px solid #fff; box-shadow:0 0 0 2px var(--teal); margin:6px 0 0 11px; position:relative; z-index:1}
.tl2 h3{font-size:1.4rem; margin:0 0 4px}
.tl2 p{margin:0; color:var(--ink-soft)}
@media (max-width:600px){.tline::before{left:8px} .tl2{grid-template-columns:28px minmax(0,1fr)} .tl2 b{grid-column:2; text-align:left; font-size:1.2rem} .tl2 i{grid-row:1/3; grid-column:1; margin-left:-1px} .tl2 > div{grid-column:2}}
.film--rrcr .gpanel{--g-bg:var(--slate)}
'''

LESSONS = [
 ('Lesson 1', 'The History of Racism & Rape Culture', ['lesson-1-1', 'lesson-1-2', 'lesson-1-3', 'lesson-1-4'],
  ['Sexual violence under U.S. slavery and the denial of consent', 'Post-emancipation racial terror and survivor testimony', 'Racist sexual stereotypes targeting Black women and men', 'Lynching, Jim Crow violence and legal exclusion', 'Resistance from the Civil Rights era through the modern #MeToo movement'],
  'This lesson traces how racism and rape culture developed together in U.S. history. Learners examine cases such as Celia, the 1866 Memphis Riot testimony of Frances Thompson, the exploitation of Sarah Baartman, and Ida B. Wells’ dismantling of the “Black rapist” myth. It also highlights resistance led by Recy Taylor, Betty Jean Owens and Tarana Burke, situating #MeToo within a much longer Black feminist lineage.'),
 ('Lesson 2', 'Sexual Violence in the Black Community Today', ['lesson-2-1', 'lesson-2-2', 'lesson-2-3', 'lesson-2-4'],
  ['Disproportionate rates of sexual violence affecting Black youth', 'Barriers to reporting and mistrust of systems', 'Bias in policing, courts and schools', 'Hypersexualization and adultification of Black girls', 'Media stereotypes and school discipline disparities'],
  'This lesson focuses on how historical racism shows up in Black survivors’ lives today. Using current data and lived examples, learners explore why reporting can feel unsafe or harmful and how stereotypes shape responses to Black pain. It includes a case study of Megan Thee Stallion, alongside discussions of dress codes, adultification bias, and the erasure of Black childhood, especially for Black girls and LGBTQ+ youth.'),
 ('Lesson 3', 'Black Boys & Men: Supporting Male Survivors', ['lesson-3-1', 'lesson-3-2'],
  ['Historical myths portraying Black men as sexual threats', 'Lynching, false accusations and racial terror', 'Consent, boundaries and the silencing of Black boys', 'Toxic masculinity, stigma and mental health impacts', 'Public survivor disclosures and pathways to support'],
  'This lesson centers Black boys and men as survivors, challenging the myth that they are only perpetrators or “always want sex.” Learners examine the deadly consequences of racist stereotypes through the murder of Emmett Till, and explore how stigma keeps many boys from being believed. It highlights survivor voices from Reggie Walker, Terry Crews and Lil Wayne.'),
 ('Lesson 4', 'Relationships & Sexual Violence in Black Media', ['lesson-4-1', 'lesson-4-2', 'conclusion'],
  ['Media representation and its impact on beliefs about relationships', 'Victim-blaming and the “fast” stereotype', 'Abuse portrayed as comedy or normalized behavior', 'Generational trauma and silence', 'Survivor storytelling through music and film'],
  'This lesson analyzes how Black relationships and sexual violence are portrayed in popular media and how those portrayals shape real-world attitudes. Learners engage with examples including Divorce in the Black, Woman Thou Art Loosed and Don’t Be a Menace, and with lyrical storytelling from Kendrick Lamar, Jay-Z and Beyoncé, and Raye.'),
]

TIMELINE = [
 ('Case', 'Celia', 'One of the cases learners examine to see how racism and rape culture developed together in U.S. history.'),
 ('1866', 'Frances Thompson', 'Her testimony about the 1866 Memphis Riot.'),
 ('Case', 'Sarah Baartman', 'The exploitation of Sarah Baartman.'),
 ('Myth', 'Ida B. Wells', 'Dismantled the “Black rapist” myth.'),
 ('Resistance', 'Recy Taylor · Betty Jean Owens · Tarana Burke', 'Resistance that situates #MeToo within a much longer Black feminist lineage.'),
]

def build():
    tabs = ''.join(f'<button role="tab" id="ls-{i}" aria-controls="lp-{i}" aria-selected="{str(i==0).lower()}" tabindex="{0 if i==0 else -1}"><small>{esc(n)}</small><span>{esc(t)}</span></button>' for i, (n, t, *_r) in enumerate(LESSONS))
    panels = []
    for i, (n, t, slides, topics, d) in enumerate(LESSONS):
        sl = ''.join(f'<div class="player__slide{" on" if j==0 else ""}" data-cap="{esc(n)}, slide {j+1}">{img(s, n + ", slide " + str(j+1) + " of " + str(len(slides)) + " from the Race, Rape Culture & Resistance learning series")}</div>' for j, s in enumerate(slides))
        panels.append(f'''<div class="lpanel" role="tabpanel" id="lp-{i}" aria-labelledby="ls-{i}"{"" if i==0 else " hidden"}><div class="player" data-player data-zoom data-interval="5000"><div class="player__bar"><i></i></div>{sl}<div class="player__ctl"><button data-prev aria-label="Previous slide">&#8249;</button><span class="player__cap"></span><button data-next aria-label="Next slide">&#8250;</button></div></div><div><p class="eyebrow">{esc(n)}</p><h3>{esc(t)}</h3><p>{esc(d)}</p><p style="font-weight:700;margin-bottom:.4em">Topics include</p><ul>{"".join(f"<li>{esc(x)}</li>" for x in topics)}</ul></div></div>''')
    tl = ''.join(f'<div class="tl2"><b>{esc(y)}</b><i></i><div><h3>{esc(n)}</h3><p>{esc(d)}</p></div></div>' for y, n, d in TIMELINE)
    body = f'''
<section class="rr-hero brick">
  <div class="wrap">
    <div>
      <nav class="crumbs" aria-label="Breadcrumb"><a href="index.html">Home</a><span>/</span><a href="library.html">Library</a><span>/</span><span>Race, Rape Culture, and Resistance</span></nav>
      <p class="eyebrow">A four-lesson learning series centered on Black youth</p>
      <h1 class="rr-title"><span>Race,</span><span>Rape Culture,</span><span>&amp; Resistance</span></h1>
      <p class="lede">SafeBAE was founded by young survivors who understood early on that sexual violence can’t be separated from race, power and visibility, especially for Black survivors. This series offers historical context, present-day analysis and pathways toward healing, grounded in the lived experiences that shaped SafeBAE from the beginning.</p>
      <div class="btns">{btn('Start the training', 'https://learning.safebae.org/race-rape-culture-and-resistance', 'slate')}{btn('Explore the lessons', '#lessons', 'ghost', arrow=True)}</div>
    </div>
    <div class="rr-photo">{img('2l3a1960', 'Jada Smith, SafeBAE co-founder', loading='eager')}<span class="sticker sticker--coral">Co-founder Jada Smith</span></div>
  </div>
</section>

<section class="rr-band rr-band--slate">
  <div class="wrap spot">
    <div>{yt('dE-wL8JePes', 'Jada’s Story', label='Watch')}</div>
    <div>
      <p class="eyebrow">Founder spotlight</p>
      <h2>Jada Smith</h2>
      <p style="color:rgba(255,255,255,.88)">Jada co-founded SafeBAE with a simple but powerful goal: to make sure what happened to her would never happen to anyone else. As a Black teenage survivor, her life was shaped not only by the harm she experienced, but by the way it was exploited online. Images of her unconscious body were shared without consent, sparking the viral hashtag #JadaPose and turning her assault into a public spectacle.</p>
      <p style="color:rgba(255,255,255,.88)">Rather than disappearing, Jada spoke out. By reclaiming her name, face and voice, she challenged a culture that too often treats Black girls’ pain as entertainment, and helped catalyze survivor-led resistance across the country.</p>
      <p class="jq">“There’s no point in hiding… Everybody has already seen my face and my body, but that’s not what I am and who I am.”</p>
      <div class="tags"><span>#JusticeForJada</span><span>#IAmJada</span><span>#StandWithJada</span><span>#JadaCounterPose</span></div>
    </div>
  </div>
</section>

<section class="rr-band" id="lessons">
  <div class="wrap">
    <p class="eyebrow">What to expect</p>
    <h2>Four lessons, from history to healing</h2>
    <p class="lede">Each lesson builds understanding across history, present-day realities, media, identity and healing, with a focus on how sexual violence operates in Black communities and what resistance looks like across generations. For youth, educators and communities seeking culturally grounded tools.</p>
    <div data-tabs="rrcr"><div class="ltabs" role="tablist" aria-label="Lessons">{tabs}</div>{''.join(panels)}</div>
  </div>
</section>

<section class="rr-band brick">
  <div class="wrap split split--top">
    <div><p class="eyebrow">From Lesson 1</p><h2>A long lineage of resistance</h2><p class="lede">Lesson 1 traces how racism and rape culture developed together in U.S. history, and places #MeToo within a much longer Black feminist lineage.</p>{btn('Start Lesson 1', 'https://learning.safebae.org/race-rape-culture-and-resistance', 'slate')}</div>
    <div class="tline">{tl}</div>
  </div>
</section>

<section class="rr-band">
  <div class="wrap"><div class="panel" style="box-shadow:none;border:1px solid var(--line)">
    <div class="panel__media">{img('dsc01134', 'SafeBAE student leaders')}</div>
    <div class="panel__body"><p class="eyebrow">Go further</p><h2 style="font-size:clamp(1.8rem,3vw,2.6rem)">Alongside the Certified Peer Educator Training</h2><p>SafeBAE expanded its Certified Peer Educator Training alongside this series.</p><div class="btns">{btn('Start the series', 'https://learning.safebae.org/race-rape-culture-and-resistance', 'teal')}{btn('Peer Educator Training', 'peer-educator.html', 'ghost', arrow=True)}</div></div>
  </div></div>
</section>
<section class="rr-band brick"><div class="wrap"><p class="eyebrow">Go deeper</p><h2>Related films and guides</h2>{related(['rape-culture', 'male-survivors', 'online-harassment'])}</div></section>
'''
    film_page('film-race-rape-culture-resistance.html', 'Race, Rape Culture, and Resistance', 'A four-lesson SafeBAE learning series centered on Black youth: history, present-day realities, media, identity and healing.', body, 'rrcr', 'family=DM+Serif+Display', CSS)
