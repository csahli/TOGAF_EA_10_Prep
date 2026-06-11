# Reference diagrams

This directory holds the source-of-truth for the 10 TOGAF reference diagrams
shown in the app's Glossary view.

## Files

- `*.svg` — one inline SVG per diagram. Each can be opened standalone in a
  browser (the CSS variables fall back to defaults, so dark-mode tinting
  won't apply, but the structure renders).
- `descriptions.json` — metadata for each diagram (`id`, `title`, `topic`,
  `description`, optional `buildHook`). The `id` must match the SVG file
  basename (e.g. `architecture-repository` ↔ `architecture-repository.svg`).
- `../diagrams.js` — auto-generated bundle. The app loads this; it embeds
  the SVG markup as a string alongside the description so the app can run
  from `file://` without `fetch()`.

## Workflow

1. Edit a `.svg` file (or add a new one).
2. Update `descriptions.json` (add/edit the matching entry).
3. From the project root, run:

   ```bash
   python build_diagrams.py
   ```

   This regenerates `data/diagrams.js` from these sources.

4. Hard-reload `index.html` in the browser.

## Adding a new diagram

1. Create `data/diagrams/<id>.svg` using the existing diagrams as a template.
   Use CSS variables (e.g. `var(--accent)`, `var(--text-dim)`) so the
   diagram theme-switches with the app.
2. Add a corresponding entry to `descriptions.json` with the same `id`.
3. If the diagram needs JavaScript layout (like the ADM ring's computed node
   positions), add a `buildHook` field naming a function registered in
   `DIAGRAM_BUILD_HOOKS` in `app.js`.
4. Run `python build_diagrams.py`.

## SVG conventions

- Always include `xmlns="http://www.w3.org/2000/svg"` on the root `<svg>` so
  the file opens standalone.
- Always include `class="svg-diagram"` and `role="img"` plus a descriptive
  `aria-label` so screen readers get a meaningful summary.
- Style with classes defined under "SVG diagram styling" in `styles.css`.
  Avoid inline `style=` attributes so theme switching works.
- Marker `id`s must be globally unique across all diagrams (the app injects
  every SVG into the same DOM). Use a prefix per diagram (e.g. `mm-`, `bb-`).
