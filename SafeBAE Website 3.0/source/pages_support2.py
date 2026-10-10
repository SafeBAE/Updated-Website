"""Support & answers, part two (v3): myths-facts, faq, posters, blog.
(survivor-support and title-ix build from pages_support.)"""
from lib import *
from data import FAQ
from films_common import help_inline, HELPLINE_CSS, POSTERS_ZIP, FILM_CSS, lib_item
import datetime, re

WPU = 'https://www.safebae.org/wp-content/uploads/'
JOTFORM = 'https://form.jotform.com/243014598961160'
SUBSTACK = 'https://substack.com/@safebae'


def crumbs(*items):
    out = []
    for t, h in items:
        out.append(a(esc(t), h) if h else f'<span>{esc(t)}</span>')
    return '<nav class="crumbs" aria-label="Breadcrumb">' + '<span>/</span>'.join(out) + '</nav>'


def month(d):
    return datetime.date.fromisoformat(d).strftime('%b %Y')


def help_strip():
    """The shared help line as a slate strip. The page's one coral button stays the donate button."""
    return (help_inline(title='Free, confidential support, 24/7')
            .replace('class="helpline"', 'class="helpline sp-help"', 1)
            .replace('btn btn--coral btn--sm', 'btn btn--mint btn--sm'))


def next_cards(items):
    out = []
    for kicker, title, desc, href in items:
        ext = href.startswith('http')
        t = ' target="_blank" rel="noopener"' if ext else ''
        out.append(f'<a href="{esc(href)}"{t}><small>{esc(kicker)}</small><b>{esc(title)}</b><span>{esc(desc)}</span>'
                   f'<i class="go" aria-hidden="true">{"&#8599;" if ext else "&rarr;"}</i></a>')
    return '<div class="sp-next">' + ''.join(out) + '</div>'


def player(slides, label, cls='', pid='', interval=5200):
    """slides: list of (image, caption, alt)."""
    sl = ''.join(f'<div class="player__slide{" on" if i == 0 else ""}" data-cap="{esc(c)}">{img(n, alt, loading="eager" if i == 0 else "lazy")}</div>'
                 for i, (n, c, alt) in enumerate(slides))
    i = f' id="{pid}"' if pid else ''
    return (f'<div class="player {cls}"{i} data-player data-zoom data-interval="{interval}" aria-roledescription="carousel" aria-label="{esc(label)}">'
            f'<div class="player__bar"><i></i></div>{sl}<div class="player__ctl"><button type="button" data-prev aria-label="Previous slide">&#8249;</button>'
            f'<span class="player__cap"></span><button type="button" data-next aria-label="Next slide">&#8250;</button></div></div>')


def vibe_band(title='Worried you, or a friend, crossed a line?'):
    return f'''<section class="band band--teal sp-vibe" id="vibe-check">
  <div class="wrap sp-g sp-vibe__grid">
    <div class="sp-c7 sp-vibe__txt">
      <p class="sp-vibe__mark"><span class="daisy" aria-hidden="true"></span>Vibe Check by SafeBAE</p>
      <h2>{esc(title)}</h2>
      <p class="lede">CheckYourVibe.org is a free, anonymous reflection tool for young people who are questioning whether they, or a friend, may have crossed a boundary or caused harm.</p>
      <p>Young people are increasingly turning to anonymous forums and AI chatbots to ask difficult questions about relationships and consent. Vibe Check guides users through confusing situations and connects them with real, evidence-based resources on consent, communication and accountability. No names, no accounts, and nothing is stored.</p>
      <div class="btns">{btn('Open Vibe Check', 'https://checkyourvibe.org/', 'mint')}{btn('How it works', 'vibe-check.html', 'white', arrow=True)}</div>
    </div>
    <div class="sp-c5 sp-vibe__phone"><div class="sp-phone">{img('vc-screen', 'The Vibe Check home screen on a phone')}</div><span class="sticker">Anonymous</span><span class="sticker sticker--white sticker--r">Nothing is stored</span></div>
  </div>
</section>'''


SP_CSS = '''
/* ---------- shared by the four pages: 12 columns inside the wrap ---------- */
.sp-g{display:grid; grid-template-columns:repeat(12,minmax(0,1fr)); gap:var(--gap); align-items:stretch}
.sp-g > *{min-width:0}
.sp-c3{grid-column:span 3} .sp-c4{grid-column:span 4} .sp-c5{grid-column:span 5} .sp-c6{grid-column:span 6} .sp-c7{grid-column:span 7} .sp-c8{grid-column:span 8} .sp-c9{grid-column:span 9}
@media (max-width:900px){ .sp-g{grid-template-columns:minmax(0,1fr)} .sp-g > *{grid-column:auto} }
main .eyebrow{color:var(--logo-teal)}
main :is(.band--slate,.band--deep,.band--logo,.sp-hero--dark) .eyebrow{color:var(--mint)}
main .band--teal .eyebrow{color:#fff}
.section-head .lede{color:var(--ink-soft)}
:is(.band--slate,.band--deep) .section-head .lede{color:rgba(255,255,255,.88)}
/* heroes */
.sp-hero{position:relative; overflow:hidden}
.sp-hero > .wrap{position:relative; z-index:1}
.sp-hero--dark{background:var(--slate) var(--grain); color:#fff}
.sp-hero--dark .mk{background:none; color:var(--mint)}
.sp-hero--dark .lede{color:rgba(255,255,255,.9)}
.sp-hero--light{background:var(--aqua); color:var(--slate)}
.sp-hero--light .wm-daisy{color:var(--logo-teal)}
.sp-hero--light :focus-visible{outline-color:var(--teal)}
.sp-hero--light .crumbs{color:var(--ink-soft)} .sp-hero--light .crumbs a{color:var(--logo-teal)}
.sp-hero h1{font-stretch:122%; font-weight:900; text-transform:uppercase; line-height:.9; letter-spacing:-.02em; margin:0 0 .32em}
.sp-hero .lede{max-width:none}
/* small screens: heading, then the picture, then the text and actions */
@media (max-width:900px){
  .sp-hero .sp-g:has(> .sp-hero__media){display:flex; flex-direction:column; gap:0}
  .sp-hero__txt{display:contents}
  .sp-hero__txt > *{order:3}
  .sp-hero__txt > :is(.crumbs,.eyebrow,h1){order:1}
  .sp-hero__txt > .eyebrow{align-self:flex-start}
  .sp-hero__media{order:2; margin-block:4px 26px}
}
/* help line as a slate strip */
.helpline.sp-help{background:var(--slate) var(--grain); color:#fff; border-radius:var(--r-xl); padding:20px var(--pad-card)}
.helpline.sp-help b{font-size:1.15rem; line-height:1.2; margin-bottom:4px}
.helpline.sp-help span{color:rgba(255,255,255,.9); font-size:1rem; line-height:1.5}
.helpline.sp-help .btn{flex:none}
/* "where next" cards: label, title, text and arrow share rows across the four cards */
.sp-next{display:grid; grid-template-columns:repeat(4,minmax(0,1fr)); gap:var(--gap)}
.sp-next a{display:flex; flex-direction:column; gap:8px; padding:var(--pad-card); border-radius:var(--r-xl); background:#fff; border:1px solid var(--line); text-decoration:none; color:var(--slate); transition:transform .25s var(--ease), box-shadow .25s var(--ease), border-color .25s; min-width:0}
.sp-next a:hover{transform:translateY(-4px); box-shadow:var(--shadow-soft); border-color:var(--teal)}
.sp-next small{font-family:var(--mono); font-size:.72rem; letter-spacing:.1em; text-transform:uppercase; color:var(--logo-teal); font-weight:600}
.sp-next b{font-family:var(--display); font-stretch:108%; font-size:1.3rem; line-height:1.12; color:var(--logo-teal)}
.sp-next span{font-size:.97rem; color:var(--ink-soft); line-height:1.5}
.sp-next .go{margin-top:auto; width:34px; height:34px; border-radius:50%; display:grid; place-items:center; background:var(--aqua); color:var(--logo-teal); font-style:normal; font-weight:800; transition:background .2s, transform .2s var(--ease)}
.sp-next a:hover .go{background:var(--mint); transform:translateX(4px)}
@supports (grid-template-rows:subgrid){ @media (min-width:961px){
  .sp-next a{display:grid; grid-template-rows:subgrid; grid-row:span 4; row-gap:8px}
  .sp-next .go{margin-top:8px; align-self:end}
}}
@media (max-width:960px){.sp-next{grid-template-columns:repeat(2,minmax(0,1fr))}} @media (max-width:520px){.sp-next{grid-template-columns:minmax(0,1fr)}}
/* filter chips */
.sp-chips{display:flex; flex-wrap:wrap; gap:8px}
.sp-chips button{font:inherit; font-size:.92rem; font-weight:700; line-height:1.2; min-height:42px; padding:8px 16px; border-radius:999px; border:1.5px solid var(--line); background:#fff; color:var(--slate); cursor:pointer; transition:border-color .2s, background .2s, color .2s}
.sp-chips button:hover{border-color:var(--teal)}
.sp-chips button[aria-pressed="true"]{background:var(--slate); color:#fff; border-color:var(--slate)}
.sp-chips small{font-family:var(--mono); font-size:.74rem; opacity:.75; margin-left:6px}
@media (pointer:coarse){ .sp-chips button{min-height:44px} }
/* Vibe Check: a full teal band */
.sp-vibe__grid{align-items:center}
.sp-vibe__mark{display:flex; align-items:center; gap:12px; font-family:var(--display); font-weight:900; font-stretch:115%; font-size:1.2rem; color:var(--mint); margin:0 0 18px}
.sp-vibe__mark .daisy{width:38px; height:38px}
.sp-vibe h2{color:#fff}
.sp-vibe .lede, .sp-vibe__txt > p{color:#fff}
.sp-vibe__txt .btns{margin-top:1.4em}
.sp-vibe__phone{position:relative; padding-block:8px}
.sp-phone{width:min(270px,66vw); margin-inline:auto; aspect-ratio:390/800; border-radius:42px; border:10px solid #0b1f25; background:#0b1f25; overflow:hidden; transform:rotate(-4deg); box-shadow:0 50px 90px -30px rgba(0,0,0,.6)}
.sp-phone img{width:100%; height:100%; object-fit:cover; object-position:top}
.sp-vibe__phone .sticker{position:absolute; left:8%; top:16%}
.sp-vibe__phone .sticker--white{left:auto; top:auto; right:8%; bottom:18%}
@media (max-width:900px){.sp-vibe__grid{display:flex; flex-direction:column; gap:0} .sp-vibe__txt{display:contents} .sp-vibe__txt > *{order:3} .sp-vibe__txt > :is(.sp-vibe__mark,h2){order:1} .sp-vibe__phone{order:2; margin:10px 0 30px} .sp-phone{width:min(210px,56vw)}}
'''

# =====================================================================
# MYTHS & FACTS
# =====================================================================
MYTH_GROUPS = [
  ('Masculinity & male survivors', [
    ('Men are too strong to be assaulted.', 'Strength does not prevent sexual violence. At least <b>1 in 6 men</b> will experience sexual abuse or assault in their lifetime.'),
    ('Men always want sex and welcome all sexual advances.', 'Sexual assault is never wanted. It is a traumatic experience for any survivor, regardless of gender.'),
    ('Only gay men commit sexual violence against other men.', 'Sexual violence is about <b>power and control</b>, not sexual orientation. Survivors and perpetrators can be of any gender or identity.'),
    ('Men abused by women “got lucky.”', 'Sexual violence is never a privilege. Women can, and do, sexually abuse or assault boys and men. Survivors are not “lucky”; they are harmed and exploited.')]),
  ('Who it affects & who commits it', [
    ('“Real rape” is committed by strangers.', 'Anyone can be a perpetrator: date rape and stranger rape are both rape. Most rapes are committed by someone the victim knows: <b>92% of female victims</b> and <b>74% of male victims</b> report perpetrators who were acquaintances or intimate partners, and as many as <b>93% of child sexual abuse survivors</b> knew their abuser.'),
    ('Only women can be raped.', 'Sexual assault is experienced by people of all genders. <b>1 out of 10</b> rape victims is male, and <b>1 in 2</b> transgender people are sexually assaulted in their lifetime.'),
    ('Sexual assault can’t happen within a marriage or relationship.', 'Consent is required every time, in every relationship. A relationship, or a past “yes,” is never standing consent. Intimate partner sexual violence is real, harmful, and a crime in all 50 states.'),
    ('Sexual violence doesn’t happen to people with disabilities.', 'People with disabilities experience sexual violence at far higher rates. People with intellectual disabilities are sexually assaulted at <b>7 times the rate</b> of people without disabilities, and their abusers are often people they know and rely on.')]),
  ('Blame & believing survivors', [
    ('False claims of rape are common. Most are made for revenge, regret, or attention.', 'False reporting rates for sexual assault are in the <b>2–10% range</b>, the same as other crimes. The far bigger problem is under-reporting: the majority of sexual assaults are never reported to authorities at all.'),
    ('Clothing choices, location, and drinking can prevent rape and harassment.', 'Sexual assault is about <b>power, not clothing</b>. This logic holds survivors responsible for their own assaults instead of placing responsibility where it belongs: on perpetrators.'),
    ('If they didn’t fight back, it wasn’t really assault.', 'Freezing is one of the most common trauma responses. Many survivors experience <b>tonic immobility</b>, an involuntary reaction that makes it impossible to move or speak. Not fighting back is never consent.'),
    ('If it really happened, they would have reported it right away.', 'Delayed reporting is the norm, not the exception. Fear, shame, self-blame, and trauma keep many survivors silent for months, years, or forever. A delay says nothing about the truth of what happened.')]),
]
REASONS = ['It’s emotionally painful, and trauma can make details hard to remember.',
           'Shame and stigma: fear of being judged, blamed, or “slut-shamed.”',
           'Fear of not being believed, or that people will defend the perpetrator.',
           'Fear that nothing will be done: fewer than 2% of reports lead to a conviction.',
           'Fear of punishment or retaliation, especially for teens.',
           'Not realizing what happened was abuse in the first place.']
