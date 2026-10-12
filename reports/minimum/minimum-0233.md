# minimum-0233

AI research report · 2026-09-25 UTC · [Export notes](../../catalog/coverage.md#text-records)

---

# CARRIER_NEUTRAL_MULTICONTACT_AND_CLOSED_FACET_ESCAPE_V1

Slot-5, Bright Harbor 33. Branch `[internal-source-reference]`. Continuation of literal parent `minimum-0232`, SHA-256 `8f50ef8265eca079539078c4b0edce571a7ca4548fba2850729bd16d2e756f03`.

## 1. Main results and scope

**The physical locations of the weak points may now replace the parent's stricter bearing-facet condition.**

**Closed-facet theorem.** Let P be a genuine uniformly filled V10/E17/F9 body at its actual volume centroid, with one physical SPD metric M. If all its physical weak equilibrium points lie in one closed true facet F, then P has an arbitrarily small analytic same-lattice regularization preserving every original labelled strict equilibrium and removing every physical weak point. A VE edge may leave F; an EF or VF may be borne by a different facet. Thus this is a genuinely multi-bearing-facet theorem, not a restatement of the parent's one-carrier class.

**Dual closed-facet theorem.** The same conclusion holds if all exposed rest-support faces at the weak points contain one common true vertex v. Here a VE contributes its exposed edge, and an EF or VF contributes its bearing facet. Their physical locations need not be v or on edges incident to v. The polar argument keeps the actual centroid of the ORIGINAL uniformly filled body; it never centres a uniformly refilled polar.

A second advance resolves more dispersed packets. There is an explicit two-parameter family of actual-COM-preserving deformations which is **mechanically neutral on an entire chosen carrier**. Its two response coefficients at every other weak contact are given below. A simultaneous positive response on the off-carrier contacts can be combined with a carrier polygon flow without unproved sequential isolation. In particular this gives open geometric rescue classes with one or two additional physical weak points, including two additional VFs. Certain completely blind first responses also have explicit order-three off-carrier and order-four full rescue.

Three new exact actual E17 controls have six physical weak points each, with strict counts respectively (2,4,4), (4,5,7), and (6,4,8). All regularize on the entire interval 0<t<=2^-24. The last has a right-corner VF: the correct complementary pair becomes positive while two other algebraic zeros persist harmlessly. None of the controls is S1U1.

Every theorem consequently applies to a weak S1U1 input meeting its stated hypotheses, but **no such first-layer input is supplied, no universal density or obstruction theorem is proved, and no complexity bound changes**. The supplied working interval remains 34<=C_min<=622.

## 2. Authority, notation, and the retained parent input

The updated journal was read completely, including its complete immutable parent payload. Its mounted bytes match 316405 bytes and SHA-256 `0117862a2121c22529a823d7e5c0f2b2cfc5d537d95c44c6eb6f8aa9c4879ac5`. The unchanged atlas and radial-index sources remain the earlier supplied inputs. No inaccessible archive, source-only hash, private parent workspace, or hypothetical S1U1 body is a computational dependency.

The parent proves arbitrary local analytic prescription of every individual primal or polar facet polygon in this layer, with genuine incidence and actual ORIGINAL-body centroid completion. Its carrier consists of VEs on edges of that facet and the EF/VF borne by it. It explicitly does not license sequencing such flows across different carriers. Those are the premises used here.

Work initially at the actual centroid 0. The original body has metric M and inverse N=M^-1. To give one formula for either side, let Z denote P or its same-origin polar P°, and set

    Z=P:     A=M, D=N, K=5 Sigma_P;
    Z=P°:    A=N, D=M, K=(5 Sigma_P)^-1.

Sigma_P is always the actual covariance of the ORIGINAL uniform body. In particular K on the polar side is not five times the covariance of a uniformly filled polar.

Choose a true carrier facet of Z in H={x:q.x=1}. Put

    ell=Kq,       s=q^T Dq,       k=q^T Kq>0.

The geometry and metric variables used below have the single common inverse D=A^-1 at every parameter value. The metric pencil is genuine physical actuation, not a second freely chosen polar metric. It can alternatively be absorbed into an analytic linear deformation of the body: for original coordinates with metric M(t), apply C(t)=M(0)^-1/2 M(t)^1/2. Then C(t)^T M(0) C(t)=M(t), C(0)=I, and the actual uniform centroid remains zero. Thus the regularizations also have a fixed-physical-metric realization.

The physical selectors remain those of the supplied radial-index theorem: protect all originally nonzero primitives and give a positive exit at each original weak vertex/facet. This removes weak points without adding equilibria and retains the strict labels; no weak-edge groups or demand that every algebraic zero disappear is introduced.

## 3. An exact two-parameter carrier-neutral family

### 3.1 Axial shape parameter, primal side

For small sigma define the plane-fixing projectivity

    T_sigma(x)=x/[1+sigma(1-q.x)].                         (3.1)

Refill its image uniformly and compute its actual centroid g_sigma. Apply

    C_g(y)=y-g(1-q.y)/(1-q.g).                            (3.2)

This is an invertible affine map fixing H pointwise and sending the actual centroid to zero. Its linear determinant is 1/(1-q.g)>0. Hence both the prescribed polygon and the true lattice are unchanged, while the actual centroid, not merely a reference point, is zero.

For an outward true boundary fan the actual quantities used in (3.2) are

    D0=sum det(Y_a,Y_b,Y_c),
    J0=sum det(Y_a,Y_b,Y_c)(Y_a+Y_b+Y_c),
    g=J0/(4D0).                                          (3.3)

The parent's exact affine centroid retraction is the source of (3.2); (3.1) supplies the additional carrier-neutral freedom exploited here.

The uniform-volume Jacobian of (3.1) is

    (1+sigma)/[1+sigma(1-q.x)]^4.

Consequently the raw centroid derivative is 5 Sigma_P q=ell. After (3.2), every vertex and every normalized pole r of Z have derivatives

    x_sigma'=(q.x-1)(x+ell),
    r_sigma'=(1+r.ell)(r-q).                              (3.4)

The pole formula follows either from the actual transformation of the supporting planes or from the true incidence equations. It is not an assigned independent polar velocity.

### 3.2 Axial shape parameter, polar side

Apply (3.1) to R=P°, with carrier v.r=1; here q=v. Its polar is exactly

    Q_sigma=(1+sigma)P-sigma v.                           (3.5)

To complete the actual ORIGINAL centroid, choose the locally unique small covector p for which the uniform image x/(1+p.x) of Q_sigma has centroid zero, and then apply I+v p^T to that image. Its polar is the raw deformed R followed by

    r -> r+p(1-v.r)/(1+p.v).                             (3.6)

Thus the full prescribed polar polygon is fixed pointwise. The actual original-volume functional is

    g_Q(p)= integral_Q x(1+p.x)^-5 dx
            / integral_Q (1+p.x)^-4 dx.

At Q=P,p=0 its p-derivative is -5 Sigma_P. Local analytic centring follows by the implicit function theorem; positive denominators and the original lattice persist locally. Since the raw centroid derivative in (3.5) is -v, p'=-(5 Sigma_P)^-1 v. This gives exactly (3.4), now with K=(5 Sigma_P)^-1. The parent's polar completion retains this original-body volume law.

General projective centroid fitting is established background, not a novelty claim of this handoff; the new use here is the mechanically neutral carrier family and its simultaneous off-carrier responses.

### 3.3 Independent normal-metric parameter

Use

    A_tau=A+tau q q^T,
    D_tau=D-[tau/(1+tau s)] Dq q^T D.                     (3.7)

For sufficiently small positive or negative tau these are SPD and exact inverses. The carrier foot is fixed exactly:

    D_tau q/(q^T D_tau q)=Dq/s.

The restriction of A_tau to tangent vectors of H is unchanged. Every within-carrier primal row x_i^T A_tau(x_j-x_i) is therefore unchanged.

For a neighboring facet with pole r, any plane-fixing genuine projectivity followed by (3.2) or (3.6) sends its pole to

    r_new=q+lambda_r(r-q),      lambda_r>0                (3.8)

locally, because it fixes the entire true edge H cap {r.x=1}. Its carrier-source dual row becomes

    q^T D_tau(r_new-q)
      =lambda_r/(1+tau s) * q^T D(r-q).                  (3.9)

Equations (3.7)–(3.9) prove exact neutrality, not only zero first derivatives: the complete carrier polygon, its foot, all within-carrier primal signs, and all carrier-source dual signs are preserved. Both complementary VF pairs are retained. The same statements hold when applying the family to an already slightly deformed carrier polygon.

## 4. Simultaneous response theorem

### 4.1 The two physical response coefficients

At a weak VE x->x+e of Z, write

    a=q.x, d=q.e, r=x^T A x.

Its axial and normal-metric response vector is

    alpha=(a-1) ell^T A e+d(r+x^T A ell),
    beta=a d.                                            (4.1)

At a weak EF of Z with bearing pole r and adjacent pole h, set

    zeta=q^T Dr, d=q^T D(h-r), rho=r^T Dr.

The responses of its forced dual row are

    alpha=-(1+r.ell)d+((h-r).ell)(rho-zeta),
    beta=-zeta d.                                        (4.2)

These follow by differentiating (3.4) and (3.7), using the actual zero row. At a VF, apply these same row derivatives to its two zero primal and two zero dual rows, keeping one valid complementary cross-edge pair.

### 4.2 Gluing with a carrier flow

Partition the entire physical weak packet into a subpacket C carried by the chosen facet in the parent's sense and its complement R. Choose one complementary pair at each VF in R. Suppose there is one vector (u,w) such that

    u alpha_i+w beta_i>0                                 (4.3)

for every selected scalar exit of R. Then the entire packet regularizes by an analytic same-lattice, actual-COM-preserving curve with positive first derivatives on all required selected exits.

Proof: take a parent carrier flow with parameter t. It opens every required exit in C. Let b_i be its actual first derivative on each selected exit in R. Compose with the neutral family at sigma=c u t,tau=c w t, where c>0 is sufficiently large that

    b_i+c(u alpha_i+w beta_i)>0  for all i in R.

Neutrality preserves the carrier exits, including both members of each chosen VF pair, exactly up to their positive factors. Every off-carrier exit is included in the displayed simultaneous sign test. Actual incidence and the actual uniform centroid are retained at every stage. Original nonzero guards are open, so the reduced physical selector theorem finishes the proof.

This proves a genuine successful first jet, not a sequence which silently assumes that different carrier flows do not interfere. The construction may use arbitrary true polygon extension, not only projective-affine motion of a frozen body.

For a fixed off-carrier selector, failure of (4.3) is equivalent to 0 belonging to the convex hull of its two-dimensional response vectors. Such failure has a certificate using at most three scalar rows. This is only an obstruction for THIS two-parameter neutral family. It is not a full-realization stress, a three-physical-point nonregularizability theorem, or an all-orders obstruction.

## 5. Proof of the closed-facet and dual theorems

Use Z=P and suppose every physical weak point lies in the closed carrier facet F. The off-carrier contacts need not be borne by F. Nevertheless **the single neutral direction tau<0 opens all of them simultaneously**.

**VE at v in F with exposed edge v->w leaving F.** Since q.v=1 and q.w<1,

    P_vw(tau)=tau(q.w-1)>0.                              (5.1)

**EF in F borne by G!=F.** Its minimal true edge is necessarily F cap G. Write r=q_G and rho=r^T Nr. Its foot lies in F, so r^T Nq=rho, while s-rho=|q-r|_N^2>0. The exact forced exit is

    Q_GF(tau)=-tau rho(s-rho)/(1+tau s)>0.                (5.2)

**VF at v in F borne by G!=F.** Let e_1,e_2 be the two outgoing true edges of G at v. Convex support gives q.e_i<=0, with at least one strict inequality: otherwise both independent edge directions, and hence G itself, would lie in F's plane. With tau decreasing, the first derivatives of the two zero primal rows are therefore nonnegative and not both zero.

Let G0=E^T M E be the actual positive-definite corner Gram matrix. The parent's mismatch coordinates satisfy

    P=G0 u,
    Q_1=s_G delta_1 u_2,   Q_2=s_G delta_2 u_1,
    s_G,delta_1,delta_2>0.                               (5.3)

For the normal direction, p=P' is nonnegative and nonzero. Since

    p^T G0^-1 p>0,

some i has both p_i>0 and (G0^-1 p)_i>0. Thus the SAME direction gives a strict positive first derivative for P_i and its complementary Q. This argument includes right corners and does not replace the two paired exits by an unrelated row. The exact flag coupling is retained from the parent.

Every off-carrier contact has now been opened by one common neutral direction. Every carried contact is left untouched. Section 4 glues this direction to the carrier flow, proving the closed-facet theorem.

For the dual statement, let p be an original physical weak point and W(p) its exposed rest-support face. Its corresponding polar physical point is

    p*=Mp/(p^T Mp).

For a true vertex v of P,

    v.p*=1  iff  v belongs to W(p).

Thus all W(p) containing v means exactly that all polar physical weak points lie in the closed polar facet corresponding to v. Apply the closed-facet proof there, using the polar completion of Section 3.2 and the same inverse pair. No uniform polar centroid is used.

The new conclusion is an existence statement for compatible VF choices. It must not be strengthened to say that every arbitrarily preselected wrong VF branch has no full-tangent stress.

## 6. Off-carrier VFs, generic two-point rescue, and a finite higher-order escape

### 6.1 A two-dimensional VF geometry

At a VF of Z with bearing pole r, set

    rho=r^T Dr, z=Dr/rho, a=q.z, b=r.ell,
    n=Dq-rho a z, ell_T=ell-b z.

Both n and ell_T are tangent to the bearing facet. The actual mismatch derivatives under the two neutral parameters are

    W_tau=a n,
    W_sigma=(a-1)ell_T+(1+b)n/rho.                        (6.1)

The neutral map to the two-dimensional mismatch plane is invertible exactly when

    a(a-1) det(z,Dq,Kq) != 0.                            (6.2)

This is a geometric mixed-moment condition at the actual original body, not an independence assumption on formal tensors.

For corner Gram matrix G0=[[a0,c0],[c0,b0]], paired first-order success means some u_i>0 and (G0 u)_i>0. If c0>=0, failure is exactly G0 u<=0. If c0<=0, failure is exactly u<=0. To verify these equivalences, use positive definiteness a0b0>c0^2 to rule out positive coordinates and positive images being supported on opposite indices. Therefore in either case the bad directions form a closed pointed cone, whose angular width is strictly less than pi. At c0=0 this is simply the negative quadrant.

### 6.2 Consequences for one or two additional physical points

Relative to a chosen carrier, the following are sufficient:

- One additional simple VE/EF with nonzero response vector; or one additional VF with a nonzero mismatch response in at least one neutral direction.
- Two additional simple VE/EF points with linearly independent response vectors.
- One additional VF with invertible map (6.1), together with one additional simple point with nonzero response vector.
- Two additional VFs, both with invertible maps (6.1).

For two simple points solve the two-by-two response system with right-hand side (1,1). For a VF and a simple point, an open positive half-plane cannot be contained in a closed pointed VF bad cone. For two VFs, the union of their two bad cones cannot cover the direction circle: each has width less than pi. Choose a direction outside the bad sets and use the actual complementary pairs it supplies. Section 4 then applies.

For a single VF, any nonzero mismatch w obeys w^T G0 w>0. At least one paired product w_i(G0w)_i is positive, and one of w or -w makes both entries positive. This proves the one-point assertion without requiring rank two.

These conditions cover packets with arbitrarily many carrier contacts; they are not limited to a total of three physical points. They are not asserted automatically on every hypothetical S1U1 input.

### 6.3 Blind first responses rescued at order three/four

There is also an exact finite higher-order mechanism for one off-carrier contact. It specifically illustrates why a failed neutral first-jet selector is not an all-orders obstruction.

For a single off-carrier VE, suppose a=q.x=0, d=q.e!=0, and initially alpha=0. Its normal response is zero, and the normal pencil preserves this VE exactly. At the premoved metric A_tau the axial response becomes exactly

    alpha(tau)=-tau d k,      k=q^T Kq>0.                (6.3)

Choose tau=t and sigma=-sign(d)t^2. The selected off-carrier row has leading coefficient |d|k t^3>0. Use the carrier polygon flow at parameter t^4. All carrier exits are positive at order four, exactly preserved by the neutral transformations; its contribution cannot change the already positive off-carrier order-three term.

Consequently a single off-carrier VE is rescued whenever d!=0, even if both original neutral first responses vanish. If d=0, its first response succeeds unless ell^T A e=0. The residual d=0,ell^T A e=0 is a limitation of this argument, not a genuine obstruction.

For a single off-carrier VF, suppose a=0 and W_sigma=0. The normal pencil preserves the VF exactly. Here n=Dq, and W_sigma=0 gives ell_T=(1+b)Dq/rho. Taking the q-product shows

    k=(1+b)s/rho>0.

Thus at the premoved metric,

    W_sigma(tau)=-[k tau/(1+tau s)] Dq.                  (6.4)

Take tau=t and sigma=epsilon t^2, choosing epsilon=1 or -1 so that the resulting nonzero leading mismatch has one strict complementary pair. Again the VF exits at order three and a carrier flow at t^4 completes the packet. At a right corner the first two mismatch jets are zero and a strict paired third term is selected; no right-corner second-jet threshold is discarded.

Combining this with (6.1), a single off-carrier VF is rescued whenever its bearing facet is not parallel to the chosen carrier, or when the two are parallel but ell_T!=0. The remaining parallel case with ell_T=0 is not ruled out by these neutral motions. No corresponding blanket assertion is made for all blind EF cases, or for several simultaneously blind off-carrier points.

All order statements here concern explicitly integrated actual deformations. They do not rely on truncating the full problem at a guessed universal jet order. The supplied general rational retraction and all-orders criterion remain separate available tools.

## 7. Three new exact actual E17 controls

All controls are uniformly filled, actually centred, use true maximal facets and edges, and have one common M(t),N(t)=M(t)^-1. Every original strict label persists on the entire interval 0<t<=2^-24.

| Control | Initial strict (S,U,H) | Physical weak packet | Neutral rates (sigma/t,tau/t) | Positive interval guards |
|---|---:|---|---:|---:|
| B8_SIX_VE | (2,4,4) | Four carrier VE plus two VE outside the carrier | (1,-1) | 242 |
| HEPT_OBTUSE_VF_EF | (4,5,7) | Four carrier VE, one carrier VF, one external EF | (0,30) | 232 |
| HEPT_RIGHT_VF_EF | (6,4,8) | Four carrier VE, one right carrier VF, one external EF | (0,570) | 232 |

The complete packets satisfy neither of the old one-carrier alternatives. These are non-S1U1 controls for the new neutral-family gluing mechanism; they are not presented as computational verification of every body in the analytic closed-facet theorem.

### 7.1 B8: neither neutral knob alone opens both outside contacts

Raw base vertices 0..7 lie at z=1 with horizontal coordinates

    (1,0),(1,1/4),(0,1),(-1/3,1),
    (-1,0),(-1,-1/2),(0,-1),(2/3,-1).

Raw vertex8=(0,0,-3), raw vertex9=(4/5,-4/5,1/5). True face cycles are

    (0,1,2,3,4,5,6,7), (0,1,8,9), (1,2,8),
    (2,3,8), (3,4,8), (4,5,8), (5,6,8),
    (6,7,9,8), (7,0,9).

Orient outward and apply (3.2) using the raw body's actual centroid and q=(0,0,1). This leaves the base unchanged and gives

    X8=(-742/5463,1901/7284,-5399/1821),
    X9=(4222/5463,-5447/7284,377/1821).

Its actual volume is 130321/32778. Use

    M=diag(108626543272/1008891919,
           417435378368/9080027271,1).

The six weak VE rows are 0->1,2->3,4->5,6->7,8->3,9->7. There are exactly six zero primitives and sixty-two protected nonzeros. Strict S={0,7}, U={1,3,5,7}, H={0-9,1-2,3-4,5-6}.

For the two off-carrier rows, the exact response vectors are

    8->3:
      alpha=-37853054482366649600/18276613826034745377,
      beta =-38980780/3316041;
    9->7:
      alpha=10249939260265302080/124330706299556091,
      beta =544388/3316041.

Both separate response columns have opposite signs at the two contacts. Hence neither sign of axial motion alone nor either sign of normal-metric motion alone opens both. Nevertheless alpha-beta is strictly positive at both, and their two-by-two determinant is

    96727076552039262340064000/99845141331627813994551 > 0.

This is an actual homogeneous countercontrol to using either individual neutral knob as a universal off-carrier resolver, NOT a blockage of every full-shape direction. In fact the chosen carrier extension also contributes favourably here; no necessity of these two knobs among all genuine deformations is claimed.

The carrier polygon uses the parent's intrinsic radial-cubic flow with zero translation, at parameter t/1024. Keep raw vertex8 fixed; determine raw vertex9 from the moving two quad planes and a fixed transverse plane through its initial value. Apply actual centroid correction, then axial sigma=t and normal tau=-t. The complete rational curve and its interval proof are in the source.

### 7.2 Heptagon controls: mixed EF and paired VF, including a right corner

Both heptagon controls use the true cycles

    F0=(0,1,2,3,4,5,6), F1=(7,8,9),
    F2=(0,1,8,7), F3=(1,2,8), F4=(2,3,9,8),
    F5=(3,4,9), F6=(4,5,9), F7=(5,6,7,9), F8=(6,0,7).

For HEPT_OBTUSE_VF_EF the raw base z=10 has coordinates

    (0,0),(1,0),(1,1/2),(3/4,1),
    (1/4,11/8),(-7/16,3/2),(-1,1/2).

The top triangle at z=-30 is generated by pairwise intersections of

    -y=1,      2x+y=4,      -x+(9/16)y=3.

For HEPT_RIGHT_VF_EF start at (0,0),(1,0), multiply the last complex coordinate by 1+i/4 four times, and append (0,3/4). Thus the base is exactly

    (0,0),(1,0),(1,1/4),(15/16,1/2),
    (13/16,47/64),(161/256,15/16),(0,3/4).

Its top lines at z=-30 are

    -y=1,      4x+y=4,      -3x+(161/16)y=20.

In both cases label top intersections (line2,line0),(line0,line1),(line1,line2) as 7,8,9. Perform actual centroid correction (3.2) with q=(0,0,1/10). This is a complete rational initial-body recipe, not a dependency on the old parent workspace.

With the resulting actual poles p_f, put e=p_4-p_3 and take M=diag(1,1,m), where

    m=-p_3,z e_z/(p_3,x e_x+p_3,y e_y).

The exact values are

    obtuse: 10765868984114493/461092370545331200;
    right:  22773326134487278410696924025
            /558387867960357733775650258944.

This puts one actual EF at the interior of true edge2-8, borne by F3, with Q34=0. Its physical point is not in F0. The other weak points are four VEs 1->2,2->3,3->4,4->5 and the single VF(vertex0,F0). There are nine zero primitives: P01,P06,Q02,Q08,P12,P23,P34,P45,Q34. The full report distinguishes P34 from Q34 and deduplicates the VF represented on two edges.

Use carrier translation (1,0,0), carrier scale constant 1 in the obtuse case and 8 in the right case, with parameter t/1024. The top edges remain parallel to the corresponding moving base edges 01,23,56; pairwise top-line intersections preserve all three genuine quads. Actual centroid correction is then applied. The single external EF response is dominated by the normal rate 30 or570, respectively, computed by the exact deterministic rule in the source. These rates are not fit after freezing the centroid.

Both selected VF exits P01 and Q08 have strictly positive derivatives throughout the certified interval. In the obtuse example Q02 remains zero but P06 becomes negative. In the right example **P06=Q02=0 identically**, while P01,Q08 are positive and the whole packet is physically weak-free. The right-corner shape keeps its two carrier edges orthogonal throughout the curve, so this is not merely a limit of an obtuse calculation.

### 7.3 What the exact checker establishes

There are 706 certified positive interval guards across the three controls and 180 protected originally nonzero primitives. All twenty selected scalar exits have strictly positive derivatives on the closed interval [0,2^-24], so their initially zero values are positive throughout its punctured interval. Exact interval automatic differentiation uses rational endpoints with 128-bit dyadic outward rounding at every operation. Every division has a denominator certified away from zero; no floating-point tolerance or parameter sampling is a proof input.

True planarity for the entire curves follows from the explicit quad constructions and invertible projective/affine maps. It is not inferred from interval boxes containing zero. The source additionally audits actual incidences and the uniform centroid at the full first jet and at the exact endpoint, the full strict/weak endpoint census, actual moments at all stages, support slacks, strict facet convexity and all sixteen true boundary-fan triangles. Integration diagonals are not mechanical edges.

Neutral-only endpoint audits retain precisely the four or five carrier weak points and remove the other one or two. Their all-orders neutrality is proved in Section3, rather than inferred from those endpoint audits.

## 8. Recovery, execution status, and remaining frontier

The following complete source is independent of all older code. Save it as `carrier_neutral.py`, UTF-8 with LF endings and a final newline. Use CPython3.13.5, standard library only, assertions enabled. No seed, external input, numerical solver or additional file is required.

    python -B -S carrier_neutral.py build
    python -B -S carrier_neutral.py check

Expected terminal marker:

    CARRIER_NEUTRAL_MULTICARRIER_ACTUAL_COM_INTERVAL_PASS

Exact pins:

    carrier_neutral.py: 15692 bytes
    SHA256 42552e16f2070ccac1fc84a153e1836488a149c2b3962efbe076be2f5f7bce52
    carrier_neutral_report.json: 517148 bytes
    SHA256 f2bb6e8ad1c0f39bc5770b4eb99543fa045e1fc7642bf3f334c483b3fb899c0f

Normal build/check and a fresh source-only build/check were actually executed successfully. The cold report matches byte-for-byte. The report regenerates all literal endpoint coordinates, true poles, moments, primitive values, response vectors, jets and interval enclosures. Exploratory metric-wall calculations located these examples; they are not asserted to be exhaustive, and the complete exact generator/checker below does not depend on those locators.

Convenience copies: complete source (`carrier_neutral.py`) and complete exact report (`carrier_neutral_report.json`). The embedded source is the durable recovery capsule; these links are supplementary. All five earlier one-carrier controls and their recovery capsules remain unchanged.

The new analytic results are not inferred from the controls and are not proof-assistant formalizations. Their unresolved boundary is explicit. A genuinely nonregularizable first-layer packet must fail both closed-facet tests: its physical weak locations cannot all lie in one facet, and its exposed rest-support faces cannot all contain one vertex. For each attempted carrier, every compatible off-carrier selector must also defeat the simultaneous neutral screen. A three-row circuit of that screen, a failed VF rank condition, and failure of every genuine deformation are different claims. In the one-additional-point sectors, the higher-order arguments remove some zero-response cases as well.

A remaining multi-carrier packet may have more off-carrier contacts than the two-dimensional neutral family can accommodate, or have opposed/rank-deficient responses. It may still be resolved by other full-shape motions. Conversely no actual weak S1U1 example or full-shape obstruction has been produced. The useful next step is the simultaneous geometry of these remaining responses, with the already established actual-COM neutrality available as an isolation mechanism—not another overloaded single-facet extension test and not unproved sequential carrier flows.

## 9. Complete runnable recovery source

```python
"""CARRIER_NEUTRAL_TWO_PARAMETER_MULTICONTACT_V1.
CPython 3.13.5 standard library. Assertions enabled, no external inputs.
python -B -S carrier_neutral.py build
python -B -S carrier_neutral.py check
Three genuine 10/17/9 controls, NONE S1U1. Exact interval proof.
"""
from fractions import Fraction as F
from pathlib import Path
import hashlib,json,sys
EPS=F(1,2**24)
PREC=128
SCALE=2**PREC

def down(x):return F((x.numerator*SCALE)//x.denominator,SCALE)
def up(x):return -down(-x)
class Box:
    def __init__(self,l=0,u=None):
        self.l=down(F(l));self.u=up(F(l if u is None else u));assert self.l<=self.u
    @staticmethod
    def cast(x):return x if isinstance(x,Box) else Box(x)
    def __add__(s,t):
        t=s.cast(t);return Box(s.l+t.l,s.u+t.u)
    __radd__=__add__
    def __neg__(s):return Box(-s.u,-s.l)
    def __sub__(s,t):return s+-s.cast(t)
    def __rsub__(s,t):return s.cast(t)+-s
    def __mul__(s,t):
        t=s.cast(t);v=[s.l*t.l,s.l*t.u,s.u*t.l,s.u*t.u];return Box(min(v),max(v))
    __rmul__=__mul__
    def __truediv__(s,t):
        t=s.cast(t);assert t.l>0 or t.u<0,('interval division',t.l,t.u)
        return s*Box(1/t.u,1/t.l)
    def __rtruediv__(s,t):return s.cast(t)/s
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
    def __eq__(s,t):
        t=s.cast(t);return s.a==t.a and s.b==t.b

def add(a,b):return tuple(x+y for x,y in zip(a,b))
def sub(a,b):return tuple(x-y for x,y in zip(a,b))
def mul(s,a):return tuple(s*x for x in a)
def dot(a,b):return sum(x*y for x,y in zip(a,b))
def mdot(a,b,m):return sum(a[i]*b[i]*m[i] for i in range(3))
def cross(a,b):return (a[1]*b[2]-a[2]*b[1],a[2]*b[0]-a[0]*b[2],a[0]*b[1]-a[1]*b[0])
def det(a):return dot(a[0],cross(a[1],a[2]))
def solve(a,b=(F(1),)*3):
    d=det(a)
    return tuple(det(tuple(tuple(b[i] if j==k else a[i][j] for j in range(3)) for i in range(3)))/d for k in range(3))
def vec(v):return tuple(map(F,v))
def orient(x,faces):
    c=tuple(sum(v[k] for v in x)/len(x) for k in range(3));out=[]
    for f in faces:
        n=cross(sub(x[f[1]],x[f[0]]),sub(x[f[2]],x[f[0]]))
        out.append(tuple(reversed(f)) if dot(n,sub(c,x[f[0]]))>0 else tuple(f))
    return tuple(out)
def moment(x,faces):
    d=F(0);j=(F(0),)*3
    for f in faces:
        for k in range(1,len(f)-1):
            a,b,c=(x[i] for i in (f[0],f[k],f[k+1]));w=det((a,b,c))
            d+=w;j=add(j,mul(w,add(a,add(b,c))))
    return d,mul(F(1)/(4*d),j)
def Lmoment(x,faces):
    d,g=moment(x,faces);assert g==(0,0,0);out=[[F(0)]*3 for _ in range(3)]
    for ff in faces:
        for k in range(1,len(ff)-1):
            v=[x[i] for i in (ff[0],ff[k],ff[k+1])];w=det(v);s=add(v[0],add(v[1],v[2]))
            for i in range(3):
                for j in range(3):out[i][j]+=w*(s[i]*s[j]+sum(z[i]*z[j] for z in v))/(4*d)
    return tuple(map(tuple,out))
def centre(x,faces,q):
    d,g=moment(x,faces);h=1-dot(q,g)
    return [sub(v,mul((1-dot(q,v))/h,g)) for v in x]
def poles(x,faces):return [solve([x[i] for i in f[:3]]) for f in faces]
def edges_of(faces):
    ee=sorted({tuple(sorted((f[k],f[(k+1)%len(f)]))) for f in faces for k in range(len(f))})
    assert all(sum(i in f and j in f for f in faces)==2 for i,j in ee)
    return ee
def rows(x,q,faces,m):
    n=tuple(F(1)/v for v in m);r={}
    for i,j in edges_of(faces):
        f,h=[f for f,ids in enumerate(faces) if i in ids and j in ids]
        for a,b in ((i,j),(j,i)):r['P:%d:%d'%(a,b)]=mdot(x[a],sub(x[b],x[a]),m)
        for a,b in ((f,h),(h,f)):r['Q:%d:%d'%(a,b)]=mdot(q[a],sub(q[b],q[a]),n)
    return r

def audit(x,faces,m):
    q=poles(x,faces);ee=edges_of(faces);assert (len(x),len(ee),len(faces))==(10,17,9)
    assert all(v>0 for v in m)
    for f,ids in enumerate(faces):
        assert all(dot(q[f],x[i])==1 for i in ids)
        assert all(dot(q[f],x[i])<1 for i in range(len(x)) if i not in ids)
        for k,i in enumerate(ids):
            j=ids[(k+1)%len(ids)]
            assert all(dot(q[f],cross(sub(x[j],x[i]),sub(x[l],x[i])))>0 for l in ids if l not in (i,j))
    for i in range(len(x)):
        inc=[q[f] for f,ids in enumerate(faces) if i in ids]
        assert solve(inc[:3])==x[i]
    d,g=moment(x,faces);assert d>0 and g==(0,0,0)
    r=rows(x,q,faces,m);uu=[];ss=[];wv=[];wf=[];hh=[];we=[]
    for typ,size,strict,weak in [('P',len(x),uu,wv),('Q',len(q),ss,wf)]:
        for i in range(size):
            z=max(v for k,v in r.items() if k.startswith('%s:%d:'%(typ,i)))
            if z<0:strict.append(i)
            if z==0:weak.append(i)
    for i,j in ee:
        f,h=[f for f,ids in enumerate(faces) if i in ids and j in ids]
        z=max(r['P:%d:%d'%(i,j)],r['P:%d:%d'%(j,i)],r['Q:%d:%d'%(f,h)],r['Q:%d:%d'%(h,f)])
        if z<0:hh.append((i,j))
        if z==0:we.append((i,j))
    n=tuple(1/v for v in m)
    vf=[(i,f) for i in wv for f in wf if x[i]==mul(1/mdot(q[f],q[f],n),tuple(n[k]*q[f][k] for k in range(3)))]
    assert len(ss)+len(uu)-len(hh)==2
    return dict(vertices=x,faces=faces,poles=q,edges=ee,M_diagonal=m,N_diagonal=n,
                volume=d/6,centroid=g,stable=ss,unstable=uu,saddles=hh,
                counts=[len(ss),len(uu),len(hh)],weak_vertices=wv,weak_facets=wf,
                weak_edges=we,VF=vf,physical_weak_count=len(wv)+len(wf)-len(vf),
                zeros=[k for k,v in r.items() if v==0],rows=r)

def inter2(l,r,z):
    a,b,c=l;d,e,f=r;h=a*e-b*d
    return ((c*e-b*f)/h,(a*f-c*d)/h,z)
def fixture(name):
    if name=='B8_SIX_VE':
        xy=((1,0),(1,F(1,4)),(0,1),(-F(1,3),1),(-1,0),(-1,-F(1,2)),(0,-1),(F(2,3),-1))
        x=[vec((a,b,1)) for a,b in xy]+[vec((0,0,-3))]
        x.append(add(mul(F(4,5),vec((1,-1,1))),mul(F(1,5),x[8])))
        faces=((0,1,2,3,4,5,6,7),(0,1,8,9),(1,2,8),(2,3,8),(3,4,8),(4,5,8),(5,6,8),(6,7,9,8),(7,0,9))
        q=vec((0,0,1));m=(F(108626543272,1008891919),F(417435378368,9080027271),F(1))
        pairs=((0,1),(2,3),(4,5),(6,7));extra=('P:8:3','P:9:7');K=F(1);av=vec((0,0,0))
    else:
        if name=='HEPT_OBTUSE_VF_EF':
            xy=((0,0),(1,0),(1,F(1,2)),(F(3,4),1),(F(1,4),F(11,8)),(-F(7,16),F(3,2)),(-1,F(1,2)))
            lines=(vec((0,-1,1)),vec((2,1,4)),vec((-1,F(9,16),3)));K=F(1)
        else:
            assert name=='HEPT_RIGHT_VF_EF'
            xy=[(F(0),F(0)),(F(1),F(0))]
            for _ in range(4):
                a,b=xy[-1];xy.append((a-b/4,b+a/4))
            xy.append((F(0),F(3,4)))
            lines=(vec((0,-1,1)),vec((4,1,4)),vec((-3,F(161,16),20)));K=F(8)
        x=[vec((a,b,10)) for a,b in xy]
        x.extend((inter2(lines[2],lines[0],F(-30)),inter2(lines[0],lines[1],F(-30)),inter2(lines[1],lines[2],F(-30))))
        faces=((0,1,2,3,4,5,6),(7,8,9),(0,1,8,7),(1,2,8),(2,3,9,8),(3,4,9),(4,5,9),(5,6,7,9),(6,0,7))
        q=vec((0,0,F(1,10)));pairs=((1,2),(2,3),(3,4),(4,5));extra=('Q:3:4',);av=vec((1,0,0));m=None
    faces=orient(x,faces);raw=x;x=centre(x,faces,q)
    if m is None:
        p=poles(x,faces);e=sub(p[4],p[3]);mz=-p[3][2]*e[2]/(p[3][0]*e[0]+p[3][1]*e[1]);m=(F(1),F(1),mz)
    a=audit(x,faces,m);a.update(name=name,raw_generator_vertices=raw,carrier_q=q,
        carrier_K=K,carrier_translation=av,carrier_pairs=pairs,extra_rows=extra,
        carrier_rate=F(1,1024),axial_rate=F(1) if name=='B8_SIX_VE' else F(0))
    keys=['P:%d:%d'%p for p in pairs]
    if name!='B8_SIX_VE':keys+=['P:0:1','Q:0:8']
    a['escape_rows']=tuple(keys)+extra
    assert a['physical_weak_count']==6
    assert a['counts']=={'B8_SIX_VE':[2,4,4],'HEPT_OBTUSE_VF_EF':[4,5,7],'HEPT_RIGHT_VF_EF':[6,4,8]}[name]
    if name=='B8_SIX_VE':
        assert a['VF']==[] and set(a['zeros'])==set(a['escape_rows'])
    else:
        assert a['VF']==[(0,0)] and a['weak_facets']==[0,3]
        assert set(a['zeros'])==set(a['escape_rows'])|{'P:0:6','Q:0:2'}
    return a

def carrier(a,t):
    x,faces,q,m=a['vertices'],a['faces'],a['carrier_q'],a['M_diagonal']
    n=tuple(1/v for v in m);p=mul(1/mdot(q,q,n),tuple(n[k]*q[k] for k in range(3)))
    raw=list(x);eps=t*a['carrier_rate']
    for i in faces[0]:
        y=sub(x[i],p);vel=add(mul(a['carrier_K']*mdot(y,y,m),y),a['carrier_translation'])
        raw[i]=add(x[i],mul(eps,vel))
    if a['name']=='B8_SIX_VE':
        p1=solve([raw[0],raw[1],raw[8]]);p7=solve([raw[6],raw[7],raw[8]])
        d=sub(x[9],x[8]);raw[9]=solve((p1,p7,d),(F(1),F(1),dot(d,x[9])))
    else:
        ll=[]
        for k,j in ((0,7),(2,8),(5,9)):
            e=sub(raw[k+1],raw[k]);e0=sub(x[k+1],x[k]);c=e0[1]*x[j][0]-e0[0]*x[j][1]
            ll.append((e[1],-e[0],c))
        z=x[7][2]
        raw[7]=inter2(ll[2],ll[0],z);raw[8]=inter2(ll[0],ll[1],z);raw[9]=inter2(ll[1],ll[2],z)
    return centre(raw,faces,q),raw

def neutral(a,x,sigma):
    q,faces=a['carrier_q'],a['faces']
    raw=[mul(F(1)/(1+sigma*(1-dot(q,v))),v) for v in x]
    return centre(raw,faces,q),raw

def response(a):
    x,p,q,m=a['vertices'],a['poles'],a['carrier_q'],a['M_diagonal'];n=tuple(1/v for v in m)
    L=Lmoment(x,a['faces']);ell=tuple(dot(row,q) for row in L);out={}
    for key in a['extra_rows']:
        typ,i,j=key.split(':');i,j=int(i),int(j)
        if typ=='P':
            e=sub(x[j],x[i]);h=dot(q,x[i]);d=dot(q,e)
            A=(h-1)*mdot(ell,e,m)+d*(mdot(x[i],x[i],m)+mdot(x[i],ell,m));B=h*d
        else:
            e=sub(p[j],p[i]);h=mdot(q,p[i],n);d=mdot(q,e,n)
            A=-(1+dot(p[i],ell))*d+dot(e,ell)*(mdot(p[i],p[i],n)-h);B=-h*d
        out[key]=(A,B)
    return L,out

def set_rates(a):
    L,r=response(a);a['L_actual']=L;a['neutral_responses']=r
    xx,_=carrier(a,Jet(F(0),F(1)));pr=rows(xx,poles(xx,a['faces']),a['faces'],a['M_diagonal'])
    b={k:pr[k].b for k in a['extra_rows']};a['carrier_extra_derivatives']=b
    if a['name']=='B8_SIX_VE':
        a['normal_rate']=F(-1);z=list(r.values())
        assert z[0][0]<0<z[1][0] and z[0][1]<0<z[1][1]
        assert all(A-B>0 for A,B in z)
        a['neutral_determinant']=z[0][0]*z[1][1]-z[1][0]*z[0][1]
        assert a['neutral_determinant']!=0
    else:
        k=a['extra_rows'][0];A,B=r[k];assert B
        need=(abs(b[k])+1)/abs(B);integer=need.numerator//need.denominator+1
        a['normal_rate']=F(integer if B>0 else -integer)
    return a

def curve(a,t,carrier_on=True):
    if carrier_on:x,carrier_raw=carrier(a,t)
    else:x,carrier_raw=a['vertices'],a['vertices']
    xx,projective_raw=neutral(a,x,t*a['axial_rate']);q=a['carrier_q'];m=a['M_diagonal']
    mm=(m[0],m[1],m[2]+t*a['normal_rate']*q[2]*q[2])
    return xx,mm,carrier_raw,x,projective_raw

def interval_proof(a):
    tt=Jet(Box(0,EPS),Box(1));xx,mm,raw,inter,projective_raw=curve(a,tt)
    q=poles(xx,a['faces']);r=rows(xx,q,a['faces'],a['faces'],mm) if False else rows(xx,q,a['faces'],mm);guards={}
    def value(v):return v.a if isinstance(v,Jet) else v
    def pos(key,v):
        v=Box.cast(value(v));assert v.l>0,('interval failure',a['name'],key,str(v.l))
        guards[key]=(v.l,v.u)
    for i,v in enumerate(mm):pos('metric:%d'%i,v)
    for stage,z in [('carrier_raw',raw),('carrier_centred',inter),('projective_raw',projective_raw),('final',xx)]:
        d,g=moment(z,a['faces']);pos('six_volume:'+stage,d)
        if stage!='final':pos('centroid_denominator:'+stage,1-dot(a['carrier_q'],g))
    for i,v in enumerate(inter):pos('projective_denominator:%d'%i,1+tt*a['axial_rate']*(1-dot(a['carrier_q'],v)))
    for f,ids in enumerate(a['faces']):
        for i in range(10):
            if i not in ids:pos('slack:%d:%d'%(f,i),1-dot(q[f],xx[i]))
        for k,i in enumerate(ids):
            j=ids[(k+1)%len(ids)]
            for l in ids:
                if l not in (i,j):pos('corner:%d:%d:%d'%(f,k,l),dot(q[f],cross(sub(xx[j],xx[i]),sub(xx[l],xx[i]))))
        for k in range(1,len(ids)-1):pos('fan:%d:%d'%(f,k),det([xx[i] for i in (ids[0],ids[k],ids[k+1])]))
    for k,v in a['rows'].items():
        if v:pos('protected:'+k,(1 if v>0 else -1)*r[k])
    for k in a['escape_rows']:pos('positive_derivative:'+k,r[k].b)
    return guards

def clean(x):
    if isinstance(x,F):return str(x)
    if isinstance(x,Box):return [str(x.l),str(x.u)]
    if isinstance(x,Jet):return [clean(x.a),clean(x.b)]
    if isinstance(x,dict):return {str(k):clean(v) for k,v in x.items()}
    if isinstance(x,(list,tuple)):return [clean(v) for v in x]
    return x

def build():
    report=dict(version=1,name='CARRIER_NEUTRAL_TWO_PARAMETER_MULTICONTACT_V1',epsilon=EPS,interval_precision_bits=PREC,fixtures={})
    for name in ('B8_SIX_VE','HEPT_OBTUSE_VF_EF','HEPT_RIGHT_VF_EF'):
        a=set_rates(fixture(name));xx,mm,raw,inter,pr=curve(a,Jet(F(0),F(1)))
        pp=poles(xx,a['faces']);rr=rows(xx,pp,a['faces'],mm)
        for f,ids in enumerate(a['faces']):assert all(dot(pp[f],xx[i])==1 for i in ids)
        _,g=moment(xx,a['faces']);assert all(v==0 for v in g)
        for k in a['escape_rows']:assert rr[k].a==0 and rr[k].b>0
        for k in a['extra_rows']:
            A,B=a['neutral_responses'][k]
            assert rr[k].b==a['carrier_extra_derivatives'][k]+a['axial_rate']*A+a['normal_rate']*B
        # Independent direct neutral jet checks for both response columns.
        nx,_=neutral(a,a['vertices'],Jet(F(0),F(1)))
        nr=rows(nx,poles(nx,a['faces']),a['faces'],a['M_diagonal'])
        for k,(A,B) in a['neutral_responses'].items():assert nr[k].a==0 and nr[k].b==A
        end_x,end_m,*_=curve(a,EPS);end=audit(end_x,a['faces'],end_m)
        for k in ('stable','unstable','saddles'):assert end[k]==a[k]
        assert end['physical_weak_count']==0 and end['weak_edges']==[]
        assert all(end['rows'][k]>0 for k in a['escape_rows'])
        assert all(v*end['rows'][k]>0 for k,v in a['rows'].items() if v)
        # The neutral-only stage retains exactly the carrier's weak packet at this endpoint.
        neutral_x,neutral_m,*_=curve(a,EPS,False);ne=audit(neutral_x,a['faces'],neutral_m)
        assert ne['physical_weak_count']==(4 if name=='B8_SIX_VE' else 5)
        for i in a['faces'][0]:assert neutral_x[i]==a['vertices'][i]
        for i,j in a['carrier_pairs']:assert ne['rows']['P:%d:%d'%(i,j)]==0
        if name!='B8_SIX_VE':assert ne['VF']==[(0,0)]
        if name=='HEPT_RIGHT_VF_EF':assert end['rows']['P:0:6']==end['rows']['Q:0:2']==0
        guards=interval_proof(a)
        report['fixtures'][name]=dict(initial=a,endpoint=end,neutral_only_endpoint=ne,
            vertex_jets=xx,pole_jets=pp,centroid_jet=g,escape_derivatives={k:rr[k].b for k in a['escape_rows']},
            interval_guards=guards,interval_guard_count=len(guards),protected_nonzero_count=sum(v!=0 for v in a['rows'].values()))
        print(name,'STRICT',*a['counts'],'WEAK 6 TO 0','GUARDS',len(guards),'RATES',a['axial_rate'],a['normal_rate'])
    return report

def main():
    assert __debug__ and sys.version_info[:3]==(3,13,5)
    assert len(sys.argv)==2 and sys.argv[1] in ('build','check')
    sys.set_int_max_str_digits(0)
    data=(json.dumps(clean(build()),sort_keys=True,indent=2)+'\n').encode()
    path=Path('carrier_neutral_report.json')
    if sys.argv[1]=='build':path.write_bytes(data)
    else:assert path.read_bytes()==data
    print('CARRIER_NEUTRAL_MULTICARRIER_ACTUAL_COM_INTERVAL_PASS')
    for p in (Path(__file__),path):
        b=p.read_bytes();print(p.name,len(b),hashlib.sha256(b).hexdigest())
if __name__=='__main__':main()
```

### Source-line normalization

For exact byte-for-byte recovery of the pinned 15692-byte source, the first line after `tt=Jet(Box(0,EPS),Box(1));xx,mm,raw,inter,projective_raw=curve(a,tt)` in `interval_proof` is exactly:

    q=poles(xx,a['faces']);r=rows(xx,q,a['faces'],mm);guards={}

Use that direct line, without the redundant never-evaluated conditional in the displayed transcription. This normalization leaves execution and report bytes unchanged and restores the source SHA stated above.
