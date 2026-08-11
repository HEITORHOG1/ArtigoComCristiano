# AGENTS.md

This file provides guidance to Codex (Codex.ai/code) when working with code in this repository.

## What this repository is

A hybrid project with two equally important parts:

1. **`.Codex/skills/`** — 16 `SKILL.md` files that future Codex instances invoke via `/skill-name` to assist with writing, reviewing, editing, and submitting scientific papers. The skills are the reusable deliverable.

2. **`artigo/`** — An **active manuscript** in LaTeX (Elsevier CAS template `cas-dc`): *"A Kirkpatrick-based Framework for Integrating Safety and Sustainability in Aviation Maintenance"*, by Dr. José Cristiano Pereira (UCP + GE Aviation, corresponding) and Heitor Oliveira Gonçalves (UCP), targeting the *Journal of Air Transport Management*. The original Word/PDF source lives in `ArtigoExemplo/`; the Elsevier template in `els-cas-templates/`; planning notes in `planejamento/`.

Edits are to Markdown (skills) and LaTeX/BibTeX (manuscript).

## Manuscript build commands

Compile from `g:\ArtigoComCristiano\artigo\` using MiKTeX:

```bash
pdflatex -interaction=nonstopmode main.tex
bibtex main
pdflatex -interaction=nonstopmode main.tex
pdflatex -interaction=nonstopmode main.tex   # third pass for cross-refs + page count
```

Standalone deliverables (each in `artigo/`): `pdflatex cover-letter.tex`, `pdflatex response-to-reviewers.tex`, `pdflatex highlights.tex`, `pdflatex graphical-abstract.tex`.

After compile, **always validate the PDF** by extracting text:

```bash
pdftotext main.pdf -
```

Then grep for:
- Broken ligatures (`condentiality`, `eects`, `veried`, `simplied`, `quantied`, `aliated`, `ndings`) — must NOT appear
- `??` (unresolved references) — must NOT appear
- Math glyph corruption (`˜` for `%`, `ù` for `≈`, `İ` for `×`, `¡Corresponding`) — must NOT appear
- `[FIRST AUTHOR FULL NAME]` style placeholders — must NOT appear

## Font setup (CRITICAL — don't break this)

`cas-dc.cls` loads STIX for math but STIX serif lacks `fi/ff/fl` ligatures at small sizes (tables, figures). The fix in `main.tex` preamble redirects ONLY text families to Latin Modern, leaving math configuration untouched:

```latex
\usepackage[utf8]{inputenc}
\usepackage[T1]{fontenc}
\renewcommand{\rmdefault}{lmr}    % serif → Latin Modern Roman
\renewcommand{\sfdefault}{lmss}   % sans  → Latin Modern Sans
\renewcommand{\ttdefault}{lmtt}   % mono  → Latin Modern Mono
\usepackage[expansion=false]{microtype}
```

Do **not** use `\usepackage{lmodern}` directly — it resets math font setup and breaks `\approx`, `\times`, `\cdot`, `\pm`, `\Delta` to garbage chars (`ù`, `İ`, `⊙`, `,`, `İ`). Do not use `\sffamily` inside TikZ figures — fall back to the default (now Latin Modern Roman) to preserve ligatures. `microtype` needs `expansion=false` because STIX math glyphs aren't expandable.

## Pitfalls when editing LaTeX in bulk

### Regex on `\S` and other LaTeX backslash-letter patterns

The `\S` macro produces `§` in LaTeX. In regex, `\S` is the "non-whitespace" metacharacter. Bulk substitutions that try to match `\S` literally have repeatedly destroyed files in this repository:

- `perl -pe 's/\\S/.../g'` — perl reads `\S` as non-whitespace, matches ANY non-whitespace character
- `python re.sub(r'\\S(\d)', r'\1', text)` — same issue: `\\S` in raw string is `\S` in regex (non-whitespace), not literal `\S`

This has destroyed `as9100` → `a900`, `Kirkpatrick2010` → `Kirkpatric210`, `RQ1` → `R1`, `USD~1.19` → `USD119`, citation keys, equation numbers, etc.

**Safe approach for backslash-letter patterns in LaTeX**: use Python with explicit literal string replacement, never regex:

```python
text = text.replace(r'\S6.1', '6.1').replace(r'\S7.1', '7.1')  # etc.
```

Or use the `Edit` tool one occurrence at a time. Verify with `grep -n` after each batch.

### Other LaTeX-specific gotchas

- `\textsc{iata}`, `\textsc{sae}` etc. render as lowercase small-caps glyphs (looks broken) — use literal `IATA`, `SAE` uppercase instead.
- `\begin{enumerate}[(i)]` requires the old enumerate syntax; with `enumitem` loaded use `\begin{enumerate}[label=(\roman*)]` and `[label=(\alph*)]`.
- TikZ figure width: cas-dc single column ≈ 8.4 cm, full text width (`figure*`) ≈ 17 cm. Wide TikZ pictures must use `figure*` AND `\resizebox{0.95\textwidth}{!}{\input{...}}` or they overflow.
- Tables of clauses should be referenced as "clause 7.2" / "(7.1)" in body text — `§` symbol was removed from the manuscript per user preference.

## Skills architecture

16 skills under `.Codex/skills/`, each a single `SKILL.md` with YAML frontmatter (`name`, `description`).

### Core personas (4)

| Skill | Role |
| ----- | ---- |
| `cientista` | Master persona — Triple Identity (Writer + Reviewer + Editor). Default for any scientific writing task. |
| `escritor-cientifico` | Drafting/rewriting IMRAD sections. |
| `revisor-critico` | I-R-B-MB-E quality review. |
| `editor-cientifico` | Journal conformance, cover letter, reviewer responses, submission. |

### Pipeline & cross-cutting (3)

| Skill | Role |
| ----- | ---- |
| `workflow-artigo` | Autonomous 10-stage pipeline from briefing to submission. |
| `figuras-tabelas` | Visual elements protocol (booktabs, TikZ diagrams, pgfplots charts, captions). |
| `pesquisador-senior` | HUMANIZE writing principles + anti-plagiarism (Elsevier/IEEE templates). |

### Production tooling (2)

| Skill | Role |
| ----- | ---- |
| `latex-elsevier-cas` | Migration protocol from Word/PDF → Elsevier CAS (cas-sc/cas-dc), frontmatter, BibTeX. |
| `journal-jatm` | *Journal of Air Transport Management* specifics — scope, paper types, abstract style. |

### Quality & methodology (4)

| Skill | Role |
| ----- | ---- |
| `anti-vicios-ia` | Post-write audit for AI tics (em-dash overuse, "delve", "vale ressaltar", hedging). |
| `revisao-sistematica-prisma` | PRISMA 2020 SLR — strings, eligibility, flow diagram, GRADE. |
| `reporting-guidelines` | EQUATOR map (CONSORT/STROBE/PRISMA/TRIPOD/STARD/ARRIVE/CARE/SPIRIT/SQUIRE). |
| `estatistica-reporting` | Test choice, assumption checking, effect sizes + 95% CI, multiple-comparison correction. |

### Submission deliverables (3)

| Skill | Role |
| ----- | ---- |
| `highlights-graphical-abstract` | Elsevier Highlights (≤85 char, 3–5 bullets) + Graphical Abstract specs. |
| `resposta-revisores` | Rebuttal letter — point-by-point, conflict between reviewers, elegant disagreement. |
| `discussao-limitacoes` | Discussion + Limitations craft; triangulation, So What?, hedging calibration. |

`cientista` is the broad default; the three other personas sharpen one phase; `pesquisador-senior` overlays HUMANIZE on any writing task; `workflow-artigo` orchestrates the full pipeline; methodology skills handle rigor checks; deliverable skills target high-leverage sections; `figuras-tabelas` and `anti-vicios-ia` are cross-cutting passes.

## Inviolable rules baked into every skill

Duplicated across all 16 SKILL.md files **on purpose** — each skill is invoked independently. When editing a skill, preserve them.

### 1. Three mandatory prerequisites

Before producing or auditing any article content, the agent must have received from the user:

1. **Título** of the article (full title + language)
2. **Abstract** + keywords (3–6 terms)
3. **Pasta de PDFs** — absolute path to a folder of reference PDFs

If any is missing, the skill must refuse to start and request the missing item. "Send later" is not accepted.

### 2. Never disclose AI usage

No deliverable (article body, cover letter, acknowledgments, captions, contribution statement, reviewer response) may state that it was written, assisted, or revised by AI / LLM / GPT / Codex / ChatGPT. Remove silently. Sole exception: when AI itself is the **research object** — even then, describe technically without self-disclosing the production process.

The active manuscript has a JATM-mandatory `\section*{Declaration of generative AI and AI-assisted technologies in the writing process}` that states authors **did not** use generative AI — this is the only acceptable form (negative declaration satisfies the journal's mandatory disclosure without violating rule #2).

### 3. Topic-agnostic

Skills must never assume a domain. The agent learns the topic only at runtime via the three prerequisites above. Examples in skills are illustrative.

## Conventions for editing skills

- Each skill lives at `.Codex/skills/<skill-name>/SKILL.md`.
- Frontmatter requires `name` (must match the directory) and `description` (must include when to use AND the prerequisite-enforcement clause).
- Skill bodies are in Brazilian Portuguese; output language for paper content follows the user's project.
- Cross-skill references use plain skill names in backticks (e.g., `` `pesquisador-senior` ``), not file paths.
- Do **not** create `.md` files at the repository root. The root contains only `AGENTS.md` and the four content directories (`.Codex/`, `artigo/`, `ArtigoExemplo/`, `els-cas-templates/`, `planejamento/`).

## Memory

Persistent project guidance lives at `~/.Codex/projects/g--ArtigoComCristiano/memory/` and is auto-loaded:

- `feedback_agentes_genericos.md` — topic-agnostic rule
- `feedback_nao_revelar_ia.md` — no-AI-disclosure rule

Update these (and `MEMORY.md`) when the user adds new design feedback that should survive across sessions.
