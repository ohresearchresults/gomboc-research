# material-60c094676ab0

Historical AI scientific source/proof material. Statements retain their original scope; this is not an independently reviewed theorem.

Public derivative: internal-record-identifiers-replaced.

---

# POLYSECT15_V1: smooth polynomial circular-section body and exact finite nonwinner

This is Recovery capsule part 3/3. The exact analytic object and certificate are reconstructed from part1 alone plus the literal parameters/commands below. Part2 preserves the numerical producer method separately; the accepted rational object does NOT depend on reproducing an optimizer result.

## Exact source identities and dependencies

Part1: `[internal-source-reference]`, entire polynomial_sections.py,6382UTF-8bytes,SHA256 fd75908f44737d632218471bce59d212bcd92c059a9c06e7fa96e429299931f7. This exact local source was rehashed and replayed before writing this manifest.

Part2: `[internal-source-reference]`, entire polynomial_scout.py. Its archive receipt reports2271bytes/SHA d6bd8568a4f6c0f4571c7263377bb5638b81ca948f96280ac622d9bc4e5c8865. The literal source text was read completely after storage. The local submitted UTF-8 source has2559bytes/SHA f52f21cb45f08a90580137945a6fdff80b1de4a3a24f07459b8308f768d9c4938. These metadata disagree; do not claim they were a matched hash verification. The complete literal method is preserved, but this supplementary producer transport discrepancy remains explicit. It is NOT an input dependency of the exact rational reconstruction or theorem.

For the OPTIONAL finite polyhedron only, also select the complete earlier exact auditor `[internal-source-reference]`, circle_family.py,13139bytes,SHA81988ecb6ea4601709b7c0311332a48da6f1a7cb1171b19e2aadeb9f99039c68. Its actual local bytes were rehashed before the finite replay. The CIRCLE5 explanatory proof/manifest `[internal-source-reference]` documents this auditor and can be attached for context, but is not a code dependency.

All core inputs are literal rational formulas. No originating sandbox, old worker geometry, numerical checkpoint, random seed, quadrature result or hidden optimizer state is needed. Preserve source files as UTF-8/LF without Markdown fences.

## 1. General exact polynomial-section criterion

Let y=x^2, rho(x)=sqrt(1-x^2), and choose rational polynomials P(y),Q(y). Define p(x)=P(x^2),q(x)=xQ(x^2),d(x)=(p(x),q(x)), and

K={ (x,u,v): x^2+(u-p(x))^2+(v-q(x))^2<=1 }.

The map (x,Y,Z)->(x,Y+p(x),Z+q(x)) is a global smooth bijection with Jacobian determinant1 and smooth inverse. It maps the unit ball to K and its sphere to the boundary. In particular the boundary is globally C-infinity, including the two tips. Equivalently the defining polynomial has nonzero gradient on the entire level set: away from the tips at least one of u-p,v-q is nonzero; at the tips its x-derivative is +/-2.

Every x-slice is a circular disk of radius rho with centre d(x), area pi(1-x^2). Hence filled volume is4pi/3, x and v first moments vanish by parity, and the u first moment is

4pi sum_j P_j/((2j+1)(2j+3)).

Thus the ACTUAL uniform filled-volume centroid is zero exactly when this rational sum vanishes. This is not a surface, vertex or point-mass centroid.

Define the following polynomials, where primes now denote derivatives with respect to y:

