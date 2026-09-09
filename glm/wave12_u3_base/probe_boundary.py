import numpy as np, itertools
from moduli import fit_params, rng

def perms():
    P=[]
    for sig in itertools.permutations(range(3)):
        M=np.zeros((3,3))
        for r,c in enumerate(sig): M[r,c]=1.0
        P.append(M)
    return P

Ps=perms()
names=[''.join(map(str,s)) for s in itertools.permutations('123')]
print("permutation matrices:",names)

def membership_resid(D):
    f,_=fit_params(D,best_of=60)
    return np.sqrt(f)

# 1) vertices all in U3 ?
print("\nvertex resid:")
for i,M in enumerate(Ps):
    print(names[i], "resid",membership_resid(M))

# 2) every pair segment: sample t in (0.05..0.95), check resid
print("\npair segments: report max resid along 8 interior samples, and first t where resid small")
pair_in=[]
for i in range(6):
    for j in range(i+1,6):
        resids=[]
        inpts=0
        for t in np.linspace(0.05,0.95,8):
            D=(1-t)*Ps[i]+t*Ps[j]
            r=membership_resid(D)
            resids.append(r)
            if r<1e-4: inpts+=1
        flag='IN' if inpts==8 else ('part' if inpts>0 else 'OUT')
        pair_in.append((flag,i,j))
        print(f"{names[i]}-{names[j]} [{flag}] maxresid={max(resids):.1e} pts_in={inpts}/8")

print("\nSummary in/part/out counts:", )
from collections import Counter
print(Counter(p[0] for p in pair_in))
