# WAVE 32 — CORRECTION V2: the six one-line R2–R7 repairs, adjudicated and applied

**Date:** 2026-09-13
**Charge:** "apply the six one-line R2–R7 repairs **only if truly merited and
addressing root cause of issues**" — the six minor findings of the Wave-30
referee read of Proposition 6.16 (*prop:cupsquare*), left on record as
recommendations by Wave 31 (which applied only R1).

**Method — adjudication before application.** The charge is conditional, so
each finding was put through a three-part test before any edit:
1. **Is the defect real?** Each R2–R7 site was located in the v11 source and
   read against the referee's description; every quoted v11 phrase was
   confirmed verbatim (the six sites: Step 1 lines 1927–1928, Step 3 lines
   1987–1992, Step 4 lines 2012–2016 and 2026–2028, Step 5 lines 2037–2047,
   Step 6 line 2061).
2. **Does the proposed repair address the root cause?** The referee's
   proposed repair text was itself re-derived by hand — not taken on trust.
3. **Is the repair's own mathematics sound?** Every arithmetic/structural
   claim entering the applied repairs was re-computed by a fresh
   exact-integer verifier (`scripts/w32_r2r7_check.py`, transcript
   `scripts/w32_r2r7_check_output.txt`, **all 12 gates PASS**, exit 0),
   written independently of the manuscript and of the wave-13C/28 machine
   data.

**The verdict: all six are merited — and one of the referee's own proposed
repair texts needed correction before it could be applied.** Details per
finding:

---

## The adjudication

### R2 (Step 1, the d_r-vanishing parenthetical) — MERITED; the referee's sketch was itself imprecise; the applied repair is the corrected version

**The defect is real and severe for a proof text:** the v11 parenthetical
justifies `d_r = 0` for `r ∉ {2,4,6}` by "`r` even forces an odd `q`-degree
in the target, where `H^{odd}(U(3)) = 0`" — and **`H^{odd}(U(3)) ≠ 0`**
(the fibre cohomology is Λ(z₁,z₃,z₅) with odd generators; gate R2A: the
odd fibre degrees are exactly {1, 3, 5, 9}). A false justification inside a
proof is not cosmetic.

**The referee's proposed two-step replacement, re-derived, is directionally
right but imprecise in its second step:** the sketch says the fibre-degree-8
classes are "already killed by d₂/d₄ (e.g. `d₄(βz₃z₅) = β(σ₂+2τ²)z₅ ≠ 0`
for every β, free or torsion)". Re-derivation shows the σ₁-multiple
coefficients βz₃z₅ are **d₂-boundaries** (via `d₂(z₁z₃z₅) = σ₁z₃z₅`),
not d₄-victims — for β = σ₁, `d₄(σ₁z₃z₅) = σ₁σ₂z₅` is itself zero on the
E₄-page (it lies in the d₂-image into (6,5)), so "≠ 0 for every β" is not a
correct d₄-statement. The applied repair states the corrected mechanism:

* **odd r:** the target sits in odd p-degree, where `H^{odd}(BK;Z) = 0`
  (Step 3's conclusion; gate R2B: `H¹(C₃; Sym^d) = ker N/(T−1)M = 0` for
  all d ≤ 8, re-computed lattice-exactly, plus 2-periodicity);
* **even r ≥ 8:** the source fibre-degree is 8 or 9 (gate R2C), and the
  classes there are boundaries before the E₈-page — in degree nine
  `d₂(βz₁z₃z₅) = βσ₁z₃z₅` kills every class whose coefficient survives
  multiplication by σ₁ and `d₄(τz₁z₃z₅) = 2τ³z₁z₅ ≠ 0` kills the torsion
  coefficients (which annihilate σ₁); in degree eight the σ₁-multiples are
  d₂-boundaries and the rest die under `d₄(βz₃z₅) = β(σ₂+2τ²)z₅ ≠ 0`.

