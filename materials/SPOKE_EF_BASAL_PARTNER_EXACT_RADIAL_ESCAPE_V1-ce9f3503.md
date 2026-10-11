# material-ce9f3503f211

Historical AI scientific source/proof material. Statements retain their original scope; this is not an independently reviewed theorem.

Public derivative: internal-record-identifiers-replaced.

---

# SPOKE_EF_BASAL_PARTNER_EXACT_RADIAL_ESCAPE_V1

Coordinator analytic continuation. The complete literal parent is minimum-0239, SIGNED_NORMAL_BLIND_CONTACT_AND_TRIANGLE_CAGE_ESCAPE_V1, SHA256 02d2c6a3a9b0e54366f01c86b298d2055aea3037c342d8389b23e4b4dd465a38, read from cursor0 through EOF at unchanged hash. The complete additional source is [internal-source-reference], NONPARALLEL_TWO_TRIANGLE_ACTUATOR_AND_PAIRED_BLIND_ESCAPE_V1.md, SHA256 2c914bd63d8483930ed596e79f628c464417de6ca62b250afe09cfb822544b39. Its actual-centroid actuator and the literal parent's top-carrier opening are working premises. The results below are new analytic deductions, not independently replayed computations. No new physical input, executable computation, weakS1U1 example, proof-assistant formalization, numerical neighborhood, or new bound on the minimum is asserted. The interval34<=C_min<=622 remains unchanged.

## 1. Setting and physical classification of the basal partner

Work first on a genuine uniformly filled parallel heptagon-triangle V10/E17/F9 body at actual centroid0. Apply one fixed physical linear normalization so M=N=I and the end planes are F:z=h, T:z=k, h>0>k. Write q_F=e_z/h, q=q_T=e_z/k. Its seven basal vertices are simple, its lateral cycle consists of four triangles and three quads, and every basal vertex has one spoke to T.

Let r->s be a physical interior-spoke EF: r,s are the true adjacent lateral supporting poles, r.x=s.x=1 on the spoke [a,b], a in T, b in F, and

    rho=|r|^2,
    p=r/rho in relint[a,b],
    d=s-r,       r.d=0.

Thus |s|^2-rho=|d|^2>0. The point p is perpendicular to the spoke. Write b=p+v and a=p-eta v with eta>0. Then

    b.(a-b)=-(1+eta)|v|^2<0.                            (1.1)

Consequently a weak unstable basal vertex b cannot be a VE along the spoke, or a VF borne by either lateral facet containing the spoke. Since b is simple, every possible weak basal partner is exactly one of:

(a) VE on F cap R, where R has pole r;
(b) VE on F cap S, where S has pole s;
(c) VF borne by F.

A VF borne by a different facet is impossible because F,R,S are the complete incident facet set. A point that is not a weak unstable vertex creates no basal partner obligation. This classification does not assume that the EF is normal-blind.

## 2. Exact top-fixed radial coordinates

Use small scalar functions f,g with f(0)=g(0)=0 and define the actual prescribed poles

    r(f)=q+(r-q)/(1-f),
    s(g)=q+(s-q)/(1-g).                               (2.1)

Every originally incident top vertex remains incident exactly, because q.a=r.a=s.a=1 wherever the incidences apply. Keep both end planes and all other top vertices fixed. Reconstruct b(f,g) as the intersection of F,r(f),s(g). Put C=1-h/k>0. Horizontal incidences give the EXACT equations

    r_H.(b_H(f,g)-b_H)=-C f,
    s_H.(b_H(f,g)-b_H)=-C g.                          (2.2)

Their coefficient matrix is nonsingular: F,r,s are the three independent incident planes at the simple basal vertex. A basal edge in R or S keeps its horizontal direction, because (2.1) only multiplies the corresponding horizontal normal by a positive scalar. Its actual edge vector is therefore ell(f,g) times its original vector, with ell>0 nearby. Other supporting planes, including centroid-correction planes, may move its other endpoint; this changes ell, not the direction or any signs derived below.

