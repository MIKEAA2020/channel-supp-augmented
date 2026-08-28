# Independent Audit 2 — `supp/final.txt`

**File:** supp/final.txt (1456 lines, LaTeX-in-markdown)
**Date:** 2026-08-28 · **Independence:** `post gpt audit corrections/` was not consulted.

## Relationship to the other versions

`final.txt` is the pre-augmentation ancestor of `FINAL_JOINT_COMPLETE_AUGMENTED.txt`:
the two share the same skeleton, but `final.txt` lacks the later additions (operational
remark, 1/d_A corollary, observable-sphere join, monotonicity proposition, exact
collapse theorem, metric-complementarity corollary, decoder-hierarchy remark). It also
contains several defects that the augmented file fixed, plus one defect that the
augmented file *fixed but the underlying error persists in neither* — see P1-1.

## Verdict

Structurally the cleanest of the long versions: it contains **one outright false
claim**, an **abstract that contradicts its own degenerate-case remark**, a
**visually self-contradictory figure**, a **duplicated sentence**, and an
**editing relic in Table 1**. The core theorems (dimension, radii, replacement
profile, upper envelope, no-programming appendix) are otherwise sound; all constants
were recomputed independently and match (see README).

---

## Priority 1 — false claims

### P1-1 (L544–547, Section "Flagged replacement instruments") — false submultiplicativity claim
> "Moreover ‖Φ⊗id_{C_n}‖_⋄ ≤ ‖Φ‖_⋄ because id_{C_n} is CPTP and the diamond norm is
> submultiplicative under tensoring with a channel."

Two independent errors in one sentence:

1. **The inequality is false.** The diamond norm is *multiplicative* under tensor
   products: ‖Φ⊗Ψ‖_⋄ = ‖Φ‖_⋄·‖Ψ‖_⋄ (stability of the diamond norm), and
   ‖id_{C_n}‖_⋄ = 1, so the correct statement is **equality**:
   ‖Φ⊗id_{C_n}‖_⋄ = ‖Φ‖_⋄.
2. **Submultiplicativity is a property of composition**, not of tensoring:
   ‖Φ∘Ψ‖_⋄ ≤ ‖Φ‖_⋄‖Ψ‖_⋄. The sentence cites the wrong property for the wrong
   operation, and the inequality direction it states would in any case be useless for
   the isometry claim it is meant to support (one needs a *lower* bound on the flagged
   norm, which equality supplies).

The augmented version (L547–549) corrected this to the equality statement — so the
error is specific to `final.txt`.

### P1-2 (L51–53, abstract) — abstract contradicts the file's own degenerate-case remark
The abstract states, without qualification,
> "Around the uniform depolarising instrument I_*, the centred relative diamond radius
> is exactly ρ = 2/(nd_B·min{d_A,d_B})",

and similarly for R. But the file's own Remark (L448–450) says that for n=d_B=1 the
body is the singleton {Tr} and the centred relative in-radius is **+∞** by the
supremum convention. Evaluating the abstract's formula at n=d_B=1 gives ρ=2 — a
direct contradiction with L448–450. The augmented file fixed this by opening the
abstract with "Assume nd_B>1…; when n=d_B=1 … ρ=+∞, R=0" (L51–52 there).
**Fix:** prefix the abstract's radius statements with the nd_B>1 assumption and state
the singleton convention, as in the augmented version.

---

## Priority 2 — internal inconsistencies

### P2-1 (L1412 vs L1395–1403, figure) — annotation contradicts the plotted curve
The blue lower envelope is plotted at height **1 for 0≤r≤6** and at **0.25 for
7≤r<13** (comment at L1398 and coordinates at L1400–1403 confirm). Yet the annotation
node sits at **(axis cs:3, 0.6)** — inside the r≤6 plateau region — and is labelled
"β_r^{(n)} = 2/nd_B·s = 0.25". A reader sees a "0.25" label attached to the segment
whose value is 1. The corrected annotation (9.5, 0.45) appears in the augmented
version (L1410 there). **Fix:** move the node onto the 7≤r≤13 plateau, e.g.
(9.5, 0.45).

