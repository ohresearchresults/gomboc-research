# material-eda1a3d4be1d

AI research material · [Export notes](../catalog/coverage.md#text-records)

<!-- historical-status:start -->
> **Historical AI material.** The title and claims below reflect the AI’s assessment at the time. Claims of proof, certification or completion are not a current verification verdict.
>
> [C622](../C622/README.md) passes the supplied exact checks; C<500 remains open; Minimum’s C≥34 remains a working lower bound requiring a consolidated proof. See [verification status and source gaps](../catalog/coverage.md).
<!-- historical-status:end -->

---

# COVARIANCE_CAPPED_STRESS_CONE_V1

## Status, dependency, and purpose

Coordinator analytic result. The complete geometric input is
[internal-source-reference],
COVARIANCE_NINE_RATIO_AND_PHYSICAL_CONTAINER_V1.md,
SHA256 e43bdb2b1745cf265601df70863e60face5ee25d5ebc4e36d120c8d361bed173.
It concerns the ACTUAL uniform volume covariance Sigma>0, physical M>0,
and the SAME inverse N=M^-1. Its necessary condition for S=U=1,
including incidental weak contacts, is that the ordered eigenvalues of
A=Sigma^(1/2) M Sigma^(1/2) satisfy a1/a2<9 and a2/a3<9.

The present result identifies the EXACT convex hull of that necessary
spectral domain, computes its support function, and turns it into a
strictly larger class of arrow-stress certificates than positive
definiteness. It does not exclude a new actual body or incidence by
itself. No finite census or code-generated exclusion is claimed.
Global34<=C_min<=622 is unchanged.

General spectral convex sets and Schur-Horn orbitopes are standard.
Primary context: Raman Sanyal and James Saunderson, "Spectral Polyhedra",
Forum of Mathematics, Sigma13(2025),e30, DOI10.1017/fms.2024.62,
https://www.cambridge.org/core/journals/forum-of-mathematics-sigma/article/spectral-polyhedra/941BEFF902EB29C144B96DF8A97F2394 .
The publisher HTML was inspected. No historical novelty is claimed for
the spectral convexity machinery. The elementary three-dimensional
proof below is complete; no theorem from that paper is needed to check it.

## 1. Exact convex hull, not merely an outer spectral box

Normalize tr A=1. Let R_9 be the set of symmetric positive definite
matrices with ordered eigenvalues a1>=a2>=a3 and
a1<=9a2, a2<=9a3. Let R_9^str use strict inequalities.
Then

  conv(R_9) = D_9
            = {B=B^T:trB=1, I/91 <= B <= 81I/91}.              (1)

Here <= is the Loewner semidefinite order. Moreover

  conv(R_9^str) = {B:trB=1,I/91 < B < 81I/91}.                 (2)

Thus retaining the adjacent-ratio conditions instead of these two
matrix inequalities cannot improve ANY linear-in-metric separation
test which uses no further geometric information.

Proof. The ratio inequalities imply a3>=1/91 and a1<=81/91.
Therefore R_9 lies in D_9. In the plane b1+b2+b3=1, the coordinate
box 1/91<=bi<=81/91 has exactly the six vertices obtained by
permuting (81,9,1)/91. Indeed, a vertex fixes at least two coordinate
bounds. Two lower bounds would force the remaining coordinate89/91,
and two upper bounds are impossible. One upper and one lower bound
leave9/91. Hence this polygon is their convex hull.
Diagonalize any B in D_9. Its three eigenvalues are a convex
combination of those six permutations. In its fixed eigenbasis,
B is consequently a convex combination of orthogonal conjugates of
diag(81,9,1)/91. These conjugates belong to R_9. This proves(1).

The same argument for 1<k<9 gives

  D_k={trB=1, I/(k^2+k+1)<=B<=k^2 I/(k^2+k+1)}
       =conv{orthogonal conjugates of diag(k^2,k,1)/(k^2+k+1)}.

Every conjugate has both adjacent ratios k<9. Every B in the open
right side of(2) lies in D_k for k<9 sufficiently close to9, because
both endpoint bounds vary continuously and monotonically toward
1/91 and81/91. Conversely R_9^str lies in that open convex set.
This proves(2).

An explicit warning about this convexification: the spectrum
(8/10,18/100,2/100) is in D_9 but has middle/minimum ratio9 on the
boundary of the strict adjacent-ratio requirement. The spectrum
(8/10,185/1000,15/1000) is in the OPEN D_9 but has middle/minimum
ratio37/3>9. It is an allowed convex combination, not necessarily
a physically admissible single S1/U1 metric. Feasibility in D_9 is
not sufficient for true metric feasibility.

## 2. Exact support function

For any real symmetric Q let q1<=q2<=q3 be its eigenvalues, and
t=q1+q2+q3. Then

  min_{B in D_9} tr(BQ)
     = (81q1+9q2+q3)/91
     = (9t+72q1-8q3)/91.                                     (3)

The maximum is obtained by reversing the weights:
(q1+9q2+81q3)/91.

Proof without a trace-rearrangement theorem. Work in an eigenbasis
of Q. Only the diagonal entries bii of B enter tr(BQ).
Each diagonal lies between1/91 and81/91 and their sum is1.
The minimum of this elementary linear program occurs at a
permutation of(81,9,1)/91. Swapping two inverted weights reduces
the objective because (larger weight-smaller weight)
times(larger q-smaller q) is nonnegative. Thus assign81/91 toq1,
9/91 toq2, and1/91 toq3. That diagonal B belongs toD_9, so the
lower bound is attained. This proves(3).

For k in place of9 the corresponding formula is
(k^2 q1+k q2+q3)/(k^2+k+1).

If Q is nonzero and the minimum in(3) is nonnegative, then

  tr(BQ)>0 for EVERY B with I/91<B<81I/91,trB=1.               (4)

To see this, such B is an interior point in the trace-one affine
space. If tr(BQ)=0 while the linear functional is nonnegative
throughout D_9, it must vanish on every trace-zero tangent
direction. Hence Q=cI. Then its value at B is c=0, contrary to
Q nonzero. This treats zero support margins exactly rather than
turning strict spectral boundaries into physical candidates.

## 3. Actual-covariance form and rational semidefinite certificate

In original coordinates let Q be any symmetric stress tensor and

  Qhat=Sigma^(-1/2) Q Sigma^(-1/2),
  tau=tr(MSigma)>0,
  B=Sigma^(1/2)M Sigma^(1/2)/tau.

Then tr(MQ)=tau tr(B Qhat). Write l<=lambda_min(Qhat) and
u>=lambda_max(Qhat). These eigenvalue bounds are certified by

  Q-l Sigma >=0,                  u Sigma-Q >=0.              (5)

Let t=tr(Sigma^-1 Q). If Q is nonzero and

  9t+72l-8u >=0,                                              (6)

then tr(MQ)>0 for every actual joint S1/U1 metric, including
incidental weak contacts. If the left side is a strictly positive
number eta, the explicit closed-domain bound is
tr(MQ)>=tau eta/91.

The condition is also exact as a description of the closed dual
cone: taking l and u to be the true extreme generalized
eigenvalues makes(6) exactly(3). For strict support margin and
rational Sigma,Q, sufficiently close rational l,u suffice.
No rationality of the exact extreme eigenvalues is assumed.

The square-root-free scalar check, after multiplying the positive
detSigma, is

  9 tr(adj(Sigma) Q)+(72l-8u)detSigma >=0.                     (7)

For rational actual data, equations(5),(7) are exact rational
matrix/polynomial checks. All principal minors certify a
three-by-three PSD matrix; leading minors alone must not be used
to assert non-strict PSD. Positive definite interval matrices can
instead be checked by any correct uniform PD enclosure.

At a varying actual shape, both Q and Sigma vary. Frozen covariance,
vertex-average covariance, independently chosen cone masses, or an
uncertified approximate star-centroid cannot be substituted.
A cell certificate must bound those SAME genuine functions.

## 4. Mechanical arrow-stress consequence

For each selected true directed primal edge e=(i,j), set

  D_e(M)=x_i^T M(x_j-x_i),
  Q_e=-sym[x_i(x_j-x_i)^T].

Thus tr(MQ_e)=-D_e(M). Positive optional edge normalizing factors
can be absorbed into Q_e and its coefficient but must remain
strictly positive on the actual domain.

Choose nonnegative weights w_e, not all zero, and set
Q=sum_e w_e Q_e. If Q is nonzero and satisfies(5),(6), then the
selected arrows cannot all satisfy D_e(M)>=0 for ANY metric
having S=U=1. Indeed, those weak arrows would give tr(MQ)<=0,
contradicting(4).

If a collection of such rows covers every true rooted tree of
an actual body, then there is no joint S1/U1 physical metric.
For a sole strict unstable root, every other vertex has some
nonnegative outgoing true arrow; each such edge strictly
increases x^T Mx because its nonzero edge vector has positive
M-square. Therefore the arrows contain a true tree to the root,
including zero-arrow weak-contact cases. Complete tree coverage
is still required. A silhouette-path cover is not a full tree
cover.

IMPORTANT DIFFERENCE FROM OLD PD STENCILS:
This proves not(S=1 and U=1), or equivalently S>=2 OR U>=2.
It does NOT prove U>=2 for every unrestricted physical metric.
The spectral premise came from BOTH S1 and U1. It does not assert
H0 or physical weak000; all joint S1/U1 metrics are excluded when
complete coverage is established, so it would suffice for110.

## 5. Exact completeness for the convex relaxation

Fix the ACTUAL Sigma and a finite selected set of arrow tensors.
Let D_Sigma be the compact convex metric domain

  tr(MSigma)=1,
  91Sigma M Sigma-Sigma>=0,
  81Sigma-91Sigma M Sigma>=0.

Then the following are equivalent:

(a) No M in D_Sigma satisfies all selected weak arrows.
(b) Some nonnegative weighted stress Q has the STRICT support
    value(3), applied to Qhat, greater than zero.

One elementary separation proof is as follows. The image
Y={(tr(MQ_e))_e : M in D_Sigma} is compact and convex. The weak
arrow system asks for intersection with the closed negative
orthant. If they are disjoint, their distance is positive and
strict convex separation supplies a functional w with
inf_{y in Y} w.y > sup_{z<=0} w.z. Finiteness of the latter
supremum requires w>=0, and its value is0. Therefore Q=sumwQ_e
has strict positive support. Conversely such a Q immediately
excludes an intersection. Formula(3) evaluates that support
exactly. This is also the usual finite minimax interpretation.

Every resulting stress can be reduced to at most SIX selected
arrows. Symmetric three-by-three matrices form a six-dimensional
real vector space. In a positive combination using more than six
vectors, choose a linear dependence, change its sign so at least
one coefficient is positive, and subtract the largest possible
nonnegative multiple while preserving every coefficient>=0.
At least one positive coefficient disappears and Q is unchanged.
Iterate. This proves the six-arrow bound directly.

This completeness concerns INFEASIBILITY IN THE CLOSED CONVEX
RELAXATION. Feasibility there is not a true S1/U1 witness. A
nonzero zero-margin certificate still excludes the actual
strict-ratio family by(4), but no claim is made here that every
infeasibility at the OPEN boundary must have a strict margin.

## 6. Strict enlargement beyond PSD: formal controls, not bodies

With Sigma=I, the following symmetric tensors illustrate the
new cone exactly:

  Q=diag(-1,10,10): min tr(BQ)=19/91>0.
  Q=diag(-1,-1,100): min tr(BQ)=10/91>0.
  Q=diag(-1,-1,90): min tr(BQ)=0, but tr(BQ)>0
                  for every actual strict-ratio B.

Each Q is indefinite and cannot be used as an unrestricted-PSD
stress. The last satisfies tr(BQ)=91b33-1 in its eigenbasis;
b33>1/91 on the actual open domain. All three are purely
linear-algebraic controls. They are NOT claimed to be sums of
true-arrow tensors of a supplied actual body, nor110 examples.

## 7. Same-origin polar use and remaining coupling

For true polar edge arrows use their actual pole coordinates,
the SAME N=M^-1, and a polar stress R. Since

  A^-1=Sigma^-1/2 N Sigma^-1/2,

the corresponding transformed polar stress is
Rhat=Sigma^1/2 R Sigma^1/2. After its own positive trace
normalization, A^-1 has the same adjacent-ratio bounds, so the
same stress criterion applies with covariance preconditioner
Sigma^-1. This preconditioner is NOT the volume covariance of
the polar; the polar need not have its own centroid at0.

Separately feasible primal and polar convex relaxations do not
supply a common physical inverse. Combining both feasibility
outputs as if independent would destroy the central coupling.
Additional nonlinear geometry/common-inverse constraints remain
a genuine route beyond the exact linear-convex barrier(1),(2).

Concrete next use is to generate covariance-capped nonnegative
rows on a genuine actual shape, certify(5),(7) continuously, and
cover all required true trees. The complete general method is
preserved here. No such new executed all-tree cover is part of
this material, and no first-layer count changes.
