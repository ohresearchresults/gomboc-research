# material-bc036d025d06

AI research material · [Export notes](../catalog/coverage.md#text-records)

---

# H5_JOINT110_UNIFORM_METRIC_COMPACTNESS_V1

## Scientific statement and scope
This coordinator-derived result removes metric degeneration as an unbounded direction of the literal H5 proper110 search. It does NOT prove that H5 is impossible, does not exclude all E17 incidences, and does not supply an attaining construction. The accepted interval remains 34 <= C_min <= 622. The actual remaining H5 shape frontier is lambda<3/5 outside the accepted all-taper macro/reflection and tube. Bounds below hold on the whole H5 parameter domain, not only that frontier.

Let P be the actual uniformly filled H5 polytope at its actual volume centroid g, with its ten genuine vertices, seventeen true edges and nine maximal facets. Suppose one common SPD metric M makes it proper110 without additional weak equilibria. Scale M by a positive scalar so its horizontal principal block G has tr(G)=1, and write uniquely

M = [[G,Gv],[v^T G,v^T G v+eta]], G>0, eta>0.

Then all of the following necessary bounds hold:

* condition(G) < 900000; in particular lambda_min(G)>1/900001.
* Writing G=(1/2)[[1+t,u],[u,1-t]], t^2+u^2 < (899999/900001)^2.
* |v_1|<10 and |v_2|<10. The stronger component bound is v_i^2<12005/144.
* 1/360000 < eta < 8, and M_zz < 34.
* The actual covariance Sigma satisfies Sigma >= I/37500, tr(Sigma)<=3/4 and 3/80<=Sigma_zz<=1/10.
* With Sigma=[[A,b],[b^T,c]], C=A-b b^T/c, the sharper body-specific shear restriction is
  c (v+b/c)^T C^(-1) (v+b/c) < 2209/192.

These are a compact necessary metric chart with rational outer boundaries. They are NOT an all-U1 metric restriction: the lower normal-height bound and the spectral restrictions use S1 together with U1. Contracting eta in a U1 pencil generally loses S1, so it is not legitimate to discard this distinction. The cap upper bounds use U1 alone.

## Exact sources and evidence status
The literal geometry and normal-metric theorem are in completely read immutable parent minimum-0250, SHA256 2cf87f1bc07e373e4dd87a52a48d1a91b98eb48ba17601cf28e76afe3e39c233. It contains the complete h5_normal_cone.py, h5_taper_atlas.py and h5_verify_taper.py source units. The parent's all-root atlas is accepted author evidence, not independently replayed here.

The finite-height actual primal/polar theorem [internal-source-reference] was read completely, SHA256 e7daf31f7dddffac638b3bb0d7005af5613e4b2473b0979daff4357ebf5894db. It gives condition(Sigma^(1/2) M Sigma^(1/2)) < 48 for the V10/F9 joint equilibrium problem, more precisely adjacent gaps <7024915/1000000 and <6832329/1000000, whose product is 9599306095407/200000000000<48. Its proof uses the same-origin polar and actual covariance, not a separately centred polar.

The covariance source [internal-source-reference] was read completely. Its ACTUALLY RETRIEVED hash is e43bdb2b1745cf265601df70863e60face5ee25d5ebc4e36d120c8d361bed173, 11958 bytes. The finite-height source's bibliography carries a different older hash for this ID; that bibliographic hash is not used as identification of the newly read bytes. The actual source proves the outer inclusion (P-g) subset sqrt(15) E_Sigma, by exact actual apex-fan moments. No mathematical discrepancy in that inequality was found or asserted.

Cross-spoke caps use fully read [internal-source-reference], SHA256 e1102aa3d0a8d581e99aaad94ead3c50798d71cac91f834f3365338fa8643be4, and complete code [internal-source-reference], SHA256 d4c753c4f64df7da26027452e6dcb528f690255841021c854a5a642bb0a5f89b. The present proof also derives the needed cap bounds explicitly below.

## 1. Literal geometry, a common ball, and uniform covariance
Put s=1-lambda and Delta=conv((0,0),(1,0),(0,1)). The basal polygon B has vertices

(1/4,0), (1-3x/4,0), (1-p,p), (q,1-q),
(0,1-3r/4), (0,1/4), (1/16,1/16).

P=conv((s B,0),(lambda Delta,1)), with 0<x,r<1, p,q>0, p+q<1 and 0<lambda<1. True facet cycles are

(6,5,4,3,2,1,0), (8,7,0,1), (7,6,0), (1,2,8),
(9,8,2,3), (9,3,4), (4,5,7,9), (6,7,5), (7,8,9).

All such B contain the fixed triangle T with vertices (1/4,0),(0,1/4),(1/16,1/16); Delta contains T too. At physical height h, convexity and the two parallel ends give

P_h = s(1-h) B + lambda h Delta,

which contains k T, k=s(1-h)+lambda h. This k lies between h and 1-h. The triangle kT is defined by x_1+3x_2>=k/4, 3x_1+x_2>=k/4, x_1+x_2<=k/4. Consequently every P contains the fixed triangular bipyramid Q defined by the following SIX halfspaces:

4x_1+4x_2-h<=0, 4x_1+4x_2+h<=1,
-4x_1-12x_2+h<=0, -4x_1-12x_2-h<=-1,
-12x_1-4x_2+h<=0, -12x_1-4x_2-h<=-1.

Indeed each inequality is linear in k, so holding at both endpoints h and 1-h implies holding at the actual k. This argument includes parameter-boundary limits as convex bodies; such limits are not asserted to have ten distinct vertices.

Q contains the Euclidean ball of radius 1/50 centred at (1/21,1/21,1/2). At this centre the first two support slacks are 5/42 with squared normal length 33. The other four slacks are 11/42 with squared normal length 161. Both exact squared comparisons are positive:

(5/42)^2 - 33/2500 > 0,
(11/42)^2 - 161/2500 > 0.

For any unit direction e, the actual outer covariance ellipsoid gives width(P,e)<=2 sqrt(15 e^T Sigma e). The contained ball gives width(P,e)>=2/50, independently of the position of the actual centroid. Hence Sigma>=I/37500. This is NOT the incorrect claim that the common ball is centred at g.

All vertices and hence P lie in [0,1]^3. Each coordinate variance is <=1/4 (integrate (X_i-1/2)^2 and subtract the squared mean shift), so tr(Sigma)<=3/4. For the horizontal covariance block A, tr(A)<=1/2. The conditional block C=A-b b^T/c satisfies C>=I/37500: for any horizontal e, evaluate the full covariance at (e,-b^T e/c), obtaining e^T C e >= (1/37500)(|e|^2+(b^T e/c)^2). Also C<=A, so lambda_max(C)<=1/2.

## 2. Exact vertical variance, not an arbitrary density estimate
The actual basal area is a=(31-24xp-24rq)/64, in [7/64,31/64]. The horizontal section area polynomial is

A(h)=a s^2(1-h)^2+s lambda h(1-h)+(lambda^2/2)h^2.

The actual boundary-fan first and second moments independently reproduce its integrals. With D=6V=lambda+2a s^2, the normalized vertical density is a mixture of Beta(1,3), Beta(2,2), Beta(3,1), with respective nonnegative probabilities

w0=2a s^2/D, w1=s lambda/D, w2=lambda^2/D, w0+w1+w2=1.

The means are 1/4,1/2,3/4 and variances 3/80,1/20,3/80. Therefore 1/4<=g_z<=3/4 and

c-3/80 = w1/80 + [w1(w0+w2)+4w0w2]/16 >=0,
1/10-c = w1/20+(w2-w0)^2/16 >=0.

For genuine interior H5 parameters the mean lies strictly between 1/4 and 3/4. The source computes the entire actual raw second-moment matrix, not just its zz entry. In particular

6 integral_P z^2 = a s^2/5+3lambda/10+3lambda^2/10.

The variance here is the volume variance, not a vertex-weight variance or covariance of tetrahedral centroids.

## 3. Covariance regression and the sharp shear inequality
Write Sigma=[[A,b],[b^T,c]], C=A-b b^T/c and a=b/c. Apply the linear coordinate change y=x-a z. Its covariance is diag(C,c). In these coordinates the metric has horizontal block G, shear w=v+a, and the same normal Schur parameter eta. Whitening by diag(C^(-1/2),c^(-1/2)) gives a metric orthogonally similar to H=Sigma^(1/2) M Sigma^(1/2):

H'=[[J,J u],[u^T J,u^T J u+c eta]],
J=C^(1/2) G C^(1/2), u=sqrt(c) C^(-1/2)w.

To see that the eigenvalues really are the same, put L=[[I,a],[0,1]], T=L diag(C^(1/2),sqrt(c)). Then TT^T=Sigma, so T=Sigma^(1/2)O with O orthogonal, and H'=T^T M T=O^T H O. No physical metric is reset to identity.

For any SPD block matrix [[J,J u],[u^T J,d]] of condition less than kappa, the following sharp universal bound holds:

|u|^2 < (kappa-1)^2/(4kappa).

When u is nonzero, compress to the span of (u/|u|,0) and (0,1). Its matrix is [[a,a|u|],[a|u|,d]], with condition no greater than the full matrix. Put t=d/a. The determinant/trace criterion gives

|u|^2 < t-kappa(1+t)^2/(kappa+1)^2
 = (kappa-1)^2/(4kappa)
   - kappa/(kappa+1)^2 [t-(kappa^2+1)/(2kappa)]^2.

The strict inequality follows from the strict condition bound. If u=0 the conclusion is immediate. At kappa=48 this proves the stated ellipsoid with 2209/192.

For any horizontal e, Cauchy-Schwarz now yields

sqrt(c)|e^T v| <= |e^T b|/sqrt(c)+sqrt(2209/192) sqrt(e^T C e)
                 < sqrt(2401/192) sqrt(e^T A e).

Equivalently c(e^T v)^2 < (2401/192)e^T A e. With a coordinate e, A_ii<=1/4 and c>=3/80 give v_i^2<12005/144<100. This bound is uniform over all genuine H5 shapes and all joint S1/U1 metrics; it is not merely a fixed-G cap box. It remains valid when the covariance regression vector is not zero.

## 4. Tangential and normal separation from singular metrics
Scale M so tr(G)=1. The block J above has tr(J)=tr(CG)>=1/37500. Interlacing gives lambda_max(H')>=lambda_max(J)>=1/75000. The joint finite-height bound condition(H')<48 therefore gives lambda_min(H')>1/3600000. The Schur complement of J in H' is c eta, and every scalar Schur complement of an SPD matrix is at least its smallest eigenvalue (apply the inverse diagonal bound). Thus

eta > 1/(3600000 c) >= 1/360000,

using c<=1/10. Normal contraction of a U1 pencil below this value cannot preserve S1.

Also condition(J)<=condition(H')<48 and condition(C)<=18750. Congruence gives condition(G)<48*18750=900000. Trace one then gives lambda_min(G)>1/900001 and the claimed disk bound. Independently condition(M)<=condition(H)*condition(Sigma)<48*(3/4)*37500=1350000; this latter coarser constant is not substituted for the sharper G and eta bounds.

## 5. Uniform upper caps
Let gamma=g_z, horizontal a_i=x_i-g_xy and k_i=h_i-gamma. At a cross true edge i->j put sigma=h_j-h_i, c_i=-k_i sigma>0,

r_i=-a_i/k_i, d_ij=-(x_j-x_i)/sigma,
m=(r_i+d_ij)/2, rho^2=|r_i-d_ij|_G^2/4.

Direct expansion gives D_ij/c_i=rho^2-|v-m|_G^2-eta. Each layer has a strictly same-layer norm-maximal vertex. Under proper110 a nonroot such vertex must have a STRICT positive cross exit, since otherwise it supplies an additional weak rest. Hence eta<rho^2 for some directed spoke.

For a basal spoke, r_i-d_ij=[(1-gamma)x_i+gamma x_j-g_xy]/gamma; for the opposite direction its negative numerator is divided by 1-gamma. The numerator is the difference of two points in [0,1]^2, with squared norm at most 2. Since c_i>=1/4 and lambda_max(G)<tr(G)=1, rho^2<8. Therefore eta<8. The cap also gives M_zz<=|r_i|_G^2+|d_ij|_G^2<32+2=34. These upper bounds do not require S1, but their use together with the lower bounds does.

## 6. Consequence for exact joint search
The actual proper110 question on H5 may now be formulated with the five bounded shape parameters and the uniformly bounded metric coordinates (t,u,v1,v2,eta) above. Denominators in the actual moments remain positive because D>=7/32. The literal source gives D,K,L and hence Sigma=L/D-KK^T/D^2 exactly. Rational inequalities may safely use closed outer bounds to cover all strict candidates.

A stronger shape-specific spectral cut requires no square-root entries: condition(H)<48 is equivalent to existence of a positive scalar tau with

M-tau Sigma^(-1)>0, 48tau Sigma^(-1)-M>0.

The full primal/polar mechanics must still use M and its actual inverse. No independent choice of polar metric, frozen centroid, missed weak stratum, or U1-only singular contraction is licensed by this chart. The joint spectral cut can rule out U1 pencils whose entire positive-height U1 interval lies below the necessary normal floor. It does not assert that such a situation has already been proved throughout the residual H5 domain.

Metric degeneration is therefore quantitatively controlled on the entire literal H5 family. True-face degeneration and weak mechanical limits remain separate questions; compactness alone does not provide positive equilibrium margins, a finite atlas that excludes every candidate, or the requested minimum. The next useful computation is joint S1/U1 feasibility within this chart or a substantive geometric exclusion using the body-specific regression ellipsoid, rather than further unrestricted U1-only searches near eta=0.

## 7. Complete reproducible source and performed checks
The self-contained source is immutable [internal-source-reference], named h5_joint_compact.py.txt. Save its exact text as h5_joint_compact.py, 8897 bytes, SHA256 18d44bfc27e0e4830a36c071cb90da9320e65659c5db4d46e15fdcdd5ccf1e18.

It requires CPython 3.13.5 and SymPy 1.14.0, no external files, random seed, numerical solver or omitted helper. Run in an empty directory:

python -B h5_joint_compact.py

Expected terminal marker: H5_JOINT110_UNIFORM_METRIC_COMPACTNESS_V1_PASS.
Expected output h5_joint_compact_report.json: 11822 bytes, SHA256 060e2c7833af6449deb62c1e0527d4088fe3090c377d9cef249355bcce897804.

The coordinator executed this source twice with byte-identical output. Checks include the full symbolic actual boundary-fan volume, first moment and all six raw second moments; independent exact section integrations; both nonnegative mixture identities; all six strict common-ball guards; the complete-square shear identity; every rational chart constant; and three actual genuine H5 support/covariance/isotropic-metric controls. Those controls are not new all-G shape exclusions or proper110 bodies. The finite-height/covariance analytic source theorems are used as accepted premises, not claimed independently replayed or proof-assistant formalized by this algebra checker.
