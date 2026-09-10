# WAVE 13C — THE BUILD, STAGE 1: BASE CELLULATION CERTIFIED (G0) + A NEW OBSTRUCTION
### Executed against `WAVE13B_SPEC_REVIEW.md` §5 (the corrected v2 "two-sheet book").
### Artifacts: `wave13c_base.py`, `wave13c_base_output.txt`, `wave13c_base_data.json`

**Status: G0 certified. The 32-cell base is a machine-verified S⁴-model. The
fibre layer could NOT be honestly assembled this run: the machine pinned a NEW
obstruction (the non-constant fibre-translation field, §3 below) that the
review's §4 ("c = translation by t₀ / t₀² on the fibres — the Wave-11
mechanism, now TWICE") mis-stated. The exact gauge construction that absorbs
it is derived in §4 and is the concrete next step. δ₂(qutrit) REMAINS OPEN.**

---

## 1. What was pinned and certified (all machine, exact integer outputs)

* **B1 — the 32-cell partition.** Labelling `mcell(θ,δ)` verified on all
  strata (sheets / 6 R / 9 F / 9 E / 6 V); region volume fractions
  0.237/0.379/0.384 and 0.238/0.382/0.380 match the Wave-13B census
  (.235/.382/.384) to sampling error.
* **B2 — ∂F/∂R incidence degrees pinned** (the review §6 item 1):
  * Every pure F is a 4-gon over 4 distinct transposition edges.
  * Every mixed F attaches to **4 edges: 3 sides + a corner BLOWUP**
    (F₆ blows up at (θ₁,θ₃)=(π/2,0); F₇,F₈ at (0,0); F₉ at (π/2,0)) —
    the blowups are REQUIRED: without them d²=0 is arithmetically impossible
    (the 4 sides alone cannot cancel in d₃(d₄(s))).
  * Every R-region bounds exactly 3 F-cells (2 pure + 1 mixed, or 1 pure + 2
    mixed), signs pinned by the outward-normal/orientation convention.
  * d(s±) = ±(Σ R(π-sheet) − Σ R(0-sheet)).
* **B3 — G0 CERTIFIED.** d² = 0 EXACTLY on the 32-cell base; base homology
  = **(ℤ,0,0,0,ℤ)**, χ = +2 (mod 101/1009/10007, torsion-free). Since the
  base is the double of U₃ glued along ∂U₃, this certifies **M ≅ S⁴ and
  hence the spec's (H-top) U₃ ≅ B⁴** — H-top is no longer a hypothesis.
* **B4 — the c-map on the base.** All 32 images pinned; c³ = id; exactly two
  fixed cells (s₊, s₋); V/E/F/R orbit structure matches the Wave-13B census
  (F-orbits {F1,F5,F2}, {F3,F8,F6}, {F4,F7,F9} — free, mixing pure/mixed;
  R-orbits {R0.bF6, R0.bF7, R1.def} and {R1.bF9, R1.bF8, R0.def} — exactly
  the census orbits (B)).
* **R-cell fibre shifts κ (the c-action on the fibre, natural gauge):**
  R0.bF6=(3,0), R0.bF7=(3,3), R1.def=(0,3), R1.bF8=(0,3), R1.bF9=(3,0),
  R0.def=(3,3) **sixths** — half-turn translations; each free orbit sums to
  (0,0) mod 6 as required by c³ = id. (These are gauge-covariant data, not
  invariants; they fix the natural-gauge baseline.)

## 2. Cell-count correction (honest arithmetic)

The review's "≈1518" total is arithmetically inconsistent with any
(base × level-3 fibre) product: the 32-cell base with Wave-11 level-3 fibres
gives **978** cells (6, 27, 108, 297, 342, 162, 36 by degree; χ=6). Moreover
the interface holonomies computed here are **half-turns** (D(π) =
diag(−1,1,1) ⇒ (½,0) in the T²-fibre), which the level-3 thirds grid cannot
align with. LCM(2,3)=6 forces **level-6 fibres** (T²: 36+108+72 = 216 cells;
S¹: 12): the honest final complex is **3786 cells** (6, 54, 378, 1188, 1368,
648, 144; χ=6), 1262 c-orbits. The per-degree table in the review §5 should
be replaced by these numbers.

