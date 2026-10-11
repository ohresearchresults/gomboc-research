# material-49738e9e414f

Historical AI scientific source/proof material. Statements retain their original scope; this is not an independently reviewed theorem.

---

"""Arbitrary concave homothetic tails: tangential whole-facet moment theorem.
Exact analytical identities and actual-profile controls, not sampled certification
of the continuum theorem. CPython 3.11+, SymPy 1.13+, assertions enabled.
"""
from pathlib import Path
from itertools import combinations
from math import factorial
import hashlib,json,platform
import sympy as S
Q=S.Rational
z,t,q,r,b,lam=S.symbols('z t q r b lam', real=True)

def clean(v):return S.factor(S.cancel(v))
def eq(a,b=0):assert clean(a-b)==0,clean(a-b)
def integ(v,a=0,b=1,var=t):return clean(S.integrate(S.expand(v),(var,a,b)))
def serial(v):
    if isinstance(v,S.MatrixBase):return [[serial(v[i,j]) for j in range(v.cols)] for i in range(v.rows)]
    if isinstance(v,S.Basic):return str(v)
    if isinstance(v,dict):return {str(k):serial(x) for k,x in v.items()}
    if isinstance(v,(list,tuple)):return [serial(x) for x in v]
    return v

def algebra():
    k=1-t;u=k+r*t;mark=q+(1-q)*t
    vm=integ(mark**2);nm=integ(mark**4);p=integ(mark**3)
    vr=integ(u**2);nr=integ(u**4);mr=integ(t*u**2)
    J=clean(nm-p+Q(3,5)*vm)
    eq(p*(1-q),(1-q**4)/4)
    eq(nr-Q(3,5)*vr,(r**3+r**4)/5)
    eq(Q(3,4)*vr-mr,(2+r)/12)
    eq(J-Q(7,20)*vm,integ(mark**2*(mark-Q(1,2))**2))
    F=clean((vm+b*vr)*(nm+b*nr)-p*(p+b*vr+b*b*(1-q)*mr))
    eq(F,vm*nm-p*p+b*(vm*nr+vr*(nm-p))+b*b*(vr*nr-p*(1-q)*mr))
    # Reference decreasing-ratio integrals used by the continuum proof.
    eq(integ(t*k**3)/integ(t*k),Q(3,10))
    eq(integ(t*t*k*k)/integ(t*t),Q(1,10))
    eq(u**3-Q(3,10)*u,k**3-Q(3,10)*k+3*r*t*(k*k-Q(1,10))+3*r*r*t*t*k+r**3*t**3)
    A,B,C,D,E,G,V,N,P,T1,T2=S.symbols('A B C D E G V N P T1 T2')
    expression=(V+2*lam*A+lam**2*B)*(N+4*lam*C+6*lam**2*D+4*lam**3*E+lam**4*G)-P*(2*lam*T1+lam**2*T2)
    observed=[S.expand(expression).coeff(lam,j) for j in range(1,7)]
    expected=[2*A*N+4*C*V-2*P*T1,B*N+8*A*C+6*D*V-P*T2,
              4*E*V+12*A*D+4*B*C,G*V+8*A*E+6*B*D,2*A*G+4*B*E,B*G]
    for x,y in zip(observed,expected):eq(x,y)
    # Literal positive endpoint/control examples, including an infinite initial slope.
    weights=[]
    for g in [t,1-t,t*(1-t),S.sqrt(t),S.sqrt(t)*(1-t)]:
        # 1-t does not obey g(0)=0 and is not needed for the proof; it is a stricter check.
        for rr in [0,Q(1,7),1,3]:
            uu=k+rr*t
            d1=integ(g*(uu**3-Q(3,10)*uu));d2=integ(g*g*(uu*uu-Q(1,10)))
            assert d1>=0 and d2>=0
            weights.append(dict(g=g,r=rr,linear_weight_gap=d1,quadratic_weight_gap=d2))
    return dict(marked_moments=(vm,p,nm),tail_moments=(vr,mr,nr),J=J,
                affine_tail_defect=F,variation_coefficients=observed,weight_controls=weights)

def base_polygon():
    raw=[S.Matrix(v) for v in [(0,0),(3,0),(4,1),(2,3),(-1,2)]]
    area=0;first=S.zeros(2,1);second=S.zeros(2)
    for a,bb in zip(raw,raw[1:]+raw[:1]):
        d=S.det(S.Matrix.hstack(a,bb));area+=d/2;first+=d*(a+bb)/6
        second+=d*((a*a.T+bb*bb.T)/12+(a*bb.T+bb*a.T)/24)
    centre=first/area;cov=(second/area-centre*centre.T).applyfunc(clean)
    assert area>0 and cov.det()>0
    return [(v-centre).applyfunc(clean) for v in raw],area,cov,centre

