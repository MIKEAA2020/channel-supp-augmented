# WAVE 25 — MANUSCRIPT INTEGRATION OF THE CERTIFIED CORE
### Executed per the user directive of 2026-09-13: "integrate the certified
### core into the manuscript" — merited-queue item 3 of the external merit
### audit, and the user decision posed by WAVE13C_RECONCILIATION §6 (claim
### strength, placement, and how much of the 13C chain to include), now made.

**Artifacts:** `../manuscript uploads v7/` (both papers, .txt sources +
tectonic-compiled PDFs, 47 and 46 pages, no errors); the generation script
`scripts/edit_v7.py` (workspace mirror, 11 anchored replacements, each
asserted to match exactly once); this note. The v6 sources are untouched.

**Bottom line.** The flagship claim is now IN the manuscript, in theorem
form, with exactly the epistemic status the bridge audit certified: **the
proof of `thm:state-d2` (δ₂ ≥ 4/3, equality at the qutrit) is a complete
deductive chain with ONE machine-certified premise (`lem:flag-cohomology`),
whose provenance, validation, and residuals are stated in the paper itself
(`rem:machine-certificate`).** The smallest gating unknown of the flat-width
program — δ₂ of the qutrit, posed as open in v6 — is closed at 4/3, and the
coordinate-flat conjecture is corrected a second time (clause r ≥ 2 → r ≥ 3).

---

## 1. What was inserted, and where (the user-decision parameters resolved)

Placement: §5, immediately after `rem:affine-scope` (the r=1 state-space
results) and before `cor:bottom-dichotomy` — the r=2 block sits exactly where
the r=1 block ends, mirroring `thm:equal-basis` → `thm:state-nonflat` one
index up. The block:

| piece | content |
|---|---|
| `lem:flag-cohomology` | H³(B) = H⁴(B) = ℤ/3 and x² = κ*(u²) generates H⁴. Proof: the CLSS E₂ page of total degrees 3 and 4 **derived by hand** in the paper's own style (E₂^{1,2} = ker N/(P−1)M ≅ ℤ/3 the only total-3 piece — the norm vanishes on ℤ³/ℤ(1,1,1), the sum-zero lattice has index three; E₂^{4,0} ≅ ℤ/3 the only total-4 piece), H³ = ker d₃, H⁴ = coker d₃, **the bit is not page-decidable** (both worlds consistent), the decision machine-certified: H₋(B) = (ℤ, ℤ/3, ℤ/3, ℤ/3, ℤ/3, 0, ℤ) → UCT → H³ = H⁴ = ℤ/3 → d₃ = 0 → the edge (which is κ*, as in degree two) carries u² to x². |
| `rem:machine-certificate` | the provenance, stated in the paper: the 14,910-cell free ℤ/3-equivariant cellulation of Fl₃ (the two-sheet book over the stratified unistochastic base, seam-subdivided); the exact-integer battery (∂² = 0, T³ = id, ∂T = T∂, freeness, the classical cover homology, orbit SNF, torsion exponents, primes ≤ 61); the four external anchors (Poincaré polynomial, Cartan–Leray-forced H₁, χ, the palindromic UCT ladder); the model-case validation of the decision logic and the Euler-class arithmetic (L(3;1,1,1): x² ≠ 0, d₃ = 0; ℝP²×S²: x² = 0, d₃ iso — each cross-validated three ways); the honest residuals (one implementation, reproduced across sessions, not independently re-implemented; the geometric identification warranted by lineage + battery, not a diffeomorphism; the finite prime scan); the repository pointer (footnote). |
| `thm:equal-basis-plane` | the plane-valued equal-value-basis theorem (the r=2 tie theorem): every continuous f: P(V) → ℝ² (V a qutrit) admits an orthonormal basis with all three values equal. Proof: the telescoping H = (h, h∘c): Fl → ℝ⁴ with H∘c = TH, T = T₁⊗I₂ **real-conjugate to R⊗I₂ by the paper's own S** (the "replacing H by S⁻¹H" step one level up — the step the bridge audit verified); R⊗I₂ = cos(2π/3)I + sin(2π/3)J is ω·Id on (ℝ⁴, J) ≅ ℂ², so the normalised Ĥ is a nowhere-vanishing section of L⊕L; e(L⊕L) = c₂ = c₁(L)² = x² ≠ 0 — contradiction. |
| `thm:state-d2` | δ₂(D(B)) ≥ 4/3 for every d_B ≥ 3 (the 3-dim subspace restriction + the vertex bound, the r=2 analog of the `thm:state-nonflat` proof verbatim); **= 4/3 at d_B = 3** (prop:monotonicity + the v6 equality); [4/3, 2(1−1/d_B)] at d_B ≥ 4 (the constant-code value). |
| `rem:affine-scope-2` | the decoder-scope caveat at the second index, mirroring `rem:affine-scope`. |

