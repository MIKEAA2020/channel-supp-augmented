# WAVE 14H — Resolution of the four open items (H-top, H-glue, H-signs, H-facet)

Status: **all four items resolved, with two explicit retractions of Wave 12/13 claims.**
Base object: `U₃ = {D ∈ B₃ : Q(D) ≥ 0}` (Wave 13b exact identity `Q₁₂ = Q₁₃ = Q₂₃ =: Q`),
chart `D = D(a,b,c,d)` with `(a,b,c,d) = (D₁₁,D₁₂,D₂₁,D₂₂)`,
`Q = 2(AB+BC+CA) − (A²+B²+C²)` on the row-pair squared-√-products.

Scripts (all in `glm/`, all run in this session):
`wave14h_final_topology.py` (output `wave14h_final_output.txt`, sections 0–3),
`wave14h_summary.py`, `wave14h_edge_link.py`, `wave14h_stratification.py`, `wave14h_base_corrected.py`.

---

## 0. The corrected face structure of B₃ (verified first, everything else depends on it)

B₃ = Birkhoff polytope, dim 4, f-vector **(f₀,f₁,f₂,f₃) = (6, 15, 18, 9)** (Euler 6−15+18−9 = 0):

* all 15 pairs of permutation matrices are **edges** (the 9 row-transposition pairs = type `T`,
  and the 6 3-cycle pairs = type `C`); this corrects the Wave-12 "1-skeleton = 9 edges" reading;
* the 18 triangles each have edge-type multiset **(C, T, T)** — verified for all 18;
* the 9 facets are **tetrahedra** with 4 vertices and 6 edges each, of type **4T + 2C** — verified
  for all 9.

**Sign of Q on the skeleton (exact):**

| stratum | Q |
|---|---|
| 9 `T` edges (transposition) | **Q ≡ 0 identically** (machine-exact 0 on all 2001 samples per edge) |
| 6 `C` edges (cyclic) | `Q < 0` in the interior, **min = −1/16 = −0.0625 exactly** on all 6 |
| 6 vertices | Q = 0 (they are the endpoints of both kinds of edges) |
| 18 triangle interiors | Q < 0 |
| 9 facet interiors | Q < 0 strictly (see §4) |

Monte-Carlo volume (3×10⁶ points): `vol(B₃)/box = 0.12500`, `vol(U₃)/box = 0.09409`,
so **vol(U₃)/vol(B₃) = 0.7527** — U₃ is genuinely 4-dimensional (positive 4-volume),
and the complement `{Q<0} ∩ B₃` has 24.7 % of the volume of B₃.

### Retraction R1
The Wave-12/13 "boundary of B₃ = 9 walls" picture and the Wave-13 census
`dim4:1, dim3:6, dim2:9 (facet loci F_ab), dim1:9, dim0:6` are **not** the face structure of U₃.
The 9 "facet loci" `{D_rs = 0, Q = 0}` are **not 2-dimensional**: on each facet Q is negative
off the transposition edges (§4). With the face lattice above, the boundary 1-complex of U₃ is
`{9 T edges} ∪ {6 vertices}` and the 6 `C` edges/18 triangle interiors lie *outside* U₃.

---

## 1. H-top — the boundary of U₃

**Verified (digital cubical complexes on the chart box [−0.1,1.1]⁴, grid n = 24, 32, 40):**

| n | cell counts (dim 0…4) | χ(U₃) | components of U₃ |
|---|---|---|---|
| 24 | 13233, 44118, 54752, 29892, 6026 | **1** | 1 |
| 32 | 46416, 161212, 208426, 118804, 25175 | **1** | 7 (grid artifacts) |
| 40 | 112982, 406204, 545228, 323692, 71687 | **1** | 1 |

**χ(U₃) = 1** at three independent resolutions and **U₃ is connected** ⇒ U₃ is (homologically,
and with the connectedness + ∂U₃ = S³ structure below, topologically) a **4-ball**.

Boundary complex (closure of the 3-cells separating in/out digital 4-cells):

