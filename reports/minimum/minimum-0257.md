# minimum-0257

AI research report · 2026-09-27 UTC

---

# JOINT_SUPPORT_SECTION_897_AND_PYRAMID_COUNTERCONTROL_V1

## Result and scope

There is a rigorous universal improvement, and the suggested simplex constant is false for actual uniformly filled bodies.

**Universal theorem.** If K is a full-dimensional compact convex three-body with its uniform volume centroid at 0 and covariance I, e is a unit vector, and y belongs to K with e·y=0, then

`||y||² / h_K(-e)² <= 47263586279502290403 / 5269120000000000000 < 897/100 = 8.97.`

The first displayed constant is approximately 8.969920267426495. It is a certified upper bound, not a proposed sharp constant. The proof uses an actual radial volume decomposition and the mandatory convex hull of the covariance inscribed ball with y. It does not replace the body by assigned vertex masses.

**Actual countercontrols.** A five-vertex quadrilateral pyramid, uniformly integrated and then whitened by its own covariance, gives the exact ratio `1053/172 > 6`. A second rational pyramid gives `751249/122530 = 6.131143393454...`. The maximum within the explicit one-parameter pyramid family is rigorously between 6.131145332531 and 6.131145332533 and is attained by a genuine full-dimensional pyramid. A two-parameter family of genuine simplicial triangular bipyramids approaches those values; explicit rational members also exceed 6. Thus neither 9/2 nor 6 is a universal bound. These are not U1/S1 constructions or minimum-problem attainers.

**Finite-height consequence, primal only.** In the actual covariance gauge, a primal escape tree of height h now gives

`lambda1/lambda2 < (897/100) cos(pi/[2(h+1)])^(2(h+1)).`

The polar factor remains 9. Combining the new primal factor with the old, same-origin polar factor gives, at V=10,F=9,

`lambda1/lambda2 < 420089917/60000000,`
`lambda2/lambda3 < 6832329/1000000,`
`lambda1/lambda3 < 956730840842231/20000000000000 = 47.83654204211155.`

The coupled trace-one primal metric floor becomes

`H/tr(H) > [20000000000000/1113377420842231] I`,

approximately `0.017963360515134842 I`. This is a universal improvement of the necessary cone, not an H5 regional computation or an E17 exclusion. No complexity bound or attaining upper example changes.

## Input audit and authority

I read all four complete supplied attachments, including the entire shared notebook and branch memory through EOF, before substantive research. The mounted bytes match the user's manifest:

- FINITE_HEIGHT_RECIPROCAL_DOMAIN_V1: 10171 bytes; SHA-256 e7daf31f7dddffac638b3bb0d7005af5613e4b2473b0979daff4357ebf5894db.
- COVARIANCE_NINE_RATIO_AND_PHYSICAL_CONTAINER_V1: 11958 bytes; SHA-256 e43bdb2b1745cf265601df70863e60face5ee25d5ebc4e36d120c8d361bed173.
- INTRINSIC_REFERENCE_ELLIPSOID_FINITE_HEIGHT_WINDOW_V1: 7853 bytes; SHA-256 d40619accf0fc38f68f9155c87c3ea2f5cf8ce8c590dfa1b3477cad75cbbe100.
- research-journal.md: 285454 bytes; SHA-256 b84cf5ebf92d44ae72b95eeb743220e6a073c8ad969719d04b830040d6245742.

The branch's actual-body and primal-only requirements are retained. The intrinsic-reference theorem changes the matrix when its reference ellipsoid changes; the new universal result below is specifically in the actual covariance gauge.

One provenance mismatch should remain visible: the finite-height source's dependency note names an older covariance digest beginning `4f0c3336`, whereas the supplied covariance file has the manifest digest beginning `e43bdb2b`. I used the complete supplied covariance proof directly and do not claim byte identity with that older digest. No missing archive payload is needed for the new theorem or the executable below.

The only outside geometric inequality used is classical Berwald, already supplied in the covariance material. Its dimension/exponent constants and equality statement were also checked against Langharst–Putterman, *Weighted Berwald's Inequality*, equation (1) and Corollary 1.4. The new joint theorem is proved below rather than attributed to that paper.

## 1. Actual radial decomposition and its exact deficit

Use a homothety to work with `Cov(K)=(3/5)I`. The ratio in question is unchanged. Write B for the unit Euclidean ball, V for volume, `R=||y||`, and `a=h_K(-e)`.

Berwald applied to every nonnegative affine function `f=h-v·X` gives `10 E f² <= 16(E f)²`. Since the variance in every unit direction is 3/5, this gives `h>=1`, and hence `B subset K` and `a>=1`.

Fix y in K. For almost every ray starting at y that meets the interior, let Z be its far endpoint. Ordinary polar integration about y, including when y is on the boundary, decomposes uniform volume as

`X = (1-T)y + T Z`,

where T is independent of Z and has density `3t²` on `[0,1]`. The endpoint law ν is not free: in angular coordinates it has density `rho_K(theta)^3/(3V)`.

