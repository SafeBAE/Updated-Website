from films_common import *

SERIES_URL = 'https://learning.safebae.org/race-rape-culture-and-resistance'

# The series' own slides are set against a brick wall with line-drawn daisies growing in front of it.
BRICK = ("url(\"data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='76' height='38'%3E%3Crect width='76' height='38' fill='%23b4eff1'/%3E"
         "%3Cpath d='M0 1H76M0 20H76M1 0V19M39 19V38' stroke='%23dbffff' stroke-width='2.4' fill='none'/%3E%3C/svg%3E\")")

CSS = '''
/* Race, Rape Culture & Resistance: the series' own look. A brick wall, line-drawn daisies, marker-highlighted lesson labels, and a serif that carries the history. */
.film--rrcr{--serif:'DM Serif Display',Georgia,serif; --wall:''' + BRICK + '''; --f-card:#fff; --f-line:var(--line); --f-ink:var(--slate); --f-ink2:var(--ink-soft); --f-acc:var(--teal); --f-acc-ink:#fff; --f-lab:var(--logo-teal); --f-disp:var(--serif); --f-dw:400; --f-dl:-.005em; --f-ds:100%}
.film--rrcr main{background:#fff; color:var(--slate)}
.film--rrcr h1,.film--rrcr h2,.film--rrcr h3{font-family:var(--serif); font-weight:400; font-stretch:100%; letter-spacing:-.005em}

/* hero: the wall stands on the right, the portrait hangs on it, the daisy grows at its foot */
.rr-hero{background:var(--aqua); --wm-o:.34}
.rr-wall{position:absolute; z-index:0; top:0; bottom:0; right:0; left:calc(50% + min(18vw,250px)); background:var(--wall)}
.rr-hero .wm-daisy{right:-10%; bottom:-25%; width:min(52vw,700px)}
.rr-hero__g{display:grid; grid-template-columns:minmax(0,7fr) minmax(0,5fr); gap:clamp(28px,4vw,56px); align-items:stretch; padding-block:clamp(40px,5vw,72px) clamp(48px,6vw,84px)}
.rr-hero__txt{min-width:0; display:flex; flex-direction:column; align-items:flex-start}
.rr-hero .crumbs{color:var(--ink-soft)} .rr-hero .crumbs a{color:var(--logo-teal)}
.rr-title{font-size:clamp(3rem,7vw,6.4rem); line-height:.95; margin:0 0 .32em; color:var(--slate)}
.rr-title > span{display:block}
.rr-title > span:nth-child(2){color:var(--logo-teal)}
.rr-title .mk{padding:0 .04em}
.rr-hero .lede{margin:0 0 1.3em}
.rr-hero__txt .btns{margin-top:auto}
.rr-photo{position:relative; min-width:0; min-height:420px}
.rr-photo img{position:absolute; inset:0; width:100%; height:100%; object-fit:cover; object-position:50% 18%; border-radius:var(--r-xl); box-shadow:0 34px 64px -34px rgba(29,65,78,.7)}
.rr-photo .sticker{position:absolute; left:-14px; bottom:30px}

/* bands */
.rr-band{padding-block:var(--band); position:relative}
.rr-band--slate{background:var(--slate) var(--grain); color:#fff}
.rr-band--aqua{background:var(--aqua)}
.rr-band h2{font-size:clamp(2.2rem,4.6vw,3.8rem); line-height:1.02; margin:0}
.rr-band .eyebrow{color:var(--logo-teal)} .rr-band--slate .eyebrow{color:var(--mint)}
.rr-band .section-head{margin-bottom:var(--head-gap)}
.rr-hero :focus-visible, .rr-band:not(.rr-band--slate) :focus-visible{outline-color:var(--teal)}

/* founder spotlight: film and text end level, her words run the full width under them */
.rr-spot{display:grid; grid-template-columns:minmax(0,5fr) minmax(0,7fr); gap:clamp(28px,4vw,56px); align-items:stretch}
.rr-spot__media{display:flex; flex-direction:column; gap:20px; min-width:0}
.rr-vid{flex:1 1 auto; aspect-ratio:auto; display:grid; border-radius:var(--r-xl)}
.rr-vid::before{content:""; grid-area:1/1; padding-top:56.25%}
.rr-vid img{position:absolute; inset:0; object-position:50% 20%}
/* she is left of centre in the frame: the play button sits beside her, not on her face */
.rr-vid .vid__play{place-items:center end; padding:0 clamp(20px,8%,48px) 40px 0}
.rr-sign{display:grid; grid-template-columns:auto minmax(0,1fr); gap:20px; align-items:center}
.rr-sign__print{margin:0 0 0 6px; width:124px; padding:6px 6px 0; background:#fff; border-radius:4px; transform:rotate(-4deg); box-shadow:0 16px 30px -16px rgba(0,0,0,.7)}
.rr-sign__print img{display:block; width:100%; aspect-ratio:4/3; object-fit:cover; border-radius:2px}
.rr-sign__print figcaption{font-family:var(--mono); font-size:.7rem; font-weight:600; letter-spacing:.06em; line-height:1; color:var(--slate); text-align:center; padding:6px 0 7px}
.tags{display:flex; flex-wrap:wrap; gap:9px 10px}
.tags span{font-family:var(--display); font-weight:900; font-stretch:112%; font-size:.95rem; line-height:1.1; padding:8px 11px; border-radius:6px; background:var(--mint); color:var(--slate); transform:rotate(-1.5deg)}
.tags span:nth-child(even){background:var(--aqua); transform:rotate(1.5deg)}
.rr-spot__txt{min-width:0}
.rr-spot__txt h2{margin-bottom:.4em}
.rr-spot__txt p:not(.eyebrow){color:rgba(255,255,255,.9); font-size:1.06rem; line-height:1.65}
.rr-quote{margin:clamp(34px,4.4vw,60px) 0 0; padding-top:clamp(28px,3.4vw,44px); border-top:1px solid rgba(255,255,255,.2); display:grid; grid-template-columns:auto minmax(0,1fr); gap:0 clamp(16px,2.4vw,32px); align-items:start}
.rr-quote::before{content:"\\201C"; font-family:var(--serif); font-size:clamp(5rem,10vw,9rem); line-height:.74; color:var(--mint); grid-row:span 2}
.rr-quote blockquote{margin:0; font-family:var(--serif); font-size:clamp(1.7rem,3.9vw,3.5rem); line-height:1.12; color:#fff; text-wrap:pretty}
.rr-quote figcaption{margin-top:18px; font-family:var(--mono); font-size:.76rem; font-weight:600; letter-spacing:.12em; text-transform:uppercase; color:var(--mint)}

/* the four lessons: a rail of four title cards, and the open lesson under them */
.rr-rail{display:grid; grid-template-columns:repeat(4,minmax(0,1fr)); gap:var(--gap); margin:0 0 clamp(14px,1.6vw,20px)}
.rr-rail button{position:relative; font:inherit; cursor:pointer; text-align:left; display:flex; flex-direction:column; align-items:flex-start; gap:14px; min-height:136px; padding:20px 20px 22px; border-radius:var(--r-xl); border:1px solid var(--line); background:#fff; color:var(--slate); transition:transform .25s var(--ease), border-color .25s, background .25s, color .25s, box-shadow .25s}
.rr-rail button:hover{transform:translateY(-3px); border-color:var(--teal); box-shadow:var(--shadow-soft)}
.rr-rail__n{display:inline-block; font-family:var(--display); font-stretch:108%; font-weight:800; font-size:.95rem; line-height:1; padding:7px 13px 8px 11px; color:var(--slate); background:var(--aqua); border-radius:255px 14px 225px 14px / 14px 225px 14px 255px; transform:rotate(-1.5deg); transition:background .25s}
.rr-rail__t{display:block; font-family:var(--serif); font-size:clamp(1.2rem,1.75vw,1.45rem); line-height:1.14; text-wrap:balance}
.rr-rail button[aria-selected="true"]{background:var(--slate); border-color:var(--slate); color:#fff; box-shadow:var(--shadow-soft)}
.rr-rail button[aria-selected="true"] .rr-rail__n{background:var(--mint)}
.rr-rail button[aria-selected="true"]::after{content:""; position:absolute; left:50%; bottom:-10px; width:18px; height:18px; margin-left:-9px; background:var(--slate); transform:rotate(45deg); border-radius:0 0 4px 0}
.rr-lesson{border:1px solid var(--line); border-radius:var(--r-xl); background:#fff; overflow:hidden; box-shadow:var(--shadow-soft)}
.rr-lesson__top{display:grid; grid-template-columns:minmax(0,7fr) minmax(0,5fr); gap:clamp(24px,3.4vw,48px); align-items:stretch; padding:clamp(18px,2.4vw,30px)}
.rr-lesson__media{min-width:0}
.rr-lesson .player{border-radius:16px; box-shadow:none}
.rr-lesson .player__cap{font-size:.9rem}
.rr-lesson__txt{display:flex; flex-direction:column; align-items:flex-start; min-width:0}
.rr-lesson__k{font-family:var(--mono); font-size:.74rem; font-weight:600; letter-spacing:.12em; text-transform:uppercase; color:var(--logo-teal); margin:2px 0 .7rem}
.rr-lesson h3{font-size:clamp(1.7rem,2.6vw,2.2rem); line-height:1.06; margin:0 0 .42em; text-wrap:balance}
.rr-lesson__txt > p:not(.rr-lesson__k){margin:0 0 1em; font-size:.98rem; line-height:1.6}
.rr-lesson__txt .btn{margin-top:auto}
.rr-topics{padding:clamp(18px,2.2vw,26px) clamp(18px,2.4vw,30px) clamp(20px,2.4vw,30px); background:var(--mist); border-top:1px solid var(--line)}
.rr-topics > p{font-family:var(--mono); font-size:.74rem; font-weight:600; letter-spacing:.12em; text-transform:uppercase; color:var(--logo-teal); margin:0 0 14px}
.rr-topics ul{list-style:none; margin:0; padding:0; display:grid; grid-template-columns:repeat(5,minmax(0,1fr)); gap:16px var(--gap)}
.rr-topics li{margin:0; padding-top:12px; border-top:3px solid var(--teal); font-size:.95rem; line-height:1.45; font-weight:600}

/* lineage: one line, five stops, resistance at the end of it */
.rr-line{list-style:none; margin:0; padding:0; position:relative; display:grid; grid-template-columns:repeat(4,minmax(0,1fr)) minmax(0,1.5fr); gap:0 var(--gap)}
.rr-line::before{content:""; position:absolute; left:0; right:0; top:8px; height:3px; border-radius:3px; background:var(--teal)}
.rr-line li{position:relative; margin:0; padding-top:40px; min-width:0}
.rr-line li::before{content:""; position:absolute; left:0; top:0; width:19px; height:19px; border-radius:50%; background:var(--mint); border:4px solid var(--aqua); box-shadow:0 0 0 2.5px var(--teal)}
.rr-line b{display:block; font-family:var(--mono); font-size:.74rem; font-weight:600; letter-spacing:.12em; text-transform:uppercase; color:var(--logo-teal); margin-bottom:8px}
.rr-line h3{font-size:1.45rem; line-height:1.12; margin:0 0 8px}
.rr-line p{margin:0; font-size:.95rem; line-height:1.55; color:var(--ink-soft)}
.rr-line li:last-child{padding:40px 0 0}
.rr-line li:last-child::before{background:var(--slate); box-shadow:0 0 0 2.5px var(--slate)}
.rr-line li:last-child h3 span{display:block}
.rr-band--wallfoot{padding-bottom:calc(var(--band) + 57px)}
.rr-band--wallfoot::after{content:""; position:absolute; left:0; right:0; bottom:0; height:57px; background:var(--wall)}

/* alongside the Peer Educator Training, with the help line as its footer */
.rr-close{border:1px solid var(--line); border-radius:var(--r-xl); overflow:hidden; background:#fff; box-shadow:var(--shadow-soft)}
.rr-close__top{display:grid; grid-template-columns:minmax(0,5fr) minmax(0,7fr)}
.rr-close__media{position:relative; min-height:300px}
.rr-close__media img{position:absolute; inset:0; width:100%; height:100%; object-fit:cover; object-position:50% 30%}
.rr-close__body{display:flex; flex-direction:column; justify-content:center; align-items:flex-start; padding:clamp(24px,4vw,52px); min-width:0}
.rr-close__body h2{font-size:clamp(1.9rem,3.2vw,2.7rem); margin:0 0 .45em}
.rr-close__body p{margin:0 0 1.3em; font-size:1.08rem; line-height:1.6}
.rr-close__body .btns{gap:10px}
.rr-close__body .btn{white-space:nowrap}
.rr-close .fprep{border:0; border-radius:0}

@media (max-width:1100px){
  .rr-rail{grid-template-columns:repeat(2,minmax(0,1fr)); gap:12px}
  .rr-rail button{min-height:0; flex-direction:row; align-items:center; gap:16px; padding:16px 18px}
  .rr-rail__n{flex:none}
  .rr-rail button[aria-selected="true"]::after{display:none}
  .rr-lesson__top{grid-template-columns:minmax(0,1fr)}
  .rr-lesson__txt .btn{margin-top:4px}
  .rr-topics ul{grid-template-columns:repeat(6,minmax(0,1fr))}
  .rr-topics li{grid-column:span 2} .rr-topics li:nth-child(n+4){grid-column:span 3}
  .rr-line{grid-template-columns:repeat(6,minmax(0,1fr)); gap:34px var(--gap)}
  .rr-line::before{display:none}
  .rr-line li{grid-column:span 2; border-top:3px solid var(--teal); padding-top:26px} .rr-line li:nth-child(n+4){grid-column:span 3}
  .rr-line li::before{top:-11px}
  .rr-line li:last-child{padding-top:26px}
}
@media (max-width:900px){
  .rr-hero__g, .rr-close__top{grid-template-columns:minmax(0,1fr)}
  /* founder spotlight on one column: name, then the film, then her story */
  .rr-spot{display:flex; flex-direction:column; gap:0}
  .rr-spot__txt{display:contents}
  .rr-spot__txt .eyebrow{order:1} .rr-spot__txt h2{order:2; margin-bottom:.55em} .rr-spot__media{order:3; margin-bottom:26px} .rr-spot__txt p:not(.eyebrow){order:4}
  .rr-vid{flex:none}
  .rr-wall{left:0; top:auto; height:min(40%,calc(100vw + 20px))}
  .rr-photo{min-height:0; aspect-ratio:4/5; max-width:520px; width:100%}
  .rr-photo .sticker{left:10px}
  .rr-hero .wm-daisy{right:-34%; bottom:-8%; width:110vw}
  .rr-close__media{min-height:240px}
}
@media (max-width:640px){
  .rr-rail{grid-template-columns:minmax(0,1fr); gap:10px}
  .rr-topics ul{grid-template-columns:minmax(0,1fr); gap:12px} .rr-topics li:nth-child(n){grid-column:auto}
  .rr-line{grid-template-columns:minmax(0,1fr); gap:0; padding-left:34px}
  .rr-line::before{display:block; left:8px; right:auto; top:6px; bottom:6px; width:3px; height:auto}
  .rr-line li:nth-child(n){grid-column:auto; border-top:0; padding:0 0 26px}
  .rr-line li:last-child{padding-bottom:0}
  .rr-line li::before{left:-34px; top:2px}
  .rr-quote{grid-template-columns:minmax(0,1fr)} .rr-quote::before{grid-row:auto; line-height:.8; margin-bottom:-.18em}
  .rr-sign{grid-template-columns:minmax(0,1fr); gap:16px} .rr-sign__print{width:132px}
}
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
 ('Case', ['Celia'], 'One of the cases learners examine to see how racism and rape culture developed together in U.S. history.'),
 ('1866', ['Frances Thompson'], 'Her testimony about the 1866 Memphis Riot.'),
 ('Case', ['Sarah Baartman'], 'The exploitation of Sarah Baartman.'),
 ('Myth', ['Ida B. Wells'], 'Dismantled the “Black rapist” myth.'),
 ('Resistance', ['Recy Taylor', 'Betty Jean Owens', 'Tarana Burke'], 'Resistance that situates #MeToo within a much longer Black feminist lineage.'),
]

def build():
    n_l = len(LESSONS)
    tabs = ''.join(f'<button role="tab" id="ls-{i}" aria-controls="lp-{i}" aria-selected="{str(i==0).lower()}" tabindex="{0 if i==0 else -1}"><span class="rr-rail__n">{esc(n)}</span><span class="rr-rail__t">{esc(t)}</span></button>' for i, (n, t, *_r) in enumerate(LESSONS))
    panels = []
    for i, (n, t, slides, topics, d) in enumerate(LESSONS):
        sl = ''.join(f'<div class="player__slide{" on" if j==0 else ""}" data-cap="{esc(n)}, slide {j+1}">{img(s, n + ", slide " + str(j+1) + " of " + str(len(slides)) + " from the Race, Rape Culture & Resistance learning series")}</div>' for j, s in enumerate(slides))
        nxt = (f'<button class="btn btn--slate btn--sm" type="button" data-next-lesson="{i+1}">Next: {esc(LESSONS[i+1][0])}<span class="arr" aria-hidden="true">&rarr;</span></button>'
               if i + 1 < n_l else btn('Start the training', SERIES_URL, 'slate', 'sm'))
        panels.append(f'''<div class="rr-lesson" role="tabpanel" id="lp-{i}" aria-labelledby="ls-{i}"{"" if i==0 else " hidden"}>
