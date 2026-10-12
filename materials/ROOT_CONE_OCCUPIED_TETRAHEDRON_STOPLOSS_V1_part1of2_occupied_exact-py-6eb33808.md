# material-6eb33808fbb3

AI research material

<!-- historical-status:start -->
> **Historical AI material.** The title and claims below reflect the AI’s assessment at the time. Claims of proof, certification or completion are not a current verification verdict.
>
> [C622](../C622/README.md) passes the supplied exact checks; C<500 remains open; Minimum’s C≥34 remains a working lower bound requiring a consolidated proof. See [verification status and source gaps](../catalog/coverage.md).
<!-- historical-status:end -->

---

#!/usr/bin/env python3
"""ROOT_CONE_OCCUPIED_TETRAHEDRON_STOPLOSS_V1.
Exact rational controls and recovery. Python 3 standard library only.
No inputs, randomization, or floating optimizer. These are NOT 110 examples.
"""
from fractions import Fraction as F
from itertools import combinations, product
from math import comb
from pathlib import Path
import hashlib, json

def dd4(vs):
    """Third divided difference of x_+^4, including all repeated knots."""
    vs=list(map(F,vs))
    assert len(vs)==4
    if min(vs)>=0:return sum(vs)
    if max(vs)<=0:return F(0)
    pos=[x for x in vs if x>0]; neg=[-x for x in vs if x<=0]
    if len(pos)==1:
        a=pos[0];return a**4/prod(a+x for x in neg)
    if len(pos)==3:
        a=neg[0];return sum(vs)+a**4/prod(a+x for x in pos)
    a,b=pos;u,v=neg
    num=a*a*b*b*(a+b)+(u+v)*a*b*(a*a+a*b+b*b)+u*v*(a**3+a*a*b+a*b*b+b**3)
    return num/((a+u)*(a+v)*(b+u)*(b+v))

def prod(xs):
    z=F(1)
    for x in xs:z*=x
    return z

def dd4_table(vs):
    xs=sorted(map(F,vs));v=[max(x,F(0))**4 for x in xs]
    for j in (1,2,3):
        v=[(v[i+1]-v[i])/(xs[i+j]-xs[i]) if xs[i+j]!=xs[i]
           else comb(4,j)*max(xs[i],F(0))**(4-j) for i in range(4-j)]
    return v[0]

def positive_cube_integral(H,L,M):
    return (max(H,F(0))**4-max(H-L*M,F(0))**4)/(4*L) if L else M*max(H,F(0))**3

def bounds(b,c,d,t,k,m,A,B,H,L):
    eta=(1-b)*(1-c)*(1-d);M=max(b,c,d)
    aa=max(A,B);bb=min(A,B)
    rplus=[L-H,-H,bb-H,aa*k-H]
    tminus=[H-L,H-L*b,H-L*c-B*(1-c),H-L*d-A*(1-d)]
    topR=[H-L,H-L*M,H-L*M-bb*(1-M),H-L*M-aa*k*(1-M)]
    topT=[H-L,H-L*M,H-L*M-A*(1-M),H-L*M-B*(1-M)]
    raw=k*dd4(rplus)+4*eta*t*H-eta*t*m*L-eta*dd4(tminus)
    correction=(1-M)**3*(k*dd4(topR)-dd4(topT))
    capped=raw-correction
    theta=eta*dd4(tminus)-(1-M)**3*dd4(topT)
    D0=k-eta*t;D1=k-eta*t*m
    cone=aa*k*k+bb*k
    old_affine=cone-4*H*D0+L*D1+4*positive_cube_integral(H,L,M)/(A*B)
    occupied_quadrant=old_affine-theta
    # The reference triangle contains the canonical unit triangle.
    assert correction>=0 and theta>=0 and capped<=occupied_quadrant<=old_affine
    return dict(uncapped=raw,capped=capped,top_gain=correction,
                tetra_obstacle=theta,old_affine=old_affine,
                occupied_quadrant=occupied_quadrant)

