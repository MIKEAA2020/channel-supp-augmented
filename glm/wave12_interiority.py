#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""WAVE 12b-3 : reconcile corner semantics. Distinguish GENUINE interior corners
(D strictly inside B3, i.e. every entry in (0,1)) from boundary coincidences
(points with some entry ~0, i.e. on the Birkhoff boundary / a 2-face or edge).
Re-examine every wall pair and every 3-wall candidate with a strict interiority
requirement (all nine entries bounded away from 0 and 1).
"""
import numpy as np
from scipy.optimize import minimize
walls=[(i,j,k) for (i,j) in [(0,1),(0,2),(1,2)] for k in range(3)]
def wall_neg(D,i,j,k):
    cols=[0,1,2]; l,m=[c for c in cols if c!=k]
    return np.sqrt(D[i][k]*D[j][k])-np.sqrt(D[i][l]*D[j][l])-np.sqrt(D[i][m]*D[j][m])
rng=np.random.default_rng(21)
def search(ws, interior, mode='resid'):
    """ws list of walls; interior=True forces entries in (lo,hi). Return resid & min-entry."""
    lo=0.02 if interior else 1e-9
    def obj(x):
        a,b,c,d=x
        if not(lo<=a<=1-lo and lo<=b<=1-lo and lo<=c<=1-lo and lo<=d<=1-lo): return 1e4
        D=np.array([[a,b,1-a-b],[c,d,1-c-d],[1-a-c,1-b-d,a+b+c+d-1]])
        if D.min()<lo or D.max()>1-lo: return 1e4
        return sum(wall_neg(D,*w)**2 for w in ws)
    best=1e9; bestx=None
    for _ in range(120):
        x0=rng.random(4)
        r=minimize(obj,x0,method='Nelder-Mead',options=dict(maxiter=30000,xatol=1e-15,fatol=1e-16))
        if r.fun<best: best=r.fun;bestx=r.x
    D=None
    if bestx is not None:
        a,b,c,d=bestx
        D=np.array([[a,b,1-a-b],[c,d,1-c-d],[1-a-c,1-b-d,a+b+c+d-1]])
    return np.sqrt(best), (D.min() if D is not None else -1)

def rowpair(w): return (w[0],w[1])
def hyp(w): return w[2]
wn=lambda w:f"W({w[0]+1}{w[1]+1}|{w[2]+1})"

# (i) pairs: interior corner exists?
print("PAIR analysis: 'interior corner' = 2-wall coincidence with all 9 entries in (0.02,0.98)")
interior_corners=[]
boundary_only=[]
for ia in range(9):
    for ib in range(ia+1,9):
        wA,wB=walls[ia],walls[ib]
        res,minent=search([wA,wB],True)
        diff_row=rowpair(wA)!=rowpair(wB); diff_hyp=hyp(wA)!=hyp(wB)
        if res<1e-6 and minent>0.02:
            interior_corners.append((wn(wA),wn(wB)))
        elif res<1e-6:
            boundary_only.append((wn(wA),wn(wB)))
print("genuine INTERIOR corner pairs:",len(interior_corners))
for c in interior_corners: print("   ",c)
print("pairs that coincide but ONLY near boundary (some entry ~0):",len(boundary_only))
for c in boundary_only[:20]: print("   ",c)

# verify rook rule
ok=True
for c in interior_corners:
    # parse
    pass
# check rule precisely
pred=[]
for ia in range(9):
    for ib in range(ia+1,9):
        if rowpair(walls[ia])!=rowpair(walls[ib]) and hyp(walls[ia])!=hyp(walls[ib]):
            pred.append((wn(walls[ia]),wn(walls[ib])))
print("\nrook-rule predicted interior corners:",len(pred), " actual:",len(interior_corners))
print("match:", sorted(pred)==sorted(interior_corners))

# (ii) triples with strict interiority
print("\nTRIPLE interior points (3 walls, all 9 entries interior):")
trips=[]
for iw in range(9):
    for jw in range(iw+1,9):
        for kw in range(jw+1,9):
            ws=[walls[iw],walls[jw],walls[kw]]
            res,minent=search(ws,True)
            if res<1e-6 and minent>0.02:
                trips.append((res,minent,[wn(w) for w in ws]))
print("interior triple points:",len(trips))
for res,me,ts in trips: print("   res",f"{res:.1e}","minent",f"{me:.3f}",ts)
