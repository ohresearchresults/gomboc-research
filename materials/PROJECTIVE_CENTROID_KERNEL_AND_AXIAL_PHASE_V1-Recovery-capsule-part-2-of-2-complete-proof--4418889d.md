# material-4418889d8c20

Historical AI scientific source/proof material. Statements retain their original scope; this is not an independently reviewed theorem.

Public derivative: internal-record-identifiers-replaced; unreviewed-encoded-blocks-omitted.

---

# PROJECTIVE_CENTROID_KERNEL_AND_AXIAL_PHASE_V1
## Recovery capsule part 2 of 2: complete analytic proof, exact controls, scope and reconstruction

This is coordinator research. It supplies a global rational polyhedral enclosure of the unique actual uniform projective-centering parameter, a strict mechanical sign theorem from NONSTRICT kernel inequalities, a rational parametrization of actual axial centering, and a full genuine mechanical phase classification for an axial square-prism family. It neither constructs a new own110 body nor excludes the entire10/17/9 layer. Accepted bounds remain34<=Cmin<=622. The computational source and proof form one recovery capsule; no other source is needed to reconstruct its controls.

## 1. Objects and actual uniform centering

Let K be a bounded full-dimensional convex3-polytope with0 in its interior, genuine vertices x_i and genuine maximal facet poles q_f, so K={x:q_f.x<=1}. Put f_i(p)=1+p.x_i and D={p:f_i(p)>0 for every i}=int(-K^polar). For p in D, T_p(x)=x/(1+p.x) preserves the whole face lattice and the origin. The image is filled UNIFORMLY; mass is not projectively transported. Its poles about0 are q_f+p.

There is exactly one p*=p*(K) for which T_p*K has actual uniform volume centroid0. Here is a self-contained justification. Its volume is Phi(p)=integral_K(1+p.x)^(-4)dx. Direct differentiation gives gradPhi=-4 integral_K x(1+p.x)^(-5)dx and HessPhi=20 integral_K xx^T(1+p.x)^(-6)dx>0. Change of variables, with Jacobian(1+p.x)^(-4), identifies gradPhi=-4 Phi g(T_pK), where g is the true image centroid. The domain D is bounded because0 is interior to K. If p approaches its boundary, at some vertex x the positive denominator delta tends to0. A fixed full-dimensional tetrahedral cone in K with apex x contains a sub-tetrahedron of linear size delta on which the denominator is at most C delta, uniformly for bounded p. Its volume is at least c delta^3, so its contribution to Phi is at least c' delta^(-1). Thus Phi diverges at every boundary point. The strictly convex function has a unique interior minimum, where and only where the actual image centroid vanishes. This existence/uniqueness is also the known projective-centering theorem; no novelty is claimed for it. All later mechanical rows refer to the own centroid ONLY at p* unless explicitly recentered.

## 2. Sharp actual-centroid support inequality, including equality

If a uniformly filled3-polytope Q has centroid0, then for every facet pole a and every vertex y,

    a.y >= -3.                                                     (2.1)

Let y0 minimize a.x on Q, with value m. Triangulate Q by tetrahedra with apex y0 and triangles on the nonincident boundary facets. Every positive-volume tetrahedron has its other three vertices at a-projection at most1. Its centroid projection is therefore at most(m+3)/4. Their positive-volume-weighted centroid is0, so0<=(m+3)/4. This proves(2.1).

If equality a.y=-3 holds for any vertex y, then y is a minimum vertex and equality holds in every positive tetrahedron of the y-fan. Every other vertex of every positive tetrahedron belongs to the plane a.x=1. The whole body is consequently the pyramid conv(y,F_a), with y its apex and F_a the entire opposite maximal facet. Conversely, the pyramid centroid is(one apex+three times the base area centroid)/4, so any own-centered pyramid satisfies a.y=-3 for its apex/opposite-base pair. Thus equality is exactly this geometric pyramid situation, not an arbitrary low-rank moment condition.

A nontetrahedral3-pyramid has a unique apex. Removing any base vertex still leaves at least three noncollinear base vertices and the apex, which are not coplanar. A tetrahedron is the exceptional body that is a pyramid at every vertex.

