"""ai-literacy.html: the SafeBAE AI Literacy Training product page.
Sources: the live training at https://ai-literacy.safebae.org (checked 9 Oct 2026: program home,
Preface, module overviews, contents, settings, support, educators page) and research_new_pages.md (B).
Imagery: the training's own illustrations and screenshots of the live training (captured with Playwright).
v3: layout pass. One hand-drawn system (Balsamiq Sans headings, dotted paper, brush and loop marks),
level frames, module panels whose two columns end level in every state, and the Four-Step Check loop."""
from lib import *
from urllib.parse import quote
import films_common as _fc
from films_common import vibe_band
VIBE_CSS = getattr(_fc, 'VIBE_CSS', '')

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


def ring(stroke):
    return svg_uri(f"<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 100 100'><path d='M52 6C78 6 95 24 94 50C93 76 74 94 48 93C22 92 6 74 7 49C8 26 26 9 50 8C62 8 70 11 76 15' fill='none' stroke='{stroke}' stroke-width='3.2' stroke-linecap='round'/></svg>")


MODS = [
  dict(k='welcome', n='', label='start here', title='Welcome', time='2 min', screens=1,
       lead='What this program covers, who it is for, and what you will be able to do by the end.',
       desc='The Preface introduces the program, who it is for, and the four things learners will be able to do by the end.',
       explore=[], sections=[],
       img=('ai-shot-welcome', 'shot', 'Screenshot of the training’s Preface screen, “Welcome to the SafeBAE AI Literacy Training”', 'Preface')),
  dict(k='m1', n=1, label='how AI works', title='What Is AI, Really?', time='45 min', screens=11,
       lead='Before we can talk about how AI affects our relationships, our thinking, or our safety, we need to understand what AI actually is and what it isn’t.',
       desc='Traditional AI, machine learning, generative AI, hallucinations, and why privacy matters.',
       explore=['What hallucinations are, and how to check a source yourself.', 'Why AI sounds correct even when it’s wrong.', 'Who can read your AI chats, and what to change.',
                'What an AI agent is, and what changes when AI takes actions.', 'The Four-Step Check, a framework for using AI.'],
       sections=['Different Types of AI', 'How Generative AI Works', 'Training Data and Testing Data', 'Hallucinations', 'When AI Sounds Certain', 'Your Chats Are Records', 'What’s Really Going On?', 'AI Agents', 'The Four-Step Check'],
       img=('ai-illo-gravity', 'illo', 'A crowd looks up in confusion at a big screen that reads “Why gravity isn’t real, by AI,” while a small screen-faced AI figure waves from the crowd.', '1D · Hallucinations')),
  dict(k='m2', n=2, label='feeds and thinking', title='How AI Shapes the Way We Think', time='60 min', screens=9,
       lead='AI doesn’t just regurgitate information, it also shapes how we think.',
       desc='Sycophancy, filter bubbles, emotional attachment, and the Four-Step Check skillset.',
       explore=['How recommendation algorithms work and shape what you see online.', 'What information a feed collects about you, and what it has no way of knowing.', 'Social sycophancy and validation, or why AI tends to agree with you.',
                'Confirmation bias and filter bubbles.', 'Emotional attachment and persuasion.', 'How to recognize online misinformation and manipulation.'],
       sections=['How the Feed Decides What You See', 'Taking Some of It Back', 'Confirmation Bias and Filter Bubbles', 'Social Sycophancy and Validation', 'What Would You Say?', 'Emotional Attachment and Persuasion', 'How AI Changes What You Believe'],
       img=('ai-illo-phone', 'illo', 'A teenager looks down at their phone, shoulders slumped, while a screen-headed AI figure puts an arm around them.', '2F · Emotional Attachment and Persuasion')),
  dict(k='m3', n=3, label='relationships', title='AI and Healthy Relationships', time='45 min', screens=8,
       lead='A chatbot can respond immediately, remember what you have told it and agree with how you feel. It is not in a relationship with you.',
       desc='Simulated vs. genuine connection, AI companions, dependency, and boundaries.',
       explore=['The difference between AI-simulated connection and genuine connection.', 'Emotional attachment to AI companions, and when reliance can become a problem.', 'Why companion apps are designed the way they are, and what laws and safety rules apply to them.',
                'How AI can show up inside real relationships, and why that’s risky.', 'How AI can make you less receptive to boundaries, feedback and differing opinions.', 'What changes when an AI agent reads or sends messages that involve other people.'],
       sections=['AI vs. Genuine Connection', 'AI Companions and Dependency', 'A Pattern Check', 'AI, Boundaries, and Consent in Relationships', 'AI Agents and Other People', 'Your Own Boundaries, in Practice'],
       img=('ai-shot-pattern', 'shot', 'Screenshot of the training: “A Pattern Check,” twelve questions about how you use AI, each answered from Never to Most days', '3C · A Pattern Check')),
  dict(k='m4', n=4, label='using AI well', title='Using AI Responsibly', time='30 min', screens=8,
       lead='AI is a tool, and like any tool, it can be used well or poorly.',
       desc='How to fact-check what AI tells you, set your own boundaries with it, notice overreliance, and know when a question should go to a person.',
       explore=['Critical thinking and fact-checking skills.', 'Healthy boundaries with AI.', 'How to recognize overreliance on AI.', 'Practical strategies for using AI safely and thoughtfully.'],
       sections=['Check It', 'Three Checks, For Real', 'Your Boundaries', 'Write Yours', 'AI or a Person?', 'Where Does This Question Go?'],
       img=('ai-shot-write', 'shot', 'Screenshot of the training: the “My AI Boundaries” personal plan, with prompts for daily and weekly time limits', '4D · Write Yours')),
  dict(k='m5', n=5, label='fake images', title='Nudify Apps and AI-Generated Image Abuse', time='45 min', screens=12,
       lead='This module focuses on one of the ways AI is being used to cause harm: creating sexual images of real people without their consent.',
       desc='What nudification apps are, the harm and the law, real deepfake cases, and how to support someone who has been targeted.',
       explore=['What nudification apps are and how they use AI to create sexualized images.', 'The harms of nonconsensual AI-generated sexual images.', 'The legal consequences of creating or sharing these images.',
                'How to support someone whose image has been used without consent.', 'Practical steps for reporting and removing nonconsensual images.'],
       sections=['Before Any of This', 'One Photo Is Enough', 'Harm and the Law', 'Know Your Rights', 'Real Cases', 'What Usually Happens Instead', 'Getting an Image Removed', 'If It Happens', 'Where to Go'],
       img=('ai-shot-removed', 'shot', 'Screenshot of the training: “Getting an Image Removed,” on free removal tools that work without uploading the image', '5G · Getting an Image Removed')),
  dict(k='m6', n=6, label='sextortion', title='Sextortion and Digital Manipulation', time='45 min', screens=7,
       lead='Sextortion is when someone threatens to share intimate images or information unless a person gives them something they want.',
       desc='What sextortion is, how AI is making it more common and more dangerous, and how to protect yourself and support a friend.',
       explore=['What sextortion is, and who does it.', 'The five stages it usually runs in, and what each one looks like.', 'How AI is making sextortion easier and more dangerous.',
                'The warning signs of sextortion and manipulation.', 'Practical strategies for protecting yourself online.', 'How to support a friend who is going through sextortion.'],
       sections=['What Sextortion Is', 'The Script', 'What AI Changed', 'The Ten-Minute Lockdown', 'If It Is Happening to You or a Friend'],
       img=('ai-shot-script', 'shot', 'Screenshot of the training: “The Script,” the five stages sextortion often follows, from building trust to creating urgency', '6B · The Script')),
  dict(k='end', n='', label='wrap-up', title='Conclusion', time='3 min', screens=1,
       lead='Everything you learned, and where to go next.',
       desc='The certificate is a one-page file you can print or download. It unlocks once you have finished every screen and every activity in the program.',
       explore=['The Four-Step Check: Pause. Question. Check. Ask.', 'Why confident language is not evidence that an answer is right.', 'Why an AI can produce caring language without experiencing care.',
                'When a question depends on another person’s feelings, boundaries or consent, and has to go to that person.', 'What rights you have if an image of you is made or shared, and how to get it removed.', 'The six steps if it happens to you, and what to do if it happens to a friend.'],
       sections=[],
       img=('ai-illo-cards', 'illo', 'A screen-faced AI figure sits at a card table under hanging lamps, holding playing cards, with word cards reading the, on, sat, cat, the laid out in front of it.', '1B · How Generative AI Works')),
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

SUPPORT = [
  ('988 Suicide & Crisis Lifeline', 'Call or text 988', 'Any crisis, any hour. Trained counselors, by phone, text or chat.', 'https://988lifeline.org/'),
  ('Crisis Text Line', 'Text HOME to 741741', 'A trained counselor texts back. No phone call.', 'https://www.crisistextline.org/'),
  ('The Trevor Project', 'Call 1-866-488-7386 or text START to 678-678', 'Counselors trained to work with LGBTQ+ young people.', 'https://www.thetrevorproject.org/get-help/'),
  ('National Sexual Assault Hotline', 'Call 800.656.4673 or text HOPE to 64673', 'Free and confidential. Staff go through your options with you.', 'https://rainn.org/hotline'),
  ('love is respect', 'Call 1-866-331-9474 or text LOVEIS to 22522', 'For a dating relationship that feels controlling or unsafe.', 'https://www.loveisrespect.org/'),
  ('Childhelp National Child Abuse Hotline', 'Call or text 800.422.4453', 'For when the person hurting you is an adult in your life.', 'https://www.childhelphotline.org/'),
  ('Take It Down', 'takeitdown.ncmec.org', 'Free help removing nude or sexual images taken of you before you turned 18, from participating platforms. The image never leaves your phone.', 'https://takeitdown.ncmec.org/'),
]

# (title, text, href, image, tag, image focus)
CONNECT = [
  ('Certified Peer Educator Training', 'A 16-module course on consent, boundaries, bystander intervention, online safety and your Title IX rights. Module 3 points to it for the relationship skills it covers more fully.', 'peer-educator.html', 'preview1', 'Free · 16 modules', '50% 100%'),
  ('#knowB4Unude', 'SafeBAE’s PSA on the pressures, risks and consequences of sharing intimate images, with a teaching guide. A natural companion to Modules 5 and 6.', 'film-knowb4unude.html', 'knowb4unude', 'Film + guide', '4% 50%'),
  ('BAE Skills Lab', 'Six interactive lessons on consent, boundaries and healthy relationships.', 'skills-lab.html', 'sl-boundary-flags-m', '6 activities', '50% 0'),
]
VIBE_TEXT = 'An anonymous self-check for anyone worried they crossed a line with somebody. Made by survivors.'

BAR = '<div class="ai-frame__bar" aria-hidden="true"><i></i><i></i><i></i><span>ai-literacy.safebae.org</span></div>'


def frame(name, alt, cap='', cls=''):
    """A screenshot of the training in a level browser frame, at the screenshot's own proportions."""
    capt = f'<figcaption>{esc(cap)}</figcaption>' if cap else ''
    return f'<figure class="ai-frame {cls}">{BAR}{img(name, alt)}{capt}</figure>'


def media(name, kind, alt, cap, extra=''):
    """Screenshot (browser bar) or illustration in a frame whose picture area stretches to its row partner."""
    bar = BAR if kind == 'shot' else ''
    return (f'<figure class="ai-media ai-media--{kind}">{bar}<div class="ai-media__img">{img(name, alt)}{extra}</div>'
            f'<figcaption>{esc(cap)}</figcaption></figure>')


def mod_panel(m, i):
    num = f'Module {m["n"]}' if m['n'] else ('Start here' if m['k'] == 'welcome' else 'Wrap-up')
    name, kind, alt, cap = m['img']
    letter = str(m['n']) if m['n'] else ''
    secs = ''.join(f'<li><b>{letter}{chr(65+j)}</b>{esc(s)}</li>' for j, s in enumerate(m['sections']))
    exp = ''.join(f'<li>{esc(x)}</li>' for x in m['explore'])
    exp_lbl = 'In this module, you will explore' if m['n'] else 'What you’ll have learned, among other things'
    desc = f'<p class="ai-mpanel__desc">{esc(m["desc"])}</p>'
    if m['k'] == 'end':
        # the certificate note sits under the picture; the recap list takes the text column
        left = f'<p class="ai-hand-lbl">{exp_lbl}</p><ul class="ai-ticks">{exp}</ul>'
        under = f'<div class="ai-cert"><p class="ai-hand-lbl">Your certificate</p><p>{esc(m["desc"])}</p></div>'
    elif exp:
        # short lists beside a long section list run in one column, so both columns end together
        one = ' ai-ticks--1' if len(m['sections']) - len(m['explore']) >= 2 else ''
        left = f'{desc}<p class="ai-hand-lbl">{exp_lbl}</p><ul class="ai-ticks{one}">{exp}</ul>'
        # where the text column is much longer than the section list, the list runs in one column at mid widths
        lmass = len(m['lead']) + len(m['desc']) + sum(len(x) for x in m['explore']) + (40 if len(m['title']) > 24 else 0)
        rmass = sum(len(x) for x in m['sections']) + 30 * len(m['sections'])
        stack = ' ai-secs--stack' if lmass >= 1.35 * rmass else ''
        under = f'<div class="ai-secs{stack}"><p class="ai-hand-lbl">Inside this module</p><ol>{secs}</ol></div>'
    else:
        left, under = desc, ''
    prev_m = MODS[i - 1] if i else None
    next_m = MODS[i + 1] if i + 1 < len(MODS) else None
    go_lbl = 'Start the training' if m['k'] == 'welcome' else ('Start Module 1' if m['k'] == 'm1' else 'Open the training')
    def step_lbl(x):
        return f'Module {x["n"]}' if x['n'] else ('Welcome' if x['k'] == 'welcome' else 'Wrap-up')
    back = f'<button type="button" class="btn btn--ghost btn--sm" data-mod-go="{prev_m["k"]}"><span aria-hidden="true">&larr;</span> {step_lbl(prev_m)}</button>' if prev_m else ''
    nxt = f'<button type="button" class="btn btn--slate btn--sm" data-mod-go="{next_m["k"]}">Next: {step_lbl(next_m)} <span class="arr" aria-hidden="true">&rarr;</span></button>' if next_m else ''
    return f'''<div class="ai-mpanel" role="tabpanel" id="mp-{m['k']}" aria-labelledby="tab-mod-{m['k']}"{'' if m['k'] == 'm1' else ' hidden'}>
  <div class="ai-mpanel__txt">
    <p class="ai-mpanel__k"><span>{esc(num)}</span><span>{esc(m['time'])}</span><span>{m['screens']} screen{'s' if m['screens'] > 1 else ''}</span></p>
    <h3>{esc(m['title'])}</h3>
    <p class="ai-mpanel__lead">{esc(m['lead'])}</p>
    {left}
  </div>
  <div class="ai-mpanel__side">{media(name, kind, alt, cap)}{under}</div>
  <div class="ai-mpanel__foot">{btn(go_lbl, TRAIN, 'mint', 'sm')}<span class="ai-mpanel__nav">{back}{nxt}</span></div>
</div>'''


def map_html():
    btns = []
    for m in MODS:
        sel = m['k'] == 'm1'
        dot = str(m['n']) if m['n'] else ('&#9733;' if m['k'] == 'welcome' else '&#10003;')
        btns.append(f'<button class="ai-stop{" ai-stop--end" if not m["n"] else ""}" role="tab" id="tab-mod-{m["k"]}" aria-controls="mp-{m["k"]}" aria-selected="{str(sel).lower()}" tabindex="{0 if sel else -1}">'
                    f'<span class="ai-stop__dot" aria-hidden="true">{dot}</span><span class="ai-stop__lbl">{esc(m["label"])}</span><span class="ai-stop__t">{esc(m["time"])}</span>'
                    f'<span class="sr-only">{esc(m["title"])}</span></button>')
    return '<div class="ai-map" role="tablist" aria-label="Training map">' + ''.join(btns) + '</div>'


def four_step():
    """The Four-Step Check as a loop you can walk: four stops on a drawn circle, one note card."""
    nodes = ''.join(f'<button type="button" class="ai-node ai-node--{i}" data-step="{i}" aria-pressed="{str(i == 0).lower()}"><span class="ai-node__n" aria-hidden="true">{i+1}</span><b>{esc(t)}</b><small>{esc(s)}</small></button>' for i, (t, s, l) in enumerate(STEPS4))
    def then(i):
        t, s, l = STEPS4[(i + 1) % 4]
        return f'<p class="ai-4d__then"><span>{"Then back to" if i == 3 else "Then"}</span><b>{esc(t)}</b><em>{esc(s)}</em></p>'
    details = ''.join(f'<div class="ai-4d" data-d="{i}"{"" if i == 0 else " hidden"}><p class="ai-4d__k"><span class="ai-4d__n" aria-hidden="true">{i+1}</span><span>Step {i+1} of 4</span></p><h3>{esc(t)}</h3><p class="ai-4d__q">{esc(s)}</p><p class="ai-4d__p">{esc(l)}</p>{then(i)}</div>' for i, (t, s, l) in enumerate(STEPS4))
    arcs = [('M200 52C286 48 354 116 349 202', 'translate(306 95) rotate(45)'), ('M349 202C352 286 284 353 199 349', 'translate(305 306) rotate(135)'),
            ('M199 349C114 352 47 284 51 199', 'translate(94 305) rotate(225)'), ('M51 199C48 114 116 47 200 52', 'translate(95 94) rotate(315)')]
    svg = ''.join(f'<g class="ai-arc ai-arc--{i}"><path pathLength="1" d="{d}"/><path class="h" d="M-11 -9L1 0L-11 9" transform="{t}"/></g>' for i, (d, t) in enumerate(arcs))
    dots = ''.join(f'<i{" class=on" if i == 0 else ""}></i>' for i in range(4))
    return f'''<div class="ai-4 reveal">
  <div class="ai-wheel" data-cur="0">
    <svg class="ai-wheel__c" viewBox="0 0 400 400" aria-hidden="true">{svg}</svg>
    <div class="ai-wheel__mid" aria-hidden="true"><b>Keep going<br>around</b><span>every answer,<br>every time</span></div>
    {nodes}
  </div>
  <div class="ai-4card">
    <div class="ai-4details" aria-live="polite">{details}</div>
    <div class="ai-4card__foot"><span class="ai-4dots" aria-hidden="true">{dots}</span><button type="button" class="btn btn--slate btn--sm" data-4next>Next: <span data-4name>Question</span> <span class="arr" aria-hidden="true">&rarr;</span></button></div>
  </div>
</div>'''


CSS = r'''
body.ai{--hand:"Balsamiq Sans","Comic Neue",var(--body)}
.ai h1{font-family:var(--hand)}
/* one heading voice on this page: the training's hand lettering (the Vibe Check band keeps its own) */
.ai main section:not(.fvb) :is(h2,h3){font-family:var(--hand); font-stretch:100%; font-weight:700; letter-spacing:0}
.ai main section:not(.fvb) h2{font-size:clamp(2rem,3.7vw,3.2rem); line-height:1.06}
.ai .section-head .lede{max-width:none}
/* marker word on this page = the training's double brushstroke */
.ai .mk{background:@@BRUSH_MINT@@ center/100% 100% no-repeat; padding:.02em .22em .08em; margin:0 -.1em; color:var(--slate); border-radius:0}
.ai .ai-hero .mk{background-image:@@BRUSH_TEAL@@; color:#fff}
.ai-loop{position:relative; display:inline-block}
.ai-loop::after{content:""; position:absolute; inset:-.32em -.5em -.36em -.55em; background:@@LOOP_MINT@@ center/100% 100% no-repeat; pointer-events:none}
.ai-hand-lbl{font-family:var(--hand); font-weight:700; font-size:1.08rem; margin:0 0 10px; color:var(--logo-teal)}
.ai-dots{background-color:#fff; background-image:@@DOTS@@}
.ai-anchor{position:absolute; top:0; left:0; width:1px; height:1px; scroll-margin-top:64px}

/* ---------- frames: every screenshot sits level ---------- */
.ai-frame,.ai-media{margin:0; position:relative; background:#fff; border:2px solid var(--slate); border-radius:16px; overflow:hidden; box-shadow:8px 8px 0 var(--mint)}
.ai-frame__bar{display:flex; align-items:center; gap:6px; height:30px; flex:none; padding:0 12px; background:var(--slate-deep); border-bottom:2px solid var(--slate)}
.ai-frame__bar i{width:9px; height:9px; border-radius:50%; background:rgba(209,254,255,.35)}
.ai-frame__bar i:first-child{background:var(--coral)}
.ai-frame__bar span{margin-left:10px; font-family:var(--mono); font-size:.7rem; letter-spacing:.06em; color:var(--aqua); white-space:nowrap; overflow:hidden; text-overflow:ellipsis}
.ai-frame img{width:100%; height:auto}
.ai-frame figcaption,.ai-media figcaption{flex:none; font-family:var(--hand); font-weight:700; font-size:.95rem; line-height:1.3; padding:9px 14px; background:var(--aqua); color:var(--slate); border-top:2px solid var(--slate)}
/* a frame that takes the height of the text beside it: the picture area grows, cropped from its top-left */
.ai-media{display:flex; flex-direction:column; flex:1 1 auto; min-width:0}
.ai-media__img{position:relative; flex:1 1 auto; aspect-ratio:12/5; overflow:hidden; background:var(--mist)}
.ai-media__img > img{position:absolute; inset:0; width:100%; height:100%; object-fit:cover; object-position:0 0}
.ai-media--illo .ai-media__img > img{object-position:50% 50%}

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

/* ---------- who + goals ---------- */
.ai-who{display:grid; grid-template-columns:minmax(0,5fr) minmax(0,7fr); gap:clamp(24px,3.4vw,48px); align-items:stretch}
.ai-who > *{min-width:0}
.ai-who .ai-media{box-shadow:8px 8px 0 var(--mint)}
.ai-who .ai-media__img{aspect-ratio:1200/834}
.ai-who .ai-media__img > img{object-position:38% 50%}
.ai-goals{display:flex; flex-direction:column; background:#fff; border:2px solid var(--slate); border-radius:var(--r-xl); padding:var(--pad-card); box-shadow:8px 8px 0 var(--teal)}
.ai-goals h3{font-size:clamp(1.4rem,2.2vw,1.8rem); margin-bottom:.7em}
.ai-goals ol{flex:1; list-style:none; padding:0; margin:0; display:grid; gap:14px; align-content:space-around; counter-reset:g}
.ai-goals li{counter-increment:g; display:grid; grid-template-columns:44px minmax(0,1fr); gap:14px; align-items:center; margin:0; font-size:1.04rem; line-height:1.5}
.ai-goals li::before{content:counter(g); width:44px; height:44px; display:grid; place-items:center; font-family:var(--hand); font-weight:700; font-size:1.25rem; color:var(--logo-teal); background:@@RING_TEAL@@ center/100% 100% no-repeat}
.ai-noteq{margin:calc(var(--gap) + 14px) 14px 10px; position:relative; display:grid; grid-template-columns:auto minmax(0,1fr); gap:6px 26px; align-items:center; padding:22px 32px; border-radius:18px; background:var(--aqua)}
.ai-noteq::after{content:""; position:absolute; inset:-10px -12px; background:@@LOOP_TEAL@@ center/100% 100% no-repeat; pointer-events:none}
.ai-noteq figcaption{font-family:var(--hand); font-weight:700; font-size:1.1rem; line-height:1.2; color:var(--logo-teal); max-width:7.4em}
.ai-noteq blockquote{margin:0; font-family:var(--hand); font-size:1.14rem; line-height:1.5; color:var(--slate)}
@media (max-width:900px){ .ai-who{grid-template-columns:minmax(0,1fr)} .ai-who .ai-media{margin-right:8px} .ai-noteq{grid-template-columns:minmax(0,1fr)} .ai-noteq figcaption{max-width:none} }

/* ---------- module map ---------- */
.ai-mods{background-image:var(--grain), @@DOTS_DARK@@}
.ai-map{position:relative; display:grid; grid-template-columns:repeat(8,minmax(0,1fr)); gap:4px; margin-bottom:26px; padding-top:6px}
.ai-map::before{content:""; position:absolute; left:6%; right:6%; top:32px; height:14px; background:@@WAVE_MINT@@ center/100% 100% no-repeat; opacity:.55}
.ai-stop{position:relative; font:inherit; background:none; border:0; color:#fff; cursor:pointer; display:flex; flex-direction:column; align-items:center; gap:6px; padding:0 2px 10px; text-align:center; border-radius:12px}
.ai-stop__dot{width:56px; height:56px; display:grid; place-items:center; border-radius:50%; background:var(--slate-deep); border:2.5px solid rgba(209,254,255,.45); font-family:var(--hand); font-weight:700; font-size:1.5rem; color:var(--aqua); transition:transform .3s var(--ease), background .3s, border-color .3s, color .3s; position:relative; z-index:1}
.ai-stop--end .ai-stop__dot{font-size:1.2rem}
.ai-stop__lbl{font-family:var(--hand); font-weight:700; font-size:1.04rem; line-height:1.15; color:#fff}
.ai-stop__t{font-family:var(--mono); font-size:.74rem; letter-spacing:.06em; color:var(--aqua)}
.ai-stop:hover .ai-stop__dot{border-color:var(--mint); transform:translateY(-3px)}
.ai-stop[aria-selected="true"] .ai-stop__dot{background:var(--mint); border-color:var(--mint); color:var(--slate); transform:scale(1.08)}
.ai-stop[aria-selected="true"] .ai-stop__dot::after{content:""; position:absolute; inset:-12px; background:@@RING_MINT@@ center/100% 100% no-repeat}
.ai-stop[aria-selected="true"] .ai-stop__lbl{color:var(--mint)}

/* ---------- module panel: text 7 / picture 5, both columns end on the same line in every state ---------- */
.ai-mpanel{display:grid; grid-template-columns:minmax(0,7fr) minmax(0,5fr); gap:clamp(20px,2.4vw,30px) clamp(24px,3.4vw,48px); align-items:stretch; background:#fff; color:var(--slate); border-radius:var(--r-xl); padding:clamp(22px,3vw,38px); box-shadow:8px 8px 0 var(--mint)}
.ai-mpanel > *{min-width:0}
.ai-mpanel__k{display:flex; flex-wrap:wrap; gap:6px; margin:0 0 14px}
.ai-mpanel__k span{font-family:var(--mono); font-size:.74rem; letter-spacing:.08em; text-transform:uppercase; font-weight:600; padding:4px 9px; border-radius:6px; background:var(--aqua); color:var(--slate)}
.ai-mpanel__k span:first-child{background:var(--slate); color:var(--mint)}
.ai-mpanel h3{font-size:clamp(1.7rem,2.8vw,2.5rem); line-height:1.1; margin:0 0 .45em}
.ai-mpanel__lead{font-family:var(--hand); font-size:1.2rem; line-height:1.5; margin:0 0 14px}
.ai-mpanel__desc{color:var(--ink-soft); margin:0 0 20px}
.ai-ticks{list-style:none; padding:0; margin:0; display:grid; grid-template-columns:repeat(2,minmax(0,1fr)); gap:11px 28px}
.ai-ticks--1{grid-template-columns:minmax(0,1fr)}
.ai-ticks li{display:grid; grid-template-columns:22px minmax(0,1fr); gap:10px; margin:0; line-height:1.45; font-size:.98rem}
.ai-ticks li::before{content:""; width:20px; height:20px; margin-top:2px; background:url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 24 24'%3E%3Cpath d='M3 13c3 2 5 5 6 7c3-7 7-12 12-16' fill='none' stroke='%2313848f' stroke-width='3' stroke-linecap='round' stroke-linejoin='round'/%3E%3C/svg%3E") center/contain no-repeat}
.ai-mpanel__side{display:flex; flex-direction:column; gap:20px}
.ai-mpanel .ai-media{box-shadow:6px 6px 0 var(--teal)}
.ai-secs ol{list-style:none; margin:0; padding:12px 0 0; border-top:1px solid var(--line); columns:2; column-gap:22px}
.ai-secs li{break-inside:avoid; margin:0 0 9px; display:grid; grid-template-columns:auto minmax(0,1fr); gap:9px; align-items:baseline; font-size:.95rem; line-height:1.3; font-weight:600}
.ai-secs li:last-child{margin-bottom:0}
.ai-secs li b{font-family:var(--mono); font-size:.72rem; background:var(--slate); color:var(--mint); border-radius:5px; padding:3px 6px}
.ai-cert{padding:16px 18px; border-radius:14px; background:var(--mist); border:1px solid var(--line)}
.ai-cert p:last-child{margin:0; font-size:.98rem; line-height:1.5}
.ai-mpanel__foot{position:relative; grid-column:1/-1; display:flex; flex-wrap:wrap; gap:12px 16px; align-items:center; justify-content:space-between; padding-top:clamp(20px,2.2vw,26px)}
.ai-mpanel__foot::before{content:""; position:absolute; left:0; right:0; top:0; height:10px; background:@@WAVE_TEAL@@ center/100% 100% no-repeat; opacity:.5}
.ai-mpanel__nav{display:flex; flex-wrap:wrap; gap:10px; margin-left:auto}
.ai-mpanel .btn--ghost:hover{background:rgba(29,65,78,.08)}
.ai-mpanel :focus-visible{outline-color:var(--teal)}
@media (max-width:1180px){
  /* mid widths: heading block beside the picture, then the two lists across the full panel */
  .ai-mpanel{grid-template-columns:repeat(2,minmax(0,1fr)); grid-template-rows:auto auto auto 1fr; row-gap:0; align-items:start}
  .ai-mpanel__txt,.ai-mpanel__side{display:contents}
  .ai-mpanel__k{grid-column:1; grid-row:1} .ai-mpanel h3{grid-column:1; grid-row:2} .ai-mpanel__lead{grid-column:1; grid-row:3} .ai-mpanel__desc{grid-column:1; grid-row:4; margin-bottom:0}
  .ai-mpanel .ai-media{grid-column:2; grid-row:1 / span 4; align-self:stretch}
  .ai-mpanel__txt > .ai-hand-lbl{grid-column:1/-1; grid-row:5; margin-top:26px}
  .ai-ticks{grid-column:1/-1; grid-row:6}
  .ai-secs,.ai-cert{grid-column:1/-1; grid-row:7; margin-top:26px}
  .ai-secs ol{columns:3}
  .ai-mpanel__foot{grid-row:8; margin-top:26px}
}
@media (max-width:1000px){
  .ai-map{display:flex; overflow-x:auto; scrollbar-width:none; gap:2px; margin-inline:calc(var(--gutter) * -1); padding-inline:var(--gutter); scroll-snap-type:x proximity}
  .ai-map::-webkit-scrollbar{display:none} .ai-map::before{display:none}
  .ai-stop{flex:0 0 100px; scroll-snap-align:start}
}
@media (max-width:760px){ .ai-secs ol{columns:2} .ai-ticks{grid-template-columns:minmax(0,1fr)} }
@media (max-width:640px){
  /* stack: label, title, picture, text, sections, actions */
  .ai-mpanel:not([hidden]){display:flex; flex-direction:column; gap:0}
  .ai-mpanel__k{order:1} .ai-mpanel h3{order:2} .ai-mpanel .ai-media{order:3; flex:none; margin:4px 6px 22px 0} .ai-mpanel__lead{order:4} .ai-mpanel__desc{order:5; margin-bottom:0}
  .ai-mpanel__txt > .ai-hand-lbl{order:6; margin-top:22px} .ai-ticks{order:7} .ai-secs,.ai-cert{order:8; margin-top:22px} .ai-mpanel__foot{order:9; margin-top:24px}
}
@media (max-width:560px){ .ai-secs ol{columns:1} }
@media (max-width:520px){ .ai-mpanel__foot .btn{flex:1 1 100%} .ai-mpanel__nav{width:100%; margin:0} .ai-mpanel__nav .btn{flex:1 1 0} }

/* ---------- four-step check: the loop ---------- */
.ai-4band{background-image:@@DOTS@@}
.ai-4{display:grid; grid-template-columns:repeat(2,minmax(0,1fr)); gap:var(--gap) clamp(24px,3.4vw,48px); align-items:stretch}
.ai-4 > *{min-width:0}
.ai-wheel{position:relative; width:100%; max-width:548px; aspect-ratio:1; margin-inline:auto; align-self:center}
.ai-wheel__c{position:absolute; inset:0; width:100%; height:100%; overflow:visible}
.ai-arc path{fill:none; stroke:var(--teal); stroke-width:3; stroke-linecap:round; stroke-linejoin:round; opacity:.5; transition:opacity .3s, stroke-width .3s}
.ai-arc path:first-child{stroke-dasharray:1; stroke-dashoffset:0}
.ai-wheel[data-cur="0"] .ai-arc--0 path,.ai-wheel[data-cur="1"] .ai-arc--1 path,.ai-wheel[data-cur="2"] .ai-arc--2 path,.ai-wheel[data-cur="3"] .ai-arc--3 path{stroke:var(--slate); stroke-width:4.6; opacity:1}
.ai-wheel[data-cur="0"] .ai-arc--0 path:first-child,.ai-wheel[data-cur="1"] .ai-arc--1 path:first-child,.ai-wheel[data-cur="2"] .ai-arc--2 path:first-child,.ai-wheel[data-cur="3"] .ai-arc--3 path:first-child{animation:ai-draw .9s var(--ease) both}
@keyframes ai-draw{from{stroke-dashoffset:1}}
.ai-wheel__mid{position:absolute; left:34%; right:34%; top:50%; transform:translateY(-50%); display:grid; text-align:center; pointer-events:none; line-height:1.2; gap:3px}
.ai-wheel__mid b{font-family:var(--hand); font-size:1.3rem; line-height:1.1; color:var(--logo-teal)}
.ai-wheel__mid span{font-family:var(--hand); font-size:.95rem; color:var(--ink-soft)}
.ai-node{position:absolute; width:33%; font:inherit; text-align:center; background:#fff; color:var(--slate); border:2px solid var(--slate); border-radius:16px; padding:10px 11px 13px; cursor:pointer; box-shadow:5px 5px 0 var(--teal); transition:translate .25s var(--ease), background .25s, box-shadow .25s; display:flex; flex-direction:column; align-items:center; gap:3px}
.ai-node__n{width:32px; height:32px; display:grid; place-items:center; font-family:var(--hand); font-weight:700; background:@@RING_TEAL@@ center/100% 100% no-repeat}
.ai-node b{font-family:var(--hand); font-size:1.3rem; line-height:1.1; text-transform:uppercase; letter-spacing:.04em}
.ai-node small{font-size:.94rem; line-height:1.32; color:var(--ink-soft)}
.ai-node:hover{translate:0 -3px}
.ai-node[aria-pressed="true"]{background:var(--mint); box-shadow:5px 5px 0 var(--slate)}
.ai-node[aria-pressed="true"] small{color:var(--slate)}
.ai-node[aria-pressed="true"] .ai-node__n{background-image:@@RING_SLATE@@}
.ai-node--0{left:33.5%; top:0} .ai-node--2{left:33.5%; bottom:0}
.ai-node--1{right:0; top:50%; transform:translateY(-50%)} .ai-node--3{left:0; top:50%; transform:translateY(-50%)}
.ai-4card{display:flex; flex-direction:column; background:#fff; border:2px solid var(--slate); border-radius:var(--r-xl); padding:clamp(22px,2.8vw,36px); box-shadow:8px 8px 0 var(--teal)}
.ai-4details{flex:1; display:grid}
.ai-4d{grid-area:1/1}
.ai-4d:not([hidden]){display:flex; flex-direction:column; animation:ai-note .45s var(--ease) both}
.ai-4d__then{margin:auto 0 0; display:grid; grid-template-columns:auto minmax(0,1fr); gap:2px 10px; align-items:baseline; padding:12px 16px; border-radius:14px; background:var(--mist); border:1.5px dashed rgba(29,65,78,.35); font-family:var(--hand); line-height:1.35}
.ai-4d__then span{font-size:.95rem; color:var(--ink-soft)}
.ai-4d__then b{font-size:1.1rem; text-transform:uppercase; letter-spacing:.04em; color:var(--logo-teal)}
.ai-4d__then em{grid-column:1/-1; font-style:normal; font-size:1rem; color:var(--slate)}
@keyframes ai-note{from{transform:translateY(10px)}}
.ai-4d__k{display:flex; align-items:center; gap:14px; margin:0 0 14px; font-family:var(--mono); font-size:.74rem; letter-spacing:.1em; text-transform:uppercase; font-weight:600; color:var(--logo-teal)}
.ai-4d__n{width:64px; height:64px; display:grid; place-items:center; font-family:var(--hand); font-weight:700; font-size:2rem; letter-spacing:0; color:var(--logo-teal); background:@@RING_TEAL@@ center/100% 100% no-repeat}
.ai main .ai-4d h3{font-size:clamp(2.2rem,3.6vw,3.2rem); line-height:1; margin:0 0 .3em}
.ai-4d__q{font-family:var(--hand); font-weight:700; font-size:clamp(1.25rem,1.8vw,1.5rem); line-height:1.35; color:var(--logo-teal); margin:0 0 .7em}
.ai-4d__p{margin:0 0 20px; font-size:1.12rem; line-height:1.62}
.ai-4card__foot{position:relative; margin-top:auto; padding-top:22px; display:flex; align-items:center; justify-content:space-between; gap:14px}
.ai-4details{margin-bottom:22px}
.ai-4card__foot::before{content:""; position:absolute; left:0; right:0; top:0; height:10px; background:@@WAVE_TEAL@@ center/100% 100% no-repeat; opacity:.5}
.ai-4dots{display:flex; gap:8px}
.ai-4dots i{width:12px; height:12px; border-radius:50%; border:2px solid var(--slate); transition:background .25s}
.ai-4dots i.on{background:var(--mint)}
.ai-4note{display:grid; grid-template-columns:44px minmax(0,1fr); gap:14px; align-items:center; margin:calc(var(--gap) + 10px) 0 0; font-family:var(--hand); font-size:1.14rem; line-height:1.5}
.ai-4note svg{width:44px; height:40px; color:var(--teal)}
@media (max-width:1100px){ .ai-4{grid-template-columns:minmax(0,1fr)} }
@media (max-width:620px){
  .ai-wheel{max-width:400px}
  .ai-node{width:37%; padding:9px 6px 11px; border-radius:14px; box-shadow:4px 4px 0 var(--teal)}
  .ai-node small{display:none}
  .ai-node b{font-size:1.06rem}
  .ai-node--0,.ai-node--2{left:31.5%}
  .ai-wheel__mid{left:38%; right:38%}
  .ai-wheel__mid b{font-size:.95rem} .ai-wheel__mid span{display:none}
}

/* ---------- how it works ---------- */
.ai-steps{list-style:none; margin:0; padding:0; display:grid; grid-template-columns:repeat(4,minmax(0,1fr)); gap:var(--gap); counter-reset:h}
.ai-steps li{position:relative; margin:0; counter-increment:h; background:#fff; border:2px solid var(--slate); border-radius:var(--r-xl); padding:22px 22px 24px; box-shadow:6px 6px 0 var(--aqua); min-width:0}
.ai-steps li::before{content:counter(h); display:grid; place-items:center; width:58px; height:58px; margin-bottom:10px; font-family:var(--hand); font-weight:700; font-size:1.9rem; color:var(--logo-teal); background:@@RING_TEAL@@ center/100% 100% no-repeat}
.ai-steps li:not(:last-child)::after{content:""; position:absolute; right:calc(var(--gap) * -1 + 1px); top:42px; width:calc(var(--gap) + 6px); height:22px; z-index:2; background:url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 40 24'%3E%3Cpath d='M2 14C12 6 22 6 34 12M26 4l9 8-10 6' fill='none' stroke='%2313848f' stroke-width='3' stroke-linecap='round' stroke-linejoin='round'/%3E%3C/svg%3E") center/contain no-repeat}
.ai-steps h3{font-size:1.32rem; line-height:1.15; margin-bottom:.4em}
.ai-steps p{margin:0; color:var(--ink-soft); font-size:.97rem; line-height:1.5}
.ai-feat{display:grid; grid-template-columns:repeat(2,minmax(0,1fr)); gap:var(--gap) clamp(28px,4vw,56px); align-items:stretch; margin-top:clamp(36px,4.6vw,60px)}
.ai-feat > *{min-width:0}
.ai-feat .ai-media__img{aspect-ratio:1280/660}
.ai-shot__in{position:absolute; left:50%; top:0; transform:translateX(-50%); height:100%; min-width:100%; aspect-ratio:1280/660}
.ai-shot__in img{width:100%; height:100%; display:block}
.ai-mark{position:absolute; pointer-events:none; background:@@LOOP_MINT4@@ center/100% 100% no-repeat}
.ai-feat__txt{display:flex; flex-direction:column}
.ai-feat h3{font-size:clamp(1.5rem,2.4vw,2.1rem); margin:0 0 .5em}
.ai-flist{flex:1; list-style:none; padding:0; margin:0; display:grid; align-content:space-between}
.ai-flist li{margin:0; display:grid; grid-template-columns:132px minmax(0,1fr); gap:14px; align-items:baseline; padding:11px 0; border-top:1px solid var(--line)}
.ai-flist li:last-child{padding-bottom:0}
.ai-flist b{font-family:var(--hand); font-size:1.08rem; color:var(--logo-teal)}
.ai-flist span{font-size:.97rem; line-height:1.5}
.ai-flist .x b{justify-self:start; display:inline-block; background:var(--coral); color:var(--slate); padding:1px 8px; border-radius:6px}
@media (max-width:1100px){ .ai-steps{grid-template-columns:repeat(2,minmax(0,1fr))} .ai-steps li:nth-child(2)::after{display:none} }
@media (max-width:860px){ .ai-feat{grid-template-columns:minmax(0,1fr)} .ai-feat .ai-media{margin-right:8px} .ai-feat__txt{margin-top:10px} }
@media (max-width:560px){ .ai-steps{grid-template-columns:minmax(0,1fr)} .ai-steps li::after{display:none} .ai-flist li{grid-template-columns:minmax(0,1fr); gap:2px} }

/* ---------- educators / parents / privacy ---------- */
.ai-trio{display:grid; grid-template-columns:repeat(3,minmax(0,1fr)); gap:var(--gap); align-items:stretch}
.ai-card{display:flex; flex-direction:column; gap:12px; border-radius:var(--r-xl); padding:var(--pad-card); background:rgba(255,255,255,.05); border:1.5px solid var(--line-dark); min-width:0}
.ai main .ai-card h3{font-size:1.6rem; line-height:1.12; margin:0; color:#fff}
.ai-card p{margin:0; color:#fff; line-height:1.55}
.ai-card .btns{margin-top:auto; padding-top:10px}
.ai-card--edu{background:var(--mint); color:var(--slate); border-color:var(--mint)}
.ai main .ai-card--edu h3,.ai-card--edu p{color:var(--slate)}
.ai-flow{list-style:none; margin:4px 0 0; padding:12px 0 0; border-top:1.5px dashed rgba(29,65,78,.4); display:grid; gap:5px; counter-reset:f}
.ai-flow li{counter-increment:f; margin:0; display:grid; grid-template-columns:28px minmax(0,1fr); gap:10px; align-items:center; font-family:var(--hand); font-weight:700; font-size:1.02rem; line-height:1.2}
.ai-flow li::before{content:counter(f); width:28px; height:28px; display:grid; place-items:center; font-size:.95rem; background:@@RING_SLATE@@ center/100% 100% no-repeat}
.ai-card blockquote{flex:1; display:grid; align-content:center; margin:0; font-family:var(--hand); font-size:clamp(1.14rem,1.55vw,1.3rem); line-height:1.5; color:#fff; padding:18px 20px; border-radius:16px; background:rgba(255,255,255,.06); border:1.5px dashed rgba(209,254,255,.4)}
.ai-card small{color:var(--aqua); font-size:.92rem; line-height:1.45}
@media (max-width:1100px){
  .ai-trio{grid-template-columns:repeat(2,minmax(0,1fr))}
  .ai-card--edu{grid-column:1/-1; display:grid; grid-template-columns:minmax(0,7fr) minmax(0,5fr); column-gap:clamp(24px,3.4vw,48px); align-items:start}
  .ai-card--edu > :is(h3,p){grid-column:1}
  .ai-card--edu .ai-flow{grid-column:2; grid-row:1 / span 2; align-self:start; margin:0; padding:0; border:0; gap:10px}
  .ai-card--edu .btns{grid-column:2; grid-row:3; align-self:end; padding-top:0}
}
@media (max-width:760px){
  .ai-trio{grid-template-columns:minmax(0,1fr)}
  .ai-card--edu{display:flex}
  .ai-card--edu .ai-flow{margin:4px 0 0; padding:12px 0 0; border-top:1.5px dashed rgba(29,65,78,.4); gap:5px}
  .ai-card--edu .btns{padding-top:10px; align-self:stretch}
}

/* ---------- connects ---------- */
.ai-conn{display:grid; grid-template-columns:minmax(0,7fr) minmax(0,5fr); gap:var(--gap); align-items:stretch}
.ai-conn__r{display:grid; gap:var(--gap); min-width:0}
.ai-cc{display:grid; background:#fff; border:2px solid var(--slate); border-radius:var(--r-xl); overflow:hidden; text-decoration:none; color:var(--slate); box-shadow:6px 6px 0 var(--teal); transition:transform .2s var(--ease), box-shadow .2s; min-width:0}
.ai-cc:hover{transform:translate(-2px,-3px); box-shadow:9px 9px 0 var(--mint)}
.ai-cc__img{position:relative; overflow:hidden; background:var(--slate)}
.ai-cc__img img{position:absolute; inset:0; width:100%; height:100%; object-fit:cover; transition:transform .5s var(--ease)}
.ai-cc:hover .ai-cc__img img{transform:scale(1.04)}
.ai-cc__b{display:flex; flex-direction:column; gap:6px; padding:18px 22px 20px; min-width:0}
.ai-cc small{font-family:var(--mono); font-size:.72rem; letter-spacing:.08em; text-transform:uppercase; font-weight:600; color:var(--logo-teal)}
.ai-cc b{font-family:var(--hand); font-size:1.4rem; line-height:1.15}
.ai-cc__t{font-size:.98rem; color:var(--ink-soft); line-height:1.5}
.ai-cc__go{margin-top:auto; padding-top:6px; font-weight:800; font-family:var(--display); color:var(--logo-teal)}
.ai-cc__go i{font-style:normal; display:inline-block; transition:transform .2s var(--ease)}
.ai-cc:hover .ai-cc__go i{transform:translateX(4px)}
/* lead card: the picture takes whatever height the two cards beside it leave */
.ai-cc--lead{grid-template-rows:minmax(180px,1fr) auto}
.ai-cc--lead .ai-cc__img{border-bottom:2px solid var(--slate)}
.ai-cc--lead b{font-size:1.7rem}
.ai-cc--side{grid-template-columns:minmax(0,34%) minmax(0,1fr)}
.ai-cc--side .ai-cc__img{border-right:2px solid var(--slate)}
@media (max-width:860px){ .ai-conn{grid-template-columns:minmax(0,1fr)} .ai-cc{margin-right:6px} .ai-cc--lead{grid-template-rows:auto auto} .ai-cc--lead .ai-cc__img{aspect-ratio:16/9} }
@media (max-width:480px){ .ai-cc--side{grid-template-columns:minmax(0,30%) minmax(0,1fr)} .ai-cc__b{padding:16px 16px 18px} }

/* ---------- support ---------- */
.ai-sup{display:grid; grid-template-columns:repeat(3,minmax(0,1fr)); gap:14px}
.ai-sl{display:grid; grid-template-rows:subgrid; grid-row:span 3; row-gap:6px; padding:18px 20px 20px; border-radius:16px; background:rgba(255,255,255,.05); border:1px solid var(--line-dark); text-decoration:none; color:#fff; min-width:0; transition:border-color .2s, background .2s, transform .2s var(--ease)}
.ai-sl:hover{border-color:var(--mint); background:rgba(255,255,255,.08); transform:translateY(-2px)}
.ai-sl b{font-family:var(--hand); font-size:1.22rem; line-height:1.2}
.ai-sl strong{font-family:var(--mono); font-weight:600; font-size:.92rem; line-height:1.4; color:var(--mint); overflow-wrap:anywhere}
.ai-sl span{font-size:.96rem; color:rgba(255,255,255,.88); line-height:1.45}
.ai-tid{grid-column:1/-1; display:grid; grid-template-columns:minmax(0,4fr) minmax(0,8fr) auto; gap:10px clamp(18px,2.4vw,32px); align-items:center; padding:18px 22px; border-radius:16px; background:rgba(21,255,200,.1); border:1.5px solid rgba(21,255,200,.5); text-decoration:none; color:#fff; transition:background .2s, transform .2s var(--ease)}
.ai-tid:hover{background:rgba(21,255,200,.16); transform:translateY(-2px)}
.ai-tid b{display:block; font-family:var(--hand); font-size:1.5rem; line-height:1.1}
.ai-tid strong{display:block; margin-top:4px; font-family:var(--mono); font-weight:600; font-size:.92rem; color:var(--mint)}
.ai-tid span{font-size:1rem; line-height:1.5}
.ai-tid i{font-style:normal; width:44px; height:44px; border-radius:50%; display:grid; place-items:center; background:var(--mint); color:var(--slate); font-weight:800}
.ai-sup-head p:not(.eyebrow){margin:.5em 0 0; color:#fff; font-size:var(--fs-lede); font-weight:500}
@media (max-width:960px){ .ai-sup{grid-template-columns:repeat(2,minmax(0,1fr))} .ai-tid{grid-template-columns:minmax(0,1fr) auto} .ai-tid span{grid-column:1; grid-row:2} .ai-tid i{grid-row:1 / span 2} }
@media (max-width:560px){ .ai-sup{grid-template-columns:minmax(0,1fr); gap:10px} .ai-sl{display:flex; flex-direction:column; gap:5px} }

/* ---------- final CTA ---------- */
.ai-cta{text-align:center}
.ai main section .ai-cta h2{font-size:clamp(2.4rem,6.4vw,5.6rem); line-height:1.02; margin:0 0 .25em}
.ai-cta .mk{background-image:@@BRUSH_WHITE@@}
.ai-cta p{font-family:var(--hand); font-size:clamp(1.1rem,1.6vw,1.35rem); max-width:none; margin:0}
.ai-cta .btns{justify-content:center; margin-top:26px}
.ai-cta__url{display:block; margin-top:18px; font-family:var(--mono); font-size:.9rem; letter-spacing:.06em; color:var(--slate)}
@media (prefers-reduced-motion:reduce){ .ai-arc path:first-child,.ai-4d{animation:none!important} }
'''

JS = r'''
(function(){
  var d = document, reduce = matchMedia('(prefers-reduced-motion: reduce)').matches;
  /* four-step check: walk the loop. It plays through once when it first comes into view, then rests. */
  var wheel = d.querySelector('.ai-wheel'), box = d.querySelector('.ai-4');
  if(wheel && box){
    var nodes = [].slice.call(box.querySelectorAll('.ai-node')), dets = [].slice.call(box.querySelectorAll('.ai-4d')), dots = [].slice.call(box.querySelectorAll('.ai-4dots i')),
        next = box.querySelector('[data-4next]'), nm = box.querySelector('[data-4name]'), names = nodes.map(function(n){ return n.querySelector('b').textContent; }), cur = 0, timer = null, left = 0;
    function pick(i){ cur = i; wheel.setAttribute('data-cur', i); nodes.forEach(function(n, k){ n.setAttribute('aria-pressed', String(k === i)); }); dets.forEach(function(x, k){ x.hidden = k !== i; }); dots.forEach(function(x, k){ x.classList.toggle('on', k <= i); }); if(nm) nm.textContent = names[(i + 1) % names.length]; }
    function stop(){ if(timer){ clearInterval(timer); timer = null; } left = 0; }
    nodes.forEach(function(n, k){ n.addEventListener('click', function(){ stop(); pick(k); }); });
    if(next) next.addEventListener('click', function(){ stop(); pick((cur + 1) % nodes.length); });
    box.addEventListener('pointerenter', stop); box.addEventListener('focusin', stop);
    if(!reduce && 'IntersectionObserver' in window){
      var io = new IntersectionObserver(function(es){ es.forEach(function(e){ if(!e.isIntersecting) return; io.disconnect(); left = nodes.length; timer = setInterval(function(){ if(!box.isConnected || left <= 0){ stop(); return; } pick((cur + 1) % nodes.length); left--; if(left <= 0) stop(); }, 3400); }); }, {threshold:.55});
      io.observe(box);
    }
  }
  /* module map: Back / Next inside a panel, and links from other pages (#mod-m2) */
  var map = d.querySelector('.ai-map'), mods = d.getElementById('modules');
  function openMod(k, scroll){ var t = d.getElementById('tab-mod-' + k); if(!t) return; t.click(); if(scroll && map){ var top = map.getBoundingClientRect().top; if(top < 96 || top > innerHeight * .6) window.scrollTo({top: window.pageYOffset + top - 110, behavior: reduce ? 'auto' : 'smooth'}); } }
  [].forEach.call(d.querySelectorAll('[data-mod-go]'), function(b){ b.addEventListener('click', function(){ openMod(b.getAttribute('data-mod-go'), true); }); });
  window.addEventListener('hashchange', function(){ var m = /^#mod-(\w+)$/.exec(location.hash); if(m) openMod(m[1], false); });
  /* keep the selected stop visible when the map scrolls (narrow screens) */
  if(map){ map.addEventListener('click', function(e){ var b = e.target.closest('[role="tab"]'); if(!b || map.scrollWidth <= map.clientWidth + 4) return; map.scrollTo({left: b.offsetLeft - map.clientWidth/2 + b.offsetWidth/2, behavior: reduce ? 'auto' : 'smooth'}); }); }
})();
'''


def build():
    DOTS = 'radial-gradient(rgba(19,132,143,.2) 1.1px, transparent 1.5px) 0 0/18px 18px'
    DOTS_DARK = 'radial-gradient(rgba(209,254,255,.11) 1.1px, transparent 1.5px) 0 0/18px 18px'
    css = CSS
    for k, v in {
        'BRUSH_TEAL': brush('#13848f', '0.85'), 'BRUSH_MINT': brush('#15ffc8', '0.9'), 'BRUSH_WHITE': brush('#ffffff', '0.85'),
        'LOOP_MINT4': loop('#15ffc8', 4), 'LOOP_MINT': loop('#15ffc8'), 'LOOP_TEAL': loop('#13848f'),
        'WAVE_TEAL': wave('#13848f'), 'WAVE_MINT': wave('#15ffc8'),
        'RING_TEAL': ring('#13848f'), 'RING_MINT': ring('#15ffc8'), 'RING_SLATE': ring('#1d414e'),
        'DOTS_DARK': DOTS_DARK, 'DOTS': DOTS,
    }.items():
        css = css.replace(f'@@{k}@@', v)
    assert '@@' not in css

    panels = ''.join(mod_panel(m, i) for i, m in enumerate(MODS))
    anchors = ''.join(f'<span class="ai-anchor" id="mod-{m["k"]}"></span>' for m in MODS)
    lines = SUPPORT[:6]
    sup = ''.join(f'<a class="ai-sl" href="{u}" target="_blank" rel="noopener"><b>{esc(n)}</b><strong>{esc(num)}</strong><span>{esc(dsc)}</span></a>' for n, num, dsc, u in lines)
    tn, tnum, tdsc, tu = SUPPORT[6]
    tid = f'<a class="ai-tid" href="{tu}" target="_blank" rel="noopener"><div><b>{esc(tn)}</b><strong>{esc(tnum)}</strong></div><span>{esc(tdsc)}</span><i aria-hidden="true">&#8599;</i></a>'
    def cc(c, kind):
        t, dsc, h, im, tag, pos = c
        return (f'<a class="ai-cc ai-cc--{kind}" href="{h}"><span class="ai-cc__img">{img(im, "", style="object-position:" + pos)}</span>'
                f'<span class="ai-cc__b"><small>{esc(tag)}</small><b>{esc(t)}</b><span class="ai-cc__t">{esc(dsc)}</span><span class="ai-cc__go">Go <i aria-hidden="true">&rarr;</i></span></span></a>')
    conn = cc(CONNECT[0], 'lead') + '<div class="ai-conn__r">' + cc(CONNECT[1], 'side') + cc(CONNECT[2], 'side') + '</div>'
    goals = ''.join(f'<li><span>{esc(g)}</span></li>' for g in GOALS)
    arrow_r = '<svg viewBox="0 0 60 54" aria-hidden="true"><path d="M6 8C8 30 22 42 50 40M40 30l11 10-13 8" fill="none" stroke="currentColor" stroke-width="3.2" stroke-linecap="round" stroke-linejoin="round"/></svg>'
    arrow = '<svg viewBox="0 0 60 54" aria-hidden="true"><path d="M52 50C36 44 18 30 10 8M4 18l6-12 11 7" fill="none" stroke="currentColor" stroke-width="3.2" stroke-linecap="round" stroke-linejoin="round"/></svg>'
    settings = (f'<figure class="ai-media ai-media--shot">{BAR}<div class="ai-media__img"><div class="ai-shot__in">'
                f'{img("ai-shot-settings", "Screenshot of the training’s Settings and privacy panel, with text size and font options")}'
                '<span class="ai-mark" style="left:25%;top:36%;width:33%;height:28%" aria-hidden="true"></span></div></div>'
                '<figcaption>Settings &amp; privacy</figcaption></figure>')

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
      <div class="btns">{btn('Start the training', TRAIN, 'mint')}{btn('Group access for educators', EDU, 'ghost')}</div>
      <div class="ai-facts"><span>Free</span><span>6 modules</span><span>Self-paced</span><span>Progress saves</span><span>Certificate</span></div>
    </div>
    <div class="ai-stage">
      {frame('ai-shot-home', 'Screenshot of the training’s home screen: “SafeBAE AI Literacy Training” beside a drawing of a billboard with a binary smiley face and a name tag that reads “Hello, my name is AI”')}
      <div class="ai-phone">{img('ai-m-four', 'The training on a phone, open to the Four-Step Check')}</div>
      <span class="ai-note">{arrow}Media Literacy Week, Oct 26–30</span>
    </div>
  </div>
</section>

<section class="band ai-dots">
  <div class="wrap">
    <div class="section-head"><div><p class="eyebrow">Who it’s for</p><h2>Made for high school and college students</h2>
      <p class="lede">The training is designed for high school and college students, though anyone 13 or older may find it useful. It builds the skills to understand AI and how it affects your relationships, your safety and the decisions you make.</p></div></div>
    <div class="ai-who reveal">
      {media('ai-illo-hello', 'illo', 'A billboard showing a smiling face drawn in binary code, with a name tag that reads “Hello, my name is AI.”', 'Illustrations from the training')}
      <div class="ai-goals">
        <h3>By the end, you will be able to:</h3>
        <ol>{goals}</ol>
      </div>
    </div>
    <figure class="ai-noteq reveal">
      <figcaption>A note before you begin</figcaption>
      <blockquote>“This program is not about shaming anyone for using AI. AI can be a helpful tool for creativity, learning, and fun. However, like any tool, it’s important to know how to use it thoughtfully.”</blockquote>
    </figure>
  </div>
</section>

<section class="band band--deep ai-mods" id="modules">
  {anchors}
  <div class="wrap">
    <div class="section-head"><div><p class="eyebrow">Chapter map &middot; 57 screens</p><h2>Six modules, in order</h2></div></div>
    <div data-tabs="ai-mod">
      {map_html()}
      {panels}
    </div>
  </div>
</section>

<section class="band band--aqua ai-4band" id="four-step">
  <div class="wrap">
    <div class="section-head"><div><p class="eyebrow">A skill from Module 1</p><h2>Pause. Question. Check. Ask.</h2>
      <p class="lede">The Four-Step Check gives you a simple way to decide what to trust, what to verify, and when an AI answer is not enough.</p></div></div>
    {four_step()}
    <p class="ai-4note">{arrow_r}<span>These four steps are for answers. An AI agent takes actions, so the check has to come before it acts. Module 2 builds on it.</span></p>
  </div>
</section>

<section class="band band--paper" id="how">
  <div class="wrap">
    <div class="section-head"><div><p class="eyebrow">How it works</p><h2>Create an account and go at your own pace</h2></div></div>
    <ol class="ai-steps reveal">
      <li><h3>Create a free account</h3><p>Your name, your school or organization, a class code if someone gave you one, your email and a password. You confirm you are 13 or older.</p></li>
      <li><h3>Go at your own pace</h3><p>Your progress is saved to your account, so you can stop any time and pick up where you left off on any phone or computer.</p></li>
      <li><h3>Switch devices with a resume code</h3><p>Pick up on a phone, tablet or school computer. Your progress travels; anything you wrote stays on the device where you wrote it.</p></li>
      <li><h3>Get your certificate</h3><p>A one-page certificate you can print or download. It unlocks once you have finished every screen and every activity.</p></li>
    </ol>
    <div class="ai-feat reveal">
      {settings}
      <div class="ai-feat__txt">
        <h3>Built into every screen</h3>
        <ul class="ai-flist">
          <li class="x"><b>Quick Exit</b><span>A Quick Exit button sits in the header of every screen.</span></li>
          <li><b>Support</b><span>The Support button lists free crisis lines and SafeBAE resources.</span></li>
          <li><b>Text size</b><span>Small, Default, Large or Extra large.</span></li>
          <li><b>Font</b><span>Handwritten or Standard. Standard is a plainer font, for anyone who finds the handwritten one harder to read.</span></li>
          <li><b>Activities</b><span>Quick checks, sorting activities, simulated feeds, scenarios and a personal AI boundaries plan.</span></li>
          <li><b>Completion record</b><span>A printable record of which screens and activities were completed, and how much time was spent.</span></li>
        </ul>
      </div>
    </div>
  </div>
</section>

<section class="band band--slate" id="adults">
  <div class="wrap">
    <div class="section-head"><div><p class="eyebrow">For adults</p><h2>For educators and parents</h2></div></div>
    <div class="ai-trio reveal">
      <div class="ai-card ai-card--edu">
        <h3>Group access for educators</h3>
        <p>Assign the training to your students and follow their progress. Tell SafeBAE about your group; SafeBAE reviews each registration and emails you a class code to give your students.</p>
        <p>Registering creates an ordinary account for the training, so you can go through it yourself straight away.</p>
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
  </div>
</section>

<section class="band band--mist" id="connects">
  <div class="wrap">
    <div class="section-head"><div><p class="eyebrow">More from SafeBAE</p><h2>Where it connects to SafeBAE’s other tools</h2></div></div>
    <div class="ai-conn reveal">{conn}</div>
  </div>
</section>

{vibe_band(VIBE_TEXT)}

<section class="band band--deep" id="support">
  <div class="wrap">
    <div class="section-head ai-sup-head"><div><p class="eyebrow">Listed inside the training</p><h2>Support is available</h2><p>Free resources, most open any hour. If you are in immediate danger, call 911.</p></div><button class="btn btn--coral section-head__act" data-open-help>All hotlines</button></div>
    <div class="ai-sup reveal">{sup}{tid}</div>
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
         head_extra=f'<style>{VIBE_CSS}{css}</style>', scripts=f'<script>{JS}</script>')


if __name__ == '__main__':
    build()
