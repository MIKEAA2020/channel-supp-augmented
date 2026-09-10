# WAVE 13C-5 — THE LEVEL-12 ρ-GAUGED REBUILD: CERTIFIED PROGRESS + A NEW
# MACHINE-PINNED ℤ/3 OBSTRUCTION
### Artifacts: `wave13c_l12.py` (output `wave13c_l12_output.txt`),
### `wave13c_diag.py`, `wave13c_diag2.py`, `wave13c_l12_eqs.json`
### Executed per the user directive: "the level-12 ρ-gauged rebuild, starting
### from the already-solved constraint system re-run in twelfths."

**Status: the level-12 rebuild is REFUTED as sufficient — a new ℤ/3 obstruction
(machine-exact, IIS-witnessed in every formulation tried) blocks the sheet
layer at level 12. The certified partial layers (below) and the pinned
obstruction ladder (level 6 → 12 → 36) sharpen the route to: LEVEL 36, or a
sheet-dependent seam gauging. δ₂(qutrit) = 4/3 REMAINS OPEN.**

## 1. Certified this run (all machine, exact integer arithmetic)

* **Level-12 fibre cellulations** (T²: 144 P + 432 edges(H,V,A) + 288 tri
  = 864; S¹: 12+12 = 24): internal d²=0, the q-cocycle, and the
  twelfth-translation permutations — all PASS.
* **G1 PASS**: 14 910 cells, degrees (6, 108, 1404, 4752, 5472, 2592, 576),
  χ = +6 (the WAVE13C_TOTAL §4 "~15 006" estimate; its printed degree list
  was a 12×6 mis-tabulation — corrected here).
* **The mod-2 gate dissolved** (the level-6 obstruction's residue): every
  doubled pin satisfies κ − t EVEN mod 12; all κ-orbit sums ≡ 0 mod 12.
  (t₀² = (8,8), t₀ = (4,4) twelfths; 3t ≡ 0 mod 12 on both sheets.)
* **The natural free-cell layer: d² = 0 exactly** at level 12 (13 182
  columns) — the doubled stage-2a pins remain mutually chain-consistent.
* **An inherited bug found and fixed**: the v2 constraint system's equation
  (4) passed the c-image F-INDEX to `rvar()` (R-variables), creating phantom
  variables `('r',6..8,·)` and corrupting the ρ-compatibility block — in
  `wave13c_total.py`'s lineage since stage 3. Fixed in `wave13c_l12.py`.

## 2. The new obstruction (mod 3, machine-pinned)

Systems tried, all IIS-extracted (`wave13c_diag.py`/`wave13c_diag2.py`):
the v2 system as inherited (after the bug fix), all 12 sign variants
(ρ-signs in the equivariance/closure/corner equations), and a cleanly
re-derived v4 (natural free layer; κ_eff = κ + ρ_{cX} − ρ_X T-map; SB/co-
sign-correct sheet equivariance). ALL inconsistent mod 3, with the SAME
underlying witness:

```
(i) the mixed-F closure tree + the wall-corner transverse equalities
    force all six tau_{si,R} of EACH sheet to a single constant;
(ii) the sheet equivariance on the SHARED R-cells then demands, for the
     SAME rho-difference (e.g. rho_5 - rho_0):
        rho_5 - rho_0 = t_+ - kappa        (sheet +)
        rho_5 - rho_0 = t_- - kappa        (sheet -)
     whose difference is  t_+ - t_- = t0 = (4,4) twelfths ≡ (1,1) mod 3.
=> 0 = 4 mod 12, i.e. 0 = 1 mod 3: FALSE.
```

The R-cells are shared between the two sheets and their fibre translations
are single-valued, so no ρ-assignment, τ-choice, or sign convention can
absorb a sheet-difference. This is a **gauge-independent invariant of the
level-12 two-sheet book** (the analogue of the level-6 ℤ/2 witness).

## 3. The obstruction ladder (the resolution route)

| level L | ℤ/2 gate (κ−t even, half-turns) | ℤ/3 gate (t₊−t₋ = t₀ = L/3 ≡ 0 mod 3) |
|---|---|---|
| 6  | FAIL (odd)          | — |
| 12 | PASS               | FAIL (12/3 = 4 ≡ 1 mod 3) |
| 36 | PASS (18 even)      | PASS (36/3 = 12 ≡ 0 mod 3) |

**Level 36** (LCM(4,9); census ≈ 132 900 cells — needs the sparse battery,
the dense ladder used here does not scale) **or a sheet-dependent seam
gauging**: split the R-cells' fibre grids per sheet — the [g] field's seam
jump (the stage-2b TAU_TILDE medians already differ per sheet, which is
exactly this data) — i.e. ρ's indexed by (sheet, R), with the (E4)/(E5)
compatibilities re-derived across the seam. The latter keeps level 12.

## 4. Honest status

* G1 PASS; fibre layers certified; the natural free layer d²=0 exact; the
  inherited equation-(4) bug fixed; the sheet layer: **OBSTRUCTED at level 12**
  (witness above, in every formulation). G2–G9 and the orbit SNF were NOT
  run (the sheet boundary is not defined).
* The F-cell adjudication (`WAVE13C_ADJUDICATION.md`) stands independently:
  the 9 F-cells are confirmed in both M and B₃; the 14H §4 facet-equality
  claim is a sampling artifact.
* δ₂(qutrit) = 4/3 REMAINS OPEN. Nothing is boxed.
