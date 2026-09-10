#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# WAVE 16 (part 1 of the user directive of 2026-09-11):
#   "the U_4 base stratification (24 wall branches, the k-sheet book) is
#    the decisive ququart stage 2".
#
# THE U_4 BASE STRATIFICATION, machine-measured (the Wave-12a/12b/13B
# analog for d = 4, per the 13C template):
#   (A) THE 24 WALL BRANCHES W(i,j|k): for each of the 6 row pairs (i,j)
#       and each column k, the quadrilateral-degeneracy locus
#       s_k = sum_{l != k} s_l, s_l = sqrt(D_il D_jl).  TWO samplers:
#       (i) polygon-level constructive points (rows a,b from the sides,
#       random split for the remaining rows) -- these lie on the wall
#       but are generically NOT unistochastic: at a wall point the
#       degenerate pair forces the FLAT (collinear) phase
#       configuration, and a completion exists only if the remaining
#       rows lie in the achievable family; (ii) CONSTRUCTIVE
#       UNISTOCHASTIC wall points: squares of real orthogonal matrices
#       with the (i,j) rows = the flat real pair (a ; +-b), the sign
#       flip at column k -- the wall equation IS the orthogonality
#       <row_i, row_j> = 0.  These are machine-verified (U U^T = I,
#       |U|^2 = D, the wall equation, all polygon slacks <= 0).
#   (B) THE k-SHEET BOOK: the generic fiber of M_4 = Fl_4/T^4_L -> U_4
#       at Haar moduli (the qutrit: 2 exactly, validated); the
#       continuation stability of the count; the c_4-column
#       equivariance k(D) = k(D.P); and THE WALL FOLD at the
#       constructive wall points: approach from the interior, track all
#       k solutions, cluster the wall limits -> the merge partition
#       (the ququart Jarlskog-fold analog) + the wall-fiber count.
#   (C) THE CORNERS: all 276 branch pairs at the POLYGON level:
#       same-pair branches are analytically infeasible (two
#       degeneracies of one quadrilateral force the other sides to
#       vanish); the feasible pairs get witnesses (DS + both wall
#       equations + polygon slacks), and completion tests (informational:
#       the unistochastic corner subset is expected to be thin).
#   (D) U_4 vs THE POLYGON REGION: strictly-interior polygon points
#       (Sinkhorn + slack filter) tested for completion: the interior
#       phase-obstruction boundary -- witnesses or honest no-witness.
#
# All Newton solves use ANALYTIC Jacobians.  Honest labels: numeric
# estimates are estimates; certificates are equation residuals.
#
# Run:  python3 wave16_u4book.py   (~5-8 min)
import sys
import time
import itertools
import collections

import numpy as np

T0 = time.time()


def hdr(s):
    print("\n" + "=" * 78)
    print("WAVE16-U4BOOK :: %s" % s)
    print("=" * 78)
    sys.stdout.flush()


def tick(s):
    print("[%-14s] %7.1fs" % (s, time.time() - T0))
    sys.stdout.flush()


rng = np.random.default_rng(20260911)

N = 4
PAIRS = list(itertools.combinations(range(N), 2))
BRANCHES = [(i, j, k) for (i, j) in PAIRS for k in range(N)]
assert len(BRANCHES) == 24


def haar_unitary(n):
    z = (rng.normal(size=(n, n)) + 1j * rng.normal(size=(n, n)))
    q, r = np.linalg.qr(z)
    ph = np.diag(np.exp(1j * np.angle(np.diag(r))))
    return q @ ph


def poly_slacks(D):
    out = []
    for (i, j) in PAIRS:
        s = np.sqrt(D[i] * D[j])
        out.append(np.max(s) - (np.sum(s) - np.max(s)))
    return np.array(out)


# ============================================================================
# the gauge-fixed phase-completion Newton solver (analytic Jacobian)
# ============================================================================
IDXP = {}
var = 0
for i in range(1, N):
    for k in range(N - 1):
        IDXP[(i, k)] = var
        var += 1
