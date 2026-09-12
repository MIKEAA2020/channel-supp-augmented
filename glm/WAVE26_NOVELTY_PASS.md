# WAVE 26 — THE FULL-TEXT NOVELTY PASS + THE v7 FLAW AUDIT
### Executed per the user directive of 2026-09-13, English only, PAT re-supplied:
### "1- full-text arXiv/MathSciNet novelty pass 2- remaining merited work for
### channels or instrument papers? 3- check both for genuine flaws and
### internal inconsistencies. don't fabricate any."
### This is merited-queue item 4 of EXTERNAL_MERIT_AUDIT §4 — the last item.

**Artifacts:** the search logs in `glm/novelty_pass/` (23 web-search JSONs,
the arXiv query battery with its rate-limit record, the arXiv website-search
pages incl. the two Guerra–Jana abstracts, 10 zbMATH Open JSONs, and
`INDEX.json`); the v7 consistency checker `scripts/check_v7.py` (workspace);
the tectonic recompiles of both v7 sources. This note.

**Bottom line.** The theorem forms of both v7 manuscripts are **clean of
collision** across every channel this pass could reach — arXiv (metadata
query battery + website search), zbMATH Open, and Google-scale web search.
The exact-value widths (δ₁(Δ₄) = 4/3, δ₂(qutrit) = 4/3, the ququart bracket),
the equal-value-basis theorems (both indices), the instrument-body exact
geometry (affine dimension, in-radius, optimal centre, covering radius,
complementarity), and the query-uniform compression framework return **no
prior art**. One **near-collision line** was found and must be engaged before
submission: the 2023–2025 Guerra–Jana programme on the cohomology of
unordered flag quotients and Auerbach bases. The v7 flaw audit found **no
mathematical or internal-consistency flaws**; one trivial editorial nit; and
the missing-citation gap above, which is a positioning flaw of omission, not
of mathematics. Nothing was fabricated in either direction: every verdict
below is tied to a saved log.

---

## 1. The battery, and its honest scope

* **23 web searches** (`web_q*.json`): the theorem-form phrasings, the
  geometry keywords, the width/compression keywords, the unistochastic
  lineage, the no-programming landscape. Google-scale coverage (full-text
  indexing of arXiv, journals, zbMATH, Wikipedia, forums).
* **arXiv API** (`arx_*.xml`, 20 queries): the burst was **rate-limited by
  arXiv** after the first queries ("Rate exceeded" — recorded verbatim in the
  files); the battery was re-issued through the **arXiv website search**
  (`arxs_*.html`, 16 queries) which is a different endpoint and worked.
  The null results below are from the website search pages (the 16.4 KB
  "no results" pages are preserved).
* **zbMATH Open** (`zbm_*.json`, 10 queries): the open reviewing database.
  **MathSciNet itself is paywalled and no credentials exist in this
  environment — that scope limit is stated plainly.** zbMATH Open + the
  web-index arXiv coverage is the honest substitute; a MathSciNet pass
  remains a one-hour task for the author at an institution, and nothing in
  the found landscape suggests it will change the verdict (zbMATH indexes
  the same mathematical literature; the near-collision line was found BY
  zbMATH and cross-confirmed on arXiv).

## 2. The theorem-form null results

Every one of these returned **zero relevant hits** (the saved pages are the
evidence; see `INDEX.json` for the query→verdict mapping):

| claim | queries | result |
|---|---|---|
| equal-value orthonormal bases (r=1, plane r=2) | `"equal value" "orthonormal basis"` (arXiv: 0 results); ham-sandwich × quantum (web: generic); equipartition × basis (web: thermodynamics noise) | **no collision** |
| δ₂(D(C³)) = 4/3, δ₂ ≥ 4/3 for d_B ≥ 3 | `4/3` width phrasings, "flat width" | **no collision** |
| δ₁(Δ₄) = 4/3 / ququart [4/3, 3/2] | simplex-width phrasings | **no collision** |
| channel/instrument-body exact geometry | `quantum channel inradius` (arXiv: **0 results**), `in-radius` (noise), Chebyshev/covering radius × quantum (arXiv: 0; web: permutons/hamming, unrelated), affine dimension × instruments | **no collision** — closest: Burrell's depolarizing Bloch-ball geometry (different object), "Almost all quantum channels are equidistant" 2026 (asymptotic diamond distances, not the in-radius) |
| continuous-encoder compression widths | `nonlinear width` × quantum (arXiv: 0), autoencoder × topological × quantum (web: Batson et al. and Kvalheim–Sontag — **both already cited** in v7), quantum-autoencoder compression-rate line (Ma 2023 et al. — architecture-specific, different problem) | **no collision** |
| instrument-level join / antipodal core | antipodal/join phrasings | **no collision** |
| no-programming (appendix) | the Nielsen–Chuang / Gschwendtner–Kubicki landscape is present and **already cited** (NielsenChuang1997, KubickiPalazuelosPerezGarcia2019) | background appendix, no claim conflict |

