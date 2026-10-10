# SafeBAE site rebuild — brief for page builders

You are building part of a from-scratch redesign of safebae.org (SafeBAE: the survivor-founded, youth-led nonprofit working to end sexual violence among middle and high school students). The client is Drew, SafeBAE's Director of Strategic Initiatives. He asked for "an entirely new, comprehensive build out… almost all of what currently exists, laid out in a new, better and more user friendly but also visually interesting way… Go as hard as possible… Make it visually beautiful, stay in our brand colors. Do an amazing job."

The home page, the unified Library and eight film landing pages are DONE. Your job is a group of the remaining content pages (listed in your task). Match the quality bar of the finished pages: open `site/index.html`, `site/library.html`, and a film page in the screenshot tool (below) before you start, and read `build/pages_home.py` + one `build/films_*.py` to see the house style in code.

## How the build works
- Static site generator in Python. `build/lib.py` gives you `page()`, `phero()`, `btn()`, `a()`, `img()`, `yt()`, `spotify()`, `embed()`, `chips()`, `eyebrow()`, `row()`, `give_band()`, `esc()`, `HOTLINES`, `daisy()`. READ lib.py fully first.
- `lib.page(slug, title, desc, body, active=<nav key>, body_class, fonts, head_extra, scripts)` writes `site/<slug>` with the shared header/mega-nav, footer, help drawer, search palette, lightbox. Nav keys: `about`, `students`, `adults`, `schools`, `library`, `resources`.
- Shared CSS: `site/assets/css/site.css` (read it fully: tokens, `.band--*` colour bands, `.wrap`, `.section-head`, `.lede`/`.lede--full`, grids `.g2/.g3/.g4/.split`, `.card`, `.rows/.row`, `.panel`, `.steps`, `.modules`, `.quote`, `.stats`, `.vid`, `.audio`, `.player`, `.acc`, `.tabs`, `.flip`, `.marquee`, `.logo-strip`, `.gallery`, `.people/.person`, `.tl` timeline, `.form/.field`, `.copy`, `.note`, `.chips`, `.sticker`). Shared JS: `site/assets/js/site.js` (read it: `data-tabs`, `data-flip`, `data-player`, `data-gallery`, `data-copy`, `form[data-static]`, `data-yt`, `data-spotify`, `data-embed`, `.reveal`, `data-open-help`, `data-quick-exit`). Grep the finished modules for real markup examples, e.g. `grep -n "data-tabs\|class=\"acc\|data-player\|class=\"people" build/*.py`.
- Reusable helpers you may import: `from data import LIB, PODCASTS, TOPICS, FAQ, library_items`; `from films_common import related, help_inline, HELPLINE_CSS, prompts`; `from pages_home import ring_svg, COMP_TEXT, cpet_player` (check what CSS they need — some CSS lives in HOME_CSS / module CSS strings, copy what you need into your page CSS).
- **Do not edit** `lib.py`, `site.css`, `site.js`, `data.py`, `pages_*.py`/`films_*.py` you didn't create, or any other agent's module. Several builders work in parallel. Put page-specific CSS in a `<style>` string passed as `head_extra`, with class names prefixed for your page (e.g. `.ab-…` for about) so nothing collides. Put page JS in `scripts='<script>(function(){ … })();</script>'`. Wrap every localStorage/sessionStorage access in try/catch.
- If you find a real bug in a shared file, don't fix it — describe it in your final report.
- Your deliverable is ONE module `build/pages_<group>.py` exposing `build()` that writes all your pages. Run it with `cd /home/claude/build && python3 -c "import pages_<group>; pages_<group>.build()"`.

