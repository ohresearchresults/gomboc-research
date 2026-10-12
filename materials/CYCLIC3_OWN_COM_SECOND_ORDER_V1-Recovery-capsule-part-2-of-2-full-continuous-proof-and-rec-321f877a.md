# material-321f877abafa

AI research material · [Export notes](../catalog/coverage.md#text-records)

<!-- historical-status:start -->
> **Historical AI material.** The title and claims below reflect the AI’s assessment at the time. Claims of proof, certification or completion are not a current verification verdict.
>
> [C622](../C622/README.md) passes the supplied exact checks; C<500 remains open; Minimum’s C≥34 remains a working lower bound requiring a consolidated proof. See [verification status and source gaps](../catalog/coverage.md).
>
> This public text omits encoded source blocks; code in the affected passages is incomplete.
<!-- historical-status:end -->

---

# CYCLIC3_OWN_COM_SECOND_ORDER_V1
## Recovery capsule part 2 of 2: full continuous theorem, actual control, negative architecture, and exact recovery

This is a new own-volume-centroid regularization result for a specified three-contact sector, NOT a class110 construction, NOT an exclusion of E17, and NOT an improvement of 34<=C_min<=622. The actual control has V/E/F=7/12/7 and strict S/U/H=5/4/7. The minimality problem and a universal theorem for arbitrary three or more weak contacts remain open.

The preceding complete two-contact result is immutable assignment minimum-0076, SHA256 bb5b0d967434487f3ef8fb86e4712d48c753bc31e44a89fb37e791e96bb86a79. It was read from cursor0 through EOF. The theorem below is proved here, rather than inferred from its two-contact statement. Physical contacts are geometric points. A simple A contact is a vertex-edge contact, a simple B is an edge-facet contact, and a vertex-facet packet is one point with two alternative escape inequalities, not two contacts.

## 1. Own-centroid projective differentiation

Let P be a full-dimensional uniformly filled convex polytope with its actual volume centroid0 and ordinary Euclidean metric. Put Sigma=E_P[xx^T]>0 and L=5Sigma. For a vector p and sufficiently small real t, the projective map T_t(x)=x/(1+t p.x) has positive denominator throughout P, hence preserves convexity and the entire face lattice. The image is again filled UNIFORMLY; we are not transporting a fixed mass density. Let g(t) be its true new volume centroid, and recenter every image point by subtracting g(t).

The Jacobian is (1+t p.x)^(-4). Therefore

g(t)=E_P[x(1+t p.x)^(-5)]/E_P[(1+t p.x)^(-4)].

Since E_P[x]=0, differentiation at0 gives g'(0)=-5Sigma p=-Lp. Everything is real analytic for small t, either from this integral on a fixed compact body or from an unchanged exact tetrahedral fan. In particular no free reference center or separately centered polar is being introduced.

For a simple A contact let z be its vertex and z+u the other endpoint of its genuine exposed edge. Then z.u=0. Its signed affine escape function is phi=z^T M u, where M=B^T B is one SPD metric induced by an actual affine map B. Positive phi removes the local weak vertex-edge pair without creating a new strict equilibrium; negative phi produces the local unstable/saddle pair. This follows directly by restricting squared distance to z+su: its derivative at s=0 is2phi and its second derivative is2u^T M u>0, while the other normal-cone guards are strict at a simple contact. All other strict or inactive features remain in their original sign chambers under sufficiently small deformation.

Write S(a,b)=(ab^T+ba^T)/2 and T=S(z,u). For the true recentered projective images z(t),u(t),

z'(0)=Lp-z(p.z),
u'(0)=-(p.(z+u))u-(p.u)z.

Consequently T(t)=S(z(t),u(t)) has derivative

D(p)=S(Lp,u)-(p.(2z+u))T-(p.u)zz^T.                 (1)

In particular tr D(p)=u.(L-|z|^2 I)p. The same one body's L occurs in every row. A subsequent affine B acts on the already recentered uniform body and therefore leaves its true centroid at0.

## 2. A unique-positive-stress rescue lemma

Here is an analytic matrix lemma with a geometric application, valid for any number k allowed by the rank assumptions. Suppose the only weak physical contacts of P are k simple A contacts (z_i,u_i). Set T_i=S(z_i,u_i). Suppose their rank as vectors in Sym(3) is k-1, and their unique dependence has strictly positive coefficients:

sum_i alpha_i T_i=0, alpha_i>0.

Let W=span{T_i}, and use the trace inner product <A,B>=tr(AB). For a fixed p expand the actual projective rows

T_i(t)=T_i+t D_i+t^2 E_i+O(t^3),
D(p)=sum_i alpha_i D_i.

The following sufficient alternatives each permit arbitrarily small own-centroid projective-then-affine regularization of all k contacts, preserving the face lattice and every original strict equilibrium:

(a) tr D(p) is nonzero for some p;
(b) tr D(p)=0 for all p, but D(p) is outside W for some p.

PROOF. The linear map R:Sym(3)->R^k, R(H)_i=<H,T_i>, has rank k-1 and image alpha-perp. Set A=sum_i alpha_i>0.

In case(a), change p to -p if necessary so s=tr D(p)>0. Choose H satisfying R(H)_i=s/A-tr D_i; this is compatible because its alpha-weighted sum is s-s=0. With M(t)=I+tH, each escape function <M(t),T_i(t)> has first coefficient s/A>0. Thus all are positive for small positive t.

In case(b), choose p with D outside W. Let K be the orthogonal projection of D onto W-perp; K!=0 and <K,D>=||K||^2. First choose H0 satisfying R(H0)_i=-tr D_i, which is compatible because tr D=0. For H=H0+aK, all first coefficients still vanish. The alpha-weighted second coefficient of <I+tH,T_i(t)> is

beta(a)=tr(sum_i alpha_i E_i)+<H0,D>+a||K||^2.

Choose any finite a making beta(a)>0. Let c_i=tr E_i+<H,D_i>. There is J with R(J)_i=beta(a)/A-c_i, because its alpha-weighted sum is zero. Then for M(t)=I+tH+t^2J,

<M(t),T_i(t)>=(beta(a)/A)t^2+O(t^3)>0

for every i and sufficiently small positive t. Since M(0)=I, it is SPD for all sufficiently small t. Use its unique positive-diagonal upper-triangular Cholesky factor B(t), with B(t)^T B(t)=M(t), as an actual Euclidean affine map. The projective map preserves the face lattice; recentering uses exactly the uniform-volume centroid; the affine map preserves that center. Positivity of all selected simple-contact escape functions removes them, and the finitely many other open physical guard conditions preserve all original strict equilibria and exclude new weak contacts. This proves both alternatives.

The statement is intentionally conditional. It does not prove every three-contact configuration satisfies(a)or(b). It is not asserted for mixed A/B rows by simply writing independent metrics: primal rows depend on M and polar rows on M^-1, whose joint second-order expansion needs additional terms. Vertex-facet packets also require their own alternatives. Neither of these unresolved sectors has been silently included.

## 3. Entire cyclic three-contact sector

In an orthonormal frame take

z1=(1,1,0), z2=(0,1,1), z3=(1,0,1),
d1=(1,-1,0), d2=(0,1,-1), d3=(-1,0,1),
u_i=h_i d_i with h_i>0.

Suppose these are genuine exposed edges of an actual own-centered convex polytope and its only weak physical contacts are the three simple A contacts at z_i. No restriction is placed on the rest of its vertices or facets beyond those hypotheses. Orthogonal similarities and common positive rescalings give the corresponding invariant sector.

Then T1=h1 diag(1,-1,0), T2=h2 diag(0,1,-1), T3=h3 diag(-1,0,1). They span exactly the diagonal trace-zero plane W and have unique positive stress alpha_i=1/h_i. Also

sum_i alpha_i u_i=sum_i d_i=0,
sum_i alpha_i |z_i|^2 u_i=2sum_i d_i=0.

Thus tr D(p)=0 for EVERY p and EVERY actual covariance Sigma. Every first own-centroid projective-affine deformation has alpha-weighted contact derivative zero. Moreover sum_i alpha_i z_i^T M u_i=0 for every symmetric M, so no affine map of any size makes all three escape functions positive simultaneously. In particular small affine changes alone cannot remove all three while preserving the original strict counts.

Nevertheless the off-diagonal entries of the actual weighted projective tensor variation (1) are

D12=-(p1-p2), D23=-(p2-p3), D31=-(p3-p1).       (2)

Indeed the L-dependent sum S(Lp,sum_i d_i) vanishes. The middle term of(1) is diagonal, and the final term contributes exactly(2). Hence D(p) is outside W whenever p is not parallel to(1,1,1). Alternative(b) of the lemma applies. EVERY actual body in this three-only cyclic sector admits an arbitrarily small second-order own-centroid projective-affine regularization, despite its first-order and all-affine-order stress barriers. A first-jet obstruction is therefore not an all-orders projective obstruction.

## 4. A literal actual three-only control

A complete exact recovery of an actual body satisfying the hypotheses is in part1, material [internal-source-reference]. It has h=(1/4,1/2,3/4), six base vertices listed in index order and one apex:

v0=(1,1,0), v1=(5/4,3/4,0),
v2=(0,1,1), v3=(0,3/2,1/2),
v4=(1,0,1), v5=(1/4,0,7/4),
v6=(-17/10,-79/40,-93/40).

The convex hexagonal base is in x+y+z=2, with oriented boundary[0,3,2,5,4,1]. Its actual area centroid is C=(17/30,79/120,31/40), and the apex is -3C. The uniform pyramid centroid is (3C+v6)/4=0. The exact volume is10/3. Exhaustive rational support enumeration gives V/E/F=7/12/7, with maximal facet cycles

[0,3,2,5,4,1], [0,1,6], [0,6,3], [1,4,6], [2,3,6], [2,6,5], [4,5,6].

Their poles q, in that order and normalized by q.x<=1, are

(1/2,1/2,1/2),
(1/2,1/2,-227/186),
(-13/134,147/134,-173/134),
(143/94,-113/94,-49/94),
(-63/34,1/2,1/2),
(-127/66,71/462,391/462),
(1/2,-241/158,1/2).

The true uniform covariance is

Sigma=((1/4,323/1600,73/320),(323/1600,541/1600,1/4),(73/320,1/4,723/1600)).

It is independently obtained by exact signed tetrahedral integration and is positive definite. All facet support inequalities, all maximal facets and genuine edges, exact volume/centroid/covariance, and all physical primitives are recomputed by part1 rather than being assumed from a supplied incidence drawing.

Initial strict stable facets are[0,2,3,5,6]; unstable vertices[1,3,5,6]; saddle edges[0,3],[1,4],[1,6],[2,5],[3,6],[4,6],[5,6]. Thus strict S/U/H=5/4/7. The only weak physical points are v0,v2,v4, on genuine edges01,23,45. Each radial support plane at z_i exposes EXACTLY its two edge endpoints, proving it is simple A and not a vertex-facet packet. There are exactly three zero primitives among all48; no weak facet contacts are present. The coincidence of a weak-vertex label and its adjacent weak-edge label is the SAME physical point, not an extra equilibrium.

For completeness the initial four edge primitives (primal at each listed endpoint followed by the two true-polar primitives) are:

01:[0,-1/8,-80/93,-18160/8649]
03:[-1/2,-1,-60/67,-13580/4489]
06:[-227/40,-12697/800,49940/579483,-335660/417477]
14:[-7/8,-3/4,-40/47,-9128/2209]
16:[-917/160,-6321/400,-485240/406503,-664664/205437]
23:[0,-1/2,-20/17,-1260/289]
25:[-1/4,-11/8,-40/33,-29080/5929]
26:[-63/10,-13197/800,420/3179,-114020/302379]
36:[-53/8,-13057/800,-213440/76313,-74560/19363]
45:[0,-9/8,-80/79,-19280/6241]
46:[-241/40,-12977/800,-296232/174511,-144600/293327]
56:[-1219/160,-1669/100,-7329320/1405173,-5189960/1441671].

These use one M=I and N=M^-1. In general part1 uses primal a^T M(b-a), b^T M(a-b) and polar q^T N(r-q), r^T N(q-r). All four strictly negative give a strict edge saddle; all nonpositive with some zero give a weak edge point; a positive primitive excludes that edge from equilibrium. Vertex and facet tests use their full respective incident lists.

## 5. An explicit metric arc and a WHOLE interval certificate

Take p=e1 and 0<t<=1/1024. Transform vertices by Y_i(t)=v_i/(1+t v_i,1), compute the actual uniform centroid g(t) by the unchanged tetrahedral fan, and set X_i(t)=Y_i(t)-g(t). The true recentered poles are

q_i(t)=(q_i+t p)/(1-(q_i+t p).g(t)).

No polar recentering is performed. Independently, the transformed body's pyramid-area formula gives the same g(t) identically. Its first two coefficients are

g'(0)=(-5/4,-323/320,-73/64),
[t^2]g(t)=(-369/640,-14799/12800,-3961/2560).

Here the weighted D of(1) and its component orthogonal to W are

D=((-1,-1,1),(-1,5/4,0),(1,0,-1/4)),
K=((0,-1,1),(-1,0,0),(1,0,0)), ||K||_F^2=4.

Use the one exact metric

M(t)=I+t H1+t^2 H2,
H1=diag(121/64,21/160,0)+(459/640)K,
H2=diag(206441/102400,156241/51200,0),
N(t)=M(t)^(-1).

The three contact functions satisfy phi_i(t)/(h_i t^2)=1+O(t), with the actual centroid included. This is not merely a formal jet calculation: part1 proves exact positivity on the ENTIRE closed[0,1/1024] of every projective denominator, every leading principal minor of M, every recentered facet denominator, all45 originally nonzero primitive sign guards, and each rational quotient phi_i/(h_i t^2). Thus on the entire positive interval all old strict equilibria are unchanged and no weak equilibria remain. The physical Euclidean body is conv{B(t)X_i(t)}, with B the unique positive-diagonal upper-triangular Cholesky factor B^T B=M. This fixes every square-root choice, keeps the true centroid0, and changes the true volume by det B. Exact algebraic Euclidean coordinates are recovered at t=1/1024.

The interval proof uses no sampling. For every rational guard f=n(t)/d(t), the denominator sign is normalized positive at0. The complete power coefficients of n,d are then converted to Bernstein coefficients on[0,e],e=1/1024. For a polynomial P(t)=sum_{j=0}^m a_j t^j, these are

b_k=sum_{j=0}^k a_j e^j binom(k,j)/binom(m,j), 0<=k<=m.

All b_k are exact positive rationals, separately for numerator and denominator. Bernstein basis functions are nonnegative and sum to1, so this proves strict positivity on the whole closed interval. Part1 computes and stores every power coefficient and minimum Bernstein coefficient in the deterministic report and asserts positivity. The three quotient denominators are nonzero at0 after exact cancellation. The endpoint is additionally checked by a new exact hull enumeration, matching the original maximal facets and edges, exact own-centroid integration, full equilibrium census, and an exact Cholesky identity. These finite exact computations prove the stated continuum signs and reconstruct the same complete object without its original sandbox.

## 6. A preserved negative control and correction of the original proposal

The initially proposed equal-parameter pyramid, h1=h2=h3=1/2 with apex(-2,-2,-2), is NOT a three-only control. Its exact own volume is10/3, strict S/U/H=4/4/6, and it has SIX physical weak contacts: three A at z_i and three B in the interiors of the three apex-z_i edges. Part1 reconstructs it completely and certifies its census. Thus the first proposal in the branch/brief must not be silently relabeled as the accepted unequal-parameter object.

This failure is architectural for the cyclic equal-h family0<h<1, not a roundoff artifact. Cyclic symmetry places the base area centroid at(2/3,2/3,2/3), hence its own-centered pyramid apex is(-2,-2,-2). One side triangle has pole q=(1/2,1/2,-3/2), independently of h, with cyclic copies for the other two. Its perpendicular foot is q/|q|^2=(2/11,2/11,-6/11)=(8/11)z1+(3/11)apex, in the relative interior of the apex-z1 edge. As that foot is a positive multiple of the single triangle pole, it is an edge-facet boundary-normal contact, distinct from z1. The three cyclic copies force three extra B contacts in addition to the three A contacts. At h=1/2 exact enumeration shows these are all six. The unequal choice h=(1/4,1/2,3/4) changes the actual area centroid/apex and removes these additional weak contacts; its complete actual census, not merely formal stress tensors, establishes the desired control.

## 7. Durable reconstruction manifest

Part1 is immutable material [internal-source-reference], whose ENTIRE text is the runnable source. Save it without wrappers or edits as cyclic3_own_com.py. It is13869UTF-8bytes, SHA256 d4c0ebaf51a2dfeebc40b08338f82fb6b3023b1a05fade40bc2c91bb0f659e1f. This part2 is the full geometric proof and recovery protocol; it is not an additional computational input. No other material, local file, checkpoint, seed, external service or solver is needed. All vertex coordinates, h_i, p, metric coefficients, interval endpoint, symmetrized negative control, and square-root choices are literal or deterministically specified in part1.

Reference environment: CPython3.13.5, SymPy1.14.0, assertions enabled. Do not run Python with-O. SymPy is the only nonstandard dependency. Reconstruction command, in the source directory:

python cyclic3_own_com.py build > build_stdout.txt

Verification command, recomputing every proof quantity and comparing all report bytes:

python cyclic3_own_com.py check > check_stdout.txt

Expected reproduced file cyclic3_own_com.json:110019bytes, SHA256 c2f96e68a25eb4dd36e22d7ccc7a410c4f75974367d99dd4c1c1d2e52d481ac3. It contains all initial and endpoint geometry, both true metric matrices, exact actual centroid functions, all48 primitives, complete interval polynomial certificates, the failed symmetric control, exact positive-Cholesky Euclidean endpoint vertices, and the full equilibrium censuses.

Both build_stdout.txt and check_stdout.txt are437bytes, SHA25672469bce32d13f228a0708484044421bf8a20ed2f0e324a78a68bbfda6624408. Their complete contents are:


[Encoded source block omitted; the code in this passage is incomplete.]

CYCLIC3_OWN_COM_SECOND_ORDER_RECOVERY_PASS

A cold replay was performed starting from only the exact source in a fresh directory, followed by build and check. All report and stdout byte counts and hashes above matched. These hashes identify the recovered bytes; they do not replace either the complete generator or the continuous geometric proof. The source and proof together preserve both the new successful non-record construction and the meaningful failed symmetric architecture.

## 8. Research significance and limits

This result exhibits a genuine own-centered polyhedron whose three weak contacts have an obstruction to every strictly positive first projective-affine jet and every affine-only rescue, yet all are removable by a single actual second-order projective-affine arc. It establishes an entire continuous cyclic three-only sector, not just this rational point. The unique-positive-stress matrix lemma supplies a further reusable sufficient criterion outside that sector.

It does not establish general regularization for arbitrary three A contacts, for multiple independent positive stresses, for mixed A/B contacts, or for vertex-facet packets. It does not create a weak110 body or a strict110 attainer. Since the explicit body's strict counts are5/4/7, its C=24 has no bearing on the accepted lower bound for110. No FULL/LOCAL count, root-class census, V>=10,F>=9, or bracket34<=C_min<=622 is changed. A useful next question is whether genuine three-contact support geometry forces the stress variation outside its original row span whenever its own-centroid first derivative vanishes; the mixed-type inverse-metric terms must be handled separately rather than omitted.
