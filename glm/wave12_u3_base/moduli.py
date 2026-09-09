import numpy as np

def Vmod(a12,a23,a13,p):
    """CKM-type unitary moduli. Return 3x3 D = |V|^2. p=cos(delta).
       Rows i cols j: V = R(12,th12).D(p).R(13,th13).D(-p).R(23,th23) convention below.
    """
    c12,s12=np.cos(a12),np.sin(a12)
    c23,s23=np.cos(a23),np.sin(a23)
    c13,s13=np.cos(a13),np.sin(a13)
    # use the explicit |V|^2 entries derived
    A = s12**2*c23**2 + c12**2*s23**2*s13**2 - 2*c12*s12*c23*s23*s13*p
    B = c12**2*c23**2 + s12**2*s23**2*s13**2 + 2*c12*s12*c23*s23*s13*p
    C = s12**2*s23**2 + c12**2*c23**2*s13**2 + 2*c12*s12*c23*s23*s13*p
    E = c12**2*s23**2 + s12**2*c23**2*s13**2 - 2*c12*s12*c23*s23*s13*p
    D = np.array([
        [c12**2*c13**2, s12**2*c13**2, s13**2],
        [A, B, s23**2*c13**2],
        [C, E, c23**2*c13**2],
    ])
    return D

def sample_moduli(rng):
    a12=rng.uniform(0,np.pi/2); a23=rng.uniform(0,np.pi/2); a13=rng.uniform(0,np.pi/2)
    p=rng.uniform(-1,1)
    return Vmod(a12,a23,a13,p)

# map back: given D find parameters
def fit_params(D, best_of=40):
    target=D
    def obj(x):
        a12,a23,a13,p=x
        if not (0<=a12<=np.pi/2 and 0<=a23<=np.pi/2 and 0<=a13<=np.pi/2 and -1<=p<=1):
            return 1e9
        return np.sum((Vmod(a12,a23,a13,p)-target)**2)
    best=(1e9,None)
    for _ in range(best_of):
        x0=[rng.uniform(0,np.pi/2),rng.uniform(0,np.pi/2),rng.uniform(0,np.pi/2),rng.uniform(-1,1)]
        # coarse grid init to be safe
        from scipy.optimize import minimize
        r=minimize(obj,x0,method='Nelder-Mead',options=dict(maxiter=8000,xatol=1e-13,fatol=1e-14))
        if r.fun<best[0]:
            best=(r.fun,r.x)
    return best

rng=np.random.default_rng(3)
if __name__=="__main__":
    # quick self check: sample moduli, refit, error small for generic interior
    errs=[]
    for _ in range(50):
        D=sample_moduli(rng)
        f,_=fit_params(D)
        errs.append(np.sqrt(f))
    print("median refit err:", np.median(errs))
