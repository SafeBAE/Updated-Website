"""SUPPORT & RIGHTS group (v3): survivor-support, title-ix.
myths-facts, faq, posters and blog build from pages_support2."""
from lib import *
from films_common import POSTERS_ZIP
import datetime

WPU = 'https://www.safebae.org/wp-content/uploads/'
BOOKSHOP = 'https://bookshop.org/shop/SafeBAE'


def crumbs(*items):
    out = []
    for t, h in items:
        out.append(a(esc(t), h) if h else f'<span>{esc(t)}</span>')
    return '<nav class="crumbs" aria-label="Breadcrumb">' + '<span>/</span>'.join(out) + '</nav>'


def esc_note():
    return ('<p class="sp-esc"><span>Need to leave quickly?</span> <span>Press <span class="kbd">Esc</span> twice</span> '
            '<span>or</span> <button type="button" data-quick-exit>Quick exit</button></p>')


def month(d):
    return datetime.date.fromisoformat(d).strftime('%b %Y')


def post_row(title, date, link, thumb):
    return (f'<a class="sp-post" href="{esc(link)}" target="_blank" rel="noopener">'
            f'<span class="sp-post__img">{img(thumb, "")}</span>'
            f'<span class="sp-post__txt"><time datetime="{date}">{month(date)}</time><b>{esc(title)}</b></span>'
            f'<i class="go" aria-hidden="true">&#8599;</i></a>')


def next_cards(items):
    out = []
    for kicker, title, desc, href in items:
        ext = href.startswith('http')
        t = ' target="_blank" rel="noopener"' if ext else ''
        out.append(f'<a href="{esc(href)}"{t}><small>{esc(kicker)}</small><b>{esc(title)}</b><span>{esc(desc)}</span>'
                   f'<i class="go" aria-hidden="true">{"&#8599;" if ext else "&rarr;"}</i></a>')
    return f'<div class="sp-next sp-next--{len(items)}">' + ''.join(out) + '</div>'


def player(slides, label, cls='', pid='', interval=5200):
    """slides: list of (image, caption, alt)."""
    sl = ''.join(f'<div class="player__slide{" on" if i == 0 else ""}" data-cap="{esc(c)}">{img(n, alt, loading="eager" if i == 0 else "lazy")}</div>'
                 for i, (n, c, alt) in enumerate(slides))
    i = f' id="{pid}"' if pid else ''
    return (f'<div class="player {cls}"{i} data-player data-zoom data-interval="{interval}" aria-roledescription="carousel" aria-label="{esc(label)}">'
            f'<div class="player__bar"><i></i></div>{sl}<div class="player__ctl"><button type="button" data-prev aria-label="Previous slide">&#8249;</button>'
            f'<span class="player__cap"></span><button type="button" data-next aria-label="Next slide">&#8250;</button></div></div>')


def vibe_band(title='Worried you, or a friend, crossed a line?'):
    """Vibe Check as a full teal band (compact: phone, text, actions)."""
    return f'''<section class="band band--teal band--tight sp-vibe" id="vibe-check">
  <div class="wrap sp-vibe__grid">
    <div class="sp-vibe__phone" aria-hidden="true"><div class="sp-phone">{img('vc-screen', '')}</div></div>
    <div class="sp-vibe__txt">
      <p class="sp-vibe__mark"><span class="daisy" aria-hidden="true"></span>Vibe Check by SafeBAE</p>
      <h2>{esc(title)}</h2>
      <p>CheckYourVibe.org is a free, anonymous reflection tool for young people who are questioning whether they, or a friend, may have crossed a boundary or caused harm. No names, no accounts, and nothing is stored.</p>
    </div>
    <div class="btns sp-vibe__act">{btn('Open Vibe Check', 'https://checkyourvibe.org/', 'mint')}{btn('How it works', 'vibe-check.html', 'white', arrow=True)}</div>
  </div>
</section>'''


def give_band_calm():
    """The shared donate band with a slate button: on Survivor Support, coral stays with the support actions."""
    return f'''<section class="band band--aqua band--tight"><div class="wrap give">
<div><p class="eyebrow">Your donation goes a long way</p><h2 style="margin:0 0 .3em">Keep prevention free for every student.</h2><p class="lede" style="margin:0">Your donation makes an immediate impact by keeping consent education and resources free for students and schools across the US.</p></div>
<div class="btns" style="justify-content:flex-end">{btn('Donate today', 'donate.html', 'slate', arrow=True)}{btn('Give monthly', 'donate.html#give', 'ghost')}</div>
</div></section>'''


SP_CSS = '''
.sp-esc{display:flex; flex-wrap:wrap; align-items:center; gap:6px 8px; margin:18px 0 0; font-size:.9rem; font-weight:600}
.sp-esc .kbd{font-size:.78rem; padding:1px 6px}
.sp-esc button{font:inherit; font-size:.88rem; font-weight:800; background:transparent; color:var(--slate); border:1.5px solid var(--slate); border-radius:6px; padding:3px 10px; cursor:pointer; transition:background .2s, color .2s}
.sp-esc button:hover{background:var(--slate); color:#fff}
@media (pointer:coarse){.sp-esc button{min-height:44px; padding-inline:14px}}
/* blog post rows */
.sp-post{display:grid; grid-template-columns:clamp(104px,13vw,150px) minmax(0,1fr) auto; gap:clamp(12px,1.6vw,20px); align-items:center; padding:12px 0; border-bottom:1px solid var(--line); text-decoration:none; color:inherit; min-width:0}
.sp-post__img{display:block; aspect-ratio:40/21; border-radius:10px; overflow:hidden; background:var(--slate)}
.sp-post__img img{width:100%; height:100%; object-fit:cover; transition:transform .5s var(--ease)}
.sp-post:hover .sp-post__img img{transform:scale(1.05)}
.sp-post__txt{display:block; min-width:0}
.sp-post time{display:block; font-family:var(--mono); font-size:.7rem; letter-spacing:.08em; text-transform:uppercase; color:var(--logo-teal); font-weight:600}
.sp-post b{display:block; font-family:var(--display); font-stretch:104%; font-weight:800; font-size:1.06rem; line-height:1.22; margin-top:3px; text-wrap:pretty}
.sp-post:hover b{text-decoration:underline; text-decoration-color:var(--mint); text-decoration-thickness:3px; text-underline-offset:3px}
.sp-post .go{width:34px; height:34px; border-radius:50%; display:grid; place-items:center; background:var(--aqua); color:var(--logo-teal); font-style:normal; font-weight:800; transition:background .2s, transform .2s var(--ease)}
.sp-post:hover .go{background:var(--mint); color:var(--slate); transform:translate(2px,-2px)}
:is(.band--slate,.band--deep) .sp-post{border-color:var(--line-dark)}
:is(.band--slate,.band--deep) .sp-post time{color:var(--mint)}
:is(.band--slate,.band--deep) .sp-post b{color:#fff}
:is(.band--slate,.band--deep) .sp-post .go{background:rgba(255,255,255,.1); color:var(--mint)}
:is(.band--slate,.band--deep) .sp-post:hover .go{background:var(--mint); color:var(--slate)}
/* onward cards */
.sp-next{display:grid; grid-template-columns:repeat(4,minmax(0,1fr)); gap:var(--gap)}
.sp-next--3{grid-template-columns:repeat(3,minmax(0,1fr))}
.sp-next a{display:grid; grid-template-columns:minmax(0,1fr) auto; grid-template-rows:auto auto 1fr; gap:6px 16px; padding:var(--pad-card); border-radius:var(--r-xl); background:#fff; border:1px solid var(--line); text-decoration:none; color:var(--slate); transition:transform .2s var(--ease), box-shadow .2s var(--ease); min-width:0}
.sp-next a:hover{transform:translateY(-3px); box-shadow:var(--shadow-soft)}
.sp-next small{grid-column:1/-1; font-family:var(--mono); font-size:.72rem; letter-spacing:.1em; text-transform:uppercase; color:var(--logo-teal); font-weight:600}
.sp-next b{grid-column:1; font-family:var(--display); font-stretch:108%; font-size:1.45rem; line-height:1.1; color:var(--logo-teal)}
.sp-next span{grid-column:1; font-size:.98rem; color:var(--ink-soft); line-height:1.5}
.sp-next .go{grid-column:2; grid-row:2 / span 2; align-self:end; width:38px; height:38px; border-radius:50%; display:grid; place-items:center; background:var(--aqua); color:var(--logo-teal); font-style:normal; font-weight:800; transition:background .2s, transform .2s var(--ease)}
.sp-next a:hover .go{background:var(--mint); transform:translateX(3px)}
@media (max-width:900px){.sp-next,.sp-next--3{grid-template-columns:1fr}}
/* portrait slide decks: a true 4:5 slide over the control bar */
.player.sp-portrait::before{padding-top:calc(125% + 56px)}
.player.sp-portrait .player__slide img{background:#fff}
.player[data-zoom]{cursor:zoom-in}
.player{border-radius:var(--r-xl)}
.player__cap{font-size:.9rem}
/* focus rings that show on light and mint surfaces */
:is(.ss-hero,.ss-choke,.ss-way--lead,.tx-quiz,.band--mint) :focus-visible{outline-color:var(--teal)}
:is(.tx-quiz,.band--mint,.ss-way--lead,.ss-say__col--do) :focus-visible{outline-color:var(--slate)}
/* filter chips */
.sp-chips{display:flex; flex-wrap:wrap; gap:8px}
.sp-chips button{font:inherit; font-size:.92rem; font-weight:700; line-height:1.2; min-height:40px; padding:8px 15px; border-radius:999px; border:1.5px solid var(--line); background:#fff; color:var(--slate); cursor:pointer; transition:background .18s, color .18s, border-color .18s}
.sp-chips button:hover{border-color:var(--teal)}
.sp-chips button[aria-pressed="true"]{background:var(--slate); color:#fff; border-color:var(--slate)}
:is(.band--slate,.band--deep) .sp-chips button{background:transparent; color:#fff; border-color:rgba(209,254,255,.32)}
:is(.band--slate,.band--deep) .sp-chips button:hover{border-color:var(--mint)}
:is(.band--slate,.band--deep) .sp-chips button[aria-pressed="true"]{background:var(--mint); color:var(--slate); border-color:var(--mint)}
@media (pointer:coarse){.sp-chips button{min-height:44px}}
/* Vibe Check: full teal band */
.sp-vibe{overflow:hidden}
.sp-vibe__grid{display:grid; grid-template-columns:clamp(120px,12vw,160px) minmax(0,1fr) auto; gap:clamp(24px,4vw,56px); align-items:center}
.sp-vibe__phone{position:relative; align-self:stretch; min-height:150px}
.sp-phone{position:absolute; left:0; top:-14px; width:100%; aspect-ratio:390/800; border-radius:26px; border:7px solid #0b1f25; background:#0b1f25; overflow:hidden; transform:rotate(-5deg); box-shadow:0 30px 60px -24px rgba(0,0,0,.6)}
.sp-phone img{width:100%; height:100%; object-fit:cover; object-position:top}
.sp-vibe__mark{display:flex; align-items:center; gap:10px; font-family:var(--display); font-weight:900; font-stretch:115%; font-size:1.08rem; color:var(--mint); margin:0 0 12px}
.sp-vibe__mark .daisy{width:30px; height:30px}
.sp-vibe h2{color:#fff; font-size:clamp(1.7rem,3vw,2.5rem); margin:0 0 .35em}
.sp-vibe__txt p:last-child{color:#fff; margin:0}
.sp-vibe__act{flex-direction:column; align-items:stretch}
@media (max-width:980px){.sp-vibe__grid{grid-template-columns:minmax(0,1fr)} .sp-vibe__phone{display:none} .sp-vibe__act{flex-direction:row; align-items:center}}
.sp-lead{color:var(--ink-soft)}
@media (max-width:860px){main .section-head > .section-head__act{flex:1 1 100%!important; max-width:none}}
/* eyebrow colours: Logo Teal on light, mint on dark, white on SafeBAE Teal */
main .eyebrow{color:var(--logo-teal)}
main :is(.band--slate,.band--deep,.band--logo,.tx-hero,.tx-who) .eyebrow{color:var(--mint)}
main .band--teal .eyebrow{color:#fff}
.tx-hero .mk{background:none; color:var(--mint)}
.sp-hero{position:relative; overflow:hidden}
.sp-hero > .wrap{position:relative; z-index:1}
'''

# =====================================================================
# 1. SURVIVOR SUPPORT
# =====================================================================
HOTLINES_SRC = [
  dict(name='love is respect', sub='National Teen Dating Abuse Hotline', desc='Free, confidential 24/7 peer support for teens experiencing dating abuse.',
       acts=[('Text', 'LOVEIS to 22522', 'sms:22522', '22522'), ('Call', '1-866-331-9474', 'tel:18663319474', '1-866-331-9474')],
       site=('loveisrespect.org', 'https://www.loveisrespect.org'), tags='text call dating', h24=True),
  dict(name='RAINN', sub='National Sexual Assault Hotline', desc='Free, confidential 24/7 support for survivors of sexual assault and their loved ones.',
       acts=[('Call', '800-656-HOPE (4673)', 'tel:18006564673', '800-656-4673'), ('Text', 'HOPE to 64673', 'sms:64673', '64673')],
       site=('rainn.org', 'https://rainn.org/help-and-healing/hotline/'), tags='call text assault', h24=True),
  dict(name='Trevor Lifeline', sub='Crisis support for LGBTQ+ youth', desc='24/7 crisis counseling for LGBTQ+ youth from The Trevor Project.',
       acts=[('Text', 'START to 678-678', 'sms:678678', '678-678'), ('Call', '1-866-488-7386', 'tel:18664887386', '1-866-488-7386')],
       site=('thetrevorproject.org', 'https://www.thetrevorproject.org/get-help/'), tags='text call lgbtq crisis', h24=True),
  dict(name='988 Suicide & Crisis Lifeline', sub='24/7 suicide & crisis support', desc='Free, confidential 24/7 support for anyone in suicidal crisis or emotional distress.',
       acts=[('Call or text', '988', 'tel:988', '988'), ('Chat', 'Online at 988lifeline.org', 'https://988lifeline.org', None)],
       site=('988lifeline.org', 'https://988lifeline.org'), tags='call text crisis', h24=True),
  dict(name='Crisis Text Line', sub='Free 24/7 crisis counseling', desc='Text with a live crisis counselor about anything. Free, 24/7, confidential.',
       acts=[('Text', 'HOME to 741741', 'sms:741741', '741741'), ('Español', 'HOLA to 741741', 'sms:741741', '741741')],
       site=('crisistextline.org', 'https://www.crisistextline.org/'), tags='text crisis', h24=True),
  dict(name='Take Back The Night', sub='Free legal hotline', desc='A global movement to end sexual violence and support survivors, including free legal assistance.',
       acts=[('Call', '567-742-8837 (567-SHATTER)', 'tel:15677428837', '567-742-8837'), ('Online', 'Or complete the online form', 'https://takebackthenight.org/legal-assistance/', None)],
       site=('takebackthenight.org', 'https://takebackthenight.org/legal-assistance/'), tags='call legal assault', h24=False),
  dict(name='SAMHSA National Helpline', sub='Mental health & substance use', desc='Free, confidential 24/7 treatment referrals for mental health and substance use (English & Spanish).',
       acts=[('Call', '1-800-662-HELP (4357)', 'tel:18006624357', '1-800-662-4357')],
       site=('samhsa.gov', 'https://www.samhsa.gov/find-help/helplines/national-helpline'), tags='call crisis', h24=True),
  dict(name='Raliance', sub='Local rape crisis center directory', desc='A national directory to find the rape crisis center nearest you.',
       acts=[('Online', 'Browse the directory online', 'https://www.raliance.org/rape-crisis-centers/', None)],
       site=('raliance.org', 'https://www.raliance.org/rape-crisis-centers/'), tags='local assault', h24=False),
]
HL_FILTERS = [('all', 'All lines'), ('text', 'Text'), ('call', 'Call'), ('dating', 'Dating abuse'), ('assault', 'Sexual assault'),
              ('lgbtq', 'LGBTQ+ youth'), ('crisis', 'Crisis & mental health'), ('legal', 'Legal help'), ('local', 'Local help')]

CHOKE_SIGNS = ['Passed out, even briefly, or can’t remember part of what happened', 'Breathing changes, or pain or difficulty swallowing',
               'A hoarse, raspy or deeper voice, or trouble speaking', 'Neck pain or tenderness, or a mark or bruise on your neck',
               'Vision changes, ringing ears, or hearing changes', 'A headache, dizziness or lightheadedness',
               'Small red spots in your eyes or on your face', 'Lost bladder or bowel control']

