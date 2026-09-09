# WAVE 12 — THE TRUE BASE U₃: CHARACTERIZATION + FOLD-WALL ARRANGEMENT INCIDENCE

**Task.** Advance the recorded decisive route (Wave 11 §5, step 1) toward closing the
qutrit bit δ₂(D(ℂ³)) = 4/3: give a machine-verified, self-consistent description of the
unistochastic region U₃ ⊊ B₃ and of the incidence structure of its **9 curved fold-walls** —
the one piece Wave 11 flagged as genuinely new work and the prerequisite for cellulating U₃.

**Method.** Rebuilt from first principles in exact/near-exact arithmetic (Python ints,
`Fraction`s, numpy float feasibility with residual-floor arguments); *independent* of the
(now refuted) full-Birkhoff base. Artifacts in `glm/wave12_u3_base/` (turn-1 probe scripts)
and `glm/wave12_wall_incidence.py`, `wave12_corner_rule.py`, `wave12_interiority.py`.

Manuscripts untouched. δ₂(qutrit) **remains open**; this wave pins the base and its boundary
stratification so the orbit-SNF cellulation is a well-posed (not yet executed) build.

---

## 1. Exact moduli model of U₃ (`moduli.py`)

For a unitary U, D_ij = |U_ij|². The full 9-modulus set is the 4-parameter CKM-type family
(θ₁₂, θ₂₃, θ₁₃, p = cos δ); its closed-form entries are p-independent in the four entries
(11),(12),(13),(23),(33)-type positions and p-linear in the four "cross" positions. Refit of
sampled interior moduli to this family → ~1e-15: the family is an exact parametrization of U₃.

## 2. Characterization of U₃ (verified both directions)

> **U₃ = { D ∈ B₃ : for every row pair (i,j), the triple
> (√(D_i1 D_j1), √(D_i2 D_j2), √(D_i3 D_j3)) is a (possibly degenerate) triangle }.**

* **Forward (image ⊆ region).** 300 000 random (Haar) unitaries never leave the region;
  min row-pair slack ≈ 4×10⁻¹² ≈ 0.
* **Reverse (region ⊆ image).** Doubly-stochastic points satisfying all three row-pair
  triangle inequalities — sampled from deep interior down to wall-adjacent (row-pair slack
  from ~8×10⁻² to ~5×10⁻⁵) — all reconstruct to a unitary at residual ~1e-16.
  Points violating an inequality fail to unitarize (residual floor tracks boundary distance).
* U₃ = closure of its 4-D interior (near-wall 0⁺ points are reachable).

This is the exact feasibility condition of each row-pair's orthogonality constraint
Σ_k m_k e^{iα_k} = 0 (same origin as Wave 11 §3), now resolved in both directions.

## 3. U₃ ∩ (Birkhoff face lattice) — verified (`probe_boundary.py`)

| ∂B₃ feature | # | In Ū₃ ? |
|---|---|---|
| permutation vertices | 6 | YES (resid ~1e-30) |
| **transposition edges** | 9 | YES — every interior point (~1e-16) |
| 6-cycle edges | 6 | NO — every interior point ~0.23 |
| triangular 2-face interiors | 18 | NO (row-pair slack −1/3) |

So Ū₃ ∩ ∂B₃ = the 6 vertices plus the 9 transposition edges. The full-Birkhoff base of the
Wave-10/11 spec is therefore geometrically infeasible exactly as Wave 11 found, now with the
correct base characterized and its 1-skeleton verified.

## 4. The 9 fold walls (`walls.py`, `walls2.py`)

Index the walls W(i,j|k): row pair i<j, hypotenuse product-column k,
g_{ijk}(D) := √(D_ik D_jk) − √(D_il D_jl) − √(D_im D_jm) = 0. Because each √-term ≥ 0, the
equation forces column-k product to be the (co-)largest of the row-pair's three, so each of
the 9 walls is an honest codim-1 piece of ∂U₃ (not a spurious interior sub-locus).

**Incidence with the 1-skeleton (verified):**
* all 6 vertices lie in **all 9** walls (full coincidence at every vertex);
* every transposition edge lies in **8 of the 9** walls. The missing wall per edge:

| edge | missing wall | edge | missing wall |
|---|---|---|---|
| 123–132 | W(2,3\|1) | 213–231 | W(2,3\|2) |
| 123–213 | W(1,2\|3) | 213–312 | W(1,3\|1) |
| 123–321 | W(1,3\|2) | 231–321 | W(1,2\|1) |
| 132–231 | W(1,3\|3) | 312–321 | W(2,3\|3) |
| 132–312 | W(1,2\|2) | | |

## 5. Wall–wall incidence in the interior (NEW — `wave12_wall_incidence.py` etc.)

Regard the 9 walls as a 3×3 grid: row = row-pair index {12,13,23}, column = hypotenuse k.

**Corner rule (verified, exact strict-interiority test):** two walls meet along a genuine
**interior 2-dim corner of Ū₃** (all nine D entries bounded away from 0 and 1) iff they differ
in **both** the row-pair coordinate and the hypotenuse column (a "rook-nonattacking" pair).

* Exactly **18** such interior corner 2-loci (the 3×3 rook-nonattacking pairs).
* Wall pairs that share a row-pair index, or share the hypotenuse column, coincide only on the
  boundary of U₃ (i.e. on the transposition-edge/vertex skeleton) — no interior corner.

**Triple points (NEW):** three walls pass through a single interior point exactly when the
three hypotenuse columns {1,2,3} are assigned bijectively to the three row-pairs {12,13,23}.
There are **6** such interior triple points (one per permutation).  [e.g.
W(1,2|1) ∩ W(1,3|2) ∩ W(2,3|3), etc.]

**Boundary of Ū₃ (synthesis).** ∂Ū₃ is assembled from the 9 fold-walls (3-cells), glued along
the 18 corner 2-loci, meeting at the 6 triple points, and closing onto the Birkhoff boundary
through the 9 transposition edges (each an edge-type coincidence of 8 walls) and the 6
vertices. This is the tightness-pattern stratification a correct base cellulation must use —
a "wall-arrangement corner analysis", exactly the new work Wave 11 §5 flagged.

## 6. Status & next step

**This wave closes the base-characterization and boundary-stratification prerequisite.**
It does **not** yet output H₂(B₃) / the qutrit bit. The remaining (large, single) build is:
cellulate Ū₃ by this stratification, attach the level-3 fibre cellulations (S¹: 3+3, T²:
9+27+18) with the t₀-twist layer and geometric orientation signs, assemble the C₃-equivariant
chain complex of Fl₃, run the Wave-11 battery (d²=0, H(Fl₃)=(ℤ,0,ℤ²,0,ℤ²,0,ℤ), T³=I, dT=Td,
freeness, N=0 on H₂), then the orbit-complex SNF → H₂(B₃) = ℤ/3 (World 1, δ₂=4/3) or 0
(World 2). That build is recorded and not fabricated here.
