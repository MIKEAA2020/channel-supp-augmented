#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""IIS diagnostics for the sign-parameterized level-12 systems (mod 3, mod 4)."""
import itertools
import json

import numpy as np

exec(open("wave13c_l12_eqs_probe.py").read()) if False else None

# rebuild the systems exactly as wave13c_l12.py does (import the builder by
# running the script's Part II/III construction in a controlled way)
import importlib.util
import sys

src = open("wave13c_l12.py").read()
cut = src.index('hdr("PART III')
pre = src[:cut]
# execute Parts 0-II (needs the JSONs; cwd must be glm)
g = {}
exec(compile(pre, "l12_pre", "exec"), g)

MOD = 12
KAPPA_R = g["KAPPA_R"]
KAPPA_F = g["KAPPA_F"]
KAPPA_E = g["KAPPA_E"]
W_RF = g["W_RF"]
SHIFT_FE = g["SHIFT_FE"]
D_REG = g["D_REG"]
CMAP = g["CMAP"]
EDGE_KEYS = g["EDGE_KEYS"]
TT0SQ = g["TT0SQ"]
TT0S = g["TT0S"]
WALLS = [0, 1, 2, 3]
WDIR = {0: (1, 0), 1: (1, 0), 2: (0, 1), 3: (1, -1)}
RLO = {0: 2, 1: 1, 2: 2, 3: 1}
RHI = {0: 4, 1: 5, 2: 5, 3: 4}
WFI = {0: 0, 1: 1, 2: 2, 3: 3}
WHI_W = {0: (6, 0), 1: (6, 0), 2: (0, 6), 3: (6, 6)}
CF_F = [4, 0, 7, 6, 1, 2, 8, 5, 3]
CF_E = {ei: CMAP[6 + ei] - 6 for ei in range(9)}
RNAME = g["RNAME"]


def build_system(s1, s2, s3):
    equations = []
    VARS = set()

    def eq_add(lhs_vars, rhs):
        equations.append((dict(lhs_vars), rhs % MOD))

    def tvar(si, ri, c):
        VARS.add(('t', si, ri, c))
        return ('t', si, ri, c)

    def svar(si, w, c):
        VARS.add(('s', si, w, c))
        return ('s', si, w, c)

    def rvar(ri, c):
        VARS.add(('r', ri, c))
        return ('r', ri, c)

    def fvar(fi, c):
        VARS.add(('f', fi, c))
        return ('f', fi, c)

    def evar(ei):
        VARS.add(('e', ei))
        return ('e', ei)

    def dvar(si, w):
        VARS.add(('D', si, w))
        return ('D', si, w)

    for si in (0, 1):
        t = TT0SQ if si == 0 else TT0S
        for ri in range(6):
            cR = CMAP[24 + ri] - 24
            for c in range(2):
                lhs = {tvar(si, ri, c): 1, tvar(si, cR, c): -1}
                if s1:
                    lhs[rvar(ri, c)] = s1
                    lhs[rvar(cR, c)] = -s1
                eq_add(lhs, (KAPPA_R[ri][c] - t[c]))
    MIX = [(4, 0, 3), (5, 0, 1), (6, 0, 2), (7, 3, 4), (8, 3, 5)]
    for si in (0, 1):
        for (fi, ra, rb) in MIX:
            for c in range(2):
                lhs = {tvar(si, ra, c): 1, tvar(si, rb, c): -1}
                if s2:
                    lhs[rvar(ra, c)] = s2
                    lhs[rvar(rb, c)] = -s2
                eq_add(lhs, 0)
    for si in (0, 1):
        for w in WALLS:
            lo, hi = RLO[w], RHI[w]
            d = WDIR[w]
            fi = WFI[w]
            for c in range(2):
                lhs = {svar(si, w, c): 1, tvar(si, lo, c): -1}
                if s3:
                    lhs[rvar(lo, c)] = s3
                    lhs[fvar(fi, c)] = -s3
                eq_add(lhs, 0)
                lhs = {svar(si, w, c): 1, tvar(si, hi, c): -1}
                if s3:
                    lhs[rvar(hi, c)] = s3
                    lhs[fvar(fi, c)] = -s3
                if d[c]:
                    lhs[dvar(si, w)] = d[c]
                eq_add(lhs, WHI_W[w][c])
    for rid in range(6):
        for (ficell, co) in D_REG[rid].items():
            fi = ficell - 15
            cR = CMAP[24 + rid] - 24
            cF = CF_F[fi]
            if (cR, cF) not in W_RF:
                continue
            for c in range(2):
                eq_add({rvar(cR, c): 1, fvar(cF, c): -1, rvar(rid, c): -1,
                        fvar(fi, c): 1},
                       (W_RF[(rid, fi)][c] - KAPPA_R[rid][c] + KAPPA_F[fi][c]
                        - W_RF[(cR, cF)][c]))
    for (fi, ei) in SHIFT_FE.keys():
        cF = CF_F[fi]
        cE = CF_E[ei]
        if (cF, cE) not in SHIFT_FE:
            continue
        rho_p, pi = EDGE_KEYS[ei]
        a = [i for i in range(3) if pi[i] == i][0]
        if a == 0:
            qcu, qcv = 0, -1
        elif a == 1:
            qcu, qcv = -1, -1
        else:
            qcu, qcv = -1, 0
        eq_add({fvar(cF, 0): qcu, fvar(cF, 1): qcv, fvar(fi, 0): -qcu,
                fvar(fi, 1): -qcv, evar(ei): -1, evar(cE): 1},
               (SHIFT_FE[(fi, ei)] - KAPPA_F[fi][0] * qcu - KAPPA_F[fi][1] * qcv
                + KAPPA_E[ei] - SHIFT_FE[(cF, cE)]
                - KAPPA_F[cF][0] * qcu - KAPPA_F[cF][1] * qcv
                + KAPPA_E[cE]))
    return equations, VARS


