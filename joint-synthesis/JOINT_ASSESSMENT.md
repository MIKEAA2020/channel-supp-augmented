# Joint Assessment of All Audits and Corrected Synthesis

**Date:** 2026-08-28 · **Repo:** `MIKEAA2020/channel-supp-augmented`

## 0. Method, scope, and order-bias policy

**Sources considered.** (i) The six audit files in `post gpt audit corrections/`:
`chatgpt suggested.txt` (50-point audit), `deepseek.txt`, `qwen.txt`, `qwen 2b.txt`,
`qwen2a.txt`, `qwen3.txt` (an 11-batch iterative transcript); and (ii) my four
independent line-level audits in `independent-audits/`
(`AUDIT-1`–`AUDIT-4`), which were produced **before** reading the folder.

**Adjudication policy.** Every finding is adjudicated on mathematical and physical
merit alone. Findings are grouped by topic and ordered by mathematical priority, not
by the order in which an audit stated them; where several audits make the same
finding, they are listed alphabetically. No audit is presumed correct because it
appeared earlier or in a "priority" list — the existing
`supp/AUDIT_RESPONSE_AND_CORRECTED_VERSION.tex` does exactly that, and its own
Priority-4 ordering is internally inconsistent (see §4 item 4).

**Inventory mismatch (provenance).** `AUDIT_RESPONSE...tex` claims a joint evaluation
of 10 audit files including `1.txt`, `2.txt`, `assistant a/b`, `deepseek bulk gap`,
`gpt aisure`, `grok1`, `qwen bulk gap`. Only six audit files exist in the repo:
`chatgpt suggested.txt`, `deepseek.txt`, `qwen.txt`, `qwen 2b.txt`, `qwen2a.txt`,
`qwen3.txt`. Six of the cited names have no file in the repository. This assessment
therefore covers the **ten audits that actually exist** (six in-folder + four
independent), and treats consensus claims about absent files as unverifiable.

**Verification.** Every formula invoked below was recomputed independently; the
headline numbers check out (D=28, ρ=0.25, R=1.75, γ=0.5, L=6 for (2,2,2); D=63,
γ=1/3, L=8 for (3,2,2); convex bound >1.75 on 0≤r<12; r_out=12, r_in=14;
Π_∞=2d_A·max{d_A,d_B}; exact gap R−1=1−ρ at r=0).

---

## 1. Adjudication ledger

Legend: **V** = valid, accept; **P** = partially valid, accept after correction;
**I** = invalid / overstated, reject or replace. "Sources" = audits making the
finding (IA1–IA4 = my independent audits; CG = chatgpt suggested; DS = deepseek;
QW = qwen; Q2B = qwen 2b; Q2A = qwen2a; Q3 = qwen3).

### A. Core topology and profile results

| # | Finding | Sources | Ruling | Action in synthesis |
|---|---|---|---|---|
| A1 | "α_r need not be monotone" is false; equatorial restriction gives α_{r+1}≤α_r for **every** metric space; once α_D=0, α_r=0 for r≥D | IA1, IA3, CG1, DS1, QW1, Q2A2, Q2B5, Q3(1,9,11) | **V, unanimous** | Proposition 4.2 with proof; the cutoff corollary is made automatic |
| A2 | "General 1/d_A lower bound" unproven as written (naive Jordan map X→X₊/TrX₊ does **not** produce instruments: wrong marginal, wrong space) | IA1, CG2, QW2, Q2A3, Q2B2, Q3(2,4.1,9) | **P→V** | The objection is correct; the claim itself is **true and now proved**: full-direction theorem with the ν-correction state (see §2.1). Adopted as Theorem 4.5 |
| A3 | deepseek's **retraction** of 1/d_A to a mere conjecture | DS2 | **I (superseded)** | The ν-mixing construction (QW/Q2A/Q2B/Q3, independently verified by IA1) proves the theorem; the conjecture is withdrawn in favour of the theorem |
| A4 | Replacement-profile proof: for r>m use equatorial S^m⊂S^r, then Borsuk–Ulam | CG9, DS(batch3 §2), Q3(4.2, 11.8) | **V** | Theorem 4.4 proof, fixed wording |
| A5 | The Jordan map X→X₊/t is a continuous image, not an embedding — keep the qualification | CG44, DS(list 13) | **V** | Stated explicitly in §4 |
| A6 | Coindex +∞ makes the intrinsic corollary vacuous; state Hausdorffness use; radial map needs q+1≤D | CG27, CG28, DS(list 6, 11), Q3(5.1, 5.2, 7.6) | **V** | Remarks after Corollary 5.8 |
| A7 | Diameter = 2 should be a proposition; stop alternating "≤2"/"=2" | CG14, DS(batch2 §3), QW16, Q3(7, 11.5) | **V** | Proposition 3.8 |
| A8 | Monotonicity of δ_r (padding) and of U_r (shrinking admissible set) | Q3(1, 9), DS | **V** | Included in Proposition 4.2 |
| A9 | "continuous image" argument in the top-subcritical width: show 2(m−r)/(m−r+1)=1 at r=m−1 | CG32, DS(list 14), Q3(11.7) | **V** | Corollary 5.11 with explicit computation |

