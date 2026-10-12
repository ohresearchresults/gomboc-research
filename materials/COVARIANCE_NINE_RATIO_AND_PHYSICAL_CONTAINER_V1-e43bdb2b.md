# material-e43bdb2b1745

AI research material

---

# COVARIANCE_NINE_RATIO_AND_PHYSICAL_CONTAINER_V1

## Status and scope

Coordinator analytic derivation. This is a universal necessary-condition and normalization theorem, not a finite exclusion, an E17 impossibility proof, or an attaining construction. The internally accepted bracket remains 34 <= C_min <= 622. No computational census or independent replay is claimed. Every covariance below is that of the actual uniformly filled three-dimensional body at its own volume centroid; vertex averages and independently assigned cone masses cannot replace it.

The elementary volume-moment proof and the mechanical proof are supplied in full. The only standard external geometric input in the slice proof is the planar Brunn-Minkowski inequality. An alternative one-line derivation of the inner bound uses the classical Berwald inequality: D. Langharst, Generalizations of Berwald's Inequality to Measures, arXiv:2210.04438v4 (24 April 2023), Corollary 1.4 and equation (1). This primary research paper was inspected in its full-form HTML at https://arxiv.org/html/2210.04438v4, specifically the displayed classical inequality. The covariance sandwich is classical in character; no claim of historical priority is made. The new use here is its explicit coupling to the SAME physical metric and inverse in the present minimum problem.

## 1. Actual covariance sandwich

Let P be a full-dimensional convex three-polytope, with uniform volume centroid 0, volume V, and

    Sigma = (1/V) integral_P x x^T dx > 0.
    E_Sigma = {x: x^T Sigma^(-1) x <= 1}.

Then

    sqrt(5/3) E_Sigma subset P subset sqrt(15) E_Sigma.             (1)

Both numerical constants are sharp for the class of homogeneous convex bodies. A centred regular tetrahedron in covariance-I position simultaneously has inradius sqrt(5/3) and circumradius sqrt(15). This sharpness does NOT imply that a body with S=U=1 can approach either equality.

### 1.1 Outer inclusion from the actual vertex fan

Fix a true vertex p. Triangulate the maximal facets not incident to p, and cone those triangles to p. These tetrahedra partition P up to boundaries; integration diagonals are not mechanical edges. Let the tetrahedron with other vertices a,b,c have its actual volume probability w_T, and set z_T=a+b+c. Expectations over T mean the actual probabilities w_T, whose sum is 1.

The simplex first moment gives E z_T=-p. Its second moment gives

    20 Sigma = E[ pp^T + aa^T+bb^T+cc^T
                    + (p+z_T)(p+z_T)^T ].

For each tetrahedron, aa^T+bb^T+cc^T >= z_T z_T^T/3. If C is the covariance of z_T under these actual probabilities, then

    E[z_T z_T^T]=pp^T+C,
    E[(p+z_T)(p+z_T)^T]=C.

Therefore 20 Sigma >= (4/3)(pp^T+C), and in particular

    Sigma >= pp^T/15.

Congruence by Sigma^(-1/2) gives p^T Sigma^(-1)p <= 15. Convexity of the ellipsoid then covers every point of P.

### 1.2 Inner inclusion from one-dimensional actual sections

Fix a unit vector n, let t=n.x and h=max_P n.x>0, and write min_P n.x=-a. A fan at a minimizing vertex has each of its three other vertex heights <=h. Its conditional tetrahedral mean is therefore <=(-a+3h)/4. The actual mean of t is 0, so a<=3h.

Put s=h-t. Its support is [0,L], where L=h+a<=4h. Let b(s) be its probability density under uniform volume. Cross-sections are convex planar sets; convexity of P and planar Brunn-Minkowski imply that sqrt(b(s)) is concave on [0,L]. Endpoint values, which do not affect integrals, can be taken by one-sided limits.

Compare b, extended by zero beyond L, with

    b0(s) = (3/(4h)) (1-s/(4h))^2,   0<=s<=4h.

