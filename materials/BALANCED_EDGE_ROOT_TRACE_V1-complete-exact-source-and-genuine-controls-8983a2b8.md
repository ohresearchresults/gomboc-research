# material-8983a2b83c22

AI research material

---

"""BALANCED_EDGE_ROOT_TRACE_V1: exact identities and complete physical controls.
CPython 3.13.5, standard library, assertions enabled. No external input or RNG.
Dependencies: the exact two source files in MANIFEST, checked before import.
Run: python -S balanced_root_exact.py build
     python -S balanced_root_exact.py check
The continuous proof is balanced_root_proof.md; controls do not replace it.
"""
from pathlib import Path
import hashlib,json,sys
assert __debug__
MANIFEST={
'joint_mass_stability_exact.py':(8331,'d760d4070fbe920485f68166515e59786da1a3e606d11348e8bf22686b2b2d79'),
'joint_mass_cubic_exact.py':(15282,'532652150f924062e713292192ea709a39b8530b675e0fb35a9ce8766b8ef531')}
for name,(length,sha) in MANIFEST.items():
    data=Path(__file__).with_name(name).read_bytes()
    assert (len(data),hashlib.sha256(data).hexdigest())==(length,sha)
import joint_mass_cubic_exact as base
F=base.F
encode=base.encode

def poly(rows):return {tuple(k):F(v) for k,v in rows if v}
def const(c):return {(0,0):F(c)} if c else {}
def add(*ps):
    out={}
    for p in ps:
        for k,v in p.items():out[k]=out.get(k,F(0))+v
    return {k:v for k,v in out.items() if v}
def scale(p,c):return {k:v*c for k,v in p.items() if v*c}
def mul(p,q):
    out={}
    for (a,b),v in p.items():
        for (c,d),w in q.items():
            k=(a+c,b+d);out[k]=out.get(k,F(0))+v*w
    return {k:v for k,v in out.items() if v}
def power(p,n):
    out=const(1)
    for _ in range(n):out=mul(out,p)
    return out
def compose(p,x,y):
    return add(*(scale(mul(power(x,i),power(y,j)),v) for (i,j),v in p.items()))
def evalp(p,x,y):return sum(v*x**i*y**j for (i,j),v in p.items())
def rows(p):return [[i,j,p[i,j]] for i,j in sorted(p)]

def polynomial_identities():
    a=poly([((1,0),1)]);w=poly([((0,1),1)]);one=const(1)
    # Literal numerator after clearing the positive denominator 6*a^2*(t-1).
    P_at=poly([((4,2),2),((4,1),-1),((3,3),2),((3,2),-5),((3,1),3),
               ((2,2),-3),((2,1),-3),((1,1),7),((1,0),1),((0,0),-3)])
    # Exact substitution t=w/a; all resulting exponents are nonnegative.
    assert all(i>=j for i,j in P_at)
    P_aw=poly([((i-j,j),v) for (i,j),v in P_at.items()])
    am=add(one,scale(a,-1));wm=add(w,scale(one,-1))
    a_quad=add(power(a,2),scale(a,-6),const(7))
    assert a_quad==add(power(am,2),scale(am,4),const(2))
    terms=[mul(power(am,2),add(const(3),scale(a,-1))),
           mul(mul(wm,am),a_quad),
           mul(mul(power(wm,2),am),add(const(3),scale(a,-2))),
           scale(power(wm,3),2)]
    assert add(*terms)==P_aw
    # Substitution a=1-v,w=1+u makes every coefficient nonnegative.
    positive=compose(P_aw,add(one,scale(a,-1)),add(one,w))
    assert all(v>0 for v in positive.values())
    # Uncut comparison denominator and derivative numerator.
    # d/da [(3-a)/(4-a(t+1))] has numerator 3t-1.
    t=w
    derivative=add(scale(add(t,one),3),const(-4))
    assert derivative==add(scale(t,3),const(-1))
    # Negative-alpha comparison: 2*denominator - numerator is positive.
    h=a;alpha=w
    D=add(scale(h,4),scale(mul(alpha,add(one,h)),-1))
    numerator=mul(mul(add(const(3),scale(alpha,-1)),h),add(one,h))
    difference=add(scale(D,2),scale(numerator,-1))
    expected=add(mul(h,add(const(5),scale(h,-3))),
                 scale(mul(mul(alpha,add(one,h)),add(const(2),scale(h,-1))),-1))
    assert difference==expected
    eps0=F(7,45)/(25*(2-F(7,45)**2))
    assert eps0==F(63,20005)
    return {'clipped_numerator_a_t':rows(P_at),'clipped_numerator_a_w':rows(P_aw),
            'four_nonnegative_terms':list(map(rows,terms)),
            'positive_expansion_a_1_minus_v_w_1_plus_u':rows(positive),
            'negative_alpha_difference':rows(difference),'universal_imbalance_cutoff':eps0}

