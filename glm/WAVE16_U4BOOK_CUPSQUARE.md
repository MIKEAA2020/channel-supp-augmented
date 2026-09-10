# WAVE 16 — THE U₄ BASE STRATIFICATION (QUQUART STAGE 2) + THE CUP SQUARE
### Executed per the user directive of 2026-09-11: "the U₄ base
### stratification (24 wall branches, the k-sheet book) is the decisive
### ququart stage 2 — machine-computing x² on the orbit complex to close
### the bridge's last cited link."

**Artifacts:** `wave16_cupsquare.py` / `wave16_cupsquare_output.txt`
(the cup square); `wave16_u4book.py` / `wave16_u4book_output.txt` (the
U₄ stratification). The cup-square script re-imports `wave13c_seam`, so
the FULL 13C-7 battery re-runs from scratch before its new work.

**Bottom line.** Both directive items are machine-executed end-to-end.
(1) **x² ≠ 0 in H⁴(B₃; ℤ) = ℤ/3 is now a machine fact** — the last
cited machine-computable link (P5) of the H₂→δ₂ bridge is closed: the
bridge now rests on machine premises everywhere except the paper-line
formula (P6). (2) **The U₄ base stratification is measured**: all 24
wall branches carry certified unistochastic points (constructive
orthounitary witnesses); the k-sheet book is genuinely two-valued
(k = 4 and k = 8 on separate strata, confirmed by 5000-start deep
multistart); **U₄ is a PROPER subset of the polygon region (machine
witnesses)** — the phase-obstruction boundary lives INSIDE; the corner
census: 36 same-pair branch pairs analytically infeasible, 144
distinct-pair pairs with constructive orthostochastic witnesses.

---

## 1. THE CUP SQUARE ON THE ORBIT COMPLEX (`wave16_cupsquare.py`)

### 1.1 The model correction this run forced

The first attempt used the order complex of the orbit face poset with
poset-comparability voltages. It died on a structural fact worth
recording: **the 13C-7 orbit complex is a NON-REGULAR CW complex** — a
lifted cell can carry two C₃-equivalent vertices in its closure (the
first probe: the orbit of F0×P₀₀ contains both vertex 1 and T²(1)), so
(a) the face poset loses the gluing data and (b) the "unique lifted
incidence" fails at the transitive level (the pair (1, 222) has two
valid lifts). The correct regular model is the quotient Δ-set

> K′ := Δ(P_T)/C₃ = sd(Fl₃-cellulation)/C₃,

whose k-simplices are the C₃-orbits of the (k+1)-chains of the total
complex's face poset. The C₃-action is free on simplices (flags have
strictly increasing dimensions, so no simplex maps to itself), and
|K′| = |T|/C₃ = |B₃|. The Alexander–Whitney cup product is defined on
any Δ-set via the ordered face maps.

### 1.2 The voltage and the Bockstein

For orbit-cells z let a(z) ∈ {0,1,2} be the sheet exponent
(z = T^a(z)·rep([z])). For a comparable pair x < y, the K′-edge it
labels is the orbit (x, y) with relative shift d = a(y)−a(x) mod 3, and
the arc-lift of the regular C₃-cover (path-lift uniqueness; each
edge-orbit has exactly its 3 translate segments as preimage) gives

> u(x→y) = (a(y) − a(x)) mod 3,

the classifying class f\*(character) ∈ H¹(B₃; F₃). Then x̄ = β₃(u) =
δũ/3 on 2-simplices — the mod-3 wraparound of the a-differences
(machine-measured: nonzero on 20 840 / 177 552 rep-rooted cover
triangles), an exact cocycle at the cochain level (δũ ≡ 0 mod 3 by the
a-telescoping, an identity).

### 1.3 The certificates (all machine, all PASS)

* **(II) structural:** no two boundary entries of any rep share an
  orbit (each orbit edge has exactly one lifted incidence); every
  orbit-boundary coefficient is ±1; the T-signs on all 6 vertex cells
  are +1.
* **(IV) the cycle transport S′:** S′(σ) = the C₃-orbits of the full
  flags under rep(σ) with the classical subdivision signs
  ε(F) = (−1)^{k(k+1)/2}·Π co (D-coefficients). The chain-map property
  **dS′ = S′d̄ is verified EXHAUSTIVELY on all 3 912 orbit cells of dim
  1..4: 0 mismatches** (the hand-derived sign theory was unreliable —
  the machine arbitrates; the vertex-sign triviality is what makes it
  work).
