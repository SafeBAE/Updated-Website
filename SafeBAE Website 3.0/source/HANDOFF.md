# HANDOFF: SafeBAE site rebuild v3.0 (2026-10-09)

## 1 GOAL
- User: Drew Davis, Dir. Strategic Initiatives, SafeBAE.
- v1 (FROZEN): 44pp. Artifact "SafeBAE Site Rebuild". Desktop `~/Desktop/Updated Website/{README.md,site/,source/}`.
- v2 (FROZEN): 47pp. Artifact "SafeBAE Site 2.0" claude.ai/artifact/VMmcNZMZr5WxZwKmuAwT4G. Desktop `~/Desktop/Updated Website/SafeBAE Website 2.0/`.
- v3 ask (Drew, 2026-10-09): copy v2 → publish as v3 with (1) layout + visual optimisation everywhere ("odd empty spaces, weird formatting in rows with multiple columns, nonsymmetrical stuff… consistent and masterfully designed"), (2) nav: Request a Program replaces 360° Schools as a tab, 360 = "guiding philosophy" and one page under it, new Assemblies page, Library + Peer Educator under Resources, #ForDaisy stays a tab, (3) better footer (keep big SAFE BEFORE ANYONE ELSE, SAFE in neon), nicer daisy that doesn't move (he supplied a line drawing), (4) KnowB4UNude redesigned around its emoji aesthetic, (5) Skills Lab landing page, (6) polished, fun, consistent, with individual takes for campaigns.
- STATUS: v3 built (49pp), checked, published as artifact "SafeBAE Site 3.0" claude.ai/artifact/TYPY7yR4NnffBvCuTCeWmu (private, 510 files), delivered to `~/Desktop/Updated Website/SafeBAE Website 3.0/` {README.md, site/, source/}. Not click-tested inside the artifact frame (same soft-navigation code as v1/v2).

## 2 RULES (v1/v2 rules still hold; see BRIEF.md, BRIEF2.md, BRIEF3.md)
**Stack:** Python static generator → plain HTML. `lib.py`: page() phero() header() footer() btn() img() esc() NAV NAV_ALIAS RIBBON FOOT_COLS SOCIAL hz_label(). `site/assets/css/site.css` + `site/assets/js/site.js` are HAND-EDITED. `build.py` runs ORDER, then `pages_about.credits()`, `search_index.build()`.

**Module → pages (v3):**
- pages_home: index (exports FILMS, FILM_STRIP_CSS, film_font_link, film_strip, cpet_player, ring_svg, COMP_TEXT)
- pages_library: library (+assets/js/library.js) · films_common (+film_crumbs) · films_red/bae/know/dating/oh/rc/men/rrcr: 8 film-*.html
- pages_resources: resources · pages_vibe: vibe-check · pages_skills: skills-lab (NEW)
- pages_support: survivor-support, title-ix · pages_support2: myths-facts, faq, posters, blog
- pages_students: students, peer-educator · pages_students2: clubs, reform-policy, summer-institute, espanol
- pages_adults: adults, parents · pages_adults2: educators, college, donate, chip-in, fundraise
- pages_programs: request-a-program (hub), assemblies (NEW)
- pages_schools: 360-schools · pages_schools2: consent-curriculum, professional-development, policy-reform-guide, accountability-training
- pages_about: about, team, impact, credits · pages_about2: partners-press, contact · pages_daisy: fordaisy, fordaisy-tattoos
- pages_ai: ai-literacy (exports brush) · pages_choking: choking-hazard

**NAV (6 tabs, lib.NAV dicts with groups):** About · Students · Adults · Request a Program (key `programs`; old `schools` aliases to it) · Resources (old `library` aliases to it; 4 groups ×5, wide menu) · #ForDaisy. Active key + breadcrumb table is in BRIEF3.md.

**3.0 system (end of site.css):** full-width mega sheets (`.mega`, `.mega__intro/__cols/__col/__h/__feature/__foot`); `--daisy-line` line-art daisy on `.phero__wm`/`.wm-daisy` (strength `--wm-o`, default .2; no rotation; `sb-bloom` entrance) and `.daisy-art` utility; `daisy-line-bold.svg`/`daisy-line-mark.svg` for small marks; footer (`.footer-mark` two lines sized in cqi: line 1 10.86cqi/stretch 125, line 2 stretch 116; `.footer-lead`, `.footer-cols` 6 cols, `.socials`); tokens `--gap --head-gap --pad-card`; utilities `.level .fill-img .section-head--center .section-head__act`; `.vid img` opacity 1; `.player` true 16:9 + stops after one pass; `.give` buttons on one row.

**Layout standard (BRIEF3):** 12-col grid; feature rows 7/5, 5/7, 8/4 ending level; one card anatomy and ≤2 surfaces per group; no orphans; no hollow boxes; no dead zones; head full width over content; ledes full width; body text ≥15px in cards, nothing readable <14px; nothing loops forever; SafeBAE video stills never tinted; coral never darkened; one signature moment per page.

**Campaign colours stay home:** safety yellow only on Choking Hazard label/stickers/tape; lavender (#d592f8) only on film-knowb4unude.

**Drew feedback this round:** liked the big footer wordmark; wanted SAFE neon; disliked rotating basic daisy; wants Vibe Check spotlighted; #ForDaisy tab matters to stakeholders.

## 3 TOOLS (source/tools, run from v3 root)
- `python3 tools/audit.py page.html [1440]` → layout findings (GAP DEAD HOLLOW UNLEVEL LOPSIDED ASYM MISALIGN MIXED ORPHAN NARROW TINY SAMEBG) + `shots/<page>_<w>_audit.jpg`. Leads, not verdicts.
- `tools/snap.py page.html 1440 full` · `tools/slice.py shots/p_1440.png 1500 0.6` · `tools/el.py page.html "<sel>" 1440 out.png "<click>||<click>"` · `tools/mobile_sheet.py shots/p_400.png 2800 0.5 4` · `tools/check.py all [pages]` (links + overflow 360/400/1440 + console).
- `_sem.py` caps concurrent browsers (SB_BROWSER_SLOTS, default 3).

## 4 REBUILD
```bash
mkdir -p /home/claude/v3/build /home/claude/crawl
cp source/*.py source/credits.jsonl /home/claude/v3/build/
cp source/img_manifest.json source/*.md /home/claude/v3/
cp -r site /home/claude/v3/site; cp -r source/tools /home/claude/v3/tools
cp -r source/crawl/* /home/claude/crawl/
cd /home/claude/v3/build && python3 build.py        # or: python3 -c "import pages_x; pages_x.build()"
cd /home/claude/v3 && python3 tools/check.py all
```
Hard-coded `/home/claude/v3` paths: lib.py L2-3, build.py + search_index.py sys.path, pages_about.py credits.jsonl, pages_daisy.py tributes.json (`/home/claude/crawl/`), tools.

**Artifact page from site/index.html:** strip doctype/html/head wrappers and charset/viewport metas, set `<title>SafeBAE Site 3.0</title>`, replace `<body class="home">` with `<script>document.body.className='home';</script>`, drop `</body></html>`. Publish with root=site, all site files except index.html and unused images, ≤254 files per call (omitted files are kept on later publishes). site.js soft-navigation swaps pages inside the artifact frame.

## 5 OPEN
- Drew to review v3; items for him are in README.md ("Please check these before launch").
- Assemblies page has no topics/length/grades/prices (SafeBAE hasn't published them).
- Forms are front-end only (tribute wall first).
- Zeffy iframe heights need one look on a live host.
- Skills Lab: "Take a Hint" and "Who's Right?" not listed (not in the repo snapshot in the Assets folder).
