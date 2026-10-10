"""Vibe Check landing page (vibe-check.html)."""
import os, random
from urllib.parse import quote
from lib import *
from data import LIB, PODCASTS

WP = 'https://www.safebae.org/wp-content/uploads/'
CYV = 'https://checkyourvibe.org/'
GUIDE_PDF = WP + '2026/03/Check-Their-Vibe-A-Guide-to-Vibe-Check.pdf'


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

SHATTUCK_NOTE = 'https://substack.com/@dominickmenshealth/note/c-255823866'

GUIDE_TABS = [
  ('refer', 'How to refer', '''<ol class="vcp-gsteps">
<li><b>Pick the right moment, not the charged one.</b><span>Wait until things have cooled down. Good windows: a car ride, a casual one-on-one moment, a follow-up conversation after things have settled.</span></li>
<li><b>Lead with curiosity, not direction.</b><span>If it sounds like a punishment or an assignment, they won’t engage honestly, even if they do open it. Offer it as something genuinely useful, not something you’re making them do.</span></li>
<li><b>Make the privacy real.</b><span>Send them the link and step away. Don’t ask to see what they wrote or what path they took. Make it clear they can stop at any point.</span></li>
<li><b>Tell them what it actually is.</b><span>Young people are suspicious of anything that looks like a trap or feels fake. Being upfront about what the tool is, and isn’t, helps a lot.</span></li>
<li><b>Give them genuine space, and keep the door open.</b><span>Let them know you’re available to talk, but take the pressure off.</span></li>
</ol>
<p class="vcp-gnote">The most common mistake is introducing a tool like this in a moment of frustration. The perfect time is before anything has happened at all, as part of a talk about dating or sex.</p>'''),
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


def _uri(svg):
    return 'url("data:image/svg+xml,' + quote(svg, safe="/:=' ") + '")'


def checks(color, sw=3.4, seed=11):
    """The scattered hand-drawn ticks from Vibe Check's own artwork, as a repeating tile."""
    rnd = random.Random(seed)
    w, h, cols, rows = 960, 600, 6, 4
    cells = [(c, r) for r in range(rows) for c in range(cols)]
    rnd.shuffle(cells)
    marks = []
    for c, r in cells[:19]:
        x = (c + .22 + .56 * rnd.random()) * w / cols
        y = (r + .22 + .56 * rnd.random()) * h / rows
        marks.append(f"<path transform='translate({x:.0f} {y:.0f}) rotate({rnd.uniform(-12, 16):.0f}) scale({rnd.uniform(.85, 1.3):.2f})' d='M-9 1L-3 9L12 -12'/>")
    return _uri(f"<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 {w} {h}'><g fill='none' stroke='{color}' stroke-width='{sw}' stroke-linecap='round' stroke-linejoin='round'>{''.join(marks)}</g></svg>")


TICK = """url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 24 24'%3E%3Cpath d='M5 12.5l4.5 4.5L19 7.5' fill='none' stroke='%231d414e' stroke-width='3.2' stroke-linecap='round' stroke-linejoin='round'/%3E%3C/svg%3E")"""

VC_CSS = '''
body.vcp{--vcp-ph:#0b1f25}
#how,#demo,#press,#adults{scroll-margin-top:76px}
/* ---------- hero: Vibe Check's own lockup (serif italic "vibe" over heavy "check") and its scattered ticks ---------- */
.vcp-hero{background:var(--teal); color:#fff; position:relative; overflow:hidden}
.vcp-checks{position:absolute; inset:0; z-index:0; background:__CHECKS_AQUA__ 0 0/960px 600px; opacity:.5; -webkit-mask-image:linear-gradient(100deg, rgba(0,0,0,.42) 0 44%, #000 62%); mask-image:linear-gradient(100deg, rgba(0,0,0,.42) 0 44%, #000 62%); pointer-events:none; animation:vcp-fade 1.4s .1s var(--ease) both}
@keyframes vcp-fade{from{opacity:0}}
.vcp-hero .wrap{position:relative; z-index:2; display:grid; grid-template-columns:minmax(0,1.22fr) minmax(0,.78fr); gap:clamp(24px,4vw,56px); align-items:center; padding-block:clamp(40px,5vw,72px) clamp(40px,4.6vw,66px)}
.vcp-hero .wrap > *{min-width:0}
.vcp-hero .crumbs, .vcp-hero .crumbs a{color:#fff}
.vcp-hero .crumbs a:hover{color:var(--mint)}
.vcp-mark{display:flex; align-items:center; gap:12px; font-family:var(--mono); font-weight:600; font-size:.78rem; letter-spacing:.14em; text-transform:uppercase; color:#fff; margin-bottom:6px}
.vcp-mark .daisy{width:34px; height:34px; color:var(--mint)}
.vcp-lockup{margin:0 0 .2em; font-size:clamp(5rem,10vw,9.2rem); line-height:.8; text-transform:none; letter-spacing:0; font-weight:400}
.vcp-lockup span{display:block}
.vcp-lockup__v{position:relative; z-index:1; font-family:"Playfair Display",Georgia,"Times New Roman",serif; font-style:italic; font-weight:500; font-stretch:100%; font-size:1.16em; line-height:.92; letter-spacing:-.02em; color:var(--aqua); padding-left:.02em}
.vcp-hero .vcp-lockup__c{font-family:var(--display); font-weight:900; font-stretch:100%; letter-spacing:-.06em; line-height:.84; color:var(--mint); background:none; padding:0; margin:-.3em 0 0 .98em}
.vcp-tag{display:inline-block; font-family:var(--display); font-weight:900; font-stretch:115%; text-transform:uppercase; font-size:clamp(1rem,1.7vw,1.35rem); background:var(--slate); color:#fff; padding:.5em .8em .42em; border-radius:6px; transform:rotate(-1.5deg); margin:0 0 22px; box-shadow:4px 4px 0 var(--mint)}
.vcp-hero .lede{color:#fff; max-width:none}
.vcp-hero .btns{margin-top:4px; gap:12px 16px}
.vcp-hero__guide{display:inline-flex; align-items:center; min-height:48px; padding:0 6px; font-family:var(--display); font-weight:800; font-stretch:108%; color:#fff; text-decoration:underline; text-decoration-color:var(--mint); text-decoration-thickness:3px; text-underline-offset:6px}
.vcp-hero__guide:hover{color:var(--mint)}
.vcp-privacy{display:flex; flex-wrap:wrap; gap:10px 24px; margin-top:28px; padding-top:20px; border-top:1px solid rgba(255,255,255,.28)}
.vcp-privacy span{display:inline-flex; align-items:center; gap:9px; font-weight:700; font-size:.98rem}
.vcp-privacy span::before{content:""; width:22px; height:22px; border-radius:50%; background:var(--mint) __TICK__ center/14px no-repeat; flex:none}
.vcp-stage{position:relative; min-height:580px; display:grid; place-items:center}
.vcp-phone{position:relative; width:min(310px,72vw); aspect-ratio:390/800; border-radius:46px; border:11px solid var(--vcp-ph); background:var(--vcp-ph); box-shadow:0 60px 100px -40px rgba(0,0,0,.65), 0 0 0 2px rgba(255,255,255,.1); overflow:hidden; transform:rotate(-3deg); z-index:2}
.vcp-phone img{width:100%; height:100%; object-fit:cover; object-position:top}
.vcp-bub{position:absolute; z-index:3; background:#fff; color:var(--slate); font-family:var(--display); font-weight:800; font-stretch:106%; font-size:clamp(.92rem,1.3vw,1.08rem); padding:12px 16px; border-radius:18px; box-shadow:0 18px 30px -16px rgba(0,0,0,.5); white-space:nowrap; opacity:0; transform:translateY(10px) scale(.96); transition:opacity .5s, transform .5s cubic-bezier(.2,.8,.2,1)}
.vcp-bub.on{opacity:1; transform:none}
.vcp-bub::after{content:""; position:absolute; bottom:-7px; width:16px; height:16px; background:inherit; transform:rotate(45deg); border-radius:3px}
.vcp-bub--l::after{right:22px} .vcp-bub--r::after{left:22px}
.vcp-bub:nth-child(odd){background:var(--aqua)}
.vcp-stage .sticker{position:absolute; z-index:4}
@media (max-width:960px){ .vcp-hero .wrap{grid-template-columns:1fr} .vcp-stage{min-height:0; padding-block:30px 10px} .vcp-phone{width:min(270px,64vw)} .vcp-checks{-webkit-mask-image:none; mask-image:none; opacity:.3} }
@media (max-width:520px){ .vcp-bub{font-size:.875rem; padding:9px 12px} .vcp-privacy{gap:10px 18px} .vcp-privacy span{font-size:.92rem} .vcp-phone{width:min(240px,62vw)} .vcp-stage{padding-block:24px 0} .vcp-hero .vcp-lockup__c{margin-left:.7em} .vcp-hero .btns .btn{flex:1 1 auto} }

/* ---------- why: heading and text beside the two cards (AI | Vibe Check), stacked with the "vs" between ---------- */
.vcp-why{display:grid; grid-template-columns:minmax(0,6fr) minmax(0,6fr); gap:var(--gap) clamp(28px,4vw,56px); align-items:center}
.vcp-why > *{min-width:0}
.vcp-why h2{font-size:clamp(1.9rem,2.9vw,2.6rem); line-height:1.06; margin:0 0 .55em}
.vcp-why__txt p{color:rgba(255,255,255,.88); margin:0; font-size:var(--fs-lede); line-height:1.55; font-weight:500}
.vcp-vs{position:relative; display:grid; grid-template-columns:minmax(0,1fr); gap:14px}
.vcp-vs > div{container-type:inline-size; border-radius:var(--r-xl); padding:clamp(20px,2.2vw,28px) var(--pad-card); display:flex; flex-direction:column; min-width:0}
.vcp-vs small{display:block; font-family:var(--mono); font-size:.74rem; letter-spacing:.12em; text-transform:uppercase; font-weight:600; margin-bottom:10px}
.vcp-vs b{display:block; font-family:var(--display); font-weight:800; font-stretch:108%; font-size:clamp(1.2rem,4.2cqi,1.6rem); line-height:1.22}
.vcp-vs__ai{background:rgba(255,255,255,.05); border:1.5px dashed rgba(209,254,255,.4); color:rgba(255,255,255,.88)}
.vcp-vs__ai small{color:var(--aqua)}
.vcp-vs__vc{background:var(--mint); color:var(--slate)}
.vcp-vs__foot{margin-top:auto; padding-top:18px; display:flex; flex-wrap:wrap; align-items:center; justify-content:space-between; gap:14px 20px}
.vcp-vs__foot .btn{box-shadow:0 4px 0 rgba(0,0,0,.18)}
.vcp-vs__vc .chip{background:var(--slate); color:#fff}
.vcp-vs__badge{position:absolute; right:clamp(28px,4vw,56px); top:50%; translate:0 -50%; width:52px; height:52px; border-radius:50%; background:var(--slate); border:3px solid var(--mint); color:var(--mint); display:grid; place-items:center; font-family:var(--display); font-weight:900; font-stretch:115%; font-size:.95rem; text-transform:uppercase; z-index:2; box-shadow:0 10px 24px -8px rgba(0,0,0,.5)}
.vcp-vs__links{margin-top:14px; display:grid}
.vcp-vs__links a{display:grid; grid-template-columns:minmax(0,1fr) auto; gap:14px; align-items:center; min-height:48px; padding:8px 0; border-top:1px solid var(--line-dark); text-decoration:none; color:#fff!important; font-weight:600; font-size:.98rem; line-height:1.4}
.vcp-vs__links a em{font-style:normal; font-family:var(--mono); font-size:.7rem; letter-spacing:.12em; text-transform:uppercase; font-weight:600; background:var(--mint); color:var(--slate); padding:3px 7px; border-radius:4px; margin-right:.6em; vertical-align:.1em}
.vcp-vs__links a i{font-style:normal; color:var(--mint); font-weight:800; transition:transform .2s var(--ease)}
.vcp-vs__links a:hover span{text-decoration:underline; text-decoration-color:var(--mint); text-decoration-thickness:2px; text-underline-offset:4px}
.vcp-vs__links a:hover i{transform:translateX(4px)}
@media (max-width:960px){ .vcp-why{grid-template-columns:minmax(0,1fr)} .vcp-why__txt p{max-width:none} }

/* ---------- how it works ---------- */
.vcp-how{display:grid; grid-template-columns:minmax(0,1.1fr) minmax(0,.9fr); gap:clamp(28px,5vw,72px); align-items:center}
.vcp-steps{list-style:none; margin:0; padding:0; counter-reset:s; border-top:1px solid var(--line)}
.vcp-steps li{margin:0; border-bottom:1px solid var(--line)}
.vcp-steps button{all:unset; box-sizing:border-box; width:100%; cursor:pointer; display:grid; grid-template-columns:54px minmax(0,1fr) 26px; gap:0 14px; padding:14px 0; position:relative; align-items:start}
.vcp-steps button:focus-visible{outline:3px solid var(--teal); outline-offset:2px; border-radius:6px}
.vcp-steps .n{grid-row:1/3; font-family:var(--display); font-weight:900; font-stretch:125%; font-size:1.9rem; line-height:1; color:rgba(29,65,78,.28); transition:color .3s}
.vcp-steps .t{font-family:var(--display); font-weight:800; font-stretch:108%; font-size:1.2rem; line-height:1.25; color:var(--slate); padding-top:4px}
.vcp-steps .d{grid-column:2; display:block; max-height:0; overflow:hidden; color:var(--ink-soft); font-size:.98rem; line-height:1.5; transition:max-height .45s ease, margin .3s; margin-top:0}
.vcp-steps .bar{position:absolute; left:0; bottom:-1px; height:3px; width:0; background:var(--teal)}
/* steps already passed get a tick, the way the tool marks its own progress */
.vcp-steps .ok{grid-column:3; grid-row:1; align-self:center; width:24px; height:24px; margin-top:4px; border-radius:50%; background:var(--mint) __TICK__ center/14px no-repeat; transform:scale(0); transition:transform .35s var(--ease)}
.vcp-steps li.done .ok{transform:none}
.vcp-steps li.done .n{color:var(--teal)}
.vcp-steps li.on .n{color:var(--teal)}
.vcp-steps li.on .d{max-height:170px; margin-top:6px}
.vcp-steps li:hover .n{color:var(--teal)}
.vcp-steps li:hover .t{color:var(--logo-teal)}
.vcp-howstage{position:relative; display:grid; place-items:center; padding:24px 0}
.vcp-howstage::before{content:""; position:absolute; inset:6% 4%; background:var(--aqua); border-radius:40px; transform:rotate(3deg)}
.vcp-howphone{position:relative; width:min(296px,74vw); aspect-ratio:390/800; border-radius:46px; border:11px solid var(--vcp-ph); background:var(--vcp-ph); overflow:hidden; box-shadow:0 50px 80px -36px rgba(22,53,64,.7)}
.vcp-howphone img{position:absolute; inset:0; width:100%; height:100%; object-fit:cover; object-position:top; opacity:0; transform:scale(1.03); transition:opacity .5s, transform .6s}
.vcp-howphone img.on{opacity:1; transform:none}
.vcp-howcap{position:absolute; left:50%; bottom:6px; transform:translateX(-50%); background:var(--slate); color:#fff; font-family:var(--mono); font-size:.74rem; letter-spacing:.1em; text-transform:uppercase; padding:7px 13px; border-radius:999px; white-space:nowrap; z-index:2}
.vcp-tools{display:flex; flex-wrap:wrap; gap:10px; align-items:center; margin-top:26px; padding:16px 18px; border-radius:14px; background:var(--mist); border:1px solid var(--line)}
.vcp-tools > b{font-family:var(--mono); font-size:.72rem; letter-spacing:.12em; text-transform:uppercase; color:var(--logo-teal); margin-right:4px}
.vcp-tools span{font-weight:700; font-size:.9rem; padding:6px 12px; border-radius:999px; background:#fff; border:1.5px solid var(--line)}
.vcp-tools .x{background:var(--coral); border-color:var(--coral); color:var(--slate)}
.vcp-tools .c{border-color:var(--coral)}
.vcp-mdesc{display:none}
@media (max-width:900px){
  .vcp-how{grid-template-columns:minmax(0,1fr); gap:0}
  .vcp-howlist{display:contents}
  .vcp-steps{order:1; display:flex; gap:8px; overflow-x:auto; border:0; padding:2px 2px 10px; scrollbar-width:none; scroll-snap-type:x proximity}
  .vcp-steps::-webkit-scrollbar{display:none}
  .vcp-steps li{border:0; flex:none; scroll-snap-align:start}
  .vcp-steps button{display:flex; align-items:center; gap:8px; min-height:44px; padding:8px 14px 8px 8px; border-radius:999px; border:2px solid var(--line); background:#fff; width:auto}
  .vcp-steps .n{font-size:1rem; width:28px; height:28px; border-radius:50%; display:grid; place-items:center; background:var(--mist); color:var(--teal)}
  .vcp-steps .t{font-size:.95rem; padding:0; white-space:nowrap}
  .vcp-steps .d, .vcp-steps .bar, .vcp-steps .ok{display:none}
  .vcp-steps li.on button{background:var(--slate); border-color:var(--slate)}
  .vcp-steps li.on .t{color:#fff} .vcp-steps li.on .n{background:var(--mint); color:var(--slate)}
  .vcp-steps li.done .n{background:var(--mint) __TICK__ center/14px no-repeat; color:transparent}
  .vcp-howstage{order:2; padding:14px 0 18px}
  .vcp-howphone{width:min(250px,62vw)}
  .vcp-mdesc{order:3; display:block; text-align:center; margin:4px 0 0; min-height:7em}
  .vcp-mdesc b{display:block; font-family:var(--display); font-stretch:108%; font-size:1.2rem; margin-bottom:4px}
  .vcp-mdesc span{display:block; color:var(--ink-soft); font-size:.97rem; line-height:1.5}
  .vcp-tools{order:4}
}

/* ---------- how it works: head beside the demo video ---------- */
.vcp-howhead{display:grid; grid-template-columns:minmax(0,5fr) minmax(0,7fr); gap:var(--gap) clamp(28px,4vw,56px); align-items:center; margin-bottom:clamp(40px,4.6vw,64px); scroll-margin-top:96px}
.vcp-howhead > *{min-width:0}
.vcp-howhead h2{font-size:clamp(1.9rem,3vw,2.6rem); margin:0 0 .35em}
.vcp-howhead .lede{color:var(--ink-soft); margin:0 0 1em}
.vcp-howhead__demo{margin:0; padding:14px 0 0; border-top:1px solid var(--line); font-size:1.02rem; line-height:1.5}
.vcp-howhead__demo b{font-family:var(--display); font-stretch:106%; color:var(--logo-teal)}
.vcp-howhead__vid .vid{border-radius:var(--r-xl); box-shadow:0 34px 60px -30px rgba(22,53,64,.6), 8px 8px 0 var(--mint)}
@media (max-width:960px){ .vcp-howhead{grid-template-columns:minmax(0,1fr)} .vcp-howhead__vid{margin-right:8px} }

/* ---------- accountability: the second half of the slate "why" band ---------- */
.vcp-acctbox{margin-top:clamp(40px,4.4vw,60px); padding-top:clamp(32px,3.6vw,48px); border-top:1px solid var(--line-dark); scroll-margin-top:96px}
.vcp-accthead{margin-bottom:var(--head-gap)}
.vcp-accthead h3{font-size:clamp(1.8rem,3.1vw,2.75rem); line-height:1.05; color:#fff; margin:0 0 .3em}
.vcp-accthead p{margin:0; font-size:var(--fs-lede); line-height:1.55; font-weight:500; color:rgba(255,255,255,.88)}
.vcp-quote{margin:clamp(24px,2.8vw,36px) 0 0; padding:4px 0 4px 24px; border-left:5px solid var(--mint)}
.vcp-quote blockquote{margin:0 0 12px; font-family:var(--display); font-weight:900; font-stretch:115%; font-size:clamp(1.8rem,3vw,2.7rem); line-height:1; letter-spacing:-.02em; color:var(--mint)}
.vcp-quote figcaption{font-family:var(--mono); font-size:.76rem; letter-spacing:.08em; text-transform:uppercase; line-height:1.6; color:var(--aqua)}
.vcp-quote figcaption a{white-space:nowrap; color:#fff; font-weight:600; text-decoration-color:var(--mint); text-underline-offset:3px}
.vcp-quote figcaption a:hover{color:var(--mint)}
.vcp-acct{display:grid; grid-template-columns:repeat(4,minmax(0,1fr)); gap:0; position:relative}
.vcp-acct > div{position:relative; padding:22px 24px 24px; background:rgba(255,255,255,.05); border:1px solid var(--line-dark); margin-left:-1px}
.vcp-acct > div:first-child{border-radius:var(--r-xl) 0 0 var(--r-xl); margin-left:0}
.vcp-acct > div:last-child{border-radius:0 var(--r-xl) var(--r-xl) 0; background:var(--mint); color:var(--slate); border-color:var(--mint)}
.vcp-acct b{display:block; font-family:var(--display); font-weight:900; font-stretch:125%; font-size:2.6rem; line-height:1; color:var(--mint); margin-bottom:10px}
.vcp-acct > div:last-child b{color:var(--slate)}
.vcp-acct h3{font-size:1.32rem; margin-bottom:.4em; color:#fff}
.vcp-acct > div:last-child h3{color:var(--slate)}
.vcp-acct p{margin:0; font-size:.98rem; line-height:1.5; color:rgba(255,255,255,.84)}
.vcp-acct > div:last-child p{color:var(--slate)}
.vcp-acct > div:not(:last-child)::after{content:""; position:absolute; right:-15px; top:36px; width:28px; height:28px; background:var(--mint) url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 24 24'%3E%3Cpath d='M8 5l7 7-7 7' fill='none' stroke='%231d414e' stroke-width='3' stroke-linecap='round' stroke-linejoin='round'/%3E%3C/svg%3E") center/14px no-repeat; border-radius:50%; z-index:2}
@media (max-width:1100px){ .vcp-acct{grid-template-columns:1fr 1fr; gap:var(--gap)} .vcp-acct > div, .vcp-acct > div:first-child, .vcp-acct > div:last-child{border-radius:16px; margin:0} .vcp-acct > div::after{display:none} }
@media (max-width:560px){ .vcp-acct{grid-template-columns:1fr} }

/* ---------- privacy / is & isn't ---------- */
.vcp-big{font-size:clamp(2.4rem,5.4vw,4.9rem); font-stretch:125%; font-weight:900; text-transform:uppercase; line-height:.88; letter-spacing:-.03em; margin:0 0 .3em}
.vcp-big span{color:var(--mint)}
.vcp-isnt{display:grid; grid-template-columns:minmax(0,1fr) minmax(0,1fr); gap:var(--gap); margin-top:var(--head-gap); align-items:stretch}
.vcp-col{border-radius:var(--r-xl); padding:var(--pad-card)}
.vcp-col h3{font-size:clamp(1.4rem,2.2vw,1.9rem); margin-bottom:.8em}
.vcp-col ul{list-style:none; padding:0; margin:0; display:grid; gap:16px}
.vcp-col li{margin:0; display:grid; grid-template-columns:28px minmax(0,1fr); gap:12px; align-items:start}
.vcp-col li::before{content:""; width:28px; height:28px; border-radius:50%; margin-top:1px}
.vcp-col li b{display:block; font-family:var(--display); font-stretch:106%; font-size:1.1rem; line-height:1.25}
.vcp-col li span{display:block; font-size:.98rem; line-height:1.45; margin-top:2px}
.vcp-col--is{background:var(--mint); color:var(--slate)}
.vcp-col--is li::before{background:var(--slate) url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 24 24'%3E%3Cpath d='M5 12.5l4.5 4.5L19 7.5' fill='none' stroke='%2315ffc8' stroke-width='3.2' stroke-linecap='round' stroke-linejoin='round'/%3E%3C/svg%3E") center/16px no-repeat}
.vcp-col--not{background:rgba(255,255,255,.05); border:1.5px solid var(--line-dark); color:#fff}
.vcp-col--not li::before{border:2px solid var(--aqua); background:url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 24 24'%3E%3Cpath d='M7 7l10 10M17 7L7 17' fill='none' stroke='%23d1feff' stroke-width='2.6' stroke-linecap='round'/%3E%3C/svg%3E") center/14px no-repeat}
.vcp-col--not li span{color:rgba(255,255,255,.8)}
.vcp-crisis{display:flex; gap:14px 26px; align-items:center; justify-content:space-between; flex-wrap:wrap; margin-top:var(--gap); padding:18px 22px; border-radius:16px; background:var(--coral); color:var(--slate)}
.vcp-crisis p{margin:0; font-weight:600; max-width:none; flex:1 1 420px}
@media (max-width:860px){ .vcp-isnt{grid-template-columns:1fr} }

/* ---------- press: two dark features, then the white lists under them ---------- */
.vcp-press{display:grid; grid-template-columns:repeat(2,minmax(0,1fr)); gap:var(--gap)}
.vcp-pr{position:relative; display:flex; flex-direction:column; gap:12px; padding:clamp(22px,2.6vw,34px); border-radius:var(--r-xl); background:var(--slate); background-image:var(--grain); color:#fff; text-decoration:none; min-width:0; transition:transform .25s var(--ease), box-shadow .25s var(--ease)}
a.vcp-pr:hover{transform:translateY(-4px); box-shadow:var(--shadow-soft)}
.vcp-pr__logo{height:52px; display:flex; align-items:center; align-self:flex-start}
.vcp-pr__logo img{height:100%; width:auto; object-fit:contain; filter:brightness(0) invert(1)}
.vcp-pr__meta{font-family:var(--mono); font-size:.74rem; letter-spacing:.1em; text-transform:uppercase; color:var(--aqua); font-weight:600}
.vcp-pr h3{margin:0}
.vcp-pr--g{container-type:inline-size}
.vcp-pr--g h3{font-size:clamp(1.7rem,7.6cqi,2.4rem); line-height:1.06; font-stretch:112%; margin-block:auto}
.vcp-pr--g .vcp-pr__go{margin-top:0}
.vcp-pr--g h3::before{content:"\\201C"; display:block; font-size:2.2em; line-height:.6; color:var(--mint); margin-bottom:-.08em}
.vcp-pr__go{margin-top:auto; padding-top:6px; font-weight:800; font-family:var(--display); font-stretch:106%; color:var(--mint)}
.vcp-wm{font-family:var(--display); font-weight:900; line-height:.95; letter-spacing:-.01em}
.vcp-wm--lst{font-stretch:75%; font-size:1.7rem; text-transform:uppercase; color:#fff}
.vcp-wm--lst i{font-style:normal; color:var(--mint)}
.vcp-wm--pn{font-stretch:125%; font-size:1.3rem; color:var(--slate); line-height:1}
.vcp-wm--pn i{font-style:normal; color:var(--teal); display:block}
.vcp-pr--lst h3{font-size:clamp(1.35rem,2.1vw,1.75rem); line-height:1.15}
.vcp-pr--lst p{margin:0; font-size:1rem; line-height:1.55; color:rgba(255,255,255,.88)}
.vcp-pr--lst p a{color:var(--mint); font-weight:700}
.vcp-pr--lst .audio{margin-top:auto; background:rgba(255,255,255,.08); border:1px solid var(--line-dark); border-radius:16px; transition:border-color .2s}
.vcp-pr--lst .audio:hover{border-color:var(--mint)}
.vcp-pr--lst .audio small{font-size:.875rem}
/* the white lists */
.vcp-prlist{display:grid; gap:var(--gap); grid-auto-rows:1fr; min-width:0}
.vcp-prrow{display:grid; grid-template-columns:132px minmax(0,1fr) auto; gap:6px 22px; align-items:center; padding:14px 24px; border-radius:var(--r-xl); background:#fff; border:1px solid var(--line); color:var(--slate); text-decoration:none; transition:transform .25s var(--ease), box-shadow .25s var(--ease); min-width:0}
.vcp-prrow:hover{transform:translateY(-3px); box-shadow:var(--shadow-soft)}
.vcp-prrow__logo{height:52px; display:flex; align-items:center}
.vcp-prrow__logo img{max-height:100%; max-width:100%; width:auto; object-fit:contain; object-position:left}
.vcp-prrow b{display:block; font-family:var(--display); font-stretch:106%; font-size:1.2rem; line-height:1.2; color:var(--logo-teal)}
.vcp-prrow small{display:block; margin-top:6px; font-family:var(--mono); font-size:.72rem; letter-spacing:.08em; text-transform:uppercase; color:var(--ink-soft); font-weight:600}
.vcp-go{width:38px; height:38px; border-radius:50%; display:grid; place-items:center; background:var(--aqua); color:var(--logo-teal); font-weight:800; transition:background .2s, transform .2s var(--ease); flex:none}
a:hover > .vcp-go{background:var(--mint); transform:translateX(3px)}
.vcp-podlist{background:#fff; border:1px solid var(--line); border-radius:var(--r-xl); padding:18px 24px 8px; display:flex; flex-direction:column; min-width:0}
.vcp-podlist__h{margin:0 0 8px; font-family:var(--mono); font-size:.74rem; letter-spacing:.12em; text-transform:uppercase; font-weight:600; color:var(--logo-teal)}
.vcp-pod{flex:1; display:grid; grid-template-columns:52px minmax(0,1fr) auto; gap:16px; align-items:center; padding:8px 0; border-top:1px solid var(--line); text-decoration:none; color:var(--slate); min-width:0}
.vcp-pod img{width:52px; height:52px; border-radius:10px; object-fit:cover}
.vcp-pod b{display:block; font-family:var(--display); font-stretch:104%; font-size:1.04rem; line-height:1.22; color:var(--logo-teal)}
.vcp-pod small{display:block; font-size:.9rem; color:var(--ink-soft); margin-top:2px; line-height:1.3}
.vcp-pod:hover b{text-decoration:underline; text-decoration-color:var(--mint); text-decoration-thickness:3px; text-underline-offset:3px}
@media (max-width:1180px){ .vcp-prrow{grid-template-columns:104px minmax(0,1fr) auto; gap:6px 18px; padding:18px 20px} .vcp-prrow b{font-size:1.12rem} }
@media (max-width:900px){ .vcp-press{grid-template-columns:minmax(0,1fr)} .vcp-prrow{grid-template-columns:132px minmax(0,1fr) auto} }
@media (max-width:520px){ .vcp-prrow{grid-template-columns:minmax(0,1fr) auto; padding:18px 20px} .vcp-prrow__logo{grid-column:1/-1; height:40px} .vcp-podlist{padding:20px 20px 8px} .vcp-pod{grid-template-columns:52px minmax(0,1fr) auto; gap:12px} .vcp-pod img{width:52px; height:52px} .vcp-pod .vcp-go{width:32px; height:32px} }

/* ---------- adult guide ---------- */
.vcp-guide{display:grid; grid-template-columns:minmax(0,3fr) minmax(0,6fr) minmax(0,3fr); gap:var(--gap) clamp(28px,3.6vw,52px); align-items:center}
.vcp-guide > *{min-width:0}
.vcp-guide h2{margin:0 0 .35em}
.vcp-guide .lede{margin-bottom:1em}
.vcp-cover{position:relative; display:block; max-width:228px; text-decoration:none}
.vcp-cover img{width:100%; border-radius:6px; box-shadow:0 40px 70px -26px rgba(0,0,0,.7); transform:rotate(-4deg); transition:transform .5s var(--ease)}
.vcp-cover:hover img{transform:rotate(-1.5deg)}
.vcp-cover .sticker{position:absolute; right:4%; bottom:8%}
.vcp-guide .lede{color:#fff}
.vcp-shael{margin:0; padding:20px 22px; border-left:5px solid var(--mint); background:rgba(255,255,255,.07); border-radius:0 14px 14px 0}
.vcp-shael p{font-family:var(--display); font-weight:700; font-stretch:104%; font-size:1.18rem; line-height:1.35; margin:0}
.vcp-shael cite{display:block; margin-top:8px; font-style:normal; font-family:var(--mono); font-size:.76rem; letter-spacing:.08em; text-transform:uppercase; color:var(--aqua)}
.vcp-gwrap{margin-top:clamp(32px,3.6vw,48px); background:#fff; color:var(--slate); border-radius:var(--r-xl); padding:var(--pad-card)}
.vcp-gwrap .tabs{margin-bottom:18px}
.vcp-gwrap .tab{transition:background .15s, border-color .15s, color .15s}
.vcp-gwrap [role="tabpanel"]{min-height:300px}
/* steps and cautions as rows: mark | what to do | why, at a width you can read */
.vcp-gsteps, .vcp-avoids{list-style:none; margin:0; padding:0; counter-reset:g; display:grid; border-top:1px solid var(--line)}
.vcp-gsteps li, .vcp-avoids > div{margin:0; counter-increment:g; display:grid; grid-template-columns:56px minmax(0,.8fr) minmax(0,1.2fr); gap:6px 28px; align-items:baseline; padding:14px 4px; border-bottom:1px solid var(--line)}
.vcp-gsteps li::before{content:counter(g); font-family:var(--display); font-weight:900; font-stretch:125%; font-size:2rem; line-height:1; color:var(--teal)}
.vcp-avoids > div::before{content:""; align-self:start; width:30px; height:30px; margin-top:-2px; border-radius:50%; background:var(--slate) url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 24 24'%3E%3Cpath d='M7 7l10 10M17 7L7 17' fill='none' stroke='%2315ffc8' stroke-width='3' stroke-linecap='round'/%3E%3C/svg%3E") center/15px no-repeat}
.vcp-gsteps b, .vcp-avoids b{display:block; font-family:var(--display); font-stretch:106%; font-size:1.16rem; line-height:1.25; color:var(--slate)}
.vcp-gsteps span, .vcp-avoids p{display:block; margin:0; font-size:1rem; color:var(--ink-soft); line-height:1.5}
.vcp-gnote{margin:18px 0 0; padding:16px 20px; border-radius:14px; background:var(--aqua); font-weight:600}
/* what to say: four lines to borrow, two by two, then the framings to avoid */
.vcp-says{display:grid; grid-template-columns:repeat(2,minmax(0,1fr)); gap:16px}
.vcp-says figure{margin:0; border-radius:18px; padding:22px 24px; background:var(--slate); color:#fff}
.vcp-says figcaption{font-family:var(--mono); font-size:.72rem; letter-spacing:.12em; text-transform:uppercase; color:var(--mint); margin-bottom:10px; font-weight:600}
.vcp-says blockquote{margin:0; font-family:var(--display); font-weight:700; font-stretch:104%; font-size:1.1rem; line-height:1.42}
.vcp-says__offer p{margin:12px 0 0; font-size:.97rem; color:var(--aqua)}
.vcp-says .vcp-avoid{grid-column:1/-1; background:var(--mist); color:var(--slate); border:1px solid var(--line)}
.vcp-says .vcp-avoid figcaption{color:var(--logo-teal)}
.vcp-says .vcp-avoid ul{margin:0; padding:0; list-style:none; display:grid; grid-template-columns:repeat(4,minmax(0,1fr)); gap:14px 22px}
.vcp-says .vcp-avoid li{margin:0; padding-left:28px; position:relative; font-weight:600; font-size:1rem; line-height:1.4; text-decoration:line-through; text-decoration-color:rgba(29,65,78,.45)}
.vcp-says .vcp-avoid li::before{content:""; position:absolute; left:0; top:3px; width:18px; height:18px; border-radius:50%; border:2px solid var(--logo-teal); background:url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 24 24'%3E%3Cpath d='M7 7l10 10M17 7L7 17' fill='none' stroke='%231d5a66' stroke-width='3' stroke-linecap='round'/%3E%3C/svg%3E") center/10px no-repeat}
.vcp-after{display:grid; grid-template-columns:repeat(2,minmax(0,1fr)); gap:16px}
.vcp-after > div{background:var(--mist); border:1px solid var(--line); border-radius:18px; padding:22px 24px}
.vcp-after b{display:block; font-family:var(--display); font-stretch:106%; font-size:1.16rem; color:var(--logo-teal); margin-bottom:12px}
.vcp-after p{font-size:1rem; line-height:1.45; margin:0 0 10px; padding-left:14px; border-left:3px solid var(--mint)}
.vcp-after p:last-child{margin-bottom:0}
.vcp-sig{display:grid; border:1px solid var(--line); border-radius:16px; overflow:hidden}
.vcp-sig > div{display:grid; grid-template-columns:minmax(0,.9fr) minmax(0,1.1fr)}
.vcp-sig > div > span{padding:14px 20px; border-top:1px solid var(--line); font-size:1rem; line-height:1.45}
.vcp-sig > div > span:first-child{font-weight:700; background:var(--mist)}
.vcp-sig__h > span{background:var(--slate)!important; color:#fff; border-top:0!important; font-family:var(--mono); font-size:.74rem!important; letter-spacing:.1em; text-transform:uppercase; font-weight:600!important}
.vcp-acc summary{font-size:1.12rem}
.vcp-acc .acc__body p{max-width:86ch}
@media (max-width:1100px){ .vcp-gwrap .tabs{gap:6px} .vcp-gwrap .tab{font-size:.92rem; padding:10px 13px} }
@media (max-width:1000px){ .vcp-says .vcp-avoid ul{grid-template-columns:repeat(2,minmax(0,1fr))} }
@media (max-width:1100px){ .vcp-guide{grid-template-columns:minmax(0,4fr) minmax(0,8fr)} .vcp-shael{grid-column:2} }
@media (max-width:860px){ .vcp-guide{grid-template-columns:1fr} .vcp-shael{grid-column:auto} .vcp-cover{max-width:200px} .vcp-gsteps li, .vcp-avoids > div{grid-template-columns:48px minmax(0,1fr)} .vcp-gsteps li::before, .vcp-avoids > div::before{grid-row:1 / span 2} .vcp-gsteps span, .vcp-avoids p{grid-column:2} }
@media (max-width:680px){ .vcp-says, .vcp-after{grid-template-columns:minmax(0,1fr)} .vcp-says .vcp-avoid{grid-column:auto} .vcp-says .vcp-avoid ul{grid-template-columns:minmax(0,1fr)}
  .vcp-sig > div{grid-template-columns:1fr} .vcp-sig > div > span:last-child{border-top:0; padding-top:0} .vcp-sig > div > span:first-child{background:transparent; padding-bottom:4px} .vcp-sig__h{display:none!important}
  .vcp-gwrap [role="tabpanel"]{min-height:0} .vcp-gwrap .tabs{flex-wrap:nowrap; overflow-x:auto; margin-inline:-4px; padding:0 4px 6px; scrollbar-width:none} .vcp-gwrap .tabs::-webkit-scrollbar{display:none} .vcp-gwrap .tab{white-space:nowrap; min-height:44px} }

/* ---------- final CTA ---------- */
.vcp-cta{text-align:center; position:relative; z-index:1}
.vcp-ctaband{overflow:hidden}
.vcp-ctaband::before{content:""; position:absolute; inset:0; background:__CHECKS_SLATE__ 40px 0/960px 600px; opacity:.24; -webkit-mask-image:radial-gradient(ellipse 58% 70% at 50% 50%, transparent 55%, #000 100%); mask-image:radial-gradient(ellipse 58% 70% at 50% 50%, transparent 55%, #000 100%); pointer-events:none}
.vcp-cta__url{display:block; font-family:var(--display); font-weight:900; font-stretch:112%; font-size:clamp(1.9rem,6.6vw,6.4rem); line-height:.9; letter-spacing:-.035em; color:var(--slate); text-decoration:none; margin:0 0 .25em; overflow-wrap:anywhere; transition:color .2s}
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
      cur = (n + items.length) % items.length; items[cur].classList.add('on'); items[cur].querySelector('button').setAttribute('aria-expanded','true'); shots[cur].classList.add('on'); cap.textContent = 'Step ' + (cur+1) + ' of ' + items.length;
      items.forEach(function(li, i){ li.classList.toggle('done', i < cur); });
      if(md){ md.querySelector('b').textContent = items[cur].querySelector('.t').textContent; md.querySelector('span').textContent = items[cur].querySelector('.d').textContent; } if(list.scrollWidth > list.clientWidth + 4){ var li = items[cur]; list.scrollTo({left: li.offsetLeft - list.offsetLeft - 8, behavior: reduce ? 'auto' : 'smooth'}); } t0 = performance.now(); if(user) auto = false; }
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
    steps_li = ''.join(f'<li class="{"on" if i == 0 else ""}"><button type="button" aria-expanded="{str(i == 0).lower()}" aria-controls="vcp-shot"><span class="n">{i+1}</span><span class="t">{esc(t)}</span><span class="ok" aria-hidden="true"></span><span class="d">{esc(dsc)}</span><span class="bar"></span></button></li>'
                       for i, (im, t, dsc) in enumerate(VC_STEPS))
    shots = ''.join(img(im, f'Vibe Check screen: {t}', cls='on' if i == 0 else '', loading='eager' if i < 2 else 'lazy') for i, (im, t, dsc) in enumerate(VC_STEPS))
    acct = ''.join(f'<div><b>{i+1}</b><h3>{esc(t)}</h3><p>{esc(dsc)}</p></div>' for i, (t, dsc) in enumerate(ACCOUNT))

    # podcasts that discuss Vibe Check (from data.PODCASTS, excluding the featured Longest Shortest Time episode)
    vc_pods = [p for p in PODCASTS if any(h == 'vibe-check.html' for _, h in p[7]) and p[0] != '0v2G7MraWG1V2iyXgGKOUF']

    def pod_img(sid):
        if sid == '5FpaHdterTLr0j9XxK5TGH':
            return 'us-velasquez-mic'
        sq = 'sp-' + sid.lower() + '-sq'
        return sq if os.path.exists(f'{SITE}/assets/img/{sq}.webp') else 'sp-' + sid.lower()
    pods_html = ''.join(f'<a class="vcp-pod" href="https://open.spotify.com/episode/{sid}" target="_blank" rel="noopener">{img(pod_img(sid), "")}<span><b>{esc(title)}</b><small>{esc(show.split(" · ")[0])}</small></span><span class="vcp-go" aria-hidden="true">&#8599;</span></a>'
                        for sid, title, show, date, desc, topics, kw, links in vc_pods)

    gtabs = ''.join(f'<button class="tab" role="tab" id="tab-g-{k}" aria-controls="gp-{k}" aria-selected="{str(i == 0).lower()}" tabindex="{0 if i == 0 else -1}">{esc(lbl)}</button>' for i, (k, lbl, _) in enumerate(GUIDE_TABS))
    gpanels = ''.join(f'<div role="tabpanel" id="gp-{k}" aria-labelledby="tab-g-{k}"{"" if i == 0 else " hidden"}>{html_}</div>' for i, (k, lbl, html_) in enumerate(GUIDE_TABS))

    body = f'''
<section class="vcp-hero">
  <span class="vcp-checks" aria-hidden="true"></span>
  <div class="wrap">
    <div class="rise">
      <nav class="crumbs" aria-label="Breadcrumb"><a href="index.html">Home</a><span>/</span><a href="resources.html">Resources</a><span>/</span><span>Vibe Check</span></nav>
      <div class="vcp-mark"><span class="daisy"></span>By SafeBAE &middot; Reflection &amp; accountability</div>
      <h1 class="vcp-lockup" aria-label="Vibe Check"><span class="vcp-lockup__v">vibe</span><span class="mk vcp-lockup__c">check</span></h1>
      <p class="vcp-tag">No judgment. Just answers.</p>
      <p class="lede">CheckYourVibe.org is a free, anonymous reflection tool for young people who are questioning whether they, or a friend, may have crossed a boundary or caused harm.</p>
      <div class="btns">{btn('Open Vibe Check', CYV, 'mint', size='')}{btn('Watch the demo', '#demo', 'white', arrow=True)}<a class="vcp-hero__guide" href="#adults">Guide for adults<span aria-hidden="true">&nbsp;&darr;</span></a></div>
      <div class="vcp-privacy"><span>No account</span><span>No names</span><span>Nothing stored</span><span>Free</span></div>
    </div>
    <div class="vcp-stage" aria-hidden="true">
      <span class="vcp-bub vcp-bub--l" style="left:0;top:9%">Did I harm someone?</span>
      <span class="vcp-bub vcp-bub--r" style="right:0;top:22%">Was that consent?</span>
      <span class="vcp-bub vcp-bub--l" style="left:2%;top:44%">Did I cross a boundary?</span>
      <span class="vcp-bub vcp-bub--r" style="right:2%;top:60%">Am I a bad person?</span>
      <span class="vcp-bub vcp-bub--l" style="left:6%;top:78%">Not sure if you crossed a line?</span>
      <div class="vcp-phone">{img('vc-screen', '', loading='eager')}</div>
      <span class="sticker sticker--coral" style="left:50%;bottom:6%;translate:-50% 0;white-space:nowrap">Quick exit on every screen</span>
    </div>
  </div>
</section>

<section class="band band--slate" id="why">
  <div class="wrap">
    <div class="vcp-why">
      <div class="vcp-why__txt">
        <h2>Young people are taking hard questions about consent to AI chatbots and anonymous forums.</h2>
        <p>Vibe Check guides users through confusing situations and connects them with real, evidence-based resources on consent, communication, and accountability. It exists because many people have questions about situations that didn’t feel clear and want to do better, but aren’t sure where to start.</p>
        <figure class="vcp-quote"><blockquote>“Accountability is relational.”</blockquote>
          <figcaption>Dominick Shattuck, PhD, on Vibe Check &middot; <a href="{SHATTUCK_NOTE}" target="_blank" rel="noopener">Read his note<span aria-hidden="true">&nbsp;&#8599;</span></a></figcaption></figure>
      </div>
      <div class="vcp-vs">
        <div class="vcp-vs__ai"><small>AI chatbots &amp; forums</small><b>AI is designed to tell you what you want to hear. It doesn’t help you reflect or take accountability.</b>
          <div class="vcp-vs__links">
            <a href="https://safebae.substack.com/p/when-you-ask-ai-for-advice-and-it" target="_blank" rel="noopener"><span>Read: when AI just agrees with you</span><i aria-hidden="true">&#8599;</i></a>
            <a href="ai-literacy.html#mod-m2"><span><em>New</em>The free SafeBAE AI Literacy Training covers why AI tends to agree with you in Module 2.</span><i aria-hidden="true">&rarr;</i></a>
          </div>
        </div>
        <span class="vcp-vs__badge" aria-hidden="true">vs</span>
        <div class="vcp-vs__vc"><small>Vibe Check</small><b>“We’re not here to judge you. We’re here to help you slow down, learn, and choose safer next steps.”</b><div class="vcp-vs__foot">{chips(['Not AI advice', 'Evidence-based resources', 'Anonymous'])}{btn('Open Vibe Check', CYV, 'slate')}</div></div>
      </div>
    </div>
    <div class="vcp-acctbox" id="accountability">
      <div class="vcp-accthead"><h3>The four parts of accountability</h3>
        <p>Vibe Check follows a framework named by Mia Mingus, drawn from transformative justice. Accountability has four parts, and they go in order.</p></div>
      <div class="vcp-acct">{acct}</div>
    </div>
  </div>
</section>

<section class="band band--paper" id="how">
  <div class="wrap">
    <div class="vcp-howhead" id="demo">
      <div class="vcp-howhead__txt"><p class="eyebrow">How it works</p><h2>One step at a time, at your own pace</h2>
        <p class="lede">Vibe Check asks about a situation and how you’re feeling, then shows tools and information based on your answers. There are no right or wrong answers, no pressure to finish, and you can stop at any point.</p>
        <p class="vcp-howhead__demo"><b>Watch the demo:</b> a walkthrough of CheckYourVibe.org, from the first screen to the next steps it offers.</p></div>
      <div class="vcp-howhead__vid">{yt(vc_lib['yt'], 'Vibe Check Demo', label='Demo')}</div>
    </div>
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

<section class="band band--slate" id="privacy">
  <div class="wrap">
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
    <div class="section-head"><div><h2>Vibe Check in the news</h2></div></div>
    <div class="vcp-press">
      <a class="vcp-pr vcp-pr--g" href="https://www.theguardian.com/us-news/2026/may/06/sexual-consent-assault-online-tool" target="_blank" rel="noopener">
        <span class="vcp-pr__logo">{img('the-guardian-logo-vector', 'The Guardian')}</span>
        <span class="vcp-pr__meta">The Guardian &middot; May 2026</span>
        <h3>Young people want to know whether they’ve perpetrated a sexual assault.</h3>
        <span class="vcp-pr__go">Read in The Guardian &#8599;</span>
      </a>
      <div class="vcp-pr vcp-pr--lst">
        <span class="vcp-wm vcp-wm--lst">The Longest <i>Shortest</i> Time</span>
        <span class="vcp-pr__meta">Podcast &middot; with Hillary Frank</span>
        <h3>“Preventing Teens from Joining the Manosphere”</h3>
        <p>Drew Davis joins Hillary Frank on <a href="https://longestshortesttime.com/episode-255-preventing-teens-from-joining-the-manosphere" target="_blank" rel="noopener">The Longest Shortest Time</a> to talk about Vibe Check, the rise of AI and online forums as relationship advice spaces, and why young people need better pathways to reflect, take accountability, and repair harm.</p>
        {spotify('0v2G7MraWG1V2iyXgGKOUF', 'Preventing Teens from Joining the Manosphere', 'The Longest Shortest Time')}
      </div>
      <div class="vcp-prlist">
        <a class="vcp-prrow" href="https://www.vox.com/technology/481444/ai-chatgpt-teen-boys-teenagers-dating-relationships" target="_blank" rel="noopener">
          <span class="vcp-prrow__logo">{img('vox-logo-svg-1', 'Vox')}</span>
          <span><b>Teen boys are using ChatGPT as their wingman. What could go wrong?</b><small>Read on Vox</small></span>
          <span class="vcp-go" aria-hidden="true">&#8599;</span>
        </a>
        <a class="vcp-prrow" href="https://www.trendwatching.com/innovations/when-teens-worry-they-may-have-crossed-a-boundary-vibe-check-helps-them-think-it-through" target="_blank" rel="noopener">
          <span class="vcp-prrow__logo">{img('public', 'TrendWatching')}</span>
          <span><b>When teens worry they crossed a boundary, Vibe Check helps them.</b><small>Read on TrendWatching</small></span>
          <span class="vcp-go" aria-hidden="true">&#8599;</span>
        </a>
        <a class="vcp-prrow" href="https://www.positive.news/" target="_blank" rel="noopener">
          <span class="vcp-prrow__logo"><span class="vcp-wm vcp-wm--pn">Positive <i>News</i></span></span>
          <span><b>A feature on Vibe Check in the October–December 2026 issue.</b><small>Print magazine &middot; Issue 127</small></span>
          <span class="vcp-go" aria-hidden="true">&#8599;</span>
        </a>
      </div>
      <div class="vcp-podlist">
        <p class="vcp-podlist__h">Also heard on</p>
        {pods_html}
      </div>
    </div>
  </div>
</section>

<section class="band band--logo" id="adults">
  <div class="wrap">
    <div class="vcp-guide">
      <a class="vcp-cover" href="{GUIDE_PDF}" target="_blank" rel="noopener" aria-label="Download Check Their Vibe: An Adults’ Guide to Vibe Check (PDF)">{img('guide-vibe-check', 'Cover of Check Their Vibe: An Adults’ Guide to Vibe Check')}<span class="sticker sticker--r">Free PDF &middot; 7 pages</span></a>
      <div class="vcp-guide__txt">
        <p class="eyebrow">For parents, caregivers &amp; adult allies</p>
        <h2>Check Their Vibe: an adults’ guide</h2>
        <p class="lede">Vibe Check is a free, private, self-guided reflection tool for young people navigating moments of sexual uncertainty. This guide helps you introduce it thoughtfully, follow up with care, and understand what it actually contains.</p>
        <div class="btns">{btn('Download the guide (PDF)', GUIDE_PDF, 'mint')}{btn('Go through Vibe Check yourself', CYV, 'ghost')}</div>
      </div>
      <blockquote class="vcp-shael"><p>“As the founding Executive Director of SafeBAE and a mom, this might be the most important tool we’ve developed.”</p><cite>Shael Norris, SafeBAE</cite></blockquote>
    </div>
    <div class="vcp-gwrap" data-tabs="vcp-guide">
      <div class="tabs" role="tablist" aria-label="Inside the guide">{gtabs}</div>
      {gpanels}
    </div>
  </div>
</section>

<section class="band band--mint vcp-ctaband">
  <div class="wrap vcp-cta">
    <a class="vcp-cta__url" href="{CYV}" target="_blank" rel="noopener">checkyour<i>vibe</i>.org</a>
    <p>No account. No names. No judgment. Just unfiltered answers.</p>
    <div class="btns">{btn('Open Vibe Check', CYV, 'slate')}<button class="btn btn--ghost" data-open-help>In crisis? Call or text 988</button></div>
  </div>
</section>
'''
    css = (VC_CSS.replace('__CHECKS_AQUA__', checks('#d1feff')).replace('__CHECKS_SLATE__', checks('#1d414e', sw=3.6, seed=5)).replace('__TICK__', TICK))
    page('vibe-check.html', 'Vibe Check · SafeBAE',
         'Vibe Check (CheckYourVibe.org) is a free, anonymous reflection tool for young people questioning whether they or a friend crossed a boundary or caused harm. No account, nothing stored.',
         body, active='resources', body_class='vcp', fonts='family=Playfair+Display:ital,wght@1,500', head_extra=f'<style>{css}</style>', scripts=f'<script>{VC_JS}</script>')


def build():
    vibe_check()


if __name__ == '__main__':
    build()
