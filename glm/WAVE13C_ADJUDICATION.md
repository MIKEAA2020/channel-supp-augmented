# WAVE 13C-4 — THE F-CELL ADJUDICATION (cross-line, versus Wave 14H §6)
### Artifacts: `wave13c_adjudicate.py` (all claims machine-exact, run 2026-09-10)
### Question (his 14H §6, user directive): my line's 9 F-cells (5 pure + 4 mixed,
### "all feasible") vs his facet survey "U₃ ∩ facet(D_rs=0) = the four T-edges
### (1-dimensional)" — no 2-dimensional facet locus in B₃. Adjudicated against
### the d(F) construction.

**VERDICT: his §4 equality-locus claim is REFUTED (a Monte-Carlo measure-zero
artifact); the 9 F-cells stand in BOTH M and B₃; the proposed resolution
"F-cells live only on the double M, not in B₃" is REJECTED; no design change.**

## 1. The exact algebra (his own Q, his own identity)

For a doubly-stochastic D, the three row-pair Heron slacks coincide
(`Q₁₂ = Q₁₃ = Q₂₃`; re-verified here on 200 000 random DS points, 0 failures —
the 13B machine identity). On any facet `{D_ij = 0}` the (ij)-pair's triangle
has its zero side, so

```
Q_ij = -(A - C)^2,   A = D_i1 D_j1, C = D_i3 D_j3  (the zero-side pair)
```

(machine-exact on 20 000 random facet points per facet, 0 failures). Hence
`Q ≤ 0` on every facet (his sign table CONFIRMED), and the equality locus
`{Q = 0} ∩ facet = {A = C}` is **codimension 1 in the 3-dimensional facet —
a 2-dimensional locus**, not the T-edges.

## 2. Why his survey missed it (the artifact, reproduced)

His method: 25 000 uniform samples per facet. Re-run here: **all 25 000
samples per facet have Q < 0, min Q ∈ [−0.0623, −0.0614]** — matching his
table (−0.0587…−0.0613) exactly. A codim-1 locus has measure zero: uniform
sampling cannot see it. His inference "the equality locus is exactly the
union of the four transposition edges" (14H §4, R1) is a sampling artifact.

## 3. The F-cells are that locus (81 machine points per facet)

Every FPMAP parametrisation (the 13C base build) on a 9×9 (u,v) grid:
`D[FZERO] = 0` to 1e-12, **Q = 0 to 1e-12**, all other 8 entries strictly
positive (**facet interior, not on the T-edges**), and the (u,v) → D map is
injective (a genuine 2-parameter family). E.g. F1(π/4, π/4) =
`[[.5,0,.5],[.25,.5,.25],[.25,.5,.25]]` — orthostochastic (on the wall),
D₁₂ = 0, all three Q's = 0 exactly, 8 positive entries.

So: the 9 F-loci are 2-dim **in M** (the (θ,δ)-domain, the 13B census (D))
**and their images are 2-dim loci of B₃** on `∂U₃ ∩ ∂B₃` (the wall∩facet
equality loci). Both lines' statements are reconciled by correcting the
facet-survey inference — not by relocating the F-cells.

## 4. d(F) adjudicates (the certified construction)

From `wave13c_base_data.json` (G0-certified: base d²=0, homology
(ℤ,0,0,0,ℤ), χ=+2 = S⁴ = double(U₃)): every `d(F_i)` is a ±1-sum of
**transposition edges** — exactly the T-edges his survey found as the Q=0
part of each facet. The F-membranes span between them.

## 5. His residuals are resolved by the F-cells

* His §3 Euler check `1−6+0−9+6 = −8 ≠ χ(U₃)=1` ("not a cell decomposition"):
  with the 9 F-cells, `1−6+9−9+6 = +1 = χ(U₃)` — **repaired** (and
  `2−6+9−9+6 = +2` for the double, the certified G0).
* His §2 boxed residual (the T-edge link inside the wall, probing failures
  "crossings degenerate into the boundary"): the wall meets ∂B₃ exactly
  along the F-membranes — his probes failed precisely there.
* His §3 boxed need ("a signed chain complex must be built on a subdivision
  of the wall"): the two-sheet book's F-layer IS that subdivision.

## 6. Consequences

1. The cellulation design is unchanged; the level-12 ρ-gauged rebuild
   proceeds with the 9 F-cells as pinned.
2. His corrected boundary stratification is `6 σ-pieces + 9 F-cells +
   9 T-edges + 6 vertices` (χ(∂U₃) = 0 ✓, χ(U₃) = 1 ✓) — the two lines
   converge on the same object.
3. No claims about δ₂ are made here.
