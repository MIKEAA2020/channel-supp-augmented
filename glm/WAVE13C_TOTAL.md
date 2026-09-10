# WAVE 13C — STAGE 3: THE ASSEMBLY ATTEMPT + A MACHINE-PINNED ℤ/2 OBSTRUCTION
### Executed against `WAVE13C_BASE_BUILD.md` §5 + the stage-2a/2b pins.
### Artifacts: `wave13c_total.py`, `wave13c_total_output.txt`, `wave13c_probe.py`, `wave13c_probe2.py`

**Status: the assembly ran and pinned a NEW obstruction (§3). The 3786-cell
complex's free-cell layer is certified (d²=0 exact on 14 472 boundary entries,
G1 counts/χ), but the sheet layer cannot satisfy [d²=0 ∧ dT=Td ∧ T³=I] at
level 6: a ℤ/2-valued corner-cocycle invariant blocks it. δ₂(qutrit) REMAINS
OPEN. The resolution route (level 12 + whole-complex ρ-gauging) is identified
and machine-scoped (§4).**

---

## 1. What was built and certified (all machine, exact integer arithmetic)

* **Level-6 fibre cellulations** (T²: 36 P + 108 edges(H,V,A) + 72 triangles
  (L,U) = 216; S¹: 6+6 = 12): internal d²=0, the q-map cocycle
  (∂∘q = q∘∂ on all edges, all fixed-rows), and the sixths-translation
  permutation property — all PASS.
* **The 3786-cell census** (6, 54, 378, 1188, 1368, 648, 144; χ=+6):
  BATTERY G1 PASS.
* **The free-cell layer** (V/E/F/R cells × fibres, 3354 columns, 14 472
  nonzero entries): the full pinned interface set (the 18 w-translations
  R→F, the 36 F→E q-shifts, the E→V pt-collapse, the fibre Leibniz signs):
  **d² = 0 EXACTLY — PASS.** Every stage-2a pin is mutually consistent at
  the chain level.
* **The wall/fusion probe** (`wave13c_probe2.py`, the decisive measurement):
  the c-translation on the wall strata DRIFTS exactly linearly in δ with
  slope 6/2π sixths along the γ-direction of the wall
  (F1: u=3+6δ/2π, v=3; F3: u=3, v=3+6δ/2π; F4: diagonal (1,−1);
  F5: constant). In the FUSED fibre grids the T-map on the F-strata is the
  CONSTANT pinned κ_F — machine-verified at δ = 0, 0.3, 1.0, 2.0, π−0.3, π.
  This proves: **the fused-coordinate transfer is exactly the γ-path, and
  the sheet's θ-wall faces are the swept prisms** (the geometric basis of
  the sheet-boundary model).

## 2. The sheet-layer constraint system (148 equations, 93 mod-6 unknowns)

Unknowns: the 12 τ̃ (s→R interfaces), 8 σ + 8 Δ (prism offsets/sweeps per
wall and sheet), the ρ-re-gauging of the R/F/E grids (30 values). Equations:
the dT=Td equivariance cycles, the mixed-F corner closures (d²=0 through
F5–F9, which the sheet prisms do not cover), the wall corners, and the
free-cell equivariances. **The system is INCONSISTENT mod 2** (both with and
without the ρ-gauging: the ρ's enter with coefficient 2 ≡ 0 mod 2).

## 3. THE OBSTRUCTION (machine witness, re-gauging-invariant)

```
F6-closure:   tau(R0.def) = tau(R0.bF6)      [d^2=0 through F6]
F7-closure:   tau(R0.def) = tau(R0.bF7)      [d^2=0 through F7]
equivariance: tau(R0.bF7) - tau(R0.bF6) = kappa(R0.bF6) - t
=> 0 = kappa(R0.bF6) - t = (3,0)-(4,4) = (1,0)  mod 2:  FALSE
```

The natural κ-jumps across the R0-triple (and the R1-triple) are the
**half-turns (0,3)/(3,0) — odd in one component mod 2**; every mixed-F
corner closure demands a zero jump. The parity of κ−t is a **ℤ/2-valued
invariant of the level-6 product cellulation**: no sheet-interface data,
prism parameter, or cell-grid re-trivialization can change it (all such
terms cancel mod 2).

Geometric reading: the two paths sheet→R₀.def→F6 and sheet→R₀.bF6→F6 land
on the same F6 fibre cell with translations differing by the c-orbit jump
κ(R0.bF6)−t; d²=0 requires them equal, dT=Td requires them to differ by
the (odd) half-turn. The 2-sheet book's fold-wall stratification is
**2-torsion-incompatible with the natural c-equivariance at the level-6
resolution.**

## 4. The resolution route (machine-scoped, next session)

1. **Level 12** (LCM extension): κ−t = (6,0)−(8,8) twelfths ≡ (0,0) mod 2 —
   the ℤ/2 obstruction dissolves (verified numerically). Cell census
   ~15 006 cells (6, 108, 756, 2376, 2736, 1296, 288; χ=6); the mod-p
   battery is numpy-feasible at this size.
2. **Whole-complex ρ-gauging**: the mod-3 residue (κ−t ≡ (1,1) mod 3)
   persists at level 12 without re-gauging; with the ρ's (the [g] boundary
   constants on the R/F/E cells) the mod-3 system becomes active and must
   be re-solved. The gauge equation −[g]+κ+[g]∘c = t (verified exactly in
   stage 2b) forces κ_eff ≡ t on all R cells in the gauged grids, which
   makes the equivariance cycles identities; the mixed-F closures then
   reduce to [g]-constancy per R-triple — consistent with the measured
   medians ((3,2),(3,2),(3,2) on the R0-triple).
3. Re-run the sheet prism model at level 12 with the ρ-gauged T-map
   (R/F: (cX, f+t) uniformly), then the full battery G1–G9 and the orbit
   SNF. The prism sweep lengths re-derive from the corner cocycles (the
   Δ unknowns), which the solver pins.

## 5. Honest status

* G1 PASS; free-cell G2 PASS; the sheet layer: **OBSTRUCTED at level 6**
  (witness above); G3–G9 and the orbit SNF were NOT run (the boundary
  operator is not yet defined on the sheet cells).
* The measured [g]|_R boundary medians (stage 2b) independently confirm
  the closure side of the witness (the R-triples are ~constant), i.e. the
  obstruction is genuinely in the equivariance structure, not a pinning
  artifact.
* δ₂(qutrit) = 4/3 REMAINS OPEN. Nothing is boxed.
