# minimum-0023

Historical AI scientific report · saved 2026-09-08 UTC. Claims below retain their original status and have not all been independently checked. The current retained construction is C622; the C<500 search remains open.

Public text derivative: internal-record-identifiers-replaced; unreviewed-encoded-blocks-omitted.

---

# C32_COMMON_MASS_VARIANCE_KERNEL_V1

## Determination and scope

This handoff does **not** establish V>=10, exclude every C32 realization, or produce a mono-unstable nine-vertex body. The incoming bracket remains **32<=C_min<=1374**. The accepted facet theorem makes C32 exactly the domain (V,E,F)=(9,16,9). The immutable parent `minimum-0018`, SHA-256 `6cf9fc49b54422dfbb5fe94da715e19c4f5c6e588ab632df7137d218ea68a8a3`, closes only its stated C30/map51318223/U8 class. I found no new literal-parent conflict and used neither the unauthenticated six-tree residue nor further C30 root enumeration. The parent's historical lower bound is superseded, not a definition of the present boundary. :contentReference[oaicite:0]{index=0} :contentReference[oaicite:1]{index=1}

The substantive outputs are:

1. **An actual-moment Krylov obstruction for four-dimensional PSD common kernels.** It replaces unrestricted rank-three coordinate searches inside such a kernel by a 4x4 eigenvector problem. A rational row-space identity can exclude every realization, including repeated-eigenvalue, singular-projection, and zero-volume boundary strata. A complete exact certificate below closes one explicitly specified, genuinely movable-corner C32 family over its entire unbounded domain, not a metric box.
2. **An all-shape C32 variance dichotomy.** For every nonpyramidal C32 body, two physically available triangulations differing by one quadrilateral flip have between-tetrahedron covariance matrices with trivial common kernel. For an octagonal pyramid the exceptional normal line survives every vertex-only tetrahedralization. This is a statement about physical moment rank, **not** by itself an equilibrium exclusion.
3. **A sharp actual homogeneous control.** A nonpyramidal, exactly own-centred C32 body has two different physical integration apices whose genuine decompositions have the same rank-two between-tetrahedron covariance. Its complete own-centroid class is **(5,2,5)**, not a winner. A single alternate cap triangulation makes that covariance positive definite while leaving the actual full covariance unchanged. Thus positive volume, nonpyramidality, and two apices do not automatically eliminate the variance kernel.

The published quadratic-shadow/SDP method is relevant methodological background; the source reviewed for that background proves the published seven-vertex lower bound, not the stronger incoming project bounds. The new statements here are proved below and their exact finite component is reconstructed by the capsule. Historical priority is not asserted. :contentReference[oaicite:2]{index=2}

## 1. Physical moments, with no independent row weights

Let P be a full-dimensional convex 3-polytope, uniformly filled, translated to its actual volume centroid 0. Let C=E[xx^T] be its actual covariance. All vertex vectors below refer to this one body. A physical metric M is any positive-definite 3x3 matrix. PSD certificate matrices on vertex-index space are a different object; allowing those matrices to be singular does not turn a singular physical metric into an admissible body.

Fix a vertex a. Triangulate every maximal facet not containing a, using only its actual vertices, and cone the triangles to a. These tetrahedra have disjoint interiors and cover P. Their integration diagonals are never silently treated as true mechanical edges. Here is a useful completeness proof. Choose a linear functional strictly exposing a and a sufficiently close transverse section of its tangent cone. Radial projection from a maps the facets not containing a onto a subdivision of that convex polygon; an interior ray has exactly one terminal boundary point. Their triangulations therefore have an edge-connected dual graph. Every other vertex occurs: otherwise all facets incident with that vertex would contain a, contradicting that their intersection is that vertex alone.

For each consistently oriented tetrahedron T=(a,i,j,k), put

```
d_T = det(v_i-v_a,v_j-v_a,v_k-v_a) > 0,
D   = sum_T d_T = 6 Vol(P),
w_T = d_T/D,
s_T = v_a+v_i+v_j+v_k,
Gamma_Tfamily = sum_T w_T s_T s_T^T.
```

The four barycentric coordinates of a uniform tetrahedron satisfy E[lambda_i]=1/4, E[lambda_i^2]=1/10, E[lambda_i lambda_j]=1/20 for i!=j. These follow by integrating monomials on the standard simplex; equivalently the integral of the product of powers is proportional to the product of the factorials. Affine change of variables gives, exactly,

```
sum_T w_T s_T = 0,
20 C = sum_T w_T [s_T s_T^T + sum_(i in T) v_i v_i^T].       (1)
```

Thus Gamma is sixteen times the covariance of the actual tetrahedron centroids. It is **not** the covariance C of all material. Every apex and every valid triangulation gives the same C in (1), with its own determinant masses. No mass is independently adjustable.

Writing E_T for the sum of the six edge-difference outer products of T gives another exact identity:

```
80 C = 5 Gamma + sum_T w_T E_T,
E_T = sum_(i<j in T) (v_i-v_j)(v_i-v_j)^T.                 (2)
```

Indeed, for four vectors, E_T=4 sum v_i v_i^T-s_T s_T^T. Each E_T is positive definite because a positive-volume tetrahedron has three independent edge directions. Consequently the within-tetrahedron term in (2) is positive definite even when Gamma is singular. For every nonzero PSD 3x3 test matrix H, its trace pairing with that within-tetrahedron term is strictly positive. This is a strict positive-volume statement, with no uniform margin or conditioning assumption.

A related complete equality classification is useful. Define Lambda_ai as the total actual mass of a-apex tetrahedra whose base contains i. Then Lambda_ai>0 for every i!=a, sum_i Lambda_ai=3, and sum_i Lambda_ai v_i=-v_a. Expansion of (1) yields

```
20(C-v_a v_a^T/15)
 = Gamma + sum_(i!=a) Lambda_ai (v_i+v_a/3)(v_i+v_a/3)^T.   (3)
```

The kernel of the right side is exactly the annihilator of all v_i+v_a/3, i!=a: those vectors already span every s_T. Its rank is at least two. It has rank two exactly when the other vertices are coplanar, that is, when P is a pyramid with apex a; otherwise it is positive definite. Since C is positive definite, (3) also gives

```
v_a^T C^(-1) v_a <= 15,
```

with equality exactly in that pyramid case. This inequality is supplied with an elementary proof, not claimed as historically new.

## 2. Rank and flip theorems for actual between-cell variance

### 2.1 A single fan has rank at least two once V>=8

Let L be the image of Gamma, of dimension r. Because all masses are positive, L is the span of the vectors s_T. Adjacent base triangles replace just one vertex, so the difference of the two replaced vertex vectors belongs to L. Start with one base triangle and traverse the connected triangle-dual graph. Every non-apex vertex is therefore in one of at most three affine translates of L.