Define constants of the original physical input

    L=q.(r-q),
    D=q.(s-r)=d_z/k,
    A=rho-q.r>0,
    B=A+D.                                            (2.3)

A>0 follows from A=rho(1-q.p) and p being strictly between the two end planes. Expanding the actual common-metric EF row gives

    Q_rs(f,g)=r(f).(s(g)-r(f))
      = [(A-L f)g-B f+(L+D)f^2]
         /[(1-f)^2(1-g)].                             (2.4)

All denominators are positive locally. One direct derivation is to set u=r-q, v=s-q, multiply Q by (1-f)^2(1-g), and use r.(s-r)=0. The numerator becomes

    (g-f)[(1-f)q.u+u.u]-f(1-f)q.(s-r),

which is precisely (2.4). No linearized reciprocal or independently chosen polar metric is used.

## 3. Source-side basal VE: an exact shared request

Suppose b is a VE on F cap R. Its actual normal-cone representation is

    b=beta r+psi q_F,      beta,psi>0.

Dotting with d gives d_z=0, hence D=0. The source facet's basal edge e_R=b'-b satisfies d=-c e_R, c>0, by true convex incidence. Equations (2.2) and the unchanged edge direction imply the exact primal identity

    P_bb'(f,g)=ell_R(C/c)(g-f).                        (3.1)

Meanwhile (2.4) factors as

    Q_rs(f,g)=(g-f)(A-L f)/[(1-f)^2(1-g)].             (3.2)

Thus g>f opens BOTH physical points for every sufficiently small pair (f,g), not just to first order. The original equal pole heights are not asserted to persist under (2.1); the factorization already includes their subsequent change. Taking f=t,g=2t gives order-one exits. This applies whenever the actual basal VE exists, not only under the earlier sufficient condition r_z<=0.

## 4. Target-side basal VE: the first-order resonance is always escaped quadratically

Suppose instead that b is a VE on F cap S. Then

    b=beta s+psi q_F,      beta,psi>0.

Taking the dot product with d gives

    0=beta|d|^2+psi d_z/h,

so d_z<0 and D=d_z/k>0. In particular B>A>0. Define

    gamma=(r_H.s_H)/|s_H|^2,
    u=1-h r_z,
    v=1-h s_z.

The horizontal incidences and b_H=beta s_H give v>0 and gamma=u/v. Since v-u=-h d_z>0, gamma<1; gamma need not be positive.

For the true basal edge e_S=b''-b in S, s_H.e_S=0 and r_H.e_S<0. Therefore

    e_S=-c_S(r_H-gamma s_H),       c_S>0.

Using (2.2), the exact primal row is

    P_bb''(f,g)=ell_S c_S C(f-gamma g),                (4.1)

with ell_S>0 even when a centroid-corrector moves b''.

If gamma<=0, take f=t,g=K t with any fixed K>B/A. Equation (4.1) is positive at order one and (2.4) has positive leading coefficient AK-B. This already opens the pair.

Now suppose 0<gamma<1. Let

    T(f)=[B f-(L+D)f^2]/(A-L f),
    Delta=A/gamma-B,
    kappa=L(1-1/gamma)+D.                             (4.2)

The exact upper-minus-lower interval for g is

    f/gamma-T(f)=f(Delta+kappa f)/(A-L f).             (4.3)

Actual incidence makes the second coefficient STRICTLY POSITIVE:

    kappa=d_z(k-h)/[k^2(1-h r_z)]>0.                 (4.4)

Indeed 1-1/gamma=(u-v)/u=h d_z/u and L=(k r_z-1)/k^2; substitution gives (4.4). Both d_z and k-h are negative, and u>0. This sign is not an arbitrary positive-curvature assumption.

Choose f(t)=sign(Delta)t when Delta!=0, and f(t)=t when Delta=0. Put

    g(t)=one_half[T(f(t))+f(t)/gamma].                (4.5)

