import numpy as np
from scipy.optimize import minimize
from moduli import Vmod, rng

def Vnames():
    import itertools
    return [''.join(map(str,s)) for s in itertools.permutations('123')]
def Pmat(sig):
    M=np.zeros((3,3))
    for r,c in enumerate(sig): M[r,c]=1.0
    return M
names=Vnames()
Ps={n:Pmat([int(ch)-1 for ch in n]) for n in names}
def rowpair_slack(D):
    m=1e9
    for (i,j) in [(0,1),(0,2),(1,2)]:
        t=np.sqrt(D[i,:]*D[j,:]); t=np.sort(t); m=min(m,t[0]+t[1]-t[2])
    return m
def fit_deep(D,best_of=90):
    def obj(x):
        a12,a23,a13,p=x
        if not(0<=a12<=np.pi/2 and 0<=a23<=np.pi/2 and 0<=a13<=np.pi/2 and -1<=p<=1): return 1e6
        return np.sum((Vmod(a12,a23,a13,p)-D)**2)
    best=1e9
    for _ in range(best_of):
        x0=[rng.uniform(0,np.pi/2),rng.uniform(0,np.pi/2),rng.uniform(0,np.pi/2),rng.uniform(-1,1)]
        r=minimize(obj,x0,method='Nelder-Mead',options=dict(maxiter=15000,xatol=1e-14,fatol=1e-15))
        best=min(best,r.fun)
    return np.sqrt(best)

# triangle faces: each has 2 transposition-IN edges + 1 cyclic-OUT edge.
# enumerate 2-faces of B3 = triples of vertices where exactly two pairs are transposition
def is_transp(a,b): # differing in exactly 2 positions
    return sum(x!=y for x,y in zip(a,b))==2
import itertools
verts=names
faces=[]
for tri in itertools.combinations(verts,3):
    tr=[is_transp(tri[i],tri[j]) for i in range(3) for j in range(i+1,3)]
    if tr.count(True)==2: faces.append(tri)
print("num triangle 2-faces:",len(faces))
print("\nTest interior of each 2-face (weighted center) for rowpair slack & membership")
for tri in faces[:]:
    # interior point: 1/3,1/3,1/3
    D=(Ps[tri[0]]+Ps[tri[1]]+Ps[tri[2]])/3
    sl=rowpair_slack(D)
    err=fit_deep(D)
    print(tri,"slack=%.4f"%sl,"cmk_err=%.2e"%(err), "IN-IMAGE" if err<1e-6 else "OUT")

# test points very close to a transposition edge but into an adjacent 2-face (should be excluded)
print("\nJust-off transposition edge into 2-face:")
D0=Ps['123']; D1=Ps['132']   # a transposition edge
for eps in [1e-3,1e-2,0.05]:
    # push toward a third vertex on a 2-face containing the edge: find face {123,132,x}
    for tri in faces:
        if '123' in tri and '132' in tri:
            third=[v for v in tri if v not in ('123','132')][0]
            break
    # point = eps*third + (1-eps)*(midpoint of edge)... to stay in 2-face near edge
    edge_mid=(D0+D1)/2
    D=(1-eps)*edge_mid+eps*Ps[third]
    print(f"eps={eps} slack={rowpair_slack(D):.4f} cmk_err={fit_deep(D):.2e}")
