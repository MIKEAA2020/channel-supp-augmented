# Wave-2 Audits: Sorted Inventory and Joint Verification Report

**Reviewer:** GLM (wave 3). **Date:** 2026-09-08.
**Inputs:** the four files in `wave 2 audits/` (`audit 1.txt`, `audit 2.txt`, `max1.txt`, `max2.txt`), containing **sixteen separate audits** written by nine distinct model attributions (gpt terra, qwen, grok, gemini, claude, hy4, an unnamed "ai model", and two "max" audits).
**Targets audited by them:** the two manuscripts in `manuscript uploads/` — `main-article-revised2.txt` (the *channel paper*, 3,646 lines) and `instruments-paper-revised2.txt` (the *instruments paper*, 1,615 lines) — the same pair reviewed in my wave-1 report (`wave 1 report/Manuscript_Review_Report_channel-supp-augmented.docx`).
**Mandate:** sort the audits out; evaluate and verify all of them jointly with my own wave-1 audit; report only, no modification of the manuscripts.

---

## 0. Executive summary

1. **Sorting.** The four files decompose into 16 audits: 8 per paper. Each has been split into its own file under `sorted-wave2-audits/` with model attribution, type, and one-line verdict (see the README there). `audit 1.txt` concatenates seven audits (gpt terra ×2, qwen ×2, grok, gemini ×2), `audit 2.txt` seven more (hy4, claude, "ai model", qwen, gemini ×2, grok); `max1.txt` and `max2.txt` are single deep audits each.

2. **Verification.** Every substantive defect claim in all 16 audits was checked against the current manuscript text at line level (exact line numbers cited below). Verdicts: **CONFIRMED** (genuine, still present), **VALID-MINOR** (genuine, low severity), **NOT CONFIRMED** (claim not supported by the current text), **FALSE POSITIVE** (claim is wrong), **SUGGESTION** (improvement, not a defect), **REJECTED** (the criticism itself is incorrect). Numerical verification claims made by the audits (max's ledger, both gemini assessments, qwen's checks) were cross-checked against my wave-1 recomputation and agree with it in every case.

3. **Outcome.** Of the **54 substantive defect claims** across all audits, **46 are verified genuine** (severity ranging from one false table caption and one conclusion overclaim down to trivial wording and notation items — all repairable by local edits; none overturns a theorem), **3 are false positives** (two produced by a text-unescaping artifact — the "\node → ode" and "\nu → u" claims in `max2.txt` — and one from auditing without the preamble), **1 is not supported by the current text**, **1 is rejected on the merits**, **1 was correctly self-retracted by its own auditor**, and **1 conditional worry resolved as already-correct** in the final text. The two most substantive surviving findings are:
   - **Instruments paper, Table 1 caption (L1296):** the claim that the lower and upper envelopes "coincide at r=0" is false outside the collapse case (β₀=1 vs U₀=R_n>1), contradicting the table's own row (L1289) and Proposition 4.18 (L1220). Found independently by gpt terra and gemini.
   - **Channel paper, Proposition (join, L1296):** stated for d_B≥3 but the join proof is vacuous at d_B=3 (the replacement sphere on W₂⊥ is S⁻¹=∅); the value is still true via the observable sphere, and the hypothesis also mismatches the companion's N_join≥2 (⟺ d_B≥4 at n=1). Found by claude, max2, and grok (softened), with gemini noting the degeneracy.

