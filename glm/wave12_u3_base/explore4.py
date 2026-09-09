import numpy as np
rng=np.random.default_rng(2)
def slack(D):
    m=1e9
    for (i,j) in [(0,1),(0,2),(1,2)]:
        t=np.sqrt(D[i,:]*D[j,:]); t=np.sort(t)
        m=min(m,t[0]+t[1]-t[2])
    return m
mins=1e9; arg=None
N=300000
for _ in range(N):
    z=(rng.standard_normal((3,3))+1j*rng.standard_normal((3,3)))
    U,_=np.linalg.qr(z)
    D=np.abs(U)**2
    s=slack(D)
    if s<mins: mins=s; arg=D
print("min slack over",N,"random unitaries:",mins)
print("rows of arg:",np.round(arg,4))

# Check the OTHER natural pairing: for each pair of rows, the numbers sqrt(D_i1 D_j2),? 
# Test: maybe correct pairing is along specific antisymmetric combination. Let's test transpose too.
minsT=1e9
for _ in range(N):
    z=(rng.standard_normal((3,3))+1j*rng.standard_normal((3,3)))
    U,_=np.linalg.qr(z)
    D=np.abs(U)**2
    s=slack(D.T)
    if s<minsT: minsT=s
print("min slack of transpose:",minsT)
