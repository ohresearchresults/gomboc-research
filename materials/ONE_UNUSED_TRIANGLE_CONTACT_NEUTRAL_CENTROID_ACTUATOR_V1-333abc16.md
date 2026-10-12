# material-333abc16f59d

AI research material · [Export notes](../catalog/coverage.md#text-records)

---

# ONE_UNUSED_TRIANGLE_CONTACT_NEUTRAL_CENTROID_ACTUATOR_V1

## Status and exact dependency

Coordinator analytic continuation, with a new exact rational interval calculation. The literal parent minimum-0241 was read from cursor 0 through EOF at SHA256 08bb47a0c75336c8605fdad5d2cf800e1e0059f4667088a638a8009efa3d968d. Its TRANSVERSE_TRIANGULAR_SPOKE_FORESTS_AND_ACTUAL_OPPOSITE_DELTA_CONTROL_V1 supplies the actual-COM triangular-source response lemma, source-local protected footprint, exact algebraic uniformly filled body ACTUAL_OPPOSITE_DELTA_TRIANGLE_CHAIN_TRANSVERSE_ESCAPE_V1, and its isolated root box. Those author findings are working premises; the original existence/census computation was not independently replayed here.

New conclusions: (i) one unpaired triangular leaf source can itself supply the missing third centroid-correction direction, replacing one of two formerly unused triangles; (ii) the condition is one explicit genuine geometric scalar, not a free moment tensor; (iii) even a paired leaf can be used if its additional physical response is positive after this completion; (iv) on the SAME exact algebraic parent body, both original target-side EF/VE pairs open while F7 is held exactly fixed and only F5 remains an unused triangular corrector. This is a new analytic germ on the parent's exact body, NOT a renamed body or a new 110 example. The parent and this germ have strict class 558. Bounds remain 34 <= C_min <= 622. No global density or whole-E17 exclusion follows.

## 1. Geometric conventions

Normalize one fixed physical metric and its inverse to M=N=I by a physical linear coordinate change. P is a full-dimensional uniformly filled convex body at its actual volume centroid zero. F and T are disjoint true facets, of sizes seven and three, containing all ten vertices. Their planes need not be parallel. Every basal F vertex is simple; lateral facets consist of four triangles and three quads.

A physical interior-spoke EF i->j has normalized source/target poles r,s, true spoke [a,b], a in T, b in F, and

    r = lambda b + mu a,     lambda,mu > 0,
    d = s-r,                d.a = d.b = d.r = 0.

Write Q_rs = r.(s-r), and retain the actual basal primal responses P_bv = b.(v-b). A weak basal VF requires one of the actual complementary primal/polar pairs, as in the parent. All original nonzero signs are protected by sufficiently small genuine motions.

For a triangular facet G=[a,b,c], let

    T_G = mean_G x x^T.

The actual uniform-centroid differential for its normalized pole velocity w is

    D_g(w) = -alpha_G T_G w,
    alpha_G = Area(G)/(Vol(P)|r_G|) > 0.

Allowed fixed-apex velocities satisfy a.w=0. Consequently its centroid-image plane has normal T_G^{-1}a. For a triangle J=[a_J,b_J,c_J] along a true F edge, the parent's exact identity gives

    n_J = q_F - c_J r_J,
    c_J = (q_F.a_J+3)/4 in (0,1),
    T_J^{-1}a_J = 12 n_J/(q_F.a_J-1).

In particular n_J is nonzero and the image of the two genuine fixed-apex J coordinates is precisely n_J-perp.

## 2. A contact-neutral centroid direction

Let G be a triangular EF source r->s with fixed target velocity v. Set

    ell = s-2r,
    z_G = a cross ell.

For any allowed source velocity w,

    Q_rs' = ell.w + r.v.

Thus z_G preserves both the fixed-apex incidence and the EF row to first order. It is NONZERO. Indeed, on a-perp the covector ell equals d-lambda b_perp, where b_perp is the projection of b onto a-perp; d is nonzero and orthogonal to b_perp. Therefore the covector is not zero. Equivalently ell parallel to a would force the source foot to equal the endpoint a, contradicting the physical interior-spoke hypothesis.

For an unused triangular corrector J, define the actual scalar

    chi(G,J) = n_J . T_G z_G.                         (2.1)

The surface prefactors alpha_G,alpha_J are positive and have no effect on nonvanishing.

### Exact four-by-four rank statement

The linear map from the two allowed G coordinates and two allowed J coordinates to (actual g', Q_rs') is invertible IF AND ONLY IF chi(G,J) != 0.

Proof: in its homogeneous kernel, Q'=0 forces w_G=t z_G. Projecting g'=0 onto n_J gives -alpha_G t chi=0. When chi!=0, t=0 and positive-definiteness of T_J gives w_J=0. Conversely, if chi=0 then T_G z_G belongs to the centroid-image plane of J, so a unique nonzero compensating w_J gives a kernel vector. All four coordinates are genuine same-lattice plane coordinates, because basal vertices are simple and the top apex incidences are imposed exactly. This is an equivalence for this particular actuator, not a statement about all shape deformations.

It follows by the ordinary analytic implicit-function theorem that, with any other compatible planes prescribed near P, one can simultaneously enforce actual g=0 and prescribe Q_rs(t) analytically. The nonlinear contact equation, not just its first jet, is part of the implicit system. No affine-centroid or vertex-average approximation is made.

## 3. Complete-packet theorem using ONE unused triangle

Use the parent's directed physical EF forest D. Assume its triangular-source and unpaired-quad conditions, except that the two-unused-triangle hypothesis is replaced by:

1. G is an UNPAIRED triangular EF source, has no incoming D arrow, and is free of the other protected source-local obligations.
2. J is a lateral triangle outside every D endpoint and all protected source-local obligations.
3. chi(G,J) != 0.

The other sources may have arbitrary permitted basal partners when triangular; unpaired quad sources have the parent's B_i != 0 condition. The complete packet may first be taken as all these EFs/partners plus the entire T-carried packet.

Assign all source velocities except G by the parent's reverse-forest construction. This is possible without G: its no-incoming condition means no other requested EF has it as its target. For all other sources prescribe the resulting top-incidence-preserving analytic plane motions, using the genuine radial motion for a moving quad. Keep all remaining planes except G,J fixed. Now use the four-by-four implicit system to impose

    actual g(t)=0,          Q_G(t)=t.

Every other source and target pole is as prescribed. Neither G nor J is an endpoint of another D arrow. Hence the basal vertex of every other paired EF is unchanged by their corrective variation. The other endpoint of a partnered basal edge may move; the parent's actual incidence identity includes precisely this motion and protects the physical first response. All handled EF/partner exits are strictly positive at first order. No additional basal partner is owed at G by hypothesis.

The entire T-carried packet stays exactly neutral: top vertices are fixed; triangles share no T edge; quads are fixed or undergo their genuine top-edge-preserving radial rescaling. Open T at amplitude t^2 by the parent's carrier flow, reconstruct all real incidences and use the fully movable simple F plane for the resulting order-two actual-COM correction. Positive order-one exits persist. Thus the entire packet regularizes, with fixed physical metric and selected orders at most two.

For arbitrary other weak groups in the initially parallel-end class, use the parent's auxiliary non-spoke opening at epsilon=t^2 and its SMALL source-local footprint H_src. Require G,J and all explicitly moving sources outside H_src as well as the stated D conditions. The minor remains nonzero on the auxiliary family. Prescribe Q_G(new)=Q_G(auxiliary)+t, and apply the same implicit completion. The other auxiliary exits are exactly protected or multiplied by positive true-edge length factors. Their selected orders are at most twenty; both members of each chosen VF pair are retained. The nonparallel actuator is applicable even if the auxiliary input has lost end parallelism.

This is a sufficient complete-packet theorem beyond the old two-unused-triangle architecture. A zero chi, an occupied G or J, or an incoming arrow to G is not an all-shape obstruction.

## 4. Paired leaf extension and the genuine scalar test

If G has a basal partner, the same implicit system remains valid, but its additional physical response must be checked rather than assumed. Fix every other prescribed velocity and put Q_G(t)=tau t, tau>0. Invertibility makes every additional first response at G an affine function of tau.

For a VE partner write P_G'=p0+p1 tau. A positive choice exists exactly when the open half-lines tau>0 and p0+p1 tau>0 intersect. In particular p0>0 or p1>0 is necessary and sufficient. For a VF test each ACTUAL complementary pair and retain positivity of both scalar responses; this gives an intersection of finitely many open intervals, not permission to drop a member of the pair. This criterion concerns the selected one-corrector first-jet architecture only.

When these genuine responses are positive, the same implicit and higher-order gluing proof establishes complete-packet escape. The following exact calculation demonstrates the paired case on a real uniformly centred body with an all-orders radial conflict.

## 5. Exact new germ on the parent's algebraic 558 control

Keep the SAME object ACTUAL_OPPOSITE_DELTA_TRIANGLE_CHAIN_TRANSVERSE_ESCAPE_V1 and all its exact data from the parent. Its four original zero rows are P12,P23,Q23,Q34; its strict census is 558, with 64 originally nonzero primitives. Let G=F2, J=F5, and target F3. F2 is a leaf of 2->3->4. All three involved top vertices and both end planes stay fixed. Crucially F7, the parent's other centroid corrector, now stays EXACTLY FIXED.

Use the parent's exact constants R=21/20, actual root coordinates U, rational isolating center

    C=(-417819504419730630621198890185,
         406482606157541070247829267790,
       -1253550426273930071347650412813)/10^30,
    |U-C|_infinity <= 10^-24.

The exact existence and uniqueness of the true actual-COM root in this box is the parent's theorem. C itself is not substituted for the actual body. The F2 and F3 vertices needed for their second moments are rational and unaffected by U. The corrector normal is affine in U:

    r5=(U0,U1,x8_x U0+x8_y U1-1),
    n5=q_F-r5/2.

The complete new checker proves, over the ENTIRE isolating cube,

    5921/500000 < chi(F2,F5) < 11843/1000000.           (5.1)

Prescribe the exact parent F3 velocity

    w3=(80000/370881,10988501/14128800,-441/800).

Keep poles 0,1,4,6,7,8 fixed. Solve for the two fixed-apex coordinates of r2(t) and the two fixed-apex coordinates of r5(t) by

    g(t)=0,             Q23(t)=t.

This defines a genuine analytic local family by (5.1). Pole r3(t)=r3+t w3 is prescribed. The new calculation, using the correct actual volume derivative, proves

    29536/100 < P12'(0) < 29537/100,                   (5.2)
    Q23'(0)=Q34'(0)=1,
    d/dt [x2(t).(-1,R,0)] at t=0 = 1.

The last function is the normalized P23 factor. Because F and F4 stay fixed, its true edge remains a positive multiple of (-1,R,0); its other endpoint may move under F5 correction. Therefore P23 also opens positively. All four physical exits open at order one. All 64 nonzero guards persist on some sufficiently small interval; strict census remains 558 and no weak point remains.

The original parent's numerical radius 2^-36 is NOT inherited. This new arc has an analytic local existence/positivity interval, with no numerical radius claimed. The algebraic object is unchanged; only the germ differs.

### Exact calculation of the new derivative

For a triangular oriented facet, Delta_G=det(a,b,c)>0 and alpha_G=Delta_G/(2V). Put ell=s-2r, z=a cross ell, and let base in a-perp satisfy ell.base+r.w3=1. Define

    L=Delta_2 T_2 base + Delta_3 T_3 w3,
    K(U)=Delta_2 n5(U).T_2 z,
    h(U)=-n5(U).L.

Then the completed G velocity is

    w2=base+[h(U)/K(U)] z.

Its remaining centroid load lies in the image of F5; the F5 fixed-apex coordinates cancel it. For e=(0,1,0) and beta=R^2, the exact partnered response is

    P12'=b0'.e-beta w3.e,
    (q_F,r2,r3)b0'=(0,-b0.w2,-b0.w3).

After multiplication by K(U)>0, this is affine in U. The checker bounds its numerator and denominator exactly on the isolating cube. It also verifies the other two normalized first responses equal one symbolically. No numerical centroid residual is used as a certificate.

## 6. Reproducibility and limits

Complete standalone new source is contact_neutral_actuator.py, 7631 UTF-8 bytes, LF with final newline, SHA256 5d6c204d5c804e4f891cbc4cac5faa77ce02d581b461717e3b9c5ec1bd00c6a8. It contains every rational input used by this calculation; it uses CPython >=3.10 standard library, assertions enabled. Executed environment CPython 3.13.5. It relies on the parent theorem for the identity/existence of the exact algebraic body; it does not purport to replay that theorem.

Commands:

    python -B -S contact_neutral_actuator.py build
    python -B -S contact_neutral_actuator.py check

Terminal marker:

    ONE_UNUSED_TRIANGLE_CONTACT_NEUTRAL_MINOR_PASS
    CHI_INTERVAL 5921/500000 11843/1000000
    PAIRED_P12_DERIVATIVE 7384/25 29537/100

Reproduced report contact_neutral_actuator_report.json: 5786 bytes, SHA256 321e5e3fbd6cad7e6decca0a82adb4fd441212c3eb9c14f0bb3e5299fa493ef8. Both normal build/check and clean source-only build/check were executed; regenerated reports were byte-identical.

Remaining questions: can actual target-class geometry remove chi=0 resonances or force the paired scalar interval to be nonempty; can several occupied source/target planes jointly correct actual COM; and can paired quadrilateral sources be handled without a radial sign hypothesis? These are not settled by the present one-corrector theorem. No weak S1U1 input, universal regularization, complete E17 lower exclusion or attaining improvement is claimed.
