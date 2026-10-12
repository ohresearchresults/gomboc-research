# material-04208701b395

AI research material · [Export notes](../catalog/coverage.md#text-records)

<!-- historical-status:start -->
> **Historical AI material.** The title and claims below reflect the AI’s assessment at the time. Claims of proof, certification or completion are not a current verification verdict.
>
> [C622](../C622/README.md) passes the supplied exact checks; C<500 remains open; Minimum’s C≥34 remains a working lower bound requiring a consolidated proof. See [verification status and source gaps](../catalog/coverage.md).
<!-- historical-status:end -->

---

# TWO_ANCHOR_PROJECTED_MASS_OBSTRUCTION_V1

## Status and scope
This is a new actual-geometric necessary condition for a joint local maximum of the adjacent-triangle trace. It is not a proof of the universal 51/25 trace bound, not a lower exclusion of the entire 10/17/9 layer, and not a new mono-monostatic construction. The accepted complexity interval remains 34 <= C_min <= 622. In particular the symbol T below is a trace, not C=2E.

The theorem explains why the previously surviving FORMAL 51/25 datum cannot be an actual joint maximum: an actual projected region would need a negative integral of a strictly positive function. This excludes every covariance and every root-mass completion of that datum, not just its previously chosen Sigma=Q*.

Exact prior proof dependencies, read completely by this coordinator:
* POLYHEDRAL_TRACE_STATIONARITY_RIGIDITY_V1, [internal-source-reference], SHA8dc6ce8812298f59a61b404ccba7c09fef867bb8844a8952bf1cacc638bcc2b9. Its finite cap/spike/whole-facet arguments imply positive G at all auxiliary vertices and max_F G+3 mean_F G<=0 on unprotected facets. The present argument uses these analytic statements, not its obsolete coarse vertex bound.
* Joint-root identities and canonical-fixing projectivity, [internal-source-reference], SHA73eb04d63deeab693d29533819d3b95c4e1af3cc01d756987381aaa2bb4c2ed8.
* Actual Berwald/fan formal-data proof, [internal-source-reference], SHAb1d05ed4c84512cf48852d5383ffcc3ff2a066c1b7f6b5777fe62d372c0cb559. This supplies the previous formal datum and rho0 lower bound, not a realized body.
No external research or numerical optimizer is a proof dependency.

## 1. Common notation and the two-anchor sector
A=(0,0,0), B=(0,0,1), C=(0,1,0), D=(1,0,0), T0=conv(A,B,C,D). Let P be a bounded convex three-polytope containing T0 and lying in x>=0,y>=0,ell>=0, with a positive-area root facet F={ell=0} intersect P. Coordinate faces may be larger support patches.

Put a>b>0, c,d>0, alpha=a-b,

ell=a+(d-a)x+(c-a)y-alpha z,
n=h_c x+h_d y, h_c=a+b+c, h_d=a+b+d.

All integrals are over the original uniformly filled actual body:
V=int_P1, E=int_Pell, N=int_Pn, t=6V, g=(u,v,z), p=u+v,
r=N/V=n(g), mu=E/V=ell(g), q=N/E=Tt, T=N/(6VE), m=3p/t,
G=n-r-qell, w=(v/(3p),u/(3p),1/3).

At a joint local maximum, the body and affine root may both vary in the full marked support-patch class; all four endpoint values remain positive. In particular this is not stationarity inside a fixed combinatorial realization stratum.

Assume G(C)>=0 and G(D)>=0. Then G(A)=-r-qa<0, G(B)=-r-qb<0. Every auxiliary true vertex has G>0. If an unprotected facet contained neither A nor B, G would be nonnegative at every vertex and positive somewhere, contradicting max_F G+3 mean_F G<=0. Thus EVERY facet other than x=0,y=0,ell=0 contains A or B.

There are no other vertical facets: a vertical plane containing one of A,B contains both, whereas the true edge AB already belongs to the two coordinate faces. The endpoints of the axial edge must indeed be A and B: an endpoint extending beyond either would be an auxiliary vertex with n=0 and G=-r-qell<0, which is impossible. Every upper nonroot facet contains B and not A; its plane has the form z+L(x,y)=1. Every lower facet contains A and not B; its plane has the form -z+L(x,y)=0. The root is an upper face with equation z=H-L0(x,y), H=a/alpha>1. These are actual facet statements, including when C,D are redundant marks. No assertion that all off-root vertices are A,B,C,D is needed.

## 2. Exact projected moment identity
Let K be the orthogonal xy projection of P and R the xy projection of F. Both are genuine compact convex planar sets, R subset K; Delta=conv((0,0),(1,0),(0,1)) subset K. Let A_K, A_R denote their areas. Up to measure-zero seams, the upper nonroot faces project to K minus R. A lower face can have nonzero projected area, but its support intercept at A is zero.

For EVERY homogeneous polynomial f(x,y) of degree j>=0,

(j+3) int_P f = int_K f + (b/alpha) int_R f.                 (1)

Proof: div[(x,y,z)f]=(j+3)f. Apply the divergence theorem. The lower and coordinate faces have support intercept zero. On upper B-faces, (x,y,z).nu dA equals dxdy; on the root it equals H dxdy. Integrating their actual projected partition gives (1). This uses a genuine filled body; no independent surface weights or density change occurs. The formula also follows from signed boundary tetrahedron integration when A is on the boundary.

In particular,
A_K=3V-(b/alpha)A_R,
int_K n=4N-(b/alpha)int_R n,
int_K n^2=5 int_P n^2-(b/alpha)int_R n^2.                  (2)

If rho=mu Area(F)/(3V |grad ell|), then A_R=3V alpha rho/mu. Since A_K>=Area(Delta)=1/2,

rho <= mu(t-1)/(bt).                                      (3)

This applies to the entire two-anchor facet class, without requiring the additional first-variation identities below.

## 3. An actual mandatory negative core and a positive remainder
On R the body function G equals n-r and is strictly positive. Moreover
G(C)=h_d-r-qc>=0, G(D)=h_c-r-qd>=0,
so r<min(h_c,h_d). Therefore the FULL triangle

L={(x,y):x,y>=0, h_c x+h_d y<=r}

lies in Delta, hence in K, and is disjoint from R up to null boundaries. It is exactly the nonpositive part of G=n-r in the quadrant. Put Omega=K minus (L union R). G is nonnegative on Omega.

The three exact moments of the compulsory negative core are

int_L1=r^2/(2h_c h_d),
int_L(n-r)=-r^3/(6h_c h_d),
int_L(n-r)^2=r^4/(12h_c h_d).                              (4)

Let W1=int_R(n-r), W2=int_R(n-r)^2 and sigma_n^2=Var_P(n). Equations(1)-(4) give actual moments of Omega:

M0=3V-(a/alpha)A_R-r^2/(2h_c h_d),
M1=rV-(a/alpha)W1+r^3/(6h_c h_d),
M2=5V sigma_n^2-(a/alpha)W2-r^4/(12h_c h_d).                (5)

Thus M0,M1,M2>=0 and M0 M2>=M1^2. In the positive-endpoint local-maximum setting these inequalities are strict: min_R(n-r)>0 and r<min(h_c,h_d) leave an open strip 0<n-r<epsilon inside Delta but outside R, so Omega has positive area and n-r is not constant there. The Hankel inequality is just Cauchy-Schwarz for THIS actual region, not freely fitted moments.

The compact projected container gives further constraints. For every point X in P, the two actual tetrahedra conv(X,A,B,C) and conv(X,A,B,D) lie in P on opposite sides of plane ABX; their volumes x/6 and y/6 imply x+y<=t. Consequently Delta subset K subset t Delta. With B0=A_K-1/2 and B1=int_K n-(h_c+h_d)/6,

B0>=0,
min(h_c,h_d) B0 <= B1 <= t max(h_c,h_d) B0.                (6)

Higher moment matrices of K minus Delta must also be positive semidefinite. For example B2=int_K n^2-(h_c^2+h_c h_d+h_d^2)/12 obeys B0 B2>=B1^2. These are necessary actual projection-completion conditions; they do not alone establish existence of K or P.

## 4. Joint root stationarity eliminates the remaining root integral
The fully read joint-root theorem gives, with original body coordinates,

W1=alpha int_F G/|grad ell|=6V^2 alpha(T-m),
W2=alpha int_F G^2/|grad ell|=6V^2 alpha m(r-n(w)).          (7)

All endpoint values must be positive for these two-sided affine-root variations. They are not licensed at a zero endpoint. Substituting(7) into the positive M1 condition yields

 t r-a t^2(T-m)+r^3/(h_c h_d)>0,

or equivalently

 T < m+r/(a t)+r^3/(a h_c h_d t^2).                        (8)

This condition does not use rho, an independently chosen covariance, or a symmetry assumption. It holds for every actual joint maximum in the G(C),G(D)>=0 sector. The M2 and Hankel conditions in(5) remain additional coupled restrictions. Neither(8) nor the displayed list has been proved sufficient or a complete universal 51/25 exclusion.

## 5. Exact exclusion of the previous formal 51/25 datum
Use the unchanged FORMAL parameters

a=1,b=2/3,c=d=1/60,t=9/5,T=51/25,
u=v=11/32,z=1937/73440.

They give r=1111/960, mu=27775/88128 and G(C)=G(D)=55781/120000>0. The earlier root-variance theorem requires
rho>=rho0=1151329/5202000.
The new actual projected area inequality(3) requires
rho<=27775/132192.
Their gap is
rho0-rho_upper=3149891/280908000>0.

Independently, the left side of(8), before division by a t^2, is

 t r-a t^2(T-m)+r^3/(h_c h_d)=-8201437/30720000<0.

The right side trace cap is 7793819/3981312, about1.9576006603, whereas T=51/25. Their difference is8201437/99532800>0. Thus this datum would assign a NEGATIVE M1=-8201437/184320000 to the actual nonnegative-G region Omega. No covariance or alternative allowed rho can repair it. It is excluded as an actual joint local maximum, not claimed to be an unrealizable list of first moments for every conceivable nonstationary body.

The rho=1/4 version separately requires A_K=117783/277750<1/2, even though K must contain Delta. These two geometric contradictions complement, rather than negate, its earlier successful relaxed moment tests.

## 6. Nonvacuous actual control and reproducibility
The complete source below reconstructs an actual uniformly filled six-vertex body with endpoints(1,1/2,1/10,1/10), true6/9/5, root in ell=0 and C,D contained in enlarged coordinate faces. It has the two-anchor facet property, positive G(C),G(D), and positive G on the root. It verifies all three degree0/1/2 projected moment identities and the actual negative-core/complement moments. It is NOT stationary: the source expressly checks failure of the joint-root W1 equation. It is not asserted to be110.

Its exact trace is9824/5593, V47/150, N614/1875, E119/1200. Root projection is the band1<=x+y<=6/5, and full projection is(6/5)Delta. The source independently reconstructs maximal facets from exact support tests and computes the original 3D mass from positive tetrahedra; 2D projected moments are computed by a separate signed polygon fan. True facet triangulations are used only for integration, not substituted for physical edges.

Recovery: save the full following source as two_anchor_projected_mass.py, UTF-8/LF with final LF. No input files, external archives, symbolic package or optimizer are required. CPython3.13.5 standard library, assertions enabled. Execute:

python -S two_anchor_projected_mass.py build
python -S two_anchor_projected_mass.py check

Both were executed by the coordinator. Expected source6994bytes SHA b442f91e1b84ce96d6027e18eac10b8cb734ceed73de334573b701f5918f3b2a. Reproduced two_anchor_projected_mass.json1829bytes SHA09c44fa2fe723be1579483f52fd4471318c448b04abc6f2d6b8d4e6e8d0f21d1. Exact terminal markers:
ACTUAL_TWO_ANCHOR_PROJECTED_MOMENT_IDENTITIES_PASS 6 9 5
ACTUAL_NEGATIVE_CORE_AND_POSITIVE_COMPLEMENT_MOMENTS_PASS
FORMAL_51_OVER_25_ALL_RHO_AND_COVARIANCE_EXCLUSION_PASS
TWO_ANCHOR_PROJECTED_MASS_RECOVERY_PASS

The analytic theorem is justified above; the executed finite audit checks the actual control and exact formal exclusion, not a symbolic formalization of all convex-body variation arguments.

## Complete exact recovery source

```python
"""TWO_ANCHOR_PROJECTED_MASS_OBSTRUCTION_V1.
Exact stdlib audit, not a global trace/minimum solver.
python -S two_anchor_projected_mass.py build|check
All actual input coordinates and all formal test parameters are literal below.
The actual six-vertex body is not asserted stationary or mono-monostatic.
"""
from fractions import Fraction as F
from itertools import combinations
from pathlib import Path
import hashlib, json, sys
assert __debug__

def add(a,b): return tuple(x+y for x,y in zip(a,b))
def sub(a,b): return tuple(x-y for x,y in zip(a,b))
def dot(a,b): return sum(x*y for x,y in zip(a,b))
def cross(a,b): return (a[1]*b[2]-a[2]*b[1],a[2]*b[0]-a[0]*b[2],a[0]*b[1]-a[1]*b[0])
def det(a,b,c): return dot(a,cross(b,c))
def hull_faces(vs):
    out=set()
    for i,j,k in combinations(range(len(vs)),3):
        n=cross(sub(vs[j],vs[i]),sub(vs[k],vs[i]))
        if n==(0,0,0): continue
        h=tuple(dot(n,sub(v,vs[i])) for v in vs)
        if min(h)>=0 or max(h)<=0: out.add(tuple(i for i,t in enumerate(h) if t==0))
    return out

def tri2(poly, n):
    # Signed origin fan; correct also when the origin is outside the polygon.
    out=[F(0)]*3
    for p,q in zip(poly,poly[1:]+poly[:1]):
        area=(p[0]*q[1]-p[1]*q[0])/2
        a=dot(n,p); b=dot(n,q)
        out[0]+=area
        out[1]+=area*(a+b)/3
        out[2]+=area*(a*a+a*b+b*b)/6
    assert out[0]>0
    return tuple(out)

def centered(m,r): return (m[0],m[1]-r*m[0],m[2]-2*r*m[1]+r*r*m[0])
def enc(x):
    if isinstance(x,F): return str(x)
    if isinstance(x,dict): return {str(k):enc(v) for k,v in x.items()}
    if isinstance(x,(list,tuple)): return [enc(v) for v in x]
    return x

def actual_control():
    a,b,c,d=F(1),F(1,2),F(1,10),F(1,10)
    alpha=a-b; H=a/alpha; hc=a+b+c; hd=a+b+d
    P=((F(0),F(0),F(0)),(F(0),F(0),F(1)),
       (F(1),F(0),F(1,5)),(F(0),F(1),F(1,5)),
       (F(0),F(6,5),F(-4,25)),(F(6,5),F(0),F(-4,25)))
    # Boundary cycles; fan orientations are not used for unsigned 3D volumes.
    facets=((0,5,2,1),(0,1,3,4),(0,4,5),(1,2,3),(2,5,4,3))
    assert hull_faces(P)=={tuple(sorted(f)) for f in facets}
    edges={tuple(sorted((f[i],f[(i+1)%len(f)]))) for f in facets for i in range(len(f))}
    assert (len(P),len(edges),len(facets))==(6,9,5)
    ell=lambda v:a+(d-a)*v[0]+(c-a)*v[1]+(b-a)*v[2]
    nn=lambda v:hc*v[0]+hd*v[1]
    assert tuple(ell(v) for v in P)==(a,b,0,0,0,0)
    # C,D are genuine contained marks, not additional true vertices.
    marks=((F(0),F(1),F(0)),(F(1),F(0),F(0)))
    for f in facets:
        v0,v1,v2=(P[i] for i in f[:3]); norm=cross(sub(v1,v0),sub(v2,v0))
        off=dot(norm,v0); vals=[dot(norm,v)-off for v in P]
        if max(vals)>0: norm=tuple(-x for x in norm);off=-off
        assert all(dot(norm,p)<=off for p in marks)
    # Actual positive tetrahedron fan from A, excluding incident facets.
    V=F(0);J=[F(0)]*3;E=F(0);N=F(0);N2=F(0);cells=[]
    for f in facets:
        if 0 in f: continue
        for k in range(1,len(f)-1):
            ids=(0,f[0],f[k],f[k+1]); pts=[P[i] for i in ids]
            vol=abs(det(sub(pts[1],pts[0]),sub(pts[2],pts[0]),sub(pts[3],pts[0])))/6
            assert vol>0
            V+=vol;cells.append((ids,vol))
            for j in range(3): J[j]+=vol*sum(p[j] for p in pts)/4
            ns=[nn(p) for p in pts]
            E+=vol*sum(ell(p) for p in pts)/4
            N+=vol*sum(ns)/4
            N2+=vol*(sum(ns)**2+sum(t*t for t in ns))/20
    g=tuple(x/V for x in J);r=N/V;q=N/E;T=N/(6*V*E)
    assert (V,N,J[2],E,T)==(F(47,150),F(614,1875),F(899,15000),F(119,1200),F(9824,5593))
    # Independently integrated true projection K and root projection R.
    K=((F(0),F(0)),(F(6,5),F(0)),(F(0),F(6,5)))
    R=((F(1),F(0)),(F(6,5),F(0)),(F(0),F(6,5)),(F(1),F(0)))
    R=((F(1),F(0)),(F(6,5),F(0)),(F(0),F(6,5)),(F(0),F(1)))
    km=tri2(K,(hc,hd)); rm=tri2(R,(hc,hd))
    assert tuple(km[j]+b/alpha*rm[j] for j in range(3))==(3*V,4*N,5*N2)
    # G is positive on the true root, and C,D have positive G.
    GC=hd-r-q*c;GD=hc-r-q*d
    assert min(GC,GD)>0 and min(nn(P[i])-r for i in (2,3,4,5))>0
    kg=centered(km,r);rg=centered(rm,r)
    core=(r*r/(2*hc*hd),-r**3/(6*hc*hd),r**4/(12*hc*hd))
    om=tuple(kg[j]-rg[j]-core[j] for j in range(3))
    assert min(om)>0 and om[0]*om[2]-om[1]**2>0
    assert kg[2]+b/alpha*rg[2]==5*V*(N2/V-r*r)
    # This control checks the geometric theorem, not joint root stationarity.
    p=g[0]+g[1]; t=6*V; m=3*p/t
    predicted_stationary_W=t*t*alpha*(T-m)/6
    assert rg[1]!=predicted_stationary_W
    return dict(vertices=P,facets=facets,edges=sorted(edges),marks=marks,cells=cells,
        endpoint_values=(a,b,c,d),V=V,J=J,E=E,N=N,N2=N2,centroid=g,trace=T,
        canonical_G=(GC,GD),projection_K=K,root_projection=R,
        projected_n_moments=km,root_n_moments=rm,negative_core_G_moments=core,
        remaining_region_G_moments=om,remaining_Hankel_determinant=om[0]*om[2]-om[1]**2,
        actual_root_G_integral=rg[1],nonstationary_predicted_root_G_integral=predicted_stationary_W)

def formal_exclusion():
    a,b,c,d=F(1),F(2,3),F(1,60),F(1,60)
    t,T,u,v,z=F(9,5),F(51,25),F(11,32),F(11,32),F(1937,73440)
    hc=a+b+c;hd=a+b+d;p=u+v;V=t/6;m=3*p/t;r=hc*u+hd*v;q=T*t
    mu=a+(d-a)*u+(c-a)*v+(b-a)*z
    assert q*mu==r
    GC=hd-r-q*c;GD=hc-r-q*d
    assert GC==GD==F(55781,120000)>0
    nw=(hc*v+hd*u)/(3*p)
    rho0=(T-m)**2/(3*T*m*(1-nw/r))
    rhoU=mu*(t-1)/(b*t)
    assert rho0==F(1151329,5202000)
    assert rhoU==F(27775,132192)
    assert rho0-rhoU==F(3149891,280908000)>0
    gap=t*r-a*t*t*(T-m)+r**3/(hc*hd)
    cap=m+r/(a*t)+r**3/(a*hc*hd*t*t)
    assert gap==F(-8201437,30720000)<0
    assert cap==F(7793819,3981312)<T
    assert T-cap==F(8201437,99532800)
    # If arbitrary rho=1/4 is inserted, the required projection is too small.
    rho=F(1,4);Ar=t*(a-b)*rho/(2*mu);Ak=t/2-b/(a-b)*Ar
    assert Ak==F(117783,277750)<F(1,2)
    return dict(meaning='Formal data excluded as an actual joint local maximum; NOT a body',
        endpoints=(a,b,c,d),t=t,T=T,centroid=(u,v,z),r=r,mu=mu,m=m,
        canonical_G=(GC,GD),rho0=rho0,rho_upper=rhoU,positive_rho_gap=rho0-rhoU,
        negative_projection_excess_first_moment=gap/6,
        necessary_trace_cap=cap,positive_trace_gap=T-cap,
        tested_rho=rho,required_projected_area=Ak)

def main():
    assert sys.argv[1:] in (['build'],['check'])
    report=dict(name='TWO_ANCHOR_PROJECTED_MASS_OBSTRUCTION_V1',actual_control=actual_control(),formal_exclusion=formal_exclusion())
    raw=(json.dumps(enc(report),sort_keys=True,separators=(',',':'))+'\n').encode()
    path=Path(__file__).with_suffix('.json')
    if sys.argv[1]=='build':path.write_bytes(raw)
    else:assert path.read_bytes()==raw
    print('ACTUAL_TWO_ANCHOR_PROJECTED_MOMENT_IDENTITIES_PASS 6 9 5')
    print('ACTUAL_NEGATIVE_CORE_AND_POSITIVE_COMPLEMENT_MOMENTS_PASS')
    print('FORMAL_51_OVER_25_ALL_RHO_AND_COVARIANCE_EXCLUSION_PASS')
    print(path.name,len(raw),hashlib.sha256(raw).hexdigest())
    print('TWO_ANCHOR_PROJECTED_MASS_RECOVERY_PASS')
if __name__=='__main__':main()
```
