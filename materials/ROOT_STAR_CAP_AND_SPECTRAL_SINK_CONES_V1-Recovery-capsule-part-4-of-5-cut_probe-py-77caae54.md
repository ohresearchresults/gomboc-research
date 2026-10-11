# material-77caae5413c6

Historical AI scientific source/proof material. Statements retain their original scope; this is not an independently reviewed theorem.

---

from cap_geometry import *
from random import Random

def scc(n,edges):
    reach=[{i} for i in range(n)]
    for a,b in edges:reach[a].add(b)
    for k in range(n):
        for i in range(n):
            if k in reach[i]:reach[i]|=reach[k]
    used=set();cc=[]
    for i in range(n):
        if i in used:continue
        c={j for j in range(n) if j in reach[i] and i in reach[j]};used|=c;cc.append(c)
    return [c for c in cc if not any(a in c and b not in c for a,b in edges)]
def possible(u,v,B,k):
    D=dot(u,mv(B,v));R2=dot(u,mv(B,u))*dot(v,mv(B,v))
    return D>=0 or (k+1)**2*D**2<=(k-1)**2*R2
P=example();q=P['poles'];truearcs=sorted(tuple(ij) for fs in P['edges'].values() for ij in (fs,fs[::-1])); rng=Random(918731)
for sample in range(5000):
    if sample<15:B=tuple(tuple(Q((sample+1) if i==j==0 else (1 if i==j else 0)) for j in range(3))for i in range(3))
    else:
        X=tuple(tuple(Q(rng.randint(-4,4)) for _ in range(3)) for _ in range(3))
        B=matadd(ID,tuple(tuple(dot(x,y) for y in X)for x in X))
    for k in (Q(3,2),Q(2),Q(3),Q(4)):
        arcs=[(i,j) for i,j in truearcs if possible(q[i],sub(q[j],q[i]),B,k)]
        comps=scc(len(q),arcs)
        if len(comps)>=2 and all(len(c)>=2 for c in comps):
            print('FOUND',sample,'B',B,'k',k,'sinks',comps,'arcs',arcs,flush=True);raise SystemExit
print('NOT_FOUND')