## Source content (what to carry over)
- Extracted text of every current page: `crawl/md/<key>.md` (key = URL path with `/` → `__`). Raw HTML: `crawl/pages/<key>.html`. Teaching-guide/PDF text: `crawl/pdf/`. Per-page image list: `python3 tools/page_images.py <key>`. Tributes for #ForDaisy: `crawl/tributes.json`. YouTube metadata: `crawl/yt.json`.
- Carry over **almost all** the substantive content of each page: every program, step, list item, stat, name, bio, quote, link, video, form and PDF. You can reorganise, tighten wording, merge duplicates, and split long pages into tabs/accordions — but facts stay exactly as the source states them.
- **Never invent** facts, statistics, quotes, names, dates, testimonials, prices, or outcomes. If you want a number, it must be in the source. Don't add years to things the source doesn't date.
- PDFs, Google Forms, Calendly, Zeffy, Jotform etc. stay as links to their existing URLs (wp-content/uploads PDFs link to `https://www.safebae.org/wp-content/uploads/...`). Use `lib.embed(src, link, label)` for an embeddable form (it renders a fallback button inside the preview sandbox and the real iframe on a live site).
- YouTube: `lib.yt(video_id, title, label=...)` needs a thumbnail image `yt-<id lowercased, non-alnum→->` in the manifest. If the thumbnail doesn't exist, download it: `curl -sSL https://i.ytimg.com/vi/<ID>/maxresdefault.jpg` (fallback hqdefault.jpg) into a scratch dir, then convert to `site/assets/img/yt-<slug>.webp` (PIL, max 1280w, quality 74). Spotify: `lib.spotify(episode_id, title, show)` needs `sp-<id lowercased>`; check `data.PODCASTS` first.

