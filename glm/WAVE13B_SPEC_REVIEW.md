# WAVE 13B — SPEC REVIEW (machine-verified) + CORRECTED DESIGN v2
### Review of `WAVE13_CELLULATION_DESIGN_SPEC.md` (commit 1c0cd1b), per the user directive:
### "review, evaluate, verify the spec. strengthen weaknesses or defects if applicable before running it."

**Verdict: the Wave-13 spec is geometrically sound in its machinery layers but
REFUTED in two structural places. Executing it as written would repeat the
Wave-11 failure mode (certified machinery on the wrong space): the G3
homology gate would fail, or worse. The corrected design (v2, §5 below)
replaces the base stratification and fibre typing; the Wave-11 equivariant
machinery (level-3 fibres, degeneration q-maps, t0-twist layer, battery,
orbit SNF) carries over verbatim. δ₂(qutrit) remains OPEN.**

All claims below are machine-verified in `wave13b_review_checks.py`
(transcript `wave13b_review_output.txt`) and `wave13b_census.py`
(transcript `wave13b_census_output.txt`).

---

## 1. Defect #1 (fatal): the interior fibre is 2×T², not T²

The spec's §0/§1.1/§3 table assigns fibre "T² = T³/centre" to *every* point of
U₃ ∩ int B₃, and §3 builds **one** top 4-cell `int Ū₃` with a T²-fibre.

**Fact [C3]:** the fibre of π: Fl₃ → U₃ over an interior point is **two
disjoint T²'s** — the two Jarlskog sheets, δ ↔ −δ. Machine: for 20/20 random
Haar points D, the CKM inversion yields |cos δ| < 1 with two branches δ₀, −δ₀
that both reconstruct D to 1e-12 with Jarlskog invariants J = ±J₀.
Theory: the (L,R)-rephasing orbits over D are separated by the invariant
J = Im(U₁₁U₂₂Ū₁₂Ū₂₁) = c₁s₁s₂c₂c₃²s₃·sin δ ≠ 0 on the interior, and
S_D = orbit(δ₀) ⊔ orbit(−δ₀).

Equivalently: the correct base of the T²-fibration Fl₃ → (4-dim base) is the
**moduli space M = Fl₃/T³_L = T³\U(3)/T³** (the "CKM moduli space"), and
M → U₃ is a **2-to-1 cover folded along the wall system**. The spec's single
top cell covers one sheet only — it builds HALF the space. (Euler
characteristic alone cannot catch this: both sheets carry χ = 0 fibres; the
G3 gate would.)

## 2. Defect #2 (fatal): the wall stratification ("rook corners", "6 triple points") is fictitious

The spec's §1.1/§1.2 stratifies ∂U₃ into 9 wall 3-cells W(i,j|k) whose pair
intersections are 18 "corner 2-loci" (rook rule) and 18 corner 2-cells plus 6
isolated triple points T, glued along a 1-skeleton V∪E (Wave-12b claims).

**Facts:**
* **[C2]** In the CKM domain (θ ∈ open cube, all 9 entries positive), *every*
  row-pair triangle degeneracy forces sin δ = 0: over 86 460 grid
  (θ,δ)-points, all 180 degenerate ones lie exactly at δ ∈ {0, π, 2π}
  (max distance 0.00e+00). Exact proof: the (ij)-triangle of |V|² is
  degenerate ⟺ the three vectors z_k = V̄_ik V_jk (with Σz_k = 0 by
  unitarity) are parallel; in the open cube z₁ ∥ z₃ forces sin δ = 0.
  **⟹ the walls of U₃ are exactly the real/orthostochastic locus; there are
  NO non-real "1-degenerate" wall points in int B₃. The "wall 3-cell
  interiors" of the spec (only one triangle degenerate) are empty.**
* **[C1]** Every real orthogonal O (all 30 trials) gives D = O² with **all
  three** triangles exactly degenerate (|slack| ≤ 1e-16) and hypotenuse
  columns forming a bijection — the orthostochastic locus is 3-dimensional
  and lies on three walls at once.
* **[C4]** At a real point the three wall-equation gradients on the 4-dim
  doubly-stochastic space are **parallel** (rank 1 of the 3×4 stack, 10/10
  trials): the three walls are mutually tangent along the 3-dim real locus.
  Pairwise wall intersections are **3-dim open overlaps**, not 2-loci; triple
  intersections are **3-dim regions**, not 6 points.