## 3. The global centroid kernel

Define the positive rational quantities, when K is rational,

    tau_i = (1/4) max_f(1-q_f.x_i),
    P_K = {p:1+p.x_i >= tau_i for every genuine vertex i}.          (3.1)

Then

    p* belongs to P_K,
    P_K is compact, and P_K is compactly contained in (3/4)D.       (3.2)

Proof: projective incidence gives the exact slack identity

    1-(q_f+p).T_p(x_i) = (1-q_f.x_i)/(1+p.x_i).                    (3.3)

At actual centering, (2.1) says the left side is at most4. Taking the maximum over f gives(3.1). For each nonzero vertex x_i, min_f q_f.x_i<0 because0 is interior to the polar polytope. Hence tau_i>1/4. The constraints in(3.1) therefore imply1+p.x_i>1/4, equivalently p/(3/4) in D. Since there are finitely many positive gaps tau_i-1/4, P_K is a closed bounded subset strictly inside(3/4)D.

This is at most V affine inequalities, requiring true vertex/facet geometry but no volume integration and no centering root. It is an OUTER enclosure, not an exact characterization of p*.

If K is not a pyramid, every inequality in(3.1) is strict at p*, by the equality classification in Section2. Consequently P_K is full-dimensional and p* is interior to it. If K is a nontetrahedral pyramid, exactly one constraint is active at p*: the constraint of its unique apex. Every other vertex constraint is strict. Locally P_K is one halfspace, so it is full-dimensional and p* is in the relative interior of that facet. For a tetrahedron P_K is a singleton, as established explicitly below.

The universal factor3/4 cannot be replaced by any smaller fixed factor. Consider

    K_eps=conv(-e1,-e2,-e3,eps*(1,1,1)), eps>0.

Its centering parameter is p*=((eps-1)/(4eps))*(1,1,1), and its last vertex denominator is(1+3eps)/4. The centered image vertices are all multiplied by the same positive scale4eps/(1+3eps) from the fixed own-centered tetrahedron{-e1,-e2,-e3,(1,1,1)}. As eps tends to0, the minimum denominator tends to1/4 and the gauge in D tends to3/4. The limiting coefficient is not attained by a full-dimensional K containing0 strictly.

More generally, if a tetrahedron contains0 with positive barycentric coefficients beta_i, then its facet opposite x_i has q_i.x_i=1-1/beta_i, so tau_i=1/(4beta_i). Since sum_i beta_i x_i=0, sum_i beta_i f_i(p)=1 for every p. All four kernel lower bounds sum to1, so all must be equalities. Three independent equations determine p uniquely. Thus P_K={p*}.

## 4. Fixed preimage point and the full-orbit scope warning

For fixed r in intK, the unique p for which g(T_pK)=T_p(r) satisfies

    4(1+p.x_i)(1-q_f.r)
       >= (1-q_f.x_i)(1+p.r) for every i,f.                       (4.1)

To prove this, recenter Q=T_pK at T_pr. Its normalized facet pole is

    (q_f+p)/[1-(q_f+p).T_pr].

The slack at its centered vertex is, using(3.3),

    (1-q_f.x_i)(1+p.r)/[(1+p.x_i)(1-q_f.r)].

Apply(2.1). For FIXED r the inequalities(4.1) are affine in p. One can equivalently put u=p/(1+p.r) and apply the origin-centering theorem to K-r; the two centered images differ by an invertible linear map. Thus there is a unique p for fixed r. As r varies, these inequalities give necessary joint(p,r) conditions for the true moving image centroid, but they do not replace that actual centroid relation.

IMPORTANT: P_K encloses the unique parameter that centers about the SPECIFIED reference0. It does not enclose every raw parameter in the full positive projective orbit when that raw image is subsequently translated by its different own centroid. Discarding p outside P_K in a full-orbit U1 search is invalid. Similarly, for already own-centered K, p*=0; origin-fixing projection followed by centering about that same origin merely undoes the projectivity. Actual shape change or reference change is needed for compression.

## 5. All primitive mechanical rows are affine before actual centering

