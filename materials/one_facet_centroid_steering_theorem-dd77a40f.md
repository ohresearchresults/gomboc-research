# material-dd77a40fd217

AI research material · [Export notes](../catalog/coverage.md#text-records)

---

# One-facet homogeneous centroid steering

## Status and purpose
This is a coordinator-derived control mechanism, not a construction of strict class110. The exact demonstration has (S,U,H)=(6,8,12), not (1,1,0). It preserves the target C=2E convention. No C<500 class110 body is claimed or promoted. The mechanism addresses the missing link between an externally prescribed center and an actual uniform-volume centroid. It does not certify that a desired equilibrium chamber is reachable within any particular figure's geometric slack. The broad archived notebook already contains the one-cut convex potential and its local positive-definite Hessian. The contributions here are a complete explicit three-intercept cap determinant, an inverse quartic, an exact rational equilibrium-preserving demonstration, and a constructive way to separate local rank from quantitative reachability.

Exact runnable source is material [internal-source-reference], one_facet_centroid_steering_source.txt, 9694 bytes, SHA-256 2526bca3cae8619885838b6dce75e1ad61cefb3779b81a2f01d73aad807ae329. This source has no external data dependency. Save its exact bytes as steering.py.

## 1. A single facet gives three independent centroid controls
Let P be a bounded full-dimensional uniform polyhedron with volume V and centroid c. Select a genuine facet F. Keep every other supporting plane fixed. Normalize the selected retained halfspace as

    1 + p dot (x-c) >= 0.

Here p is the inward plane normal divided by its positive affine value at c; p is nonzero. In taking derivatives, c in this expression is a fixed reference, equal to the actual centroid only at the base parameter. Vary all three components of p, rather than translating a plane of fixed normal. Assume a local bounded chamber in which the selected facet continues to have positive area.

The derivative of the actual centroid c(p) at the base parameter is

    J = 1/(V |p|) integral_F (x-c)(x-c)^T dA.

Proof: a perturbation dp moves the boundary in its inward-negative direction by dp dot (x-c)/|p|, thereby adding signed volume with boundary density dp dot (x-c)/|p|. Differentiate the volume and first moment and subtract c times the volume derivative. This gives the displayed expression. The sign is positive with the retained inequality used here.

J is symmetric positive definite. Indeed, for a nonzero vector z,

    z^T J z = 1/(V |p|) integral_F [z dot (x-c)]^2 dA > 0.

Equality would put the full two-dimensional facet in a plane through c. Its affine plane is instead p dot (x-c)=-1, which does not contain c. Therefore no nonzero z can give equality.

Consequently a single freely tilted and translated facet has a locally invertible, full-rank three-dimensional centroid map. This is not the same as three independent scalar truncation depths: one moving plane already has three geometric parameters. The conclusion remains valid if deleting that facet's inequality makes the fixed intersection of the other halfspaces unbounded, provided the varied polyhedra stay bounded in the local chamber; only the bounded moving facet enters the derivative.

For fixed combinatorics, it is sufficient that every vertex on the controlled facet be simple and that all nonincident support inequalities at all vertices have strict slack. Nonsimple vertices on the controlled facet can change incidences under arbitrary plane tilts; no unchanged-C assertion is made in that case.

For a triangular facet with centered vertices y1,y2,y3 and area A, the matrix is exactly

    J = A/(12 V |p|) [ (y1+y2+y3)(y1+y2+y3)^T + sum_i yi yi^T ].

With rational vertices and rational p, A/|p| is rational:

    A/|p| = |cross(y2-y1,y3-y1) dot p| / (2 p dot p).

Thus no numerical square roots are required for an exact rank certificate.

## 2. Explicit vertex-cap coordinates and determinant
Let K have volume V0 and centroid c0. Let w be a simple vertex, and let u1,u2,u3 be its independent edge vectors toward its three neighbors. Let U have these vectors as columns. A valid cut removes exactly

    T(t) = conv(w, w+t1*u1, w+t2*u2, w+t3*u3), ti>0.

Validity means the plane through the three new points separates w strictly from every other old vertex and crosses only the three incident edges. This must be checked, not inferred from the formulas. Set

    kappa = |det U|/6,
    v = kappa*t1*t2*t3,
    m = w + (t1*u1+t2*u2+t3*u3)/4,
    V = V0-v,
    c = (V0*c0-v*m)/V.

These are exact homogeneous volume and moment identities. Put B=U diag(t)/4, q(x)=sum_i [U^{-1}(x-w)]_i/ti, and alpha_i=log(ti). The retained body is on q(x)>=1, so its centroid satisfies q(c)>1. Differentiation gives

    dc/dalpha_i = -(v/V) [m-c + ti*ui/4],
    J_alpha = -(v/V) [B + (m-c) 1^T],
    det J_alpha = 4 (v/V)^3 det(B) [q(c)-1] != 0.

The determinant follows from the rank-one determinant identity and m=w+B*1. Its absolute value is

    |det J_alpha| = (3/8) v^4/V^3 [q(c)-1].

This proves full centroid rank for every valid nondegenerate simple-vertex cap, not just for a numerical fixture.

The same formula shows why rank alone is insufficient. For a cap of linear scale r, the two transverse logarithmic controls have scale approximately v*r/V, while the dominant control has scale v*|w-c|/V. Very small caps can be extremely ill-conditioned. A desired center displacement must fit actual support and equilibrium margins after applying the inverse derivative; it cannot be treated as free merely because the determinant is nonzero.

At fixed removed volume, sum_i dalpha_i=0 and

    dc = -(v/V) B dalpha.

This restricted derivative has rank two, tangent to the current cut plane. Fixed-volume one-cap control is not a full three-dimensional replacement. The original figure problem does not require fixed total volume.

## 3. An exact inverse reduces to one quartic
For a prescribed target center c*, let

    a = U^{-1}(c*-w),
    b = V0 U^{-1}(c0-c*).

A cap producing c* must have

    ti = 4(ai+bi/v),
    v^4 = 64*kappa*product_i(ai*v+bi).

Thus an inverse can be certified by a univariate quartic root, positive intercepts, 0<v<V0, and the exact separating-plane inequalities on all old vertices. Rational target data need not give rational intercepts; an algebraic-root certificate or a rational forward search is then appropriate. This statement does not assert that every target is attainable by a cap at the selected vertex.

There is at most one admissible halfspace cut of a fixed K with a given centroid. To see this, suppose P1=K intersect H1 and P2=K intersect H2 have the same centroid c. Normalize retained affine forms l1,l2 so li(c)=1, and let f=l1-l2. Then f(c)=0 and

    integral_P1 f - integral_P2 f = 0.

But f>0 on P1 minus P2 and f<0 on P2 minus P1, apart from measure-zero boundaries. If the bodies differ by positive volume the left side is strictly positive, a contradiction. Distinct proper cutting halfspaces cannot produce the same full-dimensional body. Inactive inequalities are the excluded exception.

For completeness, every c* in int(K) other than c0 is the centroid of some unique proper halfspace truncation of K, without restricting which vertices are cut. Minimize the convex function

    Phi(p) = integral_K max(0,1+p dot (x-c*)) dx.

Because a ball about c* lies in K, Phi is coercive: integration over a fixed sub-ball on the positive side of p gives a lower bound growing linearly with |p|. It is differentiable, and its gradient is the first centered moment of K intersect {1+p dot (x-c*)>=0}; the zero plane has three-dimensional measure zero. A minimizer therefore has the required centroid. If c* is not c0, the cut is active. The retained body is full-dimensional because the affine inequality has value 1 at the interior point c*. Uniqueness follows from the preceding symmetric-difference argument. This global fact does NOT preserve incidence, complexity, or equilibrium counts; the small remote-cap chamber is a much smaller admissible domain.

## 4. Strict equilibria and combinatorial cost
Suppose a simple vertex w of a strict polyhedron is not even a weak unstable equilibrium. Then there is an incident edge direction e into the body with

    (w-c0) dot e > 0.

Every normal of the newly exposed cap patch belongs to the old vertex normal cone, whose members n satisfy n dot e<=0. For a sufficiently small cut, all new patch points x and the perturbed centroid c satisfy (x-c) dot e>0. Hence x-c is not a normal to that patch: the new face, its new edges, and its new vertices have no equilibrium, including no weak boundary equilibrium. Existing equilibria lie away from this patch and persist by their strict inequalities for sufficiently small perturbations. The finite noncritical features also retain their strict exclusion witnesses. This proves an equilibrium-preserving local cap operation at a nonweak vertex. It does not say that cutting a strictly unstable vertex preserves its equilibrium type.

A simple-vertex cut changes (V_vertices,E,F) by (2,3,1), so C=2E increases by 6. The new triangular facet has three simple vertices and can thereafter serve as the three-parameter controller. Moving an already suitable existing facet within its incidence chamber costs no additional edges.

Conditional budget arithmetic: starting from an actually verified C486 body, one such cut would give C492; two would give C498. This is only bookkeeping, not certification of any archived C486 candidate as proper class110.

## 5. How this couples to a geometric construction parameter
Let d be a main geometric deformation, and p the remote control-plane parameters. To realize a desired center path c_target(d) with uniform density, solve

    c(d,p(d)) = c_target(d),
    p'(d) = [D_p c]^{-1} [c_target'(d) - partial_d c].

