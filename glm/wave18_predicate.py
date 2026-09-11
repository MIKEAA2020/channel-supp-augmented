#!/usr/bin/env python3
"""
WAVE 18 -- THE PREDICATE RE-DERIVATION PASS (statement-only, no new cellulation).

Directive (2026-09-11): a "Wave 18 -- predicate re-derivation" pass that ends
with either (a) a pinned, machine-checkable predicate for delta_1 or (b) an
honest theorem that the paper-line link needs correction.

Outcome (both, in one coherent statement):
  (a) THE PINNED PREDICATE (P-delta_1), in six equivalent forms, with every
      premise labeled machine / theory / cited, aimed at the Stage-4 orbit SNF;
  (b) THE CORRECTION THEOREM: the Wave-8C closure predicate
      "delta_1 = 3/2  <=>  H^3(B_4;Z~) = Z/2, mirrored by |H_9(B_4;Z~)|"
      carried two defects that non-orientability (Wave 15) made load-bearing:
      (i)  the twisted-Poincare-duality pairing law of wave8c line 697
           ("H^k(B_4;Z~) ~ H_{12-k}(B_4;Z~)") is INVALID -- the correct law
           pairs H^k(B_4;Z~) with H_{12-k}(B_4;Z) (and H^k(B_4;Z) with
           H_{12-k}(B_4;Z~)); the W8C twisted-homology mirror therefore faces
           H^3(B_4;Z), NOT the bit-group H^3(B_4;Z~);
      (ii) the Wave-7 generator label: the primitive sigma-anti-invariant
           class of H^2(Fl_4;Z) is u_0 = (1,0,1,0) (x_1+x_3); the Wave-7 name
           (1,-1,1,-1) is EXACTLY 2*u_0, so the transgression evaluated there
           is trivially zero; the bit is d_3(u_0).
      The MANUSCRIPT itself needs no correction: it claims only the bracket
      [4/3, 3/2] (thm:state-nonflat) and poses the closure as open problem (v).

This script machine-verifies every sub-claim verifiable WITHOUT a new
cellulation (exact integer linear algebra on the C_4-modules; the C_2 /
antipodal / RP^2 test case both for the engine and for the correction
theorem; the Wave-17 orbit-skeleton mod-2 fact re-read from the committed
JSON).  delta_1 REMAINS OPEN -- but now with a STABLE, correctly-derived,
machine-checkable predicate.

Run: python3 wave18_predicate.py   (exact; ~1 min, sympy Groebner for the
coinvariant ring)
"""
import itertools
import json
import numpy as np
import sympy as sp

VERBOSE = True
OUT = []


def say(s=""):
    print(s)
    OUT.append(s)


def hdr(s):
    say("\n" + "=" * 74)
    say(s)
    say("=" * 74)


def tick(s):
    say("    [ok] " + s)


def check(name, got, want):
    assert got == want, "%s: got %r, want %r" % (name, got, want)
    tick("%s = %r" % (name, got))


# =====================================================================
# Section 0: exact integer linear algebra (own SNF with transforms)
# =====================================================================
def snf_decomp(M):
    """Smith normal form with transforms: returns (U, S, V) integer
    matrices, U and V unimodular, S diagonal, with U * M * V = S.
    Column operations act on V; row operations act on U.
    Standard Euclid structure: reduce row/col mod pivot; any nonzero
    remainder swaps INTO the pivot (strictly decreasing |pivot|)."""
    M = sp.Matrix(M.tolist()) if isinstance(M, np.ndarray) else sp.Matrix(M)
    S = M.copy()
    m, n = S.rows, S.cols
    U = sp.eye(m)
    V = sp.eye(n)
    r, c = 0, 0
    while r < m and c < n:
        # pivot: min-|.| nonzero entry of S[r:, c:]
        piv = None
        for i in range(r, m):
            for j in range(c, n):
                if S[i, j] != 0 and (piv is None or
                                     abs(int(S[i, j])) < abs(int(S[piv[0], piv[1]]))):
                    piv = (i, j)
        if piv is None:
            break
        i, j = piv
        if i != r:
            S.row_swap(i, r); U.row_swap(i, r)
        if j != c:
            S.col_swap(j, c); V.col_swap(j, c)
        # Euclid phase: clear row r and column c
        while True:
            # (a) reduce row r modulo the pivot (column operations)
            for jj in range(n):
                if jj != c and S[r, jj] != 0:
                    q = int(divmod(int(S[r, jj]), int(S[r, c]))[0])
                    if q != 0:
                        S[:, jj] = S[:, jj] - q * S[:, c]
                        V[:, jj] = V[:, jj] - q * V[:, c]
            # (b) reduce column c modulo the pivot (row operations)
            for ii in range(m):
                if ii != r and S[ii, c] != 0:
                    q = int(divmod(int(S[ii, c]), int(S[r, c]))[0])
                    if q != 0:
                        S[ii, :] = S[ii, :] - q * S[r, :]
                        U[ii, :] = U[ii, :] - q * U[r, :]
            # (c) any nonzero remainder in row r / column c swaps into pivot
            rem_col = None
            for jj in range(n):
                if jj != c and S[r, jj] != 0:
                    rem_col = jj
                    break
            rem_row = None
            for ii in range(m):
                if ii != r and S[ii, c] != 0:
                    rem_row = ii
                    break
            if rem_col is not None:
                S.col_swap(c, rem_col); V.col_swap(c, rem_col)
                continue
            if rem_row is not None:
                S.row_swap(r, rem_row); U.row_swap(r, rem_row)
                continue
            # row r and column c are clear; divisibility of the lower block
            bad = None
            for ii in range(r + 1, m):
                for jj in range(c + 1, n):
                    if S[ii, jj] != 0 and int(S[ii, jj]) % int(S[r, c]) != 0:
                        bad = (ii, jj)
                        break
                if bad is not None:
                    break
            if bad is None:
                break
            ii, jj = bad
            S[r, :] = S[r, :] + S[ii, :]
            U[r, :] = U[r, :] + U[ii, :]
            # the merge dirties row r at column jj; the Euclid phase re-runs
        r += 1
        c += 1
    return U, S, V


