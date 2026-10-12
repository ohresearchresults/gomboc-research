# material-d3d13642a4b2

AI research material · [Export notes](../catalog/coverage.md#text-records)

---

# PROJECTIVE_CENTERING_WINDOW_V1
## Recovery capsule part 2 of 2: actual projective centering inside a strict mechanical chamber

This is a coordinator-authored general sufficient theorem and complete exact nonwinning controls. It is NOT a new class110 construction, NOT a lower exclusion for the entire10/17/9 layer, and NOT an improvement of the canonical C622 upper bound. The two complementary conclusions needed for the exact minimum remain separate: the accepted lower bound is34, the canonical actual uniform attainer has622, and no equality between them has been proved.

The contribution to this run is the connection between actual uniform projective centering, affine projective escape inequalities at a specified reference point, and a rigorously certified bounded region in which the unique centering correction preserves those inequalities. General projective centering existence/uniqueness is established mathematics, not claimed as a new discovery here. A primary reference is Ivan Izmestiev, *Fitting centroids by a projective transformation*, arXiv:1409.6176v1,22September2014, Theorem2 and Sections4.1–4.3; HTML source https://arxiv.org/html/1409.6176v1 . The basic point/body centering theorem applies to full-dimensional convex polytopes. Its two-body theorem requires hypotheses not granted by an ear-cut child touching its parent. We do not use that theorem to justify arbitrary surgery.

## 1. Actual body, reference, metric and projective domain

Let K be a compact full-dimensional convex polytope in R^3 with0 in its interior. Let x_i be its actual vertices, and let a_f be its true maximal facet poles in the convention a_f.x<=1. Fix ONE positive definite symmetric matrix M and put N=M^-1. The simultaneous use of M and N is essential. Such a metric describes the Euclidean mechanics of an actual affine image A K with A^T A=M; uniform volume centroids transform affinely because the Jacobian of A is constant.

For p in the open convex domain

D_K={p:1+p.x_i>0 for every actual vertex i},

write f_p(x)=1+p.x and T_p(x)=x/f_p(x). Positivity holds throughout K, and T_p preserves convexity, the complete face lattice, true edges and true maximal facets. It fixes0. For general p, however,0 is NOT the volume centroid of the uniformly refilled body T_p K. The actual countercontrol in Section8 shows that even the strict mechanical census can change when that distinction is ignored.

All integrals below are uniform volume integrals of the stated actual body, or their exact change-of-variables expressions over K. No freely chosen vertex masses are introduced.

## 2. Actual volume potential and exact centering

The derivative of T_p is f_p^-1 I-f_p^-2 x p^T. The matrix determinant lemma gives det D_x T_p=f_p^-4. Consequently

Phi(p)=Vol(T_p K)=integral_K f_p(x)^-4 dx,

J(p)=integral_(T_p K) y dy=integral_K x f_p(x)^-5 dx,

g(p)=J(p)/Phi(p).

Differentiation on the positive domain gives

 grad Phi(p)=-4 J(p)=-4 Phi(p) g(p),
 Hess Phi(p)=20 integral_K x x^T f_p(x)^-6 dx>0.

The last inequality is positive definiteness: a nonzero linear functional cannot vanish almost everywhere on a full-dimensional body. Thus Phi is strictly convex, and its stationary points are exactly the projective images whose OWN uniform centroid is0. There is at most one such parameter.

For completeness, existence for a convex polytope follows directly. D_K is bounded since K contains a Euclidean ball about0. If p tends to a boundary point of D_K, some actual vertex v has f_p(v) tending to0. Choose a genuine nondegenerate tetrahedron inside K with vertex v and an interior opposite triangle. Its section at fraction s from v has area proportional to s^2. Uniform boundedness of p gives f_p((1-s)v+s z)<=epsilon+C s, epsilon=f_p(v). Therefore its contribution to Phi is bounded below by a positive multiple of integral_0^s0 s^2/(epsilon+C s)^4 ds, which diverges as epsilon decreases to0. Phi tends to infinity at every boundary approach. It attains a minimum in D_K, hence has a unique centering parameter p_*.

This proof is a direct specialization of the established point/body projective-centering principle. The quantitative theorem below locates p_* in a region with known mechanical signs instead of merely establishing its existence.

## 3. Every fixed-reference escape numerator is affine in p

For the directed actual edge i->j define the primal reference-zero escape

 D^M_ij(p)=(T_p x_i)^T M(T_p x_j-T_p x_i).

Direct expansion yields

 D^M_ij(p)=[A_ij+B_ij.p]/[f_i^2 f_j],
 A_ij=x_i^T M(x_j-x_i),
 B_ij=(x_i^T M x_j)x_i-(x_i^T M x_i)x_j,
 f_i=1+p.x_i.

Every denominator is positive on D_K. The transformed true pole is a_f+p: substituting the inverse x=y/(1-p.y) in a_f.x<=1 gives (a_f+p).y<=1. For a directed true dual edge f->h,

 D^N_fh(p)=(a_f+p)^T N(a_h-a_f)=C_fh+D_fh.p,
 C_fh=a_f^T N(a_h-a_f),
 D_fh=N(a_h-a_f).

Thus, for a fixed actual K, fixed reference0 and fixed reciprocal pair M,N, all4E physical edge primitives have affine numerators in the same three projective parameters. Any prescribed collection of strict signs defines an open convex polyhedron, intersected with D_K. This does NOT make the OWN-centroid primitives affine for arbitrary p; only when g(p)=0 do these reference-zero primitives coincide with the desired homogeneous mechanics.

Keeping all4E primitive signs nonzero preserves every strict feature-labelled equilibrium and rules out any newly created weak packet. More economically, for class110 it is enough to retain a pair of complementary rooted escape trees, as shown next.

## 4. Complementary tree corollary and physical weak-point semantics

Suppose T is a primal spanning tree directed toward a specified vertex u, and the dual edges corresponding to true edges outside T form a dual spanning tree directed toward a specified facet s. Suppose each of the V-1 selected primal escapes and F-1 selected dual escapes is strictly positive. These are exactly E selected rows because V+F-2=E.

On a selected primal arrow x->y,

 ||y||_M^2-||x||_M^2=2 x^T M(y-x)+||y-x||_M^2>0.

Following the tree from any vertex to u proves that u has strictly larger norm than every other actual vertex. In particular every outgoing primitive from u is strictly negative: for any adjacent v,

 2u^T M(v-u)=||v||_M^2-||u||_M^2-||v-u||_M^2<0.

All other vertices have a selected positive escape. Thus u is the unique strict unstable vertex. The same proof in the true polar with N makes s the unique strict stable facet.

For every actual edge, either its selected primal arrow or its selected dual arrow is positive. Hence no four-sign packet has all entries nonpositive. There is no strict saddle and no physical weak VE, EF or VF equilibrium. Unselected zero primitives accompanied by the positive selected escape are harmless and need not be removed. The conclusion is exactly strict110 with no additional weak equilibria, provided the reference is the actual own centroid.

This is a sufficient mechanical certificate, not a claim that such a compatible tree pair exists in an arbitrary realization or metric. In particular, locating a projective centering parameter does not produce the tree inequalities automatically.

## 5. Quantitative centering-window theorem

Compute the actual moments of K about the specified target reference0:

 V=Vol K,
 g=(1/V) integral_K x dx,
 W=(1/V) integral_K x x^T dx>0,
 e^2=g^T W^-1 g,
 L^2=max_i x_i^T W^-1 x_i.

W is the RAW second moment about0, not the covariance unless g=0. Choose R>0 and a known upper bound Lbar>=L such that

 R Lbar<1,
 [5R/(1+R Lbar)^6]^2>e^2.                     (W1)

Then the unique actual centering parameter p_* is in the INTERIOR of

 E_R={p:p^T W p<=R^2}.

Proof. For p in E_R and x in K, Cauchy–Schwarz in W gives |p.x|<=R Lbar. The maximum of the convex quadratic x^T W^-1 x over K is attained at a vertex, so the bound applies to the entire body. Thus the whole closed ellipsoid is contained in D_K. On its boundary p^T W p=R^2,

 p.grad Phi(p)
 =-4V p.g+integral_0^1 p^T Hess Phi(t p) p dt
 >=-4V R e+20V R^2/(1+R Lbar)^6
 >0.

The first inequality uses p.g<=R e and f_(tp)(x)<=1+R Lbar in the positive Hessian integral. Condition(W1) is equivalent to the strict final inequality since all displayed scalar factors are nonnegative. Phi attains a minimum on the compact ellipsoid. At a boundary point its inward radial derivative is negative, so that minimum is interior. Its gradient vanishes, proving the claim and uniqueness by Section2. End of proof.

For an affine numerator h(p)=h0+b.p, the bound

 h0!=0 and h0^2>R^2 b^T W^-1 b                (W2)

preserves the sign of h throughout the CLOSED ellipsoid. This is another direct Cauchy–Schwarz estimate. With rational geometry, rational M,R,Lbar, all conditions(W1),(W2), positive-definiteness tests and true-lattice checks can be made with rational arithmetic only.

If(W2) holds for the E selected positive rows of Section4, the actual uniform body T_(p_*)K has strict110, weak000, the same true face lattice and the prescribed strict roots. If it holds for all4E nonzero rows, it preserves their entire sign vector and hence the complete original reference-zero strict census. The exact example below uses the latter stronger test and has census6/8/12, not110.

These are sufficient conditions. Failure of(W1), a sign margin, or a finite attempt to find the ellipsoid is NOT an exclusion of centering, class110, a projective chamber, or all metrics. No claim is made that the scalar estimates are optimal.

The same theorem can start at any rational projective parameter p0: first construct and UNIFORMLY REFILL the actual body T_p0 K, compute its own V,g,W about the target0, and apply the theorem to a further parameter u. The identity T_u T_p0=T_(p0+u) then identifies the resulting projectivity. This is not the substitution T_p0(g_old) for the actual centroid.

The exact root p_* need not be rational. The theorem still certifies an actual real construction. A rational approximation to it is a different exact body and must have its OWN centroid and mechanics recomputed; our source does precisely this for an explicit rational midpoint. It does not call that midpoint an exactly centered parameter.

## 6. The actual preimage-centroid coordinate and its derivative

Let Sigma(p) be the actual volume covariance of T_p K. Differentiating its real weighted moments gives

 Dg(p)=-5 Sigma(p)-g(p)g(p)^T.

Put d=1-p.g. Since

 d Phi=integral_K f_p(x)^-5 dx>0,

we have d>0. The preimage of the actual centroid is

 r(p)=T_p^-1 g(p)=g(p)/d
     =[integral_K x f_p(x)^-5 dx]/[integral_K f_p(x)^-5 dx].

It is in int K, being the barycenter of a strictly positive density on the whole full-dimensional body. It is NOT a freely chosen distribution or a uniform vertex centroid. Quotient differentiation, using (I+r p^T)g=r, yields

 Dr(p)=-(5/d)(I+r p^T) Sigma(p),
 det Dr(p)=-125 det Sigma(p)/d^4<0,
 (Dr(p))^-1=-(d/5) Sigma(p)^-1(I-g p^T).

The Jacobian is not asserted symmetric or positive definite. Its determinant and the complete matrix identity are checked against direct differentiated tetrahedral volume moments in the exact control.

The map r:D_K->int K is an analytic diffeomorphism. One may derive surjectivity and uniqueness without assuming a new theorem: for any prescribed r in int K, center the actual translated body K-r by its unique parameter q from Section2. At the original interior point0, positivity says1-q.r>0. Put p=q/(1-q.r), equivalently q=p/(1+p.r). The maps T_p on K, centered at T_p(r), and T_q on K-r differ by an invertible affine-linear factor, so actual affine covariance of the volume centroid gives g(p)=T_p(r). Uniqueness follows in the reverse direction. The nonsingular displayed derivative makes the inverse analytic.

A useful exact factorization is

 T_p(v)-g=(I-g p^T)(v-r)/(1+p.v).

This explains how the reference r in the original polytope and the actual centered image are coupled. It does not license replacing the denominator factors by independent variables or masses.

For a differentiable genuine family K(t), with g(K(0))=0 and positive covariance Sigma0, the implicit equation g(T_(p(t))K(t))=0 has a locally unique analytic solution when the shape data are analytic, and

 p'(0)=(1/5) Sigma0^-1 g_shape'(0).

This follows from D_p g=-5Sigma0 and the ordinary implicit-function theorem. It supplies an always nonsingular three-parameter centroid correction even when a single-vertex actuator has a rank-two fold. It does NOT prove that the mechanical guards survive a finite surgery or that a lattice-changing deletion can be made without crossing a mechanical wall. The centering-window estimates supply one sufficient guard-preserving bridge, not that missing global compression theorem.

## 7. Exact rational actual-body control

The source input is the actual box

 K=[-1,101/100] x [-1,1] x [-1,1].

The eight vertices are enumerated in lexicographic product order:
0=(-1,-1,-1),1=(-1,-1,1),2=(-1,1,-1),3=(-1,1,1),
4=(101/100,-1,-1),5=(101/100,-1,1),6=(101/100,1,-1),7=(101/100,1,1).

The six cyclic true facets are
(0,1,3,2),(4,6,7,5),(0,4,5,1),(2,3,7,6),(0,2,6,4),(1,5,7,3).
The full true f-vector is8/12/6, C24. The source independently enumerates supporting planes from every vertex triple and matches exactly these maximal facet sets, checks every strict support and convex cycle, every edge having exactly two incident facets, vertex degrees and Euler2. Facet integration diagonals are never counted as edges.

The one actual reciprocal metric is

 M=[[2,1/4,1/5],[1/4,3/2,1/7],[1/5,1/7,1]], N=M^-1.

The exact volume and moments are

 V=201/25,
 g=(1/200,0,0),
 W=diag(3367/10000,1/3,1/3),
 e^2=1/13468,
 L^2=30403/3367.

Choose R=1/400, Lbar=301/100. The exact positive outward squared gap in(W1) is

16949054261754399667014529963547413777360017741369576399 /
247225337397251745284648310450943431246515281059234545058268.

All48 primitive values at the specified reference0 are negative. Their minimum squared sign gap in(W2) is

1217208564813686231922099 /
7001737688463612358700800.

Thus the WHOLE closed ellipsoid preserves every primitive sign and the unique actual centering parameter lies strictly inside it. Its actual image has strict(S,U,H)=(6,8,12), no physical weak point and all48 primitives nonzero. This is a nonwinning theorem control, not a candidate for110.

Reflection symmetry in y and z and uniqueness force p_*=(t_*,0,0). Direct one-dimensional integration of J_x gives, for a=1,b=101/100,

 J_x(t)=[(1-4at)/(1-at)^4-(1+4bt)/(1+bt)^4]/(3t^2).

After multiplying the positive denominators, the numerator is

 (1-4t)(1+(101/100)t)^4-(1+(101/25)t)(1-t)^4
 =-(603/100000000)t^2[1360268t^3+47133t^2+6733200t-20000].

The apparent t=0 factor is from the integral formula, not a centering root; indeed J_x(0)=Vg_x=201/5000>0. The unique actual centering root in D_K satisfies

1360268t^3+47133t^2+6733200t-20000=0.

The cubic is irreducible modulo17: its leading coefficient is nonzero and it has no root in F_17. It therefore has no rational root over Q. The actual centering parameter is genuinely irrational. Ninety exact bisections starting from[0,1/100] isolate it in

[73540788560144319706388073/24758800785707605497982484480,
 183851971400360799265970183/61897001964269013744956211200].

The source takes the exact rational midpoint of this interval, constructs the separate rational image, recomputes its OWN true uniform centroid from positive tetrahedral moments, and obtains strict6/8/12, weak000 and all48 nonzero primitives. Its own centroid is not claimed to be exactly0.

## 8. Actual derivative and wrong-reference countercontrols

At the exact three-parameter value p=(1/50,-1/100,1/150), the source constructs the full actual projective body. It differentiates the determinant volumes and first moments of its actual positive origin-fan tetrahedra in each parameter direction, without numerical finite differences. It verifies dPhi/dp_k=-4Phi g_k, the full Dg identity, the full Dr identity and det Dr=-125detSigma/d^4. It also checks all48 affine-in-p primal/polar row identities against the direct actual transformed geometric values with the SAME M and N. The complete rational matrices, centroids and determinants are reproduced in window.json.

At p=(3/4,0,0), the actual body still has8/12/6 and the same M,N. Its exact volume and own centroid are

 Vol=39415913472/347428927,
 g=(-360337624/134626609,0,0).

Its strict census about the fixed zero reference is(6,7,11), whereas the OWN-volume-centroid census is(5,6,9). In both tests all48 primitives are nonzero and there are no physical weak points. The true own stable facets are0,2,3,4,5 and the true own unstable vertices are0,1,2,3,4,7. The full feature lists and every sign are in the exact output.

This is a concrete countercontrol to interpreting the affine rows as own-centroid rows for an arbitrary projective parameter. It does not contradict the window theorem, which first proves that the centering root lies inside its guarded region. It is not a110 construction or an exclusion of one.

## 9. Complete recovery and precise source identity

The CANONICAL part1 of this two-part capsule is the complete literal source material

 [internal-source-reference]
 PROJECTIVE_CENTERING_WINDOW_V1 Recovery capsule part1of2 VERIFIED LITERAL projective_window.py.txt

Save its exact UTF-8 text as projective_window.py. Its full byte count and SHA-256 are

12348 bytes
e7d6be72dc160cfd9022cf2c3f7be8b2f7b969b22df9babb5e7aa7a4b2b0fbd4.

This proof is part2. Its own immutable receipt supplies its exact material ID, byte count and SHA-256. The two complete materials are the whole recovery capsule; no originating sandbox, initial-run attachment, prior worker archive or unspecified checkpoint is required. All vertices, facets, metric entries, rational radii, bounds, prime-test range,90-step bisection rule and output encoding are literal in the source.

Reconstruction:

 python projective_window.py build --output window.json

Verification:

 python projective_window.py check --input window.json

Expected terminal markers and output pin:

 PROJECTIVE_WINDOW_BUILD_OK 9028 a4898f7ebac8d4ee569bec74940a14ad79f83c10cfcddf92b316d1f78056b365
 PROJECTIVE_WINDOW_CHECK_OK 9028 a4898f7ebac8d4ee569bec74940a14ad79f83c10cfcddf92b316d1f78056b365

The reproduced window.json has9028bytes and SHA-256

a4898f7ebac8d4ee569bec74940a14ad79f83c10cfcddf92b316d1f78056b365.

Both an original build/check and a separate cold source-only build/check completed, and the two outputs were byte-identical. The environment was CPython3.13.5, assertions enabled, standard-library fractions,itertools,argparse,hashlib,json,pathlib only. No random seed, optimizer, optional dependency, floating tolerance, external data or hidden helper is needed. Exact Fraction arithmetic controls all accepted finite checks. The proof, not the finite control, establishes the general window and derivative statements.

The earlier material [internal-source-reference],11357bytes,SHAf27875d4eb6e01be3690f0a9929aef3cc6440504ca942677dd0027a1ff08bccf, is an UNEXECUTED DIFFERENT TRANSCRIPTION and is NOT part1 of the canonical capsule. It has a different output schema and is not asserted to reproduce the9028-byte output. It is preserved historically, but superseded by the complete tested literal12348-byte source above. No result is attributed to that earlier transcription, and no byte equality between the two sources is claimed.

## 10. Scientific boundary and next connection

The theorem gives a genuine own-centroid correction inside a certified physical sign chamber. It avoids the known one-vertex rank-two fold obstruction by using the universally nonsingular local projective centroid derivative, and it avoids the invalid transported-centroid substitution by locating an actual volume-potential minimum. It does not close the separate question of finding a reducing surgery whose mechanical chamber has enough room for this correction. It does not imply that every arbitrary-reference110 can be made homogeneous by a projectivity, that every centering correction preserves its equilibria, or that every family admits one suitable fixed metric.

The most useful continuation is quantitative coupling to a genuinely changed true lattice: find an actual reduced-edge raw body with a strict compatible escape certificate and a sufficiently small actual moment defect, or derive a wider controlled mechanical/centroid region than the simple raw-moment ellipsoid. Any positive example must still be certified at its own uniform centroid and preserve the actual edge/facet distinctions. All existing accepted lower-registry counts, the lower34 and the canonical upper622 remain unchanged.
