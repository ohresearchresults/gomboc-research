# material-68e5b3c1a525

Historical AI scientific source/proof material. Statements retain their original scope; this is not an independently reviewed theorem.

Public derivative: internal-record-identifiers-replaced.

---

# UNIFORM_FACE_STRATUM_PROJECTIVE_PROPERNESS_AND_BALANCED_COMPACTNESS_V1

## 1. Result identity and evidence boundary

This is a complete coordinator analytic proof. No finite search, numerical optimization, unpreserved program or data array is a proof premise. It advances the connection between projective horizons and the full balanced E17 normal form; it does NOT exclude that normal form, exhibit a110 body, change34<=C_min<=622, or prove the exact minimum.

Accepted sources actually read in full in this continuation:

(A) PROJECTIVE_JOINT_MONOSTATIC_PROPERNESS_V1, material [internal-source-reference],16904bytes,SHA256 c1fb348aa34b5357be23eb9c19209c106053f6e38989e0768bb8d39608f7c39e. It contains the elementary two-half metric lemma, its reciprocal-polar version, maximum-tetrahedron bounds, strict-feature cluster persistence and the fixed-original-polytope horizon proof.

(B) RAVEN24_ALL_PYRAMIDS_NO_110_V1, immutable result minimum-0022,SHA256 85b0f28d8e4c53b1e4d13566ebcacb6b1bfcd92547d5524599743dde7534de92. Every genuinely uniformly filled convex pyramid at its own volume centroid, under any SPD metric, has at least two STRICT stable facets OR at least two STRICT unstable vertices, including arbitrary other weak features. The strict conclusion is essential.

(C) K34_ACTUAL_ADJACENT_TRIANGLE_EFFECTIVE_GAP_164_V1, material [internal-source-reference],32981bytes,SHA256 e651580532c14de8d0bf73a5b97f70a262b64faf5ecbf5b16c0803765806e25f. Its sections2-3 restate completely the accepted C34_MAXSIMPLEX_CHART_V3 compactness and real-geometry proof: all true joint10/17/9 bodies, allowing other weak points, have collision-free compact normalized realization charts. This compactness is OLD accepted research, not claimed as new here. Source(C) also proves explicit extremely small adjacent-triangle gaps by JPT; those numerical gap constants are not used below.

Its actual weak component lower-bound authorities, read as complete immutable payloads in this continuation, are minimum-0054,SHA256 4e39e8c2a461dc76a76e49153b9f70ace7e0e287cb3fe5e6b3c3733a8c24d774, and minimum-0024,SHA256 b578a01ead261c6f7745122c22f4bb4767884e46ac46e1531b4e749a19332f95. Unique STRICT U implies V>=10 and unique STRICT S implies F>=9 even with other weak points. No new replay of their executable certificates is asserted.

(D) BALANCED_E17_COMPLETE_EIGHT_CUT_TWO_PROJECTIVE_NORMAL_FORM_V1, immutable result minimum-0125,30126bytes,SHA256 3e3db66e34ca7337ba6d0afc4e4cdcd2b9b4d7735f5b3c1cd75b959956def185. Its full proof and exact source were read. Its eleven-parameter normal form and the intrinsic normalized-base fingerprint, up to finite square symmetries, are accepted premises. It does not assert uniqueness of all eleven parameters, and neither does this result.

The new assertions are (I) uniform projective properness over a compact family that remains inside one true face stratum, and (II) compactness INSIDE THE STRICT ELEVEN-PARAMETER DOMAIN of the entire balanced joint-monostatic feasibility set. Other physical weak points remain allowed throughout. No explicit numerical values of the two new uniform constants delta and eta are supplied.

## 2. Uniform face-stratum projective properness

