#!/usr/bin/env python3
"""WAVE 31 (v11): the R1 repair of Proposition prop:cupsquare, per the wave-30
referee read (Finding R1, the six-part mechanical repair, parts 1-4; part 5 =
the lattice-index gate G3L in w31_derivation_check.py; part 6 = the
supersession note in WAVE31_CORRECTION_V1.md / glm/README.md).

The repair corrects the integral module statement of Step 2 (the true free
part is the orbit-sum invariant lattice; the symmetric-function module is a
finite-index sublattice, index 1 for d <= 2 and 2,2,4,8 in degrees 3-6), the
H^6(BK) display of Step 3 (orbit-sum basis {A1, S1, S2, sigma_3}), the
degree-6 conclusion of Step 7 (H^6(B;Z) = Z.<[S1]>, the discriminant TWICE a
generator), the Proposition statement's top-class clause, and the
rem:machine-certificate residuals list (the strengthened gate now certifies
the lattice layer).

The main article needs NO change (the referee's integration assessment; the
sync clauses reference the flag-quotient computation, not the top-class
generator), so v11 contains the instruments paper only.

Anchored replacements, each asserted to match exactly once."""

import os
import sys

SRC = ("/home/z/my-project/channel-supp-augmented/manuscript uploads v10/"
       "instruments-paper-revised10.txt")
OUT = ("/home/z/my-project/channel-supp-augmented/manuscript uploads v11/"
       "instruments-paper-revised11.txt")
OUTTEX = OUT[:-4] + ".tex"

src = open(SRC).read()

edits = []

# ------------------------------------------------------------- Hunk 1 (R1.4)
# The Proposition statement: replace the false top-class clause.
edits.append(("statement-topclass",
"""with $x$ generating $H^2$, $x^2$ generating $H^4$, and a discriminant class
generating $H^6$.
""",
"""with $x$ generating $H^2$, $x^2$ generating $H^4$, and
$H^6(B;\\mathbb Z)\\cong\\mathbb Z$, in which the discriminant class is twice a
generator.
"""))

# ------------------------------------------------------------- Hunk 2 (R1.1)
# Step 2: the integral module equality -> the orbit-sum lattice statement,
# the module over Q, and the finite-index note with the degree-3 witness.
edits.append(("step2-module",
"""and the sequence collapses. The
free part is
\\[
H^*(BK;\\mathbb Z)_{\\mathrm{free}}\\ =\\ \\mathbb Z[\\sigma_1,\\sigma_2,\\sigma_3]\\
\\oplus\\ \\Delta\\cdot\\mathbb Z[\\sigma_1,\\sigma_2,\\sigma_3],
\\]
where $\\sigma_i=\\sigma_i(\\chi)$ are the elementary symmetric functions and
$\\Delta=\\prod_{i<j}(\\chi_i-\\chi_j)$ is the discriminant, invariant under the
cyclic group, with $\\Delta^2$ equal to the classical discriminant polynomial
in the $\\sigma_i$; the module statement follows because in each degree $d$
the orbit sums span the invariant lattice, of rank equal to the number of
orbits, which the monomial count of the displayed module reproduces. The
""",
"""and the sequence collapses. The
free part, integrally, is the invariant lattice: in each degree $d$ it is
spanned by the $C_3$-orbit sums of the degree-$d$ monomials --- the fixed
monomials $(\\chi_1\\chi_2\\chi_3)^a$ being orbits of size one --- of rank
equal to the number of orbits; the span is the whole invariant lattice,
because the monomials of an invariant polynomial occur with equal
coefficients on each orbit. Rationally, this lattice is the degree-$d$ part
of
\\[
\\mathbb Q[\\sigma_1,\\sigma_2,\\sigma_3]\\ \\oplus\\ \\Delta\\cdot
\\mathbb Q[\\sigma_1,\\sigma_2,\\sigma_3],
\\]
where $\\sigma_i=\\sigma_i(\\chi)$ are the elementary symmetric functions and
$\\Delta=\\prod_{i<j}(\\chi_i-\\chi_j)$ is the discriminant, invariant under the
cyclic group, with $\\Delta^2$ equal to the classical discriminant polynomial
in the $\\sigma_i$; the orbit counts match the monomial counts of the
displayed module, so the two rational vector spaces coincide. Integrally the
module is only a sublattice of the invariant lattice, of finite index ---
one in degrees $d\\le2$, exactly the degrees in which the crux of Step~5
below works, then $2$, $2$, $4$, $8$ in degrees $3$ to $6$ --- and already in
degree three the orbit sum
$S_1=\\chi_1^2\\chi_2+\\chi_2^2\\chi_3+\\chi_3^2\\chi_1
=\\tfrac12(\\sigma_1\\sigma_2-3\\sigma_3+\\Delta)$ is invariant but lies in the
module only after doubling. The
"""))