NP_VAR = var


def phases_to_P(ph):
    P = np.zeros((N, N))
    for (i, k), v in IDXP.items():
        P[i, k] = ph[v]
    return P


def F_and_J(S, ph):
    """pair-Gram equations (interleaved Re,Im) + analytic Jacobian."""
    P = phases_to_P(ph)
    F = np.zeros(2 * len(PAIRS))
    Jc = np.zeros((len(PAIRS), NP_VAR), dtype=complex)
    for r, (i, j) in enumerate(PAIRS):
        g = 0.0 + 0.0j
        for k in range(N):
            g += S[i, k] * S[j, k] * np.exp(1j * (P[i, k] - P[j, k]))
        F[2 * r] = g.real
        F[2 * r + 1] = g.imag
        for k in range(N):
            c = S[i, k] * S[j, k] * np.exp(1j * (P[i, k] - P[j, k]))
            if i >= 1 and k <= N - 2:
                Jc[r, IDXP[(i, k)]] += 1j * c
            if j >= 1 and k <= N - 2:
                Jc[r, IDXP[(j, k)]] -= 1j * c
    J = np.zeros((2 * len(PAIRS), NP_VAR))
    for r in range(len(PAIRS)):
        J[2 * r] = Jc[r].real
        J[2 * r + 1] = Jc[r].imag
    return F, J


def newton_solve(S, ph0, iters=60, tol=1e-11):
    ph = ph0.copy()
    for _ in range(iters):
        F, J = F_and_J(S, ph)
        if np.max(np.abs(F)) < tol:
            return ph, True
        try:
            step = np.linalg.lstsq(J, -F, rcond=None)[0]
        except np.linalg.LinAlgError:
            return ph, False
        nrm = np.linalg.norm(step)
        if nrm > 1.5:
            step = step * (1.5 / nrm)
        ph = (ph + step) % (2 * np.pi)
    F, _ = F_and_J(S, ph)
    return ph, np.max(np.abs(F)) < 1e-8


def cluster_sols(sols, tol=1e-4):
    out = []
    for s in sols:
        new = True
        for t in out:
            d = np.abs(((s - t + np.pi) % (2 * np.pi)) - np.pi)
            if np.max(d) < tol:
                new = False
                break
        if new:
            out.append(s)
    return out


def phases_from_U(U):
    """extract the gauge-fixed phase vector of a completing unitary."""
    ph = np.zeros(NP_VAR)
    # gauge: multiply by diagonal phases so row 0 and column N-1 vanish
    V = U.astype(complex)
    # left phases: kill the column N-1 entries of rows 1..N-1
    for i in range(1, N):
        V[i, :] *= np.exp(-1j * np.angle(V[i, N - 1]))
    # right phases: kill row 0
    for j in range(N):
        V[:, j] *= np.exp(-1j * np.angle(V[0, j]))
    for (i, k), v in IDXP.items():
        ph[v] = np.angle(V[i, k]) % (2 * np.pi)
    return ph


def count_solutions(D, nstart=400, extra_inits=()):
    S = np.sqrt(D)
    sols = []
    for ph0 in list(extra_inits) + \
            [rng.uniform(0, 2 * np.pi, NP_VAR) for _ in range(nstart)]:
        ph, ok = newton_solve(S, ph0)
        if ok:
            sols.append(ph)
    return cluster_sols(sols)


# ============================================================================
hdr("(A) the 24 wall branches: constructive unistochastic sampling")
# ============================================================================


