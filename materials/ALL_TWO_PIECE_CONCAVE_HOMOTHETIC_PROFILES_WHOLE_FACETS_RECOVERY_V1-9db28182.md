# material-9db28182e955

AI research material · [Export notes](../catalog/coverage.md#text-records)

<!-- historical-status:start -->
> **Historical AI material.** The title and claims below reflect the AI’s assessment at the time. Claims of proof, certification or completion are not a current verification verdict.
>
> [C622](../C622/README.md) passes the supplied exact checks; C<500 remains open; Minimum’s C≥34 remains a working lower bound requiring a consolidated proof. See [verification status and source gaps](../catalog/coverage.md).
<!-- historical-status:end -->

---

# All two-piece concave homothetic profiles: every whole facet satisfies the3/2 bound

## 1. The theorem and its exact scope
Let D be any compact full-dimensional convex planar body. Let h be a nonnegative concave function on a compact interval, positive on its interior, with at most TWO affine pieces. The actual uniformly filled body

    P={(h(z)u,z):u in D}

satisfies, for EVERY genuine whole flat facet F,

    alpha_F T_F <= (3/2) Sigma,

in positive-semidefinite order, where Sigma is the volume covariance about the actual volume centroid g, T_F is the uniform WHOLE-facet second moment about THAT SAME g, and alpha_F=distance(g,aff F) Area(F)/Volume(P). The result includes arbitrary asymmetric bases, all mixed test directions, both end caps when present, every lateral facet of either piece, and all nonsingular affine images. It includes arbitrary homogeneous bipyramids with homothetic cross-sections, two frusta joined at a largest section, and genuinely monotone two-piece profiles. The constant3/2 is sharp for the whole class because rectangular prisms attain it. No claim of strictness for every nonprism is needed.

This is NOT the arbitrary-concave-profile theorem, the universal3D whole-facet theorem, an equilibrium exclusion, an E17 incidence theorem, or a new110 construction. The accepted separate bounds34 and622 remain unchanged.

The analytical dependency is the accepted arbitrary uniform-planar whole-edge theorem in [internal-source-reference], SHA240b58ed6bde2703c5788573c8c20ca2a4278a3abc1cfc66fb8f607645eb646d,13829B. It gives alpha_D T_e<=(3/2) Sigma_D and alpha_D<=2/3 for an actual centred planar D and WHOLE edge e. Its full material was read. The affine-profile degeneracy uses the sharp all-frustum theorem in [internal-source-reference] and its complete executable source in [internal-source-reference]. These are actual geometric theorems, not independently chosen moment data.

## 2. A full-matrix reduction valid for arbitrary concave profiles
Translate the actual area centroid of D to0, and let

    V=int h^2, M=int z h^2, mu=M/V,
    E=int z^2 h^2, S=E-M^2/V>0, N4=int h^4.

The actual3D volume is Area(D)V, its centroid is(0,0,mu), and

    Sigma=diag((N4/V) Sigma_D, S/V).

For a genuine affine piece I of h, extend its line h_I(z)=A+Bz and put D0=h_I(mu)>0. Positivity follows from the supporting plane and the actual interior centroid. Define

    P3=int_I h^3,
    Pz1=int_I h^2(z-mu),
    Pz2=int_I h(z-mu)^2.

A lateral whole facet over a whole base edge e has

    alpha_F T_F=(alpha_D D0/V) [[P3 T_e, Pz1 c_e],
                               [Pz1 c_e^T, Pz2]],

where c_e is the generally nonzero edge centroid about the actual base centroid. The mixed block is retained; unlike a single frustum, it does not generally vanish.

The imported planar theorem and alpha_D<=2/3 imply that it suffices to prove

    H=N4-D0 P3>=0,
    R0=(9/4)S-D0 Pz2>=0,
    H R0-D0^2 Pz1^2>=0.                         (SC)

Indeed the desired full gap dominates alpha_D/V times the block matrix

    [[H T_e,-D0 Pz1 c_e],[-D0 Pz1 c_e^T,R0]].

Since T_e-c_e c_e^T is positive semidefinite, split off H(T_e-c_e c_e^T) and apply the remaining scalar2x2 matrix to(c_e dot v,w). This works also when H=0. Thus(SC) is a sufficient, fully coupled one-dimensional criterion for an arbitrary concave homothetic profile, not just two pieces. The unresolved extension is proving(SC), or a sharper correlated-base replacement, for every actual concave profile and every genuine affine piece. No finite random exploration proves that extension.

## 3. Complete normalization and three parameter charts
For a genuine interior slope change, rescale z and h to write

    h(z)=1+(1-l)z/a,  -a<=z<=0,
    h(z)=1-(1-q)z,    0<=z<=1,

with a>0,l,q>=0 and concavity(1-l)/a>=q-1. Every such profile lies in at least one of the following complete charts:

    central maximum: a>0,0<=l<=1,0<=q<=1;
    monotone left: l=1+a(1-q)x, a>0,0<=q,x<=1;
    monotone right: q=1+(1-l)x/a, a>0,0<=l,x<=1.

Both endpoint heights cannot exceed1 under concavity. If l>1, concavity forces q<1 and x=(l-1)/(a(1-q)) in[0,1]. The right case is symmetric. Equality and zero endpoint heights are included.

A crucial true-facet qualification: when the two slopes coincide, the apparent two lateral pieces are COPLANAR and must merge into ONE maximal facet. One must NOT sum two half-facet estimates, whose alpha and normalization differ from the whole-facet problem. The equality-of-slopes case is a single affine profile and is covered by the already proved all-frustum theorem; a constant profile is covered by the uniform-prism theorem. The exact control generator removes its spurious middle ring. When an endpoint height is0, there is an apex, not a zero-area end cap.

## 4. Seven explicit polynomial certificates close every chart
Put

    f(n,j,c)=int_0^1 (1-(1-c)u)^n u^j du.

These are rational polynomials. Define

    V=a f(2,0,l)+f(2,0,q),
    M=-a^2 f(2,1,l)+f(2,1,q),
    E=a^3 f(2,2,l)+f(2,2,q),
    N4=a f(4,0,l)+f(4,0,q).

For the LEFT affine piece, put

    Dnum=a V+(1-l)M,
    Hnum=V N4-Dnum f(3,0,l),
    Z1num=-V a^2 f(2,1,l)-M a f(2,0,l),
    Z2num=V^2 a^3 f(1,2,l)+2MV a^2 f(1,1,l)+M^2 a f(1,0,l),
    Rnum=(9/4)a V^2(VE-M^2)-Dnum Z2num,
    Detnum=a Rnum Hnum-Dnum^2 Z1num^2.

The exact correspondences are

    D0=Dnum/(aV), H=Hnum/V,
    Pz1=Z1num/V, Pz2=Z2num/V^2,
    R0=Rnum/(aV^3),
    H R0-D0^2 Pz1^2=Detnum/(a^2 V^4).

All denominators are strictly positive. Reflection and affine rescaling give the same result for the right piece; the three charts cover every reflected profile too.

For the left and right caps the remaining positive-denominator gap numerators are

    Lt=(3/2)V N4-(aV+M)l^4,
    Rt=(3/2)V N4-(V-M)q^4,
    Ln=(3/2)V^2(VE-M^2)-(aV+M)^3 l^2,
    Rn=(3/2)V^2(VE-M^2)-(V-M)^3 q^2.

For example the left-cap tangential generalized ratio is(a+mu)l^4/N4, while its radial ratio is(a+mu)^3 l^2/S. The four expressions above are exactly the3/2 gaps after positive denominators are cleared.

The complete executable below constructs Hnum,Rnum,Detnum,Lt,Rt,Ln,Rn as EXACT rational polynomials and proves each nonnegative on all THREE charts. For each nonnegative power of a it expands the coefficient polynomial in the tensor Bernstein basis on the two unit-interval parameters. Every Bernstein basis function and every power a^j is nonnegative. The monotone-right substitution is multiplied by a^degree_q, a strictly positive factor, before polynomial construction. Thus this is an exact finite GLOBAL sign certificate, not a sample, numerical optimizer, interval mesh or independent-moment relaxation.

There are21 chart-polynomial certificates, containing12896 rational Bernstein controls:7236 are zero and5660 are strictly positive; NONE is negative. Every literal coefficient, the exact polynomial monomials, degrees and basis order are regenerated in the report. The conversion formula for a power coefficient c_ij into the Bernstein control at(k,m), with chosen degrees(nl,nq), is

    sum_{i<=k,j<=m} c_ij binom(k,i)/binom(nl,i) binom(m,j)/binom(nq,j).

It is implemented with fractions.Fraction, with no floating point. This establishes(SC) and both caps on the complete three-chart domain. Arbitrary-base generality follows from Section2, not the seven finite body controls.

## 5. Actual geometric controls and evidence level
The source generates seven actual uniformly filled polytopes. It checks their genuine maximal support facets, all true edges and Euler incidence, independent oriented-volume moments, the analytic centroid/covariance formula, and every whole-facet3/2 matrix gap by all principal minors. Native Euclidean equilibrium packets are computed with the same actual centre and identity metric; these controls are NOT110:

    square bipyramid,a2,l0,q0: V/E/F6/12/8, own S8 U6 H12, physicalweak000;
    square bulged frusta,a1,l1/2,q1/3:12/20/10, own S10 U12 H20, weak000;
    pentagon one apex,a3/2,l0,q2/3:11/20/11, own S9 U7 H14, weak000;
    square monotone left,a2,l3/2,q1/4:12/20/10, own S6 U12 H16, weak000;
    triangle monotone right,a1/2,l1/3,q5/3:9/15/8, own S7 U5 H10, weak000;
    square affine merge,a2,l5/2,q1/4:8/12/6, own S6 U8 H12, weak000;
    square prism merge,a2,l1,q1:8/12/6, own S6 U8 H12, weak000.

The last two delete the spurious middle ring and use the true whole lateral facets. The raw square is(-1,-1),(1,-1),(1,1),(-1,1); pentagon(0,0),(3,0),(4,1),(2,3),(-1,2); triangle(0,0),(3,0),(1,2). Each is translated by its computed ACTUAL area centroid. All literal coordinates, face cycles, edge primitives and full matrices are generated in the report. No Euclidean census is transported through a nonorthogonal affine image.

Normal and fresh source-only executions actually completed with BYTE-IDENTICAL reports and logs. This is an exact computer-assisted polynomial-sign proof plus the analytical full-matrix reduction, not proof-assistant formalization or an independent replay of the imported uniform-planar theorem.

## 6. Complete recovery, with the exact already-durable dependency
Required files:

    two_piece_profiles.py,8497B,
    SHA256 2fbb7e19247c2a120529709bb7eacd59904c3c15a85fccd46c5c35d1492b9ae5;
    frustum_all_facets.py,11727B,
    SHA256 e5c94f2463f8c4c0b4e752edf56f64123bc8a01f1000a6f98a18016a4a85a92b.

The first file is reproduced completely below. The second is reproduced completely in [internal-source-reference], which MUST be supplied to a computational successor together with this material. It supplies only exact polytope/polygon integration helpers and the prior control machinery. No inaccessible sandbox, omitted helper, data file, seed, precision rule or patch is needed. The dependency hash and byte count are checked by the program.

CPython3.13.5, SymPy1.14.0, assertions enabled. Reconstruction and verification:

    python -B two_piece_profiles.py > two_piece_profiles.log

Outputs:

    two_piece_profiles_report.json,738264B,
    SHA256 c43568b43891606abfa43124d95c12465aaf9cfe2614bd57de34710764302bef;
    two_piece_profiles.log,637B,
    SHA256 cba0d3663333f9632953ce6477d6441849f16be779ccf931137730ca4ac3f4c6.

Expected first marker:

    EXACT_ALL_THREE_PROFILE_CHARTS_PASS 21 12896 7236

Expected final marker:

    ALL_TWO_PIECE_HOMOTHETIC_PROFILE_WHOLE_FACETS_PASS

Save the following complete source with LF and one final newline.

```python
"""Every whole facet of a homogeneous two-piece homothetic-profile body.
CPython3.13.5/SymPy1.14.0; assertions on. Exact dependency:
frustum_all_facets.py, SHA e5c94f2463f8c4c0b4e752edf56f64123bc8a01f1000a6f98a18016a4a85a92b.
All coefficient tests below are exact global certificates, not samples.
Actual controls use every true maximal facet, merging a spurious middle ring.
"""
from pathlib import Path
from fractions import Fraction
import hashlib,json,math
import sympy as S
from frustum_all_facets import exact_polytope,polygon_moments,matzero
Q=S.Rational
a,l,q,u,x=S.symbols('a l q u x',real=True)
gens=(a,l,q)
def clean(z):return S.factor(S.cancel(z))
def P(z):return S.Poly(z,*gens,domain=S.QQ)
def f(n,j,c):return S.integrate((1-(1-c)*u)**n*u**j,(u,0,1)).expand()

def polynomial_system():
    V=P(a*f(2,0,l)+f(2,0,q));M=P(-a*a*f(2,1,l)+f(2,1,q))
    E=P(a**3*f(2,2,l)+f(2,2,q));N4=P(a*f(4,0,l)+f(4,0,q))
    D=P(a)*V+P(1-l)*M
    H=V*N4-D*P(f(3,0,l))
    Z2=V**2*P(a**3*f(1,2,l))+M*V*P(2*a*a*f(1,1,l))+M**2*P(a*f(1,0,l))
    Z1=V*P(-a*a*f(2,1,l))+M*P(-a*f(2,0,l))
    radial=P(Q(9,4)*a)*V**2*(V*E-M*M)-D*Z2
    determinant=P(a)*radial*H-D**2*Z1**2
    left_t=P(Q(3,2))*V*N4-(P(a)*V+M)*P(l**4)
    right_t=P(Q(3,2))*V*N4-(V-M)*P(q**4)
    left_n=P(Q(3,2))*V**2*(V*E-M*M)-(P(a)*V+M)**3*P(l*l)
    right_n=P(Q(3,2))*V**2*(V*E-M*M)-(V-M)**3*P(q*q)
    return dict(V=V,M=M,E=E,N4=N4,Dnum=D,H=H,Z1num=Z1,Z2num=Z2,
                certificates=dict(H=H,radial=radial,determinant=determinant,
                                  left_tangent=left_t,right_tangent=right_t,
                                  left_normal=left_n,right_normal=right_n))

def bernstein_certificate(poly):
    dd={idx:Fraction(c) for idx,c in poly.terms()};blocks=[];count=zeros=0;minimum=None
    for ia in range(poly.degree_list()[0]+1):
        values={(i,j):c for (aa,i,j),c in dd.items() if aa==ia}
        if not values:continue
        nl=max(i for i,j in values);nq=max(j for i,j in values);controls=[]
        for il in range(nl+1):
            row=[]
            for iq in range(nq+1):
                val=sum(c*Fraction(math.comb(il,i),math.comb(nl,i))*Fraction(math.comb(iq,j),math.comb(nq,j))
                        for (i,j),c in values.items() if i<=il and j<=iq)
                assert val>=0,(ia,il,iq,val)
                row.append(str(val));count+=1;zeros+=val==0
                minimum=val if minimum is None else min(minimum,val)
            controls.append(row)
        blocks.append(dict(positive_power=ia,unit_square_degrees=[nl,nq],controls=controls))
    return dict(degrees=poly.degree_list(),monomials=len(dd),control_count=count,
                zero_count=zeros,negative_count=0,minimum=str(minimum),blocks=blocks)

def certificates(system):
    cert={}
    for name,poly in system['certificates'].items():
        cert[name+'_central_maximum']=bernstein_certificate(poly)
        # Concave monotone-left chart: l=1+a(1-q)x; a>0,q,x in[0,1].
        bigleft=S.Poly(S.expand(poly.as_expr().subs(l,1+a*(1-q)*x)),a,q,x,domain=S.QQ)
        cert[name+'_monotone_left']=bernstein_certificate(bigleft)
        # Concave monotone-right chart; multiplying by a^degree_q is positive.
        degreeq=poly.degree(q)
        bigright=S.Poly(S.expand(a**degreeq*poly.as_expr().subs(q,1+(1-l)*x/a)),a,l,x,domain=S.QQ)
        cc=bernstein_certificate(bigright);cc['cleared_positive_a_power']=degreeq
        cert[name+'_monotone_right']=cc
    return cert

def profile_polytope(base,aa,ll,qq):
    assert aa>0 and ll>=0 and qq>=0 and (1-ll)/aa>=qq-1
    levels=[(-aa,ll),(0,S.S.One),(1,qq)]
    merged=(1-ll)/aa==qq-1
    if merged:levels.pop(1)
    vertices=[];rings=[]
    for z,h in levels:
        if h==0:
            rings.append([len(vertices)]);vertices.append(S.Matrix((0,0,z)))
        else:
            ring=[]
            for v in base:
                ring.append(len(vertices));vertices.append(S.Matrix((h*v[0],h*v[1],z)))
            rings.append(ring)
    faces=[];n=len(base)
    for ring in (rings[0],rings[-1]):
        if len(ring)>1:faces.append(tuple(ring))
    for low,high in zip(rings,rings[1:]):
        for j in range(n):
            jj=(j+1)%n
            if len(low)==1:face=(low[0],high[j],high[jj])
            elif len(high)==1:face=(low[j],low[jj],high[0])
            else:face=(low[j],low[jj],high[jj],high[j])
            faces.append(face)
    return exact_polytope(vertices,faces),merged

def actual_controls(system):
    raw_square=[S.Matrix(p) for p in [(-1,-1),(1,-1),(1,1),(-1,1)]]
    raw_pentagon=[S.Matrix(p) for p in [(0,0),(3,0),(4,1),(2,3),(-1,2)]]
    raw_triangle=[S.Matrix(p) for p in [(0,0),(3,0),(1,2)]]
    cases=[('square_bipyramid',raw_square,Q(2),Q(0),Q(0)),
           ('square_bulged_frusta',raw_square,Q(1),Q(1,2),Q(1,3)),
           ('pentagon_one_apex',raw_pentagon,Q(3,2),Q(0),Q(2,3)),
           ('square_monotone_left',raw_square,Q(2),Q(3,2),Q(1,4)),
           ('triangle_monotone_right',raw_triangle,Q(1,2),Q(1,3),Q(5,3)),
           ('square_affine_merge',raw_square,Q(2),Q(5,2),Q(1,4)),
           ('square_prism_merge',raw_square,Q(2),Q(1),Q(1))]
    out=[]
    for name,raw,aa,ll,qq in cases:
        area,bg,bc=polygon_moments(raw);base=[z-bg for z in raw]
        body,merged=profile_polytope(base,aa,ll,qq);values={a:aa,l:ll,q:qq}
        V=system['V'].as_expr().subs(values);M=system['M'].as_expr().subs(values)
        E=system['E'].as_expr().subs(values);N4=system['N4'].as_expr().subs(values)
        mu=clean(M/V);var=clean(E/V-mu*mu)
        assert body['volume']==area*V
        matzero(body['centroid']-S.Matrix((0,0,mu)))
        cv=S.zeros(3);cv[:2,:2]=N4/V*bc;cv[2,2]=var;matzero(body['Sigma']-cv)
        for facet in body['facet_moments']:
            gap=(Q(3,2)*cv-facet['alpha']*facet['T']).applyfunc(clean)
            for k in (1,2,3):
                for inds in __import__('itertools').combinations(range(3),k):assert gap.extract(inds,inds).det()>=0
            facet['three_halves_gap']=gap
        out.append(dict(name=name,raw_base=raw,parameters=(aa,ll,qq),base_centroid=bg,
                        base_covariance=bc,removed_spurious_middle_ring=merged,actual_polytope=body))
    return out

def encode(obj):
    if isinstance(obj,S.MatrixBase):return [[encode(z) for z in row] for row in obj.tolist()]
    if isinstance(obj,S.Poly):return dict(generators=[str(z) for z in obj.gens],terms=[(p,str(c)) for p,c in obj.terms()])
    if isinstance(obj,S.Basic):return str(obj)
    if isinstance(obj,dict):return {str(k):encode(v) for k,v in obj.items()}
    if isinstance(obj,(tuple,list)):return [encode(z) for z in obj]
    return obj

def main():
    assert __debug__ and S.__version__=='1.14.0'
    dependency=Path(__file__).with_name('frustum_all_facets.py').read_bytes()
    assert len(dependency)==11727
    assert hashlib.sha256(dependency).hexdigest()=='e5c94f2463f8c4c0b4e752edf56f64123bc8a01f1000a6f98a18016a4a85a92b'
    system=polynomial_system();cert=certificates(system);controls=actual_controls(system)
    total=sum(c['control_count'] for c in cert.values());zeros=sum(c['zero_count'] for c in cert.values())
    report=dict(identity='ALL_TWO_PIECE_CONCAVE_HOMOTHETIC_PROFILES_WHOLE_FACET_THREE_HALVES_V1',
                theorem_scope='Every whole facet, arbitrary actual convex planar base, every nonnegative concave two-affine-piece profile and affine images. No arbitrary-profile or equilibrium theorem.',
                uniform_planar_source='[internal-source-reference]',polynomial_system=system,
                exact_positive_certificates=cert,total_bernstein_controls=total,zero_controls=zeros,
                actual_controls=controls,
                degenerate_affine_case='Coplanar lateral pieces MUST merge. Use the sharp all-frustum theorem, or uniform-prism theorem; never sum half-facet estimates.')
    data=(json.dumps(encode(report),sort_keys=True,indent=2)+'\n').encode()
    Path('two_piece_profiles_report.json').write_bytes(data)
    print('EXACT_ALL_THREE_PROFILE_CHARTS_PASS',len(cert),total,zeros)
    for cc in controls:
        body=cc['actual_polytope'];own=body['own_euclidean']
        print('ACTUAL',cc['name'],'VEF',len(body['vertices']),len(body['edges']),len(body['faces']),
              'OWN',len(own['S']),len(own['U']),len(own['H']),'WEAK_PACKETS',len(own['physical_weak_edge_packets']))
    print('REPORT',len(data),hashlib.sha256(data).hexdigest())
    print('ALL_TWO_PIECE_HOMOTHETIC_PROFILE_WHOLE_FACETS_PASS')
if __name__=='__main__':main()
```