If r=0, there are at most three distinct non-apex vertices. If r=1, each of those three lines contains at most two extreme points of P: a third distinct collinear point would lie between two others and would not be extreme. Thus r<=1 implies V-1<=6. Consequently

```
V>=8  ==>  rank(Gamma)>=2                                (4)
```

for **every** physical vertex-apex triangulation. This rules out rank-zero and rank-one strata; it does not rule out rank two.

### 2.2 One physical quadrilateral flip gives the exact common kernel

Suppose a maximal facet F not containing a has cyclic vertices b0,b1,b2,b3,...,b_(m-1), m>=4. Take a fan from b0. Form a second triangulation by replacing

```
(b0,b1,b2), (b0,b2,b3)
```

with

```
(b0,b1,b3), (b1,b2,b3),
```

leaving every other cap triangle unchanged. The quadrilateral is strictly convex, so both are actual positive-volume decompositions of the same body.

Let W0,W1 be their tetrahedron-sum incidence matrices: one row has four entries 1 at the tetrahedron's vertices and zero elsewhere. Then the following **incidence identity** holds:

```
ker([W0;W1]) = span(kappa_a),
(kappa_a)_a=-3,  (kappa_a)_i=1 for i!=a.                   (5)
```

Proof: a scalar vector killed by both matrices has zero sum on all four tetrahedra surrounding the flipped quadrilateral. Subtracting these four equations makes its four b-values equal, say c, and its a-value -3c. The remaining triangles in the facet fan give the same value at every other F vertex. Propagating across the connected cap-triangle dual gives that value at every non-apex vertex. The converse is immediate.

Since positive weights do not alter a Gram-sum kernel, (5) proves

```
ker(Gamma0+Gamma1)
 = {u : u.v_i=c for every i!=a, and u.v_a=-3c}.            (6)
```

For a nonpyramid this kernel is zero; for a pyramid with apex a it is exactly its base-normal line. Thus Gamma0+Gamma1 is positive definite precisely in the nonpyramid case under the stated cap-flip hypothesis. This includes every exceptional physical rank stratum, rather than assuming a numerically positive smallest eigenvalue.

For C32, sum_F(|F|-3)=2E-3F=5. There is a nontriangular maximal facet, and an apex outside it. Therefore (6) supplies a physically available positive-definite combined variance for **every nonpyramidal C32 realization**, without cataloguing graphs. The pyramid alternative is necessarily an octagonal pyramid. In any positive tetrahedron using its vertices, there is one apex and three base vertices. Their centroid lies in the plane through the solid's centroid parallel to the base. Hence every vertex-only tetrahedralization has the same normal-line variance kernel; (4) makes its rank exactly two. No number of alternative vertex-only apices removes this exception. Formula (2), not an assertion that between-cell variance is always PD, retains strict material variance there.

### 2.3 The flip update is indefinite, not a PSD improvement

For a convex quadrilateral write its diagonal intersection as

```
r b0+(1-r)b2 = s b1+(1-s)b3,  0<r,s<1.
```

Let mu be the actual volume fraction of its pyramid with apex a. The two old tetrahedra have conditional weights 1-s,s, the two new ones 1-r,r. They have the same conditional centroid. The elementary two-point variance formula therefore gives

```
Gamma1-Gamma0 = mu [r(1-r)(b0-b2)(b0-b2)^T
                    -s(1-s)(b1-b3)(b1-b3)^T].            (7)
```

The diagonals are independent, so this update has inertia (+,-,0). The corner term in (1) changes by its negative; C stays exactly unchanged. One must use a sum/common-kernel argument, not a false Loewner-monotonicity assertion.

For a PSD test metric H, tr(H Gamma)=0 exactly when image(H) is contained in ker(Gamma). At nine vertices a single Gamma has rank two or three, so a nonzero annihilating H can only have rank one. For a nonpyramidal flip pair even that rank-one exception disappears. For an actual PD physical metric every nonzero Gamma has positive trace. These statements cover arbitrary condition numbers; they assert no uniform spectral gap.

## 3. New four-dimensional-kernel actual-moment obstruction

### 3.1 From a PSD certificate to a physical coordinate subspace

Suppose justified weak forms f_i<=0 and strict actual-mass forms h_j<0 give, on each tetrahedron, a PSD index matrix Q_T with

```
<Q_T,Gram_M(v)> = <c,s_T>_M
                   + sum_i lambda_Ti f_i + sum_j eta_Tj h_j,
lambda_Ti,eta_Tj >=0,
```

where c is one common linear combination of the vertices. Multiply by the actual positive d_T and sum. The common first moment makes the first term zero. The sum is both nonnegative and nonpositive. Any positive strict-form multiplier gives an immediate contradiction. Otherwise every PSD pairing is zero, so all coordinate columns lie in K=intersection_T ker(Q_T). Factor M to justify this implication; because M is invertible, it is the same coordinate-column subspace before and after factoring.

A full-dimensional centred body has coordinate rank three. Besides the old dim(K)<=2 exclusion, positive volume requires rank(D_T B)>=3 for every actual tetrahedron, where B is a basis matrix for K and D_T takes its three edge differences. Equation (4) requires rank(W B)>=2; equation (6) requires rank([W0;W1]B)>=3 in the nonpyramid case. These are exact necessary projection-rank tests, not feasibility certificates when they pass. The parent supplement described the basic PSD/common-kernel alternative but did not close another root from it. :contentReference[oaicite:3]{index=3}

The next result deals completely with the **mass and incidence** part when dim(K)=4, retaining all exceptional strata.

### 3.2 The moment eigenvector theorem

Let B be any real n-by-4 matrix of rank four; rational B gives rational certificates. Write a candidate coordinate matrix as X=B Z, with Z a 4-by-3 matrix of rank three. Number its four rows 0,1,2,3, and define

```
p_i = (-1)^i det(Z with row i deleted).
```

Then p!=0 and ker(Z^T)=span(p). Conversely every nonzero real p is obtained this way: choose a basis of p-perpendicular and rescale one column to obtain exactly the prescribed cofactor vector.

Fix one actual oriented tetrahedralization of the prescribed face lattice. For T=(a,b,c,d), let L_T be the 3-by-4 matrix with rows B_b-B_a,B_c-B_a,B_d-B_a. Define its alternating cofactor column l_T, and its lifted vertex-sum column b_T, by

```
(l_T)_i = (-1)^i det(L_T with column i deleted),
b_T = B_a^T+B_b^T+B_c^T+B_d^T,
ell = sum_T l_T^T,
A   = sum_T b_T l_T^T.                                   (8)
```

