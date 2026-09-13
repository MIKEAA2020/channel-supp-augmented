# WAVE 30 — A REFEREE-STYLE READ OF THE NEW PROPOSITION (prop:cupsquare, v10)

**Date:** 2026-09-13
**Charge:** "a referee-style read of the new Proposition" — Proposition 6.16
(*The cup square on the flag quotient: a hand derivation*), instruments paper
v10, source lines 1857–2084, together with its integration points (Lemma 6.17,
Remarks 6.18–6.19, the open-problem list, the abstract/intro/conclusion
provenance phrases).

**Method.** Every step of the seven-step proof was re-derived by hand,
independently of the manuscript and of the wave-13C/28 machine data; every
checkable arithmetic claim was re-computed by an exact-integer script
(`w30_referee_check.py`, transcript `w30_referee_check_output.txt`) written
from scratch for this read. The machine tuple was consulted only at the end,
as a comparison, never as an input — the same discipline the wave itself
claims, and the claim survives this referee's audit of it.

---

## 1. Verdict, up front

**The Proposition is correct in its principal assertions and the proof route
is sound.** Specifically: the assertion `x² ≠ 0` in `H⁴(B;ℤ)` — the decision
bit that discharges the machine premise of Lemma 6.17 — is proved by a valid
chain (the homogeneous-space model, the pullback of the universal fibration,
Borel's transgression with the ε = 2 pin, the collapsed `BT³`-page, the
torsion-survival crux, and the edge identification); the additive tuple
`(ℤ, 0, ℤ/3, ℤ/3, ℤ/3, ℤ/3, ℤ)` is correct; and the claims that `x` generates
`H²` and `x²` generates `H⁴` are correct.

**One substantive correction is required (Finding R1):** the final clause of
the statement — "and a discriminant class generating `H⁶`" — is **false as
stated**. In `H⁶(B;ℤ) ≅ ℤ` the discriminant class is **twice** a generator.
The error originates in Step 2's integral module statement
(`H*(BK;ℤ)_free = ℤ[σ₁,σ₂,σ₃] ⊕ Δ·ℤ[σ₁,σ₂,σ₃]`), which is true rationally
but false integrally (an index-2 sublattice, with the index growing in higher
degrees). The correction is local: the groups, the crux, the lemma, and the
downstream theorem chain (`thm:equal-basis-plane`, `thm:state-d2`,
`δ₂(D(ℂ³)) = 4/3`) are all unaffected.

**Recommendation: accept with a minor revision** — R1's local correction plus
the six one-line repairs R2–R7 below. In journal terms: *correct and resubmit,
no new mathematics needed.*

---

## 2. What was independently re-verified (all confirmed)

Referee computations supporting each item are in the transcript; hand
re-derivations in the reading notes.

* **Step 0 (the homogeneous-space model).** `Fl = U(3)/T³` with the flag
  lines the column spans; the deck transformation `c` is right multiplication
  by the permutation matrix σ (column shift), which normalises `T³`; the
  ⟨c⟩-orbits are exactly the right cosets of `K = T³ ⋊ ⟨σ⟩`, so
  `B = U(3)/K`. Verified, including the harmless convention ambiguity (σ vs
  σ⁻¹ generates the same K). The freeness of the ⟨c⟩-action matches Theorem
  6.13's fixed-point argument.
* **Step 1 (the fibration and its transgressions).** The Borel construction
  `EU(3) ×_K U(3) → BK` is the associated bundle of the principal
  K-bundle `EU(3) → BK` with fibre the left K-space `U(3)`; the total space is
  weakly equivalent to `K\U(3) ≅ B` (the bundle-over-`K\U(3)` with contractible
  fibre `EU(3)`); the map `[e,g] ↦ eg` exhibits it as the pullback of the
  universal `U(3)`-bundle along `Bι`, with the identity on fibres — so the
  Serre-SS differentials are the pulled-back universal ones by naturality, and
  the local system is trivial because left translations by elements of the
  connected `U(3)` are homotopic to the identity. All checked; the transgression
  `d_{2i}(z_{2i−1}) = c_i` is classical (Borel) as cited.
