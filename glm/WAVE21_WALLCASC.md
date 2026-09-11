# WAVE 21 — STAGE 4b: THE WALL-CASCADE CENSUS BELOW κ + THE
### DRIFT-MONODROMY LIFT (consuming W19's P-19 corner data)
### Executed per the user directive of 2026-09-12: "the wall-cascade
### census below κ and the drift-monodromy lift (consuming W19's P-19
### corner data), which would harden the FALSE verdict or re-open it
### the other way."

**Artifacts:** `wave21_wallcasc.py` (the full pipeline, parameterized
`W21L`; levels 2 and 3 run) / `wave21_wallcasc_output.txt` (the full
level-2 run: Parts 0/A–F, 137 s) / `wave21_wallcasc_L3_output.txt`
(the level-3 confirmation) / `wave21_wallcasc_data.json` (the census +
the drifts + the homology + the verdict — the Stage-4c input).

**Bottom line.** BOTH deliverables, and the verdict FLIPS THE CONDITIONAL.
**(a) THE WALL-CASCADE CENSUS (the exact combinatorial layer, the
T-assignment prover over all 11,464 wall-set candidates):** the
**triangle obstruction** (any wall-set whose pair-graph contains a
triangle is exactly infeasible — the phase-compatibility mod 2π fails
for every T-assignment), which caps the cascade at m = 4 (Turán) —
**NO m ≥ 5 wall-strata exist**; the **same-k theorem** (the 48 same-k
shared-row corners exactly infeasible — the W17 96-unresolved RESOLVED:
48 infeasible + 48 disjoint); the **path-forcing theorem** (the 432
path-triples force a 4th wall — the pure path strata EMPTY); the
**star theorem** (the 96 star-triples need pairwise-distinct k's; each
kept corner in exactly 2 stars: 144×2 = 288 = 96×3); the
**balanced-k theorem** (the C₄-quads need balanced k-multisets); and
the NEW **alternating-quad theorem** (the product-identity argument:
the 36 alternating C₄'s force vanishing pair-products in the non-wall
columns — the pure strata exactly EMPTY, closure-forced into the
support cascade). **The corrected book: κ 192 (the 48 same-k REMOVED) +
τ 96 + q 72 (the 36 alternating REMOVED): 932 strata, 53,816 cells
(L=2), χ = 24 = χ(Fl₄) and the orbit χ = 6 = χ(B₄) exact.** The
witnesses: the 36 disjoint diff-k corners via the CKM chain (walls to
1e-12) + the S₄×S₄ relabeling orbits; the stars and the all-distinct
quads via REAL-ORTHOGONAL matrices (the walls exact by the row
orthogonality — the W17 mechanism); the 12 same-k disjoint corners
honestly UNRESOLVED (the degenerate-collapse evidence, kept per the
W20-B precedent). **(b) THE DRIFT-MONODROMY LIFT (the P-19
consumption):** the monodromy-carrier census (E codim-8 / V codim-9
unlinkable — the n=4 dimensional luck vs the qutrit's codim-3
E-windings; the wall/support strata one-sided; only the
non-unistochastic pockets carry π₁ — the (c)-scope) + THE
LEFT-EQUIVARIANCE CERTIFICATE (polar(t₀·M) = t₀·polar(M) exact,
200/200: the rescale-polar lift is left-torus-equivariant — the W20 §2
flat-gauge claim REALIZED by a canonical equivariant lift; THE QUTRIT
CONTRAST: the 13C's phased c₃ was NOT equivariant — the structural
difference) + the two-frame interface spot-checks (the 5 P-19
F→z2→z3 classes: drift L·t₀⁻¹ = 0 to machine precision) + the
z3→z4-interface-EMPTY note (the W19 floating-z4 finding). **⟹ the W20
honest condition (i) (the flat gauge) is DISCHARGED.**

