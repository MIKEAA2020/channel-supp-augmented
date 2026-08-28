# Independent Audit 1 — `supp/FINAL_JOINT_COMPLETE_AUGMENTED.txt`

**File:** supp/FINAL_JOINT_COMPLETE_AUGMENTED.txt (1501 lines, LaTeX-in-markdown)
**Date:** 2026-08-28 · **Independence:** `post gpt audit corrections/` was not consulted.

## Verdict

The mathematical core (dimension theorem, centred radius, covering radius, replacement
profile, upper-envelope constructions, zero-error threshold) is essentially sound; I
recomputed all headline constants (see README) and they check out. However the file
contains **two false claims, two unproven claimed results, one corrupted proof block
(LaTeX-breaking), and several internal inconsistencies** between its own sections,
some of them introduced by the late "augmentations". As it stands the file would not
compile and cannot be published without fixes.

---

## Priority 1 — false or unproven statements

### P1-1 (L554, Corollary "Metric complementarity") — unproven chord-decomposition claim
> "The uniform depolarising instrument divides the extremal chord joining the boundary
> point I_*+ρ_n Δ⃗ and the extreme pure instrument at distance R_n in ratio ρ_n:(2−ρ_n)."

- The boundary point I_*+ρ_nΔ⃗ is constructed in the proof of the centred-radius
  theorem (Sec. 3), using a direction Δ⃗ built from two orthogonal isometries.
- The "extreme pure instrument" is the covering witness from Sec. 4, built from an
  unrelated channel Φ(X)=VP_SXP_SV†+Tr[(I−P_S)X]ω.
- The claim asserts (a) these two points are collinear with I_*, (b) they are opposite
  endpoints of a diameter, (c) I_* divides the segment in ratio ρ_n:(2−ρ_n). **None of
  these is shown anywhere.** The distance between the two points is never computed,
  and collinearity with the uniform instrument is not a consequence of anything proved.
