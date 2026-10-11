# material-3ba570f2ef54

Historical AI scientific source/proof material. Statements retain their original scope; this is not an independently reviewed theorem.

---

#!/usr/bin/env python3
"""Exact actual-volume cut-and-stack regular horizon control, stdlib only.
Run with assertions enabled: python -B -S cut_stack_regular_horizon.py
No numerical hull or external checkpoint is used.
"""
from fractions import Fraction as F
from itertools import combinations
from math import gcd
import json


def add(a,b): return tuple(x+y for x,y in zip(a,b))
def sub(a,b): return tuple(x-y for x,y in zip(a,b))
def scale(c,a): return tuple(c*x for x in a)
def dot(a,b): return sum(x*y for x,y in zip(a,b))
def cross(a,b): return (a[1]*b[2]-a[2]*b[1],a[2]*b[0]-a[0]*b[2],a[0]*b[1]-a[1]*b[0])
def outer(a,b): return tuple(tuple(x*y for y in b) for x in a)
def matadd(A,B): return tuple(add(a,b) for a,b in zip(A,B))
def matscale(c,A): return tuple(scale(c,a) for a in A)
def mv(A,x): return tuple(dot(a,x) for a in A)
def det(A): return dot(A[0],cross(A[1],A[2]))
def transpose(A): return tuple(zip(*A))
def inverse(A):
    d=det(A); assert d
    # Adjugate is the transpose of row cross products.
    return matscale(1/d,transpose((cross(A[1],A[2]),cross(A[2],A[0]),cross(A[0],A[1]))))
def pd(A):
    return A[0][0]>0 and A[0][0]*A[1][1]-A[0][1]*A[1][0]>0 and det(A)>0

