# Independent Audits of `supp/` Manuscript Versions

**Date:** 2026-08-28
**Auditor:** independent line-level review (Agent Mode)
**Repo:** `MIKEAA2020/channel-supp-augmented`

## Scope and independence statement

The `supp/` folder contains seven files. Before auditing, I confirmed:

- The four `FINAL_*.tex` files (`FINAL_FULL_INSTRUMENT_GEOMETRY.tex`,
  `FINAL_JOINT_COMPLETE_AUGMENTED.tex`, `FINAL_JOINT_EVALUATED_STRENGTHENED.tex`,
  `FINAL_RIGOROUS_ELEVATED_COMPLETE.tex`) are **byte-identical**
  (md5 `fc632af4cb617a2e1849fe0df49eb8ac`). One audit covers all four.
- The two long `.txt` files (`final.txt`, 1456 lines, and
  `FINAL_JOINT_COMPLETE_AUGMENTED.txt`, 1501 lines) are near-duplicates:
  the augmented file is `final.txt` plus later additions. They are audited
  separately because their flaws differ.
- `AUDIT_RESPONSE_AND_CORRECTED_VERSION.tex` is itself a meta-document
  (an audit-response + corrected statements) and is audited as a version
  of record.

**Independence:** per instructions, the folder `post gpt audit corrections/`
was **not opened or read**. Every finding below was derived only from the
manuscript texts themselves, plus independent recomputation of the stated
formulas (all numeric checks listed per audit). Any claim that happens to
coincide with an existing audit is coincidence.

## Files in this folder

| File | Manuscript audited | Verdict summary |
|---|---|---|
| `AUDIT-1_FINAL_JOINT_COMPLETE_AUGMENTED_txt.md` | `supp/FINAL_JOINT_COMPLETE_AUGMENTED.txt` (flagship, 1501 lines) | core math mostly sound; 2 unproven claims, 2 false claims, 1 corrupted proof block, several internal inconsistencies |
| `AUDIT-2_final_txt.md` | `supp/final.txt` (1456 lines) | one outright false lemma claim; figure/table defects; degenerate-case self-inconsistency |
| `AUDIT-3_FINAL_x4_tex.md` | the four byte-identical `FINAL_*.tex` (271 lines) | not publishable as-is: unsound proof step in the flagship in-radius theorem, missing lemmas, undefined macros, no bibliography |
| `AUDIT-4_AUDIT_RESPONSE_tex.md` | `supp/AUDIT_RESPONSE_AND_CORRECTED_VERSION.tex` (205 lines) | useful summary; its own internal inconsistencies and unverifiable meta-claims |

## Independent numeric verification (all files)

The following manuscript claims were recomputed from scratch and **check out**:

- (d_A,d_B,n)=(2,2,2): D=28, ρ=2/(nd_B·s)=0.25, R=2(1−1/(nd_B·s))=1.75.
- Convex-projection bound on plotted range 0≤r≤13: min at r=11 is 34/18≈1.889>1.75;
  at r=0 it is 56/29≈1.931>1.75. Manuscript's 54/28 (r=1) and 34/18 (r=11) are correct.
- Q_2(2)=2; r_out=4·(2·2−1)=12; r_in=2·(2·4−1)=14 (no input-pinch before 14).
- Π_∞ = lim D_n·ρ_n = 2d_A²d_B/min{d_A,d_B} = 8 for (2,2,2) = 2d_A·max{d_A,d_B}.
- Exact gap at r=0: U_0=R_n=1.75; R_n−1=0.75=1−ρ_n (convex bound 1.931>1.75, so U_0=R_n).
- Pinching norm 2(1−1/ℓ): ℓ=2→1; collapse cases nd_B·s=2: (d_B=1,n=2)→D=d_A²; (d_A=1,n=1,d_B=2)→D=3.
- Spectral bound: s/(2d_A)·(2/(nd_B·s)) = 1/(nd_A·d_B) — exactly the positivity margin, so
  the ball theorem is tight; the degenerate case n=d_B=1 gives D=0 as claimed.
