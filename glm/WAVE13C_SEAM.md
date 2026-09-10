# WAVE 13C-7 — THE PER-SHEET SEAM GAUGING (route b): THE BATTERY PASSES —
# THE QUTRIT BIT IS MACHINE-CERTIFIED
### Artifacts: `wave13c_seam.py` (output `wave13c_seam_output.txt`),
### `wave13c_seam_diag.py` (the dT=Td diagnostic), `wave13c_seam_eqs.json`
### Executed per the user directive: "proceed with b" (the WAVE13C_L12.md §3
### obstruction-ladder option b — the sheet-dependent seam gauging, level 12).

**VERDICT: the full battery G1–G8 + the orbit SNF PASSES for the first time
in the 13C line. H₂(B₃) = ℤ/3 — WORLD 1 — δ₂(qutrit) = 4/3 is CONFIRMED by
the honest computation. The bit is CLOSED.**

---

## 1. The route (b) and why the mod-3 obstruction dissolves

The level-12 obstruction (`WAVE13C_L12.md` §2): the sheet-equivariance (E1)
on the SHARED R-cells demands the SAME ρ-differences to absorb t₊−κ and
t₋−κ, whose difference is t₊−t₋ = t₀ ≡ (1,1) mod 3 — a ℤ/3-valued invariant
of the two-sheet book AS LONG AS the mixed-F "seam" walls carry hard
zero-jump closures (which forced all τ̃_{si,R} of each sheet to one constant).

**The seam gauging:** the 5 mixed-F walls (F5..F9, 0-based F4..F8) carry
PER-SHEET PRISM SWEEPS (α_{s,F}·d_F) instead of hard closures. The sweep
directions are pinned by the c-orbit structure (c translates the F-fibres,
preserving drift directions around each F-c-orbit):
`{F1,F5,F2}: (1,0)  {F3,F7,F5'}: (0,1)  {F4,F6,F8'}: (1,-1)` (0-based:
{0,4,1}, {2,7,5}, {3,6,8}). The prism set becomes ALL NINE F-cells —
c-invariant — which simultaneously repairs the prism-equivariance (the
v2/v4 prism walls {F1..F4} were NOT a c-invariant set: T(prism on F1) landed
on F5, which had no prism).

The v5 system (76 equations, 58 variables: per-sheet τ̃ (24), σ (16), Δ (8),
seam α (10)): E1 (R-term equivariance, NATURAL κ, single T-map) + E2 (seam
closures with direction-constrained sweeps — the perpendicular components
are hard equalities) + E3 (θ-wall corners). **SOLVED mod 12 (mod-3 field +
Hensel mod-4 + CRT), verified on all 76 equations.** The per-sheet τ̃'s are
non-constant (e.g. sheet+: R0.def (2,2), R1.def (10,2) — the R0↔R1 seam
jump), exactly the "[g] seam jump" data of stage 2b.

## 2. Two structural defects found and fixed in the inherited sheet model

* **The prism chains were not the translation homotopy.** d²=0 on the sheet
  cells requires chains S with d(S(σ)) + S(∂σ) = τ_μ(σ) − σ (the homotopy
  identity). The v2/l12 `prism_chain` returned EMPTY for parallel sweeps
  (H along u, V along v), so the identity failed at those levels (first
  attempt: 191,808 d²-residuals). Replaced by the exact homotopy operator
  (machine-certified `h_cert` on every cell type, both directions):
  `h_u: P↦+H(j,i), H↦0, V↦+(L+U), A↦−[U(k,c−k−1)+L(k+1,c−k−1)], L,U↦0`;
  `h_v: P↦+V(i,j), V↦0, H↦−(L+U), A↦−[L(k,c−k)+U(k,c−k−1)]`;
  `h_μ = h_{(μu,0)} + τ_{(μu,0)}h_{(0,μv)}` (negative steps via the reversed
  telescoping).
* **The seam sweep conventions are pinned by the c-orbits.** The c-edges
  F2→F7, F7→F5, F6→F8, F8→F3 SWAP the R-parent roles (the δ-reversal), so
  the seams on those edges (F7, F8) sweep ra→rb (start = ra-path,
  μ = rb−ra, sign +co_a); the others sweep rb→ra. With this convention the
  homotopy chains chain exactly around every c-orbit:
  `start(cF) = start(F) + κ_F − t_s`, `μ(cF) = μ(F)`, `sgn(cF) = sgn(F)·SB[F]`
  — verified by hand on both sheets, then by the exact G5 certificate.

