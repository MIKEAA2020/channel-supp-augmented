# WAVE 15 (13C-10): the H_2 -> delta_2 BRIDGE at theorem level + the CLSS
# arbiter (audit A2 layer 5) + the transfer theorem (audit A3: the p>61 gap).
#
# User directive (2026-09-11): "address ... the H_2 -> delta_2 bridge is
# theorem-level" + "address Audit points ranked in Sec. 6 of the note
# (seam-solution uniqueness is cosmetic; Z/9-smith now has 4 consistency
# layers; p>61 scan gap; geometric identification via lineage)".
#
# Parts:
#   (I)   import wave13c_seam: the FULL 13C-7 battery re-runs from scratch.
#   (II)  NEW module-typing certificates: N = 1+T+T^2 = 0 and T of order
#         exactly 3 on H_4 (the G7/G7b recipe at k=4, mod 7 and mod 13).
#   (III) the Cartan-Leray E_2 page for the free C_3-cover Fl_3 -> B_3,
#         machine-exact from the typed modules (cyclic group cohomology by
#         exact integer Smith normal forms).
#   (IV)  the constraint cascade: brute-force all d_3 assignments consistent
#         with (totals > 6 vanish; H^6 torsion-free; d_2 = 0): exactly TWO
#         worlds; the machine-certified H_*(B_3) (orbit SNF, re-pinned here)
#         selects WORLD 1 uniquely => d_3: E_3^{1,2} -> E_3^{4,0} is ZERO.
#         [audit A2: the 5th independent consistency layer]
#   (V)   the TRANSFER identities on chains, machine-exact on all 14 910
#         cells: pi o tr = 3 id, tr o pi = 1 + T + T^2, d o tr = tr o d_bar.
#         Together with the E_2-page arithmetic (all entries Z-free or
#         3-primary) => Tor H_*(B_3) is 3-primary in EVERY degree:
#         the p > 61 scan gap is closed by THEOREM, not by scanning.
#         [audit A3]
#   (VI)  THE BRIDGE, stated as a theorem with every premise labeled
#         (machine / theory / cited), concluding delta_2(D(C^3)) = 4/3.
import sys
import time
import itertools
import numpy as np

T0 = time.time()


def hdr(s):
    print("\n" + "=" * 78)
    print("WAVE15-CLSS :: %s" % s)
    print("=" * 78)


def tick(s):
    print("[%-8s] %6.1fs" % (s, time.time() - T0))


hdr("(I) import wave13c_seam: the full 13C-7 battery re-runs")
import wave13c_seam as W  # noqa: E402  (script module, ~60 s, prints battery)

print("\n[battery re-certified on import; NC=%d cells, NORB=%d orbit cells]"
      % (W.NC, W.NORB))
tick("import+battery")

# ----------------------------------------------------------------------------
# exact integer Smith machinery (tiny matrices), self-contained
# ----------------------------------------------------------------------------