Because `E T=3/4`, `E T²=3/5`, `E[T(1-T)]=3/20`, and `E(1-T)²=1/10`, the actual first and second moments give

`E_ν Z = -y/3`,
`E_ν ZZᵀ = I`.

For `u=y/R`, when R>0, put `s=u·Z`. Thus

`E_ν (s+R/3)² = 1-R²/9 = (9-R²)/9`.                 (1)

In particular `R<=3`, recovering the outer bound without a vertex-weight relaxation. The quantity on the left is the exact deficit we will force to be positive when a is small.

We also need an upper bound on actual volume:

`V <= 4 pi sqrt(3)`.                                (2)

To see this, let a ball of radius rho have volume V. Among measurable sets of that volume it minimizes the integral of squared distance from 0: integrate the pointwise nonnegative expression `(||x||²-rho²)(1_K-1_{rho B})`. Therefore

`(9/5)V = integral_K ||x||² >= (3/5)rho² V`,

so `rho²<=3`, proving (2). No ellipsoidal shape or symmetry is being assumed for K.

## 2. A spherical-cap lower bound on the radial deficit

This is the reusable geometric estimate. Suppose

`2 < r <= R <= 3`, and `1 <= a <= a_bar`.

Define

`A=4r/3`, `B0=4 a_bar-1`, `W=r-2`,
`D=sqrt(A²+1)`, `d=B0/D`.

Assume `0<d<1` and `4W-3(3+d)/D>0`. Then

`9-R² >= Delta(r,a_bar)`,

where

`Delta(r,a_bar) = D²(1-d)³[4W-3(3+d)/D]/[8 sqrt(3)]`.  (3)

### Proof of (3)

Use orthonormal coordinates `x=-e·z`, `s=u·z`, with the third coordinate suppressed. The condition e·y=0 is essential here: y has coordinates `(0,R,0)`.

On a ray from y meeting the unit ball with x>0, define the ray-constant function

`psi = [4R/3 + a(s-R)/x]_+`.

For its actual endpoint Z in K, `0<Z_x<=a` and `Z_s<R`. Consequently

`Z_s+R/3 >= 4R/3 + a(Z_s-R)/Z_x`,

so `(Z_s+R/3)² >= psi²` whenever the right-hand positive part is nonzero. On all other directions set psi=0 and retain the trivial lower bound zero.

Convexity supplies the actual contained body `L=conv(y,B)`. In unnormalized angular cone-volume measure, inclusion gives `rho_K³>=rho_L³` pointwise. Hence (1) is bounded below by the corresponding ray integral over L divided by V.

The boundary of L consists of its conical side, whose radial flux from y is zero, and the far part of the unit sphere, `s<=1/R`. On that spherical part the outward normal is z, so the radial cone-volume element is exactly

`(1-Rs) dS/3`.

This follows directly from the radial area Jacobian, or from coning a surface element to y. Thus

`(9-R²)/9 >= (1/[3V]) integral_{S², s<=1/R} psi²(1-Rs) dS`.  (4)

Now set `L0(x,s)=A x+s-B0` and `w0(s)=W-3s`. On the unit sphere,

`(4R/3)x+a s-aR >= A x+s-(4 a_bar-1)=L0`

whenever x>=0: use `R>=r`, `a s>=s-(a_bar-1)`, and `aR<=3 a_bar`. The cap `L0>0` automatically has x>0 because `B0>1` and s<=1. Since x<=1 there,

`psi² >= L0²`.

Also, for every s in `[-1,1]`,

`1-Rs - w0(s) = 3-r+(3-R)s >= R-r >= 0`.

The region `w0>0` lies inside `s<=1/R`, since `W<=1` and R<=3. We may therefore first restrict (4) to `L0>0,w0>0`, replace the integrand by `L0² w0`, and then extend over the whole cap `L0>0`; the added part is nonpositive. This yields the valid lower bound

`(9-R²)/9 >= (1/[3V]) integral_{S², L0>0} L0²(W-3s) dS`.  (5)

There is no assumption that the extended integrand is everywhere positive.

Let `q=(A x+s)/D`. The cap is q>d, its surface element after angular averaging is `2 pi dq`, and the mean of s on each latitude is q/D. Therefore its integral is

`2 pi D² integral_d^1 (q-d)²(W-3q/D) dq`
`= [pi D²/6](1-d)³[4W-3(d+3)/D]`.

Insert this in (5) and use (2). The assumed positive bracket permits replacing V by its upper bound. This is exactly (3). All integration and all measure comparisons concern the same uniformly filled convex body.

## 3. Explicit universal constant below 8.97

Take the following rational numbers:

`r=29949/10000`, `a_bar=10017/10000`,
`A=9983/2500`, `B0=7517/2500`, `W=9949/10000`,
`D²=105910289/6250000`.

The following rational inequalities hold:

`D > 8233/2000`, `d < 1461/2000`,
`D² > 169/10`, `sqrt(3) < 26/15`.

The bracket in (3) is positive. Substitution of these deliberately outward bounds gives

`Delta > delta0`,