- What *is* true and proved: ρ+R=2 and diam=2, so the two numbers sum to the diameter.
  The corollary should stop there ("numerical identity, not a chord theorem"), as the
  compact .tex version does. **Fix:** delete the second sentence of the corollary, or
  prove the witness pair is antipodal/collinear (it isn't, in general).

### P1-2 (L1005, Proposition "Monotonicity") — false claim about α_r
> "α_r need not be monotone in general…"

This is **false**. For any metric space K and any h∈C(S^{r+1},K), restricting h to the
equatorial S^r⊂S^{r+1} gives
min_{S^r} d(h(u),h(−u)) ≥ min_{S^{r+1}} d(h(u),h(−u)),
so sup over h of the left side (α_r) is ≥ the sup of the right side (α_{r+1}):
**α_{r+1}(K) ≤ α_r(K) for every metric space K**. The file itself uses exactly this
equatorial-restriction argument later in the same proposition for β_r. The sentence
"α_r need not be monotone" contradicts the mathematics and the file's own method.
**Fix:** state α_r is non-increasing; it also makes the sentence "α_D=0 ⟹ α_r=0 for
r≥D" automatic.

### P1-3 (L706, Corollary "General direction-space lower bound 1/d_A") — unproven in this file
> "the full direction-space Jordan construction gives a continuous S^r→Inst_n with
> antipodal distance at least 2/d_A, hence α_r≥1/d_A…"

- The corollary has **no proof** and no construction. The ingredients it needs appear
  nowhere in the file: M_X (the summed partial trace of the positive Jordan part) is
  never defined; the bound 0≤M_X≤I is never shown; the "filler"
  (1/n)(I_{A_0}/d_A − λM_X)⊗I_B/d_B is never shown PSD; the trace-preservation check
  Σ_k Tr_B J_k = I_{A_0}/d_A is never performed.
- Independently, I verified the underlying construction *is* recoverable: with
  X=X₊−X₋, Tr X₊=Tr X₋=:t, M_X=Σ_k Tr_B(X₊)_k, one has Tr M_X=1 and, since
  Tr_B(X₊)_k ≤ Tr(X₊)_k·I, M_X≤Σ_k Tr(X₊)_k·I=I, so with λ=1/d_A both
  λ(X₊)_k/Tr X₊ ≥ 0 and (I/d_A−λM_X) ≥ 0 hold; then
  ‖J(X)−J(−X)‖_1 = λ·‖X₊−X₋‖_1/t = 2λ = 2/d_A, and diamond ≥ trace via |ω_A⟩.
  So the claim is *true*, but **the file proves none of it**.
- **Fix:** give the full construction with the four verifications above (M_X≥0,
  M_X≤I, filler PSD, TP) and the continuity argument (t bounded away from 0 on the
  compact sphere).

### P1-4 (L1329–1331, Proposition "Orthogonal join", proof) — corrupted text, breaks LaTeX
The proof of the orthogonal-join proposition contains the definition repeated five
times inside a single sentence and a mangled summation index:
> "For y=(y_1,…,y_ℓ), set λ_i=‖y_i‖² and u_i=y_i/‖y_i‖ when y_i≠0. Define|For y=…|
> …Define|… (×5)
> H(y)=∑_{i:For y=(y_1,…,y_ℓ), set λ_i=…, Define|…ne≠0} λ_i h_i(u_i)"

This is a paste/edit corruption. The formula and the fivefold repetition will not
compile and the summation index `i:…Defineneq0` is invalid.
**Fix:** restore the single definition sentence and the sum index
`i:y_i≠0` (this proof is written correctly in `final.txt` L1285–1297 and in the
compact .tex).

### P1-5 (L185, Remark "Operational meaning") — wrong factor in the bias claim
> "‖Δ⃗‖_{⋄,inst}=sup_ρ Σ_k ‖(id⊗Δ_k)(ρ)‖_1 equals the optimal bias in discriminating
> two instruments with a single use…"

For channels the standard relation is p_succ = 1/2 + ‖Φ−Ψ‖_⋄/4, i.e. the
**bias is ‖·‖_⋄/4**, not ‖·‖_⋄. The file's own abstract and the compact .tex state the
correct "p_succ = 1/2 + ¼‖·‖" form. As written the remark claims the norm equals the
bias — off by a factor 4 (or, under a ±½-convention, by 2). Also "equals the optimal
bias … summed over unconditional outcome contributions" is not a statement that
follows from the displayed formula; the flagged-norm formula is fine, the
interpretation sentence is not. **Fix:** "the norm equals 4×(optimal bias)", or
re-state via p_succ = 1/2 + ¼‖·‖.

---

## Priority 2 — internal inconsistencies within the file

### P2-1 (L706 vs L1087) — 1/d_A strengthening not propagated
L706 (Corollary "General direction-space lower bound") claims
β_r ≥ max{ρ_n,1/d_A} for m_n≤r<D_n. But L1087 (Proposition "Gap structure") still
writes "for m_n≤r<D_n, β_r=ρ_n and U_r≥1, so bracket width at least 1−ρ_n", and the
Definition of β_r (L727–736) was never updated either. So the file simultaneously
asserts two different lower envelopes. If the 1/d_A bound is kept (it should be — it
is true), then the certified gap statements in L1087 and the abstract's
"α_r≥2/(nd_B·s) for intermediate" should use γ=max{ρ_n,1/d_A}.

### P2-2 (L693 vs definitions) — β^⋆ used but never defined
L693 (Theorem "Observable sphere beyond replacement") ends "Hence strengthened lower
envelope β_r^{⋆,(n)} with 1 for r≤L and ρ_n for L<r<D_n". A formal piecewise
definition (including the r≥D_n case, the capping at D_n−1, and the combination with
1/d_A) never appears; L1005 and L1087 then cite β_r^{⋆,(n)} as if defined. Note the
L693 semi-definition uses ρ_n (not γ) — the third inconsistency involving the same
quantity. **Fix:** one formal definition of β^{⋆} and of the final
β^{best}=max{β,β^{⋆},β^{dir}}, with β^{dir} also defined (see AUDIT-4).

### P2-3 (L1010, Theorem "Zero-error threshold") — misattributed argument
> "The forward direction uses β_r>0 for r<D_n **from Borsuk–Ulam**…"

β_r>0 for r<D_n comes from the replacement-sphere construction and the centred-ball
theorem, not from Borsuk–Ulam. Borsuk–Ulam is used (a) for the α_r=0 collapse at
r≥D_n (L73, L1087), and (b) inside the replacement profile proof. The attribution in
the theorem statement is wrong. **Fix:** "the forward direction uses β_r>0 (ball and
replacement constructions); Borsuk–Ulam supplies the converse-direction collapse at
r≥D_n" (or just delete the parenthetical).

### P2-4 (L1077, Remark "Error 1 barrier") — overclaim about which schemes are excluded
> "Hence no linear projection, Helly barycentre, or block-pinching scheme can achieve
> ε∈(0,1) in the bulk m_n≤r<D_n."

What is proved is only that **the three specific upper-bound constructions presented in
this paper** (constant code, convex/linear projection with Helly decoder, balanced
pinching) each give ≥1 in that range. The sentence overgeneralizes to *any* linear
projection or pinching scheme. Also note the first regime 0<r≤m_n−1 is excluded from
"bulk" but the sentence's own premises (admissible terms ≥1) cover it as well, where
β=1 makes sub-1 genuinely impossible — the scope wording should distinguish the two
regimes. **Fix:** restrict the claim to "the constructions in this paper".

