import json,sys,math,hashlib
from pathlib import Path
from fractions import Fraction as F
sys.set_int_max_str_digits(0)
def dot(a,b):
    return sum(x*y for x,y in zip(a,b))
d=Path(sys.argv[1])
raw=json.loads((d/'RAW.json').read_text())
a=json.loads((d/'A.json').read_text())
labels=json.loads((d/'LABELS.json').read_text())
N=raw['I']; c=list(map(F,a['raw_centroid']))
den=math.lcm(*(z.denominator for z in c))
C=[int(den*z) for z in c]
H=[raw['D']*den-dot(n,C) for n in N]
assert min(H)>0
L=[dot(n,n) for n in N]
adj=[{j for j in range(len(N))
      if H[i]*dot(N[i],N[j])-H[j]*L[i]>0}
     for i in range(len(N))]
roots=[i for i,z in enumerate(adj) if not z]
assert [labels[i] for i in roots]==[3,30]
r,u=labels.index(3),labels.index(30)
def reach(root):
    R={root}
    while True:
        T=R|{i for i,z in enumerate(adj) if z&R}
        if T==R:
            return R
        R=T
R=reach(r); B=set(range(len(N)))-R
assert B==reach(u) and R.isdisjoint(B)
assert all(adj[i]<=B for i in B)
assert all(L[i]*H[u]**2<=L[u]*H[i]**2 for i in B)
beta=F(99,100)
checked=[]
for j in sorted(R):
    rhs=(2*beta.numerator*L[u]*H[j]
         -beta.denominator*dot(N[u],N[j])*H[u])
    lhs=beta.denominator**2*L[u]*L[j]*H[u]**2
    assert rhs>0 and rhs**2>lhs,j
    checked.append(labels[j])
result=dict(
    status='EXACT_CAP118_POLAR_BASIN_AND_ONE_NEW_POLE_OBSTRUCTION_PASS',
    reference='own centroid of unchanged physical CAP118; not polar centroid',
    root_basin=[labels[i] for i in sorted(R)],
    unwanted_basin=[labels[i] for i in sorted(B)],
    root_basin_size=len(R),unwanted_basin_size=len(B),
    two_hop_capacity_upper=str(beta),tested_root_labels=checked,
    raw_sha256=hashlib.sha256((d/'RAW.json').read_bytes()).hexdigest())
(d/'POLAR_BASIN.json').write_text(json.dumps(result,sort_keys=True))
print(result['status'],len(R),len(B))