### B. Exact parameters (dimension, radii, covering)

| # | Finding | Sources | Ruling | Action |
|---|---|---|---|---|
| B1 | "Exact metric parameters of the body" overclaims; enumerate exact vs certified | IA1–IA4, CG3/41, DS3, QW8, Q2A1, Q3(8, 10, 11.1, 11.2) | **V, unanimous** | New title, abstract, Remark 2.7 |
| B2 | Affine-dimension proof: "block-positive" ≠ "positive semidefinite"; use PD blocks + relative interior | CG19, DS(list 1), Q3(4.1, 11.4) | **V** | Proposition 3.1 proof |
| B3 | Spectral lemma: state max{0,λ_max(−X)}, spaces A_0⊗B⊗C_n, |v,k₀⟩ notation, Tr Y=0 step, ⟨w|Y|w⟩≥−TrY₋ derivation | CG10, DS(list 3), Q3(11), IA3 (compact .tex states it without proof) | **V** | Lemma 3.2 with full proof |
| B4 | **Compact `.tex` only**: the ball proof's chain ‖Z_k‖_∞≤‖Tr_B|Z_k|‖_∞≤s‖Z_k‖₁/d_A is false in both steps (counterexample: MES block, d_A=4,d_B=2) | IA3 (unique) | **V** | Replaced by the spectral-lemma proof (Lemma 3.2 → Theorem 3.3) |
| B5 | POVM branch of centred radius: write Δ₁,Δ₂ as maps A→C with Δ₁+Δ₂=0; J_F=P^T/d_A | CG11, DS(list 4), Q3(11) | **V** | Theorem 3.4 proof |
| B6 | Covering-radius optimality: explicit G=U(B)×S_n action, invariance, convexity, Jensen, Schur, permutation average → I_* | CG6, DS(batch2 §2), QW9, Q2A5, Q2B3, Q3(10) | **V, unanimous** | Theorem 3.6 proof |
| B7 | Covering equality witness is not an "extreme pure instrument"; say "channel acting as a pure isometry on the selected s-dimensional subspace" | CG39, DS(list 7), Q3(6.2) | **V** | Theorem 3.6 proof |
| B8 | **New (this pass):** final.txt/AUGMENTED say the witness's "trace distance is 2(1−1/(nd_Bs))" — that is the **trace norm**; the trace distance is 1−1/(nd_Bs). The instrument norm equals the trace norm of the flagged difference, so the theorem's number is right but the label is wrong | IA2/IA1 (cross-checked here) | **V** | Theorem 3.6 states ‖σ−τ‖₁=2(1−1/K) |
| B9 | Metric-complementarity "extremal chord" sentence unsupported (independent witnesses, no collinearity) | IA1, CG15, DS(batch2 §3), QW10, Q2A5, Q3(7, 11.5) | **V, unanimous** | Corollary 3.9 keeps the numerical identity ρ+R=2 only |
| B10 | I_* is "an optimal centre", not necessarily "the" centre | CG45, DS(list 13) | **V** | Wording throughout |
| B11 | Global in-radius open; do not claim it; optional conjecture | CG3, QW14, IA1 | **V** | Remark 3.7 |
| B12 | Degenerate case n=d_B=1: singleton, D=0, V={0}, ρ=+∞ (sup convention), R=0, widths 0; enforce nd_B>1 globally | CG46, DS(list 18), QW17, Q3(11.3), IA1/IA2 (final.txt abstract contradicts its own remark) | **V** | Remark 2.6; abstract opens with the assumption |
| B13 | Bipartite-domination proof: restrict to supp ρ_R, rank bound on V explicit | CG13, DS(list 5), Q3(11.9.1) | **V** | Lemma 3.5 |
| B14 | Ball theorem: note blockwise PSD + marginal I/d_A forces each component trace-nonincreasing (completeness) | CG15-adjacent, IA3 (compact .tex omits) | **V** | One line in Theorem 3.3 proof |

