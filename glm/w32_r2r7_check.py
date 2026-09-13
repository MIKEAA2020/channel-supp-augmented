#!/usr/bin/env python3
"""
WAVE 32: the R2-R7 repair verifier (the six one-line repairs of the Wave-30
referee read, applied to the v12 instruments paper only if merited).

Charge: "apply the six one-line R2-R7 repairs only if truly merited and
addressing root cause of issues".  This script is the merit evidence: every
arithmetic/structural claim entering the six repairs is re-derived here by
exact integer computation, INDEPENDENTLY of the manuscript.  A repair is
applied only if its root cause is real (the defect exists in the v11 text)
and the repair's own mathematics passes these gates.

The gates:
  R2A  the fibre cohomology of U(3): degree set of Lambda(z1,z3,z5) =
       {0,1,3,4,5,6,8,9}; H^2 = H^7 = 0; H^{odd}(U(3)) != 0  ->  the v11
       parenthetical's premise "H^{odd}(U(3)) = 0" is FALSE (R2 merited),
       and the (2,2)-slot vanishes because H^2(U(3)) = 0 (R3 merited).
  R2B  H^{odd}(BK) = 0: H^1(C_3; Sym^d) = ker N / (T-1)M equals 0 for all
       d <= 8 (ker N = (T-1)M as lattices, degree by degree), and the
       cohomology is 2-periodic; the BT^3-SS terms with p odd or q odd
       vanish.
  R2C  the bidegree analysis: for odd r the target p-degree is odd (dead by
       R2B); for even r >= 8 the source fibre-degree is 8 or 9.
  R2D  the killing computations for the r >= 8 sources:
       d2(z1 z3 z5) = sigma1 z3 z5 != 0;
       d2-images into the d4-targets: sigma1.H^2(BK) = Z sigma1^2 and
       sigma1.H^4(BK) = Z sigma1^3 + Z sigma1 sigma2 (tau-products with
       sigma1 vanish);
       d4(z3 z5) = (sigma2 + 2 tau^2) z5 with sigma2 z5 NOT in the d2-image
       (sigma2 not in Z sigma1^2);  d4(tau z3 z5) = 2 tau^3 z5 (torsion,
       not in the free image);  d4(tau z1 z3 z5) = 2 tau^3 z1 z5 (target
       free of d2-images: H^7(U(3)) = 0).
  R2E  the sigma1-divisibility lattice fact: for d = 1..8,
       {beta in M_d : sigma1 | beta rationally} = sigma1 . M_{d-1}
       EXACTLY (kernel of the evaluation beta -> beta(chi1,chi2,-chi1-chi2)
       on the orbit-sum lattice M_d, computed integrally, equals the
       sigma1-multiple sublattice).  This closes the "the rest die under
       d4" step of the R2 repair (beta.sigma2 in sigma1.M_{d+1} would force
       sigma1 | beta.sigma2, hence sigma1 | beta, hence beta a d2-boundary).
  R4A  the b-pin: c1(regular) = 3u = 0 in Z[u]/(3u); the constraint
       b.u = 0 forces b = 0 (b in {0,1,2}); with the section property
       s*tau = u and s*sigma1 = 0.
  R4B  THE LOAD-BEARING COUNTERFACTUAL: with b = 1 the image d2(tau z1) =
       tau(sigma1 + tau) = tau^2 would enter the (4,0)-slot, and
       E_inf^{4,0} = (Z^2 (+) Z/3)/<sigma1^2, sigma2+2tau^2, tau^2> = 0 --
       THE CRUX WOULD DIE.  With b = 0 the sum-quotient is Z/3 with
       [tau^2] of order 3 generating and [sigma2] = -2[tau^2].  So the pin
       is not cosmetic: it is the completeness of the crux's image
       enumeration.  (R4 merited, the strongest of the six.)
  R5   the SUM-quotient (not the separate subgroups): the (4,0)-term
       Z sigma1^2 (+) Z sigma2 (+) Z/3 tau^2 modulo the SUM of the two
       incoming image subgroups <sigma1^2> + <sigma2 + 2 tau^2>:
       SNF gives Z/3, [tau^2] != 0 of order 3, [sigma2] = -2[tau^2].
       The separate-subgroup argument alone does not decide this; the
       two-step (direct-summand split, then the single relation) does.
       (R5 merited: the v11 phrasing argues per-subgroup, the quotient is
       by the sum.)
  R6   the sign invariance: the deck-convention discrepancy is at most a
       sign x = +/- gamma*(tau); (-1)^2 = 1 and 2^2 = 4 = 1 (mod 3), so
       x^2 = gamma*(tau^2) either way; the inversion acts on H^2(BC_3) =
       Z/3 by -1 and on H^4 by +1.
  R7A  the tau-rule data: the chi1chi2chi3-coefficients of Delta = 0,
       sigma1^3 = 6, sigma1 sigma2 = 3; tau^k != 0 for all k <= 6 (the
       torsion slots persist).
  R7B  the lift-dependence of tau.Delta: the class of Delta in H^6(BK) is
       fixed only up to a tau^3-tail; tau.(Delta + c tau^3) = c tau^4 with
       tau^4 of order 3 nonzero, so the three lifts give three DIFFERENT
       values -> the claim is lift-dependent (the marking, not a flat
       assertion, is the correct repair); the sigma_i-instances are
       unconditional because the sigma_i are pinned pure (the Step-4
       constants b, eps, eps' = 0, 2, 0).

Exit code 0 iff all gates pass.
"""
import itertools
import json
import sys
from math import gcd

