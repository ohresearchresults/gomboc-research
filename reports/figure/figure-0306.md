# figure-0306

AI research report · 2026-09-04 UTC

---

# Keen Quartz 89 — intrinsic moment conservation and certified critical collars

## Determination

**NONWINNER for the requested all-polyhedral object.** I did not produce a finite homogeneous polyhedron of own-centroid class `(1,1,0)`.

There are three concrete outputs, which must not be conflated:

1. A rational, fully expanded **1,073-vertex moment-conservative polyhedron**, and a genuinely local 1,141-vertex refinement. Their ordinary volume centroids are **exactly zero without translating either solid**. Complete, independent integer/Fraction audits give `(474,507,979)` and `(490,501,989)`, respectively. They demonstrate the mass-conservation mechanism, not successful mechanics.
2. A **constructive, exactly centred, partly polyhedral `(1,1,0)` body**: its two critical neighborhoods are replaced by explicitly specified finite polyhedral collars, including a complete common-separator proof at their interfaces with the remaining curved surface. Its noncritical belt is still curved. The two truncated collar meshes were actually expanded, with 94,209 and 94,208 vertices. This is not an all-polyhedral Gömböc.
3. An exact band/slab moment operator that permits local remeshing or section translation while keeping volume moments hard-constrained and leaving all distant complete feature stars unchanged. This supplies a route for joining the first two outputs, but I did not finish that compatible finite belt.

The attached journal's latest allocation distinguishes this intrinsic route from the coordinator's projective route. I used no unprovided formulas or artifacts from the cancelled smooth assignment. All data and proofs below were reconstructed in this turn. Journal input SHA-256: `909a949e6b9ef6c03d71f654109c20b2c1559f09004f85cb25b7b15f81f7a54e`.

The smooth source below is a translated-section construction, not the journal's `R^4` radial surface. The published radial representation is useful context, but is not a premise of these calculations; no priority claim is made for the alternative source.

## 1. A volume-centred smooth source with linear section moments

Write `e(P)=(cos P,sin P)` and let

```
rho(z) = sqrt(1-z^2),       -1 <= z <= 1,
w(z)   = epsilon e(P(z)),
K      = {(x,y,z): |(x,y)-w(z)|^2 <= 1-z^2}.
```

These are circular horizontal sections of a **uniform-density solid**. The relevant integrals are therefore

```
V = 4*pi/3,
Mx+i My = pi epsilon integral[-1,1] (1-z^2) exp(i P(z)) dz,
Mz = pi integral[-1,1] z(1-z^2) dz = 0.
```

They are neither surface moments nor vertex-mass moments.

### 1.1 Analytic source used for the finite experiment

Take

```
a = 3*pi/2,
eta(z) = a(z-z^3/3),
P(z) = eta(z),
epsilon = 1/64.
```

Since `eta'=a(1-z^2)` and `eta(-1)=-pi`, `eta(1)=pi`, the complex first moment is `pi epsilon/a` times the integral of `exp(i t)` over a complete period. It is exactly zero. Thus the ordinary centroid is the origin.

Parameterize the boundary by

```
p(z,psi) = ( e(P(z)) [epsilon + rho(z) exp(i psi)], z ).
```

The horizontal entry is interpreted as a complex number. Exactly, for every phase `P`,

```
|p|^2 = 1 + epsilon^2 + 2 epsilon rho(z) cos(psi).
```

Away from the poles, its only critical points are `(z,psi)=(0,0),(0,pi)`. In these coordinates the Hessians of squared distance are `-2 epsilon I` and `+2 epsilon I`. The corresponding points are `(1+epsilon,0,0)` and `(epsilon-1,0,0)`. The poles are `(-epsilon,0,+/-1)` with vertical normals and are not equilibria. Consequently, once convexity is established, this is exactly a one-stable/one-unstable homogeneous smooth body.

Here is an explicit global convexity and curvature proof. Put

```
F(x,y,z)= |v|^2+z^2-1,     v=(x,y)-w(z).
```

For a direction `(h,t)` in horizontal/vertical coordinates,

```
(1/2) D^2F[(h,t),(h,t)]
   = |h-t w'|^2 + (1-v dot w'') t^2.
```

If `s >= ||w'||` and `b >= ||w''|| < 1`, this gives

```
D^2F >= 2(1-b)/(1+s)^2 I,
|grad F| <= 2(1+s),
principal curvatures >= (1-b)/(1+s)^3.
```

Global convexity, rather than only local curvature, follows separately: for every horizontal unit vector `n`, the function `n dot w(z)+rho(z)` is strictly concave because `rho''<=-1` and `||w''||<1`. The solid is the intersection of the resulting convex hypographs.

For the analytic source,

```
|w''|^2 = epsilon^2 [4 a^2 z^2 + a^4(1-z^2)^4]
        <= epsilon^2 a^4.
```

The last inequality follows from `(1-u)^4<=1-u` and `a^2>4`. Using `pi<22/7`, one obtains `s<33/448`, `1-b>2047/3136`, and `(1-b)/(1+s)^2>1/2`. Thus `D^2F>I`, `|grad F|<9/4`, and every principal curvature exceeds **`4/9`**. No numerical critical-point counter is needed.

### 1.2 A C-infinity flat-phase source for exact spherical critical neighborhoods

The later collar construction uses a different, explicitly defined member of the same section-translated family, with `epsilon=1/128`.

Set `q(z)=(3z-z^3)/2`. Define a lifted function `Q0` by

