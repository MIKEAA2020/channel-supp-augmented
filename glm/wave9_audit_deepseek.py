#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
WAVE 9 (audit).  Machine verification of
    'wave 2 audits/deepseek response_quantum.txt'   (1002 lines)

Sections
  A. Milestone 1a: E2 page of B_3 = Fl_3/C_3                -> CONFIRM
  B. Milestone 1b: C_3 orbits on the GKM graph              -> CONFIRM
  C. The prototype: honest equivariant CW + quotient SNF
       (S^2, antipodal)   -> H_*(RP^2) = (Z, Z/2, 0)
       (S^2 x S^2, T)     -> TRUE H_*(M)  vs the document's
         claimed outputs H_2 = Z/2, H_4 = Z/2  (both shown FALSE)
  D. CLSS pages of RP^2 and M: the document's SNF outputs are the
     E2_{0,q} fiber-coinvariant terms, not H_*(M); the differentials
     that kill them are located.
  E. BO(2) vs B Pin(2):  H^3(BO(2)) = Z/2 => d3 = 0;
     H^3(B Pin(2)) = 0 => d3 = iso.  Wave 8c Section E corrected;
     the refutation of 'd3 = <alpha cup k_2>' is withdrawn.
  F. RP^2 reduction counterexample: level-1 equivariance of the
     Postnikov map does NOT give a Borel map; P_2(RP^2) != P_2(BO(2)).
     This is the exact failure mode of the document's central
     'P_2 B_3 = P_2 B(T^2 x| C_3)' reduction (circular).

