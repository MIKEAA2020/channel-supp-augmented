#!/usr/bin/env python3
"""WAVE 32 (v12): the six one-line R2-R7 repairs of the Wave-30 referee
read, applied to the v11 instruments paper -- EACH ONLY AFTER THE MERIT
ADJUDICATION PASSED (w32_r2r7_check.py, all 12 gates):

  R2 (Step 1)  the garbled d_r-vanishing parenthetical ("H^{odd}(U(3)) = 0"
               -- FALSE, z_1, z_3, z_5 are odd-degree) replaced by the
               correct two-step justification.  NOTE: the referee's own
               sketch ("d4(beta z3 z5) != 0 for every beta") is itself
               imprecise: the sigma_1-multiple coefficients in degree eight
               are d2-BOUNDARIES (via z1 z3 z5), not d4-victims; the applied
               repair states the corrected version (verified: R2C, R2D, R2E
               -- including the sigma_1-divisibility lattice fact, degrees
               1-8, which closes the general-beta case).
  R3 (Step 5)  the silent (2,2)-slot: added the vanishing clause (the
               exterior algebra has no degree-2 class; gate R2A/R3).
  R4 (Step 4)  the c_1-uniqueness parenthetical replaced by the honest
               statement iota*c_1 = sigma_1 + b tau with the b-pin added to
               the splitting argument (0 = s*(iota*c_1) = bu, s*tau = u).
               LOAD-BEARING: unpinned, d_2(tau z_1) = b tau^2 would enter
               the (4,0)-slot and E_inf^{4,0} would be 0 -- the crux would
               die (gate R4B, the counterfactual computed exactly).
  R5 (Step 5)  the crux's per-subgroup phrasing replaced by the explicit
               two-step quotient (split off the direct summand Z sigma_1^2
               first, then the single relation; the sum-quotient verified:
               gate R5, with the (2,2)-witness that separate non-membership
               does not imply sum non-membership).
  R6 (Step 6)  the convention remark: the identification passes through the
               inversion K\\U(3) = U(3)/K, so a different deck convention
               could at worst flip a sign, and the sign squares away in
               x^2 = gamma*(tau^2) (gate R6).
  R7 (Step 3)  tau.Delta marked lift-dependent (the class of Delta is fixed
               only up to a tau^3-tail; tau.(Delta + c tau^3) = c tau^4),
               with the sigma_i-instances noted unconditional (pinned pure
               by Step 4); the claim is unused downstream (gate R7B).

The main article needs NO change (all six sites are internal to the proof
of Proposition 6.16 in the instruments paper; the main-article sync
clauses do not reference the proof internals).  v12 = the instruments
paper only; the main article stays at v10.

Anchored replacements, each asserted to match exactly once."""

import os
import sys

SRC = ("/home/z/my-project/channel-supp-augmented/manuscript uploads v11/"
       "instruments-paper-revised11.txt")
OUTDIR = ("/home/z/my-project/channel-supp-augmented/manuscript uploads v12")
OUT = OUTDIR + "/instruments-paper-revised12.txt"
OUTTEX = OUT[:-4] + ".tex"

src = open(SRC).read()

edits = []

# ------------------------------------------------------------- Hunk 1 (R2)
edits.append(("step1-dr-vanishing",
"""and $d_r=0$ for $r\\notin\\{2,4,6\\}$ by bidegree ($r$ even forces an odd
$q$-degree in the target, where $H^{\\mathrm{odd}}(U(3))=0$).
""",
"""and $d_r=0$ for $r\\notin\\{2,4,6\\}$: for odd $r$ the target sits in odd
$p$-degree, where $H^{\\mathrm{odd}}(BK;\\mathbb Z)=0$ by Step~3 below; for
even $r\\ge8$ the source fibre-degree is $8$ or $9$, and the fibre classes
there are boundaries before the $E_8$-page. In fibre degree nine,
$d_2(\\beta z_1z_3z_5)=\\beta\\sigma_1z_3z_5$ kills every class whose
coefficient survives multiplication by $\\sigma_1$, and
$d_4(\\tau z_1z_3z_5)=2\\tau^3z_1z_5\\ne0$ kills the torsion coefficients,
which annihilate $\\sigma_1$. In fibre degree eight the $\\sigma_1$-multiple
coefficients are $d_2$-boundaries, and the rest die under
$d_4(\\beta z_3z_5)=\\beta(\\sigma_2+2\\tau^2)z_5\\ne0$: a class $\\beta$ whose
$\\beta\\sigma_2$ is a $\\sigma_1$-multiple is itself a $\\sigma_1$-multiple,
rationally in the invariant module and then integrally (divisibility by
$\\sigma_1=\\chi_1+\\chi_2+\\chi_3$ is triangular in the monomials), hence a
$d_2$-boundary.
"""))

