# WAVE 23 — STAGE 5: THE 4-SKELETON SECONDARY-OBSTRUCTION CONSTRUCTION
### + THE PRIMARY'S ORBIT-LEVEL DECISION + THE LEVEL-4 CROSS-CHECK
### Executed per the user directive of 2026-09-12: "the 4-skeleton
### secondary-obstruction construction, the primary's orbit-level decision,
### and the level-4 cross-check."

**Artifacts:** `wave23_stage5.py` (Parts 0/A–D; ~40 s at L=2, the W21
certified assembly core recovered verbatim with every gate re-verified) /
`wave23_stage5_output.txt` (L=2) / `wave23_stage5_output_L3.txt` (the
level-3 confirmation) / `wave23_stage5_data.json` /
`wave23_level4.py` (Part C) / `wave23_level4_output.txt` /
`wave23_level4_data.json`.

**Bottom line.** ALL THREE STAGE-5 DELIVERABLES, and the outcome is a
STRUCTURAL DOUBLE-BLOCKADE that pins the shape of everything the
certified complex can and cannot decide. **(a) THE 4-SKELETON
SECONDARY-OBSTRUCTION CONSTRUCTION:** the S²-fibre cocycle model built
over the certified 4-skeleton — the Z~ local system
(χ(c₄) = −1 = the fibre-orientation = B₄'s own orientation character)
realized as the twisted coinvariant complex, with a genuine
CONVENTION THEOREM discovered by machine search: the transition-position
twist (−1)^{t(j)} is INCONSISTENT (d_tw² ≠ 0), and the unique consistent
nontrivial harmonization is the ORBIT-SIZE twist (χ restricted through
the stabilizer structure: χ(c₄²) = +1 forces the size-2 orbits to carry
+1; the size-1 fixed cells carry the twist through the TSGN = −1
anchors) — the local-system certificate d_tw² = 0 PASSES. THE
STRUCTURAL THEOREM (the secondary): the c₄ cocycle condition is VACUOUS
on the whole certified complex (the 4-skeleton has no 5-cells; the full
complex's 5-cells — the Z2/q P-cells — carry fibre faces only: the W19
parity barrier), and every 4-cell is a free-region cell, so the
self-gauge lattice L⁴ IS C⁴: **G⁴ = 0: the secondary obstruction's
INVARIANT CONTENT on the certified complex is STRUCTURALLY ZERO.**
**(b) THE PRIMARY'S ORBIT-LEVEL DECISION:** H³(B^orb;Z~) = Z¹²³ ⊕ 0
(no 2-torsion slot at all — the e-class's Z/2 target is EMPTY on the
complex), and the gauge quotient: every 3-cell is a free-region cell
(984/984: the excised base faces), so the self-gauge lattice L³ IS the
full cocycle lattice: **G³ = 0: the e-class CANNOT BE CARRIED — the
certified complex has no invariant degree-3 obstruction content (the
W19 parity excisions removed the carriers).** **(c) THE LEVEL-4
CROSS-CHECK:** the L=4 assembly (428,632 cells) through the same
certified code path with the FULL G2 gate, the subdivision certificates
(π∘S = the multiplicity diagonal, d₄∘S = S∘d₂, d₂∘π = π∘d₄, S
T-equivariant — all PASS), and the DIRECT machine ladders: the FULL
mod-2 rank ladder (degrees 1..12) L2 = L4 EXACT, the mod-2 homology
dims EQUAL, the t₂ ladder EQUALS the certified W21 read — **the
level-crossing certificate EXTENDED TO LEVEL 4 [cert].**

---

## 1. The S²-fibre cocycle model (Part A): the convention theorem

The certified 4-skeleton: the 3,342 orbit cells of degree ≤ 4
([6, 204, 540, 984, 1608]), the degree filtration (a genuine
subcomplex: G6sk PASS). The bundle data: the fibre action
R~ = diag(R_{π/2}, −1)|_{S(V)}: det = −1 (the Z~ twist on π₂);
deg(R~)² = +1 (π₃(S²) = Z carries the TRIVIAL action — the secondary's
slot, the W18/W22 premise re-derived machine-exactly).

The twisted coinvariant complex: face j ↦ OSGN[j]·ε(j)·e_{ORB[j]}.
Machine search over the harmonization ε:
* ε = (−1)^{t(j)} (the transition position — the textbook tensor
  C⊗_{Z[C₄]}Z~ derivation): **INCONSISTENT** — 2,304 residuals, all in
  the (deg 10–12, S→W) compositions (the ±8 patterns);
* ε = 1 (the untwisted): PASS (the W21's G6);
* **ε = the orbit-size twist** (size-4 → +1, size-2/1 → −1): **PASS —
  THE CONVENTION THEOREM**: the character χ: C₄ → ±1 with χ(c₄²) = +1
  must be constant on the free orbits and is forced nontrivial only
  through the stabilizer cells (the 256 fixed cells carry the TSGN = −1
  anchors; the 1,280 size-2 cells carry the −1). The local-system
  certificate d_tw² = 0 PASSES (the G6tw battery) — the unique
  consistent nontrivial local-system realization on the certified
  complex.

**The twisted ladders** (the convention-C complex): b(Z~) =
(1, 34, 81, 123, 201, 230, 214, 188, 141, 86, 32, 4, 1), t₂(Z~) =
[0,0,0,0,0,0,0,1,3,3,1,0,0] — IDENTICAL to the untwisted reads (the
honest convention note: the complex's 1-skeleton is entirely
free-orbit, so the orientation character is invisible at H₀ — the true
B₄ would read the Z/2-monodromy; the complex's connectivity cannot see
it).

## 2. The freedom census (A.5): the W19 excision structure

Machine-verified from the re-derived middle lattice: NO feasible z3 is
strictly inside a feasible z4, and NO feasible z4 has a feasible z3
parent (the floating-z4 + the all-infeasible parent class) — so every
Z3/Z4-stratum cell's BASE faces lie in exactly-infeasible (excised)
strata. THE CENSUS: **984/984 3-cells and 1608/1608 4-cells are
Z3/Z4-stratum cells whose boundary spheres carry FREE REGIONS** (the
base faces excised; only the fibre faces glued). The 5-cells: {Z2:
256, Z3: 1440, Q: 144} — all with un-wired base faces (the W19 parity
barrier: the z2→z3 integral boundaries are exactly the
parity-impossible layer).

## 3. The gauge quotients (A.6): the primary's invariant content

On a partial (excised-face) complex the obstruction cocycle's values on
the free-region cells are GAUGE DATA: the winding choices on the
excised faces shift c₃(σ) by arbitrary integers, constrained only by
the cocycle preservation δc₃ = 0 (the machine-built constraint system
ML3: 1,608 equations × 984 gauges, rank 567). The invariant group:

G³ = ker(δ³~)/(im(δ²~) + L³), L³ = the self-gauge lattice.

**THE MACHINE READS:** dim_F2 ker(δ³~) = 417; dim(im δ²~ + L³) = 417
(the mod-2 computation: ker = im + L³ EXACTLY); and the structural
fact: since every 3-cell is a free-region cell, ML3 IS the full δ³
matrix, so **L³ = ker(δ³) = the cocycle lattice itself: G³ = 0
STRUCTURALLY** (free rank 0, no torsion, the mod-2 dim 0). The
e-class's invariant content on the certified 4-skeleton: **ZERO.**

## 4. The structural theorem (A.7): the secondary's invariant content

The c₄ cocycle condition δc₄ = 0 requires the 5-cells' boundary
relations. THE CENSUS: the 4-skeleton has NO 5-cells; the FULL
complex's 5-cells (the Z2/q P-cells + the Z3 fibre-cells) carry FIBRE
faces only (1,440/1,840 have degree-4 boundary faces — all fibre
terms; none carries base faces: the W19 parity barrier). And every
4-cell is a free-region cell (L⁴ = C⁴ unrestricted — there are no
5-cell relations to constrain the self-gauges). **THEOREM: G⁴ = 0 —
the secondary obstruction's invariant content on the certified complex
is STRUCTURALLY ZERO. The o₄ decision requires exactly the structure
the certified book cannot carry: the 5-skeleton's integral z2→z3
boundaries are the W19 parity-impossible layer.**

## 5. The primary's orbit-level decision (Part B)

* **THE GROUP:** H³(B^orb;Z~) = Z¹²³ ⊕ 0 — the 2-torsion slot is EMPTY
  (the e-class's Z/2 target: the W18 form-4 group would be 0-or-Z/2 on
  the true B₄; the complex reads NO torsion at all, only the free
  truncation pollution).
* **THE INVARIANT CONTENT:** dim_F2 G³ = 0, free = 0.
* **THE DECISION: the e-class CANNOT-BE-CARRIED** — the certified
  complex has no invariant degree-3 obstruction content: the W19 parity
  excisions removed the carriers. The primary route is UNDECIDABLE at
  this level (not killed: the excision structure removed the invariant
  slot itself; the honest conditional labels — the flat gauge, the
  truncation structure — all standing).

## 6. The level-4 cross-check (Part C, wave23_level4.py)

* The L=4 assembly through the same certified code path: 428,632
  cells, χ = 24, the FULL G2 d² = 0 gate PASS.
* The subdivision certificates: S: C(L2) → C(L4) (the cubical ×2
  refinement along each cell's own directions: P→1, X/Y/Z→2,
  XY/XZ/YZ→4, Q→8 children, all +1) and π: C(L4) → C(L2) (the
  aggregation): **π∘S = the multiplicity diagonal (S injective over
  Z) — PASS on all 53,816 cells; d₄∘S = S∘d₂ (the subdivision
  commutation) — PASS; d₂∘π = π∘d₄ (the aggregation commutation) —
  PASS; S is T-EQUIVARIANT (fibre-only vs base-only) — PASS on all
  cells.**
* **THE DIRECT MACHINE LADDERS** (not just the structural argument):
  the FULL mod-2 orbit rank ladder (degrees 1..12): **L2 = L4 EXACT**;
  the mod-2 homology dims H_k(F₂): **EQUAL at every degree**; the t₂
  ladder recomputed from the L4 mod-2 dims + the certified Betti:
  **EQUALS the W21 certified read** — the [1,3,3,1] 2-primary window
  and the whole t₂ ladder survive the level-4 refinement IDENTICALLY.
  The rational spot ranks (degrees 1–4, 8–10, the large prime): L2 =
  L4 EXACT.
* **VERDICT: the W21 level condition (iii) DISCHARGED** — the levels
  2/3/4 agree; the conditional structure of the W20/W21/W22 verdicts
  now rests on the truncation conditions alone.

## 7. Scoreboard

* **δ₁ (ququart): OPEN — the Stage-5 structure pinned: BOTH obstruction
  routes are DOUBLY-BLOCKED on the certified complex:** the primary's
  degree-3 slot carries NO invariant content (G³ = 0: the excisions
  removed the carriers; H³(B^orb;Z~) has no 2-torsion at all), and the
  secondary's degree-4 slot is structurally zero (G⁴ = 0: the c₄
  cocycle condition is vacuous — the 5-skeleton's integral boundaries
  are the W19 parity-impossible layer). The W22 "ALIVE-BUT-INVISIBLE"
  secondary is upgraded to "ALIVE-BUT-UNREACHABLE-ON-THE-CERTIFIED-
  COMPLEX"; the primary joins it. The bracket [4/3, 3/2] intact; the
  next-frontier scope: structures beyond the certified book (the true
  B₄'s 4-skeleton — unavailable — or new machinery: the mod-2 secondary
  operations, the CLSS d₃-transgression, the cup-product route whose
  z-cell vertex structure is exactly the excised layer).
* **The level conditions: DISCHARGED (2/3/4 identical, [cert]).**
* **δ₂ (qutrit): 4/3, machine-certified — untouched (H₂(B₃) = ℤ/3).**
* Manuscripts untouched.

**Nothing here reopens the qutrit verdict: H₂(B₃) = ℤ/3, δ₂ = 4/3.**