* **Step 2 (the cohomology of BK) — the groups.** The collapse argument of the
  `BT³ → BK → BC₃` page is airtight: with the permutation-orbit decomposition
  of each `Sym^d`, an even-r differential targets an odd fibre-degree (where
  `H^{odd}(BT³) = 0`) and an odd-r differential targets an odd, positive
  group-degree (where the entries vanish: permutation modules are acyclic and
  the trivial summands have `H^{odd}(C₃;ℤ) = 0`). The free ranks equal the
  Burnside orbit counts (re-computed d ≤ 8: 1, 1, 2, 4, 5, 7, 10, 12, 15) and
  the torsion sits in bidegrees `(2k, 6a)`, k ≥ 1, one `ℤ/3` each. Confirmed.
* **Step 3 (the torsion product rule) — the arithmetic.** All the τ-products
  used in the proof were re-computed from the norm model
  `H²(C₃; M_d) = M_d^{C₃}/N·M_d` (agreement of the fixed-monomial detection
  rule with direct membership tests, ten products): `τσ₁ = τσ₂ = τΔ = τσ₁³ =
  τσ₁σ₂ = 0` (the χ₁χ₂χ₃-coefficients 0, 0, 0, 6, 3 respectively) and
  `τσ₃ ≠ 0` (coefficient 1) generating the `(2,6)`-slot; `τ^k ≠ 0` for all k
  (the slots persist). The display `H⁴(BK) ≅ ℤσ₁² ⊕ ℤσ₂ ⊕ ℤ/3·τ²` is correct
  **as a lattice** (the degree-2 orbit sums
  `χ₁²+χ₂²+χ₃² = σ₁²−2σ₂` and `χ₁χ₂+χ₂χ₃+χ₃χ₁ = σ₂` generate exactly
  `⟨σ₁², σ₂⟩`, index 1 — verified) — this matters: the degrees the crux needs
  are exactly the safe ones.
* **Step 4 (the transgression values).** The Chern-root restriction
  `c_i(χ) = σ_i(χ)` on the fibre; the splitting `s: BC₃ → BK` through
  `σ ↦ (1;σ)`; the composite classifies the regular representation
  `1 ⊕ ω ⊕ ω²`, whose Chern classes in `ℤ[u]/(3u)` are `c₁ = 3u = 0`,
  `c₂ = 2u²`, `c₃ = 0` (re-computed: `(1+0u)(1+1u)(1+2u) = 1 + 3u + 2u²`).
  The section kills positive fibre degree, so `2u² = εu²` pins **ε = 2** and
  `0 = ε'u³` pins **ε' = 0**; the τ²-pullback `s*(τ²) = u²` is the ring-map
  image. All confirmed.
* **Step 5 (the crux) — the heart of the proof.** The incoming images into
  the `(4,0)`-slot are `⟨σ₁²⟩` (from `d₂(βz₁) = βσ₁`, β free; note
  `τσ₁ = 0` kills the torsion part of the image) and `⟨σ₂ + 2τ²⟩` (from
  `d₄(z₃)`); nothing leaves `(4,0)`; the `(0,4)`-term dies under
  `d₂(z₁z₃) = σ₁z₃ ≠ 0` (injective, free target); the `(2,2)`- and
  `(3,1)`/`(1,3)`-slots vanish. Hence
  `E∞^{4,0} = (ℤσ₂ ⊕ ℤ/3·τ²)/⟨σ₂+2τ²⟩` and the SNF of `[[1,2],[0,3]]` gives
  `≅ ℤ/3` with `[τ²]` of order 3, nonzero, generating (and
  `[σ₂] = −2[τ²]`). **The crux is correct.** (See R5 on the phrasing.)
* **Step 6 (the edge).** The edge of the fibration's SS is the projection
  pullback; the cover `Fl → B` is the T³-quotient of the principal K-bundle
  `U(3) → B`, hence classified by `π∘γ` with `γ` the classifying map — this
  is functoriality of the associated-bundle construction and is rigorous.
  `κ = π∘γ` and `x = κ*(u) = γ*(τ)` (see R6 for a convention remark), and
  `x² = γ*(τ²) = [τ²] ≠ 0`. Confirmed — **the main assertion holds.**
