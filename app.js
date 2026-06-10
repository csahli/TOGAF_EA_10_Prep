/* =========================================================================
   TOGAF EA Practitioner — Mock Exam Studio
   Vanilla JS SPA. Loads two question banks, runs L1/L2/blended sessions,
   scores (incl. Level 2 gradient scoring), and persists history in localStorage.
   ========================================================================= */

const HISTORY_KEY = "togaf_exam_history_v1";
const THEME_KEY = "togaf_exam_theme";


const state = {
  banks: { 1: [], 2: [] },
  loaded: false,
  mode: "1",            // "1" | "2" | "blended"
  count: 20,
  shuffle: true,
  instant: true,
  session: [],          // array of question objects (working copy)
  answers: [],          // per-question: { choice: index|null, scored: number, max: number, correct: bool }
  index: 0,
};

const MODE_HINTS = {
  "1": "Single best answer. Knowledge recall across the TOGAF Standard.",
  "2": "Scenario questions with gradient scoring: best = 5, second-best = 3, others = 0.",
  "blended": "A mix of Level 1 recall and Level 2 scenarios in one session.",
};

/* ---------- helpers ---------- */
const $ = (sel) => document.querySelector(sel);
const $$ = (sel) => Array.from(document.querySelectorAll(sel));
const LETTERS = ["A", "B", "C", "D", "E", "F"];

function shuffleArr(arr) {
  const a = arr.slice();
  for (let i = a.length - 1; i > 0; i--) {
    const j = Math.floor(Math.random() * (i + 1));
    [a[i], a[j]] = [a[j], a[i]];
  }
  return a;
}

function escapeHtml(s) {
  return String(s).replace(/[&<>"']/g, (c) => ({
    "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;", "'": "&#39;",
  }[c]));
}

// Renders **bold** segments only (used in scenario text) safely.
function renderInline(text) {
  const escaped = escapeHtml(text);
  const bold = escaped.replace(/\*\*(.+?)\*\*/g, "<strong>$1</strong>");
  // Multi-paragraph scenarios use blank lines (\n\n) between context,
  // situation, and the question — render each block as its own paragraph.
  return bold
    .split(/\n{2,}/)
    .map((block) => `<p>${block.replace(/\n/g, "<br>")}</p>`)
    .join("");
}


/* ---------- theme (light / dark) ---------- */
function applyTheme(theme) {
  const root = document.documentElement;
  if (theme === "light") root.setAttribute("data-theme", "light");
  else root.removeAttribute("data-theme");
  const icon = document.querySelector("#themeToggle .theme-icon");
  if (icon) icon.textContent = theme === "light" ? "☀" : "☾";
}
function initTheme() {
  let theme;
  try { theme = localStorage.getItem(THEME_KEY); } catch { theme = null; }
  if (!theme) {
    // respect the OS preference on first visit
    theme = window.matchMedia && window.matchMedia("(prefers-color-scheme: light)").matches
      ? "light" : "dark";
  }
  applyTheme(theme);
}
function toggleTheme() {
  const isLight = document.documentElement.getAttribute("data-theme") === "light";
  const next = isLight ? "dark" : "light";
  applyTheme(next);
  try { localStorage.setItem(THEME_KEY, next); } catch (e) { /* ignore */ }
}


/* ---------- data loading ----------

   Banks are loaded as plain <script> files (data/questions_level1.js and
   data/questions_level2.js) that assign window.TOGAF_BANK_1 / _2. This means
   the app runs by simply opening index.html in a browser — NO server needed. */
function loadBanks() {
  try {
    const b1 = window.TOGAF_BANK_1;
    const b2 = window.TOGAF_BANK_2;
    if (!b1 || !b2) throw new Error("Question bank globals not found.");
    state.banks[1] = b1.questions;
    state.banks[2] = b2.questions;
    state.loaded = true;
    $("#bankNote").textContent =
      `${state.banks[1].length} Level 1 + ${state.banks[2].length} Level 2 questions ready.`;
    $("#startBtn").disabled = false;
  } catch (err) {
    state.loaded = false;
    $("#bankNote").innerHTML =
      "⚠️ Could not load question banks. Make sure the <code>data/</code> folder " +
      "with the <code>.js</code> bank files sits next to <code>index.html</code>.";
    $("#startBtn").disabled = true;
    console.error(err);
  }
}


