# material-62c78876c1b2

Historical AI scientific source/proof material. Statements retain their original scope; this is not an independently reviewed theorem.

Public derivative: internal-record-identifiers-replaced.

---

# DEGREE7_TWO_CAP_CLASSIFICATION_AND_EXACT_POLAR_COMPLETION_V1

Coordinator original synthesis. This is a complete geometric reduction and local realization theorem, NOT an all-metric equilibrium exclusion. It leaves the accepted global interval34<=Cmin<=622 unchanged. True facets/edges, actual uniform volume centroids, and one reciprocal physical metric are used throughout. No assertion of historical priority or canonical catalogue-ID correspondence is made.

## 1. The maximal-degree sector of10/17/9 has exactly three types

Let P be a full-dimensional convex polyhedron with(V,E,F)=(10,17,9). Every vertex has degree at least3. Since the degree sum is34, no degree exceeds7. If A has degree7, it is the unique such vertex and every other vertex has degree3.

Exactly seven facets meet A. Move A to0. Their halfspaces define the full pointed tangent cone C at A, with seven extreme rays. The remaining two true facets have inequalities l_1(X)<=1,l_2(X)<=1, with l_1,l_2 linear, because A strictly satisfies both. Consequently

P=C intersect{l_1<=1,l_2<=1}.                                      (1)

Both cuts are irredundant. Boundedness supplies a positive combination z=theta*l_1+(1-theta)*l_2 strictly positive on C\{0}, with0<theta<1. Here is an elementary polyhedral justification: boundedness is equivalent to C intersect{l_1<=0,l_2<=0}={0}. If no positive combination belonged to int(C*), separation of the two polyhedral cones would provide a nonzero vector in that intersection. A combination with one zero coefficient can be perturbed to make both coefficients positive while retaining strict positivity on the compact unit section of C. Rescale the coefficients to sum1. The two l_i are independent: parallel normals with two active cuts would either leave a nonzero recession direction or make one cut redundant.

Set x=l_1-l_2 and complete(x,z) to linear coordinates(x,y,z). Let B=C intersect{z=1}, a strictly convex seven-vertex polygon. Write b=(x,y,1) and

R(b)=1/[1+(1-theta)x] for x>=0,
R(b)=1/[1-theta*x]   for x<=0.                              (2)

Then every point of P has the unique radial representation r*b, b in B,0<=r<=R(b), apart from the apex. The two cap planes are z+(1-theta)x=1 and z-theta*x=1. This is an exact chart for EVERY body in the degree7 sector, after an invertible affine change of coordinates, not merely a selected realization or a projective subclass.

The line x=0 intersects int(B), because otherwise one cap would be redundant. It contains no vertex of B: a ray with l_1=l_2 at its endpoint would give a non-apical vertex incident to both cap planes and both incident side planes, hence degree at least4, contradicting the degree count. Thus x=0 meets exactly two open polygon edges. It divides the seven polygon vertices into two contiguous, nonempty blocks of sizes k and7-k,1<=k<=6.

The complete vertex set of P consists of A, the seven points R(b_i)b_i, and the two seam endpoints where x=0,z=1 on the boundary of B. There are five triangular and two quadrilateral lateral facets. The two caps have k+2 and9-k vertices. Their unordered size pairs are exactly

(3,8), (4,7), (5,6).                                      (3)

Each block size determines the whole unlabelled graph: retain the cyclic order of the seven rays, insert one seam vertex into each transition side, and join the seam vertices by the cap-intersection edge. Reversal and cap exchange are the only changes needed to identify k with7-k. Conversely, any strictly convex B with a vertex-free crossing line and any0<theta<1 in(2) gives precisely this true lattice. The three size pairs distinguish the types, and the three exact controls below establish existence. These are three abstract degree7 types, NOT three newly excluded types or an asserted match to existing canonical IDs.

## 2. Coupled actual mass formula, not free positive cap weights

The chart Jacobian is r^2. With dA the ordinary(x,y)-area on B, put

Z0=int_B R^3 dA,
Z1=int_B R^4 b dA,
Z2=int_B R^5 b b^T dA.

Then the ACTUAL uniform body has

Vol(P)=Z0/3,
g=3 Z1/(4 Z0),
E_P[XX^T]=3 Z2/(5 Z0).                                   (4)

Both caps use the SAME polygon and kernel R. Their volume and moment weights cannot be chosen independently. More generally, for homogeneous polynomial f of degree m,

