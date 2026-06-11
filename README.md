# TOGAF® EA Practitioner — Mock Exam Studio

**🌐 Live demo: <https://csahli.github.io/TOGAF_EA_10_Prep/>**

A single-page web app for practising TOGAF Standard 10th Edition exam questions,
aligned to the published OGEA-101 / OGEA-102 / OGEA-103 exam structure.

## Features

- **Level 1 (Foundation)** — 128 single-best-answer recall questions, each
  with a best-effort citation back to the TOGAF Standard 10th Edition (C220)
  or the relevant TOGAF Series Guide. 128 unique stems across 25 topics.
- **Level 2 (Practitioner)** — 128 scenario questions scored on the same
  5/3/1/0 gradient the OGEA-102 exam uses (best = 5, second-best = 3,
  third-best = 1, distractor = 0). The gradings themselves are the author's
  interpretation, not an Open Group answer key. Built from 16 distinct
  scenario templates × company-name variants — within any single session,
  picks are deduplicated so the same scenario never repeats under a
  different company name.
- **Blended** — mixes both levels in one practice session.
- **Practice mode** — pick your own question count, shuffle and toggle instant
  feedback per question. When you answer a question the rationale and the
  C220 reference appear inline immediately.
- **Official exam simulation** — enforces the published Open Group conditions:
  - OGEA-101: 40 questions / 60 minutes / closed book / 24-40 pass
  - OGEA-102: 8 questions / 90 minutes / open book / 24-40 pass
  - OGEA-103 Combined: 48 questions / 150 minutes / each part 24-40 to pass
  - Visible countdown timer, auto-submit on timeout
  - The full set of questions is chosen up-front at the start of the
    simulation (no on-the-fly resampling) and Level 2 picks are guaranteed
    to come from distinct scenario templates.
- Score ring, per-question review with rationales **and source citations**
  on both the inline feedback and the final review screen
- Glossary of 30 core TOGAF concepts with links to the official TOGAF Standard,
  plus 10 inline reference diagrams (ADM Cycle, TOGAF Enterprise Metamodel,
  Content Framework, Architecture Repository, Enterprise Continuum, ABB→SBB,
  ADM Iteration Cycles, Architecture Landscape levels, Stakeholder Power/Interest
  matrix, Architecture Partitioning) — click any diagram to enlarge
- **Score history stored in your browser (localStorage)** — plus Export to JSON

## Run it

Just **double-click `index.html`** (or open it in any browser). No server
required.

The question banks are loaded as plain JavaScript files
(`data/questions_level1.js` / `data/questions_level2.js`) via `<script>` tags,
so everything runs straight from `file://`. Keep the `data/` folder next to
`index.html`.

## Accuracy and verification

> **This tool is provided as a free study aid on a best-effort basis. It is
> not authoritative and is not a substitute for the official TOGAF Standard,
> a reputable study guide, or accredited training.**

The questions and rationales were drafted with reference to the TOGAF Standard
10th Edition evaluation bundle (C220 Parts 0-5) and then run through a
self-review pass to catch obvious errors, miscitations, and TOGAF 10 → TOGAF 9
naming drift. A handful of corrections were applied as a result (e.g.
*Architecture Development iteration*, *TOGAF Enterprise Metamodel*,
*Implementation Factor Catalog*). The per-question `Reference:` line on the
review screen points at the C220 section the item was drafted from, so you
can always verify a claim against the source yourself — and you should,
especially before relying on any item for exam preparation.

Known limitations:

- The review pass was best-effort, not exhaustive; remaining inaccuracies,
  ambiguous phrasing, or outdated terminology are likely.
- "Best", "second-best", "third-best" and "distractor" gradings on Level 2
  scenarios reflect the author's interpretation of TOGAF guidance, not an
  Open Group answer key. Real OGEA-102 grading may differ on borderline
  options.
- The L2 question pool is built from 16 distinct scenario templates combined
  with org-name variants. Within any one session the app enforces
  template-distinct picks, so you won't see the same scenario twice in a
  row — but across many sessions you will eventually see every template.
  Coverage is narrower than the headline "128 L2 questions" suggests; treat
  repeated exposure as familiarity practice, not as evidence of mastery.
- Citation accuracy is the author's best read of where each concept lives in
  the standard; chapter and section numbers may be off by one in places.

If you spot an error, please open an issue or a pull request — corrections
are welcome.

For authoritative practice and assessment, use The Open Group's own
materials, an accredited training provider's study pack, or the published
TOGAF® Series Guides and the TOGAF Standard itself.

## Regenerate / extend the question banks

Edit the templates in `generate_questions.py`, then:
```bash
python generate_questions.py
```
This rewrites both JSON files and both JS files (128 questions each).

## Edit or add diagrams

Each reference diagram lives as its own `.svg` file in `data/diagrams/`,
with metadata (title, description, topic) in `data/diagrams/descriptions.json`.
After editing either, rebuild the runtime bundle:
```bash
python build_diagrams.py
```
See `data/diagrams/README.md` for the file conventions and how to add a new
diagram.

## Disclaimer

All questions are **original study material** written in the style/format of
the TOGAF EA Practitioner exam. They are **not** real exam questions and
contain no proprietary Open Group content. For authentic practice exams, use
The Open Group or accredited training providers. TOGAF® is a registered
trademark of The Open Group.

Score history is stored locally in your browser (`localStorage`) and never
leaves your machine.