<div class="rr-lesson__top">
  <div class="rr-lesson__media"><div class="player" data-player data-zoom data-interval="5000"><div class="player__bar"><i></i></div>{sl}<div class="player__ctl"><button data-prev aria-label="Previous slide">&#8249;</button><span class="player__cap"></span><button data-next aria-label="Next slide">&#8250;</button></div></div></div>
  <div class="rr-lesson__txt"><p class="rr-lesson__k">{esc(n)} of {n_l}</p><h3>{esc(t)}</h3><p>{esc(d)}</p>{nxt}</div>
</div>
<div class="rr-topics"><p>Topics include</p><ul>{"".join(f"<li>{esc(x)}</li>" for x in topics)}</ul></div>
</div>''')
    tl = ''.join(f'<li><b>{esc(y)}</b><h3>{" · ".join(esc(x) for x in names) if len(names) == 1 else "".join(f"<span>{esc(x)}{'' if k == len(names) - 1 else '<i class=sr-only>, </i>'}</span>" for k, x in enumerate(names))}</h3><p>{esc(d)}</p></li>' for y, names, d in TIMELINE)
    body = f'''
<section class="rr-hero fhero fhero--light"><span class="rr-wall" aria-hidden="true"></span><span class="wm-daisy" aria-hidden="true"></span>
  <div class="wrap rr-hero__g">
    <div class="rr-hero__txt rise">
      {film_crumbs('Race, Rape Culture, and Resistance')}
      <p class="eyebrow">A four-lesson learning series centered on Black youth</p>
      <h1 class="rr-title"><span>Race,</span><span>Rape Culture,</span><span>&amp; <span class="mk">Resistance</span></span></h1>
      <p class="lede">SafeBAE was founded by young survivors who understood early on that sexual violence can’t be separated from race, power and visibility, especially for Black survivors. This series offers historical context, present-day analysis and pathways toward healing, grounded in the lived experiences that shaped SafeBAE from the beginning.</p>
      <div class="btns">{btn('Start the training', SERIES_URL, 'slate')}{btn('Explore the lessons', '#lessons', 'ghost', arrow=True)}</div>
    </div>
    <div class="rr-photo">{img('2l3a1960', 'Jada Smith, SafeBAE co-founder', loading='eager')}<span class="sticker">Co-founder Jada Smith</span></div>
  </div>