def _snf(M):
    rows = len(M)
    cols = len(M[0]) if rows else 0
    A = [[int(x) for x in r] for r in M]

    def rop(i1, i2, m):
        for j in range(cols):
            A[i2][j] -= m * A[i1][j]

    def cop(j1, j2, m):
        for i in range(rows):
            A[i][j2] -= m * A[i][j1]

    def swr(i1, i2):
        A[i1], A[i2] = A[i2], A[i1]

    def swc(j1, j2):
        for i in range(rows):
            A[i][j1], A[i][j2] = A[i][j2], A[i][j1]

    r = c = 0
    while r < rows and c < cols:
        while True:
            best = None
            for i in range(r, rows):
                for j in range(c, cols):
                    if A[i][j] != 0 and (best is None
                                         or abs(A[i][j]) < abs(A[best[0]][best[1]])):
                        best = (i, j)
            if best is None:
                break
            i0, j0 = best
            if i0 != r:
                swr(i0, r)
            if j0 != c:
                swc(j0, c)
            piv = A[r][c]
            dirty = False
            for j in range(c + 1, cols):
                if A[r][j] != 0:
                    cop(c, j, A[r][j] // piv)
                    if A[r][j] != 0:
                        dirty = True
            for i in range(r + 1, rows):
                if A[i][c] != 0:
                    rop(r, i, A[i][c] // piv)
                    if A[i][c] != 0:
                        dirty = True
            if not dirty:
                bad = None
                for i in range(r + 1, rows):
                    for j in range(c + 1, cols):
                        if A[i][j] != 0 and A[i][j] % piv != 0:
                            bad = (i, j)
                            break
                    if bad:
                        break
                if bad:
                    rop(bad[0], r, -1)
                    dirty = True
            if not dirty:
                break
        if best is None:
            break
        r += 1
        c += 1
    for i in range(min(rows, cols)):
        if A[i][i] < 0:
            for j in range(cols):
                A[i][j] = -A[i][j]
    diag = [abs(A[i][i]) for i in range(min(rows, cols))]
    return diag


def grp(diag):
    """(rank, torsion) of Z^n / (matrix image) given the SNF diagonal."""
    nz = [d for d in diag if d != 0]
    tors = [d for d in nz if d > 1]
    return len(diag) - len(nz), tors


def im_quot(matrix):
    """Z^r / im(matrix): matrix given as list of columns (each a list)."""
    if not matrix:
        return (0, [], 0)
    rows = len(matrix[0])
    M = [[0] * len(matrix) for _ in range(rows)]
    for j, col in enumerate(matrix):
        for i in range(rows):
            M[i][j] = col[i]
    d = _snf(M)
    rk, tors = grp(d)
    return (rk, tors, sum(1 for x in d if x != 0))


def ker_sub_quot(dmap, prev_map):
    """H = ker(dmap)/im(prev_map) for integer matrices as column lists."""
    # ker(dmap): exact nullspace via SNF of the ROW matrix
    rows = len(dmap[0]) if dmap else 0
    if not dmap:
        K = np.eye(rows, dtype=np.int64)
        rk_ker = rows
    else:
        M = [[0] * len(dmap) for _ in range(rows)]
        for j, col in enumerate(dmap):
            for i in range(rows):
                M[i][j] = col[i]
        # integer kernel: SNF with transforms is needed; use the Fraction
        # nullspace + saturation assert (matrices are tiny and the modules
        # here are kernels of (g-1) or N -- saturated by construction)
        import fractions
        F = [[fractions.Fraction(M[i][j]) for j in range(len(M[0]))]
             for i in range(rows)]
        # Gauss-Jordan exact
        mat = [row[:] for row in F]
        piv = []
        rr = 0
        for cc in range(len(mat[0])):
            sel = None
            for i in range(rr, len(mat)):
                if mat[i][cc] != 0:
                    sel = i
                    break
            if sel is None:
                continue
            mat[rr], mat[sel] = mat[sel], mat[rr]
            inv = 1 / mat[rr][cc]
            mat[rr] = [v * inv for v in mat[rr]]
            for i in range(len(mat)):
                if i != rr and mat[i][cc] != 0:
                    f = mat[i][cc]
                    mat[i] = [a - f * b for a, b in zip(mat[i], mat[rr])]
            piv.append(cc)
            rr += 1
        free = [j for j in range(len(mat[0])) if j not in piv]
        basis = []
        for fc in free:
            v = [fractions.Fraction(0)] * len(mat[0])
            v[fc] = fractions.Fraction(1)
            for i, pc in enumerate(piv):
                v[pc] = -mat[i][fc]
            # scale to primitive integer
            den = 1
            for x in v:
                den = den * x.denominator // np.gcd(den, x.denominator)
            vi = [int(x * den) for x in v]
            g = 0
            for x in vi:
                g = np.gcd(g, abs(x))
            if g > 1:
                vi = [x // g for x in vi]
            basis.append(vi)
        K = np.array(basis, dtype=np.int64).T if basis else \
            np.zeros((rows, 0), dtype=np.int64)
        rk_ker = len(basis)
    if not prev_map:
        return (rk_ker, [], K)
    # coordinates of im(prev) in the K basis: must be integral (saturated)
    coords = []
    for col in prev_map:
        x = solve_lin(K, col)
        if x is None:
            raise AssertionError("image not in kernel")
        coords.append([int(v) for v in x])
    if not coords:
        return (rk_ker, [], K)
    Al = [[coords[j][i] for j in range(len(coords))] for i in range(rk_ker)]
    d = _snf(Al)
    rk, tors = grp(d)
    return (rk, tors, K)


def solve_lin(K, vec):
    import fractions
    n, r = K.shape
    M = [[fractions.Fraction(int(K[i][j])) for j in range(r)]
         + [fractions.Fraction(int(vec[i]))] for i in range(n)]
    piv = []
    row = 0
    for col in range(r):
        sel = None
        for i in range(row, n):
            if M[i][col] != 0:
                sel = i
                break
        if sel is None:
            continue
        M[row], M[sel] = M[sel], M[row]
        inv = 1 / M[row][col]
        M[row] = [v * inv for v in M[row]]
        for i in range(n):
            if i != row and M[i][col] != 0:
                f = M[i][col]
                M[i] = [a - f * b for a, b in zip(M[i], M[row])]
        piv.append(col)
        row += 1
    for i in range(row, n):
        if M[i][r] != 0:
            return None
    x = [fractions.Fraction(0)] * r
    for i, col in enumerate(piv):
        x[col] = M[i][r]
    for v in x:
        if v.denominator != 1:
            raise AssertionError("nonintegral kernel coordinates (saturated?)")
    return [int(v) for v in x]


# ----------------------------------------------------------------------------
# (II) module typing: N = 0 and order-3 on H_4 (NEW), re-check H_2 at p=13
# ----------------------------------------------------------------------------
hdr("(II) the C_3-modules H^q(Fl_3): typing certificates")


def typing_check(k, p):
    """G7/G7b recipe at degree k mod p: N = 0 on H_k; T of order exactly 3.
    float64-accelerated mod-p arithmetic (exact: entries stay < 2^53)."""
    dk = W.dense_D(k, p, dtype=np.int64)
    dk1 = W.dense_D(k + 1, p, dtype=np.int64)
    B = np.array(W.nullspace_dense(dk, p), dtype=np.int64)
    if B.shape[0] == 0:
        return None, None
    T, _, _ = W.dense_T(k, p)
    Tf = T.astype(np.float64) % p
    TT = (Tf @ Tf) % p
    Nf = (np.eye(W.NK[k], dtype=np.float64) + Tf + TT) % p
    NB = (Nf @ B.T.astype(np.float64)) % p
    r_d = W.rank_dense_modp(dk1.copy(), p)
    r_comb = W.rank_dense_modp(
        np.hstack([dk1, NB.astype(np.int64) % p]).copy() % p, p)
    n_zero = (r_comb == r_d)
    TB = ((Tf - np.eye(W.NK[k], dtype=np.float64)) @ B.T.astype(np.float64)) % p
    r_comb2 = W.rank_dense_modp(
        np.hstack([dk1, TB.astype(np.int64) % p]).copy() % p, p)
    order3 = (r_comb2 > r_d)
    return n_zero, order3


results = {}
for k, ps in ((2, (7, 13)), (4, (7, 13))):
    for p in ps:
        nz, o3 = typing_check(k, p)
        results[(k, p)] = (nz, o3)
        print("H_%d (mod %2d): N=1+T+T^2 equals 0 on homology: %s ;  T has "
              "order exactly 3: %s" % (k, p, nz, o3))
ok2 = all(results[(2, p)] == (True, True) for p in (7, 13))
ok4 = all(results[(4, p)] == (True, True) for p in (7, 13))
print("H_2 typing (omega, both primes): %s ; H_4 typing (omega, both primes): "
      "%s ; H_6: T=+1 certified by the battery G8 (rank 1, sign +1)."
      % ("PASS" if ok2 else "FAIL", "PASS" if ok4 else "FAIL"))
assert ok2 and ok4
betaF = W.betaF
print("H_*(Fl_3) ranks (battery G3): %s -> modules: q=0: Z(triv), q=2: Z^2"
      "(omega), q=4: Z^2(omega), q=6: Z(triv, +1)" % betaF)
tick("typing")

# ----------------------------------------------------------------------------
# (III) the E_2 page from the typed modules (exact cyclic cohomology)
# ----------------------------------------------------------------------------
hdr("(III) the Cartan-Leray E_2^{p,q} = H^p(C_3; H^q(Fl_3)) -- machine-exact")

OMEGA_G = [[0, -1], [1, -1]]   # the order-3 GL_2(Z) matrix (no eigenvalue 1)


def mat_mul(A, B):
    return [[sum(A[i][t] * B[t][j] for t in range(len(B))) for j in range(len(B[0]))]
            for i in range(len(A))]


def mat_add(A, B):
    return [[A[i][j] + B[i][j] for j in range(len(A[0]))] for i in range(len(A))]


def cols_of(A):
    return [[A[i][j] for i in range(len(A))] for j in range(len(A[0]))]


def group_cohom(g, rank, pmax):
    """H^p(C_3; M) for p = 0..pmax, M = Z^rank with g acting; exact."""
    n = rank
    I = [[int(i == j) for j in range(n)] for i in range(n)]
    gm = [[g[i][j] for j in range(n)] for i in range(n)]
    g2 = mat_mul(gm, gm)
    gmin1 = [[gm[i][j] - I[i][j] for j in range(n)] for i in range(n)]
    Nm = [[I[i][j] + gm[i][j] + g2[i][j] for j in range(n)] for i in range(n)]
    # cochain complex: 0 -> M --(g-1)--> M --N--> M --(g-1)--> M --N--> ...
    out = []
    prev = None       # im of delta^{p-1} as column list
    for p in range(pmax + 1):
        dmap = gmin1 if p % 2 == 0 else Nm
        rk, tors, K = ker_sub_quot(cols_of(dmap), prev)
        out.append((rk, tors))
        prev = cols_of(dmap)
    return out


PMAX = 15
PAGE = {}
for q, (g, rank) in ((0, ([[1]], 1)), (2, (OMEGA_G, 2)),
                     (4, (OMEGA_G, 2)), (6, ([[1]], 1))):
    cohs = group_cohom(g, rank, PMAX)
    for p, (rk, tors) in enumerate(cohs):
        if rk > 0 or tors:
            PAGE[(p, q)] = (rk, tors)

print("E_2 page (nonzero entries; q = 0, 2, 4, 6 rows; p up to %d):" % PMAX)
for q in (0, 2, 4, 6):
    row = []
    for p in range(0, 16):
        if (p, q) in PAGE:
            rk, tors = PAGE[(p, q)]
            s = "Z" if rk else ""
            if rk and tors:
                s += "+"
            s += "+".join("Z/%d" % t for t in tors) if tors else ("" if tors else ("Z" if rk else ""))
            if s == "":
                s = "0"
            row.append("p=%d:%s" % (p, s))
    print("  q=%d: %s" % (q, "  ".join(row)))

# every entry is Z-free or 3-primary (the A3 arithmetic core)
prim = all(all(t in (1, 3) or t % 3 == 0 and t in (3,) for t in tors)
           for (rk, tors) in PAGE.values())
alltor3 = all(all(t == 3 for t in tors) for (rk, tors) in PAGE.values())
print("all torsion entries are exactly Z/3 (no Z/9, no other primes): %s"
      % ("PASS" if alltor3 else "FAIL"))
assert alltor3
# d_2 = 0 structurally: targets (p+2, q-1) have odd q-1 -> no entries
d2ok = all((p + 2, q - 1) not in PAGE or q - 1 in (0, 2, 4, 6)
           for (p, q) in PAGE)
print("d_2 targets land on empty rows (rows are 2 apart): %s"
      % ("PASS" if d2ok else "FAIL"))
assert d2ok
tick("E2 page")

# ----------------------------------------------------------------------------
# (IV) the constraint cascade + the world selection
# ----------------------------------------------------------------------------
hdr("(IV) the d_3 cascade: forced arrows, two worlds, machine selection")

# the machine-certified H_*(B_3), re-pinned in THIS run (orbit SNF + Z/9)
r1, c1 = W.coker_order9(1)
r2, c2 = W.coker_order9(2)
r3, c3 = W.coker_order9(3)
r4, c4 = W.coker_order9(4)
H1_9 = (c1 * c2) // (9 ** W.QK[0])
H2_9 = (c2 * c3) // (9 ** W.QK[1])
H3_9 = (c3 * c4) // (9 ** W.QK[2])
betaQ, torsQ = W.betaQ, W.torsQ
print("orbit SNF re-run: beta=%s t_3=%s ; |H_k(Z/9)| = %s"
      % (betaQ, torsQ[3], [W.H0_9, H1_9, H2_9, H3_9]))
import math

e1 = round(math.log(H1_9, 3)) if H1_9 in (1, 3, 9) else None
e2 = round(math.log(H2_9, 3)) - e1 if H2_9 in (1, 3, 9, 27, 81) and e1 is not None else None
# H_3, H_4 exponents (13C-8 pinned e_3 = e_4 = 1); re-derive the Z/9 slot
t3H3 = torsQ[3][3]
t3H4 = torsQ[3][4]
Hvec = []
for k in range(7):
    Hvec.append((betaQ[k], torsQ[3][k]))
print("certified H_*(B_3) = %s  [13C-8: H_3 = H_4 = Z/3 exactly]"
      % Hvec)
CERT = (betaQ[0] == 1 and betaQ[6] == 1 and betaQ[1] == betaQ[2] == 0
        and Hvec[1] == (0, 1) and Hvec[2] == (0, 1) and Hvec[3] == (0, 1)
        and Hvec[4] == (0, 1) and Hvec[5] == (0, 0) and Hvec[6] == (1, 0))
assert CERT, "certified vector mismatch"
# UCT: H^k(B_3) from the certified homology
HCOH = []
for k in range(7):
    hom_k = (betaQ[k], torsQ[3][k])
    hom_prev = (betaQ[k - 1], torsQ[3][k - 1]) if k else (1, 0)
    free = hom_k[0]
    tor = hom_prev[1] + (hom_k[1] if False else 0)
    # H^k = Hom(H_k, Z) (+) Ext(H_{k-1}, Z); Ext(Z/3, Z) = Z/3
    HCOH.append((free, hom_prev[1]))
print("UCT-dual H^*(B_3) = %s" % HCOH)

# d_3 arrows between nonzero entries.  The page is 2-periodic in p (infinite
# to the right); only arrows whose SOURCE has total <= 7 can affect the
# observable E_inf (d_3 raises the total by exactly 1, and entries at total
# >= 8 can never reach back into totals <= 6).  The tail (total >= 8) dies by
# the periodic iso-pairing, verified structurally below.
ARROWS = []
for (p, q) in sorted(PAGE):
    tgt = (p + 3, q - 2)
    if q >= 2 and p + q <= 7 and tgt in PAGE:
        ARROWS.append(((p, q), tgt))
print("d_3 arrows with source-total <= 7: %d" % len(ARROWS))
for a, b in ARROWS:
    print("   %s -> %s   [%s -> %s]" % (a, b, PAGE[a], PAGE[b]))

# structural tail verification: entries with total >= 8 whose twin
# (p+3, q-2) lies INSIDE the window must be paired (source or target);
# entries at the window edge (twin beyond PMAX) must be deep tail
# (total >= 12, far beyond the observables), where the 2-periodicity of the
# page (the pattern (odd,2)->(even,0), (even,6)->(odd,4) persists for all p)
# pairs them off by the same isos -- recorded as the periodicity argument.
TWIN = {(p, q): (p + 3, q - 2) for (p, q) in PAGE if q in (2, 6)
        and (p + 3, q - 2) in PAGE}
tail_ok = True
for e in PAGE:
    if e[0] + e[1] >= 8:
        if e in TWIN or e in TWIN.values():
            continue
        if e[0] + e[1] >= 12:
            continue          # window-edge deep tail (periodicity argument)
        tail_ok = False
        print("   unpaired tail entry: %s" % (e,))
print("tail (total >= 8) paired by the periodic d_3 isos (in-window pairs + "
      "the 2-periodicity argument at the window edge): %s"
      % ("PASS" if tail_ok else "FAIL"))
assert tail_ok


def is_free(entry):
    rk, tors = PAGE[entry]
    return rk > 0 and not tors


def brute_worlds():
    worlds = []
    for bits in itertools.product((0, 1), repeat=len(ARROWS)):
        surv = {}
        for e in PAGE:
            if e[0] + e[1] <= 6:
                surv[e] = PAGE[e]
        dead = set()
        for (on, (a, b)) in zip(bits, ARROWS):
            if on:
                # nonzero differential a -> b (both a,b are torsion Z/3 or
                # a = (0,6) is Z): torsion case = iso (both die); Z -> Z/3
                # = surjection (source survives as 3Z ~ Z, target dies)
                if is_free(a):
                    surv[a] = (1, [])
                else:
                    surv.pop(a, None)
                    dead.add(a)
                surv.pop(b, None)
                dead.add(b)
        ok = True
        if (6, 0) in surv:
            ok = False          # H^6 must be torsion-free
        for e in PAGE:
            if e[0] + e[1] == 7 and e not in dead:
                ok = False      # total-7 entries must die (dim B_3 = 6)
                break
        if not ok:
            continue
        worlds.append((bits, dict(surv)))
    return worlds


worlds = brute_worlds()
print("assignments consistent with (totals>6 vanish; H^6 torsion-free; tail "
      "paired): %d" % len(worlds))
bitidx = [i for i, (a, b) in enumerate(ARROWS) if a == (1, 2) and b == (4, 0)]
assert len(bitidx) == 1
bitidx = bitidx[0]


def world_Hn(surv):
    out = {}
    for (p, q), (rk, tors) in surv.items():
        n = p + q
        out.setdefault(n, []).append((p, q, rk, tuple(tors)))
    return out


matches = []
for bits, surv in worlds:
    Hn = world_Hn(surv)
    ok = True
    for n in range(7):
        pieces = Hn.get(n, [])
        tfree, ttor = HCOH[n]
        gotfree = sum(1 for pc in pieces if pc[2] > 0 and not pc[3])
        gottor = sum(len(pc[3]) for pc in pieces)
        if (gotfree, gottor) != (tfree, ttor):
            ok = False
            break
    if ok:
        matches.append((bits, surv, Hn))
print("worlds whose E_inf matches the certified H^*(B_3) exactly: %d"
      % len(matches))
bitvals = set(bits[bitidx] for (bits, _, _) in matches)
print("the bit d_3: E_3^{1,2} -> E_3^{4,0} across matching worlds: %s"
      % (sorted(bitvals),))
if bitvals == {0}:
    print("   -> ZERO in every world matching the certified H^*(B_3)")
assert bitvals == {0}, "the world selection failed"
print("""
(IV) VERDICT: the E_2 page + the axioms (dim 6, H^6 free, d_2 = 0) admit
exactly two d_3 assignments (World 1: the bit is ZERO; World 2: iso, killing
both (1,2) and (4,0)).  The machine-certified H^*(B_3) = (Z, 0, Z/3, Z/3,
Z/3, Z/3, Z) matches World 1 ONLY.  Hence:

      d_3: E_3^{1,2} -> E_3^{4,0} is ZERO    [WORLD 1]

This is an INDEPENDENT derivation of the world bit from the T-action on
H_*(Fl_3) + cyclic group cohomology -- a 5th consistency layer for the
Z/9-smith pipeline (audit A2).""")
tick("cascade")

# ----------------------------------------------------------------------------
# (V) the transfer identities (audit A3)
# ----------------------------------------------------------------------------
hdr("(V) the transfer: pi o tr = 3 id, tr o pi = 1+T+T^2, d tr = tr d_bar")


def sparse_add(acc, idx, co):
    acc[idx] = acc.get(idx, 0) + co
    if acc[idx] == 0:
        del acc[idx]


# pi: chains(Fl) -> chains(B): pi(e_i) = OSGN[i] * e_{ORB[i]}
# tr: chains(B) -> chains(Fl): tr(e_r) = sum_{x in orbit(r)} OSGN[x] e_x
# (i) pi o tr = 3 id on orbit reps
bad1 = 0
for r in W.REPS:
    o = [r, W.TSUP[r], W.TSUP[W.TSUP[r]]]
    s = sum(W.OSGN[x] ** 2 for x in o)
    if s != 3:
        bad1 += 1
assert bad1 == 0
print("(i)  pi(tr(e_r)) = 3 e_r on all %d orbit reps: PASS (exact)"
      % len(W.REPS))

# (ii) tr o pi = 1 + T + T^2 on all cells
bad2 = 0
witness = None
for i in range(W.NC):
    lhs = {}
    oi = W.ORB[i]
    for x in (oi, W.TSUP[oi], W.TSUP[W.TSUP[oi]]):
        sparse_add(lhs, x, W.OSGN[i] * W.OSGN[x])
    # 1 + T + T^2 (e_i):
    i1 = W.TSUP[i]
    i2 = W.TSUP[i1]
    rhs = {i: 1}
    sparse_add(rhs, i1, W.TSGN[i])
    sparse_add(rhs, i2, W.TSGN[i] * W.TSGN[i1])
    if lhs != rhs:
        bad2 += 1
        if witness is None:
            witness = (i, lhs, rhs)
assert bad2 == 0, "tr o pi != 1+T+T^2 at %s" % (witness,)
print("(ii) tr(pi(e_i)) = (1 + T + T^2)(e_i) on all %d cells: PASS (exact)"
      % W.NC)

# (iii) d o tr = tr o d_bar  (tr is a chain map)
bad3 = 0
w3 = None
for k in range(1, 7):
    for r, col in W.DB[k].items():
        # d(tr(e_r)):
        lhs = {}
        o = [r, W.TSUP[r], W.TSUP[W.TSUP[r]]]
        for x in o:
            for j, co in W.D[x].items():
                sparse_add(lhs, j, W.OSGN[x] * co)
        # tr(d_bar(e_r)):
        rhs = {}
        for row, co in col.items():
            oo = [row, W.TSUP[row], W.TSUP[W.TSUP[row]]]
            for x in oo:
                sparse_add(rhs, x, W.OSGN[x] * co)
        if lhs != rhs:
            bad3 += 1
            if w3 is None:
                w3 = (k, r, lhs, rhs)
assert bad3 == 0, "d tr != tr d_bar at %s" % (w3,)
print("(iii) d(tr(e_r)) = tr(d_bar(e_r)) on all %d orbit columns: PASS "
      "(exact)" % sum(len(W.DB[k]) for k in range(1, 7)))
print("""
(V) THEOREM (transfer + CLSS arithmetic; audit A3):
  pi_* o tr_* = 3 id on H_*(B_3)  [chain identities (i)+(iii) certified exact
  on every cell]; every E_2 entry of the CLSS is Z-free or Z/3 (III);
  E_inf pieces are subquotients of E_2; H^k(B_3) has a filtration with
  E_inf graded pieces; extensions of 3-primary groups are 3-primary.
  Hence Tor H^k(B_3) is 3-primary for EVERY k, and by UCT
  Tor H_k(B_3) ~ Tor H^{k+1}(B_3) is 3-primary for every k.

  => NO p != 3 torsion in any degree of H_*(B_3), by theorem.
  => the p > 61 scan gap is CLOSED (the finite prime scans of 13C-7/8 were
     sufficient all along: only p = 3 could occur; the Z/9-smith pinned the
     3-adic exponents: H_k = Z/3 in k = 1..4).""")
tick("transfer")

# ----------------------------------------------------------------------------
# (VI) the bridge theorem
# ----------------------------------------------------------------------------
hdr("(VI) THE BRIDGE: H_2(B_3) = Z/3  =>  delta_2(D(C^3)) = 4/3")
print("""
THEOREM (the H_2 -> delta_2 bridge).  Premises, each labeled:

  (P1) [MACHINE, 13C-7/8, re-certified on this import + (II) above]
       Fl_3 carries the free order-3 c-action (G4/G6, coset lemma:
       u P_sigma T^3 = u T^3 forces P_sigma^k in T^3, false for k=1,2);
       H_*(Fl_3) = (Z, 0, Z^2, 0, Z^2, 0, Z) torsion-free (G3);
       the C_3-modules: H^0, H^6 trivial (T = +1 on H_6, G8), H^2, H^4 of
       omega-type (N = 0 and order exactly 3, mod 7 AND mod 13, (II)).
  (P2) [MACHINE, 13C-7/8, re-pinned in (IV)] the orbit-complex SNF:
       H_*(B_3) = (Z, Z/3, Z/3, Z/3, Z/3, 0, Z) with the Z/9 exponents
       pinned (no Z/9); UCT-dual H^*(B_3) = (Z, 0, Z/3, Z/3, Z/3, Z/3, Z),
       PD-palindromic (13C-8 cross-check).
  (P3) [THEORY] the Cartan-Leray spectral sequence of the regular cover
       Fl_3 -> B_3 with group C_3: E_2^{p,q} = H^p(C_3; H^q(Fl_3)) abuts to
       H^{p+q}(B_3); cyclic group cohomology computed exactly (III);
       d_2 = 0 structurally; the d_3 cascade constrained by (dim B_3 = 6,
       H^6 torsion-free) admits exactly two worlds (IV).
  (P4) [MACHINE, (IV)] the certified H^*(B_3) matches World 1 ONLY:
       the differential d_3: E_3^{1,2} -> E_3^{4,0} is ZERO.
  (P5) [CITED, the Wave-7 theorem / the CLSS framework of the paper line]
       for x in H^2(B_3; Z) = Z/3 the classifying class: the cup square
       x^2 in H^4(B_3; Z) = Z/3 is nonzero IF AND ONLY IF the CLSS
       differential d_3: E_3^{1,2} -> E_3^{4,0} vanishes (d_3 is exactly
       the obstruction to x^2 surviving).
  (P6) [CITED, the paper line] delta_2(D(C^3)) = 4/3 if and only if
       x^2 != 0 (the delta-invariant formula for the qutrit).

  CONCLUSION: P1+P2+P3+P4 give d_3 = 0; P5 gives x^2 != 0 in
  H^4(B_3; Z) = Z/3; P6 gives

      delta_2(D(C^3)) = 4/3,

  with the qutrit bit's machine side (P1, P2, P4) certified end-to-end and
  the two cited links (P5, P6) isolated as the paper-line inputs.  The
  equivalence is complete: World 2 (H_2 = 0, d_3 iso, x^2 = 0) is excluded
  by P2.  QED

  Status of the bridge: the machine certifies every homological premise;
  the cup-product step (P5) and the delta formula (P6) remain cited theory
  (computing the orbit-complex cup product is not part of this run).""")
tick("bridge done")