Local existence follows from the proved rank statement. This can turn a previously frozen-center exploration into a physically homogeneous continuation, but only as long as the controller remains an admissible supporting facet and all its local equilibrium exclusions remain strict.

If the critical face/edge/vertex geometry is disjoint from every vertex moved by the control plane, it stays exactly fixed under this control. Its contact inequalities then vary only through the true center. It is not sufficient that the facet have a different name: the entire critical feature and its relevant neighbors must be untouched.

A rigorous finite reachability test can use a parameter box around p0. With J0=D_p c(p0), certify sup_box ||I-J0^{-1}D_p c||<=eta<1 and ||J0^{-1}(c_target-c(p0))||<=(1-eta)r for a radius-r ball contained in that box. Together with support and strict-equilibrium certificates throughout the box, the contraction argument certifies an actual solution. No such quantitative controller box has yet been computed for C622 or the near-threshold B118 family in this work. Their exact source references were not resolving consistently during this context; this is a specific source dependency, not a scientific exclusion.

## 6. Exact rational demonstration
The complete script uses only Python's standard library, with fractions.Fraction for all predicates and moments. Start from the unit cube and retain

    100*x + 5*y + (10/3)*z >= 1.

This body has 10 vertices, 15 edges, 7 facets, C30, and exactly S6/U8/H12 with no additional weak equilibrium. Select its nonweak vertex w=(0,1/5,0), whose neighboring vertices are (0,1,0), (1/100,0,0), and (0,0,3/10). Use edge intercept fractions (1/10,1/8,1/6) for a second cap.

