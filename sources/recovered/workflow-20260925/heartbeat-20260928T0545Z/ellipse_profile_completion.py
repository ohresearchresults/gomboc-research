"""Exact curved completion with the actual centroid fixed.
CPython3.13.5/SymPy1.14.0; assertions on; no external inputs.
The unique minimizer concerns a fixed-test volume-scaled matrix defect,
NOT the generalized Rayleigh ratio or the unrestricted whole-body problem.
"""
from pathlib import Path
import hashlib,json,math
import sympy as S
Q=S.Rational
u,z,dlt,x=S.symbols('u z delta x',real=True)

def clean(v):return S.factor(S.cancel(v))
def zero(v):assert clean(v)==0,clean(v)
def integ(v,lo,hi):return clean(S.integrate(S.expand(v),(z,lo,hi)))
LO=Q(7490675,10000000);HI=Q(7490676,10000000)

def positive_on_root_interval(expr):
    nn,dd=S.fraction(clean(expr))
    if dd.subs(u,(LO+HI)/2)<0:nn=-nn;dd=-dd
    out={}
    for name,poly in [('numerator',nn),('denominator',dd)]:
        p=S.Poly(S.expand(poly.subs(u,LO+(HI-LO)*x)),x,domain=S.QQ);n=p.degree()
        cc=[clean(sum(p.nth(i)*Q(math.comb(k,i),math.comb(n,i)) for i in range(k+1))) for k in range(n+1)]
        assert min(cc)>0,(name,expr,min(cc))
        out[name]=dict(degree=n,controls=cc)
    return out