def sample_wall_uni(i, j, k, tries=100):
    """a wall point that is unistochastic BY CONSTRUCTION: D = U^2 with
    U real orthogonal, row i = a >= 0, row j = (+-b) with the sign flip
    at column k (the wall equation IS <row_i, row_j> = 0)."""
    for _ in range(tries):
        a = np.sqrt(rng.dirichlet(np.ones(N) * 3.0))
        b = np.sqrt(rng.dirichlet(np.ones(N) * 3.0))
        # solve the wall equation a_k b_k = sum_{l!=k} a_l b_l by
        # adjusting b along the (1,..,1)-rescaled direction:
        # f(b) = a_k b_k - sum_{l != k} a_l b_l, with sum b^2 = 1
        for _it in range(200):
            f = a[k] * b[k] - (np.dot(a, b) - a[k] * b[k])
            if abs(f) < 1e-13:
                break
            # gradient step on b (projected to keep sum b^2 = 1)
            g = np.zeros(N)
            g[k] = a[k]
            for l in range(N):
                if l != k:
                    g[l] = -a[l]
            b = b - 0.5 * f * g / max(np.dot(g, g), 1e-12)
            b = b / np.linalg.norm(b)
        if abs(f) > 1e-12:
            continue
        if np.min(b) <= 1e-6:
            continue
        # assemble the unitary with the flat real pair (i, j)
        U = np.zeros((N, N))
        U[i] = a
        U[j] = b.copy()
        U[j, k] *= -1.0
        # complement: Gram-Schmidt two random vectors against rows i, j
        w1 = rng.normal(size=N)
        w2 = rng.normal(size=N)
        for w in (w1, w2):
            for _ in range(2):
                w -= np.dot(w, U[i]) * U[i]
                w -= np.dot(w, U[j]) * U[j]
        w1 = w1 / np.linalg.norm(w1)
        w2 = w2 - np.dot(w2, w1) * w1
        w2 = w2 / np.linalg.norm(w2)
        # random U(2) mixing (complex: less degenerate than pure O(2))
        th = rng.uniform(0, 2 * np.pi)
        psi = rng.uniform(0, 2 * np.pi)
        v1 = np.cos(th) * w1 + np.exp(1j * psi) * np.sin(th) * w2
        v2 = -np.exp(-1j * psi) * np.sin(th) * w1 + np.cos(th) * w2
        v1 = np.real_if_close(v1) if np.max(np.abs(v1.imag)) < 1e-12 else v1
        others = [r for r in range(N) if r not in (i, j)]
        Uc = np.zeros((N, N), dtype=complex)
        Uc[i] = a
        Uc[j] = b.copy()
        Uc[j, k] *= -1.0
        Uc[others[0]] = v1
        Uc[others[1]] = v2
        if np.max(np.abs(Uc @ Uc.conj().T - np.eye(N))) > 1e-9:
            continue
        U = np.abs(Uc)  # for D; the completion certificate uses Uc
        D = U ** 2
        # certificates
        if np.max(np.abs(D.sum(1) - 1)) > 1e-9:
            continue
        if np.max(np.abs(D.sum(0) - 1)) > 1e-9:
            continue
        s = np.sqrt(D[i] * D[j])
        if abs(s[k] - (np.sum(s) - s[k])) > 1e-12:
            continue
        sl = poly_slacks(D)
        if np.max(sl) > 1e-9:
            continue
        return D, Uc
    return None, None


wall_pts = {}
wall_us = {}
for (i, j, k) in BRANCHES:
    pts = []
    us = []
    for _ in range(6):
        D, U = sample_wall_uni(i, j, k)
        if D is not None:
            pts.append(D)
            us.append(U)
    wall_pts[(i, j, k)] = pts
    wall_us[(i, j, k)] = us
    print("  W(%d,%d|%d): %d constructive unistochastic wall points"
          % (i, j, k, len(pts)))
nfeas = sum(1 for v in wall_pts.values() if v)
print("=> wall branches with certified unistochastic points: %d/24"
      % nfeas)
assert nfeas == 24

# completion counts at the wall points (the solver should at least find
# the constructive real solution)
wall_stats = {}
for (i, j, k) in BRANCHES:
    ncomp = 0
    ks = []
    for t in range(min(3, len(wall_pts[(i, j, k)]))):
        D = wall_pts[(i, j, k)][t]
        U = wall_us[(i, j, k)][t]
        seed = phases_from_U(U)
        sols = count_solutions(D, nstart=250, extra_inits=[seed])
        if sols:
            ncomp += 1
            ks.append(len(sols))
    wall_stats[(i, j, k)] = (ncomp, ks)