E_P f(X)=3/(m+3) * int_B R^(m+3) f(b) dA / Z0.

Geometrically P is the union of the two actual pyramids conv(A,F_+) and conv(A,F_-), with disjoint interiors and a common triangular interface conv(A,w_1,w_2). If lambda is the true first pyramid's volume fraction and c_+,c_- are the actual area centroids of the full cap facets, then

g=[A+3(lambda*c_++(1-lambda)*c_-)]/4.                      (5)

At the own-centred origin this becomes lambda*c_++(1-lambda)*c_-=-A/3. It is not legitimate to substitute the separate pyramid centroids as the reference for P's mechanics. The two pieces have(k+3,10-k) vertices:4/9,5/8,or6/7 up to exchange. Separate piece exclusions do not automatically glue at the new centroid.

For exact computation triangulate each of B intersect{x>=0} and B intersect{x<=0}. On a triangle of ordinary area a with vertices b_0,b_1,b_2, let l_i=1+alpha*x_i>0,alpha=1-theta or-theta, and w_i=b_i/l_i. Write S=sum w_i and m0=a/(l_0 l_1 l_2). Its contributions are

int R^3=m0,
int R^4 b=(m0/3)S,
int R^5 b b^T=(m0/12)(SS^T+sum w_i w_i^T).                (6)

Proof: the projective map(x,y)->(x/l,y/l) has Jacobian l^-3, and sends the triangle to the triangle with the displayed three-dimensional affine-plane vertices w_i. Its projected area is a/(l_0 l_1 l_2). Uniform triangular first and second moments give(6). This provides exact rational formulas at every rational chart point, including the seam; no quadrature or independent facet densities occur.

## 3. Every prescribed heptagonal polar face has an actual E17 completion

Let Q be ANY strictly convex heptagon in an affine plane not containing0. Write that plane as A.q=1, and use an invertible linear primal/dual chart to put A=e3 and q_i=(p_i,1). The following theorem concerns these literal seven poles, not a projectively altered alias:

There is a full-dimensional uniformly filled own-centred10/17/9 polyhedron whose seven facets incident to A have exactly these poles. It can be obtained by a sufficiently small generic cut at a base vertex of an appropriately centred heptagonal pyramid, while adjusting only its base plane to repair the ACTUAL centroid. Locally the fixed-pole completion has three free cap-plane parameters. This is a real existence theorem, not universal rationality or a uniform cut-size claim.

### 3.1 Centre the uncut pyramid with the poles fixed

For b in int(conv{p_i}), define the bounded polar polygon

C_b={y:(p_i-b).y<=1 for every i},
Phi(b)=area(C_b).

Using n=(cos phi,sin phi),h(n)=max_i p_i.n,

Phi(b)=(1/2)int_0^(2pi)[h(n)-b.n]^-2 dphi,
grad Phi(b)=3 int_{C_b} y dA,
Hess Phi(b)=3 int nn^T[h(n)-b.n]^-4 dphi >0.              (7)

The last matrix is positive definite because a nonzero linear functional does not vanish on almost every direction. The area tends to infinity as b approaches the polygon boundary: all C_b contain a common positive-radius disk, whereas in a supporting direction with h(n)-b.n->0 they contain n/[h(n)-b.n]; the convex hull of that disk and this point has unbounded area. Hence Phi has a unique interior minimizer b*, and C_b* has area centroid0. These statements follow from(7), without assuming a polar centroid equals an original centroid.

Consider the pyramid with side poles fixed at q_i=(p_i,1), apex e3, and base plane

z=-h+u.y.

Its projected base is(1+h)C_{-u}, so if c(u) is the centroid of C_{-u}, its true volume centroid is

g_y=(3/4)(1+h)c(u),
g_z=1/4-3h/4+(3/4)(1+h)u.c(u).                          (8)

At u=-b*,h=1/3 this is exactly0. All side facets are irredundant because the p_i form a strictly convex polygon.

### 3.2 The base-plane centroid Jacobian is invertible

Let a(u)=area(C_{-u}). By(7),grad a=-3a c. At c=0,

Dc=-(Hess a)/(3a),

which is negative definite. At the centred pyramid, the derivative of(g_y,g_z) with respect to(u,h) is the block matrix

[[Dc,0],[u^T Dc,-3/4]].                                  (9)

