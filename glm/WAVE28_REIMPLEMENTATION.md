# WAVE 28 — THE DEDICATED RE-IMPLEMENTATION SESSION
### Executed per the user directive of 2026-09-13: "1- the dedicated
### re-implementation session 2- update all manuscript sections, including
### title, abstract, keywords and other sections to align with all surviving
### findings and waves"
### This is the W27 §4 verdict's bounded merited item: closes bridge-audit
### honest residual (i) ("the 13C-7 cellulation remains ONE implementation,
### not independently re-implemented").

**Artifacts:** `w28_base.py` + `w28_base_output.txt` + `w28_base_data.json`
(module 1); `w28_pins.py` + `w28_pins_output.txt` + `w28_pin_data.json`
(module 2); `w28_total.py` + `w28_total_output.txt` +
`w28_total_output.json` (module 3); this note.

**VERDICT: the independent re-implementation REPRODUCES the certified
computation in every layer.** The base cellulation matches the committed
data field-by-field (6/6 fields); all seven pin families match (58+32
values, measurement spread 0.000); the full battery passes on the freshly
assembled 14 910-cell complex (G1–G9 + d̄² = 0, all eleven gates); and the
orbit-complex homology is the committed tuple
**H\_\*(B₃) = (ℤ, ℤ/3, ℤ/3, ℤ/3, ℤ/3, 0, ℤ)**, with the ℤ/9 ladder
(9, 3, 9, 9, 9, 3, 9) and the Poincaré-duality cross-check matching. The
qutrit verdict — H₂(B₃) = ℤ/3, hence CLSS d₃ = 0, hence
**δ₂(D(ℂ³)) = 4/3** — now rests on **two independent implementations**.

---

## 1. The independence inventory (what was done differently)

| layer | 13C original (2026-09-10) | wave 28 re-implementation |
|---|---|---|
| geometry | `Vckm` transcription | own layout, unitarity + F-zero-patterns re-verified |
| d(E) | endpoint algebra | same convention, fresh code |
| d(F) | exact-side tracing + two corner-blowup checks | dense-sampling side tracer, traversal degrees from endpoint t-values, ALL FOUR corners blowup-checked with own near-corner one-sided limits |
| d(R) | Monte-Carlo `face_frac` + sign formula + mixed-F side analysis | EXACT region membership on the θ-cube faces (wall signs are constant per face, decided at 5 points), mixed-wall adjacency by ±θ₂ perturbation, signs by the outward-normal determinant det[t_u, t_v, n_out] |
| d(s) | delta-arc rule | δ-interval boundary rule, own derivation |
| CMAP | algebra + `ckm_normal` sampling | own column-shift algebra + own normaliser (cos δ formula re-derived and confirmed; J-invariant branch) |
| base G0 | mod-p ranks | **exact integer Smith normal form (sympy)** — an independent algorithm |
| phase measurement | BFS gauge solver `phase_solve` (L and R jointly) | **column ratios** angle(U_ij/U_i'j) − angle(V_ij/V_i'j) = L_i − L_i' (R cancels per column), circular-median over all valid columns; the E-stratum S¹-coordinate via the moving-row pair |
| D-inversions | per-cell closed forms (`inv_F`), bisection (`inv_E`) | damped Newton (F), grid + Newton (E) |
| SB signs | Jacobian determinants (incl. gauge-jumpy R-cells) | **constraint propagation from dT = Td** (V-convention + T³ = I force everything; deterministic, self-certifying) |
| T² cellulation | own labels/formulas from wave 11 | own labels, boundaries re-derived from the anti-diagonal-cut grid cycles, certified d²=0 + χ = 0 + translations commute with d |
| q-map | closed formulas from wave 11 | **derived from the three linear projections** (u,v) ↦ −v / −(u+v) / −u by vertex evaluation; certified by the q-cocycle on 3×864 cells |
| homotopy h | closed-form + machine certificate | **re-derived level-by-level from the identity** d(hs)+h(ds) = τ(s)−s (P → E_u, E_u → 0, E_v → L+U, E_a → −(U+L)); certified on all cell types |
| seam solver | mod-3 field + Hensel mod-4 + CRT | **unit-pivot Gaussian elimination over ℤ/12 directly** |
| seam system | 76 eq / 58 vars | re-derived (E1 from R-term equivariance, E2/E3 from closure); 76 eq / 58 vars; **the solution vector equals the original's** (τ̃, σ, Δ, α identical) |
| battery linear algebra | own dense elimination, primes {1000003, 1000033}, torsion {2,3,5,7,11,13} | own elimination (different pivot routine), primes **{1000037, 1000081}** (sympy-verified; 1000093 was caught composite), torsion **{3, 17, 19, 23, 29, 31}** |
| ℤ/9 orders | `coker_order9` unit-pivot smith ladder | **incremental echelon subgroup-order algorithm** over ℤ/9 (generator insertion with unit/3-pivot rows, displacement cascade) |
| G7/G8 prime | 7 | **101** |