/* ---------- view switching ---------- */
function showView(name) {
  $$(".view").forEach((v) => v.classList.toggle("hidden", v.dataset.view !== name));
  $$(".nav-link").forEach((n) => n.classList.toggle("is-active", n.dataset.nav === name));
  window.scrollTo({ top: 0, behavior: "smooth" });
}

/* ---------- session build ---------- */
function buildSession() {
  let pool;
  if (state.mode === "1") pool = state.banks[1].slice();
  else if (state.mode === "2") pool = state.banks[2].slice();
  else pool = state.banks[1].concat(state.banks[2]); // blended

  if (state.shuffle) {
    pool = shuffleArr(pool);
  } else if (state.mode === "blended") {
    // keep a deterministic but mixed order: interleave L1 and L2
    const l1 = state.banks[1].slice();
    const l2 = state.banks[2].slice();
    pool = [];
    const max = Math.max(l1.length, l2.length);
    for (let i = 0; i < max; i++) {
      if (i < l1.length) pool.push(l1[i]);
      if (i < l2.length) pool.push(l2[i]);
    }
  }

  state.session = pool.slice(0, state.count);

  state.answers = state.session.map((q) => ({
    choice: null,
    scored: 0,
    max: q.level === 2 ? (q.maxScore || 5) : 1,
    correct: false,
  }));
  state.index = 0;
}

/* ---------- quiz rendering ---------- */
function renderQuestion() {
  const q = state.session[state.index];
  const a = state.answers[state.index];
  const total = state.session.length;

  $("#qCounter").textContent = `Question ${state.index + 1} / ${total}`;
  $("#qLevelPill").textContent = q.level === 2 ? "Level 2" : "Level 1";
  $("#qTopic").textContent = q.topic || "";
  $("#progressFill").style.width = `${((state.index) / total) * 100}%`;
  $("#qText").innerHTML = renderInline(q.question);

  const wrap = $("#optionsWrap");
  wrap.innerHTML = "";
  q.options.forEach((opt, i) => {
    const btn = document.createElement("button");
    btn.className = "option";
    btn.innerHTML = `<span class="opt-key">${LETTERS[i]}</span><span class="opt-text">${escapeHtml(opt)}</span>`;
    btn.addEventListener("click", () => selectOption(i));
    wrap.appendChild(btn);
  });

  const fb = $("#feedback");
  fb.classList.add("hidden");
  fb.innerHTML = "";

  // If already answered, re-display locked state
  if (a.choice !== null) {
    applyAnsweredStyles();
    if (state.instant) showFeedback();
  }

  $("#prevBtn").disabled = state.index === 0;
  $("#nextBtn").textContent = state.index === total - 1 ? "Finish ✓" : "Next →";
}

function selectOption(i) {
  const a = state.answers[state.index];
  // In instant mode, lock after first answer; allow change if not instant.
  if (state.instant && a.choice !== null) return;

  const q = state.session[state.index];
  a.choice = i;
  if (q.level === 2) {
    a.scored = q.scores[i];
    a.max = q.maxScore || 5;
    a.correct = a.scored === a.max;
  } else {
    a.correct = i === q.answer;
    a.scored = a.correct ? 1 : 0;
    a.max = 1;
  }

  applyAnsweredStyles();
  if (state.instant) showFeedback();
}

function applyAnsweredStyles() {
  const q = state.session[state.index];
  const a = state.answers[state.index];
  const opts = $$("#optionsWrap .option");

  opts.forEach((el, i) => {
    el.classList.remove("selected", "correct", "partial", "wrong");
    if (state.instant) el.classList.add("locked");

    if (i === a.choice) el.classList.add("selected");

    if (state.instant) {
      if (q.level === 2) {
        const s = q.scores[i];
        if (s === (q.maxScore || 5)) el.classList.add("correct");
        else if (s > 0) el.classList.add("partial");
        else if (i === a.choice) el.classList.add("wrong");
        // show score chip
        if (!el.querySelector(".opt-score")) {
          const chip = document.createElement("span");
          chip.className = "opt-score";
          chip.textContent = `${s} pt${s === 1 ? "" : "s"}`;
          el.appendChild(chip);
        }
      } else {
        if (i === q.answer) el.classList.add("correct");
        else if (i === a.choice) el.classList.add("wrong");
      }
    }
  });
}