- Jordan-sphere / replacement profile arithmetic: sphere S^{nd_B²−2} in a body of affine
  dimension nd_B²−1; Borsuk–Ulam gives α_r=0 for r≥nd_B²−1. Consistent.
- Helly–barycentre argument: R=2k/(k+1) with 2(m−1)/m≤R for m≤k+1. Sound.
- Observable-sphere join arithmetic: (d_A²−2)+(N−2)+1 = d_A²+N−3 with
  N=2(d_B−1)²+(n−2)d_B² (pure-σ reduction understood). Consistent, but see AUDIT-1 P3.

## What was found (headlines)

1. **AUGMENTED txt, L554**: the "metric complementarity" corollary claims the uniform
   instrument divides an "extremal chord" in ratio ρ_n:(2−ρ_n). The two witnesses
   (ball-boundary point and covering witness) are constructed in different proofs with
   no shared geometry; their mutual distance is never computed. The numerical identity
   ρ+R=2 is fine; the chord statement is unproven.
2. **AUGMENTED txt, L1005**: "α_r need not be monotone in general" is **false** — the
   equatorial-restriction argument used elsewhere in the same file proves α_r is
   non-increasing for every metric space.
3. **AUGMENTED txt, L706**: the "general direction-space lower bound 1/d_A" corollary is
   asserted with no construction in the file: M_X is never defined, 0≤M_X≤I is never
   shown, the filler state is never verified PSD, TP-ness is never checked. The claim is
   *recoverable* (the construction works, with M_X≤I because Σ_k Tr(X₊)_k=1), but as
   written the corollary is unproven. It also creates an internal inconsistency with
   L1087, which still uses the weaker β_r=ρ_n.
4. **AUGMENTED txt, L1329–1331**: the orthogonal-join proof is corrupted — the
   definition of λ_i,u_i is repeated five times mid-sentence and the sum index is
   mangled ("Defineneq0"). The LaTeX will not compile.
5. **AUGMENTED txt, L185**: "the norm equals the optimal bias" is off by a factor 4:
   p_succ = 1/2 + ‖·‖/4, so bias = ‖·‖/4, not ‖·‖. (The compact .tex states the
   factor-1/4 version correctly.)
6. **final.txt, L544**: "‖Φ⊗id_Cn‖_⋄ ≤ ‖Φ‖_⋄ because id_Cn is CPTP and the diamond
   norm is submultiplicative under tensoring" is **false**: the diamond norm is
   *multiplicative* under tensor products, so equality holds; submultiplicativity is a
   property of composition. (Also, the inequality direction would be useless for the
   isometry claim it is meant to support.)
7. **final.txt, figure**: the node at (3,0.6) is labelled "β=0.25" but sits on the
   β=1 plateau (0≤r≤6) — a visual contradiction with the caption's own numbers; and
   ymax=1.7 clips the red U-curve drawn at 1.75.
8. **compact .tex, L92**: the centred in-radius proof chain
   ‖Z_k‖_∞ ≤ ‖Tr_B|Z_k|‖_∞ ≤ s‖Z_k‖_1/d_A is **false in both steps** for general Z_k
   (counterexample: maximally entangled |MES⟩⟨MES| with d_A=4,d_B=2 gives
   1 ≤ 1/4 ≤ 1/2 — both inequalities fail). The correct proof needs the spectral-bound
   lemma (which the file states but never proves). The full .txt versions prove the
   same theorem correctly.
9. **compact .tex**: undefined macros (`\Lin`, `\Herm`, `\Sstate`, `\rank`), no
   bibliography, statement-only "lemmas", a self-referential editorial sentence inside
   the dimension proof (L83), and a corrupted monotonicity sentence (L55). Will not
   compile as-is.
10. **AUDIT_RESPONSE .tex**: internally inconsistent in places (its own P4 item 23
    endorses a 1/d_A strengthening that its "corrected abstract" omits; "β^dir" is
    never defined; audit files it cites are absent from the repo).

Full details, severity levels, and per-file line references are in the four audit files.
