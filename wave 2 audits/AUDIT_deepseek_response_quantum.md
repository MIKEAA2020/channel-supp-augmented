# Audit of `deepseek response_quantum.txt` (Wave 9)

**Audited file:** `wave 2 audits/deepseek response_quantum.txt` (1002 lines, added at commit 26680c2).
**Machine verification:** `glm/wave9_audit_deepseek.py` (this repo) / `scripts/audit_deepseek_wave2.py` (working copy), exact integer arithmetic (SNF / lattice calculus, no floating point). Transcript: `glm/wave9_audit_output.txt`.
**Bottom line:** the file's *honest* first half (E2-page, GKM orbits, problem statement) is correct and matches the repo's own Wave 8b verification. The file's *decisive* second half (the "split section kills the k3-cocycle" endgame and the four boxed conclusions, lines 822-1002) is **not valid mathematics**: the central reduction step is circular, the prototype "validation" computes the wrong objects, and a step it relies on is an unproven formula. **The two spectral-sequence bits remain OPEN; delta_2(qutrit) = 4/3 and delta_1(ququart) = 3/2 are NOT theorems.** A by-product of this audit is a *correction of the repo's own Wave 8c Section E* (its refutation of the cup-with-k2 formula was itself based on a wrong forced value).

---

## 1. Line-level verdicts

