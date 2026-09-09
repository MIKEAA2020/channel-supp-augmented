# WAVE 11 — THE HONEST 1896-CELL RUN: EXECUTED, AND THE RECORDED SPEC IS REFUTED

**Task.** Execute the recorded decisive computation (Wave 10 audit Sections 3+5, worklog
Task 14): build the honest C₃-equivariant 1896-cell chain model of Fl₃ = U(3)/T³, certify
it against the full verification battery, then read the qutrit bit
δ₂(D(ℂ³)) = 4/3 off the orbit-complex Smith normal form of B₃ = Fl₃/⟨c⟩.

**Machine artifacts.** `glm/wave11_honest_fl3.py` (908 lines, all exact arithmetic —
Python ints, `Fraction`s, sympy integer SNF toolkit, numpy mod-p linear algebra),
transcript `glm/wave11_honest_output.txt`. Manuscripts untouched.

---

## 1. What was built and what passed

The full recorded spec was implemented faithfully: the 49-face Birkhoff base with
geometric interior-boundary signs ε_Φ (exact `Fraction` determinants, σ-consistency
ε_{Φσ} = ε_Φ·s(Φ) verified), level-3 fiber cellulations (S¹: 3+3; T²: 9+27+18 = 54
cells with the three circle families {u=a}, {v=b}, {u+v=c} at thirds), the c-action
(base permutation π ↦ σ⁻¹∘π with sorted-vertex shuffle signs s(F), s(interior) = +1
verified by the exact det of the σ-map on the affine 4-space; interior fiber
translation +t₀, t₀ = (1/3,1/3) in (u,v) = (arg z₂/z₁, arg z₃/z₂) coords — consistent
with the exact identity F₀P_σ = diag(1,ω,ω²)F₀), and the transition layer
τ_{F→G} = q_G((p(F)−p(G))·t₀) (the unique c-equivariant cocycle representative, since
H¹ of the face poset with the torus sheaf vanishes and the t₀-monodromy is the only
twist).

**Chain-level battery — every item PASSES:**

| Check | Result |
|---|---|
| cell counts | 1896 = (6, 81, 351, 675, 576, 189, 18), χ = 6 |
| d² = 0 | exact, all degrees |
| T³ = I | exact, sign product +1 on every cell |
| c free on cells | no fixed cell among the 1896 |
| degree preservation | exact |
| **dT = Td** | exact (the hard one: the τ/t₀ layer is c-consistent) |
| degeneration degrees | the ±1 q-map table (derived from the (u,v)-geometry) consistent with d²=0 |

This certifies the *machinery*: the equivariant-cellulation framework, the t₀-twist
layer, the level-3 structure, the boundary-operator assembly — all of it is sound and
reusable.

## 2. The failure that settles this wave

**H·(built complex; ℚ) = (ℤ, 0, ℤ², ℤ, ℤ⁴, 0, 0) ≠ (ℤ, 0, ℤ², 0, ℤ², 0, ℤ) = H·(Fl₃;ℚ).**

In particular H₆ = 0, impossible for the closed, connected, orientable 6-manifold Fl₃
(H₆ = ℤ). Torsion audit (exact mod-p UCT induction, p ∈ {2,3,5,7,11,13}): no torsion
anywhere — so the defect is not torsion, it is the space itself. The built complex is
a genuine C₃-equivariant chain complex — of the wrong space. The orbit-complex SNF was
therefore **skipped** (it would compute H·(the wrong quotient), a fabricated answer in
exactly the style Waves 9–10 refuted).

## 3. Root cause (machine-checked, Part IV-bis of the script)

The recorded base — the Birkhoff face lattice with T³/Stab-fibers over all 34
one-block faces — is **unistochastically infeasible** on 33 of those 34:

* D ∈ Bo₃ is unistochastic (lies in the image of π: Fl₃ → Bo₃) iff for every row pair
  (a,b) the magnitudes mₖ = √(D_{ak}D_{bk}) satisfy the triangle inequalities — the
  exact solvability condition of the pair's orthogonality constraint
  Σₖ mₖe^{iαₖ} = 0 (checked in exact `Fraction` arithmetic).