* **Step 7 (the remaining degrees).** Degree 2: `H²(B) = ℤ/3`, generated by
  the edge image of τ (= x). Degree 3: `d₂(σ₁z₁) = σ₁² ≠ 0` kills the free
  part of `(2,1)` while `d₂(τz₁) = τσ₁ = 0` leaves `ℤ/3·τz₁`; `z₃` dies under
  `d₄` — note the image `σ₂+2τ²` has **infinite order**, so `d₄` is injective
  on `ℤz₃`; this is exactly the point where the derivation correctly
  diverges from the lens model (there the transgression image is torsion and
  `3z₃` survives). Degree 5: the free `(4,1)`-classes die under `d₂`
  (`τ²σ₁ = τ(τσ₁) = 0` survives); `τz₃` dies under
  `d₄(τz₃) = τ(σ₂+2τ²) = 2τ³ ≠ 0`; `z₅` dies under `d₆(z₅) = σ₃ ≠ 0`
  (infinite order again); so `H⁵ = ℤ/3·τ²z₁`. Degree 6: the group is `ℤ`
  (see R1 for the generator). The mixed terms die transversally as claimed.
  The degree runs are all correct.
* **The tuple.** `(ℤ, 0, ℤ/3, ℤ/3, ℤ/3, ℤ/3, ℤ)`, independently, and the
  UCT inversion matches the wave-13C/28 machine homology tuple
  `(ℤ, ℤ/3, ℤ/3, ℤ/3, ℤ/3, 0, ℤ)` — read only as a comparison, as the wave
  states. Euler characteristic 2 = 6/3 consistent.
* **The Lemma 6.17 decision logic.** `x² = κ*(u²)` is the edge image of `u²`
  through `E∞^{4,0} = coker d₃^{1,2}`; a nonzero image forces the cokernel
  nonzero; a `ℤ/3 → ℤ/3` map with nonzero cokernel is zero; so `d₃^{1,2} = 0`
  and `H³ = H⁴ = ℤ/3` with `x²` generating. Sound; the page-level computations
  (`E₂^{1,2} = ℤ/3` via the norm/invariants on `H²(Fl)`, the vanishing
  fixed-vector argument on `H⁴(Fl)`) re-verified.
* **The lens-model validation (G7 of the wave).** Re-derived by hand:
  `SU(2) → ESU(2)×_{C₃}SU(2) → BC₃` with `d₄(z₃) = 2u²` (the pin for the
  2-dimensional rep `ω ⊕ ω²`) reproduces `H*(L(3;1)) = (ℤ, 0, ℤ/3, ℤ)` with
  the surviving `3z₃` — the mechanism, and the contrast with the flag case,
  are exactly as the wave reports. The `ℝP²×S²` companion case pins the other
  world (`x² = 0`, `d₃` an isomorphism), as recorded in Wave 24.

---

## 3. Finding R1 (substantive) — the integral module statement and the H⁶-generator clause

**What is claimed.** Step 2 (lines 1945–1955): "The free part is
`ℤ[σ₁,σ₂,σ₃] ⊕ Δ·ℤ[σ₁,σ₂,σ₃]` … the module statement follows because in each
degree d the orbit sums span the invariant lattice, of rank equal to the
number of orbits, which the monomial count of the displayed module
reproduces." Step 3 (lines 1985–1987) displays
`H⁶(BK) ≅ ℤ{σ₁³, σ₁σ₂, σ₃, Δ} ⊕ ℤ/3·τ³`. Step 7 (lines 2070–2080) concludes
`H⁶(B) ≅ … ≅ ℤ·⟨Δ⟩`, "the top class being the discriminant", and the
**Proposition's statement** (lines 1872–1873) asserts "a discriminant class
generating `H⁶`".

**What is wrong.** The rank-reproduction argument proves only that the
displayed module is a *finite-index* sublattice of the invariant (orbit-sum)
lattice `M_d^{C₃} = H^{2d}(BK)/tors` (the edge `H^{2d}(BK) → E∞^{0,2d} =
H⁰(C₃; Sym^d)` is surjective with torsion kernel). Integral equality fails
from degree 3 on. The index, computed exactly (transcript, CHECK 1):

| degree d | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 |
|---|---|---|---|---|---|---|---|---|---|
| `[M_d^{C₃} : module]` | 1 | 1 | 1 | **2** | **2** | **4** | **8** | **16** | **32** |

