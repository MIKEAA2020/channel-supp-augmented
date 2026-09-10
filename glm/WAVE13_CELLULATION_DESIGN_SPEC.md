# WAVE 13 — CELLULATION DESIGN SPEC for the corrected base Ū₃
### (the equivariant-cell build that would close δ₂(qutrit))

**Object.** A C₃-equivariant CW/chain model of Fl₃ = U(3)/T³ over the true base
Ū₃ (unistochastic region), designed so that after the Wave‑11 battery and the
orbit‑complex Smith normal form, H₂(B₃) reads the qutrit bit:
> H₂(B₃) = ℤ/3  ⟺  CLSS d₃ = 0  ⟺  **δ₂(D(ℂ³)) = 4/3**  (World 1)
> H₂(B₃) = 0    ⟺  obstruction dies                            (World 2)

This is the **design spec**, for review. It is deliberately **not** a claimed
execution: every quantity that must be derived (local near‑∂B₃ models, exact
orientation degrees on curved walls, proof that Ū₃ is a 4‑ball, boundary
matching) is boxed as an open item, with the route to verify it. Manifold-level
facts marked **[V]** are machine‑verified in Waves 11–13.

---

## 0. Conventions

* Rows `i`, columns `j`; D_ij = |U_ij|². B₃ = Birkhoff 3×3 (4‑D polytope,
  f = (6,15,18,9,1), all faces simplices).
* U₃ = image of π: Fl₃ → B₃; **[V]** U₃ = {D ∈ B₃ : every row‑pair
  (i,j) product‑triple (√DᵢₖDⱼₖ)ₖ is a possibly‑degenerate triangle}.
* c = right‑mult by the cyclic permutation P_σ (σ = (123) on columns): free
  order‑3 on Fl₃; on B₃ it is the **cyclic column shift** D ↦ (D with columns
  σ‑cycled), hence on the wall labels it **rotates the hypotenuse index** k and
  fixes each row‑pair.
* Flat point D_f = (1/3)·(all ones) ∈ int U₃ **[V]** is the **unique** c‑fixed
  base point; it is the Fourier/Hadamard moduli, and c acts there by the fibre
  translation t₀ (exact identity F₀P_σ = diag(1,ω,ω²)F₀). **Freeness is carried
  by the fibre over D_f, never by the base point.**
* Fibres **[V]**: T² = T³/centre over every point of U₃ ∩ int B₃ (incl. walls,
  corners, triples, facet‑equality loci); S¹ over the 9 transposition edges;
  pt over the 6 vertices; empty over everything outside U₃.

---

## 1. The base Ū₃ as a 4‑ball and its boundary strata

**Working hypothesis (open item H‑top):** Ū₃ is a topological 4‑ball, i.e. there
is a single top cell `int Ū₃`, and ∂Ū₃ is a 3‑sphere with the cell
decomposition below. *(Verify: Ū₃ convex? — no, non‑convex since √‑inequalities.
Show contractible + collared; or prove the boundary is S³ by the gluing of §1.2.
This is prerequisite but I expect it to hold; the region is a "cornered ball".)*

### 1.1 Boundary strata and fibre types

| label | stratum | dim | fibre | # | c‑orbits [#] |
|---|---|---|---|---|---|
| V | 6 permutation vertices | 0 | pt | 6 | 2 × 3 |
| T | 6 triple points (3 walls) | 0 | T² | 6 | 2 × 3 |
| E | 9 transposition edges | 1 | S¹ | 9 | 3 × 3 |
| W | 9 fold‑walls W(i,j\|k) | 3 | T² | 9 | 3 × 3 |
| C | 18 corner 2‑loci (2 walls) | 2 | T² | 18 | 6 × 3 |
| F | facet‑equality 2‑loci (on ∂B₃) | 2 | T² | ≥9 **[V]** each facet has a 2‑dim feasible locus | *to census* |
| P | the flat point D_f ∈ int Ū₃ | 0 | T² | 1 | **c‑fixed** |