RISK = [('stats-marginalized2', 'Foster youth', 'Foster youth: compared to children living with both biological parents, children in foster care are 10 times more likely to be sexually abused. 81% of girls in foster care were sexually abused and 68% suffered abuse at the hands of multiple people.'),
        ('stats-marginalized3', 'Race and ethnicity', 'Race and ethnicity: non-white people often face numerous barriers to accessing resources and reporting. For every Black woman who reports rape, at least 15 Black women do not report.'),
        ('stats-marginalized4', 'Indigenous people', 'Indigenous people are at greatest risk of experiencing sexual violence in the United States. 41% of sexual assaults against Indigenous people in the U.S. are committed by a stranger.'),
        ('stats-marginalized5', 'Black youth', 'Black youth are also at increased risk of experiencing sexual violence. One in four Black girls will be sexually assaulted before they turn 18 (National Center on Violence Against Women in the Black Community).'),
        ('stats-marginalized6', 'People with disabilities', 'People with disabilities: youth with physical or developmental disabilities are 5 times more likely to be sexually assaulted than their nondisabled peers. Over 90% of people with developmental disabilities will experience sexual assault (University of Michigan).'),
        ('stats-marginalized7', 'LGBTQ+ people', 'LGBTQ+ people face increased barriers to reporting, including fears of being outed, risk of violence and of not being believed. Myth: being sexually assaulted by someone of the same gender can make a person gay or lesbian. Fact: the assault is typically not based on the sexual preferences of the victim or rapist, and therefore does not necessarily change the victim’s sexual orientation.'),
        ('stats-marginalized8', 'Lesbian and bisexual women', 'Lesbian and bisexual women are much more likely to experience sexual violence compared to heterosexual women, with 63% of bisexual, 49% of lesbian, and 35% of heterosexual women reporting being raped in their lifetime by anyone (NIH).'),
        ('stats-marginalized9', 'Transgender and gender diverse people', 'Transgender and gender diverse people: almost half of all transgender people have been sexually assaulted at some point in their lives, and these rates are even higher for non-white trans people and those who have done sex work, been homeless, or have a disability (National Center for Transgender Equality).'),
        ('stats-marginalized10', 'Transgender people face the greatest risks', 'Transgender people face the greatest risks for all types of violence, especially those who have more than one marginalized identity. Transgender people are significantly more likely to be murdered during their assault. #ProtectTransYouth'),
        ('stats-marginalized11', 'Statistics on male survivors', 'Statistics on male survivors: over half of male victims of completed or attempted rape reported experiencing their first victimization prior to age 18. Men are more likely to be sexually assaulted than be falsely accused of rape.')]
CAUSES = [('Being under the influence', 'var(--coral)'), ('The clothes someone is wearing', 'var(--mint)'), ('Walking alone', 'var(--teal)'),
          ('Flirty behavior', 'var(--aqua)'), ('Hooking up with a lot of people', 'var(--gray)')]
ELEMENTS = ['Victim blaming', 'Racial stereotypes', 'Rape myths', 'Media + algorithms', 'Peer influence', 'Gender + sexuality beliefs']
WALL_LINE = 'Reporting for survivors can feel like hitting a brick wall.'

MF_CSS = '''
/* hero */
.mf-hero .wrap{padding-block:clamp(40px,5vw,72px) clamp(40px,5vw,64px)}
.mf-hero__txt{align-self:center}
.mf-hero h1{font-size:clamp(2.3rem,4.5vw,4.3rem)}
.mf-hero .lede{margin:0}
.mf-strike{position:relative; display:inline-block}
.mf-strike::after{content:""; position:absolute; left:-4%; right:-4%; top:52%; height:.11em; background:var(--coral); border-radius:.06em; transform:rotate(-4deg) scaleX(0); transform-origin:left; animation:mfstrike .7s .5s cubic-bezier(.2,.8,.2,1) forwards}
@keyframes mfstrike{to{transform:rotate(-4deg) scaleX(1)}}
.mf-hero__media{position:relative; min-height:clamp(300px,29vw,400px)}
.mf-hero__photo{position:absolute; inset:30px 0 0 0; border-radius:var(--r-xl); overflow:hidden; box-shadow:var(--shadow-soft)}
.mf-hero__photo img{width:100%; height:100%; object-fit:cover; object-position:40% 60%}
.mf-hero__card{position:absolute; right:-18px; top:0; width:min(74%,318px); height:156px; perspective:1000px; animation:sb-rise .9s .4s var(--ease) both}
.mf-hero__in{position:relative; width:100%; height:100%; transform-style:preserve-3d; animation:mfcard 1s 1.9s var(--ease) both}
.mf-hero__face{position:absolute; inset:0; backface-visibility:hidden; -webkit-backface-visibility:hidden; border-radius:var(--r-xl); padding:18px 22px; display:flex; flex-direction:column; gap:8px; background:var(--slate-deep); border:1.5px solid var(--line-dark); box-shadow:var(--shadow-soft)}
.mf-hero__face small{font-family:var(--mono); font-size:.72rem; letter-spacing:.12em; text-transform:uppercase; font-weight:600; color:var(--coral)}
.mf-hero__face b{font-family:var(--display); font-stretch:106%; font-size:1.14rem; line-height:1.25}
.mf-hero__face--back{background:var(--mint); color:var(--slate); border-color:var(--mint); transform:rotateY(180deg)}
.mf-hero__face--back small{color:var(--slate)}
/* the preview card turns once, from the myth to the fact, and rests */
@keyframes mfcard{from{transform:rotateY(0)} to{transform:rotateY(180deg)}}
.mf-qs{display:grid; grid-template-columns:repeat(4,minmax(0,1fr)); gap:var(--gap); margin-top:clamp(28px,3.4vw,44px)}
.mf-qs a{display:grid; grid-template-rows:auto 1fr auto; gap:10px; min-height:146px; padding:20px 22px; border-radius:14px; background:var(--slate-deep); border:1px solid var(--line-dark); color:#fff; text-decoration:none; transition:background .2s, transform .25s var(--ease), color .2s, border-color .2s}
.mf-qs a:hover{background:var(--mint); border-color:var(--mint); color:var(--slate); transform:translateY(-4px)}
.mf-qs small{font-family:var(--mono); font-size:.72rem; letter-spacing:.1em; text-transform:uppercase; color:var(--mint); font-weight:600}
.mf-qs a:hover small{color:var(--slate)}
.mf-qs b{font-family:var(--display); font-stretch:110%; font-size:clamp(1.15rem,1.7vw,1.4rem); line-height:1.1; text-wrap:balance}
.mf-qs i{font-style:normal; font-weight:800; width:30px; height:30px; border-radius:50%; display:grid; place-items:center; background:rgba(255,255,255,.1); transition:transform .25s var(--ease), background .2s}
.mf-qs a:hover i{transform:translateY(3px); background:rgba(29,65,78,.14)}
@media (max-width:960px){.mf-qs{grid-template-columns:repeat(2,minmax(0,1fr))}}
@media (max-width:900px){.mf-hero__media{min-height:0; height:clamp(250px,62vw,420px)} .mf-hero__card{right:10px}}
@media (max-width:520px){.mf-qs{gap:10px} .mf-qs a{min-height:124px; padding:16px}}

/* causes: the pie beside the culture that excuses it */
.mf-pie{background:var(--mist); border:1px solid var(--line); border-radius:var(--r-xl); padding:var(--pad-card); display:grid; grid-template-columns:minmax(0,5fr) minmax(0,6fr); grid-template-rows:auto 1fr auto; gap:20px clamp(20px,3vw,40px); align-items:center}
.mf-pie__title{grid-column:1/-1; margin:0; font-family:var(--display); font-weight:900; font-stretch:125%; text-transform:uppercase; font-size:clamp(1.6rem,3vw,2.4rem); line-height:1; letter-spacing:-.01em; color:var(--logo-teal)}
.mf-pie__chart{position:relative; aspect-ratio:1; width:100%; max-width:290px; justify-self:center}
.mf-pie__chart svg{width:100%; height:100%; transform:rotate(-90deg); display:block}
.mf-pie__chart .bg{fill:#fff; stroke:var(--line); stroke-width:2}
.mf-pie__chart .fill{fill:none; stroke:var(--slate); stroke-width:100; stroke-dasharray:0 100; transition:stroke-dasharray 1s cubic-bezier(.2,.8,.2,1)}
.mf-pie__pct{position:absolute; inset:0; display:grid; place-items:center; font-family:var(--display); font-weight:900; font-stretch:112%; font-size:clamp(2.2rem,4vw,3.4rem); color:var(--slate); transition:color .4s}
.mf-pie.full .mf-pie__pct{color:var(--mint)}
.mf-pie__legend{list-style:none; padding:0; margin:0; display:grid; gap:8px}
.mf-pie__legend li{margin:0}
.mf-pie__legend button{display:flex; align-items:center; gap:12px; width:100%; min-height:46px; text-align:left; font:inherit; font-weight:700; font-size:.98rem; line-height:1.25; padding:8px 14px; border-radius:12px; border:1.5px solid var(--line); background:#fff; color:var(--slate); cursor:pointer; transition:border-color .2s, background .2s, color .2s}
.mf-pie__legend button::before{content:""; flex:none; width:20px; height:20px; border-radius:5px; background:var(--sw); box-shadow:inset 0 0 0 1px rgba(29,65,78,.18)}
.mf-pie__legend button:hover{border-color:var(--teal)}
.mf-pie__legend button[aria-pressed="true"] .t{text-decoration:line-through; text-decoration-thickness:2px; color:var(--ink-soft)}
.mf-pie__legend button[aria-pressed="true"]::after{content:"0%"; margin-left:auto; font-family:var(--display); font-weight:900; font-size:1rem; color:var(--slate)}
.mf-pie__legend .is-cause[aria-pressed="true"]{background:var(--slate); color:#fff; border-color:var(--slate)} .mf-pie__legend .is-cause[aria-pressed="true"] .t{text-decoration:none; color:#fff}
.mf-pie__legend .is-cause[aria-pressed="true"]::after{content:"100%"; color:var(--mint)}
.mf-pie__msg{grid-column:1/-1; margin:0; padding-top:18px; border-top:1px solid var(--line); min-height:calc(3em + 18px); font-size:1rem; font-weight:600; line-height:1.5}
.mf-pie__msg b{font-family:var(--display); font-stretch:110%}
.mf-culture{background:var(--slate) var(--grain); color:#fff; border-radius:var(--r-xl); padding:var(--pad-card); display:flex; flex-direction:column}
.mf-culture > p{margin:0; color:rgba(255,255,255,.94); font-size:1.1rem; line-height:1.58}
.mf-culture .mf-els-label{font-family:var(--mono); font-size:.72rem; letter-spacing:.1em; text-transform:uppercase; color:var(--mint); font-weight:600; margin:24px 0 0}
.mf-els{list-style:none; margin:10px 0 0; padding:0; display:grid; grid-template-columns:repeat(2,minmax(0,1fr)); grid-auto-rows:1fr; gap:0 20px; flex:1}
.mf-els li{margin:0; padding:12px 0; border-top:2px solid var(--mint); font-family:var(--display); font-stretch:106%; font-weight:800; font-size:1.08rem; line-height:1.2; display:flex; align-items:center}
@media (max-width:560px){.mf-pie{grid-template-columns:minmax(0,1fr)} .mf-pie__chart{max-width:220px}}

/* why survivors don't report */
.mf-wall{position:relative; border-radius:var(--r-xl); overflow:hidden; display:grid; place-items:center; padding:clamp(26px,3.4vw,44px); min-height:260px; container-type:inline-size; background:#94d7db url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='136' height='88'%3E%3Cpath d='M0 2.5H136M0 46.5H136M2.5 0V46M70.5 46V88' stroke='%23d1feff' stroke-width='5' fill='none'/%3E%3C/svg%3E") 0 0/136px 88px; box-shadow:var(--shadow-soft)}
.mf-wall p{margin:0; font-family:var(--display); font-weight:800; font-stretch:108%; font-size:clamp(1.7rem,13cqi,3.5rem); line-height:1.04; letter-spacing:-.01em; text-align:center; color:var(--slate); text-wrap:balance; text-shadow:0 0 12px #94d7db, 0 0 12px #94d7db, 0 0 5px #94d7db}
.mf-reasons{list-style:none; padding:0; margin:0; display:grid; grid-template-columns:repeat(2,minmax(0,1fr)); grid-auto-rows:1fr; gap:12px}
.mf-reasons li{margin:0; background:#fff; border-radius:14px; padding:18px 20px; font-weight:650; font-size:1.02rem; line-height:1.45; display:flex; align-items:center; box-shadow:0 10px 24px -22px rgba(29,65,78,.6)}
@media (max-width:560px){.mf-reasons{grid-template-columns:minmax(0,1fr); grid-auto-rows:auto}}

/* a real example */
.mf-meg__a,.mf-meg__b{display:flex; flex-direction:column; gap:var(--gap)}
.mf-meg__txt h2{margin-bottom:.45em}
.mf-meg__txt p{font-size:1.04rem}
.mf-tweet{margin:auto 0 0; border:1px solid var(--line); border-radius:var(--r-xl); overflow:hidden; background:#fff; box-shadow:var(--shadow-soft)}
.mf-tweet img{width:100%}
.mf-tweet figcaption{font-size:.9rem; color:var(--ink-soft); padding:10px 18px 12px; border-top:1px solid var(--line)}
.mf-meg__q{margin:0; flex:1; container-type:inline-size; display:flex; flex-direction:column; justify-content:center; padding:clamp(22px,3vw,40px); border-radius:var(--r-xl); background:var(--slate) var(--grain); color:#fff}
.mf-meg__q blockquote{margin:0; font-family:var(--display); font-stretch:104%; font-weight:700; font-size:clamp(1.25rem,6.4cqi,1.95rem); line-height:1.28; text-wrap:pretty}
.mf-meg__q .cite{color:var(--mint); margin-top:18px}
@media (max-width:560px){.mf-meg .vid{aspect-ratio:auto; display:flex; flex-direction:column} .mf-meg .vid img{aspect-ratio:16/9; height:auto} .mf-meg .vid__play{inset:0 0 auto 0; aspect-ratio:16/9} .mf-meg .vid__label{position:static; flex-wrap:wrap; gap:4px 12px}}
@media (max-width:900px){.mf-meg__a,.mf-meg__b{display:contents} .mf-meg{gap:20px} .mf-meg .vid{order:2} .mf-meg__q{order:3} .mf-tweet{order:4; margin:0}}

/* myths vs. facts: the wall of flip cards */
.mf-mvf-head{margin-bottom:var(--head-gap)}
.mf-mvf-head__txt{display:flex; flex-direction:column}
.mf-mvf-head__txt h2{margin:0 0 .3em}
.mf-mvf-head__txt .lede{color:rgba(255,255,255,.9); margin:0}
.mf-mvf-head .vid{align-self:end}
.mf-ctl{margin-top:auto; padding-top:22px; display:flex; flex-wrap:wrap; align-items:center; gap:14px 26px}
.mf-meter{display:flex; flex-wrap:wrap; align-items:center; gap:10px 14px; margin:0; font-weight:700; font-size:.98rem}
.mf-meter b{font-family:var(--display); font-weight:900; font-size:1.5rem; color:var(--mint); margin-right:2px}
.mf-meter__pips{display:flex; gap:5px}
.mf-meter__pips i{width:13px; height:13px; border-radius:50%; border:2px solid rgba(255,255,255,.4); transition:background .3s, border-color .3s, transform .3s var(--ease)}
.mf-meter__pips i:nth-child(4n+1):not(:first-child){margin-left:7px}
.mf-meter__pips i.on{background:var(--mint); border-color:var(--mint); transform:scale(1.12)}
.mf-grp + .mf-grp{margin-top:clamp(28px,3.4vw,44px)}
.mf-grp h3{display:flex; align-items:baseline; flex-wrap:wrap; gap:6px 14px; color:#fff; font-size:clamp(1.3rem,2vw,1.6rem); margin:0 0 16px}
.mf-grp h3 small{font-family:var(--mono); font-size:.72rem; letter-spacing:.1em; text-transform:uppercase; color:var(--mint); font-weight:600}
.mf-flips{display:grid; grid-template-columns:repeat(2,minmax(0,1fr)); gap:var(--gap)}
.mf-flips .flip{min-height:0; height:100%}
.mf-flips .flip__in{height:100%}
.mf-flips .flip__face{min-height:200px; border-radius:var(--r-xl); padding:var(--pad-card); gap:12px}
.mf-flips .flip__face--front{background:var(--slate-deep); border:1.5px solid var(--line-dark); transition:border-color .25s}
.mf-flips .flip:hover .flip__face--front{border-color:var(--mint)}
.mf-flips .flip__tag{font-size:.74rem}
.mf-flips .flip__face--front .flip__tag{color:var(--coral)}
.mf-flips .flip__face--front .flip__txt{font-size:clamp(1.35rem,2.3vw,1.8rem); font-stretch:106%; font-weight:800; line-height:1.14; margin-block:auto; text-wrap:balance}
.mf-flips .flip__face--back .flip__txt{font-family:var(--body); font-weight:550; font-size:1.03rem; line-height:1.52; margin-block:auto}
.mf-flips .flip__face--back .flip__txt b{font-family:var(--display); font-weight:900; font-stretch:108%}
.mf-flips .flip__face .hint{margin-top:0; display:flex; align-items:center; gap:.5em; font-size:.9rem; font-weight:700; opacity:1}
.mf-flips .flip__face--front .hint{color:var(--mint)}
.mf-flips .hint::after{content:"\\2192"; transition:transform .2s var(--ease)}
.mf-flips .flip:hover .hint::after{transform:translateX(4px)}
.mf-flips .flip:focus-visible{outline-offset:4px}
@media (max-width:700px){.mf-flips{grid-template-columns:minmax(0,1fr)} .mf-flips .flip__face{min-height:180px}}
.mf-choke{align-items:center; margin-top:clamp(30px,3.6vw,48px); padding:var(--pad-card); border-radius:var(--r-xl); background:rgba(255,255,255,.05); border:1px solid var(--line-dark)}
.mf-choke__label{padding:8px 14px 8px 8px}
.mf-choke__tag{margin:0 0 10px; font-family:var(--mono); font-size:.72rem; letter-spacing:.1em; text-transform:uppercase; font-weight:600; color:var(--mint)}
.mf-choke__pair{display:flex; flex-wrap:wrap; gap:8px; margin:0 0 12px}
.mf-choke__pair span{font-family:var(--display); font-stretch:106%; font-weight:800; font-size:1.14rem; line-height:1.2; padding:9px 14px; border-radius:12px; background:var(--slate-deep); border:1px solid var(--line-dark)}
.mf-choke__pair span:last-child{background:var(--mint); color:var(--slate); border-color:var(--mint)}
.mf-choke__pair small{display:block; font-family:var(--mono); font-size:.72rem; letter-spacing:.1em; text-transform:uppercase; font-weight:600; opacity:.85; margin-bottom:2px}
.mf-choke__txt{margin:0; font-size:.98rem; line-height:1.55; color:rgba(255,255,255,.9)}
.mf-choke__act{display:flex; justify-content:flex-end}
@media (max-width:900px){.mf-choke__label{max-width:320px; padding-right:8px} .mf-choke__act{justify-content:flex-start}}

/* who is most at risk */
.mf-risk__hint{margin:.9em 0 0; font-weight:600; line-height:1.5; color:var(--slate)}
.mf-risk__list{display:grid; grid-template-columns:repeat(5,minmax(0,1fr)); gap:8px; margin-bottom:14px}
.mf-risk__list button{font:inherit; font-size:.92rem; font-weight:700; text-align:left; line-height:1.25; min-height:58px; padding:10px 14px; border-radius:12px; border:1.5px solid var(--line); background:#fff; color:var(--slate); cursor:pointer; transition:border-color .2s, background .2s, color .2s}
.mf-risk__list button:hover{border-color:var(--teal)}
.mf-risk__list button[aria-pressed="true"]{background:var(--slate); color:#fff; border-color:var(--slate); box-shadow:inset 0 -4px 0 var(--mint)}
.mf-risk .player{border-radius:var(--r-xl)}
.mf-risk .player__cap{font-size:.92rem}
.mf-after{margin-top:var(--head-gap); display:grid; gap:var(--gap)}
@media (max-width:860px){.mf-risk__list{grid-template-columns:repeat(2,minmax(0,1fr))}}
'''


