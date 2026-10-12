# minimum-0241

AI research report · 2026-09-25 UTC · [Export notes](../../catalog/coverage.md#text-records)

---

# TRANSVERSE_TRIANGULAR_SPOKE_FORESTS_AND_ACTUAL_OPPOSITE_DELTA_CONTROL_V1

Slot-5, Bright Harbor 33. Branch `[internal-source-reference]`.

## 1. Results

**The opposite-sign radial obstruction is genuinely realizable, but it need not survive a transverse plane motion.** A new exact algebraic, uniformly filled parallel heptagon–triangle body has two consecutive target-partner spoke EFs with

    gamma_pair=(441/521, 441/841),
    Delta=(1040/76587, -16400/194481).

Thus every simultaneous top-fixed radial germ for their four physical exits fails the supplied sign-forest criterion. Nevertheless an explicitly prescribed nonradial motion of the two bearing triangles, completed at the actual uniform centroid, opens all four at first order. A rational interval certificate proves the entire same-lattice escape for 0<t<=2^-36. The original and final strict classes are both (S,U,H)=(5,5,8). This is NOT an S1U1 control.

The accompanying analytic theorem does not depend on this example. **A triangular bearing facet has two genuine transverse coordinates which can open a spoke EF and any permitted basal partner while its target pole is fixed, or has an arbitrary already prescribed compatible velocity.** At a target-side VE the two physical responses are an invertible two-by-two block, irrespective of gamma_pair, Delta, or resonance. Source-side VEs and basal VFs also have unconditional compatible positive directions. The VF construction retains an actual complementary pair, including right corners.

This yields a complete-packet theorem for triangular-source forests, with an extension allowing unpaired quadrilateral sources. With two unused lateral triangles for actual-COM correction, every paired exit opens at order one and the complete top-carried packet at order two. In particular, **two consecutive spoke EFs whose bearing facets are triangles and whose terminal target is a quad always regularize together with their possible basal partners and the entire top-carried packet**. No radial sign hypothesis is needed. This theorem also holds when the two end facets are nonparallel, provided they are disjoint true facets containing all ten vertices.

A separate exact edge-direction argument reduces the protected footprint: a basal weak row does not require freezing its other endpoint. This releases triangle correctors that were occupied only through an outgoing edge's target. Combined with the transverse theorem, arbitrary remaining protected groups in the initially parallel class can be retained with selected orders at most twenty. The supplied radial sign theorem likewise remains valid with this smaller footprint and its existing order-thirty bound.

No weak-S1U1-specific universal sign theorem or full-shape obstruction is asserted. Any actual weak S1U1 input satisfying one of the successful geometric hypotheses regularizes to proper110. The accepted project interval remains 34<=C_min<=622.

## 2. Inputs and authority

The complete current journal and all three supplied analytic materials were read through EOF; their mounted bytes match the manifests:

    research-journal: 354694 bytes
    678a5d3351e0ee45a9c7b0bc602f4205739a0711b2d8d6ec00a692627a9517d3
    NONPARALLEL_TWO_TRIANGLE_ACTUATOR_AND_PAIRED_BLIND_ESCAPE_V1: 12716 bytes
    2c914bd63d8483930ed596e79f628c464417de6ca62b250afe09cfb822544b39
    SPOKE_EF_BASAL_PARTNER_EXACT_RADIAL_ESCAPE_V1: 15016 bytes
    ce9f3503f2111b0c739ba2a18d21337bcb02390c81dbbca5dc19062b83c0fc70
    PAIRED_SPOKE_SIGN_FOREST_GERM_CRITERION_V1: 15831 bytes
    748766944a6e4c4b2eeed157155e2251cd48c8d0363dffbc2568bd845cc5ec2d

The literal parent is `minimum-0239`, SHA256 `02d2c6a3a9b0e54366f01c86b298d2055aea3037c342d8389b23e4b4dd465a38`. Its prescribed-pole realization, actual-centroid equations, partial non-spoke opening and physical selectors are retained. No new conflict with its literal payload was found.

The supplied sign-forest theorem is used as an already proved exact radial criterion, not independently re-derived. Its unresolved opposite-Delta possibility is the one realized below. Its two-unused-triangle condition remains a sufficient realization mechanism, not an automatic property of every packet.

## 3. Geometric setting and physical obligations

Let P be uniformly filled, full-dimensional and at its actual volume centroid 0. Use one SPD metric M and its inverse N=M^-1. A constant physical linear normalization makes M=N=I for the following derivation. It also transforms the actual uniform centroid correctly.

Let F and T be disjoint true facets of sizes seven and three containing all ten vertices. Parallelism is not needed until the auxiliary complete-packet extension in Section 7. Seven F-boundary edges and three T-boundary edges leave seven spokes. Every F vertex needs a spoke, so it has exactly one and is simple. Consequently the seven lateral facets form a cycle: four triangles and three quads. Each quad is the unique lateral neighbor of a T edge. A triangle has exactly one top apex.

Write q_F and q for the normalized poles of F and T. A physical spoke EF r->s lies in the relative interior of a true spoke [a,b], a in T, b in F. Put

    rho=r.r,
    p=r/rho=(1-theta)b+theta a,    0<theta<1,
    d=s-r,
    lambda=rho(1-theta)>0,       mu=rho theta>0.

Then

    r=lambda b+mu a,
    d.a=d.b=d.r=0,
    |s|^2-|r|^2=|d|^2>0.                              (3.1)

The points a,b are linearly independent: otherwise their supporting edge line would pass through the interior origin. The directed graph D of these EF arrows is acyclic and has outdegree at most one, since a facet has one perpendicular foot.

At b, the spoke derivative is strictly negative. If b is weak, its only possible partner is a VE along F cap R, a VE along F cap S, or a VF borne by F. The classification follows from this strict spoke derivative and the three actual incident facets F,R,S; it does not require parallel ends.

The physical functions to open are

    P_ij=x_i.M(x_j-x_i),       Q_rs=r.N(s-r).

At a VF, an acceptable pair is (P_1,Q_2)>0 or (P_2,Q_1)>0, with the cross-edge pairing of the supplied true flag identities. No demand is made that every harmless algebraic zero disappear.

## 4. Transverse triangular-source lemma

Suppose the bearing facet R is a triangle. Its plane may rotate in the two-dimensional space a.w=0 while fixing its top apex a. Let its target pole s have any already prescribed compatible velocity v, fixing the incident top vertices. Keep q_F fixed.

Define

    b_perp=b-(a.b/|a|^2)a,
    w(X,Y)=X b_perp/|b_perp|^2 + Y d/|d|^2.             (4.1)

This is a genuine two-coordinate plane velocity, with

    a.w=0,       b.w=X,       d.w=Y.

The denominators are strictly positive. Equation (3.1) gives the EF response

    Q_rs'=Y-lambda X+r.v.                              (4.2)

Let b_v be the unique solution of

    q_F.b_v=0,       r.b_v=0,       s.b_v=-b.v.           (4.3)

The coefficient matrix is nonsingular because b is a true simple vertex. The actual basal vertex derivative is obtained from (4.3) by replacing its middle right-hand side by -X.

### 4.1 Target-side basal VE: full response rank two

Suppose b=beta s+psi q_F, beta,psi>0, and let e be its true outgoing basal edge in S. Thus q_F.e=s.e=b.e=0 and r.e<0. Define

    c_T=-|e|^2/(r.e)>0,
    p_v=b_v.e-beta v.e.

Differentiating the actual primal row gives

    P'=c_T X+p_v.                                     (4.4)

To check that no neighboring-vertex motion was omitted, use

    P'=b'.e+b.e',
    b.e'=-beta v.e.

The second identity follows from the two actual moving incidences on the S edge. It holds regardless of how the other endpoint of e moves, including movement induced by centroid-corrector planes. The X-dependent part of b' is -X e/(r.e), proving (4.4).

Choose

    X=(1-p_v)/c_T,
    Y=1+lambda X-r.v.                                 (4.5)

Then P'=Q_rs'=1. More generally either output can be prescribed arbitrarily. In particular v=0 is allowed: the target pole may stay exactly fixed. This is impossible for a positive-gamma target pair in the old radial family, but is possible for the full triangular-source plane.

### 4.2 Source-side basal VE: a positive direction even at rank collapse

Suppose b=beta r+psi q_F, beta,psi>0. True incidence gives

    d=-c e,       c>0,

where e is the source facet's outgoing basal edge. Indeed q_F.d=0 follows by dotting the normal-cone representation with d; together with r.d=0 and the strict adjacent support slack this proves the displayed direction and sign.

The actual differentiated incidences give

    P'=(-X+beta Y+b.v)/c,
    Q_rs'=Y-lambda X+r.v.                              (4.6)

Take Y=0 and X=-K with

    K>max(0,-b.v,-r.v/lambda).

Both physical exits are strictly positive. No false full-rank claim is required when the two rows happen to be positively dependent.

### 4.3 Basal F-VF: a specified complementary pair

Here b=q_F/|q_F|^2. Choose the primal edge e in S. With c_T as above,

    P_S'=c_T X+b_v.e,
    Q_(F,R)'=q_F.w=|q_F|^2 X.                          (4.7)

Choose X>0 large enough that the first expression is positive, and then choose Y so (4.2)>0. The pair is exactly P_S with Q_(F,R), the complementary edge of the F corner. Both actual scalar functions have positive first derivatives. This includes right corners without compressing a higher-order VF test.

### 4.4 No basal weak partner

Take X=0 and Y=1-r.v. This gives Q_rs'=1, with no additional local obligation.

### Conclusion of the lemma

A triangular EF source can handle its EF and every possible basal partner for any already assigned compatible target velocity. The construction uses actual plane incidence and a fixed common metric, not freely specified contact tensors. It provides a positive first jet which will be integrated with the actual centroid in Section 5.

## 5. Complete-packet transverse forest theorem

### Statement

Assume the complete physical weak packet consists of the T-carried packet, the interior-spoke EFs in D, and any weak basal endpoints of those EFs. Suppose:

1. Every EF with a basal weak partner has a triangular bearing facet.
2. A quadrilateral EF source has no basal weak partner and has B_i nonzero, where

       A_i=|r_i|^2-q.r_i>0,
       B_i=A_i+q.(r_j-r_i),        i->j in D.

3. Two distinct lateral triangles are outside all source and target poles of D.

Then the entire packet has analytic same-lattice actual-COM regularization, retaining every original strict label. The physical metric and its inverse can be fixed throughout. All selected EF/partner exits have positive first order; the entire T-carried packet opens at order two.

In the especially relevant all-triangular-source case, condition 2 is empty. These statements hold for nonparallel F,T as well as parallel ones.

### 5.1 Reverse-forest assignment

Assign zero velocity to every D node with no outgoing arrow. Process each source after its unique target.

For a triangular source use Section 4, with v equal to the already assigned target velocity. For an unpaired quad use its genuine top-edge-preserving velocity

    w_i=k_i(r_i-q).

Its exact first response is

    Q_ij'=-B_i k_i+r_i.v_j.

Therefore take k_i=(r_i.v_j-1)/B_i. This opens its EF at first order. Both incident top vertices remain fixed. No sign restriction on B_i is needed, but B_i=0 is excluded from this particular quad-source extension.

There is no simultaneous implicit cycle. Incoming sources adapt to the same already assigned target velocity. In particular the two functions at a target-side pair do not force a sign on that target's scalar radial displacement.

### 5.2 Actual uniform-centroid completion

Use the two unused triangular facets as correctors. For a triangle G=[a,b,c] on a true F edge, let

    T_G=mean_G xx^T,
    theta=q_F.a,
    c_G=(theta+3)/4.

At actual centroid zero,

    D_rg= -Area(G)/(Vol(P)|r|) T_G,
    T_G^-1 a=12/(theta-1) [q_F-c_G r].                  (5.1)

The original uniform volume gives -3<theta<1 because P is not a pyramid over F. The two allowed fixed-apex image planes are distinct; the supplied nonparallel theorem proves this using the true F-edge directions and convexity of the same-origin polar. Thus their four genuine pole coordinates have rank-three actual-centroid derivative.

Prescribe r_i(t)=r_i+t w_i at each source and keep the other D poles fixed. Correct the actual centroid with any fixed nonsingular three-column choice from the two correctors. Every basal vertex is reconstructed as the intersection of F and its two lateral planes. Each triangular pole continues to contain its fixed top apex; every quad source continues to contain its fixed top edge. Hence the construction has the true lattice and actual uniform centroid, not a formal first-order realization.

The correctors cannot change an EF endpoint pole or its basal source vertex. They may move the other endpoint of a partnered basal edge; the exact incidence cancellations in Section 4 already include that movement. All selected first derivatives therefore remain positive after completion.

### 5.3 Complete top packet and strict guards

All top vertices stay fixed. A quad is either fixed or has the form q+(1+t k_i)(r_i-q), so every T-source dual row is unchanged or multiplied by 1+t k_i>0. Correcting triangles do not share an edge with T. Consequently the entire T-carried packet remains exactly neutral during the first stage.

Open the top polygon at eta=t^2 using its intrinsic radial-cubic-plus-translation flow

    a_i -> a_i+eta(K R_i y_i+b_0),
    y_i=a_i-p_T, R_i=y_i.M y_i,
    p_T=Nq/(q.Nq).

Take b_0=0 without a bearing EF/VF, an inward translation at a bearing EF, or an outgoing true edge at a bearing VF. A sufficiently large fixed K opens all carried VEs while retaining the required bearing-facet exit or complementary VF pair. This is the supplied carrier construction.

A joint analytic extension is explicit. For each quad impose its two current moving top incidences and one fixed independent linear normalization on its pole. For each lateral triangle impose its one current moving top incidence and two independent normalizations. Reconstruct the basal intersections, then use the fully movable simple F plane to correct the actual centroid. Its surface-second-moment derivative is invertible. At eta=0 this extension is the first-stage body, and all changes are O(t^2). They cannot spoil any positive order-one EF/partner exit.

All originally nonzero primitives persist in a sufficiently small neighborhood. Every original weak vertex and facet now has a positive physical exit. The exact selector theorem retains all original strict S,U,H labels and removes every physical weak point.

### Concrete unconditional two-pair class

If D is a two-edge path R0->R1->S with R0,R1 triangular and S quadrilateral, two of the four lateral triangles are automatically unused. Thus arbitrary permitted basal partners on both spokes, with the entire T-carried packet, always regularize. Opposite nonzero Delta signs, simultaneous resonances, and a fixed terminal target cause no exception. Two disjoint triangular-source arrows with quad targets are covered too.

This is a complete-packet geometric theorem, not a statement that a failed radial pattern is unrealizable. The actual example in Section 8 shows that the failed pattern can occur.

## 6. A smaller exact protected footprint

The older footprint froze both endpoints of a protected primal row. That is unnecessarily strong at a simple basal source.

### Edge-ray protection lemma

Hold the three incident facet planes of a simple vertex b fixed. Then b and each of its true incident edge lines remain fixed. The other endpoint b' of an edge may move, but locally

    b'_new-b = ell (b'_old-b),       ell>0.