def I_equal(t,a):
    assert t>=1 and 0<a<=1
    if t==1:return F(1,2)-a/3
    if a*t<=1:return t*(3-a*(t+1))/6
    return (a**3*t-3*a*a*t+3*a*t-1)/(6*a*a*(t-1))

def comparison_bound(h,a):
    assert 0<h<=1 and a<=1
    if a<=0:return (3-a)*h*(1+h)/(4*h-a*(1+h))
    t=1/h;A=t/2;I=I_equal(t,a)
    return (3-a)*(A-I)/(2*a*A*(A/3+I))

def exact_integral_controls():
    old=base.old
    controls=[]
    # These evaluate exact integration formulae, not a sampled universal proof.
    for t,a in ((F(1),F(1)),(F(5),F(1,5)),(F(5),F(1,2)),(F(10,3),F(3,4)),(F(2),F(1))):
        if t==1:
            integ=old.integral(old.mul([1,-a],[0,1]),0,1)
        else:
            cut=min(t,1/a)
            integ=old.integral(old.mul([1,-a],[0,1]),0,1)
            if cut>1:
                integ+=old.integral(old.scale(old.mul([1,-a],[t,-1]),1/(t-1)),1,cut)
        assert integ==I_equal(t,a)
        bound=comparison_bound(1/t,a)
        assert bound<=2
        if t>1 or a<1:assert bound<2
        controls.append([t,a,integ,bound])
    # The radial clipped moment formula for every tested rational radius and cap.
    rays=[]
    for R,H in ((F(2),F(3)),(F(3),F(1)),(F(7,3),F(5,4)),(F(1),F(1))):
        m=min(R,H)
        measured=m**3/12+max(F(0),R*R-H*H)*H/8
        expected=m*(3*R*R-m*m)/24
        assert measured==expected
        rays.append([R,H,measured])
    return {'planar_profile_integrals':controls,'radial_clipped_moment_identities':rays}

SMALL=[(F(3,4),F(5,4),F(-2,5)),(F(5,4),F(3,4),F(-3,5)),(1,1,F(-3,10))]
LARGE=[(1,3,-1),(3,1,-2),(2,2,F(-1,2))]
NEAR=[(F(1,3),F(7,9),F(1,20)),(F(7,9),F(1,3),F(-1,20)),(F(5,9),F(5,9),F(1,10))]
ASYM=[(1,F(5,4),0),(2,F(5,6),F(-1,2)),(3,F(5,12),F(-1,4))]