def myths_facts():
    flips_html = []
    for g, items in MYTH_GROUPS:
        cards = ''.join(f'<button type="button" class="flip" data-flip aria-pressed="false"><span class="flip__in"><span class="flip__face flip__face--front"><span class="flip__tag">Myth</span><span class="flip__txt">{esc(m)}</span><span class="hint">Tap for the fact</span></span>'
                        f'<span class="flip__face flip__face--back"><span class="flip__tag">Fact</span><span class="flip__txt">{f}</span><span class="hint">Tap to flip back</span></span></span></button>' for m, f in items)
        flips_html.append(f'<div class="mf-grp reveal"><h3>{esc(g)} <small>{len(items)} myths</small></h3><div class="mf-flips">{cards}</div></div>')
    n_myths = sum(len(i) for _, i in MYTH_GROUPS)
    legend = ''.join(f'<li><button type="button" aria-pressed="false" style="--sw:{c}" data-v="0"><span class="t">{esc(t)}</span></button></li>' for t, c in CAUSES)
    legend += '<li><button type="button" aria-pressed="false" style="--sw:var(--slate)" data-v="100" class="is-cause"><span class="t">Rapist</span></button></li>'
    els = ''.join(f'<li>{esc(e)}</li>' for e in ELEMENTS)
    reasons = ''.join(f'<li>{esc(r)}</li>' for r in REASONS)
    risk_chips = ''.join(f'<button type="button" data-go="{i}" aria-pressed="{str(i == 0).lower()}">{esc(c)}</button>' for i, (n, c, alt) in enumerate(RISK))

    body = f'''
<section class="sp-hero sp-hero--dark mf-hero">
  <span class="wm-daisy" aria-hidden="true"></span>
  <div class="wrap">
    <div class="sp-g">
      <div class="sp-c7 rise sp-hero__txt mf-hero__txt">
        {crumbs(('Home', 'index.html'), ('Resources', 'resources.html'), ('Myths & Facts', None))}
        <p class="eyebrow">Myths, facts &amp; statistics</p>
        <h1>Let’s debunk the <span class="mk mf-strike">myths</span> about sexual assault.</h1>
        <p class="lede">What the research actually says about sexual violence, who is most affected, and why so much of it goes unreported.</p>
      </div>
      <div class="sp-c5 sp-hero__media mf-hero__media">
        <div class="mf-hero__photo">{img('img-2400', 'Students sitting in a circle during a SafeBAE discussion', loading='eager')}</div>
        <div class="mf-hero__card" aria-hidden="true"><div class="mf-hero__in">
          <div class="mf-hero__face"><small>Myth</small><b>If they didn’t fight back, it wasn’t really assault.</b></div>
          <div class="mf-hero__face mf-hero__face--back"><small>Fact</small><b>Freezing is one of the most common trauma responses. Not fighting back is never consent.</b></div>
        </div></div>
      </div>
    </div>
    <nav class="mf-qs" aria-label="Questions on this page">
      <a href="#causes"><small>Causes</small><b>What causes sexual violence?</b><i aria-hidden="true">&darr;</i></a>
      <a href="#survivors-report"><small>Reporting</small><b>Why don’t survivors report?</b><i aria-hidden="true">&darr;</i></a>
      <a href="#myths-vs-facts"><small>{n_myths} myths</small><b>Understanding myths vs. facts</b><i aria-hidden="true">&darr;</i></a>
      <a href="#who-is-most-at-risk"><small>Risk</small><b>Who is most at risk?</b><i aria-hidden="true">&darr;</i></a>
    </nav>
  </div>
</section>

<section class="band band--paper" id="causes">
  <div class="wrap">
    <div class="section-head"><div><h2>What causes sexual violence?</h2>
      <p class="lede lede--full">People blame a lot of things: being under the influence, the clothes someone is wearing, walking alone, flirty behavior, or hooking up with a lot of people. None of these cause sexual violence. It happens when someone chooses to ignore or violate another person’s boundaries and consent.</p></div></div>
    <div class="sp-g">
      <div class="sp-c7 mf-pie reveal" id="mfPie">
        <p class="mf-pie__title">Causes of rape</p>
        <div class="mf-pie__chart"><svg viewBox="0 0 200 200" aria-hidden="true"><circle class="bg" cx="100" cy="100" r="99"/><circle class="fill" cx="100" cy="100" r="50" pathLength="100"/></svg><span class="mf-pie__pct" aria-hidden="true">?</span></div>
        <ul class="mf-pie__legend">{legend}</ul>
        <p class="mf-pie__msg" aria-live="polite">Tap each one to see how much of the chart it takes up.</p>
      </div>
      <div class="sp-c5 mf-culture reveal">
        <p>That choice is often reinforced by rape culture: victim-blaming, harmful stereotypes, peer pressure, media, algorithms, and beliefs about gender, sexuality, power, and entitlement. Prevention means holding people accountable and challenging the culture that excuses harm.</p>
        <p class="mf-els-label">Elements of rape culture</p>
        <ul class="mf-els">{els}</ul>
      </div>
    </div>
  </div>
</section>

<section class="band band--aqua" id="survivors-report">
  <div class="wrap">
    <div class="section-head"><div><h2>Why don’t survivors report?</h2>
      <p class="lede lede--full" style="color:var(--slate)">If a survivor doesn’t report to the police, it does NOT mean the violence didn’t happen. There are many reasons someone might not come forward:</p></div></div>
    <div class="sp-g">
      <div class="sp-c5 mf-wall reveal"><p>{esc(WALL_LINE)}</p></div>
      <ul class="sp-c7 mf-reasons reveal">{reasons}</ul>
    </div>
  </div>
</section>

<section class="band band--paper" id="megan">
  <div class="wrap sp-g mf-meg">
    <div class="sp-c6 mf-meg__a">
      <div class="mf-meg__txt">
        <p class="eyebrow">Real example</p>
        <h2>Megan Thee Stallion</h2>
        <p>In 2020, Megan Thee Stallion was harmed by someone she knew. When police arrived, she said she had stepped on glass because she feared the situation could escalate into police violence. After she later spoke out, she was mocked, doubted, and blamed publicly.</p>
        <p>Her story shows why reporting is never simple, and why we should never assume silence means nothing happened. Survivors deserve to be believed, supported, and given choices.</p>
      </div>
      <figure class="mf-tweet">{img('63abc69e2b109-image', 'Tweet from Megan Thee Stallion, @theestallion, January 21, 2021: “Y’all so believe black women and protect black women online BUT WHEN I LITERALLY SAY I GOT SHOT ITS CONFUSING”')}<figcaption>Megan Thee Stallion on Twitter, January 21, 2021</figcaption></figure>
    </div>
    <div class="sp-c6 mf-meg__b">
      {yt('EY7aAlieiko', 'Gayle King on Megan Thee Stallion’s Hurt and Pain From 2020 Shooting', label='Entertainment Tonight')}
      <figure class="mf-meg__q"><blockquote>“I didn’t want them to kill any of us, or shoot any of us. So I just said I stepped on glass… Even though this person just did this to me, my first reaction still was to try to save us. I didn’t want to see anybody die.”</blockquote><span class="cite">Megan Thee Stallion</span></figure>
    </div>
  </div>
</section>

<section class="band band--slate" id="myths-vs-facts">
  <div class="wrap">
    <div class="sp-g mf-mvf-head">
      <div class="sp-c7 mf-mvf-head__txt"><p class="eyebrow">{n_myths} myths &middot; {len(MYTH_GROUPS)} themes</p><h2>Myths vs. facts: sexual violence</h2>
        <p class="lede">Tap a card to flip it and see what the research says.</p>
        <div class="mf-ctl"><button class="btn btn--mint" type="button" id="mfAll">Reveal all facts</button>
          <p class="mf-meter" aria-live="polite"><span><b id="mfN">0</b> of {n_myths} myths debunked</span><span class="mf-meter__pips" aria-hidden="true">{'<i></i>' * n_myths}</span></p></div></div>
      {yt('elCyCZb9BU8', 'Sexual Assault: Myths vs. Facts', thumb='yt-elcyczb9bu8-a', label='SafeBAE', cls='sp-c5')}
    </div>
    {''.join(flips_html)}
    <aside class="sp-g mf-choke" aria-label="From the Choking Hazard campaign">
      <div class="sp-c4 mf-choke__label">{hz_label("hz--tilt")}</div>
      <div class="sp-c5 mf-choke__body">
        <p class="mf-choke__tag">One more myth, from Choking Hazard</p>
        <p class="mf-choke__pair"><span><small>Myth</small>“It’s safe if you do it right.”</span><span><small>Fact</small>There’s no safe way.</span></p>
        <p class="mf-choke__txt">SafeBAE’s campaign on sexual strangulation, which young people call “choking”, gives young people, parents and educators the evidence, myth-vs-fact, and the signs that need medical care.</p>
      </div>
      <div class="sp-c3 mf-choke__act">{btn('Choking Hazard', 'choking-hazard.html', 'mint', arrow=True)}</div>
    </aside>
  </div>
</section>

<section class="band band--paper" id="who-is-most-at-risk">
  <div class="wrap">
    <div class="section-head"><div><p class="eyebrow">Who is most at risk?</p><h2>Identity shapes risk, and access to help</h2>
      <p class="lede lede--full">Different identities, and the intersections between them, play a big role in the risk of experiencing violence and in access to reporting and healing resources. As you read these statistics, remember that there’s a lack of research on many marginalized groups, so these numbers are subject to change, and this is in no way a comprehensive list.</p>
      <p class="mf-risk__hint">Explore the slide deck to learn more about how different marginalized groups experience heightened risk, barriers to reporting, and unequal access to support.</p></div></div>
    <div class="mf-risk reveal">
      <div class="mf-risk__list" role="group" aria-label="Jump to a slide">{risk_chips}</div>
      {player(RISK, 'Stats: marginalized groups, ten slides', '', 'mfPlayer', interval=7000)}
    </div>
    <div class="mf-after">{help_strip()}
    {next_cards([('Support', 'Survivor support', 'Hotlines, healing resources and what to say when someone tells you.', 'survivor-support.html'),
                 ('Film + guide', 'Supporting male survivors', 'Theo Hutt’s story, and the myths that keep male survivors silent.', 'film-sexual-assault-of-men.html'),
                 ('Rights', 'Title IX', 'What your school owes you and how to ask for supportive measures.', 'title-ix.html'),
                 ('Answers', 'FAQ', 'Why survivors don’t report, rape culture, coercion and more.', 'faq.html')])}
    </div>
  </div>
</section>

{give_band()}
'''
    js = r'''<script>
(function(){
  var pie = document.getElementById('mfPie');
  if(pie){ var fill = pie.querySelector('.fill'), pct = pie.querySelector('.mf-pie__pct'), msg = pie.querySelector('.mf-pie__msg'), bs = pie.querySelectorAll('.mf-pie__legend button');
    bs.forEach(function(b){ b.addEventListener('click', function(){ b.setAttribute('aria-pressed','true'); var v = +b.getAttribute('data-v');
      if(v){ fill.style.strokeDasharray = '100 100'; pie.classList.add('full'); pct.textContent = '100%'; msg.innerHTML = '<b>Rapist: 100%.</b> It happens when someone chooses to ignore or violate another person’s boundaries and consent.'; }
      else { if(!pie.classList.contains('full')) pct.textContent = '0%'; msg.innerHTML = '<b>' + b.textContent + ': 0%.</b> None of these cause sexual violence.'; } }); }); }
  /* the flip wall: count what has been debunked */
  var all = document.getElementById('mfAll'), flips = [].slice.call(document.querySelectorAll('.mf-flips .flip')), nEl = document.getElementById('mfN'), pips = document.querySelectorAll('.mf-meter__pips i'), seen = {};
  function meter(){ var n = 0; flips.forEach(function(f, i){ if(seen[i]) n++; if(pips[i]) pips[i].classList.toggle('on', !!seen[i]); }); if(nEl) nEl.textContent = n;
    var shown = flips.every(function(f){ return f.getAttribute('aria-pressed') === 'true'; }); if(all){ all.setAttribute('data-on', shown ? '1' : '0'); all.textContent = shown ? 'Show the myths again' : 'Reveal all facts'; } }
  flips.forEach(function(f, i){ f.addEventListener('click', function(){ setTimeout(function(){ if(f.getAttribute('aria-pressed') === 'true') seen[i] = 1; meter(); }, 0); }); });
  if(all) all.addEventListener('click', function(){ var on = all.getAttribute('data-on') !== '1'; flips.forEach(function(f, i){ f.setAttribute('aria-pressed', String(on)); if(on) seen[i] = 1; }); if(!on) seen = {}; meter(); });
  /* risk slides: the index above the player follows it */
  var pl = document.getElementById('mfPlayer'), chips = document.querySelectorAll('[data-go]');
  if(pl && chips.length){ var cap = pl.querySelector('.player__cap'), nx = pl.querySelector('[data-next]'), N = pl.querySelectorAll('.player__slide').length;
    function cur(){ return (parseInt(cap.textContent, 10) || 1) - 1; }
    chips.forEach(function(c){ c.addEventListener('click', function(){ var steps = (+c.getAttribute('data-go') - cur() + N) % N; for(var i = 0; i < steps; i++) nx.click(); }); });
    new MutationObserver(function(){ var k = cur(); chips.forEach(function(c){ c.setAttribute('aria-pressed', String(+c.getAttribute('data-go') === k)); }); }).observe(cap, {childList:true, characterData:true, subtree:true}); }
})();
</script>'''
    page('myths-facts.html', 'Myths & Facts · SafeBAE',
         'SafeBAE debunks common myths about sexual assault with research and statistics, covering causes, underreporting, male survivors, and who is most at risk.',
         body, active='resources', body_class='mf', head_extra=f'<style>{SP_CSS}{HELPLINE_CSS}{MF_CSS}</style>', scripts=js)


