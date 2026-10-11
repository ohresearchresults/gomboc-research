# material-cf75f3a88147

Historical AI scientific source/proof material. Statements retain their original scope; this is not an independently reviewed theorem.

---

# UNIFORM_AFFINE_SIMPLEX_COMPACTIFICATION_110_V1

## Result and limits
A coordinator analytic reduction for the WHOLE homogeneous-polytope problem, not one projective orbit or frozen pole family. Every full-dimensional homogeneous convex3-polytope having exactly one strict stable facet and exactly one strict unstable vertex admits a coordinate gauge with all of the following properties:

1. A maximal-volume inscribed tetrahedron is the fixed regular tetrahedron with vertices (1,1,1),(1,-1,-1),(-1,1,-1),(-1,-1,1) before translating by the actual volume centroid.
2. Its centred coordinate body K contains the Euclidean ball of radius1/2 and lies in the Euclidean ball of radius2sqrt(11), both centred at0.
3. Its physical SPD quadratic form M has adjacent ordered eigenvalue ratios lambda1/lambda2<176 and lambda2/lambda3<176, hence condition number<30976.
4. After trace M=1, lambda_min(M)>1/31153 and lambda_max(M)<30976/31153.

Extra physical weak equilibria do not invalidate this necessary bound when the strict stable and unstable counts are both one. Proper110 is therefore covered. This does NOT assert that the proper110 feasible set is closed, does not exclude any new incidence type, and does not evaluate the minimum. It supplies an explicit universal compact CONTAINER for joint shape/metric search. Degenerate incidence strata and weak-contact boundaries still require their own exclusion or feasibility analysis.

The proof is self-contained below. Its ingredients are elementary convex geometry; no priority claim for the underlying classical centroid-depth or affine-normalization principles is intended. This derivation does not apply an origin-symmetric John/Lp-John theorem to a nonsymmetric body and uses no free moment matrix. No computer calculation materially produces this theorem.

## 1. Elementary centroid depth in dimension three
Let P be a full-dimensional convex body and fix a unit direction u. Write a=min_P u.x, b=max_P u.x and w=b-a>0. Let A(t) be the area of the section at u.x=t. Choose a point v of P with u.v=b. For a<s<t<b, convexity maps the section at s into the section at t by homothety with centre v and ratio (b-t)/(b-s). Therefore

  A(t)/(b-t)^2 >= A(s)/(b-s)^2.

Thus the actual slice density A(t) is the reference cone density (b-t)^2 multiplied by a nonnegative nondecreasing function h(t). Weighting a probability measure by a nondecreasing function cannot decrease the expectation of t: this follows directly by integrating (t-s)(h(t)-h(s))>=0 over two independent copies of the reference measure. Truncation and monotone limits handle a possible unbounded h near b. The reference cone density has mean a+w/4, by direct polynomial integration. Consequently the volume centroid g satisfies

  u.g >= a+w/4.

Applying the same argument in direction -u gives u.g<=b-w/4. In particular both distances from g to the two supporting planes are at least w/4. This proof uses the genuine UNIFORM SOLID centroid. It is not a statement about vertex averages or a projectively transported old centroid.

## 2. Maximal-volume tetrahedron gauge
Choose a maximal-volume tetrahedron S contained in P. It exists by compactness and has positive volume. For a polytope it can be chosen with true vertices: absolute determinant is convex separately in each point, so successive maximization over the body can move every corner to a true vertex without reducing the maximal volume.

Apply an invertible affine map sending its four corners to

  u0=(1,1,1), u1=(1,-1,-1),
  u2=(-1,1,-1), u3=(-1,-1,1).

Call the transformed, not yet centred body P0. Uniform density is preserved up to a constant Jacobian, so its actual centroid g0 is the affine image of the original centroid. For every x in P0 let lambda_i be its barycentric coordinates relative to S. Replacing corner i of S by x multiplies signed volume by lambda_i; maximality therefore gives

  sum lambda_i=1,  -1<=lambda_i<=1 for all i.

The regular tetrahedron vectors have ui.ui=3 and ui.uj=-1 for i!=j. Consequently

  ||x||^2=4 sum lambda_i^2-1.

On the polytope {lambda in[-1,1]^4:sum lambda_i=1}, the maximum of the convex function sum lambda_i^2 is attained at a vertex. Such vertices are exactly the permutations of (1,1,-1,0): at least three active cube bounds are required, and the fourth coordinate must then be0. Thus sum lambda_i^2<=3 and

  P0 subset ball(0,sqrt(11)).

Also g0 belongs to P0, so K=P0-g0 is contained in ball(0,2sqrt(11)).

For every unit u the four scalars a_i=u.ui have average0 and average square1, because sum ui=0 and sum ui ui^T=4I. Their range is at least2. Indeed, for any values in[m,b], (a-m)(b-a)>=0 gives variance<= (b-m)^2/4 after averaging and completing a square. Here the variance is1. Hence every width of S, and therefore every width of P0, is at least2.

Section1 then puts g0 at distance at least1/2 from EVERY supporting plane of P0. Equivalently,

  ball(0,1/2) subset K subset ball(0,2sqrt(11)).     (2.1)

This bound is uniform over all vertex counts and all full-dimensional shapes. It does not assume an a priori aspect-ratio bound or a fixed combinatorial type.