### C. Compression widths and decoders

| # | Finding | Sources | Ruling | Action |
|---|---|---|---|---|
| C1 | State the convention: continuous encoder, unrestricted decoder; "continuous compression" is misleading | IA1, CG7/8/30, DS(batch3 §1), QW11, Q2A6, Q2B4, Q3(9, 11) | **V, unanimous** | Convention 5.1, Definition 5.1 |
| C2 | Zero-error threshold: for r≥D exact decoding can be chosen **continuous** (affine c + nearest-point projection Π_C); converse holds via β>0 | DS(batch3 §1), QW11, Q2A6, Q3(9) | **V** | Theorem 5.6 (stronger than original) |
| C3 | Zero-error converse: g(f(h(u)))=g(f(h(−u))) because **codes coincide**, not by continuity of g | CG8 | **V** | Proof of Theorem 5.6 / Corollary 5.7 |
| C4 | Helly decoder is existential, not constructive; pinching is constructive | CG16, DS(batch3 §8), QW13, Q3(Batch3, 11) | **V** | "certified upper bounds"; Remark 5.3 |
| C5 | Pinching-norm proof: roots-of-unity identity + normalized test vector | CG17, DS(batch3 §9), Q3(4.3) | **V** | Lemma 5.4 |
| C6 | Input-pinching conjugation Ĵ_{Φ∘P_A}=(P_{\bar A_0}⊗id_B)Ĵ_Φ with conjugate basis | CG18, DS(list 6), Q3(4.4) | **V** | Theorem 5.5 |
| C7 | **final.txt only:** "‖Φ⊗id‖_⋄≤‖Φ‖_⋄ by submultiplicativity" is false — diamond is multiplicative under tensoring (equality), submultiplicativity is composition | IA2 (unique), corroborated by AUDIT_RESPONSE P1-5 | **V** | Deleted; stability used correctly only where needed |
| C8 | Certified bracket width: U−ρ≥1−ρ bounds the **certified interval**, not the unknown true width | IA1, CG33, DS(list 9), Q3(7.2, 11) | **V** | Proposition 5.13 wording |
| C9 | Collapse nd_Bs=2: lower bound 1 throughout r<D comes from the centred ball (radial map at ρ_n=1), not only from replacement spheres | CG25, DS(batch2 §4), Q3(7.3, 11) | **V** | Theorem 5.12 proof |
| C10 | Π_∞ "strictly invariant under outcome branching" overstates; say "finite large-n limit" | IA1, CG34, DS(list 12), Q3(7.1) | **V** | Corollary 5.14 wording |
| C11 | Error-1 barrier: only the paper's three constructions are excluded from ε<1, not all conceivable schemes | IA1 | **V (unique)** | Remark 5.15 scoped |
| C12 | Figure: U_r must be verified over the plotted range (convex >1.75 there; input pinch enters at 14) | CG35, DS(list 17), Q3(11.10) | **V** | Figure 1 with verified caption |
| C13 | **final.txt only:** annotation at (3,0.6) labelled β=0.25 sits on the β=1 plateau; ymax=1.7 clips the 1.75 curve | IA2 (unique) | **V** | Figure 1 (corrected and upgraded to the strengthened envelope) |

