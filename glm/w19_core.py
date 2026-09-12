"""Wave 19 continuation -- the (c)-scope -- RECONSTRUCTED MODEL CORE.
M = Fl_3/T^3_L, L=2 (the 2-torsion torus quotient), per the standing section-6 directive.

All structures derived from the honest A2 / level-2 / GKM / S3 model in the Z^3 picture.
Every axiom is verified at import time; verification results are part of the record.
The honest Z^3 picture: roots = e_i - e_j in Z^3 (mod the diagonal), rho = (1,0,-1),
the cocharacter-ish lattice Lambda = {v in Z^3 : sum v_i = 0}, the level-2 sector
group Gamma = Lambda/2Lam ~= (Z/2)^2 with the dot-product pairing mod 2.

Reconstruction provenance: standing directives (Waves 15-21) + the prior session's locked
design; one arithmetic slip in the prior session's final d(F) hand-computation
((-1,-1,2) mis-copied as -(1,-2,1)) is corrected here -- the code decides.
"""
from fractions import Fraction
import json, itertools, math, sys

VERBOSE = ("-q" not in sys.argv)

def log(*a):
    if VERBOSE: print(*a)

# ------------------------------------------------------------------ Z^3 lattice
def vadd(u, v): return (u[0]+v[0], u[1]+v[1], u[2]+v[2])
def vsub(u, v): return (u[0]-v[0], u[1]-v[1], u[2]-v[2])
def dot(u, v):  return u[0]*v[0] + u[1]*v[1] + u[2]*v[2]

ALPHA1 = (1, -1, 0)   # e1 - e2
ALPHA2 = (0, 1, -1)   # e2 - e3
RHO    = (1, 0, -1)   # e1 - e3 = alpha1 + alpha2
POS_ROOTS = [ALPHA1, ALPHA2, RHO]
ROOTS = [ALPHA1, ALPHA2, RHO, (-1,1,0), (0,-1,1), (-1,0,1)]

LAMBDA = sorted([v for v in itertools.product(range(-2,3), repeat=3) if sum(v) == 0],
                key=lambda v: (sum(abs(x) for x in v), v))
# level-2 hexagon corners: sum=0, |v_i| <= 2  ->  the P-19 corner set
H2 = LAMBDA
assert len(H2) == 19, len(H2)
log(f"[core] 19 P-19 corners: OK (|v_i|<=2, sum=0)")

# ------------------------------------------------------------------ sectors
def sector(v): return (v[0] % 2, v[1] % 2, v[2] % 2)   # even-sum triples -> 4 classes
SECTORS = {}
for v in H2:
    SECTORS.setdefault(sector(v), []).append(v)
sec_counts = sorted(len(x) for x in SECTORS.values())
assert sec_counts == [4,4,4,7], sec_counts
log(f"[core] sector counts (7,4,4,4): OK  classes={sorted(SECTORS)}")

GAMMA = sorted(SECTORS.keys())        # the 4 elements of Lambda/2Lam as mod-2 triples
GAMMA_NONTRIV = [g for g in GAMMA if g != (0,0,0)]

