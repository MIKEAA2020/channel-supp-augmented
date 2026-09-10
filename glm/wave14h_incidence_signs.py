#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""WAVE 14H (resolution, part 2): base POSET incidences + ORIENTATION SIGNS.
Base cells (census certified in wave14h_base_corrected.py):
   dim4: 1 (int U3)  dim3: 6 (sigma in S3)  dim2: 9 (facet loci F_ab)
   dim1: 9 (transposition edges)  dim0: 6 (vertices)
Determines: F_ab <-> 3-cells; dF_ab = edges; dE = vertices; and the +-1
orientation degrees, certified by d^2 = 0.
"""
import numpy as np, itertools
from scipy.optimize import brentq
rng=np.random.default_rng(7)
NAMES=[''.join(map(str,p)) for p in itertools.permutations('123')]

def Dmat(vec):
    a,b,c,d=vec
    return np.array([[a,b,1-a-b],[c,d,1-c-d],[1-a-c,1-b-d,a+b+c+d-1]],float)
def Dflat(M):
    return np.array([M[0,0],M[0,1],M[1,0],M[1,1]])
def Qf(vec):
    D=Dmat(vec)
    out=0
    for (i,j) in [(0,1)]:
        p2=np.array([D[i,k]*D[j,k] for k in range(3)]); A,B,C=p2
        out=2*(A*B+B*C+C*A)-(A*A+B*B+C*C)
    return out
def sigma_of(D,tol=1e-6):
    out=[]
    for (i,j) in [(0,1),(0,2),(1,2)]:
        p=np.sqrt(np.clip(D[i,:]*D[j,:],0,None)); s=np.sort(p)
        if s[0]+s[1]-s[2]>tol: out.append(None); continue
        out.append(int(np.argmax(p)))
    return tuple(out)

# ---- vertices / edges ----
def Pmat(s): 
    M=np.zeros((3,3))
    for r,ch in enumerate(s): M[r,int(ch)-1]=1.0
    return M
V={n:Pmat(n) for n in NAMES}
def is_transp(a,b): return sum(x!=y for x,y in zip(a,b))==2
EDGES=[(a,b) for i,a in enumerate(NAMES) for b in NAMES[i+1:] if is_transp(a,b)]
def edge_pts(e,t): return (1-t)*V[e[0]]+t*V[e[1]]

# ---- facet loci (9). Facet F_ab = {D_ab=0}; locus = {D_ab=0, Q=0} = 2-dim.
# explicit parametrization by facet type; use the general solution of
#   {D_ab = 0} cap {row-pairs through the zero give p-equality}.
def facet_locus(ab, n=400, seed=0):
    """return list of (D, sigma-partial) on the locus interior of facet {D_ab=0}"""
    r=ab[0]; c=ab[1]
    out=[]
    rr=rng if False else np.random.default_rng(seed)
    for _ in range(n*40):
        if len(out)>=n: break
        # build DS matrix with D[r,c]=0 and p-equality for the two row pairs through column c
        a=rr.random()
        if a<1e-3 or a>1-1e-3: continue
        A=np.zeros((3,3)); A[r,c]=0
        # fill row r: A[r,k] for k!=c with sum 1
        kk=[k for k in range(3) if k!=c]
        A[r,kk[0]]=1-a; A[r,kk[1]]=a   # a = A[r,kk[1]]
        # choose the other row values to satisfy the p-equalities
        # p_k^(r,i) = sqrt(A[r,k]A[i,k]); need equality for the two k!=c :
        # A[r,k1]A[i,k1] = A[r,k2]A[i,k2]  -> A[i,k2] = A[i,k1]*(A[r,k1]/A[r,k2])
        s=1.0
        for i in range(3):
            if i==r: continue
            # col sums: A[i,c] + sum_{k!=c} A[i,k] = 1
            t1=rr.random()*0.9+0.05
            t2=t1*(A[r,kk[0]]/A[r,kk[1]]) if A[r,kk[1]]>1e-9 else t1
            # scale so row sum =1: A[i,c]+t1+t2=1
            tot=t1+t2
            if tot>1-1e-6: continue
            A[i,c]=1-tot; A[i,kk[0]]=t1; A[i,kk[1]]=t2
        if np.any(A<-1e-12): continue
        # fix column sums: columns other than c must sum to 1; c already? enforce by rejection
        if not np.allclose(A.sum(axis=0),1,atol=1e-6): 
            continue
        out.append(A)
    return out

print("=== facet-locus feasibility by direct column-sum-consistent sampling ===")
# simpler: generic search in the 3-dim facet for Q=0 (2-dim locus), keep interior
def facet_search(ab, n=300):
    r,c=ab; out=[]
    for _ in range(n*200):
        if len(out)>=n: break
        a,b,d= rng.random(3)   # use D11,D12,D22 with D13=0 fixed pattern for ab=(0,2)
        # generic: assemble DS with D[r,c]=0
        M=np.zeros((3,3))
        # fill using the DS parametrization with the constraint D[r,c]=0
        # take general DS from (x1..x4) and impose the facet by solving
        # x2 = 1-x1  when (r,c)=(0,2)
        if (r,c)==(0,2):
            x=(a,1-a,b,d)
        elif (r,c)==(0,1):
            x=(a,b,d,b)  # placeholder, not used
            continue
        else:
            continue
        D=Dmat(x)
        if D.min()<0.02: continue
        # root in a free direction to hit Q=0
        v=rng.standard_normal(4); 
        # move along the facet: keep x2=1-x1 : adjust
        f=lambda t: Qf((x[0]+t*v[0], 1-(x[0]+t*v[0]), x[2]+t*v[2], x[3]+t*v[3]))
        lo=None; t=0.0
        if f(0)<0: continue
        t=0.0
        for _ in range(400):
            t+=0.004
            xx=(x[0]+t*v[0], 1-(x[0]+t*v[0]), x[2]+t*v[2], x[3]+t*v[3])
            if Dmat(xx).min()<1e-3: break
            if f(t)<0: lo=t; break
        if lo is None: continue
        try:
            t0=brentq(f, lo-0.004, lo, xtol=1e-14)
        except Exception: continue
        xx=(x[0]+t0*v[0], 1-(x[0]+t0*v[0]), x[2]+t0*v[2], x[3]+t0*v[3])
        Dm_=Dmat(xx)
        if Dm_.min()<1e-3: continue
        out.append(Dm_)
    return out

F02=facet_search((0,2))
print("facet {D13=0}: interior locus points found:",len(F02))
from collections import Counter
sc={}
for D in F02:
    s=sigma_of(D)
    sc[s]=sc.get(s,0)+1
print("  sigma (with None where ambiguous) counts:",dict(list(sc.items())[:10]))
# which entry vanishes at the locus boundary -> identify edges
def closest_edge(D):
    best=None;bd=1e9
    for e in EDGES:
        for t in np.linspace(0,1,101):
            d=np.linalg.norm(D-edge_pts(e,t))
            if d<bd: bd=d;best=(e,t)
    return best,bd
print("\n  boundary behaviour: shrink toward locus boundary (some entry -> 0):")
# sample the explicit (a,c) parametrization to get the 2-dim domain and its edges
def facet_locus_ac(n=4000):
    out=[]
    for _ in range(n*6):
        if len(out)>=n: break
        a=rng.random()
        if a<1e-3 or a>1-1e-3: continue
        c=rng.random()*(1-a)
        f=1-a-c
        d=a*c/(1-a); g=a*f/(1-a)
        e=1-c-d; h=1-f-g
        D=np.array([[a,1-a,0],[c,d,e],[f,g,h]])
        if D.min()<-1e-12 or D.max()>1+1e-12: continue
        out.append((a,c,D))
    return out
AC=facet_locus_ac()
print("  (a,c)-parametrised points:",len(AC))
# classify boundary of the (a,c) domain: c=0, f=0, e=0, h=0
def which_zero(D,tol=1e-9):
    z=[]
    for i in range(3):
        for j in range(3):
            if abs(D[i,j])<tol: z.append((i,j))
    return z
cnt=Counter()
for a,c,D in AC[:2000]:
    # parametric boundary indicators
    tags=[]
    if abs(c)<1e-3: tags.append("D21=0")
    if abs(1-a-c)<1e-3: tags.append("D31=0")
    if abs(1-c-a*c/(1-a))<1e-3: tags.append("D23=0")
    if abs(1-(1-a-c)-a*(1-a-c)/(1-a))<1e-3: tags.append("D33=0")
    cnt[tuple(tags)]+=1
print("  boundary-tag counts (empty=interior):",dict(list(cnt.items())[:8]))