### D. Operational and physical content

| # | Finding | Sources | Ruling | Action |
|---|---|---|---|---|
| D1 | Instrument norm ≠ "optimal bias"; equal-prior formula p_succ=1/2+¼‖·‖ | IA1, CG37, DS(batch2 §4), QW12, Q3(6, 11.6) | **V, unanimous** | Remark 2.3 |
| D2 | 1/n factor: "distribution of the uniform trace budget" is centre-specific; two **distinct** witnesses (orthogonal-output isometry for d_B>1; effect transfer for d_B=1) realize the same numerical budget | IA1, CG12/24, DS(list 10), Q2B7, Q3(6.1) | **V** | Remark 3.7 (two-witness wording) |
| D3 | POVM identification d_B=1: I_k(X)=Tr(E_kX), ΣE_k=I_A | CG23, DS(batch3 §2), QW15, Q3(3.1, 11.4) | **V** | Remark 2.5 |
| D4 | Choi normalization remark Ĵ=J^{unnorm}/d_A, Tr_BĴ=I/d_A iff TP | CG40, DS(batch3 §1), Q3(3.2, 11.4) | **V** | Remark 2.2 |
| D5 | d_A=1 isometry I_k(x)=xτ_k, ‖I−J‖=Σ‖τ_k−σ_k‖₁; exact profile | CG31, DS(list 8), Q3 | **V** | Corollary 6.3 |
| D6 | No-programming theorem needs dim E>1 hypothesis (compact .tex omits it); pure→mixed step needs the rank-one/span argument; quantifiers for the processor subsequence | IA3 (missing hypothesis), CG20/21, DS(list 2,3), Q2B6, Q3(1.1, 1.2, 8.3, 8.4) | **V** | Appendix A rewritten |
| D7 | No-programming is motivation, not a premise of the geometry theorems; scope remark | CG42, DS, Q3(1.3, 8.1, 8.2) | **V** | Appendix A kept (shortened) with scope remark; Introduction states the separation |
| D8 | Channel-case n=1: delete "in agreement with the main article" (phantom reference; normalization unmatched) | IA2, CG47, DS(list 14) | **V** | §6.1 standalone statement |

### E. Consistency, notation, compilation

| # | Finding | Sources | Ruling | Action |
|---|---|---|---|---|
| E1 | Corrupted orthogonal-join proof (5× repeated definition, mangled index) | IA1, CG5, DS(batch2 §1), QW5, Q2A4, Q2B1, Q3(5, 5.9, 10.5) | **V, unanimous** | Proposition 4.7 clean proof |
| E2 | **New (this pass):** qwen3 Batch 10's own corrected join proof defines ν_i but sums h_i(u_i) — variable mismatch to fix when adopting | (Q3 internal) | **V** | Synthesis uses u_i throughout |
| E3 | Duplicated "Define u_i…" sentence (final.txt) | IA2 (unique) | **V** | fixed by E1 |
| E4 | "minus surjectivity" table relic | IA2 (unique), corroborated by AUDIT_RESPONSE P1-4 | **V** | Table 1 "via surjectivity" |
| E5 | Notation collisions (r, k, s, R, S): rename rank r_R, input blocks k_in, output blocks ℓ_out | CG48, DS(list 15), Q3(11.9) | **V** | Remark 2.8 + renames |
| E6 | Double `\appendix` | CG49, DS(list 16), Q3(5.10, 6.1) | **V** | Single appendix A |
| E7 | Unused packages (dsfont, bm, multirow) | CG50, DS(list 15), Q3(6.2) | **V** | Clean preamble |
| E8 | **Compact `.tex` only:** undefined macros (\Lin,\Herm,\Sstate,\rank), no bibliography, statement-only lemmas, editorial note inside the dimension proof ("Not block-positive but…"), "No filler lines" in abstract, corrupted monotonicity sentence | IA3 (unique) | **V** | All fixed in the synthesis |
| E9 | Undefined β^{⋆,(n)} / β^{dir}; envelope never integrated into the bracket | IA1, CG4/26, DS4/6, QW7, Q2A4, Q3(3, 4, 5.5, 10.4) | **V, unanimous** | Single Definition 4.11 of β^best (no stray symbols) |
| E10 | Observable-join needs pure σ and N_join≥2 edge cases | IA1, CG4, QW6, Q3(4, Batch 4) | **V** | Theorem 4.6 uses σ=|b₀⟩⟨b₀|; Definition 4.10 handles invalid cases |
| E11 | Envelope definition must come after the constructions; d_A=1 gives L=D−1 and empty middle range | DS6, QW6, Q3(10) | **V** | Ordering of §4 fixed |
| E12 | Compact `.tex` figure: schematic axis is not the stated geometry; U_r described in caption but not drawn | IA3 (unique) | **V** | Figure 1 (real pgfplots coordinates, U_r drawn) |