## 3. The near-collision line (the one genuine finding)

**Guerra–Jana**, in two papers, plus the surrounding school:

* **arXiv:2309.00429**, *Cohomology of complete unordered flag manifolds*
  (Trans. AMS **378**, 3507–3550, 2025): quotients of complete flag manifolds
  in C^n and R^n by **Σ_n**; homological stability; closed-form stable
  cohomology rings; an algorithmic procedure for the unstable additive
  cohomology.
* **arXiv:2304.12990**, *The mod-2 cohomology groups of low-dimensional
  unordered flag manifolds and Auerbach bases* (Topology & its Applications,
  2025): real unordered flag manifolds for small n; the computation improves
  the known estimate of the **number of Auerbach bases** of small-dimensional
  normed spaces.
* Surrounding school (found, not currently cited anywhere in v7): Weber's
  Pełczyński-conjecture line (Auerbach bases via LS category / cup-length of
  real flag manifolds), Korbaš 2003 (Z₂ cup-length of real flag manifolds),
  Menet 2018/2019 (integral cohomology of quotients by prime-order
  automorphisms, isolated-fixed-point regime), Matszangosz 2019 (integer
  cohomology of real partial flag manifolds, algorithmic), the classical
  Z_p-Borsuk–Ulam literature (cyclic-group BU theorems, incl. the 2022
  connective-K-theory version).

**The differentiation, stated precisely:**

| axis | Guerra–Jana | this project (v7) |
|---|---|---|
| space | Fl_n/Σ_n (full symmetric group) | **Fl₃/C₃** (the cyclic = alternating subgroup, an intermediate quotient the TAMS paper does not treat) |
| coefficients | field coefficients, any characteristic; mod-2 explicit | **integral**, the 3-torsion with the exponents pinned |
| the decision bit | not present (their cohomology is direct) | the **two-worlds d₃^{1,2} bit** + its machine certificate |
| application | **Auerbach bases** of real normed spaces (counting estimates) | **equal-value orthonormal bases** for continuous f on P(C³) → quantum compression widths |
| output | cohomology + basis counts | δ₂(D(C³)) = 4/3 + the width theorems |

None of the project's theorem forms appears in their work, and none of their
results is claimed in the project's papers. **But the seam is the same seam**
(flag-quotient cohomological obstruction → basis-existence theorems), their
machinery would cover the cyclic case as an easy variant, and their
application (Auerbach) is the exact sibling of the equal-value-basis
application. A referee drawn from this school — and Topology & its
Applications / TAMS referees would be — will know these papers. **The v7
manuscripts cite none of them.** This is the single highest-risk item the
pass found, and it is a *citation/positioning* gap, not a collision.

## 4. The v7 flaw audit ("don't fabricate any" — none were)

Mechanical (`scripts/check_v7.py`, both papers):
labels/refs — no danglers, no duplicates; cite keys — all resolve;
environments — balanced; display math — 197/197 and 233/233 balanced; `$`
parity — even after proper comment stripping; non-ASCII — none;
`\left/\right` — balanced. The three raw flags (the `\[` counts 200/197 and
237/233, the odd MAIN `$` count 3071) were **diagnosed to the line** and are
checker artifacts: `\\[4pt]` line-skip tokens (3 and 4 of them) and
multi-line inline math / TikZ `\\$` nodes — not paper flaws. Both sources
**recompiled under tectonic with no errors** (the compile-test copies were
verified byte-identical to the v7 sources first).