For any fixed physical metric during this operation,

    P_(b,b')^new = ell P_(b,b')^old.                     (6.1)

Thus a zero, or an already positive small exit, is exactly protected without fixing b'. The claim is about the true edge line and its positive length, not a generic tangent cancellation.

### Source-local footprint H_src

Omit the spoke-EF groups and the basal partners to be explicitly opened. For every remaining original weak group use the following lateral-pole footprint:

- A zero P row with a basal source contributes only the two lateral poles at that source, not the other pole at its basal target.
- A zero P row from a top vertex to a basal vertex contributes the two lateral poles at the basal target. A within-T P row contributes none.
- A zero Q row whose source is not T contributes its lateral source/target poles; the end poles are held fixed separately. T-source rows contribute none because their neighbors are quads and are fixed or radially rescaled.

At every remaining VF retain the requirements for both its primal and polar groups; using all its original zero rows is safe. Do not replace the VF by one unrelated scalar row.

Holding H_src fixed, the end planes fixed and the top vertices fixed preserves every selected remaining P or Q row exactly or by a positive factor. This holds on an auxiliary slightly perturbed input, not only at the original zero. In particular, a corrector triangle occupied solely as the other pole at an outgoing basal edge's target is now available.

The supplied radial sign-forest and actual-COM theorem remain valid with H_src in place of the larger reduced footprint: their proof needs exactly this positive-factor protection. Thus a successful radial sign assignment with two correctors outside H_src and D still gives the prior order-thirty arbitrary-protected-packet conclusion. This is a geometric improvement of the realization condition, not another solution of the scalar sign problem.

