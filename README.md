# TOGAF® EA Practitioner — Mock Exam Studio

A single-page web app for practising TOGAF Standard 10th Edition exam questions.

## Features
- **Level 1 (Foundation)** — 128 single-best-answer recall questions (`data/questions_level1.json`)
- **Level 2 (Practitioner)** — 128 gradient-scored scenario questions (`data/questions_level2.json`)
- **Blended** mode mixes both levels in one session
- Choose question count, shuffle, instant feedback
- Gradient scoring for Level 2 (best = 5, second-best = 3, others = 0)
- Score ring, per-question review with rationales
- **Score history stored in your browser (localStorage)** — plus Export to JSON

## Run it
Just **double-click `index.html`** (or open it in any browser). No server required.

The question banks are loaded as plain JavaScript files
(`data/questions_level1.js` / `data/questions_level2.js`) via `<script>` tags,
so everything runs straight from `file://`. Keep the `data/` folder next to
`index.html`.


## Regenerate / extend the question banks
Edit the templates in `generate_questions.py`, then:
```bash
python generate_questions.py
```
This rewrites both JSON files (128 questions each).

## Disclaimer
All questions are **original study material** written in the style/format of the
TOGAF EA Practitioner exam. They are **not** real exam questions and contain no
proprietary Open Group content. For authentic practice exams, use The Open Group
or accredited training providers. TOGAF® is a registered trademark of The Open Group.