The last clause needed a new fact the referee's sketch did not supply:
**the σ₁-divisibility lattice fact** — a class β whose βσ₂ is a σ₁-multiple
is itself a σ₁-multiple (rationally in the invariant module by coprimality —
σ₂ does not vanish at the σ₁-root locus χ₃ = −χ₁−χ₂, gate-verified — and
then integrally, divisibility by σ₁ = χ₁+χ₂+χ₃ being triangular in the
monomials), hence a d₂-boundary. **Gate R2E verifies this exactly for
degrees 1–8:** the kernel of the evaluation β ↦ β(χ₁,χ₂,−χ₁−χ₂) on the
orbit-sum lattice M_d equals σ₁·M_{d−1} **as lattices** (rank and
membership, degree by degree). The other killing computations are verified
by gates R2D (σ₂ ∉ Zσ₁²; the d₂-image lattices ⟨σ₁²⟩ and ⟨σ₁³, σ₁σ₂⟩
computed from the τ-arithmetic τσ₁ = τ²σ₁ = 0; the torsion images
2τ³z₅, 2τ³z₁z₅ nonzero against the free d₂-images; H⁷(U) = 0).

This is the one repair that outgrew "one line" (2 source lines → 15): the
root cause — a false justification — demanded a correct one, and the
correct one needed the σ₁-bookkeeping the referee's sketch missed.

### R3 (Step 5, the silent (2,2)-slot) — MERITED

The v11 enumeration "In total degree four the terms are E₂^{4,0}, E₂^{3,1} =
E₂^{1,3} = 0, and E₂^{0,4}" claims completeness but silently omits the
(2,2)-bidegree, whose E₂-term would be H²(BK)⊗H²(U(3)) with both factors
potentially nonzero — the vanishing comes entirely from **H²(U(3);Z) = 0**
(exterior algebra on odd degrees: no degree-2 class; gate R2A/R3), which the
paper nowhere states. The crux step should be enumeration-complete. Applied:
one clause, "$E_2^{2,2}=0$ (the exterior algebra Λ(z₁,z₃,z₅) has no class of
degree two)". Root cause (incomplete enumeration in the load-bearing step)
addressed exactly.

### R4 (Step 4, the c₁-uniqueness parenthetical) — MERITED, and LOAD-BEARING (the strongest of the six)

**The defect is real:** the v11 parenthetical claims ι*c₁ = σ₁ because "the
free generator is the unique class restricting to σ₁(χ), since the torsion
restricts to zero" — but the classes restricting to σ₁(χ) form the **coset
σ₁ + bτ, b ∈ Z/3**, and the restriction does not see b. The uniqueness claim
is invalid as stated.

**The pin is not cosmetic — it is load-bearing.** With ι*c₁ = σ₁ + bτ and
b unpinned, the (2,1)-source d₂-image into the crux's (4,0)-slot would
include `d₂(τz₁) = τ(σ₁+bτ) = bτ²`; for b ∈ {1,2} (both coprime to 3) this
injects the extra relation ⟨τ²⟩ into E∞^{4,0} and **the crux dies**
(gate R4B, computed exactly: the quotient with the extra relation (0,0,1)
is the trivial group — E∞^{4,0} = 0, x² would be 0, the Proposition's main
assertion would fail). The completeness of the crux's image enumeration
currently *silently depends* on b = 0; the v11 text never establishes it.