4. **Joint evaluation with wave 1.** Wave-2 audits independently corroborated five of my wave-1 findings (C_n in the channel Figure 2; the s-symbol clash; the duplicated decoder sentence; the finite-sample diameter cap living only in the proof; the companion asymmetries), sharpened three of them, and added ~25 verified findings my report had not listed. Conversely, my wave-1 audit retains ~14 findings that no wave-2 audit found (spelling conventions, load-bearing Nechita citation, abstract overclaim, appendix redundancy, bibliography order, Kolmogorov-width phrasing, the t's caption typo, typesetting inventory, and the mechanical-compile baseline itself). The union is consolidated in §8. Two wave-2 findings land on material **I authored** in the pre-revision synthesis paper (the λ=1 endpoint of the join proof, and the B-marginal naming convention — see I7/I5); both are fair catches and are acknowledged as such.

5. **Bottom line.** Both manuscripts remain mathematically sound at the theorem level — every audit that attempted full verification (qwen ×2, grok ×2, gemini ×2, max1, and my wave-1 pass) reached the same conclusion, and the defect claims that survive verification are wording-, scoping-, citation-, and edge-case-level. No audit found a wrong theorem. The three items that come closest to "mathematical" defects are the Table-1 caption falsehood (instruments), the conclusion's d_A=1 overclaim (instruments), and the hidden same-topology hypothesis in the profile-properties lemma (channel) — each fixable in one or two lines.

---

## 1. Inventory of the sixteen audits (sorted)

| File / lines | Model | Target | Type | Standout content |
|---|---|---|---|---|
| audit 1.txt L1–361 | gpt terra | instruments | line-level, 17 findings | caption r=0; d_A=1 overclaim; ρ_n/R_n ordering; 5 proof-wording items |
| audit 1.txt L362–389 | qwen | instruments | verification | "consistent"; macros/snippet caveats |
| audit 1.txt L390–636 | gpt terra | instruments | recommendations | physical roadmap; D_max reading; representation-vs-processor caveat |
| audit 1.txt L637–697 | qwen | instruments | recommendations | positivity-budget analogy; qubit dichotomy |
| audit 1.txt L698–710 | grok | instruments | verification | "all results follow"; conjugate-bar and sphere-dimension notes |
| audit 1.txt L711–2106 | gemini | instruments | line-level (mangled encoding) | A_0/E; table d_A−1; Figure 2(c) callout; covering-proof grammar |
| audit 1.txt L2107–2304 | gemini | instruments | assessment + verification | full verification checklist; physical insights |
| max1.txt (whole) | max | instruments | deep audit (2 passes) | "no mathematical error"; nd_B>1 hypothesis; notation overclaim; ledger |
| audit 2.txt L1–25 | hy4 | channel | preliminary (1st half) | figure caption items; cor:id-dep; Clifford parameters |
| audit 2.txt L26–84 | claude | channel | line-level (A/B/C) | join d_B=3; item-5 hypothesis; figure-caption forensics; cross-paper mismatch |
| audit 2.txt L85–260 | "ai model" | channel | line-level + intuition | \rhodep false alarm (retracted R_s alarm also here) |
| audit 2.txt L261–335 | qwen | channel | full audit | "no substantive errors"; duplicated sentence; coindex note |
| audit 2.txt L336–345 | gemini | channel | verification (1st half) | consistent |
| audit 2.txt L346–354 | grok | channel | cross-companion check | join d_B≥3 vs ≥4; C_n; conjugate bars |
| audit 2.txt L355–491 | gemini | channel | assessment + verification (2nd half) | full checklist; insights |
| max2.txt (whole) | max | channel | deep audit | "ode" compile-error claim (false positive); d_B=3 join (valid); consistency ledger |

Attribution caveats, stated honestly: (i) the "model" labels are the ones written into the files by whoever pasted them; hy4/"ai model"/"max" cannot be independently confirmed; (ii) the first gemini audit in `audit 1.txt` (segment 06) is corrupted by unicode mangling (math rendered one-glyph-per-line), so its quotes were reconstructed from context; (iii) claude's and hy4's audits cover "the first half" of the channel paper as delivered to them, which explains their "pending second half" hedging; their B-items are resolved here against the full text.

## 2. Method

Each substantive claim was located in the current manuscript text (grep at exact-string level, then full-line reads — truncation at 180–210 characters repeatedly hid quoted material, so all verdicts below are based on **full untruncated lines**); the surrounding proof was re-read where the claim was mathematical; and the claim was classified per the verdict scale in §0. Line numbers refer to the files in `manuscript uploads/` exactly as they stand today (byte-identical to the copies my wave-1 report used, re-verified by diff). Where a quoted sentence could not be found in the current text, the older in-repo versions (`joint-synthesis/`, `gpt round two/`) were searched to determine whether the quote was stale rather than hallucinated.

---

## 3. Verification: instruments-paper claims

MS-B = `instruments-paper-revised2.txt` (1,615 lines). "GT#n" = gpt terra's numbered finding in segment 01; "G" = gemini (segment 06 or 07); "max1#n" = max1.txt; "q/g" = qwen/grok verification segments.

| ID | Claim (abridged) | Source | Verdict | Evidence in current text |
|----|------------------|--------|--------|--------------------------|
| I1 | Table 1 caption: "The lower and upper envelopes coincide at r=0, in the collapse case, and from r=D on" — coincidence at r=0 fails in general (β₀=1, U₀=R_n=2(1−1/(nd_Bs))>1 unless nd_Bs=2) | GT#1, G | **CONFIRMED — most substantive instruments finding** | L1296 (caption, verbatim); contradicted by the same table's row L1289 ("exact gap R_n−1=1−ρ_n") and prop:gap L1220. Both audits' suggested replacement text is correct. |
| I2 | Conclusion: "for d_A=1 the subcritical widths are exact" — overclaims; the paper's own exact/certified accounting lists only the d_A=1 *antipodal profile* as exact, and marks intermediate widths open | GT#2 | **CONFIRMED — internal inconsistency** | L1481 (conclusion, verbatim) vs L159 (rem:exact-vs-certified: exact item (vi) is the profile; open item (a) is intermediate widths). GT's list of what *is* proved for d_A=1 matches the text. |
| I3 | ρ_n and R_n are used before they are defined | GT#3 | **CONFIRMED (presentation)** — with a citation nuance | ρ_n appears at L314 and L515 (remarks) and in Figure 1/caption L547/L568 ("centred in-radius ρ_n", "covering radius R_n"); formal definitions only at def:beta-best L900 and prop:gap L1218. Nuance: rem:radius-terminology itself (L536) uses the qualified names ρ_◇,inst/R_inst — the bare symbols are in the figure and neighbouring remarks, not in that remark's own text. |
| I4 | prop:diameter proof: "Testing … on a maximally entangled input produces the difference of two orthogonal flagged pure states" — outputs are I_{A₀}/d_A⊗σ±, not pure for d_A>1 (orthogonal on the flag factor; trace-norm 2 still correct) | GT#4 | **CONFIRMED (proof wording)** | L410 (verbatim). GT's repair (product pure inputs give pure outputs; or "orthogonally supported states of trace distance 2") is correct. |
| I5 | lem:spectral: "the support of the $B$-marginal Tr_B\|v⟩⟨v\|" — that is the A₀-marginal, not the B-marginal | GT#5 | **CONFIRMED** | L203 (verbatim; my earlier searches missed it only because "$B$-marginal" is in math mode). Schmidt-rank argument that follows is correct, as GT says. |
| I6 | thm:observable says "choose two orthogonal output states σ±" but cor:join-dimension needs them pure; the channel companion already says "pure" | GT#6, claude-C | **CONFIRMED** | L781 (no "pure") vs L854 (W_obs=span{\|φ±⟩}, needs pure σ±= \|φ±⟩⟨φ±\|); channel paper L1255 "Fix two orthogonal pure states σ+,σ−". A genuine cross-paper asymmetry. |
| I7 | prop:join-inst proof handles λ=0 but not λ=1: at λ=1, v=y₂/‖y₂‖ is undefined yet "Otherwise set vD₂=…" is invoked | GT#7 | **CONFIRMED (proof-completeness)** | L835 (full line): "Fix y and write λ=‖y₁‖², u=y₁/‖y₁‖, v=y₂/‖y₂‖ where the corresponding blocks are nonzero. If λ=0 … Otherwise set vD₁=…, vD₂=…". At λ=1 the (1−λ)vD₂ term has zero weight, so the result is safe, but the written proof leaves vD₂ undefined. Note: this proposition is one I authored in the pre-revision synthesis paper — a fair catch. Trivial fix (three-case split or "set the vanishing term to 0"). |
| I8 | thm:no-programming: "Hence every pure vector in the support of π_U programs 𝒰_U exactly" — does not follow from the eigenvector argument (superpositions need the extremality/convex-decomposition argument, which is absent; unnecessary anyway) | GT#8 | **CONFIRMED** | L1518 (verbatim, beyond the 180-char window). L1520 shows the conclusion is reachable via eigenvectors alone, exactly as GT notes. |
| I9 | rem:barrier(ii): "Orthogonal joins of full-body spheres … cannot extend the regime of antipodal separation 2 beyond it" — reads as a general impossibility claim; scope should be narrowed | GT#9 | **VALID-MINOR (wording)** | L1278. Fair point: "These are precisely the constructions already absorbed" is doing ambiguous work. Mitigating context my wave-1 report noted: the *first* paragraph (L1276) is explicitly scoped ("concerns these specific constructions rather than all possible codes"), and the open-problem list (L1483 (ii)) preserves the question. Recommended rewording per GT. |
| I10 | d_A=1 specialisation: "governed by the lower-dimensional replacement structure of the body" — for d_A=1 the replacement body *is* the whole body (same affine dimension nd_B²−1) | GT#10, G | **CONFIRMED** | L1331 (verbatim). Both audits' replacements are accurate. |
| I11 | thm:pinching display: ‖𝓘−(𝒫_B⊗id_{C_n})∘𝓘‖_{◇,inst} composes a flagged-channel-level map with the instrument tuple — type-inconsistent unless read componentwise | GT#11 | **VALID-MINOR** | L1114. Partially mitigated: L1110 *does* declare the componentwise convention (𝓘̃_k=𝒫_B∘𝓘_k) and L1112 the flagged-channel equivalent, one line before the display. The estimate is correct. GT's fix (write ‖𝓘−𝓘̃‖) is still the cleaner choice. |
| I12 | lem:domination: with the displayed conjugate-basis vectorisation, Tr_B\|K⟩⟩⟨⟨K\| is the transpose/conjugate of K†K — a reader sees an apparent missing transpose; state the identification | GT#12 | **VALID-MINOR** | L330 (convention declared: \|K⟩⟩=Σ\|ī⟩⊗K\|i⟩). Verified: the proof only needs ΣK_α†K_α=I, which survives the transpose because I is invariant. Correct observation, harmless in effect. |
| I13 | lem:inradius-concave: the concavity argument implicitly assumes the in-radius supremum is attained; use ε-radii or cite compactness | GT#13 | **VALID-MINOR** | L457 ("Assume 𝓘ᵢ+B(ρᵢ)⊆Inst … Optimising ρ₀ and ρ₁ independently"). Attainment does hold here (compactness), but it is not stated. One-line fix. |
| I14 | lem:inradius-concave carries no nd_B>1 hypothesis although the degenerate case (n=d_B=1, in-radius +∞) makes its statement ill-defined; the global convention covers it but is load-bearing exactly here | max1#1 | **CONFIRMED (scoping)** | Statement L432–449 (no hypothesis); rem:degenerate L151–154; thm:global-inradius *does* carry it (L472), so nothing downstream breaks — exactly max1's assessment. |
| I15 | rem:notation overclaims symbol consistency: W is reserved for "input or support subspaces" but prop:join-inst/cor:join-dimension use W⊆B⊗C_n (output-flag); E is reserved for the covering reference but the appendix uses E as the programming *input* system | max1#2 | **CONFIRMED** | L164 vs L818 (W⊆B⊗C_n) and L1495–1496 (E = program-task input). Also grok's related bar-placement note = I16. |
| I16 | Unremarked conjugate-basis flip: lem:spectral puts bars on the A factor, thm:exact-radius on the A₀ factor (both correct in context) | max1#3, grok | **CONFIRMED (trivial)** | L205 vs L262. |
| I17 | prop:gap item 1: the chain D_n+1≥nd_B²≥nd_Bs silently uses nd_B≥s | max1#4 | **CONFIRMED (trivial)** | L1234. |
| I18 | sec:lower intro sentence syntactically doubled ("builds … — … then combined … — and combines them …"); Figure 2(a) stops at r=13 leaving r_in=14 off-plot | max1#5 | **CONFIRMED (trivial)** | L521; L1356 (xmax=13.4). |
| I19 | Table 2 row for the full-direction sphere prints ν=(I_{A₀}−μ)/(d_A−1) with no d_A≥2 proviso — division by zero at d_A=1, where the theorem (L702) bypasses the correction state | G | **CONFIRMED** | L1449 vs L702–705 ("If d_A=1 … set J±(Z)=Θ±; Otherwise put λ=1/d_A"). |
| I20 | thm:collapse: "(see Figure 2(c))" is attached after case (ii) (d_A=1,n=1,d_B=2) but Figure 2(c) plots case (i) with (d_A,d_B,n)=(2,1,2) | G | **CONFIRMED** | L1205 vs figure title L1420 "(c) d_A=2, d_B=1, n=2: exact collapse". Gemini's fix (attach the callout to case (i)) is right. |
| I21 | thm:covering proof: "the maximally mixed state on the nd_Bs-dimensional support of that output" — the pure output's support is 1-dimensional; should say the containing subspace / the uniform instrument's output | G | **CONFIRMED (wording)** | L376. |
| I22 | thm:ball proof: an operator with a zero eigenvalue called "positive" where Prop 2.1 distinguishes "positive definite"/"positive semidefinite" | G | **VALID-MINOR (trivial)** | L280; physics-standard usage, but the inconsistency with the paper's own earlier distinction is real. |
| I23 | A₀ serves as the diamond-norm reference in Definition 1 while E is the reference in covering arguments — prefer one symbol | G | **VALID-MINOR** | L101–103 vs L164 and thm:covering. Compounded by I15. |
| I24 | "the exact gap is R_n−1" phrasing could be read as a gap in knowledge rather than the certified-lower-to-width gap | G | **VALID-MINOR (trivial)** | L1220, L1289. |
| I25 | rem:degenerate: add "(where the formula 2/(nd_Bs) does not apply)" to prevent mis-substitution | G | **VALID-MINOR (trivial)** | L151–154. |
| I26 | Figure 1 (radius notions): red dashed R_n circle "visibly drawn with a radius comparable to the body diameter" — possibly misleading | GT#15 | **REJECTED as a defect** | L542–551: the red circle is centred at I_*(0,0) with radius 2, and the true covering radius is R_n=2−ρ_n — comparable to the diameter by the paper's own complementarity identity; the caption (L568) already says "schematic" and flags ρ_n+R_n=2 as special. At most a cosmetic preference. |
| I27 | "Hence all state-space results transfer" (d_A=1) is vague about which results transfer | GT#14 | **VALID-MINOR** | L1323. GT's enumeration of what actually transfers is accurate. |
| I28 | thm:exact-radius "exactly two cases" abrupt; state once whether the companion uses the same Choi/diamond conventions | GT#16, GT#17 | **SUGGESTION** | L254. |
| I29 | Verification passes (qwen segment 02, grok 05, gemini 07, max1 ledger) | q, g, G, max1 | **CONSISTENT with wave-1** | All recomputed constants (D, ρ_n, R_n, L's, N_join, Q_ℓ, example numbers 56/29, 34/18, steps at 21/27, collapse at r=4) match my wave-1 verification log exactly. No conflicts found anywhere between their "verified" claims and the text. |

**Not found in the current text (instruments):** none of GT#7's skeptically-quoted siblings — all quotes located. One quote initially seemed absent (GT#7 "Otherwise set …") because of line truncation in my own tooling; it is present (L835) and valid. `B-marginal` (I5) likewise present (L203).

---

## 4. Verification: channel-paper claims

MS-A = `main-article-revised2.txt` (3,646 lines). "claude-A#" = claude segment 02 items; "hy4-n" = hy4 segment 01; "max2-x.y" = max2.txt sections; "q-n" = qwen segment 04 items; "G1/G2" = gemini segments 05/07.

| ID | Claim (abridged) | Source | Verdict | Evidence in current text |
|----|------------------|--------|--------|--------------------------|
| C1 | prop:join-channel assumes d_B≥3 but the proof is vacuous at d_B=3: dim W₂⊥=1 ⟹ Herm₀(W₂⊥)={0} ⟹ the replacement sphere S^{(d_B−2)²−2}=S⁻¹ is empty; the claimed range d_A²−2 is still true via the observable sphere alone; the L_join definition and Table 1 cite the join for d_B=3 | claude-A3, max2-2.1, grok, G1 | **CONFIRMED — most substantive channel finding** | Statement L1294–1303 ("Assume d_A≥2 and d_B≥3"); proof L1305–1313 (only notes "d_B−2≥1"); L_join def L1397–1401 (d_B≥3 branch); table row L1953–1955. Four audits agree (grok softened: "statement remains true"). Consensus fix: restrict to d_B≥4 or add the one-sentence d_B=3 reduction. |
| C2 | Cross-paper mismatch: channel join requires d_B≥3, instruments join requires N_join≥2 (⟺ d_B≥4 at n=1), yet the channel paper says its proposition "is the n=1 case of the instrument-level join" | claude-C, grok | **CONFIRMED** | A L1301–1302 vs B L856–866 ("If N_join≥2…" with N_join=(d_B−2)² at n=1). For d_B=3 the pointer is inaccurate as stated. This also refines my wave-1 cross-paper review, which had verified all *n=1 specialisation values* but not the hypotheses' edge. |
| C3 | Profile properties item 5 (metric perturbation) hides a hypothesis: comparing d₀/d₁-separations for the same h presupposes the same continuous-map class C(Sʳ,K); uniform closeness alone does not imply topological equivalence | claude-A1 | **CONFIRMED — genuine rigor gap** | Statement L258–260; proof L270–276 ("for every fixed h:Sʳ→K"). Claude's counterexample-style concern is mathematically right (uniformly close metrics can induce different topologies); the intended applications (equivalent norms) are safe. One-line hypothesis fix, as proposed. |
| C4 | "Effective Schmidt rank" remark is misplaced (sits between "The following spectral certificate gives…" and the subsection it points to) and cites "the witness V₀,V₁:S_A→B" with S_A undefined in the main text (defined only in the appendix) | claude-A2 | **CONFIRMED** | L818–826; S_A next appears at L3108 (appendix). |
| C5 | Envelope certification misattributes: the *existence* of the ball B̄(Ω,ρ_dep)⊆Chan is the exact-in-radius theorem; thm:global-inradius-channel only adds that re-centring cannot enlarge it — but both the envelope definition and the hierarchy proof cite the global theorem for the ball | claude-A4 | **CONFIRMED (citation precision)** | Definition certification list L1423–1426; proof L1467–1470 ("the globally optimal centred ball of Theorem thm:global-inradius-channel"). No mathematical error (both theorems are true and adjacent), but the citation is to the wrong theorem for the containment step. |
| C6 | thm:global-inradius-channel proof: (i) the halfspace characterisation is stated "about an interior point" but concavity is then used on all of K (boundary points give 0 — fine but unstated); (ii) Jensen over the Haar integral needs a continuity/measurability word — the instruments paper supplies Lipschitz continuity, this paper asserts only concavity | claude-A5 | **CONFIRMED (two one-line gaps)** | L1351–1372. (i) is genuinely a gap in the written argument; (ii) is correct as criticism — MS-B L503 explicitly invokes "concave and continuous (Lemma lem:inradius-concave)" while MS-A L1365–1366 says only "Jensen's inequality for the concave in-radius". |
| C7 | Figure 2 (fig:replacement-join) caption/body issues: (a) node "B⊗C_n: flag-diagonal nd_B² dim" uses C_n and n, never defined in this paper; (b) in-figure note "s=2 gives α_r=1 for 0≤r≤3⌊d_B/2⌋−1" clashes with s=min{d_A,d_B}; (c) caption's "≥2min ρᵢ" uses ρᵢ defined only in the appendix; (d) caption attributes the Jordan construction X↦X₊/TrX₊ to Lemma (replacement isometry) instead of the replacement-family theorem; (e) figure label R=Σ(bᵢ²−1)−1 collides with radius symbols; (f) r_out, r_in appear in the figure ~570 lines before their definitions; (g) "the block-join construction above" points at a construction that lives in the appendix | claude-A6, hy4-2, grok; (a)+(b) = my wave-1 A1/A2 | **CONFIRMED (all seven sub-claims located)** | L1119 (C_n); L1143 (s=2, r_out/r_in; definitions at L1715+); L1145 (caption: ρᵢ, and "(Lemma~lem:replacement)" for the Jordan map — the isometry lemma is L957–959, the Jordan construction is in the replacement-family theorem; the second citation to lem:replacement, for the isometry transfer, *is* correct); L1128 (R); L3351 (appendix R) vs L444 (sectional radius R_r); L3322/L3329 (ρᵢ, appendix only); L1153–1154 ("block-join construction above"). |
| C8 | Garbled sentence: "…then by the generalized Borsuk–Ulam theorem … applied to κ∘h gives, for every h…" | claude-A7, ai-model, max2 | **CONFIRMED** | L391–393 (verbatim). Three audits independently flag it. Math correct; grammar broken. |
| C9 | "The breakpoint L_{A,B}+1 separates two input-dependent scales" — the first scale (d_B²−1, output-state preparation) is input-*independent* | claude-A8 | **CONFIRMED (wording)** | L1477–1479. |
| C10 | Notation overloads: V (direction space 𝒱 L1291; unitaries V L1359; isometries V₀,V₁ L823/L3108; the domination matrix V), R (covering/sectional R_r L444; join dimension L1128/L3351), σ_u (Clifford states L1222 vs join-sphere states), ‖·‖_E declared and never used | claude-A9 | **CONFIRMED** | All occurrences located; ‖·‖_E at L427–429 with no later use. Extends my wave-1 A3 (which flagged q and Δ but not V/R/σ_u). |
| C11 | At d=2 the unitary-promise bound r≥d² is not sharp: PU(2)≅RP³ does not embed in ℝ⁴, so r≥5 | claude-A10 | **VALID as a note — not a defect** | L1196–1203: the proposition explicitly says "This is a lower bound …; whether d² coordinates admit an exact continuous encoder is not addressed here." The non-embedding fact is correct (embedding dimension of RP³ is 5); worth a footnote, nothing more. |
| C12 | Clifford construction: if the appendix took U_u=H_u⊕I_{C⊥} then U_{−u}=−U_u and the antipodal distance would vanish at powers of two | claude-B1 | **RESOLVED — no defect in the final text** | The appendix uses U_u^{(C)}=(I_C+iH_u)/√2, Ũ_u=U^{(C)}_u⊕I_{C⊥}, U_{−u}=U_u† (L3503–3509), which is exactly the working family claude proposed; (U_{−u}†U_u)²=−I_C ⟹ antipodal outputs orthogonal (maximally-entangled overlap Tr(iH_u)/p=0). G2's report of the formula is accurate. Residual minor point: the *main-text* theorem (L1166–1167) still says only "unitaries built from these anticommuting generators", leaving the formula to the appendix — a wording opportunity, consistent with C13. |
| C13 | σ_u, H_u, P_C, ‖H_u‖₁=p used in main-text corollaries before their appendix definitions | claude-B5, G1, hy4-4 | **CONFIRMED** | L1222–1236 (cor:clifford-exact and the separation corollary) vs L3490–3499 (definitions). hy4-4's request that σ_u be trace-one and positive is satisfied (σ_u=(P_C+H_u)/p, Tr=1, σ_uσ_{−u}=0 — verified). claude's parallel \TPHP claim is **not confirmed**: \TPHP(A,B) is introduced in thm:hierarchy L1438 and first *used* at L1442–1463, all before the Chebyshev-theorem uses at L1549+; ordering is correct (the macro is also defined at L37). |
| C14 | "Multiple TikZ figures use `ode` instead of `\node` — hard compilation problem, HIGH severity" (fig:dependency, fig:replacement-join, fig:comb-complete-code) | max2-1.1 | **FALSE POSITIVE** | The manuscripts contain 29 occurrences of `\node[` and 2 of mid-path `node[midway`; zero literal `ode`. The quoted "ode[box] (source)…" is `\node[box] (source)…` after a `\n`-unescape pass consumed the backslash-n of `\node` (same artifact produces the `\scriptsize]` fragments in the quotes). Tectonic compiles both papers with exit 0 and no errors (wave-1, re-runnable). The auditor's own hedge ("Unless there is an undefined macro ode in the preamble") was the clue. |
| C15 | Fiber-radius notation "u_r" is visually ambiguous / possible stray control sequence | max2-1.2 | **FALSE POSITIVE (same artifact)** | The notation is `\nu_r` (Greek nu): L596 "δ_r^c=ν_r", and def:fiber-widths defines ν(K;Y,X). The auditor's "could be misread as \nu" is exactly backwards — it *is* \nu, and the "line break before u" they saw is the escape artifact. |
| C16 | thm:global-inradius-channel proof defers the Haar-barycentre computation to a later theorem's proof | max2-3.1, ai-model | **CONFIRMED (minor)** | L1364–1365. The one-line Schur computation is the standard fix (both audits propose it). |
| C17 | lem:mixed-no-programming uses extremality of unitary channels without citation or proof | max2-3.2 | **CONFIRMED (trivial)** | L2356–2357 (the Nielsen–Chuang citation at L2359 covers the pure-program part only). |
| C18 | "informationally complete POVM" in prop:one-query-injective is IC for the channel affine hull, not the full output state space | max2-3.3 | **CONFIRMED (wording)** | L2885–2888 with Scott2006 cited for general IC-POVMs; the POVM has D_{A,B}+1 elements on A₀⊗B. |
| C19 | Finite-sample bound d_A√(d_A d_B)/(η√N) can exceed the diameter 2; the cap appears only in the proof | max2-3.4, G1 | **CONFIRMED — also my wave-1 micro-observation** | Statement L2922–2935; cap only in proof (L2984 per wave-1). Three-way agreement. |
| C20 | The comb figure caption forward-references cor:heterogeneous-slots (stated later) | max2-3.5 | **CONFIRMED (trivial)** | L2660 vs L2695. |
| C21 | "Hausdorff manifold of rank-k density operators" wording (noncompact, not closed) | max2-3.6 | **VALID-MINOR** | L2257–2258; the coindex argument only needs Hausdorff, as both max2 and the text note. |
| C22 | Duplicated decoder sentence in the pinching proof ("Define the decoder as above…") | qwen-1 | **CONFIRMED — my wave-1 A7, same lines** | L1762–1764. Two independent finds. |
| C23 | cor:id-dep: Tr_H\|J\| with both systems labelled H — say "over the output copy" | hy4-3 | **VALID-MINOR** | L935–938. (Symmetric example, so the formula is unaffected; clarity only.) |
| C24 | Appendix vectorisation identity: "with … \|K⟩⟩=Σ\|ī⟩_R⊗K\|i⟩_B **so that Tr_B\|K⟩⟩⟨⟨K\|=K†K**" | (qwen-2 endorsed it as "correct"; GT#12's analysis applies) | **CONFIRMED imprecision — a joint finding neither wave-1 nor qwen caught** | L3177, with the main-text convention at L634–639 (written unbarred: \|K⟩⟩=Σ_{a,b}K_{ba}\|a⟩⊗\|b⟩). Under the stated barred convention, Tr_B\|K⟩⟩⟨⟨K\| is the transpose/conjugate of K†K, not K†K itself; the conclusion actually used (Σ_α K_α†K_α = I) survives because I is transpose-invariant, and the ⟨⟨V\|K⟩⟩=Tr(V†K) pairing is fine. Qwen's polish note (add the output-copy clarification) stands, but its "this is correct" verdict glosses the missing transpose — the same subtlety GT#12 flagged in the *other* paper. Also a mild MS-A-internal presentation inconsistency: main text unbarred vs appendix barred notation for the same convention. |
| C25 | "The manuscript occasionally suppresses the ℤ₂ subscript in coind" | hy4-5, qwen-4 | **NOT CONFIRMED** | All 12 symbolic uses of `\operatorname{coind}` in MS-A carry the subscript (L319, L338, L363, L594, L2066, L2249, L2255, L2262 …); the other 29 "coind/coindex" hits are prose. Either already fixed in this revision or a misreading. |
| C26 | "\rhodep is an undefined macro … will fail to compile" | ai-model-1 | **FALSE POSITIVE** | `\newcommand{\rhodep}{\rho_{\mathrm{dep}}}` at L38; the audit itself hedged ("unless defined in a preamble not provided") — it was. |
| C27 | "s=2 gives α_r=1 for 0≤r≤3⌊d_B/2⌋−1 is arithmetically incorrect" | ai-model (self-retracted) | **Correctly retracted** | R₂=q(2²−1)−1=3q−1=3⌊d_B/2⌋−1 for both parities (verified: d_B=3,4,5 give 2,5,5). The auditor's visible self-check is honest and right; the formula in the figure/appendix is correct (the *symbol* clash is the real issue — C7(b)). |
| C28 | Verification passes (qwen segment 04, grok 06, G1+G2, max2 §4, ai-model spot-checks) | q, g, G, max2 | **CONSISTENT with wave-1** | Qubit example numbers (D=12, ρ=1/2, δ₀=3/2, β steps 1→1/2, U steps 3/2→1 at r=4, r_out=4, convex bound 18/10), pinching identity 2(1−1/ℓ), Q_ℓ balanced partitions, memory threshold m²−1≥D, packing η≤4/(L^{1/n}−1), tetrahedral γ_{2,2}≥1−(1/2)√(8/3), comb Lipschitz N‖·‖, sampled-transcript simplex dimension — all match my wave-1 recomputation and the texts. Grok's cross-companion specialisation checks agree with my wave-1 cross-paper review (except C2's hypothesis edge, which grok did flag). |

---

## 5. False positives, artifacts, and non-findings

**The unescaping artifact (max2).** Two of max2's three "high-priority" claims (C14 "ode", C15 "u_r") are systematic artifacts: when LaTeX source passes through a layer that interprets the two characters `\n` as a newline, every `\node` becomes ⟨newline⟩`ode` and every `\nu` becomes ⟨newline⟩`u`. The fingerprints are all over max2's quotes — "ode[box] (source)…", "write $ u_r(K;X)$", "u(K;Y,X)" — and its own hedges ("Unless there is an undefined macro `ode` in the preamble", "If this is merely a line break before `u`, then it is fine") show the auditor noticed the anomaly but reached the wrong conclusion. Practical lesson for future waves: any claim whose quoted text contains a suspicious line break right before a short token should be re-checked against the raw bytes before it is believed. Both manuscripts compile cleanly (tectonic, exit 0, no errors — wave-1, and the sources contain 29 `\node[` and zero literal `ode`/`nodeidway` tokens).

**Partial-input artifacts.** C26 (`\rhodep` "undefined") comes from auditing a snippet without the preamble (the macro is defined at L38); claude's B-items and hy4's items are explicitly hedged "pending the second half" — their open questions resolve cleanly against the full text (B1 resolved by the appendix formula, B2 resolved by my wave-1 re-derivation of the Lemma 3.2 bound, B4 consistent, B6 valid-trivial, B3 valid = C7(c)).

**Stale-vs-current.** No claim was found that quotes text absent from the current manuscripts except through the artifacts above. One initially suspicious case (GT#7's "Otherwise set…") turned out to be present but hidden beyond my own tooling's 180-character display cut — a reminder that "quote not found" verdicts require full-line reads before being asserted (this cut both ways during this verification).

**Soft claims that did not survive.** I26 (the radius-notions figure) is rejected on the merits: the drawing is centred at I_*, its proportions are consistent with R_n=2−ρ_n≈diam, and the caption already carries the schematic disclaimer plus the specialness of ρ_n+R_n=2. C25 (coind subscript suppression) is not supported by the current text.

---

## 6. Cross-audit consensus, divergence, and per-audit reliability

**Consensus findings (multiple independent audits, all verified):**

| Finding | Audits agreeing |
|---|---|
| d_B=3 join edge case (C1) | claude, max2, grok (softened), gemini-1 (degeneracy note) — 4 |
| C_n / n undefined in channel Figure 2 (C7a) | claude, grok, hy4 — 3 (+ my wave-1) |
| s-symbol clash in figure/appendix (C7b) | claude, hy4 — 2 (+ my wave-1) |
| Garbled Borsuk–Ulam sentence (C8) | claude, ai-model, max2 — 3 |
| Duplicated decoder sentence (C22) | qwen — 1 (+ my wave-1) |
| Finite-sample diameter cap (C19) | max2, gemini-1 — 2 (+ my wave-1 micro-observation) |
| Forward references to appendix definitions (C13, C16) | claude, gemini-1, max2, ai-model — 4 |
| Caption r=0 falsehood (I1) | gpt terra, gemini — 2 (missed by all others) |

**Divergences and how they resolve.** The sharpest divergence: qwen's channel verdict ("no logical gaps, misapplied theorems, or contradictory statements… mathematically rigorous and internally consistent") versus claude's A-list and max2's edge case. Resolution: qwen is *not wrong about the theorems* — every divergent item is a hypothesis-precision, proof-completeness, or wording matter — but qwen demonstrably under-reports (it endorsed the L3177 identity as "correct" (C24) and found none of C1–C6). Similarly grok's channel verdict "internally consistent across both halves and with the instrument companion" is too strong given C1/C2 — though grok itself listed the d_B≥3/≥4 mismatch as a "minor observation", which is the honest reading. On the instruments side, gpt terra's 17 findings versus qwen's "consistent": same resolution, and notably gpt terra's *mathematical* batting average on checkable claims is high (16 of 17 verified in some form; #15 rejected on the merits, #16/#17 stylistic only).

**Per-audit reliability ranking** (precision × yield on checkable defect claims, verified here):

| Audit | Defect claims | Verified | False/non-findings | Notes |
|---|---|---|---|---|
| claude (channel) | ~16 substantive | **all confirmed** (incl. 7-part figure forensics) | \TPHP ordering claim (1) | Highest precision and depth; the only audit to catch C3's hidden hypothesis and C5's misattribution |
| gpt terra I (instruments) | 17 | 15 valid (2 top findings), 1 rejected, 1 stylistic | 0 fabricated | Every quote located verbatim; strong mathematical judgment (the I4/I8 analyses are correct) |
| max1 (instruments) | 5 | all confirmed (trivial-to-minor) | 0 | Careful, modest, correct; ledger matches my recomputation |
| max2 (channel) | 9 | 7 valid (incl. top finding C1) | **2 false positives** (escape artifacts) | The d_B=3 catch is real and important; the "HIGH severity" compile claim is not |
| gemini ×4 | ~12 defect-level | all located & valid (I19–I25, C13, C19, C20) | 0 | Line-level segments arrive unicode-mangled but content is accurate; verification checklists match independent recomputation |
| grok ×2 | 5 notes | all accurate | 0 (verdict prose slightly overclaims) | Minimal volume, maximal accuracy per claim |
| hy4 (channel) | 5 | 4 valid (coind item not confirmed) | 1 | Honest hedging; first-half limits |
| qwen ×3 | 4 | 2 valid (duplicated sentence; polish) | 1 non-finding; 1 miss (C24 endorsed) | Conservative — good at not hallucinating, weak at finding |
| "ai model" (channel) | 6 | 3 valid | 1 false positive (`\rhodep`), 1 self-retracted alarm | The self-retraction of the R₂ formula was correct and commendable |

---

## 7. Joint evaluation with my wave-1 audit

**Where wave 2 corroborates wave 1 (independent confirmation):**

| My wave-1 finding | Wave-2 confirmation |
|---|---|
| A1 — C_n in Figure 2 (L1119) | claude-A6(a), grok, hy4-2 |
| A2 — s dual meaning (L1143, L3380/3411) | claude-A6(b), hy4-2 (plus "ai model" verifying the s=2 arithmetic) |
| A3 — q, Δ overloads | extended by claude-A9 (V, R, σ_u, ‖·‖_E) |
| A7 — duplicated decoder sentence (L1762–1764) | qwen-1, identical lines |
| Micro — finite-sample cap only in proof (L2984) | max2-3.4, gemini-1 |
| A10 — companion asymmetries | claude-C adds the join-hypothesis mismatch (C2); claude-C also confirms the observable-sphere pure-σ± asymmetry (I6) |
| §4 verification log (all constants/examples) | max1 ledger, max2 §4, both gemini assessments, qwen — all numbers identical |
| B7 — "error-one-barrier remark is scoped" | nuance: the remark's *first* paragraph is indeed scoped (as I wrote), but gpt terra correctly exposes the *second* paragraph's item (ii) as ambiguously overreaching (I9) |

**Where wave 2 extends wave 1 (new verified findings not in my report):** I1 (caption r=0), I2 (d_A=1 conclusion overclaim), I3 (ρ_n/R_n ordering), I4, I5, I6, I7 (λ=1 — in a construction I authored), I8, I13, I14, I19, I20, I21, C1, C2, C3, C4, C5, C6, C7(c,d,f,g), C10 (extension), C13, C16, C18, C23, C24. Notably, C24 is a finding that *emerged only from the joint evaluation* (qwen's endorsement + gpt terra's sibling analysis prompted the re-derivation).

**Where wave 1 remains the sole source (no wave-2 audit found these):** A4 (mixed British/American spelling, 25+ lines), A5 (load-bearing Nechita et al. citation in Lemma 3.2 — with my independent re-derivation), A6 (abstract's "matching upper bounds" overclaim), A8 (Clifford theorem's compound statement/double-bound p), A9 (structured-partition appendix redundancy), A11/A12 (overfull-box inventory, bibliography order, 24 orphaned labels, resizebox/graphicx), B1 ("Kolmogorov n-widths" phrasing), B2 (citation records to verify), B3 (the "t's" possessive in the comparison-table caption — still present at L1454), B4, B5, B6, B8, and the compile/integrity baseline itself (both papers compile clean, all cross-references resolve — the single fact that disposed of max2's compile-error claim).

**Corrections to my own wave-1 work prompted by this round:** (i) my cross-paper review verified specialisation *values* but not hypothesis *edges* — C2 (d_B≥3 vs N_join≥2) slipped through; (ii) I did not catch the caption/consistency items I1/I2; (iii) the join proof I authored in the pre-revision synthesis paper left the λ=1 endpoint implicit (I7) — the current instruments text inherited it. All three are now on the consolidated list below.

---

## 8. Consolidated defect list (union of wave 1 + verified wave 2), ranked

### Instruments paper (MS-B)

**Priority 1 — false statements as written (both one-line fixes):**
1. Table 1 caption "coincide at r=0" (I1, L1296) — reword per GT/gemini.
2. Conclusion "for d_A=1 the subcritical widths are exact" (I2, L1481) — qualify per GT (aligns with rem:exact-vs-certified L159).

**Priority 2 — proof completeness / scoping (one-to-three-line fixes, no theorem affected):**
3. prop:join-inst λ=1 endpoint (I7, L835); 4. prop:profile… n/a (channel); 4. thm:no-programming "every pure vector" (I8, L1518); 5. lem:inradius-concave hypothesis + attainment (I14, I13); 6. thm:observable "pure" σ± (I6, L781) — also restores companion symmetry; 7. prop:diameter pure-state wording (I4, L410); 8. lem:spectral "B-marginal" → "A₀-marginal" (I5, L203).

**Priority 3 — notation, ordering, captions:**
9. ρ_n/R_n before definition (I3); 10. Table 2 d_A≥2 proviso (I19, L1449); 11. Figure 2(c) callout placement (I20, L1205); 12. thm:covering "support of that output" (I21, L376); 13. "lower-dimensional" for d_A=1 (I10, L1331); 14. rem:barrier(ii) scoping (I9, L1278); 15. rem:notation W/E overclaim (I15, L164) + A₀/E (I23); 16. conjugation-flip note (I16); 17. "state-space results transfer" (I27); 18. pinching display (I11, L1114); 19. domination convention note (I12, L330) — and the same transpose clarification now also needed at MS-A L3177 (C24); 20. "exact gap" phrasing (I24); 21. "positive" vs "positive semidefinite" (I22); 22. prop:gap nd_B≥s line (I17); 23. sec:lower doubled syntax + figure (a) r-range (I18); 24. wave-1 B-items (Kolmogorov phrasing L928; t's caption L1454; B4; B5; citation records; overfull boxes).

### Channel paper (MS-A)

**Priority 1 — proof edge case and cross-paper hypothesis:**
1. prop:join-channel at d_B=3 (C1, L1294–1336) — restrict to d_B≥4 or add the reduction sentence; 2. the cross-paper pointer "this is the n=1 case of the instrument-level join" (C2, L1301) — align with N_join≥2.

**Priority 2 — rigor/citation precision (one-line fixes):**
3. profile-properties item 5 same-topology hypothesis (C3, L258); 4. thm:global-inradius proof notes (C6); 5. envelope certification attribution (C5, L1423/L1467); 6. L3177 vectorisation identity transpose (C24) + unbarred/barred notation alignment with L635.

**Priority 3 — figure, wording, forward references:**
7. Figure 2 overhaul (C7: C_n node, s=2 note, ρᵢ, Jordan-map attribution, R label, r_out/r_in forward refs, "construction above"); 8. garbled Borsuk–Ulam sentence (C8, L391); 9. Schmidt-rank remark placement + S_A (C4); 10. "two input-dependent scales" (C9); 11. Clifford corollaries' σ_u/H_u/P_C forward refs (C13) and main-text formula vagueness (C12 residual); 12. Haar-barycentre forward ref (C16); 13. "informationally complete" wording (C18); 14. finite-sample cap in statement (C19); 15. comb-caption forward ref (C20); 16. Tr_H clarification (C23); 17. "Hausdorff manifold" wording (C21); 18. extremality citation (C17); 19. ‖·‖_E and V/R/σ_u cleanups (C10); 20. wave-1 A-items (spelling A4; Nechita A5; abstract A6; Clifford compound A8; appendix redundancy A9; A11/A12 typesetting/bibliography/graphicx; micro-observations).

**Explicitly *not* defects (recorded to close the loop):** max2's "ode" and "u_r" compile claims (C14, C15); `\rhodep` availability (C26); coind subscript suppression (C25); the radius-notions figure proportions (I26); the PU(2)/RP³ sharpness note as a flaw (C11 — the paper already disclaims sharpness; keep as an optional footnote); claude's B1 Clifford worry (resolved by the appendix formula); the s=2 arithmetic alarm (C27, self-retracted, formula correct).

---

## 9. Overall assessment

The sixteen wave-2 audits, once sorted and verified, tell a consistent story with my wave-1 report: **both manuscripts are mathematically sound at the theorem level, and their remaining defects are concentrated in wording, scoping, citation precision, figure hygiene, and a small number of one-line proof-completeness gaps.** Across three independent verification waves (my wave-1 pass, the wave-2 verification segments, and this round's re-verification), no claim of a wrong theorem, wrong constant, or wrong example has survived checking; every recomputed number agrees. The union defect list above is fully editorial in the strict sense: no result needs re-derivation, and the two "false as written" statements (a table caption and one conclusion sentence) plus one proof edge case are each fixable in a single sentence.

The audits also differ meaningfully in reliability, and that difference is now measured rather than asserted: claude and gpt terra produced the deepest accurate findings; max1 was precise but conservative; the gemini segments were accurate despite mangled transport; grok was sparse but sound; qwen was sound but under-sensitive; max2 combined the single best channel-paper catch with the round's only high-profile false positives (an artifact, not a judgment failure); hy4 and "ai model" were honest but input-limited. For any future wave, the practical protocol is: verify quotes against raw bytes (full lines, no display truncation), compile before believing compile-error claims, and treat "pending the second half" hedging as resolvable rather than as a finding.

## 10. Security note

The repository credential used to retrieve and push these materials was shared in plaintext chat. It has now served its purpose for this task; rotate or revoke it, and prefer fine-grained tokens scoped to single repositories with short expiry for future rounds.