PRACTICES = ['Re-affirm your self-worth', 'Practice mindfulness', 'Practice self care', 'Take the time you need to process',
             'Journal your thoughts', 'Express your feelings', 'Honor your needs', 'Forgive yourself', 'Reassure yourself',
             'Talk about your experiences', 'Focus on the present moment', 'Practice positive self talk']

WAYS = [('Start by believing.', 'The single best way to support a survivor is to believe them. Questioning their account, even out of shock, can be devastating and may keep them from ever opening up again.'),
        ('Listen more than you speak.', 'Show you’re engaged: make eye contact, don’t interrupt, and let them share as much or as little as they want. You don’t need details to be helpful. Never press for them.'),
        ('Validate their feelings.', 'If they minimize what happened (“other people have it worse”), gently remind them they’re allowed to be as upset as they need to be. No assault is “not bad enough” to matter.'),
        ('Meet immediate needs first.', 'Before processing emotions, make sure they feel physically safe and cared for. Something as simple as a glass of water, a snack, a cozy blanket, or asking if they want a hug can signal to their brain that they’re safe now.'),
        ('Let them lead.', 'Follow their choices about whether to report, who to tell, and how to cope. Reporting can be re-traumatizing, so never pressure them to. You can help them understand their options while respecting whatever they decide.')]
SAY = ['“I’m so sorry this happened to you.”', '“You are not alone. I know there are people that can help.”', '“How can I support you?”',
       '“It’s not your fault.”', '“I’m glad you felt safe to tell me so I can be here for you.”', '“You didn’t deserve that to happen to you.”']
DONT = ['“Why didn’t you just leave?”', '“Why were you there?”', '“If you kissed, you should have known something was going to happen.”',
        '“Were you drinking?”', '“What were you wearing?”', '“It’s going to be fine; just move on.”', '“If it was really a big deal, why didn’t you tell me sooner?”']

BS = 'https://bookshop.org/a/safebae/'
MEDIA = [
 ('books', 'Consent-themed picture books (children)', [
   ('Body Boundaries Make Me Stronger', 'Elizabeth Cole', 'https://www.goodreads.com/book/show/69706233'),
   ('C Is For Consent', 'Eleanor Morrison, illustrated by Faye Orlove', BS + '9780999890806'),
   ('Can I Give You A Squish?', 'Emily Neilson', BS + '9781984814777'),
   ('Consent Ninja', 'Mary Nhin', 'https://www.ninjalifehacks.tv/products/consent-ninja-paperback-book'),
   ('Don’t Hug Doug: (He Doesn’t Like It)', 'Carrie Finison, Daniel Wiseman', BS + '9781984813022'),
   ('Don’t Hug The Quokka!', 'Daniel Errico, Mia Powell', BS + '9781433837067'),
   ('Don’t Touch My Hair', 'Sharee Miller', BS + '9780316562584'),
   ('Hands Off, Harry!', 'Rosemary Wells', BS + '9780061921124'),
   ('Harrison P. Spader, Personal Space Invader', 'Christianne Jones, Cale Atkinson', BS + '9781515827238'),
   ('I Choose To Say No', 'Elizabeth Estrada', 'https://www.goodreads.com/en/book/show/59612653-i-choose-to-say-no'),
   ('Miles Is The Boss Of His Body', 'Samantha Kurtzman-Counter, Abbie Schiller, illustrated by Valentina Ventimiglia', BS + '9780989407137'),
   ('My Body Belongs To Me', 'Jill Starishevsky, illustrated by Angela Padrón', BS + '9798330921874'),
   ('We Ask Permission', 'Lydia Bowers, Isabel Muñoz', BS + '9781631986758'),
   ('Where Hands Go', 'Krystaelynne Sanders Diggs and Ananta Mohanta', 'https://ksdiggs.com/products/where-hands-go-an-introduction-to-safe-and-unsafe-touch'),
   ('Will Ladybug Hug?', 'Hilary Leung', BS + '9781338215601'),
   ('Yes! No!: A First Conversation About Consent', 'Megan Madison, Jessica Ralli, Isabel Roxas', BS + '9780593383322')]),
 ('docs', 'Documentaries', [
   ('A Thousand Girls Like Me', '', 'https://www.imdb.com/title/tt8804304/'), ('Allen v. Farrow', '', 'https://www.imdb.com/title/tt13990468/'),
   ('Aly Raisman: Darkness to Light', '', 'https://www.imdb.com/title/tt10098366/'), ('Athlete A', '', 'https://www.imdb.com/title/tt11905462/'),
   ('Audrie & Daisy', '', 'https://www.imdb.com/title/tt5278460/'), ('Dive', '', 'https://www.imdb.com/title/tt22656762/'),
   ('I Am Evidence', '', 'https://www.imdb.com/title/tt6794374/'), ('Jeffrey Epstein: Filthy Rich', '', 'https://www.imdb.com/title/tt12312250/'),
   ('On the Record', '', 'https://www.imdb.com/title/tt11394650/'), ('Phoenix Rising', '', 'https://www.imdb.com/title/tt17036612/'),
   ('Roll Red Roll', '', 'https://www.imdb.com/title/tt8092888/'), ('Surviving R. Kelly', '', 'https://www.imdb.com/title/tt8385496/'),
   ('The Hunting Ground', '', 'https://www.imdb.com/title/tt4185572/'), ('Untouchable', '', 'https://www.imdb.com/title/tt9358228/'),
   ('Victim/Suspect', '', 'https://www.imdb.com/title/tt24079788/'), ('What Haunts Us', '', 'https://www.imdb.com/title/tt6073760/')]),
 ('films', 'Films & TV (scripted)', [
   ('8th Grade', '', 'https://www.imdb.com/title/tt7014006/'), ('I May Destroy You', '', 'https://www.imdb.com/title/tt11204260/'),
   ('Moxie', '', 'https://www.imdb.com/title/tt6432466/'), ('Pink', '', 'https://www.imdb.com/title/tt5571734/'),
   ('Promising Young Woman', '', 'https://www.imdb.com/title/tt9620292/'), ('The Assistant', '', 'https://www.imdb.com/title/tt9000224/'),
   ('Unbelievable', '', 'https://www.imdb.com/title/tt7909970/')]),
 ('nonfiction', 'Nonfiction books & memoirs', [
   ('Talk To Your Boys', 'Joanna Schroeder and Christopher Pepper', BS + '9781523527311'),
   ('Abolition. Feminism. Now.', 'Angela Davis, Gina Dent, Erica Meiners, Beth Richie', BS + '9781642592580'),
   ('All About Love', 'Bell Hooks', BS + '9780060959470'),
   ('All Boys Aren’t Blue: A Memoir Manifesto', 'George M. Johnson', BS + '9781250895561'),
   ('Boys & Sex', 'Peggy Orenstein', BS + '9780062666987'),
   ('Catch and Kill', 'Ronan Farrow', BS + '9780316486644'),
   ('Consent on Campus: A Manifesto', 'Donna Freitas', BS + '9780190671150'),
   ('Credible', 'Deborah Tuerkheimer', BS + '9780063585195'),
   ('Even if You’re Broken', 'Katie Rose Guest Pryal', 'https://bluecrowpublishing.com/team/even-if-youre-broken-essays-on-sexual-assault-and-metoo/'),
   ('For the Love of Men: From Toxic to a More Mindful Masculinity', 'Liz Plank', BS + '9781250757203'),
   ('Girls & Sex', 'Peggy Orenstein', BS + '9780062209740'),
   ('I’m Glad My Mom Died', 'Jennette McCurdy', BS + '9781982185831'),
   ('In the Dreamhouse', 'Carmen Maria Machado', BS + '9781644450383'),
   ('Is Rape a Crime?: A Memoir, an Investigation, and a Manifesto', 'Michelle Bowdler', BS + '9781250255761'),
   ('Know My Name: A Memoir', 'Chanel Miller', BS + '9780735223721'),
   ('Man Enough', 'Justin Baldoni', BS + '9780063055605'),
   ('Missoula: Rape and the Justice System in a College Town', 'Jon Krakauer', BS + '9780804170567'),
   ('Not That Bad', 'Roxane Gay', BS + '9780062413512'),
   ('Notes on a Silencing: A Memoir', 'Lacy Crawford', BS + '9780316491532'),
   ('Roll Red Roll: Rape, Power, and Football in the American Heartland', 'Nancy Schwartzman', BS + '9780306924361'),
   ('Sexual Citizens', 'Jennifer Hirsch, Shamus Khan', BS + '9781324001706'),
   ('Sexual Justice', 'Alexandra Brodsky', BS + '9781250839367'),
   ('She Said', 'Jodi Kantor, Megan Twohey', BS + '9780525560364'),
   ('South of Forgiveness', 'Thordis Elva, Tom Stranger', BS + '9781510730014'),
   ('The Body Keeps the Score: Brain, Mind, and Body in the Healing of Trauma', 'Bessel Van Der Kolk, MD', BS + '9780143127741'),
   ('The Macho Paradox: Why Some Men Hurt Women and How All Men Can Help', 'Jackson Katz', BS + '9781402204012'),
   ('The Moment: Standing Up to Bill Cosby, Speaking Up for Women', 'Andrea Constand', 'https://www.penguinrandomhouse.com/books/646293/the-moment-by-andrea-constand/'),
   ('The Purity Myth', 'Jessica Valenti', BS + '9781580053143'),
   ('The Revolution Starts at Home', 'Ching-in Chen, Jai Dulani, Leah Lakshmi Piepzna-Samarasinha', BS + '9781849352628'),
   ('The Truth Will Set You Free But First It’ll Piss You Off!', 'Gloria Steinem', BS + '9780593132685'),
   ('Unbound: My Story of Liberation and the Birth of the Me Too Movement', 'Tarana Burke', BS + '9781250621740'),
   ('Unslut: A Diary and a Memoir', 'Emily Lindin', BS + '9781942186007'),
   ('Women Don’t Owe You Pretty', 'Florence Given', BS + '9781524857561')]),
 ('ya', 'Young adult fiction', [
   ('All Girls', 'Emily Layden', BS + '9781250751126'),
   ('All the Rage', 'Courtney Summers', 'https://us.macmillan.com/books/9781250069153/alltherage/'),
   ('Asking For It', 'Louise O’Neill', 'https://uk.bookshop.org/p/books/asking-for-it-louise-o-neill/199196a1adfc0bbf?ean=9781784293208'),
   ('Beartown', 'Fredrik Backman', BS + '9781501160776'),
   ('Bitter End', 'Jennifer Brown', BS + '9780316086967'),
   ('Breaking Beautiful', 'Jennifer Shaw Wolf', 'https://www.goodreads.com/book/show/10914560-breaking-beautiful'),
   ('Dreamland', 'Sarah Dessen', BS + '9780142401750'),
   ('Exit, Pursued by a Bear', 'E.K. Johnston', 'https://www.penguinrandomhouse.com/books/529826/exit-pursued-by-a-bear-by-ek-johnston/'),
   ('Fault Line', 'Christa Desir', BS + '9781442460720'),
   ('Finnikin of the Rock', 'Melina Marchetta', 'https://www.goodreads.com/book/show/4932435-finnikin-of-the-rock'),
   ('If You Could Be Mine', 'Sara Farizan', BS + '9781616204556'),
   ('Inexcusable', 'Chris Lynch', BS + '9781481432023'),
   ('I’ll Meet You There', 'Heather Demetrios', BS + '9781250080073'),
   ('Lily and Taylor', 'Elise Moser', 'https://houseofanansi.com/products/lily-and-taylor'),
   ('My Life Next Door', 'Huntley Fitzpatrick', BS + '9780142426043'),
   ('My Sister, The Serial Killer', 'Oyinkan Braithwaite', BS + '9780525564201'),
   ('Pointe', 'Brandy Colbert', BS + '9780147514417'),
   ('Queenie', 'Candice Carty Williams', BS + '9781501196027'),
   ('Speak', 'Laurie Halse Anderson', BS + '9780312674397'),
   ('The Dangerous Art of Blending In', 'Angelo Surmelis', BS + '9780062659019'),
   ('The Miseducation of Cameron Post', 'Emily M. Danforth', BS + '9780062020574'),
   ('The Young Elites', 'Marie Lu', BS + '9780147511683'),
   ('Where the Stars Still Shine', 'Trish Doller', 'https://www.goodreads.com/book/show/15826648-where-the-stars-still-shine')]),
 ('pods', 'Podcasts & alternative media', [
   ('Dear Katie Podcast', 'Katie Koestner', 'https://katiekoestner.com/podcast/'),
   ('Man Enough', 'Justin Baldoni, Liz Plank, Jamey Heath', 'https://manenough.com/podcast/'),
   ('Your Friend is Accused of SA, Now What?', 'Teenager Therapy', 'https://open.spotify.com/episode/4G1sLBqWPcyOfv5m8tFczP'),
   ('Unscrewed', 'Jaclyn Friedman', 'https://podcasts.apple.com/us/podcast/unscrewed/id580230127'),
   ('Self-Compassion: The Proven Power of Being Kind to Yourself', 'Kristin Neff', BS + '9780061733529'),
   ('You Throw Like a Girl', 'Don McPherson', 'https://www.akashicbooks.com/catalog/you-throw-like-a-girl/')]),
]


def src_label(u):
    if 'bookshop.org' in u: return 'Bookshop'
    if 'imdb.com' in u: return 'IMDb'
    if 'goodreads.com' in u: return 'Goodreads'
    if 'spotify.com' in u: return 'Spotify'
    if 'apple.com' in u: return 'Apple'
    if 'penguinrandomhouse' in u or 'macmillan' in u or 'akashic' in u or 'bluecrow' in u or 'houseofanansi' in u: return 'Publisher'
    return 'Website'


OC1 = [('offcampusp11', 'Let’s talk about Off Campus', 'Let’s talk about Off Campus: models of consent and healthy sexual relationships. Trigger warning: mention of sexual assault.'),
       ('offcampusp12', 'Based on Elle Kennedy’s bestselling series', 'Based on Elle Kennedy’s bestselling series, Off Campus will premiere on Prime Video on May 13th. The first season will be based on the first book in the series, The Deal.'),
       ('offcampusp13', 'Hannah Wells is a survivor of sexual assault', 'Hannah Wells, the main character, is a survivor of sexual assault. Hannah (played by Ella Bright) is a resilient character, but she carries a lot of baggage, especially when it comes to sex. Quote from Ella Bright in a Teen Vogue interview.'),
       ('offcampusp14', '“Sex is all about trust.”', '“Sex is all about trust. Even if you don’t love the other person, even if it’s just a hookup, it still takes a serious amount of trust to open yourself up and let yourself go to that vulnerable place, you know?” Garrett Graham, The Deal by Elle Kennedy.'),
       ('offcampusp15', 'What consent looks like', 'Throughout the book, Hannah and Garrett show us what consent looks like and the importance of being in-tune with your partner. He takes things slow, asks for verbal consent and continuously checks in.'),
       ('offcampusp16', 'How partners can help', '“Partners can help by practicing clear, proactive communication that affirms the survivor’s experience, articulates the boundaries of the relationship, and offers a willingness to be patient.” CAASE.'),
       ('offcampusp17', 'Tips for a healthy sexual relationship', 'Some tips for building a healthy sexual relationship: figure out what your boundaries are and talk about them with your partner; check in throughout; express your needs and wants; look and listen for non-verbal cues.')]
OC2 = [('offcampusp21', 'Green flags from Off Campus, season 1', 'Green flags from Off Campus, season 1. Warning: spoilers.'),
       ('offcampusp22', 'Green flag 1: “Consent is key.”', 'Green flag 1. “Trust. That’s it. She’s just got to feel completely safe. Like, completely relaxed. But consent is key. And she can’t consent if she doesn’t feel safe.” Dean, episode 4.'),
       ('offcampusp23', 'Green flag 2: “Not until you want me to.”', 'Green flag 2. Hannah: “Uh, you don’t need to turn around. You’re about to see me naked.” Garrett: “Yeah, but not until you want me to.”'),
       ('offcampusp24', 'Green flag 3: He notices she’s nervous', 'Green flag 3. Garrett notices Hannah is nervous. He gives her something more comfortable to wear. He dances with her to get the nerves out.'),
       ('offcampusp25', 'Green flag 4: He reads her cues and stops', 'Green flag 4. When they’re about to have sex, Garrett reads Hannah’s non-verbal cues and can tell that she’s not fully comfortable. So, he stops. He reminds her she doesn’t have to do this, showing respect for her decisions.'),
       ('offcampusp26', 'Green flag 5: A safe place to open up', 'Green flag 5. Hannah being a safe place for Garrett to show emotion and open up about his dad.'),
       ('offcampusp27', '“A healthy sex life is so important.”', '“I think being able to tell a story of someone who has dealt with sexual assault and can still have a romance and a healthy sex life is so important.” Louisa Levy, Off Campus showrunner.')]

