# WAVE 17 — STAGE 3 OF THE QUQUART PIPELINE: THE U₄-BOOK CELLULATION
### Executed per the user directive of 2026-09-11: "Stage-3 U₄-book
### cellulation per the design consequences recorded in the note (thin
### wall-slices as seams, the 4-vs-8 stratification, non-orientability built
### in."

**Artifacts:** `wave17_u4cells.py` / `wave17_u4cells_output.txt` (the full
run, 88 s) / `wave17_u4cells_data.json` (the exported cellulation data —
the Stage-4 input).

**Bottom line.** The Stage-3 U₄-book cellulation is delivered as a certified
stratification skeleton with all three design consequences of
`WAVE16_U4BOOK_CUPSQUARE.md` §2.5 built in: (i) the **thin completable
wall-slices as the 24 seam cells** (constructive certificates 24/24, the
thinness pilot 0/24 re-confirming that the unistochastic locus on a ququart
wall is a thin subfamily); (ii) the **4-vs-8 sheet strata s₄/s₈ with the
internal critical locus C as an additional stratum**, plus the
phase-obstruction boundary P (fresh witnesses); (iii) **non-orientability
built in**: χ(c₄) = −1 pinned by exact integer arithmetic on the 9-dim base
and re-derived on the 12-dim flag level (the Wave-15 sign-representation
fact), so the C₄-orbit skeleton is non-orientable by construction and
retains only the mod-2 fundamental class — machine-verified
(H₉^{orb}(ℤ/2) = 1). One **new machine finding** is recorded: the naive
closure-containment boundary d(F) **violates d² = 0 mod 2** (odd endpoint
multiplicities {5: 18, 0: 6}) — the true d(F) needs the Stage-3.5
CKM-chain parameter tracing, exactly as the qutrit's 13C-1 tracing was far
sparser than its containment lists. **δ₁ (the ququart bit) remains OPEN.**
The qutrit verdict is untouched: H₂(B₃) = ℤ/3, δ₂ = 4/3.

---

## 1. The cellulation (the skeleton census)

| class | cells | dim | certificate |
|---|---|---|---|
| V (the permutation moduli) | 24 | 0 | exact: left-torus fixed points |
| E (the transposition strata) | 72 | 1 | **each ≅ (0,1), endpoints pinned** |
| F (the one-zero strata) | 16 | 7 | constructive witnesses 16/16 |
| s₄, s₈ (the sheet strata) | 2 | 9 | exemplars + deep multistart [est] |
| C (the internal critical locus) | 1 | 8 | continuation evidence [est+theory] |
| P (the phase-obstruction boundary) | 1 | 8 | interior witnesses [est] |
| w (the seams = thin wall-slices) | 24 | 8 | constructive 24/24 [cert] |
| κ (the corner skeleton) | 144 (+96 open) | 7 | 144 witnesses; 36 exact-infeasible |

Variant A = 284 cells (the 144 certified corners); variant B = 380 (the 240
distinct-pair corners, the 96 unresolved included). The 36 same-pair branch
pairs are excluded by exact infeasibility.

**The c₄-cell-map (exact, c₄⁴ = id everywhere):** V: ρ ↦ σ∘ρ (6 orbits of
4); E: the support relabel (i,k) ↦ (i,σ(k)) (18 orbits); F: (i,k) ↦
(i,σ(k)) (4 orbits); the seams: (i,j\|k) ↦ (i,j\|σ(k)) (6 orbits); the
corners: the induced pair map (60 free orbits over the 240; the same-pair
"opposite" corners W(i,j\|k),W(i,j\|k+2) are c₄²-stabilized 2-orbits — but
those are the infeasible ones, excluded); the strata s₄, s₈, C, P are
c₄-fixed (the completion system's column-equivariance is exact algebra).

## 2. The certified support strata (`wave17_u4cells.py` PART I)

**V (24).** Every [P_ρ] is a fixed point of the whole left torus (the
conjugation P_ρ⁻¹·diag·P_ρ stays exactly diagonal — 192/192 machine checks
with identically-zero off-diagonal entries): the T³-fibres of Fl₄ → M₄
fully collapse over the V-cells — the Stage-4 fibre-degeneration input.

**E (72) — the E-cell theorem [cert].** The transposition strata (the
6-entry supports, the 2×2 blocks + the complement matching):
* the rephasing invariants of a 2×2 unitary block are x = |a|² and Θ =
  arg(ad/bc); **unitarity forces cos Θ = −1 exactly** (sympy:
  x²+(1−x)²−2x(1−x)cosΘ = 1 ⇒ cosΘ = −1), so Θ ≡ π and **x ∈ (0,1) is the
  only invariant**;
* 2000 random U(2) blocks: max |Θ − π| = 1.45e−14;
* same-x pairs are linked by diagonal double cosets: 120/120 to 1e−9 (a BFS
  potential solve on the support graph — the solvability condition is
  exactly Θ′ = Θ);
* the endpoints x → 0/1 land exactly on the two permutations ρ∘τ, ρ.
⟹ **each E-stratum ≅ (0,1) with the certified boundary data**
**d(E) = V(ρ) − V(ρ∘τ)** (the x-orientation).

**F (16).** Constructive one-zero unitaries 16/16 (the zero-column +
Gram–Schmidt completion). The closure poset is certified: each F(i,k) has
45 E-strata in its closure; each E lies below 10 F's (16·45 = 72·10 = 720
— the counts cross-check).

