# material-c9db1bd5bf62

Historical AI scientific source/proof material. Statements retain their original scope; this is not an independently reviewed theorem.

Public derivative: internal-record-identifiers-replaced.

---

# Exact edgewise representation of the whole-facet stable-root cone

## Statement
Let P be a full-dimensional convex three-polytope with a specified interior origin. For the minimum problem this origin is always the actual uniform volume centroid. Let F be one TRUE maximal facet with cyclic, distinct vertices p_0,...,p_(m-1), and actual pole q normalized by q.p_i=1. The physical metric is M>0 and its polar metric is exactly M^-1. Define

R_F={M>0: M^-1 q/(q^T M^-1 q) belongs to relint F},
D_F={A symmetric: tr(A M)<=0 for every M in R_F}.

Put B_i=sym(p_i p_(i+1)^T), with cyclic indices and sym(uv^T)=(uv^T+vu^T)/2. Then the following is an EXACT finite description, not a sufficient sampling test:

A belongs to D_F if and only if
q^T A q<=0,
and for EVERY true boundary edge i there exists a scalar lambda_i>=0 such that
lambda_i B_i-A is positive semidefinite.

Thus a whole stable-facet hypothesis has a finite semidefinite dual representation with one nonnegative scalar and one 3-by-3 LMI per true facet edge. Diagonals of a face triangulation are not used. No independent polar metric, freely chosen foot, or separate vertex mass is introduced. The unmarked origin formulation is general; actual-centroid geometry must still be supplied when applying it to a homogeneous body.

This theorem connects the root-conditioned cone described analytically in archived coordinator material [internal-source-reference] to a genuinely convex finite computation. That material's older non-record bevel calculation is not a new complexity record. The present finite-LMI and convex-hull statements are coordinator derivations; no claim of literature priority is made. The scalar implication below is the homogeneous S-lemma, also discussed in Polik--Terlaky, A Survey of the S-Lemma, SIAM Review49 (2007),371--418, DOI10.1137/S003614450444614X. An elementary proof of the special case needed here is included, so that citation is not a computational dependency.

## 1. Root-fibre decomposition
For p in F, q.p=1. The metrics with this exact foot are precisely
M=alpha q q^T+L,
alpha>0, L>=0, ker L=span(p).
Indeed the foot condition is Mp=alpha q, where alpha=p^T M p. Subtract alpha q q^T. The Cauchy--Schwarz inequality in the M inner product proves L>=0, and equality gives its stated kernel. The converse follows immediately, including M>0.

Varying alpha and the positive quadratic form on p-perpendicular gives
A in D_F iff q^T A q<=0 and w^T A w<=0 whenever w.p=0 for some p in F.
Initially p may be restricted to relint F; continuity extends the condition to its closed boundary. Conversely this condition applied to the displayed fibre proves tr(A M)<=0.

## 2. A polygon turns the continuum of tangent planes into true edge wedges
For any vector w, some p in F satisfies w.p=0 iff the minimum and maximum of w.p_i straddle zero. Since the boundary vertex cycle is connected, this holds iff at least one genuine boundary edge has
(w.p_i)(w.p_(i+1))<=0.
The assertion includes zero at a vertex and zero on an entire edge. For strict sign changes it is the intermediate-value property on a polygon edge; the converse is affine interpolation on that same edge. Therefore the union of all p-perpendicular planes is exactly the union of m opposite-sign quadratic wedges. Testing only isolated vertex-perpendicular planes would NOT suffice.

## 3. Elementary exact S-lemma for one edge wedge
Two distinct facet vertices p,r with q.p=q.r=1 are linearly independent. Choose coordinates x=p.w,y=r.w,z=(p cross r).w. The coordinate matrix is invertible and rational when p,r are rational. Write the transformed quadratic A as a block matrix with top block A_2, cross vector b and final scalar c.