QUICK = [  # the four 24/7 lines shown in the hero, taken from HOTLINES_SRC
  ('Dating abuse', 'Text LOVEIS to 22522', 'love is respect', 'sms:22522'),
  ('Sexual assault', 'Call 800-656-HOPE', 'RAINN · 800-656-4673', 'tel:18006564673'),
  ('Suicide & crisis', 'Call or text 988', '988 Suicide & Crisis Lifeline', 'tel:988'),
  ('LGBTQ+ youth', 'Text START to 678-678', 'Trevor Lifeline', 'sms:678678'),
]
OC_QUOTE = ('I think being able to tell a story of someone who has dealt with sexual assault and can still have a romance and a healthy sex life is so important.',
            'Louisa Levy, Off Campus showrunner')

# a hotline card laid out wide: details on the left, the numbers on the right
_WIDE = '''
%S%{grid-row:auto; grid-template-rows:auto auto 1fr auto; grid-template-columns:minmax(0,5fr) minmax(0,7fr); column-gap:clamp(20px,3vw,44px); padding:clamp(20px,2.6vw,30px)}
%S% .ss-line__top{grid-column:1; grid-row:1; justify-content:flex-start; align-items:center; gap:14px}
%S% h3{font-size:clamp(1.3rem,2vw,1.6rem)}
%S% .ss-line__sub{grid-column:1; grid-row:2}
%S% .ss-line__desc{grid-column:1; grid-row:3; margin-top:12px}
%S% .ss-line__site{grid-column:1; grid-row:4}
%S% .ss-acts{grid-column:2; grid-row:1 / -1; margin:0; padding:8px clamp(16px,2.2vw,28px)}
'''
# ...and, where there is room, the numbers side by side
_WIDE_ROW = '''
%S% .ss-acts{flex-direction:row; align-items:center}
%S% .ss-act{flex:1 1 0; padding:12px 0}
%S% .ss-act + .ss-act{border-top:0; border-left:1px solid var(--line-dark); margin-left:clamp(14px,2vw,26px); padding-left:clamp(14px,2vw,26px)}
%S% a.ss-num{font-size:clamp(1.4rem,2.05vw,1.84rem)}
%S% a.ss-num--link{font-size:clamp(1.2rem,1.7vw,1.5rem)}
'''