`delta0 = [(169/10)/(8(26/15))] (539/2000)³`
`         * [4(9949/10000)-3(3+1461/2000)/(8233/2000)]`
`       = 158493720497709597/5269120000000000000`
`       > 3/100`.                                      (6)

Let `rho=R²/a²` and

`T0=max(r²,9/a_bar²)=100000000/11148921`.

The exact verifier checks `T0 < 9-delta0 < 897/100`. If rho<T0 the desired result already holds. Otherwise a>=1 and R<=3 imply

`R² >= rho >= r²`, and `a² <= 9/rho <= a_bar²`.

Thus (3)-(6) apply, giving `rho<=R²<=9-delta0`. Returning to covariance I proves the universal theorem. The convenient constant 8.97 cannot be an equality case; even the larger closed-form certificate above has deliberate slack.

This is a quantitative incompatibility theorem for the separately extremal support and radius bounds. It is not an optimization of the cap argument and not a claim that the sharp constant is near 8.97.

## 4. Equality at either old separate bound explains only 9/2

There is a useful exact boundary statement, distinct from the universal theorem.

In the gauge `Cov=(3/5)I`, if R=3, equation (1) forces almost every radial endpoint to lie in `u·z=-1`. Convexity and closure then force `K=conv(y,F)` for a genuine planar base F in that plane: otherwise a positive-volume set of directions would have endpoints off the plane. Radial cone measure on a flat base is its uniform area measure. Consequently F has horizontal centroid 0 and horizontal covariance I. The two-dimensional Berwald support bound is `h_F(-e)²>=2`. Hence `R²/a²<=9/2`.

If instead a=1, equality holds in the three-dimensional affine Berwald inequality. Its equality condition makes K a cone with base in `e·x=-1` and an apex at height 3. The actual mean and mixed covariance force the apex to be `3e` and the base's horizontal centroid to be 0; its horizontal covariance is I. The central section is 3/4 of that base. The planar outer covariance bound is 8, so again `||y||²<= (3/4)²*8=9/2`.

For completeness, the planar outer bound follows from the same radial calculation in dimension 2: endpoint second moment is `2I`, endpoint mean is minus half the marked point, and nonnegative variance gives squared point norm at most 8. Equality makes the planar body a triangle. The planar inner bound follows from `6 E f²<=9(E f)²`, giving variance at most half the squared support distance.

Equality 9/2 in either separate-bound situation therefore forces a regular tetrahedron in covariance position, with the indicated planar support or central-edge configuration. This explains why the simplex value appears naturally but does not extend to bodies that compromise between the two separate extrema. The actual countercontrols below make that distinction necessary.

## 5. Explicit actual pyramid counterfamily and its sharp family maximum

For `0<u<1/3`, put `b=(1+u)(1-3u)` and let P_u be the convex hull of

`v0=(0,0,0), v1=(1,0,0), v2=(0,1,0), v3=(0,0,1), v4=(-u,b,0)`.

Its true maximal facets are

`(0,1,2,4), (0,1,3), (1,2,3), (2,4,3), (4,0,3)`.

The base is strictly convex: its four consecutive turn determinants are `1`, `3u(1+u)`, `u`, and b. Thus every parameter in the stated open interval is an actual full-dimensional quadrilateral pyramid with `(V,E,F)=(5,8,5)`, not a limiting density.

The two tetrahedra `(0,1,2,3)` and `(0,2,4,3)` partition it, with actual volumes `1/6` and `u/6`. Their integrated moments give

`Vol(P_u)=(1+u)/6`,
`g=((1-u)/4, (1+u-3u²)/4, 1/4)`,

and, writing Sigma for its actual covariance,

```
80 Sigma =
[ 3u²+2u+3,             9u³+12u²-4u-1,                 u-1       ]
[ 9u³+12u²-4u-1,        3(9u⁴+18u³-13u²+2u+1),        3u²-u-1   ]
[ u-1,                  3u²-u-1,                       3         ].
```

Define `n=(2+3u,-1,-1)`. The actual equations are

`n·g=0`, and `(n·v0,...,n·v4)=(0,2+3u,-1,-1,-1)`.

Consequently `h_{P_u-g}(-n)=1`, attained on the genuine triangular facet `(2,4,3)`.

Now define the actual uniformly filled isotropic body and the requested data by

`K_u=Sigma^(-1/2)(P_u-g)`,
`y_u=-Sigma^(-1/2)g`,
`e_u=Sigma^(1/2)n/sqrt(nᵀ Sigma n)`.

The square roots mean the unique symmetric positive-definite square roots. This is a fully specified exact algebraic reconstruction. Linear change of coordinates preserves uniform filling, so K_u has actual centroid 0 and covariance I. Also `||e_u||=1`, `e_u·y_u=0`, and y_u is an actual vertex.

Set

`N(u)=12u³-11u²+2u+1`,
`D(u)=36u³-11u²+2u+1`.

Directly from the integrated covariance,

`gᵀ Sigma^(-1)g=15 N(u)/D(u)`,
`nᵀ Sigma n=3(3u+1)/10`.

