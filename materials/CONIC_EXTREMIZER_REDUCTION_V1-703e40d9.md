# material-703e40d96d50

AI research material · [Export notes](../catalog/coverage.md#text-records)

<!-- historical-status:start -->
> **Historical AI material.** The title and claims below reflect the AI’s assessment at the time. Claims of proof, certification or completion are not a current verification verdict.
>
> [C622](../C622/README.md) passes the supplied exact checks; C<500 remains open; Minimum’s C≥34 remains a working lower bound requiring a consolidated proof. See [verification status and source gaps](../catalog/coverage.md).
<!-- historical-status:end -->

---

# Attainment and finite conic extremizers for actual centered whole-facet moments

## Scope and evidence
This is a coordinator analytical theorem, not a proof that the optimal constant is three halves and not an equilibrium exclusion. The exact planar equivalence and the normal three-halves theorem are taken from the fully read literal parent minimum-0290, SHA256 a1afff32561b16a73bf7a017e7ad3233330ac76bf67282f7cac952c02cc464a8. The first-variation formula and the already completed two moment subclasses are in [internal-source-reference]. The arguments below supply the compactness, nonsmooth boundary and finite-conic steps that that earlier material expressly left open. Its other limitations remain in force. No numerical maximization or symbolic computation is used in this proof.

Let K be a compact full-dimensional convex planar support, ell a nonzero nonnegative affine density, e a genuine entire edge, and t an inward affine coordinate with t=0 on e. Let Y be a nonconstant affine test centered at the ACTUAL ell-weighted mean. Write

    V = int_K ell,       J = int_K t ell,       I = int_K ell Y^2,
    B_j = int_e ell Y^j / |grad t|,
    R = J B_2/(V I),     alpha = J B_0/V^2.

If B2=0, R=0. The universal strong constant is the supremum of R over this class and over the test direction. The weaker positive leverage functional is L=J B1^2/(V B0 I). The assertions about GLOBAL attainment below are for R; the local variation/boundary assertions also apply to positive L. An enlargement of a limiting edge increases B2 but need not increase B1^2/B0, so no separate global-attainment theorem for L is being claimed.

## 1. A useful endpoint-mass bound
For a nonnegative section profile f on [0,H] such that f^(1/(n-1)) is concave, n>=2, with f(0)>0, put V=int f and J=int t f. Then

    J f(0)/V^2 <= n/(n+1).

Proof. Set T=nV/f(0), and g(t)=f(0)(1-t/T)^(n-1) on [0,T], zero beyond. Its mass is V. One must have H<=T: otherwise concavity puts f^(1/(n-1)) strictly above the reference declining line throughout (0,T), contradicting equality of mass. The difference of the two roots vanishes at0 and is concave on [0,H]; its value divided by t is nonincreasing. Consequently f-g has at most one sign change, from positive to negative, including its negative tail up to T. Equal mass then gives int t(f-g)<=0. Direct integration gives int t g=n V^2/((n+1)f(0)). The zero-density case is immediate.

Apply this with n=3 to the convex uniform lift

    P = {(x,z): x in K, |z|<=ell(x)/2}.

The square root of its section area is concave, by the usual section form of Brunn-Minkowski used in the planar parent. Coarea identifies f(0)=B0 and its volume/first normal moment with V,J. Thus alpha<=3/4 for every actual planar affine-density support. This auxiliary bound is not itself the desired covariance inequality.

## 2. Uniform compactness after class-preserving normalization
The lift P is symmetric in z, so its centroid has z-coordinate0 and its mixed horizontal/z covariance is0. Translate horizontally by the actual mean and apply a horizontal nonsingular linear map and an independent positive vertical scale so that the UNIFORM lift has centroid0 and covariance I3. These transformations preserve the affine-thickness form, genuine whole lateral facets and the value of R when the test is transformed accordingly. Rescale the transformed test to be a unit horizontal direction. Normalize the inward edge normal to length1; then J/V is its support distance h.

Every centered uniform convex3-body of covariance I3 satisfies

    ball(0,1/12) subset P subset ball(0,12).

Here is a direct bound, avoiding an assumed compactness theorem for the desired ratio. Markov gives uniform mass at least1/2 to P intersect ball(0,4), since E|X|^2=3. For any v in P, the half-homothetic image (v+(P intersect ball(0,4)))/2 is contained in P and has uniform mass at least1/16. If |v|>4, projection along v there is at least |v|/2-2. Its unit directional second moment is1, so 1>=(|v|/2-2)^2/16 and |v|<=12. For any unit direction with support interval [-a,b], zero mean and variance1 imply 1<=ab by integrating (X+a)(b-X)>=0. Since a,b<=12, both are at least1/12. The inner ball follows from all supporting inequalities.

The normalized bodies therefore admit a Hausdorff-convergent subsequence, with the same inner/outer bounds. This can be obtained by uniform convergence of their bounded12-Lipschitz support functions on the sphere. Volume and all bounded polynomial moments converge because the common inner ball prevents degeneration and convex boundaries have zero volume.

This limit stays in the affine-thickness class, rather than merely in the class of arbitrary convex3-bodies. Its horizontal projections K_n contain the disk of radius1/12 and lie in the disk of radius12. The affine heights ell_n are between0 and24 on K_n. Their values at0 and at the four fixed points +/-e_i/24 are bounded, so their affine coefficients have a convergent subsequence. The limiting ell is nonnegative on K=lim K_n and is nonzero; the limiting body is exactly {(x,z):x in K, |z|<=ell(x)/2}. Its uniform centroid/covariance remain0/I3.

## 3. The global strong supremum is attained
The supremum is finite: for the whole lateral facet F, the cone conv(0,F) has volume fraction alpha/3. Radial integration inside this cone contributes alpha T/5 to the covariance of P. Thus R<=5. A rectangular prism and its normal test give R=3/2, so the supremum M lies in [3/2,5].

Take a sequence approaching M and normalize it as in Section2. Pass to convergent subsequences of the bodies, unit horizontal test directions, unit inward normals and the two endpoints of their marked planar edges. Their support distances h lie in[1/12,12]. The limiting segment e0 is contained in the limiting support face, but need not exhaust it. The affine heights, tests and segment endpoints converge, hence the integrals B2 over these segments converge. If this segment had zero length or zero weighted Y^2 integral, the limiting R would be0, impossible since M>=3/2. Thus the limiting support face is an actual whole edge e of positive length. Replacing e0 by that whole edge can only increase its nonnegative integral B2. All volume, covariance and normal-mean factors have already converged. Therefore the limiting ACTUAL support K, density ell, full edge e and test achieve at least M, and hence exactly M by the definition of the supremum.

This is an attainment theorem for the strong universal problem, with possible enlargement to a genuine whole limiting facet handled explicitly. It does not assume a fixed incidence or a polygonal limit.

## 4. Local variational sign rules without a smoothness hypothesis
Fix an actual maximizer, its edge e, affine density and test direction. Set h=J/V and eta=B1/B2 for R, or eta=B0/B1 for a positive L. For a small bounded signed density-mass change delta nu of the support away from e, the exact first variation is

    delta log R = int Phi d(delta nu) + O(||delta nu||_TV^2),
    Phi(t,Y) = t/J - 1/V - Y^2/I - 2 eta Y/V,

with the analogous formula for L. The actual-centering term is essential; the complete derivation is in [internal-source-reference]. The remainder depends on finitely many bounded raw moments and positive fixed denominators, so it applies to the cap perturbations below regardless of their parametrization by distance.

(a) Every extreme point v outside e satisfies Phi(v)>=0. If Phi(v)<0, take a small cap containing v and contained in a neighborhood where Phi<0, avoiding e. Such localized caps exist at every extreme point: v is not in the compact convex hull of K outside any prescribed neighborhood, so separation supplies the required cutting halfplane. Removal increases the functional. Every nonempty cap has positive ell mass, even when ell(v)=0.

(b) A true straight boundary edge [v,w] with both endpoints outside e must lie in ell=0. Otherwise its relative interior has positive density. Along it,

    Phi((1-s)v+s w) = (1-s)Phi(v)+sPhi(w)
                         + s(1-s)(Y(v)-Y(w))^2/I.

Assume t,Y are independent. The right side is strictly positive in the edge interior if Y(v)!=Y(w). If those values agree, distinctness gives different t and hence different Phi values, so nonnegative endpoint values again yield strict positivity inside. Add a sufficiently small outward point beyond the relative interior of this one edge, keeping t>0 and ell>=0. The added thin triangle has positive first variation. Its whole base is the entire edge; no unsupported claim of a localized bump on a flat edge is used. This contradicts maximality.

Thus there are at most two non-marked positive-density edges, one incident to each endpoint of e, and at most one additional edge on the single supporting line ell=0. A straight edge here means the full maximal boundary segment, not a subdivision. Including e, the support has at most FOUR straight edges. If ell is strictly positive on K it has at most THREE.

(c) At any boundary point v outside e and outside the finitely many closed straight edges, Phi(v)=0. Such a point is extreme, so part(a) gives the lower inequality. An outward point p tending to v, with t(p)>0 and ell(p)>=0, adds mass localized near v. To justify localization, suppose added points could remain a positive distance away. A separating supporting normal for those points has a convergent subsequence; in the limit both v and a distant boundary point maximize the same normal, producing a nontrivial straight boundary segment containing v, a contradiction. If ell(v)=0 at an isolated contact, choose p on that supporting line, which still gives an outward perturbation within ell>=0. Hence Phi(v)>0 would increase the functional by adding the local cap. Equality follows, and extends by continuity to endpoints of any nonlinear arc.

## 5. Exact finite-conic reduction
If the maximizing test is dependent on t, the accepted universal normal theorem already gives R<=3/2. A hypothetical supercritical maximum M>3/2 therefore has independent coordinates(t,Y). Every nonlinear boundary point then lies on the SINGLE parabola

    t = h + (J/I)Y^2 + (2J eta/V)Y.

There are at most four remaining straight edges by Section4. Removing these from the boundary leaves at most four connected arcs, each a genuine arc of this same parabola. There is no residual Cantor-curvature or arbitrary nonsmooth boundary alternative: the pointwise cap argument gives the conic equation on every remaining point, and only finitely many straight segments remain. Degenerate or empty arcs are allowed. With strictly positive density there are at most three straight edges and three arcs.

Consequently the universal strong inequality is equivalent to checking this finite conic extremizer class, together with the already settled normal case. In particular, if a counterexample exists, a globally maximizing counterexample exists in this class. This does not yet give an exhaustive parameterized sign certificate on that class; it is not a triangle-only or quadrilateral-only reduction. The exact matching of segments, parabolic arcs, the supporting density-zero edge and the self-consistent actual moments remains the next problem.

The parabola of a supercritical extremizer is separated from the marked edge. Completing its square gives

    min_Y t_parabola = h[1-eta^2 I/V].

For R, Cauchy on the edge gives eta^2 I/V<=alpha/R; for positive L, equality eta^2 I/V=alpha/L holds. Since alpha<=3/4, any local supercritical value R>3/2, or L>3/2 respectively, has

    min_Y t_parabola > h/2 >0.

Thus a putative supercritical arc cannot directly meet t=0. Its straight connecting segments or density-zero boundary are a real geometric issue, not an ignorable endpoint limit. The earlier simple parabolic-wing tests do not cover every such connection.

## Consequence and unchanged limitations
Compactness/strong attainment and nonsmooth-to-conic reduction are now proved, replacing those specific open items in the earlier variation note. The universal constant itself, the finite conic-class sign problem, separate weak-functional attainment and any new equilibrium/C-minimum implication remain unresolved. The separate accepted bracket is still34<=Cmin<=622.
