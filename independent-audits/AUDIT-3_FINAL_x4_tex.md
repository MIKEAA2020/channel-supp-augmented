# Independent Audit 3 — `supp/FINAL_FULL_INSTRUMENT_GEOMETRY.tex` and its three byte-identical twins

**Files:** `FINAL_FULL_INSTRUMENT_GEOMETRY.tex`, `FINAL_JOINT_COMPLETE_AUGMENTED.tex`,
`FINAL_JOINT_EVALUATED_STRENGTHENED.tex`, `FINAL_RIGOROUS_ELEVATED_COMPLETE.tex`
**Identity check:** all four have md5 `fc632af4cb617a2e1849fe0df49eb8ac` (271 lines,
25221 bytes) — one audit covers all four; the differing filenames describe content
that does not differ ("evaluated", "strengthened", "rigorous", "elevated" are
aspirational labels).
**Date:** 2026-08-28 · **Independence:** `post gpt audit corrections/` was not consulted.

## Verdict

This is a compressed re-statement of the long `.txt` manuscripts with several claims
upgraded (monotone α, 1/d_A bound, observable join, exact collapse). As a mathematical
document it is **not publishable as-is**: the proof of the flagship centred in-radius
theorem contains a **false two-step operator inequality**, several "lemmas" it cites
**do not exist in the file**, the 1/d_A "theorem" has a **statement-only proof stub**
with an essential ingredient never defined, the spectral-bound "lemma" has **no
proof at all**, and the file **will not compile** (undefined macros, no bibliography).

---

## Priority 1 — mathematical defects

### P1-1 (L92, proof of Theorem "Centred in-radius") — false inequality chain
The proof of ρ_n=2/(nd_B·s) rests on:
> ‖Z_k‖_∞ ≤ ‖Tr_B|Z_k|‖_∞ ≤ s‖Z_k‖_1/d_A.

**Both inequalities are false in general.**
- First step: take Z_k = |MES⟩⟨MES| (d_A=4, d_B=2): ‖Z_k‖_∞=1 while
  ‖Tr_B|Z_k|‖_∞=‖I/4‖_∞=1/4, so 1 ≤ 1/4 fails.
- Second step: take Z_k=|ψ⟩⟨ψ|⊗I_B with d_A=4, d_B=2 (so s=2): ‖Tr_B|Z_k|‖_∞=2 while
  s‖Z_k‖_1/d_A=2·2/4=1, so 2 ≤ 1 fails.
- And such blocks *can* occur as blocks of a direction: Z₁=|ψ⟩⟨ψ|⊗I_B,
  Z₂=−|ψ⟩⟨ψ|⊗I_B satisfies Σ_k Tr_B Z_k=0.

The correct route is the spectral-bound lemma (bounding λ_max(−X) of the *flagged*
Choi by s‖Δ⃗‖/2d_A — proved in the long `.txt` versions). The compact file states
that lemma at L265 but **never proves it** (see P1-3), so as written the theorem's
proof is unsound. Note: the theorem *statement* is true (independently verified, and
proved correctly in the long versions) — the defect is in this proof.

### P1-2 (L111–115, Theorem "Full-direction") — proof stub with undefined ingredient
The theorem claims α_r≥1/d_A via an explicit construction, and the proof builds
P=Z₊/t, Q=Z₋/t, common marginal μ, and the instruments
J^±=λP+(1−λ)ν⊗τ₀ with ν=(I_{A₀}/d_A−λμ)/(1−λ). The **essential verification that
ν≥0 is missing**: the text never proves I/d_A−λμ≥0 (it would need λ≤1/(d_A‖μ‖_∞),
i.e. ‖μ‖_∞≤1, which is true since μ=Tr_{BC_n}P is a state marginal of a state with
marginal I/d_A… but none of this appears). The displayed "Improved λ(Z)=…" fragment at
the end is a stub, not integrated. Also, the proof's fidelity argument
"if t=0 then … sum zero ⟹ each zero ⟹ W=0" (L126) mixes up an operator W with the
scalar sum: the displayed string "0=Tr_{BC_n}W=Σ_{b,c}⟨b,c|W|b,c⟩≥0, each ≥0, sum
zero ⟹ each zero" writes ⟨b,c|W|b,c⟩ (a scalar) where it means the partial-trace
*operators* (I⊗⟨b,c|)W(I⊗|b,c⟩); the conclusion W=0 is right but the notation is
scalar/operator-conflated. The theorem's claim is recoverable and true (see
AUDIT-1 P1-3), but this file proves neither the ν≥0 step nor states the M_X version.

### P1-3 (L265–266, Lemma "Spectral bound") — statement without proof
The centred in-radius theorem (P1-1) depends on this lemma, which the file states
without any proof. The long `.txt` versions prove it (and their proof is correct).
As the linchpin lemma of the paper, this must carry its proof or a citation.

