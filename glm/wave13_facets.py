#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""WAVE 13c: the 2-dim facet-equality loci (U3 cap facet relint regions of B3).
Wave 11 recorded facets feasible only on a codim-1 equality locus with T2 fibre.
Probe one facet exhaustively, characterize the feasible subset dimension, and
census the 9 facets' loci.
Facet = {D_ij = 0} (9 of them, tetrahedra in B3).
Membership in U3 = row-pair triangle inequalities (verified char).
"""
import numpy as np, itertools
def rp_slack(D):
    m=1e9
    for (i,j) in [(0,1),(0,2),(1,2)]:
        t=np.sqrt(np.clip(D[i,:]*D[j,:],0,None)); t=np.sort(t); m=min(m,t[0]+t[1]-t[2])
    return m
def inU3(D): return rp_slack(D)>=-1e-9

# facet D_13=0 : free entries (i,1),(i,2),(i,3),(i,?); param 3 coords then boundary 2-param
# points on facet: D = [[a,b,0],[c,d,e],[f,g,h]] with row/col sums.
# Actually with D_13=0: row1 a+b=1, col3 e+h=1. Let free: a=c1, d=c2, g=c3... use earlier param:
def facet13(a,d,f):
    # a=D11,d=D22,f=D31 ; derive:
    D=np.zeros((3,3))
    D[0,0]=a; D[0,1]=1-a       # row1
    D[1,1]=d;                   # will set col2
    # col2: D12+D22+D32=1 -> D32=1-(1-a)-d=a-d
    D[2,1]=a-d
    # col1: D11+D21+D31=1 -> D21=1-a-f
    D[2,0]=f; D[1,0]=1-a-f
    # col3: D13+D23+D33=1 with D13=0 -> D23+D33=1
    # row2: D21+D22+D23=1 -> D23=1-(1-a-f)-d=a+f-d ; then D33=1-D23=1-a-f+d
    D[1,2]=a+f-d; D[2,2]=1-a-f+d
    return D
def feas_ok(a,d,f):
    D=facet13(a,d,f)
    if D.min()<-1e-9 or D.max()>1+1e-9: return None
    if not inU3(D): return None
    return D

# scan to find extent of feasible region dimension
# sample uniform grid in (a,d,f) in [0,1]^3 intersect facet
feas_pts=[]
for a in np.linspace(0,1,40):
    for d in np.linspace(0,1,40):
        for f in np.linspace(0,1,40):
            D=feas_ok(a,d,f)
            if D is not None:
                feas_pts.append((a,d,f,D))
print("facet D13=0: feasible volume-fraction in (a,d,f)-cube:", len(feas_pts)/40**3, " total pts",len(feas_pts))
# dimension: are all 3 params free or only 2?  estimate by checking if feasible pts fill a 2D or 3D set
if feas_pts:
    P=np.array([[x,y,z] for (x,y,z,_) in feas_pts])
    # covariance rank
    C=np.cov(P.T); e=np.linalg.eigvalsh(C)
    print("  covariance eigenvalues:",np.round(e,4))
    print("  => effective dim (nonzero eig count):",int((e>1e-3).sum()))

# show a sample feasible interior-of-facet point
print("\nsample feasible facet points:",len(feas_pts))
for a,d,f,D in feas_pts[::max(1,len(feas_pts)//5)][:5]:
    print("  a,d,f=",round(a,2),round(d,2),round(f,2)," slack",round(rp_slack(D),3))
    print(np.round(D,3))