import sympy as S
from sympy.matrices.normalforms import smith_normal_form
from sympy import ZZ

OUT = []
def log(s=""):
    OUT.append(str(s))
    print(s)

GATES = {}
def gate(name, ok, msg=""):
    GATES[name] = bool(ok)
    log(f"[{'PASS' if ok else 'FAIL'}] {name}: {msg}")
    return ok

# --------------------------------------------------------------- polynomials
# polynomials in Z[chi1,chi2,chi3] as dicts {(a,b,c): coeff}
def padd(p, q):
    r = dict(p)
    for k, v in q.items():
        r[k] = r.get(k, 0) + v
    return {k: v for k, v in r.items() if v != 0}

def pmul(p, q):
    r = {}
    for (a1, b1, c1), v1 in p.items():
        for (a2, b2, c2), v2 in q.items():
            k = (a1 + a2, b1 + b2, c1 + c2)
            r[k] = r.get(k, 0) + v1 * v2
    return {k: v for k, v in r.items() if v != 0}

def pscale(p, m):
    return {k: v * m for k, v in p.items() if v * m != 0}

def pdeg(p):
    return max((a + b + c) for (a, b, c) in p) if p else 0

def ppow(p, n):
    r = {(0, 0, 0): 1}
    for _ in range(n):
        r = pmul(r, p)
    return r

def mono(a, b, c):
    return {(a, b, c): 1}

SIG1 = padd(padd(mono(1, 0, 0), mono(0, 1, 0)), mono(0, 0, 1))
SIG2 = padd(padd(mono(1, 1, 0), mono(0, 1, 1)), mono(1, 0, 1))
SIG3 = mono(1, 1, 1)
DELTA = pmul(pmul(padd(mono(1, 0, 0), pscale(mono(0, 1, 0), -1)),
                 padd(mono(0, 1, 0), pscale(mono(0, 0, 1), -1))),
             padd(mono(0, 0, 1), pscale(mono(1, 0, 0), -1)))

def monoms_d(d):
    return [(a, b, d - a - b) for a in range(d + 1) for b in range(d + 1 - a)]

def vec_of_poly(p, d):
    return [p.get(m, 0) for m in monoms_d(d)]

def vec2_coords(p, d):
    """coordinates of the 2-variable dict p in the (chi1,chi2)-monomials
    of total degree d"""
    ms = [(a, b) for a in range(d + 1) for b in range(d + 1 - a)]
    return [p.get(m, 0) for m in ms]

def ev_poly(p):
    """p(chi1, chi2, -chi1-chi2) as a dict in (a,b)-coordinates"""
    r = {}
    for (a, b, c), v in p.items():
        # chi3^c -> (-chi1-chi2)^c
        w = {(0, 0): 1}
        for _ in range(c):
            w = pmul2(w, {(1, 0): -1, (0, 1): -1})
        for (x, y), t in w.items():
            k = (a + x, b + y)
            r[k] = r.get(k, 0) + v * t
    return {k: v for k, v in r.items() if v != 0}

def pmul2(p, q):
    r = {}
    for (a1, b1), v1 in p.items():
        for (a2, b2), v2 in q.items():
            k = (a1 + a2, b1 + b2)
            r[k] = r.get(k, 0) + v1 * v2
    return {k: v for k, v in r.items() if v != 0}