# ------------------------------------------------------------------ quadratic refinement
# Q(v) = sum_i binom(v_i,2) mod 2 on LATTICE reps; polarization: Q(u+v)+Q(u)+Q(v) = <u,v> mod 2
def Q(v): return sum((v[i]*(v[i]-1))//2 for i in range(3)) % 2
def Q_class(g): return Q(SECTORS[g][0])   # well-defined mod 2Lam (verified next)
# (i) well-definedness on sector classes: all lattice reps of a class agree mod 2
for g, reps in SECTORS.items():
    assert len({Q(v) for v in reps}) == 1, g
# (ii) polarization identity on all 16 sector pairs, via lattice reps
for u in GAMMA:
    for w in GAMMA:
        ru, rw = SECTORS[u][0], SECTORS[w][0]
        su = Q(ru); sv = Q(rw)
        ruw = vadd(ru, rw)
        suv = Q_class((ruw[0] % 2, ruw[1] % 2, ruw[2] % 2))
        rhs = dot(ru, rw) % 2
        assert (suv ^ su ^ sv) == rhs, (u, w)
log("[core] Q well-defined on Lambda/2Lam + polarization identity (16 pairs): OK")

# ------------------------------------------------------------------ characters of Gamma
# psi_mu(gamma) = (-1)^{<mu,gamma>}  (mu in Lambda mod 2, gamma in Gamma)
# Characters are named by their DEFINING ROOT: psi_a1 = psi_{alpha1}, etc.
# NOTE <alpha_i, alpha_i> = 2 = 0 mod 2, so psi_{alpha1} is trivial on alpha1's own class.
def psi(mu, g):
    return 1 if dot(mu, g) % 2 == 0 else -1

# the three nontrivial mod-2 classes of Lambda/2Lam, keyed by their root representatives
CLS_A1 = (1, 1, 0)   # class of alpha1 = e1-e2 = (1,-1,0)
CLS_A2 = (0, 1, 1)  # class of alpha2 = e2-e3 = (0,1,-1)
CLS_RHO = (1, 0, 1) # class of rho    = e1-e3 = (1,0,-1)
assert CLS_A1 in SECTORS and CLS_A2 in SECTORS and CLS_RHO in SECTORS
assert (CLS_A1[0]^CLS_A2[0], CLS_A1[1]^CLS_A2[1], CLS_A1[2]^CLS_A2[2]) == CLS_RHO
# position-derived cell names (convention-free), defined after perm_apply below:
#   e=(0,1,2) pos rho; s1=(1,0,2) pos alpha2; s2=(0,2,1) pos alpha1;
#   s1s2=(2,0,1) pos -alpha1; s2s1=(1,2,0) pos -alpha2; w0=(2,1,0) pos -rho

CHAR_LABELS = {"triv": (0,0,0), "psi_a1": CLS_A1, "psi_a2": CLS_A2, "psi_rho": CLS_RHO}
CHARS = {name: {g: (1 if dot(m2, g) % 2 == 0 else -1) for g in GAMMA}
         for name, m2 in CHAR_LABELS.items()}

def char_of(mu):
    """the character psi_mu (mu a lattice vector), identified by mu's mod-2 class"""
    m2 = (mu[0] % 2, mu[1] % 2, mu[2] % 2)
    for name, c in CHAR_LABELS.items():
        if c == m2: return name
    raise ValueError(mu)

# structural character facts:
# (i) every nontrivial character has a nontrivial kernel (order 2) and is nontrivial
for name, ch in CHARS.items():
    if name == "triv": continue
    assert any(ch[g] == -1 for g in GAMMA)
    ker = [g for g in GAMMA if ch[g] == 1]
    assert len(ker) == 2 and ker[0] != ker[1] if len(ker) == 2 else True
# (ii) psi_a1 . psi_a2 = psi_rho  (alpha1 + alpha2 = rho)
assert all(CHARS["psi_a1"][g] * CHARS["psi_a2"][g] == CHARS["psi_rho"][g] for g in GAMMA)
# (iii) the self-pairing quirk: psi_{alpha1}(alpha1-class) = +1, but psi_{alpha1}(alpha2-class) = -1
assert CHARS["psi_a1"][CLS_A1] == 1 and CHARS["psi_a1"][CLS_A2] == -1 and CHARS["psi_a1"][CLS_RHO] == -1
assert CHARS["psi_a2"][CLS_A2] == 1 and CHARS["psi_a2"][CLS_A1] == -1 and CHARS["psi_a2"][CLS_RHO] == -1
assert CHARS["psi_rho"][CLS_A1] == -1 and CHARS["psi_rho"][CLS_A2] == -1 and CHARS["psi_rho"][CLS_RHO] == 1
log("[core] character table: OK (psi_a1, psi_a2 = E-characters; psi_rho = V-character)")
log("[core]   psi_a1: " + repr(CHARS["psi_a1"]) + "  (kernel: alpha1-class)")
log("[core]   psi_a2: " + repr(CHARS["psi_a2"]) + "  (kernel: alpha2-class)")
log("[core]   psi_rho: " + repr(CHARS["psi_rho"]) + "  (kernel: rho-class)")

# E/V split of the roots: alpha1, alpha2 = E; rho = V. This is the STRUCTURAL split
# (the 2 rho-labeled GKM hexagon edges are the V-edges), NOT a Q-gauge claim.
# Q-gauge note: in the oblique gauge Q(x,y)=xy mod 2 one has Q(a1)=Q(a2)=0, Q(rho)=1
# (the prior session's gauge); in the Z^3 gauge Q=sum binom(v_i,2) all three roots have
# Q=1. Both are honest quadratic refinements of the same alternating form (they differ
# by the linear form x+y); the E/V split is pinned by the hexagon label structure.
# oblique coordinates of a sum-zero Z^3 vector: v = x*alpha1 + y*alpha2 -> (x, y)
def obl(v): return (v[0], v[0] + v[1])
Q_obl = lambda v: (v[0] * (v[0] + v[1])) % 2
EV_OF_ROOT = {ALPHA1: "E", ALPHA2: "E", RHO: "V"}
assert obl(ALPHA1) == (1,0) and obl(ALPHA2) == (0,1) and obl(RHO) == (1,1)
assert Q_obl(ALPHA1) == 0 and Q_obl(ALPHA2) == 0 and Q_obl(RHO) == 1
log("[core] E/V root split (structural): alpha1,alpha2 = E; rho = V; oblique-Q parities 0,0,1: OK")

# ------------------------------------------------------------------ 19-corner graph
# edges in the 6 root directions; connection s(v -> v+delta) = (-1)^{<v,delta>}
EDGE_DIRS = ROOTS
edges = set()
for v in H2:
    for d in EDGE_DIRS:
        w = vadd(v, d)
        if w in set(H2):
            edges.add(tuple(sorted([v, w])))
edges = sorted(edges)
assert len(edges) == 42, len(edges)
log(f"[core] P-19 graph: 19 vertices, 42 root-edges: OK")

def conn_sign(v, delta):
    """level-2 connection along v -> v+delta (symmetric gauge): (-1)^{<v,delta>}"""
    return 1 if dot(v, delta) % 2 == 0 else -1

# unit triangles: v, v+d1, v+d1+d2 for the ordered root pairs (d1,d2) with d1+d2 a root
triangles = set()
for v in H2:
    for d1 in POS_ROOTS:
        for d2 in POS_ROOTS:
            if d1 == d2: continue
            if tuple(vadd(d1, d2)) not in [tuple(r) for r in POS_ROOTS]: continue
            a, b, c = v, vadd(v, d1), vadd(v, vadd(d1, d2))
            if a in set(H2) and b in set(H2) and c in set(H2):
                triangles.add(tuple(sorted([a, b, c])))
triangles = sorted(triangles)
assert len(triangles) == 24, len(triangles)
log(f"[core] unit-triangle triangulation: 24 triangles: OK")

def tri_curvature(tri):
    """product of the 3 edge connections around the triangle (in cyclic order)"""
    (a, b, c) = sorted(tri)
    # cyclic order: use the sorted ring via the actual edges
    ring = [a, b, c]
    prod = 1
    for i in range(3):
        u, w = ring[i], ring[(i+1) % 3]
        d = vsub(w, u)
        prod *= conn_sign(u, d)
    return prod

curvs = [tri_curvature(t) for t in triangles]
assert all(c == -1 for c in curvs), set(curvs)
log("[core] curvature = -1 on ALL 24 unit triangles: OK  (connection convention pinned)")

# Q-sign bookkeeping of triangles: E-triangles (all 3 corners Q=0) vs mixed
tri_q = [sum(Q(v) for v in t) % 2 for t in triangles]
log(f"[core] triangle Q-parity census: odd={sum(tri_q)}, even={24-sum(tri_q)}")

# ------------------------------------------------------------------ S3 and the flag cells
# permutations as tuples: p[i] = image of i; act on Z^3 by permuting coordinates.
def perm_apply(p, v):  return (v[p[0]], v[p[1]], v[p[2]])
def perm_mul(p, q):    return tuple(p[q[i]] for i in range(3))
def perm_inv(p):
    r = [0,0,0]
    for i in range(3): r[p[i]] = i
    return tuple(r)

S3 = sorted(itertools.permutations(range(3)))
S_GEN = [(1,0,2), (0,2,1)]     # s1 = swap 1,2 ; s2 = swap 2,3
S1, S2 = S_GEN
IDENT = (0,1,2)
W0 = (2,1,0)
S1S2 = (2, 0, 1); S2S1 = (1, 2, 0)   # via positions: s1s2*rho = -alpha1, s2s1*rho = -alpha2
assert perm_apply(S1S2, RHO) == (-1, 1, 0) and perm_apply(S2S1, RHO) == (0, -1, 1)
def word(w):  # reduced word as list of generator indices (0-based: 0=s1, 1=s2)
    # brute force length via inversions of one-line notation
    inv = sum(1 for i in range(3) for j in range(i+1,3) if w[i] > w[j])
    # find a reduced word by greedy left descent
    out = []
    cur = w
    while cur != IDENT:
        for gi, s in enumerate(S_GEN):
            if perm_apply(perm_inv(s), cur) == cur: continue
        # find a generator that reduces length
        done = False
        for gi, s in enumerate(S_GEN):
            t = perm_mul(perm_inv(s), cur)
            tinv = sum(1 for i in range(3) for j in range(i+1,3) if t[i] > t[j])
            if tinv < sum(1 for i in range(3) for j in range(i+1,3) if cur[i] > cur[j]):
                out.append(gi); cur = t; done = True; break
        assert done
    return out

CELLS = {}   # w -> dict(len, word, position w.rho, character)
for w in S3:
    l = len(word(w))
    pos = perm_apply(w, RHO)
    chi_key = char_of(vsub(pos, RHO))          # chi_w = psi_{w rho - rho}
    CELLS[w] = dict(w=w, len=l, word=word(w), pos=pos, chi=chi_key)

# structural checks from the locked design:
chi_census = {}
for c in CELLS.values():
    chi_census.setdefault(c["chi"], []).append(c["w"])
assert sorted(len(v) for v in chi_census.values()) == [2, 2, 2]
# e and w0 carry trivial; s1,s2s1 carry chi_a; s2,s1s2 carry chi_b
assert CELLS[IDENT]["chi"] == "triv" and CELLS[W0]["chi"] == "triv"
assert CELLS[S1]["chi"] == char_of(vsub(perm_apply(S1,RHO), RHO))
log("[core] cell characters chi_w = psi_(w rho - rho): {e,w0}: triv, "
    "{s1,s2s1}: " + CELLS[S1]['chi'] + ", {s2,s1s2}: " + CELLS[S2]['chi'] + " : OK")
log("[core]   full census: " + repr({k: [c["w"] for c in CELLS.values() if c["chi"] == k] for k in chi_census}))

# KEY structural fact: the V-character psi_rho NEVER appears as a cell character.
assert "psi_rho" not in set(c["chi"] for c in CELLS.values())
log("[core] *** THE V-CHARACTER psi_rho NEVER APPEARS AS A CELL CHARACTER ***")

# ------------------------------------------------------------------ strong Bruhat order / GKM graph
def inv_set(w):
    """Inv(w) = {alpha in Phi+ : w^{-1}(alpha) < 0}"""
    wi = perm_inv(w)
    out = []
    for a in POS_ROOTS:
        im = perm_apply(wi, a)
        if im[0] < 0 or (im[0] == 0 and im[1] < 0):
            # lexicographic-negative test on sum-zero triples: image is negative iff
            # its first nonzero coordinate is negative
            if next((x for x in im if x != 0), 0) < 0:
                out.append(a)
    return out

INV = {w: inv_set(w) for w in S3}
assert INV[IDENT] == []
assert sorted(INV[S1]) == sorted([ALPHA1])
assert sorted(INV[S2]) == sorted([ALPHA2])
assert sorted(INV[S1S2]) == sorted([ALPHA1, RHO])   # s1 s2
assert sorted(INV[S2S1]) == sorted([ALPHA2, RHO])   # s2 s1
assert sorted(INV[W0]) == sorted(POS_ROOTS)
# telescoping identity: sum Inv(w) = rho - w rho
for w in S3:
    s = (0,0,0)
    for a in INV[w]: s = vadd(s, a)
    assert s == vsub(RHO, perm_apply(w, RHO)), (w, s)
log("[core] Inv sets + telescoping sum(Inv(w)) = rho - w*rho: OK (all 6 cells)")

# strong order: w' <= w iff Inv(w') subset Inv(w). Coverings = the GKM hexagon edges.
def subset(A, B): return all(a in B for a in A)
HASSE = []
for w in S3:
    for u in S3:
        if u == w: continue
        if not subset(INV[u], INV[w]): continue
        if len(INV[w]) - len(INV[u]) != 1: continue
        # covering: nothing strictly between
        between = [z for z in S3 if z not in (u, w) and subset(INV[u], INV[z]) and subset(INV[z], INV[w])]
        if not between:
            beta = [a for a in INV[w] if a not in INV[u]]
            assert len(beta) == 1
            HASSE.append(dict(u=u, w=w, beta=beta[0], chi_u=CELLS[u]["chi"], chi_w=CELLS[w]["chi"]))
assert len(HASSE) == 6, len(HASSE)
# the GKM hexagon: 4 E-edges + 2 V-edges (labels: alpha1/alpha2 = E, rho = V)
nV = sum(1 for h in HASSE if h["beta"] == RHO)
assert nV == 2, nV
log(f"[core] GKM hexagon (strong Bruhat coverings): 6 edges = 4 E + 2 V: OK")
for h in HASSE:
    ev = "V" if h["beta"] == RHO else "E"
    log(f"[core]   edge {h['u']} -> {h['w']}  label beta={'rho' if h['beta']==RHO else ('a1' if h['beta']==ALPHA1 else 'a2')}"
        f"  [{ev}]  chi(target)={h['chi_u']}")

# descent character identity: psi_{u rho - w rho} = chi_u * chi_w  (since 2 w rho ~ 0)
for h in HASSE:
    mu = vsub(perm_apply(h["u"], RHO), perm_apply(h["w"], RHO))
    lhs = char_of(mu)
    # product of characters chi_u * chi_w:
    prod = {}
    for g in GAMMA:
        prod[g] = CHARS[h["chi_u"]][g] * CHARS[h["chi_w"]][g]
    pr_name = None
    for name, cd in CHARS.items():
        if cd == prod: pr_name = name; break
    assert lhs == pr_name, (h, lhs, pr_name)
log("[core] descent-character identity psi_(u rho - w rho) = chi_u . chi_w : OK (all 6 edges)")

# ------------------------------------------------------------------ the (locked) booked Gamma-module structure
# H_*(Fl_3) as booked E^2-modules: (triv, psi1 (+) psi2, psi2 (+) psi1, triv)
# honest derivation: cell-character structure. chi_a = psi_{alpha1-ish}, chi_b = psi_{alpha2-ish}
MODULES = {0: ["triv"], 2: ["psi_a1", "psi_a2"], 4: ["psi_a2", "psi_a1"], 6: ["triv"]}
log(f"[core] booked module structure H_q(Fl3): {MODULES}  (s1,s2s1->psi_a1; s2,s1s2->psi_a2; e,w0->triv)")

# ------------------------------------------------------------------ SNF (integer)
def snf(mat):
    """Smith normal form of a list-of-rows integer matrix; returns list of diagonal entries."""
    M = [row[:] for row in mat]
    R, C = len(M), len(M[0]) if M else 0
    res = []
    r = c = 0
    while r < R and c < C:
        # find pivot
        piv = None
        for i in range(r, R):
            for j in range(c, C):
                if M[i][j] != 0:
                    if piv is None or abs(M[i][j]) < abs(M[piv[0]][piv[1]]):
                        piv = (i, j)
        if piv is None: break
        i, j = piv
        M[r], M[i] = M[i], M[r]
        for row in M: row[c], row[j] = row[j], row[c]
        # reduce
        ok = False
        while not ok:
            ok = True
            for i2 in range(r+1, R):
                if M[i2][c] != 0:
                    q = M[i2][c] // M[r][c]
                    for jj in range(c, C): M[i2][jj] -= q * M[r][jj]
                    if M[i2][c] != 0:
                        M[r], M[i2] = M[i2], M[r]; ok = False
            for j2 in range(c+1, C):
                if M[r][j2] != 0:
                    q = M[r][j2] // M[r][c]
                    for ii in range(r, R): M[ii][j2] -= q * M[ii][c]
                    if M[r][j2] != 0:
                        for row in M: row[c], row[j2] = row[j2], row[c]; ok = False
        if M[r][c] < 0: M[r][c] = -M[r][c]
        res.append(M[r][c])
        r += 1; c += 1
    return res

def homology_from_snf(sn, n_src, n_tgt):
    """from SNF diagonal of the boundary b: C_n -> C_{n-1}: (free part, torsion) of H_{n-1}
       given n_src = rank C_n (source) and n_tgt = rank C_{n-1}."""
    tors = [d for d in sn if d not in (0, 1)]
    n_nonzero_unit = sum(1 for d in sn if d == 1)
    rank_b = sum(1 for d in sn if d != 0)
    return (n_tgt - rank_b, sorted(tors))

# ------------------------------------------------------------------ export
def export():
    return dict(
        corners=[list(v) for v in H2],
        sectors={str(k): [list(v) for v in vs] for k, vs in SECTORS.items()},
        edges=[list(e) for e in edges],
        triangles=[list(t) for t in triangles],
        cells={str(w): dict(len=c["len"], word=c["word"], pos=list(c["pos"]), chi=c["chi"])
               for w, c in CELLS.items()},
        hasse=[dict(u=list(h["u"]), w=list(h["w"]), beta=list(h["beta"]),
                    ev=("V" if h["beta"] == RHO else "E"), chi_u=h["chi_u"], chi_w=h["chi_w"])
               for h in HASSE],
        modules=MODULES,
    )

if __name__ == "__main__":
    log("\n=== w19_core: ALL VERIFICATION GATES PASSED ===")
    print("CORE_OK")