## 7. Arbitrary remaining groups: order-twenty transverse gluing

Now assume the original ends are parallel, so the literal parent's auxiliary non-spoke opening is available. Keep the forest conditions of Section 5, except that the complete packet may have arbitrary additional weak groups. Require every moving EF source to lie outside H_src, and require two corrector triangles outside H_src and every D endpoint. A terminal D target MAY belong to H_src; it is held fixed and the transverse triangular predecessor still opens its pair.

Use the parent's actual-COM auxiliary family R(epsilon) to open all original non-spoke groups while temporarily ignoring the spoke-EF rows. It supplies positive selected orders at most ten, including both members of each chosen VF pair. Its role is a partial sign-opening family, not a claim of complete regularization by itself.

Put epsilon=t^2. On R(epsilon), keep its current end planes and top vertices fixed and apply the assigned plane velocities. A triangular velocity can be extended to the current top apex analytically by projecting its fixed initial vector into a_i(epsilon)-perp; at epsilon=0 it is unchanged. A quad velocity is extended as k_i(r_i(epsilon)-q(epsilon)). Complete the actual centroid with the chosen two triangles; the nonparallel actuator applies even if R(epsilon) has lost end parallelism.

Every explicitly treated EF/partner row has

    positive_constant*t + O(t^2)+O(epsilon),