Let T be a compact metric parameter space. Let P_t=conv(X_1(t),...,X_N(t)) be a continuous family of full-dimensional convex3-polytopes, all containing0 in their interiors. All displayed vertices are true and distinct. Assume their labelled true face lattice is the same for every t, including parameter limits. These hypotheses imply a common positive interior radius about0 and a common finite outer radius. Put

 l_i(t,p)=1+p dot X_i(t),
 D_t={p: l_i(t,p)>0 for every i},
 P_(t,p)=conv(X_i(t)/l_i(t,p)).

Every image is uniformly refilled, and its reference point is its own ordinary volume centroid. Let

 J_T={(t,p):p in D_t and some SPD M gives STRICT S=U=1}.

THEOREM I. J_T is a compact subset of the open positivity domain over T. In particular there is eta_T>0 for which l_i(t,p)>=eta_T at every point of J_T and every vertex i. The assertion is trivial when J_T is empty. It does not require a source P_t itself to be joint monostatic.

This strengthens the fixed-P result in(A). The distinction matters: varying original barycentric coefficients generally cannot be treated as constant. The face-stratum hypothesis below makes the necessary coefficients EXACTLY zero, not merely asymptotically small.

### 2.1 A maximum tetrahedron must be adapted to the entire limiting pole face

Suppose t_n->t_*, p_n->p_*, l_i(t_n,p_n)>0, and min_i l_i(t_n,p_n)->0. A common interior radius bounds all p_n, so passage to such a convergent subsequence is legitimate. Set

 S={i:l_i(t_*,p_*)=0}.

It is the vertex set of a nonempty proper exposed face F_* of P_(t_*), of dimension d in{0,1,2}. Because the labelled true face lattice persists, the same indices S form a flat d-dimensional face F_n of every source P_(t_n). Their source vertices converge to the true distinct vertices of F_*.

At each n choose a maximum-volume vertex tetrahedron of the IMAGE P_(t_n,p_n). Pass to a subsequence with one fixed ordered index set I of four vertices. Let Z=I intersect S, k=|Z|. Write Delta_I(n) for its original source determinant. Its image absolute determinant is exactly

 |Delta_I(n)| / product_(i in I) l_i(t_n,p_n).

First, k<=d+1: more than d+1 vertices of the same flat source face would make this tetrahedron affinely dependent at every n. Second, every subset of at most d+1 true vertices of F_* is affinely independent here. For d=2 this says that three true vertices of a convex polygon cannot be collinear; dimensions0,1 are immediate.

Complete the limiting vertices Z to a set J_S of d+1 independent vertices of F_*, and then to a full tetrahedron J with 3-d vertices outside S. This is possible because P_(t_*) is full-dimensional. Delta_J(n) tends to a nonzero determinant. The common vertices Z cancel from the ratio of image volumes:

 V_I(n)/V_J(n)
 =|Delta_I(n)/Delta_J(n)|
  *[product_(j in J\I) l_j(n)]/[product_(i in I\J) l_i(n)].

Every denominator factor on the right belongs to a vertex outside S and has a strictly positive limit. The determinant quotient is bounded. If k<d+1, the numerator contains at least one additional factor with index in S and tending to zero. The ratio would tend to zero, contradicting maximality V_I(n)>=V_J(n). Therefore

 k=d+1.

Now choose J to contain exactly the same d+1 indices Z and complete them using vertices outside S. All denominator factors in the volume ratio that survive cancellation have positive finite limits. Maximality then also forces Delta_I(n) to stay bounded away from zero. In particular the original tetrahedron I has a genuinely independent limit, despite possible unrelated nonfacet coplanarities elsewhere in the source realization.

### 2.2 Exact zero coefficients and the limiting affine join

Normalize the maximum IMAGE tetrahedron I to the standard tetrahedron0,e1,e2,e3. All normalized image vertices lie in[-1,1]^3, since every affine barycentric coordinate has absolute value at most1 by determinant replacement. Pass to a subsequence on which all normalized image coordinates converge.

Let alpha_ij(n) be the SOURCE affine barycentric coordinates relative to I. The previous step makes these well-defined and convergent. The normalized IMAGE barycentric coordinates satisfy the exact identity

 beta_ij(n)=alpha_ij(n)*l_j(n)/l_i(n).