# =====================================================================
# FAQ
# =====================================================================
FAQ_CATS = [('faq-consent', 'Consent'), ('faq-violence', 'Sexual violence'), ('faq-relationships', 'Healthy relationships'),
            ('faq-online', 'Online safety & nudes'), ('faq-action', 'Action & your rights'), ('faq-healing', 'Support & healing')]
FAQ_LONG = {  # canonical long-form posts on safebae.org (from the live WordPress site)
  'Why don’t survivors report sexual assault?': 'https://www.safebae.org/why-dont-survivors-report-sexual-assault/',
  'What is Title IX and what are my rights at school?': 'https://www.safebae.org/what-is-title-ix-student-rights/',
}
FAQ_REL = {
  'What is consent?': [('Practice in the BAE Skills Lab', 'skills-lab.html'), ('Choking Hazard: why choking can’t meet the pillars of consent', 'choking-hazard.html')],
  'Can someone give consent if they’re drunk or high?': ('Myths & facts about blame', 'myths-facts.html#myths-vs-facts'),
  'What is rape culture?': ('Film: Rape Culture & a Culture of Respect', 'film-rape-culture.html'),
  'Why don’t survivors report sexual assault?': ('Why survivors don’t report', 'myths-facts.html#survivors-report'),
  'Can boys and men be victims of sexual violence?': ('Film: Supporting Male Survivors', 'film-sexual-assault-of-men.html'),
  'What are the signs of a healthy relationship?': ('Film: It’s Giving Red Flags', 'film-its-giving-red-flags.html'),
  'What are the signs of an unhealthy or abusive relationship?': ('Talk to love is respect', 'survivor-support.html#hotlines'),
  'What are the risks of sending nudes?': [('Film: #knowB4Unude', 'film-knowb4unude.html'), ('AI Literacy Training: fake images and sextortion', 'ai-literacy.html')],
  'What is bystander intervention?': ('Film: BAEcode: Game On!', 'film-baecode-game-on.html'),
  'What is Title IX and what are my rights at school?': ('Your rights under Title IX', 'title-ix.html'),
  'How do I report sexual assault? What are my options?': ('Hotlines and local help', 'survivor-support.html#hotlines'),
  'How do I support a friend who has been sexually assaulted?': ('What to say, and what not to say', 'survivor-support.html#when-someone-tells-you'),
  'How do survivors heal after sexual assault?': ('Healing resources', 'survivor-support.html#healing'),
}

FQ_CSS = '''
/* hero: the question box is the page's main control */
.fq-hero .wrap{padding-block:clamp(40px,5vw,72px) clamp(40px,5vw,64px)}
.fq-hero__txt{align-self:center}
.fq-hero h1{font-size:clamp(2.4rem,4.5vw,4.3rem); color:var(--logo-teal)}
.fq-hero .lede{margin:0 0 1.3em}
.fq-search{display:flex; gap:10px; align-items:center; background:#fff; border-radius:16px; padding:8px 8px 8px 20px; box-shadow:0 22px 44px -26px rgba(29,65,78,.55); border:2px solid transparent; transition:border-color .2s}
.fq-search:focus-within{border-color:var(--teal)}
.fq-search svg{width:22px; height:22px; color:var(--teal); flex:none}
.fq-search input{flex:1; min-width:0; border:0; outline:0; font:inherit; font-size:1.1rem; color:var(--slate); background:transparent; padding:12px 0}
.fq-search input::placeholder{color:var(--ink-soft); opacity:1}
.fq-search input::-webkit-search-cancel-button{display:none}
.fq-search button{flex:none}
.fq-count{flex:none; font-family:var(--mono); font-size:.76rem; letter-spacing:.08em; text-transform:uppercase; color:var(--logo-teal); font-weight:600; white-space:nowrap; padding-right:10px}
@media (max-width:520px){.fq-search{flex-wrap:wrap; padding:6px 8px 6px 16px} .fq-search input{font-size:1.02rem} .fq-count{order:9; flex:0 0 100%; padding:0 0 9px 32px}}
.fq-meta{display:flex; flex-wrap:wrap; align-items:center; gap:8px 10px; margin:16px 0 0}
.fq-meta__l{font-family:var(--mono); font-size:.76rem; letter-spacing:.1em; text-transform:uppercase; font-weight:600; color:var(--logo-teal); margin-right:4px}
.fq-try{font:inherit; font-size:.9rem; font-weight:700; line-height:1.2; min-height:36px; padding:6px 13px; border-radius:999px; border:1.5px solid rgba(29,90,102,.3); background:transparent; color:var(--logo-teal); cursor:pointer; transition:background .2s, border-color .2s, color .2s}
.fq-try:hover{background:#fff; border-color:var(--teal)}
.fq-try[aria-pressed="true"]{background:var(--slate); border-color:var(--slate); color:#fff}
@media (pointer:coarse){ .fq-try{min-height:44px} }
.fq-hero__media{position:relative; min-height:clamp(320px,31vw,430px)}
.fq-hero__photo{position:absolute; inset:20px 0 24px 0; border-radius:var(--r-xl); overflow:hidden; box-shadow:var(--shadow-soft)}
.fq-hero__photo img{width:100%; height:100%; object-fit:cover; object-position:50% 30%}
.fq-ask-b{position:absolute; z-index:1; display:inline-flex; align-items:center; gap:8px; font-family:var(--display); font-stretch:106%; font-weight:800; font-size:clamp(.95rem,1.25vw,1.08rem); line-height:1.2; padding:12px 16px; border-radius:18px; text-decoration:none; box-shadow:var(--shadow-soft); transition:transform .25s var(--ease); animation:sb-rise .9s var(--ease) both}
.fq-ask-b i{font-style:normal; transition:transform .2s var(--ease)}
.fq-ask-b:hover{transform:translateY(-3px)} .fq-ask-b:hover i{transform:translateX(3px)}
.fq-ask-b--a{left:-14px; top:0; background:#fff; color:var(--logo-teal); border-bottom-left-radius:4px; animation-delay:.45s}
.fq-ask-b--b{right:-14px; top:46%; background:var(--slate); color:#fff; border-bottom-right-radius:4px; animation-delay:.7s}
.fq-ask-b--c{left:9%; bottom:0; background:var(--mint); color:var(--slate); border-bottom-left-radius:4px; animation-delay:.95s}
@media (max-width:900px){.fq-hero__media{min-height:0; height:clamp(260px,64vw,420px)} .fq-ask-b--a{left:8px} .fq-ask-b--b{right:8px}}

/* topic bar: sticks under the header and shows the filter state */
.fq-jump{position:sticky; top:76px; z-index:30; background:rgba(255,255,255,.96); backdrop-filter:blur(6px); border-bottom:1px solid var(--line)}
.fq-jump .wrap{display:flex; align-items:center; gap:14px; padding-block:12px}
.fq-jump :focus-visible{outline-color:var(--teal)}
.fq-jump__list{position:relative; display:flex; gap:7px; overflow-x:auto; scrollbar-width:none; flex:1; min-width:0; padding:2px 26px 2px 2px; margin-right:-12px; -webkit-mask-image:linear-gradient(90deg,#000 calc(100% - 26px),transparent); mask-image:linear-gradient(90deg,#000 calc(100% - 26px),transparent)}
.fq-jump__list::-webkit-scrollbar{display:none}
.fq-jump a{flex:none; display:inline-flex; align-items:center; min-height:40px; font-size:.92rem; font-weight:700; padding:8px 13px; border-radius:999px; border:1.5px solid var(--line); text-decoration:none; color:var(--slate); white-space:nowrap; background:#fff; transition:background .2s, color .2s, border-color .2s, opacity .2s}
.fq-jump a small{font-family:var(--mono); font-size:.74rem; color:var(--logo-teal); margin-left:7px}
.fq-jump a:hover{border-color:var(--teal)}
.fq-jump a.on{background:var(--slate); color:#fff; border-color:var(--slate)} .fq-jump a.on small{color:var(--mint)}
.fq-jump a.off{opacity:.35; pointer-events:none}
.fq-jump__clear{flex:none; display:inline-flex; align-items:center; gap:8px; min-height:40px; font:inherit; font-size:.9rem; font-weight:800; padding:8px 14px; border-radius:999px; border:0; background:var(--mint); color:var(--slate); cursor:pointer; white-space:nowrap}
.fq-jump__clear span{max-width:14ch; overflow:hidden; text-overflow:ellipsis}
@media (pointer:coarse){ .fq-jump a,.fq-jump__clear{min-height:44px} }
@media (max-width:700px){ .fq-jump__clear span{display:none} }

/* topic groups: heading on top, questions below at the full width of the column */
.fq-cat{scroll-margin-top:150px}
.fq-cat:not([hidden]) ~ .fq-cat{margin-top:clamp(40px,5vw,68px)}
.fq-cat[hidden]{display:none}
.fq-cat__head{display:flex; align-items:baseline; justify-content:space-between; gap:10px 24px; flex-wrap:wrap; border-top:4px solid var(--slate); padding-top:18px; margin-bottom:10px}
.fq-cat__head h2{font-size:clamp(1.6rem,2.8vw,2.4rem); margin:0}
.fq-cat__head small{font-family:var(--mono); font-size:.76rem; letter-spacing:.1em; text-transform:uppercase; color:var(--logo-teal); font-weight:600}
.fq-acc{border-top:0}
.fq-acc details{scroll-margin-top:150px; border-bottom:1px solid var(--line); transition:background .25s}
.fq-acc details[hidden]{display:none}
.fq-acc summary{font-size:clamp(1.12rem,1.55vw,1.32rem); padding:20px 64px 20px 0; transition:color .2s}
.fq-acc summary::after{right:8px; width:34px; height:34px; margin-top:-17px; background-size:16px}
.fq-acc summary:hover{color:var(--teal)}
.fq-acc summary:hover::after{background-color:var(--mint)}
/* the open answer is a panel: text at reading width on the left, related links as rows on the right */
.fq-acc details[open]{background:var(--mist); border-color:transparent; border-radius:var(--r-xl); margin:10px calc(var(--fq-out) * -1) 12px; padding-inline:var(--fq-out)}
.fq-acc{--fq-out:clamp(12px,2vw,26px)}
.fq-acc details[open] summary{padding-top:22px; padding-bottom:10px; color:var(--logo-teal)}
.fq-acc details:has(+ details[open]){border-color:transparent}
.fq-a{display:grid; grid-template-columns:repeat(12,minmax(0,1fr)); gap:14px var(--gap); padding:4px 0 var(--fq-out)}
.fq-a > p{grid-column:span 7; margin:0; font-size:1.06rem; line-height:1.68; color:var(--slate)}
.fq-links{grid-column:span 5; align-self:start}
.fq-links__h{display:block; font-family:var(--mono); font-size:.72rem; letter-spacing:.1em; text-transform:uppercase; font-weight:600; color:var(--logo-teal); padding-bottom:8px; border-bottom:1px solid var(--line)}
.fq-row{display:grid; grid-template-columns:minmax(0,1fr) auto; gap:14px; align-items:center; min-height:58px; padding:10px 0; border-bottom:1px solid var(--line); text-decoration:none; color:var(--slate)}
.fq-row b{display:block; font-family:var(--display); font-stretch:105%; font-weight:800; font-size:1.04rem; line-height:1.25; color:var(--logo-teal)}
.fq-row small{display:block; font-size:.88rem; color:var(--ink-soft); margin-top:2px}
.fq-row i{font-style:normal; font-weight:800; width:34px; height:34px; border-radius:50%; display:grid; place-items:center; background:#fff; border:1px solid var(--line); color:var(--logo-teal); transition:background .2s, transform .2s var(--ease), border-color .2s}
.fq-row:hover b{text-decoration:underline; text-decoration-color:var(--mint); text-decoration-thickness:3px; text-underline-offset:3px}
.fq-row:hover i{background:var(--mint); border-color:var(--mint); transform:translateX(3px)}
.fq-acc mark{background:rgba(21,255,200,.5); color:inherit; border-radius:3px; padding:0 1px}
@media (max-width:860px){.fq-a > p,.fq-links{grid-column:1/-1}}
.fq-empty{display:grid; grid-template-columns:repeat(12,minmax(0,1fr)); gap:var(--gap); align-items:center; padding:var(--pad-card); border-radius:var(--r-xl); background:var(--mist); border:1px solid var(--line)}
.fq-empty__txt{grid-column:span 7}
.fq-empty h2{font-size:clamp(1.5rem,2.6vw,2.1rem); margin:0 0 .4em; overflow-wrap:anywhere}
.fq-empty p{margin:0 0 1.2em; color:var(--ink-soft)}
.fq-empty__try{grid-column:span 5; align-self:stretch; display:flex; flex-direction:column; justify-content:center; padding:var(--pad-card); border-radius:14px; background:#fff; border:1px solid var(--line)}
.fq-empty__try small{font-family:var(--mono); font-size:.72rem; letter-spacing:.1em; text-transform:uppercase; font-weight:600; color:var(--logo-teal); margin-bottom:10px}
.fq-empty__try div{display:flex; flex-wrap:wrap; gap:8px}
@media (max-width:860px){.fq-empty__txt,.fq-empty__try{grid-column:1/-1}}

/* still have a question */
.fq-ask > div{border-radius:var(--r-xl); padding:var(--pad-card); display:flex; flex-direction:column; gap:8px}
.fq-ask > div .btns{margin-top:auto; padding-top:14px}
.fq-ask__a{background:var(--mist); border:1px solid var(--line)}
.fq-ask__b{background:var(--slate) var(--grain); color:#fff}
.fq-ask__b .eyebrow{color:var(--mint)}
.fq-ask__b p{color:rgba(255,255,255,.9)}
.fq-ask h3{margin:0; font-size:clamp(1.4rem,2.2vw,1.8rem)}
.fq-ask p{margin:0; font-size:1.02rem}
'''

