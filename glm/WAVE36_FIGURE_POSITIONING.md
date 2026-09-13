# Wave 36 — The two figure-positioning repairs (v15 / v12)

**Directive** (user, 2026-09-14): (1) instruments paper, Figure 2 — the
`U(3) → U(3)` (the annotation `classifies U(3) → U(3)/K`) superimposed on a
curved arrow; move it into whitespace while remaining adjacent to the arrow it
describes. (2) main article, Figure 2 — the lowest box superimposed/crossed
the arrow to its right; move the box down just enough to clear the crossing,
staying above/outside the contents of the box. (3) journal-fit study (answered
in conversation; see the session log).

Scope: **pure positioning** — two node coordinates and one arrow route. No
text, caption, label, or claim content changed anywhere; the no-new-claims
gate holds trivially. Instruments v14 → **v15**; main v11 → **v12**; both in
`manuscript uploads v15/`.

---

## Defect 1 (instruments, `fig:flag-fibration`, page 36)

**Measurement** (300-dpi render, red-overlay curve trace, calibration from
the curve endpoints): the γ arrow sweeps from (9.1, 0.05) through a belly at
y ≈ −1.5..−1.66 (x ≈ 5..6.5) to (0.62, −0.02). The annotation, centred
(4.1, −1.42) with ink bbox 34.4 mm × 5.8 mm, overlapped the shaft diagonally:
439 black curve pixels inside the label bbox, the curve crossing from
(3.37, −1.07) to (6.14, −1.68) — straight through the text.

**Repair design.** A rasterised free-placement search over every forbidden
region (the three curves dilated 1.2 mm, all black text dilated 0.8 mm, node
bboxes) for the 34.4 mm × 5.8 mm one-line label: **0 candidates below the γ
belly** — the corridor between the belly (above), the π curve and its
arrowhead (left, ending (3.4, −2.4)), the BC₃ node (below, top edge −2.48),
and the κ curve (right, x ≈ 6.7–7.0 at that height) is 7.7–9.0 mm tall
against 7.5 mm needed including margins, and 2.8 cm wide against the 3.44 cm
label — and **391 candidates above the curve**, in the band between the
Bι arrow and the γ belly. Validated centres: (5.0, −0.37)..(5.0, −0.47);
**(5.0, −0.42)** chosen (maximises the minimum clearance to the γ symbol
below and the Bι arrow above). The label now sits directly above the γ
symbol, which sits above the curve shaft — the label–symbol–curve stack
makes the association with γ unambiguous.

**Edit**: one line, `at (4.1,-1.42)` → `at (5.0,-0.42)`.

## Defect 2 (main, `fig:replacement-join`, page 15)

**Measurement** (300-dpi render + a `\pgfgetlastxy` debug build): the
flagged-space box grew to **73.1 mm wide** (text-driven, past its 56 mm
design minimum; east edge +36.6 mm), while the orthogonal-join arrow turned
at **+33.2 mm** (B.east + 5 mm) — inside the box's span — at height
**J.north = −42.6 mm**, 1.5 mm *below* the box's top edge (−41.1 mm),
because the S^R circle is positioned on the box's centreline. Both segments
cut the box's top-right region: the vertical shaft crossed the top edge and
ran 1.5 mm into the interior; the horizontal run passed through the
box's top-right interior for 3.4 mm before exiting the east edge. The
crossing is **translation-invariant**: moving the box drags S, S^R, and the
balanced-partitions note with it (all relative placements), hence drags
J.north and the turning height — the overlap survives any pure translation.

**Repair design** (twofold, the directed box-move plus the root-cause
reroute):
1. The box moves **down 3.5 mm** (as directed), from resolved centre
   (0, −50.3) to a deterministic `at (0,-53.8mm)` (the source's
   `below=5mm of B` + `at (0,-36mm)` combination had ambiguous resolution
   semantics; the new form is anchor-deterministic). The B-box gap widens
   16.2 → 19.9 mm.
2. The orthogonal-join arrow turns at **+12 mm** from B.east (+40.2 mm,
   3.6 mm clear of the box's 73.1 mm-wide east edge), so its shaft and
   horizontal run stay above and outside the box — the arrow no longer
   enters the box, keeping its path above the box's contents. The
   `orthogonal join` label rides above the horizontal run (pos 0.86),
   clear of the Rep box, the Perfect-separation text, and the S^R circle.

**Edits**: two lines (the FB node line; the orthogonal-join draw line).
The h_i arrow's designed termination at B₁'s corner inside the B box was
examined and deliberately left unchanged (it is the construction's
statement — the block sphere maps into the B₁ block — not a defect, and not
flagged).

---

## QA (the v13/v14 battery, pure-positioning variant)

- **P-layer** (`check_v15.py`): the three hunks present exactly once; the
  pure-positioning gate — unified diffs of exactly 2 lines (instruments)
  and 8 lines (main) versus v14/v11, every changed line a coordinate or a
  source comment; `.txt == .tex` for both papers; both figure captions
  byte-identical; labels unique; no undefined references; the informal
  register sweep clean (precise W34-style needles); page counts 53 / 46.
  **30/30 PASS, exit 0.** Honest debug trail: six checker-needle bugs fixed
  in place before any conclusion (comment-line diff prefixes; a
  split-versus-index extraction bug in the caption comparison; two
  over-broad informal-register needles — "as recorded in the definition"
  and "the previous section" are legitimate prose; a pdftotext spacing
  needle — `U (3)` extracts with a space).
- **Compile QA**: tectonic exit 0 on both; 53 / 46 pages (unchanged); the
  number-free warning multisets **identical** to the fresh v14/v11
  baselines (26 / 54 warnings, every region pre-existing) — zero new
  typesetting defects.
- **R-layer**: pdftotext render needles pass (the γ annotation renders on
  page 36 — the page dump shows `classifies U (3) → U (3)/K` sitting above
  the `γ` symbol; the orthogonal-join label renders on page 15; the
  balanced-partitions note still renders, having moved with the box).
- **V-layer (visual, VLM on the final PDF pages)**: instruments p. 36 —
  the annotation overlaps nothing, in whitespace near the γ arrow,
  association unambiguous; main p. 15 — no arrow enters or crosses any
  box, the orthogonal-join arrow passes to the right of the wide lower box
  without touching it, its label clear of all elements. Also verified at
  the standalone-render stage before integration (both figures), and the
  geometry verified numerically (the only verticals inside the box's
  x-range are the box's own borders; the arrow shaft at +40.2 mm).
- **M-layer**: the Wave-31 derivation battery re-run: **ALL 12 GATES PASS**
  — the mathematics untouched (as the diff gate already implies: no
  mathematics was within three coordinate lines of the edit).

The verdict chain unchanged: x² ≠ 0; (ℤ, 0, ℤ/3, ℤ/3, ℤ/3, ℤ/3, ℤ);
H⁶(B;ℤ) = ℤ with the discriminant twice a generator; δ₂(D(ℂ³)) = 4/3;
ququart [4/3, 3/2] OPEN; the W23 stop stands.

## Artifacts

`edit_v15.py` (the anchored edit), `check_v15.py` + `check_v15_output.txt`
(the battery transcript), the standalone prototypes and red-overlay
measurements in `compile-test/w36/` (session workspace, not committed).
Deliverables: `manuscript uploads v15/` (instruments-paper-revised15 and
main-article-revised12, `.tex/.txt/.pdf`), the v15/v12 PDFs copied to the
download folder.
