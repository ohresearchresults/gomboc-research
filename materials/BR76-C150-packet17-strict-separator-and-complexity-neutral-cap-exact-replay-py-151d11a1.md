# material-151d11a1db01

AI research material · [Export notes](../catalog/coverage.md#text-records)

---

#!/usr/bin/env python3
from fractions import Fraction as F
from itertools import combinations

PARENT_ASSIGNMENT = "figure-0463"
PARENT_RESULT_SHA256 = "e7b52f322ec02b7d6c34a4cdb992622c807fb2f6f7bf868299cc1685c7be5bc6"
ROWS = [
[-865,126,-26],[-834,7,77],[-683,-218,271],[-440,408,-262],
[-497,-352,388],[-368,-411,441],[-249,-445,472],[-194,463,-300],
[-181,-452,479],[-48,-468,475],[17,452,-290],[0,-472,470],
[126,-463,441],[171,-449,436],[286,-405,397],[316,-407,361],
[387,-371,311],[370,39,-276],[423,-335,304],[421,96,-209],
[476,-266,282],[510,-223,248],[524,153,-24],[531,-209,184],
[556,70,43],[564,-52,135],[310,-228,274],[15,-96,-83],[450,126,-181]
]
PACKET = [0,1,2,3,4,5,6,7,8,9,11,21,22,23,25,39,44]

def det3(a,b,c):
    return (a[0]*(b[1]*c[2]-b[2]*c[1])
           -a[1]*(b[0]*c[2]-b[2]*c[0])
           +a[2]*(b[0]*c[1]-b[1]*c[0]))

def solve3(A,b):
    d=det3(A[0],A[1],A[2])
    if d==0:
        return None
    ans=[]
    for j in range(3):
        M=[list(r) for r in A]
        for i in range(3):
            M[i][j]=b[i]
        ans.append(det3(M[0],M[1],M[2])/d)
    return tuple(ans)

def dot(a,b):
    return sum(x*y for x,y in zip(a,b))

def enumerate_vertices(rows,rhs):
    table={}
    for I in combinations(range(len(rows)),3):
        x=solve3([rows[i] for i in I],[rhs[i] for i in I])
        if x is None:
            continue
        if all(dot(rows[i],x) <= rhs[i] for i in range(len(rows))):
            owners=tuple(i for i in range(len(rows)) if dot(rows[i],x)==rhs[i])
            table[x]=owners
    verts=sorted(table)
    return verts,[table[x] for x in verts]

def true_edges(owners):
    ans=[]
    for i,j in combinations(range(len(owners)),2):
        common=tuple(sorted(set(owners[i]) & set(owners[j])))
        if len(common)==2:
            ans.append((i,j,common))
    return ans

R=[tuple(F(v) for v in row) for row in ROWS]
h=[F(1000)]*len(R)
V,O=enumerate_vertices(R,h)
E=true_edges(O)
assert len(V)==50 and len(E)==75 and all(len(o)==3 for o in O)
assert [e for e in E if e[:2]==(39,41)]==[(39,41,(10,28))]
assert O[18]==(6,7,22)

q=(F(578),F(69),F(1000))
values=[dot(q,v) for v in V]
mx=max((values[i],i) for i in PACKET)
mn=min((values[i],i) for i in range(len(V)) if i not in PACKET)
assert mx==(F(-38132531000,33827071),39)
assert mn==(F(-66691400,6112141),48)
assert mx[0] < F(-569) < mn[0]

R2=R+[tuple(-a for a in q)]
h2=h+[F(569)]
W,P=enumerate_vertices(R2,h2)
E2=true_edges(P)
active=sorted({k for o in P for k in o})
capverts=[i for i,o in enumerate(P) if 29 in o]
assert len(W)==50 and len(E2)==75 and all(len(o)==3 for o in P)
assert len(active)==27
assert active==[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,20,21,22,23,24,25,28,29]
assert len(capverts)==17
old_index={v:i for i,v in enumerate(V)}
common=sorted(old_index[v] for v in W if v in old_index)
retained=sorted(set(range(50))-set(PACKET))
assert common==retained and len(common)==33
assert 19 not in active and 26 not in active and 27 not in active and 29 in active
assert 50-75+27==2

print("BR76_C150_PACKET17_STRICT_SEPARATOR_COMPLEXITY_NEUTRAL_CAP_PASS")
print("separator_q",tuple(int(x) for x in q),"threshold",-569)
print("max_packet",mx[0],"vertex",mx[1])
print("min_retained",mn[0],"vertex",mn[1])
print("parent_VEF",50,75,27,"cap_VEF",len(W),len(E2),len(active))
print("cap_vertices",capverts)
print("active_rows",active)