FQ_TRY = ['consent', 'report', 'nudes', 'Title IX']


def slugify(s):
    return re.sub(r'[^a-z0-9]+', '-', s.lower().replace('’', '')).strip('-')[:60]


def faq():
    total = sum(len(q) for _, q in FAQ)
    jump = ''.join(f'<a href="#{cid}" data-cat="{cid}">{esc(lbl)}<small>{len(FAQ[i][1])}</small></a>' for i, (cid, lbl) in enumerate(FAQ_CATS))
    cats = []
    for i, (cat, qs) in enumerate(FAQ):
        cid, short = FAQ_CATS[i]
        dets = []
        for q, ans, link in qs:
            long = FAQ_LONG.get(q, link if link.startswith('http') else None)
            rel = FAQ_REL.get(q)
            rows = ''
            if long:
                rows += (f'<a class="fq-row" href="{esc(long)}" target="_blank" rel="noopener"><span><b>Read the full answer</b><small>safebae.org</small></span>'
                         '<i aria-hidden="true">&#8599;</i></a>')
            for r_ in ([rel] if isinstance(rel, tuple) else (rel or [])):
                ext = r_[1].startswith('http')
                t = ' target="_blank" rel="noopener"' if ext else ''
                rows += (f'<a class="fq-row" href="{esc(r_[1])}"{t}><span><b>{esc(r_[0])}</b></span>'
                         f'<i aria-hidden="true">{"&#8599;" if ext else "&rarr;"}</i></a>')
            dets.append(f'<details id="q-{slugify(q)}"><summary>{esc(q)}</summary><div class="acc__body fq-a"><p>{esc(ans)}</p>'
                        f'<div class="fq-links"><small class="fq-links__h">Related</small>{rows}</div></div></details>')
        cats.append(f'<section class="fq-cat" id="{cid}" data-cat="{cid}"><header class="fq-cat__head"><h2>{esc(cat)}</h2>'
                    f'<small data-n="{len(qs)}">{len(qs)} question{"s" if len(qs) != 1 else ""}</small></header><div class="acc fq-acc">{"".join(dets)}</div></section>')
    tries = ''.join(f'<button type="button" class="fq-try" data-try="{esc(t)}" aria-pressed="false">{esc(t)}</button>' for t in FQ_TRY)
    tries2 = ''.join(f'<button type="button" class="fq-try" data-try="{esc(t)}">{esc(t)}</button>' for t in FQ_TRY)

    body = f'''
<section class="sp-hero sp-hero--light fq-hero">
  <span class="wm-daisy" aria-hidden="true"></span>
  <div class="wrap sp-g">
    <div class="sp-c6 rise sp-hero__txt fq-hero__txt">
    {crumbs(('Home', 'index.html'), ('Resources', 'resources.html'), ('FAQ', None))}
    <h1>Frequently asked <span class="mk">questions</span></h1>
    <p class="lede">SafeBAE answers your questions about teen dating violence, sexual assault, consent, and healthy relationships.</p>
    <form class="fq-search" role="search" onsubmit="return false"><label class="sr-only" for="fq-q">Filter the questions</label>{ICON_SEARCH}<input id="fq-q" type="search" placeholder="Type to filter the questions" autocomplete="off"><output class="fq-count" id="fq-count" for="fq-q" aria-live="polite">{total} questions</output><button class="btn btn--slate btn--sm" type="button" id="fq-clear" hidden>Clear</button></form>
    <div class="fq-meta"><span class="fq-meta__l">Try</span>{tries}</div>
    </div>
    <div class="sp-c6 sp-hero__media fq-hero__media">
      <div class="fq-hero__photo">{img('sumact5', 'Three students talking during a SafeBAE Summer Activist Institute session', loading='eager')}</div>
      <a class="fq-ask-b fq-ask-b--a" href="#q-what-is-consent">What is consent?<i aria-hidden="true">&rarr;</i></a>
      <a class="fq-ask-b fq-ask-b--b" href="#q-how-do-i-support-a-friend-who-has-been-sexually-assaulted">How do I support a friend?<i aria-hidden="true">&rarr;</i></a>
      <a class="fq-ask-b fq-ask-b--c" href="#q-what-is-title-ix-and-what-are-my-rights-at-school">What are my rights at school?<i aria-hidden="true">&rarr;</i></a>
    </div>
  </div>
</section>
<nav class="fq-jump" aria-label="FAQ topics"><div class="wrap"><div class="fq-jump__list">{jump}</div><button type="button" class="fq-jump__clear" id="fq-clear2" hidden>Clear <span id="fq-term2"></span> &times;</button></div></nav>
<section class="band band--paper">
  <div class="wrap">
    <div id="fq-list">{''.join(cats)}</div>
    <div class="fq-empty" id="fq-empty" hidden>
      <div class="fq-empty__txt"><h2>No questions match “<span id="fq-term"></span>”.</h2><p>Try a shorter word, or search every page, film and podcast on the site.</p>
        <div class="btns"><button class="btn btn--slate" type="button" id="fq-site">Search the whole site</button>{btn('Ask the SafeBAE team', 'contact.html', 'ghost')}</div></div>
      <div class="fq-empty__try"><small>Try one of these</small><div>{tries2}</div></div>
    </div>
  </div>
</section>
{vibe_band('Not sure if you crossed a line?')}
<section class="band band--paper band--tight">
  <div class="wrap sp-g fq-ask">
    <div class="sp-c6 fq-ask__a reveal"><p class="eyebrow" style="margin:0">Still have a question?</p><h3>Ask the SafeBAE team</h3><p class="muted">Reach the SafeBAE team with questions about our programs, trainings and resources.</p><div class="btns">{btn('Contact us', 'contact.html', 'slate', arrow=True)}{btn('Myths & facts', 'myths-facts.html', 'ghost')}</div></div>
    <div class="sp-c6 fq-ask__b reveal"><p class="eyebrow" style="margin:0">Need to talk to someone?</p><h3>Free, confidential support</h3><p>Text LOVEIS to 22522, call 800-656-HOPE (4673), or call or text 988. Most lines are open 24/7.</p><div class="btns"><button class="btn btn--mint" type="button" data-open-help>All hotlines</button>{btn('Survivor support', 'survivor-support.html', 'ghost', arrow=True)}</div></div>
  </div>
</section>
{give_band()}
'''
    js = r'''<script>
(function(){
  var inp = document.getElementById('fq-q'); if(!inp) return;
  var items = [].slice.call(document.querySelectorAll('.fq-acc details')), cats = [].slice.call(document.querySelectorAll('.fq-cat')), jl = [].slice.call(document.querySelectorAll('.fq-jump a'));
  var cnt = document.getElementById('fq-count'), empty = document.getElementById('fq-empty'), term = document.getElementById('fq-term'), clr = document.getElementById('fq-clear'), total = items.length;
  var clr2 = document.getElementById('fq-clear2'), term2 = document.getElementById('fq-term2'), tries = [].slice.call(document.querySelectorAll('[data-try]')), list = document.getElementById('fq-list');
  function norm(s){ return (s || '').toLowerCase().normalize('NFD').replace(/[\u0300-\u036f]/g, '').replace(/[’']/g, ''); }
  items.forEach(function(d){ d._t = norm(d.textContent); d._s = d.querySelector('summary'); d._s0 = d._s.textContent; d._p = d.querySelector('.acc__body p'); d._p0 = d._p.textContent; });
  function escH(s){ return s.replace(/&/g,'&amp;').replace(/</g,'&lt;').replace(/>/g,'&gt;'); }
  function mark(txt, terms){ var h = escH(txt); if(!terms.length) return h; terms.forEach(function(t){ if(t.length < 2) return; var re = new RegExp('(' + t.replace(/[.*+?^${}()|[\]\\]/g, '\\$&') + ')', 'ig'); h = h.replace(re, '<mark>$1</mark>'); }); return h; }
  function run(){ var raw = inp.value.trim(), terms = norm(raw).split(/\s+/).filter(Boolean), n = 0;
    items.forEach(function(d){ var ok = terms.every(function(t){ return d._t.indexOf(t) >= 0; }); d.hidden = !ok; if(ok) n++;
      d._s.innerHTML = mark(d._s0, terms.length ? raw.split(/\s+/) : []); d._p.innerHTML = mark(d._p0, terms.length ? raw.split(/\s+/) : []); });
    cats.forEach(function(c){ var k = c.querySelectorAll('details:not([hidden])').length, lab = c.querySelector('.fq-cat__head small'), N = +lab.getAttribute('data-n'); c.hidden = !k; lab.textContent = (terms.length && k < N) ? (k + ' of ' + N + ' match') : (N + ' question' + (N === 1 ? '' : 's')); });
    jl.forEach(function(l){ var c = document.getElementById(l.getAttribute('data-cat')); l.classList.toggle('off', !!(c && c.hidden)); });
    if(terms.length && n && n <= 4) items.forEach(function(d){ if(!d.hidden && !d.open){ d.open = true; d._auto = 1; } });
    if(!terms.length) items.forEach(function(d){ if(d._auto){ d.open = false; d._auto = 0; } });
    cnt.textContent = terms.length ? (n + ' of ' + total + ' match') : (total + ' questions');
    empty.hidden = n > 0; list.hidden = n === 0; term.textContent = raw; clr.hidden = !raw; clr2.hidden = !raw; term2.textContent = raw ? '“' + raw + '”' : '';
    tries.forEach(function(b){ if(b.hasAttribute('aria-pressed')) b.setAttribute('aria-pressed', String(norm(b.getAttribute('data-try')) === norm(raw))); }); }
  inp.addEventListener('input', run);
  function clear(){ inp.value = ''; run(); }
  clr.addEventListener('click', function(){ clear(); inp.focus(); });
  clr2.addEventListener('click', clear);
  tries.forEach(function(b){ b.addEventListener('click', function(){ var t = b.getAttribute('data-try'); inp.value = (norm(inp.value.trim()) === norm(t)) ? '' : t; run(); }); });
  document.getElementById('fq-site').addEventListener('click', function(){ if(window.SB && SB.openSearch) SB.openSearch(inp.value); });
  try{ var m = location.search.match(/[?&]q=([^&]+)/); if(m){ inp.value = decodeURIComponent(m[1].replace(/\+/g,' ')); run(); } }catch(e){}
  /* open a question from the hash */
  function openHash(){ var h = location.hash.slice(1); if(!h) return; var el = document.getElementById(h); if(el && el.tagName === 'DETAILS'){ var was = el.hidden; if(was) clear(); el.open = true; if(was) setTimeout(function(){ el.scrollIntoView({block:'start'}); }, 40); } }
  openHash(); window.addEventListener('hashchange', openHash);
  /* active topic in the bar */
  if('IntersectionObserver' in window){ var io = new IntersectionObserver(function(es){ es.forEach(function(e){ if(e.isIntersecting){ var id = e.target.id; jl.forEach(function(l){ var on = l.getAttribute('data-cat') === id; l.classList.toggle('on', on); if(on && l.scrollIntoView && l.parentNode.scrollWidth > l.parentNode.clientWidth){ l.parentNode.scrollLeft = l.offsetLeft - 16; } }); } }); }, {rootMargin:'-45% 0px -50% 0px'}); cats.forEach(function(c){ io.observe(c); }); }
})();
</script>'''
    page('faq.html', 'FAQ · SafeBAE', 'Get answers to your most pressing questions on topics like consent, boundaries, and relationships from SafeBAE.',
         body, active='resources', body_class='fq', head_extra=f'<style>{SP_CSS}{FQ_CSS}</style>', scripts=js)