Claim strength: theorem — the machine premise is an explicitly-labelled
computational lemma inside the proof, exactly the classification the bridge
audit issued (a LEMMA in a complete deductive chain, not the whole content).

How much of the 13C chain: the derivation **summarized** at the level a
referee needs (the page computation by hand, the two-worlds gap, the
certificate, the anchors, the residuals) — the wave history stays in the
repository, not the paper.

## 2. The consistency edits (seven further places + the main article)

* **Intro contributions**: the second-index clause added (with
  `thm:equal-basis-plane` and `thm:state-d2` in the citation list).
* **Specialisations roadmap**: the fourth obstruction thread named.
* **`cor:flat-fails` remark**: the r=2 failure extended to every d_B ≥ 3 at
  any n (slice-gate + state-d2), not only the coordinate-count instances.
* **`rem:flat-status`**: the open range is now r ≥ 3; the smallest gating
  unknown is CLOSED at 4/3; "no d_B ≥ 3 instance is flat at the second index".
* **`con:coord-flat`**: the clause corrected a second time — (d_B ≤ 2 or
  r ≥ 3) — and the discussion rewritten honestly: "the conjecture has been
  corrected twice, each time by a state-space result"; the second form
  predicted δ₂ = 1 on the one-outcome qutrit (nd_B = 3 ≤ 2·2+2) and is
  refuted by the theorem.
* **Conclusion**: the second-index sentence added; the conjecture clause
  r ≥ 3.
* **Open problems**: (v) updated (the first open gating unknowns are now δ₂
  of the ququart and δ₃ of the qutrit); **(vi) new** — the machine-free
  derivation of H³/H⁴ of B, or an independent re-implementation (the last
  computational premise).
* **Main article**: one sync clause in open problem (1) (the companion's
  plane-valued extension, machine-certified, δ₂^◇ ≥ 4/3, the qutrit again
  exactly 4/3). No other main-article touch point exists (scanned).

## 3. Build QA

* `tectonic` on both v7 sources: **no errors**; 47 pages (instruments) and 46
  (main article); no undefined references or citations.
* The one compile error during development (`\con` → `\cong` typo in the
  H⁴ display) was caught by the compiler, fixed in the generation script, and
  the v7 sources regenerated from v6 by the fixed script (all 11 anchored
  assertions re-passed) — the committed sources are exactly the script's
  output.
* All over/underfull box warnings live in pre-existing v6 regions; **none in
  the inserted block**.
* All four new headings verified present in the compiled PDF text; the
  main-article sync clause verified present.
* Consistency cross-checks done before writing: `thm:pinching`'s two-sector
  threshold for the qutrit state space (r ≥ nQ₂(3)−1 = 4) does not conflict
  with δ₂ = 4/3 at r = 2; `prop:monotonicity` and `cor:constant-code` ground
  the upper-bound citations; the `lem:flag-cohomology` cohomology tuple
  agrees with the paper's own degree-2 CLSS computation and with Poincaré
  duality + UCT.

## 4. The scoreboard

* **Qutrit**: H₂(B₃) = ℤ/3, δ₂(D(ℂ³)) = 4/3 — machine-certified theorem
  (bridge audited end-to-end by Wave 24) — **now in the manuscript**.
* **The merited queue**: (1) merit audit DONE; (2) bridge audit DONE; (3)
  this integration DONE; (4) the full-text arXiv/MathSciNet novelty pass —
  REMAINING, at submission time.
* **Ququart**: δ₁ OPEN, the bracket [4/3, 3/2] intact, the W23
  double-blockade unchanged.
* The push backlog is clear: the two stranded commits (2692611 the merit
  audit, 955a651 Wave 24) were pushed at the start of this session
  (a94aff0..955a651), and this round is committed and pushed on top.