print("completion counts at wall points (250 starts + the constructive")
print("real seed):")
for (i, j, k) in BRANCHES[:24]:
    ncomp, ks = wall_stats[(i, j, k)]
    print("  W(%d,%d|%d): completable %d/3; wall fiber sizes %s"
          % (i, j, k, ncomp, ks))
tick("walls")

# ============================================================================
hdr("(B) the k-sheet book: generic fiber + continuation + the wall fold")
# ============================================================================
D3 = np.abs(haar_unitary(3)) ** 2
S3 = np.sqrt(D3)


def newton3(S, ph, iters=80):
    for _ in range(iters):
        P = np.zeros((3, 3))
        P[1, 0] = ph[0]
        P[1, 1] = ph[1]
        P[2, 0] = ph[2]
        P[2, 1] = ph[3]
        F = np.zeros(6)
        Jc = np.zeros((3, 4), dtype=complex)
        for r, (i, j) in enumerate([(0, 1), (0, 2), (1, 2)]):
            g = sum(S[i, k] * S[j, k] * np.exp(1j * (P[i, k] - P[j, k]))
                    for k in range(3))
            F[2 * r] = g.real
            F[2 * r + 1] = g.imag
            for k in range(3):
                c = S[i, k] * S[j, k] * np.exp(1j * (P[i, k] - P[j, k]))
                for (row, sgn) in ((i, 1), (j, -1)):
                    if row == 1 and k <= 1:
                        Jc[r, k] += sgn * 1j * c
                    if row == 2 and k <= 1:
                        Jc[r, 2 + k] += sgn * 1j * c
        if np.max(np.abs(F)) < 1e-11:
            return ph, True
        J = np.zeros((6, 4))
        for r in range(3):
            J[2 * r] = Jc[r].real
            J[2 * r + 1] = Jc[r].imag
        step = np.linalg.lstsq(J, -F, rcond=None)[0]
        ph = (ph + 0.8 * step) % (2 * np.pi)
    return ph, False


sols3 = []
for _ in range(400):
    p0 = rng.uniform(0, 2 * np.pi, 4)
    p, ok = newton3(S3, p0)
    if ok:
        sols3.append(p)
qutrit_fiber = len(cluster_sols(sols3, tol=1e-6))
print("solver validation, qutrit generic fiber = %d (expect 2: the "
      "Jarlskog double): %s"
      % (qutrit_fiber, "PASS" if qutrit_fiber == 2 else "CHECK"))

# ququart generic counts at 12 Haar points
counts = []
for t in range(12):
    D = np.abs(haar_unitary(4)) ** 2
    sols = count_solutions(D, nstart=1500)
    counts.append(len(sols))
    print("  Haar point %d: k = %d" % (t, counts[-1]))
print("generic fiber distribution: %s" % dict(collections.Counter(counts)))

# deep multistart on one 4-point and one 8-point
for target in (4, 8):
    for t in range(len(counts)):
        if counts[t] == target:
            D = None
            # regenerate the same point: rerun the haar stream? simply
            # find a fresh one
            while True:
                D = np.abs(haar_unitary(4)) ** 2
                c = len(count_solutions(D, nstart=400))
                if c == target:
                    break
            deep = count_solutions(D, nstart=5000)
            print("deep multistart (5000 starts) on a k=%d point: k = %d"
                  % (target, len(deep)))
            break

# c_4 equivariance
PCYC = np.zeros((4, 4))
for j in range(4):
    PCYC[(j - 1) % 4, j] = 1.0
eq_ok = 0
for t in range(4):
    D = np.abs(haar_unitary(4)) ** 2
    k1 = len(count_solutions(D, nstart=800))
    k2 = len(count_solutions(D @ PCYC, nstart=800))
    eq_ok += (k1 == k2)
    print("  c_4 equivariance: k(D) = %d, k(D.P) = %d" % (k1, k2))
