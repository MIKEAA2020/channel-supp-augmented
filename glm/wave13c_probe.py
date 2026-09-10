#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
WAVE 13C-2c : THE WALL/FUSION PROBE (pre-assembly, decisive).

Question: is the c-translation on the F-strata CONSTANT in the FUSED fibre
coordinates, or does it drift with the (absorbed) delta-direction?
The stage-2a pins measured kappa_F only at the rep-slices (delta_F = 0).
The prism/sweep structure of the sheet faces depends on the delta-drift.

Probes (all machine, sixths units):
  (Pr-1) For each pure wall F_w (source) and its c-image stratum:
         sample source points (theta_wall fixed, delta varying);
         measure the conversion L: V(theta,delta) P_sigma -> L * Vrep(cF);
         report uv_shift(L) (the translation in the image-rep convention)
         as a function of delta. Linear drift => fused-coordinate transfer.
  (Pr-2) The sheet->wall conversion gamma (re-measured, wall-attached,
         delta-varying) -- reconfirm slopes/endpoints per wall.
  (Pr-3) The sheet->R conversion at delta -> 0 / pi (natural tau = 0).
  (Pr-4) The c-image of the mixed-F strata (F3 -> F8): same question as Pr-1
         for the wall whose c-image is a MIXED stratum (the crux for dT=Td).