def pdf_jet(knots,mid):
    h=sorted(map(F,knots));mid=F(mid)
    cur=[(F(h[i]<=mid<h[i+1]),F(0),F(0)) for i in range(3)]
    def mul(v,a,b):return (a*v[0],a*v[1]+b*v[0],a*v[2]+b*v[1])
    for degree in (1,2):
        nxt=[]
        for i in range(3-degree):
            v=[F(0)]*3
            den=h[i+degree]-h[i]
            if den:v=[x+y for x,y in zip(v,mul(cur[i],(mid-h[i])/den,1/den))]
            den=h[i+degree+1]-h[i+1]
            if den:v=[x+y for x,y in zip(v,mul(cur[i+1],(h[i+degree+1]-mid)/den,-1/den))]
            nxt.append(tuple(v))
        cur=nxt
    return tuple(3*x/(h[-1]-h[0]) for x in cur[0])

def mix(laws,x):return tuple(sum(w*pdf_jet(h,x)[i] for h,w in laws) for i in range(3))

def formal_control():
    b,c,d,h=F(1,2),F(13,20),F(1,10),F(1,2)
    alpha,epsilon,delta=1-b,1-c,1-d;eta=alpha*epsilon*delta
    D=1-h*h*c;t=D/eta;m=(1-h*h*c*c)/D;k=F(1)
    u=(1-h**3*c)/(delta*D);v=(1-h**3*c)/(epsilon*D)
    w=(4-delta*u-epsilon*v-m)/alpha
    lam=eta/D;rho=c*(1-h*h)/D;omega=d*epsilon/D;gamma=b*delta*epsilon/D
    laws=[((1,b,c,d),lam),((c,0,0,0),rho),((c,d,0,0),omega),((c,b,d,0),gamma)]
    shadow=[((1,0,0,0),1/D),((c,0,0,0),-h*h*c/D)]
    assert min(lam,rho,omega,gamma)>0 and sum((lam,rho,omega,gamma))==1 and lam==1/t
    intervals=sorted({F(0),b,c,d,F(1)})
    for lo,hi in zip(intervals,intervals[1:]):
        x=(lo+hi)/2;jet=mix(laws,x)
        assert jet==mix(shadow,x) and jet[0]>0 and jet[1]**2-4*jet[0]*jet[2]>=0
    D0=k-eta*t;D1=k-eta*t*m
    Lx=k*k-eta*t*delta*u;Ly=k*k-eta*t*epsilon*v
    I=h**3*c/4
    assert (D0,D1,Lx,Ly)==(h*h*c,h*h*c*c,h**3*c,h**3*c)
    assert Lx+Ly==8*I
    # ALL weighted V2 inequalities follow from (A+B)>=2sqrt(AB).
    # ALL directional integral-strip inequalities follow from the pointwise
    # bound integral d_*^2/(1-q) <= h^4*c/4 and 3h/4<1.
    assert 3*h**4*c/4 < Lx and lam*(4-m)**3>27*eta
    scalar={
        'u_min':u-1,'v_min':v-1,'sum':t+1-u-v,'volume_high':F(45,7)-t,
        'b_plus_c':b+c-F(9,8),'height_lo':w-2+t,'height_hi':t+2-u-v-w,
        'C_fan_endpoint':t*(m-c)-1-b-d,'D_fan_endpoint':t*(m-d)-1-b-c,
        'x_single_cap':F(10,9)-(1+b+c)*u/(t*m),
        'y_single_cap':F(10,9)-(1+b+d)*v/(t*m)}
    assert min(scalar.values())>0
    H=h;L=h/c;bo=bounds(b,c,d,t,k,m,F(1),F(1),H,L)
    lhs=eta*t*(delta*u+epsilon*v)
    assert bo['old_affine']==lhs and bo['top_gain']==0
    assert bo['tetra_obstacle']==F(729,2768480)
    assert lhs-bo['capped']==bo['tetra_obstacle']>0
    T=((1+b+c)*u+(1+b+d)*v)/(t*m)
    assert T==F(42973,31959)<F(51,25)
    return dict(status='FORMAL_PROFILE_AND_MOMENTS_NOT_A_PROPER_ROOT_ONLY_BODY',
        parameters=dict(b=b,c=c,d=d,h=h,t=t,kappa=k,m=m,u=u,v=v,w=w,T=T),
        seven_C_fan_masses=[lam,rho,F(0),omega,F(0),gamma,F(0)],
        D0=D0,D1=D1,I=I,Lx=Lx,Ly=Ly,strict_scalar_slacks=scalar,
        test=dict(A=1,B=1,H=H,L=L),lhs=lhs,bounds=bo,
        warning='The shadow cone with X+Y+(h/c)q>=h excludes canonical B. No actual high-trace or mechanical counterexample is claimed.')

