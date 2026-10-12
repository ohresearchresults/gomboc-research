# material-16c220d5eb2b

AI research material

<!-- historical-status:start -->
> **Historical AI material.** The title and claims below reflect the AI’s assessment at the time. Claims of proof, certification or completion are not a current verification verdict.
>
> [C622](../C622/README.md) passes the supplied exact checks; C<500 remains open; Minimum’s C≥34 remains a working lower bound requiring a consolidated proof. See [verification status and source gaps](../catalog/coverage.md).
<!-- historical-status:end -->

---

"""PAIR_SECOND_MOMENT_H_2_31_AND_PARTIAL_CUT_V1.
Exact arithmetic and true-body controls; not a formalization of Brunn-Minkowski.
CPython3.13.5, standard library, assertions enabled. Exact dependency:
  pair_facet_merge_exact.py, 11504 bytes,
  1b954cbca536f21dd815184881e91bf50e5c506050d8b6378883ced3369a85f7.
Run: python -S pair_second_moment_cut_exact.py build|check
"""
from fractions import Fraction as F
from pathlib import Path
from math import comb
import hashlib
import importlib.util
import json
import sys
assert __debug__
PARENT='pair_facet_merge_exact.py'
p=Path(__file__).with_name(PARENT)
b=p.read_bytes()
assert len(b)==11504 and hashlib.sha256(b).hexdigest()=='1b954cbca536f21dd815184881e91bf50e5c506050d8b6378883ced3369a85f7'
spec=importlib.util.spec_from_file_location('merge',p)
g=importlib.util.module_from_spec(spec)
spec.loader.exec_module(g)
IDENTITY='PAIR_SECOND_MOMENT_H_2_31_AND_PARTIAL_CUT_V1'
OUTPUT='pair_second_moment_cut_exact.json'

def arithmetic():
    tau=F(51,25);M=F(37,50);H=F(2,31);alpha=3/M
    polynomial=2*M*M-(3+2*tau)*M+tau*tau
    s=1-alpha*H
    bound=s*((2-H)*s+H)*(s*tau+2*H)/(2*(1-H)*(1-tau*(1-s)/4))
    gamma=tau*alpha/4
    margin=alpha-1/(1-H)-gamma/(1-gamma*H)
    assert polynomial==F(11,625)>0
    assert s==F(847,1147)>0
    assert bound==F(150698679109,135441946550)
    assert bound-F(111,100)==F(716236877,270883893100)>0
    assert margin>0 and alpha*tau-2>0
    assert H<1/alpha and H<1/gamma and H<1
    return {'tau':tau,'mass_floor':M,'mass_polynomial_gap':polynomial,
            'h_floor':H,'alpha':alpha,'gamma':gamma,'log_derivative_margin':margin,
            's_endpoint':s,'cut_endpoint':bound,'cut_cap_gap':bound-F(111,100),
            'reciprocal_product_floor':H*H,'reciprocal_sum_floor':2*H}

def face_second(body,facet,ell):
    points=body['points'];cycle=facet['cycle'];a=points[cycle[0]]
    mass=F(0);first=F(0);second=F(0)
    for j in range(1,len(cycle)-1):
        b=points[cycle[j]];c=points[cycle[j+1]]
        weight=g.det(a,b,c)/(2*body['volume']);assert weight>0
        vals=[g.ell_value(ell,x) for x in (a,b,c)]
        mass+=weight;first+=weight*sum(vals)/3
        second+=weight*(sum(vals)**2+sum(x*x for x in vals))/12
    assert second>=first*first/mass
    return mass,first,second