* **[C6]** A Wave-12b-style "corner" solution of W(12|1)∩W(13|2) (found by
  their own method: Nelder-Mead on squared residuals) lies on the third wall
  E(23|3) = 0 at 1e-16 and moves in a 3-parameter θ-family (172/200 random
  |Δθ|~0.02 perturbations stay on all three walls).

**Methodology audit of Wave 12b** (`wave12_corner_rule.py`,
`wave13_cell_data.py`): their verification checks *existence of approximate
solutions* of the wall equations (Nelder-Mead, acceptance 1e-6 on squared
residuals), never the *dimension* of the solution loci and never the
strictness of the remaining triangle inequalities. All their "corner" and
"triple" solutions are points of the real locus — consistent with their
own raw data, mis-interpreted. The edge-incidence data ("each edge in 8/9
walls") is correct and is consistent with the corrected picture (verified:
at an edge the row-pair m-triples are trivially degenerate for all walls
except the one whose hypotenuse is a zero column-pair). The Wave-12a
characterization of U₃ by the 9 inequalities is correct and is retained.

## 3. The corrected geometry (all machine-verified)

* **U₃** = {D ∈ B₃ : all row-pair triangles (possibly degenerate)} — the
  Wave-12a characterization, retained.
* **Interior** (all triangles strict): fibre = **2×T²** (two Jarlskog sheets
  J = ±J₀(D) > 0 / < 0).
* **∂U₃ = the orthostochastic locus** = the images of the two real sheets
  {δ=0} and {δ=π} of M. Over it the fibre is **one T²** (the fold). The wall
  equations carve the real locus into **6 bijection-pattern regions**
  R(a,b,c) = {real D : (h₁₂,h₁₃,h₂₃) = (a,b,c) a bijection}, 3 per real
  sheet [census (A)]:
  δ=0: R(123), R(132), R(321);  δ=π: R(213), R(231), R(312).
  Each wall W(i,j|k) = the union of exactly 2 R-regions [census (C)]:
  W(12|1)=R(123)∪R(132), W(12|2)=R(213)∪R(231), W(12|3)=R(321)∪R(312),
  W(13|1)=R(213)∪R(312), W(13|2)=R(123)∪R(321), W(13|3)=R(132)∪R(231),
  W(23|1)=R(321)∪R(231), W(23|2)=R(132)∪R(312), W(23|3)=R(123)∪R(213).
* **∂B₃ strata**: 9 F-loci (2-dim, fibre T², ONE M-class each — the δ is
  absorbed by (L,R)-rephasing on 8-nonzero supports): 5 *pure* (θ-faces:
  D₁₂, D₁₃, D₂₃, D₁₁, D₃₃ = 0) + 4 *mixed* (cancellation loci inside the
  real sheets: D₂₂, D₃₁ = 0 at δ=0; D₂₁, D₃₂ = 0 at δ=π) [census (D)];
  9 transposition edges (fibre S¹); 6 vertices (fibre pt). χ(Fl₃) = 6 all
  from the point fibres — unchanged.
* **c-action on M [C5, census (B)]**: J(UP_σ) = J(U) exactly (max
  |Δ| = 3.5e-17 over Haar samples) ⟹ **c preserves each Jarlskog sheet**;
  the two 4-cells are individually c-invariant. On the 6 R-regions c acts
  freely in **2 orbits of 3**:
  (d0,123)→(d1,231)→(d1,312)→(d0,123);
  (d0,132)→(d1,213)→(d0,321)→(d0,132).
* **c-fixed points**: exactly TWO M-classes lie over the flat point D_f
  (all-1/3): [F₀] (J>0, sheet₊) and [F̄₀] (J<0, sheet₋); both are c-fixed
  (F₀P_σ = t₀F₀, F̄₀P_σ = t̄₀F̄₀, exact cyclotomic identity, Wave 10).
  Freeness is carried by the fibres: c = translation by t₀ (resp. t₀²) on
  the T³_L/centre fibre — free of order 3 on the level-3 54-cell T² (the
  Wave-11 mechanism, now TWICE, once per sheet).

## 4. Why the spec's other layers survive

* The linear c on the base (column cycling; hypotenuse rotation k↦σ(k))
  — retained: c remains the column cycling on U₃ ⊂ affine 4-space.
