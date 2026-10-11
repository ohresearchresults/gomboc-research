# material-d760d4070fbe

Historical AI scientific source/proof material. Statements retain their original scope; this is not an independently reviewed theorem.

---

"""JOINT_MASS_QUANTITATIVE_STABILITY_V1: exact finite checks, not the continuous proof.
CPython 3.13.5; standard library; assertions enabled.
Run: python -S joint_mass_stability_exact.py build
     python -S joint_mass_stability_exact.py check
No external inputs, random seed, optimizer or optional parameters are used.
"""
from fractions import Fraction as F
from math import comb
from pathlib import Path
import hashlib
import json
import sys
assert __debug__

def trim(p):
    p=list(p)
    while len(p)>1 and not p[-1]: p.pop()
    return p

def add(*ps):
    n=max(map(len,ps)); out=[F(0)]*n
    for p in ps:
        for i,a in enumerate(p): out[i]+=a
    return trim(out)

def scale(p,c): return trim([a*c for a in p])

def mul(p,q):
    out=[F(0)]*(len(p)+len(q)-1)
    for i,a in enumerate(p):
        for j,b in enumerate(q): out[i+j]+=a*b
    return trim(out)

def power(p,n):
    out=[F(1)]
    for _ in range(n): out=mul(out,p)
    return out

def value(p,x):
    out=F(0)
    for a in reversed(p): out=out*x+a
    return out

def integral(p,lo,hi):
    return sum(a*(hi**(i+1)-lo**(i+1))/(i+1) for i,a in enumerate(p))

def affine(p,lo,hi):
    out=[F(0)]*len(p)
    for k,a in enumerate(p):
        for j in range(k+1): out[j]+=a*comb(k,j)*lo**(k-j)*(hi-lo)**j
    return trim(out)

def bernstein(p,lo,hi,n=4):
    q=affine(p,lo,hi); assert len(q)<=n+1
    out=[sum(q[j]*F(comb(i,j),comb(n,j)) for j in range(min(i,len(q)-1)+1)) for i in range(n+1)]
    back=[F(0)]
    for i,a in enumerate(out):
        basis=mul([F(0)]*i+[F(1)],power([F(1),F(-1)],n-i))
        back=add(back,scale(basis,a*comb(n,i)))
    assert trim(back)==trim(q)
    return out

def hinge_tetra(nodes,mid):
    """Polynomial in threshold t of E[(ell-t)+] on one uniform tetrahedron.
    Hermite divided differences handle every repeated node exactly.
    The expression is valid on an interval containing no node in its interior.
    """
    v=sorted(nodes)
    def term(x,k):
        return scale(power([x,F(-1)],4-k),F(comb(4,k))) if x>mid else [F(0)]
    q=[term(x,0) for x in v]
    for k in range(1,4):
        q=[term(v[j],k) if v[j+k]==v[j]
           else scale(add(q[j+1],scale(q[j],-1)),1/(v[j+k]-v[j]))
           for j in range(4-k)]
    return scale(q[0],F(1,4))

def encode(x):
    if isinstance(x,F): return str(x)
    if isinstance(x,dict): return {k:encode(v) for k,v in x.items()}
    if isinstance(x,(list,tuple)): return [encode(v) for v in x]
    return x

