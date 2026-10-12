# material-5a359d1b4083

AI research material · [Export notes](../catalog/coverage.md#text-records)

---

# TWO_CAP_CENTROID_SEAM_LOCALIZATION_AND_GLOBAL_COMPLETION_V1

Coordinator original results: a true-facet centroid/maximal-radius inequality, a universal fourteen-case necessary reduction for apical U1 in the entire degree-seven E17 sector, exact all-SPD exclusions on three actual fifteen-parameter shape boxes, and a global three-parameter fixed-cone completion theorem. None excludes every root of a whole incidence type. No proper110 attainer or new bound follows:34<=Cmin<=622 remains.

## 1. Physical conventions and actual mass

Let P be a full-dimensional uniformly filled convex polyhedron, translated ONCE to its actual volume centroid0. Fix one SPD physical matrix M. Write <x,y>=x^T M y, n(x)=<x,x>, and D_xy=<x,y-x>. At a vertex x, all outgoing TRUE-edge D_xy<0 means a strict unstable equilibrium. For distinct vertices, if n(y)<=n(x), then

D_xy=[n(y)-n(x)-n(y-x)]/2<0.                         (1)

This remains strict when the radii tie. A non-strictly-unstable vertex therefore has at least one true outgoing arrow D_xy>=0. No absence of other weak contacts is needed for the exclusion below. In any finite body, a global maximum-radius vertex is strict U by(1).

Fix a vertex A. Cone P from A to every full true facet F not incident to A. The interiors of those pyramids are disjoint. Let lambda_F be their actual positive volume fractions and c_F their full area centroids, measured relative to the SAME volume centroid0. Then

A+3 sum_F lambda_F c_F=0,  sum_F lambda_F=1.          (2)

No independent face densities or chosen vertex masses occur. Define the linear-in-M facet balance

B_F=n(A)+3<A,c_F>.

Equation(2) gives sum_F lambda_F B_F=0.

## 2. Facet centroid/maximal-radius lemma

Let F be ANY genuine two-dimensional convex polygon and v ANY one of its vertices maximizing n on F. Triangulate F by its vertex fan at v. A fan triangle has vertices(v,p,q), with strictly positive normalized area weight omega; the weights sum1. The exact area-centroid formula is

3c_F=v+sum omega(p+q).

For an arbitrary vector A, whether or not vA is an edge, the following identity holds:

B_F-D_vA = (1/2) sum omega [
 n(A+p)+n(A+q)+n(v)-n(p)+n(v)-n(q)].                  (3)

Indeed, expansion of the right side gives n(A)+n(v)+sum omega<A,p+q>, equal to the left side. Every bracket is nonnegative because v maximizes n. It is strictly positive for every nondegenerate fan triangle: equality would force p=q=-A under SPD M, impossible for a triangle of positive area. Consequently

D_vA < B_F.                                         (4)

In particular, B_F<=0 forces D_vA<0, including all radius ties and the balance wall B_F=0.

If every true edge at v lies in F except possibly vA, equations(1),(4) make v strict U. This is a genuine facet/area-centroid result. It does not use a false combined-cap reflection, a marked triangle in place of F, or a separate pyramid's own centroid.

As an immediate special case, a uniformly filled pyramid at its own centroid has only one nonincident facet, so B_F=0. Its highest-radius base vertex is a nonapical strict U for every SPD. This elementary corollary does not transfer the separate centroids of two pyramids to their union.

## 3. Universal two-cap seam localization

Suppose P is a pointed n-ray cone at A truncated by exactly two true caps F_-,F_+, with every nonapical vertex simple and the cap seam crossing no cone ray. There are n ray endpoints and two seam endpoints w0,w1. Each ray endpoint has its two in-cap neighbors and A as its three neighbors. Each seam endpoint has three neighbors: the other seam endpoint, one ray endpoint in F_- and one in F_+. It is NOT adjacent to A.

This includes EVERY degree-seven(V,E,F)=(10,17,9) body, by the complete classification in [internal-source-reference]. Its three possible cap-size pairs are(3,8),(4,7),(5,6).

Assume A is the sole strict U. Then:

1. The two balances cannot both vanish. Otherwise a global nonapical maximum-radius vertex on either cap is strict U: a ray endpoint by(4), or a seam endpoint by(1). Since their positive weighted mean is0, exactly one balance is negative and the other positive.
2. Call the negative-balance cap F_N and the other cap F_P. Every maximal-radius vertex of F_N must be a seam endpoint w. A ray endpoint would be strict U by(4).
3. At such a w, both true edges lying in F_N are strictly negative by(1). Therefore its unique edge w->u entering F_P must obey D_wu>=0. In particular n(u)>n(w).
4. The maximum radius on F_P is strictly greater than the maximum on F_N. Any maximizing vertex v of F_P cannot be a seam endpoint. Thus v is a ray endpoint belonging exclusively to F_P. Its in-cap outgoing edges are negative, so D_vA>=0.

This proves a necessary reduction to the following cases. Choose the negative cap, one of the two seam endpoints w, and an exclusive ray endpoint v of the positive cap. Require

n(w)>=n(j) for every vertex j of F_N,
n(v)>=n(j) for every vertex j of F_P,
D_wu>=0, D_vA>=0, -B_FN>=0, M SPD.                  (5)

Using weak inequalities in(5) enlarges the necessary cases and is safe. If one cap has k exclusive ray endpoints, the other has n-k, so the TOTAL is2k+2(n-k)=2n cases. In degree7 it is exactly FOURTEEN, not an enumeration of arbitrary rooted trees.

All quantities in(5) are homogeneous linear functions of the SAME M for fixed actual geometry. Excluding all fourteen cones proves that every SPD has a nonapical strict U. It does not exclude sole U at another vertex, and it does not imply all-root110 exclusion.

## 4. Exact closed shape boxes in all three degree-seven types

The complete autonomous source is [internal-source-reference], twocap_seam.py.txt. It has every input, every stress weight and every helper; it does not import the older two-cap source.

Central chart inputs, indexed gi=0,1,2, are

cut=-5/2,-3/2,-1/2 respectively,
b_j=(j-cut,j^2,1), j=-3,-2,-1,0,1,2,3,
theta=1/2.

Raw apex Y0=0. For a section point b=(x,y,1), its ray endpoint is Rb, with

R=1/[1+(1-theta)x] for x>0,
R=1/[1-theta*x] for x<0.

Vertices1 through7 follow increasing j. Vertices8,9 are the two intersections of x=0 with the oriented heptagon boundary, in the order encountered. Every true facet and edge is recomputed by exact supporting-triple enumeration. The cap type is respectively(3,8),(4,7),(5,6). Sorted support-vertex sets define this source's facet indices; do not silently equate them to a different source's lateral-facet numbering.

At each centre, two actual volume fans agree exactly. Actual cap means and volume fractions satisfy(2). For each of the fourteen cases, the source constructs twelve symmetric matrices A_l with A_l:M>=0 as follows: the negative-cap norm comparisons in its stored facet-cycle order, then positive-cap comparisons, then escape(v,A), escape(w,u), and negative balance -B_FN. The sum of the two cap sizes is11, so there are9 nontrivial norm comparisons plus these3 last constraints.

The42 literal nonnegative integer rows contain210 nonzero weights, all<=1000. They yield

Q=-sum_l weight_l A_l positive definite.             (6)

All126 exact rational leading principal minors are positive. Contraction with any SPD M contradicts(5): Q:M>0 but -sum weight_l(A_l:M)<=0. No metric sampling or condition-number bound enters the proof.

The source also certifies the following three CLOSED actual shape boxes. Vary all fourteen x/y coordinates of the seven section points independently by at most10^-8, and vary theta independently by at most10^-8. The z section coordinates stay exactly1. These are fifteen independent parameters in the displayed chart, not fifteen claimed mod-affine invariants.

Every one of the three boxes has strict heptagon support inequalities and the same crossing signs. The standard two-cap construction therefore gives the stated true lattice throughout. Actual coordinates, cap areas, cone volumes and the NEW uniform volume centroid are recomputed as rational functions of those parameters. The source encloses these functions by closed rational interval arithmetic, rounded OUTWARD after each operation to the fixed grid10^-30. It does not interpolate independent vertex masses.

For every one of the42 matrices, all three interval lower bounds on its leading principal minors are strictly positive. The geometric checks comprise105 strict projected polygon support inequalities; the matrix checks comprise126 strict interval minor bounds. Thus(6), and therefore the existence of a nonapical strict U for EVERY SPD, holds on all three complete closed fifteen-parameter boxes. This is not coverage of the whole three-dimensional fixed-cone chart in section6 or of an entire incidence type.

The conclusion includes finite weak-arrow walls, radius ties, the balance wall and arbitrarily ill-conditioned SPD matrices. Physical weak000 is required only for the exact illustrative controls below, not for this lower exclusion.

## 5. Exact countercontrols to the simpler top-nonroot rule

On central geometry gi=1 take

M=(1/1000)*((430,31,490),(31,5,35),(490,35,565)).

On central geometry gi=2 take

M=(1/1000)*((68,-6,246),(-6,3,-21),(246,-21,930)).

Both are exactly SPD. At the actual own volume centroid, both have

n(Y0-g)>n(Y1-g)>n(Yi-g) for every i=2,...,9,
D_10>0.

Thus the unique highest nonroot vertex has a genuine strict escape to the apex and is NOT U. Nevertheless the all-metric seam theorem above guarantees another nonapical U, and the full actual reciprocal census is233weak000 for each metric. Specifically the first U set is{0,7,9}, the second{0,8,9}. In this source's facet numbering both S sets are{1,7}; the saddle sets are respectively{04,19,79} and{04,19,89}. All136 true-edge primitives in the two records are nonzero. The poles use the same centroid and N=M^-1, never an independently fitted or centred dual metric.

The highest-nonroot strategy is therefore genuinely weaker than seam localization even on these already excluded actual bodies. These are material negative controls, not failed110 candidates to discard. The new source preserves their full vertices, facets, moments, metrics and packets.

## 6. Global fixed-cone completion: three parameters, not only local repair

This part synthesizes the general vertex-projective centring theorem proved in fully read minimum-0203, SHAafe1de89443d478069ffce2a0c36375fc3fb7e039137eb7ba4299106211dca19, with the full two-cap classification. The deduction here is a global classification of completions at fixed apex cone. It supplies no equilibrium feasibility claim.

Fix a point A and a pointed full-dimensional tangent cone C in A-relative coordinates u=Y-A, with -A in intC. This is automatic for an actual own-centred body with literal apex planes q_i.Y<=1, q_i.A=1. Fix an ORDERED cap-difference linear functional delta which is nonzero on every extreme ray and takes both signs on those rays. Define caps by

l_1=b+delta/2, l_2=b-delta/2,
K_b=C intersect{l_1<=1,l_2<=1}.

Choose b sufficiently far inside the dual cone so both cap functionals are positive on all rays. Then K_b is a bounded genuine two-cap body. Its cap activity on each ray is determined solely by the sign of delta; the two sign blocks are contiguous in a cone section. Both caps are irredundant.

For the vertex-centred projectivity T_c(u)=u/(1+c.u), the cap coefficients transform as l_i->l_i+c. Therefore delta is unchanged. Conversely, any two bounded cap pairs with this same delta differ by such a common addition c. The denominator is strictly positive on the entire first body: on each terminal ray point it equals the ratio of the second and first positive stopping functionals, and on a radial segment it interpolates between that positive value and1. Thus these are exactly one full positive vertex-projective class, not merely a small projective neighborhood.

For completeness, the centring theorem used here has the following self-contained proof. Given ANY bounded full-dimensional K with vertex0, let D={c:1+c.u>0 for all u in K}, C=coneK, and choose z inintC. Put

V(c)=integral_K(1+c.u)^-4 du,
Psi_z(c)=log V(c)+4c.z.

The projective Jacobian is(1+c.u)^-4. If m_c and Sigma_c are the ACTUAL centroid and covariance of T_c(K), differentiation gives

grad logV=-4m_c,
Hess logV=20Sigma_c+4m_c m_c^T positive definite.

At every finite boundary point of D a denominator vanishes at a nonzero vertex. A genuine solid cone inside K at that vertex bounds the integral below by a positive multiple of integral r^2/(epsilon+Cr)^4 dr, which diverges as epsilon decreases to0. Along any unbounded sequence in D, limiting unit directions belong to C*. Since z is interior to C, c.z grows at a positive linear rate in |c|, while logV>=logVolK-4log(1+R|c|). Hence Psi_z is coercive and strictly convex. It has one unique interior minimizer, where m_c=z. The positive Hessian gives analytic dependence on fixed-incidence input parameters.

Apply this with z=-A. The resulting absolute body A+T_c(K_b) has actual uniform centroid0, retains A and ALL its literal incident planes, and retains cap difference delta. Uniqueness shows that the result is independent of the preliminary choice of b. Conversely every actual own-centred two-cap completion with this cone and ordered delta is this result.

Therefore the entire fixed-cone space of ordered proper two-cap own-centred completions is parametrized globally by delta in the open sign chambers described above: THREE real parameters. For unordered caps identify delta with -delta. Dependence within a chamber is analytic; the number of positive and negative rays determines the cap-size pair. The old local three-dimensional IFT fibre is now a global chart. Rational input need not produce rational centring parameters; exact construction can be specified by the unique positive-domain solution of the rational actual-moment equations. This is not a claim that an optimizer checkpoint or decimal centroid constitutes an exact construction.

## 7. Connection to the parallel folded-roof result

After deriving and computing the seam results, the coordinator fully read minimum-0205, SHA3c3400957135c7c06e7249bcff19346e77973c3d8c5c980cdc553c148b24f59d. It gives a complementary whole-sector chart: projection along an interior seam direction yields a convex nonagon K and roof H(u)=(u,1-beta|u1|). The actual homogeneous moments are integral_P phi=(1/(d+3)) integral_K phi(H(u)) for degree-d homogeneous phi. Cap volume fractions are projected area fractions.

That parent supplies a rigorous analytical strict222 reciprocal tail with only the two caps stable, and a true combined-cap half-reflection failure. It explicitly does NOT report an observed execution receipt for its included verifier; no such receipt is invented here. Those negative results are compatible with(3)-(5): our lemma uses each TRUE full cap and its own area centroid, coupled by(2), not the false lifted reflection. Its tail has nonapical U and no unstable apex, so it does not contradict the apical-only exclusions.

The useful unresolved connection is to combine the common projected-area measure, the true seam-quadrilateral compatibility and the fourteen metric cases over the global actual shape space. The present42 certificates do not prove the fourteen cones empty for arbitrary geometry. Other unstable roots also remain separate.

## 8. Complete recovery and observed checks

Source material [internal-source-reference] is the complete13485-byte UTF-8/LF source. Save unchanged as twocap_seam.py.
SHA256 a008566eabc4d809c1fbc25116af32b9e6a3371f2558e304ef8d5ca612ebe0cd.
No external data, numerical optimizer, prior material file or third-party library is needed for reconstruction. All literal stress rows and both metrics are embedded. The source uses CPython>=3.10 standard library; execution was observed with CPython3.13.5, assertions enabled. Exact Fraction arithmetic and the explicit outward grid10^-30 are the only verification arithmetic rules.

Reconstruction and verification command:

python -B -S twocap_seam.py > run.out

Expected deterministic output twocap_seam.json:
126678 bytes, SHA256 b0aadb500d477d8a87958b556f2d7520d30960f81c5e68f907c3d170a681453a.
Expected run.out SHA256:
5dbb4bb2b82faef8b1c04f598dc3b5b2effa60faff8d057c4a2b932da32ff7f7.

Expected markers:
TWO_CAP_ALL_THREE_CONTROLS_ROOT0_U1_EMPTY_42_EXACT_SEAM_CERTIFICATES_PASS
THREE_FULL_15_PARAMETER_ACTUAL_SHAPE_BOXES_RADIUS_1E_MINUS8_126_INTERVAL_MINORS_PASS
COUNTERCONTROL 1 1 2 3 3
COUNTERCONTROL 2 1 2 3 3
TWOCAP_SEAM_EXACT_PASS 126678 b0aadb500d477d8a87958b556f2d7520d30960f81c5e68f907c3d170a681453a

The coordinator executed this complete source successfully. This is an exact computational certificate with an analytical coverage argument, not a proof-assistant formalization or an independently authored implementation. The two true volume fans are independently chosen decompositions inside this implementation. Exploratory floating-point searches were used only to discover small integer stresses and metrics; all final inputs are literal and their validity is recomputed exactly. No unsuccessful finite search is used as a global exclusion.