Fix ONE positive definite symmetric M, with N=M^(-1). For an oriented genuine edge i->j, define

    A_ij=x_i^T M(x_j-x_i),
    B_ij=(x_i^T M x_j)x_i-(x_i^T M x_i)x_j,
    h_ij(p)=A_ij+B_ij.p.                                         (5.1)

Then the true reference0 primal primitive for the image edge is

    T_px_i^T M(T_px_j-T_px_i)=h_ij(p)/(f_i(p)^2 f_j(p)).           (5.2)

For adjacent genuine facet poles q_f,q_h, the dual primitive is

    (q_f+p)^T N(q_h-q_f)
       =q_f^T N(q_h-q_f)+[N(q_h-q_f)].p.                         (5.3)

The denominator in(5.2) is positive. All4E rows are therefore affine-sign tests in the SAME p and SAME reciprocal pair. They are actual-own mechanical rows at p*, not at arbitrary p.

Every such affine row is nonconstant. The primal endpoints x_i,x_j are linearly independent: an edge line through interior0 is impossible, and two same-ray extreme vertices are impossible. Since x_i^TMx_i>0, B_ij cannot vanish. Distinct adjacent poles and invertible N give a nonzero dual gradient.

## 6. Strict mechanics from nonstrict polyhedral inequalities

THEOREM. Suppose K is not a tetrahedron. If any primitive affine row h of(5.1) or(5.3) satisfies h(p*)=0, then h takes both strictly positive and strictly negative values on P_K. Consequently

    h>=0 on P_K implies h(p*)>0,
    h<=0 on P_K implies h(p*)<0.                                (6.1)

The inequalities on P_K may be NONSTRICT, and checking its finitely many vertices suffices. There is no need for a positive LP margin. This statement concerns genuine mechanical rows; it is false for arbitrary affine functions on a pyramid.

For nonpyramids the proof is immediate: p* is an interior point of the full-dimensional P_K and h has a nonzero gradient. The pyramid case requires the actual geometry.

First rebase the entire assertion at the centered image K'=T_p*K. If u is a further origin-fixing parameter, then T_u T_p*=T_(p*+u). The new vertex slacks are scaled by1/f_i(p*), hence P_K'=P_K-p*. Its primal affine numerators are those for K at p*+u divided by the fixed positive factor f_i(p*)^2 f_j(p*); its dual affine rows agree exactly. We can therefore assume p*=0 and K own-centered without changing the sign question.

Let a be the unique apex of a nontetrahedral pyramid. At0 the only active kernel inequality has normal a. Any affine h that vanishes at0 and is one-sided on P_K must have gradient parallel to a: locally P_K is the halfspace a.p>=0, and all directions tangent to it occur with both signs.

For a primal row on x->y, write u=y-x. At a weak value x^TMu=0, the gradient in(5.1) reduces to

    B=-||x||_M^2 u.                                              (6.2)

Parallelism to a would require the genuine edge vector u to be parallel to a. A base edge is tangent to the base, whereas the base pole q_0 satisfies q_0.a=-3, so a base edge cannot be parallel to a. A side edge between a base vertex b and a can be parallel to a only if b=-a/3, by the base equation q_0.b=1. Neither oriented primitive on that edge vanishes: their values are negative nonzero multiples of ||a||_M^2. Thus(6.2) cannot be parallel to a at a zero primitive.

For a dual row, its gradient D=N(q_h-q_f) is nonzero. If D=c a, its value at0 is q_f.D=c(q_f.a), and q_f.a is either1 for a side facet or-3 for the base facet. This cannot vanish. Therefore no zero dual primitive can have the required normal either. The one-sided supposition is impossible, proving the theorem.

Applications: nonstrict rational linear inequalities at the vertices of P_K can prove strict selected escape arrows at the actual own centroid. Positive arrows on a primal spanning tree directed toward one root and on the complementary dual spanning tree directed toward one dual root suffice for strict110 with no weak packets, by the established tree-cotree equilibrium criterion. All4E signs can instead certify the full census. A row that straddles P_K is simply unresolved by this enclosure, not an exclusion and not a weak equilibrium. A successful sign theorem does not guarantee the desired110 signs exist for the input body.

