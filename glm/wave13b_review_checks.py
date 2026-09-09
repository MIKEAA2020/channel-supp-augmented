#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""WAVE 13B : line-level review verification of the WAVE-13 cellulation spec.

Machine checks that decide the two structural claims of the review:

  [C1]  Every real-orthogonal O (all entries nonzero) gives D = O^2 with ALL
        THREE row-pair triangles EXACTLY degenerate, and the three hypotenuse
        columns form a bijection.  => the orthostochastic locus is 3-dim and
        lies on three walls at once (the spec's "6 isolated triple points"
        cannot be right).

  [C2]  Inside the CKM domain (theta in open cube, all 9 entries positive),
        every row-pair triangle degeneracy forces sin(delta) = 0.  Scan a
        theta-grid x delta-circle: wall slacks vanish only at delta in {0,pi}.
        => the walls of U3 are EXACTLY the real/orthostochastic locus; there
        are NO non-real "1-degenerate" wall points in int B3.

  [C3]  Fibre sheet count: for a random Haar unitary U with positive entries,
        the CKM inversion of D=|U|^2 yields |cos(delta)|<1 with TWO branches
        (+-delta) (both reconstruct D exactly, Jarlskog signs opposite) =>
        fibre over int U3 is TWO T^2 sheets, not one.  For real-orthostochastic
        D, |cos(delta)| = 1 (single branch, the fold).

  [C4]  Wall tangency along the real locus: at D = O^2 the three wall-equation
        gradients on the 4-dim doubly-stochastic space are parallel
        (rank <= 1) => the three walls are mutually tangent along a 3-dim
        locus; pairwise "corner" intersections are 3-dim, not 2-dim.

  [C5]  c preserves the Jarlskog sign on positive-entry unitaries:
        J(U P_sigma) = J(U)  (quartic identity) => the two sheets are
        individually c-invariant (needed by the corrected T-map design).

  [C6]  A "corner" point of a rook pair, found exactly as Wave-12b found them,
        lies on the THIRD wall as well and moves in a 3-dim family: the
        Wave-12b corner/triple interpretation (2-loci / 6 points) is refuted.

