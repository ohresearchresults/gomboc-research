# material-fe9f6a773b79

Historical AI scientific source/proof material. Statements retain their original scope; this is not an independently reviewed theorem.

Public derivative: internal-record-identifiers-replaced.

---

# Planar variation and two complete centered whole-facet subclasses

## Status and parent
These are new coordinator analytical and exact-symbolic results. They do NOT prove the universal centered whole-facet inequality, any whole E17 exclusion, or an improved attainer. The separate accepted bounds remain 34<=Cmin<=622. The fully read parent is minimum-0290, SHA256 a1afff32561b16a73bf7a017e7ad3233330ac76bf67282f7cac952c02cc464a8. It establishes the exact arbitrary-planar-support reduction, the universal normal bound, full affine-thickness triangle bound and sharp transverse bound 10-5sqrt(3). Its literal result remains the exact dependency for those theorems; the arguments and two computations newly supplied here do not require its code.

## 1. Actual-centred variation formula
Let K be a full-dimensional convex planar body, t>=0 a nonconstant affine coordinate with marked whole edge e={t=0}, and ell a nonnegative nonzero affine density. Let V=int_K ell, J=int_K t ell, m=J/V. Fix an affine y, let Y=y-E_mu y, I=int_K ell Y^2, and B_j=int_e ell Y^j/|grad t|. Assume I,B2>0 and use R=J B2/(V I). All coordinates Y below are centred at the ACTUAL current density barycentre. For a small signed change of the support away from e, keeping ell fixed, let delta nu be the signed density mass added or removed. Then

    delta log R = int Phi d(delta nu) + O(||delta nu||_TV^2),
    Phi(t,Y) = t/J - 1/V - Y^2/I - 2 B1 Y/(V B2).

The expansion applies to bounded small perturbations. Indeed delta mu_y=int Y d(delta nu)/V+O(delta mass^2); delta B2=-2 B1 delta mu_y+O(delta mass^2), whereas delta I=int Y^2 d(delta nu)+O(delta mass^2), since int_K ell Y=0. In particular the centring term in Phi may NOT be dropped. For the positive leverage ratio L=J B1^2/(V B0 I), B1!=0, the same formula holds with B1/B2 replaced by B0/B1.

## 2. Polygonal local-maximizer obstruction
Assume (t,Y) are independent affine coordinates. At a local maximum of R, or of a positive L, among ALL nearby convex supports with the same marked edge and the same affine density, every vertex v not on e satisfies Phi(v)>=0. Otherwise removing a sufficiently small cap at v, avoiding e, strictly increases the ratio. This remains valid if ell(v)=0: every nonempty sufficiently small cap has positive density mass, and Phi is uniformly negative there.

Suppose a true polygon edge [v,w] has neither endpoint on e and ell is not identically zero on that edge. Along it,

    Phi((1-s)v+s w) = (1-s)Phi(v)+s Phi(w)
                          + s(1-s)(Y(v)-Y(w))^2/I.

If Y(v)!=Y(w), this is strictly positive in its interior. If Y(v)=Y(w), independence implies t(v)!=t(w), hence Phi(v)!=Phi(w); the nonnegative endpoint values again give a positive interior value. A sufficiently small outward cap on the relative interior of this edge sees only that true edge, stays in t>0 and ell>=0, and has strictly positive leading variation. This contradicts local maximality.

Consequently every edge joining two vertices off e would have to lie in the single line ell=0. A genuine n-gon has n-3 such edges, whereas at most one true edge lies in a fixed supporting line. Therefore a polygonal local maximizer has n<=4. For n=4 its edge opposite e has ell=0. If ell is strictly positive on K, a polygonal local maximizer has n<=3. For ell constant positive the latter statement applies. This is a local-maximizer theorem in the unrestricted support class, NOT a bound on the number of vertices in arbitrary counterexamples, NOT a proof of a triangular/quadrilateral localization, and NOT permission to discard curved supports. Adding/removing caps can increase the number of vertices.

When (t,Y) are dependent the normal theorem in the parent handles the ratio; the strict chord argument is not claimed in that case. Combined with the parent's triangle theorem and Section3, any polygonal maximizer cannot exceed3/2. This does NOT establish that a global maximizing support is polygonal.

