# WAVE 35 — Figures and readings (v14): the two merited diagrams and the two merited text additions

**Directive (2026-09-14).** Implement the shortlist from the merit assessment
as a wave — the phase diagram, the fibration diagram, and the two text
additions — each gated by a no-new-claims check and the same compile/QA
battery as v13; humanize faithfully for conceptual clarity, seamless flow and
easy understanding, after looking up a few related landmark articles.

**Scope.** Instruments paper only, v13 → v14. The main article is unchanged
(it defers the flat-width classification to the companion and already carries
its own figures); it stays at v11 in `manuscript uploads v13/`, byte-verified.

**A reconstruction note.** The shortlist itself was delivered in the
conversation preceding this session and was not persisted to disk; the four
items were re-derived from the manuscripts against the same
"genuine, non-decorative, non-superficial" gate before implementation:
(i) the flat-width classification is stated across five theorems, three
corollaries, one lemma and one conjecture whose regime picture the reader must
currently assemble mentally — a phase diagram is genuinely load-bearing; (ii)
the proof of `prop:cupsquare` juggles six spaces and eight maps in its first
two steps — a fibration diagram fixes them, and a long spectral-sequence
computation merits a guide paragraph; (iii) the operational meaning of the
flat value versus the 4/3 surcharge (the paper's own rem:operational exists
precisely for this) merits an explicit reading paragraph. All four additions
land in the instruments paper, where the underlying results live.

---

## 1. The four items and where they landed

### Item 1 — the fibration diagram (`fig:flag-fibration`)

Placed in the running text immediately before Proposition `prop:cupsquare`
(floats to page 36). Content, drawn exactly as stated in the proof:

* the Borel pullback square of Step 1: `EU(3)×_K U(3) → EU(3)` (top, labelled
  `[e,g] ↦ eg`), `→ BK` (labelled ρ), `EU(3) → BU(3)`, `BK → BU(3)` (labelled
  `Bι`), the pullback note, the fibre labels `U(3)` on both vertical arrows,
  the annotations "≃ B" (Step 1: homotopy equivalent to `K\U(3) ≅ B`) and
  "contractible";
* the quotient tower of Step 0: `Fl = U(3)/T³`, `B = U(3)/K = Fl/⟨c⟩`, the
  regular 3-fold cover with deck group ⟨c⟩ ≅ Z/3;
* the classifying maps of Step 6: `γ: B → BK` (classifies the principal
  K-bundle `U(3) → U(3)/K`), `π: BK → BC₃` (the quotient), `κ = π∘γ`;
* the fibre arrow `BT³ → BK` of the Step 2 fibration `BT³ → BK → BC₃`.

No-new-claims gate: a 19-entry correspondence table (checker gate M-fib)
verifies that every node, arrow, and annotation string of the figure occurs
in the proof text of the paper — nothing is drawn beyond the stated maps.

### Item 2 — the proof guide (text addition 2)

Inserted between the proof's opening paragraph ("...the cyclic cohomology of
finite modules.") and Step 0. One paragraph, seven sentences, one per step
plus the figure pointer; the register follows the landmark survey below. It
uses the paper's own vocabulary ("the crux of Step 5" is the proof's own
phrase). No mathematical assertion beyond the step texts.

### Item 3 — the phase diagram (`fig:flat-regimes`)

Placed after the conjecture discussion and before Example `ex:222` (floats to
page 45; referenced from the reading paragraph). Three side-by-side panels in
the (r, nd_B) plane, in the house `pgfplots` axis style of `fig:envelope`,
each panel honest at its own lattice:

* **(a) d_B = 1**: δ_r = 1 between the phase boundary nd_B = 2r+2 and the
  exact-reconstruction region (r ≥ D = n−1); δ_r ≥ 4/3 above the boundary
  (Corollaries 6.8/6.4 = `cor:classical-dichotomy`/`cor:flat-fails`); the
  dashed line nd_B = 2r+3 with the exact value 4/3 marked at (1,5),(2,7),(3,9)
  (`cor:exact-d1`); the row nd_B = 2 is the collapse case (i).
* **(b) d_B = 2**: flat ⟺ below the boundary (`cor:qubit-dichotomy`,
  r ≥ n−1 ⟺ nd_B ≤ 2r+2); δ_r ≥ 4/3 above; the row nd_B = 2 is the collapse
  case (ii) (`thm:collapse`: δ = 1 below D = 3, 0 from D on — the drawn
  regions reproduce this row exactly).
