# material-a77792911be0

Historical AI scientific source/proof material. Statements retain their original scope; this is not an independently reviewed theorem.

Public derivative: internal-record-identifiers-replaced.

---

# BR76 C162 edge20--21 exact circuit-height probe

This is a coordinator-derived exact scoped result from the literal 29-row input of immutable parent `figure-0458` (SHA ffdd3e223d750c32adce2b7e561c469f8926ada4b6a66b260c61a1ebd3e3eef5). It studies only fixed normals with a single RHS/support-height move. It is NOT a family exclusion.

Literal body has common RHS 1000 and rows:
```python
ROWS=[
[-869,125,-26],[-838,15,69],[-683,-218,271],[-462,408,-262],[-497,-352,388],[-368,-411,441],[-249,-445,472],[-200,464,-306],[-183,-452,479],[-48,-468,475],[15,449,-290],[0,-472,470],[126,-463,441],[169,-452,436],[284,-409,395],[326,-407,349],[391,-371,307],[372,39,-276],[423,-341,297],[421,90,-213],[474,-282,272],[508,-237,234],[523,150,-26],[531,-211,191],[556,70,43],[564,-52,131],[310,-232,298],[-1,-92,-83],[436,155,-144]]
]
```

In the parent, lex vertices20 and21 have active owner triples respectively (2,8,22) and (8,22,26), so the very short true edge20--21 is the common (8,22) edge of the four-plane circuit {2,8,22,26}. Keeping all normals and all other RHS values fixed:
- If h8 alone moves, exact concurrence of planes {2,8,22,26} occurs at
  h8*=3013382500/3013379 = 1000.0011614868226...
- If h22 alone moves, it occurs at
  h22*=1332240625/1332238 = 1000.0019703686579...

Thus the circuit really is extraordinarily close in pure support height. At exact test h8=1000+1/500, or h22=1000+1/500, the (8,22) edge has flipped to the alternative (2,26) edge, but the body remains V54/E81/F29,C162 strict121 with S=[0], U=[2,19], H=[42,44], no additional weak roots in the exact checker. Hence **crossing this one circuit on either one-coordinate support-height axis is not itself the desired U/H cancellation**. It is still a useful topology-changing entrance for coupled moves.

Conversely h8=1000-1/1000 or h22=1000-1/1000 (same incidence side) already gives strict132: S=[0], U=[2,19,42], H=[40,42],[42,44]. This shows the nearby equilibrium wall is even closer on the inward support-height side and creates a U/H pair rather than cancelling the existing packet.

Complete standalone exact replay below uses only Python stdlib Fractions. It reconstructs the maximal simple H-polytope, homogeneous volume centroid, stable-face / unstable-vertex / mixed-edge equilibrium census, and the circuit owner flip.

