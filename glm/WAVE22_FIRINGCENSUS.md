# WAVE 22 — STAGE 4c-cont: THE FIRING-CENSUS MACHINERY PORTED TO THE
### n=4 932-STRATUM COMPLEX + THE ORPHAN-LAYER TEST + THE SECONDARY-OBSTRUCTION PIN
### Executed per the user directive of 2026-09-12: "port the firing-census
### machinery to the n=4 932-stratum complex, test the orphan-layer
### question, and pin the secondary obstruction."

**Artifacts:** `wave22_firingcensus.py` (the port: Parts 0/A–E, ~20 s) /
`wave22_firingcensus_output.txt` / `wave22_firingcensus_data.json` /
`wave22_secondary.py` (the pin: Parts 0/A–D) /
`wave22_secondary_output.txt` / `wave22_secondary_data.json`.

**Bottom line.** ALL THREE DELIVERABLES, and the orphan-layer answer is the
opposite of the cheap expectation. **(a) THE PORT:** the W19-cScope
machinery (the character books, the firing census, the per-book twisted
homologies, the total complex, the provenance decomposition, the
correction-vacuity and support-descent tests) transferred to the n=4
structure where the κ-truncation lives — with TWO structural discoveries
the n=3 analog could not show: THE RADICAL THEOREM (the Γ₄ = Λ/2Λ ≅ (ℤ/2)³
dot-pairing is **degenerate** at n=4: the radical is the ρ-quad (1,1,1,1),
so the n=3 V-character slot **collapses to the trivial character**, and the
character group splits 4 dot + 4 **exotic**), and THE SIGN-LAYER
REQUIREMENT (at n=3 the W19 book complexes had ZERO fired 2-paths — the
no-chaining luck that made the +1 gauge honest; at n=4 **12 chained firing
triples exist**, so d² = 0 forces a sign layer: solved as the mod-2
exponent system, 36 variables / 6 equations, **CONSISTENT** — the
W20/W21 seam-battery pattern one level down, and it CLOSES). **(b) THE
ORPHAN-LAYER ANSWER: YES** — the n=4 book **does possess the
silently-dropped layer**: the **ψ₁₂ book** (the pure middle-composite root
labels a₁₂, a₂₃) fires (12 of the 36 GKM edges; 24 of the 72 E-strata) but
**ZERO of the 24 cells carry it** (the χ_w = ψ_{wρ−ρ} image is exactly
{triv: 8, ψ₁: 8, ψ₂: 8}) — the A2 ψ_ρ-orphan pattern **REPRODUCES** at A3,
with the twist that the highest root α₁₂₃ escapes into the mixed book ψ₂.
The dropped content is censused: the ψ₁₂ book complex carries **Z/8-torsion**
(the exact n=3 V-book ((ℤ/4)²) parallel), and the dropped Γ₄-blocks carry
**70 × ℤ/2 over the degree-9 window** — but the drop is structurally
correct (the χ-image theorem), so **the re-open verdict SURVIVES the
orphan test**. **(c) THE SECONDARY PIN:** H⁴(B₄;ℤ) = **ℤ²⁰¹ FREE** at the
certified levels 2/3 (no torsion secondary!), and **every computable
shadow of the secondary class vanishes machine-exactly** — the
torsion-to-free theorem: p₁(ν) = κ*p₁(V) with p₁(V) = 2v² ∈ ℤ/4 pulled
into a free group = **0 EXACTLY**; β(w₃) = 0 (2-torsion in free); Sq¹(w₂) =
0 (Wu + w₃ = w₁w₂) — the secondary route to δ₁ = 3/2 is
**ALIVE-BUT-INVISIBLE**: decidable only by the Stage-5 4-skeleton
construction.

---

## 1. The character theory (Part 0): the radical theorem

Λ₄/2Λ₄ = the 8 even-sum parity quads; the character group has 8 elements
but the dot pairing ⟨μ,γ⟩ is **degenerate**: its radical is
{0, (1,1,1,1)}, so only **4 dot characters** exist {triv, ψ₁, ψ₂, ψ₁₂}
(the other 4 are *exotic* — functionals with no lattice representative).
At n=3 the pairing was nondegenerate and (1,1,1) was not even in Γ₃; at
n=4 **the ρ-quad IS the radical**: the n=3 V-character slot (ψ_ρ) collapses
to the **trivial** character. The 6 roots collapse in pairs as characters:
α₁~α₃ (ψ₁, the outer simples — PURE), α₂~α₁₂₃ (ψ₂, the MIXED book: the
middle simple with the highest root), α₁₂~α₂₃ (ψ₁₂, the middle composites —
PURE). **The A2 E/V split does not lift cleanly: the composite labels
split between the mixed book (the highest root) and the orphan book (the
middles).**

## 2. The firing census (Part A)