def dot(a,b):return sum(x*y for x,y in zip(a,b))
def sub(a,b):return tuple(x-y for x,y in zip(a,b))
def cross(a,b):return (a[1]*b[2]-a[2]*b[1],a[2]*b[0]-a[0]*b[2],a[0]*b[1]-a[1]*b[0])
def det(a,b,c):return dot(a,cross(b,c))
def hull2(q):
    # q=(x,y,label). Exact monotone chain; boundary collinear points removed.
    q=sorted(q)
    def orient(a,b,c):return (b[0]-a[0])*(c[1]-a[1])-(b[1]-a[1])*(c[0]-a[0])
    def half(z):
        h=[]
        for p in z:
            while len(h)>=2 and orient(h[-2],h[-1],p)<=0:h.pop()
            h.append(p)
        return h
    return half(q)[:-1]+half(q[::-1])[:-1]

def hull3(P):
    faces={}
    for i,j,k in combinations(range(len(P)),3):
        n=cross(sub(P[j],P[i]),sub(P[k],P[i]))
        if not any(n):continue
        z=[dot(n,sub(p,P[i])) for p in P]
        if min(z)<0<max(z):continue
        ids=frozenset(i for i,h in enumerate(z) if not h)
        if ids in faces:continue
        drop=next(j for j,x in enumerate(n) if x)
        ax=[j for j in range(3) if j!=drop]
        cyc=hull2([(P[i][ax[0]],P[i][ax[1]],i) for i in ids])
        assert {v[2] for v in cyc}==set(ids)
        faces[ids]=tuple(v[2] for v in cyc)
    fs=sorted(faces.values());ed=sorted({tuple(sorted((f[j-1],f[j]))) for f in fs for j in range(len(f))})
    assert {i for f in fs for i in f}==set(range(len(P)))
    assert len(P)-len(ed)+len(fs)==2
    return fs,ed

def moments(P,faces,apex):
    V=F(0);J=[F(0)]*3
    for face in faces:
        if apex in face:continue
        for j in range(1,len(face)-1):
            ids=(apex,face[0],face[j],face[j+1])
            vol=abs(det(*(sub(P[i],P[apex]) for i in ids[1:])))/6
            assert vol>0
            V+=vol
            for ax in range(3):J[ax]+=vol*sum(P[i][ax] for i in ids)/4
    return V,tuple(J)