Cauchy-Binet and the actual tetrahedron centroid formula give

```
d_T = l_T^T p,
D = ell p,
4D g(P) = Z^T A p.                                      (9)
```

No independent tetrahedron weights occur in (8)-(9). Thus, on the strict geometric realization domain,

```
g(P)=0  <==>  A p=lambda p for some real lambda.           (10)
```

This is an exact 4x4 eigenvector problem, not a numerical surrogate for the original quartic moments.

The geometric domain can also be stated completely in p. For any ordered quadruple use its cofactor row as above, so its oriented determinant is linear in p. For each prescribed facet choose its first three cyclic vertices: require zero determinants for all other incident vertices, and strictly positive inward-apex determinants for every nonincident vertex. For each consecutive pair i,j of that facet and each other facet vertex k, require det(v_i-v_o,v_j-v_o,v_k-v_o)>0 with a fixed o outside the facet. These linear inequalities enforce strict convexity and the prescribed cyclic order. Together with the oriented facet sphere they make those facets the complete hull; include d_T>0 explicitly. This is a finite homogeneous polyhedral cone with linear equalities in p.

Consequently the full mass/incidence question in K is decidable by intersecting that cone with **every real eigenspace** ker(A-lambda I). The characteristic polynomial has degree at most four. Repeated eigenvalues require their entire eigenspaces, not one sampled eigenvector; generalized eigenvectors do not satisfy (10). Zero eigenvalues are retained unless their actual volumes vanish. Normalize ell p=1 and use exact strict linear feasibility on each eigenspace. This leaves coordinates unbounded and does not discard any positive-volume scale. Once a mass/incidence class survives, its physical SPD mechanical problem still has to be solved; (10) is not a mono-unstable certificate by itself.

### 3.3 A rational Krylov row identity is already a complete exclusion certificate

Let Q consist of necessary facet-coplanarity rows, so Qp=0. Every centred realization also satisfies Q A^j p=0 for all j by (10). Therefore

```
ell in row-span[Q; Q A; Q A^2; Q A^3]                    (11)
```

forces D=ell p=0 and excludes **every strict positive-volume realization in K**. A displayed rational row combination is a complete certificate. Cayley-Hamilton explains why further powers do not enlarge this row space. Failure of (11) is not feasibility: one must still test all real eigenspaces and strict geometry, including Jordan-degenerate cases.

The construction is basis-independent. Under B->B G with invertible 4x4 G, the cofactor coordinate becomes p'=(det G)^(-1)G^T p, while

```
A'=(det G) G^T A G^(-T),
ell'=(det G) ell G^(-T),
Q'=(det G) Q G^(-T).
```

Thus the eigenvector condition and row-space obstruction are unchanged. All physical SPD metrics, including unbounded ones, are covered because they are invertible right changes of the three coordinate columns.

For dimensions <=2 use rank; for dimension three check the single affine-equivalence class and its actual centroid; for dimension four use (8)-(11). No claim is made that this settles kernels of dimension five or higher.

## 4. Exact whole-continuous C32 corner-family exclusion

Use the nine raw vertices X_i defined in Section 5. Put

```
o=(1/10,1/4,0),
W_i=X_i-o,
B_i=(W_ix,W_iy,W_iz, 1 if i=2 else 0).                    (12)
```

**Theorem C32_K4_CORNER_MASS_UNSAT_V1.** There is no rank-three real Z for which the nine rows of BZ realize the complete C32 facets listed below and have uniform-volume centroid 0. There are no coordinate-size, condition-number, or connected-component restrictions. Singular upper 3x3 blocks of Z are included; only a genuinely zero-volume final body is inadmissible.

This is not an empty geometric class. Z consisting of I3 followed by a zero row gives W, whose reference origin is strictly interior. With an invertible upper block, the family consists of arbitrary invertible linear images plus motion of vertex 2 in its sole quadrilateral facet plane. Small motions give a genuine two-dimensional shape family. The theorem excludes centring throughout the **entire** strict realization domain, not merely that small neighbourhood. It is not a closure of the unrestricted C32 graph or a proof that a mechanical SDP has already forced this K.

Take the six oriented tetrahedra

```
(0,1,3,2), (0,1,4,3), (0,1,5,4),
(0,1,6,5), (0,1,7,6), (0,1,8,7).
```

All lifted facet-coplanarity constraints except one vanish identically. The remaining row is a nonzero multiple of q=(24,10,1,0). Directly from (8),

```
A = [[4950/169, -11880/169, 0, -1316364600/62748517],
     [-2000/169, 4800/169, 0, -3112849000/62748517],
     [0, 0, 0, 0],
     [250/13, -600/13, 0, -250/13]],
ell = (250/13,-600/13,0,-1500/13).
```

The complete rational certificate is

```
ell = (1127646687245/21240202792248) q A
       -(34576660625/42480405584496) q A^2.                (13)
```

Equations q p=0 and Ap=lambda p annihilate both terms, hence D=0, contrary to positive volume. This proves the whole stated family theorem. The exceptional invariant subspace is not silently dropped: [q;qA;qA^2] has rank three and kernel span((-12,-5,338,0)); A kills that vector and ell kills it as well. The only remaining algebraic direction has zero signed volume.

The capsule additionally tests the centred affine lift B_i=(v_i,1). There A=diag(0,0,0,-6000/13). Its three-dimensional zero-eigenvalue space has zero volume, whereas the fourth eigenline gives the correct actual centred body. This checks both a surviving physical stratum and a repeated-eigenvalue boundary stratum; it is not evidence from a finite eigenvector sample.

## 5. Exact physical C32 control and the implication it refutes

### 5.1 Generator, whole rational family, and physical decomposition

For the exact control set t=1/5, c=12/13, s=5/13, H=25. Start (x0,y0)=(1,0), and use

```
(x_(k+1),y_(k+1))=(c*x_k-s*y_k, s*x_k+c*y_k),
X0=(0,0,H), X1=(0,0,-H),
X_(k+2)=(x_k,y_k,(-1)^k),  k=0,...,6.                    (14)
```

There is also a complete continuous rational family: take any real 0<t<1/4 and replace c,s,H by (1-t^2)/(1+t^2), 2t/(1+t^2), 1/t^2. If theta=2 arctan(t), then 0<6theta<pi. The supporting planes are the two vertical sector planes; the three planes with normals (2u_k,1-c), k=1,3,5, support 1+c; the two planes with normals (2u_k,c-1), k=2,4, support 1+c; and the two end planes with normals ((H+1)u_k,-1), k=0,6, support H. Here u_k=(x_k,y_k). The vertical outward normals are (0,-1,0) and (-y6,x6,0), with support zero.