The degree-3 witness: the orbit sum `S₁ = χ₁²χ₂ + χ₂²χ₃ + χ₃²χ₁` is invariant
but `S₁ = ½(σ₁σ₂ − 3σ₃ + Δ)` (since `S₁+S₂ = σ₁σ₂ − 3σ₃` and
`S₁ − S₂ = Δ`), and the linear system `S₁ = aσ₁³ + bσ₁σ₂ + cσ₃ + eΔ` forces
`b = e = ½` (transcript, CHECK 2) — no integer solution. Over `ℚ` the module
statement is of course true (2 invertible), which is why the rational
cohomology remark in Step 7 survives.

**How it propagates.** Two propagation paths, both confined to degree 6:

1. The Step 3 display `H⁶(BK) ≅ ℤ{σ₁³,σ₁σ₂,σ₃,Δ} ⊕ ℤ/3·τ³` is correct as an
   abstract group (`ℤ⁴ ⊕ ℤ/3`) but false as an identification via the named
   classes: they span an index-2 sublattice of the free part. The true free
   part is the orbit-sum lattice `⟨A₁, S₁, S₂, σ₃⟩` with
   `A₁ = χ₁³+χ₂³+χ₃³`.
2. Step 7's degree-6 quotient, run on the true lattice
   `M₃^{C₃}/⟨σ₁³, σ₁σ₂, σ₃⟩`, is `≅ ℤ` (free rank 1, no torsion — verified,
   CHECK 6), but the generator is the class of the **orbit sum** `S₁`, and the
   relations give `[S₂] = −[S₁]`, `[A₁] = 0`, `[σ₃] = 0`, hence
   **`[Δ] = [S₁−S₂] = 2[S₁]`** — the discriminant class is twice a generator.
   Verified exactly: `Δ − 2S₁` lies in the image lattice, `Δ − S₁` does not,
   `S₁` does not (transcript, CHECK 6). So both "≅ ℤ·⟨Δ⟩" (Step 7) and "a
   discriminant class generating `H⁶`" (the statement) are incorrect as
   stated; the group `ℤ` is correct.

**What is NOT affected.** The crux and everything downstream of it: the
crux lives in degrees ≤ 4 of `BK`-cohomology, i.e. fibre-degrees ≤ 2, where
the module statement is exact (index 1 — verified); the τ-rule is a monomial
computation, independent of the module presentation; the classes `σ₁, σ₂, σ₃`
are pinned as canonical classes (Chern-class pullbacks) in Step 4, not via
the module statement; and Lemma 6.17, `thm:equal-basis-plane`, `thm:state-d2`,
and `δ₂(D(ℂ³)) = 4/3` use only `H²/H³/H⁴` and the decision bit. The additive
tuple — the object the three independent routes agree on — is untouched. The
rational statement `H*(B;ℚ) = ℚ ⊕ ℚ·Δ̄` remains correct (and is the right
framing for the discriminant).

**Why the wave's gates did not catch it.** Gate G3 of
`w29_derivation_check.py` compares the *ranks* (`#orbits` vs
`nmons(d) + nmons(d−3)`) — an index-2 sublattice is invisible to a rank check.
(G10 compares groups; `ℤ` matches `ℤ`.) This is a gate-design gap, not an
execution failure: the gates certified exactly what they tested, and the
manuscript then asserted slightly more than the gates certified.

**The repair (mechanical, ~six lines of source):**
1. Step 2: replace the module equality by the orbit-sum lattice statement
   (the free part is the invariant lattice spanned by the orbit sums together
   with the fixed monomials `(χ₁χ₂χ₃)^a`), or state the module over `ℚ` and
   give the integral free ranks separately; optionally note the index
   (2 in degree 3, growing thereafter).
2. Step 3: replace the `H⁶(BK)` generating set by the orbit sums
   `{A₁, S₁, S₂, σ₃}` (keeping the `ℤ/3·τ³` torsion), or display the group
   abstractly.
3. Step 7: conclude `H⁶(B;ℤ) ≅ ℤ`, generated by the class of the orbit sum
   `S₁`, with the discriminant twice a generator (consistent with the
   rational cohomology).
