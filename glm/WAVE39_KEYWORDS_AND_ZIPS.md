# Wave 39 — The six top keywords per paper + the LaTeX source bundles

**Directive (2026-09-14).** "For both papers, select 6 top keywords. For
both papers, provide LaTeX documents with figures and tables compressed
into a .zip format."

**Scope.** Both papers, as new versions continuing the unblind-labelled
line: instruments v17 → v18 (`manuscript uploads v18/instruments-paper-unblinded18.tex`),
main v14 → v15 (`manuscript uploads v18/main-article-unblinded15.tex`),
plus two submission-ready .zip bundles staged in the session download
folder. The keyword lines are trimmed to six entries each, SELECTED
FROM THE EXISTING LISTS ONLY (no new keyword text coined) — a
front-matter metadata change; no prose, mathematics, figures, captions,
labels, or references touched, so the no-new-claims gate holds
trivially. One changed source line per paper (2 diff lines), file line
counts unchanged (compile-warning line numbers preserved exactly).

## The selections

**Instruments (6 of the existing 10):**
`quantum instruments; diamond norm; compression width; Chebyshev radius;
equivariant cohomology; Borsuk--Ulam theorem.`
Dropped: *antipodal profile* (subsumed under the compression-width /
Borsuk–Ulam pair), *quantum measurements* (subsumed under quantum
instruments), *flag manifolds* (the stage rather than the contribution —
subsumed under equivariant cohomology, which names the machinery of the
flag-quotiet computation), *no-programming theorem* (appendix-only
material).
Rationale: one entry per load-bearing axis of the paper — the object
(title), the metric, the central quantity (title: Certified Compression
Bounds), the exact-geometry headline (title: Optimal Centres), the
flag-quotient obstruction machinery (title: Flag-Quotient Width
Obstructions), and the antipodal obstruction engine.

**Main (6 of the existing 9):**
`quantum channel compression; diamond norm; antipodal width; exact
in-radius; nonlinear approximation; Borsuk--Ulam theorem.`
Dropped: *quantum combs* (the cited adaptive-network framework; the
query-uniform results are already indexed by "quantum channel
compression"), *flat-width dichotomy* and *flag-quotient cohomology*
(the companion's contributions, appearing here only as the
input-independent specialisation summary).
Rationale: the problem statement, the metric (title: Exact Diamond
Balls), the central obstruction concept (title: Antipodal Widths), the
exact-geometry headline, the mathematical lineage
(DeVore–Howard–Micchelli/Pinkus, the abstract's framing sentence), and
the topological engine.

## QA battery

- **edit_v18.py**: each anchor matched exactly once; diff audit = 2
  changed lines per paper (the one keyword line replaced); .txt
  byte-mirrors written (house convention since v15).
- **check_v18.py: 54/54 PASS, exit 0.** P-layer: blind-marker and
  placeholder sweeps (the wave-38 identity and declarations properties
  persist, byte-exact); the new six-keyword line byte-exact with
  exactly six entries, the kept entries in order, the dropped entries
  absent from the keyword line; the reconstruction gate (new == source
  + exactly the one hunk, independently re-derived and byte-verified);
  .txt == .tex; label / ref / cite / caption / section / bibitem
  ledgers all unchanged (zero ref/cite deltas this wave); math-delimiter
  parity; source line counts unchanged. M-layer: page counts 53/46
  (unchanged); the page-1 title-block render needles; the page-1
  rendered Keywords-line gate (six kept present, dropped absent, on
  that line); full-text blind and placeholder sweeps; declarations
  render needles; the companion-citation render.
- **Tectonic: exit 0 on both; 53/46 pages.** The number-free warning
  SIGNATURE sets identical to fresh v17/v14 baselines
  (w39_warn_cmp.py, re-compiled fresh this wave). The only raw delta is
  documented and benign: the v17 keywords line was Overfull by
  0.19373pt (once per TeX pass) and the trimmed v18 line fits, so that
  warning is gone — a layout improvement, not a defect. Main's warning
  file is byte-identical to the baseline modulo the basename. Honest
  debug trail: one checker bug fixed in place (the basename-stripping
  prefix regex in the raw-line comparison; the wave-36/37/38 quirk
  class).
- **W31 derivation battery re-run: ALL GATES PASS.** The mathematics
  untouched; the verdict chain unchanged (x^2 ≠ 0; H^6 = Z with the
  discriminant twice a generator; delta_2 = 4/3; ququart [4/3, 3/2]
  OPEN; the W23 stop stands).
- **VLM verification on both page-1 renders**: title blocks complete
  and clean (identity + date), the Keywords lines rendered completely
  within the margins, no truncation, no overlap, no defects; the model
  reads back exactly the six selected keywords on both pages.

## The .zip bundles

Both papers are fully self-contained LaTeX documents: all figures are
TikZ/pgfplots pictures and all tables are tabular environments typeset
INLINE in the .tex; the bibliographies are inline `thebibliography`
environments (no .bib/.bbl). Each bundle therefore contains exactly
three files:

| Bundle | Contents |
|---|---|
| `instruments-paper-unblinded18-latex.zip` | `README.txt` (manifest: title, version, six keywords, figure/table inventory, compile instructions), `instruments-paper-unblinded18.tex` (4 figures / 9 TikZ diagrams / 3 tables, all inline), `instruments-paper-unblinded18.pdf` (53 pp., compiled reference) |
| `main-article-unblinded15-latex.zip` | `README.txt` (same manifest structure), `main-article-unblinded15.tex` (4 figures / 2 tables, all inline), `main-article-unblinded15.pdf` (46 pp., compiled reference) |

**Round-trip validation**: each zip extracted into a clean directory
and compiled from the extracted source — Tectonic exit 0 on both, 53/46
pages; the zipped .tex and .pdf bytes are SHA-256-identical to the repo
deliverables in `manuscript uploads v18/`; the download-folder copies
are byte-identical to the working zips. The bundles need no network or
external assets at compile time beyond standard CTAN packages.

**Staging**: the two zips live in the session download folder (with the
wave's PDFs, .tex sources, and this note); the repo carries the
`manuscript uploads v18/` folder (tex/txt/pdf, both papers) as the
audit trail.