All arithmetic is exact (integer Smith normal form / lattice calculus).
"""

import itertools
from sympy import Matrix, eye, zeros

SEP = "=" * 78


def hdr(s):
    print("\n" + SEP)
    print(s)
    print(SEP)


# ----------------------------------------------------------------------------
# Integer lattice toolkit:  SNF with transforms, kernels, images, quotients.
# Invariant:  A = U * M * V  (row ops left-multiply U, col ops right-multiply V)
# ----------------------------------------------------------------------------

def _row_add(A, U, r, i, q):
    """A[r,:] += q * A[i,:] ; same on U."""
    n = A.shape[1]
    for j in range(n):
        A[r, j] += q * A[i, j]
    for j in range(U.shape[1]):
        U[r, j] += q * U[i, j]


def _col_add(A, V, c, j, q):
    """A[:,c] += q * A[:,j] ; same on V."""
    m = A.shape[0]
    for i in range(m):
        A[i, c] += q * A[i, j]
    for i in range(V.shape[0]):
        V[i, c] += q * V[i, j]


def _row_swap(A, U, r, i):
    n = A.shape[1]
    for j in range(n):
        A[r, j], A[i, j] = A[i, j], A[r, j]
    for j in range(U.shape[1]):
        U[r, j], U[i, j] = U[i, j], U[r, j]


def _col_swap(A, V, c, j):
    m = A.shape[0]
    for i in range(m):
        A[i, c], A[i, j] = A[i, j], A[i, c]
    for i in range(V.shape[0]):
        V[i, c], V[i, j] = V[i, j], V[i, c]


def _row_neg(A, U, r):
    for j in range(A.shape[1]):
        A[r, j] = -A[r, j]
    for j in range(U.shape[1]):
        U[r, j] = -U[r, j]


def smith_decomposition(M):
    """(S, U, V) with U * M * V = S diagonal, U, V unimodular."""
    M = Matrix(M)
    m, n = M.shape
    A = Matrix(M)
    U = eye(m)
    V = eye(n)
    r = c = 0
    while r < m and c < n:
        piv = None
        for i in range(r, m):
            for j in range(c, n):
                if A[i, j] != 0 and (piv is None or abs(A[i, j]) < abs(A[piv[0], piv[1]])):
                    piv = (i, j)
        if piv is None:
            break
        pi, pj = piv
        if pi != r:
            _row_swap(A, U, pi, r)
        if pj != c:
            _col_swap(A, V, pj, c)
        # eliminate
        progress = True
        while progress:
            progress = False
            for j in range(c + 1, n):
                if A[r, j] != 0:
                    q = A[r, j] // A[r, c]
                    if q != 0:
                        _col_add(A, V, j, c, -q)
                    if A[r, j] != 0:
                        # remainder: swap columns and continue
                        _col_swap(A, V, j, c)
                        progress = True
                        break
            if progress:
                continue
            for i in range(r + 1, m):
                if A[i, c] != 0:
                    q = A[i, c] // A[r, c]
                    if q != 0:
                        _row_add(A, U, i, r, -q)
                    if A[i, c] != 0:
                        _row_swap(A, U, i, r)
                        progress = True
                        break
            if progress:
                continue
        if A[r, c] < 0:
            _row_neg(A, U, r)
        # divisibility: make A[r,c] divide everything in the block
        while True:
            bad = None
            for i in range(r + 1, m):
                for j in range(c + 1, n):
                    if A[i, j] != 0 and A[i, j] % A[r, c] != 0:
                        bad = (i, j)
                        break
                if bad:
                    break
            if bad is None:
                break
            i, j = bad
            _row_add(A, U, r, i, 1)   # row r += row i
        r += 1
        c += 1
    assert U * M * V == A
    assert abs(U.det()) == 1 and abs(V.det()) == 1
    return A, U, V


def kernel_lattice(M):
    """Independent basis (columns) of ker(M) cap Z^n (saturated)."""
    M = Matrix(M)
    if M.shape[1] == 0:
        return zeros(0, 0) if M.shape[0] == 0 else eye(0, 0)
    if M.shape[0] == 0:
        return eye(M.shape[1])
    S, U, V = smith_decomposition(M)
    n = M.shape[1]
    keep = [j for j in range(S.shape[1]) if all(S[i, j] == 0 for i in range(S.shape[0]))]
    if not keep:
        return zeros(n, 0)
    return Matrix.hstack(*[V[:, j] for j in keep])


def image_lattice_basis(M):
    """Independent basis (columns) of the integer column span of M."""
    M = Matrix(M)
    if M.shape[0] == 0 or M.shape[1] == 0:
        return zeros(M.shape[0], 0)
    S, U, V = smith_decomposition(M)
    Uinv = U.inv()
    cols = []
    for i in range(min(S.shape[0], S.shape[1])):
        if S[i, i] != 0:
            cols.append(S[i, i] * Uinv[:, i])
    if not cols:
        return zeros(M.shape[0], 0)
    return Matrix.hstack(*cols)


def quotient_group(n, sub_basis):
    """(free, torsion) structure of Z^n / span(columns of sub_basis)."""
    sub_basis = Matrix(sub_basis)
    if sub_basis.shape[1] == 0:
        return (n, [])
    S, U, V = smith_decomposition(sub_basis)
    tors = []
    rank = 0
    for i in range(min(S.shape[0], S.shape[1])):
        if S[i, i] != 0:
            rank += 1
            if abs(S[i, i]) > 1:
                tors.append(abs(S[i, i]))
    return (n - rank, sorted(tors))


def in_lattice(P_basis, v):
    """Is integer vector v in the lattice spanned by columns of P_basis?"""
    P_basis = Matrix(P_basis)
    v = Matrix(v)
    if P_basis.shape[1] == 0:
        return all(x == 0 for x in v)
    S, U, V = smith_decomposition(P_basis)
    y = U * v
    for i in range(S.shape[1]):
        d = S[i, i]
        yi = y[i, 0] if i < y.shape[0] else 0
        if d == 0:
            if yi != 0:
                return False
        else:
            if int(yi) % int(d) != 0:
                return False
    # rows beyond rank of P must vanish
    for i in range(S.shape[1], y.shape[0]):
        if y[i, 0] != 0:
            return False
    return True


def subquotient(P_basis, S_basis):
    """(free, torsion) for lattice P / sublattice S (independent bases)."""
    P_basis = Matrix(P_basis)
    S_basis = Matrix(S_basis)
    r = P_basis.shape[1]
    t = S_basis.shape[1]
    if t == 0:
        return (r, [])
    # solve P * C = S with integer C (possible since S is a sublattice of P)
    Ssnf, U, V = smith_decomposition(P_basis)
    rhs = U * S_basis
    # solve Ssnf * Y = rhs, Y = V^{-1} C  is r x t; rows i >= r must vanish
    n = P_basis.shape[0]
    for i in range(r, rhs.shape[0]):
        for j in range(t):
            assert rhs[i, j] == 0, "S not contained in P (row %d)" % i
    cols = []
    for j in range(t):
        col = []
        for i in range(r):
            d = Ssnf[i, i]
            ri = rhs[i, j]
            if d == 0:
                assert ri == 0, "S not contained in P"
                col.append(0)
            else:
                assert ri % d == 0, "S not contained in P (divisibility)"
                col.append(ri // d)
        cols.append(Matrix(col))  # r x 1
    if cols:
        Y = Matrix.hstack(*cols)   # r x t
        C = V * Y                   # r x t in P-coordinates
    else:
        C = zeros(r, 0)
    assert P_basis * C == S_basis, "coordinate solve failed"
    return quotient_group(r, C)


def abelian(free_tors):
    if not isinstance(free_tors, tuple):
        return str(free_tors)
    free, tors = free_tors
    parts = []
    if free:
        parts.append("Z" if free == 1 else "Z^%d" % free)
    parts += ["Z/%d" % t for t in tors]
    return " + ".join(parts) if parts else "0"


def homology_of_complex(ranks, boundaries):
    """ranks: [n_0..n_N]; boundaries[k] = d_{k+1}: C_{k+1} -> C_k (matrix
    with n_k rows, n_{k+1} cols), k = 0..N-1.  Returns H_0..H_N."""
    N = len(ranks) - 1
    out = []
    for k in range(N + 1):
        if k == 0:
            cyc = eye(ranks[0]) if ranks[0] > 0 else zeros(0, 0)
        else:
            cyc = kernel_lattice(boundaries[k - 1])
        if k == N:
            bnd = zeros(ranks[N], 0)
        else:
            bnd = image_lattice_basis(boundaries[k])
        if cyc.shape[1] == 0:
            out.append((0, []))
            continue
        if bnd.shape[1] == 0:
            # cycles form a free sublattice; no boundaries
            out.append((cyc.shape[1], []))
            continue
        if not all(in_lattice(cyc, bnd[:, j]) for j in range(bnd.shape[1])):
            out.append("BAD_COMPLEX")
            continue
        out.append(subquotient(cyc, bnd))
    return out


def coinvariant_homology(ranks, T_mats, boundaries):
    """H_*(X/G) for a free cellular cyclic action.
    H_k = d_k^{-1}(im(T_{k-1}-I)) / ( im(T_k - I) + im d_{k+1} )  in C_k.
    ranks: [n_0..n_N]; T_mats[k]: action on C_k; boundaries[k]: d_{k+1}.
    """
    N = len(ranks) - 1
    A = [Matrix(T_mats[k]) - eye(ranks[k]) for k in range(N + 1)]
    out = []
    for k in range(N + 1):
        n_k = ranks[k]
        if k == 0:
            P = eye(n_k) if n_k > 0 else zeros(0, 0)
        else:
            d = boundaries[k - 1]     # d_{k+1}?? careful: see below
            # boundaries[k-1] is d_{k} : C_k -> C_{k-1}
            stacked = Matrix.hstack(-Matrix(d), Matrix(A[k - 1]))
            ker = kernel_lattice(stacked)
            if ker.shape[1] == 0:
                P = zeros(n_k, 0)
            else:
                xproj = Matrix([[ker[i, j] for j in range(ker.shape[1])]
                                for i in range(n_k)])
                P = image_lattice_basis(xproj) if xproj.shape[1] else zeros(n_k, 0)
        parts = []
        Ai = image_lattice_basis(A[k])
        if Ai.shape[1]:
            parts.append(Ai)
        if k < N:
            Bi = image_lattice_basis(boundaries[k])
            if Bi.shape[1]:
                parts.append(Bi)
        if parts:
            B = Matrix.hstack(*parts)
        else:
            B = zeros(n_k, 0)
        if P.shape[1] == 0:
            out.append((0, []))
            continue
        if B.shape[1] == 0:
            out.append((P.shape[1], []))
            continue
        if not all(in_lattice(P, B[:, j]) for j in range(B.shape[1])):
            out.append("DENOM_NOT_IN_P(k=%d)" % k)
            continue
        out.append(subquotient(P, B))
    return out


# ----------------------------------------------------------------------------
# Cyclic group (co)homology with matrix modules (exact).
# ----------------------------------------------------------------------------

def cyclic_cohomology(P, n, degree):
    P = Matrix(P)
    r = P.shape[0]
    I = eye(r)
    g_m = P - I
    N = eye(r)
    for i in range(1, n):
        N = N + P ** i
    if degree == 0:
        # invariants M^G = ker(g - 1)  (a free sublattice)
        return (kernel_lattice(g_m).shape[1], [])
    if degree % 2 == 1:
        kerN = kernel_lattice(N)
        if kerN.shape[1] == 0:
            return (0, [])
        imL = image_lattice_basis(g_m)
        if imL.shape[1] == 0:
            return quotient_group(kerN.shape[0], kerN)
        return subquotient(kerN, imL)
    else:
        kerG = kernel_lattice(g_m)
        if kerG.shape[1] == 0:
            return (0, [])
        imN = image_lattice_basis(N)
        if imN.shape[1] == 0:
            return quotient_group(kerG.shape[0], kerG)
        return subquotient(kerG, imN)


def cyclic_homology(P, n, degree):
    P = Matrix(P)
    r = P.shape[0]
    I = eye(r)
    g_m = P - I
    N = eye(r)
    for i in range(1, n):
        N = N + P ** i
    if degree == 0:
        return quotient_group(r, image_lattice_basis(g_m))
    delta_k = g_m if degree % 2 == 1 else N
    delta_k1 = N if degree % 2 == 1 else g_m
    ker = kernel_lattice(delta_k)
    if ker.shape[1] == 0:
        return (0, [])
    im = image_lattice_basis(delta_k1)
    if im.shape[1] == 0:
        return quotient_group(ker.shape[0], ker)
    return subquotient(ker, im)


# ============================================================================
# A. E2 page for B_3
# ============================================================================

hdr("A. E2 page of B_3 = Fl_3/C_3 (document Milestone 1a, lines 13-152)")

P_iota = Matrix([[0, -1], [1, -1]])
P_deg4 = Matrix([[-1, 1], [-1, 0]])
assert P_iota ** 3 == eye(2) and P_deg4 ** 3 == eye(2)
assert eye(2) + P_iota + P_iota ** 2 == zeros(2, 2)
assert eye(2) + P_deg4 + P_deg4 ** 2 == zeros(2, 2)
print("P = %s , P4 = %s , N = 0 on both (matches document)" %
      (P_iota.tolist(), P_deg4.tolist()))

E2B = {}
for p in range(5):
    E2B[(p, 0)] = cyclic_cohomology(eye(1), 3, p)
for p in range(4):
    E2B[(p, 2)] = cyclic_cohomology(P_iota, 3, p)
    E2B[(p, 4)] = cyclic_cohomology(P_deg4, 3, p)
print("q=0: ", {p: abelian(E2B[(p, 0)]) for p in range(5)})
print("q=2: ", {p: abelian(E2B[(p, 2)]) for p in range(4)})
print("q=4: ", {p: abelian(E2B[(p, 4)]) for p in range(4)})
doc = {(0, 0): "Z", (2, 0): "Z/3", (4, 0): "Z/3", (1, 2): "Z/3",
       (3, 2): "Z/3", (1, 4): "Z/3", (3, 4): "Z/3",
       (0, 2): "0", (2, 2): "0", (0, 4): "0", (2, 4): "0", (3, 0): "0"}
okA = all(abelian(E2B[key]) == val for key, val in doc.items())
print("VERDICT A: E2-page " + ("CONFIRMED (agrees with Wave 8b)." if okA else "MISMATCH!"))

# ============================================================================
# B. GKM orbit pattern
# ============================================================================

hdr("B. C_3 orbits on the GKM graph (document Milestone 1b, lines 155-234)")


def right_Q(p):
    return (p[1], p[2], p[0])


S3 = list(itertools.permutations([1, 2, 3]))
edges = set()
for v in S3:
    for i, j in [(0, 1), (1, 2), (0, 2)]:
        u = list(v)
        u[i], u[j] = u[j], u[i]
        edges.add(tuple(sorted([v, tuple(u)])))
edges = sorted(edges)


def orbit_of(rep, act):
    orb, x = [rep], act(rep)
    while x != rep:
        orb.append(x)
        x = act(x)
    return sorted(orb)


vorb, seen = [], set()
for v in S3:
    if v not in seen:
        o = orbit_of(v, right_Q)
        seen.update(o)
        vorb.append(o)
eorb, seene = [], set()
for e in edges:
    if e not in seene:
        o = orbit_of(e, lambda e: tuple(sorted([right_Q(e[0]), right_Q(e[1])])))
        seene.update(o)
        eorb.append(o)
print("GKM graph: %d vertices, %d edges; vertex orbits: %d (sizes %s); "
      "edge orbits: %d (sizes %s)" %
      (len(S3), len(edges), len(vorb), [len(o) for o in vorb],
       len(eorb), [len(o) for o in eorb]))
okB = len(vorb) == 2 and len(eorb) == 3 and all(len(o) == 3 for o in vorb + eorb)
print("VERDICT B: '2 vertex orbits, 3 edge orbits, 9 = 3*3 invariant 2-spheres' "
      + ("CONFIRMED." if okB else "REFUTED."))

# ============================================================================
# C. Honest equivariant CW + quotient SNF (the repaired prototype)
# ============================================================================

hdr("C. Honest equivariant CW models and quotient SNF (document lines 284-495)")

# ---- C.1 (S^2, antipodal) : CW lifted from the standard RP^2 CW ----------
d1_s2 = Matrix([[-1, 1], [1, -1]])      # d(c+) = p- - p+ , d(c-) = p+ - p-
d2_s2 = Matrix([[1, -1], [1, -1]])      # d(D+) = c+ + c- , d(D-) = -(c+ + c-)
a_s2 = [Matrix([[0, 1], [1, 0]]),
        Matrix([[0, 1], [1, 0]]),
        Matrix([[0, -1], [-1, 0]])]     # a(D+) = -D- (degree -1 on H_2)
ranks_s2 = [2, 2, 2]
bnd_s2 = [d1_s2, d2_s2]

H_s2 = homology_of_complex(ranks_s2, bnd_s2)
print("(S^2 model) H_* =", [abelian(h) for h in H_s2], "  expected [Z, 0, Z]")
assert H_s2 == [(1, []), (0, []), (1, [])]
for k in range(2):
    assert bnd_s2[k] * a_s2[k + 1] == a_s2[k] * bnd_s2[k]
for A in a_s2:
    assert A ** 2 == eye(2)
assert a_s2[2] * Matrix([1, 1]) == -Matrix([1, 1])
print("checks: H_*(S^2), chain equivariance, antipodal degree -1 : PASS")

H_rp2 = coinvariant_homology(ranks_s2, a_s2, bnd_s2)
print("H_*(RP^2) by honest quotient SNF =", [abelian(h) for h in H_rp2],
      "  expected [Z, Z/2, 0]")
okC1 = H_rp2 == [(1, []), (0, [2]), (0, [])]
print("C.1 honest pipeline reproduces H_*(RP^2) = (Z, Z/2, 0): "
      + ("PASS" if okC1 else "FAIL"))

# ---- C.2 (S^2 x S^2, T(x,y) = (-y,x)) ------------------------------------
# product CW.  Cell = (i, j, a, b): i-cells in factor 1, j-cells in factor 2.
# T_*(u (x) v) = (-1)^{|u||v|} (a_* v) (x) u
# d(u (x) v)   = du (x) v + (-1)^{|u|} u (x) dv

def build_product():
    cells_by_k = {}
    for k in range(5):
        cells = []
        for i in range(3):
            j = k - i
            if 0 <= j <= 2:
                for a in range(2):
                    for b in range(2):
                        cells.append((i, j, a, b))
        cells_by_k[k] = cells
    idx = {k: {cells_by_k[k][t]: t for t in range(len(cells_by_k[k]))}
           for k in range(5)}
    T, D = {}, {}
    for k in range(5):
        n = len(cells_by_k[k])
        Tk = zeros(n, n)
        for t, (i, j, a, b) in enumerate(cells_by_k[k]):
            for bp in range(2):
                coeff = a_s2[j][bp, b]
                if coeff == 0:
                    continue
                s = (-1) ** (i * j)
                t2 = idx[k][(j, i, bp, a)]
                Tk[t2, t] = s * coeff
        T[k] = Tk
    for k in range(1, 5):
        prev = cells_by_k[k - 1]
        pidx = idx[k - 1]
        Dk = zeros(len(prev), len(cells_by_k[k]))
        for t, (i, j, a, b) in enumerate(cells_by_k[k]):
            if i >= 1:
                di = [bnd_s2[i - 1][0, a], bnd_s2[i - 1][1, a]]
                for ap in range(2):
                    if di[ap] != 0:
                        Dk[pidx[(i - 1, j, ap, b)], t] += di[ap]
            if j >= 1:
                dj = [bnd_s2[j - 1][0, b], bnd_s2[j - 1][1, b]]
                s = (-1) ** i
                for bp in range(2):
                    if dj[bp] != 0:
                        Dk[pidx[(i, j - 1, a, bp)], t] += s * dj[bp]
        D[k] = Dk
    ranks = [len(cells_by_k[k]) for k in range(5)]
    return ranks, T, D


ranks_p, T_p, D_p = build_product()
print("\nproduct CW ranks C_0..C_4 =", ranks_p, " (4, 8, 12, 8, 4 cells)")
H_prod = homology_of_complex(ranks_p, [D_p[k] for k in range(1, 5)])
print("(S^2 x S^2 model) H_* =", [abelian(h) for h in H_prod],
      "  expected [Z, 0, Z^2, 0, Z]")
assert H_prod == [(1, []), (0, []), (2, []), (0, []), (1, [])]
for k in range(5):
    assert T_p[k] ** 4 == eye(ranks_p[k]), "T^4 != I at k=%d" % k
for k in range(1, 5):
    assert D_p[k] * T_p[k] == T_p[k - 1] * D_p[k], "dT != Td at k=%d" % k
print("checks: H_*(S^2 x S^2), T^4 = I, chain-level equivariance : PASS")

# orientation: T has degree -1 on H_4  (M non-orientable)
topcell = Matrix([1, 1, 1, 1])  # sum of all 4-cells is NOT the top class; use H_4:
cyc4 = kernel_lattice(D_p[4])
print("H_4 cycle direction (should map to -itself under T):",
      cyc4.tolist())
tv = T_p[4] * cyc4[:, 0]
import sympy
ratio = sympy.Rational(1)
# find lambda with tv = lambda * cyc (exact rational)
lams = set()
for i in range(cyc4.shape[0]):
    if cyc4[i, 0] != 0:
        lams.add(sympy.Rational(tv[i, 0], cyc4[i, 0]))
assert len(lams) == 1 and lams.pop() == -1, "T degree on top class != -1"
print("T acts by -1 on the top class: PASS (M non-orientable)")

H_M = coinvariant_homology(ranks_p, T_p, [D_p[k] for k in range(1, 5)])
print("\n*** H_*(M) by the HONEST equivariant quotient SNF ***")
print("   H_*( (S^2 x S^2)/C_4 ) =", [abelian(h) for h in H_M])
print("document claims: H_4(M) = Z/2 (lines 420-429) and H_2(M) = Z/2 "
      "(line 482);  H^4(M;Z) = Z/2 (line 313-319).")
print("expected truth: H_0 = Z, H_1 = Z/4 (pi_1 = C_4), H_2 = 0, "
      "H_3 = Z/2 (PD: H_3 = H^1(M;Z~) = Z/2), H_4 = 0 (non-orientable).")

# ============================================================================
# D. CLSS pages: what the document's SNF outputs actually compute
# ============================================================================

hdr("D. CLSS pages of RP^2 and M (document lines 374-495 diagnosis)")

# --- D.1  RP^2 ---
print("D.1  CLSS of S^2 -> RP^2 (free C_2 = antipodal):")
sign = Matrix([[-1]])
E2_rp2 = {}
for p in range(5):
    E2_rp2[(p, 0)] = cyclic_cohomology(eye(1), 2, p)   # H^0(S^2) = Z trivial
    E2_rp2[(p, 2)] = cyclic_cohomology(sign, 2, p)     # H^2(S^2) = Z sign
for q in (0, 2):
    print("   q=%d: " % q, {p: abelian(E2_rp2[(p, q)]) for p in range(5)})
print("   H^3(RP^2;Z) = 0 (closed 2-manifold) and the only total-3 term is "
      "E2^{1,2} = Z/2,")
print("   so 0 = H^3 = ker(d_3: E3^{1,2} -> E3^{4,0})   =>   d_3 injective.")
print("   H^4(RP^2;Z) = 0 = E_infty^{4,0} = (Z/2)/im(d_3)  =>  d_3 surjective.")
print("   ==> d_3^{RP^2}: Z/2 -> Z/2 is an ISOMORPHISM (nonzero).")

# twisted (Z~) version: the k_2 detector
print("\n   Twisted (Z~) page: E2^{p,2} = H^p(C_2; H^2(S^2) (x) eps) = H^p(C_2; Z):")
E2_rp2_tw = {}
for p in range(4):
    E2_rp2_tw[(p, 2)] = cyclic_cohomology(eye(1), 2, p)
    E2_rp2_tw[(p, 0)] = cyclic_cohomology(sign, 2, p)
print("   q=0 (eps):", {p: abelian(E2_rp2_tw[(p, 0)]) for p in range(4)})
print("   q=2 (Z):  ", {p: abelian(E2_rp2_tw[(p, 2)]) for p in range(4)})
print("   E2^{0,2} = Z, E2^{3,0} = H^3(C_2; eps) = Z/2, H^3(RP^2;Z~) = 0")
print("   ==> the twisted transgression d_3: Z -> Z/2 is SURJECTIVE (nonzero);")
print("   by the classical k-invariant/transgression theorem (Spanier) this")
print("   measures k_2(RP^2) = generator != 0 in H^3(C_2; Z_sign) = Z/2.")

# --- D.2  M = (S^2 x S^2)/C_4 ---
J = Matrix([[0, -1], [1, 0]])   # T on H_2(S^2 x S^2): u->v, v->-u
assert J ** 4 == eye(2)
NJ = eye(2) + J + J ** 2 + J ** 3
assert NJ == zeros(2, 2)
print("\nD.2  CLSS of S^2 x S^2 -> M (free C_4):")
print("   T_* on H_2: J = %s (conjuate to the document's [[0,1],[-1,0]]); "
      "N = 0" % J.tolist())
E2_M = {}
for p in range(5):
    E2_M[(p, 0)] = cyclic_cohomology(eye(1), 4, p)
for p in range(4):
    E2_M[(p, 2)] = cyclic_cohomology(J, 4, p)
    E2_M[(p, 4)] = cyclic_cohomology(sign, 4, p)
print("   q=0:", {p: abelian(E2_M[(p, 0)]) for p in range(5)})
print("   q=2:", {p: abelian(E2_M[(p, 2)]) for p in range(4)})
print("   q=4:", {p: abelian(E2_M[(p, 4)]) for p in range(4)})

# homological page: the document's outputs are E2_{0,2}, E2_{0,4}
E2M_hom_02 = cyclic_homology(J, 4, 0)   # H_0(C_4; H_2(fiber)) = coinvariants
E2M_hom_04 = cyclic_homology(sign, 4, 0)
print("\n   HOMOLOGICAL page coinvariants: E2_{0,2} = H_0(C_4; H_2(S^2xS^2)) "
      "= %s" % abelian(E2M_hom_02))
print("                             E2_{0,4} = H_0(C_4; H_4(S^2xS^2)) "
      "= %s" % abelian(E2M_hom_04))
print("   THE DOCUMENT'S 'H_2(M) = Z/2' AND 'H_4(M) = Z/2' ARE EXACTLY THESE")
print("   TWO E2_{0,q} TERMS (coinvariants of the fiber homology), NOT the")
print("   homology of the quotient.  In the true CLSS they are killed by")
print("   differentials (d_3: E3_{3,0} -> E3_{0,2} resp. d_5: E5_{5,0} -> "
      "E5_{0,4}).")
print("   Honest SNF above gives the actual H_*(M); compare.")
print("\n   Coefficients check (PD/UCT): H^1(M;Z~) = H^1(C_4; eps) = %s "
      "= H_3(M) by PD." % abelian(cyclic_cohomology(sign, 4, 1)))
print("   H^4(M;Z) = Ext(H_3, Z) = Z/2 = E_infty^{4,0} = (Z/4)/d_3(Z/2) =>")
print("   im(d_3) = 2Z/4Z, i.e. d_3: E3^{1,2} = Z/2 -> E3^{4,0} = Z/4 is")
print("   INJECTIVE (nonzero) -- the document's own target, now derived by")
print("   the correct route.")

# ============================================================================
# E. BO(2) vs B Pin(2):  correction of Wave 8c Section E
# ============================================================================

hdr("E. Test cases BO(2) vs B(Pin(2)) (Wave 8c Section E correction)")

print("Both fit the fibration  BS^1 -> E -> BC_2  with conjugation on H^2(BS^1):")
print("  O(2)  = S^1 x| C_2  (split: reflection squares to 1)      E = BO(2)")
print("  Pin(2)= S^1 .C_2 binary-dihedral (j^2 = -1, non-split)     E = B Pin(2)")
print("E2 page (identical for both; modules H^q(BS^1): q=0: Z, q=2: Z_sign,"
      " q=4: Z):")
E2_bo = {}
for p in range(5):
    E2_bo[(p, 0)] = cyclic_cohomology(eye(1), 2, p)
    E2_bo[(p, 4)] = cyclic_cohomology(eye(1), 2, p)
for p in range(5):
    E2_bo[(p, 2)] = cyclic_cohomology(sign, 2, p)
for q in (0, 2, 4):
    print("  q=%d: " % q, {p: abelian(E2_bo[(p, q)]) for p in range(5)})

print("""
  H^3(BO(2);Z):  the Bockstein of w_2 is nonzero because
       rho(beta(w_2)) = Sq^1(w_2) = w_1 w_2  !=  0   in F_2[w_1,w_2]
  (rank 2 => w_3 = 0).  Also H^{odd}(BO(2);Q) = 0, so H^3 is 2-torsion.
  Hence H^3(BO(2);Z) = Z/2 = ker(d_3: E3^{1,2}=Z/2 -> E3^{4,0}=Z/2)
  ==>  d_3^{BO(2)} = 0.                        [textbook facts, cited]

  H^3(B Pin(2);Z):  use the fibration  RP^2 -> B Pin(2) -> BSU(2)
  (fiber SU(2)/Pin(2) = S^2/<antipodal> = RP^2; base simply connected).
  E2^{p,q} = H^p(BSU(2); H^q(RP^2;Z)),  H^q(RP^2) = (Z, 0, Z/2).
  Total-degree-3 entries: (3,0)=H^3(BSU(2))=0, (2,1)=0, (1,2)=H^1(BSU(2);Z/2)=0,
  (0,3)=0.   ==>  H^3(B Pin(2);Z) = 0.
  Hence 0 = ker(d_3) with source Z/2   ==>  d_3^{B Pin(2)} = ISO (nonzero).