## 3. Complete quadrilaterals with affine density zero on the opposite edge
Every genuine convex quadrilateral with marked edge e and a nonnegative affine density vanishing on the opposite edge has horizontal whole-facet matrix bound alpha T<=3Sigma/2. The covariance Sigma and facet second moment T are both around its actual affine-density barycentre.

For nonparallel lines e and ell=0, use the independent affine coordinates (t,ell), with positive rescalings. The two edges become positive axis segments, so up to interchanging endpoints and rescaling the model is

    K=conv{(0,1),(1,0),(1+b,0),(0,1+a)}, ell=y, a,b>0,
    e={t=0,1<=y<=1+a}.

Put B=1+a,D=1+b. K is the outer right triangle with intercepts D,B minus the inner right triangle with intercepts1,1. Thus the complete raw moments are

    M_ij=int_K t^i y^j ell = i! (j+1)! [D^(i+1) B^(j+2)-1]/(i+j+3)!,
    E_j=int_e ell y^j = [B^(j+2)-1]/(j+2).

Let V=M00, Jvec=(M10,M01), K2=[[M20,M11],[M11,M02]], g=Jvec/V, c=(0,E1/E0), alpha=M10 E0/V^2. Then

    Sigma=K2/V-gg^T,
    T=diag(0,E2/E0)-gc^T-cg^T+gg^T.

The supplied exact source forms G=3Sigma/2-alpha T. Expanded in a,b, the numerator of G00 has52 nonnegative monomials (total degree14), and the numerator of det G has99 nonnegative monomials (degree22); both have positive terms. Their denominators also have nonnegative coefficients and are strictly positive for a,b>0. Sylvester therefore gives G>0 on the ENTIRE strict two-parameter quadrant, not at sampled points.

If e and ell=0 are parallel, rotate the opposite supporting line slightly, move its two endpoints continuously on the adjacent side lines, and use a positive normalization of its vanishing affine density converging to ell. The positive density on e persists for sufficiently small rotations. These genuine nonparallel quadrilaterals converge with all volume, centroid and edge moments. The non-strict bound follows by continuity. No assertion of strictness or sharpness at every parallel limit is needed.

For the actual uniform three-dimensional lift P={(t,y,z):(t,y) in K, |z|<=ell(t,y)/2}, mixed horizontal/z moments vanish about the actual centroid. The parent's universal transverse bound 10-5sqrt(3)<3/2 therefore combines with the new horizontal block to give the full three-dimensional whole-facet matrix bound on the marked lateral facet. This is a moment theorem, not an equilibrium census.

## 4. A complete curved-support control: parabolic-wing prisms
This independent family is included because the local-maximizer theorem leaves curved supports genuinely open. Let d>0,0<=v<=1, use coordinates(t,y), and put

    U(y)=(y+1)/(d+2),
    W(y)=(1-v)(y-1)/d + v(y-1)^2/d^2.

Take -1<=y<=1+d, upper bound t<=U(y), lower bound t>=0 for y<=1 and t>=W(y) for y>=1, and constant density ell=1. The lower graph is convex and joins t=0 with nonnegative derivative; U is affine and lies above it. Hence this is a genuine convex support with marked edge e={t=0,-1<=y<=1}. For v>0 the wing is curved and no finite polygon-support reduction is being assumed. At v=0 it is an ordinary triangle.

The exact source integrates both pieces and forms the same actual-centred matrix. It gives

    V=(dv+6)/6,
    J_t=-(dv^2-5dv-20)/60,
    J_y=(d^2v+2dv+4d+4)/12,
    alpha=6[(5-v)dv+20]/[5(dv+6)^2].

Power-positive coefficients in d and Bernstein coefficients in v of G00,G11,det G are all nonnegative: respective control counts35,35,81 with10,10,36 zeros. In fact G00 and det G already have positive-coefficient power numerators, so they are strictly positive throughout d>0,0<=v<=1. Thus the full horizontal matrix bound holds on this entire unbounded curved-support family. Its ordinary uniform height-one prism lift also satisfies the full3D matrix bound: the vertical block has ratio alpha<=2/3, since with D=dv,

    2/3-alpha=2D(5D+15+9v)/[15(D+6)^2]>=0.