SS_CSS = '''
/* ---------- hero ---------- */
.ss-hero{--q:54px; --wm-o:.17; color:var(--slate); background:linear-gradient(to bottom, var(--aqua) calc(100% - var(--q)), transparent calc(100% - var(--q))), var(--grain) left bottom repeat-x, linear-gradient(var(--slate), var(--slate)) var(--aqua)}
.ss-hero__bg{position:absolute; inset:0 0 var(--q) 0; overflow:hidden; pointer-events:none}
.ss-hero .wm-daisy{color:var(--logo-teal)}
.ss-hero__grid{display:grid; grid-template-columns:minmax(0,7fr) minmax(0,5fr); grid-template-areas:"text photo" "quick quick"; column-gap:clamp(28px,4.4vw,64px); row-gap:clamp(30px,3.6vw,46px); align-items:center; padding-top:clamp(36px,4.4vw,60px)}
.ss-hero__text{grid-area:text; min-width:0} .ss-hero__photo{grid-area:photo} .ss-quick{grid-area:quick}
.ss-hero .crumbs{color:var(--ink-soft); margin-bottom:18px} .ss-hero .crumbs a{color:var(--logo-teal)}
.ss-hero h1{font-size:clamp(2.5rem,4.9vw,4.4rem); font-stretch:110%; font-weight:850; line-height:.96; letter-spacing:-.02em; color:var(--logo-teal); margin:0 0 .32em}
.ss-hero .lede{color:var(--slate); max-width:none; margin-bottom:1em}
.ss-hero__photo{position:relative}
.ss-hero__photo img{width:100%; aspect-ratio:4/3; object-fit:cover; object-position:50% 30%; border-radius:var(--r-xl); box-shadow:var(--shadow-soft)}
.ss-hero__photo .sticker{position:absolute; left:-12px; bottom:22px}
.ss-bubble{position:absolute; margin:0; font-family:var(--display); font-stretch:106%; font-weight:800; font-size:clamp(.98rem,1.4vw,1.18rem); line-height:1.2; padding:12px 16px; border-radius:18px; box-shadow:var(--shadow-soft); animation:sb-rise-t .9s .5s var(--ease) both}
@keyframes sb-rise-t{from{transform:translateY(14px)}}
.ss-bubble--a{right:-14px; top:-20px; background:#fff; color:var(--logo-teal); border-bottom-right-radius:4px}
.ss-bubble--b{right:8%; bottom:-22px; background:var(--slate); color:#fff; border-bottom-left-radius:4px; animation-delay:.8s}
.ss-bubble::after{content:""; position:absolute; width:14px; height:14px; background:inherit; bottom:-6px; transform:rotate(45deg)}
.ss-bubble--a::after{right:22px} .ss-bubble--b::after{left:22px}
/* the four 24/7 lines, on the seam between the hero and the full list */
.ss-quick{display:grid; grid-template-columns:repeat(4,minmax(0,1fr)); column-gap:var(--gap); background:#fff; border-radius:var(--r-xl); border:1px solid var(--line); box-shadow:0 28px 54px -32px rgba(8,26,32,.75); overflow:hidden}
.ss-quick a{position:relative; display:flex; flex-direction:column; justify-content:center; gap:3px; min-height:108px; padding:16px 8px 17px 20px; text-decoration:none; color:var(--slate); min-width:0}
.ss-quick a + a::before{content:""; position:absolute; left:calc(var(--gap) / -2); top:18px; bottom:18px; width:1px; background:var(--line)}
.ss-quick small{font-family:var(--mono); font-size:.72rem; letter-spacing:.1em; text-transform:uppercase; font-weight:600; color:var(--logo-teal)}
.ss-quick b{font-family:var(--display); font-weight:800; font-stretch:98%; font-size:clamp(1.1rem,1.62vw,1.36rem); line-height:1.15; letter-spacing:-.005em; color:var(--slate); text-decoration:underline; text-decoration-color:transparent; text-decoration-thickness:3px; text-underline-offset:4px; transition:text-decoration-color .2s}
.ss-quick a:hover b,.ss-quick a:focus-visible b{text-decoration-color:var(--mint)}
.ss-quick span{font-size:.9rem; color:var(--ink-soft); line-height:1.3}
.ss-quick a:focus-visible{outline-offset:-4px; outline-color:var(--teal)}
@media (max-width:1100px){
  .ss-quick{grid-template-columns:repeat(2,minmax(0,1fr))}
  .ss-quick a{min-height:92px}
  .ss-quick a:nth-child(odd)::before{display:none}
  .ss-quick a:nth-child(n+3){border-top:1px solid var(--line)}
  .ss-quick a:nth-child(3)::after{content:""; position:absolute; top:-1px; left:100%; width:var(--gap); height:1px; background:var(--line)}
}
@media (max-width:860px){
  .ss-hero{--q:0px; padding-bottom:44px}
  .ss-hero__grid{grid-template-columns:minmax(0,1fr); grid-template-areas:"text" "quick" "photo"; row-gap:22px}
  .ss-hero__photo{max-width:520px; margin:22px 0 0}
  .ss-hero__photo .sticker{left:10px}
  .ss-bubble--a{right:6px} .ss-bubble--b{right:auto; left:14px}
}
@media (max-width:560px){
  .ss-hero__photo .sticker{display:none}
  .ss-quick{grid-template-columns:1fr}
  .ss-quick a{min-height:0; padding:13px 16px 14px}
  .ss-quick a::before,.ss-quick a::after{display:none!important}
  .ss-quick a + a{border-top:1px solid var(--line)}
  .ss-quick b{font-size:1.2rem}
}

/* ---------- hotline finder ---------- */
#hotlines{padding-top:clamp(40px,5vw,68px); scroll-margin-top:36px}
.ss-choke{scroll-margin-top:112px}
.ss-hl-head .lede{color:rgba(255,255,255,.88)}
.ss-911{display:flex; gap:14px; align-items:center; margin:0; max-width:320px; background:var(--coral); color:var(--slate); border-radius:14px; padding:14px 18px; font-weight:700; line-height:1.3}
.ss-911 b{font-family:var(--display); font-stretch:118%; font-weight:900; font-size:2rem; line-height:1}
.ss-filterbar{margin:0 0 16px}
.ss-filter__count{font-family:var(--mono); font-size:.76rem; letter-spacing:.1em; text-transform:uppercase; font-weight:600; color:var(--mint); margin:16px 0 0}
.ss-lines{display:grid; grid-template-columns:repeat(4,minmax(0,1fr)); gap:var(--gap)}
.ss-line{display:grid; grid-template-rows:subgrid; grid-row:span 5; row-gap:0; padding:20px; border-radius:var(--r-xl); background:rgba(255,255,255,.06); border:1px solid var(--line-dark); min-width:0; color:#fff; transition:border-color .25s, background .25s}
.ss-line:hover{border-color:rgba(21,255,200,.45); background:rgba(255,255,255,.08)}
.ss-line[hidden]{display:none}
.ss-lines.is-in .ss-line{animation:ss-in .45s var(--ease) both}
@keyframes ss-in{from{transform:translateY(12px)}}
.ss-line__top{display:flex; justify-content:space-between; gap:10px; align-items:flex-start}
.ss-line h3{font-size:1.2rem; line-height:1.14; font-stretch:106%; margin:0; color:#fff}
.ss-line__top .chip{background:var(--mint); flex:none}
.ss-line__sub{font-size:.92rem; font-weight:600; line-height:1.35; color:var(--aqua); margin:6px 0 0}
.ss-acts{display:flex; flex-direction:column; justify-content:center; margin:14px 0; padding:3px 14px; border-radius:14px; background:rgba(8,26,32,.46); border:1px solid rgba(209,254,255,.12)}
.ss-act{display:grid; grid-template-columns:minmax(0,1fr) auto; align-items:center; gap:1px 8px; padding:11px 0 12px; min-width:0}
.ss-act + .ss-act{border-top:1px solid var(--line-dark)}
.ss-act small{font-family:var(--mono); font-size:.72rem; letter-spacing:.12em; text-transform:uppercase; color:rgba(255,255,255,.74); font-weight:600}
.ss-act button{position:relative; font:inherit; font-family:var(--mono); font-size:.72rem; letter-spacing:.06em; text-transform:uppercase; font-weight:600; background:none; border:0; padding:0; color:var(--aqua); cursor:pointer; text-decoration:underline; text-decoration-color:rgba(209,254,255,.4); text-underline-offset:3px}
.ss-act button::after{content:""; position:absolute; inset:-12px -10px}
.ss-act button:hover{color:var(--mint); text-decoration-color:var(--mint)}
.ss-line a.ss-num{grid-column:1/-1; display:block; white-space:nowrap; font-family:var(--display); font-weight:800; font-stretch:90%; font-size:clamp(1.2rem,1.6vw,1.44rem); line-height:1.14; letter-spacing:-.005em; color:var(--mint); text-decoration:none}
.ss-line a.ss-num:hover{text-decoration:underline; text-decoration-thickness:2px; text-underline-offset:4px}
.ss-num i{display:block; font-style:normal; font-stretch:100%; font-size:.95rem; font-weight:700; letter-spacing:0; color:var(--aqua); margin-top:2px}
.ss-line a.ss-num--link{white-space:normal; font-size:clamp(1.1rem,1.36vw,1.22rem); font-stretch:100%; line-height:1.2; color:var(--aqua); text-decoration:underline; text-decoration-color:var(--mint); text-decoration-thickness:2px; text-underline-offset:4px}
.ss-line a.ss-num--link:hover{color:var(--mint)}
.ss-acts > .ss-act:only-child a.ss-num{font-size:clamp(1.3rem,1.74vw,1.58rem)}
.ss-acts > .ss-act:only-child a.ss-num--link{font-size:clamp(1.2rem,1.56vw,1.4rem)}
.ss-line__desc{font-size:.95rem; color:rgba(255,255,255,.86); margin:0; line-height:1.48}
.ss-line a.ss-line__site{align-self:end; justify-self:start; margin-top:12px; font-weight:700; font-size:.92rem; color:var(--aqua); text-decoration:none}
.ss-line a.ss-line__site:hover{color:var(--mint)}
@media (pointer:coarse){.ss-line a.ss-num{padding-block:5px} .ss-line a.ss-line__site{padding-block:10px; margin-top:2px}}
@media (min-width:1101px){
  .ss-lines[data-n="6"],.ss-lines[data-n="3"]{grid-template-columns:repeat(3,minmax(0,1fr))}
  .ss-lines[data-n="2"]{grid-template-columns:repeat(2,minmax(0,1fr))}
  .ss-lines[data-n="5"]{grid-template-columns:repeat(6,minmax(0,1fr))}
  .ss-lines[data-n="5"] .ss-line{grid-column:span 2}
  .ss-lines[data-n="5"] .ss-line[data-i="4"]{grid-column:2 / span 2}
}
@media (max-width:1100px){.ss-lines{grid-template-columns:repeat(2,minmax(0,1fr))}}
@media (max-width:640px){.ss-lines{grid-template-columns:minmax(0,1fr)}}
.ss-lines[data-n="1"]{grid-template-columns:minmax(0,1fr)}
@media (min-width:641px){''' + _WIDE.replace('%S%', '.ss-lines[data-n="1"] .ss-line') + '''}
@media (min-width:1000px){''' + _WIDE_ROW.replace('%S%', '.ss-lines[data-n="1"] .ss-line') + '''}
@media (min-width:641px) and (max-width:1100px){
.ss-lines[data-odd="1"] .ss-line[data-last]{grid-column:1 / -1}''' + _WIDE.replace('%S%', '.ss-lines[data-odd="1"] .ss-line[data-last]') + '''}
@media (min-width:1000px) and (max-width:1100px){''' + _WIDE_ROW.replace('%S%', '.ss-lines[data-odd="1"] .ss-line[data-last]') + '''}

/* ---------- if you were choked or strangled ---------- */
.ss-choke{display:grid; grid-template-columns:minmax(0,7fr) minmax(0,5fr); gap:clamp(22px,3.4vw,44px); margin-top:var(--gap); padding:var(--pad-card); border-radius:var(--r-xl); background:#fff; color:var(--slate)}
.ss-choke__main,.ss-choke__side{display:flex; flex-direction:column; min-width:0}
.ss-choke__tag{display:flex; align-items:center; gap:.7em; font-family:var(--mono); font-size:.72rem; letter-spacing:.1em; text-transform:uppercase; font-weight:600; color:var(--logo-teal); margin:0 0 10px}
.ss-choke__tag::before{content:""; flex:none; width:10px; height:10px; border-radius:50%; background:var(--coral)}
.ss-choke h3{font-size:clamp(1.6rem,2.6vw,2.2rem); margin:0 0 .3em; color:var(--slate)}
.ss-choke__lead{font-size:1.08rem; font-weight:600; margin:0 0 16px}
.ss-choke__signs{flex:1; list-style:none; padding:0; margin:0; display:grid; grid-template-columns:repeat(2,minmax(0,1fr)); grid-auto-rows:1fr; gap:8px}
.ss-choke__signs li{display:flex; align-items:center; gap:12px; margin:0; padding:11px 14px; border-radius:12px; background:var(--mist); font-size:.98rem; font-weight:600; line-height:1.35}
.ss-choke__signs li::before{content:""; flex:none; width:9px; height:9px; border-radius:50%; background:var(--coral)}
.ss-choke__say{flex:1; display:flex; flex-direction:column; justify-content:center; gap:5px; margin:0; padding:20px 22px; border-radius:16px; background:var(--aqua)}
.ss-choke__say span{font-size:.98rem; font-weight:600}
.ss-choke__say b{font-family:var(--display); font-stretch:112%; font-weight:900; font-size:clamp(1.7rem,2.8vw,2.4rem); line-height:1.05; color:var(--logo-teal)}
.ss-choke__911{margin:12px 0 0; padding:16px 18px; border-radius:16px; background:#fff1f1; border:1px solid #ffc7c7; font-size:.96rem; line-height:1.5}
.ss-choke__911 b{font-family:var(--display); font-stretch:108%; font-weight:900; font-size:1.08rem}
.ss-choke__side .btns{margin-top:14px}
@media (max-width:900px){.ss-choke{grid-template-columns:minmax(0,1fr)}}
@media (max-width:560px){.ss-choke__signs{grid-template-columns:minmax(0,1fr); grid-auto-rows:auto}}

/* ---------- healing ---------- */
.ss-heal{display:grid; grid-template-columns:minmax(0,5fr) minmax(0,7fr); gap:clamp(24px,4vw,56px); align-items:stretch}
.ss-heal__txt{display:flex; flex-direction:column; min-width:0}
.ss-heal__txt > p{margin:0}
.ss-heal__txt .btns{margin-top:20px; gap:10px}
.ss-heal__txt .btn{padding-inline:1em; font-size:.97rem}
.ss-tattoo{flex:1; display:grid; grid-template-columns:minmax(104px,32%) minmax(0,1fr); min-height:168px; margin-top:24px; border-radius:var(--r-xl); border:1px solid var(--line); background:var(--mist); overflow:hidden; text-decoration:none; color:var(--slate); transition:box-shadow .25s var(--ease), transform .25s var(--ease)}
.ss-tattoo:hover{box-shadow:var(--shadow-soft); transform:translateY(-3px)}
.ss-tattoo__img{position:relative; overflow:hidden}
.ss-tattoo__img img{position:absolute; inset:0; width:100%; height:100%; object-fit:cover; object-position:50% 28%; transition:transform .5s var(--ease)}
.ss-tattoo:hover .ss-tattoo__img img{transform:scale(1.05)}
.ss-tattoo__txt{display:flex; flex-direction:column; justify-content:center; gap:5px; padding:18px 20px; min-width:0}
.ss-tattoo small{font-family:var(--mono); font-size:.72rem; letter-spacing:.1em; text-transform:uppercase; color:var(--logo-teal); font-weight:600}
.ss-tattoo b{font-family:var(--display); font-stretch:108%; font-size:1.3rem; line-height:1.12; color:var(--logo-teal)}
.ss-tattoo__txt > span{font-size:.95rem; color:var(--ink-soft); line-height:1.45}
.ss-tattoo em{font-style:normal; font-weight:700; font-size:.95rem; color:var(--logo-teal); margin-top:4px}
.ss-tattoo em::after{content:"\\2192"; display:inline-block; margin-left:.4em; transition:transform .2s var(--ease)}
.ss-tattoo:hover em::after{transform:translateX(4px)}
.ss-practice{background:var(--grain) var(--slate); color:#fff; border-radius:var(--r-xl); padding:var(--pad-card); display:flex; flex-direction:column; min-width:0}
.ss-practice h3{color:#fff; font-size:clamp(1.35rem,2.1vw,1.7rem); margin-bottom:.3em}
.ss-practice > p{color:rgba(255,255,255,.86); margin:0}
.ss-tiles{flex:1; display:grid; grid-template-columns:repeat(4,minmax(0,1fr)); grid-auto-rows:1fr; gap:10px; margin:18px 0}
.ss-tiles button{position:relative; font:inherit; text-align:left; font-family:var(--display); font-stretch:104%; font-weight:800; font-size:1rem; line-height:1.18; padding:14px 14px 14px; border-radius:12px; border:1.5px solid var(--line-dark); background:rgba(255,255,255,.05); color:#fff; cursor:pointer; min-height:84px; display:flex; align-items:flex-end; transition:background .25s, color .25s, border-color .25s, transform .25s var(--ease), box-shadow .25s}
.ss-tiles button::before{content:""; position:absolute; right:10px; top:10px; width:16px; height:16px; border-radius:50%; border:1.5px solid rgba(209,254,255,.4); transition:background .2s, border-color .2s}
.ss-tiles button:hover{border-color:var(--mint)}
.ss-tiles button[aria-pressed="true"]{background:var(--mint); color:var(--slate); border-color:var(--mint)}
.ss-tiles button[aria-pressed="true"]::before{border-color:var(--slate); background:var(--slate) url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 24 24'%3E%3Cpath d='M5 12.5l4.5 4.5L19 7.5' fill='none' stroke='%2315ffc8' stroke-width='3.6' stroke-linecap='round' stroke-linejoin='round'/%3E%3C/svg%3E") center/11px no-repeat}
.ss-tiles button.pick{transform:scale(1.04); box-shadow:0 0 0 4px rgba(21,255,200,.35)}
.ss-pick{display:flex; flex-wrap:wrap; gap:12px 16px; align-items:center; min-height:44px}
.ss-pick output{font-weight:700; color:var(--mint)}
@media (max-width:1100px){.ss-heal{grid-template-columns:minmax(0,1fr)}}
@media (max-width:640px){.ss-tiles{grid-template-columns:repeat(2,minmax(0,1fr))} .ss-tiles button{min-height:72px}}
@media (max-width:420px){.ss-tattoo{grid-template-columns:96px minmax(0,1fr)} .ss-tattoo__txt{padding:16px}}

/* ---------- dating after sexual assault ---------- */
.ss-date{display:grid; grid-template-columns:minmax(0,7fr) minmax(0,5fr); gap:clamp(24px,4vw,56px); align-items:stretch}
.ss-date__media{display:flex; min-width:0}
.ss-date__media .vid{flex:1; aspect-ratio:auto; min-height:0; border-radius:var(--r-xl)}
.ss-now{display:flex; flex-wrap:wrap; gap:10px 20px; align-items:center; justify-content:space-between; margin-top:var(--gap); padding:16px clamp(16px,2vw,24px); border-radius:16px; background:var(--grain) var(--slate); color:#fff; line-height:1.45}
.ss-now > span:first-child{flex:1 1 300px; min-width:0}
.ss-now b{font-family:var(--display); font-stretch:104%}
.ss-now strong{color:var(--mint)}
.ss-now .copy{border:0; background:#fff}
.ss-date__txt{display:flex; flex-direction:column; min-width:0}
.ss-date__txt .btns{margin-top:auto; padding-top:10px}
@media (max-width:1100px){.ss-date{grid-template-columns:minmax(0,1fr)} .ss-date__media .vid{aspect-ratio:16/9} .ss-date__txt .btns{margin-top:6px}}

/* ---------- when someone tells you ---------- */
.ss-tell__head .lede{color:rgba(255,255,255,.9)}
.ss-ways{display:grid; grid-template-columns:repeat(2,minmax(0,1fr)); gap:var(--gap)}
.ss-way{border-radius:var(--r-xl); padding:var(--pad-card); background:rgba(255,255,255,.06); border:1px solid var(--line-dark); min-width:0}
.ss-way h3{font-size:1.42rem; color:var(--mint); margin:0 0 .4em}
.ss-way p{margin:0; color:rgba(255,255,255,.9); font-size:1rem; line-height:1.58}
.ss-way--lead{position:relative; overflow:hidden; grid-column:1 / -1; display:grid; grid-template-columns:minmax(0,5fr) minmax(0,7fr); gap:clamp(18px,4vw,56px); align-items:center; padding:clamp(24px,3.4vw,44px); background:var(--mint); border-color:transparent; color:var(--slate)}
.ss-way--lead h3{font-size:clamp(2.1rem,4vw,3.4rem); font-stretch:118%; font-weight:900; line-height:.96; letter-spacing:-.02em; color:var(--slate); margin:0}
.ss-way--lead p{color:var(--slate); font-size:var(--fs-lede); font-weight:500; line-height:1.5}
@media (max-width:760px){.ss-ways{grid-template-columns:minmax(0,1fr)} .ss-way--lead{grid-template-columns:minmax(0,1fr)}}

/* ---------- words that help ---------- */
.ss-say{display:grid; grid-template-columns:repeat(2,minmax(0,1fr)); gap:var(--gap); align-items:stretch}
.ss-say__col{display:flex; flex-direction:column; border-radius:var(--r-xl); padding:var(--pad-card); min-width:0}
.ss-say__col--do{background:var(--mint); color:var(--slate)}
.ss-say__col--dont{background:#fff; border:1px solid var(--line); color:var(--slate)}
.ss-say h3{margin:0; font-size:clamp(1.4rem,2.1vw,1.7rem)}
.ss-say__col > small{display:block; font-family:var(--mono); font-size:.72rem; letter-spacing:.1em; text-transform:uppercase; font-weight:600; margin-bottom:6px; color:var(--logo-teal)}
.ss-say ul{flex:1; list-style:none; padding:0; margin:16px 0 0; display:grid; grid-auto-rows:1fr; gap:8px}
.ss-say li{display:flex; align-items:center; gap:13px; margin:0; font-family:var(--display); font-stretch:104%; font-weight:700; font-size:1.1rem; line-height:1.28; padding:11px 16px 11px 13px; border-radius:12px}
.ss-say li::before{content:""; flex:none; width:24px; height:24px; border-radius:50%}
.ss-say__col--do li{background:rgba(255,255,255,.62)}
.ss-say__col--do li::before{background:var(--slate) url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 24 24'%3E%3Cpath d='M5.5 12.5l4.2 4.2L18.5 8' fill='none' stroke='%2315ffc8' stroke-width='3.2' stroke-linecap='round' stroke-linejoin='round'/%3E%3C/svg%3E") center/14px no-repeat}
.ss-say__col--dont li{background:var(--mist); color:var(--ink-soft)}
.ss-say__col--dont li::before{background:#fff url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 24 24'%3E%3Cpath d='M7 7l10 10M17 7L7 17' fill='none' stroke='%2346646e' stroke-width='3' stroke-linecap='round'/%3E%3C/svg%3E") center/13px no-repeat; box-shadow:inset 0 0 0 1.5px var(--line)}
@media (max-width:760px){.ss-say{grid-template-columns:minmax(0,1fr)} .ss-say ul{grid-auto-rows:auto}}
.ss-print{display:grid; grid-template-columns:auto minmax(0,1fr) auto; gap:clamp(14px,2vw,24px); align-items:center; margin-top:var(--gap); padding:14px clamp(16px,2vw,24px) 14px 14px; border-radius:var(--r-xl); background:#fff; border:1px solid var(--line)}
.ss-print > button{border:0; padding:0; background:none; cursor:zoom-in; border-radius:10px; overflow:hidden; box-shadow:0 10px 24px -14px rgba(29,65,78,.6)}
.ss-print img{width:124px; transition:transform .35s var(--ease)}
.ss-print > button:hover img{transform:scale(1.04)}
.ss-print b{display:block; font-family:var(--display); font-stretch:106%; font-size:1.22rem; line-height:1.15; color:var(--logo-teal); margin-bottom:3px}
.ss-print span{color:var(--ink-soft); font-size:.98rem; line-height:1.45}
@media (max-width:700px){.ss-print{grid-template-columns:auto minmax(0,1fr)} .ss-print .btns{grid-column:1/-1} .ss-print img{width:92px}}

/* ---------- shareable graphics ---------- */
.ss-gal{display:grid; grid-template-columns:repeat(4,minmax(0,1fr)); gap:var(--gap)}
.ss-gal button{display:flex; flex-direction:column; border:0; padding:10px 10px 0; background:#fff; border-radius:18px; cursor:zoom-in; text-align:left; font:inherit; color:var(--slate); box-shadow:0 18px 34px -24px rgba(29,65,78,.7); transition:transform .25s var(--ease), box-shadow .25s var(--ease); min-width:0}
.ss-gal button:hover{transform:translateY(-4px) rotate(-.6deg); box-shadow:0 26px 40px -24px rgba(29,65,78,.8)}
.ss-gal button:nth-child(even):hover{transform:translateY(-4px) rotate(.6deg)}
.ss-gal__img{display:block; aspect-ratio:3/4; overflow:hidden; border-radius:10px; background:var(--mist)}
.ss-gal__img img{width:100%; height:100%; object-fit:cover}
.ss-gal__cap{flex:1; display:flex; align-items:center; justify-content:space-between; gap:12px; padding:12px 4px 13px 6px; font-family:var(--display); font-stretch:104%; font-weight:800; font-size:1rem; line-height:1.2}
.ss-gal__cap i{flex:none; width:28px; height:28px; border-radius:50%; background:var(--aqua) url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 24 24'%3E%3Cpath d='M12 5v14M5 12h14' stroke='%231d5a66' stroke-width='2.8' stroke-linecap='round'/%3E%3C/svg%3E") center/13px no-repeat; transition:background-color .2s}
.ss-gal button:hover .ss-gal__cap i{background-color:var(--mint)}
@media (max-width:900px){.ss-gal{grid-template-columns:repeat(2,minmax(0,1fr))}}
@media (max-width:420px){.ss-gal{gap:12px} .ss-gal__cap{font-size:.92rem; padding-inline:2px}}

/* ---------- survivor-centered media ---------- */
.ss-shop{display:flex; align-items:center; gap:14px 20px; max-width:560px; padding:16px 18px 16px 22px; border-radius:16px; background:var(--grain) var(--slate); color:#fff}
.ss-shop p{flex:1 1 220px; color:rgba(255,255,255,.9); margin:0; font-size:.98rem; line-height:1.45}
.ss-shop .btn{flex:none}
.ss-cats{display:grid; grid-template-columns:repeat(3,minmax(0,1fr)); gap:10px var(--gap); margin-bottom:var(--gap)}
.ss-cats button{display:flex; align-items:center; justify-content:space-between; gap:12px; min-height:56px; padding:10px 14px 10px 18px; border-radius:14px; border:1.5px solid var(--line); background:#fff; color:var(--logo-teal); font:inherit; font-family:var(--display); font-stretch:104%; font-weight:800; font-size:1.05rem; line-height:1.2; text-align:left; cursor:pointer; transition:background .2s, color .2s, border-color .2s}
.ss-cats button:hover{border-color:var(--teal)}
.ss-cats span{min-width:0}
.ss-cats small{flex:none; min-width:34px; text-align:center; font-family:var(--mono); font-size:.76rem; font-weight:600; letter-spacing:.04em; padding:4px 7px; border-radius:6px; background:var(--aqua); color:var(--slate); font-stretch:100%}
.ss-cats button[aria-selected="true"]{background:var(--slate); border-color:var(--slate); color:#fff}
.ss-cats button[aria-selected="true"] small{background:var(--mint)}
.ss-books{--c:4; list-style:none; padding:0; margin:0; display:grid; grid-template-columns:repeat(var(--c),minmax(0,1fr)); gap:0 var(--gap); border-bottom:1px solid var(--line)}
.ss-books--c3{--c:3}
.ss-books li{display:flex; margin:0; border-top:1px solid var(--line); min-width:0}
.ss-books a{flex:1; display:grid; grid-template-columns:minmax(0,1fr) auto; align-content:center; gap:2px 12px; min-height:64px; padding:12px 2px; text-decoration:none; color:var(--slate); min-width:0}
.ss-books b{align-self:center; font-weight:700; font-size:1rem; line-height:1.3; text-wrap:pretty}
.ss-books small{grid-column:1; color:var(--ink-soft); font-size:.9rem; line-height:1.35}
.ss-books em{grid-column:2; grid-row:1 / span 2; align-self:center; font-style:normal; font-family:var(--mono); font-size:.7rem; font-weight:600; letter-spacing:.06em; text-transform:uppercase; color:var(--logo-teal); white-space:nowrap}
.ss-books em::after{content:" \\2197"; font-family:var(--body)}
.ss-books a:hover b{color:var(--teal); text-decoration:underline; text-decoration-color:var(--mint); text-decoration-thickness:2px; text-underline-offset:3px}
@media (max-width:1100px){.ss-books{--c:2} .ss-books--c3{--c:3}}
@media (max-width:860px){.ss-books,.ss-books--c3{--c:2} .ss-cats{grid-template-columns:repeat(2,minmax(0,1fr))} .ss-shop{max-width:none}}
@media (max-width:560px){.ss-books,.ss-books--c3{--c:1} .ss-cats{grid-template-columns:minmax(0,1fr); gap:8px} .ss-cats button{min-height:48px} .ss-shop{flex-wrap:wrap}}

/* ---------- Off Campus ---------- */
.ss-oc{display:grid; grid-template-columns:repeat(3,minmax(0,1fr)); gap:clamp(20px,3vw,40px); align-items:stretch}
.ss-oc__intro{display:flex; flex-direction:column; min-width:0}
.ss-oc__intro > p{color:rgba(255,255,255,.9); margin:0}
.ss-oc__q{margin:auto 0; padding:18px 0 14px}
.ss-oc__q .quote{font-size:clamp(1.12rem,1.5vw,1.3rem); line-height:1.32}
.ss-oc__q .quote::before{font-size:3.4em}
.ss-oc__q .cite{color:var(--mint); margin-top:12px}
.ss-oc__note{font-size:.92rem; color:rgba(255,255,255,.78)!important; line-height:1.5}
.ss-oc__set{display:flex; flex-direction:column; min-width:0}
.ss-oc__set > p{display:flex; justify-content:space-between; gap:10px; align-items:center; margin:0 0 12px; min-height:28px}
.ss-oc__set b{font-family:var(--display); font-stretch:106%; font-size:1.1rem; line-height:1.2; color:#fff}
.ss-oc__set .chip{background:var(--mint)}
@media (max-width:1100px){.ss-oc{grid-template-columns:repeat(2,minmax(0,1fr))} .ss-oc__intro{grid-column:1/-1; display:grid; grid-template-columns:repeat(2,minmax(0,1fr)); column-gap:clamp(20px,3vw,40px)} .ss-oc__intro > *{grid-column:1} .ss-oc__intro > .ss-oc__q{grid-column:2; grid-row:1 / span 4; align-self:center; margin:0; padding:0} .ss-oc__note{margin-top:12px!important}}
@media (max-width:640px){.ss-oc{grid-template-columns:minmax(0,1fr)} .ss-oc__intro{display:flex} .ss-oc__intro > .ss-oc__q{padding:18px 0 6px}}
'''