# ------------------------------------------------------------- Hunk 2 (R7)
edits.append(("step3-tau-delta",
"""and $\\tau\\cdot f=0$ when $3\\nmid d$. In particular $\\tau\\sigma_1=
\\tau\\sigma_2=0$ (degree not divisible by $3$), $\\tau\\Delta=0$ (the
alternating polynomial $\\Delta$ contains no monomial
$\\chi_1\\chi_2\\chi_3$), and $\\tau\\sigma_1^3=0$ (the coefficient of
$\\chi_1\\chi_2\\chi_3$ in $\\sigma_1^3$ is $6$), while $\\tau\\sigma_3$ is the
generator of the $(2,6)$-slot. Also $\\tau^k\\cdot\\tau^{k'}=\\tau^{k+k'}\\ne0$;
""",
"""and $\\tau\\cdot f=0$ when $3\\nmid d$. In particular $\\tau\\sigma_1=
\\tau\\sigma_2=0$ (degree not divisible by $3$) and
$\\tau\\sigma_1^3=0$ (the coefficient of
$\\chi_1\\chi_2\\chi_3$ in $\\sigma_1^3$ is $6$), while $\\tau\\sigma_3$ is the
generator of the $(2,6)$-slot --- these instances unconditional, the
$\\sigma_i$ being the pinned pure classes of Step~4 below. The instance
$\\tau\\Delta=0$ (the graded class of the alternating $\\Delta$ contains no
monomial $\\chi_1\\chi_2\\chi_3$) is lift-dependent: the class of $\\Delta$ in
$H^6(BK;\\mathbb Z)$ is fixed only up to a $\\tau^3$-tail, and
$\\tau\\cdot(\\Delta+c\\,\\tau^3)=c\\,\\tau^4\\ne0$ when $c\\ne0$; it is not used
below. Also $\\tau^k\\cdot\\tau^{k'}=\\tau^{k+k'}\\ne0$;
"""))

# ------------------------------------------------------------ Hunk 3 (R4a)
edits.append(("step4-c1-display",
"""$\\iota^*c_1=\\sigma_1$ (the free generator is the unique class restricting
to $\\sigma_1(\\chi)$, since the torsion restricts to zero and the $(0,2)$-slot
is $\\mathbb Z\\sigma_1$), $\\iota^*c_2=\\sigma_2+\\varepsilon\\tau^2$
and $\\iota^*c_3=\\sigma_3+\\varepsilon'\\tau^3$ with
$\\varepsilon,\\varepsilon'\\in\\mathbb Z/3$. The constants are pinned by the
""",
"""$\\iota^*c_1=\\sigma_1+b\\,\\tau$, $\\iota^*c_2=\\sigma_2+\\varepsilon\\tau^2$
and $\\iota^*c_3=\\sigma_3+\\varepsilon'\\tau^3$ with
$b,\\varepsilon,\\varepsilon'\\in\\mathbb Z/3$ (the restriction to the fibre
pins only the free components: the torsion restricts to zero, and the
$(0,2)$-slot is $\\mathbb Z\\sigma_1$). The constants are pinned by the
"""))

# ------------------------------------------------------------ Hunk 4 (R4b)
edits.append(("step4-b-pin",
"""$s^*(\\tau^3)=u^3$. Hence $2u^2=s^*(\\iota^*c_2)=\\varepsilon u^2$ and
$0=\\varepsilon'u^3$, so
""",
"""$s^*(\\tau^3)=u^3$. Hence $0=s^*(\\iota^*c_1)=s^*(\\sigma_1+b\\,\\tau)=bu$
(as $s^*\\sigma_1=0$, the class $\\sigma_1$ having positive fibre degree,
and $s^*\\tau=u$, $s$ being a section of the projection whose pullback
class $\\tau$ is), so $b=0$; and $2u^2=s^*(\\iota^*c_2)=\\varepsilon u^2$
and $0=\\varepsilon'u^3$, so
"""))