```
Q0(t)=0                         on [-1/10,1/10],
Q0(t)=S((t-1/10)/(4/5))         on [1/10,9/10],
S(u)=10u^3-15u^4+6u^5,
Q0(t+1)=Q0(t)+1.
```

Let `phi` be the even, nonnegative, integral-one C-infinity bump proportional to

```
exp(-1/(1-(1000 t)^2))   for |t|<1/1000,
0                       otherwise.
```

Define `Q=Q0*phi` and `P(z)=pi Q(q(z))`. This specifies the kernel normalization by its integral, not by a numerical approximation.

`Q` is odd, `Q(t+1)=Q(t)+1`, and `Q=0` on `|t|<=99/1000`. Thus `exp(i pi Q)` is antiperiodic with period one and has zero integral over `[-1,1]`. The same volume calculation proves centroid zero. The squared-distance identity above proves exactly two nondegenerate equilibria again. On `|z|<=1/20`, the body is **exactly the unit ball centred at `(epsilon,0,0)`**, because `q(1/20)<99/1000`.

A reproducible rational interval certificate proves

```
||w'|| < epsilon * 2475/224,
||w''|| < 100 epsilon.
```

The certificate uses 8,192 equal rational intervals covering `z in [0,1]`, reflection for negative `z`, and a full convolution-shift interval `v in [-1/1000,1/1000]`. On the active part `q(z)+v in [1/10,9/10]`, put

```
u=(q(z)+v-1/10)/(4/5),
A=(75/2) u^2(1-u)^2,
D=(375/4) u(1-u)(1-2u).
```

Evaluate, with outward rational interval operations,

```
pi^2 [D q'(z)^2 + A q''(z)]^2
 + pi^4 [A q'(z)]^4.
```

Outside the active interval set both derivatives to zero. The largest upper endpoint is less than `9545`, hence less than `10000`. The actual recorded upper endpoint is approximately `9544.921464855608`.

For pi use the rational interval

```
[3.14159265358979323846264338327950288,
 3.14159265358979323846264338327950289].
```

It is independently enclosed using Machin's identity and alternating series: 70 terms for `atan(1/5)` and 20 for `atan(1/239)`.

Convolution does not invalidate this bound. Its first two phase derivatives are averages. If `Abar` denotes the average of nonnegative `A`, then `Abar^2<=average(A^2)`; the Euclidean triangle inequality then bounds the norm of the averaged second-derivative expression by the largest pre-convolution norm checked above.

With `s=2475/28672`, the resulting exact inequalities are

```
principal curvature >= (7/32)/(1+s)^3 > 1/6,
D^2F >= 2(7/32)/(1+s)^2 I > (1/3) I.
```

This is a C-infinity, exactly volume-centred, strictly convex source. The analytic and flat-phase seeds are separate specified bodies; their epsilon values must not be interchanged.

## 2. Exact local volume-moment conservation for polyhedral bands

Fix a rational strictly convex planar polygon `G` with area centroid zero and area `A`. At rational levels `z_i`, use horizontal sections

```
S_i = w_i + r_i G,    r_i >= 0.
```

Between successive levels interpolate both `r` and `w` affinely. For `h=z_(i+1)-z_i`, `r=r_i`, `s=r_(i+1)`, define

```
a_i = h(3r^2+2rs+s^2)/12,
b_i = h(r^2+2rs+3s^2)/12.
```

Exact ordinary-volume integration gives

```
V       = A sum_i (a_i+b_i),
M_xy    = A sum_i (a_i w_i + b_i w_(i+1)),
M_z     = A sum_i (a_i z_i + b_i z_(i+1)).
```

In particular, the two horizontal moments are **linear** in the section translations. Volume and vertical moment do not depend on them.

### 2.1 Co-design the phase with the finite area's distribution

Let `r_h` be the actual piecewise-linear radius, not the smooth radius. Define

```
U(z)=integral[-1,z] r_h(t)^2 dt,
W=U(1),
zeta(z)=2*pi*(U(z)/W-1/2).
```

Then `epsilon exp(i zeta(z))` has zero `r_h^2`-weighted mean exactly. Its weighted primitive is `epsilon W/(2*pi)` times `J(exp(i zeta))`, where `J(x,y)=(y,-x)`.

For a pair of consecutive cells, keep the two even-node translations and solve the middle translation explicitly:

```
T_j = kappa J(E_(2j+2)-E_(2j)),
w_(2j+1) = [T_j-a_(2j)w_(2j)-b_(2j+1)w_(2j+2)]
           / [b_(2j)+a_(2j+1)].
```

Here the ideal quantities are `E_i=exp(i zeta(z_i))` and `kappa=epsilon W/(2*pi)`.

For an **exact rational** solid, replace the `E_i` and `kappa` by rational values, force `E_N=E_0`, and retain the same formula. Every two-cell band's moment is exactly its specified `T_j`, and the total horizontal moment telescopes to zero. Symmetric levels/radii give vertical moment zero. No numerical root or final centroid translation is involved.

For a different zero-mean phase, including the flat phase in Section 1.2, use rational samples of its **integrated primitive** as the `T_j` endpoints. The shortcut `kappa J(E_end-E_start)` is specific to the unmodified phase `exp(i zeta)` and must not be applied unchanged to the flat phase.

### 2.2 Why retaining the old smooth phase is not a harmless shortcut

Matching smooth band moments while linearly interpolating `sqrt(1-z^2)` fails at the poles. In the first two cells of width `h`, the smooth area integral is asymptotic to `4h^2`; the piecewise-linear-radius area integral is `(8+2sqrt(2))h^2/3`. The middle-node moment weight is `(4+sqrt(2))h^2/3`.

