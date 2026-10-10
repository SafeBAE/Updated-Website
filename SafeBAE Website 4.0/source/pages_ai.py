"""ai-literacy.html: launch page for the SafeBAE AI Literacy Training (ai-literacy.safebae.org).
Sources: the live training at https://ai-literacy.safebae.org (checked 9 Oct 2026: program home,
Preface, module overviews, contents, settings, support, educators page) and research_new_pages.md (B).
Imagery: the training's own illustrations and screenshots of the live training (captured with Playwright).
v4: a context-and-launch page in the pattern of choking-hazard.html. Who it is for and what learners
will be able to do, the six modules as a chapter map with one line each (signature), the Four-Step Check,
how it works for learners, educators and parents, and the launch. The module detail lives in the training.
One hand-drawn system: Balsamiq Sans headings, dotted paper, brush, loop, wave and ring marks."""
from lib import *
from urllib.parse import quote

TRAIN = 'https://ai-literacy.safebae.org/'
EDU = 'https://ai-literacy.safebae.org/educators.html'
PRIV = 'https://ai-literacy.safebae.org/privacy-policy.html'


def svg_uri(svg):
    return 'url("data:image/svg+xml,' + quote(svg, safe=" =:/'-.,()") + '")'


def brush(fill, op):
    # the training's double brushstroke (two offset strokes)
    return svg_uri(f"<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 1920 400' preserveAspectRatio='none'><g fill='{fill}' fill-opacity='{op}'>"
                   "<path d='M90 84Q960 -44 1812 84Q1834 88 1848 118Q1880 190 1891 288Q1893 312 1872 310Q960 230 152 310Q134 311 124 290Q92 205 78 112Q74 87 90 84Z'/>"
                   "<path d='M38 158Q900 32 1766 158Q1788 162 1802 192Q1832 262 1842 360Q1845 384 1822 382Q960 306 103 383Q84 384 74 362Q43 280 28 186Q24 161 38 158Z'/></g></svg>")


def loop(stroke, w=3):
    # a pen loop that overshoots where it starts, like the training's callout loops
    return svg_uri(f"<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 400 120' preserveAspectRatio='none'><path d='M34 30C120 6 300 2 368 22C396 30 402 66 384 88C346 116 124 122 42 106C8 98 2 66 16 44C28 24 84 12 156 8' fill='none' stroke='{stroke}' stroke-width='{w}' stroke-linecap='round' vector-effect='non-scaling-stroke'/></svg>")


def wave(stroke):
    return svg_uri(f"<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 200 14' preserveAspectRatio='none'><path d='M2 8C20 2 34 2 52 8S84 14 102 8S134 2 152 8S184 14 198 7' fill='none' stroke='{stroke}' stroke-width='2.4' stroke-linecap='round' vector-effect='non-scaling-stroke'/></svg>")


def vwave(stroke):
    # the chapter map's wavy route, drawn top to bottom
    return svg_uri(f"<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 14 200' preserveAspectRatio='none'><path d='M7 2C1 20 1 34 7 52S13 84 7 102S1 134 7 152S13 184 6 198' fill='none' stroke='{stroke}' stroke-width='2.4' stroke-linecap='round' vector-effect='non-scaling-stroke'/></svg>")


def ring(stroke):
    return svg_uri(f"<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 100 100'><path d='M52 6C78 6 95 24 94 50C93 76 74 94 48 93C22 92 6 74 7 49C8 26 26 9 50 8C62 8 70 11 76 15' fill='none' stroke='{stroke}' stroke-width='3.2' stroke-linecap='round'/></svg>")


# the chapter map: (key, number, title, time, screens, one line, picture, kind, caption, picture focus)
MODS = [
  ('welcome', '', 'Welcome', '2 min', 1, 'What this program covers, who it is for, and what you will be able to do by the end.',
   'ai-shot-welcome', 'shot', 'Preface', '24% 0', 'Screenshot of the training’s Preface screen, “Welcome to the SafeBAE AI Literacy Training”'),
  ('m1', 1, 'What Is AI, Really?', '45 min', 11, 'Traditional AI, machine learning, generative AI, hallucinations, and why privacy matters.',
   'ai-illo-gravity', 'illo', 'Module 1 · Hallucinations', '50% 50%', 'A crowd looks up in confusion at a big screen that reads “Why gravity isn’t real, by AI,” while a small screen-faced AI figure waves from the crowd.'),
  ('m2', 2, 'How AI Shapes the Way We Think', '60 min', 9, 'Sycophancy, filter bubbles, emotional attachment, and the Four-Step Check skillset.',
   'ai-illo-phone', 'illo', 'Module 2 · Emotional Attachment and Persuasion', '50% 30%', 'A teenager looks down at their phone, shoulders slumped, while a screen-headed AI figure puts an arm around them.'),
  ('m3', 3, 'AI and Healthy Relationships', '45 min', 8, 'Simulated vs. genuine connection, AI companions, dependency, and boundaries.',
   'ai-shot-pattern', 'shot', 'Module 3 · A Pattern Check', '24% 0', 'Screenshot of the training: “A Pattern Check,” questions about how you use AI, each answered from Never to Most days'),
  ('m4', 4, 'Using AI Responsibly', '30 min', 8, 'How to fact-check what AI tells you, set your own boundaries with it, notice overreliance, and know when a question should go to a person.',
   'ai-shot-write', 'shot', 'Module 4 · Write Yours', '24% 0', 'Screenshot of the training: the “My AI Boundaries” personal plan, with prompts for daily and weekly time limits'),
  ('m5', 5, 'Nudify Apps and AI-Generated Image Abuse', '45 min', 12, 'What nudification apps are, the harm and the law, real deepfake cases, and how to support someone who has been targeted.',
   'ai-shot-removed', 'shot', 'Module 5 · Getting an Image Removed', '24% 0', 'Screenshot of the training: “Getting an Image Removed,” on free removal tools that work without uploading the image'),
  ('m6', 6, 'Sextortion and Digital Manipulation', '45 min', 7, 'What sextortion is, how AI is making it more common and more dangerous, and how to protect yourself and support a friend.',
   'ai-shot-script', 'shot', 'Module 6 · The Script', '24% 0', 'Screenshot of the training: “The Script,” the five stages sextortion often follows, from building trust to creating urgency'),
  ('end', '', 'Conclusion', '3 min', 1, 'Everything you learned, and where to go next.',
   'ai-illo-cards', 'illo', 'Module 1 · How Generative AI Works', '50% 50%', 'A screen-faced AI figure sits at a card table under hanging lamps, holding playing cards, with word cards reading the, on, sat, cat, the laid out in front of it.'),
]