4. The Proposition statement: replace "and a discriminant class generating
   `H⁶`" by "and `H⁶(B;ℤ) ≅ ℤ`, in which the discriminant class is twice a
   generator" (or drop the clause — the tuple is the operative content).
5. Add a lattice-index gate to the verifier (membership test of `S₁` in the
   module lattice, or the index table above) so the correction is certified.
6. The wave-29 note and the commit message record "H⁶ = ℤ·Δ"; the correction
   wave should note the supersession.

---

## 4. Findings R2–R7 (minor; one-line repairs each)

* **R2 (Step 1, lines 1926–1927).** The parenthetical justifying
  `d_r = 0` for `r ∉ {2,4,6}` reads "r even forces an odd q-degree in the
  target, where `H^{odd}(U(3)) = 0`" — but `H^{odd}(U(3)) ≠ 0` (`z₁, z₃, z₅`
  are odd-degree classes). The claim is true; the correct justification is
  two-step: (i) r odd ⟹ the target has odd, positive p-degree, where
  `H^{odd}(BK) = 0` (Step 2/3); (ii) r even ≥ 8 ⟹ the only possible source
  fibre-degrees are 8 and 9 (`z₃z₅`, `z₁z₃z₅`), and those classes are already
  killed by `d₂`/`d₄` (e.g. `d₄(βz₃z₅) = β(σ₂+2τ²)z₅ ≠ 0` for every β, free
  or torsion). Reword the parenthetical.
* **R3 (Step 5, line 2019).** The enumeration of the total-degree-4 terms
  silently omits `(2,2)`. It vanishes because `H²(U(3);ℤ) = 0` — one clause.
* **R4 (Step 4, lines 1993–1995).** The parenthetical "the free generator is
  the unique class restricting to `σ₁(χ)`, since the torsion restricts to
  zero" does not establish uniqueness: the classes restricting to `σ₁(χ)` are
  the coset `σ₁ + bτ`, `b ∈ {0,1,2}`. The constant b *is* pinned — by the
  same splitting the paragraph then uses for `ε, ε'`: `s*ι*c₁ = c₁(reg) =
  3u = 0` and `s*(σ₁ + bτ) = bu` force `b = 0`. Add the c₁ case to the
  pinning sentence.
* **R5 (Step 5, lines 2024–2028).** "A finite-order element never lies in a
  subgroup generated by an infinite-order element" rules out membership in
  each image subgroup *separately*, but the quotient is by their *sum*. The
  gap is closed by the displayed two-step quotient (first split off the
  `ℤσ₁²` direct summand — the image of `τ²` is unchanged by a direct-summand
  quotient — and only then mod out by the single remaining relation); the
  conclusion is correct (SNF-verified). One sentence would make it airtight.
* **R6 (Step 6, lines 2040–2051).** The identification of the transported
  projection with the classifying map γ — hence the exact equality
  `x = γ*(τ)` — is correct in substance but depends on the alignment of the
  deck-action convention with the C₃-structure on the associated bundle (the
  identification is fixed by the functorial `κ = π∘γ` part, which is
  rigorous). The referee notes the robustness: the only possible discrepancy
  is a sign in `ℤ/3` (`x = ±γ*(τ)`), and the conclusion
  `x² = γ*(τ²)` is invariant under it (2² = 4 ≡ 1 mod 3). A one-line remark
  removes the dependence on the reader's convention bookkeeping.
* **R7 (Step 3, lines 1974–1977).** The claim `τΔ = 0` is sensitive to the
  choice of the Δ-lift's torsion component (the τ-rule controls the leading
  graded component; a torsion tail of the lift could contribute a deeper
  `τ·(tail)` term), and no pin is given for that tail. The claim is never
  used downstream (the crux and the degree runs use only `τσ₁ = τσ₂ =
  τ²σ₁ = 0` and `τσ₃, τ³ ≠ 0`, all sound because the σᵢ are pinned pure by
  Step 4's splitting), so nothing fails — but either pin the tail (e.g. choose
  the lift with vanishing τ³-coordinate) or mark the claim as lift-dependent.
  Also note `τσ₁σ₂ = 0` holds (coefficient 3) if wanted for symmetry of the
  display.

---

## 5. The integration points (assessed)

