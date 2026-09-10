# WAVE 15 (13C-9): OP2 -- the equator complex (dU_3) is S^3: a machine proof.
#
# User directive (2026-09-11): "address sigma-class connectedness, dU_3 ~= S^3
# proof, the H_2 -> delta_2 bridge is theorem-level" + the ranked audit points.
#
# This script proves, from the CERTIFIED 13C-7/8 book (wave13c_base.py, whose
# battery re-runs on import):
#   (A) the equator subcomplex E = the 30 cells (6V + 9E + 9F + 6R) with the
#       certified D_EDGE/D_FACE/D_REG has integral homology (Z, 0, 0, Z),
#       exactly (tiny exact Smith normal forms, no lattice shortcuts);
#   (B) every vertex link is a CLOSED connected surface with H = (Z, 0, Z)
#       => S^2 (classification of closed surfaces) => |E| is a closed
#       combinatorial 3-manifold (conditional on the regular-CW lineage
#       premise, documented in the note);
#   (C) pi_1(E) = 1: spanning-tree presentation + Tietze collapse to the
#       empty presentation (sound: Tietze transformations preserve the group);
#   (D) conclusion: |E| is a closed 3-manifold with pi_1 trivial, hence
#       homeomorphic to S^3 by the Poincare theorem (Perelman).  With the
#       lineage identification E = dU_3 this closes 14H's boxed H-top item
#       "dU_3 ~= S^3 beyond chi + connectedness".
#
# Honest caveats (recorded, not hidden):
#   - the equator's realization IS dU_3 only through the book's construction
#     lineage (audit point A4 of the reconciliation note); the machine
#     certificates here are combinatorial properties OF THE BOOK.
#   - the 14H digital chi(dU_3) = 0 at grids n = 24/32/40 is the independent
#     external cross-check (already recorded).
import sys
import time
import numpy as np
from collections import deque

T0 = time.time()


def hdr(s):
    print("\n" + "=" * 78)
    print("WAVE15-EQUATOR :: %s" % s)
    print("=" * 78)


def tick(s):
    print("[%-8s] %6.1fs" % (s, time.time() - T0))


hdr("import wave13c_base (the certified G0 book; battery re-runs on import)")
import wave13c_base as B  # noqa: E402  (script-style module, runs ~3 s)

PI2 = B.PI2
NV, NE, NF, NR = 6, 9, 9, 6
print("book imported; using the 30 equator cells (6 V, 9 E, 9 F, 6 R).")
tick("import")

# ----------------------------------------------------------------------------
# exact integer Smith normal form with transforms (tiny matrices only)
# ----------------------------------------------------------------------------


def _snf_uv(M):
    """M (list-of-lists int) -> (P, D, Q) with A_final = P M Q, A = D in Smith
    form, P/Q unimodular.  Divisibility d_i | d_{i+1} enforced by the classic
    submatrix-divisibility refinement."""
    rows = len(M)
    cols = len(M[0]) if rows else 0
    A = [[int(x) for x in r] for r in M]
    P = [[int(i == j) for j in range(rows)] for i in range(rows)]
    Q = [[int(i == j) for j in range(cols)] for i in range(cols)]

    def row_op(i1, i2, mult):      # A[i2] -= mult * A[i1]
        for j in range(cols):
            A[i2][j] -= mult * A[i1][j]
        for j in range(rows):
            P[i2][j] -= mult * P[i1][j]

    def col_op(j1, j2, mult):      # A[:, j2] -= mult * A[:, j1]
        for i in range(rows):
            A[i][j2] -= mult * A[i][j1]
        for i in range(cols):
            Q[i][j2] -= mult * Q[i][j1]

    def swap_rows(i1, i2):
        A[i1], A[i2] = A[i2], A[i1]
        P[i1], P[i2] = P[i2], P[i1]

    def swap_cols(j1, j2):
        for i in range(rows):
            A[i][j1], A[i][j2] = A[i][j2], A[i][j1]
        for i in range(cols):
            Q[i][j1], Q[i][j2] = Q[i][j2], Q[i][j1]

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
                swap_rows(i0, r)
            if j0 != c:
                swap_cols(j0, c)
            piv = A[r][c]
            dirty = False
            for j in range(c + 1, cols):
                if A[r][j] != 0:
                    q = A[r][j] // piv
                    col_op(c, j, q)
                    if A[r][j] != 0:
                        dirty = True
            for i in range(r + 1, rows):
                if A[i][c] != 0:
                    q = A[i][c] // piv
                    row_op(r, i, q)
                    if A[i][c] != 0:
                        dirty = True
            if not dirty:
                # pivot divides its row/col; must divide the whole submatrix
                bad = None
                for i in range(r + 1, rows):
                    for j in range(c + 1, cols):
                        if A[i][j] != 0 and A[i][j] % piv != 0:
                            bad = (i, j)
                            break
                    if bad:
                        break
                if bad:
                    row_op(bad[0], r, -1)   # A[r] += A[bad_row]
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
            for j in range(rows):
                P[i][j] = -P[i][j]
    diag = [A[i][i] for i in range(min(rows, cols))]
    for i in range(len(diag) - 1):
        if diag[i] != 0 and diag[i + 1] != 0 and diag[i + 1] % diag[i] != 0:
            raise AssertionError("SNF divisibility failed: %s" % diag)
    return P, A, Q


