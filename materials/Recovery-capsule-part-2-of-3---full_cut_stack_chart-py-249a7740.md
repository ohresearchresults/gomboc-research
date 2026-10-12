# material-249a774019a7

AI research material

---

#!/usr/bin/env python3
"""Complete rational E17 cut-stack chart: exact new controls and affine inverse.
Standard library only. Run with assertions: python -B -S full_cut_stack_chart.py.
No external input, floating point, random seed, solver or hidden checkpoint.
The continuum theorem is the accompanying analytic proof, not this finite test.
"""
from fractions import Fraction as F
from itertools import combinations
import hashlib
import json

ZERO = (F(0),) * 3
CYCLES = ((0,3,4,1,7,6),(0,2,5,3),(0,6,8,2),(1,4,5,2),
          (1,2,8,7),(3,9,4),(3,5,9),(4,9,5),(6,7,8))
TETS = ((0,1,2,5),(0,1,4,5),(0,3,4,5),(3,4,5,9),
        (0,1,2,8),(0,1,7,8),(0,6,7,8))
METRIC = ((F(7),F(1),F(2)),(F(1),F(5),F(-1)),(F(2),F(-1),F(6)))
BETA = F(2,5)
P = (F(1,5),F(2,5),F(3,5))
Q = (F(1,4),F(1,3),F(1,2))
U = (F(1,5),F(2,5),F(2,5))
PS = F(4,5)
ALPHAS = (F(-1),F(0),F(1,2),F(1),F(2))
AFFINE = ((F(2),F(1),F(0)),(F(0),F(1),F(1)),(F(1),F(0),F(1)))
SHIFT = (F(2,3),F(-1,5),F(7,4))


def add(a,b): return tuple(x+y for x,y in zip(a,b))
def sub(a,b): return tuple(x-y for x,y in zip(a,b))
def scale(c,a): return tuple(c*x for x in a)
def dot(a,b): return sum((x*y for x,y in zip(a,b)),F(0))
def cross(a,b): return (a[1]*b[2]-a[2]*b[1],a[2]*b[0]-a[0]*b[2],a[0]*b[1]-a[1]*b[0])
def det(A): return dot(A[0],cross(A[1],A[2]))
def tr(A): return tuple(zip(*A))
def mv(A,x): return tuple(dot(a,x) for a in A)
def outer(a,b): return tuple(tuple(x*y for y in b) for x in a)
def ma(A,B): return tuple(add(a,b) for a,b in zip(A,B))
def ms(c,A): return tuple(scale(c,a) for a in A)
def mm(A,B): return tuple(tuple(dot(a,b) for b in tr(B)) for a in A)
def vsum(X): return tuple(sum((x[k] for x in X),F(0)) for k in range(3))
def product(X):
    r=F(1)
    for x in X:r*=x
    return r

def inverse(A):
    d=det(A)
    if not d: raise ValueError('Singular matrix')
    return ms(1/d,tr((cross(A[1],A[2]),cross(A[2],A[0]),cross(A[0],A[1]))))

def pd(A): return A[0][0]>0 and A[0][0]*A[1][1]-A[0][1]*A[1][0]>0 and det(A)>0

def geometry(beta,a,p,q,u,ps):
    assert 0<beta<1 and all(v>0 for v in p+q+u) and sum(u)==1
    excess=ps-dot(u,p)
    assert excess>0
    d=tuple(1+a*x for x in p); e=tuple(1+(1-a)*x for x in q); ds=1+a*ps
    assert min(d+e+(ds,))>0
    B=((F(0),-beta,F(0)),(F(0),1-beta,F(0)),(F(0),F(0),F(1)))
    L=tuple((-p[j]/d[j],B[j][1]/d[j],B[j][2]/d[j]) for j in range(3))
    R=tuple((q[j]/e[j],B[j][1]/e[j],B[j][2]/e[j]) for j in range(3))
    us=vsum([scale(u[j],B[j]) for j in range(3)])
    S=(-ps/ds,us[1]/ds,us[2]/ds)
    weights=(p[2]/d[2],p[1]/(d[1]*d[2]),p[0]/product(d),
             excess/(ds*product(d)),q[2]/e[2],q[1]/(e[1]*e[2]),q[0]/product(e))
    assert min(weights)>0
    def prism(v,k):
        return (sum(v)+k*sum(v[i]*v[j] for i,j in combinations(range(3),2))+k*k*product(v))/product(1+k*x for x in v)
    assert sum(weights)==prism(p,a)+excess/(ds*product(d))+prism(q,1-a)
    return B+L+R+(S,),weights