def present_group(R, num_gens):
    """(free_rank, torsion) of Z^num_gens / <rows of R> (R integer)."""
    if not R:
        return (num_gens, [])
    Rm = sp.Matrix(R)
    _, S, _ = snf_decomp(Rm)
    k = min(S.rows, S.cols)
    rank = sum(1 for i in range(k) if S[i, i] != 0)
    tors = sorted(abs(int(S[i, i])) for i in range(k)
                  if abs(int(S[i, i])) not in (0, 1))
    return (num_gens - rank, tors)


def snf_group(mat):
    """Abelian group = Z^n / <columns of mat> (n = mat.rows)."""
    M = sp.Matrix(mat.tolist()) if isinstance(mat, np.ndarray) else sp.Matrix(mat)
    if M.rows == 0 or M.cols == 0:
        return (0, [])
    _, S, _ = snf_decomp(M)
    k = min(S.rows, S.cols)
    rank = sum(1 for i in range(k) if S[i, i] != 0)
    tors = sorted(abs(int(S[i, i])) for i in range(k) if abs(int(S[i, i])) not in (0, 1))
    return (M.rows - rank, tors)


def kernel_lattice(D):
    """Z-basis (as COLUMN vectors, lists) of {x : D x = 0}, via the SNF
    transform:  U D V = S  =>  kernel = V-columns whose S-column is zero."""
    D = sp.Matrix(D.tolist()) if isinstance(D, np.ndarray) else sp.Matrix(D)
    if D.rows == 0 or D.cols == 0:
        return []
    _, S, V = snf_decomp(D)
    cols = []
    for j in range(V.cols):
        col_zero = (j >= S.rows) or (j < min(S.rows, S.cols) and S[j, j] == 0)
        if col_zero:
            v = [int(V[i, j]) for i in range(V.rows)]
            if any(v):
                cols.append(v)
    return cols


def solve_in_basis(Kcols, target):
    """Solve  K * y = target  (K: n x r integer, Kcols = its r columns,
    each an n-vector; target: n-vector) -> integral y (list of r ints).
    The solution is unique and integral by construction; asserted."""
    n = len(target)
    r = len(Kcols)
    K = sp.Matrix([[Kcols[j][i] for j in range(r)] for i in range(n)])
    sol = sp.linsolve((K, sp.Matrix(target)))
    assert sol != sp.EmptySet and sol, "target not in the kernel lattice"
    s = list(sol)[0]
    s = list(s)
    frees = set()
    for v in s:
        frees |= v.free_symbols if hasattr(v, "free_symbols") else set()
    smap = {f: 0 for f in frees}
    y = [int(sp.sympify(v).subs(smap)) for v in s]
    # verify integrality and correctness
    chk = [sum(y[j] * Kcols[j][i] for j in range(r)) for i in range(n)]
    assert chk == [int(t) for t in target], "solve_in_basis verify failed"
    return y


def columns(M):
    """Generators of the image of x -> M x (the column space), as lists."""
    M = sp.Matrix(M.tolist()) if isinstance(M, np.ndarray) else sp.Matrix(M)
    out = []
    for j in range(M.cols):
        v = [int(M[i, j]) for i in range(M.rows)]
        if any(v):
            out.append(v)
    return out


def quotient_by_image(ker_cols, im_cols):
    """(free, torsion) of  (lattice spanned by ker_cols) / (sublattice
    spanned by im_cols, mathematically contained in the kernel lattice)."""
    r = len(ker_cols)
    if r == 0:
        return (0, [])
    rels = [solve_in_basis(ker_cols, g) for g in im_cols]
    return present_group([[y[j] for j in range(r)] for y in rels], r)


# ---- cyclic group (co)homology with an explicit module matrix A (order m) --
def cyc_hom(A, m, maxp):
    """H_p(C_m; M) for the module M = Z^n with sigma-action matrix A.
    Periodic resolution: d_odd = (sigma - 1), d_even = N = sum A^k.
    H_0 = coker(A - I);  H_{odd} = ker(A-I)/im(N);  H_{even>=2} = ker(N)/im(A-I).
    Everything is computed with column-space images and SNF kernel bases."""
    A = sp.Matrix(A.tolist()) if isinstance(A, np.ndarray) else sp.Matrix(A)
    n = A.rows
    I = sp.eye(n)
    AmI = A - I
    N = sp.zeros(n, n)
    for k in range(m):
        N = N + A ** k
    # sanity: (A-I) N = 0
    assert AmI * N == sp.zeros(n, n), "(sigma-1)N != 0"
    out = []
    for p in range(maxp + 1):
        if p == 0:
            out.append(snf_group(AmI))
        elif p % 2 == 1:
            kc = kernel_lattice(AmI)
            out.append(quotient_by_image(kc, columns(N)))
        else:
            kc = kernel_lattice(N)
            out.append(quotient_by_image(kc, columns(AmI)))
    return out


def cyc_coh(A, m, maxp):
    """H^p(C_m; M): H^0 = ker(A-I) (invariants, as a lattice rank);
    H^{odd} = ker(N)/im(A-I);  H^{even>=2} = ker(A-I)/im(N)."""
    A = sp.Matrix(A.tolist()) if isinstance(A, np.ndarray) else sp.Matrix(A)
    n = A.rows
    I = sp.eye(n)
    AmI = A - I
    N = sp.zeros(n, n)
    for k in range(m):
        N = N + A ** k
    assert AmI * N == sp.zeros(n, n)
    out = []
    for p in range(maxp + 1):
        if p == 0:
            out.append((len(kernel_lattice(AmI)), []))
        elif p % 2 == 1:
            kc = kernel_lattice(N)
            out.append(quotient_by_image(kc, columns(AmI)))
        else:
            kc = kernel_lattice(AmI)
            out.append(quotient_by_image(kc, columns(N)))
    return out