Incidence facts **[V]** (Waves 11–13):
* every vertex V ∈ **all 9** walls W and all 9 facet‑loci;
* every transposition edge E lies in **8 of the 9** walls (missing‑wall table,
  Wave 12) and is shared by several corners C and facet‑loci F;
* a wall pair W(i,j|k), W(a,b|c) meets in a **genuine interior 2‑locus C**
  ⟺ they differ in **both** row‑pair and hypotenuse (**rook rule**); 18 such C;
* three walls meet at an interior point T ⟺ the three hypotenuse columns are a
  bijection onto the three row‑pairs; **6** such T;
* facet relints are unistochastic only on a codim‑1 equality locus **[V]**.

### 1.2 Structural statement for the cellulation (open item H‑glue)

∂Ū₃ is assembled from two parts that meet along the 1‑skeleton:
* **Part A — the fold‑wall system** (all of it in int B₃, fibre T²): the
  hypersurface bounding U₃∩int B₃, decomposed into the 9 wall 3‑cells W,
  18 corner 2‑cells C, 6 triple 0‑cells T, glued so that C = W∩W′ and
  T = W∩W′∩W″.
* **Part B — the Birkhoff‑boundary part** (∂B₃ ∩ Ū₃): the 6 vertices V, the 9
  transposition edges E, and the facet‑equality 2‑loci F.
Part A and Part B share exactly V ∪ E. Walls do **not** extend to ∂B₃ through
int B₃ except by limiting onto the 1‑skeleton V ∪ E (each E ⊂ 8 walls, each
V ⊂ all 9). *(Verify: every wall 3‑cell has boundary = union of some corner
2‑cells C and some transposition edges E, with the induced degree/gluing; the
18 corners each limit onto 7 of the 9 E — Wave 13 probe. Produce the exact
incidence poset numerically and certify d²=0 for the base sub‑complex alone.)*

**Why the fine matching matters (and why Wave 11 failed):** the previous 1896
build placed T² fibres over the 6‑cycle edges and 18 triangles, which carry
*empty* fibres; here every base cell has the fibre type recorded in §1.1, and the
top cell is Ū₃ (whose boundary is the wall system), not B₃.

---

## 2. The fibre cellulations (reused from Wave 11, **[V]**)

* **pt**: 1 cell.
* **S¹**: 3 vertices + 3 arcs = 6 cells (the "level‑3" 1‑cellulation of S¹).
* **T²**: 9+27+18 = 54 cells — the 3×3 grid (u,v) ∈ {0,⅓,⅔}² with circle
  families {u = a}, {v = b}, {u+v = c} at thirds; (u,v) = (arg z₂/z₁, arg z₃/z₂).
* c acts on a T² fibre over a fixed base point with the **t₀‑translation**
  t₀ = (⅓,⅓) (permutes the 54 cells, no fixed cell). **[V]**

These are exactly the certified level‑3 structures from `wave11_honest_fl3.py`.

---

## 3. Base cellulation and cell census

**Design rule.** Subdivide each stratum into open cells with constant fibre type,
matching the c‑orbits, so the base is a c‑equivariant regular CW structure of the
4‑ball with the *single top cell* int Ū₃.

Proposed count (to be locked by the H‑glue derivation):

| dim | cells | comment |
|---|---|---|
| 0 | V:6, T:6, + P:1 (+ any added vertices) | fibre pt/T² |
| 1 | E:9 (+ skeleton arcs) | S¹ fibre |
| 2 | C:18, F: ≥9 (+ any required subdivision of walls/corners) | T² fibre |
| 3 | W:9 (each a curved 3‑cell) | T² fibre |
| 4 | int Ū₃ : 1 | T² fibre |

*(The precise 1‑ and 2‑skeleton of ∂Ū₃, i.e. how C and F subdivide and meet
V, E, T, is the single genuinely open combinatorial input; §H‑glue.)*

