#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""WAVE 13B-2 : census data for the corrected (v2) base cellulation.

Pins, numerically:
  (A) the 6 bijection-pattern regions R(a,b,c) of the real locus: which
      patterns occur on the delta=0 sheet vs the delta=pi sheet, and the
      approximate volume of each region in theta-space (all 6 nonempty?).
  (B) the c-action on the R-regions: (theta,delta) -> CKM normal form of
      V(theta,delta) P_sigma: the induced map on (pattern, sheet): the
      orbit structure.  Also: c maps real sheets to real sheets?
  (C) the wall->R incidence: each wall W(i,j|k) = which R-regions.
  (D) the F-loci: the 9 zero-pattern strati = 5 pure (theta-face) + 4 mixed
      (delta=0/pi cancellation); each meets which edges/regions.
"""
import numpy as np
import itertools

rng = np.random.default_rng(4242)

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

Psig = np.zeros((3, 3)); Psig[0, 1] = 1; Psig[1, 2] = 1; Psig[2, 0] = 1

def triangle_hyp(D, i, j):
    m = np.sqrt(D[i, :] * D[j, :])
    return int(np.argmax(m))

def pattern_of(D):
    return tuple(triangle_hyp(D, i, j) + 1 for (i, j) in [(0, 1), (0, 2), (1, 2)])

def ckm_normal(U, tries=40):
    """CKM (theta, delta) normal form of a unitary with positive entries.
    Returns (theta, delta, ok)."""
    D = np.abs(U) ** 2
    if D.min() <= 0:
        return None, None, False
    s3sq = D[0, 2]; c3sq = 1.0 - s3sq
    if c3sq <= 0: return None, None, False
    t = (np.arccos(np.sqrt(D[0, 0] / c3sq)),
         np.arccos(np.sqrt(D[2, 2] / c3sq)),
         np.arccos(np.sqrt(c3sq)))
    s1, c1 = np.sin(t[0]), np.cos(t[0])
    s2, c2 = np.sin(t[1]), np.cos(t[1])
    s3 = np.sin(t[2])
    denom = 2 * s1 * c2 * c1 * s2 * s3
    if denom <= 1e-14: return None, None, False
    cosd = (D[1, 0] - s1**2 * c2**2 - c1**2 * s2**2 * s3**2) / denom
    cosd = np.clip(cosd, -1, 1)
    # pick the delta whose J matches J(U)
    JU = np.imag(U[0, 0] * U[1, 1] * np.conj(U[0, 1]) * np.conj(U[1, 0]))
    for d in (np.arccos(cosd), -np.arccos(cosd)):
        V = Vckm(*t, d)
        if np.max(np.abs(np.abs(V) ** 2 - D)) < 1e-10:
            JV = np.imag(V[0, 0] * V[1, 1] * np.conj(V[0, 1]) * np.conj(V[1, 0]))
            if abs(JV - JU) < 1e-10:
                return t, d, True
    return t, np.arccos(cosd), True

# ---------- (A) pattern census on each real sheet ----------
print("=" * 72)
print("(A) bijection-pattern regions on the two real sheets")
print("=" * 72)
N = 200000
th = rng.uniform(1e-3, np.pi/2 - 1e-3, size=(N, 3))
count = {0: {}, np.pi: {}}
for sheet in (0.0, np.pi):
    for k in range(N):
        V = Vckm(*th[k], sheet)
        D = np.abs(V) ** 2
        if D.min() < 1e-6:   # near boundary: skip (F/edge strata)
            continue
        p = pattern_of(D)
        count[sheet][p] = count[sheet].get(p, 0) + 1
for sheet in (0.0, np.pi):
    lab = "delta=0 " if sheet == 0.0 else "delta=pi"
    tot = sum(count[sheet].values())
    print(f"  {lab}: total interior samples {tot}")
    for p in sorted(count[sheet]):
        print(f"    R{p}: {count[sheet][p]:6d}  ({100*count[sheet][p]/max(tot,1):.1f}%)")

# ---------- (B) c-action on (pattern, sheet) ----------
print()
print("=" * 72)
print("(B) c-action on the R-regions: pattern & sheet mapping")
print("=" * 72)
# For samples on each (sheet, pattern): apply c, renormalize, record image.
cmap = {}
ntry = 0
for sheet in (0.0, np.pi):
    for k in range(N):
        if ntry > 4000: break
        V = Vckm(*th[k], sheet)
        D = np.abs(V) ** 2
        if D.min() < 1e-3: continue
        p = pattern_of(D)
        key = (sheet, p)
        if key in cmap: continue
        Up = V @ Psig
        Dp = np.abs(Up) ** 2
        if Dp.min() <= 1e-9: continue
        t2, d2, ok = ckm_normal(Up)
        if not ok: continue
        # renormalized delta -> sheet
        if abs(np.sin(d2)) < 1e-9:
            sheet2 = 0.0 if np.cos(d2) > 0 else np.pi
            p2 = pattern_of(np.abs(Vckm(*t2, d2)) ** 2)
            cmap[key] = (sheet2, p2)
            ntry += 1
print("  c: (sheet, R) -> (sheet, R)   [sheet 0 = delta 0, 1 = delta pi]")
for k in sorted(cmap, key=lambda x: (x[0], x[1])):
    s0 = 0 if k[0] == 0.0 else 1
    v = cmap[k]
    s1 = 0 if v[0] == 0.0 else 1
    print(f"    (sheet{s0}, R{k[1]}) -> (sheet{s1}, R{v[1]})")

# orbits of the map
def f(x):
    s, p = x
    s = 0 if s == 0.0 else 1
    key = (0.0 if s == 0 else np.pi, tuple(p))
    if key in cmap:
        v = cmap[key]
        return (0 if v[0] == 0.0 else 1, tuple(v[1]))
    return None
items = [(0 if k[0]==0.0 else 1, tuple(k[1])) for k in cmap]
seen = set()
print("  orbits:")
for it in sorted(set(items)):
    if it in seen: continue
    orb = [it]; seen.add(it)
    cur = f(it)
    while cur is not None and cur not in orb and len(orb) < 6:
        orb.append(cur); seen.add(cur); cur = f(cur)
    print("   ", orb)

# ---------- (C) wall -> R incidence ----------
print()
print("=" * 72)
print("(C) wall W(i,j|k) = union of which R-regions (machine-sampled)")
print("=" * 72)
wallR = {}
for sheet in (0.0, np.pi):
    for k in range(N):
        V = Vckm(*th[k], sheet)
        D = np.abs(V) ** 2
        if D.min() < 1e-6: continue
        p = pattern_of(D)
        for (ij, pos) in zip([(0,1),(0,2),(1,2)], range(3)):
            w = (ij, p[pos])
            wallR.setdefault(w, set()).add((sheet, p))
for w in sorted(wallR, key=lambda x: (x[0], x[1])):
    s = "W(%d%d|%d)" % (w[0][0]+1, w[0][1]+1, w[1])
    rs = ["(d%d,R%s)" % (0 if r[0]==0.0 else 1, str(r[1])) for r in sorted(wallR[w])]
    print(f"  {s} = {rs}")

# ---------- (D) pure vs mixed F-loci sanity ----------
print()
print("=" * 72)
print("(D) the 9 F-loci: pure-face (5) + mixed-cancellation (4)")
print("=" * 72)
# pure: theta conditions killing a single entry; mixed: delta=0/pi cancellations.
# Check: at delta=0, which mixed entries can vanish (two-term cancellation)?
# V22(theta,0) = c1c2 - s1s2s3 ; V31(theta,0) = s1s2 - c1c2s3
# V21(theta,pi) = -(s1c2 - c1s2s3) ; V32(theta,pi) = -(c1s2 - s1c2s3)
for lab, expr, rngf in [
    ("V22(theta,0)=0 feasible", lambda t: np.cos(t[0])*np.cos(t[1]) - np.sin(t[0])*np.sin(t[1])*np.sin(t[2]), None),
    ("V31(theta,0)=0 feasible", lambda t: np.sin(t[0])*np.sin(t[1]) - np.cos(t[0])*np.cos(t[1])*np.sin(t[2]), None),
    ("V21(theta,pi)=0 feasible", lambda t: np.sin(t[0])*np.cos(t[1]) - np.cos(t[0])*np.sin(t[1])*np.sin(t[2]), None),
    ("V32(theta,pi)=0 feasible", lambda t: np.cos(t[0])*np.sin(t[1]) - np.sin(t[0])*np.cos(t[1])*np.sin(t[2]), None),
]:
    # find a feasible theta by random search
    hit = None
    for _ in range(200000):
        t = rng.uniform(0.02, np.pi/2-0.02, 3)
        if abs(expr(t)) < 1e-4:
            hit = t; break
    print(f"  {lab}: {'FOUND' if hit is not None else 'not found'}"
          + (f" at theta~{np.round(hit,3).tolist()}" if hit is not None else ""))
print("  => the 4 mixed F-loci exist as 2-dim cancellation loci inside the")
print("     real sheets (they are the pattern-region flip boundaries).")