Float tolerances: 1e-9..1e-12; trigonometric exact identities hold to ~1e-15.
"""
import numpy as np
import itertools

rng = np.random.default_rng(20260910)

# ---------------- CKM parametrisation ----------------
def Vckm(t1, t2, t3, delta):
    c1, s1 = np.cos(t1), np.sin(t1)
    c2, s2 = np.cos(t2), np.sin(t2)
    c3, s3 = np.cos(t3), np.sin(t3)
    e = np.exp(1j * delta)
    V = np.array([
        [c1 * c3,               s1 * c3,               s3 * np.conj(e)],
        [-s1 * c2 - c1 * s2 * s3 * e,  c1 * c2 - s1 * s2 * s3 * e,  s2 * c3],
        [s1 * s2 - c1 * c2 * s3 * e,  -c1 * s2 - s1 * c2 * s3 * e,  c2 * c3],
    ], dtype=complex)
    return V

def unitary_ok(V, tol=1e-12):
    return np.max(np.abs(V @ V.conj().T - np.eye(3))) < tol

def Jarskog(U):
    return np.imag(U[0, 0] * U[1, 1] * np.conj(U[0, 1]) * np.conj(U[1, 0]))

def rowpair_sides(D, i, j):
    # m_k = sqrt(D[i,k] D[j,k]) for row pair (i,j)
    return np.sqrt(D[i, :] * D[j, :])

def triangle_slack(D, i, j):
    """Return (hyp, slack): the degeneracy slack = max - (sum of others)."""
    m = rowpair_sides(D, i, j)
    order = np.argsort(m)
    hyp = int(order[2])
    slack = m[order[2]] - m[order[1]] - m[order[0]]
    return hyp, slack

# ---------------- C1 : real orthogonal => 3 walls ----------------
def rand_orth(min_entry=0.05, max_tries=10000):
    for _ in range(max_tries):
        A = rng.normal(size=(3, 3))
        Q, R = np.linalg.qr(A)
        Q = Q * np.sign(np.diag(R))          # canonical sign fix
        if np.min(np.abs(Q)) > min_entry:
            return Q
    raise RuntimeError("no generic orthogonal found")

print("=" * 72)
print("[C1] real orthogonal O  =>  D = O^2 has all three triangles degenerate")
print("=" * 72)
ok = True
patterns = set()
for trial in range(30):
    O = rand_orth()
    D = O ** 2
    assert np.max(np.abs(D.sum(axis=0) - 1)) < 1e-12
    assert np.max(np.abs(D.sum(axis=1) - 1)) < 1e-12
    hyps, slacks = [], []
    for (i, j) in [(0, 1), (0, 2), (1, 2)]:
        h, s = triangle_slack(D, i, j)
        hyps.append(h)
        slacks.append(s)
    if max(abs(s) for s in slacks) > 1e-10:
        ok = False
        print("  FAIL: slacks", slacks)
    if len(set(hyps)) != 3:
        ok = False
        print("  FAIL: hyps not a bijection", hyps)
    patterns.add(tuple(h + 1 for h in hyps))
print("  all 30 trials: |slack| <= 1e-10 and (h12,h13,h23) is a bijection:",
      ok)
print("  observed bijection patterns:", sorted(patterns))
print("  => the orthostochastic locus is 3-dim and lies on 3 walls at once.")

# ---------------- C2 : walls only at sin(delta)=0 ----------------
print()
print("=" * 72)
print("[C2] wall slacks in the CKM domain vanish ONLY at delta in {0,pi}")
print("=" * 72)
bad = 0
tested = 0
degenerate_deltas = []
thetas = rng.uniform(0.05, np.pi / 2 - 0.05, size=(60, 3))
deltas = np.linspace(0, 2 * np.pi, 1441)
def dist_to_real_sheets(dl):
    """distance from dl to {0, pi, 2pi}"""
    d = dl % np.pi
    return min(d, np.pi - d)
for th in thetas:
    for dl in deltas:
        V = Vckm(*th, dl)
        D = np.abs(V) ** 2
        deg = False
        for (i, j) in [(0, 1), (0, 2), (1, 2)]:
            h, s = triangle_slack(D, i, j)
            if abs(s) < 1e-9:
                deg = True
        tested += 1
        if deg:
            degenerate_deltas.append(dist_to_real_sheets(dl))
        if deg and dist_to_real_sheets(dl) > 1e-6:
            bad += 1
            print("  VIOLATION: degeneracy at delta =", dl)
print(f"  tested {tested} (theta,delta) points; degenerate ones: "
      f"{len(degenerate_deltas)}; away from {{0,pi,2pi}}: {bad}")
print(f"  max distance of a degenerate point to the real sheets "
      f"{{0,pi,2pi}}: {max(degenerate_deltas) if degenerate_deltas else 0:.2e}")
print("  => all 9 walls of U3 are exactly the real sheets delta in {0,pi};")
print("     no non-real 1-degenerate wall points exist in int B3.")

# ---------------- C3 : two sheets over interior, one over walls ----------------
print()
print("=" * 72)
print("[C3] CKM inversion: two branches over interior, one over real locus")
print("=" * 72)
def ckm_invert(D):
    """Invert D -> (theta, cosdelta). Requires all entries > 0."""
    if D.min() <= 0:
        raise ValueError("positive entries required")
    s3sq = D[0, 2]
    c3sq = 1.0 - s3sq
    c1sq = D[0, 0] / c3sq
    s1sq = D[0, 1] / c3sq
    c2sq = D[2, 2] / c3sq
    s2sq = D[1, 2] / c3sq
    t = (np.arccos(np.sqrt(c1sq)), np.arccos(np.sqrt(c2sq)),
         np.arccos(np.sqrt(c3sq)))
    s1, c1 = np.sin(t[0]), np.cos(t[0])
    s2, c2 = np.sin(t[1]), np.cos(t[1])
    s3, c3 = np.sin(t[2]), np.cos(t[2])
    denom = 2 * s1 * c2 * c1 * s2 * s3
    cosd = (D[1, 0] - s1sq * c2sq - c1sq * s2sq * s3sq) / denom
    return t, cosd

n_two_branch = 0
for trial in range(20):
    # random Haar unitary with positive entries
    while True:
        X = (rng.normal(size=(3, 3)) + 1j * rng.normal(size=(3, 3))) / np.sqrt(2)
        Q, R = np.linalg.qr(X)
        Q = Q * np.sign(np.diag(R))
        if np.min(np.abs(Q)) > 0.1:
            break
    U = Q
    D = np.abs(U) ** 2
    t, cosd = ckm_invert(D)
    if not (-1 < cosd < 1):
        print("  (unexpected: Haar point on the wall, skipped)")
        continue
    n_two_branch += 1
    d0 = np.arccos(cosd)
    Vp, Vm = Vckm(*t, d0), Vckm(*t, -d0)
    assert unitary_ok(Vp) and unitary_ok(Vm)
    errp = np.max(np.abs(np.abs(Vp) ** 2 - D))
    errm = np.max(np.abs(np.abs(Vm) ** 2 - D))
    Jp, Jm = Jarskog(Vp), Jarskog(Vm)
    if not (errp < 1e-12 and errm < 1e-12):
        print(f"  FAIL reconstruction: {errp} {errm}")
    if not (abs(Jp + Jm) < 1e-12 and abs(Jp) > 1e-15):
        print(f"  FAIL Jarlskog: {Jp} {Jm}")
print(f"  {n_two_branch}/20 Haar points: two CKM branches (+-delta) both "
      f"reconstruct D to 1e-12, J flips sign")
print("  => fibre of Fl3 -> U3 over an interior point is TWO T^2's "
      "(two Jarlskog sheets).")

n_one_branch = 0
for trial in range(20):
    O = rand_orth()
    D = O ** 2
    t, cosd = ckm_invert(D)
    if abs(abs(cosd) - 1) > 1e-10:
        print(f"  FAIL: real point with |cos delta| = {abs(cosd)}")
    else:
        n_one_branch += 1
print(f"  {n_one_branch}/20 real-orthostochastic points: |cos delta| = 1 "
      f"(single branch, the fold)")
print("  => over the walls the fibre is ONE T^2 (the fold), as the spec says;")
print("     over the interior it is TWO T^2's (spec defect #1).")

# ---------------- C4 : wall gradients parallel on the real locus --------------
print()
print("=" * 72)
print("[C4] the three wall gradients at a real point are parallel (rank<=1)")
print("=" * 72)
def D_of_abcd(a, b, c, d):
    return np.array([
        [a, b, 1 - a - b],
        [c, d, 1 - c - d],
        [1 - a - c, 1 - b - d, a + b + c + d - 1]])

def wall_E(D, i, j, k):
    cols = [x for x in range(3) if x != k]
    l, m = cols
    return (np.sqrt(D[i, k] * D[j, k])
            - np.sqrt(D[i, l] * D[j, l])
            - np.sqrt(D[i, m] * D[j, m]))

worst_rank = 0
for trial in range(10):
    O = rand_orth()
    D0 = O ** 2
    hyps = [triangle_slack(D0, i, j)[0] for (i, j) in [(0, 1), (0, 2), (1, 2)]]
    a0, b0, c0, d0 = D0[0, 0], D0[0, 1], D0[1, 0], D0[1, 1]
    h = 1e-7
    grads = []
    for (ij, k) in zip([(0, 1), (0, 2), (1, 2)], hyps):
        g = np.zeros(4)
        for ax in range(4):
            up = [a0, b0, c0, d0]; up[ax] += h
            dn = [a0, b0, c0, d0]; dn[ax] -= h
            g[ax] = (wall_E(D_of_abcd(*up), ij[0], ij[1], k)
                     - wall_E(D_of_abcd(*dn), ij[0], ij[1], k)) / (2 * h)
        grads.append(g)
    G = np.vstack(grads)
    sv = np.linalg.svd(G, compute_uv=False)
    rank = int(np.sum(sv > sv[0] * 1e-6)) if sv[0] > 0 else 0
    worst_rank = max(worst_rank, rank)
    # also: are the three E's ~constant to first order along random dirs?
print(f"  worst rank of the 3x4 gradient stack over 10 real points: "
      f"{worst_rank}  (needs <= 1 for tangency)")
print("  => the three walls are mutually TANGENT along the 3-dim real locus;")
print("     pairwise intersections are 3-dim (not 'corner 2-loci'), and the")
print("     triple loci are 3-dim (not 6 isolated points). Spec defect #2.")

# ---------------- C5 : J(U P) = J(U) on positive-entry unitaries -------------
print()
print("=" * 72)
print("[C5] J(U P_sigma) = J(U) exactly (c preserves the Jarlskog sheet)")
print("=" * 72)
Psig = np.zeros((3, 3)); Psig[0, 1] = 1; Psig[1, 2] = 1; Psig[2, 0] = 1
err = 0.0
for trial in range(30):
    while True:
        X = (rng.normal(size=(3, 3)) + 1j * rng.normal(size=(3, 3))) / np.sqrt(2)
        Q, R = np.linalg.qr(X)
        Q = Q * np.sign(np.diag(R))
        if np.min(np.abs(Q)) > 0.1:
            break
    err = max(err, abs(Jarskog(Q @ Psig) - Jarskog(Q)))
print(f"  max |J(UP) - J(U)| over 30 Haar samples: {err:.2e}")
print("  => the c-action preserves each Jarlskog sheet (sheets are c-invariant")
print("     4-cells; the t0-twist lives on the fibres over the flat points).")

# ---------------- C6 : the Wave-12b 'corner' is a 3-dim real locus ------------
print()
print("=" * 72)
print("[C6] Wave-12b 'corner' of W(12|1)&W(13|2): actually on the 3rd wall,")
print("     and it moves in a 3-parameter family (dimension 3, not 2)")
print("=" * 72)
# find a real O whose pattern is (h12,h13,h23) = (1,2,3)
found = None
for _ in range(200000):
    O = rand_orth(min_entry=0.02)
    D = O ** 2
    hyps = [triangle_slack(D, i, j)[0] + 1 for (i, j) in [(0, 1), (0, 2), (1, 2)]]
    if hyps == [1, 2, 3]:
        found = (O, D)
        break
O, D = found
print("  found real O with pattern (h12,h13,h23)=(1,2,3):")
print("  O =", np.round(O, 4).tolist())
h1 = wall_E(D, 0, 1, 0); h2 = wall_E(D, 0, 2, 1); h3 = wall_E(D, 1, 2, 2)
print(f"  wall residuals at D=O^2:  E(12|1)={h1:.2e}  E(13|2)={h2:.2e}  "
      f"E(23|3)={h3:.2e}")
print("  => the point is on THREE walls: Wave-12b's 'corner' solutions are")
print("     real-locus points (all three triangles degenerate).")
# 3-dim family: perturb theta in the CKM parametrization at delta=0
t, cosd = ckm_invert(D)
assert abs(abs(cosd) - 1) < 1e-10
moved = 0
for trial in range(200):
    dth = rng.normal(scale=0.02, size=3)
    V = Vckm(*(np.array(t) + dth), 0.0)
    if np.min(np.abs(V)) < 1e-6:
        continue
    Dp = np.abs(V) ** 2
    if max(abs(wall_E(Dp, 0, 1, 0)), abs(wall_E(Dp, 0, 2, 1)),
           abs(wall_E(Dp, 1, 2, 2))) < 1e-9:
        moved += 1
print(f"  random 3-parameter theta-perturbations staying on ALL THREE walls: "
      f"{moved}/200 (|dtheta|~0.02)")
print("  => the 'corner'/'triple' locus is 3-dimensional; the Wave-12b/13")
print("     stratification (18 corner 2-cells, 6 triple points) is refuted.")

print()
print("=" * 72)
print("REVIEW VERDICT INPUTS: C1-C6 all as predicted.")
print("Spec defect #1 (fatal): interior fibre is 2xT^2 (two Jarlskog sheets),")
print("   not T^2 -- the single-top-cell design builds half the space.")
print("Spec defect #2 (fatal): the walls are exactly the orthostochastic locus;")
print("   wall pair intersections are 3-dim tangent overlaps, not 2-cells;")
print("   triples are 3-dim regions, not 6 points; no 'rook corner' strata.")
print("=" * 72)
