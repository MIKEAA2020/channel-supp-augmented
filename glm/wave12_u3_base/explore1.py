import numpy as np

def unistoch_moduli(U):
    """D_ij = |U_ij|^2. Rows i, cols j."""
    return np.abs(U)**2

def rowpair_triple(D, i, j):
    """the triple (sqrt(D_i1 D_j1), sqrt(D_i2 D_j2), sqrt(D_i3 D_j3))"""
    return np.sqrt(D[i,:]*D[j,:])

def tri_ok(a, tol=1e-9):
    a=np.sort(a)
    return a[2] <= a[0]+a[1]+tol  # degenerate allowed

def all_rowpair_ok(D, tol=1e-9):
    for (i,j) in [(0,1),(0,2),(1,2)]:
        if not tri_ok(rowpair_triple(D,i,j), tol):
            return False
    return True

def is_doubly_stochastic(D, tol=1e-9):
    return (np.all(D>= -tol) and
            np.allclose(D.sum(axis=1),1,atol=tol) and
            np.allclose(D.sum(axis=0),1,atol=tol))

rng=np.random.default_rng(0)

# ---- TEST 1: forward. random unitaries -> D must satisfy all row-pair triangle ineqs
bad=0
N=200000
for _ in range(N):
    z=(rng.standard_normal((3,3))+1j*rng.standard_normal((3,3)))
    U,_=np.linalg.qr(z)
    D=unistoch_moduli(U)
    if not all_rowpair_ok(D):
        bad+=1
print(f"forward test: {bad}/{N} random unitaries violate row-pair triangle ineq (want 0)")

# also random 'structured' via polar/symmetric complex gaussian: fine, generic is enough.

# ---- TEST 2: backward-ish. Does a D satisfying all inequalities come from SOME unitary?
# Use the known sufficiency: build U from columns greedily? Instead: for a sample of such D,
# try to find phases to make rows orthogonal. We'll do a constructive check via direct search below.
print("done fwd")