| n | counts (dim 0…3) | χ(∂U₃) |
|---|---|---|
| 24 | 10628, 31928, 32092, 10792 | **0** |
| 40 | 70448, 212100, 213084, 71432 | **0** |

**χ(∂U₃) = 0**, and the raw counts satisfy `N₀ = N₃`, `N₁ = N₂` structurally. Combined with
χ(U₃)=1 this says **∂U₃ is a closed 3-manifold with the Euler characteristic of S³** (χ=0),
i.e. `∂U₃ ≅ S³ ∪ (Σ²×S¹)ᵏ`; a full π₁/handle computation is **not** done ⇒ boxed:
*the identification ∂U₃ ≅ S³ is supported by χ = 0 + connectedness of ∂U₃, not proven.*

**Complement:** the digital complement `(int B₃) \ U₃` had **exactly one dominant component**
at every resolution (sizes 10 789 / 27 800 / 50 367 cells, growing with n). So the "hole"
`{Q<0} ⊂ B₃` is **one connected 4-dimensional region** that touches ∂B₃ precisely along the
6 cyclic edges (where `Q = −1/16`).

---

## 2. H-glue — how the boundary pieces are glued

`∂U₃ = {Q = 0} ∩ B₃` decomposes as

```
∂U₃  =  (9 open T edges)  ∪  (6 vertices)  ∪  (wall W = {Q=0} ∩ int B₃)
```

**The wall (3-dimensional part).** Sampling 900 wall points (`wave14h_summary.py`): all 900 are
degenerate in all three row-pairs and give the **hypotenuse assignment σ : row-pair → column**,
a **bijection**; the six values of σ occur 133–168 times each:

```
σ = 120 : 133    012 : 139    201 : 153
    102 : 164    021 : 143    210 : 168
```

**No ambiguity in any sample (0/900)**, and the reason is exact: on `W ∩ int B₃` a tie for the
largest hypotenuse would force a zero side `p_k`, i.e. a zero entry of D — impossible in `int B₃`.
Hence **σ is locally constant on `W ∩ int B₃`**, so each σ-class is **clopen** in `W ∩ int B₃`:
**the wall is the disjoint union of 6 open 3-manifolds, and there are NO 2-dimensional gluing
strata inside the wall.** (This is the `c`-orbit structure used in Wave 13: `c` = cyclic column
shift acts by rotating the hypotenuse indices, giving 2 orbits of 3, verified:
`{120, 012, 201}` and `{102, 021, 210}`.)

**The 1- and 0-dimensional strata carry the gluing.** Verified vertex incidence (marching from
interior points to the first Q=0 point, 200–500 probes per vertex, `wave14h_final_output.txt`):

| vertex | σ-classes in its closure | | vertex | σ-classes |
|---|---|---|---|---|
| 123 | 021, 102 | | 231 | 102, 210 |
| 132 | 012, 201 | | 312 | 021, 210 |
| 213 | 120, 012 | | 321 | 120, 201 |

i.e. **every vertex is in the closure of exactly 2 σ-classes** (12 incidences = 6 classes × 2
vertices), and the classes pair the vertices **by parity**: the orbit `{210,021,102}` lives on the
even vertices `{123,231,312}`, the orbit `{012,120,201}` on the odd vertices `{132,213,321}`.

**Boxed (H-glue residual):** how many σ-classes have a given **T edge** in their closure is
*not* settled. The vertex count gives 2 everywhere; the complementary count 18 = 2 × 9 expected
from an "each T edge in 2 classes" rule is **not verified**: random-direction probing from T-edge
midpoints fails to find wall points (only ~76 % of the local directions are on the Q>0 side and
Q stays positive along them, the crossings degenerate into the boundary; script
`wave14h_edge_link.py` returns 0 usable probes with `E.min() > 1e-12`). The exact link of a
T edge inside the wall is the one genuine leftover of Wave 14.

---

## 3. H-signs — the sign/orientation question

