#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Diagnose the dT=Td residuals of the seam assembly (which cells, what terms)."""
import sys

src = open("wave13c_seam.py").read()
cut = src.index('GATES = {"G1": True, "G2": True')
pre = src[:cut]
g = {}
exec(compile(pre, "seam_pre", "exec"), g)

D = g["D"]
TSUP = g["TSUP"] if "TSUP" in g else None
CELLS = g["CELLS"]
CELLI = g["CELLI"]
DEG = g["DEG"]
CMAP = g["CMAP"]
SB = g["SB"]
KAPPA_F = g["KAPPA_F"]
KAPPA_R = g["KAPPA_R"]
KAPPA_E = g["KAPPA_E"]
MOD = g["MOD"]
T2CELLS = g["T2CELLS"]
t2_tr = g["t2_tr"]
cellname = g["cellname"]
TT = g["TT"]
h_mu = g["h_mu"]
W_RF = g["W_RF"]
MIX = g["MIX"]
WALLS = g["WALLS"]
RLO = g["RLO"]
RHI = g["RHI"]
WFI = g["WFI"]
seam_theta_sign = g["seam_theta_sign"]
WDIR = g["WDIR"]
TT0SQ = g["TT0SQ"]
TT0S = g["TT0S"]
t2_bound = g["t2_bound"]
NC = g["NC"]


def t_shift(cid):
    if cid < 6:
        return None
    if cid < 15:
        return ('s1', KAPPA_E[cid - 6])
    if cid < 24:
        return ('t2', KAPPA_F[cid - 15])
    if cid < 30:
        return ('t2', KAPPA_R[cid - 24])
    return ('t2', TT0SQ if cid == 30 else TT0S)


def tmap(idx):
    cid, fc = CELLS[idx]
    tgt = CMAP[cid]
    sh = t_shift(cid)
    if cid < 6:
        nfc = fc
    elif sh is None:
        nfc = fc
    elif sh[0] == 't2':
        nfc = t2_tr(fc, sh[1][0], sh[1][1])
    else:
        nfc = (fc[0], (fc[1] + sh[1]) % MOD)
    return CELLI[(tgt, nfc)], SB[cid]


def sheet_terms_raw(si, fc):
    """the prism/seam chain terms of d(s_si, fc) as (F-index, chain)."""
    out = []
    for w in WALLS:
        lo, hi = RLO[w], RHI[w]
        fi = WFI[w]
        wlo = W_RF.get((lo, fi), (0, 0))
        whi = W_RF.get((hi, fi), (0, 0))
        sig = g["SIG"][si][w]
        mu = ((TT[si][hi][0] + whi[0] - sig[0]) % MOD,
              (TT[si][hi][1] + whi[1] - sig[1]) % MOD)
        ch = h_mu(mu, t2_tr(fc, sig[0], sig[1]))
        sgn = seam_theta_sign(si, lo, fi)
        out.append((fi, sgn, ch, mu, sig))
    for (fi, ra, rb) in MIX:
        wa = W_RF.get((ra, fi), (0, 0))
        wb = W_RF.get((rb, fi), (0, 0))
        start = ((TT[si][rb][0] + wb[0]) % MOD, (TT[si][rb][1] + wb[1]) % MOD)
        mu = ((TT[si][ra][0] + wa[0] - start[0]) % MOD,
              (TT[si][ra][1] + wa[1] - start[1]) % MOD)
        ch = h_mu(mu, t2_tr(fc, start[0], start[1]))
        sgn = -seam_theta_sign(si, ra, fi)
        out.append((fi, sgn, ch, mu, start))
    return out


# classify failing cells
badcells = {}
for idx in range(NC):
    cid, fc = CELLS[idx]
    k = DEG[idx]
    if k == 0 or cid < 24 or cid >= 32:
        # only diagnose the sheet cells (the prism-equivariance)
        pass
    if not (30 <= cid < 32):
        continue
    # T(d(cell)):
    acc = {}
    for j, co in D[idx].items():
        tj, tsg = tmap(j)
        acc[tj] = acc.get(tj, 0) + co * tsg
    acc = {a: b for a, b in acc.items() if b != 0}
    acc2 = {}
    tj, tsg = tmap(idx)
    for j, co in D[tj].items():
        acc2[j] = acc2.get(j, 0) + co * tsg
    acc2 = {a: b for a, b in acc2.items() if b != 0}
    if acc != acc2:
        si = cid - 30
        key = (si, fc[0])
        badcells[key] = badcells.get(key, 0) + 1

print("failing sheet cells by (sheet, fibre-type): %s" % dict(sorted(badcells.items())))
print("total failing sheet cells: %d" % sum(badcells.values()))

# for ONE failing cell of each type, show the mismatching terms
shown = set()
for idx in range(NC):
    cid, fc = CELLS[idx]
    if not (30 <= cid < 32):
        continue
    if (cid - 30, fc[0]) not in badcells or (cid - 30, fc[0]) in shown:
        continue
    acc = {}
    for j, co in D[idx].items():
        tj, tsg = tmap(j)
        acc[tj] = acc.get(tj, 0) + co * tsg
    acc = {a: b for a, b in acc.items() if b != 0}
    acc2 = {}
    tj, tsg = tmap(idx)
    for j, co in D[tj].items():
        acc2[j] = acc2.get(j, 0) + co * tsg
    acc2 = {a: b for a, b in acc2.items() if b != 0}
    diffs = []
    for kk in set(acc) | set(acc2):
        if acc.get(kk, 0) != acc2.get(kk, 0):
            diffs.append((kk, acc.get(kk, 0), acc2.get(kk, 0)))
    print("\nsheet cell (s%d, %s)  T-target=(%s): %d differing terms" %
          (cid - 30, fc, cellname(CELLS[tmap(idx)[0]][0]), len(diffs)))
    for (kk, a, b) in diffs[:8]:
        print("   cell %s (%s, %s): Td-coef %d  vs  dT-coef %d" %
              (kk, cellname(CELLS[kk][0]), CELLS[kk][1], a, b))
    shown.add((cid - 30, fc[0]))
    if len(shown) >= 4:
        break
