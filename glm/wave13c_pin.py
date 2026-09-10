#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
WAVE 13C-2a : THE FIBRE-LAYER PINNING (stage 2, part 1) -- v2
Stratum-aware: c-images of F/E-stratum points are re-expressed via closed-form
D-inversions on the target cell's parametrization (ckm_normal only works on
the generic R/sheet strata).

Pins (integer outputs rounded from well-separated data, sixths):
  (P1) kappa on the 9 F-cells   (P2) kappa on the 9 E-cells (S^1)
  (P3) kappa on the 6 R-cells   (P4) w(R->F), the 18 interface translations
  (P5) tau(s->R), 12 values (natural gauge, near-limit conversions)
  (P6) the gamma-paths (sheet->pureF conversions as paths in delta)
  (P7) the F->E interface S^1-shifts
  (P8) base orientation signs s_b (32 cells)
  (P9) consistency relations (c-equivariance, orbit sums, base dT=Td w/ signs)

Run:  python3 wave13c_pin.py
"""
import itertools
import json
import sys
import time

import numpy as np

T0 = time.time()
SEP = "=" * 78
rng = np.random.default_rng(20260911)
PI2 = np.pi / 2.0


def hdr(s):
    print("\n" + SEP)
    print(s)
    print(SEP)


def tick(msg):
    print("[t+%6.1fs] %s" % (time.time() - T0, msg))
    sys.stdout.flush()


# ----------------------------------------------------------------------------
# CKM machinery (stage-1 conventions)
# ----------------------------------------------------------------------------
PSIG = np.zeros((3, 3)); PSIG[0, 1] = 1; PSIG[1, 2] = 1; PSIG[2, 0] = 1
SIG = (1, 2, 0)


def Vckm(t1, t2, t3, delta):
    c1, s1 = np.cos(t1), np.sin(t1)
    c2, s2 = np.cos(t2), np.sin(t2)
    c3, s3 = np.cos(t3), np.sin(t3)
    e = np.exp(1j * delta)
    return np.array([
        [c1 * c3,               s1 * c3,               s3 * np.conj(e)],
        [-s1 * c2 - c1 * s2 * s3 * e,  c1 * c2 - s1 * s2 * s3 * e,  s2 * c3],
        [s1 * s2 - c1 * c2 * s3 * e,  -c1 * s2 - s1 * c2 * s3 * e,  c2 * c3],
    ], dtype=complex)


def Dof(th, d):
    return np.abs(Vckm(th[0], th[1], th[2], d)) ** 2


def ckm_normal(U):
    D = np.abs(U) ** 2
    s3sq = D[0, 2]
    c3sq = 1.0 - s3sq
    if c3sq <= 1e-12 or s3sq <= 1e-12 or D[0, 0] <= 1e-12 or D[2, 2] <= 1e-12:
        return None
    t = (np.arccos(np.sqrt(np.clip(D[0, 0] / c3sq, 0, 1))),
         np.arccos(np.sqrt(np.clip(D[2, 2] / c3sq, 0, 1))),
         np.arccos(np.sqrt(c3sq)))
    s1, c1 = np.sin(t[0]), np.cos(t[0])
    s2, c2 = np.sin(t[1]), np.cos(t[1])
    s3 = np.sin(t[2])
    denom = 2 * s1 * c2 * c1 * s2 * s3
    if denom <= 1e-13:
        return None
    cosd = (D[1, 0] - s1 ** 2 * c2 ** 2 - c1 ** 2 * s2 ** 2 * s3 ** 2) / denom
    cosd = float(np.clip(cosd, -1, 1))
    JU = np.imag(U[0, 0] * U[1, 1] * np.conj(U[0, 1]) * np.conj(U[1, 0]))
    if abs(cosd - 1.0) < 1e-9:
        cand = (0.0,)
    elif abs(cosd + 1.0) < 1e-9:
        cand = (np.pi,)
    else:
        cand = (np.arccos(cosd), -np.arccos(cosd))
    for dd in cand:
        V = Vckm(*t, dd)
        if np.max(np.abs(np.abs(V) ** 2 - D)) < 1e-9:
            JV = np.imag(V[0, 0] * V[1, 1] * np.conj(V[0, 1]) * np.conj(V[1, 0]))
            if abs(JV - JU) < 1e-8:
                return (t[0], t[1], t[2], dd)
    return None


# ----------------------------------------------------------------------------
# phase_solve: the universal conversion solver
# ----------------------------------------------------------------------------
def phase_solve(U, V, tol=0.03, ctol=1e-6):
    """Diagonal phases L, R with U ~ L V R.  BFS on the support graph,
    per-component gauge L := 0 (handles disconnected 5-supports of edges;
    the q_a projections live inside the big component, hence well-defined).
    Returns (L[3 angles], residual) or None on cycle inconsistency."""
    cons = []
    for i in range(3):
        for j in range(3):
            if abs(U[i, j]) > tol and abs(V[i, j]) > tol:
                cons.append((i, j, float(np.angle(U[i, j] / V[i, j]))))
    if not cons:
        return None
    L = [None] * 3
    R = [None] * 3
    adj = {}
    for (i, j, a) in cons:
        adj.setdefault(("r", i), []).append((("c", j), a, i, j))
        adj.setdefault(("c", j), []).append((("r", i), a, i, j))
    seen = set()
    resid = 0.0
    for start in [("r", 0), ("r", 1), ("r", 2)]:
        if start in seen or adj.get(start) is None:
            continue
        L[start[1]] = 0.0
        seen.add(start)
        frontier = [start]
        while frontier:
            nxt = []
            for node in frontier:
                for (other, a, i, j) in adj.get(node, []):
                    if other in seen:
                        val = (L[i] + R[j] - a + np.pi) % (2 * np.pi) - np.pi
                        if abs(val) > ctol:
                            return None
                        resid = max(resid, abs(val))
                    else:
                        if node[0] == "r":
                            R[j] = (a - L[i]) % (2 * np.pi)
                        else:
                            L[i] = (a - R[j]) % (2 * np.pi)
                        seen.add(other)
                        nxt.append(other)
            frontier = nxt
    if any(x is None for x in L):
        return None
    for (i, j, a) in cons:
        v = (L[i] + R[j] - a + np.pi) % (2 * np.pi) - np.pi
        resid = max(resid, abs(v))
    return (np.array(L), resid)


def phase_solve_soft(U, V, tol=0.03):
    """Same BFS but NEVER fails on inconsistency: returns L and the residual
    (for near-limit conversions where O(eps) mismatch is expected)."""
    cons = []
    for i in range(3):
        for j in range(3):
            if abs(U[i, j]) > tol and abs(V[i, j]) > tol:
                cons.append((i, j, float(np.angle(U[i, j] / V[i, j]))))
    if not cons:
        return None
    L = [None] * 3
    R = [None] * 3
    L[0] = 0.0
    adj = {}
    for (i, j, a) in cons:
        adj.setdefault(("r", i), []).append((("c", j), a, i, j))
        adj.setdefault(("c", j), []).append((("r", i), a, i, j))
    seen = {("r", 0)}
    frontier = [("r", 0)]
    while frontier:
        nxt = []
        for node in frontier:
            for (other, a, i, j) in adj.get(node, []):
                if other not in seen:
                    if node[0] == "r":
                        R[j] = (a - L[i]) % (2 * np.pi)
                    else:
                        L[i] = (a - R[j]) % (2 * np.pi)
                    seen.add(other)
                    nxt.append(other)
        frontier = nxt
    if any(x is None for x in L):
        return None
    resid = 0.0
    for (i, j, a) in cons:
        if R[j] is not None:
            v = (L[i] + R[j] - a + np.pi) % (2 * np.pi) - np.pi
            resid = max(resid, abs(v))
    return (np.array(L), resid)


def uv_shift(L):
    u = (L[1] - L[0]) / (2 * np.pi)
    v = (L[2] - L[1]) / (2 * np.pi)
    return (u % 1.0, v % 1.0)


def round_report(vals, name):
    if not vals:
        print("  %-24s -> NO SAMPLES" % name)
        return ((0, 0), False, 9.9)
    m = np.array(vals) * 6.0 % 6.0
    m = np.where(m > 5.75, m - 6.0, m)
    med = np.median(m, axis=0)
    r = tuple(np.round(med).astype(int) % 6)
    spread = float(np.max(np.abs(m - med)))
    ok = spread < 0.2 and len(vals) >= 5
    print("  %-24s -> (%d,%d) sixths [n=%d spread %.3f] %s" %
          (name, r[0], r[1], len(vals), spread, "OK" if ok else "DRIFT/FAIL"))
    return (r, ok, spread)


# ----------------------------------------------------------------------------
# base cell structures (stage-1)
# ----------------------------------------------------------------------------
PERMS = sorted(itertools.permutations(range(3)))
PID = {p: i for i, p in enumerate(PERMS)}
Q01, Q02, Q12 = (1, 0, 2), (2, 1, 0), (0, 2, 1)


def comp(p, q):
    return tuple(p[q[i]] for i in range(3))


EDGE_KEYS = []
for pi in (Q01, Q02, Q12):
    pairs = []
    for rho in PERMS:
        r2 = comp(rho, pi)
        pair = tuple(sorted([rho, r2]))
        if pair not in pairs:
            pairs.append(pair)
    for (a, b) in pairs:
        EDGE_KEYS.append((a, pi) if comp(a, pi) == b else (b, pi))
EID = {k: i for i, k in enumerate(EDGE_KEYS)}
EDGE_SUPPORT = {}
for (rho, pi) in EDGE_KEYS:
    r2 = comp(rho, pi)
    supp = frozenset([(i, rho[i]) for i in range(3)] + [(i, r2[i]) for i in range(3)])
    EDGE_SUPPORT[supp] = EID[(rho, pi)]

FNAMES = ["F1{th1=0}", "F2{th1=pi/2}", "F3{th2=0}", "F4{th2=pi/2}", "F5{th3=0}",
          "F6{d0,D22}", "F7{d0,D31}", "F8{dpi,D21}", "F9{dpi,D32}"]
FZERO = [(0, 1), (0, 0), (1, 2), (2, 2), (0, 2), (1, 1), (2, 0), (1, 0), (2, 1)]
RKEYS = [("R0.def", 0.0), ("R0.bF6", 0.0), ("R0.bF7", 0.0),
         ("R1.def", np.pi), ("R1.bF8", np.pi), ("R1.bF9", np.pi)]
RNAME = [r[0] for r in RKEYS]
FIXROW = {}
for (rho, pi) in EDGE_KEYS:
    FIXROW[(rho, pi)] = [i for i in range(3) if pi[i] == i][0]

CUBE_EDGES = []
for i1 in range(3):
    for v1 in (0.0, PI2):
        for i2 in range(i1 + 1, 3):
            for v2 in (0.0, PI2):
                CUBE_EDGES.append((i1, v1, i2, v2, 3 - i1 - i2))
CUBE_EDGE_OF_E = {}   # edge-cell -> its cube-edge (support-matched)
for (rho, pi) in EDGE_KEYS:
    r2 = comp(rho, pi)
    exp = frozenset([(i, rho[i]) for i in range(3)] + [(i, r2[i]) for i in range(3)])
    for ce in CUBE_EDGES:
        i1, v1, i2, v2, iv = ce
        th = [0.0, 0.0, 0.0]
        th[i1], th[i2], th[iv] = v1, v2, 0.5
        D = Dof(th, 0.0)
        supp = frozenset((i, k) for i in range(3) for k in range(3) if D[i, k] > 1e-9)
        if supp == exp:
            CUBE_EDGE_OF_E[EID[(rho, pi)]] = ce
            break
assert len(CUBE_EDGE_OF_E) == 9


def q_proj(a, u, v):
    if a == 0:
        return (-v) % 1.0
    if a == 1:
        return (-(u + v)) % 1.0
    return (-u) % 1.0


def th2_f6(u, v):
    return np.arctan(np.cos(u) / (np.sin(u) * np.sin(v) + 1e-300))


FPMAP = [
    lambda u, v: (0.0, u, v, 0.0),
    lambda u, v: (PI2, u, v, 0.0),
    lambda u, v: (u, 0.0, v, 0.0),
    lambda u, v: (u, PI2, v, 0.0),
    lambda u, v: (u, v, 0.0, 0.0),
    lambda u, v: (u, th2_f6(u, v), v, 0.0),
    lambda u, v: (u, np.arctan(np.cos(u) * np.sin(v) / (np.sin(u) + 1e-300)), v, 0.0),
    lambda u, v: (u, np.arctan(np.sin(u) / (np.cos(u) * np.sin(v) + 1e-300)), v, np.pi),
    lambda u, v: (u, np.arctan(np.sin(u) * np.sin(v) / (np.cos(u) + 1e-300)), v, np.pi),
]


def Vrep_F(fi, u, v):
    p = FPMAP[fi](u, v)
    return Vckm(p[0], p[1], p[2], p[3])


def inv_F(fi, D):
    """Closed-form D-inversion on F-cell fi -> (u, v)."""
    if fi == 0:
        return (float(np.arcsin(np.sqrt(D[2, 1]))), float(np.arccos(np.sqrt(D[0, 0]))))
    if fi == 1:
        return (float(np.arcsin(np.sqrt(D[2, 0]))), float(np.arccos(np.sqrt(D[0, 1]))))
    if fi == 2:
        return (float(np.arcsin(np.sqrt(D[1, 0]))), float(np.arccos(np.sqrt(D[2, 2]))))
    if fi == 3:
        return (float(np.arcsin(np.sqrt(D[2, 0]))), float(np.arccos(np.sqrt(D[1, 2]))))
    if fi == 4:
        return (float(np.arccos(np.sqrt(D[0, 0]))), float(np.arcsin(np.sqrt(D[1, 2]))))
    s3 = float(np.sqrt(D[0, 2]))
    c1 = float(np.sqrt(np.clip(D[0, 0] / (1.0 - D[0, 2]), 0, 1)))
    s1 = np.sqrt(max(0.0, 1.0 - c1 * c1))
    u = float(np.arccos(c1))
    v = float(np.arcsin(s3))
    if fi == 5:
        t2 = np.arctan(c1 / max(s1 * s3, 1e-300))
    elif fi == 6:
        t2 = np.arctan(c1 * s3 / max(s1, 1e-300))
    elif fi == 7:
        t2 = np.arctan(s1 / max(c1 * s3, 1e-300))
    else:
        t2 = np.arctan(s1 * s3 / max(c1, 1e-300))
    p = FPMAP[fi](u, v)
    # rebuild theta through FPMAP to stay consistent
    return (u, v)


def inv_E(ei, D):
    """Bisection D-inversion on edge-cell ei -> cube-edge theta vector."""
    ce = CUBE_EDGE_OF_E[ei]
    i1, v1, i2, v2, iv = ce
    # pick a varying support entry to invert: use the full-mismatch bisect
    def mism(t):
        th = [0.0, 0.0, 0.0]
        th[i1], th[i2], th[iv] = v1, v2, t
        Dd = Dof(th, 0.0)
        return np.max(np.abs(Dd - D))
    lo, hi = 1e-4, PI2 - 1e-4
    if mism(lo) < 1e-9:
        return lo
    if mism(hi) < 1e-9:
        return hi
    for _ in range(80):
        mid = 0.5 * (lo + hi)
        if mism(mid) < 1e-9:
            return mid
        # decide direction by comparing mismatch at mid vs quarter points
        if mism(0.5 * (lo + mid)) < mism(0.5 * (mid + hi)):
            hi = mid
        else:
            lo = mid
    return 0.5 * (lo + hi)


def Vrep_E(ei, t):
    ce = CUBE_EDGE_OF_E[ei]
    i1, v1, i2, v2, iv = ce
    th = [0.0, 0.0, 0.0]
    th[i1], th[i2], th[iv] = v1, v2, t
    return Vckm(th[0], th[1], th[2], 0.0)


def stratum_cell(D, tol=1e-9):
    """Cell id (F:15..23, E:6..14, V:0..5) from a D-magnitudes pattern."""
    zeros = [(i, k) for i in range(3) for k in range(3) if D[i, k] < tol]
    if len(zeros) == 1:
        return 15 + FZERO.index(zeros[0])
    supp = frozenset((i, k) for i in range(3) for k in range(3) if D[i, k] >= tol)
    if supp in EDGE_SUPPORT:
        return 6 + EDGE_SUPPORT[supp]
    for vi, p in enumerate(PERMS):
        if supp == frozenset((i, p[i]) for i in range(3)):
            return vi
    return None


def stratum_rep(cid, D):
    """Representative matrix V of the cell-rep matching magnitudes D."""
    if 15 <= cid < 24:
        fi = cid - 15
        u, v = inv_F(fi, D)
        return Vrep_F(fi, u, v)
    if 6 <= cid < 15:
        ei = cid - 6
        t = inv_E(ei, D)
        return Vrep_E(ei, t)
    if cid < 6:
        p = PERMS[cid]
        # corner: theta_k = 0 if p[k] == k else pi/2 (canonical choice)
        th = [0.0 if p[k] == k else PI2 for k in range(3)]
        return Vckm(th[0], th[1], th[2], 0.0)
    return None


# ----------------------------------------------------------------------------
# samplers
# ----------------------------------------------------------------------------
def F_sampler(fi, n):
    out = []
    while len(out) < n:
        u = rng.uniform(0.17, PI2 - 0.17)
        v = rng.uniform(0.17, PI2 - 0.17)
        p = FPMAP[fi](u, v)
        out.append((np.array([p[0], p[1], p[2]]), p[3], (u, v)))
    return out


def E_sampler(ei, n):
    ce = CUBE_EDGE_OF_E[ei]
    i1, v1, i2, v2, iv = ce
    out = []
    for tv in np.linspace(0.15, PI2 - 0.15, n):
        th = [0.0, 0.0, 0.0]
        th[i1], th[i2], th[iv] = v1, v2, float(tv)
        out.append((np.array(th, dtype=float), 0.0, float(tv)))
    return out


def R_sampler(rid, n):
    out = []
    dd = RKEYS[rid][1]
    while len(out) < n:
        th = rng.uniform(0.12, PI2 - 0.12, 3)
        c1, s1 = np.cos(th[0]), np.sin(th[0])
        c2, s2 = np.cos(th[1]), np.sin(th[1])
        s3 = np.sin(th[2])
        if dd == 0.0:
            g = (c1 * c2 - s1 * s2 * s3, s1 * s2 - c1 * c2 * s3)
            ok = (rid == 0 and g[0] > 1e-6 and g[1] > 1e-6) or \
                 (rid == 1 and g[0] < -1e-6) or (rid == 2 and g[1] < -1e-6)
        else:
            g = (s1 * c2 - c1 * s2 * s3, c1 * s2 - s1 * c2 * s3)
            ok = (rid == 3 and g[0] > 1e-6 and g[1] > 1e-6) or \
                 (rid == 4 and g[0] < -1e-6) or (rid == 5 and g[1] < -1e-6)
        if ok:
            out.append((th.copy(), dd))
            if len(out) >= n:
                break
    return out


with open("wave13c_base_data.json") as f:
    BD = json.load(f)
D_FACE = [{int(k): v for k, v in d.items()} for d in BD["D_FACE"]]
D_REG = [{int(k): v for k, v in d.items()} for d in BD["D_REG"]]
D_EDGE = [{int(k): v for k, v in d.items()} for d in BD["D_EDGE"]]
D_SHEET = [{int(k): v for k, v in d.items()} for d in BD["D_SHEET"]]
CMAP = {int(k): v[0] for k, v in BD["CMAP"].items()}


def cellname(cid):
    if cid < 6:
        return "V%s" % (PERMS[cid],)
    if cid < 15:
        rho, pi = EDGE_KEYS[cid - 6]
        return "E(r%s,q%s)" % (rho, pi)
    if cid < 24:
        return FNAMES[cid - 15]
    if cid < 30:
        return RKEYS[cid - 24][0]
    return ["s+", "s-"][cid - 30]


# ----------------------------------------------------------------------------
# kappa_at: stratum-aware
# ----------------------------------------------------------------------------
def kappa_at(th, d):
    U = Vckm(th[0], th[1], th[2], d) @ PSIG
    D = np.abs(U) ** 2
    cid = stratum_cell(D)
    if cid is not None:
        V = stratum_rep(cid, D)
    else:
        nf = ckm_normal(U)
        if nf is None:
            return None
        V = Vckm(nf[0], nf[1], nf[2], nf[3])
    ps = phase_solve(U, V)
    if ps is None:
        return None
    return uv_shift(ps[0])


# ----------------------------------------------------------------------------
hdr("P1: kappa on the 9 F-cells (sixths)")
KAPPA_F = {}
for fi in range(9):
    vals = []
    for (th, d, uv) in F_sampler(fi, 60):
        k = kappa_at(th, d)
        if k is not None:
            vals.append(k)
    KAPPA_F[fi] = round_report(vals, "kappa(%s)" % FNAMES[fi])
tick("P1 done")

hdr("P3: kappa on the 6 R-cells (sixths)")
KAPPA_R = {}
for rid in range(6):
    vals = []
    for (th, d) in R_sampler(rid, 60):
        k = kappa_at(th, d)
        if k is not None:
            vals.append(k)
    KAPPA_R[rid] = round_report(vals, "kappa(%s)" % RNAME[rid])
tick("P3 done")

hdr("P2: kappa on the 9 E-cells (S^1, sixths)")
KAPPA_E = {}
for ei in range(9):
    rho, pi = EDGE_KEYS[ei]
    a = FIXROW[(rho, pi)]
    vals = []
    for (th, d, tv) in E_sampler(ei, 24):
        k = kappa_at(th, d)
        if k is not None:
            vals.append(q_proj(a, k[0], k[1]))
    if vals:
        m = np.array(vals) * 6.0 % 6.0
        m = np.where(m > 5.75, m - 6.0, m)
        med = np.median(m)
        r = int(round(med)) % 6
        spread = float(np.max(np.abs(m - med)))
        ok = spread < 0.25 and len(vals) >= 8
        KAPPA_E[ei] = ((r,), ok, spread)
        print("  %-24s -> kappa_E=%d [n=%d spread %.3f] %s (row a=%d)" %
              (cellname(6 + ei), r, len(vals), spread, "OK" if ok else "FAIL", a))
    else:
        KAPPA_E[ei] = ((0,), False, 9.9)
        print("  %-24s -> NO SAMPLES" % cellname(6 + ei))
tick("P2 done")

# ----------------------------------------------------------------------------
hdr("P4: w(R->F) interface translations (sixths)")
R_F_INC = []
for rid in range(6):
    for ficell, co in sorted(D_REG[rid].items()):
        R_F_INC.append((rid, ficell - 15, co))
assert len(R_F_INC) == 18

W_RF = {}
for (rid, fi, co) in R_F_INC:
    dR = RKEYS[rid][1]
    vals = []
    for (th, d, uv) in F_sampler(fi, 30):
        # F-rep point p = FPMAP(u,v): the R-side form at the SAME locus point:
        if abs(d - dR) < 1e-9:
            # same-delta: R-side form == F-rep exactly -> w = 0 (verify once)
            VR = Vrep_F(fi, uv[0], uv[1])
            VF = Vrep_F(fi, uv[0], uv[1])
            ps = phase_solve(VR, VF)
            if ps is not None:
                vals.append(uv_shift(ps[0]))
        else:
            # cross-delta (pure F only): R-side form V(locus theta, dR)
            VR = Vckm(th[0], th[1], th[2], dR)
            VF = Vrep_F(fi, uv[0], uv[1])
            ps = phase_solve(VR, VF)
            if ps is not None:
                vals.append(uv_shift(ps[0]))
    W_RF[(rid, fi)] = round_report(vals, "w(%s->%s)" % (RNAME[rid], FNAMES[fi]))
tick("P4 done")

# ----------------------------------------------------------------------------
hdr("P5: tau(s->R) natural-gauge (near-limit soft conversions, eps=1e-4)")
TAU_S = {}
for si, (sname, dlo, dhi) in enumerate([("s+", 0.0, np.pi), ("s-", np.pi, 2 * np.pi)]):
    for rid in range(6):
        dtarget = RKEYS[rid][1]
        vals = []
        for trial in range(24):
            th = rng.uniform(0.12, PI2 - 0.12, 3)
            eps = 1e-4
            d = dtarget + eps if si == 0 else dtarget - eps
            if d < 0:
                d += 2 * np.pi
            if d > 2 * np.pi:
                d -= 2 * np.pi
            U1 = Vckm(th[0], th[1], th[2], d)
            U2 = Vckm(th[0], th[1], th[2], dtarget)
            ps = phase_solve_soft(U1, U2)
            if ps is not None and ps[1] < 0.02:
                vals.append(uv_shift(ps[0]))
        if vals:
            m = np.array(vals) * 6.0 % 6.0
            m = np.where(m > 5.75, m - 6.0, m)
            med = np.median(m, axis=0)
            r = tuple(np.round(med).astype(int) % 6)
            spread = float(np.max(np.abs(m - med)))
        else:
            r, spread = (0, 0), 9.9
        TAU_S[(si, rid)] = r
        print("  tau(%s->%-8s) = (%d,%d) [n=%d spread %.3f]" %
              (sname, RNAME[rid], r[0], r[1], len(vals), spread))
tick("P5 done")

# ----------------------------------------------------------------------------
hdr("P6: gamma-paths sheet->pureF (conversion V(wall-theta, delta) -> V(.,0))")
GAMMA_SLOPE = {}
for fi in range(5):
    wall = fi // 2
    for si, (sname, dlo, dhi) in enumerate([("s+", 0.0, np.pi), ("s-", np.pi, 2 * np.pi)]):
        samples = []
        for dd in np.linspace(dlo + 0.2, dhi - 0.2, 14):
            th = rng.uniform(0.2, PI2 - 0.2, 3)
            th[wall] = 0.0
            if fi == 1:
                th[0] = PI2
            if fi == 3:
                th[1] = PI2
            if fi == 4:
                th[2] = 0.0
            U = Vckm(th[0], th[1], th[2], dd)
            VF = Vckm(th[0], th[1], th[2], 0.0)
            ps = phase_solve(U, VF)
            if ps is not None:
                samples.append((dd, uv_shift(ps[0])))
        if len(samples) >= 10:
            def unwrap(arr):
                out = [arr[0]]
                for x in arr[1:]:
                    dstep = (x - out[-1] + 0.5) % 1.0 - 0.5
                    out.append(out[-1] + dstep)
                return out
            uu = unwrap([s[1][0] for s in samples])
            vv = unwrap([s[1][1] for s in samples])
            span = samples[-1][0] - samples[0][0]
            su = (uu[-1] - uu[0]) / span
            sv = (vv[-1] - vv[0]) / span
            GAMMA_SLOPE[(fi, si)] = (su, sv, uu[-1] - uu[0], vv[-1] - vv[0])
            print("  gamma(%s->%s): slope (%+.4f, %+.4f)/rad, endpoint (%+.3f, %+.3f) turns"
                  % (sname, FNAMES[fi], su, sv, uu[-1] - uu[0], vv[-1] - vv[0]))
        else:
            GAMMA_SLOPE[(fi, si)] = None
            print("  gamma(%s->%s): INSUFFICIENT SAMPLES (%d)" % (sname, FNAMES[fi], len(samples)))
tick("P6 done")

# ----------------------------------------------------------------------------
hdr("P7: F->E interface S^1-shifts (sixths)")
FE_INC = []
for fi in range(9):
    for ei, co in sorted(D_FACE[fi].items()):
        FE_INC.append((fi, ei - 6, co))
print("  (F,E) incidences: %d" % len(FE_INC))
SHIFT_FE = {}
for (fi, ei, co) in FE_INC:
    rho, pi = EDGE_KEYS[ei]
    a = FIXROW[(rho, pi)]
    vals = []
    # shared locus points: F-side rep on the SPECIFIC side attaching to ei
    # (determine the side->edge correspondence by labelling side points)
    side_of = {}
    for side in range(4):
        labs = set()
        for uu2 in (0.25 * PI2, 0.5 * PI2, 0.75 * PI2):
            if side == 0:
                us, vs = uu2, 0.0
            elif side == 1:
                us, vs = PI2, uu2
            elif side == 2:
                us, vs = uu2, PI2
            else:
                us, vs = 0.0, uu2
            Ds = Dof(list(FPMAP[fi](us, vs))[:3], FPMAP[fi](us, vs)[3])
            cid_s = stratum_cell(Ds)
            if cid_s is not None:
                labs.add(cid_s)
        if len(labs) == 1:
            side_of[list(labs)[0]] = side
    vals = []
    if 6 + ei in side_of:
        side = side_of[6 + ei]
        for trial in range(30):
            uu_ = rng.uniform(0.12, PI2 - 0.12)
            if side == 0:
                u, v = uu_, 0.0
            elif side == 1:
                u, v = PI2, uu_
            elif side == 2:
                u, v = uu_, PI2
            else:
                u, v = 0.0, uu_
            pF = FPMAP[fi](u, v)
            D = Dof([pF[0], pF[1], pF[2]], pF[3])
            # E-side: the D-inversion on the edge
            t = inv_E(ei, D)
            VE = Vrep_E(ei, t)
            VF = Vrep_F(fi, u, v)
            ps = phase_solve(VF, VE)
            if ps is not None:
                s = uv_shift(ps[0])
                vals.append(q_proj(a, s[0], s[1]))
    else:
        # corner-blowup edge of a mixed F: {(u0, th2, v0, dF), th2 free}
        blowup = {5: (PI2, 0.0), 6: (0.0, 0.0), 7: (0.0, 0.0), 8: (PI2, 0.0)}
        if fi in blowup:
            u0, v0 = blowup[fi]
            for trial in range(30):
                t2 = rng.uniform(0.1, PI2 - 0.1)
                VF = Vckm(u0, t2, v0, FPMAP[fi](0.3, 0.3)[3])
                D = np.abs(VF) ** 2
                t = inv_E(ei, D)
                VE = Vrep_E(ei, t)
                ps = phase_solve(VF, VE)
                if ps is not None:
                    s = uv_shift(ps[0])
                    vals.append(q_proj(a, s[0], s[1]))
    if vals:
        m = np.array(vals) * 6.0 % 6.0
        m = np.where(m > 5.75, m - 6.0, m)
        med = np.median(m)
        r = int(round(med)) % 6
        spread = float(np.max(np.abs(m - med)))
        ok = spread < 0.3 and len(vals) >= 10
        SHIFT_FE[(fi, ei)] = ((r,), ok, spread)
        print("  %s->%-22s shift=%d [n=%d spread %.3f] %s" %
              (FNAMES[fi], cellname(6 + ei), r, len(vals), spread, "OK" if ok else "SPREAD"))
    else:
        SHIFT_FE[(fi, ei)] = ((0,), False, 9.9)
        print("  %s->%-22s NO SAMPLES" % (FNAMES[fi], cellname(6 + ei)))
tick("P7 done")

# ----------------------------------------------------------------------------
hdr("P8: base orientation signs s_b")
SB = {}
for cid in range(6):
    SB[cid] = 1
for ei in range(9):
    cid = 6 + ei
    de = D_EDGE[ei]
    v1 = [k for k in de if de[k] == 1][0]
    v0 = [k for k in de if de[k] == -1][0]
    cE = CMAP[cid] - 6
    de2 = D_EDGE[cE]
    h2 = [k for k in de2 if de2[k] == 1][0]
    t2 = [k for k in de2 if de2[k] == -1][0]
    if CMAP[v0] == t2 and CMAP[v1] == h2:
        SB[cid] = 1
    elif CMAP[v0] == h2 and CMAP[v1] == t2:
        SB[cid] = -1
    else:
        raise AssertionError("edge c-map inconsistent at %s" % cellname(cid))
for fi in range(9):
    while True:
        u = rng.uniform(0.25, PI2 - 0.25)
        v = rng.uniform(0.25, PI2 - 0.25)
        p = FPMAP[fi](u, v)
        th = np.array([p[0], p[1], p[2]])
        U = Vckm(th[0], th[1], th[2], p[3])
        D = np.abs(U) ** 2
        cF = CMAP[15 + fi]
        V0 = stratum_rep(cF, np.abs(U @ PSIG) ** 2)
        if V0 is None:
            continue
        h = 2e-5
        cols = []
        ok = True
        for (du, dv) in [(h, 0), (0, h)]:
            p2 = FPMAP[fi](u + du, v + dv)
            U2 = Vckm(p2[0], p2[1], p2[2], p2[3])
            V2 = stratum_rep(cF, np.abs(U2 @ PSIG) ** 2)
            if V2 is None:
                ok = False
                break
            # param change of the c-image rep: use inv_F on cF
            D2 = np.abs(U2 @ PSIG) ** 2
            D1 = np.abs(U @ PSIG) ** 2
            w2 = inv_F(cF - 15, D2) if 15 <= cF < 24 else None
            w1 = inv_F(cF - 15, D1) if 15 <= cF < 24 else None
            if w2 is None or w1 is None:
                ok = False
                break
            cols.append([(w2[0] - w1[0]) / (du or dv), (w2[1] - w1[1]) / (du or dv)])
        if ok:
            J = np.array(cols)
            det = np.linalg.det(J)
            if abs(det) > 1e-4:
                SB[15 + fi] = 1 if det > 0 else -1
                print("  s(%-16s) = %+d (F-Jacobian det %+.2e)" % (FNAMES[fi], SB[15 + fi], det))
                break
for rid in range(6):
    while True:
        pts = R_sampler(rid, 1)
        th, d = pts[0]
        U = Vckm(th[0], th[1], th[2], d) @ PSIG      # <-- c-image!
        nf = ckm_normal(U)
        if nf is None:
            continue
        h = 1e-5
        cols = []
        ok = True
        for i in range(3):
            th2 = th.copy()
            th2[i] += h
            if th2[i] > PI2 - 1e-9:
                th2[i] -= 2 * h
            U2 = Vckm(th2[0], th2[1], th2[2], d) @ PSIG
            nf2 = ckm_normal(U2)
            if nf2 is None:
                ok = False
                break
            step = th2[i] - th[i]
            cols.append([(nf2[j] - nf[j]) / step for j in range(3)])
        if ok:
            J = np.array(cols).T
            det = np.linalg.det(J)
            if abs(det) > 1e-6:
                SB[24 + rid] = 1 if det > 0 else -1
                print("  s(%-16s) = %+d (R-Jacobian det %+.2e)" % (RNAME[rid], SB[24 + rid], det))
                break
for si, (sname, dmid) in enumerate([("s+", np.pi / 2), ("s-", 3 * np.pi / 2)]):
    while True:
        th = rng.uniform(0.3, PI2 - 0.3, 3)
        U = Vckm(th[0], th[1], th[2], dmid) @ PSIG   # <-- c-image!
        nf = ckm_normal(U)
        if nf is None:
            continue
        h = 1e-5
        cols = []
        ok = True
        for i in range(4):
            if i < 3:
                th2 = th.copy()
                th2[i] += h
                d2 = dmid
            else:
                th2 = th.copy()
                d2 = dmid + h
            U2 = Vckm(th2[0], th2[1], th2[2], d2) @ PSIG
            nf2 = ckm_normal(U2)
            if nf2 is None:
                ok = False
                break
            cols.append([(nf2[j] - nf[j]) / h for j in range(4)])
        if ok:
            J = np.array(cols).T
            det = np.linalg.det(J)
            if abs(det) > 1e-9:
                SB[30 + si] = 1 if det > 0 else -1
                print("  s(%-16s) = %+d (sheet-Jacobian det %+.2e)" % (sname, SB[30 + si], det))
                break
assert len(SB) == 32
tick("P8 done")

# ----------------------------------------------------------------------------
hdr("P9: consistency relations")


def add6(a, b):
    return ((a[0] + b[0]) % 6, (a[1] + b[1]) % 6)


def sub6(a, b):
    return ((a[0] - b[0]) % 6, (a[1] - b[1]) % 6)


bad = 0
print("(i) w-equivariance: w(cR->cF) = w(R->F) + kappa_F - kappa_R")
for (rid, fi) in sorted(W_RF.keys()):
    w = W_RF[(rid, fi)][0]
    cR = CMAP[24 + rid] - 24
    cF = CMAP[15 + fi] - 15
    if (cR, cF) in W_RF:
        wc = W_RF[(cR, cF)][0]
        pred = sub6(add6(w, KAPPA_F[fi][0]), KAPPA_R[rid][0])
        okv = wc == pred
        print("   w(%s->%s): %s vs pred %s %s" %
              (RNAME[rid], FNAMES[fi], wc, pred, "OK" if okv else "FAIL"))
        if not okv:
            bad += 1
print("(ii) kappa orbit sums (R and F): expect (0,0) mod 6")
for base, nm, KK in [(24, "R", KAPPA_R), (15, "F", KAPPA_F)]:
    for cid0 in [base + i for i in range(6 if nm == "R" else 9)]:
        c1 = CMAP[cid0]
        c2 = CMAP[c1]
        if cid0 < c1 < c2:
            k0 = KK[cid0 - base][0]
            k1 = KK[c1 - base][0]
            k2 = KK[c2 - base][0]
            tot = add6(add6(k0, k1), k2)
            st = "OK" if tot == (0, 0) else "FAIL"
            if tot != (0, 0):
                bad += 1
                print("   %s %s: %s + %s + %s = %s %s" % (nm, cellname(cid0), k0, k1, k2, tot, st))
print("   all orbit sums checked")
print("(iii) sign products s_b s_cb s_c2b = +1")
sp_bad = 0
for cid in range(32):
    c1 = CMAP[cid]
    c2 = CMAP[c1]
    if SB[cid] * SB[c1] * SB[c2] != 1:
        sp_bad += 1
        print("   %s: %+d FAIL" % (cellname(cid), SB[cid] * SB[c1] * SB[c2]))
bad += sp_bad
print("   sign products: %d failures" % sp_bad)
print("(iv) BASE dT = Td with signs (NEW certification)")


def bcol(cid):
    if cid < 6:
        return {}
    if cid < 15:
        return dict(D_EDGE[cid - 6])
    if cid < 24:
        return dict(D_FACE[cid - 15])
    if cid < 30:
        return dict(D_REG[cid - 24])
    return dict(D_SHEET[cid - 30])


basebad = 0
for cid in range(6, 32):
    lhs = {}
    for tgt, co in bcol(cid).items():
        lhs[CMAP[tgt]] = lhs.get(CMAP[tgt], 0) + co * SB[tgt]
    rhs = {k: v * SB[cid] for k, v in bcol(CMAP[cid]).items()}
    lhs = {k: v for k, v in lhs.items() if v != 0}
    rhs = {k: v for k, v in rhs.items() if v != 0}
    if lhs != rhs:
        basebad += 1
        print("   BASE dT!=Td at %s: lhs %s rhs %s" % (cellname(cid), lhs, rhs))
if basebad == 0:
    print("   BASE dT = Td (with signs) on all 32 base cells: OK [NEW CERT]")
bad += basebad
tick("P9 done")

out = {
    "KAPPA_F": {str(k): [list(map(int, v[0])), v[1], v[2]] for k, v in KAPPA_F.items()},
    "KAPPA_R": {str(k): [list(map(int, v[0])), v[1], v[2]] for k, v in KAPPA_R.items()},
    "KAPPA_E": {str(k): [list(map(int, v[0])), v[1], v[2]] for k, v in KAPPA_E.items()},
    "W_RF": {"%d,%d" % k: [list(map(int, v[0])), v[1], v[2]] for k, v in W_RF.items()},
    "TAU_S": {"%d,%d" % k: [int(x) for x in v] for k, v in TAU_S.items()},
    "SHIFT_FE": {"%d,%d" % k: [list(map(int, v[0])), v[1], v[2]] for k, v in SHIFT_FE.items()},
    "GAMMA_SLOPE": {"%d,%d" % k: ([float(x) for x in v] if v else None) for k, v in GAMMA_SLOPE.items()},
    "SB": {str(k): int(v) for k, v in SB.items()},
    "CONSISTENCY_BAD": int(bad),
}
with open("wave13c_pin_data.json", "w") as f:
    json.dump(out, f, indent=1)
print("\npin data -> wave13c_pin_data.json   (consistency failures: %d)" % bad)
hdr("WAVE 13C-2a COMPLETE")