and hence remains positive after epsilon=t^2. Every other selected auxiliary exit is protected exactly or by a positive factor by Section 6. Its positive order is at most twenty. Both actual members of every retained VF pair survive. The metric of R(epsilon) is held fixed during the plane-motion stage and N is its actual inverse; a final analytic linear factor can absorb its metric variation if a fixed-physical-metric presentation is desired.

This proves genuine full-packet escape under the stated geometric hypotheses. It removes fixed-target radial conflicts and some occupied-corrector footprints. It does not claim that every occupied plane can be released. EF sources inside H_src, fewer than two usable correctors, and paired quadrilateral sources remain separate mechanisms.

## 8. Exact actual opposite-Delta control

### 8.1 Identity, incidence, and the isolated actual-centroid point

The new object is `ACTUAL_OPPOSITE_DELTA_TRIANGLE_CHAIN_TRANSVERSE_ESCAPE_V1`. It is an algebraic uniform polytope, not the nearby rational seed and not any previous reflection control.

Set R=21/20, M=N=I, F:z=1, T:z=-1. Use the following true oriented maximal facet cycles:

    F0=(0,1,2,3,4,5,6), F1=(9,8,7),
    F2=(7,1,0), F3=(7,2,1), F4=(7,8,3,2),
    F5=(8,4,3), F6=(8,9,5,4),
    F7=(9,6,5), F8=(9,7,0,6).

The important fixed vertices and poles are

    a=x7=(R,-1,-1), b0=x1=(R,0,1), b1=x2=(R,1,1),
    r2=(5R,-2,1)/(5R^2+1),
    r3=(1/R,0,0),
    r4=(1/R,1/R^2,-1/R^2).

The complete rational reference-plane generator is `initial()` in the source. Its exact nine inputs, in order (m,cx,cy,d,ax,u,v,w,t), are

    (225082171,-82658883,-186396676,144995592,245518313,
     21525122,27871567,70099732,28332266)/10^8.

Only the two triangular planes F5,F7 are adjusted to obtain the actual body. Write their three free coordinates as U=(U0,U1,U2), with

    c7=(r7_seed)_y,
    r5=(U0,U1,x8_x U0+x8_y U1-1),
    r7=(U2,c7,x9_x U2+x9_y c7-1).

All other poles and all top vertices are held at the generator's exact rational values. Every basal point is its three true plane intersection. Define g(U,0) by the actual oriented fan-volume centroid.

The exact body is the UNIQUE solution g(U,0)=0 in the rational isolating cube of radius 10^-24 around

    (-417819504419730630621198890185,
       406482606157541070247829267790,
     -1253550426273930071347650412813)/10^30.              (8.1)

The source proves existence and uniqueness, not merely a small centroid residual. After clearing its nonzero local denominators, these are three rational polynomial equations with a nonsingular isolated solution. Thus (8.1) and the generator are an exact algebraic representation. The decimal seed itself is never substituted for the true uniform centroid.

### 8.2 Four actual physical contacts and strict census

The exact local identities are

    r2/|r2|^2=(3/5)b0+(2/5)a,
    r3/|r3|^2=(b1+a)/2,
    b0=R^2 r3+q_F,
    b1=R^2 r4+2q_F.                                    (8.2)

They exhibit physical EFs on spokes 1--7 and 2--7, and target-side VEs 1->2 and 2->3. All coefficients placing the feet and normal-cone points are strictly positive.

There are exactly four zero primitives:

    P12, P23, Q23, Q34.

Every other one of the 68 true-edge primitives is nonzero. The actual strict census is

    S={0,1,4,7,8},
    U={3,6,7,8,9},
    H={0-1,0-7,3-8,5-6,6-9,7-8,7-9,8-9}.

Thus strict(S,U,H)=(5,5,8), with two physical VE and two physical EF points, and no VF. In this particular control T is strictly stable; its weak carried packet is empty. The analytic theorem, separately, allows an arbitrary T-carried weak packet.

### 8.3 A real all-orders radial conflict

The two arrows are 2->3->4. Their target-partner coefficients are exactly

    gamma_23=441/521,       Delta_23=1040/76587>0,
    gamma_34=441/841,       Delta_34=-16400/194481<0.

The first pair requires f2,f3 to have positive eventual sign, while the second requires f3,f4 to have negative eventual sign. The supplied exact sign theorem therefore excludes every simultaneous sufficiently small analytic radial escape germ for these physical exits, including arbitrary higher orders. This is a realized uniform-COM obstruction to that radial class, not a formal coefficient counterexample. It is not a full-shape obstruction.

There is also a separate exact fixed-body metric limitation. For M=diag(G,lambda) with G>0 and lambda>0, using its SAME inverse,

    P12=R G12,
    Q34=-G12/(R^3 det G),
    P12 Q34=-G12^2/(R^2 det G)<=0.                      (8.3)

Thus these two forced local exits cannot both be positive under a block-diagonal metric alone. Within an old-guard-preserving neighborhood this prevents that metric-only regularization. No claim is made about arbitrary full SPD metrics, large changes of the other guards, or another shape family.

### 8.4 A genuine first-order escape with a certified continuous interval

Keep r4 and all other noncorrecting planes fixed. Prescribe

    r2(t)=r2+t w2,       r3(t)=r3+t w3,

    w2=(340818629427/228281881000,
         12965085077549/4565637620000,
        -2903946929791/2282818810000),

    w3=(80000/370881,
         10988501/14128800,
        -441/800).

Both velocities annihilate the fixed apex a. In particular w3 has a nonzero y component, whereas r3-q_T has zero y component: this is a genuinely transverse triangular-plane movement, not a radial reparameterization.