**Freeness analysis.** c fixes only P (base). Every other base cell lies in a free
c‑orbit of size 3 (census §1.1). A total cell = (base cell) × (fibre cell) is
moved by T = (c on base) ∘ (t₀/permutation on fibre). Cells with c‑fixed base
(= those over P) are moved by t₀ on the fibre and are free **iff** t₀ acts freely
on the level‑3 T² cells **[V]**: the 54‑cell T² is cycled by t₀ with no fixed
cell, so no total cell is fixed. This is the mechanism Wave 11 used, and it
carries over verbatim.

---

## 4. The boundary operator d (assembly)

Following Wave 11 exactly, with the base ∂ now the corrected poset:
> d = (base boundary part) ⊗ 1  +  (−1)^{dim(base cell)} · (1 ⊗ fibre boundary).

* **Base part.** For a base cell σ of ∂‑dimension r, ∂_base σ = Σ over cells in
  its closure (from §1.2 incidence) of ±1·τ, where the **sign** is the relative
  orientation computed from the boundary orientation of the 4‑ball / the
  fold‑wall system.
* **Fibre part.** Reuse the level‑3 fibre boundaries (T², S¹ as in Wave 11).

**Open item H‑signs.** The ±1 geometric orientation degrees on the *curved* wall
3‑cells, corner 2‑cells, and their meeting with E/F/V must be *derived*, not
assumed. Recommended route: (i) triangulate each wall/corner by pulling back a
triangulation of its domain of parameters (each wall is a graph over 2–3 of the
D‑coordinates after the equality is solved); (ii) compute the orientation of each
incident face by the sign of the Jacobian / by the simplex‑facet convention used
in `wave11_honest_fl3.py` (ε_Φ = s(Φ)·σ‑consistent); (iii) certify by d² = 0 on
the base complex alone (see §6, gate G0).

---

## 5. The c‑action T and the t₀‑twist/transition layer

* **T on cells.** T(base cell, fibre cell) = ( c(base cell), c‑image on fibre ),
  where c on the base permutes columns (hypotenuse rotation) per the orbit tables
  (§1.1), with a **sign** s(·) = the parity of the relabelling (as in Wave 11,
  s(interior) = +1 verified by the σ‑map on the affine 4‑space). On the fibre the
  action is the t₀‑translation over c‑fixed base points and a cellular
  permutation over the others.
* **The flat point / t₀ layer.** The unique c‑fixed base point P = D_f carries a
  full T² fibre (54 cells). To make the total action free, the fibre action over P
  is the **t₀‑translation** (order 3, free on the 54 cells). This is the content
  of the exact identity F₀P_σ = diag(1,ω,ω²)F₀ **[V]**.
* **Transition cocycle τ.** Wave 11 defined the *unique* c‑equivariant transition
  layer
  > τ_{σ→τ} = q_τ( (p(σ)−p(τ))·t₀ ),
  where p: base cells → ℤ/3 is the c‑orbit phase and q_τ the canonical fibre
  quotient. It is a coboundary (contractible base, top cell int Ū₃), so the only
  twist is the t₀‑monodromy [g, g−t₀, g+t₀] around the interior/fixed base. This
  transfers verbatim to the corrected base because the top cell is again a single
  c‑invariant 4‑cell containing the fixed point P. **[re‑verify in the new base]**

---

## 6. Verification battery (identical to Wave 11)

| gate | check |
|---|---|
| G0 | base sub‑complex: d² = 0 (its own boundary operator), consistent Euler for the 4‑ball |
| G1 | total cell counts per degree, χ = 6 |
| G2 | d² = 0 exactly (full complex) |
| G3 | H(Fl₃) = (ℤ,0,ℤ²,0,ℤ²,0,ℤ), incl. mod‑p torsion audit p ∈ {2,3,5,7,11,13} |
| G4 | T³ = I; G5 dT = Td exactly; G6 c free on all cells; G7 1+T+T² = 0 on H₂, T order 3 there; G8 T = +1 on H₆ |
| G9 | **orbit complex** C(Fl₃) ⊗_{ℤ[C₃]} ℤ → SNF (sympy) → H(B₃); mandatory H₀=ℤ, H₁=ℤ/3, H₅=0, H₆=ℤ; **THE BIT: H₂(B₃)=ℤ/3 ⇔ δ₂=4/3** |

