#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""WAVE 14: corrected stratification of the U3 boundary.
KEY IDENTITY (exact, verified): on the doubly-stochastic affine space,
   Q12 = Q13 = Q23 =: Q  (4*Area^2 of each row-pair product-triple).
Hence  U3 = {D in B3 : Q(D) >= 0}, with a SINGLE boundary hypersurface
   B := {Q = 0} cap int B3   (3-dimensional in the 4-dim affine space),
and on B ALL THREE row-pairs are degenerate simultaneously.
Stratify B by the "hypotenuse triple" h = (k12,k13,k23) in {1,2,3}^3:
   k_r := the index realising  p_{k} = p_{l} + p_{m}  for row pair r.
Report: which triples occur, the stratum census, and the codim-1 hysteresis
loci (where two p's of some row pair are equal, so h is ambiguous).
"""
import numpy as np, itertools
from scipy.optimize import brentq
rng=np.random.default_rng(0)

def D_of(x):
    a,b,c,d=x
    return np.array([[a,b,1-a-b],[c,d,1-c-d],[1-a-c,1-b-d,a+b+c+d-1]],float)
def Q(D):
    def qf(i,j):
        p2=[D[i,k]*D[j,k] for k in range(3)]
        a2,b2,c2=p2
        return 2*(a2*b2+b2*c2+c2*a2)-(a2**2+b2**2+c2**2)
    return qf(0,1)
def hyp_triple(D, tol=1e-6):
    """for each row pair return the index k realising degeneracy, or None"""
    res=[]
    for (i,j) in [(0,1),(0,2),(1,2)]:
        p=np.sqrt(np.clip(D[i,:]*D[j,:],0,None))
        s=np.sort(p)   # s0<=s1<=s2
        deg = (s[0]+s[1]-s[2])
        if abs(deg)>tol: res.append(None); continue
        # the hypotenuse is the largest index
        k=int(np.argmax(p))
        res.append(k)
    return tuple(res)

def find_boundary_point():
    """random DS interior point; move along random line to Q=0 inside int B3"""
    while True:
        x=rng.random(4)
        D=D_of(x)
        if D.min()<0.02 or D.max()>0.98: continue
        if Q(D)<0.02: continue     # want clearly interior
        v=rng.standard_normal(4); v/=np.linalg.norm(v)
        f=lambda t: Q(D_of(x+t*v))
        # find sign change
        t=0.0; step=0.01
        prev=f(0); tt=None
        t=0.0
        for _ in range(400):
            t+=step
            Dt=D_of(x+t*v)
            if Dt.min()<1e-3 or Dt.max()>1-1e-3: break
            cur=f(t)
            if cur<0:
                tt=t; break
            prev=cur
        if tt is None: continue
        r=brentq(lambda t: Q(D_of(x+t*v)), tt-step, tt, xtol=1e-14)
        D=D_of(x+r*v)
        if D.min()<1e-3 or D.max()>1-1e-3: continue
        return D

from collections import Counter
cnt=Counter()
samples=[]
for _ in range(4000):
    D=find_boundary_point()
    h=hyp_triple(D)
    if None in h: continue
    cnt[h]+=1
    samples.append((D,h))
print("hypotenuse-triple census on B = {Q=0} cap int B3 (4000 samples):")
for h,c in sorted(cnt.items(), key=lambda t:-t[1]):
    print("   h =",h," count",c,"  (fraction %.3f)"%(c/sum(cnt.values())))
print("total valid samples:",sum(cnt.values())," distinct triples:",len(cnt))
