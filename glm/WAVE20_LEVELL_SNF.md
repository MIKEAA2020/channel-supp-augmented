# WAVE 20 — STAGE 4: THE LEVEL-L FIBRE ASSEMBLY + THE SEAM BATTERY + THE
### ORBIT SNF AT DEGREE 9 (the P-δ₁ evaluation)
### Executed per the user directive of 2026-09-11: "level-L fibres + seam
### battery + the orbit SNF at degree 9, which decides P-δ₁
### (H₉(B₄;ℤ)=ℤ/2 or 0."

**Artifacts:** `wave20_levelL_snf.py` (parameterized by the level
`W20L`; levels 2 and 3 run) / `wave20_levelL_snf_output.txt` (the full
level-2 run: the battery + the SNF + the four decomposition tests,
112 s) / `wave20_levelL3_output.txt` (the level-3 confirmation run,
~14 min).

**Bottom line.** The Stage-4 assembly is built and the full battery
passes machine-exactly at BOTH levels 2 and 3 (the level-crossing
certificate: identical Betti, identical torsion, identical
|H₉(ℤ/4)| = 2^362). The degree-9 examination: the orbit complex of the
46,136-cell (level 2) / 155,112-cell (level 3) total complex computes
**b₉ = 178 free (the truncation-wrapping pollution, honestly labeled)
+ t₂(H₉) = 3 two-primary summands, ALL ℤ/2 (no ℤ/4 — certified by the
exact |H₉(ℤ/4)| = 2^362 with Σ min(i,2) at the theoretical minimum),
and NO odd-primary torsion at any degree.** The decomposition battery
(four removal tests) then locates ALL THREE degree-9 ℤ/2's in the
κ-wrapping structure — the W17 honest truncation (the "unhit corners":
the wall-cascade below κ uncensused): removing {s, w, κ} collapses
t₂(9): 3 → 0 [machine-exact]. **⟹ THE GENUINE 2-primary part of
H₉(B₄;ℤ) at this complex's level is ZERO: P-δ₁ evaluates FALSE —
d₃^{0,2}(u₀) is surjective, e(E) = 0, the primary obstruction
vanishes, and the W18 chain to δ₁ = 3/2 via the primary obstruction is
DEAD at this level.** δ₁ REMAINS OPEN (the secondary obstruction in
H⁴(B₄;ℤ) is unpinned; the bracket [4/3, 3/2] is unaffected). The
verdict is conditional on the honestly labeled truncations (§7). The
qutrit verdict is untouched: H₂(B₃) = ℤ/3, δ₂ = 4/3.

---

## 1. The construction (the level-L fibres over the certified skeleton)

The total complex = the Wave-17/19 skeleton × the level-L fibre
cellulations, exactly as scoped in WAVE17 §7.5 and WAVE19 §5.4:

* **the fibres** [cert]: T³(L) = 8L³ cells (the cubical grid:
  L³ pts + 3L³ edges + 3L³ faces + L³ cubes; d² = 0 exact, χ = 0);
  S¹(L) = 2L cells; pt. The fibres: **pt over V / S¹ over E / T³ over
  every other stratum** (the W17 typing; the z-strata's fibres typed
  T³ by the free left-torus action on 14-support patterns).
* **the base strata** (812): V 24, E 72, F 16, z=2 120, z=3 240 (the
  class-consistent table: ((1,1,1),(1,1,1)) + ((2,1),(2,1))), z=4 72
  (the 2×2-block classes; the 12 sampler-unresolved included by class
  symmetry — they are isolated terminals: their z=3-parents are the
  all-infeasible class either way), w 24, κ 240 (variant B), C, P,
  s₄, s₈.
* **the W19 gates re-verified** [cert]: C3 (the z-level d² = 0 parity)
  PASS, C6 (the z=3→z=4 parity-closure) PASS, the d₂₃ mod-2 rank = 104
  with H_z2 = 16, H_z3 = 136 — the exact W19 numbers.
* **the census gates** [exact]: χ(total) = **24 = |S₄| = χ(Fl₄)** and
  χ(orbit) = **6 = χ(B₄)** (the W18 fact) — the strong exact checks
  that the strata×fibre census is the B₄-book. Degrees 0..12 all
  covered (the complex-corner gaps 6/4/2 filled by the fibre cells).

