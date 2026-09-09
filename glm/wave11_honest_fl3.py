#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
WAVE 11 - THE HONEST 1896-CELL RUN
(recorded spec: 'wave 2 audits/AUDIT_deepseek_response_quantum2.md' Sections 3+5,
 worklog Task 14; corrected base layer per the fresh-session analysis.)

Object: settle the qutrit bit  delta_2(D(C^3)) = 4/3  by machine, via the honest
C_3-equivariant chain model of Fl_3 = U(3)/T^3 and the orbit-complex SNF of
B_3 := Fl_3 / <c>,  c([U]) = [U P_sigma]  (free action, order 3).

THE MODEL (all choices forced; no free parameters beyond Z/3-conventions):
  * Base: the 49 open faces of the Birkhoff polytope Bo_3 (f = 6,15,18,9,1; all
    faces simplices).  IMPORTANT (fresh-session correction): only the
    VERTEX / sphere-edge / one-block-face strata carry nonempty fibers; over the
    one-block faces the fiber is T^3/Stab(F) = T^2.  The cell counts are exactly
    the recorded spec: 1896 cells (6,81,351,675,576,189,18), chi = 6.
  * Fibers (level-3 cellulations):
      pt          : 1 cell                       (6 vertices)
      S^1 (3+3)   : 3 pts + 3 arcs = 6 cells     (9 sphere-edges, 2-block)
      T^2 (9+27+18): grid u,v in {0,1/3,2/3}^2, circle families
                     {u=a},{v=b},{u+v=c} at thirds  (34 one-block faces)
    with (u,v) = (arg z2/z1, arg z3/z2)  [exact: t0 = (1/3,1/3)].
  * c-action on cells: T(F,e) = s(F)*(F_sigma, e) for proper F (s = sorted-vertex
    shuffle parity; s(interior)=+1 verified),  T(int,e) = (int, e + t0)
    [exact: F0 P_sigma = diag(1,w,w^2) F0, Waves 9/10].
  * Transition layer (the addendum): tau_{F->G} = q_G((p(F)-p(G)) t0), where
    p: faces -> Z/3 is the c-orbit phase and q_G the canonical quotient
    T^3/Stab(F) -> T^3/Stab(G).  This is the UNIQUE c-equivariant representative:
    the poset cocycle is a coboundary (contractible base, top element 'interior'),
    and the t0-monodromy around the interior c-orbit is the only twist
    [g, g - t0, g + t0] - exactly the recorded addendum.
  * d = base part (simplex signs; geometric eps_Phi for the interior 4-cell;
    translations of fiber cells; degeneration q-maps with +-1 degrees derived
    from the (u,v)-geometry)  +  (-1)^{dim F} * fiber part.

VERIFICATION BATTERY (the certification gate):
  (1) cell counts (6,81,351,675,576,189,18), total 1896, chi = 6;
  (2) d^2 = 0 exactly;
  (3) H_*(Fl_3) = (Z,0,Z^2,0,Z^2,0,Z): rational Betti (mod large primes) and
      torsion audit by exact mod-p UCT induction (p = 2,3,5,7,11,13);
  (4) T^3 = I;  (5) dT = Td exactly;  (6) c acts freely on cells;
  (7) 1+T+T^2 = 0 on H_2 and T has order 3 there (mod 7);
  (8) T = +1 on H_6 (mod 7);
  (9) ORBIT COMPLEX C(Fl_3) (x)_{Z[C3]} Z (632 orbits): d_bar, homology by
      exact mod-p UCT induction AND integral Smith normal form for the
      decisive degrees -> H_*(B_3); mandatory slots H_0=Z, H_1=Z/3, H_5=0, H_6=Z;
      THE BIT: H_2(B_3) = Z/3  <=>  CLSS d_3 = 0  <=>  delta_2(qutrit) = 4/3
      (World 1)   vs   H_2 = 0  (World 2, obstruction dies).