* **Lemma 6.17 (lem:flag-cohomology).** The rewritten proof — the page-level
  computation, the two-worlds statement, and the hand decision via
  Proposition 6.16 with the machine retained as the cross-check — is sound
  and correctly scoped. No changes needed beyond R1's knock-on (none reaches
  the lemma: it uses degrees ≤ 4 only).
* **Remark 6.19 (rem:machine-certificate).** The three-independent-routes
  framing (hand derivation, cellulation, re-implementation) is fair and
  survives this read. Two phrases deserve adjustment after R1: "a
  self-contained invariant-theory step" is where the false module statement
  lives, and "the invariant lattice … verified by an exact-integer script"
  overstates what G3 tested (ranks). Suggested rewording: the invariant-theory
  input is the orbit decomposition and the τ-rule (monomial arithmetic,
  script-verified); the module presentation is corrected per R1.
* **Remark 6.18 (rem:flag-literature).** The differentiation from the
  Guerra–Jana programme (symmetric-group quotients with field coefficients,
  in the service of Auerbach counting, vs the cyclic intermediate quotient
  with integral coefficients and torsion exponents pinned, in the service of
  the width chain) is accurate, and the characterisation of the hand
  derivation as "the integral lift of the transgression route" is now
  referee-confirmed in substance: the fibration comparison, the
  Chern-class transgressions, and the invariant-theoretic replacement of the
  field-coefficient module algebra are all present and correct; the
  torsion-survival argument (Step 5) is exactly the layer the field
  algorithms do not address. No changes needed.
* **Open problem (vi).** The discharge — "the hand derivation … is supplied
  by Proposition 6.16, whose transgression computation removes the last
  computational premise of Theorem 6.13's chain" — is substantively valid:
  what the open problem asked for (the hand derivation of the cohomology
  deciding the lemma) is delivered. The R1 correction does not reopen it; the
  remaining neighbourhood direction stated there (unstable integral cohomology
  of the symmetric-group quotients) is correctly identified.
* **Abstract/intro/conclusion provenance phrases** ("hand-derived,
  machine-certified, and independently re-implemented"): accurate for what
  they assert (the additive cohomology of B and the cup-square decision); the
  main article's sync clauses are likewise fine. No changes required by this
  read beyond R1's local fixes in the instruments paper.

---

## 6. Referee's summary of the mathematical content

The route is a genuine integral lift of the Guerra–Jana transgression
mechanism, not a notational variant of it: the pullback identification of the
Borel fibration (Step 1) is what makes the transgressions *known* rather than
re-computed; the collapse of the `BT³`-page (Step 2) is the replacement for
the field-coefficient module algebra; the ε = 2 pin (Step 4) is a clean use
of the splitting section and the regular representation; and the
torsion-survival crux (Step 5) — three lines of order arithmetic that decide
an element's survival against infinite-order relations — is the integral
layer the cited programme does not touch. The proof is checkable line by
line, which was the point of the wave, and this referee's independent
re-computation confirms it in every load-bearing place. The single defect
found (R1) sits in the decorative layer (the ring/module presentation and the
top-degree generator), which is also where a machine cross-check is least
able to help — torsion-free rank-1 groups do not expose generator
ambiguities. That is a fitting place for the residual human error, and a
fitting note on which to recommend revision rather than rejection.

**Overall recommendation: accept with minor revision** (R1 mandatory; R2–R7
and the G3-gate strengthening recommended).

---

## 7. Artifacts of this wave

* `scripts/w30_referee_check.py` — the independent exact-integer verifier
  (7 check families: module indices per degree; the degree-3 witness; the
  τ-rule vs norm computations; the regular-rep Chern classes; the crux SNF
  and the order of `[τ²]`; the degree-6 quotient with the `[Δ] = 2[S₁]`
  membership tests; the free-rank inventory).
* `scripts/w30_referee_check_output.txt` — the transcript (all checks PASS
  in the directions asserted; the two *disconfirming* results are the module
  index table and the `[Δ] = 2[S₁]` triple membership test, i.e. exactly the
  R1 evidence).
* Mirrors in `glm/`; the report copied to the download folder; committed and
  pushed with the session PAT (the token handled via a transient
  `GIT_ASKPASS` helper, never echoed, never committed).