Its determinant is nonzero. Thus all three true centroid equations can be repaired using only the three base-plane parameters, while every prescribed side pole remains fixed.

### 3.3 Cut and repair without changing the literal face

Choose one simple base vertex v and a linear functional n.X strictly maximized there. For nearby(u,h), that vertex v(u,h) and its three incident edges vary smoothly. Cut by

n.X <= n.v(u,h)-epsilon, epsilon>0.

For sufficiently small positive epsilon, exactly v is removed and three new edge-intersection vertices appear. The removed region is a genuine tetrahedron with volume of order epsilon^3 and analytic moments. Those moment formulas have an analytic extension to epsilon=0, so the invertible Jacobian(9) and the implicit-function theorem give u(epsilon),h(epsilon), restoring the actual centroid to0. Their corrections are O(epsilon^3). The cut does not reach A or remove any original side facet. It changes an8/14/8 pyramid to10/17/9, retaining the seven literal side poles as the full polar face at A.

Allowing the new cut plane's two normal directions and its offset to vary gives three local completion parameters. Equivalently, the two cap planes have six local parameters and the three actual centroid equations have rank3 by(9) and continuity. The generic-cut construction is in the(3,8) type of(3); the assertion is not that the same construction covers the other two types.

The same argument for a strictly convex n-gon gives an own-centred(n+3,2n+3,n+2) completion for n>=3. For n=7 it reaches the first open E17 layer with only one new cut. In particular, excluding an arbitrary locally realizable heptagonal pole shape is NOT a substitute for a global U1/S1 incompatibility theorem.

## 4. Complete exact controls and preservation

The complete autonomous source is research material [internal-source-reference], degree7_twocap.py.txt. Save its bytes unchanged as twocap.py. Size8956 bytes; SHA25641105eaa7aafbcb22e9b402c66ab915cca01840fce0ff829c7e506e14abe35ba. It uses Python>=3.10 standard library only, executed with CPython3.13.5 and assertions enabled. No external source, seed, precision choice, optimizer or imported geometry package is required.

Inputs are literal theta=1/2 and three polygons

b_j=(j-c,j^2,1), j=-3,-2,-1,0,1,2,3,
c=-5/2,-3/2,-1/2 respectively.

Their seven ray endpoints are given by(2); their last two vertices are the exact two intersections of x=0 with the polygon boundary; vertex0 is A=0. All raw coordinates, actual centroids and moments are regenerated rather than supplied as decimal inputs. The SAME matrix

M=((13,2,1),(2,11,3),(1,3,17)), N=M^-1

is used after each body's actual centroid translation. Exact supporting-triple hull enumeration recovers all maximal facets, strict convex cycles, true edges and degrees. Apex fans from A and from the vertex-average interior point agree with each other AND with the two-dimensional integral formulas(6) for volume, centroid and full raw second moment. Formula(5) is separately checked.

The full physical census has(S,U,H)=(3,2,3),(4,2,4),(3,2,3) respectively. Every one of the68 true edge-packet primitives is nonzero in each control, so all have weak000. They are NOT110, and these particular U2 controls are NOT an all-SPD theorem for their shapes. They establish actual rational existence of each of the three incidence types and validate the exact chart/mass machinery.

Reconstruction and exact verification are the same command, rerunning all assertions:

python -S twocap.py --output twocap.json

Expected final marker:

DEGREE7_TWO_CAP_THREE_TYPES_EXACT_MOMENTS_AND_MECHANICS_PASS 34750 24f0c4b78ae320a0b981b8e81e11d54c09ddc39d398b65415e8a7cfe8976f3e0

The deterministic twocap.json is34750 bytes with the displayed SHA256. It contains every facet, edge, rational moment, metric, pole-derived edge packet and census. This source+proof pair is a complete recovery capsule; a sandbox link or output hash alone is not the record.

## 5. Scientific boundary and next question

The degree7 sector is completely represented geometrically, and local polar-face realizability is unrestricted. Neither result excludes110. The unfinished step is the coupled global mechanics of the two real cap pyramids at their COMMON actual centroid, including possible unstable roots other than A, and generic reciprocal constraints outside A's polar face. The new chart supplies shared rational moment formulas for that step and must not be confused with an actual heptagonal primal facet (for example TREE410 index13749) or with any pre-existing canonical-type number. No canonical count subtraction or stronger minimum is claimed.
