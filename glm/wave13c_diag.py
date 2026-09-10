#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
WAVE 13C-5b : constraint-system diagnostics -- find the irreducible
inconsistent subsystem (IIS) of the level-12 rho-gauged sheet-layer system,
mod 3 (and mod 4). Reads wave13c_l12_eqs.json.
"""
import json
import sys

import numpy as np

with open("wave13c_l12_eqs.json") as f:
    EQJ = json.load(f)
varlist = [tuple(eval(v)) if v[0] == "(" else v for v in EQJ["varlist"]]
VI = {v: i for i, v in enumerate(varlist)}
eqs = []
for (lhs, rhs) in EQJ["equations"]:
    d = {}
    for k, v in lhs.items():
        key = tuple(eval(k)) if k[0] == "(" else k
        d[VI[key]] = v
    eqs.append((d, rhs))
N = len(varlist)


def consistent(subset, p):
    rows = []
    for i in subset:
        (lhs, rhs) = eqs[i]
        r = [0] * (N + 1)
        for j, co in lhs.items():
            r[j] += co % p
        r[-1] = rhs % p
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


def iis(p):
    if consistent(list(range(len(eqs))), p):
        return None
    cur = list(range(len(eqs)))
    changed = True
    while changed:
        changed = False
        for i in list(cur):
            trial = [x for x in cur if x != i]
            if not consistent(trial, p):
                cur = trial
                changed = True
                break
    return cur


for p in (3, 2):
    s = iis(p)
    if s is None:
        print("mod %d: CONSISTENT" % p)
        continue
    print("mod %d: INCONSISTENT; IIS = %d equations:" % (p, len(s)))
    for i in s:
        (lhs, rhs) = eqs[i]
        terms = " + ".join("%+d*%s" % (co, varlist[j]) for j, co in sorted(lhs.items()))
        print("   eq#%3d: %s = %d" % (i, terms, rhs))
    # the derived contradiction: RREF of the IIS
    rows = []
    for i in s:
        (lhs, rhs) = eqs[i]
        r = [0] * (N + 1)
        for j, co in lhs.items():
            r[j] += co % p
        r[-1] = rhs % p
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
            print("   => contradiction row: 0 = %d (mod %d)" % (M[i, -1], p))

# also: which equation GROUPS are involved
GRP = {}
for i in range(len(eqs)):
    (lhs, rhs) = eqs[i]
    ks = set(lhs.keys())
    if any(varlist[j][0] == 'D' for j in ks):
        GRP[i] = "wall-corner(Delta)"
    elif any(varlist[j][0] == 's' for j in ks):
        GRP[i] = "wall-corner(sigma)"
    elif any(varlist[j][0] == 'r' for j in ks):
        GRP[i] = "equivariance/w-cycles(rho_R)"
    elif any(varlist[j][0] == 'f' for j in ks):
        GRP[i] = "qshift-equiv(rho_F)"
    elif any(varlist[j][0] == 'e' for j in ks):
        GRP[i] = "qshift-equiv(rho_E)"
    else:
        GRP[i] = "closure(tau)"
for p in (3,):
    s = iis(p)
    if s:
        from collections import Counter
        print("IIS group census (mod %d): %s" % (p, Counter(GRP[i] for i in s)))