* **Six-cycle edges** conv(P, P_σ): each row pair shares exactly one nonzero column;
  the constraint reads √(t(1−t))·e^{iφ} = 0 with t ∈ (0,1) — impossible at *every*
  interior point (machine: infeasible at t = 1/3, 2/5 on all 6). The spec's "T² fibers
  over the 6 six-cycle edges" are **empty**.
* **All 18 triangles**: a row pair sharing exactly one nonzero column, m > 0 —
  impossible (machine: infeasible at all 18 barycenters). Fibers empty.
* **The 9 facets**: the row pair adjacent to the zero entry shares two columns;
  feasibility forces the equality D_{a'k'}D_{bk'} = D_{a''k''}D_{bk''} — a codim-1
  equality *locus* (which is why the symmetric barycenter tests feasible). The open
  3-dim facet relint carries no fiber.
* Nonempty fibers over the Birkhoff base exist only over: the interior 4-cell (T²),
  the 9 sphere-edges E_{ak} (S¹), the 6 vertices (pt), and the 2-dim facet equality
  loci (T²).

The image of π is the **unistochastic region U₃ ⊊ Bo₃**, whose boundary consists of
the 9 curved fold-walls {m_i = m_j + m_k} (row-pair triangle degenerations, T²-fibers,
fold type — the total space stays smooth across them), meeting the Birkhoff boundary
along the 2-dim facet equality loci, the sphere-edges (where the fiber drops to S¹)
and the vertices. The Birkhoff face lattice is *not* the stratification of the base
of the fibration.

**Where the spec came from.** Waves 9–10 machine-confirmed the face lattice and
HALL (doubly stochastic) feasibility — the unistochastic (triangle-inequality) side
was never checked; that gap propagated into the recorded "design skeleton" that Wave
10's audit had CONFIRMED. This wave corrects Wave 10's own confirmation: the skeleton
is combinatorially right and geometrically wrong.

## 4. Verdict

* The recorded 1896-cell spec (Wave 10 audit Sections 3+5, worklog Task 14) is
  **REFUTED** by its own verification battery — precisely the failure mode the
  battery exists to catch.
* δ₂(qutrit) = 4/3 remains **OPEN**. No boxed value is issued; the numerics of
  Waves 7–8 still point to the d₃ = 0 world, but nothing is settled.
* Wave 10's claim-level correction: the audit of `deepseek response_quantum2.txt`
  correctly refuted the document's *outputs* and the *c-action triviality* claim, and
  correctly recorded the level-3/t₀ machinery as "the honest remaining route" — but
  its "design skeleton CONFIRMED" verdict overstated: the base stratification was
  never feasible.

## 5. The honest decisive route (recorded for the next session)

Same machinery, corrected base:

1. Cellulate the **unistochastic region Ū₃** — the 4-cell int(U₃), the 9 fold-wall
   3-cells W_{(ab),i} = {m^{(ab)}_i = m^{(ab)}_j + m^{(ab)}_k} (S₃×S₃-symmetric,
   semialgebraic, T²-fibers), their continuations to the 2-dim facet equality loci
   (T²-fibers), the 9 sphere-edges (S¹), the 6 vertices. The open problem of that
   build is the wall arrangement's incidence structure (which wall-piece bounds
   which, with what degree) — the walls are genuinely curved, so the corner analysis
   is new work; the ±1-degree and fold-type structure must be derived, not assumed.
2. Keep: the level-3 fiber cellulations, the (u,v)-coordinates, the t₀-twist layer
   τ_{F→G} = q_G((p(F)−p(G))t₀), the geometric orientation machinery, the full
   battery (d²=0, H(Fl₃) = (ℤ,0,ℤ²,0,ℤ²,0,ℤ) with the mod-p torsion audit, T³=I,
   dT=Td, freeness, N=0 on H₂, T=+1 on H₆).
3. Then the orbit-complex SNF (coinvariants under the free cellular C₃-action) gives
   H·(B₃) and settles the qutrit bit in either direction. Fl₄/ququart remains
   honestly deferred (~10⁵ cells at the corrected base).