def survivor_support():
    filt = ''.join(f'<button type="button" data-f="{k}" aria-pressed="{str(k == "all").lower()}">{esc(l)}</button>' for k, l in HL_FILTERS)
    cards = []
    for n, h in enumerate(HOTLINES_SRC):
        acts = []
        for label, disp, href, cp in h['acts']:
            if cp:
                main, _, alt = disp.partition(' (')
                alt = f' <i>({esc(alt)}</i>' if alt else ''
                acts.append(f'<div class="ss-act"><small>{esc(label)}</small><button type="button" data-copy="{esc(cp)}" aria-label="Copy {esc(cp)}">Copy</button>'
                            f'<a class="ss-num" href="{esc(href)}">{esc(main)}{alt}</a></div>')
            else:
                acts.append(f'<div class="ss-act"><small>{esc(label)}</small>{a(esc(disp), href, "ss-num ss-num--link")}</div>')
        chip = '<span class="chip">24/7</span>' if h['h24'] else ''
        last = ' data-last' if n == len(HOTLINES_SRC) - 1 else ''
        cards.append(f'''<article class="ss-line" data-tags="{h['tags']}" data-i="{n + 1}"{last}><div class="ss-line__top"><h3>{esc(h['name'])}</h3>{chip}</div>
<p class="ss-line__sub">{esc(h['sub'])}</p><div class="ss-acts">{''.join(acts)}</div><p class="ss-line__desc">{esc(h['desc'])}</p>
{a(esc(h['site'][0]) + ' &#8599;', h['site'][1], 'ss-line__site')}</article>''')
    quick = ''.join(f'<a href="{href}"><small>{esc(k)}</small><b>{esc(big)}</b><span>{esc(org)}</span></a>' for k, big, org, href in QUICK)

    tiles = ''.join(f'<button type="button" aria-pressed="false">{esc(p)}</button>' for p in PRACTICES)
    lead_t, lead_d = WAYS[0]
    ways = (f'<article class="ss-way ss-way--lead"><h3>{esc(lead_t)}</h3><p>{esc(lead_d)}</p></article>'
            + ''.join(f'<article class="ss-way"><h3>{esc(t)}</h3><p>{esc(d)}</p></article>' for t, d in WAYS[1:]))
    say = ''.join(f'<li>{esc(s)}</li>' for s in SAY)
    dont = ''.join(f'<li>{esc(s)}</li>' for s in DONT)

    gal_items = [('healing-from-trauma-3', 'Healing from a traumatic relationship', 'Poster: Healing from a traumatic relationship. Re-affirm your self-worth, practice mindfulness, practice self care, take the time you need to process, journal your thoughts, express your feelings, honor your needs, forgive yourself, reassure yourself, talk about your experiences, focus on the present moment, practice positive self talk.'),
                 ('everyone-can-do-something-1', 'No one can do everything, but everyone can do something', 'Poster: No one can do everything but everyone can do something. End rape culture.'),
                 ('relationships-4', 'What goes into a healthy relationship?', 'Poster: What goes into a healthy relationship? Equality at the center, surrounded by nonviolence, respect, trust, good communication, honesty, healthy boundaries and more.'),
                 ('relationships-vs-poster-1', 'Healthy vs. unhealthy relationships', 'Poster comparing healthy and unhealthy relationship behaviors.')]
    gal = ''.join(f'<button type="button" data-src="{imgsrc(n)}" data-cap="{esc(c)}" aria-label="Enlarge: {esc(c)}"><span class="ss-gal__img">{img(n, alt)}</span>'
                  f'<span class="ss-gal__cap">{esc(c)}<i aria-hidden="true"></i></span></button>' for n, c, alt in gal_items)

    tabs, panels = [], []
    for i, (k, title, items) in enumerate(MEDIA):
        cols = 4 if len(items) % 4 == 0 or (len(items) % 3 and (4 - len(items) % 4) <= (3 - len(items) % 3)) else 3
        lis = ''.join(f'<li><a href="{esc(u)}" target="_blank" rel="noopener"><b>{esc(t)}</b>{f"<small>{esc(by)}</small>" if by else ""}<em>{src_label(u)}</em></a></li>' for t, by, u in items)
        tabs.append(f'<button type="button" role="tab" id="ss-t-{k}" aria-controls="ss-p-{k}" aria-selected="{str(i == 0).lower()}" tabindex="{0 if i == 0 else -1}"><span>{esc(title)}</span><small>{len(items)}</small></button>')
        panels.append(f'<div role="tabpanel" id="ss-p-{k}" aria-labelledby="ss-t-{k}"{"" if i == 0 else " hidden"}><ul class="ss-books ss-books--c{cols}">{lis}</ul></div>')

    body = f'''
<section class="ss-hero sp-hero">
  <div class="ss-hero__bg" aria-hidden="true"><span class="wm-daisy"></span></div>
  <div class="wrap">
    <div class="ss-hero__grid">
      <div class="ss-hero__text rise">
        {crumbs(('Home', 'index.html'), ('Resources', 'resources.html'), ('Survivor Support', None))}
        <h1>Survivor support &amp; <span class="mk">healing</span></h1>
        <p class="lede">Healing after sexual violence is deeply personal, with no single path forward. Many survivors find strength in connection, whether with peers, supportive communities, or professionals.</p>
        <div class="btns">{btn('Talk to someone now', '#hotlines', 'coral', arrow=True)}{btn('When someone tells you', '#when-someone-tells-you', 'slate')}</div>
        {esc_note()}
      </div>
      <div class="ss-hero__photo">{img('safebae-5', 'Two young women leaning their heads together and smiling', loading='eager')}<span class="sticker">Free &amp; confidential</span>
        <p class="ss-bubble ss-bubble--a" aria-hidden="true">“It’s not your fault.”</p>
        <p class="ss-bubble ss-bubble--b" aria-hidden="true">“How can I support you?”</p></div>
      <nav class="ss-quick" aria-label="Four free lines open 24/7">{quick}</nav>
    </div>
  </div>
</section>

<section class="band band--slate" id="hotlines">
  <div class="wrap">
    <div class="section-head ss-hl-head">
      <div><p class="eyebrow">8 free, confidential lines</p><h2>Talk to someone now</h2>
        <p class="lede lede--full">There are many resources to help find your local services. We recommend contacting your local rape crisis services to get recommendations for services close to you.</p></div>
      <p class="ss-911 section-head__act"><b>911</b><span>If you are in immediate danger, call 911.</span></p>
    </div>
    <div class="ss-filterbar">
      <div class="sp-chips ss-filter" role="group" aria-label="Filter hotlines">{filt}</div>
      <p class="ss-filter__count" id="ss-count" aria-live="polite">8 lines</p>
    </div>
    <div class="ss-lines" data-n="8" data-odd="0">{''.join(cards)}</div>
    <article class="ss-choke reveal" id="strangled" aria-labelledby="ss-choke-h">
      <div class="ss-choke__main">
        <p class="ss-choke__tag">From Choking Hazard, SafeBAE’s campaign on sexual strangulation</p>
        <h3 id="ss-choke-h">If you were choked or strangled</h3>
        <p class="ss-choke__lead">Go to an ER today, even with no marks and even if you agreed to it, if you:</p>
        <ul class="ss-choke__signs">{''.join(f'<li>{esc(x)}</li>' for x in CHOKE_SIGNS)}</ul>
      </div>
      <div class="ss-choke__side">
        <p class="ss-choke__say"><span>At the front desk, say</span> <b>“I was strangled.”</b> <span>Not just “my throat hurts.”</span></p>
        <p class="ss-choke__911"><b>Call 911</b> if someone is unconscious, has trouble breathing, has a swelling neck, seems confused, has one-sided weakness or numbness, has a seizure, or shows stroke signs. Symptoms can show up later: throat swelling can develop hours later, and a torn-artery stroke can occur days or weeks later.</p>
        <div class="btns">{btn('What to know about choking', 'choking-hazard.html', 'slate', 'sm', arrow=True)}</div>
      </div>
    </article>
  </div>
</section>

<section class="band band--paper" id="healing">
  <div class="wrap">
    <div class="section-head"><div><h2>Healing takes time, and support.</h2>
      <p class="lede lede--full">Connection with peers, supportive communities, or professionals can ease feelings of isolation, reduce guilt or shame, and provide tools for coping. Even when survivors understand they are not to blame, it often takes time and support to fully believe it.</p></div></div>
    <div class="ss-heal reveal">
      <div class="ss-heal__txt">
        <p>For some, reconnecting with their body and emotions may feel overwhelming. Some survivors experience disconnection or turn to risky behaviors to manage pain. While facing these feelings can be difficult, avoiding them can cause further harm. With compassionate support and mental health resources, survivors can begin to process trauma, reclaim safety, and move toward healing.</p>
        <div class="btns">{btn('Find a local rape crisis center', 'https://www.raliance.org/rape-crisis-centers/', 'slate')}<button class="btn btn--ghost" data-open-help type="button">All hotlines</button></div>
        <a class="ss-tattoo" href="fordaisy-tattoos.html"><span class="ss-tattoo__img">{img('fordaisy28', 'Daisy Coleman tattooing a client')}</span><span class="ss-tattoo__txt"><small>#ForDaisy</small><b>Tattoos &amp; healing</b><span>SafeBAE co-founder Daisy Coleman was a tattoo artist. Some survivors describe tattoos as one path to reclaiming their bodies.</span><em>Read more</em></span></a>
      </div>
      <div class="ss-practice">
        <h3>Healing from a traumatic relationship</h3>
        <p>Small practices that can help. Tap the ones you want to try, or let us pick one for today.</p>
        <div class="ss-tiles" role="group" aria-label="Healing practices">{tiles}</div>
        <div class="ss-pick"><button class="btn btn--mint btn--sm" type="button" id="ss-pick">Pick one for me</button><output id="ss-today" aria-live="polite"></output></div>
      </div>
    </div>
  </div>
</section>

<section class="band band--aqua" id="dating">
  <div class="wrap">
    <div class="section-head"><div><p class="eyebrow">Film + teaching guide &middot; with <i>Teen Vogue</i></p><h2>Dating after sexual assault</h2></div></div>
    <div class="ss-date reveal">
    <div class="ss-date__media">{yt('rIxB8vlmAjY', 'Intimacy & Dating After Sexual Assault', label='With Teen Vogue')}</div>
    <div class="ss-date__txt">
      <p>Relationships and intimacy after assault can bring new challenges. Survivors may face triggers that complicate dating, while partners may feel uncertain about how to provide support. To open space for these conversations, SafeBAE partnered with <i>Teen Vogue</i> to produce <a class="link" href="film-dating-after-sexual-assault.html">Dating After Sexual Assault</a>.</p>
      <p>The short video and teaching guide affirm that healing looks different for everyone and offer practical tools for navigating trust, communication, and boundaries, creating space for survivors and partners to explore healthy intimacy after trauma.</p>
      <div class="btns">{btn('Film + teaching guide', 'film-dating-after-sexual-assault.html', 'slate', arrow=True)}</div>
    </div>
    </div>
    <div class="ss-now"><span><b>If you’d like immediate support from a trained professional,</b> you can text <strong>LOVEIS</strong> to <strong>22522</strong>.</span><span class="copy"><span>22522</span><button type="button" data-copy="22522">Copy</button></span></div>
  </div>
</section>

<section class="band band--slate" id="when-someone-tells-you">
  <div class="wrap">
    <div class="section-head ss-tell__head"><div><h2>When someone tells you they’ve been assaulted</h2>
      <p class="lede lede--full">Opening up about sexual violence takes tremendous courage. If someone chooses to share their experience with you, here’s how to show up for them.</p></div>
      <div class="btns section-head__act">{btn('How to support a friend (FAQ)', 'faq.html#faq-healing', 'ghost')}</div></div>
    <div class="ss-ways reveal">{ways}</div>
  </div>
</section>

<section class="band band--mist" id="what-to-say">
  <div class="wrap">
    <div class="section-head"><div><h2>Words that help, and words that hurt</h2></div></div>
    <div class="ss-say reveal">
      <div class="ss-say__col ss-say__col--do"><small>Try saying</small><h3>Words that help</h3><ul>{say}</ul></div>
      <div class="ss-say__col ss-say__col--dont"><small>Don’t say</small><h3>Words to avoid</h3><ul>{dont}</ul></div>
    </div>
    <div class="ss-print" data-gallery>
      <button type="button" data-src="{imgsrc('8x8-what-not-to-say-poster-pdf')}" data-cap="What to say vs. what not to say" aria-label="Enlarge the poster">{img('8x8-what-not-to-say-poster-pdf', 'Poster: What to say to a friend who shares they have been assaulted, versus what not to say')}</button>
      <div><b>Print it as a poster</b><span>These phrases as a free “What to say vs. what not to say” poster for classrooms, counseling offices, hallways and student spaces.</span></div>
      <div class="btns">{btn('Download (PDF)', WPU + '2025/08/8x8-what-not-to-say-poster.pdf', 'slate')}</div>
    </div>
  </div>
</section>

<section class="band band--mint" id="shareable-graphics">
  <div class="wrap">
    <div class="section-head"><div><p class="eyebrow">4 graphics &middot; free to print</p><h2>Shareable graphics</h2></div><div class="btns section-head__act">{btn('Download all posters (.zip)', POSTERS_ZIP, 'slate')}{btn('See every poster', 'posters.html', 'ghost', arrow=True)}</div></div>
    <div class="ss-gal reveal" data-gallery>{gal}</div>
  </div>
</section>

<section class="band band--paper" id="media">
  <div class="wrap">
    <div class="section-head"><div><p class="eyebrow">101 books, films &amp; podcasts</p><h2>Survivor-centered media</h2></div>
      <div class="ss-shop section-head__act"><p>You can support SafeBAE’s work by purchasing books from our digital bookshop.</p>{btn('SafeBAE on Bookshop.org', BOOKSHOP, 'mint', 'sm')}</div></div>
    <div data-tabs>
      <div class="ss-cats" role="tablist" aria-label="Media by type">{''.join(tabs)}</div>
      {''.join(panels)}
    </div>
  </div>
</section>

<section class="band band--deep" id="off-campus">
  <div class="wrap ss-oc reveal">
    <div class="ss-oc__intro">
      <p class="eyebrow">A recent favorite</p>
      <h2>Off Campus</h2>
      <p>Based on Elle Kennedy’s bestselling series, <i>Off Campus</i> follows Hannah Wells, a survivor of sexual assault, and Garrett Graham. The story models consent and healthy sexual relationships, from a partner who checks in to one who stops when she isn’t fully comfortable.</p>
      <figure class="ss-oc__q"><blockquote class="quote">{esc(OC_QUOTE[0])}</blockquote><figcaption class="cite">{esc(OC_QUOTE[1])}</figcaption></figure>
      <p class="ss-oc__note">Tap a slide to enlarge it.</p>
    </div>
    <div class="ss-oc__set"><p><b>Let’s talk about Off Campus</b><span class="chip">Mentions SA</span></p>{player(OC1, 'Let’s talk about Off Campus: seven slides', 'sp-portrait')}</div>
    <div class="ss-oc__set"><p><b>Green flags from season 1</b><span class="chip">Spoilers</span></p>{player(OC2, 'Green flags from Off Campus season 1: seven slides', 'sp-portrait', interval=5600)}</div>
  </div>
</section>

<section class="band band--paper band--tight">
  <div class="wrap">
    <div class="section-head"><div><h2>More support and answers</h2></div></div>
    {next_cards([('Your rights', 'Title IX', 'What your school owes you, supportive measures, and who to talk to.', 'title-ix.html'),
                 ('Research', 'Myths & facts', 'Why survivors don’t report, and what the research actually says.', 'myths-facts.html'),
                 ('Answers', 'FAQ', 'Straight answers about consent, reporting, healing and more.', 'faq.html')])}
  </div>
</section>
{vibe_band()}
{give_band_calm()}
'''
    js = r'''<script>
(function(){
  var f = document.querySelector('.ss-filter'), out = document.getElementById('ss-count'), grid = document.querySelector('.ss-lines');
  if(f && grid){ var bs = f.querySelectorAll('button'), cards = grid.querySelectorAll('.ss-line');
    function apply(t){ var n = 0, last = null;
      cards.forEach(function(c){ var on = t === 'all' || (' ' + c.getAttribute('data-tags') + ' ').indexOf(' ' + t + ' ') >= 0; c.hidden = !on; c.removeAttribute('data-last');
        if(on){ n++; c.setAttribute('data-i', n); last = c; } else c.removeAttribute('data-i'); });
      if(last) last.setAttribute('data-last', '');
      grid.setAttribute('data-n', n); grid.setAttribute('data-odd', n % 2 ? '1' : '0');
      if(out) out.textContent = n + (n === 1 ? ' line' : ' lines');
      grid.classList.remove('is-in'); void grid.offsetWidth; grid.classList.add('is-in'); }
    bs.forEach(function(b){ b.addEventListener('click', function(){ bs.forEach(function(x){ x.setAttribute('aria-pressed', String(x === b)); }); apply(b.getAttribute('data-f')); }); }); }
  var tiles = document.querySelectorAll('.ss-tiles button'), today = document.getElementById('ss-today'), pk = document.getElementById('ss-pick');
  tiles.forEach(function(t){ t.addEventListener('click', function(){ t.setAttribute('aria-pressed', t.getAttribute('aria-pressed') === 'true' ? 'false' : 'true'); t.classList.remove('pick'); }); });
  if(pk) pk.addEventListener('click', function(){ var i = Math.floor(Math.random() * tiles.length); tiles.forEach(function(x){ x.classList.remove('pick'); }); var t = tiles[i]; t.classList.add('pick'); t.setAttribute('aria-pressed', 'true'); today.textContent = 'For today: ' + t.textContent + '.'; });
})();
</script>'''
    page('survivor-support.html', 'Survivor Support & Healing · SafeBAE',
         'Support resources for survivors and those helping them, including hotlines, healing tools, and guidance for when someone discloses assault.',
         body, active='resources', body_class='ss', head_extra=f'<style>{SP_CSS}{SS_CSS}</style>', scripts=js)