```python
#!/usr/bin/env python3
from fractions import Fraction as F
from itertools import combinations
from collections import defaultdict
ROWS=[
[-869,125,-26],[-838,15,69],[-683,-218,271],[-462,408,-262],[-497,-352,388],[-368,-411,441],[-249,-445,472],[-200,464,-306],[-183,-452,479],[-48,-468,475],[15,449,-290],[0,-472,470],[126,-463,441],[169,-452,436],[284,-409,395],[326,-407,349],[391,-371,307],[372,39,-276],[423,-341,297],[421,90,-213],[474,-282,272],[508,-237,234],[523,150,-26],[531,-211,191],[556,70,43],[564,-52,131],[310,-232,298],[-1,-92,-83],[436,155,-144]]
]
def det(a,b,c):
    return a[0]*(b[1]*c[2]-b[2]*c[1])-a[1]*(b[0]*c[2]-b[2]*c[0])+a[2]*(b[0]*c[1]-b[1]*c[0])
def sol(a,b,c,ha,hb,hc):
    D=det(a,b,c)
    if not D:return None
    return (F(det([ha,a[1],a[2]],[hb,b[1],b[2]],[hc,c[1],c[2]]),D),
            F(det([a[0],ha,a[2]],[b[0],hb,b[2]],[c[0],hc,c[2]]),D),
            F(det([a[0],a[1],ha],[b[0],b[1],hb],[c[0],c[1],hc]),D))
def dot(a,b):return sum(F(a[k])*b[k] for k in range(3))
def hull(hs):
    D={}
    for I in combinations(range(len(ROWS)),3):
        p=sol(ROWS[I[0]],ROWS[I[1]],ROWS[I[2]],hs[I[0]],hs[I[1]],hs[I[2]])
        if p and all(dot(r,p)<=hs[j] for j,r in enumerate(ROWS)):
            D[p]=tuple(j for j,r in enumerate(ROWS) if dot(r,p)==hs[j])
    v=sorted(D); o=[D[p] for p in v]
    sf=defaultdict(list)
    for q,O in enumerate(o):
        assert len(O)==3
        for i in O:sf[i].append(q)
    faces={}
    for i,vs in sf.items():
        A={x:[] for x in vs}
        for a,b in combinations(vs,2):
            if len(set(o[a])&set(o[b]))==2:A[a].append(b);A[b].append(a)
        assert all(len(A[x])==2 for x in vs)
        s=min(vs); cyc=[s]; prev=None; cur=s
        while True:
            n=A[cur][0] if A[cur][0]!=prev else A[cur][1]
            if n==s:break
            cyc.append(n);prev,cur=cur,n
        assert len(cyc)==len(vs);faces[i]=cyc
    E={}
    for a,b in combinations(range(len(v)),2):
        I=tuple(sorted(set(o[a])&set(o[b])))
        if len(I)==2:E[(a,b)]=I
    assert len(v)-len(E)+len(faces)==2
    return v,o,faces,E
def mass(v,faces):
    V=F(0);M=[F(0),F(0),F(0)]
    for cyc in faces.values():
        a=v[cyc[0]]
        for t in range(1,len(cyc)-1):
            b,c=v[cyc[t]],v[cyc[t+1]]
            w=abs(F(det(a,b,c),6));V+=w
            for k in range(3):M[k]+=w*(a[k]+b[k]+c[k])/4
    return V,tuple(x/V for x in M)
def colsolve(ns,y):
    return sol([ns[0][0],ns[1][0],ns[2][0]],[ns[0][1],ns[1][1],ns[2][1]],[ns[0][2],ns[1][2],ns[2][2]],*y)
def audit(hs):
    v,o,faces,E=hull(hs);V,c=mass(v,faces)
    S=[];U=[];H=[];wS=[];wU=[];wH=[]
    for i in faces:
        n=ROWS[i];s=hs[i]-dot(n,c);nn=sum(F(z*z) for z in n)
        y=tuple(s*F(n[k],nn) for k in range(3));x=tuple(c[k]+y[k] for k in range(3))
        q=[dot(ROWS[j],x)-hs[j] for j in range(len(ROWS)) if j!=i]
        if all(z<0 for z in q):S.append(i)
        elif all(z<=0 for z in q):wS.append(i)
    for q,p in enumerate(v):
        y=tuple(p[k]-c[k] for k in range(3));lam=colsolve([ROWS[i] for i in o[q]],y)
        if all(z>0 for z in lam):U.append(q)
        elif all(z>=0 for z in lam):wU.append(q)
    for (a,b),(i,j) in E.items():
        ni,nj=ROWS[i],ROWS[j];A=dot(ni,ni);B=dot(ni,nj);C=dot(nj,nj)
        si=hs[i]-dot(ni,c);sj=hs[j]-dot(nj,c);D=A*C-B*B
        al=(si*C-sj*B)/D;be=(sj*A-si*B)/D
        y=tuple(al*ni[k]+be*nj[k] for k in range(3));x=tuple(c[k]+y[k] for k in range(3))
        q=[dot(ROWS[k],x)-hs[k] for k in range(len(ROWS)) if k not in (i,j)]
        if al>0 and be>0 and all(z<0 for z in q):H.append((a,b))
        elif al>=0 and be>=0 and all(z<=0 for z in q):wH.append((a,b))
    return v,o,E,(len(v),len(E),len(faces)),(S,U,H),(wS,wU,wH),V,c
B=[F(1000)]*29
v,o,E,n,cls,w,_,_=audit(B)
assert n==(54,81,29) and cls==([0],[2,19],[(42,44)]) and w==([],[],[])
assert o[20]==(2,8,22) and o[21]==(8,22,26) and E[(20,21)]==(8,22)
p=sol(ROWS[2],ROWS[22],ROWS[26],F(1000),F(1000),F(1000))
h8=dot(ROWS[8],p);assert h8==F(3013382500,3013379)
p=sol(ROWS[2],ROWS[8],ROWS[26],F(1000),F(1000),F(1000))
h22=dot(ROWS[22],p);assert h22==F(1332240625,1332238)
for k in (8,22):
    hs=B[:];hs[k]+=F(1,500)
    v,o,E,n,cls,w,_,_=audit(hs)
    assert n==(54,81,29) and cls==([0],[2,19],[(42,44)]) and w==([],[],[])
    assert E[(20,21)]==(2,26)
for k in (8,22):
    hs=B[:];hs[k]-=F(1,1000)
    v,o,E,n,cls,w,_,_=audit(hs)
    assert n==(54,81,29) and cls==([0],[2,19,42],[(40,42),(42,44)]) and w==([],[],[])
print("BR76_C162_EDGE20_21_CIRCUIT_HEIGHT_PROBE_PASS",h8,h22)
```

Run:
`python -B -S BR76_C162_EDGE20_21_CIRCUIT_HEIGHT_PROBE.py`

Expected terminal marker:
`BR76_C162_EDGE20_21_CIRCUIT_HEIGHT_PROBE_PASS 3013382500/3013379 1332240625/1332238`