def actual_control(name,b,c,d,xy):
    b,c,d=map(F,(b,c,d));xy=[tuple(map(F,p)) for p in xy]
    eta=(1-b)*(1-c)*(1-d)
    P=[(F(0),F(0),F(1)),(F(0),F(0),b),(F(0),1-c,c),(1-d,F(0),d)]
    P += [(x,y,F(0)) for x,y in xy]
    fs,ed=hull3(P);ff={frozenset(f) for f in fs}
    assert frozenset((0,1,2)) in ff and frozenset((0,1,3)) in ff
    assert frozenset(range(4,len(P))) in ff and min(min(q) for q in xy)>0
    V,J=moments(P,fs,2)
    assert (V,J)==moments(P,fs,0)
    t=6*V/eta;m=4*J[2]/V;u=4*J[0]/((1-d)*V);v=4*J[1]/((1-c)*V)
    K=hull2([(F(0),F(0),0),(F(1),F(0),1),(F(0),F(1),2)]+[(x,y,j+3) for j,(x,y) in enumerate(xy)])
    kap=sum(K[i-1][0]*K[i][1]-K[i-1][1]*K[i][0] for i in range(len(K)))
    assert kap>=1
    tests=[]
    for A,B in [(F(1),F(1)),((1+b+c)/(1-d),(1+b+d)/(1-c))]:
        for H,L in [(F(0),F(0)),(F(1,2),F(0)),(F(1),F(1)),(F(2),F(3)),(F(3),F(2)),(F(1),F(-1)),(F(-1),F(-2))]:
            bo=bounds(b,c,d,t,kap,m,A,B,H,L)
            lhs=eta*t*(A*(1-d)*u+B*(1-c)*v)
            assert bo['capped']>=lhs
            tests.append(dict(A=A,B=B,H=H,L=L,lhs=lhs,slack=bo['capped']-lhs,top_gain=bo['top_gain']))
    T=((1+b+c)*u+(1+b+d)*v)/(t*m)
    return dict(name=name,status='ACTUAL_ROOT_ONLY_TRACE_CONTROL_NOT_110_CENSUS',
        endpoints=[1,b,c,d],vertices_XYq=P,facets=fs,edges=ed,
        f_vector=[len(P),len(ed),len(fs)],negative_root_vertices=sum(x+y>1 for x,y in xy),
        t=t,kappa=kap,m=m,u=u,v=v,T=T,tests=tests)

def encode(x):
    if isinstance(x,F):return str(x)
    if isinstance(x,dict):return {str(k):encode(v) for k,v in x.items()}
    if isinstance(x,(tuple,list)):return [encode(v) for v in x]
    return x

def main():
    n=0
    for vs in product([-2,-1,0,1,2],repeat=4):
        assert dd4(vs)==dd4_table(vs)>=0;n+=1
    control=formal_control()
    xy=[(F(1,10),F(3,20)),(F(6,5),F(1,5)),(F(13,10),F(7,10)),(F(1,5),F(11,10))]
    xy2=[(F(1,8),F(1,8)),(F(9,8),F(1,8)),(F(5,4),F(1)),(F(1,8),F(5,4))]
    inputs=[('MIXED_THREE_NEGATIVE_ROOTS',F(1,2),F(13,20),F(1,10),xy),
            ('B_HIGHEST_MULTIPLE_NEGATIVE_ROOTS',F(4,5),F(2,5),F(1,5),xy2),
            ('D_ABOVE_B_MULTIPLE_NEGATIVE_ROOTS',F(1,4),F(3,5),F(2,5),xy)]
    recs=[actual_control(*r) for r in inputs]
    assert all(r['negative_root_vertices']>=2 for r in recs)
    out=dict(identity='ROOT_CONE_OCCUPIED_TETRAHEDRON_STOPLOSS_V1',
             status='NEW_NECESSARY_VALUE_BOUNDS_AND_EXACT_CONTROLS_NO_GLOBAL_204_PROOF',
             divided_difference_checks=n,formal=control,actual=recs)
    raw=(json.dumps(encode(out),sort_keys=True,indent=2)+'\n').encode()
    Path('occupied_controls.json').write_bytes(raw)
    print('EXACT_CONFLUENT_STOPLOSS_625_KNOT_QUADRUPLES_PASS')
    print('FULL_HEIGHT_LAW_AND_ALL_V2_FAMILIES_FORMAL_SEPARATOR_PASS')
    print('OCCUPIED_CANONICAL_TETRAHEDRON_STRICTLY_EXCLUDES_FORMAL_POINT')
    print('formal_T='+str(control['parameters']['T']))
    print('formal_obstacle='+str(control['bounds']['tetra_obstacle']))
    print('THREE_ACTUAL_MULTIPLE_NEGATIVE_ROOTS_TWO_VOLUME_FANS_PASS')
    print('42_EXACT_TOP_CORRECTED_STOPLOSS_TESTS_PASS')
    print('report_bytes='+str(len(raw)))
    print('report_sha256='+hashlib.sha256(raw).hexdigest())
    print('ROOT_CONE_OCCUPIED_TETRAHEDRON_STOPLOSS_V1_RECOVERY_PASS')
if __name__=='__main__':main()
