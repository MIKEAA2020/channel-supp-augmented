#!/usr/bin/env python3
"""WAVE 14: link of a transposition edge inside the wall W={Q=0} cap B3.
March outward from an edge point toward random nearby interior points (B3 convex),
locate the FIRST Q=0 crossing; record sigma there (relaxed interior filter)."""
import numpy as np, itertools
from collections import Counter
from scipy.optimize import brentq
rng=np.random.default_rng(4242)
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
def sig(E,eps=1e-7):
    out=[]
    for (i,j) in [(0,1),(0,2),(1,2)]:
        p=np.sqrt(np.clip(E[i,:]*E[j,:],0,None)); s=np.sort(p)
        if s[0]+s[1]-s[2]>1e-6: return None
        k=int(np.argmax(p)); out.append(None if (p[k]-s[1])<eps else k)
    return tuple(out)
S=np.linspace(0,1,201)
for i,x in enumerate(PERM):
    for y in PERM[i+1:]:
        if sum(1 for k in range(3) if x[k]!=y[k])!=2: continue
        x0=0.5*(vec(VM[x])+vec(VM[y]))
        res=Counter(); tot=0
        for _ in range(60):
            Y=x0[None,:]+0.35*(rng.random((4000,4))-0.5)
            Ey=entries(Y); qy=Qarr(Y)
            keep=(Ey.min(axis=(1,2))>1e-9)&(qy>1e-4)
            Y=Y[keep]
            if not len(Y): continue
            P=x0[None,None,:]+S[None,:,None]*(Y[:,None,:]-x0[None,None,:])
            Ep=entries(P); q=Qarr(P)
            for k in range(len(Y)):
                if (Ep[k].min(axis=1)<0).any(): continue
                j=1+int(np.argmax(q[k,1:]<=0))
                if not (q[k,j]<=0): continue
                u=Y[k]-x0
                try: t=brentq(lambda t: float(Qarr(x0+t*u)),0.0,S[j],xtol=1e-16)
                except Exception: continue
                E=entries(x0+t*u)
                if E.min()<1e-12: continue
                s=sig(E)
                if s is not None and all(v is not None for v in s):
                    res[s]+=1
        print(f"  edge {x}-{y}: {sum(res.values())} wall probes -> sigma { {''.join(map(str,k)):v for k,v in res.most_common()} }")