**THE HOMOLOGY OUTCOME (the decisive fact): the [1,3,3,1] t₂ pattern
SURVIVES the κ-attachment UNCHANGED** (t₂ = [0,…,0,1,3,3,1,0,0] at
degrees 7–10; |H₉(B;ℤ/4)| = 2^178 with L−2b₉ = 6 — all six summands
ℤ/2's, no ℤ/4; all odd-primary torsion zero) **while b₉ halves
178 → 86** (the completion killed 92 FREE classes but NOT the torsion).
The decomposition battery (six removal tests, all d̄² = 0 PASS): the
s-/{s,C,P}/F-removals leave t₂(9) = 3; the {s,w}-, {s,w,K}- and
{s,w,K,T,Q}-removals all collapse it 3 → 0 — the layer is carried by
the FULL cascade chain s→w→κ→τ. **The levels 2 and 3 agree EXACTLY
(the level-crossing certificate: identical Betti, identical t₂,
identical |H₉(ℤ/4)| = 2^178; the battery reads match).**

---

## 1. The exact combinatorial layer (Part A)

The wall equations s_k^{(ij)} = Σ_{l≠k} s_l^{(ij)} force the
pair-phase differences θ_il − θ_jl ≡ ψ^{(ij)} + π·[l ∈ T^{(ij)}] with
T^{(ij)} ∈ {{k}, [4]∖{k}} — 2 choices per wall. The T-assignment
prover enumerates all 2^m assignments and checks (i) the
cycle-consistency (the indicator sums constant in l on every
fundamental cycle of the pair-graph — the ψ's absorb the constants)
and (ii) the non-wall pairs' closability (the path-sum patterns mixed;
1-vs-3 = a forced extra wall; all-equal = infeasible). Machine
verdicts over the full candidate tree:

| layer | candidates | infeasible-exact | compatible | forced |
|---|---|---|---|---|
| m = 2 (corners) | 276 | 84 (36 same-pair + 48 same-k) | 192 | 0 |
| m = 3 (triples) | 1280 | 752 | 96 (the stars) | 432 (the paths) |
| m = 4 (quads) | 3840 | 3732 | 108 → 72 | 0 |
| m = 5 | 6144 | 6144 | 0 | 0 |
| m = 6 | 4096 | 4096 (Turán) | 0 | 0 |

**THE THEOREMS (each machine-proved by the exhaustive enumeration; the
alternating-quad theorem by the product-identity derivation):** the
triangle obstruction (the generalization of the W17 same-pair sympy
theorem); the same-k corner infeasibility; the path-forcing (the
distance-3 pair's closure forces the 4th wall); the star distinct-k
requirement; the balanced-k condition; the alternating-quad emptiness
(the four one-term bounds' product is an identity on the eight
a/b-column entries ⟹ every bound tight ⟹ the non-wall column terms
vanish ⟹ no positive-entry solution). **The wall-cascade below κ is
FINITE and SHALLOW: κ (m=2) → the star-triples τ (m=3) → the
all-distinct C₄-quads q (m=4) → the support descent (the (c)-scope).**
The incidence: each of the 144 shared-diff-k corners has exactly 2
star-faces; each star has 3 corner-faces (288 = 96×3) — the
"each-corner-in-exactly-2-seams" parity gate one level down, and the
d² = 0 of the κ→τ layer is automatic (the interval structure).

## 2. The witness census (Part B)

* **the 36 disjoint diff-k corners:** the CKM-chain solve (the 9 chain
  parameters, the wall equations to 1e-12, the chain IS a unitary —
  completions automatic): the class representative W(0,1|0)×W(2,3|1)
  witnessed (min entry 1.3e-3); the S₄×S₄ relabeling orbit covers the
  class [cert]. (The W17 real sampler could not reach these: the
  real-slice F-structure forbids them — the complex phases free the
  cross-pairs. The chain solves what the real GS cannot.)
* **the 96 stars:** REAL-ORTHOGONAL witnesses (the row-pair
  orthogonality IS the wall equation: min entry 2.6e-4, the walls
  exact) [cert].
* **the 72 all-distinct quads:** REAL-ORTHOGONAL witnesses [cert].
* **the 36 alternating quads:** REMOVED (the exact theorem: the pure
  strata EMPTY).
* **the 12 same-k disjoint corners:** UNRESOLVED (300 seeded chain
  starts: the degenerate-collapse evidence; kept per the W20-B
  precedent, honestly labeled).

## 3. The drift-monodromy lift (Part C — the P-19 consumption)

The W20 §7(i) worry ("the drift monodromies of the F→z=2→z=3→z=4
corners are unmodelled") is discharged in three layers: **(1) the
monodromy-carrier census** — the fibre-degeneration loci of the
T³-fibration Fl₄→M₄ are E (dim 1, codim 8) and V (dim 0, codim 9):
codim ≥ 3 removals preserve π₁, so no loop in the base can link them
(the qutrit's E-strata were codim 3 — linkable — the source of the 13C
E-edge windings; the ququart's dimensional luck kills the analog); the
wall and support strata are one-sided in the moduli (no loops); the
only π₁ carriers are the non-unistochastic pockets (the W16 interior
holes — the (c)-scope). **(2) THE LEFT-EQUIVARIANCE CERTIFICATE:**
polar(t₀·M) = t₀·polar(M) machine-exact (200/200 random tests) — the
rescale-polar moduli-tracking lift is left-torus-equivariant, so the
transport t·[u] ↦ t·[u′] holds identically along any path it tracks.
THE QUTRIT CONTRAST: the 13C transport was NOT equivariant (the phased
c₃, the t₀² fibre offsets, the gauge g); the ququart's c₄-purity (the
W17 §5.4 certificate) + the equivariant lift IS the structural
difference — the flat gauge is not merely defensible, it is REALIZED.
**(3) the two-frame spot-checks:** the 5 P-19 interface classes
(F→z2 same-row/same-col/rook; z2→z3 L-shape/diagonal) via the polar
interpolation: drift L·t₀⁻¹ = (0,0,0) to machine precision at every
class [FLAT]. The z3→z4 interface is EMPTY (the W19 floating-z4
finding: the feasible z4's have no feasible z3-parents — the support
cascade's censused chain ends at z3; the z ≥ 5/E/V completion is the
(c)-scope). **⟹ the codim-2 corner prism terms P_v(f) = 0 CONFIRMED;
the W20 honest condition (i) DISCHARGED.**

## 4. The assembly (Part D) + the battery

The corrected book: 932 strata (V24 E72 F16 Z2-120 Z3-240 Z4-72 W24
**K192 T96 Q72** C P s4 s8) × the level-L fibres (pt/S¹/T³, the flat
canonical gauge): 53,816 cells at L=2 / 180,672 at L=3. The census
gates: χ = 24 = |S₄| = χ(Fl₄) and the orbit χ = 6 = χ(B₄) EXACT. **The
extended seam battery:** the W20 sign system (the s→w/C/P and w→κ
corner signs) re-solved over the filtered 192-corners + the NEW κ→τ
sign layer (288 variables): **1,380 equations, CONSISTENT, 83 free
sign-gauges** — the battery closes one level deeper than W20 (which
itself closed one level deeper than the 13C's Z/2 obstruction). G2:
d² = 0 EXACT (integral, all cells). The T-map (the c4-action with the
W20 anchors + the 36 E-flip compensators): G4 T⁴ = id, G4b dT = Td
(0 mismatches — the τ/q cells at TSGN = +1, no flips needed). G6:
d̄² = 0 on the orbit complex. The P-19 cross-check: the
wave19_ckmtrace_data.json middle-lattice re-verified (the gates
C3/C6/d23dF, the 15 faces per F).

## 5. THE DEGREE-9 EXAMINATION (Part E) + the battery (Part F)

* **the Betti** (two large primes): b = (1, 34, 81, 123, 201, 230,
  214, 188, 141, **86**, 32, 4, 1) — IDENTICAL at L=2 and L=3 (the
  level-crossing certificate). b₉ = 86 (vs the W20's 178: the
  κ-attachment killed 92 free classes).
* **the mod-p ladder:** ALL odd-primary torsion ZERO; **t₂ =
  (0,…,0,1,3,3,1,0,0)** at degrees 7–10 — THE SAME [1,3,3,1] PATTERN
  AS W20: the (ℤ/2)⊗H*(T³;ℤ) Künneth signature of ONE degree-7
  wrapping generator.
* **the exact ℤ/4 route:** |H₉(B;ℤ/4)| = 2^178 exactly; L − 2b₉ = 6 =
  the theoretical minimum ⟹ all six 2-primary summands (3 at H₉, 3 at
  H₈) are ℤ/2's, no ℤ/4.
* **the decomposition battery** (all d̄² = 0 PASS): T1 {s}, T2
  {s,C,P}, T3 {F}: t₂(9) = 3 (unchanged); T4 {s,w}, T5 {s,w,K}, T6
  {s,w,K,T,Q}: t₂(9) = 0 — the whole layer is carried by the FULL
  cascade chain; the removal of ANY link kills it.

## 6. THE VERDICT: RE-OPENED (the W20 conditional FALSE is UN-HARDENED)

The W20 §7 criterion: the Stage-4b completion (a)+(b) was supposed
either to DISSOLVE the κ-wrapping artifacts (→ FALSE hardens) or to
re-introduce a genuine ℤ/2 (→ re-open). **THE OUTCOME: NEITHER — the
[1,3,3,1] pattern SURVIVES the κ-attachment UNCHANGED while b₉ halves:
the W20 artifact-mechanism (the terminal-κ wrapping dissolving with
the true boundaries) is REFUTED — the classes persist through the
censused cascade.** ⟹ P-δ₁ RE-OPENS the other way: the degree-9
2-primary classes are now persistent candidates; per the W18
PD-mirror at most ONE of the three is genuine; the decisive remaining
test is the **(c)-scope: the support-descent completion below the τ/q
cells (the new truncation frontier) + the E/V connections**. The flat
gauge (i) is DISCHARGED (Part C); the wall-cascade (ii-a) is censused
and attached; the honest conditions are now (ii-c) and (iii) the
levels (2 and 3 agree; the level-4 not run).

## 7. Scoreboard

* **δ₁ (ququart): OPEN, re-opened from the W20 conditional-FALSE —
  the primary-obstruction route REVIVED-conditional** (the persistent
  [1,3,3,1] layer: at most one genuine per the PD-mirror; the
  (c)-scope decisive); the bracket [4/3, 3/2] unaffected; the
  secondary-obstruction route (H⁴(B₄;ℤ)) remains open either way.
* **δ₂ (qutrit): 4/3, machine-certified** — untouched (H₂(B₃) = ℤ/3).
* Manuscripts untouched.

**Nothing here reopens the qutrit verdict: H₂(B₃) = ℤ/3, δ₂ = 4/3.**
