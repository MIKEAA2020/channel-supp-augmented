#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
WAVE 28 - MODULE 1 (the dedicated re-implementation, part 1 of 3):
THE BASE CELLULATION (32 cells) -- a fresh, independent re-implementation of
the WAVE 13C-1 stage, executed per the W27 merit verdict ("the bounded,
merited next-session item: closes bridge-audit residual (i)").

INDEPENDENCE STATEMENT (what is fresh here vs. the 13C-1 original):
  * fresh geometry code (own CKM parameterisation layout, own zero-pattern
    classifier, own inverse normaliser re-derived from the D-entries);
  * d(E) from the endpoint algebra (same orientation convention as the
    committed labelling -- the labelling is spec, the code is fresh);
  * d(F) from a dense-sampling boundary tracer of the (u,v)-parameter
    squares: side labels by support matching, traversal degrees from the
    endpoint values of the varying D-entry, ALL FOUR corners checked for
    blowups (the original checked two) with own CCW corner bookkeeping;
  * d(R) from an exact face-membership analysis of the g-wall regions (the
    original used Monte-Carlo face_frac + a sign formula; here the region
    membership on the six theta-cube faces is decided EXACTLY from the
    wall equations, and the face signs from the outward-normal determinant
    rule det[t_u, t_v, n_out] computed numerically at wall points);
  * d(s) from the delta-interval boundary rule (own derivation);
  * CMAP for V/E/F from the column-shift algebra (own code), for R/s from
    fresh sampling through the fresh normaliser;
  * G0 certification (d^2=0 + base homology) via EXACT INTEGER Smith
    normal form (sympy) -- the original used mod-p ranks; and
  * every field compared against the committed wave13c_base_data.json.

Run:  python3 w28_base.py   (cwd = glm/; output: w28_base_output.txt)
"""
import itertools
import json
import sys
import time

import numpy as np
from sympy import Matrix

T0 = time.time()
SEP = "=" * 78
RNG = np.random.default_rng(20280913)
HALFPI = np.pi / 2.0
TOL = 1e-9


def hdr(s):
    print("\n" + SEP)
    print(s)
    print(SEP)
    sys.stdout.flush()


def tick(msg):
    print("[t+%6.1fs] %s" % (time.time() - T0, msg))
    sys.stdout.flush()


# ----------------------------------------------------------------------------
# the geometry, fresh
# ----------------------------------------------------------------------------
# The CKM parameterisation of U(3) modulo the right diagonal torus (spec):
#   V(t1,t2,t3,d) rows built from the (c_k, s_k) pairs; d = the CKM phase.
# Fresh layout: assemble row by row from the angle tables.
def V3(t1, t2, t3, d):
    c1, s1 = np.cos(t1), np.sin(t1)
    c2, s2 = np.cos(t2), np.sin(t2)
    c3, s3 = np.cos(t3), np.sin(t3)
    ph = np.exp(1j * d)
    row0 = np.array([c1 * c3, s1 * c3, s3 * np.conj(ph)])
    row1 = np.array([-s1 * c2 - c1 * s2 * s3 * ph,
                     c1 * c2 - s1 * s2 * s3 * ph,
                     s2 * c3])
    row2 = np.array([s1 * s2 - c1 * c2 * s3 * ph,
                     -c1 * s2 - s1 * c2 * s3 * ph,
                     c2 * c3])
    return np.array([row0, row1, row2])


# the cyclic column permutation P_sigma: (U P)_ij = U_{i, j-1 mod 3}
PCYC = np.zeros((3, 3))
PCYC[0, 1] = PCYC[1, 2] = PCYC[2, 0] = 1.0
SIG = (1, 2, 0)          # old column b -> new column SIG[b]


def shift_cols(U):
    return U @ PCYC


def Dmat(U):
    return np.abs(U) ** 2


# ---- the wall equations (fresh derivation from the zero-entries) ---------
# delta = 0:   D[1,1] = (c1c2 - s1s2s3)^2  -> g6 := c1c2 - s1s2s3   (F6 wall)
#              D[2,0] = (s1s2 - c1c2s3)^2  -> g7 := s1s2 - c1c2s3   (F7 wall)
# delta = pi:  D[1,0] = (s1c2 - c1s2s3)^2  -> g8 := s1c2 - c1s2s3   (F8 wall)
#              D[2,1] = (c1s2 - s1c2s3)^2  -> g9 := c1s2 - s1c2s3   (F9 wall)
def walls(th, d):
    c1, s1 = np.cos(th[0]), np.sin(th[0])
    c2, s2 = np.cos(th[1]), np.sin(th[1])
    s3 = np.sin(th[2])
    if abs(np.cos(d) - 1.0) < 1e-12:          # d = 0
        return (c1 * c2 - s1 * s2 * s3, s1 * s2 - c1 * c2 * s3)
    return (s1 * c2 - c1 * s2 * s3, c1 * s2 - s1 * c2 * s3)


def region_of(th, d):
    """wall-region id 0..5 (None if not on a wall stratum sheet)."""
    g = walls(th, d)
    if abs(np.cos(d) - 1.0) < 1e-12:
        if g[0] > TOL and g[1] > TOL:
            return 0
        if g[0] < -TOL:
            return 1
        if g[1] < -TOL:
            return 2
        return None
    if g[0] > TOL and g[1] > TOL:
        return 3
    if g[0] < -TOL:
        return 4
    if g[1] < -TOL:
        return 5
    return None


# ---- the 32 base cells (labels per the committed data = the spec) --------
PERMS = sorted(itertools.permutations(range(3)))
PID = {p: i for i, p in enumerate(PERMS)}
TRANSP = [(1, 0, 2), (2, 1, 0), (0, 2, 1)]     # the three transpositions


def comp(p, q):
    return tuple(p[q[i]] for i in range(3))


EDGE_KEYS = []
for tr in TRANSP:
    seen_pairs = []
    for rho in PERMS:
        r2 = comp(rho, tr)
        pair = tuple(sorted([rho, r2]))
        if pair not in seen_pairs:
            seen_pairs.append(pair)
    for (a, b) in seen_pairs:
        EDGE_KEYS.append((a, tr) if comp(a, tr) == b else (b, tr))
assert len(EDGE_KEYS) == 9
EID = {k: i for i, k in enumerate(EDGE_KEYS)}
EDGE_SUPPORT = {}
for (rho, tr) in EDGE_KEYS:
    r2 = comp(rho, tr)
    EDGE_SUPPORT[frozenset([(i, rho[i]) for i in range(3)]
                            + [(i, r2[i]) for i in range(3)])] = EID[(rho, tr)]

FNAMES = ["F1{th1=0}", "F2{th1=pi/2}", "F3{th2=0}", "F4{th2=pi/2}", "F5{th3=0}",
          "F6{d0,D22}", "F7{d0,D31}", "F8{dpi,D21}", "F9{dpi,D32}"]
FZERO = [(0, 1), (0, 0), (1, 2), (2, 2), (0, 2), (1, 1), (2, 0), (1, 0), (2, 1)]
RKEYS = [("R0.def", 0.0), ("R0.bF6", 0.0), ("R0.bF7", 0.0),
         ("R1.def", np.pi), ("R1.bF8", np.pi), ("R1.bF9", np.pi)]


# the F-cell parameterisations (spec): (u,v) -> (t1,t2,t3,d).
def th2_f6(u, v):
    return np.arctan(np.cos(u) / (np.sin(u) * np.sin(v) + 1e-300))


FPMAP = [
    lambda u, v: (0.0, u, v, 0.0),
    lambda u, v: (HALFPI, u, v, 0.0),
    lambda u, v: (u, 0.0, v, 0.0),
    lambda u, v: (u, HALFPI, v, 0.0),
    lambda u, v: (u, v, 0.0, 0.0),
    lambda u, v: (u, th2_f6(u, v), v, 0.0),
    lambda u, v: (u, np.arctan(np.cos(u) * np.sin(v) / (np.sin(u) + 1e-300)), v, 0.0),
    lambda u, v: (u, np.arctan(np.sin(u) / (np.cos(u) * np.sin(v) + 1e-300)), v, np.pi),
    lambda u, v: (u, np.arctan(np.sin(u) * np.sin(v) / (np.cos(u) + 1e-300)), v, np.pi),
]
FVERIFY = {0: (0, 1), 1: (0, 0), 2: (1, 2), 3: (2, 2), 4: (0, 2),
           5: (1, 1), 6: (2, 0), 7: (1, 0), 8: (2, 1)}


def cellname(cid):
    if cid < 6:
        return "V%s" % (PERMS[cid],)
    if cid < 15:
        rho, tr = EDGE_KEYS[cid - 6]
        return "E(r%s,q%s)" % (rho, tr)
    if cid < 24:
        return FNAMES[cid - 15]
    if cid < 30:
        return RKEYS[cid - 24][0]
    return ["s+", "s-"][cid - 30]


# ---- fresh D-magnitude classifier ----------------------------------------
def classify(D):
    """(kind, index) from the D-magnitude pattern; None if 9-support."""
    zeros = [(i, k) for i in range(3) for k in range(3) if D[i, k] < 1e-7]
    if len(zeros) == 1:
        return ("F", FZERO.index(zeros[0]))
    supp = frozenset((i, k) for i in range(3) for k in range(3) if D[i, k] >= 1e-7)
    if supp in EDGE_SUPPORT:
        return ("E", EDGE_SUPPORT[supp])
    for vi, p in enumerate(PERMS):
        if supp == frozenset((i, p[i]) for i in range(3)):
            return ("V", vi)
    return None


def edge_t(ei, th, d=0.0):
    """the varying D-entry of the edge-cell (its + direction is t: 0 -> 1)."""
    rho, tr = EDGE_KEYS[ei]
    r2 = comp(rho, tr)
    D = Dmat(V3(th[0], th[1], th[2], d))
    for i in range(3):
        if rho[i] != r2[i]:
            return float(D[i, r2[i]])
    raise AssertionError


# ----------------------------------------------------------------------------
hdr("PART 0: geometry sanity (fresh) -- F-parameterisations verified")
for fi in range(9):
    bad = 0
    for (u, v) in [(0.31, 0.42), (0.83, 0.21), (0.5, 0.77), (1.2, 0.9)]:
        p = FPMAP[fi](u, v)
        D = Dmat(V3(p[0], p[1], p[2], p[3]))
        z = [(i, k) for i in range(3) for k in range(3) if D[i, k] < 1e-9]
        if z != [FVERIFY[fi]]:
            bad += 1
    assert bad == 0, "FPMAP[%d] zero-pattern mismatch" % fi
# unitarity spot check
for _ in range(5):
    th = RNG.uniform(0.05, HALFPI - 0.05, 3)
    d = RNG.uniform(0.05, 2 * np.pi - 0.05)
    U = V3(th[0], th[1], th[2], d)
    assert np.max(np.abs(U @ U.conj().T - np.eye(3))) < 1e-12
print("V3 unitary; FPMAP zero-patterns exact (9/9); wall equations re-derived: OK")
tick("part 0 done")

# ----------------------------------------------------------------------------
hdr("PART 1: d(E) (fresh endpoint algebra)")
D_EDGE = []
for (rho, tr) in EDGE_KEYS:
    D_EDGE.append({PID[comp(rho, tr)]: 1, PID[rho]: -1})
print("d(E_i) = +V(rho.q) - V(rho): all 9 pinned (algebra)")
tick("part 1 done")

# ----------------------------------------------------------------------------
hdr("PART 2: d(F) (fresh dense-sampling boundary tracer)")


def side_defs():
    """CCW sides of the (u,v) square: (name, point(s), traversal sign)."""
    return [
        ("bottom", lambda s: (s, 0.0), +1),
        ("right",  lambda s: (HALFPI, s), +1),
        ("top",    lambda s: (s, HALFPI), -1),
        ("left",   lambda s: (0.0, s), -1),
    ]


CORNER_ORDER = ["left", "bottom", "right", "top"]   # CCW arrival order at (0,0),(0,0)... per-corner resolved below


def trace_F(fi):
    """d(F) by tracing the CCW boundary of the (u,v) parameter square.
    Sides: label by dense support sampling; degree from the endpoint jump of
    the edge parameter t. Corners (all four, mixed and pure alike): a corner
    BLOWS UP onto the cube edge {(t1,t3)=(u0,v0), t2 in (in,out)} iff the
    two adjacent sides disagree on theta2 there. Returns {edge_cell: coeff}.
    """
    pmap = FPMAP[fi]
    terms = {}

    def theta2_at(u, v):
        return pmap(u, v)[1]

    # ---- sides ----
    side_label = {}
    side_th2 = {}
    for (nm, f, dr) in side_defs():
        labs = set()
        for s in np.linspace(0.06, HALFPI - 0.06, 9):
            p = pmap(*f(s))
            D = Dmat(V3(p[0], p[1], p[2], p[3]))
            c = classify(D)
            labs.add(c)
        assert len(labs) == 1, "F%d side %s labels %s" % (fi, nm, labs)
        lab = labs.pop()
        side_label[nm] = lab
        # theta2 near both ends (for corner blowup detection)
        side_th2[(nm, 0)] = theta2_at(*f(0.02 * HALFPI))
        side_th2[(nm, 1)] = theta2_at(*f(0.98 * HALFPI))
        if lab is None or lab[0] != "E":
            continue          # vertex / crushed side: no edge term
        ei = lab[1]
        # endpoints of the side in (u,v): (0,H) or (H,0) depending on dr
        if dr > 0:
            p0, p1 = pmap(*f(0.0)), pmap(*f(HALFPI))
        else:
            p0, p1 = pmap(*f(HALFPI)), pmap(*f(0.0))
        t0 = edge_t(ei, np.array([p0[0], p0[1], p0[2]]), p0[3])
        t1 = edge_t(ei, np.array([p1[0], p1[1], p1[2]]), p1[3])
        # the traversal degree in the edge-cell: +1 iff the varying entry t
        # INCREASES along the traversal (p0 = traversal start, p1 = its end)
        deg = t1 - t0
        assert abs(abs(deg) - 1.0) < 1e-9, "F%d side %s degree %.6f" % (fi, nm, deg)
        cid = 6 + ei
        terms[cid] = terms.get(cid, 0) + int(round(deg))
    # ---- corners (all four) ----
    # CCW corner structure: (corner (u0,v0), incoming side, outgoing side).
    # theta2 at the corner ALONG a side = pmap at a point epsilon-inside
    # that side at the corner (the parameterisation limits differ per side).
    NEAR = {
        ("bottom", (0.0, 0.0)): (0.002, 0.0),
        ("bottom", (HALFPI, 0.0)): (HALFPI - 0.002, 0.0),
        ("right", (HALFPI, 0.0)): (HALFPI, 0.002),
        ("right", (HALFPI, HALFPI)): (HALFPI, HALFPI - 0.002),
        ("top", (HALFPI, HALFPI)): (HALFPI - 0.002, HALFPI),
        ("top", (0.0, HALFPI)): (0.002, HALFPI),
        ("left", (0.0, HALFPI)): (0.0, HALFPI - 0.002),
        ("left", (0.0, 0.0)): (0.0, 0.002),
    }
    corners = [
        ((0.0, 0.0), "left", "bottom"),
        ((HALFPI, 0.0), "bottom", "right"),
        ((HALFPI, HALFPI), "right", "top"),
        ((0.0, HALFPI), "top", "left"),
    ]
    dF = pmap(0.3, 0.3)[3]
    for (cu, nin, nout) in corners:
        th2_in = pmap(*NEAR[(nin, cu)])[1]
        th2_out = pmap(*NEAR[(nout, cu)])[1]
        if abs(th2_in - th2_out) < 0.1:
            continue          # no blowup: corner maps to a single point
        # snap the one-sided limits to the exact cube-edge endpoints
        def snap(x):
            if abs(x) < 0.1:
                return 0.0
            if abs(x - HALFPI) < 0.1:
                return HALFPI
            raise AssertionError("blowup theta2 limit %.4f not 0/pi/2" % x)
        th2_in, th2_out = snap(th2_in), snap(th2_out)
        u0, v0 = cu
        # blowup edge: (t1,t3) = (u0,v0), t2 from th2_in to th2_out
        thm = 0.5 * (th2_in + th2_out)
        Dm = Dmat(V3(u0, thm, v0, dF))
        cm = classify(Dm)
        assert cm is not None and cm[0] == "E", \
            "F%d corner %s blowup label %s" % (fi, cu, cm)
        ei = cm[1]
        t_in = edge_t(ei, np.array([u0, th2_in, v0]), dF)
        t_out = edge_t(ei, np.array([u0, th2_out, v0]), dF)
        deg = t_out - t_in
        assert abs(abs(deg) - 1.0) < 1e-6, "blowup degree %s" % deg
        cid = 6 + ei
        terms[cid] = terms.get(cid, 0) + int(round(deg))
        print("  F%d corner %s BLOWS UP onto %s (th2 %.2f -> %.2f, coeff %+d)"
              % (fi, (round(u0, 2), round(v0, 2)), cellname(cid),
                 th2_in, th2_out, int(round(deg))))
    return {k: v for k, v in terms.items() if v != 0}


D_FACE = []
for fi in range(9):
    tr = trace_F(fi)
    D_FACE.append(tr)
    s = " + ".join("%+d*%s" % (v, cellname(k)) for k, v in sorted(tr.items()))
    print("  d(%-13s) = %s" % (FNAMES[fi], s if s else "0"))
tick("part 2 done")

# ----------------------------------------------------------------------------
hdr("PART 3: d(R) (fresh exact region-boundary analysis + outward normals)")
# Region boundaries: the wall surfaces g=0 (mixed F's) and the theta-cube
# faces that belong to the region's closure.  Face membership decided
# EXACTLY from the wall signs on the face (wall signs are constant on each
# open cube face): a face theta_idx = val belongs to region R's boundary iff
# the face's interior points satisfy R's defining inequalities.
FACES = [
    (0, 0.0, (1, 2), 15),    # theta1=0    -> F1
    (0, HALFPI, (1, 2), 16),  # theta1=pi/2 -> F2
    (1, 0.0, (0, 2), 17),    # theta2=0    -> F3
    (1, HALFPI, (0, 2), 18),  # theta2=pi/2 -> F4
    (2, 0.0, (0, 1), 19),    # theta3=0    -> F5
]


def face_in_region(face, rid):
    """EXACT: is the open face in region rid's closure? (signs of the g's on
    the face are constant; decided at one interior point + verified at 5)."""
    idx, val, frees, fcid = face
    d = RKEYS[rid][1]
    pts = []
    for (a, b) in [(0.3, 0.4), (0.7, 0.2), (0.2, 0.75), (0.55, 0.55), (0.8, 0.65)]:
        th = [0.0, 0.0, 0.0]
        th[frees[0]], th[frees[1]] = a, b
        th[idx] = val
        pts.append(np.array(th))
    ids = set(region_of(p, d) for p in pts)
    assert len(ids) == 1, "region id not constant on face %s: %s" % (fcid, ids)
    return ids.pop() == rid


def face_sign_pure(face, rid):
    """outward-normal determinant rule:  eps = det[t_u, t_v, n_out] with the
    ambient orientation (theta1, theta2, theta3)."""
    idx, val, frees, fcid = face
    tu = np.zeros(3)
    tu[frees[0]] = 1.0                      # (u,v) = (theta_f0, theta_f1)
    tv = np.zeros(3)
    tv[frees[1]] = 1.0
    n = np.zeros(3)
    n[idx] = -1.0 if val == 0.0 else +1.0   # outward from the theta-cube
    return int(np.sign(np.linalg.det(np.array([tu, tv, n]))))


def wall_grad(rid, fi, th):
    """numeric gradient of the wall equation of the mixed F fi at th."""
    h = 1e-6
    g = []
    for i in range(3):
        tp = np.array(th, dtype=float)
        tp[i] = min(tp[i] + h, HALFPI)
        tm = np.array(th, dtype=float)
        tm[i] = max(tp[i] - h, 0.0)
        gp = walls(tp, RKEYS[rid][1])
        gm = walls(tm, RKEYS[rid][1])
        kk = fi - 5 if RKEYS[rid][1] == 0.0 else fi - 7
        g.append((gp[kk] - gm[kk]) / (tp[i] - tm[i]))
    return np.array(g)


def mixed_sign(rid, fi):
    """sign of the mixed face F fi in d(R_rid), IF the wall is adjacent to
    the region; else None.  Adjacency: perturb an F-locus point in +-theta2
    and test region membership (the two sides of the wall are the two
    adjacent regions).  Sign: the outward-normal determinant rule
    det[t_u, t_v, n_out] with n_out = -sign(g_R) * grad(wall eqn).
    """
    d = RKEYS[rid][1]
    kk = fi - 5 if d == 0.0 else fi - 7
    for (u, v) in [(0.35, 0.55), (0.62, 0.30), (0.48, 0.78), (0.80, 0.42),
                   (0.28, 0.66), (0.55, 0.18)]:
        p = FPMAP[fi](u, v)
        th = np.array([p[0], p[1], p[2]])
        for eps in (1e-3, -1e-3):
            thp = th.copy()
            thp[1] += eps
            if region_of(thp, d) != rid:
                continue
            # adjacent: g on the rid side has sign sign(g_in)
            g_in = walls(thp, d)[kk]
            if abs(g_in) < 1e-9:
                continue
            gr = wall_grad(rid, fi, th)
            gn = np.linalg.norm(gr)
            if gn < 1e-9:
                continue
            n_out = -np.sign(g_in) * gr / gn
            # tangents of the F-parameterisation at (u, v)
            h = 1e-5
            pu = FPMAP[fi](min(u + h, HALFPI - 1e-9), v)
            pv = FPMAP[fi](u, min(v + h, HALFPI - 1e-9))
            du = max(pu[0] - p[0], 1e-12)
            dv = max(pv[2] - p[2], 1e-12)
            tu = np.array([(pu[j] - p[j]) / du for j in range(3)])
            tv = np.array([(pv[j] - p[j]) / dv for j in range(3)])
            det = np.linalg.det(np.array([tu, tv, n_out]))
            if abs(det) > 0.15:
                return int(np.sign(det)), th
    return None, None


D_REG = []
for rid in range(6):
    terms = {}
    for face in FACES:
        if face_in_region(face, rid):
            s = face_sign_pure(face, rid)
            terms[face[3]] = terms.get(face[3], 0) + s
    # mixed walls: F is on R's boundary iff the +-theta2 perturbations of an
    # F-locus point land in R (the two sides of the wall are the two regions)
    for fi in (5, 6, 7, 8):
        dR = RKEYS[rid][1]
        dF = 0.0 if fi in (5, 6) else np.pi
        if abs(dR - dF) > 1e-9:
            continue
        s, thw = mixed_sign(rid, fi)
        if s is None:
            continue          # wall not adjacent to this region
        terms[15 + fi] = terms.get(15 + fi, 0) + s
    D_REG.append({k: v for k, v in terms.items() if v != 0})
    s = " + ".join("%+d*%s" % (v, cellname(k)) for k, v in sorted(D_REG[-1].items()))
    print("  d(%-8s) = %s" % (RKEYS[rid][0], s))
tick("part 3 done")

# ----------------------------------------------------------------------------
hdr("PART 4: d(s) (fresh delta-interval rule)")
# s+ = {delta in (0,pi)}: top face delta=pi (+ orientation), bottom delta=0 (-).
# s- = {delta in (pi,2pi)}: top face delta=2pi==0 (+), bottom delta=pi (-).
D_SHEET = [
    {24 + r: 1 for r in (3, 4, 5)},
    {24 + r: 1 for r in (0, 1, 2)},
]
D_SHEET[0].update({24 + r: -1 for r in (0, 1, 2)})
D_SHEET[1].update({24 + r: -1 for r in (3, 4, 5)})
print("d(s+) = +[R1.def+R1.bF8+R1.bF9] - [R0.def+R0.bF6+R0.bF7]")
print("d(s-) = +[R0.*] - [R1.*]   (delta-interval boundary rule, fresh)")
tick("part 4 done")

# ----------------------------------------------------------------------------
hdr("PART 5: CMAP (fresh: V/E/F by algebra; R/s by sampling + normaliser)")


def normalise(U):
    """fresh inverse map D -> (t1,t2,t3,d) of the CKM chart (or None).
    c3^2 = 1 - D[0,2]; c1^2 = D[0,0]/c3^2; c2^2 = D[2,2]/c3^2;
    cos d = (D[1,0] - s1^2 c2^2 - c1^2 s2^2 s3^2)/(2 s1 c1 c2 s2 s3),
    sign of d by the J-invariant Im(U00 U11 ubar(01) ubar(10))."""
    D = np.abs(U) ** 2
    s3sq = D[0, 2]
    c3sq = 1.0 - s3sq
    if c3sq <= 1e-12 or s3sq <= 1e-12 or D[0, 0] <= 1e-12 or D[2, 2] <= 1e-12:
        return None
    t1 = np.arccos(np.sqrt(min(max(D[0, 0] / c3sq, 0.0), 1.0)))
    t2 = np.arccos(np.sqrt(min(max(D[2, 2] / c3sq, 0.0), 1.0)))
    t3 = np.arccos(np.sqrt(c3sq))
    s1, c1 = np.sin(t1), np.cos(t1)
    s2, c2 = np.sin(t2), np.cos(t2)
    s3 = np.sin(t3)
    den = 2.0 * s1 * c2 * c1 * s2 * s3
    if den <= 1e-13:
        return None
    cd = (D[1, 0] - s1 ** 2 * c2 ** 2 - c1 ** 2 * s2 ** 2 * s3 ** 2) / den
    cd = float(min(max(cd, -1.0), 1.0))
    JU = float(np.imag(U[0, 0] * U[1, 1] * np.conj(U[0, 1]) * np.conj(U[1, 0])))
    for dd in ((0.0,) if abs(cd - 1) < 1e-9 else
               ((np.pi,) if abs(cd + 1) < 1e-9 else (np.arccos(cd), -np.arccos(cd)))):
        V = V3(t1, t2, t3, dd)
        if np.max(np.abs(np.abs(V) ** 2 - D)) < 1e-9:
            JV = float(np.imag(V[0, 0] * V[1, 1] * np.conj(V[0, 1]) * np.conj(V[1, 0])))
            if abs(JV - JU) < 1e-8:
                return (t1, t2, t3, dd)
    return None


CMAP = {}
for cid in range(6):                       # vertices: rho -> SIG o rho
    CMAP[cid] = PID[comp(SIG, PERMS[cid])]
for cid in range(6, 15):                   # edges: (rho,pi) -> (SIG o rho, pi)
    rho, tr = EDGE_KEYS[cid - 6]
    r1 = comp(SIG, rho)
    img = None
    for kk in ((r1, tr), (comp(r1, tr), tr)):
        if kk in EID:
            img = EID[kk]
            break
    CMAP[cid] = 6 + img
for cid in range(15, 24):                  # F: zero (a,b) -> (a, SIG[b])
    z = FZERO[cid - 15]
    zi = (z[0], SIG[z[1]])
    CMAP[cid] = 15 + FZERO.index(zi)
# R and sheets: sampled through the fresh normaliser
def sample_point(cid):
    for _ in range(20000):
        th = RNG.uniform(0.05, HALFPI - 0.05, 3)
        if 24 <= cid < 30:
            d = RKEYS[cid - 24][1]
            if region_of(th, d) != cid - 24:
                continue
            return (th, d)
        d = RNG.uniform(0.05, 2 * np.pi - 0.05)
        if cid == 30 and np.sin(d) <= 0.08:
            continue
        if cid == 31 and np.sin(d) >= -0.08:
            continue
        return (th, d)
    return None


def classify_full(th, d):
    """the full 32-cell label of V3(th,d): the wall strata only exist at
    delta = 0 or pi; interior delta is the two sheets."""
    cd = np.cos(d)
    if abs(cd - 1.0) < 1e-9 or abs(cd + 1.0) < 1e-9:
        r = region_of(th, d)
        return None if r is None else 24 + r
    return 30 + (0 if np.sin(d) > 0 else 1)


for cid in range(24, 32):
    imgs = set()
    for _ in range(8):
        (th, d) = sample_point(cid)
        nf = normalise(shift_cols(V3(th[0], th[1], th[2], d)))
        if nf is None:
            continue
        imgs.add(classify_full(np.array(nf[:3]), nf[3]))
    assert len(imgs) == 1, "%s c-image not unique: %s" % (cellname(cid), imgs)
    CMAP[cid] = imgs.pop()
    print("  %-10s -> %-10s (sampled, fresh normaliser)" % (cellname(cid), cellname(CMAP[cid])))
for cid in range(32):
    assert CMAP[CMAP[CMAP[cid]]] == cid, "c^3 != id at %s" % cellname(cid)
print("c^3 = id on all 32 cells; fixed base cells: %s"
      % [cellname(c) for c in range(32) if CMAP[c] == c])
tick("part 5 done")

# ----------------------------------------------------------------------------
hdr("PART 6: G0 -- base d^2=0 + base homology via EXACT INTEGER SNF (sympy)")


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


BDIM = {}
for c in range(32):
    BDIM[c] = 0 if c < 6 else (1 if c < 15 else (2 if c < 24 else (3 if c < 30 else 4)))

BASE_DB = {}
for cid in range(32):
    if BDIM[cid] == 0:
        continue
    col = {}
    for tgt, co in bcol(cid).items():
        assert BDIM[tgt] == BDIM[cid] - 1, \
            "degree mismatch %s -> %s" % (cellname(cid), cellname(tgt))
        col[tgt] = co
    BASE_DB[cid] = col

resid = 0
for cid in range(32):
    if BDIM[cid] < 2:
        continue
    acc = {}
    for tgt, co in BASE_DB[cid].items():
        for tgt2, co2 in BASE_DB.get(tgt, {}).items():
            acc[tgt2] = acc.get(tgt2, 0) + co * co2
    for v in acc.values():
        if v != 0:
            resid += 1
            print("  d^2 residual at %s: %d" % (cellname(cid), v))
assert resid == 0, "BASE d^2=0 FAILED (%d residuals)" % resid
print("G0-a: base d^2 = 0 exactly: PASS")

# exact integer homology of the base complex via sympy SNF
CB = [6, 9, 9, 6, 2]
dense = {}
for k in range(1, 5):
    rows = [c for c in range(32) if BDIM[c] == k - 1]
    cols = [c for c in range(32) if BDIM[c] == k]
    M = Matrix.zeros(len(rows), len(cols))
    for j, c in enumerate(cols):
        for r, co in BASE_DB[c].items():
            M[rows.index(r), j] = co
    dense[k] = M
# H_k = ker d_k / im d_{k+1}: SNF of each d_k gives rank; torsion via the
# SNF of the stacked map.  Simplest exact route: homology via SNF of the
# block matrix [d_k | d_{k+1}] per degree (standard chain-complex SNF).
def base_homology():
    beta = [0] * 5
    tor = [0] * 5
    ranks = {k: dense[k].rank() for k in range(1, 5)}
    for k in range(5):
        rk_in = ranks.get(k, 0)          # rank d_k (into C_{k-1})
        rk_out = ranks.get(k + 1, 0)     # rank d_{k+1} (out of C_k)
        beta[k] = CB[k] - rk_in - rk_out
    # torsion: SNF diagonal of the map d_{k+1} restricted mod the cycles --
    # exact: torsion H_k = elementary divisors of [d_{k+1}] beyond rank, i.e.
    # SNF of d_{k+1} gives the image; torsion = cycles not hit.  Compute via
    # the SNF of d_{k+1} directly: # of non-unit nonzero invariant factors
    # that are NOT forced by... instead use the standard: H_k = ker/im; the
    # torsion subgroup order = |ker d_k| / |im d_{k+1} embed in ker| -- for
    # the certification it suffices that beta = (1,0,0,0,1) and the SNF of
    # each d_k has NO invariant factor > 1 (all torsion-free).
    for k in range(1, 5):
        S = dense[k].tolist()
        from sympy.matrices.normalforms import smith_normal_form
        snf = smith_normal_form(Matrix(S))
        diag = [abs(snf[i, i]) for i in range(min(snf.rows, snf.cols))]
        nontrivial = [d for d in diag if d > 1]
        if nontrivial:
            print("  NOTE d%d SNF non-unit invariants: %s" % (k, nontrivial))
            tor[k - 1] = len(nontrivial)
    return beta, tor


beta, tor = base_homology()
chi = sum((-1) ** k * CB[k] for k in range(5))
print("base Betti (EXACT integer SNF): %s   chi=%+d" % (beta, chi))
assert beta == [1, 0, 0, 0, 1], "base homology is not S^4: %s" % beta
assert all(t == 0 for t in tor), "base torsion found: %s" % tor
print("G0-b: base homology = (Z,0,0,0,Z) torsion-free (sympy SNF): PASS")
tick("part 6 done")

# ----------------------------------------------------------------------------
hdr("PART 7: comparison against the committed wave13c_base_data.json")
try:
    with open("wave13c_base_data.json") as f:
        ORIG = json.load(f)
except FileNotFoundError:
    ORIG = None
    print("original base data not found -- comparison SKIPPED")

if ORIG is not None:
    o_edge = [{int(k): v for k, v in d.items()} for d in ORIG["D_EDGE"]]
    o_face = [{int(k): v for k, v in d.items()} for d in ORIG["D_FACE"]]
    o_reg = [{int(k): v for k, v in d.items()} for d in ORIG["D_REG"]]
    o_sheet = [{int(k): v for k, v in d.items()} for d in ORIG["D_SHEET"]]
    o_cmap = {int(k): v[0] for k, v in ORIG["CMAP"].items()}
    o_keys = [tuple(tuple(k) for k in e) for e in ORIG["EDGE_KEYS"]]

    def cmp(name, mine, theirs):
        if mine == theirs:
            print("  %-8s: MATCH (all %d entries)" % (name, len(mine)))
            return True
        print("  %-8s: MISMATCH" % name)
        for i, (a, b) in enumerate(zip(mine, theirs)):
            if a != b:
                print("    [%d] fresh %s vs original %s" % (i, a, b))
        return False

    allmatch = True
    allmatch &= cmp("EDGE_KEYS", [tuple(tuple(x) for x in ((list(a), list(b)) if False else (a, b))) for (a, b) in EDGE_KEYS], o_keys)
    allmatch &= cmp("D_EDGE", D_EDGE, o_edge)
    allmatch &= cmp("D_FACE", D_FACE, o_face)
    allmatch &= cmp("D_REG", D_REG, o_reg)
    allmatch &= cmp("D_SHEET", D_SHEET, o_sheet)
    allmatch &= cmp("CMAP", CMAP, o_cmap)
    print("\nFIELD-BY-FIELD BASE COMPARISON: %s"
          % ("ALL MATCH -- the two independent derivations agree" if allmatch
             else "DISCREPANCIES FOUND (inspect above)"))

# ----------------------------------------------------------------------------
with open("w28_base_data.json", "w") as f:
    json.dump({
        "EDGE_KEYS": [[list(a), list(b)] for (a, b) in EDGE_KEYS],
        "D_EDGE": [{str(k): v for k, v in d.items()} for d in D_EDGE],
        "D_FACE": [{str(k): v for k, v in d.items()} for d in D_FACE],
        "D_REG": [{str(k): v for k, v in d.items()} for d in D_REG],
        "D_SHEET": [{str(k): v for k, v in d.items()} for d in D_SHEET],
        "CMAP": {str(k): v for k, v in CMAP.items()},
    }, f, indent=1)
print("fresh base data -> w28_base_data.json")
hdr("WAVE 28 MODULE 1 COMPLETE (base re-implementation)")
tick("module 1 complete")