Use F5,F7 for the actual-centroid correction, with the same three coordinates U. For every t in [0,2^-36], the exact centroid equation g(U,t)=0 has a unique solution in the cube of radius 10^-6 about (8.1). It extends the initial root analytically. Both end planes, the top triangle, and M=N=I remain fixed along this actual uniformly refilled curve.

The construction makes Q23'(0)=Q34'(0)=P12'(0)=1. For P23 use the fixed target-edge direction e=(-1,R,0):

    P23(t)=ell(t) f(t),
    f(t)=x2(t).e,       f(0)=0,       f'(0)=1,
    ell(t)=x2_x(t)-x3_x(t)>0.

These three rows and the factor f are independent of the centroid-corrector coordinates. The exact interval calculation proves their derivatives strictly positive on [0,2^-36] and ell positive on the entire certified shape box. Hence all four physical exits are positive for 0<t<=2^-36. All 64 originally nonzero primitive signs persist, so the strict census stays exactly 558 and no weak point remains.

### 8.5 What the interval proof actually certifies

Let C be the rational vector in (8.1), J0=D_U g(C,0), and R0=J0^-1. For each of the initial and path boxes, the checker proves

    beta >= sup ||I-R0 D_U g||_infinity,     beta<1/4,
    sup ||R0 g(C,t)||_infinity+beta*radius < radius.      (8.4)

The suprema are enclosed by exact interval arithmetic, not by samples. Therefore U -> U-R0 g(U,t) is a contraction mapping the relevant closed cube strictly into itself. This proves existence and uniqueness of the actual-centroid root for every parameter in the whole interval. Its Jacobian is nonsingular there, giving the claimed analytic family.

All arithmetic bounds use rational endpoints with 160-bit dyadic outward rounding at every operation. Every division is certified away from zero. The checker also verifies 154 positive geometric guards, including actual supports, strict facet convexity, the sixteen fan tetrahedra and all basal triple intersections. True planarity along the whole family follows from the exact plane-intersection construction and fixed-apex incidences; an interval containing zero is not used as a planarity proof. The four original zero identities follow from (8.2), not from a numerical zero tolerance.

The report includes the exact root equations' generator, isolating boxes, preconditioner, derivative enclosures, all geometric and mechanical interval data and the complete census. The rational seed is explicitly labelled as construction data only. Rational fixed-point iteration using (8.4) refines the exact algebraic point to any required accuracy; no inaccessible floating-point coordinate array is part of its definition.

## 9. Evidence, limits, and continuation

Normal build/check and a clean source-only build/check were actually executed, and the regenerated reports matched byte-for-byte. The numerical locator used to find a seed is not acceptance evidence. The autonomous source below reconstructs the exact rational reference geometry and proves the algebraic initial body and its whole implicit escape interval.

This establishes that actual incidence and true uniform centring alone do NOT force compatible radial Delta signs. A weak-S1U1-specific sign theorem could still hold; the 558 control does not refute one. The new triangular-source theorem instead bypasses those signs by actual geometric freedoms and remains valid on any genuine weak S1U1 input meeting its complete-packet hypotheses.

The remaining cases are explicit: a paired EF source which is a quad; an unpaired quad source with B=0 beyond the handled alternatives; EF source planes genuinely occupied by other protected source/dual obligations; or insufficient unused centroid-corrector triangles even after the source-local footprint reduction. Two disjoint triangle-to-triangle EF pairs can, for example, occupy all four lateral triangles. Failure of this particular correction architecture is still not failure of all same-lattice deformations.

No universal proper110 density, all-E17 exclusion, S1U1 construction, canonical-registry subtraction or bound improvement follows. The new control preserves a material non-record body and an actual all-orders restricted-family failure together with its full-shape rescue. The most useful next extension is to permit contact-occupied planes to participate in centroid correction while compensating their physical outputs, or to treat paired quad sources with a second genuinely independent actuator.

## 10. Complete runnable recovery

Save the following exact source as `transverse_spoke.py`, UTF-8 with LF endings and a final newline. It uses CPython3.13.5, standard library only, assertions enabled; no seed file, external solver, earlier workspace or additional input is required.

    python -B -S transverse_spoke.py build
    python -B -S transverse_spoke.py check

Expected terminal marker:

    ACTUAL_OPPOSITE_DELTA_TRANSVERSE_CENTROID_INTERVAL_PASS
    STRICT 5 5 8; WEAK 4 TO 0; PROTECTED 64; EPS 1/68719476736

Exact pins:

    transverse_spoke.py: 12966 bytes
    SHA256 87a58f941ae0eaac2ed5c2b1bf545416c9056b4a002aa29e0efd0c80e9d1379b
    transverse_spoke_report.json: 196464 bytes
    SHA256 fb52b0878b8dadc4d213c994624447089a662bd9e94c3b6d7379ab84f91c4023

Convenience copies: source (`transverse_spoke.py`) and exact report (`transverse_spoke_report.json`). The literal source below is the durable recovery capsule. The analytic forest and footprint theorems are proved above; they are not inferred from this one control or claimed proof-assistant formalizations.