def eqdesc(lhs, rhs):
    terms = " ".join("%+d*%s" % (co, k) for k, co in sorted(lhs.items(), key=str))
    return "%s = %d" % (terms, rhs)


def consistent(subset, p, halved=False):
    rows = []
    for (lhs, rhs) in subset:
        r = [0] * (NV + 1)
        for v, co in lhs.items():
            r[VI[v]] += co % p
        r[-1] = ((rhs // 2) % p) if halved else (rhs % p)
        rows.append(r)
    M = np.array(rows, dtype=np.int64) % p
    m, n = M.shape
    r = 0
    for j in range(n - 1):
        piv = -1
        for i in range(r, m):
            if M[i, j] % p:
                piv = i
                break
        if piv < 0:
            continue
        M[[r, piv]] = M[[piv, r]]
        inv = pow(int(M[r, j]), p - 2, p)
        M[r] = (M[r] * inv) % p
        for i in range(m):
            if i != r and M[i, j] % p:
                M[i] = (M[i] - M[i, j] * M[r]) % p
        r += 1
    for i in range(m):
        if all(M[i, j] % p == 0 for j in range(n - 1)) and M[i, -1] % p:
            return False
    return True


def iis(eqs, p, halved=False):
    if consistent(eqs, p, halved):
        return None
    cur = list(eqs)
    changed = True
    while changed:
        changed = False
        for i in range(len(cur)):
            trial = cur[:i] + cur[i + 1:]
            if not consistent(trial, p, halved):
                cur = trial
                changed = True
                break
    return cur


for signs in [(1, -1, 0), (-1, 1, 0), (1, 0, 0)]:
    eqs, vs = build_system(*signs)
    VLIST = sorted(vs, key=str)
    VI = {v: i for i, v in enumerate(VLIST)}
    NV = len(VLIST)
    print("=" * 70)
    print("signs (s1,s2,s3) = %s, %d equations, %d vars" % (signs, len(eqs), NV))
    for (p, halved, tag) in [(3, False, "mod 3"), (2, True, "mod 4 (halved)")]:
        s = iis(eqs, p, halved)
        if s is None:
            print("  %s: CONSISTENT" % tag)
        else:
            print("  %s: INCONSISTENT, IIS (%d eqs):" % (tag, len(s)))
            for (lhs, rhs) in s:
                print("     %s" % eqdesc(lhs, rhs))
