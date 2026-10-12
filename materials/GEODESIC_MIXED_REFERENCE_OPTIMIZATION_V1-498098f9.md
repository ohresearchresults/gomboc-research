# material-498098f99b56

AI research material · [Export notes](../catalog/coverage.md#text-records)

<!-- historical-status:start -->
> **Historical AI material.** The title and claims below reflect the AI’s assessment at the time. Claims of proof, certification or completion are not a current verification verdict.
>
> [C622](../C622/README.md) passes the supplied exact checks; C<500 remains open; Minimum’s C≥34 remains a working lower bound requiring a consolidated proof. See [verification status and source gaps](../catalog/coverage.md).
<!-- historical-status:end -->

---

# Geodesic convexity of the full mixed reference objective

## Scope and relation to accepted sources
This is an analytic coordinator result. It concerns one fixed convex body P with 0 in its interior, its polar at that same origin, and an auxiliary positive definite reference C. It does not alter a physical metric M, does not recenter the polar at a fictitious mass center, and does not prove that any body has S=U=1. The underlying orthogonal-factor and hybrid mechanism are the fully read sources [internal-source-reference] (SHA 14c4a841bc3e3482a2e68b20110ccdc434ae3682bc2c5d51bfd3f00b769f93c8) and [internal-source-reference] (SHA 9558c1fd25a29027cabe1cd20b6ecd19abd6017c9330ae1200b408f231cf505f). Their caution that general Euclidean mixed-objective convexity had not been established remains correct. The new statement is geodesic convexity, not Euclidean convexity or monotonicity of an arbitrary scalar fixed-U search.

The standard matrix facts used below are also discussed in Sra and Hosseini, Conic geometric optimisation on the manifold of positive definite matrices, arXiv:1312.1039v3: the affine-invariant positive definite geodesic, joint monotonicity of its weighted geometric mean, and congruence invariance. A direct argument for the principal scalar convexity assertions is included here; the new physical application is not attributed to that paper.

## Definitions
For actual orthogonal pairs w in P, n in Ppolar, w.n=0, put p_(w,n)(C)=(w^T C^-1 w)(n^T C n), and U(C)=max p_(w,n)(C). The maximum is over the fixed compact pair set. Nonzero pairs suffice, and U(C)>0 because both bodies contain balls.

Fix marked nonzero vectors a,q with c=a.q nonzero. Put chi(C)=(a^T C^-1 a)(q^T Cq)/c^2-1 >=0 and delta(C)=asinh(sqrt(chi(C))). Let F>0 be a fixed scalar. For the physical E17 application F=f(10)f(9), f(m)=cos(pi/(2m))^(2m). Define K(C)=max(1,F U(C)^2). The maximum with 1 is a harmless mathematically explicit clamp: a condition number cannot be less than 1.

The sharp condition-number mixed-product ceiling is
L(C)=[((K+1)sqrt(1+chi)+(K-1)sqrt(chi))/(2sqrt(K))]^2.
It bounds the normalized product (a^T M a)(q^T M^-1 q)/c^2 when the transported physical metric H=C^(1/2) M C^(1/2) has condition number at most K. The question here is global optimization of this sufficient ceiling over C, not feasibility of M.

The geodesic between C0 and C1 is Ct=C0^(1/2)(C0^(-1/2) C1 C0^(-1/2))^t C0^(1/2), 0<=t<=1. Write this as C0 #_t C1.

## Theorem 1: pure factors and the marked angle
Both log U(C) and delta(C) are geodesically convex. The same log-convexity holds for the larger separate-radius product Gamma(C), obtained by dropping the orthogonality restriction.

Proof of the pure factor assertion. Diagonalize D=C0^(-1/2) C1 C0^(-1/2). For fixed n, n^T Ct n is a sum of nonnegative constants times exp(t log d_i). Its logarithm is convex by Holder's inequality. Likewise w^T Ct^-1 w is a positive exponential sum in -t log d_i. Thus log p_(w,n)(Ct) is convex for each nonzero pair. Its maximum is log U(Ct), so the maximum is convex. The same proof gives log Gamma.

For the angle, form the fixed oblique reflection J=I-2 a q^T/c. Then J^2=I. Write u=C^-1/2 a and v=C^1/2 q. In an orthonormal basis whose first vector is u/|u| and whose second vector is the component of v perpendicular to u, C^-1/2 J C^1/2 has a two-dimensional block [-1,-2s;0,1], with |s|=sqrt(chi), and is the identity on the remaining directions. The largest singular value of that block is sqrt(1+chi)+sqrt(chi). Therefore
exp(delta(C))=||C^-1/2 J C^1/2||_2,
and equivalently J C J^T <= exp(2delta(C)) C in the Loewner order. This identity includes chi=0; the reflection is then orthogonal in the C frame.

If the displayed inequality holds for C0 and C1 with factors k0 and k1, congruence invariance and joint monotonicity of the weighted geometric mean give
J(C0 #_t C1)J^T = (JC0J^T) #_t (JC1J^T)
<= (k0 C0) #_t (k1 C1)
= k0^(1-t) k1^t (C0 #_t C1).
Taking k_i=exp(2delta(C_i)) proves delta(Ct)<=(1-t)delta(C0)+t delta(C1).

## Theorem 2: global mixed optimization
The functions
B(C)=max(0, log U(C)+(log F)/2)+delta(C),
log U(C)+delta(C), L(C), and log L(C)
are geodesically convex. In fact L(C)=cosh(B(C))^2.

To see the identity, put t=(log K)/2>=0. Then (K+1)/(2sqrt K)=cosh t, (K-1)/(2sqrt K)=sinh t, sqrt(1+chi)=cosh delta, and sqrt chi=sinh delta. Thus the square root of L is cosh(t+delta). The first two convexity statements follow from Theorem 1 and closure under sums and maxima. Both cosh(B)^2 and 2log cosh(B) are convex and increasing for B>=0, which proves the rest.

All these relevant minimum problems attain a minimum modulo positive scalar multiples of C. Choose r, rho>0 with r times the unit ball contained in P and rho times the unit ball contained in Ppolar. Orthogonal eigenvectors e_min,e_max of C give the valid pair (r e_min,rho e_max). Therefore U(C)>=r^2 rho^2 cond(C). Any bounded sublevel of log U+delta or B bounds cond(C). Normalize det C=1, which is preserved along geodesics. The resulting sublevel stays uniformly positive definite and is compact. The objectives are continuous, so minima are attained. Every local minimum is global; uniqueness is not asserted.

This result does not say a Euclidean parametrization has no numerical artifacts, and numerical stationarity alone is not an exact global certificate. A true upper certificate must still cover the continuum of actual orthogonal pairs. The exact lower-certificate construction below deliberately avoids needing that upper calculation.

## Theorem 3: finite weighted-log lower certificate
Choose any finite nonzero actual orthogonal pairs (w_i,n_i), and positive weights lambda_i with sum 1. They need not be active pairs of U at the reference. The function
phi(C)=sum_i lambda_i log p_i(C)+delta(C)
is geodesically convex and is everywhere at most log U(C)+delta(C).

If all directional derivatives of phi at Cstar are nonnegative, phi has a global minimum there: along the geodesic from Cstar to any C, convexity makes the value at the endpoint at least the initial value plus its nonnegative initial right derivative. Consequently
U(C) exp(delta(C)) >= product_i p_i(Cstar)^(lambda_i)
for every positive definite C, if delta(Cstar)=0. A lower bound shared strictly by every p_i(Cstar) is therefore a strict all-reference lower bound. No exact optimizer, extremal active-pair identification, or continuum upper certificate is needed for this direction.

Here is an entirely rational stationarity test when the marked pair is aligned. Apply an origin-fixing coordinate change so a=(b0,h), with b0 in R^2 and h nonzero, and q is a nonzero multiple of e3. Scale C so C33=h^2. Every positive definite C in this scale has the unique representation
C(W,b)=[W+b b^T, h b; h b^T, h^2], W positive definite.
Then chi(C)=(b0-b)^T W^-1(b0-b). At b=b0 the first directional derivative of delta is sqrt(db^T W^-1 db), independent of the first-order variation of W.

For each pair write t=w_z/h, y=w_H-t b0, z=W^-1 y, r=n_H, nb=n.a,
A=y.z+t^2, D=r^T W r+nb^2, p=A D.
In the three independent W coordinates (W11,W12,W22), the gradient of log p is
((-z1^2 D+A r1^2)/p,
 (-2 z1 z2 D+2 A r1 r2)/p,
 (-z2^2 D+A r2^2)/p).
Its b gradient is -2t z/A+2nb r/D.

Suppose the positive weights make the sum of the three W gradients zero, and let d be the weighted sum of the b gradients. The exact sufficient condition is d^T W d<=1. Then, for every db,
d.db+sqrt(db^T W^-1 db)>=0
by the dual Cauchy inequality. The W derivative vanishes. Since this chart covers every tangent direction modulo the irrelevant scalar direction, all initial geodesic derivatives of phi are nonnegative. The previous global lower bound follows. All ingredients are rational when the body, W, and weights are rational.

At an unaligned reference chi>0, in a whitened frame the ordinary tangent gradient of delta is (1/2)sqrt((1+chi)/chi) times (qhat qhat^T-ahat ahat^T). The gradient of log p is nhat nhat^T-what what^T. Thus an exact balance of active gradients and the angle gradient gives a global minimizer for log U+delta. At alignment the angle has a norm subgradient rather than the singular displayed smooth formula. At most six active pair gradients are needed for a full three-dimensional optimality balance by the five-dimensional traceless tangent space; this does not say an arbitrary six-pair selection evaluates U at other references.

## Optional algebraic lower bounds via matrix words
For T_i=w_i n_i^T, ||C^-1/2 T_i C^1/2||_2=sqrt(p_i(C))<=sqrt U(C). The oblique reflection has norm exp(delta(C)). Hence every product word containing 2k rank-one matrices T_i and k copies of J obeys spectral radius(word)^(1/k)<=U(C)exp(delta(C)). In particular
U(C)exp(delta(C)) >= |(n_i^T J w_j)(n_j^T w_i)|.
These are reference-independent algebraic tests. They may be weaker than the weighted-log certificate; no universal sufficiency claim is made.

## Consequence and boundary
For E17, F=f(10)f(9). Any all-reference lower bound U exp(delta)>L0 with F L0^2>1 forces the best unchanged mixed ceiling to exceed (F L0^2+1)^2/(4F L0^2), since B>=log(sqrt F U)+delta. This is an obstruction to a proof template, not a construction of a physical equilibrium metric. It shows exactly when better auxiliary reference optimization cannot replace missing actual primal/polar root geometry.

The companion exact H5 computation in h5_mixed_reference_exact.py applies Theorem 3 to four true pairs at theta=(3/20,3/20,3/20,9/20,13/100) and marked top9/basal pole. Its exact recovery sources must be supplied before that computational claim is used as a reconstructible object. This analytic theorem is self-contained and does not depend on running that program.