# =====================================================================
# POSTERS
# =====================================================================
POSTERS = [  # (image, title, topic, individual download or None, format, alt)
  ('8x8-what-not-to-say-poster-pdf', 'What to say vs. what not to say', 'support', WPU + '2025/08/8x8-what-not-to-say-poster.pdf', 'PDF', 'Poster: what to say to a friend who shares they have been assaulted, and what not to say'),
  ('healing-from-trauma-3', 'Healing from a traumatic relationship', 'support', WPU + '2025/09/Healing-From-Trauma_page-0001-3.jpg', 'JPG', 'Poster: Healing from a traumatic relationship, with twelve self-care practices'),
  ('everyone-can-do-something-1', 'No one can do everything, but everyone can do something', 'support', WPU + '2025/09/Everyone-Can-Do-Something_page-0001-1-scaled.jpg', 'JPG', 'Poster: No one can do everything but everyone can do something. End rape culture.'),
  ('poster-ending-online-harassment', 'Ending online harassment is everyone’s responsibility', 'online', None, 'PNG', 'Poster: Ending online harassment is everyone’s responsibility'),
  ('no-means-no-pdf', 'No means no, but so does…', 'consent', WPU + '2024/11/no-means-no.pdf', 'PDF', 'Poster: No means no, but so does silence, “maybe later,” “I’m not sure,” being drunk, changing their mind, a power imbalance, seeming hesitant, and pressuring them. Always get enthusiastic consent.'),
  ('poster-consent-is-bae', 'Consent is BAE', 'consent', WPU + '2025/08/8x8-consent-is-bae.png', 'PNG', 'Poster: Consent is BAE, before anything else. Mutual, ongoing, sober, enthusiastic, voluntary, revocable.'),
  ('baby-consent-print-materials-1', 'Early ways to teach consent', 'consent', WPU + '2025/08/baby-consent-print-materials-1_page-0001-scaled.jpg', 'JPG', 'Poster: early ways to teach consent. Smile, high five, fist bump, handshake, hug.'),
  ('poster-sober', 'If you’ve had too much to drink…', 'consent', None, 'PDF', 'Poster: If you’ve had too much to drink, you know not to drive, but did you know the same is true for hooking up?'),
  ('poster-arousal-not-consent', 'Arousal ≠ consent', 'consent', None, 'PDF', 'Poster: Arousal does not equal consent'),
  ('poster-erection-not-consent', 'Erection ≠ consent', 'consent', None, 'PDF', 'Poster: Erection does not equal consent'),
  ('relationships-4', 'What goes into a healthy relationship?', 'relationships', WPU + '2025/09/relationships-4_page-0001-scaled.jpg', 'JPG', 'Poster: What goes into a healthy relationship? Equality at the center, surrounded by trust, respect, honesty, healthy boundaries, good communication and more.'),
  ('relationships-vs-poster-1', 'Healthy vs. unhealthy relationships', 'relationships', WPU + '2025/09/relationships-vs-Poster-1_page-0001-scaled.jpg', 'JPG', 'Poster comparing healthy and unhealthy relationship behaviors'),
  ('knowb4unude-1', 'Have you ever gotten a nude you didn’t want?', 'online', WPU + '2025/09/KnowB4Unude-1.jpg', 'JPG', 'Poster: Have you ever gotten a nude you didn’t want? #knowB4Unude'),
  ('nudes-poster-2', 'Do you trust the person you send nudes to?', 'online', WPU + '2025/08/nudes-poster-2_page-0001.jpg', 'JPG', 'Poster: Do you trust the person you send nudes to? #knowB4Unude'),
  ('nudes-poster-3', 'If a teacher catches you sharing nudes…', 'online', WPU + '2025/08/Nudes-poster-3_page-0001.jpg', 'JPG', 'Poster: Did you know that if a teacher catches you sharing nudes, they’re required to tell the police? #knowB4Unude'),
  ('poster-do-you-knowb4unude', 'Do you #knowB4Unude?', 'online', WPU + '2023/11/do-you-knowB4Unude-4.jpg', 'JPG', 'Poster: Do you #knowB4Unude? A peach emoji in a photo frame.'),
  ('all-statistics', 'Causes of rape', 'facts', WPU + '2026/07/ALL-statistics.png', 'PNG', 'Pie chart poster: causes of rape. Being under the influence, clothes, walking alone, flirty behavior and hooking up all take up none of the chart. The rapist takes up all of it.'),
  ('poster-3-false-reports', 'How often do false reports for rape occur?', 'facts', None, 'PDF', 'Poster: How often do false reports for rape occur? 3% of the time. Support survivors.'),
  ('poster-never-report', 'Half of high school victims never report', 'facts', None, 'PDF', 'Poster: 1/2 of high school victims never report. Journal of Adolescent Health.'),
  ('poster-60-percent', '60% of high school boys…', 'facts', None, 'PDF', 'Poster: 60% of high school boys find it acceptable to force sex on a girl in some circumstances. Journal of Adolescent Health.'),
  ('poster-81-percent', '81% have experienced sexual harassment', 'facts', None, 'PDF', 'Poster: By the time students are done with secondary school, 81% have experienced some sort of sexual harassment (Gruber & Fineran). Help us change that.'),
  ('poster-male-survivors', 'Guys are more likely to be assaulted than falsely accused', 'facts', None, 'PDF', 'Poster: Statistically, guys are more likely to be sexually assaulted than they are to be falsely accused of rape.'),
]
PO_TOPICS = [('all', 'All posters'), ('consent', 'Consent'), ('relationships', 'Relationships'), ('online', 'Nudes & online'), ('support', 'Support & action'), ('facts', 'Facts & figures')]
PO_LABEL = dict(PO_TOPICS)
PO_PAIR = ['red-flags', 'knowb4unude', 'male-survivors']

PO_CSS = '''
/* hero: three posters pinned up, each shown whole */
.po-hero .wrap{padding-block:clamp(40px,5vw,72px) clamp(44px,5.4vw,76px)}
.po-hero__txt{align-self:center}
.po-hero h1{font-size:clamp(2.3rem,4.6vw,4.3rem)}
.po-fan{position:relative; min-height:clamp(300px,31vw,430px)}
.po-fan figure{position:absolute; top:50%; margin:0; height:62%; aspect-ratio:3/4; background:#fff; padding:7px; border-radius:6px; box-shadow:0 26px 50px -22px rgba(0,0,0,.7); transform:translateY(-50%) rotate(var(--r)); transition:transform .5s cubic-bezier(.2,.8,.2,1)}
.po-fan figure img{width:100%; height:100%; object-fit:cover; border-radius:3px}
.po-fan figure::before{content:""; position:absolute; top:-11px; left:50%; width:74px; height:22px; margin-left:-37px; background:rgba(21,255,200,.82); transform:rotate(-3deg); z-index:2}
.po-fan figure:nth-child(1){left:0; --r:-9deg; margin-top:3%}
.po-fan figure:nth-child(2){left:50%; translate:-50% 0; --r:-1deg; height:78%; margin-top:-2%; z-index:2}
.po-fan figure:nth-child(3){right:0; --r:8deg; margin-top:3%; z-index:1}
.po-fan:hover figure:nth-child(1){--r:-13deg} .po-fan:hover figure:nth-child(3){--r:12deg}
.po-fan .sticker{position:absolute; right:3%; bottom:7%; z-index:3; font-size:1.05rem}
@media (max-width:900px){.po-fan{min-height:0; height:clamp(250px,66vw,400px); width:100%; max-width:520px}}

/* the wall: every poster whole, at its own proportions, the same height along a row */
.po-tools{display:grid; gap:12px; margin-bottom:var(--head-gap)}
.po-tools p{margin:0; font-size:.95rem; font-weight:600; color:var(--ink-soft)}
.po-wall{--po-h:300px; display:flex; flex-wrap:wrap; column-gap:var(--gap); align-items:stretch; margin-bottom:calc(var(--po-row) * -1); --po-row:clamp(28px,3.2vw,44px)}
.po-card{flex:var(--ar) 1 calc(var(--ar) * var(--po-h)); min-width:0; display:flex; flex-direction:column; margin-bottom:var(--po-row)}
.po-card[hidden]{display:none}
.po-br{flex:0 0 100%; height:0}
.po-card__img{display:block; width:100%; aspect-ratio:var(--ar); border:0; padding:0; background:#fff; border-radius:6px; overflow:hidden; cursor:zoom-in; box-shadow:0 0 0 1px rgba(29,65,78,.1), 0 22px 34px -22px rgba(29,65,78,.6); transition:transform .35s var(--ease), box-shadow .35s var(--ease)}
.po-card__img img{width:100%; height:100%; object-fit:cover; display:block}
.po-card__img:hover{transform:translateY(-5px) rotate(-.7deg); box-shadow:0 0 0 1px rgba(29,65,78,.1), 0 30px 44px -22px rgba(29,65,78,.65)}
.po-card__img:focus-visible{outline-offset:4px}
.po-card__body{display:flex; flex-direction:column; flex:1; padding-top:14px; min-width:0; container-type:inline-size}
.po-card__topic{font-family:var(--mono); font-size:.72rem; letter-spacing:.1em; text-transform:uppercase; font-weight:600; color:var(--logo-teal)}
.po-card__body b{font-family:var(--display); font-stretch:106%; font-weight:800; font-size:1.12rem; line-height:1.2; margin-top:5px; text-wrap:balance}
.po-card__foot{margin-top:auto; padding-top:8px}
.po-dl{display:inline-flex; align-items:center; gap:.45em; min-height:34px; font-weight:800; font-size:.92rem; color:var(--logo-teal); text-decoration:none}
.po-dl span{white-space:nowrap; text-decoration:underline; text-decoration-color:var(--mint); text-decoration-thickness:3px; text-underline-offset:4px}
.po-dl i{font-style:normal; transition:transform .2s var(--ease)}
.po-dl:hover i{transform:translateY(3px)}
.po-dl--zip{color:var(--ink-soft)} .po-dl--zip span{text-decoration-color:var(--gray)}
@container (max-width:128px){ .po-dl span{white-space:normal} }
@media (pointer:coarse){ .po-dl{min-height:44px} }
/* the full set closes the wall and takes whatever is left of the last row */
.po-zip{flex:999 1 280px; min-width:0; display:flex; container-type:inline-size; margin-bottom:var(--po-row)}
.po-zip__in{flex:1; display:flex; flex-direction:column; justify-content:space-between; gap:20px; padding:var(--pad-card); border-radius:var(--r-xl); background:var(--slate) var(--grain); color:#fff}
.po-zip .eyebrow{color:var(--mint); margin-bottom:.7rem}
.po-zip b{display:block; font-family:var(--display); font-weight:900; font-stretch:115%; font-size:clamp(1.4rem,8cqi,2.4rem); line-height:1; text-wrap:balance}
.po-zip p{margin:12px 0 0; color:rgba(255,255,255,.9); font-size:.97rem; line-height:1.5}
.po-zip .btn{align-self:flex-start}
@container (min-width:760px){ .po-zip__in{flex-direction:row; align-items:center} .po-zip__in > div{max-width:64ch} .po-zip .btn{align-self:center; flex:none} .po-zip b{font-size:2.3rem} }
@container (max-width:250px){ .po-zip__in{padding:16px} .po-zip b{font-size:1.25rem; line-height:1.1} .po-zip p:not(.eyebrow){display:none} .po-zip .btn{align-self:stretch; padding-inline:.5em; font-size:.92rem} }
@media (max-width:900px){.po-wall{--po-h:230px} .po-dl{font-size:.88rem} .po-dl span{white-space:nowrap} .po-dl i{display:none}}
@media (max-width:560px){.po-wall{--po-h:170px; column-gap:14px} .po-card__body b{font-size:1.02rem} .po-tools{margin-bottom:22px}}

/* Choking Hazard posters: the tape is mint and white on purpose */
.po-ch{overflow:hidden; padding-top:14px}
.po-tape{display:flex; gap:0; white-space:nowrap; margin-bottom:var(--band); background:repeating-linear-gradient(-45deg, var(--slate) 0 16px, var(--mint) 16px 32px); padding:7px 0; transform:rotate(-1.2deg) scale(1.03); transform-origin:center}
.po-tape span{flex:none; font-family:var(--display); font-weight:900; font-stretch:118%; text-transform:uppercase; font-size:.95rem; letter-spacing:.04em; color:var(--slate); background:#fff; padding:5px 18px; margin-right:40px}
.po-ch__grid{align-items:center}
.po-ch__label{padding:10px 26px 10px 10px}
.po-ch__txt .lede{color:rgba(255,255,255,.92)}
.po-ch__txt h2{color:#fff}
@media (max-width:900px){.po-ch__label{max-width:340px; padding-right:10px}}

/* pair a poster with a film */
.po-pair .frel__grid{margin-bottom:var(--gap)}
'''


def film_cards(ids):
    """The shared film card (films_common .fcard), so this row matches "Teach these next" on the film pages."""
    cards = []
    for i in ids:
        it = lib_item(i)
        cards.append(f'<a class="fcard" href="{it["href"]}"><span class="fcard__media">{img(it["thumb"], "")}</span><span class="fcard__body">'
                     f'<span class="fcard__sub">{esc(it["sub"])}</span><b class="fcard__t">{esc(it["title"])}</b><span class="fcard__d">{esc(it["desc"])}</span>'
                     f'<span class="fcard__go">Watch and teach<i aria-hidden="true">&rarr;</i></span></span></a>')
    return f'<div class="frel__grid frel__grid--n{len(cards)}">{"".join(cards)}</div>'


