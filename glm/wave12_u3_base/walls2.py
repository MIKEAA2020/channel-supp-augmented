import numpy as np, itertools
from walls import g_wall
def Pmat(s): 
    M=np.zeros((3,3))
    for r,ch in enumerate(s): M[r,int(ch)-1]=1.0
    return M
names=[''.join(map(str,x)) for x in itertools.permutations('123')]
Ps={n:Pmat(n) for n in names}
def is_transp(a,b): return sum(x!=y for x,y in zip(a,b))==2
edges=[]
for i in range(6):
    for j in range(i+1,6):
        if is_transp(names[i],names[j]): edges.append((names[i],names[j]))
walls=[(i,j,k) for (i,j) in [(0,1),(0,2),(1,2)] for k in range(3)]
def wname(w): return f"W({w[0]+1},{w[1]+1}|{w[2]+1})"

print("For each transposition edge: the ONE wall it is NOT contained in")
for (a,b) in edges:
    notin=[]
    for w in walls:
        gs=[g_wall((1-t)*Ps[a]+t*Ps[b],*w) for t in np.linspace(0,1,41)]
        if max(abs(np.array(gs)))>1e-9: notin.append(w)
    print(f"{a}-{b}: NOT in {[wname(w) for w in notin]}")

# interpret: an edge = 2x2 free block. Find which rowpair/col is the "isolated separating".
# test whether interior of wall A meets interior of wall B (two degeneracies both strict-boundary),
# i.e. is W(A)∩W(B) (both equalities tight) 2-dim inside int(B3)?
print("\nPairwise wall intersections: sample B3 interior points where both g_A~0 and g_B~0")
# detect if there's a codim-2 locus of simultaneous double-degeneracy inside int(B3)
# Use random search for points in int B3 (all entries>0) with two wall-equalities.
from scipy.optimize import minimize
def in_intB3(D): return D.min()>1e-6 and D.max()<1-1e-6
def gen_intds():
    while True:
        a,b,c,d=np.random.random(4)
        D=np.array([[a,b,1-a-b],[c,d,1-c-d],[1-a-c,1-b-d,a+b+c+d-1]])
        if D.min()>0.01 and D.max()<0.99: return D
rng=np.random.default_rng(5)
def find_double(wA,wB):
    best=1e9; bestD=None
    for _ in range(40):
        D=gen_intds()
        def o(x):
            Dt=gen_intds()  # not used
            # optimize in 4 coords toward both walls
            return 0
        # local refine with coordinates
    return None
# simpler: for given wA,wB check feasibility of D in int B3 with g_A=g_B=0 via Nelder over 4 coords
def coord(x):
    a,b,c,d=x
    return np.array([[a,b,1-a-b],[c,d,1-c-d],[1-a-c,1-b-d,a+b+c+d-1]])
def feas(wA,wB):
    def obj(x):
        a,b,c,d=x
        if not(0<=a<=1 and 0<=b<=1 and 0<=c<=1 and 0<=d<=1): return 1e3
        D=coord(x)
        if D.min()<-1e-9 or D.max()>1+1e-9: return 1e3
        pen=0
        if D.min()<0.001: pen+= (0.001-D.min())*1e4  # push interior
        return g_wall(D,*wA)**2+g_wall(D,*wB)**2+pen
    best=1e9
    for _ in range(30):
        x0=rng.random(4)
        r=minimize(obj,x0,method='Nelder-Mead',options=dict(maxiter=6000,xatol=1e-12,fatol=1e-13))
        best=min(best,r.fun)
    return np.sqrt(best)
# sample a subset of pairs
pairs=[((0,1,0),(0,2,0)),((0,1,0),(0,1,1)),((0,1,0),(1,2,2)),((0,2,1),(1,2,0)),((0,1,2),(0,2,2))]
for pA,pB in pairs:
    r=feas(pA,pB)
    print(f"{wname(pA)} ∩ {wname(pB)} residual={r:.2e}", "-> interior 2-locus EXISTS" if r<1e-3 else "-> ~only at boundary/vertex")
