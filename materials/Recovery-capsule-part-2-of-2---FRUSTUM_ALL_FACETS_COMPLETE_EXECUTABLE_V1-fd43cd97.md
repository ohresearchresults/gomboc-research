# material-fd43cd9771d2

Historical AI scientific source/proof material. Statements retain their original scope; this is not an independently reviewed theorem.

Public derivative: internal-record-identifiers-replaced.

---

# Recovery capsule part 2 of 2: complete executed source

Object: ALL_HOMOTHETIC_FRUSTA_WHOLE_FACET_SHARP_CONSTANT_V1.
The analytical proof, exact accepted planar dependency and scope are in Recovery capsule part1, [internal-source-reference]. This file contains the complete standalone executable; no previous sandbox or data file is a dependency.

Save the following code with LF and one final newline as frustum_all_facets.py,11727B, SHA256 e5c94f2463f8c4c0b4e752edf56f64123bc8a01f1000a6f98a18016a4a85a92b. CPython3.13.5, SymPy1.14.0, assertions enabled. Run python -B frustum_all_facets.py > frustum_all_facets.log. Expected report68684B SHA784340feb962f4c06b48776c225a37c8da15c2bde586fbb82372bd702ddb1d12; log367B SHAe71fba3aad07059cea2ed2989a25cf727589ef9130ce3eb017584191644f4df6. Normal and fresh source-only runs actually completed with identical bytes. Terminal marker FRUSTUM_ALL_FACETS_SHARP_KAPPA_AND_NODAL_TRIM_PASS.

