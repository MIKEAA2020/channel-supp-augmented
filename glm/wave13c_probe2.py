#!/usr/bin/env python3
import numpy as np

PSIG = np.zeros((3, 3)); PSIG[0, 1] = 1; PSIG[1, 2] = 1; PSIG[2, 0] = 1
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


def phase_solve(U, V, tol=0.03, ctol=1e-6):
    cons = []
    for i in range(3):
        for j in range(3):
            if abs(U[i, j]) > tol and abs(V[i, j]) > tol:
                cons.append((i, j, float(np.angle(U[i, j] / V[i, j]))))
    if not cons:
        return None
    L = [None] * 3
    R = [None] * 3
    adj = {}
    for (i, j, a) in cons:
        adj.setdefault(("r", i), []).append((("c", j), a, i, j))
        adj.setdefault(("c", j), []).append((("r", i), a, i, j))
    seen = set()
    for start in [("r", 0), ("r", 1), ("r", 2)]:
        if start in seen or adj.get(start) is None:
            continue
        L[start[1]] = 0.0
        seen.add(start)
        frontier = [start]
        while frontier:
            nxt = []
            for node in frontier:
                for (other, a, i, j) in adj.get(node, []):
                    if other in seen:
                        continue
                    if node[0] == "r":
                        R[j] = (a - L[i]) % (2 * np.pi)
                    else:
                        L[i] = (a - R[j]) % (2 * np.pi)
                    seen.add(other)
                    nxt.append(other)
            frontier = nxt
    if any(x is None for x in L):
        return None
    return np.array(L)


def uv_shift(L):
    return (((L[1] - L[0]) / (2 * np.pi)) % 1.0, ((L[2] - L[1]) / (2 * np.pi)) % 1.0)


print("=== F1-wall (th1=0) -> F5-image: translation vs delta (fixed thetas) ===")
for dd in (0.0, 0.15, 0.3, 1.0, 2.0, np.pi - 0.3, np.pi - 0.15, np.pi):
    th = [0.0, 0.7, 1.1]
    U = Vckm(th[0], th[1], th[2], dd) @ PSIG
    D = np.abs(U) ** 2
    # F5 rep params: u = arccos(sqrt(D00)), v = arcsin(sqrt(D12))
    uu = float(np.arccos(np.sqrt(D[0, 0])))
    vv = float(np.arcsin(np.sqrt(D[1, 2])))
    Vt = Vckm(uu, vv, 0.0, 0.0)
    L = phase_solve(U, Vt)
    if L is None:
        print("delta=%.4f  None" % dd)
        continue
    s = uv_shift(L)
    print("delta=%.4f  u,v sixths = (%.4f, %.4f)" % (dd, s[0] * 6, s[1] * 6))

print("\n=== F2-wall (th1=pi/2) -> F1-image ===")
for dd in (0.0, 0.3, np.pi - 0.3, np.pi):
    th = [PI2, 0.7, 1.1]
    U = Vckm(th[0], th[1], th[2], dd) @ PSIG
    D = np.abs(U) ** 2
    uu = float(np.arcsin(np.sqrt(D[2, 0])))
    vv = float(np.arccos(np.sqrt(D[0, 1])))
    Vt = Vckm(0.0, uu, vv, 0.0)
    L = phase_solve(U, Vt)
    if L is None:
        print("delta=%.4f  None" % dd)
        continue
    s = uv_shift(L)
    print("delta=%.4f  u,v sixths = (%.4f, %.4f)" % (dd, s[0] * 6, s[1] * 6))

print("\n=== F3-wall (th2=0) -> F8-image (mixed, delta=pi rep) ===")
for dd in (0.0, 0.3, np.pi - 0.3, np.pi):
    th = [0.5, 0.0, 1.0]
    U = Vckm(th[0], th[1], th[2], dd) @ PSIG
    D = np.abs(U) ** 2
    s3 = float(np.sqrt(D[0, 2]))
    c1 = float(np.sqrt(np.clip(D[0, 0] / (1.0 - D[0, 2]), 0, 1)))
    s1 = np.sqrt(max(0.0, 1 - c1 * c1))
    uu = float(np.arccos(c1))
    vv = float(np.arcsin(s3))
    t2 = np.arctan(s1 / max(c1 * s3, 1e-300))
    Vt = Vckm(uu, t2, vv, np.pi)
    L = phase_solve(U, Vt)
    if L is None:
        print("delta=%.4f  None" % dd)
        continue
    s = uv_shift(L)
    print("delta=%.4f  u,v sixths = (%.4f, %.4f)" % (dd, s[0] * 6, s[1] * 6))

print("\n=== F5-wall (th3=0) -> F2-image ===")
for dd in (0.0, 0.3, np.pi - 0.3, np.pi):
    th = [0.5, 0.7, 0.0]
    U = Vckm(th[0], th[1], th[2], dd) @ PSIG
    D = np.abs(U) ** 2
    uu = float(np.arcsin(np.sqrt(D[2, 0])))
    vv = float(np.arccos(np.sqrt(D[0, 1])))
    Vt = Vckm(PI2, uu, vv, 0.0)
    L = phase_solve(U, Vt)
    if L is None:
        print("delta=%.4f  None" % dd)
        continue
    s = uv_shift(L)
    print("delta=%.4f  u,v sixths = (%.4f, %.4f)" % (dd, s[0] * 6, s[1] * 6))

print("\n=== F4-wall (th2=pi/2) -> F7-image (mixed, delta=0 rep) ===")
for dd in (0.0, 0.3, np.pi - 0.3, np.pi):
    th = [0.5, PI2, 1.0]
    U = Vckm(th[0], th[1], th[2], dd) @ PSIG
    D = np.abs(U) ** 2
    s3 = float(np.sqrt(D[0, 2]))
    c1 = float(np.sqrt(np.clip(D[0, 0] / (1.0 - D[0, 2]), 0, 1)))
    s1 = np.sqrt(max(0.0, 1 - c1 * c1))
    uu = float(np.arccos(c1))
    vv = float(np.arcsin(s3))
    t2 = np.arctan(c1 * s3 / max(s1, 1e-300))
    Vt = Vckm(uu, t2, vv, 0.0)
    L = phase_solve(U, Vt)
    if L is None:
        print("delta=%.4f  None" % dd)
        continue
    s = uv_shift(L)
    print("delta=%.4f  u,v sixths = (%.4f, %.4f)" % (dd, s[0] * 6, s[1] * 6))
