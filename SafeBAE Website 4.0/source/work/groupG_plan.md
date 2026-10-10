# Group G — about: plan (v4)

Measured before (1440, full page incl. header + footer): about 9,348 · team 5,905 · impact 7,530 · credits 2,764 · partners-press 7,152 · contact 3,508.
Incoming anchors from other pages: none except our own (about → impact#climate/#training/#reports, team → partners-press#torrey, partners-press → team#board). All kept.

## about.html — job: who SafeBAE is and how it began
9 sections / 9,348px → 7 sections / target ~6,500–7,000px.
1. Hero — keep (mission, collage).
2. BAE strip — keep.
3. Our story — keep head, lede, 7/5 text + photo. **Cut the pull quote**: it repeats paragraph two word for word.
4. How we began + The co-founders — **merge** into one deep section: video (7) beside the lede and the founders' account (5), then the four co-founder cards. The name chips go (the cards carry the names). Ids `how-we-began` (section) and `co-founders` (card row) both stay.
5. Shael Norris — keep.
6. Milestones (signature) — keep; tighten into a zigzag timeline (year above each card, the two sides interleave) so it runs about 400px shorter. Fill-on-scroll stays.
7. "Prevention led by young people, in their own schools" — **reduce** the 7-card bento to one 7/5 row: Vibe Check as the teal feature panel (Drew's flagship, not a small card) beside four compact program links (Peer Educator Training, Clubs, 360° Schools, the Library). AI Literacy and Choking Hazard cards go (home page, utility bar and nav feature them).
- **Cut** "Meet the people and the work" (nav, footer and links already on the page cover Team, Impact, #ForDaisy; Partners & Press and Contact are in the nav/footer).
- Backgrounds: slate / mint / paper / deep / paper / slate / paper → footer.

## team.html — job: who runs SafeBAE (staff, youth media team, board)
5 sections, light pass.
- Hero mosaic, leadership rows, board — keep; check rows level.
- Youth media team: switch the round portraits to the board's square card anatomy (photo, name, role) on one row of seven, so every people card on the page reads as one family.
- "Ways to join this work" — keep (one short row of three; the page's one ending).

## impact.html — job: SafeBAE's evidence (published research, climate survey, training efficacy, reports)
7 sections / 7,530px → 5 sections / ~6,300px.
- Hero, research, climate — keep.
- **Merge** the aqua "What we measure, and what we found" band and the "Does prevention work?" video band into the training section: first row = eyebrow "2023 program efficacy data", h2, the efficacy paragraph as lede (5) beside the video with its caption (7); second row = the training text (5) beside the chart (7); then the two student quotes. Id `efficacy` and `video` move onto the rows that now hold them; `training` stays on the section.
- Reports — keep (one ending); background becomes aqua so it doesn't sit paper-on-paper after training.

## partners-press.html — job: who SafeBAE works with and how media has covered it
6 sections, light pass.
- Hero: second button "Read our blog" → "Press contacts" (contact.html#press); the blog card at the end of the page already carries the blog.
- Press, podcasts (signature deck), Torrey, films, professionals + collaborator wall + news card (the one ending) — keep; check level rows and 400px.

## contact.html — job: get each person to the right channel
4 sections, light pass. Help card, route picker (signature), program request form, address/social/newsletter row (the ending, light so it doesn't sit dark-on-dark against the footer). Check level and 400px.

## credits.html — job: credit stock photography
3 sections, light pass. Drop the redundant "Unsplash photography" eyebrow; only list photos still used on the site (so the count stays true after other builders' cuts). `credits()` keeps its name and is still called by build.py.