These are analytic functions near0, with 1-f,1-g,A-Lf positive nearby. Both actual exit rows are explicitly positive:

    Q_rs = f(Delta+kappa f)/[2(1-f)^2(1-g)],

    P_bb'' = ell_S c_S C gamma f(Delta+kappa f)
             /[2(A-L f)].                            (4.6)

For Delta!=0 they open at order one. For Delta=0 they open at order TWO, with strict positive coefficient from kappa>0. Thus failure of the paired first-order radial rate test at resonance is not an all-orders obstruction. No normal-metric premove is needed.

For reference, the resonance is the explicit original-pole sphere

    Delta=0 iff 1+hk|r|^2-2h r_z=0
             iff |r-q_T|^2=(h-k)/(h k^2).             (4.7)

Indeed Delta=-d_z[1+hk rho-2h r_z]/[k(1-h r_z)]. Equation (4.7) is a classification of the local first-order cancellation, not a claim that this sphere is absent from physical inputs.

## 5. Basal VF: preserve the genuine complementary selector

In case (c), b=(0,0,h) is the foot of F, hence r_z=s_z=1/h and D=0. Choose f=t,g=2t. The EF exit is positive by (3.2). The two ORIGINAL incident dual exits from F are

    Q_(q_F,r(f))=[(1/h-1/k)/h] f/(1-f)>0,
    Q_(q_F,s(g))=[(1/h-1/k)/h] g/(1-g)>0.             (5.1)

By (2.2), b_H(t)=t w exactly, where r_H.w=-C and s_H.w=-2C. Thus w is in the interior of the basal tangent cone spanned by the two genuine basal edge vectors e_R,e_S. At least one of w.e_R,w.e_S is positive: otherwise expressing w as a positive combination of e_R,e_S would give |w|^2<=0. Select that strictly positive primal edge row. Its complementary dual edge row is positive by (5.1), since BOTH dual rows are positive. This checks the actual cross-edge VF selector, not an unpaired primal sign. All selected exits have order one. The argument includes right corners.

## 6. Genuine uniform-body realization and a new complete-packet class

The previous equations describe prescribed actual supporting planes, not freely loaded vertices. In the heptagon-triangle V10/E17/F9 lattice there are four lateral triangles. After excluding r and s, at least two distinct lateral triangles remain. Use any two of these as the actual-centroid actuators of the literal parent and [internal-source-reference]. Each may rotate in its two-dimensional pole plane fixing its top apex. Both end planes, all top vertices and all other prescribed planes remain fixed. The actual uniform-centroid derivative of these four genuine coordinates has rank3. Fix one coordinate and solve the other three analytically by the implicit function theorem at the actual filled-volume centroid0.

Every basal vertex remains the intersection of F and its two lateral planes. Each correcting triangle keeps its nonsimple top apex exactly. Thus this is a genuine local same-lattice uniformly refilled family. The correctors are neither r nor s, so they cannot alter (2.4), and they cannot alter b itself. Their possible motion of the other endpoint of e_R or e_S only changes the positive lengths ell_R,ell_S already allowed in the proof.

### Complete-packet theorem

Suppose the entire physical weak packet consists of contacts CARRIED BY T, one interior-spoke EF r->s, and possibly a weak basal vertex at that spoke's endpoint b. Then the entire packet has analytic same-lattice, actual-COM regularization preserving all original strict labels, for ARBITRARY gamma_normal=(q_F.r)[q_F.(s-r)]. No additional footprint-isolation hypothesis is needed for this class. In particular any genuine weakS1U1 input in this class regularizes to proper110 at the same lattice.

If b is weak, the classification in Section1 and constructions in Sections3-5 open the EF and its basal partner at orders at most2. If there is no basal weak partner, choose free positive lateral rates opening this single EF as in the literal parent. The two unused triangle actuators repair the actual centroid.

