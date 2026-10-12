# material-e97d3774ae40

AI research material · [Export notes](../catalog/coverage.md#text-records)

<!-- historical-status:start -->
> **Historical AI material.** The title and claims below reflect the AI’s assessment at the time. Claims of proof, certification or completion are not a current verification verdict.
>
> [C622](../C622/README.md) passes the supplied exact checks; C<500 remains open; Minimum’s C≥34 remains a working lower bound requiring a consolidated proof. See [verification status and source gaps](../catalog/coverage.md).
<!-- historical-status:end -->

---

# Slab normal moments characterize scalar Brunn realization

## Status and why this is a new constraint

This coordinator theorem turns the sharp actual-facet normal variance curve into a complete one-coordinate realization criterion, under stated piecewise-smooth regularity. It does not characterize a full spatial joint law, a specified polyhedral incidence, a physical metric, or class110. The bounds34<=Cmin<=622 and canonical attainingC622 do not change.

The complete sharp normal comparison is [internal-source-reference], SHA984fc0c74293ab6727b77265c3e64e3011653d95d5c4ed3f6df94641f2e37c35. The actual all-apex/common-law theorem is the fully read immutable result minimum-0276, SHA08ba2642537a354443744c217de7b00b23a5e4e61bea4a3ea0f2931e867f36c0. Its projected countercontrols do not refute its full-spatial completeness theorem. The visible-coordinate projective invariance mechanism is preserved in [internal-source-reference]; a one-coordinate derivation is also given below.

The new exact countercontrol is different from the parent's density3/13(1+u^2/4): it is C1 and piecewise quadratic, passes the FULL sharp normal curve at both original endpoints, and passes all projected exponent-three apex and cross-apex tests, even after every positive one-coordinate projective refill. Nevertheless a genuine slab normal test rejects it. Thus checking the original whole-support normal moments once, even sharply, is not a replacement for actual sectional realization.

## 1. The sharp curve and slab data

For r>=0 put

A(r)=3(3r^2+2r+1)/[4(r^2+r+1)^2],
S(r)=3(r^4+4r^3+10r^2+4r+1)/[5(3r^2+2r+1)^2].

A maps[0,infinity) continuously and strictly decreasingly onto(0,3/4], with A(0)=3/4. Write F(alpha)=S(A^-1(alpha)). The prior theorem proves that every density rho whose square root is concave, after centring and rescaling its upper endpoint to1, satisfies variance>=F(endpoint density). A homothetic frustum attains equality for every alpha. In particular F(alpha)>=2alpha/3.

Let rho be a continuous positive density on the interior of a bounded interval I, with finite one-sided endpoint values. It need not initially have unit integral. For any closed subinterval J=[a,b] inside I, set

m0=int_a^b rho(x)dx,
mu=(int_a^b x rho(x)dx)/m0,
sigma2=(int_a^b(x-mu)^2 rho(x)dx)/m0,
h=b-mu,
alpha_J=h rho(b)/m0,
v_J=sigma2/h^2.

These are the mass-normalized and actual-centroid-normalized data of the slab. An arbitrary old centre, transported centre or adjustable endpoint measure is not used. For an actual uniformly filled convex3-body and a fixed linear coordinate x, intersection with the two planes x=a,b is an actual convex slab with those normal moments. The new cap x=b is a complete genuine facet of that slab whenever it has positive area. These are auxiliary slabs; their facet/vertex counts are not asserted to equal those of the original body.

Call J admissible for the sharp moment test when

0<alpha_J<=3/4 and v_J>=F(alpha_J).                         (1)

## 2. Equivalence theorem

Assume g=sqrt(rho) is continuous, piecewise C2 with finitely many breakpoints, has finite one-sided first derivatives there, and is positive in the interior. Endpoint values are their one-sided limits. Then the following are equivalent:

(a) g is concave on I.
(b) Every nondegenerate interior subinterval J satisfies(1).
(c) For every interior point x, all sufficiently small symmetric intervals[x-e,x+e] satisfy(1).
(d) After normalization, rho is the marginal of uniform volume on some compact convex3-body, for one nonconstant linear coordinate.

The implication(d)->(a) is Brunn-Minkowski sectional root concavity. The implication(a)->(b) is the already proved sharp actual normal comparison, applied directly to the restricted density. The implication(b)->(c) is immediate. The converse(c)->(a) follows from the exact local expansions below. Finally(a)->(d) has an explicit geometric construction: fix any centred convex planar body D containing0 and take

K={(x,y):x in I, y in g(x)D} subset R x R^2.

This is convex because g is nonnegative and concave and D is convex and contains0. Its section area is Area(D)g(x)^2, so its normalized uniform marginal is rho/int_I rho. Positivity of g on an interval makes K full-dimensional. This is an existence theorem for a convex body, not necessarily a polytope and not a body with prescribed incidence or equilibria.

### Smooth-point expansion

At a C2 point x0 put a=rho'(x0)/rho(x0), b=rho''(x0)/(2rho(x0)). After x=x0+e u, the unnormalized density is rho(x0)[1+a e u+b e^2 u^2+o(e^2)], uniformly for|u|<=1. Direct integration gives

alpha_J=1/2+(a/3)e+(-a^2/6+b/3)e^2+o(e^2),
v_J=1/3+(2a/9)e+(4b/45)e^2+o(e^2).

The exact sharp curve has

F(1/2)=1/3, F'(1/2)=2/3, F''(1/2)=7/5.

Therefore

v_J-F(alpha_J)=(a^2-4b)e^2/30+o(e^2)
              =-2g''(x0)e^2/[15g(x0)]+o(e^2).               (2)

Condition(c) forces g''(x0)<=0 on each smooth piece.

### Breakpoint expansion

At a breakpoint let the one-sided density slopes be rho'_- and rho'_+. Write

a=(rho'_++rho'_-)/(2rho(x0)),
k=(rho'_+-rho'_-)/(2rho(x0)).

Then locally rho(x0+e u)/rho(x0)=1+a e u+k e|u|+O(e^2). The zeroth, first and second unnormalized moments are2+k e, 2a e/3 and2/3+k e/2, up to their required orders. Using F'(1/2)=2/3 gives

v_J-F(alpha_J)=-k e/12+O(e^2)
              =-[g'_+(x0)-g'_-(x0)]e/[12g(x0)]+O(e^2).    (3)

Hence condition(c) forbids an upward derivative jump. Piecewise g''<=0 together with only downward derivative jumps makes the global derivative nonincreasing, which is exactly concavity of continuous g. This finishes the proof. Only first-order small-slab expansions are used at the breakpoints; no unproved global differentiability is assumed.

## 3. Finite algebra for piecewise-quadratic projected polyhedral laws

On an interval where rho(x)=a_i x^2+b_i x+c_i>0,

(sqrt(rho))''=(4a_i c_i-b_i^2)/(4rho^(3/2)).

Thus on every piece the smooth concavity condition is exactly

b_i^2-4a_i c_i>=0.                                         (4)

At a positive continuous knot t, the remaining condition is

rho'_+(t)<=rho'_-(t).                                      (5)

Consequently a given continuous positive piecewise-quadratic profile has the scalar convex3D realization property precisely when the finitely many discriminant and derivative-jump conditions(4)-(5) hold. All conditions are exact polynomial inequalities in its coefficients and knot positions. Density normalization is irrelevant to their signs.

A fixed-coordinate section of an actual3D polytope has this piecewise-quadratic form between successive vertex levels: each section vertex is affine in the level along its fixed true edge, the section polygon's cyclic incidence is unchanged within the interval, and its oriented area is quadratic. Degenerate levels are handled by continuity and one-sided derivatives. The finite criterion is therefore directly relevant to candidate projected polyhedral laws, but it remains a one-coordinate test. It does not prove that independently specified profiles in many directions come from one common polytope, nor does the explicit homothetic lift preserve a given finite facet count.

## 4. A new exact control that passes the global sharp test

On[-1,1] let

p(x)=1-x^2/5+b(|x|-1/2)_+^2,
b=79712/231215,
Z=int_-1^1 p=438244/231215,
rho=p/Z.

The density is even, strictly positive, C1 and piecewise quadratic, with only the two interior knots-1/2 and1/2. It has mean0. Its two original endpoint data agree by symmetry:

alpha=51225/109561=A(11/10),
variance=703971/2191220,
F(alpha)=728643/2332445.

The FULL sharp global gap is

variance-F(alpha)=9071304927/1022180026580>0.                (6)

Thus both original endpoint tests pass strictly. This is stronger than merely passing the two simpler inequalities alpha/(5(1-alpha)) and2alpha/3.

On the right outer interval its quadratic coefficients, in ascending order, are

(1+b/4, -b, b-1/5).

Their discriminant is

b^2-4(1+b/4)(b-1/5)=-589668/1156075<0.                    (7)

Therefore sqrt(rho) is strictly convex there and no uniform convex3D lift with this one-coordinate marginal exists.

For a completely explicit rejecting slab take J=[89/100,91/100]. Exact integrations give a positive mass and variance,49/100<alpha_J<1/2, but

v_J-2alpha_J/3
=-5071582559869198015584244600799014/
  2456959371573337044490860067539217981935<0.                (8)

Since F(alpha_J)>=2alpha_J/3, this slab fails the full sharp test as well. The output report preserves its exact normalized alpha, variance, mean and unnormalized mass. This law is intentionally NONPHYSICAL; no true-polyhedron equilibrium census is claimed.

## 5. Why all visible exponent-three apex tests still pass

For any apex z in[-1,1] and nonnegative C1 phi, define

E_z(phi)=int[phi+(x-z)phi'/3]rho(x)dx.

Integration by parts on the three smooth pieces cancels the interior boundary terms because rho is continuous. The endpoint terms are nonnegative, and the bulk density is

[2p(x)-(x-z)p'(x)]/(3Z).

Here p>=4/5 and |p'|<=2/5+b on[-1,1], so uniformly in x,z

2p-(x-z)p' >= 2(4/5)-2(2/5+b)=25548/231215>0.             (9)

Thus every projected exponent-three apex square test passes, in fact every nonnegative C1 test passes strictly when its bulk integral is nonzero.

There is one common radial endpoint law, not separately fitted endpoint moments. Take nu=E_0, a positive probability measure on[-1,1]. For every monomial of degree j, its nu moment is(1+j/3) times the rho moment. Radial mixing X=T Z with Z~nu and independent density3t^2 on[0,1] multiplies the j-th moment by3/(3+j), recovering rho by compact moment uniqueness. Conditioning on any independent tested endpoint Z~nu then gives the full projected cross-apex positivity for every polynomial Q(X,Z), exactly as in the cited common-law theorem. This control therefore is not an artifact of choosing unrelated moment factors.

### Every positive one-coordinate projective refill preserves the same blindness

Let L(x)=1+s x>0 on[-1,1], y=x/L(x), and refill formally with the ambient3D Jacobian weight L^-4 before pushing forward. After normalization Z_L, the new visible density is

rho_tilde(y)=rho(x)L(x)^-2/Z_L.

For a transformed apex z_tilde=z/L(z), direct differentiation gives

2rho_tilde(y)-(y-z_tilde)rho_tilde'(y)
=[2rho(x)-(x-z)rho'(x)]/[Z_L L(x)L(z)].                    (10)

All factors in the denominator are positive. The endpoints also have nonnegative flux terms, so all transformed projected apex tests pass. Reconstructing nu_tilde=E_y0 for a source apex in the transformed interval, and using the same radial identity, proves all transformed projected cross-apex tests too. An affine change of visible coordinates, including recentering at the transformed actual mean of the formal law, preserves this positivity. No assertion is made that the sharp ORIGINAL global normal test continues to pass after every such projectivity; it was proved at the two original endpoints only.

This distinction is the meaningful negative result: all projected apex/projective tests plus the two original sharp normal tests do not impose local Brunn realization. The all-slab sharp normal family does impose it, within the theorem's regularity and one-coordinate scope.

## 6. Exact source-only recovery and observed checks

The complete4909-byte source is [internal-source-reference], saved as slab_profile_exact.py, SHA87a3502980805e1585d9e39dd2e46ddb38ab18c8044037aaf5e5153cba1296e2. Required versions used: CPython3.13.5, SymPy1.14.0. No data, seeds, settings, previous script or sandbox file is required.

Run: python -B slab_profile_exact.py

Observed terminal marker, both in the original directory and a fresh directory containing only that source:

SLAB_PROFILE_REALIZATION_EXACT_V1 PASS 1420 87e02e599f3147dbf3e2dd9b559377a60eb426d9973f89316283b83ef18e82c0

The regenerated output slab_profile_exact_report.json is1420 bytes with the displayed SHA. Exact rational arithmetic checks the control's piecewise C1 joins, positivity bound, normalization, sharp global positive gap, discriminant, and explicit negative slab gap. Symbolic rational-series arithmetic checks(2)-(3) and F'(1/2),F''(1/2). It does not replace the analytic equivalence proof or claim a proof-assistant formalization.

## 7. Limits and next useful connection

The finite discriminant criterion can be added to candidate projected moment/section models that previously used only apex Euler constraints. A true slab changes the body and generally adds facets, so this theorem alone neither closes a fixed E17 tree packet nor preserves its incidence along a deformation. Multiple directional profiles must still be coupled by the one actual spatial law. The unresolved matrix1/5 facet theorem remains a different tangential/cross-covariance issue; the scalar iff theorem does not resolve it. The exact C600 construction and canonicalC622 are untouched.
