# WAVE 33 — THE SECOND REFEREE PASS: the v12 proof read end-to-end

**Date:** 2026-09-13
**Charge:** "a second referee-style pass over the v12 proof to confirm the
repairs read cleanly end-to-end" — Proposition 6.16 (*prop:cupsquare*, the
cup square on the flag quotient: a hand derivation), instruments paper
**v12**, source lines 1857–2138, together with its integration points
(Lemma 6.17, Remarks 6.18–6.19, the statement, the open-problem list, the
main-article sync clauses).

**Method.** The full seven-step proof was re-read line by line and re-derived
by hand a second time, with the repairs in place; the reading this time was
explicitly a *seam* reading — each repaired passage was checked in context,
against its neighbours, for dangling dependencies, contradictions with
unrepaired text, and claims silently changed by the patches. Every checkable
arithmetic claim was re-computed by a fresh exact-integer script
(`w33_second_pass_check.py`, transcript `w33_second_pass_output.txt`,
**178 checks, all PASS, exit 0**), written from scratch for this pass —
independent of the manuscript, of the wave-13C/28 machine data, and of the
w30/w31/w32 verifier scripts, whose code was not consulted. The honest debug
trail: four bugs in the *checker's own* code were caught and fixed before any
conclusion was drawn (a shadowed function name, an orbit-basis ordering
assumption, a wrong kernel-basis convention in the SNF routine — the kernel
of `P·A·Q = S` is the columns of `Q`, not of `Q⁻¹` — and a degree mismatch
in the σ₂-bookkeeping evaluation), each of which had produced spurious FAILs
against mathematics that re-derivation confirmed was correct.

---

## 1. Verdict, up front

**The repairs read cleanly end-to-end. The v12 proof is now a coherent,
self-consistent, line-checkable derivation from Step 0 to Step 7, and the
referee cycle of Waves 30–32 is closed.** All eleven repair hunks are present
(R1's five from Wave 31; R2–R7's six from Wave 32); all seven superseded
phrasings are gone; every load-bearing claim of the proof — including every
claim the repairs introduced — was independently re-verified, and the
cross-step dependencies that the repairs created or relied on all resolve.

**No mandatory corrections.** Two residual polish items are recorded below
(Findings F1 and F2): each is a single optional clause, neither affects any
assertion of the Proposition, and neither rises to the level of a repair —
they are noted so that a future revision may take them free of charge. In
journal terms: *accept; the minor revision has been executed and executed
well.*

**Recommendation: accept.** The epistemic chain on the Proposition now runs:
hand-derived (W29) → machine-certified (W13C) → independently re-implemented
(W28) → referee-verified (W30, findings R1–R7) → lattice-gated (W31, R1
applied + G3L) → referee-complete (W32, R2–R7 adjudicated and applied) →
**second-pass confirmed (W33, this wave: the repaired proof re-read and
re-verified end-to-end).**

---

## 2. What the second pass confirmed (per repair, in context)

### R1 (Wave 31, the substantive repair) — CONFIRMED, all five hunks, seam-clean

* **The statement clause** (lines 1872–1874): "$H^6(B;\mathbb Z)\cong\mathbb Z$,
  in which the discriminant class is twice a generator" — correct, and (see
  F2) *well defined*: the τ³-tail ambiguity of the Δ-lift in $H^6(BK)$ dies
  in the quotient, so the image of Δ in $H^6(B)$ is lift-independent. This
  was made a dedicated gate (M4, lift-independence for c = 0, 1, 2) and
  passes.
* **Step 2** (the orbit-sum invariant lattice, the equal-coefficient
  justification, the rational module, the index note "one in degrees
  $d\le2$, exactly the degrees in which the crux of Step 5 below works, then
  2, 2, 4, 8 in degrees 3 to 6", the witness $S_1=\tfrac12(\sigma_1\sigma_2
  -3\sigma_3+\Delta)$): every claim re-computed. The index table (M1: 1, 1,
  1, 2, 2, 4, 8 for degrees 0–6, by determinant of the change-of-basis), the
  four polynomial identities ($S_1+S_2$, $S_1-S_2=\Delta$, the witness, the
  Newton identity for $A_1$), the witness's non-membership and $2S_1$'s
  membership (M1, rank-matched rational solve, non-integral/integral exactly
  as the text asserts).
