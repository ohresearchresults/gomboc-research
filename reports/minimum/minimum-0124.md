# minimum-0124

AI research report · 2026-09-20 UTC · [Export notes](../../catalog/coverage.md#text-records)

<!-- historical-status:start -->
> **Historical AI report.** The title and claims below reflect the AI’s assessment at the time. Claims of proof, certification or completion are not a current verification verdict.
>
> Minimum’s C≥34 remains a working lower bound requiring a consolidated proof. [C622](../../C622/README.md) passes the supplied exact checks. See [verification status and source gaps](../../catalog/coverage.md).
>
> This public text omits encoded source blocks; code in the affected passages is incomplete.
<!-- historical-status:end -->

---

# NO_FREE_FOUR_A_MATCHING_LOW_RANK_AND_FOUR_TYPE_RESIDUAL_V1

## 1. Results and exact remaining boundary

Three substantial parts of the requested endpoint-cover sector are closed.

**Theorem A.** A simplicial, uniformly filled, own-centroid three-polytope whose only physical weak points are four simple A=VE points, and whose eight actual vertices are their eight distinct endpoints, admits arbitrarily small genuine regularizations preserving the complete face lattice and exactly all original feature-labelled strict S/U/H equilibria, with no new strict or weak equilibrium. Thus the entire no-free **n=8 matching sector** is closed.

**Theorem B.** The same conclusion holds throughout the no-free four-A sector whenever the four contact tensors have rank at most two. This includes changes of the obstructing stress under a preliminary affine motion; it is not a fixed-stress-only argument.

**Theorem C.** On six vertices the entire sector whose contact forest has component edge counts 2+2 is closed. So is the sector with counts 3+1 when the three-edge component is an undirected star, regardless of its root. These are five of the seven rooted six-vertex contact-forest types.

An additional structural improvement holds before regularization: **the entire signed FULL vertex-shape stress space has dimension at most one**, even with no free vertex. The previous dimension-three bound is not sharp in this four-contact sector.

Combining these results with the accepted free-vertex theorem leaves only **four rooted endpoint-cover forest types**, all on six or seven vertices, and only in tensor rank three with a unique strictly positive full stress. Additional exact affine and true-moment tests below close every member of these types that fails the stated residual equations. The four-type description is necessary, not an assertion that its strongest residual is physically realizable.

**The complete no-free problem is not proved closed here.** No actual body realizing the remaining full-stress conjunction, and no all-orders obstruction to arbitrary-small shape regularization, is supplied. Two new exact rational no-free bodies and a whole regularization arc are supplied; their tensor stress cone is genuinely two-dimensional, but their FULL shape matrices have rank four. They are meaningful nonrecord controls, not coexistence counterexamples or110 attainers.

## 2. Inputs, authority, and scope

The complete new 2133-line journal was read through EOF, including the entire literal required parent and its executable source. Earlier unchanged inputs remain the already supplied context; no old verification suite was routinely restarted.

Current input: `research-journal(20260920-043445).md`, 336967 UTF-8 bytes, SHA-256 `91ea21e1f9af692ac23c42fdc32dd63cebcd8670e2e0260371c1b5d4ded9d674`.

Literal parent: `minimum-0121`, 53417 bytes, authenticated SHA-256 `5b7a015a3854870aa9d3d3450d95cb8c92e4f9fe85a0a6582486bf3030421fc6`. The authenticated envelope uses compact UTF-8 JSON, keys `version,result_markdown`, `ensure_ascii=False`, separators `(',',':')`, one final LF inside the Markdown string, and no envelope-final LF. No source-identity or scientific conflict was found. The parent closes the nonempty-free sector and explicitly leaves the endpoint-cover problem addressed here.

The inherited geometric inputs used below are actual triangular-star rank at least two, nonsingularity at true degree three or four, and the already accepted free-vertex regularization theorem. In particular the degree-four input is the positive determinant formula for the actual deletion cap, not positivity of a symmetric part or a claim about arbitrary high-degree vertices. These distinctions and the formula are preserved in the supplied journal.

For explicit low-degree recovery, a planar deletion cap of height h and volume v has det A=(v/(4V))³[2+4(H−n·g)/h]>0, with unit n and base plane n·x=H; the bulk lies below that plane and the cap centroid has height h/4 above it. In the nonplanar degree-four chart, T>0 and the true remainder satisfy G_K≥1/4, and

    det A=T(T+1){V_K[2T−1+4G_K]+T²/6}/[24³(V_K+T/6)^4]>0.

These are actual cone/ear moment formulas; affine chart changes conjugate A.

The new proof is analytic. Exact calculations verify its finite graph algebra and new actual controls; finite samples are not the universal proof. No external theorem was added as an unprovided premise, and no peer-review, priority, or proof-assistant certification is claimed.

## 3. One full stress line without a free vertex

Use physical Euclidean coordinates at the actual uniform centroid0. An original common SPD metric is absorbed into a genuine affine image, never into independently centered primal and polar bodies. For contact i put

    x_i→y_i,  u_i=y_i−x_i,  x_i·u_i=0,
    T_i=sym(x_i u_i^T),  W=span(T_i),  U=W^perp.

Here the radial plane at x_i exposes exactly the true edge [x_i,y_i]. Let A_j=D_(v_j)g be the actual volume-centroid derivative. The full shape rows and forces are

    (Rh)_i=(u_i−x_i)·h_(x_i)+x_i·h_(y_i)−u_i·Σ_j A_j h_j,
    c_alpha=Σ_i alpha_i u_i,
    F_j(alpha)=Σ_(source i=j)alpha_i(u_i−x_i)
                          +Σ_(target i=j)alpha_i x_i,
    R^T alpha=0  iff  F_j(alpha)=A_j^T c_alpha for EVERY j.       (1)

Testing all affine vertex fields also gives Σalpha_i T_i=0. These are actual full-shape equations, strictly stronger than tensor stress.

The simple contacts form a rooted forest: there is at most one outgoing edge at a source, and |y_i|²−|x_i|²=|u_i|²>0. A directed cycle is impossible, and an undirected cycle with outdegree at most one would be directed. The force map F is injective on signed coefficients: remove source leaves successively, using their nonzero force factor p=y−2x, with x·p=−|x|². Hence c is injective on ker R^T.

### Lemma 1: a nonsingular contact leaf exists

A *contact leaf* has degree one in the contact forest, not necessarily in the true polytope graph. With four forest edges covering n vertices, its number l satisfies l≥2n−8. If all contact leaves had true degree at least five, simplicial Euler counting would give

    6n−12=Σ true_degree ≥5l+3(n−l)≥7n−16,

contradicting n≥5. Thus a contact leaf w has true degree at most four, so its actual A_w is nonsingular.

At w, F_w(alpha)=alpha_e p, where p=y−2x for a source leaf or p=x for a target leaf, and p≠0. Equation(1) implies

    c_alpha=alpha_e A_w^(-T)p.

Together with injectivity of c, this proves dim ker R^T≤1. Every nonzero signed full stress has a nonzero coefficient on **every** contact-leaf edge having a nonsingular endpoint. In a nonnegative stress those coefficients are positive.

Consequently the entire cone, rather than an arbitrarily selected ray, is controlled. If ker R^T has no nonzero nonnegative vector, strict finite-dimensional separation gives Rh>0. For a mixed-sign generator alpha, an explicit positive vector in alpha^perp is obtained by assigning the sum of the negative magnitudes to its positive entries, the sum of its positive entries to its negative entries, and1 to zero entries; solve Rh equal to that vector.

The count also gives a reusable extension: a no-free k-contact forest has a contact leaf of true degree at most four whenever n>4k−12. This is a stress-dimension observation, not a new general k-contact regularization theorem.

## 4. Three algebraic-geometric lemmas

### 4.1 Actual affine transport

For H∈U and sufficiently small epsilon, M=I+epsilon H is positive definite. A real B with B^T B=M gives an actual uniformly filled body BP with centroid0 and all contact equalities exactly zero. Its centroid derivatives are B A_j B^(-1). In the original chart the exact full stress equations become

    M F_j(beta)=A_j^T M c_beta.                              (2)

The coefficient space L={beta:Σbeta_i T_i=0} remains unchanged under tensor congruence. This handles every new stress, including changed supports. No transported nonuniform volume law is used.

### 4.2 Rank-one projection lemma for a contact forest

For nonzero weights on a forest let K have off-diagonal edge weight alpha_i, source diagonal −2alpha_i, and root diagonal0; thus F(alpha)=KX when X has vertex-coordinate rows. Suppose a scalar vector z satisfies

    Kz=0,  z_source(z_target−z_source)=0 on every edge.       (3)

Then z=0 at every endpoint. Indeed a source leaf gives z_target=2z_source; its contact equation then gives z_source²=0 and both coordinates vanish. Delete the leaf and repeat. This lemma permits signed nonzero weights; isolated vertices are not included in its conclusion.

For positive weights on at most four edges, K has nullity at most one. A path has this property by its nonzero off-diagonal recurrence. A star or the five-vertex fork reduces to a path by eliminating nonroot leaves at the nonzero pivots −2alpha. One- and two-edge components are nonsingular, and there is at most one larger component. This supplies a short complete proof of the small-forest fact used below, consistent with the literal parent.

### 4.3 The common-factor geometry is genuinely constrained

For a nonzero n define W(n)={sym(nq^T):q·n=0}. If W=W(n), each orthogonal contact factorization has exactly one of two forms:

    X type: x=tau n, u∈n^perp nonzero;
    E type: x=q∈n^perp nonzero, u=lambda n.

This follows by restricting sym(xu^T) to n^perp and to the n-axis. A target has both nonzero axial and transverse components, so **no target can be a source**. At most two X sources are possible, one on each ray of the n-axis, because0 is interior and all sources are true vertices. A shared target can belong only to one X and one E contact; then the two tensors are equal, not opposite. Each component therefore has at most two edges.

Each E source q is an exposed vertex of the orthogonal projection to n^perp: its supporting plane exposes precisely its own vertical edge. If two E columns are adjacent vertices of that projected polygon, the corresponding true facet contains their four distinct endpoints and is nonsimplicial. This is a true-facet argument, not an integration-diagonal claim.

## 5. Proof of Theorem B: the entire rank-two sector

Rank one is impossible in the no-free full-dimensional sector: proportional nonzero products (x_i·z)(u_i·z) have the same two factor lines, so every covered endpoint lies in one linear plane. Thus only rank two needs proof.

Suppose there is a nonnegative full stress at the original body; otherwise regularize in first order. Lemma1 makes its signed full-stress space a line generated by alpha≥0. The tensor relation space L has dimension two, and U has dimension four.

Consider the linear matrix space

    C(M):L→R^(3n),  beta↦(M F_j(beta)−A_j^T M c_beta)_j,
    M∈U.                                                     (4)

If some 2×2 minor is not identically zero, injective C(M), hence full shape rank four, occurs arbitrarily close to I with M>0. Polynomial nonvanishing supplies arbitrary-smallness, not a finite-sample inference.

Assume all these minors vanish. A linear space of rank-at-most-one matrices with a two-dimensional domain has either a common kernel line or a common image line. To prove this elementary dichotomy, fix one rank-one map uv^T. Any second map must have either image span(u) or row span(v), since otherwise their sum has rank two. Maps of the two different kinds cannot both occur unless they also share the common factor.

### 5.1 A common kernel is impossible

Its generator is the original alpha. Thus H F_j(alpha)=A_j^T Hc for every H∈U. Let E(H)=Hc and let S be the positive support of alpha.

If S covers all actual vertices, F=K_S X spans at least two dimensions. If it spans three, no nonzero symmetric matrix annihilates it, contradicting dim ker E≥1. If it spans two, every nonzero H∈ker E is a scalar multiple of nn^T for its normal n. Thus nn^T∈U and K_S Xn=0. All contact projection products vanish, so lemma(3) forces Xn=0, contradicting full dimension. Here the full-support K nullity bound applies. If S is proper but still covers every vertex, there are at most three active edges on at least five vertices; all components have at most two edges, so K_S is nonsingular and the span-three argument applies directly.

If S misses an actual vertex w, equation(1) at that vertex and rank A_w≥2 give dim E(U)≤1, hence dim ker E≥3. Every H in this kernel annihilates span F. A span of dimension at least two has a symmetric annihilator of dimension at most one, impossible. If span F is a line n, the kernel must be the entire three-dimensional space of symmetric matrices annihilating n. In particular qq^T∈U for every q⊥n. Apply(3) to K_S X_S q=0: every active endpoint lies on the n-axis, impossible for one nonzero orthogonal contact pair.

### 5.2 A common image is impossible

First c:L→R³ is injective in this case. Otherwise take beta≠0 with c_beta=0. Its nonzero F(beta) spans the common image of(4), so every H∈U acts by one scalar on span_j F_j(beta). If that span has dimension at least two, such symmetric matrices form a space of dimension at most two, contradicting dim U=4. If it is a line n, U is exactly the block-diagonal space preserving n, so W=W(n). But the geometry in§4.3 makes every source a contact leaf and its force factor u−x have a nonzero transverse component. Forces all parallel to n then force beta=0, again a contradiction.

Choose the nonsingular contact-leaf edge e from Lemma1 and nonzero beta∈L with beta_e=0. Its c_beta is nonzero. At that leaf the common-image condition says A_w^T Hc_beta is always proportional to A_w^T c_beta. Nonsingularity gives Hc_beta parallel to c_beta for every H∈U. Therefore W=W(n) with n=c_beta.

The n=5 case is incompatible with components of at most two edges. At n=6 there must be two two-edge components. Their two pairs of equal tensors span rank two, so no nonzero nonnegative tensor relation exists, contradicting alpha≥0.

At n=7 or8 there are at least **two distinct contact-leaf edges** with a true degree-at-most-four endpoint. At n=8, otherwise three disjoint edges have all six endpoints of degree at least five, forcing the other adjacent pair to have degree three. Two adjacent degree-three vertices in a triangulated sphere force that sphere to be the tetrahedron, impossible here.

For n=7 the W(n) forest has six contact leaves and one two-edge root. If its only low-leaf edge belongs to that two-edge component, the degree sum is at least31>30. If it is a matching edge, the only remaining possibility would have degree multiset (3,3,4,5,5,5,5). This is impossible: remove its two nonadjacent degree-three vertices. The remaining five-vertex triangulation is a triangular bipyramid. Each of the two capped faces contains one of its degree-three apices. Re-inserting the vertices either leaves one apex of degree three or makes both apices degree four, whereas the proposed remaining multiset has exactly one4 and no3. The source verifies the entire capped-face overcover; the optional graph-atlas check is not a proof dependency.

For each such low-leaf edge e, the one-dimensional space L∩{beta_e=0} maps under c to the same n-axis; W(n) has a unique common invariant axis. Injectivity of c implies these spaces coincide. Hence one nonzero beta is supported on at most two contacts. It cannot be supported on one. The two tensors are proportional, and c_beta parallel to n forces both contacts to be E type: two X directions are transverse, while one X direction cannot have its transverse part canceled by an E direction. Their two distinct source points must lie on opposite rays of one line p⊂n^perp.

At n=7 there is an X/E shared-target pair with equal tensors. If one supported E edge belongs to it, its other tensor is also along p, forcing the final tensor along p by the positive relation. If neither belongs to it, both remaining edges form that equal-tensor pair; their positive coefficients again force its tensor along p. Both possibilities contradict rank two.

At n=8, if there are three or four E contacts, their exposed projection vertices, with at most one additional X-target projection, necessarily contain two adjacent E columns. The resulting four-vertex maximal facet contradicts simpliciality. Otherwise there are exactly two E and two X contacts. The X sources have opposite axial signs tau_+>0>tau_− and positive alpha coefficients on both edges. Project the tensor balance onto any transverse coordinate perpendicular to p:

    alpha_+ tau_+ u_+^perp + alpha_− tau_− u_−^perp=0.

The two nonzero transverse coordinates have the same sign, or both are zero. All other projected vertices lie on p. Thus0 is on the boundary of the projection, or the projection is one-dimensional, contradicting0∈int P.

Both rank-one-space alternatives are excluded. Some minor of(4) is therefore nonzero, proving Theorem B. This argument tracks the entire future tensor-relation space, not just continuation of alpha.

A finite reconstruction recipe for the affine witness is available: choose a basis H_1,...,H_4 of U and test the 81 coefficient vectors in {0,1,2}^4 on the minors of C(I+Σa_jH_j). A nonzero quadratic polynomial cannot vanish on that grid. For the resulting H, a sufficiently small dyadic epsilon avoids the finitely many roots and preserves M>0 and all strict/excluding guards. The grid points themselves are algebraic test matrices, not claimed physical metrics.

## 6. Actual trace and projective-moment tests; proof of Theorem A

For a positive full-support rank-three stress alpha the tensor relation line is unique. Put c=c_alpha and f_j=F_j(alpha). Define

    L_j(H)=H f_j−A_j^T Hc,  H∈U.                            (5)

Any nonzero value on a basis of U destroys the only possible full stress at every sufficiently small nonzero affine parameter. The new full shape matrix then has rank four. Assume instead that all(5) vanish.

### 6.1 The trace vector is an actual barycenter, not free data

For an outward true triangle F=(i,j,k) set D_F=det(v_i,v_j,v_k)>0. Actual boundary integration gives

    A_j=(1/(24V))Σ_(F contains j)(Σ_(v in F)v+v_j)n_F^T,
    d_j=tr A_j=(1/(6V))Σ_(F contains j)D_F>0,
    Σ_j d_j=3,  Σ_j d_j v_j=0.                              (6)

The positivity uses the true uniformly filled body at its own centroid. It is not a hypothesis about an arbitrary centroid matrix.

For n=8 the positive matching K is invertible and F=KX spans R³. Therefore H↦Hc is an isomorphism U→R³: a kernel element would annihilate every f_j. Write its inverse H(t). The persistent equations say A_j^T t=H(t)f_j, so tr A_j is one linear functional of f_j. Hence d=Fb for some b. Tensor balance gives

    d^T K^(-1)d=b^T F^T K^(-1)Fb=b^T X^T KX b=0.

But one matching edge x→y contributes

    2 d_y(d_x+d_y)/alpha_i>0

to this quadratic form. Summing four edges contradicts(6). Thus(5) cannot all vanish, proving the full-positive rank-three matching case.

Rank four has no tensor stress. A mixed-sign full stress permits a positive first shape direction. A proper-support rank-three nonnegative stress admits an affine motion with tensor derivatives0 on its support and1 elsewhere; this follows from image alpha^perp. The off-support contacts disappear and at most three remain. If a free vertex remains, use the literal parent. If they still cover all at least five vertices, their components have at most two edges, their positive K is invertible, and their unique relation has tensor rank two. The same fixed-stress argument is even simpler: dim U=4 forces a nonzero H with Hc=0, whereas F=KX spans R³ and would force H=0. Thus an affine witness exists there too. Together with Theorem B, all n=8 cases are covered.

### 6.2 Exact tests within the still-open rank-three types

For any full-support no-free rank-three case, persistence of(5) forces H↦Hc to be injective. Indeed F spans at least two dimensions by nullity K≤1. A nonzero kernel matrix would therefore either be impossible or be proportional to nn^T; in the latter case lemma(3) gives Xn=0. Consequently persistence requires

    d∈col(KX),  dim span{A_j}≤3.                             (7)

For nonsingular K, d^T K^(-1)d≠0 is a sufficient witness that persistence fails. These are exact sufficient regularization tests, not independent fitted-moment relaxations.

**Important limit:** in a nonsingular six-vertex positive-tensor-stress configuration, col(KX)=ker X^T by dimension, so d∈col(KX) and d^T K^(-1)d=0 are automatic. The trace test does not close that remaining six-vertex class. A seven-vertex purely algebraic countercontrol in the capsule has positive edge weights, 0<d_j<1, Σd_j=3 and d^T K^(-1)d=0; no realizing body is asserted.

A second test is stronger in a different direction. If U contains nn^T for n≠0, then this H itself has nonzero(5). To prove it, suppose L(nn^T)=0. The full stress would persist on the actual affine line I+epsilon nn^T. Testing actual projective vertex velocities gives, on that line,

    5 Sigma M c=Σ_i alpha_i(x_i^T M x_i)u_i,                 (8)

where Sigma is the actual original uniform covariance. This identity follows directly from the uniformly refilled map x/(1+t p·x), whose Jacobian is (1+t p·x)^(-4) and whose centroid derivative at0 is −5 Sigma p. Differentiate(8) in epsilon and dot with n. Each (n·x_i)(n·u_i)=0, so positivity of n^T Sigma n forces n·c=0. Equation(5) then gives KXn=0. Lemma(3) forces all vertices into n^perp, a contradiction.

Existence of nn^T∈U is a finite exact test: among the16 choices s_i∈{x_i,u_i}, some 3×4 matrix [s_1 s_2 s_3 s_4] must have rank at most two. Thus every surviving residual must have rank three in **all16** factor selections.

When a rank-three full-positive case has a nonzero(5), the parent's original-body quadratic construction also applies: R_H^T alpha cannot belong to im R^T, because testing a hypothetical correcting stress on all affine fields makes it a multiple of alpha. Choose v∈ker R with alpha R_H v>0, use the complete actual quadratic centroid coefficient, and add an order-s² vertex correction. This is not asserted as a uniform quadratic bound for the new rank-two theorem.

## 7. The four-type residual and the six-vertex inertia restrictions

Four contact edges covering five vertices form one rooted tree. Its four sources are not strict U, and the remaining vertex is the only possible strict U; a maximum-norm true vertex guarantees that it is strict. Such an own-centroid body is excluded already by the accepted U=1⇒n≥10 theorem, including weak contacts. This is a vacuous endpoint-cover sector, not a new minimum bound.

For six vertices, positive full-support tensor balance means X^T KX=0 with rank X=3. If K has inertia (p,q,z), a totally isotropic subspace has dimension at most z+min(p,q). A positive two-edge component has inertia(1,2,0); a matching component has(1,1,0). Thus 2+2 components cannot support a full-dimensional positive tensor stress. A three-edge star has(1,3,0) for either root type; adjoining one matching edge is again impossible. Proper-support and lower-rank cases were already handled above. This proves Theorem C.

The remaining rooted arrays, with −1 denoting each component root and every other entry its parent, are exactly

    n6: (-1,0,1,2,-1,4),
    n6: (-1,0,0,1,-1,4),
    n7: (-1,0,0,-1,3,-1,5),
    n7: (-1,0,1,-1,3,-1,5).                               (9)

These are abstract contact-forest types, not polytope incidence-registry entries. The exhaustive counts by vertex number are9,7,2,1 for n=5,6,7,8. The general regularization question is still open only inside(9), with all of the following necessary restrictions: tensor rank three; one strictly positive full stress satisfying every actual vertex equation; identically zero(5) on U; all16 factor selections of rank three; and(7) with actual moments. No body satisfying this conjunction is produced.

The six-vertex residual must also have exactly two original strict U vertices, its two forest roots; the seven-vertex residual has at least two of its three roots strict U, by the same accepted small-vertex bound.

There are further necessary weight inequalities in the six-vertex cases. For the three-edge path rooted at an end, give edges1→0,2→1,3→2 weights a,b,c>0. Its determinant is −a²c(4b−c). If c<4b, eliminating leaves proves inertia(1,3,0), so positive full-dimensional tensor balance is impossible. Therefore the surviving case requires c≥4b. For the internally rooted path 1→0,2→0,3→1, weights a,b,c give determinant −bc[4a²+4ab−bc], and the surviving condition is

    bc≥4a(a+b).

Equality is **not** discarded: the path then has inertia(1,2,1), and adding its matching edge still permits a three-dimensional isotropic subspace. The capsule contains the exact Schur matrices proving the whole positive-weight statements, not sampled eigenvalues.

If a future actual body has identically zero(5), its entire contact-zero affine metric family retains the positive full stress. That is a precise failure of this affine-premotion/first-shape-jet mechanism. It is not an impossibility theorem for nonlinear vertex motions or arbitrary-small full regularization.

## 8. Why the regularizations are physical; new actual controls

After a valid preliminary affine motion, choose the positive actual shape velocity just proved to exist. In a simplicial chamber all vertex coordinates are free local shape parameters. On the resulting raw curve use the **complete** actual moments

    V(s)=Σ det(v_i(s),v_j(s),v_k(s))/6,
    J(s)=Σ det(v_i(s),v_j(s),v_k(s))
                        [v_i(s)+v_j(s)+v_k(s)]/24,
    g(s)=J(s)/V(s).

No adjacent mixed determinant is omitted. Recenter by this g(s), not its first-order approximation. Positive leading A escapes eliminate each whole original simple packet. The finite strict and excluding guards preserve the true lattice, original strict labels and absence of new equilibria. Harmless primitive zeros elsewhere need not be individually removed. The same M and M^(-1) govern the primal and dual throughout. This is the physical convention retained in the literal parent.

### Two rational no-free rank-two controls

For parameters (a,q,p,b) define

    X=[(1,0,0),(1,p,p),(0,1,0),(-q,1,0),
       (0,0,1),(-q,0,1),(-a,0,0),(-a,-b,-b)].              (10)

The two new exact parameter tuples are

    C1=(18/31,14/31,414050/445831,1582847/891662),
    C2=(5/7,12/49,75096/86113,138397/86113).

Both true hulls are simplicial8/18/12, with complete sorted maximal facets

    012,014,027,047,123,135,145,237,356,367,457,567.

Their uniform centroids are exactly0, verified by two different positive apex fans. Their volumes are28403830/13820761 and152278/86113. The four and only physical weak points are simple A on0→1,2→3,4→5,6→7; all68 other true-edge primitives are nonzero. Every vertex is a weak-edge endpoint. True degrees are(4,5,4,5,4,5,3,6).

C1 has strict8/4/10; C2 has strict7/4/9. For C2, stable facet labels are[2,3,4,6,8,9,11], unstable vertices[1,3,5,7], and saddle edges[(0,7),(1,2),(1,3),(1,4),(1,5),(3,6),(3,7),(5,6),(5,7)]. Labels are zero-based in the displayed sorted facet order.

The tensor rows are (p,p),(-q,0),(0,-q),(ab,ab) in the basis sym(e1 e2^T),sym(e1 e3^T). Their entire nonnegative relation cone has extreme rays

    (q,p,p,0),  (0,ab,ab,q).

Their sum is strictly positive. Thus no SPD affine metric can make all four designated A escape values positive. Nevertheless the FULL actual shape matrix has rank four at both bodies. Every vertex equation is independently checked symbolically in arbitrary stress and metric coefficients, and all24 actual centroid partial derivatives at C2 are independently differentiated from the full boundary moments. This is a genuine multiple-tensor-stress control, not a formal point array and not a full-shape-stress obstruction.

### A whole genuine endpoint-motion arc on C2

Let R be its actual4×24 shape matrix. Define E∈R^(24×3) by E_(0,0)=1, E_(1,1)=E_(2,1)=1, E_(3,2)=1 and every other entry0. Set

    h=E [ (R E)_(rows 0,1,3) ]^(-1)(1,1,1)^T.

Thus only raw vertex0 moves by(r,s,s), and raw vertex1 by(u,0,0); all other raw endpoints remain fixed. The exact source reconstructs every coefficient. It proves Rh=(1,1,1,1)^T and

    g'(0)=(49/12,86113/276794,86113/276794),

which is deliberately nonzero. Actual recentering is essential: it is what opens the other three raw contact equalities. The complete nonzero second centroid coefficient and all mixed volume/first-moment terms are retained in the report and reconstructed by the capsule.

On the ENTIRE interval0<s≤1/65536, the actual recentered arc retains strict7/4/9 and has weak000. Its145 exact polynomial guards comprise60 nonincident supports,12 centroid-plane guards,1 volume guard,68 old primitive signs and4 positive weak quotients. All517 Bernstein coefficients are strictly positive, maximum polynomial degree8. The endpoint is independently re-hulled, integrated from two different positive apex fans, and fully mechanically audited. This is not endpoint sampling.

The simplest noncentral radial prescription is a meaningful failure here: h_j=|v_j|²v_j, followed by its true own-centroid recentering, has first escape signs(+,-,-,-). The exact derivative and all four coefficients are preserved. This defeats that prescription, not the complete regularization theorem.

### Wrong-chamber rational root and the earlier quintic locator

In the displayed simplicial facet chamber, direct integration gives

    6V=2ab+a+2bq+2b+4pq+2p+1,
    24Jx=−[4a²b+a²+4abq+2ab+2aq+2bq²−2b
                         +6pq²−4pq−4p+2q−1],
    24Jy=24Jz=−2ab²+ab+a−2b²q−2b²+2bq+b
                         +4p²q+2p²+4pq+2p+1.

A rational search first returned(5/11,4/11,4328/19501,22712/19501). Its actual hull instead has the true quadrilateral2345 and counts8/17/11. Reintegrating that true hull gives

    V=735860/643533,
    g=(10845/1618892,145667871/5740002344,
                       145667871/5740002344),

with strict6/5/9 and weak000. It is not an own-centroid four-A example. The complete actual lattice, moments and mechanics are retained, rather than silently applying the old chamber formula.

An earlier algebraic locator used p=3/4,q=1/2,

    b=(27−8a²−8a)/(32a²+32a−12),
    640a^5+6976a^4+13088a³+5168a²−3222a−1935=0,
    510/1000<a<511/1000.

The unique root in that interval and its conditional moment elimination are reconstructed, but **no exact root-body hull or full mechanical audit is claimed for this locator**. The rational C1/C2 controls require none of it.

A useful purely algebraic negative control has contact parents(-1,0,0,-1,3,-1,5), positive edge weights(1/16,1,272/33,272/33), and d=(3/7,...,3/7). Its K is invertible and d^T K^(-1)d=0 despite0<d_j<1 andΣd_j=3. There is no supplied X or actual body realizing these data. It prevents promoting the matching trace positivity to every forest.

## 9. Reproducible capsule and most useful continuation

Save the complete capsule below as `recover_endpoint_cover.py`, UTF-8/LF with one final LF. It contains the entire exact source, not a link or an unavailable parent import. The decoded plain source includes every hull, moment, shape, mechanical and Bernstein helper; all rational inputs; the full forest enumeration and Schur certificates; and the optional deterministic discovery searches.

Executed main environment: CPython3.13.5, SymPy1.14.0, installed mpmath1.3.0, assertions and PYTHONHASHSEED=0. Optional `atlas` uses NetworkX3.6.1; the theorem and main build do not. There is no RNG or numerical acceptance tolerance.

    export PYTHONHASHSEED=0
    python recover_endpoint_cover.py build > build.txt
    python recover_endpoint_cover.py check > check.txt
    cmp build.txt check.txt

Both the plain-source build/check and a fresh **capsule-only** cold build/check completed with byte parity. No previous suite was rerun. Exact pins:

    recover_endpoint_cover.py 10697 bytes
    SHA256 0c39ef7a7688f20922a185c26e599148dc14015db7d945eb4e8ec3a5c3e0a71a
    endpoint_cover_four_a.py 18813 bytes
    SHA256 24ae5f48c6ca19c07fad1c101306f55fad3c0d47dcdd8dc168963a5608b74a0d
    endpoint_cover_four_a.json 150447 bytes
    SHA256 ea4908a282bf818cf70632051814370c9806deb5054496b819a7484a8e60de6f
    build.txt / check.txt 402 bytes
    SHA256 82c68fdf25dbea75eb3946df6474e6d3b0dc4dab8310008204adf3e816be3ae6

Exact main stdout:


[Encoded source block omitted; the code in this passage is incomplete.]

    endpoint_cover_four_a.json 150447 ea4908a282bf818cf70632051814370c9806deb5054496b819a7484a8e60de6f
    ENDPOINT_COVER_FOUR_A_RECOVERY_PASS

The independent cold receipt ended `ENDPOINT_COVER_COMPLETE_CAPSULE_COLD_PASS`. Optional commands `locate20`, `locate50` and `atlas` reproduce the exact finite discovery units. The two rational searches use reduced fractions with denominator at most20 or50, respectively, giving127 or773 candidates per scalar grid, with0<q<a<1 and b>0; the latter additionally requires p>1/2 and returns exactly C1,C2. Their absence of additional hits is not an exclusion or completeness theorem over shapes.

Convenience copies: plain source (`endpoint_cover_four_a.py`), exact report (`endpoint_cover_four_a.json`), capsule (`recover_endpoint_cover.py`).

The useful continuation is now the four explicit forests(9), not the closed free-clique or no-free matching sector. It should retain the one-dimensional signed stress space, the full actual residual(5), the rank-one factor test, the actual trace's six-vertex limitation, and complete mixed moment jets. The nonsimplicial, mixed A/B and VF complements are unchanged. The global bracket34≤C_min≤622 and every polytope-incidence registry count remain unchanged; none of the new graph counts or nonrecord controls is a minimum claim.

```python
"""Recover the complete ENDPOINT_COVER_FOUR_A_REGULARIZATION_V1 source.
Python3.13.5, SymPy1.14.0; optional atlas uses NetworkX3.6.1.
Run: python recover_endpoint_cover.py build|check|locate20|locate50|atlas
Parent minimum-0121,
SHA256 5b7a015a3854870aa9d3d3450d95cb8c92e4f9fe85a0a6582486bf3030421fc6.
"""
import base64,hashlib,pathlib,subprocess,sys,zlib
assert __debug__
DATA=r"""
c-
oCTX?NPlvfuqHG;=>lf(A=$#v(oEki;1~i|xV0;|xznM@RyMLC6wd<J|oBSJjIaAenn_#*%ueuCA`GwVU66|NY|n{q4=w_0V~DbA
K^#KHPjAIDKbu@#oji{lV2g{o&QkwR3OQPu|_`*0WXAteeexn<#g?<?YU_o2|OhQ`|HSl6AO>QlbPeuD4ba7eCzv6htd!aQ)|L6s
(_D$z%N_W^j}s^5az)tsQT*4H9Rv+9Zx!k9W#=6E6J!db7ZL{O@Arx$B@|h?lnUUw6H5)03N+gICz6;)f}NvQsu`kSf=FsE1~~Q#
b3%7dMQQBoHn96|{&}>-tIGTW<h_w~E%uYLO~4cN-{(htgLVY8?4V5(LT?=jR1bGW`1nYSVBXLhE%9rK{v5T_-
`B!lZZ5V7yr?AHIJ6tfVtH4xli4Y+1_n%}{X{i`pvjgCtc}W9YN-
a280hWxNQ|`pNIV|9&z_R!b#z*Rw@9R>EbxO4iCPeDaEL4T!7|TT$h$mg6vT1@Yr#<pWewDt4a3^~_0vc;R}%GKkh3)Fg4)_!+1V
qJUQ~Va(znBut-
@^@%8%xhWz@=IJUT=`NM!>23*22uqTlaHdck#}CGvspBYa<SS|2ae$U74C6SIs+@z=lfP(M9|)f5{R1DbL9$A<CNcHi6?_J}Kx^u
~HM|1njaLgzU90-ZZGUiaJ*29ePMsTXwoP5v8NA*-c*C;~f89U5?_9h)S4Au5?y^tS_V~;-%(mO?wp-mZ!*$R7rr&I}4gb9Djl14
?BWO*|CqcLE8g8fEZM3?b@uX=qjaI{)cpdfR;`WaIrJ1DDZZ|vn$<_7k*Wn!<X;9WBO;acE(h@H%vt_gm(rUH4q6Q##TW6$uZgx5
iT_-
1s_#gCdlQY()L0aeda@ID^JEYq&%_b{vcAMvC;(NcR$;Xq=W}{2Y^R~gh8jUl6$v<`b<lW8nu>X$XYyf?U)*t{M`nKV32XL@YKJ?
#Rh<eh1Qhc`9vw=9mv&EiJ%lew6iM=IC@Xet?Eo%q0q{E&a_6@b{*(Q9vxBa^-
7|%YLtP&+8a|L!Rj&3m697ll%$AXWo+ZG%0GG`dQcR2z8HoY9pNoZ5E$6(jpI0lKMUFs)(Fi}!qSM5c&l3=|_BIO0E7rV(O^0c(>
xsewvbS0c9VH!s18o#v{lGeYt>m+=6>!yLO1dB9KWMhEE;QGN@bIF)^8ECieuh!bQ?g4hG=IOj$00Y7B4EbLUBf*SD*k!9LNT4l}
Cs{q)><eD-
`=!2KEy8rI0XdI@1%P3W7|0*Q`dCvx^wwFs@7VBBw+iDwk}V$*q|q|f^dCo|XzL9~HG(+l`8@Wg@xrl{3vt58Gutc{+Jm4E2*nGg
Q<m;axCDV6uNJ#0$ju3eGnCOFNCRcO+C;t!@;&gUD5gPt2UD(vph4(HQ<ShMU>UAa8u|fEH%sk-
{G*>Pf(XXzaftLgpOD~1@`!jA1*!%zeHv)IlMWle%JyPJwTIE%u04!GTNjJ|FnSaPSu>zjMCm^k>Ygy#1X;xvR3;rojA>qYCx*uh
;_zS>0W8Bv!{+)M;|-98zaK)JP__=5%iy?t>4Ipp41hWT?}gyDlo}-
jC)kiv<Pa)OfFa2#$ua%Iup(NEvPOQgifI(QtmWX0ZyD{HY|Lon+P}fDJwIH+w13jd{f#1|eDX1@5vbjD;A=o!*B)W_kzv~;|1#m
r)pLN8d~V2L$ZdN&RT~3{nhSsQisk_TcsFgm2IcY{%VnDk++qcStG9_!d}Tz3VPhN?P|cYG|Mxr#7lDGTvsmeW&<4|r44cJjRBPA
-AEr%W{S7s&#i|~!VofiBfI=b7V*PN$BtZQNq=BLJpN+kV%VTe1Ha0%8u{ZINv7zvAY;Q+L@u*?vNWdg4fK&y5_{<3-
i~_{L+v$|z%cR71u%g}$m#@ZNU{&*d1mBHP1#(~n8^H2*busY*!mkvH!^jU_G~6sOpxol4i4Aq5SIe%#!+PZiPBOOQt@NI^^FVCS
QPzu1k?)Mu?lD;d;-Uu<MlL@#m=kYT-ew$7VLkX}9Am53Fot@9vljROt62<oJq^~tuI^^B=HgV7d=GtfkUb+Hf>@AwK5;;&4%-
e(HAX4~{>cAUO(9Yq^L=I#u^=@t5Ki{i=|QjIgW;oB*@C68a-4g>q-An&%Stk-
&XEV%vI#&xlt99aG?crXA~*r)iiIVisu#7wBqgFXOpIwKNd`WSP(#p(X^*9g%);7&0scb&At@ODkxz%9D8v%nqamq*<oQVdse7w<
r|G>x(TaEu!s!g;Okq{ovIEq75n<2c2zGUZ@{cPF#v69er)UerOmsjKg8M_hHTj#~du19Z1`U*f6ywT8Wrm6me0yJ|{%NQ85gwJ-
(?+YfW%%^00oG}+mDl>Pig2}UWm_NSixTT3pP;Uvnhm2!Wj543w87^`@f_$xV8m%VcfHjZw5cTUJ(&uM_KT!?&Us5LXil`Z1u~bm
L#As>G!}DY5H;3hPpbX9+U>oqVtr^=u~8K(;Lo#NYgMLtC8`fIc>NOH-
=1oXR^?vbV_+a{zeq_+uZnc+3oZ=2nHz;3Qc7?yH%%nLzR}T3ZCcdsJ+N$o63cNh!n^0QW>i4=Wi{>Izf65bxt_+a+Em{c#IrvPK
5A*=(dkUgIo{II$Sx!Klod^K?Cc)cp@=)|9QP5Qj6T%J=E6i4(I#Z3=ORLEU8`&WF*|nY#ta)W`UYB^P2$^VY}fEhC-
^GLTr3;g1&^rsKQ=p%+^jMGnAtU1suNjMsGrFCnXTJ;PP24MM_^Zii;#v>lz9a^7V#EyuF`Z0GGzlT3l>$p#aT!yPtk<vLD{%iW@
6bBBAb^rc-gF2)-0GGNOoB@LW>3nOc*vLwTc#EIt5-eEL@;ck92C6<n4ErO<%RxgQz%!YT;j^-
l^7TE|gqc)^YKZE=K|j0+dc^J=Cwi=(+u6&r9gZxJPPDK1bmNrOZYIJ@oR%$QgC3??b_9JF)9Mf+klP5r~TG<-
|$2WZ@hrW()X(?_d_cahA*(gH7BgU+9(K)Ld17r(Y2wuHZCqY)f;LUUz}lUnttEy$w8ouU|^SaDFI32jJK?D{~9}t2S*~+ti1ZFO
@!Q{;Vf&;zAP_nt;^X)LwLK*5fr}s2Q`G7c4C<`hZUw#`Xe~S?(g9xdPb_bR@N8NfdaQ^4#0y&(f}uvo3)<GWVWWrO%a3?*kO#8$
%qv#_a2*i0B96aa3hY4u*UpF$`-Jo8>Y@_|s$rc8&}w#9-
v|um*nDp7_h50Kpgpi#b3O@!|>~@KPJYKPDm=Lhi;7L58@AyOgG$K#lUk-UH2$u84L$X5BDl%FRjP{Bkped?W+nr?g<xJTTF*1s#
wO-!Ip6?2@Xwr*zBAw2zd|*~@^^Bs1Jz{-
A{&<EK^M=iR6D<LP~Gxuj(!mMJjSXth~WkQ6wJU=5Zxhzm9&qRKfsiTkWt4@BkWvueRqRjw{nu-
J*3Ip(T`_~+zT*+{VMM*$H=H@qCE4I9Q<EntVK);)|8Ch6K)t}w)@S|4Gk03*AhuUgY0Y;U!7abOR+aU<vSzBa8)>qDKWGPLVVz{
mjv{1k``<7AXjt>rQcc*KAF#o|!bzFq}ag0dhQBX({-
Q)+hQiu|+RX}KJgrIbxU)uOx`8Kh?Nf3{up9pwJ9kHOlPZUC;u2FJ>;3_1(kk+XyD(n{CZHVXK*4~iq|2c~;hFWYmjLB>Y0OWAG{
BOxP#C@^ecrZCF|K6N3@3vNo6X^BUS-ZN{E4Nw@gPY=!0f55Ic=)Ne=`wXd+587xX5E)i3EATotBq};=Ifl$7j>`gy_VFne6|=ho
dnkvFf*>XUjpStpaVul?-;=E$EW)sk$pbBOwgyI4&?-
?HhT>G(rB>E=Sb=YvDXI=gFA0TJ{gzcVT2PmVM+y{4>+1yeuGXJ(4(Kzr)Cc(kQkZ7CBCW5Y0Cl0MA6S^UzOR4qwR~lAhNFSp<-
<&xA}_#)tk2RlFuzuL&?|m%i-
3m{WC(YQ_#Su7a$kx$Vim?&IYUjr|Is>N+m|}z)fn*#&`+Qo$o{MtI@HgL7dh3yJY*?~R8!rBVYO6!k6i8|ANG>DfZD9`g^fNVU!
>|RfSDOqN7V^qJiX+_<=hsep}#4hQQrzmYL}G{xU2f`hq1PIxUUYEjS0pB3+NJ!33pMGqv`Y~Oq94jxHmkEsaIY~R>RcfbMDV8Gr
?74CTHCz&=uxbaEU?D)Hkt@MpU-
HX`e98bjEJ7LpdKLj&#|5!qajN^GJsBizn$Ewk=tv?wGqU0p;ryr%eY2VidXyN2(KtDH=L8WkryB*nt-hjLN|huqm<OFl%t2ELfT
Z6DB;a#P!2(1?C3|jMNk?tpJ3!`ggL5rZrGU%W;ronN~1`S8Gdgc~bLf<N8Us0GcK6#q@7a@mEZAvRsF<TA&hQ`*OKixOKH?Ji&n
6q=6A4u*o^fx3Ji^tHlmjGkA$z76c?~9b8bf+zoPD_k(E?1Tx|?2Jr_AeOr&#Gi|O{E^hBCm3iea4TI_0Bbn=jy+!b*?_0f(RZ~9
*R7Fr|pZrR?fbn@-cT)!tOtg|$GZsc#;%S%+PJA(|2g*N3WxK^@K|NWOTPk4n?y_QG%-CSWWo5$H;b@8oA&=b!x-
}`<GO`CZcI+R$K@Mb}4`GacR-0`DG0J~19S>Gm5_(x)U0JS>F)U?fP%R-
TNp+&kOmGRf{i*~k9ll!6fQe?*s53|x#r@pWdl#Uh49uckfT>{G^kUS&2Yxq6171#epj8`GE_94JVh$Pg8W<KfVNY;i>tVFj^omd
uEU7!A7nRrIN)9SB6egJ>VRhSJK}WMu=JgPvhv!A%W%n?YQe9WJT+DFK5QWJD0RVzw(3EzF!|mm7%sLQZ!4Kdp2YM!!Tmi?;;q)1
tOejeaSx}Q=Kg@OThl0sOTcftkF#Txjrx}xRgB6UgDJR~vLAkK~CAh}FfU9Ml?u$57rshFYVdHPy1RRS|R!-
Pnzt?TM7lBM*i7305E<l2n!=MB?T#|-)FZzCL3R_@g>KjI;z7--<-%t~=0y&6`L`1p3|4j4AR3Z`Ofi5-
v{t@&kM@#noocHC^%EB9&58&`bl}aXjo}YEQY(kXu;X(K@Gdd^M{s`$N#-
k4i`H{oUQLf>9bvaZXy_m8HO;HBq{)Ii_0T(+*BA{91s~2rBRR)A%fv=A|2NHlkiY4Q$q!#SCvx3|*5+*;VHtb7AObmPdq|qdAG_
{X|o&KUn?I(>&W0#X>k3`#oi(U?)Aip8q2+}}5TqI0k9>#{nZheGGrdhMtjI`Mgdc-u#>&K^{-
vk8YfD}|*v|57VtIyn2Tk8j%_t}FvbWa-
)#^{z3bmwd$)T&+X&WwZo{+a*A`y%t$lF_n2WF><Io#<#=Pd8)0j)2B3#3;Xko|+KPBkMH@0v>39_CnNd$$U<dB#Smc4Qm+rJmAn
E^9D&8S<InOzZZ6xOehs*jOS76?bs`fNSUT%Ut3tLEq80?b4us@HAyH<8v6>~mvIU|k5gno?n`r(@IDqx8N5<7191mB1Od$Xbh|B
Kf7A=NGr#$WQ=P}S9|PuyY3iLyz{4i$rK(#wT&RZT$F@Ay>?hthCt%2+)h>r;@o+-
|J3+NT!@>+P4iYR@Ubx<=7QD$=2scbq)dJ;8RBjqNdBj9ApRD<50EO467MQ$w8P}dr*dQuLRTa#e1D3{!YJJbFE7d~k7lJcv3Gzq
|zW;Ag7!jwPCT={FUP|mH0iN6w&VUdSpE9!s2`k!w8krZ?E<A`zi)L0ajviyOdH*!Tv+xpAP<Op~70jbgqYzIY)f$y&_8!~x(<sK
G=i)NYc?Mh}+Y>ANNtmjOX)sP)nI8F%auxXjiUmMRNkN1z@W9_{QcGjh$P#m~`q;rmMi+TPQuOn7+|FC?VwP#@u{=el-*HrL<p-
I`FAFDHm>rZTC88(V{J?bQ>Eu{v;hGp|LTOlXRe4rdW=F7hl=p6sPGRsQn9B1wvhCUp7c8I24?BW~%R3%JB+~cwL`=1sN%Sg00eV
l1DRwb+Qaszh=p)53&I|eg=P&|R<#_>wb2Qs6$curt2Do_VnHd$NjOxAd&WY&v$TIfH&?e`4eh$eiPO80kjv(~Y{Ub^TXFdz*b%r
`vv)-
WwMFTi%!b~nR&uYUk`fs##$o~11=t%Y~b;B$rg2r$>fG4~$P!VT8ifr65f+mvEqDhgKj8yb{+d3y5>x`UP4brvDA0o~^CLS$DUX-
!osYD7Ap8L<@)&+Am=4TCSEH}Ud`}oRF9g5e6e8m(%!7lqm%d&@SXb-
d{#w?@?kI5&J*1;rRuM+K39m7$XNhqd<4t~Rif0WkTid*q2TB|ayc?XS}qS2T)fwoorJH`S%+rp_g+rUsHjC_>1g>`-
mf|!oNe04Zme5#|#$&WlrOILKZ_xCMxRz79E9zrDeN3ZP_%F!!%xhTr2gkyNvfB}^5yU!0wr{yCyi@*i_D^H5D4c4?-
a%Uvo8f3(tO;J)>Ii%*?9+`IUEtT}*AdiMHxj+{&X-
2vI#yOtZ%8M}!TR<jn%gdg3fi`Smi@|8OI<9*9X~X_$ClfnyhT@F#lXi@?fCe~%=GB0;0PIiNHV+UPpEihVBX5H`bE{sC(SMYFv{
Tm47*~p1f9|4ES9lPp3C~3!4w!?|nBm#_WE}dSg_N@zS_8q0Xe)rl?i%bGL0QFB+OpL+jCYB<4E?$?oCPV=B>}FA;vuE|8god!*$
P>Q>$kC+1`Y=fY|~`%HTb{aA83v~)Qo_)%9RF-KeFS+O5q4{>Ch*S(&>2Wm_cE&y|QCG{dY0U#x7-yB$h>#i&@o7$}{(~I<-
U_JkKKHFGVmyBZ<!{&fPxXXi@u{Bu$(DKi}(Yav2|^!z#LDEB^t!2ZhC872jREuoNH~VAknm#}*q*&xH#bEr9u^crX{O#gLuHg@3
MceRKWx=KVLmTwE!me63+ds)jnQ_e@8aT{Am6h~U4p#u+RCI|wh{?31H1_*w7y^e+t$p38{SnT#hDHnj0(`^L<DqoY{~&94tZIB_
B6V-
`pn`~Oj3dw8=jnhF}QTO|Dcgc7EBx;pgMi(P(IggO6cvB?5o+Nhia8?q(OMGdwA#GdyxSnt!aJYPmPos6DA>G;dSwgq_hUbsrAAk
AOmw3c#SOPm-cnJSx#wyAFQ)913gfsy6FcbIBdE%qQPJ{)e|s1|>M+kv-
u(8+UzI#(_60tP>8<A4^=Jpokdxwo*M0f+JKu!&+=ItCo1C{d$e>N1Z2gu}#P0^7-
@mTKkih=q_d;G=BeFK1mxh!+QhhJ$y3*o7d~VysS7-joX*hcmCkQw)Mr(T5Q(fojD>{iIr-hzkA-
I5VFdpe3F@b>KT=m>>DnmV#RZ$Pi6<=B@q9s^k!oVCjYtf+#P?C^J%U+q4Rn%HDUrvogCTFS3O%#qU{Zk&sX9G?tJk-
{t)vEhN64`{UAT$JqS7U137YA9@d*xM!eFQCPb2&{Wx!eL5_b$IZbiG2T4Aao?E7EztKgw}+mpsHqy2r^-
{Uu@C7zhKY`XNN7##uud)fPd|O%^PtFOusGDGnhC|FUVU`)KwCcn0V+u)0SusJsmWUk5c4KpRb$w(uOrRh6(M@1=3dpUnx)1*eOq
}8;QN(#`!nrh%nR4)%}*vAMHtRuH@iUA3IB1G=tLH=XcuZTC_Gq^s1ilL(Lz5qmS6FGEG=~Xsms8vZxCW{s~LAOoG?AxsPvIl-
`0*-9XSR%rb#8PdI#lrtlSWnE*b{Ex|0D#^Im@wgEByoKmNn81iMQ0$NgP)lxUrh?6i?gng%a%;K2p~gF<benx;zBmUuK9-
BWh$3O?8+Eb*n=d&rFP%Ur72J#AtKv&EnM4%sQcLx$!23fU>YLZ$+VVAwOPXq>jr;mNLzow93USjujViO;>{nb?+8PJ!#<1kX6C1
9tVZ|JiwW+5htPV&HtfdDkD_3{(;^_nuuGAp(Rv0EMvz8LkjF0>!=07rYc0y%dL!UiK~nviq89ez@pIIXuAbrsa!11$n}c&oZ+Mp
mD{>kZ`6N^JZ8a4Rl+?7I%uQIt~(NHDPKdMZ39KiE15I4ItRHQwPko$W1^#LtngTP)fu`wv>paKnOdQKFu?rc|1VRk({On$LkSf$
Ii}p$f7eWYI7^3WTWZQKjW>6OLlWBmh4Oa;pz)KZ$J01`vd0=-
ak8k4*Iv3&iku7cGLHpN&tXZH+JP#uA94<(k$}S<H1V2oWl>d>G`(hHy`b?AHiCqH&aM-fyLHs8Ni32bDG_Tan=z>QDk#-uesTV-
O?2|9e)PDlrgzuQCg8lCmqry=fpIR;%5G;@6nzk5odqZ^E`7A+L2=bs?ASVWv8};)%f>pwLn*e=k7)Bo!`R&n;F&-
b>Ie8GxWGF#v_%{O5Uml&0ia@d@!aLZn)Izr89=5=*JVR(OA`sCl00HI!uQ?km7U-
x$bg`v?T8CsfIdnTt(G1X1Z|<sw`%2F{rB34r_mHaJ`HzWwe6pXDE?cb<8z2lyndRQ@}C*%XKaXWujih{s;^H!yed|KLs8f3xNmp
FW_{tf57FwmQ6>O`5}J)p_W_HwQGZ1oAA#DueqhmQ%U17P~fcA#mV7cP)p4Qvq11sGaDJb5}H|gAA!O=HSs;R&`ALU?aAVY2!H6j
W=zIop<4ti&`!$$$dz`rbAHyrw^r3`8eJT_(yX@44#%R|Xt1Hro9(jY55}VgI7pR;IH6!80zPqd>DY)aqJksjg3r}9Ve=Y>q2qPK
BekZe73Tr+Yuc~sf$Qao0~;);nH?$d!^uR;5t6`PtHr^|t6m2X4$E+7!PatQTpWRsH$rPXp`jrB0L}N1-wIt#lnWGuiVQNqetWD-
dAfw2G~X4+Znkvy!my9Ui;HFB<Qo+r_YaxKyGP%^fus1Rx~^P}Eb?fV`t#&m;rK!Z?$?_&4-
O>ZmibTg$T5SLgHsFasMdTA44>mI<nysJoCWatL<@&hU|#v0JeTHYa8h>XA@Zn<JWufkVnJhi?nq{r%I+*4Im$bTIQ3x{O1mYS!v
n2qp6#X6GH*=%AAb%5>?-aGg8#*TU4Z02GLUD;#hEQj?StbVt!nJ2B%-c7fSncb6Kd?IBHqwOPnlqRAnGXG(-
X0Ep0lYd18CI*vEl{tM=+w!X>`V`749Y~Fl<y;-pQY~z<3#&4S1}G-)pFe->iUze+g4SzzgbXAtT5Q0M&w*EORJ-DFeN2ws@Gu18
$y#;EuwYs+Q*#a(9@b2FPK=!vv}odHDcB1&VBAiq7>tJH`D`wLbnJst^Q@P=eru51osL{=1=bd-
?6|>K#}&{jcw@hRiEhr6^UOR3S_OX$LQgqYr|KQYl!}v1*OSL=Dr`0yq}j=|VEKAZdz1&6b%)ByDCU3E8>>KOvcJ@$M!wQb#JYre
HgcRAx=GH~B**g^xD>VCJgiZExw*9Ab8nAByYg+D+Ce#uGIGK-DebuA}t_ZAKl-
)@2g0&=*W=K8hs_^kS3Mcus}=*TX;_)$lhx>i%XKW1ig8pn*=%$aNlrUCP2xAZhTdKdehiHP{OTSX|eu>i<QmUWY!IMmsQc5jZBZ
+eWK(#<qa?5s^ADWTV~T4eGPt#Sg(WXEALxa9ig_*KKqg<4M=-
dXqDw(`*=Rvun1RXNGs)H9CGUZX4}Z>%24Wn&<9WtJ`wBLC5fe&V+jt_;V^0e?&!7kN@lpPFdB<B;(6yVc+^QI0L}YyET|m49)y7
r<fsYmISUZS^@IduxOq$VRG^Q&kGPMgNwW2opbJ-ISt2j`q%HBtLuxw@T!k>UqIO0Ik)}0JAsn`F#P+*fgSJ_c)#nI@UH>e!uc?`
xR8QscyWDqGjIm|>rV{_e}o3*(d`8*XdQw0_u%IG&&<QiT)x2#?6$$hB?3U)hJ&vcAQ8VDgK&BC`NA=r&qHVEz?<o?-
$ik523LPxA*{RM;0ku_nbU&l{(aH^1Uu>ooIk(z2k-Ax=2`;BjrJsqT@dL+y}h}+8eZLBIDqx_-
SFb-8oU|o^i$bm7YAc&6}iiRWPC~fjTcME{!B}7&q~e?ILUEv80OqM4oVNlQ7tY-PW~SvhZ?W
"""
b=zlib.decompress(base64.b85decode(''.join(DATA.split())))
assert len(b)==18813
assert hashlib.sha256(b).hexdigest()=='24ae5f48c6ca19c07fad1c101306f55fad3c0d47dcdd8dc168963a5608b74a0d'
p=pathlib.Path('endpoint_cover_four_a.py')
p.write_bytes(b)
assert sys.argv[1:] in (['build'],['check'],['locate20'],['locate50'],['atlas'])
subprocess.run([sys.executable,str(p),*sys.argv[1:]],check=True)

```