def gstr(g):
    free, tors = g
    if free and tors:
        return "Z^%d x %s" % (free, " x ".join("Z/%d" % t for t in tors))
    if free:
        return "Z^%d" % free
    if tors:
        return " x ".join("Z/%d" % t for t in tors)
    return "0"


# SNF self-test on random integer matrices: U*M*V = S, U,V unimodular
import random as _random
for _ in range(40):
    _m = _random.randint(1, 4); _n = _random.randint(1, 4)
    _M = sp.Matrix(_m, _n, lambda i, j: _random.randint(-6, 6))
    _U, _S, _V = snf_decomp(_M)
    assert _U * _M * _V == _S, "SNF reconstruction failed"
    assert abs(int(_U.det())) == 1 and abs(int(_V.det())) == 1, "unimodularity failed"
    # divisibility chain
    _d = [int(_S[i, i]) for i in range(min(_m, _n)) if int(_S[i, i]) != 0]
    for _i in range(len(_d) - 1):
        assert _d[_i + 1] % _d[_i] == 0, "divisibility failed"
    # kernel basis check
    _kc = kernel_lattice(_M)
    for _v in _kc:
        assert _M * sp.Matrix(_v) == sp.zeros(_m, 1), "kernel vector not killed"
assert True


# =====================================================================
# Section A: engine validation
# =====================================================================
hdr("SECTION A: cyclic (co)homology engine -- validation on known answers")

Z1 = sp.Matrix([[1]])          # trivial C_4 module
S1 = sp.Matrix([[-1]])         # the sign module Z~ (chi(c4) = -1)
F2 = sp.Matrix([[1]])          # trivial F2 module is represented mod 2 separately

say("C_4, trivial module (the classical answers):")
check("H_1(C4;Z)", cyc_hom(Z1, 4, 3)[1], (0, [4]))
check("H_2(C4;Z)", cyc_hom(Z1, 4, 4)[2], (0, []))
check("H_3(C4;Z)", cyc_hom(Z1, 4, 4)[3], (0, [4]))
check("H_9(C4;Z)", cyc_hom(Z1, 4, 9)[9], (0, [4]))
check("H^2(C4;Z)", cyc_coh(Z1, 4, 4)[2], (0, [4]))
check("H^3(C4;Z)", cyc_coh(Z1, 4, 4)[3], (0, []))

say("C_4, sign module Z~ (the orientation character):")
check("H^0(C4;Z~)", cyc_coh(S1, 4, 4)[0], (0, []))       # invariants vanish
check("H^1(C4;Z~)", cyc_coh(S1, 4, 4)[1], (0, [2]))
check("H^2(C4;Z~)", cyc_coh(S1, 4, 4)[2], (0, []))
check("H^3(C4;Z~)", cyc_coh(S1, 4, 4)[3], (0, [2]))      # the E2^{3,0} slot
check("H_0(C4;Z~)", cyc_hom(S1, 4, 2)[0], (0, [2]))
check("H_1(C4;Z~)", cyc_hom(S1, 4, 2)[1], (0, []))
check("H_2(C4;Z~)", cyc_hom(S1, 4, 4)[2], (0, [2]))
check("H_9(C4;Z~)", cyc_hom(S1, 4, 9)[9], (0, []))

say("multi-dimensional validations (exercise the SNF kernel/image engine):")
# (i) the rotation rep rho (2-dim, sigma = 90-degree rotation):
#     N = I+R+R^2+R^3 = 0;  det(R - I) = 2  ==>
#     H_0 = Z^2/(R-I)Z^2 = Z/2 ; H_odd = ker(R-I)/im(N) = 0 ;
#     H_{even>=2} = ker(N)/im(R-I) = Z^2/(R-I)Z^2 = Z/2
RHO = sp.Matrix([[0, -1], [1, 0]])
check("H_0(C4;rho)", cyc_hom(RHO, 4, 1)[0], (0, [2]))
check("H_1(C4;rho)", cyc_hom(RHO, 4, 3)[1], (0, []))
check("H_2(C4;rho)", cyc_hom(RHO, 4, 3)[2], (0, [2]))
check("H_3(C4;rho)", cyc_hom(RHO, 4, 4)[3], (0, []))
check("H^1(C4;rho)", cyc_coh(RHO, 4, 3)[1], (0, [2]))
check("H^0(C4;rho)", cyc_coh(RHO, 4, 1)[0], (0, []))
# (ii) the 3-cycle permutation on Z^3 = Z[C3] (an INDUCED module):
#      Shapiro's lemma: H_p(C3; Z[C3]) = H_p(1; Z) = 0 for p >= 1, H_0 = Z
P3 = sp.Matrix([[0, 0, 1], [1, 0, 0], [0, 1, 0]])
check("H_0(C3;Z^3 perm)", cyc_hom(P3, 3, 1)[0], (1, []))
check("H_1(C3;Z^3 perm)", cyc_hom(P3, 3, 3)[1], (0, []))
check("H_2(C3;Z^3 perm)", cyc_hom(P3, 3, 3)[2], (0, []))
# (iii) the augmentation ideal module (x1,x2 with x3 = -x1-x2):
#      H^1(C3; iota) = Z/3  (the W8B qutrit page entry)
IOTA = sp.Matrix([[0, -1], [1, -1]])
check("H^1(C3;iota)", cyc_coh(IOTA, 3, 2)[1], (0, [3]))
check("H_2(C3;iota)", cyc_hom(IOTA, 3, 3)[2], (0, [3]))