### P2-2 (L1386, figure) — ymax=1.7 clips the plotted upper curve
The red upper-envelope curve is drawn at **y=1.75** for 0≤r<12 (L1405), but the axis
declares `ymax=1.7` (L1386). The curve is clipped out of the plot area. The augmented
version changed ymax to 2.0. **Fix:** ymax≥1.9 (the augmented file's 2.0 works).

### P2-3 (L1284, proof of the orthogonal join) — duplicated definition sentence
> "Define u_i=y_i/‖y_i‖_2 when y_i≠0. Define H(y)=…"

The sentence "Define u_i=y_i/‖y_i‖_2 when y_i≠0." appears twice consecutively
(L1284): once as a display-stub line, then again embedded in the following line.
Compilation stutter; the definition of λ_i=‖y_i‖² is placed before the display but
the display shows nothing before "Define". Cosmetic-but-visible duplication.
**Fix:** keep one definition sentence (as in the augmented version's *intended*
text — note the augmented version instead *corrupted* this spot, see AUDIT-1 P1-4).

### P2-4 (L1344, Table 1) — editing relic "minus surjectivity"
The Origin column for the affine dimension reads:
> "n d_A² d_B² − d_A² **minus surjectivity** H ↦ H⊗I_{B₁}/b₁"

This is a leftover fragment of an editing note (an earlier draft evidently wrote
"minus [the surjectivity of]…"). In context the dimension *is* obtained *via* the
surjectivity of the marginal map, not "minus" it. The augmented version's table reads
"via surjectivity of the marginal map (X_1,…,X_n) ↦ Σ_k Tr_B X_k = H, e.g.
X_1=H⊗I_B/d_B" — correct. **Fix:** adopt that wording.

### P2-5 (L1437, figure caption) — phantom reference to "the main text"
> "The plot truncates at r=13 to parallel the qubit envelope in the main text (the
> main-text qubit envelope)…"

The parenthetical "(the main-text qubit envelope)" is a duplicated fragment, and the
reference to a "main text" is dangling — in this repo `final.txt` is a standalone
supplementary file. Same issue in the figure comment at L1398 ("as in main").
**Fix:** delete or replace with a self-contained justification.

---

## Priority 3 — notes and robustness

- **L202–236 (Instrument spectral bound):** stated as λ_max(−X) ≤ s‖Δ⃗‖/2d_A without
  the max{0,·} guard. This is nonetheless **valid**, because X is traceless
  (the direction constraint forces Tr X=0), hence λ_min(X)≤0 and
  λ_max(−X)=−λ_min(X)≥0; the proof's eigenvector step also runs through trivially
  when λ=0. The augmented version's max{0,·} formulation is cosmetic, not a fix of a
  real gap. (Independently verified — flagged here so it is not mis-reported as a flaw.)
- **L448–450 (degenerate case):** correct and consistent with the relative-ball
  definition (the ball around {Tr} with direction space {0} is contained in the body
  for every ρ, so the supremum is +∞). Good.
- **L528–530 (covering tightness):** the witness Φ is TP (trace of the second term
  compensates), and the maximally-entangled Schmidt-s input gives pure-vs-mixed trace
  distance 2(1−1/(nd_B·s)) — verified. Sound.
- **L544–547:** besides P1-1, the sentence "For any instrument I, its flagged channel
  Î is a channel, hence ‖Î‖_⋄=1" is fine (flagged diamond norm of a channel is 1).
- **L684–690:** the claim t_X=Tr X₊=Tr X₋>0 for nonzero traceless X is correct
  (X₊=0 would force X=−X₋≤0 with zero trace, hence X=0).
- **L909–930 (convex-projection/Helly):** sound; barycentre bound 2(m−1)/m≤R=2k/(k+1)
  holds for m≤k+1, and the "if F is also a member then m≤k" bookkeeping is right.
- **Appendix (no-programming):** the pure→mixed extremality step, the orthogonal
  supports step, the embedding/compactness divergence argument and the CPTP checks
  (Λ_j, R∘ι=id) are all correct as written.
- **LaTeX preamble:** `\diamondnorm`, `\diamondinst`, `\bm`, `\multirow`, `\dsfont`
  defined but unused; `\Lin`/`\Chan` used only in the appendix. Cosmetic.
- **Missing from this version (not errors, but deltas):** no monotonicity statement
  for α_r (the augmented version added one and got it wrong — see AUDIT-1 P1-2); no
  metric-complementarity corollary (so it avoids AUDIT-1 P1-1's chord claim); no 1/d_A
  bound; no exact-collapse theorem (it only has the inline nd_B·s=2 remark at
  L1226–1232, which is correct).

## Verified-correct highlights (for balance)

- All headline constants (D=28, ρ=0.25, R=1.75 for (2,2,2); Q_2(2)=2, r_out=12,
  r_in=14; exact gap 0.75 at r=0; collapse cases) recomputed and confirmed — see
  README for the full list.
- The degenerate-case remark, spectral lemma, covering tightness witness,
  replacement-profile Borsuk–Ulam argument, Helly decoder bound, pinching norms and
  the no-programming appendix are all sound.
