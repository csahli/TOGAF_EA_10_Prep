# TOGAF® EA Practitioner — Mock Exam Studio

A single-page web app for practising TOGAF Standard 10th Edition exam questions,
aligned to the published OGEA-101 / OGEA-102 / OGEA-103 exam structure.

## Features

- **Level 1 (Foundation)** — 128 single-best-answer recall questions, every
  item with a citation back to the TOGAF Standard 10th Edition (C220) or the
  relevant TOGAF Series Guide. 128 unique stems across 25 topics.
- **Level 2 (Practitioner)** — 128 scenario questions using the **official
  OGEA-102 gradient: best = 5, second-best = 3, third-best = 1, distractor = 0**.
- **Blended** — mixes both levels in one practice session.
- **Practice mode** — pick your own question count, shuffle and toggle instant
  feedback per question.
- **Official exam simulation** — enforces the published Open Group conditions:
  - OGEA-101: 40 questions / 60 minutes / closed book / 24-40 pass
  - OGEA-102: 8 questions / 90 minutes / open book / 24-40 pass
  - OGEA-103 Combined: 48 questions / 150 minutes / each part 24-40 to pass
  - Visible countdown timer, auto-submit on timeout
- Score ring, per-question review with rationales **and source citations**
  shown on the review screen
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

Every Level 1 item and every Level 2 template was cross-checked against the
TOGAF Standard 10th Edition evaluation bundle (C220 Parts 0-5) by a per-part
verification pass. The check confirmed:

- 16 of 16 Level 2 "best" (5-point) answers are correct per C220
- All Level 1 ADM-phase items (37/37) verified clean against C220 Part 1
- Substantive errors found during verification have been corrected (including
  TOGAF 10 renames: Architecture Development iteration, TOGAF Enterprise
  Metamodel, Implementation Factor Catalog) and citations have been moved to
  the correct C220 part or TOGAF Series Guide

See the per-question `Reference:` line on the review screen for the exact
C220 section that supports each item.

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
