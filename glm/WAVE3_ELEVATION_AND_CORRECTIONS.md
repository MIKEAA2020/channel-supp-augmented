# Wave 3 — Corrections and Mathematical Elevations: the v3 Manuscripts

**Date:** 2026-09-08. **Author:** GLM (this assistant).
**Mandate (user, verbatim):** *"for overclaims, prioritize rigorously elevating math to close gaps and meet or exceed them. do not regress or soften unless truly irrepairable/unreachable. demote to conjecture if truly plausible but proof remains out of reach. apply all corrections as new versions, commit and push."*

**Inputs:** the consolidated defect list of `WAVE2_AUDIT_VERIFICATION_REPORT.md` §8 (union of wave 1 + the 46 verified wave-2 findings) plus the wave-1 report's A/B items.
**Deliverables:** `manuscript uploads v3/instruments-paper-revised3.{txt,pdf}` and `manuscript uploads v3/main-article-revised3.{txt,pdf}` — corrected new versions of the two manuscripts. The originals in `manuscript uploads/` are untouched.

---

## 0. Executive summary

Every overclaim was treated by elevation first. Four claims were **met or exceeded by new mathematics**; one was **demoted to an explicit conjecture** (with partial results proved around it); only one sentence was genuinely regressed — an unproved proof-internal step replaced by the proved step that already carried the theorem (I8). All remaining verified findings (wording, scoping, citations, figures, notation, spelling, typesetting) were applied. Both v3 sources compile with Tectonic (exit 0, no errors, no undefined references), every cross-reference resolves, and all remaining overfull boxes are below 3 pt.

| Overclaim | Treatment | Result |
|---|---|---|
| Instruments Table 1 caption "envelopes coincide at r=0" (I1) | **Elevated**: lower envelope upgraded at r=0 to the exact constant-code width R_n | Caption now **true as written**; β₀=R_n=U₀ exact |
| Instruments conclusion "d_A=1 subcritical widths exact" (I2) | **Repaired + demoted to conjecture**: new Conjecture `con:flat-d1` + partial-evidence remark + open problem (v) | Precise claim + explicit conjecture |
| Channel join at d_B=3 vacuity (C1) + cross-paper pointer (C2) | **Elevated** both sides: channel proof handles d_B=3 via the observable sphere; instruments `N_join ≥ 1` extension makes the pointer exact | Stronger statements kept: d_B≥3 on the channel, N_join≥1 on the instruments side |
| Abstract "matching upper bounds" (A6 + instruments twin) | **Repaired with the r=0 elevation**: "meet the envelope exactly at zero latent dimension, in the collapse case, and from the affine dimension on" | Truthful and stronger |
| Finite-sample bound can exceed the diameter (C19) | **Elevated**: cap folded into the statement, `min{2, d_A√(d_A d_B)/(η√N)}` | Non-vacuous for every N |
| thm:global-inradius proof gaps (C6, C16) | **Elevated**: 1-Lipschitz continuity of the in-radius proved inline, boundary-centre case handled, Haar barycentre computed inline | Proof complete, self-contained |
| Lemma 3.2 load-bearing external citation (A5) | **Elevated**: self-contained Jordan-decomposition proof added; citation retained as independent derivation | No external dependency |
| thm:no-programming "every pure vector" (I8) | **Repaired**: replaced by the proved eigenvector statement (which carries the orthogonality step); overreach removed | Only genuine softening, and only of an unproved proof sentence |

New mathematical content added to the manuscripts: the upgraded envelope value β₀=R_n with its full proof chain (8 theorem/proof sites per paper), the N_join≥1 join extension, the d_B=3 reduction, the Lipschitz/Jensen completion, the self-contained Choi-diamond upper bound, the error-one-floor corollary (A10-iv), the continuous-decoder-at-threshold clause (A10-v), the flat-widths conjecture with partial results, and the RP³ sharpness note (C11).

## 1. Elevations in detail

### 1.1 The r=0 envelope coincidence (I1 / E1–E7)

The caption claimed the envelopes "coincide at r=0"; as written β₀=1< U₀=R_n outside the collapse case. Rather than soften the caption, the **certified lower envelope itself was upgraded**: `def:beta-best` (instruments) and `def:channel-envelope` (channel) now set β₀ := R_n = 2(1−1/(nd_Bs)), resp. 2−ρ_dep, the **exact constant-code width** already proved by `cor:constant-code` / `thm:depolarizing-chebyshev`+`thm:exact-chebyshev-radius`. The caption's claim is therefore now true, and the lower envelope is strictly stronger than before (R_n ≥ 1).

The full proof chain was updated so the elevation is airtight: the non-increasing proof of `prop:monotonicity` (R_n ≥ 1), the r=0 cases of `cor:bracket`, `cor:intrinsic` (via the centre-optimality clause of `thm:covering`), `thm:hierarchy` (channel), the rewritten `prop:gap` item 1, Table 1 row + caption, `rem:exact-vs-certified` item (vii), both abstracts, both worked-example texts, both envelope figures (new marked point β₀=U₀ at r=0), and `cor:scaling` (r_n=0 now carries the exact value R_n→2).