The G1–G8 checks certify the *machinery*; G9 alone reads the number. G9 is only
meaningful if G1–G8 pass on the *correct* base (the 1896 build passed G1–G8 on the
wrong space and correctly refused G9).

---

## 7. Reading the bit

* If the orbit complex passes the mandatory slots and H₂(B₃) = **ℤ/3** ⇒ World 1:
  the CLSS transgression d₃ = 0 ⇒ **δ₂(qutrit) = 4/3**.
* If H₂(B₃) = **0** ⇒ World 2: the obstruction dies, δ₂(qutrit) = 1.
Either result is a closed, battery‑certified answer.

---

## 8. Open items to derive & verify (the review checklist)

1. **H‑top:** prove Ū₃ is a 4‑ball and ∂Ū₃ = S³ with the §1 cell decomposition
   (or exhibit the correct replacement).
2. **H‑glue:** the exact base poset of the corrected base — how the 9 wall 3‑cells
   W, 18 corners C, 6 triples T meet each other and the 1‑skeleton V∪E, and how
   the facet‑equality 2‑loci F subdivide and attach. Numerically pinned in Wave 13
   (each C incident to 7 E; each E ⊂ 8 W; every V ⊂ 9 W) but needs exact,
   d²=0‑certified articulation (G0).
3. **H‑signs:** geometric ±1 orientation degrees on the curved walls/corners and
   their incidence with E/F/V (route: parameter‑pullback triangulation, §4).
4. **H‑facet:** exact description + c‑orbit census of the 9 facet‑equality 2‑loci F
   (dimension 2 confirmed; explicit equations and fibre‑type T² to be written down).
5. **H‑twist:** re‑certify the t₀‑transition layer §5 against the new base.
6. Then execute G1–G9.

**Expected scale.** The corrected base has ~40–70 base cells (not the 49‑face
lattice); × level‑3 fibres gives on the order of a few thousand total cells —
comfortably within the exact‑arithmetic machinery already proven in
`wave11_honest_fl3.py` (which handled 1896 cells and 8262 boundary entries).

---

## 9. Files

* `wave13_cell_data.py` — corner↔edge incidence (each corner incident to 7 E).
* `wave13_orbits_topo.py` — base c‑orbit census (V:2, W:3, E:3, C:6, T:2 orbits, all ×3; P fixed).
* `wave13_facets.py` — facet‑equality 2‑loci ([V] 2‑dim, on ∂B₃).
* Prior: `wave12_wall_incidence.py`, `wave12_corner_rule.py`, `wave12_interiority.py`, `wave12_u3_base/*`.

**Status.** δ₂(qutrit) = 4/3 remains **open**. This spec is the reviewed‑before‑execution
blueprint for the build that closes it; the design is coherent and every
geometric fact it leans on is either verified or explicitly boxed for derivation.


---

## §8-bis  Wave 14 outcome (added after the fact)

The four open items of §8 are resolved in `WAVE14H_RESOLUTION.md`, and two claims of this spec
are **retracted** there:

* the census `dim2:9 (facet loci F_ab)` and the "18 interior corner 2-loci / 6 interior triple
  points" corner rule — both presupposed several independent walls, but `Q12 = Q13 = Q23`, and
  in fact `Q < 0` on every facet off its four transposition edges, so there are **no 2-cells**;
* the fibre-count check of `chi(Fl3) = 6` built on that census — to be recomputed.

Corrected base data: `f-vector(B3) = (6,15,18,9)`; `Q ≡ 0` on the 9 transposition edges,
`Q_min = -1/16` on the 6 cyclic edges; `chi(U3) = 1` (n = 24,32,40), `chi(dU3) = 0`,
one hole component, wall = 6 open 3-manifolds indexed by the hypotenuse bijection
`sigma in S3` (2 c-orbits of 3), every vertex in the closure of exactly 2 of them.