**THE HONEST FINDING (new, machine-exact).** The naive containment
boundary d(F) = Σ(closure E's) **violates d² = 0 mod 2**: for F(0,1) the
V-endpoint multiplicities are **{5: 18, 0: 6}** — the value 5 is odd. The
true d(F) is not the containment union (the qutrit 13C-1 analogue had
*traced* 4-sided frontiers, far sparser than its closure lists). **d(F) is
UNPINNED at Stage 3** — labeled [open], with the Stage-3.5 CKM-chain
parameter tracing as the identified route.

## 3. The seam layer (design consequences (i) + (iv), PART II)

* **The 24 seams:** constructive unistochastic wall points on every branch
  W(i,j\|k) — certificates per point: U U† = I to 1e−9, |U|² doubly
  stochastic, the wall equation s_k = Σ_{l≠k} s_l to 1e−12, all 6 polygon
  slacks ≤ 0. **24/24 [cert]** (the Wave-16 result re-derived from
  scratch).
* **The thinness pilot:** 24 fresh random polygon-level wall points (rows
  split freely, the wall equation solved, the complement rows sampled in
  the transportation polytope): **0/24 complete** (80 starts each) —
  consistent with Wave-16's 0/120: the seam cells are the THIN completable
  slices, not the wall branches.
* **The seam fibres** (seeded Newton counts at the constructive wall
  points, 150 starts + the constructive seed): the distribution
  {2: 15, 3: 4, 4: 2, 5: 1, 7: 1, 8: 1} — numeric estimates at the
  degenerate locus, the Stage-4 sheet-structure input.
* **The corners:** the same-pair infeasibility is EXACT (sympy: with s > 0
  the two wall equations have no solution; without positivity the forced
  solution is s_{l1} = −s_{l2}) — the 36 same-pair pairs excluded. The
  census over 276 pairs: **{infeasible-exact: 36, feasible: 144,
  unresolved: 96}** — reproducing Wave-16 exactly. Each realized corner
  satisfies both wall equations to 1e-10: **each corner lies in exactly 2
  seams** (the manifold-with-corners property at the corner level).
* **The branch graph:** the 240-level graph and even the 144-witness graph
  are both connected (single component of 24) ⟹ the closure-forced design:
  d² = 0 requires each sheet stratum's seam set to be a union of
  components, hence **both s₄ and s₈ abut all 24 seams**:
  **d(s₄) = d(s₈) = Σ(24 w) + C + P** (the per-branch near-wall sheet
  counts are the fold data — Stage-4 sheet-level business, honestly
  numeric there).

## 4. The book strata (design consequence (ii), PART III)

* **s₄/s₈:** fresh Haar moduli at 600 starts: {4: 4, 8: 4}; deep
  multistarts (2000 starts) hold both k = 4 and k = 8. Both strata are
  nonempty with confirmed exemplars (the exemplar matrices recorded in the
  JSON).
* **C (the internal critical locus):** continuation walks show genuine
  count transitions (4 → 0 through the phase boundary; 8 → 4 across the
  critical locus). With the count locally constant off the branch locus
  (the standard covering premise) and both values realized, a nonempty
  critical locus separates the strata: C is the 8-dim additional stratum
  (the analog of the qutrit's Jarlskog fold, now a whole locus).
* **P (the phase-obstruction boundary):** 37 strictly-interior polygon
  points tested (250 starts): 31 complete, **5 do NOT** — fresh witnesses
  (min slacks −0.464, −0.433) that U₄ is a proper subset of the polygon
  region, re-confirming Wave-16.
* **c₄-equivariance:** k(D) = k(D·P) 3/3.
* **The fold book (2 branches):** W(0,1\|0): interior k = 4 → near-wall 4
  (no coalescence yet at t = 0.01); W(1,2\|3): interior k = 4 → near-wall
  2 (pairwise coalescence — the Jarlskog-fold analog). Numeric estimates at
  the degenerate locus, honestly labeled.

## 5. Non-orientability built in (design consequence (iii)) [exact]

1. **The 9-dim base:** the column 4-cycle acts on the 16 entry coordinates
   with sign (+1)⁴ = +1; the invariant decomposition
   (row-sum-zero 12-dim) = V₉ (the DS-directions) ⊕ col-uniform(3); the
   col-uniform 3-dim piece carries sign(σ) = −1; hence
   **det(action on V₉) = −1** (sympy exact, on the corner basis; the
   numeric cross-check gives −1.000000).
2. **The 12-dim flag level:** the conjugation X ↦ P⁻¹XP permutes the 16
   entry positions with sign +1, the Cartan (diagonal 4-dim) with −1, so
   the off-diagonal 12-dim quotient carries **−1** (exact; the numeric
   12×12 block computation gives −1.000000).
3. **The Wave-15 fact re-derived from scratch:** the coinvariant ring
   ℤ[x₁..x₄]/(e₁..e₄) has standard monomials per degree (1,3,5,6,5,3,1)
   (total 24 = |S₄|); the degree-6 piece is 1-dimensional (m = x₂x₃²x₄³)
   and σ(m) reduces to **−m**: the sign representation.
4. **The factorization:** sign(Fl₄) = sign(M₄)·sign(T³-fibre) =
   (−1)·(+1): the fibre map t·[u] ↦ t·[uP] is the identity in the fibre
   coordinate (c₄ commutes with the left torus) — consistent at every
   level.

⟹ **χ(c₄) = −1 is the orientation character of the skeleton's gluing
data; the C₄-orbit skeleton (the base book of B₄'s cellulation) is
NON-ORIENTABLE BY CONSTRUCTION.**

## 6. The skeleton battery (PART IV)

The boundary data, honestly labeled: d(E) [cert]; d(w) = the corner
incidence [design, lex-signs]; d(s₄) = d(s₈) = Σw + C + P [design,
closure-forced]; d(C) = d(P) = 0 [terminal: the deeper stratification
open]; **d(F) UNPINNED [open]**.

* **d² = 0 (mod 2) on the truncated design complex: PASS** in both
  variants (the matrix products vanish exactly; the cancellation is the
  "each corner in exactly 2 seams" incidence).
* **The mod-2 homology** (the truncation labeled):

| | H₉ | H₈ | H₇ | H₁ | H₀ |
|---|---|---|---|---|---|
| skeleton A (144) | 1 | 2 | 137 | 49 | 1 |
| skeleton B (240) | 1 | 2 | 233 | 49 | 1 |
| **orbit B (the C₄-quotient)** | **1** | 2 | 59 | 13 | 1 |

  H₉ = 1 is the fundamental class s₄+s₈; H₁/H₀ are the 1-skeleton's
  (connected, cycle rank 49 — the Birkhoff edge graph; 13 on the orbit).
  H₇ carries the 16 F-classes and the unhit corners — the codim-2
  truncation, honestly labeled.
* **The orbit complex:** d² = 0 PASS; **H₉^{orb}(ℤ/2) = 1 — the mod-2
  fundamental class SURVIVES the non-orientable quotient** (the
  orientation character χ = −1 kills the integral class, exactly as
  non-orientability requires; only ℤ/2-duality remains, the Wave-15
  consequence built into the skeleton).
* The gates G'1–G'6 all PASS (with the numeric layers labeled [est]).

## 7. The honest gaps + the Stage-4 scope

1. **d(F) unpinned** (the mod-2 obstruction above): the Stage-3.5 route =
   the CKM-chain parameter tracing (the 4×4 Givens-chain coordinates: 6
   angles + 3 phases over the GZ-interlacing domain — the qutrit 13C-1
   tracing analog).
2. **The middle support strata** (the 2..6-zero pattern lattice, the
   cascade strata) uncellulated — the skeleton truncates at the one-zero
   level plus the block strata (V/E) exactly as the qutrit's 32-cell
   structure did; the middle lattice is the Stage-3.5/4 enumeration.
3. **The 96 corner pairs** unresolved (sampler-limited, not exclusion).
4. **The sheet/fold data** numeric: the coalescence partitions and the
   seam fibres are estimates at degenerate loci.
5. Then, per the 13C template: **level-L fibres over the skeleton** (the
   T³-degeneration: pt over V (certified in PART I), S¹ over E (the
   stabilizer T² = the phases constant on the block component — exact
   support-component structure), T³ over F and the generic strata — note
   the contrast with the qutrit: no T²-level, the ququart's effective
   left torus is T³), **the seam battery, the orbit SNF under the
   twisted orientation data** (ℤ/2-duality; the δ₁ = 3/2 paper-line link
   to be re-derived under non-orientability first).

**Nothing here reopens the qutrit verdict: H₂(B₃) = ℤ/3, δ₂ = 4/3.**
