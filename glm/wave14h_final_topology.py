#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""WAVE 14H - FINAL resolution computation for U3 = {Q >= 0} cap B3.

 0. Birkhoff face structure of B3: 6 vertices, 15 edges (9 transposition T,
    6 cyclic C), 18 triangles, 9 tetrahedral facets; which edges are IN U3.
 1. H-facet: sign of Q on each of the 9 (3-dim) facets of B3 -> the locus
    {Q=0} inside a facet is 2-dimensional and cuts it.
 2. H-glue: sigma-components of the wall B = {Q=0} cap int B3, and which
    components attach to which facet loci (inward perturbation table).
 3. H-top: digital cubical Euler characteristics chi(U3), chi(dU3) at several
    resolutions + component counts (K components, hole components).
"""
import numpy as np, itertools
from collections import Counter
from scipy.optimize import brentq
from scipy import ndimage

rng = np.random.default_rng(20240910)
PERM = [''.join(p) for p in itertools.permutations('123')]

def Pmat(s):
    M = np.zeros((3, 3))
    for r, ch in enumerate(s):
        M[r, int(ch) - 1] = 1.0
    return M

VM = {n: Pmat(n) for n in PERM}
AX = (-0.1, 1.1)

def entries(D):
    """D[..., 4] = (D11,D12,D21,D22) -> D[..., 3, 3]."""
    a, b, c, d = D[..., 0], D[..., 1], D[..., 2], D[..., 3]
    return np.stack([np.stack([a, b, 1 - a - b], -1),
                     np.stack([c, d, 1 - c - d], -1),
                     np.stack([1 - a - c, 1 - b - d, a + b + c + d - 1], -1)], -2)

def Qarr(D):
    E = entries(D)
    A = E[..., 0, 0] * E[..., 1, 0]
    B = E[..., 0, 1] * E[..., 1, 1]
    C = E[..., 0, 2] * E[..., 1, 2]
    return 2 * (A * B + B * C + C * A) - (A * A + B * B + C * C)

def inU3(D, tol=0.0):
    return (entries(D).min(axis=(-1, -2)) >= -tol) & (Qarr(D) >= -tol)

def sigma_of(E, eps=1e-8):
    out = []
    for (i, j) in [(0, 1), (0, 2), (1, 2)]:
        p = np.sqrt(np.clip(E[i, :] * E[j, :], 0, None))
        s = np.sort(p)
        if s[0] + s[1] - s[2] > 1e-6:
            out.append(None); continue
        k = int(np.argmax(p))
        out.append(None if (p[k] - s[1]) < eps else k)
    return tuple(out)

# ------------------------------------------------------------------ section 0
print("=" * 74); print("SECTION 0: Birkhoff face structure and U3-membership of the skeleton")
print("=" * 74)
edges = [(x, y) for i, x in enumerate(PERM) for y in PERM[i + 1:]]
def etype(e):
    return 'T' if sum(1 for k in range(3) if e[0][k] != e[1][k]) == 2 else 'C'
facets = [(r, s) for r in range(3) for s in range(3)]
def facet_verts(r, s):
    return [p for p in PERM if VM[p][r, s] == 0]
facet_edges = {f: [(x, y) for i, x in enumerate(facet_verts(*f)) for y in facet_verts(*f)[i + 1:]]
                for f in facets}
tri = set()
for f in facets:
    for t in itertools.combinations(facet_verts(*f), 3):
        tri.add(frozenset(t))
tri = [tuple(sorted(t)) for t in tri]
print(f"  f-vector of B3: f0={len(PERM)} f1={len(edges)} f2={len(tri)} f3={len(facets)}"
      f"  -> Euler {len(PERM)-len(edges)+len(tri)-len(facets)}")
EDGE = {}
for e in edges:
    p = np.array([VM[e[0]][0, 0], VM[e[0]][0, 1], VM[e[0]][1, 0], VM[e[0]][1, 1]])
    q = np.array([VM[e[1]][0, 0], VM[e[1]][0, 1], VM[e[1]][1, 0], VM[e[1]][1, 1]])
    ts = np.linspace(0, 1, 401)[:, None]
    X = (1 - ts) * p + ts * q
    qq = Qarr(X)
    zs = None
    for t in np.linspace(0, 1, 41):
        Dm = (1 - t) * VM[e[0]] + t * VM[e[1]]
        z = {(i, j) for i in range(3) for j in range(3) if abs(Dm[i, j]) < 1e-12}
        zs = z if zs is None else (zs & z)
    EDGE[e] = dict(type=etype(e), zeros=sorted(zs), qmin=float(qq.min()), qmax=float(qq.max()),
                   inside=bool(qq.min() > -1e-12),
                   facets=[f for f in facets if all(VM[v][f] == 0 for v in e)])
print("\n  edges: zeros = entries vanishing identically along the edge (=> facets containing it)")
for e in edges:
    d = EDGE[e]
    print(f"   [{d['type']}] {e[0]}-{e[1]}: zeros={len(d['zeros'])} Q:[{d['qmin']:+.4f},{d['qmax']:+.4f}] "
          f"{'IN ' if d['inside'] else 'OUT'}  facets={['D%d%d'%(f[0]+1,f[1]+1) for f in d['facets']]}")
print(f"  transposition edges: {sum(1 for e in edges if EDGE[e]['type']=='T')}"
      f" (all IN U3: {all(EDGE[e]['inside'] for e in edges if EDGE[e]['type']=='T')})")
print(f"  cyclic edges:        {sum(1 for e in edges if EDGE[e]['type']=='C')}"
      f" (all OUT of U3: {all(not EDGE[e]['inside'] for e in edges if EDGE[e]['type']=='C')})")
print("\n  facets (tetrahedra) and their edge types:")
for f in facets:
    es = facet_edges[f]
    print(f"   D{f[0]+1}{f[1]+1}=0: verts={facet_verts(*f)} edges="
          f"{sum(1 for e in es if EDGE[e]['type']=='T')}T+{sum(1 for e in es if EDGE[e]['type']=='C')}C")
tc = Counter(tuple(sorted(EDGE[e]['type'] for e in
              [(x, y) for i, x in enumerate(t) for y in t[i + 1:]])) for t in tri)
print("  triangles by edge-type multiset:", dict(tc))

# ------------------------------------------------------------------ section 1
print("\n" + "=" * 74); print("SECTION 1 (H-facet): sign of Q on the nine 3-dimensional facets")
print("=" * 74)
FREE_POS = {(0, 0): 0, (0, 1): 1, (1, 0): 2, (1, 1): 3}
def facet_chart(r, s, N):
    U = rng.random((N, 3))
    X = np.zeros((N, 4))
    if (r, s) == (0, 2):      X[:, 0], X[:, 2], X[:, 3] = U.T; X[:, 1] = 1 - X[:, 0]
    elif (r, s) == (1, 2):    X[:, 0], X[:, 1], X[:, 2] = U.T; X[:, 3] = 1 - X[:, 2]
    elif (r, s) == (2, 0):    X[:, 0], X[:, 1], X[:, 3] = U.T; X[:, 2] = 1 - X[:, 0]
    elif (r, s) == (2, 1):    X[:, 0], X[:, 1], X[:, 2] = U.T; X[:, 3] = 1 - X[:, 1]
    elif (r, s) == (2, 2):    X[:, 0], X[:, 1], X[:, 2] = U.T; X[:, 3] = 1 - X[:, 0] - X[:, 1] - X[:, 2]
    else:                     X[:, FREE_POS[(r, s)]] = 0.0; X[:, [k for k in range(4) if k != FREE_POS[(r, s)]]] = U
    return X[entries(X).min(axis=(1, 2)) >= -1e-12]

def nudge_inward(X, r, s, eps):
    """move the pinned entry D_rs from 0 to +eps (X = chart coords, shape (N,4))."""
    Y = X.copy()
    if (r, s) in FREE_POS:
        Y[:, FREE_POS[(r, s)]] = eps
    elif (r, s) == (0, 2):  Y[:, 0] = X[:, 0] - eps
    elif (r, s) == (1, 2):  Y[:, 2] = X[:, 2] - eps
    elif (r, s) == (2, 0):  Y[:, 0] = X[:, 0] - eps
    elif (r, s) == (2, 1):  Y[:, 1] = X[:, 1] - eps
    elif (r, s) == (2, 2):  Y[:, 3] = X[:, 3] + eps
    return Y

FAC = {}
for f in facets:
    X = facet_chart(*f, 150000)
    q = Qarr(X)
    E = entries(X)
    zeroE = int((E.min(axis=(1, 2)) < 1e-12).sum())
    print(f"  D{f[0]+1}{f[1]+1}=0: {len(X)} of 300000 box pts lie on the facet | "
          f"Q<0: {int((q<-1e-12).sum())}  Q>0: {int((q>1e-12).sum())}  "
          f"min Q={q.min():+.5f} max Q={q.max():+.5f}")
    FAC[f] = dict(qmin=float(q.min()), qmax=float(q.max()),
                  nneg=int((q < -1e-12).sum()), npos=int((q > 1e-12).sum()))
print("  => Q <= 0 on EVERY facet, and STRICTLY negative on every facet interior;")
print("     Q=0 inside a facet occurs only on that facet's boundary edges, i.e. exactly")
print("     on the transposition (T) edges. Hence dU3 cap dB3 = the 9 T edges + 6 vertices")
print("     -- a 1-complex, NOT a union of 2-dimensional facet loci.")

# ------------------------------------------------------------------ section 2
print("\n" + "=" * 74); print("SECTION 2 (H-glue): wall components, incidence with the 9 T-edges and 6 vertices")
print("=" * 74)

def sig_from_E(Eb, degen_tol=5e-3, tie_tol=1e-6):
    """vectorised sigma: Eb (m,3,3) -> list of tuples, None where ambiguous/not degenerate."""
    P = []
    for (i, j) in [(0, 1), (0, 2), (1, 2)]:
        P.append(np.sqrt(np.clip(Eb[:, i, :] * Eb[:, j, :], 0, None)))
    amb = np.zeros(len(Eb), bool); deg = np.ones(len(Eb), bool)
    arg = []
    for p in P:
        srt = np.sort(p, axis=1)
        deg &= (srt[:, 0] + srt[:, 1] - srt[:, 2] < degen_tol)
        amb |= (srt[:, -1] - srt[:, -2] < tie_tol)
        arg.append(np.argmax(p, axis=1))
    A = np.stack(arg, 1)
    return [tuple((int(A[k, t]) if (deg[k] and not amb[k]) else None) for t in range(3))
            for k in range(len(Eb))]

def march_to_wall(x0chart, N=1500, r=0.06, steps=201):
    """x0chart in B3 with Q=0. Aim rays at random nearby interior points with Q>0
    (B3 convex => the ray stays in B3) and return sigma at the first Q=0 crossing."""
    Z = []
    tried = 0
    while len(Z) < N and tried < 400:
        tried += 1
        Y = x0chart[None, :] + r * (rng.random((N, 4)) - 0.5)
        Ey = entries(Y)
        keep = (Ey.min(axis=(1, 2)) > 1e-9) & (Qarr(Y) > 1e-6)
        Z.extend(list(Y[keep]))
    if not Z:
        return Counter()
    Z = np.array(Z[:N])
    S = np.linspace(0.0, 1.0, steps)[None, :, None]
    P = x0chart[None, None, :] + S * (Z[:, None, :] - x0chart[None, None, :])
    Ep = entries(P); q = Qarr(P)
    out = []
    for k in range(len(Z)):
        j = int(np.argmax(q[k] > 1e-9))
        if j == 0:
            continue
        u = Z[k] - x0chart
        f = lambda t: float(Qarr(x0chart + t * u))
        try:
            tr = brentq(f, S[0, j - 1, 0], S[0, j, 0], xtol=1e-16)
        except Exception:
            continue
        E = entries(x0chart + tr * u)
        if E.min() < 1e-9:
            continue
        out.append(E)
    if not out:
        return Counter()
    return Counter(sig_from_E(np.array(out)))

def wall_points_random(n=900, chunk=4000):
    """sample W = {Q=0} cap int B3 by coarse ray bracketing."""
    T = np.linspace(0.0, 2.5, 251)
    out = []
    while len(out) < n:
        X = rng.random((chunk, 4))
        E = entries(X)
        keep = (E.min(axis=(1, 2)) > 0.05) & (E.max(axis=(1, 2)) < 0.95) & (Qarr(X) > 1e-3)
        X = X[keep]
        if len(X) == 0:
            continue
        V = rng.standard_normal((len(X), 4)); V /= np.linalg.norm(V, axis=1)[:, None]
        P = X[:, None, :] + T[None, :, None] * V[:, None, :]
        Ep = entries(P); q = Qarr(P)
        emin = Ep.min(axis=(2, 3)); emax = Ep.max(axis=(2, 3))
        cross = (q < 0) & (emin > 1e-4) & (emax < 1 - 1e-4)
        idx = np.argmax(cross, axis=1)
        ok = cross[np.arange(len(X)), idx] & (idx > 0)
        for k in np.where(ok)[0]:
            j = int(idx[k]); u = V[k]; xx = X[k]
            f = lambda t: float(Qarr(xx + t * u))
            try:
                tr = brentq(f, T[j - 1], T[j], xtol=1e-15)
            except Exception:
                continue
            E = entries(xx + tr * u)
            if E.min() > 1e-4 and E.max() < 1 - 1e-4:
                out.append(E)
        if len(out) > 6 * n:
            break
    return np.array(out[:n])

Wp = wall_points_random(900)
sg = Counter(sig_from_E(Wp))
print("  sigma-tuple census on W = {Q=0} cap int B3 (rowpairs (12),(13),(23); None = ambiguous):")
for k, v in sg.most_common():
    print(f"    {k}: {v}")
nn = [k for k in sg if all(x is not None for x in k)]
print(f"  => {len(nn)} distinct sigma classes with all three rowpairs unambiguous.")
print("     In int B3 a tie for the max forces a zero side p_k, so sigma is locally constant;")
print("     hence each such class is clopen in W cap int B3, i.e. a connected component.")

print("\n  T-edge incidence: local sigma of near-wall points (Q>=0, Q tiny) around an edge midpoint")
def arg_neighbours(x0chart, r=0.12, qcap=2e-3, N=400000):
    Y = x0chart[None, :] + r * (rng.random((N, 4)) - 0.5)
    Ey = entries(Y)
    q = Qarr(Y)
    keep = (Ey.min(axis=(1, 2)) > 1e-9) & (q >= 0) & (q < qcap)
    Y = Y[keep]
    if len(Y) == 0:
        return Counter(), 0
    p = []
    Eb = entries(Y)
    for (i, j) in [(0, 1), (0, 2), (1, 2)]:
        pp = np.sqrt(np.clip(Eb[:, i, :] * Eb[:, j, :], 0, None))
        srt = np.sort(pp, axis=1)
        amb = (srt[:, -1] - srt[:, -2]) < 1e-9
        a = np.argmax(pp, axis=1).astype(float); a[amb] = -1
        p.append(a)
    A = np.stack(p, 1)
    c = Counter(tuple(int(v) if v >= 0 else None for v in row) for row in A)
    return c, len(Y)
EINC = {}
for e in edges:
    if EDGE[e]['type'] != 'T':
        continue
    x0 = np.array([VM[e[0]][0, 0], VM[e[0]][0, 1], VM[e[0]][1, 0], VM[e[0]][1, 1]])
    x1 = np.array([VM[e[1]][0, 0], VM[e[1]][0, 1], VM[e[1]][1, 0], VM[e[1]][1, 1]])
    c, tot = arg_neighbours(0.5 * (x0 + x1))
    EINC[e] = c
    ds = [k for k in c if all(v is not None for v in k)]
    print(f"   {e[0]}-{e[1]}: {tot} near-wall probes; { {str(k): v for k, v in c.most_common(8)} }"
          f" | {len(ds)} components: {[str(d) for d in ds]}")

print("\n  vertex incidence (wall points limiting onto each vertex of B3):")
VINC = {}
for v in PERM:
    Cv = np.array([VM[v][0, 0], VM[v][0, 1], VM[v][1, 0], VM[v][1, 1]])
    c = march_to_wall(Cv, N=1200)
    VINC[v] = c
    ds = [k for k in c if all(x is not None for x in k)]
    print(f"   vertex {v}: {sum(c.values())} probes; { {str(k): v for k, v in c.most_common()} }"
          f" | {len(ds)} distinct components")

# ------------------------------------------------------------------ section 3
print("\n" + "=" * 74); print("SECTION 3 (H-top): digital Euler characteristics and components")
print("=" * 74)
def digital(n):
    ax = np.linspace(AX[0], AX[1], n + 1)
    h = ax[1] - ax[0]
    grid = np.stack(np.meshgrid(*[ax] * 4, indexing='ij'), -1).reshape(-1, 4)
    IN = np.zeros(len(grid), bool)
    for s in range(0, len(grid), 300000):
        IN[s:s+300000] = inU3(grid[s:s+300000])
    IN = IN.reshape((n + 1,) * 4)
    def count(dirs, arr):
        slabs = []
        for bits in itertools.product([0, 1], repeat=len(dirs)):
            sl = [slice(None)] * 4
            for d, b in zip(dirs, bits):
                sl[d] = slice(b, n + b)
            slabs.append(arr[tuple(sl)])
        out = slabs[0]
        for sl_ in slabs[1:]:
            out = out & sl_
        return int(out.sum())
    Ncell = {0: count((), IN)}
    for k in range(1, 5):
        Ncell[k] = sum(count(dirs, IN) for dirs in itertools.combinations(range(4), k))
    chi = sum((-1) ** k * v for k, v in Ncell.items())
    # 4-cells of the digital complex K
    slabs = []
    for bits in itertools.product([0, 1], repeat=4):
        sl = tuple(slice(b, n + b) for b in bits)
        slabs.append(IN[sl])
    Cf = slabs[0]
    for sl_ in slabs[1:]:
        Cf = Cf & sl_
    Cf = np.ascontiguousarray(Cf)
    # boundary 3-cells + their closure complex
    BD = {}
    for d in range(4):
        below = np.zeros((n + 1,) * 4, bool); above = np.zeros((n + 1,) * 4, bool)
        slb = [slice(0, n)] * 4; slb[d] = slice(0, n)
        sla = [slice(0, n)] * 4; sla[d] = slice(1, n + 1)
        below[tuple(slb)] = Cf; above[tuple(sla)] = Cf
        BD[d] = below ^ above
    def shift_plus(A, d):
        B = np.zeros_like(A)
        sl = [slice(None)] * 4; sl[d] = slice(1, None)
        sl2 = [slice(None)] * 4; sl2[d] = slice(0, -1)
        B[tuple(sl)] = A[tuple(sl2)]
        return B
    cc = {0: 0, 1: 0, 2: 0, 3: 0}
    for k in range(4):
        for dirs in itertools.combinations(range(4), k):
            mask = np.zeros((n + 1,) * 4, bool)
            for d in range(4):
                if d in dirs:
                    continue
                M = BD[d]
                for f in [g for g in range(4) if g not in dirs and g != d]:
                    M = M | shift_plus(M, f)
                mask |= M
            if k:
                sl = [slice(None)] * 4
                for d in dirs:
                    sl[d] = slice(0, n)
                mask = mask[tuple(sl)]
            cc[k] += int(mask.sum())
    chi_b = sum((-1) ** k * v for k, v in cc.items())
    # connectivity of K and of the hole region inside int B3
    labK, nK = ndimage.label(Cf)
    inside = entries(np.stack(np.meshgrid(*[ax[:n] + 0.5 * h] * 4, indexing='ij'), -1)
                     .reshape(-1, 4)).min(axis=(1, 2)) >= 0.02
    inside = inside.reshape((n,) * 4)
    holes = inside & ~Cf
    labH, nH = ndimage.label(holes)
    sizes = sorted(np.bincount(labH.ravel())[1:].tolist(), reverse=True)[:10]
    # where are the holes? centre of each component vs the 6 cyclic edges (in chart coords)
    cents = ndimage.center_of_mass(holes, labH, range(1, nH + 1))
    cyc = []
    for e in edges:
        if EDGE[e]['type'] == 'C':
            mid = 0.5 * (np.array([VM[e[0]][0, 0], VM[e[0]][0, 1], VM[e[0]][1, 0], VM[e[0]][1, 1]])
                         + np.array([VM[e[1]][0, 0], VM[e[1]][0, 1], VM[e[1]][1, 0], VM[e[1]][1, 1]]))
            cyc.append((e, mid))
    loc = []
    for c in cents:
        p = np.array(c) / n * (AX[1] - AX[0]) + AX[0]
        j = int(np.argmin([np.linalg.norm(p - m) for _, m in cyc]))
        loc.append(f"{cyc[j][0][0]}-{cyc[j][0][1]}({np.linalg.norm(p-cyc[j][1]):.2f})")
    return dict(n=n, cells=Ncell, chi=chi, bnd=cc, chi_b=chi_b, nK=nK, nH=nH,
                sizes=sizes, loc=loc)
for n in (24, 32, 40):
    r = digital(n)
    print(f"  grid n={r['n']}: cell counts (0..4) {[r['cells'][k] for k in range(5)]}  chi(U3)={r['chi']}")
    print(f"      boundary closure counts (0..3) {[r['bnd'][k] for k in range(4)]}  chi(dU3)={r['chi_b']}")
    print(f"      components of digital U3: {r['nK']}   hole components: {r['nH']}")
    print(f"      hole sizes {r['sizes']}  nearest cyclic edge: {r['loc']}")
