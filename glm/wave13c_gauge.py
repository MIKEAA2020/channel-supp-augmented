#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
WAVE 13C-2b : THE SHEET GAUGE (stage 2, part 2) -- v2
Gauge g = exp(2pi.i((2/3)D1 + (1/3)D2)) on both sheets with T^3-lift tracking.
  (G1) D_L field on a (theta,delta) grid per sheet + BFS lift tracking
  (G2) cocycle-lift relation D1+D2+D3 = k*2pi   (k=(0,2,1) on s+, (0,1,2) on s-)
  (G3) gauge equation -[g]+kappa+[g].c = t0^2 / t0  on the grid
  (G4) tau~(s->R) = -[g]|_R-face (12 values, sixths; branch-continued samples)
  (G5) gauged gamma-paths gamma~ = gamma - [g]|_F-face (10 paths)
Run:  python3 wave13c_gauge.py
"""
import json
import sys
import time

import numpy as np

T0 = time.time()
SEP = "=" * 78
rng = np.random.default_rng(20260912)
PI2 = np.pi / 2.0


def hdr(s):
    print("\n" + SEP)
    print(s)
    print(SEP)


def tick(msg):
    print("[t+%6.1fs] %s" % (time.time() - T0, msg))
    sys.stdout.flush()


PSIG = np.zeros((3, 3)); PSIG[0, 1] = 1; PSIG[1, 2] = 1; PSIG[2, 0] = 1


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


def phase_solve(U, V, tol=0.03, ctol=1e-6):
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
    return np.array(L)


def uv_shift(L):
    u = (L[1] - L[0]) / (2 * np.pi)
    v = (L[2] - L[1]) / (2 * np.pi)
    return (u % 1.0, v % 1.0)


def D_L_raw(th, d):
    U = Vckm(th[0], th[1], th[2], d) @ PSIG
    nf = ckm_normal(U)
    if nf is None:
        return None
    V = Vckm(nf[0], nf[1], nf[2], nf[3])
    L = phase_solve(U, V)
    if L is None:
        return None
    return np.array(L)


def unwrap_to(ref, val):
    return val + 2 * np.pi * np.round((ref - val) / (2 * np.pi))


def gclass(D1lift, D2lift):
    """T^2 class (u,v turns) of g = exp(2pi i ((2/3)D1 + (1/3)D2))."""
    v = (2.0 / 3.0) * D1lift + (1.0 / 3.0) * D2lift
    return np.array([(v[1] - v[0]) / (2 * np.pi), (v[2] - v[1]) / (2 * np.pi)]) % 1.0


# flat point, base lifts
FP = np.array([np.arccos(1 / np.sqrt(2)), np.arccos(1 / np.sqrt(2)),
               np.arccos(np.sqrt(2.0 / 3.0))])
# t0^2 = diag(1, w^2, w) : phases (0, 4pi/3, 2pi/3); 3x = (0,2,1)*2pi
BASE_PLUS = np.array([0.0, 4 * np.pi / 3.0, 2 * np.pi / 3.0])
# t0    = diag(1, w, w^2): phases (0, 2pi/3, 4pi/3); 3x = (0,1,2)*2pi
BASE_MINUS = np.array([0.0, 2 * np.pi / 3.0, 4 * np.pi / 3.0])

NTH, ND = 5, 7
THS = np.linspace(0.12, PI2 - 0.12, NTH)


def build_lifts(dlo, dhi):
    ds = np.linspace(dlo + 0.12, dhi - 0.12, ND)
    nodes = {}
    for i1, a in enumerate(THS):
        for i2, b in enumerate(THS):
            for i3, c in enumerate(THS):
                for jd, d in enumerate(ds):
                    nodes[(i1, i2, i3, jd)] = (np.array([a, b, c]), float(d))
    D1, D2, D3 = {}, {}, {}
    ccoord = {}
    for key, (th, d) in nodes.items():
        U = Vckm(th[0], th[1], th[2], d) @ PSIG
        nf1 = ckm_normal(U)
        if nf1 is None:
            continue
        U2 = Vckm(*nf1) @ PSIG
        nf2 = ckm_normal(U2)
        if nf2 is None:
            continue
        ccoord[key] = (nf1, nf2)
    dmid = 0.5 * (dlo + dhi)
    start = (int(np.argmin(np.abs(THS - FP[0]))), int(np.argmin(np.abs(THS - FP[1]))),
             int(np.argmin(np.abs(THS - FP[2]))), int(np.argmin(np.abs(ds - dmid))))
    base = BASE_PLUS if dlo == 0.0 else BASE_MINUS
    D1[start] = base.copy()
    D2[start] = base.copy()
    D3[start] = base.copy()
    frontier = [start]
    while frontier:
        nxt = []
        for key in frontier:
            (i1, i2, i3, jd) = key
            for step in [(1, 0, 0, 0), (-1, 0, 0, 0), (0, 1, 0, 0), (0, -1, 0, 0),
                         (0, 0, 1, 0), (0, 0, -1, 0), (0, 0, 0, 1), (0, 0, 0, -1)]:
                nk = (i1 + step[0], i2 + step[1], i3 + step[2], jd + step[3])
                if nk not in nodes or nk in D1 or nk not in ccoord:
                    continue
                th, d = nodes[nk]
                nf1, nf2 = ccoord[nk]
                r1 = D_L_raw(th, d)
                r2 = D_L_raw(np.array(nf1[:3]), nf1[3])
                r3 = D_L_raw(np.array(nf2[:3]), nf2[3])
                if r1 is None or r2 is None or r3 is None:
                    continue
                D1[nk] = unwrap_to(D1[key], r1)
                D2[nk] = unwrap_to(D2[key], r2)
                D3[nk] = unwrap_to(D3[key], r3)
                nxt.append(nk)
        frontier = nxt
    return nodes, D1, D2, D3, ds


hdr("G1-G3: lifts, cocycle, gauge equation (both sheets)")
RESULTS = {}
for si, (sname, dlo, dhi, kvec) in enumerate([
        ("s+", 0.0, np.pi, np.array([0.0, 2.0, 1.0])),
        ("s-", np.pi, 2 * np.pi, np.array([0.0, 1.0, 2.0]))]):
    nodes, D1, D2, D3, ds = build_lifts(dlo, dhi)
    # remove near-corner outliers whose c^2-image hits a degenerate stratum
    bad = [k for k in D1
           if np.max(np.abs((D1[k] + D2[k] + D3[k]) / (2 * np.pi) - kvec)) > 0.02]
    for k in bad:
        del D1[k], D2[k], D3[k]
    print("%s: %d / %d grid nodes lifted (%d near-corner outliers excluded)"
          % (sname, len(D1), len(nodes), len(bad)))
    devs = np.array([np.max(np.abs((D1[k] + D2[k] + D3[k]) / (2 * np.pi) - kvec))
                     for k in D1])
    print("  cocycle-lift D1+D2+D3 = %s: max dev %.4f" % (kvec.tolist(), devs.max()))
    assert devs.max() < 0.02, "lift tracking failed on %s" % sname
    tgt = np.array([2 / 3.0, 2 / 3.0]) if si == 0 else np.array([1 / 3.0, 1 / 3.0])
    gerrs = []
    for k in D1:
        g = gclass(D1[k], D2[k])
        gc = gclass(D2[k], D3[k])
        kap = np.array([(D1[k][1] - D1[k][0]), (D1[k][2] - D1[k][1])]) / (2 * np.pi)
        eq = (kap - g + gc) % 1.0
        dev = (eq - tgt + 0.5) % 1.0 - 0.5
        gerrs.append(np.max(np.abs(dev)))
    gerrs = np.array(gerrs)
    print("  gauge equation: max dev %.5f (n=%d)" % (gerrs.max(), len(gerrs)))
    assert gerrs.max() < 0.02, "gauge equation fails on %s" % sname
    RESULTS[sname] = (nodes, D1, D2, D3, ds)
tick("G1-G3 done")


def g_at(th, d, sname):
    """Branch-continued [g]-class at an arbitrary sheet point (nearest grid node)."""
    nodes, D1, D2, D3, ds = RESULTS[sname]
    dlo, dhi = (0.0, np.pi) if sname == "s+" else (np.pi, 2 * np.pi)
    i1 = int(np.clip(np.argmin(np.abs(THS - th[0])), 0, NTH - 1))
    i2 = int(np.clip(np.argmin(np.abs(THS - th[1])), 0, NTH - 1))
    i3 = int(np.clip(np.argmin(np.abs(THS - th[2])), 0, NTH - 1))
    jd = int(np.clip(np.argmin(np.abs(ds - d)), 0, ND - 1))
    key = (i1, i2, i3, jd)
    if key not in D1:
        return None
    r1 = D_L_raw(th, d)
    U = Vckm(th[0], th[1], th[2], d) @ PSIG
    nf1 = ckm_normal(U)
    if r1 is None or nf1 is None:
        return None
    r2 = D_L_raw(np.array(nf1[:3]), nf1[3])
    if r2 is None:
        return None
    l1 = unwrap_to(D1[key], r1)
    l2 = unwrap_to(D2[key], r2)
    return gclass(l1, l2)


# ----------------------------------------------------------------------------
hdr("G4: tau~(s->R) = -[g]|_R-face (sixths)")
RKEYS = [("R0.def", 0.0), ("R0.bF6", 0.0), ("R0.bF7", 0.0),
         ("R1.def", np.pi), ("R1.bF8", np.pi), ("R1.bF9", np.pi)]
RNAME = [r[0] for r in RKEYS]
TAU_TILDE = {}
for sname in ("s+", "s-"):
    dlo, dhi = (0.0, np.pi) if sname == "s+" else (np.pi, 2 * np.pi)
    for rid in range(6):
        dtarget = RKEYS[rid][1]
        eps = 0.04 if dtarget == 0.0 else -0.04
        if sname == "s+":
            d = dtarget + (0.04 if dtarget == 0.0 else -0.04)
        else:
            d = dtarget + (-0.04 if dtarget == 0.0 else 0.04)
            if d < 0:
                d += 2 * np.pi
        vals2 = []
        for trial in range(30):
            th = rng.uniform(0.15, PI2 - 0.15, 3)
            g = g_at(th, d, sname)
            if g is not None:
                vals2.append(((-g[0]) % 1.0, (-g[1]) % 1.0))
        if vals2:
            m = np.array(vals2) * 6.0 % 6.0
            m = np.where(m > 5.75, m - 6.0, m)
            med = np.median(m, axis=0)
            spread = float(np.max(np.abs(m - med)))
            r = tuple(np.round(med).astype(int) % 6)
            TAU_TILDE[(sname, rid)] = (r, spread, len(vals2))
            print("  tau~(%s->%-8s) = (%d,%d) [n=%d spread %.3f] %s" %
                  (sname, RNAME[rid], r[0], r[1], len(vals2), spread,
                   "OK" if spread < 0.3 else "DRIFT"))
        else:
            TAU_TILDE[(sname, rid)] = ((0, 0), 9.9, 0)
            print("  tau~(%s->%-8s) NO SAMPLES" % (sname, RNAME[rid]))
tick("G4 done")

# ----------------------------------------------------------------------------
hdr("G5: gauged gamma-paths gamma~ = gamma - [g]|_F-face")
FNB = ["F1{th1=0}", "F2{th1=pi/2}", "F3{th2=0}", "F4{th2=pi/2}", "F5{th3=0}"]
GAMMA_T = {}
for fi in range(5):
    wall = fi // 2
    for sname, (dlo, dhi) in [("s+", (0.0, np.pi)), ("s-", (np.pi, 2 * np.pi))]:
        pts = []
        for dd in np.linspace(dlo + 0.15, dhi - 0.15, 10):
            th = rng.uniform(0.2, PI2 - 0.2, 3)
            th[wall] = 0.04
            if fi == 1:
                th[0] = PI2 - 0.04
            if fi == 3:
                th[1] = PI2 - 0.04
            if fi == 4:
                th[2] = 0.04
            Lg = phase_solve(Vckm(th[0], th[1], th[2], dd),
                             Vckm(th[0], th[1], th[2], 0.0) if th[wall] < 0.1
                             else Vckm(th[0], th[1], th[2], 0.0))
            # natural gamma: wall value ~0; for F2/F4 the wall is pi/2 with
            # the rep at wall value pi/2 as well (rep delta=0)
            if Lg is None:
                continue
            gam = np.array(uv_shift(Lg))
            g = g_at(th, dd, sname)
            if g is None:
                continue
            gtil = (gam - g) % 1.0
            pts.append((dd, gtil))
        if len(pts) >= 7:
            def unwrap(arr):
                out = [arr[0]]
                for x in arr[1:]:
                    dstep = (x - out[-1] + 0.5) % 1.0 - 0.5
                    out.append(out[-1] + dstep)
                return out
            uu = unwrap([p[1][0] for p in pts])
            vv = unwrap([p[1][1] for p in pts])
            span = pts[-1][0] - pts[0][0]
            su, sv = (uu[-1] - uu[0]) / span, (vv[-1] - vv[0]) / span
            ts = np.array([(p[0] - pts[0][0]) / span for p in pts])
            ru = np.max(np.abs(np.array(uu) - (uu[0] + (uu[-1] - uu[0]) * ts)))
            rv = np.max(np.abs(np.array(vv) - (vv[0] + (vv[-1] - vv[0]) * ts)))
            GAMMA_T[(fi, sname)] = (su, sv, uu[0], vv[0], uu[-1], vv[-1],
                                    float(max(ru, rv)))
            print("  gamma~(%s->%s): slope (%+.3f,%+.3f)/rad  (%+.3f,%+.3f)->(%+.3f,%+.3f) "
                  "[lin.res %.4f]" % (sname, FNB[fi], su, sv, uu[0], vv[0],
                                      uu[-1], vv[-1], max(ru, rv)))
        else:
            GAMMA_T[(fi, sname)] = None
            print("  gamma~(%s->%s): INSUFFICIENT (%d)" % (sname, FNB[fi], len(pts)))
tick("G5 done")

out = {
    "TAU_TILDE": {"%s,%d" % k: [list(map(int, v[0])), v[1], v[2]]
                  for k, v in TAU_TILDE.items()},
    "GAMMA_T": {"%d,%s" % k: ([float(x) for x in v] if v else None)
                for k, v in GAMMA_T.items()},
}
with open("wave13c_gauge_data.json", "w") as f:
    json.dump(out, f, indent=1)
print("\ngauge data -> wave13c_gauge_data.json")
hdr("WAVE 13C-2b COMPLETE (gauge)")