### P2-5 (L68/L722 vs P1-2) — "middle range empty when d_A=1" vs monotonicity claims
With the (false) monotonicity claim removed and β^{⋆} defined, the sentence "The
middle range is empty when d_A=1" remains true for the *basic* β (D_{1,B}=nd_B²−1),
but the file should say so explicitly for the envelope actually used. Cosmetic once
P2-1/P2-2 are fixed; flagged for consistency.

### P2-6 (L554 phrase "extreme pure instrument at distance R_n")
Even ignoring the chord issue (P1-1): the covering witness Φ is trace-preserving but
is it *extreme* in the instrument body? Extremality is not shown anywhere. The word
"extreme" should be dropped or proved.

---

## Priority 3 — under-specified / robustness

### P3-1 (L693) — observable-sphere join: pure-σ reduction implicit
The join argument needs the observable sphere to be supported on the 2-dimensional
subspace span{|b₀⟩⊗|1⟩, |b₀⟩⊗|2⟩}; this requires fixing σ=|b₀⟩⟨b₀| **pure**. The
theorem's construction fixes "σ∈S(B)" arbitrary (for n≥2) and never states the pure
choice needed for the join; the complement dimension N_rep^obs=2(d_B−1)²+(n−2)d_B² is
correct **only** under the pure-σ reduction and the flag-block-diagonality, neither of
which is written out. The arithmetic (d_A²+N−3 via join formula) checks out given the
reduction. **Fix:** state the reduction explicitly ("taking σ pure, the support is …;
the trace-zero replacement sphere on the orthogonal complement has dimension N−2").

### P3-2 (L1010) — "iff" for the zero-error threshold relies on unrestricted decoders
The theorem says δ_r=0 iff r≥D_n. The "if" direction uses an affine-coordinate inverse
that is discontinuous (nearest-point projection Π_C is invoked in the compact .tex;
here the unrestricted-decoder convention is stated at L180). The file's Convention
(L179–181) says the decoder is unrestricted unless stated, so the claim is consistent,
but a reader could miss that the *continuous* decoder claim ("moreover… continuous"
in the .tex version) needs Π_C; here it is not mentioned. Minor wording gap.

### P3-3 (L330) — dimension proof wording
"Since every Choi block of I_* is positive definite, sufficiently small perturbations
in every direction of V remain block-positive" — fine, but "block-positive" is used
here for "positive semidefinite blocks" and again differently at L83 of the .tex
("Not block-positive but positive semidefinite terminology used"). Terminology
drift between versions. Cosmetic.

### P3-4 (L1077) — "covering-number bounds log N(ε)≤r log(1/ε)" as a barrier-breaking tool
This parenthetical is vague and its role ("Breaking the barrier requires nonlinear
manifold encodings, covering-number bounds …") is unmotivated; a covering-number bound
is a *lower*-bound-style counting statement, not obviously a construction that breaks
the ≥1 barrier. Either give the construction or delete the parenthetical.

---

## Priority 4 — LaTeX/editorial

- **L1329–1331** — see P1-4 (corruption).
- The figure (L1370–1420) and its caption (L1421) are internally consistent after the
  corrections (node at (9.5,0.45), ymax=2.0, U=1.75 for 0≤r<12, 1 for 12≤r≤13); the
  red curve segment to (12.99,1) and the blue segment to (12.99,0.25) slightly overrun
  xmax=13 — cosmetic.
- `\bm`, `\multirow`, `\dsfont` are loaded and unused (or unused for this file).
- Phantom references to "the main article" (figure caption: "to parallel the qubit
  envelope in the main text") — this supplementary file is standalone in the repo.
- L554: corollary numbered within the covering section but placed before the
  replacement section it conceptually completes — organizational nit.

## Verified-correct highlights (for balance)

- Dimension D_n, centred radius ρ_n, covering radius R_n, diameter 2: all correct,
  and the tightness witnesses (orthogonal isometries / POVM effect transfer) are
  genuinely maximal — verified numerically (README).
- Spectral-bound lemma (with max{0,·}) is correct; note Tr X=0 forces λ_max(−X)≥0,
  so the max{0,·} guard is cosmetic, not essential (the unguarded version in
  final.txt is also valid for this reason).
- Bipartite domination lemma and the a≤Kb ⇒ ½‖σ−τ‖₁≤1−1/K step: correct.
- Pinching-norm lemma, balanced-Q minimization, Helly–barycentre bound 2k/(k+1):
  correct.
- Replacement profile and d_A=1 isometry: correct.
- Degenerate-case bookkeeping (n=d_B=1 → D=0, ρ=+∞ by sup-convention, R=0): correct
  and consistent with the definition of the relative ball.
- Collapse case nd_B·s=2: correct, including D=d_A² (two-outcome POVMs) and D=3
  (trivial-input qubit channels).