def moments(pieces):
    vv=mm=nn=ee=0
    for a,bb,h in pieces:
        vv+=integ(h*h,a,bb,z);mm+=integ(z*h*h,a,bb,z)
        nn+=integ(h**4,a,bb,z);ee+=integ(z*z*h*h,a,bb,z)
    vv,mm,nn,ee=map(clean,(vv,mm,nn,ee));mu=clean(mm/vv);ss=clean(ee-mm*mm/vv)
    return vv,mu,ss,nn

def sides(pieces,base,area,cov):
    vv,mu,ss,nn=moments(pieces);Sigma=S.zeros(3)
    Sigma[:2,:2]=nn/vv*cov;Sigma[2,2]=ss/vv
    records=[]
    for j,(lo,hi,h) in enumerate(pieces):
        if S.diff(h,z,2)!=0:continue
        slope=S.diff(h,z);d0=clean(h.subs(z,mu))
        p1=integ(h,lo,hi,z);p2=integ(h*h,lo,hi,z);p3=integ(h**3,lo,hi,z)
        pz0=integ(h*(z-mu),lo,hi,z);pz1=integ(h*h*(z-mu),lo,hi,z);pz2=integ(h*(z-mu)**2,lo,hi,z)
        H=clean(nn-d0*p3);R=clean(Q(9,4)*ss-d0*pz2);mixed=clean(H*R-d0*d0*pz1*pz1)
        assert H>=0
        matrices=[]
        for k,(a,bb) in enumerate(zip(base,base[1:]+base[:1])):
            ce=(a+bb)/2;te=(a*a.T+bb*bb.T)/3+(a*bb.T+bb*a.T)/6
            beta=clean(S.det(S.Matrix.hstack(a,bb))/area)
            edge=bb-a;normal=S.Matrix([edge[1],-edge[0]]);support=clean(normal.dot(a))
            assert support>0 and beta>0 and d0>0
            T=S.zeros(3);T[:2,:2]=p3/p1*te;T[:2,2]=pz1/p1*ce;T[2,:2]=(pz1/p1*ce).T;T[2,2]=pz2/p1
            pole=S.Matrix([normal[0]/support,normal[1]/support,-slope])/d0
            cf=S.Matrix([*(p2/p1*ce),pz0/p1]);assert (T*pole-cf).applyfunc(clean)==S.zeros(3,1)
            alpha=clean(beta*d0*p1/vv);gap=(Q(3,2)*Sigma-alpha*T).applyfunc(clean)
            minors=[clean(gap.extract(ix,ix).det()) for size in [1,2,3] for ix in combinations(range(3),size)]
            assert all(v>=0 for v in minors)
            matrices.append(dict(edge=k,alpha=alpha,T=T,pole=pole,centroid=cf,gap_minors=minors))
        records.append(dict(piece=j,line=h,D0=d0,P3=p3,H=H,R=R,mixed_gap=mixed,facets=matrices))
    return dict(volume=clean(area*vv),centroid=(0,0,mu),Sigma=Sigma,
                axial=(vv,mu,ss,nn),sides=records)

def chord(pieces,index):
    out=list(pieces);lo,hi,h=out[index];line=clean(h.subs(z,lo)+(h.subs(z,hi)-h.subs(z,lo))*(z-lo)/(hi-lo))
    out[index]=(lo,hi,line);return out