```python
"""Sharp whole-facet moments of every homothetic frustum; exact controls.
CPython 3.13.5, SymPy 1.14.0; assertions enabled; no external inputs.
The arbitrary-base theorem uses the accepted uniform-planar 3/2 theorem.
This code verifies the scalar reduction and actual rational polytope moments,
not an enumeration of all convex bodies or all equilibrium realizations.
"""
from pathlib import Path
import hashlib, json
import sympy as S
Q=S.Rational
r=S.symbols('r', real=True)

def clean(x): return S.factor(S.cancel(x))
def zero(x): assert clean(x)==0, clean(x)
def matzero(x): assert x.applyfunc(clean)==S.zeros(*x.shape), x

def positive_coefficients(expr):
    p=S.Poly(S.expand(expr),r)
    assert all(c>=0 for c in p.all_coeffs()) and p.nth(0)>0
    return dict(degree=p.degree(),ascending=[p.nth(i) for i in range(p.degree()+1)])

def scalar_theorem():
    A={k:(1-r**(k+1))/S.Integer(k+1) for k in range(1,5)}
    mu=clean(A[3]/A[2]); var=clean(A[4]/A[2]-mu*mu)
    K=clean(A[3]**2/(A[2]*A[4])); cap=clean(Q(3,2)*K)
    radial=clean(A[3]**2*(A[1]*A[3]-A[2]**2)/(A[2]**2*(A[2]*A[4]-A[3]**2)))
    top_n=clean((1-mu)**3/(A[2]*var))
    bottom_n=clean((mu-r)**3*r*r/(A[2]*var))
    top_t=clean((1-mu)/A[4]); bottom_t=clean((mu-r)*r**4/A[4])
    U=1+r+r*r; W=1+r+r*r+r**3+r**4
    P=1+4*r+10*r*r+4*r**3+r**4
    zero(cap-45*(r+1)**2*(r*r+1)**2/(32*U*W))
    zero(Q(3,2)-cap-3*(r-1)**2*P/(32*U*W))
    zero(cap-Q(45,32)-45*r**3/(32*U*W))
    derivative=clean(S.diff(cap,r))
    zero(derivative-45*r*r*(1-r)*(1+r)*(1+r*r)*(3*r*r+4*r+3)/(32*U**2*W**2))
    zero(radial-Q(15,8)+15*r*r*(9*r**4+20*r**3+26*r*r+20*r+9)/(8*U**2*P))
    certificates={}
    for name,expr,factor in [
        ('cap_minus_top_normal',cap-top_n,(1-r)**2),
        ('cap_minus_bottom_normal',cap-bottom_n,(1-r)**2),
        ('cap_minus_top_tangent',cap-top_t,S.S.One),
        ('cap_minus_bottom_tangent',cap-bottom_t,S.S.One),
        ('radial_below_15_8',Q(15,8)-radial,r*r),
    ]:
        nn,dd=S.fraction(clean(expr/factor))
        certificates[name]=dict(numerator=positive_coefficients(nn),denominator=positive_coefficients(dd),removed_factor=factor)
    assert cap.subs(r,0)==Q(45,32) and S.limit(cap,r,1,dir='-')==Q(3,2)
    # The maximum lateral radial block is (2/3)*radial<=5/4<45/32<=cap.
    assert Q(2,3)*Q(15,8)==Q(5,4)<Q(45,32)
    return dict(A=A,mean_radial=mu,variance_radial=var,transport_factor=K,
                sharp_all_facet_constant=cap,radial_factor=radial,
                top_normal=top_n,bottom_normal=bottom_n,top_tangent=top_t,bottom_tangent=bottom_t,
                positive_certificates=certificates,derivative=derivative,
                sharp_gap=clean(Q(3,2)-cap),pyramid_constant=Q(45,32))

def polygon_moments(points):
    area=S.S.Zero; first=S.zeros(2,1); second=S.zeros(2)
    for a,b in zip(points,points[1:]+points[:1]):
        det=S.det(S.Matrix.hstack(a,b)); area+=det/2
        first+=det*(a+b)/6
        ss=a+b; second+=det*(ss*ss.T+a*a.T+b*b.T)/24
    assert area>0
    g=(first/area).applyfunc(clean)
    cov=(second/area-g*g.T).applyfunc(clean)
    assert cov.det()>0
    return area,g,cov

def make_frustum(base,s):
    n=len(base)
    if s==0:
        vertices=[S.Matrix([0,0,0])]+[S.Matrix([p[0],p[1],1]) for p in base]
        faces=[tuple(range(1,n+1))]+[(0,1+j,1+(j+1)%n) for j in range(n)]
    else:
        vertices=[S.Matrix([s*p[0],s*p[1],s]) for p in base]+[S.Matrix([p[0],p[1],1]) for p in base]
        faces=[tuple(range(n)),tuple(range(n,2*n))]+[(j,(j+1)%n,(j+1)%n+n,j+n) for j in range(n)]
    return vertices,faces

def exact_polytope(vertices,cycles):
    interior=sum(vertices,S.zeros(3,1))/len(vertices)  # orientation point ONLY, not mass centroid
    faces=[]
    for old in cycles:
        f=list(old); a,b,c=[vertices[i] for i in f[:3]]; n=(b-a).cross(c-a)
        assert n.dot(n)>0
        if n.dot(a-interior)<0: f.reverse()
        a,b,c=[vertices[i] for i in f[:3]]; n=(b-a).cross(c-a)
        assert n.dot(a-interior)>0
        for j,v in enumerate(vertices):
            h=clean(n.dot(v-a))
            assert h==0 if j in f else h<0
        faces.append(tuple(f))
    edges=sorted({tuple(sorted((a,b))) for f in faces for a,b in zip(f,f[1:]+f[:1])})
    assert len(vertices)-len(edges)+len(faces)==2
    incidence={e:[j for j,f in enumerate(faces) if e in [tuple(sorted(ab)) for ab in zip(f,f[1:]+f[:1])]] for e in edges}
    assert all(len(v)==2 for v in incidence.values())
    V=S.S.Zero; first=S.zeros(3,1); second=S.zeros(3)
    for f in faces:
        a=vertices[f[0]]
        for k in range(1,len(f)-1):
            b,c=vertices[f[k]],vertices[f[k+1]]; D=S.det(S.Matrix.hstack(a,b,c)); v=a+b+c
            V+=D/6; first+=D*v/24
            second+=D*(v*v.T+a*a.T+b*b.T+c*c.T)/120
    V=clean(V); assert V>0
    g=(first/V).applyfunc(clean); cov=(second/V-g*g.T).applyfunc(clean)
    assert all(cov[:k,:k].det()>0 for k in (1,2,3))
    data=[]
    for f in faces:
        a,b,c=[vertices[i] for i in f[:3]]; n=(b-a).cross(c-a)
        h=clean(n.dot(a-g)); assert h>0
        mass=S.S.Zero; moment1=S.zeros(3,1); moment2=S.zeros(3)
        for k in range(1,len(f)-1):
            b,c=vertices[f[k]],vertices[f[k+1]]
            w=clean(n.dot((b-a).cross(c-a))); assert w>0
            v=a+b+c; mass+=w; moment1+=w*v/3
            moment2+=w*(v*v.T+a*a.T+b*b.T+c*c.T)/12
        cf=(moment1/mass-g).applyfunc(clean)
        T=(moment2/mass-(moment1/mass)*g.T-g*(moment1/mass).T+g*g.T).applyfunc(clean)
        alpha=clean(h*mass/(2*n.dot(n)*V)); pole=(n/h).applyfunc(clean)
        matzero(T*pole-cf)
        data.append(dict(vertices=f,alpha=alpha,c=cf,T=T,pole=pole))
    centered=[v-g for v in vertices]; poles=[f['pole'] for f in data]
    stable=[i for i,a in enumerate(poles) if all(a.dot(b)-a.dot(a)<0 for j,b in enumerate(poles) if j!=i)]
    unstable=[i for i,a in enumerate(centered) if all(a.dot(centered[j]-a)<0 for e in edges if i in e for j in e if j!=i)]
    saddles=[]; weak=[]; prim=[]
    for e in edges:
        i,j=e; k,l=incidence[e]; a,b=centered[i],centered[j]; c,d=poles[k],poles[l]
        values=[clean(a.dot(b)-a.dot(a)),clean(a.dot(b)-b.dot(b)),clean(c.dot(d)-c.dot(c)),clean(c.dot(d)-d.dot(d))]
        if all(x<0 for x in values): saddles.append(e)
        if all(x<=0 for x in values) and any(x==0 for x in values): weak.append(e)
        prim.append(dict(edge=e,faces=(k,l),values=values))
    if not weak: assert len(stable)+len(unstable)-len(saddles)==2
    return dict(vertices=vertices,faces=faces,edges=edges,volume=V,centroid=g,Sigma=cov,facet_moments=data,
                own_euclidean=dict(S=stable,U=unstable,H=saddles,physical_weak_edge_packets=weak),
                all_edge_primitives=prim)

def controls(theorem):
    records=[]
    shapes=[('square',[S.Matrix(p) for p in [(-1,-1),(1,-1),(1,1),(-1,1)]]),
            ('asymmetric_pentagon',[S.Matrix(p) for p in [(0,0),(3,0),(4,1),(2,3),(-1,2)]])]
    for name,raw in shapes:
        area,bg,bc=polygon_moments(raw);base=[p-bg for p in raw]
        for s in (S.S.Zero,Q(1,2)):
            vertices,faces=make_frustum(base,s);P=exact_polytope(vertices,faces)
            mu=clean(theorem['mean_radial'].subs(r,s)); vv=clean(theorem['variance_radial'].subs(r,s))
            A=theorem['A']; varx=clean((A[4]/A[2]).subs(r,s))
            expected=S.zeros(3);expected[:2,:2]=varx*bc;expected[2,2]=vv
            assert P['volume']==area*A[2].subs(r,s)
            matzero(P['centroid']-S.Matrix([0,0,mu]));matzero(P['Sigma']-expected)
            C=theorem['sharp_all_facet_constant'].subs(r,s); strict=0; singular=0
            for F in P['facet_moments']:
                gap=(C*P['Sigma']-F['alpha']*F['T']).applyfunc(clean)
                for k in (1,2,3):
                    for inds in __import__('itertools').combinations(range(3),k): assert gap.extract(inds,inds).det()>=0
                if gap.det()>0:strict+=1
                else:singular+=1
                F['sharp_gap']=gap
            if name=='square':
                assert singular==4
                # A lateral normal in the base, transported radially, realizes the sharp ratio.
                side=P['facet_moments'][1 if s==0 else 2]
                point=vertices[side['vertices'][0]]
                # The first native side has y=-r, so its distinguished centred test is y.
                v=S.Matrix([0,1,0]); quotient=clean(side['alpha']*(v.T*side['T']*v)[0]/(v.T*P['Sigma']*v)[0])
                assert quotient==C
                P['attaining_test']=v;P['attaining_ratio']=quotient
            assert len(P['own_euclidean']['S'])>=2
            records.append(dict(base_name=name,raw_base=raw,base_area=area,base_centroid=bg,base_covariance=bc,
                                cut_fraction=s,sharp_constant=C,strict_facets=strict,singular_facets=singular,polytope=P))
    return records

def nodal_exact_family(theorem):
    # Affine image of the square frustum: (r,x,z)->(t=(r+x)/2,y=1+2x,z).
    # In (t,y), K is the triangle A(0,-1),B(0,1),C(1,3), trimmed by
    # ell=1-y+4t>=2s. Uniform lift has 2|z|<=ell.
    t,y,s=S.symbols('t y s', real=True);ell=1-y+4*t
    def moment(expr):
        return clean(S.integrate(S.integrate(expr,(y,4*t-1,1+4*t-2*s)),(t,0,s))+
                     S.integrate(S.integrate(expr,(y,4*t-1,1+2*t)),(t,s,1)))
    V=moment(ell);J=moment(t*ell);M=moment(y*ell);I=moment((y-1)**2*ell)
    assert clean(M/V)==1
    B2=clean(S.integrate((1-y)*(y-1)**2,(y,-1,1-2*s)))
    R=clean(J*B2/(V*I));C=theorem['sharp_all_facet_constant'].subs(r,s)
    zero(R-C);zero(R-Q(45,32)-45*s**3/(32*(s*s+s+1)*(s**4+s**3+s*s+s+1)))
    gain=clean(R-R.subs(s,0));assert S.limit(gain/s**3,s,0)==Q(45,32)
    assert S.limit((S.log(R)-S.log(R.subs(s,0)))/s**3,s,0)==1
    return dict(description='Actual nodal-apex trim, entire 0<=s<1; Y=y-1 has zero at original marked apex.',
                volume=V,first_normal=J,mean_y=1,central_test_moment=I,whole_marked_B2=B2,R=R,gain=gain,
                removed_volume=clean(V.subs(s,0)-V),leading_log_gain_order=3,leading_log_gain_coefficient=1,
                affine_map='(r,x,z)->((r+x)/2,1+2*x,z)',
                raw_planar_triangle=[(0,-1),(0,1),(1,3)],density=ell,cut='ell>=2*s')

def encode(x):
    if isinstance(x,S.MatrixBase): return [[encode(v) for v in row] for row in x.tolist()]
    if isinstance(x,S.Basic): return str(x)
    if isinstance(x,dict):return {str(k):encode(v) for k,v in x.items()}
    if isinstance(x,(list,tuple)):return [encode(v) for v in x]
    return x

def main():
    assert __debug__ and S.__version__=='1.14.0'
    theorem=scalar_theorem();cc=controls(theorem)
    report=dict(identity='ALL_HOMOTHETIC_FRUSTA_WHOLE_FACET_SHARP_CONSTANT_V1',
                accepted_planar_source='[internal-source-reference]',
                accepted_planar_sha256='240b58ed6bde2703c5788573c8c20ca2a4278a3abc1cfc66fb8f607645eb646d',
                scalar_theorem=theorem,actual_controls=cc,nodal_trim=nodal_exact_family(theorem),
                scope='Every whole facet of every actual homogeneous homothetic frustum over any convex planar base; affine invariant. Not all convex bodies or an equilibrium exclusion.')
    raw=(json.dumps(encode(report),sort_keys=True,indent=2)+'\n').encode()
    Path('frustum_all_facets_report.json').write_bytes(raw)
    for c in cc:
        p=c['polytope'];own=p['own_euclidean']
        print('ACTUAL',c['base_name'],c['cut_fraction'],'VEF',len(p['vertices']),len(p['edges']),len(p['faces']),
              'OWN',len(own['S']),len(own['U']),len(own['H']),'WEAK_PACKETS',len(own['physical_weak_edge_packets']))
    print('REPORT',len(raw),hashlib.sha256(raw).hexdigest())
    print('FRUSTUM_ALL_FACETS_SHARP_KAPPA_AND_NODAL_TRIM_PASS')
if __name__=='__main__':main()
```