For the same parity the support checks reduce to cos(delta)<=1; for opposite parity they reduce to cos(delta)<=c, with equality only at the indicated neighbours. Since the angular span is less than pi, every unlisted contact is strict. The displayed contacts are convex triangles/quadrilaterals, and their edge-paired closed sphere already supplies both incident facets at every edge, so there are no additional hull facets. The determinants of (X0,X1,X_(k+2),X_(k+3)) have absolute value 2Hs>0. These are genuine cap-fan tetrahedra, not an assumed tetrahedral cover.

All six tetrahedra have actual weight 1/6. Consequently

```
Vol(P)=2Hs=4/[t(1+t^2)],
g_z=0,
g_xy=(1/24) sum_(k=0..5)(u_k+u_(k+1)).
```

Translate by this true centroid. All six s_T then have z-coordinate zero, while their six XY values are distinct points on a circle after translation and span a plane. Both apex 0 and apex 1 use exactly this same physical six-tetrahedron decomposition. Their Gamma matrices have rank two and common kernel span((0,0,1)). The body is not a pyramid.

This refutes the proposed implication **nonpyramid + positive volume + two actual apices => trivial between-cell-variance common kernel**, even on C32, and through a continuous family with H unbounded as t approaches zero. For the rank-one PSD test H=diag(0,0,1), even the paired Jensen variance is exactly zero. This does not contradict the parent's PD-only strictness. It does **not** refute an implication that additionally assumes U=1.

Indeed this Euclidean family has U=2. Since |g_xy|<1/2 and H>16, every even rail vertex escapes strictly to X0 and every odd rail vertex to X1: its escape product is H-2+g_xy.u_k>0. These are true edges. At both apices every incident support is positive, bounded below by H(H-1)-1/2 for rail comparisons, and their mutual support is 2H^2. Thus the tied-radius apices are both strict unstable vertices. Invertible linear images preserve the rank counterexample; their equilibrium classes are not asserted to remain unchanged under arbitrary metrics.

### 5.2 Literal exact own-centroid audit at t=1/5

At this parameter,

```
Vol(P)=250/13,
g=(702075/4826809,20706125/57921708,0),
v_i=X_i-g.
```

The complete outward maximal facet cycles, in permanent facet order, are

```
F0=(0,1,2)       F1=(0,8,1)
F2=(0,2,3,4)     F3=(0,4,5,6)     F4=(0,6,7,8)
F5=(1,3,2)       F6=(1,5,4,3)     F7=(1,7,6,5)
F8=(1,8,7).
```

The sixteen true edges are

```
(0,1),(0,2),(0,4),(0,6),(0,8),
(1,2),(1,3),(1,5),(1,7),(1,8),
(2,3),(3,4),(4,5),(5,6),(6,7),(7,8).
```

The exact full covariance is

```
C = [[21940641731431/232980851224810,
      -2044448737397/93192340489924, -28083/24134045],
     [-2044448737397/93192340489924,
      165002374158815/3354924257637264, -165649/57921708],
     [-28083/24134045, -165649/57921708, 313/5]].
```

The original common-apex Gamma is

```
[[27212984340625/23298085122481,
  -9919144944500/23298085122481,0],
 [-9919144944500/23298085122481,
  61832765725400/209682766102329,0],
 [0,0,0]].
```

Flip cap quadrilateral (1,5,4,3), replacing tetrahedra with vertex sets {0,1,3,4},{0,1,4,5} by {0,1,3,5},{0,3,4,5}. The other four tetrahedra are unchanged. The new determinant masses are respectively 6000/169 and 500/169; the unchanged ones are 250/13. Formula (7) has mu=1/3,r=1/13,s=1/2. The new Gamma is

```
[[26907177029621/23298085122481,
  -9069047343420/23298085122481,952/2197],
 [-9069047343420/23298085122481,
  59208550342325/209682766102329,960/2197],
 [952/2197,960/2197,16]].
```

Its determinant is 497471479250000/209682766102329>0 and all leading principal minors are positive. The determinant of Gamma0+Gamma1 is 2089830066500000/209682766102329>0. Both decompositions reproduce the **same** C and zero first moment exactly. In the full family the new z-variance is 4c/[3(1-c)]>0, and the unchanged tetrahedron sums already span the XY plane, so the new Gamma is PD throughout that family as well.

The exhaustive own-centroid equilibrium ledger is

```
Stable facets:       F0,F1,F3,F6,F7.
Unstable vertices:   0,1.
Saddle true edges:   (0,1),(1,2),(1,8),(4,5),(5,6).
(S,U,H)=(5,2,5);     S+U-H=2.
```

All 128 primitives in the primary face/vertex/four-component-edge ledger are nonzero. Using the generated primitive integer outward planes, the minimum nonincidence slack is 7800. The minimum positive equilibrium primitive and minimum magnitude of the selected negative exclusion witness are, respectively,

| Features | Included minimum | Excluded-witness minimum |
|---|---:|---:|
| Faces | 862765/156 | 17782805/26 |
| Vertices | 2896787475/4826809 | 111718682/4826809 |
| Edges | 5/1390120992 | 96011393/1071987632617824 |

These raw margins have their stated normalization; they are not presented as invariant distances.

The primary audit reconstructs all supporting triples and maximal facets, integrates from an interior point, and checks the face projection, every true-neighbour vertex support, and all four edge-cone components. A separate analytic-H reconstruction enumerates all 84 plane triples, proves boundedness by a strictly positive spanning relation, and obtains exactly the same nine vertices. It checks faces with all normalized facet poles, vertices against all other vertices, and edges using the strict primal and dual segment-foot parameters. The latter uses polarity only for feature geometry at the same specified origin, never an assumption about the polar's volume centroid. Signed-origin integration and all nine actual apex integrations agree with the first integration.

The pyramid equality fixture is also exact and fully audited by the capsule: base z=-1 with XY vertices

```
(1,0),(3/5,4/5),(0,1),(-3/5,4/5),
(-1,0),(-3/5,-4/5),(0,-1),(3/5,-4/5),
```

and apex (0,0,3). Its volume is 56/15, centroid 0, covariance diag(223/1750,247/1750,3/5), and class (9,9,16). Every vertex and every facet is an equilibrium and every true edge is a saddle. Every apex fan has rank-two Gamma with the same vertical kernel, and C-v_apex v_apex^T/15 has rank two. This is an equality-stratum check, not a monostatic construction.

## 6. What was tried, limits, and continuation

