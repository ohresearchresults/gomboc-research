# material-641cc5803a02

AI research material · [Export notes](../catalog/coverage.md#text-records)

<!-- historical-status:start -->
> **Historical AI material.** The title and claims below reflect the AI’s assessment at the time. Claims of proof, certification or completion are not a current verification verdict.
>
> [C622](../C622/README.md) passes the supplied exact checks; C<500 remains open; Minimum’s C≥34 remains a working lower bound requiring a consolidated proof. See [verification status and source gaps](../catalog/coverage.md).
<!-- historical-status:end -->

---

# J111 — all direct new roots, every cut family of polar witness depth at most3, and a64-times-wider centre cube

This is a new EXECUTED exact finite-family exclusion, not an own110 construction and not a global impossibility result. It strengthens J109 by using convexity of the homogeneous body, rather than a positive/negative moment relaxation. The complete verifier is below. Its sole input is the1888-byte literal R82.txt FILE block already preserved in [internal-source-reference] (J109 exact capsule). Read and supply that complete material together with this one for a computational successor. No old47-unit workspace, floating geometry engine, external optimizer or originating sandbox is required.

## Precise theorem
K={x:N_i.x<=1000000 for the literal82 R82 rows}. Set rational O=(.02496294,.00321635,-.00678274), delta=1/32, kappa=31/10. For EVERY c with ||c-O||infinity<=delta, put q_i(c)=N_i/(1000000-N_i.c). Take ANY r!=0 satisfying q7(c).(r-q7(c))>=0 and q18(c).(r-q18(c))>=0. Intersect K with r.(x-c)<=1 and ANY family of further cuts w.(x-c)<=1, where each w admits at most THREE nonnegative radial steps to r: x0=w,...,xm=r,m<=3, xj.(x(j+1)-xj)>=0. The intermediate vectors may be virtual; in particular every actual cut tree of that depth is included. There is no count limit on controls and arbitrary old-facet retirement is allowed.

For the resulting homogeneous convex body L,

r.(centroid(L)-c) < -1/40.

In particular its own centre cannot be c. This is a scale-invariant centroid-coordinate gap, not the unnormalized first-moment bound from J109. The theorem does NOT exclude depth>=4, trees using longer routes through old points, other policies for replacing the old stable basin, changed old K, added material, or c outside this cube. It does not assert that all few-cut constructions have a short tree. K's old equilibrium labels are not assumptions of the proof beyond the literal designation of rows7 and18.

## 1. Exact support of bounded-depth radial chains
Let r=rho*n with |n|=1, and let z make angle theta with n. The support over all w admitting at most m nonnegative radial steps to r is

H_m(z)=rho*|z|*cos(theta/(m+1))^(m+1), m>=1.

Proof: include the angle between w and z as one additional angle. A positive objective requires this angle<pi/2. Each radial inequality bounds the preceding length by the next length times the cosine of their angle; all relevant angles lie in[0,pi/2]. Their sum is at least theta. Concavity of log(cos) bounds their product by cos(theta/(m+1))^(m+1). Equality is attained by equally spaced directions on a great-circle arc from z/|z| to n, with the successive source lengths chosen by the cosine equalities. Shorter paths can be padded with repeated points. Zero source vectors are harmless. Strict paths have the same supremum by inward limiting perturbations.

Thus every such cut retains the compulsory convex core with radial extent

h*sec(theta/(m+1))^(m+1), h=1/rho.

Its backwards extent is infinite for m1,8h for m2,4h for m3, and about2.885h for m4. In particular any depth<=3 cut evaluates at z0=-kappa*r/|r|^2 to at most kappa/4=31/40<1.

## 2. The old K also retains z0, uniformly in root direction and centre
Write a_j(c)=q_j(c)/|q_j(c)|^2=(1000000-N_j.c)N_j/|N_j|^2. The two root inequalities are exactly a7(c).r>=1 and a18(c).r>=1. For each old row i, the verifier constructs nonnegative rational multipliers lambda7,lambda18 such that throughout the entire centre cube

lambda7+lambda18 - |kappa*q_i(c)-lambda7*a7(c)-lambda18*a18(c)|^2/4 > 59/1000.

Completing the square therefore gives, for every feasible r,

|r|^2+kappa*q_i(c).r >59/1000>0.

Consequently q_i(c).z0<1 for all82 old planes, so c+z0 lies strictly inside old K. The multipliers are obtained from an exact two-halfspace quadratic projection at O; their optimality is not needed once the above strict certificate is checked. Each a_j(c) is affine, and each q_i(c) is a fixed vector divided by a strictly positive affine denominator. Componentwise rational intervals bound every coefficient over the full cube; no centre samples, numerical signs or sphere sampling are used.

The worst interval certificate is at input row40. Its gap is strictly between59399725599/10^12 and59399725600/10^12, approximately .0593997256. Four spanning old normals0,1,25,79 have positive dependence weights54310017238897143,104340949429946730,349664626843221027,409554057464299308; this proves K is bounded. All old offsets stay strictly positive throughout the cube, so it also has interior there.

## 3. Homogeneous centroid constraint from convexity
For any full-dimensional compact convex body with projection range[-d,b] in a unit direction, its mean projection is at most(3b-d)/4. To prove this directly, take a lowest point p. The copy p+t(L-p) is contained in L by convexity, has volume t^3 times volume(L), and lies below height -d+t(b+d). Thus the distribution function of the nonnegative random height T+d is at least(s/(b+d))^3. Integrating its tail gives E[T+d]<=3(b+d)/4.

Here the root cut bounds b<=h, while c+z0 is an interior point of L at projection -kappa*h. The point is interior even for an infinite family: all added normals have length<=rho and share the strict31/40 bound there; old K has finitely many strict inequalities. Hence d>kappa*h. The mean projection is strictly less than(3-kappa)h/4=-h/40, giving r.(centroid(L)-c)<-1/40.

A related universal consequence is that a homogeneous convex polyhedron centred at0 cannot have ALL its normalized supporting normals reach a single r through at most3 radial steps: the full depth3 core would force a backwards support4h but the centroid constraint requires at most3h. This does not bound the total number of faces or exclude longer trees.

## Why the new convexity argument matters
A positive relaxed moment capacity is not realizability. For the depth2 core, its whole negative axial moment is exactly (7168*pi/135)h^4. This follows by t=cos(theta), y=tan(theta/3), integrating -3(1-3y^2)(3y-y^3)(1+y^2)^2 from y=1/sqrt3 to sqrt3; the integral is14336/135. If a ball of radius R is in K and h*sqrt(14471/135)<R, the union of the negative depth2 core and the positive cylinder 0<=n.z<=h, |z-(n.z)n|<=h*sqrt(14336/135) contains the full core, lies inside the root-cut ball, and has centroid0. Its positive cylinder moment exactly balances the core's negative moment. This union is NOT convex. Its existence shows that a merely measurable sandwich relaxation really can fail to exclude depth2, while the convex homogeneous centroid argument still excludes it. The numerical moment-capacity probes preceding this theorem must not be mistaken for feasible convex mass control.

## Exact recovery and observed execution
Extract verify111.py below and R82.txt from the complete input material to the same directory. Run `python -B -S verify111.py`. Executed environment CPython3.13.5, standard library only. Expected terminal:
`J111_ALL_ROOTS_DEPTH3_CUBE1_OVER32_CENTROID_GAP_EXACT_PASS_NO_110`.

Manifest:
- R82.txt1888B SHA9765712b5ffaa464ed4d677974256294c6d867b77fe77b930d166853f66a92a7 (complete literal in [internal-source-reference]).
- verify111.py5420B SHAbe64471b038968ac9e36c05009872a5191350b5178ffea30fe7105622984ae66.
- Generated J111_EXACT.json187892B SHAa989c0603c113e04ecafe0be0ed1d4e67955a1f022688428a7e69fa77bbedf74. It contains all82 exact multipliers, all coefficient intervals and exact gap values, not a selected subset. It is regenerated deterministically by the complete source; a hash is not being used instead of input bytes.

### FILE verify111.py
```python
"""J111: exact three-step polar-cut obstruction, including a large centre cube.
CPython standard library only. This proves a scoped family exclusion, not own110.
The geometric envelope and centroid arguments are proved in the accompanying text.
"""
from fractions import Fraction as F
from pathlib import Path
import hashlib, json, sys
sys.set_int_max_str_digits(0)
ROOT=Path(__file__).resolve().parent
raw=(ROOT/'R82.txt').read_bytes()
assert len(raw)==1888 and hashlib.sha256(raw).hexdigest()=='9765712b5ffaa464ed4d677974256294c6d867b77fe77b930d166853f66a92a7'
lines=raw.decode().splitlines(); count,D=map(int,lines[0].split())
N=[tuple(map(int,line.split())) for line in lines[1:]]
assert count==len(N)==82 and D==1000000
O=tuple(map(F,('0.02496294','0.00321635','-0.00678274')))
DELTA=F(1,32); KAPPA=F(31,10)
def dot(a,b): return sum(x*y for x,y in zip(a,b))
def add(a,b): return tuple(x+y for x,y in zip(a,b))
def sub(a,b): return tuple(x-y for x,y in zip(a,b))
def mul(t,a): return tuple(t*x for x in a)
def cross(a,b): return (a[1]*b[2]-a[2]*b[1],a[2]*b[0]-a[0]*b[2],a[0]*b[1]-a[1]*b[0])
def det(a,b,c): return dot(a,cross(b,c))
def interval(x,den=10**12):
    k=(x*den).numerator//(x*den).denominator
    return [k,k+1,den]
# A positive dependence on four spanning old normals proves that K is bounded.
ids=(0,1,25,79); ns=[N[i] for i in ids]
weights=[(-1)**j*det(*(ns[:j]+ns[j+1:])) for j in range(4)]
if max(weights)<0: weights=[-w for w in weights]
assert min(weights)>0 and all(sum(w*n[k] for w,n in zip(weights,ns))==0 for k in range(3))
assert det(*ns[:3])!=0
# Strict old-plane offsets for every centre in the entire closed infinity cube.
d=[D-dot(v,O) for v in N]
assert all(s-DELTA*sum(map(abs,v))>0 for s,v in zip(d,N))
q=[mul(1/s,v) for v,s in zip(N,d)]
a=[mul(d[i]/dot(N[i],N[i]),N[i]) for i in (7,18)]

def multipliers(v):
    """Exact KKT projection onto the two direct-root halfspaces at O.
    Only the resulting nonnegative multipliers, not optimality, are used in proof.
    """
    p=mul(-KAPPA/2,v)
    for active in ((),(0,),(1,),(0,1)):
        mu=[F(0),F(0)]
        if len(active)==1:
            j=active[0]; mu[j]=(1-dot(a[j],p))/dot(a[j],a[j])
        elif len(active)==2:
            A,B,C=dot(a[0],a[0]),dot(a[0],a[1]),dot(a[1],a[1])
            s,t=1-dot(a[0],p),1-dot(a[1],p); dd=A*C-B*B
            assert dd>0
            mu=[(C*s-B*t)/dd,(A*t-B*s)/dd]
        r=add(p,add(mul(mu[0],a[0]),mul(mu[1],a[1])))
        if min(mu)>=0 and all(dot(aa,r)>=1 for aa in a):
            return [2*t for t in mu]
    raise AssertionError('Exact two-halfspace projection did not find multipliers')

# a_j(c)=(D-N_j.c) N_j/|N_j|^2 is affine in c.
af=[]
for j in (7,18):
    err=DELTA*sum(map(abs,N[j]))/dot(N[j],N[j])
    lo=d[j]/dot(N[j],N[j])-err; hi=d[j]/dot(N[j],N[j])+err
    af.append([(min(lo*v,hi*v),max(lo*v,hi*v)) for v in N[j]])
certificate=[]
for i,v in enumerate(q):
    lam=multipliers(v); assert min(lam)>=0
    ds=DELTA*sum(map(abs,N[i])); lo,hi=d[i]-ds,d[i]+ds; assert lo>0
    qi=[(min(F(t,1)/lo,F(t,1)/hi),max(F(t,1)/lo,F(t,1)/hi)) for t in N[i]]
    coefficients=[]
    for k in range(3):
        low=KAPPA*qi[k][0]-sum(lam[j]*af[j][k][1] for j in (0,1))
        high=KAPPA*qi[k][1]-sum(lam[j]*af[j][k][0] for j in (0,1))
        assert low<=high; coefficients.append((low,high))
    square_upper=sum(max(lo*lo,hi*hi) for lo,hi in coefficients)
    gap=sum(lam)-square_upper/4
    assert gap>F(59,1000)
    certificate.append(dict(input_plane=i,lambda7=str(lam[0]),lambda18=str(lam[1]),
        coefficient_intervals=[[str(a),str(b)] for a,b in coefficients],gap=str(gap)))
worst=min((F(row['gap']),row['input_plane']) for row in certificate)
# K contains c-KAPPA*r/|r|^2 for every root r with a7(c).r>=1,a18(c).r>=1.
# Every cutting vector with <=3 radial steps to r evaluates there <=KAPPA/4<1.
# Hence L reaches below -KAPPA*h while its root cut bounds it above by h.
# Homothetic volume inclusion implies centre(L).n <=(3h+minimum height)/4,
# yielding the strict scale-invariant gap r.(centre(L)-c)<-1/40.
assert KAPPA<4 and (KAPPA-3)/4==F(1,40)
result=dict(identity='J111_ALL_DIRECT_ROOTS_DEPTH_AT_MOST3_CENTROID_CUBE_EXCLUSION',
    scope='Literal R82, every c with ||c-O||infinity<=1/32, every nonzero r receiving nonnegative radial arrows from BOTH q7(c),q18(c), any family of additional cuts each admitting at most3 nonnegative radial steps to r. Their intermediate vectors may be virtual; any actual such tree is included. Root cut and all added cuts use centre c. Old-facet retirement is unrestricted. A homogeneous convex intersection cannot have centroid c. Paths longer than3, changed old K, other root policies, and centres outside the cube are not excluded.',
    O=list(map(str,O)),delta=str(DELTA),retained_back_point_multiple=str(KAPPA),
    centroid_gap='r.(centroid(L)-c)<-1/40',worst_plane=worst[1],
    worst_gap=str(worst[0]),worst_gap_interval=interval(worst[0]),
    boundedness_normals=list(ids),boundedness_positive_weights=weights,certificate=certificate)
output=(json.dumps(result,indent=2)+'\n').encode();(ROOT/'J111_EXACT.json').write_bytes(output)
print(json.dumps(dict(planes=82,delta=str(DELTA),kappa=str(KAPPA),worst_plane=worst[1],
    worst_gap_interval=interval(worst[0]),output_bytes=len(output),output_sha256=hashlib.sha256(output).hexdigest()),indent=2))
print('J111_ALL_ROOTS_DEPTH3_CUBE1_OVER32_CENTROID_GAP_EXACT_PASS_NO_110')
```
