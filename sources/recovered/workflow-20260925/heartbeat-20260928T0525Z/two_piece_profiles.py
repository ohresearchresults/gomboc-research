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
                uniform_planar_source='att_d5545c8115fbde24bc6e_01',polynomial_system=system,
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