I replaced the tentative inference from full material covariance to PD between-tetrahedron variance by an explicit actual-mass construction. The resulting counterexample exposed the missing distinction between C and Gamma and led to the exact flip update and the complete C32 pyramid/nonpyramid dichotomy. I then followed the common-kernel route beyond the parent's dimension-at-most-two test: four-dimensional coordinate kernels admit the actual-moment eigenvector reduction, and the displayed rational Krylov identity yields an exact whole-family exclusion with a surviving zero-volume algebraic kernel. Finite metric/SDP locator attempts supplied no additional certified mechanical exclusion and are not evidence for the bound.

The most useful continuation is to retain PSD certificates with kernel dimension four rather than insist on shifted PD. Recover their exact rational kernel B, construct A and ell from an actual cap tetrahedralization, form all facet-coplanarity rows Q, and test (11). If it fails, enumerate every real eigenspace and its entire strict geometry cone. Simultaneously use the physically available cap-flip pair to test projected variance rank, treating octagonal pyramids through their explicit normal-line exception and within-tetrahedron variance. A passing moment/incidence test still requires the same-metric mechanical inequalities. Weak escape equalities are permitted: with M positive definite, v_i.(v_j-v_i)_M>=0 implies N(v_j)-N(v_i)>=N(v_j-v_i)>0, so norm ties do not invalidate the escape-tree implication. No finite negative search, metric bound, or incomplete tree family is being promoted.

## 7. Complete deterministic recovery capsule

The theorem proofs above do not depend on a sandbox. The following single source contains every finite input and helper, including the new C32 body, complete hull/mechanics reconstruction, both physical triangulations, all nine apex moments, the analytic-H audit, the exact Krylov certificate, and the pyramid stratum. The immutable parent identity is provenance, not a required input file. The old parent source was authenticated at 15920 bytes with SHA-256 a131e4b3bfc83a4badf4783e31210fa2a5798d8b24d7d2d0592b71fceec712e2; the new control does not reuse its geometry.

Executed replay environment: **CPython 3.13.5, standard library only, assertions enabled**. Exploratory symbolic algebra used SymPy 1.14.0; the promoted certificates and inputs below require none of its code. Save the source below as `c32_mass_kernel_v1.py`, UTF-8 with LF and one terminal newline. Run

```
python3 -S c32_mass_kernel_v1.py
```

Exact source: **15812 bytes**, SHA-256 **dea16976288841caf9361815ab1812525ae8d5681f94f0e344e16f58aa5119aa**.

Canonical generated report `c32_mass_kernel_v1_report.json`: **17311 bytes**, SHA-256 **b0c363591689cd94f63a2b600e099ef6cb089f3893a36ec3791def220f63c26d**. It includes every rational coordinate, plane, primitive, tetrahedral mass, covariance and certificate matrix. Two clean-directory executions reproduced byte-identical reports. The analytic-H audit is a separate reconstruction path inside the supplied program, not a claim of external peer review.

Expected terminal markers:


[An encoded source block is omitted from this text export pending a complete content review. This passage is not a complete executable package.]


