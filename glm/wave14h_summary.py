#!/usr/bin/env python3
"""WAVE 14H summary: exact edge values, volume fractions, sigma pairing table."""
import numpy as np, itertools
from collections import Counter
rng = np.random.default_rng(7)
PERM=[''.join(p) for p in itertools.permutations('123')]
def Pmat(s):
    M=np.zeros((3,3))
    for r,ch in enumerate(s): M[r,int(ch)-1]=1.0
    return M
VM={p:Pmat(p) for p in PERM}
def entries(X):
    a,b,c,d=X[...,0],X[...,1],X[...,2],X[...,3]
    return np.stack([np.stack([a,b,1-a-b],-1),np.stack([c,d,1-c-d],-1),
                     np.stack([1-a-c,1-b-d,a+b+c+d-1],-1)],-2)
def Qarr(X):
    E=entries(X); A=E[...,0,0]*E[...,1,0]; B=E[...,0,1]*E[...,1,1]; C=E[...,0,2]*E[...,1,2]
    return 2*(A*B+B*C+C*A)-(A*A+B*B+C*C)
def vec(M): return np.array([M[0,0],M[0,1],M[1,0],M[1,1]])
print("(a) Q along the 15 edges of B3 (t in [0,1], 2001 pts):")
for i,x in enumerate(PERM):
    for y in PERM[i+1:]:
        typ='T' if sum(1 for k in range(3) if x[k]!=y[k])==2 else 'C'
        ts=np.linspace(0,1,2001)[:,None]
        Q=Qarr((1-ts)*vec(VM[x])+ts*vec(VM[y]))
        print(f"   [{typ}] {x}-{y}: Q min {Q.min():+.3e} max {Q.max():+.3e}"
              f"  {'IDENTICALLY 0' if abs(Q).max()<1e-13 else 'negative inside'}")
print("\n(b) Monte-Carlo volumes in the chart box [0,1]^4 (3e6 pts):")
N=3000000; X=rng.random((N,4)); E=entries(X)
inB=(E.min(axis=(1,2))>=-1e-15).mean(); inU=((E.min(axis=(1,2))>=-1e-15)&(Qarr(X)>=0)).mean()
print(f"   vol(B3)/box = {inB:.5f}   vol(U3)/box = {inU:.5f}   vol(U3)/vol(B3) = {inU/inB:.4f}")
print("\n(c) sigma-value frequencies on W (900 wall points) -- ambiguity count:")
pts=[]
T=np.linspace(0,2.5,251)
while len(pts)<900:
    Y=rng.random((4000,4)); E=entries(Y)
    Y=Y[(E.min(axis=(1,2))>0.05)&(E.max(axis=(1,2))<0.95)&(Qarr(Y)>1e-3)]
    if not len(Y): continue
    V=rng.standard_normal((len(Y),4)); V/=np.linalg.norm(V,axis=1)[:,None]
    P=Y[:,None,:]+T[None,:,None]*V[:,None,:]; Ep=entries(P); q=Qarr(P)
    em=Ep.min(axis=(2,3)); eM=Ep.max(axis=(2,3))
    cr=(q<0)&(em>1e-4)&(eM<1-1e-4); idx=np.argmax(cr,axis=1)
    ok=cr[np.arange(len(Y)),idx]&(idx>0)
    from scipy.optimize import brentq
    for k in np.where(ok)[0]:
        j=int(idx[k]); u=V[k]; xx=Y[k]
        try: tt=brentq(lambda t: float(Qarr(xx+t*u)),T[j-1],T[j],xtol=1e-15)
        except Exception: continue
        Ee=entries(xx+tt*u)
        if Ee.min()>1e-4 and Ee.max()<1-1e-4: pts.append(Ee)
def sig(E,eps=1e-6):
    out=[]
    for (i,j) in [(0,1),(0,2),(1,2)]:
        p=np.sqrt(np.clip(E[i,:]*E[j,:],0,None)); s=np.sort(p)
        if s[0]+s[1]-s[2]>1e-7: return None
        k=int(np.argmax(p)); out.append(None if (p[k]-s[1])<eps else k)
    return tuple(out)
c=Counter(sig(E) for E in pts[:900])
print("  ",dict(c)); print(f"   unambiguous perms: {sum(v for k,v in c.items() if k and all(x is not None for x in k))}"
      f" / {sum(c.values())}  ambiguous-or-nonplanar: {sum(v for k,v in c.items() if not k or any(x is None for x in k))}")
cg=Counter()
for k in c:
    if k and all(x is not None for x in k):
        cg[tuple((v-1)%3 for v in k)]+=c[k]
print("   c-orbit check (c = cyclic column shift, rotate hypotenuse indices by -1):")
for a in (0,1,2):
    pass
orb={}
for k in c: 
    if k and all(x is not None for x in k):
        rep=min(tuple((v+t)%3 for v in k) for t in range(3))
        orb.setdefault(rep,[]).append(k)
print("   c-orbits of the 6 sigma classes:",[[ ''.join(map(str,k)) for k in v] for v in orb.values()])
print("\n(d) B3 face data recheck: facet D13=0 vertices",[p for p in PERM if VM[p][0,2]==0])
