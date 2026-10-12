# material-4a38d3c678b4

AI research material · [Export notes](../catalog/coverage.md#text-records)

---

# H5_INTRINSIC_REFERENCE_REFLECTION_HYBRID_V1

## Scope and exact scientific change

A new general geometric-spectral implication removes the alpha^2>=gamma restriction from the seven-turn reflection theorem when a common-metric reciprocal product ceiling is available. A fixed rational reference ellipsoid, not the physical metric and not a reset covariance, yields a full five-dimensional actual-centroid H5 exclusion beyond that restriction and beyond the unchanged universal condition48 product bound.

For every genuine H5 body with

    x,r,p in [149/1000,151/1000],
    q in [449/1000,451/1000],
    lambda in [41/500,87/1000],

and also for its coordinate reflection x<->r,p<->q, every physical SPD metric M has S>=2 or U>=2. Additional physical weak equilibria are allowed in this exclusion. This is not unrestricted U>=2, not all H5, not all E17, and not an attaining construction. The global accepted bracket remains 34<=C_min<=622.

The exact computation was executed by the coordinator with CPython3.13.5 standard library. All 343 scalar polynomials have a strictly positive constant-minus-sum-of-absolute-other-coefficients bound on the entire normalized box. There are 134120 exact rational coefficients. This is a whole-region calculation, not sampling. An exact own446weak000 physical control distinguishes the new sufficient criterion from the old ones.

## Source lineage and evidence level

The complete immutable result minimum-0255, SHA256 b02e9ea175553f06a5fc27b626e52977c8baf76d50df0e70d68eff5fb913393e, is the accepted seven-turn reflection source; it was read in full before this work. Its root proofs and true-edge half-turn argument are extended below, without changing its object or incidence. The arbitrary-reference finite-height theorem is preserved in [internal-source-reference], SHA256 d40619accf0fc38f68f9155c87c3ea2f5cf8ce8c590dfa1b3477cad75cbbe100, read in full. It supplies the adjacent spectral ratios for the same physical inverse. The previous coordinator output [internal-source-reference] suggested a covariance-only hybrid but did not preserve its regional code. Its numerical regional counts are NOT adopted here. The present reference matrix, region, exact program and control are newly and completely preserved.

## General mixed-product ceiling

Let C be any fixed positive-definite reference matrix, a a nonzero primal vector, q a nonzero covector with a.q nonzero, and M positive definite. Define

    H=C^(1/2) M C^(1/2),
    chi_C(a,q)=(a^T C^-1 a)(q^T C q)/(a.q)^2-1 >=0,
    L_K(chi)=((K+1)sqrt(1+chi)+(K-1)sqrt(chi))^2/(4K).

If condition(H)<=K with K>=1, then

    (a^T M a)(q^T M^-1 q)/(a.q)^2 <= L_K(chi_C(a,q)).       (P)

Proof: put u=C^-1/2 a and v=C^1/2 q, normalize their Euclidean norms to one, and scale H so I<=H<=K I. The scalar inequality 1/t<=(K+1-t)/K on [1,K] gives H^-1<=((K+1)I-H)/K. Write A=u^T H u, B=v^T H v and s=sqrt(1-(u.v)^2). The two nonzero eigenvalues of uu^T-vv^T are +s and -s, so A-B<= (K-1)s. Therefore

    (u^T H u)(v^T H^-1 v)
    <= A(K+1-B)/K
    = ((K+1+A-B)^2-(K+1-A-B)^2)/(4K)
    <= (K+1+(K-1)s)^2/(4K).

The first squared term is positive and bounded by the displayed difference bound. Restoring the norms and dividing by (a.q)^2 gives (P). This uses the actual inverse of H and consequently the actual inverse of M, not a second independently chosen metric. L_K is nondecreasing in both K>=1 and chi>=0; for K this follows also from the nested condition-number classes and the sharp two-dimensional extremizer of the displayed inequality, or directly by writing it as a positive multiple of K+1/K plus a constant.

## General reflection-to-product lower bound

Let P=conv((B,0),(T,1)), with B,T full-dimensional planar polygons and B having n true vertices. Let g=(c,gamma) be the specified interior centre, 0<gamma<1/2; in the application g is the actual uniform-volume centroid. Let B_g,T_g be the corresponding centred subsets in three dimensions, and let q_B be the basal pole normalized by q.X<=1 on P-g. Choose 0<alpha<1, and write

    beta=gamma(1+alpha)/(1-gamma),
    kappa=alpha+beta,
    r=beta/alpha.

Assume

    alpha>=1-2gamma,
    -alpha B_g-beta T_g subset B_g,                         (R)
    q.a>-1 for every actual nonbasal pole q and every a in T_g,  (A)
    r cos(pi/n)^n<=1.                                      (T)

The conclusions that a basal strict U and a nonbasal strict S exist for every physical metric do not require alpha^2>=gamma. Here are the root arguments, to make the dependency precise.

Apply a physical linear map L with L^T L=M and rotate the two end planes horizontally. The new poles are L^-T q, so their Euclidean metric is exactly M^-1. Let h>0 be the plane separation, with base height -gamma h and top height (1-gamma)h. The map F_a(b)=-alpha b-beta a maps the base to itself and has the interior fixed point -gamma a/(1-gamma). Interior follows because a negative homothety of ratio alpha<1 preserving a full polygon cannot have its fixed point on a supporting line.

A maximal-norm basal vertex is a strict U: if its derivative toward a top vertex were nonnegative, the strict positive true edge length and kappa>=1 would give |F_a(b)|>|b|, contrary to basal maximality. Same-layer incident derivatives are strictly negative by the squared-norm identity.

R implies W: -(1-2gamma)B_g-2gamma T_g subset B_g. This follows by interpolating F_a(b) with its fixed point with coefficient (1-2gamma)/alpha. For a maximal-norm nonbasal true pole q, set mu=min_T q.a>-1, delta=1-gamma+gamma mu, u=(1-2gamma)/delta, v=gamma(1+mu)/delta. Then u,v>0,u+v=1 and z=-u q-v q_B belongs to the actual polar, on a top-vertex-dual face containing no basal pole. W proves its basal inequalities; the minimum mu proves its top inequalities. Thus |z|<=|q|. A nonnegative derivative from q to q_B would instead give |z|^2=|q|^2+2v q.(q_B-q)+v^2|q_B-q|^2>|q|^2. All other nonbasal derivatives are strictly negative by maximality. Hence q is a strict polar U, equivalently a strict nonbasal primal S.

Now assume S=U=1. Since the nonbasal S exists, the basal foot is not in the relative interior. Choose a maximum-norm top vertex a. It is not U, because a basal U already exists; hence there is a nonnegative true spoke a->b to the base. Put a=(d,0,(1-gamma)h). Its escape implies d>0 and

    b_x >= d+(1-gamma)h^2/d > d.

The basal chord on this horizontal axis contains the interior fixed point -gamma d/(1-gamma). Since the origin is not interior to the base, the whole chord is on the negative axis. R bounds that chord inside [-r d,0]. In particular b_y is nonzero.

If alpha^2>=gamma, then kappa>=r and the accepted seven-turn argument already contradicts U1. Suppose instead alpha^2<gamma, so r>kappa>=1. If the horizontal norm of F_a(b) exceeded r d, maximize horizontal norm in the opposite closed half of the base. Its maximizer lies off the chord, is a true basal vertex, has radius greater than r d>=d, and is a strict U: all same-layer derivatives are negative by local maximality, and every top derivative is bounded by rho d-rho^2-gamma h^2<0. For an edge crossing the separating chord, a nonnegative initial derivative would increase the norm up to the chord and contradict its radius bound. Thus the unique root lies in the half-plane opposite b.

Following nonnegative true escape edges from a->b to this unique U strictly increases full squared norm. After that first edge all vertices have greater norm than any top vertex, so the remainder stays basal. Stop at the first axis crossing. This is a horizontal half-turn in at most n arrows, with strictly positive first horizontal derivative. The cosine product bound gives endpoint radius strictly greater than d/cos(pi/n)^n, at least r d, contrary to the chord bound. Therefore necessarily

    |F_a(b)_horizontal| <= r d.

Because b_y is nonzero, the preceding x-coordinate escape gives the strict inequality

    kappa d + alpha(1-gamma)h^2/d < r d.

Using r-kappa=(gamma-alpha^2)/(alpha(1-gamma)), we obtain

    d^2/h^2 > alpha^2(1-gamma)^2/(gamma-alpha^2).

The physical basal pole is (0,0,-1/(gamma h)). Consequently

    (a^T M a)(q_B^T M^-1 q_B)/(a.q_B)^2
      =1+d^2/((1-gamma)^2 h^2)
      > gamma/(gamma-alpha^2).                             (Q)

This strict lower bound is necessary for joint S1/U1 at some maximum-norm top vertex. It remains strict when the spoke derivative is zero. No deletion of incidental weak contacts is used.

Combining (P) and (Q): if alpha^2<gamma and a valid common-reference condition bound K satisfies

    max over top vertices a of L_K(chi_C(a,q_B))
        <= gamma/(gamma-alpha^2),                          (HYBRID)

then S=U=1 is impossible. Equality in the ceiling is sufficient, because (Q) is strict. A region may combine the old alpha^2>=gamma alternative and this new alternative without conflating them.

## Actual-shape reference window

For the centred actual polytope and all its normalized true facet poles, put

    Gamma_C=(max_vertex v v^T C^-1 v)(max_pole q q^T C q).

In E17, joint S1/U1 and the accepted finite-height theorem imply adjacent eigenvalue ratios of H_C bounded by Gamma_C f(10) and Gamma_C f(9), where f(m)=cos(pi/(2m))^(2m). Thus

    condition(H_C) <= Gamma_C^2 f(10)f(9) < (16/27)Gamma_C^2.

The exact program verifies the elementary rational cosine majorants using pi>333/106, itself from the Machin identity with alternating rational bounds. This avoids numerical trigonometric constants. C may be fixed independently of the moving covariance; it is only a reference ellipsoid. M remains the single variable physical metric and its inverse remains unchanged.

## Full five-dimensional exact H5 certificate

The reference matrix, with arbitrary overall scale, is

    C = [[296,-103,-122],[-103,271,-112],[-122,-112,422]],
    det C = 18812782 >0.

The first two leading minors are positive as well. Use

    alpha=251/500,
    gamma < 2783/10000,
    Gamma_C < 73/10,
    chi_C(a,q_B) < 1/80 for every top vertex,
    K_*=(16/27)(73/10)^2=21316/675,
    L_*=21/2.

The exact box stated above has alpha>=1-2gamma, alpha^2<gamma, R strict, A strict, and r<3/2. The seven-turn condition follows from cos(pi/7)^7<1/2, also checked by rational bounds. To verify L_K*(1/80)<21/2 without square roots, put A=K_*+1, B=K_*-1 and s=4K_* L_*-A^2(1+1/80)-B^2/80. The exact values are

    s = 4373353279/18225000 >0,
    s^2-4A^2 B^2 (1/80)(81/80)
      =1523114610596986/207594140625 >0.

Finally

    alpha^2-(2783/10000)(1-2/21)=137/656250>0,

so 21/2<gamma/(gamma-alpha^2) everywhere in the box. This gives the joint exclusion for every actual physical metric, including those with extra weak equilibria.

The literal H5 vertices are z_i=((1-lambda)B_i,0), i=0,...,6, and z7=(0,0,1), z8=(lambda,0,1), z9=(0,lambda,1), where

    B=((1/4,0),(1-3x/4,0),(1-p,p),(q,1-q),
       (0,1-3r/4),(0,1/4),(1/16,1/16)).

The actual nine facet cycles, outward supports, all nonincident strict support inequalities and three independent incident planes at every vertex are checked on the whole box. They maintain the true V10/E17/F9 lattice. Moment integration over the literal oriented boundary derives D=6Vol and K=Dg and agrees identically with the exact closed moment formulas. The centroid moves with all five parameters; there is no freely selected mass weight or reference-centre substitution.

If V_i=D z_i-K, n_f is the unnormalized actual outward facet normal, H_f=D h_f-n_f.K and A_C=adj(C), the 90 Gamma inequalities are precisely

    (73/10) det(C) H_f^2
        -(V_i^T A_C V_i)(n_f^T C n_f)>0.

The three top angle inequalities are

    (81/80)det(C)(D-K_z)^2-C_zz V_i^T A_C V_i>0.

Together with the 147 R inequalities, 21 A inequalities, support/rank/height guards these are 343 polynomials. Each is expanded in the independent variables t_i in [-1,1] under the exact affine parametrization of the whole box. A polynomial c_0+sum c_e t^e is bounded below by c_0-sum_{e!=0}|c_e|. All 343 lower bounds are strictly positive. The source regenerates every one of the 134120 rational coefficients and all exact lower/upper bounds; no sampled vertices or floating tolerances enter the conclusion.

## Exact nonredundancy control

Take theta=(3/20,3/20,3/20,9/20,87/1000). Its actual uniform volume and centre are

    Vol=670603249/4800000000,
    g=(100218936160757/429186079360000,
       94357604044667/429186079360000,
       746258449/2682412996).

The exact maximal R-admissible alpha is 83969686434587/167045005965775, strictly between251/500 and503/1000. The limiting support is true facet1, basal vertex4, top vertex9. Its R intercept is83969686434587/429186079360000 and slope is-6681800238631/17167443174400. Thus no alpha satisfying R can satisfy alpha^2>=gamma. This control lies outside the old seven-turn sufficient class, not merely outside its particular rectangular certificates.

Also, even at the largest R-admissible alpha,

    gamma/(gamma-alpha_max^2)
      =20823621147194876211276067046347680625/
       1910173250822299650763118260794125901
      <2401/192.

For an unchanged condition48 bound, L_48(chi)>=L_48(0)=2401/192 for every reference angle chi>=0. Hence the covariance-only condition48 HYBRID test cannot close this control for any R-admissible alpha, even with an ideally aligned angle. The new intrinsic Gamma_C condition bound closes it. This is a limitation of that sufficient test, not a feasible joint metric.

With M=[[5,1,2],[1,3,-1],[2,-1,4]] and its exact inverse, the body is own446physicalweak000: S={0,1,5,6}, U={1,2,4,8}, H={(0,1),(1,2),(1,8),(2,3),(4,9),(6,7)}. All68 true-edge primal/polar primitives are nonzero. The code recovers every maximal support from all120 vertex triples, the true17 edges, and independently recomputes the same actual volume and centroid using a positive apex7 tetrahedron fan. This is a nonattaining control only.

## Complete recovery capsule and pins

The two raw source materials below, saved with the indicated .py names and their final LF, are sufficient to reconstruct both exact reports. No originating sandbox, numerical locator, old H5 source file or encoded archive is needed for reconstruction. The analytic theorem still has the explicit source lineage above.

- [internal-source-reference]: hybrid_exact_region.py,8410 bytes, SHA2564b4d8deb6b3ac50b2f001be38a95fb5da508d7df4cbf70e1bfb2c5a8541f5cbd.
- [internal-source-reference]: hybrid_exact_control.py,5883 bytes, SHA25665f6b996766c4e79ac79d7712c9dc888692654fcf8c0975fd4c2f4cd6407d109.

Reconstruction and verification commands, in a fresh directory containing just those sources:

    python -B -S hybrid_exact_region.py HYBRID_EXACT_REGION.json
    python -B -S hybrid_exact_control.py HYBRID_EXACT_CONTROL.json

Use CPython3.13.5 standard library with assertions enabled; no -O. Expected terminal markers:

    H5_TRUE_CENTROID_REFERENCE_ELLIPSOID_HYBRID_WHOLE_BOX_PASS
    H5_HYBRID_ACTUAL_CENTROID_NONDUPLICATE_CONTROL_PASS

Exact regenerated outputs:

- HYBRID_EXACT_REGION.json,71076 bytes,SHA256c88619df239e182f450441b305f56e036f94ec5568c4042c90eaf58066d23153.
- HYBRID_EXACT_CONTROL.json,11728 bytes,SHA256a872cf1c0eed4cfd03531efce3227de996db9f80d2a73c26a16da9fa3e55ec7a.

The float reference search is auxiliary and is preserved separately as a complete two-source method. Its rounded rational C is now an explicit exact input above; optimization success, its objective values and its software tolerances are not proof premises. The unresolved scientific frontier is extension beyond these R/A/spectral guards, particularly W-only geometries and the rest of the full H5 moduli, not rechecking an already accepted author atlas.
