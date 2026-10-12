# material-54374c6e67c8

AI research material

<!-- historical-status:start -->
> **Historical AI material.** The title and claims below reflect the AI’s assessment at the time. Claims of proof, certification or completion are not a current verification verdict.
>
> [C622](../C622/README.md) passes the supplied exact checks; C<500 remains open; Minimum’s C≥34 remains a working lower bound requiring a consolidated proof. See [verification status and source gaps](../catalog/coverage.md).
<!-- historical-status:end -->

---

"""Exact H5 geometry and orthogonal edge pairs; no external proof inputs.
Python >=3.11 standard library. Fractions everywhere in the exact routines.
The optional locator imports this module, not conversely.
"""
from fractions import Fraction as Q
from itertools import combinations
from math import comb

FACES=((6,5,4,3,2,1,0),(8,7,0,1),(7,6,0),(1,2,8),
       (9,8,2,3),(9,3,4),(4,5,7,9),(6,7,5),(7,8,9))

def dot(a,b): return sum((x*y for x,y in zip(a,b)),Q(0))
def add(a,b): return tuple(x+y for x,y in zip(a,b))
def sub(a,b): return tuple(x-y for x,y in zip(a,b))
def scale(t,a): return tuple(t*x for x in a)
def cross(a,b): return (a[1]*b[2]-a[2]*b[1],a[2]*b[0]-a[0]*b[2],a[0]*b[1]-a[1]*b[0])
def det(A): return dot(A[0],cross(A[1],A[2]))
def transpose(A): return tuple(zip(*A))
def mv(A,v): return tuple(dot(row,v) for row in A)
def mm(A,B): return tuple(tuple(dot(row,col) for col in transpose(B)) for row in A)
def quad(v,A): return dot(v,mv(A,v))
def inv(A):
    d=det(A)
    assert d
    return tuple(tuple(x/d for x in row) for row in transpose((cross(A[1],A[2]),cross(A[2],A[0]),cross(A[0],A[1]))))
def positive(A): return A[0][0]>0 and A[0][0]*A[1][1]-A[0][1]**2>0 and det(A)>0