def failed_tail_mass_bound():
    # Actual two-piece concave profiles refute H >= c D0^2 Vout for every fixed c>0.
    eps=S.symbols('eps',positive=True);h=(1+eps-z)/eps
    vv=clean(1+integ(h*h,1,1+eps,z));mm=clean(Q(1,2)+integ(z*h*h,1,1+eps,z))
    mu=clean(mm/vv);nn=1+eps/5;d0=clean((1+eps-mu)/eps)
    ss=clean(Q(1,3)+integ(z*z*h*h,1,1+eps,z)-mm*mm/vv)
    cc=integ(h*h*(z-mu),1,1+eps,z);pzz=integ(h*(z-mu)**2,1,1+eps,z)
    HH=clean(nn-d0*eps/4);RR=clean(Q(9,4)*ss-d0*pzz);GG=clean(HH*RR-d0*d0*cc*cc)
    ratio=clean(HH/d0**2);eq(S.limit(ratio/eps**2,eps,0),Q(7,2))
    for vv0 in [HH,RR,GG]:
        num,den=S.fraction(vv0)
        assert all(c>0 for c in S.Poly(num,eps).all_coeffs())
        assert all(c>=0 for c in S.Poly(S.expand(den),eps).all_coeffs())
    return dict(profile=((0,1,S.Integer(1)),(1,1+eps,h)),V=vv,mu=mu,S=ss,
                D0=d0,H=HH,Pz1=cc,R=RR,mixed_gap=GG,Vout=1,ratio=ratio,
                ratio_over_eps_squared_limit=Q(7,2),
                meaning='Refutes only the proposed uniform tail-mass lower bound, not the tangential or full3/2 inequality.')

def main():
    assert __debug__
    cert=algebra();base,area,cov,rawg=base_polygon()
    curved=[(-1,0,1+z/3-z*z/4),(0,1,1+z/3),(1,2,1+z/3-(z-1)**2/2)]
    for i,(lo,hi,h) in enumerate(curved):
        assert h.subs(z,lo)>0 and h.subs(z,hi)>0 and S.diff(h,z,2)<=0
        if i:assert curved[i-1][2].subs(z,lo)==h.subs(z,lo) and S.diff(curved[i-1][2],z).subs(z,lo)>=S.diff(h,z).subs(z,lo)
    both=curved;right=chord(both,2);straight=chord(right,0)
    profiles={name:sides(pp,base,area,cov) for name,pp in [('curved',both),('right_straight',right),('both_straight',straight)]}
    defects=[]
    for pp in [both,right,straight]:
        vv,mu,ss,nn=moments(pp);p3=integ((1+z/3)**3,0,1,z);defects.append(clean(vv*(nn-(1+mu/3)*p3)))
    assert defects[0]>defects[1]>defects[2]>0
    # The earlier exact five-piece body: 30/55/27 and strict244 weak0 in the endcap capsule.
    knots=[Q(i,5) for i in range(6)];heights=list(map(S.sympify,[1,Q(7,5),Q(17,10),Q(9,5),Q(8,5),1]))
    pl=[(knots[i],knots[i+1],heights[i]+(heights[i+1]-heights[i])*(z-knots[i])/(knots[i+1]-knots[i])) for i in range(5)]
    profiles['five_piece']=sides(pl,base,area,cov)
    profiles['prism']=sides([(0,1,S.Integer(1))],base,area,cov)
    assert profiles['prism']['sides'][0]['H']==0
    for item in profiles['five_piece']['sides']:assert item['H']>0
    for pp in [curved,right,straight,pl]:
        for (a,bb,h),(c,d,k) in zip(pp,pp[1:]):assert bb==c and h.subs(z,bb)==k.subs(z,c)
    report=dict(identity='ARBITRARY_CONCAVE_PROFILE_TANGENTIAL_SIDE_DEFECT_MONOTONICITY_V1',
        algebra=cert,failed_tail_mass_bound=failed_tail_mass_bound(),base=base,raw_base_centroid=rawg,base_area=area,base_covariance=cov,
        literal_profiles=dict(curved=curved,right_straight=right,both_straight=straight,five_piece=pl),
        curved_straightening_volume_cleared_defects=defects,profiles=profiles,
        scope='Universal H=N4-D0 P3>=0 for every affine marked interval, with strictness except a whole prism profile. Full mixed determinants are checked on controls only, not proved for arbitrary tails. No U2, E17 exclusion or new110 attainer.',
        environment=dict(python=platform.python_version(),sympy=S.__version__))
    data=(json.dumps(serial(report),sort_keys=True,indent=2)+'\n').encode();Path('profile_tangential_report.json').write_bytes(data)
    print('MONOTONE_RATIO_BETA_INTEGRALS_AND_ALL_VARIATION_COEFFICIENTS_PASS')
    print('ARBITRARY_CONCAVE_TAIL_STRAIGHTENING_TANGENTIAL_DEFECT_PASS')
    print('ACTUAL_CURVED_TAIL_AND_25_FIVE_PIECE_WHOLE_SIDE_TENSORS_PASS')
    print('REPORT',len(data),hashlib.sha256(data).hexdigest())
    print('PROFILE_TANGENTIAL_DEFECT_COMPLETE_SOURCE_RECOVERY_PASS')
if __name__=='__main__':main()