For i in S, the source vertex X_i(t_n) lies in the actual flat face F_n, whose affine span is generated by the d+1 basis vertices Z. Consequently

 alpha_ij(n)=0 for every j in I\Z, EXACTLY for every n.

Thus all image limits from S lie in the standard face-spanned affine subspace on Z. For i outside S, l_i has a positive limit, alpha_ij(n) remains bounded and l_j->0 for j in Z. Hence beta_ij(n)->0 on Z. These other image limits lie in the complementary standard affine subspace on I\Z.

Each block contains its own standard basis vertices. The full-dimensional limiting body is therefore the genuine affine join of a d-dimensional polytope and a(2-d)-dimensional polytope. In dimension3 this is a pyramid when d=0 or2, and a tetrahedron when d=1. No independent moments, invented center or surrogate density enter this conclusion.

### 2.3 Metric and centroid limits finish the theorem

The elementary facts from(A) are recalled to make the closure mechanism explicit. In a maximum-tetrahedron frame a true uniformly filled body B has, at its own centroid g,

 (1/(4 sqrt(3))) unitball subset B-g subset (3 sqrt(3)/2) unitball.

For a general centered body rB subset K subset RB, the two-half quadratic maximum argument shows U=1 implies lambda2/lambda1>(r/R)^2. Apply the same argument to the actual polar under M^{-1} to get S=1 implies lambda3/lambda2>(r/R)^2. Thus after lambda_max(M)=1 the closure of jointly feasible metrics in this frame satisfies

 (1/104976) I <= M <= I.

The actual volume centroids converge in the bounded full-dimensional geometric limit. The limiting metric is SPD. Strict U vertices persist even when vertex labels merge: choose the largest quadratic norm inside each cluster, use

 x^T M(y-x)=[q(y)-q(x)-q(y-x)]/2

to obtain all within-cluster strict inequalities, and use the limit's strict inequalities outside the cluster. Actual pole clusters give the same persistence for S in the reciprocal metric. These are precisely the full lemmas proved in(A).

The limiting actual uniform pyramid has two strict S or two strict U by(B), after absorbing the limiting SPD into an affine image. Their persistence contradicts strict S=U=1 in the approximating bodies. Hence J_T has no boundary sequence with a vanishing l_i.

For a convergent sequence with all limiting l_i positive, the same metric compactness and strict-feature persistence give at most one strict S and one strict U in the limit. Every interior-reference-point convex polytope has at least one strict farthest vertex, and its actual polar supplies at least one strict stable facet. Thus the limit has exactly one of each. This proves closedness inside the positivity domain. Compactness of T, boundedness of p from the uniform interior ball, and the boundary exclusion prove Theorem I.

## 3. The critical realization compactness is already accepted

The whole joint10/17/9 realization class admits the compact maximum-tetrahedron normalization in(C). An elementary alternate explanation, using(A), is useful here but is not a new compactness claim.

A convergent normalized sequence has a full-dimensional limit and an SPD limiting metric. Cluster persistence makes its strict S and U at most1, and universal existence makes each exactly1. The accepted weak-scope lower bounds give V>=10,F>=9 in the limit. The fixed lists provide at most10 vertices and9 poles, so all labels remain distinct true vertices/facets.

Each old edge between two distinct vertex labels remains in the intersection of its two distinct supporting planes, hence is a true edge of the limit. Its endpoints cannot cease being endpoints because they remain extreme vertices. Euler gives exactly17 limit edges, already accounted for by the old list. Thus there are no extra incidences and the full face lattice persists. This is the geometric collision-free part of(C). In particular a sequence of joint balanced bodies has, after subsequences and simultaneous affine/metric normalization, a joint balanced limit with the same labelled face lattice.

The positive eigenvalue bound just recalled implies a stronger trace-normalized metric cutoff than the older maximum-simplex proof required: set c=1/324. Since lambda1<lambda3/c^2 and lambda2<lambda3/c,

 trace(M)=1 => lambda_min(M)>c^2/(1+c+c^2)=1/105301.