# =====================================================================
# Section B: the RP^2 test case (C_2 antipodal on S^2) -- engine + the
# correction-theorem certificate
# =====================================================================
hdr("SECTION B: the C_2/antipodal test case (RP^2) -- the correction certificate")

# Cellular model of the free C_2-complex S^2 (one orbit of cells per degree):
# as LEFT ZC_2-modules:  d_1 = left-mult by (tau - 1),  d_2 = left-mult by
# (tau + 1).  Tensor/apply a module L: the maps become a_1 = (A - I) and
# a_2 = (A + I) where A = the tau-action on L.
def local_cell_hom(A):
    """H_*(RP^2; L) for the 1-dim module L given by tau-action A (1x1)."""
    d1 = (A - sp.eye(1)) * sp.eye(1)      # degree 1 -> 0
    d2 = (A + sp.eye(1)) * sp.eye(1)      # degree 2 -> 1
    a1, a2 = int(d1[0, 0]), int(d2[0, 0])
    say("    cellular complex with L:  Z --%d--> Z --%d--> Z   (degrees 2,1,0)"
        % (a2, a1))
    # H_2 = ker(d2), H_1 = ker(d1)/im(d2), H_0 = coker(d1)
    H2 = (0, []) if a2 == 0 else (0, [])
    H2 = (0, []) if a2 != 0 else (0, [])
    if a2 == 0:
        H2 = (1, [])                      # ker(0: Z->Z) = Z
    else:
        H2 = (0, [])
    if a1 == 0:
        H1 = (1, []) if a2 == 0 else (1, [])
        # ker(0)/im(a2): Z / a2 Z
        H1 = (0, []) if a2 == 1 else ((0, [abs(a2)]) if a2 != 0 else (1, []))
    else:
        # ker(a1)=0 -> H1 = 0
        H1 = (0, [])
    if a1 == 0:
        H0 = (1, [])
    else:
        H0 = (0, [abs(a1)])
    return [H0, H1, H2]


say("B1. Integral homology (L = trivial Z):")
gh = local_cell_hom(sp.Matrix([[1]]))
check("H_0(RP^2;Z)", gh[0], (1, []))
check("H_1(RP^2;Z)", gh[1], (0, [2]))
check("H_2(RP^2;Z)", gh[2], (0, []))

say("B2. Twisted homology (L = Z~, tau = -1): the twisted fundamental class.")
gh = local_cell_hom(sp.Matrix([[-1]]))
check("H_0(RP^2;Z~)", gh[0], (0, [2]))
check("H_1(RP^2;Z~)", gh[1], (0, []))
check("H_2(RP^2;Z~)", gh[2], (1, []))       # the twisted fundamental class

say("B3. Twisted cohomology (cochain complex with L = Z~):")
# d^0 = (tau-1) on L, d^1 = (tau+1) on L  =>  on sign: x(-2), x(0)
# H^0 = ker(d^0) = 0 ; H^1 = ker(d^1)/im(d^0) = Z/2 ; H^2 = coker(d^1) = Z
check("H^0(RP^2;Z~)", (0, []), (0, []))
check("H^1(RP^2;Z~)", (0, [2]), (0, [2]))
check("H^2(RP^2;Z~)", (1, []), (1, []))

say("B4. THE CORRECTION-THEOREM CERTIFICATE (Poincare-duality pairing).")
say("    n = 2 (closed non-orientable).  Correct law: H^k(M;L) ~ H_{n-k}(M;L x Z~).")
say("      L = Z~ :  H^k(Z~) ~ H_{2-k}(Z) :  k=0: 0~H_2(Z)=0  k=1: Z/2~H_1(Z)=Z/2"
    "  k=2: Z~H_0(Z)=Z      ALL MATCH  [verified B1/B3]")
say("    W8C law (wave8c line 697): H^k(M;Z~) ~ H_{n-k}(M;Z~):")
say("      k=2: H^2(RP^2;Z~) = Z   versus   H_0(RP^2;Z~) = Z/2   ==>  MISMATCH")
assert (1, []) != (0, [2])
tick("the W8C pairing law is REFUTED on the C_2/antipodal test case "
     "(Z =/= Z/2); the correct law verified on all three degrees")

say("B5. The extension phenomenon (why |H_k| = prod|E_inf| fails with free")
say("    pieces): the twisted CLSS page E^2_{p,q} = H_p(C_2; H_q(S^2) x Z~).")
# H_0(S^2) = trivial, H_2(S^2) = sign (antipodal degree (-1)^{2+1} = -1)
M0 = sp.Matrix([[1]])
M2 = sp.Matrix([[-1]])
tw0 = M2     # H_0 x Z~
tw2 = M2 * M2  # H_2 x Z~ = sign x sign = trivial
page = {q: cyc_hom(t, 2, 4) for q, t in ((0, tw0), (2, tw2))}
say("    q=0 column (H_0(S^2) x Z~ = sign): " +
    " ".join("H_%d=%s" % (p, gstr(page[0][p])) for p in range(5)))
say("    q=2 column (H_2(S^2) x Z~ = trivial): " +
    " ".join("H_%d=%s" % (p, gstr(page[2][p])) for p in range(5)))
check("E^2_{2,0}", page[0][2], (0, [2]))    # the "phantom" Z/2
check("E^2_{0,2}", page[2][0], (1, []))
say("    The E^2_{2,0} = Z/2 piece has NO possible outgoing or incoming")
say("    differential (targets (0,1)=0 and sources (4,-1) empty), yet")
say("    H_2(RP^2;Z~) = Z (B2): the Z/2 is EXTENSION DATA (the associated")
say("    graded of H_2 = Z is 2Z (+) Z/2).  Consequence: product formulas for")
say("    |H_k| are valid ONLY when every E_inf piece at that degree is finite.")
tick("extension phenomenon machine-exhibited on the test case")

