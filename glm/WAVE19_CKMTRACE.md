# WAVE 19 — STAGE 3.5: PIN d(F) VIA THE CKM-CHAIN PARAMETER TRACING
### Executed per the user directive of 2026-09-11: "3.5 (pin d(F) via
### CKM-chain tracing) and 13C Stage 2a/2b."

**Artifacts:** `wave19_ckmtrace.py` / `wave19_ckmtrace_output.txt` (the
full run, 356 s) / `wave19_ckmtrace_data.json` (the Stage-4 input).

**Bottom line.** BOTH deliverables, in one coherent statement. **(a) THE
PINNED d(F) (the middle-lattice form):** d(F) = Σ(the 15 feasible z=2
faces) is a machine-certified mod-2 cycle — d₂₃∘d(F) = 0 exactly, the
feasibility table parity-closed through z=4, all 120 z=2 strata carrying
constructive witnesses. **(b) THE CORRECTION THEOREM:** the Wave-17
framing of d(F) as an E-level 1-chain is STRUCTURALLY IMPOSSIBLE at
n = 4 — the parity theorem (each relevant V is an endpoint of exactly
2 moving + 3 fixed-row transposition E-cells = 5, odd) — so the honest
"pin d(F)" lands one level deeper than the Wave-17 note scoped, in the
middle support lattice. The method itself (the CKM-chain preimage trace
+ the M-class clustering) is VALIDATED at n=3 against the certified
13C-1 `D_FACE` (9/9, mod 2). **δ₁ remains OPEN** (the Stage-4 orbit-SNF
target untouched); the qutrit verdict is untouched: H₂(B₃) = ℤ/3,
δ₂ = 4/3.

---

## 1. The method: the 4×4 CKM chain + the n=3 validation [cert]

The chain (the qutrit Vckm cascade generalized): U₄ = G₃₄(θ₆)·G₂₄(θ₅,δ₃)·
G₂₃(θ₄)·G₁₄(θ₃,δ₂)·G₁₃(θ₂,δ₁)·G₁₂(θ₁) — **6 angles + 3 phases = 9
parameters = dim M₄**. The chain-entry structure (machine-exact, 400
samples to 1e-12):

* row 0: |U₀₀| = c₁c₂c₃, |U₀₁| = s₁c₂c₃, |U₀₂| = s₂c₃, |U₀₃| = s₃;
* col 3: |U₁₃| = s₅c₃, |U₂₃| = s₆c₅c₃, |U₃₃| = c₆c₅c₃;
* the 7 chain entries (pure: zeros realized on the s/c-factor angle
  walls) + the 9 mixed lower-left entries (zeros on the curved
  interference-closure loci) = 16 = the certified F-census;
* the coverage: 60/60 Haar moduli inversions to 1e-8 [cert].

**THE TRACE:** for each E-cell (the moduli families D_E(x)): the
multistart damped Gauss–Newton preimage solve on the 16-entry moduli
match (9 vars); the solutions clustered into M₄-classes by the
**rephasing double-coset test** (the phase-potential BFS on the support
graph — the tolerance matched to the solver precision; the on-wall
phase-redundancy collapses the solution families, machine-exhibited).

**THE n=3 VALIDATION (the method certificate):** the identical pipeline
at n=3 reproduces the certified 13C-1 `D_FACE` (from the committed
`wave13c_base_data.json`) **exactly, mod 2, 9/9 F-cells**. The counting
rule it certifies: **c(E₀; F) = the E-fiber (sheet) count k_E mod 2**;
the qutrit's k_E = 1 everywhere (the two sheets merge at the boundary —
the M₃-fiber over every E-modulus is a single class, 36/36 machine
checks).

## 2. The ququart E-fibers: the 4-vs-8 book MERGES at the boundary [est]