This improves that chart's old lower cutoff1/1082881, not the intrinsic isotropic theorem, and does not exclude a new physical body. Its potential computational usefulness has not been tested.

## 4. The full balanced parameter domain

Use exactly the source(D) normal form. With

 t=((sx,sy),(wx,wy),(nx,ny),(ex,ey)),

all eight entries are positive, and

 sx+ex<2, wx+nx<2, sy+wy<2, ny+ey<2.

The body C(t,a), a>0, has the true base vertices

 0=(-1+sx,-1,0), 1=(-1,-1+sy,0),
 2=(-1,1-wy,0), 3=(-1+wx,1,0),
 4=(1-nx,1,0), 5=(1,1-ny,0),
 6=(1,-1+ey,0), 7=(1-ex,-1,0),

and apices8=(-a,0,1),9=(a,0,1). Set

 K(t,a,u,v)=T_(u,v,0)(C(t,a)),
 T_(u,v,0)(X)=X/(1+u*x+v*y).

All ten denominators must be positive. Every body in the entire balanced incidence type is an affine image of such a body, at its TRUE refilled centroid and with one transported reciprocal metric pair. Define B_joint to be the set of these eleven parameter tuples that admit strict S=U=1 under some SPD metric. Other physical weak points are allowed.

THEOREM II. B_joint is compact INSIDE this strict eleven-parameter domain. In particular, if it is nonempty, there exist constants0<delta<=2/3 and0<eta<=1 such that every tuple in B_joint satisfies

 each of the eight cuts >=delta,
 each of the four surviving side lengths >=delta,
 eta/(2-eta) <= a <= 2/eta-1,
 |u|,|v| <= 3/delta,
 each of the ten original denominators >=eta/2.

These are uniform constants for the whole balanced incidence, not constants separately chosen for each fixed t. Their numerical values are not determined by this proof. If B_joint is empty the statements hold vacuously with arbitrary suitably small positive constants.

### 4.1 The intrinsic cut parameters cannot leave their true open domain

The four intrinsic basal support lines in(D) are two carrying the basal edges of the two quadrilateral facets and two carrying the middle edges of the two three-triangle blocks. They are in general projective position. Their canonical normalization to the square determines the eight cut lengths up to finitely many square symmetries. No uniqueness of the remaining three shape parameters is needed.

The canonical cut data vary continuously LOCALLY on the true balanced face stratum, up to that finite choice. Here is an explicit continuity justification. Fix a true limiting body B_* and one positive projectivity from(D) putting it in normal form. The same fixed projectivity stays positive on sufficiently close labelled bodies, after continuously aligning their basal planes by affine coordinates. The two apex heights h,k are then close to the same positive height and their planar coordinates p,q stay distinct. Put

 dvec=h*q-k*p,
 b=-(h-k)*dvec/(dvec dot dvec),
 ell(x)=1+b dot x.

Near the chosen normal form dvec is nonzero, b tends to0 and ell is positive on the whole nearby body. The identity h*ell(q)-k*ell(p)=0 means that the positive projectivity with denominator ell equalizes the two heights continuously. Continuous affine shears and scalings put the apex line horizontally at height1 and the two true quadrilateral base supports at y=+/-1. Their middle-chain lines are x=l0+l1*y and x=r0+r1*y. At the limiting body d=r0-l0>|r1-l1|=|e|, and this strict inequality persists. The rectification in(D), with positive denominator d+e*y, is therefore continuous here. The resulting cuts remain strictly positive with strictly positive surviving sides.

