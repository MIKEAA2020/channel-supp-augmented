import numpy as np
from scipy.optimize import minimize

def sample_ds(rng):
    while True:
        a,b,c,d = rng.random(4)
        D=np.array([[a,b,1-a-b],[c,d,1-c-d],[1-a-c,1-b-d,a+b+c+d-1]])
        if D.min()>=-1e-12 and D.max()<=1+1e-12:
            return np.clip(D,0,1)
def all_rowpair_ok(D,tol=1e-9):
    for (i,j) in [(0,1),(0,2),(1,2)]:
        t=np.sqrt(D[i,:]*D[j,:]); t=np.sort(t)
        if t[2]>t[0]+t[1]+tol: return False
    return True
def slack(D):
    m=1e9
    for (i,j) in [(0,1),(0,2),(1,2)]:
        t=np.sqrt(D[i,:]*D[j,:]); t=np.sort(t)
        m=min(m,t[0]+t[1]-t[2])
    return m
def reconstruct_U(D):
    r=np.sqrt(np.clip(D,0,None))
    best=None;bestf=np.inf
    for seed in range(6):
        ph=rng.random(9)*2*np.pi
        def obj(p):
            P=p.reshape(3,3); U=r*np.exp(1j*P)
            M=U@U.conj().T
            return np.sum(np.abs(M-np.eye(3))**2)
        res=minimize(obj,ph,method='Nelder-Mead',options=dict(maxiter=8000,xatol=1e-13,fatol=1e-13))
        if res.fun<bestf: bestf=res.fun; best=r*np.exp(1j*res.x.reshape(3,3))
    return best,bestf

rng=np.random.default_rng(1)
# hunt specifically for points that violate row-pair but reconstruct
found=0
N=4000
buckets={}
for _ in range(N):
    D=sample_ds(rng)
    s=slack(D)
    inside=s>=-1e-9
    U,resid=reconstruct_U(D)
    if not inside and resid<1e-5:
        print("violating but reconstr resid=",resid," slack=",s)
        print(np.round(D,6))
        found+=1
        if found>=3: break
print("found",found)