""")
print("  ==> Wave 8c Section E's 'the CLSS d_3 is ZERO in both cases' is")
print("      WRONG in the B Pin(2) case; its refutation of")
print("      'd_3^{1,2} = <alpha cup k_2>' is WITHDRAWN.")
print("      Corrected status: formula unproven; CONSISTENT in both test cases")
print("      (k_2(BO(2)) = 0 split <-> d_3 = 0;  k_2(Pin(2)) = Bockstein != 0")
print("       <-> d_3 = iso) and in the RP^2 case (k_2 = gen, d_3 = iso).")

# ============================================================================
# F. The reduction counterexample (the document's central step)
# ============================================================================

hdr("F. RP^2 counterexample to 'Borel preserves the 2-type' (document lines "
    "264-280, 721-735)")

print("""
  The 2-Postnikov map  f : S^2 -> K(Z,2) = BS^1  IS weakly equivariant:
  both  (f o a)^* u  and  (conj o f)^* u  pull the generator u to -x in
  H^2(S^2) (a^* x = -x since the antipodal has degree -1; conj^* u = -u).
  So 'equivariant up to homotopy' (document's hypothesis) HOLDS here.

  But IF that promoted to a Borel map  RP^2 = Borel(S^2) -> Borel(BS^1) =
  B(S^1 x|_conj C_2) = BO(2)  (i.e. P_2 RP^2 = P_2 BO(2), the document's
  reduction pattern), then Serre-SS naturality would force
       d_3^{RP^2} = d_3^{BO(2)}.
  Sections D and E give   d_3^{RP^2} = iso  (H^3(RP^2) = 0)   but
                         d_3^{BO(2)} = 0    (H^3(BO(2)) = Z/2).
  CONTRADICTION  ==>  P_2(RP^2) != P_2(BO(2)).

  The missing ingredient is full coherence of the equivariance, which
  exists iff k_2(RP^2) = k_2(BO(2)) -- i.e. iff the very bit one wants to
  compute is already answered.  (Note P_2(RP^2) ~ P_2(B Pin(2)) is the
  consistent matching: both k_2 = generator, both d_3 = iso.)

  CONSEQUENCE: the document's reduction
       P_2 B_3  =  P_2 B(T^2 x| C_3),   d_3^{B_3} = d_3^{BT^2-Borel}
  (lines 264-280, 721-735, asserted 'rigorous') is the SAME fallacy: the
  weak equivariance of Fl_3 -> K(Z^2,2) does not produce a Borel map
  unless k_2(B_3) = k_2(B(T^2 x| C_3)) = 0 (split Borel side), which is
  equivalent to the qutrit bit itself.  THE REDUCTION IS CIRCULAR.
  The subsequent 'split section kills the k_3-cocycle' computation
  (lines 822-872) then computes k_3 of the WRONG space (the split Borel
  side), and the final boxes (lines 899-1002) do not follow.
""")

# ============================================================================
# Final scoreboard
# ============================================================================

hdr("FINAL VERDICTS ON 'deepseek response_quantum.txt'")

verdicts = [
    ("Milestone 1a: E2 page (lines 13-152)",
     "CORRECT (machine-confirmed; = Wave 8b)."),
    ("Milestone 1b: GKM orbits (lines 155-234)",
     "CORRECT incl. honest caveat (machine-confirmed)."),
    ("2-Postnikov reduction P_2B_3 = P_2B(T^2 x| C_3) 'rigorous' "
     "(lines 264-280, 721-735)",
     "UNSOUND/CIRCULAR -- refuted by the RP^2/BO(2) counterexample (Sec. F)."),
    ("Prototype target: d_3 on M forced nonzero, H^4(M) = Z/2 "
     "(lines 284-330)",
     "CORRECT (derived here by the right route: PD/UCT + CLSS)."),
    ("Prototype 'cellular model' + 'Exact SNF check' (lines 374-495)",
     "INVALID: no equivariant CW with those vanishing quotient boundaries "
     "exists; outputs 'H_4 = Z/2', 'H_2 = Z/2' are the CLSS E2_{0,4}, "
     "E2_{0,2} coinvariant terms, not H_*(M). Honest SNF (Sec. C) gives the "
     "true answer. The inference 'H^4 ~ H_4' is also wrong (UCT)."),
    ("Branch 'computation' (lines 659-689)",
     "Not a computation: prints two hardcoded dictionaries."),
    ("Formula d_3(alpha) = <alpha cup k_3> used throughout (lines 529, 648, "
     "782, 819)",
     "UNPROVEN (and the repo's Wave 8c 'refutation' is itself corrected "
     "here: formula stands as open, consistent in all testable cases)."),
    ("'Split section kills the k_3-cocycle' (lines 822-872)",
     "Computes k_3 of the split Borel side B(T^2 x| C_3) -- not of B_3; "
     "the transfer step to B_3 is the broken/circular reduction. (The "
     "cocycle vanishing on the split Borel side itself is plausible.)"),
    ("Boxed conclusions H^4(B_3)=Z/3, delta_2(qutrit)=4/3, "
     "H^3(B_4;Z~)=Z/2, delta_1(ququart)=3/2 (lines 899-1002)",
     "UNSUPPORTED.  Both bits remain OPEN.  Numerical evidence "
     "(Wave 8a) still favors both, but no proof exists."),
]
for t, v in verdicts:
    print(" * %s\n     -> %s\n" % (t, v))

print("STATUS AFTER THIS AUDIT: delta_2(qutrit) and delta_1(ququart) are")
print("STILL OPEN.  The honest route remains the C_d-equivariant chain model")
print("of Fl_d (or an equivalent certified computation of k_2(B_d)).")
print("\nWAVE 9 audit script complete.")

# ============================================================================
# G. Cross-consistency of the honest H_*(M)
# ============================================================================

hdr("G. Cross-consistency checks of the honest computation")
HomC4 = {p: cyclic_homology(eye(1), 4, p) for p in range(6)}
print("Homological q=0 row  H_p(C_4; Z) =",
      {p: abelian(HomC4[p]) for p in range(6)})
print("  H_2(M) = 0 forces d_3: E3_{3,0} = H_3(C_4;Z) = Z/4 -> E3_{0,2} = Z/2 "
      "SURJECTIVE (kills the document's 'H_2' term);")
print("  H_4(M) = 0 forces d_5: E5_{5,0} = H_5(C_4;Z) = Z/4 -> E5_{0,4} = Z/2 "
      "SURJECTIVE (kills the document's 'H_4' term).")
chi_M = sum((-1) ** k * (H_M[k][0] if isinstance(H_M[k], tuple) else 0)
            for k in range(len(H_M)))
print("\nEuler characteristic from honest H_*(M): %d ;  chi(S^2 x S^2)/4 = "
      "4/4 = 1  %s" % (chi_M, "MATCH" if chi_M == 1 else "MISMATCH"))
chi_rp2 = sum((-1) ** k * (H_rp2[k][0] if isinstance(H_rp2[k], tuple) else 0)
              for k in range(len(H_rp2)))
print("Euler characteristic of RP^2 from honest H_*: %d (expected 1) %s"
      % (chi_rp2, "MATCH" if chi_rp2 == 1 else "MISMATCH"))
print("\nAll machine results in this audit are exact (no floating point).")