def maximal_facets(V):
    found=set()
    for i,j,k in combinations(range(len(V)),3):
        n=cross(sub(V[j],V[i]),sub(V[k],V[i]))
        if not any(n):continue
        values=[dot(n,sub(v,V[i])) for v in V]
        if min(values)<0<max(values):continue
        assert min(values)<0 or max(values)>0
        found.add(tuple(h for h,x in enumerate(values) if x==0))
    return found


def surface(V):
    assert len(set(V))==10
    assert maximal_facets(V)=={tuple(sorted(c)) for c in CYCLES}
    D=F(0);J=ZERO;K=(ZERO,)*3;inc={};planes=[];guards=[]
    arrows=[]
    for fi,cy in enumerate(CYCLES):
        aa,bb,cc=[V[i] for i in cy[:3]]
        n=cross(sub(bb,aa),sub(cc,aa));h=dot(n,aa)
        assert any(n)
        slack=[h-dot(n,x) for x in V]
        assert all(slack[i]==0 for i in cy)
        assert all(slack[i]>0 for i in range(10) if i not in cy)
        guards.extend(slack[i] for i in range(10) if i not in cy)
        for j in range(len(cy)):
            i,k,l=cy[j],cy[(j+1)%len(cy)],cy[(j+2)%len(cy)]
            z=dot(cross(sub(V[k],V[i]),sub(V[l],V[k])),n)
            assert z>0;guards.append(z)
            inc.setdefault(tuple(sorted((i,k))),[]).append(fi);arrows.append((i,k))
        for j in range(1,len(cy)-1):
            v=[V[i] for i in (cy[0],cy[j],cy[j+1])];s=vsum(v);w=det(v)
            D+=w;J=add(J,scale(w,s));Q0=outer(s,s)
            for x in v:Q0=ma(Q0,outer(x,x))
            K=ma(K,ms(w,Q0))
        planes.append((n,h))
    assert len(set(arrows))==34 and all((j,i) in arrows for i,j in arrows)
    assert len(inc)==17 and all(len(fs)==2 for fs in inc.values()) and D>0
    return D,J,K,inc,planes,min(guards)


def positive_tet_moments(V,weights):
    D=F(0);J=ZERO;K=(ZERO,)*3
    for ids,w in zip(TETS,weights):
        tet=[V[i] for i in ids]
        observed=abs(det([sub(tet[j],tet[0]) for j in (1,2,3)]))
        assert observed==w>0
        s=vsum(tet);D+=w;J=add(J,scale(w,s));Q0=outer(s,s)
        for x in tet:Q0=ma(Q0,outer(x,x))
        K=ma(K,ms(w,Q0))
    return D,J,K


def recover(V):
    """Affine-invariant inverse chart; input labelled true incidence is assumed."""
    b0,b1,b2=V[:3]
    frame=tr((sub(b0,V[3]),sub(b1,b0),sub(b2,b0)))
    inv=inverse(frame)
    W=tuple(mv(inv,sub(v,b0)) for v in V)
    assert W[0]==ZERO and W[1]==(0,1,0) and W[2]==(0,0,1) and W[3]==(-1,0,0)
    a0=-(1-W[4][1]-W[4][2])/W[4][0]
    a1=-W[3][1]/W[3][0]
    b0c=-(1-W[7][1]-W[7][2])/W[7][0]
    b1c=-W[6][1]/W[6][0]
    h=a0+a1;k=b0c+b1c;gap=h-k
    assert a0>b0c and a1>b1c and gap>0
    beta=(a1-b1c)/gap;a=h/gap;shear=a1-beta*h
    Z=tuple((gap*x,y-beta+beta*z+shear*x,z) for x,y,z in W)
    p=tuple(-Z[j+3][0]/(1+a*Z[j+3][0]) for j in range(3))
    q=tuple(Z[j+6][0]/(1+(a-1)*Z[j+6][0]) for j in range(3))
    fs=1+a*Z[9][0];ps=-Z[9][0]/fs
    u2=Z[9][2]/fs;u1=Z[9][1]/fs+beta*(1-u2);u=(1-u1-u2,u1,u2)
    generated,_=geometry(beta,a,p,q,u,ps)
    assert Z==generated
    return beta,a,p,q,u,ps