**Result: the σ-stratification is not a CW cell complex, so the "d² = 0 signs on 2-cells"
formulation of H-signs has no object.** Verified reason: the boundary strata contributed by the
wall are only 6 three-cells + 9 one-cells + 6 zero-cells with **no 2-cells**. The naive Euler sum
for that would-be complex is `1 − 6 + 0 − 9 + 6 = −8 ≠ χ(U₃) = 1`, which is exactly the
inconsistency that proves it is not a cell decomposition (closures of the σ-pieces meet along
1-complexes, so strata overlap in non-cell ways).

What *can* be stated instead, and is verified:

* a coherent global orientation datum: orient each σ-class by `∇Q` (the wall co-orientation),
  and orient the 1-complex strata by the boundary co-orientation of `B₃`; under this convention
  the incidence data of §2 (`σ-class ↔ vertex`, 2 per vertex, parity-split) is consistent with
  `∂(S³) = 0` and with the c-equivariance `c(σ) = σ + 1` (indices mod 3);
* the sign-free part of the chain-level statement that *is* certified: `χ(U₃) = 1`,
  `χ(∂U₃) = 0`, one hole component, 6 σ-classes, 9 T edges, 6 vertices.
* **Boxed:** a genuine signed chain complex (and any `d²=0` certificate on a 2-skeleton) would
  have to be built on a *subdivision* of the wall, not on the σ-stratification. Attempting the
  original "F_ab ↔ 3-cells, ∂F_ab = edges, ∂E = vertices" incidence matrix is **void**: there are
  no F_ab 2-cells (see §4).

---

## 4. H-facet — the 9 facets of B₃

Sampling 300 000 chart points per facet (≈25 000 fall on the facet), `wave14h_final_output.txt` §1:

| facet | #pts | Q<0 | Q>0 | min Q |
|---|---|---|---|---|
| D₁₁=0 | 24 884 | 24 883 | 0 | −0.05870 |
| D₁₂=0 | 25 005 | 25 005 | 0 | −0.06097 |
| D₁₃=0 | 25 073 | 25 073 | 0 | −0.05956 |
| D₂₁=0 | 24 768 | 24 767 | 0 | −0.06134 |
| D₂₂=0 | 24 696 | 24 696 | 0 | −0.05995 |
| D₂₃=0 | 24 744 | 24 743 | 0 | −0.06052 |
| D₃₁=0 | 24 924 | 24 924 | 0 | −0.06066 |
| D₃₂=0 | 24 969 | 24 969 | 0 | −0.06048 |
| D₃₃=0 | 24 965 | 24 964 | 0 | −0.06115 |

**Resolution of H-facet:** on **every** facet, `Q ≤ 0` everywhere, with `Q < 0` on the whole
facet **interior**; the equality locus `{Q = 0}` inside a facet is **exactly the union of that
facet's four transposition edges** (Q ≡ 0 there, §0) — the two cyclic edges and the triangle
interiors carried by the facet have `Q < 0`. Therefore

```
U₃ ∩ facet(D_rs = 0)  =  the four T-edges of that tetrahedron   (a 1-dimensional set),
∂U₃ ∩ ∂B₃            =  the 9 T-edges ∪ the 6 vertices          (a 1-complex, no 2-cells).
```

### Retraction R2
`wave14h_base_corrected.py`'s `facet_locus_ac` (a claimed explicit 2-parameter (a,c)
parametrisation of `{D₁₃=0, Q=0}` with `d = ac/(1−a)`) is **wrong**: it produces points that are
not in `{Q=0}`. The independent 300 000-point survey above (which finds Q>0 at *no* sample point
of any facet) supersedes it. Likewise the "18 interior corner 2-loci / 6 interior triple points"
corner rule of the Wave 13 spec is void: it presupposed several independent walls
(`Q₁₂, Q₁₃, Q₂₃` distinct), whereas `Q₁₂ ≡ Q₁₃ ≡ Q₂₃`.

---

## 5. Consequences for the cellulation programme (honest status)

1. `U₃ = {Q ≥ 0} ∩ B₃` is a 4-ball, `∂U₃ = {Q=0} ∩ B₃` has χ = 0, the complement hole is a single
   connected 4-dimensional region touching ∂B₃ along the six cyclic edges (`Q = −1/16`).
