# material-192e14a57e44

AI research material

---

from fractions import Fraction as Q
from itertools import combinations
import json

def vec(a): return tuple(Q(x) for x in a)
def add(a,b): return tuple(x+y for x,y in zip(a,b))
def sub(a,b): return tuple(x-y for x,y in zip(a,b))
def mul(c,a): return tuple(c*x for x in a)
def dot(a,b): return sum(x*y for x,y in zip(a,b))
def cross(a,b): return (a[1]*b[2]-a[2]*b[1],a[2]*b[0]-a[0]*b[2],a[0]*b[1]-a[1]*b[0])
def det(a,b,c): return dot(a,cross(b,c))
def outer(a,b): return tuple(tuple(x*y for y in b) for x in a)
def matadd(A,B): return tuple(tuple(x+y for x,y in zip(a,b)) for a,b in zip(A,B))
def matscale(c,A): return tuple(tuple(c*x for x in a) for a in A)
def mv(A,v): return tuple(dot(a,v) for a in A)
def transpose(A): return tuple(zip(*A))
def inv(A):
    a,b,c=A
    D=det(a,b,c)
    assert D
    return matscale(1/D,transpose((cross(b,c),cross(c,a),cross(a,b))))
ZERO=(Q(0),)*3
ZMAT=(ZERO,)*3
ID=tuple(tuple(Q(i==j) for j in range(3)) for i in range(3))

def hull(points):
    V=list(map(vec,points)); n=len(V)
    c=mul(Q(1,n),tuple(sum(x[j] for x in V) for j in range(3)))
    F={}
    for i,j,k in combinations(range(n),3):
        normal=cross(sub(V[j],V[i]),sub(V[k],V[i]))
        if normal==ZERO: continue
        h=dot(normal,V[i]); s=[dot(normal,v)-h for v in V]
        if max(s)>0 and min(s)<0: continue
        if min(s)==max(s)==0: continue
        if max(s)>0: normal=mul(-1,normal); h=-h; s=[-x for x in s]
        ids=tuple(m for m in range(n) if s[m]==0)
        F[ids]=(normal,h)
    facets=[]; planes=[]
    for ids,(normal,h) in sorted(F.items()):
        nxt={}
        for i,j in combinations(ids,2):
            ss=[dot(normal,cross(sub(V[j],V[i]),sub(V[k],V[i]))) for k in ids if k not in (i,j)]
            if min(ss)>0: nxt[i]=j
            elif max(ss)<0: nxt[j]=i
        assert len(nxt)==len(ids),(ids,nxt)
        cyc=[min(ids)]
        while nxt[cyc[-1]]!=cyc[0]:
            cyc.append(nxt[cyc[-1]]); assert len(cyc)<=len(ids)
        assert len(cyc)==len(ids)
        facets.append(tuple(cyc)); planes.append((normal,h))
    edges={}
    for f,cyc in enumerate(facets):
        for a,b in zip(cyc,cyc[1:]+cyc[:1]):
            edges.setdefault(tuple(sorted((a,b))),[]).append(f)
    assert set(x for e in edges for x in e)==set(range(n))
    assert all(len(fs)==2 for fs in edges.values())
    assert n-len(edges)+len(facets)==2
    vol=Q(0); first=ZERO; raw=ZMAT
    for cyc in facets:
        for j in range(1,len(cyc)-1):
            vv=[c,V[cyc[0]],V[cyc[j]],V[cyc[j+1]]]
            w=det(sub(vv[1],c),sub(vv[2],c),sub(vv[3],c))/6
            assert w>0
            ss=tuple(sum(v[k] for v in vv) for k in range(3))
            R=outer(ss,ss)
            for v in vv: R=matadd(R,outer(v,v))
            vol+=w; first=add(first,mul(w/4,ss)); raw=matadd(raw,matscale(w/20,R))
    g=mul(1/vol,first); cov=matadd(matscale(1/vol,raw),matscale(-1,outer(g,g)))
    X=[sub(v,g) for v in V]
    poles=[mul(1/(h-dot(no,g)),no) for no,h in planes]
    face_centers=[]
    for cyc,qi in zip(facets,poles):
        A=Q(0); C=ZERO
        for j in range(1,len(cyc)-1):
            a,b,c1=[X[k] for k in (cyc[0],cyc[j],cyc[j+1])]
            w=dot(qi,cross(sub(b,a),sub(c1,a)))
            assert w>0
            A+=w; C=add(C,mul(w/3,add(add(a,b),c1)))
        face_centers.append(mul(1/A,C))
    return dict(vertices=V,X=X,facets=facets,edges=edges,poles=poles,volume=vol,g=g,cov=cov,face_centers=face_centers)

def mechanics(P,N=ID):
    M=inv(N); X=P['X']; qq=P['poles']
    Dv=[[dot(x,mv(M,sub(y,x))) for y in X] for x in X]
    Dq=[[dot(q,mv(N,sub(r,q))) for r in qq] for q in qq]
    U=[i for i,row in enumerate(Dv) if all(x<0 for j,x in enumerate(row) if i!=j)]
    S=[i for i,row in enumerate(Dq) if all(x<0 for j,x in enumerate(row) if i!=j)]
    H=[]; zeros=[]
    for (i,j),(f,g) in sorted(P['edges'].items()):
        signs=(Dv[i][j],Dv[j][i],Dq[f][g],Dq[g][f])
        if all(x<0 for x in signs): H.append((i,j))
        if any(x==0 for x in signs): zeros.append(((i,j),(f,g),signs))
    assert len(S)+len(U)-len(H)==2 or zeros
    return dict(S=S,U=U,H=H,zeros=zeros)

def example(H=Q(5,2)):
    B=[(-2,-2,0),(2,-2,0),(2,2,0),(-2,2,0)]
    T=[(3,3,H),(-1,3,H),(-2,1,H),(-Q(7,4),0,H),(-1,-1,H),(3,-1,H)]
    return hull(B+T)

def summary(P):
    R=mechanics(P)
    print('f',len(P['X']),len(P['edges']),len(P['facets']),'V',P['volume'],'g',P['g'],'SUH',len(R['S']),len(R['U']),len(R['H']),'zero',len(R['zeros']))
    for i,(f,q) in enumerate(zip(P['facets'],P['poles'])):
        good=[j for j,x in enumerate(P['X']) if j not in f and (2-dot(q,x))**2-dot(q,q)*dot(x,x)>=0]
        neighbors=sorted({g if i==k else k for fs in P['edges'].values() if i in fs for k,g in [fs]})
        hits={j:tuple(v for v in P['facets'][j] if v not in f and v in good) for j in neighbors}
        print(i,f,'q',q,'good',good,'neighbors',hits,'stable',i in R['S'])

if __name__=='__main__':
    summary(example())