* **Step 3's display** ($H^6(BK)\cong\mathbb Z\{A_1,S_1,S_2,\sigma_3\}\oplus
  \mathbb Z/3\cdot\tau^3$ with the relations and the index-two note): the
  orbit counts (Burnside 4 for degree 3), the disjointness of the orbit
  supports (independence), and the index-two statement (M1 degree 3) all
  re-verified. The $H^4(BK)$ display is untouched and was already exact as a
  lattice (index 1 in degree 2, M1) — the referee's original observation
  that "the degrees the crux needs are exactly the safe ones" survives.
* **Step 7's quotient** (run "on the orbit-sum lattice of Step 3"):
  $\bigl(\mathbb Z\{A_1,S_1,S_2,\sigma_3\}\oplus\mathbb Z/3\tau^3\bigr)/
  \langle\sigma_1^3,\sigma_1\sigma_2,2\tau^3,\sigma_3\rangle\cong\mathbb Z
  \cdot\langle S_1\rangle$ — re-computed by SNF on the relation system in
  the paper's coordinates $(A_1,S_1,S_2,\sigma_3,\tau^3)$: free rank 1, no
  torsion (M4); the coordinate identities $\sigma_1^3=(1,3,3,6)$,
  $\sigma_1\sigma_2=(0,1,1,3)$, $\Delta=(0,1,-1,0)$ exact; the membership
  triple ($\Delta-2S_1$ a relation; $\Delta-S_1$ and $S_1$ not) exact; the
  torsion death ($2\tau^3=0$ with 2 invertible mod 3) and the top class
  $S_1$ with $\Delta=2S_1$ — all as printed. The closing rational-consistency
  clause ("where two is invertible and the discriminant class does
  generate") matches the corrected integral statement.
* **The remark knock-on** (rem:machine-certificate's residuals list now
  naming "the orbit-sum invariant lattice together with its finite index
  over the symmetric-function module" and "the twice-a-generator position of
  the discriminant in the top class"): present, and now *accurate* — the
  w31 gate G3L tests exactly those (containment, index, witness, generator),
  so the phrase "verified by an exact-integer script" no longer overstates.

### R2 (the corrected two-step d_r-vanishing) — CONFIRMED, mechanism complete

The repaired Step 1 parenthetical is mathematically airtight, and every
ingredient was re-derived and re-computed independently:

* **odd r:** target p-degree odd (sources live in even p-degree since
  $H^{\mathrm{odd}}(BK;\mathbb Z)=0$), and the forward reference is marked
  ("by Step 3 below") and *supported*: Step 3's closing sentence ("The odd
  cohomology $H^{\mathrm{odd}}(BK;\mathbb Z)$ vanishes, as the collapse
  argument shows") is present (line 2024) — the seam is closed. Gate M2
  re-proves the support: $\ker N\subseteq(T-1)M$ lattice-exactly on all of
  $\operatorname{Sym}^d$, $d\le 8$.
* **even r ≥ 8:** the source fibre-degree is 8 or 9 (M5: the exterior-algebra
  degree set is exactly $\{0,1,3,4,5,6,8,9\}$); the degree-9 classes die by
  $d_2$ (free coefficients, $\beta\sigma_1\ne0$) or $d_4$ (torsion
  coefficients, $2\tau^{a+2}\ne0$); the degree-8 σ₁-multiples are
  d₂-boundaries (via $d_2(\gamma z_1z_3z_5)=\gamma\sigma_1z_3z_5$), and the
  rest die under $d_4(\beta z_3z_5)=\beta(\sigma_2+2\tau^2)z_5\ne0$ — whose
  non-vanishing *on the E₄ page* is exactly the point the referee's own
  original sketch missed. The σ₁-divisibility lattice fact that closes it —
  $\{\beta\in M_d:\sigma_1\mid\beta\}=\sigma_1\cdot M_{d-1}$ **as lattices** —
  is re-verified by M5 for degrees 1–8 (rank match + index 1, degree by
  degree, via the evaluation kernel at the σ₁-root locus), and the σ₂-side
  bookkeeping ($\{\beta:\sigma_1\mid\beta\sigma_2\}$ = the same σ₁-multiples;
  $\sigma_2$ at the locus $\chi_3=-\chi_1-\chi_2$ is $-(x^2+xy+y^2)\ne0$) for
  degrees 2–8. The triangular-divisibility clause ("divisibility by
  $\sigma_1=\chi_1+\chi_2+\chi_3$ is triangular in the monomials") is the
  monic-in-χ₃ division argument — sound, and now load-bearing in exactly the
  right place.

### R3 (the (2,2)-clause) — CONFIRMED

The Step 5 enumeration now reads $E_2^{4,0}$, $E_2^{3,1}=E_2^{1,3}=0$, **and
$E_2^{2,2}=0$ (the exterior algebra $\Lambda(z_1,z_3,z_5)$ has no class of
degree two)**, and $E_2^{0,4}$ — which is now genuinely enumeration-complete:
the five bidegrees of total degree 4 are all accounted for (M5: no degree-2
fibre class). The incoming-image list ("$d_2(\sigma_1z_1)=\sigma_1^2$ and
$d_4(z_3)=\sigma_2+2\tau^2$") is complete *given the R4 pin* — see below.

### R4 (the b-pin, load-bearing) — CONFIRMED, both hunks

The display $\iota^*c_1=\sigma_1+b\,\tau$ with the honest parenthetical ("the
restriction to the fibre pins only the free components"), and the pinning
chain "Hence $0=s^*(\iota^*c_1)=s^*(\sigma_1+b\,\tau)=bu$ … so $b=0$" —
re-derived: the regular representation's Chern classes in $\mathbb Z[u]/(3u)$
re-computed (M6: $(1+u)(1+2u)=1+3u+2u^2$, so $c_1=0$, $c_2=2u^2$, $c_3=0$),
the section arithmetic ($s^*\sigma_1=0$, $s^*\tau=u$, $s^*\tau^2=u^2$,
$s^*\tau^3=u^3$) consistent, and the pins $(b,\varepsilon,\varepsilon')
=(0,2,0)$ forced exactly as printed. **The load-bearing consequence is real
and now supplied:** with b pinned, $d_2(\tau z_1)=\tau\sigma_1=0$ (used in
the Step 5 incoming-image completeness and in Step 7's degree-3 run) is
line-checkable; unpinned, the crux would die — the counterfactual (M3: with
the extra relation $\langle\tau^2\rangle$ the quotient is the trivial group)
re-computed and confirmed. Step 5's completeness now rests on an established
fact rather than a silent dependence — exactly the repair the adjudication
promised.

### R5 (the two-step quotient) — CONFIRMED

The repaired passage (quotient out the direct summand $\mathbb Z\sigma_1^2$
first; then the *single* incoming relation $\sigma_2+2\tau^2$, a class of
infinite order; "an element of order three never lies in the subgroup
generated by an infinite-order class") is logically valid as scoped: after
the direct-summand quotient there is exactly one relation, and the
order argument applies to it. The sum-quotient itself was re-verified
(M3: SNF gives $\mathbb Z/3$ with $[\tau^2]$ of order 3 generating and
$[\sigma_2]=-2[\tau^2]$; the two-step's intermediate
$(\mathbb Z\sigma_2\oplus\mathbb Z/3\tau^2)/\langle\sigma_2+2\tau^2\rangle$
likewise), and the logical-gap witness ((2,2) in the sum but in neither
summand) re-exhibited. The old per-subgroup sentence is gone (P2).

### R6 (the deck-convention parenthetical) — CONFIRMED

The parenthetical ("the identification passes through the inversion
$K\backslash U(3)\cong U(3)/K$ … the sign squaring away in
$x^2=\gamma^*(\tau^2)$") is present at the identification sentence, correct
($(\pm1)^2=1$), and does not interfere with the surrounding functoriality
argument ($\kappa=\pi\circ\gamma$ is asserted on the rigorous part, as the
first referee noted).

### R7 (the τΔ marking) — CONFIRMED

The marking ("is lift-dependent: the class of $\Delta$ in $H^6(BK;\mathbb Z)$
is fixed only up to a $\tau^3$-tail, and
$\tau\cdot(\Delta+c\,\tau^3)=c\,\tau^4\ne0$ when $c\ne0$; it is not used
below") is present, and its scoping is accurate in both directions: the
claim $\tau\Delta=0$ at the leading level is correct (M2: Δ contains no
$\chi_1\chi_2\chi_3$ monomial), the three lift-values are distinct (M8), and
the downstream uses really do avoid it — the crux and the degree runs use
only the σᵢ-instances, which the text correctly marks unconditional via
Step 4's pins. The *graded class of the alternating Δ* rewording (replacing
the old "alternating polynomial") is an accurate description of what the
τ-rule sees.

---

## 3. Findings (both optional; one clause each; no mathematics affected)

### F1 (nano, presentational) — Step 1's repaired text uses σ/τ before their definitions, unmarked in the even-r clause

The R2 repair moved the fibre-degree-8/9 killing computations into Step 1;
they use $\sigma_1$, $\sigma_2$, $\tau$ (and the transgression value
$\sigma_2+2\tau^2$, which Step 4 pins) — the first occurrences are at source
lines 1931 and 1933, while $\sigma_i$ is introduced at line 1969 (Step 2),
$\tau$ at line 1983 (Step 2's end), and the value $\sigma_2+2\tau^2$ is
pinned at line 2047 (Step 4): thirty-eight lines of forward dependency.
The odd-r clause carries its marker ("by Step 3 below"); the even-r clause
carries none. There is no logical circularity — Step 2/3/4 are established
by independent means (the $BT^3$-page, the norm model, the splitting) — but
a linear reader meets the symbols before their definitions. A single
parenthetical, e.g. "(the transgression values and the τ-arithmetic used
here are established in Steps 3 and 4 below)", would close it. A second,
smaller wrinkle in the same sentence: the lead-in "the fibre classes there
are *boundaries* before the $E_8$-page" conflates two death modes — the
σ₁-multiple degree-8 classes are indeed d₂-boundaries, but the degree-9 free
classes and the remaining degree-8 classes die as *non-cycles* (nonzero
differentials), not as boundaries; the elaborating sentences that follow are
precise about exactly this distinction, so only the lead-in word is loose.
"Killed" for "boundaries" would fix it.

### F2 (nano, presentational) — the lift-independence of Step 7's orbit-sum quotient could be stated in half a clause

Step 3's display $H^6(BK)\cong\mathbb Z\{A_1,S_1,S_2,\sigma_3\}\oplus
\mathbb Z/3\cdot\tau^3$ presents the orbit sums as named classes; strictly,
$S_1$, $S_2$ (and any Δ-lift) are defined only up to τ³-tails — the display
chooses a splitting, and only $A_1$ (a σ-polynomial, $A_1=\sigma_1^3-3\sigma_
1\sigma_2+3\sigma_3$) and the pinned σᵢ are canonical. Step 7 then computes
the quotient on these classes. The computation is nonetheless
**lift-independent**: the relation $2\tau^3=0$ (with 3 invertible... rather,
2 invertible mod 3) kills the τ³-ambiguity in the quotient, so every choice
of lifts gives the same $H^6(B)=\mathbb Z\cdot\langle S_1\rangle$ with
$[\Delta]=2[S_1]$ — verified as a dedicated gate (M4, lift-independence for
c = 0, 1, 2). This is also exactly what makes the *statement's* phrase "the
discriminant class is twice a generator" well defined in $H^6(B;\mathbb Z)$
despite the R7-marked ambiguity in $H^6(BK)$. The paper never says so
explicitly; a half-clause in Step 7 ("the τ³-tail ambiguity of the orbit-sum
lifts dying with the torsion in the quotient, so the quotient and the
discriminant's position in it are lift-independent") would close it.

**Neither finding is a defect in a claim.** Both are one-clause polish
opportunities of the same species as R7 was (a marking), strictly weaker:
nothing downstream depends on them, and the proof as printed is already
checkable line by line. They are recorded for a future revision's
convenience, not as conditions of acceptance.

---

## 4. The integration points (re-assessed, all clean)

* **Lemma 6.17 (lem:flag-cohomology).** Unchanged by the repair waves (it
  uses degrees ≤ 4 only); its proof's references to Proposition 6.16 ("proves
  $x^2\ne0$ by an integral transgression computation, independent of the
  Cartan–Leray page") and to the machine certificate ("agrees with the full
  cohomology tuple") remain accurate against the v12 text — the tuple, and
  now the corrected top-degree statement, are what the proposition asserts.
* **Remark 6.19 (rem:machine-certificate).** The residuals list names the
  lattice layer and the twice-a-generator position (R1's fifth hunk), which
  the G3L gate genuinely certifies; the earlier phrase "a self-contained
  invariant-theory step" (flagged for attention by the first referee's §5)
  now points at a correct, self-contained step — the substance of the
  referee's concern was addressed by the correction itself, and no rewording
  is needed.
* **Remark 6.18 (rem:flag-literature).** The differentiation clause ("the
  torsion-survival argument of Step 5 handling the integral 3-torsion layer")
  remains accurate — Step 5's argument is unchanged in substance by the R3/R5
  phrasing repairs.
* **The statement.** Internally consistent with Step 7 (the tuple, the
  generators, the twice-a-generator clause), and the "discriminant class" is
  well defined in $H^6(B)$ (M4's lift-independence gate) even though the
  $H^6(BK)$-level ambiguity is (correctly) marked in Step 3.
* **The main article (v10, unchanged).** The sync clauses are prose-level
  ("through a flag-quotient computation that is hand-derived,
  machine-certified, and independently re-implemented"; "the cyclic flag
  quotient underlying that premise") and contain no proof internals (P5:
  verified — no orbit-sum, lattice-index, or pin notation appears there);
  nothing in the v12 repairs creates a drift. The main article correctly
  stays at v10.
* **The open problem (vi) discharge.** Unaffected by this pass; the
  proposition it cites is now the twice-refereed, twice-repaired version of
  itself.

---

## 5. The referee's summary

The first pass asked whether the proof was *correct*; this pass asked
whether the *repaired* proof *reads* as a proof — whether the eleven
surgical hunks, each verified in isolation by their own waves, compose into
a text a reader can walk through without ever tripping over a seam. They
do. The forward-dependency structure is sound (and where it exists — Step
1's use of Steps 3–4 — it is either marked or, per F1, one clause short of
being marked); the load-bearing dependency created by the repairs (Step 5's
completeness resting on the R4 pin) is supplied rather than silent; the
superseded statements are gone everywhere, including in the rendered PDF;
the corrected top-degree story (orbit-sum lattice → index → quotient →
$S_1$ → $\Delta=2S_1$) is told consistently in the statement, Steps 2/3/7,
and the certificate remark; and the two independent verification layers
(w31's G3L, w32's twelve gates) are now joined by this pass's 178 checks,
which re-derive the whole chain from the orbit decomposition up. The
residue — two optional clauses — is the honest size of what remains.

The mathematics, final state: $x^2\ne0$ in $H^4(B;\mathbb Z)$; the additive
tuple $(\mathbb Z,0,\mathbb Z/3,\mathbb Z/3,\mathbb Z/3,\mathbb Z/3,\mathbb
Z)$; $x$ generating $H^2$ and $x^2$ generating $H^4$; $H^6(B;\mathbb Z)
\cong\mathbb Z$ with the discriminant twice a generator — hand-derived,
machine-certified, independently re-implemented, referee-verified,
lattice-gated, referee-complete, and now **second-pass confirmed**.
$\mathrm{thm}$:state-d2 and $\delta_2(\mathcal D(\mathbb C^3))=4/3$
untouched; the ququart bracket $[4/3,3/2]$ OPEN; the W23 stop stands.

**Overall recommendation: accept** — the revision requested by Wave 30 has
been executed (W31: R1; W32: R2–R7, adjudicated) and survives a full second
read; the two polish items F1/F2 are optional.

---

## 6. Artifacts of this wave

* `scripts/w33_second_pass_check.py` — the independent exact-integer
  verifier (13 gate families, 178 checks: the seam/textual layer P1–P5 and
  the mathematical layer M1–M8, including the new lift-independence gate
  M4 and the σ₁/σ₂-bookkeeping gates M5).
* `scripts/w33_second_pass_output.txt` + `scripts/w33_second_pass_check.json`
  — the transcript and the structured record (all PASS, exit 0), with the
  honest debug trail of the four checker-code bugs caught en route.
* `glm/WAVE33_SECOND_REFEREE_PASS.md` — this note.
* `glm/w33_report.tex` + the compiled PDF — the LaTeX rendition.
* The download folder: the PDF + this note.
* Committed and pushed with the session PAT (the token handled via a
  transient `GIT_ASKPASS` helper, never echoed, never committed, the helper
  deleted after use).
