import numpy as np
from scipy.optimize import minimize
from moduli import Vmod, rng

def rowpair_slack(D):
    m=1e9
    for (i,j) in [(0,1),(0,2),(1,2)]:
        t=np.sqrt(D[i,:]*D[j,:]); t=np.sort(t)
        m=min(m,t[0]+t[1]-t[2])
    return m

def sample_rowpair_ds(rng,nmax=100000):
    # sample doubly stochastic, keep only those with all rowpair slack>margin
    out=[]
    while len(out)<1:
        for _ in range(nmax):
            a,b,c,d=rng.random(4)
            D=np.array([[a,b,1-a-b],[c,d,1-c-d],[1-a-c,1-b-d,a+b+c+d-1]])
            if D.min()>=-1e-12 and D.max()<=1+1e-12 and rowpair_slack(D)>0.02:
                out.append(np.clip(D,0,1)); break
    return out[0]

def fit_deep(D,best_of=120):
    target=D
    def obj(x):
        a12,a23,a13,p=x
        if not(0<=a12<=np.pi/2 and 0<=a23<=np.pi/2 and 0<=a13<=np.pi/2 and -1<=p<=1): return 1e6
        return np.sum((Vmod(a12,a23,a13,p)-target)**2)
    best=1e9
    for _ in range(best_of):
        # latin-ish random init
        x0=[rng.uniform(0,np.pi/2),rng.uniform(0,np.pi/2),rng.uniform(0,np.pi/2),rng.uniform(-1,1)]
        r=minimize(obj,x0,method='Nelder-Mead',options=dict(maxiter=15000,xatol=1e-14,fatol=1e-15))
        best=min(best,r.fun)
    return np.sqrt(best)

# Look for points in rowpair region that CANNOT be reached by CKM map -> would prove U3 proper.
# Strategy: generate rowpair points from the CKM map is obviously reachable; need NON-CKM rowpair pts.
# Use a completely independent doubly-stochastic + rowpair sampler.
worst_deep=0
N=30
for it in range(N):
    D=sample_rowpair_ds(rng,2)
    err=fit_deep(D)
    if err>worst_deep: worst_deep=err
    tag="inside" if err<1e-6 else "!!NOT-REACHABLE"
    if err>1e-6 or it<3:
        print(f"it{it} slack={rowpair_slack(D):.4f} cmk-err={err:.3e} {tag}")
print("deep rowpair points NOT all reachable?" )