The GKM/weak-order book of S₄: 24 cells (degrees 2l(w), counts
(1,3,5,6,5,3,1)), 36 Hasse edges (the W19 left-multiplication word
convention, w = s_k∘u), labels = the conjugated descent roots u·α_k. THE
DESCENT-IDENTITY GATE (χ_u·χ_w = ψ_label) passes on all 36. The label
census: **{ψ₁: 12, ψ₂: 12, ψ₁₂: 12}**; d(F) per book: **d(F)^ψ₁ = 8·(two
l=5 cells), d(F)^ψ₂ = 8·(one l=5 cell), d(F)^ψ₁₂ = 0** — the orphan book
does not fire at the top cell, exactly as the n=3 ψ_ρ-book had d(F) = 0.
**THE MOD-2 VANISHING:** every firing coefficient is |Γ₄| = 8 ≡ 0 mod 2 —
d(F) is a mod-2 cycle trivially; the primary-obstruction route's firing
shadow is dead at n=4, structurally (the same |Γ|-divisibility that killed
it in the W19 analog book). The E72 census (the 932-book's edge strata,
from the committed W17 JSON): {ψ₁: 24, ψ₂: 24, ψ₁₂: 24} — the ψ₁₂-descent
carriers exist in the E-layer of the 932-stratum book (the orphan's only
appearance).

## 3. The sign layer (Part B): the n=3-luck exposed

At n=3 the W19 book complexes had **zero** fired 2-paths (α-labels and
ρ-labels never chain), so the +1 gauge gave d² = 0 for free. At n=4 the
chains exist (12 chained triples over 6 (u,w,σ)-classes — forced whenever
χ_u = χ_w and χ_v = χ_u·σ). The parity gates pass (every fired count
even), and the mod-2 exponent sign system (36 edge variables, 6
equations) is **CONSISTENT with 30 free gauges**; the signed d² = 0 gate
passes on every book at every degree. **This is the W20 (1008-equation)
and W21 (1380-equation) seam-battery pattern one level down — the
machinery port required and found the sign closure.**

## 4. The per-book homologies (Part B)

With the signed boundaries (entries ±8 = ±|Γ₄|·[label = σ]): the ψ₁/ψ₂
books carry **Z/8-torsion layers** (ψ₁: Z/8 at H₀, H₂, …, H₁₀; ψ₂
similar); the **ψ₁₂ orphan book carries (Z/8)³ at H₂ and Z/8's through
H₈** — the exact parallel of the n=3 V-book's (ℤ/4)² at its middle H₂
(the |Γ|-torsion signature: ℤ/|Γ₃| = ℤ/4 at n=3, ℤ/|Γ₄| = ℤ/8 at n=4);
the triv book is the free (1,3,5,6,5,3,1) — the A3-book's free flag
homology, matching the W19's triv = (1,2,2,1) at n=3; the 4 exotic books
have zero firing boundary → free homology (nothing dropped there).

## 5. T₄ = the A3 book × Koszul(Γ₄) (Part C): the untruncated n=4 analog

Basis (w,i,j,k), 3,816 generators, degrees 0..13; D² = 0 exact; the block
decomposition H_n(T₄) = ⊕_w H_{n−2l(w)}(Γ₄; ℤ_{χ_w}) gated; the anchors
(H₀ = ℤ, H₁ = (ℤ/2)³ for the trivial module) pass. The t₂-pattern:
(0, 3, 6, 13, 24, 42, 63, 104, 140, **203**, 261, 347, 428, 540) — all
plain ℤ/2, no ℤ/4 at any degree. **THE UNTRUNCATED n=4 ANALOG:
t₂(9)(T₄) = 203** (the n=3 analog read 23; the certified truncated
932-stratum layer reads 3). THE DEGREE-9 PROVENANCE: **E:128 (ψ₁: 68,
ψ₂: 60) / N:75 / V:0** — the V-provenance is zero exactly as at n=3
(V:0), but for the structural reason (no ψ₁₂-cells) rather than the n=3
radical-free reason. The support-descent no-cut test passes automatically
(l + m ≥ 5 > 3 for every degree-9 generator).

## 6. The 932-stratum engagement (Part D)