### 1.2 The d_B=3 join (C1/C2/E8)

The channel proposition keeps its **stronger hypothesis d_B ≥ 3**: the proof now splits off d_B=3 explicitly — Herm₀(W₂^⊥) is trivial, the replacement sphere S⁻¹ is empty, and the displayed range d_A²−2 is realised by the observable sphere alone. For d_B ≥ 4 the join proof runs as before. On the instruments side, `cor:join-dimension` was extended from N_join ≥ 2 to **N_join ≥ 1**: at the degenerate value N_join=1 (only n=1, d_B=3) the join reduces to the observable sphere and the displayed formula reproduces d_A²−2, so the statement holds with the strictly wider coverage. `def:one-sphere` and the threshold table follow ((2,3,1) row: L_join = 2, degenerate). The channel paper's cross-pointer "this is the n=1 case of the instrument-level join" is now exact for every d_B ≥ 3, closing C2. Both join proofs also gained the missing λ∈{0,1} endpoint sentence (I7 and its channel twin).

### 1.3 The d_A=1 flat-widths conjecture (I2)

The conclusion's overclaim was replaced by the precise statement (profile exact; top-subcritical width exact; one-sphere envelope values exact) together with a new numbered **Conjecture** (`con:flat-d1`): for d_A=1 and nd_B>2, δ_r = 1 throughout 1 ≤ r ≤ nd_B²−2. The accompanying remark records the proved partial results (lower bound from the exact profile; equality at the top-subcritical index; equality from the two-sector pinching threshold nQ₂(d_B)−1 upward) and honestly notes the classical special case (simplices, d_B=1, n≥5, small r) is already open — the bracket [1, min{2(1−1/n), 2(n−2)/(n−1)}] at r=1. The conjecture is cross-referenced from the open-problem list (new item (v)) and from the channel paper's open problem 1. This is the mandated "demote to conjecture" treatment: the claim is plausible (every proved value equals the floor), the proof is out of reach (it contains open classical questions), and the conjecture is stated with its evidence.

### 1.4 Proof-completeness elevations

* **C6/C16 (channel, thm:global-inradius):** the halfspace characterisation now covers boundary centres (supporting halfspace, both sides vanish); the in-radius's **1-Lipschitz continuity is proved inline** (ball translation argument), which licenses Jensen for the Haar integral via finite convex combinations and continuity; the Schur/permutation barycentre computation is inlined instead of deferred to a later proof.
* **A5 (channel, Lemma 3.2):** self-contained proof of ‖Δ‖_◇ ≤ ‖Tr_B|J_Δ|‖_∞ via the Jordan decomposition J=J₊−J₋, CP maps Δ±, trace-through-the-adjoint, and |J|=J₊+J₋; the Nechita et al. citation is retained as an independent derivation, no longer load-bearing.
* **A10(iv):** new `cor:upper-floor` (channel) mirroring the instruments' Proposition: every admissible upper-envelope term is ≥ 1 below the affine dimension.
* **A10(v):** `prop:euclidean-threshold` now states the **continuous decoder** at and above the affine dimension (nearest-point projection), matching the instruments' threshold theorem.
* **I7:** prop:join-inst λ=1 endpoint completed by an explicit three-case split.
* **I13/I14:** `lem:inradius-concave` (instruments) gains the hypothesis nd_B>1 (degenerate singleton excluded, cross-referenced) and an admissible-value/attainment-free concavity argument.
* **I8:** the no-programming proof now states what is actually proved — every positive-weight eigenvector programs exactly, and these span the support (which is all the orthogonality step needs).
* **C3:** profile item 5 now carries the same-topology hypothesis **with a proof that it is automatic for norm metrics**, plus an explicit counterexample note (the ε-close discrete perturbation) showing the hypothesis cannot be dropped.
* **C11:** footnote added: at d=2 the unitary-promise bound sharpens to r ≥ 5 (PU(2)≅RP³, embedding dimension 5).
* **C19:** the diameter cap min{2, ·} moved from the proof into the theorem statement.

## 2. All other verified corrections applied

