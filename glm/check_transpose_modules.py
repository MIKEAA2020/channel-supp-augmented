#!/usr/bin/env python3
"""Check: are the coinvariant shift modules conjugate (over GL_n(Z)) to their
transposes?  (Needed: the homology CLSS page uses H_q(Fl_d) = the TRANSPOSE
modules, while the cohomology page uses the coinvariant matrices directly.)
If conjugate, the homology H_p values coincide and no fix is needed."""
import sys
sys.path.insert(0, '/home/z/my-project/scripts')
# import the machinery without running the whole wave8c script
import importlib.util
src = open('/home/z/my-project/scripts/wave8c_homology_side.py').read()
# extract just the helper section (before "SECTION A" prints)
head = src[:src.index('def hdr(s):')]
ns = {}
exec(head, ns)
mat_mul = ns['mat_mul']; cyc_hom = ns['cyc_hom']; cyc_coh = ns['cyc_coh']

# rebuild coinvariant_module from the file
start = src.index('def coinvariant_module(d, k):')
end = src.index('print("  building C_4-modules')
mod_src = src[start:end]
ns2 = dict(ns)
exec(mod_src, ns2)
coinvariant_module = ns2['coinvariant_module']

def transpose(A):
    return [[A[j][i] for j in range(len(A))] for i in range(len(A))]

def find_conjugator(A, B):
    """Search small unimodular U with U A = B U (brute force over entries in
    -2..2 for small n).  Returns U or None."""
    n = len(A)
    from itertools import product as iproduct
    rng = range(-2, 3)
    # A and B are conjugate iff A^k and B^k have equal traces for all k and
    # the modules are isomorphic; brute force only for n <= 3:
    if n > 3:
        return "skip-brute-force"
    # solve U A = B U: linear equations in the entries of U
    # U A - B U = 0: n^2 equations, n^2 unknowns
    import itertools
    # set up: for each (i,j): sum_k U[i][k] A[k][j] - sum_k B[i][k] U[k][j] = 0
    rows = []
    for i in range(n):
        for j in range(n):
            row = [0] * (n * n)
            for k in range(n):
                row[i * n + k] += A[k][j]
                row[i * n + j] -= B[i][k] * 0  # placeholder
            rows.append(row)
    # redo properly:
    rows = []
    for i in range(n):
        for j in range(n):
            row = [0] * (n * n)
            for k in range(n):
                row[i * n + k] += A[k][j]          # U[i][k] * A[k][j]
            for k in range(n):
                row[k * n + j] -= B[i][k]          # B[i][k] * U[k][j]
            rows.append(row)
    # find integer kernel of rows (solutions U with UA = BU), then require
    # det(U) = +-1
    kb = ns['kernel_basis'](rows) if rows else []
    if not kb:
        return None
    # search integer combinations of the kernel basis with det = +-1
    # kernel basis vectors reshaped to matrices
    mats = []
    for v in kb:
        mats.append([v[i * n:(i + 1) * n] for i in range(n)])
    if len(mats) == 1:
        U = mats[0]
        d = det(U)
        if abs(d) == 1:
            return U
        # try scaling? no.  None.
        return None
    # small search over combinations (2 basis vectors, coefficients -3..3)
    import itertools
    for c1 in range(-3, 4):
        for c2 in range(-3, 4):
            U = [[c1 * mats[0][i][j] + c2 * mats[1][i][j] for j in range(n)]
                 for i in range(n)]
            if det(U) in (1, -1):
                return U
    return None

def det(U):
    n = len(U)
    if n == 1:
        return U[0][0]
    if n == 2:
        return U[0][0] * U[1][1] - U[0][1] * U[1][0]
    s = 0
    for j in range(n):
        if U[0][j]:
            minor = [[U[i][k] for k in range(n) if k != j] for i in range(1, n)]
            s += ((-1) ** j) * U[0][j] * det(minor)
    return s

print("QUTRIT (d=3): iota module A = [[0,-1],[1,-1]]")
IOTA = [[0, -1], [1, -1]]
IT = transpose(IOTA)
U = find_conjugator(IOTA, IT)
print("  A ~ A^T :", "YES (conjugator found)" if U not in (None, "skip-brute-force") else
      ("UNKNOWN (brute force failed)" if U == "skip-brute-force" else "NO"))
hi_A = cyc_hom(IOTA, 3, 6)
hi_AT = cyc_hom(IT, 3, 6)
print("  H_p(C3; A-module): ", hi_A[:5])
print("  H_p(C3; A^T-module):", hi_AT[:5])
assert hi_A == hi_AT, "qutrit: transpose module differs!"
print("  [ok] homology groups identical for A and A^T modules.")

print("\nQUQUART (d=4): degree-1 and degree-2 coinvariant modules")
A1, _ = coinvariant_module(4, 1)
A2, _ = coinvariant_module(4, 2)
for name, A in (("deg1", A1), ("deg2", A2)):
    AT = transpose(A)
    hA = cyc_hom(A, 4, 6)
    hAT = cyc_hom(AT, 4, 6)
    same = (hA == hAT)
    print(f"  {name}: H_p(C4; A)   = {hA[:5]}")
    print(f"  {name}: H_p(C4; A^T) = {hAT[:5]}   identical: {same}")
    # twisted: g -> -A  vs g -> -(A^T)
    mA = [[-x for x in row] for row in A]
    mAT = [[-x for x in row] for row in AT]
    tA = cyc_hom(mA, 4, 10)
    tAT = cyc_hom(mAT, 4, 10)
    print(f"  {name} twisted: H_p(C4; -A)   = {tA[:6]}")
    print(f"  {name} twisted: H_p(C4; -A^T) = {tAT[:6]}   identical: {tA == tAT}")
print("""
CONCLUSION: if identical, the wave8c homology-page values computed with the
cohomology matrices are correct as-is; the transpose conjugation is
harmless.  (Any difference would require fixing Section C/D modules.)""")