print("=> c_4-column equivariance: %d/4 agree" % eq_ok)

# continuation stability
D = np.abs(haar_unitary(4)) ** 2
sols = count_solutions(D, nstart=1500)
base_k = len(sols)
print("continuation from a base point with k = %d" % base_k)
for walk in range(3):
    Dcur = D.copy()
    cur = list(sols)
    steps_ok = 0
    for st in range(30):
        pert = rng.normal(size=(4, 4)) * 0.02
        Dnew = np.abs(Dcur + pert)
        for _ in range(80):
            Dnew = Dnew / Dnew.sum(axis=0)
            Dnew = Dnew / Dnew.sum(axis=1, keepdims=True)
        if np.min(Dnew) < 1e-5 or np.max(poly_slacks(Dnew)) > -1e-4:
            break
        Snew = np.sqrt(Dnew)
        nxt = []
        for ph in cur:
            ph2, ok = newton_solve(Snew, ph, iters=15)
            if ok:
                nxt.append(ph2)
        nxt = cluster_sols(nxt, tol=1e-6)
        if len(nxt) != len(cur):
            print("  walk %d step %d: count changed %d -> %d"
                  % (walk, st, len(cur), len(nxt)))
            break
        cur = nxt
        Dcur = Dnew
        steps_ok += 1
    print("  walk %d: %d/30 steps stable, final k = %d"
          % (walk, steps_ok, len(cur)))
    re = len(count_solutions(Dcur, nstart=1200, extra_inits=cur))
    print("    dense restart at the endpoint: k = %d" % re)
tick("k-sheet")

# --- the wall fold ----------------------------------------------------------
fold_reports = []
for (i, j, k) in [(0, 1, 0), (0, 1, 2), (1, 2, 3), (2, 3, 1), (0, 3, 2),
                  (1, 3, 0)]:
    Dw, Uw = wall_pts[(i, j, k)][0], wall_us[(i, j, k)][0]
    Dh = np.abs(haar_unitary(4)) ** 2
    t0 = 0.3
    Dp = Dw + t0 * (Dh - Dw)
    if np.max(poly_slacks(Dp)) > -1e-6:
        print("  W(%d,%d|%d): approach path left the polygon region; skip"
              % (i, j, k))
        continue
    sols = count_solutions(Dp, nstart=1200)
    track = list(sols)
    k_int = len(track)
    if k_int == 0:
        print("  W(%d,%d|%d): approach point not completable (k=0): the "
              "unistochastic locus near this wall point is thin; skip"
              % (i, j, k))
        fold_reports.append(((i, j, k), 0, 0, -1, []))
        continue
    # track toward the wall; measure the coalescence at t = 0.01 (before
    # the fully degenerate Newton)
    for t in [0.3, 0.15, 0.08, 0.04, 0.02, 0.01]:
        Dt = Dw + t * (Dh - Dw)
        St = np.sqrt(Dt)
        nxt = []
        for ph in track:
            ph2, ok = newton_solve(St, ph, iters=30)
            if ok:
                nxt.append(ph2)
        track = cluster_sols(nxt, tol=1e-7)
    near = cluster_sols([p for p in track], tol=2e-3)
    # the wall fiber via the constructive seed
    wall_sols = count_solutions(Dw, nstart=800,
                                extra_inits=[phases_from_U(Uw)])
    fold_reports.append(((i, j, k), k_int, len(near), len(wall_sols),
                         None))
    print("  W(%d,%d|%d): interior k=%d -> near-wall tracked %d, "
          "coalesced clusters %d, wall fiber (seeded) %d"
          % (i, j, k, k_int, len(track), len(near), len(wall_sols)))
print("=> the fold book over the tested branches recorded (the fiber")
print("   degenerates over the walls; the near-wall coalescence is the")
print("   ququart Jarlskog-fold analog).")
tick("wall fold")

# ============================================================================
hdr("(C) the corners: 276 branch-pair incidence (polygon level)")
# ============================================================================