function showFeedback() {
  const q = state.session[state.index];
  const a = state.answers[state.index];
  const fb = $("#feedback");
  if (q.level === 2) {
    const r = q.rationales[a.choice];
    const best = q.options[q.answer];
    fb.innerHTML =
      `<strong>You scored ${a.scored} / ${a.max}.</strong> ${escapeHtml(r)}` +
      (a.scored === a.max ? "" : `<br><br><strong>Best answer (${a.max} pts):</strong> ${escapeHtml(best)}`);
  } else {
    fb.innerHTML = a.correct
      ? `<strong>Correct.</strong> ${escapeHtml(q.explanation)}`
      : `<strong>Not quite.</strong> The best answer is <strong>${escapeHtml(q.options[q.answer])}</strong>. ${escapeHtml(q.explanation)}`;
  }
  fb.classList.remove("hidden");
}

function nextQuestion() {
  if (state.index < state.session.length - 1) {
    state.index++;
    renderQuestion();
  } else {
    finishSession();
  }
}
function prevQuestion() {
  if (state.index > 0) {
    state.index--;
    renderQuestion();
  }
}

/* ---------- results ---------- */
function finishSession() {
  $("#progressFill").style.width = "100%";

  const earned = state.answers.reduce((s, a) => s + a.scored, 0);
  const max = state.answers.reduce((s, a) => s + a.max, 0);
  const pct = max ? Math.round((earned / max) * 100) : 0;
  const fullCount = state.answers.filter((a) => a.correct).length;
  const partialCount = state.answers.filter((a) => !a.correct && a.scored > 0).length;
  const answered = state.answers.filter((a) => a.choice !== null).length;

  $("#scorePct").textContent = `${pct}%`;
  $("#scoreRing").style.setProperty("--pct", `${pct}%`);

  let verdict, sub;
  if (pct >= 80) { verdict = "Excellent work."; sub = "You're tracking well above the typical pass threshold."; }
  else if (pct >= 60) { verdict = "Solid progress."; sub = "Around the pass mark — keep reinforcing weak topics."; }
  else { verdict = "Keep practising."; sub = "Review the rationales below and revisit the ADM phases."; }
  $("#resultVerdict").textContent = verdict;
  $("#resultSub").textContent = sub;

  $("#resultStats").innerHTML = `
    <div class="stat"><div class="stat-num">${earned}/${max}</div><div class="stat-lbl">Points</div></div>
    <div class="stat"><div class="stat-num">${fullCount}</div><div class="stat-lbl">Full marks</div></div>
    <div class="stat"><div class="stat-num">${partialCount}</div><div class="stat-lbl">Partial</div></div>
    <div class="stat"><div class="stat-num">${answered}/${state.session.length}</div><div class="stat-lbl">Answered</div></div>`;

  $("#reviewList").classList.add("hidden");
  $("#reviewList").innerHTML = "";

  saveHistory({
    when: Date.now(),
    mode: state.mode,
    count: state.session.length,
    earned, max, pct, fullCount, partialCount,
    responses: state.session.map((q, i) => ({
      id: q.id, level: q.level, choice: state.answers[i].choice,
      scored: state.answers[i].scored, max: state.answers[i].max,
    })),
  });

  showView("results");
}

function renderReview() {
  const list = $("#reviewList");
  list.innerHTML = "";
  state.session.forEach((q, idx) => {
    const a = state.answers[idx];
    const item = document.createElement("div");
    item.className = "review-item";
    let optsHtml = "";
    q.options.forEach((opt, i) => {
      let cls = "review-opt";
      if (q.level === 2) {
        const s = q.scores[i];
        if (s === (q.maxScore || 5)) cls += " correct";
        else if (s > 0) cls += " partial";
        else if (i === a.choice) cls += " chosen-wrong";
      } else {
        if (i === q.answer) cls += " correct";
        else if (i === a.choice) cls += " chosen-wrong";
      }
      const marker = i === a.choice ? "● " : "";
      const scoreTag = q.level === 2 ? ` <em style="margin-left:auto;color:var(--text-faint)">${q.scores[i]} pt</em>` : "";
      optsHtml += `<div class="${cls}"><span>${LETTERS[i]}.</span><span>${marker}${escapeHtml(opt)}</span>${scoreTag}</div>`;
    });
    const expl = q.level === 2
      ? (a.choice !== null ? escapeHtml(q.rationales[a.choice]) : "Not answered.")
      : escapeHtml(q.explanation);
    item.innerHTML =
      `<div class="review-q">${idx + 1}. ${renderInline(q.question)}</div>` +
      optsHtml +
      `<div class="review-expl"><strong>Scored ${a.scored}/${a.max}.</strong> ${expl}</div>`;
    list.appendChild(item);
  });
  list.classList.remove("hidden");
  list.scrollIntoView({ behavior: "smooth" });
}