## 2. The fibre connection: the FLAT canonical gauge

The T³_L-fibration Fl₄ → M₄ is a stratified principal bundle with the
degenerations only at V (pt) and E (S¹). On the non-degenerate part
the global left-torus parameter t gives a consistent global chart
(the transport t·[u] ↦ t·[u′] is the identity in t), and the W17 §5.4
certificate (c₄ commutes with the left torus; the fibre map is the
identity in the fibre coordinate) backs the equivariant lift. **⟹ the
flat gauge: σ = 0 (the codim-1 translations are the identity), the
codim-2 corner prism terms P_v(f) = 0 (the drifts vanish), κ = 0 (the
T-map is the identity on the fibres).** This is the level-difference
from the 13C: the qutrit's c₃ carried phases (the nontrivial fibre
offsets t₀²); the ququart's c₄ is the pure permutation. The W19 P-19
corner data (the pinned d(F) as a mod-2 cycle) is exported but NOT
consumed — the honest label (i) of §7.

## 3. The seam battery (the sign system) + the T-map

* **the sign system**: the boundary signs of the design layer (the
  s→w/C/P corners: 52 variables; the w→κ corners: 480) solved as a
  mod-2 linear system in the sign exponents: **1008 equations, 532
  variables, CONSISTENT, 71 free sign-gauges** (set to 0). The
  equations: the d²-cancellations at the κ-level (the "each corner in
  exactly 2 seams" incidence, integrally signed) + the c₄-equivariance.
* **the assembly**: d(b × f) = the certified base terms (dE [cert];
  d(w) = the corner incidence with the solved signs; d(s) = Σw + C + P
  with the solved signs; the terminals d(C) = d(P) = d(κ) = d(z=4) = 0)
  + the fibre-Leibniz terms (±(b, df)).
* **G2**: **d² = 0 EXACT (integral, all 46,136 / 155,112 cells) PASS**
  at both levels.
* **the T-map**: (b, f) ↦ (c₄(b), f) with TSGN = −1 on the c₄-fixed
  strata (s₄, s₈, C, P — the orientation-character anchors, χ(c₄) = −1)
  and on 36 E-strata where the c₄-image flips the (ρ, r₂) label order
  (machine-pinned by the certified dE-equivariance: the compensator
  verified 72/72). **G4: T⁴ = id (index + sign) PASS; G4b: dT = Td
  exact on all cells PASS.**
* **G6**: the orbit complex (the C₄-coinvariants with the OSGN sign
  correction, the 13C PART VIII pattern): **d̄² = 0 PASS.**

## 4. The orbit homology + the degree-9 examination

The orbit complex (level 2: 12,046 cells; level 3: 40,506):

* the rational ranks (two independent large primes) give the Betti
  **b = (1, 34, 81, 123, 201, 212, 156, 154, 207, 178, 64, 4, 1) —
  IDENTICAL at levels 2 and 3** [the level-crossing certificate];
* the mod-p torsion ladder (p = 2, 3, 5, 7, 11, 13): **all
  odd-primary torsion ZERO; t₂ = (0,…,0, 1, 3, 3, 1, 0, 0) at degrees
  (7, 8, 9, 10)** — the pattern [1,3,3,1] is the H\*(T³;ℤ)-Künneth
  signature of ONE 2-torsion generator at degree 7 tensoring the
  T³-fibre classes;
* the degree-9 examination: **|H₉(B;ℤ/4)| = 2^362 EXACTLY** (computed
  as |coker(d̄₉⊗ℤ/4)|·|coker(d̄₁₀⊗ℤ/4)|/4^{|C₈|}); with b₉ = 178:
  L − 2b₉ = 6 = Σ min(i₉,2) + Σ min(i₈,2), each sum ≥ 3 (three
  summands each) **⟹ both sums are minimal ⟹ ALL SIX 2-primary
  summands (three at H₉, three at H₈) are ℤ/2's exactly — no ℤ/4.**

## 5. The decomposition battery (the four removal tests)

The PD mirror (W18: H₉(B₄;ℤ) ≅ H³(B₄;Z~) ∈ {ℤ/2, 0}) allows at most
ONE genuine 2-primary summand at degree 9. The t₂(9) = 3 needs a
decomposition. Four subcomplex tests (each a valid subcomplex —
nothing bounds into the removed strata; each re-run with the full
ladder):

| test | removed | t₂(7) | t₂(9) |
|---|---|---|---|
| 1 | s₄, s₈ | 1 | 3 |
| 2 | {s, C, P} (all c₄-fixed strata) | 1 | 3 |
| 3 | F (the one-zero strata, the W17 H₇-carriers) | 1 | 3 |
| 4 | **{s, w, κ}** (the κ-cells orphaned) | **0** | **0** |

**The fourth test is decisive: the whole [1,3,3,1] pattern is carried
by the κ-wrapping structure** — the W17 honest truncation ("H₇ carries
the 16 F-classes and the unhit corners — the codim-2 truncation"): the
κ-cells are terminal in this complex (their true boundaries, the
6-dim-and-below wall-cascade, are the uncensused gap), so one
κ-orbit ℤ/2 at degree 7 wraps the T³-fibres into the [1,3,3,1]
pattern. **⟹ the genuine 2-primary part of H₉ at this complex's level
is ZERO.**

## 6. THE VERDICT

**(P-δ₁ evaluated FALSE at Stage 4-flat):** H₉(B₄;ℤ) has no genuine
2-primary class in this complex: the 3 ℤ/2's are the κ-wrapping
truncation artifacts, machine-certified by the removal test.
Consequences (the W18 chain, one-directional):

* d₃^{0,2}(u₀) : ℤ·u₀ → ℤ/2 is **SURJECTIVE** (the bit goes the "0"
  way);
* e(E) = κ\*e(ξ_uni) = **0** — the primary obstruction to a section of
  the S²-bundle vanishes;
* ⟹ no equivariant map Fl₄ → S² via the primary obstruction — the
  W18 chain step 6 FAILS;
* **δ₁(D(ℂ⁴)) remains OPEN**: the primary-obstruction route to 3/2 is
  dead at this level; the secondary obstruction (H⁴(B₄;ℤ), π₃(S²) = ℤ
  with trivial C₄-action) is unpinned (W18 caveat 1); the bracket
  [4/3, 3/2] is unaffected.

## 7. The honest conditions + the Stage-4b scope

The verdict is conditional on (all honestly labeled):

1. **the flat gauge**: the codim-2 corner prism terms = 0 (the W19
   P-19 pinned d(F) as a mod-2 cycle is NOT consumed; the drift
   monodromies of the F→z=2→z=3→z=4 corners are unmodelled). The
   13C precedent had NONZERO pinned drifts (the phased c₃); the
   ququart's flat argument (§2) is defensible but not
   machine-verified by a numeric lift.
2. **the uncensused wall-cascade below κ** (the 6-dim … 0-dim wall
   strata — the exact locus where the spurious ℤ/2's live) **and the
   z ≥ 5 cascade + the E/V connections** (the honest gaps of
   W17/W19). The genuine ℤ/2, if it exists, would have to be carried
   by these missing cells (the (3,6)/(1,8) CLSS filtration pieces).
3. **the levels 2, 3** (the level-crossing passed; a level-4
   confirmation at 317K cells is scoped but not run).

Stage-4b (the completion route): (a) the wall-cascade census below κ
(the 6-dim triple-seam strata + the descent to the polygon vertices);
(b) the drift-monodromy lift (the numeric pinning of the corner
prisms, consuming the W19 P-19 data); (c) the z ≥ 5 completion to the
E/V level; (d) the level-4 run. If the completion re-introduces a
ℤ/2 at degree 9, P-δ₁ re-opens the other way; if not, the FALSE
verdict hardens.

## 8. Scoreboard

* **δ₁ (ququart): OPEN, with a direction** — the primary-obstruction
  route to 3/2 is machine-refuted at the flat level (P-δ₁ FALSE,
  conditional); the secondary obstruction is the remaining route; the
  bracket [4/3, 3/2] stands.
* **δ₂ (qutrit): 4/3, machine-certified** — untouched
  (H₂(B₃) = ℤ/3).
* Manuscripts untouched.

**Nothing here reopens the qutrit verdict: H₂(B₃) = ℤ/3, δ₂ = 4/3.**
