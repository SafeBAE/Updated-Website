# HANDOFF: SafeBAE site rebuild v4.0 (2026-10-09)

## 1 GOAL
- User: Drew Davis, Dir. Strategic Initiatives, SafeBAE.
- v1 (FROZEN): 44pp. Desktop `~/Desktop/Updated Website/{README.md,site/,source/}`.
- v2 (FROZEN): 47pp. Artifact "SafeBAE Site 2.0" claude.ai/artifact/VMmcNZMZr5WxZwKmuAwT4G. Desktop `SafeBAE Website 2.0/`.
- v3 (FROZEN): 49pp. Artifact "SafeBAE Site 3.0" claude.ai/artifact/TYPY7yR4NnffBvCuTCeWmu. Desktop `SafeBAE Website 3.0/`.
- v4 ask (Drew, 2026-10-09): copy v3 → publish as v4 with (1) footer "insane… way too much… completely unwieldy" → cohesive and simple, (2) visual refinement + more strategic planning of layout and content on each page + the overall navigation experience, (3) pages that feel overwhelming, e.g. Choking Hazard: "doesn't need to replicate everything from chokinghazard.org… just launch people there and provide some context", (4) better overall.
- STATUS: v4 built (49pp), checked (check.py all clean), published as artifact "SafeBAE Site 4.0", delivered to `~/Desktop/Updated Website/SafeBAE Website 4.0/` {README.md, site/, source/}.

## 2 RULES (v1–v3 rules still hold: BRIEF.md, BRIEF2.md, BRIEF3.md; this round: BRIEF4.md)
**Stack:** unchanged. Python static generator → plain HTML. `lib.py` page() phero() header() footer() btn() img() esc() NAV NAV_ALIAS RIBBON FOOT_COLS SOCIAL. `site.css` + `site.js` hand-edited. `build.py` runs ORDER, then `pages_about.credits()`, `search_index.build()`.

**4.0 system (end of site.css, "4.0 system layer"):**
- Header: two bars. RIBBON entries render in the utility bar (`.utility__new`, hidden < 1040px) and in the phone drawer (`.drawer__new`). The ribbon bar and its rotation are gone.
- Footer (`lib.footer`): `.ft` grid (brand span 4 / `.ft__links` 4 cols span 8), `.ft__help` line (coral accent), `.footer-mark` two lines at every width (`.fm1` 10.86cqi stretch 125, `.fm2` stretch 116; neon `b` with glow, solid aqua `i`), `.ft__legal`. FOOT_COLS = 4 columns (Resources has 6 incl. Resources Hub). Old support strip, v1/v2/v3 footer CSS and footer daisy removed.
- Nav tabs are `<a class="nav__top" href=landing>`: hover/focus opens the mega sheet, click opens the page; touch screens: first tap opens the sheet. ArrowDown/Space opens and focuses the sheet. Drawer adds `.drawer__land` (Resources Hub) where a tab's landing page isn't in its groups.
- `give_band()` returns '' (retired). Donate/Chip In/Fundraise keep their own giving sections.
- Mega: Resources feature card is `.mega__feature--vc` (teal + phone screen), via NAV `feature_cls`.
- `.site-footer` has a 1px inset hairline so dark closing sections separate from it.

**Page strategy (BRIEF4):** one job per page; launch pages give context and send people to the tool's own site (pattern: choking-hazard.html); hubs route; content pages keep substance and drop cross-promos; at most one cross-promo besides the page's subject; Vibe Check as a full teal band where relevant; one closing section per page.

**Shared helpers added this round:** `pages_schools2.closing()` + `CLOSE_CSS` (one ending for 360 and the four program pages); `films_common.teach()`, `teach_tail()`, `TEACH_CSS`, `BEGIN_LEDE` ("Teach it" section on film pages).

**Choking Hazard page ids:** #how-common (facts), #campaign (doors), #er, #schools.

## 3 TOOLS (source/tools, run from v4 root)
v3 tools plus: `tools/ov.py shot.png out.jpg cols 0 scale` (whole page as columns), `tools/ov2.py out.jpg cols scale page…` (several pages side by side, reads shots/r/), `tools/vp.py page.html w h out "click||hover:sel" [scrollY]` (viewport shot after clicks/hovers; mega menus need `hover:`).

## 4 REBUILD
Same as v3 with v4 paths: copy source/*.py + credits.jsonl to /home/claude/v4/build, img_manifest.json + *.md to /home/claude/v4, site → /home/claude/v4/site, tools → /home/claude/v4/tools, crawl/* → /home/claude/crawl, then `cd /home/claude/v4/build && python3 build.py`.

**Artifact page from site/index.html:** strip doctype/html/head wrappers and charset/viewport metas, set `<title>SafeBAE Site 4.0</title>`, replace `<body class="home">` with `<script>document.body.className='home';</script>`, drop `</body></html>`. Publish with root=site, all site files except index.html and unused images (images not named in any html/css/js), ≤250 files per call.

## 4b ROUND 2 (2026-10-10, Drew's fixes)
- Footer sign-off "still off" → two-line full-width, solid aqua letters (options sheet `footer-signoff-options.png` in the Desktop folder: before / one line solid / two lines solid (applied) / neon sign).
- Parents: restorative justice diagram (`untitled-design`, credit iirp.edu) restored in an alternative-justice row; v3 CheckYourVibe.org band + full "Sharing Vibe Check with your child" (tabs, 5 steps, say/avoid, starters) restored, linking to vibe-check.html#adults.
- Vibe Check: Dominick Shattuck full note + Substack rows restored (`#shattuck`); short quote removed from #why.
- Resources Hub: v3 `pages_resources.py` restored (Group A's trimmed version kept at work/pages_resources_v4groupA.py); Vibe Check questions play once; Choking Hazard shelf text updated.
- Each tab links to its landing page (see 2).

## 5 OPEN
- Drew to review v4; items in README.md ("Please check these before launch").
- Carried: Assemblies facts unpublished; forms front-end only; Zeffy heights on a live host; Take a Hint / Who's Right? not in Skills Lab snapshot.