* **(c) d_B ≥ 3**: red above the boundary (`cor:flat-fails`) and in the
  columns r ∈ {1,2} (the state-space obstruction, `thm:state-nonflat` +
  `thm:state-d2` + the concentration gate `lem:slice-gate`); below the
  boundary at r ≥ 3: the conjectured region (`con:coord-flat`, light fill),
  the certified sub-region beyond the pinching boundary r = nQ_2(d_B)−1
  (`thm:pinching`; drawn for d_B = 3 where Q_2(3) = 5), the strip between
  open (`rem:flat-status`); the dotted exact-reconstruction boundary (drawn
  for d_B = 3); the qutrit exact points (1,3),(2,3), the point (1,6)
  (n = 2, 2(1−1/3) = 4/3, `thm:mass-exact`), and the open ququart point
  (1,4) with δ₁ ∈ [4/3, 3/2] (`cor:bottom-dichotomy`).

No-new-claims gate (checker gates M-a/M-b/M-c/M-fig): the lattice partition
of each panel is re-derived from the cited statements and compared with the
drawn half-planes at every lattice point in a window (r ≤ 15/40, n ≤ 20/10);
the two drawn lines for d_B = 3 are verified to pass through their lattice
points ((5n−1, 3n) and (9n−1, 3n)); Q_2(3) = 5 is computed as the balanced
two-sector instantiation of `thm:pinching`'s formula; every label box is
verified to lie strictly inside its region. Two arithmetic instantiations are
flagged as such (not new claims): Q_2(3) = 2²+1² = 5 from the theorem's
r_out = d_A²(n Σ b_j² − 1) with the balanced split of 3; and the caption's
2(1−1/3) = 4/3.

### Item 4 — the operational reading (text addition 1)

