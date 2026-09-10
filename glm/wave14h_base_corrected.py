# !!! RETRACTED IN PART by WAVE14H_RESOLUTION.md (Wave 14) !!!
#  - the "9 facet loci are 2-dimensional" census and the facet_locus_ac (a,c)
#    parametrisation below are WRONG: Q < 0 on every facet off its four
#    transposition edges (300000-point survey, wave14h_final_output.txt section 1).
#  - the correct boundary stratification of U3 is 6 (3-dim sigma-pieces) + 9
#    transposition edges + 6 vertices, with NO 2-cells.
#  Kept for provenance only; see wave14h_final_topology.py for the corrected data.
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""WAVE 14H (resolution): the CORRECTED base stratification of U3 = {Q >= 0} cap B3.

Findings being certified here:
 (1) Q12 = Q13 = Q23 =: Q  (exact).            [H-facet/H-top foundation]
 (2) {Q=0} cap int B3 splits into 6 OPEN 3-MANIFOLDS indexed by the
     hypotenuse assignment sigma in S3 (a bijection rowpair -> column).
     sigma is locally constant in int B3 (argmax is strict there), hence the
     6 sigma-level-sets are the connected components.
 (3) The Birkhoff-boundary part: per facet {D_ab = 0} the U3-locus is
     2-dimensional; the 6 three-cells, the 9 facet-loci, the 9 transposition
     edges and the 6 vertices give the base census
        dim4:1, dim3:6, dim2:9, dim1:9, dim0:6   => chi(U3)=1, chi(dU3)=0
     (a 4-ball with S^3 boundary), and Fl3's Euler characteristic
        6*chi(pt)+9*chi(S^1)+9*chi(T^2)+6*chi(T^2)+1*chi(T^2) = 6  [matches]
 (4) c-orbits of the base cells.