def body_control(raw,raw_ell,label):
    original=g.hull(raw);center=original['center']
    points=[g.sub(x,center) for x in raw];body=g.hull(points);V=body['volume']
    mu=g.ell_value(raw_ell,center)
    ell=(F(1),)+tuple(x/mu for x in raw_ell[1:])
    assert body['center']==g.ZERO and all(g.ell_value(ell,x)>=0 for x in points)
    facets=[face_second(body,f,ell) for f in body['facets']]
    E2=F(0)
    for f in body['facets']:
        cy=f['cycle'];a=points[cy[0]]
        for j in range(1,len(cy)-1):
            b=points[cy[j]];c=points[cy[j+1]]
            v=g.det(a,b,c)/6
            vals=[F(1)]+[g.ell_value(ell,x) for x in (a,b,c)]
            E2+=v/V*(sum(vals)**2+sum(x*x for x in vals))/20
    assert sum(x[0] for x in facets)==sum(x[1] for x in facets)==3
    assert sum(x[2] for x in facets)==5*E2-2<=6
    assert E2<=F(8,5)
    chi=sum(x[1]*x[1]/x[0] for x in facets)
    assert chi<=5*E2-2
    f1=g.facet_by_set(body,(0,1,2));f2=g.facet_by_set(body,(0,1,3))
    m1,L1,_=face_second(body,f1,ell);m2,L2,_=face_second(body,f2,ell)
    m=m1+m2;T=L1+L2
    assert T*T/m+(3-T)**2/(3-m)<=6
    q1=g.scale(f1['normal'],1/f1['offset']);q2=g.scale(f2['normal'],1/f2['offset'])
    A,B,C,D=points[:4];h=g.tet(A,B,C,D)/V
    p=g.scale(g.add(g.scale(q1,m1),g.scale(q2,m2)),1/m)
    ds=3*h/m;s=1-ds
    assert g.dot(p,A)==g.dot(p,B)==1 and g.dot(p,C)==g.dot(p,D)==s
    va,vb,vc,vd=[g.ell_value(ell,x) for x in (A,B,C,D)]
    q=va+vb
    assert min(va,vb)>=4*T-8
    kmax=min(F(1),1/ds)
    trials=[kmax*z for z in (F(1,4),F(1,2),F(3,4))]
    if s>0:trials.append(F(1))
    tetbody=g.hull([A,B,C,D]);records=[]
    for k in trials:
        t=1-ds*k;assert t>0 and 0<k<=1
        Ap=g.scale(A,t);Bp=g.scale(B,t)
        images=[];weighted=F(0);area=F(0)
        for O in (C,D):
            E=g.add(g.scale(A,1-k),g.scale(O,k))
            W=g.add(g.scale(B,1-k),g.scale(O,k))
            images.append([Ap,Bp,W,E])
            for x in (Ap,Bp,W,E):
                assert g.dot(p,x)==t
                assert all(g.dot(f['normal'],x)<=f['offset'] for f in body['facets'])
            for tri in ((Ap,Bp,W),(Ap,W,E)):
                weight=abs(g.det(*tri))/(2*V)
                area+=weight
                weighted+=weight*sum(g.ell_value(ell,x) for x in tri)/3
        Af=t*t+t*(1-k)+(1-k)**2
        Bf=k*(t+2*(1-k))
        L=t*k*(m*q*Af+(3*T-m*q)*Bf+m*(1-t)*(2*t+1-k))/3
        assert area==t*k*(t+1-k)*m and weighted==L
        f=3*k*k-2*k**3;I=2*k**3-F(3,2)*k**4;Z=f-ds*I
        J=q*(F(3,2)*k*k-2*k**3+F(3,4)*k**4)+(vc+vd)*(k**3-F(3,4)*k**4)
        # Exact truncated tetrahedron, with no centroid assumption on this subbody.
        removed=g.clip(tetbody,g.scale(p,-1),-t)
        assert removed['volume']==h*V*f
        assert g.dot(p,removed['moment'])==h*V*Z
        assert removed['volume']*g.ell_value(ell,removed['center'])==h*V*J
        lower=g.clip(body,p,t)
        cut=[f for f in lower['facets'] if all(g.dot(p,lower['points'][i])==t for i in f['cycle'])]
        assert len(cut)==1
        _,trace=g.cone_integrals(lower,cut[0],ell)
        root_integral=lower['volume']*g.ell_value(ell,lower['center'])
        actual=(1-g.dot(p,lower['center'])/t)*trace/root_integral
        bound=L*(1+h*Z/(t*(1-h*f)))/(1-h*J)
        assert 1-h*f>0 and 1-h*J>0
        assert trace/V>=L
        assert lower['volume']<=(1-h*f)*V
        assert g.dot(p,lower['center'])<=-h*Z/(1-h*f)
        assert root_integral<=V*(1-h*J)
        assert bound<=actual<F(111,100)
        records.append({'k':k,'t':t,'images':images,'rho':h*f,'p_removed_moment':h*Z,
                        'root_removed_moment':h*J,'projected_trace':L,'lower_bound':bound,
                        'actual_cut_trace':actual,'cut_volume':lower['volume'],
                        'cut_center':lower['center'],'cut_points':lower['points'],
                        'cut_facets':[f['cycle'] for f in lower['facets']],
                        'cut_edges':lower['edges']})
    return {'label':label,'raw_points':raw,'raw_ell':raw_ell,'own_center':center,
            'volume':V,'facets':[f['cycle'] for f in body['facets']], 'edges':body['edges'],
            'facet_mass_first_second':facets,'E_ell_squared':E2,'row_chi_square_plus_three':chi,
            'h':h,'m1':m1,'m2':m2,'T':T,'p':p,'s':s,'partial_cuts':records,
            'not_110_witness':True}