---

## 2. The three real disagreements, resolved on merit

**2.1 The 1/d_A bound: delete (CG), conjecture (DS), or theorem (QW-family)?**
CG is right that the *naive* construction fails (X₊ lives on A₀⊗B⊗C_n and lacks the
instrument marginal). CG's remedy (delete) and DS's remedy (conjecture) are the
**weaker** resolutions. The correct construction mixes the Jordan parts with a
correction state ν=(I_{A₀}/d_A−μ/d_A)/(1−1/d_A)=(I−μ)/(d_A−1)≥0 (since μ is a state,
μ≤I), giving instruments J^±=λP+(1−λ)ν⊗τ₀ with marginal I/d_A and
‖J⁺−J⁻‖₁=2/d_A. I verified all four needed checks independently (my IA1 P1-3
"recoverable"); the QW-family supplies the complete proof. **Ruling: theorem, adopted**
(Theorem 4.5). This is the single most important upgrade in the synthesis.

**2.2 Envelope middle value: ρ_n (DS) vs γ=max{ρ_n,1/d_A} (QW-family, IA1).**
Given §2.1, γ is strictly stronger and proved. **Ruling: γ** (Definition 4.11).

**2.3 Observable/join formalization: "needs hypotheses" (CG) vs formal (Q3).**
Q3's clean theorem (E_± effects, eigenvector witness) plus the join lemma with the
N_join cases (2(d_B−1)²+(n−2)d_B² for n≥2; (d_B−2)² for n=1; ignore if N_join<2) is
complete. IA1 adds the requirement that σ be pure (otherwise the support is not
2-dimensional and N_join is wrong). **Ruling: adopt with pure σ.**