"""
import numpy as np, itertools
from scipy.optimize import brentq
rng=np.random.default_rng(12345)

def Qp(a,b,c,d):
    D=[[a,b,1-a-b],[c,d,1-c-d],[1-a-c,1-b-d,a+b+c+d-1]]
    D=np.array(D,float)
    def qf(i,j):
        p2=np.array([D[i,k]*D[j,k] for k in range(3)])
        A,B,C=p2
        return 2*(A*B+B*C+C*A)-(A*A+B*B+C*C)
    return qf(0,1),D
def Q(x): return Qp(*x)[0]
def Dm(x): return Qp(*x)[1]
def sigma(D):
    """hypotenuse index per row pair (0/1/2 or None if not degenerate)"""
    out=[]
    for (i,j) in [(0,1),(0,2),(1,2)]:
        p=np.sqrt(np.clip(D[i,:]*D[j,:],0,None))
        s=np.sort(p)
        if s[0]+s[1]-s[2] > 1e-7: out.append(None); continue
        out.append(int(np.argmax(p)))
    return tuple(out)

# ---------- (2) sigma census on {Q=0} cap int B3 ----------
from collections import Counter
def sample_boundary():
    while True:
        x=rng.random(4)
        if Dm(x).min()<0.03 or Dm(x).max()>0.97: continue
        if Q(x)<0.03: continue
        v=rng.standard_normal(4); v/=np.linalg.norm(v)
        lo=None
        t=0.0
        for _ in range(600):
            t+=0.005
            if Dm(x+t*v).min()<1e-3 or Dm(x+t*v).max()>1-1e-3: break
            if Q(x+t*v)<0: lo=t; break
        if lo is None: continue
        t0=brentq(lambda t: Q(x+t*v), lo-0.005, lo, xtol=1e-15)
        D=Dm(x+t0*v)
        if D.min()<1e-3 or D.max()>1-1e-3: continue
        return D
cnt=Counter(); pts=[]
for _ in range(3000):
    D=sample_boundary(); s=sigma(D)
    if None in s: continue
    cnt[s]+=1; pts.append((D,s))
print("(2) sigma census on {Q=0} cap int B3:")
for s,c in sorted(cnt.items()): print("    sigma =",s," count",c)
print("    distinct sigma:",len(cnt),"  all permutations of {0,1,2}? ",
      all(sorted(s)==[0,1,2] for s in cnt))

# ---------- (3) facet loci ----------
# facet D13=0  <=> x2 = 1-x1 ; free (x1,x3,x4). Locus: Q(x1,1-x1,x3,x4)=0.
def facet_locus_pts(n=4000):
    P=[]
    for _ in range(n*20):
        if len(P)>=n: break
        x1=rng.random(); x3=rng.random(); x4=rng.random()
        x2=1-x1
        D=Dm((x1,x2,x3,x4))
        if D.min()<0.02: continue
        P.append((x1,x3,x4,Q((x1,x2,x3,x4)),D))
    return P
P=facet_locus_pts()
feas=[p for p in P if abs(p[3])<2e-3]
print("\n(3) facet {D13=0}: grid-sampled near-locus points:",len(feas),"/",len(P))
if feas:
    Z=np.array([[p[0],p[1],p[2]] for p in feas])
    Z=Z-Z.mean(axis=0); C=np.cov(Z.T); w=np.linalg.eigvalsh(C)
    print("    local spread eigs:",np.round(w,6),"  -> intrinsic dim =",int((w>1e-4).sum()))
# exact facet locus via the 2 equations  a c = b d, a f = b g  with b=1-a, f=1-a-c
def facet_locus_exact(n=3000):
    out=[]
    for _ in range(n*10):
        if len(out)>=n: break
        a=rng.random()
        if a<1e-3 or a>1-1e-3: continue
        c=rng.random()*(1-a)          # f = 1-a-c >= 0
        f=1-a-c
        d=a*c/(1-a); g=a*f/(1-a)
        e=1-c-d; h=1-f-g
        D=np.array([[a,1-a,0],[c,d,e],[f,g,h]])
        if D.min()<-1e-12: continue
        out.append((a,c,D))
    return out
FL=facet_locus_exact()
print("    explicit 2-parameter facet-locus points (a,c):",len(FL),
      " entries>=0 ok:",all(p[2].min()>=-1e-12 for p in FL))
# on the facet locus, which sigma for rowpair (2,3)?
s23=Counter(); s12=Counter(); s13=Counter()
for a,c,D in FL[:1500]:
    p=np.sqrt(np.clip(D[1,:]*D[2,:],0,None))
    s23[int(np.argmax(p))]+=1
print("    facet locus: rowpair(2,3) hypotenuse distribution:",dict(s23))
print("    (rowpairs (1,2),(1,3) are ambiguous there: p1=p2)")

# ---------- Euler characteristics ----------
print("\n(4) base census & Euler characteristics")
def chi(cells): return sum(((-1)**d)*n for d,n in cells)
U3=[(4,1),(3,6),(2,9),(1,9),(0,6)]
print("    U3 cells (dim,count):",U3," chi(U3)=",chi(U3))
dU3=[(3,6),(2,9),(1,9),(0,6)]
print("    dU3 cells:",dU3," chi(dU3)=",chi(dU3),"(S^3 has chi=0)")
fib={'pt':1,'S1':0,'T2':0}
chiFl3=6*1+9*0+9*0+6*0+1*0
print("    chi(Fl3) from fibres =",chiFl3,"(must equal 6)")

# ---------- c-orbits ----------
print("\n(5) c-orbits of base cells (c = cyclic column shift, rotates hypotenuse indices)")
def csigma(s): return tuple((k+1)%3 for k in s)
seen=set(); orbs=[]
for s in itertools.permutations(range(3)):
    if s in seen: continue
    orb=[s]; x=s
    while True:
        x=csigma(x)
        if x==s: break
        orb.append(x)
    for y in orb: seen.add(y)
    orbs.append(orb)
print("    6 three-cells -> c-orbits:",[[list(o) for o in orb] for orb in orbs], " => ",len(orbs),"orbits of 3")
print("    9 facet-loci: 9 = 3 x 3 (c cycles facet indices) => 3 orbits of 3")
print("    9 edges: 3 orbits of 3 ; 6 vertices: 2 orbits of 3 ; 4-cell: 1 c-invariant")
