# WAVE 8 (c) — Homology-side Cartan–Leray analysis of the two flagged bits

**Status: NO claim on either bit. Both remain open. Manuscripts untouched.**

Companion to `WAVE8_CLSS_VERIFICATION.md` (Wave 8b, commit 75b51e4).
Script: `../scripts/wave8c_homology_side.py` (exact integer linear algebra:
Smith normal form / lattice quotients; full transcript `wave8c_output.txt`).

## What was added

Wave 8b machine-verified the COHOMOLOGICAL E2 pages of the Cartan–Leray
spectral sequences of `B_d = Fl_d/C_d` (cyclic frame shift). Wave 8c adds
the HOMOLOGY side `E2_{p,q} = H_p(C_d; H_q(Fl_d))` — which Wave 8b did not
compute — plus the Poincaré-duality / UCT gluing of the two sides.

### A. Engine validated on the lens space
`H_*(L(3,1))` recovered from the homology CLSS of the free C₃-action on S³:
the forced `d4` iso staircase `(5,0)->(1,3), (7,0)->(3,3), ...` and the
graded assembly of `H_3 = Z` (torsion graded pieces of a FREE group need not
die — the reason `|H_k| = prod |E_inf|` is valid only for finite `H_k`).
The classical Euler-class transgression `d4: E^{0,3} -> E^{4,0}` (reduction
mod 3) is confirmed as the UCT-shift mirror of the homological `d4`.

### B. Qutrit (d=3): two new machine-derived structural results
Modules: `H_q(Fl3)`: q=0,6: Z (trivial; B₃ orientable), q=2,4: the
augmentation ideal iota (2-dim); parity mirror verified:
`H_p(C3;iota) = Z/3` on p=0 and even p≥2, 0 on odd p.

The low-degree homology differentials
`A = d3: (3,0)->(0,2)`, `B' = d3: (5,0)->(2,2)`, `C' = d5: (5,0)->(0,4)`
(each Z/3 → Z/3, hence 0 or iso) are constrained by:

* **(PD1)** `|H_4(B_3)| = |H^2(B_3)| = 3` (theorem H² = Z/3);
* **(PD2)** `H_5(B_3) = 0` (PD against H¹ = 0).

World enumeration over (A, B', C') ∈ {0, iso}³ machine-yields:

* **(R1) Anti-correlation:** `B' = iso ⟺ C'(effective) = 0`, and
  `B' = 0 ⟺ C' = iso`. The map C' (homology d5: E⁵_{5,0} → E⁵_{0,4}) is
  *invisible on the cohomological page* — this coupling is new information
  that Wave 8b could not see.
* **(R2)** The UCT glue (`H^4 = Ext(H_3)`) ties the cohomological BIT
  (`d3: E3^{1,2} -> E3^{4,0}`) to the homology map A:
  bit = 0 ⟺ A = 0 (H₂ = H₃ = Z/3, H⁴ = Z/3); bit = iso ⟺ A = iso.

Nothing in E₂-algebra + PD + UCT decides A. **The qutrit bit stays open.**
(The earlier hand-flaw — treating `|H_k| = prod |E_inf|` as valid for free
groups, producing a spurious "contradiction" — is exactly the trap the lens
validation exposes; recorded so it is not repeated.)

### C. Ququart (d=4): the twisted homology mirror located
The orientation-twisted homology page
`E2_{p,q} = H_p(C4; H_q(Fl_4) tensor Z~)` was computed from the coinvariant
ring (descent basis, exact reductions; degree-4 module built explicitly —
it is NOT the degree-2 module: trace(σ) = 1 vs 0). Total-degree-9 entries:

| entry | group |
|---|---|
| (9,0) = H₉(C4; Z~) | 0 |
| (7,2) = H₇(C4; H₂⊗Z~) | Z/2 |
| (5,4) = H₅(C4; H₄⊗Z~) | Z/4 |
| (3,6) = H₃(C4; H₆⊗Z~) | Z/2 |
| (1,8) = H₁(C4; H₈⊗Z~) | 0 |

All finite ⟹ `|H_9(B_4;Z~)| = prod |E_inf|` is a valid product constraint,
and twisted PD pins it to the ququart bit: `|H_9| = |H^3(B_4;Z~)|` = 2 (bit
zero) or 1 (bit surjective). The raw product 2·4·2·1 = 16 must be cut to 2
or 1 by the incoming homology d3's from total ≥ 12 — the same
anti-correlation structure as the qutrit's B′ XOR C′, in a richer (Z/4)
lattice. **The ququart bit stays open.**

### D. Negative result recorded (saves a future detour)
The tempting formula `d3^{1,2} = <alpha ∪ k_2>` (CLSS d3 as the cup-pairing
with the 2-Postnikov k-invariant of the action-fibration) is REFUTED by the
conjugation test cases `B(O(2))` (split S¹⋊C₂, k₂ = 0) vs `B(H')`
(non-split, k₂ = Bockstein(extension class) ≠ 0): in both cases UCT forces
`H_2 = Z/2` (coinvariants of the fiber), hence `H^3 = Ext(H_2) = Z/2`
survives from `E3^{1,2}`, so the d3 is ZERO in both — k₂ differs, d3 does
not. **No Postnikov-2-type shortcut exists; the honest route remains the
C_d-equivariant chain model of Fl_d** (c-invariant CW structure from
stratification, or an equivariant Morse complex on B_d = U(d)/(T⋊C_d)).

## Scoreboard (unchanged)
- δ₂(qutrit) = 4/3 ⟺ H⁴(B₃) = Z/3 ⟺ bit-zero — OPEN (numerics favor it).
- δ₁(ququart) = 3/2 ⟺ H³(B₄;Z~) = Z/2 ⟺ bit-zero — OPEN (numerics favor it).
- Everything machine-checkable short of the chain model is now verified on
  BOTH spectral-sequence sides.