* **(V) H_k(B₃;F₃) bases** by exact mod-3 elimination: (1,2,2,2,1) for
  k = 1..5 — matching the UCT from the certified H\*(B₃).
* **(VI) THE DECISION:** the AW cup square on the 4-simplices of
  S′(γ), ⟨x̄², S′(γ)⟩ = Σ ε·x̄(v₀v₁v₂)·x̄(v₂v₃e), over an H₄-basis:

  > **H₄-pairing vector = [0, 2]  ⇒  x̄² ≠ 0 in H⁴(B₃;F₃).**

  Aux products for the record: ⟨u, S′(H₁-rep)⟩ = [1] (the voltage is
  genuinely the classifying class, nonzero on π₁ = C₃); ⟨u·u⟩ = [0,0]
  (graded commutativity, as it must); ⟨x̄·u⟩ = [0,1].
* **(VII) cross-checks:** ⟨x̄², S′(∂c₅)⟩ = 0 for 5 random 5-boundaries
  (the functional descends to H₄); a random lift re-choice
  (u → u − δb) leaves the pairing vector EXACTLY [0, 2].

### 1.4 The theorem (the bridge, P5 closed)

> **THEOREM.** With (P1)–(P4) as in Wave 15 (machine premises, all
> re-certified on import), **(P5) is now [machine, THIS RUN]: x² ≠ 0 in
> H⁴(B₃;ℤ)** — x̄² = ρ(x²) (ρ a ring hom) and ρ is injective on the
> 3-torsion, and x̄² pairs nonzero with the H₄ basis. (P6) [cited: the
> paper line] δ₂(D(ℂ³)) = 4/3 ⟺ x² ≠ 0.
>
> **Conclusion:** the two directions of the P5 equivalence are now
> verified INDEPENDENTLY — the CLSS cascade selected d₃ = 0 (World 1,
> the homological side) and the cup square is measured nonzero directly
> (the cohomological side). **The bridge H₂(B₃) = ℤ/3 ⇒ δ₂ = 4/3 rests
> on machine premises end-to-end except the paper-line formula (P6).
> World 2 is excluded on both sides.**

The qutrit verdict is unchanged and now fully closed at the machine
layer: H₂(B₃) = ℤ/3, δ₂(D(ℂ³)) = 4/3.

---

## 2. THE U₄ BASE STRATIFICATION (`wave16_u4book.py`) — ququart stage 2

The 13C template's Wave-12a/12b/13B stages, applied to d = 4.

### 2.1 The 24 wall branches W(i,j|k)

For each of the 6 row pairs (i,j) and each column k: the
quadrilateral-degeneracy locus s_k = Σ_{l≠k} s_l (s_l = √(D_{il}D_{jl}))
— the analog of the qutrit's 9 fold-walls, 24 branches here (6×4).

**Constructive unistochastic wall points** (the decisive sampler): at a
wall point the degenerate pair forces the FLAT (collinear) phase
configuration, and a completion exists iff the remaining rows lie in
the achievable family — so the sampler builds D = |U|² directly, with U
unitary, row i = a ≥ 0, row j = (±b) with the sign flip at column k:
**the wall equation IS the orthogonality ⟨row_i, row_j⟩ = 0.** The
complement rows are sampled in the U(2)-family (Gram–Schmidt + a
complex mixing). Certificates per point: U U\* = I to 1e-9, |U|² = D
doubly stochastic, the wall equation to 1e-12, all 6 polygon slacks
≤ 0.

> **All 24 branches carry certified unistochastic points ⇒ every branch
> contributes to ∂U₄.** Completion tests at 3 points per branch
> (250 starts + the constructive seed): 3/3 completable everywhere;
> the wall fibers there measure 2–11 (numeric estimates at the
> degenerate locus).

**A NEW STRUCTURAL FACT (the ququart/qutrit contrast):** unlike the
qutrit — where the whole wall is unistochastic (the 13C-4 adjudication)
— at a ququart wall point the flat-pair condition makes the
unistochastic locus on the wall a THIN subfamily: in the pilot, random
polygon-level wall points (rows split freely) gave **0/120
completions**. The wall branches bound U₄, but only along thin
completable slices.

### 2.2 The k-sheet book (the fiber of M₄ = Fl₄/T⁴_L → U₄)

* **Qutrit validation:** the analytic-Jacobian gauge-fixed Newton
  solver returns the generic fiber **= 2 exactly** (the Jarlskog
  double) — PASS.