Therefore the exact joint ratio is

`R(u)=9(3u+1)N(u)/[2D(u)]`.                            (7)

At u=1/6 this is `1053/172 > 6`. At u=8/45 it is `751249/122530`. For the latter, the raw fifth vertex is `(-8/45,371/675,0)`, the actual volume is `53/270`, and

`g=(37/180,731/2700,1/4)`, `n=(38/15,-1,-1)`.

No whitening approximation is required to certify these ratios.

### Exact maximization within this family

The denominator is positive: `D(0)=1` and

`108 D'(u)=(108u-11)²+95>0`.

Differentiating (7) gives

`R'(u)=27 F(u)/[2D(u)²]`,

`F(u)=432u⁶-264u⁵+209u⁴-100u³-42u²+4u+1`.

An exact Sturm calculation in the complete source proves F has exactly one root in `(0,1/3)`. Since F(0)>0 and F(1/3)<0, it is the unique global maximum in this family; both endpoint limits equal 9/2. The maximizing parameter is the unique root in

`177618408377203/10^15 < u_* < 177618408377205/10^15`,

and exact rational interval evaluation proves

`6131145332531/10^12 < R(u_*) < 6131145332533/10^12`.

The parameter is strictly interior, so this family maximum is attained by a genuine convex body. This is a sharp family result, not a universal classification of extremizers.

## 6. Preserve the nonpyramidal constructions, not just the largest value

For `0<u<1/3` and `zeta>0`, replace v4 by

`v4=(-u(1+zeta), (1+zeta)(1+u)(1-3u), -zeta)`

and retain `v0=0,v1=e1,v2=e2,v3=e3`. These are actual simplicial triangular bipyramids with `(V,E,F)=(5,9,6)`.

Indeed, with `L=(1+zeta)(1+u)` and `b=L(1-3u)`,

`v4 + u(1+zeta)v1 + zeta v3 = b v2 + (L-b)v0`.

All coefficients are positive. The segment joining the two apices 0 and e2 meets the relative interior of the equatorial triangle `(1,3,4)`. The two actual tetrahedra `(0,1,3,4)` and `(2,1,3,4)` therefore partition the body, with volumes `b/6` and `(L-b)/6`.

The same n gives n·g=0 and support 1. Its exact ratio is

`R(u,zeta)=9(3u+1) N_zeta/[2 D_zeta]`,

`N_zeta=(1+zeta)² N(u)+12 zeta u(u-1)`,
`D_zeta=(1+zeta)² D(u)+12 zeta u(3u-1)`.

The derivative is

`dR/dzeta = 108u²(zeta-1)(zeta+1)(u+1)²(3u+1)/D_zeta²`.

Thus the value decreases until zeta=1 and then increases; both zeta->0 and zeta->infinity limits are (7). The denominator is positive, for example by `D_zeta >= (1+zeta)²[36u³-2u²-u+1] > 0`. The family has the same supremum as the pyramid family but does not attain it at finite positive zeta.

At `(u,zeta)=(8/45,1/100)`, the exact ratio is `7540947049/1239848530 > 6`. At `(8/45,1/1000)` it is `751526809249/122674382530 > 6`. These preserve a genuine simplicial nonpyramidal countercontrol; the failure of a bound of 6 is not confined to the quadrilateral-pyramid boundary.

Also retain the simpler initial two-tetrahedron control

`conv((0,3,0),(-1,-1,-1),(-1,-1,1),(2,-1,0),(-1,-2,0))`.

Its tetrahedra `(0,1,2,3)` and `(4,1,2,3)` have actual volumes 4 and 1. Its volume is 5, centroid `(-1/20,-1/4,0)`, and covariance

```
[127/400, 23/400, 0   ]
[23/400,  59/80,  0   ]
[0,       0,      1/10].
```

Take the first vertex minus this actual centroid as the marked point and raw normal `(13/4,-1/20,0)`, then use the same whitening recipe. Its exact ratio is `2199289/424194 > 9/2`. Its true f-vector is `(5,9,6)`. This lower-value construction is included because it demonstrates the radial-apex mechanism with especially simple rational coordinates.

None of these bodies is asserted to have a complete U1/S1 mechanical system. Their role is to refute unconditional proposed joint geometric constants.

## 7. Finite-height primal gap, polar limitation, and coupled floor

For an actual body P at its uniform centroid, let Sigma be its actual covariance and M its physical SPD metric. In covariance coordinates use

`K=Sigma^(-1/2)P`, `H=Sigma^(1/2) M Sigma^(1/2)`.

The supplied finite-height argument follows a true-edge escape path from a negative support vertex to its first crossing y of the central eigenplane. Reversing the transformed path gives shadow inequalities `z_j·z_(j-1)>=||z_j||²`. The angle sum and concavity of log cos yield `|e·z_d|<=b_h||z_0||`, where `b_h=cos(pi/[2(h+1)])^(h+1)`. This argument accepts nonnegative, not just positive, selected arrows.

Keeping the actual support instead of substituting separate radii now gives