Both densities have total integral 1 and first moment h. The positive set of b-b0 is an interval: on [0,L] its sign is the sign of sqrt(b) minus the affine function sqrt(3/(4h))(1-s/(4h)), and that difference is concave; outside [0,L], b-b0 is nonpositive. Let alpha,beta be the endpoints of this positive interval when the densities differ. The sign pattern is nonpositive, nonnegative, nonpositive. Thus, pointwise almost everywhere,

    (s-alpha)(s-beta)(b(s)-b0(s)) <= 0.

The zeroth and first moment differences vanish. On integration this proves

    E_b s^2 <= E_b0 s^2 = 8h^2/5.

The case of an empty positive set forces equality of the densities, and the same conclusion holds. Consequently

    n^T Sigma n = E(t^2) = E(s^2)-h^2 <= 3h^2/5.

This holds in every support direction, so the support function of P dominates sqrt(5/3) sqrt(n^T Sigma n), proving the inner inclusion in (1).

Alternative check: apply classical Berwald with dimension 3, exponents 1 and 2, and the nonnegative affine function f=h-n.x. It reads sqrt(10 E f^2)<=4 E f=4h, giving exactly the same bound. This is a statement about volume measure, not a free projected polygon with uniform area density.

## 2. Universal covariance gauge

Set

    K = sqrt(3/5) Sigma^(-1/2) P.

This is an origin-fixing invertible linear change of coordinates. It preserves actual uniform centring, the true face lattice and all equilibrium counts WHEN the metric is transported. It gives

    B subset K subset 3B,      Cov(K)=(3/5)I.                     (2)

For a physical SPD metric M on the original coordinates, the metric on K is

    M_K = (5/3) Sigma^(1/2) M Sigma^(1/2).

One must not replace this matrix by I. Positive scalar multiples are immaterial to equilibrium counts. The same-origin polar has (1/3)B subset K^circ subset B, and its physical metric is M_K^(-1), not a separately chosen matrix and not a metric determined by the polar's own centroid.

## 3. Spectral two-half lemma, including equality and weak contacts

Let Q be any convex full-dimensional three-polytope with rB subset Q subset RB, r>0. Let H>0 have eigenvalues lambda1>=lambda2>=lambda3. If

    lambda1 r^2 >= lambda2 R^2,                                 (3)

then Q has at least two STRICT unstable vertices for H. Additional weak equilibria elsewhere are irrelevant.

Proof. Let e be a unit lambda1-eigenvector. On the central plane e.x=0, x^T Hx<=lambda2 R^2. Each of the points +/-re belongs to Q. If either lies in the interior, moving it slightly farther along its ray gives energy strictly greater than lambda1 r^2. If it lies on the boundary, every supporting facet there must also support the contained ball rB there, and hence must have normal parallel to the corresponding +/-e. Because facets are maximal and true, precisely one facet is active and the point lies in its relative interior. A sufficiently small nonzero tangent displacement y stays in that facet and has

    (+/-re+y)^T H(+/-re+y)=lambda1 r^2+y^T Hy>lambda1 r^2.

Thus on each side of the central plane there is a point with energy strictly larger than every point of the plane, including when (3) is an equality. Maximize the energy on each compact half-polytope. A maximizer lies off the central plane and is a true vertex of Q. Along any sufficiently short nontrivial incident segment v+td inside that half, maximality and positive definiteness give

    2t v^T Hd+t^2 d^T Hd<=0,

so v^T Hd<0. Each is a strict unstable vertex, and the two half-spaces give distinct ones. This proves the lemma.

## 4. Adjacent ratio NINE under S=U=1

For actual P and M define the symmetric SPD covariance-weighted metric

    A = Sigma^(1/2) M Sigma^(1/2),

and let a1>=a2>=a3>0 be its eigenvalues. From (2), the two-half lemma and U(P,M)=1,

    a1/a2 < 9.                                                 (4)

Strict stable facets of P correspond to strict unstable vertices of its same-origin polar under M^(-1). Indeed, a polar vertex q_f has a strict maximum of the linear functional (M^(-1)q_f).q over the polar precisely when the primal foot

    x_f = M^(-1)q_f/(q_f^T M^(-1)q_f)