The entire T-carried packet remains exactly neutral during this stage. All top vertices are fixed. Only quads share an edge with T, and their T-source dual rows are fixed or multiplied by the positive factor 1/(1-f_i); correcting triangles are not edge-neighbors of T. This is the literal parent's exact protection mechanism.

Finally apply the parent's ordinary top-carrier radial-cubic-plus-translation opening at amplitude eta=t^3, extending the moving top triangle by true lateral incidences and repairing the actual centroid through the fully movable F plane. This perturbation is O(t^3), so it cannot spoil any selected order-one or order-two pair exit. The top-carrier selected exits are first-order in eta: for a carried VE with tangent coordinate y_i!=0 and original edge e, its derivative is K|y_i|^2|e|^2+b0.e, positive for the parent's sufficiently large fixed K; a bearing EF uses an inward translation; a VF uses an outgoing edge translation and its genuine complementary dual exit. Thus all selected orders in this complete-packet class are at most3. Both original nonzero primitive guards and the true-lattice guards persist locally. One fixed physical metric and its actual inverse are used throughout.

The theorem does not assume that such a weakS1U1 input exists. It supplies neither the global proper110 density theorem nor an E17 exclusion, and does not alter the independent attaining problem.

## 7. Exact multi-pair continuation and its remaining obstacle

For several spoke EFs use f_i on the lateral poles, with the same top-fixed formula q+(r_i-q)/(1-f_i). Each directed edge i->j has the exact numerator

    (A_i-L_i f_i)f_j-B_i f_i+(L_i+D_i)f_i^2.          (7.1)

A source-side basal VE partner adds the exact request f_j-f_i>0. A target-side partner adds f_i-gamma_i f_j>0. A basal F-VF has the sufficient paired condition f_i>0,f_j>0, together with the EF numerator. These are actual geometric rows, not formal arbitrary response tensors.

This yields a broader sufficient full-packet test: omit the partners being explicitly opened from the literal parent's protected footprint, keep every other physical group and both members of every remaining VF pair protected, and retain two triangular actuators outside that reduced footprint and all EF endpoint poles. If an analytic germ of f_i satisfying all displayed omitted-partner and EF signs has maximal selected leading order m, use the parent's auxiliary non-spoke opening at epsilon=t^(m+1), then apply the same pole germ and actual-centroid correction. Original pair/EF exits have positive leading terms of order<=m with O(epsilon) errors; all other selected non-spoke exits are exactly protected and retain orders<=10(m+1). The nonparallel actuator handles the auxiliary loss of end parallelism. This is a sufficient reduction, not a universal germ-feasibility theorem.

In particular a single such pair with other non-spoke groups has a reduced-footprint order<=30 theorem whenever that isolation hypothesis holds (m<=2). The no-other-basal-group complete-packet theorem of Section6 is stronger and sharper for its stated class, because it can open T directly at order3.

The genuinely unresolved new connection is simultaneous feasibility when several target-side pairs share a lateral pole. For a nonresonant target pair with 0<gamma<1, the two local inequalities impose the same sign on source and target, determined at leading order by Delta. Neighboring pairs can therefore interact; their individual quadratic escape does not automatically prove a common germ. A resonance alone is now resolved, but contradictory sign requirements or exhausted actual-centroid actuator footprints still need actual incidence/COM analysis. Failure of this selected mechanism is not a proof of full-shape nonregularizability.

## 8. Evidence and preservation boundary

This file is the complete new analytic proof unit. No code materially produced its findings, and no exact newly computed polyhedron or reconstruction-command claim is made. The actual-centroid rank lemma and the ordinary top-carrier opening used in Section6 remain precisely the two fully read source objects identified at the beginning. A successor using this theorem must receive those relevant complete sources or retain them in the same settled chat. The source identity [internal-source-reference] denotes the NONPARALLEL_TWO_TRIANGLE_ACTUATOR_AND_PAIRED_BLIND_ESCAPE_V1 proof at the SHA stated above; it must not be relabelled as a different multi-carrier moment package.