Now take any sequence of tuples in B_joint. Normalize the corresponding physical bodies and metrics by the accepted critical compactness(C). A subsequence converges to a true joint balanced body. The preceding local construction gives canonical cuts converging to true interior cut data. The given t_n differ from these only by a finite possible relabelling of the intrinsic square frame; after another subsequence the choice is constant. Hence the original t_n also converge to interior feasible cut data. The collection T_joint of feasible cut vectors is therefore compact inside the eight-cut domain. Since the eight cuts and four side remainders are continuous strictly positive functions on it, their common minimum is some delta>0; reduce delta if necessary so delta<=2/3. This is where the independent minimal V and F bounds matter. Arbitrary balanced bodies without joint mechanics do admit cut degenerations.

### 4.2 Re-express all remaining parameters as projectivities of a compact true source family

Use the compact source family C(t,1), t in T_joint. Its own mechanics is irrelevant. Let e0=(0,0,1/2); this point lies in the interior of every source, uniformly so by compactness. Translate by e0 to meet the origin convention of Theorem I.

The exact identity from(D) gives, with c=1/a,

 T_(u,v,c-1)(C(t,1))
   =diag(1,1,a)*K(t,a,u,v).

Thus the physical joint condition for K is equivalent, under a genuine affine change and its transported SPD, to the same condition on the left. Normalize its denominator to value1 at e0. Its parameter in the translated source coordinates is

 p'=(2a*u/(1+a), 2a*v/(1+a), 2*(1-a)/(1+a)).

The source family has a single unchanged true face lattice and lies in a compact nondegenerate realization stratum. Theorem I applies UNIFORMLY, giving0<eta<=1 with

 l'_i=1+p' dot (X_i(t,1)-e0) >=eta

at every source vertex for every joint tuple.

For the two source apices,

 l'_8=2*(1-a*u)/(1+a),
 l'_9=2*(1+a*u)/(1+a).

Their sum is4/(1+a), so a<=2/eta-1. The point(0,0,0) is a convex combination of the basal vertices. Evaluating the same affine denominator there gives2a/(1+a)>=eta, whence a>=eta/(2-eta).

For a basal vertex, its original normal-form denominator is (1+a)l'_i/(2a)>=eta/2. For an apex it is (1+a)l'_i/2>=eta/2. This establishes the claimed strictly positive common denominator cutoff without treating a nonlinear projectivity as a metric isometry.

For completeness there is an elementary explicit u,v bound in terms of delta alone. Each cut entry is between delta and2-2delta. At the origin, a corner support has unnormalized slack tx+ty-tx*ty>=delta; its planar normal has norm<=2 sqrt(2). The slack bound follows by taking the minimum of this bilinear expression at the four corners of [delta,2-2delta]^2, using0<delta<=2/3. Thus the true basal polygon contains the centered disk of radius r0=delta/(2 sqrt(2)). Positivity of1+u*x+v*y on that disk gives sqrt(u^2+v^2)<1/r0=2 sqrt(2)/delta<3/delta. This proves the stated coordinate bounds.

### 4.3 Closedness and a fully physical compact metric box

The parameter bounds just proved place all tuples in a bounded closed box separated from every true geometric and denominator boundary. Any tuple limit therefore has the same actual balanced face lattice, and its vertices and true volume centroid converge. Normalize a sequence of feasible metrics by trace=1. On the resulting compact family of full-dimensional centered bodies the two-half/polar lemma bounds both successive eigenvalue ratios away from zero. An SPD metric subsequence therefore converges. Strict S/U persistence gives at most1 of each in the limit and their universal existence gives exactly1. This proves closedness of B_joint, hence Theorem II.

One can make the last metric bound explicit in terms of the two existential constants, without adding an independent mass model. The original basal inradius is at least r0=delta/(2 sqrt(2)). Under the planar map x->x/(1+(u,v) dot x), the actual basal poles change from q to q+(u,v). Their norms are at most2/r0, so the transformed base contains a centered disk of radius delta/(4 sqrt(2)). The point(0,0,1) lies on the actual image of the apex edge and is fixed by this projectivity. Hence K contains the convex cone over that disk with apex(0,0,1), and contains a ball of radius delta/16 about e0. The true centroid's depth in every support interval is at least one quarter of the width, giving centered inradius at least delta/32.