Inserted after the conjecture discussion. One paragraph: the antipodal floor
reading of the value 1 (the flat-half proof's own implication: the exact
antipodal profile forces error ≥ 1 throughout the subcritical range), the
surcharge reading of 4/3 with its mechanism (the equal-value-basis theorems +
the under-weighting inequality of the `thm:state-nonflat` proof: some basis
state under-weighted by mass ≥ 2/3, the trace norm charging twice the missing
mass), the qutrit exactness, and the operational detectability (an error of
4/3 instantiates rem:operational's formula at 1/2 + (1/4)(4/3) = 5/6).

No-new-claims gate: every sentence is a restatement of a cited result or an
arithmetic instantiation of a stated formula; the two instantiations (5/6;
the 2/3 missing mass) are exact-fraction-verified in the checker (gate M).

---

## 2. The landmark scan (the "look up a few related landmark articles" directive)

Live web lookups (logs in `scripts/landmark_lookups/`; the closest
neighbours' abstract pages were already cached in `glm/novelty_pass/` from
Wave 27):

* **Guerra–Jana**, *Cohomology of complete unordered flag manifolds*
  (arXiv 2309.00429; Trans. AMS 378 (2025)) — the closest neighbouring
  paper, cited as `GuerraJana2025`. Register: declarative first-person
  plural, results stated as achievements ("We compute... We show..."),
  zero meta-commentary.
* **Matszangosz**, *On the cohomology rings of real flag manifolds: Schubert
  cycles* (arXiv 1910.11149; Math. Ann. 381 (2021)) — "We give an
  algorithm...", "We conjecture..."; algorithms and conjectures stated flatly.
* **Korbaš–Lőrinc** and the Borsuk–Ulam application literature (survey-level
  material) — intuition delivered as plain declarative prose tied to the
  objects.
* **Nielsen–Chuang**, *Programmable quantum gate arrays* (quant-ph/9703032)
  — the quantum-side landmark: physical intuition (measurement disturbance,
  no-cloning) woven into flowing prose, never as asides.
* **DeVore–Howard–Micchelli**, *Optimal nonlinear approximation*
  (Manuscripta Math. 63 (1989)) — the widths landmark; crisp statement pairs.

The style lessons applied: intuition as plain declarative sentences; one
purposeful sentence introducing each figure ("Figure X records/displays
..."); captions carry the precise content with honest qualifiers (the house
caption convention of `fig:radius-notions`: "The drawing is schematic; ..."),
maintained here by the caption sentence "The drawings are schematic: the
regions are exact at the lattice points of each panel within the subcritical
range...".

---

## 3. The edit and QA records

**The edit** (`scripts/edit_v14.py`, three anchored hunks — the fibration
figure, the guide, the reading + phase figure — each matched exactly once;
the figure blocks live in `scripts/w35_fibration_fig.tex` and
`scripts/w35_phases_fig.tex`): instruments v14 written to
`manuscript uploads v14/` (.tex + identical .txt twin), delta +11,578 chars;
**the edit is a pure insertion** (checker gate: every paragraph of the v13
source is contained in v14 verbatim). Honest debug trail: one anchor
mismatch (the proof opening's line break "of\nfinite modules.") caught on
first run and fixed in place.

**The QA battery (as v13):**

* **`check_v14.py`: 96/96 PASS, exit 0.** P-layer: 23 new-phrase presences;
  17 must-hold anchors (the prop:cupsquare statement, both transgression
  displays, the Step-5 crux display, the Step-6 edge, the dichotomy
  statements) byte-intact; `.txt == .tex`; labels unique, all refs resolve;
  informal-register sweep clean; main article byte-unchanged; v13 contained
  in v14. R-layer: 19 render needles through pdftotext normalisation (form
  feeds, page-number lines, hyphenation, ligatures, dashes) plus the
  raw-mode gates for the rotated in-figure labels (layout-mode pdftotext
  drops rotated runs — "certified flat", the two bare "fibre" lines, and the
  "regular 3-fold" note all verified in raw mode; same extraction-quirk class
  the v13 QA documented). M-layer: the phase-diagram lattice partitions
  re-derived panel-by-panel from the cited theorems and matched to the drawn
  half-planes at every lattice point in the window; the two d_B = 3 lines
  pass through (5n−1, 3n) and (9n−1, 3n); Q_2(3) = 5; the exact-value marks;
  the 5/6 and 2/3 arithmetic instantiations (exact fractions); the
  19-entry fibration correspondence table; every label box inside its region.
  Honest debug trail: five checker-needle bugs fixed en route (the
  "conjectured flat" substring colliding with the pre-existing "conjectured
  flat range"; three must-hold anchors with wrong line breaks; three
  correspondence needles with math-delimiter/line-break mismatches; the
  rotated-label extraction mode).
* **Tectonic: exit 0, 53 pages (v13: 51)** — the two figures and two
  paragraphs add two pages. The number-free warning multiset is **identical
  to the v13 baseline** (8 Overfull + 18 Underfull + 1 summary), and every
  warning region is pre-existing (the abstract/keywords line, the
  flag-literature overfull pair 3.34/11.59 pt, the tab:summary underfulls,
  the bibliography underfulls, the end matter): **zero new typesetting
  defects**. Honest debug trail: the first compile failed with "Environment
  axis undefined" — the phase panels had bare `\begin{axis}` outside a
  `tikzpicture` wrapper (the house figures always wrap; the minimal test
  reproduced it); fixed by wrapping the three panels, compile clean.
* **PDF render QA:** the two figure captions, both inserted paragraphs, and
  the in-figure labels verified rendered (pages 36 and 45); the figures
  introduce no overfull boxes (their tikzpictures fit the 16 cm text width).
* **The Wave-31 derivation battery re-run: ALL 12 GATES PASS, exit 0** — the
  mathematics layer is untouched (pure insertion; the 17 must-hold anchors
  byte-identical).

## 4. What deliberately did NOT change

* Every theorem, lemma, proposition, corollary, conjecture statement, proof,
  display, and constant — the edit is a pure insertion; the verdict chain
  (x² ≠ 0; the tuple; H⁶(B;Z) = Z with the discriminant twice a generator;
  δ₂(D(C³)) = 4/3; the ququart bracket [4/3, 3/2] open; the W23 stop) is
  untouched.
* The main article (v11) — byte-unchanged; its flat-width content is a
  summary pointer to the companion, so the diagrams and readings belong
  where the results are proved.
* The register: the additions are in the landmark style (declarative, we-form
  absent by house convention — the paper states results impersonally), no
  version references, no self-commentary, no informal vocabulary; the
  figure captions follow the honest-qualifier convention of the existing
  figures.

## 5. Artifacts

* `manuscript uploads v14/`: `instruments-paper-revised14.tex` / `.txt` / `.pdf`
  (main stays at v11 in `manuscript uploads v13/`)
* `glm/scripts mirror`: `edit_v14.py`, `check_v14.py`, `w35_fibration_fig.tex`,
  `w35_phases_fig.tex`, `check_v14_output.txt`
* `download/`: `instruments-paper-revised14.pdf`, `WAVE35_FIGURES_AND_READINGS.md`
