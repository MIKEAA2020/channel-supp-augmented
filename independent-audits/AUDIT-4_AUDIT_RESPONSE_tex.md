# Independent Audit 4 — `supp/AUDIT_RESPONSE_AND_CORRECTED_VERSION.tex`

**File:** supp/AUDIT_RESPONSE_AND_CORRECTED_VERSION.tex (205 lines)
**Role:** meta-document — a joint evaluation of (alleged) prior audits plus corrected
statements for the manuscript. Audited here as a *version of record*, on its own
internal consistency.
**Date:** 2026-08-28 · **Independence:** `post gpt audit corrections/` was not consulted,
so all claims this document makes *about specific audit files* are treated here as
unverifiable metadata, not as content to be cross-checked.

## Verdict

Useful as a fix-list — most of its mathematical corrections are right, and I
independently confirm its main recomputations (node (9.5,0.45); r_out=12; r_in=14;
ymax=2.0; U_0=R_n with 2−2/(D_n+1)≥R_n; exact gap R_n−1=1−ρ_n at r=0; the 1/d_A
construction being valid; the "α_r need not be monotone" claim being false; the
‖Φ⊗id‖ equality). But the document has **its own internal inconsistencies**:
its corrected statements do not incorporate its own Priority-4 rulings, one symbol it
endorses as standard (`β^dir`) is never defined, and its inventory of prior audits
does not match the files actually present in the repository.

---

## Priority 1 — internal inconsistencies of the corrected statements

### P1-1 (L97–104, "Corrected abstract") — omits the document's own Priority-4 strengthening
P4 item 23 (L53–54) rules that the 1/d_A direction-space bound is valid and
"meets/exceeds ambition" and must be added. Yet the corrected abstract (L101) still
states only
> "α_r ≥ 2/(nd_B·s) for intermediate nd_B²−1≤r<D_n",

with no mention of α_r≥1/d_A. The corrected abstract is therefore not the abstract
of the document's own corrected version. Either the abstract must carry the
γ=max{ρ_n,1/d_A} form, or P4-23 must be withdrawn.

### P1-2 (L125–127, corrected β^{⋆}) — defines β^⋆ with ρ_n, contradicting P4-23 again
The corrected definition sets β^{⋆,(n)}=1 for r≤L, **ρ_n** for L<r<D_n, 0 for r≥D_n.
Given P4-23 (α_r≥1/d_A in the intermediate regime), the intermediate value should be
γ=max{ρ_n,1/d_A}; the stated β^⋆ ignores the very improvement this document
endorses 30 lines earlier.

### P1-3 (L128, "β^{best}=max{β,β^{⋆},β^{dir}}") — β^{dir} is never defined
`β^{dir}` appears exactly once in the entire document, inside the definition of
β^{best}. No formula, no reference, no indication of which direction-space bound it
encodes (presumably the 1/d_A one, i.e. β^{dir}=1/d_A in the intermediate regime —
but that is exactly what P1-1/P1-2 show is not consistently handled). A symbol used
in a definition must be defined.

### P1-4 (L99–100, "Corrected figure") — the corrected node coordinates contradict the plateau geometry it states
The corrected figure text says the β annotation should sit at **(9.5, 0.45)** while
also stating "β=2/(nd_B·s)=0.25 on plateau 7≤r≤27" — consistent (9.5 is inside the
plateau; 0.45 is just above the 0.25 line). Fine. But it also says the red U_r is
"**1.75 for 0≤r<12, 1 for 12≤r≤13**" and that the caption should state the minimum
is "checked over the plotted range". Independently verified: convex(1)=54/28≈1.928
and convex(11)=34/18≈1.889 both exceed 1.75, so min=1.75 on 0≤r<12 — **correct**.
However the stated plateau "7≤r≤27" contradicts the plotted range 0≤r≤13 the same
sentence describes; the plateau description belongs to the full envelope, not to the
truncated figure. Wording-level inconsistency (a reader cannot tell which r-range the
figure actually shows).

### P1-5 (L51, "Corrected monotonicity" proposition) — proof-free reversal of a theorem-level claim
The corrected proposition reverses "need not be monotone" to "non-increasing" — this
reversal is **mathematically right** (independently verified: equatorial restriction).
But the document presents it as a *corrected proposition* with a one-line justification
("by restricting h:S^{r+1}→K to equatorial S^r⊂S^{r+1}"), i.e. the document's own
flagship-level correction is stated without proof, in a document whose P4-22 says the
original claim was false. Acceptable for a response letter, but the corrected
*manuscript* must carry the full argument.

---

## Priority 2 — unverifiable or mismatched meta-claims

