# Worklog — Task 15: the true base U₃ and its fold-wall stratification

**Project:** δ₂(qutrit) ∈ {4/3, 1}, decided by H₂(B₃), B₃ := Fl₃/⟨c⟩,
Fl₃ = U(3)/T³, c = cyclic column shift (free order-3).
H₂(B₃) = coker(d₃ : ℤ/3 → ℤ/3);  **= ℤ/3 ⟺ δ₂ = 4/3 ; = 0 ⟺ δ₂ = 1.**

**Status (unchanged): δ₂(qutrit) = 4/3 is OPEN.**
This task does **not** close it. It delivers the piece that was flagged as the
*genuinely new work*: a verified, self-consistent model of the true base
U₃ (the unistochastic region) and of the fold-wall arrangement on its boundary,
computed from first principles (no dependency on the prior session's repo,
which is **not present on this machine**).

Honest note on environment: this is a fresh sandbox containing only the
`glm internal.txt` thinking dump. There is **no worklog, no scripts directory,
no GitHub repo** on disk here, so the previously-"proven" equivariant-CW + SNF
machine could not be loaded and re-run. Everything below was rebuilt and
verified in `./u3_lab/`. The final equivariant H₂ computation therefore
remains the *next* task; its exact prerequisites are spelled out at the end.

---

## 1. Notation & the exact moduli map

Rows are indexed i, columns j. D_ij = |U_ij|². A 3×3 doubly-stochastic matrix
is the set B₃ (the Birkhoff polytope, a 4-D polytope).

The map is realised by the standard CKM-type 4-parameter family
(θ₁₂, θ₂₃, θ₁₃, p=cos δ). Its 9 moduli (exact, verified self-consistent:
refit of sampled interior points to ~1e-15):

|V₁₁|²=c₁₂²c₁₃², |V₁₂|²=s₁₂²c₁₃², |V₁₃|²=s₁₃²,
|V₂₃|²=s₂₃²c₁₃², |V₃₃|²=c₂₃²c₁₃²,  (p-independent)
and four p-linear entries (rows 2,3 cols 1,2), e.g.
|V₂₁|² = s₁₂²c₂₃² + c₁₂²s₂₃²s₁₃² − 2 c₁₂s₁₂c₂₃s₂₃s₁₃·p, etc.

This is an exact parametrization of U₃ = image{moduli of 3×3 unitaries}.

## 2. Characterization of U₃ (verified)

For each row pair (i,j) the three numbers
   √(D_i1 D_j1), √(D_i2 D_j2), √(D_i3 D_j3)
must form a (possibly degenerate) triangle: largest ≤ sum of the other two.

**Forward (necessary) — verified:** 300 000 random (Haar) unitaries *never*
leave this region (minimum row-pair slack ≈ 4×10⁻¹² ≈ 0). U₃ ⊆ region.

**Reverse (sufficiency, U₃ ⊇ region) — verified:** doubly-stochastic points
satisfying all three row-pair triangle inequalities, sampled deep *and* down to
wall-adjacent (row-pair slack from ~8×10⁻² down to ~5×10⁻⁵), all reconstruct to a
unitary at residual ~1e-16. Points violating an inequality fail to unitarize
(residual floor scales with boundary distance), confirming the boundary is the
equality locus.

**Conclusion.** U₃ = {D ∈ B₃ : each row-pair product-triple is a (possibly
degenerate) triangle}. It is the *closure* of its 4-D interior; the interior is
the region of strict inequalities.

## 3. U₃ ∩ (Birkhoff face lattice) — verified (probe_boundary.py)

| Feature of ∂B₃ | # | In Ū₃? |
|---|---|---|
| permutation vertices | 6 | YES (resid ~1e-30) |
| **transposition edges** | 9 | YES — *every* interior point (all 8 samples ~1e-16) |
| 6-cycle edges | 6 | **NO** — every interior point ~0.23 (out) |
| triangular 2-face interiors | 18 | NO (slack −1/3, out) |