</section>

<section class="rr-band rr-band--slate">
  <div class="wrap">
    <div class="rr-spot">
      <div class="rr-spot__media">{yt('dE-wL8JePes', 'Jada’s Story', thumb='jada-story-still', cls='rr-vid', label='Watch')}
        <div class="rr-sign"><figure class="rr-sign__print">{img('yt-de-wl8jepes', 'Jada Smith raises her fist and holds a sign that reads #IAMJADA')}<figcaption>#IAmJada</figcaption></figure>
        <div class="tags"><span>#JusticeForJada</span><span>#IAmJada</span><span>#StandWithJada</span><span>#JadaCounterPose</span></div></div>
      </div>
      <div class="rr-spot__txt">
        <p class="eyebrow">Founder spotlight</p>
        <h2>Jada Smith</h2>
        <p>Jada co-founded SafeBAE with a simple but powerful goal: to make sure what happened to her would never happen to anyone else. As a Black teenage survivor, her life was shaped not only by the harm she experienced, but by the way it was exploited online. Images of her unconscious body were shared without consent, sparking the viral hashtag #JadaPose and turning her assault into a public spectacle.</p>
        <p>Rather than disappearing, Jada spoke out. By reclaiming her name, face and voice, she challenged a culture that too often treats Black girls’ pain as entertainment, and helped catalyze survivor-led resistance across the country.</p>
      </div>
    </div>
    <figure class="rr-quote reveal"><blockquote>There’s no point in hiding… Everybody has already seen my face and my body, but that’s not what I am and who I am.”</blockquote><figcaption>Jada Smith</figcaption></figure>
  </div>