`lambda1 a² <= b_h² lambda2 ||y||² < (897/100)b_h² lambda2 a²`.

This proves the new strict primal gap. A unique strict unstable vertex supplies a rooted tree even with incidental weak contacts: every other vertex has a nonnegative true-edge escape, and each distinct escape strictly increases squared H-norm. Thus no cycle occurs, every path ends at the unique strict root, and h<=V-1. Equality of a selected arrow does not evade the argument. The latest supplied intrinsic theorem explicitly includes this weak-contact scope.

The same-origin polar has the inherited radial shell ratio 3, but need not have its own uniform centroid at 0 or covariance I. Accordingly, only its old bound is used:

`lambda2/lambda3 <= 9 f(k+1)`, with `f(m)=cos(pi/[2m])^(2m)`.

A unique strict stable facet corresponds to a unique strict unstable polar vertex under H^(-1). This is the inherited same-origin, same-inverse step, not a new uniform-polar assertion.

For V=10,F=9, the independent exact cosine check below reconfirms the parent ceilings `p0=7024915/10^6` and `q0=6832329/10^6`. Since `(897/100)/9=299/300`, put

`p=(299/300)p0=420089917/60000000`,
`q=q0=6832329/1000000`,
`D=pq+q+1=1113377420842231/20000000000000`.

Writing `A_H=H/tr(H)`, the simultaneous primal and polar gaps give the strict bounds

`[20000000000000/1113377420842231] I < A_H`
`< [956730840842231/1113377420842231] I`.

For `B_H=H^(-1)/tr(H^(-1))`, the corresponding lower bound is

`B_H > [60000000000000/3350282439526693] I`.

The different denominators are intentional: inversion exchanges the two adjacent gap caps. These are consequences for one coupled inverse pair, not independently chosen metrics.

In the original frame, with `tau=tr(Sigma M)`, the primal floor and ceiling are exactly

`D Sigma M Sigma - tau Sigma > 0`,
`pq tau Sigma - D Sigma M Sigma > 0`.

The trace-floor stress parameter from the intrinsic-reference source becomes

`alpha=1/(D-3)=20000000000000/1053377420842231`.

This substitution is justified at `C=Sigma`. It does not insert the universal constant into an unchanged matrix for a different reference ellipsoid. Shape-specific intrinsic shells may still be imposed in their own transported frames.

## 8. What was tried, remaining uncertainty, and useful continuation

The initial simplex-target approach was tested with actual two-tetrahedron bodies and failed: the preserved simple bipyramid already exceeds 9/2. The quadrilateral-pyramid and two-parameter bipyramid calculations then gave the stronger countercontrols above. For an upper theorem, I switched from separate radius/support estimates to the exact radial endpoint variance and the mandatory contained body conv(y,B). That is the source of the uniform improvement, rather than an inference from numerical optimization.

The exact universal optimum has not been identified. It is a genuine attained convex-body maximum, not merely a singular limit: the covariance sandwich gives a common inner ball and outer ball; the support functions are uniformly bounded and equicontinuous; a uniformly convergent subsequence preserves the inner ball, centroid and covariance by volume-moment continuity. Unit e and marked y also have convergent subsequences, and the support denominator stays positive. Thus the present rigorous bracket for that optimum is

`6.131145332531 < C_opt <= 47263586279502290403/5269120000000000000`.

The family maximum is evidence for a stronger target but not evidence that all bodies reduce to that family. In particular, no localization to pyramids, no freely chosen concave-density extremizer, and no global extremizer classification has been proved here.

The most useful next analytic step is to strengthen (4) while retaining its actual cone-volume law. The current certificate deliberately throws away part of the positive far-sphere contribution and replaces a ray-dependent denominator by 1. More importantly, it uses only the mandatory body conv(y,B); exploiting additional same-body moment information could produce a much larger improvement. The closed formula (3) is also available for exact parameter optimization without repeating the geometry. Separately, the explicit two-parameter bipyramid family is a useful nonpyramidal calibration for any proposed bound below 6.1311.

The exact counterexamples rule out 9/2 and 6. Numerical exploration does not rule out any remaining constant, and none of its failed searches is being promoted to an exclusion. No independent polar-uniform theorem, H5 atlas computation, full E17 exclusion, or new attainer is claimed.

## 9. Complete deterministic recovery capsule

The sole Python block below is the complete runnable source `joint_support_section_v1.py`, including a final LF. It needs only CPython 3.13.5 and SymPy 1.14.0, the versions actually used. There are no random choices, external inputs, hidden tables, numerical optimizers, or omitted helpers. The actual vertices, tetrahedra, facet cycles, covariance calculations, cap constants, root-isolation procedure, and trigonometric checks are all included.

Source: 10547 bytes; SHA-256 `ede99b2df3bff51b55b51c72d84008977dfdbf043141015a4ad874a35271eaf5`.

Command: `python3 joint_support_section_v1.py > joint_support_section_v1.out` with assertions enabled.

Expected terminal marker: `JOINT_SUPPORT_SECTION_897_AND_PYRAMID_COUNTERCONTROL_V1 PASS`.