# =====================================================================
# 2. TITLE IX
# =====================================================================
TIMELINE = [
  ('1972', '1972', 'Title IX Enacted', 'Title IX of the Education Amendments of 1972 is signed into law, prohibiting sex-based discrimination in any education program or activity receiving federal financial assistance.'),
  ('1977', '1977', 'Alexander v. Yale', 'A group of students filed a lawsuit against Yale University, arguing that the university’s failure to address sexual harassment constituted a violation of Title IX. This was the first case to use Title IX to argue that sexual harassment is a form of sex discrimination.'),
  ('1992', '1992', 'Franklin v. Gwinnett County Public Schools', 'This landmark decision marked the first successful interpretation of Title IX to cover sexual harassment, significantly strengthening the law’s enforcement and protections against gender-based discrimination in educational settings.'),
  ('2011', '2011', 'The “Dear Colleague” Letter', 'The Obama administration’s Office for Civil Rights issues the “Dear Colleague” Letter, clarifying that sexual violence is a form of sexual harassment prohibited by Title IX and outlining schools’ responsibility to respond promptly and equitably to reports of sexual violence.'),
  ('2017', '2017', 'Rescission of 2011 Guidance', 'The 2011 guidance is rescinded by the Trump/DeVos administration, and interim guidance is provided, allowing schools more flexibility in handling sexual violence cases and decreasing protections for survivors.'),
  ('2020', '2020', 'The Trump/DeVos Title IX Rules', 'In May 2020, new Title IX regulations are published. These regulations require schools to follow specific procedures for investigating and adjudicating sexual harassment and assault cases, including live hearings and cross-examinations. These rules make it harder for survivors to get the support they need.'),
  ('2022', '2022', 'Proposed Title IX Rule', 'After over a year of pressure from organizers, the Biden administration proposes new changes to the Title IX regulations on June 23, 2022 (the 50th anniversary of Title IX) to better protect students and ensure fair processes. These changes aimed to address some of the criticisms of the 2020 rules.'),
  ('2024', '2024', 'Final Rule Update', 'New Title IX rules are finalized and released on April 19, 2024, and take effect August 1, 2024. These rules provided enhanced protections for students and survivors, including LGBTQ+ students and pregnant and postpartum students.'),
  ('Jan 2025', 'January 9, 2025', 'Vacatur and Post-Decision Status', 'A federal district court issues a decisive ruling that vacates the 2024 Final Rule in its entirety. The Department of Education has confirmed that the 2024 Title IX regulations and related resources are not effective in any jurisdiction, meaning the 2020 regulations are the rules schools must follow today.'),
  ('Jun 2026', 'June 16, 2026', 'Civil Rights Enforcement Moves to the DOJ', 'The U.S. Department of Education moves civil rights enforcement from OCR to the Department of Justice, shifting how harassment and discrimination complaints in K-12 schools and colleges are investigated and resolved, and making it even more confusing for students and families to understand where and how to seek justice.'),
  ('Today', 'Today', 'What Comes Next?', 'The future of Title IX and its enforcement at the federal level remains uncertain, and yet students still have the legal right to be protected in their schools.'),
]
RIGHTS = ['Your school is required by law to ensure your safety on campus.',
          'Your school is required to have established procedures for handling complaints of sexual discrimination, harassment, or violence.',
          'You have the right to report sexual harassment or assault to your school, and your school MUST take steps to ensure victims do not have to share space, such as classes, with their abuser.',
          'Your school should inform you of your right to counseling services and your right to make a report to law enforcement.',
          'Your school may NOT retaliate against someone filing a complaint and must keep the complainant safe from retaliatory harassment.',
          'Schools can NOT discourage you from continuing your education, and must provide reasonable accommodations for your safety.']
VIOLATION = ['the survivor experiences harassment during the reporting process',
             'the investigation isn’t prompt and impartial',
             'the survivor faces retaliation',
             'the school fails to provide reasonable accommodations or a no-contact order']
MEASURES = [
  ('Care & support', ['Referral to health services', 'Provision of resources for medical and/or psychological support or disability', 'Access to community resources', 'Referral to survivor advocate services']),
  ('Safety at school', ['School grounds-based no-contact orders', 'Imposition of interim suspension for the perpetrator', 'Limiting a perpetrator’s access to activities', 'Arranging cafeteria and study hall schedules']),
  ('Classes & schoolwork', ['Change in academic schedule', 'Change in course load, including reduced course load or alternative assignments', 'Academic support and tutoring', 'Option for independent study',
                            'Excused class absence for treatment, hospitalization, and medical or mental health conditions', 'Assurance that survivors will suffer no academic penalties for court or conduct proceedings',
                            'Retrospective withdrawal from classes', 'Immediate withdrawal from a class', 'Leave of absence from the institution']),
  ('Anything else', ['Any other reasonable safe forms of assistance and support as requested by the survivor to help them feel safe and supported']),
]
TELL_ME_LIES = [('1', 'Tell Me Lies… but not about Title IX', 'Tell Me Lies… but not about Title IX. A new season of Tell Me Lies is out, and sexual assault is a central plotline. We’re not doing a recap; we’re doing a reality check on what the show portrays.'),
                ('2', 'What happens in the show', 'Tell Me Lies is a Hulu drama set around a college friend group. This season includes a scene where Lucy is brought into an admin-style meeting with another student who was assaulted by the same person, and the conversation is framed like they need Lucy to “come forward” so the stories can corroborate each other.'),
                ('3', 'What the show portrays', 'What the show portrays: a surprise group meeting, an implied requirement that survivors corroborate each other, and admin-driven urgency over survivor choice.'),
                ('4', 'What Title IX is actually supposed to do', 'What Title IX is actually supposed to do: the school’s job starts with the Title IX Coordinator; supportive measures are offered immediately, even if no formal complaint is filed; privacy and confidentiality are built in; the complainant chooses whether to file a formal complaint; parties are handled separately and get written notice.'),
                ('5', 'What this storyline teaches viewers', 'What this storyline teaches viewers, and why it is harmful: four lies, including “you need another survivor to back you up” and “if you don’t do the formal process, nothing happens.”'),
                ('6', 'Real prevention starts here', 'When a show makes sexual assault a major storyline, it has a responsibility not to normalize a process that pressures survivors or makes reporting look like a trap. Real prevention starts with these conversations.')]
TIX_POSTS = [('Why Students Walk Out: The Westlake High Protest and the Power of Youth Activism', '2025-05-06', 'https://www.safebae.org/why-students-walk-out-the-westlake-high-protest-and-the-power-of-youth-activism/', 'blog-why-students-walk-out-the-westlake-high-prot'),
             ('A Future Without the Department of Education: What We Must Do Now', '2025-04-21', 'https://www.safebae.org/a-future-without-the-department-of-education-what-we-must-do-now/', 'blog-a-future-without-the-department-of-education'),
             ('In a Time of Federal Cutbacks, Students Are Demanding Consent Education—We Need to Keep Showing Up', '2025-01-31', 'https://www.safebae.org/in-a-time-of-federal-cutbacks-students-are-demanding-consent-education-we-need-to-keep-showing-up/', 'blog-in-a-time-of-federal-cutbacks-students-are-d')]
TIX_FAQ = 'https://www.safebae.org/what-is-title-ix-student-rights/'
_P = '<svg viewBox="0 0 24 44" focusable="false"><circle cx="12" cy="7.5" r="6.2"/><path d="M2.4 43V26a9.6 9.6 0 0 1 19.2 0v17z"/></svg>'
PEOPLE = ''.join(f'<i class="{"on" if k < 7 else ""}" style="--d:{k * 80}ms">{_P}</i>' for k in range(10))