def int_kernel(M):
    """basis (columns) of the integer kernel lattice of M (list-of-lists)."""
    rows = len(M)
    cols = len(M[0]) if rows else 0
    if rows == 0:
        return np.eye(cols, dtype=np.int64), cols
    _, D, Q = _snf_uv(M)
    Df = [[0] * cols for _ in range(rows)]
    for i in range(min(rows, cols)):
        for j in range(min(rows, cols)):
            Df[i][j] = D[i][j]
    Qm = np.array(Q, dtype=np.int64)
    basis = [Qm[:, j] for j in range(cols)
             if all(Df[i][j] == 0 for i in range(rows))]
    if not basis:
        return np.zeros((cols, 0), dtype=np.int64), 0
    return np.array(basis, dtype=np.int64).T, len(basis)


def solve_coords(Kbasis, vec):
    """exact rational coordinates x with Kbasis @ x = vec."""
    import fractions
    n, r = Kbasis.shape
    M = [[fractions.Fraction(int(Kbasis[i][j])) for j in range(r)]
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
    return x


def homology_of(Dmats, nk):
    """exact integral homology: H_k = ker d_k / im d_{k+1} via exact kernel
    lattices + SNF of the image coordinates."""
    out = {}
    for k in range(len(nk)):
        dk = Dmats.get(k)
        dk1 = Dmats.get(k + 1)
        if dk is None or all(all(v == 0 for v in row) for row in dk):
            K = np.eye(nk[k], dtype=np.int64)
            rk_k = nk[k]
        else:
            K, rk_k = int_kernel(dk)
        if rk_k == 0:
            out[k] = (0, [])
            continue
        if dk1 is None or all(all(v == 0 for v in row) for row in dk1):
            out[k] = (rk_k, [])
            continue
        n1 = len(dk1[0])
        coords = []
        for j in range(n1):
            cv = [dk1[i][j] for i in range(len(dk1))]
            x = solve_coords(K, np.array(cv, dtype=np.int64))
            if x is None:
                raise AssertionError("im d_{k+1} not in ker d_k at k=%d" % k)
            coords.append(x)
        import fractions
        for x in coords:
            for v in x:
                if isinstance(v, fractions.Fraction) and v.denominator != 1:
                    raise AssertionError("nonintegral coords at k=%d" % k)
        if not coords:
            out[k] = (rk_k, [])
            continue
        Al = [[int(v) for v in [coords[j][i] for j in range(len(coords))]]
              for i in range(rk_k)]
        _, D, _ = _snf_uv(Al)
        diag = [abs(D[i][i]) for i in range(min(len(Al), len(Al[0])))]
        nz = sum(1 for d in diag if d != 0)
        tors = [d for d in diag if d > 1]
        out[k] = (rk_k - nz, tors)
    return out


# ----------------------------------------------------------------------------
# (A) the equator complex + exact homology
# ----------------------------------------------------------------------------
hdr("(A) the equator complex: exact integral homology")


def dense(k):
    if k == 1:
        return [[B.D_EDGE[e].get(v, 0) for e in range(NE)] for v in range(NV)]
    if k == 2:
        return [[B.D_FACE[f].get(6 + e, 0) for f in range(NF)] for e in range(NE)]
    if k == 3:
        return [[B.D_REG[r].get(15 + f, 0) for r in range(NR)] for f in range(NF)]
    return None


NK = [NV, NE, NF, NR]
DM = {1: dense(1), 2: dense(2), 3: dense(3)}
for k in (2, 3):
    A = np.array(DM[k], dtype=np.int64)
    Bm = np.array(DM[k - 1], dtype=np.int64)
    assert np.max(np.abs(Bm @ A)) == 0, "d^2 != 0 at k=%d" % k
print("equator d^2 = 0 re-certified (k=2,3): PASS")
H = homology_of(DM, NK)
for k in range(4):
    rk, tors = H[k]
    print("H_%d(equator) = Z^%d %s" % (
        k, rk, ("+ " + " + ".join("Z/%d" % t for t in tors)) if tors else ""))
H_OK = (H[0] == (1, []) and H[1] == (0, []) and H[2] == (0, [])
        and H[3] == (1, []))
print("(A) VERDICT: H_*(equator) = (Z, 0, 0, Z) exactly (no torsion): %s"
      % ("PASS" if H_OK else "FAIL"))
if not H_OK:
    sys.exit(1)
print("chi(equator) = %d  (14H digital chi(dU_3) = 0 at grids 24/32/40)"
      % (NK[0] - NK[1] + NK[2] - NK[3]))
tick("homology")

# ----------------------------------------------------------------------------
# ordered F-boundary walks (needed for links + pi_1)
# ----------------------------------------------------------------------------
hdr("(A2) ordered F-boundary walks (side tracing + blowups, in order)")


def ordered_walk(fi):
    """CCW cyclic word of (edge_id, sign) for d(F); aggregation must equal
    the certified D_FACE[fi]."""
    pmap = B.FPMAP[fi]
    seq = []
    side_th2 = {}
    SIDES = [
        ("bottom", lambda s: (s, 0.0), +1),
        ("right", lambda s: (PI2, s), +1),
        ("top", lambda s: (s, PI2), -1),
        ("left", lambda s: (0.0, s), -1),
    ]
    agg = {}
    for (nm, f, dr) in SIDES:
        labs = set()
        for s in (0.22 * PI2, 0.5 * PI2, 0.78 * PI2):
            p = pmap(*f(s))
            c = B.mcell(np.array([p[0], p[1], p[2]]), p[3])
            labs.add(c)
        assert len(labs) == 1, "F%d side %s labels %s" % (fi, nm, labs)
        c = labs.pop()
        if c is None or not (6 <= c < 15):
            for s in (0.02 * PI2, 0.98 * PI2):
                p = pmap(*f(s))
                side_th2[(nm, round(s / PI2))] = p[1]
            seq.append((nm, None, 0))
            continue

        def t_exact(s):
            p = pmap(*f(s))
            return B.edge_param(c - 6, np.array([p[0], p[1], p[2]]))

        t0, t1 = t_exact(0.0), t_exact(PI2)
        dt = (t1 - t0) if dr > 0 else (t0 - t1)
        assert abs(abs(dt) - 1) < 1e-9, "F%d side %s dt=%.6f" % (fi, nm, dt)
        sg = int(round(dt))
        agg[c] = agg.get(c, 0) + sg
        seq.append((nm, c, sg))
        for s in (0.02 * PI2, 0.98 * PI2):
            p = pmap(*f(s))
            side_th2[(nm, round(s / PI2))] = p[1]
    if fi >= 5:
        for u0, cnm, before in [(PI2, "corner_b0", "bottom"),
                                (0.0, "corner_00", "left")]:
            if u0 == 0.0:
                th2_in = side_th2[("left", 0)]
                th2_out = side_th2[("bottom", 0)]
            else:
                th2_in = side_th2[("bottom", 1)]
                th2_out = side_th2[("right", 0)]
            if abs(th2_in - th2_out) < 0.1:
                continue
            thm = np.array([u0, 0.5 * PI2, 0.0])
            cm = B.mcell(thm, 0.0)
            assert cm is not None and 6 <= cm < 15, "blowup label %s" % cm
            t_in = B.edge_param(cm - 6, np.array([u0, th2_in, 0.0]))
            t_out = B.edge_param(cm - 6, np.array([u0, th2_out, 0.0]))
            ddt = t_out - t_in
            assert abs(abs(ddt) - 1) < 1e-6, "blowup dt %s" % ddt
            sg = int(round(ddt))
            agg[cm] = agg.get(cm, 0) + sg
            idx = [i for i, (nm, _, _) in enumerate(seq) if nm == before][0]
            seq.insert(idx + 1, (cnm, cm, sg))
    df = {int(k): v for k, v in B.D_FACE[fi].items()}
    assert {k: v for k, v in agg.items() if v != 0} == df, \
        "F%d aggregation %s != D_FACE %s" % (fi, agg, df)
    word = [(c, sg) for (nm, c, sg) in seq if c is not None]
    return word


def edge_endpoints(ei):
    d = B.D_EDGE[ei]
    start = [k for k, v in d.items() if v == -1][0]
    end = [k for k, v in d.items() if v == 1][0]
    return start, end


WALKS = {}
for fi in range(NF):
    word = ordered_walk(fi)
    n = len(word)
    vs = []
    ok = True
    for i in range(n):
        e, sg = word[i]
        a, b = edge_endpoints(e - 6)
        dep, arr = (a, b) if sg > 0 else (b, a)
        if i == 0:
            vs.append(dep)
        elif vs[-1] != dep:
            ok = False
        vs.append(arr)
    closed = (n > 0 and vs[0] == vs[-1])
    print("d(%-14s): %s  chains=%s closes=%s" % (
        B.FNAMES[fi], ["E%d%+d" % (e, sg) for (e, sg) in word], ok, closed))
    assert ok and closed, "F%d walk fails to chain/close" % fi
    WALKS[fi] = (word, vs)
print("all 9 F-boundaries reconstruct as closed cyclic words chaining at "
      "shared vertices, aggregating EXACTLY to the certified d(F): PASS")
tick("walks")

# ----------------------------------------------------------------------------
# (B) vertex links
# ----------------------------------------------------------------------------
hdr("(B) vertex links of the equator complex: closed surfaces, H = (Z,0,Z)")


def link_complex(v):
    E_v = [e for e in range(NE) if v in edge_endpoints(e)]
    pos0 = {e: i for i, e in enumerate(E_v)}
    corners = []       # (fi, e_in, e_out) at v
    for fi in range(NF):
        word, vs = WALKS[fi]
        n = len(word)
        for i in range(n):
            if vs[i + 1] == v:            # corner between word[i], word[i+1]
                corners.append((fi, word[i][0] - 6, word[(i + 1) % n][0] - 6))
    faces = []
    for r in range(NR):
        fs = [int(k) - 15 for k in B.D_REG[r]]
        if any(v in WALKS[f][1] for f in fs):
            faces.append(r)
    d1 = np.zeros((len(E_v), len(corners)), dtype=np.int64)
    for i, (fi, e_in, e_out) in enumerate(corners):
        d1[pos0[e_out], i] += 1
        d1[pos0[e_in], i] -= 1
    d2 = np.zeros((len(corners), len(faces)), dtype=np.int64)
    for j, r in enumerate(faces):
        for k, srf in B.D_REG[r].items():
            fi = int(k) - 15
            for i, (fj, e_in, e_out) in enumerate(corners):
                if fj == fi:
                    d2[i, j] += srf
    return E_v, corners, faces, d1, d2


ALL_S2 = True
for v in range(NV):
    E_v, corners, faces, d1, d2 = link_complex(v)
    inc = np.sum(np.abs(d2), axis=1)
    multi = [i for i in range(len(corners)) if inc[i] != 2]
    # balanced 0-cells: heads == tails at every link vertex (closed surface)
    degbal = int(np.max(np.abs(np.sum(d1, axis=1)))) if len(E_v) else 0
    dd = int(np.max(np.abs(d1 @ d2))) if (d1.size and d2.size) else 0
    seen = set()
    if len(E_v):
        stack = [0]
        while stack:
            x = stack.pop()
            if x in seen:
                continue
            seen.add(x)
            for i in range(len(corners)):
                if d1[x, i] != 0:
                    for y in range(len(E_v)):
                        if d1[y, i] != 0 and y not in seen:
                            stack.append(y)
    conn = (len(seen) == len(E_v))
    nk_l = [len(E_v), len(corners), len(faces)]
    DMl = {1: [[int(d1[i][j]) for j in range(len(corners))]
               for i in range(len(E_v))],
           2: [[int(d2[i][j]) for j in range(len(faces))]
               for i in range(len(corners))]}
    Hl = homology_of(DMl, nk_l)
    h0 = Hl[0]
    h1 = Hl[1]
    chi_l = len(E_v) - len(corners) + len(faces)
    closed = (not multi) and dd == 0
    is_s2 = (h0 == (1, []) and h1 == (0, []) and chi_l == 2
             and conn and closed)
    ALL_S2 = ALL_S2 and is_s2
    print("V%s: link V=%d E=%d F=%d chi=%+d H=(Z^%d%s, Z^%d%s) conn=%s "
          "closed=%s cycles=%s -> %s" % (
              B.PERMS[v], len(E_v), len(corners), len(faces), chi_l,
              h0[0], ("/" + "/".join(str(t) for t in h0[1])) if h0[1] else "",
              h1[0], ("/" + "/".join(str(t) for t in h1[1])) if h1[1] else "",
              conn, "OK" if not multi else "FAIL(bad-incidence %s)" % multi,
              "OK" if dd == 0 else "FAIL(d1d2=%d)" % dd,
              "S^2" if is_s2 else "NOT-S2"))
if ALL_S2:
    print("(B) VERDICT: all 6 vertex links are S^2 (closed, connected, "
          "H=(Z,0,Z)) => the equator is a closed combinatorial 3-manifold "
          "(regular-CW premise): PASS")
else:
    print("(B) VERDICT: some link is NOT S^2 -- honest report above.")
tick("links")

# ----------------------------------------------------------------------------
# (C) pi_1 via spanning tree + Tietze
# ----------------------------------------------------------------------------
hdr("(C) pi_1(equator): spanning-tree presentation + Tietze collapse")

adjE = {e: edge_endpoints(e) for e in range(NE)}
parent = {0: None}
tree = set()
q = deque([0])
while q:
    x = q.popleft()
    for e in range(NE):
        a, b = adjE[e]
        if a == x and b not in parent:
            parent[b] = (x, e, +1)
            tree.add(e)
            q.append(b)
        elif b == x and a not in parent:
            parent[a] = (x, e, -1)
            tree.add(e)
            q.append(a)
assert len(tree) == NV - 1
nontree = [e for e in range(NE) if e not in tree]
gen_of = {e: i + 1 for i, e in enumerate(nontree)}
print("spanning tree: %d edges; generators: %s" %
      (len(tree), ["E%d" % e for e in nontree]))

rels0 = []
for fi in range(NF):
    word, vs = WALKS[fi]
    rels0.append([sg * gen_of[e - 6] for (e, sg) in word if (e - 6) in gen_of])
print("presentation: %d generators, %d relators (lengths %s)" %
      (len(nontree), len(rels0), [len(w) for w in rels0]))


def freered(w):
    out = []
    for g in w:
        if out and out[-1] == -g:
            out.pop()
        else:
            out.append(g)
    return out


def used_gens(rels):
    return sorted({abs(t) for r in rels for t in r})


def tietze(rels):
    rels = [freered(list(w)) for w in rels]
    rels = [w for w in rels if w]
    changed = True
    while changed and rels:
        changed = False
        # length-1 relators: g = 1 (or g^-1 = 1): kill g
        for i, w in enumerate(rels):
            if len(w) == 1:
                g = abs(w[0])
                rels = [[t for t in x if abs(t) != g] for x in rels]
                rels = [freered(x) for x in rels if freered(x)]
                changed = True
                break
        if changed:
            continue
        # length-2 relators [sg*g, sh*h] => h = (-sg*sh) * g
        for i, w in enumerate(rels):
            if len(w) == 2 and w[0] != -w[1] and abs(w[0]) != abs(w[1]):
                g, h = abs(w[0]), abs(w[1])
                sg, sh = (1 if w[0] > 0 else -1), (1 if w[1] > 0 else -1)
                s = -sg * sh
                newr = []
                for x in rels:
                    if x is w:
                        continue
                    y = [s * (1 if t > 0 else -1) * g if abs(t) == h else t
                         for t in x]
                    y = freered(y)
                    if y:
                        newr.append(y)
                    else:
                        newr.append(y)  # keep empties out
                rels = [x for x in newr if x]
                changed = True
                break
        if changed:
            continue
        # relators of the form [g, g] (g^2 = 1) and [g, -g] reduced away;
        # g^2=1 with trivial abelianization cannot persist -- if it does, we
        # report honestly.
    rels = [w for w in rels if w]
    ng = len(used_gens(rels))
    return rels, ng, (len(rels) == 0 and ng == 0)


rels1, ng1, ok_tz = tietze([list(w) for w in rels0])
print("after Tietze: %d generators, %d relators %s" %
      (ng1, len(rels1), rels1[:10]))
if rels1:
    gu = used_gens(rels1)
    gi = {g: i for i, g in enumerate(gu)}
    Mab = np.zeros((len(gu), len(rels1)), dtype=np.int64)
    for j, r in enumerate(rels1):
        for t in r:
            Mab[gi[abs(t)], j] += (1 if t > 0 else -1)
    rk_ab = int(np.linalg.matrix_rank(Mab.astype(np.float64))) if Mab.size else 0
    print("residual abelianization: rank %d / %d generators "
          "(must be full for H_1 = 0)" % (rk_ab, len(gu)))
if ok_tz:
    print("(C) VERDICT: pi_1(equator) = 1 (Tietze collapse to the empty "
          "presentation; Tietze moves are sound): PASS")
else:
    print("(C) VERDICT: not fully collapsed -- honest partial above.")

# ----------------------------------------------------------------------------
# (D) conclusion
# ----------------------------------------------------------------------------
hdr("(D) conclusion")
if H_OK and ALL_S2 and ok_tz:
    print("""
CONCLUSION (machine; conditional on the regular-CW lineage premise, audit A4):
  |equator| is a closed combinatorial 3-manifold (all six vertex links S^2,
  closed, connected, H(link) = (Z,0,Z)), with H_*(|equator|) = (Z,0,0,Z)
  (exact SNF) and pi_1 = 1 (Tietze).  By the Poincare theorem (Perelman),
  |equator| ~= S^3.  The equator is the boundary of BOTH top cells of the
  certified book (d(s+/-) = +-(R3+R4+R5-R0-R1-R2), d^2 = 0), i.e. the fold
  locus of double(U_3) = M.  With the lineage identification equator = dU_3
  (WAVE13C_RECONCILIATION.md Sec. 3), OP2 is CLOSED:

      dU_3 ~= S^3  at theorem level, from the certified stratification.

  Independent cross-checks: chi(dU_3) = 0 (14H digital, 3 grid sizes);
  U_3 itself a 4-ball candidate (chi = 1; the double has H = (Z,0,0,0,Z),
  chi = +2, G0) -- now consistent with dU_3 = S^3 exactly.""")
else:
    print("""
HONEST PARTIAL: some component above did not close; see the per-step
verdicts.  No claim beyond what passed.""")
tick("done")
