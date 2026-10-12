# minimum-0147

AI research report · 2026-09-20 UTC · [Export notes](../../catalog/coverage.md#text-records)

<!-- historical-status:start -->
> **Historical AI report.** The title and claims below reflect the AI’s assessment at the time. Claims of proof, certification or completion are not a current verification verdict.
>
> Minimum’s C≥34 remains a working lower bound requiring a consolidated proof. [C622](../../C622/README.md) passes the supplied exact checks. See [verification status and source gaps](../../catalog/coverage.md).
<!-- historical-status:end -->

---

# ONE_ZERO_HOMOTHETIC_SHELL_VALUE_AND_AUXILIARY_ELIMINATION_V1

## 1. Result and scope

The unrestricted one-zero endpoint problem is **not resolved** here. The new result is a complete sharp value theorem for an infinite-dimensional subclass that allows arbitrarily many positive-ell auxiliary vertices, curved boundary profiles, and unbounded auxiliary geometry before optimization.

The subclass consists of bodies whose ell-level sections are homothetic triangular shells, with the largest ell-value attained at the canonical common-edge endpoint A. Its precise definition is in Section 2. No transformation of a general convex body into this subclass is asserted.

**Value theorem.** In this entire marked support-patch class, with `a>b>0`, `c=0`, and `0<d<=a`,

    T < Cstar < 203/100 < 51/25,

where

    Cstar = max H(b,rho),
    H(b,rho) = 2(1-b^2)(1-b rho^3)
               /[(1-b rho^2)(1-b^2 rho^2)],
    0<b<1, 0<rho<1.

The accepted two-anchor calculation gives

    2.0287830356734117251411563027
      < Cstar <
    2.0287830356734117251411563029.

The constant is sharp as a supremum even in the positive-d subclass. It is not attained there. A maximizing sequence can have a genuine positive-ell auxiliary vertex while d tends to zero. In the closed class allowing d=0, a global maximizer exists and is a six-vertex, root-only two-anchor body. This conclusion is proved by actual body variations, not by applying a local theorem to fixed-vertex-count approximants.

There is also an explicit proper-pair consequence. If P is any positive-root body in the subclass, q is any relative-interior root point with positive x and y, and

    K_lambda = conv(Tetra, lambda P+(1-lambda)q),
    9993/10000 <= lambda < 1,

then K_lambda has the genuine maximal coordinate triangles ABC and ABD, retains the same endpoint values and a positive-area root, and satisfies

    T(K_lambda) < 20300/9951 < 51/25.

The second inequality has exact gap `1/248775`. These proper bodies generally no longer have homothetic sections. Thus the result includes an explicit three-dimensional family of proper resolutions, not just limiting marked patches.

The main mechanism is new: the positive root-cut integral forces a one-sign-change condition for a profile variation. Actual curvature-measure variations then make the entire lower profile linear and permit only one upper-profile corner, at the marked D height. A four-parameter exact comparison shows that this remaining positive-ell roof cannot beat the two-anchor value.

## 2. Exact class and original uniform moments

Normalize a=1 by dividing ell and n by a. This does not change T. Write

    alpha=1-b, h=1+b,
    ell=1+(d-1)x-y-alpha z,
    n=h x+(h+d)y,
    A=(0,0,0), B=(0,0,1), C=(0,1,0), D=(1,0,0).

Here `0<b<1`, `0<=d<=1`, and `Tetra=conv(A,B,C,D)`.

The theorem concerns bounded full-dimensional convex bodies P containing Tetra, lying in `x,y,ell>=0`, and satisfying `ell<=1` throughout P. Thus the largest ell-value is the canonical value at A. Introduce the actual affine coordinates

    w=ell(x,y,z),
    z=[1+(d-1)x-y-w]/alpha.

Their Jacobian has absolute value alpha. The additional geometric assumption is that for some constant `kappa>0`, the image K of P is exactly

    K = {x,y>=0, 0<=w<=1,
         L(w)<=x/kappa+y<=U(w)},                       (2.1)

where L is nonnegative and convex, U is concave, and the corresponding planar region is closed. These are actual filled sections, not independently assigned section masses. The profiles can be nonsmooth and need not be piecewise linear.

Canonical containment means

    L(1)=L(b)=0,
    L(0)<=1<=U(0),
    L(d)<=1/kappa<=U(d).

Convexity and nonnegativity give `L=0` on `[b,1]`. A positive-area root is equivalent to `L(0)<U(0)`. For attainment we initially allow the equality case as well.

Conversely, these profile conditions define a convex body: (2.1) is the intersection of the quadrant with the inverse image of the convex planar region between L and U. The inverse affine map gives the original uniformly filled P. Both canonical triangles are genuine contained support patches. With positive root area they are strict patches in the coordinate faces, rather than whole triangular facets.

Put

    A2 = integral_0^1 (U^2-L^2) dw,
    A3 = integral_0^1 (U^3-L^3) dw,
    B2 = integral_0^1 w(U^2-L^2) dw.

Direct integration over each filled triangular shell gives the ORIGINAL volume and first moments:

    V = kappa A2/(2 alpha),
    X = integral_P x = kappa^2 A3/(6 alpha),
    Y = integral_P y = kappa A3/(6 alpha),
    E = integral_P ell = kappa B2/(2 alpha),
    Z = integral_P z = [V+(d-1)X-Y-E]/alpha,
    N = integral_P n = hX+(h+d)Y.                    (2.2)

Consequently

    T = alpha [h+(h+d)/kappa] A3/(9 A2 B2).           (2.3)

The actual centroid is `(X,Y,Z)/V`. None of the variations below holds it fixed. The curvature measures introduced later represent convex functions; they are not physical volume densities.

The C/D-reflected theorem follows by interchanging x and y, and c and d.

## 3. Inherited premises and input status

The complete current journal update, its literal parent payload, and the new coordinator source were read through EOF in the preceding unfinished attempt. This continuation used that completed reading and the unchanged sources already supplied in this chat.

The parent is `HIGH_TRACE_VARIABLE_ENDPOINT_LOCALIZATION_16_V1`, assignment `minimum-0142`, advertised assignment SHA-256

    8fb94d359f15a77c8c5b7d6b1395ea099a9bbaecc6be1bbb741498706df275c2.

The new coordinator source is `GLOBAL_HIGH_TRACE_ATTAINMENT_AND_ROOT_CUT_FIRST_VARIATION_V1`, material `[internal-source-reference]`, 15603 bytes, SHA-256

    52786c239b2ed0a438f276cb7c2baa108b5617168f5398a25da747e2b7515379.

The following accepted mathematical premises are used explicitly:

1. The actual fixed-patch cone-tail and joint-mass inequalities from `[internal-source-reference]` and `[internal-source-reference]`, including their arbitrary-convex-body scope.
2. The closed endpoint flux inequality and complete original-body root-shave identity in the accepted parent and coordinator source.
3. The balanced proper-pair bound `T<=2` when `a=b` and `0<=c,d<=a`, recorded in the shared notebook.
4. The explicit two-anchor scalar result `max H=Cstar<203/100`, recorded in notebook Section 69 under `minimum-0131`, SHA-256 `d3756f66557a0c54904607b6213c9e6307c97e45dfc49c2b044b0538c73ac499`.

The last premise is a stated accepted scalar theorem. Its old optimizer certificate and complete source are not newly attached, and no reconstruction of those unavailable bytes is claimed. The new domination theorem below reduces to the displayed H itself, so its exact mathematical dependency is explicit.

The thirteen-vertex theorem is not invoked in the profile proof. In particular, a maximum within the profile subclass is never promoted to a maximum among all convex bodies.

## 4. Genuine attainment in the closed profile class

A slightly weaker tail estimate than the target-specific bound supplies compactness already above trace 2. This is useful because Cstar lies below 51/25.

For the two fixed triangle patches let

    m_x=X/(2V^2), m_y=Y/(2V^2), m=m_x+m_y,
    h_V=1/(6V).

The inherited joint-mass inequality is

    m <= 3(1+h_V)/4 <= 3/2.                           (4.1)

Normalize ell by its true mean. At threshold `s=11/8`, put

    U_tail=(21/32)^4=194481/1048576.

The two actual patch cones and the global affine-tail bound give

    (m/3) K(T/m,s) <= U_tail,
    K(z,s)=integral_0^1 3r^2(1+r(z-1)-s)_+ dr.

Using only `v_+>=v` in this integral yields

    T/4 - 3m/8 <= U_tail.

Together with (4.1), this proves the general marked-body estimate

    1/(6V) >= (8/9)(T-489393/262144).                 (4.2)

In particular, every body with `T>=2` satisfies

    6V <= Bstar := 294912/34895,
    V <= 49152/34895.                                (4.3)

This estimate is not an all-level volume bound. At 51/25 the previously accepted target-specific bound remains stronger.

For a body containing Tetra in the quadrant, the exact one-point hull formula gives

    x+y <= 6V,  1-6V <= z <= 6V-x-y                   (4.4)

at every point of P. Thus (4.3) gives a common Euclidean container.

The endpoint flux inequality gives

    min(1,b) >= 4 mean_P(ell)(T-2).                   (4.5)

Since `E>=1/24` and V is bounded above, b stays away from zero on any fixed trace superlevel strictly above 2. The limit b=1 is also excluded from such a maximizing sequence by the balanced bound `T<=2`, because here `0<=d<=1`.

For completeness, only the proper-pair version of that balanced bound is needed. A balanced marked body can be approximated by bodies with a positive root triangle and then by proper marked resolutions. A small root triangle near C can be added inside the protected wedge, and the root-centered contraction toward a positive-x,y root point restores the exact coordinate triangles. All added points have ell=0 and all contracted points retain `ell<=1`. The actual volume moments converge. Therefore the non-strict bound `T<=2` passes to the balanced patch limit, including a collapsed root. No limit of strict inequalities is used to claim a strict balanced gap.

The aspect ratio also stays nondegenerate. Since C lies in the root, `U(0)>=1`, and the root x-intercept is `kappa U(0)`, (4.4) gives `kappa<=Bstar`. The presence of D and the y-intercept at its height give `kappa>=1/Bstar`.

Now take a maximizing sequence in the closed profile class. There is an explicit member with trace above `101/50`: the root-only profile with

    b=1/5, rho=4/5, d=0, kappa=1,
    U(w)=1-w,
    L(w)=rho(1-w/b)_+

has

    T=44880/22127 > 101/50.

Thus the maximizing sequence can be chosen in that fixed superlevel. It has a Hausdorff-convergent subsequence, convergent endpoint parameters, and convergent kappa. The limits b=0 and b=1 have just been excluded.

For `0<b<1`, the affine map to `(x,y,w)` remains invertible. The shell property is closed: project K to the compact convex region in coordinates `(x/kappa+y,w)`. Convergence of that region and of kappa recovers the entire filled shell by distributing each nonnegative s between x/kappa and y. This proves Hausdorff convergence of the reconstructed shells, including endpoint sections.

All original integrals in (2.2) are continuous under this bounded Hausdorff convergence. The retained tetrahedron gives `V>=1/6` and `E>=1/24`. Hence the ratio has a genuine global maximizer in the closed profile class. Bodies outside the chosen superlevel have smaller trace, so the container has not constrained an improving variation.

## 5. Optimizing the actual marked patches

At a global maximum, the marks can be normalized further without assuming they were vertices initially.

First, B is the bottom point of the actual axis segment. To see this directly, hold the filled K fixed and choose a smaller admissible b. Formula (2.3), before eliminating kappa, has numerator proportional to

    (1-b^2) integral_K x
      + [1-b^2+d(1-b)] integral_K y.

It strictly increases when b decreases from a positive value. All moments of the newly normalized physical P are still the actual affine images of K. Consequently, at the maximum,

    L(w)>0 for 0<=w<b,
    L(w)=0 for b<=w<=1.                              (5.1)

Second, C must be the outer endpoint of the root section in x=0. Replacing C by `(0,U(0),0)` in level coordinates and affinely normalizing the new tetrahedron multiplies the first marked-patch numerator contribution by U(0), while leaving the other contribution unchanged. It is a valid support triangle in the same filled body. Since `U(0)>=1`, maximality gives

    U(0)=1.                                         (5.2)

This re-marking need not contain the old triangle. Its trace change follows from the actual triangle area times its affine ell-average, not from an assumed containment of triangles.

Third, at the same height d, D must be the outer x-intercept. Moving it to that intercept and normalizing x increases the second marked-patch contribution unless it was already outer. Thus

    kappa U(d)=1.                                   (5.3)

This does not require maximizing over the height d. Subsequent profile variations hold d fixed and reset kappa according to (5.3).

Write

    rho=L(0),
    r=N/V, q=N/E,
    k=[h kappa+h+d]/2,
    g=n-r-q ell.

The root will shortly be shown to have positive area. Then (5.1) gives `0<rho<1`.

## 6. The root-shave variation stays inside this class

This is the step that licenses the sign condition used in the free-boundary proof.

For small positive epsilon, cut the original body at `ell>=epsilon`. Slide C toward A to

    C_epsilon=(1-epsilon)C+epsilon A.

If d=0, also slide D toward A in the same way. Otherwise retain D and choose epsilon<d. Retain A and B. Put

    s_C=1-epsilon,
    s_D=1-epsilon if d=0, otherwise 1.

The actual canonical affine normalization is

    Phi(x,y,z)=(x/s_D,y/s_C,z),
    j=1/(s_C s_D).

Let the lost region have actual integrals `w_R,J_R,E_R`, and put

    V_minus=V-w_R,
    J_minus=J-J_R=(X_minus,Y_minus,Z_minus),
    E_minus=E-E_R.

Before the harmless final scaling of ell, the normalized body has exactly

    V_new=j V_minus,
    J_new=j Phi J_minus,
    E_new=j(E_minus-epsilon V_minus),
    N_new=j[(a_new+b_new+c_new)X_minus/s_D
            +(a_new+b_new+d_new)Y_minus/s_C],         (6.1)

with endpoint values

    a_new=1-epsilon, b_new=b-epsilon, c_new=0,
    d_new=d-epsilon if d>0, otherwise 0.

Equivalently, its trace is

    T_epsilon=[Kx X_minus+Ky Y_minus]
               /[6V_minus(E_minus-epsilon V_minus)],

    Kx=h-(3+b)epsilon+2epsilon^2,
    Ky=h+d-3epsilon                         if d>0,
    Ky=h-(3+b)epsilon+2epsilon^2             if d=0. (6.2)

These are changes of actual uniformly filled bodies and actual selected triangles.

After scaling the new maximum ell-value back to one, the profiles are

    w'= (w-epsilon)/(1-epsilon),
    kappa'=kappa s_C/s_D,
    L'(w')=L(epsilon+(1-epsilon)w')/s_C,
    U'(w')=U(epsilon+(1-epsilon)w')/s_C.              (6.3)

Thus convexity, concavity, the full-shell property, and the condition that the maximum ell-value is the A value all survive. The new C mark need not be outer, which is allowed in the optimization class. The d=0 and d=1 boundaries are both respected.

The slice formulas in (2.2) give the lost volume and moments by integrating over `0<=w<epsilon`. They remain valid for nonsmooth profiles. Continuity of the endpoint profiles gives loss `o(epsilon)` when the root area is zero. For a positive root the first-order losses are its actual section area and first moments; the loss of the ell-integral is `O(epsilon^2)`.

The inherited exact root-cut identity, or differentiation of (6.1)-(6.2), therefore gives

    dT_epsilon/depsilon at 0
      = [T-m-(b/3)m_0]/mean_P(ell) - G_F/(6VE),

    m_0=m_x+1_{d=0}m_y,
    G_F=integral_F g/|grad ell| dA.                  (6.4)

Since `m_0<=m<=3/2` and `b<=1`, the bracket is at least `T-2`. At a maximum with T>2, (6.4) first excludes root-area collapse and then proves

    G_F >= 6V^2[T-m-(b/3)m_0] >0.                   (6.5)

In the shell coordinates, the area distortion from the root xy-plane is constant. Hence its actual area mean of n is

    mean_F n
      = (2k/3)(1-rho^3)/(1-rho^2)
      = (2k/3)(1+rho+rho^2)/(1+rho)
      < k.

On the root, g=n-r. Consequently the decisive sign is

    r < mean_F n < k.                               (6.6)

No root area has been substituted for a volume integral in obtaining this inequality.

## 7. All lower-profile auxiliary geometry disappears

We now work at the genuinely attained joint maximum. Every convex nonincreasing lower profile satisfying (5.1) has a representation

    L(w)=integral_(0,b] (1-w/t)_+ dmu(t),
    mu((0,b])=rho.                                  (7.1)

For a nonsmooth profile this is its derivative Stieltjes measure: in the interior, `dmu(t)=t dL'(t)`, with the appropriate nonnegative terminal atom at b. Finite endpoint continuity excludes an atom at zero. The formula also follows by integrating the monotone derivative. It does not assign a new physical density to P.

Replace a small fraction of mu by a point mass at any `t in (0,b]`, preserving its total mass. This is an actual convex-profile variation. It preserves the root value rho and all canonical points. Indeed,

    L(w)<=rho(1-w/b)_+ < U(w)  for 0<=w<1,

because `U(w)>=1-w` and rho<1. Small variations retain the actual axis endpoint b.

The exact first derivative of the original moment ratio has the sign of the frozen variation of `N-rV-qE`. For a lower-profile variation it is

    -kappa integral_0^b p_L(w) delta L(w) dw,
    p_L(w)=L(w)[kL(w)-r-qw].                         (7.2)

Thus the derivative associated with unit mass at t is, up to a fixed positive factor,

    K_L(t)=-integral_0^t p_L(w)(1-w/t) dw.

At maximality, mu is supported on global maximizers of K_L in `(0,b]`.

Now `kL(w)-r-qw` is strictly decreasing, because L is nonincreasing and q>0. Therefore p_L is either negative throughout, or changes sign exactly once from positive to negative. Moreover,

    K_L'(t)=-(1/t^2) integral_0^t w p_L(w) dw.        (7.3)

The cumulative integral in (7.3) is either always negative, or first increases and then decreases, crossing zero at most once. Hence K_L is either strictly increasing, or first decreases and then increases. Its maximum on `[0,b]` occurs at an endpoint. The endpoint value at zero is zero, but zero is not an admissible support point of mu. If it were strictly larger than K_L(b), arbitrarily small positive t would contradict maximality of the existing measure. The only possible support is therefore b.

We have proved

    L(w)=rho(1-w/b)_+.                               (7.4)

This removes an arbitrary lower-profile curvature measure, not just finitely many preselected vertices.

## 8. The upper profile has only the marked D corner

Using (5.3), the exact trace becomes

    T=alpha Z_D A3/(9 A2 B2),
    Z_D=h+(h+d)U(d),
    k=Z_D/[2U(d)].                                  (8.1)

When U varies, change kappa to `1/U(d)` so that D remains the actual outer endpoint at height d. This is an actual affine change of the filled shell, already included in the moments (2.2).

For a variation `delta U=psi`, differentiation of (8.1) gives

    T'/T = [3/(k A3)]
           [integral_0^1 p_U(w) psi(w) dw
            +gamma psi(d)],

    p_U(w)=U(w)[kU(w)-r-qw],
    gamma=A3(h+d)/[6U(d)]>0.                         (8.2)

The positive point reaction gamma is fixed by the true marked-patch normalization. It is not an adjustable multiplier or an independent mass.

Let `nu=-U''` be the nonnegative distributional curvature measure. With

    G(w,t)=min(w,t)[1-max(w,t)],

one has

    U(w)=1-w+U(1)w+integral_(0,1) G(w,t) dnu(t).       (8.3)

The measure need only be locally finite; the Green integral is finite. Adding a small nonnegative curvature atom preserves concavity. Removing a small fraction of nu on a compact subinterval also remains admissible: the gap from the lower profile is bounded below by `(1-rho)(1-w)`, and the relevant Green perturbation is bounded by a constant times `1-w`.

Define

    H_U(t)=integral_0^1 p_U(w)G(w,t) dw+gamma G(d,t).

The preceding actual-body variations prove

    H_U(t)<=0 for 0<t<1,
    H_U=0 nu-almost everywhere.                      (8.4)

It satisfies

    H_U(0)=H_U(1)=0,
    H_U''=-p_U-gamma delta_d                         (8.5)

in the interior, omitting the point mass when d is an endpoint.

By (6.6), `kU(0)-r=k-r>0`. The function

    kU(w)-r-qw

is concave. Its sign is positive on an initial interval and, if it becomes negative, stays strictly negative thereafter. Thus p_U has the sign pattern positive-then-negative.

Starting at zero, H_U is strictly concave on the initial positive-p_U interval. Since H_U<=0, it is strictly negative there. A negative derivative jump at d only strengthens that conclusion when d is in this initial interval. On the remaining intervals H_U is strictly convex, so it cannot attain the interior maximum zero. The only possible interior zero is the downward corner at d itself. Consequently

    support(nu) subset {d}.                          (8.6)

This argument includes singular continuous curvature and infinitely many potential profile corners.

If `0<=d<1` and `U(1)>0`, the two-sided affine variation `psi(w)=w` is admissible. Equation (8.2) then gives `H_U'(1)=0`. The sign pattern and (8.4) force p_U to be negative near 1; otherwise H_U would be strictly concave with two zero endpoint values and positive interior values. But with p_U negative near 1, equations `H_U(1)=H_U'(1)=0` and `H_U''>0` make H_U positive immediately to the left of 1. This contradicts (8.4).

Therefore

    U(1)=0 for 0<=d<1.                               (8.7)

For d=0, (8.6) has no interior support, so

    U(w)=1-w, kappa=1.

For `0<d<1`, write `u=U(d)>0`. Equations (8.6)-(8.7) give the exact two-segment profile

    U(w)=1+(u-1)w/d                 for 0<=w<=d,
    U(w)=u(1-w)/(1-d)               for d<=w<=1,
    u>=1-d,
    kappa=1/u.                                      (8.8)

At d=1, the curvature support is again empty, and the remaining case is

    U(w)=1+(u-1)w, u=U(1)>0, kappa=1/u.              (8.9)

Thus all d=1 boundary maxima are included. No positive-root maximum has been discarded at that endpoint.

## 9. Exact value comparison for the remaining positive-ell roof

The profiles (7.4), (8.8), and (8.9) define actual convex bodies for

    0<b<1, 0<rho<1, 0<d<=1, u>0, u>=1-d.

Their original moments are given by (2.2), with

    D_V=u^2+d(1+u)-b rho^2,
    D_E=u^2(1+2d)+d^2(1+2u)-b^2 rho^2,
    D_N=u^3+d(1+u+u^2)-b rho^3,

    V=D_V/(6 alpha u),
    E=D_E/(24 alpha u),
    X=D_N/(24 alpha u^2),
    Y=D_N/(24 alpha u),
    Z=[V+(d-1)X-Y-E]/alpha,

    T=alpha [h+(h+d)u]D_N/(D_V D_E).                 (9.1)

These formulas include the d=1 cap and all facet-merger seams.

**Exact comparison lemma.** Every body in (9.1) satisfies

    T < H(b,rho)                                    (9.2)

when d>0.

Here is a complete algebraic proof. Set

    A0=1-b rho^3, B0=1-b rho^2, C0=1-b^2 rho^2,
    delta=u+d-1>=0,
    l1=2-d,
    e1=2(1+d-d^2), e2=1+2d,
    c1=3-3d+d^2, c2=3-2d,
    K0=2h-d(b+d), k1=h+d.

Then

    D_V=B0+l1 delta+delta^2,
    D_E=C0+e1 delta+e2 delta^2,
    D_N=A0+c1 delta+c2 delta^2+delta^3,
    h+(h+d)u=K0+k1 delta.

The desired difference has positive denominator and numerator

    P(delta)=2h A0 D_V D_E
              -(K0+k1 delta)D_N B0 C0.

Write `P=sum_(j=0)^4 P_j delta^j`. Its constant coefficient is

    P_0=d(b+d)A0 B0 C0>0.                            (9.3)

The other coefficients are

    P_1=2h A0(l1 C0+e1 B0)
         -B0 C0(k1 A0+K0 c1),
    P_2=2h A0(C0+l1 e1+e2 B0)
         -B0 C0(k1 c1+K0 c2),
    P_3=2h A0(l1 e2+e1)-B0 C0(k1 c2+K0),
    P_4=2h A0 e2-k1 B0 C0.                           (9.4)

All are nonnegative. The following inequalities and identities provide an explicit certificate without a numerical positivity test.

First,

    A0>=B0>=B0 C0>0,
    1/(B0 C0)>=1/B0+1/C0-1,
    2/B0+2/C0-3/A0>=1/h.                             (9.5)

For the last inequality, use A0>=B0 and the exact identity

    h(2B0-C0)-B0 C0
      =b(1-rho^2)(1+b^2 rho^2)>=0.

Put `s=d(1-2d/3)`. Since `l1-2c1/3=s`, `e1-2c1/3=4s`, `K0<=2h`, and `K0/h>=2-d`, (9.5) gives

    P_1/(A0 B0 C0)
      >=10h s+(2-d)c1/3-h-d
      >=(2-h)+(10h-8)d/3>=0.                         (9.6)

The second step uses `d^2<=d` and `d^3<=d` after expansion.

For P_2 put

    f=l1 e1=4+2d-6d^2+2d^3,
    Q2=k1 c1+K0 c2
      =9h+(6-10h)d+(3h-8)d^2+3d^3.

One has

    1+f-Q2/(3h)
      =2+(16/3-2/h)d+(-7+8/(3h))d^2+(2-1/h)d^3
      >=2/3.

Apply (9.5) first to `Q2/A0` and then to `1/(B0 C0)`. The coefficients of both `1/B0` and `1/C0` are nonnegative by the preceding inequality. Replacing them by their lower value at one gives

    P_2/(A0 B0 C0)
      >=2h(2+2d+f)-Q2(4h-1)/(3h)
      >=3+[(16h^2+h-2)/(3h)]d
           +(4h-4+1/h)d^3
      >0.                                           (9.7)

Again the last step follows by replacing the negative d-squared term by its lower bound using `d^2<=d`.

Finally, `A0>=B0 C0` directly gives

    P_3/(B0 C0)>=3h+(5h-1)d>0,
    P_4/(B0 C0)>=h+(4h-1)d>0.                        (9.8)

All these bounds use only `1<=h<=2` and `0<=d<=1`. Equations (9.3)-(9.8) prove `P(delta)>0` for every d>0 and delta>=0, establishing (9.2).

In particular the normal-form deficit has the explicit lower bound

    H(b,rho)-T
      >= alpha d(b+d)A0/(D_V D_E)>0.                 (9.9)

This deficit is asserted for the normal form, not for arbitrary profiles at their original fixed parameters.

The competitor giving H is an actual different body: use d=0, kappa=1, `U=1-w`, and `L=rho(1-w/b)_+`. Its original moments are

    V0=B0/(6 alpha), E0=C0/(24 alpha),
    X0=Y0=A0/(24 alpha),
    Z0=(4B0-2A0-C0)/(24 alpha^2).

Thus (9.2) is not deletion of auxiliaries at a fixed root. The root plane, endpoint value d, and all uniform moments are recomputed.

## 10. Assembly, sharpness, and the endpoint boundary

The closed profile class has a genuine global maximum above 101/50. Its root is positive, its common-edge endpoints satisfy `0<b<1`, and its marks satisfy (5.1)-(5.3). The nonsmooth profile variations reduce it to (7.4) and either (8.8) or (8.9).

If its d were positive, (9.2) would supply an admissible root-only body in the same closed class with strictly larger trace. This contradicts global maximality. Therefore every global maximum has

    d=0, kappa=1,
    U=1-w, L=rho(1-w/b)_+.

Its trace is H. Conversely all these root-only bodies belong to the class. Hence the global maximum is exactly Cstar.

If a positive-d body attained Cstar, it would itself be a global maximum and would satisfy the same normal-form argument, contradicting (9.2). Therefore every positive-d body has `T<Cstar`.

The bound is sharp as a supremum on the open positive-d stratum. In (9.1), set u=1 and let d decrease to zero. For any fixed b,rho the trace tends to H(b,rho). Taking b,rho at, or approaching, the maximizer of H gives trace tending to Cstar while a positive-ell auxiliary is present for every d>0. The root area need not collapse. Instead D reaches the root, the positive-ell auxiliary approaches C, and the eight-vertex roof limits to the six-vertex root-only body.

Thus this proof explicitly encounters and resolves the d=0 boundary. It does not assume that a maximum exists in the open positive-d subclass.

## 11. Uniform transfer to genuine maximal triangles

Let P be any positive-root shell body, not necessarily polyhedral. Choose q in the relative interior of its root with positive x,y, and put

    H_lambda=lambda P+(1-lambda)q,
    K_lambda=conv(Tetra,H_lambda), 0<lambda<1.

All points of H_lambda have strictly positive x and y. Hence

    K_lambda intersect {x=0}=ABC,
    K_lambda intersect {y=0}=ABD.

The root contains `lambda F+(1-lambda)q`, so it has positive area. These are genuine support-face statements, not combinatorial labels on a generating list.

The actual uniform integrals of H_lambda are

    V_H=lambda^3 V,
    J_H=lambda^4 J+lambda^3(1-lambda)Vq,
    E_H=lambda^4 E,
    N_H=lambda^4 N+lambda^3(1-lambda)n(q)V.

Moreover `H_lambda subset K_lambda subset P`. The moments of K_lambda are those of P minus the actual integrals over `P minus K_lambda`; its centroid is recomputed accordingly. Since ell and n are nonnegative,

    V_K>=lambda^3 V,
    E_K>=lambda^4 E,
    N_K<=N.

Therefore

    T(K_lambda)<=lambda^(-7)T(P).                    (11.1)

For `lambda>=9993/10000`, Bernoulli's inequality gives

    lambda^7>=1-7(1-lambda)>=9951/10000.

The sharp shell bound and `Cstar<203/100` now give

    T(K_lambda)<20300/9951<51/25,
    51/25-20300/9951=1/248775.                        (11.2)

This is a whole explicit proper-pair family with arbitrary auxiliary complexity and arbitrary positive-x,y root center q. It is not a claim that every proper pair is such a resolution, nor a claim of monotonicity of T under root contraction.

## 12. Exact non-root-only control and recovery data

The following rational member demonstrates that the sector genuinely contains a positive-ell auxiliary and trace above 2. It is not a counterexample to 51/25 and is not an equilibrium attainer.

Use

    b=1/5, d=1/1000, rho=4/5, u=1, kappa=1,
    ell=1-(999/1000)x-y-(4/5)z,
    n=(6/5)x+(1201/1000)y.

Its eight true vertices, with fixed labels, are

    0: (0,0,0)
    1: (0,0,1)
    2: (0,1,0)
    3: (1,0,0)
    4: (4/5,0,251/1000)
    5: (1,0,1/800)
    6: (0,4/5,1/4)
    7: (0,1,-1/800).

Vertex 7 is a genuine noncanonical positive-ell auxiliary, with `ell(7)=1/1000`. Vertex 3 is D and has the same positive ell-value. The root vertices are 4,5,2,6.

The complete maximal-facet cycles are

    (4,5,2,6)
    (0,7,2,6,1)
    (0,3,5,4,1)
    (5,3,7,2)
    (0,3,7)
    (1,4,6).

In that order, their inward halfspace descriptions are

    999x+1000y+800z <=1000,
    x>=0,
    y>=0,
    x+y<=1,
    y+800z>=0,
    749x+750y+800z<=800.

They give true `V/E/F=8/12/6`. The two coordinate faces are pentagons, not the canonical triangles.

The exact original uniform integrals are

    V=437/2400,
    J=(1501/32000,1501/32000,449561/9600000),
    centroid=(237/920,237/920,449561/1748000),
    E=976403/19200000,
    N=3603901/32000000,
    T=45522960/22457269.

In particular,

    2 < T < 44880/22127 < 203/100.

The middle comparison is to the actual two-anchor body at the same b,rho but d=0, not to deletion at the original root.

The literal rational data and formulas above are the primary recovery certificate. The following complete standard-library unit independently reconstructs the hull, all maximal facets, the positive tetrahedral volume fan, the actual first moment, and the trace. It has no external inputs or randomness. A completed machine-verification receipt for this new audit is not retained in this continuation; the verification claimed here is analytic, with this independent executable checker supplied rather than an unobserved digest or execution claim.

Target replay environment: CPython 3.13.5, standard library, assertions enabled. Save as `one_zero_shell_control.py` and run `python one_zero_shell_control.py`. The expected terminal marker is `ONE_ZERO_TRIANGULAR_SHELL_CONTROL_PASS 8 12 6`.

```python
from fractions import Fraction as F
from itertools import combinations

# Parent: minimum-0142.
# Exact new input: b=1/5, d=1/1000, rho=4/5, u=kappa=1.
P = [tuple(F(x) for x in row) for row in [
    ('0','0','0'), ('0','0','1'),
    ('0','1','0'), ('1','0','0'),
    ('4/5','0','251/1000'), ('1','0','1/800'),
    ('0','4/5','1/4'), ('0','1','-1/800')]]
FACETS = [(4,5,2,6), (0,7,2,6,1), (0,3,5,4,1),
          (5,3,7,2), (0,3,7), (1,4,6)]
PLANES = [((999,1000,800),1000), ((-1,0,0),0),
          ((0,-1,0),0), ((1,1,0),1),
          ((0,-1,-800),0), ((749,750,800),800)]


def sub(a,b):
    return tuple(x-y for x,y in zip(a,b))


def dot(a,b):
    return sum((x*y for x,y in zip(a,b)), F(0))


def cross(a,b):
    return (a[1]*b[2]-a[2]*b[1],
            a[2]*b[0]-a[0]*b[2],
            a[0]*b[1]-a[1]*b[0])


def det(a,b,c):
    return dot(a,cross(b,c))


def main():
    hull_faces=set()
    for i,j,k in combinations(range(len(P)),3):
        normal=cross(sub(P[j],P[i]),sub(P[k],P[i]))
        if normal==(0,0,0):
            continue
        rhs=dot(normal,P[i])
        vals=[dot(normal,v)-rhs for v in P]
        if all(t<=0 for t in vals) or all(t>=0 for t in vals):
            hull_faces.add(frozenset(i for i,t in enumerate(vals) if t==0))
    assert hull_faces=={frozenset(f) for f in FACETS}

    edges={}
    for face,(normal,rhs) in zip(FACETS,PLANES):
        assert {i for i,v in enumerate(P) if dot(normal,v)==rhs}==set(face)
        assert all(dot(normal,v)<=rhs for v in P)
        turns=[]
        for j in range(len(face)):
            a=P[face[j]]
            b=P[face[(j+1)%len(face)]]
            c=P[face[(j+2)%len(face)]]
            turns.append(dot(cross(sub(b,a),sub(c,b)),normal))
            e=tuple(sorted((face[j],face[(j+1)%len(face)])))
            edges[e]=edges.get(e,0)+1
        assert all(t>0 for t in turns) or all(t<0 for t in turns)
    assert len(edges)==12 and set(edges.values())=={2}
    assert len(P)-len(edges)+len(FACETS)==2

    for v in P:
        active=[n for n,rhs in PLANES if dot(n,v)==rhs]
        assert any(det(*triple)!=0 for triple in combinations(active,3))

    o=tuple(sum(v[j] for v in P)/len(P) for j in range(3))
    assert all(dot(n,o)<rhs for n,rhs in PLANES)
    V=F(0)
    J=(F(0),F(0),F(0))
    for face in FACETS:
        a=P[face[0]]
        for i in range(1,len(face)-1):
            b,c=P[face[i]],P[face[i+1]]
            vol=abs(det(sub(a,o),sub(b,o),sub(c,o)))/6
            assert vol>0
            V+=vol
            J=tuple(J[j]+vol*(o[j]+a[j]+b[j]+c[j])/4 for j in range(3))

    assert V==F(437,2400)
    assert J==(F(1501,32000),F(1501,32000),F(449561,9600000))
    assert tuple(x/V for x in J)==(F(237,920),F(237,920),F(449561,1748000))
    E=V-F(999,1000)*J[0]-J[1]-F(4,5)*J[2]
    N=F(6,5)*J[0]+F(1201,1000)*J[1]
    T=N/(6*V*E)
    assert E==F(976403,19200000)
    assert N==F(3603901,32000000)
    assert T==F(45522960,22457269)
    b,rho=F(1,5),F(4,5)
    H=2*(1-b*b)*(1-b*rho**3)/((1-b*rho**2)*(1-b*b*rho**2))
    assert H==F(44880,22127)
    assert F(2)<T<H<F(203,100)
    assert F(20300,9951)<F(51,25)
    print('ONE_ZERO_TRIANGULAR_SHELL_CONTROL_PASS 8 12 6')


if __name__=='__main__':
    main()
```

## 13. What was tried, what remains, and continuation

The successful direction was to keep the full positive-ell profile geometry rather than try another fixed-root deletion. Three exact uniform profile integrals expose a useful variational structure. The root-canonical point C, together with the admissible root shave, supplies the initial positive sign needed to control the outer forcing. The D normalization contributes a positive point reaction at its actual height. Those two geometric facts, not a free weighted relaxation, force the finite profile normal form.

The new result excludes all bodies of the form (2.1) with `max ell=a`, including nonpolyhedral profiles and arbitrarily many positive-ell auxiliaries, and the explicit proper-resolution collar (11.2). It does not establish that every one-zero body has this section form. No vertical Steiner operation or uniformly refilled projective image is used or licensed.

The genuinely remaining one-zero geometry includes changing transverse section shapes, changing ratios of the two coordinate intercepts, off-axis auxiliary vertices, and bodies with an auxiliary ell-height exceeding a. The accepted thirteen-vertex extremal skeleton does not itself remove these possibilities. This work also does not prove fixed-endpoint attainment, a finite monotone algorithm for arbitrary one-zero bodies, or a universal trace bound on the entire one-zero stratum.

The most useful continuation is to replace the constant-aspect shell by actual sections with nonproportional coordinate profiles while retaining three-dimensional convexity. The proof identifies a specific target: recover an exact positive mark-reaction term and enough sign control to constrain the remaining curvature. Optimizing two intercept functions or curvature measures as independent physical masses would lose the body coupling and is not justified.

The main theorem and quartic comparison are analytic and have not been independently refereed or proof-assistant formalized. The exact control has a complete literal recovery and analytic support/moment certificate; no numerical optimization result is used. There is no new actual trace counterexample, E17 exclusion, mechanical 110 attainer, or change to the accepted interval `34<=C_min<=622`.
