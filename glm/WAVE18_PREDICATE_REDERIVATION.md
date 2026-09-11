# WAVE 18 — THE PREDICATE RE-DERIVATION PASS (statement-only, no new cellulation)
### Executed per the user directive of 2026-09-11: "a 'Wave 18 — predicate
### re-derivation' pass (statement-only, no new cellulation) that ends with
### either a pinned, machine-checkable predicate for δ₁ or an honest theorem
### that the paper-line link needs correction."

**Artifacts:** `wave18_predicate.py` / `wave18_predicate_output.txt`
(exact integer linear algebra: a self-implemented Smith normal form with
transforms, stress-tested 500/500 on random integer matrices; cyclic
C_m-(co)homology on explicit module matrices, validated on classical
answers incl. the rotation rep and Shapiro's lemma; the C₂/antipodal
RP² model; the coinvariant ring re-derived from scratch with sympy
Gröbner). 64 machine checks, all PASS. No new cellulation; the Wave-17
orbit-skeleton mod-2 fact is re-read from the committed JSON.

**Bottom line.** BOTH deliverables, in one coherent statement. **(a) The
pinned predicate** (P-δ₁): the ququart closure statement, re-derived under
non-orientability, in six equivalent machine-checkable forms, aimed at the
Stage-4 orbit SNF — the first δ₁ statement that is stable under everything
the construction stages have discovered. **(b) The correction theorem: the
Wave-8C paper-line link as recorded needed repair** — two defects that
Wave 15's non-orientability made load-bearing, both machine-certified on
the C₂/antipodal test case; the manuscript itself needs NO correction (it
claims only the bracket [4/3, 3/2] and poses the closure as open problem
(v)). **δ₁ REMAINS OPEN** — the transgression d₃(u₀) is not decidable at
the page level (the mod-2 shadow is nonzero, and the RP² test case
exhibits a nonzero-shadow transgression that is surjective) — but the
predicate it must be evaluated against is now pinned. The qutrit verdict
is untouched: H₂(B₃) = ℤ/3, δ₂(D(ℂ³)) = 4/3.

---

## 1. The re-derived chain (every premise labeled)

Let B₄ = Fl₄/⟨c₄⟩ (the free order-4 cyclic quotient, the coset lemma;
closed 12-manifold, χ(B₄) = 6), Z~ its orientation local system, and
E = Fl₄ ×_{C₄} S² → B₄ the S²-bundle with fiber action
R̃| = diag(R_{π/2}, −1)|_{S²} (the 4-cycle on the Σ = 0 hyperplane of ℝ⁴).