/* ---------- history (localStorage) ---------- */
function getHistory() {
  try { return JSON.parse(localStorage.getItem(HISTORY_KEY)) || []; }
  catch { return []; }
}
function saveHistory(entry) {
  const h = getHistory();
  h.unshift(entry);
  localStorage.setItem(HISTORY_KEY, JSON.stringify(h.slice(0, 200)));
}
function modeLabel(m) {
  return m === "1" ? "Level 1 · Foundation" : m === "2" ? "Level 2 · Practitioner" : "Blended";
}
function renderHistory() {
  const h = getHistory();
  const body = $("#historyBody");
  if (!h.length) {
    body.innerHTML = `<div class="empty">No sessions yet. Complete a quiz to see your history here.</div>`;
    return;
  }
  body.innerHTML = h.map((e) => {
    const d = new Date(e.when);
    const color = e.pct >= 80 ? "var(--good)" : e.pct >= 60 ? "var(--warn)" : "var(--bad)";
    return `<div class="hist-row">
      <div class="hist-badge" style="background:${color};color:var(--bg)">${e.pct}%</div>
      <div class="hist-meta">
        <div class="hist-mode">${modeLabel(e.mode)}</div>
        <div class="hist-date">${d.toLocaleString()} · ${e.count} questions</div>
      </div>
      <div class="hist-score">${e.earned}/${e.max}<small>${e.fullCount} full · ${e.partialCount} partial</small></div>
    </div>`;
  }).join("");
}
function exportHistory() {
  const blob = new Blob([JSON.stringify(getHistory(), null, 2)], { type: "application/json" });
  const url = URL.createObjectURL(blob);
  const a = document.createElement("a");
  a.href = url;
  a.download = `togaf_score_history_${new Date().toISOString().slice(0, 10)}.json`;
  a.click();
  URL.revokeObjectURL(url);
}

/* ---------- glossary / definitions ---------- */
const glossaryState = { cat: "All", query: "", built: false };

function buildAdmRing() {
  const g = document.getElementById("admRing");
  if (!g || g.childNodes.length) return;
  const phases = ["Prelim", "A. Vision", "B. Business", "C. Info Sys",
                  "D. Tech", "E. Opp/Sol", "F. Migration", "G. Govern", "H. Change"];
  // Place 9 labels evenly around the ring.
  const cx = 160, cy = 160, r = 120;
  phases.forEach((p, i) => {
    const ang = (i / phases.length) * Math.PI * 2 - Math.PI / 2;
    const x = cx + r * Math.cos(ang);
    const y = cy + r * Math.sin(ang);
    const circle = document.createElementNS("http://www.w3.org/2000/svg", "circle");
    circle.setAttribute("cx", x); circle.setAttribute("cy", y);
    circle.setAttribute("r", 26); circle.setAttribute("class", "adm-seg");
    g.appendChild(circle);
    const t = document.createElementNS("http://www.w3.org/2000/svg", "text");
    t.setAttribute("x", x); t.setAttribute("y", y + 3);
    t.setAttribute("text-anchor", "middle"); t.setAttribute("class", "adm-lbl");
    t.style.fontSize = "8px";
    t.textContent = p;
    g.appendChild(t);
  });
}