def census(V,g,inc,planes,M):
    assert pd(M)
    N=inverse(M);assert pd(N)
    assert mm(M,N)==((1,0,0),(0,1,0),(0,0,1))
    X=tuple(sub(v,g) for v in V);poles=[]
    for n,h in planes:
        hc=h-dot(n,g);assert hc>0;poles.append(scale(1/hc,n))
    ve={};ef={}
    for (i,j),(f,h) in sorted(inc.items()):
        ve[i,j]=dot(X[i],mv(M,sub(X[j],X[i])))
        ve[j,i]=dot(X[j],mv(M,sub(X[i],X[j])))
        ef[f,h]=dot(poles[f],mv(N,sub(poles[h],poles[f])))
        ef[h,f]=dot(poles[h],mv(N,sub(poles[f],poles[h])))
    assert len(ve)==len(ef)==34
    assert all(v!=0 for v in list(ve.values())+list(ef.values()))
    Uv=[i for i in range(10) if all(v<0 for (a,b),v in ve.items() if a==i)]
    Sf=[i for i in range(9) if all(v<0 for (a,b),v in ef.items() if a==i)]
    He=[edge for edge,(f,h) in sorted(inc.items()) if ve[edge]<0 and ve[edge[::-1]]<0 and ef[f,h]<0 and ef[h,f]<0]
    assert len(Sf)+len(Uv)-len(He)==2
    return {'S':Sf,'U':Uv,'H':He,'counts':[len(Sf),len(Uv),len(He)],'physical_weak':'000',
            'M':M,'N':N,'poles':poles,'VE':[(i,j,v) for (i,j),v in sorted(ve.items())],
            'EF':[(i,j,v) for (i,j),v in sorted(ef.items())]}


def serial(o):
    if isinstance(o,F):return str(o)
    if isinstance(o,dict):return {k:serial(v) for k,v in o.items()}
    if isinstance(o,(tuple,list)):return [serial(x) for x in o]
    return o


def main():
    if not __debug__:raise RuntimeError('Assertions must remain enabled')
    results=[];reference,_=geometry(BETA,F(1),P,Q,U,PS)
    for a in ALPHAS:
        V,w=geometry(BETA,a,P,Q,U,PS)
        data=surface(V);D,J,K,inc,planes,guard=data
        assert (D,J,K)==positive_tet_moments(V,w)
        g=scale(1/(4*D),J);S=ma(ms(1/(20*D),K),ms(-1,outer(g,g)))
        assert pd(S)
        expected=(BETA,a,P,Q,U,PS)
        assert recover(V)==expected
        image=tuple(add(mv(AFFINE,v),SHIFT) for v in V)
        assert recover(image)==expected
        D1,J1,K1,_,_,_=surface(image)
        assert D1==abs(det(AFFINE))*D
        g1=scale(1/(4*D1),J1);S1=ma(ms(1/(20*D1),K1),ms(-1,outer(g1,g1)))
        assert g1==add(mv(AFFINE,g),SHIFT) and S1==mm(mm(AFFINE,S),tr(AFFINE))
        projected=tuple(scale(1/(1+(1-a)*x[0]),x) for x in reference)
        assert all(1+(1-a)*x[0]>0 for x in reference) and projected==V
        mech=census(V,g,inc,planes,METRIC)
        results.append({'a':a,'vertices':V,'seven_six_volumes':w,'volume':D/6,
                        'centroid':g,'covariance':S,'support_turn_guard':guard,'mechanics':mech})
    report={'identity':'FULL_CUT_STACK_INCIDENT_REALIZATION_PROJECTIVE_CHART_SEVEN_POSITIVE_TETS_V1',
            'inputs':{'beta':BETA,'p':P,'q':Q,'u':U,'ps':PS,'a_values':ALPHAS,'affine_map':AFFINE,'translation':SHIFT},
            'cycles':CYCLES,'tetrahedra':TETS,'controls':results,
            'scope':'Five actual rational controls, full proper censuses, seven-positive-tet moment identities, affine inverse and projective correspondence. The all-realization chart is proved analytically in the companion proof; this finite computation alone is not a whole-domain exclusion.',
            'marker':'FULL_CUT_STACK_CHART_SEVEN_POSITIVE_TETS_EXACT_PASS'}
    print(json.dumps(serial(report),sort_keys=True,indent=2))

if __name__=='__main__':main()