## 3. Two strict maxima from a spectral gap
Let a convex polytope K have0 interior and satisfy rB subset K subset RB. Let M be SPD with lambda1>=lambda2>=lambda3>0 and unit principal eigenvector e1. If

  lambda1*r^2 >= lambda2*R^2,                       (3.1)

then K has at least TWO strict unstable vertices for the physical norm squared f(x)=x^T Mx.

Proof. On the section e1.x=0, f(x)<=lambda2 R^2. The points +r e1 and -r e1 belong to the two opposite half-polytopes and have f=lambda1 r^2. On each half-polytope maximize the strictly convex function f. If its maximum is greater than the section bound, a maximizer lies strictly on that side and is a true vertex of K. If equality holds throughout this comparison, the corresponding point +/-r e1 itself is a maximizer lying strictly on that side. A maximizer of a strictly convex function on a polytope must be an extreme point, so again it is a true vertex of K, not a newly cut section vertex.

At a maximum x strictly in one half-space, every incident true edge direction e has x^T M e<0. Otherwise f(x+t e)=f(x)+2t x^T M e+t^2 e^T M e would increase for sufficiently small t>0 while staying in that half-polytope, a contradiction. Thus the two opposite-side maxima are two distinct STRICT unstable vertices. This includes equality in(3.1); it does not rely on absence of weak equilibria elsewhere.

Consequently U=1 implies

  lambda1/lambda2 < (R/r)^2.                       (3.2)

No centroid assumption was used in this spectral lemma.

## 4. The same-origin polar gives the other spectral ratio
Let K be the centred coordinate polytope and Kpolar={q:q.x<=1 for every x in K}. The physical metric is M and its one reciprocal metric is N=M^-1. A true facet with pole q is strictly stable precisely when its physical orthogonal foot Nq/(q^T Nq) belongs to the relative interior of that facet. In terms of adjacent true facet poles q', this is exactly

  q^T N(q'-q)<0 for every true neighbor q'.

These are the strict instability inequalities at vertex q of Kpolar in the metric N. The local facet inequalities suffice because the true ridges give the facet polygon's irredundant inequalities in its affine plane; equivalently the neighboring polar edges generate the tangent cone at q. Thus S(K,M)=U(Kpolar,N). This uses the SAME reference0 and inverse metric; it does not assume that the polar has a uniform-density centroid at0.

From rB subset K subset RB one has (1/R)B subset Kpolar subset (1/r)B. Applying Section3 to Kpolar and N, whose two largest eigenvalues are1/lambda3 and1/lambda2, shows that S=1 implies

  lambda2/lambda3 < (R/r)^2.                       (4.1)

With the completely uniform bounds(2.1), (R/r)^2=176. Combining(3.2) and(4.1) gives

  lambda1/lambda2<176,
  lambda2/lambda3<176,
  lambda1/lambda3<176^2=30976.

If tr M=1, then lambda1<176^2 lambda3 and lambda2<176 lambda3 yield

  1<(176^2+176+1)lambda3=31153 lambda3.

Similarly lambda2>lambda1/176 and lambda3>lambda1/176^2 give lambda1<30976/31153. This proves all stated strict bounds.

## 5. Why changing coordinates does not change the physical problem
Write the original physical centred vertices as y_i=T X_i with an invertible linear T, where X_i are the centred vertices in the tetrahedron gauge. Then all original Euclidean vertex mechanics are encoded by M=T^T T on X_i. Uniform-density centring is preserved because T has constant determinant. Scaling M by a positive scalar changes no equilibrium sign; trace normalization is harmless.

The transformed body K itself need not be110 in the coordinate Euclidean metric I. The theorem concerns the PAIR(K,M), which represents exactly the original physical body. It is not a claim that the physical110 class is invariant under arbitrary affine shape changes with metric held fixed. The maximal-volume simplex is a coordinate gauge, not an extra restriction on physical candidates.

## 6. Compact joint container and the remaining logical gap
For a fixed finite vertex-label bound, all coordinate vectors lie in the closed ball of radius2sqrt(11), every coordinate body contains the ball of radius1/2 and has actual centroid0, and normalized candidate metrics lie in the compact SPD matrix set

  tr M=1, M >= (1/31153) I.

Taking the closed non-strict container also allows limiting equality in these normalization bounds, even though actual S=U=1 satisfies the strict versions. Limits remain full-dimensional and have their actual volume centroid at0; the uniform inscribed ball prevents dimensional collapse and keeps positive volume. Vertex coincidences, disappearing edges and merged facets can still occur.

In the first open10/17/9 layer, the maximal-volume simplex can be selected from four of the ten true vertices. Its maximality relative to the other vertex tetrahedra is a finite family of determinant inequalities. The actual centroid is obtained from genuine positive volume fans, and same-metric primal/adj(M)-polar equilibrium predicates are polynomial after positive denominator clearing. This gives a globally bounded joint semialgebraic formulation covering arbitrary realizations, rather than only a fixed source's projective orbit.

Compact containment alone is NOT an exclusion, does not ensure a uniform positive certificate margin, and does not close merged-facet or physical weak-contact strata. A boundary limit with fewer true features must be analyzed using the applicable actual-centroid/refinement theorem with its correct graph scope. No such additional boundary theorem is asserted here. The reduction also need not be computationally small: finite exact decision and a practical proof are different obligations.

The useful research consequence is that genuinely unbounded shape AND metric parameters can be removed simultaneously for proper110 search, without assuming the finite projective block of any one family covers all candidates. The accepted bracket remains34<=C_min<=622, and the lower exclusion and attaining construction are still separate.