function renderGlossary() {
  const data = window.TOGAF_GLOSSARY;
  const listEl = $("#glossaryList");
  if (!data) { listEl.innerHTML = `<div class="gloss-empty">Glossary data not loaded.</div>`; return; }

  buildAdmRing();

  // category chips (build once)
  if (!glossaryState.built) {
    const cats = ["All", ...Array.from(new Set(data.terms.map((t) => t.category)))];
    $("#glossaryCats").innerHTML = cats.map((c) =>
      `<button class="cat-chip${c === glossaryState.cat ? " is-active" : ""}" data-cat="${escapeHtml(c)}">${escapeHtml(c)}</button>`
    ).join("");
    $$("#glossaryCats .cat-chip").forEach((chip) => chip.addEventListener("click", () => {
      glossaryState.cat = chip.dataset.cat;
      $$("#glossaryCats .cat-chip").forEach((c) => c.classList.toggle("is-active", c === chip));
      renderGlossary();
    }));
    glossaryState.built = true;
  }

  const q = glossaryState.query.trim().toLowerCase();
  const filtered = data.terms.filter((t) => {
    const inCat = glossaryState.cat === "All" || t.category === glossaryState.cat;
    const inQuery = !q || t.term.toLowerCase().includes(q) || t.definition.toLowerCase().includes(q);
    return inCat && inQuery;
  });

  if (!filtered.length) {
    listEl.innerHTML = `<div class="gloss-empty">No terms match your search.</div>`;
    return;
  }

  const highlight = (text) => {
    const esc = escapeHtml(text);
    if (!q) return esc;
    const re = new RegExp(`(${q.replace(/[.*+?^${}()|[\]\\]/g, "\\$&")})`, "ig");
    return esc.replace(re, "<mark>$1</mark>");
  };

  listEl.innerHTML = filtered.map((t) => `
    <div class="gloss-item">
      <div class="gloss-head">
        <span class="gloss-term">${highlight(t.term)}</span>
        <span class="gloss-cat">${escapeHtml(t.category)}</span>
      </div>
      <p class="gloss-def">${highlight(t.definition)}</p>
      <a class="gloss-doc" href="${escapeHtml(t.doc)}" target="_blank" rel="noopener">📖 Read in TOGAF Standard ↗</a>
    </div>`).join("");
}

/* ---------- wiring ---------- */
function init() {

  // theme
  initTheme();
  $("#themeToggle").addEventListener("click", toggleTheme);

  // nav

  $$(".nav-link").forEach((n) => n.addEventListener("click", () => {
    const v = n.dataset.nav;
    if (v === "history") renderHistory();
    if (v === "glossary") renderGlossary();
    showView(v);
  }));

  // glossary search
  $("#glossarySearch").addEventListener("input", (e) => {
    glossaryState.query = e.target.value;
    renderGlossary();
  });


  // mode segmented control
  $$("#modeGroup .seg-btn").forEach((b) => b.addEventListener("click", () => {
    $$("#modeGroup .seg-btn").forEach((x) => x.classList.remove("is-active"));
    b.classList.add("is-active");
    state.mode = b.dataset.mode;
    $("#modeHint").textContent = MODE_HINTS[state.mode];
  }));

  // count + toggles
  $("#countRange").addEventListener("input", (e) => {
    state.count = parseInt(e.target.value, 10);
    $("#countVal").textContent = state.count;
  });
  $("#shuffleToggle").addEventListener("change", (e) => state.shuffle = e.target.checked);
  $("#instantToggle").addEventListener("change", (e) => state.instant = e.target.checked);

  // start
  $("#startBtn").addEventListener("click", () => {
    if (!state.loaded) return;
    buildSession();
    showView("quiz");
    renderQuestion();
  });

  // quiz nav
  $("#nextBtn").addEventListener("click", nextQuestion);
  $("#prevBtn").addEventListener("click", prevQuestion);
  $("#quitBtn").addEventListener("click", () => { if (confirm("Quit this session? Progress will not be saved.")) showView("home"); });

  // results
  $("#reviewBtn").addEventListener("click", renderReview);
  $("#againBtn").addEventListener("click", () => showView("home"));

  // history tools
  $("#exportBtn").addEventListener("click", exportHistory);
  $("#clearBtn").addEventListener("click", () => {
    if (confirm("Delete all saved score history?")) { localStorage.removeItem(HISTORY_KEY); renderHistory(); }
  });

  showView("home");
  loadBanks();
}

document.addEventListener("DOMContentLoaded", init);