## 3. NEW OBSTRUCTION (machine-pinned): the sheet fibre-translation field DRIFTS

For the fibration Fl₃ → M with canonical (u,v) = (arg λ₂/λ₁, arg λ₃/λ₂)
fibre coordinates, the c-action on the total space is
  c(x, λ) = (c_M(x), λ·D_L(x)),   κ(x) := [D_L(x)] ∈ T².
Machine facts (all in `wave13c_base_output.txt` / diagnostics):
* **Flat point:** κ([F₀]) = (2/3, 2/3) = t₀² (census-PSIG convention;
  Wave-10's F₀P_σ = t₀F₀ used the opposite cycle) and κ([F̄₀]) = t₀.
* **Orbit sums:** κ(x)+κ(cx)+κ(c²x) ≡ 0 exactly on random sheet points
  (the c³ = 1 cocycle condition holds).
* **BUT κ is NOT constant on the sheets:** it drifts over ranges of order
  ±1.5 sixths around the flat value (s₊: u ∈ [3.17,5.65], v ∈ [−0.24,5.48];
  s₋: u ∈ [0.78,2.98], v ∈ [0.22,2.71]), continuously (κ → (4,4) as
  x → [F₀]). The review's §4 fibre typing ("translation by t₀, the Wave-11
  mechanism, now TWICE") is valid **only at the two flat points**.

Consequence: with the natural (normal-form) trivializations the product
cells (sheet, fibre-cell) are NOT c-cellular (the fibre image of one cell is
a continuously translated family spanning many cells). A re-trivialization
is required before any T-map can be written down.

## 4. The gauge construction that absorbs the drift (derived, ready to implement)

Write β := κ·t₀^{−2} on s₊ (so β + β∘c + β∘c² = 0, β([F₀]) = 0). Since
s₊ ≅ B⁴ is simply connected, the T²-valued maps D_L, D_L∘c, D_L∘c² admit
smooth ℝ²-lifts D̃₁, D̃₂, D̃₃, and
  **g(x) := exp(2πi·((2/3)D̃₁(x) + (1/3)D̃₂(x)))**
solves g(x)·t₀²·g(cx)⁻¹ = D_L(x) identically (abelian, cocycle, checked
algebraically). Re-trivializing each sheet-fibre by μ := λ·g(x) makes the
c-fibre-action the CONSTANT translation t₀² (s₊) / t₀ (s₋); on the free
base cells the fibre gauges can be set so κ ≡ 0 (free orbits carry no
cohomological obstruction). The price: the sheet→F interface maps become the
gauge-modified paths γ(δ) = g(y,δ)⁻¹·D(δ)·c_F, whose swept-cell coefficients
must then be pinned numerically (path-walking on the level-6 grid), and the
whole assembly certified by d²=0, dT=Td, T³=I, freeness, and the G1–G9
battery. The R→pureF interfaces carry constant half-shifts (½·w_F) in the
natural gauge (pinned), and the F→E degenerations are the canonical
quotients q: T³/centre → T³/stab (fixed-row table).

## 5. Remaining work to the bit (unchanged gates, honest order)

1. Implement the gauge g (machine: interpolate the ℝ²-lifts; verify the
   gauge equation to 1e-9 on a grid), re-pin the sheet→F swept coefficients.
2. Level-6 fibre cellulations + q-maps; assemble the 3786-cell complex.
3. Battery G0–G9 (G3 now also certifies the two-sheet structure).
4. Orbit-complex (1262 orbits) mod-p homology + integral SNF on the decisive
   degrees → H₂(B₃) = ℤ/3 (δ₂ = 4/3) or 0 (δ₂ = 1).

**The qutrit bit is still OPEN; nothing here changes the verdict structure —
it hardens the road to it.**
