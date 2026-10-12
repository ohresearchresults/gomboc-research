# material-dcf2cf5c0aa9

AI research material · [Export notes](../catalog/coverage.md#text-records)

---

# FIRST_LAYER_23_VARIABLE_CLOSED_ATLAS_AND_REALIZATION_REGULARITY_V1

## Scientific status

Coordinator analytic result. It supplies a finite, explicitly described, compact basic-closed polynomial atlas for actual V10/E17/F9 homogeneous bodies with one strict stable facet and one strict unstable vertex, allowing additional weak equilibria. It also proves that the underlying true realization space, before mechanical inequalities, is smooth of dimension eleven after affine normalization; adding a trace-one physical SPD metric gives sixteen local continuous parameters. It does NOT decide whether any atlas cell is nonempty, does NOT remove additional weak rests, and does NOT change 34 <= C_min <= 622.

The essential issue repaired here is specific: merely weakening arbitrary guessed incidence/centroid equations can add fake collapsed labelled bodies. The present model imposes an outward supporting closed triangle cycle and actual primal/dual trees; the already accepted lower bounds then prove that no fake vertex or facet collapse occurs in this model. This does not license other naive closure relaxations.

## Inputs and relation to earlier work

1. Accepted weak-inclusive lower theorems: U=1 implies at least ten true vertices; S=1 implies at least nine true facets, for a full-dimensional homogeneous body at its actual volume centroid. The stable bound is applied to the original uniform body, NOT to an independently recentered or uniformly filled polar.
2. Stronger accepted vertex input: [internal-source-reference], NINE_VERTEX_NONZERO_PSD_REFINEMENT_COLLAR_V1, SHA256 3052074db1f19530ac423145576607e4c86366b7e45a96cf9f17f880f0aee65b. A contained labelled refinement of any actual at-most-nine-vertex uniform hull has no rooted complete weak-arrow tree under any nonzero PSD metric.
3. [internal-source-reference], TEN_VERTEX_EFFECTIVE_DELETION_GAP_AND_CLOSED_CENTROID_CYCLES_V1, contains the complete new supporting-cycle actual-centroid lemma and the statement/reference of Jeronimo-Perrucci-Tsigaridas Theorem 1. The present proof includes the geometric mechanism again where needed but does not use its extremely small deletion constant.
4. Earlier qualitative global closure theorem: [internal-source-reference], FIRST_LAYER_HAUSDORFF_CLOSEDNESS_AND_TRUE_INCIDENCE_COLLARS_V1, SHA256 9afd5508a25df68c0ea47538d87e9e064cc74e888b36361f89ce7b8cf1222232a07d. It established compactness/incidence collars under an actual joint metric atlas; it explicitly did not prove proper-110 density. The present model makes the finite closed polynomial description and several feature bounds explicit.

## 1. A rational maximum-simplex gauge and a joint SPD floor

Choose a maximum-volume vertex tetrahedron of any candidate and affinely map its four vertices to 0,e1,e2,e3, in that order. Reflect the chosen orientation of the abstract boundary if the affine map reverses orientation. Every barycentric coordinate of every other vertex has absolute value <=1 by the vertex-replacement volume test. Thus all raw vertices y_i lie in [-1,1]^3 and P contains the standard tetrahedron Delta. Require every four-vertex determinant in this gauge to have absolute value <=1. There are 210 such tetrahedra.

The actual uniform centroid transforms affinely. Transport the physical quadratic metric by affine congruence and rescale it to trace one. Never reset this metric to the identity.

A lower inradius and upper circumradius about the actual centroid g are

    r = 1/(4 sqrt(3)),       R = 2 sqrt(3),       R/r = 24.

Here every directional width of Delta is at least 1/sqrt(3): the range of {0,n1,n2,n3} for a unit normal n is at least max|n_i|. For any support direction of an actual uniform three-polytope, its centroid lies at distance at least one quarter of its width from the lower supporting plane. To prove this, cone a triangulated boundary to a vertex of maximum height in this direction. Each nonzero-volume tetrahedron has mean height at least one quarter of that maximum height, and averaging its actual positive volumes proves the claim. Hence rB is contained in P-g. The cube diameter gives P-g subset RB.

For any convex body K with rB subset K subset RB, and SPD eigenvalues lambda1>=lambda2>=lambda3, unique strict radial maximum implies

    lambda1 <= (R/r)^2 lambda2.

Proof: if lambda1 r^2 > lambda2 R^2, cut K by the plane perpendicular to a leading eigenvector through zero. In each half, the maximum of x^T M x is at least lambda1 r^2, whereas every point in the dividing plane has value at most lambda2 R^2. Each half-maximum is therefore an original vertex off that plane. It has negative radial derivative toward any different point in the same half, since strict convexity would otherwise raise the value. A nonnegative derivative toward an opposite-half point would raise the value at the intervening dividing-plane point, also impossible. Thus there is a strict unstable vertex in each half.

Apply this argument also to the actual Euclidean polar (P-g)^circ, whose radius ratio is again R/r, using the inverse of the SAME metric. Stable facets of P correspond to unstable vertices of that polar in M^{-1}; this step does not invoke the polar's volume centroid. Joint S=U=1 therefore implies

    lambda1 <= 576 lambda2,       lambda2 <= 576 lambda3,
    lambda3 >= 1/(576^2+576+1) = 1/332353.

The more conservative closed floor M >= 10^{-6} I is consequently valid for every joint candidate in this gauge. It is not claimed for U=1 alone.

## 2. Exact 23-variable system for one discrete atlas choice

Fix a labelled oriented three-connected planar polyhedral map G with V=10, E=17, F=9, an ordered four-label normalization tetrahedron, a rooted spanning tree T of its genuine primal graph and a rooted spanning tree T* of its genuine dual graph. The two trees need not be complementary. Vary all these finite choices to form the complete atlas.

Relabel the chosen tetrahedron as labels 0,1,2,3, with raw coordinates 0,e1,e2,e3. The other six vertices have eighteen real coordinate variables. Use five further variables for

    M = [[m00,m01,m02],[m01,m11,m12],[m02,m12,1-m00-m11]].

There are exactly 23 real variables.

Triangulate each oriented abstract face by its first-vertex fan. The total number of listed triangles is sum_F(k_F-2)=34-18=16. Their formal oriented boundary is zero. Define

    D = sum_triangles det(y_a,y_b,y_c),
    J = sum_triangles det(y_a,y_b,y_c) (y_a+y_b+y_c).

For each oriented face F=(a,b,c,...) use its first three vertices to define

    n_F = (y_b-y_a) cross (y_c-y_a),
    h_F = n_F dot y_a,
    H_F = 4D h_F - n_F dot J.

The basic-closed constraints are all the following:

(a) Each of the eighteen free coordinates is in [-1,1].
(b) For every four-label subset, -1 <= det(y_j-y_i,y_k-y_i,y_l-y_i) <= 1.
(c) For every one of the sixteen listed triangles (a,b,c), and every one of the ten labels l,

    det(y_b-y_a,y_c-y_a,y_l-y_a) <= 0.

(d) Each remaining vertex of each declared face is coplanar with its first three vertices:

    n_F dot (y_i-y_a) = 0.

Exactly sum_F(k_F-3)=34-27=7 such equalities suffice. Using a redundant upper count of 34 is harmless for the complexity bound below.
(e) D >= 1.
(f) All seven principal minors of 10^6 M-I are nonnegative.
(g) For each of the nine arrows i->j of T,

    P_ij = (4D y_i-J)^T M (y_j-y_i) >= 0.

(h) For every face F impose H_F >= 0.
(i) For each of the eight arrows F->G of T*,

    R_FG = n_F^T adj(M) (H_F n_G-H_G n_F) >= 0.

No division or independent inverse metric appears in these polynomial constraints. The optional H_F inequalities are retained in the count, although the proof below derives strict positivity from the other structural conditions.

## 3. Faithfulness at all closed boundary points

First, the raw hull is full-dimensional since it contains the fixed standard tetrahedron. The sixteen triangles form a geometric two-cycle and every nondegenerate triangle is outward supporting by (c). Subdividing the actual boundary into their cells, the zero-boundary condition forces its nonnegative integer covering coefficient to be constant on the connected boundary. Since D>=1, this coefficient is positive. Thus

    g = J/(4D)

is exactly the uniform centroid of the raw hull, even if some labels or initially declared faces have collapsed. Any possible multiple covering cancels in this quotient. This is an actual filled hull, not a free weighted-centroid completion.

Second, (f) makes M strictly positive definite, with trace one. Dividing (g) by 4D gives a weak-arrow tree on all ten raw labels. If the hull had at most nine true vertices, it would contradict the accepted nonzero-PSD refinement theorem, because all true vertices occur among these labels. Therefore all ten labels are distinct true vertices of the hull.

Third, any three distinct true vertices on one actual supporting plane are noncollinear; otherwise one of them would lie between the other two and would not be extreme. Hence every selected face normal n_F is nonzero. Its first fan triangle occurs in (c), so its plane really supports the hull. Constraint (d) puts every declared face vertex on that plane. Since the actual centroid is interior,

    h_F - n_F dot g > 0,       H_F > 0.

Every actual facet is covered by at least one nondegenerate cycle triangle. Each such triangle belongs to one declared coplanar face. Therefore there are at most nine actual facets. Declared faces could at this intermediate stage still be duplicate supporting planes.

Fourth, the actual polar vertices, with possible duplicate labels, are

    q_F = n_F/(h_F-n_F dot g) = 4D n_F/H_F.

They include every true vertex of the polar. Since H_F,H_G,D and det(M) are positive, the sign of q_F^T M^{-1}(q_G-q_F) is exactly the sign of R_FG. Thus (i) supplies a rooted weak-arrow tree for the actual polar in the common inverse metric.

A rooted weak-arrow tree under an SPD metric allows at most one strict unstable corner fibre: any strict unstable corner has strictly negative derivative toward every different point of the hull, so its labels cannot leave that fibre. Every such fibre would have to contain the same tree root. There is at least one strict unstable corner, since the global maximum of a strictly convex quadratic function on a polytope is at a vertex and has strictly negative outgoing derivatives. Therefore the original body has exactly one strict unstable vertex and, by the polar correspondence, exactly one strict stable facet. This reasoning does not exclude other weak rests.

Fifth, apply the accepted stable lower bound to the ORIGINAL actual homogeneous body: S=1 implies at least nine true facets. There are consequently exactly nine; all declared planes are different and are the true facets. Euler now gives E=10+9-2=17. A three-polytope has 2E vertex-facet incidences (sum of its face sizes). The declared map already supplies 34 distinct incidences, all preserved by (d). Since the actual body also has exactly 34, no extra incidence is possible. The full vertex-face incidence structure, hence the face lattice and genuine graph, is exactly G. No triangulation diagonal was used as a mechanical edge.

Conversely, any actual joint S=U=1 V10/E17/F9 body can be normalized as above. Its actual boundary fan has D=6 Vol(P)>=1. Every nonroot vertex has a genuine outgoing edge with nonnegative derivative, because otherwise it would be another strict unstable vertex. Along such arrows the quadratic norm strictly increases, so these choices form a rooted tree ending at the unique unstable vertex. The same reasoning on the actual polar supplies T*. The radius argument proves (f). Thus every actual joint body appears in at least one of these basic-closed systems.

The equivalence is therefore exact for the weak-inclusive S=U=1 class. It is not a proof that all such bodies are proper110 or that any such body exists.

## 4. Compactness and explicit polynomial feature margins

Each cell is closed by construction. The free vertices are in a cube and M is PSD of trace one, hence every variable is bounded. Each cell is compact, including cells with maximum-tetrahedron ties or mechanical zero rows.

A common safe bound on the number of defining polynomials is m<=700: 36 box bounds, 420 tetrahedron bounds, 160 triangle-support bounds, at most 34 redundant planarity equations, one D bound, seven metric minors, seventeen tree rows and nine H bounds. This sum is 684. With the seven nonredundant planarity equations it is 657. All coefficients are integers and all degrees are <=12.

Uniform l1 estimates for coordinate polynomials (constants or individual variables) are

    ||D||_1 <= 16*6 = 96,
    ||J_r||_1 <= 288,
    ||n_F,r||_1 <= 8,       ||h_F||_1 <= 24,
    ||H_F||_1 <= 4*96*24 + 3*8*288 = 16128.

Each M entry has l1 norm <=3 after eliminating m22; each adj(M) entry has l1 norm <=18. Therefore

    ||R_FG||_1 <= 9*8*18*(2*16128*8) = 334430208.

For the metric minors, each entry of 10^6 M-I has l1 norm <4*10^6, so even the determinant has l1 norm <6*(4*10^6)^3 <2^80. H=2^80 therefore bounds all coefficients of all defining polynomials. The degrees of P_ij and H_F are at most 6 and that of R_FG at most 12.

Several integer polynomial features are strictly positive at EVERY point of each nonempty cell, by the faithfulness proof:

- |y_i-y_j|^2 for any distinct labels;
- |(y_j-y_i) cross (y_k-y_i)|^2 for any three distinct labels;
- h_F-n_F dot y_i whenever i is not incident to F;
- H_F for every declared face;
- |n_F cross n_G|^2 for adjacent distinct faces;
- -P_uj for every j != u, where u is the chosen primal root;
- -R_sF for every F != s, where s is the chosen dual root.

For the last two claims, the weak tree and strict convexity make its root the unique global maximum of the corresponding quadratic norm on the distinct vertices, hence give a strict negative derivative toward each different vertex. The displayed feature degrees are <=12 and their integer coefficient heights are also <=2^80.

Apply the primary minimum theorem stated in [internal-source-reference] to each compact component, with n=23,d=12,H=2^80,m<=700. Htilde=H. The logarithm base two of its base is

    4-23/2+80+23 log2(12) < 176,

and the exponent is 23*24^23. The exact integer bound is

    176*23*24^23 = 224956767695414588990411741752983552 < 2^118.

Every listed positive feature is consequently strictly greater than

    b_* = 2^(-2^118).

The same bound applies to all cells; no count of discrete choices is needed. This is a bound on the displayed polynomial quantities in this exact affine normalization, not a claim that every unnormalized physical length or dihedral angle is at least b_*. It does not bound arbitrary four-vertex determinants, nonadjacent face-normal cross products, or nonroot mechanical rows away from zero. Those can vanish legitimately. In particular, no bound against additional weak equilibria has been proved.

## 5. No hidden singularities in true three-polytope realization equations

This separate analytic lemma is useful for future regularization and continuous optimization. Fix any actual full-dimensional convex three-polytope with a prescribed labelled face lattice. Choose a fixed interior origin o, which remains interior in a small neighborhood, and represent each facet by its normalized pole p_F satisfying

    p_F dot (y_i-o) = 1     for every incident (i,F).

Use 3V vertex variables and 3F pole variables. The Jacobian of these I=2E incidence equations has FULL ROW RANK at every genuine convex realization.

Proof. A row dependence would give nonzero weights omega_iF supported on incidences with

    sum_{F incident i} omega_iF p_F = 0,
    sum_{i incident F} omega_iF (y_i-o) = 0.

For a fixed facet F, any at most three of its vertex vectors y_i-o are linearly independent: the points are distinct extreme points on an affine plane not containing o, and three cannot be collinear. For a fixed vertex i, the same statement holds for any at most three incident poles, since they are distinct extreme vertices of the corresponding true facet of the polar. Consequently every nonisolated node of the support graph of omega has degree at least four.

But that support graph is a simple bipartite planar graph: it is a subgraph of the vertex-face incidence graph embedded radially in the polyhedral sphere. A nonempty simple bipartite planar graph with all degrees at least four cannot exist, because for its n nonisolated nodes one has e>=2n, whereas planarity gives e<=2n-4. Hence omega=0, proving full row rank.

By the implicit function theorem, the local true incidence realization space has dimension

    3(V+F)-2E = E+6.

Facet poles are uniquely and smoothly determined by any three incident vertices, so the same dimension holds in the vertex-only description with face-planarity constraints. For V10/E17/F9 it is 23 before affine normalization. Fixing any nondegenerate four-vertex affine frame removes twelve dimensions, yielding eleven. Equivalently, the seven explicit face-planarity equations in the eighteen remaining vertex variables have rank seven everywhere on the genuine realization space. The five trace-one SPD variables then give sixteen local parameters.

Maximum-tetrahedron inequalities choose closed sectors of these smooth charts and can have ties; they do not create an intrinsic realization singularity. Mechanical tree inequalities may still cut lower-dimensional sets or be active. Smoothness of the underlying geometry does NOT imply strict feasibility of all desired escape signs, generic proper110 density, or removal of multicontact positive stresses. Earlier projective-affine rescue results for limited contact configurations remain narrower results, not a universal regularization theorem.

## 6. Exact arithmetic reproducibility and limits

No global cell compiler, quantifier elimination, interval covering of the 23-variable atlas or numerical feasibility solve is claimed here. The proof gives all symbolic constraints explicitly. The following is the complete standard-library source unit for the arithmetic checks used in the coefficient/minimum-bound deduction; no seed or external input is required. It may be saved as first_layer_atlas_bounds.py and run with Python 3.13.5 (or compatible Python 3 with exact integers), assertions enabled.

```python
#!/usr/bin/env python3
from fractions import Fraction

D = 16*6
J = 3*D
normal = 8
plane = 3*normal
Hface = 4*D*plane + 3*normal*J
adj = 2*3**2
dual = 9*normal*adj*(2*Hface*normal)
metric = 6*(4*10**6)**3
m = 36+420+160+34+1+7+17+9
assert (D,J,normal,plane,Hface,adj,dual,m) == (96,288,8,24,16128,18,334430208,684)
assert max(metric,dual,2*23+2*700) < 2**80
assert 12**3 < 2**11
assert Fraction(4)-Fraction(23,2)+80+Fraction(23*11,3) < 176
k = 176*23*24**23
assert k == 224956767695414588990411741752983552
assert k < 2**118
assert 576**2+576+1 == 332353 < 10**6
assert 34-27 == 7 and 3*19-34-12 == 11
print('FIRST_LAYER_CLOSED_ATLAS_BOUNDS_PASS')
print(k)
```

The expected two terminal lines are FIRST_LAYER_CLOSED_ATLAS_BOUNDS_PASS and the displayed exact integer 224956767695414588990411741752983552. The proof of faithfulness and the realization-Jacobian rank argument are analytic; they are not certified by these arithmetic assertions.

Next scientific frontiers: exploit the sixteen-dimensional actual realization/metric manifold to escape weak mechanical walls beyond the projective-affine family; or derive an actual uniform-body inequality closing one or more nonempty candidate tree cells. Merely constructing this atlas, observing its compactness, or invoking decidability is not an exclusion or an attaining example.
