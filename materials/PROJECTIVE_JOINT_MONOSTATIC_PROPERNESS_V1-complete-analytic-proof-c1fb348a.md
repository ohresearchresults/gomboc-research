# material-c1fb348aa34b

AI research material · [Export notes](../catalog/coverage.md#text-records)

<!-- historical-status:start -->
> **Historical AI material.** The title and claims below reflect the AI’s assessment at the time. Claims of proof, certification or completion are not a current verification verdict.
>
> [C622](../C622/README.md) passes the supplied exact checks; C<500 remains open; Minimum’s C≥34 remains a working lower bound requiring a consolidated proof. See [verification status and source gaps](../catalog/coverage.md).
<!-- historical-status:end -->

---

# PROJECTIVE_JOINT_MONOSTATIC_PROPERNESS_V1

## Identity, premises and scope

Coordinator analytic result. No numerical computation, fitted moment model, finite search or unpreserved code is a proof premise. This is a compactness/properness theorem, NOT an exclusion of an entire projective class, an E17 exclusion, or a new attaining construction.

Fix ANY full-dimensional convex 3-polytope P=conv(X_i) with 0 in its interior. Set D={p: l_i(p)=1+p dot X_i>0 for every true vertex i}, and P_p=conv(X_i/l_i(p)). Each P_p is uniformly refilled, and g_p is its own ordinary volume centroid. An arbitrary positive definite metric M is permitted, but stable features always use the reciprocal metric M^{-1} of this SAME centered body. No independent polar mass or polar centroid is used. Let S and U count strict stable maximal facets and strict unstable true vertices, even when other physical weak points exist.

THEOREM. The set
  J(P)={p in D: there exists SPD M for which S(P_p-g_p,M)=U(P_p-g_p,M)=1}
is a compact subset of D (possibly empty). Consequently there is eta(P)>0 such that every p in J(P) satisfies min_i l_i(p)>=eta(P). The corresponding no-additional-weak subset is contained in this same compact set but is not asserted closed.

No numerical value of eta(P) is supplied. The result removes all projective-horizon boundary directions for the joint problem; it does not prove that J(P) is empty. In particular it applies to every projective star, including nonsimple vertices, of the literal bevel body in minimum-0122.

The ONE accepted earlier geometric theorem used to obtain the final contradiction is RAVEN24_ALL_PYRAMIDS_NO_110_V1: every full-dimensional uniformly filled convex pyramid at its own volume centroid has at least two strict stable facets OR at least two strict unstable vertices, including all other weak/degenerate features. Its complete proof and executable algebraic controls are the immutable result minimum-0022, SHA-256 85b0f28d8e4c53b1e4d13566ebcacb6b1bfcd92547d5524599743dde7534de92. That result was read from cursor zero through EOF in this continuation. The present theorem uses its actual strict conclusion, not merely a generic no110 statement. No independent replay of its controls was required or claimed.

The earlier bounded simple-vertex frame and rank-one-only material [internal-source-reference], SHA-256 5d0d746e2df50e044b1206951d3e340885394641752c73679a8884713a32e1f7, motivated this direction. Everything needed for the new proof is established below. Its old U=1-only rank-two boundary is not falsely declared closed: the added S=1 condition is essential.

## 1. A geometric two-half lemma

Let K be a full-dimensional convex polytope containing r times the Euclidean unit ball and contained in R times that ball, with r>0. The reference origin need not be its volume centroid. Let M be SPD with eigenvalues lambda1>=lambda2>=lambda3>0 and unit top eigenvector a.

If lambda1*r^2 >= lambda2*R^2, then U(K,M)>=2, and these unstable vertices are strict.

Proof. On the central cut a dot x=0, q(x)=x^T M x<=lambda2 R^2. Each closed half K_+ and K_- contains respectively r a and -r a, where q=lambda1 r^2. A maximum of q on each half can therefore be chosen strictly off the cut. In the equality case, if the maximum equals the cut bound, the corresponding point +/-r a itself is an off-cut maximizer. Strict convexity implies that any maximizer is an extreme point of the clipped polytope; an off-cut extreme point is a true vertex of K. Let x be one of these maxima. For any y in K distinct from x, some 0<t<=1 has x+t(y-x) in the same half. Maximality gives
  0 >= q(x+t(y-x))-q(x)
    =2t x^T M(y-x)+t^2 (y-x)^T M(y-x).
Thus x^T M(y-x)<0. Both vertices, lying in opposite open halves, are distinct and strictly unstable. This includes repeated top eigenvalues and ties between maxima.

Consequently U=1 implies lambda2/lambda1 > (r/R)^2. Non-strict bounds can of course be used when taking closures.

## 2. The reciprocal second half: JOINT metric compactness

Write K={x:q_f dot x<=1}, with the q_f its actual distinct facet poles, and Q=K^circ=conv(q_f). The strict M-stable foot of facet f is
  z_f=M^{-1}q_f/(q_f^T M^{-1}q_f).
It lies in the relative interior of that true facet exactly when
  q_j^T M^{-1}q_f < q_f^T M^{-1}q_f for all j!=f.
These are precisely the strict unstable-vertex inequalities at q_f for Q under N=M^{-1}. Hence S(K,M)=U(Q,N). This is geometric polarity, not a statement that Q has uniform centroid zero.

From rB subset K subset RB follows (1/R)B subset Q subset (1/r)B. Applying section 1 to N, whose top two eigenvalues are 1/lambda3 and 1/lambda2, shows that S=1 implies lambda3/lambda2 > c, where c=(r/R)^2. Together,
  S=U=1 => lambda2/lambda1>c, lambda3/lambda2>c,
                 lambda3/lambda1>c^2.
After scalar normalization lambda1=1, all such M have closure in the compact SPD set c^2 I <= M <= I. Neither rank-one NOR rank-two metric escape is then possible. This improves the scope of the earlier rank-one-only argument, not the numerical constant of the already accepted isotropic-gauge bounds in the common notebook.

## 3. Exact uniform geometric constants in a maximum-tetrahedron frame

For any full-dimensional convex polytope B, choose a maximum-volume tetrahedron with vertices among its true vertices and use the unique affine map sending its ordered vertices to 0,e1,e2,e3. Denote the normalized polytope again by B. It contains T=conv(0,e1,e2,e3). For any vertex y of B each of its four affine barycentric coordinates relative to T has absolute value at most one: replacing the corresponding tetrahedron vertex multiplies its signed determinant by that barycentric coordinate, and cannot increase the maximal absolute determinant. In particular every ordinary coordinate of y belongs to [-1,1]. Thus diam(B)<=2 sqrt(3), independently of its number of vertices and shape.

Here is a self-contained centroid depth bound. For any unit n let the supporting interval of n dot x on a convex 3-polytope be [m,m+w]. Triangulate it by tetrahedra sharing a vertex attaining the upper support. The mean n-coordinate of each tetrahedron is at least m+w/4. Volume weighting gives n dot g>=m+w/4. Repeating with a lower-support apex gives n dot g<=m+3w/4. Degenerate tetrahedra have zero volume and do not change the argument.

The width of T in every unit direction is at least 1/sqrt(3), since if its four projected coordinates 0,n1,n2,n3 span an interval of length w, then |nj|<=w and 1=sum nj^2<=3w^2. Therefore the own-centroid body K=B-g contains the ball of radius r=1/(4 sqrt(3)). Also for any y in K, use n=y/|y| and the upper support minus centroid depth bound to obtain |y|<=3 diam(B)/4<=3 sqrt(3)/2. Thus one may take R=3 sqrt(3)/2, c=r^2/R^2=1/324.

Every jointly monostatic metric in this frame, normalized by its top eigenvalue, consequently has
  (1/104976) I <= M <= I
in its closure. The constant is deliberately conservative. It is not asserted better than the existing isotropic estimates. The important point is that it holds in a frame whose projective boundary can be analyzed by exact fixed barycentric coordinates.

For the older positive simple-vertex box 0<=y_k<=L_k containing T, the same proof gives c>=1/(27 sum L_k^2). These constants are consequences of true uniform volume centering, not an adjustable center assumption.

## 4. Maximum-tetrahedron compactification of ANY projective horizon

Consider any sequence p_n in D tending to a point p_* of its boundary. Since 0 is interior to P, D is bounded; l_i(p_*)>=0 for all i, with at least one zero and at least one positive. At each n choose a maximum-volume vertex tetrahedron of P_{p_n}, and normalize it as in section 3. There are finitely many choices, so pass to a subsequence with one fixed ordered original vertex set I=(i0,i1,i2,i3). The original four vertices are affinely independent, because a nonsingular projectivity preserves projective independence.

Let alpha_ij be the FIXED original affine barycentric coordinates of X_i relative to the original tetrahedron I. Thus sum_j alpha_ij=1 and X_i=sum_j alpha_ij X_ij. In the normalized image frame the barycentric coordinates are EXACTLY
  beta_ij(n)=alpha_ij*l_ij(p_n)/l_i(p_n).
The identity follows from the two displayed affine relations and l_i=sum_j alpha_ij l_ij. It also proves that these beta sum to one. Maximality of the image tetrahedron gives |beta_ij(n)|<=1 for every i,j.

Partition the four basis indices into Z={j:l_ij(p_*)=0} and A={j:l_ij(p_*)>0}. Both sets are nonempty. If Z were empty, any zero-slack original vertex would have at least one nonzero alpha against a positive limiting numerator, forcing its beta to diverge. If A were empty, the affine function 1+p_* dot x would vanish at four affinely independent points and hence vanish identically, contrary to its value one at x=0.

For an original vertex i with l_i(p_*)=0, boundedness of beta implies alpha_ij=0 for every j in A. Thus all its image limits lie in the affine span of the fixed standard tetrahedron vertices with labels Z. For a vertex i with l_i(p_*)>0, beta_ij(n) tends to zero for j in Z. Its image limits lie in the affine span of the complementary standard vertices A.

Pass to a subsequence on which all normalized vertex coordinates converge; they are in the fixed cube. Let B_Z and B_A be the convex hulls of their respective zero-slack and positive-slack limits. Each contains all standard basis vertices of its block, and its affine hull is exactly that block's affine span. The full limit is therefore the genuine affine JOIN
  B_* = conv(B_Z union B_A),
  dim B_Z=|Z|-1, dim B_A=|A|-1.
The two affine spans are complementary faces of the standard tetrahedron, so the join is full three-dimensional. This is a statement about an actual limiting body, not an unconstrained pair of moment measures.

In dimension three every such nontrivial join is a pyramid. A block of size one is a point apex over a two-dimensional polygon. If the sizes are two and two, both block hulls are nondegenerate intervals, and their join is a tetrahedron, again a pyramid. The zero-slack face of P has dimension |Z|-1, since it contains that many independent basis vertices and is contained in their affine span. Thus a pole face of dimension zero or two gives a pyramid, and a pole edge gives a tetrahedron.

There is no assertion that a chosen naive cube compactification is continuous or that all rates have the same limiting base. Rate-dependent polygons may occur. Every subsequential full-dimensional limit nevertheless has the required join/pyramid structure. Simplicity of a vertex and the seven-star coverage fraction of the bevel are irrelevant to this argument.

## 5. Persistence of STRICT equilibria under coalescing labelled features

Let K_n=conv(v_i,n) have a fixed finite number of labelled true vertices, converging coordinatewise to a full-dimensional K=conv(v_i). Permit limiting vertices to coalesce or become nonextreme. Let M_n converge to an SPD M and suppose the reference origins remain uniformly interior.

If v is a strict unstable TRUE vertex of the limit, collect all labels i with v_i=v. For each n choose in this cluster a label x_n maximizing q_n(x)=x^T M_n x. Against another distinct point y_n of this cluster,
  x_n^T M_n(y_n-x_n)
    =[q_n(y_n)-q_n(x_n)-q_n(y_n-x_n)]/2<0.
Against every label outside the cluster, its limit is a distinct point y of K, and strict instability gives v^T M(y-v)<0; there are finitely many such labels, so all these inequalities remain strict for large n. Hence x_n is a true strict unstable vertex of K_n. Different strict unstable vertices of the limit give disjoint clusters. Therefore U cannot be smaller than the limit's strict U for all sufficiently large n.

For stable facets apply the same argument to the actual poles. Uniform interior and exterior radii bound every pole. Actual polars converge to K^circ: Hausdorff convergence together with a common interior ball gives inclusions (1-epsilon)K subset K_n subset (1+epsilon)K for epsilon tending to zero, and polarity reverses them. The fixed finite lists of actual facet poles have convergent subsequences, their hull limit is K^circ, and M_n^{-1} tends to M^{-1}. Section 2 now transfers the strict-unstable persistence to S. No labelled limiting facet is required to remain a facet; nearby true facets in its pole cluster supply the necessary stable feature.

The centers in our application really converge to the own centroid of B_*: all B_n are in a common bounded cube, contain the same positive-volume tetrahedron, and converge in Hausdorff distance. Their indicators converge almost everywhere away from the measure-zero boundary of B_*, so volume and first moments converge by bounded integration. Centering commutes with this limit. This is exactly where replacing actual refilled centroids by transported centroids would invalidate the application.

## 6. Proof of compactness/properness

Suppose p_n in J(P) approached the boundary of D. Normalize maximum-volume tetrahedra as in section 4. For each n transport its original SPD metric by the SAME affine normalization, center at the actual transformed volume centroid, and scale the metric to largest eigenvalue one. Strict equilibrium counts are unchanged by this simultaneous affine/metric transport. Sections 2 and 3 give a convergent metric subsequence with an SPD limit. Section 4 gives a full-dimensional limiting pyramid, and section 5 gives its actual own centroid.

The accepted all-pyramid theorem, after absorbing the limiting SPD metric into a genuine affine image, supplies two strict U or two strict S of this limit. Section 5 preserves that pair in all sufficiently late approximating bodies. This contradicts S=U=1. Thus no sequence in J(P) approaches the projective horizon.

For closedness inside D, take p_n in J(P) tending to p in D and repeat the fixed-tetrahedron normalization. The limiting map is nonsingular because the original chosen tetrahedron is independent and all its slacks stay positive. The normalized metric subsequence is SPD, and the actual limit is an affine image of P_p at its true centroid. Persistence shows its strict S and U are each at most one. They are each at least one: a farthest vertex always has all strict outgoing products, and the same fact on the actual polar supplies a strict stable facet. Therefore the limit also has S=U=1, so p belongs to J(P).

D is bounded, J(P) is closed in D, and no sequence in it reaches the boundary. It is consequently compact in the ambient Euclidean parameter space. A positive minimum of min_i l_i on this compact set gives eta(P); in the empty case choose any positive value. This proves the theorem.

## 7. Consequences and unresolved tasks

1. The previous seven-simple-star boundary problem for the bevel is subsumed by an all-projective-class JOINT boundary exclusion. No whole bevel orbit has yet been excluded. The three nonsimple-vertex stars are covered by the compactness theorem just as the seven simple stars are.
2. The method does not prove U>=2 throughout the class. It permits genuinely mono-unstable bodies when their stable count is at least two; asking for the unnecessarily stronger U-only conclusion can leave rank-two escapes that the actual joint problem does not have.
3. To obtain an executable finite covering certificate, one still needs a quantified eta and/or explicit pyramid-neighborhood witnesses. The present compactness proof is not a numerical bound, an interval certificate, or a completion of the E17 census. For fixed rational P, the own-centroid rational formulas and strict-feature conditions define a semialgebraic feasibility problem; quantifier elimination can in principle determine a rational cutoff, but no such computation is claimed here.
4. The argument fixes one original P. It does not automatically give a uniform eta over the entire noncompact realization space of a combinatorial type. Across shape degenerations, the original fixed barycentric coefficients and the limiting nonzero/zero slack partition need not remain fixed; that is a separate higher-layer boundary question.
5. The mechanism uses finite labelled vertices/poles and full-dimensional limits. It is not claimed as a no-approximation theorem for smooth monostatic bodies or arbitrary infinite-vertex convex bodies.

## Preservation and verification boundary

This entire UTF-8 document is the exact recovery unit for the analytic result. There is no originating sandbox computation or unstored array to reconstruct. Verification consists of the explicit arguments in sections 1-6 together with the literal accepted all-pyramid parent identified above. The runtime material SHA identifies this complete text. No external priority claim, independent replay of the parent, formal proof-assistant check, new C bound or new construction is asserted.
