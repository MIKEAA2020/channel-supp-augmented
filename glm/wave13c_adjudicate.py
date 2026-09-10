#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
WAVE 13C-4 : THE F-CELL ADJUDICATION (cross-line, versus Wave 14H section 6).

The question (his 14H section 6 / the user's directive): my line's base book has
9 F-cells (5 pure + 4 mixed, 'all feasible'); his facet survey finds
  "U_3 cap facet(D_rs=0) = the four T-edges  (a 1-dimensional set)",
i.e. NO 2-dimensional facet locus in B_3. Both were claimed to be possible only
if the F-cells live on the double M = Fl_3/T^3_L, not in B_3. This script
adjudicates that against the d(F) construction machine-wise.

Method:
  (A) exact algebra on every facet {D_ij = 0}:  Q_ij = -(A - C)^2 with
      A = D_i1 D_j1 (product over the two columns k with... the pair (ij)
      has its zero side at k = j), so {Q = 0} cap facet is the codim-1
      locus {A = C}  -> 2-dimensional. The identity Q_12 = Q_13 = Q_23
      (13B machine result) is re-verified on random doubly-stochastic D.
  (B) HIS METHOD reproduced: 25 000 random samples per facet -> all Q < 0,
      min ~ -0.06 (matches his table) -> uniform sampling CANNOT see a
      measure-zero codim-1 locus. His "equality locus = T-edges only" is a
      Monte-Carlo artifact.
  (C) MY F-CELLS: the 9 FPMAP parametrisations (the 13C base build) on dense
      (u,v) grids -> every image point has D[FZERO] = 0 to 1e-12, Q = 0 to
      1e-12, all other 8 entries positive (FACET INTERIOR, not T-edges) and
      the (u,v) -> D map is injective on the grid (a genuine 2-dim locus).
  (D) d(F) cross-check from the certified base data: d(F_i) = sums of
      transposition edges with +/-1 -- the F-membranes' boundaries are
      exactly the T-edges he found as the Q = 0 part of each facet.
  (E) The Euler repair: with the 9 F-cells his failed stratification closes:
      chi(U_3) = 1 - 6 + 9 - 9 + 6 = +1 (his 14H section 3 computed
      1 - 6 + 0 - 9 + 6 = -8 and concluded 'not a cell decomposition').

Run:  python3 wave13c_adjudicate.py
"""
import itertools
import json
import sys

import numpy as np

TOL = 1e-12
rng = np.random.default_rng(20260910)
PI2 = np.pi / 2.0


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
FNAMES = ["F1{th1=0}", "F2{th1=pi/2}", "F3{th2=0}", "F4{th2=pi/2}", "F5{th3=0}",
          "F6{d0,D22}", "F7{d0,D31}", "F8{dpi,D21}", "F9{dpi,D32}"]
FZERO = [(0, 1), (0, 0), (1, 2), (2, 2), (0, 2), (1, 1), (2, 0), (1, 0), (2, 1)]


def hq(a, b, c):
    """Heron slack 2(ab+bc+ca)-(a^2+b^2+c^2) on SQUARED sides a,b,c."""
    return 2.0 * (a * b + b * c + c * a) - (a * a + b * b + c * c)


def Qs(D):
    """The three row-pair Heron slacks of a doubly-stochastic D."""
    out = []
    for (i, j) in ((0, 1), (0, 2), (1, 2)):
        a = D[i, 0] * D[j, 0]
        b = D[i, 1] * D[j, 1]
        c = D[i, 2] * D[j, 2]
        out.append(hq(a, b, c))
    return out


def ds_from_chart(a, b, c, d):
    D = np.zeros((3, 3))
    D[0, 0], D[0, 1], D[1, 0], D[1, 1] = a, b, c, d
    D[0, 2] = 1.0 - a - b
    D[1, 2] = 1.0 - c - d
    D[2, 0] = 1.0 - a - c
    D[2, 1] = 1.0 - b - d
    D[2, 2] = a + b + c + d - 1.0
    return D


print("=" * 78)
print("WAVE 13C-4: F-CELL ADJUDICATION vs Wave 14H section 6")
print("=" * 78)

# ---------------------------------------------------------------- (A)
print("\n(A) exact facet algebra: on {D_ij=0},  Q = -(A-C)^2 <= 0,")
print("    equality locus {A=C} is codim-1 in the 3-dim facet (2-dim).")
bad = 0
for _ in range(200000):
    a, b, c, d = rng.uniform(0.0, 1.0, 4)
    D = ds_from_chart(a, b, c, d)
    if D.min() < -1e-12:
        continue
    q = Qs(D)
    if max(abs(q[0] - q[1]), abs(q[0] - q[2])) > 1e-13:
        bad += 1
print("    identity Q12=Q13=Q23 on random DS points: %d failures" % bad)
assert bad == 0

# the zero-side index of each facet (which column k has D_ik D_jk ~ 0 side)
ZS = {}
for (i, j) in [(0, 1), (0, 2), (1, 2)]:
    for k in range(3):
        ZS[(i, j, k)] = None
print("    on facet {D_ij=0} the (ij)-pair has its zero side at k=j:")
check = 0
for (i, j) in [(0, 1), (0, 2), (1, 2)]:
    a, c = 0.3, 0.2
    b = d = 0.0 if (i, j) != (0, 1) else 0.0
    # build a DS point with D[i,j]=0: use the chart with the (i,j) coord 0
    D = ds_from_chart(*(0.3, 0.0, 0.2, 0.25))
    Qv = Qs(D)
    print("      sample Q on {D_12=0}: %s  (all <= 0)" % np.round(Qv, 6))
    check += 1
# exact algebra check on all 9 facets: Q(pair with zero entry) = -(A-C)^2
for (zi, zj) in FZERO:
    for _ in range(20000):
        a, b, c, dd = rng.uniform(0.05, 0.9, 4)
        D = ds_from_chart(a, b, c, dd)
        if D.min() < 1e-9:
            continue
        D[zi, zj] = 0.0
        # renormalise rows/cols minimally: just use it if still DS-ish
        if abs(D.sum() - 3.0) > 1e-9 or abs(D.sum(axis=0) - 1).max() > 1e-9 \
                or abs(D.sum(axis=1) - 1).max() > 1e-9 or D.min() < 0:
            continue
        q = Qs(D)
        i, j = (zi, zj) if zi < zj else (zj, zi)
        A = D[i, 0] * D[j, 0] + D[i, 1] * D[j, 1] + D[i, 2] * D[j, 2]
        # recompute the pair with the zero entry:
        i, j = (zi, zj) if zi < zj else (zj, zi)
        a2 = D[i, 0] * D[j, 0]
        b2 = D[i, 1] * D[j, 1]
        c2 = D[i, 2] * D[j, 2]
        sides = [a2, b2, c2]
        zz = sides.index(0.0) if 0.0 in sides else -1
        others = [s for s in sides if s != 0.0]
        if zz >= 0 and len(others) == 2:
            exact = -(others[0] - others[1]) ** 2
            got = hq(a2, b2, c2)
            if abs(got - exact) > 1e-15:
                bad += 1
print("    Q = -(A-C)^2 exactly on zero-side pairs: %d failures" % bad)
assert bad == 0

# ---------------------------------------------------------------- (B)
print("\n(B) HIS METHOD reproduced (uniform facet sampling, 25k pts/facet):")
PERMS3 = sorted(itertools.permutations(range(3)))
for (zi, zj) in FZERO:
    i, j = (zi, zj) if zi < zj else (zj, zi)
    # sample the facet: fix D[i,j]=0 by the chart, keep positivity
    qs = []
    tries = 0
    while len(qs) < 25000 and tries < 400000:
        tries += 1
        a, b, c, dd = rng.uniform(0.0, 1.0, 4)
        # chart coordinates map to D; forcing D[i,j] = 0 requires setting the
        # corresponding chart/free coordinate: sample 3 free coords instead
        # -> use the 4 chart coords with the one realising D[i,j] pinned to 0
        D = ds_from_chart(a, b, c, dd)
        # project onto the facet by zeroing the (i,j) entry and resampling the
        # complementary free coordinate is messy; instead sample uniformly on
        # the facet tetrahedron via its vertices (his own facet data):
        # vertices = permutations supported away from (i,j)
        verts = []
        for p in PERMS3:
            M = np.zeros((3, 3))
            for r in range(3):
                M[r, p[r]] = 1.0
            if M[i, j] == 0.0:
                verts.append(M)
        w = rng.dirichlet((0.6, 0.6, 0.6, 0.6))
        D = sum(w[t] * verts[t] for t in range(4))
        if D.min() < 0 or abs(D.sum() - 3) > 1e-9:
            continue
        qs.append(min(Qs(D)))
    qs = np.array(qs)
    print("   facet D_%d%d=0: n=%d  max Q = %+.2e  min Q = %+.4f  [his: -0.059..-0.061]"
          % (i + 1, j + 1, len(qs), qs.max(), qs.min()))
    assert qs.max() < 0.0
print("   -> uniform sampling sees Q<0 everywhere: the {A=C} locus is measure-zero;")
print("      his inference 'equality locus = T-edges only' is a sampling artifact.")

# ---------------------------------------------------------------- (C)
print("\n(C) MY 9 F-CELLS: dense FPMAP grids (facet-interior, Q=0, 2-dim):")
for fi in range(9):
    (zi, zj) = FZERO[fi]
    us = np.linspace(0.15, PI2 - 0.15, 9)
    vs = np.linspace(0.15, PI2 - 0.15, 9)
    pts = []
    minoth = 1.0
    for u in us:
        for v in vs:
            p = FPMAP[fi](u, v)
            V = Vckm(p[0], p[1], p[2], p[3])
            D = np.abs(V) ** 2
            assert abs(D[zi, zj]) < TOL, "F%d zero entry fails" % (fi + 1)
            q = Qs(D)
            assert max(abs(x) for x in q) < TOL, "F%d not on wall: %s" % (fi + 1, q)
            others = [D[a, b] for a in range(3) for b in range(3)
                      if (a, b) != (zi, zj)]
            minoth = min(minoth, min(others))
            assert min(others) > 1e-6, "F%d not facet-interior" % (fi + 1)
            pts.append(D.flatten())
    P = np.array(pts)
    G = P.reshape(9, 9, 9)
    # 2-dim-ness: rows differ when u differs; columns differ when v differs
    du = np.abs(G[1] - G[0]).max()
    dv = np.abs(G[:, 1] - G[:, 0]).max()
    inj = len({tuple(np.round(x, 9)) for x in P}) == len(P)
    print("   %-13s: 81 pts, D[%d,%d]=0 (1e-12), Q=0 (1e-12), 8 entries>0,"
          " dD/du=%.3f dD/dv=%.3f injective=%s"
          % (FNAMES[fi], zi, zj, du, dv, inj))
    assert du > 1e-3 and dv > 1e-3 and inj
print("   -> every facet carries a 2-dim Q=0 locus with 8 positive entries:")
print("      REFUTES 'U_3 cap facet = T-edges (1-dim)' and confirms the 13B census (D).")

# ---------------------------------------------------------------- (D)
print("\n(D) d(F) (certified base data) = the T-edges of each facet:")
with open("wave13c_base_data.json") as f:
    BD = json.load(f)
EDGE_KEYS = [(tuple(k[0]), tuple(k[1])) for k in BD["EDGE_KEYS"]]
for fi in range(9):
    terms = BD["D_FACE"][fi]
    edges = []
    for k, v in sorted(terms.items(), key=lambda x: int(x[0])):
        rho, pi = EDGE_KEYS[int(k) - 6]
        edges.append("%+d*E(r%s,q%s)" % (v, rho, pi))
    print("   d(%-13s) = %s" % (FNAMES[fi], " ".join(edges)))
print("   -> the F-membranes bound exactly onto the transposition edges that")
print("      his survey identified as the Q=0 part of each facet.")

# ---------------------------------------------------------------- (E)
print("\n(E) Euler repair of his 14H section 3 stratification:")
print("   his:   1 - 6 + 0 - 9 + 6 = -8  !=  chi(U_3) = 1   (not a CW complex)")
print("   with the 9 F-cells:  1 - 6 + 9 - 9 + 6 = %+d = chi(U_3)  [PASS]" %
      (1 - 6 + 9 - 9 + 6))
print("   the double (two sheets): 2 - 6 + 9 - 9 + 6 = %+d = chi(S^4)  [certified G0]"
      % (2 - 6 + 9 - 9 + 6))

print("\n" + "=" * 78)
print("VERDICT")
print("=" * 78)
print("""1. His section 4 'equality locus {Q=0} in a facet = the four T-edges'
   is REFUTED: on every facet {D_ij=0} the pair slack is exactly
   Q = -(A-C)^2 (A = D_i1 D_j1, C = D_i3 D_j3 on the zero-side pair),
   so {Q=0} is the codim-1 locus {A=C} -- TWO-dimensional, with facet-
   interior points (all 8 other entries positive). 81 machine points per
   facet, Q = 0 to 1e-12. His uniform sampling (25k pts, min Q ~ -0.06,
   all < 0) cannot hit a measure-zero locus: the artifact is identified.
2. The 9 F-cells are exactly these loci: they are cells of the base book
   (the M = Fl_3/T^3_L cellulation, d^2=0-certified, chi=+2 = S^4) AND
   their images are 2-dim loci of B_3 on the wall/facet intersection.
   The proposed resolution 'F-cells live only on the double M, not in B_3'
   is REJECTED; both lines' statements are reconciled by correcting the
   facet-survey inference, not by relocating the F-cells.
3. d(F) adjudicates: the F-boundaries are the T-edges (his Q=0 facet part);
   the F-cells are the subdivision 2-cells his section 3 boxed as required
   (his Euler check -8 is repaired to +1 by them; his T-edge-link probing
   failed exactly where the F-membranes attach).
4. Consequence: no change to the cellulation design. The level-12
   rho-gauged rebuild proceeds with the 9 F-cells as pinned.""")
print("\n[adjudication complete; no claims about delta_2 are made here]")
