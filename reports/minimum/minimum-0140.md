# minimum-0140

AI research report · 2026-09-20 UTC · [Export notes](../../catalog/coverage.md#text-records)

---

# UNEQUAL_WALL_AND_FREE_CHORD_REGULARIZATION_V1

## 1. Findings and precise boundary

**The entire apex-at-own-COM-height wall is regularizable.** Let a true facet B contain all vertices of a uniformly filled convex three-polytope except two apices. If one apex lies in the plane through the actual volume centroid parallel to B, and every physical weak equilibrium is simple A=VE, then there is an arbitrarily small genuine regularization preserving the full face lattice and exactly the original strict feature-labelled equilibria. This holds for any finite number of A points, not just four. The construction has positive escapes of order at most two and maintains the true centroid throughout.

Consequently, **every pure-four-A two-apex E17 configuration with at most one nonbasal weak edge is now closed, at all apex heights**: the new wall theorem handles the former zero-height exception, the inherited normal-height motion handles nonzero beta, and the literal parent handles a parallel weak ridge. Any finite basal A set plus one nonparallel nonbasal A edge is covered as well.

A second theorem closes a substantial part of the genuine unequal-height unique-adverse sector. Its **entire nonnegative intrinsic stress cone is zero** whenever there are two free internal base vertices assigned to the same apex, or two such vertices with nonparallel neighbor chords. In particular, three free internal base vertices suffice. These hypotheses concern the actual polygon and actual realization freedom, not independent motions of vertices on quadrilateral facets.

Two further advances are retained. Every surviving unique-adverse full stress has a resultant with a strictly prescribed nonzero normal component. A separate actual-moment ratio test closes another continuous sector and gives a necessary interval condition on the whole remaining stress cone.

The controls clarify the limits. A new rational pure-four-A body on the centroid-height wall has a wrong-sign fold on its **entire local base-pointwise-fixed, fixed-centroid, fixed-metric realization family**. This is stronger than failure of one frozen star, but is not a full obstruction: its full intrinsic and tensor ranks are four. A normal-metric correction and genuine coupled shape motion regularize it. Another exact body realizes the unique-adverse sign conflict, where either sign of the normal-height-only motion creates an unwanted strict pair, yet actual free-star and affine mechanisms succeed.

The full unequal-height problem is not closed. No body with an obstructing full nonnegative intrinsic stress cone, and no obstruction to arbitrary-small unrestricted regularization, is supplied. Non-B8 E17 lattices and mixed EF/VF points remain outside these theorems. No110 attainer, census change, or improvement of34<=C_min<=622 is claimed.

## 2. Inputs and evidence status

The complete new1650-line `research-journal(20260920-185950).md` was read consecutively through EOF, including the full literal parent and its executable capsule. It has308730 UTF-8 bytes and SHA-256 `8731c1f26dec74b84ce2cd6cf66f496471b6b6148ec72eb2a5ec211450660b16`.

The authoritative parent is `minimum-0135`, title `PARALLEL_RIDGE_FOUR_A_COMPLETE_V1`. Its36449-byte compact JSON envelope authenticates to `06bcaecddd17941df222ba6114e96630b6ef21dee59acab656dfe79ce8456e4e`. Serialization is UTF-8, `ensure_ascii=False`, separators `(',',':')`, keys `version,result_markdown`, one terminal LF inside the Markdown string and none after the envelope. No source conflict was found, and the new computation has no missing exact dependency. The parent's full parallel-ridge theorem remains accepted and is not reproved here.

The inherited basal flow, true realization chart and polygon-reaction stress equations are used as working premises. In particular, the basal construction supplies a genuine tangent direction positive on every basal A row, not merely a sequence of nearby bodies.

The new source imports no predecessor code or report. Original build/check, fresh source-only build/check and fresh capsule-only build/check all executed with byte parity. Exact acceptance uses only rational arithmetic in the Python standard library. The continuous theorems below are analytic; the controls and interval certificates do not substitute for their proofs. No proof-assistant formalization or priority claim is made.

## 3. A facet-pointwise projective family with the endogenous centroid

Use coordinates with B in z=n.X=0 and P in z>=0. Let g0 be the actual raw volume centroid, gamma=n.g0>0, and x=X-g0. Let M0 be the one original metric and N0=M0^-1. Define the actual centered moments

    Sigma=E_P[xx^T],  v=Sigma n,  sigma=n^T Sigma n>0,
    mu=E_P[x(n.x)^2].

For small tau, apply T_tau(X)=X/(1+tau z), whose denominator is positive on the whole body. Uniformly refill the image. Its actual moments are

    V_tau=integral_P (1+tau z)^(-4) dX,
    J_tau=integral_P X(1+tau z)^(-5) dX,
    g_tau=J_tau/V_tau.                                  (1)

The fourth power is the actual projective Jacobian. These are not transported uniform masses. Correct the center by

    F_tau(Y)=Y+(n.Y)(g0-g_tau)/(n.g_tau).                (2)

This affine map fixes B pointwise, sends g_tau exactly to g0, and has determinant gamma/(n.g_tau)>0. Thus K_tau=F_tau(T_tau(P)) is an actual uniformly filled realization at its true centroid g0. Every maximal-facet coplanarity is preserved.

Independently use the metric pencil

    M_s=M0+s nn^T>0,  N_s=M_s^-1.                       (3)

An actual affine factor L_s with L_s^T L_s=M_s turns the chart into one Euclidean body L_s(K_tau-g0). The primal and polar do not receive independent metrics or independent centers. Every basal weak escape stays identically zero for all small(tau,s), because its endpoints are fixed and n.u=0.

### Complete first and second contact jets

Put

    ell=5v/gamma,
    k=(-5+25sigma/gamma^2)v-15mu/gamma.

For a vertex with raw height H_i=n.X_i, actual centered position after(1)-(2) is

    x_i(tau)=x_i+tau H_i(ell-x_i)
                +tau^2[H_i k+H_i^2(x_i-ell)]+O(tau^3). (4)

For a weak arrow x_i->x_i+u_i, define h_i=n.x_i, d_i=n.u_i, H_i=gamma+h_i and

    beta_i=h_i d_i,
    q_i=H_i u_i+d_i x_i,
    kappa_i=ell^T M0 q_i-d_i x_i^T M0 x_i.

Its actual escape has the expansion

    phi_i(tau,s)=beta_i s+kappa_i tau+a_i s tau+b_i tau^2
                              +O(tau^3+|s|tau^2),       (5)

where

    a_i=d_i[(gamma+2h_i)n.ell-2gamma h_i-3h_i^2-h_i d_i],
    b_i=k^T M0 q_i+H_i d_i|ell-x_i|_M0^2
                                      -(2H_i+d_i)kappa_i. (6)

There is no pure s^2 term in this linear metric pencil. To derive(4), expand the two actual integrals in(1), divide by V_tau, and then apply(2). The first displacement is H_i(ell-x_i); subtracting source and target gives u_i'=d_i(ell-x_i)-(H_i+d_i)u_i. Substitution gives(5)-(6). Thus the same actual third moment mu enters every row, and it cannot be replaced by fitted cell means.

These formulas are reusable beyond the wall theorem. The recovery independently checks them at both stationary and nonstationary actual controls against full boundary-moment expansions.

## 4. Complete centroid-height-wall theorem

Assume one apex a has raw height H_a=gamma. The other apex has H_b>gamma, because the centroid height is strictly below the maximum vertex height. Every nonbasal beta is strictly negative except possibly one simple A point e whose source is a. A simple A source has only one outgoing weak edge: its radial supporting plane exposes exactly that edge. For e, h_e=0 and d_e!=0. Basal rows have beta=0.

If no such e exists, s<0 in(3) opens every nonbasal point, leaving only basal points. Otherwise set

    chi=kappa_e,  C=a_e=5d_e sigma!=0.                  (7)

The nonzero cross coefficient follows from the positive variance of the actual full-dimensional body, not from a generic-rank hypothesis.

If chi!=0, choose

    epsilon=min(1, min_{beta_j<0}[-beta_j/(2(1+|kappa_j|))]),
    tau=sign(chi) epsilon t,  s=-t.

Omit an empty minimum. Then e opens with first coefficient epsilon|chi|>0, and every other nonbasal first coefficient is at least -beta_j/2>0.

If chi=0, use the actual b_e from(6) and choose

    epsilon=min(1, |C|/[2(1+|b_e|)],
                    min_{beta_j<0}[-beta_j/(2(1+|kappa_j|))]),
    tau=-sign(C) epsilon t,  s=-t.                      (8)

All other nonbasal points again open to first order. The exceptional row has second coefficient

    b_e epsilon^2+|C|epsilon >= |C|epsilon/2>0.           (9)

Every basal contact remains exactly zero during this simultaneous actual motion.

Finish with the inherited basal radial motion, genuine quadrilateral lift and exact centroid correction. They can be chosen analytically in the preceding small parameter: retain the same initially nonzero plane-intersection minors. If the slowest opened nonbasal row has leading term c_i t^r, r=1 or2, take the basal parameter delta=eta t^r. Its basal first coefficients are all positive. Choose eta>0 small enough that its contribution to each order-r nonbasal coefficient has magnitude less than c_i/2. Rows already positive at lower order remain positive. This gives an actual analytic full regularization with every weak escape positive at order at most two.

All remaining physical packet and strict-feature guards are open. Preserve each original strict equilibrium inequality, and a strictly positive excluding primitive for every absent packet. Harmless zero primitives need not individually disappear. Since the original physical weak points were simple A, positivity is the no-new-pair side of each complete packet. The true lattice and all original strict labels therefore persist with no new strict or weak equilibria. This proves the theorem for any finite A set under its two-apex wall hypothesis.

### The whole intrinsic cone, including the stationary wall

Let R be the actual own-centroid contact derivative on the full true realization tangent space. A full nonnegative stress alpha satisfies R^T alpha=0 there, or Q^T alpha=C_inc^T lambda in vertex/pole coordinates with all polygon reactions retained.

Testing the actual normal affine motion gives sum alpha_i beta_i=0. At the wall, therefore, alpha can be supported only on basal rows and e. The basal positive tangent rules out a nonzero basal-only stress, so every nonzero alpha has alpha_e>0. Testing(1)-(2) gives alpha_e chi=0. Hence chi!=0 makes the **entire** nonnegative intrinsic cone zero.

At chi=0, emptiness of the original cone is not asserted. Instead the genuine curve(8) has weighted second escape alpha_e times the strictly positive quantity(9), for every nonzero cone member. Its facet reactions and actual second centroid response are already incorporated because this is a curve of true bodies, not a prescribed unconstrained Hessian.

There is an exact scale diagnostic: for the contact-zero normal metric predistortion on the basal/e subsystem,

    chi(s)=chi(0)+5s d_e sigma.                          (10)

Thus at most one normal scale can retain this particular first-order stationarity. That is necessary for a full stress, not sufficient for its existence. In physical coordinates its tensor equation also forces the resultant to be

    sum alpha_i u_i=alpha_e[u_e+(d_e/gamma)x_e].          (11)

No signed-stress dimension-one statement follows or is used.

## 5. Unequal heights: orientation of every adverse full stress

Now let 0<H_a<H_b with h_a=H_a-gamma!=0. In the unresolved sign-conflict sector, e is the unique positive-beta packet. It is either a->b with h_a>0, or a->B with h_a<0. All other nonbasal beta values are negative; there is no nonbasal zero in this sector. The classification and the positive coefficient of e are inherited; the following stronger resultant identity is new.

For any nonzero full nonnegative intrinsic stress, write c_alpha=sum alpha_i u_i. The basal tangent and normal metric test imply alpha_e>0 and at least one supported negative-beta row. Then

    h_a(n.c_alpha)=sum_i alpha_i(h_a-h_i)d_i>0.          (12)

The equality uses sum alpha beta=0. Every potentially supported nonbasal term other than e is strictly positive: for B->A it is H_a H_A; for b->B it is H_b(H_b-H_a); and for b->a it is(H_b-H_a)^2. Basal terms vanish. There is no second outgoing simple A from a. Thus

    n.c_alpha!=0,  sign(n.c_alpha)=sign(h_a).            (13)

This is a statement about the whole actual intrinsic cone, independent of how many signed stresses it contains.

More quantitatively, set w_j=-alpha_j beta_j/(alpha_e beta_e) on negative rows. These weights sum to1, and

    (n.c_alpha)/alpha_e
       belongs to beta_e conv{1/h_a+1/gamma, 1/h_a-1/h_b}. (14)

Both listed endpoints have the same nonzero sign as h_a. These weights are dual stress coefficients, not physical vertex masses.

### A second actual-moment test

For each nonbasal row define rho_i=kappa_i/beta_i, with kappa from the genuine projective family(5). If

    rho_e outside [min_{j!=e}rho_j, max_{j!=e}rho_j],     (15)

a line in the(tau,s) plane makes every nonbasal first coefficient positive. For example, when rho_e exceeds every other rho, choose r between them and tau>0,s=-r tau. For the opposite exterior choose tau<0. Basal rows stay exactly zero, and the genuine basal cleanup finishes.

Any surviving full stress must satisfy

    rho_e=sum_{beta_j<0} w_j rho_j.                     (16)

With exactly two nonbasal weak points, their two rho values must therefore be equal for a full first-order obstruction to survive this test.

The full second jet is useful at an equal-ratio boundary. If every nonbasal rho_i equals rho, take s=-rho tau+zeta tau^2. A sufficient condition for all second coefficients to be positive is

    (b_e-rho a_e)/beta_e
           > max_{j!=e}(b_j-rho a_j)/beta_j.             (17)

Choose zeta between the corresponding thresholds and then use the basal cleanup. Failure of(15) or(17) is only failure of this two-parameter mechanism, not nonregularizability.

## 6. A complete free-internal-chord sector of the adverse cone

Call a base vertex internal when it meets B and two triangular side facets with the same apex A, but neither ridge quadrilateral. Let its neighbors on the base be p,q. It is free when it avoids every endpoint of every weak edge. Every small displacement h parallel to B is then an actual one-vertex realization motion.

Put d_w=Area(p,w,q)>0 and lambda_w=grad_w d_w in the base plane. The actual deleted corner is the tetrahedron(A,p,w,q). Its uniform volume and first moment give

    D_w g[h]=H_A/(12V)
       {d_w h+(lambda_w.h)(A+p+w+q-4g)}.               (18)

The heights satisfy

    max(H_a,H_b)<4gamma<H_a+H_b.                        (19)

Indeed a positive fan from either apex has positive base cells with height sum H_A and positive cells involving the other apex with height sum H_a+H_b. Both occur because each apex is an actual vertex outside the other apex's base pyramid. Thus H_A-4gamma is strictly negative.

Formula(18) has rank two on the basal plane: its zero vertical component first forces lambda_w.h=0, and then d_w h=0. A full stress annihilates it at a free vertex. In physical Euclidean coordinates, with c_B the basal component of c_alpha,

    d_w c_B+[c_alpha.(A+p+w+q-4g)]lambda_w=0.           (20)

Hence c_B is parallel to the outward normal of the neighbor chord[p,q]. Two free internal vertices with nonparallel chords force c_B=0; equation(19)-(20) then forces n.c_alpha=0, contradicting(13).

### Same-apex parallel chords are also impossible for a full stress

Suppose the two chords are parallel and assigned to the same apex. Their outward senses must be opposite: each ear chord separates its own extreme vertex from all other base vertices. Orient a unit basal normal e outward at w and inward at z. Let a be the common e-coordinate of w's neighbors, and b that of z's neighbors. Then

    w_e>a>=z_e,  z_e<b<=w_e.

The weak inequalities allow adjacency, which must not be excluded. Write c_B=t e. The two equations(20) become

    t(A_e+2w_e+a-4g_e)=c_z(4gamma-H_A),
    t(A_e+2z_e+b-4g_e)=c_z(4gamma-H_A).                 (21)

Their left coefficients differ by

    2(w_e-z_e)+a-b >= w_e-z_e>0.

Thus t=0 and then c_z=0, again contradicting(13).

**Theorem.** In the genuine unique-adverse sector, two free internal base vertices assigned to the same apex, or two with nonparallel neighbor chords, eliminate the entire nonnegative intrinsic stress cone. Three free internal vertices always suffice by the two-apex pigeonhole argument.

This gives complete incidence sectors: in a3/7 roof any two free internal vertices work; in a4/6 roof any two free vertices in the three-internal-vertex side block work; in a5/5 roof either entire two-internal-vertex side block being free works. The nonparallel-chord alternative further includes pairs assigned to different apices. These are not selected-tree census deltas.

### From the stress theorem to an actual nonlinear body

The strict finite-dimensional alternative gives Rh>0 once the full nonnegative kernel is zero. This tangent is realizable, not merely formal. In true vertex/pole coordinates the incidence equations are q_f.x_v=1. Their planar bipartite incidence graph is3-degenerate. Remove a node of degree at most three; its remaining neighbor vectors are independent because they are vertices of a true polygonal primal or polar facet in a plane excluding0. Select a nonzero coordinate minor. Reverse the removals, taking the other coordinates as free parameters and solving the recorded linear systems. This is a local rational realization chart through the original body.

A straight path in its free coordinates integrates the chosen tangent while satisfying every maximal-facet coplanarity identically. All strict support and polygon inequalities remain open. Integrate the actual new boundary moments and subtract J/V. Its contact derivative is precisely R, so the positive leading escapes give the required full physical regularization. Adjacent mixed terms are thereby retained, even though only the first derivative was needed for this theorem. No polygon reaction was discarded.

## 7. New exact wall controls and a genuine restricted-modulus fold

### Complete common lattice and rational bodies

Use the following outward maximal-facet cycles in fixed labels0,...,8:

    (7,6,5,4,3,2,1,0), (0,1,8,9), (1,2,8), (8,2,3,9),
    (3,4,9), (4,5,9), (5,6,9), (6,7,9), (7,0,9).       (22)

Their true hull is10/17/9, with apex degrees3/7. It is neither a balanced5/5 body nor the parent's different parallel7/3 fixture. The raw vertices are

    0=(1,0,0),       1=(1,1/4,0),
    2=(0,1,0),       3=(-1/3,1,0),
    4=(-1,0,0),      5=(-1,-1/5,0),
    6=(8/39,-1,0),   7=(2/5,-1,0),
    8=(1,1,1),       9=(1,1,39/10).                     (23)

Actual raw V=29/8 and g=(178421/565500,18543/58000,1). Apply the actual affine shear

    S(X)=(X_x-g_x X_z, X_y-g_y X_z, X_z),
    X_i=S(raw_i)-e_z.                                  (24)

Write Xhat_i=S(raw_i). All mechanical calculations use the actual centered X_i, never the old raw reference. With

    k=100455305104/136161074439,
    M_Y=diag(1,k,Y),  N_Y=diag(1,1/k,1/Y),               (25)

the physical Euclidean body is diag(1,sqrt(k),sqrt(Y))X. It is uniform and has its own centroid0.

Two controls use Y=1 and

    Y*=593430910334618/1654957765056375.

Their only physical weak points are0->1,2->3,4->5,8->1. A third control uses

    k2=31133538128/14452485723,
    Y2*=113471256248581/175661462500875,

and replaces the last weak arrow by8->2. All three have exactly four zero primitives and no harmless zeros or EF/VF points. Their common strict labels are

    S=[0,1,3,4,6,8],
    U=[1,3,5,7,9],
    H=[(0,7),(0,9),(1,2),(3,4),(3,9),
       (5,6),(5,9),(7,9),(8,9)].                        (26)

The source reconstructs the full hull from supporting triples, checks all true edge intersections, both positive apex fans and second moments, and verifies that each radial supporting plane exposes exactly its designated weak edge.

There is also an entire unbounded normal-metric family: for every

    Y>6278456569/19777372875,

the primary body(23)-(25) has exactly the four stated A points and strict6/5/9 with labels(26). All68 primitive numerators are affine in Y after multiplying polar rows by positive Y. The recovery gives their complete coefficients and the exact common sign chamber. This is not inferred from the two selected Y values.

The actual projective diagnostic is

    chi(Y)=296715455167309/290343467553750-(57/20)Y,

with unique zero Y*. The relevant actual covariance column is

    Sigma e_z=(-1937009/56550000,-210647/5800000,57/100),

and the actual centered third moment is

    mu=(-7067669/226200000,-781527/23200000,713/2000).

At Y*, the direct facet-fixed projective coefficient of tau^2 is

    -32716818702238154507/7502475201588900000<0,

while its normal-projective cross coefficient is -57/20. These are true whole-body moments.

### The whole base-pointwise, own-COM modulus has the wrong sign

Let d=(Xhat_9-Xhat_8)/(29/10)=(-g_x,-g_y,1). Move raw Xhat_8 to Xhat_8+sigma d, holding every other raw vertex fixed, then apply the exact centroid repair(2). Its raw moments satisfy

    V(sigma)=29/8-sigma/8,
    D(sigma)=J_z(sigma)=29/8-sigma/16-sigma^2/32.

At the fixed critical metric M_Y*, the exceptional escape is exactly

    phi_8->1(sigma)=-sigma^2(p0+p1 sigma+p2 sigma^2)/D(sigma)^2,

where

    p0=32716818702238154507/4801584129016896000,
    p1=-2732509606335158981/4801584129016896000,
    p2=33885112142939881/2400792064508448000.

Here p2>0 and the discriminant is

    -4097584386794231861390294889551
       /67368573739577598865914101760000<0.              (27)

Thus every nonzero sufficiently small sigma has the wrong escape sign. The three basal A equalities remain exact; all other guards remain open, so an extra strict U at8 and strict H on1-8 are born. The two actual endpoints sigma=+/-1/65536 are also independently audited, each with strict6/6/10 and three A points. The all-orders local assertion follows from(27) and openness, not from those two samples; no fixed whole-interval certificate for every other source-only guard is claimed.

This curve parameterizes the entire restricted local realization family. The two fixed basal sides of the quadrilaterals meet at C=(1,1,0), so any nearby pair of apices must lie on one common line through C. Base-pointwise affine maps X->X+zv act transitively at a fixed apex-height ratio. The actual centroid fixes the three-parameter affine freedom uniquely, since its height is positive. The remaining ratio is one-dimensional, and the raw sigma above changes it monotonically from(39/10)/(1+sigma). Hence no arbitrary nonlinear motion fixing the whole base pointwise, its true centroid and this metric can open the exceptional point locally.

This is a genuine restricted-modulus obstruction, not a full intrinsic obstruction. At Y* even the contact tensors have rank4. Four true directions, each followed by the actual centroid repair, give the full contact derivative

    [k/16, 0, 0, 0],
    [0, 1/9, 0, 0],
    [0, 0, k/25, 0],
    [1156751929929601/669451633372548000,
     -234062820020491/41840727085784250,
     4366974990824521/2003013530702437500,
     15512593895843987/184591443025518750].              (28)

The columns are source0 along0->1, source2 along2->3, source4 along4->5, and free vertex6 along e_x. The final entry is positive. Every direction retains true coplanarity and true COM, so the full intrinsic rank is4. The fixture must not be presented as positive-full-stress coexistence. The order-two arc below certifies the coupled mechanism; rank4 already permits an order-one full regularization of this particular fixture.

## 8. Two completely certified regularization curves

Starting at the primary critical body, use raw polynomial vertices

    W8=Xhat_8+t d,
    Wi=Xhat_i+delta(t)(Xhat_j-Xhat_i)
                     for(i,j)=(0,1),(2,3),(4,5),
    Wi=Xhat_i for all other i.                          (29)

Use delta=t^2/100 for the principal curve. Retain also the earlier, nonwinning-in-order curve delta=t^3. The source motions on quadrilateral edges and the ridge-line motion keep both quadrilateral planes exactly; the other changed side facets are triangles.

Compute the complete actual raw V(t),J(t) from(22), D=J_z, and set

    X_i(t)=W_i-e_z+W_i,z[e_z V(t)-J(t)]/D(t),
    M(t)=diag(1,k,Y*-2t),  N(t)=M(t)^-1.                (30)

This is a complete rational recovery recipe, with all moment helpers in the capsule. The actual centroid is identically0 and the chart volume is V(t)^2/D(t); physical volume additionally has the common factor sqrt(det M(t)). Every shared-triangle determinant is retained.

The basal escapes are exactly

    (k/16)delta(1-delta),
    (1/9)delta(1-delta),
    (k/25)delta(1-delta).

For the principal curve every first coefficient is zero and the four second coefficients are

    6278456569/13616107443900,
    1/900,
    25113826276/85100671524375,
    41084114655566384819448917/28393117400413192050000000. (31)

They are all positive. For the cubic-basal companion the exceptional second coefficient is91299096380026362493/63095816445362649000>0 and the basal leading order is three. Its exact construction is preserved rather than discarded for having worse order.

**Both entire intervals0<t<=1/65536 are certified.** The principal curve has218 polynomial guards,4137 strictly positive Bernstein coefficients and maximum degree38. The cubic-basal curve has218 guards,5354 positive coefficients and maximum degree50. All original strict labels(26) persist and weak000 holds throughout.

Each certificate contains3 volume/centroid/metric guards,9 centroid-inside conditions,56 strict nonincidences,82 true facet-polygon guards and68 mechanical guards, with the original zero rows divided by their positive leading powers. Every coefficient is returned in the exact report. Both endpoints are independently re-hulled, integrated from two positive apex fans and fully mechanically recounted.

The mixed jets are independently audited. For homogeneous Z_i=D X_i, the identities are J_homogeneous=0 and V_homogeneous=V_raw^2 D^2. Every literal incidence satisfies q.h+x.k=0 and q.eta+x.xi+h.k=0. The straight-vertex second centroid coefficient is not zero:

    (-132719984467/206879692500000,
     -27748217461/21218430000000,
     -1163931/121945000).

It is canceled by the actual acceleration's linear centroid response. All metric cross terms and polygon-curvature terms are retained, not replaced by an independently adjustable center.

### A five-A negative control, not a four-point fixture

Keep(23) except replace6 by(0,-1,0) and7 by(46/195,-1,0). Its raw V is still29/8, but g=(56103/188500,55373/174000,1). Use the same actual shear/centering rule and M=diag(1,1069613120304/1506143316301,1). It has strict7/5/10 and **five** physical A points0->1,2->3,4->5,6->7,8->1, with no EF/VF or harmless zeros. Its complete actual audit is retained. It is covered analytically by the finite-contact wall theorem, but no separate whole regularization arc is claimed for this control.

## 9. A genuine unique-adverse control and the normal-only boundary

Use(23) with apex9=(1,1,4), and no preliminary shear. Its actual raw data are

    V=387/104,
    g=(1430293/4527900,148669/464400,529/516).

Put X=raw-g. The symmetric metric entries in order(xx,yy,zz,xy,xz,yz) are

    68002994209035631577/6121813828884811308,
    227537972413724/48913529787639,
    1,
    34255361688863267732/50504964088299693291,
    -22244005041925805229/7482216901970324932,
    -1.                                                 (32)

All leading principal minors are positive, and the recovered N is its exact inverse. This specifies a genuine Euclidean affine image of the uniformly filled centered body.

Its only physical weak points are0->1,2->3,8->1,9->3. All64 other primitives are nonzero, with strict labels

    S=[0,8], U=[1,3,5,7],
    H=[(0,7),(2,8),(3,4),(5,6)].

The beta values are exactly

    (0,0,13/516,-1535/129).

Thus the unique-adverse sign-conflict class is physically nonempty. Free internal vertices4,5,6,7 are assigned to apex9; the independently differentiated true centroid columns at4,5 have joint rank3 and agree with(18). The contact tensors have rank4 too. The two nonbasal moment ratios are

    63268049788024597081965955984/234442780673784968764489725,
    -17183610206102001668902883/1203577486067758953356159625.

They are unequal, so both the free-chord theorem and the ratio test apply. This is not a realized obstructing stress.

The normal-only motion M+s nn^T has a real limitation. For s>0 it opens8->1 but makes9->3 negative, creating U9 and H3-9. For s<0 it opens9->3 but creates U8 and H1-8. On **every0<|s|<=1/65536**, an exact65-guard two-sided Bernstein certificate preserves all other signs and positive definiteness. Each side has strict2/5/5 plus the two basal A points, not a valid full regularization. The two endpoints are separately audited. This is a whole-interval failure of the selected normal actuator, not an obstruction to the full realization motions proved available above.

## 10. Complete recovery and executed identities

Save the following capsule as `recover_wall.py`, UTF-8/LF with one final LF. It embeds the complete23025-byte standard-library source `wall_roof.py`: all exact inputs, hull/fan/polar mechanics, actual moment helpers, the stationary-fold and rank checks, the unbounded normal chamber, both regularization arcs, all mixed jets and all Bernstein vectors. No predecessor file or network is needed.

Observed environment: CPython3.13.5, assertions enabled, `PYTHONHASHSEED=0`. Run in a fresh directory:

    export PYTHONHASHSEED=0
    python -S recover_wall.py build > build.txt
    python -S recover_wall.py check > check.txt
    cmp build.txt check.txt

The optional `extract` command writes the complete plain source without running the audits. Original, fresh source-only and fresh capsule-only build/check all completed with matching source/report/stdout bytes. Final cold receipts ended `UNEQUAL_WALL_FINAL_SOURCE_ONLY_COLD_BUILD_CHECK_PARITY_PASS` and `UNEQUAL_WALL_FINAL_CAPSULE_ONLY_COLD_BUILD_CHECK_PARITY_PASS`.

    recover_wall.py 12967 bytes
    SHA256 4355ec9dbd5fe7983b12b9f8146d29f5aebd89a5fb3d4c13943ca89626b519f1
    wall_roof.py 23025 bytes
    SHA256 2dc3927bbb593a1ca0a56f3054694e3ed85c767152a597be431e8b8198e798e7
    wall_roof.json 2463311 bytes
    SHA256 cb0f1b0ba0394aa0b9251fb4e0d0c79b9c967017863ce73e1250125bad514de6
    build.txt and check.txt 657 bytes each
    SHA256 7fb094a3f86c9264da93fdd0f8fe0a27910ea896aeda6f8506a5934eaa31e7d0

Exact main stdout:


[Encoded source block omitted; the code in this passage is incomplete.]

    cubic_scale_arc EPSILON 1/65536 GUARDS 218 BERNSTEIN 5354 MAXDEG 50
    wall_roof.json 2463311 cb0f1b0ba0394aa0b9251fb4e0d0c79b9c967017863ce73e1250125bad514de6
    UNEQUAL_WALL_AND_FREE_CHORD_RECOVERY_PASS

Convenience copies: complete source (`wall_roof.py`), exact report (`wall_roof.json`), capsule (`recover_wall.py`), executed receipt (`build.txt`). The literal capsule below is sufficient without these links.

```python
"""UNEQUAL_WALL_AND_FREE_CHORD_REGULARIZATION_V1 exact recovery.
CPython3.13.5 standard library, assertions, PYTHONHASHSEED=0.
python -S recover_wall.py build|check|extract
Parent minimum-0135,
SHA256 06bcaecddd17941df222ba6114e96630b6ef21dee59acab656dfe79ce8456e4e.
"""
from pathlib import Path
import base64,hashlib,subprocess,sys,zlib
assert __debug__
DATA=(
    'c-qZ8YggmAlHd6izGu!}+d+ZYA%P^VK1(;y4bwatXrReveH`0K91=V2JP6G8f8VN-<VO;EX71h(+h>N@Qb{V6O7&97x~_k_IR5(W'
    '@QZVQ_~napcyZ*MTpu4hA3tASA34{@pT2!Lygq$Aygj|VaPF*~t&dkPvq2nHcdY78O`Fc#$afQ88-?A(O<tJhPNzXK3*%_o(xO<q'
    'zWB7Wb>${OG=r+XbD!LwU3G_(hvTykPdAn0^ZQ=oHhS^4ZayE{wYpZRcRe@oeBZbB8+(@Dvu(TU)-7u<Xw>V~O1B>LY|9UVTEq3+'
    'ZoO9bd%=Fg3l8>b^<Xd9+0u1=tCz%Mt(UkSA)<xjNu12I6IlR=XeR<DoB^_NJW64_c-##mm)Z%Cu{#^&Yene<N@32b;tF23<nwSE'
    'M@$>IQv_hz^kusBJ3rZa<i?3nF_~GaZcW2}#7FM9>$}>rX)NDY%(Ah3S24F1uJ5ZFmvx)7`D7Fr%k3Af7bn`1y=Y;iy@nG5Dop^N'
    '&bu4H%Wr^BJ$Dpj@ScSCN=pHc(5|`V$FqE=)A`simZi;oGC<l7dYYHS(<v1-lVCPaBF%8yR;Sc$+nurtf8fdLF!@x$vWlo>^2x$7'
    'OVo-!{a}VYGB52DFoO~?7M7b^AHVaqvCrzP#`aj1*~|irm{Eb>1J-~i3(5}Q_W*vYShA(TKcfoZSiJ`g@wWzD;BTGn)9*g3z;9>k'
    '<c7Bem8P(`fp7FolL*m6GJO2r*}A<x1r$8MntAOZ{n@rU0>~3U^gP7p#Etp^;4}&%!!yekjBtF!|M<B@U51Pr1krpPB<?IQK7Kcw'
    'Thtoppy=+w5LUCZ?X{aQPV@L^XBy0aUhaG}GYYthB{EsNWA3<<Ne}`0p@}2<p*K@d&;jg&@zem&me{`<;&*&xa&GNwu*EfZG%~QP'
    '2Ss)^e`vaJNAm#NZhgGGxIO%M3j{;*0}X-Tg2F_8oGY&CU=Dpfh<VK;p9AuSDJB`RA$!7p^V`snG=pWWVk<4;f&q~EjRz$8Lp$u4'
    'Ouj$Kcj!|KdjQQJn_e8v!e|~qk<Z)6MUensO4yA5A3CjRpSN*~8n2@K70dmO=&x+y+q6$)k<a=5X;M3|jpb5=a%Qi^mGw<RE}m(x'
    'h^ZvI;xX(4C@o)4ZX|sq&ut(=4|WdDy9aETk)j9ND=Re#JH%yK#03^Zj=w?~*^cuHA{%0>o)(Oz!5e_@Dq8>pGIbgV(VJh~9viGJ'
    '?a2+ZX-xxOU|ek0GyjP{1CtQX@nvAX<F;4~@d_;2EDTHJ4>GbAaU!IExdmF@%bP^?UL;lFAx~C#we#hQu=zdu!mu^&(igE!QS2bl'
    'f{5@!?>L18F+qs(5`|}OAqu#3aXdG}VIkj57MbrW=}fIk+1lT3a3qkFnYRh>CGEU102vR=odiq%h#1}R-wm^M#vfbPyxoT9RY6rX'
    'JA!2jMXl!`><?yB-tOf1667FGYQoz%Kxey+J1cA5>$H5161`+dwn4Dm#+x9yKmxrgRv@*b`Vb%{10>CLlyC(kQcBSIX6tU7`@40R'
    'A8J+OjFI{?UYWmZ?`69o-%q+q1sXK30Sk~b&|S%Rh3C>MzNHA3mhifUrMYX_m2?&E*crQK5=XflLYsBj7{|p8HVq@RsJy@!qdGB0'
    ';dI7`8fK~jaa0!v9SfvDUk*1c()ujS6qiC5&_3*Jq9~&1`ono2MFgQpx|ok!vYR%dXCz{%B<1{6IZHk5F;_j3IucqSj25^hMaO<1'
    'IAfgZA3sR3ZMR={{U8&>NhcdHho9(n9C!ma3O(fWbL@H&kAf9O{nrI(i+WQWCfF%r)~=9-DHu?CvVaXG5Ot(hne>W9U^}#u_!*Id'
    '4dp)J@4!vQFaniba7CkYbA>z3*SJGS<+io^ni1+;PMXNh43NL3)Y($qBN^s=MZmx=r4pKId(dIxp$9cW)$=wnE&{VT5Sf+bdsn{G'
    't7^r3cA-GhF0m}9W*25A8O0c=YbOgBA*FR6t-=<Rb@OEwmi1tmT$wG(2Kllolp(EEQ5#tq2*TuW(pDI|OMpgw*TfYmKu`Mw6^sC`'
    'BGtZHt_^^adH>L9(t4AAn2t#3P5jGr973mon67%#(>|Ggqc_{idRP=S_M~Sjd>5c~J51BR{Q`Qi2K^bJi7%Am64apm1;`;dntZSC'
    'Dj7d5%+61xNS=W41K4@tBH$-3@E-Gn>5N<KJGYRpK7bJjmN?ns7CV9e_srBV$KNuRfq5w36f8VYO^u+1sZPd+8ci_z3D}cWFw@JT'
    '`H8VtXI7(TZi2M2GXeyzy5=WFwZXucY=NkIR<`}vofs!<nYRN!Y~u_pGGy`h+U!7kGG3t}C>IduU)gholU9Wy2LBV2-r4NTW?yag'
    '+$dHyI+;mw$N8O2Hsl%SXX5EA=U?sA+<tw}bHsnHY(F=kd7lfha|UAPE)|!^^<b-SY12XACVAHqT`k-@prgRmTB4VQ+eW?G#H&aM'
    'YH8#ZG8A`O{fhKk<sS>A-~(?<72dC`!b|IZOIv^~pV8+5gbUJUVY6X@Hdq04Q4?8kzOaEbM1>*eLwI@2h_eOeBTCjEyLUA1k5z^6'
    'wbOF>L;Il9N(CD-CODaZ($f<cZs#2S><a&MPBKJ}{`7>V)M6o;&Y_X^8#oNWJX+r!k6onji<g8mZq!N!paS&6{uT@PyZ!W3l0_C3'
    'LC4!t$Gfa;v8N{nBrtcOt%M`$1IvErT*q!hSX#aLozoaw+Bt6{!Li|q@f{?lL~|TQpc4?)@t7AiUJE@D*F)QEqZ5Y2Fgx2u8y#IR'
    '?$-88yJHp{PSsyCv%xd*ziOMFqv*^4k&D-W!wgsomz>=J`%-usd7C)fG-&RR$88}wJ1`iz(Go+G*aRCQNGeb}nR5kZ&nuUkins*<'
    'Ng{W0=0&?~t#zG~=Zai<Q#~;qsj4^eFGzUz*$Jb`eCG7^W}n_c;DZFvAN1w})9>`=9n*mU+$2P0u7mTq5R#7m>F0X$oaq-JpjWgx'
    '(_b<sp+}~ttFJf5W2X1q2%g%{71&=L97W)-H`UY6t>3h7QAmT&0<?}^qIevF1lM9PHnguhTiyuhrCpI(*3%rAOgM8KaLGnJu>LA!'
    'HQ>vR$H@TncDz;l#A8>=BKf@_QoPO@q;QiNc4cObJQUX2^B^1rwCZ9&^SzZWvM9mDYKq65NjyPcQ()bV<B`NVHJ#n)MRlaWf*)#X'
    '%gn+SljB!_`i`d{!G*|y0&+_NP{#0;(Z)LT3sP?&XMUsZ&CP@2KTCK3a~N=OoP@gPau_uxaM<b`V4QL;S||GJr1OD2ws}I^WyDs2'
    'B^%)oV!Mom3T`|fZJsnoZ?RL#&uLrDscdDD2DfO5NKkUK(8Lg4Fwshgn+$ZR;0UtYOxoc#x?pap3#BQ>i69>#$|b@I`x$t?ez@2)'
    '(YCvra;Ce9kdydXwTsN0@XPUT#KLGMrOtaH_kcQ<+3IpZL&?99nr`$@tLe%KXkFedbz9NyF2ynwhpOTG!3>Rbg~D)!Ig!KA4t>Xm'
    '?{Z5Zw$JZs7l3h_UptpmO%|AxeKni7i4d{nwzr0hANG1{EI2GlX5Spyl<0tdfm#aZQdiSK*qb?i{45~YQ=YJ>EY!Z<(D9R*+iDW='
    'r)F+||C}W81Uh<=Xb1fy2#Sd3P%B&MRtP4^>L$aoR8q`fQQM$P!A!V%<i?dDV)$eTqx^J)9V6l?R}@dVdR&QT%GihqfJhxkam%L;'
    '20SP}L4VRZQ&d8uKZ{~y0S19nH%Nd(1F#V$ESO9YuZT}}1VJ*dnxYpI3?LW)RVoe5(usk=IpYb~jnPvCPiv8cr){tSvpCFCRugSw'
    'jF*r|Fu>;wVYU<IBMQH1x9-abIWG=+z0eDTXg1YmgCw5!2e67hD4*GL%t*Gw3#cg6t<xRwrI`<OotW$jgE}fe0ILp~olnq|!xz|f'
    'FdZ;&eKfyZQxtkwXv@Mb{Mcz-N(u^VYze%3VKSXL(|Df122TPKLHEi_xGDsM3#M}5wMo;XkKl)i2sKJmoeZB00?b{OdpqcmSzTdv'
    '16T7N3dBm|lU(eyM>azkSZbbe-o4p6;%6{1vem(jVkmzf9~IWdGw@WoU%@zc>1g{INnp@x>8^Z+r5mC@RP>BR_b?+6%A5?j$45kp'
    'CIpW(3$lGW9Y$5AnAy3GoC~YZGd_Sm*ioruXB-QqOuJ_=9qo((!c03-%o9C<#+*^iiHk6k@X!)77i|IvilCtAUExvO>1gSjrU*$!'
    '!E$D(P<#dkjY(d)CRs49h^U$DB8~zX5}1I**YG_b<9FN85)ZB>9gcsPD1e<T9-xz!cmhvJ8gb-Xi^9%&=uu*!G)4Fi4uC@aVW)(b'
    'iWt8(u>g85zm}dw-|RU(ltTd`h9MIQ9=6eK!G=gHE=Fp06R@GvrGOei`dJW7<HSLu82pLU{sm0p`78~iZSW129Ig6RKAeQ+1~yBh'
    'BNQv0qlsjojRcQjN6vOARF`xoL2hFI=)#Bqf^cMP5kH{6wm8}Yr#xdQ7)#8;ixb>10c;`?%YS9RO#hAh<!->v2Du?0r<o6fdTyw^'
    '5Sr%MKo}8s18{s{hm>%e6avSOQzo}Y58P{q_J<TsUObwQBMKNUf>G>&e~^oJhLImE#kmU-b5#;q1xbY41<AY$RV_f-2$i`j>K}NR'
    'tL<uqc6-!&9fLJi8cnF60gUXEld*ZZnvV?TWNhocO*2a+rFfIlav-GS+UZU)<a@7<ckYYFJNN2%=RSYDlV82u+1EXu!(@PJS>+iI'
    'HguRn%g6IP3FUI#(!G%hN+D>csmlzHu$ibJCtigtg$d+0B-N%)A8idS<BD`F$rV@)GE@rKJlRo@lq7~(*dZ0mobPREvxMh`1r7b6'
    '%O%fnFbl0`iD;a9)95Xy+70~F3|pq7`R>S`U?0tra0y<n3tlhn0x-T4u*E}<_JiKsgBBS=dUKX!1p+`uFQYgayCbLPj>FN5+D8vu'
    '&7k#TBAzqfy3>|n+)nF>t0e&1w_ZH)nmOj3)+px4*sVdxQE#Xi|5hQ=8jt*R!3yJuaKtYo^FJmSLx;aTT41-!+eSVlkD(@vG*K&*'
    'UUS^E%qYa^Q=l>yWKeQv8`M1(qsb&f`c%YxY-;U_SQd0j*rb4E1vyxOR61|S4C9b}fX!wW{XJ4%T_lWDgDPr+Cj^JvA4)GCo`{R{'
    '0_9MFt+-G}riYw=5aA~gr2in)XA;LVUOwFYpwwsO9TvTN@tUww<d??`OH2iTFYlom77!n?Xb>thK<FuqzzxEz*~YVlA%lrBi7|zK'
    'Qy$9&DAS^XHRYPEd>FEYVNbcU(!ddr)Ek5qUMmsNMNE+`7U|j+qmNk9nvTFp;^kZfGF432*EZDysZo-lPNMgB+4=G)2EtK|k)sK$'
    '>x=hp5Ejlo+{7IRvmnu%`uF!0rk!&?bo&Nk^4(;}`XRV%uxHSVauadx0RH<doQ%T2*Sas-cfD|8k_(anR*?hSX57UA+OUL!5CdL='
    '(4oVAFPO~qCQeBd(meDg{V;tVg+EZX$W7~f$9S5Q4j_V2VY4G9<iwOs=Mzlqnxbf9=d9~ap$T~`LU2gUl}Yedc4UG=$e)~KYT*$N'
    'w+4$hT3Nqp6};8T{#C25>y3^|uWV36F%r!pVJzTgT%A5{;iul4omqdov*7K{?7!Wa<j)75?lE<0@U|@X<_UP2^CZa5hnX-KRx_~H'
    'GB<K*8edT=4i;bunA<|Yf=%#*hmtZHj&47c6Ns$HhEAo%0%V5YF*kJ{taKhwAKN~4Kb<8mCKY4`RGW0W%+^bZ20nr`Q*++J10asn'
    'D_Y2^OS9FtWHQDO)_3<#af~oq@ifX#>uphAzC%wt1qUM~-y%J)vN(T)Mf1F1^e-YF2*h1>=H^hR9?jOLVCEJucZ;aI*?|)pkbRqB'
    '3zLvKukiL*fsaM#y>)J3p;avOyj72A#rS#CF>3h(@jk!<ZR8%(?|~=`s4$>HG!-r3d=nHNu~(#IUowA?e}gIty?VB25Ue&3Jro=H'
    '!D>BqlOMs#C1CwUJM~-|s2n{k&tjfUh<ODiN#&iQYn0GQX6}r}^MrTgdEkh^f4O8Q0gpv_@OHD>A$L9}s4;1g6t`-!G6c2BDX#@|'
    'A1ob;2I<Ygf~k^e0ITck%>ar}j3|(&o_tRMdU<sfMqcO#ptPNI<AZimk4#rP&golvvv1`KY$&jq{_*nM8HG{cCJym<KnoG+O=R5k'
    'qz4xUPkWRya}y5@3>GXWpr@l5x7l<SOgJ8~Ta^k~T54f4^MiA7%#vEVxFoA~t~fT%oU+zAZ)5bET^TtG8DHD0O<CEd;KW}Etl^pR'
    '=71U<sMERnzYs$6gAqswq(x~~Dk<{(YA+*;H1C1ARoAZSIz^`|&_VvE{>?v2G5mWz=)dTKssKX418u>S>6y3BQD76kCBrHU#CNSa'
    'TP<p^jgWS&kY*GFN<?p<A5){Id5(V~L^uxu84l^s-NYA;l*ml;jgi|8Mr<Nud>A5DQXQkhU~?)6N<9!AC;{|`PIY=yfWYQ`MoV(?'
    '6U7nqO`hojUEn}xm}r4z<dNb|guNV(F^e@$bTGg~Em*q=c%vvO$f}$qxa}w8YI+2DE>8TV{em$YWy1Wq1yW!fAduu7@szQSc()5R'
    ';EQs>F<BY*D9}(8iOdumRWuMYgJp!xk;I|zpu_D0MbP9i^L9~seoyAnbmV$Zd{9nDU38SsrmQIC-Vvm7+onNN3>d{xDl=g;20TuX'
    '|JGDn8VPNOJ_u461a%S&gl9DC%&1BhX-Pzx3I0%SAzWN0|5%;B@9#%F77e&u6g2zP;{e#C$EE|WmIo`-=K<x)O=MQyFZ8jh?`HKb'
    ')ptd`R9DlUa3={J2GcXk(?M3$qav0T4OCG%Z8%U3b3Q-Je*rsn-Q|Z0Hko9RZ(Jb+7K`R47_%0MYEVgWQ_|x`mt{8G@SV(>Lg)>m'
    'o4TS64rTzx`4J9w0p|yzHzofiw_|#V^J5;*@Q_Mp1kR{^hfQ{Jr<hbG;)6Nfg?&E`DMf^3p#Ta4;Ka;M?zuE6CbtL~g$eD}0iBr*'
    '0_}MKb_E(UL3t8`bNd{^Q!iWwKGOh+GVM+9m&dU`AI+zD^GI{G=Om8$WgH2XVC3&?X~QAAWOp$;i`iq$j$*!c)|Jw8NW>YU>8t_)'
    'L$vTQ5I`Ms5$Ab~v*Vx`qsdf|i&Ex^g%)5JXc@vXw5b=g4M3HYEwfY#Hzy1b+>U2<az36Y6X%&|*dcmU1{l7t<X$awKgxS0@dnO_'
    'g2H(OlPQ@&^;)f32h_w_JtoT|>vcgQX9ubMw$u+DI#DH5`-rGmFJ!PTOfBDJl0i-oQqEjnA`$t0IZfT2ZetI5H(njlAf}WgK%-`I'
    'PmImFQ?m*9r6Ys+)`i(czA~;}@rn+f@tV6w>EoO6g4Q{B!{Z{{SY;DaavyYUw(bIU7O<~Dn&1be4E`5Mej@d+QLM>j`Q5>~EkyDo'
    'JPp$nKY022C;5-L9_~^sVVQGtTS<$<@y~;F>@0tbgVLqZiuqzZ)x}Q%sbWLF(V6}Y{{O6JhRe7O)twFD1uT}^#DTFh)gBNdAd0Lk'
    '59YOpcy*azm16a{*(QFBRhnfiXzegZCR4`Q9wuKFghD<+FwS;n{-W17&ZX2<voyN6m`0c8|3UeUzG>=MoWbEW8-)Ev{o>nt1FZX>'
    'KMsDbxBC2xR-dUAY~BMCTV}M*tUHi=V;9`8iO9Q)!GjaVTys&(nv2om8xHYEf&XdjPbrGLub6W)VLS=IWHEUNdJ`QDks2thL(B-j'
    'XL%bFlLGN|9FI}yG|!kmh{th1h=O=N%{2q`^t}1mJjy$o(gwvyYaC&o;5pMl3C;l(F_0rgE4IYL#?|V#y9SmGN9b`P1M5QifNv_K'
    'P$qvIFP`HBFuw#3?Sa8iMwvi$cj*YJjmJ34oK%&<d{wUI&lz>$*@}e%|CqFv6Gx*Lz4^xqWiLgRC9L@w5E6bKfo$+|1T%u402XBu'
    'psS4i70)u$^v+EGH-)a!{c!4`W{=#o@NEsl^x1RlpsnmXnP_gJj0XfFpEUVYc0;WDvp{PJfpY`)MG;1Mp@EoLAZCVv0}3~!Tmu4m'
    'H3zhiA^KCs1;DJ1{lHkRUp!i}t27O&Ex`)T`Ht6FZ*!96r_B<|GhBth3#Td29|-kiHf8@(1wD!T2TOH5<>z`Y8*fCli`|G$vh<#%'
    'OzoK@@eo4*3l*eMM}NPO*4LCBH5-J9uZiuT3BqdQIX`YcXs`c`foZ(|ji(-ycuHoTh8Nj1Ap1_?7!le$ZoD4%NO$8FoebMvrv>AQ'
    'J5b^p+-|+~N&<W()nISq6*XD9nvbQ5(^C~MoW1ZmQI*v0lQ4g6Re}dOAr@ozX|*Lfk!fnLGU_qGL=(&(!?V9h`-y(@1L5^IvW<Zd'
    ')N(vebJt+DyF{ovonjjc8LVA9;=;@qd(-u_Rsix^#$Q+sllwtuitwo_E!Vc~T4_PYnxYIauxdEoa^;Rd;p`2=vwTiRW8NT?p;Qn$'
    'Gzm2a;Ak^v=$8GG445wSDNtR}8gct&^KIE&gnwbIrF1yub2g4)Z~JBm@Y>RZ3|u$kMP{7Prd_;5j5WAACx%T|Ur=VrQY$M>+tf-v'
    'QH}HRiBa2Ub|tUwC<a1%#2L>)rp!T}jX=>Lruq};Ul$}Xg*%!wZ9TW|WUv&lFBGeoX*Vwd<tcp*jN%`9Q=ykC0aEpOz?nODl3*kQ'
    'q{0;7Fw0$>J5=r();9c@x{8webkB}*4U%|77vt702fdm(Dfn-@-1PQ8W9^Ppc9Dq{ZYJ&h<(o-pEdKbh>0VMRyOy+2w~~hH1ntL<'
    '|HGvuU?JeInpMy44ZX5{j+Vu1Lk<I#EEpoSYIBY$ShX#21?W{?0b08gDjEYt78qm8B@eds`az{)HyV3(rBSKY>Q$?@zrS0zz}dE{'
    '2lm0i!QO#oRVxQz>f82yt-9aXxA&|n{Mp?*XjoO4$^OB9z1jc(OW&}9dUel6f6}T$XZ5OG-`}s=yR}NKve&5ZRSphd^m?OeH=wm%'
    'wrzWFuY#3U!>%1vYBuob{@#IYTlGf8YV234_8veZtR)2HxKd$b%VJ~OX5$L{R^ZpNInEU$@NEJR6&=>5Cj_^|8v$cu<QOnz;smdA'
    'Qj<yv0L##zgpEiQofoeh33&5;rEoPh6&r0zDLzMu{nRO4phl2s+)wMNa({Zq9K5hL7(fQ9rN7u@OMBz;(*Zp<7+zgpyD|0l<)Xbe'
    'E)<Exh`)82Xz%~wovJRLk+xNikRj86%Cf-RgmB6Z)Rwm~c@hL#m9{s@wpz8uEW1I+`>BGKUzv#)Z)$T^+Z7jgL4o}3EYnn5YtUMG'
    'fJLn>@R-ZvnVdx+^zeB>f1guUJ!%hNB<K>b-o*(Q?#UBt<x=Ai8f5H0xO}uaXjq;`et_uE=a0zG%H_6$brE=AYxTh73^4f}Ov@k`'
    'y@1iVaJ!>Ge6|9-I12vZx0Vu2hxcM}bO5M;x#ec@1qyxAO+R618qa0R{Evgy4|v+9Cm?PEk6{Pkt@8BP>W4VCngIDn+@MN4Gq+h;'
    'JXi3Uay8`_9MYE0X-h_+Os3PCyLQI0KAzYTf^?*BtR{dmBfVNGGeXH~{R@YK510u0oF2$M7ZN~QiwPS}3VFZSt;lMW=H@HTb1^9-'
    '!VD*-w6Kx7%EZi=XaF3;a;5UxhC9JMh?I~8&-nfWbL5b(Mhw4WBKU8D3<x%eUAimemP*vP9J+-It=L)AndzdZ=jhK25Mm=H0CI=v'
    'ly50gJM;8Yshv}kf;}mCVO?utU90NY17GT*Y_DUctNagMDGv8W_P7v$ziIar$p%I*lVdCopvvgPYvW)xh<)&)!V#W`ldy8N=>U8y'
    'E$)K9IH%KF;QujjeEX{4?d8?~Imq~_NNwBZ7||c{>?;vd6SF%}QmY)Gm19MEHQqi_TscKVUJ*^i_baBRx$)d5(+zKAcFxyRJ6n^a'
    '_^Acxz4)yKEXZeO&c)eGAqR6_IEfL*Fp3Z8>?KK$Ug+3G%x2|;;!k4bU09IS$T!Ohu8j8UN|b-)V@MN<@Kd`^7BbI*>njm+QVZQ~'
    'E_(jUxOp0GNhKxaCawo##{o=aLBUsoc!R^npa;Q*DA*C>VC5r4WAxZkQ^L+n2`n!}Rl8v_8}J5QHo;Nf%OkFXR^ayoZs14D)+#CX'
    'xe_$Rp0ijhvYd#n(f~h&)uP}&7vMxZ6^9dG1VSNRtQA4sl#00+tKKA}m<&6DHy9KHPJ#E+EM|MlyU^-DnXX9x>SA<u9r{8I;|N0('
    'x~JdOh*!>sT)+Rkc4Hb9J9wUyM1yM9p_8?|H%UG%II}KAa8bGA9Pl?k6sm3qRkV}4yrwsmyk-Iba|c8+dUZ89eS`0-qMN^tyuJ}='
    'EQA@;M->3<&cl&UjxMO}FmjU@P9OCU-||4;vZeBMiWS*+3P3WB$Ud0`c@Vn*l71wFAW&jZ=ULLR1kLh{z+Y@s_o|hKRjF3@>J}L9'
    '_1azoJheLbQT6J6E$4F3CH=IE{29TrlQR?wCphR@;O7DxC=BQh059GMP#v1BB;nbGo2=M%IVM(R1t2Mdq)^7H@>>}cDdFp}$E-1i'
    '_!D=8x8>Hs)at+(U?jpAtD%bA?!s(|SvUih`FkJrBu5tWwJC($)_?V#P9Wj`^%I>sZBc#dQAW0Y5nEQJg*QQiKzjx;PZ9{@t0GIg'
    'ET^nZz%D5F;(1a&)a3N1EduNT!JshxkcF(>5fkgV9vvNg{0>_JL>xSlRh0YeA=A;+?u(Q<x$SPRPpP>Y3Miu%gQcsS?f|9+?=ZD{'
    ')9iG?R`S-0*zHNebYK^~>0<8QybD5&OiG6eiJf3$Q;-e#!pT;a%9yS&aW=tZ43%cOOBzDg$VDInLi)UbI}RL&bKL<8IgA`f&(Z-M'
    'kYn9>-*JTAcmc7W^cNVLrVZ8BNrJ#ywsmr2DBKx$hg?dQ7FY!aehPKRpN}Va3QIA1fB@?`PG-(i@G|8j5T*fYkr~D!4B#&YOktYa'
    '`hP{bxg(o_F~sp3tA>so0tRN>+riFtang{X2b)`B)|~7-!!iX<_hlALjcyn17)sKR_S_Db3BIfaUD)kzX_&D!GxXcfxLXcC-r^Qg'
    'Tj}%h>8H=P&d1}6+w05IBeAuvzFi+XCzs!@okOwBPVb<hgI~hDzJ%(-n;S$?_IvUTnw&z_>BY_IM@N1y)44vp_<fI>A3xyx$LrJE'
    '(~mIZ#pU%m{Cxa;c>dw|dbPJt#~0sDFOC7h)34uP)T6uO>ziZe_Wn}r_M6+o>l^A;_H%jh<-2ooc=`pAUg_+^AvC?Z1mx~d;py`J'
    'f^^mS<<Yk<-)@}y>&uHz&duqk3z+SfBj>~A?PqvBI=)%$2#3G_eE9{W&E@s=@yFZaBj@n?<BfB9efsJ20?@dD`NJ&hPR(gJ_s567'
    'S1OgYUanzA=cf<QI3@Vi<(KcDKw#mFpySi4>q{ik`7!qA+#CZrkDRmP+YF_`89wf;^}QxPi~wv&=k_fzK0Gr0`0D2L%jJd6+;*yg'
    'VRwJ}c6faR>O@>IR@xY>R~^>q;^y}FR5V#V5QV1ahYv@`pQtu>7TQUtJ=wt>Nj(F*GWiMN9dLr|S{;ja2Eoz~L4?f=Gb7foh5g4%'
    ';EV5yCjSc$&Yy_'
)
b=zlib.decompress(base64.b85decode(DATA))
assert len(b)==23025
assert hashlib.sha256(b).hexdigest()=='2dc3927bbb593a1ca0a56f3054694e3ed85c767152a597be431e8b8198e798e7'
p=Path('wall_roof.py');p.write_bytes(b)
assert sys.argv[1:] in (['build'],['check'],['extract'])
if sys.argv[1]=='extract':print('UNEQUAL_WALL_SOURCE_EXTRACTION_PASS')
else:
 subprocess.run([sys.executable,'-S',str(p),*sys.argv[1:]],check=True)
 r=Path('wall_roof.json').read_bytes()
 assert len(r)==2463311
 assert hashlib.sha256(r).hexdigest()=='cb0f1b0ba0394aa0b9251fb4e0d0c79b9c967017863ce73e1250125bad514de6'
```

## 11. Remaining continuous problem

The useful remaining pure-four-A two-apex class is narrower: unequal heights, neither apex on its own-COM-height wall, at least two nonbasal weak points, and a unique positive-beta packet competing with negative-beta packets. Any surviving full nonnegative intrinsic stress must obey the strict resultant orientation(12)-(14) and the actual-moment convex relation(16).

There can be at most two free internal base vertices. If there are two, they must belong to different apices and have parallel neighbor chords. The actual full vertex/facet stress equations, with polygon reactions, must still hold. These are necessary overcovers after the new sufficient tests, not claims that every listed combination is physically realizable with an obstructing stress. The second-jet test(17) may close additional members but was not shown universally positive.

The main failed strengthening was to expect the whole base-fixed actual-COM modulus always to open a wall packet. The exact fold(27) disproves it, while the variance cross term(7) supplies the missing motion and closes the wall nonetheless. The remaining consequential step is to combine the same endogenous moment family with weak-endpoint or ridge-plane motions in the unique-adverse complement, rather than repeat a normal-only or one-stress test. Full unequal-height regularization, non-B8 lattices and mixed/VF configurations are not declared solved.
