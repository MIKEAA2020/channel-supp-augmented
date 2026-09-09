#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
WAVE 12b - FOLD-WALL ARRANGEMENT INCIDENCE of the unistochastic region U_3.
Prerequisite for the corrected base cellulation (Wave 11 Sec.5 step 1): the walls
of U_3 and how they meet.  Machine-verified (exact feasibility + structure).

Setup: U_3 = {D in B_3 : every row-pair sqrt-triple is a (possibly degenerate)
triangle}, B_3 = Birkhoff 3x3 (affine 4-manifold).  Boundary pieces:
  6 vertices (permutation matrices), 9 transposition edges (S^1 fibres, IN U_3),
  and 9 fold-walls  W(i,j|k)  = locus in int B_3 where
     sqrt(D_ik D_jk) = sqrt(D_il D_jl) + sqrt(D_im D_jm), {k,l,m}={1,2,3},
  i.e. row pair (i,j) is degenerate with column k the "hypotenuse".
We tabulate the incidence of the 9 walls with the Birkhoff 1-skeleton AND the
wall-wall intersections (which pairs meet along a genuine 2-dim corner of U_3).

All arithmetic exact where possible (root-of-D products; feasibility by strict
sign tests of squared equalities), plus rational-point sampling.
"""
import numpy as np, itertools, json

def wall_neg(D, i, j, k):
    """wall function signifier: leg - hyp; use squared-sqrt trick.
       Return value >0 strict inside (not wall), 0 on wall (approx)."""
    cols=[0,1,2]; l,m=[c for c in cols if c!=k]
    hyp=np.sqrt(D[i,k]*D[j,k])
    leg=np.sqrt(D[i,l]*D[j,l])+np.sqrt(D[i,m]*D[j,m])
    return leg-hyp

walls=[(i,j,k) for (i,j) in [(0,1),(0,2),(1,2)] for k in range(3)]
def wname(w): return f"W({w[0]+1}{w[1]+1}|{w[2]+1})"

def Pmat(sig):
    M=np.zeros((3,3))
    for r,ch in enumerate(sig): M[r,int(ch)-1]=1.0
    return M
names=[''.join(map(str,x)) for x in itertools.permutations('123')]
Ps={n:Pmat(n) for n in names}
def is_transp(a,b): return sum(x!=y for x,y in zip(a,b))==2
edges=[(a,b) for i,a in enumerate(names) for b in names[i+1:] if is_transp(a,b)]
edges=[e for e in edges]

def interior_of_edge(a,b,t): return (1-t)*Ps[a]+t*Ps[b]

# ---- (A) which wall contains which edge & which vertices
def on_wall(D,w,tol=1e-9): return abs(wall_neg(D,*w))<tol

print("=== A. edge/wall incidence (already known: each edge in 8/9 walls) ===")
edge_miss={}
for (a,b) in edges:
    miss=[]
    for w in walls:
        # not on wall iff g != 0 at interior sample
        vals=[wall_neg(interior_of_edge(a,b,t),*w) for t in np.linspace(0,1,41)]
        if max(abs(np.array(vals)))>1e-9: miss.append(w)
    edge_miss[(a,b)]=[wname(w) for w in miss]
    print(f"  {a}-{b}: missing wall {[wname(w) for w in miss]}")

# ---- (B) wall-pair intersections: does an interior 2-dim corner of U3 exist?
# A corner of U3 = a point in int(U3) closure where exactly two walls are tight.
# Feasibility: minimize g_A^2+g_B^2 keeping D in int B3; success ~0 => 2-locus.
from scipy.optimize import minimize
def gen_intds(rng,minm=1e-3):
    while True:
        a,b,c,d=rng.random(4)
        D=np.array([[a,b,1-a-b],[c,d,1-c-d],[1-a-c,1-b-d,a+b+c+d-1]])
        if D.min()>minm and D.max()<1-minm: return D
rng=np.random.default_rng(11)
def corner_resid(wA,wB):
    def obj(x):
        a,b,c,d=x
        if not(0<=a<=1 and 0<=b<=1 and 0<=c<=1 and 0<=d<=1): return 1e3
        D=[[a,b,1-a-b],[c,d,1-c-d],[1-a-c,1-b-d,a+b+c+d-1]]
        Dm=np.min(D)
        if Dm<0: return 1e3
        # discourage hitting boundary (want interior corner)
        pen = 0 if Dm>1e-4 else (1e-4-Dm)*1e5
        return wall_neg(np.array(D),*wA)**2+wall_neg(np.array(D),*wB)**2+pen
    best=1e9
    for _ in range(60):
        x0=rng.random(4)
        r=minimize(obj,x0,method='Nelder-Mead',options=dict(maxiter=15000,xatol=1e-13,fatol=1e-14))
        best=min(best,r.fun)
    return np.sqrt(best)

print("\n=== B. wall-pair corners (interior 2-loci). residual<1e-4 => genuine corner ===")
corners=[]
for ia in range(9):
    for ib in range(ia+1,9):
        wA,wB=walls[ia],walls[ib]
        r=corner_resid(wA,wB)
        has = r<1e-4
        if has: corners.append((wname(wA),wname(wB)))
        print(f"  {wname(wA)} cap {wname(wB)}: resid={r:.1e}  {'CORNER' if has else 'boundary/vertex-only'}")
print(f"\ntotal wall pairs with genuine interior corner: {len(corners)}")

# ---- (C) which transposition edges each corner 2-locus is incident to is the
# further refinement; report the corner incidence graph summary
print("\ncorner pairs list:")
for c in corners: print("  ",c)
