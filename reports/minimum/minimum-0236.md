# minimum-0236

AI research report · 2026-09-25 UTC · [Export notes](../../catalog/coverage.md#text-records)

---

# PARALLEL_HEPTAGON_TRIANGLE_FULL_PACKET_ESCAPE_V1

Slot-5, Bright Harbor 33. Branch `[internal-source-reference]`.

## 1. Main result

**Every actual uniformly filled V10/E17/F9 body whose vertices lie on two parallel true facets, one a heptagon and the other a triangle, admits same-lattice regularization of its entire weak packet whenever no physical EF lies in the interior of an edge joining the two facets.** There is no restriction on the number or distribution of its VE and VF points, and no rank, genericity, covariance-symmetry or nonzero-centroid-response hypothesis.

In particular this closes **all pure VE/VF packets in the parallel heptagon–triangle class**, not merely packets carried by one facet. EF points on the boundary edges of either end facet are also permitted, including those borne by a lateral facet.

There is a further enlargement. Write q for the actual pole of the heptagonal facet, M for the physical metric and N=M^-1. At a weak EF in a joining edge, let r be its bearing-facet pole and s the other incident facet pole. Define

    gamma_EF = (q^T N r) [q^T N(s-r)].                    (1.1)

The conclusion still holds when joining-edge EF points occur, provided **gamma_EF>0 at every one of them**. This is a geometric condition on the actual common inverse metric. It is not an independently selectable response tensor.

The proof constructs one analytic curve. A common negative-normal metric motion first opens all permitted contacts not carried by the two end facets. The two genuine top-plane tilt freedoms then resolve the complete triangle-carried packet. A later heptagon-opening motion is protected by exact fixed-heptagon neutrality. Singular first-response matrices are bypassed by an explicit contact-preserving metric premove, not assumed nonsingular. All selected physical exits can be made positive with leading orders at most **ten** in the resulting parameter.

For a weak-inclusive S1U1 input in this class, the curve gives arbitrarily close proper110 bodies of the same lattice. No actual S1U1 input is asserted, and no lower or upper complexity bound changes. The accepted internal interval remains 34<=C_min<=622. fileciteturn16file1L9-L13

### Target-class structural consequence

A genuinely nonregularizable weak S1U1 body in the parallel heptagon–triangle class must therefore possess a physical EF in the interior of a joining edge with

    gamma_EF <= 0.                                       (1.2)

This is a necessary remaining contact mechanism, **not a sufficient obstruction**. The theorem does not cover all heptagonal E17 incidences, nonparallel end facets, or every packet satisfying (1.2).

## 2. Authority and research approach

The entire updated journal, including the complete literal parent, and the supplied octagon V2 material were read. Their mounted-byte checks match:

    research-journal.md: 343436 bytes
    SHA256 514090bd16b77aad2bbb86de20ec80f2963a627272161ac87e6294de1166c623

    OCTAGON_NEUTRAL_SHARP_GERMS_V2.md: 11454 bytes
    SHA256 2b7ece164c049acfbda00688770a77c8446c9c915b624196818c9b7fd1e5e1be

The direct immutable parent is `minimum-0234`, SHA256 `147eb971dd88329f6c7420454ae7ece06003d4b0e48e1919078aed8b99542edc`. Its complete fixed-heptagon fibre, actual-centroid correction, exact neutrality and VF pairing are working premises. No new discrepancy with that payload was found. fileciteturn22file0L114-L130

The new step is not another coordinate-access result. I used the two tilt freedoms to study the **complete physical packet on the opposite triangle**. Its contact geometry sharply limits the simultaneous obligations. A normal-metric parameter makes the relevant response matrices polynomial pencils; genuine quad incidence prevents the only potentially persistent two-simple-contact rank defect. VF pairing is handled by its actual corner cone. This supplies a successful higher-order curve even at exceptional metric values where the original first-response test is singular.

No new numerical search, physical control, interval computation or symbolic-computation certificate is claimed in this continuation. The result below is analytic. The unchanged parent controls retain their earlier verification status.

## 3. Precise geometric setting

Let P be genuine, full-dimensional and uniformly filled, with actual volume centroid 0. Suppose its ten vertices lie in the union of two disjoint parallel true facets F and T, with |F|=7 and |T|=3. An edge joining a vertex of F to a vertex of T will be called a **spoke**.

A constant physical linear normalization sends M to I, followed by a rotation. Uniform volume centroids transform affinely under this normalization. We may consequently write

    F: z=h,       T: z=k,       h>0>k,                    (3.1)

and write the three top vertices as X_i=(y_i,k), y_i in R^2. The signs in (3.1) follow from the actual centroid being interior to the body. They are not assumptions about an independently chosen reference.

There are seven F-boundary edges and three T-boundary edges. Every F vertex has at least one spoke, and E=17 leaves exactly seven spokes. Thus every F vertex has exactly one spoke. The three top labels occur in nonempty consecutive blocks around F. Each top edge has one lateral neighbor, necessarily a quadrilateral. The complete boundary consists of

    F, T, three lateral quads, four lateral triangles.    (3.2)

In particular each top vertex is incident to two of the quads. The corresponding two base edges are parallel to its two top edges and hence are not parallel to each other. Their supporting lines meet at a finite point B_i in the plane z=h. The line X_i B_i is the intersection of the two actual quad planes.

These are true face-intersection statements. No integration diagonal is used as an edge. The parent also records this precise heptagon–triangle incidence and the genuine quad-line actuators. fileciteturn23file0L49-L75

### Physical partition of the weak packet

Let C_F and C_T be the packets carried by the end facets in the parent's sense: VEs whose exposed edges belong to that facet, and the EF or VF borne by that facet.

Every other weak point is one of the following:

- a VE on a spoke, at either endpoint;
- a VF at an end vertex but borne by a lateral facet;
- an EF on an end-boundary edge but borne by its lateral facet;
- an EF in a spoke.

This is exhaustive because all vertices lie in F or T and every true edge is either an end-boundary edge or a spoke. A VF is counted once, with its coupled primal and polar exits, not as additional VE and EF points.

## 4. One common metric motion opens all permitted cross contacts

Keep the body fixed and use

    M_lambda=diag(1,1,lambda),
    N_lambda=diag(1,1,1/lambda),
    lambda=1-t,        0<t<1.                             (4.1)

In original coordinates this is exactly

    M(t)=M-t q q^T/s_F,
    N(t)=N+t Nq q^T N/[s_F(1-t)],
    s_F=q^T Nq.                                          (4.2)

Thus there is one SPD metric and its actual inverse throughout. Both end-facet feet and tangent metrics remain fixed. Every zero row of C_F and C_T remains zero under this fixed-body premove, and their other originally nonzero guards persist locally.

### 4.1 VE on a spoke

For an original zero P_ij with a spoke i->j,

    P_ij(t)=-t z_i(z_j-z_i)>0.                            (4.3)

Indeed its source height is either h>0 with target k<0, or k<0 with target h>0. Both directions have the displayed strict sign. All such VEs are opened by the same motion.

### 4.2 EF on an end edge, borne laterally

Let r be its bearing pole, rho=|r|^2, and let the end plane be z=z_0, z_0=h or k. The bearing foot is r/rho and lies in that end edge, so r_z=rho z_0. The neighboring end pole is e_z/z_0. Since the lateral facet is distinct from the end facet,

    r_z(1/z_0-r_z)=rho(1-rho z_0^2)=|r_horizontal|^2>0.

For this original zero dual row, (4.1) therefore gives

    Q(t)=t |r_horizontal|^2/(1-t)>0.                     (4.4)

An EF borne by the end itself belongs instead to C_F or C_T and remains neutral at this stage.

### 4.3 VF borne by a lateral facet

Let v lie in one end facet and let e_1,e_2 be its two outgoing true edges in the bearing lateral facet. Both normal increments point into the slab or are zero; at least one is nonzero. Thus the two primal derivatives under (4.1) satisfy

    p_i=P_i'(0)=-z_v(e_i)_z>=0,
    (p_1,p_2)!=(0,0).                                    (4.5)

Let G be the actual positive-definite corner Gram matrix. At the VF the supplied exact flag identities are

    P=G u,
    Q_1=s delta_1 u_2,     Q_2=s delta_2 u_1,
    s,delta_1,delta_2>0.                                  (4.6)

Since p^T G^-1 p>0, some i has both p_i>0 and (G^-1 p)_i>0. The corresponding **complementary** pair, (P_1,Q_2) or (P_2,Q_1), therefore has two positive first derivatives. This includes a right corner; it does not discard one side of the VF obligation. The identities and their higher-order pairing semantics are retained from the literal parent. fileciteturn23file0L131-L135

### 4.4 EF in a spoke

For an original zero Q_rs, the exact formula in normalized coordinates is

    Q_rs(t)=t r_z(s_z-r_z)/(1-t).                        (4.7)

The sign is precisely the sign of gamma_EF in (1.1). Hence every spoke EF with gamma_EF>0 is opened simultaneously. A gamma_EF=0 point remains identically neutral in this metric motion, and gamma_EF<0 has the wrong sign. Those cases are not included in the theorem.

All permitted cross contacts have now acquired strict selected exits of order one. Later shape changes of order at least three will not destroy them.

## 5. Two genuine tilts with the actual uniform centroid retained

For L in R^2 define a raw deformation, keeping F fixed, by

    Y_i(L)=X_i+[(L.y_i)/(h-k)](B_i-X_i),    i in T.        (5.1)

Each top vertex moves on the intersection line of its two true quad planes. All three quads remain exactly planar and keep their raw planes. Every other moving facet is a triangle. Strict support, noncollinearity and convexity persist for sufficiently small L, so this is a genuine same-lattice deformation.

Compute its actual uniform centroid from the fixed oriented boundary fan:

    D(L)=sum det(Y_a,Y_b,Y_c),
    J(L)=sum det(Y_a,Y_b,Y_c)(Y_a+Y_b+Y_c),
    g(L)=J(L)/(4D(L)).                                   (5.2)

Then apply the physical affine map

    C_g(x)=x-g(1-z/h)/(1-g_z/h).                          (5.3)

It fixes F pointwise and sends the actual uniform centroid exactly to 0. It is locally invertible, so the true face lattice is unchanged. This is the parent's exact actual-volume retraction, not transported old-centroid data. fileciteturn22file0L170-L184

For a direction L, let c(L) be the raw centroid derivative at zero. It is a linear map of L, determined by (5.2). More explicitly, with d_abc=det(X_a,X_b,X_c) and W_i the raw velocities from (5.1),

    d'_abc=det(W_a,X_b,X_c)+det(X_a,W_b,X_c)
            +det(X_a,X_b,W_c),

    c(L)=[sum d'_abc(X_a+X_b+X_c)
          +sum d_abc(W_a+W_b+W_c)]/(4D(0)).              (5.4)

Here J(0)=0 has been used. The summation uses the actual sixteen boundary-fan triangles. No centroid derivative is chosen independently.

Put alpha=1-k/h. The corrected top velocities take the form

    X_i'=(v_i(L), ell_0(L)+L.y_i),
    v_i(L)=W_i,horizontal-alpha c_horizontal(L),
    ell_0(L)=-alpha c_z(L).                              (5.5)

In particular their height differences are exactly L.(y_j-y_i). The actual centroid correction subtracts the **same** horizontal and vertical vector at every top vertex because their initial height is common. This common load is important below.

At fixed M_lambda, the top plane has first-order equation

    z=k+epsilon[ell_0(L)+L.y]+O(epsilon^2).

Its physical perpendicular foot consequently has horizontal derivative

    p_T,horizontal'=-lambda k L.                         (5.6)

Thus L is the actual first tilt of the top plane after centring. The two independent L directions are the genuine tilt freedoms absent from the old axial family, which preserves parallelism of the end planes.

## 6. A triangle has only a small complete carried packet

This is a classification of possible **physical contacts carried by T**, not a count of arbitrary algebraic zero rows.

If T has no bearing EF/VF, it has at most two carried VE sources. Three sources would each have a zero exit to another triangle vertex. Along every such arrow the squared norm strictly increases, so a directed cycle is impossible. Two carried VEs use different triangle edges, hence nonparallel edge vectors.

If T bears an EF, take its foot as the horizontal origin and write the edge endpoints and third vertex as

    A=(-a,0), B=(b,0), C=(c,d),       a,b,d>0.             (6.1)

The two edge-end arrows along AB are strictly negative. The other possible zero arrows obey

    A->C: c=-a;
    B->C: c=b;
    C->A: c in (-a,0);
    C->B: c in (0,b).                                    (6.2)

These conditions follow directly from the zero dot products, including the positive d^2 term in the last two cases. They are mutually incompatible as two distinct carried VE sources. Thus a bearing EF allows at most one further carried VE.

If T bears a VF at vertex A=0, the arrows B->A and C->A are strictly negative. At most one carried VE can occur on BC. A triangle has only one perpendicular foot, so two separate bearing EF/VF points are impossible.

The complete possibilities for C_T are therefore:

    zero, one or two simple VE points;
    one EF, possibly with one VE;
    one VF, possibly with one VE.                        (6.3)

The last possibility contains three scalar obligations if its VF pair is written without compression. The proof below retains them all.

## 7. Actual tilt responses and the nonpersistent simple-contact obstruction

### 7.1 Simple response pencils

At a carried VE i->j, put e=y_j-y_i. Equations (5.5)–(5.6) give

    P_ij'=v_i.e+y_i.(v_j-v_i)+lambda k L.e.               (7.1)

This is a row of the form

    [a_ij+lambda k e].L,

with a_ij a fixed actual-body coefficient vector. Its centroid contribution is already included in v_i.

At a bearing EF on edge ij, let theta_i y_i+theta_j y_j=0, theta_i,theta_j>0, theta_i+theta_j=1. Let nu be the inward horizontal normal of that triangle edge. Use the signed foot-exit function

    psi=nu(L).[theta_i Y_i,horizontal(L)
                  +theta_j Y_j,horizontal(L)-p_T,horizontal(L)].

The exact physical Q row is a positive analytic multiple of psi near the original EF. To see this, restrict the neighboring supporting-plane inequality to the top plane: its inward-edge normal has the opposite sign to the restricted support gradient. Therefore psi>0 is exactly the foot violating that neighboring inequality, and Q=(q_T^T N q_T) times this violation. No physical sign is lost by this normalization.

At zero,

    psi'=nu.(theta_i v_i+theta_j v_j)+lambda k nu.L.       (7.2)

The moving nu contributes nothing because the bracket is initially zero. The coefficients of both simple-contact responses are affine in the same lambda.

A single response has a nonzero polynomial component because k!=0 and its leading vector is a nonzero edge or edge normal. For two VEs, the 2-by-2 response determinant has nonzero leading coefficient

    k^2 det(e_1,e_2).

For EF+VE the same argument works unless the VE edge is parallel to the EF inward normal.

### 7.2 The exceptional parallel EF–VE configuration is forced by incidence

In that exceptional case, (6.2) implies that the VE goes from an endpoint of the EF edge to the third vertex. After reflection and relabelling, write

    A=(-a,0,k), B=(b,0,k), C=(-a,d,k),    a,b,d>0,

with EF on AB and VE A->C. The actual quads across AB and AC have poles

    r_AB=(0,beta,1/k),
    r_AC=(gamma,0,delta),       beta!=0, gamma!=0.        (7.3)

A zero beta or gamma would make that quad's plane the top plane itself, contradicting the true incidence with F.

These raw quad planes are fixed by (5.1). Subtracting their two endpoint incidence derivatives gives

    v_C,x-v_A,x=-(delta/gamma)d L_y,
    v_B,y-v_A,y=-(a+b)L_x/(k beta).                      (7.4)

The actual centroid loads cancel in these differences because (5.5) subtracts the same alpha c from all three top vertices.

Normalize the VE row by the positive d, writing f=P_AC/d. With theta_A=b/(a+b), theta_B=a/(a+b), equations (7.1)–(7.4) give

    f'=v_A,y+(a delta/gamma)L_y+lambda k L_y,
    psi'=v_A,y-a L_x/(k beta)+lambda k L_y,

    f'-psi'=a L_x/(k beta)+(a delta/gamma)L_y.            (7.5)

Both responses have the same lambda k L_y part, but their difference has a nonzero L_x coefficient. Hence their response determinant has a nonzero linear coefficient in lambda, namely a/beta up to row order.

This removes the only potentially persistent two-simple-contact rank defect. It is not a generic determinant assumption. It uses the true quad incidences and the actual common centroid correction.

### 7.3 Consequence

For every simple-contact packet in (6.3), its response matrix has full row rank for all lambda outside a finite set. A two-row determinant has degree at most two. A suitable one-row component has degree at most one.

At lambda=1 the matrix may be singular. The theorem does **not** assert positive first-order escape at the original metric. It uses the contact-preserving premove lambda=1-t to pass this finite resonance set. For all sufficiently small positive t, the relevant matrix is invertible, and its inverse has a pole of order at most two at t=0.

## 8. VF plus another contact: compatible pairs, not independent scalar choices

Suppose T bears a VF at X_0=(0,0,k). Let E be the invertible 2-by-2 matrix of its two horizontal outgoing edges, and let G=E^T E.

The horizontal mismatch between that vertex and the top foot has tilt derivative

    w'=R(lambda)L,
    R(lambda)=V_0+lambda k I,                            (8.1)

where V_0 L=v_0(L) is the actual corrected vertex velocity. Its determinant has leading coefficient k^2, so R is invertible outside a finite set, with inverse pole order at most two along lambda=1-t.

For a mismatch w, put u=E^-1 w. A valid first-order VF escape requires

    u_i>0 and (G u)_i>0 for at least one i.               (8.2)

The chosen scalar pair is then (P_i,Q_other), exactly as in (4.6).

Write G=[[a,c],[c,b]], a,b>0, ab>c^2. Its bad mismatch directions have a particularly useful exact description:

    c>=0: failure of (8.2) is exactly G u<=0;
    c<=0: failure of (8.2) is exactly u<=0.               (8.3)

For c>=0, a mixed-sign u whose positive coordinate has nonpositive image forces the other image coordinate strictly negative by ab>c^2. The remaining sign cases are immediate. For c<=0, a positive coordinate with a nonpositive other coordinate has a positive image in the same coordinate; if both coordinates are positive, u^T G u>0 supplies a successful coordinate. This proves (8.3), including c=0.

Thus the bad directions form a closed pointed cone in the physical mismatch plane. In particular they cannot contain an open half-plane. At a right corner this is simply a linearly transformed negative quadrant, not an unpaired first-jet substitute.

If there is a further carried VE, denote its tilt response row by b(lambda). By (7.1) it is affine in lambda with nonzero leading vector. Define

    H(t)=b(1-t) R(1-t)^-1.                               (8.4)

It is a nonzero rational row. Its numerator degrees are at most two and its denominator degree at most two. Consequently its first nonzero Laurent term is

    H(t)=t^r H_*+higher terms,
    -2<=r<=2,             H_*!=0.                        (8.5)

Choose a constant mismatch w with H_*.w>0 and satisfying one strict complementary VF pair in (8.2). Such a w exists because the open half-plane H_*.w>0 cannot be contained in the closed pointed bad cone. This chooses the VF branch and the VE response **simultaneously**.

For a lone VF choose, for example, w equal to its first outgoing edge. Then u=(1,0), P_1 has positive coefficient and so does its complementary Q_2. This remains valid when the other pair has a zero or negative coefficient.

## 9. An analytic resonance bypass with explicit finite orders

All the following curves are defined for sufficiently small t>0 and extend analytically to t=0. No numerical radius is asserted.

Let the body initially stay fixed during the metric premove lambda=1-t. The carried packets C_F and C_T remain exactly weak at this stage. The functions of the later tilt L are analytic jointly in (L,t), with the following uniform Taylor forms:

    simple rows = A(1-t)L+O(|L|^2),
    VF mismatch = R(1-t)L+O(|L|^2).                      (9.1)

The positive-factor EF normalization does not change any leading order or sign.

### Simple triangle packets

For two simple rows use their invertible response matrix A and set

    L(t)=t^5 A(1-t)^-1 (1,1)^T.                          (9.2)

Its possible inverse pole has order at most two, so L(t)=O(t^3). Both rows are therefore

    t^5+O(t^6)>0.

For one row use a nonzero component and its one-dimensional right inverse, with the same t^5 prefactor. The empty packet needs no tilt.

### Lone VF

Use a fixed successful mismatch w and

    L(t)=t^5 R(1-t)^-1 w.                                (9.3)

Then L=O(t^3), and the actual mismatch is t^5 w+O(t^6). Both members of the selected VF pair are strictly positive at order five. The changing edge basis and Gram matrix add only later terms.

### VF and VE

Choose w by (8.5) and use

    L(t)=t^7 R(1-t)^-1 w.                                (9.4)

Now L=O(t^5). The VF mismatch is t^7 w+O(t^10), while the extra VE row is

    t^7 H(t).w+O(t^10).

Its positive leading order is 7+r, between five and nine. The remainder begins at order ten and cannot destroy it. Both VF exits have positive leading order seven.

These formulae prove integrated higher-order success even when the original response matrix is singular. They do not equate a failed original first jet with nonregularizability. In the right-corner case the construction produces an actual positive complementary pair; it never relies on an ambiguous equality in a compressed second-jet threshold.

All permitted cross contacts from Section4 retain their positive order-one exits: the largest subsequent tilt is only O(t^3).

## 10. Opening the heptagon and retaining simultaneous signs

For completeness, the last step can be reconstructed directly rather than treating the heptagon-opening flow as an unspecified actuator.

Its foot is p_F=(0,0,h). For a carrier vertex write y_i=X_i-p_F and r_i=|y_i|^2. Prescribe

    X_i(eta)=X_i+eta(K r_i y_i+a),      i in F.            (10.1)

Take a=0 if F has no bearing EF/VF. At a bearing EF take a=z-p_F for any z in relint F. At a bearing VF take a to be one outgoing true F edge at its foot vertex. Choose

    K=1+sum_carried_VE |a.e_ij|/[r_i |e_ij|^2].           (10.2)

Every denominator in (10.2) is positive: a carried VE cannot be the carrier foot itself, which would be a VF. Its selected derivative is

    P_ij'=K r_i |e_ij|^2+a.e_ij>0.

The inward translation opens the bearing EF. At a bearing VF, the outgoing-edge translation gives u'=(1,0), hence the corresponding positive complementary pair, also at a right corner. These are the inherited carrier signs, with the exact physical pairing retained. fileciteturn21file0L93-L98

An explicit raw extension of (10.1) is available in this incidence. Keep the top height k. For each of the three base edges associated with a top edge, take its moving horizontal edge vector, rotate it by ninety degrees to obtain a line normal, and retain the original top-line constant. Intersect the three top lines pairwise in their original cyclic order. Their initial pairwise determinants are nonzero. Each moving top edge is parallel to its associated base edge, so the three true quads remain planar. The remaining lateral faces are triangles. Compute the actual uniform centroid and apply (5.3), preserving the prescribed F polygon pointwise.

Call the resulting centred body P_eta. Take

    eta=t^10.                                            (10.3)

The tilt construction extends jointly analytically to P_eta, even though its top plane need no longer be parallel to F after centring. Indeed compute B_i from the two actual base-edge lines of its quad neighbors, and use the raw update

    Z_i -> Z_i + [(L.pi(Z_i))/(h-Z_i,z)](B_i-Z_i),         (10.4)

where pi is the fixed horizontal projection. Then apply the actual uniform-centroid correction. At eta=0 this is (5.1); all its denominators are nonzero near the starting body. It always fixes F pointwise and preserves the true quad incidences.

Apply this extended tilt with the already selected L(t), together with the metric M_lambda. Joint analyticity implies that every off-F row differs from its eta=0 value by O(t^10). Every selected off-F positive term has order at most nine, so it survives.

The F-carried rows are protected exactly. A genuine fixed-F-polygon motion sends every carrier-edge neighbor pole r to

    r_new=q+mu_r(r-q),       mu_r>0.

Thus its within-F primal rows are unchanged, and under the normal pencil its F-source polar rows are multiplied by a positive factor. Both members of each selected carrier VF pair retain their signs. This exact neutrality is the parent's full-fibre identity, not a sequential-isolation assumption. fileciteturn23file0L79-L95

The resulting leading-order bookkeeping is:

| Physical obligation | Positive order supplied |
|---|---:|
| Permitted cross contacts, including cross VFs | 1 |
| Triangle simple packet or lone VF | 5 |
| Triangle VF in a VF+VE packet | 7 |
| Its additional VE | Between 5 and 9 |
| Heptagon-carried packet | 10 |

Every originally nonzero primitive is retained by continuity in a sufficiently small true-lattice neighborhood. Every original weak vertex and weak facet now has a positive physical exit. The supplied extremal-selector equivalence therefore retains all original strict S,U,H labels and leaves no other strict or weak equilibria. fileciteturn16file7L78-L102

All intermediate shape centring uses the ORIGINAL uniformly filled body's actual fan moments. No uniformly recentered polar is introduced. The common metric and inverse are exactly (4.1) or (4.2). To obtain a curve with the initial physical metric fixed, absorb M_lambda at the end by the analytic linear map diag(1,1,sqrt(lambda)) in the normalized frame. It preserves the zero uniform centroid and the face lattice. At t=0 this map is the identity.

This completes the theorem.

## 11. Reconstruction recipe and verification boundary

For an actual input in the stated class, the proof gives the following complete analytic recipe.

Normalize the common metric once, identify F,T and the three true quads, and check the EF spoke signs (1.1). Form the actual linear maps c(L) and v_i(L) by (5.1), (5.4) and (5.5). Classify the triangle-carried packet using Section6. Build its explicit affine-in-lambda response matrix from (7.1), (7.2) or (8.1).

For the simple cases, use the rational inverse in (9.2). For a lone VF use (9.3). For VF+VE, extract the first nonzero Laurent coefficient of the rational row (8.4), and choose w by one of the two feasible systems of strict linear inequalities

    H_*.w>0,
    (E^-1 w)_i>0,
    (G E^-1 w)_i>0,          i=1 or 2.

Section8 proves that at least one of these two systems has a solution. Use (9.4). Finally form (10.1)–(10.4), centring every raw body by (5.2)–(5.3), and absorb the metric if a fixed-metric curve is desired.

All apparent poles in the selected L(t) are cancelled by the stated powers of t. For rational or algebraic normalized data this uses exact field arithmetic and finite sign decisions. For arbitrary real data it is the same analytic existence construction. No global coordinate chart, numerical locator or unstated positive-stress solver is needed to establish the theorem.

A sufficiently small positive interval exists by the proved nonzero determinant polynomials and the original strict geometric/mechanical guards. This continuation does not compute a universal radius or an input-specific interval certificate. No new exact body or computational output is presented, so there is no new source archive, output hash or execution marker to recover. The mathematical construction above is the continuation-critical handoff.

## 12. What this changes for S1U1, and what remains

For weak S1U1, strict H=0 is already forced by the supplied weak radial-index identity. The construction therefore converts every input satisfying the theorem's geometric/contact hypotheses to proper110 without cancelling or adding any original strict equilibrium. It does not assume that such an input has been found. fileciteturn16file7L7-L13

The new result is stronger than access to the full fibre or a generic four-column cone test. It proves success on a complete class of dispersed physical packets, including arbitrary numbers of VE/VF contacts across both end facets and all their spokes. The triangle's physical contact classification, the nonzero determinant coefficient in the parallel EF–VE case, and the pointed VF bad cone replace generic rank assumptions. A moment coefficient may vanish; the normal-metric resonance bypass still works.

The unresolved residual in this parallel class is now concentrated on **adverse or normal-blind EF points inside spokes**, potentially coupled to other contacts. Their occurrence is not a nonregularizability certificate. The unchanged parent `HEPT_REFLECTION_FIVE_WEAK` is an instructive boundary: its literal poles satisfy q_8-q_2=(0,c,0), so its spoke EF has gamma_EF=0, yet the parent already gives genuine full-fibre escape. Its strict count is446, not S1U1. This confirms that (1.2) identifies a remaining mechanism rather than an obstruction. fileciteturn23file0L245-L258 fileciteturn24file0L20-L30

The supplied octagon V2 theorem remains a different, conditional statement: its mixed calibrated germs have positive orders at most12 and carrier gluing order13, but it does not establish feasibility for every packet. The order-ten construction here exploits parallel heptagon–triangle contact geometry and is not a replacement for that general octagonal screen. fileciteturn16file0L64-L70

Finally, no conclusion is made that a failed original calibrated first jet is an all-orders failure, or that a failed calibrated germ is a full-shape obstruction. The present construction explicitly illustrates the former distinction: it can begin with a singular response at the original metric and still integrate to an analytic simultaneous escape. Nonparallel end geometry, other heptagonal incidences, adverse spoke-EF packets and the complete E17 S1U1 question remain separate. No attaining construction, canonical registry subtraction or bound improvement follows.