Consequently, correcting that band's smooth target forces a centreline displacement tending to the nonzero magnitude

```
epsilon (4-2sqrt(2))/(4+sqrt(2)).
```

At `epsilon=1/64` this is approximately `0.00338106836107`, even as the mesh is refined. I rejected that version. The area-CDF phase above removes this boundary-layer mismatch.

There is also an effective approximation estimate for the ideal, unrounded construction. For a uniform grid with `h=2/N`, `N` divisible by four, `W>=1`, `|r_h r_h'|<=2`, and the mass-phase centreline satisfies `|w_*''|<65 epsilon` cellwise. The middle-node correction is at most `(65/2) epsilon h^2` because its hat-function moment weight is at least one quarter of the band's total weight.

The radius-square loss is exactly, on each cell,

```
(1-z^2)-r_h(z)^2 = t(1-t)[h^2+(r_(i+1)-r_i)^2],   0<=t<=1.
```

Summing yields an upper bound `h^2(1+log(N)/6)` for its integral. Thus the ideal centreline converges to the analytic source, with

```
||w_h-w||_infinity
 <= epsilon h^2 [325/8 + 2*pi*(1+log(N)/6)].
```

This estimate is for the unrounded construction. The rational finite experiments below are certified directly, rather than by asserting an unproved rounding envelope.

### 2.3 Convexity and complete incidence are checked, not assumed

For a CCW polygon edge of `G`, let `n` be its outward planar normal and `h_G=n dot G_j`. Put `H_i=n dot w_i+r_i h_G`. Require strict decrease of consecutive slopes

```
(H_i-H_(i-1))/(z_i-z_(i-1))
 > (H_(i+1)-H_i)/(z_(i+1)-z_i)
```

for every polygon edge and every interior level. These are affine inequalities in the translations. They prove convexity of the whole assembled solid and exposure of its intended side faces.

With zero-radius end sections and `m` polygon vertices, the actual lattice is

```
V=(N-1)m+2,    E=(2N-1)m,    F=N m.
```

Side faces are quadrilaterals, except for the two pole fans. Quadrilateral triangulation diagonals are never counted as true edges.

## 3. Materialized exact finite experiment and all-feature margins

The principal instance uses `N=64`, `m=17`, `epsilon=1/64`, coordinate proposal grid `2^-40`, and primitive scale grid `2^-60`. The exact polygon, phase samples, and complete reconstruction/checker are included in Section 8.

The following classifications are at each actual uniform-volume centroid:

| Construction | Centroid x | `(S,U,H)` | Weakest physical all-feature decision margin |
|---|---:|---:|---:|
| Ordinary samples of analytic `eta` | `9.74122771160e-6` | `(480,507,985)` | `3.62050793591e-6` |
| Samples of finite-area CDF phase, no band solve | `-2.75409638671e-6` | `(480,503,981)` | `2.61933023783e-5` |
| Exact two-cell moment conservation | **exactly 0** | **`(474,507,979)`** | `7.59937942745e-5` |

All three have `(V,E,F)=(1073,2159,1088)` and identical volume, because their section translations do not affect volume. For the balanced member the volume is exactly

```
286922547131749555664395329592722668672193946267735
/
70152078591883340073776871970381584943484762062848.
```

The ordinary-sampling first-moment error is about `3.98416971144e-5`. Its normalized error `||M||/V` is **2.69056935768 times** its weakest actual mechanical margin. The CDF-only ratio is `0.1051450614`; the exact band-balanced ratio is **zero**.

For the balanced member, exact squared-rational comparisons certify:

```
absolute score of every maximal face   > 1/14000,
absolute score of every vertex          > 1/5300,
absolute score of every full edge cone  > 1/14000,
every inactive vertex/plane distance    > 1/2000.
```

The measured minima are respectively `7.59937942745e-5`, `1.89538109526e-4`, `7.59937942745e-5`, and `5.16801213850e-4`.

The verifier uses these complete tests. For CCW face edge `a->b` and outward normal `n`, the face primitive is `(a-c) dot ((b-a) cross n)/|(b-a) cross n|`. A vertex primitive is `(a-c) dot (a-b)/|a-b|` for every true neighbor. For edge `d=b-a` with incident normals `n1,n2`, put `v=n1 cross n2`; the four edge primitives are

```
-(a-c) dot d / |d|,
 (b-c) dot d / |d|,
 (a-c) dot (n2 cross v) / |n2 cross v|,
 (a-c) dot (v cross n1) / |v cross n1|.
```

A feature is an equilibrium exactly when all its primitives are positive. The feature score is their minimum. A strictly negative minimum is a complete exclusion, even if another irrelevant primitive is zero. Each normalized primitive is 1-Lipschitz under movement of the reference centre, so these are actual centre-motion margins, not arbitrarily scaled residuals.

The second, independent implementation tests **all 1,167,424 face/vertex pairs with integer homogeneous coordinates**, reconstructs every true edge from maximal cycles, checks opposite orientations, integrates all tetrahedral moments exactly, and independently matches them to the horizontal-section formula. It reproduces `(474,507,979)` and exact zero moments. It does not rely on Qhull incidence tolerances.

### 3.1 Local refinement with unchanged distant full stars

Refine only the paired bands

```
[-11/16,-5/8] and [5/8,11/16].
```

Insert one midpoint in each of their four old cells. Set the new radii by exact dyadic square-root rounding. Keep band endpoints fixed, propose new centreline points by interpolation, and solve each band's old middle translation using its new exact weights so that **that band's old horizontal first moment is unchanged**. Reflection preserves the vertical moment.

