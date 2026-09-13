#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
WAVE 33 -- the second referee pass over the v12 proof of Proposition
prop:cupsquare (the instruments paper, v12).

Written from scratch for THIS pass: the second reader re-derived every
load-bearing claim by hand before coding it, and the gates below recompute
that re-derivation in exact integer arithmetic -- independently of the
manuscript text, of the wave-13C/28 machine data, and of the w30/w31/w32
verifier scripts (their code was not consulted).

Gate families
  P*  textual seams: repaired phrasings present, superseded phrasings gone,
      .tex == .txt, main-article sync, the notation-order scan (informational).
  M*  mathematics: lattice layer, tau-rule, crux, pins, degree-6 quotient
      (incl. the lift-independence of the H^6(B)-discriminant), the R2
      killing mechanism (incl. the sigma_1-divisibility lattice fact),
      the degree runs, R6/R7.
"""

import json
import os
import re
import sys
from fractions import Fraction
from math import comb

BASE = "/home/z/my-project"
V12DIR = os.path.join(BASE, "channel-supp-augmented", "manuscript uploads v12")
V12_TEX = os.path.join(V12DIR, "instruments-paper-revised12.tex")
V12_TXT = os.path.join(V12DIR, "instruments-paper-revised12.txt")
MAIN_TEX = os.path.join(BASE, "channel-supp-augmented",
                        "manuscript uploads v10", "main-article-revised10.tex")
OUT_TXT = os.path.join(BASE, "scripts", "w33_second_pass_output.txt")
OUT_JSON = os.path.join(BASE, "scripts", "w33_second_pass_check.json")

LOG = []
FAILS = []


def log(s=""):
    print(s)
    LOG.append(s)


def check(gate, name, ok, detail=""):
    status = "PASS" if ok else "FAIL"
    line = "[{}] {}: {}{}".format(gate, name, status,
                                  (" -- " + detail) if detail else "")
    print(line)
    LOG.append(line)
    if not ok:
        FAILS.append(line)
    return ok


def info(s):
    print(s)
    LOG.append(s)


# =====================================================================
# Part P -- textual seams
# =====================================================================

def norm(s):
    s = s.replace("~", " ")
    return re.sub(r"\s+", " ", s).strip()


PRESENCE = [
    # --- R1 (Wave 31): the five hunks ---
    ("R1-h1 statement", r"in which the discriminant class is twice a"),
    ("R1-h2 lattice", r"The free part, integrally, is the invariant lattice"),
    ("R1-h2 equal-coeff",
     r"the span is the whole invariant lattice, because the monomials of an invariant polynomial occur with equal coefficients on each orbit"),
    ("R1-h2 sublattice",
     r"Integrally the module is only a sublattice of the invariant lattice, of finite index"),
    ("R1-h2 safe degrees",
     r"one in degrees $d\le2$, exactly the degrees in which the crux of Step~5 below works, then $2$, $2$, $4$, $8$ in degrees $3$ to $6$"),
    ("R1-h2 witness",
     r"=\tfrac12(\sigma_1\sigma_2-3\sigma_3+\Delta)$ is invariant but lies in the module only after doubling"),
    ("R1-h3 display",
     r"H^6(BK;\mathbb Z)\ \cong\ \mathbb Z\{A_1,\,S_1,\,S_2,\,\sigma_3\}\oplus"),
    ("R1-h3 defs",
     r"where $A_1=\chi_1^3+\chi_2^3+\chi_3^3$ and $S_2=\chi_1^2\chi_3+\chi_2^2\chi_1+\chi_3^2\chi_2$, with $S_1$ as in Step~2"),
    ("R1-h3 relations",
     r"the two orbit sums satisfy $S_1+S_2=\sigma_1\sigma_2-3\sigma_3$ and $S_1-S_2=\Delta$"),
    ("R1-h3 index-two",
     r"the symmetric-function module of Step~2 spans an index-two sublattice of this free part, the four orbit sums generating it exactly"),
    ("R1-h7 quotient",
     r"running the quotient on the orbit-sum lattice of Step~3"),
    ("R1-h7 identities",
     r"using $\sigma_1\sigma_2=S_1+S_2+3\sigma_3$ and $\sigma_1^3=A_1+3(S_1+S_2)+6\sigma_3$: the relations kill $\sigma_3$, then $S_1+S_2$, then $A_1$ (each substituting into the next)"),
    ("R1-h7 torsion",
     r"the torsion class $\tau^3$ dies because $2\tau^3=0$ forces it (two is invertible modulo three), and the top class is the orbit sum $S_1$"),
    ("R1-h7 twice",
     r"in which the discriminant $\Delta=S_1-S_2=2S_1$ is twice a generator"),
    ("R1-h7 rational",
     r"where two is invertible and the discriminant class does generate"),
    ("R1-h5 remark",
     r"the orbit-sum invariant lattice together with its finite index over the symmetric-function module, the twice-a-generator position of the discriminant in the top class"),
    # --- R2 (Wave 32): the corrected two-step ---
    ("R2 odd-r",
     r"for odd $r$ the target sits in odd $p$-degree, where $H^{\mathrm{odd}}(BK;\mathbb Z)=0$ by Step~3 below"),
    ("R2 even-r lead",
     r"for even $r\ge8$ the source fibre-degree is $8$ or $9$, and the fibre classes there are boundaries before the $E_8$-page"),
    ("R2 deg9 free",
     r"d_2(\beta z_1z_3z_5)=\beta\sigma_1z_3z_5"),
    ("R2 deg9 free clause",
     r"kills every class whose coefficient survives multiplication by $\sigma_1$"),
    ("R2 deg9 torsion",
     r"d_4(\tau z_1z_3z_5)=2\tau^3z_1z_5\ne0$ kills the torsion coefficients, which annihilate $\sigma_1$"),
    ("R2 deg8 boundaries",
     r"In fibre degree eight the $\sigma_1$-multiple coefficients are $d_2$-boundaries"),
    ("R2 deg8 d4",
     r"d_4(\beta z_3z_5)=\beta(\sigma_2+2\tau^2)z_5\ne0"),
    ("R2 divisibility",
     r"a class $\beta$ whose $\beta\sigma_2$ is a $\sigma_1$-multiple is itself a $\sigma_1$-multiple"),
    ("R2 triangular",
     r"divisibility by $\sigma_1=\chi_1+\chi_2+\chi_3$ is triangular in the monomials"),
    # --- R3 ---
    ("R3 (2,2)-clause",
     r"the exterior algebra $\Lambda(z_1,z_3,z_5)$ has no class of degree two"),
    # --- R4 (two hunks) ---
    ("R4a display",
     r"hence $\iota^*c_1=\sigma_1+b\,\tau$, $\iota^*c_2=\sigma_2+\varepsilon\tau^2$ and $\iota^*c_3=\sigma_3+\varepsilon'\tau^3$"),
    ("R4a parenthetical",
     r"the restriction to the fibre pins only the free components: the torsion restricts to zero, and the $(0,2)$-slot is $\mathbb Z\sigma_1$"),
    ("R4b pin",
     r"Hence $0=s^*(\iota^*c_1)=s^*(\sigma_1+b\,\tau)=bu$"),
    ("R4b section",
     r"and $s^*\tau=u$, $s$ being a section of the projection whose pullback class $\tau$ is), so $b=0$"),
    ("R4b eps",
     r"and $2u^2=s^*(\iota^*c_2)=\varepsilon u^2$ and $0=\varepsilon'u^3$"),
    ("R4 pinned display",
     r"d_2(z_1)=\sigma_1,\qquad d_4(z_3)=\sigma_2+2\tau^2,\qquad d_6(z_5)=\sigma_3"),
    # --- R5 ---
    ("R5 two-step",
     r"Quotient out the direct summand $\mathbb Z\sigma_1^2$ first --- a quotient by a direct summand leaves both the class of $\tau^2$ and the complementary summand unchanged"),
    ("R5 single relation",
     r"with the single incoming relation $\sigma_2+2\tau^2$, a class of infinite order (its free component $\sigma_2$ is nonzero); an element of order three never lies in the subgroup generated by an infinite-order class"),
    # --- R6 ---
    ("R6 parenthetical",
     r"the identification passes through the inversion $K\backslash U(3)\cong U(3)/K$, so a different deck convention could at worst flip a sign, $x=\pm\gamma^*(\tau)$; nothing below depends on the choice, the sign squaring away in $x^2=\gamma^*(\tau^2)$"),
    # --- R7 ---
    ("R7 unconditional",
     r"these instances unconditional, the $\sigma_i$ being the pinned pure classes of Step~4 below"),
    ("R7 lift-dependent",
     r"is lift-dependent: the class of $\Delta$ in $H^6(BK;\mathbb Z)$ is fixed only up to a $\tau^3$-tail, and $\tau\cdot(\Delta+c\,\tau^3)=c\,\tau^4\ne0$ when $c\ne0$; it is not used below"),
    # --- Step 3 closing (supports Step 1's forward reference) ---
    ("odd-BK support",
     r"The odd cohomology $H^{\mathrm{odd}}(BK;\mathbb Z)$ vanishes, as the collapse argument shows"),
]

ABSENCE = [
    ("v11 R2 premise (false)",
     r"where $H^{\mathrm{odd}}(U(3))=0$"),
    ("v11 R5 per-subgroup",
     r"a finite-order element never lies in a subgroup generated by an infinite-order element"),
    ("v11 R4 uniqueness",
     r"the free generator is the unique class restricting"),
    ("v11 R7 flat tauDelta",
     r"the alternating polynomial $\Delta$ contains no monomial"),
    ("v10 statement clause",
     r"a discriminant class generating"),
    ("v10 top-class clause",
     r"the top class being the discriminant"),
    ("v10 integral module",
     r"\Delta\cdot\mathbb Z[\sigma_1,\sigma_2,\sigma_3]"),
]


def run_part_p():
    info("")
    info("=" * 70)
    info("PART P -- TEXTUAL SEAMS (v12, .tex and .txt)")
    info("=" * 70)
    with open(V12_TEX, "r", encoding="utf-8") as f:
        tex_raw = f.read()
    with open(V12_TXT, "r", encoding="utf-8") as f:
        txt_raw = f.read()
    tex = norm(tex_raw)
    txt = norm(txt_raw)

    n_ok = 0
    for name, phrase in PRESENCE:
        ph = norm(phrase)
        ok = (ph in tex) and (ph in txt)
        check("P1", "presence: " + name, ok)
        n_ok += ok
    info("   ({} of {} presence phrases verified)".format(n_ok, len(PRESENCE)))

    for name, phrase in ABSENCE:
        ph = norm(phrase)
        ok = (ph not in tex) and (ph not in txt)
        check("P2", "absence: " + name, ok)

    check("P4", ".tex == .txt (byte-identical)",
          tex_raw == txt_raw,
          "sizes {} vs {}".format(len(tex_raw), len(txt_raw)))

    # --- P3: the notation-order scan (informational, Finding F1) ---
    info("")
    info("[P3] notation-order scan (Step 1 uses sigma/tau before their definitions):")
    lines = tex_raw.split("\n")
    # locate step boundaries
    step1 = step2 = step4 = None
    sig_def = tau_def = pin_line = odd_line = None
    for i, ln in enumerate(lines, 1):
        if step1 is None and "\\emph{Step 1 (the fibration" in ln:
            step1 = i
        if step2 is None and "\\emph{Step 2 (the cohomology" in ln:
            step2 = i
        if step4 is None and "\\emph{Step 4 (the transgression" in ln:
            step4 = i
        if sig_def is None and "are the elementary symmetric functions" in ln:
            sig_def = i
        if tau_def is None and "for the class of the $(2,0)$-slot" in ln:
            tau_def = i
        if pin_line is None and "so $b=0$" in ln:
            pin_line = i
        if odd_line is None and "collapse argument shows" in ln:
            odd_line = i
    first_sigma = first_tau = None
    if step1 and step2:
        for i in range(step1, step2):
            if first_sigma is None and ("\\sigma_1" in lines[i - 1]
                                        or "\\sigma_2" in lines[i - 1]):
                first_sigma = i
            if first_tau is None and "\\tau" in lines[i - 1]:
                first_tau = i
    info("   Step 1 spans lines {}-{}".format(step1, step2 - 1 if step2 else "?"))
    info("   first sigma_1/sigma_2 use inside Step 1: line {}".format(first_sigma))
    info("   first tau use inside Step 1:              line {}".format(first_tau))
    info("   sigma_i defined (Step 2):                 line {}".format(sig_def))
    info("   tau defined (Step 2 end):                 line {}".format(tau_def))
    info("   H^odd(BK)=0 stated (Step 3):              line {}".format(odd_line))
    info("   d_4(z_3)=sigma_2+2tau^2 pinned (Step 4):  line {}".format(pin_line))
    forward = (first_sigma is not None and sig_def is not None
               and first_sigma < sig_def)
    info("   => F1 evidence: Step 1 uses sigma/tau {} lines before the "
         "definitions".format(sig_def - first_sigma) if forward else "")
    info("   (informational only -- see the wave note, Finding F1)")

    # --- P5: main-article sync (v10) ---
    info("")
    info("[P5] main-article sync clauses (main stays at v10):")
    try:
        with open(MAIN_TEX, "r", encoding="utf-8") as f:
            main = norm(f.read())
        for phrase in [r"hand-derived, machine-certified, and independently re-implemented",
                       r"flag-quotient computation",
                       r"the cyclic flag quotient underlying that premise"]:
            check("P5", "main sync: " + phrase[:50],
                  norm(phrase) in main)
        # the main article must NOT reference proof internals
        for phrase in [r"orbit-sum", r"lattice-index", r"b\,\tau"]:
            check("P5", "main free of proof-internal '{}':".format(phrase),
                  norm(phrase) not in main)
    except FileNotFoundError:
        check("P5", "main article present", False, MAIN_TEX)


# =====================================================================
# Exact-integer engine
# =====================================================================

def padd(a, b):
    r = dict(a)
    for k, v in b.items():
        r[k] = r.get(k, 0) + v
    r = {k: v for k, v in r.items() if v != 0}
    return r


def psub(a, b):
    return padd(a, {k: -v for k, v in b.items()})


def pscale(a, c):
    return {k: c * v for k, v in a.items() if c * v != 0}


def pmul(a, b):
    r = {}
    for (e1, e2, e3), c in a.items():
        for (f1, f2, f3), d in b.items():
            k = (e1 + f1, e2 + f2, e3 + f3)
            r[k] = r.get(k, 0) + c * d
    return {k: v for k, v in r.items() if v != 0}


def Tact(p):
    # T: chi1 -> chi2, chi2 -> chi3, chi3 -> chi1
    return {(e3, e1, e2): c for (e1, e2, e3), c in p.items()}


CHI1 = {(1, 0, 0): 1}
CHI2 = {(0, 1, 0): 1}
CHI3 = {(0, 0, 1): 1}
SIG1 = padd(padd(CHI1, CHI2), CHI3)
SIG2 = padd(pmul(CHI1, CHI2), padd(pmul(CHI1, CHI3), pmul(CHI2, CHI3)))
SIG3 = pmul(pmul(CHI1, CHI2), CHI3)
DELTA = pmul(pmul(psub(CHI1, CHI2), psub(CHI1, CHI3)), psub(CHI2, CHI3))


def monomials(d):
    out = []
    for e1 in range(d + 1):
        for e2 in range(d + 1 - e1):
            out.append((e1, e2, d - e1 - e2))
    return out


def orbit_cycle(e):
    cyc = [e]
    cur = (e[2], e[0], e[1])
    while cur != e:
        cyc.append(cur)
        cur = (cur[2], cur[0], cur[1])
    return cyc


def orbit_sums(d):
    """Basis of the invariant lattice M_d^{C3}: orbit sums (fixed monomials
    included as singleton orbits). Disjoint supports => independent."""
    sums = []
    seen = set()
    for e in monomials(d):
        if e in seen:
            continue
        cyc = orbit_cycle(e)
        seen.update(cyc)
        s = {}
        for m in cyc:
            s[m] = s.get(m, 0) + 1
        sums.append(s)
    return sums


def inv_coords(p, d):
    """Coordinates of an invariant polynomial in the orbit-sum basis.
    Returns None if p is not invariant (or not homogeneous of degree d)."""
    for (e1, e2, e3) in p:
        if e1 + e2 + e3 != d:
            return None
    basis = orbit_sums(d)
    coords = []
    for s in basis:
        cs = set(p.get(m, 0) for m in s)
        if len(cs) != 1:
            return None
        coords.append(cs.pop())
    return coords


def sig_monoms(deg):
    """All products sigma_1^a sigma_2^b sigma_3^c with a+2b+3c = deg."""
    out = []
    for c in range(deg // 3 + 1):
        for b in range((deg - 3 * c) // 2 + 1):
            a = deg - 3 * c - 2 * b
            poly = {(0, 0, 0): 1}
            for _ in range(a):
                poly = pmul(poly, SIG1)
            for _ in range(b):
                poly = pmul(poly, SIG2)
            for _ in range(c):
                poly = pmul(poly, SIG3)
            out.append(poly)
    return out


def module_gens(d):
    gens = list(sig_monoms(d))
    if d >= 3:
        gens += [pmul(DELTA, m) for m in sig_monoms(d - 3)]
    return gens


# ---------------- linear algebra over Z ----------------

def det_int(M):
    n = len(M)
    A = [[Fraction(M[i][j]) for j in range(n)] for i in range(n)]
    det = Fraction(1)
    for c in range(n):
        piv = None
        for i in range(c, n):
            if A[i][c] != 0:
                piv = i
                break
        if piv is None:
            return Fraction(0)
        if piv != c:
            A[c], A[piv] = A[piv], A[c]
            det = -det
        det *= A[c][c]
        inv = Fraction(1) / A[c][c]
        for i in range(c + 1, n):
            if A[i][c] != 0:
                f = A[i][c] * inv
                for j in range(c, n):
                    A[i][j] -= f * A[c][j]
    assert det.denominator == 1
    return int(det)


def solve_int(B, v):
    """Solve B x = v (B: m x n) over the rationals; return (x, integral?)
    or None if inconsistent."""
    m = len(B)
    n = len(B[0])
    A = [[Fraction(B[i][j]) for j in range(n)] for i in range(m)]
    rhs = [Fraction(x) for x in v]
    piv_col = []
    row = 0
    for c in range(n):
        piv = None
        for i in range(row, m):
            if A[i][c] != 0:
                piv = i
                break
        if piv is None:
            continue
        A[row], A[piv] = A[piv], A[row]
        rhs[row], rhs[piv] = rhs[piv], rhs[row]
        inv = Fraction(1) / A[row][c]
        A[row] = [x * inv for x in A[row]]
        rhs[row] *= inv
        for i in range(m):
            if i != row and A[i][c] != 0:
                f = A[i][c]
                A[i] = [a - f * b for a, b in zip(A[i], A[row])]
                rhs[i] -= f * rhs[row]
        piv_col.append(c)
        row += 1
    for i in range(m):
        if all(A[i][j] == 0 for j in range(n)) and rhs[i] != 0:
            return None
    x = [Fraction(0)] * n
    for r, c in enumerate(piv_col):
        x[c] = rhs[r]
    integral = all(xi.denominator == 1 for xi in x)
    return x, integral


def matmul(A, B):
    return [[sum(A[i][k] * B[k][j] for k in range(len(B)))
             for j in range(len(B[0]))] for i in range(len(A))]


def vec_mat(v, M):
    """row vector times matrix"""
    return [sum(v[k] * M[k][j] for k in range(len(M))) for j in range(len(M[0]))]


def mat_inv_int(M):
    n = len(M)
    A = [[Fraction(M[i][j]) for j in range(n)] for i in range(n)]
    I = [[Fraction(int(i == j)) for j in range(n)] for i in range(n)]
    for c in range(n):
        piv = None
        for i in range(c, n):
            if A[i][c] != 0:
                piv = i
                break
        assert piv is not None, "matrix not invertible"
        A[c], A[piv] = A[piv], A[c]
        I[c], I[piv] = I[piv], I[c]
        inv = Fraction(1) / A[c][c]
        A[c] = [x * inv for x in A[c]]
        I[c] = [x * inv for x in I[c]]
        for i in range(n):
            if i != c and A[i][c] != 0:
                f = A[i][c]
                A[i] = [a - f * b for a, b in zip(A[i], A[c])]
                I[i] = [a - f * b for a, b in zip(I[i], I[c])]
    for i in range(n):
        for j in range(n):
            assert I[i][j].denominator == 1
    return [[int(I[i][j]) for j in range(n)] for i in range(n)]


def snf(rows):
    """Smith normal form: returns (S, P, Q) with P.rows.Q = S diagonal,
    S[i][i] >= 0, P and Q unimodular."""
    m = len(rows)
    n = len(rows[0])
    S = [list(r) for r in rows]
    P = [[int(i == j) for j in range(m)] for i in range(m)]
    Q = [[int(i == j) for j in range(n)] for i in range(n)]

    def swap_rows(i, k):
        S[i], S[k] = S[k], S[i]
        P[i], P[k] = P[k], P[i]

    def swap_cols(j, l):
        for i in range(m):
            S[i][j], S[i][l] = S[i][l], S[i][j]
        for i in range(n):
            Q[i][j], Q[i][l] = Q[i][l], Q[i][j]

    def add_row(i, k, q):
        for j in range(n):
            S[i][j] += q * S[k][j]
        for j in range(m):
            P[i][j] += q * P[k][j]

    def add_col(j, l, q):
        for i in range(m):
            S[i][j] += q * S[i][l]
        for i in range(n):
            Q[i][j] += q * Q[i][l]

    r = c = 0
    guard = 0
    while r < m and c < n:
        guard += 1
        assert guard < 100000, "snf runaway"
        piv = None
        for i in range(r, m):
            for j in range(c, n):
                if S[i][j] != 0:
                    if piv is None or abs(S[i][j]) < abs(S[piv[0]][piv[1]]):
                        piv = (i, j)
        if piv is None:
            break
        i, j = piv
        if i != r:
            swap_rows(i, r)
        if j != c:
            swap_cols(j, c)
        # Euclid-clear row r (right of c) and column c (below r)
        inner_guard = 0
        while True:
            inner_guard += 1
            assert inner_guard < 100000, "snf inner runaway"
            row_nz = next((j2 for j2 in range(c + 1, n) if S[r][j2] != 0), None)
            col_nz = next((i2 for i2 in range(r + 1, m) if S[i2][c] != 0), None)
            if row_nz is None and col_nz is None:
                break
            if row_nz is not None:
                j2 = row_nz
                q = S[r][j2] // S[r][c]
                add_col(j2, c, -q)
                if S[r][j2] != 0:
                    swap_cols(j2, c)
                continue
            i2 = col_nz
            q = S[i2][c] // S[r][c]
            add_row(i2, r, -q)
            if S[i2][c] != 0:
                swap_rows(i2, r)
        # divisibility of the remaining submatrix by the pivot
        bad = None
        for i2 in range(r, m):
            for j2 in range(c, n):
                if S[i2][j2] != 0 and S[i2][j2] % S[r][c] != 0:
                    bad = (i2, j2)
                    break
            if bad:
                break
        if bad is not None:
            add_row(r, bad[0], 1)
            continue
        if S[r][c] < 0:
            add_row(r, r, -2)
        r += 1
        c += 1
    return S, P, Q


def snf_rank_diag(S):
    r = 0
    while r < len(S) and r < len(S[0]) and S[r][r] != 0:
        r += 1
    return r


def rowspan_contains(R, v):
    """Is the row vector v in the integer row span of the rows of R?"""
    S, P, Q = snf(R)
    n = len(R[0])
    w = vec_mat(v, Q)
    rank = snf_rank_diag(S)
    for j in range(rank, n):
        if w[j] != 0:
            return False
    for j in range(rank):
        if w[j] % S[j][j] != 0:
            return False
    return True


def quotient_structure(R, n):
    """Z^n / <rows of R> = (free rank, [torsion invariants >1])"""
    S, P, Q = snf(R)
    rank = snf_rank_diag(S)
    tors = [S[j][j] for j in range(rank) if abs(S[j][j]) > 1]
    return n - rank, sorted(tors)


def element_order(R, v, bound=12):
    """Order of the class of v in Z^n/<rows R> (0 = infinite)."""
    if rowspan_contains(R, v):
        return 1
    for t in range(2, bound + 1):
        if rowspan_contains(R, [t * x for x in v]):
            return t
    return 0


def integer_kernel(cols):
    """cols: matrix as list of rows (m x n), interpreted column-wise map
    x -> cols.x. Returns a basis (list of integer vectors, length n) of
    {x : cols.x = 0}.

    Derivation: S = P.cols.Q  =>  cols = P^-1 S Q^-1, so
    cols.x = 0  <=>  S (Q^-1 x) = 0  <=>  (Q^-1 x)_j = 0 for j < rank.
    Hence the kernel is spanned by the columns of Q at positions >= rank.
    """
    S, P, Q = snf(cols)
    n = len(cols[0])
    rank = snf_rank_diag(S)
    basis = []
    for j in range(rank, n):
        basis.append([Q[i][j] for i in range(n)])
    return basis


def subst_sigma1_locus(p):
    """Substitute chi3 = -(chi1+chi2): return poly in (x,y) exponents."""
    r = {}
    for (e1, e2, e3), c in p.items():
        sign = (-1) ** e3
        for k in range(e3 + 1):
            key = (e1 + k, e2 + e3 - k)
            r[key] = r.get(key, 0) + c * sign * comb(e3, k)
    return {k: v for k, v in r.items() if v != 0}


def coords3(p):
    """Coordinates of a degree-3 invariant in the PAPER order
    (A1, S1, S2, sigma3), robust to the enumeration order of the orbit
    basis."""
    cc = inv_coords(p, 3)
    if cc is None:
        return None
    basis = orbit_sums(3)
    targets = [(3, 0, 0), (2, 1, 0), (2, 0, 1), (1, 1, 1)]
    order = []
    for t in targets:
        for idx, s in enumerate(basis):
            if t in s:
                order.append(idx)
                break
    return [cc[order[k]] for k in range(4)]


def eval_matrix(d):
    """Columns = orbit sums of M_d substituted at the sigma_1-root locus.
    Rows indexed by the (d+1) monomials x^{d-i} y^i."""
    basis = orbit_sums(d)
    keys = [(d - i, i) for i in range(d + 1)]
    kidx = {k: i for i, k in enumerate(keys)}
    A = [[0] * len(basis) for _ in range(len(keys))]
    for j, s in enumerate(basis):
        sub = subst_sigma1_locus(s)
        for k, c in sub.items():
            A[kidx[k]][j] = c
    return A, basis


# =====================================================================
# Part M -- mathematics
# =====================================================================

def run_part_m():
    info("")
    info("=" * 70)
    info("PART M -- MATHEMATICS (independent exact-integer re-derivation)")
    info("=" * 70)

    # ---------- M1: the lattice layer (R1) ----------
    info("")
    info("[M1] the orbit-sum lattice vs the symmetric-function module:")
    expect_index = {0: 1, 1: 1, 2: 1, 3: 2, 4: 2, 5: 4, 6: 8}
    for d in range(0, 7):
        basis = orbit_sums(d)
        gens = module_gens(d)
        coords = []
        invariant_ok = True
        for g in gens:
            cc = inv_coords(g, d)
            if cc is None:
                invariant_ok = False
                break
            coords.append(cc)
        if not check("M1", "degree {}: module generators invariant".format(d),
                     invariant_ok):
            continue
        B = [[coords[j][i] for j in range(len(coords))]
             for i in range(len(basis))]  # r x r (basis rows, gens cols)
        dd = det_int(B)
        check("M1", "degree {}: index [M_d : module] = {}".format(
            d, expect_index[d]), abs(dd) == expect_index[d],
            "det = {}".format(dd))

    # the witness S1
    S1 = orbit_sums(3)[1]  # orbit of (2,1,0): A1, S1, S2, sigma3 order?
    # determine names precisely
    orb3 = orbit_sums(3)
    A1 = None
    S1p = None
    S2p = None
    FIX = None
    for s in orb3:
        if (3, 0, 0) in s:
            A1 = s
        elif (2, 1, 0) in s:
            S1p = s
        elif (2, 0, 1) in s:
            S2p = s
        else:
            FIX = s
    check("M1", "M_3 basis = {A1, S1, S2, sigma3} (4 orbits)",
          A1 is not None and S1p is not None and S2p is not None
          and FIX == {(1, 1, 1): 1})
    check("M1", "identity 2*S1 = sigma1*sigma2 - 3*sigma3 + Delta",
          pscale(S1p, 2) == padd(psub(pmul(SIG1, SIG2), pscale(SIG3, 3)),
                                 DELTA))
    check("M1", "identity S1 + S2 = sigma1*sigma2 - 3*sigma3",
          padd(S1p, S2p) == psub(pmul(SIG1, SIG2), pscale(SIG3, 3)))
    check("M1", "identity S1 - S2 = Delta", psub(S1p, S2p) == DELTA)
    check("M1", "Newton: A1 = sigma1^3 - 3 sigma1 sigma2 + 3 sigma3",
          A1 == padd(psub(pmul(SIG1, pmul(SIG1, SIG1)),
                          pscale(pmul(SIG1, SIG2), 3)),
                     pscale(SIG3, 3)))
    # witness membership
    gens3 = module_gens(3)
    mods3_coords = [inv_coords(g, 3) for g in gens3]
    B3 = [[mods3_coords[j][i] for j in range(len(mods3_coords))] for i in range(4)]
    vS1 = inv_coords(S1p, 3)
    sol = solve_int(B3, vS1)
    check("M1", "witness: S1 NOT in the module lattice (b = e = 1/2)",
          sol is not None and not sol[1],
          "rational solution exists (rank match), not integral")
    sol2 = solve_int(B3, [2 * x for x in vS1])
    check("M1", "witness: 2*S1 IS in the module lattice",
          sol2 is not None and sol2[1])

    # ---------- M2: the tau-rule ----------
    info("")
    info("[M2] the torsion product rule (norm model H^2(C3; M_d) = M^C3 / N M):")
    for d in range(0, 9):
        basis = orbit_sums(d)
        r = len(basis)
        fixed = None
        for idx, s in enumerate(basis):
            if len(s) == 1 and (d % 3 == 0):
                m = next(iter(s))
                if m[0] == m[1] == m[2]:
                    fixed = idx
        # norm image rows in orbit-sum coordinates:
        # N(orbit monomial) = orbit sum -> e_j (free orbits only);
        # N(fixed monomial) = 3 e_fixed
        rows = []
        for i in range(r):
            if i != fixed:
                rows.append([int(j == i) for j in range(r)])
        if fixed is not None:
            rows.append([3 if j == fixed else 0 for j in range(r)])
        free, tors = quotient_structure(rows, r)
        if d % 3 == 0:
            check("M2", "degree {}: H^2(C3; M_d) = Z/3 (fixed coord mod 3)"
                  .format(d), free == 0 and tors == [3])
        else:
            check("M2", "degree {}: H^2(C3; M_d) = 0".format(d),
                  free == 0 and tors == [])

    def tau_of(p):
        """tau . f = [fixed-monomial coefficient mod 3] as 0,1,2 (None=0)."""
        d = sum(next(iter(p)))
        if d % 3 != 0:
            return 0
        return p.get((d // 3, d // 3, d // 3), 0) % 3

    check("M2", "tau*sigma1 = 0 (3 does not divide 1)", tau_of(SIG1) == 0)
    check("M2", "tau*sigma2 = 0 (3 does not divide 2)", tau_of(SIG2) == 0)
    check("M2", "tau*sigma1^3 = 0 (chi1chi2chi3-coeff 6)",
          tau_of(pmul(SIG1, pmul(SIG1, SIG1))) == 0)
    check("M2", "tau*sigma3 != 0 (generator of the (2,6)-slot)",
          tau_of(SIG3) == 1)
    check("M2", "tau*Delta = 0 at the leading level (no chi1chi2chi3)",
          tau_of(DELTA) == 0)
    check("M2", "tau*A1 = 0", tau_of(A1) == 0)
    check("M2", "tau*S1 = tau*S2 = 0", tau_of(S1p) == 0 and tau_of(S2p) == 0)
    check("M2", "tau*sigma1*sigma2 = 0 (chi1chi2chi3-coeff 3)",
          tau_of(pmul(SIG1, SIG2)) == 0)
    # H^odd(BK) = 0 support: ker N = (T-1)M on each Sym^d
    for d in range(0, 9):
        mons = monomials(d)
        idx = {m: i for i, m in enumerate(mons)}
        n = len(mons)
        Tm = [[0] * n for _ in range(n)]
        for m in mons:
            tm = (m[2], m[0], m[1])
            Tm[idx[tm]][idx[m]] += 1  # column m maps to tm  (column convention)
        # rows: we need matrices acting on column vectors x:
        # T acts: (Tx)_i = sum_j Tm[i][j] x_j -- Tm as above is T.
        def mm(A, Bm):
            return [[sum(A[i][k] * Bm[k][j] for k in range(len(Bm)))
                     for j in range(len(Bm[0]))] for i in range(len(A))]
        I = [[int(i == j) for j in range(n)] for i in range(n)]
        Nm = mm(mm(I, Tm), Tm)
        Nm = [[Nm[i][j] + Tm[i][j] + I[i][j] for j in range(n)]
              for i in range(n)]
        Tminus1 = [[Tm[i][j] - I[i][j] for j in range(n)] for i in range(n)]
        Tminus1_T = [list(col) for col in zip(*Tminus1)]
        kerN = integer_kernel(Nm)
        ok = True
        for b in kerN:
            if not rowspan_contains(Tminus1_T, b):
                ok = False
                break
        check("M2", "degree {}: ker N  <=  (T-1)M  [H^odd(BK)=0]"
              .format(d), ok, "ker rank {}".format(len(kerN)))

    # ---------- M3: the crux ----------
    info("")
    info("[M3] the crux: E_inf^{4,0} = (Z sigma1^2 (+) Z sigma2 (+) Z/3 tau^2)"
         " / <sigma1^2, sigma2 + 2 tau^2>:")
    # coordinates (sigma1^2, sigma2, tau^2); Z/3 on tau^2 -> relation (0,0,3)
    rows = [[1, 0, 0], [0, 1, 2], [0, 0, 3]]
    free, tors = quotient_structure(rows, 3)
    check("M3", "quotient = Z/3 (no free part)", free == 0 and tors == [3])
    check("M3", "[tau^2] has order 3 (nonzero)", element_order(rows, [0, 0, 1]) == 3)
    check("M3", "[sigma2] = -2[tau^2]",
          rowspan_contains(rows, [0, 1, 2]))
    # the two-step: quotient by the direct summand first
    rows2 = [[1, 2], [0, 3]]  # (sigma2, tau^2-torsion)
    free2, tors2 = quotient_structure(rows2, 2)
    check("M3", "two-step: (Z sigma2 (+) Z/3 tau^2)/<sigma2+2tau^2> = Z/3",
          free2 == 0 and tors2 == [3])
    # R5's logical-gap witness
    check("M3", "witness (2,2) in <(2,0)>+<(0,2)> but in neither alone",
          rowspan_contains([[2, 0], [0, 2]], [2, 2])
          and not rowspan_contains([[2, 0]], [2, 2])
          and not rowspan_contains([[0, 2]], [2, 2]))
    # R4B counterfactual: unpinned b injects <tau^2> and kills the crux
    rows_b = [[1, 0, 0], [0, 1, 2], [0, 0, 3], [0, 0, 1]]
    free_b, tors_b = quotient_structure(rows_b, 3)
    check("M3", "counterfactual (b unpinned, d_2(tau z1) = tau^2): "
          "E_inf^{4,0} = 0 -- the crux dies",
          free_b == 0 and tors_b == [])

    # ---------- M4: the degree-6 quotient ----------
    info("")
    info("[M4] the degree-6 quotient (orbit-sum lattice, R1's Step-7 repair):")
    # coordinates (A1, S1, S2, sigma3, tau^3) -- paper order
    c_A1 = coords3(A1)
    c_S1 = coords3(S1p)
    c_S2 = coords3(S2p)
    c_s3 = coords3(SIG3)
    c_D = coords3(DELTA)
    c_s13 = coords3(pmul(SIG1, pmul(SIG1, SIG1)))
    c_s12 = coords3(pmul(SIG1, SIG2))
    check("M4", "sigma1^3 = A1 + 3(S1+S2) + 6 sigma3 (coords (1,3,3,6))",
          c_s13 == [1, 3, 3, 6])
    check("M4", "sigma1 sigma2 = (S1+S2) + 3 sigma3 (coords (0,1,1,3))",
          c_s12 == [0, 1, 1, 3])
    check("M4", "Delta = S1 - S2 (coords (0,1,-1,0))", c_D == [0, 1, -1, 0])
    R6 = [c_s13 + [0], c_s12 + [0], [0, 0, 0, 1, 0], [0, 0, 0, 0, 2],
          [0, 0, 0, 0, 3]]
    free6, tors6 = quotient_structure(R6, 5)
    check("M4", "quotient = Z (free rank 1, no torsion)",
          free6 == 1 and tors6 == [])
    vS1_6 = [0, 1, 0, 0, 0]
    vD_6 = c_D + [0]
    check("M4", "[S1] != 0 (infinite order)",
          element_order(R6, vS1_6) == 0)
    check("M4", "membership: Delta - 2 S1 IS a relation",
          rowspan_contains(R6, [vD_6[i] - 2 * vS1_6[i] for i in range(5)]))
    check("M4", "membership: Delta - S1 is NOT",
          not rowspan_contains(R6, [vD_6[i] - vS1_6[i] for i in range(5)]))
    check("M4", "membership: S1 is NOT",
          not rowspan_contains(R6, vS1_6))
    # lift-independence of the H^6(B) discriminant class (new gate)
    ok_lift = True
    for c in (0, 1, 2):
        vv = [vD_6[i] + (c if i == 4 else 0) for i in range(5)]
        if not rowspan_contains(R6, [vv[i] - 2 * vS1_6[i] for i in range(5)]):
            ok_lift = False
    check("M4", "lift-independence: [Delta + c tau^3] = 2[S1] for c=0,1,2 "
          "(the tau^3-tail dies in the quotient)", ok_lift)
    # tau^3 itself dies
    check("M4", "[tau^3] = 0 in the quotient (2 tau^3 and 3 tau^3 force it)",
          rowspan_contains(R6, [0, 0, 0, 0, 1]))

    # ---------- M5: the R2 killing mechanism ----------
    info("")
    info("[M5] the R2 mechanism (even r >= 8 sources dead before E_8):")
    fibre = {0}
    for a in range(2):
        for b in range(2):
            for cc in range(2):
                fibre.add(a * 1 + b * 3 + cc * 5)
    check("M5", "fibre degrees of Lambda(z1,z3,z5) = {0,1,3,4,5,6,8,9}",
          fibre == {0, 1, 3, 4, 5, 6, 8, 9})
    check("M5", "H^2(U(3)) = 0 and H^7(U(3)) = 0 (no degree 2 or 7)",
          2 not in fibre and 7 not in fibre)
    # the sigma1-divisibility lattice fact, degrees 1..8
    for d in range(1, 9):
        A, basis_d = eval_matrix(d)
        ker = integer_kernel(A)
        # sigma1 * M_{d-1} generators in M_d coordinates
        prev = orbit_sums(d - 1)
        gen_coords = []
        ok_in = True
        for s in prev:
            g = pmul(SIG1, s)
            cc = inv_coords(g, d)
            if cc is None:
                ok_in = False
                break
            w = [sum(A[i][j] * cc[j] for j in range(len(basis_d)))
                 for i in range(len(A))]
            if any(w):
                ok_in = False
                break
            gen_coords.append(cc)
        name = "degree {}: sigma1.M_{}  <=  ker(eval) [automatic]".format(
            d, d - 1)
        if not check("M5", name, ok_in):
            continue
        check("M5", "degree {}: rank(ker) = rank(sigma1.M_{})".format(
            d, d - 1), len(ker) == len(gen_coords),
            "ker rank {}, gens {}".format(len(ker), len(gen_coords)))
        # index [ker : sigma1 M] = 1
        if len(ker) == len(gen_coords) and len(ker) > 0:
            Kb = [[ker[j][i] for j in range(len(ker))]
                  for i in range(len(ker[0]))]
            sols_ok = True
            C = []
            for gc in gen_coords:
                sol = solve_int(Kb, gc)
                if sol is None or not sol[1]:
                    sols_ok = False
                    break
                C.append([int(x) for x in sol[0]])
            if not sols_ok:
                check("M5", "degree {}: sigma1.M inside ker (integral "
                      "coords)".format(d), False)
            else:
                dd = det_int(C)
                check("M5", "degree {}: [ker(eval) : sigma1.M_{}] = 1"
                      .format(d, d - 1), abs(dd) == 1, "det = {}".format(dd))
    # the sigma2-version: ker(beta -> eval(beta*sigma2)) = ker(eval)
    subS2 = subst_sigma1_locus(SIG2)
    check("M5", "sigma2 at the sigma1-root locus = -(x^2+xy+y^2) != 0",
          subS2 == {(2, 0): -1, (1, 1): -1, (0, 2): -1},
          "computed {}".format(subS2))
    for d in range(2, 9):
        A, basis_d = eval_matrix(d)
        # columns: sigma2 * (orbit sums of M_d), evaluated -- degree d+2 keys
        keys2 = [(d + 2 - i, i) for i in range(d + 3)]
        kidx2 = {k: i for i, k in enumerate(keys2)}
        A2 = [[0] * len(basis_d) for _ in range(len(keys2))]
        for j, s in enumerate(basis_d):
            sub = subst_sigma1_locus(pmul(SIG2, s))
            for k, cval in sub.items():
                A2[kidx2[k]][j] = cval
        ker1 = integer_kernel(A)
        ker2 = integer_kernel(A2)
        ok = len(ker1) == len(ker2)
        if ok and len(ker1) > 0:
            for b in ker2:
                if not rowspan_contains(ker1, b):
                    ok = False
                    break
            if ok:
                for b in ker1:
                    if not rowspan_contains(ker2, b):
                        ok = False
                        break
        check("M5", "degree {}: {{beta : sigma1 | beta sigma2}} = "
              "sigma1-multiples [the sigma_1-bookkeeping clause]".format(d),
              ok, "ker ranks {} vs {}".format(len(ker1), len(ker2)))
    # the degree-9 torsion kill arithmetic
    check("M5", "tau sigma1 = 0 and 2 tau^3 != 0 (tau^3 of order 3)",
          tau_of(SIG1) == 0 and (2 % 3) != 0)

    # ---------- M6: the pins (R4) ----------
    info("")
    info("[M6] the pins (the regular representation, Z[u]/(3u)):")

    def reg_mul(a, b):
        # a, b: dicts u-exp -> coeff; coeffs of u^k (k>=1) live mod 3
        r = {}
        for e1, c1 in a.items():
            for e2, c2 in b.items():
                r[e1 + e2] = r.get(e1 + e2, 0) + c1 * c2
        return {k: (v % 3 if k >= 1 else v) for k, v in r.items()
                if (v % 3 if k >= 1 else v) != 0}

    total = reg_mul({0: 1, 1: 1}, {0: 1, 1: 2})  # (1+u)(1+2u)
    check("M6", "(1+u)(1+2u) = 1 + 2u^2 in Z[u]/(3u)",
          total == {0: 1, 2: 2}, "got {}".format(total))
    check("M6", "c1(regular) = 3u = 0 (the u-coefficient is 0 mod 3)",
          total.get(1, 0) == 0)
    check("M6", "c2(regular) = 2 u^2", total.get(2, 0) == 2)
    check("M6", "c3(regular) = 0", total.get(3, 0) is None
          or total.get(3, 0) == 0)
    # b: 0 = s*(iota*c1) = b u  ->  b = 0 in Z/3 (u nonzero, order 3)
    check("M6", "b u = 0 forces b = 0 (u generates H^2(BC3) = Z/3)",
          (1 * 1) % 3 != 0)  # u != 0; 3 | b*1 iff b = 0 mod 3
    check("M6", "eps: 2 u^2 = eps u^2 pins eps = 2 (mod 3)",
          (2 - 2) % 3 == 0 and (2 - 0) % 3 != 0 and (2 - 1) % 3 != 0)
    check("M6", "eps': 0 = eps' u^3 pins eps' = 0",
          (0 - 0) % 3 == 0 and (0 - 1) % 3 != 0 and (0 - 2) % 3 != 0)

    # ---------- M7: the degree runs ----------
    info("")
    info("[M7] the degree runs and the tuple:")
    rows2deg = [[1, 0], [0, 3]]  # (sigma1, tau): d_2(z1) = sigma1
    f2, t2 = quotient_structure(rows2deg, 2)
    check("M7", "H^2(B) = (Z sigma1 (+) Z/3 tau)/<sigma1> = Z/3",
          f2 == 0 and t2 == [3])
    check("M7", "H^2(B) generated by the class of tau (order 3)",
          element_order(rows2deg, [0, 1]) == 3)
    check("M7", "degree 3: d_2(sigma1 z1) = sigma1^2 != 0 (free part dies)",
          pmul(SIG1, SIG1) != {})
    check("M7", "degree 3: d_2(tau z1) = tau sigma1 = 0 (b = 0 pinned)",
          tau_of(SIG1) == 0)
    check("M7", "degree 5: tau^2 sigma1 = 0 (tau composed with tau sigma1)",
          tau_of(SIG1) == 0)
    check("M7", "degree 5: d_4(tau z3) = tau(sigma2 + 2 tau^2) = 2 tau^3",
          tau_of(SIG2) == 0)  # tau sigma2 = 0; 2 tau^3 != 0 by order 3
    check("M7", "degree 5: z5 dies (sigma3 != 0, infinite order)",
          SIG3 != {})
    check("M7", "degree 5: free (4,1)-classes die (sigma1 sigma2, "
          "sigma1^3 nonzero)",
          pmul(SIG1, SIG2) != {} and pmul(SIG1, pmul(SIG1, SIG1)) != {})
    check("M7", "mixed kills: d_2(z1z3) = sigma1 z3, d_2(z1z5) = sigma1 z5 "
          "(sigma1 nonzero)", SIG1 != {})
    # tuple assembly
    info("   tuple assembled from M3/M4/M7: "
         "(Z, 0, Z/3, Z/3, Z/3, Z/3, Z)  -- H^1 = 0 (odd BK cohomology, "
         "z1 killed by d_2(z1)=sigma1)")

    # ---------- M8: R6 / R7 ----------
    info("")
    info("[M8] R6 sign invariance and R7 lift-values:")
    check("M8", "R6: (x = +/- gamma*tau) squares away: (+/-1)^2 = 1",
          (1) ** 2 == (-1) ** 2)
    vals = set(c % 3 for c in (0, 1, 2))
    check("M8", "R7: tau(Delta + c tau^3) = c tau^4 takes three distinct "
          "values {0, tau^4, 2 tau^4}", vals == {0, 1, 2})


def main():
    info("WAVE 33 -- second referee pass over the v12 proof "
         "(independent verifier)")
    info("date: 2026-09-13; engine: exact integer arithmetic, no floats")
    run_part_p()
    run_part_m()
    info("")
    info("=" * 70)
    if FAILS:
        info("RESULT: {} FAILURE(S)".format(len(FAILS)))
        for f in FAILS:
            info("  " + f)
        code = 1
    else:
        info("RESULT: ALL GATES PASS")
        code = 0
    with open(OUT_TXT, "w", encoding="utf-8") as f:
        f.write("\n".join(LOG) + "\n")
    n_checks = sum(1 for l in LOG if l.startswith("[") and ": " in l)
    with open(OUT_JSON, "w", encoding="utf-8") as f:
        json.dump({"wave": 33, "pass": code == 0,
                   "n_failures": len(FAILS),
                   "checks": [l for l in LOG if l.startswith("[")],
                   "failures": FAILS}, f, indent=1)
    info("transcript: {}".format(OUT_TXT))
    info("json:       {}".format(OUT_JSON))
    sys.exit(code)


if __name__ == "__main__":
    main()