# --------------------------------------------------------- Hunk 5 (R3+R5)
edits.append(("step5-terms-and-crux",
"""differential. In total degree four the terms are
$E_2^{4,0}=\\mathbb Z\\sigma_1^2\\oplus\\mathbb Z\\sigma_2\\oplus\\mathbb
Z/3\\cdot\\tau^2$, $E_2^{3,1}=E_2^{1,3}=0$ (odd cohomology of $BK$), and
$E_2^{0,4}=\\mathbb Z\\cdot z_1z_3$. The incoming images into the $(4,0)$
slot are $d_2(\\sigma_1z_1)=\\sigma_1^2$ and $d_4(z_3)=\\sigma_2+2\\tau^2$,
while $d_2(z_1z_3)=\\sigma_1z_3\\ne0$ kills the $z_1z_3$ class. The class
$\\tau^2$ has order three; both $\\sigma_1^2$ and $\\sigma_2+2\\tau^2$ generate
infinite cyclic subgroups --- the latter because its free component
$\\sigma_2$ is nonzero --- and a finite-order element never lies in a
subgroup generated by an infinite-order element. Consequently the class of
$\\tau^2$ is nonzero in
""",
"""differential. In total degree four the terms are
$E_2^{4,0}=\\mathbb Z\\sigma_1^2\\oplus\\mathbb Z\\sigma_2\\oplus\\mathbb
Z/3\\cdot\\tau^2$, $E_2^{3,1}=E_2^{1,3}=0$ (odd cohomology of $BK$),
$E_2^{2,2}=0$ (the exterior algebra $\\Lambda(z_1,z_3,z_5)$ has no class of
degree two), and $E_2^{0,4}=\\mathbb Z\\cdot z_1z_3$. The incoming images into the $(4,0)$
slot are $d_2(\\sigma_1z_1)=\\sigma_1^2$ and $d_4(z_3)=\\sigma_2+2\\tau^2$,
while $d_2(z_1z_3)=\\sigma_1z_3\\ne0$ kills the $z_1z_3$ class. The class
$\\tau^2$ has order three. Quotient out the direct summand
$\\mathbb Z\\sigma_1^2$ first --- a quotient by a direct summand leaves both
the class of $\\tau^2$ and the complementary summand unchanged --- after
which the $(4,0)$-term is $\\mathbb Z\\sigma_2\\oplus\\mathbb Z/3\\cdot\\tau^2$
with the single incoming relation $\\sigma_2+2\\tau^2$, a class of infinite
order (its free component $\\sigma_2$ is nonzero); an element of order
three never lies in the subgroup generated by an infinite-order class.
Consequently the class of
$\\tau^2$ is nonzero in
"""))

# ------------------------------------------------------------- Hunk 6 (R6)
edits.append(("step6-convention",
"""$U(3)\\to U(3)/K=B$. The intermediate cover""",
"""$U(3)\\to U(3)/K=B$ (the identification passes through the inversion
$K\\backslash U(3)\\cong U(3)/K$, so a different deck convention could at
worst flip a sign, $x=\\pm\\gamma^*(\\tau)$; nothing below depends on the
choice, the sign squaring away in $x^2=\\gamma^*(\\tau^2)$). The intermediate
cover"""))

# ---------------------------------------------------------------- apply
os.makedirs(OUTDIR, exist_ok=True)
out = src
for name, old, new in edits:
    n = out.count(old)
    assert n == 1, f"hunk {name!r}: {n} matches (expected exactly 1)"
    out = out.replace(old, new)

with open(OUT, "w") as f:
    f.write(out)
with open(OUTTEX, "w") as f:
    f.write(out)

nl_old, nl_new = src.count("\n"), out.count("\n")
print(f"v12 written: {OUT}")
print(f"             {OUTTEX}")
print(f"hunks applied: {len(edits)} (R2, R7, R4a, R4b, R3+R5, R6)")
print(f"net line delta: {nl_new - nl_old:+d}")
print(f"bytes: {len(src)} -> {len(out)}")
assert out != src
# the superseded v11 statements must be GONE:
for gone in [
    "by bidegree ($r$ even forces an odd",
    "where $H^{\\mathrm{odd}}(U(3))=0$",
    "the free generator is the unique class restricting",
    "both $\\sigma_1^2$ and $\\sigma_2+2\\tau^2$ generate",
    "alternating polynomial $\\Delta$ contains no monomial",
]:
    assert gone not in out, f"superseded v11 statement still present: {gone!r}"
print("all superseded v11 statements removed: OK")
