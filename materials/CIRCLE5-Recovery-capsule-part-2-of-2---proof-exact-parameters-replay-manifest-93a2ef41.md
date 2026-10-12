# material-93a2ef419e63

AI research material · [Export notes](../catalog/coverage.md#text-records)

---

# CIRCLE5: exact mass-balanced circular sections and two polyhedral nonwinners

This is Recovery capsule part 2/2 for object/method identity CIRCLE5_V1. Part 1/2 is the entire literal source circle_family.py, immutable material [internal-source-reference], 13139 UTF-8 bytes, SHA-256 81988ecb6ea4601709b7c0311332a48da6f1a7cb1171b19e2aadeb9f99039c68. Both parts together are self-contained. No originating sandbox, prior worker result, archive, numerical input checkpoint or optimizer is required. Preserve the literal file from part 1 as circle_family.py without Markdown fences, UTF-8 and LF endings.

## Evidence boundary

The analytic theorem below constructs a homogeneous strictly convex C1 body with exactly two isolated nondegenerate radial critical points. It is smooth away from its two axial tips, generally NOT C2 at the tips, and is NOT a polyhedron. It is therefore not the requested own strict110/weak000 polyhedral construction with C<500. Its rational boundary and tangent oracles offer a new construction seed. No priority claim is made. The two exact finite polyhedra are deliberately retained negative controls, not records and not approximations promoted to110. Their full filled-volume centroids differ from that of the analytic body and are recomputed, not assumed zero.

## 1. General circular-section criterion

Write rho(x)=sqrt(1-x^2), -1<=x<=1, and take a continuous planar centre d(x). Define

K={ (x,w) in R x R^2 : -1<=x<=1, |w-d(x)|<=rho(x) }.

For each transverse unit vector n, h_n(x)=rho(x)+n dot d(x) is the support function of the x-slice. K is convex if and only if every h_n is concave: the convexity condition for two slices is precisely the Minkowski inclusion of their interpolated disks in the intermediate slice, equivalently all their support inequalities. If d is twice differentiable on (-1,1), then

|d''(x)| < -rho''(x) = rho(x)^(-3)

implies h_n''<0 for every n. The strict interpolation inequality holds for distinct x, including endpoints by continuity and interior strictness. Slices at fixed interior x are strictly convex disks. Thus K is strictly convex.

Each slice has area pi(1-x^2), independently of d. Hence

Vol(K)=4pi/3,
centroid_x=0,
centroid_w=(3/4) integral[-1,1] (1-x^2)d(x) dx.

These are FILLED-volume moments, not surface or point-mass moments.

If |d|=a>0 is constant and d=a(cos phi,sin phi), parameterize the boundary away from the tips by

p=(x,d(x)+rho(x)(cos theta,sin theta)), psi=theta-phi(x).

Its squared distance from zero is

q=|p|^2=1+a^2+2a rho(x) cos psi.

Coordinates (x,psi) are regular for |x|<1. Since rho>0 and a>0, q_psi=0 forces psi=0 or pi; q_x=0 then forces x=0. At these points rho'(0)=0,rho''(0)=-1 and the Hessian in (x,psi) is diag(-2a cos psi,-2a cos psi). There is one nondegenerate maximum and one nondegenerate minimum. There are no other interior critical points. To obtain the COMPLETE equilibrium statement one must also analyze the two axial tips; the argument is supplied for the exact family below.

For this constant-amplitude phase family,

|d''|=a sqrt(phi''^2+phi'^4).

For comparison, phi=kx with tan k=k makes the moment integral zero because integral(1-x^2)cos(kx)dx=4(sin k-k cos k)/k^3 and the sine moment is odd. For the first positive nonzero such root, 0<a<1/k^2 is a sufficient strict convexity condition. That transcendental-phase family is not needed to recover CIRCLE5 or either finite control.

## 2. Exact CIRCLE5 family

Fix any rational 0<a<1/25. Put

A(x)=1-12x^2+16x^4,
B(x)=5x-20x^3+16x^5,
C(x)=rho(x)A(x), S(x)=B(x),
d(x)=a(C(x),S(x)).

The polynomial identity

(1-x^2)A(x)^2+B(x)^2=1

shows |d|=a. Equivalently C=cos(5 arcsin x), S=sin(5 arcsin x). This trigonometric identification is explanatory only: the defining formulas and rational oracles contain no transcendental parameter solve.

### Exact own mass

The S moment is odd. The C moment is

integral[-1,1] (1-x^2)^(3/2)(1-12x^2+16x^4) dx
=3pi/8 -12(pi/16) +16(3pi/128)=0.

These half-integer beta integrals may alternatively be obtained by x=sin t and the orthogonality of cos(5t) to cos(t),cos(3t) over [-pi/2,pi/2], since cos^3 t=(3cos t+cos3t)/4. Therefore the actual filled centroid is exactly (0,0,0), and the volume is4pi/3.

### Strict convexity

For phi=5 arcsin x, phi'=5/rho and phi''=5x/rho^3. Therefore

rho^6 |d''/a|^2 =25(25-24x^2) <=625.

Thus |d''|<=25a rho^(-3)<rho^(-3), giving the strict convexity criterion in Section1. The source also checks this as a symbolic polynomial/radical identity, independently of numerical sampling.

### Tips, regularity and complete critical set

At x approaching +1 or -1, using rho as the small variable,

C=5rho+O(rho^3),
S=+1+O(rho^2) at +1,
S=-1+O(rho^2) at -1.

The tip coordinates are (1,0,a) and (-1,0,-a). Relative to either tip, the transverse boundary displacement is

rho(5a+cos theta, sin theta)+O(rho^2).

The circle centred at (5a,0) with radius1 contains zero strictly because5a<1. Consequently, in every transverse direction, displacement has size comparable to rho, while axial displacement is O(rho^2). Locally the boundary is a graph x=x_tip+O(|delta w|^2), with derivative zero at the tip. This graph is C1 there; away from the tip it is smooth, and its gradient tends to zero there. The unique outward support normal at each tip is respectively +e_x and -e_x. The radial vectors (1,0,a) and (-1,0,-a) are not parallel to these normals because a>0. Thus neither tip is an equilibrium. This also rules out hidden weak support equilibria at the nonsmooth-curvature tips.

The only radial critical points are therefore

U=(0,a+1,0), a nondegenerate maximum,
S=(0,a-1,0), a nondegenerate minimum.

The surface is generally not C2 at the tips: the leading quadratic graph depends on the gauge of a translated disk rather than a quadratic form. Do not describe CIRCLE5 as globally C-infinity. Its two equilibrium points themselves lie in a smooth part and are nondegenerate. For a convex C1 body containing its own centroid, radial critical points are exactly points whose support plane is perpendicular to the centroidal radius, so the radial classification gives the usual single stable and single unstable support equilibria. There is no finite V/E/F or C attached to this analytic body.

## 3. Rational boundary and tangent oracles

Choose rational t in[-1,1], and set

x=2t/(1+t^2), rho=(1-t^2)/(1+t^2).

Choose a rational unit vector u=(u1,u2), with u1^2+u2^2=1. Two equivalent sampling conventions are useful.

Fixed-world transverse direction:
p=(x,aC+rho u1,aS+rho u2).

Phase-aligned transverse direction:
p=(x,C(a+rho u1)-S rho u2,S(a+rho u1)+C rho u2).

All coordinates are rational. In the aligned convention, letting Y=rho u1,Z=rho u2, the map is p=(x,R_phi(x)(a+Y,Z)) and |p|^2=1+a^2+2aY. This makes the radial potential elementary but does not make fixed-psi grid edges gradient-aligned in the physical surface metric.

For an interior boundary point, let dy=y-aC,dz=z-aS. Since C'=-5S/rho,S'=5C/rho, an outward supporting normal is

n=(x-a(dy C'+dz S'),dy,dz), h=n dot p.

At the tips use n=(sign x,0,0),h=1. For rational t,a,u the normal and offset are rational. Strict convexity implies that these are supporting planes of the whole analytic body, not merely of a sampled cloud.

## 4. Complete source and what it verifies

The literal part1 source uses exact integers and fractions for maximal supporting planes, maximal facet polygons, true edges, two-origin tetrahedral mass, independent coordinatewise divergence volume/moment identities, all outgoing physical vertex signs, same-centre polar signs, independent physical facet-foot tests, and all true-edge normal-cone/foot tests. It checks the closed oriented connected maximal complex and Euler relation. SciPy Qhull nominates triples only; each nomination is checked exactly and the program aborts on non-supporting candidates or incomplete closure.

It distinguishes primitive zero predicates from actual additional weak equilibria. A vertex is strictU when every outgoing dot is negative and weakU when their maximum is zero. Stable facets are checked both by same-centre polar outgoing signs and by the relative interior of the orthogonal foot. Mixed-edge strict equilibria require an interior edge foot and strictly positive coefficients in the two-facet normal cone; additional weak cases use simultaneous nonnegative conditions with at least one equality. The weak-free S+U-H=2 identity is an extra check, not the source of the census.

Both physical and same-centre polar radial landscapes use the exact minimum squared radius along every TRUE chord. Equal death levels are processed simultaneously. A positive bar records the whole strict-superlevel dying component, its complete true-edge cut, peak/elder, exact birth/death/relative depth, and an attaining bottleneck path. This avoids a tie-order-dependent partial packet.

## 5. Exact reconstruction and verification commands

Tested environment: Python3.13.5, NumPy2.3.5, SciPy1.17.0, SymPy1.14.0. No random seed is used. No optimizer is run. All input parameters and the eight transverse directions are literal in this capsule/source. The eight directions in cyclic order are

(1,0),(3/5,4/5),(0,1),(-3/5,4/5),(-1,0),(-3/5,-4/5),(0,-1),(3/5,-4/5).

For both controls m=5,a=1/26. Use t=j/5 for j=-5,...,5, all eight directions on every interior slice and one copy of each tip. Sort the distinct rational coordinate tuples lexicographically, as the source does. This gives74 input/hull vertices. No rounding occurs. Do not set --no-landscape.

Reconstruction AND verification, in a clean directory containing the exact source:

OPENBLAS_NUM_THREADS=1 python circle_family.py --out aligned5 --m 5 --a 1/26 --mode aligned
OPENBLAS_NUM_THREADS=1 python circle_family.py --out fixed5 --m 5 --a 1/26 --mode fixed

Each command must print both terminal markers:
CIRCLE5_EXACT_IDENTITIES_PASS
CIRCLE5_EXACT_POLYHEDRON_PASS

The source writes all exact input coordinates, complete maximal faces/edges, actual mass, roots/weak lists and both landscapes in input.json and audit.json. The source plus the two commands is a complete deterministic generator of every output byte; the large literal audit reports need not be archived in addition to this recovery capsule.

Expected files and SHA-256:

circle_family.py:13139bytes,81988ecb6ea4601709b7c0311332a48da6f1a7cb1171b19e2aadeb9f99039c68
aligned5/input.json:3960bytes,a255526516b4c06e611aaf8e6bdd20374ac83ed0257acb9aa5228e1f8f2748aa
aligned5/audit.json:385500bytes,c58d3c68673df12e2ae9388395c887f65747f0c29357668c865f31d71f5a3559
fixed5/input.json:3688bytes,5a12b0998d9bce0deb39ccd15b446dd3d5b125f566a683aa3f9b41e31a152ebe
fixed5/audit.json:155093bytes,f24b93a6e2db66d89e18bab1a4eb212b72d7f2c97c71b3c5fe18ee30e5262587

Hash verification command:
sha256sum circle_family.py aligned5/input.json aligned5/audit.json fixed5/input.json fixed5/audit.json

The expected input bytes are generated from the literal exact recipe, not from hashes. Hashes identify the resulting bytes and do not substitute for the source.

## 6. Exact negative-control results

CIRCLE5_ALIGNED_M5_A1_26:
V74/E216/F144,C432,
strict(S,U,H)=(108,74,180),additionalweak000,primitivezero000.
Actual filled centroid:
(0,-530185097556548201658023854432649559105712524779490686761938202080381/298078006200860855785065039652234072324642912165444571881813932375338720,0).

CIRCLE5_FIXED_M5_A1_26:
V74/E152/F80,C304,
strict(S,U,H)=(64,74,136),additionalweak000,primitivezero000.
Actual filled centroid:
(0,-2790699005689809782996471213071539759/5806879106576379522227393077515092452472,0).

The fixed-direction version preserves many quadrilateral facets because consecutive equal-orientation homothetic polygon slices have coplanar lateral quadrilaterals. The aligned version generally triangulates them and consumes more edges. Both have all74 vertices unstable at their OWN mass, despite the analytic body's unique unstable equilibrium. They are evidence that these two coarse meshes are mechanically unsuitable, not an exclusion of finer/adaptive meshes, a different sampling phase, tangent-H constructions, critical-point patching or altered analytic profiles.

## 7. Open construction question

The finite target remains strict110/additionalweak000 with E<=249. A useful continuation must adapt geometry to BOTH radial landscapes and actual mass. Uniform visual fidelity or Hausdorff closeness is not by itself an equilibrium certificate. For any positive physical escape i->j,

|p_j-c|^2-|p_i-c|^2 > |p_j-p_i|^2,

so the modest radial change has to pay for the actual chord length. Fixed phase parameter lines can be very badly aligned with the physical radial gradient because the sections rotate. A dedicated apex patch near U and a single flat stable carrier near S may be necessary, together with sparse flow-aware edges elsewhere and a controlled filled-moment correction. These are directions, NOT established construction theorems. The phase/amplitude/radius profile may be changed, but its mass, convexity and complete critical set then require new analysis. The CIRCLE5 theorem does not automatically transfer to those altered bodies.