def scalar_relaxation_control():
    # A complete rational tuple in a deliberately weaker scalar system.
    # It is not a polytope and is excluded by the new second-moment inequality.
    h=F(1,4);m1=F(7,25);m2=F(6,25);m=m1+m2;T=F(51,25)
    u=F(1109,1000);v=T-u;q=F(8);c=3*u/m1-q;d=3*v/m2-q
    assert 3*h/4<=m1<=F(3,4) and 3*h/4<=m2<=F(3,4)
    assert m<=3*(1+h)/4 and 0<=c<=4 and 0<=d<=4
    assert T-F(111,100)<u<F(111,100) and T-F(111,100)<v<F(111,100)
    assert h*(q+c+d)<4 and q>=8*T-16
    add=g.poly_add;mul=g.poly_mul;sc=g.poly_scale
    k=[F(0),F(1)];one=[F(1)];k2=mul(k,k);k3=mul(k2,k);k4=mul(k3,k)
    t=add(one,sc(k,-3*h/m));w=add(one,sc(k,-1))
    A=add(add(mul(t,t),mul(t,w)),mul(w,w));B=mul(k,add(t,sc(w,2)))
    brace=add(add(sc(A,m*q),sc(B,3*T-m*q)),sc(mul(add(one,sc(t,-1)),add(sc(t,2),w)),m))
    f=add(sc(k2,3),sc(k3,-2));I=add(sc(k3,2),sc(k4,F(-3,2)));Z=add(f,sc(I,-3*h/m))
    J=add(sc(add(add(sc(k2,F(3,2)),sc(k3,-2)),sc(k4,F(3,4))),q),sc(add(k3,sc(k4,F(-3,4))),c+d))
    Df=add(one,sc(f,-h));Dj=add(one,sc(J,-h));D=mul(Df,Dj)
    N=sc(mul(mul(k,brace),add(mul(t,Df),sc(Z,h))),F(1,3))
    P=add(sc(D,F(3,5)),sc(N,-1));kmax=m/(3*h)
    def power(a,n):
        out=one
        for _ in range(n):out=mul(out,a)
        return out
    def bernstein(poly):
        n=len(poly)-1
        coeff=[sum(poly[j]*kmax**j*F(comb(i,j),comb(n,j)) for j in range(i+1)) for i in range(n+1)]
        reconstructed=[F(0)]
        for i,b in enumerate(coeff):
            term=mul(power(k,i),power([F(1),F(-1)],n-i))
            reconstructed=add(reconstructed,sc(term,b*comb(n,i)))
        expected=[v*kmax**j for j,v in enumerate(poly)]
        assert reconstructed==expected and all(b>0 for b in coeff)
        return {'power_coefficients_in_k':poly,'bernstein_coefficients_on_0_kmax':coeff}
    certs={name:bernstein(poly) for name,poly in (('1-h*f',Df),('1-h*J',Dj),('3/5*denominator-numerator',P))}
    lower=u*u/m1+v*v/m2+(3-T)**2/(3-m)
    assert lower==F(436198603,52080000)>6
    return {'h':h,'m1':m1,'m2':m2,'T':T,'lambda_root_1':u,'lambda_root_2':v,
            'a':F(4),'b':F(4),'c':c,'d':d,'q':q,'kmax':kmax,
            'tetrahedron_root_sum_times_h':h*(q+c+d),'certificates':certs,
            'all_partial_cut_bounds_strictly_below':F(3,5),
            'mandatory_second_moment_lower_bound':lower,'excess_over_six':lower-6,
            'not_a_body':True,'excluded_by_second_moment':True}

def run():
    standard=[g.ZERO,(F(0),F(0),F(1)),(F(0),F(1),F(0)),(F(1),F(0),F(0))]
    controls=[body_control(standard,(F(1),F(-1),F(-1),F(0)),'tetrahedron_root_edge_CD')]
    for r in (2,4,8,16):
        r=F(r);e=F(1,100);z=-(2*r-1)/2
        raw=standard+[(r-e,r+e,z),(r+e,r-e,z),(r,r,z+e)]
        controls.append(body_control(raw,(2*r,F(-1),F(-1),F(0)),'true_root_triangle_r_'+str(r)))
    report={'identity':IDENTITY,'arithmetic':arithmetic(),'controls':controls,'scalar_relaxation_control':scalar_relaxation_control(),
            'C_lower_bound_unchanged':34,'full_E17_exclusion':False,
            'exact_minimum_found':False,'analytic_proof_required':True}
    data=(json.dumps(g.serialize(report),sort_keys=True,indent=2)+'\n').encode()
    if len(sys.argv)!=2 or sys.argv[1] not in ('build','check'):
        raise SystemExit('Usage: python -S pair_second_moment_cut_exact.py build|check')
    p=Path(OUTPUT)
    if sys.argv[1]=='build':p.write_bytes(data)
    elif not p.exists() or p.read_bytes()!=data:raise SystemExit('Exact report mismatch.')
    print('ACTUAL_BOUNDARY_SECOND_MOMENT_IDENTITY_PASS 5')
    print('PAIR_HIGH_TRACE_MASS_37_50_H_2_31_PASS 11/625 716236877/270883893100')
    print('PARTIAL_TETRAHEDRON_CUT_TRUE_GEOMETRY_PASS',sum(len(x['partial_cuts']) for x in controls))
    print('PARTIAL_CUT_SCALAR_RELAXATION_BARRIER_EXACT_PASS 17 436198603/52080000')
    print('PAIR_SECOND_MOMENT_PARTIAL_CUT_RECOVERY_PASS',len(data),hashlib.sha256(data).hexdigest())
if __name__=='__main__':run()
