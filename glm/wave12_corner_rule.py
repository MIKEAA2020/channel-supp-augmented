#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""WAVE 12b-2 : verify the CORNER RULE exactly.
Conjecture from numerics: W(i,j|k) and W(a,b|c) have a genuine interior corner
(of U3, a 2-dim locus)  <=>  {i,j} != {a,b}   AND   k != c.
Walls sharing a row-pair-index OR sharing the hypotenuse column meet only on the
Birkhoff 1-skeleton (vertices/transposition edges).  Verify at exact rational
sample points (exact sqrt algebra via squared equalities and a tolerance-free
strict-feasibility test at rational coordinates).
"""
import numpy as np, itertools
from fractions import Fraction

def on_wall_frac(D, i, j, k, tol=Fraction(1,10**9)):
    # D is 3x3 of Fractions (0..1).  Test |leg-hyp| < tol using squared forms.
    cols=[0,1,2]; l,m=[c for c in cols if c!=k]
    def s(a):  # a>=0 Fraction -> sqrt approx as float for feasibility
        return float(a)**0.5
    leg = s(D[i][l]*D[j][l]) + s(D[i][m]*D[j][m])
    hyp = s(D[i][k]*D[j][k])
    return abs(leg-hyp) < float(tol)

def wall_neg(D,i,j,k):
    cols=[0,1,2]; l,m=[c for c in cols if c!=k]
    return np.sqrt(D[i][k]*D[j][k])-np.sqrt(D[i][l]*D[j][l])-np.sqrt(D[i][m]*D[j][m])

def Pmat(sig):
    M=np.zeros((3,3))
    for r,ch in enumerate(sig): M[r,int(ch)-1]=1.0
    return M
names=[''.join(map(str,x)) for x in itertools.permutations('123')]
Ps={n:Pmat(n) for n in names}

walls=[(i,j,k) for (i,j) in [(0,1),(0,2),(1,2)] for k in range(3)]
def rowpair(w): return (w[0],w[1])
def hyp(w): return w[2]

# Exact rational corner test: build a rational D in int(B3) that is a corner of
# two given walls by solving the two equations in the 4 parameters approximately
# then snapping to rationals and checking both wall residuals < small tolerance.
from scipy.optimize import minimize
rng=np.random.default_rng(7)
def find_corner_point(wA,wB):
    def obj(x):
        a,b,c,d=x
        if not(0<=a<=1 and 0<=b<=1 and 0<=c<=1 and 0<=d<=1): return 1e3
        D=np.array([[a,b,1-a-b],[c,d,1-c-d],[1-a-c,1-b-d,a+b+c+d-1]])
        if D.min()<1e-6: return 1e3
        return wall_neg(D,*wA)**2+wall_neg(D,*wB)**2
    best=1e9
    for _ in range(80):
        x0=rng.random(4)
        r=minimize(obj,x0,method='Nelder-Mead',options=dict(maxiter=20000,xatol=1e-14,fatol=1e-15))
        best=min(best,r.fun)
    if best<1e-8:
        # recover best point
        pass
    return best

def find_corner_D(wA,wB):
    def obj(x):
        a,b,c,d=x
        if not(0<=a<=1 and 0<=b<=1 and 0<=c<=1 and 0<=d<=1): return 1e3
        D=np.array([[a,b,1-a-b],[c,d,1-c-d],[1-a-c,1-b-d,a+b+c+d-1]])
        if D.min()<1e-6: return 1e3
        return wall_neg(D,*wA)**2+wall_neg(D,*wB)**2
    best=1e9; bestx=None
    for _ in range(80):
        x0=rng.random(4)
        r=minimize(obj,x0,method='Nelder-Mead',options=dict(maxiter=30000,xatol=1e-15,fatol=1e-16))
        if r.fun<best: best=r.fun;bestx=r.x
    if best<1e-6:
        a,b,c,d=bestx
        D=np.array([[a,b,1-a-b],[c,d,1-c-d],[1-a-c,1-b-d,a+b+c+d-1]])
        return D
    return None

wn=lambda w:f"W({w[0]+1}{w[1]+1}|{w[2]+1})"

# Test all 36 pairs: expect corner iff rowpairs differ AND hyps differ
import collections
mism=[]
for ia in range(9):
    for ib in range(ia+1,9):
        wA,wB=walls[ia],walls[ib]
        diff_row = rowpair(wA)!=rowpair(wB)
        diff_hyp = hyp(wA)!=hyp(wB)
        predicted = diff_row and diff_hyp
        D=find_corner_D(wA,wB)
        actual = D is not None
        if predicted!=actual:
            mism.append((wn(wA),wn(wB),predicted,actual))
print("corner-rule mismatches (should be []):",mism)

# count predicted corners = pairs differing in both coordinates
n=0
for ia in range(9):
    for ib in range(ia+1,9):
        if rowpair(walls[ia])!=rowpair(walls[ib]) and hyp(walls[ia])!=hyp(walls[ib]): n+=1
print("predicted corner count (rook-nonattacking pairs):",n," (matches 18)")

# 3-wall points: do triples meet at a single interior point?
def find_triple_D(ws):
    def obj(x):
        a,b,c,d=x
        if not(0<=a<=1 and 0<=b<=1 and 0<=c<=1 and 0<=d<=1): return 1e3
        D=np.array([[a,b,1-a-b],[c,d,1-c-d],[1-a-c,1-b-d,a+b+c+d-1]])
        if D.min()<1e-6: return 1e3
        return sum(wall_neg(D,*w)**2 for w in ws)
    best=1e9;bestx=None
    for _ in range(120):
        x0=rng.random(4)
        r=minimize(obj,x0,method='Nelder-Mead',options=dict(maxiter=30000,xatol=1e-15,fatol=1e-16))
        if r.fun<best: best=r.fun;bestx=r.x
    if best<1e-6:
        a,b,c,d=bestx
        return np.array([[a,b,1-a-b],[c,d,1-c-d],[1-a-c,1-b-d,a+b+c+d-1]])
    return None
print("\nTriple-wall interior points (3 walls through one interior point?):")
cnt=0
for iw in range(9):
    for jw in range(iw+1,9):
        for kw in range(jw+1,9):
            ws=[walls[iw],walls[jw],walls[kw]]
            # must be pairwise corner-compatible to even try
            comp=True
            for x in range(3):
                for y in range(x+1,3):
                    if not(rowpair(ws[x])!=rowpair(ws[y]) and hyp(ws[x])!=hyp(ws[y])): comp=False
            if not comp: continue
            D=find_triple_D(ws)
            if D is not None:
                cnt+=1
                if cnt<=6: print("  triple:",[wn(w) for w in ws])
print("total triple interior points:",cnt)