```python
from fractions import Fraction as F
from itertools import combinations
from math import gcd,lcm

def add(a,b):return tuple(x+y for x,y in zip(a,b))
def sub(a,b):return tuple(x-y for x,y in zip(a,b))
def mul(t,a):return tuple(t*x for x in a)
def dot(a,b):return sum(x*y for x,y in zip(a,b))
def cross(a,b):return (a[1]*b[2]-a[2]*b[1],a[2]*b[0]-a[0]*b[2],a[0]*b[1]-a[1]*b[0])
def det(a,b,c):return dot(a,cross(b,c))
def outer(a,b):return tuple(tuple(x*y for y in b)for x in a)
def matadd(A,B):return tuple(add(a,b)for a,b in zip(A,B))
def matscale(t,A):return tuple(mul(t,a)for a in A)
def zeros():return ((F(0),)*3,)*3

def rank(rows):
 A=[list(map(F,r))for r in rows]
 if not A:return 0
 k=0
 for j in range(len(A[0])):
  z=next((i for i in range(k,len(A))if A[i][j]),None)
  if z is None:continue
  A[k],A[z]=A[z],A[k];p=A[k][j];A[k]=[x/p for x in A[k]]
  for i in range(len(A)):
   if i!=k:
    t=A[i][j];A[i]=[x-t*y for x,y in zip(A[i],A[k])]
  k+=1
  if k==len(A):break
 return k

def hull(P):
 fs={}
 for i,j,k in combinations(range(len(P)),3):
  n=cross(sub(P[j],P[i]),sub(P[k],P[i]))
  if not any(n):continue
  h=dot(n,P[i]);s=[h-dot(n,v)for v in P]
  if all(x<=0 for x in s):n=mul(-1,n);h=-h;s=[-x for x in s]
  if not all(x>=0 for x in s):continue
  ids=tuple(i for i,x in enumerate(s)if x==0)
  assert any(x>0 for x in s)
  ds=lcm(*(x.denominator for x in n+(h,)))
  ns=tuple(int(x*ds)for x in n+(h,));g=gcd(*ns)
  val=tuple(F(x//g)for x in ns)
  if ids in fs:assert fs[ids]==val
  fs[ids]=val
 fs=dict(sorted(fs.items()))
 edges={}
 for f,g in combinations(fs,2):
  e=tuple(sorted(set(f)&set(g)))
  assert len(e)<=2
  if len(e)==2:
   assert e not in edges;edges[e]=(f,g)
 assert set.union(*(set(f)for f in fs))==set(range(len(P)))
 assert len(P)-len(edges)+len(fs)==2
 cycles={}
 for f,nh in fs.items():
  adj={i:[]for i in f}
  for a,b in edges:
   if a in adj and b in adj:adj[a].append(b);adj[b].append(a)
  assert all(len(v)==2 for v in adj.values())
  a=min(f);cy=[a,min(adj[a])]
  while True:
   b=next(i for i in adj[cy[-1]] if i!=cy[-2])
   if b==a:break
   assert b not in cy;cy.append(b)
  assert set(cy)==set(f)
  if dot(nh[:3],cross(sub(P[cy[1]],P[cy[0]]),sub(P[cy[2]],P[cy[1]])))<0:cy=[cy[0]]+cy[:0:-1]
  for a,b in zip(cy,cy[1:]+cy[:1]):
   for i in cy:
    if i not in (a,b):assert dot(nh[:3],cross(sub(P[b],P[a]),sub(P[i],P[a])))>0
  cycles[f]=tuple(cy)
 for i in range(len(P)):assert rank([fs[f][:3]for f in fs if i in f])==3
 return fs,edges,cycles

def tetra(P,ids):
 a,b,c,d=[P[i]for i in ids]
 return abs(det(sub(b,a),sub(c,a),sub(d,a)))

def fan_tri(cy):return [(cy[0],cy[i],cy[i+1])for i in range(1,len(cy)-1)]

def moment(P,cycles):
 q=mul(F(1,len(P)),tuple(sum(p[k]for p in P)for k in range(3)))
 D=F(0);B=(F(0),)*3;J=zeros()
 for cy in cycles.values():
  for ids in fan_tri(cy):
   vs=[q]+[P[i]for i in ids];a,b,c=[sub(v,q)for v in vs[1:]]
   d=det(a,b,c);assert d>0
   s=tuple(sum(v[k]for v in vs)for k in range(3))
   D+=d;B=add(B,mul(d,s));K=outer(s,s)
   for v in vs:K=matadd(K,outer(v,v))
   J=matadd(J,matscale(d,K))
 g=mul(F(1,4*D),B);C=matadd(matscale(F(1,20*D),J),matscale(-1,outer(g,g)))
 return D/6,g,C

def audit(P,fs,edges,cycles):
 S=[];U=[];H=[];deg=[];ledger={'face':[],'vertex':[],'edge':[]}
 fl=list(fs)
 for f in fl:
  n=fs[f][:3];h=fs[f][3];assert h>0
  foot=mul(h/dot(n,n),n);cy=cycles[f]
  vals=[dot(n,cross(sub(P[b],P[a]),sub(foot,P[a]))) for a,b in zip(cy,cy[1:]+cy[:1])]
  ledger['face'].append(vals)
  if min(vals)>0:S.append(fl.index(f))
  elif min(vals)==0:deg.append(('F',f))
 for i,p in enumerate(P):
  ns=sorted({b if a==i else a for a,b in edges if i in (a,b)})
  vals=[dot(p,sub(p,P[j]))for j in ns];ledger['vertex'].append(vals)
  if min(vals)>0:U.append(i)
  elif min(vals)==0:deg.append(('V',i))
 for (i,j),(f,g)in sorted(edges.items()):
  p,q=P[i],P[j];d=sub(q,p);t=-dot(p,d)/dot(d,d);x=add(p,mul(t,d))
  n,m=fs[f][:3],fs[g][:3];aa,bb,cc=dot(n,n),dot(n,m),dot(m,m);dd=aa*cc-bb*bb;assert dd>0
  r,s=dot(n,x),dot(m,x);beta=(cc*r-bb*s)/dd;gamma=(aa*s-bb*r)/dd
  assert x==add(mul(beta,n),mul(gamma,m))
  vals=[t,1-t,beta,gamma];ledger['edge'].append(vals)
  if min(vals)>0:H.append((i,j))
  elif min(vals)==0:deg.append(('E',(i,j)))
 if not deg:assert len(S)+len(U)-len(H)==2
 return S,U,H,deg,ledger

def fan_moment(P,ts):
 ds=[tetra(P,ids)for ids in ts];assert min(ds)>0
 D=sum(ds);G=zeros();B=(F(0),)*3;J=zeros();counts=[F(0)]*len(P)
 for ids,d in zip(ts,ds):
  s=tuple(sum(P[i][k]for i in ids)for k in range(3));B=add(B,mul(d,s));G=matadd(G,matscale(d/D,outer(s,s)))
  K=outer(s,s)
  for i in ids:counts[i]+=d/D;K=matadd(K,outer(P[i],P[i]))
  J=matadd(J,matscale(d/(20*D),K))
 return D/6,B,G,J,counts,ds

def mm(A,B):
 return tuple(tuple(dot(r,c)for c in zip(*B))for r in A)
def transpose(A):return tuple(zip(*A))
def leading(A):
 return (A[0][0],A[0][0]*A[1][1]-A[0][1]*A[1][0],det(*A))
def cofactor4(A):
 return tuple((-1)**i*det(*(tuple(r[j]for j in range(4)if j!=i)for r in A))for i in range(4))
def lifted_normal(B,t):
 return cofactor4([sub(B[i],B[t[0]])for i in t[1:]])
def orient(P,t):
 if det(*(sub(P[j],P[t[0]])for j in t[1:]))<0:
  t=t[:2]+(t[3],t[2])
 assert det(*(sub(P[j],P[t[0]])for j in t[1:]))>0
 return t

def apex_decomposition(cycles,a,b=None):
 out=[]
 for f,cy in cycles.items():
  if a in f:continue
  if b is not None:
   assert b in f
   k=cy.index(b);cy=cy[k:]+cy[:k]
  out.extend((a,)+t for t in fan_tri(cy))
 return out

def basic_report(P):
 fs,es,cy=hull(P);vol,g,C=moment(P,cy)
 V=[sub(p,g)for p in P];fs,es,cy=hull(V)
 assert moment(V,cy)==(vol,(0,0,0),C)
 S,U,H,deg,L=audit(V,fs,es,cy)
 assert not deg
 # A separate signed-origin boundary integration of volume and first moment.
 D=F(0);B=(F(0),)*3
 for cycle in cy.values():
  for a,b,c in fan_tri(cycle):
   dt=det(V[a],V[b],V[c]);assert dt>0
   D+=dt;B=add(B,mul(dt,add(add(V[a],V[b]),V[c])))
 assert D==6*vol and B==(0,0,0)
 assert min(leading(C))>0
 mins={}
 for typ,inds in [('face',S),('vertex',U),('edge',[sorted(es).index(e)for e in H])]:
  rows=L[typ]
  mins[typ]=dict(positive=min(x for i in inds for x in rows[i]),
   negative_witness=min(-min(v)for i,v in enumerate(rows)if i not in inds)) if len(inds)<len(rows) else dict(positive=min(x for row in rows for x in row))
 rep=dict(raw_vertices=P,centroid=g,centered_vertices=V,volume=vol,covariance=C,
  faces=list(cy.values()),planes=list(fs.values()),edges=sorted(es),
  stable=S,unstable=U,saddles=H,degenerate=deg,primitives=L,margins=mins,
  primitive_zero_count=sum(x==0 for rows in L.values()for row in rows for x in row),
  minimum_integer_plane_nonincidence=min(nh[3]-dot(nh[:3],p)for f,nh in fs.items()for i,p in enumerate(V)if i not in f))
 return V,fs,es,cy,rep

def independent_h_audit(P,V,g,cycles,edges):
 # Analytic supporting planes, not supporting-triple output.
 c,H=F(12,13),F(25);u=[p[:2]for p in P[2:]]
 ns=[(F(0),F(-1),F(0)),(-u[6][1],u[6][0],F(0))]
 ns += [(2*u[k][0],2*u[k][1],1-c)for k in (1,3,5)]
 ns += [((H+1)*u[0][0],(H+1)*u[0][1],F(-1))]
 ns += [(2*u[k][0],2*u[k][1],c-1)for k in (2,4)]
 ns += [((H+1)*u[6][0],(H+1)*u[6][1],F(-1))]
 rawh=[0,0,1+c,1+c,1+c,H,1+c,1+c,H]
 hs=[h-dot(n,g)for n,h in zip(ns,rawh)];assert min(hs)>0
 vertices=set()
 for a,b,c in combinations(range(9),3):
  d=det(ns[a],ns[b],ns[c])
  if not d:continue
  x=mul(1/d,add(add(mul(hs[a],cross(ns[b],ns[c])),mul(hs[b],cross(ns[c],ns[a]))),mul(hs[c],cross(ns[a],ns[b]))))
  if all(dot(n,x)<=h for n,h in zip(ns,hs)):vertices.add(x)
 assert vertices==set(V)
 flux=(F(0),)*3;weights=[]
 for n,cycle in zip(ns,cycles.values()):
  area=(F(0),)*3
  for a,b in zip(cycle,cycle[1:]+cycle[:1]):area=add(area,cross(V[a],V[b]))
  w=dot(area,n)/dot(n,n);assert w>0 and mul(w,n)==area
  flux=add(flux,mul(w,n));weights.append(w)
 assert flux==(0,0,0)and rank(ns)==3  # Strict positive spanning: bounded H-body.
 poles=[mul(1/h,n)for n,h in zip(ns,hs)]
 stable=[i for i,q in enumerate(poles)if all(i==j or dot(q,sub(q,r))>0 for j,r in enumerate(poles))]
 unstable=[i for i,x in enumerate(V)if all(i==j or dot(x,sub(x,y))>0 for j,y in enumerate(V))]
 fl=list(cycles);saddles=[]
 for (i,j),(f,g)in sorted(edges.items()):
  d=sub(V[j],V[i]);t=-dot(V[i],d)/dot(d,d)
  a,b=fl.index(f),fl.index(g);e=sub(poles[b],poles[a]);u=-dot(poles[a],e)/dot(e,e)
  if 0<t<1 and 0<u<1:saddles.append((i,j))
 assert stable==[0,1,3,6,7]and unstable==[0,1]
 assert saddles==[(0,1),(1,2),(1,8),(4,5),(5,6)]
 return dict(normals=ns,supports=hs,positive_spanning_weights=weights,
  triple_count=84,vertex_count=len(vertices),stable=stable,unstable=unstable,saddles=saddles)

def main():
 import hashlib,json
 from pathlib import Path
 assert __debug__
 P=[(F(0),F(0),F(25)),(F(0),F(0),F(-25))];x,y=F(1),F(0)
 for k in range(7):
  P.append((x,y,F((-1)**k)));x,y=(12*x-5*y)/13,(5*x+12*y)/13
 V,fs,es,cy,R=basic_report(P)
 expected=((0,1,2),(0,8,1),(0,2,3,4),(0,4,5,6),(0,6,7,8),
           (1,3,2),(1,5,4,3),(1,7,6,5),(1,8,7))
 assert tuple(cy.values())==expected and (len(V),len(es),len(fs))==(9,16,9)
 assert R['volume']==F(250,13)
 assert R['centroid']==(F(702075,4826809),F(20706125,57921708),0)
 assert R['stable']==[0,1,3,6,7] and R['unstable']==[0,1]
 assert R['saddles']==[(0,1),(1,2),(1,8),(4,5),(5,6)]
 assert R['primitive_zero_count']==0 and dot(V[0],V[0])==dot(V[1],V[1])
 HA=independent_h_audit(P,V,R['centroid'],cy,es)
 T0=apex_decomposition(cy,0,1);TB=apex_decomposition(cy,1,0)
 as_sets=lambda ts:{tuple(sorted(t))for t in ts}
 assert as_sets(T0)==as_sets(TB)=={(0,1,i,i+1)for i in range(2,8)}
 T0=sorted(orient(P,t)for t in T0)
 # Flip the genuine cap quadrilateral with cycle (1,5,4,3).
 T1=[t for t in T0 if set(t)not in ({0,1,3,4},{0,1,4,5})]
 T1+=list(map(lambda t:orient(P,t),[(0,1,3,5),(0,3,4,5)]))
 assert tuple(cy[(1,3,4,5)])==(1,5,4,3)
 A=fan_moment(V,T0);B=fan_moment(V,T1)
 for Z in (A,B):assert Z[0]==R['volume'] and Z[1]==(0,0,0)and Z[3]==R['covariance']
 assert A[5]==[F(250,13)]*6
 G0,G1=A[2],B[2]
 assert rank(G0)==2 and G0[2]==(0,0,0)and min(leading(G0)[:2])>0
 assert min(leading(G1))>0 and G1[2][2]==16
 assert det(*G1)==F(497471479250000,209682766102329)
 assert det(*matadd(G0,G1))==F(2089830066500000,209682766102329)
 # Radon coefficients: q=(1/13)B+(12/13)X4=(X3+X5)/2.
 r,s,mu=F(1,13),F(1,2),F(1,3)
 assert add(mul(r,V[1]),mul(1-r,V[4]))==mul(s,add(V[3],V[5]))
 d02=sub(V[1],V[4]);d13=sub(V[5],V[3])
 update=matadd(matscale(mu*r*(1-r),outer(d02,d02)),matscale(-mu*s*(1-s),outer(d13,d13)))
 assert matadd(G0,update)==G1 and rank(update)==2
 assert update[2][2]>0 and update[0][0]<0
 # Shared-covariance and within-tetrahedron identities, for every apex.
 fans=[]
 for a in range(9):
  ts=apex_decomposition(cy,a);fm=fan_moment(V,ts)
  assert fm[0]==R['volume'] and fm[1]==(0,0,0)and fm[3]==R['covariance']
  E=zeros();corner=zeros();base=zeros();D=sum(fm[5])
  for t,d in zip(ts,fm[5]):
   w=d/D
   for i,j in combinations(t,2):E=matadd(E,matscale(w,outer(sub(V[i],V[j]),sub(V[i],V[j]))))
   for i in t:corner=matadd(corner,matscale(w,outer(V[i],V[i])))
   for i in t:
    if i!=a:
     v=add(V[i],mul(F(1,3),V[a]));base=matadd(base,matscale(w,outer(v,v)))
  assert matadd(matscale(5,fm[2]),E)==matscale(80,R['covariance'])
  assert matadd(fm[2],corner)==matscale(20,R['covariance'])
  residual=matadd(R['covariance'],matscale(F(-1,15),outer(V[a],V[a])))
  assert matadd(fm[2],base)==matscale(20,residual)
  assert min(leading(E))>0 and min(leading(residual))>0 and rank(fm[2])>=2
  fans.append(dict(apex=a,tetrahedra=ts,masses=fm[5],occurrences=fm[4],gamma=fm[2],inertia_residual=residual))
 # The two triangulations' tetra-sum incidence operator has kernel (-3,1,...,1).
 W0=[tuple(F(i in t)for i in range(9))for t in T0]
 W1=[tuple(F(i in t)for i in range(9))for t in T1]
 kap=(-3,)+(1,)*8
 assert rank(W0)==6 and rank(W0+W1)==8 and all(dot(w,kap)==0 for w in W0+W1)
 # A four-dimensional kernel with a genuine two-parameter movable corner.
 # Its reference origin is strictly interior before any corner movement.
 offset=(F(1,10),F(1,4),F(0));W=[sub(p,offset)for p in P]
 wf,we,wc=hull(W)
 assert tuple(wc.values())==expected and min(nh[3]for nh in wf.values())>0
 K=[p+(F(i==2),)for i,p in enumerate(W)]
 assert rank(K)==4
 Q=[lifted_normal(K,f)for f in fs if len(f)==4]
 q=(F(24),F(10),F(1),F(0))
 assert Q[0]==mul(F(5,13),q)and all(v==(0,0,0,0)for v in Q[1:])
 EA=[[F(0)]*4 for _ in range(4)];ell=[F(0)]*4
 for t in T0:
  l=lifted_normal(K,t);s4=tuple(sum(K[i][j]for i in t)for j in range(4))
  assert dot(l,(0,0,0,-1))==tetra(P,t)
  assert all(dot(l,sub(K[i],K[t[0]]))==0 for i in t[1:])
  for i in range(4):
   ell[i]+=l[i]
   for j in range(4):EA[i][j]+=s4[i]*l[j]
 EA=tuple(map(tuple,EA));ell=tuple(ell)
 assert EA==((F(4950,169),F(-11880,169),0,F(-1316364600,62748517)),
  (F(-2000,169),F(4800,169),0,F(-3112849000,62748517)),
  (0,0,0,0),(F(250,13),F(-600,13),0,F(-250,13)))
 assert ell==(F(250,13),F(-600,13),0,F(-1500,13))
 qA=mm((q,),EA)[0];qAA=mm((qA,),EA)[0]
 coeff=(F(1127646687245,21240202792248),F(-34576660625,42480405584496))
 assert add(mul(coeff[0],qA),mul(coeff[1],qAA))==ell
 null=(-12,-5,338,0)
 assert rank([q,qA,qAA])==3 and all(dot(row,null)==0 for row in (q,qA,qAA,ell))
 assert all(dot(row,null)==0 for row in EA)
 # If Q*p=0 and EA*p=lambda*p, the row identity forces ell*p=0.
 # This contradicts the nonzero signed volume of every strict physical realization.
 # A centered affine lift tests the repeated zero-eigenvalue stratum as well.
 KC=[v+(F(1),)for v in V];EC=[[F(0)]*4 for _ in range(4)]
 for t in T0:
  l=lifted_normal(KC,t);s4=tuple(sum(KC[i][j]for i in t)for j in range(4))
  for i in range(4):
   for j in range(4):EC[i][j]+=s4[i]*l[j]
 assert EC==[[F(-6000,13)if i==j==3 else F(0)for j in range(4)]for i in range(4)]
 # Exact positive-volume C32 pyramid: the exceptional line really survives all fans.
 octagon=((1,0),(F(3,5),F(4,5)),(0,1),(-F(3,5),F(4,5)),
          (-1,0),(-F(3,5),-F(4,5)),(0,-1),(F(3,5),-F(4,5)))
 PY=[(F(x),F(y),F(-1))for x,y in octagon]+[(F(0),F(0),F(3))]
 PV,pf,pe,pc,PR=basic_report(PY)
 assert (len(PV),len(pe),len(pf))==(9,16,9)and PR['centroid']==(0,0,0)
 PG=[]
 for a in range(9):
  f=fan_moment(PV,apex_decomposition(pc,a))
  assert f[0]==PR['volume']and f[1]==(0,0,0)and f[3]==PR['covariance']
  assert rank(f[2])==2 and f[2][2]==(0,0,0)
  PG.append(f[2])
 residual=matadd(PR['covariance'],matscale(F(-1,15),outer(PV[8],PV[8])))
 assert rank(residual)==2 and residual[2]==(0,0,0)
 report=dict(version=1,name='C32_COMMON_MASS_VARIANCE_KERNEL_V1',
  parent_assignment='minimum-0018',
  parent_sha256='6cf9fc49b54422dfbb5fe94da715e19c4f5c6e588ab632df7137d218ea68a8a3',
  control=R,independent_h_reconstruction=HA,tetrahedra0=T0,tetrahedra1=T1,masses0=A[5],masses1=B[5],
  gamma0=G0,gamma1=G1,flip_update=update,all_apex_fans=fans,
  incidence_ranks=[rank(W0),rank(W0+W1)],pyramid_pattern=kap,
  kernel4_offset=offset,kernel4_basis=K,kernel4_quad_normals=Q,
  kernel4_moment_matrix=EA,kernel4_volume_row=ell,kernel4_krylov=[q,qA,qAA],
  kernel4_coefficients=coeff,kernel4_nullvector=null,
  centered_lift_moment_matrix=EC,pyramid=PR,pyramid_fan_gammas=PG,
  no_universal_V10_or_C32_exclusion=True)
 out=(json.dumps(report,default=lambda x:str(x),sort_keys=True,separators=(',',':'))+'\n').encode()
 Path('c32_mass_kernel_v1_report.json').write_bytes(out)
 print('C32_EXACT_HULL_AND_OWN_CENTROID_5_2_5_PASS')
 print('ANALYTIC_H_84_TRIPLES_AND_INDEPENDENT_FULL_AUDIT_PASS')
 print('COMMON_APEX_RANK2_AND_PHYSICAL_RANK3_FLIP_PASS')
 print('SAME_COVARIANCE_AND_INDEFINITE_FLIP_UPDATE_PASS')
 print('KERNEL_FOUR_ACTUAL_MOMENT_OBSTRUCTION_PASS')
 print('PYRAMID_EQUALITY_STRATUM_PASS')
 print('REPORT',len(out),hashlib.sha256(out).hexdigest())
 src=Path(__file__).read_bytes();print('SOURCE',len(src),hashlib.sha256(src).hexdigest())
 print('NO_V10_OR_WHOLE_C32_EXCLUSION')

if __name__=='__main__':main()
```
