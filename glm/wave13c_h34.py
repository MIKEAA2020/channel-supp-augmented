#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
WAVE 13C-8 : PIN THE H_3/H_4 3-ADIC EXPONENTS OF B_3
(the one number WAVE13C_SEAM.md section 5 left open: "their EXPONENTS are not
pinned by this run (would need the c4/c5 Z/9-smith)"; user directive 2026-09-10).

Method:
  1. import wave13c_seam -- the ENTIRE 13C-7 battery (G1..G8 + d_bar^2 + the
     orbit verdict) re-executes from scratch on the committed data files, an
     independent re-certification of the closed qutrit bit;
  2. extend the certified Z/9 unit-pivot smith to d4, d5, d6 of the ORBIT
     complex (coker_order9: unit pivots, 3-entry-aware below-pivot clearing,
     L-residual mod-3 rank -- the routine whose d1..d3 output pinned e_1=e_2=1);
  3. read |H_k(B_3; Z/9)| for k = 0..6 off the exact coker ladder
     (|H_k| = c_k * c_{k+1} / 9^{QK[k-1]}, with c_7 := 9^{QK[6]} = |coker(0)|);
  4. pin the 3-adic exponents e_k (H_k = Z^{beta_k} (+) Z/3^{e_k}, one 3-primary
     summand in degrees 1..4, none elsewhere) from the UCT over Z/9:
        |H_k(Z/9)| = |H_k (x) Z/9| * |Tor(H_{k-1}, Z/9)|
                   = 3^{min(e_k,2) + min(e_{k-1},2)}   (beta_k = 0, k = 1..5)
        |H_6(Z/9)| = 9 * 3^{min(e_5,2)} = 9            (H_6 = Z free)
     e_5 = 0 is forced by t_3[5] = 0, so |H_5(Z/9)| = 3^{min(e_4,2)} reads
     e_4 DIRECTLY (an independent second read of e_4 besides |H_4(Z/9)|);
  5. cross-check every pinned exponent against POINCARE DUALITY
     (B_3 = Fl_3/<c> is a closed orientable 6-manifold: G8 certified T = +1 on
     H_6; PD + UCT force Tor H_3 = Tor H_2, Tor H_4 = Tor H_1, Tor H_5 = 0):
        predicted e_3 = e_2 = 1,  e_4 = e_1 = 1,  e_5 = 0.
     PD was never used to build the complex, so agreement is a genuinely
     independent consistency certificate; disagreement would be a red flag.

Run:  python3 wave13c_h34.py   (from glm/; the import rewrites
wave13c_seam_eqs.json byte-identically). Output: wave13c_h34_output.txt.
"""
import sys
import time

T0 = time.time()
SEP = "=" * 78


def hdr(s):
    print("\n" + SEP)
    print(s)
    print(SEP)
    sys.stdout.flush()


def tick(msg):
    print("[t+%7.1fs] %s" % (time.time() - T0, msg))
    sys.stdout.flush()


print("WAVE 13C-8: importing wave13c_seam -- the full 13C-7 battery re-runs ...")
sys.stdout.flush()
import wave13c_seam as W  # noqa: E402  (the whole battery executes here)

# ---------------------------------------------------------------------------
# PART IX-a: 13C-7 re-certified on the fresh import
# ---------------------------------------------------------------------------
assert W.ALL_GATES, "battery gates failed on re-run"
assert W.H1_9 == 3 and W.H2_9 == 9, "H_1/H_2 (Z/9) orders changed"
assert W.betaQ == [1, 0, 0, 0, 0, 0, 1], "Betti vector changed"
assert W.torsQ[3] == [0, 1, 1, 1, 1, 0, 0], "t_3 vector changed"
assert all(all(v == 0 for v in W.torsQ[p]) for p in W.torsQ if p != 3)
hdr("PART IX-a: 13C-7 RE-CERTIFIED on import (all gates; H_1(Z/9)=3, H_2(Z/9)=9)")

# ---------------------------------------------------------------------------
# PART IX-b: the c4/c5/c6 Z/9-smith of the orbit complex
# ---------------------------------------------------------------------------
hdr("PART IX-b: the c4/c5/c6 Z/9-smith of the orbit complex (4970 cells)")

r4, c4 = W.coker_order9(4)
tick("coker_order9(4) done")
r5, c5 = W.coker_order9(5)
tick("coker_order9(5) done")
r6, c6 = W.coker_order9(6)
tick("coker_order9(6) done")

# the unit-pivot rank over Z/9 must equal the mod-3 rank (same assertion the
# 13C-7 run made for d1..d3)
assert r4 == W.rank_dense_modp(W.qdense_D(4, 3), 3), "rank mismatch d4"
assert r5 == W.rank_dense_modp(W.qdense_D(5, 3), 3), "rank mismatch d5"
assert r6 == W.rank_dense_modp(W.qdense_D(6, 3), 3), "rank mismatch d6"
print("unit-pivot ranks == mod-3 ranks for d4, d5, d6: OK")


def v3(x):
    n, y = 0, x
    while y % 3 == 0 and y > 1:
        y //= 3
        n += 1
    assert y == 1, "order is not a pure power of 3: %d" % x
    return n


LAD = [(W.r1, W.c1), (W.r2, W.c2), (W.r3, W.c3), (r4, c4), (r5, c5), (r6, c6)]
print("Z/9 coker ladder (every |coker d_k| is a power of 3):")
for k, (rk, ck) in enumerate(LAD, 1):
    print("  d%d: unit-pivot rank %4d,  |coker d%d| = 3^%d" % (k, rk, k, v3(ck)))

# ---------------------------------------------------------------------------
# PART IX-c: the |H_k(B_3; Z/9)| ladder (exact integers)
# ---------------------------------------------------------------------------
QK = W.QK
C = [None, W.c1, W.c2, W.c3, c4, c5, c6, 9 ** QK[6]]  # C[7] = |coker(0 -> C_6)|
H9 = [None] * 7
H9[0] = C[1]
for k in range(1, 7):
    num = C[k] * C[k + 1]
    den = 9 ** QK[k - 1]
    assert num % den == 0, "non-integral |H_%d(Z/9)|" % k
    H9[k] = num // den
    v3(H9[k])  # asserts pure power of 3
print("\n|H_k(B_3; Z/9)| machine orders (exact):")
for k in range(7):
    print("  |H_%d(B_3; Z/9)| = 3^%d = %d" % (k, v3(H9[k]), H9[k]))
assert H9[0] == 9, "connectedness"
assert H9[6] == 9, "H_6 = Z must give |H_6(Z/9)| = 9"

# ---------------------------------------------------------------------------
# PART IX-d: UCT pinning of the 3-adic exponents e_k
# ---------------------------------------------------------------------------
hdr("PART IX-d: UCT pinning (e_k = 3-adic exponent of the single 3-summand)")

beta, t3 = W.betaQ, W.torsQ[3]
h = [v3(H9[k]) for k in range(7)]
e = [None] * 7
e[0] = 0                       # H_0 = Z, no torsion
# e_5 = 0 forced: t_3[5] = 0 (no 3-primary summand in H_5)
assert t3[5] == 0 and beta[5] == 0
e[5] = 0
e[6] = None                    # H_6 = Z free, no e_6

print("k : h_k = v3|H_k(Z/9)| = min(e_k,2)+min(e_{k-1},2)   ->   e_k")
for k in range(1, 6):
    assert beta[k] == 0, "unexpected free part in H_%d" % k
    resid = h[k] - min(e[k - 1], 2)
    if resid == 0:
        e[k] = 0
    elif resid == 1:
        e[k] = 1
    else:
        e[k] = None  # resid >= 2: e_k >= 2, unresolvable by Z/9 (needs Z/27)
    print("  k = %d:  h = %d,  min(e_%d,2) = %d  ->  e_%d = %s"
          % (k, h[k], k - 1, min(e[k - 1], 2), k,
             e[k] if e[k] is not None else ">= 2 (Z/9 cannot resolve)"))
# degree 6 closes the ladder: |H_6(Z/9)| = 9 * 3^{min(e_5,2)} = 9
assert h[6] == 2 + min(e[5], 2), "degree-6 UCT inconsistency"
print("  k = 6:  h = 2 + min(e_5,2) = %d  (consistent, H_6 = Z)" % h[6])

# the two independent reads of e_4: |H_5(Z/9)| = 3^{min(e_4,2)} (e_5 = 0)
# and |H_4(Z/9)| = 3^{min(e_4,2)+min(e_3,2)}
read_a = h[5]                        # = min(e_4, 2)
read_b = h[4] - min(e[3], 2) if e[3] is not None else None
print("\ntwo independent reads of min(e_4,2):  |H_5(Z/9)|-read = %d,  "
      "|H_4(Z/9)|-read = %s" % (read_a, read_b))
assert read_b is None or read_a == read_b, "e_4 reads disagree"

# ---------------------------------------------------------------------------
# PART IX-e: Poincare-duality cross-check (independent prediction)
# ---------------------------------------------------------------------------
hdr("PART IX-e: Poincare-duality cross-check (independent of the build)")

# B_3 = Fl_3/<c>: closed orientable 6-manifold (free C_3 action, G8 T = +1 on
# H_6).  PD + UCT: Tor H_k = Tor H_{n-k-1} (n = 6):
#   Tor H_3 = Tor H_2   ->  e_3 = e_2
#   Tor H_4 = Tor H_1   ->  e_4 = e_1
#   Tor H_5 = Tor H_0 = 0  ->  e_5 = 0   (also beta_4 = beta_2, beta_5 = beta_1)
PD_PRED = {3: ("e_3 = e_2", e[2]), 4: ("e_4 = e_1", e[1]), 5: ("e_5 = 0", 0)}
pd_ok = True
for k in sorted(PD_PRED):
    label, pred = PD_PRED[k]
    got = e[k]
    ok = (got == pred)
    pd_ok = pd_ok and ok
    print("  PD predicts %-8s = %s ;  machine pin e_%d = %s  :  %s"
          % (label.split(" = ")[0], pred, k,
             got if got is not None else ">=2?", "MATCH" if ok else "MISMATCH"))
assert beta[4] == beta[2] and beta[5] == beta[1], "free-part PD violation"
print("  free parts: beta_4 = beta_2 = %d, beta_5 = beta_1 = %d : MATCH"
      % (beta[4], beta[1]))
print("POINCARE DUALITY CROSS-CHECK: %s" % ("ALL MATCH" if pd_ok else "MISMATCH -- RED FLAG"))

# ---------------------------------------------------------------------------
# PART IX-f: extended mod-p torsion scan (audit hardening)
# ---------------------------------------------------------------------------
# The 13C-7 torsion scan covered p in {2,3,5,7,11,13}. For B_3 the slots
# H_0, H_1, H_5, H_6 are forced exactly (pi_1 = C_3 -> H_1 = Z/3; PD ->
# Tor H_4 = Tor H_1, H_5 = 0, H_6 = Z), but a hypothetical large prime could
# still hide in the (H_2, H_3) pair (PD pairs them). Extend the scan.
hdr("PART IX-f: extended mod-p torsion scan, p in {17..61} (hardening 'no p != 3')")

PRIMES_X = [17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61]
for p in PRIMES_X:
    tp = [0] * 7
    prev = 0
    for k in range(7):
        rka = W.rank_dense_modp(W.qdense_D(k, p), p)
        rkb = W.rank_dense_modp(W.qdense_D(k + 1, p), p)
        bp = QK[k] - rka - rkb
        tp[k] = bp - beta[k] - prev
        prev = tp[k]
    clean = all(v == 0 for v in tp)
    print("  p = %2d:  t_p = %s  :  %s" % (p, tp, "clean" if clean else "TORSION FOUND"))
    assert clean, "unexpected %d-torsion: %s" % (p, tp)
print("extended scan p = 17..61: NO p != 3 torsion in any degree (B_3)")
tick("extended prime scan done")

# ---------------------------------------------------------------------------
# VERDICT
# ---------------------------------------------------------------------------
hdr("VERDICT: the H_3/H_4 exponents are pinned (WAVE13C_SEAM.md s.5 caveat closed)")

grp = []
for k in range(7):
    if beta[k] == 1 and t3[k] == 0:
        grp.append("Z")
    elif beta[k] == 0 and t3[k] == 0:
        grp.append("0")
    elif beta[k] == 0 and t3[k] == 1:
        grp.append("Z/3" if e[k] == 1 else ("Z/3^%s" % e[k] if e[k] else "Z/3^{>=2}"))
    else:
        grp.append("UNEXPECTED")
print("H_*(B_3) = (%s)" % ", ".join(grp))
print("  every slot: beta + t_p (p in {2,3,5,7,11,13}) + e_k (this run) + PD cross-check")
if e[3] == 1 and e[4] == 1 and pd_ok:
    print("\nFINAL: H_3(B_3) = Z/3 and H_4(B_3) = Z/3, exponents e_3 = e_4 = 1 "
          "MACHINE-PINNED (c4/c5/c6 Z/9-smith), PD-consistent.")
    print("  H_2(B_3) = Z/3 unchanged; the qutrit bit and its verdict are unaffected.")
else:
    print("\nHONEST STOP: exponents not cleanly pinned -- inspect the output above.")

tick("run complete")