The resulting fully expanded rational body has

```
(V,E,F) = (1141,2295,1156),
centroid = exactly (0,0,0),
(S,U,H) = (490,501,989),
V approximately 4.0900902369552785.
```

Exact lower bounds are `1/20000` for face decisions, `1/34000` for vertex and edge decisions, and `1/2800` for inactive incidence. The independent verifier checks all **1,318,996** face/vertex pairs.

Exactly 1,020 maximal faces, 971 complete vertex stars, and 1,989 complete true-edge stars are geometrically identical before and after refinement. Their classifications agree literally, because their geometry and the centre are unchanged. Changes inside the refined bands are not hidden: the global class changes as displayed above. This is a local conservation experiment, not a claim that arbitrary refinement preserves mechanics.

## 4. Finite critical collars, with the mixed smooth/polyhedral seams included

This section uses the flat-phase source of Section 1.2, with `epsilon=1/128`.

### 4.1 Complete exact construction recipe

Let `D=2^48`, `m=1024`. Construct `G` by rounding the coordinates of `(1-4/D)(cos(2*pi*j/m),sin(2*pi*j/m))` to multiples of `1/D`, using exact quarter-turn/reflection symmetry. All resulting polygon inequalities are checked exactly. Let

```
a_G^2 = min_j h_j^2/|n_j|^2,
b_G^2 = max_j |G_j|^2,
```

where `n_j` is an outward edge normal and `h_j=n_j dot G_j`. The certified values include

```
a_G^2 > 0.99999058764126,
b_G^2 < 1.
```

Start `r_0=1/64`. Repeatedly append `min((129/128)r_i,1/32)` until reaching `1/32`, then append the guard radius `129/4096`. There are **92 radii**. Define

```
g_i = floor(D sqrt(1-r_i^2))/D,
k_i = (g_(i+1)-g_i)/(r_(i+1)-r_i),
h_i^+ = epsilon+g_i,
h_i^- = g_i-epsilon.
```

The downward square-root rounding is important: it keeps every prescribed collar point inside the relevant sphere. Nearest rounding is not substituted here.

The positive collar has vertices `(h_i^+,r_i G_j)` and an axial apex `A=(H,0,0)`. The negative collar has vertices `(-h_i^-,r_i G_j)` and a central stable polygon at `x=epsilon-g_0`. In these expressions `r_i G_j` occupies the `(y,z)` coordinates.

Choose the apex height by the exact rational formula

```
L = h_0^+ + r_0^2 b_G^2/h_0^+,
U = h_0^+ - r_0 k_0,
H = (L+U)/2.
```

Numerically `H approximately 1.0079341231697982`.

For every annular interval and every polygon edge, impose the two halfspaces

```
 x - (k_i/h_j) n_j dot (y,z) <=  epsilon+g_i-k_i r_i,
-x - (k_i/h_j) n_j dot (y,z) <= -epsilon+g_i-k_i r_i.
```

Also impose the two core cuts `epsilon-g_0 <= x <= epsilon+g_0`. Intersect these halfspaces with the smooth source to get `Kc`, then set `Khat=conv(Kc union {A})`.

The apex satisfies all annulus planes, and the upper core-cut polygon is its only visible boundary piece. Thus adding the apex adds exactly one pyramid over `r_0 G`; it is not an uncontrolled global hull addition.

The truncated positive and negative collar meshes have `(vertices, displayed faces)` equal to `(94209,94208)` and `(94208,93185)`. Their outer rims are **truncation/display boundaries**, not an asserted global true-edge list. In `Khat`, the last annular planes continue to their certified curved seams. These open meshes are not complete solids.

### 4.2 Internal collars: feasible directions exclude complete normal cones

For any convex body and reference centre zero, an equilibrium at `p` requires `p` to belong to the full outward normal cone. A feasible tangent direction `d` with `p dot d>0` disproves that condition for the **entire cone at once**.

On a positive annulus, write `p(s)=(h(s),s v)` with `v` on the boundary of `G`. The inward radial direction is feasible. On a negative annulus, `p(s)=(-h(s),s v)` and the outward radial direction is feasible. The following rational inequalities were checked on every interval:

```
-h_(i+1)^+ k_i - r_(i+1) b_G^2 > epsilon r_0/3,
 h_i^- k_i + r_i a_G^2          > epsilon r_0/5.
```

The apex-cone slope `kc=(h_0^+-H)/r_0` satisfies `k_0<kc<0` and

```
-h_0^+ kc-r_0 b_G^2 > epsilon r_0/6.
```

These directions remain feasible on ring edges and multi-face vertices. Their norms are less than two in the radial parameterization. Thus they exclude all unintended equilibria in the internal collars, including mixed polyhedral normal cones. The stable polygon contains the perpendicular foot strictly; the apex has every directed true-edge primitive greater than `1/128`.

### 4.3 Outer seams: a common separator for every active plane and the sphere

This is the step that cannot be replaced by independent facet tests.

For annulus `i`, define `E_i=(2/3)epsilon r_i`, and `T_i=g_i-k_i r_i`. Exact rational checks give

```
T_i^2 > (1-E_i^2/2)^2 (1+k_i^2/a_G^2),
k_i^2/(1+k_i^2) > r_i^2,
(1001/1000)|k_i|+3E_i < 1/20.
```

The first inequality says that the plane's unit distance from the sphere centre is at least `1-E_i^2/2`. Consequently, at any point of that plane inside the unit ball, its unit normal is within `E_i` of the local unit radial direction. The second inequality bounds the transverse coordinate from below by `r_i-E_i`.