## Links
Internal links must point at pages in the new sitemap:
index.html · about.html · team.html · impact.html · partners-press.html · fordaisy.html · contact.html · credits.html · students.html · peer-educator.html (#register for the registration form) · clubs.html · reform-policy.html · summer-institute.html · espanol.html · adults.html · parents.html · educators.html · college.html · request-a-program.html · 360-schools.html · consent-curriculum.html · professional-development.html · policy-reform-guide.html · accountability-training.html · library.html (#films #podcasts #guides) · posters.html · resources.html · vibe-check.html · survivor-support.html (#hotlines) · title-ix.html · myths-facts.html · faq.html · blog.html · donate.html · chip-in.html · fundraise.html · film-its-giving-red-flags.html · film-baecode-game-on.html · film-knowb4unude.html · film-dating-after-sexual-assault.html · film-online-harassment-of-survivors.html · film-rape-culture.html · film-sexual-assault-of-men.html · film-race-rape-culture-resistance.html
Old-URL mapping: /about-us/→about · /about-us/our-team/→team · /about-us/data-reports/→impact · /get-involved/students/become-a-peer-educator/ and /resources/peer-educator-training/→peer-educator · …/studentregistration/→peer-educator.html#register · /get-involved/students/clubs/→clubs · /get-involved/students/reform_school_policy/→reform-policy · /get-involved/students/version-en-espanol/→espanol · /meet-the-fellows/→summer-institute · /get-involved/educators/→educators · /get-involved/college-students/→college · /360-schools/school-policy-reform-guide/→policy-reform-guide · /chipin/→chip-in · /justin/ /tuna/ /vanessa/→fundraise · /resources/videos|podcasts|teaching-guides/→library.html#films|#podcasts|#guides · /resources/videos/<film>/→the film page. Blog posts (safebae.org/<post>/ or /blog/…) stay as external links to safebae.org. External sites (skills-lab.safebae.org, clubs.safebae.org, checkyourvibe.org, safebae.podia.com, bookshop.org/shop/SafeBAE, substack) stay external.

## Design rules (Drew's standing preferences — follow strictly)
- Brand colours only (tokens in site.css): Logo Teal #1d5a66 (headings/anchors), SafeBAE Teal #13848f (primary), Deep Slate #1d414e (text, dark backgrounds), Electric Mint #15ffc8 (accent/CTAs/highlights), Pale Aqua #d1feff (light backgrounds/tints), Soft Gray #e1e1e1 (neutrals/dividers). Coral #fe7171 = urgency/emphasis, use SECOND MOST sparingly, never darken it. Midnight Indigo #210658 = use MOST sparingly (ideally not at all). White and tints of these are fine. No other hues, no off-brand gradients.
- Typography: Archivo (display, variable width — use `font-stretch` like the finished pages), Montserrat (body), IBM Plex Mono (labels). Already loaded by `page()`.
- Ledes/subtitles span the full content width — no narrow max-width caps on intro paragraphs (use `.lede--full` or override).
- No decorative "01 / 02 / 03" numbering. Numbers only for real sequences (steps of a process, lesson numbers).
- No big empty gaps; keep vertical rhythm tight. Side-by-side boxes must be equal height. Cards in a row share edges/baselines; pick column counts the items fill (no orphan card alone on a row).
- Informational pages are calm but not bare: use colour bands, photos, a pull quote, an interactive element (tabs, accordion, flip cards, slide player, checklist, timeline) where it genuinely helps navigate the content.
- Each page should feel designed for its subject, not a template fill. Vary hero treatments (`phero` kinds: image, split with media + sticker, teal, logo, aqua, coral) and section rhythms across your pages.
- Vibe Check (checkyourvibe.org) is a flagship tool: where it's relevant to the audience, give it a full teal band (`band band--teal`) rather than a small link.
- Support resources (hotlines) should be easy to reach from anything touching on harm: `help_inline()` or a button with `data-open-help`.
- Must work at 400px wide: no horizontal scroll, grids stack, `min-width:0` on text-bearing grid children.

## Copy rules (Drew is strict about this)
Plain, declarative, warm, specific. Write like SafeBAE's own staff, not like marketing AI.
- No meta/self-referential copy ("This page…", "Below you'll find…", "Explore our…", "Welcome to…").
- No rhetorical triads ("learn, grow, and lead"), no "not just X — it's Y" / "X isn't about A, it's about B" constructions, no "Whether you're A or B…", no "In today's world", no "empower/unlock/elevate/journey/dive in/game-changer", no exclamation-mark hype, no emoji.
- Headings say the thing ("Start a club at your school", "What happens after you register"), not slogans.
- Keep SafeBAE's own phrasing where it's good — it's their voice.

## Images
- Use real SafeBAE photos first (`tools/page_images.py <key>` shows what each original page used; full list = keys of `/home/claude/img_manifest.json` plus any `site/assets/img/*.webp`). Make a contact sheet to look at candidates: `python3 tools/sheet.py /home/claude/shots/<name>.jpg 6 site/assets/img/a.webp site/assets/img/b.webp …` then Read the jpg.
- Unsplash is allowed for pages that lack photos (load `mcp__Unsplash__search_photos` via ToolSearch). Pick natural, documentary-feeling photos of teens/young adults/educators/parents — no cheesy stock, nothing that depicts violence or distress. Download with `python3 tools/unsplash.py "<urls.raw>" <slug> "<user.name>" "<user.links.html>" "<links.html>"` → then `img('us-<slug>', alt)`. That records the credit automatically. Use a handful per group at most.
- Always write meaningful alt text for content images; decorative images get alt="".

## Checking your work (required)
- Screenshot: `cd /home/claude && python3 tools/snap.py <page>.html 1440 full` then `python3 tools/slice.py shots/<page>_1440.png 1800 0.5` and Read the slice jpgs. Repeat at 400 width (`snap.py <page>.html 400 full`, slice with `1800 0.6`). snap.py prints console errors and HORIZONTAL OVERFLOW warnings — fix all of them.
- Single element: `python3 tools/el.py <page>.html "<css selector>" 1280 shots/x.png "<optional selector to click first>"`.
- Look at every section in every page at both widths. Fix overlaps, clipped text, empty gaps, unequal side-by-side boxes, low contrast, orphan cards. Iterate until it looks finished.
- Check internal links: every `href` that isn't http/mailto/tel/# must be in the sitemap above.

## Final report (your last message)
Short: pages built; for each page any source content you deliberately left out and why; new images downloaded (slugs); any shared-file bugs noticed; anything you couldn't do. Don't paste code.
