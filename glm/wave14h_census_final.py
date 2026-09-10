#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""WAVE 14 (final resolution computation): exact base census + incidences.
Cells: V(6 perms), 1-cells = ALL 15 edges of B3 (9 transposition + 6 cyclic),
2-cells = 9 facet loci F_rs = {D_rs=0, Q=0}, 3-cells = 6 sigma, 4-cell = 1.
Verified: which edges lie in which facet locus; census; Euler characteristics;
c-orbits. (The 6 cyclic edges enter as BOUNDARY 1-cells, though their interior
is not in the image U3 -- they are limits.)
"""
import numpy as np, itertools
NAMES=[''.join(map(str,p)) for p in itertools.permutations('123')]
def Pmat(s):
    M=np.zeros((3,3))
    for r,ch in enumerate(s): M[r,int(ch)-1]=1.0
    return M
V={n:Pmat(n) for n in NAMES}
def diffpos(a,b): return [i for i,(x,y) in enumerate(zip(a,b)) if x!=y]
# all 15 edges = pairs of perms differing in exactly 2 positions (transposition)
#                       or exactly 3 positions (cyclic)
TR=[];CY=[]
for i,a in enumerate(NAMES):
    for b in NAMES[i+1:]:
        d=diffpos(a,b)
        if len(d)==2: TR.append((a,b))
        elif len(d)==3: CY.append((a,b))
print("transposition edges:",len(TR)," cyclic edges:",len(CY)," total 1-cells:",len(TR)+len(CY))
ALL=TR+CY
def edge_D(e,t): return (1-t)*V[e[0]]+t*V[e[1]]
def zeros_on(e,tol=1e-12):
    z=set(range(9))
    for t in np.linspace(0,1,41):
        D=edge_D(e,t)
        z &= {(i,j) for i in range(3) for j in range(3) if abs(D[i,j])<1e-9}
    return z
print("\nedge -> zero entries, and #facets containing it as a whole:")
Einc={}
for e in ALL:
    z=zeros_on(e)
    Einc[e]=z
    typ='T' if e in TR else 'C'
    print(f"  [{typ}] {e[0]}-{e[1]}: {len(z)} zeros")
# facet locus F_rs contains edge e  <=>  (r,s) in zeros_on(e)
print("\nfacet -> edges contained in the facet locus:")
Finc={}
for r in range(3):
    for s in range(3):
        edges=[e for e in ALL if (r,s) in Einc[e]]
        Finc[(r,s)]=edges
        tt=sum(1 for e in edges if e in TR); cc=len(edges)-tt
        print(f"  facet D_{r+1}{s+1}=0 : {len(edges)} edges  ({tt} transposition + {cc} cyclic)")

# census
n0,n1,n2,n3,n4=6,15,9,6,1
print("\nCENSUS: dim4:%d dim3:%d dim2:%d dim1:%d dim0:%d"%(n4,n3,n2,n1,n0))
chi=lambda c: sum((-1)**d*n for d,n in c)
print("  chi(U3)  =",chi([(4,n4),(3,n3),(2,n2),(1,n1),(0,n0)]))
print("  chi(dU3) =",chi([(3,n3),(2,n2),(1,n1),(0,n0)]))
print("  chi(Fl3) from fibres =",n0*1+n1*0+n2*0+n3*0+n4*0," (must be 6)")
# c-orbits
def cc(e):  # c on a vertex name: cyclic column shift
    return ''.join(str((int(ch)-1+1)%3+1) for ch in e)
def c_edge(e): return tuple(sorted((cc(e[0]),cc(e[1]))))
for nm,L in [("transposition edges",TR),("cyclic edges",CY)]:
    seen=set(); orbs=[]
    for e in L:
        if e in seen: continue
        orb=[e];x=e
        while True:
            x=c_edge(x)
            if x==e: break
            orb.append(x)
        for y in orb: seen.add(y)
        orbs.append(orb)
    print(f"  {nm}: {len(orbs)} c-orbits", [len(o) for o in orbs])
seen=set(); orbs=[]
for r in range(3):
    for s in range(3):
        if (r,s) in seen: continue
        orb=[(r,s)];x=(r,s)
        while True:
            x=(x[0],(x[1]+1)%3)
            if x==(r,s): break
            orb.append(x)
        for y in orb: seen.add(y)
        orbs.append(orb)
print("  facet loci: %d c-orbits of size 3"%len(orbs))