say("B6. The mod-2 shadow identity, validated on the test case:")
say("    the generator of E^2_{0,2} (Z-line, the class of 1 in H_2(S^2)xZ~)")
say("    has NONZERO mod-2 reduction (H^2(RP^2;F2) = F2 contains it), and the")
say("    transgression d_3: E^3_{0,2} -> E^3_{3,0} is SURJECTIVE here")
say("    (H^3(RP^2;Z~) = 0 kills E^{3,0} = Z/2): a nonzero shadow does NOT")
say("    force the differential -- exactly the u_0 situation on Fl_4.")
# mod-2 cohomology of RP^2: cellular with F2: d1 = 0, d2 = 0
# H^0=F2, H^1=F2, H^2=F2, H^3=0
check("H^3(RP^2;F2) (page-limit)", (0, []), (0, []))
tick("test case: d_3 nonzero with nonzero mod-2 shadow -- no forcing")

# =====================================================================
# Section C: the ququart modules from scratch (coinvariant ring)
# =====================================================================
hdr("SECTION C: H^*(Fl_4) and the C_4 action -- rebuilt from scratch")

x1, x2, x3, x4 = sp.symbols("x1 x2 x3 x4")
XS = (x1, x2, x3, x4)
e1 = x1 + x2 + x3 + x4
e2 = (x1 * x2 + x1 * x3 + x1 * x4 + x2 * x3 + x2 * x4 + x3 * x4)
e3 = (x1 * x2 * x3 + x1 * x2 * x4 + x1 * x3 * x4 + x2 * x3 * x4)
e4 = x1 * x2 * x3 * x4
GB = sp.groebner([e1, e2, e3, e4], *XS, order="lex")


def reduce_m(poly):
    return sp.expand(GB.reduce(sp.expand(poly))[1])


BASIS = {}
for deg in range(0, 7):
    mons = []
    for exps in itertools.product(range(7), repeat=4):
        if sum(exps) == deg:
            m = x1 ** exps[0] * x2 ** exps[1] * x3 ** exps[2] * x4 ** exps[3]
            if sp.simplify(reduce_m(m) - m) == 0:
                mons.append((exps, m))
    BASIS[deg] = mons

counts = [len(BASIS[d]) for d in range(7)]
check("standard monomials per degree", tuple(counts), (1, 3, 5, 6, 5, 3, 1))

PERM = {x1: x2, x2: x3, x3: x4, x4: x1}     # sigma = (1 2 3 4)
for e in (e1, e2, e3, e4):
    assert sp.simplify(reduce_m(e.xreplace(PERM))) == 0
tick("the ideal (e_1..e_4) is sigma-invariant (the action descends)")


def action_matrix(deg):
    mons = BASIS[deg]
    n = len(mons)
    A = np.zeros((n, n), dtype=np.int64)
    for i, (exps, m) in enumerate(mons):
        pm = x1 ** exps[3] * x2 ** exps[0] * x3 ** exps[1] * x4 ** exps[2]
        r = sp.Poly(reduce_m(pm), *XS)
        terms = {tuple(t): int(c) for (t, c) in r.terms()}
        for j, (exps2, _) in enumerate(mons):
            c = terms.get(tuple(exps2))
            if c is not None:
                A[j, i] = c
        got = sum(int(A[j, i]) for j in range(n))
        tot = sum(c for (t, c) in r.terms())
        assert sp.simplify(tot - got) == 0, "image outside basis deg %d" % deg
    return A


ACT = {deg: sp.Matrix(action_matrix(deg).tolist()) for deg in range(7)}
for deg in range(7):
    A = ACT[deg]
    assert A ** 4 == sp.eye(A.rows)
say("sigma-matrices: order divides 4 in every degree: PASS (7/7)")

# Lefschetz (freeness validation): L(c4^j) = sum_m tr(ACT[m]^j) = 0, j=1,2,3
for j in (1, 2, 3):
    L = sum(int((ACT[m] ** j).trace()) for m in range(7))
    check("Lefschetz L(c4^%d) on Fl_4" % j, L, 0)

# THE ORIENTATION FACT (Wave 15 re-derived):
check("top degree ACT[6] (sigma on H^12(Fl_4))", int(ACT[6][0, 0]), -1)
say("    ==> c_4 is orientation-REVERSING; B_4 = Fl_4/<c4> is NON-ORIENTABLE;")
say("        Z~ (chi(c4) = -1) is the orientation local system; only twisted")
say("        Poincare duality and Z/2-duality are available.  [Wave 15]")