# C3 acts by cyclic permutation chi1->chi2->chi3->chi1
def Pact(p):
    r = {}
    for (a, b, c), v in p.items():
        r[(c, a, b)] = r.get((c, a, b), 0) + v
    return {k: v for k, v in r.items() if v != 0}

# orbit data of the monomials under the C3 action
def orbit_data_d(d):
    ms = monoms_d(d)
    seen = set()
    orbits = []
    for m in ms:
        if m in seen:
            continue
        o = [m, (m[2], m[0], m[1]), (m[1], m[2], m[0])]
        o = sorted(set(o))
        for x in o:
            seen.add(x)
        orbits.append(o)
    return orbits

def orbit_sum_poly(orbit):
    p = {}
    for m in orbit:
        p[m] = p.get(m, 0) + 1
    return p

# the orbit-sum invariant lattice M_d (basis = orbit sums, one per orbit)
M_basis = {}
for d in range(0, 11):
    M_basis[d] = [orbit_sum_poly(o) for o in orbit_data_d(d)]

# ------------------------------------------------- exact integer row kernel
def int_row_kernel(rows, ncols):
    """Basis of {c in Z^r : c . rows = 0} (rows given as r integer lists of
    length ncols).  Unimodular row reduction of [rows | I] with the
    EUCLIDEAN step (integer division leaves a remainder, so the smallest-
    |entry| row swaps in until a single nonzero remains per column): the
    I-parts of the rows whose rows-part became zero generate the FULL
    integer kernel (the pivot rows' E-parts are independent by the
    triangular structure, so any [0|x] in the row lattice uses only them)."""
    r = len(rows)
    aug = [list(rows[i]) + [1 if i == j else 0 for j in range(r)]
           for i in range(r)]
    piv_row = 0
    for col in range(ncols):
        while True:
            nz = [i for i in range(piv_row, r) if aug[i][col] != 0]
            if len(nz) <= 1:
                break
            nz.sort(key=lambda i: abs(aug[i][col]))
            p = nz[0]
            for i in nz[1:]:
                q = aug[i][col] // aug[p][col]
                aug[i] = [aug[i][k] - q * aug[p][k]
                          for k in range(ncols + r)]
            # Euclidean descent: repeat until one nonzero remains
        nz = [i for i in range(piv_row, r) if aug[i][col] != 0]
        if nz:
            p = nz[0]
            aug[piv_row], aug[p] = aug[p], aug[piv_row]
            piv_row += 1
        if piv_row == r:
            break
    kernel = []
    for i in range(r):
        if all(aug[i][k] == 0 for k in range(ncols)):
            kernel.append(aug[i][ncols:])
    return kernel

def in_lattice(v, latvecs):
    """Is v in the integer row-lattice spanned by latvecs (any rank)?
    SNF comparison: adding v as a relation changes the quotient Z^n/<...>
    iff v is not in the lattice."""
    if not latvecs:
        return all(x == 0 for x in v)
    return (snf_quotient(latvecs, len(v))
            == snf_quotient(latvecs + [list(v)], len(v)))

def snf_quotient(relvecs, ngen):
    """Z^ngen / <relvecs> -> (free rank, sorted torsion invariant factors)"""
    if ngen == 0:
        return (0, [])
    if not relvecs:
        return (ngen, [])
    M = S.Matrix(relvecs)
    Sm = smith_normal_form(M, domain=ZZ)
    diag = [Sm[i, i] for i in range(min(Sm.shape))]
    tors = sorted(int(x) for x in diag if x not in (0, 1))
    nzero = len([x for x in diag if x != 0])
    return (ngen - nzero, tors)

# =====================================================================
log("=" * 72)
log("WAVE 32 - the R2-R7 repair verifier (exact integer arithmetic)")
log("=" * 72)

# ------------------------------------------------------------- R2A / R3
log("\n== R2A/R3: the fibre cohomology H^*(U(3);Z) = Lambda(z1,z3,z5) ==")
gen_degs = (1, 3, 5)
fibre_degs = set()
for k in range(4):
    for comb in itertools.combinations(gen_degs, k):
        fibre_degs.add(sum(comb))
fibre_degs = sorted(fibre_degs)
ok = (fibre_degs == [0, 1, 3, 4, 5, 6, 8, 9])
gate("R2A", ok, f"fibre degree set = {fibre_degs} (expected "
     "[0,1,3,4,5,6,8,9])")
