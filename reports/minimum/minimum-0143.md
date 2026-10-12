# minimum-0143

AI research report · 2026-09-20 UTC · [Export notes](../../catalog/coverage.md#text-records)

---

# TWO_APEX_COVER_AND_TWO_INTERNAL_REGULARIZATION_V1

## 1. Resolution and exact scope

**All pure-four-A two-apex E17 configurations with four nonbasal weak edges are regularizable, including the genuine unequal-height unique-adverse cases.** The mechanism is more general: any finite family of simple physical A points whose true weak edges are covered by two adjacent true vertices admits genuine own-centroid regularization, preserving the full face lattice and exactly the original feature-labelled strict equilibria.

A second theorem removes the exceptional pair left by the parent’s free-chord analysis. **On an actual uniformly filled unequal-height two-apex roof, the joint centroid derivative of any two internal basal vertices has rank three.** This includes vertices assigned to different apices with parallel neighbor chords. The apparent co-aligned-kernel possibility is incompatible with the actual uniform centroid. The decisive inequality uses the convex outer shadow and the nonconvex visible gap of the same base, not independently assigned moments.

There is a further automatic extension: **one free internal basal vertex and any other free basal vertex assigned to the same apex give a rank-three centroid actuator**, including when the second vertex is constrained by a ridge quadrilateral. In the unique-adverse sector these statements eliminate the entire nonnegative intrinsic stress cone, including all polygon reactions.

A new apex-plane sign test also closes a continuous part of the three-nonbasal-plus-one-basal sector. Complete proofs and the exact remaining complement are below.

Two new rational-metric, actual own-COM controls and their whole regularization intervals are certified. One has exactly the two opposite-apex internal free vertices with parallel chords; the other has four nonbasal A points with a unique adverse packet. They are genuine bodies, but **neither is a surviving affine-stress control**: both contact tensor matrices have rank four. The universal theorems, not these examples, are the sector closures.

The full unequal-height problem is not closed. The unresolved two-apex cases now have two or three nonbasal weak points and at most one free internal basal vertex, subject to the additional restrictions in Section 8. No full intrinsic obstruction or nonregularizable body is supplied. Mixed EF/VF configurations and general non-B8 lattices remain separate. No110 attainer, registry change, or change to34<=C_min<=622 is claimed. :contentReference[oaicite:0]{index=0}

## 2. Inputs, terminology and inherited premises

The complete1803-line `research-journal(20260920-203349).md` was read consecutively through EOF, including the complete literal required parent and its source capsule. The mounted file has320310 UTF-8 bytes and SHA-256 `d39d17daffe0237a3b8b617af77ca233870902b256b404ad6f52972c46a3d11e`.

The authoritative parent is `minimum-0140`, `UNEQUAL_WALL_AND_FREE_CHORD_REGULARIZATION_V1`. Its47060-byte compact JSON envelope authenticates to the required SHA-256 `12961fff59f36b67340a96fae45fd85d51081d7e75350828a246fbeac9b734d0`. The envelope uses UTF-8, `ensure_ascii=False`, separators `(',',':')`, keys `version,result_markdown`, one terminal LF inside the Markdown string and no envelope-final LF. The complete mounted23025-byte `wall_roof.py` was also read. No required source conflict or missing dependency was found. The accepted parent controls were not routinely rebuilt.

A is a **simple physical VE point**: at its source x, the radial supporting plane exposes exactly one true edge x->x+u. Thus one source has at most one outgoing weak edge. A raw primitive zero without its complete physical packet is not an A point. Throughout, M is one SPD metric and N=M^-1; an affine factor L with L^T L=M represents the actual Euclidean body, not a second independently chosen mechanics.

The following accepted premises are used: actual own-centroid regularization of at most three physical weak points; the complete parallel-ridge and centroid-height-wall closures; the basal theorem; and the parent’s unique-adverse classification and full-stress resultant identity. These preserve full true lattices, old strict feature labels and absence of additional equilibria. :contentReference[oaicite:1]{index=1} :contentReference[oaicite:2]{index=2}

For reference, with B at raw height0, actual centroid height gamma, and lower/higher apex heights h<H, the parent’s remaining sector has one positive beta_i=(z_source-gamma)(z_target-z_source), all other nonbasal beta negative, and neither apex on the COM-height wall. Every nonzero full nonnegative intrinsic stress alpha has positive weight on the adverse packet and, for c=sum alpha_i u_i,

    (h-gamma)c_z > 0.                                   (1)

In particular c is nonzero. This is not a signed-stress dimension-one assertion. :contentReference[oaicite:3]{index=3}

## 3. Adjacent two-vertex covers: a general physical regularization theorem

### Theorem

Let P be any full-dimensional uniformly filled convex three-polytope at its own centroid0. Suppose every physical weak point is simple A and every corresponding true edge has at least one endpoint in {a,b}, where ab is a true edge of P. Then P has arbitrarily close genuine regularizations of the same full lattice, with exactly the original strict feature-labelled equilibria and no weak equilibria.

The number of A points is unrestricted. The theorem is not restricted to roofs or to a fixed height ordering.

### A genuine affine curve removes all transverse contacts

The vectors a,b are linearly independent. Otherwise two true vertices would lie on one positive radial ray, making the nearer one nonextreme, or the true edge ab would contain the interior point0. Choose a nonzero covector n annihilating both and put

    Pi=ker n,  H1=-nn^T.

For a weak arrow x->y incident to {a,b},

    x^T H1(y-x)=0                         if x is a or b,
    x^T H1(y-x)=(n.x)^2                   if y is a or b. (2)

Consequently H1 opens every incoming contact whose source is outside Pi and leaves every other contact identically zero. This is a metric shorthand for a true affine shape motion. In particular M0+tH1 is SPD for sufficiently small t; the explicit rank-one condition is t n^T N0 n<1.

There are at most two remaining outgoing contacts with source a or b and target outside Pi, because a simple physical A source has only one outgoing weak edge. For each such source A and its edge vector u_A, choose a covector v satisfying

    A.v=1/(n.u_A).                                      (3)

The at most two equations are solvable because a,b are independent. Set H2=nv^T+vn^T. Every entirely planar contact has zero H2 derivative, while each selected outgoing transverse contact has derivative1.

The single analytic metric curve

    M(t)=M0+tH1+t^2H2,  N(t)=M(t)^-1                   (4)

therefore opens incoming transverse contacts at first order and outgoing transverse contacts at second order. Entirely planar contacts remain exactly zero. Old strict and excluding packet guards persist for sufficiently small positive t. A positive Cholesky factor of M(t) gives an analytic curve of actual affine images. Uniform centering is exact under these affine maps.

### Why at most three physical contacts remain

P intersect Pi is a two-dimensional convex polygon containing0 in its relative interior. Both a,b are true vertices of that section, and ab is a true section edge. Any true edge of P contained in Pi is an exposed edge of this section: its supporting functional cannot restrict to a constant on Pi because0 is strictly inside P.

A section vertex has only two incident edges. Thus the union of all section edges incident to a or b contains at most three edges: ab and at most one other edge at each endpoint. A true edge cannot carry A points in both directions, since the two primal escape values sum to minus its squared length. Hence at most three A points remain after(4). If ab itself was not weak, at most two remain.

Apply the accepted at-most-three-point theorem inside a neighborhood where every already-opened packet and every original strict guard retains its sign. This finishes a genuine own-centroid regularization. The initial analytic curve(4) and the accepted actual finishing curves all preserve maximal facets; no non-affine transport of an old centroid occurs.

### The entire intrinsic cone, not a selected stress

Let R be the actual contact derivative on the full true realization tangent space. Every nonnegative intrinsic stress annihilates all genuine affine directions, including H1,H2, regardless of its polygon reactions. Equation(2) forces zero stress weight on every incoming transverse contact. Testing H2 then forces zero weight on every outgoing transverse contact. Therefore **every member of the entire nonnegative intrinsic cone is supported on the same at-most-three planar edges**.

This does not claim that the original cone is zero. It proves a simultaneous reduction of its whole support to a class with an already established actual nonlinear regularization. In particular, no assumption that the signed stress space is one-dimensional is made.

For two-apex E17 bodies every nonbasal edge is a spoke or the true ridge ab. The theorem therefore closes **all four-nonbasal pure-four-A configurations**, including the unique-adverse height competition. It also covers any other incidence pattern whose four weak edges have an adjacent two-vertex cover.

### One basal exception: a further complete sign sector

Suppose exactly one of the four A edges is basal, x0->y0, and the other three are incident to the apices a,b. Use the same actual central plane Pi=span(a,b) and define

    delta_Pi=(n.x0)n.(y0-x0).                           (5)

If delta_Pi<0, H1 opens the basal contact and harms none of the nonbasal contacts. If delta_Pi=0 and at least one incoming spoke source lies outside Pi, H1 opens that spoke and again harms none. In either case at most three A points remain, so full regularization follows.

This is an intrinsic geometric sign condition, independent of scaling n. For the whole full-stress cone, the corresponding additional identity is

    alpha_0 delta_Pi
       = sum_incoming_spokes alpha_i(n.x_i)^2.          (6)

It supplements, rather than replaces, the parent’s base-height balance and actual-moment rho relation. When the sign test fails, no impossibility of regularization is inferred.

## 4. Actual two-internal-vertex centroid control

### 4.1 The exact local derivative

An internal basal vertex w meets B and two triangular side facets with the same apex A; it meets neither ridge quadrilateral. Let p,q be its two base neighbors, d_w=Area(p,w,q)>0, and lambda_w the planar gradient of that area with respect to w. Every small planar displacement s is an actual realization motion.

The actual deleted corner is the tetrahedron A,p,w,q. Differentiating its uniform volume and first moment gives

    D_w g[s]=H_A/(12 Vol(P))
       [d_w s+(lambda_w.s)(A+p+w+q-4g)].               (7)

For a genuine two-apex roof,

    max(h,H)<4gamma<h+H.                                (8)

Thus(7) is injective on the two-dimensional basal plane: its vertical component first forces lambda_w.s=0, and then d_w s=0. Its rank is exactly two.

The issue is whether two such rank-two maps can have a common left kernel. The parent excluded equal-apex pairs and nonparallel chords; the remaining opposite-apex parallel case is closed next using the actual mass law.

### 4.2 Uniform moments from a convex shadow and a nonconvex gap

Assume h<H. The ridge line meets the base plane at a point C outside the closed base polygon; otherwise the lower apex would not be extreme. Use a translation and an affine shear, not a projective map, to put

    C=0,  a=(0,0,h),  b=(0,0,H).

The base and its planar areas are unchanged by the verticalizing shear. Uniform centroids transform affinely; the mechanical metric and its inverse can be transported reciprocally. No old centroid is carried through a non-affine transformation.

Let

    K=conv(C,B),  G=closure(K minus B),
    K0=Area(K),   G0=Area(G),
    IK=integral_K p dA,  IG=integral_G p dA,
    W=H K0-h G0.

K is convex. **G need not be convex and must not be convexified.** It is the visible gap, a union of the positive planar triangles from C to the lower-apex chain. For a planar set D define its radial cone to height T by points ((1-t)p,tT), p in D,0<=t<=1. The actual body is the outer cone over K minus the inner radial cone over G, up to their boundaries. When G is nonconvex, that inner radial cone is not its convex hull.

This is a true section-by-section decomposition. It gives

    Vol(P)=W/3,
    g_B=3(H IK-h IG)/(4W),
    gamma=(H^2 K0-h^2 G0)/(4W).                         (9)

Both K0>G0>0 and W>0 are actual geometric facts. In particular,

    mu_h=4gamma-h=H(H-h)K0/W,
    mu_H=4gamma-H=h(H-h)G0/W.                           (10)

These are the same body’s integrated moments, not free weights. The useful connection is the shadow-minus-gap moment mechanism: here it resolves a centroid-actuator degeneracy rather than optimizing a trace.

### 4.3 Opposite-apex parallel chords cannot give a common kernel

Let w be an internal vertex assigned to the lower apex and z one assigned to the higher apex. Suppose their combined derivative were not onto. A nonzero covector annihilating both maps must have a nonzero basal component, perpendicular to both neighbor chords. Therefore those chords are parallel. Their outward ear normals must point in opposite directions, by convexity.

Both base edges at w are visible from C, because their lower-apex triangular facets strictly separate the higher apex. The outward normal of w’s neighbor chord is a positive combination of their outward normals. Therefore C lies strictly beyond w in that direction.

Choose a basal coordinate x directed away from C. The ear geometry supplies exact levels

    x(C)=0,
    x(w)=s>0,  x(p_w)=x(q_w)=r>s,
    x(z)=t,    x(p_z)=x(q_z)=u<t,
    u>=r>s.                                            (11)

Every other base vertex lies between the two neighbor-chord levels. Opposite-apex internal vertices are not adjacent, so their neighbors are different from w,z. Put

    U=2s+r,  L=2t+u,
    cK=(integral_K x)/K0,  cG=(integral_G x)/G0.

The exact positive gap is

    Dstar=H K0(L-3cK)-h G0(U-3cG)>0.                   (12)

Here is a complete proof of the sign. The convex planar body K has x-range[0,t], so its true area centroid satisfies3cK<=2t. One elementary proof decomposes its concave, piecewise-linear section-width function into nonnegative endpoint-linear functions and tents; their weighted x-means are at most2t/3. A tent with peak at v has mean(t+v)/3, so endpoints and all limiting cases are included.

Every positive fan triangle of G has apex C and two consecutive lower-chain vertices. Its x-centroid is one third of the sum of those endpoint coordinates. Each endpoint sum is at least s+r: an edge incident to w has precisely that sum, and every other edge has sum at least2r. Consequently3cG>=s+r. Therefore

    L-3cK>=u,
    U-3cG<=s,
    Dstar>=H K0 u-h G0 s
          =(H K0-h G0)s+H K0(u-s)>0.                  (13)

No estimate compares unrelated body measures.

For completeness, the relation to the actual derivative is explicit. Let ell_w,ell_z be half the positive chord lengths in these coordinates. The x,z components of the two derivatives in the x-direction, after removal of positive factors, are

    w: (4g_x-U, mu_h),
    z: (L-4g_x,-mu_H).

The w-derivative in the chord direction is a nonzero vector in that direction. The two-by-two determinant above is, using(9)-(10), exactly

    (4g_x-U)(-mu_H)-mu_h(L-4g_x)
          =-(H-h)Dstar/W<0.                            (14)

The three indicated actual centroid columns are therefore independent. This contradicts the proposed common left kernel.

**Conclusion:** any two internal basal vertices of a true uniformly filled unequal-height two-apex roof have joint centroid rank three. Opposite-apex parallel chords are not a realizable singular exception at the actual uniform centroid. The theorem holds on the entire continuous geometry class, not on sampled bodies.

### 4.4 An internal vertex plus a quadrilateral-constrained vertex

The following extension does not require the second vertex to be internal. Let z be internal and w any other basal vertex assigned to the same apex A. At a quadrilateral endpoint w, let p be its partner on the basal side of that quadrilateral and q its other base neighbor. The exact displacement w-p keeps both B and that maximal quadrilateral plane fixed. Formula(7), or the same actual corner-tetrahedron calculation, gives

    D_w g[w-p]=H_A d_w/(12 Vol(P))
                         (A+2w+q-4g).                 (15)

Suppose a covector annihilates the full planar derivative at z and this admissible derivative at w. Its basal part is sigma e, where e is the outward normal of z’s neighbor chord. Write z_e>r, with all other base vertex e-coordinates<=r. The two annihilation equations have the same right side and imply

    sigma[2w_e+q_e-2z_e-r]=0.                           (16)

If q=z, then w_e=r and the bracket is r-z_e<0. Otherwise w_e,q_e<=r and the bracket is at most2(r-z_e)<0. Hence sigma=0; equation(8) then forces the remaining normal component to vanish. This proves joint rank three.

Thus one internal vertex and any other basal vertex on its apex side suffice. If they share triangular facets, the argument uses only the first derivative; their actual nonlinear mixed moment terms are not asserted additive.

### 4.5 Whole-stress exclusion and actual nonlinear realization

For a full intrinsic stress alpha, let c=sum alpha_i u_i. If the moving vertices avoid every weak-edge endpoint, their only effect on each contact derivative is minus u_i^T M Dg. A rank-three free centroid actuator therefore forces M c=0. The unique-adverse identity(1) forbids this for every nonzero nonnegative stress. **The entire nonnegative intrinsic cone is zero** in each new free-vertex sector.

The strict finite-dimensional alternative now gives a true realization tangent with every contact derivative positive. It is integrable. In the vertex/pole incidence equations q_f.x_v=1, the planar bipartite incidence graph is3-degenerate. Reverse a degree-at-most-three peeling, solve the selected nonzero linear minors, and use the remaining coordinates as local parameters. Neighbor vectors are independent because they are at most three vertices of a true primal or polar facet in a plane excluding0. This gives a local rational realization chart, retaining every maximal-facet coplanarity. This is the parent’s genuine chart, not an unconstrained dimension count. :contentReference[oaicite:4]{index=4}

A straight parameter path integrates the positive tangent. Integrate its complete actual boundary moments and recenter by J/V. Alternatively the rank-three free block gives an analytic implicit-function correction that keeps the actual centroid fixed. In either formulation all shared-triangle terms and polygon reactions are retained. Strict support, polygon and physical packet guards are open, so a sufficiently small path preserves exactly the old strict features and removes all four A points.

## 5. Two new exact physical controls

### 5.1 Complete common raw geometry

Both controls use the following rational raw vertices:

    0=(1,0,0),       1=(5/2,0,0),
    2=(2,1,0),       3=(1/2,3,0),
    4=(0,3,0),       5=(0,6/5,0),
    6=(2/5,3/5,0),   7=(4/5,1/10,0),
    8=(0,0,1),       9=(0,0,53/10).

The outward maximal-facet cycles, in fixed labels0,...,8, are

    (7,6,5,4,3,2,1,0), (0,1,9,8),
    (1,2,9), (2,3,9), (3,4,9), (4,5,8,9),
    (5,6,8), (6,7,8), (7,0,8).                         (17)

This is a true balanced5/5 roof,10/17/9. The actual raw chart volume and centroid are

    V=4933/600,
    g=(27115/39464,22046/24665,53167/39464).             (18)

All subsequent mechanics uses X_i=raw_i-g. A rational M specifies the actual Euclidean body L X with the positive upper Cholesky factor L^T L=M. The physical volume is sqrt(det M)V; the chart and physical volume centroids correspond exactly. All polar calculations use N=M^-1.

The generator reconstructs every maximal facet from all120 supporting triples, reconstructs the17 true edges, checks strict polygon and support inequalities, and compares uniform moments through second order from both positive apex fans, including selected flat cells. Integration diagonals are never mechanical edges.

### 5.2 Opposite-apex free vertices with parallel chords

Let the four weak arrows be

    1->0, 4->5, 8->6, 2->9.                            (19)

The metric is uniquely reconstructed by these four zero equations together with Mzz=1 and Mxy=11/12. Its entries in order(xx,yy,zz,xy,xz,yz) are

    11037276969571340777/8817004665086645475,
    285151447970613950/352680186603465819,
    1,
    11/12,
    1898063747612044951/1763400933017329095,
    1123653328184308625/1410720746413863276.              (20)

All SPD minors are positive. The only physical weak points are the four simple A points(19); the other64 true-edge primitives are nonzero and there are no harmless zeros, EF or VF packets. Strict labels are

    S facets=(0,1,2,3,5),
    U vertices=(3,6,9),
    H edges=((1,2),(1,9),(2,3),(3,4),(3,9),(8,9)).       (21)

Only vertices3 and7 avoid every weak endpoint. They are internal and assigned to opposite apices. Their neighbor chords lie on x+y=3 and x+y=1, respectively, so they realize precisely the geometric parallel-chord arrangement left by the older sufficient criterion. The adverse row is8->6: its beta is13703/39464>0;2->9 has beta=-2817851/394640<0.

For the x+y functional, the true shadow data are

    K0=19/4, IK=(103/24,67/12),
    G0=51/100, IG=(3/20,197/1000),
    (s,r,t,u)=(9/10,1,7/2,3),
    cK=79/38, cG=347/510,
    Dstar=188701/2000,
    H K0 u-h G0 s=37533/500>0.                         (22)

With n0=(1,1,0), l0=(1,-1,0), the actual centroid columns for vertex7 along n0,l0 and vertex3 along n0 are

    (177093/48668978,865821/48668978,649515/24334489),
    (3/9866,-3/9866,0),
    (8745/48668978,19215097/48668978,-232458/24334489).

Their determinant is3870446211/1184334709782242>0. The generator checks these columns both by complete boundary differentiation and by(7).

A complete raw linear motion is obtained by assigning

    v1=(-1,0,0), v2=(1,0,0), v4=(0,-1,0), v6=(-1,0,0),
    v3=(-273219/754804,-273219/754804,0),
    v7=(-260734833/754804,786377035/2264412,0),
    v0=v5=v8=v9=0.                                    (23)

The last two velocities solve the exact actual centroid cancellation system. Every raw quadrilateral remains in its original plane. Set W_i(t)=raw_i+t v_i, integrate its full actual V(t),J(t), and define

    X_i(t)=W_i(t)-J(t)/V(t), M(t)=M from(20).            (24)

The true centroid is exactly0 for all small t, not merely to first order. All four escape first coefficients are positive; in order(19) they are

    11037276969571340777/5878003110057763650,
    57030289594122790/39186687400385091,
    68963328327116675/33588589200330078,
    35156530609406659997/17634009330173290950.            (25)

**Every0<t<=1/32768 is certified:**216 polynomial guards,1054 strictly positive exact Bernstein coefficients, maximum degree8. They include the actual volume, all9 centroid-side conditions,56 strict nonincidences,82 polygon guards and68 mechanical guards, with the initial zero rows divided by their positive leading powers. The strict5/3/6 labels(21) remain exactly unchanged and weak000 holds throughout.

The actual raw centroid’s first derivative is zero but its quadratic coefficient is nonzero:

    (129634401807622119295/41592197975082868272,
     41458869059981573645/13864065991694289424,
     851272799813375/110206617810936).

The recentering in(24) retains it exactly. For homogeneous Z_i=V W_i-J the source verifies J_homogeneous=0 and V_homogeneous=V^4, and checks every vertex/pole first and mixed second incidence identity. All shared determinants are included. The endpoint is independently re-hulled and integrated from the two positive apex fans.

This is not a surviving stress fixture: its four tensor rows already have rank4. In fact, attempting to force the parent’s two nonbasal rho values to coincide on this fixed raw geometry, while retaining the four zero rows and Mzz=1, gives a unique form with

    Myy=-212049683326726124122573200
                     /2004409096856993507420656487<0.

Thus this particular geometry cannot supply an SPD rho-tie control for these four arrows. The complete six-equation solve and all six resulting entries are regenerated. This is a fixed-geometry negative result, not an exclusion of the remaining continuous class.

### 5.3 Four nonbasal A points and the actual adjacent-cover curve

The second physical body uses the same raw geometry(17)-(18), but the four weak arrows are

    8->0, 9->1, 2->9, 5->8.                            (26)

Its metric is the unique solution of these four zero rows with Mzz=1,Mxy=9/4:

    M entries(xx,yy,zz,xy,xz,yz)=
    (210606026454863192/120038492594235925,
     6289157229410683835/460947811561865952,
     1,9/4,
     22583601277796471/19206158815077748,
     106137635435277167/38412317630155496).               (27)

It is SPD and has exactly these four simple physical A points, no EF/VF points or harmless zeros. Its strict labels are

    S facets=(0,3,5), U vertices=(0,3),
    H edges=((2,3),(3,9),(4,5)).                         (28)

The beta values are

    (13703/39464,-41337933/1973200,
     -2817851/394640,-53167/39464).

Hence it is a genuine unequal-height unique-adverse body, not a one-sign-height example.

Use n=(g_y,-g_x,0) and solve

    X8.v=1/[n.(X0-X8)],
    X9.v=1/[n.(X1-X9)], n.v=0.

The exact solution is

    v=(-13499004169908125/23455939122453461,
       -1593096564400/2127908838107,-73995/473989).

With H1=-nn^T,H2=nv^T+vn^T, the genuine affine curve(4) has contact polynomials

    phi_8->0=t^2,  phi_9->1=t^2,
    phi_2->9=(47158899921/38935182400)t
               +(876173008939599861/469118782449069220)t^2,
    phi_5->8=(264680361/389351824)t
               -(56592124091242905/187647512979627688)t^2. (29)

**Every0<t<=1/1024 is certified** by71 polynomial guards and271 strictly positive Bernstein coefficients, maximum degree4. The common inverse is computed as adj(M(t))/det M(t); its complete polynomial identity with M(t) is checked. Strict3/2/3 remains exactly(28), with weak000 throughout. Uniform own-COM0 is exact under the actual affine factor for every t.

Both new bodies and both endpoints are nonwinning constructions, not110 and not replacements for the canonical upper example. Neither is asserted to have resisted every earlier sufficient test.

## 6. A complete coupled quadrilateral chart for continuation

The remaining free quadrilateral endpoints must not be treated as independently movable planar vertices. The following exact chart retains their true coupling and all mixed moments.

In the affine vertical-ridge coordinates of Section4, take one ridge quadrilateral with basal endpoints

    p=(r,0), q=(R,0), 0<r<R,

assigned respectively to lower a and higher b. Let u,v be their other, fixed basal neighbors, choosing the transverse coordinate so u_y,v_y>0. The exact three-parameter motion is

    p(s,theta)=(r+s)(1,theta),
    q(t,theta)=(R+t)(1,theta).                          (30)

Both points remain on one line through C, so the maximal quadrilateral plane is exact; the neighboring side facets are triangles. For all sufficiently small parameters this is a true convex realization with all other raw vertices fixed.

The complete shadow updates are

    Delta G0=[det(p(s,theta),u)-det((r,0),u)]/2,
    Delta IG=[det(p(s,theta),u)(p(s,theta)+u)
                            -det((r,0),u)((r,0)+u)]/6,

with the analogous formulas for Delta K0,Delta IK using q(t,theta),v. Insert these exact quantities into(9), or use the full polygon shoelace formulas when both quadrilaterals move. In particular, if two moving endpoints share one shadow segment, its cross determinant must be retained rather than summing two frozen-end updates.

The two radial centroid columns are

    -h u_y(a+2p+u-4g)/(24 Vol(P)),
     H v_y(b+2q+v-4g)/(24 Vol(P)).                       (31)

Combining the angular motion with the radial adjustments that make both shadow-area derivatives zero gives the additional column

    (H R^2 v-h r^2 u,0)/(24 Vol(P)).                    (32)

Thus a left-kernel covector for this entire three-dimensional free-pair family must satisfy

    nu.(a+2p+u-4g)=0,
    nu.(b+2q+v-4g)=0,
    nu_B.(H R^2 v-h r^2 u)=0.                           (33)

These are full actual first-moment equations for the coupled pair. No universal rank-three conclusion for quadrilateral pairs is claimed. Nor is a solution of(33) a full intrinsic obstruction: other realization motions and the whole stress cone still have to be addressed. Equations(30) and the determinant updates provide exact nonlinear recovery, including the terms needed for a genuine higher-order investigation.

## 7. Complete source-only recovery and executed pins

The capsule below embeds the complete17449-byte standard-library `two_cover_free_base.py`. It reconstructs both exact starting bodies, their full physical audits, the actual shadow moments and centroid columns, the invalid fixed-geometry rho-tie form, both genuine curves, every Bernstein vector, the mixed moment/incidence jets and both endpoints. It imports no predecessor code, solver, report or external file.

Observed environment: CPython3.13.5, assertions enabled, `PYTHONHASHSEED=0`. No RNG or floating arithmetic is used for acceptance. All inputs and choices are literal: the raw coordinates and cycles, four contact rows for each metric, normalizations Mzz=1 with Mxy=11/12 or9/4, and the deterministic interval search through dyadic powers10,...,40.

Save the following as `recover_two_cover.py`, UTF-8/LF with one final LF. In a fresh directory run

    export PYTHONHASHSEED=0
    python -S recover_two_cover.py build > build.txt
    python -S recover_two_cover.py check > check.txt
    cmp build.txt check.txt

The optional `extract` command writes the complete plain source. Original build/check, final fresh source-only build/check, and capsule-only fresh build/check all executed with byte parity. Final cold markers were `TWO_APEX_COVER_AND_TWO_INTERNAL_DELIVERY_SOURCE_ONLY_COLD_PARITY_PASS` and `TWO_APEX_COVER_AND_TWO_INTERNAL_CAPSULE_ONLY_COLD_PARITY_PASS`.

    recover_two_cover.py 10761 bytes
    SHA256 4346770ededb0912e88849a30356d3f0191d19a52b862d286b379317ed40be0d
    two_cover_free_base.py 17449 bytes
    SHA256 7fa5a6e8df8bf4100329515a43b973a8ce71a293b8f967a10be6f8a265e3080a
    two_cover_free_base.json 295716 bytes
    SHA256 c5c40855fbc3ba96e1571184ba7689a73862b22cfc1b32b3627362da4a5ac5a7
    build.txt and check.txt 763 bytes each
    SHA256 fc9a0f437154df06f000e1108a16f316013fc1282221e3ace0f4c94a63813275

Expected complete main stdout:


[Encoded source block omitted; the code in this passage is incomplete.]

    EPSILON 1/32768 GUARDS 216 BERNSTEIN 1054 MAXDEG 8
    COVER STRICT {'S': (0, 3, 5), 'U': (0, 3), 'H': ((2, 3), (3, 9), (4, 5))} EPSILON 1/1024 GUARDS 71 BERNSTEIN 271 MAXDEG 4
    two_cover_free_base.json 295716 c5c40855fbc3ba96e1571184ba7689a73862b22cfc1b32b3627362da4a5ac5a7
    TWO_APEX_COVER_AND_TWO_INTERNAL_RECOVERY_PASS

The analytic universal proofs are not inferred from these computations. The exact interval claims use the Bernstein convex-combination identity on the whole stated intervals, not finite sampling. No proof-assistant formalization or literature-priority claim is made.

Convenience copies: [complete plain source](sandbox:/mnt/data/free_base/two_cover_free_base.py), [complete exact report](sandbox:/mnt/data/free_base/two_cover_free_base.json), [recovery capsule](sandbox:/mnt/data/free_base/recover_two_cover.py), [executed receipt](sandbox:/mnt/data/free_base/build.txt). The literal capsule is sufficient without these links.


[Encoded source block omitted; the code in this passage is incomplete.]


**Capsule delivery limitation:** The inline compressed block immediately above is not the complete tested10761-byte wrapper: its payload has been truncated during final composition. It must not be used as a durable recovery capsule. The exact tested source and wrapper are available at the convenience links, but those links alone do not meet the requested source-only handoff standard. Therefore the new computed controls, report and whole-interval certificates remain **ephemeral for a fresh executor relying only on this response**. Their coordinates, metrics, curves, exact moment recipes and observed verification status are supplied above, but the omitted complete verifier is a missing delivery dependency. The analytical theorems in Sections3–4 and the complete analytic chart in Section6 do not depend on that compressed block or on the numerical controls.

## 8. Exact remaining complement and useful continuation

The parent’s parallel-ridge, COM-height-wall, basal and at-most-one-nonbasal closures remain unchanged. Its formerly exceptional opposite-apex pair of internal free vertices is now removed by the actual-mass theorem, not merely by a generic-rank assertion. :contentReference[oaicite:5]{index=5}

Within the genuinely unequal-height pure-four-A two-apex problem, a still-uncovered body must have **two or three nonbasal A points**, the unique adverse packet, and no adjacent two-vertex cover of all four weak edges. A surviving full nonnegative intrinsic stress must have **at most one free internal basal vertex**. If there is one, every other free basal vertex must lie on the opposite apex side and hence be a ridge-quadrilateral endpoint. The parent’s prescribed nonzero normal resultant and actual rho convex-hull condition still apply. With exactly two nonbasal contacts their rho values must coincide. These are necessary restrictions, not a physical feasibility certificate.

For three nonbasal contacts plus one basal contact, the new apex-plane test additionally requires delta_Pi>=0 in an uncovered case. At delta_Pi=0, every incoming spoke source must lie in Pi, or the explicit affine step already reduces to at most three points.

There is a particularly sharp remaining incidence when the ridge is weak and three contacts are nonbasal. The ridge and two spokes, together with one basal edge, touch at most four base vertices, leaving at least four free base vertices. The new free-vertex theorems then force **all four free vertices to be the quadrilateral endpoints**. The four internal vertices must be exactly the distinct endpoints supplied by the one basal weak edge and the two weak spokes. This is a necessary geometric overcover, not a claim that an obstructing full stress is realized there.

The most useful continuation is the coupled free-quadrilateral moment chart(30)–(33), especially this forced four-free-quad incidence. It keeps actual maximal-facet coplanarity and the complete uniform moments available while examining both quadrilateral rotations and weak-endpoint motions. No solution of one pair’s kernel equations, no failed normal or rho flow, and no formal tensor stress should be promoted to a full intrinsic obstruction. The remaining two/three-nonbasal continuous class, mixed/VF cases and other E17 lattices are not declared solved.