So Ū₃ ∩ ∂B₃ = the 6 vertices plus the **9 transposition edges**; the 6-cycle
edges and all triangular 2-faces are *outside* U₃. (This matches the fibre facts
in the prior session and justifies that the older "full-Birkhoff" cell model
contained fictional cells over empty-fibre faces.)

## 4. The 9 fold walls and their incidence (walls.py, walls2.py)

Index the walls W(i,j|k): row pair i<j, "hypotenuse" product-column k, i.e.
g(D) := [√(D_i,l D_j,l) + √(D_i,m D_j,m)] − √(D_i,k D_j,k) = 0, {k,l,m} = {1,2,3}.

**Observed incidence along the Birkhoff 1-skeleton:**

* All 6 vertices lie in **all 9** walls (full coincidence at every vertex).
* Every transposition edge lies in exactly **8** of the 9 walls. The one wall it
  is *not* in is tabulated below.

| transposition edge | wall NOT containing it |
|---|---|
| 123–132 | W(2,3\|1) |
| 123–213 | W(1,2\|3) |
| 123–321 | W(1,3\|2) |
| 132–231 | W(1,3\|3) |
| 132–312 | W(1,2\|2) |
| 213–231 | W(2,3\|2) |
| 213–312 | W(1,3\|1) |
| 231–321 | W(1,2\|1) |
| 312–321 | W(2,3\|3) |

**Pairwise wall ∩ wall in the interior of B₃ (walls2.py):** not all pairs meet
only on the boundary. Examples that possess a genuine codimension-2 (2-D)
double-degeneracy locus *inside* int B₃:
   W(1,2|1) ∩ W(2,3|3),  W(1,3|2) ∩ W(2,3|1)  (residual → ~0 in int B₃).
Others (e.g. same row-pair, different hypotenuse; W(1,2|1)∩W(1,2|2)) only meet
on the boundary/vertices (residual stays ~1e-3 in int B₃).

**Structural remark:** the wall system is *not* the simple "9 cleanly
incident curved disks" suggested by the idealised picture. All walls share the
6 vertices; each edge is common to 8 walls; and walls meet pairwise along
real interior 2-loci in a pattern that depends on (row-pair × hypotenuse).
This degeneracy is the true content of "the wall-arrangement incidences" and is
the combinatorial input a correct cell model must reflect. Any equivariant-cell
rebuild must therefore subdivide U₃ by the *tightness pattern* (which of the 9
inequalities are equalities) intersected with the 1-skeleton data above — not by
a fictitious clean-9-wall picture.

## 5. What this delivers / what it does not

**Delivered (all reproduced & machine-verified this session):**
* exact 4-parameter moduli model of U₃;
* clean characterization of U₃ (region of row-pair triangle inequalities);
* verified 1-skeleton membership (9 transposition edges in, 6-cycle edges &
  2-face interiors out);
* wall-indexing, edge-in-8-walls incidence table, and the presence of genuine
  interior wall∩wall 2-loci.

**Not delivered (still OPEN):** the number δ₂(qutrit). The decisive step needs
the full equivariant-CW construction of Fl₃ over this true base plus the
validated fibre-cell gates and SNF reduction that lived in the prior repo —
none of which is on this machine, and which cannot be responsibly re-derived in
one session. The branch/sheet structure (degree/2-sheet question) also needs the
full fibre model and is *not* settled here.

## 6. Files

`./u3_lab/`
* `moduli.py` — exact CKM moduli map + fit-back membership oracle.
* `explore1–4.py` — characterization checks (forward/backward, properness).
* `probe_boundary.py` — vertices/edge membership in Ū₃.
* `proper.py`, `proper2.py` — interior & 2-face checks.
* `nearwall.py` — near-wall reachability + branch count.
* `walls.py`, `walls2.py` — wall incidence tables & pairwise intersections.