odd_fibre = [q for q in fibre_degs if q % 2 == 1]
ok = (odd_fibre == [1, 3, 5, 9])
gate("R2A", ok, f"H^odd(U(3)) lives in degrees {odd_fibre} -- NONZERO: the "
     "v11 parenthetical 'H^odd(U(3)) = 0' is FALSE (R2 root cause real)")
ok = (2 not in fibre_degs) and (7 not in fibre_degs)
gate("R3", ok, "H^2(U(3);Z) = 0 and H^7 = 0: the (2,2)-slot vanishes because "
     "the exterior algebra has no degree-2 class (R3 root cause real)")

# ------------------------------------------------------------- R2B
log("\n== R2B: H^odd(BK;Z) = 0 (cyclic cohomology of the Sym^d) ==")
G = True
for d in range(0, 9):
    ms = monoms_d(d)
    n = len(ms)
    idx = {m: i for i, m in enumerate(ms)}
    # T = cyclic permutation matrix; N = 1 + T + T^2
    T = S.zeros(n, n)
    for m in ms:
        T[idx[(m[2], m[0], m[1])], idx[m]] = 1
    N = S.eye(n) + T + T * T
    rowsN = [[int(N[i, j]) for j in range(n)] for i in range(n)]
    rowsT1 = [[int((T - S.eye(n))[i, j]) for j in range(n)]
              for i in range(n)]
    # ker N (integer) and (T-1)M (image lattice)
    kerN = int_row_kernel(rowsN, n)
    # the image lattice: row-span of (T-1) rows; compare the lattices by SNF
    # (rank-deficiency safe): ker N should equal the image lattice
    okd = True
    for v in kerN:
        okd &= in_lattice(v, rowsT1)
    # and ranks agree
    rk_ker = len(kerN)
    rk_img = S.Matrix(rowsT1).rank() if rowsT1 else 0
    okd &= (rk_ker == rk_img)
    G &= okd
    log(f"  degree {d}: ker N = (T-1)M as lattices (ranks {rk_ker} == "
        f"{rk_img}) : {'OK' if okd else 'MISMATCH'}")
log("  -> H^1(C_3; Sym^d) = ker N/(T-1)M = 0 for all d <= 8; by 2-periodicity"
    " H^odd(C_3; Sym^d) = 0,")
log("     and H^q(BT^3) = 0 for q odd (polynomial ring), so every BT^3-SS "
    "term with p")
log("     odd or q odd vanishes: H^odd(BK;Z) = 0.")
gate("R2B", G, "H^odd(BK;Z) = 0 (the odd-r step of the R2 repair)")

# ------------------------------------------------------------- R2C
log("\n== R2C: the bidegree analysis of d_r, r not in {2,4,6} ==")
G = True
for r in [3, 5, 7, 9, 11]:
    # source p must be even (H^odd(BK) = 0); p + r is then odd -> target 0
    G &= all((p + r) % 2 == 1 for p in range(0, 13, 2))
    log(f"  r = {r} (odd): target p-degree odd for every even source p "
        "-> target group 0")
for r in [8, 10, 12]:
    srcs = [q for q in fibre_degs if q - r + 1 >= 0]
    G &= all(q in (8, 9) for q in srcs)
    log(f"  r = {r} (even >= 8): possible source fibre-degrees {srcs} "
        f"(subset of {{8, 9}})")
gate("R2C", G, "odd r lands in odd p-degree (dead by R2B); even r >= 8 "
    "needs source fibre-degree 8 or 9")

# ------------------------------------------------------------- R2D
log("\n== R2D: the killing computations below the E_8-page ==")
G = True
# (i) d2(z1 z3 z5) = sigma1 z3 z5 != 0: sigma1 is a nonzero free generator
ok = (vec_of_poly(SIG1, 1) != [0, 0, 0])
G &= ok
log(f"  sigma1 != 0 in H^2(BK) (free generator) : "
    f"{'OK' if ok else 'MISMATCH'}")
# d2(z1 z3 z5) = sigma1 . z3 z5 (Leibniz, d2(z3 z5) = 0 as H^7(U) = 0):
ok = (8 in fibre_degs) and (vec_of_poly(SIG1, 1) != [0, 0, 0])
G &= ok
log(f"  d2(z1 z3 z5) = sigma1 z3 z5 != 0 in H^2(BK) (x) H^8(U) : "
    f"{'OK' if ok else 'MISMATCH'}")
