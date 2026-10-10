# SafeBAE site 3.0 — brief for page builders

You are one of several builders working in parallel on version 3 of the rebuilt safebae.org (SafeBAE: the survivor-founded, youth-led nonprofit working to end sexual violence among middle and high school students). The client is Drew Davis, SafeBAE's Director of Strategic Initiatives. Version 2 is finished and frozen; v3 is a copy of it that needs a layout and visual-design pass.

## What Drew asked for (his words)
> "Optimizing layout and visual design. Right now, some of the things have odd empty spaces, weird formatting in rows with multiple columns, nonsymetrical stuff where symetrical would be better, poor design elements sometimes, etc... Refine it. Make sure that the layout is visually pleasing across the board. Don't leave weird empty spaces or huge gaps. Prioritize making it consistent and masterfully designed so that every element is specifically and strategically placed perfectly."
>
> "I just need a visual, profesionalization and like fun creative visual update. I want this site to feel so fucking polished and perfect that it blows everyone's minds. The visuals need to be thoughtfully designed and carefully crafted. And it should be consistent, while still allowing for exciting individual creative takes for some of the different campaigns (like KnowB4Unude should have its own unique design that leverages its own aesthetic, compared to another teaching guide/video page)."

So the job on every page is: **find every place the layout is off and fix it, then raise the craft.** Keep each page's sections and content. This is a design pass, not a rewrite.

## Where to work
- v3 lives in `/home/claude/v3/`: generator `build/`, output `site/`, tools `tools/`, screenshots `shots/`.
- Build only your own module(s): `cd /home/claude/v3/build && python3 -c "import <module>; <module>.build()"`. Never run `build.py` (other builders are mid-edit).
- **Do not edit** `lib.py`, `site/assets/css/site.css`, `site/assets/js/site.js`, `data.py`, `build.py`, `search_index.py`, anything in `tools/`, or a module you were not assigned. If you need a shared change, describe it in your final report. Page CSS goes in your module's CSS strings (class names keep your page prefix); page JS in `scripts=`.
- Some modules were split from a larger v2 file by copying it, so your module may still contain functions and CSS for pages it no longer builds. Look at `build()` at the bottom to see which pages are yours. Delete the dead page functions, data and CSS that only other pages used (rebuild to prove nothing broke).
- Helpers that other modules import (for example `pages_home.cpet_player`, `film_strip`, `ring_svg`, `FILM_STRIP_CSS`, `COMP_TEXT`, `pages_ai.brush`, everything in `films_common`) must keep their names, signatures and class names.
- New images: put a `.webp` in `site/assets/img/<slug>.webp` (PIL, max 1800px wide, quality ~80) and use `img('<slug>', alt)`. Real SafeBAE photos first; the full set is `ls site/assets/img`. Contact sheet: `python3 tools/sheet.py shots/<name>.jpg 6 site/assets/img/a.webp …`. Unsplash only if a page truly lacks a photo (`python3 tools/unsplash.py …`, see BRIEF.md).
- Read first: `build/lib.py` (all of it), `site/assets/css/site.css` (all of it, especially the "SafeBAE 3.0 system layer" at the end), your module, and BRIEF.md + BRIEF2.md (the v1/v2 rules still hold unless this brief changes them).

