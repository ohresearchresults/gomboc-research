# material-9afd5508a25d

AI research material · [Export notes](../catalog/coverage.md#text-records)

---

# FIRST_LAYER_HAUSDORFF_CLOSEDNESS_AND_GEOMETRIC_COLLARS_V1

## Evidence, dependencies and scope
This is a coordinator analytic theorem, not a computed exclusion. The radial-extremum persistence and incidence-stabilization proofs below are independent of the earlier finite lower-bound certificates. The first-layer specialization invokes the following INTERNALLY ACCEPTED premises in their stated weak-contact scope; it does not independently replay their computational proofs.

(LB-V) A full-dimensional uniform convex 3-polytope with exactly one STRICT unstable vertex at its own volume centroid under any physical SPD metric has at least 10 true vertices, even if incidental weak contacts are present.
(LB-F) The corresponding exactly one STRICT stable facet condition forces at least 9 maximal facets, likewise allowing incidental weak contacts and any physical SPD metric.

The accepted notebook links for LB-V are minimum-0006; corrected universal285 capsule parts [internal-source-reference], [internal-source-reference], [internal-source-reference]; and final-broom results minimum-0054, minimum-0049. LB-F is linked as minimum-0024. These are evidence links, not a claim that their literal payloads are attached here or freshly verified.

The normalization source actually read completely for this theorem is [internal-source-reference], UNIFORM_AFFINE_SIMPLEX_COMPACTIFICATION_110_V1.md, 11104 bytes, SHA256 cf75f3a88147ee039293cd048851db62f76a0726a4e551359f8b17819b4b9a95. Its gauge uses an UNROOTED maximal-volume tetrahedron mapped to a regular tetrahedron, followed by translation by the ACTUAL uniform solid centroid. It supplies

  r B subset K subset R B, r=1/2, R=2 sqrt(11),
  tr M=1, M >= a I, a=1/31153,

for S=U=1 even with additional weak contacts. The physical object is the pair (K,M); M must NOT be reset to I. The gauge is not a designated-root tetrahedron or an arbitrary cap44.

New conclusion: the actual S=U=1 family in this container with at most 10 vertices and at most 9 facets is compact, and every member has exactly 10/17/9 true features. Along a convergent sequence in that family the vertex-facet incidence is eventually unchanged after relabelling. Hence there are uniform positive, but currently UNEVALUATED, geometric and strict-root margins. True vertex collisions, facet mergers, true-edge disappearance and new incidences cannot occur in the closure of first-layer S=U=1 candidates. Nonroot physical weak equilibria can remain. Neither proper110 closedness nor weak-contact regularizability is proved. No C34 exclusion, new attainer or improved global bracket follows.

## 1. Polyhedral radial extrema are strict
Let K be a full-dimensional convex polytope with 0 in its interior and let M be SPD. On the coordinate unit sphere define

  f(K,M;u)=rho_K(u)^2 u^T M u,

where rho_K is the positive radial function. Radial parametrization is a homeomorphism to the boundary, so local extrema of f are exactly local extrema of physical squared distance on the boundary. Apply the linear map M^(1/2) as a proof device and use the Euclidean metric for the classification below.

A local maximum cannot be in the relative interior of an edge or facet: there is a boundary line segment through it in both directions, and squared distance is strictly convex on that segment. Thus a local maximum is a true vertex v. For every incident edge direction e pointing into K, it must have v.e<0. If v.e>=0 then |v+t e|^2=|v|^2+2t v.e+t^2|e|^2 increases for all small positive t. Conversely, negativity on every incident edge generator makes v a strict local maximum: the finite generated tangent cone has v.d uniformly strictly negative on its unit directions; the linear decrease dominates the quadratic term near v. These are exactly strict unstable-vertex inequalities. In original coordinates they read v^T M e<0.

For a local minimum, write the irredundant maximal-facet inequalities with unit outward normals as n_i.x<=h_i, h_i>0. Near a fixed sphere direction u0 the radial function is the minimum of the finitely many relevant smooth positive functions g_i(u)=h_i/(n_i.u). Constraints with negative denominator do not bind; those with zero denominator at u0 remain irrelevant near the finite radial value. If rho has a local minimum at u0, each function active at u0 has a local minimum there, because nearby g_i>=rho>=rho(u0)=g_i(u0). In its positive hemisphere g_i has a local minimum only at u=n_i. Thus all active normals coincide. Irredundancy leaves one active maximal facet, with perpendicular foot in its relative interior. This is a strict stable facet and a strict local minimum.

Every full-dimensional convex polytope with an interior reference point therefore has at least one STRICT stable facet and one STRICT unstable vertex: take global extrema on the compact sphere. The conclusion holds in the presence of other weak contacts. The polyhedral hypothesis is essential; this is not a statement about arbitrary smooth convex surfaces.

## 2. Persistence under Hausdorff and SPD convergence
Assume rB subset K_n,K subset RB, with fixed r>0 and finite R, that K_n tends to K in Hausdorff distance, that K and the K_n are full-dimensional polytopes, and that M_n tends to an SPD M. The radial functions converge uniformly. Indeed, for Hausdorff error epsilon,

  K_n subset K+epsilon B subset (1+epsilon/r)K,
  K subset (1+epsilon/r)K_n.

These inclusions uniformly bound their radial ratios. Consequently f(K_n,M_n;.) tends uniformly to f(K,M;.).

A strict local extremum persists as a local extremum in a small fixed neighborhood under sufficiently small uniform perturbations: choose the neighborhood boundary with a strict value gap from the central extremum and maximize or minimize on its closure. The perturbed extremum is in the interior. Use mutually disjoint neighborhoods around the finitely many limit extrema. Section 1 identifies all the perturbed polyhedral extrema as strict equilibria of the same kind. Hence

  S(K,M) <= liminf S(K_n,M_n),
  U(K,M) <= liminf U(K_n,M_n).

If S(K_n,M_n)=U(K_n,M_n)=1, the limit has at most one of each, and Section 1 supplies at least one: S(K,M)=U(K,M)=1. This does not exclude weak non-extremal stationary contacts. Both a full-dimensional polyhedral limit and an SPD limiting metric are required.

## 3. Compact semantic first-layer family
Let W be the family of genuine pairs (K,M) with all of the following properties:

- K is a full-dimensional convex 3-polytope with at most 10 true vertices and at most 9 maximal facets;
- its actual UNIFORM SOLID volume centroid is 0;
- rB subset K subset RB, where r=1/2 and R=2 sqrt(11);
- M is symmetric, tr M=1 and M>=I/31153;
- S(K,M)=U(K,M)=1. Additional weak contacts are allowed; H=0 is NOT part of the definition.

Every hypothetical proper110 first-layer object has a representative in W by the normalization source. W may be empty; no existence is asserted.

W is compact. For a sequence, pad the vertex lists to length ten if needed and pass to convergent labelled vertices in the closed R ball. Their convex hull is the Hausdorff limit, so the limit is a polytope with at most ten vertices. The contained r ball protects full dimension and positive volume. Same-origin polarity, or convergent lists of at most nine unit-normal inequalities with h in [r,R], gives at most nine facets in the limit. The trace/eigenvalue domain of M is compact and its limiting metrics remain SPD.

The actual volume centroid stays zero. The Hausdorff sandwich inclusions imply volume convergence and symmetric-difference volume tending to zero, while common boundedness makes all first moments converge. Section 2 preserves S=U=1. Every limit therefore belongs to W.

Apply LB-V and LB-F to all members, including those limits. Each must have V=10 and F=9, hence E=V+F-2=17. The weak-contact scope of the accepted lower bounds is indispensable here. Lower bounds only for weak-free proper110 would not justify this step.

## 4. Three-dimensional incidence stabilization
Consider any convergent sequence in W. Label its ten vertices and nine unit-normal facet inequalities, and pass to a subsequence with converging labels and a constant finite vertex-facet incidence relation I.

All ten limiting vertex labels remain distinct true vertices: their convex hull is the limiting polytope, which still has ten true vertices. All nine limiting inequalities likewise define distinct genuine facets, since the limit has nine facets and equals their intersection. To justify that intersection equality, contract any point satisfying all the limiting inequalities slightly toward 0. Because every support h>=r>0, the contracted point satisfies all inequalities strictly and lies in all sufficiently late polytopes. Let the contraction tend to 1.

Every original incidence equality n_f.v_i=h_f persists in the limit. Thus I is a subset of the actual limiting incidence relation I_lim. For any convex 3-polytope,

  number of vertex-facet incidences
  = sum_f(number of vertices of f)
  = sum_f(number of edges of f)
  = 2E.

Here both incidence cardinalities are 34. Inclusion with equal cardinality yields I=I_lim: new incidences cannot appear either. The face lattice and the true edges persist.

There are finitely many face lattices with these counts. Each labelled combinatorial piece of W is therefore compact, and different incidence types cannot meet through geometric degeneration inside W. This argument uses dimension three and Euler's identity; no higher-dimensional analogue from V and F alone is asserted.

## 5. Uniform geometric and strict-root collars
If W is nonempty, compactness on its finitely many labelled incidence pieces gives positive uniform minima for:

1. Distances between distinct true vertices, hence each true-edge length.
2. The area of each maximal facet, and the area of each triangle formed by three distinct true vertices of one facet. Three such vertices cannot be collinear, because each is extreme in the convex facet polygon.
3. Every nonincidence slack h_f-n_f.v_i, with n_f unit and v_i not incident to f.
4. Separation of distinct normalized facet planes (n_f,h_f), and adjacent-facet exterior angles away from zero.
5. The strict root-neighbor inequalities at the unique unstable vertex, and the reciprocal polar inequalities at the unique stable facet.

For item 5, let r denote the unstable root label (not the inradius). The unique strict unstable vertex of the limit persists in a small neighborhood. Vertex separation and incidence stabilization imply that the sequence's unique unstable vertex has this same label eventually. The limiting root is strict, so all numbers

  -v_r^T M(v_j-v_r), for true neighbors j of r,

have a positive uniform minimum over W. For the stable root use the SAME-ORIGIN polar vertices q_f=n_f/h_f and the SAME inverse physical metric N=M^-1. The stable facet corresponds to a strict unstable polar vertex. Polarity and metric inversion are continuous on the compact container, giving a positive uniform minimum of

  -q_s^T N(q_t-q_s), for true neighbors t of the stable-root pole s.

There is also a positive uniform gap between the physical squared norm of the unstable root and that of every other true vertex, and between the N-squared norm of the stable-root pole and that of every other pole. Any global squared-norm maximum at a true vertex is strict unstable by Section 1. A tied maximum at two distinct vertices would give two strict unstable vertices. Compactness and root persistence therefore prevent these gaps from tending to zero.

All these constants are EXISTENTIAL and UNEVALUATED. Their existence is not an explicit rational certificate radius and not a computational exclusion. No positive lower bound is asserted for arbitrary four-vertex determinants or selected boundary-apex fan cells: nonfacial coplanarity and flat selected fan cells can still occur. No uniform positive margin is asserted for arbitrary nonroot escape inequalities; those can vanish at genuine physical weak contacts.

## 6. Boundary of proper110 and the algebraic-closure warning
A sequence of proper110 bodies represented in W has a limit with S=U=1 and the same true-feature incidence after relabelling. A strict saddle on a limiting true edge would persist by its strict edge-position and normal-cone inequalities, because that edge and its two facets persist. Thus the limit also has no STRICT saddle. Nevertheless extra physical weak VE/EF/VF contacts may appear.

At the FIRST layer, this proof removes geometric true-feature degeneration from actual S=U=1 sequences by using the accepted vertex and facet lower bounds. The remaining weak-contact regularization problem is not solved. No claim is made that all weak-contact S=U=1 points are limits of proper110, that proper110 is closed or dense, or that a weak-only realization can be perturbed without creating additional strict equilibria.

One must NOT replace all strict inequalities in a fixed labelled polynomial encoding by weak inequalities and identify the resulting algebraic set with W. That naive relaxation can contain collided redundant labels or artificial zero-length arrows, without being a limit of genuine S=U=1 bodies. The theorem concerns the semantic family of actual convex polytopes with their actual uniform centroid, true features and common physical metric. An effective finite-chart method must quantify suitable geometric collars or separately exclude its spurious algebraic boundary components.

Next useful questions are effective rational collar estimates for the first layer, infeasibility on its compact fixed-incidence pieces, and simultaneous removal or obstruction of nonroot weak-contact packets while preserving the actual uniform centroid and reciprocal metric. Another frozen-source projective cell or freely fitted moment matrix does not answer these questions.

Global status remains 34<=C_min<=622, with lower exclusion and attaining construction separate. This result is an analytic compactness and stratification advance, not the requested minimum proof.