D=P^2+yQ^2,
R=(1-y)D,
T=D-(1-y)D'=-R',
W=T^2-R(D')^2,
N=2P'+4yP'',
L=6Q'+4yQ'',
J=1-(1-y)^3(N^2+yL^2).

The code calls the last polynomial K, whereas this prose calls it J to distinguish it from the solid K.

Suppose D,T,W,J are all strictly positive on the CLOSED interval[0,1], the mass sum vanishes, and 0<P(0)<1. Then the following arguments certify strict convexity and exactly one nondegenerate stable and one nondegenerate unstable equilibrium, with no extra support equilibrium.

### Strict convexity

For any transverse unit vector n, the support of the x-slice in direction n is h_n(x)=rho(x)+n dot d(x). Convexity of K is equivalent to concavity of every h_n: the required inclusion of Minkowski-interpolated disks in the intermediate disk is equivalent to all support inequalities. We have rho''=-rho^(-3), p''=N(y),q''=xL(y). Thus J>0 implies |d''|<rho^(-3), and h_n''<0 for every n throughout the interior. Strict support interpolation extends to endpoint pairs by continuity and strictness on the intervening open interval. Distinct points in the same interior slice also interpolate strictly inside its strictly convex disk, except coincident points. Therefore K is strictly convex. This argument is independent of sampled supports.

### Complete radial critical set

Because D>0, write d=sqrt(D)(cos phi,sin phi); a smooth angle can be chosen on the interval. In regular boundary coordinates x and relative angle psi=theta-phi(x),

|r|^2=1+D(y)+2sqrt(R(y))cos psi.

For |x|<1, the angular critical equation forces psi=0 or pi. Their two squared-radius branches are

f_+(y)=1+D+2sqrt R,
f_-(y)=1+D-2sqrt R.

Since T>0 and W>0, T>sqrt(R)|D'| on[0,1). Consequently

f_+'=D'-T/sqrt R<0,
f_-'=D'+T/sqrt R>0.

The radial derivative with respect to x is2x times the appropriate derivative above, so x=0 is the only remaining critical coordinate. At x=0, mixed x/psi derivatives vanish; the x Hessian entries are2f_+'(0)<0 and2f_-'(0)>0, while the psi entries are respectively -2P(0) and+2P(0). Hence the two points are nondegenerate:

U=(0,1+P(0),0), maximum;
S=(0,P(0)-1,0), minimum.

At x=+/-1, the two tips are (+/-1,P(1),+/-Q(1)). Their unique support normals are +/-e_x. D(1)>0 implies the transverse radial component is nonzero, so the tips are NOT equilibria. There are no other boundary points. A convex smooth body's support equilibrium about an interior point is exactly a boundary point with radial vector normal to the boundary, so this radial classification is the complete mechanical equilibrium classification. No extra weak or degenerate support equilibrium is hidden at a tip.

## 2. Literal POLYSECT15 exact object

Choose

P(y)=(1/15)(1-(43/6)y+(91/18)y^2),
Q(y)=(1/15)((39/10)-(70/9)y+(5/3)y^2).

The displayed formulas, together with the inequality defining K, are the whole exact body. Its defining boundary polynomial has degree10. The rational mass sum is exactly0. P(0)=1/15, P(1)=-2/27,Q(1)=-199/1350. The certificate below proves strict convexity and the complete critical classification.

Therefore this globally smooth homogeneous body has

volume4pi/3, actual centroid(0,0,0),
U=(0,16/15,0), S=(0,-14/15,0),
minimum radial distance14/15, maximum16/15, ratio7/8.

This is an ANALYTIC body, NOT a polyhedron. It has no finite V/E/F/C assigned. It does NOT meet the requested finite own110/weak000,C<500 target. No novelty or priority relative to external literature is claimed. Its purpose is a stronger, polynomial and globally smooth seed for equilibrium-aware finite construction, complementing CIRCLE5.

## 3. Exact Bernstein positivity certificates

The core uses only Python standard-library rational arithmetic. For polynomial c_0+...+c_n y^n on[0,1], it computes Bernstein coefficients

b_i=sum_{j=0}^i c_j binom(i,j)/binom(n,j).

Positive Bernstein coefficients bound the polynomial below by their minimum because the Bernstein basis is nonnegative and sums to1. Rational de Casteljau subdivision at1/2 produces exact coefficients on subintervals, recursively if required; the accepted leaves are checked to cover[0,1] without gaps. The code aborts rather than accepting an unresolved interval at its maximum depth40. No grid sampling is used for these certificates.

Exact REPLAYED certificate data:

D: degree5, ONE leaf[0,1], minimum coefficient1/225.
T: degree5, TWO leaves. On[0,1/2] minimum37/67500; on[1/2,1] minimum1361/1166400. Global lower bound37/67500.
W: degree14, TWO leaves. On[0,1/2] minimum29857/128144531250; on[1/2,1] minimum195795246145333/344373768000000000000. Global lower bound is the first value.
J(code K): degree6, ONE leaf[0,1], minimum176/2025.

The generated analytic_certificate.json includes every power coefficient and every Bernstein leaf coefficient, not only these minima. All four bounds are strictly positive. Any draft reporting two leaves for D or a different certificate hash is superseded by the exact replay here.

## 4. Exact rational boundary and support oracles

For rational t in[-1,1], put x=2t/(1+t^2),rho=(1-t^2)/(1+t^2). For rational unit direction e=(e1,e2),

r=(x,P(x^2)+rho e1,xQ(x^2)+rho e2)

is an exact rational boundary point. Write du=u-p(x),dv=v-q(x). An outward support normal is

n=(x-du p'(x)-dv q'(x),du,dv), h=n dot r.

All entries are rational. This formula also gives the correct unique axis normal at a tip. Strict convexity proves that the plane is supporting for the whole analytic body.

## 5. Deterministic exact replay

Core tested environment Python3.13.5, standard library only. The optional finite audit additionally uses NumPy2.3.5/SciPy1.17.0 through the exact circle_family.py dependency. The verifier uses no random seed, floating optimization or rounding.

Core command in a clean directory with the exact part1 source:
python polynomial_sections.py --out polysect15

Expected marker:
POLYSECT15_ANALYTIC_EXACT_PASS

Expected analytic_certificate.json:3431bytes,SHA
034c2c85c04d0c2a99db84a41eb3f966fb20d1ed97719e05cc52b8ed3dba423fe

Optional finite construction AND complete verification, with the exact circle_family.py alongside:
OPENBLAS_NUM_THREADS=1 python polynomial_sections.py --out polysect15_m5 --sample-m 5

Additional marker:
POLYSECT15_FINITE_EXACT_PASS

This finite command also regenerates the same3431byte analytic certificate. Expected finite files:
finite_input.json:3612bytes,SHA ac7e682138504a394c9a7ffbcfc7a6f59a9af780b9ed580aee5147b856247cb0
finite_audit.json:164144bytes,SHA 9ba8658f4115cb374e3634d48ba18d8e84f354df2bd0108f73d12702556c113e

Verification command:
sha256sum polynomial_sections.py circle_family.py polysect15_m5/analytic_certificate.json polysect15_m5/finite_input.json polysect15_m5/finite_audit.json

The exact core source/input recipe regenerates all bytes; hashes identify outputs but do not replace the source. The fresh exact replay used for this manifest was named replay_polysect15_m5 locally; output directory names are not included in generated JSON, so the commands above give the identical file bytes.

## 6. Finite exact negative control: POLYSECT15_FIXED_M5

The command uses t=j/5,j=-5,...,5, one copy of each tip, and the following eight fixed transverse directions on each of the nine interior slices:
(1,0),(3/5,4/5),(0,1),(-3/5,4/5),(-1,0),(-3/5,-4/5),(0,-1),(3/5,-4/5).

The sorted rational cloud has74 points, all hull vertices. Its actual maximal hull is

V74/E152/F80,C304,
strict(S,U,H)=(68,74,140),additionalweak000,primitivezero000.

Its ACTUAL filled-volume centroid is
(0,-113751104631883625359/5352082146637566842250,0),
NOT the analytic body's zero centroid. All74 vertices are unstable even after its own mass is used. The slight improvement in analytic radial resource therefore does not make this coarse grid mechanically suitable.

The exact auditor reconstructs maximal supporting planes and polygons, true edges and their two owners, oriented closed connected boundary and Euler relation; Qhull only nominates triples, all supports/closure are checked exactly. Mass is computed using two tetrahedral origins and independent coordinatewise divergence volume/moment identities. Vertex outgoing signs, same-centre polar facet signs plus independent physical face-foot tests, and every true-edge orthogonal-foot/normal-cone sign are all audited. Primitive zero and actual additional weak equilibria are distinguished. Both complete radial chord-min landscapes, with simultaneous tied-death events, whole dying components/cuts and attaining paths, are emitted.

This exact control is a material NONWINNER, not110, not an improvement of the accepted C622 own110, and not an exclusion of all adaptive meshes/tangent-H bodies/critical-point patches based on POLYSECT15. Any draft giving this same identity the tuple(60,74,132), a near-zero centroid, or different output hashes is superseded by the literal exact replay in Sections5–6. In particular the analytical moment identity must never substitute for the sampled hull's integrated moment.

## 7. Numerical producer, exact rationalization and open directions

The preserved scout optimizes a rational-mass-compatible polynomial SHAPE, with P_shape(0)=1, the final P coefficient solved from the exact linear mass weights, independent Q coefficients, and amplitude a. It initializes by a least-squares fit to cos(kx),sin(kx)/x for the root sin k-k cos k=0 in(4,5). Its complete code specifies2001 initialization nodes,1601 y constraint nodes,100001 diagnostic nodes, SLSQP bounds/tolerances and degree choices2,3,4,5. It is a finite floating search, NOT a global optimum or exact positivity proof. Dense minima may miss violations between nodes.

The locally recorded degree2 nomination had a approximately0.06831354205112987,P_shape approximately[1,-7.171315288997593,5.066402340994384],Q_shape approximately[3.9037002254905495,-7.777802498898008,1.6711427242380485]. These floating values explain the manual choice of the exact displayed P,Q and a=1/15; they are not reconstruction input. Higher-degree nominal amplitudes around.06846,.07188,.07310 are unverified floating nominations and are not accepted new analytic bodies. Optimizer repeatability is not used by any exact claim in this capsule.

The main remaining problem is finite mechanics: positive physical escape i->j must satisfy |r_j-c|^2-|r_i-c|^2>|r_j-r_i|^2. Sparse coarse meshes can have chords too long relative to radial growth; simply copying a visually smooth shape creates many local polyhedral roots. Dedicated stable/unstable critical patches, physical-gradient-aware edges, nonuniform sampling and exact filled-moment correction remain open. Varying the circular radius profile or the polynomial centre is also a legitimate analytic extension, but requires rebuilding its mass, convexity and complete critical-set proof. The present theorem is a concrete seed, not a general discretization theorem.