STEPS4 = [
  ('Pause', 'Don’t accept the answer automatically.', 'Pause means creating a little space between getting an answer and believing or using it. AI can produce an answer instantly. That does not mean you need to accept it instantly.'),
  ('Question', 'What is it claiming? How could you know if it is true?', 'Question means identifying what the AI is actually claiming, and what evidence would support it. Is it giving you a fact? A statistic? An interpretation? A guess about another person? Different claims need different evidence.'),
  ('Check', 'Verify important claims somewhere outside the AI.', 'Check means verifying important information somewhere outside the chatbot. If the AI gives you a citation, check that the source exists and says what the AI claims it says. The more important the answer is, the stronger your checking should be.'),
  ('Ask', 'For anything about your life, ask a person.', 'Ask means recognizing when information alone is not enough. Questions about your health, safety, relationships, school situation, legal rights, or another person’s intentions often depend on context an AI does not have.'),
]

GOALS = [
  'Think critically about AI-generated content, especially on sensitive topics like relationships, consent, and sexual health.',
  'Set healthy boundaries with AI tools and recognize signs of over-reliance.',
  'Understand AI’s limits, including what it can do, what it can’t do, and why it’s not a substitute for real-world connection.',
  'Know when to seek real-world support from trusted adults, friends, and resources.',
]

HOW = [
  ('Create a free account', 'Your name, your school or organization, a class code if someone gave you one, your email and a password. You confirm you are 13 or older.'),
  ('Go at your own pace', 'Your progress is saved to your account, so you can stop any time and pick up where you left off on any phone or computer.'),
  ('Switch devices with a resume code', 'Pick up on a phone, tablet or school computer. Your progress travels; anything you wrote stays on the device where you wrote it.'),
  ('Get your certificate', 'A one-page certificate you can print or download. It unlocks once you have finished every screen and every activity.'),
]

BAR = '<div class="ai-frame__bar" aria-hidden="true"><i></i><i></i><i></i><span>ai-literacy.safebae.org</span></div>'


def frame(name, alt, cap='', cls=''):
    """A screenshot of the training in a level browser frame, at the screenshot's own proportions."""
    capt = f'<figcaption>{esc(cap)}</figcaption>' if cap else ''
    return f'<figure class="ai-frame {cls}">{BAR}{img(name, alt)}{capt}</figure>'


def chapter_map():
    """The chapter map, drawn top to bottom: one stop per module with one line each, and the module's
    own picture beside the list (it follows the stop you point at or pick)."""
    rows, pics = [], []
    for i, (k, n, title, time, screens, line, im, kind, cap, pos, alt) in enumerate(MODS):
        on = k == 'm1'
        dot = str(n) if n else ('&#9733;' if k == 'welcome' else '&#10003;')
        lbl = f'Module {n}' if n else ('Start here' if k == 'welcome' else 'Wrap-up')
        rows.append(f'<li class="ai-row{" ai-row--end" if not n else ""}{" on" if on else ""}" id="mod-{k}">'
                    f'<button type="button" aria-pressed="{str(on).lower()}" data-mod="{i}">'
                    f'<span class="ai-row__dot" aria-hidden="true">{dot}</span>'
                    f'<span class="ai-row__b"><span class="ai-row__t"><span class="sr-only">{lbl}: </span>{esc(title)}</span><span class="ai-row__d">{esc(line)}</span></span>'
                    f'<span class="ai-row__m"><b>{time}</b><span>{screens} screen{"s" if screens > 1 else ""}</span></span></button></li>')
        pics.append(f'<img src="{imgsrc(im)}" alt="{esc(alt)}" class="ai-pic--{kind}{" on" if on else ""}" style="object-position:{pos}" loading="lazy" decoding="async" data-cap="{esc(cap)}">')
    first_cap = MODS[1][8]
    return f'''<div class="ai-route">
  <ol class="ai-list" aria-label="Chapter map">{''.join(rows)}</ol>
  <div class="ai-route__side">
    <figure class="ai-pic">{BAR}<div class="ai-pic__img">{''.join(pics)}</div><figcaption aria-live="polite">{esc(first_cap)}</figcaption></figure>
    <p class="ai-route__note">Activities along the way include quick checks, sorting activities, simulated feeds, scenarios and a personal AI boundaries plan.</p>
    <div class="btns">{btn('Start the training', TRAIN, 'mint')}</div>
  </div>
</div>'''