Shared spec (necessarily, and honestly): the CKM parameterisation, the
32-cell book architecture (6 V + 9 E + 9 F + 6 R + 2 s), the level-12
fibre refinement, the route-b seam-gauging architecture (per-sheet τ̃'s,
theta prisms, seam sweeps), the q-map sign conventions, the cell labelling
(EDGE_KEYS order etc.) for comparability, and the sheet T-translations
t_{s±} = t₀², t₀ (verified: T³ = I, order 3, free; falsification-tested
below).

## 2. Module 1 — the base (all fields match)

Fresh derivation, G0 certification (d² = 0 exactly; base homology
(ℤ,0,0,0,ℤ) **by exact integer SNF**; χ = +2), then field-by-field
comparison against `wave13c_base_data.json`:

```
EDGE_KEYS: MATCH (9)   D_EDGE: MATCH (9)   D_FACE: MATCH (9)
D_REG: MATCH (6)       D_SHEET: MATCH (2)  CMAP: MATCH (32)
```

Two implementation bugs were found and fixed in the fresh code during
development (a reversed traversal-degree sign on the CCW top/left sides; a
corner-adjacency indexing error in the blowup check) — exactly the class
of bug the re-implementation exists to catch; the corrected derivation
lands on the committed data identically. One methodological difference
surfaced and was resolved honestly: the outward-normal determinant rule
reproduces the original's pure-face sign formula (−1)^{idx+1}/(−1)^{idx}
and its mixed-face side·b₂ analysis without either Monte-Carlo or
closed-form sign tables.

## 3. Module 2 — the pins (all fields match, spread 0.000)

The column-ratio method measured every pin family with **zero spread**
(the median estimate is exact at every sample):

```
KAPPA_F: MATCH (9)    KAPPA_R: MATCH (6)    KAPPA_E: MATCH (9)
W_RF: MATCH (18)      SHIFT_FE: MATCH (36)  TAU_S: MATCH (12)
SB: MATCH (32)
```

The consistency battery (w-equivariance w(cR→cF) = w(R→F)+κ_F−κ_R; κ
orbit sums ≡ 0; sign products = +1; base dT = Td with signs) passes with
zero failures. The SB derivation is a genuinely different route: the
original's Jacobian determinants are gauge-sensitive on the R-cells (a
normal-form branch jump can flip the apparent sign — reproduced here),
while the constraint-propagation solve is deterministic and certifies
itself; both land on the same 32 signs.

## 4. Module 3 — the total complex, the battery, the tuple

* **G1**: 14 910 cells, degrees (6, 108, 1404, 4752, 5472, 2592, 576),
  χ = +6 — PASS.
* **The seam system**: 76 equations, 58 variables, re-derived from the
  equivariance and closure structure; solved over ℤ/12 by unit-pivot
  elimination; **the solution coincides with the original's** (τ̃(s+):
  R0.def (2,2), R0.bF6 (2,0), R0.bF7 (0,4), R1.def (10,2), R1.bF8 (10,4),
  R1.bF9 (0,0); and mirrored on s−; σ, Δ, α likewise).
* **G2**: d² = 0 exactly on all 14 910 cells (free layer + seam-augmented
  sheet layer, homotopy chains re-derived) — PASS, 0 residuals.
* **G4/G6/G5**: T³ = id with sign products +1; no fixed cells; dT = Td
  exactly on all cells — PASS.
* **G3**: H(Fl₃) = (ℤ, 0, ℤ², 0, ℤ², 0, ℤ), torsion-free at
  p ∈ {3, 17, 19, 23, 29, 31} — PASS (rational rank agrees between
  1000037 and 1000081).
