# minimum-0243

AI research report · 2026-09-25 UTC · [Export notes](../../catalog/coverage.md#text-records)

---

# SATURATED_OCCUPIED_TRIANGLE_PAIRS_ESV_ESCAPE_AND_BALANCED_FIBRES_V1

Slot-5, Bright Harbor 33. Branch `[internal-source-reference]`.

## 1. Main result and remaining mechanism

**The saturated four-triangle configuration regularizes whenever neither basal partner is a target-side VE.** More precisely, suppose the complete physical weak packet consists of the T-carried packet, two interior-spoke EFs whose four source/target facets are distinct triangles, and their possible basal partners. At each spoke, permit no basal weak partner, a source-side basal VE, or a basal VF borne by F. Then there is an analytic same-lattice regularization at the actual uniform-volume centroid, with one fixed physical metric and its inverse. The off-T contacts open at order one and the complete T-carried packet at order two.

All four lateral triangles may therefore be contact-occupied. No unused triangular corrector, nonzero chi assumption, generic response-rank hypothesis, or radial sign assignment is required. The proof makes the occupied pairs themselves supply the centroid correction. It also works with nonparallel disjoint end facets containing all ten vertices.

A second construction covers further packets, including target-side basal VEs. Each individual triangular pair has an explicit one-dimensional **actual-centred, constant-volume deformation fibre**, with every other supporting plane fixed. If either pair has a successful first-order physical selector along this fibre, the entire saturated packet regularizes, allowing any permitted partner at the other pair. Selected orders are at most three. This is an explicit geometric exchange direction, not a generic actuator-rank test.

The unresolved part of the primary saturated class is consequently narrower: a genuinely nonregularizable input must contain at least one **target-side basal VE**, and neither pair can admit the successful balanced-fibre selector just described. These are necessary remaining conditions, not a sufficient obstruction. No weak S1U1 input is asserted. For an actual weak S1U1 input in either successful class, the result is proper110 at the same lattice. The accepted internal minimum interval and independent attaining obligation remain 34<=C_min<=622. fileciteturn47file2L9-L13

There is also a new exact negative control on the SAME algebraic parent body `ACTUAL_OPPOSITE_DELTA_TRIANGLE_CHAIN_TRANSVERSE_ESCAPE_V1`, still strict558. Its first EF/target-VE pair cannot escape within its actual-centred two-plane fibre, even to higher order. The full shape escapes already supplied by the parent and coordinator remain valid; they leave this restricted fibre.

## 2. Authority and scope

The entire updated journal, its complete literal parent, and both new supplied materials were read through EOF. Mounted-byte checks match:

    research-journal: 365097 bytes
    SHA256 8faf082a1c0e8c863b3b664315397da52f95ff203b33f9fbd6e9fd6f22879ee0

    ONE_UNUSED_TRIANGLE_CONTACT_NEUTRAL_CENTROID_ACTUATOR_V1.md: 13751 bytes
    SHA256 333abc16f59d09decc7e88cb032e8e61bfa8dcc770673a043480e1f5808b7dc4

    contact_neutral_actuator.py.txt: 7631 bytes
    SHA256 5d6c204d5c804e4f891cbc4cac5faa77ce02d581b461717e3b9c5ec1bd00c6a8

The direct immutable parent is `minimum-0241`, SHA256 `08bb47a0c75336c8605fdad5d2cf800e1e0059f4667088a638a8009efa3d968d`. Its genuine transverse source motions, physical partner classification, source-local footprint and exact algebraic body identity are retained. No conflict with its literal payload was found.

The supplied one-unused-triangle result proves invertibility of a particular centroid/contact system when its genuine scalar chi is nonzero. The new theorem instead treats two fully occupied pairs and proves the required compatibility from actual moment and polygon geometry, including the singular cases appearing in the VF argument below. fileciteturn47file0L37-L84

## 3. Setting and notation

Let P be a genuine uniformly filled V10/E17/F9 body at its actual volume centroid 0. Its disjoint true facets F and T have seven and three vertices, respectively, and contain all ten vertices. Start with any one physical SPD metric M and N=M^-1. A constant physical linear normalization makes M=N=I for the proof; the actual uniform centroid transforms affinely under this normalization.

Every F vertex has exactly one spoke to T and is simple. There are four lateral triangles and three lateral quads. Only the quads share an edge with T. During the main first stage, both end planes, all top vertices, all three quads and the physical metric remain fixed. Only the four occupied triangular planes move.

For one EF pair, write

    R=[a,b,c],       S=[a,b,e],

where a is its top endpoint, b its basal endpoint, and c,e are the two true F-neighbours of b. Let r,s be the normalized poles, with r the EF-bearing pole. Put q=q_F. Then

    r = lambda b + mu a,       lambda,mu>0,
    d = s-r,                  d.a=d.b=d.r=0.             (3.1)

The pole foot r/|r|^2 lies in relint[a,b]. The two primal derivatives along that spoke are strictly negative. A weak basal partner is therefore exactly a source-side VE on F cap R, a target-side VE on F cap S, or a VF borne by F. This is a physical classification, not a classification of unrelated zero rows. fileciteturn47file4L9-L25

Call the three partner types used by the principal theorem:

    E: no basal weak partner;
    S: source-side basal VE;
    V: basal VF borne by F.

There can be at most one V partner, since F has a unique perpendicular foot. A target-side VE is deliberately not included in this E/S/V notation.

The mechanical functions remain

    P_bv=b.(v-b),          Q_rs=r.(s-r).

At every VF the selected primal and polar exits must form an actual complementary pair. The proof below checks this explicitly.

## 4. The exact four-coordinate occupied-pair moment block

### 4.1 True coordinates and uniform support bounds

Use the three linearly independent physical vectors a,b,c as a linear coordinate basis. This is only a coordinate calculation; it does not reset the physical metric. In this basis,

    a=(1,0,0), b=(0,1,0), c=(0,0,1),
    q=(theta,1,1), r=(1,1,1), s=(1,1,1-j),
    H=1-theta,       j=1-s.c>0,

and true incidence gives

    e=(-j u/H, 1+u+theta j u/H, -u),       u>0.          (4.1)

Here u is the ratio of the absolute determinants of the two actual facet triangles:

    D_R=|det(a,b,c)|,
    D_S=|det(a,b,e)|=u D_R.

In particular

    q.e=s.e=1,        r.e=1-j u.

The actual uniformly filled centroid supplies the strict bounds

    0<H<4,        0<j<4,        0<j u<4.                (4.2)

For completeness, for a true facet with pole p and an outside vertex x, coning the actual boundary to x gives p.x>=-3 at uniform centroid 0. Equality forces the whole body to be the pyramid over that facet with apex x. Apply this to F,a; S,c; and R,e. P is not a pyramid over F, and a pyramid over either triangular facet would be a tetrahedron, not this body. Thus all three relevant inequalities are strict. These are constraints on the actual uniform volume, not independent reference or moment parameters. fileciteturn47file3L12-L27

### 4.2 Genuine plane coordinates

Let w and v be the source and target pole velocities. They fix a. Use the four independent evaluation coordinates

    a.w=0, b.w=x, c.w=y,
    a.v=0, b.v=X, e.v=Z.                               (4.3)

Every such velocity is a genuine local plane motion. All basal vertices are reconstructed from their three incident planes. The top incidences remain exact, including at nonsimple top vertices. Strict support and convexity persist locally.

For a true triangular facet G,

    T_G=mean_G xx^T
       =[(a+b+c)(a+b+c)^T+aa^T+bb^T+cc^T]/12.

The original uniform-centroid derivative is

    g'=-D_R T_R w/(2V)-D_S T_S v/(2V).                 (4.4)

This is the actual boundary-flux derivative. Moving the ends of edges on a fixed neighbouring plane produces no omitted independent edge load.

Define W by its four physical-vector columns:

    W=[a+2b+c, a+b+2c, u(a+2b+e), u(a+b+2e)].           (4.5)

Then, in the chosen vector basis,

    g'= -D_R/(24V) W (x,y,X,Z)^T.

A direct determinant identity is

    det W[:,0,1,2] = j u^2(H-4)/H !=0.                 (4.6)

Thus these TWO OCCUPIED triangles always have a rank-three actual centroid map. Its unique kernel is

    k=(2u,-u,-2,1)^T.                                 (4.7)

The issue is not access to the centroid directions. It is which of them remain available while the physical contacts are retained or opened.

## 5. Contact-neutral moment planes with a geometric sign structure

### 5.1 Source-side VE partners

Suppose b is a source-side VE. Its actual normal-cone representation is

    b=beta r+psi q,        beta,psi>0.

Equation (3.1) implies

    d=-c_0(c-b),          c_0>0.                       (5.1)

Consider the two-dimensional subspace

    x=y=X,        Z arbitrary.                        (5.2)

It is neutral for BOTH Q_rs and the basal VE to first order, regardless of how the other endpoint of the basal edge moves.

Indeed w.d=0, r.w=lambda x and r.v=lambda X, so Q'=0. The basal derivative satisfies q.b'=0 and r.b'=s.b'=-x, hence d.b'=0. Therefore

    P'=b'.(c-b)-beta w.(c-b)=0.

This includes any compatible motion of c. It is not an assumption that c stays fixed.

The image of (5.2) under the centroid map is a genuine two-dimensional plane. It is two-dimensional because the kernel vector (4.7) cannot satisfy x=y unless its coefficient is zero. Define

    C=4-H=theta+3,
    K_S=2(u+1)(u+3)-3j u,
    n_S=2K_S q-C[3r+u(u+4)s].                          (5.3)

Then n_S is an exact normal to that moment plane. The actual support bounds imply

    K_S=2(u-1)^2+4+3u(4-j)>0.

The following exact identities will be important:

    n_S.(a+3b)       =-6C j u<0,
    n_S.(a+b+2c)     = 2C j u(u+1)>0,
    n_S.(a+b+2e)     = 0.                              (5.4)

No response determinant involving the physical metric is being assumed nonzero. Even if the EF and VE responses become positively dependent on a larger space, the explicit subspace (5.2) remains available.

### 5.2 Unpaired EFs

For type E, only Q_rs must be kept neutral. In the a,b,c basis let the common inverse metric be N_hat. Equation (3.1) means

    N_hat r=(mu,lambda,0),       lambda>0.

Put

    nu=j(N_hat)33>0,       kappa=j(N_hat)23.

The true EF differential in coordinates (4.3) is

    Q'=(-lambda-kappa)x-nu y+lambda X.                 (5.5)

Thus

    Q'(k)=u(nu-2kappa)-2lambda(u+1).                   (5.6)

If (5.6) is nonzero, the Q-neutral subspace already maps ONTO all three centroid directions: correct any centroid load and then use the moment kernel k to annul Q'. This case needs no second neutral moment plane.

If (5.6) is zero, the Q-neutral centroid image is two-dimensional. Set

    K_E=lambda(2+2u-j u)+nu u^2,
    n_E=4K_E q-C[2lambda r+u(2lambda+nu u)s].           (5.7)

It is an exact normal to that image. To verify this, the covector

    ell= -2K_E q/(j u^2 C)
         +lambda r/(j u^2)
         +(2lambda+nu u)s/(2j u)

satisfies ell^T W equal to the row (5.5) when (5.6)=0, and n_E=-2j u^2 C ell.

The actual bounds (4.2), not an arbitrary coefficient assumption, give K_E>0. For u<=1,

    2+2u-j u=2(1-u)+u(4-j)>0;

for u>=1,

    2+2u-j u=2(u-1)+(4-j u)>0.

The corresponding identities are

    n_E.(a+3b)       =-4j u C lambda<0,
    n_E.(a+b+2c)     = 2j u^2 C nu>0,
    n_E.(a+b+2e)     = 0.                              (5.8)

This deals with the exceptional unpaired response exactly; it is not discarded as nongeneric.

### 5.3 Why these normals cannot agree across disjoint pairs

Both n_S and n_E have the form

    n=Aq-Br-Ds,       A,B,D>0,                         (5.9)

and satisfy

    n.(a+3b)<0,
    n.(a+b+2c)>0,
    n.(a+b+2e)=0.                                     (5.10)

They have two useful actual-polygon properties:

**First, b is the unique minimum of n on F.** For x in F,

    n.x-n.b=B(1-r.x)+D(1-s.x)>=0,

with equality only at F cap R cap S={b}.

**Second, n is strictly positive at every other true vertex of F.** From the first identity in (5.10),

    (B+D)/A>(theta+3)/4>theta,

so n.a<0. If n.b>0, (5.9) already proves the assertion. If n.b<=0, the last two identities in (5.10) give n.c>0 and n.e>0. Every other vertex x of the convex polygon F can be written

    x=b+t(c-b)+v(e-b),       t,v>=0,       t+v>=1.

The tangent cone gives t,v>=0; the true diagonal ce separates b from all other polygon vertices and gives t+v>=1. Hence

    n.x=(1-t-v)n.b+t n.c+v n.e>0.

Now take the canonical normals from two disjoint pairs, with distinct basal endpoints b1,b2. They cannot be positively proportional, since that would give the same unique minimum on F. They cannot be negatively proportional either: any basal vertex different from b1,b2 has strictly positive value under both. Therefore their two centroid-image planes are DISTINCT and together span R^3.

This is the main geometric coupling. The quarter-height bounds establish the coefficient signs; true facet intersection and the actual two neighbours of each basal corner prevent the residual centroid normals from coinciding. A dimension count alone would not prove this.

## 6. Completion when both partners are E or S

A positive primary velocity for either type is available by moving the source pole in direction d=s-r while holding its target fixed. The spoke endpoint b stays fixed, and

    Q'=|d|^2>0.

For a source-side VE, (5.1) also gives

    P'=-beta d.(c-b)=beta j>0.

Choose such primary velocities for both pairs. If one type-E pair has (5.6) nonzero, its Q-neutral centroid image is all R^3, so use it to cancel the total actual centroid load without changing any selected contact first derivative.

Otherwise use the two contact-neutral planes from Section 5. They span R^3, so their velocities cancel the total centroid load. Every selected EF and source-VE derivative stays strictly positive.

The two local contact blocks do not acquire hidden cross terms. Their pole sets are disjoint and F is fixed, so each basal source vertex depends only on its own two lateral planes. A motion of another pair can move an edge's other endpoint, but the differentiated normal-cone incidence used in Section 5 includes and cancels precisely that contribution. Thus this is a simultaneous centred first jet, not an unjustified sequence of independent carrier flows.

## 7. A basal VF can also participate without an unused corrector

At most one pair has a basal F-VF. Let this be the V pair and let the other pair be E or S.

If the other pair has a three-dimensional contact-neutral centroid image, its correction can accommodate any positive EF/VF primary velocity, and the preceding proof applies. Otherwise let n be its canonical normal from Section 5; its contact-neutral centroid image is n-perp.

It suffices first to find a V-pair velocity with all its selected physical exits positive and

    n.g'_V=0.                                         (7.1)

### 7.1 Physical VF variables and the pointed bad cone

At the VF,

    b=q/|q|^2.

The two pole evaluations b.w,b.v determine the arbitrary basal velocity m=b' in the tangent plane of F. The remaining two coordinates are independent hinges about the line ab. Both hinges leave m, and all VF first responses, unchanged.

Write m=E u in the true F-edge basis and G=E^T E. The exact first-order complementary condition is

    u_i>0 and (G u)_i>0 for at least one i.              (7.2)

For G=[[a,c],[c,b]], ab>c^2, the failed directions are

    G u<=0 when c>=0;
    u<=0   when c<=0.

These are closed pointed cones. Consequently no entire nonzero line, and no open half-plane, consists of failed directions. This is the genuine paired VF criterion. It includes c=0, the right-corner case.

### 7.2 Two occupied hinges and the exceptional case

Let the source hinge be w=d,v=0 and the target hinge w=0,v=d. Their effects are:

    source hinge: Q'=|d|^2>0, centroid direction proportional to +(a+b+2c);
    target hinge: Q'=0,       centroid direction proportional to -(a+b+2e).

Both are VF-neutral. Indeed d.b=0 and b is proportional to q, so d.q=0 as well.

If n sees the target hinge, choose any successful VF mismatch, open Q with the source hinge, and cancel the scalar centroid load with the target hinge.

Suppose n does not see the target hinge but sees the source hinge. Solving (7.1) fixes the source-hinge coefficient, and Q' becomes a linear functional L(m) of the two mismatch coordinates. If L is nonzero, its positive half-plane contains a successful VF direction by (7.2).

L CANNOT be identically zero here. Otherwise n.g'_V would be a nonzero scalar multiple of Q' on the entire four-coordinate V pair. Forgetting its VF partner, the pair would then be exactly the exceptional unpaired case of Section 5.2, and n would be proportional to its canonical n_E. Section 5.3 forbids proportionality between that normal and the other pair's canonical normal.

Finally suppose n sees neither hinge. Its scalar centroid load depends only on m. Choose a nonzero m in its kernel which succeeds in (7.2); a pointed cone cannot contain both directions of that line. Then open Q by the source hinge. If the scalar functional is zero, any successful mismatch works.

Thus (7.1) always has a strictly successful EF/VF velocity. No nonzero chi hypothesis was inserted at the exceptional step.

### 7.3 Adding the other pair and cancelling the full centroid

Choose a positive primary velocity for the E/S pair and multiply it by a sufficiently small positive constant delta. The unrestricted centroid map of the V pair has rank three by (4.6), so a small additional V-pair velocity cancels the new scalar n-load. Positivity of its already strict EF and complementary VF derivatives persists for sufficiently small delta.

The remaining centroid load is in n-perp. Cancel it with a contact-neutral velocity of the E/S pair. Its own exits remain positive, and the V-pair first responses are unaffected by the other endpoint motions. This constructs the required simultaneous actual-centred first jet for every E/S/V combination.

## 8. Integration, complete T packet, and other guards

The successful first jet is a vector V0 in the eight genuine fixed-apex plane coordinates, with

    Dg V0=0

and every selected off-T physical exit strictly positive to first order.

The actual centroid map has rank three; a single occupied triangular pair already supplies the nonzero minor (4.6). Choose those three plane coordinates as a correction subspace B. Solve

    g(t V0+B z(t))=0,       z(0)=0.

The analytic implicit-function theorem gives z'(0)=0, hence z(t)=O(t^2). These are actual fan-volume centroid equations of the ORIGINAL uniformly filled body. Every selected positive order-one exit survives. This integrates the first jet into a genuine same-lattice family, rather than treating a tangent solution as sufficient without a realization argument.

Throughout this first stage, T and its vertices are fixed and all three quads are fixed. Its within-T primal rows and its T-source polar rows are therefore exactly unchanged. The complete T-carried packet remains neutral, including a bearing EF or VF.

Now open T at amplitude eta=t^2 using the accepted intrinsic carrier flow

    a_i -> a_i+eta(K R_i y_i+b_0),
    y_i=a_i-p_T,       R_i=y_i^T M y_i,
    p_T=Nq_T/(q_T^T Nq_T).

Use b_0=0 without a bearing EF/VF, an inward translation at a bearing EF, or an outgoing true edge at a bearing VF, and choose K to dominate the finitely many VE translation terms. This opens the actual complementary pair at a VF, including a right corner. fileciteturn56file0L157-L169

For a direct extension, solve each lateral quad's two moving top incidences with one fixed independent pole normalization, and each triangle's one moving top incidence with two normalizations. Reconstruct the simple basal vertices. Correct the actual centroid through the fully movable F plane, whose surface-second-moment derivative is invertible. This changes the first-stage body by O(t^2), too late to spoil its order-one exits. F need not remain parallel to T during this final completion, but the true lattice is unchanged.

M and N=M^-1 remain fixed throughout. All originally nonzero geometric and mechanical guards persist on a sufficiently small interval. Every original weak vertex and weak facet has a positive selected exit, so the physical selector theorem retains all original strict S,U,H labels and leaves no other strict or weak equilibrium. Harmless algebraic zeros need not disappear. fileciteturn47file15L78-L93

This proves the principal theorem, including complete T-carried packets and all the stated basal partners.

### Protected additional groups

There is also an initially parallel-end extension with other weak groups. Use the literal parent's source-local footprint H_src for the remaining groups: a basal primal source freezes its own two lateral planes; a top-to-basal row freezes the basal target's two planes; a non-T polar row freezes its lateral endpoint poles. Within-T rows need no further planes. At a VF retain both physical group protections.

If NONE of the four moving triangular planes lies in H_src, the parent's auxiliary non-spoke opening at epsilon=t^2 can be combined with the construction above. Extend the initially successful eight-coordinate velocity analytically and solve the actual centroid equations on the auxiliary family. The handled pair exits remain positive at order one; the other selected exits are kept exactly or multiplied by positive true-edge length factors. Their orders are at most twenty. This is a conditional footprint extension, not a claim that arbitrary additional F-carried groups avoid the four occupied triangles.

## 9. The actual-centred constant-volume two-plane fibre

The kernel (4.7) has a useful independent interpretation and gives an additional saturated escape class.

Hold every plane except R,S fixed. Use the finite affine pole coordinates corresponding to the evaluations (4.3), and set Z=t. Equation (4.6) permits solving the three actual centroid equations uniquely for x(t),y(t),X(t). The resulting analytic fibre satisfies

    (x,y,X,Z)=t(2u,-u,-2,1)+O(t^2).                    (9.1)

It is the entire local actual-centred two-plane realization fibre, not a selected formal jet.

Its actual volume is also constant. For any allowed motion of either triangle, with a and F fixed, the true surface formulas give

    d(q.J)=[(theta+3)/4] dV,

where J is the ORIGINAL volume first moment. Thus

    q.J-[(theta+3)/4]V

is constant throughout this four-coordinate plane family. On the centred fibre J=0, and theta+3>0; therefore V=V0 exactly. This is genuine volume and centroid conservation, not independently fixed cell weights.

### Balanced-fibre escape test

Let w_k,v_k be the unique pole velocities satisfying

    (a,b,c) w_k=(0,2u,-u),
    (a,b,e) v_k=(0,-2,1).                              (9.2)

Compute the actual EF derivative

    q_k=(s-2r).w_k+r.v_k.

For a VE partner with bearing pole p and coefficient b=beta p+psi q, let

    (q,r,s)b_k'=(0,-b.w_k,-b.v_k),
    p_k=b_k'.edge-beta p_k'.edge,                       (9.3)

where p_k' is w_k or v_k according to the bearing facet. This includes the edge's other-end motion.

For type E, q_k!=0 gives a successful orientation. For a VE partner,

    q_k p_k>0                                         (9.4)

is exactly the successful first-order two-plane test. For a basal VF, test each actual complementary pair on the two orientations of (9.2); retain positivity of both members and of q_k.

If either pair in the saturated configuration passes this test, first follow its centred fibre in the successful orientation. Its contacts open at order one, while the other pair stays EXACTLY weak: that pair's poles and basal source vertex are fixed, and its edge rows can only acquire positive length factors. The whole T packet also stays exactly neutral.

Next open the second pair at amplitude t^2 by the parent's genuine triangular-source construction, using the first pair's two now-open triangular planes as centroid correctors. Their rank-three moment minor is already proved. Their corrections are O(t^2) and cannot destroy the first pair's positive order-one exits. This second pair may have a target-side VE or a basal VF. Finally open T at t^3. All selected orders are at most three, with fixed M,N and actual COM throughout.

This argument supplies the simultaneous sign/isolation proof needed for sequencing; it does not assume that one carrier's flow leaves another unchanged.

### Exact scope of a failed balanced test

For a VE partner, if q_k p_k<0, the two forced exits have opposite nonzero derivatives in the local coordinate of the one-dimensional centred fibre. They therefore have opposite signs at EVERY sufficiently close noninitial point of that fibre. No higher-order reparameterization can make both positive.

This is an all-orders obstruction to the actual-centred TWO-PLANE family with all other planes and M fixed. It is not an obstruction to four-plane correction, to other shape directions, or to full same-lattice regularization. Equality in (9.4) remains a higher-order question; it is not classified as failure here.

## 10. Exact relative countercontrol on the unchanged algebraic 558 body

Use EXACTLY `ACTUAL_OPPOSITE_DELTA_TRIANGLE_CHAIN_TRANSVERSE_ESCAPE_V1` from the literal parent. Its actual body is the isolated uniform-centroid root, not its rational reference seed. The parent strict census is 558, and the four original zero rows are P12,P23,Q23,Q34. fileciteturn57file0L19-L34

For its first pair take

    a=x7, b=x1, c=x0, e=x2,
    q=q_F0, r=q_F2, s=q_F3.

These four vertices and three poles are rational and are unchanged by the parent's algebraic F5/F7 centroid completion. All other ACTUAL supporting planes, including the algebraic F5,F7, are held fixed in the new relative fibre.

The exact balanced direction (9.2) gives

    Q23'=-5692094294790568508776142572787339236320
          /5351914121477973276715904325281257796089 <0,

    P12'=175661701010536566693
          /28083216002510914600 >0.                    (10.1)

The complete new source checks both fractions, the true zero contact and normal-cone identities, the local support bounds, and the EXACT zero actual first-moment load of this direction. Equations (4.6) and (9.1) then prove the local fibre statement, so (10.1) excludes simultaneous P12,Q23 escape throughout this actual-centred two-plane germ.

This does not replace or contradict the parent's full-shape escape. The new coordinator germ explicitly moves F5 in addition to its prescribed F3 and corrected F2 while holding F7 fixed, and escapes the relative obstruction. Its analytic local interval remains distinct from the parent's certified numerical interval. fileciteturn47file0L94-L130

No new body, S1U1 example, census computation, or numerical radius is asserted by this relative calculation. Normal build/check and a clean source-only build/check of the NEW identity/derivative unit were executed, with byte-identical reports. The old algebraic-body existence and strict census were used as supplied premises, not independently replayed.

## 11. What is now left

The previous exhausted-corrector condition is no longer an obstruction for the complete E/S/V saturated class. Two occupied patches supply either a full contact-neutral centroid map or distinct geometrically constrained moment planes. A basal VF does not require a further unused plane: its complementary alternatives, together with the unpaired resonance classification, remove the remaining scalar obstruction.

In the primary saturated class, the unresolved partner mechanism now necessarily includes a target-side basal VE. Some such cases are removed by the exact balanced-fibre test and sequential construction of Section 9. The remaining cases require genuinely coupled target-pair response control, or a weakS1U1-specific restriction on that geometry. The opposite signs in (10.1) show why local two-plane centring alone cannot simply be presumed to work.

This is not universal proper110 density, an exclusion of the full E17 layer, a new canonical registry subtraction, or an attaining improvement. The source-side and VF closure is stronger than a generic finite actuator test; the target-side residual is not promoted to a full-shape obstruction.

## 12. Complete runnable recovery unit

Save the following source as `occupied_pair_moments.py`, UTF-8 with LF endings and a final newline. Place the SUPPLIED `contact_neutral_actuator.py.txt` beside it, unchanged. That 7631-byte dependency has SHA256 `5d6c204d5c804e4f891cbc4cac5faa77ce02d581b461717e3b9c5ec1bd00c6a8`; the new script verifies it before loading its exact rational inputs. No older workspace, seed file, generated report, or archive lookup is required.

Executed stack: CPython3.13.5, SymPy1.14.0, assertions enabled.

    python -B occupied_pair_moments.py build contact_neutral_actuator.py.txt
    python -B occupied_pair_moments.py check contact_neutral_actuator.py.txt

Expected markers:

    SATURATED_OCCUPIED_PAIR_MOMENT_IDENTITIES_PASS
    ACTUAL_558_TWO_PLANE_CENTRED_FIBRE_OPPOSED_EXITS_PASS

Exact pins:

    occupied_pair_moments.py: 6724 bytes
    SHA256 aaeb383822717a9295ad6e01935f7941ad89e657c6f7869cba716c4bf2367743

    occupied_pair_moments_report.json: 5747 bytes
    SHA256 26fc9f6c10c48b66027c72fd52ff841eefb42f9db33c7d93ad1ccae4c6940ddd

Convenience copies: [source](sandbox:/mnt/data/saturated_work/occupied_pair_moments.py) and [exact report](sandbox:/mnt/data/saturated_work/occupied_pair_moments_report.json). The literal unit below is the durable new recovery. The saturated theorem is the analytic proof above, not an inference from these identities or from the non-S1U1 control.

```python
"""Occupied adjacent-triangle moment identities and one relative countercontrol.
Python 3.13.5 / SymPy 1.14.0, assertions enabled.
The algebraic body's existence and census are premises from minimum-0241.
The only input dependency is the supplied contact_neutral_actuator.py.txt (pinned below).
Usage: python -B occupied_pair_moments.py build|check [dependency_path]
"""
from fractions import Fraction as F
from pathlib import Path
import hashlib
import json
import sys
import types
import sympy as S

PARENT_SHA = '5d6c204d5c804e4f891cbc4cac5faa77ce02d581b461717e3b9c5ec1bd00c6a8'

def identities():
    u,j,H,lam,nu = S.symbols('u j H lam nu', positive=True)
    kap = S.symbols('kap', real=True)
    a,b,c = (S.eye(3)[:,i] for i in range(3))
    theta = 1-H
    e = S.Matrix([-j*u/H, 1+u+theta*j*u/H, -u])
    q = S.Matrix([theta,1,1])
    r = S.Matrix([1,1,1])
    s = S.Matrix([1,1,1-j])
    assert all(S.simplify(z-w)==0 for z,w in zip((q.dot(e),s.dot(e),r.dot(e)),(1,1,1-j*u)))
    W = S.Matrix.hstack(a+2*b+c,a+b+2*c,u*(a+2*b+e),u*(a+b+2*e))
    kernel = S.Matrix([2*u,-u,-2,1])
    assert S.simplify(W*kernel) == S.zeros(3,1)
    minor = S.factor(W[:,[0,1,2]].det())
    assert minor == j*u**2*(H-4)/H
    C = 4-H
    KS = 2*(u+1)*(u+3)-3*j*u
    nS = 2*KS*q-C*(3*r+u*(u+4)*s)
    ZS = S.Matrix([[1,0],[1,0],[1,0],[0,1]])
    assert S.simplify(nS.T*W*ZS) == S.zeros(1,2)
    assert S.simplify(nS.dot(a+3*b)+6*C*j*u) == 0
    assert S.simplify(nS.dot(a+b+2*c)-2*C*j*u*(u+1)) == 0
    assert S.simplify(nS.dot(a+b+2*e)) == 0
    Q = S.Matrix([[-lam-kap,-nu,lam,0]])
    qker = S.factor((Q*kernel)[0])
    assert S.simplify(qker-(u*(nu-2*kap)-2*lam*(u+1))) == 0
    resonance = (nu-2*lam*(1+1/u))/2
    KE = lam*(2+2*u-j*u)+nu*u**2
    ell = (-2*KE/(j*u**2*C))*q + lam/(j*u**2)*r + (2*lam+nu*u)/(2*j*u)*s
    assert S.simplify(ell.T*W-Q.subs(kap,resonance)) == S.zeros(1,4)
    nE = 4*KE*q-C*(2*lam*r+u*(2*lam+nu*u)*s)
    assert S.simplify(nE+2*j*u**2*C*ell) == S.zeros(3,1)
    assert S.simplify(nE.dot(a+3*b)+4*j*u*C*lam) == 0
    assert S.simplify(nE.dot(a+b+2*c)-2*j*u**2*C*nu) == 0
    assert S.simplify(nE.dot(a+b+2*e)) == 0
    # Exact decompositions used to prove positive q_F coefficients from true support bounds.
    assert S.expand(KS-(2*(u-1)**2+4+3*u*(4-j))) == 0
    assert S.expand((2+2*u-j*u)-(2*(1-u)+u*(4-j))) == 0
    assert S.expand((2+2*u-j*u)-(2*(u-1)+(4-j*u))) == 0
    return {'coordinates':{'a':a,'b':b,'c':c,'e':e,'q_F':q,'r':r,'s':s},
            'moment_map_12W':W,'moment_kernel':kernel,'nonzero_minor':minor,
            'source_partner_neutral_basis':ZS,'source_normal':nS,
            'source_positive_coefficient':KS,'unpaired_row':Q,
            'unpaired_kernel_response':qker,'unpaired_resonance_kappa':resonance,
            'unpaired_conormal':ell,'unpaired_normal':nE,'unpaired_positive_coefficient':KE}

def load_parent(path):
    raw=path.read_bytes()
    assert len(raw)==7631 and hashlib.sha256(raw).hexdigest()==PARENT_SHA
    module=types.ModuleType('supplied_contact_neutral_actuator')
    module.__file__=str(path)
    exec(compile(raw,str(path),'exec'),module.__dict__)
    return module

def relative_control(parent):
    x,p=parent.initial()
    a,b,c,e=(x[i] for i in (7,1,0,2))
    q,r,s=(p[i] for i in (0,2,3))
    D=abs(parent.det((a,b,c)))
    DS=abs(parent.det((a,b,e)))
    u=DS/D
    j=1-parent.dot(s,c)
    H=1-parent.dot(q,a)
    assert 0<j<4 and 0<j*u<4 and 0<H<4
    assert parent.dot(r,parent.sub(s,r))==0
    beta=parent.R**2
    assert b==parent.add(parent.mul(beta,s),q)
    w=parent.solve((a,b,c),(F(0),2*u,-u))
    v=parent.solve((a,b,e),(F(0),F(-2),F(1)))
    TG=parent.moment_triangle((a,b,c))
    TJ=parent.moment_triangle((a,b,e))
    load=parent.add(parent.mul(D,parent.matvec(TG,w)),parent.mul(DS,parent.matvec(TJ,v)))
    assert load==(0,0,0)
    bp=parent.solve((q,r,s),(F(0),-parent.dot(b,w),-parent.dot(b,v)))
    edge=parent.sub(e,b)
    dq=parent.dot(parent.sub(s,parent.mul(2,r)),w)+parent.dot(r,v)
    dp=parent.dot(bp,edge)-beta*parent.dot(v,edge)
    assert dq<0<dp
    # This point is NOT the rational seed: these particular four vertices/poles
    # are unchanged by the parent's algebraic F5/F7 centroid completion.
    return {'body':'ACTUAL_OPPOSITE_DELTA_TRIANGLE_CHAIN_TRANSVERSE_ESCAPE_V1',
            'parent_assignment':'minimum-0241',
            'parent_assignment_sha256':'08bb47a0c75336c8605fdad5d2cf800e1e0059f4667088a638a8009efa3d968d',
            'strict_census_premise':[5,5,8],
            'status':'Only poles F2,F3 vary; all other actual poles, including algebraic F5/F7, stay fixed.',
            'root_center':parent.C,'root_radius':parent.RAD,
            'local_vertices':[a,b,c,e],'local_poles':[q,r,s],
            'u':u,'j':j,'H':H,'source_velocity':w,'target_velocity':v,
            'actual_first_moment_load_without_common_factor':load,
            'P12_derivative':dp,'Q23_derivative':dq,'derivative_product':dp*dq,
            'conclusion':'Opposite nonzero signs exclude simultaneous P12,Q23 escape in the entire local actual-COM two-plane fibre. Not a full-shape obstruction.',
            'radius':'No new numerical radius or replay of parent body existence/census.'}

def clean(x):
    if isinstance(x,F): return str(x)
    if isinstance(x,S.MatrixBase): return clean(x.tolist())
    if isinstance(x,S.Basic): return str(x)
    if isinstance(x,dict): return {k:clean(v) for k,v in x.items()}
    if isinstance(x,(list,tuple)): return [clean(v) for v in x]
    return x

def main():
    assert __debug__ and sys.version_info>=(3,10) and S.__version__=='1.14.0'
    assert len(sys.argv) in (2,3) and sys.argv[1] in ('build','check')
    path=Path(sys.argv[2] if len(sys.argv)==3 else 'contact_neutral_actuator.py.txt')
    report={'name':'SATURATED_OCCUPIED_PAIR_MOMENTS_V1','symbolic':identities(),
            'relative_control':relative_control(load_parent(path)),
            'scope':'Analytic saturated escape theorem is proved in the handoff; these are identities and one relative non-S1U1 countercontrol, not a sampled proof.'}
    data=(json.dumps(clean(report),sort_keys=True,indent=2)+'\n').encode()
    out=Path('occupied_pair_moments_report.json')
    if sys.argv[1]=='build': out.write_bytes(data)
    else: assert out.read_bytes()==data
    print('SATURATED_OCCUPIED_PAIR_MOMENT_IDENTITIES_PASS')
    print('ACTUAL_558_TWO_PLANE_CENTRED_FIBRE_OPPOSED_EXITS_PASS')
    print('Q23_PRIME',report['relative_control']['Q23_derivative'])
    print('P12_PRIME',report['relative_control']['P12_derivative'])
    for p in (Path(__file__),out):
        raw=p.read_bytes();print(p.name,len(raw),hashlib.sha256(raw).hexdigest())
if __name__=='__main__': main()
```