CSS = r'''
body.ai{--hand:"Balsamiq Sans","Comic Neue",var(--body)}
.ai h1{font-family:var(--hand)}
/* one heading voice on this page: the training's hand lettering */
.ai main :is(h2,h3){font-family:var(--hand); font-stretch:100%; font-weight:700; letter-spacing:0}
.ai main h2{font-size:clamp(2rem,3.7vw,3.2rem); line-height:1.06}
.ai .section-head .lede{max-width:none}
/* marker word on this page = the training's double brushstroke */
.ai .mk{background:@@BRUSH_MINT@@ center/100% 100% no-repeat; padding:.02em .22em .08em; margin:0 -.1em; color:var(--slate); border-radius:0}
.ai .ai-hero .mk{background-image:@@BRUSH_TEAL@@; color:#fff}
.ai-loop{position:relative; display:inline-block}
.ai-loop::after{content:""; position:absolute; inset:-.32em -.5em -.36em -.55em; background:@@LOOP_MINT@@ center/100% 100% no-repeat; pointer-events:none}
.ai-dots{background-color:#fff; background-image:@@DOTS@@}

/* ---------- frames ---------- */
.ai-frame,.ai-pic{margin:0; position:relative; background:#fff; border:2px solid var(--slate); border-radius:16px; overflow:hidden; box-shadow:8px 8px 0 var(--mint)}
.ai-frame__bar{display:flex; align-items:center; gap:6px; height:30px; flex:none; padding:0 12px; background:var(--slate-deep); border-bottom:2px solid var(--slate)}
.ai-frame__bar i{width:9px; height:9px; border-radius:50%; background:rgba(209,254,255,.35)}
.ai-frame__bar i:first-child{background:var(--coral)}
.ai-frame__bar span{margin-left:10px; font-family:var(--mono); font-size:.7rem; letter-spacing:.06em; color:var(--aqua); white-space:nowrap; overflow:hidden; text-overflow:ellipsis}
.ai-frame img{width:100%; height:auto}
.ai-pic figcaption{font-family:var(--hand); font-weight:700; font-size:.98rem; line-height:1.3; padding:10px 14px; background:var(--aqua); color:var(--slate); border-top:2px solid var(--slate)}

/* ---------- hero ---------- */
.ai-hero{position:relative; overflow:hidden; background-color:var(--slate); background-image:var(--grain), @@DOTS_DARK@@; color:#fff; --wm-o:.15}
.ai-hero > .wrap{position:relative; z-index:1; display:grid; grid-template-columns:repeat(2,minmax(0,1fr)); gap:clamp(28px,4vw,60px); align-items:center; padding-block:clamp(40px,5vw,72px) clamp(48px,5.5vw,84px)}
.ai-hero .wrap > *{min-width:0}
.ai-hero .crumbs{color:rgba(255,255,255,.8)}
.ai-hero .eyebrow{color:var(--mint)}
.ai-hero h1{font-weight:700; font-stretch:100%; font-size:clamp(2.4rem,4.4vw,4rem); line-height:1.08; letter-spacing:-.01em; margin:0 0 .4em; text-transform:none}
.ai-hero .lede{color:#fff; max-width:none}
.ai-launch{font-family:var(--hand); font-size:clamp(1.1rem,1.6vw,1.32rem); margin:6px 0 26px; color:var(--aqua)}
.ai-launch .ai-loop{color:#fff; font-weight:700; margin:0 .35em}
.ai-facts{display:flex; flex-wrap:wrap; gap:8px; margin-top:24px}
.ai-facts span{font-family:var(--hand); font-weight:700; font-size:.98rem; padding:6px 12px; border-radius:10px; border:2px solid rgba(209,254,255,.35); color:#fff}
.ai-facts span:first-child{background:var(--mint); color:var(--slate); border-color:var(--mint)}
.ai-stage{position:relative; padding:0 12% 66px 0}
.ai-phone{position:absolute; right:0; bottom:0; width:30%; aspect-ratio:390/800; border-radius:30px; border:8px solid #0b1f25; background:#0b1f25; overflow:hidden; box-shadow:0 30px 60px -24px rgba(0,0,0,.7), 6px 6px 0 var(--mint); z-index:2}
.ai-phone img{width:100%; height:100%; object-fit:cover; object-position:top}
.ai-note{position:absolute; left:5%; bottom:6px; z-index:3; font-family:var(--hand); font-weight:700; font-size:clamp(1rem,1.4vw,1.2rem); color:var(--slate); background:var(--mint); padding:8px 14px 9px; border-radius:6px; transform:rotate(-3deg); box-shadow:3px 3px 0 var(--slate)}
.ai-note svg{position:absolute; right:-50px; top:-34px; width:56px; height:50px; color:var(--mint); transform:scaleX(-1)}
@media (max-width:960px){ .ai-hero > .wrap{grid-template-columns:minmax(0,1fr)} .ai-stage{max-width:640px} }
@media (max-width:520px){ .ai-stage{padding:0 15% 74px 0} .ai-phone{width:35%; border-width:6px; border-radius:22px} .ai-note{left:0} .ai-note svg{display:none} }

/* ---------- who it's for: head and the training's own note beside the goals ---------- */
.ai-who{display:grid; grid-template-columns:minmax(0,7fr) minmax(0,5fr); gap:var(--gap) clamp(28px,4vw,56px); align-items:center}
.ai-who > *{min-width:0}
.ai-who h2{margin:0 0 .45em}
.ai-who .lede{margin:0}
.ai-noteq{position:relative; margin:clamp(30px,3.4vw,44px) 14px 10px 10px; display:grid; gap:6px; padding:20px 28px 22px; border-radius:18px; background:var(--aqua)}
.ai-noteq::after{content:""; position:absolute; inset:-10px -12px; background:@@LOOP_TEAL@@ center/100% 100% no-repeat; pointer-events:none}
.ai-noteq figcaption{font-family:var(--hand); font-weight:700; font-size:1.08rem; line-height:1.2; color:var(--logo-teal)}
.ai-noteq blockquote{margin:0; font-family:var(--hand); font-size:1.12rem; line-height:1.5; color:var(--slate)}
.ai-goals{display:flex; flex-direction:column; background:#fff; border:2px solid var(--slate); border-radius:var(--r-xl); padding:var(--pad-card); box-shadow:8px 8px 0 var(--teal)}
.ai-goals h3{font-size:clamp(1.35rem,2vw,1.7rem); margin:0 0 .7em}
.ai-goals ol{list-style:none; padding:0; margin:0; display:grid; gap:14px; counter-reset:g}
.ai-goals li{counter-increment:g; display:grid; grid-template-columns:44px minmax(0,1fr); gap:14px; align-items:center; margin:0; font-size:1.02rem; line-height:1.48}
.ai-goals li::before{content:counter(g); width:44px; height:44px; display:grid; place-items:center; font-family:var(--hand); font-weight:700; font-size:1.25rem; color:var(--logo-teal); background:@@RING_TEAL@@ center/100% 100% no-repeat}
@media (max-width:900px){ .ai-who{grid-template-columns:minmax(0,1fr)} .ai-goals{margin-right:8px} }
@media (max-width:560px){ .ai-noteq{margin-inline:0} .ai-noteq::after{display:none} }

/* ---------- the chapter map: a wavy route down the list, the module's picture beside it ---------- */
.ai-mods{background-image:var(--grain), @@DOTS_DARK@@}
.ai-mods .section-head .lede{color:rgba(255,255,255,.86)}
.ai-route{display:grid; grid-template-columns:minmax(0,8fr) minmax(0,4fr); gap:var(--gap) clamp(28px,4vw,56px); align-items:start}
.ai-route > *{min-width:0}
.ai-list{position:relative; list-style:none; margin:0; padding:0}
.ai-list::before{content:""; position:absolute; left:21px; top:30px; bottom:30px; width:14px; background:@@VWAVE_MINT@@ center/100% 100% no-repeat; opacity:.5}
.ai-row{margin:0; scroll-margin-top:120px}
.ai-row button{all:unset; box-sizing:border-box; width:100%; cursor:pointer; position:relative; display:grid; grid-template-columns:56px minmax(0,1fr) auto; gap:0 18px; align-items:center; padding:9px 16px 9px 0; border-radius:16px; transition:background .25s}
.ai-row button:focus-visible{outline:3px solid var(--mint); outline-offset:2px}
.ai-row__dot{position:relative; z-index:1; width:56px; height:56px; display:grid; place-items:center; border-radius:50%; background:var(--slate-deep); border:2.5px solid rgba(209,254,255,.45); font-family:var(--hand); font-weight:700; font-size:1.45rem; color:var(--aqua); transition:transform .3s var(--ease), background .3s, border-color .3s, color .3s}
.ai-row--end .ai-row__dot{font-size:1.15rem}
.ai-row__b{display:grid; gap:2px; min-width:0}
.ai-row__t{font-family:var(--hand); font-weight:700; font-size:1.24rem; line-height:1.2; color:#fff}
.ai-row__d{font-size:.96rem; line-height:1.45; color:rgba(255,255,255,.8)}
.ai-row__m{display:grid; justify-items:end; gap:2px; font-family:var(--mono); font-size:.74rem; letter-spacing:.06em; color:var(--aqua); white-space:nowrap}
.ai-row__m b{font-family:var(--hand); font-size:1.02rem; letter-spacing:0; color:#fff}
.ai-row button:hover{background:rgba(209,254,255,.05)}
.ai-row button:hover .ai-row__dot{border-color:var(--mint); transform:scale(1.05)}
.ai-row.on button{background:rgba(21,255,200,.1)}
.ai-row.on .ai-row__dot{background:var(--mint); border-color:var(--mint); color:var(--slate)}
.ai-row.on .ai-row__dot::after{content:""; position:absolute; inset:-11px; background:@@RING_MINT@@ center/100% 100% no-repeat}
.ai-row.on .ai-row__t{color:var(--mint)}
.ai-route__side{position:sticky; top:96px; display:flex; flex-direction:column; gap:18px}
.ai-pic{display:flex; flex-direction:column}
.ai-pic__img{position:relative; aspect-ratio:4/3; background:var(--mist); overflow:hidden}
.ai-pic__img img{position:absolute; inset:0; width:100%; height:100%; object-fit:cover; opacity:0; transform:scale(1.03); transition:opacity .45s, transform .6s var(--ease)}
.ai-pic__img img.on{opacity:1; transform:none}
.ai-route__note{margin:6px 0 0; font-size:1rem; line-height:1.55; color:rgba(255,255,255,.86)}
@media (max-width:960px){
  .ai-route{grid-template-columns:minmax(0,1fr)}
  .ai-route__side{position:relative; top:auto; order:-1; margin-right:8px}
}
@media (max-width:560px){
  .ai-row button{grid-template-columns:44px minmax(0,1fr); gap:0 14px; padding-right:8px}
  .ai-row__dot{width:44px; height:44px; font-size:1.15rem}
  .ai-list::before{left:15px}
  .ai-row__m{grid-column:2; justify-items:start; display:flex; gap:10px; margin-top:4px}
}

/* ---------- four-step check: four stops on one drawn loop ---------- */
.ai-4band{background-image:@@DOTS@@}
.ai-4wrap{position:relative; padding-bottom:64px}
.ai-4{position:relative; list-style:none; margin:0; padding:0; display:grid; grid-template-columns:repeat(4,minmax(0,1fr)); gap:var(--gap); counter-reset:s}
.ai-4 li{position:relative; z-index:1; margin:0; counter-increment:s; display:flex; flex-direction:column; background:#fff; border:2px solid var(--slate); border-radius:var(--r-xl); padding:20px 22px 22px; box-shadow:6px 6px 0 var(--teal); min-width:0}
.ai-4 li::before{content:counter(s); width:52px; height:52px; display:grid; place-items:center; margin-bottom:8px; font-family:var(--hand); font-weight:700; font-size:1.6rem; color:var(--logo-teal); background:@@RING_TEAL@@ center/100% 100% no-repeat}
.ai-4 li:first-child{background:var(--mint); box-shadow:6px 6px 0 var(--slate)}
.ai-4 li:not(:last-child)::after{content:""; position:absolute; right:calc(var(--gap) * -1 + 1px); top:34px; width:calc(var(--gap) + 6px); height:22px; z-index:2; background:url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 40 24'%3E%3Cpath d='M2 14C12 6 22 6 34 12M26 4l9 8-10 6' fill='none' stroke='%231d414e' stroke-width='3' stroke-linecap='round' stroke-linejoin='round'/%3E%3C/svg%3E") center/contain no-repeat}
.ai main .ai-4 h3{font-size:1.5rem; line-height:1; text-transform:uppercase; letter-spacing:.04em; margin:0 0 .4em}
.ai-4__q{font-family:var(--hand); font-weight:700; font-size:1.14rem; line-height:1.4; color:var(--logo-teal); margin:0}
.ai-4 li:first-child .ai-4__q{color:var(--slate)}
/* the loop back from Ask to Pause */
.ai-4__back{position:absolute; left:calc((100% - 3 * var(--gap)) / 8); right:calc((100% - 3 * var(--gap)) / 8); bottom:0; height:58px; pointer-events:none}
.ai-4__back svg{width:100%; height:100%; overflow:visible; color:var(--slate)}
.ai-4__back span{position:absolute; left:50%; bottom:-6px; transform:translateX(-50%); font-family:var(--hand); font-weight:700; font-size:1.08rem; color:var(--logo-teal); background:var(--aqua); padding:0 14px; white-space:nowrap}
.ai-4note{display:grid; grid-template-columns:44px minmax(0,1fr); gap:14px; align-items:center; margin:clamp(22px,2.6vw,32px) 0 0; font-family:var(--hand); font-size:1.12rem; line-height:1.5}
.ai-4note svg{width:44px; height:40px; color:var(--teal)}
@media (max-width:1100px){ .ai-4wrap{padding-bottom:0} .ai-4{grid-template-columns:repeat(2,minmax(0,1fr))} .ai-4 li:nth-child(2)::after{display:none} .ai-4__back{display:none} }
@media (max-width:620px){ .ai-4{grid-template-columns:minmax(0,1fr)} .ai-4 li::after{display:none} }

/* ---------- how it works, for learners, educators and parents ---------- */
.ai-steps{list-style:none; margin:0; padding:0; display:grid; grid-template-columns:repeat(4,minmax(0,1fr)); gap:var(--gap); counter-reset:h}
.ai-steps li{position:relative; margin:0; counter-increment:h; background:rgba(255,255,255,.05); border:1.5px solid var(--line-dark); border-radius:var(--r-xl); padding:20px 22px 22px; min-width:0}
.ai-steps li::before{content:counter(h); display:grid; place-items:center; width:52px; height:52px; margin-bottom:8px; font-family:var(--hand); font-weight:700; font-size:1.6rem; color:var(--mint); background:@@RING_MINT@@ center/100% 100% no-repeat}
.ai-steps li:not(:last-child)::after{content:""; position:absolute; right:calc(var(--gap) * -1 + 1px); top:34px; width:calc(var(--gap) + 6px); height:22px; z-index:2; background:url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 40 24'%3E%3Cpath d='M2 14C12 6 22 6 34 12M26 4l9 8-10 6' fill='none' stroke='%2315ffc8' stroke-width='3' stroke-linecap='round' stroke-linejoin='round'/%3E%3C/svg%3E") center/contain no-repeat}
.ai main .ai-steps h3{font-size:1.28rem; line-height:1.15; margin:0 0 .4em; color:#fff}
.ai-steps p{margin:0; color:rgba(255,255,255,.84); font-size:.96rem; line-height:1.5}
.ai-adults{display:grid; grid-template-columns:repeat(2,minmax(0,1fr)); gap:var(--gap); align-items:stretch; margin-top:clamp(36px,4vw,56px); scroll-margin-top:96px}
.ai-card{display:flex; flex-direction:column; gap:12px; border-radius:var(--r-xl); padding:var(--pad-card); background:#fff; color:var(--slate); border:2px solid var(--slate); box-shadow:8px 8px 0 var(--teal); min-width:0}
.ai main .ai-card h3{font-size:1.5rem; line-height:1.12; margin:0}
.ai-card p{margin:0; line-height:1.55; font-size:1rem}
.ai-card .btns{margin-top:auto; padding-top:8px}
.ai-card--edu{grid-column:1/-1; display:grid; grid-template-columns:minmax(0,7fr) minmax(0,5fr); gap:12px clamp(28px,4vw,56px); align-items:start; background:var(--mint); box-shadow:8px 8px 0 var(--slate)}
.ai-card--edu > :is(h3,p){grid-column:1}
.ai-card--edu .ai-flow{grid-column:2; grid-row:1 / span 3; align-self:center; margin:0; padding:4px 0 4px 28px; border-top:0; border-left:1.5px dashed rgba(29,65,78,.4); gap:12px}
.ai-card--edu .btns{grid-column:1; padding-top:4px}
.ai-flow{list-style:none; margin:2px 0 0; padding:12px 0 0; border-top:1.5px dashed rgba(29,65,78,.4); display:grid; gap:6px; counter-reset:f}
.ai-flow li{counter-increment:f; margin:0; display:grid; grid-template-columns:28px minmax(0,1fr); gap:10px; align-items:center; font-family:var(--hand); font-weight:700; font-size:1.02rem; line-height:1.2}
.ai-flow li::before{content:counter(f); width:28px; height:28px; display:grid; place-items:center; font-size:.95rem; background:@@RING_SLATE@@ center/100% 100% no-repeat}
.ai-card blockquote{margin:0; font-family:var(--hand); font-size:1.08rem; line-height:1.5; padding:14px 16px; border-radius:14px; background:var(--mist); border:1.5px dashed rgba(29,65,78,.35)}
.ai-card small{color:var(--ink-soft); font-size:.9rem; line-height:1.45}
.ai-safe{display:flex; flex-wrap:wrap; align-items:center; justify-content:space-between; gap:14px 32px; margin-top:var(--gap); padding:18px 24px; border-radius:var(--r-xl); border:1.5px solid rgba(254,113,113,.6); background:rgba(254,113,113,.08)}
.ai-safe p{margin:0; flex:1 1 520px; color:rgba(255,255,255,.92); font-size:1.02rem; line-height:1.5}
.ai-safe b{color:#fff}
@media (max-width:1100px){
  .ai-steps{grid-template-columns:repeat(2,minmax(0,1fr))} .ai-steps li:nth-child(2)::after{display:none}
}
@media (max-width:760px){ .ai-adults{grid-template-columns:minmax(0,1fr)} .ai-card{margin-right:8px} .ai-card--edu{display:flex} .ai-card--edu .ai-flow{padding:12px 0 0; border-left:0; border-top:1.5px dashed rgba(29,65,78,.4); gap:6px} }
@media (max-width:560px){ .ai-steps{grid-template-columns:minmax(0,1fr)} .ai-steps li::after{display:none} }

/* ---------- final CTA ---------- */
.ai-cta{text-align:center}
.ai main section .ai-cta h2{font-size:clamp(2.4rem,6vw,5.2rem); line-height:1.02; margin:0 0 .25em}
.ai-cta .mk{background-image:@@BRUSH_WHITE@@}
.ai-cta p{font-family:var(--hand); font-size:clamp(1.1rem,1.6vw,1.35rem); max-width:none; margin:0}
.ai-cta .btns{justify-content:center; margin-top:24px}
.ai-cta__url{display:block; margin-top:16px; font-family:var(--mono); font-size:.9rem; letter-spacing:.06em; color:var(--slate)}
@media (prefers-reduced-motion:reduce){ .ai-pic__img img{transition:none} }
'''