Line-level (the W25 block, read against an independent re-derivation done
in this session): the `lem:flag-cohomology` E₂-page claims were re-derived
by hand here — H²(Fl) = Z³/Z(1,1,1) with cyclic P; N vanishes; M^P = 0;
(P−1)M = the sum-zero image with index three → E₂^{1,2} = Z/3 ✓; H⁴(Fl) =
Z² with the order-three trace −1 action, no fixed vectors → E₂^{0,4} =
E₂^{2,2} = 0 ✓; E₂^{4,0} = Z/3 ✓; the d₂/d₄ vanishing analysis and the
H³ = ker d₃, H⁴ = coker d₃ forcing ✓; the UCT reading (Ext(H₂), Ext(H₃)) ✓;
and the total-degree 5/6 cross-check (the d₃^{3,2} → E^{6,0} iso killing
both, leaving H⁵ = Z/3 from E^{1,4} and H⁶ = Z from E^{0,6}) is consistent
with the machine tuple at the page level ✓. `thm:equal-basis-plane`:
the T = T₁⊗I₂ conjugation, the J-structure, c₂(L⊕L) = c₁(L)² = x², and
the nowhere-vanishing-section → e = 0 contradiction ✓.
`thm:state-d2`: the trace inequality Σ⟨ψ_i|c|ψ_i⟩ = Tr(cP_V) ≤ 1, the
traceless-X bound ‖X‖₁ = 2TrX₊ ≥ 2(1 − ⟨ψ|c|ψ⟩) ≥ 4/3 (witnessed by the
projector ψψ*: Tr X₊ ≥ Tr(ψψ*X) = 1 − ⟨ψ|c|ψ⟩) ✓; the monotonicity/upper
bound chain and the 2(1−1/d_B) ≥ 4/3 ⟺ d_B ≥ 3 check ✓.
`cor:bottom-dichotomy` case table and the twice-corrected
`con:coord-flat` narrative (each correction's refuting instance) ✓.
Cross-paper: the MAIN sync clause (open problem 1) matches
`thm:state-d2` exactly; the bracket statements match everywhere.
Machine-artifact consistency: 4,970 orbits × 3 = 14,910 cells ✓;
H_*(B) = (Z, Z/3, Z/3, Z/3, Z/3, 0, Z) in `wave13c_h34_output.txt:222` ✓;
χ(Fl) = 6 = 3χ(B) ✓.

**Genuine findings (both minor, neither mathematical):**
1. `main-article-revised7.txt` carries an **uncited bibitem**
   (`NechitaEtAl2018` never `\cite`d) — a dead reference-list entry. Trivial
   fix; harmless (thebibliography prints it either way).
2. **The citation gap of §3** — the missing Guerra–Jana / Auerbach-school /
   Z_p-BU citations. A positioning flaw of omission.

**No fabricated flaws:** every check above either passed with the saved
evidence or failed with a diagnosed checker artifact. Nothing was invented
to make the audit look productive.

## 5. The verdict, and the remaining merited work

**Are the results novel at full-text scale?** The quantum-information
theorem forms: **yes** — clean across arXiv, zbMATH Open, and web-scale
full-text coverage, with the closest neighbors (Batson, Kvalheim–Sontag,
the quantum-autoencoder line, Burrell, the equidistant-channels 2026 note)
already cited or clearly disjoint. The pure-topology premise sits **next
to** an active line (Guerra–Jana) that must be cited and differentiated;
the differentiation exists and is clean (§3), but it is currently absent
from the papers.

**The remaining merited queue (both papers):**
1. **The v8 citation/positioning pass** — REQUIRED before any submission,
   and now the only blocking item: add the Guerra–Jana pair (both papers),
   Weber/Korbaš (Auerbach-via-flag-cup-length school) and the Z_p-BU
   background to the instruments paper's related work; one positioning
   paragraph each ("the cyclic quotient is not among the quotients they
   treat; their application is Auerbach counting, ours is the equal-value/
   width chain; the machine premise is complementary to their algorithmic
   programme"); the same anchors where the main article touches the flag
   story; drop or cite `NechitaEtAl2018`. Estimated: one anchored edit
   script, one compile, one consistency re-run.
2. **The independent re-implementation / machine-free derivation of
   H^{3,4}(B)** — already open problem (vi); still the last computational
   residual; merited but heavy (a second implementation of the 13C chain or
   a Guerra–Jana-style derivation adapted to the cyclic case — their
   algorithmic procedure is a candidate independent route).
3. **A MathSciNet pass at an institution** — one hour, author-side; the
   zbMATH/Open coverage here makes a surprise unlikely.
4. **Not merited** (unchanged): any new wave campaign on the n=4 complex
   (the W23 exhaustion certificate stands); δ₂(ququart)/δ₃(qutrit) attacks;
   the mod-2 secondary operations / CLSS d₃ at n=4 frontier list.

**Nothing in this note touches the mathematics: H₂(B₃) = ℤ/3,
δ₂(D(ℂ³)) = 4/3, and the ququart bracket [4/3, 3/2] stand exactly as
committed; the v7 manuscripts are unchanged.**