This is a complete control family, not a classification of the remaining extremizers.

## 5. Remaining free-boundary mechanism
On a C2 strictly curved free boundary arc away from e, with positive ell, both signs of sufficiently small smooth normal variations are admissible. Stationarity requires Phi=0. Consequently that arc, in independent(t,Y) coordinates, lies on

    t=J/V + (J/I)Y^2 + (2J eta/V)Y,
    eta=B1/B2 for R, eta=B0/B1 for L.

The parabola has positive curvature as a t-graph, so it can occur on the lower t-boundary, not on a strictly concave upper graph. This is a necessary local condition only. Matching flat arcs, supporting density-zero edges, nonsmooth curvature measures, existence/compactness of a global extremizer, and a universal bound on those remaining configurations are NOT settled. The simple wing in Section4 does not cover all such stationary configurations. None of these results alone implies a whole E17 mechanical exclusion.

## Recovery and exact output pins
Each source below is standalone. Save its literal block under the named filename, with LF newlines and one final newline. Environment: Python3.13.5, SymPy1.14.0. No input checkpoint, numerical seed, external file or non-default precision is used. Assertions must remain enabled.

    python -B zero_opposite_quad.py
    python -B parabolic_wing.py

These are both reconstruction and verification commands. Expected markers:
ZERO_OPPOSITE_QUAD_HORIZONTAL_THREE_HALVES_EXACT_PASS
PARABOLIC_WING_COMPLETE_MOMENT_PASS

Input pins:
zero_opposite_quad.py1998B SHA25629f458b951a2324166b97433bc6040ae62ba29e19756e5ea2253f746e59cc3cc
parabolic_wing.py2173B SHA25605cf198814dc0bb9e4853fb53f49e7c5763ca2177f9cd10c590a1d8c14593100
Output pins:
zero_opposite_quad_report.json3944B SHA2561fa96292d019370b1e205245279a46f5d568bd3901503db0ba2d51b8d145fd95
parabolic_wing_report.json4236B SHA2562e852af71f738a14e7c109f8d8b83f692fc68b6d9c1e7b9a05097753b384faaf
Both normal executions and fresh source-only executions completed and produced byte-identical reports. These are exact-symbolic checks of the displayed identities and positive polynomials, not formal proof-assistant certification.

## Complete source zero_opposite_quad.py

```python
"""Exact centered whole lateral-facet matrix for every nonparallel quadrilateral
with affine density zero on its opposite edge. K=conv{(0,1),(1,0),
(1+b,0),(0,1+a)}, ell=y, a,b>0. Raw coordinates (t,y).
Python3.13.5 SymPy1.14.0. Assertions required. No saved input.
"""
import sympy as s,json,hashlib
from pathlib import Path
a,b=s.symbols('a b',nonnegative=True);B=1+a;D=1+b

def moment(i,j):return s.factor(s.factorial(i)*s.factorial(j+1)*(D**(i+1)*B**(j+2)-1)/s.factorial(i+j+3))
V=moment(0,0);J=s.Matrix([moment(1,0),moment(0,1)]);K=s.Matrix([[moment(2,0),moment(1,1)],[moment(1,1),moment(0,2)]])
Bj=[s.factor((B**(j+2)-1)/s.Integer(j+2)) for j in range(3)]
g=J/V;c=s.Matrix([0,Bj[1]/Bj[0]])
T=s.diag(0,Bj[2]/Bj[0])-g*c.T-c*g.T+g*g.T
Sig=K/V-g*g.T;alpha=s.factor(J[0]*Bj[0]/V**2)
G=(s.Rational(3,2)*Sig-alpha*T).applyfunc(s.factor)
print('V',V,'g',list(map(s.factor,g)),'alpha',alpha,flush=True)
records=[]
for name,f in [('G00',G[0,0]),('det',s.factor(G.det()))]:
    num,den=s.fraction(f);P=s.Poly(s.expand(num),a,b);N=s.Poly(s.expand(den),a,b)
    ok=all(x>=0 for x in P.coeffs()) and all(x>=0 for x in N.coeffs())
    print(name,'terms',len(P.terms()),'negative',sum(bool(x<0) for x in P.coeffs()),'degree',P.total_degree(),'positive',ok,flush=True)
    records.append({'name':name,'numerator':str(num),'denominator':str(den),'positive_coefficients':ok,'num_terms':len(P.terms()),'num_degree':P.total_degree()})
report={'identity':'AFFINE_QUADRILATERAL_ZERO_OPPOSITE_EDGE_CENTERED_THREE_HALVES_V1','volume':str(V),'first_moment':list(map(str,J)),'second_moment':list(map(str,K)),'edge_moments':list(map(str,Bj)),'g':list(map(str,g)),'alpha':str(alpha),'certificates':records}
data=(json.dumps(report,sort_keys=True,indent=2)+'\n').encode();Path(__file__).with_name('zero_opposite_quad_report.json').write_bytes(data)
assert all(x['positive_coefficients'] for x in records)
print('ZERO_OPPOSITE_QUAD_HORIZONTAL_THREE_HALVES_EXACT_PASS',len(data),hashlib.sha256(data).hexdigest(),flush=True)
```