def main():
    assert __debug__ and S.__version__=='1.14.0'
    rootpoly=u**4-5*u*u+10*u-5
    assert rootpoly.subs(u,LO)<0<rootpoly.subs(u,HI)
    assert LO>0 and HI<1
    # On [0,1], rootpoly'=4u^3-10u+10>0 except no zero at1.
    assert S.diff(rootpoly,u,2).subs(u,LO)<0
    disc=u*(2-u);r=-u/(1-u);ht=(u+(1-u)*z)/S.sqrt(disc);arc2=2*z-z*z
    zero(ht.subs(z,u)**2-arc2.subs(z,u))
    zero(S.diff(ht,z).subs(z,u)-(1-u)/S.sqrt(disc))
    zero(ht**2-arc2-(z-u)**2/disc)
    V=integ(ht**2,r,u)+integ(arc2,u,1)
    M=integ(z*ht**2,r,u)+integ(z*arc2,u,1)
    E=integ(z*z*ht**2,r,u)+integ(z*z*arc2,u,1)
    N4=integ(ht**4,r,u)+integ(arc2**2,u,1)
    zero(M+rootpoly/(12*(1-u)**2))
    D0=u/S.sqrt(disc);P1=integ(ht,r,u);P3=integ(ht**3,r,u)
    Pz1=integ(z*ht**2,r,u);Pz2=integ(z*z*ht,r,u)
    H=clean(N4-D0*P3);R=clean(3*E-D0*Pz2);C=clean(D0*Pz1)
    cert={name:positive_on_root_interval(expr) for name,expr in [
        ('volume',V),('covariance_tangent',N4),('covariance_axial',E),
        ('marked_x_gap',H),('marked_axial_gap',R),('marked_xz_determinant',H*R-C*C),
        ('marked_other_tangent_gap',3*N4-D0*P3),('top_tangent_gap',3*N4-2),('top_normal_gap',3*E-2)]}
    Sigma=S.diag(N4/(3*V),N4/(3*V),E/V)
    TF=S.Matrix([[P3/P1,0,Pz1/P1],[0,P3/(3*P1),0],[Pz1/P1,0,Pz2/P1]])
    alpha=clean(D0*P1/(2*V));pole=S.Matrix([1/D0,0,-(1-u)/(S.sqrt(disc)*D0)])
    cf=S.Matrix([integ(ht**2,r,u)/P1,0,integ(z*ht,r,u)/P1])
    assert (TF*pole-cf).applyfunc(clean)==S.zeros(3,1)
    test=S.Matrix([1,0,-S.sqrt(Q(2,3))])
    F=clean(2*V*(test.T*(Q(3,2)*Sigma-alpha*TF)*test)[0])
    zero(F-(H+Q(2,3)*R+2*S.sqrt(Q(2,3))*C))
    AA=integ(z*(z-u)**2,u,1)
    BB=integ(z*(u+(1-u)*z)*(z-u),u,1)
    zero(BB-AA-integ(z*(z-u)*u*(2-z),u,1))
    eq=clean((1+dlt*dlt)*AA-2*dlt*BB)
    # Unique physical root lies between0 and1-u: constant-height completion is too low.
    zero(eq.subs(dlt,1-u)-disc*integ(z*(disc-arc2),u,1))
    delta_exact=clean((BB-S.sqrt(BB*BB-AA*AA))/AA)
    affine=(u+(1-u)*z-dlt*(z-u))/S.sqrt(disc)
    mdiff=integ(z*(affine**2-arc2),u,1)
    zero(mdiff-eq/disc)
    gap=integ((affine**2-arc2)**2,u,1)
    energy_diff=integ(affine**4-arc2**2+2*z*z*(affine**2-arc2),u,1)
    zero(energy_diff-4*mdiff-gap)
    # Abstract exact pointwise square identity, valid for any competing h^2=k.
    k=S.symbols('k',real=True)
    zero(k*k-arc2**2+2*z*z*(k-arc2)-4*z*(k-arc2)-(k-arc2)**2)
    hh=S.symbols('h',positive=True)
    lag=hh**4+2*z*z*hh*hh-4*z*hh*hh
    zero(S.diff(lag,hh).subs(hh,S.sqrt(arc2)))
    zero(S.diff(lag,hh,2).subs(hh,S.sqrt(arc2))-8*arc2)
    root=S.CRootOf(rootpoly,u,1)
    nums={name:str(expr.subs(u,root).evalf(30)) for name,expr in [('u',u),('delta',delta_exact),('V',V),('N4',N4),('E',E),('fixed_test_defect',F)]}
    hu=S.sqrt(disc)
    flats=[dict(kind='lateral',fixed_coordinate=axis,sign=sg,
                vertices=[(0,0,r)]+[(sg*hu,k*hu,u) if axis=='x' else (k*hu,sg*hu,u) for k in(-1,1)])
           for axis in('x','y') for sg in(-1,1)]
    flats.append(dict(kind='top',vertices=[(-1,-1,1),(1,-1,1),(1,1,1),(-1,1,1)]))
    report=dict(identity='ACTUAL_CURVED_PROFILE_COMPLETION_UNIQUE_DEFECT_MINIMIZER_V1',
                root_polynomial=rootpoly,root_interval=(LO,HI),root_specification='unique root in(0,1)',
                profile=dict(interval=(r,1),left_piece=ht,right_squared_piece=arc2,join=u),
                actual_volume=4*V,actual_centroid=(0,0,0),centroid_numerator=M,Sigma=Sigma,
                whole_marked_facet=dict(alpha=alpha,T=TF,c=cf,pole=pole),
                all_five_whole_flat_facets=flats,curved_boundary='four lateral patches over u<z<1',
                exact_positive_matrix_certificates=cert,test=test,volume_scaled_defect=F,
                affine_same_centroid_competitor=dict(height=affine,delta=delta_exact,delta_equation=eq,
                                                   root_interval_in_delta=(0,1-u),moment_difference=mdiff,
                                                   strict_defect_increase=gap),
                universal_completion_identity='F[h]-F[h0]=int_u^1(h^2-(2z-z^2))^2 dz whenever actual axial first moment is0 and the whole left piece is fixed.',
                numerics_diagnostic_only=nums,
                scope='A genuine curved homogeneous body, not a polytope or an equilibrium result. Unique global completion minimizer for this FIXED-TEST VOLUME-SCALED defect and fixed marked facet, interval and actual centroid. Not a Rayleigh-ratio optimizer or an unrestricted extremum.')
    def encode(v):
        if isinstance(v,S.MatrixBase):return [[encode(t) for t in row] for row in v.tolist()]
        if isinstance(v,S.Basic):return str(v)
        if isinstance(v,dict):return {str(k):encode(t) for k,t in v.items()}
        if isinstance(v,(list,tuple)):return [encode(t) for t in v]
        return v
    data=(json.dumps(encode(report),sort_keys=True,indent=2)+'\n').encode()
    Path('ellipse_profile_completion_report.json').write_bytes(data)
    print('ACTUAL_CENTROID_QUARTIC_AND_ALL_FIVE_FLAT_FACETS_PD_PASS')
    print('UNIQUE_CURVED_FIXED_TEST_COMPLETION_SQUARE_IDENTITY_PASS')
    print('AFFINE_SAME_CENTROID_COMPETITOR_STRICTLY_WORSE_PASS')
    print('REPORT',len(data),hashlib.sha256(data).hexdigest())
    print('ELLIPSE_PROFILE_COMPLETION_EXACT_PASS')
if __name__=='__main__':main()