The condition w^T A w<=0 whenever xy<=0 forces c<=0. If c=0, b=0 is forced, since z is free on a nonempty open set of (x,y). If c<0, maximizing over z gives the two-dimensional Schur form
T=A_2-b b^T/c.
For c=0 put T=A_2. Write T=[[-a,h],[h,-d]]. Negativity on xy<=0 is equivalent to a,d>=0 and h>=-sqrt(a d). If h>=0, subtracting 2h*xy leaves a nonpositive diagonal form. If h<0, that condition says T itself is negative semidefinite. Thus in either case lambda=2 max(h,0)>=0 gives
T-lambda*sym(e1 e2^T)<=0,
and reversing the Schur complement gives
A-lambda*sym(p r^T)<=0.
The converse is immediate because lambda*xy<=0 on the wedge. This proves the required equivalence, including all singular cases. Moreover a rational A,p,r passing the wedge has a RATIONAL lambda supplied by this formula. No square root is needed in exact acceptance: check the resulting principal minors.

Combining Sections1--3 proves the finite-LMI theorem.

## 4. Exact closed convex hull of root-stable physical metrics
The same theorem has a useful primal form. Let C_F be the closed convex cone generated by R_F. Then

C_F={ t q q^T + sum_i L_i :
      t>=0, L_i>=0, p_i^T L_i p_(i+1)<=0 for every i }.

This is an exact extended semidefinite representation of the CONVEX HULL, not of R_F itself. A decomposition into these blocks is not one stable-root physical metric and cannot be substituted for its inverse.

Proof: Every root fibre metric has alpha q q^T plus a rank-two positive form supported on p-perpendicular. Spectrally decompose the latter into rank-one terms w w^T. Each w belongs to at least one edge wedge by Section2, so assign its term to that edge block.

Conversely, if L>=0 and tr(B_i L)<=0, write L=U U^T of rank r. There is an orthonormal basis z_k for which each diagonal value z_k^T U^T B_i U z_k equals tr(B_i L)/r<=0. To see this, choose a unit vector with that Rayleigh quotient between the smallest and largest eigenvalues, then induct on its orthogonal complement, whose average quotient is unchanged. Thus L=sum_k (U z_k)(U z_k)^T with every summand in the edge wedge. Each such direction is perpendicular to a point of the corresponding true facet edge. Approximate that point by interior points p_n and the direction by w_n perpendicular to p_n. The matrices epsilon_n q q^T+w_n w_n^T+epsilon_n times the orthogonal projection onto p_n-perpendicular are in R_F and tend to w w^T. Likewise q q^T is a root-fibre limit. Finite sums therefore belong to C_F.

Finally the displayed sum of cones is closed: every summand is positive semidefinite, so bounded trace of the total bounds each L_i and t. A convergent sequence of totals therefore has a simultaneously convergent subsequence of all components, preserving every closed inequality. This proves the equality without a hidden closure qualification or conic-duality regularity assumption.

## 5. Direct arrow-stress use and strictness
For true directed primal edges a->b let T_ab=sym(a(b-a)^T). Choose nonnegative weights w_ab and A=sum w_ab T_ab. If every chosen arrow is nonnegative in a physical M, then tr(A M)>=0.

If A is a nonzero member of D_F in three dimensions, in fact tr(A M)<0 for EVERY M>0 whose foot is in the CLOSED facet F. Here is the strictness argument. The plane restrictions allow at most one positive eigenvalue. If A has a positive eigenvalue and a nonzero kernel vector n, adding arbitrary multiples of n to a positive quadratic direction shows that every p in F must satisfy p.n=0; the facet spans R^3, a contradiction. Thus a non-negative-semidefinite member has inertia (+,--), with no zero eigenvalue. Equality in the root-fibre trace would force the entire two-dimensional plane restriction to vanish, which would give a singular matrix, impossible. If A is nonzero negative semidefinite, strictness follows directly from M>0. This argument is specifically three-dimensional; boundary-foot strictness in dimension two is not asserted.

For a transparent uniform margin choose any fixed positive definite reference C and delta>0 and test A+delta C in D_F by the finite LMIs. Then
sum w_ab D_ab(M)<=-delta tr(C M)<0
throughout the closed root facet. This contradicts all selected weak arrows at once. The finite search variables are just the arrow weights, delta and the m edge multipliers; the constraints are linear scalar equations/inequalities and LMIs. All weights and multipliers may be certified by exact rational principal minors when a strict rational certificate has been found. With lambda_i=0 this contains the old globally negative-semidefinite stress method.