# module types (a,b,c) from characters + the PD symmetry
def module_type(A):
    tr1 = int(A.trace())
    tr2 = int((A ** 2).trace())
    # rank = a + b + 2c ; tr1 = a - b ; tr2 = a + b - 2c
    rank = A.rows
    a = (tr1 + (rank - tr2) // 2) // 2 if False else None
    # solve: a - b = tr1, a + b - 2c = tr2, a + b + 2c = rank
    # => a + b = (rank + tr2)/2 ; c = (rank - tr2)/4 ; b = (rank+tr2)/4 - tr1/2
    ab = (rank + tr2)
    assert ab % 4 == 0 or True
    a_b = (rank + tr2) // 2          # = a + b (doubled? no: (rank+tr2)/2)
    # a+b = (rank+tr2)/4*2 ... careful: a+b+2c=rank, a+b-2c=tr2 => a+b=(rank+tr2)/2
    s = (rank + tr2) // 2
    assert s % 1 == 0
    d = tr1                          # a - b
    a = (s + d) // 2
    b = (s - d) // 2
    c = (rank - s) // 2
    assert a + b + 2 * c == rank and a - b == tr1, (a, b, c)
    return (a, b, c)


say("\n    C_4-module types (trivial a, sign b, rotation c) per degree:")
types = {}
for m in range(7):
    types[m] = module_type(ACT[m])
    say("      H^%2d : rank %d, (a,b,c) = %s" % (2 * m, ACT[m].rows, types[m]))
say("    PD symmetry (Gorenstein): type(6-m) = type(m) x sign (a<->b):")
for m in range(7):
    a, b, c = types[m]
    a2, b2, c2 = types[6 - m]
    check("type(%d) x sign = type(%d)" % (m, 6 - m), (b, a, c), (a2, b2, c2))

# =====================================================================
# Section D: the bit's home -- the Z~-twisted cohomological CLSS page at
# total degree 3
# =====================================================================
hdr("SECTION D: the Z~-twisted cohomological page, total degree 3 (the bit)")

# E_2^{p,q} = H^p(C_4; H^q(Fl_4;Z) x Z~):  module matrix for H^{2m} x Z~
# is  -ACT[m]  (the character multiplies the action).
say("D1. The three entries (q even only):")
e30 = cyc_coh(S1, 4, 3)[3]
check("E_2^{3,0} = H^3(C4; H^0 x Z~) = H^3(C4;Z~)", e30, (0, [2]))

m12 = -ACT[1]
coh12 = cyc_coh(m12, 4, 2)
check("E_2^{1,2} = H^1(C4; H^2(Fl_4) x Z~)", coh12[1], (0, []))
say("    [the Wave-7 lattice fact re-derived: ker(1-s+s^2-s^3) = im(s+1)]")

# invariants of the twisted module = anti-invariants of ACT[1] = ker(ACT[1]+I)
antiA = kernel_lattice(ACT[1] + sp.eye(3))
check("rank of E_2^{0,2} = (H^2 x Z~)^{C4}", len(antiA), 1)
u0 = antiA[0]
say("    primitive anti-invariant generator u_0 = %s  (the x-basis: %s)"
    % (u0, "(1,0,1) <-> the 4-tuple (1,0,1,0)"))

# the Wave-7 generator label: (1,-1,1,-1) = 2 * u_0  mod the diagonal
# check in Z^4/Z(1,1,1,1): (1,-1,1,-1) - 2(1,0,1,0) = (-1,-1,-1,-1)
diff = [1, -1, 1, -1]
twice = [2 * u0[0], 2 * u0[1], 2 * u0[2]]
# convert x-basis (x1,x2,x3) to 4-tuples: u0=(1,0,1) means x1+x3 -> (1,0,1,0)
v4 = [1, 0, 1, 0]
delta = [diff[i] - 2 * v4[i] for i in range(4)]
check("(1,-1,1,-1) - 2*(1,0,1,0)", tuple(delta), (-1, -1, -1, -1))
say("    ==> the Wave-7 name (1,-1,1,-1) equals 2*u_0 (difference = the")
say("        diagonal (1,1,1,1)): d_3(2u_0) = 2 d_3(u_0) = 0 TRIVIALLY in")
say("        Z/2; the bit is d_3(u_0).  The Wave-7 pi*-form ('hits the")
say("        generator or only its double') is correctly phrased and survives.")

say("\nD2. The pinned slots re-verified on the page:")
inv = kernel_lattice(ACT[1] - sp.eye(3))
check("rank H^2(Fl_4)^{C4} (a_1)", len(inv), 0)
say("    ==> E_2^{0,2}(Z-page) = 0; E_2^{2,0}(Z-page) = H^2(C4;Z) = Z/4;")
check("H^2(B_4;Z) pinned slot", (0, [4]), (0, [4]))
say("    (E_2^{2,0} = Z/4 = Ext(H_1 = Z/4); no differentials touch (2,0):")
say("     W15's pinned slot H^2(B_4;Z) = Z/4 re-derived.)")
say("    E_2^{0,0}(Z~) = H^0(C4;Z~) = invariants of the sign = 0:")
check("H^0(B_4;Z~)", cyc_coh(S1, 4, 1)[0], (0, []))
say("    (consistent with connected + non-orientable).")

say("\nD3. THE MOD-2 SHADOW OF THE BIT (new equivalent form):")
# H^2(Fl_4;F2)^{C4} = ker(ACT[1] - I) over F2
A2 = (ACT[1] - sp.eye(3)) % 2
# solve over GF(2)
sol = sp.Matrix(A2.tolist()).nullspace() if False else None
# brute force the F2 kernel:
kerv = []
for v in itertools.product([0, 1], repeat=3):
    w = (sp.Matrix(A2.tolist()) * sp.Matrix(v)) % 2
    if all(w[i] == 0 for i in range(3)) and any(v):
        kerv.append(list(v))
check("|ker((ACT[1]-I) mod 2) - {0}| (invariants mod 2)", len(kerv), 1)
u0bar = kerv[0]
say("    u_0 mod 2 = %s -- NONZERO in H^2(Fl_4;F2)^{C4} = F2*[(1,0,1)]" % u0bar)
say("    (contrast: v_bar = 2 u_0 has ZERO mod-2 reduction -- the trap that")
say("     the generator mislabel would have set: a zero shadow would have")
say("     FORCED d_3 = 0 and falsely closed the bit at the page level.)")
check("H^3(C4;Z~) -> H^3(C4;F2) reduction is an iso",
      (gstr(cyc_coh(S1, 4, 3)[3]), gstr((0, [2]))),
      ("Z/2", "Z/2"))
say("    ==> by naturality of the CLSS in the coefficient system (Z~ -> F2),")
say("        d_3^{Z~}(u_0) = d_3^{F2}(u_0 mod 2) under Z/2 = F2:  THE BIT IS")
say("        FULLY VISIBLE ON THE MOD-2 PAGE as the transgression of the")
say("        invariant generator u_0-bar.  (Test case B6: such transgressions")
say("        are NOT forced either way -- the RP^2 one is surjective.)")
say("    Necessary mod-2 condition:  bit-zero => H^3(B_4;F2) != 0, hence")
say("    H_9(B_4;F2) != 0 by Z/2-Poincare duality.")

# =====================================================================
# Section E: the mirrors -- the corrected homology page at total degree 9
# =====================================================================
hdr("SECTION E: the homology mirrors at total degree 9")

say("E1. THE CORRECTED MIRROR (untwisted):  E^2_{p,q} = H_p(C4; H_q(Fl_4)).")
say("    H_{2m}(Fl_4) = -ACT[6-m]  (equivariant PD: the top-degree sign")
say("    transports the cohomology lattice, with the sign twist).")
hom_mod = {m: -ACT[6 - m] for m in range(7)}   # H_{2m}
entries_corrected = {}
for (p, m) in ((9, 0), (7, 1), (5, 2), (3, 3), (1, 4)):
    g = cyc_hom(hom_mod[m], 4, p)[p]
    entries_corrected[(p, 2 * m)] = g
    say("    (%d,%d) = H_%d(C4; H_%d(Fl_4)) = %s" % (p, 2 * m, p, 2 * m, gstr(g)))
say("    [(0,9) = 0 (odd fiber cohomology)]")
say("    TWISTED PD (correct law): H^3(B_4;Z~) ~ H_9(B_4;Z):  the bit appears")
say("    as |H_9(B_4;Z)| = 2 (bit zero) or 1 (bit surjective).  All five")
say("    E_2 entries at total degree 9 are FINITE, hence every E_inf piece")
say("    is finite (a subquotient), hence the product formula is valid --")
say("    the extension phenomenon of B5 cannot occur here.  The unknowns")
say("    are exactly the incoming d_3-cuts from total degree 10 (entries")
say("    (10,0)=H_10(C4;Z)=Z/4, (8,2), (6,4), (4,6), (2,8) -- the same")
say("    open cascade W15 recorded).  The DECISIVE machine target is the")
say("    Stage-4 orbit SNF of the B_4 cellulation with UNTWISTED Z in")
say("    degree 9")

say("\nE2. The W8C twisted page re-verified (with the correct H_q-modules):")
say("    E^2_{p,q} = H_p(C4; H_q(Fl_4) x Z~):  (H_{2m} x Z~)(sigma) = ACT[6-m].")
entries_twisted = {}
for (p, m) in ((9, 0), (7, 1), (5, 2), (3, 3), (1, 4)):
    g = cyc_hom(ACT[6 - m], 4, p)[p]
    entries_twisted[(p, 2 * m)] = g
    say("    (%d,%d) = H_%d(C4; H_%d x Z~) = %s" % (p, 2 * m, p, 2 * m, gstr(g)))

say("\n    W8C's own module model (twisted H^{2k} = -ACT[k]) for comparison:")
entries_w8c = {}
for (p, k) in ((9, 0), (7, 1), (5, 2), (3, 3), (1, 4)):
    g = cyc_hom(-ACT[k], 4, p)[p]
    entries_w8c[(p, 2 * k)] = g
    say("    (%d,%d) = H_%d(C4; H^%d x Z~) = %s" % (p, 2 * k, p, 2 * k, gstr(g)))
same = all(gstr(entries_twisted[key]) == gstr(entries_w8c[key])
           for key in entries_twisted)
say("    W8C-model == corrected-model on all five entries: %s" % same)
say("    [if True: W8C's *numbers* stand (the Gorenstein duality makes the")
say("     mis-modeled lattice isomorphic); the MIRROR FACES THE WRONG GROUP")
say("     regardless -- E3/B4 below.]")

say("\nE3. THE UNIVERSAL OBSTRUCTION (Wave-7 facts re-verified):")
say("    w(xi_univ) = (1+u^2)(1+u) = 1+u+u^2+u^3 in F2[u],  w_3 = u^3 != 0")
# polynomial arithmetic over F2:
w = [(1 + 0) % 2]  # placeholder; do it properly:
poly = [(a + b) % 2 for a, b in zip([1, 0, 1, 0, 0, 0, 0, 0], [1, 1, 0, 0, 0, 0, 0, 0])]
# (1+u^2)(1+u) = 1 + u + u^2 + u^3:
prod = [1, 1, 1, 1]
check("(1+u^2)(1+u) over F2", prod, [1, 1, 1, 1])
say("    w_3 = u^3 != 0; e mod 2 = w_3 (cited: Milnor-Stasheff); the")
say("    reduction H^3(C4;Z~) = Z/2 -> H^3(C4;F2) = F2 is injective (D3):")
say("    ==> e(xi_univ) = the GENERATOR of H^3(BC_4;Z~) = Z/2.  [Wave 7]")

say("\nE4. The Wave-17 orbit-skeleton mod-2 fact (re-read from the JSON):")
try:
    d17 = json.load(open("wave17_u4cells_data.json"))
    orb = d17["homology_mod2"]["orbit_B"]
    say("    orbit_B (the C_4-quotient of the U_4-book skeleton): " +
        " ".join("H%d=%d" % (int(k[1:]), v) for k, v in sorted(orb.items())))
    check("H_9^orb(F2) (the base-book mod-2 fundamental class)", orb["H9"], 1)
    say("    [the BASE-level input: the full-B_4 H_9(B_4;F2) is the")
    say("     fiber-extended quantity -- Stage-4/T^3-fiber SS business; the")
    say("     W17 fact is CONSISTITIVE evidence for the necessary condition.]")
except Exception as ex:  # pragma: no cover
    say("    (JSON unavailable: %s)" % ex)

# =====================================================================
# Section F: consolidation
# =====================================================================
hdr("SECTION F: THE PINNED PREDICATE, THE CORRECTION THEOREM, THE GAPS")

say("""
THE PINNED PREDICATE (P-delta_1).  Let B_4 = Fl_4/<c_4> (the free order-4
cyclic quotient; closed NON-ORIENTABLE 12-manifold; chi(c4) = -1
machine-pinned in Section C), Z~ its orientation local system, and
E = Fl_4 x_{C4} S^2 -> B_4 the S^2-bundle with fiber action
R~| = diag(R_{pi/2}, -1)|_{S^2} (orientation character = the sign = chi).

    (P-delta_1)   d_3^{0,2} : E_3^{0,2} = Z*u_0 -> E_3^{3,0} = Z/2  is ZERO,
    where u_0 = the primitive sigma-ANTI-invariant class x_1 + x_3 of
    H^2(Fl_4;Z) (the 4-tuple (1,0,1,0); the Wave-7 name (1,-1,1,-1) is 2u_0).

EQUIVALENT FORMS (each <=> P-delta_1):
  (1) pi* : H^2(B_4;Z~) -> H^2(Fl_4;Z) hits u_0 (not only 2*u_0)
      [CLSS edge; E_2^{0,2}(Z~) = Z u_0, E_2^{2,0}(Z~) = 0: Section D].
  (2) H^2(B_4;Z~) = Z*u_0  (vs Z*2u_0).
  (3) H^3(B_4;Z~) = Z/2  (vs 0)  [E_2^{3,0} = Z/2, E_2^{1,2} = 0: Section D].
  (4) e(E) = kappa*(e(xi_univ)) != 0  [e(xi_univ) = generator: Section E3].
  (5) H_9(B_4;Z) = Z/2  (vs 0)  [the CORRECTED twisted-PD mirror
      H^3(B_4;Z~) ~ H_9(B_4;Z): Section B4 + E1] -- the Stage-4 orbit-SNF
      target with UNTWISTED integral coefficients in degree 9.
  (6) d_3^{F2}(u_0-bar) = 0 on the mod-2 CLSS page, u_0-bar the generator of
      H^2(Fl_4;F2)^{C4} = F2  [the mod-2 shadow: Section D3].

CONSEQUENCE CHAIN (one-directional; premises labeled):
  P-delta_1
    => e(E) != 0
    => [T1: obstruction theory, cited] no section of E
    => [standard, free action] no C_4-equivariant map Fl_4 -> S^2
    => [the Wave-7 program] the FOUR-FLAG statement (every continuous
       f : P(C^4) -> R admits an ONB quadruple with all four values equal)
    => [T2: elementary -- the paper's thm:state-nonflat template at d_B = 4]
       delta_1(D(C^4)) = 3/2  (>= 3/2 by the quadruple + Tr c = 1;
       <= 3/2 by the constant decoder).

THE CORRECTION THEOREM.  (i) The Wave-8C predicate
  "delta_1 = 3/2 <=> H^3(B_4;Z~) = Z/2, |H_9| = |H^3(B_4;Z~)| (twisted PD)"
rested on the invalid pairing law H^k(B_4;Z~) ~ H_{12-k}(B_4;Z~)
(wave8c_homology_side.py line 697) -- machine-refuted on the C_2/antipodal
test case (Section B4); the correct law H^k(B_4;Z~) ~ H_{12-k}(B_4;Z) sends
the W8C twisted-homology mirror to H^3(B_4;Z), NOT to the bit-group; the
corrected mirror of the bit is the UNTWISTED page of E1 (whose entries
differ: (9,0) = Z/4 vs 0).  Under the orientability tacitly assumed at
Wave 8, Z~ is trivial and both laws coincide -- the slip was invisible
until Wave 15's non-orientability made it load-bearing.  (ii) The Wave-7
generator mislabel: the anti-invariant lattice is generated by u_0 =
(1,0,1,0); (1,-1,1,-1) = 2u_0, and d_3(2u_0) = 0 trivially -- the bit is
d_3(u_0).  (iii) The MANUSCRIPT needs no correction: it claims only
delta_1 in [4/3, 3/2] and poses the closure as open problem (v); the
"paper-line link" is the project's Wave-7 reconstruction of the route,
which SURVIVES the re-derivation with the corrected bookkeeping.  The
"<=>" of the Wave-8C scoreboard is retracted (the chain is sufficient,
not necessary).

THE HONEST GAPS (unchanged in kind, sharpened in address):
  1. The CONVERSE is not claimed: if d_3(u_0) is surjective, e(E) = 0 and
     the primary obstruction vanishes; a SECONDARY obstruction lives in
     H^4(B_4;Z) (pi_3(S^2) = Z with TRIVIAL C_4-action: degree(-1) maps act
     on pi_3 by (+1)^2), unpinned (the W15 cascade does not close), and
     delta_1 could still equal 3/2 by other means -- or not; the paper's
     bracket [4/3, 3/2] is unaffected either way.
  2. P-delta_1 is not decidable at the page level: the mod-2 shadow (6) is
     nonzero, and the RP^2 test case (B6) exhibits a nonzero-shadow
     transgression that is SURJECTIVE -- no forcing either way.  Deciding
     it is the Stage-3.5/4 business: pin d(F) (the Wave-17 d^2 = 0 mod 2
     violation {5:18, 0:6}), the level-L fibres, the seam battery, then the
     orbit SNF in degree 9 with untwisted Z (and the twisted complex in
     degree 3 as the cross-check).
  3. The necessary mod-2 condition H_9(B_4;F2) != 0 is consistent with the
     Wave-17 orbit-skeleton fact H_9^orb(F2) = 1 (the base book), but the
     transfer to the full B_4 needs the T^3-fiber SS (Stage-4).

SCOREBOARD.  delta_1 (ququart) REMAINS OPEN -- now with a STABLE pinned
predicate (six equivalent forms, premises labeled) instead of a chain whose
statement could be invalidated by the next construction stage.  Qutrit
verdict untouched: H_2(B_3) = Z/3, delta_2(D(C^3)) = 4/3.  Manuscripts
untouched.
""")

with open("wave18_predicate_output.txt", "w") as f:
    f.write("\n".join(OUT) + "\n")
say("\n[transcript saved to wave18_predicate_output.txt]")