TX_CSS = '''
/* ---------- hero ---------- */
.tx-hero{background:var(--grain) var(--logo-teal); color:#fff}
.tx-hero__grid{display:grid; grid-template-columns:minmax(0,7fr) minmax(0,5fr); gap:clamp(28px,4.4vw,64px); align-items:center; padding-block:clamp(48px,6vw,88px)}
.tx-hero h1{font-size:clamp(4.2rem,12vw,10rem); font-stretch:125%; font-weight:900; line-height:.8; letter-spacing:-.03em; margin:0; text-transform:uppercase}
.tx-hero h1 > span{display:block; font-size:clamp(1.6rem,3.2vw,2.6rem); font-stretch:112%; letter-spacing:-.01em; line-height:1.05; margin-top:.35em; color:#fff}
.tx-hero .lede{color:rgba(255,255,255,.92); margin-top:24px; max-width:none}
.tx-hero__media{position:relative}
.tx-hero__photo{position:relative; margin-left:18%}
.tx-hero__photo img{width:100%; aspect-ratio:4/3; object-fit:cover; object-position:60% 30%; border-radius:var(--r-xl); box-shadow:var(--shadow-soft)}
.tx-hero__photo .sticker{position:absolute; right:-10px; top:18px}
.tx-law{position:relative; z-index:1; width:min(92%,500px); margin:-72px 0 0; background:var(--grain) var(--slate-deep); border-radius:var(--r-xl); padding:clamp(20px,2.6vw,30px); box-shadow:var(--shadow-soft)}
.tx-law small{display:block; font-family:var(--mono); font-size:.7rem; letter-spacing:.05em; text-transform:uppercase; color:var(--mint); font-weight:600; text-wrap:balance}
.tx-law blockquote{margin:10px 0 0; font-family:var(--display); font-stretch:104%; font-weight:700; font-size:clamp(1.02rem,1.5vw,1.22rem); line-height:1.36; text-wrap:pretty}
.tx-law blockquote::before{content:"\\201C"; display:block; font-size:3.4em; line-height:.55; color:var(--mint); font-stretch:125%; margin-bottom:.05em}
@media (max-width:900px){.tx-hero__grid{grid-template-columns:minmax(0,1fr)} .tx-hero__media{max-width:560px}}
@media (max-width:560px){.tx-hero__photo{margin-left:0} .tx-law{width:auto; margin:-40px 10px 0}}

/* ---------- what it does ---------- */
.tx-does{display:grid; grid-template-columns:repeat(3,minmax(0,1fr)); gap:var(--gap)}
.tx-does > div{display:flex; flex-direction:column; gap:10px; border-radius:var(--r-xl); padding:var(--pad-card); background:var(--mist); border:1px solid var(--line); min-width:0}
.tx-does i{width:38px; height:38px; border-radius:50%; background:var(--mint) url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 24 24'%3E%3Cpath d='M6 12.5l4 4 8-9' fill='none' stroke='%231d414e' stroke-width='3' stroke-linecap='round' stroke-linejoin='round'/%3E%3C/svg%3E") center/20px no-repeat}
.tx-does b{display:block; font-family:var(--display); font-stretch:110%; font-size:1.5rem; line-height:1.1; color:var(--logo-teal)}
.tx-does p{margin:0; color:var(--ink-soft)}
@media (max-width:860px){.tx-does{grid-template-columns:minmax(0,1fr)} .tx-does > div{display:grid; grid-template-columns:auto minmax(0,1fr); gap:4px 16px} .tx-does i{grid-row:1 / span 2} }

/* ---------- 7 in 10 pictograph ---------- */
.tx-pict{display:flex; align-items:flex-end; gap:clamp(14px,3vw,44px)}
.tx-pict__n{flex:none; font-family:var(--display); font-weight:900; font-stretch:125%; font-size:clamp(4.4rem,11.2vw,9.8rem); line-height:.74; letter-spacing:-.04em; color:var(--slate); margin-bottom:-.04em}
.tx-people{flex:1; display:grid; grid-template-columns:repeat(10,minmax(0,1fr)); gap:clamp(4px,1.1vw,16px); align-items:end; min-width:0}
.tx-people i{display:block; min-width:0}
.tx-people svg{display:block; width:100%; height:auto; overflow:visible; fill:transparent; stroke:var(--slate); stroke-width:3px; vector-effect:non-scaling-stroke; stroke-linejoin:round}
.tx-people svg *{vector-effect:non-scaling-stroke}
.tx-people i.on svg{fill:var(--slate)}
.js .tx-people i.on svg{fill:transparent; transition:fill .45s var(--ease) var(--d)}
.js .tx-pict.seen .tx-people i.on svg{fill:var(--slate)}
.tx-people i:not(.on) svg{stroke-dasharray:5 5}
.tx-stat__txt{display:grid; grid-template-columns:minmax(0,7fr) minmax(0,5fr); gap:clamp(16px,4vw,56px); align-items:stretch; margin-top:clamp(20px,2.6vw,32px); padding-top:clamp(18px,2.4vw,28px); border-top:2px solid rgba(29,65,78,.2)}
.tx-stat__say{font-family:var(--display); font-stretch:104%; font-weight:800; font-size:clamp(1.3rem,2.25vw,1.86rem); line-height:1.2; margin:0; text-wrap:pretty}
.tx-stat__more{display:flex; flex-direction:column; align-items:flex-start; gap:14px; min-width:0}
.tx-stat__more p{margin:0; font-weight:600; font-size:1.06rem; line-height:1.5}
.tx-stat__more .btn{margin-top:auto}
@media (max-width:760px){.tx-stat__txt{grid-template-columns:minmax(0,1fr)} .tx-pict{flex-direction:column; align-items:stretch; gap:18px} .tx-people svg{stroke-width:2px} .tx-people i:not(.on) svg{stroke-dasharray:3 3}}

/* ---------- explainer + quiz ---------- */
.tx-vq{display:grid; grid-template-columns:minmax(0,7fr) minmax(0,5fr); gap:clamp(22px,3.4vw,48px); align-items:stretch}
.tx-vq__vid{display:flex; flex-direction:column; min-width:0}
.tx-vq__vid h2{margin-bottom:.55em}
.tx-vq__vid .vid{border-radius:var(--r-xl)}
.tx-quiz a.link{color:var(--logo-teal)}
.tx-quiz{background:var(--mint); color:var(--slate); border-radius:var(--r-xl); padding:var(--pad-card); display:flex; flex-direction:column; min-width:0}
.tx-quiz h2{font-size:clamp(1.7rem,2.8vw,2.3rem); margin:0 0 .2em}
main .tx-quiz .eyebrow{color:var(--slate)}
.tx-prog{display:flex; gap:6px; margin:10px 0 22px}
.tx-prog span{flex:1; height:6px; border-radius:3px; background:rgba(29,65,78,.18); transition:background .3s}
.tx-prog span.done{background:var(--slate)}
.tx-step + .tx-step{margin-top:20px; padding-top:20px; border-top:1px solid rgba(29,65,78,.2)}
.js .tx-step{display:none; margin:0; padding:0; border:0}
.js .tx-step.on{flex:1; display:flex; flex-direction:column; animation:txin .35s var(--ease)}
@keyframes txin{from{transform:translateY(10px)}}
.tx-q{font-family:var(--display); font-stretch:108%; font-weight:800; font-size:clamp(1.3rem,2.1vw,1.62rem); line-height:1.15; margin:0 0 16px}
.tx-choices{flex:1; display:grid; grid-template-columns:1fr 1fr; gap:10px}
.tx-choices button{font:inherit; font-family:var(--display); font-weight:800; font-stretch:108%; font-size:1.25rem; min-height:72px; padding:16px; border-radius:14px; border:2px solid var(--slate); background:#fff; color:var(--slate); cursor:pointer; box-shadow:0 4px 0 rgba(29,65,78,.9); transition:background .2s, color .2s, transform .18s, box-shadow .18s}
.tx-choices button:hover{background:var(--slate); color:#fff; transform:translateY(-2px); box-shadow:0 6px 0 rgba(22,53,64,.9)}
.tx-unsure{align-self:flex-start; margin-top:16px; font:inherit; font-weight:700; background:none; border:0; color:var(--slate); text-decoration:underline; text-underline-offset:3px; cursor:pointer; padding:6px 0; min-height:32px}
.tx-help{margin-top:8px; background:rgba(255,255,255,.62); border-radius:12px; padding:14px 16px; font-size:.96rem; line-height:1.5}
.tx-res{flex:1; display:flex; flex-direction:column; background:#fff; border-radius:16px; padding:20px 22px}
.tx-res h3{font-size:clamp(1.4rem,2.2vw,1.8rem); margin:0 0 .4em}
.tx-res p{margin:0 0 16px}
.tx-res .btns{gap:8px; margin-top:auto}
@media (max-width:960px){.tx-vq{grid-template-columns:minmax(0,1fr)} .tx-choices{flex:none}}

/* ---------- rights ---------- */
.tx-rights{display:grid; grid-template-columns:minmax(0,7fr) minmax(0,5fr); gap:clamp(24px,4vw,56px); align-items:stretch}
.tx-list{list-style:none; padding:0; margin:0; display:grid; grid-auto-rows:1fr; gap:10px; min-width:0}
.tx-list li{display:flex; align-items:center; gap:14px; margin:0; padding:14px 20px 14px 16px; border-radius:14px; background:var(--mist); font-weight:600; line-height:1.45; font-size:1rem}
.tx-list li::before{content:""; flex:none; width:28px; height:28px; border-radius:50%; background:var(--mint) url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 24 24'%3E%3Cpath d='M6 12.5l4 4 8-9' fill='none' stroke='%231d414e' stroke-width='3' stroke-linecap='round' stroke-linejoin='round'/%3E%3C/svg%3E") center/16px no-repeat}
.tx-who{scroll-margin-top:112px; background:var(--grain) var(--slate); color:#fff; border-radius:var(--r-xl); padding:var(--pad-card); display:flex; flex-direction:column; min-width:0}
.tx-who h3{color:#fff; font-size:clamp(1.5rem,2.4vw,2rem)}
.tx-who p{color:rgba(255,255,255,.9)}
.tx-who ul{margin:0 0 16px; padding-left:1.1em; color:rgba(255,255,255,.9)}
.tx-who li::marker{color:var(--mint)}
.tx-who .btns{margin-top:auto; padding-top:6px; display:grid; grid-template-columns:repeat(auto-fit,minmax(190px,1fr)); gap:10px}
@media (max-width:960px){.tx-rights{grid-template-columns:minmax(0,1fr)} .tx-list{grid-auto-rows:auto}}

/* ---------- timeline ---------- */
.tx-tl__track{position:relative; display:grid; grid-template-columns:repeat(11,minmax(0,1fr)); gap:4px; margin-bottom:22px}
.tx-tl__line{position:absolute; left:4.5%; right:4.5%; top:20px; height:3px; background:var(--line-dark); border-radius:2px}
.tx-tl__line i{display:block; height:100%; width:0; background:var(--mint); transition:width .45s var(--ease); border-radius:2px}
.tx-tl__track button{position:relative; z-index:1; display:flex; flex-direction:column; align-items:center; gap:10px; background:none; border:0; color:rgba(255,255,255,.76); font:inherit; cursor:pointer; padding:4px 0 6px; min-height:56px}
.tx-tl__track .dot{width:20px; height:20px; margin-top:8px; border-radius:50%; background:var(--slate-deep); border:3px solid rgba(209,254,255,.45); transition:all .25s var(--ease)}
.tx-tl__track button:hover .dot{border-color:var(--mint)}
.tx-tl__track button.past .dot{border-color:var(--mint); background:var(--mint)}
.tx-tl__track button[aria-selected="true"] .dot{background:var(--mint); border-color:#fff; transform:scale(1.35)}
.tx-tl__track .lbl{font-family:var(--mono); font-size:.8rem; font-weight:600; letter-spacing:.02em; white-space:nowrap}
.tx-tl__track button[aria-selected="true"] .lbl{color:var(--mint)}
.tx-tl__panel{display:grid; grid-template-columns:minmax(0,5fr) minmax(0,7fr); gap:clamp(20px,4vw,56px); align-items:center; padding:clamp(22px,3vw,40px); border-radius:var(--r-xl); background:rgba(255,255,255,.05); border:1px solid var(--line-dark); min-height:252px}
.tx-tl__panel + .tx-tl__panel{margin-top:12px}
.js .tx-tl__panel{display:none; margin:0} .js .tx-tl__panel.on{display:grid; animation:txin .35s var(--ease)}
.tx-tl__panel .tx-tl__date{font-family:var(--display); font-weight:900; font-stretch:125%; font-size:clamp(3rem,7.4vw,6.4rem); line-height:.88; letter-spacing:-.02em; color:var(--mint); margin:0}
.tx-tl__panel .tx-tl__date--long{font-size:clamp(2rem,4.3vw,3.7rem); line-height:.95}
.tx-tl__panel h3{font-size:clamp(1.4rem,2.4vw,2rem); color:#fff}
.tx-tl__panel p{color:rgba(255,255,255,.9); margin:0}
.tx-tl__nav{display:flex; justify-content:space-between; align-items:center; gap:12px; margin-top:16px}
.tx-tl__nav button{font:inherit; font-weight:700; background:transparent; color:#fff; border:1.5px solid rgba(209,254,255,.32); border-radius:999px; min-height:44px; padding:8px 18px; cursor:pointer; transition:border-color .2s, color .2s}
.tx-tl__nav button:hover{border-color:var(--mint); color:var(--mint)}
.tx-tl__n{font-family:var(--mono); font-size:.8rem; letter-spacing:.08em; color:var(--aqua)}
.tx-tl:not(.ready) .tx-tl__nav,.tx-tl:not(.ready) .tx-tl__track{display:none}
@media (max-width:860px){.tx-tl__track{display:flex; overflow-x:auto; gap:22px; padding:0 4px 8px; scrollbar-width:thin; scroll-snap-type:x proximity} .tx-tl__track button{flex:none; scroll-snap-align:center} .tx-tl__line{display:none} .tx-tl__panel{grid-template-columns:minmax(0,1fr); min-height:0; align-items:start}}

/* ---------- supportive measures ---------- */
.tx-sm{display:grid; gap:16px; background:#fff; border-radius:var(--r-xl); padding:var(--pad-card); box-shadow:var(--shadow-soft)}
.tx-sm__how{margin:0; font-weight:600}
.tx-sm__grp{display:grid; grid-template-columns:170px minmax(0,1fr); gap:10px 20px; align-items:start; padding-top:16px; border-top:1px solid var(--line)}
.tx-sm__grp > b{font-family:var(--mono); font-size:.74rem; letter-spacing:.1em; text-transform:uppercase; color:var(--logo-teal); padding-top:15px; font-weight:600}
.tx-sm__pills{display:grid; grid-template-columns:repeat(2,minmax(0,1fr)); gap:8px}
.tx-sm__pills button{position:relative; display:flex; align-items:center; min-height:50px; font:inherit; font-size:.98rem; font-weight:600; text-align:left; line-height:1.35; padding:10px 16px 10px 46px; border-radius:12px; border:1.5px solid var(--line); background:var(--mist); color:var(--slate); cursor:pointer; transition:background .18s, color .18s, border-color .18s}
.tx-sm__pills button:last-child:nth-child(odd){grid-column:1 / -1}
.tx-sm__pills button::before{content:""; position:absolute; left:15px; top:50%; width:18px; height:18px; margin-top:-9px; border-radius:5px; border:2px solid var(--teal); background:#fff; transition:background .18s, border-color .18s}
.tx-sm__pills button:hover{border-color:var(--teal)}
.tx-sm__pills button[aria-pressed="true"]{background:var(--slate); color:#fff; border-color:var(--slate)}
.tx-sm__pills button[aria-pressed="true"]::before{background:var(--mint) url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 24 24'%3E%3Cpath d='M5 12.5l4.5 4.5L19 7.5' fill='none' stroke='%231d414e' stroke-width='3.4' stroke-linecap='round' stroke-linejoin='round'/%3E%3C/svg%3E") center/12px no-repeat; border-color:var(--mint)}
.tx-sm__bar{display:flex; flex-wrap:wrap; gap:10px 16px; align-items:center; justify-content:space-between; padding-top:16px; border-top:1px solid var(--line)}
.tx-sm__bar output{font-family:var(--mono); font-size:.8rem; letter-spacing:.06em; text-transform:uppercase; font-weight:600; color:var(--logo-teal)}
.tx-sm textarea{width:100%; min-height:150px; font:inherit; font-size:.95rem; padding:12px; border-radius:10px; border:2px solid var(--teal)}
.tx-sm__note{margin:0; font-weight:700; padding:16px 18px; border-radius:14px; background:var(--aqua); line-height:1.45}
@media (max-width:860px){.tx-sm__grp{grid-template-columns:minmax(0,1fr); gap:8px} .tx-sm__grp > b{padding-top:0}}
@media (max-width:620px){.tx-sm__pills{grid-template-columns:minmax(0,1fr)}}
.tx-more{display:grid; grid-template-columns:repeat(2,minmax(0,1fr)); gap:var(--gap); margin-top:var(--gap); align-items:stretch}
.tx-more > div{display:grid; grid-template-columns:clamp(110px,14vw,170px) minmax(0,1fr); gap:clamp(14px,2vw,24px); align-items:center; background:#fff; border-radius:var(--r-xl); padding:18px clamp(16px,2vw,24px) 18px 18px; border:1px solid var(--line); min-width:0}
.tx-more img{width:100%; border-radius:10px}
.tx-more button.tx-zoom{border:0; padding:0; background:none; cursor:zoom-in; border-radius:10px; overflow:hidden}
.tx-more b{display:block; font-family:var(--display); font-stretch:106%; font-size:1.22rem; line-height:1.15; margin-bottom:4px; color:var(--logo-teal)}
.tx-more p{margin:0 0 12px; font-size:.98rem; color:var(--ink-soft); line-height:1.45}
@media (max-width:900px){.tx-more{grid-template-columns:minmax(0,1fr)}}
@media (max-width:440px){.tx-more > div{grid-template-columns:84px minmax(0,1fr); align-items:start}}

/* ---------- media analysis + blog ---------- */
.tx-media{display:grid; grid-template-columns:minmax(0,5fr) minmax(0,7fr); gap:clamp(24px,4vw,56px); align-items:stretch}
.tx-media__deck{min-width:0}
.tx-media__cap{display:flex; flex-wrap:wrap; align-items:center; justify-content:space-between; gap:10px 16px; margin:14px 0 0; font-size:.92rem; color:rgba(255,255,255,.8)}
.tx-media__txt{display:flex; flex-direction:column; min-width:0}
.tx-media__txt .lede{color:rgba(255,255,255,.9); margin-bottom:1em}
.tx-media__q{margin:0; padding:18px 20px; border-radius:16px; background:rgba(255,255,255,.06); border:1px solid var(--line-dark)}
.tx-media__q blockquote{margin:0; color:rgba(255,255,255,.94); font-size:1.02rem; line-height:1.55}
.tx-media__q figcaption{margin-top:8px; font-family:var(--mono); font-size:.86rem; font-weight:600; color:var(--mint)}
.tx-posts{margin-top:auto; padding-top:clamp(18px,2.2vw,26px)}
.tx-posts .sp-post{grid-template-columns:clamp(96px,10vw,128px) minmax(0,1fr) auto; padding:10px 0}
.tx-posts__head{display:flex; flex-wrap:wrap; justify-content:space-between; align-items:baseline; gap:8px 16px; padding-bottom:12px; border-bottom:1px solid var(--line-dark)}
.tx-posts__head h3{margin:0; color:#fff; font-size:1.35rem}
.tx-posts .sp-post:last-child{border-bottom:0; padding-bottom:0}
@media (max-width:960px){.tx-media{grid-template-columns:minmax(0,1fr); gap:0} .tx-media__txt{display:contents} .tx-media__deck{order:1; max-width:460px; width:100%; margin:4px auto 26px} .tx-media__q{order:2} .tx-posts{order:3; margin-top:0}}

/* ---------- schools can do more ---------- */
.tx-more2{display:grid; grid-template-columns:repeat(2,minmax(0,1fr)); gap:clamp(24px,4vw,56px); align-items:stretch}
.tx-more2__txt{display:flex; flex-direction:column; min-width:0}
.tx-more2__txt .btns{margin-top:auto; padding-top:10px}
.tx-better{color:var(--slate); font-weight:800; text-decoration:underline; text-decoration-color:var(--mint); text-decoration-thickness:3px; text-underline-offset:4px}
.tx-photo{position:relative; min-height:320px}
.tx-photo img{position:absolute; inset:0; width:100%; height:100%; object-fit:cover; object-position:50% 60%; border-radius:var(--r-xl); box-shadow:var(--shadow-soft)}
.tx-photo .sticker{position:absolute; right:-8px; top:20px}
@media (max-width:860px){.tx-more2{grid-template-columns:minmax(0,1fr); gap:0} .tx-more2__txt{display:contents} .tx-more2__txt > p{order:2} .tx-more2__txt > .btns{order:3; margin-top:0; padding-top:4px} .tx-photo{order:1; min-height:0; aspect-ratio:4/3; margin:6px 0 22px} .tx-photo .sticker{right:8px}}
'''