| step | premise type | content |
|---|---|---|
| 0 | **[machine, Wave 15 + §C re-derived]** | χ(c₄) = −1 exactly (the top graded piece of ℤ[x₁..x₄]/(e₁..e₄) is the sign rep): c₄ is orientation-REVERSING ⇒ **B₄ is NON-ORIENTABLE**, Z~(c₄) = −1. |
| 1 | **[machine, §C]** | the C₄-modules H^{2m}(Fl₄) (types (a,b,c) = (1,0,0), (0,1,1), (1,2,1), (1,1,2), (2,1,1), (1,0,1), (0,1,0)); the Gorenstein/PD symmetry type(6−m) = type(m)⊗sign holds 7/7 — a new consistency layer on the W15 module data. |
| 2 | **[machine, §D = W7 re-derived]** | the Z~-twisted cohomological CLSS page at total degree 3 has exactly: E₂^{3,0} = H³(C₄;Z~) = ℤ/2; E₂^{1,2} = H¹(C₄; H²(Fl₄)⊗Z~) = **0** (the W7 lattice fact ker(1−σ+σ²−σ³) = im(σ+1) re-derived); E₂^{0,2} = (H²(Fl₄)⊗Z~)^{C₄} = **ℤ·u₀**, u₀ = the primitive σ-anti-invariant class (1,0,1,0) (the standard-monomial class x₁+x₃). |
| 3 | **[theory: obstruction theory, cited]** | equivariant maps Fl₄ → S² ↔ sections of E (free action); the PRIMARY obstruction = the twisted Euler class e(E) ∈ H³(B₄; Z~ρ) with ρ = the fiber-orientation character = deg(R̃|) = −1 = **χ** — the same local system. |
| 4 | **[machine, §E3 = W7 re-derived]** | e(ξ_univ) = the generator of H³(BC₄;Z~) = ℤ/2 (w(ξ_univ) = (1+u²)(1+u) = 1+u+u²+u³ ⇒ w₃ = u³ ≠ 0; e mod 2 = w₃; the reduction ℤ/2 → 𝔽₂ injective); e(E) = κ*e(ξ_univ), κ the classifying map. |
| 5 | **[machine/theory, §D]** | the CLSS edge: e(E) ≠ 0 ⟺ the incoming d₃: E₃^{0,2} = ℤ·u₀ → E₃^{3,0} = ℤ/2 is **ZERO**; if d₃ is surjective, H³(B₄;Z~) = 0 and e(E) = 0. |
| 6 | **[theory: standard]** | e(E) ≠ 0 ⇒ no section ⇒ no equivariant map ⇒ the telescoping construction never avoids zero ⇒ **the four-flag statement** (every continuous f : P(ℂ⁴) → ℝ admits an ONB quadruple with all four values equal). |
| 7 | **[theory: elementary — the paper's own thm:state-nonflat template at d_B = 4]** | four-flag ⇒ (Tr c = 1 ⇒ minᵢ⟨ψᵢ|c|ψᵢ⟩ ≤ 1/4 ⇒ error ≥ 2(1−1/4) = 3/2; the constant decoder gives ≤ 3/2) ⇒ **δ₁(D(ℂ⁴)) = 3/2**. |

The chain is one-directional (sufficient), exactly as the paper's own
qutrit proof is. The Wave-8C scoreboard's "⟺" is retracted.

## 2. The correction theorem (what Wave 15 actually broke)

**(i) The twisted-PD pairing law of Wave 8C is invalid.**
`wave8c_homology_side.py` line 697 asserts
`H^k(B_4;Z~) ~ H_{12-k}(B_4;Z~)`. The correct law for a closed
n-manifold is **H^k(M;L) ≅ H_{n−k}(M; L⊗Z~)**; with L = Z~ (and
Z~⊗Z~ ≅ ℤ) this pairs **H³(B₄;Z~) with H₉(B₄;ℤ)** — and H^k(B₄;ℤ) with
H_{12−k}(B₄;Z~). Machine-certified on the C₂/antipodal test case
(ℝP², n = 2): the correct law matches in all three degrees
(H⁰(Z~) = 0 ~ H₂(ℤ) = 0; H¹(Z~) = ℤ/2 ~ H₁(ℤ) = ℤ/2; H²(Z~) = ℤ ~
H₀(ℤ) = ℤ), while the W8C law fails at k = 2: H²(ℝP²;Z~) = ℤ versus
H₀(ℝP²;Z~) = ℤ/2. Consequences:

* the W8C twisted-homology mirror E₂_{p,q} = H_p(C₄; H_q(Fl₄)⊗Z~)
  computes H₉(B₄;Z~), which mirrors **H³(B₄;ℤ)** — NOT the bit-group
  H³(B₄;Z~); the W8C line "|H₉| = |H³(B₄;Z~)| = 2 (bit zero) or 1
  (bit surjective)" faced the wrong group;
* the corrected mirror of the bit is the **UNTWISTED** page
  E²_{p,q} = H_p(C₄; H_q(Fl₄)) at total degree 9 (the H_q-modules =
  −ACT[6−m], the equivariant-PD transport), whose entries differ from
  the twisted page's: **(9,0) = ℤ/4, (7,2) = 0, (5,4) = 0, (3,6) = ℤ/2,
  (1,8) = ℤ/4**;
* under the orientability tacitly assumed at Wave 8, Z~ is trivial and
  both laws coincide — the slip was invisible until Wave 15's
  non-orientability made it load-bearing. (The W8C page ENTRIES
  themselves were right: re-verified 5/5, including with W8C's own
  module model — the Gorenstein duality makes the mis-modeled lattice
  isomorphic. Only the facing was wrong.)

**(ii) The Wave-7 generator label.** The anti-invariant lattice of
H²(Fl₄;ℤ) is generated by **u₀ = (1,0,1,0)** (primitive, machine-exact);
the Wave-7 name "(1,−1,1,−1)" is exactly **2u₀** (difference = the
diagonal (1,1,1,1)). Since d₃ is ℤ/2-valued, d₃(2u₀) = 2d₃(u₀) = 0
trivially — the bit is **d₃(u₀)**. This matters: 2u₀ has ZERO mod-2
reduction, and a generator with zero shadow would have FORCED d₃ = 0
(the naturality argument of §3, form 6), falsely closing the bit at the
page level; u₀ has NONZERO shadow, and no forcing occurs. The W7 π*-form
("π* hits the generator or only its double") was phrased with the correct
primitive and survives verbatim.

**(iii) The manuscript itself needs no correction.** It claims only
δ₁(D(ℂ⁴)) ∈ [4/3, 3/2] (thm:state-nonflat, exact upper bound = the
constant decoder) and poses the closure as open problem (v); the
"paper-line link" is the project's Wave-7 reconstruction of the natural
route, which SURVIVES the re-derivation with the corrected coefficient
bookkeeping.

## 3. The pinned predicate

> **(P-δ₁)** d₃^{0,2} : E₃^{0,2} = ℤ·u₀ → E₃^{3,0} = ℤ/2 is ZERO,
> u₀ = the primitive σ-anti-invariant class x₁+x₃ ∈ H²(Fl₄;ℤ)
> (the 4-tuple (1,0,1,0)).

Equivalent forms (each ⟺ P-δ₁, given the machine premises above):

1. π* : H²(B₄;Z~) → H²(Fl₄;ℤ) hits u₀ (not only 2u₀) [CLSS edge];
2. H²(B₄;Z~) = ℤ·u₀ (vs ℤ·2u₀) [page: E₂^{0,2}(Z~) = ℤu₀, E₂^{2,0}(Z~) = 0];
3. H³(B₄;Z~) = ℤ/2 (vs 0) [page: (3,0) = ℤ/2, (1,2) = 0];
4. e(E) = κ*e(ξ_univ) ≠ 0;
5. **H₉(B₄;ℤ) = ℤ/2 (vs 0)** — the corrected twisted-PD mirror, and the
   Stage-4 orbit-SNF target with UNTWISTED ℤ-coefficients in degree 9;
6. d₃^{𝔽₂}(ū₀) = 0 on the mod-2 CLSS page, ū₀ = u₀ mod 2 = the generator
   of H²(Fl₄;𝔽₂)^{C₄} = 𝔽₂·[(1,0,1)] — **the mod-2 shadow**: by
   naturality of the CLSS in the coefficient system (the C₄-map Z~ → 𝔽₂,
   −1 ≡ 1 mod 2), d₃^{Z~}(u₀) = d₃^{𝔽₂}(ū₀) under ℤ/2 ≅ 𝔽₂ (the target
   reduction is an isomorphism, machine-checked): the ℤ/2-valued bit is
   FULLY VISIBLE on the mod-2 page.

**P-δ₁ ⟹ δ₁(D(ℂ⁴)) = 3/2** (the chain of §1).

Necessary mod-2 condition (bit-zero ⟹): H⁹... H₃(B₄;𝔽₂) ∋ the (3,0)-image
≠ 0, hence H₉(B₄;𝔽₂) ≠ 0 by ℤ/2-Poincaré duality (valid on
non-orientable manifolds). The Wave-17 orbit skeleton gives the BASE-level
fact H₉^orb(𝔽₂) = 1 (the mod-2 fundamental class of the 9-dim base book
survives the non-orientable quotient) — consistent, supportive, but not
transferred (the T³-fiber SS is Stage-4 business).

## 4. What this wave machine-verified (64 checks, no new cellulation)

* the SNF-with-transforms engine: 500/500 random-matrix stress trials
  (reconstruction, unimodularity, diagonality, kernel extraction);
* the cyclic (co)homology engine on classical answers: C₄/ℤ, C₄/Z~,
  the rotation rep ρ (H₀ = ℤ/2, H_odd = 0, H_{even≥2} = ℤ/2), the
  induced permutation module (Shapiro: H₀ = ℤ, H_{p≥1} = 0), the qutrit
  augmentation ideal (H¹ = ℤ/3);
* the ℝP² model: H(ℤ) = (ℤ, ℤ/2, 0), H(Z~) = (ℤ/2, 0, ℤ) (the twisted
  fundamental class), H^*(Z~) = (0, ℤ/2, ℤ) — and the two PD laws
  (correct: 3/3 match; W8C: refuted at k = 2);
* the extension phenomenon: on the twisted CLSS page of ℝP² the
  E²_{2,0} = ℤ/2 piece cannot die yet H₂ = ℤ — the ℤ/2 is extension
  data (gr H₂ = 2ℤ ⊕ ℤ/2): product formulas for |H_k| are valid ONLY
  when all E∞ pieces are finite (relevant to E1: at total degree 9 all
  five entries ARE finite, so the product formula is valid there);
* the coinvariant ring, σ-matrices, order, Lefschetz (0 for c₄^j,
  j = 1,2,3), the orientation character (−1), the module table, the
  Gorenstein PD symmetry 7/7;
* the bit's page: E₂^{3,0} = ℤ/2, E₂^{1,2} = 0, E₂^{0,2} = ℤ·u₀;
  u₀ primitive, (1,−1,1,−1) = 2u₀; the pinned slot H²(B₄;ℤ) = ℤ/4
  re-derived; H⁰(B₄;Z~) = 0;
* the mod-2 layer: H²(Fl₄;𝔽₂)^{C₄} = 𝔽₂·ū₀ ≠ 0; the target reduction
  ℤ/2 → 𝔽₂ an isomorphism; the shadow statement of §3 form 6;
* the corrected untwisted mirror (5 entries) and the W8C twisted page
  (5 entries re-verified, both module models agreeing);
* the universal obstruction (w₃ = u³ ≠ 0 ⇒ e(ξ_univ) = generator);
* the Wave-17 orbit-skeleton mod-2 fact re-read from the JSON
  (H₉^orb = 1).

## 5. The honest gaps + the continuation

1. **The converse is not claimed.** If d₃(u₀) is surjective: e(E) = 0,
   the primary obstruction vanishes; a SECONDARY obstruction lives in
   H⁴(B₄;ℤ) (π₃(S²) = ℤ with TRIVIAL C₄-action — degree −1 maps act on
   π₃(S²) by (−1)² = +1), which is unpinned (the W15 cascade does not
   close); δ₁ could still be 3/2 by other means — or not. The paper's
   bracket [4/3, 3/2] is unaffected either way.
2. **P-δ₁ is not decidable at the page level.** The mod-2 shadow ū₀ ≠ 0,
   and the RP² test case (B6) is a nonzero-shadow transgression that IS
   surjective — no forcing either way. Deciding it is exactly the
   Stage-3.5/4 program: pin d(F) (the Wave-17 d²=0-mod-2 violation
   {5:18, 0:6} via the CKM-chain tracing), the level-L fibres over the
   certified skeleton (pt over V / S¹ over E / T³ over F and the generic
   strata), the seam battery, then the orbit SNF in degree 9 with
   UNtwisted ℤ (target: H₉(B₄;ℤ) = ℤ/2 or 0) and the twisted complex in
   degree 3 as the cross-check (H³(B₄;Z~)), with the mod-2 page as the
   third layer.
3. **The 13C pipeline (qutrit Stage 2a/2b, wave13c_total.py) remains the
   carried task** — untouched by this wave, which was statement-only.

## 6. Scoreboard

* **δ₁ (ququart): OPEN**, now against a STABLE pinned predicate (six
  equivalent forms, every premise labeled, the Stage-4 machine target
  identified). The predicate-instability pattern (W7 bracket → W8C
  equivalence → W15 invalidation) ends here: this statement is derived
  under non-orientability and survives everything the construction
  stages know.
* **δ₂ (qutrit): 4/3, machine-certified** (H₂(B₃) = ℤ/3, five
  consistency layers, the x² certificate, the S³ boundary, the stated
  bridge) — untouched.
* Manuscripts untouched.

**Nothing here reopens the qutrit verdict: H₂(B₃) = ℤ/3, δ₂ = 4/3.**