* The fibre cellulations (level-3: T² 54 cells, S¹ 6 cells, pt) — reused.
* The degeneration story T² → S¹ → pt at the ∂B₃ strati — retained (it
  happens ONLY at edges/vertices; F-loci keep full T² fibres: the
  stabilizer is the centre there — machine-checked in §3).
* The transition-cocycle / t₀-twist layer — re-derived on the new poset
  (the gauge is now pinned at TWO fixed points: τ = t₀ on sheet₊, t₀² on
  sheet₋; the unique-cocycle/contractible-base argument is unchanged).
* The battery G0–G9 and the orbit-SNF bit readout — unchanged.

## 5. Corrected design v2 — "the two-sheet book" (= cellulating M)

**Base cells (32):**

| dim | cells | fibre | c-orbits |
|---|---|---|---|
| 4 | 2 sheets s₊, s₋ (= the J>0 / J<0 halves of int U₃'s cover) | T² (54) | 2 fixed cells (fibre-only t₀-action) |
| 3 | 6 regions R(a,b,c) | T² (54) | 2 × 3, free |
| 2 | 9 F-loci (5 pure + 4 mixed) | T² (54) | 3 × 3, free (c: (i,j)↦(i,σ(j)) mixes pure/mixed) |
| 1 | 9 transposition edges | S¹ (6) | 3 × 3, free |
| 0 | 6 permutation vertices | pt | 2 × 3, free |

Total cells ≈ 6 + 27 + 108 + 324 + 486 + 405 + 162 = **1518** by degree
(0..6), χ = 6 — comfortably inside the demonstrated exact-arithmetic scale
(Wave 11 handled 1896 cells / 8262 boundary entries).

**Boundary structure (to be pinned by the build, then certified by G0):**
* ∂(edge) = its two permutation vertices (±1).
* ∂(F-locus) = the transposition edges on its facet (±1; the pure F's are
  θ-face squares whose 4 sides map to U₃-edges; the mixed F's are
  cancellation surfaces bounded by pure-F's and edges).
* ∂(R-region) = the pattern-flip loci (mixed F's) + cube faces (pure F's)
  + edges (±1).
* **The fold:** ∂s₊ = (δ=π sheet image) − (δ=0 sheet image) = Σ ±R;
  ∂s₋ = (δ=0 image) − (δ=π image): the two 4-cells glue to the SAME six
  R-cells with opposite arc orientations, so s₊+s₋ is a 4-cycle
  (χ(base) = 2, H₄(base) ⊇ ℤ — the expected base homology gate).

**T-map:** T(base cell, fibre cell) = (c(base cell), fibre action):
free orbit permutations on R/F/E/V; the two fixed 4-cells act by the t₀-/
t₀²-translation on the 54-cell T² (free); orientation signs = permutation
parity × fibre-map sign (the Wave-11 sign machinery); τ-cocycle = the t₀
phase gauge pinned at the two flat points.

**Battery (identical to Wave 11):** G0 base d²=0 + base homology (χ=2,
one 4-cycle); G1 counts/χ=6; G2 d²=0 exact; G3 H(Fl₃) = (ℤ,0,ℤ²,0,ℤ²,0,ℤ)
with mod-p audit; G4–G8 (T³=I, dT=Td, freeness, N=0 on H₂, T=+1 on H₆);
G9 orbit-complex SNF → **H₂(B₃) = ℤ/3 ⟺ δ₂(qutrit) = 4/3; H₂(B₃) = 0 ⟺ 1.**

## 6. Remaining derivation items (the honest open list for the build)

1. Pin ∂F and ∂R exactly (which edges/F-cells, ± degrees) numerically and
   certify d²=0 on the 32-cell base (G0).
2. Derive the fold signs on ∂s± (the arc orientation × the θ↦|V(θ,δ-sheet)|²
   Jacobian signs per R-region).
3. Re-certify the τ-cocycle on the new poset with the two pinned values
   (t₀ on sheet₊'s flat fibre, t₀² on sheet₋'s).
4. Execute G1–G9; read the bit.

**Status after this review:** δ₂(qutrit) = 4/3 remains OPEN. The Wave-13
spec must NOT be executed as written; the corrected v2 design above is the
reviewed-before-execution blueprint. The next session builds the 1518-cell
complex against this document.