To see that the cuts really occur in the spherical strip, use `D^2F> I/3`. At a spherical support point with unit normal `n`, any point cut off at inward depth `delta` is within `sqrt(12 delta)` of that support point. Here this is at most `sqrt(6) E_i<3 E_i`, so the third inequality localizes every cut to `|z|<1/20`. The two core cuts obey the same localization bound. Thus no non-spherical remote patch is silently being cut.

Now let `o=epsilon e_x`, `u=(p-o)/|p-o|`, and

```
t=o-(o dot u)u,
C=(2/3)/(1-(2/3)epsilon),
E*=C epsilon |(y,z)|,
d_min=1-(max E_i)^2/2,
d=t-(E*|t|/d_min)u.
```

For **every** active annular plane, its normal `n` satisfies `n dot d<=0`. The same is true for the sphere normal if the sphere is active. On the other hand,

```
p dot d >= |t| epsilon |(y,z)| [1-C(1+epsilon)/d_min].
```

The bracket exceeds `0.324607320897`. This proves a single strictly positive feasible direction against all active generators simultaneously. It covers polyhedral faces, edges, high-valence vertices, and all mixed plane/sphere seams.

Together with the core arguments and the unchanged smooth belt, a conservative common exclusion margin for the nontarget collar features, their seams, and the remaining curved belt is

```
B = epsilon r_0/16 = 1/131072.
```

This is not a pointwise exclusion bound inside the intended stable face, which contains its intended equilibrium. For the unchanged smooth belt, the section-untwisting parameterization has derivative norm less than 13. Outside the removed cores, its spherical distance-gradient factor is at least `(999/1000)r_0`, giving a larger margin than `B`.

The remaining visibility assertion for the apex is also quantitative. `H-epsilon<1/g_0`, so it cannot see any surviving spherical surface outside the upper core cut. Outside `|z|<1/20`, the global strong-convexity bound gives a support deficit at least `1/5600`, whereas `H-(1+epsilon)<1/5600`. Hence it cannot see a remote non-spherical piece either.

**Proved scope:** `Khat` has exactly one stable polygon, one unstable apex, and no other equilibrium relative to the origin. Its two finite critical collars and their curved interfaces have complete normal-cone separation. The rest of its boundary is still curved.

## 5. The critical-patch moment cost is already below the mechanical margin

Let `V_R` be the volume removed at one end by the core cut and annular planes. The two removed regions are reflections about `x=epsilon`, because they lie wholly in the exactly spherical strip. Let `A_G` be the area of `G`, and let

```
V_cone = A_G r_0^2 [H-(epsilon+g_0)]/3.
```

The actual volume and first moments of `Khat` are therefore

```
V(Khat) = 4*pi/3 - 2 V_R + V_cone,
Mx(Khat) = -2 epsilon V_R
           + V_cone [H+3(epsilon+g_0)]/4,
My(Khat)=Mz(Khat)=0.
```

A simple spherical-cap union bound already proves

```
volume symmetric difference < 1.560165739e-7,
||M(Khat)|| < 1.608920918e-7,
||c(Khat)|| < 4.022302295e-8.
```

The first bound is obtained by summing `pi delta^2` for each annular spherical cap, with `delta<=E_i^2/2`, adding the two core caps, and adding the exact pyramid volume. The moment bound uses that every changed point has norm less than `33/32`. It is not an assumed quadrature error.

A sharper outward-rational calculation gives

```
V_R in [4.68245068e-8, 4.68313576e-8],
Mx in [6.20562421e-8, 6.20563492e-8],
c_x in [1.48148366e-8, 1.48148622e-8].
```

Thus the actual critical-patch centroid displacement is less than **0.002 times** `B`. This is the opposite scaling from the inherited cumulative axial drift.

For reconstruction of the sharper bounds, let `f(s)` be `g_0` on `[0,r_0]`, the linear interpolant through `(r_i,g_i)` on the annuli, and the last affine segment extended afterward. For a fixed angular radius factor `R`, integrate the removed radial height `sqrt(1-rho^2)-f(rho/R)`. The polygon has `a_G<=R<=1`; monotonicity bounds the true volume between the two constant-factor integrals, multiplied by `2*pi`.

All radial antiderivatives are elementary:

```
integral rho sqrt(1-rho^2) d rho = -(1-rho^2)^(3/2)/3,
integral rho(A+B rho) d rho = A rho^2/2+B rho^3/3.
```

For the final line, the outer intersection is

```
rho_out = [-A B + sqrt(1+B^2-A^2)]/(1+B^2).
```

Use exact rational interval square roots, for example denominator `2^160`, and the pi interval already specified. These recipes reproduce the printed enclosures without surface integration or Monte Carlo.

### 5.1 Exact, physically small, collar-frozen mass closure

Reserve the even band field

```
chi(z) = (1-16(|z|-1/2)^2)^3   when 1/4 <= |z| <= 3/4,
         0                    otherwise.
```

It is C2, with `|chi|<=1`, `|chi'|<7`, `|chi''|<=96`, and

```
pi integral[-1,1] (1-z^2) chi(z) dz = 107*pi/315.
```

Apply the volume-preserving, non-rigid shape map

```
T_lambda(x,y,z)=(x+lambda chi(z),y,z),
lambda = -315 Mx(Khat)/(107*pi).
```

The determinant is one. On its support, the body's sections are still the original disks; consequently this formula makes **all three ordinary first moments exactly zero**. It fixes every critical collar and seam point, since they lie in `|z|<1/20`. It is not translation by the body's centroid.