The tetrahedron exception is essential, not just a proof limitation. On K=conv(-e1,-e2,-e3,(1,1,1)), choose

    M=[[1,-1,-1],[-1,3,0],[-1,0,3]].

Its leading principal minors are1,2,3, so M is SPD. K is own-centered and P_K={0}. It has one physical VE weak point on edge(0,3) under the listed vertex order, strict(S,U,H)=(4,3,5). The zero primitive is zero on the whole singleton kernel, so neither nonstrict sign can be promoted to strict.

## 7. Symmetry sections and a genuine failure of careless restriction

If a linear map H preserves K and0, uniqueness of actual centering implies H^(-T)p*=p*. Thus p* lies in the linear fixed subspace L of the dual symmetry group. If K is NOT A PYRAMID, p* is in the relative interior of P_K intersect L. Any affine row that is nonnegative there and not identically zero on that section is strictly positive at p*, and likewise for negative signs. This is ordinary relative-interior affine geometry, not a symmetry requirement on M. It can improve the full kernel test substantially.

Do not extend that nonstrict section rule blindly to pyramids. Consider the exact own-centered square pyramid with lexicographic base order

    (-1,-1,-1),(-1,1,-1),(1,-1,-1),(1,1,-1),(0,0,3)

and

    M=[[8,0,13/5],[0,1,0],[13/5,0,1]], detM=31/25>0.

Its actual strict census is(S,U,H)=(4,3,5), with two physical VE weak points on edges(2,4),(3,4). Every zero primitive strictly straddles the FULL kernel, in accord with Section6. The symmetry-fixed vertical section, however, is0<=p_z<=1/3. On that section each physical zero row is nonpositive and nonconstant but vanishes at p*=0. Thus the pyramid section would falsely certify strict negativity. The source retains all exact rows and bounds. Also the generic affine function3p_z is nonnegative on the full kernel and zero at p*, illustrating why the full-kernel theorem was specifically mechanical. Strict positive margin on any valid containing section remains safe; it is the promotion of nonstrict to strict that needs the hypotheses above.

## 8. Rational parametrization of actual centering for axial prisms

Let B be any planar convex body of positive area and area centroid0. Let K_a=[-1,a] times B, a>0. For every k>0 put

    r=1+k+k^2, q=1+2k+3k^2,
    a(k)=(3+2k+k^2)/(k q),
    t(k)=(1-k)q/(4r).                                           (8.1)

Then the uniformly refilled image T_(t,0,0)K_a has actual volume centroid0. No reflection symmetry of B is required beyond its area centroid being0.

Proof: the image is a homothetic frustum whose axial endpoints are L=-1/(1-t), R=a/(1+at), with ratio of right to left cross-section scale k=(1-t)/(1+at). Its section centroids lie on the axis. In the unit fractional axial coordinate u=(z-L)/(R-L), section area is proportional to(1+(k-1)u)^2. Direct integration gives its centroid fraction

    eta=integral_0^1 u(1+(k-1)u)^2du /
            integral_0^1 (1+(k-1)u)^2du
       =(1+2k+3k^2)/(4(1+k+k^2)).                               (8.2)

The origin has fraction-L/(R-L)=(1+at)/(1+a)=1/(1+ak). Equating to eta yields a(k), and solving k=(1-t)/(1+at) yields t(k). The denominators1-t and1+at are positive from these formulas. The transverse centroid is0 by the homothetic centered sections. This is the actual three-dimensional integral, not a transported centroid.

The derivative of a(k) has positive denominator[k(1+2k+3k^2)]^2 and numerator

    -3-12k-30k^2-12k^3-3k^4<0.

Its limits are infinity at k down0 and0 at k to infinity. Thus(8.1) parametrizes the ENTIRE positive-a centering curve, not merely several samples. Also

    t'(k)=-3k^2(k^2+2k+3)/(4(1+k+k^2)^2)<0.

For k<=1, a>=1 and0<=t<1/4. Rational k gives exact rational a,t and rational image vertices when B is rational. This does not contradict the irrational algebraic centering parameter that can occur for a fixed rational a. It is a rational parametrization of the algebraic curve by a different parameter.

## 9. Full axial mechanical phase, including all four weak walls