Output: 3637 bytes; SHA-256 `32316b729f0aea4ac3772b7c7d7bf1f3f25ad690bae5bd1f0e905701aee5a822`.

Normal execution and a source-only reconstruction extracted from this Markdown into a clean directory both passed. The reconstructed source and its output were byte-identical to the pinned files. This is an author replay, not a coordinator or proof-assistant verification.

The code checks exact algebra, rational bounds, the sharp family maximizer by Sturm isolation, and true supporting facets for every literal rational control. It is not a proof-assistant formalization of the analytic cone-measure argument. The complete source and proofs here are sufficient to continue without any sandbox or historical archive.

Convenience copies: runnable source (`joint_support_section_v1.py`), exact output (`joint_support_section_v1.out`), and Markdown handoff (`result_markdown.md`).

```python
#!/usr/bin/env python3
'''Exact recovery for JOINT_SUPPORT_SECTION_897_AND_PYRAMID_COUNTERCONTROL_V1.
Python 3.13.5 and SymPy 1.14.0 were used. No numerical solver or external input.
Run with assertions enabled: python3 joint_support_section_v1.py > report.txt
The accompanying handoff contains the geometric proof, not just these checks.
'''
import json
from math import factorial
import sympy as s

F = s.Rational
u = s.symbols('u')


def clean(x):
    return s.factor(s.cancel(x))


def moments(vertices, tetrahedra, volumes):
    V = sum(volumes)
    g = s.zeros(3, 1)
    W = s.zeros(3)
    for ids, vol in zip(tetrahedra, volumes):
        a = [vertices[i] for i in ids]
        det = s.det(s.Matrix.hstack(*[a[j] - a[0] for j in (1, 2, 3)]))
        assert clean(det**2 - 36*vol**2) == 0
        z = sum(a, s.zeros(3, 1))
        g += vol*z/(4*V)
        W += vol*(z*z.T + sum((v*v.T for v in a), s.zeros(3)))/(20*V)
    g = g.applyfunc(clean)
    C = (W - g*g.T).applyfunc(clean)
    return clean(V), g, C


def convex_audit(vertices, facets):
    edges = set()
    for face in facets:
        a, b, c = [vertices[i] for i in face[:3]]
        n = (b-a).cross(c-a)
        assert n.dot(n) > 0
        h = n.dot(a)
        slacks = [h-n.dot(v) for v in vertices]
        if all(z <= 0 for z in slacks):
            slacks = [-z for z in slacks]
        assert all(z >= 0 for z in slacks)
        assert {i for i, z in enumerate(slacks) if z == 0} == set(face)
        for i, j in zip(face, face[1:] + face[:1]):
            edges.add(tuple(sorted((i, j))))
    assert len(vertices)-len(edges)+len(facets) == 2
    return [len(vertices), len(edges), len(facets)]


def point_support_ratio(vertices, g, C, index, n):
    y = vertices[index]-g
    assert clean(n.dot(y)) == 0
    a = max(clean(-n.dot(v-g)) for v in vertices)
    assert a > 0
    r2 = clean((y.T*C.inv()*y)[0])
    v = clean((n.T*C*n)[0])
    return clean(r2*v/a**2), r2, v, a


def imul(a, b):
    vals = [x*y for x in a for y in b]
    return min(vals), max(vals)


def peval_interval(expr, variable, lo, hi):
    out = (F(0), F(0))
    for c in s.Poly(expr, variable).all_coeffs():
        out = imul(out, (lo, hi))
        out = (out[0]+c, out[1]+c)
    return out


def variations(sturm, x):
    signs = [s.sign(p.subs(u, x)) for p in sturm]
    signs = [a for a in signs if a]
    return sum(a != b for a, b in zip(signs, signs[1:]))


def matrix_strings(M):
    return [[str(clean(M[i, j])) for j in range(M.cols)]
            for i in range(M.rows)]


def atan_interval(inv, terms=30):
    x = F(1, inv)
    a = sum(((-1)**j*x**(2*j+1)/(2*j+1) for j in range(terms)), F(0))
    b = a + (-1)**terms*x**(2*terms+1)/(2*terms+1)
    return min(a, b), max(a, b)


def cos_upper(x):
    assert 0 < x < 1
    return sum(((-1)**j*x**(2*j)/factorial(2*j) for j in range(5)), F(0))


def main():
    # All constants in the spherical-cap proof are checked by rational arithmetic.
    c = F(897, 100)
    r, abar = F(29949, 10000), F(10017, 10000)
    A, B, W = 4*r/3, 4*abar-1, r-2
    D2 = A*A+1
    Dlo, dhi, sq3hi, D2lo = F(8233, 2000), F(1461, 2000), F(26, 15), F(169, 10)
    assert r > 2 and abar > 1 and Dlo > 0 and 0 < dhi < 1
    assert Dlo**2 < D2 and B**2 < dhi**2*D2 and D2lo < D2
    assert sq3hi**2 > 3
    bracket = 4*W - 3*(3+dhi)/Dlo
    delta = clean(D2lo*(1-dhi)**3*bracket/(8*sq3hi))
    assert bracket > 0 and delta > F(3, 100)
    assert delta == F(158493720497709597, 5269120000000000000)
    c_cert = 9-delta
    threshold = max(r*r, 9/abar**2)
    assert threshold < c_cert < c
    # Independent polynomial integration check of the surface-cap formula.
    q, d, DD, WW = s.symbols('q d DD WW')
    integ = s.integrate((q-d)**2*(WW-3*q/DD), (q, d, 1))
    expected = (1-d)**3*(4*WW-3*(d+3)/DD)/12
    assert s.simplify(integ-expected) == 0

    # Genuine one-parameter quadrilateral pyramids, 0 < u < 1/3.
    b = (1+u)*(1-3*u)
    verts = [s.Matrix(z) for z in [(0,0,0), (1,0,0), (0,1,0), (0,0,1), (-u,b,0)]]
    V, g, C = moments(verts, [(0,1,2,3), (0,2,4,3)], [F(1,6), u/6])
    assert clean(V-(1+u)/6) == 0
    assert (g-s.Matrix([(1-u)/4, (1+u-3*u*u)/4, F(1,4)])).applyfunc(clean) == s.zeros(3,1)
    C80 = s.Matrix([
        [3*u*u+2*u+3, 9*u**3+12*u*u-4*u-1, u-1],
        [9*u**3+12*u*u-4*u-1, 3*(9*u**4+18*u**3-13*u*u+2*u+1), 3*u*u-u-1],
        [u-1, 3*u*u-u-1, 3]])
    assert (80*C-C80).applyfunc(clean) == s.zeros(3)
    n = s.Matrix([2+3*u, -1, -1])
    assert clean(n.dot(g)) == 0
    assert [clean(n.dot(v)) for v in verts] == [0, 2+3*u, -1, -1, -1]
    N = 12*u**3-11*u*u+2*u+1
    D = 36*u**3-11*u*u+2*u+1
    ratio = 9*(3*u+1)*N/(2*D)
    r2 = clean((g.T*C.inv()*g)[0])
    vn = clean((n.T*C*n)[0])
    assert clean(r2-15*N/D) == 0
    assert clean(vn-3*(3*u+1)/10) == 0
    assert clean(r2*vn-ratio) == 0
    assert s.expand(108*s.diff(D,u)-(108*u-11)**2-95) == 0
    Fcrit = 432*u**6-264*u**5+209*u**4-100*u**3-42*u*u+4*u+1
    assert clean(s.diff(ratio,u)-27*Fcrit/(2*D*D)) == 0
    sturm = s.sturm(Fcrit,u)
    assert variations(sturm,F(0))-variations(sturm,F(1,3)) == 1
    assert ratio.subs(u,0) == F(9,2) and ratio.subs(u,F(1,3)) == F(9,2)
    lo, hi = F(1,6), F(1,5)
    assert Fcrit.subs(u,lo) > 0 and Fcrit.subs(u,hi) < 0
    for unused in range(120):
        mid = (lo+hi)/2
        if Fcrit.subs(u,mid) > 0:
            lo = mid
        else:
            hi = mid
    numlo, numhi = peval_interval(9*(3*u+1)*N,u,lo,hi)
    denlo, denhi = peval_interval(2*D,u,lo,hi)
    assert numlo > 0 and denlo > 0
    maxlo, maxhi = numlo/denhi, numhi/denlo
    max_decimal = [F(6131145332531,10**12), F(6131145332533,10**12)]
    assert max_decimal[0] < maxlo < maxhi < max_decimal[1]
    root_decimal = [F(177618408377203,10**15), F(177618408377205,10**15)]
    assert root_decimal[0] < lo < hi < root_decimal[1]

    samples = []
    facets = [(0,1,2,4), (0,1,3), (1,2,3), (2,4,3), (4,0,3)]
    for uu, expected_ratio in [(F(1,6),F(1053,172)), (F(8,45),F(751249,122530))]:
        vv = [v.subs(u,uu) for v in verts]
        gg, CC, nn = g.subs(u,uu), C.subs(u,uu), n.subs(u,uu)
        fvector = convex_audit(vv,facets)
        assert fvector == [5,8,5]
        assert all(CC[:k,:k].det() > 0 for k in (1,2,3))
        rr, rrsq, nv, support = point_support_ratio(vv,gg,CC,0,nn)
        assert rr == expected_ratio and rr > 6 and support == 1
        samples.append({'u':str(uu), 'volume':str(V.subs(u,uu)), 'f_vector':fvector,
                        'centroid':matrix_strings(gg), 'covariance':matrix_strings(CC),
                        'raw_normal':matrix_strings(nn), 'ratio':str(rr),
                        'whitened_point_norm_squared':str(rrsq), 'normal_variance':str(nv)})

    # Full-dimensional simplicial bipyramids approach the pyramid values.
    zeta = s.symbols('zeta', positive=True)
    bb = (1+zeta)*(1+u)*(1-3*u)
    vv_family = [s.Matrix(z) for z in
                 [(0,0,0),(1,0,0),(0,1,0),(0,0,1),(-u*(1+zeta),bb,-zeta)]]
    VZ, gZ, CZ = moments(vv_family,[(0,1,3,4),(2,1,3,4)],
                         [bb/6,3*u*(1+zeta)*(1+u)/6])
    NZ = (1+zeta)**2*N + 12*zeta*u*(u-1)
    DZ = (1+zeta)**2*D + 12*zeta*u*(3*u-1)
    RZ = 9*(3*u+1)*NZ/(2*DZ)
    assert clean(n.dot(gZ)) == 0
    assert clean((n.T*CZ*n)[0]-vn) == 0
    assert clean((gZ.T*CZ.inv()*gZ)[0]-15*NZ/DZ) == 0
    assert clean(s.diff(RZ,zeta)-108*u*u*(zeta-1)*(zeta+1)*(u+1)**2*(3*u+1)/DZ**2) == 0
    bipyramid_samples = []
    bfaces = [(0,1,4),(0,3,4),(0,1,3),(2,1,4),(2,3,4),(2,1,3)]
    for zz, target in [(F(1,100),F(7540947049,1239848530)),
                       (F(1,1000),F(751526809249,122674382530))]:
        sub = {u:F(8,45),zeta:zz}
        vv = [v.subs(sub) for v in vv_family]
        gg, CC, nn = gZ.subs(sub),CZ.subs(sub),n.subs(sub)
        assert convex_audit(vv,bfaces) == [5,9,6]
        rr, unused1, unused2, aa = point_support_ratio(vv,gg,CC,0,nn)
        assert rr == target and rr > 6 and aa == 1
        bipyramid_samples.append({'u':'8/45','zeta':str(zz),'ratio':str(rr),
                                  'volume':str(VZ.subs(sub)),'f_vector':[5,9,6]})

    # Preserve the material nonrecord: a true triangular bipyramid, not a free mass model.
    vv = [s.Matrix(z) for z in [(0,3,0),(-1,-1,-1),(-1,-1,1),(2,-1,0),(-1,-2,0)]]
    VB, gB, CB = moments(vv,[(0,1,2,3),(4,1,2,3)],[F(4),F(1)])
    fb = convex_audit(vv,[(0,1,2),(0,2,3),(0,3,1),(4,1,2),(4,2,3),(4,3,1)])
    yy = vv[0]-gB
    nn = s.Matrix([yy[1],-yy[0],0])
    rb, rrb, nb, ab = point_support_ratio(vv,gB,CB,0,nn)
    assert rb == F(2199289,424194) and fb == [5,9,6]

    # Recheck the inherited trigonometric rational upper bounds independently.
    lo5, hi5 = atan_interval(5)
    lo239, hi239 = atan_interval(239)
    pi_lo, pi_hi = 16*lo5-4*hi239, 16*hi5-4*lo239
    decimal_lo = F(3141592653589793,10**15)
    decimal_hi = F(3141592653589794,10**15)
    assert decimal_lo < pi_lo < pi_hi < decimal_hi
    p0, q0 = F(7024915,10**6), F(6832329,10**6)
    assert 9*cos_upper(decimal_lo/20)**20 < p0
    assert 9*cos_upper(decimal_lo/18)**18 < q0
    p, q0 = F(299,300)*p0, q0
    DD = p*q0+q0+1
    DB = p*q0+p+1
    assert p == F(420089917,60000000)
    assert p*q0 == F(956730840842231,20000000000000)
    assert 1/DD == F(20000000000000,1113377420842231)
    assert 1/DB == F(60000000000000,3350282439526693)
    report = {
        'object':'JOINT_SUPPORT_SECTION_897_AND_PYRAMID_COUNTERCONTROL_V1',
        'cap_delta_lower':str(delta), 'closed_universal_upper':str(c_cert),
        'convenient_strict_upper':str(c), 'threshold':str(threshold),
        'pyramid_family_critical_polynomial':str(Fcrit),
        'unique_maximizer_bracket':[str(z) for z in root_decimal],
        'family_maximum_bracket':[str(z) for z in max_decimal],
        'actual_pyramid_samples':samples,
        'actual_near_pyramid_bipyramids':bipyramid_samples,
        'actual_bipyramid_nonrecord':{'volume':str(VB),'f_vector':fb,'ratio':str(rb),
                                     'centroid':matrix_strings(gB),'covariance':matrix_strings(CB)},
        'finite_height_V10_F9':{'primal_gap_upper':str(p),'polar_gap_upper':str(q0),
                              'condition_upper':str(p*q0),'trace_floor':str(1/DD),
                              'inverse_trace_floor':str(1/DB),'trace_ceiling':str(p*q0/DD),
                              'floor_dual_alpha':str(1/(DD-3))},
        'exact_checks':'PASS'}
    print(json.dumps(report,sort_keys=True,indent=2))
    print('JOINT_SUPPORT_SECTION_897_AND_PYRAMID_COUNTERCONTROL_V1 PASS')


if __name__ == '__main__':
    main()
```