**The applied repair** uses the machinery the paragraph already has — the
same splitting s that pins ε and ε′: the display becomes
ι*c₁ = σ₁ + bτ with b, ε, ε′ ∈ Z/3 (the honest "the restriction pins only
the free components" parenthetical), and the pinning chain gains the c₁
case: 0 = s*(ι*c₁) = s*(σ₁+bτ) = bu (s*σ₁ = 0 by positive fibre degree;
s*τ = u, s being a section of the projection whose pullback class τ is),
so b = 0 (gate R4A: c₁(regular) = 3u = 0; b·u = 0 forces b = 0 in Z/3).
The Step-4 display `d₂(z₁) = σ₁` is then genuinely pinned, and Step 5's
`d₂(τz₁) = τσ₁ = 0` (line 2080) becomes line-checkable.

### R5 (Step 5, the crux's per-subgroup phrasing) — MERITED

**The defect is real as a matter of logic:** the v11 sentence rules out
τ² ∈ ⟨σ₁²⟩ and τ² ∈ ⟨σ₂+2τ²⟩ *separately* ("a finite-order element never
lies in a subgroup generated by an infinite-order element") — but E∞^{4,0}
quotients by the **sum** ⟨σ₁²⟩ + ⟨σ₂+2τ²⟩, and separate non-membership does
not imply non-membership in the sum. Gate R5 exhibits the logical gap on a
witness: (2,2) ∈ ⟨(2,0)⟩ + ⟨(0,2)⟩ ⊂ Z² but in neither summand alone.

**The applied repair** makes the two-step explicit and matches the displayed
quotient: quotient out the direct summand Zσ₁² first (a quotient by a direct
summand leaves both the class of τ² and the complementary summand
unchanged), leaving Zσ₂ ⊕ Z/3τ² with the **single** incoming relation
σ₂+2τ² — a class of infinite order — where the order-three argument applies.
**Gate R5 verifies the sum-quotient itself** (not the separate subgroups):
SNF of the full relation system gives Z/3 with [τ²] of order 3 generating
and [σ₂] = −2[τ²]. The conclusion was correct; the phrasing now proves it.

### R6 (Step 6, the deck-convention sign) — MERITED

**The defect is real, if mild:** the identification "the projection ρ is the
classifying map γ" passes through the inversion K\U(3) ≅ U(3)/K, so a
reader with the other deck-action convention lands on x = ±γ*(τ), and the
text's exact equality is convention-laden. The referee's own independent
re-derivation tripped exactly here — which is the point of a referee read.
**The conclusion is invariant** (gate R6: (−1)² = 1, and on H⁴ the
inversion acts by +1), but the proof text should say so. Applied: one
parenthetical at the identification sentence — "the identification passes
through the inversion K\U(3) ≅ U(3)/K, so a different deck convention could
at worst flip a sign, x = ±γ*(τ); nothing below depends on the choice, the
sign squaring away in x² = γ*(τ²)."

### R7 (Step 3, τΔ = 0) — MERITED, as a marking (the referee's own menu, option 2)

**The defect is real:** the flat claim "τΔ = 0 (the alternating polynomial
Δ contains no monomial χ₁χ₂χ₃)" addresses only the *leading graded
component*; the class of Δ in H⁶(BK) = M₃ ⊕ Z/3τ³ is fixed only up to a
τ³-tail, and τ·(Δ + cτ³) = cτ⁴ ≠ 0 for c ≠ 0 (gate R7B: the three lifts
give the three distinct values 0, τ⁴, 2τ⁴). The claim is **unused
downstream** (verified: the crux and the degree runs use only the
σᵢ-instances, which are unconditional because the σᵢ are the pinned pure
classes of Step 4 — the pins (b, ε, ε′) = (0, 2, 0) make them tail-free).
Applied per the referee's option 2 (mark as lift-dependent), with the
contrast clause: the σᵢ-instances are noted unconditional, the Δ-instance
marked lift-dependent with the formula τ·(Δ+cτ³) = cτ⁴, and "it is not used
below". The alternative option (pin the tail) would have added a convention
the proof doesn't need.

---

## The applied edit (v12)

`scripts/edit_v12.py` — 6 anchored replacements (R2; R7; R4 in two hunks —
the display and the pinning chain; R3+R5 as one hunk, both in the Step-5
opening; R6), each asserted to match exactly once; the v11→v12 diff is
confined to exactly these six regions, net **+29 lines**; `.txt` and `.tex`
written together (byte-identical, 210,505 bytes each). The main article
needs no change (all six sites are internal to the proof of Proposition 6.16
in the instruments paper; the main-article sync clauses do not reference the
proof internals) — **v12 = the instruments paper only; the main article
stays at v10.**

## The QA

* **Compile:** tectonic exit 0, **51 pages** (v11 was 51), zero errors, zero
  undefined references. Every box warning compared against a fresh v11
  compile: **the number-free warning multiset is byte-identical**, and every
  v12 warning region shifts back to a pre-existing v11 region by exactly the
  net line delta −29 (the flag-literature overfull pair 3.34/11.59pt at
  v11:2275–2308 → v12:2304–2337; the bibliography underfulls; nothing in the
  six repaired regions).
* **`scripts/check_v12.py`: 96 PASS, 0 failures** — all 24 v12
  repair-phrase checks present, all 6 superseded v11 phrasings gone
  (including "H^{odd}(U(3)) = 0" and the per-subgroup sentence), all v11/R1
  must-hold checks and all v10 must-hold checks intact (one documented
  phrasing update: the R5 repair replaces the "finite-order element never
  lies in a subgroup…" sentence by its two-step version, so the old-phrase
  check becomes the new-phrase check); the W26 artifacts annotated in-checker
  (INST 211/208, MAIN 237/233, TikZ 3073 — v10/v11/v12-identical); the INST
  dollar delta vs v11 is +74 = 37 new math pairs, parity even.
* **PDF render:** verified phrase-by-phrase via pdftotext with
  whitespace/ligature/prime normalization — 17 new-phrase renders PASS, the
  three old statements absent from the rendered PDF.
* **The math layer unchanged:** the full Wave-31 derivation battery re-run —
  **all 12 gates PASS** (G1–G10, G8a, G3L), exit 0. The R2–R7 repairs are
  textual/argumentative; no arithmetic of the derivation changed.
* **The new verifier:** `scripts/w32_r2r7_check.py` — 12 gates (R2A, R2B,
  R2C, R2D, R2E, R3, R4A, R4B, R5, R6, R7A, R7B), all PASS, exit 0. Honest
  debug trail: three bugs in my own gate code caught before any conclusion
  was drawn — a rank-assertion in the lattice membership helper (fixed by an
  SNF-based comparison), a wrong substitution factor in the evaluation map
  (the (−χ₁−χ₂) polynomial; caught because the σ₁-divisibility kernel came
  out empty), and a containment assertion in the bidegree enumeration
  (higher r shrinks the source set). Each fixed in place, battery re-run.

## The epistemic status

* The Proposition's assertions are unchanged and now fully line-checkable:
  x² ≠ 0; the additive tuple (Z, 0, Z/3, Z/3, Z/3, Z/3, Z); x generating H²;
  x² generating H⁴; H⁶(B;Z) = Z with the discriminant twice a generator
  (the Wave-31/R1 correction, intact).
* The referee's "accept with minor revision" verdict is now **fully
  implemented on both axes**: R1 (Wave 31, the substantive repair + the
  lattice-index gate G3L) and R2–R7 (this wave, adjudicated and applied —
  each verified to address its root cause, with the one instance where the
  referee's own repair sketch was imprecise corrected before application).
* Hand-derived (W29), machine-certified (13C), independently re-implemented
  (W28), referee-verified (W30), lattice-gated (W31), and now
  referee-complete (W32). thm:state-d2 and δ₂(D(ℂ³)) = 4/3 untouched; the
  ququart bracket [4/3, 3/2] OPEN; the W23 stop stands.
* The remaining merited queue is unchanged: the author-side MathSciNet pass
  at submission time; nothing else.

## Artifacts

* `glm/WAVE32_CORRECTION_V2.md` — this note.
* `glm/w32_r2r7_check.py` + `glm/w32_r2r7_check_output.txt` +
  `glm/w32_r2r7_check.json` — the adjudication verifier (mirrored from
  `scripts/`).
* `glm/edit_v12.py`, `glm/check_v12.py` — the edit and the checker
  (mirrored from `scripts/`).
* `manuscript uploads v12/` — `instruments-paper-revised12.tex/.txt/.pdf`.
* The download folder: `instruments-paper-revised12.pdf` +
  `WAVE32_CORRECTION_V2.md`.
