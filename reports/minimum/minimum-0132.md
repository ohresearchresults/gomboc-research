# minimum-0132

AI research report · 2026-09-20 UTC · [Export notes](../../catalog/coverage.md#text-records)

<!-- historical-status:start -->
> **Historical AI report.** The title and claims below reflect the AI’s assessment at the time. Claims of proof, certification or completion are not a current verification verdict.
>
> Minimum’s C≥34 remains a working lower bound requiring a consolidated proof. [C622](../../C622/README.md) passes the supplied exact checks. See [verification status and source gaps](../../catalog/coverage.md).
>
> This public text omits encoded source blocks; code in the affected passages is incomplete.
<!-- historical-status:end -->

---

# NONBASAL_E17_NORMAL_AND_HORIZONTAL_RIDGE_V1

## 1. Results

Two new regularization mechanisms close substantial nonbasal sectors of the true two-apex V10/E17/F9 problem.

**Normal-height theorem.** Let P have exactly four simple physical A=VE weak points at its actual uniform-volume centroid. Choose a true facet B, an affine function ell that is zero on B and positive inside P, and define

    h(v)=ell(v)−ell(g),
    beta_i=h(x_i)[h(y_i)−h(x_i)]

for each weak arrow x_i→y_i. If all beta_i have one weak sign and at least one is nonzero, P regularizes arbitrarily closely while retaining its full lattice and exactly its original strict feature-labelled equilibria. This uses a genuine affine image, not a freely adjusted centroid. In its most general form, the last step invokes the accepted at-most-three-A theorem.

Important complete consequences are:

* Every four-A configuration whose four sources belong to one true facet and at least one weak edge leaves that facet regularizes, on an arbitrary convex three-polytope.
* On every two-apex E17 realization, all mixtures of basal weak edges and weak spokes regularize when both apices lie strictly above the base-parallel plane through the actual centroid. Spoke orientations are unrestricted. No weak ridge is required in this statement.
* On an equal-height two-apex E17 body, every pure-four-A configuration containing a weak spoke regularizes, including configurations that also contain a horizontal weak ridge.
* A configuration with three basal weak edges and one nonbasal weak edge regularizes whenever that last edge has beta≠0.

For the cases in which the affine step removes every nonbasal point, the remaining basal contacts can be removed by the literal parent, with no restriction to four total contacts.

**Horizontal-ridge theorem.** Let P be a genuine two-apex E17 body with its ridge parallel to the octagonal base. Suppose its only weak points are one simple A on the ridge, a→b, and any finite number of simple basal A points. If a base vertex adjacent to the ridge source a is not an endpoint of any basal weak edge, P has a genuine first- or second-order regularization at the original body. The theorem also holds when a free vertex on the other apex’s side satisfies the explicit nonzero linear-moment test in section4. Neither a nonsingular independent-vertex centroid map nor absence of a full constrained stress is assumed.

A new **parallel-quadrilateral lemma** explains a physically important failed construction: two simple A points on opposite parallel sides of a true quadrilateral, with their source vertices joined by another side, force an additional simple EF point on that connecting side. Four A rows in that arrangement cannot constitute a pure-four-A body.

These are not a universal nonbasal theorem. The remaining normal-sign conflict localizes to **one adverse physical packet**, not an arbitrary collection of bad rows. The horizontal-ridge complement is narrowed to an explicit target-side critical-moment configuration. No body realizing an obstruction to arbitrary-small full regularization is supplied.

There are fifteen new exact actual E17 controls, including nine pure-four-A bodies, four bodies with four A plus one EF, and two bodies with three A plus a harmless fourth zero primitive. Two complete own-centroid curves are certified on whole rational intervals, preserving strict8/5/11 and7/6/11 respectively. None is110, and the minimum bracket34≤C_min≤622 is unchanged.

## 2. Input authority and evidence

I read the complete1820-line `research-journal(20260920-163942).md` through EOF, including the whole literal parent and its runnable source. The file has301894 UTF-8 bytes and SHA-256

    24a2a1c03b993aabc3c6dccea9244ca42a4baa6242f27b5a50202daaf0a77639.

The required parent is `minimum-0130`, literal title `FACET_FIXED_UNIFORM_CENTROID_BASAL_A_REGULARIZATION_V1`. Its authenticated compact JSON envelope has40131 bytes and the required SHA-256

    9863c408b85c35e7e71a6b9190aebd11854fb989462ab2a72ccf1f2d871ab00e.

Authentication uses UTF-8, `ensure_ascii=False`, separators `(',',':')`, keys `version,result_markdown`, one final LF inside the Markdown string and no envelope-final LF. No source conflict was found. Earlier unchanged evidence remains the supplied same-chat context; no missing exact computational dependency is needed by the new capsule.

The parent’s all-basal theorem is used as accepted evidence, not re-announced as new work. Its exact centroid correction fixes one facet pointwise; it does not fix two independent facets or automatically protect nonbasal endpoints. The general normal-sign reduction also uses the shared accepted theorem for at most three simple A points; its actual projective refilling, rather than transported mass, is essential.

All new exact controls and both interval certificates were executed. The final source completed an original check and fresh source-only build/check with byte parity. A preceding unoptimized check timed out; it is not counted as a successful run. Replacing symbolic rational differentiation by exact coefficient jets preserved the report bytes and allowed the final checks to complete. Wrapper extraction was independently byte-matched to that final source. No proof-assistant or literature-priority certification is claimed.

## 3. Normal-height separation and the single adverse packet

### 3.1 Exact physical affine motion

Work in an original rational or real coordinate chart at g=0, with the one physical SPD metric M0 and its inverse. Write n=grad ell. Set

    M(t)=M0−t n n^T.

For sufficiently small positive or negative t this remains SPD. Choose an actual continuous affine factor B(t) with B(t)^T B(t)=M(t). The uniformly filled body B(t)P has its actual centroid at0, because affine maps transport uniform volume centroids. Its true lattice is unchanged, and the polar metric is exactly M(t)^{-1}.

At an original weak A point the escape is exactly

    x_i^T M(t)(y_i−x_i)=−t beta_i.                       (1)

Thus beta_i≤0 opens every strictly negative row while keeping every zero row exactly zero. For beta_i≥0 use negative t instead. The three other primitives in each simple packet remain strictly negative at a sufficiently small step. Existing strict and excluding guards remain open. Consequently no strict pair is born, no new weak packet appears, and at least one of the four original weak points disappears. At most three simple A points remain, so the accepted three-point theorem finishes the regularization.

This argument is stronger than counting a positive affine derivative: equation(1) gives exact zero preservation for all the other packets during the preliminary motion. It handles the whole set of four physical points, not four arbitrarily chosen primitive zeros.

If every nonbasal beta is strictly negative, all nonbasal points disappear at once. The literal basal theorem then finishes any number of remaining basal A points on a two-apex body.

### 3.2 Complete geometric sectors

Every base vertex has h=−c, where c=ell(g)>0, and each outside vertex has ell>0. Therefore a basal→apex weak spoke always has beta<0. This proves the cofacial-source consequence stated in section1.

If both apices have h>0, every weak spoke has beta<0 in either orientation. A weak ridge directed from the higher apex to the lower one also has beta<0. A horizontal ridge has beta=0. In particular, equal-height apices lie above the actual centroid, and any weak spoke can be opened while all basal contacts and the possible horizontal ridge remain zero. With four original points this leaves at most three.

If the apices straddle the actual base-parallel centroid plane, a weak ridge has beta<0 in either orientation. Every spoke is also negative except a spoke whose source is the lower apex and whose target is basal. Thus the whole straddling sector without that last kind of weak source is closed by the same motion.

Finally, with only one nonbasal contact, all other beta values are zero. Any nonzero beta on that contact, of either sign, opens it without affecting the basal contacts.

### 3.3 What can actually oppose this motion

On a two-apex body there is at most one apex below the centroid plane: the centroid’s ell-coordinate is strictly below the maximum vertex ell-coordinate. A simple A source has only one outgoing weak edge. It follows that **at most one nonbasal beta can be positive**. Its edge is precisely one of:

    a weak ridge directed from the lower to the higher apex,
    when both apices are above the centroid plane;

or

    a weak spoke directed from an apex below the centroid plane
    to a base vertex.

A positive beta cannot coexist with a nonbasal zero beta. Nonbasal zero beta occurs only for a horizontal ridge, or for an outgoing weak edge whose apex source lies exactly in the centroid plane; there is at most one such nonbasal zero point.

Hence the normal-sign test fails only in two kinds of nonbasal four-contact configurations: one positive beta together with at least one negative beta; or one zero-beta nonbasal point with three basal points. The next section closes a substantial part of the latter class. This is an exhaustive sign classification for this particular normal motion, not a classification of all feasible bodies or stresses.

### 3.4 Consequence for the entire constrained stress cone

Let alpha≥0 be any nonzero FULL realization-space stress, with the polygon reactions retained. Testing it on the actual affine normal motion gives

    Σ_i alpha_i beta_i=0.                               (2)

No nonzero nonnegative full stress can be supported only on basal contacts: the parent’s actual basal construction supplies a realization velocity positive on every basal row, even when other rows are merely ignored for this algebraic test.

In a mixed-sign residual, therefore, every nonzero full nonnegative stress has a strictly positive coefficient on the unique adverse packet e:

    alpha_e beta_e=Σ_(beta_i<0) alpha_i |beta_i|>0.        (3)

For a horizontal-ridge-plus-basal residual, every such stress has a positive ridge coefficient. These assertions concern the **whole cone**. They do not assert that its signed span has dimension one; the nonsimplicial polygon reactions are still present.

## 4. Horizontal ridge: an exact source-side quadratic moment

### 4.1 Coordinates and the actual slice law

Absorb the original metric into an actual affine image and use physical orthonormal coordinates. Put B in z=0, let the ridge direction be e_x, and write

    a=(0,c,H),  b=(L,c,H),  L>0, H>0.

The weak ridge equation implies that the actual centroid has x-coordinate0. Write it as g0=(0,g_y,gamma), with gamma>0. These are coordinates for the same actual body; no center is prescribed in place of integration.

For each transverse y in the base projection, write the filled base interval as

    [l(y),r(y)].

Here l is convex and r is concave. At height z=tH, the true section of conv(B,[a,b]) has y-coordinate `(1−t)y+t c` and x-interval

    [(1−t)l(y), (1−t)r(y)+tL].                          (4)

The extra transverse Jacobian is1−t. Thus all moment calculations below are integrals over the actual uniformly filled body.

The base vertices on the l-chain are exactly the base vertices adjacent to the ridge source a. The two joining quadrilateral base edges are parallel to e_x. Moving one of their endpoints along e_x preserves its quadrilateral plane; an interior chain vertex is incident only to the base and triangular side facets. Consequently any small horizontal displacement of a base vertex, with the other vertices and both raw apices fixed, is a genuine lattice-preserving realization motion. No integration diagonal is treated as a mechanical edge.

### 4.2 A free source-side vertex always works

Choose a source-side base vertex w avoiding all basal weak-edge endpoints. Move its x-coordinate by s, keeping y and z fixed. Its change in l is s psi(y), where psi is the piecewise-linear hat function at w. Let the transverse lengths on its two sides be d_-,d_+≥0, with d_-+d_+>0. At a chain endpoint one of them is zero. Denote the neighboring x-coordinates by l_-,l_w,l_+.

Direct integration of(4) gives the complete, exact change of the ridge-direction first moment:

    J_x(s)=A s−B s²,
    A=−H[d_-(l_-+2l_w)+d_+(l_++2l_w)]/24,
    B=H(d_-+d_+)/24>0.                                 (5)

The original J_x is0. In particular, this is not a frozen-star approximation. The actual volume and vertical first moment are

    V(s)=V(0)−H(d_-+d_+)s/6,
    J_z(s)=J_z(0)−H²(d_-+d_+)s/24.                      (6)

For completeness, the quadratic term in(5) comes from

    −(H/8)∫[(l+s psi)²−l²]dy,
    ∫psi²dy=(d_-+d_+)/3.

Choose the sign of s so that A s<0 when A≠0. If A=0, either nonzero sign gives J_x(s)<0 to second order.

Now apply the parent’s actual facet-fixed centroid correction

    F_s(x)=x+z(g0−g(s))/g_z(s).                         (7)

It fixes B pointwise, sends the true new centroid to g0, and has positive determinant gamma/g_z(s). Since the two raw apices have the same height, their difference after F_s is still exactly L e_x. The actual own-centroid ridge escape is therefore

    phi_ridge(s)=−HL J_x(s)/J_z(s)>0.                   (8)

Every basal weak endpoint stayed fixed, and(7) fixes it again. Hence every original basal weak escape is still exactly zero. All remaining packet and strict/excluding guards persist for small s.

This proves that the ridge can always be removed using a free source-side vertex, including at a zero first derivative. It does not assume a three-dimensional independent free-vertex centroid map.

### 4.3 A genuine first- or second-order full regularization

Let K(s,delta) be the actual body obtained by the preceding motion and correction, followed by the parent’s basal radial flow, quadrilateral lift and centroid correction with parameter delta. These operations are analytic near(0,0); the same nonsingular plane-intersection pivots can be retained. At delta=0 all basal weak endpoints are the original ones.

Suppose the ridge escape from(8) has leading term c_r s^r, with c_r>0 and r=1 or2. Each basal escape has positive delta derivative d_i>0. Let R be the delta derivative of the ridge escape at(0,0), and choose

    epsilon=min(1,c_r/[2(1+|R|)]),
    delta=epsilon s^r.                                 (9)

Then every basal escape has leading coefficient epsilon d_i>0, and the ridge coefficient is at least c_r/2. Thus the full body regularizes to first order when the free slide has A≠0, and to second order when A=0. Actual uniform COM is fixed at every parameter value.

The construction automatically includes the polygon-curvature term in the intrinsic second jet. In the parent’s notation, its vertex/pole jets obey C z2=−d, and stress pairing is alpha·b−lambda·d, not alpha·b alone. Equation(8), together with the positive ridge coefficient of every full nonnegative stress, is also a direct whole-cone explanation of the second-order rescue.

The concrete recovery uses the simpler safe choice delta=s³ for its ridge control. That particular curve is not asserted to have minimal order.

### 4.4 Target-side extension and a precise simultaneous-motion boundary

A free target-side vertex also opens the ridge whenever its linear J_x coefficient is nonzero. Its exact formula is

    J_x(s)=A_+ s+B s²,
    A_+=H[d_-(r_-+2r_w+L)+d_+(r_++2r_w+L)]/24,
    B=H(d_-+d_+)/24>0.                                 (10)

Choose the sign making A_+s<0 and proceed as above.

Consequently a horizontal ridge with three basal points survives these automatic free-slide tests only if every free base vertex is on the target side and every one satisfies A_+=0. There are at least two free base vertices, since three basal edges cover at most six of the eight base vertices.

There is an exact boundary for this restricted architecture, including simultaneous motions. Let delta(y)=Σ_j s_j psi_j(y) move all such target-side free vertices, with every other raw vertex fixed. If all their linear coefficients vanish, then

    J_x(new)−J_x(old)=(H/8)∫delta(y)²dy>0                (11)

for every nonzero displacement. The hat functions are linearly independent; their Gram matrix has diagonal entries(d_-+d_+)/3, adjacent off-diagonal entries equal to the intervening transverse length divided by6, and zero other entries. Thus all adjacent mixed terms are retained. After the actual correction(7), the ridge escape is negative, not positive. No nonlinear parameterization of these same simultaneous horizontal free-vertex motions can evade(11).

This is a **conditional all-orders failure of that restricted architecture**, not an all-orders obstruction to full regularization. No actual pure-four-A body satisfying all of these critical equalities is constructed here. Moving contact endpoints, changing transverse base coordinates, changing ridge orientation, and the full constrained affine/projective tests remain available.

For example, when the ridge source has true degree7, its source-side chain has six base vertices. With three basal weak edges, a free source-side vertex exists unless those three edges cover all six source-side vertices. In that exception they must be the three matching edges of that six-vertex chain. This closes the entire complementary degree7-source incidence sector, without a metric or coordinate-complexity restriction.

## 5. Parallel weak sides force a real EF packet

**Lemma.** In a genuine convex three-polytope, let a maximal quadrilateral contain opposite parallel sides x→x+u and y→y+v, and suppose x,y are joined by another true side. If both arrows are simple physical A points, then the connecting edge[x,y] carries a simple EF point for that quadrilateral.

Use physical Euclidean coordinates at the reference point. With common direction d, the two A equations give x·d=y·d=0. The quadrilateral’s normal q is perpendicular to d. Its foot q/|q|² therefore belongs both to its plane and to d-perp; their intersection is exactly the line through x,y.

Because the original radial planes expose only their respective weak sides, the two primitives along[x,y] are strictly negative. The foot on its line is consequently in relint[x,y]. If q' is the other facet pole at that edge, then

    q·(q'−q)=0,  q'·(q−q')<0.

Together with the two strictly negative primal values, these are exactly a simple EF packet. The foot is in the relative interior of a true edge, so this is not a VF duplication or a harmless zero. The same proof uses M-orthogonality and M^{-1} in a general chart.

In particular, a weak horizontal ridge and a parallel basal weak side of an incident quadrilateral cannot have adjacent source vertices in a pure-A body. Opposite diagonal sources are not excluded by this lemma. This distinction explained the first failed ridge construction below; changing the actual basal vertices, not relabelling its zeros, produced the successful pure-A controls.

## 6. Exact actual controls and continuous curves

### 6.1 Complete common realization

The fixed outward facet cycles, with zero-based labels, are

    (0,7,6,5,4,3,2,1), (0,1,8,9), (0,9,7),
    (1,2,8), (2,3,8), (3,4,8), (4,5,9,8),
    (5,6,9), (6,7,9).

The raw positive-orientation family is

    0=(1,0,0),       1=(1,1/4,0),
    2=(0,r,0),       3=(−1/3,s,0),
    4=(−1,1/5,0),    5=(−1,0,0),
    6=(0,−1,0),      7=(2/5,−1,0),
    8=(0,a,2),       9=(0,−a,2).                         (12)

Integrate its true uniform centroid g, apply the affine shear

    S=[[1,0,−g_x/g_z],[0,1,−g_y/g_z],[0,0,1]],           (13)

and subtract Sg. The capsule independently reconstructs the true hull, all seventeen edges, maximal facets, poles and mechanics, and checks volume, first and second moments from two different positive apex fans. All controls happen to have balanced apex degrees5/5; the analytic theorems are not restricted to balanced realizations.

### 6.2 Five pure ridge-plus-three-basal controls

Use the five exact tuples(r,s,a):

    (21/20,23/20,3/20),
    (39/20,7/4,7/10),
    (9/8,49/40,17/80),
    (47/40,9/8,1/5),
    (59/40,13/10,31/80).

At M=I their only weak points are0→1,5→4,6→7 and8→9. All other64 primitives are nonzero. Their volumes are89/45,149/45,763/360,251/120,38/15; the post-shear raw centroid heights are49/89,191/298,865/1526,283/502,183/304. Their strict counts are8/5/11,7/5/10,8/5/11,9/6/13,8/5/11.

These are not full-stress coexistence controls. The first has tensor rank3 with relation, in the displayed contact order,

    (−7807/4900,−7673/3920,0,1),

which has mixed signs; its constrained shape matrix has rank4. The new theorem is analytic and is not inferred from these examples.

For the first body, the post-shear raw apices are

    (−67/2940,0,2), (−67/2940,−3/10,2),

and g0=(0,0,49/89). Move raw vertex2 by+t e_y, vertices0 and5 by+t³ e_y, and vertex6 by+t³ e_x. All other raw vertices are fixed. The complete actual raw moments are

    V=89/45+4t/9−13t³/15−t⁶/3,
    Jx=631t/8820+23803t³/176400+67t⁶/35280−t⁹/12,
    Jy=103t/360+t²/9+73t³/200−t⁶/40−t⁹/12,
    Jz=49/45+2t/9−13t³/30−t⁶/6.                         (14)

Apply the exact affine map

    L(t)=[[1,0,−Jx/Jz],[0,1,−Jy/Jz],[0,0,(49/89)V/Jz]]

and subtract g0. Its actual centroid is identically0 and volume is(49/89)V²/Jz. The three basal escapes are exactly

    t³(1/4−t³), t³(1/5−t³), t³(2/5−t³),

and the ridge escape is(3/5)Jy/Jz, with first two coefficients309/1960 and279/9604.

**Whole interval certificate:**0<t≤1/65536. All218 polynomial guards have6808 strictly positive exact Bernstein coefficients, maximum degree60. The original strict labels are

    S=[0,1,2,3,5,6,7,8],
    U=[1,3,4,7,9],
    H=[(0,7),(0,9),(1,2),(1,8),(3,4),(3,8),
       (4,8),(5,6),(5,9),(6,9),(7,9)].

They remain exactly unchanged and weak000 holds throughout.

### 6.3 Six spoke controls: four pure, two with harmless zeros

In(12) take r=47/40,s=9/8 and a=2,3,4,5,6,8. After actual centering, choose

    M=diag(1,1,lambda),
    lambda=−[X2_horizontal·(X8−X2)_horizontal]
                    /[X2_z(X8_z−X2_z)],                 (15)

which is a positive rational for every listed input. The Euclidean body is diag(1,1,sqrt(lambda))X, so these chart metrics are actual uniform affine realizations.

For a=4,5,6,8 the only weak points are0→1,2→8,5→4,6→7; all have strict7/6/11. At a=2,3 there are only three physical A points: edge6–7 has packet(0,−,−,+), a harmless zero. Those two controls have strict6/5/9 and6/6/10. They are not pure-four-A fixtures.

The primary a=4 control has chart volume859/120, post-shear centroid height1499/1718, and

    lambda=6581566087/3595201600.

Its post-shear raw apices are

    (−176/22485,29184/7495,2),
    (−176/22485,−30776/7495,2).

Move raw vertices0,5 by+t² e_y and6 by+t² e_x; apply the same exact centroid fixer using this body’s actual V,J and gamma=1499/1718. Simultaneously use

    M(t)=diag(1,1,lambda(1−t)),  N(t)=M(t)^{-1}.          (16)

The three basal escapes are t²(1/4−t²),t²(1/5−t²),t²(2/5−t²). The spoke escape has first coefficient7661893/2398400>0; its actual second coefficient is−9093466/32191025, which is retained rather than discarded.

**Whole interval certificate:**

    0<t≤104173609050597191064585849256
          /118260603575831818502927443641586961.

All218 polynomial guards have4574 strictly positive Bernstein coefficients, maximum degree40. Original strict labels

    S=[0,1,3,4,6,7,8],
    U=[1,3,4,7,8,9],
    H=[(0,7),(1,2),(1,8),(2,3),(3,4),(3,8),
       (5,6),(5,9),(6,9),(7,9),(8,9)]

remain unchanged, with weak000 throughout.

### 6.4 Four distinct failed ridge controls, preserved

Replace vertices4,5 in(12) by(−1,0,0),(−1,−1/5,0), and use

    (39/20,27/20,11/20),
    (39/20,33/20,5/8),
    (67/60,77/60,1/6),
    (7/4,49/30,13/24).

After the same true integration and shear, all have strict6/5/9, four A on0→1,4→5,6→7,8→9, **plus one simple EF on4–8**. Their true volumes are3,16/5,283/135,539/180. For the first, the EF foot has segment parameter6185200/13820881∈(0,1); the capsule supplies the complete exact foot and verifies every packet. Section5 explains this failure for the whole stated parallel-side architecture, not just the four samples.

These are different from the parent’s eight4A+2EF controls. Neither set is silently renamed as pure-four-A.

## 7. Full moment and second-jet audit

For each interval the capsule uses polynomial homogeneous coordinates Z_i=D X_i, with D=Jz>0, generated from the actual raw moments and the centroid fixer. It verifies the exact identities

    J_homogeneous=0,
    V_homogeneous=gamma V_raw² D².

The218 guards per curve comprise three volume/scale/metric guards, nine centroid-inside guards,56 strict nonincidences,82 strict facet-polygon guards and68 mechanical guards, with the four original zeros divided by their positive leading powers. Both primal and dual values use the same M and its adjugate/inverse.

For each positively oriented polynomial p(t)=p0+Σp_jt^j, the deterministic interval rule is

    epsilon=min(1/65536, all p0/[2(1+Σ_(j≥1)|p_j|)]).

It guarantees a positive rational epsilon and positive Bernstein coefficients on the whole closed interval. The report contains every coefficient, not a sampled positivity claim. Both endpoints are independently re-hulled, re-integrated from two apex fans, and fully mechanically recounted.

The complete actual vertex/pole first and second jets are also checked. In both controls rankC=34, rank[C;G]=37, and the constrained contact rank is4. The verified equations include

    C h=0,
    C eta+d=0,  d_vf=h_v·k_f,
    G h=0,
    g2_straight+G eta=0.

All shared-triangle second determinant terms and all metric cross terms are included in the independently checked escape coefficients. The ridge control has nonzero straight g2 even though its full corrected curve is exactly own-centered. Thus this is not an audit with a frozen or first-order-only center.

## 8. Exact recovery capsule and observed identities

The following single capsule reconstructs the **complete16657-byte runnable source**, including every helper, all fifteen exact inputs, both interval certificates, the full second-jet audit and both finite rational discovery grids. No parent code, report, archive, network or sandbox file is an input.

Save it as `recover_nonbasal.py`, UTF-8/LF with one final LF. In a fresh directory run:

    export PYTHONHASHSEED=0
    python recover_nonbasal.py build > build.txt
    python recover_nonbasal.py check > check.txt
    cmp build.txt check.txt

Observed environment: CPython3.13.5, SymPy1.14.0, mpmath1.3.0, assertions enabled. Optional `locate-negative` and `locate-pure` reproduce the complete bounded square-discriminant searches; their failed candidates are not exclusion evidence.

Exact pins:

    recover_nonbasal.py 10092 bytes
    SHA256 9eb0e43dc344632d7e6518cf9b7f2e6207b245d9c6e08a11b3e7d4078b054037
    nonbasal_e17.py 16657 bytes
    SHA256 9cbebc12e390ae34d7a645a1a9ffcb45581c3937865626a7dff9feeb0d7bdbfd
    nonbasal_e17.json 5792478 bytes
    SHA256 478a62f509084b4785d3d7569895214ef18566a0dd20a791f190dbbb696ce961
    build.txt / check.txt 497 bytes
    SHA256 f41fe072cf6b69e92e4cdaf4fdc23b04a090267fc05b43f9f5d7be3b7a3d37e7

Exact main stdout:


[Encoded source block omitted; the code in this passage is incomplete.]

    spoke GUARDS 218 BERNSTEIN 4574 EPS 104173609050597191064585849256/118260603575831818502927443641586961
    nonbasal_e17.json 5792478 478a62f509084b4785d3d7569895214ef18566a0dd20a791f190dbbb696ce961
    NONBASAL_E17_RECOVERY_PASS

Fresh-source receipts ended `NONBASAL_FINAL_SOURCE_ONLY_COLD_BUILD_BYTE_PARITY_PASS` and `NONBASAL_FINAL_SOURCE_ONLY_COLD_CHECK_BYTE_PARITY_PASS`. Wrapper extraction ended `NONBASAL_SOURCE_EXTRACTION_PASS` and matched the final source bytes. Optional locator stdout pins are97 bytes/SHA `e9f06136346bcf3e30fcd0f98fa90a37afe22e8ccdd18fe86aaffd1de6c3ab41` and110 bytes/SHA `2d34cdc12a4b8ebeaed2a88824821e88038e11b5ccc0658edb280405de626e98`.

Convenience copies: plain source (`nonbasal_e17.py`), complete exact report (`nonbasal_e17.json`), recovery capsule (`recover_nonbasal.py`), build receipt (`build.txt`). Recovery does not require these links.

```python
"""Recover NONBASAL_E17_NORMAL_AND_HORIZONTAL_RIDGE_V1.
CPython3.13.5, SymPy1.14.0, mpmath1.3.0; assertions, PYTHONHASHSEED=0.
python recover_nonbasal.py build|check|extract|locate-negative|locate-pure
Parent minimum-0130,
SHA256 9863c408b85c35e7e71a6b9190aebd11854fb989462ab2a72ccf1f2d871ab00e.
"""
from pathlib import Path
import base64,hashlib,subprocess,sys,zlib
assert __debug__
DATA=(
    'c-oyiYjdNzlHc<y*t)d~*s=rIdD+9M$|TNYa`T!blSzi9C=A#pv9SlR<K*1)-?zIZKsY(GclXqpSdUh#TWa-7LRHnvtIN-aw}<E6'
    'z})jLuWl}&czAj2onGC1{dskH2i2Re$6p5Cz1iM6x_-?k^Q6-@JMA5&+`i7PU(L4JZ5vFPEoOc`G25NC(O3K|i_$!vCmB<&AMZ}D'
    'E>90{Pj3f<W7}wNEeMN}%#)#?`BN`4_u7kBWw?x|;lF}O6g>ZHIuHCjY9-Ow&*N28)ECP%+Pa)83qOsLycNvDNQq~Qd73jNTIW%k'
    '_){hHbDt@xpM>+7k}PM#D9x04s*I*{K$eUZKM0~l?k7Ri-cnU{Ym@@u0;r$HLxE1YhAQuf0c}2?PqU&cn9qiB;&b*E={#HpIR_o3'
    'en8Cy=!t0H-MBz95*BB_(tJy_O#BQ9U{BdRVcBa|v}dm~SR6l7vMs)>isyyVa5?ro1$b1lw&$&YMVQ9(Y+L0UqHcY&v-S;9=}-I0'
    'PpG{`={(aq%+&kJSExs?k=B874rSQO;e4v8xvFnnAKnZu?`+l2#@_9G?{#!M`jTA)3-3O;{?_{E&$oj^UlmZ^?dhSd9_;USg08VY'
    '+}{a0JJDXWXZpLt1M|S}qhV;8`#asy@L>O-yKDJF%ipttU}TQ0a3A1?h7qY-M~Bz;H_c?bJ3F0See3Aab~J<Sv0b*qx~#)2pqfF8'
    '$@bX+l@8b*{F>0Sud^)${?jY~gbJ|OrQa?LKA_SLAi`n0fbu|hw@z+tCtoh6k(R+4N1-;-b!CJ?qQr@E^yqHg-FyWSMvmdKk@G}<'
    'nx<O=qVf}#LD<F-&@zn@z|=Bf1`zc>|Jowxn9+a;WHCxXjJ2ajy+;&pAmGDAAO08FH6k@Zi3X(T|H+|UUDr$a!Erl_@-Q0t%W1Af'
    '%yIR$zgR>GFc|AdQy2$%fexTSxM!J$D1>Yw(!sHA+vXlgmp`2nSu1F=h~5>_3qx1_bQ$5;t?TbM16ZqXngzRI=nM)SQJ`N~cPJf*'
    'raji>KPL7F(gA=r>YLU*U|oVU_t?G|+uajw0>)%JwV^xZm=0pac}*JZZe0$(5NYM~)}APs=6l*Y1>HL^Q85Dm?1CV2;)?=EDjzG@'
    '0kS&<304<pzP-Ns=fFF(9h6Fx#9g-UZo%Ft!8Gy{Z7udWjq+uhC~MrP>Fa2j1X|V(P&-X^B?igK;v^$&rL9@kzVP!jUVrwpNLQk1'
    '7AXZVASCS3dI1~vd-NRU-$Y*`B=ljFYd#yYK<^c}{dPFdwP8B|^^$3UF6c;5J(qO+cB&GU<A`A^y%M%`{^C*%3Rqva^Z7K+at&7b'
    'W7L2&mI%!96v_Vx7SBTk_$NX>>%BS=&uqn~6{qE|4>4&-5~K5~OALL$&)Ti+%oZ)zWC<tjq0|e@B(&iuYkH|CV)n$Iaky-MG@*Gw'
    '^g5E>NNnu^R7LB-i9rMKeR*)6MMDV&EF`x5vj->>u#C&7><Mirp<P|^Ar<itt~`7eCt9d~GCs}xH55L;M69&^Fx0pz^9hyD-s&om'
    '3*(z@8$z84eN?Dt!~!ZvR8MX>P%=+v{xq{4w_K(X3tkcRTf6`;R;pSe7?;ovUY%aY?f-s_`T}*KJ`-KysF2HI?W-B^zc-sN-Gj3#'
    'kO^jxJ!F$ckNEj|`()7QC>%%G#+HxR<lTk?PnI;{EQ<2Fkw6q9{lD;MBHIQ@!Q&wPlWoa6S+;|o?{R8q*Qib25l$#k3Wh@NF^!fm'
    'A5Hv)rMJZ#zgx0mqlG?bPvAra&sswhJK&7m+Q!z*Xt|oftFE^J`?Cg<cKDH+`M9ObUqoyBa-Kvii$FX>`z~EZl~%%TILQh^^a%DR'
    'b={*^q#1hu%>LO9=8IQN@848jl-_@d;_)P}3m=jKo<qgm!gdg++jLM8_(7)Kcl)7@x^&@~ZVN%!!m-LyhnMvJo1HCZ+JgP8Hd4%6'
    'NG7)?p|1Dun|8Rp+dqS!#@n{lmA99(-n+p*?XB_FzH1_4ZQWS6?})55lC{uT#i6cmo0cK#Dn8e}&UoRhDBS2wP{mh%F`t5KP-wIH'
    'GM5*LZ{yLUBm!tp?2Q%T$CS?Lu;mvgG=O3`4iMK@A=&0f&o2aD&<%h>B%)yACvkvsaUsaNv@hCmvV!gXWfz3^7c1Lw+-hMS-2P%z'
    'HkDo?%`tyLApm*spYeC%r!&ApZM2lOQSy$a6Wj(k*t&3|giWayV}%Nh%-hUgaK4xW%EWiuca4h%l!mBQd~p2GIi-5h<73ZI^wgA+'
    '_6yDtfL%7AG;v#46$r3i^o+1)!h2jvd1PbTi4*V~+gUtLv^U``lM+XQ1*c6r8^c*y0;Ew5UaXLKu~FF=P~-X{*;Si~Z6l<yYO{FT'
    'L~iRy<_j0T=yFhoU|AVaQ!{aBnzAvd1*3;sR2z|vCD>>R&<3)UjeEr|ehgmt3n~eW+WW=S3$=H_)JwH@$yB6F?crah;+!hY%+vy@'
    'TB2tvE}XYW<5`T6E_BgKR=cO(sy*k4hYH*gsWjkXq!%2nzzR!yu73Z`sMX(&I)zarqrysyH5Fc1M*0%`6fj!S{_E~v{B)u5Pa%p-'
    '88GIv=NN1@7wngGo{Vj5fCv?$cR&(N%kW+$n1@R03u6F+Z!&`!6zHMT4ZgNP(O*ixEo|%PIGv$aY-lYQg|yPN+|Kf-fsZm-i&r;b'
    'j5-#BAs+JbEgUOq2C!z)Zwm{>F%b@2|DK((8x|V2Fh36@?<;UU(v*e!Rr9`Ev!3_1y`qro%(kDXaAVtPT1H`Sf7sHZhek8p=i|rr'
    '+4g<^*8W;psawZjmTR~0q;2Cdf)-P>n7oAxvHxN_Tyfqu)_P6ZjqRditoI)Zuyt!Jfx&pU#(KfzChyRW9lvFN1?<DWd*b&AmH__!'
    'q)M9NI{X_8aZxToVcUhkWsCW9q*f|+Y2);uDq(4+{!Fk+b*E=B!zClK<Yj$ZqYle$EKw!B_o)2YA4dNI;yhSlsFeM99Q*)11Wa6j'
    '#8@I1(dC&4-KF#Nhu!7k_a2NdFLw6cA?v=EUkNqS_9@XpKH|)-+r2)7bWs4#qHLB|?1ej<e4buS_tR0J|B2?+rx!soo(a)W=~02b'
    'RGk<l0D7H~%E3ZS@8Wj6;C8Ig+FvxVu(`<Gt}juGZ+4+f6dv~zN23e<^i=aXk@6>q8FFkTIyem_z34$#!b1z&d&f+d?K7uX4Tfg2'
    '{}BQ~+-&A>3*g#z0rsJEa`FDu?S1I51D4WuxR{+G@Om?xHIP`C#{mJ5BuAp80=A2-FBz5Mn|Usd1dh2>-3I=0OXoVf?zUF1gY)n)'
    'AbJs!d4<5CICx#RpHHIP7xQR1CpGJ|kqD}9<KL?K?%Wxl2*oG9793HDr$v1Y8fgoUo>qgnLtkGIfJN%PvkR-EISvJHz}G2yRYEq&'
    'DI&2tB_H8+HuSR?d^h)_^RwwF;AX2m{L9Dy&Z0a@!P-0ASi0ae_%Gly_%BR-P<szd9edO=X6n7#yO)e~Fkks;jA;jePq*)xnoS}<'
    'ReQI9dY+LV;f?$Rv4;jIT|i!trIw0BLRe}CwKtnFHIEVyWRE*BcU2vtE2xVot7?v>JT%3=yLJM$AY1rBq)Db!jn;YUdxH}XmtUn#'
    'U{zze9%_#^MYt2y3V#?!Ks1jFj{1;02wZn^)6BEQ7S9mtZYABPatL?o020?eb)H!4+Gbx0C{8~PAcA=`8pS~zC3&VT1Yy^J^Ljpg'
    'Ei-G-!}2ohM~!pcjx!JEm9aY4?IfRQPx_{^x^9QjIE`Qpo0v<cnZb2?f_M=oNX4`Z_6sI1E*(S&ME&457bGo^kY7dZ7ZbsJYS;^!'
    '+|ajwi9$a$ZH>2@dh3@cG*StKkF^RgO9nGV+4^XRU^oTO&19)1cmm3o{?r4$GA)e)_Q)=B_A3|sJ=oCZz-e&h$c*Bnhvu(-X%Pvk'
    '6mYkHVeqC(tX&7(b1peke;8rL2=xC*|4m|{Oj!i4ZvUtf8Zf(ia#D`tsSW2-NFm)3h*_tx>cPKe$F+GV)~8mZ*=dY=oeuuEHrF~d'
    '?obx>m%quKe3pc{mY*t<g|%cvq3_B55y(dB>VMB2_CGhVKX#i4)WnV^YDm422*Qc@dRYE>TeG?i+LL>=ys-FUzsva?R@nz;?SUA7'
    'GfEEY3lGYPkqNIaeIW%BUu#;`zHl<ufYQOiJ#dGY7&jY@FD0z#tM&?*UAERb!S&1D7wCPV-Zk~m_+Xi?qKc(ek;Zy#f<Wv2r_^@D'
    '5q^_`XBs8EXvqM*fumjlJ*DVmfU%MRtPOxIp0}+)CQivm;nG5rEO6-E3fn~)4KBEKzx=2%v1REub;;ZwHGrxnC1&42e8GX-@cu)&'
    'h}ThwcLz}l&Y+*<N)TbJ7>5crDf5v6nqRrSyE**&<@63i3uP5e=RusmGG#GcW=fteBaz0EwQ!rS-O46@pMc*d;`amp&+XrvWm3<q'
    'vU+D$S>F2n0pf`&6n}=|&rtmPO9paiPgd9pf1l{@bLGK8I8<Gl^h1+sOR6<_$Eqq0L8PmZmVhk*mIP1^lVINr+iwn=LI2IPm(5l4'
    'rR=#kn|5eoVh{>iXg1y;WHK6WroL@;fq87SsL>RSJghW@b9QEKmq)ihwu)A(Y;E0}4GE~xuxb(nh(sjEM~<!L7nGaQFFQ5ui@Y7i'
    'qmh>D?QA*Bv>Z%&|J175!H8Eq+ajwRrx|(#eUaCd6z2b5J%kh7N+`l#DGZ^x>RL_vW;7-`ssy*Gp&~dn8%uI|t6dqcY>g0cO%qPA'
    'zoiMqGq$i=<?`co1&zp>0&6(oC5z*)A~WK<PStSLM8a@=Icb1ZB4{y*3!nQ@kd=duLWUm;AGd;jTG&Eo!MM_&dBU8vZPSuC7!gv)'
    'j_GT>7C@4mA{;D~NR^uJZhe&W7uxcOeUY;Gdm>AbJlpR9zZnH&OW-VB?IX2!#MCcp?@Q_Tdf(LEH-oAfIGu44g<dxC7m@I4@h?+}'
    'BXDT_Y5Yb$EqW$uZz4IeoWB~3q>R)atUFWVB#6TZ{BsZ0yANc6rw)EUO+B9E-q-@a-jdMrnWHQKlE9IsDk~-{n|WP$$9@`+&orBd'
    '#cc*Abm$af;NbSh{%q#+1|Cab5~KgacGg1MeUQq*ydWTiur!S!c2avkF!y1CsmuHGG>lTaQ^iuefgi><J8v|ofvP_+8pUC6{U6Rw'
    'Roule6^i_dg`F{vc|0fdqqv?q0S7PA`^WZKk*GSCLo-S^oMCF~*kumB2!Wbe)C@*kH}0V>1o>eypV^LZ%qv94jWwP{!~`YFW!PZ4'
    'gp4<EOxiuwTF02_t5)m>C+)FJjcp&x88n!a1Kdy8*`(qUJL-(e=izKpSC#jZmS6{zYU3C+YmorC$Uk;+H!@&iGerjMBBv}>!!}zv'
    'pErC$9Sc9pF)Bz193V`fs|%Fi9Ae3+yx}6L3q$VTvW28X1A8MbDpW-PtNVw+#E^ie{&9vvY5l2Em)heHs*DF>)xX5@z^o|L-fBJt'
    'U9Pfwn4xGpdsEr5s6!N)#(^g}8Y)8@g4e2>SH}Hpxxg1z^&7nSqiEo7uaJdQ(YBJ)jK7lKjMe9=8EjfHL}aXrj_T@u^WM26vx-cK'
    'R|t883+2U02D_!Q5qKb{|Ncew;zL?Eu`8J-Axk10DiTTy5JgE!$^==Z{#0;LM)HG$Dknt@2+ojjwsJwDYNT&GjKUk<I{n}+;ZA_V'
    '1%InIQ2^-H;G|IQeYit>6*)n?`4F_Bl#b^K(S~jr(1%h)i!&69<bwyu7ptr%V%ad~=aD+h>_2Pw^Y}VMGjU$6rfKQeLzNP@IzCv`'
    'YKOP%$MmpxoI?|EwG+{5)gxj4P(_#zS;~uxo%u8@ht(7b<$k2BN#e6)XjeD#tSC<KzLQOcb|IzMS(Ybm{aVw}#5xJTV`DXo8%^FS'
    '!}tQ`!@EsI(Gnk^L5nq#A@(;WeoJcedE4;)u;C_1OKK}nxplEb$8xdZSmJ9FSWLQo+!RxkFuZ(xCwhfDMWTl(D^QIuU{EF5;g@ml'
    'yP*r=#4WbL>e8rMwkZRRm&|9Nh}#n%d}jUq+$7|bnI`dmVuS?`VP6PL?dDVTvtnAZMSp*?%lk}@9c2xUskl8}>5WCr?BS^;tAGzi'
    '%zct{Y^#(@<vB)+%sx82E=74k&lYg7Y>pOA-IBO{9EbN1@Jn`RTeBLPNsl0W2rK0GS%G8rFiTOR(f9--Kb2GG^W2|G7yJJ%8Hr6Q'
    'N^hA}j1Z-X?I0lm=&}Y((`Y<3zG?XEM|);ZI-^norFV(KXHa_Lky_Q5P||Qi%8+-QN&my>16f$i@+eMJ*T!<67-|xA1jZK|qblLw'
    '6yX=pC;LH<ZvP@eA42Nx(}f@m=2%t{dx}^Zl^281!{8sk9E>dJwV>N7uLq0%%_~CCegMwH4JgB~@{SOysp!J{pmlLaxZb!Utlfp-'
    'JQq=Ua^$-j$1QJIHZSO1TiSP8c1^uinfe|6ovONY-}3C*@0~P}8TgeKD|_5XwkLc=6aL@}wTV!$r7jgaim6ij@6x9AFbJ)O+QYw0'
    'g<XlKV9k0c{@jzo2l@d<6+f8lTJ`REl}9AA`HaGvGx_?Va63lv8dLV?Oa;|EA4f?vUuGUCk13!zuD4dxkq4|+^+yS{U<?*3%}atr'
    ')}Zu*!O`ZgEpmEp0is8*cO*2VK*M+i`a_DIL;=FHQmv@Hs?5mbgVu~;+0`DMWeI0_u~MEKj~=?HJvuo|#obVQ_*cI7NW#TDMyNmW'
    'RtE)+NRK$_ksuv!c;J-OZ+4<>Y}&Y+`S^b4uj0mJ3Tx^Ko?eT4lYc1JVw3^_Xp-UA0ud_MaX!iVN<N7*d;o_DxDgy&C5w~sG-?HN'
    'utE6lFjBH*I`RW_G4g1f`cs~C3#Tkh+0<au6`PuD$?$F^qYnu(O%10?m?~34nXZ(nsVtRKl@-+UCwSaZl0H6oQ5go-Qtvbx<+i4o'
    't)<?W8qH-xo35HKx(;H{lAEV1Y~u2d5q2?#gCl@h8?!2#_^Gm6rwuKfHnO&05!3iEH`A63EwkPX(^@CZQugZG`_fHvflLF^EF=vF'
    'Yg3a~^v27!)#V`20aa?Kr$vNg{?y_a%c!qB+$a>|$U75JdNl%sX&NVypKjzO2v3{Zv=_V{tC?=~*U}GxF^HXhH_QU;;9tOmYBpb{'
    'LDa&)LmA@hTt9v7gGiv`3j03uU%{{`s5_P65?ET!lw$W)A+7wQ9*wS_OHn<V&%jv*nTyt-4Imy%VyJ|124^EmUzIU%oH6C{>JA`+'
    '=@P$tQ5NZZKFYXMp4i1#H~ophCMKI$Y|^n$`0Jq){$S{YzXm#?hdq7%+*<g@6uIF$j$!C4Yxdg1G(qDPQv;YEfRa%;(s0t~4$?H3'
    'Ww4IHx(3@d+>O_K&WRR7^pNP)>qc&=p>2B`BJu_lYDSxKm@Lc4tKgp)X^0BW$0G7`+j{R~rna4By?5`g`8AQF0msNMeepo$i9sd!'
    'o8p@&Sg0(+LJ7F>xMX7KoBp#Rpj#7b1Gt<B&=U+)CLK|9H%UjA6|FW8nzhf47Gp5CkGZ1OXNXDB<(FDb(Q3NyNh(Prc&ox9;bc;u'
    'S?dFg;2>>o6U18|FD!aTL^F~jQK-Mi;PwycDQ{S0uZ#cAUU@rUXlR11W}T!D=-J+_A;Hvf;mUpnFH%}KUB>!E__q0%JORHx$4{s_'
    '^l(Uga3vlzi2HSPMgk^$;_dF{-krUEg4pKc)qz8s+S*~O+rT6=DBEUtzj5{oPB4A>rV&6}1W|JcVZyN1LqQB$An1E1GmYdw><t8@'
    'd%{K-7CjPzk4f}xt##NW`kE);VuxX=%cZ%DPsJ+}@w8DdG6tkM-bZ%gqX!;86=NX0OYse@dUEys@)%4Ve<e8r9X63n-p1VYm6!PX'
    'VW-FSKfnFw$d0cr2P&(ebgo<JW6Ht-z|ST@Qp?wwZ!oRMI_N^xKojzVpK|fznMC7vL*75!+!%g2_`*k1%Ay*-`3V<Z!ueoJcxFR9'
    'Hbn&Dqp8~EfrHGY8wrYARUC_yR3tEnPWwIx@IHR>_rD|f{vm=LwnJZP?bHxpFXprHcFVTEY5NDPyTfle%dRTJju2g-;h_E@3$lv2'
    '^miFs{%{Zm?e6TGJG;Ba{vPY>9PC(zxoe2`6Mh<i8Nrmln6TVGhK&XCaz)*`w@`S5V7LDdAN;Dc<Kzc8{A*8Eee@~68b;qR_k!1e'
    '-a;QeG8HdtJ^E5a?a`}V>03j*AK`8k-k#*>?~ZBU-OX1CDe>nayPgmu^va=H$)Sf{i&qGv1O`p=oei!@+3Up#xDDXgj=lV4?iEks'
    '=y8r0_!(Wa;0UJTs;fQx3kyrGHQfhodf9&!pPN94Elymq>6qwF$17Bx6evRAjR#Y8nWNH|&Q#j?+F5QxhE=yr=T`{bc9uhwl)c3H'
    'L=(`e<P`|#N*Z9>?<Ugwl0umepKPHv`goJ1;g`tma5-CGq)cD20SFvk2uHo==rtpy#j*&u12k-AYalTUWDMM8^}iEUZ;N4i`FsmM'
    'tJc)om)|&x`VoUbFJG)4KFfMZL4Lg9YaZc8Z{p%xe&2{d5Iuwf2Gk{h$(r)y>&e|<aOoW$-F+AGe*^-5b9H{}-Q9d2co&Dax8C{T'
    '-QCxt0iB8K!=rx=?r!1t_EwN6aKSk^JU<_td*8kv9($nBZ@feA`uzJXK4-(BcR#MY)5DvK^8w)eIk>s1=6a6}fq$G{oe#XLAC~}l'
    ';gzTKX7J_v`5_$5!@I9nK>N+nM+i>7pPzddUmpg?-o@1go=~LW=<53X@Dc{!J$knTnE%*2+hC_uys)zlmv_l|<=B0PrxHNBeEEKO'
    'b9~FqjqlU~W^l#S&x4!G+q=QnOO;XY-$cxSXmEW?FhyR%mD$0aO#E3y)8Jk+@ojuNoA}nwF158M(K?Jl!IU>UVl8S4?grStAKW|^'
    'JcERJ9^$4?<vkD2tmi>!O=oxOe*ljHT$}'
)
b=zlib.decompress(base64.b85decode(DATA))
assert len(b)==16657
assert hashlib.sha256(b).hexdigest()=='9cbebc12e390ae34d7a645a1a9ffcb45581c3937865626a7dff9feeb0d7bdbfd'
p=Path('nonbasal_e17.py');p.write_bytes(b)
assert sys.argv[1:] in (['build'],['check'],['extract'],['locate-negative'],['locate-pure'])
if sys.argv[1]=='extract':print('NONBASAL_SOURCE_EXTRACTION_PASS')
else:subprocess.run([sys.executable,str(p),*sys.argv[1:]],check=True)
```

## 9. Remaining frontier

The useful remaining two-apex pure-four-A cases are now: a single adverse positive-beta packet competing with one or more negative-beta packets; an apex-source contact exactly on the actual centroid-height wall; and a horizontal ridge with three basal contacts for which all free vertices are target-side and all explicit linear moment coefficients vanish. These are necessary overcovers after the new automatic tests, not assertions of physical realizability. Existing full constrained affine/projective and intrinsic second-jet tests may close further members.

The whole adverse-packet stress cone obeys(3), providing a concrete target for a further contact-preserving actuator. The horizontal target-critical architecture has the exact simultaneous quadratic boundary(11), so repeating independent frozen-star tests there would lose the relevant coupling. A useful continuation should either vary the transverse base coordinates or the weak endpoints, or prove that an actual uniform-centroid body cannot meet those critical equalities together with all physical packet guards.

Non-B8 E17 incidences and mixed/VF configurations remain separate. No positive tensor stress has been promoted to a physical all-orders obstruction, no finite failure has been promoted to a universal exclusion, and none of the new constructions changes34≤C_min≤622.