def body(theta):
    x,r,p,q,lam=map(Q,theta);s=1-lam
    b=((Q(1,4),0),(1-3*x/4,0),(1-p,p),(q,1-q),(0,1-3*r/4),(0,Q(1,4)),(Q(1,16),Q(1,16)))
    z=tuple((s*u,s*v,Q(0)) for u,v in b)+((Q(0),Q(0),Q(1)),(lam,Q(0),Q(1)),(Q(0),lam,Q(1)))
    area=(31-24*x*p-24*r*q)/64
    bx=Q(509,3072)-3*x*p/8+3*x*x*p/32+x*p*p/8-r*q*q/8
    by=Q(509,3072)-3*r*q/8+3*r*r*q/32+r*q*q/8-x*p*p/8
    D=lam+2*area*s*s
    K=(3*s**3*bx/2+s*s*lam*(1-3*x*p/4)/4+lam*lam/4,
       3*s**3*by/2+s*s*lam*(1-3*r*q/4)/4+lam*lam/4,
       area*s*s/2+lam/2+lam*lam/4)
    dd=Q(0);kk=(Q(0),)*3
    for face in FACES:
        a=z[face[0]]
        for j in range(1,len(face)-1):
            bb,cc=z[face[j]],z[face[j+1]];d=dot(a,cross(bb,cc))
            dd+=d;kk=add(kk,scale(d/4,add(add(a,bb),cc)))
    assert dd==D and kk==K and D>0
    g=scale(1/D,K);v=tuple(sub(a,g) for a in z)
    planar=(((Q(0),Q(-1)),Q(0),Q(0),1),((p,p-3*x/4),s*p*(1-3*x/4),lam*p,3),
            ((Q(1),Q(1)),s,lam,4),((q-3*r/4,q),s*q*(1-3*r/4),lam*q,5),
            ((Q(-1),Q(0)),Q(0),Q(0),6),((Q(-3),Q(-1)),-s/4,Q(0),7),((Q(-1),Q(-3)),-s/4,Q(0),2))
    ns=[None]*9;hs=[None]*9;ns[0]=(Q(0),Q(0),Q(-1));hs[0]=Q(0);ns[8]=(Q(0),Q(0),Q(1));hs[8]=Q(1)
    for n,h,t,f in planar:ns[f]=n+(h-t,);hs[f]=h
    poles=tuple(scale(1/(h-dot(n,g)),n) for n,h in zip(ns,hs))
    for f in range(9):
        assert hs[f]-dot(ns[f],g)>0
        for i in range(10):
            slack=hs[f]-dot(ns[f],z[i]);assert slack==0 if i in FACES[f] else slack>0
    for i in range(10):
        incident=[f for f in range(9) if i in FACES[f]]
        assert any(det(tuple(ns[f] for f in triple)) for triple in combinations(incident,3))
    # Exhaust all supporting vertex triples: no unlisted maximal facet.
    recovered=set()
    for i,j,k in combinations(range(10),3):
        n=cross(sub(z[j],z[i]),sub(z[k],z[i]));vals=[dot(n,sub(a,z[i])) for a in z]
        if any(n) and (all(t>=0 for t in vals) or all(t<=0 for t in vals)):
            recovered.add(tuple(l for l,t in enumerate(vals) if not t))
    assert recovered=={tuple(sorted(f)) for f in FACES}
    ef={}
    for f,face in enumerate(FACES):
        for i,j in zip(face,face[1:]+face[:1]):ef.setdefault(tuple(sorted((i,j))),[]).append(f)
    assert len(ef)==17 and all(len(f)==2 for f in ef.values())
    edges=tuple(sorted(ef));dual=tuple(sorted(tuple(sorted(f)) for f in ef.values()))
    # Geometric controls for reflection, affine in alpha.
    def Rval(alpha,i,j,k):
        n,h,t,f=planar[k]
        return (D-K[2])*h-(1+alpha)*dot(n,K[:2])+alpha*(D-K[2])*dot(n,z[i][:2])+(1+alpha)*K[2]*dot(n,z[j][:2])
    amax=[];limit=[]
    for j in range(7,10):
        bounds=[(Q(1),None)]
        for k in range(7):
            for i in range(7):
                r0=Rval(Q(0),i,j,k);slope=Rval(Q(1),i,j,k)-r0
                assert r0>0
                if slope<0:bounds.append((-r0/slope,(k,i,j)))
        a,b=min(bounds,key=lambda a:a[0]);amax.append(a);limit.append(b)
    A_min=min(2*(h-dot(n+(h-t,),g))-(t-dot(n,z[j][:2])) for n,h,t,f in planar for j in range(7,10))
    return {'theta':tuple(map(Q,theta)),'raw':z,'v':v,'poles':poles,'g':g,'volume':D/6,'D':D,'K':K,
            'edges':edges,'dual':dual,'ef':ef,'amax':tuple(amax),'limiting':tuple(limit),'Amin':A_min,'Rval':Rval}

# Ascending polynomial coefficients, with exact removal of trailing zeros.
def trim(a):
    a=list(a)
    while len(a)>1 and not a[-1]:a.pop()
    return a

def padd(a,b):
    c=[Q(0)]*max(len(a),len(b))
    for i,t in enumerate(a):c[i]+=t
    for i,t in enumerate(b):c[i]+=t
    return trim(c)
def pscale(c,a):return trim([c*t for t in a])
def pmul(a,b):
    c=[Q(0)]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b):c[i+j]+=x*y
    return trim(c)
def peval(p,t):
    y=Q(0)
    for x in p[::-1]:y=y*t+x
    return y

def linearquad(a,b,C):return [quad(a,C),2*dot(a,mv(C,b)),quad(b,C)]