### P1-4 (L124–128, Theorem "Full-direction", fidelity step) — scalar/operator conflation
Described under P1-2: the chain "0=Tr_{BC_n}W=Σ_{b,c}⟨b,c|W|b,c⟩≥0, each ≥0, sum
zero ⟹ each zero ⟹ W=0" writes a *sum of scalars* equal to an *operator* (Tr_{BC_n}W).
Correct statement: Tr_{BC_n}W = Σ_{b,c}(I_{A₀}⊗⟨b,c|)W(I_{A₀}⊗|b,c⟩) = 0 with each
summand PSD, hence each summand = 0, hence W=0. The argument is right, the notation
is not; as written the displayed identity is type-inconsistent.

---

## Priority 2 — missing content / self-references

### P2-1 (L112) — "Lemma replacement isometric homeomorphism" does not exist
The Replacement-profile proof cites a lemma ("Lemma replacement isometric
homeomorphism") that is never stated in this file (in the long versions it is
Lemma "Replacement-instrument isometry" with a full proof). The proof of the profile
formula for RepInst depends on it.

### P2-2 (L29, L193, L212) — Helly/convex-projection machinery cited but never proved
The Bracket corollary (L177) and the zero-error theorem cite "convex-projection"
bounds 2(D−r)/(D−r+1) and Helly selection, but the file contains no statement or
proof of the convex-projection upper bound nor of the Helly–barycentre argument
(they are Proposition "Convex-projection" in the long versions). The pinching
theorem (L197) is stated with a one-line proof sketch that omits the surjectivity
checks — a statement-only item.

### P2-3 (L215, proof of "Zero-error continuous decoder") — compressed beyond verifiability
"affine c:A→R^{D_n} homeomorphism onto compact convex C, nearest-point projection
Π_C…" — the argument is correct in outline (independently verified: injective affine
coordinates + 1-Lipschitz metric projection onto a closed convex set), but the file
never defines A^{(n)}'s affine structure or proves c is a homeomorphism onto its
image; given P2-1/P2-2, the reader cannot reconstruct it from this file alone.

### P2-4 (L83) — editorial sentence left inside the Dimension proof
> "Not block-positive but positive semidefinite terminology used."

This is a self-addressed editing note, not a mathematical sentence, sitting inside
the proof of the Dimension theorem.

### P2-5 (L55) — corrupted sentence in the Monotonicity proposition
> "Lower envelope piecewise non-increasing non-increasing."

Doubled phrase. Also, this proposition (L53–64) is otherwise correct — it states the
*true* monotonicity α_{r+1}≤α_r, in contrast to the false "α_r need not be monotone"
claim in the augmented `.txt` (AUDIT-1 P1-2). The two files contradict each other;
this file is the right one.

### P2-6 (L240–241, figure) — schematic axis is not the stated geometry
The tikz figure draws the β envelope with breakpoints at x=2 and x=6 labelled L and
D_n, but for the caption's own example (L=6, D=28) a linear r-axis would put L at
≈21% and D_n at the right edge — the axis is an unstated non-linear compression, and
the γ plateau (drawn at height 1.5 with caption γ=0.5) is scaled arbitrarily while
the y-axis is labelled β_r. The caption's red-U description ("R=1.75, 1 from output
pinching") is **not drawn** (no red curve exists in the figure). Either draw U_r or
drop it from the caption.

---

## Priority 3 — LaTeX/compile defects (file will not compile)

- **Undefined macros:** `\Lin` (L250), `\Herm` (L147), `\Sstate` (L256), `\rank`
  (L45), `\coind` (L45, L233) are used but **never defined** in the preamble; only
  `\Inst`, `\RepInst`, `\Tr`, `\id`, `\coind`… in fact `\coind` *is* defined
  (L18) — but `\Lin`, `\Herm`, `\Sstate`, `\rank` are not. Compilation fails.
- **No bibliography:** the file contains no `\cite` and no
  `\begin{thebibliography}` — acceptable for a self-contained note, but the file
  also cites nothing, so external claims (Borsuk–Ulam, Schur, diamond stability)
  are unreferenced.
- **Proof-stub formatting:** several "proofs" are single run-on sentences
  (e.g., L247–256), including the no-programming theorem whose statement (L247)
  omits the dim E>1 hypothesis that its own proof requires (infinitely many distinct
  unitaries exist only for dim E>1).
- **L44 (abstract):** "No filler lines." — meta-commentary inside the abstract of a
  formal document.

## Verified-correct highlights (for balance)

- The monotonicity proposition here is correct (equatorial restriction), including
  the U_r non-increasing claim (admissible bounds at r remain admissible at r+1;
  2(D−r)/(D−r+1) decreases).
- The diameter theorem and its two-case tightness (orthogonal outputs / distinct
  deterministic outcomes) are correct.
- The replacement-profile theorem's Borsuk–Ulam argument (affine coordinates in
  R^{nd_B²−1}) is correct, given the missing isometry lemma.
- The collapse theorem (nd_B·s=2 ⟹ ρ=R=1, δ=1 below D_n) is correct, including both
  case identifications.
- The observable theorem (E_±=(I±K)/2, eigenvector witness, α_r=1 for r≤d_A²−2) is
  correct, including the channel case n=1.
- The join arithmetic (d_A²+N−3) and the L-threshold table values (28/6/2/3 and
  63/6/7/8) are correct given the pure-σ reduction (see AUDIT-1 P3-1).
- The pinching lemma's roots-of-unity proof sketch is correct.
