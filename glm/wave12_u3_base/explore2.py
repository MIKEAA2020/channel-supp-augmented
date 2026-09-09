import numpy as np
from scipy.optimize import minimize

def sample_ds(rng):
    # generic doubly stochastic via projecting; easier: build from 4 dirichlet-ish.
    while True:
        a,b,c,d = rng.random(4)
        D=np.array([[a,b,1-a-b],[c,d,1-c-d],[1-a-c,1-b-d,a+b+c+d-1]])
        if D.min()>=-1e-12 and D.max()<=1+1e-12:
            return np.clip(D,0,1)
def tri_ok_arr(a, tol=1e-9):
    a=np.sort(a); return a[2]<=a[0]+a[1]+tol
def all_rowpair_ok(D,tol=1e-9):
    for (i,j) in [(0,1),(0,2),(1,2)]:
        t=np.sqrt(D[i,:]*D[j,:])
        if not tri_ok_arr(t,tol): return False
    return True
def slack(D):
    # min over inequalities of (a0+a1-a2) i.e. how strict; negative => violated
    m=1e9
    for (i,j) in [(0,1),(0,2),(1,2)]:
        t=np.sqrt(D[i,:]*D[j,:]); t=np.sort(t)
        m=min(m,t[0]+t[1]-t[2])
    return m

def reconstruct_U(D, tol=1e-7):
    r=np.sqrt(np.clip(D,0,None))
    ph=np.zeros(9)
    def obj(p):
        P=p.reshape(3,3)
        U=r*np.exp(1j*P)
        # fix gauge: first column phases can be absorbed into right phases; keep but objective invariant partly
        M=U@U.conj().T
        return np.sum(np.abs(M-np.eye(3))**2)
    res=minimize(obj, ph, method='Nelder-Mead', options=dict(maxiter=4000,xatol=1e-12,fatol=1e-12))
    U=r*np.exp(1j*res.x.reshape(3,3))
    return U, res.fun

rng=np.random.default_rng(1)
N=400
ok_yes=0; ok_reached=0
for _ in range(N):
    D=sample_ds(rng)
    inside=all_rowpair_ok(D)
    U,resid=reconstruct_U(D)
    if inside:
        ok_yes+=1
        if resid<1e-6: ok_reached+=1
        else:
            # strict interior should reconstruct; print fails
            if slack(D)>1e-5:
                print("INTERIOR FAIL resid=",resid,"slack",slack(D))
    else:
        # violating points: resid should stay >0
        if resid<1e-6:
            print("OUTSIDE reconstructed resid=",resid,"slack",slack(D))
print(f"sample: {ok_yes}/{N} inside. inside reconstructed: {ok_reached}/{ok_yes}")