## Complete source parabolic_wing.py

```python
"""Exact whole-facet moment check for a convex parabolic-wing planar prism.
Standalone analytic polynomial identities; no numerical inputs.
Python3.13.5 SymPy1.14.0. Assertions required.
"""
import sympy as s,json,hashlib
from pathlib import Path
d,v,y,t=s.symbols('d v y t',nonnegative=True)
# e: t=0,-1<=y<=1. Top line to (t,y)=(1,1+d), and convex lower wing.
u=(y+1)/(d+2)
w=(1-v)*(y-1)/d+v*(y-1)**2/d**2

def integ(f):
    f=s.integrate(f,t)
    a=s.integrate(f.subs(t,u)-f.subs(t,0),(y,-1,1))
    b=s.integrate(f.subs(t,u)-f.subs(t,w),(y,1,1+d))
    return s.factor(a+b)
V=integ(1);J=s.Matrix([integ(t),integ(y)])
K=s.Matrix([[integ(t*t),integ(t*y)],[integ(t*y),integ(y*y)]])
g=J/V;alpha=s.factor(2*J[0]/V**2)
S=K/V-g*g.T;T=s.diag(0,s.Rational(1,3))+g*g.T
G=(s.Rational(3,2)*S-alpha*T).applyfunc(s.factor)
print('V',V,'J',J.T,'alpha',alpha,flush=True)
print('G00',G[0,0],flush=True)
print('G11',G[1,1],flush=True)
print('DET',s.factor(G.det()),flush=True)
records=[]
for name,f in [('G00',G[0,0]),('G11',G[1,1]),('det',s.factor(G.det()))]:
    num,den=s.fraction(f)
    P=s.Poly(num,d,v);N=P.degree(v)
    # Power-positive d and Bernstein-positive v imply whole d>=0,0<=v<=1.
    coeff=[]
    for i in range(P.degree(d)+1):
        pd=s.Poly(s.expand(num).coeff(d,i),v)
        for j in range(N+1):
            val=s.factor(sum(pd.nth(k)*s.binomial(j,k)/s.binomial(N,k) for k in range(j+1)))
            coeff.append(val)
    print(name,'controls',len(coeff),'negative',sum(bool(x<0) for x in coeff),'zeros',sum(x==0 for x in coeff),flush=True)
    records.append({'name':name,'numerator':str(num),'denominator':str(den),'controls':list(map(str,coeff)),'nonnegative':all(x>=0 for x in coeff)})
report={'identity':'PARABOLIC_WING_UNIFORM_PRISM_CENTERED_THREE_HALVES_V1','volume':str(V),'first_moment':list(map(str,J)),'second_moment':list(map(str,K)),'controls':records}
b=(json.dumps(report,sort_keys=True,indent=2)+'\n').encode();Path(__file__).with_name('parabolic_wing_report.json').write_bytes(b)
print('PARABOLIC_WING_COMPLETE_MOMENT_PASS' if all(x['nonnegative'] for x in records) else 'PARABOLIC_WING_INCOMPLETE_SIGN_TEST',len(b),hashlib.sha256(b).hexdigest())
```