The E-fiber (sheet) counts over the 72 ququart E-cells: **k_E = 1 for
all 72** (the x-continuation solve at x ∈ {0.75, 0.25}; the counts
constant along x). So the 4-vs-8 sheet book — two sheet strata over the
generic locus — collapses to a SINGLE boundary sheet over every
transposition stratum, exactly as the qutrit's 2-sheet book did. The
Stage-4 interface data at the E-level is therefore the full containment
(45 E's per F) with k_E = 1 (the table exported).

## 3. THE PARITY THEOREM (the correction, exact) [cert]

For F(i,k) and each V(ρ) with ρ(i) ≠ k, the containment E's having V(ρ)
as an endpoint decompose EXACTLY as:

* **2 moving-row transpositions** τ (τ(i) ≠ i, ρ(τ(i)) ≠ k), and
* **3 fixed-row transpositions** τ ⊂ {rows ≠ i} (all valid),

= **C(n−1,2) + (n−2) = 3 + 2 = 5 per V — ODD.** Consequences:

* the E-level mod-2 "d(F)" cycle σ(F) = Σ c_E·E with the natural
  coefficients (containment, or the k_E sheet counts) is **structurally
  impossible at n = 4** — both gates FAIL 16/16 (re-verified: the naive
  {5:18, 0:6});
* at n = 3 the count is 1 + 1 = 2 (EVEN) — the qutrit's dimensional
  luck: that is why the 13C-1 traced d(F) at the E-level worked there;
* **the Wave-17 "naive containment boundary fails mod 2" finding is
  this transposition arithmetic, not a pinning gap** — no sparser
  E-sublist can close it (the obstruction is per-V, not per-E);
* general coefficient systems over F₂ exist (18×45: large kernel), but
  none is canonical — the honest object is one level deeper.

## 4. THE MIDDLE SUPPORT LATTICE — the true d(F), pinned [cert]

The support stratification of M₄ has dims **9, 7, 5, 3, 1, …** (each
extra zero costs 2 real dimensions): the F-cells (7-dim) have no
6-dimensional faces — the true d(F) is the sum of the **z=2 faces
(5-dim, the codim-2 strata)**, and the boundary-of-boundary
cancellations run through the z-level complex:

* **the z=2 census: 120/120 patterns FEASIBLE** (constructive witnesses
  by the alternating-projection column construction; the
  transpose-symmetry check passes: 24 same-row = 24 same-col = feasible;
  72 rook-free = feasible) — every F-cell has all **15** z=2 faces;
* **the z=3 census: 240/560 feasible** — the drops are clean by symmetry
  class (row-profile, col-profile): the feasible classes are
  ((1,1,1),(1,1,1)) [96] and ((2,1),(2,1)) [144]; the classes
  ((1,1,1),(2,1)) [144], ((1,1,1),(3,)) [16], ((2,1),(1,1,1)) [144],
  ((3,),(1,1,1)) [16] are exactly infeasible — the sampler is
  class-consistent [cert];
* **the z=4 census: 60/1820 feasible** (the 2×2-block classes
  ((1,1,1,1),(2,2)) [36] and ((2,2),(1,1,1,1)) [24 + 12
  sampler-unresolved, by class symmetry feasible]; the 12 are honestly
  labeled [est]) — the feasible z=4 strata FLOAT: their z=3-parents are
  the all-infeasible ((2,1),(1,1,1)) class;
* **GATE C3 (d₂₃∘d(F) = 0 for all 16 F-cells): PASS [cert]** — each
  feasible z=3 stratum in F's closure has exactly 2 feasible z=2-parents
  (drop either extra zero): the mod-2 cancellation is exact;
* **GATE C6 (the deep parity-closure z=3→z=4): PASS [cert]** — 0 breaks:
  the feasibility table is parity-closed (no z=4 has exactly one
  feasible z=3-parent) — the z-level complex is a genuine mod-2 complex;
* **the z-complex mod-2 homology (feasible z=2 → z=3):** rank d₂₃ = 104;
  **H_z2 = 16, H_z3 = 136** (of 120 × 240); the 16 F-face-vectors span
  dimension 15 — the single relation is Σ(all 16 F-vectors) = 0, i.e.
  **each z=2 face lies on exactly 2 F-cells** (F(i,k) and F(j,l)), the
  exact 13C-1 "each corner in exactly 2 seams" analog, one level up.

**(P-19) THE PINNED d(F):** d(F(i,k)) = Σ(the 15 feasible z=2 faces),
a mod-2 cycle in the z-level complex, certified by the exact gates
above. This is the object the Stage-4 level-L fibre assembly consumes
(the F×T³-cells' boundaries = d(F)×(fibre-cells) + F×(fibre-boundaries),
with the E-level interface data = the containment + k_E = 1).

## 5. The honest gaps + the Stage-4 scope

1. **The z ≥ 5 censuses** (the deeper feasibility drops and the
   completion of the z-lattice down to the E/V levels): scoped, not run
   (the z=4 sampler-unresolved 12 aside, the class structure is clean
   and the parity-closure mechanism is proven).
2. **The integral (signed) d(F)**: the mod-2 cycle is pinned; the
   orientations (the 13C-1-style signed cyclic words) are the Stage-4
   business, as they were for the qutrit (13C-1 → 13C-7).
3. **The E-level σ(F)**: as an incidence TABLE (the containment + the
   sheet data) it is exported for the Stage-4 interface maps; as a
   mod-2 cycle it does not exist (§3) — the honest correction.
4. Then, per the 13C template: the level-L fibres over the certified
   skeleton + the middle lattice (pt over V / S¹ over E / T³ over F and
   the generic strata; the z=2 strata's fibres to be typed), the seam
   battery, the orbit SNF in degree 9 with UNtwisted ℤ (the Wave-18
   pinned target H₉(B₄;ℤ) = ℤ/2 or 0) with the twisted degree-3
   cross-check.

## 6. The 13C Stage-2a/2b reconciliation (the carried task)

The carried task "build wave13c_total.py; the 3786-cell assembly;
G1–G8 + the orbit SNF; decide H₂(B₃)" is **CLOSED in the repo** —
verified from the committed artifacts this session: `wave13c_total.py`
ran (the stage-2a/2b pins: the level-6 fibres certified, the free-cell
d²=0 exact, the Z/2 obstruction machine-pinned — the honest record),
the obstruction was dissolved by the route-b per-sheet seam gauging
(`wave13c_seam.py`: the 14910-cell battery G1–G8 + d̄² ALL-PASS) and
the orbit SNF closed the bit: **H₂(B₃) = ℤ/3, δ₂(D(ℂ³)) = 4/3
machine-certified** (re-verified independently in Waves 15/16). The
stale carried list (the documented summary-hazard) is corrected here;
no qutrit work was re-done.

## 7. Scoreboard

* **δ₁ (ququart): OPEN** — the Stage-4 target (the orbit SNF, degree 9,
  untwisted) is untouched this wave; Stage 3.5 delivered its input: the
  pinned d(F), the E-fiber table, the middle lattice's first three
  levels.
* **δ₂ (qutrit): 4/3, machine-certified** — untouched (and the carried
  task reconciled above).
* Manuscripts untouched.

**Nothing here reopens the qutrit verdict: H₂(B₃) = ℤ/3, δ₂ = 4/3.**