def title_ix():
    tl_btns, tl_panels = [], []
    for i, (short, full, h, txt) in enumerate(TIMELINE):
        tl_btns.append(f'<button type="button" role="tab" id="tl-t{i}" aria-controls="tl-p{i}" aria-selected="{str(i == 0).lower()}" tabindex="{0 if i == 0 else -1}"><span class="dot"></span><span class="lbl">{esc(short)}</span></button>')
        long = ' tx-tl__date--long' if len(full) > 6 else ''
        tl_panels.append(f'<article class="tx-tl__panel{" on" if i == 0 else ""}" role="tabpanel" id="tl-p{i}" aria-labelledby="tl-t{i}"><p class="tx-tl__date{long}">{esc(full)}</p><div><h3>{esc(h)}</h3><p>{esc(txt)}</p></div></article>')
    rights = ''.join(f'<li>{esc(r)}</li>' for r in RIGHTS)
    viol = ''.join(f'<li>{esc(v)}</li>' for v in VIOLATION)
    sm = ''.join(f'<div class="tx-sm__grp"><b>{esc(g)}</b><div class="tx-sm__pills">' + ''.join(f'<button type="button" aria-pressed="false">{esc(x)}</button>' for x in items) + '</div></div>' for g, items in MEASURES)
    tml = [(n, c, alt) for n, c, alt in TELL_ME_LIES]
    posts = ''.join(post_row(*p) for p in TIX_POSTS)

    body = f'''
<section class="tx-hero sp-hero">
  <span class="wm-daisy" aria-hidden="true"></span>
  <div class="wrap tx-hero__grid">
    <div class="rise">
      {crumbs(('Home', 'index.html'), ('Resources', 'resources.html'), ('Title IX', None))}
      <h1>Title IX <span>Your <span class="mk">rights</span> at school</span></h1>
      <p class="lede">Title IX is a federal civil rights law that protects students from sex discrimination in schools and guarantees the right to an education free from harassment, assault, and inequity. Every student deserves to know these protections exist.</p>
      <div class="btns">{btn('Is my school covered?', '#covered', 'mint', arrow=True)}{btn('Supportive measures', '#supportive-measures', 'ghost')}</div>
    </div>
    <div class="tx-hero__media">
      <div class="tx-hero__photo">{img('img-2395', 'Two SafeBAE educators leading a session in a classroom', loading='eager')}<span class="sticker sticker--r">Know your rights</span></div>
      <figure class="tx-law"><small>Title IX of the Education Amendments of 1972</small>
        <blockquote>No person in the United States shall, on the basis of sex, be excluded from participation in, be denied the benefits of, or be subjected to discrimination under any education program or activity receiving Federal financial assistance.</blockquote></figure>
    </div>
  </div>
</section>

<section class="band band--paper">
  <div class="wrap">
    <div class="section-head"><div><h2>So, what does it do?</h2></div></div>
    <div class="tx-does reveal">
      <div><i aria-hidden="true"></i><b>Prohibits discrimination</b><p>Title IX prohibits sex-based discrimination in any school or educational program that receives federal funding.</p></div>
      <div><i aria-hidden="true"></i><b>Protects all students</b><p>Title IX protections apply to all students, regardless of gender identity or expression.</p></div>
      <div><i aria-hidden="true"></i><b>Covers various issues</b><p>Title IX covers a wide range of issues, including sexual harassment, assault, and other forms of gender-based violence.</p></div>
    </div>
  </div>
</section>

<section class="band band--mint band--tight tx-stat">
  <div class="wrap">
    <div class="tx-pict" role="img" aria-label="70 percent: 7 out of 10 students"><b class="tx-pict__n" aria-hidden="true">70%</b><span class="tx-people" aria-hidden="true">{PEOPLE}</span></div>
    <div class="tx-stat__txt">
      <p class="tx-stat__say">of students in SafeBAE’s national school climate survey said their school didn’t adequately teach their Title IX rights.</p>
      <div class="tx-stat__more"><p>It is important to know your rights in order to protect yourself or a friend.</p>{btn('Read the full answer', TIX_FAQ, 'slate', 'sm')}</div>
    </div>
  </div>
</section>

<section class="band band--slate" id="covered">
  <div class="wrap tx-vq reveal">
    <div class="tx-vq__vid"><p class="eyebrow">Animated explainer</p><h2>Title IX explained</h2>{yt('cdtPRr_5wXE', 'Title IX Explained', label='Animated explainer')}</div>
    <div class="tx-quiz" id="txQuiz">
      <p class="eyebrow">Take the 2-question quiz</p>
      <h2>Is my school covered by Title IX?</h2>
      <div class="tx-prog" aria-hidden="true"><span data-p="1"></span><span data-p="2"></span></div>
      <section class="tx-step on" data-step="s1" aria-live="polite">
        <p class="tx-q">Do you attend a public or private school?</p>
        <div class="tx-choices"><button type="button" data-a1="public">Public</button><button type="button" data-a1="private">Private</button></div>
        <button type="button" class="tx-unsure" aria-expanded="false" aria-controls="txh1">Unsure?</button>
        <div class="tx-help" id="txh1" hidden><b>Here’s how to find out:</b> Your school’s website likely lists this information under its “About Us” page or pages discussing its history, mission, or governance. You can also check your student handbook, enrollment forms, or ask a teacher or administrator.</div>
      </section>
      <section class="tx-step" data-step="s2" aria-live="polite">
        <p class="tx-q">Does your school receive <em>any</em> federal funding?</p>
        <div class="tx-choices"><button type="button" data-a2="yes">Yes</button><button type="button" data-a2="no">No</button></div>
        <button type="button" class="tx-unsure" aria-expanded="false" aria-controls="txh2">Unsure?</button>
        <div class="tx-help" id="txh2" hidden><b>Here’s how to find out:</b> Information about your school’s funding sources can likely be found in its annual reports, budgets, or financial statements. You can also check <a class="link" href="https://www.usaspending.gov/" target="_blank" rel="noopener">usaspending.gov</a> or see if your school’s tax statements are available online. If you’re not able to find this information online, you can ask a school administrator, guidance counselor, or teacher.</div>
      </section>
      <section class="tx-step" data-step="yes" aria-live="polite"><div class="tx-res">
        <h3>Your school IS covered by Title IX</h3>
        <p>That means your school is legally required to prevent and respond to sex-based discrimination, including sexual harassment and assault, so every student has equal access to education.</p>
        <div class="btns">{btn('Supportive measures', '#supportive-measures', 'slate', 'sm')}{btn('Who do I talk to?', '#coordinator', 'ghost', 'sm')}<button type="button" class="btn btn--ghost btn--sm" data-restart>Start over</button></div></div>
      </section>
      <section class="tx-step" data-step="no" aria-live="polite"><div class="tx-res">
        <h3>Your school is NOT covered by Title IX</h3>
        <p>Private schools that receive no federal funding aren’t bound by Title IX. But your school may still have its own anti-discrimination and safety policies. Check your student handbook or ask an administrator about your rights and protections.</p>
        <div class="btns">{btn('Push for a stronger policy', 'reform-policy.html', 'slate', 'sm')}<button type="button" class="btn btn--ghost btn--sm" data-restart>Start over</button></div></div>
      </section>
    </div>
  </div>
</section>

<section class="band band--paper" id="rights">
  <div class="wrap">
    <div class="section-head"><div><h2>What Title IX laws really mean</h2>
      <p class="lede lede--full">Title IX addresses sexual violence and requires schools to proactively address, remedy, and eliminate sexual violence on their campuses. You are protected under Title IX regardless of your gender and how you identify.</p></div></div>
    <div class="tx-rights reveal">
    <ul class="tx-list">{rights}</ul>
    <div class="tx-who" id="coordinator">
      <p class="eyebrow">Who do I talk to?</p>
      <h3>Go to your Title IX Coordinator</h3>
      <p>When in doubt, go directly to the school Title IX Director (sometimes called the Title IX Coordinator). Your school website should have that information, or you can ask the school secretary.</p>
      <p style="margin-bottom:8px"><b>A school is in violation of Title IX if:</b></p>
      <ul>{viol}</ul>
      <p>Title IX laws are always changing, which is why knowing what is available to protect you is so crucial.</p>
      <div class="btns">{btn('Read the full FAQ answer', TIX_FAQ, 'mint', 'sm')}<button class="btn btn--ghost btn--sm" type="button" data-open-help>Talk to someone now</button></div>
    </div>
    </div>
  </div>
</section>

<section class="band band--deep" id="timeline">
  <div class="wrap">
    <div class="section-head"><div><p class="eyebrow">11 moments &middot; 1972 to today</p><h2>Timeline of Title IX</h2><p class="lede lede--full" style="color:rgba(255,255,255,.9)">Select a year to read what changed.</p></div></div>
    <div class="tx-tl" id="txTl">
      <div class="tx-tl__track" role="tablist" aria-label="Title IX timeline"><div class="tx-tl__line" aria-hidden="true"><i></i></div>{''.join(tl_btns)}</div>
      <div class="tx-tl__panels">{''.join(tl_panels)}</div>
      <div class="tx-tl__nav"><button type="button" data-tl="-1">&#8249; Earlier</button><span class="tx-tl__n" aria-live="polite">1 of {len(TIMELINE)}</span><button type="button" data-tl="1">Later &#8250;</button></div>
    </div>
  </div>
</section>

<section class="band band--aqua" id="supportive-measures">
  <div class="wrap">
    <div class="section-head"><div><p class="eyebrow">18 supportive measures</p><h2>Support you can ask for, with or without an investigation</h2>
      <p class="lede lede--full">Schools are required to offer supportive measures to students impacted by any form of sex discrimination, including sexual harassment and sexual assault. Students and families can request supportive measures even if they choose not to have an investigation.</p></div></div>
    <div class="tx-sm reveal" id="txSm">
      <p class="tx-sm__how">Tap the measures you want to ask your school about, then copy your list to bring to your Title IX Coordinator, a counselor or a trusted adult.</p>
      {sm}
      <div class="tx-sm__bar"><output id="txSmN">0 selected</output><div class="btns"><button class="btn btn--slate btn--sm" type="button" id="txSmCopy">Copy my list</button><button class="btn btn--ghost btn--sm" type="button" id="txSmClear">Clear</button></div></div>
      <textarea id="txSmOut" hidden aria-label="Your list of supportive measures" readonly></textarea>
      <p class="tx-sm__note">Your school cannot require or pressure you to pursue any of these options. They can be offered and the reporting student can take advantage of them. However, they should never be made to feel they have to leave school or change schools.</p>
    </div>
    <div class="tx-more">
      <div>{img('nwlc-logo-1200x630-1', 'National Women’s Law Center')}<div><b>FAQs brought to you by our friends</b><p>The National Women’s Law Center’s guide to supportive measures in K-12 schools.</p>{btn('Supportive Measures FAQ (K-12)', 'https://nwlc.org/wp-content/uploads/2021/11/Supportive-Measures-FAQ-K12-vF.pdf', 'teal', 'sm')}</div></div>
      <div data-gallery><button type="button" class="tx-zoom" data-src="{imgsrc('13-title-ix-1')}" data-cap="Supportive measures" aria-label="Enlarge the supportive measures graphic">{img('13-title-ix-1', 'Infographic: supportive measures your school can offer a survivor, with or without an investigation')}</button><div><b>Save it as one graphic</b><p>Every supportive measure on one shareable slide.</p><button type="button" class="btn btn--slate btn--sm" onclick="this.closest('[data-gallery]').querySelector('button[data-src]').click()">View the graphic</button></div></div>
    </div>
  </div>
</section>

<section class="band band--slate" id="media-analysis">
  <div class="wrap tx-media reveal">
    <div class="tx-media__deck">{player(tml, 'Tell Me Lies… but not about Title IX: six slides', 'sp-portrait', interval=6000)}
      <p class="tx-media__cap"><span>Tap a slide to enlarge it.</span>{btn('Follow @safe_bae', 'https://www.instagram.com/safe_bae/', 'mint', 'sm')}</p></div>
    <div class="tx-media__txt">
      <p class="eyebrow">Resources, updates &amp; media analysis</p>
      <h2>Tell Me Lies… but not about Title IX</h2>
      <p class="lede">SafeBAE’s blog posts and social media explainers on Title IX, school accountability, and student rights.</p>
      <figure class="tx-media__q"><blockquote>“A new season of Tell Me Lies is out, and sexual assault is a central plotline. We’re not doing a recap… we’re doing a reality check on what the show portrays.”</blockquote>
        <figcaption>@safe_bae</figcaption></figure>
      <div class="tx-posts"><div class="tx-posts__head"><h3>From the SafeBAE blog</h3>{a('All Title IX posts', 'https://www.safebae.org/category/title-ix/', 'arrow-link')}</div>{posts}</div>
    </div>
  </div>
</section>

<section class="band band--paper">
  <div class="wrap tx-more2 reveal">
    <div class="tx-more2__txt">
      <h2>Schools can do more</h2>
      <p>Since 2020, schools have been pulled back and forth between restrictive rules, attempts at expanded protections, and ongoing court challenges. This leaves survivors with fewer options, and schools without clear or consistent guidance. That’s why knowing about Title IX is important, but not enough on its own. <b class="tx-better">Your school has the power to do better.</b></p>
      <p>We created the School Policy Reform Guide to help students, educators, and administrators strengthen policies beyond the bare federal minimum. By adopting trauma-informed, survivor-centered practices, schools can ensure real safety, transparency, and accountability.</p>
      <div class="btns">{btn('For students', 'reform-policy.html', 'slate', arrow=True)}{btn('For administrators', 'policy-reform-guide.html', 'ghost', arrow=True)}</div>
    </div>
    <div class="tx-photo">{img('img-3947', 'Students in a classroom during a SafeBAE session')}<span class="sticker sticker--r">Policy reform guide</span></div>
  </div>
</section>
{give_band()}
'''
    js = r'''<script>
(function(){
  /* quiz */
  var q = document.getElementById('txQuiz');
  if(q){ var steps = q.querySelectorAll('.tx-step'), p1 = q.querySelector('[data-p="1"]'), p2 = q.querySelector('[data-p="2"]');
    function show(n){ steps.forEach(function(s){ s.classList.toggle('on', s.getAttribute('data-step') === n); }); var f = q.querySelector('.tx-step.on button'); if(f && n !== 's1') f.focus({preventScroll:true}); }
    q.addEventListener('click', function(e){ var t = e.target.closest('button'); if(!t) return;
      if(t.hasAttribute('data-a1')){ p1.classList.add('done'); if(t.getAttribute('data-a1') === 'public'){ p2.classList.add('done'); show('yes'); } else show('s2'); }
      else if(t.hasAttribute('data-a2')){ p2.classList.add('done'); show(t.getAttribute('data-a2') === 'yes' ? 'yes' : 'no'); }
      else if(t.classList.contains('tx-unsure')){ var b = document.getElementById(t.getAttribute('aria-controls')); var o = b.hidden; b.hidden = !o; t.setAttribute('aria-expanded', String(o)); }
      else if(t.hasAttribute('data-restart')){ p1.classList.remove('done'); p2.classList.remove('done'); q.querySelectorAll('.tx-help').forEach(function(h){ h.hidden = true; }); q.querySelectorAll('.tx-unsure').forEach(function(b){ b.setAttribute('aria-expanded','false'); }); show('s1'); q.querySelector('[data-a1]').focus({preventScroll:true}); }
    }); }
  /* pictograph */
  var pc = document.querySelector('.tx-pict'); if(pc){ if('IntersectionObserver' in window){ var po = new IntersectionObserver(function(es){ es.forEach(function(e){ if(e.isIntersecting){ pc.classList.add('seen'); po.disconnect(); } }); }, {threshold:.5}); po.observe(pc); } else pc.classList.add('seen'); }
  /* timeline */
  var tl = document.getElementById('txTl');
  if(tl){ tl.classList.add('ready'); var tabs = tl.querySelectorAll('[role="tab"]'), panels = tl.querySelectorAll('.tx-tl__panel'), fill = tl.querySelector('.tx-tl__line i'), n = tl.querySelector('.tx-tl__n'), cur = 0;
    function sel(i, focus){ cur = (i + tabs.length) % tabs.length; tabs.forEach(function(t, k){ var on = k === cur; t.setAttribute('aria-selected', String(on)); t.tabIndex = on ? 0 : -1; t.classList.toggle('past', k < cur); panels[k].classList.toggle('on', on); });
      if(fill) fill.style.width = (cur / (tabs.length - 1) * 100) + '%'; n.textContent = (cur + 1) + ' of ' + tabs.length;
      if(focus) tabs[cur].focus(); var tr = tabs[cur].parentNode; if(tr.scrollWidth > tr.clientWidth) tr.scrollTo({left: tabs[cur].offsetLeft - tr.clientWidth/2 + tabs[cur].offsetWidth/2, behavior:'smooth'}); }
    tabs.forEach(function(t, i){ t.addEventListener('click', function(){ sel(i); }); t.addEventListener('keydown', function(e){ var d = e.key === 'ArrowRight' ? 1 : e.key === 'ArrowLeft' ? -1 : 0; if(d){ e.preventDefault(); sel(cur + d, true); } }); });
    tl.querySelectorAll('[data-tl]').forEach(function(b){ b.addEventListener('click', function(){ sel(cur + (+b.getAttribute('data-tl'))); }); });
    sel(0); }
  /* supportive measures list */
  var sm = document.getElementById('txSm');
  if(sm){ var pills = sm.querySelectorAll('.tx-sm__pills button'), out = document.getElementById('txSmN'), ta = document.getElementById('txSmOut'), cp = document.getElementById('txSmCopy');
    function chosen(){ return Array.prototype.filter.call(pills, function(p){ return p.getAttribute('aria-pressed') === 'true'; }).map(function(p){ return p.textContent; }); }
    function upd(){ var c = chosen(); out.textContent = c.length + ' selected'; if(!ta.hidden) ta.value = text(c); }
    function text(c){ return 'Supportive measures I would like to ask about:\n' + c.map(function(x){ return '- ' + x; }).join('\n'); }
    pills.forEach(function(p){ p.addEventListener('click', function(){ p.setAttribute('aria-pressed', p.getAttribute('aria-pressed') === 'true' ? 'false' : 'true'); upd(); }); });
    cp.addEventListener('click', function(){ var c = chosen(); if(!c.length){ out.textContent = 'Pick at least one first'; return; } var t = text(c);
      function fallback(){ ta.hidden = false; ta.value = t; ta.focus(); ta.select(); cp.textContent = 'Select and copy below'; }
      if(navigator.clipboard && navigator.clipboard.writeText){ navigator.clipboard.writeText(t).then(function(){ cp.textContent = 'Copied'; setTimeout(function(){ cp.textContent = 'Copy my list'; }, 1600); }, fallback); } else fallback(); });
    document.getElementById('txSmClear').addEventListener('click', function(){ pills.forEach(function(p){ p.setAttribute('aria-pressed','false'); }); ta.hidden = true; cp.textContent = 'Copy my list'; upd(); }); }
})();
</script>'''
    page('title-ix.html', 'Title IX · SafeBAE',
         'Understand Title IX: student rights, reporting options, how schools must respond to sexual harassment, and a timeline of the law’s key changes.',
         body, active='resources', body_class='tx', head_extra=f'<style>{SP_CSS}{TX_CSS}</style>', scripts=js)


def build():
    survivor_support()
    title_ix()


if __name__ == '__main__':
    build()