Absence of a positive margin, a failed solver, or feasibility in C_F is NOT a physical S1/U1 witness. The remaining gap is genuine nonconvex root geometry, not an omitted inverse that may be independently reset. Whole E17, whole H5, and the complexity bracket34..622 are unchanged by this representation alone.

## 6. A sharp limitation: every point of the facet plane is a hull foot
The convex hull qualification cannot be removed, even for an actual homogeneous cube. More strongly, for ANY true facet F in dimension three and ANY point u of its affine plane, some average of two metrics in R_F has actual normal foot u. Thus membership in C_F alone gives no bounded location for the normal foot, although C_F remains a proper constrained cone of matrices.

Apply an origin-fixing linear coordinate change so the facet plane is z=1 and q=e3. Choose two distinct interior feet u1,u2 in its planar polygon such that u is not on their line. This is always possible for a two-dimensional facet. Put vi=u-ui. Solve the two independent linear equations f.v1=1 and f.v2=-1. For any epsilon>0 let
G1=f f^T+epsilon*(I-v1 v1^T/|v1|^2),
G2=f f^T+epsilon*(I-v2 v2^T/|v2|^2).
Both are positive definite; G1 v1=f and G2 v2=-f. Set
Mi=[[Gi,-Gi ui],[-ui^T Gi,1+ui^T Gi ui]].
Its Schur complement is1 and its top-plane foot is exactly(ui,1). But (G1+G2)u=G1 u1+G2 u2, so the same inverse of (M1+M2)/2 has normal foot (u,1). All matrices and the construction are rational when the selected geometry is rational. An interior target can also be treated this way; no boundary limit is required. This is a physical common-inverse calculation, not an independently prescribed polar point.

A small exact control uses the actual uniform cube [-1,1]^3 at its centroid0 and its top square. Set u1=(1/2,0),u2=(0,1/2),
G1=[[9/4,-149/100],[-149/100,1]],
G2=[[1,-149/100],[-149/100,9/4]],
and Mi as above. Both have strict top stability, while their average has top-plane foot (38/27,38/27,1), outside the square. These are not110 bodies or a new complexity construction. This result explains why a failed root-dual certificate cannot be treated as a physical surviving root case. Additional true-arrow or spectral constraints can still separate the cone; the finite exact LMI representation is useful precisely as a controlled relaxation.

## 7. Exact executable control and recovery
The accompanying self-contained root_cone_exact.py uses CPython3.13.5 and SymPy1.14.0, no external inputs. It computes the rational edge multipliers by Section3, checks ALL principal minors, and applies them to the literal non-record bevel body at t=1/4 from archived coordinator material [internal-source-reference]. It independently integrates that actual body from its true maximal facets, recovers all supporting triples and17 true edges, verifies the actual centroid, the nonzero stress A+5I in the root dual, and a physical SPD control for the three selected positive primal arrows. This is a finite-LMI demonstration of the preserved bevel obstruction, not a new global bevel theorem. It also checks the cube and arbitrary-target hull-gap constructions above exactly.

The proof of Sections1--6 is analytic; the code checks these finite controls and is not a proof-assistant formalization. Normal and source-only executions and exact recovery pins are supplied in the capsule below. H5 determinant-lift code and its actual probes are a separate source unit. No new H5 shape exclusion, E17 closure,110 attainer or change to34..622 is implied by these controls.

Recovery input is exactly material [internal-source-reference]. Save its complete literal text as root_cone_exact.py (5216 bytes, SHA-256 a720b725ff3670fb37e7f900638a183d2ef4f7e16cafb0a8ea7c45e4cf6afc47). Run with assertions enabled:

    python -B root_cone_exact.py > root_cone_exact_report.out

Expected output: root_cone_exact_report.out,7153 bytes,SHA-256 4482a2592c809617a77aaf178441ae8ebe0312cc964e0b716160b67d474e7926. Terminal marker: ROOT_FACET_EDGE_LMI_AND_HULL_GAP_V1_PASS. Both the ordinary execution and a fresh-directory source-only execution containing only this exact input were observed by the coordinator, with matching output hash and no stderr. The source includes all exact input coordinates, facet cycles, weights, matrices, chosen parameters and output generation; no original sandbox or old bevel capsule is needed for this control. The historical archived coordinator source is retained for chronology, not a missing recovery input.