| Lines | Claim | Verdict |
|---|---|---|
| 1-9 | Status statement: "I will not claim a full SNF computation for H^4(B3)" | HONEST, correct framing |
| 13-152 | Milestone 1a: exact E2 page of B3 | **CORRECT** — machine-confirmed; identical to Wave 8b (`glm/wave8b_verify_flag_quotient_e2.py`). P = [[0,-1],[1,-1]], P4 = [[-1,1],[-1,0]], N = 0, H^{2k+1}(C3; iota) = Z/3, H^{even} = 0, the two-branch dichotomy H4(B3) in {Z/3, 0} |
| 155-234 | Milestone 1b: GKM orbit scaffold | **CORRECT** — machine-confirmed: 6 vertices in 2 orbits of 3, 9 edges in 3 orbits of 3; honest caveat at line 234 ("not yet the cellular 1-skeleton") is right |
| 238-262 | "Concrete route to the final SNF" (cellulate the 9 spheres + the 6-stratum) | Reasonable as a plan (this is the repo's standing plan); no claim verified here |
| 264-280 | **"A mathematically cleaner reduction is available: P2B3 = P2B(T2 x| C3)"**; "the deciding differential d3 for B3 agrees with the Cartan-Leray differential for the Borel model" | **UNSOUND (circular)** — see Section 3 below. Refuted by the RP2/BO(2) counterexample: level-1 equivariance of the Postnikov map does *not* induce a Borel map; it does so iff k2(B3) = k2(B(T2 x| C3)), which is equivalent to the qutrit bit itself |
| 284-330 | Prototype: M = (S^2 x S^2)/C4, forced nonzero d3, H4(M;Z) = Z/2 | **CORRECT** (the *target* is right) — re-derived here by the correct route (PD with local coefficients + UCT + exact CLSS page) |
| 374-439 | "Cellular model": standard CW on S2 (C0 = C2 = Z), T-action matrices J and -1, "quotient boundary maps vanish", H4(M) = Z/(T-1)Z = Z/2 | **INVALID** — see Section 4. (a) no equivariant CW with these chain groups exists (the antipodal is not cellular on the minimal CW); (b) the asserted vanishing of quotient boundaries is false for any honest equivariant cellulation; (c) **H4(M;Z) = 0** (M is a closed non-orientable 4-manifold), not Z/2 |
| 442-476 | "Exact SNF check" (sympy) | The code runs and its SNFs are what is printed, but it computes coinvariants of the *homology-level* action — not the homology of the quotient. See Section 4 |
| 478-495 | "H2(M) = Z/2 ... H4(M) = Z/2 ... H^4 ~ H4 ... the same quotient-chain SNF pipeline is operational" | **REFUTED** — honest quotient SNF gives **H2(M) = 0 and H4(M) = 0** (full answer: H*(M) = (Z, Z/4, 0, Z/2, 0)); the inference "H^4 ~ H4" is also wrong (UCT: H^4 = Ext(H3, Z)); the pipeline as applied is not operational |
| 499-509 | "What this does not yet settle" | HONEST and accurate |
| 510-544 | "Exact C3-resolution and k3-twisted Cartan-Leray model"; d3(alpha) = <alpha cup k3> | The resolution machinery is fine; the **formula is unproven** and is used as if established (see Section 5) |
| 548-627 | Cyclic cohomology code (sympy) | Correct (matches Wave 8b/8c engines) |
| 630-703 | "Algebraic twisted total complex" + "branch computation" | The branch "computation" (lines 659-689) is two hardcoded Python dictionaries — it computes nothing |
| 707-756 | "What now determines the branch": k3(B3) = k3(B(T2 x| C3)) | The *identification of the invariant* is a genuinely useful reframing; the reduction on which it sits is the circular step (Section 3) |
| 758-820 | "Why the 2-Postnikov reduction is more profound" | Overstated: the reduction is not valid as stated (Section 3) |
| 822-872 | **"Crossed-module computation: the split section kills the k3-cocycle"** | **UNSOUND where it matters** — the cocycle vanishing on the *split Borel side* B(T2 x| C3) may well be true (it is the standard MLW computation for a semidirect product), but the transfer "k3(B3) = k3(B(T2 x| C3))" (line 713-719, 869) is exactly the broken reduction. The document computes k3 of the wrong space. Counterexample: O(2) = S1 x| C2 splits, yet k2(RP2) = generator != 0 while k2(BO(2)) = 0 — same failure mode |
| 874-943 | d3 = 0, H4(B3) = Z/3, kappa*(u^2) != 0, **delta_2(qutrit) = 4/3** | **UNSUPPORTED** — conclusion does not follow (Sections 3-5) |
| 945-1002 | Ququart analog: **H3(B4;Z~) = Z/2, delta_1(ququart) = 3/2** | **UNSUPPORTED** — same two failure modes (circular reduction + unproven formula), and the ququart k3 value is not computed anywhere, only asserted by the same split argument |

## 2. What is confirmed (machine, exact)

- E2 page of B3 (all entries, both parities) — agrees with Wave 8b.
- GKM orbit pattern: 2 vertex orbits, 3 edge orbits, sizes (3,3), (3,3,3).
- The two-branch dichotomy for H4(B3) and H3(B3) (d3 = 0 vs iso) — this framing is correct.
- The prototype *target*: d3: E3^{1,2} = Z/2 -> E3^{4,0} = Z/4 on M is **injective** (im = 2Z/4Z), and H^4(M;Z) = Z/2. (Document's lines 300-330 correct; derived here via H3(M) = H^1(M;Z~) = Z/2 = Ext source.)

## 3. The central error: the "P2 B3 = P2 B(T2 x| C3)" reduction is circular

The document's reduction (lines 264-280, 721-735, asserted "rigorous") has the shape:
"C3-equivariant-up-to-homotopy Postnikov map Fl3 -> K(Z^2,2)  =>  Borel map B3 -> B(T2 x| C3) preserving the 2-type => the two d3's agree."

**Counterexample (machine-verified, Sections D/E/F of the audit script).** Take X = S^2 with the free antipodal C2-action, so X/C2 = RP2, and the analogous 2-Postnikov map f: S2 -> K(Z,2) = BS1 with conj on the target. Then:

1. f IS weakly equivariant (level 1): (f o a)^*u = -x = (conj o f)^*u on H^2. The document's hypothesis holds verbatim.
2. d3^{RP2}: E3^{1,2} = H^1(C2;Z_sign) = Z/2 -> E3^{4,0} = Z/2 is an **isomorphism** (forced: H^3(RP2;Z) = 0 for a closed 2-manifold, and H^4(RP2;Z) = 0).
3. d3^{BO(2)}: the same-named differential in the Serre SS of BS1 -> BO(2) -> BC2 is **zero** (forced: H^3(BO(2);Z) = Z/2 != 0, since the Bockstein beta(w2) is nonzero: rho beta(w2) = Sq^1 w2 = w1 w2 != 0 in F2[w1,w2]).
4. If the document's reduction were valid, the Borel map RP2 -> BO(2) would exist and force d3^{RP2} = d3^{BO(2)} by SS naturality. Contradiction. Hence **P2(RP2) != P2(BO(2))**: weak equivariance does NOT promote to a Borel map. The promotion requires *full coherence* of the equivariance, which exists iff k2(RP2) = k2(BO(2)) — i.e. iff the bit one is trying to compute is already answered.

For B3 the situation is identical in form: d3^{B3} = d3^{BT2-Borel} requires k2(B3) = k2(B(T2 x| C3)) = 0 (split side), which is *equivalent to the qutrit bit itself*. The document's "cleaner reduction" assumes the answer. (The consistent matching in the RP2 family is P2(RP2) ~ P2(B Pin(2)) — non-split, both k2 = generator, both d3 = iso.)

## 4. The prototype "validation" computes the wrong objects

The document's Section "Milestone: quotient-chain SNF" (lines 374-495) treats the *homology-level* action matrices (J on H2, -1 on H4) as if they were cellular chain actions of an equivariant CW with vanishing differentials, then takes coinvariants. Three independent errors:

1. **No such equivariant CW exists.** The minimal CW of S2 (one 0-cell + one 2-cell) admits no cellular antipodal action (the 0-cell would have to be antipodally fixed).
2. **Category error.** The coinvariants of the homology action are E2_{0,q}-terms of the homological Cartan-Leray page, not H_q of the quotient: H_0(C4; H_2) = Z/2 is exactly E2_{0,2}, H_0(C4; H_4) = Z/2 is exactly E2_{0,4}. In the true spectral sequence these terms are *killed by differentials* (d3: E3_{3,0} = H_3(C4;Z) = Z/4 -> E3_{0,2} surjective; d5: E5_{5,0} = H_5(C4;Z) = Z/4 -> E5_{0,4} surjective), because H2(M) = H4(M) = 0.
3. **The true answer.** The honest equivariant cellulation (cells = lifts of the RP2 CW; product CW on S2 x S2; T_*(u (x) v) = (-1)^{|u||v|} a_*v (x) u, exactly order 4 on chains) gives by exact quotient SNF:

   **H_*(M) = (Z, Z/4, 0, Z/2, 0)**  — in particular **H_2(M) = 0 and H_4(M) = 0**, contradicting the document's outputs "H_2 = Z/2" (line 482) and "H_4 = Z/2" (lines 420-429). Cross-checks: chi(M) = 1 = chi(S2 x S2)/4; H_1 = Z/4 = pi_1(M)^ab; H_3 = Z/2 = H^1(M;Z~) by PD; H^4(M;Z) = Ext(H_3,Z) = Z/2 (the document's *target* value, reached by the correct route).

   The same honest pipeline reproduces H_*(RP2) = (Z, Z/2, 0) exactly, which is what a *valid* prototype validation should look like. The "H^4 ~ H_4" inference (lines 485-492) is also wrong as stated (UCT: H^4 = Ext(H_3,Z), not H_4).

   **This is the repaired deliverable of this audit**: the quotient-chain SNF pipeline *is* operational when fed an honest equivariant cellulation — the document's shortcut (homology matrices + vanishing boundaries) is what fails.

## 5. The unproven formula, and a correction to the repo's own Wave 8c

The document repeatedly relies on d3(alpha) = <alpha cup k3> (lines 529, 648, 782, 819) without proof. Note the repo's own Wave 8c (commit 8d7fef6, Section E) had *refuted* this formula via the pair BO(2) / B(binary-dihedral): "k2 differs, d3 identical (both zero)".

**Wave 8c Section E is itself in error, and this audit corrects it.** The claimed forced value "d3 = 0 in both cases" used "UCT forces H_2 = Z/2 coinvariants, hence H^3 = Ext(H_2) = Z/2 survives". For B Pin(2) (the binary-dihedral group, j^2 = -1) this is wrong: the fibration RP2 -> B Pin(2) -> BSU(2) (fiber SU(2)/Pin(2) = S2/antipodal = RP2; base simply connected) has E2^{p,q} = H^p(BSU(2); H^q(RP2)) with all total-degree-3 entries zero, so **H^3(B Pin(2);Z) = 0** and therefore **d3^{B Pin(2)} = iso (nonzero)** — while d3^{BO(2)} = 0 stands. Hence the two d3's are *not* identical, the Wave 8c refutation collapses, and the formula's status returns to **unproven but consistent** in every testable case:

| case | k2 | d3 | formula-consistent? |
|---|---|---|---|
| BO(2) (split) | 0 | 0 | yes |
| B Pin(2) (non-split, j^2 = -1) | Bockstein != 0 | iso | yes |
| RP2 | generator != 0 (twisted transgression, Spanier's theorem) | iso | yes |

The formula remains unusable as a proof step until it is itself proven; the document treats it as established.

## 6. Status of the two bits (unchanged)

- **Qutrit:** H^4(B3;Z) = Z/3 iff the CLSS d3: E3^{1,2} = Z/3 -> E3^{4,0} = Z/3 vanishes. OPEN.
- **Ququart:** H^3(B4;Z~) = Z/2 iff the twisted d3: E3^{0,2} = Z.(1,-1,1,-1) -> E3^{3,0} = Z/2 vanishes. OPEN.
- Numerical evidence (Wave 8a) continues to favor both vanishings (hence delta_2 = 4/3 and delta_1 = 3/2), but neither is a theorem. Manuscripts are untouched and must remain untouched.

**What the audit adds to the roadmap:** (i) the pipeline for the honest cellulation is now *demonstrated* end-to-end on a nontrivial free action (S2 x S2 / C4, correct answer with cross-checks); (ii) the 2-Postnikov shortcut is definitively closed as a route unless one first proves k2(B_d) = k2(B(T^{d-1} x| C_d)) — which is the bit itself; (iii) the cup-with-k2 formula is back on the table as a *plausible lemma* (all three known test cases consistent) — proving it would reduce both bits to computing k2(B_d), i.e. to the MLW class of the crossed module attached to the honest equivariant 3-skeleton of Fl_d.

## 7. Provenance / honesty notes

- The document's opening (lines 1-9, 333-354, 499-509) explicitly disclaims a completed computation — good. The final sections (822-1002) then override this with boxed "settled" conclusions that the preceding text does not support. This pattern (honest preamble, unsound endgame) is exactly the one Wave 8b flagged in the previous claimed output; it must not be recorded in the manuscripts as settling anything.
- No changes were made to any manuscript. delta values, theorem statements, and the open-problem list are unaffected by this audit.
