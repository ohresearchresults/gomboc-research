# minimum-0290

AI research report · 2026-09-27 UTC · [Export notes](../../catalog/coverage.md#text-records)

<!-- historical-status:start -->
> **Historical AI report.** The title and claims below reflect the AI’s assessment at the time. Claims of proof, certification or completion are not a current verification verdict.
>
> Minimum’s C≥34 remains a working lower bound requiring a consolidated proof. [C622](../../C622/README.md) passes the supplied exact checks. See [verification status and source gaps](../../catalog/coverage.md).
<!-- historical-status:end -->

---

# CENTERED_FACET_PLANAR_REDUCTION_AND_SHARP_FIBRE_V1

## 1. Results and exact scope

The universal centered three-halves inequality is reduced **exactly to the horizontal block of a lateral facet of an affine-thickness body over an arbitrary convex planar support**. The reduction preserves both actual mean constraints, handles all lower-dimensional localization alternatives, and has a uniform boundary-layer error. It does not assume that an extremal planar support has finitely many prescribed vertices.

There are two complementary complete inequalities.

**The entire other block is settled sharply on arbitrary planar supports.** For every nonnegative affine thickness, the lateral facet’s transverse-fibre second-moment ratio is at most

    kappa_0 = 10−5 sqrt(3) < 3/2.

A genuine algebraic 6/9/5 body attains this constant. Restricting the planar support to triangles gives only the smaller sharp constant 5/4, so a triangles-only reduction would miss this actual extremizer.

**All concave homothetic section profiles are covered in the full matrix sense.** The marked end facet satisfies alpha T≤3Sigma/2 for every concave scalar profile and every convex planar base, including arbitrary nonlinear and piecewise-linear profiles with arbitrarily many knots. The tangential coefficient improves to the sharp 5/4. A genuine rational 9/15/8 control lies outside the parent’s equal-area opposite-section hypothesis and beyond homothetic frusta.

Neither universal alpha T≤3Sigma/2 nor the weaker universal alpha c^T Sigma^(-1)c≤3/2 is proved or refuted here. What remains is one precisely specified horizontal planar inequality, not an unchecked mean constraint or an unresolved transverse-fibre block. A strict universal counterexample, if one exists, can be chosen to be a rational affine-thickness polytope with a lateral marked facet and a horizontal violating test. **There is no bound on its planar vertex count in this result.**

No moment theorem here is an all-SPD U2/S2 theorem, a full E17 exclusion, or a 110 construction. The accepted minimum bracket remains 34≤C_min≤622.

### Input authority and observed execution

Both new files were read completely through EOF, including all three source units in the coordinator material and the full literal parent in the journal. All supplied byte counts and hashes matched. The journal is 331268 bytes, SHA `8843f8977eb984c5240f7fa779f85ec58db5126fb2d30612828910bf46b11751`; coordinator material is 49723 bytes, SHA `2da1625674f6ba02f6d21c09a0d24c00228bd8f97fea7cdf541c8224f7f5b447`.

The required parent `minimum-0287` was reconstructed as a 43518-byte compact UTF-8 JSON envelope, with its required SHA

`c727d65c5ee2199479e3391cdbc57a4fec7396ce8065950aec4e6175e5e5cf8e`.

No missing exact dependency or source-identity conflict was found. The accepted opposite-section, parallelogram, and earlier E17 moment interval were not rerun or relabelled as new results.

The new exact program was executed normally, in a fresh directory containing only its source, and after decoding the inline recovery into another fresh directory. All three reports and stdout copies were byte-identical. These runs certify the stated exact algebra and actual controls; the universal reductions and profile theorem are analytic. This is not a claimed coordinator replay or proof-assistant formalization.

## 2. The two centered constants and the actual planar lift

For an actual uniformly filled convex three-body P, translated to its volume centroid, and its entire genuine facet F:q·x=1, retain

    alpha=Area(F)/(||q|| Vol(P)),
    c=E_F x, T=E_F xx^T, Sigma=E_P xx^T.

Define C_3 as the supremum of alpha E_FY²/E_PY² over all such bodies, facets, and nonzero centered linear tests Y. Define L_3 similarly with numerator alpha(E_FY)². Thus C_3 is the best full centered matrix constant and L_3 is the best centroid-leverage constant.

Now take an arbitrary compact convex planar body K, a nonnegative affine function ell not identically zero, and a genuine edge e={t=0}, where t≥0 is affine. Write

    V=integral_K ell,
    mu=ell dx/V, m=E_mu t,
    B_j=integral_e ell Y^j ds/||grad t||,
    I_2=integral_K ell Y² dx,

where Y is affine and E_muY=0. Positive-area lateral facets have B_0>0. Define C_side and L_side as the suprema, respectively, of

    m B_2/I_2,             m B_1²/(B_0 I_2).          (2.1)

These are genuine physical quantities. The uniform three-body

    P(K,ell)={(x,z):x in K, |z|≤ell(x)/2}             (2.2)

has volume V and centroid (g_mu,0). Its whole lateral facet over e has alpha=mB_0/V. For horizontal Y, its volume and facet moments are exactly those in (2.1). Its vertical mean and every mixed horizontal/vertical covariance vanish by its actual reflection symmetry.

### Theorem 1 — exact reduction of both constants

    C_3=C_side,             L_3=L_side.              (2.3)

Equivalently, for every K0≥3/2, the universal three-dimensional centered bound with constant K0 holds if and only if the corresponding planar inequality (2.1) holds on every convex planar support with every nonnegative affine density. Both side constants are at least 3/2, by a rectangular prism and the centered normal test.

Only the reverse inequality in (2.3) needs proof; the lift (2.2) gives the other direction immediately.

## 3. Retaining two mean equalities under localization

The external input is Fradelizi–Guédon, *The Extreme Points of Subsets of s-Concave Probabilities and a Geometric Localization Theorem*, DCG 31 (2004), 327–335, DOI 10.1007/s00454-003-2868-y. Theorem 3 bounds extreme support dimension by p under p constraints and s≤1/(p+1). Only the dimension-p case is asserted to be s-affine. Theorems 1–2 give the stronger one-constraint segment description. The density conversion is stated in Section 2. These distinctions, including the lower-dimensional qualification, are essential here.

Fix the original P,F and centered Y. Put

    t=1−q·x, E_Pt=1, E_PY=0, R=max_P|Y|.

Let S be the compact set of 1/3-concave probabilities nu on P with

    E_nu(t−1)≥0,          E_nuY≥0.

Take its weakly closed convex hull C and the subset

    D={nu in C:E_nu(t−1)=0 and E_nuY=0}.

**D is an exposed face of C:** the nonnegative functional E(t−1)+EY vanishes precisely when both summands vanish. The actual uniform measure belongs to D. A continuous convex functional on D has a maximum at an extreme point of D, hence at an extreme point of C. Compactness of S puts these extreme points back in S; they are also extreme in conv(S). The cited localization theorem therefore applies.

This is why both means are equalities for every selected extremal, including a lower-dimensional one. It is not a claim that merely imposing EY≥0 forces EY=0. Nor is it an application of the full-dimensional part of Theorem 3 to a lower-dimensional measure.

For dimension 2 the extremal density is a nonnegative affine ell on its arbitrary convex planar support. For dimension 1 its density psi has concave square root, but need not be square of an affine function. If t is nonconstant, EY=0 forces Y to be a scalar multiple of t−1 on that line. Realize psi as the actual normal marginal of the convex three-body with square sections of side sqrt(psi). The accepted universal normal three-halves theorem then handles this branch, without any false affine-density assertion. If t is constant, it is 1 and the small layer is empty. A Dirac has t=1,Y=0. If t,Y are dependent on a dimension-2 support, its actual lift similarly reduces the needed test to a normal one.

The universal normal bound and its scope, as opposed to the full mixed-moment claim, are explicit in the supplied update.

### A continuous layer functional for each target

For 0<epsilon≤1/4 use

    k_epsilon(t)=(2/epsilon)(1−t/epsilon)_+.

Its integral over t≥0 is 1, and its first moment is epsilon/3. For the strong target use

    Phi_epsilon(nu)=E_nu[k_epsilon Y²]−K0 E_nuY².    (3.1)

For leverage use

    Psi_epsilon(nu)=(E_nu[k_epsilon Y])²/E_nu k_epsilon
                      −K0 E_nuY²,                  (3.2)

with the quotient defined to be 0 at zero denominator. The latter is a convex quadratic perspective. It is continuous even at that boundary because its nonnegative quotient is at most R² E_nu k_epsilon. Thus both functionals admit the extreme-face argument just given. The continuous triangular kernel avoids a sign/semicontinuity shortcut with a signed boundary first moment.

### Uniform error: no fixed-needle limit assumption

Assume the appropriate planar bound (2.1) with K0≥3/2. Let nu be any possible nonconstant extremal and write p(s) for its t-marginal density, S(s)=Pr(t≥s), and nu_s for its conditional law on that tail. Denote its conditional means by m_s=E_nu_s t and y_s=E_nu_sY.

For almost every 0≤s≤epsilon, its truncated actual lift has whole facet t=s and

    p(s)(m_s−s)/S(s)≤3/4.

This is the actual three-dimensional facet-mass bound, applied after centering that truncated lift at its own centroid. The dimension-1 case uses the square-section lift described above. Levels below the support have p(s)=0 and require no facet assertion. Because m_s≥1, it follows that p(s)≤1 on 0≤s≤1/4. Hence

    1−S(s)≤s,              |y_s|≤Rs/(1−s).

Apply the assumed planar centered inequality to the tail, with centered test Y−y_s. In the one-dimensional/dependent case use the established normal bound. For the strong target this gives

    p(s) E[(Y−y_s)^2 | t=s]
       ≤ K0 S(s) Var_nu_s(Y)/(m_s−s)
       ≤ K0 E_nuY²/(1−s).

For leverage replace that conditional second moment by (E[Y|t=s]−y_s)². The same estimate holds.

Expanding the shift, using |Y|≤R, yields the uniform bound

    p(s) E[Y²|t=s]
       ≤ K0 E_nuY² + (4/3)(K0+2)R² s,              (3.3)

or, for leverage, the same bound with (E[Y|t=s])². Integrating (3.3) against k_epsilon gives error at most

    (4/9)(K0+2)R² epsilon.

For (3.2), weighted Cauchy–Schwarz first bounds its quotient by the integral of k_epsilon p(s)(E[Y|t=s])². All constants are independent of which extremal is selected and of epsilon. The layer-empty cases are already nonpositive.

The extreme-face maximum transfers the same error bound to the original actual measure. Its section area and affine moments converge to those of the whole F. Consequently

    E_P[k_epsilon Y²] -> alpha E_FY²,
    (E_P[k_epsilon Y])²/E_P k_epsilon -> alpha(E_FY)².

Letting epsilon tend to zero proves both assertions in (2.3). No mixture of different physical origins or independently assigned facet masses is used.

### Strict counterexamples can be chosen rational in this reduced class

By (2.3), a strict failure of either universal inequality implies a failure on some planar affine-density support. Approximate that support by convex polygons while retaining the marked supporting line and converging its complete marked edge. Approximate ell by rational affine functions, adding a small positive constant if needed. Actual volume, edge moments, centroid and covariance converge. Strict failure persists, and the test may also be rationally approximated.

Thus a counterexample, if present, has a rational uniform lift (2.2). Its centroid is rational and exactly computable. This is an existence/reduction statement, not a supplied counterexample or a polygon-vertex cutoff.

## 4. The remaining arbitrary-support inequality in explicit section form

In coordinates (t,y), write

    K={0≤t≤H, a(t)−b(t)≤y≤a(t)+b(t)},
    ell(t,y)=u0+u1 t+v y,
    k(t)=u0+u1t+v a(t).

The exact geometric conditions are b≥0, both b+a and b−a concave, and k≥|v|b. These retain the actual upper and lower convex-support boundaries. Let

    M0=2bk,
    M1=2b[ka+v b²/3],
    M2=2b[k(a²+b²/3)+2vab²/3].                     (4.1)

They are the actual slice integrals of ell, ell y, and ell y². Centering the tested coordinate requires integral_0^H M1=0. Put

    V=integral M0, J_t=integral t M0, I_2=integral M2.

The remaining universal matrix assertion is exactly

    J_t M2(0) ≤ (3/2) V I_2;                        (4.2)

the remaining leverage assertion is exactly

    J_t M1(0)² ≤ (3/2) V M0(0) I_2.                 (4.3)

Every independent mixed affine test can be chosen as the coordinate y; dependent tests are normal and already closed. A formal tuple of the Mj not arising from the coupled concavity/affine-density conditions is not a counterexample.

Equivalently, in the actual centered (t−m,y) frame of this planar law, the normal entry of G=(3/2)Cov−alpha T_edge is known nonnegative. If

    delta=(3/2)Var(t)−alpha m²>0,

the missing mixed condition is precisely

    (3/2)E y²−alpha E_e y²
       >= [(3/2)E(ty)+alpha m E_e y]²/delta.        (4.4)

At delta=0 the numerator must vanish and the remaining diagonal be nonnegative. The normal theorem does not supply (4.4).

## 5. Sharp transverse-fibre theorem on every affine planar support

### Theorem 2

For every actual body (2.2) and every genuine whole lateral facet over e,

    alpha E_F z²/E_P z²
       = m [integral_e ell³ ds/||grad t||]/[integral_K ell³]
       ≤ kappa_0=10−5sqrt(3).                      (5.1)

Both the true volume and whole-facet means of z are 0. The corresponding vertical block of (3/2)Sigma−alpha T is therefore strictly positive, with relative margin (3/2)−kappa_0. This theorem covers arbitrary convex planar supports, not only polygons or quadrilaterals.

### One-constraint proof and exact sharp polynomial

Scale t so m=1. On uniform area probabilities on the fixed K use the single constraint E[(t−1)ell]≥0 and functional

    epsilon^(-1) E[1_{t≤epsilon}ell³]−kappa_0 E ell³.

Theorem 2 of Fradelizi–Guédon applies with s=1/2. The relevant segment densities are affine. At a nonconstant segment put t=a+dz and, after positive endpoint normalizations,

    L(z)=1+(r−1)z,       ell(z)=ell(0)[1+(h−1)z],
    r,h≥0, 0≤z≤1.

Write

    A=integral L[1+(h−1)z]=(2hr+h+r+2)/6,
    B=integral zL[1+(h−1)z]=(3hr+h+r+1)/12,
    C=integral L[1+(h−1)z]^3
      =(4h³r+h³+3h²r+2h²+2hr+3h+r+4)/20.

The necessary endpoint inequality is B≤kappa_0 AC. Set d0=r−sqrt(3)+1. Its full exact certificate is

    120(kappa_0 AC−B)=kappa_0 {
      [d0+2h(r−sqrt(3)/2)]²
      +h²[3r²+(16+4sqrt(3))r+4]
      +h³(10r²+16r+4)+h⁴(8r²+6r+1)}.              (5.2)

Every term is nonnegative. Equality occurs exactly at h=0,r=sqrt(3)−1. Cases with zero initial density or zero ell(0) have zero boundary term and follow directly, so they are not lost by the displayed normalization.

For completeness, the layer error is uniform. Normalize the affine density endpoints to have sum 1; then rho≤2 and |rho'|≤2. Put L0=max_K ell. Along every segment 0≤ell≤L0 and |ell'|≤L0, so |(rho ell³)'|≤8L0³. The active constraint gives d=(1−a)/(B/A)≥1−epsilon. Integrating up to (epsilon−a)/d and using (5.2) bounds the functional by

    (2kappa_0+16)L0³ epsilon ≤20L0³ epsilon

for epsilon≤1/2. Diracs, zero-ell segments and layer-empty segments are nonpositive. Localization and actual coarea convergence now prove (5.1).

### A genuine sharp body and a triangles-only obstruction

For r>0 take

    P_r={0≤t≤1, |x|≤[1+(r−1)t]/2, |y|≤(1−t)/2},

with the entire bottom rectangle marked. Its six vertices are

    (−1/2,−1/2,0),(1/2,−1/2,0),(1/2,1/2,0),
    (−1/2,1/2,0),(−r/2,0,1),(r/2,0,1).

The five outward maximal cycles are

    (3,2,1,0), (0,1,5,4), (2,3,4,5), (0,4,3), (1,2,5).

The genuine lattice is 6/9/5. Put m=(r+1)/(2(r+2)). Its actual moments are

    V=(r+2)/6, g=(0,0,m), alpha=3(r+1)/(r+2)²,
    T=diag(1/12,1/12,m²),
    Sigma=diag((r³+2r²+3r+4)/(40(r+2)),
               (r+4)/(40(r+2)),
               (r²+6r+3)/(20(r+2)²)).

Its fibre ratio is 10(r+1)/[(r+2)(r+4)], attaining kappa_0 at r=sqrt(3)−1. The exact source recovers the entire algebraic hull in Q(sqrt(3)), its actual volume/covariance, every whole-facet moment and a separate positive tetrahedral fan. All three marked generalized ratios are strictly below 3/2. This is sharpness for (5.1), not a counterexample to the requested inequality and not 110.

On a triangular planar support, let a,b be the thicknesses at the marked edge’s ends and c the third thickness. Put S3=a³+a²b+ab²+b³ and H3=S3+c(a²+ab+b²)+c²(a+b)+c³. The exact fibre ratio is

    5(a+b+2c)S3/[4(a+b+c)H3] ≤5/4,

because

    (a+b+c)H3−(a+b+2c)S3
       =cab(a+b)+c²(2a²+3ab+2b²)+2c³(a+b)+c⁴ ≥0.

The bound is sharp at c=0. Since kappa_0>4/3>5/4, even this already resolved block cannot have its sharp value found by testing only triangles. No reduction to triangles or quadrilaterals is inferred for the still-open horizontal block.

## 6. Full matrix theorem for arbitrary concave homothetic profiles

### Theorem 3

Let D be any full-dimensional convex planar body with area centroid 0 and covariance S_D. Let f:[0,H]→[0,infinity) be continuous and concave, with f(0)>0 and positive interior. Let section centres be affine. The actual body

    P={ (a+bt+f(t)u,t):u in D, 0≤t≤H }

satisfies alpha T≤3Sigma/2 on its entire marked end facet t=0. After absorbing f(0) into the base scale so that f(0)=1, and removing the affine shear, let

    I2=integral f², I4=integral f⁴,
    m=(integral t f²)/I2.

Then the tangential generalized ratio is at most the sharp 5/4:

    m/I4≤5/4.                                      (6.1)

In invariant form the stronger matrix statement is

    alpha T ≤ (5/4)Sigma
       +(1/4) Sigma q q^T Sigma/(q^T Sigma q).       (6.2)

The tangential coefficient 5/4 is attained by a pyramid profile; the normal coefficient 3/2 is attained by a prism. No complete equality classification of every normal profile is needed or asserted here.

### One-crossing proof

Concavity gives f(t)≥1−t/H, hence H≤3I2. Extend f by 0 after H and compare it to

    g(t)=(1−t/(3I2))_+.

Both squared profiles have integral I2. On [0,H], f−g is concave and vanishes at 0, so f²−g² has at most one sign change, from positive to negative; the possible g-only tail has the latter sign. Therefore

    integral t f²≤integral t g²=(3/4)I2².

If c is a crossing, f²+g² is at least 2g(c)² on the positive part of f²−g² and at most that value on its negative part. This includes a crossing at H when the zero extension jumps. Consequently

    I4=integral f⁴≥integral g⁴=3I2/5.

Together these prove (6.1), strictly unless f is the linear cone profile. Actual integration gives

    Sigma=diag((I4/I2)S_D,Var(t)),
    T=diag(S_D,m²), alpha=m/I2.

The remaining normal ratio is bounded by 3/2 by the accepted universal normal theorem. This proves (6.2) and the full centered inequality, with all moments from the same section-area law f².

For the fixed-kernel completion matrix B=alpha^(-1)T^(-1)−qq^T, inversion of (6.2) gives

    B≥(4/5)Sigma^(-1)−[1+2/(15 q^T Sigma q)]qq^T.

In particular its coefficient on physical directions u with q·u=0 is 4/5. As with the parent’s curvature interpretation, this only describes a fixed released kernel when B is being interpreted as a profile Hessian; it does not authorize moving other facets independently.

### A non-frustum actual control outside the opposite-section premise

Use triangular base D=conv{(−1,−1),(1,−1),(0,2)} and

    f(t)=1+t/4,                  0≤t≤1/2,
    f(t)=7/4−5t/4,              1/2≤t≤1.

Use shear L with rows (1,0,1/3),(0,1,−2/5),(0,0,1). The nine true vertices are L(f(t)u,t), with u in the listed base order and levels (t,f)=(0,1),(1/2,9/8),(1,1/2). The complete outward cycles are

    (2,1,0),(6,7,8),
    (0,1,4,3),(1,2,5,4),(2,0,3,5),
    (3,4,7,6),(4,5,8,7),(5,3,6,8).

This is a genuine 9/15/8 body with actual

    V=175/64,
    g=(74/525,−148/875,74/175), alpha=14208/30625,
    Sigma=L diag(18943/112000,56829/112000,15447/245000)L^T.

The marked whole bottom facet has tangent ratio 303104/663005 and normal ratio 207474688/157688125, both strict. Its mass lies between 1/10 and 57/100. At the opposite centered plane q·x=−1 the raw height is 2m and the section scale is 97/140. Its area is only 9409/19600 of the marked facet area. Thus no equal-area opposite section can fit, so the parent’s opposite-section theorem does not already prove this instance. The profile is not affine and the body is not a frustum.

The exact verification recomputes every support, all 15 genuine edges, both actual moment integrals, all eight whole-facet moment matrices and the marked strict matrix gap. No equilibrium census is supplied or inferred.

## 7. Exploration and precise remaining obstruction

A fixed-knot planar-support locator was implemented directly from (4.1). It represents both concave boundaries by independent nonnegative tent-curvature coefficients and uses one actual nonnegative affine density. With five interior knots it returned maximum matrix ratio 1.4999859193237746 after 52104 calls, reaching its limit; the leverage run returned 1.499985919907031 after 45656 calls under its numerical stopping criterion. These are not exact inequalities or counterexamples.

A separate ten-parameter convex rectangular-section search returned 1.4994411563517547 after 30100 calls at its iteration limit. Three complete positive affine-quadrilateral locators returned 1.4999999999999702, 1.4999999999999836 and 1.4999999999999742 after 6060, 4680 and 5040 calls. They approached prism-like configurations. No sampled-call count is an incidence or continuum cover.

The opposing weighted-quadrilateral sectors were also tried with exact binomial-square and grouped Bernstein decompositions. Those particular certificates did not close. The original determinant polynomials still had 588 and 795 negative power coefficients; the greedy square assignments left 109 and 86 uncovered negative terms. This is a limitation of those chosen decompositions, not a geometric failure. Their complete inputs and generators are retained as optional exploratory units.

The consequential remaining question is (4.2), or the weaker (4.3), with both actual concavity constraints and integral M1=0. The transverse side block now has a strict universal gap and the two-mean localization passage is complete. Normal-only information still leaves the Schur inequality (4.4) uncontrolled. The universal full centered constant has not been assigned the value 3/2 by any calculation in this handoff.

## 8. Complete recovery and exact evidence

The complete recovery contains ten source units. The acceptance unit is standalone: it requires only CPython 3.13.5 and SymPy 1.14.0, assertions enabled, and no external data file, optimizer, saved checkpoint or source from another branch. It verifies the sharp needle sum of squares, the triangle comparison, the actual section-moment formulas, and both complete actual controls through their true hulls and two independent volume-moment integrations.

The optional numerical units use NumPy 2.3.5 and SciPy 1.17.0 with single-thread BLAS/OMP. Their complete seeds, bounds, methods, tolerances, rounding rules and stopping limits are literal. The two unchanged coordinator helpers `facet_planar_exact.py` and `search_polygons.py` retain hashes `492057af9db374aca5b83de08162b6bcbc4b37d0c3ac27c9e8d0acb28907ee1e` and `d129127df84ea6d08712bc472e2065a026b3c947482dac46722bdb6afb4233ed` and are included in full. They are optional exploration dependencies, not new theorem acceptance premises.

Save the complete block below as `recover_centered_planar_completion.py` with its final LF. Run

```sh
python -B -S recover_centered_planar_completion.py fresh
cd fresh
python -B centered_planar_completion_exact.py > centered_exact.log
```

Observed terminal markers:

```text
CENTERED_PLANAR_COMPLETION_FULL_SOURCE_RECOVERY_PASS
ACTUAL_HULLS 6/9/5 9/15/8; COMPLETE_WHOLE_FACETS 13
SHARP_FIBRE 10 - 5*sqrt(3)
REPORT 28649 6c7913d918f2461a85dddf892cdc514243a9f55b82fa252540603466d917bd44
CENTERED_FACET_PLANAR_REDUCTION_AND_SHARP_FIBRE_EXACT_PASS
```

Pins:

```text
centered_planar_completion_exact.py —10442 bytes
2bff4f39c85e36744d110c893a1b9b142eb13c5c629beb82441bad2d09bc5f16
centered_planar_completion_report.json —28649 bytes
6c7913d918f2461a85dddf892cdc514243a9f55b82fa252540603466d917bd44
centered_exact.log —216 bytes
036acc499a34056fff4e54fe05a7d955323052d06c42675538f0a3a0bdc2e02d
Decoded ten-source map —35404 bytes
499f158a8306caff0479798bbd857df7e374c320a99958a067afe72616f29599
recover_centered_planar_completion.py —17543 bytes
2e8434f3251103a893337bb83f7b884625e7adc4d102e4eec45dbcf6c0b8ee06
```

The source-only and decoded-source runs reproduced both the 28649-byte report and 216-byte stdout exactly. The report is regenerated, not an input. Its 13 facet records are supporting actual controls, not computational verification of the analytic universal reductions.

Optional discovery replay, with `OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1` set for numerical commands:

```sh
python -B planar_tent_search.py 5 29521 500 matrix
python -B planar_tent_search.py 5 29522 500 leverage
python -B rectangle_slice_search.py 2 29401 300
python -B quad_search.py 29501 400 6
python -B quad_search.py 29502 400 6
python -B quad_search.py 29503 400 6
python -B quad_analysis.py
python -B quad_sos.py
python -B quad_group.py
python -B quad_shift_group.py
```

The last four commands regenerate their complete polynomial inputs; no large saved polynomial table is necessary. Failed output from these optional searches is not an acceptance marker. Floating discovery is not promised to be byte-identical on another numerical stack.

Convenience copies supplement the inline recovery: complete source/report bundle (`centered_planar_completion_certificate.zip`), exact report (`centered_planar_completion_report.json`), and recovery source (`recover_centered_planar_completion.py`).

```python
"""Recover complete exact source and optional reproducible numerical explorations.
Exact acceptance: CPython3.13.5/SymPy1.14.0; no optimizer or data-file input.
Optional locators: NumPy2.3.5/SciPy1.17.0, one BLAS/OMP thread.
"""
from pathlib import Path
import base64,hashlib,json,sys,zlib
PAYLOAD=r"""
c-rNC36tBl(%@g=`qh?53Y19dmI7DC<H_2NGxi+urXp)q6iG?+NR%E)UE}BfzTG%TP|}Q@<lC*<+PvoxiK78D8hxPwetj{G7Ge6L
|Mi6*##xwz!Fav!VlNr{tL1tTX3;7hhkMV@YU{&`{)^A-f0tL+_gA-9ugAY!TwdLeKfb@XzPKGj!ta;&Z$Dg*FRovY@7`S8ejNYu
_SNmx_>)un9A6<6&0EaEN#bc<9BA;q@fO-{zFLIV)bqnk^H*_}tQKiayZm^_=Brq1)SO1GMYOxa^5a2sYEH9e1GMXv7RBpLrm+DK
ZMs-_SrpGSFNw1G5<2b^ZMDv#W%TIbD2SFoo2#XkhGC$s5-nKmVyG0P0PTJrYKxWcEkxmZ_;2W0lpR>NG(gM7$8^?h>|+#fHcM@t
tgw0fT}@MHI)nn=;sA{U(A!O{?VvN7m!@HY)ziMV=A*J+X+MDQ&oRgM=Xjbx&(~fyUqllvTCP_~rhSB0krM%=Yz26ec>rt@#cV9;
=U61py%g({FX<}I6Vt<TeSj`%chF;cSG#4Eyv67E?gn1de<zvVFh0k>UVQv`K^@y_nRhpz<3F!%KS1_ln5<I0K^!RYIS#_9<}X4o
*7rsqu$FC-Si7qwfMjS*zpDW@vsD7Q1}~h>Skce12LJ5=UbtTaiggLZ;5pG0GO67c5N)11q5GP@3a3;3?#38+*jZ?05ls*J-kLx!
MQx6L&8tP}SdNZO<U~y&+MX9rJ*s;zZNt*NpKJr$j?ySjGcWc--6K()8CtkVLrr%u6N>Uzi@*LPUTx8OI-x9MQZ6^i%jH9iS1=nB
Impy2XLxzWB+r1Z($gCGE9;Nxy=<5hbHZE0${h7eFH55Rm}B~)n68VOw_Yy}(@pI2X%JJjUZwDZB}-Vnp!A}4Uq<v|q2t6}4EqnH
|1hcrVWt}fjDHHt?g7><ppLktVdO-!TrFWWjAtSIX30TcuK>*{!Nr%#1|RA0uJ#-2wZ1kOtTn>oWk<YFoYLWFFlT?G*pGq`W({6=
F4mc19R^syW!0$uIGhfh(a6GIdo(g?K2Ubbl3gXas57T=Em&o`%o&K`<Is6djDs#JqzgL4%(=z0*M>5R$5ByG!Q&Rlo{=EyHJ`(+
z+^<Wm>R~LWtezbsHY1<=^qyPf(3x@%|d+<#`@GSltHtm$b|TGh-1*dR3D80&Wnvk#a!{~4P$gv^LVuS#PTH8d~0Hq2Op<MS0SwJ
*ns(wFLR@qCYc7q;Pt{_7N#@>E)@p)*K7mqQ5SFebogaNSf`!5(}p_y;=l5&KY^ETWoCh?kA{UmtQSU=m1Fcsse4NAo24%12sz6a
{#b4qD~gF@`5bUTnNhh@kEO{1EYV?{4j;tKkZF1Dc?$)poFS+9z?P+4M725aH2*<2;bm=zMf%?;r!7oFII0}cp$~k~BGi9rx1qn<
hENuSrx0Etu$6tZ1pYeTEEWJD2ysebZ7&W)3!>Ebk^rT2ywcJQ@R<l?F~G>eeN7@_69+WK&M256U&zBrcS@*&jvcS(FSu$WWhFm|
1O=<WTq#9a))!JeRMu-Wi}{Kb>y_7jV$lMqWfbdJ$#@A^gff5&{{9olt}<n^Vb;7L&^cLq45)XqqOmrDMm}JaNt9!Xme<8pbg!Vg
Z@dyrD4+{eB|6lRUlFl@VEv4Y?<^6A@I_)dk_o&9VS88m6NLZZ9YY@o;`Ko{1~-LHpw3^ABDA~@3Np4^<UY};SOHLYGzjPknQpg&
NCzn}1z2y}Ey1Rh>3m(K!QdVIG1Ii(9NgfOo~H0tyRTvueQR!O_pB|3X@E(J4jV?@wdDZ0V0>-B0866s9S*XTa-?S<!Mx6S-|VP%
9U#K8If77sZOzPC?cNv&F$+cVb@sMcMJR=%EZT-z26EDyhe6^Iu4KY0j9?OR*#TuF7GG6Dvf_xBn}sJ9*^1%sk)yB9SJ2?KI;lsq
s!r=*>cu6A`d>1;`qo;N=0!~Q2^&N71|`vgBL%WvjjG#iP8*nZLLQtxasnxGZhnAN5aJWm!Z6{*Qh*H?QJU#6QiJgM4UAElMg(!a
wq6@3;8A3h$>g2&4sule`n1r^jdi0Ik_!$EskE%~keJLF!;02iQjj<$^HgP-OXylb0MjT*vl0!Y!0qGUq_s1ehQcn6xZWu_obsa4
fa@gN?UBBbgrJz0bPRapYF1r$&0OVD^)Redq7}y1%j{!-Bd<~{%7@LLkwO|r6&VUd_Fv;Gj(db@K85%Q{9syU2do!$%(G?+n(xb{
cyB~8Q>kRs?k)8d8B3M37e#vwquD$Y-H;mTtc*Qgri8yWnCj(j#C1_@;4Rj3PZ^lWGwS;5dfPZ%$R#NECPKFSslmlDH?&z6X0YD*
jHF<_sNG@QQXSaLTbDa{3(LnfOyH;%>!GQZ=8Hux+#vEZ#yTQcB6La;Z#RyCb9xIJvlrA^K+w`TQ7HrIVT`JfER3Tk93AX0kh4D}
_w=4H{NbMxfZP?3&66-3&%MPqOvgA9_$N^(?6YzoABkA*{D*Lrnf)c()dKVg3fL#7YB4sMtfGL<$XzsB!o01vL`s)2vUvDMa@~B4
nn+6X_uO(5{v18G(nvz)Xo??}lhq>CE00>D%_}5c#c??E5IVh2HlY~Qd+Jp61g6z|9E6JnzRlSi&%OXiVBLi?rVYI}p$GxFWdlDn
2Cqt)kLFSK<!N2hY~=YRew;fVE-YXrb2F*Vt4Y;0fN*nqJ1+Xl(i?eE2bcKMWiKtg31!U&7KfiI*2KEl*u2V{gfxKEM6psp3TR^8
-BcanO!)T(h>hw2tD<98-8Br;bR~@d*G9<DwFE%wPP^JfPl$<tS<|NO*euU!=ZQ^I@3J&Za-Kkq<JzXqyg=rKd1<{eEdHYNPF1mO
;{*lBM_4)QR&S#9@REx=OuyCL4uQdPKsleu8_wN1`m4GQZGujaZYHVzb>6p0(!aa0oNuyn-tND&ySbOFg*pN{PhyExt4*Ux0;Y<$
?lYH)r}*_&K*`A@0-Y*3Xrg>7v?VT&6q5F|iRM2^(svH^s*}N;OFh%8dgi1$G2yiVuQ2hD1}PqTWFXxX66Q^V-ZiSedFR3(_;KJz
=D|Ry4iKxpVZLct?9nyh<*q0&PFEmO5VVQ;27>~Wj6G<u7F}%7z>16pL?N?zey#zeCBUkfy<DNK5ooJ8w1Nl}%al9QKol{Pj2kgI
9=T&v^QO}%4kcCvQV(QFcI1I<Rm2{&rMA-^v~7g|OI@f~4Y0B7Kp(1GQ$JWs=^5k;e37Das95a>)BIwJDny62tQ}cacfvUOa>lKZ
dC4ry=+HHH<^#dM`h&TI#&+he-Y{f}zJx@c1i0LqOOZc1@d)I&^sEU}^0<LFk!o1pbHbZ0?CRg+2-S7a=%d(Lcn2`C!z6*)n-p-5
nl>2RPdKQF_UlX9sJjBo;W{P1l3QCvGNft0YPWVJXZI?eQ?+RNB#}RaNgOVy3*5v?>j2WgKS#t=%m*({^b~k676ybkPZmziGsWRY
s$;4kd;rPqQN{vD9EQOn94jPoL0*x|Q7-*bWDH|bOt4b^LrPh>7)-*YhdzviB6G{(NK5BjL9uFxaO#VdG3I7iO8HzDJp$!Aq?OXv
$e^?n!I&lAAqiI4h{l+r&wU`}Er&`jmHBYQW=bxb6N)TTJbODj90F5zKsh4v7j*IAX_BHn$XunobtWmPyC`MhQ9g|d;{;t0ppp@X
*ap!dle9<^o?Ox(P10g%C@Ki^61U{qnuRNR>?ej%2q!Tw^NH$QY!8<B<S@&CC5ZxPdf(N8$eZbUg8bNJa<9QeVO?+9qVyS!Nk1;4
ONrUQW<)ZGV&j~x2VEXkxJFhPS)WeiWJzUZg{6iD#dE*+&<12KM~2XnzXO3Oc2FIi3FqxZ%F1!wu`&WvOepaUQ(#XF>CAwz(y+pc
Llf-x`9bjt_iQ+90+3)FK{)setkpQv&jd*wXof@KDtr!W7?EgHhXJw&<JgaS%$PY04sqy=j&+Bl4GeBMSbMp3vFCuXa(RlG6B20A
V3se#DO15KBc8%Z6xz|-qz4q86Lf8}4v^(7z2pJZe>M>mcpmbDF;iE@tUa1{8O(~sSQMXyahM>dfM<av{&Pyb$P|+`a8AZIXyt-$
y$Y5S`MEriJFwgf41$KS5}`Ux(B(Kl<;ihu#%>gT48zIU5BhX)XOr)bo-m@vl7Vn4?AKAq*@RPltT&1DN(dGMEALkC0L!piCT0u9
gQY&ip`3B-2NMNgK<>hXaMnR>)hChfP>Ov?H08@Sg~_X#Q`6*Nz<dB9F1@To2z1_Ix$xh*<ZY9@Bkx?wdjP%T4^8<1+^=|a%hWV1
>W?Tzj@xMwr^i=Hx7P%sw3}TUUmG3LYqRuruR%I(NEO3h(s%W@?qKVotb&F9&V^SCmY7)KOL!IAs9qWZsx60r;e|Yx{n*f}(IB0N
UP24@GX$Q^@C^%#43Tx;>K5bCgs~<k-yvi2g;h6;>WR50iFqKISg9FF5PL%u0&G@=AnB2=!MY+QoI8y6<bb8IzemzU%91weKus=F
6bT}viw*Lnb;Q|q6geFNI0WmYMY^N|Pc10e20(v7@L;FLig3Y>x1~%hP@)!j+pOzt^DPV*pIr7Nr>jg5CD}oNIlpx&<z&%ro+(;L
4oZ)wKnRc@lpMUa=(x$=YWL@4$r(W+b}4chLAfu4^}OlYUDB}IuH=Qc(iH`C*)#^XF;&?;kZt`uYM>s#YuF9PZjyGpVcRY4DFq0S
;o6;Mr`hgyiPM7B(RK0$^ZGyC>PR4>(odY{3pT{POH+=~vkscd5h|H1vyGovzY%l?US%l2GD0;Tl;-6?Def9S@r<7wwHR>pAljrf
XLUTeUbfiEWub5n8f-!b9BED5&o?P<w=o89p{q(;t(oE)O1lkA;uttQ2)<1FcWqBCr}j6+TMzII3+H?CP09tq=lKs|j0pb_&UV<}
e7OS6GrmZHH7<cP#=?WSB>Z8VvpV^ZR~4;is1m>;<`VTbBO;wU?PPMCSCeSUm3Zdo<HbsN2L&mw^n{=VGm5QBj5C4f1sKF$V&(Be
D^TFU5|F}oASNtYfY^;TOZ3*IoAeop8^(SSNK+13*%P_?Ujc3n87(p#Vx3GdVy4-wb|ZX&UwqxyvK8CNkbLkIEC7uB9AcVbWY77s
XsqQ0zhcP;qmLcf8hkr@%bNsrFH_z4b{>k3{UL0_(<lZ~fZ;$!B_!>OfR`xNkD^z`;~<=DX5+D}!o0i8vIN~{1!f(s{PkeBN=^+z
zoNO9R2Z6Ewd3(`QahqYMq3U9QhX1LOu1@~t39P`9b1{#D{T{lwVI?rkjrQv238Oyf(10{E^BD9Nu|{ZG<fB7N^}_RMS+|YCyUjD
>KIX03pUGjs^e^MJi=h%@Ax4+q)fRZ5!=J0u2HRg{v20~8kAiHq1@!dcs9NAOjsNTTf@en@-D%(IXPrus$(xC(@tOs>XnPj``<6#
kKg?M{{5ZSuJ`IKtygzi_3l8s{P5ey_gD8<<Nx{Q!}}{ft#_K!sFWcnb6O$XP$=c!UVZ#<dtYH3khM=ld|eGD(rvYQVr?Gog9w-<
Mpu;T|5duW`UA!^{&;bBhaH8bF&@X>G8~U7t&GP=-Q#hk&#C-#{DQn-+*YFTB!-jw9MsrLBmv+{+z^PuR0BFl*P$OxF-n8Ou@=!3
gu1r`k_gd3S`O13l*2SNAUWXw-ZMd(7$<=dnJEvLR0AZ>_Wvj((qAnW()lO?8ey$_n?;6;_(!56$GCfrq_u$NP{|`0&WY|cQ5&?Q
xmuBE+**i`moNO~bHSP7g$G=+Vm#bZq~F{S?c)kVV}vzCH10H13)fIOq%|O#Sv~-KLB6I&&!ze;(f%OXoD^H}lHL7DZ<)p>y(E7Q
w0Cs)C;4+U&~E6EJrVX75<t>I{@Vuqv$V%gE}q)u-_zkAr<?rRh7RW^$wjR@whOy42HF-Z1$bP`!YsCCe`3tLY6#kn*YV7}mPgjo
x4I#F<N4~Js`SFVQ#W`|N+0cAzk_zLl744y@o|T-K&5@%Gh5*&P*|`5)Es_Mfx(|I93p>WX*+m27tW?>e9QT+>YARx#t(nKoJWFD
Z!6oSZ(VGZp&e^&WGxYp_Uy9IrAGw~ntEFS+Bg9Ue;!6pM{Yd>yMcS<c1eJL0!#RYpzhZwNFMc1p!Yw>oTR=7>OjBHcSDV9bm$iW
-ZEnWFw!fmErB;gJn(FCU~n+XZw70;uKnjfP$bZ@|NN&`I1!dQ$gM~TL}h|KPD@Kl&b>chVNvE2;9NwPlt5s>p_fsV7ZPIiBt#;%
sen=QR~tZ$4GSc8SS^uZSn*LrgGc8>k%^(Grz9yRnD0BVrim=?^hZWt^Gx~&OdL$$5#%_n(wiGSXL)*T8>aFGcDtHajU5=1VR|P{
7B)?$7mH1TSCl8{bLeq(K6GF)iM0frX{is-c=PfVj4TU_kS`<SbjgjLtasHAts=Ez!=|Y>tjI92ebbDND>i`|n<Zj=#fb4rp+qnO
bxxx1G6LCCax={x?o!omn4iE%F!fKSSo{{U6Z0KB8J26l%P<QH+)R0Pfj#S!slS`b!c|@k<7JHME3*LdWH8QC=#bqHLJ*EiSeZa-
Z;B}JH-H?(&l^AtI!f8QBi?PLzT5)Q*GH=Lnji64EOcMEPkpv3YFlry0hO)T@47&X2$zz!-Xv%Y?ZSjr2t9wUF>7wZ4_ScGEgM8v
<%(~G`HNK=1`=8xAqR4D4x>VyHCzJ&$Uvb<qFEFV_(qy^a26ZIU<apRtu%FCD~O)7(#Q3;Hb@0f6)iW*F*|q=`4RAzN+0bR4E|IG
hbD}~k(8Oa^>Iu1o-&GYy~3U=<mLuex)js{?E^fmViAt|2kzB;U_$zX5Y-=0RL|*<)fNP!uu57e1;`|aI&+Ev7y6LLq6uOJYNiT1
mClbhRH1BiJWJXZoDtMI`n8fqK{!Tt7VZOA`Z+ZSx&ego5(Skhh03&7_RR5mU?+u%QUlk~+Xk)}B*v?TG!)<2sLgz+H%5aScpQGH
w<VhDZOIVd+|uu?#J8?ohxYM0<O|V0T8K7Vi078!Utvp#OX(@WlSDZ}X@SpMiBMjkz#Kh~&f7c~o@rDh2xr{YDrScHM9UMvT&Kqv
#&YMhki18yfNl}esDJi6!@4#LGZFL5x-`|kP#TG&FsHlo2C?PtOKDr@$YYKe1eIebR;zM)0dvrc?!ZV|=$(T9H(O;F0hTFN>xOT?
kHHQKlogwhRIFEc;;S`ZtWT{~T%}}~h-WK>B?~L|!$^i*{K$IMooWK25gyPdk528>lxfeeWXBk&i}(}Jsg2}*vX*CjuapIbr2IjK
U$H$-mZ|s5#7yBi%_D?fQ$2;G^oi_CifNDv=@@K;kCu!)VyO+6rLh8~2^Hdp(wTWt@3xyvmI%tl#MerqEfX*6PRH%$Q9y?!y6VBg
REU##+Tzs`loePL8oCg&Fa~*mM(LhH@5zBCsiOU@^*uS9*)!7jrrE4E+U6e7cBnSlL$!s!d-DJ(9hW~=vCRH-4e`ncsAah=S5)F@
2(8+6Ftcg7-7YWHu-mN6QGiy{yf9x|m*yqz46Jn=10YqD$;czkciJ-Tv2wh_mSMCVGQ^&lnOU_9|M+ZXI6kL~zYYGIfx&^f3O|7E
LVmmII_#kZ1#Mol;o7`vx5=x*PqnF3Z8dp8QMFO+wTpsn(rD-XX%eTriz@<a);jj*kw7`aLXB=}KITf?@%b3JL#Ku_Wt5$6Oj2Mm
M0>>Px7<95+I=nDhRH!g^3fvnqUW(N0|_JFH(kXGC`lbaH~@=kVNFYDN{?LW$OBJwB6I=hQ<51q+}vfF1*#CmsSMtErm7!lCkkzk
F)}lQu2lNW+g6cXtMn_ZCj;RK*HE;wh&OHRfl0Io7b~!P@HlIfE-Q-S!i=Uc88e4yuHXf9;V*R)Bbao*292(;17HFeXVtu;E-(A6
o*D4cOCrh_p5G#fC7Na!{(B$~U_AK|Xn>%-(_g$rnj3r|L@1uKSxSp@$<G8X4#r@$$*AHD!VW7kak+{`+fZ0GUphksuq`NskU>rr
J>b%c=RD~^h)-?1C1w6}sAvqZzcj)w4!Ja38lx)pO|+Bsm_#R7^Hp>~HQ8hAny+FlWLwz`ZAzcj=kbnSgSaYe=7eVEBhgZt)!}DD
cjk5=4dnxx$zGvWbM+jk=TUM=S|$^Q`bQuMiYjqreJLCPWWhwTF<@IgPfv|5N*jE%K|VWJZx~g-5CCgo8&K+@x<Jgyu{=_z`f30)
j{W!IaJ5PK!mM799sIo{8dv<IL_vvU`K5Ut?{L*4s`_Q@6))uzw~S!bzic<lR*2WYjc%8y(2Qd4c5Ejr49@5tWJ9)v{(*0QTL+Pm
*C>NQlh_#ecWVrOqwt=X8<Yq<<r>Q9TPrnqIbIPonD^D+KtNra2X$Zmk1~^<gVL4qFd_~Oq|#RC7YrIoDRXmFB2`O_{x4}s?=q?=
M`z5R!muAasVn^oD4*BD{l7OWea3m)T<)rA%C_2@(Eyk>RW;^cjnekh*9tRx#wZN(2t(x5ORSTgHHR`ZhQQcjiyw*%N8gI&q;M`Y
0T}-zC?ixQJ-0ao1Nl{`_X_O}f<Wd%_tl)Ux_(K<N$`bSIPV__f@22(U)CQ`yfQIHHgwB&tmhuEBTqx!jaly^+!*Ff1j(kM;D&N_
D;;D3;PC<E2CA7$ra~@<7;s}3Vk8KRC;5Bh<S2D<%ytO|p@?(G0WQHblyFPd4KsiK8;y)7nk<2QuAc(AhN`9_Ee&&u7|Am(Un>gp
$;P`%Ul9@&32CgjJ#y$rhG0qgP|F93pCkt;ghZu}QsI;uj$!BZRRyO6LLroIr3Eys@SXd3Hs+&Ooi*dB7cDjk1}~J3$R$9}J8mHt
>jT&cQ>D1ZQCcnKm4KDcApghuA!nwHf$}`TEM-JZ!Fk(}iquC{&@c_C4f{Vmv8;~m`ARuv0o27`pl=~wbdtja9XQR1I5r`opun_Z
F6uA|_a1K2)+$G*=!g5^6FnR$0hNCVS!m0*x?R%gwaW5Ff_a{I7A^ux9lP5qcUOo09<6{8!L$=X7k=l`0P>}VebhU4&n7*)*~G}U
mff{U+i5iNXl9`@@Vd%Yo*JZ(%Y!`N9ET->tonslkyKQl#h9t_rJ`k*#_>`sX&r!l+)#x#=7958NfItR_AX`1k(P1{jzt>)5nVG{
DIyMVdszfk5FS_{g9(^Mw%Wyx13WX!00m)EtH^`v;Xb2Ed;v#F9!qc(V<18c)PRE0HuAX;0&GFYKZM020148{CYxH_azKD65ztD-
7(Ba&fA{;V%l8*|cUO0RebZj_GefFRLoe~?>ZbiQnzOL(@Pt5yNCT<ZFD_r0vY?I!T&4ah-iCWA6Xl5}aUT&skR#5=fNT^&N}K%P
NfMS1`0yH5Hjn&=I80Lw!vIKrZV|*RuCXj!AT;RY$AepI)LQjBKl*rZYEGvHHn9j5;E@6>Hh?bzsLyYUNVSk3gz(X0k1;>BV!L1L
e6P~a@hYu_@it1p0IPiXcy;{>kUhTs{kQS`o7=04*LSeED^5kZ;V31_4*YW)_3=hrh7_;m7Cdm=Lrq*H73MJp(R2y}2Xh-3MTnu9
$T?x?Xbb7kV9iTrTlCis?yjz0ms4FxeS2R{Ye3p>A6{S4Jf+EuPL!uI$#~i1mS=?rY{Cd}s#6-TYl|pO*Ffk@AHJ@-#von=VM_Q~
Wkm|tS8V}eG!BvwA7<VrO?3<-&9D>;HUjEHpUIFN6RW#bcI?_@5bN&oK_=D*!u~Q31&m~O3W-4wz4;LspW`|1m3qrb;AxM2fafKN
chHCMBy<D)vAzMt-+DCa@OL8|CL4q)Az3^i`3(hNdS(pX{K}qKHl$yE`2G5x+JjeDclQ|eIJmvK{BZl4S;zTKGs;aI!<Mn-1cw&x
*ZLL|GGhR8uSjtEPSrK9M@9`q)!bW$x=XH+haf9WDReS3h6tPVN7cm4@@IhZ^BXM33h~}41^H-7g@47;3k>VZTZgg29I1HnS1G0g
y%Bf=*(%<k-?;n4>H{2)Iu>eF9JBg_w^#Me6nB$ZT_xRO>ChGqY#9YqXQM;wi9fKN+`-&iOpC0ln)QI^Bh3sNfa(BbZBy68^5(-}
?Z{_5eisE$h`pI^y#ZX;RdRL6hV*KY&rUaDYLNusKhfRKYkRQFsJ{DI&&;)L81+ws<pJN<4m?AlOUI!sm*v+#S<B2^W`j$|<;koZ
OFRrNT})iNm~emusE!sLfG{D;f;#3UiwhA~!axRr3<8CWpQsaBPFuz<azfL>DfR1M&3W<=Jv8K+9_!gX^o)1r9y)_v(8DP-Yz*$9
A5I<3Kj=m{t;)`136Hck^?Tl>DwKpSIZ*PRch0CoX9j^Nhwfi23dJlea4!k~ET%M4Jxi)cLFgJqXPaFk8PIQHHO+wCg8?P|DJ_T(
x=C0sfz%e^R`v(_V)|3I@9tWxBjVM^ySJ){LH2})s6+=!r`}m-SP&V1#_(g%F1(pcg;#?V>K@(ZF{~)L$Ga%V=Avj~5GG_%bB(eM
E>L(Z%F6?%Ltfl72!EK!2j3XUBlbMulR@%R^`h1?lciz8M#Nv`LCQl>0>&(h;Jl2;uy~Q_E~JmdeFCC4?6?&>?LWTHVci$7?p0X#
1+04xOXve*E<f1cV&sq)f~Ae?wn$u{+mGrNU;BA_e&TR7`64*vY_Xbv%D{LlLC#7zSH)F^X;pUgGfNI=cv6ME;zHni_4+5A-75^S
CLdseq3=8X_KS!h{D_ynv7|f>*a>@l%>mflZ&%9W^aI($3VW<zX(n~46sbbMO0ueqI7n9fB@U*~WCeSd(gFY$gle&@r&T>D$xcz>
-iy`3lQUI3dxI{k5uVt-Ht-$Abwt=-upX>7X*0V4qmIt29y;KkaKI!11s1CE>n>};%Q}Ws9d!|d;1yl4I_O)xj$)mHT0^@8CX}%z
hj{pC<4qM&I_J)IvRfq&xSkxswyBwl94(h27)x2m)MSnexr-gsYl2ao6kAjqT!Ick5#=PF0$<=nl5RlZ1KBrOtrj|ru_h9rtMC_B
HwIW>hInVP2lY70RQzd0)tbLve;a?rcHswG`X;pf0aj2|e#NNZz5iakGB(Qeeg+9Amnc*|1!HC|PqBd}&#WnSHaCq@uEd{)gFbzw
=V|n-EM)Q(H`zps|7V@V|KIp@aS!V2x4-RYTCY$2OoKR_(XXM{5emg7*1EJI^ppKf0m6uuRVKpy!J^jJ7|;a3_!~TMzum>F%L-w4
*@2E74*Lz^><F<PUMdJ@U?NtC*t!ChAe3RaA@7ZGCYDa|kTJ(m`otEH#FcEY&r1)B{*0>f{(xe9;s!ikRw6@f6ZhJXk#I~H#t3GY
Nio2`KT?q?KovNZUK{RF;9eHoH9YkrC`<*~GoCT}#riFH#VlEE)|^pr4v=`|$o5}E0vf2lJQ1D#gK_aCP9!!CQ4a#GMo=HScmkvp
!;mi#u$$v~B_tP~&#aD@jvDMki<|*}%<o0h_tk?TtUtjJ(E9U;ms@>m*rW%`ms^ThlEVT9<ss<f^kJVFdwEzQ1`Fywik<*8iaB-i
P;7Qy2Bfb~Y-2Qt!TehWGA4izkCjkwu_FOLWdk<!S~pJaeB82Nff#5KL9yNFfCPBY-|>}_s7k<~eqz@{GL!A6{8nSm4q^gzh04f4
mzxV-QaL2mhIqExf`B&1CKtFh9|uq>pO6I!Frq_G*zeH<FrLI9+s`UAEZ8bMkTu(QVJiSH*4Dwij89jKakSUY$iB=9*l96kJD9~d
5>V~YC(QXvpH~}B$d-6je>C()6m#Wq+yHL?_VK{?AcpB3K#FKc<;F~gL*JA|&r9VCzkf2@P`vP^<HVm%GiQ$!p$}c?270pT@E2AU
<KH4Yt;}}%c}WtT9#`NwRYyIw@JIz+BR~U(hcp*+nu`PSh`y!r?WU_tdjyK>!}#Sg)Y+&X4WmE`<BOOKOc6S%x;=4Xb0<D8T_Mmi
sX%RU`pIKEKJW&8sIZ&oDg+XT{jTheLJADV7_!HeDmE)2fR@E6gj9Btr>g8U@2sKl%qLx>V1Y;{Dcb~*F48=XK{!DXN)n-mo8863
5XP=^ul-j#9>3#WT!7B7m`O$*Ml+zVbpE$Ikh}`R3R`qDMFQkE<DB@mGJ+R}Dv>o(nH1h7wi?%pfe);!#;$r1x4ejF)Eu$se6E!J
r%?bLV4cqAHKcP;<m(D_s7O-0I1)<zOZ&hgykYXi^{1;O2otmheV~SiU6h6c;BL4h5o*~=%ddLK>4JH%QSDj}hj?Lti+36f=FqtE
{<(B2g<Oz#Ho38Bj$hCm$Q<>`clA$$OL|lPgccp>17V`i2)onq@lhE=tz}8~iqpaaFr?Ok|5wY2=vdt;wOVzjOPci_!3Q?}U=Q7P
M%Ee+;K#92HrV4{z6C$x5_55STA#7P#?LX3gof4aQT6e0*e57fMrN>Q*Ycs4_0cfrbDoV4Al>(Sy0>Of?-kW~)?6Iq7~D^(zTemG
O?|h+oA(Uk=l#C^O1QUp<K`>o;NrZLN~#w}{_m&c(%{B7l4f7^11S!kVeZV~52<|E$cL>lB8$~5rCH(3;Agmb!$s<+!jChfvm*VH
UKTHByfF9leyTb|%B}#W2t6x4nW22LZxCgty9Vz?!|Jxd^KJpT!ojSv-jnyn$ZS62AHbdz{(&gV{R2)bcM!OL(?O6Ft{$}H_uTLq
B+_NTuz-Km_L)b6zUR&YtcDMN(_etdr_+ieHpXAEJ>ef1FcHN><9Yd$d}q&5ZVECGd0&%Zg;85&gmi$f>TdLTrvZx{Q_X=>zrhck
d;KQ{#MABv);m$E5a=?ODJYQp_f^8RywV&b(UFP!O(>fQJLs<(&`eE3W0}W{0;5hq*?ms6d`hv*yYh^Jd7@rQfIq5F{*WqpqDB5g
6|&GCpH&^dr!_K6=c-|{eZr-15`wZ;VuJsPMp<4nnwBq7{V8+4nA8zb2r!)q4HQVFT7hR6Pe}(=m*gr{mCV<|(*w=n-C1mTOd`I!
YVj)tVfs+%WNHPhIH8QzLG{4%^a*GgZ`t>Y%4-2tl_caBdu9BH>aibDM&V3hZZ&@%`VZ_2D5qQH2#+ikkK&K8gOjuJ<-_o2{grob
-u`lbCqLA&Ev~^XAAz;lVIpw~w#h$h@KVPMiQs=c9FX11%{)B#y#uMHCL2ar!W6?pd<u*BMfZ&(E`gWmpE$^{TFFKBQo6{{ohCmk
5)!Kn?xfmJ@-`o+R>Nwz4CF?&*Jn;MbX>4e5PZt-9t6xH+u+=zFhWCeEgfBogAC9Sp<pa-a+l>9YB|o2Ll7xP%f5Oz_OXP(<-p*R
1+4Q0%HTfY*)qm$Jo1Zf8~Eh|nKI!i<qCkGk8B=q&K!GBgz|FDE@ecz<jO5i{b-o{;pXgDTncpL{3v0EC_j=L<J9CWikDazU>Z0N
D7LV+&v<8)M%cuv5q<NOY>pPi*hyHWX(;v5IcX76&o-CPU-SeO9Q_0tbr_WCnx@;tn`iMyaj<#x+Dt&lo=oU9qB1Fu-}7F6MEBBU
^77_%^sK@2!-uH_A!kv~!v!>)z~f}1U<b&z1j{2HqGU25$<fs&Sd=qzd@@cLJ7|l@(8Z#IG@`7beV^YGqVG{89p3>2X<V@vAK`Ms
2FBMji;l|##p@sxaa_ZA*)74|pcr{p9T%(Y;cvRL6wiq&sRk#Vpn|QP5HI8%EuVjBcblb_nM+f@HJ2-KfX&k6qw&97abr(@KuOE5
q~+p?+qLR)#Lov%abzPkPVWpjnqqc|19bh&%9dfuo(Uug#CffLTBFn+&{q}di@!|ZWik;j;fPw-XCtb4Pbng>oG;EG<EiaR|AADv
;Kk_oToFL=er*u;>hV|46YmrLJ`ul(F?w#?qi;vdvDgX#<v{UeF_O=nSx;>aVBgPdFoM2;H!|^P&vX&t&HLYXarK1?qMUAIel0J<
1NC^p8;=IeL2C?jDueYj7Okh%H5RX@$$&kK#$904UlMwOhR&|~hu=Q3$i4iNhIkUFxE1QW4g%)tKZw2iFLaKbhUcBe*g2f9xS-aY
i`+Y{;ED>prtN@IcN*AtTBRYXwCra?_#RPP*kw!s*pS^11@V0+u&)0oegEayzD*t4+huts57(>XWdMq!>JiHnuRFA)GIp=^6Y+Uj
5ucYC%2jhm@p(YXixi#o`1u0MVH_a|N?~}w|FaY?Wy?ItX)zX8`X@1c*muhjc|6taD*<^;9+1br?u8*g=m%j6sm?l@2iXDa+z0kZ
T;lB`=%B%Z@7RdNe$k$ugt!fM2a)K?#D=_-b^k=P90sGwI+m=HUx<R&9kQ<SZzT<vd$K%`#}V(91Ct`6Ja?J7+nc+?;1d-|HB?9Q
W8Nb1X9kct-`G7&I(x6(%lJ$~7C7-*VsX4e6d1RJrDKbGoMPAfWDM?x4slA^2k4N@7UA~Hht@P_FxvX3!95O*U5Pq$>J5Vb?Apkv
o@ty%@Ep4e$(_NSY$u;dISm+l%E`w+f^zq)qYnuV{wZb7$BvbPqDmwyVxt(n6Qp*+NnIESn4Iryvj{1w(!C&i9wT+det@kNF;2}K
Ni>lmPQ~4g@ct5;R0KF%Z;&n*Tp}KZ71m&7MA>gXuo8yRz4<*w>N^2TL$nDo@X5uXr!HPOZ0b!D1oq#EVRGz$9K<Bllq4uQC0Pv9
*+@C17tBM+=k@QoCq=A?2xvN10*as}8O?-8fX}NId<ft3R;mg+!eZ_ng)omjlSg|>C2vTSvM)g%#CZg-e4OCq@W5mhu<Hf!<B{^5
f&}}d{_q_w0YoPfnA89+8Q3?Q#o{0AqCKmAC@19kmJgZBRsM<EwZS{2Uw%uni-vRl#xDFe25(&~^|pb3*|*KGj!oa?-`un5jd(u$
iBSHPwe`_g*0y}#Dk4!8_pLT`uDq%?B<QvjH6RP)5eTX_>}ha8K|#il+{pxU;n`u&b|H?q(AaR%GDx>{%N~V@9PH@k=k4iDd-z>O
cHv#Rt?tSf=iP{$oZ+Wil5Q0Nuq(ep_Rgs4Tijm4Tktl9@$>fFO?Md5j$aPjkd0C0H`G1g<#dZPpSNWxiz4Nrinp9Uebt=+1b>!4
0*y43L!RQxrKQ{M<cGwd1)u}g&K9tCW6Ob*Py=JfAv^9<SLG3e#rGvoc6%Q&r~?BrKfgd-!$L2A`1!^09x$>8B-<@lJ9NJ1TN{y~
_+>{77Mo=}79}2s{g@@A_VqZ7`>q+|S9x>y08nSKGJ$w&@<V3wCM0<uEzN<PKi2SAI@a(gjy1^GL#Mj_IS0kgHYo4LNd)4#4czbT
-wJbmE%-w%*GVo74DjJwWrb*Nl)q&$DsC&pqgKp;tNjmD;<aQ0<{3BV!0=jaW^=I-piRN77e@U5k=^6-pCMkCVqm^dJ(6EsUK<0p
;rs<RoTH-+XN&JR7aPvvKW09#Zw<0aB#w;%+ij1I_nnn(XPyba>Wy5$z;u>_$*4r{p)+es@e!0Zq2(U*WFj`9ClfQ1I&d*Jxrd8u
e&=?j8A<Ys&G^!(0E6W!qB78{h8*c`N7$$5jKSF^@aTU1Z9_ujSDqb1^b+6#Z(Vfv;RR(P^**6DcKyOC*aOh<tfV==!_zJo=XB}s
j5jgwlVY$K5hDj{fqIn~&p~l&E$A$sz|rx70z(22V=Dn*Iw)>J@j#uV_{Iv`B||m^d<yiE&o9ucneY?vkX)=nH9+92*lz7JC8i?u
ib`KO*-_!)2bKO@Nz1>P(4VQP`GJi}UkL(`A7ki$A{9Jm%lljD^WSe}H5of1u1q{R;Txas`=3SwxM!jP@Vp?y&5xWHEVFrm_WTe6
*TCZ{dvxXF(FueWX%r`yQ_#h~8*m^FBS1$|s&jc`kh7coXB2q*pD6I`&~z^Bcz0`iA@gL|0Y3*UKTm*|WVyh?&UcdO_W~B%*jIv3
WD^B}luQ7TEv*143-S2Ev{GNjSsk5$^<u|8tjqWW>=P*d@wZZ_f)Y}PP@alcC?AwQr}y)*5_MSeFuMp^Ae9X8C65tHY0Z84vZ!2R
Bcp6IeD}2TH}YZ~#p#Rw*B8&+`d-{zK6LD6(<Lw5$#mMBHhO-y6*k(PW;1Xc+wb-oo-^r9oTeL2oQB`>+iq_XPP%Th=}f%94eZ{;
Z%v){i_w#pqYpbhyGvd)d#>H;c+*}mX>^*N@3kh~MiAOvr|nMK6My12AtSK;hUdE-zZZ4`+w&)Gw`X_4&<U}HCr)w?-Cm<XUO4Tk
-|IPH5HxJto7lG9_Pj>7-EA}`Jtqh~2f#JF9<=IqyiU+{rlH&RCT%zDOdAakTR1&o0vK|e<VE24PP09A?4CF6x}n#ccAR$Cb2?7Y
bK8y!c!E|TyW48@I)J!V*qV4<yEhFw(AXpgUc{gb9k=U{7oC>vw}YnN@|qpH+i7)zDGa$i_1s>o>vY==wC7D)y<Vr)>P|erHwhXI
=uW5MOl`X{%^|B8aoRl>JKYFeK(^OzwE+n**Fo6rH79nn(Q8e5-Hzjj?PkY!>~`3}Dy?AJp0)sT!wp-#ZUOozd}at$$%~2I@cm}9
*#a79IbI8<VG=s_)U&&-jve%zR>OAvpw$beZnM+1TkYn=Yr~kDlfZA;?E<_A1sJ+^58!r#h97nTxdF^z)9-eJNyoMU3Sc0ZI*8D)
3%F`bK?`)k(4P8@ZWAV9>Upislwsr<m;capoHlvU_Bvg^-2mEace|Zw8^~~Cx0<dS`d)Jav)%B4C~PluyFobd+dZc@>9}^I<#fXq
j1^lsXTc8}cDs$ZcYBTtli6*CUORx9bzGqFjvKmmyXDz#d(!ZG%}%rH2A<z+cU*T8OxoUb(sUb*FnBTg_U(TIyi_t}
"""
def main():
    raw=zlib.decompress(base64.b85decode(''.join(PAYLOAD.split())))
    assert len(raw)==35404 and hashlib.sha256(raw).hexdigest()=="499f158a8306caff0479798bbd857df7e374c320a99958a067afe72616f29599"
    obj=json.loads(raw);root=Path(sys.argv[1] if len(sys.argv)>1 else 'centered_planar_recovered')
    root.mkdir(parents=True,exist_ok=True)
    for name,source in sorted(obj['files'].items()):
        assert Path(name).name==name
        b=source.encode();pin=[len(b),hashlib.sha256(b).hexdigest()]
        assert pin==obj['pins'][name]
        p=root/name
        if p.exists() and p.read_bytes()!=b:raise FileExistsError(str(p))
        p.write_bytes(b);print(name,*pin)
    print('CENTERED_PLANAR_COMPLETION_FULL_SOURCE_RECOVERY_PASS')
if __name__=='__main__':main()
```

## 9. Continuation

The remaining universal problem can now be attacked entirely through the actual affine-density planar side model (4.1)–(4.4), with no additional graph-facet or transverse-fibre obligation and no localization mean gap. Any strict failure has a rational polygonal actual lift; a complete positive proof still has to handle arbitrary convex supports rather than a prescribed vertex count. The concave-profile theorem gives a separate infinite-dimensional benchmark and effective mixed-matrix constraint. Neither route changes the E17 minimum without the original mechanical obligations.