The unique linear moment root is enclosed by

```
lambda in [-5.81517951e-8, -5.81516947e-8].
```

In particular `|lambda|<1/16000000`. The updated section derivatives still certify principal curvature greater than `1/6` on the curved part and `D^2F>I/3`. For any unit feasible direction in the moved belt, the positive radial work changes by less than `9|lambda|`; normalizing the moved direction costs at most a factor `1+7|lambda|`. Therefore the belt retains a noncritical margin greater than **`1/150000`**. The two critical patches are unchanged exactly. A larger reserved interval `|lambda|<=1/3200000` still preserves a positive mechanical margin and supplies an x-moment capacity of `107*pi/(315*3200000)`, approximately `3.34e-7`, versus the required `6.21e-8`. This is a checked capacity comparison, not only a nonzero Jacobian.

**Hybrid theorem:** `T_lambda(Khat)` is a convex homogeneous body, has exact ordinary centroid zero and strict equilibrium class `(1,1,0)`, and has the explicitly materialized polyhedral critical neighborhoods above. **It is not a polyhedron because the noncritical belt is still curved.** The supplied analytic proof and rational scalar certificates establish this intermediate construction; there has been no external mathematical peer review.

## 6. General slab operator and the remaining finite task

The moment mechanism is not restricted to homothetic polygons. Let a slab be the convex hull of two arbitrary fixed polygons at heights `z_i,z_(i+1)`. Translating these polygons horizontally by `u_i,u_(i+1)` is an affine shear on that slab. If its volume is `V_i` and original centroid height is `c_zi`, then

```
t_i=(c_zi-z_i)/(z_(i+1)-z_i),
Delta M_xy = V_i[(1-t_i)u_i+t_i u_(i+1)].
```

Volume and vertical moment are unchanged. The complete horizontal moment map is thus exactly linear even for independently twisted or asymmetric sections. For a fixed slab face lattice, all vertex/plane support inequalities are affine in these translations: each triangle has two vertices on one level, so its horizontal normal components are fixed and its vertical normal component is linear in the translation difference.

There are two essential limitations. First, this is not three independent moment controls: vertical moments require symmetry or an additional height/shape variable. The constructions here use exact reflection/half-turn balance. Second, the formula is valid for the **actual convex slab assembly**. If the global hull skips levels, the formal slab moment is not the true hull moment. An exploratory twisted-ring implementation exhibited precisely this failure and was rejected. A zero formal moment is not accepted without the complete supporting-plane test.

The most useful continuation is now specific: retain the fixed-size critical collars and their seam inequalities from Sections 4–5; construct a noncritical band/slab mesh whose full normal cones have common separators; use the exact linear moment operator or band-conservative targets while solving the actual convexity inequalities; and audit every realized feature before refining another band. Use the integrated primitive of the flat phase rather than the unmodified-phase shortcut. Maintain the half-turn symmetry `(x,y,z)->(x,-y,-z)` in the finite background so that `My=Mz=0` remains structural; this symmetry fixes both intended equilibria and does not impose central symmetry. The finite 1,073-vertex example provides the exact arithmetic and local-conservation checker; the hybrid construction provides protected critical neighborhoods with a real mass-capacity budget.

I did **not** establish a moderate-size all-polyhedral realization of that combined belt. The remaining obstruction is geometric/mechanical discretization of the noncritical network, not a missing volume-centroid identity or a rank-only actuator claim. Coarse polygons, nominal slab assemblies, and the two separate outputs must not be promoted to a finished Gömböc.

## 7. Reproduction and evidence boundary

The bundle contains complete rational V/F/E data for both finite nonwinners, maximal-polygon OBJ files, binary STL display meshes, the two expanded open critical-patch OBJ files, the rational derivative/seam/moment certificates, and runnable scripts.

`python RUN_ALL.py` terminates with:

```
ALL_FINITE_AND_CRITICAL_PATCH_CHECKS_PASS; NO_ALL_POLYHEDRAL_WINNER
```

`replay_exact.py` uses only the Python standard library. The critical polygon proposer additionally uses `mpmath`; its trigonometric approximations are not proof premises, because the actual rational polygon and every required inequality are checked afterward. The original numerical explorations are not promoted to certificates.

OBJ and STL versions of the two finite nonwinners are watertight with 2,142 and 2,278 triangles. STL is a single-precision display approximation: its centroid differs from exact zero by about `1.1e-9`. The rational JSON and exact checker, not STL, define the mathematical solids. The critical collar meshes have open outer rims deliberately and are not complete physical solids.

## 8. Standalone exact finite reconstruction and exhaustive checker

The following code is the complete standard-library reconstruction and checker for the principal finite body and its local refinement. It embeds every continuation-critical rational sample, constructs all maximal faces and true edges, checks all inactive incidences exactly, integrates exact volume moments in two ways, and classifies every face, vertex and full edge cone. It never subtracts a computed solid centroid.