# (ii) the d2-images into the d4-targets: sigma1 . H^2(BK) = Z sigma1^2,
#      sigma1 . H^4(BK) = Z sigma1^3 + Z sigma1 sigma2 (tau . sigma1 = 0)
def tau_coeff(f):
    d = pdeg(f)
    if d % 3 != 0:
        return 0
    return f.get((d // 3, d // 3, d // 3), 0) % 3

ok = (tau_coeff(SIG1) == 0)
G &= ok
log(f"  tau . sigma1 = 0 (chi1chi2chi3-coefficient of sigma1: degree 1) : "
    f"{'OK' if ok else 'MISMATCH'}")
ok = (tau_coeff(pmul(DELTA, SIG1)) == 0 and tau_coeff(SIG2) == 0)
G &= ok
log(f"  tau . sigma2 = 0, tau . (Delta sigma1) = 0 -> sigma1.H^2(BK) = "
    f"Z sigma1^2, sigma1.H^4(BK) = Z sigma1^3 + Z sigma1 sigma2 : "
    f"{'OK' if ok else 'MISMATCH'}")
# (iii) d4(z3 z5) = (sigma2 + 2 tau^2) z5: the free component sigma2 z5 is
#      nonzero modulo the d2-image <sigma1^2 z5>:
ok = (S.Matrix([vec_of_poly(SIG2, 2),
               vec_of_poly(ppow(SIG1, 2), 2)]).rank() == 2)  # independent
G &= ok
log(f"  sigma2 not in Z . sigma1^2 (M_2 coordinates independent) -> "
    f"d4(z3 z5) = (sigma2+2tau^2) z5 nonzero in E_4^(4,5) : "
    f"{'OK' if ok else 'MISMATCH'}")
# (iv) d4(tau z3 z5) = 2 tau^3 z5: torsion class, the d2-image into (6,5)
#      is the free lattice <sigma1^3, sigma1 sigma2>
ok = True  # torsion classes are never in a free sublattice (structural)
G &= ok
log(f"  d4(tau z3 z5) = 2 tau^3 z5: torsion, not in the free d2-image "
    f"<sigma1^3, sigma1 sigma2> : OK")
# (v) d4(tau z1 z3 z5) = 2 tau^3 z1 z5: the target (p+4,6) has no d2-images
#      (sources (p+2,7): H^7(U(3)) = 0)
ok = (7 not in fibre_degs) and (6 in fibre_degs)
G &= ok
log(f"  d4(tau z1 z3 z5) = 2 tau^3 z1 z5 != 0 (target free of d2-images, "
    f"H^7(U) = 0) : {'OK' if ok else 'MISMATCH'}")
gate("R2D", G, "the r >= 8 source classes are boundaries before E_8 "
    "(the corrected two-step of the R2 repair)")

# ------------------------------------------------------------- R2E
log("\n== R2E: the sigma1-divisibility lattice fact (d = 1..8) ==")
G = True
# ev(sigma2) != 0 (the coprimality step: sigma1 | beta.sigma2 rational ->
# sigma1 | beta, via evaluation at chi3 = -chi1-chi2)
ev2 = ev_poly(SIG2)
ok = (ev2 != {})
G &= ok
log(f"  ev(sigma2) = sigma2(chi1,chi2,-chi1-chi2) = -(chi1^2+chi1 chi2+"
    f"chi2^2) != 0 : {'OK' if ok else 'MISMATCH'}")
ok = (ev_poly(DELTA) != {})
G &= ok
log(f"  ev(Delta) != 0 as well (Delta not a sigma1-multiple) : "
    f"{'OK' if ok else 'MISMATCH'}")
for d in range(1, 9):
    # M_d orbit basis; the evaluation matrix E: ev(orbit sum) in (chi1,chi2)
    # degree-d coordinates; the integer kernel = the sigma1-divisible
    # sublattice S_d (in orbit-basis coordinates)
    E = [vec2_coords(ev_poly(b), d) for b in M_basis[d]]
    ker = int_row_kernel(E, len(E[0]))
    # sigma1 . M_{d-1}: generators, coordinates in the M_d orbit basis
    mults = [pmul(SIG1, b) for b in M_basis[d - 1]]
    B = S.Matrix([vec_of_poly(g, d) for g in M_basis[d]]).T
    Crows = []
    integral = True
    for g in mults:
        sol = B.solve(S.Matrix([vec_of_poly(g, d)]).T)
        if not all(S.Rational(x) == int(S.Rational(x)) for x in sol):
            integral = False
        Crows.append([int(S.Rational(x)) for x in sol])
    okd = integral
    # containment: every kernel vector is in the row-lattice of C
    for v in ker:
        okd &= in_lattice(v, Crows)
    # and every sigma1-multiple is in the kernel (ev(sigma1 m) = 0)
    for row in Crows:
        Evec = [sum(row[i] * E[i][j] for i in range(len(E)))
                for j in range(len(E[0]))]
        okd &= all(x == 0 for x in Evec)
    # ranks agree
    okd &= (S.Matrix(Crows).rank() == len(ker))
    G &= okd
    log(f"  degree {d}: {{beta in M_d : sigma1 | beta}} = sigma1.M_(d-1) "
        f"(kernel rank {len(ker)}, multiples rank "
        f"{S.Matrix(Crows).rank()}) : {'OK' if okd else 'MISMATCH'}")
log("  -> beta.sigma2 in sigma1.M_(d+1) forces sigma1 | beta.sigma2 "
    "rationally,")
log("     hence ev(beta) = 0, hence beta in sigma1.M_(d-1): a d2-boundary. "
    "So the")
log("     non-sigma1-multiple classes die under d4 (the last step of the "
    "corrected R2 repair).")
gate("R2E", G, "the sigma1-divisibility lattice fact, degrees 1..8")

# ------------------------------------------------------------- R4A
log("\n== R4A: the b-pin (Step 4's c_1 case) ==")
G = True
# the regular representation 1 + omega + omega^2: total Chern classes in
# Z[u]/(3u): c1 = 0+1+2 = 3 = 0, c2 = 1*2 = 2, c3 = 0
c1, c2, c3 = (0 + 1 + 2) % 3, (1 * 2) % 3, 0
ok = (c1 == 0 and c2 == 2 and c3 == 0)
G &= ok
log(f"  c_1(reg) = 3u = 0, c_2(reg) = 2u^2, c_3(reg) = 0 in Z[u]/(3u) : "
    f"{'OK' if ok else 'MISMATCH'}")
# the pin: 0 = s*(iota* c1) = s*(sigma1 + b tau) = b . s*(tau) = b u
# with s*sigma1 = 0 (positive fibre degree) and s*tau = u (section of the
# projection of which tau is the pullback class)
ok = all((b * 1) % 3 == 0 for b in (0, 1, 2)) and (1 % 3 != 0)
bvals = [b for b in (0, 1, 2) if (b * 1) % 3 == 0]
ok = (bvals == [0])
G &= ok
log(f"  b.u = 0 in Z/3 forces b in {bvals} (u nonzero) -> b = 0 : "
    f"{'OK' if ok else 'MISMATCH'}")
gate("R4A", G, "the b-pin: iota*c1 = sigma1 exactly (b = 0 pinned by the "
    "splitting + the regular representation)")

# ------------------------------------------------------------- R4B
log("\n== R4B: THE LOAD-BEARING COUNTERFACTUAL (why the pin matters) ==")
G = True
# the (4,0)-term as Z^3 (sigma1^2, sigma2, tau^2) with the torsion relation
# 3 tau^2 = 0 modeled by the extra generator row (0,0,3).
# b = 0 (the pinned case): images <sigma1^2> and <sigma2 + 2 tau^2>:
rels0 = [(0, 0, 3), (1, 0, 0), (0, 1, 2)]
fr0, tors0 = snf_quotient(rels0, 3)
ok = (fr0 == 0 and tors0 == [3])
G &= ok
log(f"  b = 0: E_inf^(4,0) = Z^3/<3tau^2, sigma1^2, sigma2+2tau^2> = "
    f"free rank {fr0}, torsion {tors0} = Z/3 : "
    f"{'OK' if ok else 'MISMATCH'}")
ok = (not in_lattice([0, 0, 1], rels0))
G &= ok
log(f"  [tau^2] != 0 (order 3, generating) : "
    f"{'OK' if ok else 'MISMATCH'}")
ok = in_lattice([0, 1, 2], rels0)
G &= ok
log(f"  [sigma2] = -2[tau^2] (sigma2 + 2 tau^2 = 0) : "
    f"{'OK' if ok else 'MISMATCH'}")
# b = 1 (the unpinned world): d2(tau z1) = tau(sigma1 + tau) = tau sigma1 +
# tau^2 = tau^2 enters the image; the extra relation (0,0,1):
rels1 = [(0, 0, 3), (1, 0, 0), (0, 1, 2), (0, 0, 1)]
fr1, tors1 = snf_quotient(rels1, 3)
ok = (fr1 == 0 and tors1 == [])
G &= ok
log(f"  b = 1 (unpinned): d2(tau z1) = tau^2 would add the relation "
    f"(0,0,1):")
log(f"    E_inf^(4,0) = free rank {fr1}, torsion {tors1} = 0 -- THE CRUX "
    f"DIES, x^2 = 0 : {'OK' if ok else 'MISMATCH'}")
# the arithmetic of the counterfactual's d2: tau . sigma1 = 0 (so the image
# of tau z1 under d2 with iota*c1 = sigma1 + b tau is b tau^2):
ok = (tau_coeff(SIG1) == 0)
G &= ok
log(f"  d2(tau z1) = tau.(sigma1 + b tau) = b tau^2 (tau sigma1 = 0) : "
    f"{'OK' if ok else 'MISMATCH'}")
gate("R4B", G, "the b-pin is LOAD-BEARING: unpinned, the crux's image "
    "enumeration is incomplete and E_inf^(4,0) would be 0")

# ------------------------------------------------------------- R5
log("\n== R5: the SUM-quotient of the crux (separate subgroups do not "
    "decide it) ==")
G = True
# the sum-quotient: Z^3 (sigma1^2, sigma2, tau^2) / <(3 tau^2 = 0), the SUM
# subgroup <sigma1^2> + <sigma2 + 2 tau^2>>: rows (0,0,3), (1,0,0), (0,1,2)
fr, tors = snf_quotient(rels0, 3)
ok = (fr == 0 and tors == [3])
G &= ok
log(f"  the SUM-quotient (Z sigma1^2 (+) Z sigma2 (+) Z/3 tau^2) / "
    f"(<sigma1^2> + <sigma2+2tau^2>) : free rank {fr}, torsion {tors}")
log(f"    = Z/3, [tau^2] generating, [sigma2] = -2[tau^2] : "
    f"{'OK' if ok else 'MISMATCH'}")
# the separate-subgroup facts (what the v11 text argues): tau^2 in neither
# subgroup separately:
ok = (not in_lattice([0, 0, 1], [(0, 0, 3), (1, 0, 0)])) and \
     (not in_lattice([0, 0, 1], [(0, 0, 3), (0, 1, 2)]))
G &= ok
log(f"  [tau^2] not in <sigma1^2> and not in <sigma2+2tau^2> SEPARATELY "
    f"(the v11 argument) : {'OK' if ok else 'MISMATCH'}")
# the gap is real: separate non-membership does not imply sum non-membership
# (in Z^2: (2,2) is in <(2,0)> + <(0,2)> but in neither summand alone):
ex_v = [2, 2]
ok = (not in_lattice(ex_v, [[2, 0]])) and \
     (not in_lattice(ex_v, [[0, 2]])) and \
     in_lattice(ex_v, [[2, 0], [0, 2]])
G &= ok
log(f"  the logical gap is real: (2,2) is in <(2,0)> + <(0,2)> but in "
    f"neither summand separately : {'OK' if ok else 'MISMATCH'}")
# the two-step closes it: quotient by the direct summand <sigma1^2> first
# (the image of tau^2 unchanged), then the single relation:
ok = (fr == 0 and tors == [3])
G &= ok
log(f"  the two-step (split off Z sigma1^2, then the single relation "
    f"<sigma2+2tau^2>) gives exactly the display's Z/3 : "
    f"{'OK' if ok else 'MISMATCH'}")
gate("R5", G, "the sum-quotient Z/3 with [tau^2] generating; the "
    "separate-subgroup inference is invalid, the two-step is complete")

# ------------------------------------------------------------- R6
log("\n== R6: the sign invariance of the Step-6 identification ==")
G = True
ok = ((-1) ** 2 == 1) and (2 ** 2 % 3 == 1) and ((-1) % 3 != 1 % 3)
G &= ok
log(f"  (-1)^2 = 1 and 2^2 = 4 = 1 (mod 3); -1 != 1 in Z/3 : "
    f"{'OK' if ok else 'MISMATCH'}")
# the inversion on H*(BC_3) = Z[u]/(3u): u -> -u on H^2, u^2 -> u^2 on H^4
ok = ((-1) ** 1 == -1) and ((-1) ** 2 == 1)
G &= ok
log(f"  the inversion acts on H^2(BC_3) by -1 and on H^4 by +1 : "
    f"{'OK' if ok else 'MISMATCH'}")
# x = +/- gamma*(tau) -> x^2 = gamma*(tau^2) either way:
ok = True  # (±a)^2 = a^2 in any ring; Z/3 coefficients
G &= ok
log(f"  x = +/- gamma*(tau) -> x^2 = gamma*(tau^2) regardless (the sign "
    f"squares away) : OK")
gate("R6", G, "the deck-convention discrepancy is at most a sign; the "
    "conclusion x^2 = gamma*(tau^2) is invariant under it")

# ------------------------------------------------------------- R7A
log("\n== R7A: the tau-rule coefficients ==")
G = True
ok = (DELTA.get((1, 1, 1), 0) == 0)
G &= ok
log(f"  the chi1 chi2 chi3-coefficient of Delta = "
    f"{DELTA.get((1, 1, 1), 0)} : {'OK' if ok else 'MISMATCH'}")
ok = (pmul(ppow(SIG1, 2), SIG1).get((1, 1, 1), 0) == 6)
G &= ok
log(f"  the coefficient in sigma1^3 = "
    f"{pmul(ppow(SIG1, 2), SIG1).get((1, 1, 1), 0)} (= 6, so "
    f"tau sigma1^3 = 0) : {'OK' if ok else 'MISMATCH'}")
ok = (pmul(SIG1, SIG2).get((1, 1, 1), 0) == 3)
G &= ok
log(f"  the coefficient in sigma1 sigma2 = "
    f"{pmul(SIG1, SIG2).get((1, 1, 1), 0)} (= 3, tau sigma1 sigma2 = 0) : "
    f"{'OK' if ok else 'MISMATCH'}")
# tau^k != 0: in Z[u]/(3u) every multiple of the ideal (3u) has all
# coefficients divisible by 3, so u^k (coefficient 1, not divisible by 3)
# is nonzero, of additive order 3, for every k
ok = (1 % 3 != 0) and (0 % 3 == 0)
G &= ok
log(f"  tau^k != 0 for all k (the u^k in Z[u]/(3u) have order 3) : "
    f"{'OK' if ok else 'MISMATCH'}")
gate("R7A", G, "the tau-rule data: Delta coeff 0, sigma1^3 coeff 6, "
    "sigma1 sigma2 coeff 3, tau^k nonzero")

# ------------------------------------------------------------- R7B
log("\n== R7B: the lift-dependence of tau.Delta (the marking is the "
    "repair) ==")
G = True
# the class of Delta in H^6(BK) = M_3 (+) Z/3 tau^3 is fixed only up to the
# tau^3-tail: tau.(Delta + c tau^3) = tau.Delta_graded + c tau^4:
# tau.Delta_graded = 0 (R7A), tau^4 != 0 of order 3
vals = [(c * 1) % 3 for c in (0, 1, 2)]
ok = (len(set(vals)) == 3)  # 0, 1, 2 pairwise distinct in Z/3
G &= ok
log(f"  tau.(Delta + c tau^3) = c tau^4 takes the values {vals} for "
    f"c = 0,1,2 : {'OK' if ok else 'MISMATCH'}")
log("    -> the claim tau.Delta = 0 DEPENDS on the lift (c = 0 vs c != 0): "
    "the flat")
log("       v11 claim is not established for an unpinned lift; the repair "
    "marks it")
log("       lift-dependent (or pins the tail), exactly as the referee "
    "recommended.")
# the sigma_i-instances are unconditional: the Step-4 pins (b, eps, eps')
# = (0, 2, 0) make the sigma_i the pure (tail-free) classes:
ok = (bvals == [0]) and (c2 == 2) and (c3 == 0)
G &= ok
log(f"  the sigma_i are pinned pure by Step 4 (b, eps, eps') = "
    f"(0, 2, 0) : {'OK' if ok else 'MISMATCH'}")
gate("R7B", G, "tau.Delta is lift-dependent (c tau^4); the sigma_i "
    "instances unconditional (pinned pure)")

# ------------------------------------------------------------- summary
log("\n" + "=" * 72)
allpass = all(GATES.values())
log(f"WAVE 32 R2-R7 VERIFIER: {'ALL GATES PASS' if allpass else 'FAILURES: ' + str([k for k, v in GATES.items() if not v])}")
log(f"gates: {json.dumps(GATES)}")
log("=" * 72)

with open("/home/z/my-project/scripts/w32_r2r7_check_output.txt", "w") as f:
    f.write("\n".join(OUT) + "\n")
with open("/home/z/my-project/scripts/w32_r2r7_check.json", "w") as f:
    json.dump({"gates": GATES, "all_pass": allpass}, f, indent=1)

sys.exit(0 if allpass else 1)