def posters():
    counts = {k: (len(POSTERS) if k == 'all' else sum(1 for p in POSTERS if p[2] == k)) for k, _ in PO_TOPICS}
    chips_ = ''.join(f'<button type="button" data-t="{k}" aria-pressed="{str(k == "all").lower()}">{esc(l)}<small>{counts[k]}</small></button>' for k, l in PO_TOPICS)
    cards = []
    for n, t, topic, dl, fmt, alt in POSTERS:
        m = MANIFEST.get(n)
        if not m:
            from PIL import Image
            im = Image.open(f'{SITE}/assets/img/{n}.webp'); m = {'w': im.width, 'h': im.height}
        ar = round(m['w'] / m['h'], 4)
        foot = (f'<a class="po-dl" href="{esc(dl)}" target="_blank" rel="noopener"><span>Download ({fmt})</span><i aria-hidden="true">&darr;</i></a>' if dl
                else f'<a class="po-dl po-dl--zip" href="{esc(POSTERS_ZIP)}" target="_blank" rel="noopener"><span>In the full set (.zip)</span><i aria-hidden="true">&darr;</i></a>')
        cards.append(f'<article class="po-card reveal" data-t="{topic}" data-ar="{ar}" style="--ar:{ar}"><button type="button" class="po-card__img" data-src="{imgsrc(n)}" data-cap="{esc(t)}" aria-label="Enlarge poster: {esc(t)}">{img(n, alt)}</button>'
                     f'<div class="po-card__body"><span class="po-card__topic">{esc(PO_LABEL[topic])}</span><b>{esc(t)}</b><div class="po-card__foot">{foot}</div></div></article>')
    fan = ''.join(f'<figure>{img(n, "", loading="eager")}</figure>' for n in ['relationships-vs-poster-1', 'baby-consent-print-materials-1', 'everyone-can-do-something-1'])
    body = f'''
<section class="sp-hero sp-hero--dark po-hero">
  <span class="wm-daisy" aria-hidden="true"></span>
  <div class="wrap sp-g">
    <div class="sp-c7 rise sp-hero__txt po-hero__txt">
      {crumbs(('Home', 'index.html'), ('Resources', 'resources.html'), ('Posters', None))}
      <p class="eyebrow">Free to print &amp; share</p>
      <h1>Shareable prevention <span class="mk">posters</span></h1>
      <p class="lede">Our posters are easy-to-share educational materials that can help reinforce key messages around consent, healthy relationships, boundaries, and student support. They work well in classrooms, counseling offices, hallways, wellness centers, and student spaces.</p>
      <div class="btns">{btn('Download all posters (.zip)', POSTERS_ZIP, 'mint')}{btn('Teaching guides', 'library.html#guides', 'ghost', arrow=True)}</div>
    </div>
    <div class="sp-c5 sp-hero__media po-fan" aria-hidden="true">{fan}<span class="sticker sticker--r">Free</span></div>
  </div>
</section>
<section class="band band--mist" id="gallery">
  <div class="wrap">
    <div class="po-tools"><div class="sp-chips" role="group" aria-label="Filter posters by topic" id="po-filter">{chips_}</div><p>Tap a poster to see it full size.</p></div>
    <div class="po-wall" id="po-grid">{''.join(cards)}<article class="po-zip" data-t="all"><div class="po-zip__in"><div><p class="eyebrow">The full set</p><b>21 posters in one free download</b><p>Every poster above as PDFs and images in one .zip. No Means No is a separate PDF, linked on its card.</p></div>{btn('Download the .zip', POSTERS_ZIP, 'mint')}</div></article></div>
  </div>
</section>
<section class="band band--deep po-ch" id="choking-hazard-posters">
  <div class="po-tape" aria-hidden="true"><span>There’s no safe way to choke someone</span><span>There’s no safe way to choke someone</span><span>There’s no safe way to choke someone</span><span>There’s no safe way to choke someone</span><span>There’s no safe way to choke someone</span></div>
  <div class="wrap sp-g po-ch__grid">
    <div class="sp-c5 po-ch__label">{hz_label("hz--tilt")}</div>
    <div class="sp-c7 po-ch__txt">
      <p class="eyebrow">Free from Choking Hazard</p>
      <h2>Warning posters on sexual strangulation</h2>
      <p class="lede">Choking Hazard is SafeBAE’s campaign on sexual strangulation, which young people call “choking”. Its free warning posters and warning sticker are available to download from the campaign site.</p>
      <div class="btns">{btn('Download the warning posters', 'https://chokinghazard.org/resources/#downloads', 'mint')}{btn('About the campaign', 'choking-hazard.html', 'ghost', arrow=True)}</div>
    </div>
  </div>
</section>
<section class="band band--paper film po-pair">
  <div class="wrap">
    <div class="section-head"><div><h2>Pair a poster with a film and guide</h2></div><div class="section-head__act">{btn('The full library', 'library.html', 'slate', arrow=True)}</div></div>
    {film_cards(PO_PAIR)}
    {help_strip()}
  </div>
</section>
{give_band()}
'''
    js = r'''<script>
(function(){
  var f = document.getElementById('po-filter'), wall = document.getElementById('po-grid'); if(!f || !wall) return;
  var bs = f.querySelectorAll('button'), cards = [].slice.call(wall.querySelectorAll('.po-card')), zip = wall.querySelector('.po-zip');
  /* Pack the visible posters into rows. Along a row every poster has the same height, so captions and download links line up;
     the "full set" card takes what is left of the last row, so no row ends with a lone poster. */
  function layout(){
    var W = wall.clientWidth; if(!W) return;
    var g = parseFloat(getComputedStyle(wall).columnGap) || 0;
    /* target height: a row of two, three or four square posters, by width */
    var per = W < 520 ? 2 : W < 900 ? 3 : 4, sq = (W - g * (per - 1)) / per;
    var P = W < 520 ? [sq, 148, .7, 1.8, 124] : W < 900 ? [sq, 260, .72, 1.6, 138] : [sq * 1.07, W < 1040 ? 280 : 300, .72, 1.34, 140];
    var H = P[0], minZ = P[1], lo = P[2] * H, hi = P[3] * H, minW = P[4];
    var vis = cards.filter(function(c){ return !c.hidden; }), n = vis.length, ar = vis.map(function(c){ return +c.getAttribute('data-ar') || 1; });
    var sum = [0]; ar.forEach(function(a, i){ sum[i + 1] = sum[i] + a; });
    function rowH(i, j){ return (W - g * (j - i - 1)) / (sum[j] - sum[i]); }
    function dev(h, i, j){ var d = (h - H) / H, m = 9; if(d > 0) d *= 1.7; for(var q = i; q < j; q++) m = Math.min(m, ar[q]); return d * d + (h < lo || h > hi ? 4 : 0) + (m * h < minW ? 4 : 0); }
    function lastMax(i){ return (W - g * (n - i) - minZ) / (sum[n] - sum[i]); }
    var best = [], cut = [];
    for(var i = n; i >= 0; i--){ cut[i] = -1;
      if(i === n) best[i] = .03; else { var hm = lastMax(i); best[i] = hm < lo ? 1e9 : dev(Math.min(H, hm), i, n); }
      for(var j = i + 1; j <= n; j++){ var c = dev(rowH(i, j), i, j) + best[j]; if(c < best[i]){ best[i] = c; cut[i] = j; } } }
    [].slice.call(wall.querySelectorAll('.po-br')).forEach(function(b){ b.remove(); });
    var k = 0, prevH = 0;
    while(k < n && cut[k] > 0){ var e = cut[k]; for(var q = k; q < e; q++){ vis[q].style.flex = ar[q] + ' 1 0%'; } prevH = rowH(k, e);
      var br = document.createElement('i'); br.className = 'po-br'; br.setAttribute('aria-hidden', 'true'); wall.insertBefore(br, e < n ? vis[e] : zip); k = e; }
    if(k < n){ var hx = lastMax(k), h = Math.min(prevH && prevH <= hx && prevH >= lo ? prevH : H, hx);
      for(var q2 = k; q2 < n; q2++){ vis[q2].style.flex = '0 0 ' + (ar[q2] * h).toFixed(2) + 'px'; } zip.style.flex = '1 1 0%'; zip.style.minHeight = h.toFixed(2) + 'px'; zip.style.alignSelf = 'flex-start'; }
    else { zip.style.flex = '1 1 100%'; zip.style.minHeight = ''; zip.style.alignSelf = ''; }
  }
  bs.forEach(function(b){ b.addEventListener('click', function(){ var t = b.getAttribute('data-t'); bs.forEach(function(x){ x.setAttribute('aria-pressed', String(x === b)); }); cards.forEach(function(c){ c.hidden = !(t === 'all' || c.getAttribute('data-t') === t); }); layout(); }); });
  wall.addEventListener('click', function(e){ var b = e.target.closest('.po-card__img'); if(!b || !window.SB || !SB.openLightbox) return; var vis = cards.filter(function(c){ return !c.hidden; }).map(function(c){ return c.querySelector('.po-card__img'); });
    SB.openLightbox(vis.map(function(x){ return {src:x.getAttribute('data-src'), cap:x.getAttribute('data-cap')}; }), vis.indexOf(b)); });
  layout();
  var raf; function again(){ cancelAnimationFrame(raf); raf = requestAnimationFrame(layout); }
  if('ResizeObserver' in window){ var w0 = wall.clientWidth; new ResizeObserver(function(){ if(wall.clientWidth !== w0){ w0 = wall.clientWidth; again(); } }).observe(wall); } else { window.addEventListener('resize', again); }
})();
</script>'''
    page('posters.html', 'Posters · SafeBAE', 'Download posters on consent, boundaries, and prevention. Free visuals for classrooms, schools, and student spaces.',
         body, active='resources', body_class='po', head_extra=f'<style>{SP_CSS}{HELPLINE_CSS}{FILM_CSS}{PO_CSS}</style>', scripts=js)


# =====================================================================
# BLOG
# =====================================================================
BLOG_LEAD = ('Vibe Check: A tool for perpetrators, from survivors', '2026-05-29', 'https://www.safebae.org/vibe-check-a-tool-for-perpetrators-from-survivors/', 'blog-vibe-check-a-tool-for-perpetrators-from-surv')
BLOG_SECTIONS = [
  ('explainers', 'Media analysis & explainers', [('All explainers', 'https://www.safebae.org/category/cultural-analysis-explainers/')], [
    ('The Real Crisis Behind the Manosphere', '2026-03-17', 'https://www.safebae.org/what-is-the-manosphere-online-misogyny/', 'blog-what-is-the-manosphere-online-misogyny'),
    ('ANTM on Netflix: Consent & Rape Culture', '2026-02-26', 'https://www.safebae.org/antm-on-netflix-sexual-violence-edited-as-entertainment/', 'blog-antm-on-netflix-sexual-violence-edited-as-en'),
    ('How Are Young People Learning About Sex and Consent Online And Why Is It Important?', '2026-01-26', 'https://www.safebae.org/how-are-young-people-learning-about-sex-and-consent-online-and-why-is-it-important/', 'blog-how-are-young-people-learning-about-sex-and'),
    ('Rape Culture, Then And Now: What Have We Learned?', '2025-11-18', 'https://www.safebae.org/rape-culture-then-and-now-what-have-we-learned/', 'blog-rape-culture-then-and-now-what-have-we-learn')]),
  ('policy', 'Policy & legal news', [('All policy & legal news', 'https://www.safebae.org/category/policy-legal-news/')], [
    ('New York Just Passed a Bill to Protect Minors from Unsafe AI Chatbots.', '2026-07-02', 'https://www.safebae.org/new-york-just-passed-a-bill-to-protect-minors-from-unsafe-ai-chatbots/', 'blog-new-york-just-passed-a-bill-to-protect-minor'),
    ('Why Students Walk Out: The Westlake High Protest and the Power of Youth Activism', '2025-05-06', 'https://www.safebae.org/why-students-walk-out-the-westlake-high-protest-and-the-power-of-youth-activism/', 'blog-why-students-walk-out-the-westlake-high-prot'),
    ('Tennessee Bill to Guarantee Teen Rape Kits Fails in Committee', '2025-05-01', 'https://www.safebae.org/tennessee-bill-to-guarantee-teen-rape-kits-fails-in-committee/', 'blog-tennessee-bill-to-guarantee-teen-rape-kits-f'),
    ('Consent Education Wins in Indiana After Students Speak Out', '2025-04-25', 'https://www.safebae.org/consent-education-wins-in-indiana-after-students-speak-out/', 'blog-consent-education-wins-in-indiana-after-stud')]),
  ('culture', 'Culture news & commentary', [('All culture news', 'https://www.safebae.org/category/culture-news-commentary/')], [
    ('Sedona Prince Goes Undrafted in 2025 WNBA Draft After Year of Assault Allegations', '2025-04-15', 'https://www.safebae.org/sedona-prince-goes-undrafted-in-2025-wnba-draft-after-year-of-assault-allegations/', 'blog-sedona-prince-goes-undrafted-in-2025-wnba-dr'),
    ('A Rape Game Was Live on Steam. That Should Tell Us Everything.', '2025-04-11', 'https://www.safebae.org/a-rape-game-was-live-on-steam-that-should-tell-us-everything/', 'blog-a-rape-game-was-live-on-steam-that-should-te'),
    ('What Drake & Josh’s Reunion Teaches Us About Supporting Survivors', '2025-03-26', 'https://www.safebae.org/what-drake-joshs-reunion-teaches-us-about-supporting-survivors/', 'blog-what-drake-joshs-reunion-teaches-us-about-su'),
    ('Jack Wright, Sienna Mae, and the Urgent Need for Consent Education', '2025-01-21', 'https://www.safebae.org/jack-wright-sienna-mae-and-the-urgent-need-for-consent-education/', 'blog-jack-wright-sienna-mae-and-the-urgent-need-f')]),
  ('programs', 'Programs, partnerships & school visits', [('Programs', 'https://www.safebae.org/category/programs/'), ('School visits & trainings', 'https://www.safebae.org/category/school-visits-trainings/')], [
    ('Launching Leaders: How SafeBAE Alumni Took the Healthy Youth Conference Stage', '2025-04-30', 'https://www.safebae.org/launching-leaders-how-safebae-alumni-took-the-healthy-youth-conference-stage/', 'blog-launching-leaders-how-safebae-alumni-took-th'),
    ('SafeBAE Joins HopSkipDrive’s Safety Advisory Board', '2025-04-26', 'https://www.safebae.org/safebae-joins-hopskipdrives-safety-advisory-board/', 'blog-safebae-joins-hopskipdrives-safety-advisory'),
    ('Kicking Off Our Whole-School Approach with Alliance Public Schools in Los Angeles', '2025-04-14', 'https://www.safebae.org/kicking-off-our-whole-school-approach-with-alliance-public-schools-in-los-angeles/', 'blog-kicking-off-our-whole-school-approach-with-a'),
    ('SafeBAE Brings Consent Education to Middle Schoolers at Belmont Day School', '2025-03-10', 'https://www.safebae.org/safebae-brings-consent-education-to-middle-schoolers-at-belmont-day-school/', 'blog-safebae-brings-consent-education-to-middle-s')]),
]
BLOG_TOPICS = [('Title IX', 'https://www.safebae.org/category/title-ix/'), ('Vibe Check', 'https://www.safebae.org/category/vibe-check/'),
               ('Stories', 'https://www.safebae.org/category/blog/stories/'), ('News', 'https://www.safebae.org/category/blog/news/'),
               ('FAQ answers', 'https://www.safebae.org/category/faq/'), ('Every post', 'https://www.safebae.org/category/blog/')]