Since a<=2/eta-1 and all original denominators are at least eta/2, every raw image vertex has Euclidean norm at most5/eta^2. Thus diameter<=10/eta^2 and the own-centered outer radius is at most8/eta^2. The two-half lemma may consequently use

 c=(delta*eta^2/256)^2.

For trace(M)=1, lambda_min>=c^2/3 gives the explicit necessary box

 [delta^4*eta^8/(3*2^32)] I <= M <= I.

These deliberately loose constants have not been optimized. Their role is to identify a compact physical metric domain once delta and eta are quantified, not to pretend that those two constants have already been computed.

## 5. Consequence for exact feasibility and its actual limitation

For the fixed balanced incidence, choose a primal rooted spanning tree and a rooted spanning tree of the actual facet poles. Impose their nine and eight weak arrow inequalities with one reciprocal pair M,M^{-1}. An arrow x->y with x^T M(y-x)>=0 forces q(y)>q(x), so these trees exclude extra strict U or S. The designated roots are necessarily strict: any outgoing nonnegative product at a root would give a larger quadratic norm at a neighbor, whose tree path back to the root strictly increases norm again, a contradiction. Conversely unique strict U and S permit these choices of weak escape trees. Thus the finite union of these systems is EXACTLY the joint strict S=U=1 problem, allowing other physical weak points.

The exact true centroid and poles in the eleven-parameter family are rational functions with positive actual denominators, as supplied in(D). Their denominators may be cleared with their true signs, not replaced by adjustable weights. A symmetric trace-normalized metric contributes five independent coordinates. Therefore this entire balanced joint feasibility problem has a finite union of compact basic closed semialgebraic models in SIXTEEN real coordinates, with actual rational centroid formulas; the box constants can be chosen rational below the positive gaps above. No auxiliary inverse metric is independent: use adj(M) after multiplying by det(M)>0.

This is a smaller explicit intrinsic parameter setting than the general33-variable E17 max-simplex map, but not a claim of a low-degree, efficient, or already executed decision procedure. The degrees and coefficient heights of a complete sixteen-coordinate implementation have not been calculated here. The existential cutoffs are not numerical input to a certified finite search until quantified or replaced by exact covering witnesses. Generic quantifier elimination in principle does not establish emptiness, and no such elimination or continuous coefficient cover is claimed.

For the actual no-additional-weak110 target, the physically interpreted four-primitives-per-edge census must still be imposed. The no-additional-weak subset need not itself be closed. Neither Theorem I nor II asserts universal weak-point regularization, and neither proves H=0 merely by counting S and U when extra weak points are allowed.

## 6. Boundary of applicability and next useful work

Theorem I requires a source family compact INSIDE a true face stratum. It is invalid to treat varying barycentric coefficients as constants at arbitrary degenerating source shapes. The maximum-tetrahedron face-adaptation argument is exactly the missing bridge that permits this uniform extension.

The balanced conclusion uses the accepted intrinsic four-line fingerprint and collision-free critical compactness. It is not automatically a theorem for the two other octagonal-base degree types(3,7),(4,6), although their own normal forms may admit analogous arguments.

No entire balanced orbit, graph type, full E17 layer or lower bound above34 is closed. The canonical exact622 body remains the attaining upper example, not a proven minimum.

A useful next step is to quantify delta/eta from actual balanced geometry or derive a structural common-metric contradiction on this now intrinsically compact domain. Optimizing only older narrow equal-angle families does not resolve it. Four-contact nonsimplicial regularization remains a distinct live direction.

## 7. Exact preservation

This complete UTF-8 document is the exact recovery unit for the new analytic result. It uses no originating sandbox files or numerical observations. Its proof dependencies are the full immutable sources(A)-(D) identified in section1. The trace-normalized105301 cutoff and the displayed conditional boxes follow by the explicit algebra above and are not reported as machine-observed checks. No external priority claim, independent replay of accepted source computations or formal proof-assistant verification is made.