def physical(name,extra,vals,root_required,balanced):
    vals=tuple(map(F,vals));assert vals[0]==vals[1] and max(vals)>0 and min(vals)>=0
    P=base.hull(base.T0+extra)
    faces={frozenset(f) for f in P['faces']}
    assert frozenset((0,1,2)) in faces and frozenset((0,1,3)) in faces
    assert (0,1) in P['edges']
    assert all(base.ell_at(vals,p)>=0 for p in P['points'])
    root=frozenset(i for i in P['vertices'] if base.ell_at(vals,P['points'][i])==0)
    if root_required:assert root in faces
    T=base.trace(P,vals);h=1/(6*P['volume'])
    result={'name':name,'polytope':P,'ell_ABCD':vals,'root_indices':sorted(root),
            'root_is_maximal_facet':root in faces,'h':h,'trace':T,'claim_110':False}
    if balanced:
        assert vals[2]==vals[3]
        if vals[0]==0:
            bound=h;assert T==h
        else:
            alpha=1-vals[2]/vals[0]
            bound=comparison_bound(h,alpha)
            result['alpha']=alpha
        assert T<=bound<=2
        if not (len(P['vertices'])==4 and vals[2]==0):assert T<2
        result['proved_comparison_bound']=bound
    else:
        a,b,c,d=vals;eps=abs(c-d)/max(vals)
        upper=2+eps*(2/h-h)
        assert T<upper
        top=max(c,d);vp=(a,b,top,top)
        assert all(base.ell_at(vp,p)>=0 for p in P['points'])
        assert base.trace(P,vp)<2
        B=base.integral_ell(P,vals);X,Y,_=P['moment'];V=P['volume']
        # For c<d we raise c by adding (d-c)y, so the correction exchanges X,Y.
        corr=(c-d)*(2*X/B-Y/(6*V*B)) if c>=d else (d-c)*(2*Y/B-X/(6*V*B))
        assert T<2+corr
        result.update({'balanced_plus_values':vp,'balanced_plus_trace':base.trace(P,vp),
                       'exact_perturbation_upper':2+corr,'normalized_imbalance':eps,
                       'uniform_perturbation_upper':upper})
    return result

def report():
    controls=[
      physical('tetrahedron_equality_function_zero_on_edge',[],(1,1,0,0),False,True),
      physical('actual_root_h_below_one_half',SMALL,(1,1,F(1,2),F(1,2)),True,True),
      physical('actual_root_large_projection',LARGE,(1,1,F(3,4),F(3,4)),True,True),
      physical('actual_root_near_CD',NEAR,(1,1,F(1,10),F(1,10)),True,True),
      physical('negative_alpha_no_zero_set',LARGE,(1,1,2,2),False,True),
      physical('zero_endpoint_values',SMALL,(0,0,1,1),False,True),
      physical('asymmetric_actual_root_perturbation',ASYM,(1,1,F(2,5),F(3,4)),True,False)]
    assert controls[0]['trace']==2 and not controls[0]['root_is_maximal_facet']
    assert controls[1]['h']==F(40,113)
    assert controls[2]['h']<F(3,10)
    return {'identity':'BALANCED_EDGE_ROOT_TRACE_V1','proof_file':'balanced_root_proof.md',
            'exact_identities':polynomial_identities(),'integral_controls':exact_integral_controls(),
            'physical_controls':controls,'claim_C_ge_36':False,'claim_exact_minimum':False}

def main():
    if len(sys.argv)!=2 or sys.argv[1] not in ('build','check'):
        raise SystemExit('Use build or check; assertions must be enabled.')
    r=report();data=(json.dumps(encode(r),ensure_ascii=True,sort_keys=True,indent=2)+'\n').encode('utf-8')
    out=Path('balanced_root_exact.json')
    if sys.argv[1]=='build':out.write_bytes(data)
    else:assert out.read_bytes()==data
    print('ROOT_CLIPPED_RADIAL_AND_PLANAR_IDENTITIES_PASS')
    print('BALANCED_ROOT_FOUR_NONNEGATIVE_TERMS_PASS')
    print('BALANCED_ROOT_ACTUAL_PHYSICAL_CONTROLS_PASS',len(r['physical_controls']))
    print('BALANCED_ROOT_EXACT_PASS',len(data),hashlib.sha256(data).hexdigest())
if __name__=='__main__':main()
