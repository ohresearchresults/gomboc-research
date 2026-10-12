# material-d40619accf0f

AI research material · [Export notes](../catalog/coverage.md#text-records)

---

# INTRINSIC_REFERENCE_ELLIPSOID_FINITE_HEIGHT_WINDOW_V1

## Scope
Coordinator analytic theorem, continuing the fully read finite-height source [internal-source-reference], the covariance sandwich [internal-source-reference], and the trace-floor dual [internal-source-reference]. This is not a new universal numerical bound, an all-H5 exclusion, an E17 exclusion, or an attaining construction. The internal bracket remains 34 <= C_min <= 622. Computational regional work and controls must have their own exact recovery source before promotion; they are not asserted by this analytic material.

The key distinction is between a freely chosen REFERENCE ellipsoid C and the PHYSICAL metric M. Changing C never changes the body or its physical metric. It does change the matrix in which spectral bounds are expressed. A fixed local reference C is not a frozen physical M, a frozen centroid, or a replacement of volume covariance by vertex masses.

## 1. Exact intrinsic shell
Let P be a full-dimensional convex three-polytope containing the reference origin in its interior. Write its true vertices as v_i and its true maximal facet equations as q_f dot x <= 1. Fix any symmetric positive-definite C. Define

    R_C^2 = max_i v_i^T C^(-1) v_i,
    L_C   = max_f q_f^T C q_f,
    r_C^2 = 1/L_C,
    Gamma_C = R_C^2 L_C.

These finite formulas are exact. The outer radius of C^(-1/2)P is attained at a vertex because the squared norm is convex. Its centred inradius is the minimum distance to a true supporting plane, hence 1/sqrt(L_C). Thus

    r_C B subset C^(-1/2)P subset R_C B.

The same-origin polar has the reciprocal shell, with exactly the same squared radius ratio Gamma_C. Its physical metric is the inverse of the transported primal metric; neither independent polar centring nor a polar volume covariance is used.

## 2. Finite-height spectral lemma, with nonnegative escape arrows
Let Q obey rB subset Q subset RB, and let its physical metric H have eigenvalues mu1 >= mu2 >= mu3 > 0. Suppose Q has exactly one strict unstable vertex and admits an escape tree of height h, every selected true arrow a->b satisfying a^T H(b-a) >= 0. Such a tree always exists when there is exactly one strict unstable vertex: each other vertex has a nonnegative outgoing true edge, and squared H-norm strictly increases along it because

    ||b||_H^2-||a||_H^2 = 2 a^T H(b-a)+||b-a||_H^2 > 0.

Choose a unit top eigenvector e, oriented so the root has nonnegative e coordinate. There is a vertex v on the opposite support plane with -e dot v >= r. Follow its tree path to the first intersection w with e dot x=0; if necessary, stop inside the crossing true edge. All prefix shadow inequalities remain nonnegative by linearity in the edge parameter.

In H^(1/2) coordinates prepend the orthogonal projection of H^(1/2)v onto the negative e axis. This adds one nonnegative shadow link. The resulting chain turns through at least pi/2 in at most h+1 links. If theta_j is the angle between successive nonzero chain vectors, each link gives norm_next >= norm_previous/cos(theta_j), with 0 <= theta_j < pi/2. Spherical triangle inequality and concavity of log(cos t) yield

    ||w||_H^2 >= mu1 r^2 / cos(pi/(2(h+1)))^(2(h+1)).

The right-hand exponent convention is unambiguous: the denominator is [cos(pi/(2(h+1)))] raised to 2(h+1). Fewer links only strengthen the estimate; m log cos(pi/(2m)) is increasing for m>=2. On the central plane, ||w||_H^2 <= mu2 R^2. Consequently

    mu1/mu2 <= (R/r)^2 f(h+1),
    f(m) = cos(pi/(2m))^(2m).

No strictness of the selected escape arrows was assumed, so incidental weak contacts do not evade this necessary condition.

## 3. Joint stable/unstable consequence in ANY reference frame
For P and M set H_C=C^(1/2) M C^(1/2), with eigenvalues mu1 >= mu2 >= mu3. If U(P,M)=1 and S(P,M)=1, apply the preceding lemma to C^(-1/2)P and to its same-origin polar with H_C^(-1). If primal and dual escape heights are h and k, then

    mu1/mu2 <= Gamma_C f(h+1),
    mu2/mu3 <= Gamma_C f(k+1).

Without choosing particular trees, h<=V-1 and k<=F-1, so use f(V),f(F). This applies at any interior reference; the actual homogeneous minimum problem additionally requires that the reference be the true volume centroid. No density relaxation has been made.

For V=10,F=9 retain the rational upper constants from the finite-height source:

    p0=7024915/1000000 > 9 f(10),
    q0=6832329/1000000 > 9 f(9).

A certified Gamma_C <= G gives strict adjacent upper bounds p=G*p0/9 and q=G*q0/9. For p,q>=1 put D=pq+q+1. Then

    H_C/tr(CM) >= I/D.

Using C=Sigma, where Sigma is the actual moving uniform covariance, sharpens the former universal factor9 by the actual Gamma_Sigma. Using a different or optimized C is equally legitimate ONLY with H_C. It is incorrect to substitute Gamma_C into a bound on the unchanged H_Sigma.

## 4. Scalar stress dual and local reference cells
For any true arrow i->j at the ACTUAL reference, define A_ij=sym(v_i(v_j-v_i)^T), so D_ij(M)=tr(M A_ij). For a positive weighted packet set

    Q = -sum_e w_e A_e,
    alpha = 1/(D-3),
    P = Q + alpha tr(C^(-1)Q) C,
    ell = 1/D = alpha/(1+3alpha).

Assume D>3. Write T=C^(-1/2)Q C^(-1/2) and P0=T+alpha tr(T)I. Direct inversion gives T=P0-ell tr(P0)I. Therefore

    tr(MQ) = tr[(H_C-ell tr(H_C)I) P0].

If P is positive definite and the necessary floor H_C >= ell tr(H_C)I holds, the right side is strictly positive: its first factor is positive semidefinite with strictly positive trace (1-3ell)tr(H_C), and P0 is positive definite. Thus some selected true arrow is negative. Covering every possible rooted tree by such packets excludes U=1 in this floor cone, and hence excludes joint S=U=1 whenever the intrinsic shell bound placed all hypothetical joint metrics in the cone. It is NOT an unrestricted all-SPD U>=2 theorem.

For a parameter cell, C may be the exact actual covariance at the cell MIDPOINT, held fixed only as an auxiliary ellipsoid throughout that cell. The moving body's actual centroid and its true vertices/poles remain variable. Certifying Gamma_C <= G over the whole cell then gives a valid cell-dependent metric cone. The intermediate matrix in this construction is C, not the moving Sigma(theta). No assertion about the latter's global spectral floor follows automatically.

Quantitative form in any fixed working frame: if P/sum(w_e) >= delta I, C<=R I, and tr(CM)=1, then some selected arrow obeys

    D_e(M) <= -delta (D-3)/(R D).

If additionally Sigma(theta)<=K C uniformly, then at the actual moving normalization tr(Sigma(theta)M)=1 the same bound is divided by K. This follows from tr(CM)>=1/K, not from resetting the physical metric.

## 5. Several reference ellipsoids and the remaining universal question
Every hypothetical physical jointS1U1 metric satisfies the necessary cones from ALL certified reference ellipsoids simultaneously. Their intersection is convex in M when only these trace-floor/window inequalities are retained. Certificates may therefore combine their dual stresses. This is a useful additional constraint, not a claim that the convex intersection is exactly the physical reciprocal feasibility set. No completeness or Slater claim is made here for an empty or boundary-only intersection.

The existing open branch [internal-source-reference] asks for a sharper UNIVERSAL upper bound on ||y||^2/h_K(-e)^2 for an actual uniformly filled covariance-I three-body, where e is unit, y belongs to K, and e dot y=0. The separately sharp outer/support estimates give9, but their joint value may be smaller. A regular simplex gives9/2 in natural extremal configurations; this does not prove the universal value. The intrinsic-shell theorem above does not settle that question. A primal uniform-body refinement must not be applied to the generally non-uniformly-centred polar without a separate argument.