```python
#!/usr/bin/env python3
"""Self-contained, standard-library-only exact finite experiment.
No point is translated by the resulting solid's centroid.
Verifies ALL face/vertex incidences as integers and ALL mechanical features.
"""
from fractions import Fraction as Q
from collections import defaultdict
from math import isqrt,lcm,sqrt,gcd
import json,os,time
D=2**40
EE=[(-1099511627776,0),(-1099366688382,-17852285336),(-1096929244427,-75313028989),(-1086630814088,-167807310597),(-1060298464212,-291020594468),(-1008300690314,-438469540023),(-920986679465,-600590838977),(-790441697973,-764282501252),(-612431718166,-913155633065),(-388248300899,-1028683175941),(-126040491401,-1092263527791),(158810283537,-1087982129200),(444612144699,-1005607209799),(705677106377,-843175925386),(915784754693,-608493305376),(1052211456337,-319024874841),(1099511627776,0)]
GG=[(1099511627776,0),(1025264058808,397189412410),(812548897514,740736193771),(490094505122,984242447603),(101450134106,1094821305010),(-300895639676,1057538478562),(-662603790000,877429220560),(-934823626869,578818284319),(-1080790352893,202034731438)]
def add(a,b):return tuple(x+y for x,y in zip(a,b))
def sub(a,b):return tuple(x-y for x,y in zip(a,b))
def sc(c,a):return tuple(c*x for x in a)
def dot(a,b):return sum(x*y for x,y in zip(a,b))
def cross(a,b):return (a[1]*b[2]-a[2]*b[1],a[2]*b[0]-a[0]*b[2],a[0]*b[1]-a[1]*b[0])
def det(a,b,c):return dot(a,cross(b,c))
def rsqrt(x):
 t=x*D*D;n=isqrt(t.numerator//t.denominator)
 return Q(n+(t>Q((2*n+1)**2,4)),D)
def weight(z0,z1,r,s):
 h=z1-z0;return h*(3*r*r+2*r*s+s*s)/12,h*(r*r+2*r*s+3*s*s)/12

def seed():
 z=[Q(i-32,32) for i in range(65)];r=[rsqrt(1-t*t) for t in z]
 E={2*i:tuple(Q(x,D) for x in t) for i,t in enumerate(EE)}
 for i in range(34,65,2):E[i]=(E[64-i][0],-E[64-i][1])
 w=[None]*65
 for i in range(0,65,2):w[i]=sc(Q(1,64),E[i])
 kap=Q(3818978989101066,2**60)
 for i in range(0,64,2):
  a,b=weight(z[i],z[i+1],r[i],r[i+1]);c,d=weight(z[i+1],z[i+2],r[i+1],r[i+2])
  e=sub(E[i+2],E[i]);T=sc(kap,(e[1],-e[0]))
  w[i+1]=sc(1/(b+c),sub(sub(T,sc(a,w[i])),sc(d,w[i+2])))
 G=[tuple(Q(x,D) for x in t) for t in GG]
 G += [(G[17-j][0],-G[17-j][1]) for j in range(9,17)]
 cr=[G[i][0]*G[(i+1)%17][1]-G[i][1]*G[(i+1)%17][0] for i in range(17)]
 A2=sum(cr);C=tuple(sum((G[i][k]+G[(i+1)%17][k])*cr[i] for i in range(17))/(3*A2) for k in (0,1))
 G=[sub(p,C) for p in G]
 return z,r,w,G,A2/2

def refine(data):
 z,r,w,G,A=data;z=z[:];r=r[:];w=w[:]
 # Replace upper band 52..54 first, then lower band 10..12.
 for i in (52,10):
  zz=[z[i],(z[i]+z[i+1])/2,z[i+1],(z[i+1]+z[i+2])/2,z[i+2]]
  rr=[r[i],rsqrt(1-zz[1]**2),r[i+1],rsqrt(1-zz[3]**2),r[i+2]]
  ww=[w[i],sc(Q(1,2),add(w[i],w[i+1])),w[i+1],sc(Q(1,2),add(w[i+1],w[i+2])),w[i+2]]
  T=(Q(0),Q(0))
  for j in (i,i+1):
   a,b=weight(z[j],z[j+1],r[j],r[j+1]);T=add(T,add(sc(a,w[j]),sc(b,w[j+1])))
  W=[Q(0)]*5
  for j in range(4):
   a,b=weight(zz[j],zz[j+1],rr[j],rr[j+1]);W[j]+=a;W[j+1]+=b
  ww[2]=tuple((T[k]-sum(W[j]*ww[j][k] for j in (0,1,3,4)))/W[2] for k in (0,1))
  assert all(sum(W[j]*ww[j][k] for j in range(5))==T[k] for k in (0,1))
  z[i:i+3]=zz;r[i:i+3]=rr;w[i:i+3]=ww
 return z,r,w,G,A

def mesh(data):
 z,r,w,G,A=data;V=[];ids=[];m=len(G)
 for zi,ri,wi in zip(z,r,w):
  if ri==0:ids.append([len(V)]*m);V.append(wi+(zi,));continue
  ids.append([])
  for p in G:ids[-1].append(len(V));V.append(add(wi,sc(ri,p))+(zi,))
 F=[]
 for i in range(len(z)-1):
  for j in range(m):F.append(list(dict.fromkeys([ids[i][j],ids[i][(j+1)%m],ids[i+1][(j+1)%m],ids[i+1][j]])))
 return V,F

def score(q,v):
 d=dot(v,v);assert d>0;return dot(q,v),d
# Pair (a,b) denotes signed physical distance a/sqrt(b).
def less(p,q):
 if (p[0]>0)!=(q[0]>0):return p[0]<=0
 if p[0]==0 or q[0]==0:return p[0]<q[0]
 u=p[0]*p[0]*q[1];v=q[0]*q[0]*p[1]
 return u<v if p[0]>0 else u>v

def minimum(ps):
 p=ps[0]
 for q in ps[1:]:
  if less(q,p):p=q
 return p

def audit(data,expected,bounds,incbound):
 st=time.time();V,faces=mesh(data);z,r,w,G,A=data;m=len(G);N=len(z)-1
 # Exact horizontal support concavity, an independent structural hull check.
 for j in range(m):
  d=sub(G[(j+1)%m],G[j]);n=(d[1],-d[0]);h=dot(n,G[j]);assert h>0
  H=[dot(n,u)+s*h for u,s in zip(w,r)]
  sl=[(H[i+1]-H[i])/(z[i+1]-z[i]) for i in range(N)]
  assert all(sl[i]>sl[i+1] for i in range(N-1))
 # Integer homogeneous coordinates allow a literal ALL-pairs support audit.
 HV=[]
 for v in V:
  den=lcm(*(x.denominator for x in v));HV.append(tuple(int(x*den) for x in v)+(den,))
 normal=[];edge=defaultdict(list);volume=Q(0);moment=(Q(0),)*3;incmin=None
 for f,cyc in enumerate(faces):
  a,b,c=[V[i] for i in cyc[:3]];nr=cross(sub(b,a),sub(c,a));hh=dot(nr,a);assert hh>0
  den=lcm(*(x.denominator for x in nr+(hh,)));p=tuple(int(x*den) for x in nr)+(-int(hh*den),)
  gg=gcd(*p);p=tuple(x//gg for x in p)
  ni=p[:3];norm2=dot(ni,ni);members=set(cyc)
  for i,vh in enumerate(HV):
   s=dot(p,vh)
   if i in members:assert s==0
   else:
    assert s<0
    nu=s*s;de=vh[3]**2*norm2
    assert nu*incbound.denominator**2>de*incbound.numerator**2
    if incmin is None or nu*incmin.denominator<incmin.numerator*de:incmin=Q(nu,de)
  normal.append(ni)
  for a,b,c in zip(cyc,cyc[1:]+cyc[:1],cyc[2:]+cyc[:2]):assert dot(cross(sub(V[b],V[a]),sub(V[c],V[b])),ni)>0
  for a,b in zip(cyc,cyc[1:]+cyc[:1]):edge[tuple(sorted((a,b)))].append((f,a,b))
  a=V[cyc[0]]
  for j in range(1,len(cyc)-1):
   b,c=V[cyc[j]],V[cyc[j+1]];dv=det(a,b,c)/6;assert dv>0
   volume+=dv;moment=add(moment,sc(dv/4,add(add(a,b),c)))
 assert all(len(t)==2 and t[0][1:]==t[1][1:][::-1] for t in edge.values())
 assert (len(V),len(edge),len(faces))==((N-1)*m+2,(2*N-1)*m,N*m)
 assert len(V)-len(edge)+len(faces)==2 and moment==(0,0,0)
 # Independent horizontal-section volume/moment integration.
 vv=Q(0);mm=[Q(0)]*3
 for i in range(N):
  a,b=weight(z[i],z[i+1],r[i],r[i+1]);vv+=a+b
  for k in (0,1):mm[k]+=a*w[i][k]+b*w[i+1][k]
  mm[2]+=a*z[i]+b*z[i+1]
 assert volume==A*vv and mm==[0,0,0]
 sf=[];su=[];se=[];neighbors=[[] for _ in V]
 for cyc,n in zip(faces,normal):sf.append(minimum([score(V[a],cross(sub(V[b],V[a]),n)) for a,b in zip(cyc,cyc[1:]+cyc[:1])]))
 for (a,b),inc in edge.items():
  d=sub(V[b],V[a]);n1,n2=(normal[t[0]] for t in inc);v=cross(n1,n2)
  se.append(minimum([score(V[a],sc(-1,d)),score(V[b],d),score(V[a],cross(n2,v)),score(V[a],cross(v,n1))]))
  neighbors[a].append(b);neighbors[b].append(a)
 for a,nb in enumerate(neighbors):su.append(minimum([score(V[a],sub(V[a],V[b])) for b in nb]))
 groups=[sf,su,se];counts=tuple(sum(p[0]>0 for p in ss) for ss in groups)
 assert counts==expected and counts[0]+counts[1]-counts[2]==2
 margins=[]
 for ss,b in zip(groups,bounds):
  assert all(p[0]!=0 and p[0]**2>b*b*p[1] for p in ss)
  margins.append(sqrt(float(min(p[0]**2/p[1] for p in ss))))
 assert incmin>incbound*incbound
 out={'VEF':(len(V),len(edge),len(faces)),'class':counts,'exact_centroid':[0,0,0], 'volume':float(volume),'margins':margins,'incidence':sqrt(float(incmin)),'literal_support_pairs':len(V)*len(faces),'seconds':time.time()-st}
 print(json.dumps(out),flush=True)
 return out

if __name__=='__main__':
 d=seed();a=audit(d,(474,507,979),[Q(1,14000),Q(1,5300),Q(1,14000)],Q(1,2000))
 b=audit(refine(d),(490,501,989),[Q(1,20000),Q(1,34000),Q(1,34000)],Q(1,2800))
 print('ALL_EXACT_BAND_MOMENT_AND_FULL_MECHANICS_CHECKS_PASS; NONWINNERS',flush=True)
 json.dump({'source':a,'refined':b},open(os.path.join(os.path.dirname(__file__),'independent_replay.json'),'w'),indent=2)
```

## 9. Supplementary artifacts

Complete proof, exact data, checks, and meshes (`keen_quartz_mass_balance_handoff.zip`). Archive SHA-256: `88d2fac95165c3be9a321d21e3d86fd4ea40191ea0bc39dc337a80d9eec1cec2`.

Standalone exact finite checker (`replay_exact.py`). Its complete source is also embedded above.

Readable Markdown handoff (`HANDOFF.md`). None of these links is the sole source of a continuation-critical construction.