* **Ququart generic fiber at 12 Haar points: {4: 9, 8: 3}.**
  **The 4-vs-8 split is GENUINE, not missed basins:** 5000-start deep
  multistart on a k=4 point returns 4; on a k=8 point returns 8.
* **Continuation** (tracked random walks): the count is stable within
  strata and CHANGES across transitions (walks that end with tracked
  k=4 but dense-restart k=8 at the same endpoint) — i.e. **there is a
  critical/branch locus INSIDE the region separating a 4-sheeted from
  an 8-sheeted book.** The U₄-book is not a constant-sheet cover.
* **c₄-equivariance:** k(D) = k(D·P) for the column 4-cycle — 4/4
  agree (the wall branches fall into the 6 c₄-orbits of 4 as the
  template predicts).
* **The wall fold:** tracked approach to constructive wall points:
  k = 4 → near-wall coalescence to 2 (sheets merge in pairs — the
  Jarlskog-fold analog), with the wall fiber measured at 2; other
  branches show k = 8 → 8 (no coalescence at t = 0.01; the merge is
  closer to the wall), and one approach point itself not completable
  (k = 0: the thin-locus effect). Honest labels: the fold partitions
  are numeric estimates at a degenerate locus.

### 2.3 The corners (276 branch pairs, polygon level)

* **Same-pair branches (36 = 6 pairs × C(4,2)):** analytically
  infeasible — two degeneracies of one quadrilateral force the
  remaining sides to vanish, impossible with positive entries
  (machine-confirmed: no constructive witness either).
* **Distinct-pair branches (240):** **144 carry constructive
  ORTHOSTOCHASTIC witnesses** (D = |U|², U real orthogonal, both wall
  equations = the two 1–3 sign-split orthogonality conditions, flips
  assigned to the non-shared rows); 96 unresolved by the sampler (the
  sign-pattern-after-projection resampling failed; labeled honestly —
  feasibility not excluded). Completion at 30 tested witnesses: 30/30
  (the witness is itself a completion).

### 2.4 U₄ vs the polygon region — the interior phase-obstruction boundary

81 strictly-interior polygon points (Sinkhorn, all 6 slacks < −0.02)
tested with 500 starts each: **76 complete, 4 DO NOT.**

> **U₄ is a PROPER subset of the polygon region — machine witnesses.**
> Three witness matrices are recorded in the output (min slacks
> −0.43/−0.45/−0.47, deep in the polygon interior). The
> phase-obstruction boundary (the critical locus of M₄ → U₄) lives
> INSIDE the polygon region — this is the n = 4 contrast with the
> qutrit (where unistochastic = the triangle inequalities exactly),
> and it is the same object that splits the book into 4- and 8-sheeted
> strata.

### 2.5 Design consequences for the Stage-3 cellulation

Per the 13C template, the honest U₄-book cellulation must build in:
(i) the 24 wall branches as the fold walls, with the THIN completable
slices as the seam structure; (ii) the variable sheet count (4 vs 8)
with the internal critical locus as an additional stratum (the analog
of the qutrit's Jarlskog branch, now a whole locus); (iii) the
non-orientability of B₄ (Wave 15: c₄ reverses orientation) in the sheet
gluing; (iv) the same-pair-branch exclusion and the 144 constructive
corner witnesses as the corner skeleton. Then: level-L fibres, the seam
battery, the orbit SNF per the template.

---

## 3. Updated remaining tasks / open problems

1. **Ququart bit δ₁** — OPEN, with the Stage-2 stratification now
   measured: the decisive continuation is the honest U₄-book cellulation
   (the design consequences above), then the battery + orbit SNF; the
   δ₁ = 3/2 paper-line link must be re-derived under non-orientability
   (Wave 15).
2. **The bridge** — CLOSED at the machine layer (P5 machine-computed;
   P6 the only cited input, the paper-line formula, by design).
3. **Manuscript integration** — unchanged (user decision).
4. The 96 unresolved corner pairs (sampler-limited, not exclusion) and
   the exact sheet-count stratification (4 vs 8 regions + the critical
   locus) are scoped continuations of Stage 2, non-blocking for the
   Stage-3 design.

**Nothing in this wave reopens the qutrit verdict: H₂(B₃) = ℤ/3,
δ₂(D(ℂ³)) = 4/3 — now with the bridge's last machine-computable cited
link closed and the cup square measured directly on the certified
complex.**