Run:  python3 wave13c_probe.py
"""
import itertools
import json
import sys
import time

import numpy as np

T0 = time.time()
SEP = "=" * 78
rng = np.random.default_rng(20260913)
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


# base structures (stage-1)
PERMS = sorted(itertools.permutations(range(3)))
FZERO = [(0, 1), (0, 0), (1, 2), (2, 2), (0, 2), (1, 1), (2, 0), (1, 0), (2, 1)]
FNAMES = ["F1{th1=0}", "F2{th1=pi/2}", "F3{th2=0}", "F4{th2=pi/2}", "F5{th3=0}",
          "F6{d0,D22}", "F7{d0,D31}", "F8{dpi,D21}", "F9{dpi,D32}"]
CMAP_F = [4, 0, 7, 6, 1, 2, 8, 5, 3]     # c(F_i) index (stage-1 pinned)
# F1->F5, F2->F1, F3->F8, F4->F7, F5->F2, F6->F3, F7->F9, F8->F6, F9->F4
assert CMAP_F[0] == 4 and CMAP_F[2] == 7 and CMAP_F[3] == 6


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


def unwrap_seq(vals):
    out = [vals[0]]
    for x in vals[1:]:
        d = (x - out[-1] + 0.5) % 1.0 - 0.5
        out.append(out[-1] + d)
    return out


def to_six(x):
    return (x * 6.0) % 6.0


# ----------------------------------------------------------------------------
# Pr-1: c-translation on wall strata, delta-varying.
#   source wall fi_s (pure, theta-fixed), points (theta_wall, o1, o2, delta).
#   image rep: the c-image stratum cF, its FPMAP-rep with parameters solved
#   from |V(theta,delta) P_sigma|^2 by the closed-form inversions.
# ----------------------------------------------------------------------------
hdr("Pr-1: c-translation on the pure walls (delta-varying, sixths)")


def inv_F(fi, D):
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
    return (u, v)


for fi_s in range(5):
    fi_t = CMAP_F[fi_s]
    wall = [0, 0, 0]
    wallval = [0.0, 0.0, 0.0]
    wall[0] = fi_s // 2
    wallval[0] = 0.0 if fi_s % 2 == 0 else PI2
    print("\n--- wall %s  ->  c-image %s ---" % (FNAMES[fi_s], FNAMES[fi_t]))
    rows = []
    for dd in np.linspace(0.25, np.pi - 0.25, 6):
        # source point: on the wall (exactly), other thetas generic
        o1 = rng.uniform(0.2, PI2 - 0.2)
        o2 = rng.uniform(0.2, PI2 - 0.2)
        th = [o1, o2, o1]
        th[wall[0]] = wallval[0]
        th = [th[0], th[1], th[2]]
        # place the free thetas into the two slots != wall
        slots = [k for k in range(3) if k != wall[0]]
        th[slots[0]], th[slots[1]] = o1, o2
        U = Vckm(th[0], th[1], th[2], dd) @ PSIG
        D = np.abs(U) ** 2
        uv = inv_F(fi_t, D)
        Vt = Vrep_F(fi_t, uv[0], uv[1])
        L = phase_solve(U, Vt)
        if L is None:
            rows.append((dd, None))
            continue
        rows.append((dd, uv_shift(L)))
    ok = [r for r in rows if r[1] is not None]
    if len(ok) < 4:
        print("  insufficient samples")
        continue
    us = unwrap_seq([to_six(r[1][0]) for r in ok])
    vs = unwrap_seq([to_six(r[1][1]) for r in ok])
    dds = [r[0] for r in ok]
    span = dds[-1] - dds[0]
    su = (us[-1] - us[0]) / span
    sv = (vs[-1] - vs[0]) / span
    print("  u-sixths: %s" % np.round(us, 2))
    print("  v-sixths: %s" % np.round(vs, 2))
    print("  slope (sixths/rad): (%+.3f, %+.3f)   [1/2pi*6 = 0.955]" % (su, sv))
    # expected: linear drift with slope = the fused-circle transfer
tick("Pr-1 done")


# ----------------------------------------------------------------------------
# Pr-4: the same for the F3-wall whose c-image is MIXED (F8), and F4 -> F7.
# ----------------------------------------------------------------------------
hdr("Pr-4: c-translation wall->MIXED stratum (F3->F8, F4->F7)")


def inv_F_mixed(fi, D, srcwall):
    # mixed reps need the two free params (u,v); solve from magnitudes:
    # for F7/F8/F9 the rep has delta = pi; params (u,v) are (th1, th3).
    u = float(np.arccos(np.sqrt(np.clip(D[0, 0] / (1.0 - D[0, 2]), 0, 1))))
    v = float(np.arcsin(np.sqrt(D[0, 2])))
    return (u, v)


for fi_s in (2, 3):
    fi_t = CMAP_F[fi_s]
    wall = fi_s // 2 + 1        # theta2 for both F3,F4
    wallval = 0.0 if fi_s == 2 else PI2
    print("\n--- wall %s  ->  c-image %s (MIXED) ---" % (FNAMES[fi_s], FNAMES[fi_t]))
    rows = []
    for dd in np.linspace(0.25, np.pi - 0.25, 6):
        th = [0.0, 0.0, 0.0]
        th[0] = rng.uniform(0.2, PI2 - 0.2)
        th[2] = rng.uniform(0.2, PI2 - 0.2)
        th[1] = wallval
        U = Vckm(th[0], th[1], th[2], dd) @ PSIG
        D = np.abs(U) ** 2
        # the image is on the mixed stratum: D[0,0]-ish determined;
        # rep params: (u, v) from the closed forms (th1, th3 of the rep)
        s3 = float(np.sqrt(D[0, 2]))
        c1 = float(np.sqrt(np.clip(D[0, 0] / (1.0 - D[0, 2]), 0, 1)))
        s1 = np.sqrt(max(0.0, 1.0 - c1 * c1))
        u = float(np.arccos(c1))
        v = float(np.arcsin(s3))
        if fi_t == 7:
            t2 = np.arctan(s1 / max(c1 * s3, 1e-300))
        elif fi_t == 6:
            t2 = np.arctan(c1 * s3 / max(s1, 1e-300))
        Vt = Vckm(u, t2, v, np.pi)
        L = phase_solve(U, Vt)
        if L is None:
            rows.append((dd, None))
            continue
        rows.append((dd, uv_shift(L)))
    ok = [r for r in rows if r[1] is not None]
    if len(ok) < 4:
        print("  insufficient samples (%d)" % len(ok))
        continue
    us = unwrap_seq([to_six(r[1][0]) for r in ok])
    vs = unwrap_seq([to_six(r[1][1]) for r in ok])
    dds = [r[0] for r in ok]
    span = dds[-1] - dds[0]
    print("  u-sixths: %s" % np.round(us, 2))
    print("  v-sixths: %s" % np.round(vs, 2))
    print("  slope (sixths/rad): (%+.3f, %+.3f)" % ((us[-1]-us[0])/span, (vs[-1]-vs[0])/span))
tick("Pr-4 done")

# ----------------------------------------------------------------------------
# Pr-2: sheet->wall gamma, re-measured at the wall (both sign conventions),
#       deltas on (0,pi) and (pi,2pi).
# ----------------------------------------------------------------------------
hdr("Pr-2: sheet->wall gamma paths (delta-varying, wall-attached, sixths)")
for fi in range(5):
    wall = fi // 2
    for (lo, hi, nm) in [(0.05, np.pi - 0.05, "s+"), (np.pi + 0.05, 2 * np.pi - 0.05, "s-")]:
        pts = []
        for dd in np.linspace(lo, hi, 8):
            th = [rng.uniform(0.2, PI2 - 0.2) for _ in range(3)]
            th[wall] = 0.0 if fi % 2 == 0 else PI2
            Uw = Vckm(th[0], th[1], th[2], dd)
            VF = Vckm(th[0], th[1], th[2], 0.0)
            L = phase_solve(Uw, VF)
            if L is not None:
                pts.append((dd, uv_shift(L)))
        if len(pts) < 6:
            print("  gamma(%s->%s): insufficient" % (nm, FNAMES[fi]))
            continue
        us = unwrap_seq([to_six(p[1][0]) for p in pts])
        vs = unwrap_seq([to_six(p[1][1]) for p in pts])
        span = pts[-1][0] - pts[0][0]
        print("  gamma(%s->%-12s): slope (%+.3f,%+.3f)/rad  u:%s v:%s" %
              (nm, FNAMES[fi], (us[-1]-us[0])/span, (vs[-1]-vs[0])/span,
               np.round(us, 2), np.round(vs, 2)))
tick("Pr-2 done")

# ----------------------------------------------------------------------------
# Pr-3: sheet->R conversion (delta -> 0 and pi): natural tau
# ----------------------------------------------------------------------------
hdr("Pr-3: sheet->R natural conversions (eps-limit)")
for (dtarget, nm) in [(0.0, "delta->0+"), (np.pi, "delta->pi-"), (2*np.pi, "delta->2pi-")]:
    vals = []
    for trial in range(20):
        th = rng.uniform(0.15, PI2 - 0.15, 3)
        eps = 1e-4
        d = (dtarget + eps) % (2 * np.pi)
        U1 = Vckm(th[0], th[1], th[2], d)
        U2 = Vckm(th[0], th[1], th[2], dtarget % (2 * np.pi))
        L = phase_solve(U1, U2)
        if L is not None:
            vals.append(uv_shift(L))
    if vals:
        m = np.array(vals) * 6.0 % 6.0
        m = np.where(m > 5.75, m - 6.0, m)
        print("  %s: median %s  spread %.3f  [n=%d]" %
              (nm, np.round(np.median(m, axis=0), 2), np.max(np.abs(m - np.median(m, axis=0))), len(vals)))
    else:
        print("  %s: no samples" % nm)
tick("Pr-3 done")

hdr("PROBE COMPLETE")