### P2-1 (L29–31) — inventory of prior audits does not match the repository
The document says it evaluated "chatgpt suggested.txt" plus "9 other audits
(1.txt, 2.txt, assistant a/b, deepseek, deepseek bulk gap, gpt aisure, grok1, qwen,
qwen bulk gap)". The repository's `post gpt audit corrections/` folder contains only:
`chatgpt suggested.txt`, `deepseek.txt`, `qwen 2b.txt`, `qwen.txt`, `qwen2a.txt`,
`qwen3.txt`. Six of the ten cited audit names correspond to files that **do not exist
in the repo**. Either the inventory lists private/uncommitted files, or the names are
wrong. This is a provenance inconsistency for a document whose entire authority rests
on that joint evaluation.

### P2-2 (L29) — "contains 50 points" is unverifiable from the repo
Consistent with P2-1: the claim that `chatgpt suggested.txt` contains 50 points cannot
be checked without the referenced content being the same as the repo file. (I did not
open the audits folder per instructions, so this is flagged as provenance, not as a
substantive finding.)

### P2-3 (L54, P4-23) — "The construction in deepseek bulk gap.txt IS valid"
Same provenance problem: the construction is validated by reference to a file that is
not in the repository. Independently, the *construction itself* (as restated at
L121–123) is correct — I verified all four needed checks (M_X≥0; M_X≤I because
Σ_k Tr(X₊)_k=1; filler PSD since λM_X≤I/d_A; Σ_k Tr_B J_k=I_{A₀}/d_A) — but the
document's restatement omits the M_X≤I justification, which is the one non-trivial
step. A corrected manuscript must include it (see AUDIT-1 P1-3).

### P2-4 (L38–42, P1 items) — "all audits agree" is not reproducible
The Priority-1 list asserts consensus ("VALID, all audits agree", etc.) across the
ten alleged audit files. Given P2-1, this consensus claim cannot be reproduced from
the repository state. Methodological note for provenance, not a math error.

---

## Priority 3 — editorial

- **L74 (P4-36):** "all VALID editorial, fix" — lumps ~14 distinct issues (unused
  package, notation collisions, duplicate appendix, phantom references) into one
  item; a corrected manuscript needs them fixed individually and verifiably.
- **L83–84 (Invalid points):** the rebuttal of "bulk gap attempt with 1/d_A is
  impossible" is correct in substance (the construction works), but the rebuttal of
  "not publishable as exact geometry" is argued from the *post-fix* state; it would
  be stronger to concede that the pre-fix manuscript overclaimed ("exact metric
  parameters" — see P4-24) and that the claim is now scoped correctly.
- **L110–113 (Helly correction):** "‖c−x_j‖≤2(m−1)/m≤2k/(k+1)=R" — independently
  verified correct (m≤k+1). Good.
- **L130 (Operational):** "p_succ=1/2+‖I−J‖/4, bias 1/4‖·‖ or 1/2‖·‖ depending
  convention" — the 1/4 form is the right one (matches the compact .tex); the "or
  1/2" hedge reintroduces exactly the ambiguity that AUDIT-1 P1-5 flags in the
  augmented `.txt`. Pick one convention and state it once.
- **L196–197:** "$\backslash$ appendix removed" and "second $\backslash$ appendix
  duplicate" — the two appendix-fix notes overlap; fine, but the corrected manuscript
  must actually remove it (the compact .tex still has one appendix).
- **Notation fixes listed (L197–198):** latent q, rank r_R, input blocks k_in, output
  ℓ_out — the compact .tex adopts these; the long `.txt` versions do not (they still
  use r for both latent dimension and rank in places). Fix is only half-applied across
  the versions in `supp/`.

## Verified-correct highlights (for balance)

- The document's core recomputations are right: node (9.5,0.45); Q_2(2)=2, r_out=12,
  r_in=14; ymax=2.0; U_0=R_n (convex bound 2−2/(D_n+1)≥R_n for all admissible
  (d_A,d_B,n) — independently checked); exact certified gap R_n−1=1−ρ_n at r=0;
  ρ=+∞/R=0 convention for n=d_B=1; the false "‖Φ⊗id‖≤‖Φ‖" ruling (equality holds);
  the false "α_r need not be monotone" ruling (non-increasing holds); the validity
  of the 1/d_A construction.
- Its corrected collapse theorem, diameter proposition, and metric-complementarity
  restriction ("numerical identity, not chord decomposition") are all right, and the
  chord restriction matches AUDIT-1 P1-1.
- The P2-11 correction (gap statement false at r=0; U_0=R_n; bracket width is the
  certified width, not a proven gap) is precise and correct.