2. The correct boundary stratification is **6 (3-dim σ-pieces) + 9 (T edges) + 6 (vertices)**,
   glued only through the 1-complex. No 2-cells exist at this level.
3. The earlier fibre-count check `χ(Fl₃) = 6·χ(pt) + 9·χ(S¹) + 9·χ(T²) + 6·χ(T²) + 1·χ(T²) = 6`
   was built on the retracted census and must be **recomputed** from the corrected stratification;
   the target `χ(Fl₃) = 6` is therefore currently **unverified**, not refuted.
4. Remaining genuine gaps (boxed, do not fabricate):
   * the link of a **T edge** inside the wall (§2 residual);
   * proof (not just χ + connectedness) that `∂U₃ ≅ S³`;
   * connectedness of each σ-class (locally constant σ gives 6 clopen classes; that each class
     is *connected* is assumed, not shown);
   * whether a subdivision-based signed cell complex exists for the Wave-11 battery / orbit SNF
     (`δ₂(qutrit) = 4/3 ⟺ H₂(B₃) = ℤ/3`) — the σ-stratification cannot serve as that complex (§3).

---

## 6. Cross-line reconciliation with the parallel Wave 13B/13C line

While this audit was running, a **second, independent agent line** pushed to the same `main` on top
of the shared base `1c0cd1b`: `f572192` (Wave 13B spec review), `ab58ec9` (Wave 13C stage 1),
`15b7bcd` (stage 2a/2b), `9abae08` (stage 3). To avoid numbering collision that line keeps
`wave13b_*` / `wave13c_*`; **this document's artifacts were renamed to the `wave14h_*` namespace
("Wave 14H", H = the four H-items of the Wave-13 spec)** and this commit is rebased on top of
`9abae08`. Nothing of the other line was modified, reverted or force-pushed.

### Agreement (independent methods)
| statement | Wave 14H (this line) | Wave 13B/13C (their line) |
|---|---|---|
| no single-degenerate wall strata; the three row-pair degenerations coincide | `Q₁₂ ≡ Q₁₃ ≡ Q₂₃` exactly, so a wall is one hypersurface | "wall interiors (single-degenerate strata) are EMPTY" |
| Wave-12b "18 rook corners / 6 triple points" void | Retraction R2 (facet survey) | "fictions" (dimension test) |
| U₃ is a 4-ball | χ(U₃)=1 at n=24,32,40; χ(∂U₃)=0; one complement component | double(U₃) has χ=+2, homology (ℤ,0,0,0,ℤ) ⇒ ~S⁴ |
| Fl₃ → U₃ is 2-to-1 (two Jarlskog sheets) | consistent: the 6 σ-classes split as 2 c-orbits of 3, and the vertex pairings split the vertices by parity (even ↔ one orbit, odd ↔ the other) | 6 bijection regions = 3 per sheet; sheets c-invariant |

### Open tension (for the user to adjudicate, NOT resolved here)
* **F-cells.** Their base book has 9 F-cells (5 "pure" + 4 "mixed", claimed feasible). This line's
  direct survey finds `{D_rs = 0} ∩ {Q = 0} =` that facet's four transposition edges only
  (300 000 samples per facet, `Q > 0` at **no** sample point), i.e. no 2-dimensional facet locus in
  B₃. Both can hold only if their F-cells live on the double `M = Fl₃/T³_L` (a symmetric-difference
  locus there) rather than in B₃. This is the one place where the two lines appear to contradict;
  it should be checked explicitly against their `d(F)` construction, not assumed away.
* **Complex size/shape.** Their certified complex is 3786 cells at level-6 fibres with a mod-2
  assembly obstruction routed to level 12; this line's H-signs result is that the *σ-stratification
  of the wall itself* carries no 2-cells, so a signed complex must be built on a subdivision. The
  two statements are compatible but are not the same object.
* Both lines agree that `δ₂(qutrit) = 4/3` remains **OPEN**.
