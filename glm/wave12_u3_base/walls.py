import numpy as np, itertools

def g_wall(D,i,j,k):
    """hypotenuse = product column k for row pair (i,j). Return sum(legs)-hyp (0 on wall).
       i<j rows. {l,m}= other columns. legs are the other two product-columns."""
    cols=[0,1,2]; l,m=[c for c in cols if c!=k]
    hyp=np.sqrt(D[i,k]*D[j,k])
    leg=np.sqrt(D[i,l]*D[j,l])+np.sqrt(D[i,m]*D[j,m])
    return leg-hyp   # 0 => degenerate with col-k as hypotenuse-or-equal

def perms(names_ok=True):
    import itertools
    return [''.join(map(str,s)) for s in itertools.permutations('123')]
def Pmat(sigstr):
    M=np.zeros((3,3))
    for r,ch in enumerate(sigstr): M[r,int(ch)-1]=1.0
    return M
names=perms(); Ps={n:Pmat(n) for n in names}

def is_transp_edge(a,b):
    # permutation indices differ in exactly two positions
    return sum(x!=y for x,y in zip(a,b))==2

edges=[]
for i in range(6):
    for j in range(i+1,6):
        if is_transp_edge(names[i],names[j]): edges.append((names[i],names[j]))
print("9 transposition edges:")
for e in edges: print("  ",e)

walls=[]  # (i,j,k) with i<j rows (0-idx), k hypotenuse col
for (i,j) in [(0,1),(0,2),(1,2)]:
    for k in range(3): walls.append((i,j,k))
def wname(w): return f"W({w[0]+1},{w[1]+1}|{w[2]+1})"

print("\nIncidence: which wall contains which edge (test g=0 on 20 samples along edge)")
inc={w:[] for w in walls}
for (a,b) in edges:
    E=[]
    for w in walls:
        gs=[]
        for t in np.linspace(0,1,21):
            D=(1-t)*Ps[a]+t*Ps[b]
            gs.append(g_wall(D,*w))
        if max(abs(np.array(gs)))<1e-9: E.append(w)
    inc_here=E
    print(a,"-",b,":", ",".join(wname(w) for w in E) if E else "NONE")

# Vertices: test which walls contain each vertex
print("\nVertex containment in walls:")
for n in names:
    V=[w for w in walls if abs(g_wall(Ps[n],*w))<1e-12]
    print(n, ":", ",".join(wname(w) for w in V) if V else "NONE")
