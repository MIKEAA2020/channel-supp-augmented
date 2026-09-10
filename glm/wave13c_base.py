#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
WAVE 13C-1 : THE BASE CELLULATION (32 cells) -- machine pinning of the
two-sheet book of WAVE13B_SPEC_REVIEW.md section 5.

Pins, numerically (integer outputs rounded from well-separated data):
  (B1) the 32 base cells + labelling mcell(theta,delta); partition check.
  (B2) d(E) endpoints; d(F) by boundary tracing of explicit parameter squares
       (INCLUDING the corner blowups of the mixed F's); d(R) by closure-face
       analysis with orientation signs; d(s) by the delta-arc rule.
  (B3) G0: base d^2=0 EXACTLY; base homology = (Z,0,0,0,Z), chi=+2 (M~S^4).
  (B4) the c-map on the 32 cells; fibre shifts [D_L] in sixths (for Part III).

Run:  python3 wave13c_base.py
"""
import itertools
import sys
import time
import json
import numpy as np

T0 = time.time()
SEP = "=" * 78
rng = np.random.default_rng(20260910)
PI2 = np.pi / 2.0
TOLZ = 1e-7
TOLS = 1e-9


def hdr(s):
    print("\n" + SEP)
    print(s)
    print(SEP)


def tick(msg):
    print("[t+%6.1fs] %s" % (time.time() - T0, msg))
    sys.stdout.flush()


# ----------------------------------------------------------------------------
# CKM machinery
# ----------------------------------------------------------------------------
PSIG = np.zeros((3, 3)); PSIG[0, 1] = 1; PSIG[1, 2] = 1; PSIG[2, 0] = 1
SIG = (1, 2, 0)      # 0-based: (U P_sig)_{ij} = U_{i, sig^{-1}(j)}


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


def Dof(t1, t2, t3, delta):
    return np.abs(Vckm(t1, t2, t3, delta)) ** 2


# ----------------------------------------------------------------------------
# cells
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
    assert len(pairs) == 3
    for (a, b) in pairs:
        EDGE_KEYS.append((a, pi) if comp(a, pi) == b else (b, pi))
assert len(EDGE_KEYS) == 9
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
NV, NE, NF, NR, NS = 6, 9, 9, 6, 2


def cellname(cid):
    if cid < NV:
        return "V%s" % (PERMS[cid],)
    if cid < NV + NE:
        rho, pi = EDGE_KEYS[cid - NV]
        return "E(r%s,q%s)" % (rho, pi)
    if cid < NV + NE + NF:
        return FNAMES[cid - NV - NE]
    if cid < NV + NE + NF + NR:
        return RKEYS[cid - NV - NE - NF][0]
    return ["s+", "s-"][cid - 30]


def gfun(th, d):
    c1, s1 = np.cos(th[0]), np.sin(th[0])
    c2, s2 = np.cos(th[1]), np.sin(th[1])
    s3 = np.sin(th[2])
    if d == 0.0:
        return (c1 * c2 - s1 * s2 * s3, s1 * s2 - c1 * c2 * s3)
    return (s1 * c2 - c1 * s2 * s3, c1 * s2 - s1 * c2 * s3)


def region_id(th, d):
    g6, g7 = gfun(th, 0.0)
    g8, g9 = gfun(th, np.pi)
    if d == 0.0:
        if g6 > TOLS and g7 > TOLS:
            return 0
        if g6 < -TOLS:
            return 1
        if g7 < -TOLS:
            return 2
    else:
        if g8 > TOLS and g9 > TOLS:
            return 3
        if g8 < -TOLS:
            return 4
        if g9 < -TOLS:
            return 5
    return None


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

def mcell(th, d):
    D = Dof(th[0], th[1], th[2], d)
    zeros = [(i, k) for i in range(3) for k in range(3) if D[i, k] < TOLZ]
    if len(zeros) == 0:
        if abs(np.sin(d)) < 1e-9:
            r = region_id(th, 0.0 if np.cos(d) > 0 else np.pi)
            return None if r is None else 24 + r
        return 30 + (0 if np.sin(d) > 0 else 1)
    if len(zeros) == 1:
        z = zeros[0]
        try:
            return 6 + 9 + FZERO.index(z)
        except ValueError:
            return None
    supp = frozenset((i, k) for i in range(3) for k in range(3) if D[i, k] >= TOLZ)
    if supp in EDGE_SUPPORT:
        return 6 + EDGE_SUPPORT[supp]
    for vi, p in enumerate(PERMS):
        if supp == frozenset((i, p[i]) for i in range(3)):
            return vi
    return None


# ----------------------------------------------------------------------------
hdr("PART B1: labelling + partition check (32 cells)")
# (i) generic interior points land on the two sheets (near-wall points may
#     fall below the zero tolerance; those are wall-adjacent, not mislabels)
nsheet = 0
nall = 0
for _ in range(40000):
    th = rng.uniform(0.03, PI2 - 0.03, 3)
    d = rng.uniform(0.03, 2 * np.pi - 0.03)
    c = mcell(th, d)
    nall += 1
    if c in (30, 31):
        nsheet += 1
assert nsheet / nall > 0.999, "interior points not on sheets: %.4f" % (nsheet / nall)
# (ii) each stratum sampled deliberately
seen = set([30, 31])
for d in (0.0, np.pi):
    for _ in range(6000):
        th = rng.uniform(0.02, PI2 - 0.02, 3)
        r = region_id(th, d)
        if r is not None:
            seen.add(24 + r)
for fi in range(9):
    for _ in range(3000):
        u = rng.uniform(0.03, PI2 - 0.03)
        v = rng.uniform(0.03, PI2 - 0.03)
        p = FPMAP[fi](u, v)
        c = mcell(np.array([p[0], p[1], p[2]]), p[3])
        if c is not None:
            seen.add(c)
CUBE_EDGES = []
for i1 in range(3):
    for v1 in (0.0, PI2):
        for i2 in range(i1 + 1, 3):
            for v2 in (0.0, PI2):
                CUBE_EDGES.append((i1, v1, i2, v2, 3 - i1 - i2))
for (i1, v1, i2, v2, iv) in CUBE_EDGES:
    for tv in np.linspace(0.02, PI2 - 0.02, 25):
        th = [0.0, 0.0, 0.0]
        th[i1], th[i2], th[iv] = v1, v2, tv
        for dd in (0.0, np.pi):
            c = mcell(np.array(th), dd)
            if c is not None:
                seen.add(c)
for p in PERMS:
    for dd in (0.0,):
        for corner in itertools.product((0.0, PI2), repeat=3):
            pass
# vertices: any corner with delta arbitrary (gauge) -> the M-class
for corner in itertools.product((0.0, PI2), repeat=3):
    for dd in (0.0, 0.7, np.pi):
        c = mcell(np.array(corner), dd)
        if c is not None:
            seen.add(c)
missing = [cellname(i) for i in range(32) if i not in seen]
assert not missing, "cells never labelled: %s" % missing
print("B1 PASS: 32-cell partition (all strata machine-verified)")
for d in (0.0, np.pi):
    vols = [0, 0, 0]
    for _ in range(30000):
        th = rng.uniform(0.01, PI2 - 0.01, 3)
        r = region_id(th, d)
        if r is not None:
            vols[r if d == 0.0 else r - 3] += 1
    print("  delta=%.0f region fractions %s (census: .235/.382/.384)" %
          (d, np.round(np.array(vols) / 30000.0, 3)))
tick("B1 done")

# ----------------------------------------------------------------------------
# B2a: d(E)
# ----------------------------------------------------------------------------
D_EDGE = []
for (rho, pi) in EDGE_KEYS:
    D_EDGE.append({PID[comp(rho, pi)]: 1, PID[rho]: -1})

# ----------------------------------------------------------------------------
# B2b: d(F) by boundary tracing
# ----------------------------------------------------------------------------


def edge_param(ei, th):
    rho, pi = EDGE_KEYS[ei]
    r2 = comp(rho, pi)
    D = Dof(th[0], th[1], th[2], 0.0)
    for i in range(3):
        if rho[i] != r2[i]:
            return float(D[i, r2[i]])
    raise AssertionError


def loop_pts(eps=2e-4, r=4e-4, nseg=3000):
    """CCW boundary of the eps-shrunk rounded square in the parameter
    (u,v)-domain (0,PI2)^2, with corner arcs of radius r."""
    a, b = eps, PI2 - eps
    pts = []
    n4 = nseg // 4
    for t in np.linspace(a, b - r, n4):
        pts.append((t, a))                                     # bottom ->
    for ang in np.linspace(-PI2, 0, 80):                       # corner (b,a)
        pts.append((b - r + r * np.cos(ang), a + r + r * np.sin(ang)))
    for t in np.linspace(a + r, b - r, n4):
        pts.append((b, t))                                     # right ->
    for ang in np.linspace(0, PI2, 80):                        # corner (b,b)
        pts.append((b - r + r * np.cos(ang), b - r + r * np.sin(ang)))
    for t in np.linspace(a + r, b - r, n4):
        pts.append((b - t + 0.0, b))                           # top <-
    for ang in np.linspace(PI2, np.pi, 80):                    # corner (a,b)
        pts.append((a + r + r * np.cos(ang), b - r + r * np.sin(ang)))
    for t in np.linspace(a + r, b - r, n4):
        pts.append((a, b - t))                                 # left <-
    for ang in np.linspace(np.pi, 1.5 * np.pi, 80):            # corner (a,a)
        pts.append((a + r + r * np.cos(ang), a + r + r * np.sin(ang)))
    return pts


def trace_boundary(fi):
    """d(F) via EXACT side evaluation + corner-blowup analysis.
    Parameter square (u,v) in [0,PI2]^2, CCW: bottom v=0 u:a->b; right u=b v:a->b;
    top v=b u:b->a; left u=a v:b->a.  Sides are evaluated at the EXACT bound
    (labels exact); corner blowups (mixed F's) detected by side-theta2 jumps."""
    pmap = FPMAP[fi]
    out = {}

    def lab_t(u, v):
        p = pmap(u, v)
        th = np.array([p[0], p[1], p[2]])
        c = mcell(th, p[3])
        t = edge_param(c - 6, th) if (c is not None and 6 <= c < 15) else None
        return c, t, p

    SIDES = [
        ("bottom", lambda s: (s, 0.0), +1),      # u: a->b
        ("right",  lambda s: (PI2, s), +1),      # v: a->b
        ("top",    lambda s: (s, PI2), -1),      # u: b->a
        ("left",   lambda s: (0.0, s), -1),      # v: b->a
    ]
    side_th2 = {}      # (side, corner) -> theta2 at that corner
    for (nm, f, dr) in SIDES:
        labs = set()
        dts = []
        for s in (0.22 * PI2, 0.5 * PI2, 0.78 * PI2):
            c, t, p = lab_t(*f(s))
            labs.add(c)
            dts.append(t)
        assert len(labs) == 1, "F%d side %s labels %s" % (fi, nm, labs)
        c = labs.pop()
        if c is None or not (6 <= c < 15):
            # vertex or crushed side: no edge term; record theta2 for corners
            for s in (0.02 * PI2, 0.98 * PI2):
                p = pmap(*f(s))
                side_th2[(nm, round(s / PI2))] = p[1]
            continue
        # traversal dt over the FULL side: t at exact endpoints (vertices)
        def t_exact(s):
            p = pmap(*f(s))
            th = np.array([p[0], p[1], p[2]])
            return edge_param(c - 6, th)
        t0 = t_exact(0.0)
        t1 = t_exact(PI2)
        if dr > 0:
            dt = t1 - t0
        else:
            dt = t0 - t1
        assert abs(abs(dt) - 1) < 1e-9, \
            "F%d side %s dt=%.6f" % (fi, nm, dt)
        out[c - 6] = out.get(c - 6, 0) + int(round(dt))
        for s in (0.02 * PI2, 0.98 * PI2):
            p = pmap(*f(s))
            side_th2[(nm, round(s / PI2))] = p[1]

    # corner blowups (mixed F's): at corners (u0, 0) [v0=0], the bottom and
    # left/right sides meet; a theta2 jump => the corner blows up onto the
    # cube edge {(th1,th3)=(u0,0), th2 free}.
    if fi >= 5:
        for u0 in (0.0, PI2):
            # incoming side / outgoing side per CCW:
            if u0 == 0.0:
                th2_in = side_th2[("left", 0)]
                th2_out = side_th2[("bottom", 0)]
            else:
                th2_in = side_th2[("bottom", 1)]
                th2_out = side_th2[("right", 0)]
            if abs(th2_in - th2_out) < 0.1:
                continue        # no blowup: corner -> vertex
            # blowup edge: (th1, th3) = (u0, 0), th2 varies
            thm = np.array([u0, 0.5 * PI2, 0.0])
            cm = mcell(thm, 0.0)
            assert cm is not None and 6 <= cm < 15, "blowup edge label %s" % cm
            t_in = edge_param(cm - 6, np.array([u0, th2_in, 0.0]))
            t_out = edge_param(cm - 6, np.array([u0, th2_out, 0.0]))
            dt = t_out - t_in
            assert abs(abs(dt) - 1) < 1e-6, "blowup dt %s" % dt
            out[cm - 6] = out.get(cm - 6, 0) + int(round(dt))
    return out



hdr("PART B2b: d(F) by exact-side tracing + corner blowups")
D_FACE = []
for fi in range(NF):
    tr = trace_boundary(fi)
    D_FACE.append({6 + e: v for e, v in tr.items()})
    s = " + ".join("%+d*%s" % (v, cellname(6 + e)) for e, v in sorted(tr.items()))
    print("  d(%-13s) = %s" % (FNAMES[fi], s if s else "0"))
tick("B2b done")

# ----------------------------------------------------------------------------

FACES = [
    (0, 0.0, (1, 2), 15),     # th1=0    -> F1
    (0, PI2, (1, 2), 16),     # th1=pi/2 -> F2
    (1, 0.0, (0, 2), 17),     # th2=0    -> F3
    (1, PI2, (0, 2), 18),     # th2=pi/2 -> F4
    (2, 0.0, (0, 1), 19),     # th3=0    -> F5
]

hdr("PART B2c: d(R) closure faces + orientation signs")

def face_frac(rid, face):
    idx, val, frees, _ = face
    hit = 0
    tot = 0
    for _ in range(240):
        q = rng.uniform(0.08, PI2 - 0.08, 2)
        th = [0.0, 0.0, 0.0]
        th[frees[0]], th[frees[1]] = q[0], q[1]
        tot += 1
        found = False
        for dirn in (+1, -1):
            th3 = list(th)
            th3[idx] = val + dirn * 1e-4
            th3 = [min(max(x, 1e-10), PI2 - 1e-10) for x in th3]
            if region_id(np.array(th3), RKEYS[rid][1]) == rid:
                found = True
                break
        hit += found
    return hit / float(tot)


def face_sign_pure(face):
    idx, val, frees, fcid = face
    sgn_out = -1.0 if val == 0.0 else +1.0
    return int(sgn_out * ((-1) ** idx))


D_REG = []
for rid in range(NR):
    terms = {}
    for face in FACES:
        fr = face_frac(rid, face)
        assert fr < 0.1 or fr > 0.9, "partial face closure %.2f R%d %s" % (
            fr, rid, FNAMES[face[3] - 15])
        if fr > 0.9:
            s = face_sign_pure(face)
            terms[face[3]] = terms.get(face[3], 0) + s
    # mixed F's on the same sheet
    dR = RKEYS[rid][1]
    for fi in (5, 6, 7, 8):
        dF = 0.0 if fi in (5, 6) else np.pi
        if abs(dR - dF) > 1e-9:
            continue
        # side of the region at the surface:
        side = 0
        for _ in range(200):
            u = rng.uniform(0.1, PI2 - 0.1)
            v = rng.uniform(0.1, PI2 - 0.1)
            thS = FPMAP[fi](u, v)
            for dth2 in (1e-3, -1e-3):
                thp = np.array([thS[0], thS[1] + dth2, thS[2]])
                if region_id(thp, dR) == rid:
                    gg = gfun(thp, dR)[fi - 5 if dR == 0.0 else fi - 7]
                    side = int(np.sign(gg))
                    break
            if side:
                break
        if side == 0:
            continue
        u0, v0 = 0.7, 0.6
        thS = FPMAP[fi](u0, v0)
        k = fi - 5 if dR == 0.0 else fi - 7
        gp = gfun(np.array([thS[0], thS[1] + 1e-5, thS[2]]), dR)[k]
        gm = gfun(np.array([thS[0], thS[1] - 1e-5, thS[2]]), dR)[k]
        b2 = int(np.sign(gp - gm))
        terms[15 + fi] = terms.get(15 + fi, 0) + side * b2
    D_REG.append({k: v for k, v in terms.items() if v != 0})
    s = " + ".join("%+d*%s" % (v, cellname(k)) for k, v in sorted(D_REG[-1].items()))
    print("  d(%-8s) = %s" % (RKEYS[rid][0], s))
tick("B2c done")

# ----------------------------------------------------------------------------
# B2d: d(s)
# ----------------------------------------------------------------------------
D_SHEET = [
    {24 + r: 1 for r in (3, 4, 5)},
    {24 + r: 1 for r in (0, 1, 2)},
]
D_SHEET[0].update({24 + r: -1 for r in (0, 1, 2)})
D_SHEET[1].update({24 + r: -1 for r in (3, 4, 5)})
print("\nd(s+) = sum R(pi-sheet) - sum R(0-sheet);  d(s-) = -d(s+)")

# ----------------------------------------------------------------------------
# B3: G0
# ----------------------------------------------------------------------------
hdr("PART B3: G0 -- base d^2=0 and base homology (expect S^4)")
CB = [NV, NE, NF, NR, NS]
BDIM = {}
c = 0
for k in range(5):
    for _ in range(CB[k]):
        BDIM[c] = k
        c += 1


def bcol(cid):
    if cid < NV:
        return {}
    if cid < NV + NE:
        return dict(D_EDGE[cid - NV])
    if cid < 24:
        return dict(D_FACE[cid - NV - NE])
    if cid < 30:
        return dict(D_REG[cid - 24])
    return dict(D_SHEET[cid - 30])


DB = {k: {} for k in range(1, 5)}
for cid in range(32):
    k = BDIM[cid]
    if k == 0:
        continue
    col = {}
    for tgt, co in bcol(cid).items():
        assert BDIM[tgt] == k - 1, "degree mismatch %s -> %s" % (
            cellname(cid), cellname(tgt))
        col[tgt] = col.get(tgt, 0) + co
    DB[k][cid] = {j: v for j, v in col.items() if v != 0}

bad = 0
for k in range(2, 5):
    for cid, col in DB[k].items():
        acc = {}
        for tgt, co in col.items():
            for tgt2, co2 in DB[k - 1].get(tgt, {}).items():
                acc[tgt2] = acc.get(tgt2, 0) + co * co2
        for v in acc.values():
            if v != 0:
                bad += 1
                print("  d^2 != 0: %s (deg %d): residual %d" % (cellname(cid), k, v))
assert bad == 0, "BASE d^2 = 0 FAILED (%d residuals)" % bad
print("BATTERY G0-a: base d^2 = 0 exactly: PASS")

from sympy import Matrix, zeros


def dense_bd(k):
    locK = [x for x in range(32) if BDIM[x] == k]
    locK1 = [x for x in range(32) if BDIM[x] == k - 1]
    M = np.zeros((len(locK1), len(locK)), dtype=np.int64)
    for cid, col in DB[k].items():
        for tgt, co in col.items():
            M[locK1.index(tgt), locK.index(cid)] = co
    return M


def rank_modp_dense(M, p):
    M = M.astype(np.int64) % p
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
        for i in range(m):
            if i != r and M[i, j]:
                M[i] = (M[i] - M[i, j] * M[r]) % p
        r += 1
    return r


for p in (101, 1009, 10007):
    ranks = [0] * 6
    for k in range(1, 5):
        ranks[k] = rank_modp_dense(dense_bd(k), p)
    b = [CB[k] - ranks[k] - ranks[k + 1] for k in range(5)]
    chi = sum((-1) ** k * CB[k] for k in range(5))
    print("mod-%5d Betti %s   chi=%+d" % (p, b, chi))
    assert b == [1, 0, 0, 0, 1], "base homology is not S^4: %s" % b
print("BATTERY G0-b: base homology = (Z,0,0,0,Z), chi=+2: PASS")
print("  => M = double(U3) ~ S^4: (H-top) U3 ~ B^4 certified by the cellulation.")
tick("B3 done")

# ----------------------------------------------------------------------------
# B4: c-map, fibre shifts
# ----------------------------------------------------------------------------
hdr("PART B4: c-map on base cells + fibre shifts (sixths)")


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


def fibre_shift(th, d):
    """(u,v) shift (turns mod 1) of the c-action on the fibre at (th,d):
    c(lambda V) = (lambda D_L) V' (mod right rephasing).  Gauge-invariant:
    ratios within a common column cancel M."""
    U = Vckm(th[0], th[1], th[2], d) @ PSIG
    nf = ckm_normal(U)
    if nf is None:
        return None
    V = Vckm(nf[0], nf[1], nf[2], nf[3])
    W = U / V
    # u = arg(D1/D0): from a column j with |V_0j|,|V_1j| both > .15
    u = v = None
    for j in range(3):
        if abs(V[0, j]) > 0.15 and abs(V[1, j]) > 0.15:
            u = np.angle(W[1, j] / W[0, j]) / (2 * np.pi)
            break
    for j in range(3):
        if abs(V[1, j]) > 0.15 and abs(V[2, j]) > 0.15:
            v = np.angle(W[2, j] / W[1, j]) / (2 * np.pi)
            break
    if u is None or v is None:
        return None
    return (u % 1.0, v % 1.0)


def cell_interior(cid, n=6):
    out = []
    guard = 0
    while len(out) < n and guard < 30000:
        guard += 1
        th = rng.uniform(0.04, PI2 - 0.04, 3)
        d = rng.uniform(0.04, 2 * np.pi - 0.04)
        if 30 <= cid < 32:
            if (0 if np.sin(d) > 0 else 1) != cid - 30 or abs(np.sin(d)) < 0.08:
                continue
        elif 24 <= cid < 30:
            dd = RKEYS[cid - 24][1]
            if region_id(th, dd) != cid - 24 or min(th) < 0.04:
                continue
            d = dd
        elif 15 <= cid < 24:
            fi = cid - 15
            if fi < 5:
                face = FACES[fi]
                q = rng.uniform(0.07, PI2 - 0.07, 2)
                th = [0.0, 0.0, 0.0]
                th[face[2][0]], th[face[2][1]] = q[0], q[1]
                th[face[0]] = face[1]
                d = 0.0
            else:
                u = rng.uniform(0.07, PI2 - 0.07)
                v = rng.uniform(0.07, PI2 - 0.07)
                p = FPMAP[fi](u, v)
                th, d = [p[0], p[1], p[2]], p[3]
        else:
            continue
        if mcell(np.array([th[0], th[1], th[2]]), d) == cid:
            out.append((np.array([th[0], th[1], th[2]]), d))
    return out


def to_sixths(shifts):
    m = np.array(shifts) * 6.0 % 6.0
    m = np.where(m > 5.75, m - 6.0, m)
    if m.size == 0:
        return None
    if np.max(np.abs(m - m[0])) < 0.12:
        return (int(round(m[0, 0])) % 6 if m.ndim == 2 else None)
    return "NONCONST"


def to_sixths2(shifts):
    m = np.array(shifts)
    m = (m * 6.0) % 6.0
    m = np.where(m > 5.75, m - 6.0, m)
    if np.max(np.abs(m - m[0])) < 0.12:
        return (int(round(m[0, 0])) % 6, int(round(m[0, 1])) % 6)
    return "NONCONST %s" % np.round(m, 2).tolist()


print("\nc-map on cells (image cell, fibre shift in sixths):")
CMAP = {}
# vertices: rho -> sigma o rho
for cid in range(NV):
    img = PID[comp(SIG, PERMS[cid])]
    CMAP[cid] = (img, None)
    print("  %-14s -> %-14s (perm)" % (cellname(cid), cellname(img)))
# edges: (rho,pi) -> (sigma o rho, pi)
for cid in range(NV, NV + NE):
    rho, pi = EDGE_KEYS[cid - NV]
    r1 = comp(SIG, rho)
    img = None
    for kk in ((r1, pi), (comp(r1, pi), pi)):
        if kk in EID:
            img = EID[kk]
            break
    assert img is not None
    CMAP[cid] = (NV + img, None)
    print("  %-14s -> %-14s (perm)" % (cellname(cid), cellname(NV + img)))
# F-cells: exact zero-pattern rule: zero (a,b) -> (a, sigma(b))
# ((U P_sig)_{ij} = U_{i,sig^{-1}(j)}: a zero of U in column b moves to
# column sigma(b) of U P_sig) -- pure algebra.
for cid in range(15, 24):
    fi = cid - 15
    z = FZERO[fi]
    zi = (z[0], SIG[z[1]])
    img = 15 + FZERO.index(zi)
    CMAP[cid] = (img, None)
    ver = set()
    for (th, d) in cell_interior(cid, n=6):
        U = Vckm(th[0], th[1], th[2], d) @ PSIG
        Du = np.abs(U) ** 2
        zs = [(i, k) for i in range(3) for k in range(3) if Du[i, k] < 1e-9]
        if len(zs) == 1 and zs[0] == zi:
            ver.add(img)
    assert img in ver, "F-map zero-pattern mismatch at %s" % cellname(cid)
    print("  %-14s -> %-14s (zero-pattern rule; kappa deferred)" %
          (cellname(cid), cellname(img)))
# R-cells and sheets: sampling (9-nonzero images -> normal form works)
for cid in list(range(24, 32)):
    samples = cell_interior(cid, n=8)
    imgs, shifts = set(), []
    for (th, d) in samples:
        U = Vckm(th[0], th[1], th[2], d) @ PSIG
        nf = ckm_normal(U)
        if nf is None:
            continue
        img = mcell(np.array([nf[0], nf[1], nf[2]]), nf[3])
        if img is None:
            continue
        imgs.add(img)
        fs = fibre_shift(th, d)
        if fs is not None:
            shifts.append(fs)
    assert len(imgs) == 1, "%s: c-image not unique: %s" % (
        cellname(cid), sorted(cellname(i) for i in imgs))
    img = imgs.pop()
    sh = to_sixths2(shifts) if shifts else None
    CMAP[cid] = (img, sh)
    if sh is not None and isinstance(sh, str):
        # sheets: kappa is a NON-CONSTANT drift field -- record range stats
        m = np.array(shifts) * 6.0 % 6.0
        m = np.where(m > 5.75, m - 6.0, m)
        print("  %-14s -> %-14s kappa DRIFTS: range u[%.2f,%.2f] v[%.2f,%.2f] "
              "sixths (flat pt pins t0^2=(4,4) / t0=(2,2))"
              % (cellname(cid), cellname(img),
                 m[:, 0].min(), m[:, 0].max(), m[:, 1].min(), m[:, 1].max()))
        CMAP[cid] = (img, "DRIFT")
    else:
        print("  %-14s -> %-14s kappa=%s" % (cellname(cid), cellname(img), sh))

# c^3 = id on cells + freeness
for cid in range(32):
    i1 = CMAP[cid][0]
    i2 = CMAP[i1][0]
    i3 = CMAP[i2][0]
    assert i3 == cid, "c^3 != id at %s" % cellname(cid)
fixed = [cid for cid in range(32) if CMAP[cid][0] == cid]
print("\nc^3 = id on all 32 cells: OK;  c-fixed base cells: %s (the two sheets)"
      % [cellname(x) for x in fixed])
assert sorted(fixed) == [30, 31]

tick("B4 done")

out = {
    "PERMS": [list(p) for p in PERMS],
    "EDGE_KEYS": [list(k) for k in EDGE_KEYS],
    "D_EDGE": [{str(k): v for k, v in d.items()} for d in D_EDGE],
    "D_FACE": [{str(k): v for k, v in d.items()} for d in D_FACE],
    "D_REG": [{str(k): v for k, v in d.items()} for d in D_REG],
    "D_SHEET": [{str(k): v for k, v in d.items()} for d in D_SHEET],
    "CMAP": {str(k): [v[0], v[1] if (v[1] is None or not isinstance(v[1], str)) else None]
             for k, v in CMAP.items()},
}
with open("wave13c_base_data.json", "w") as f:
    json.dump(out, f, indent=1)
print("\nbase data pinned -> wave13c_base_data.json")
hdr("WAVE 13C-1 COMPLETE: base cellulation certified (G0)")
