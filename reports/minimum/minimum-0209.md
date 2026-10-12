# minimum-0209

AI research report · 2026-09-23 UTC · [Export notes](../../catalog/coverage.md#text-records)

---

# HEX6_SIX_CORNER_SHADOW_OBSTRUCTION_AND_BASE_TANGENT_U2_V5

## 1. Main result

**A rank-two true rooted escape system on an actual uniformly filled three-dimensional polytope requires at least SEVEN corners in its planar shadow.** The statement includes weak selected arrows and collapsed true edges. It uses the actual projected volume measure, not uniform area measure on the shadow.

The key new geometric theorem is stronger than a statement about a particular completion:

> If a convex polygon Q contains 0 in its interior, satisfies −Q/3 ⊂ Q, and has at most six corners, then Q has at least two strict radial-maximum corners.

Every linear shadow of a uniformly filled, own-centred convex three-polytope satisfies −Q/3 ⊂ Q. Consequently, every rank-two shadow with at most six corners has at least two noncommunicating exposed fibres in its weak-arrow graph. **No true-edge arborescence toward any one root can exist.** A collapsed edge cannot hide the second obstruction.

This gives a new geometry-wide mechanical boundary on the COMPLETE fixed-six-pole atlas. Its true heptagonal facet F6 contains seven of the ten vertices. Whenever the kernel of a rank-two metric is parallel to F6, that facet projects to a segment, and the remaining three vertices give a shadow with at most five corners. Thus:

> On every completion in the entire open five-cut cube, including genuinely unequal and virtual-horizon-crossed completions, every nonzero singular PSD metric whose kernel contains a direction parallel to F6 is incompatible with every true rooted escape tree.

There is a genuine positive-definite consequence, not just an exclusion at a singular matrix. Each such rank-two metric has an explicit, geometry-dependent open neighborhood in which every SPD metric has at least two strict U vertices. Over the compact closed atlas, a uniform neighborhood exists. Its numerical width is not evaluated here.

In particular, for EVERY actual completion there is an explicitly defined reciprocal family with eigenvalues 1,1,epsilon, apex 0 strictly unstable, and a nonapical strict U for all sufficiently small positive epsilon. The two large eigenvalues remain equal: this is a rank-two obstruction not supplied by the earlier dominant-one-eigenvalue argument.

No U1 or110 construction is claimed. The complement with seven to ten shadow corners and kernels transverse to F6 remains open; an SPD component staying away from the excluded singular boundary is also not excluded. No canonical count or global complexity bound changes.

## 2. Input authority and evidence level

The selected immutable parent is

    minimum-0208
    SHA256 8009afaa54e6d97c95b01bfbc40ea119fcc3fd87a4cb1528b21a5e4a2b70b9d9
    HEX6_DEEP_INDEPENDENT_BAND_GLOBAL_PSD_NONAPICAL_U_V4.

Its small-cut and deep-band exclusions are not replayed or retested. The complete fixed-pole atlas and its compactification are used in their accepted V3 scope. The new results below are analytic, and all needed shadow and weak-graph arguments are proved here.

**Retained-context limitation:** the standalone new rank-two material's full text was not recovered in the tool-visible responses of this execution. I do not claim an additional complete read or execution of that file. No unprovided step of its proof is needed below: the exposed-fibre implication used here is independently established in section 6. No new numerical search result, computational certificate, observed census, or cold-execution receipt is claimed.

## 3. Actual centring gives a three-to-one geometric constraint on every shadow

Let P be a full-dimensional convex three-polytope of uniform density with actual volume centroid 0. For every true vertex a, triangulate the actual boundary facets not containing a and cone those triangles from a. This is a positive-volume decomposition of the SAME body. The centroid formula gives

    0 = (1/4) a + (1/4) sum_T theta_T (b_T+c_T+d_T),
    theta_T > 0, sum_T theta_T = 1.

Therefore

    −a/3 = sum_T theta_T (b_T+c_T+d_T)/3 ∈ P.

Taking convex combinations of vertices proves

    −P/3 ⊂ P.                                             (3.1)

This is a consequence of genuine uniform volume moments. The coefficients are actual tetrahedral volume fractions, not independently adjustable masses.

For any rank-two linear map L, put Q=LP. Then

    −Q/3 ⊂ Q.                                             (3.2)

Equivalently, for every linear functional ell on the shadow,

    max_Q ell ≤ 3(−min_Q ell).                             (3.3)

The actual marginal is, up to a constant Jacobian factor, the length of P∩L⁻¹(y). This length is a nonnegative concave function on Q, and its weighted first moment is zero. It is generally NOT the constant area density. Equation (3.2) is a necessary consequence of that actual fibre-length centring which survives without having to replace the marginal by a fictitious uniform polygon.

The new planar theorem below applies to every polygon satisfying (3.2), whether or not a particular fibre density realizing it has been specified. It is therefore a valid relaxation of the actual problem.

## 4. A radial-chain estimate

Consider distinct consecutive corners v_m,...,v_1,v_0 of a convex polygon containing 0 in its interior, with weak arrows

    v_j·(v_(j−1)−v_j) ≥ 0,  j=1,...,m.

Normalize v_0=(1,0). Let theta be the positive angular span of this boundary chain, measured from v_0 toward v_m along the chosen side. If the successive angular increments are delta_j, then

    0 < delta_j < pi/2,
    |v_j| ≤ |v_(j−1)| cos(delta_j),
    theta = sum delta_j.

Strict positivity of the increments follows from true polygon corners and an interior origin. A weak arrow still makes the vertex norms strictly increase toward v_0, because the corresponding edge is nonzero.

Concavity of log cos on (−pi/2,pi/2) gives

    |v_m| ≤ product cos(delta_j)
          ≤ cos^m(theta/m).                              (4.1)

For m≥2, maximizing the possible negative x-coordinate yields

    −(v_m)_x ≤ cos^(m+1)(pi/(m+1)).                       (4.2)

Indeed, where cos theta is negative, the relevant function is

    (−cos theta) cos^m(theta/m).

Its maximum occurs at theta=m pi/(m+1); on the part theta>pi it is decreasing. For m=1 the x-coordinate is nonnegative.

The particular bounds needed here are

    one arrow:   (v_1)_x ≥ 0,
    two arrows:  (v_2)_x ≥ −1/8,
    three arrows:(v_3)_x ≥ −1/4.                          (4.3)

There is an important equality statement. In an upper-half-plane three-arrow chain, equality (v_3)_x=−1/4 forces equality in both steps of (4.1) and in the scalar maximization. Hence

    v_3=(−1/4,1/4).                                      (4.4)

This equality information will remove the final weak boundary in the six-corner proof.

## 5. Six-corner theorem, including weak boundaries

### Theorem

Let Q be a full-dimensional convex polygon with 0∈int Q and −Q/3⊂Q. If Q has at most six corners, it has at least two strict radial-maximum corners.

Here a strict radial-maximum corner v means that its two incident outgoing primitives are both strictly negative. The assertion does not assume that all other primitives are nonzero.

### 5.1. The boundary graph when there is only one strict maximum

Suppose, for contradiction, that A is the only strict radial-maximum corner. Normalize A=(1,0).

At every other corner v, at least one incident arrow is nonnegative. There cannot be two: the direction −v toward the interior origin is a strictly positive combination of the two incident edge directions, and taking its dot product with v gives −|v|²<0.

Thus every nonroot corner has exactly one weak outgoing boundary arrow. Along any such arrow the squared norm strictly increases. There are no cycles, and every path terminates at A. The selected edges are the polygon boundary with exactly one edge removed, oriented toward A.

Consequently A is the unique global maximum-radius corner. The missing edge has negative primitives at both ends. The root can be an endpoint or an interior vertex of the remaining path.

### 5.2. At most five corners

If A is internal in the path, every corner reaches it in at most three arrows. Equation (4.3) implies

    x ≥ −1/4 on Q.

But −A/3=(−1/3,0) must belong to Q, a contradiction.

If A is an endpoint, every corner except the far endpoint again has at most three arrows to A. The far endpoint is reached along at most four boundary edges. The angular span of that whole path is greater than pi: its missing closing edge has angular span strictly less than pi because the origin is interior.

For a four-edge path, (4.1) therefore gives radius strictly less than cos⁴(pi/4)=1/4. A three-edge path gives an even smaller bound; a two-edge path cannot have span greater than pi with both increments less than pi/2. Again all x-coordinates are at least −1/4, contradicting −A/3∈Q.

### 5.3. Six corners with an internal root

If the two branch lengths are 2 and3, the previous three-arrow argument applies. The only remaining internal-root case has branch lengths4 and1.

Write the long endpoint as B and the short endpoint as C. All other corners have x≥−1/4, and C→A gives C_x≥0. Since −A/3∈Q, necessarily

    B=(−a,h), a≥1/3.

The four-edge angular span to B is less than pi. Otherwise (4.1) would give |B|≤1/4, impossible. Reflecting the figure if necessary, h>0 and every corner of the long branch lies above the x-axis.

Write C=(c,−d), with d>0. Its weak arrow to A gives

    c²+d²≤c.

The only negative-axis crossing of the boundary is the missing edge BC. Containment of (−1/3,0) requires

    d(3a−1) ≥ h(3c+1).                                   (5.1)

On the other hand,

    (3c+1)²−16d²
       ≥(3c+1)²−16(c−c²)
       =(5c−1)²≥0.

Thus 4d≤3c+1, and (5.1) forces

    3a−4h≥1.                                             (5.2)

This is incompatible with the four-arrow geometry. Write B=r(cos theta,sin theta), pi/2<theta<pi. By (4.1),

    3a−4h
      ≤(−3 cos theta−4 sin theta) cos⁴(theta/4).

Where the first factor is positive, the expression is strictly increasing up to theta=pi. Indeed tan(theta/4)≤1, so its derivative is bounded below by

    cos⁴(theta/4)(7 sin theta−cos theta)>0.

Its endpoint value is3/4. Hence 3a−4h≤3/4<1, contradicting (5.2).

### 5.4. Six corners with an endpoint root

Label the path away from A as v_1,...,v_5, with weak arrows v_i→v_(i−1), and increasing angular coordinates

    0<theta_1<...<theta_5=Omega<2pi.

The missing edge joins v_5 to A, so Omega>pi. Corners v_1,v_2,v_3 have x≥−1/4. Thus −A/3∈Q forces at least one of v_4,v_5 to have x≤−1/3.

**Case A: (v_5)_x≤−1/3.** Its radius is at least1/3. Equation (4.1) and

    cos(2/3)<4/5,
    (4/5)^5<1/3

imply Omega<10/3. The cosine inequality follows, for example, from its alternating Taylor upper bound 1−2/9+2/243=191/243<4/5.

Any corner below the x-axis has angle between pi and Omega. Its radius is at most

    cos⁵(pi/5)=(11+5 sqrt(5))/64<7/20.

Using pi>25/8 and sin t<t,

    −min_Q y <(7/20)(10/3−pi)<7/96.                       (5.3)

Some chain corner has angle in [pi/4,3pi/4], since successive angular increments are less than pi/2. Its radius is at least |v_5|≥1/3, so

    max_Q y ≥1/(3 sqrt(2))>7/32.

This contradicts max_Q y≤3(−min_Q y), which follows from −Q/3⊂Q and (5.3).

**Case B: (v_4)_x≤−1/3.** Write

    v_4=(−a,h), a≥1/3, h>0, r=|v_4|.

As before theta_4<pi, so v_1,...,v_4 are above the x-axis and v_5 is the only corner below it. The weak arrow v_5→v_4 puts v_5 in the closed disk with diameter [0,v_4]. Therefore, with b=−min_Q y,

    b≤(r−h)/2.                                           (5.4)

Write v_3=(xi,eta). The three-arrow bound gives xi≥−1/4. The weak arrow v_4→v_3 gives

    h eta ≥r²+a xi≥r²−a/4.

Consequently

    4h[eta−3(r−h)/2]
      ≥4a²+10h²−6rh−a
      ≥a²+10h²−6rh
       =(r−3h)²≥0,                                      (5.5)

where the second inequality uses a≥1/3.

Equations (5.4)–(5.5) imply eta≥3b. But −Q/3⊂Q requires max_Q y≤3b. Thus every inequality must be equality. In particular,

    a=1/3, r=3h, xi=−1/4.

The equality rule (4.4) forces v_3=(−1/4,1/4). Meanwhile a=1/3 and r=3h give h=1/(6sqrt(2)) and r=1/(2sqrt(2)); equality in (5.5) would require eta=1/(2sqrt(2)), not1/4. This is impossible.

All six-corner cases are closed. The argument includes weak arrows and every equality encountered in the proof.

### A control showing why the centroid hypothesis matters

The convex pentagon, in cyclic order,

    A=(1,0),
    v1=(1/2,1/2),
    v2=(0,1/2),
    v3=(−1/4,1/4),
    C=(1/5,−3/10)

contains0 in its interior and has only A as a strict radial maximum. Its weak rooted path has

    D_v1,A=D_v2,v1=D_v3,v2=0,
    D_C,A=7/100>0.

The other incident primitive at each nonroot is negative. This does not contradict the theorem: its minimum x-coordinate is−1/4, so −A/3 is outside the polygon. It cannot be the shadow at the actual uniform volume centroid of a three-polytope. This is a planar hypothesis control, not an actual E17 or110 construction.

No sharpness claim is made for the threshold seven: the proof excludes at most six corners; it does not construct a seven-corner feasible example.

## 6. From shadow corners to TRUE rooted reachability

Let M0=L^T L have rank two and let y be a strict radial-maximum corner of Q=LP. Its two incident shadow directions have negative dot product with y. They generate the tangent cone of Q at y, so

    y·(z−y)<0 for every z∈Q distinct from y.               (6.1)

Let T be the set of true vertices of P projecting to y. It is nonempty. The exposed preimage P∩L⁻¹(y) is a true vertex or a true edge, since the kernel is one-dimensional.

For EVERY true outgoing edge i∈T, j∉T,

    D_ij(M0)=y·(LX_j−y)<0.                               (6.2)

Thus no weak-arrow path can leave this fibre. Internal collapsed edges have zero primitives, but they do not provide an exit.

By the theorem in section5, a shadow with at most six corners has at least two such disjoint closed fibres. Any specified root lies outside at least one of them. Therefore no true-edge rooted escape tree exists, for any root.

This argument does not identify a projected boundary edge with a true primal edge. The projection may merge several vertices, collapse an edge, or place original vertices inside a shadow edge or in the interior. The obstruction is transported through the genuine outgoing boundary of an exposed fibre. Projected-origin and boundary-interior exceptions cannot remove that closed boundary.

For rank one, the positive and negative endpoints of the projected segment similarly have two closed exposed preimages. Hence no nonzero rank-one metric admits a weak rooted escape tree either.

A genuine sequence of SPD U1 systems has, after taking a subsequence, the SAME selected true rooted tree. Its limiting PSD metric satisfies that tree's weak inequalities. The singular systems excluded above therefore cannot be such limits. Counting singular strict-U vertices alone would not establish this conclusion.

## 7. Entire unequal atlas: a large-facet kernel obstruction

### General theorem

Let P be any actual uniformly filled own-centred three-polytope with a true facet F and at most FOUR vertices outside F. Let M0 be rank two, and suppose its kernel is parallel to F.

The image LF is a segment. The remaining at most four vertices imply that LP has at most six corners. Sections5–6 therefore give:

> Every true rooted escape system, at every root, is impossible under M0, including weak arrows and collapsed fibres.

This is an actual geometry theorem. It does not depend on a selected tree, an f-vector catalogue, or the shape of the facet within its plane.

### Application to the fixed-six-pole class

In the supplied ten-vertex graph,

    F6=(4,3,9,2,1,7,6),
    vertices outside F6 are exactly {0,5,8}.

Thus a kernel parallel to F6 gives a shadow with at most FIVE corners. The rank-two exclusion holds for the WHOLE open five-cut atlas, not only near equal cuts, and not only in the bounded-released-pyramid sector.

The same general theorem also applies whenever another actual E17 realization has at least six vertices on one maximal facet. In particular, it provides a tangent-kernel boundary obstruction for the larger cap in each of the recorded degree-seven cap-size patterns (3,8), (4,7), and (5,6). It does not transfer any degree-five- or degree-six-specific finite stress catalogue to those bodies.

### Explicit positive-definite neighborhood

For a fixed P and M0, select two strict radial-maximum shadow corners and their exposed vertex sets T1,T2. Let

    eta=min [−D_ij(M0)/(||X_i||·||X_j−X_i||)],

where the minimum runs over the genuine outgoing boundary edges of these two sets. Every denominator is positive and every numerator is strictly positive, so eta>0.

If M is SPD and

    ||M−M0||_op≤eta/2,

all those boundary primitives remain strictly negative. In each T_l choose a vertex of maximum M-norm. Its internal incident arrows are strictly negative by

    D_ij(M)=(|X_j|_M²−|X_i|_M²−|X_j−X_i|_M²)/2,

and its external incident arrows are negative by the preserved boundary. Hence M has at least TWO strict U vertices.

This is a complete closed metric neighborhood, not a claim obtained by checking a few perturbations. It permits weak contacts elsewhere. A simultaneous actual-body perturbation can be included by checking the same boundary margins with the bound

    ||sym(Z_i(Z_j−Z_i)^T)−sym(X_i(X_j−X_i)^T)||_op
       ≤4R epsilon+2 epsilon²,

when ||X_i||≤R and ||Z_i−X_i||≤epsilon. Only genuine own-centred convex realizations are in the mechanical conclusion.

## 8. An explicit reciprocal rank-two tail on EVERY completion

The following family makes the exclusion nonvacuous at the designated apex.

The origin is strictly inside the fixed planar pole hexagon. One exact certificate uses p1,p2,p4 with positive barycentric weights

    (1451583,1784021,240000)/3475604.

Therefore (0,0,1) is a strictly positive combination of q1,q2,q4. On every actual fixed-pole completion, z≤1 is a support touching only A. In particular X_i,z<1 at every other true vertex.

Let q_B=(a,b,c) be the ACTUAL pole of F6. In the star-centred atlas,

    q_B=(b_source+4c_star)/(1+4(c_star)_z).

Its third coordinate is negative. If w=(a,b) is nonzero, put

    Pi=w w^T/(w^T w).

If w=0, take Pi=diag(1,0). For epsilon>0 define the ONE reciprocal physical pair

    M_epsilon = blockdiag(Pi+epsilon(I2−Pi),1),
    N_epsilon = blockdiag(Pi+epsilon^(-1)(I2−Pi),1).

Their product is exactly I. The singular limit has rank two and a horizontal kernel parallel to F6. Its shadow therefore has at least two strict radial maxima.

Moreover,

    M_epsilon A=A,
    D_0i(M_epsilon)=X_i,z−1<0

for every true apex edge and every epsilon>0. Apex0 is always strict U. Taking the exposed nonapical fibre of the singular limit and applying the boundary-margin formula in section7 proves that, for all sufficiently small positive epsilon, there is also a nonapical strict U.

For 0<epsilon≤1 the eigenvalues are 1,1,epsilon. This entire asymptotic mechanism lies outside the earlier dominant-first-eigenvalue test. It excludes U1 alone and does not rely on S1.

A concrete genuinely unequal source to which this construction applies is

    (x,y,z,u,v)=(1/2,3/4,1/3,4/5,2/5).

It is outside both the small-cut exclusion and the deep almost-diagonal band. Its exact actual-centred body is specified in section10. Choosing the lexicographically first strict nonapical shadow-corner fibre in the singular limit, and then the boundary minimum eta above, gives a deterministic algebraic family 0<epsilon≤min(1,eta/2) with apexU and another strict U.

This is an analytic family construction. No labelled S/U/H census or weak-free claim for that unequal example has been computed. In particular it is not presented as a new U1 witness.

## 9. A uniform forbidden metric neighborhood over the full atlas

The accepted V3 compactification supplies a continuous closed-cube family of genuine full-dimensional own-centred bodies, with a common retained tetrahedron and ||X_i||≤18. Some labels merge on the boundary; those boundary objects are not counted as10/17/9.

The base pole q_B remains continuous and nonzero. Normalize PSD matrices by tr M=1 and define

    delta_B(P,M)=q_B^T adj(M) q_B / ||q_B||².

For rank two, delta_B=0 exactly when the kernel is parallel to F6. Rank-one matrices also have delta_B=0. Section7 excludes every rooted weak tree throughout this zero set, including the closed-cube limits. The proof remains valid with merged labels: two distinct strict shadow corners still give two closed sets of labels, and every edge leaving either set has a strictly negative primitive.

For clarity, an exact positive uniform constant can be defined without claiming that it was computed. Let

    Psi(P,M)=max_(root r, true graph spanning tree T)
                 min_((i,j) in T oriented toward r) D_ij(P,M).

The graph is fixed and the maximum is finite, so Psi is continuous. On the compact set delta_B=0 it is strictly negative. Put

    gamma=−max_(closed atlas, M PSD, tr M=1, delta_B=0) Psi(P,M)>0.

Then, with R=18,

    delta0=min(1/16,[gamma/(16R²)]^4)>0                 (9.1)

has the following consequence:

> Every SPD physical metric satisfying
>
>     q_B^T adj(M) q_B / [||q_B||²(tr M)²] ≤ delta0
>
> has at least two strict U vertices on every actual completion in the full atlas.

To verify the neighborhood estimate, let k be a unit vector in q_B-perp minimizing k^T M k there. The determinant of this two-dimensional restriction is delta_B, so s=k^T M k≤sqrt(delta_B). Set

    M'= (I−kk^T) M (I−kk^T),
    M0=M'/(1−s).

M0 is normalized PSD with a tangent kernel. For delta_B≤1/16,

    ||M−M0||_op≤4 delta_B^(1/4).

Each primitive changes by at most 2R² times that norm. Equation (9.1) therefore gives Psi(P,M)≤−gamma/2<0. No weak rooted tree exists, so an SPD metric cannot have only one strict U.

**The existence and positivity of delta0 are proved; its numerical value is not evaluated.** This is not an executed uniform stencil certificate. Its substantive input is the new mechanical exclusion of the entire tangent-kernel zero set, not merely compactness of the geometry.

In reciprocal notation the numerator is det(M)·q_B^T Nq_B with N=M⁻¹. Thus a prospective U1 sequence on this atlas must keep that scale-invariant quantity away from zero. A rank-two limit, if one exists, must be transverse to the true base plane.

## 10. Self-contained actual-body reconstruction data

The exact literal geometry is repeated here so that the unequal-family consequence does not require an inaccessible coordinate file.

    p = 1/100000 * (
      (60401,−32565), (80000,−20000), (0,60000),
      (−80000,80000), (−483861,−325040), (−447814,−355009));
    A=(0,0,1), q_i=(p_i,1);
    b_source=(2615613/500000,816129/250000,−3);
    B_i=[q_i;q_((i+1) mod6);b_source]⁻¹(1,1,1).

For any fractions in the open five-cube,

    Y0=A;
    Y1=B1; Y2=B2; Y3=B4; Y4=B5;
    Y5=B0+x(A−B0);
    Y6=B0+y(B5−B0);
    Y7=B0+z(B1−B0);
    Y8=B3+u(A−B3);
    Y9=B3+v(B4−B3).

True maximal facet cycles:

    (0,4,6,5), (0,5,7,1), (0,1,2), (0,2,8),
    (0,8,9,3), (0,3,4), (4,3,9,2,1,7,6),
    (5,6,7), (9,8,2).

True edges:

    01,02,03,04,05,08,12,17,28,29,34,39,46,56,57,67,89.

The partial cut passes through the old B2; that incidence is unchanged.

Write U_i=Y_i−A. The positive apex-fan triples are

    (4,3,9), (4,9,2), (4,2,1), (4,1,7),
    (4,7,6), (5,6,7), (9,8,2).

For a triple T={i,j,k}, put a_T=|det(U_i,U_j,U_k)|/6. For star parameter c define

    d_i(c)=1+c·U_i,
    W(c)=product_(i=1)^9 d_i(c),
    Z(c)=sum_T a_T product_(i not in {0} union T) d_i(c).

The exact actual-centred body is

    X_i=A+U_i/d_i(c),

where c is the unique solution with all ACTUAL d_i>0 of

    Z_x W−Z W_x=0,
    Z_y W−Z W_y=0,
    Z_z W−Z W_z−4ZW=0.

Its actual uniform volume is Z/W. These equations encode the newly refilled uniform first moments, not the image of the old centroid. Rational cuts specify an exact algebraic body; rationality of c is not asserted.

For the explicit unequal example use exactly

    (1/2,3/4,1/3,4/5,2/5).

The pair M_epsilon,N_epsilon in section8, together with the deterministic exposed-fibre selection and boundary minimum, specifies the nonwinning physical family completely. No positivity is imposed at removed virtual B0 or B3. An unbounded released virtual pyramid does not invalidate the bounded actual body or any proof above.

No code materially produced this result. Accordingly there is no new computational capsule, byte pin, or claimed execution to reconstruct. The exact data and finite algebraic selection rules above are the analytic reconstruction recipe.

## 11. What is closed, and what remains

The new obstruction removes ALL rank-two weak rooted systems with at most six shadow corners, across the entire actual unequal-completion atlas. It also removes the whole base-tangent kernel boundary, supplies explicit pointwise SPD neighborhoods, and proves a uniform forbidden neighborhood over the compact atlas. These statements include collapsed fibres and finite weak-arrow boundaries and do not assume S1 or H0.

It does not prove that every rank-two shadow has at most six corners. Seven-, eight-, nine-, and ten-corner shadows remain possible geometric sectors. Their actual fibre-length centring must still be enforced. Nor does a complete exclusion of rank-two candidates, were it later obtained, automatically exclude an SPD U1 component staying away from that boundary.

The most useful continuation is therefore the genuinely unequal seven-to-ten-corner shadow sectors with kernels transverse to F6. The six-corner proof shows exactly where the next difficulty begins: the negative support needed by actual centring can no longer be confined to the last one or two vertices of a short boundary chain. Any prospective strict planar solution must then be checked on every true nonroot fibre before applying an SPD lift; a singular outgoing-arrow count without rooted reachability remains insufficient. Proper110 additionally requires the same reciprocal metric on all true maximal facets and a complete saddle and physical-weak-equilibrium check.