JS = r'''
(function(){
  var d = document;
  /* chapter map: pointing at or picking a stop shows that module's picture; links from other pages (#mod-m2) pick it */
  var list = d.querySelector('.ai-list'), pics = [].slice.call(d.querySelectorAll('.ai-pic__img img')), cap = d.querySelector('.ai-pic figcaption');
  if(!list) return;
  var rows = [].slice.call(list.querySelectorAll('.ai-row')), cur = -1, picked = 1;
  function show(i){ if(i === cur) return; cur = i; pics.forEach(function(p, k){ p.classList.toggle('on', k === i); }); if(cap) cap.textContent = pics[i].getAttribute('data-cap'); }
  function pick(i){ picked = i; rows.forEach(function(r, k){ r.classList.toggle('on', k === i); r.querySelector('button').setAttribute('aria-pressed', String(k === i)); }); show(i); }
  rows.forEach(function(r, i){ var b = r.querySelector('button');
    b.addEventListener('click', function(){ pick(i); });
    b.addEventListener('mouseenter', function(){ show(i); });
    b.addEventListener('focus', function(){ show(i); });
  });
  list.addEventListener('mouseleave', function(){ show(picked); });
  function fromHash(){ var m = /^#mod-(\w+)$/.exec(location.hash); if(!m) return; var i = rows.map(function(r){ return r.id; }).indexOf('mod-' + m[1]); if(i > -1) pick(i); }
  window.addEventListener('hashchange', fromHash); fromHash();
})();
'''