Take B=[-1,1]^2 and the SAME actual image from Section8, with M=diag(m,1,1), m>0, N=diag(1/m,1,1). It has true(V,E,F)=(8,12,6). For any positive admissible a,t that is actually centered, its strict counts are

    U=4*1[t>-m/2]+4*1[t<a m/2],
    S=2+4*1[-m<t<a m],
    H=4*(1[-m/2<t<a m/2]+1[t>-m]+1[t<a m]).                     (9.1)

Each wall t=-m/2 or t=a m/2 has exactly four physical VE weak points. Each wall t=-m or t=a m has exactly four physical EF weak points. There are no other zero primitives or physical VF packets on these walls. The walls are distinct for a,m>0. Away from them the family is weak-free.

Proof enumerates genuine edge types, not an abstract count. A longitudinal edge connects(c,sigma,tau) to(d,sigma,tau), where{c,d}={-1,a}. Its two primal affine numerators are

    (a+1)(-m-2t),   (a+1)(2t-a m).

Its two dual primitives, from adjacent transverse poles, are both-1. A transverse edge at axial end c=-1 or a has two primal numerators-2(1+ct), strictly negative. The end-facet to side-facet dual primitive is-(1+ct)/(m c^2)<0, and the reverse is-1+t/(m c). The two axial facets are always strict stable; each of the four side facets is stable exactly when both reverse rows are negative. A vertex is unstable exactly when its sole longitudinal outgoing row is negative, since its other two rows are negative. Testing all four rows in each genuine edge packet gives(9.1), the listed weak walls and no VF packet. The same reciprocal pair is used throughout.

In particular S>=2 and U>=4 for this entire axial-metric family, so it never contains110. This is NOT an all-SPD exclusion for arbitrary projective frusta.

A root-free continuous consequence uses Section7: for EVERY a>=1 and M=I, the two transverse reflection symmetries put p* on the axis, and

    P_K intersect axis = [(a-3)/(4a),1/2].                       (9.2)

Indeed tau_left=1/2 and tau_right=(a+1)/4. The box is not a pyramid, so p* is strictly interior to the section. At both endpoints all48 affine primitive rows are nonpositive and none is identically zero on the section. This follows directly from the four formulas above: lower endpoint>=-1/2, upper endpoint<=a/2, lower endpoint>=-1 and upper endpoint<a for a>=1, with the displayed positive denominators. Section7 promotes every row to strictly negative at p*. Hence the whole unbounded a>=1 family has strict(S,U,H)=(6,8,12), weak000, without solving t or integrating the centering root. Do NOT extend that same census to all0<a<1: the phase formula can change there.

## 10. Exact controls, completed execution and negative boundaries

The complete source projective_kernel.py uses only fractions.Fraction and the standard library. It reconstructs every true maximal facet from all supporting triples, merges coplanar triangles, computes genuine facet intersections/edges, checks every input vertex has three independent incident poles, checks Euler and face cycles, and triangulates all outward facets. Actual volume/first moments are computed by two positive tetrahedral fans: the origin and vertex0. The latter may contain zero tetrahedra, which are explicitly allowed and do not contribute. Both fans agree exactly. All own-centroid claims require first_moment exactly0. Raw body records also retain their actual centroid, but their recorded mechanical rows are reference0 rows unless that centroid is0.

It enumerates the vertices of P_K by every independent triple of bounding hyperplanes and all exact inequalities. It uses one SPD M and exact inverse N, verifies all4E affine formulas against direct transformed-body rows, and performs complete physical packet tests. The report contains all literal rational vertices, facets, edges, triangles, poles, moments, metrics, affine rows and kernel bounds; there are no omitted arrays or seeds.

Control groups:

1. Boxes a=1,3/2,2,10: all kernels have six vertices. The cube kernel is{|p_x|+|p_y|+|p_z|<=1/2}; all48 rows are nonpositive on it. At a=3/2, the six kernel vertices are(-1/4,0,0),(1/2,0,0),(1/20,+/-9/20,0),(1/20,0,+/-9/20). For each asymmetric listed box the FULL kernel straddles eight primal rows, even though the symmetry-axis section certifies all48. This demonstrates a real limitation of the unrestricted enclosure, not a physical weak point or failure of the actual centering.

