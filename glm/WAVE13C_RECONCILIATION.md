# WAVE 13C — CROSS-LINE RECONCILIATION NOTE: the two lines converge on the
# same boundary stratification
### Artifacts: this note; `wave13c_h34.py` / `wave13c_h34_output.txt`
### (13C-8: the c4/c5/c6 ℤ/9-smith pinning the H₃/H₄ exponents + the extended
### torsion-prime scan + the full-battery re-certification on import).
### Executed per the user directive of 2026-09-10: (1) cross-line
### reconciliation note, (2) fix the H₃/H₄ exponents, (3) remaining tasks /
### open problems / audit points.

**Bottom line.** The two agent lines that ran in parallel on the corrected
base U₃ — the **14H line** (H-top/H-glue/H-signs/H-facet audit; sampling +
digital cubical topology) and the **13B/13C line** (the honest machine
cellulation → battery → orbit SNF) — *contradicted each other on the F-cells*
at 14H time ("no 2-dimensional facet locus in B₃" vs "9 F-cells, all
feasible"). After the 13C-4 adjudication both lines stand on **one boundary
stratification**, and that stratification now carries a fully certified
machine complex: the 13C-7 battery ALL-PASS, re-certified from scratch by
13C-8, with every homology slot of B₃ machine-pinned. The qutrit bit is
closed on it: **H₂(B₃) = ℤ/3, δ₂(D(ℂ³)) = 4/3.**

---

## 0. The two lines (identification, lineage, methods)

| | **Line 14H** (commits `70da0b5`, `13d0c41`, `5305b79`) | **Line 13B/13C** (commits `f572192`, `ab58ec9`, `15b7bcd`, `9abae08`, `1d5e18a`, `da39342`) |
|---|---|---|
| object | U₃ = {Q ≥ 0} ∩ B₃ directly, in the chart box | M = double(U₃) = Fl₃/T³_L, the two-sheet book, then the full 14 910-cell Fl₃-complex |
| method | Monte-Carlo sampling (300k pts/facet), digital cubical complexes (grids n = 24/32/40), exact arithmetic on the skeleton | exact integer chain complexes, constraint-system solving (mod 12), certified boundary/T-map, orbit coinvariants + SNF |
| output | χ(U₃)=1, χ(∂U₃)=0, face lattice of B₃, wall σ-classes, four boxed H-items | G0 base book (S⁴), fibre pins, level-12 rebuild, seam gauging, G1–G8 + d̄²=0, H₋(B₃) |

Both lines descend from the shared Wave-12 discovery (U₃ = the unistochastic
region; the Birkhoff-face-lattice base infeasible — Wave 11's root cause) and
were kept deliberately independent (separate namespaces `wave14h_*` vs
`wave13b_*`/`wave13c_*`; nothing of either line was reverted).

## 1. The disagreement as it stood (14H §6 "open tension")

* **F-cells.** 14H's facet survey: 300 000 samples per facet, Q > 0 at *no*
  sample → "U₃ ∩ facet = the four T-edges (1-dimensional)"; ∂U₃ ∩ ∂B₃ is a
  1-complex, **no 2-cells**. The 13B book: **9 F-cells (5 pure + 4 mixed)**,
  2-dimensional, claimed feasible. 14H proposed the resolution "their F-cells
  live only on the double M" and explicitly asked for adjudication against
  the d(F) construction.
* **Wall structure.** 13B's "9 walls W(i,j|k)" vs 14H's single hypersurface
  {Q = 0} with 6 clopen σ-classes (Q₁₂ ≡ Q₁₃ ≡ Q₂₃ exactly).
* **Euler bookkeeping.** 14H's would-be σ-stratification complex
  1 − 6 + 0 − 9 + 6 = −8 ≠ χ(U₃) = 1 ("not a cell decomposition").
* Both lines agreed: no single-degenerate wall strata, the Wave-12b corner
  rule void, U₃ a 4-ball, 2-to-1 Jarlskog sheets, δ₂(qutrit) OPEN.

## 2. The adjudication (13C-4, `WAVE13C_ADJUDICATION.md`)

Machine-exact, both directions:

* **His §4 claim is REFUTED as a measure-zero sampling artifact.** On every
  facet Q = −(A−C)² (his own identity, machine-exact on 20 000 random facet
  points per facet), so {Q = 0} ∩ facet = {A = C} is **codimension 1 in the
  3-dimensional facet — a 2-dimensional locus**. Uniform sampling cannot see
  it (re-run: all 25 000 samples per facet have Q < 0, min ∈ [−0.0623,
  −0.0614], matching his table — the artifact reproduced on his own method).
* **The 9 F-cells ARE that locus.** 81 machine points per facet on the 13C
  FPMAP grids: D[FZERO] = 0 to 1e-12, Q = 0 to 1e-12, the other 8 entries
  strictly positive (facet interior, *not* on the T-edges), (u,v) → D
  injective — a genuine 2-parameter family.
* **d(F) adjudicates:** every d(Fᵢ) is a ±1-sum of transposition edges —
  exactly the T-edges his survey found as the Q = 0 part of each facet; the
  F-membranes span between them.
* **His residuals repaired, not relocated:** with the 9 F-cells his Euler
  −8 becomes 1 − 6 + 9 − 9 + 6 = **+1 = χ(U₃)** (and +2 for the double, the
  G0 certificate). The proposed "F-cells only on M" resolution is
  **REJECTED**: the F-loci are 2-dim in M *and* their images are 2-dim loci
  of B₃ on ∂U₃ ∩ ∂B₃. No design change.

## 3. THE CONVERGED BOUNDARY STRATIFICATION

```
∂U₃  =  6 σ-pieces   (3-dim: {Q=0} ∩ int B₃, clopen, hypotenuse bijections,
                       2 c-orbits of 3, parity-split vertex incidences)
      + 9 F-cells    (2-dim: the {Q=0} ∩ facet equality loci {A=C},
                       5 pure (4-gons) + 4 mixed (3 sides + corner blowup))
      + 9 T-edges    (1-dim: the transposition pairs; Q ≡ 0 identically)
      + 6 vertices   (0-dim)
χ(∂U₃) = 6 − 9 + 9 − 6 = 0 ✓     χ(U₃) = 1 ✓     χ(double U₃) = +2 ✓ (G0)
```

Corrections adopted from each side (both lines retracted something):

* **from 14H into the cellulation design:** the wall is ONE hypersurface with
  6 σ-pieces (13B's "9 walls W(i,j|k)" corrected — the three row-pair
  degenerations coincide); the B₃ face lattice is f = (6, 15, 18, 9) with the
  6 cyclic edges *outside* U₃ (Q = −1/16) — so the U₃ 1-skeleton is the
  9 T-edges, reconciling 13B's "9 edges" with 14H's 15-edge polytope
  skeleton; the "18 rook corners / 6 triple points" corner rule retracted
  (14H R2, 13B agreement "fictions").
* **from 13C into the stratification:** the 9 two-dimensional F-cells are
  restored (14H's "no 2-cells at this level" corrected — the sampled facet
  survey missed the measure-zero equality loci); the mixed-F corner blowups
  (required for d² = 0); the existence of a subdivision-based signed chain
  complex on exactly this stratification (14H's H-signs boxed need —
  delivered by 13C-7).

## 4. The machine arbiter: the converged stratification is *certified*, not
## merely agreed

The decisive certificate is that the 13C-7 complex built on this
stratification — 14 910 cells, degrees (6, 108, 1404, 4752, 5472, 2592, 576),
χ = +6 — passes the **full battery**, re-run from scratch by 13C-8 on the
committed data files (`wave13c_h34_output.txt`, exit clean):

```
G1 counts/χ  PASS     G2 d²=0 exact (all 14 910 cells)  PASS
G3 H(Fl₃) = (Z,0,Z²,0,Z²,0,Z), torsion-free p∈{2,3,5,7}  PASS
G4 T³=I     PASS     G5 dT=Td exact (hard-stop path)     PASS
G6 freeness PASS     G7/G7b N=0 + order-3 on H₂ (mod 7)  PASS
G8 T=+1 on H₆ (mod 7) PASS     d̄²=0 (orbit coinvariants)  PASS
```

A wrong stratification could not produce a closed orientable 6-manifold
cellulation with Fl₃'s exact homology, a free orientation-preserving C₃
action, and the free-cover identity χ(Fl₃) = 3·χ(B₃) = 6 — this is the
χ(Fl₃) recomputation 14H §5.3 explicitly requested. The G3 homology vector
matches the known Poincaré polynomial of U(3)/T³ (1 + 2t² + 2t⁴ + t⁶),
an independent external cross-check.

**13C-8 additions (this run):**

* the **c4/c5/c6 ℤ/9-smith** of the orbit complex: |coker d₄| = 3⁸⁶⁷,
  |coker d₅| = 3²³⁰³, |coker d₆| = 3¹³⁴⁶ (unit-pivot ranks 1150/672/191,
  each asserted equal to its mod-3 rank);
* the full UCT ladder |Hₖ(B₃; ℤ/9)| = **(9, 3, 9, 9, 9, 3, 9)** — exactly
  palindromic, as Poincaré duality demands;
* **exponents pinned:** e₁ = e₂ = e₃ = e₄ = 1, e₅ = 0 — H₃ = H₄ = ℤ/3
  exactly (no ℤ/9); e₄ read twice independently (|H₅(ℤ/9)| and |H₄(ℤ/9)|),
  agreeing;
* **PD cross-check ALL MATCH** (Tor H₃ = Tor H₂, Tor H₄ = Tor H₁, Tor H₅ = 0,
  free parts β₄ = β₂, β₅ = β₁) — independent of the build;
* **extended torsion scan** p ∈ {17, …, 61}: no p ≠ 3 torsion in any degree
  (hardening the finite-scan caveat; see §6 audit point A3 for what remains).

## 5. Status of the four 14H boxed items + the bit

| 14H item | status after reconciliation |
|---|---|
| H-top (U₃ ≅ B⁴) | χ(U₃)=1 at 3 resolutions (14H) + G0: double(U₃) has homology (ℤ,0,0,0,ℤ), χ=+2 (13C) — supported from both sides; the ∂U₃ ≅ S³ *proof* beyond χ+connectedness remains open (A2) |
| H-glue (T-edge link in the wall) | 14H's probes failed exactly where the wall meets ∂B₃ — on the F-membranes; the combinatorial answer is the certified d(F) (each F-membrane's boundary = the T-edge ±1-sums, G0 d²=0); σ-class *connectedness* still assumed (A1) |
| H-signs (needs a subdivision complex) | DELIVERED: the seam-augmented 14 910-cell complex, G2/G5 exact — 14H's boxed need is closed by 13C-7 |
| H-facet (facet-equality locus) | RESOLVED by the adjudication: the locus is 2-dimensional ({A=C}); both lines converged |
| δ₂(qutrit) | both lines recorded OPEN at 14H time → CLOSED by 13C-7: H₂(B₃) = ℤ/3 → WORLD 1 (CLSS d₃ = 0, x² ≠ 0 survives) → **δ₂ = 4/3 machine-certified**, re-certified 13C-8 with every slot pinned |

## 6. Remaining tasks, open problems, audit points (user ask 3)

**Remaining tasks (work, not knowledge gaps):**
1. **Ququart bit** — δ₁(ququart) = 3/2 (d = 4, Fl₄): OPEN, untouched. The
   13C pipeline (two-sheet book over the corrected base, level-L fibres,
   seam gauging if the shared-cell obstructions recur, battery, orbit SNF)
   is the template; the Fl₄ base stratification work has not started.
   The obstruction-ladder lesson transfers: expect level LCM constraints and
   per-sheet seam data, not whole-complex uniform gauges.
2. **Manuscript integration** — the synthesis/instruments papers still carry
   the pre-13C status (both bits OPEN; Manuscripts untouched throughout).
   Writing δ₂ = 4/3 as machine-certified (with the H₂(B₃) = ℤ/3 derivation
   summarized) into whichever manuscript claims it is a user decision:
   claim strength, placement, and how much of the 13C chain to include.
3. **Ledger hygiene** — the out-of-repo shared worklog ended at Wave 11;
   backfilled by this session (Waves 12a → 13C-8).

**Open problems (mathematical, boxed honestly):**
1. **σ-class connectedness** (14H §5.4): the 6 wall classes are clopen;
   that *each* is connected is sampled/assumed, not proven. The cellulation
   line does not need it (its R-cells are the bijection regions of the
   two-sheet book), but the geometric identification "σ-piece ↔ R-cell"
   leans on it.
2. **∂U₃ ≅ S³** beyond χ = 0 + connectedness (+ G0's double ≃ S⁴ homology).
   A handle/π₁ computation of the digital boundary, or a certification that
   the G0 book's ∂-structure is the double of a collar, would close it.
3. **The exact T-edge link inside the wall** as a geometric object: the
   combinatorial answer (d(F) = T-edge sums, corner blowups) is certified
   and battery-consistent; 14H's dedicated link computation was never run.
4. **The H₂ → δ₂ bridge** (theorem-level, not machine): the equivalence
   chain "H₂(B₃) = ℤ/3 ⟺ CLSS d₃ = 0 ⟺ δ₂(D(ℂ³)) = 4/3" rests on the Wave-7
   theorem (x² ≠ 0 survives) and the CLSS framework from the paper line.
   The machine certifies the H₂ side completely; the bridge is used as
   established theory, per the project's recorded logic.

**Audit points (where a future error could hide — ranked):**
1. **The seam-gauging solution is mod 12.** The v5 system (76 eqs, 58 vars)
   is solved and verified mod 12 (mod-3 field + Hensel mod-4 + CRT); the
   integral boundary entries are the chosen twelfth-integer representatives.
   The battery then certifies d²=0/dT=Td *over ℤ* on those representatives,
   so the certification is complete — but the *uniqueness* of the seam data
   was not classified (other solutions could give different-but-equivalent
   complexes). Risk to the verdict: none (any solution passing the battery
   certifies the same homology); risk to provenance: cosmetic.
2. **The ℤ/9-smith routine was repaired once already** (the 13C-7 fix of the
   skipped 3-entries). The 13C-8 run re-exercised it on d1–d6 with the
   internal asserts (pure powers of 3, exact divisibility, rank agreement,
   PD palindromy) all passing — four independent consistency layers. Any
   residual bug would now have to break the PD symmetry of the ladder.
3. **Finite prime scans.** B₃ torsion scanned p ∈ {2,3,5,7,11,13} ∪
   {17,…,61} (13C-8); Fl₃ scanned p ∈ {2,3,5,7} plus two large rational
   primes. Slots forced by π₁/PD (H₁, H₄, H₅, H₆) need no scan; the
   remaining exposure is the (H₂, H₃) pair at p > 61 — bounded in practice
   by the small integer entries of the orbit boundary matrices, but no
   written Hadamard-type bound exists yet. Closing it: extend the scan
   mechanically or write the entry-bound argument.
4. **Geometric identification of the complex.** The battery certifies the
   complex *is a closed orientable 6-manifold model of Fl₃ with a free C₃
   action* (homology + χ + T-actions + freeness, matching the external
   Poincaré polynomial); it does not reconstruct a diffeomorphism to
   U(3)/T³. The construction lineage (G0 book ← the adjudicated
   stratification ← the U₃ geometry) is the geometric warrant.
5. **The 14H digital-topology numbers** (χ at n = 24/32/40, volume ratios)
   are grid-derived, not exact; they were never load-bearing for the bit
   (the exact skeleton arithmetic was), and the grid artifact at n = 32
   (7 spurious components) shows the resolution sensitivity honestly.

**Nothing in this note reopens the qutrit verdict; the two lines' converged
stratification is now the single certified object it was always aiming to
be.**