def build():
    DOTS = 'radial-gradient(rgba(19,132,143,.2) 1.1px, transparent 1.5px) 0 0/18px 18px'
    DOTS_DARK = 'radial-gradient(rgba(209,254,255,.11) 1.1px, transparent 1.5px) 0 0/18px 18px'
    css = CSS
    for k, v in {
        'BRUSH_TEAL': brush('#13848f', '0.85'), 'BRUSH_MINT': brush('#15ffc8', '0.9'), 'BRUSH_WHITE': brush('#ffffff', '0.85'),
        'LOOP_MINT': loop('#15ffc8'), 'LOOP_TEAL': loop('#13848f'),
        'VWAVE_MINT': vwave('#15ffc8'),
        'RING_TEAL': ring('#13848f'), 'RING_MINT': ring('#15ffc8'), 'RING_SLATE': ring('#1d414e'),
        'DOTS_DARK': DOTS_DARK, 'DOTS': DOTS,
    }.items():
        css = css.replace(f'@@{k}@@', v)
    assert '@@' not in css

    goals = ''.join(f'<li><span>{esc(g)}</span></li>' for g in GOALS)
    four = ''.join(f'<li><h3>{esc(t)}</h3><p class="ai-4__q">{esc(q)}</p></li>' for t, q, l in STEPS4)
    back = ('<div class="ai-4__back" aria-hidden="true"><svg viewBox="0 0 1000 58" preserveAspectRatio="none"><path d="M994 2C998 40 940 52 760 54L240 54C60 52 2 40 6 4" fill="none" stroke="currentColor" stroke-width="3" stroke-linecap="round" vector-effect="non-scaling-stroke"/>'
            '<path d="M-4 18L6 3L17 17" fill="none" stroke="currentColor" stroke-width="3" stroke-linecap="round" stroke-linejoin="round" vector-effect="non-scaling-stroke"/></svg><span>Keep going around, every answer, every time</span></div>')
    how = ''.join(f'<li><h3>{esc(t)}</h3><p>{esc(dsc)}</p></li>' for t, dsc in HOW)
    arrow_r = '<svg viewBox="0 0 60 54" aria-hidden="true"><path d="M6 8C8 30 22 42 50 40M40 30l11 10-13 8" fill="none" stroke="currentColor" stroke-width="3.2" stroke-linecap="round" stroke-linejoin="round"/></svg>'
    arrow = '<svg viewBox="0 0 60 54" aria-hidden="true"><path d="M52 50C36 44 18 30 10 8M4 18l6-12 11 7" fill="none" stroke="currentColor" stroke-width="3.2" stroke-linecap="round" stroke-linejoin="round"/></svg>'

    body = f'''
<section class="ai-hero">
  <span class="wm-daisy" aria-hidden="true"></span>
  <div class="wrap">
    <div class="rise">
      <nav class="crumbs" aria-label="Breadcrumb"><a href="index.html">Home</a><span>/</span><a href="resources.html">Resources</a><span>/</span><span>AI Literacy Training</span></nav>
      <p class="eyebrow">New &middot; Free &middot; Ages 13+</p>
      <h1>SafeBAE AI Literacy <span class="mk">Training</span></h1>
      <p class="lede">Six modules for high school and college students on AI, how it works, where it can go wrong, and what it means for navigating relationships, consent, privacy, and a world increasingly shaped by algorithms.</p>
      <p class="ai-launch">Launches during U.S. Media Literacy Week, <span class="ai-loop">October 26–30, 2026</span></p>
      <div class="btns">{btn('Start the training', TRAIN, 'mint')}{btn('Group access for educators', '#adults', 'ghost', arrow=True)}</div>
      <div class="ai-facts"><span>Free</span><span>6 modules</span><span>Self-paced</span><span>Progress saves</span><span>Certificate</span></div>
    </div>
    <div class="ai-stage">
      {frame('ai-shot-home', 'Screenshot of the training’s home screen: “SafeBAE AI Literacy Training” beside a drawing of a billboard with a binary smiley face and a name tag that reads “Hello, my name is AI”')}
      <div class="ai-phone">{img('ai-m-four', 'The training on a phone, open to the Four-Step Check')}</div>
      <span class="ai-note">{arrow}Media Literacy Week, Oct 26–30</span>
    </div>
  </div>
</section>

<section class="band ai-dots" id="who">
  <div class="wrap ai-who">
    <div>
      <h2>Made for high school and college students</h2>
      <p class="lede">The training is designed for high school and college students, though anyone 13 or older may find it useful. It builds the skills to understand AI and how it affects your relationships, your safety and the decisions you make.</p>
      <figure class="ai-noteq">
        <figcaption>A note before you begin</figcaption>
        <blockquote>“This program is not about shaming anyone for using AI. AI can be a helpful tool for creativity, learning, and fun. However, like any tool, it’s important to know how to use it thoughtfully.”</blockquote>
      </figure>
    </div>
    <div class="ai-goals reveal">
      <h3>By the end, you will be able to:</h3>
      <ol>{goals}</ol>
    </div>
  </div>
</section>

<section class="band band--deep ai-mods" id="modules">
  <div class="wrap">
    <div class="section-head"><div><p class="eyebrow">Chapter map &middot; 57 screens</p><h2>Six modules, in order</h2></div></div>
    {chapter_map()}
  </div>
</section>

<section class="band band--aqua ai-4band" id="four-step">
  <div class="wrap">
    <div class="section-head"><div><p class="eyebrow">A skill from Module 1</p><h2>Pause. Question. Check. Ask.</h2>
      <p class="lede">The Four-Step Check gives you a simple way to decide what to trust, what to verify, and when an AI answer is not enough.</p></div></div>
    <div class="ai-4wrap reveal"><ol class="ai-4">{four}</ol>{back}</div>
    <p class="ai-4note">{arrow_r}<span>These four steps are for answers. An AI agent takes actions, so the check has to come before it acts. Module 2 builds on it.</span></p>
  </div>
</section>

<section class="band band--slate" id="how">
  <div class="wrap">
    <div class="section-head"><div><h2>Create an account and go at your own pace</h2></div></div>
    <ol class="ai-steps reveal">{how}</ol>
    <div class="ai-adults reveal" id="adults">
      <div class="ai-card ai-card--edu">
        <h3>Group access for educators</h3>
        <p>Assign the training to your students and follow their progress. Tell SafeBAE about your group; SafeBAE reviews each registration and emails you a class code to give your students. Registering also creates an ordinary account, so you can go through the training yourself straight away.</p>
        <ol class="ai-flow" aria-label="How group access works"><li>Tell SafeBAE about your group</li><li>SafeBAE reviews your registration</li><li>A class code arrives by email</li></ol>
        <div class="btns">{btn('Register for group access', EDU, 'slate')}</div>
      </div>
      <div class="ai-card">
        <h3>For parents and caregivers</h3>
        <p>The training is free and self-paced, for high school and college students and anyone 13 or older. When a learner joins with a class code, the teacher or group leader who gave it can see their name, school, email and how far they have got.</p>
        <p>Learners can print or download a completion record to hand in when a teacher, parent, advisor or club leader asks for one.</p>
        <div class="btns">{btn('Resources for parents', 'parents.html', 'ghost', arrow=True)}</div>
      </div>
      <div class="ai-card">
        <h3>Privacy</h3>
        <blockquote>“Your name, school, email, progress and quiz answers are saved to your account, where SafeBAE staff can see them. What you type, and the personal plans and self-checks you fill in, stay on the device you used.”</blockquote>
        <small>From the training’s sign-up screen.</small>
        <div class="btns">{btn('Read the Privacy Policy', PRIV, 'ghost')}</div>
      </div>
    </div>
    <div class="ai-safe"><p><b>Modules 5 and 6 cover image abuse and sextortion.</b> Every screen of the training has a Quick Exit button, and a Support button that lists free crisis lines and SafeBAE resources.</p><button class="btn btn--coral btn--sm" type="button" data-open-help>Talk to someone now</button></div>
  </div>
</section>

<section class="band band--mint">
  <div class="wrap ai-cta">
    <p class="eyebrow">Launches October 26–30, 2026</p>
    <h2>Start the <span class="mk">training</span></h2>
    <p>Create a free account and your progress saves as you go.</p>
    <div class="btns">{btn('Open the AI Literacy Training', TRAIN, 'slate')}{btn('Group access for educators', EDU, 'ghost')}</div>
    <span class="ai-cta__url">ai-literacy.safebae.org</span>
  </div>
</section>
'''
    page('ai-literacy.html', 'AI Literacy Training · SafeBAE',
         'The free SafeBAE AI Literacy Training: six self-paced modules for high school and college students on how AI works, feeds, relationships, using AI well, fake images and sextortion. Launches October 26–30, 2026.',
         body, active='resources', body_class='ai', fonts='family=Balsamiq+Sans:ital,wght@0,400;0,700;1,400',
         head_extra=f'<style>{css}</style>', scripts=f'<script>{JS}</script>')


if __name__ == '__main__':
    build()