**2.4 The no-programming appendix: shorten/remove (CG42, DS) vs keep with tightened
proofs (Q3).** On physical merit the appendix earns its place: it is what separates
*representational* dimension (the paper's main theorem) from *programmable
evaluation*, which is the paper's stated physical motivation. **Ruling: keep as one
appendix with dim E>1, quantifier-clean proofs, and a scope remark.**

**2.5 AUDIT_RESPONSE's internal contradiction.** It rules (P4-23) that the 1/d_A
construction is valid and must be added, yet its own "corrected abstract" (L97–104)
and its corrected β^⋆ definition (L125–127) omit it and its β^{dir} (L128) is never
defined (IA4). **Ruling: the synthesis follows the *ruling*, not the *response's own
summary* — γ is in the abstract and in β^best.**

---

## 3. Strengthening log — weak suggestions completed

1. **CG2 "delete or prove"** → proved (Theorem 4.5, ν-mixing construction).
2. **DS2 conjecture c=1/d_A** → resolved affirmatively by the same theorem.
3. **DS4 β^⋆ with middle ρ_n** → upgraded to γ=max{ρ_n,1/d_A}.
4. **CG26 "Option A: delete the observable sphere"** → Option B fully formalized
   (Theorem 4.6 + Definition 4.10/4.11).
5. **Q3 Batch 10 join proof ν_i/u_i mismatch** → corrected (use u_i).
6. **CG7/8 decoder caveat ("the proof does not establish the continuous-decoder
   case")** → upgraded to Theorem 5.6: at r≥D the decoder *can* be continuous via
   Π_C (single-valued 1-Lipschitz projection onto a compact convex set).
7. **CG25 collapse proof "the reader must reconstruct this"** → explicit radial-map
   argument at ρ_n=1 (Theorem 5.12).
8. **CG10 spectral-lemma "opaque"** → full proof with max{0,·}, block-diagonal
   reduction, and the Y-argument (Lemma 3.2).
9. **CG35 figure "requires checking input pinching"** → full verification written
   into the caption; figure upgraded to the strengthened envelope (γ=0.5 for (2,2,2)).
10. **My IA1 P2-4 / IA3 (error-1 barrier overclaim)** → scoped to "the three
    constructions of this paper" (Remark 5.15).
11. **My IA1 P3-1 (join needs pure σ)** → stated explicitly (Theorem 4.6).
12. **My IA2 final.txt-only defects** (false ‖Φ⊗id‖≤‖Φ‖; abstract vs degenerate
    remark; figure node; ymax; duplicated sentence; table relic) → all fixed.
13. **My IA3 compact-.tex-only defects** (false inequality chain; missing lemmas;
    undefined macros; no bibliography; editorial sentence; missing dim E>1) → all
    fixed.
14. **New catch this pass (B8):** "trace distance 2(1−1/K)" relabeled as the trace
    norm ‖σ−τ‖₁ (the instrument norm equals it; the theorem's number is correct).

---

## 4. Residual items deliberately left open (stated as such in the paper)

1. Global in-radius (is I_* the optimal in-radius centre?) — open, with conjecture.
2. Exact full-body α_r and δ_r^⋄ for 0<r<D outside the collapse case — certified
   bracket only, width ≥1−γ in the intermediate regime.
3. Whether U_r is optimal — not claimed.
4. The AUDIT_RESPONSE's claim that "all audits agree" on its Priority-1 list — not
   reproducible from repo contents (inventory mismatch, §0); irrelevant to this
   assessment, which adjudicates each finding on its own merit.

---

## 5. The corrected synthesis paper

All accepted findings are implemented in **`CORRECTED_SYNTHESIS_PAPER.tex`** in this
folder: a complete, self-contained, compilable manuscript with
- corrected title and abstract (exact vs certified; degenerate case; γ; bracket;
  zero-error threshold; operational factor 1/4);
- full proofs of: affine dimension; spectral bound (max{0,·}); instrument ball
  (with the trace-nonincreasing completeness note); exact centred in-radius (both
  witnesses); covering radius with explicit group averaging; diameter; replacement
  profile (equatorial Borsuk–Ulam); **full-direction antipodal sphere 2/d_A**;
  observable sphere (pure σ) and observable–replacement join with N_join edge
  cases; strengthened envelope β^best with L_{A,B}^{(n)} and γ; monotonicity of
  α_r, δ_r, U_r; convex-projection (Helly–barycentre with the m≤k+1 bookkeeping);
  pinching (roots-of-unity, conjugation formula); zero-error threshold with
  continuous decoder; exact collapse nd_Bs=2; top-subcritical replacement width;
  gap structure; Π_∞ asymptotics;
- corrected figure and tables (verified U_r, strengthened envelope, (2,2,2) and
  (3,2,2) examples);
- a single appendix (no-programming, dim E>1, quantifier-clean);
- clean notation (r_R, k_in, ℓ_out), full bibliography, no overclaims.

Numbering map (synthesis → ledger): Theorem 3.1 (B2), 3.2 (B3/B4), 3.3 (B14), 3.4
(B5), 3.5 (B13), 3.6 (B6/B7/B8), 3.8 (A7), 3.9 (B9), 4.2 (A1/A8), 4.4 (A4), 4.5
(A2/A3), 4.6/4.7/4.10/4.11 (E9/E10/E11), 5.1–5.6 (C1–C4, C7), 5.11–5.15 (C8–C12),
6.3 (D5), Appendix A (D6/D7), Figure 1 (C12/C13), Table 1 (E4).

---

## 6. Residual sweep — final three points, implemented after the first synthesis

A second pass over every audit point (all 50 chatgpt items, both deepseek batches
plus its "still to be applied" list, qwen's 20 sections, qwen 2b's 7 items,
qwen2a's 6 items, all 11 qwen3 batches, and the four independent audits) found
exactly three items not yet implemented. They are now in the paper:

1. **Radius terminology remark** (chatgpt #36; deepseek list item 10;
   AUDIT_RESPONSE "radius senses"). Implemented as Remark "Terminology for the
   three radius notions" (after Definition of α_r): centred relative in-radius,
   worst-case covering radius, and antipodal profile are explicitly distinguished,
   and unqualified "radius" is avoided. **As-is.**

2. **Decoder-codomain hierarchy** (augmented manuscript Remark "Decoder codomain
   hierarchy"; AUDIT_RESPONSE P2-7). Implemented as Remark "Decoder codomain does
   not weaken the lower bounds" after the width definition: since the triangle
   inequality holds for every point of the ambient affine space, the certified
   lower bounds hold even for unphysical affine-valued decoders, giving the chain
   β^best ≤ δ^c(Inst;𝔄) ≤ δ^c(Inst;Inst) = δ^⋄ ≤ U, with constant-code
   admissibility (I_* ∈ Inst) making the upper bounds physical. **As-is.**

3. **Covering-number "barrier-breaking" parenthetical, corrected** (augmented
   manuscript Error-1 remark; my AUDIT-1 P3-4). The original suggestion that
   "covering-number bounds log N(ε) ≤ r log(1/ε) with ε<1" could break the
   error-one barrier is **mathematically wrong as stated**: an ε-net of a
   D-dimensional convex body needs Θ(D log₂(1/ε)) bits, which exceeds D for every
   ε < r₀/2, so nets are strictly dominated by the affine encoding (error 0 at
   exactly D coordinates). Implemented **in corrected form** in the barrier
   remark: two paragraphs proving why (i) net encodings and (ii) orthogonal
   joins (already absorbed into β^best) cannot break the barrier. **Modified.**

### Deliberately not implemented (with reasons)

- deepseek's retraction of 1/d_A to a conjecture — superseded by the full-direction
  theorem (adjudication §2.1).
- chatgpt's "Option A: delete the observable sphere" — superseded by the formal
  observable/join package (§2.3).
- The tensor-identity orientation point (chatgpt #38, deepseek list 11) — moot:
  the corrected paper never uses ‖Φ⊗id‖; composition submultiplicativity is used
  where it is valid (pinching).
- The "β^dir" symbol (AUDIT_RESPONSE) — dropped in favour of the single γ-based
  envelope.
- qwen3's "optional: shorten the appendix by deleting the unequal-output
  corollary" — the corollary is retained (valid, one paragraph, completes the
  appendix's physical picture).
- chatgpt #22 (attribute the replacement distance in the abstract to the isometry
  lemma) — cosmetic; the attribution is present in the body (Theorem 4.4).

With this sweep, **every audit point is either implemented, adjudicated as
superseded, or explicitly rejected with a documented reason.**

---

## 7. Systematic content-recovery and proof-completeness scan (third pass)

A deep, systematic scan compared the synthesis against **every earlier manuscript version**
(`final.txt`, `FINAL_JOINT_COMPLETE_AUGMENTED.txt`, the four byte-identical `FINAL_*.tex`,
`AUDIT_RESPONSE_AND_CORRECTED_VERSION.tex`), item by item. Results per question:

### Q1 — Content from earlier drafts worth implementing: found and implemented

1. **Scaling-with-n regime analysis** (final.txt §"Scaling with n") — recovered **with
   correction**: the original's middle-regime statement "certified lower ρ_n=O(1/n)"
   is upgraded to the strengthened envelope: γ→1/d_A, a constant. New Corollary
   "Scaling with the number of outcomes" gives the three regimes c<d_B², d_B²<c<d_A²d_B²,
   c>d_A²d_B², including the O(1) bound L_{A,B}^{(n)}=nd_B²+O(1) and the note that the
   certified bracket has asymptotic length at least 1−1/d_A.
2. **Resource interpretation of the two breakpoints** (final.txt) — recovered as-is
   (Remark after Definition of β^best), extended with the observable construction's role.
3. **In-radius versus antipodal profile remark** (augmented .txt) — recovered as-is:
   no contradiction between ρ_n<1 and α_r=1 for r≤nd_B²−2 (different mechanisms).
4. **Tunable mixing parameter λ(Z)=1/(d_A‖μ(Z)‖_∞)** (compact .tex, "Improved λ")
   — recovered **with correction**: implemented as a remark, with the exact condition
   λ≤1/(d_A‖μ‖_∞), the λ=1 endpoint (μ=I/d_A needs no filler), and an explicit
   continuity caveat (why the proof fixes λ=1/d_A).
5. **"If both encoder and decoder must be continuous" caveat** (compact .tex) —
   recovered as-is into the nonconstructive-decoder remark: threshold unchanged via Π_C,
   subcritical U_r become existence statements.
6. **d_A=1 "centred in-radius irrelevant for the antipodal profile"** (final.txt) —
   recovered as-is into the input-independent specialisation.

### Q2 — Accidental content loss / condensation: none remaining

Every remaining paragraph of every earlier version was accounted for: either present
verbatim in the synthesis, present in strengthened form (tracked in §1–§4), or
deliberately removed as false/unproven (chord claim, ‖Φ⊗id‖≤‖Φ‖, "α_r need not be
monotone", unproven 1/d_A corollary, undefined β^⋆/β^dir, schematic figure). The only
condensations were the six items above, now restored. Two deliberately dropped items
are documented with reasons: final.txt's summary Table 2 (regime/guarantee/status) —
its content is fully carried by the theorems and Table 1; and the "flagged-state
picture" prose remark — its content is absorbed in the replacement-isometry lemma
and its proof.

### Q3 — Proof completeness: full proofs throughout, with the literature exception

The synthesis presents **every** proof in full. The only results replaced by citation
are standard textbook material, per the stated rule:
- **Schur's lemma** for U(d)-averaging (used once in the covering theorem) — cited
  to Watrous 2018 rather than re-proved.
- **Composition submultiplicativity of the diamond norm** (used in pinching) — cited
  to Watrous 2018.
- **Borsuk–Ulam** — cited to Matoušek at first proof use; the equatorial-restriction
  reductions are still written out at every use.
- **Helly's theorem** — cited to Barvinok; the Helly–barycentre verification (m≤k+1
  bookkeeping, 2(m−1)/m≤2k/(k+1)) is proved in full.
- **Pure-program no-programming theorem** — cited to Nielsen–Chuang; the pure→mixed
  extension and the compactness corollary are proved in full (the non-standard part).
- The metric-projection properties (single-valued, 1-Lipschitz) used in the zero-error
  theorem are stated self-containedly in one sentence (they are two lines of convex
  analysis and are kept rather than cited for readability).

Two further proof-completeness upgrades applied in this pass:
- Corollary "Metric complementarity" and Corollary "Asymptotic positivity–dimension
  product" now carry explicit (one-line, algebraic) proof environments.
- The balanced-block minimisation of Q_ℓ now includes the termination argument
  (finite set of partitions + strictly decreasing exchange ⇒ balanced fixed point).

### Q3-adjacent: notation collisions completed

The remaining collisions listed in the audits were eliminated: subspaces are now
denoted W (killing s vs S), the reference system in the covering arguments is now E
(killing R-radius vs R-reference), joining the earlier r_R/k_in/ℓ_out renames.
The notation remark records the full convention.
