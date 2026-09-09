import numpy as np
import moduli
from scipy.optimize import minimize
from moduli import Vmod, rng

def rowpair_slack(D):
    m=1e9
    for (i,j) in [(0,1),(0,2),(1,2)]:
        t=np.sqrt(D[i,:]*D[j,:]); t=np.sort(t); m=min(m,t[0]+t[1]-t[2])
    return m
def fit_deep(D,best_of=150):
    def obj(x):
        a12,a23,a13,p=x
        if not(0<=a12<=np.pi/2 and 0<=a23<=np.pi/2 and 0<=a13<=np.pi/2 and -1<=p<=1): return 1e6
        return np.sum((Vmod(a12,a23,a13,p)-D)**2)
    best=1e9;bx=None
    for _ in range(best_of):
        x0=[rng.uniform(0,np.pi/2),rng.uniform(0,np.pi/2),rng.uniform(0,np.pi/2),rng.uniform(-1,1)]
        r=minimize(obj,x0,method='Nelder-Mead',options=dict(maxiter=20000,xatol=1e-14,fatol=1e-16))
        if r.fun<best: best=r.fun;bx=r.x
    return np.sqrt(best), bx

# generate points in rowpair interior very close to wall (tiny positive slack), not on edge
def gen_nearwall(target_slack):
    for _ in range(400000):
        a,b,c,d=rng.random(4)
        D=np.array([[a,b,1-a-b],[c,d,1-c-d],[1-a-c,1-b-d,a+b+c+d-1]])
        if D.min()>0.01 and D.max()<0.99:
            s=rowpair_slack(D)
            if s>0 and abs(s-target_slack)<max(0.3*target_slack,2e-6):
                return D
    return None

for ts in [5e-5, 5e-4, 5e-3]:
    D=gen_nearwall(ts)
    if D is None:
        print(f"target slack {ts:.0e}: could not generate (slack rarely that small); use coarser")
        continue
    err,_=fit_deep(D)
    print(f"target slack {ts:.0e}: actual slack={rowpair_slack(D):.2e} cmk_err={err:.2e}", "IN" if err<1e-7 else "MARGINAL/OUT")

# branch count over a generic interior point: how many distinct (a12,a23,a13,p) give err~0?
D=moduli.sample_moduli(rng)
print("\nbranch structure: count distinct near-zero minima of generic interior point")
sol=[]
for _ in range(400):
    x0=[rng.uniform(0,np.pi/2),rng.uniform(0,np.pi/2),rng.uniform(0,np.pi/2),rng.uniform(-1,1)]
    def obj(x):
        a12,a23,a13,p=x
        if not(0<=a12<=np.pi/2 and 0<=a23<=np.pi/2 and 0<=a13<=np.pi/2 and -1<=p<=1): return 1e6
        return np.sum((Vmod(a12,a23,a13,p)-D)**2)
    r=minimize(obj,x0,method='Nelder-Mead',options=dict(maxiter=15000,xatol=1e-10,fatol=1e-11))
    if r.fun<1e-8:
        x=r.x
        key=tuple(np.round([np.sin(2*x[0]) if False else x[0],x[1],x[2],x[3]],6))
        if not any(np.allclose(x[:3],np.array(s[:3]),atol=1e-4) and abs(x[3]-s[3])<1e-3 for s in sol):
            sol.append(x)
print("distinct solutions (err<1e-8):",len(sol))
for x in sol: print("  a12=%.3f a23=%.3f a13=%.3f p=%.3f"%(x[0],x[1],x[2],x[3]))