lies in the relative interior of the true facet f. Vertex edge inequalities characterize this strict linear maximum. This is exactly the strict polar radial-maximum condition. No claim that the polar is uniformly centred is needed.

Apply the geometric two-half lemma to K^circ and M_K^(-1); their radius ratio is again 3. From S(P,M)=1,

    a2/a3 < 9.                                                 (5)

In particular, if S=U=1 (even with incidental weak contacts),

    condition(A)<81.

Normalize tau=tr(A)=tr(M Sigma). Then

    tau/91 < a3 <= a2 <= a1 < 81 tau/91.                        (6)

For the lower bound, a2<9a3 and a1<81a3, so tau<91a3. For the upper bound, a2>a1/9 and a3>a1/81, so tau>91a1/81.

The exact coordinate-free linear matrix inequalities, at fixed actual Sigma, are

    91 Sigma M Sigma - tau Sigma > 0,
    81 tau Sigma - 91 Sigma M Sigma > 0.                        (7)

They follow by congruence from (6). They are necessary joint-S1/U1 conditions, not U1-only conditions, sufficient conditions, or inequalities for M in an arbitrary untransported frame. Multiplying every entry by positive powers of actual volume clears covariance denominators if a polynomial chart is desired. No square-root matrix needs to appear in that chart.

These replace the earlier maximal-tetrahedron container constants 176, 30976 and 1/31153 by 9, 81 and 1/91 IN THE NEW COVARIANCE GAUGE. The old constants and existing certificates remain valid in their own frames; one must not insert 1/91 into an unrelated frozen working-frame metric normalization.

## 5. Physical body consequences without an affine gauge

For Euclidean physical P, M=I, so A=Sigma. Thus an actual homogeneous S=U=1 body has adjacent principal variance ratios <9 and covariance condition <81. Its physical inertia tensor per unit mass is J=tr(Sigma)I-Sigma. If its ordered covariance eigenvalues are a1>=a2>=a3, then

    condition(J)=(a1+a2)/(a2+a3)
                <10a2/((10/9)a2)=9.

This is an intrinsic Euclidean necessary condition, not a statement about a freely reset metric.

Normalize P by a HOMOTHETY so that tr(Sigma)=E|X|^2=1; do not make any anisotropic coordinate change. Equations (1) and (6) give the explicit physical container

    sqrt(5/273) B subset P subset sqrt(1215/91) B.              (8)

Indeed, the squared inner radius is at least (5/3)a3>5/273, and the squared outer radius is at most 15a1<1215/91. Therefore the actual origin-centred circumradius/inradius ratio is <27. The closed radii in (8) are convenient uniform constants, not asserted optimal for S=U=1.

This gives a Euclidean-M=I compact geometric formulation using only translation to the actual centroid and scalar normalization. Unlike an arbitrary affine gauge followed by an illicit reset of M, this formulation makes no anisotropic change at all. For a fixed-pole/projective atlas where geometry and M encode separate freedoms, retain M and use (7) instead.

## 6. Relation to the first-layer compactness program

The previously accepted first-layer Hausdorff/incidence theorem can now use the smaller container (2) and the protected trace-one metric interval (1/91)I<M<(81/91)I. Alternatively it can use the physical container (8) with Euclidean M=I. The covariance-normalization equality is closed under full-dimensional Hausdorff limits because the actual first and second volume moments are continuous.

Nothing here proves effective lower bounds on nonincidence slacks, true edge lengths, facet areas, root margins, or nonroot escape margins. Incidental weak VE/EF/VF packets remain possible. The internally accepted weak-scope V>=10 and F>=9 theorems are still needed for the separate no-feature-degeneration result on the first layer. No E17 type or root orbit is removed by this normalization alone.

Concrete next use: in an actual shape cell with rigorously enclosed Sigma, impose (7) before subdividing the full physical metric domain or doing common-inverse stable/unstable feasibility. This protects all joint S1/U1 candidates from the singular boundary by explicit constants and preserves the same-metric coupling. A row-stencil failure still does not prove feasibility. Genuine weak-contact regularization and a whole first-layer contradiction remain distinct unresolved tasks.