The book: **V24 = the moment-graph cells (the χ_w labels) + E72 = the
firing labels (ψ_β) + the 836 T³-fibred strata = the trivial book** (the
W20/W21 certified flat gauge: free fibre-translations, base-neutral).
The κ-descent census (the 192 corners re-derived from the committed W17
corner data, the 48 same-k-shared removal re-verified): 144 shared-row
corners' root-sums telescope to the **leaf-pair characters {ψ₁: 48, ψ₁₂:
48, ψ₂: 48}**; the 48 disjoint corners sum to the radical = **triv**.
**THE STAR/QUAD TELESCOPING THEOREMS:** all 96 τ-strata (3 walls sharing
a row: the sum's quad is (1,1,1,1) = the radical) and all 72 q-strata
(the C₄-cycle sum telescopes to 0 exactly) carry the **trivial** descent
character. **THE WRAPPING GENERATOR'S BOOK:** the W21 decomposition
battery (re-read: the {s}-, {s,C,P}-, {F}-removals leave t₂(9) = 3; the
{s,w}-, {s,w,K}-, {s,w,K,T,Q}-removals collapse 3 → 0) says the
[1,3,3,1] layer lives on the cascade chain s→w→κ→τ, ALL of whose strata
are triv-book: **the degree-7 wrapping generator is a TRIVIAL-book
class and its (ℤ/2)⊗H*(T³) family is the untwisted fibre book — the
n=3→n=4 PROVENANCE FLIP (the n=3 analog read E:14/N:9/V:0; the n=4
certified layer reads N-carried).**

## 7. The orphan-layer adjudication (Part E): the decisive answer

(i) **The question answered: YES** — the silently-dropped layer exists:
the ψ₁₂ book fires (12 GKM edges + 24 E-strata) but has zero cell
carriers (the χ-image = {triv, ψ₁, ψ₂} exactly — the machine census);
the A2 ψ_ρ-pattern reproduces at A3 (with the highest-root escape into
ψ₂). (ii) The dropped content censused: the ψ₁₂ Γ₄-blocks carry
**70 × ℤ/2 over the degree-9 window** (H₉: 30, H₇: 20, H₅: 12, H₃: 6,
H₁: 2 — the counterfactual T₄-never-sees); the ψ₁₂ book complex carries
Z/8-torsion — the layer is NOT empty. (iii) The structural certificate:
the drop is CORRECT — χ_w = ψ_{wρ−ρ} is structurally a dot character and
the χ-image excludes ψ₁₂ exactly as the n=3 χ-image excluded ψ_ρ; the
V-correction vacuity test (the W19-(d) analog) passes: 0 cells to
remove, no ψ₁₂-artifact at any degree. (iv) **The verdict: the re-open
reading SURVIVES the orphan test** — the W19 tension (ii) was justified
(the layer exists), but nothing that carries 2-primary torsion is
wrongly dropped: the degree-9 count and the [1,3,3,1] certified layer
are unaffected.

## 8. The secondary-obstruction pin (wave22_secondary.py)

- **The group:** H⁴(B₄;ℤ) = Hom(H₄,ℤ) ⊕ Ext(H₃,ℤ) = **ℤ²⁰¹ ⊕ 0 FREE** at
  the certified levels 2/3 (the W21 Betti re-read from the committed
  JSON; the χ = 6 gate passes): the secondary obstruction at n=4 is NOT a
  torsion class — the structural contrast with the primary's ℤ/2.
- **The class's shadows, each machine-zero:** (i) **THE TORSION-TO-FREE
  VANISHING:** ν = κ*(V) with p₁(V) = c₁²−2c₂ = 6v² = **2v² ∈ ℤ/4**
  (c(V⊗ℂ) = (1+v)(1−v)(1+2v) machine-multiplied in ℤ[v]/(4v)); any
  homomorphism ℤ/4 → ℤ²⁰¹ is zero ⟹ **p₁(ν) = 0 EXACTLY**; (ii)
  β(w₃(ν)) = 0 (the Bockstein image is 2-torsion; the free group has
  none); (iii) Sq¹(w₂) = w₁w₂ + w₃ = 2w₃ = 0 (Wu + the rep structure
  w(V) = (1+u₂)(1+s): w₃ = w₁w₂); (iv) the fibre-parts vanish (the W21
  certificates: the left-equivariant polar lift 200/200 + the
  drift-zero spot checks — the section data over the fibre directions
  exists). The L(4,1) model validates the mechanism (the universal
  ℤ/2-Euler pulls back to 0 through the free H³(L;ℤ) — the same
  torsion-to-free).
- **The pinned predicate P-δ₁^sec:** (1) o₄ = 0 (the section extends over
  the 4-skeleton given e(E) = 0); (2) the shadow form: all
  characteristic-class shadows zero (machine); (3) the structural form:
  the finite C₄-structure forces the universal p₁ to pull back to zero —
  the secondary's only possible nonzero part is the FREE Hopf-class
  residual, invisible to characteristic classes; (4) the decision scope:
  the 4-skeleton obstruction-chain construction on the 932-stratum
  complex = **THE STAGE-5 TARGET**.
- **The honest gaps:** a nonzero free o₄ is ANOTHER sufficient route to
  δ₁ = 3/2 (parallel to the primary); the level-4 cross-check stands;
  even o₄ = 0 does not finish the 12-manifold's section problem (π₄(S²) =
  ℤ/2 at H⁵, … — the Stage-5+ chain).

## 9. Scoreboard

* **δ₁ (ququart): OPEN — the RE-OPEN status unchanged and now
  doubly-sheltered:** the primary's firing shadow is structurally dead
  (the |Γ₄|-divisibility), the orphan test passes (nothing wrongly
  dropped), the [1,3,3,1] certified layer is the triv-book wrapping
  family, and the secondary is pinned ALIVE-BUT-INVISIBLE (every
  characteristic shadow zero; the free residual = the Stage-5
  decision). The bracket [4/3, 3/2] intact.
* **δ₂ (qutrit): 4/3, machine-certified — untouched (H₂(B₃) = ℤ/3).**
* Manuscripts untouched.

**Nothing here reopens the qutrit verdict: H₂(B₃) = ℤ/3, δ₂ = 4/3.**