</section>

<section class="rr-band" id="lessons">
  <div class="wrap">
    <div class="section-head"><div><h2>Four lessons, from history to healing</h2>
    <p class="lede">Each lesson builds understanding across history, present-day realities, media, identity and healing, with a focus on how sexual violence operates in Black communities and what resistance looks like across generations. For youth, educators and communities seeking culturally grounded tools.</p></div></div>
    <div data-tabs="rrcr"><div class="rr-rail" role="tablist" aria-label="Lessons">{tabs}</div>{''.join(panels)}</div>
  </div>
</section>

<section class="rr-band rr-band--aqua rr-band--wallfoot">
  <div class="wrap">
    <div class="section-head"><div><p class="eyebrow">From Lesson 1</p><h2>A long lineage of resistance</h2><p class="lede">Lesson 1 traces how racism and rape culture developed together in U.S. history, and places #MeToo within a much longer Black feminist lineage.</p></div><div class="section-head__act">{btn('Start Lesson 1', SERIES_URL, 'slate')}</div></div>
    <ol class="rr-line reveal">{tl}</ol>
  </div>
</section>

<section class="rr-band">
  <div class="wrap"><div class="rr-close reveal">
    <div class="rr-close__top">
      <div class="rr-close__media">{img('dsc01134', 'SafeBAE student leaders')}</div>
      <div class="rr-close__body"><h2>Alongside the Certified Peer Educator Training</h2><p>SafeBAE expanded its Certified Peer Educator Training alongside this series.</p><div class="btns">{btn('Start the series', SERIES_URL, 'teal')}{btn('Peer Educator Training', 'peer-educator.html', 'ghost', arrow=True)}</div></div>
    </div>
    {help_card()}
  </div></div>
</section>
{frelated(['rape-culture', 'male-survivors', 'online-harassment'], 'rr-band rr-band--aqua', 'Related films and guides')}
'''
    js = r'''<script>
(function(){
  var tabs = [].slice.call(document.querySelectorAll('.rr-rail [role="tab"]'));
  document.querySelectorAll('[data-next-lesson]').forEach(function(n){ n.addEventListener('click', function(){
    var t = tabs[+n.getAttribute('data-next-lesson')]; if(!t) return;
    t.click(); t.focus({preventScroll:true});
    var top = document.querySelector('.rr-rail').getBoundingClientRect().top + window.scrollY - 120;
    if(window.scrollY > top) window.scrollTo({top: top, behavior: 'smooth'});
  }); });
})();
</script>'''
    film_page('film-race-rape-culture-resistance.html', 'Race, Rape Culture, and Resistance', 'A four-lesson SafeBAE learning series centered on Black youth: history, present-day realities, media, identity and healing.', body, 'rrcr', 'family=DM+Serif+Display', CSS, js)