The result has 12 vertices, 18 edges, 8 facets, C36 and still exactly S6/U8/H12, no weak equilibria. Its volume is 1199879/1200000 and its centroid is

    (1919999039/3839612800,
     1439985107/2879709600,
     47999279/95990320).

The removed second volume is 1/1200000. Its logarithmic-intercept centroid Jacobian determinant is

    -2601199101/26531376313468630035953676800000.

A shared old tangent-cone exclusion witness for the new patch is e=(1/100,-1/5,0). Its minimum dot product (x-c) dot e over the three patch vertices is

    44933316403/1151883840000 > 0.

The script forms the normalized-plane second-moment Jacobian, proves positive leading principal minors by exact arithmetic, and checks the coordinate-change chain rule against the explicit cap derivative. It also verifies the inverse quartic at this target. Eight rational +/-1 percent intercept-corner fixtures retain the same equilibrium counts. Those eight tests are NOT claimed to certify the entire parameter box; local openness follows from the theorem, while a finite box requires its own bound.

## 7. Recovery and verification
Exact source input is the complete material [internal-source-reference]: steering.py, 9694 bytes, SHA-256 2526bca3cae8619885838b6dce75e1ad61cefb3779b81a2f01d73aad807ae329.
Reproduced output: result.json, 5202 bytes, SHA-256 7045e8ac518fb08b2bca9476e023d937bcaab61a6c572d7c05c6c5c68d5485ad.
Executed with CPython 3.13.5, standard library only, no external packages, network, seeds, tolerances, or nondefault numeric precision. UTF-8 text, LF endings.

Reconstruction: save the source material as steering.py with its exact terminal LF. Verification: run `python steering.py`, then `sha256sum steering.py result.json`. Expected terminal markers are EXACT_STEERING_OK, DET_LOG_J with the fraction above, PATCH_WITNESS_MIN with the fraction above, and NO_CLASS110_CLAIM. This is one exact computational implementation accompanying a first-principles proof, not an independent third-party audit.