```python
"""Exact algebraic own-centred 10/17/9 opposite-Delta control.
CPython 3.13.5 standard library; assertions enabled; no external inputs.
python -B -S transverse_spoke.py build
python -B -S transverse_spoke.py check
Strict 5/5/8, NOT S1U1. Entire implicit escape interval is certified.
"""
from fractions import Fraction as F
R=F(21,20)
PARAMS=tuple(F(x,10**8) for x in (225082171,-82658883,-186396676,144995592,245518313,21525122,27871567,70099732,28332266))
FACES=((0,1,2,3,4,5,6),(9,8,7),(7,1,0),(7,2,1),(7,8,3,2),(8,4,3),(8,9,5,4),(9,6,5),(9,7,0,6))
def add(a,b):return tuple(x+y for x,y in zip(a,b))
def sub(a,b):return tuple(x-y for x,y in zip(a,b))
def mul(c,a):return tuple(c*x for x in a)
def dot(a,b):return sum(x*y for x,y in zip(a,b))
def cross(a,b):return (a[1]*b[2]-a[2]*b[1],a[2]*b[0]-a[0]*b[2],a[0]*b[1]-a[1]*b[0])
def det(a):return dot(a[0],cross(a[1],a[2]))
def solve(a,b=(1,1,1)):
 d=det(a)
 return tuple(det(tuple(tuple(b[i] if j==k else a[i][j] for j in range(3)) for i in range(3)))/d for k in range(3))
def initial():
 m,cx,cy,d,ax,u,v,w,t=PARAMS
 a=(R,-F(1));b=add(a,mul(m,(-F(1),R)));c=(cx,cy)
 aa=(ax,R*R+1-R*ax);bb=add(aa,mul(d,sub(b,a)));cc=add(aa,mul(d,sub(c,a)))
 delta=sub(aa,cc);lam=(5*R*R-5*R*cc[0]+2*cc[1])/(5*R*delta[0]-2*delta[1])
 p0=add(cc,mul(lam,delta))
 bot=(p0,(R,F(0)),(R,F(1)),add(bb,mul(u,sub(aa,bb))),add(bb,mul(v,sub(cc,bb))),add(cc,mul(w,sub(bb,cc))),add(cc,mul(t,sub(aa,cc))))
 x=[z+(F(1),) for z in bot]+[z+(-F(1),) for z in(a,b,c)]
 p=[solve([x[i] for i in f[:3]]) for f in FACES]
 assert p[2]==mul(1/(5*R*R+1),(5*R,-F(2),F(1)))
 assert p[3]==(1/R,F(0),F(0)) and p[4]==(1/R,1/(R*R),-1/(R*R))
 return x,p
X0,P0=initial()
def body(u, x0=X0,p0=P0, speeds=None,t=None):
 p=list(p0)
 p[5]=(u[0],u[1],x0[8][0]*u[0]+x0[8][1]*u[1]-1)
 p[7]=(u[2],p0[7][1],x0[9][0]*u[2]+x0[9][1]*p0[7][1]-1)
 if speeds is not None:
  for f,w in speeds.items():p[f]=add(p[f],mul(t,w))
 x=[solve((p[0],p[l],p[r])) for l,r in ((8,2),(2,3),(3,4),(4,5),(5,6),(6,7),(7,8))]+list(x0[7:])
 return x,p

def moments(x):
 D=0;J=(0,0,0)
 for f in FACES:
  a=x[f[0]]
  for k in range(1,len(f)-1):
   b,c=x[f[k]],x[f[k+1]];w=det((a,b,c));D+=w;J=add(J,mul(w,add(a,add(b,c))))
 return D/6,mul(1/(4*D),J)

def target_speed(r,s,a,b,e,v):
 # e is any positive multiple of the actual target-side basal edge.
 rho=dot(r,r);p=mul(1/rho,r)
 theta=(p[2]-b[2])/(a[2]-b[2]);lam=rho*(1-theta)
 d=sub(s,r);bp=sub(b,mul(dot(a,b)/dot(a,a),a))
 beta=(b[0]*s[0]+b[1]*s[1])/(s[0]*s[0]+s[1]*s[1])
 bv=solve(((F(0),F(0),F(1)),r,s),(F(0),F(0),-dot(b,v)))
 ct=-dot(e,e)/dot(r,e);pv=dot(bv,e)-beta*dot(v,e)
 X=(1-pv)/ct;Y=1+lam*X-dot(r,v)
 w=add(mul(X/dot(bp,bp),bp),mul(Y/dot(d,d),d))
 assert dot(a,w)==0
 bb=solve(((F(0),F(0),F(1)),r,s),(F(0),-dot(b,w),-dot(b,v)))
 assert dot(bb,e)-beta*dot(v,e)==1
 assert dot(sub(s,mul(2,r)),w)+dot(r,v)==1
 return w

def speeds():
 z=(F(0),)*3;a=X0[7]
 w3=target_speed(P0[3],P0[4],a,X0[2],(-F(1),R,F(0)),z)
 w2=target_speed(P0[2],P0[3],a,X0[1],(F(0),F(1),F(0)),w3)
 return {2:w2,3:w3}

# Exact algebraic initial point: the unique actual-centroid zero in this box.
CENTER=tuple(F(n,10**30) for n in (-417819504419730630621198890185,
 406482606157541070247829267790,-1253550426273930071347650412813))
ROOT_RADIUS=F(1,10**24)
PATH_RADIUS=F(1,10**6)
EPS=F(1,2**36)
BITS=160
SCALE=2**BITS
ZERO_KEYS=('P:1:2','P:2:3','Q:2:3','Q:3:4')

def down(x):
 x=F(x);return F((x.numerator*SCALE)//x.denominator,SCALE)
def up(x):return -down(-F(x))
class Box:
 def __init__(self,l=0,u=None):
  self.l=down(l);self.u=up(l if u is None else u);assert self.l<=self.u
 @staticmethod
 def cast(x):return x if isinstance(x,Box) else Box(x)
 def __add__(s,t):
  if isinstance(t,Jet):return NotImplemented
  t=s.cast(t);return Box(s.l+t.l,s.u+t.u)
 __radd__=__add__
 def __neg__(s):return Box(-s.u,-s.l)
 def __sub__(s,t):
  if isinstance(t,Jet):return NotImplemented
  return s+-s.cast(t)
 def __rsub__(s,t):return s.cast(t)+-s
 def __mul__(s,t):
  if isinstance(t,Jet):return NotImplemented
  t=s.cast(t);v=(s.l*t.l,s.l*t.u,s.u*t.l,s.u*t.u);return Box(min(v),max(v))
 __rmul__=__mul__
 def __truediv__(s,t):
  if isinstance(t,Jet):return NotImplemented
  t=s.cast(t);assert t.l>0 or t.u<0,('division across zero',t.l,t.u)
  return s*Box(1/t.u,1/t.l)
 def __rtruediv__(s,t):return s.cast(t)/s
 def magnitude(s):return max(abs(s.l),abs(s.u))
class Jet:
 def __init__(self,a=0,b=0):self.a,self.b=a,b
 @staticmethod
 def cast(x):return x if isinstance(x,Jet) else Jet(x)
 def __add__(s,t):
  t=s.cast(t);return Jet(s.a+t.a,s.b+t.b)
 __radd__=__add__
 def __neg__(s):return Jet(-s.a,-s.b)
 def __sub__(s,t):return s+-s.cast(t)
 def __rsub__(s,t):return s.cast(t)+-s
 def __mul__(s,t):
  t=s.cast(t);return Jet(s.a*t.a,s.b*t.a+s.a*t.b)
 __rmul__=__mul__
 def __truediv__(s,t):
  t=s.cast(t);return Jet(s.a/t.a,(s.b*t.a-s.a*t.b)/(t.a*t.a))
 def __rtruediv__(s,t):return s.cast(t)/s

def centroid(u,t=0):return moments(body(u,speeds=speeds(),t=t)[0])[1]
def jacobian(u,t=0):
 cols=[]
 for j in range(3):
  y=[Jet(v,int(i==j)) for i,v in enumerate(u)]
  g=centroid(y,t);cols.append(tuple(z.b for z in g))
 return tuple(tuple(cols[j][i] for j in range(3)) for i in range(3))
def inverse(a):
 cols=[solve(a,tuple(int(i==j) for i in range(3))) for j in range(3)]
 return tuple(tuple(cols[j][i] for j in range(3)) for i in range(3))
def matvec(a,x):return tuple(dot(row,x) for row in a)

def root_certificate(rad,t):
 U=tuple(Box(c-rad,c+rad) for c in CENTER)
 J0=jacobian(CENTER,F(0));R0=inverse(J0)
 J=jacobian(U,t)
 E=tuple(tuple(Box(int(i==j))-sum(R0[i][k]*J[k][j] for k in range(3)) for j in range(3)) for i in range(3))
 contraction=max(sum(z.magnitude() for z in row) for row in E)
 drift=tuple(Box.cast(z).magnitude() for z in matvec(R0,centroid(CENTER,t)))
 assert contraction<F(1,4)
 assert max(drift)+contraction*rad<rad
 return dict(radius=rad,t=t,U=U,exact_center_jacobian=J0,
             center_jacobian_determinant=det(J0),preconditioner=R0,
             derivative_defect=E,contraction=contraction,center_drift=drift,
             margin=rad-max(drift)-contraction*rad)

def edges():
 E=sorted({tuple(sorted((f[k],f[(k+1)%len(f)]))) for f in FACES for k in range(len(f))})
 assert len(E)==17 and sum(map(len,FACES))==34
 assert all(sum(i in f and j in f for f in FACES)==2 for i,j in E)
 return E

def primitives(x,p):
 out={}
 for a,b in edges():
  i,j=[i for i,f in enumerate(FACES) if a in f and b in f]
  for s,t in ((a,b),(b,a)):out['P:%d:%d'%(s,t)]=dot(x[s],sub(x[t],x[s]))
  for s,t in ((i,j),(j,i)):out['Q:%d:%d'%(s,t)]=dot(p[s],sub(p[t],p[s]))
 assert len(out)==68
 return out

def geometry_certificate(U,t):
 x,p=body(U,speeds=speeds(),t=t);guards={}
 def positive(k,z):
  z=Box.cast(z);assert z.l>0,('geometric guard',k,z.l,z.u)
  guards[k]=z
 V,g=moments(x);positive('volume',V)
 for i,v in enumerate(x):
  for j,f in enumerate(FACES):
   if i not in f:positive('slack:%d:%d'%(j,i),1-dot(p[j],v))
 for j,f in enumerate(FACES):
  for k,a in enumerate(f):
   b=f[(k+1)%len(f)]
   for c in f:
    if c not in (a,b):positive('corner:%d:%d:%d'%(j,k,c),dot(p[j],cross(sub(x[b],x[a]),sub(x[c],x[a]))))
  for k in range(1,len(f)-1):positive('fan:%d:%d'%(j,k),det((x[f[0]],x[f[k]],x[f[k+1]])))
 for a,(l,r) in enumerate(((8,2),(2,3),(3,4),(4,5),(5,6),(6,7),(7,8))):
  initial=det((P0[0],P0[l],P0[r]));sgn=1 if initial>0 else -1
  positive('basal_intersection:%d'%a,sgn*det((p[0],p[l],p[r])))
 # Symbolic incidence is by construction. Audit it additionally at exact centers.
 cx,cp=body(CENTER,speeds=speeds(),t=F(0))
 assert all(dot(cp[j],cx[i])==1 for j,f in enumerate(FACES) for i in f)
 return x,p,dict(volume=V,centroid_interval=g,guards=guards)

def classify(signs):
 U=[];S=[];H=[];wv=[];wf=[];we=[]
 for typ,n,strict,weak in (('P',10,U,wv),('Q',9,S,wf)):
  for i in range(n):
   m=max(v for k,v in signs.items() if k.startswith('%s:%d:'%(typ,i)))
   if m<0:strict.append(i)
   if m==0:weak.append(i)
 for a,b in edges():
  i,j=[i for i,f in enumerate(FACES) if a in f and b in f]
  m=max(signs['P:%d:%d'%(a,b)],signs['P:%d:%d'%(b,a)],signs['Q:%d:%d'%(i,j)],signs['Q:%d:%d'%(j,i)])
  if m<0:H.append((a,b))
  if m==0:we.append((a,b))
 assert len(S)+len(U)-len(H)==2
 return dict(stable=S,unstable=U,saddles=H,weak_vertices=wv,weak_facets=wf,weak_edges=we,counts=(len(S),len(U),len(H)))

def physical_certificate(U,t,initial_signs=None):
 x,p,geo=geometry_certificate(U,t);rows=primitives(x,p);signs={}
 for k,z in rows.items():
  if k in ZERO_KEYS:
   # Path signs concern 0<t<=EPS, certified by positive_path_factors().
   signs[k]=0 if initial_signs is None else 1
  else:
   z=Box.cast(z);assert z.l>0 or z.u<0,('unprotected row',k,z.l,z.u)
   signs[k]=1 if z.l>0 else -1
   if initial_signs is not None:assert signs[k]==initial_signs[k]
 return dict(geometry=geo,vertices=x,poles=p,rows=rows,signs=signs,census=classify(signs))

def local_identities():
 a,b0,b1=X0[7],X0[1],X0[2];r,s,v=P0[2],P0[3],P0[4];qf=P0[0];qt=P0[1]
 rho=dot(r,r);rho1=dot(s,s)
 assert mul(1/rho,r)==add(mul(F(3,5),b0),mul(F(2,5),a))
 assert mul(1/rho1,s)==mul(F(1,2),add(a,b1))
 assert b0==add(mul(R*R,s),qf)
 assert b1==add(mul(R*R,v),mul(2,qf))
 assert dot(r,sub(s,r))==dot(s,sub(v,s))==0
 out=[]
 for x,y in ((r,s),(s,v)):
  A=dot(x,x)-dot(qt,x);L=dot(qt,sub(x,qt));D=dot(qt,sub(y,x));B=A+D
  gamma=dot(x[:2],y[:2])/dot(y[:2],y[:2]);Delta=A/gamma-B
  kappa=L*(1-1/gamma)+D
  assert 0<gamma<1 and A>0 and D>0 and kappa>0
  out.append(dict(A=A,B=B,L=L,D=D,gamma=gamma,Delta=Delta,kappa=kappa,
                  gamma_normal=x[2]*(y[2]-x[2])))
 assert out[0]['gamma']==F(441,521) and out[1]['gamma']==F(441,841)
 assert out[0]['Delta']==F(1040,76587) and out[1]['Delta']==-F(16400,194481)
 return out

def positive_path_factors():
 # These three rows and this fourth normalized factor are independent of u.
 t=Jet(Box(0,EPS),Box(1));x,p=body(tuple(Jet(c) for c in CENTER),speeds=speeds(),t=t)
 rows=primitives(x,p)
 functions={'P:1:2':rows['P:1:2'],'Q:2:3':rows['Q:2:3'],'Q:3:4':rows['Q:3:4'],
            'P:2:3_positive_edge_factor':dot(x[2],(-F(1),R,F(0)))}
 zerox,zerop=body(CENTER,speeds=speeds(),t=F(0));zero=primitives(zerox,zerop)
 assert all(zero[k]==0 for k in ZERO_KEYS)
 assert dot(zerox[2],(-F(1),R,F(0)))==0
 for k,z in functions.items():assert Box.cast(z.b).l>0,('exit derivative',k,z.b.l,z.b.u)
 # Because p4 and F are fixed, edge 2->3 is a positive multiple of (-1,R,0).
 X,_=body(tuple(Box(c-PATH_RADIUS,c+PATH_RADIUS) for c in CENTER),speeds=speeds(),t=Box(0,EPS))
 ell=X[2][0]-X[3][0];assert ell.l>0
 return dict(derivatives={k:z.b for k,z in functions.items()},edge_scale=ell)

def clean(x):
 if isinstance(x,F):return str(x)
 if isinstance(x,Box):return [str(x.l),str(x.u)]
 if isinstance(x,Jet):return [clean(x.a),clean(x.b)]
 if isinstance(x,dict):return {str(k):clean(v) for k,v in x.items()}
 if isinstance(x,(list,tuple)):return [clean(v) for v in x]
 return x

def build():
 local=local_identities();root=root_certificate(ROOT_RADIUS,Box(0));ini=physical_certificate(root['U'],Box(0))
 assert ini['census']['counts']==(5,5,8)
 assert ini['census']['weak_vertices']==[1,2] and ini['census']['weak_facets']==[2,3]
 assert ini['census']['weak_edges']==[(1,2),(1,7),(2,3),(2,7)]
 path=root_certificate(PATH_RADIUS,Box(0,EPS));factors=positive_path_factors()
 end=physical_certificate(path['U'],Box(0,EPS),ini['signs'])
 for k in ('stable','unstable','saddles','counts'):assert end['census'][k]==ini['census'][k]
 assert end['census']['weak_vertices']==end['census']['weak_facets']==end['census']['weak_edges']==[]
 return dict(name='ACTUAL_OPPOSITE_DELTA_TRIANGLE_CHAIN_TRANSVERSE_ESCAPE_V1',
             status='Algebraic uniform body, NOT S1U1. All t in (0,epsilon] certified.',
             parameters=PARAMS,R=R,center=CENTER,root_radius=ROOT_RADIUS,epsilon=EPS,
             path_radius=PATH_RADIUS,dyadic_bits=BITS,faces=FACES,edges=edges(),
             seed_vertices=X0,seed_poles=P0,seed_note='Only construction data; the actual body is at the certified centroid root.',
             local_contacts=local,primary_pole_velocities=speeds(),
             root_certificate=root,initial=ini,path_certificate=path,
             positive_path_factors=factors,path_guards=end,protected_nonzero_count=64,
             physical_weak_points_initial=4,physical_weak_points_final=0)

def main():
 import sys,json,hashlib
 from pathlib import Path
 assert __debug__ and sys.version_info[:3]==(3,13,5)
 assert len(sys.argv)==2 and sys.argv[1] in ('build','check')
 sys.set_int_max_str_digits(0)
 report=build();data=(json.dumps(clean(report),sort_keys=True,indent=2)+'\n').encode()
 p=Path('transverse_spoke_report.json')
 if sys.argv[1]=='build':p.write_bytes(data)
 else:assert p.read_bytes()==data
 print('ACTUAL_OPPOSITE_DELTA_TRANSVERSE_CENTROID_INTERVAL_PASS')
 print('STRICT 5 5 8; WEAK 4 TO 0; PROTECTED 64; EPS',EPS)
 for f in (Path(__file__),p):
  b=f.read_bytes();print(f.name,len(b),hashlib.sha256(b).hexdigest())
if __name__=='__main__':main()
```