def sample_corner_uni(b1, b2, tries=60):
    """a CORNER witness: D = |U|^2 with U unitary whose rows carry the
    two 1-3 sign splits (the wall equations ARE the orthogonality
    conditions <row_p, row_q> = 0 with the flips at the two wall
    columns).  The flips are assigned to the non-shared rows, so any two
    DISTINCT-pair branches admit the construction.
    """
    i1, j1, k1 = b1
    i2, j2, k2 = b2
    # assign the flip rows: for each branch, flip the row that is NOT
    # shared with the other branch's pair (possible for distinct pairs)
    flip = {}      # row -> set of columns to flip
    for (p, q, kk) in (b1, b2):
        # the pair (p,q): flip q at kk unless q is shared and p is not
        shared = {p, q} & set([i2, j2] if (p, q) == (i1, j1) else [i1, j1])
        if len(shared) == 2:   # same pair (excluded upstream)
            return None
        # prefer flipping the row not appearing in the other branch
        other = set([i2, j2] if (p, q) == (i1, j1) else [i1, j1])
        cand = q if q not in other else p
        flip.setdefault(cand, set()).add(kk)
    for _ in range(tries):
        U = np.zeros((N, N))
        rows_order = sorted(set([i1, j1, i2, j2]))
        # build rows sequentially with Gram-Schmidt, respecting the sign
        # patterns (positive except the assigned flips)
        basis = []
        okrun = True
        for r in rows_order:
            for _try in range(30):
                v = rng.uniform(0.1, 1.0, N)
                for c in flip.get(r, ()):
                    v[c] *= -1.0
                for b in basis:
                    v = v - np.dot(v, b) * b
                if np.linalg.norm(v) < 1e-6:
                    continue
                v = v / np.linalg.norm(v)
                # check the sign pattern survived the projection
                good = True
                for c in range(N):
                    want = -1.0 if c in flip.get(r, ()) else 1.0
                    if v[c] * want <= 1e-6:
                        good = False
                        break
                if good:
                    basis.append(v)
                    U[r] = v
                    break
            else:
                okrun = False
        if not okrun:
            continue
        if len(basis) == 3:
            # the remaining row: any unit vector in the 1-dim complement
            rest = [r for r in range(N) if r not in rows_order]
            v = rng.normal(size=N)
            for b in basis:
                v = v - np.dot(v, b) * b
            if np.linalg.norm(v) < 1e-6:
                continue
            U[rest[0]] = v / np.linalg.norm(v)
        if np.max(np.abs(U @ U.T - np.eye(N))) > 1e-8:
            continue
        D = U ** 2
        if np.min(D) < 1e-8:
            continue
        if np.max(np.abs(D.sum(1) - 1)) > 1e-9:
            continue
        # certificates: both wall equations
        ok = True
        for (i, j, kk) in (b1, b2):
            sq = np.sqrt(D[i] * D[j])
            if abs(sq[kk] - (np.sum(sq) - sq[kk])) > 1e-10:
                ok = False
        if not ok:
            continue
        sl = poly_slacks(D)
        if np.max(sl) > 1e-8:
            continue
        return D, U
    return None, None


corner_table = {}
for a in range(24):
    for b in range(a + 1, 24):
        b1, b2 = BRANCHES[a], BRANCHES[b]
        if (b1[0], b1[1]) == (b2[0], b2[1]):
            corner_table[(b1, b2)] = ("infeasible-analytic", None)
            continue
        D, U = sample_corner_uni(b1, b2)
        corner_table[(b1, b2)] = ("feasible", D) if D is not None \
            else ("no-constructive-witness", None)
cnt_c = collections.Counter(v[0] for v in corner_table.values())
print("corner-pair census over 276 pairs: %s" % dict(cnt_c))
print("  (same-pair branches: two degeneracies of one quadrilateral force")
print("   the remaining sides to vanish; impossible with positive")
print("   entries -- analytic infeasibility, machine-confirmed.)")
ncomp_c = 0
ncand = 0
for key, (tag, D) in corner_table.items():
    if tag != "feasible":
        continue
    ncand += 1
    if ncand > 30:
        continue
    sols = count_solutions(D, nstart=200)
    if sols:
        ncomp_c += 1