* **G7/G7b/G8** (mod 101): 1+T+T² = 0 on H₂; T has order exactly 3 on H₂;
  T = +1 on H₆ — PASS.
* **Orbit complex**: 4 970 orbits, quotient degrees (2, 36, 468, 1584,
  1824, 864, 192); d̄² = 0 — PASS.
* **The homology of B₃**:
  * Betti (1, 0, 0, 0, 0, 0, 1); chain ranks (0, 1, 35, 433, 1151, 673, 191)
    — identical to the original's.
  * t₃ = (0, 1, 1, 1, 1, 0, 0); **no p ≠ 3 torsion at p ∈ {17, 19, 23, 29,
    31}** (the original scanned {2, 5, 7, 11, 13} — the union of the two
    scans is larger than either).
  * |H_k(B₃; ℤ/9)| = **(9, 3, 9, 9, 9, 3, 9)** by the incremental
    subgroup-order algorithm — the original's palindromic ladder exactly.
  * 3-adic exponents e = (0, 1, 1, 1, 1, 0); Poincaré-duality cross-check
    (e₃ = e₂, e₄ = e₁, e₅ = 0): MATCH.
* **THE TUPLE**: H\_\*(B₃) = (ℤ, ℤ/3, ℤ/3, ℤ/3, ℤ/3, 0, ℤ) — **MATCH**
  with the committed 13C-7/8 verdict.

## 5. Falsification (which data the certificates force)

Flipping any single seam start convention, all of them, or swapping the
sheet translations t_{s+} ↔ t_{s−} breaks the battery: the F7/F9/all
flips and the t swap break dT = Td outright; the F5/F6/F8 flips keep
d² = 0 and dT = Td but **destroy the orbit homology** (β₂(B₃) reads −36,
t₃(H₂) reads 38 — the flipped assembly is not a valid equivariant
cellulation of the flag manifold). The full battery therefore forces the
convention data. One honest negative finding: the WDIR/SEAM_DIR sweep
directions that parameterise the constraint system's α/Δ absorption are
NOT forced — the assembled complex is independent of them (the sweep
lengths and starts are solved data); they are a parameterisation choice,
reported as such.

## 6. What this does and does not close

**Closed:** bridge-audit residual (i) — the 13C-7 chain now has two
implementations agreeing on every input datum (base, pins), on the
assembled complex, on the full battery, and on the tuple. An
implementation bug in either line would have to survive both codebases
and both algorithm families (BFS gauge solve vs column ratios; CRT/Hensel
vs direct ℤ/12 elimination; smith ladder vs incremental subgroup orders;
mod-p ranks vs exact SNF on the base).

**Not closed (stated plainly):**
1. **Spec-level risk remains.** The two implementations share the
   mathematical architecture (the 32-cell book, the level-12 fibre, the
   route-b seam gauging). A wrong spec would be reproduced twice; the
   re-implementation catches implementation bugs, not spec bugs. The
   spec's own certification remains the battery + the four external
   anchors + the model-case validations recorded in W24/W25.
2. **The geometric identification** of the 14 910-cell complex with a
   cellulation of Fl₃ is warranted by construction lineage + the battery
   (G3 reproduces the classical homology of Fl₃ exactly), not by an
   explicit diffeomorphism — unchanged.
3. **The prime scan is finite** (now the union {2,3,5,7,11,13,17,19,23,
   29,31} across the two implementations, plus two independent large
   rational primes).
4. **The machine-free derivation** (the W27 §4 high-merit item, open
   problem (vi) in the paper: the Guerra–Jana-route hand proof that x²
   survives on the cyclic quotient) was NOT attempted this session — the
   re-implementation and the manuscript alignment took it; it remains the
   next merited research item.

## 7. The scoreboard

* **The bit, twice-certified:** H₂(B₃) = ℤ/3 ⟹ δ₂(D(ℂ³)) = 4/3, now by
  two independent implementations (13C-7/8 and wave 28).
* Bridge-audit residual (i): CLOSED. Residuals (ii)–(iv) of W24 §"stated
  plainly" unchanged (geometric warrant, finite scan, LINK-A).
* The manuscript residuals in `rem:machine-certificate` (v8: "one
  implementation ... not independently re-implemented") are now
  **stale** and are updated in the v9 pass (this wave's part 2).
* δ₁(ququart) OPEN, bracket [4/3, 3/2] intact; the W23 stop unchanged.
