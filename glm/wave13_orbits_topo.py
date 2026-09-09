#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""WAVE 13b: base c-orbit census + boundary-topology sanity for the corrected
cellulation design spec.
 c = cyclic column permutation sigma=(123) on moduli D (D_{ij}->D_{i,sigma^-1 j}),
 equivalently rotates the hypotenuse index of each wall; fixes the flat point
 D_f = (1/3) all-ones (barycenter, in int U3).
Report c-orbit structure of: 6 vertices, 9 transposition edges, 9 walls,
18 corners, 6 triple points.
"""
import itertools
def cyc(j):  # sigma=(1->2,2->3,3->1) i.e. 0->1,1->2,2->0 in 0-index
    return (j+1)%3
names=[''.join(map(str,x)) for x in itertools.permutations('123')]

def vertices_orbits():
    # vertex = permutation pi (image tuple). c permutes columns by sigma on codomain values.
    # Represent pi as tuple of columns for rows (0,1,2): value = column.
    # c(D)_{i j}=D_{i, sigma^-1 j}; a permutation matrix P_pi has D_{i j}=1 iff pi(i)=j.
    # c maps to D' with D'_{i j}=D_{i,sigma^-1 j}; D'_{i j}=1 iff pi(i)=sigma^-1 j iff sigma pi(i)=j.
    # => new pi' = sigma ∘ pi  (on column values).
    def sigma_val(v): return cyc(v)
    seen=set(); orbs=[]
    for n in names:
        pi=tuple(int(ch)-1 for ch in n)
        if pi in seen: continue
        orb=[pi]; x=pi
        while True:
            x=tuple(sigma_val(v) for v in x); 
            if x==pi: break
            orb.append(x)
        for y in orb: seen.add(y)
        orbs.append(orb)
    return orbs
ov=vertices_orbits()
print("vertex c-orbits:",len(ov), [ [ ''.join(str(c+1) for c in o) for o in orb] for orb in ov])

def c_on_perm(pi):  # pi as tuple columns; c(pi)=sigma∘pi on values
    return tuple((v+1)%3 for v in pi)

# walls labelled by (rp,hyp) in coords: rp in {(0,1),(0,2),(1,2)}, hyp in {0,1,2}
def rp_index(rp): return {(0,1):0,(0,2):1,(1,2):2}[rp]
rp_list=[(0,1),(0,2),(1,2)]
walls=[(ri,k) for ri in range(3) for k in range(3)]  # (rowpair-index,hyp)
def wname(r,k): return f"W({'12' if r==0 else '13' if r==1 else '23'}|{k+1})"
seen=set(); worbs=[]
for w in walls:
    if w in seen: continue
    orb=[w]; x=w
    while True:
        r,k=x; x=(r,cyc(k))
        if x==w: break
        orb.append(x)
    for y in orb: seen.add(y)
    worbs.append(orb)
print("wall c-orbits:",len(worbs), [[wname(r,k) for (r,k) in o] for o in worbs])

# edges: between vertices pi, pi'.  Under c both vertices' values shifted by sigma:
# conv(P,P') -> conv(P_sigma∘pi, P_sigma∘pi'). represent edge by unordered {pi,pi'}.
def edge_rep(pi,pi2): 
    a=tuple(sorted((pi,pi2)))
    return a
edge_seen=set(); eorbs=[]
E=[]
for i in range(6):
    for j in range(i+1,6):
        pi=tuple(int(c)-1 for c in names[i]); pi2=tuple(int(c)-1 for c in names[j])
        if sum(1 for a,b in zip(pi,pi2) if a!=b)==2:  # transposition diff (2 spots differ)
            E.append((pi,pi2))
print("num transposition edges:",len(E))
seen=set(); eorbs=[]
for e in E:
    if e in seen: continue
    orb=[e]; x=e
    while True:
        x=tuple(sorted((c_on_perm(x[0]),c_on_perm(x[1]))))
        if x==e: break
        orb.append(x)
    for y in orb: seen.add(y)
    eorbs.append(orb)
print("edge c-orbits:",len(eorbs), [[ ''.join(str(c+1) for c in o[0][0])+'-'+''.join(str(c+1) for c in o[0][1]) for e in orb])

# corners & triples orbit counts via formulas (verified by group action reasoning):
print("\nExpected (group-action):")
print(" corners: 3 rowpair-pairs x (3 colpairs cycled /3) ... = 6 c-orbits of 3")
print(" triples : 2 c-orbits of 3  (left-sigma on 6 bijections)")
print(" walls: 3 c-orbits of 3 ; edges: 3 c-orbits of 3 ; vertices: 2 c-orbits of 3")