def orthogonal_pairs(B):
    """Complete curve pieces plus exceptional points; rational exact topology.
    pieces: (edge ids,a,u,N0,N1,c,d,lo,hi), n(s)=(N0+s*N1)/(c+d*s).
    points include vertical fibres at their t endpoints, and all constant-square corners.
    """
    pieces=[];points=[]
    for ei,(i,j) in enumerate(B['edges']):
        a=B['v'][i];u=sub(B['v'][j],a)
        for fi,(k,l) in enumerate(B['dual']):
            b=B['poles'][k];vv=sub(B['poles'][l],b)
            A=dot(a,b);bb=dot(u,b);c=dot(a,vv);d=dot(u,vv)
            def point(s,t):
                w=add(a,scale(s,u));n=add(b,scale(t,vv));assert dot(w,n)==0
                points.append((ei,fi,s,t,w,n))
            if c==0 and d==0:
                if bb:
                    s=-A/bb
                    if 0<=s<=1:point(s,Q(0));point(s,Q(1))
                elif A==0:
                    for s in (Q(0),Q(1)):
                        for t in (Q(0),Q(1)):point(s,t)
                continue
            roots={Q(0),Q(1)}
            for a0,a1 in ((c,d),(A,bb),(A+c,bb+d)):
                if a1:
                    rr=-a0/a1
                    if 0<=rr<=1:roots.add(rr)
            roots=sorted(roots)
            for rr in roots:
                den=c+d*rr;num=A+bb*rr
                if den:
                    t=-num/den
                    if 0<=t<=1:point(rr,t)
                elif num==0:point(rr,Q(0));point(rr,Q(1))
            N0=sub(scale(c,b),scale(A,vv));N1=sub(scale(d,b),scale(bb,vv))
            for lo,hi in zip(roots,roots[1:]):
                mid=(lo+hi)/2;den=c+d*mid
                if den and 0<=-(A+bb*mid)/den<=1:
                    # A shared numerator/denominator zero is removable, n is constant.
                    if d and A*d==bb*c:
                        n=add(b,scale(-bb/d,vv));assert dot(add(a,scale(mid,u)),n)==0
                        pieces.append((ei,fi,a,u,n,(Q(0),)*3,Q(1),Q(0),lo,hi))
                    else:
                        assert c+d*lo and c+d*hi
                        pieces.append((ei,fi,a,u,N0,N1,c,d,lo,hi))
    return pieces,points

def bernstein(p,lo,hi):
    n=len(p)-1
    power=[sum(p[j]*comb(j,k)*lo**(j-k)*(hi-lo)**k for j in range(k,n+1)) for k in range(n+1)]
    return [sum(power[k]*Q(comb(i,k),comb(n,k)) for k in range(i+1)) for i in range(n+1)]

def exact_bound(B,C,U,max_depth=24):
    """Prove all continuum orthogonal products <= U or raise ArithmeticError."""
    assert positive(C);Ci=inv(C);pieces,pts=orthogonal_pairs(B);smallest=None;leaves=0;depth=0
    for ei,fi,s,t,w,n in pts:
        gap=U-quad(w,Ci)*quad(n,C)
        assert gap>=0,('point',ei,fi,str(s),str(t),str(gap))
    for ei,fi,a,u,N0,N1,c,d,lo,hi in pieces:
        poly=padd(pscale(U,pmul([c,d],[c,d])),pscale(-1,pmul(linearquad(a,u,Ci),linearquad(N0,N1,C))))
        todo=[(lo,hi,0)]
        while todo:
            l,h,dep=todo.pop();coef=bernstein(poly,l,h);mn=min(coef)
            if mn>=0:
                leaves+=1;depth=max(depth,dep);smallest=mn if smallest is None else min(smallest,mn)
            elif dep>=max_depth:
                raise ArithmeticError(('unclosed interval',ei,fi,str(l),str(h),str(mn)))
            else:
                m=(l+h)/2;todo.extend(((l,m,dep+1),(m,h,dep+1)))
    return {'edge_pairs':len(B['edges'])*len(B['dual']),'pieces':len(pieces),'points':len(pts),
            'leaves':leaves,'max_depth':depth,'smallest_bernstein':str(smallest)}

def aligned_reference(B,j,W):
    h=1-B['g'][2];m=B['v'][j][:2]
    return ((W[0][0]+m[0]**2,W[0][1]+m[0]*m[1],h*m[0]),
            (W[1][0]+m[0]*m[1],W[1][1]+m[1]**2,h*m[1]),
            (h*m[0],h*m[1],h*h))

def census(B,M):
    N=inv(M);assert positive(M)
    dp={(i,j):dot(B['v'][i],mv(M,sub(B['v'][j],B['v'][i]))) for e in B['edges'] for i,j in (e,e[::-1])}
    dq={(i,j):dot(B['poles'][i],mv(N,sub(B['poles'][j],B['poles'][i]))) for e in B['dual'] for i,j in (e,e[::-1])}
    U=[i for i in range(10) if all(t<0 for (a,b),t in dp.items() if a==i)]
    S=[i for i in range(9) if all(t<0 for (a,b),t in dq.items() if a==i)]
    H=[];weak=[]
    for e in B['edges']:
        i,j=e;f,g=B['ef'][e];p=(dp[i,j],dp[j,i],dq[f,g],dq[g,f])
        if all(t<0 for t in p):H.append(e)
        elif all(t<=0 for t in p):weak.append(e)
    assert len(S)+len(U)-len(H)==2
    return {'S':S,'U':U,'H':H,'weak_edges':weak,'zero_primitives':sum(x==0 for x in (*dp.values(),*dq.values()))}