2. k=1/100,1/2,1,2,100: exact rational actual centering and all phase regions/walls,26 metric controls in total. At k=1/2, a=34/11,t=11/56. With m=121/3808 the census is(2,4,4,0); m=121/1904 gives(2,4,4,4), an EF wall; m=363/3808 gives(6,4,8,0); m=121/952 gives(6,4,8,4), a VE wall; m=363/1904 or1 gives(6,8,12,0). At k=2, a=11/34,t=-17/28, the negative EF/VE walls are m=17/28 and17/14. These bodies differ from fixed-a irrational-root controls in earlier capsules.

3. eps=1,1/10,1/100 in Section3: singleton kernels, true rational own-centered tetrahedra, exact sharpness denominator(1+3eps)/4, strict(4,4,6), weak0 under I.

4. The genuine square pyramid in Section7: ownCOM0, strict(4,3,5), two VE points, all zero rows strictly straddling the full kernel, yet each physical zero row one-sided on the symmetry axis. This is the retained countercontrol to an invalid symmetry extension, not an own110 candidate.

5. The tetrahedron in Section6: ownCOM0, one VE point and singleton kernel. This proves the tetrahedron exception is physically necessary.

Finite controls do not by themselves establish universal geometry; Sections1-9 give the continuous arguments. They also do not prove any new bound on the minimum. No independent worker-result replay is involved: these are the coordinator's own newly computed controls.

## 11. Exact recovery protocol and pins

Recovery capsule part1 is immutable material [internal-source-reference]. Save its ENTIRE literal text, including its final newline and without a Markdown fence, as projective_kernel.py. The source has14613 UTF-8 bytes and SHA-256

    74ae7e92d020bfa4ce1e6d1e80fd473d18041463d41b140680c8f618cfd65c26

Part2 is this proof. It is not a runtime code dependency; its immutable receipt supplies its own byte hash. No earlier capsule, worker source, input checkpoint, network package or sandbox file is needed. Every input is literal in part1. Exact dependency environment used: CPython3.13.5 standard library only, assertions enabled, no random generator, no optional parameters.

In a clean directory execute:

    python projective_kernel.py build > kernel_build.txt
    python projective_kernel.py check > kernel_check.txt
    cmp kernel_build.txt kernel_check.txt
    sha256sum projective_kernel.py projective_kernel.json kernel_build.txt kernel_check.txt

The output projective_kernel.json is167390 bytes, SHA-256

    2a684b07f38ad98d5800b365bc15fc66e64cc7df32d705a8add74eadd6e63fb0

The two stdout files are identical432-byte UTF-8 files, each SHA-256

    546fd4396410b69281917f01c4f077a4adde40c07e1c5606b528bc64642e742e

Their complete text is:


[An encoded source block is omitted from this text export pending a complete content review. This passage is not a complete executable package.]

    PROJECTIVE_CENTROID_KERNEL_AND_AXIAL_PHASE_RECOVERY_PASS

The original build/check were executed successfully. A second empty directory received ONLY projective_kernel.py, then completed build/check. The reproduced report and both stdout files were byte-compared to the original outputs successfully. These are completed exact executions, not just predicted terminal markers. Hashes identify the bytes; the complete deterministic source in part1 is what reconstructs them.

## 12. Research consequences and remaining question

The new kernel is complementary to the existing local universal-barrier Newton windows: it can certify strict mechanics by finite affine inequalities before root solving, and its sharp boundary stratification explains when zero-margin certificates are valid. Symmetry can strengthen it but has a precise pyramid failure mode. The actual axial centering curve supplies an exact rational source of genuine weak controls and separates changing body geometry from merely changing an unknown root.

The next meaningful connection is the joint fixed-preimage constraint(4.1), actual shape change and common-metric mechanical feasibility. A full positive projective-orbit search must keep its moving true centroid; the origin-centering kernel alone does not truncate that orbit. The existence of a tree-cotree sign system within a centering kernel is not established for a new small110 body. No minimality claim beyond the independently accepted34..622 interval is made.
