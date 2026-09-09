#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""WAVE 13 (pre-spec): pin the concrete incidence data needed by the corrected-base
cellulation design. Verify:
  (A) corner 2-loci (rook-nonattacking wall pairs): which transposition edges lie on
      their closure (endpoints), i.e. corner<->edge incidence.
  (B) each fold-wall 3-cell: the set of transposition edges on its closure.
  (C) base cell/orbit census under the column-cyclic action c (hypotenuse rotation),
      incl. the fixed flat point D_f = (1/3)ones in int U3.
Only float probes + exact incidence bookkeeping; residuals ~0 certify incidence.
"""
import numpy as np, itertools
from scipy.optimize import minimize

def wall_neg(D,i,j,k):
    cols=[0,1,2]; l,m=[c for c in cols if c!=k]
    return np.sqrt(D[i][k]*D[j][k])-np.sqrt(D[i][l]*D[j][l])-np.sqrt(D[i][m]*D[j][m])

names=[''.join(map(str,x)) for x in itertools.permutations('123')]
def Pmat(s):
    M=np.zeros((3,3))
    for r,ch in enumerate(s): M[r,int(ch)-1]=1.0
    return M
Ps={n:Pmat(n) for n in names}
def is_transp(a,b): return sum(x!=y for x,y in zip(a,b))==2
edges=[(a,b) for i,a in enumerate(names) for b in names[i+1:] if is_transp(a,b)]
def edgename(e): return e[0]+'-'+e[1]

W=[(i,j,k) for (i,j) in [(0,1),(0,2),(1,2)] for k in range(3)]
def wn(w): return f"W({w[0]+1}{w[1]+1}|{w[2]+1})"
def rp(w): return (w[0],w[1])
def hyp(w): return w[2]

# edge -> set of walls containing it
def edge_contains(e,w,tol=1e-9):
    a,b=e; ok=True
    for t in np.linspace(0,1,41):
        D=(1-t)*Ps[a]+t*Ps[b]
        if abs(wall_neg(D,*w))>tol: ok=False;break
    return ok
edge_walls={e:[w for w in W if edge_contains(e,w)] for e in edges}
print("=== edge -> #walls containing (expect 8 each) ===")
for e in edges: print(" ",edgename(e), len(edge_walls[e]))

# corners = pairs differing in both coords
corners=[]
for ia in range(9):
    for ib in range(ia+1,9):
        if rp(W[ia])!=rp(W[ib]) and hyp(W[ia])!=hyp(W[ib]):
            corners.append((W[ia],W[ib]))
print("num corners:",len(corners))

# For a corner (pair of walls), a transposition edge is an ENDPOINT if the corner
# 2-locus limits onto that edge, i.e. the two walls both contain the edge AND the
# corner equation system, restricted toward the edge, has the edge in closure.
# Robust check: a point very close to the edge that is a corner solution exists.
def corner_resid_near_edge(corner,e):
    wA,wB=corner; a,b=e
    def obj(x):
        # x=(t, n1..n4): D=(1-t)edge(t')... build D in B3 near edge e
        t=x[0]
        # base point on edge:
        Dbase=(1-t)*Ps[a]+t*Ps[b]
        # perturb only free directions orthogonal-ish: add small symmetric correction
        # simpler: parametrize D near edge via doubly stochastic with small off-edge
        return 0.0
    return 0.0
def corner_edge_incidence(corner,e):
    """find D along the corner with max possible t toward edge; if D->edge interior, incident."""
    wA,wB=corner; a,b=e
    # restrict: seek corner solution and measure its min distance to each of the 
    # edge's entries; endpoint-of-corner means we can push D to be ON the edge
    # Parametrize near-edge points as (1-s)*D_edge_midpoint + s*stuff won't keep in B3 generic.
    # Instead: minimize wall residuals subject to D lying very near the segment conv(a,b)+tiny normal.
    # Practical: the corner locus is 2-dim; its boundary includes transposition edges e iff
    # there is a sequence of corner points -> a point of e with all other entries-> those of edge.
    # Search for corner point minimizing distance to edge-set metric = sum (entry-vs-edge-target)^2
    target_mid=(Ps[a]+Ps[b])/2
    def obj(x):
        a_,b_,c_,d_=x
        if not(0<=a_<=1 and 0<=b_<=1 and 0<=c_<=1 and 0<=d_<=1): return 1e6
        D=np.array([[a_,b_,1-a_-b_],[c_,d_,1-c_-d_],[1-a_-c_,1-b_-d_,a_+b_+c_+d_-1]])
        if D.min()<0: return 1e6
        wr=wall_neg(D,*wA)**2+wall_neg(D,*wB)**2
        dist=np.sum((D-target_mid)**2)   # want close to edge
        return wr + 50*dist
    best=1e9;bestx=None
    for _ in range(120):
        x0=np.random.random(4)
        r=minimize(obj,x0,method='Nelder-Mead',options=dict(maxiter=20000,xatol=1e-13,fatol=1e-14))
        if r.fun<best: best=r.fun;bestx=r.x
    if bestx is None: return False, best
    a_,b_,c_,d_=bestx
    D=np.array([[a_,b_,1-a_-b_],[c_,d_,1-c_-d_],[1-a_-c_,1-b_-d_,a_+b_+c_+d_-1]])
    dist=np.sum((D-target_mid)**2)
    on_wall=wall_neg(D,*wA)**2+wall_neg(D,*wB)**2
    return dist<1e-6, (dist,on_wall)

print("\n=== corner -> incident transposition edges (endpoints) ===")
for corner in corners:
    inc=[]
    for e in edges:
        hit,_=corner_edge_incidence(corner,e)
        if hit: inc.append(e)
    print(" ",wn(corner[0]),"&",wn(corner[1]), "->", [edgename(e) for e in inc])