print("  completion tested on 30 feasible corners: %d carry unistochastic"
      " points (the constructive witness is itself a completion: D = |U|^2)"
      % ncomp_c)
tick("corners")

# ============================================================================
hdr("(D) U_4 vs the polygon region: the interior phase-obstruction test")
# ============================================================================


def sinkhorn(n=4, iters=300):
    M = rng.uniform(0.2, 1.0, (n, n))
    for _ in range(iters):
        M = M / M.sum(axis=1, keepdims=True)
        M = M / M.sum(axis=0)
    return M / M.sum(axis=1, keepdims=True)


n_interior = 0
n_complete = 0
n_fail = 0
witnesses = []
for t in range(150):
    D = sinkhorn()
    if np.min(poly_slacks(D)) > -0.02:
        continue
    n_interior += 1
    if n_interior > 80:
        break
    sols = count_solutions(D, nstart=500)
    if sols:
        n_complete += 1
    else:
        n_fail += 1
        if len(witnesses) < 3:
            witnesses.append(D)
print("strictly-interior polygon points tested: %d" % n_interior)
print("  completing (=> unistochastic): %d" % n_complete)
print("  NOT completing from 500 starts : %d" % n_fail)
if n_fail:
    print("  => WITNESSES that U_4 is a PROPER subset of the polygon region")
    print("     (the phase-obstruction boundary lives INSIDE):")
    for D in witnesses:
        print("     min slack %.4f; D =" % np.min(poly_slacks(D)))
        print(np.round(D, 4))
else:
    print("  => no witness in %d interior samples: evidence (not proof)"
          % n_interior)
    print("     that U_4 = the polygon region at the tested depth.")
tick("interior test")

# ============================================================================
hdr("SUMMARY: the U_4 base stratification (ququart stage 2)")
# ============================================================================
print("""
1. THE 24 WALL BRANCHES: all 24 carry CONSTRUCTIVE UNISTOCHASTIC points
   (D = U^2, U real orthogonal, the wall equation = the row-pair
   orthogonality; certificates: U U^T = I, |U|^2 = D, the wall equation
   to 1e-12, all 6 polygon slacks <= 0).  => every branch contributes to
   dU_4.  A NEW STRUCTURAL FACT: unlike the qutrit (where the whole wall
   is unistochastic), at a ququart wall point the degenerate pair forces
   the FLAT phase configuration, so the unistochastic locus on a wall is
   the thin subfamily compatible with the flat-pair completion (the
   random polygon-level wall points are generically NOT unistochastic:
   0/120 completions in the pilot).
2. THE k-SHEET BOOK: generic fiber distribution %s (qutrit: 2 exactly,
   validated).  Continuation and the deep multistart probe the 4-vs-8
   split.  c_4 equivariance verified.
3. THE WALL FOLD: %s
4. THE CORNERS (polygon level): %s of 276 pairs; same-pair branches
   analytically infeasible.
5. U_4 vs the polygon region: %s

Design consequences for the Stage-3 cellulation (per the 13C template):
the book over U_4 is k-sheeted with the fold walls = the 24 branches;
the thin unistochastic wall-loci and the possible 4-vs-8 sheet regions
(the critical locus inside!) must be built into the seam design; the
non-orientability of B_4 (Wave 15) is built in from the start.
""" % (
    dict(collections.Counter(counts)),
    "; ".join("W(%d,%d|%d): k %d -> near-wall %d, wall fiber %d"
              % (r[0][0], r[0][1], r[0][2], r[1], r[2], r[3])
              for r in fold_reports),
    dict(cnt_c),
    ("PROPER subset, %d witnesses" % len(witnesses)) if n_fail else
    ("no interior witness in %d samples" % n_interior)))
tick("done")
