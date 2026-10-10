# Group H plan — library & films (v4)

Measured at 1440 before any edit (scrollHeight, footer included).

## Shared change (films_common)
New `teach(fid, cls, ...)`: one "Teach it" section that replaces `begin()` + `guide_panel()`.
- id="guide" on the section (hero buttons link there); id="begin" kept on the facilitator-notes card inside it (Red Flags' run-of-show links there).
- Composition: guide cover (4 cols, takes the height of its partner) beside the guide text, download + posters buttons, survey line, then the "Before you begin" card (three notes as rows + the coral help strip). Optional campaign posters row (gallery) under it, for the pages whose tiny poster bands fold in.
- The section takes the page's own surfaces through the --f-* tokens (each film keeps its look to the end) instead of the Logo Teal band, so it can alternate with the page's bands (several pages put a teal Vibe Check band right before it).
- `teach_tail(...)` = teach + "Teach these next". Old helpers (`guide_panel`, `begin`, `begin_card`, `help_card`, `tail`, `frelated`, `vibe_band`, `help_inline`, CSS strings…) stay exported and unchanged.

## library.html — job: find any SafeBAE film, podcast or teaching guide and open it.
Before: 4 blocks (hero, filter bar, catalog, "More from SafeBAE") / 10,295px.
- Keep hero (search + three format doors), filter bar, catalog shelves (signature: live search + filters + drawer).
- Cut "More from SafeBAE" (AI Literacy + Choking Hazard cards, Consent Curriculum door): cross-promos the nav/utility bar/footer carry.
- Replace with one compact closing line inside the catalog's end: posters (posters.html) + suggest a topic (contact.html).
- Layout pass on shelves/cards.

## Film pages (each ≤ 9 sections; ending = "Teach it" + "Teach these next")
### film-its-giving-red-flags — job: show the film and give a teacher the full consent lesson around it.
Before 11 / 10,053. Keep hero, Before you press play (run of show), MOVERS (signature tabs), The submissions, grounding, Red to Green, Vibe Check band. Fold "Put it on the wall" (2 posters) into Teach it. Merge Before you begin + guide → Teach it. Then Teach these next. → 9.
### film-baecode-game-on — job: the bystander film and its mission-by-mission lesson.
Before 9 / 8,580. Keep hero (cabinet), Flip the Bro Code, missions (signature), Four D's, Why people don't step in, Made by students. Merge begin + guide → Teach it. → 8.
### film-knowb4unude — job: the PSA and a non-judgmental lesson on nudes, pressure and sextortion.
Before 12 blocks (11 sections + tag strip) / 9,647. Keep hero (phone), strip, PSA + quote, stats (Polaroids), Start the conversation, What would you do (signature tabs), Vibe Check band, sextortion + laws. Fold "Share the campaign" posters into Teach it; merge begin + guide. → 9 sections.
### film-dating-after-sexual-assault — job: the film and guidance for survivors and partners.
Before 9 / 7,587. Keep hero, Healing is not a straight line (breath orb — signature), guidance tabs, Reflect together, Show up for survivors. Fold "Posters for healing" into Teach it; merge begin + guide. → 7.
### film-online-harassment-of-survivors — job: the #QuitThisSh*t films and how peers step in.
Before 8 / 7,014. Keep hero, Rewrite the thread (signature), films tabs, Ways you can step in. Merge its own begin (group agreements) + "From the campaign" prints + guide → Teach it. → 6.
### film-rape-culture — job: Charlie's film and the lesson on recognizing and interrupting rape culture.
Before 11 / 9,152. Merge "What is rape culture?" definition into the six-elements section as its head (the definition leads into where it's learned). Keep myths, Interrupt it (signature wall), Discuss, one small action, Vibe Check band. Merge begin + guide → Teach it. → 9.
### film-sexual-assault-of-men — job: Theo's testimony and the lesson on male survivors.
Before 11 / 9,072. Merge the mint "1 in 6" band with "Not every man's experience is the same" (both are the numbers) into one stat section after the hero. Keep Discuss (+ poster), Myth or fact, The rules boys are taught (signature), Know the terms, Your role. Merge begin + guide → Teach it. → 9.
### film-race-rape-culture-resistance — job: introduce the four-lesson series and send people to start it.
Before 6 / 5,974. Light pass: no guide/begin pair here. Check the closing card ("Alongside the Certified Peer Educator Training" + help line) reads as the series' start, and that the two closing sections are level and alternate.

## Checks
- Inbound anchors from other pages: only library.html#films/#guides/#podcasts/#parenting (kept). Film pages: keep #guide, #begin, #film, #movers, #scenes, #ground, #red-to-green, #missions, #guidance, #thread, #films, #elements, #discuss, #rules, #lessons.
- No tint on stills from SafeBAE's own videos.

## Outcome (1440, footer included)
library 10,295 → 9,887 · red flags 11/10,053 → 9/9,637 · baecode 9/8,580 → 8/8,411 · knowb4unude 11/9,647 → 9/9,238 · dating 9/7,587 → 7/7,218 · online harassment 8/7,014 → 6/6,638 · rape culture 11/9,152 → 9/8,760 · men 11/9,072 → 9/8,934 · rrcr 6/5,974 → 6/5,958. check.py all: clean.