def make_report():
    # The one-dimensional height-loss inequality is an exact polynomial identity.
    # integral_H^R (s-H)(1-s/R) ds = (R-H)^3/(6R).
    for H,R in ((F(1),F(3,2)),(F(2,3),F(7,3)),(F(1),F(1))):
        assert integral(mul([-H,F(1)],[F(1),-1/R]),H,R)==(R-H)**3/(6*R)
    # A real truncated concave profile with a positive endpoint, not a zero-endpoint assumption.
    H=F(1); prof=[F(1),F(-1,2)]; W=integral(prof,0,H); R=2*W
    Dp=R*R/6-integral(mul([F(0),F(1)],prof),0,H)
    assert Dp>= (R-H)**3/(6*R)>0
    # Radial first-order stochastic comparison control.
    f=[F(1),F(-3,8)]; rad=F(3,2); q=[F(1),-1/rad]
    assert integral(mul([F(0),F(1)],f),0,1)==rad**2/6
    j=rad**3/12-integral(mul([F(0),F(0),F(1)],f),0,1)
    neg=integral(mul(mul([F(0),F(1)],[F(-1),F(1)]),q),1,rad)
    assert 0<neg<=j
    # Exact negative-cap formula for the auxiliary two-tetrahedron cone.
    caps=[]
    for t,eta in ((F(2),F(1,5)),(F(1),F(1,3)),(F(7,4),F(3,7))):
        tk=t+eta; nodes=(-t,-t,1-t,eta)
        mean=value(hinge_tetra(nodes,F(0)),F(0))
        measured=tk*mean/6
        expected=eta**4/(24*tk*(tk-1))
        assert measured==expected
        caps.append([t,eta,measured])
    # Constants use w=(4/3)(1-h)delta <= (1-h)^2 <= 1.
    # With u=w^(1/12), w^(1/3)+w^(1/4)=u^4+u^3 <= 2u^3.
    # Exact factorization: 2u^3-u^4-u^3=u^3(1-u).
    assert add([0,0,0,2],scale(add([0,0,0,0,1],[0,0,0,1]),-1))==[F(0),F(0),F(0),F(1),F(-1)]
    # Uniform high-trace gap, with all endpoint cases covered by three closed intervals.
    tau=F(51,25); gap0=F(1,50000000000000)
    intervals=((F(7,45),F(1,3)),(F(1,3),F(1,2)),(F(1,2),F(1)))
    bounds=[]
    for lo,hi in intervals:
        bound=F(3,4)*lo**8/(1-lo)*(((1-hi)**2+F(1,25))/28)**4
        assert bound>gap0
        bounds.append([lo,hi,bound,bound-gap0])
    # An exact formal scalar relaxation point, explicitly NOT a polytope or 110 witness.
    h=F(1,5); delta=F(1,10**18); m=F(3,4)*(1+h)-delta; m1=m2=m/2
    lam=tau/2; a=(tau-h)/(m-h); c=3*tau/m-2*a; d=c; b=a
    zc=(3-tau)/(3-m)
    V=1/(6*h); gx=m1/(3*h); gy=m2/(3*h); gz=(1-gx-gy)/2
    assert 0<delta<gap0
    assert all(F(3,4)*h<q<F(3,4) for q in (m1,m2))
    assert m<F(3,4)*(1+h)
    assert F(13,15)<m<3 and h>F(7,45)
    assert all(0<q<4 for q in (a,b,c,d))
    assert a+(d-a)*gx+(c-a)*gy+(b-a)*gz==1
    assert m1*(a+b+c)/3==lam and m2*(a+b+d)/3==lam
    assert lam<F(132,119)<F(10,9)
    assert 4>a+h*(a+c+d)  # Equal-endpoint two-corner integral bound.
    assert F(1,2)-1/(4*h)<gz<F(1,2)-gx-gy+1/(4*h)
    # Two separate necessary second-moment checks.
    Q=(a*a+b*b+c*c+a*b+a*c+b*c)/6
    surface_second=m*Q+(3-m)*zc*zc
    assert surface_second<6
    vals=(a,b,c,d); tetmean=sum(vals)/4
    tetsecond=(sum(q*q for q in vals)+sum(vals)**2)/20
    volume_second=h*tetsecond+(1-h*tetmean)**2/(1-h)
    assert h*tetmean<1 and volume_second<F(8,5)
    # Full threshold continuum, not a finite sampling of t.
    # Formal triangular cones: values (1,a,a,c); complementary Jensen cone: (1,zc,zc,zc).
    U=power([F(1),F(-1,4)],4)
    knots=sorted(set((F(0),zc,F(1),c,a,F(4))))
    assert knots[0]==0 and knots[-1]==4 and 0<zc<1<c<a<4
    leaves=[]; polynomials=[]
    for i,(lo,hi) in enumerate(zip(knots,knots[1:])):
        mid=(lo+hi)/2
        P=add(U,scale(hinge_tetra((F(1),a,a,c),mid),-m/3),
                 scale(hinge_tetra((F(1),zc,zc,zc),mid),-(3-m)/3))
        polynomials.append([lo,hi,P])
        def cover(l,r,path):
            B=bernstein(P,l,r)
            if min(B)>=0:
                leaves.append({'interval':i,'lo':l,'hi':r,'path':path,'bernstein':B})
                return
            assert len(path)<16, 'No certificate found; this is not a mathematical exclusion.'
            mid2=(l+r)/2
            cover(l,mid2,path+'0'); cover(mid2,r,path+'1')
        cover(lo,hi,'')
        used=[v for v in leaves if v['interval']==i]
        assert used[0]['lo']==lo and used[-1]['hi']==hi
        assert all(p['hi']==q['lo'] for p,q in zip(used,used[1:]))
    # For t>=4 all hinge terms and U_+ are zero. All piecewise boundaries are continuous.
    local_gap=F(3,4)*h**8/(1-h)*((tau-(1+2*h-h*h))/28)**4
    assert delta<local_gap
    return {'identity':'JOINT_MASS_QUANTITATIVE_STABILITY_V1',
            'continuous_proof_file':'joint_mass_stability_proof.md',
            'height_loss_control':[H,W,R,Dp],
            'radial_control':[j,neg],
            'negative_cap_exact_controls':caps,
            'uniform_gap':gap0,'three_closed_interval_bounds':bounds,
            'formal_control':{'is_polytope':False,'h':h,'delta':delta,'m1':m1,'m2':m2,
                'lambda1':lam,'lambda2':lam,'a':a,'b':b,'c':c,'d':d,'complement':zc,
                'formal_centroid':[gx,gy,gz],'surface_second':surface_second,
                'volume_second':volume_second,'new_local_gap':local_gap},
            'full_threshold_polynomials':polynomials,'full_threshold_bernstein_leaves':leaves,
            'constant_source':'T<=1+2h-h^2+28*((4/3)*(1-h)*delta)^(1/4)/h^2',
            'claim_C_ge_36':False,'claim_exact_minimum':False}

def main():
    if len(sys.argv)!=2 or sys.argv[1] not in ('build','check'):
        raise SystemExit('Use build or check; assertions must be enabled.')
    report=make_report()
    data=(json.dumps(encode(report),ensure_ascii=True,sort_keys=True,indent=2)+'\n').encode('utf-8')
    path=Path('joint_mass_stability_exact.json')
    if sys.argv[1]=='build': path.write_bytes(data)
    else: assert path.read_bytes()==data
    print('QUANTITATIVE_HEIGHT_RADIAL_AND_NEGATIVE_CAP_CONTROLS_PASS')
    print('UNIVERSAL_HIGH_TRACE_MASS_GAP_PASS',report['uniform_gap'])
    print('POSITIVE_DEFICIT_FORMAL_CONTROL_FULL_TAIL_PASS',len(report['full_threshold_bernstein_leaves']))
    print('JOINT_MASS_STABILITY_EXACT_PASS',len(data),hashlib.sha256(data).hexdigest())
if __name__=='__main__': main()