def primitive(v):
    l=1
    for x in v: l=l*x.denominator//gcd(l,x.denominator)
    a=tuple(int(x*l) for x in v); g=0
    for x in a:g=gcd(g,abs(x))
    assert g
    return tuple(x//g for x in a)

CYCLES=((0,3,4,1,7,6),(0,2,5,3),(0,6,8,2),(1,4,5,2),(1,2,8,7),(3,9,4),(3,5,9),(4,9,5),(6,7,8))
BETA=F(2,5)
FCUT=(F(3,10),F(3,5),F(7,10))
STACK=F(2,5)
WEIGHTS=(F(1,5),F(2,5),F(2,5))
LEFT_SCALE=F(1)
CWIDTH=(F(63,5000),F(63,2500),F(189,5000))
METRIC=((F(7),F(1),F(2)),(F(1),F(5),F(-1)),(F(2),F(-1),F(6)))


def vertices(s):
    """s=0 is the regular ten-vertex horizon, s>0 genuine finite pyramid inputs."""
    assert 0<=s<=F(1,16)
    b=((F(0),-BETA,F(0)),(F(0),1-BETA,F(0)),(F(0),F(0),F(1)))
    p=FCUT[0]*FCUT[1]*FCUT[2]
    dl=1-(1-STACK)*p
    cs=sum(CWIDTH); c2=sum(CWIDTH[i]*CWIDTH[j] for i,j in combinations(range(3),2)); c3=CWIDTH[0]*CWIDTH[1]*CWIDTH[2]
    assert LEFT_SCALE*dl+cs==1
    delta=1-s*(c2+LEFT_SCALE*cs)+s*s*(c3+LEFT_SCALE*c2)-s**3*LEFT_SCALE*c3
    assert delta>0
    left=tuple((-LEFT_SCALE*(1-f)/delta,f*v[1],f*v[2]) for f,v in zip(FCUT,b))
    right=tuple(((1-s*LEFT_SCALE)*c/delta,(1-s*c)*v[1],(1-s*c)*v[2]) for c,v in zip(CWIDTH,b))
    apex=(-LEFT_SCALE/delta,F(0),F(0))
    centroid=tuple(sum(w*v[k] for w,v in zip(WEIGHTS,left)) for k in range(3))
    stack=add(scale(STACK,apex),scale(1-STACK,centroid))
    return tuple(b)+left+right+(stack,)


def hull_faces(V):
    faces={}
    for i,j,k in combinations(range(len(V)),3):
        n=cross(sub(V[j],V[i]),sub(V[k],V[i]));
        if not any(n):continue
        h=dot(n,V[i]);slack=[h-dot(n,x) for x in V]
        if min(slack)<0 and max(slack)>0:continue
        if max(slack)==0:n=scale(-1,n);h=-h;slack=[-x for x in slack]
        assert min(slack)>=0 and max(slack)>0
        inds=frozenset(i for i,x in enumerate(slack) if x==0)
        key=primitive(n+(h,))
        faces[inds]=key
    return faces


def certify(s):
    V=vertices(s); assert len(set(V))==10
    recovered=hull_faces(V)
    assert set(recovered)=={frozenset(c) for c in CYCLES}
    normals=[]; incidence={}; D=F(0); J=(F(0),)*3; second=tuple((F(0),)*3 for _ in range(3)); guards=[]
    for fi,cy in enumerate(CYCLES):
        a,b,c=(V[i] for i in cy[:3]); n=cross(sub(b,a),sub(c,a));h=dot(n,a)
        assert any(n)
        sl=[h-dot(n,x) for x in V]
        assert all(sl[i]==0 for i in cy) and all(sl[i]>0 for i in range(10) if i not in cy)
        assert primitive(n+(h,))==recovered[frozenset(cy)]
        guards.extend(sl[i] for i in range(10) if i not in cy)
        for q in range(len(cy)):
            i,j,k=cy[q],cy[(q+1)%len(cy)],cy[(q+2)%len(cy)]
            turn=dot(cross(sub(V[j],V[i]),sub(V[k],V[j])),n);assert turn>0;guards.append(turn)
            incidence.setdefault(tuple(sorted((i,j))),[]).append(fi)
        for q in range(1,len(cy)-1):
            a,b,c=V[cy[0]],V[cy[q]],V[cy[q+1]]
            d=dot(a,cross(b,c));S=add(add(a,b),c);D+=d;J=add(J,scale(d,S))
            Q=matadd(outer(S,S),matadd(outer(a,a),matadd(outer(b,b),outer(c,c))))
            second=matadd(second,matscale(d,Q))
        normals.append((n,h))
    assert len(incidence)==17 and all(len(x)==2 for x in incidence.values())
    assert D==1 # actual volume is exactly 1/6 after the single x normalization
    g=scale(1/(4*D),J)
    Sigma=matadd(matscale(1/(20*D),second),matscale(F(-1),outer(g,g)))
    assert pd(Sigma)
    X=tuple(sub(x,g) for x in V)
    poles=[]
    for n,h in normals:
        hc=h-dot(n,g);assert hc>0;poles.append(scale(1/hc,n))
    M=METRIC;N=inverse(M); assert pd(M) and pd(N)
    assert all(dot(M[i],tuple(N[k][j] for k in range(3)))==(1 if i==j else 0) for i in range(3) for j in range(3))
    ve={};ef={}
    for (i,j),(f,h) in sorted(incidence.items()):
        ve[i,j]=dot(X[i],mv(M,sub(X[j],X[i])))
        ve[j,i]=dot(X[j],mv(M,sub(X[i],X[j])))
        ef[f,h]=dot(poles[f],mv(N,sub(poles[h],poles[f])))
        ef[h,f]=dot(poles[h],mv(N,sub(poles[f],poles[h])))
    assert len(ve)==34 and len(ef)==34
    assert all(x!=0 for x in list(ve.values())+list(ef.values()))
    U=[i for i in range(10) if all(v<0 for (a,b),v in ve.items() if a==i)]
    S=[i for i in range(9) if all(v<0 for (a,b),v in ef.items() if a==i)]
    H=[(i,j) for (i,j),(f,h) in sorted(incidence.items()) if ve[i,j]<0 and ve[j,i]<0 and ef[f,h]<0 and ef[h,f]<0]
    assert len(S)+len(U)-len(H)==2
    return {'s':s,'vertices':V,'cycles':CYCLES,'edges':list(sorted(incidence)), 'volume':D/6,'centroid':g,'covariance':Sigma,'M':M,'N':N,'poles':poles,'S':S,'U':U,'H':H,'weak':'000','primitive_count':68,'VE':[(i,j,v) for (i,j),v in sorted(ve.items())],'EF':[(i,j,v) for (i,j),v in sorted(ef.items())],'minimum_support_or_turn_guard':min(guards)}


def encode(o):
    if isinstance(o,F):return str(o)
    if isinstance(o,dict):return {k:encode(v) for k,v in o.items()}
    if isinstance(o,(tuple,list)):return [encode(x) for x in o]
    return o


def main():
    controls=[certify(s) for s in (F(0),F(1,16),F(1,256))]
    out={'identity':'CUT_STACK_ELEVEN_MODULI_REGULAR_RIGHT_HORIZON_V1','inputs':{'beta':BETA,'f':FCUT,'t':STACK,'w':WEIGHTS,'A':LEFT_SCALE,'c':CWIDTH},'controls':controls,
         'scope':'Three exact actual bodies only; the rational s-family is defined, but no all-s mechanical sign certificate is claimed.',
         'marker':'CUT_STACK_REGULAR_HORIZON_ACTUAL_CENSUS_PASS'}
    print(json.dumps(encode(out),sort_keys=True,indent=2))

if __name__=='__main__':main()