# ------------------------------------------------------------- Hunk 3 (R1.2)
# Step 3: the H^6(BK) display -- orbit-sum basis instead of the module one.
edits.append(("step3-h6-display",
"""so $\\tau^2$ is a class of order $3$ in
\\[
H^4(BK;\\mathbb Z)\\ \\cong\\ \\mathbb Z\\sigma_1^2\\ \\oplus\\ \\mathbb Z\\sigma_2\\
\\oplus\\ \\mathbb Z/3\\cdot\\tau^2,
\\qquad
H^6(BK;\\mathbb Z)\\ \\cong\\ \\mathbb Z\\{\\sigma_1^3,\\sigma_1\\sigma_2,\\sigma_3,
\\Delta\\}\\oplus\\mathbb Z/3\\cdot\\tau^3,
\\]
and $H^{\\mathrm{odd}}(BK;\\mathbb Z)=0$.
""",
"""so $\\tau^2$ is a class of order $3$ in
\\[
H^4(BK;\\mathbb Z)\\ \\cong\\ \\mathbb Z\\sigma_1^2\\ \\oplus\\ \\mathbb Z\\sigma_2\\
\\oplus\\ \\mathbb Z/3\\cdot\\tau^2,
\\qquad
H^6(BK;\\mathbb Z)\\ \\cong\\ \\mathbb Z\\{A_1,\\,S_1,\\,S_2,\\,\\sigma_3\\}\\oplus
\\mathbb Z/3\\cdot\\tau^3,
\\]
where $A_1=\\chi_1^3+\\chi_2^3+\\chi_3^3$ and
$S_2=\\chi_1^2\\chi_3+\\chi_2^2\\chi_1+\\chi_3^2\\chi_2$, with $S_1$ as in
Step~2; the two orbit sums satisfy $S_1+S_2=\\sigma_1\\sigma_2-3\\sigma_3$ and
$S_1-S_2=\\Delta$, and the symmetric-function module of Step~2 spans an
index-two sublattice of this free part, the four orbit sums generating it
exactly. The odd cohomology $H^{\\mathrm{odd}}(BK;\\mathbb Z)$ vanishes, as the
collapse argument shows.
"""))

# ------------------------------------------------------------- Hunk 4 (R1.3)
# Step 7: run the degree-6 quotient on the orbit-sum lattice; the generator
# is S1 and the discriminant is TWICE a generator.
edits.append(("step7-degree6",
"""Total degree six: the incoming images into $(6,0)$ are
$\\sigma_1\\sigma_2$ and $\\sigma_1^3$ (from $d_2$), $2\\tau^3$ (from $d_4$),
and $\\sigma_3$ (from $d_6$), so
\\[
H^6(B;\\mathbb Z)\\ \\cong\\ \\bigl(\\mathbb Z\\{\\sigma_1^3,\\sigma_1\\sigma_2,
\\sigma_3,\\Delta\\}\\oplus\\mathbb Z/3\\cdot\\tau^3\\bigr)\\big/\\langle\\sigma_1^3,\\
\\sigma_1\\sigma_2,\\ 2\\tau^3,\\ \\sigma_3\\rangle\\ \\cong\\ \\mathbb Z\\cdot
\\langle\\Delta\\rangle,
\\]
the top class being the discriminant, consistently with the rational
cohomology $H^*(B;\\mathbb Q)=\\mathbb Q\\oplus\\mathbb Q\\cdot\\bar\\Delta$ read
off from the invariant theory of Step 2.""",
"""Total degree six: the incoming images into $(6,0)$ are
$\\sigma_1\\sigma_2$ and $\\sigma_1^3$ (from $d_2$), $2\\tau^3$ (from $d_4$),
and $\\sigma_3$ (from $d_6$), so, running the quotient on the orbit-sum
lattice of Step~3,
\\[
H^6(B;\\mathbb Z)\\ \\cong\\ \\bigl(\\mathbb Z\\{A_1,S_1,S_2,\\sigma_3\\}\\oplus
\\mathbb Z/3\\cdot\\tau^3\\bigr)\\big/\\langle\\sigma_1^3,\\ \\sigma_1\\sigma_2,\\
2\\tau^3,\\ \\sigma_3\\rangle\\ \\cong\\ \\mathbb Z\\cdot\\langle S_1\\rangle,
\\]
using $\\sigma_1\\sigma_2=S_1+S_2+3\\sigma_3$ and
$\\sigma_1^3=A_1+3(S_1+S_2)+6\\sigma_3$: the relations kill $\\sigma_3$, then
$S_1+S_2$, then $A_1$ (each substituting into the next), the torsion class
$\\tau^3$ dies because $2\\tau^3=0$ forces it (two is invertible modulo
three), and the top class is the orbit sum $S_1$, in which the discriminant
$\\Delta=S_1-S_2=2S_1$ is twice a generator --- consistently with the
rational cohomology $H^*(B;\\mathbb Q)=\\mathbb Q\\oplus\\mathbb Q\\cdot
\\bar\\Delta$, read off from the invariant theory of Step~2, where two is
invertible and the discriminant class does generate."""))

# ------------------------------------------------------------- Hunk 5 (R1 knock-on)
# rem:machine-certificate: the residuals list now names the lattice layer
# that the strengthened gate (G3L) certifies.
edits.append(("remark-residuals",
"""arithmetic (the orbit counts, the invariant lattice, the torsion product
rule, the Chern classes of the regular representation, and the
Leibniz-signed page bookkeeping, including the $D^2=0$ coherence check) has
been verified by an exact-integer script whose transcript is part of the
companion repository;""",
"""arithmetic (the orbit counts, the orbit-sum invariant lattice together with
its finite index over the symmetric-function module, the twice-a-generator
position of the discriminant in the top class, the torsion product rule, the
Chern classes of the regular representation, and the Leibniz-signed page
bookkeeping, including the $D^2=0$ coherence check) has been verified by an
exact-integer script whose transcript is part of the companion repository;"""))

n_ok = 0
for (name, old, new) in edits:
    c = src.count(old)
    if c != 1:
        print(f"ANCHOR FAIL [{name}]: found {c} occurrences (expected 1)")
        sys.exit(1)
    src = src.replace(old, new)
    n_ok += 1
    print(f"  ok [{name}]")

os.makedirs(os.path.dirname(OUT), exist_ok=True)
open(OUT, "w").write(src)
open(OUTTEX, "w").write(src)
print(f"instruments v11 written with {n_ok} hunks "
      f"({len(src.splitlines())} lines); .txt and .tex written")
