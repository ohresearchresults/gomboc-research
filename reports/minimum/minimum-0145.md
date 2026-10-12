# minimum-0145

AI research report · 2026-09-20 UTC · [Export notes](../../catalog/coverage.md#text-records)

---

# FOUR_FREE_QUADRILATERAL_MOMENT_SUBMERSION_V1

## 1. Main result and scope

**The forced four-free-quadrilateral-endpoint sector is closed.** Every actual unequal-height two-apex E17 body in the stated sector—one weak ridge, two weak spokes, one weak basal edge, and all four quadrilateral base endpoints avoiding the weak edges—admits genuine own-centroid regularization preserving its full maximal-face lattice and exactly its original strict feature-labelled equilibria, with no additional equilibria.

The underlying theorem is stronger and independent of the contact count. With the apices and all internal basal vertices fixed, the six genuine coupled motions of the four quadrilateral endpoints make the actual map

\[
P\longmapsto (\operatorname{Vol}P,\;\int_P X\,dX)
\]

**a submersion of rank four at every unequal-height realization.** Its proof uses the actual uniform moments and convex boundary order. No genericity, sampled rank test, independently movable quadrilateral endpoints, or freely assigned shadow moments are assumed.

Consequently, **any finite pure-A set is first-order regularizable when all four quadrilateral base endpoints are free**, in this two-quadrilateral roof class. The entire nonnegative intrinsic stress cone is zero; this is not a statement about one chosen stress or about the dimension of the signed stress space.

Together with the accepted parent reductions, this closes every pure-four-A two-apex E17 case having a weak ridge and three nonbasal weak edges, whether or not the four-free-endpoint incidence was initially apparent. Cases with four nonbasal edges or at most one were already closed. A weak ridge with exactly one weak spoke and two weak basal edges can still remain.

A new exact body realizes the priority incidence as **pure four A**, not four A plus EF. Both quadrilateral planes rotate in its certified actual-centroid curve. A second new actual body shows that the stronger claim “the four radial motions alone always give rank-four volume/first-moment control” is false. That second body still has rank-three radial centroid control, so it is not a regularization obstruction.

The formerly omitted complete 17449-byte `two_cover_free_base.py` is restored verbatim below. Its two earlier controls and interval verifiers are no longer dependent on a truncated wrapper. No minimum bound, registry count, or attaining construction changes.

## 2. Source authority and verification status

The complete 1706-line `research-journal(20260920-213917).md`, including its entire literal parent, was read consecutively through EOF. Its 316338 UTF-8 bytes have SHA-256 `5657679a4cf0e6882a08c97ce4dca799851eb8b02f22f3f405e5b415fab97ce8`.

The authoritative parent is `minimum-0143`, `TWO_APEX_COVER_AND_TWO_INTERNAL_REGULARIZATION_V1`. Its compact JSON envelope authenticates at 37539 bytes to `c38b1e713ef30a6ad4e9d6b5bd5eaa3d1354bb762a26e5a80862f5ca9cceed15`: UTF-8, `ensure_ascii=False`, compact separators, keys `version,result_markdown`, one final LF inside the Markdown value, no envelope-final LF. No scientific source conflict was found. The parent explicitly identified its truncated inline computational capsule; that is the specific dependency repaired here. :contentReference[oaicite:0]{index=0} :contentReference[oaicite:1]{index=1}

The complete mounted source and recovery wrapper were read. Appendix A is the unchanged source, with its original hash, not a rewritten substitute. Earlier build/check receipts for its two controls remain inherited; they were not routinely replayed. New `four_quad.py` build/check and a fresh two-source-only build/check were executed and matched byte for byte. The universal theorem below is analytic, not inferred from the controls or their finite certificates. No proof-assistant formalization or literature-priority claim is made.

## 3. The genuine coupled family and its actual uniform moments

Let B be the true basal polygon. Assume its only nontriangular side facets are the two true ridge quadrilaterals; all other nonbasal facets are triangles. This includes all three octagonal-base E17 types, with apex degrees 3/7, 4/6 and 5/5.

The unequal-height ridge meets the basal plane at C outside B. By an affine coordinate change, put

\[
C=0,\quad a=(0,0,h),\quad b=(0,0,H),\qquad 0<h<H.
\]

Use the two basal supporting rays through C as coordinate axes. Write the near and far endpoints on them as

\[
p_1=(r_1,0),\ q_1=(R_1,0),\quad
p_2=(0,r_2),\ q_2=(0,R_2),\qquad 0<r_i<R_i.
\]

The p vertices are assigned to a and the q vertices to b. Let u_i be the other basal neighbor of p_i and v_i the other basal neighbor of q_i. All unlisted coordinates here are basal z=0. The required transverse coordinates are positive: u1_y,v1_y,u2_x,v2_x>0. A triangular block of length one is allowed; then its two endpoint-neighbor labels coincide with the opposite endpoints.

The exact six-parameter family is

\[
\begin{aligned}
p_1'&=(r_1+s_1)(1,\theta_1),&q_1'&=(R_1+t_1)(1,\theta_1),\\
p_2'&=(r_2+s_2)(\theta_2,1),&q_2'&=(R_2+t_2)(\theta_2,1).
\end{aligned} \tag{1}
\]

Keep a,b and every internal basal vertex fixed. Each pair remains on one line through C, so both maximal-quadrilateral coplanarities hold identically. Every other side facet is triangular, and the base stays planar. All remaining strict support and polygon inequalities persist in a neighborhood. Thus (1) is an actual open realization family, not only a tangent-space description.

Let K=conv(C,B) and G=closure(K minus B). K is convex; **G is the actual generally nonconvex visible gap**. The parent’s shadow-minus-gap decomposition gives the actual body as the outer radial cone of height H over K minus the inner radial cone of height h over G. In particular G is not replaced by its convex hull.

Write A=area(K), D=area(G), I=integral_K p dA, L=integral_G p dA. Uniform radial-cone integration gives

\[
V=\frac{HA-hD}{3},\qquad
J_B=\frac{HI-hL}{4},\qquad
J_z=\frac{H^2A-h^2D}{12}. \tag{2}
\]

The moment decomposition is the accepted parent’s actual uniform construction. :contentReference[oaicite:2]{index=2} These formulas follow respectively from the integrals of (1-t)^2, (1-t)^3, and t(1-t)^2 on [0,1]. The centroid is exactly J/V. For simultaneous motions, A,D,I,L are computed by the **full polygon determinant sums** of the changing shadow and gap. Every shared-edge cross determinant remains. The affine normalization preserves uniform density and transports the actual centroid; M transforms covariantly and N remains its inverse. No projective transfer of an old centroid is used.

### Six exact moment directions

Use the four radial endpoint motions, and for each quadrilateral use the angular motion with radial compensation making both its shadow-area derivatives zero. At the first pair the latter velocities are

\[
\delta p_1=(r_1/u_{1y})u_1,\qquad
\delta q_1=(R_1/v_{1y})v_1. \tag{3}
\]

The second pair uses the corresponding x coordinates. These are genuine tangent directions to (1), not separately chosen transverse endpoint motions.

For a lower radial direction, its nonzero volume derivative is a negative factor and

\[
\delta J=\frac{\delta V}{4}(a+2p_i+u_i).
\]

For an upper radial direction,

\[
\delta J=\frac{\delta V}{4}(b+2q_i+v_i).
\]

For (3), and likewise for the second pair,

\[
\delta V=\delta J_z=0,\qquad
\delta J_B=\frac{H R_i^2 v_i-h r_i^2 u_i}{24}. \tag{4}
\]

For example, at the first pair the two radial volume derivatives are -h u1_y/6 and H v1_y/6. Equations (3)–(4) follow by differentiating the actual triangle determinant and first-moment contribution, not by fitting masses.

## 4. Universal rank-four theorem

Suppose a covector (lambda,nu), with nu=(w,nu_z), annihilates all six derivatives of (V,J). The radial equations are

\[
\begin{aligned}
4\lambda+\nu\cdot(a+2p_i+u_i)&=0,\\
4\lambda+\nu\cdot(b+2q_i+v_i)&=0,
\end{aligned}\qquad i=1,2, \tag{5}
\]

and the two angular equations are

\[
w\cdot(HR_i^2v_i-hr_i^2u_i)=0. \tag{6}
\]

We show that no nonzero annihilator exists.

### Lower-chain order fixes the sign of the basal covector

Convexity implies

\[
u_1,u_2\in\operatorname{conv}(0,p_1,p_2). \tag{7}
\]

Explicitly, their coordinates are nonnegative and u_x/r1+u_y/r2<=1. At p1 this last inequality is precisely the supporting-side condition for the edge u1–p1 evaluated at p2; the second endpoint is analogous. It remains valid for a one-triangle chain. It does not assert convexity of G.

Let f(p)=w.p, A_i=f(p_i), U_i=f(u_i). Subtracting the two lower equations in (5) gives

\[
2A_1+U_1=2A_2+U_2. \tag{8}
\]

If A1>=0>=A2 and A1>A2, (7) gives U1-U2>=-(A1-A2), so the left-minus-right side of (8) is at least A1-A2>0, a contradiction. The reversed case is identical. If both A values are zero, w=0 because p1,p2 are independent. Otherwise, after changing the sign of the whole annihilator,

\[
A_1,A_2>0,\qquad 0<U_i\le A_*:=\max(A_1,A_2). \tag{9}
\]

Thus f is strictly positive on K except at C.

### Upper-chain order contradicts an angular equation

Put P_i=f(q_i)=(R_i/r_i)A_i and V_i=f(v_i). The upper radial equations give

\[
2P_1+V_1=2P_2+V_2. \tag{10}
\]

The following elementary convex-polygon fact is decisive: if f has its unique minimum at C and q1,q2 are C’s two neighbors on the convex shadow K, then (10) implies

\[
V_j\ge P_j=\max(P_1,P_2)
\]

for an endpoint j attaining that maximum. To verify it, assume P1>=P2 and V1<P1. Equation (10) gives V2-V1=2(P1-P2)>=0. If the inequality is strict, choose a level between V1 and min(P1,V2). Its superlevel set would meet two separated boundary arcs, with both v1 and C below it, forcing at least four crossings of a line with the boundary of a convex polygon. If equality holds, P1=P2 and V1=V2<P1 gives the same contradiction using the two endpoints. Thus V1>=P1. This also covers a single internal neighbor or a one-edge upper chain.

But P_*:=max(P1,P2)>A_* because both R_i/r_i>1. For this j, (9) therefore implies

\[
H R_j^2 V_j-h r_j^2 U_j
\ \ge H R_j^2 P_*-h r_j^2 A_*>0,
\]

contradicting (6).

Hence w=0. The lower and upper equations in (5) now give 4lambda+h nu_z=4lambda+H nu_z=0. Since h!=H, lambda=nu_z=0. This proves rank four.

**Minimal actuator consequence.** The four radial moment columns always have rank at least three. Indeed 2p1+u1-2p2-u2 is nonzero: apply a functional taking values 1 and -1 at p1,p2 and use (7). This difference is purely basal, whereas one normalized lower and one upper column have independent volume/z-moment components. If the four radial columns have rank only three, at least one of the two coupled angular columns raises the rank to four. Thus four selected scalar parameters suffice locally, although which angular parameter is needed can depend on the body.

The theorem has no uniform conditioning bound near height equality, a collapsing basal side, or a degenerating true lattice. Those limits are not silently included in its open realization statement.

## 5. Elimination of the whole physical intrinsic stress cone

Assume every physical weak point is simple A and every quadrilateral basal endpoint avoids **all** weak-edge endpoints. Let R be the actual contact derivative on the full true realization tangent space, including actual recentering. Let alpha>=0 satisfy R^T alpha=0 and set

\[
c=\sum_i\alpha_i u_i.
\]

On the free family (1), no weak endpoint moves before recentering. Its weighted contact derivative is therefore

\[
-c^T M\,Dg.
\]

The rank-four moment theorem implies rank(Dg)=3. Hence Mc=0, and c=0. This tests every full intrinsic stress, irrespective of its polygon reactions.

### The two-apex height identity removes every nonbasal stress weight

An actual affine metric motion with derivative nn^T, n=d z, yields

\[
\sum_i\alpha_i(z_i-\gamma)(z_j-z_i)=0. \tag{11}
\]

It is realized by affine images with one reciprocal M,N pair; it is not an independent metric assigned to a fixed polar.

Group the weighted height increments by source level:

\[
D_B=\sum_{\text{basal source}}\alpha_i(z_j-z_i)\ge0,
\quad D_a=\sum_{\text{source }a}\alpha_i(z_j-h),
\quad D_b=\sum_{\text{source }b}\alpha_i(z_j-H)\le0.
\]

Basal-to-basal increments are zero. Since c_z=0 and (11) holds,

\[
D_B+D_a+D_b=0,\qquad hD_a+HD_b=0. \tag{12}
\]

If D_a<=0, the second equation forces D_a=D_b=0 and then D_B=0. If D_a>0, it forces D_b=-(h/H)D_a and D_B=-(1-h/H)D_a<0, impossible. A simple A source has at most one outgoing weak edge, so D_a=0 cannot conceal cancellation of two oppositely directed weak packets at a. The other two groups have uniform signs. Thus **every nonbasal stress weight is zero**. This argument also covers the COM-height wall; no division by h-gamma occurs.

### Basal weights are impossible as well

All remaining weak endpoints are internal basal vertices, whose planar motions are genuine. Let o be the M-orthogonal projection of the actual centroid onto B and p_i=v_i-o, rho_i=p_i^T M p_i. Move each internal basal vertex with velocity rho_i p_i, leaving the apices and the four quad endpoints fixed.

For a basal weak arrow i->j,

\[
p_i^T M(p_j-p_i)=0,\qquad
\rho_j-\rho_i=|p_j-p_i|_M^2>0,
\]

and its fixed-reference derivative is rho_i(rho_j-rho_i)>0. Here rho_i>0: if the source were o, its radial plane would expose the whole base facet, not the stipulated simple VE edge. The actual centroid correction contributes -c^T M g'=0 after weighting. Any nonzero remaining basal alpha would therefore give a strictly positive weighted derivative, contradicting the stress equation.

So the **entire nonnegative intrinsic cone is {0}**, for any finite pure-A set satisfying the free-quad hypothesis. No signed-stress dimension claim is used.

### A true nonlinear curve and full feature control

The strict finite-dimensional alternative supplies a genuine realization tangent h with Rh>0. Integrate it in the accepted local rational vertex/pole incidence chart: reverse a degree-at-most-three peeling of the planar incidence graph and solve the selected nonzero linear minors of q_f.x_v=1. Every nonempty bipartite planar subgraph has a node of degree at most three. At that node the remaining neighbor vectors are independent: they are at most three vertices of a true primal or polar facet in a plane excluding the origin, with no three collinear. Reverse elimination solves precisely those linear equations using a nonzero coordinate minor and leaves the other coordinates as parameters. It is a genuine local rational chart, so it integrates the specified tangent, not merely some tangent of the same dimension. The resulting vertex family Phi(s0+t h) satisfies every maximal-facet coplanarity identically. Integrate its actual V(t),J(t) and subtract J(t)/V(t). This gives an analytic curve of actual uniformly filled bodies whose contact escapes have positive first coefficients. The moment submersion alternatively permits an analytic implicit-function correction keeping both V and J fixed.

All original strict support and polygon inequalities persist. For each absent physical packet retain one of its originally positive excluding primitives; for every old strict feature retain its strict defining inequalities. At each original simple A packet the positive escape is the side that creates no new strict pair. Thus the complete original strict feature labels persist and no new strict or weak equilibria appear. Harmless primitive zeros need not individually disappear. The argument does not apply unchanged to additional EF or VF packets.

## 6. Exact priority-incidence control and a whole certified curve

Use the following raw vertices and outward maximal-facet cycles:

    0=(1,0,0),       1=(5/2,0,0),
    2=(2,1,0),       3=(1/2,3,0),
    4=(0,3,0),       5=(0,6/5,0),
    6=(2/5,3/5,0),   7=(4/5,1/10,0),
    8=(0,0,1),       9=(0,0,11/10).

    (7,6,5,4,3,2,1,0), (0,1,9,8),
    (1,2,9), (2,3,9), (3,4,9), (4,5,8,9),
    (5,6,8), (6,7,8), (7,0,8).

The actual raw V=943/600 and g=(5485/7544,8917/9430,2095/7544). Put X_i=raw_i-g. In the coordinate order xx,yy,zz,xy,xz,yz, use

    M=(373094793869173/419044326678741,
       230600529690818/419044326678741,
       1, 2/3,
       349001372152703/698407211131235,
       53026476595170/139681442226247).

This means the symmetric matrix with those six entries. Its positive upper Cholesky factor L defines the actual Euclidean uniformly filled body L X; N is exactly M^-1.

Its only physical weak points are

    8->9, 2->3, 6->8, 7->8.

All four quad endpoints 0,1,4,5 are free, and all four internal vertices are touched. There are exactly four zero primitives, all simple A, and 64 other nonzero primitives: no EF, VF or harmless zeros. The beta values in that contact order are (5449/75440,0,-2095/7544,-2095/7544), so the ridge is genuinely the unique adverse packet. The strict labels are

    S=(0,1,2,3,5), U=(3,9),
    H=((0,1),(1,9),(2,9),(3,9),(4,5)).

This is a true balanced5/5, 10/17/9 body with strict5/2/5 plus four A points, not110. Its contact tensor rank is four; it is **not** a realized surviving affine or intrinsic stress.

### Both quadrilaterals rotate

Set theta=-125423/49428 and define

    r0(t)=1+8t,
    r1(t)=5/2+(8531817/1510300)t,
    r5(t)=6/5+(135687/13730)t,
    r4(t)=3-(10355946/377575)t.

The complete raw curve is

    W0=(r0(t), t*r0(t), 0),
    W1=(r1(t), t*r1(t), 0),
    W2=(2-3t/2, 1+2t, 0), W3=(1/2,3,0),
    W4=(theta*t*r4(t), r4(t), 0),
    W5=(theta*t*r5(t), r5(t), 0),
    W6=(2/5+2t,3/5,0), W7=(4/5+2t,1/10,0),
    W8=(0,0,1+t), W9=(0,0,11/10).

Integrate the complete actual V(t),J(t), set X_i(t)=W_i(t)-J(t)/V(t), and keep M fixed. This is the actual physical body L X(t). Both quad couplings are exact; no mixed t^2 endpoint product is discarded.

The radial/area-neutral angular six moment columns have rank four. The selected correction minor on columns (1,2,3,5), zero-indexed in the source, is -166133/2560000000. The four-radial minor at this particular body is -847/82944000000, also nonzero. The raw V' and J' are all zero, but the actual raw centroid's quadratic coefficient is nonzero:

    (730873150719384951/36879679718662000,
     -388041511528293279/18439839859331000,
     -67841418568403/670539631248400).

It is included by the exact recentering, not treated as an adjustable center. The four positive escape first coefficients are

    1/10,
    342752393015789/1676177306714964,
    2467668741520753/10476108166968525,
    1617536569975876/10476108166968525.

**The entire interval 0<t<=1/2048 is certified.** There are 216 polynomial guards and 1666 strictly positive exact Bernstein coefficients, maximum degree14. They comprise actual volume, all9 centroid-side conditions,56 strict nonincidences,82 polygon conditions, and68 mechanical conditions, with each initial A numerator divided by its positive leading power. Throughout, the strict5/2/5 labels above remain unchanged and weak000 holds.

The source independently compares the boundary moments with the complete shadow-minus-gap polynomial identities, including the varying lower height. For homogeneous Z_i=V W_i-J it verifies J_homogeneous=0 and V_homogeneous=V^4. Every vertex/pole incidence is checked through its mixed second coefficient as well as by the full plane polynomial. Both starting and endpoint hulls are reconstructed from supporting triples and audited using two positive apex fans and the same reciprocal metric. Positivity is certified on the whole interval, not inferred from endpoint sampling.

## 7. A genuine limit of the radial-only strengthening

Use the same facet cycles but the raw vertices

    (1,0,0),(3,0,0),(3,1,0),(1,3,0),(0,3,0),(0,1,0),
    (1/5,1/2,0),(1/2,1/5,0),(0,0,1),(0,0,2).

Its actual V=913/200 and g=(35171/36520,35171/36520,5539/10956). With the centered vertices and M=((3,1,1),(1,2,0),(1,0,2)), it is a true own-COM 10/17/9 body with strict4/6/8 and weak000, fully audited in the source.

Its four radial (V,J) columns have rank exactly three. The exact annihilator is

    (lambda,nu_x,nu_y,nu_z)=(-23/146,-10/73,-10/73,1).

It evaluates to0 on all four radial columns but to -713/1752 on each of the two area-neutral angular columns. All six columns therefore have rank four, as proved. The radial centroid columns already have rank three. Thus this is a countercontrol only to the stronger **radial-only simultaneous volume/first-moment** claim, not to centroid control or regularization. Its full construction and verification are preserved, not omitted for being nonwinning.

## 8. Exact remaining complement

The priority four-free-quad incidence and, more broadly, every unequal-height pure-A body with all four quad endpoints free are no longer an open actuator problem.

For completeness, a weak ridge, two weak spokes and one weak basal edge touch at most four basal vertices, leaving at least four free. Two free internal vertices are already covered by the parent. If exactly one internal vertex is free, the parent covers a second free basal vertex on its own apex side; avoiding that test would leave only the two opposite-apex quad endpoints as possible other free vertices, fewer than required. Hence a case not already covered has no free internal vertex and all four quad endpoints free, and the new theorem applies. Parallel-ridge and COM-height-wall cases retain their accepted closures. :contentReference[oaicite:3]{index=3} :contentReference[oaicite:4]{index=4}

After all inherited reductions and this theorem, a still-uncovered pure-four-A two-apex E17 case has two or three nonbasal contacts, neither apex on its COM-height wall, and the unique adverse packet competing with negative-beta packets. There is no adjacent two-vertex cover. There is at most one free internal basal vertex; if one exists, every other free basal vertex is an opposite-apex quad endpoint. If there are no free internal vertices, at most three quad endpoints are free.

With three nonbasal contacts, **the ridge is not weak**: the remaining case has three weak spokes and one basal weak edge, also subject to the parent's apex-plane sign restriction and actual rho convex-hull condition.

With a weak ridge and exactly two nonbasal contacts, there is one weak spoke and two basal weak edges. At least three base vertices are free. In an uncovered case exactly three are free, either three quad endpoints, or one internal vertex together with the two opposite-apex quad endpoints. Thus the five touched basal endpoints are distinct. The parent’s equal-rho necessary condition for the two nonbasal rows still applies. These are necessary overcovers, not realized full stresses or nonregularizable bodies.

The next consequential step is the genuine three-free-quad family, or one free internal vertex plus the two opposite-apex quad endpoints, coupled to their weak-endpoint equations. The present proof needs both lower and both upper radial equations to constrain the whole moment annihilator; it does not establish the corresponding three-endpoint theorem. One pair’s kernel or a failed restricted actuator remains insufficient for a physical obstruction. General mixed EF/VF points and non-B8 E17 lattices remain outside the theorem.

## 9. Complete recovery, including the previous source repair

Save Appendix A as `two_cover_free_base.py` and Appendix B as `four_quad.py`, UTF-8/LF, each with one final LF. These are the complete runnable units; no journal, wrapper, report download, solver or external library is needed.

Observed environment: CPython3.13.5 standard library, assertions enabled, `PYTHONHASHSEED=0`. The exact inputs, all non-default choices and interval search powers10 through40 are literal in the source. The new body is reconstructed by four exact zero equations plus Mzz=1,Mxy=2/3. No numerical locator is required.

    export PYTHONHASHSEED=0
    python -S four_quad.py build > new-build.txt
    python -S four_quad.py check > new-check.txt
    cmp new-build.txt new-check.txt

New observed pins:

    four_quad.py 9921 bytes
    SHA256 26932469a65b3c99b0ded163568ff866199bf4f7ec75b62c703e3b62734c78cf
    four_quad.json 346832 bytes
    SHA256 044ae18f824d24430cdc6993f8b32ff636c62d16c3ac3ed2634faec331f24da9
    new-build.txt/new-check.txt 616 bytes each
    SHA256 d478abc2c136241a48fe1ba7868f6bbc774a12df02690334e94d6554ef1a0d9e

Exact new stdout:


[Encoded source block omitted; the code in this passage is incomplete.]

    EPSILON 1/2048 GUARDS 216 BERNSTEIN 1666 MAXDEG 14
    four_quad.json 346832 044ae18f824d24430cdc6993f8b32ff636c62d16c3ac3ed2634faec331f24da9
    FOUR_FREE_QUADRILATERAL_RECOVERY_PASS

Fresh two-source-only build/check also matched both the report and stdout, ending `FOUR_QUAD_SOURCE_ONLY_COLD_BUILD_CHECK_PARITY_PASS`.

The restored previous unit is 17449 bytes, SHA-256 `7fa5a6e8df8bf4100329515a43b973a8ce71a293b8f967a10be6f8a265e3080a`. Its inherited commands are

    python -S two_cover_free_base.py build
    python -S two_cover_free_base.py check

They reconstruct both prior controls, their two whole intervals, their full actual mixed jets, and the fixed-geometry invalid rho-tie form. Expected prior report: `two_cover_free_base.json`,295716 bytes,SHA `c5c40855fbc3ba96e1571184ba7689a73862b22cfc1b32b3627362da4a5ac5a7`; stdout763 bytes,SHA `fc9a0f437154df06f000e1108a16f316013fc1282221e3ace0f4c94a63813275`, ending `TWO_APEX_COVER_AND_TWO_INTERNAL_RECOVERY_PASS`. The old two intervals are 1/32768 with216 guards/1054 coefficients, and1/1024 with71 guards/271 coefficients. Their strict5/3/6 and3/2/3 labels are preserved by the unchanged verifier. These are restored earlier results, not newly discovered controls or a claim of a new replay of their old suites.

Convenience copies: [new source](sandbox:/mnt/data/four_quad/four_quad.py), [new exact report](sandbox:/mnt/data/four_quad/four_quad.json), [restored previous source](sandbox:/mnt/data/four_quad/two_cover_free_base.py), [new executed receipt](sandbox:/mnt/data/four_quad/build.txt). The literal units below, not those links, are the durable recovery.

## Appendix A. Complete restored `two_cover_free_base.py`

```python
"""TWO_APEX_COVER_AND_TWO_INTERNAL_REGULARIZATION_V1.
Exact recovery: CPython 3.13.5 standard library; assertions; no RNG.
Parent minimum-0140,
SHA256 12961fff59f36b67340a96fae45fd85d51081d7e75350828a246fbeac9b734d0.
Run python -S two_cover_free_base.py build|check.
"""
from fractions import Fraction as F
from itertools import combinations
from math import comb
from pathlib import Path
import hashlib,json,sys
assert __debug__
Z=(F(0),)*3
CY=((7,6,5,4,3,2,1,0),(0,1,9,8),(1,2,9),(2,3,9),(3,4,9),
    (4,5,8,9),(5,6,8),(6,7,8),(7,0,8))
TRI=tuple((cy[0],cy[j],cy[j+1]) for cy in CY for j in range(1,len(cy)-1))
CONTACTS=((1,0),(4,5),(8,6),(2,9))
RAW=tuple(tuple(map(F,p)) for p in ((1,0,0),(F(5,2),0,0),(2,1,0),
    (F(1,2),3,0),(0,3,0),(0,F(6,5),0),(F(2,5),F(3,5),0),
    (F(4,5),F(1,10),0),(0,0,1),(0,0,F(53,10))))
ED={}
for f,cy in enumerate(CY):
 for i,j in zip(cy,cy[1:]+cy[:1]):ED.setdefault(tuple(sorted((i,j))),[]).append(f)
ED=dict(sorted(ED.items()))
assert len(ED)==17 and all(len(v)==2 for v in ED.values())
def add(a,b):return tuple(x+y for x,y in zip(a,b))
def sub(a,b):return tuple(x-y for x,y in zip(a,b))
def mul(a,s):return tuple(s*x for x in a)
def dot(a,b):return sum(x*y for x,y in zip(a,b))
def cross(a,b):return (a[1]*b[2]-a[2]*b[1],a[2]*b[0]-a[0]*b[2],a[0]*b[1]-a[1]*b[0])
def det(a,b,c):return dot(a,cross(b,c))
def mv(M,v):return tuple(dot(r,v) for r in M)
def md(a,b,M):return dot(a,mv(M,b))
def eye(n):return [[F(i==j) for j in range(n)] for i in range(n)]
def solve(A,b):
 a=[list(map(F,r))+[F(s)] for r,s in zip(A,b)];n=len(b)
 assert len(a)==n and all(len(r)==n+1 for r in a)
 for j in range(n):
  k=next(i for i in range(j,n) if a[i][j]);a[j],a[k]=a[k],a[j]
  d=a[j][j];a[j]=[x/d for x in a[j]]
  for i in range(n):
   if i!=j:
    d=a[i][j];a[i]=[x-d*y for x,y in zip(a[i],a[j])]
 return tuple(r[-1] for r in a)
def inverse(A):
 n=len(A);cols=[solve(A,[F(i==j) for i in range(n)]) for j in range(n)]
 return tuple(tuple(cols[j][i] for j in range(n)) for i in range(n))
def rank(A):
 a=[list(map(F,r)) for r in A];i=0
 for j in range(len(a[0])):
  ks=[k for k in range(i,len(a)) if a[k][j]]
  if not ks:continue
  k=ks[0];a[i],a[k]=a[k],a[i];d=a[i][j];a[i]=[v/d for v in a[i]]
  for k in range(len(a)):
   if k!=i:
    d=a[k][j];a[k]=[x-d*y for x,y in zip(a[k],a[i])]
  i+=1
  if i==len(a):break
 return i
def tensor(x,u):return (x[0]*u[0],x[1]*u[1],x[2]*u[2],
    x[0]*u[1]+x[1]*u[0],x[0]*u[2]+x[2]*u[0],x[1]*u[2]+x[2]*u[1])
def mat(v):
 a,b,c,d,e,f=v;return ((a,d,e),(d,b,f),(e,f,c))
def positive(M):return (M[0][0],M[0][0]*M[1][1]-M[0][1]**2,det(*M))
def mass(X,apex=Z):
 V=F(0);J=Z;R=[[F(0)]*3 for _ in range(3)];cells=[]
 for tr in TRI:
  pts=[apex]+[X[i] for i in tr];d=det(*(sub(p,apex) for p in pts[1:]));S=tuple(sum(p[k] for p in pts) for k in range(3))
  V+=d/6;J=add(J,mul(S,d/24));cells.append(d)
  for i in range(3):
   for j in range(3):R[i][j]+=d*(S[i]*S[j]+sum(p[i]*p[j] for p in pts))/120
 return V,J,tuple(map(tuple,R)),tuple(cells)
def hull(X):
 facets=set()
 for i,j,k in combinations(range(10),3):
  n=cross(sub(X[j],X[i]),sub(X[k],X[i]))
  if n==Z:continue
  vals=[dot(n,sub(p,X[i])) for p in X]
  if max(vals)<=0 or min(vals)>=0:facets.add(tuple(q for q,v in enumerate(vals) if v==0))
 assert facets=={tuple(sorted(c)) for c in CY}
 for cy in CY:
  a,b,c=[X[i] for i in cy[:3]];n=cross(sub(b,a),sub(c,a))
  assert all(dot(n,sub(X[i],a))==0 for i in cy)
  assert all(dot(n,sub(X[i],a))<0 for i in range(10) if i not in cy)
  for i,j in zip(cy,cy[1:]+cy[:1]):
   assert all(dot(n,cross(sub(X[j],X[i]),sub(X[k],X[i])))>0 for k in cy if k not in (i,j))
 for (i,j),(f,g) in ED.items():assert set(CY[f])&set(CY[g])=={i,j}
 assert 10-17+9==2
 return sorted(facets)
def audit(X,M):
 facets=hull(X);V,J,R,cells=mass(X);assert V>0 and J==Z
 fans=[]
 for a in (8,9):
  vv,jj,rr,dd=mass(X,X[a]);assert (vv,jj,rr)==(V,J,R) and min(dd)>=0
  fans.append(dd)
 assert min(positive(M))>0;N=inverse(M);Q=[]
 for cy in CY:
  a,b,c=[X[i] for i in cy[:3]];nn=cross(sub(b,a),sub(c,a));d=dot(nn,a);assert d>0;Q.append(mul(nn,1/d))
 pv=[[] for _ in X];qv=[[] for _ in Q];pack=[];weak=[];saddles=[];harmless=[]
 for (i,j),(f,g) in ED.items():
  v=(md(X[i],sub(X[j],X[i]),M),md(X[j],sub(X[i],X[j]),M),
     md(Q[f],sub(Q[g],Q[f]),N),md(Q[g],sub(Q[f],Q[g]),N))
  pv[i].append(v[0]);pv[j].append(v[1]);qv[f].append(v[2]);qv[g].append(v[3]);pack.append(((i,j),(f,g),v))
  if max(v)<0:saddles.append((i,j))
  elif max(v)<=0 and 0 in v:weak.append(((i,j),v))
  elif 0 in v:harmless.append(((i,j),v))
 return dict(vertices=X,facets=CY,edges=tuple(ED),volume=V,covariance=tuple(tuple(r/V for r in row) for row in R),
    M=M,N=N,poles=Q,packets=pack,weak=weak,harmless=harmless,positive_fans=fans,
    strict=dict(S=tuple(i for i,v in enumerate(qv) if max(v)<0),U=tuple(i for i,v in enumerate(pv) if max(v)<0),H=tuple(saddles)))
class P:
 def __init__(self,c=0):
  self.c=list(c.c) if isinstance(c,P) else list(map(F,c)) if isinstance(c,(list,tuple)) else [F(c)]
  while len(self.c)>1 and self.c[-1]==0:self.c.pop()
 def __add__(self,o):
  o=P(o);return P([(self.c[i] if i<len(self.c) else 0)+(o.c[i] if i<len(o.c) else 0) for i in range(max(len(self.c),len(o.c)))])
 __radd__=__add__
 def __neg__(self):return P([-x for x in self.c])
 def __sub__(self,o):return self+-P(o)
 def __rsub__(self,o):return P(o)+-self
 def __mul__(self,o):
  o=P(o);r=[F(0)]*(len(self.c)+len(o.c)-1)
  for i,a in enumerate(self.c):
   for j,b in enumerate(o.c):r[i+j]+=a*b
  return P(r)
 __rmul__=__mul__
 def __truediv__(self,o):return self*(1/F(o))
 def __pow__(self,n):
  assert n>=0;r=P(1)
  for _ in range(n):r=r*self
  return r
 def __eq__(self,o):return self.c==P(o).c
 def coeff(self,i):return self.c[i] if i<len(self.c) else F(0)
 def val(self,t):
  r=F(0)
  for c in self.c[::-1]:r=r*t+c
  return r
 def diff(self):return P([i*self.c[i] for i in range(1,len(self.c))] or [0])
def pmass(X):
 V=P(0);J=(P(0),)*3
 for tr in TRI:
  a,b,c=[X[i] for i in tr];d=det(a,b,c);V+=d/6;J=add(J,mul(add(add(a,b),c),d/24))
 return V,J
def jet(a,b):
 a=P(a);b=P(b);assert b.coeff(0)!=0;r=[]
 for k in range(3):r.append((a.coeff(k)-sum(b.coeff(j)*r[k-j] for j in range(1,k+1)))/b.coeff(0))
 return tuple(r)
def bern(p,eps):
 p=P(p);n=len(p.c)-1
 return tuple(sum(p.c[k]*eps**k*F(comb(i,k),comb(n,k)) for k in range(i+1)) for i in range(n+1))
def polygon(ids):
 pts=[(F(0),F(0)) if i==-1 else RAW[i][:2] for i in ids];A=F(0);I=[F(0),F(0)]
 for a,b in zip(pts,pts[1:]+pts[:1]):
  d=a[0]*b[1]-a[1]*b[0];A+=d/2
  for k in range(2):I[k]+=d*(a[k]+b[k])/6
 return A,tuple(I)
def jac_vertex(i,h,V,g):
 X=[tuple(P((a,v if k==i else 0)) for a,v in zip(p,h)) for k,p in enumerate(RAW)]
 vv,jj=pmass(X);return tuple((j.coeff(1)-g[k]*vv.coeff(1))/V for k,j in enumerate(jj))
def ear(i,h,V,g):
 p=(i-1)%8;q=(i+1)%8;A=8 if i in (5,6,7,0) else 9
 # positive ear area and its planar gradient, directly differentiated
 def area(w):return cross(sub(w,RAW[p]),sub(RAW[q],RAW[p]))[2]/2
 d=area(RAW[i]);sgn=1 if d>0 else -1;d*=sgn
 lam=tuple(sgn*(area(add(RAW[i],e))-area(RAW[i])) for e in ((F(1),0,0),(0,F(1),0),Z))
 assert d>0;S=add(add(add(RAW[A],RAW[p]),RAW[i]),RAW[q]);S=sub(S,mul(g,4))
 return mul(add(mul(h,d),mul(S,dot(lam,h))),RAW[A][2]/(12*V)),d,lam

def cover_control(X,g):
 C=((8,0),(9,1),(2,9),(5,8));T=[tensor(X[i],sub(X[j],X[i])) for i,j in C]
 m=solve(T+[(0,0,1,0,0,0),(0,0,0,1,0,0)],(0,0,0,0,1,F(9,4)));M=mat(m)
 old=audit(X,M);assert len(old['weak'])==4 and not old['harmless'] and rank(T)==4
 for i,j in C:
  vals=[md(X[i],sub(p,X[i]),M) for p in X]
  assert vals[i]==vals[j]==0 and all(v<0 for k,v in enumerate(vals) if k not in (i,j))
 n=(g[1],-g[0],F(0));assert dot(n,X[8])==dot(n,X[9])==0
 v=solve((X[8],X[9],n),(1/dot(n,sub(X[0],X[8])),1/dot(n,sub(X[1],X[9])),0))
 H1=tuple(tuple(-x*y for y in n) for x in n)
 H2=tuple(tuple(n[i]*v[j]+v[i]*n[j] for j in range(3)) for i in range(3))
 MM=tuple(tuple(P((M[i][j],H1[i][j],H2[i][j])) for j in range(3)) for i in range(3))
 cc=(cross(MM[1],MM[2]),cross(MM[2],MM[0]),cross(MM[0],MM[1]));adj=tuple(tuple(cc[j][i] for j in range(3)) for i in range(3));dd=det(*MM)
 for i in range(3):
  for j in range(3):assert sum(MM[i][k]*adj[k][j] for k in range(3))==dd*(i==j)
 guards=[('SPD:'+str(k),p) for k,p in enumerate(positive(MM),1)];jphi=[]
 for z,((i,j),(f,gg),vals) in enumerate(old['packets']):
  q,r=old['poles'][f],old['poles'][gg]
  ps=(md(X[i],sub(X[j],X[i]),MM),md(X[j],sub(X[i],X[j]),MM),md(q,sub(r,q),adj),md(r,sub(q,r),adj))
  for k,(p,original) in enumerate(zip(ps,vals)):
   p=P(p)
   if original: pp=p*(1 if original>0 else -1);assert pp.coeff(0)>0
   else:
    assert k<2 and p.coeff(0)==0
    src,dst=(i,j) if k==0 else(j,i);order=2 if src in (8,9) else 1
    assert all(p.coeff(j)==0 for j in range(order)) and p.coeff(order)>0
    if order==2:assert p.coeff(2)==1
    else:assert p.coeff(1)==dot(n,X[src])**2
    pp=P(p.c[order:]);jphi.append(((src,dst),order,p))
   guards.append(('mechanic:'+str((z,k)),pp))
 for power in range(10,41):
  eps=F(1,2**power);bs=[bern(p,eps) for _,p in guards]
  if all(min(b)>0 for b in bs):break
 else:raise AssertionError('no affine-cover interval')
 endM=tuple(tuple(p.val(eps) for p in row) for row in MM);end=audit(X,endM)
 assert old['strict']==end['strict'] and not end['weak'] and not end['harmless']
 beta=[X[i][2]*(X[j][2]-X[i][2]) for i,j in C];assert beta[0]>0 and all(b<0 for b in beta[1:])
 return dict(contacts=C,initial=old,normal=n,mixed_covector=v,H1=H1,H2=H2,
  metric_polynomial=MM,adjugate=adj,metric_determinant=dd,
  inverse_metric_jets=tuple(tuple(jet(a,dd) for a in row) for row in adj),
  beta=beta,contact_polynomials=jphi,interval=eps,
  guards=tuple((name,p,b) for (name,p),b in zip(guards,bs)),
  bernstein_count=sum(map(len,bs)),max_degree=max(len(p.c)-1 for _,p in guards),endpoint=end,tensor_rank=rank(T))

def build():
 V,J,R,_=mass(RAW);g=mul(J,1/V);X=tuple(sub(p,g) for p in RAW)
 assert V==F(4933,600) and g==(F(27115,39464),F(22046,24665),F(53167,39464))
 T=[tensor(X[i],sub(X[j],X[i])) for i,j in CONTACTS]
 m=solve(T+[(0,0,1,0,0,0),(0,0,0,1,0,0)],(0,0,0,0,1,F(11,12)));M=mat(m)
 initial=audit(X,M);assert len(initial['weak'])==4 and not initial['harmless']
 for i,j in CONTACTS:
  vals=[md(X[i],sub(p,X[i]),M) for p in X]
  assert vals[i]==vals[j]==0 and all(v<0 for k,v in enumerate(vals) if k not in (i,j))
 assert {i for e,v in initial['weak'] for i in e}=={0,1,2,4,5,6,8,9}
 assert len([v for _,_,r in initial['packets'] for v in r if v==0])==4
 # Attempting a rho tie on this fixed geometry is not a physical stress control.
 ell=mul(tuple(row[2] for row in initial['covariance']),5/g[2]);rho_rows=[]
 for i,j in CONTACTS[2:]:
  x=X[i];du=sub(X[j],x);dz=du[2];Hi=x[2]+g[2];qi=add(mul(du,Hi),mul(x,dz));be=x[2]*dz
  rho_rows.append(tuple((a-dz*b)/be for a,b in zip(tensor(ell,qi),tensor(x,x))))
 tie=solve(T+[tuple(a-b for a,b in zip(*rho_rows)),(0,0,1,0,0,0)],(0,0,0,0,0,1))
 assert tie[1]<0
 A,I=polygon((-1,1,2,3,4));B,L=polygon((-1,0,7,6,5));h=RAW[8][2];H=RAW[9][2];W=H*A-h*B
 assert A>B>0
 assert V==W/3
 assert g[:2]==tuple(3*(H*i-h*l)/(4*W) for i,l in zip(I,L))
 assert g[2]==(H*H*A-h*h*B)/(4*W)
 # x functional = old x+y. The two ear chords have x=1 and x=3.
 s=F(9,10);r=F(1);t=F(7,2);u=F(3);U=2*s+r;D=2*t+u
 CK=sum(I)/A;CG=sum(L)/B;gap=H*A*(D-3*CK)-h*B*(U-3*CG)
 assert min(sum(p[:2]) for p in RAW[:8])==s and max(sum(p[:2]) for p in RAW[:8])==t
 assert 3*CK<=2*t and 3*CG>=s+r and gap>=H*A*u-h*B*s>0
 n=(F(1),F(1),F(0));l=(F(1),F(-1),F(0))
 cols=[jac_vertex(7,n,V,g),jac_vertex(7,l,V,g),jac_vertex(3,n,V,g)]
 for i,d,col in zip((7,7,3),(n,l,n),cols):assert ear(i,d,V,g)[0]==col
 A3=tuple(tuple(col[k] for col in cols) for k in range(3));assert det(*A3)!=0
 # Four raw opening motions, then solve three free coordinates to cancel the actual centroid derivative.
 v=[Z for _ in RAW];v[1]=(-F(1),0,0);v[4]=(0,-F(1),0);v[6]=(-F(1),0,0);v[2]=(F(1),0,0)
 W0=tuple(tuple(P((a,b)) for a,b in zip(p,d)) for p,d in zip(RAW,v));vv,jj=pmass(W0)
 dg=tuple((j.coeff(1)-g[k]*vv.coeff(1))/V for k,j in enumerate(jj));abc=solve(A3,mul(dg,-1))
 v[7]=add(mul(n,abc[0]),mul(l,abc[1]));v[3]=mul(n,abc[2])
 WW=tuple(tuple(P((a,b)) for a,b in zip(p,d)) for p,d in zip(RAW,v));VV,JJ=pmass(WW)
 assert all(j.coeff(1)==g[k]*VV.coeff(1) for k,j in enumerate(JJ))
 ZZ=tuple(sub(mul(p,VV),JJ) for p in WW);vh,jh=pmass(ZZ);assert vh==VV**4 and all(j==0 for j in jh)
 gj=tuple(jet(j,VV) for j in JJ);xj=tuple(tuple(jet(a,VV) for a in z) for z in ZZ)
 assert tuple(j[1] for j in gj)==Z
 guards=[('volume',VV)];ns=[];ds=[];qj=[]
 for f,cy in enumerate(CY):
  a,b,c=[WW[i] for i in cy[:3]];nn=cross(sub(b,a),sub(c,a));hh=dot(nn,a);dd=VV*hh-dot(nn,JJ)
  ns.append(nn);ds.append(dd);guards.append(('inside:'+str(f),dd));qj.append(tuple(jet(VV*a,dd) for a in nn))
  for i in cy:assert dot(nn,sub(WW[i],a))==0
  for i in range(10):
   if i not in cy:guards.append(('support:'+str((f,i)),dot(nn,sub(a,WW[i]))))
  for i,j in zip(cy,cy[1:]+cy[:1]):
   for k in cy:
    if k not in (i,j):guards.append(('polygon:'+str((f,i,j,k)),dot(nn,cross(sub(WW[j],WW[i]),sub(WW[k],WW[i])))))
  for i in cy:
   xx=[[xj[i][k][o] for k in range(3)] for o in range(3)];qq=[[qj[f][k][o] for k in range(3)] for o in range(3)]
   assert dot(xx[0],qq[0])==1
   assert dot(xx[1],qq[0])+dot(xx[0],qq[1])==0
   assert dot(xx[2],qq[0])+dot(xx[1],qq[1])+dot(xx[0],qq[2])==0
 N=initial['N'];first=[];contact_second=[]
 for num,((i,j),(f,gg),vals) in enumerate(initial['packets']):
  pol=[md(ZZ[i],sub(ZZ[j],ZZ[i]),M),md(ZZ[j],sub(ZZ[i],ZZ[j]),M),
       md(ns[f],sub(mul(ns[gg],ds[f]),mul(ns[f],ds[gg])),N),
       md(ns[gg],sub(mul(ns[f],ds[gg]),mul(ns[gg],ds[f])),N)]
  for k,(p,old) in enumerate(zip(pol,vals)):
   if old:
    assert p.coeff(0)*old>0;pp=p*(1 if old>0 else -1)
   else:
    assert k<2 and p.coeff(0)==0 and p.coeff(1)>0;pp=P(p.c[1:])
    src,dst=(i,j) if k==0 else(j,i);jphi=jet(p,VV**2)
    direct=md(v[src],sub(X[dst],X[src]),M)+md(X[src],sub(v[dst],v[src]),M)
    assert jphi[1]==direct>0;first.append(((src,dst),direct));contact_second.append(((src,dst),jphi[2]))
   guards.append(('mechanic:'+str((num,k)),pp))
 assert len(first)==4
 for power in range(10,41):
  eps=F(1,2**power);bs=[bern(p,eps) for _,p in guards]
  if all(min(b)>0 for b in bs):break
 else:raise AssertionError('no interval certificate')
 end=tuple(tuple(a.val(eps)/VV.val(eps) for a in z) for z in ZZ);final=audit(end,M)
 assert final['strict']==initial['strict'] and not final['weak'] and not final['harmless']
 # Small exact proof-helper identities for the two-vertex-cover metric steps on this actual body.
 aa,bb=X[8],X[9];normal=cross(aa,bb);assert normal!=Z
 H1=tuple(tuple(-a*b for b in normal) for a in normal)
 cover_rows=[]
 for i,j in ED:
  if i not in (8,9) and j not in (8,9):continue
  for src,dst in ((i,j),(j,i)):
   measured=md(X[src],sub(X[dst],X[src]),H1)
   expected=F(0) if src in (8,9) else dot(normal,X[src])**2
   assert measured==expected;cover_rows.append(((src,dst),measured))
 # The actual first-order full contact matrix has rank four, witnessed by this positive arc and a tensor minor.
 assert rank(T)==4
 return dict(name='TWO_APEX_COVER_AND_TWO_INTERNAL_REGULARIZATION_V1',parent='minimum-0140',
   raw=RAW,initial=initial,raw_centroid=g,contacts=CONTACTS,cover=cover_control(X,g),
   shadow=dict(K=(A,I),G=(B,L),near=(s,r,U),far=(t,u,D),means=(CK,CG),gap=gap,lower_gap=H*A*u-h*B*s),
   rho_tie_normalized_metric=mat(tie),rho_rows=rho_rows,
   free_vertices=(3,7),free_centroid_columns=cols,free_minor=det(*A3),
   correction=abc,raw_velocity=v,raw_volume=VV,raw_first_moment=JJ,homogeneous_vertices=ZZ,
   actual_centroid_jets=gj,vertex_jets=xj,pole_jets=qj,contact_first=first,contact_second=contact_second,
   interval=eps,guards=tuple((name,p,b) for (name,p),b in zip(guards,bs)),
   bernstein_count=sum(map(len,bs)),max_degree=max(len(p.c)-1 for _,p in guards),
   endpoint=final,apex_plane_normal=normal,cover_metric_identity_rows=cover_rows,tensor_rank=rank(T))
def encode(x):
 if isinstance(x,F):return str(x)
 if isinstance(x,P):return [str(v) for v in x.c]
 if isinstance(x,(tuple,list)):return [encode(v) for v in x]
 if isinstance(x,dict):return {str(k):encode(v) for k,v in x.items()}
 return x
if __name__=='__main__':
 assert sys.argv[1:] in (['build'],['check'])
 report=build();data=(json.dumps(encode(report),sort_keys=True,separators=(',',':'))+'\n').encode()
 p=Path('two_cover_free_base.json')
 if sys.argv[1]=='build':p.write_bytes(data)
 else:assert p.read_bytes()==data
 print('ACTUAL_UNEQUAL_PURE_FOUR_A_TWO_OPPOSITE_INTERNAL_PARALLEL_CHORDS_PASS')
 print('TRUE_SHADOW_DIFFERENCE_MOMENTS_AND_POSITIVE_CENTROID_MINOR_PASS')
 print('EXACT_FREE_VERTEX_CENTROID_REPAIR_FULL_MIXED_JETS_PASS')
 print('WHOLE_INTERVAL_OLD_STRICT_LABELS_WEAK000_PASS')
 print('ADJACENT_TWO_VERTEX_COVER_AFFINE_IDENTITIES_PASS')
 print('PURE_FOUR_NONBASAL_ADVERSE_OWN_COM_RECIPROCAL_AFFINE_ARC_PASS')
 print('STRICT',report['initial']['strict'])
 print('EPSILON',report['interval'],'GUARDS',len(report['guards']),'BERNSTEIN',report['bernstein_count'],'MAXDEG',report['max_degree'])
 print('COVER STRICT',report['cover']['initial']['strict'],'EPSILON',report['cover']['interval'],'GUARDS',len(report['cover']['guards']),'BERNSTEIN',report['cover']['bernstein_count'],'MAXDEG',report['cover']['max_degree'])
 print(p.name,len(data),hashlib.sha256(data).hexdigest())
 print('TWO_APEX_COVER_AND_TWO_INTERNAL_RECOVERY_PASS')
```

## Appendix B. Complete new `four_quad.py`

```python
"""FOUR_FREE_QUADRILATERAL_MOMENT_SUBMERSION_V1 exact physical control.
CPython 3.13.5 standard library, assertions, PYTHONHASHSEED=0.
Requires the complete unchanged two_cover_free_base.py, SHA256
7fa5a6e8df8bf4100329515a43b973a8ce71a293b8f967a10be6f8a265e3080a.
Parent minimum-0143, SHA256
c38b1e713ef30a6ad4e9d6b5bd5eaa3d1354bb762a26e5a80862f5ca9cceed15.
Run python -S four_quad.py build|check. No discovery search is needed.
"""
from pathlib import Path
import hashlib,json,sys
assert __debug__
assert hashlib.sha256(Path(__file__).with_name('two_cover_free_base.py').read_bytes()).hexdigest()=='7fa5a6e8df8bf4100329515a43b973a8ce71a293b8f967a10be6f8a265e3080a'
import two_cover_free_base as T
from two_cover_free_base import F,P,Z,add,sub,mul,dot,cross,det,mv,md,solve,rank,mat,mass,pmass,jet,bern,audit,tensor,encode
from itertools import combinations
CS=((8,9),(2,3),(6,8),(7,8))
RAW=T.RAW[:-1]+((F(0),F(0),F(11,10)),)

def mdiff(v,raw=RAW):
 W=tuple(tuple(P((a,b)) for a,b in zip(p,d)) for p,d in zip(raw,v))
 V,J=pmass(W)
 return (V.coeff(1),)+tuple(j.coeff(1) for j in J)

def determinant(A):
 if len(A)==1:return A[0][0]
 return sum((-1)**j*A[0][j]*determinant([row[:j]+row[j+1:] for row in A[1:]]) for j in range(len(A)))

def planar(W,ids):
 pts=[(P(0),P(0)) if i==-1 else W[i][:2] for i in ids]
 A=P(0);I=(P(0),P(0))
 for a,b in zip(pts,pts[1:]+pts[:1]):
  d=a[0]*b[1]-a[1]*b[0];A+=d/2;I=add(I,mul(add(a,b),d/6))
 return A,I

def radial_only_control():
 raw=tuple(tuple(map(F,p)) for p in ((1,0,0),(3,0,0),(3,1,0),(1,3,0),(0,3,0),
  (0,1,0),(F(1,5),F(1,2),0),(F(1,2),F(1,5),0),(0,0,1),(0,0,2)))
 V,J,_,_=mass(raw);g=mul(J,1/V);X=tuple(sub(p,g) for p in raw)
 M=tuple(tuple(map(F,r)) for r in ((3,1,1),(1,2,0),(1,0,2)));body=audit(X,M)
 assert V==F(913,200) and g==(F(35171,36520),F(35171,36520),F(5539,10956))
 assert not body['weak'] and not body['harmless']
 directions=[]
 for i,e in ((0,(1,0,0)),(1,(1,0,0)),(5,(0,1,0)),(4,(0,1,0))):
  d=[Z]*10;d[i]=tuple(map(F,e));directions.append(d)
 d=[Z]*10;d[0]=mul(raw[7],1/raw[7][1]);d[1]=mul(raw[2],3/raw[2][1]);directions.append(d)
 d=[Z]*10;d[5]=mul(raw[6],1/raw[6][0]);d[4]=mul(raw[3],3/raw[3][0]);directions.append(d)
 cols=tuple(mdiff(d,raw) for d in directions)
 assert rank(tuple(zip(*cols[:4])))==3 and rank(tuple(zip(*cols)))==4
 nu=(F(-23,146),F(-10,73),F(-10,73),F(1))
 assert tuple(dot(nu,c) for c in cols)==(0,0,0,0,F(-713,1752),F(-713,1752))
 centroid_columns=tuple(tuple((c[k+1]-g[k]*c[0])/V for k in range(3)) for c in cols)
 assert rank(tuple(zip(*centroid_columns[:4])))==3
 return dict(raw=raw,centroid=g,body=body,directions=directions,columns=cols,
  radial_rank=3,full_rank=4,radial_annihilator=nu,centroid_columns=centroid_columns)

def control():
 V,J,R,_=mass(RAW);g=mul(J,1/V);X=tuple(sub(p,g) for p in RAW)
 assert V==F(943,600) and g==(F(5485,7544),F(8917,9430),F(2095,7544))
 rows=[tensor(X[i],sub(X[j],X[i])) for i,j in CS]
 m=solve(rows+[(0,0,1,0,0,0),(0,0,0,1,0,0)],(0,0,0,0,1,F(2,3)))
 M=mat(m);old=audit(X,M)
 strict=dict(S=(0,1,2,3,5),U=(3,9),H=((0,1),(1,9),(2,9),(3,9),(4,5)))
 assert old['strict']==strict and len(old['weak'])==4 and not old['harmless']
 assert sum(v==0 for _,_,vs in old['packets'] for v in vs)==4
 for i,j in CS:
  vals=[md(X[i],sub(p,X[i]),M) for p in X]
  assert vals[i]==vals[j]==0 and all(v<0 for k,v in enumerate(vals) if k not in (i,j))
 free=tuple(i for i in range(10) if all(i not in e for e in CS));assert free==(0,1,4,5)
 beta=tuple(X[i][2]*(X[j][2]-X[i][2]) for i,j in CS)
 assert beta[0]>0 and beta[1]==0 and beta[2]<0 and beta[3]<0
 # Four independent radial directions and the two area-neutral angular directions.
 ds=[]
 for i,e in ((0,(1,0,0)),(1,(1,0,0)),(5,(0,1,0)),(4,(0,1,0))):
  d=[Z]*10;d[i]=tuple(map(F,e));ds.append(d)
 d=[Z]*10;d[0]=mul(RAW[7],1/RAW[7][1]);d[1]=mul(RAW[2],F(5,2)/RAW[2][1]);ds.append(d)
 d=[Z]*10;d[5]=mul(RAW[6],F(6,5)/RAW[6][0]);d[4]=mul(RAW[3],F(3)/RAW[3][0]);ds.append(d)
 cols=tuple(mdiff(d) for d in ds);assert rank(tuple(zip(*cols)))==4
 # Compare all six actual volume/first-moment columns to the explicit shadow derivatives.
 h=RAW[8][2];H=RAW[9][2]
 expected=[]
 for p,u,ht,sgn,k in ((RAW[0],RAW[7],h,-1,1),(RAW[1],RAW[2],H,1,1),
                      (RAW[5],RAW[6],h,-1,0),(RAW[4],RAW[3],H,1,0)):
  dv=sgn*ht*u[k]/6
  expected.append((dv,)+mul(add(add(mul(p,2),u),(0,0,ht)),dv/4))
 for r,R,u,v in ((F(1),F(5,2),RAW[7],RAW[2]),(F(6,5),F(3),RAW[6],RAW[3])):
  expected.append((F(0),)+mul(sub(mul(v,H*R*R),mul(u,h*r*r)),F(1,24)))
 assert cols==tuple(expected)
 minors=tuple((ix,determinant([[cols[j][i] for j in ix] for i in range(4)])) for ix in combinations(range(6),4))
 # Raw opening motion; the internal vertices move in the basal plane, apex8 on its ridge.
 opening=[Z]*10;opening[8]=(0,0,F(1));opening[2]=sub(RAW[3],RAW[2]);opening[6]=opening[7]=(F(2),0,0)
 direct=tuple(md(sub(sub(X[j],X[i]),X[i]),opening[i],M)+md(X[i],opening[j],M) for i,j in CS)
 assert min(direct)>0
 # Force BOTH quadrilateral planes to rotate. Fix angular1=1; solve radial1,5,4 and angular2.
 va=[add(x,y) for x,y in zip(opening,ds[4])];ix=(1,2,3,5)
 A4=[[cols[j][i] for j in ix] for i in range(4)]
 correction=solve(A4,mul(mdiff(va),-1));velocity=va[:]
 for c,j in zip(correction,ix):velocity=[add(x,mul(y,c)) for x,y in zip(velocity,ds[j])]
 assert mdiff(velocity)==(0,0,0,0)
 theta1=F(1);theta2=correction[-1];assert theta2!=0
 t=P((0,1));WW=[tuple(P((a,b)) for a,b in zip(p,v)) for p,v in zip(RAW,velocity)]
 r0=P((RAW[0][0],velocity[0][0]));r1=P((RAW[1][0],velocity[1][0]))
 r5=P((RAW[5][1],velocity[5][1]));r4=P((RAW[4][1],velocity[4][1]))
 WW[0]=(r0,r0*theta1*t,P(0));WW[1]=(r1,r1*theta1*t,P(0))
 WW[5]=(r5*theta2*t,r5,P(0));WW[4]=(r4*theta2*t,r4,P(0));WW=tuple(WW)
 VV,JJ=pmass(WW);assert VV.coeff(1)==0 and all(j.coeff(1)==0 for j in JJ)
 K,IK=planar(WW,(-1,1,2,3,4));G,IG=planar(WW,(-1,0,7,6,5));hh=WW[8][2]
 assert VV==(H*K-hh*G)/3
 assert JJ[:2]==tuple((H*a-hh*b)/4 for a,b in zip(IK,IG))
 assert JJ[2]==(H*H*K-hh*hh*G)/12
 ZZ=tuple(sub(mul(p,VV),JJ) for p in WW);vh,jh=pmass(ZZ)
 assert vh==VV**4 and all(j==0 for j in jh)
 gj=tuple(jet(j,VV) for j in JJ);xj=tuple(tuple(jet(a,VV) for a in z) for z in ZZ)
 assert tuple(j[1] for j in gj)==Z and any(j[2] for j in gj)
 guards=[('volume',VV)];ns=[];dsupport=[];qj=[]
 for f,cy in enumerate(T.CY):
  a,b,c=[WW[i] for i in cy[:3]];n=cross(sub(b,a),sub(c,a));hh=dot(n,a);d=VV*hh-dot(n,JJ)
  ns.append(n);dsupport.append(d);guards.append(('inside:'+str(f),d));qj.append(tuple(jet(VV*a,d) for a in n))
  for i in cy:assert dot(n,sub(WW[i],a))==0
  for i in range(10):
   if i not in cy:guards.append(('support:'+str((f,i)),dot(n,sub(a,WW[i]))))
  for i,j in zip(cy,cy[1:]+cy[:1]):
   for k in cy:
    if k not in (i,j):guards.append(('polygon:'+str((f,i,j,k)),dot(n,cross(sub(WW[j],WW[i]),sub(WW[k],WW[i])))))
  for i in cy:
   xx=[[xj[i][k][o] for k in range(3)] for o in range(3)];qq=[[qj[f][k][o] for k in range(3)] for o in range(3)]
   assert dot(xx[0],qq[0])==1
   assert dot(xx[1],qq[0])+dot(xx[0],qq[1])==0
   assert dot(xx[2],qq[0])+dot(xx[1],qq[1])+dot(xx[0],qq[2])==0
 N=old['N'];contact_jets=[]
 for num,((i,j),(f,gg),vals) in enumerate(old['packets']):
  ps=(md(ZZ[i],sub(ZZ[j],ZZ[i]),M),md(ZZ[j],sub(ZZ[i],ZZ[j]),M),
      md(ns[f],sub(mul(ns[gg],dsupport[f]),mul(ns[f],dsupport[gg])),N),
      md(ns[gg],sub(mul(ns[f],dsupport[gg]),mul(ns[gg],dsupport[f])),N))
  for k,(p,previous) in enumerate(zip(ps,vals)):
   if previous:
    assert p.coeff(0)*previous>0;pp=p*(1 if previous>0 else -1)
   else:
    assert k<2 and p.coeff(0)==0 and p.coeff(1)>0;pp=P(p.c[1:])
    edge=(i,j) if k==0 else (j,i);jj=jet(p,VV**2)
    assert jj[1]==direct[CS.index(edge)]>0;contact_jets.append((edge,jj))
   guards.append(('mechanic:'+str((num,k)),pp))
 assert len(contact_jets)==4
 for power in range(10,41):
  eps=F(1,2**power);bs=[bern(p,eps) for _,p in guards]
  if all(min(b)>0 for b in bs):break
 else:raise AssertionError('no certified interval')
 endpoint=tuple(tuple(p.val(eps)/VV.val(eps) for p in z) for z in ZZ);end=audit(endpoint,M)
 assert end['strict']==old['strict'] and not end['weak'] and not end['harmless']
 return dict(name='FOUR_FREE_QUADRILATERAL_MOMENT_SUBMERSION_V1',raw=RAW,contacts=CS,initial=old,
   centroid=g,beta=beta,free_vertices=free,moment_directions=ds,moment_columns=cols,moment_minors=minors,
   moment_rank=4,tensor_rank=rank(rows),raw_opening=opening,direct_contact_first=direct,
   correction_basis=ix,correction=correction,raw_velocity=velocity,theta=(theta1,theta2),
   raw_polynomial_vertices=WW,raw_volume=VV,raw_first_moment=JJ,shadow_K=(K,IK),gap_G=(G,IG),
   homogeneous_vertices=ZZ,centroid_jets=gj,vertex_jets=xj,pole_jets=qj,contact_jets=contact_jets,
   interval=eps,guards=tuple((name,p,b) for (name,p),b in zip(guards,bs)),
   bernstein_count=sum(map(len,bs)),max_degree=max(len(p.c)-1 for _,p in guards),endpoint=end)

if __name__=='__main__':
 assert sys.argv[1:] in (['build'],['check'])
 out=control();out['radial_only_countercontrol']=radial_only_control();data=(json.dumps(encode(out),sort_keys=True,separators=(',',':'))+'\n').encode()
 p=Path('four_quad.json')
 if sys.argv[1]=='build':p.write_bytes(data)
 else:assert p.read_bytes()==data
 print('ACTUAL_FOUR_FREE_QUAD_PURE_FOUR_A_UNEQUAL_ADVERSE_RIDGE_PASS')
 print('SIX_GENUINE_COUPLED_MOMENT_COLUMNS_RANK4_PASS')
 print('ACTUAL_RADIAL_ONLY_RANK3_NOT_FULL_MOMENT_SUBMERSION_PASS')
 print('BOTH_QUADRILATERAL_ROTATIONS_FULL_SHADOW_GAP_POLYNOMIAL_IDENTITIES_PASS')
 print('ACTUAL_RECENTERING_AND_ALL_MIXED_SECOND_JETS_PASS')
 print('OLD_STRICT_LABELS_AND_WEAK000_WHOLE_INTERVAL_PASS')
 print('STRICT',out['initial']['strict'],'TENSOR_RANK',out['tensor_rank'])
 print('EPSILON',out['interval'],'GUARDS',len(out['guards']),'BERNSTEIN',out['bernstein_count'],'MAXDEG',out['max_degree'])
 print(p.name,len(data),hashlib.sha256(data).hexdigest())
 print('FOUR_FREE_QUADRILATERAL_RECOVERY_PASS')
```