A third inherited bug was found and fixed in the ℤ/9 smith routine
(`coker_order9`): its pivot elimination skipped the 3-entries below the
unit pivots, leaving nonzero pivot-column entries in the eventual free rows,
which polluted the L-residual through the column-clear step and inflated
the 3-rank (t = 36, arithmetically inconsistent with d̄²=0 mod 9: the
correct t = 1). The first run of the fixed routine restores consistency:
|im d̄₃| = 3⁸⁶⁵ ≤ |ker d̄₂| = 3⁸⁶⁷.

## 3. The battery (all machine, exact integer arithmetic)

| gate | content | result |
|---|---|---|
| G1 | 14 910 cells, degrees (6,108,1404,4752,5472,2592,576), χ=+6 | PASS |
| G2 | d² = 0 exactly on all 14 910 cells (free layer + seam-augmented sheet layer) | PASS, 0 residuals |
| G3 | H(complex) = (ℤ, 0, ℤ², 0, ℤ², 0, ℤ), torsion-free p ∈ {2,3,5,7} | PASS — the complex is a genuine Fl₃ cellulation |
| G4 | T³ = id on all cells (sign products +1) | PASS |
| G5 | dT = Td exactly on all cells (incl. the prism/seam terms) | PASS, 0 residuals |
| G6 | freeness: no fixed cells | PASS |
| G7 | N = 1+T+T² = 0 on H₂ (mod 7) | PASS |
| G7b | T has order exactly 3 on H₂ (mod 7) | PASS |
| G8 | T = +1 on H₆ (mod 7) | PASS |
| d̄² | orbit boundary d̄² = 0 (sign-correct coinvariants) | PASS |

The orbit complex: 4970 cells (all orbits size 3), quotient degrees
(2, 36, 468, 1584, 1824, 864, 192).

## 4. The verdict

```
B_3 Betti (rational) = (1, 0, 0, 0, 0, 0, 1)
mod-p torsion counts t_p: p=3: (0,1,1,1,1,0,0); p in {2,5,7,11,13}: all 0
|H_0(B_3; Z/9)| = 9   (connected)
|H_1(B_3; Z/9)| = 3   -> min(i,2) = 1 -> H_1 = Z/3 exactly (i = 1)
|H_2(B_3; Z/9)| = 9   -> min(j,2) = 1 -> H_2 = Z/3 exactly (j = 1)

H_*(B_3) = (Z, Z/3, Z/3, Z/3, Z/3, 0, Z)
```

**THE BIT: H₂(B₃) = ℤ/3** (β₂ = 0, exactly one 3-primary summand, exponent
j = 1 machine-pinned by the UCT ℤ/9 computation; no p ≠ 3 torsion).

* → WORLD 1: the CLSS d₃: E3^{1,2} → E3^{4,0} is ZERO.
* → the Chern-class obstruction x² ≠ 0 survives (the Wave 7 theorem).
* → **δ₂(D(ℂ³)) = 4/3 is CONFIRMED by the honest computation.**

Consistency checks: χ(Fl₃) = 6 = 3·χ(B₃) = 3·2 (free 3-cover ✓);
H₂(B₃;ℚ) = H₂(Fl₃;ℚ)^{C₃} = 0 ✓ (G7: 1+T+T² = 0 on H₂ ✓); H₆(B₃) = ℤ with
T = +1 ✓ (G8); H₁ = ℤ/3 = abelianized π₁ ✓.

## 5. Honest caveats

* The H₃, H₄ slots have exactly one 3-primary summand each (t₃ = 1); their
  EXPONENTS are not pinned by this run (would need the c4/c5 ℤ/9-smith).
  They do not affect the qutrit bit.
* The seam sweeps are the per-sheet data that the level-6/12 lines kept
  trying to gauge away; the machine certificates (G2, G5, G3) establish
  that the seam-augmented chain complex is a valid Fl₃-cellulation with a
  C₃-equivariant cellular T-map — this is the certification the whole
  13C battery was designed to demand.
* The obstruction ladder closes: the ℤ/2 (level 6) and ℤ/3 (level 12
  shared-seam) obstructions were artefacts of over-rigid seam models, not
  of the space; level 36 is unnecessary.