SUBSTACK_POSTS = [('Vibe Check by SafeBAE', 'A tool for perpetrators, from survivors.', 'https://safebae.substack.com/p/vibe-check'),
                  ('When you Ask AI for Advice, and It Just Agrees with You…', 'A new study shows why that is a problem.', 'https://safebae.substack.com/p/when-you-ask-ai-for-advice-and-it'),
                  ('New York Just Passed a Bill to Protect Minors from Unsafe AI Chatbots.', 'Here is why that matters for consent and accountability.', 'https://safebae.substack.com/p/new-york-just-passed-a-bill-to-protect')]

BL_CSS = '''
/* hero: masthead beside the lead story */
.bl-hero .wrap{padding-block:clamp(40px,5vw,72px) clamp(44px,5.4vw,76px)}
.bl-hero__txt{display:flex; flex-direction:column}
.bl-hero .bl-mast{font-size:clamp(3rem,5.8vw,5.3rem); font-stretch:118%; line-height:.82; letter-spacing:-.03em; margin:0 0 .28em}
.bl-hero .lede{margin:0 0 1.2em}
.bl-warn{display:flex; gap:14px; align-items:center; margin:auto 0 18px; padding:14px 16px; border-radius:14px; background:rgba(255,255,255,.06); border:1px solid var(--line-dark); font-size:.95rem; line-height:1.45; color:var(--aqua)}
.bl-warn b{color:#fff}
.bl-warn button{margin-left:auto; flex:none; font:inherit; font-size:.9rem; font-weight:800; min-height:38px; background:#fff; color:var(--slate); border:0; border-radius:8px; padding:6px 13px; cursor:pointer; transition:background .2s}
.bl-warn button:hover{background:var(--mint)}
@media (pointer:coarse){ .bl-warn button{min-height:44px} }
.bl-lead{position:relative; display:flex; flex-direction:column; text-decoration:none; color:#fff; background:var(--slate-deep); border:1px solid var(--line-dark); border-radius:var(--r-xl); overflow:hidden; box-shadow:0 34px 70px -34px rgba(0,0,0,.75); transition:transform .3s var(--ease), border-color .3s}
.bl-lead:hover{transform:translateY(-5px); border-color:var(--mint)}
.bl-lead__img{display:block; aspect-ratio:2/1; overflow:hidden}
.bl-lead__img img{width:100%; height:100%; object-fit:cover; object-position:50% 0; transform-origin:50% 0; transition:transform .7s var(--ease)}
.bl-lead:hover .bl-lead__img img{transform:scale(1.03)}
.bl-lead__body{flex:1; padding:22px var(--pad-card) var(--pad-card); display:flex; flex-direction:column; gap:10px}
.bl-lead__body small{font-family:var(--mono); font-size:.72rem; letter-spacing:.1em; text-transform:uppercase; color:var(--mint); font-weight:600}
.bl-lead__body b{font-family:var(--display); font-stretch:110%; font-size:clamp(1.5rem,2.6vw,2.2rem); line-height:1.06; text-wrap:balance}
.bl-lead__body > span{color:rgba(255,255,255,.86); font-size:1rem; line-height:1.5}
.bl-lead__go{margin-top:auto; padding-top:6px; display:inline-flex; align-items:center; gap:.5em; color:var(--mint)!important; font-weight:800}
.bl-lead__go i{font-style:normal; transition:transform .2s var(--ease)}
.bl-lead:hover .bl-lead__go i{transform:translate(3px,-3px)}
.bl-lead .sticker{position:absolute; left:18px; top:18px; z-index:1}
@media (max-width:900px){.bl-warn{margin-top:0}}

/* sections of four: image, date, title and link share rows across each card */
.bl-sec .section-head{border-top:4px solid var(--slate); padding-top:18px; align-items:center; margin-bottom:clamp(22px,2.6vw,34px)}
.band--deep.bl-sec .section-head{border-color:var(--mint)}
.bl-sec h2{font-size:clamp(1.7rem,3.2vw,2.7rem)}
.bl-sec .btns{gap:8px; flex-wrap:nowrap}
.bl-posts{display:grid; grid-template-columns:repeat(4,minmax(0,1fr)); gap:var(--gap)}
.bl-post{display:flex; flex-direction:column; text-decoration:none; color:inherit; min-width:0}
.bl-post__img{display:block; aspect-ratio:40/21; border-radius:14px; overflow:hidden; background:var(--slate); box-shadow:0 16px 30px -22px rgba(22,53,64,.7)}
.bl-post__img img{width:100%; height:100%; object-fit:cover; transition:transform .6s var(--ease)}
.bl-post:hover .bl-post__img img{transform:scale(1.04)}
.bl-post time{font-family:var(--mono); font-size:.72rem; letter-spacing:.08em; text-transform:uppercase; color:var(--logo-teal); margin-top:16px; font-weight:600}
.bl-post b{font-family:var(--display); font-stretch:106%; font-weight:800; font-size:1.2rem; line-height:1.2; margin-top:6px; text-wrap:pretty}
.bl-post:hover b{text-decoration:underline; text-decoration-color:var(--mint); text-decoration-thickness:3px; text-underline-offset:3px}
.bl-post__go{margin-top:auto; padding-top:12px; font-size:.9rem; font-weight:700; color:var(--ink-soft)}
.band--deep .bl-post time{color:var(--mint)} .band--deep .bl-post b{color:#fff} .band--deep .bl-post__go{color:rgba(255,255,255,.72)}
.band--deep .bl-post__img{box-shadow:0 0 0 1px var(--line-dark)}
@supports (grid-template-rows:subgrid){ @media (min-width:621px){
  .bl-post{display:grid; grid-template-rows:subgrid; grid-row:span 4; row-gap:0}
  .bl-post__go{margin-top:0; align-self:end}
}}
@media (max-width:1000px){.bl-posts{grid-template-columns:repeat(2,minmax(0,1fr)); row-gap:clamp(26px,3.4vw,36px)}}
@media (max-width:620px){
  .bl-posts{grid-template-columns:minmax(0,1fr); row-gap:0}
  .bl-post{display:grid; grid-template-columns:132px minmax(0,1fr); grid-template-rows:auto auto 1fr; column-gap:14px; padding:14px 0; border-top:1px solid var(--line)}
  .band--deep .bl-post{border-color:var(--line-dark)}
  .bl-post__img{grid-row:1 / span 3; align-self:start; border-radius:10px}
  .bl-post time{margin-top:0}
  .bl-post b{font-size:1.06rem; margin-top:4px}
  .bl-post__go{padding-top:6px; align-self:start}
  .bl-sec .btns{flex-wrap:wrap}
  .bl-sec .section-head__act{flex:1 1 100%!important; min-width:0}
}

/* topics: one row across the full width */
.bl-topics{display:grid; gap:16px}
.bl-topics h2{margin:0; font-size:clamp(1.3rem,2vw,1.6rem)}
.bl-topics__list{display:grid; grid-template-columns:repeat(6,minmax(0,1fr)); gap:10px}
.bl-topics__list a{display:flex; align-items:center; justify-content:space-between; gap:8px; min-height:50px; padding:10px 16px; border-radius:12px; background:#fff; border:1px solid var(--line); text-decoration:none; color:var(--slate); font-family:var(--display); font-stretch:104%; font-weight:800; font-size:1rem; line-height:1.15; transition:transform .2s var(--ease), border-color .2s, background .2s}
.bl-topics__list a i{font-style:normal; color:var(--teal); transition:transform .2s var(--ease)}
.bl-topics__list a:hover{transform:translateY(-3px); border-color:var(--teal)}
.bl-topics__list a:hover i{transform:translate(2px,-2px)}
@media (max-width:1100px){.bl-topics__list{grid-template-columns:repeat(3,minmax(0,1fr))}}
@media (max-width:520px){.bl-topics__list{grid-template-columns:repeat(2,minmax(0,1fr))}}

/* newsletter beside the two ways in */
.bl-sub,.bl-write,.bl-new{border-radius:var(--r-xl); padding:var(--pad-card); min-width:0}
.bl-sub{background:var(--teal); color:#fff; display:flex; flex-direction:column}
.bl-sub h2,.bl-write h2{font-size:clamp(1.7rem,3vw,2.5rem); margin:0 0 .35em}
.bl-sub .eyebrow{color:#fff}
.bl-sub .rows{margin:6px 0 24px; border-color:rgba(255,255,255,.3)}
.bl-sub .row{border-color:rgba(255,255,255,.3); padding:16px 0}
.bl-sub .row:hover{background:rgba(255,255,255,.08)}
.bl-sub .row b{color:#fff; font-size:1.14rem} .bl-sub .row small{color:#fff; font-size:.95rem}
.bl-sub .btns{margin-top:auto}
.bl-side{display:flex; flex-direction:column; gap:var(--gap)}
.bl-write{flex:1; background:var(--aqua); color:var(--slate); display:flex; flex-direction:column; justify-content:center}
.bl-write p{margin:0 0 22px; font-size:1.08rem; line-height:1.55}
.bl-new{display:grid; grid-template-columns:minmax(0,1fr) auto; gap:6px 16px; align-items:center; text-decoration:none; color:var(--slate); background:#fff; border:1px solid var(--line); transition:transform .25s var(--ease), box-shadow .25s var(--ease), border-color .25s}
.bl-new:hover{transform:translateY(-3px); box-shadow:var(--shadow-soft); border-color:var(--teal)}
.bl-new small{grid-column:1/-1; justify-self:start; font-family:var(--mono); font-size:.72rem; letter-spacing:.12em; text-transform:uppercase; font-weight:600; background:var(--slate); color:var(--mint); padding:3px 8px; border-radius:4px}
.bl-new b{font-family:var(--display); font-stretch:105%; font-weight:800; font-size:1.1rem; line-height:1.25; color:var(--logo-teal)}
.bl-new i{font-style:normal; font-weight:800; width:36px; height:36px; border-radius:50%; display:grid; place-items:center; background:var(--aqua); color:var(--logo-teal); transition:background .2s, transform .2s var(--ease)}
.bl-new:hover i{background:var(--mint); transform:translateX(3px)}
'''


def post_card(title, date, link, thumb):
    return (f'<a class="bl-post reveal" href="{esc(link)}" target="_blank" rel="noopener">'
            f'<span class="bl-post__img">{img(thumb, "")}</span>'
            f'<time datetime="{date}">{month(date)}</time><b>{esc(title)}</b>'
            f'<span class="bl-post__go">Read on safebae.org &#8599;</span></a>')


def blog():
    secs = []
    for i, (k, title, links, posts) in enumerate(BLOG_SECTIONS):
        band = 'band--paper' if i % 2 == 0 else 'band--deep'
        lb = ''.join(btn(t, u, 'ghost', 'sm') for t, u in links)
        secs.append(f'''<section class="band {band} band--tight bl-sec" id="{k}"><div class="wrap">
<div class="section-head"><div><h2>{esc(title)}</h2></div><div class="btns section-head__act">{lb}</div></div>
<div class="bl-posts">{''.join(post_card(*p) for p in posts)}</div></div></section>''')
    topics = ''.join(f'<a href="{esc(u)}" target="_blank" rel="noopener">{esc(t)}<i aria-hidden="true">&#8599;</i></a>' for t, u in BLOG_TOPICS)
    subs = ''.join(row(t, d, u) for t, d, u in SUBSTACK_POSTS)
    t, d, u, th = BLOG_LEAD
    body = f'''
<section class="sp-hero sp-hero--dark bl-hero">
  <span class="wm-daisy" aria-hidden="true"></span>
  <div class="wrap sp-g">
    <div class="sp-c5 rise bl-hero__txt">
      {crumbs(('Home', 'index.html'), ('Resources', 'resources.html'), ('Blog', None))}
      <p class="eyebrow">The SafeBAE blog</p>
      <h1 class="bl-mast">News &amp;<br><span class="mk">stories</span></h1>
      <p class="lede">Read stories from survivors, stay updated with SafeBAE, and share what you learn with your friends.</p>
      <p class="bl-warn"><span><b>Content note:</b> material posted may contain sensitive language. Reader discretion is advised.</span><button type="button" data-open-help>Get help</button></p>
      <div class="btns">{btn('Submit an article', JOTFORM, 'mint')}{btn('Get the newsletter', SUBSTACK, 'ghost')}</div>
    </div>
    <a class="sp-c7 bl-lead" href="{esc(u)}" target="_blank" rel="noopener">
      <span class="sticker">Featured</span>
      <span class="bl-lead__img">{img(th, '', loading='eager')}</span>
      <span class="bl-lead__body"><small>Vibe Check &middot; {month(d)}</small><b>{esc(t)}</b><span>A free and anonymous tool for young people who are worried they may have crossed a boundary or caused harm.</span><span class="bl-lead__go">Read on safebae.org<i aria-hidden="true">&#8599;</i></span></span>
    </a>
  </div>
</section>
{''.join(secs)}
<section class="band band--aqua band--tight">
  <div class="wrap bl-topics"><h2>Browse by topic</h2><div class="bl-topics__list">{topics}</div></div>
</section>
<section class="band band--paper">
  <div class="wrap sp-g">
    <div class="sp-c7 bl-sub reveal">
      <p class="eyebrow">SafeBAE on Substack</p>
      <h2>Get the newsletter</h2>
      <div class="rows">{subs}</div>
      <div class="btns">{btn('Subscribe on Substack', SUBSTACK, 'mint')}{btn('Explore Vibe Check', 'vibe-check.html', 'white', arrow=True)}</div>
    </div>
    <div class="sp-c5 bl-side reveal">
      <div class="bl-write">
        <h2>Submit an article</h2>
        <p>If you would like to submit an article of your own to SafeBAE, send it through our submission form.</p>
        <div class="btns">{btn('Submit an article', JOTFORM, 'slate')}{btn('Contact us', 'contact.html', 'ghost', arrow=True)}</div>
      </div>
      <a class="bl-new" href="ai-literacy.html"><small>New</small><b>The SafeBAE AI Literacy Training launches during U.S. Media Literacy Week, October 26–30</b><i aria-hidden="true">&rarr;</i></a>
    </div>
  </div>
</section>
{give_band()}
'''
    page('blog.html', 'Blog · SafeBAE', 'SafeBAE’s blog: media analysis, policy and legal news, culture commentary, and stories from schools on consent and sexual violence prevention.',
         body, active='resources', body_class='bl', head_extra=f'<style>{SP_CSS}{BL_CSS}</style>')


def build():
    myths_facts()
    faq()
    posters()
    blog()


if __name__ == '__main__':
    build()