**Instruments paper (instruments-paper-revised3):** I3 (early ρ_n/R_n definition with forward references), I4 (diameter proof wording), I5 (A₀-marginal), I6 (pure σ±), I9 (barrier remark scoped), I10 (d_A=1 replacement body = whole body), I11 (pinching display type-consistent), I12 (vectorisation conjugation note), I15/I16/I23 (notation remark rewritten: W on flag-output side, E as A₀-copy and appendix programming input, conjugation-flip note), I17 (nd_B ≥ s justified), I18 (sec:lower syntax + figure (a) extended to r=14 with the input-pinch step), I19 (Table 2 d_A≥2 proviso), I20 (collapse figure callout on case (i)), I21 (covering proof "its own output"), I22 (positive → positive semidefinite, 3 sites), I24 (gap phrasing rewritten with the elevation), I25 (degenerate-remark mis-substitution guard), I27 (transfer enumeration), B1 (Kolmogorov phrasing + "matching upper bounds" wording), B2 (Kubicki author initial A.M. → M.), B3 (t's typography), B4 (tunable-λ degeneracy explained), B5 (balanced-partition argument promoted to `lem:balanced`), B6 (the 11.6 pt overfull reflowed; sub-3 pt boxes remain), A6-twin (abstract), conjecture environment added.

**Channel paper (main-article-revised3):** A1/C7 (Figure 2: flag-space node redrawn in channel-only terms, R→R_J, s=2→c=2 with corollary reference, ρᵢ removed from the caption, Jordan construction re-attributed to `thm:full-state-antipodal`, "construction above" → figure+appendix pointer, balanced note references the pinching theorem), A2/A3-partition (block-size cap s→c, full-block count q→m, join dimension R→R_J throughout the partition appendix and figure), A3 (diameter symbol on the `\diam` macro in `prop:convex-projection-upper`; simplex Δ→Σ), A4/A10(vi) (British spelling unified, 64 replacements incl. centred/normalised/analysed/barycentre; TikZ keys untouched), A7 (duplicated decoder sentence), A8 (Clifford theorem split into `prop:clifford-replacement` + `thm:clifford-unitary`, parameters bound once), A9 (partition-appendix retention rationale), A10(i) (Acknowledgements added), A10(ii) (hidelinks, matching the companion), A11 (all four overfull sources reflowed; 14.4/7.5/3.7 pt boxes eliminated), A12 (bibliography reordered to first-citation order — Nielsen–Chuang first; `graphicx` loaded explicitly; two natural cross-references added for orphaned labels), C8 (Borsuk–Ulam sentence grammar), C9 (two scales wording), C10 (‖·‖_E removed; 𝒱_V→𝒞_V conjugation superoperator; σ_{u₂}→τ_{u₂} in the join proof), C13 (Clifford forward references to the appendix + main-text formula U_u=(I_C+iH_u)/√2⊕I_{C⊥}), C17 (extremality justified inline), C18 (IC-for-the-affine-hull wording), C20 (comb caption "(stated below)"), C21 (manifold wording), C22 (duplicate decoder sentence = A7), C23 (Tr_{H_out} clarification), C24 (appendix vectorisation aligned with the main-text unbarred convention, making the constraint identity literally correct), X1 (companion-pointer reworded: no-programming is appendix material), B5-channel (balanced-partition lemma), C12-residual, and the two abstract/conclusion/figure/example updates for the β₀ elevation.

**Explicitly not changed** (with reasons): A10(iii) definition-numbering style (cosmetic; the papers cross-reference by name, not number); B2's remaining bibliographic records and the channel paper's citation records (require publisher verification, not editable assertions — flagged in wave 1 §8); the underfull table columns and the two slightly-wide figures (cosmetic, per wave-1 A11 note); max2's "ode"/"u_r" and `\rhodep` claims (false positives, nothing to fix); the radius-notions figure proportions (I26, rejected on the merits).

## 3. Verification

* **Tectonic:** both sources compile end-to-end, exit 0, no errors; final-pass logs contain **zero** undefined references or citations; no multiply-defined labels.
* **Static audit** (`scripts/audit_v3.py`): instruments — 79 labels (no duplicates), 180 refs (all resolve), 16/16 bibliography entries cited; channel — 99 labels, 176 refs, 23/23 entries cited; environments balanced; braces balanced; math-$ parity even in both.
* **Overfull boxes:** instruments 3 (0.19, 2.99, 0.14 pt), channel 1 (0.62 pt) — all sub-3 pt, invisible; the wave-1 inventory of 11.6/14.4/7.5 pt boxes is cleared.
* **Figures:** the envelope figures render the new marked points (β₀=U₀=R_n at r=0 in both papers; instruments panel (a) extended to r=14 with the input-pinch step), confirmed in the compiled PDF text layer.
* Page counts: instruments 35 pages, channel 46 pages.

## 4. Reproducibility

All edits are scripted and idempotent-per-source: `scripts/edit_instruments_v3.py` (53 tagged edits), `scripts/edit_channel_v3.py` (85 tagged edits + spelling pass + bibliography reorder), `scripts/fix_overfull_v3.py` (4 reflow fixes), `scripts/audit_v3.py` (integrity audit), run against fresh copies of the revised2 sources.

## 5. Security note

The GitHub personal access token used for repository access was shared in plaintext chat. It should be revoked and rotated now that the work is pushed. (Same note as wave 3's report, §10.)