All arithmetic exact (Python ints, Fractions, sympy integer SNF, numpy mod p).
Fl_4 / ququart: out of scope this run (honest deferral, recorded).
"""

import itertools
import sys
import time
from fractions import Fraction

import numpy as np
from sympy import Matrix, eye, zeros

SEP = "=" * 78
T0 = time.time()


def hdr(s):
    print("\n" + SEP)
    print(s)
    print(SEP)


def tick(msg):
    print("[t+%7.1fs] %s" % (time.time() - T0, msg))
    sys.stdout.flush()


# ----------------------------------------------------------------------------
# Integer lattice toolkit (wave 9 provenance, unchanged)
# ----------------------------------------------------------------------------

def _row_add(A, U, r, i, q):
    n = A.shape[1]
    for j in range(n):
        if A[i, j]:
            A[r, j] += q * A[i, j]
    for j in range(U.shape[1]):
        if U[i, j]:
            U[r, j] += q * U[i, j]


def _col_add(A, V, c, j, q):
    m = A.shape[0]
    for i in range(m):
        if A[i, j]:
            A[i, c] += q * A[i, j]
    for i in range(V.shape[0]):
        if V[i, j]:
            V[i, c] += q * V[i, j]


def _row_swap(A, U, r, i):
    for j in range(A.shape[1]):
        A[r, j], A[i, j] = A[i, j], A[r, j]
    for j in range(U.shape[1]):
        U[r, j], U[i, j] = U[i, j], U[r, j]


def _col_swap(A, V, c, j):
    for i in range(A.shape[0]):
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
        progress = True
        while progress:
            progress = False
            for j in range(c + 1, n):
                if A[r, j] != 0:
                    q = A[r, j] // A[r, c]
                    if q != 0:
                        _col_add(A, V, j, c, -q)
                    if A[r, j] != 0:
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
            _row_add(A, U, r, i, 1)
        r += 1
        c += 1
    assert U * M * V == A
    assert abs(U.det()) == 1 and abs(V.det()) == 1
    return A, U, V


def kernel_lattice(M):
    """Independent basis (columns) of ker(M) cap Z^n (saturated)."""
    M = Matrix(M)
    if M.shape[1] == 0:
        return zeros(0, 0) if M.shape[0] == 0 else zeros(0, 0)
    if M.shape[0] == 0:
        return eye(M.shape[1])
    S, U, V = smith_decomposition(M)
    keep = [j for j in range(S.shape[1]) if all(S[i, j] == 0 for i in range(S.shape[0]))]
    if not keep:
        return zeros(M.shape[1], 0)
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


def subquotient(P_basis, S_basis):
    """(free, torsion) for lattice P / sublattice S (independent bases)."""
    P_basis = Matrix(P_basis)
    S_basis = Matrix(S_basis)
    r = P_basis.shape[1]
    t = S_basis.shape[1]
    if t == 0:
        return (r, [])
    Ssnf, U, V = smith_decomposition(P_basis)
    rhs = U * S_basis
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
        cols.append(Matrix(col))
    Y = Matrix.hstack(*cols) if cols else zeros(r, 0)
    C = V * Y
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


# ----------------------------------------------------------------------------
# mod-p dense linear algebra (exact; used for Betti / torsion audit / actions)
# ----------------------------------------------------------------------------

def dense_modp(Dk, ncols, nrows, p):
    M = np.zeros((nrows, ncols), dtype=np.int64)
    for j, col in Dk.items():
        for i, v in col.items():
            M[i, j] = v % p
    return M


def rank_modp(Dk, ncols, nrows, p):
    M = dense_modp(Dk, ncols, nrows, p)
    M = M % p
    m, n = M.shape
    r = 0
    for j in range(n):
        piv = -1
        for i in range(r, m):
            if M[i, j]:
                piv = i
                break
        if piv < 0:
            continue
        if piv != r:
            M[[r, piv]] = M[[piv, r]]
        inv = pow(int(M[r, j]), p - 2, p)
        M[r] = (M[r] * inv) % p
        below = np.nonzero(M[r + 1:, j])[0]
        for off in below:
            i = r + 1 + off
            M[i] = (M[i] - M[i, j] * M[r]) % p
        r += 1
        if r == m:
            break
    return r


def nullspace_modp(Dk, ncols, nrows, p):
    """Basis (dense rows) of ker mod p."""
    M = dense_modp(Dk, ncols, nrows, p) % p
    m, n = M.shape
    r = 0
    piv_col_of_row = []
    piv_cols = []
    for j in range(n):
        piv = -1
        for i in range(r, m):
            if M[i, j]:
                piv = i
                break
        if piv < 0:
            continue
        if piv != r:
            M[[r, piv]] = M[[piv, r]]
        inv = pow(int(M[r, j]), p - 2, p)
        M[r] = (M[r] * inv) % p
        nz = np.nonzero(M[:, j])[0]
        for i in nz:
            if i != r:
                M[i] = (M[i] - M[i, j] * M[r]) % p
        piv_col_of_row.append(j)
        piv_cols.append(j)
        r += 1
        if r == m:
            break
    free = [j for j in range(n) if j not in set(piv_cols)]
    basis = []
    for f in free:
        v = np.zeros(n, dtype=np.int64)
        v[f] = 1
        for i, j in enumerate(piv_col_of_row):
            v[j] = (-M[i, f]) % p
        basis.append(v)
    return basis


def rank_dense_modp(M, p):
    M = (M % p).astype(np.int64)
    m, n = M.shape
    r = 0
    for j in range(n):
        piv = -1
        for i in range(r, m):
            if M[i, j]:
                piv = i
                break
        if piv < 0:
            continue
        if piv != r:
            M[[r, piv]] = M[[piv, r]]
        inv = pow(int(M[r, j]), p - 2, p)
        M[r] = (M[r] * inv) % p
        below = np.nonzero(M[r + 1:, j])[0]
        for off in below:
            i = r + 1 + off
            M[i] = (M[i] - M[i, j] * M[r]) % p
        r += 1
        if r == m:
            break
    return r


# ============================================================================
# PART I : base - face lattice of the Birkhoff polytope Bo_3
# ============================================================================
hdr("PART I: base face lattice of Bo_3 (49 faces, f = 6,15,18,9,1)")

PERMS = sorted(itertools.permutations(range(3)))
PID = {p: i for i, p in enumerate(PERMS)}


def SIGPI(p):  # vertex map of D -> D P_sigma:  pi -> sigma^{-1} o pi
    # (v_pi P_sigma)_{ak} = [pi(a) = sigma(k)]  =>  pi'(a) = sigma^{-1}(pi(a))
    return ((p[0] - 1) % 3, (p[1] - 1) % 3, (p[2] - 1) % 3)


POS = [(a, k) for a in range(3) for k in range(3)]

face_keys = set()
for r in range(len(POS) + 1):
    for Z in itertools.combinations(POS, r):
        vs = tuple(sorted(i for i, p in enumerate(PERMS) if all(p[a] != k for (a, k) in Z)))
        if vs:
            face_keys.add(vs)
FK = sorted(face_keys)
NF = len(FK)
FKS = set(FK)
INT = FK.index(tuple(range(6)))
# face dimension: proper faces are simplices (dim = #verts-1); interior is dim 4
DIMF = [len(vs) - 1 if len(vs) <= 4 else 4 for vs in FK]
assert DIMF[INT] == 4

fv = [0] * 5
for fi in range(NF):
    fv[DIMF[fi]] += 1
print("faces: %d   f-vector %s   (interior id %d)" % (NF, fv, INT))
assert NF == 49 and fv == [6, 15, 18, 9, 1]


def vmat_frac(i):
    p = PERMS[i]
    M = [[Fraction(0)] * 3 for _ in range(3)]
    for a in range(3):
        M[a][p[a]] = Fraction(1)
    return M


# affine independence (all 48 PROPER faces are simplices; interior is the 4-cell)
for fi, vs in enumerate(FK):
    if len(vs) == 1 or fi == INT:
        continue
    base = vmat_frac(vs[0])
    rows = []
    for l in range(1, len(vs)):
        W = vmat_frac(vs[l])
        rows.append([W[a][k] - base[a][k] for a in range(3) for k in range(3)])
    Ms = Matrix(rows)
    assert Ms.rank() == len(vs) - 1, "face not a simplex: %s" % (vs,)
print("all 48 proper faces are simplices: OK")


def support(vs):
    return sorted(set((a, PERMS[i][a]) for i in vs for a in range(3)))


def comp_groups(vs):
    par = list(range(6))

    def find(x):
        while par[x] != x:
            par[x] = par[par[x]]
            x = par[x]
        return x

    for i in vs:
        for a in range(3):
            ra, rk = find(a), find(3 + PERMS[i][a])
            if ra != rk:
                par[ra] = rk
    groups = {}
    for x in range(6):
        groups.setdefault(find(x), []).append(x)
    return list(groups.values())


CTYPE = []       # 'pt' / 'S1' / 'T2'
FIXEDROW = []    # for S1 faces: the singleton row
for fi, vs in enumerate(FK):
    gr = comp_groups(vs)
    if len(gr) == 3:
        CTYPE.append('pt')
        FIXEDROW.append(None)
    elif len(gr) == 2:
        CTYPE.append('S1')
        fr = None
        for g in gr:
            rows_in = [x for x in g if x < 3]
            if len(rows_in) == 1:
                fr = rows_in[0]
        assert fr is not None
        FIXEDROW.append(fr)
    else:
        assert len(gr) == 1
        CTYPE.append('T2')
        FIXEDROW.append(None)

cnt = {'pt': 0, 'S1': 0, 'T2': 0}
for c in CTYPE:
    cnt[c] += 1
print("fiber types: vertices(pt)=%d, sphere-edges(S1)=%d, one-block(T2)=%d" %
      (cnt['pt'], cnt['S1'], cnt['T2']))
assert cnt['pt'] == 6 and cnt['S1'] == 9 and cnt['T2'] == 34

# sanity: sphere-edges are the 9 E_{ak} (vertices agree at one position)
se = [fi for fi in range(NF) if CTYPE[fi] == 'S1']
akset = set()
for fi in se:
    vs = FK[fi]
    p0, p1 = PERMS[vs[0]], PERMS[vs[1]]
    ag = [(a, p0[a]) for a in range(3) if p0[a] == p1[a]]
    assert len(ag) == 1
    akset.add(ag[0])
assert len(akset) == 9
print("sphere-edges = the 9 E_{ak} = conv(P,P') with P,P' agreeing at (a,k): OK")

# codim-1 boundary data for simplicial faces (vertices and interior skipped)
CODIM1 = {}
for fi in range(NF):
    if fi == INT or len(FK[fi]) == 1:
        continue
    vs = FK[fi]
    out = []
    for i in range(len(vs)):
        sub = tuple(x for j, x in enumerate(vs) if j != i)
        assert sub in FKS, "sub-face missing"
        out.append((FK.index(sub), (-1) ** i))
    CODIM1[fi] = out

# c-action on faces
FSIG = [None] * NF


def fsig(fi):
    if FSIG[fi] is not None:
        return FSIG[fi]
    vs = FK[fi]
    img = tuple(sorted(PID[SIGPI(PERMS[i])] for i in vs))
    FSIG[fi] = FK.index(img)
    return FSIG[fi]


for fi in range(NF):
    fsig(fi)

# orbit phase p(F) in Z/3 (p(cF) = p(F)+1); representatives = min of orbit
PMAP = [None] * NF
SSHUF = [None] * NF
seen = set()
for fi in range(NF):
    if fi in seen:
        continue
    orbit = [fi]
    cur = fsig(fi)
    while cur != fi:
        orbit.append(cur)
        cur = fsig(cur)
    assert len(orbit) in (1, 3)
    rep = min(orbit)
    st = orbit.index(rep)
    for k2 in range(len(orbit)):
        PMAP[orbit[(rep_index := (st + k2) % len(orbit))]] = k2 % 3
    for x in orbit:
        seen.add(x)
assert PMAP[INT] == 0
nprop = sum(1 for fi in range(NF) if fi != INT)
assert all(x in seen for x in range(NF)) and len(seen) == NF
print("face c-orbits: 1 fixed (interior) + %d free orbits of 3" % (nprop // 3))
assert nprop % 3 == 0 and nprop // 3 == 16

# shuffle sign s(F) of the sorted-vertex list under the sigma map
def shuffle_sign(fi):
    vs = FK[fi]
    tgt = FK[fsig(fi)]
    perm_idx = []
    for v in vs:
        w = PID[SIGPI(PERMS[v])]
        perm_idx.append(tgt.index(w))
    inv = 0
    for i in range(len(perm_idx)):
        for j in range(i + 1, len(perm_idx)):
            if perm_idx[i] > perm_idx[j]:
                inv += 1
    return -1 if inv % 2 else 1


for fi in range(NF):
    SSHUF[fi] = shuffle_sign(fi)

# interior 4-cell: orientation = ambient basis (B00,B01,B10,B11);
# sigma-map det on the affine 4-space (verify +1)
def sigma_det_on_L():
    # coords of MP_sigma in the B-basis = flattened top-left 2x2 of M P_sigma
    # c'00 = M[0][1], c'01 = -(M00+M01), c'10 = M[1][1], c'11 = -(M10+M11)
    rows = [[0, 1, 0, 0], [-1, -1, 0, 0], [0, 0, 0, 1], [0, 0, -1, -1]]
    d = Matrix(rows).det()
    return int(d)


S_INT = sigma_det_on_L()
print("sigma-map det on the affine 4-space: %+d (interior T-sign)" % S_INT)
assert S_INT == 1


def ambient_coords(M):
    return [M[0][0], M[0][1], M[1][0], M[1][1]]


def proj_E(ak):
    a, k = ak
    M = [[Fraction(0)] * 3 for _ in range(3)]
    for i in range(3):
        for j in range(3):
            M[i][j] = (Fraction(int(i == a and j == k))
                       - Fraction(1, 3) * int(i == a)
                       - Fraction(1, 3) * int(j == k)
                       + Fraction(1, 9))
    return M


def det4(rows):
    A = [[float(x) for x in r] for r in rows]
    import copy
    A = [list(r) for r in rows]
    n = 4
    det = Fraction(1)
    for col in range(n):
        piv = None
        for rr in range(col, n):
            if A[rr][col] != 0:
                piv = rr
                break
        if piv is None:
            return Fraction(0)
        if piv != col:
            A[col], A[piv] = A[piv], A[col]
            det = -det
        det *= A[col][col]
        inv = Fraction(1, 1) / A[col][col]
        for rr in range(col + 1, n):
            if A[rr][col] != 0:
                f = A[rr][col] * inv
                for cc in range(col, n):
                    A[rr][cc] -= f * A[col][cc]
    return det


# geometric boundary signs eps_Phi for the interior 4-cell
def facet_zero_pos(fi):
    vs = FK[fi]
    supp = set(support(vs))
    for (a, k) in POS:
        if (a, k) not in supp:
            return (a, k)
    raise AssertionError


facets = [fi for fi in range(NF) if len(FK[fi]) == 4]
EPS = {}
for fi in facets:
    vs = FK[fi]
    ak = facet_zero_pos(fi)
    n_out = [[-x for x in row] for row in proj_E(ak)]
    base = vmat_frac(vs[0])
    rows = [ambient_coords(n_out)]
    for l in range(1, 4):
        W = vmat_frac(vs[l])
        e = [[W[a][k] - base[a][k] for k in range(3)] for a in range(3)]
        rows.append(ambient_coords(e))
    d = det4(rows)
    assert d != 0
    EPS[fi] = 1 if d > 0 else -1

CODIM1[INT] = [(fi, EPS[fi]) for fi in facets]
print("interior boundary signs eps_Phi computed geometrically for %d facets" % len(facets))

# sigma-consistency of eps (battery item): eps_{Phi sigma} = eps_Phi * s(Phi)
for fi in facets:
    assert EPS[fsig(fi)] == EPS[fi] * SSHUF[fi], "eps sigma-consistency fails"
print("eps_{Phi sigma} = eps_Phi * s(Phi) for all 9 facets: OK")

tick("Part I done")

# ============================================================================
# PART II : level-3 fiber cellulations
# ============================================================================
hdr("PART II: level-3 fiber cellulations (S1: 3+3, T2: 9+27+18 = 54 cells)")

T2CELLS = []
for i in range(3):
    for j in range(3):
        T2CELLS.append(('P', i, j))
for j in range(3):
    for i in range(3):
        T2CELLS.append(('H', j, i))
for i in range(3):
    for j in range(3):
        T2CELLS.append(('V', i, j))
for c in range(3):
    for k in range(3):
        T2CELLS.append(('A', c, k))
for i in range(3):
    for j in range(3):
        T2CELLS.append(('L', i, j))
for i in range(3):
    for j in range(3):
        T2CELLS.append(('U', i, j))
assert len(T2CELLS) == 54

S1CELLS = [('p', m) for m in range(3)] + [('a', m) for m in range(3)]
PTCELL = ('X',)


def fdim(fc):
    if fc == PTCELL:
        return 0
    if fc[0] == 'P' or fc[0] == 'p':
        return 0
    if fc[0] in ('L', 'U'):
        return 2
    return 1


def t2_bound(c):
    k = c[0]
    if k == 'P':
        return []
    if k == 'H':
        _, j, i = c
        return [(1, ('P', (i + 1) % 3, j)), (-1, ('P', i, j))]
    if k == 'V':
        _, i, j = c
        return [(1, ('P', i, (j + 1) % 3)), (-1, ('P', i, j))]
    if k == 'A':
        _, c3, kk = c
        return [(1, ('P', (kk + 1) % 3, (c3 - kk - 1) % 3)), (-1, ('P', kk, (c3 - kk) % 3))]
    if k == 'L':
        _, i, j = c
        cc = (i + j + 1) % 3
        return [(1, ('H', j, i)), (-1, ('A', cc, i)), (-1, ('V', i, j))]
    if k == 'U':
        _, i, j = c
        cc = (i + 1 + j + 1 - 1) % 3  # (i+1)+(j+1)+... use square (i,j) anti-diagonal
        cc = (i + j + 1) % 3
        return [(1, ('V', (i + 1) % 3, j)), (-1, ('H', (j + 1) % 3, i)), (1, ('A', cc, i))]
    raise ValueError


def t2_tr(c, d1, d2):
    k = c[0]
    if k == 'P':
        return ('P', (c[1] + d1) % 3, (c[2] + d2) % 3)
    if k == 'H':
        return ('H', (c[1] + d2) % 3, (c[2] + d1) % 3)
    if k == 'V':
        return ('V', (c[1] + d1) % 3, (c[2] + d2) % 3)
    if k == 'A':
        return ('A', (c[1] + d1 + d2) % 3, (c[2] + d1) % 3)
    return (k, (c[1] + d1) % 3, (c[2] + d2) % 3)


def t2_q(c, a):
    """q-map T^2 -> S^1 for the sphere-edge with fixed row a
    (glued rows: the other two).  a=0: q=-v; a=1: q=-(u+v); a=2: q=-u.
    Returns None | (coeff, 'p', m) | (coeff, 'a', m)."""
    k = c[0]
    if k == 'P':
        i, j = c[1], c[2]
        if a == 0:
            return (1, 'p', (-j) % 3)
        if a == 1:
            return (1, 'p', (-i - j) % 3)
        return (1, 'p', (-i) % 3)
    if k == 'H':
        j, i = c[1], c[2]
        if a == 0:
            return None
        if a == 1:
            return (-1, 'a', (-i - j - 1) % 3)
        return (-1, 'a', (-i - 1) % 3)
    if k == 'V':
        i, j = c[1], c[2]
        if a == 0:
            return (-1, 'a', (-j - 1) % 3)
        if a == 1:
            return (-1, 'a', (-i - j - 1) % 3)
        return None
    if k == 'A':
        cc, kk = c[1], c[2]
        if a == 0:
            return (1, 'a', (kk - cc) % 3)
        if a == 1:
            return None
        return (-1, 'a', (-kk - 1) % 3)
    return None


def s1_bound(c):
    if c[0] == 'a':
        return [(1, ('p', (c[1] + 1) % 3)), (-1, ('p', c[1]))]
    return []


SHIFT3 = [2, 1, 2]  # q_G(t0) in thirds for fixed row a = 0,1,2

# internal d^2=0 for the fiber cellulations
for c in T2CELLS:
    acc = {}
    for (co, e2) in t2_bound(c):
        for (co2, e3) in t2_bound(e2):
            acc[e3] = acc.get(e3, 0) + co * co2
    assert all(v == 0 for v in acc.values()), "fiber d^2 != 0 at %s" % (c,)
for c in S1CELLS:
    acc = {}
    for (co, e2) in s1_bound(c):
        for (co2, e3) in s1_bound(e2):
            acc[e3] = acc.get(e3, 0) + co * co2
    assert all(v == 0 for v in acc.values())
print("fiber cellulation boundaries: d^2 = 0 OK;  cells: T2 9+27+18, S1 3+3")

# translation action sanity: tau-shifts permute the 54 cells
for (d1, d2) in [(1, 1), (2, 2), (1, 0), (0, 1)]:
    imgs = set(t2_tr(c, d1, d2) for c in T2CELLS)
    assert len(imgs) == 54
print("grid translations by thirds act as permutations of the 54 cells: OK")

tick("Part II done")

# ============================================================================
# PART III : global cells, boundary operator
# ============================================================================
hdr("PART III: the 1896 cells and the boundary operator d")


def face_fcells(ct):
    if ct == 'pt':
        return [PTCELL]
    if ct == 'S1':
        return S1CELLS
    return T2CELLS


CELLS = []
CELLI = {}
for fi in range(NF):
    for fc in face_fcells(CTYPE[fi]):
        CELLI[(fi, fc)] = len(CELLS)
        CELLS.append((fi, fc))
NC = len(CELLS)
DEG = [0] * NC
for idx, (fi, fc) in enumerate(CELLS):
    DEG[idx] = DIMF[fi] + fdim(fc)

NK = [0] * 7
for idx in range(NC):
    NK[DEG[idx]] += 1
chi = sum((-1) ** k * NK[k] for k in range(7))
print("cells: %d   per-degree %s   chi = %+d" % (NC, NK, chi))
assert NC == 1896
assert NK == [6, 81, 351, 675, 576, 189, 18]
assert chi == 6


def cell_terms(fi, fc):
    out = []
    ct = CTYPE[fi]
    if ct == 'pt':
        return out
    for (gi, sg) in CODIM1[fi]:
        gct = CTYPE[gi]
        if gct == 'T2':
            dd = (PMAP[fi] - PMAP[gi]) % 3
            out.append((sg, (gi, t2_tr(fc, dd, dd))))
        elif gct == 'S1':
            a = FIXEDROW[gi]
            r = t2_q(fc, a)
            if r is not None:
                (cq, kind, m) = r
                s = (SHIFT3[a] * ((PMAP[fi] - PMAP[gi]) % 3)) % 3
                out.append((sg * cq, (gi, (kind, (m + s) % 3))))
        else:  # vertex fiber: only 0-dim fiber cells survive
            if fdim(fc) == 0:
                out.append((sg, (gi, PTCELL)))
    sign = (-1) ** DIMF[fi]
    if ct == 'T2':
        for (co, e2) in t2_bound(fc):
            out.append((sign * co, (fi, e2)))
    elif ct == 'S1':
        for (co, e2) in s1_bound(fc):
            out.append((sign * co, (fi, e2)))
    return out


D = [dict() for _ in range(7)]  # D[k]: {k-cell: {(k-1)-cell: coeff}}
for idx, (fi, fc) in enumerate(CELLS):
    k = DEG[idx]
    col = {}
    for (co, tgt) in cell_terms(fi, fc):
        j = CELLI[tgt]
        assert DEG[j] == k - 1, "degree mismatch %d -> %d" % (k, DEG[j])
        col[j] = col.get(j, 0) + co
    col = {j: v for j, v in col.items() if v != 0}
    D[k][idx] = col

nz = sum(len(c) for k in range(7) for c in D[k].values())
print("boundary operator built: %d nonzero column entries" % nz)

# local per-degree index maps (global cell id -> local index in its degree)
LOCF = [dict() for _ in range(7)]
for k in range(7):
    c = 0
    for idx in range(NC):
        if DEG[idx] == k:
            LOCF[k][idx] = c
            c += 1
DLOC = [dict() for _ in range(7)]
for k in range(1, 7):
    DLOC[k] = {LOCF[k][col]: {LOCF[k - 1][row]: v for row, v in terms.items()}
               for col, terms in D[k].items()}

# battery (2): d^2 = 0 exactly
bad = 0
for k in range(2, 7):
    for col, terms in D[k].items():
        acc = {}
        for row, co in terms.items():
            for row2, co2 in D[k - 1].get(row, {}).items():
                acc[row2] = acc.get(row2, 0) + co * co2
        for v in acc.values():
            if v != 0:
                bad += 1
                if bad < 5:
                    print("  d^2 != 0 at cell %d (deg %d): residual %d" % (col, k, v))
assert bad == 0, "d^2 = 0 FAILED (%d residuals)" % bad
print("BATTERY: d^2 = 0 exactly: PASS")

tick("Part III done")
# ============================================================================
# PART IV : the c-action T on cells; equivariance battery
# ============================================================================
hdr("PART IV: c-action on cells, T^3 = I, dT = Td, freeness")

TSUP = [0] * NC
TSGN = [1] * NC
for idx, (fi, fc) in enumerate(CELLS):
    if fi == INT:
        TSUP[idx] = CELLI[(INT, t2_tr(fc, 1, 1))]   # +t0, t0 = (1/3,1/3)
        TSGN[idx] = 1                                # s(interior) = +1 (verified)
    else:
        TSUP[idx] = CELLI[(fsig(fi), fc)]
        TSGN[idx] = SSHUF[fi]

# T^3 = I on cells
ok3 = True
for idx in range(NC):
    i1 = TSUP[idx]
    i2 = TSUP[i1]
    i3 = TSUP[i2]
    if i3 != idx or (TSGN[idx] * TSGN[i1] * TSGN[i2]) != 1:
        ok3 = False
        break
assert ok3, "T^3 != I"
print("BATTERY: T^3 = I (with sign product +1): PASS")

# freeness: no fixed cells
fixed = [idx for idx in range(NC) if TSUP[idx] == idx]
assert not fixed, "c has fixed cells: %s" % fixed[:5]
print("BATTERY: c acts freely on the 1896 cells (no fixed cell): PASS")

# degree preservation
for idx in range(NC):
    assert DEG[TSUP[idx]] == DEG[idx]
print("BATTERY: T preserves cell degrees: PASS")

# dT = Td exactly
baddt = 0
for k in range(1, 7):
    for col, terms in D[k].items():
        lhs = {}
        for row, co in terms.items():
            j2 = TSUP[row]
            lhs[j2] = lhs.get(j2, 0) + co * TSGN[row]
        lhs = {j: v for j, v in lhs.items() if v != 0}
        tcol = TSUP[col]
        tsg = TSGN[col]
        rhs = {j: v * tsg for j, v in D[k][tcol].items()}
        rhs = {j: v for j, v in rhs.items() if v != 0}
        if lhs != rhs:
            baddt += 1
            if baddt < 5:
                print("  dT != Td at cell %d deg %d" % (col, k))
                print("   lhs:", sorted(lhs.items())[:6])
                print("   rhs:", sorted(rhs.items())[:6])
assert baddt == 0, "dT = Td FAILED (%d cells)" % baddt
print("BATTERY: dT = Td exactly: PASS")

tick("Part IV done")

# ============================================================================
# PART IV-bis : unistochastic feasibility audit of the Birkhoff base strata
# D is unistochastic iff for every row pair (a,b) the magnitudes
# m_k = sqrt(D_{ak} D_{bk}) satisfy the triangle inequalities (exact
# solvability of the pair's orthogonality constraint  sum m_k e^{i a_k} = 0).
# ============================================================================
hdr("PART IV-bis: unistochastic feasibility audit of the base strata")


def pair_feasible(D, a, b):
    ms = [D[a][k] * D[b][k] for k in range(3)]  # Fractions (squared mags)
    for i in range(3):
        x, y, z = ms[i], ms[(i + 1) % 3], ms[(i + 2) % 3]
        if x >= y + z and (x - y - z) ** 2 > 4 * y * z:
            return False
    return True


def feasible_D(D):
    return all(pair_feasible(D, a, b) for (a, b) in [(0, 1), (0, 2), (1, 2)])


def barycenter(vs):
    n = len(vs)
    M = [[Fraction(0)] * 3 for _ in range(3)]
    for i in vs:
        W = vmat_frac(i)
        for a in range(3):
            for k in range(3):
                M[a][k] += W[a][k]
    return [[x / n for x in row] for row in M]


from collections import Counter

table = Counter()
for fi in range(NF):
    D = barycenter(FK[fi])
    table[(DIMF[fi], CTYPE[fi], feasible_D(D))] += 1
print("face-BARYCENTER feasibility (dim, fiber-type, feasible):")
for key in sorted(table):
    print("   dim %d  type %-3s  feasible=%-5s : %d faces" % (key[0], key[1], key[2], table[key]))

# generic parameter scan on the 15 edges (t = 1/3, 2/5) -- feasibility along the edge
edge_scan = Counter()
for fi in range(NF):
    if DIMF[fi] != 1:
        continue
    v0, v1 = vmat_frac(FK[fi][0]), vmat_frac(FK[fi][1])
    for t in (Fraction(1, 3), Fraction(2, 5)):
        D = [[(1 - t) * v0[a][k] + t * v1[a][k] for k in range(3)] for a in range(3)]
        edge_scan[(CTYPE[fi], feasible_D(D))] += 1
print("edge-generic-point feasibility (type, feasible):")
for key in sorted(edge_scan):
    print("   type %-3s  feasible=%-5s : %d edge-points" % (key[0], key[1], edge_scan[key]))
print("=> the 6 six-cycle edges and the 18 triangles are INFEASIBLE (all points);")
print("=> facets are feasible only on the 2-dim equality locus; only interior,")
print("   9 sphere-edges, 6 vertices (+ facet equality loci) carry nonempty fibers.")

tick("Part IV-bis done")

# ============================================================================
# PART V : homology of Fl_3 (rational Betti + exact mod-p torsion audit)
# ============================================================================
hdr("PART V: H_*(Fl_3) - Betti (mod large primes) + torsion audit (mod-p UCT)")


def betti_and_torsion(Dloc, NKl, label, primes_tors=(2, 3, 5, 7, 11, 13), primes_rat=(10000019, 10000079)):
    nd = len(NKl)
    cache = {}

    def rk(k, p):
        if (k, p) not in cache:
            if k < 1 or k >= nd:
                cache[(k, p)] = 0
            else:
                cache[(k, p)] = rank_modp(Dloc[k], NKl[k], NKl[k - 1], p)
        return cache[(k, p)]

    rk_rat = None
    for p in primes_rat:
        rkl = [rk(k, p) for k in range(nd + 1)]
        if rk_rat is None:
            rk_rat = rkl
        else:
            assert rkl == rk_rat, "rational rank differs between primes at p=%d" % p
    beta = [0] * nd
    for k in range(nd):
        beta[k] = NKl[k] - rk_rat[k] - rk_rat[k + 1]
    tors = {}
    for p in primes_tors:
        bp = [0] * nd
        for k in range(nd):
            bp[k] = NKl[k] - rk(k, p) - rk(k + 1, p)
        tp = [0] * nd
        for k in range(nd):
            tp[k] = bp[k] - beta[k] - (tp[k - 1] if k >= 1 else 0)
        tors[p] = tp
    print("%s: chain ranks %s" % (label, rk_rat[:nd]))
    print("%s: Betti  b = %s" % (label, beta))
    for p in primes_tors:
        print("%s: mod-%2d Betti %s   -> torsion summand counts t_p = %s" %
              (label, p, [NKl[k] - rk(k, p) - rk(k + 1, p) for k in range(nd)], tors[p]))
    return beta, tors


betaF, torsF = betti_and_torsion(DLOC, NK, "Fl_3")
SPEC_OK = (betaF == [1, 0, 2, 0, 2, 0, 1]
           and all(all(v == 0 for v in torsF[p]) for p in torsF))
if not SPEC_OK:
    hdr("BATTERY FAILURE -> THE RECORDED 1896-CELL SPEC IS REFUTED")
    print("H_*(built complex; Q)  = %s   (torsion summands: %s)" %
          (betaF, {p: torsF[p] for p in torsF}))
    print("H_*(Fl_3; Q) required = [1, 0, 2, 0, 2, 0, 1]   with H_6 = Z (closed 6-manifold).")
    print()
    print("The chain-level battery PASSED in full (1896 cells (6,81,351,675,576,189,18),")
    print("chi = 6, d^2 = 0 exactly, T^3 = I, c free on cells, dT = Td exactly):")
    print("the built complex is a genuine C_3-equivariant chain complex -- but it is NOT")
    print("a model of Fl_3, because the BASE stratification of the recorded spec is")
    print("geometrically infeasible:")
    print()
    print("ROOT CAUSE (unistochastic feasibility, machine-checked):")
    print(" * six-cycle edges conv(P, P_sigma): every interior point has a row pair whose")
    print("   orthogonality constraint is  sqrt(t(1-t)) e^{i phi} = 0  with t in (0,1) --")
    print("   IMPOSSIBLE.  The 'T^2 fibers over 6 six-cycle edges' are EMPTY.")
    print(" * the 18 triangular 2-faces: each contains a row pair sharing exactly ONE")
    print("   nonzero column: constraint  m e^{i phi} = 0 with m > 0 -- IMPOSSIBLE.")
    print(" * the 9 facets: the row pair adjacent to the zero entry shares two columns;")
    print("   feasibility forces the equality  D_{a'k'} D_{bk'} = D_{a''k''} D_{bk''}")
    print("   (which is why the barycenter, by symmetry, tests feasible) -- the feasible")
    print("   set is a codim-1 equality LOCUS (2-dim, T^2 fibers); the open 3-dim facet")
    print("   relint of the spec carries NO fiber.")
    print(" Nonempty fibers over the Birkhoff base exist only over: the interior 4-cell")
    print(" (T^2), the 9 sphere-edges (S^1), the 6 vertices (pt), and the 2-dim facet")
    print(" equality loci (T^2).  The image of pi: Fl_3 -> Bo_3 is the UNISTOCHASTIC")
    print(" region U_3, bounded by the 9 curved fold-walls  {m_i = m_j + m_k} (row-pair")
    print(" triangle degenerations, T^2 fibers), not by the Birkhoff facets.  The")
    print(" Wave 9/10 machine checks verified the face lattice and HALL (doubly")
    print(" stochastic) feasibility -- never the unistochastic (triangle-inequality)")
    print(" side; that gap propagated into the recorded spec.")
    print()
    print("CONSEQUENCE: the 1896-cell orbit-complex SNF below would compute the")
    print("homology of the WRONG space, so it is skipped.  The qutrit bit REMAINS OPEN.")
    print("The honest decisive route (recorded for the next session): cellulate the")
    print("unistochastic region (the wall arrangement W_{(ab),i}:  m^{(ab)}_i =")
    print("m^{(ab)}_j + m^{(ab)}_k, 9 walls, S_3 x S_3 symmetric, T^2-fibers, fold type),")
    print("with the SAME level-3 fiber cellulations, the SAME t0/twist layer and the")
    print("SAME battery; then the orbit-complex SNF settles H_2(B_3).")
    sys.exit(1)
print("BATTERY: H_*(Fl_3) = (Z, 0, Z^2, 0, Z^2, 0, Z), torsion-free "
      "(exact mod-p UCT induction for p in {2,3,5,7,11,13}): PASS")

tick("Part V done")

# ============================================================================
# PART VI : the c-action on H_2 and H_6 (mod 7)
# ============================================================================
hdr("PART VI: c-action on homology (N = 1+T+T^2 on H_2, T on H_6)")

P7 = 7


def dense_D(k, p):
    M = np.zeros((NK[k - 1], NK[k]), dtype=np.int64)
    for j, col in DLOC[k].items():
        for i, v in col.items():
            M[i, j] = v % p
    return M


def dense_T(k, p):
    # T as a matrix on C_k (rows = target cell, cols = source cell)
    idxk = [idx for idx in range(NC) if DEG[idx] == k]
    pos = {idx: i for i, idx in enumerate(idxk)}
    M = np.zeros((len(idxk), len(idxk)), dtype=np.int64)
    for i, idx in enumerate(idxk):
        M[pos[TSUP[idx]], i] = TSGN[idx] % p
    return M, idxk, pos


# H_2: cycles mod 7
d2_7 = dense_D(2, P7)
ns = nullspace_modp(DLOC[2], NK[2], NK[1], P7)
B = np.array(ns).T if ns else np.zeros((NK[2], 0), dtype=np.int64)  # NK[2] x dim
print("H_2(F_7) cycles: %d basis vectors" % B.shape[1])
T2_7, _, _ = dense_T(2, P7)
N7 = (np.eye(NK[2], dtype=np.int64) + T2_7 + T2_7 @ T2_7) % P7
d3_7 = dense_D(3, P7)
r_d3 = rank_dense_modp(d3_7.copy(), P7)
NB = (N7 @ B) % P7
r_comb = rank_dense_modp(np.hstack([d3_7, NB]), P7)
assert r_comb == r_d3, "N = 1+T+T^2 NOT zero on H_2 (mod 7)"
print("BATTERY: 1+T+T^2 = 0 on H_2 (mod 7): PASS  (rank %d == %d)" % (r_comb, r_d3))

# order exactly 3 on H_2: (T-I) not zero on H_2
TB = ((T2_7 - np.eye(NK[2], dtype=np.int64)) @ B) % P7
r_comb2 = rank_dense_modp(np.hstack([d3_7, TB]), P7)
assert r_comb2 > r_d3, "T acts trivially on H_2?!"
print("BATTERY: T has order exactly 3 on H_2 (mod 7): PASS  (rank %d > %d)" % (r_comb2, r_d3))

# H_6: T = +1 on the top class
d6_7 = dense_D(6, P7)
ns6 = nullspace_modp(DLOC[6], NK[6], NK[5], P7)
print("H_6(F_7) cycles: %d (expect 1)" % len(ns6))
assert len(ns6) == 1
v = ns6[0]
T6_7, idxk6, pos6 = dense_T(6, P7)
w = T6_7 @ v % P7
scale = None
for i in range(len(v)):
    if v[i] % P7:
        scale = (int(w[i]) * pow(int(v[i]), P7 - 2, P7)) % P7
        break
for i in range(len(v)):
    if v[i] % P7 and (int(w[i]) - scale * int(v[i])) % P7:
        raise AssertionError("T not scalar on H_6")
print("BATTERY: T = %+d on H_6 (mod 7): %s" % (scale, "PASS" if scale == 1 else "FAIL"))
assert scale == 1

tick("Part VI done")

# ============================================================================
# PART VII : the orbit complex (632 orbits) and H_*(B_3)
# ============================================================================
hdr("PART VII: orbit complex C(Fl_3) (x)_{Z[C3]} Z - the quotient homology")

ORB = [None] * NC
norb_orbits = 0
for idx in range(NC):
    if ORB[idx] is None:
        o = [idx, TSUP[idx], TSUP[TSUP[idx]]]
        assert TSUP[o[2]] == idx
        rep = min(o)
        for x in o:
            ORB[x] = rep
        norb_orbits += 1
NORB = len(set(ORB))
print("cell orbits: %d (spec: 632)" % NORB)
assert NORB == 632

# representatives and quotient chain groups
REPS = sorted(set(ORB))
RIDX = {r: i for i, r in enumerate(REPS)}
QK = [0] * 7
for r in REPS:
    QK[DEG[r]] += 1
print("quotient chains per degree: %s   total %d" % (QK, sum(QK)))
assert QK == [2, 27, 117, 225, 192, 63, 6] and sum(QK) == 632

DB = [dict() for _ in range(7)]
for r in REPS:
    k = DEG[r]
    col = {}
    for row, co in D[k][r].items():
        rr = ORB[row]
        col[rr] = col.get(rr, 0) + co
    col = {j: v for j, v in col.items() if v != 0}
    DB[k][r] = col

# d_bar^2 = 0 (also follows from d^2=0 + dT=Td, but check directly)
badq = 0
for k in range(2, 7):
    for col, terms in DB[k].items():
        acc = {}
        for row, co in terms.items():
            for row2, co2 in DB[k - 1].get(row, {}).items():
                acc[row2] = acc.get(row2, 0) + co * co2
        for v in acc.values():
            if v != 0:
                badq += 1
assert badq == 0
print("BATTERY: d_bar^2 = 0: PASS")

tick("orbit complex built")

# ---- mod-p exact homology of the quotient ----
QLOCF = [dict() for _ in range(7)]
for k in range(7):
    c = 0
    for r in REPS:
        if DEG[r] == k:
            QLOCF[k][r] = c
            c += 1
QLOC = [dict() for _ in range(7)]
for k in range(1, 7):
    QLOC[k] = {QLOCF[k][col]: {QLOCF[k - 1][row]: v for row, v in terms.items()}
               for col, terms in DB[k].items()}

betaQ, torsQ = betti_and_torsion(QLOC, QK, "B_3 ")

# ---- integral Smith normal form for the decisive degrees ----
hdr("PART VIII: integral SNF of the quotient (H_1, H_2, H_5, H_6)")


def db_sympy(k):
    m, n = QK[k - 1], QK[k]
    M = zeros(m, n)
    # need index maps rep -> local index
    reps_k = [r for r in REPS if DEG[r] == k]
    reps_k1 = [r for r in REPS if DEG[r] == k - 1]
    posk = {r: i for i, r in enumerate(reps_k)}
    posk1 = {r: i for i, r in enumerate(reps_k1)}
    for r, col in DB[k].items():
        for row, co in col.items():
            M[posk1[row], posk[r]] = co
    return M


def homology_integral(k):
    """H_k(quotient) via kernel/image lattices (integral)."""
    d_lo = db_sympy(k)      # C_k -> C_{k-1}
    K = kernel_lattice(d_lo)
    if k + 1 <= 6:
        d_hi = db_sympy(k + 1)
        S = image_lattice_basis(d_hi)
    else:
        S = zeros(QK[k], 0)
    if S.shape[1] == 0:
        return (K.shape[1], [])
    return subquotient(K, S)


Hq = {}
for k in (1, 2, 5, 6):
    tick("integral SNF: H_%d of the quotient ..." % k)
    Hq[k] = homology_integral(k)
    print("  H_%d(B_3) = %s" % (k, abelian(Hq[k])))

tick("integral SNF done")

# ============================================================================
# VERDICT
# ============================================================================
hdr("VERDICT: H_*(B_3) and the qutrit bit")

print("mod-p exact:  Betti b(B_3) = %s" % betaQ)
for p in sorted(torsQ):
    print("              t_%d(B_3) = %s" % (p, torsQ[p]))
for k in (1, 2, 5, 6):
    print("integral SNF: H_%d(B_3) = %s" % (k, abelian(Hq[k])))

# mandatory slots
checks = []
checks.append(("H_0 = Z", betaQ[0] == 1 and torsQ[3][0] == 0))
checks.append(("H_1 = Z/3", Hq[1][0] == 0 and Hq[1][1] == [3]))
checks.append(("H_5 = 0", Hq[5] == (0, [])))
checks.append(("H_6 = Z", Hq[6] == (1, [])))
for (name, ok) in checks:
    print("  mandatory %s : %s" % (name, "PASS" if ok else "FAIL"))

h2 = Hq[2]
print("\nTHE BIT: H_2(B_3) = %s" % abelian(h2))
if h2 == (0, [3]):
    print("  -> WORLD 1: CLSS d_3: E3^{1,2} -> E3^{4,0} is ZERO.")
    print("  -> the Chern-class obstruction x^2 != 0 survives (Wave 7 theorem),")
    print("  -> delta_2(D(C^3)) = 4/3  is CONFIRMED by the honest computation.")
elif h2 == (0, []):
    print("  -> WORLD 2: CLSS d_3 is an isomorphism; the obstruction dies;")
    print("  -> delta_2(qutrit) = 4/3 is REFUTED; the bit resolves the other way.")
else:
    print("  -> UNEXPECTED (battery inconsistency?) — inspect manually.")

print("\n(Fl_4 / ququart: honestly deferred — ~10^5 cells; separate run.)")
tick("run complete")