## What is already new in the shared system (done; look at any built page)
- **Navigation, six tabs:** About · Students · Adults · Request a Program · Resources · #ForDaisy. Full-width mega sheets. "360° Schools" is no longer a tab: it is the approach behind the programs and one page under Request a Program. The Library, Peer Educator Training, AI Literacy Training and the campaigns sit under Resources.
- **Footer:** two-line neon wordmark, lead row, six link columns.
- **The daisy:** the old turning daisy silhouette in heroes is gone. `.phero__wm` / `.wm-daisy` now draw a hand-drawn line daisy (`assets/img/daisy-line.svg`) that sits still. Its strength is `--wm-o` (default .2): set `--wm-o` on your hero if you need it lighter or stronger; `color` sets the line colour (mint on dark, `var(--logo-teal)` on light). Page rules that set `opacity` on `.wm-daisy` no longer do anything: delete them and use `--wm-o`. Position overrides (`right/left/bottom/width`) still work; the art is now 1100:852, so re-check any hero where you position it, and make sure it never sits behind body text in a way that hurts reading. There is also `<span class="daisy-art" aria-hidden="true"></span>` for a drawn daisy as a section accent (size, position and colour it locally; at most one per page outside hero and footer). No element on the site spins continuously any more: remove any `sb-spin` use you find in your pages.
- **Tokens:** `--gap` (grid gap), `--head-gap` (space under a section head), `--pad-card` (card padding). Utilities: `.level` (row of boxes that end level, last child pinned to the floor), `.fill-img` (photo that fills its row partner's height), `.section-head--center`.

## Site map changes you must reflect in your pages
New pages: `assemblies.html` (Assemblies, under Request a Program) and `skills-lab.html` (BAE Skills Lab landing page). Other builders are writing them now; link to them even though `tools/check.py` will call them broken until they exist.

| Page | `active=` | Breadcrumb |
|---|---|---|
| about, team, impact, partners-press, contact, credits | `about` | Home / About / … |
| donate, chip-in, fundraise | `about` | Home / Donate (/ …) |
| students, clubs, reform-policy, summer-institute, espanol | `students` | Home / Students / … |
| adults, parents, educators, college | `adults` | Home / Adults / … |
| request-a-program | `programs` | Home / Request a Program |
| assemblies, 360-schools, consent-curriculum, professional-development, policy-reform-guide, accountability-training | `programs` | Home / Request a Program / … |
| resources | `resources` | Home / Resources |
| library, posters, vibe-check, skills-lab, peer-educator, ai-literacy, choking-hazard, survivor-support, title-ix, myths-facts, faq, blog | `resources` | Home / Resources / … |
| film-*.html | `resources` | Home / Resources / Library / … |
| fordaisy, fordaisy-tattoos | `fordaisy` | Home / #ForDaisy (/ Tattoos & Healing) |

- "Home" links to `index.html`; middle crumbs link to their page (Resources → `resources.html`, Library → `library.html`, Request a Program → `request-a-program.html`, etc.).
- Wherever a page **describes the Skills Lab** (a card, tile or row about it), the main link goes to `skills-lab.html`. A button that says "Open the Skills Lab" may still go straight to `https://skills-lab.safebae.org/`.
- Wherever a page mentions **assemblies** as something a school can book, link the word or the card to `assemblies.html`.
- **360° framing:** describe SafeBAE 360° Schools as SafeBAE's whole-school approach (the model that ties the programs together), reached through Request a Program. Don't call it a tab or present it as a separate product line next to "Request a Program". Buttons that said "Explore 360° Schools" are fine as "How 360° Schools works" or similar. Don't rewrite the 360 content itself.
- Don't invent facts for any of this. Allowed facts for AI Literacy, Choking Hazard and Tattoos & Healing are in BRIEF2.md.

## The layout standard (what "fixed" means)
Work at 1440px first, then 1024px, then 400px.

1. **One grid.** Think in 12 columns inside the 1240px wrap. A row of boxes is either equal columns (2, 3, 4) or a clear feature split (for example 7/5 or 8/4). When rows stack in the same section, their column lines line up, or the rows mirror each other on purpose (7/5 over 5/7). No 58/42 over 49/51.
2. **Symmetry by default.** If items are peers, they get equal width, equal height, the same anatomy (media, label, title, text, action in the same order and position) and the same surface. A group uses at most two surface treatments, and a different surface must mean something (the featured one).
3. **No orphans.** Pick column counts the items fill: 4 items → 4 or 2×2, 5 → 3+2 centred or a 2/3 feature split, 6 → 3×2, 7 → 4+3 or a feature + 6. Never one lonely card on a last row.
4. **Fill what you frame.** No box with content floating in a pool of blank space; no card whose text ends halfway down while its neighbour runs long. Fix by resizing the box to its content, giving short items a shared richer anatomy, switching the photo to `object-fit:cover` so it takes the height of the text beside it, or changing the composition. Don't fix it by padding the copy.
5. **No dead zones.** In a two-column section both columns end at about the same height. If one side is a short heading and the other a long list, restack (heading on top, full width), or put something real beside the heading (photo, stat, pull quote, action), or use a sticky side heading only when the long side is long enough to justify it.
6. **Rhythm.** Section padding is `var(--band)` (`.band--tight` for a short joining band). Space under a section head is `var(--head-gap)`. Grid gaps are `var(--gap)`. No blank vertical stretch over ~120px inside a section. Alternate light and dark sections; no two neighbours share a background unless they are deliberately one block.
7. **Section heads.** Title left, lede under it at the full width of the content column, optional action on the right (`.section-head`). A centred head only over a centred composition. Never a narrow `max-width` cap on a lede or subtitle (Drew has rejected this twice: "crammed into just staying in the left side column").
8. **Type you can read.** Running text in cards is at least .95rem (15px); nothing meant to be read is under 14px; mono labels at least .7rem. Card titles 1.2–1.5rem. Line length 45–85 characters for paragraphs. If a card only works with tiny type, it has too much in it or too little width: change the layout.
9. **Surfaces.** Large cards `border-radius: var(--r-xl)` (22px), small tiles and chips 12–14px, buttons 10px. On light backgrounds 1px `var(--line)` borders; raised elements `var(--shadow-soft)`. Photos 22px radius. Inside padding `var(--pad-card)`.
10. **Small screens.** At 400px: no horizontal scroll, grids stack in a sensible order (heading, then media, then text, then actions), tap targets at least 44px, no text under 14px.

## The craft standard (what "blow minds" means here)
- Every page keeps (or gains) **one signature moment**: an interactive, a data visual, an image composition or a type treatment that a visitor will remember and that helps them understand the content. Check that the existing one still works and looks finished; improve it if it is weak. One per page, not five.
- **Consistent, then individual.** The shared system (header, footer, heroes, section heads, buttons, cards, type) is the same everywhere. Campaign and tool pages (KnowB4UNude, It's Giving Red Flags, BAEcode: Game On, Choking Hazard, AI Literacy, Vibe Check, Skills Lab, #ForDaisy) each get their own visual identity built from their real campaign materials, inside the shared header and footer.
- **Details that read as care:** aligned baselines across a row, consistent icon sizes, hover and focus states on everything clickable, numbers set in the display face, captions on photos that need them, images cropped on the subject (set `object-position`), no stretched or pixelated images, no letterboxed thumbnails.
- **Motion with a purpose:** entrances (`.rise`, `.reveal`), hover lifts, count-ups, draw-ins. Nothing loops forever. Respect `prefers-reduced-motion`.
- **Not clutter.** Drew has called dense builds that stack pickers, carousels, stat rows, checklists and jump-link rows "too messy and overwhelming and weird", and stripped pages "a little bit too bare". Aim between: calm structure, a few substantial elements.
- Design choices Drew has rejected before, do not reintroduce: decorative 01/02/03 section numbers; big empty gaps; subtitles set narrow or flush-left under a big heading; a page describing its own structure; darkening the brand coral (#fe7171 stays exactly that); a filter or tint over stills from SafeBAE's own videos (they stay in original colour); two side-by-side boxes that end at different heights.

## Colour and copy (unchanged from v2, restated)
- Brand colours only: Logo Teal #1d5a66 (headings on light), SafeBAE Teal #13848f, Deep Slate #1d414e, Electric Mint #15ffc8, Pale Aqua #d1feff, Soft Gray #e1e1e1, Coral #fe7171 (urgency and support only, at most one coral button per page, never darkened), Midnight Indigo never. White and tints of these are fine. Small text on SafeBAE Teal is white. No SafeBAE Teal text on Deep Slate. Accents should be clearly felt, not hairline.
- Campaign colours stay inside their campaign: safety yellow #FFD600 + ink only on the Choking Hazard label, stickers and tape; KnowB4UNude's own colours only on the KnowB4UNude page.
- Vibe Check, where it appears, is a full teal band, not a small link.
- Copy: plain, declarative, specific. No meta copy ("This page…", "Below you'll find…"), no triads, no "not X but Y", no "Whether you're…", no hype words, no exclamation marks, no emoji (except where a campaign's own identity uses them and your task says so). US spelling. Keep SafeBAE's own wording; change copy only where a layout fix needs a shorter or clearer line, and never change a fact, number, name, quote or link. No invented facts.

## How to work (required)
1. Build your pages. For each page run the audit and look at the overview it writes:
   `cd /home/claude/v3 && python3 tools/audit.py <page>.html 1440` → prints findings (GAP, DEAD zone, HOLLOW box, UNLEVEL, LOPSIDED, ASYM, MISALIGN, MIXED, ORPHAN, NARROW, TINY) and writes `shots/<page>_1440_audit.jpg` with the flagged zones boxed and numbered. Findings are leads, not verdicts, and the audit misses most taste problems.
2. Then **look at every section yourself** at reading size: `python3 tools/snap.py <page>.html 1440 full` then `python3 tools/slice.py shots/<page>_1440.png 1500 0.6` and Read every slice. For a single block: `python3 tools/el.py <page>.html "<css selector>" 1440 shots/<name>.png` (optional 5th arg: selector(s) to click first, `||`-separated).
3. Write down, per section, what is wrong against the layout standard. Fix it in the module. Rebuild. Re-shoot. Repeat until you would sign the page.
4. Repeat the look at 1024 (`snap.py <page>.html 1024 full`) and at 400 (`snap.py <page>.html 400 full`, then `python3 tools/mobile_sheet.py shots/<page>_400.png 2800 0.5 4`).
5. Open every tab, accordion, filter and toggle state at least once (`el.py` with a click selector) and check those layouts too.
6. Finish with `python3 tools/check.py all <your pages>` (no overflow at 360/400/1440, no console errors, no broken links other than `assemblies.html` / `skills-lab.html` if they are not built yet) and a last `audit.py` run on each page.
The screenshot tools share a small machine: at most a few browsers run at once, so a command may wait its turn. Don't shoot more than you will look at.

## Final report (your last message, short)
Per page: the layout problems you found and what you changed (one line each), the signature moment, anything you could not fix, any shared-file change you need, new image slugs. No code.

---
## Addendum for the second group of builders (read this too)
The first group has finished: `index`, `resources`, `vibe-check`, `library`, `film-its-giving-red-flags`, `film-baecode-game-on`, `film-knowb4unude`, `request-a-program`, `assemblies` (new), `skills-lab` (new), `360-schools`, `students`, `peer-educator`, `adults`, `parents`, `fordaisy`, `fordaisy-tattoos`. **Those pages are the quality bar and the pattern source.** Before you start, shoot and look at the two finished pages closest to yours (for example `python3 tools/snap.py parents.html 1440 full` then slice) and read the CSS in their modules for the patterns they use, so sibling pages feel like one family:
- Feature rows are 7/5, 5/7 or 8/4 on a 12-column grid, with both sides ending level; photos fill the height of the text beside them (`object-fit:cover` + a set `object-position`).
- Card groups share one anatomy and at most two surfaces; rows of cards use CSS subgrid (or equal fixed rows) so labels, titles, text and actions line up across the row.
- A short heading never sits alone beside a tall list: the head goes full width on top, the content below.
- Body text in cards is 15px or more; nothing readable under 14px.
- Nothing loops forever: marquees and rotating text play once and rest. The shared slide player now stops after one pass.

Shared changes since the brief was written (already in `site.css` / `site.js` / `lib.py`; don't re-implement them):
- `.vid img` is now full opacity (stills from SafeBAE's own videos stay in original colour; never put a filter, tint, duotone or dim layer over them).
- `.player` now reserves its control bar under a true 16:9 (or 3:4 `.player--portrait`) slide area, and stops after one pass or on a manual click.
- `give_band()` keeps its two buttons on one row down to 861px.
- `.section-head__act`: put this class on an action element in a `.section-head` so it keeps its natural width.
- `.btn--sm` grows to 44px on touch screens; focus rings on aqua/coral heroes are teal; `.form__note` is 14.4px.
- Film pages: `films_common.film_page()` now sets `active='resources'` and there is `film_crumbs(title)` → "Home / Resources / Library / <title>". In a film module, replace the hand-written `<nav class="crumbs">…</nav>` line with `{film_crumbs('<title>')}`. The shared guide panel (`.gpanel`, text column `.gpanel__txt`) and "Teach these next" (`.frel__grid--n<count>`) were rebuilt; `.fhero--light .wm-daisy` no longer sets opacity (use `--wm-o`). `films_common.py` is finished: do not edit it.
- The drawn daisy's thin line disappears below about 150px wide. For small daisy marks use `assets/img/daisy-line-bold.svg` (heavier line) as a mask, or the existing `.daisy` icon.
- `assemblies.html` and `skills-lab.html` now exist; `check.py` should report no broken links at all.
- Page titles use the pattern `Name · SafeBAE`.

Working notes from the first group:
- `shots/` and `work/` are shared by every builder. Prefix your own files (`shots/<yourpage>-…`, `work/<prefix>_…`) so nobody overwrites anyone.
- `snap.py` freezes CSS animations when it shoots. An entrance animation that starts from `opacity:0` can be caught invisible in a full-page shot; if a block looks missing, check it with `el.py` before "fixing" it, and prefer transform-only entrances (`.reveal`, `.rise`).
- Don't trust `audit.py` at 1024 for layouts that restack; look.
