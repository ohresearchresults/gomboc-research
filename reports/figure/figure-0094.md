# figure-0094

AI research report · 2026-08-26 UTC

<!-- historical-status:start -->
> **Historical AI report.** The title and claims below reflect the AI’s assessment at the time. Claims of proof, certification or completion are not a current verification verdict.
>
> [C622](../../C622/README.md) passes the supplied exact checks; the search for C<500 remains open. See [verification status and source gaps](../../catalog/coverage.md).
<!-- historical-status:end -->

---

# Verdict

No finite homogeneous convex polyhedral Gömböc was certified in this turn. The strongest newly materialized theorem-guided body is a deterministic finite inward-halfspace construction with one stable face but an open residual unstable–saddle pair. At the construction center its class is `(S,U,H)=(1,2,1)`; at its own uniform-volume centroid it is `(8,4,10)`. It therefore fails the required own-centroid `(1,1,0)` gate. The exact eight-vertex `(2,2,2)` body from the resolved branch remains the strongest fully exact finite fallback, but it is secondary rather than the primary construction reported here.

The run’s acceptance gate requires a materialized uniform-density polyhedron evaluated at its own exact volume centroid, with exactly one stable maximal face, one unstable vertex, no saddle edges, complete incidence reconstruction, strict margins, independent verification, and OBJ/STL. A smooth source, auxiliary-center result, wall point, or unexpanded existence construction is insufficient.

# What was implemented

I implemented the three geometric parts of Lángi’s proof as an explicit finite generator rather than another quasi-uniform Fourier mesh:

1. a dedicated inward stable cap at the smooth radial minimum;
2. a three-plane concurrent unstable fan at an interior apex near the smooth radial maximum;
3. a deterministic noncritical spiral of inward-shifted smooth supporting planes, with a row-by-row projection-foot exclusion inequality.

The proof source constructs the stable neighborhood by a near-parallel truncating plane followed by finitely many additional truncations, and constructs the unstable neighborhood from a radially decreasing polygonal curve whose rotated copies form a conical fan. Its centroid correction uses four disjoint base polygons and pyramidal cones whose first moments are `(alpha_i tau_i + beta_i tau_i^2) w_i`; the four directions positively span the origin, making the moment map locally surjective.

The new computation materially advances that architecture: the noncritical halfspaces are no longer sampled quasi-uniformly, and every generated row is an inward shift of an actual support plane of the certified Fourier seed. It nevertheless exposes two finite failures: the unstable fan does not control the final active maximum, and the existing safe facets do not contain a feasible four-actuator moment cone.

# Certified smooth source

The source remains

```text
R(theta,phi)^4 = 1 + 4 beta sin(theta) cos(phi-P(theta))
beta = 1/160
P(theta) = eta(theta) - (1/3) sin(3 eta(theta))
eta(theta) = (3 pi/2)(cos(theta)-cos(theta)^3/3).
```

It is kept strictly separate from the finite-polyhedron result. Its stored interval certificate proves

```text
minimum B_11                         >= 0.42891126735459995
minimum determinant of second form >= 0.4208148562262843
minimum Gaussian curvature          >= 0.4316325731624288
checked parameter boxes              = 10,368.
```

An independent dense differential reconstruction gives minimum Gaussian curvature approximately `0.5157510290`. The centroid is algebraically zero: after longitude integration, the transverse first moment becomes a complete-period Fourier integral with frequencies `1+3m`, none of which is zero. The only radial critical points are `(theta,psi)=(pi/2,pi)` and `(pi/2,0)`, the strict minimum and maximum.

# Deterministic finite theorem-guided generator

The strongest open construction uses

```text
beta          = 1/160
a             = -1/3
k             = 3
W             = 8
cN            = 12
N             = cN W^2 = 768
gamma         = 0.22
t_max         = cos(gamma)
phase         = 0.19
apex_inset    = 5e-5
absolute monotonicity margin = 1e-8
stable-cap extra margin      = 1e-5
unstable fan size            = 3.
```

For `i=0,...,767`, set

```text
s_i      = (i+1/2)/768
t_i      = -t_max + 2 t_max s_i
lambda_i = 16 pi s_i + 0.19.
```

Map the untwisted coordinates to the unit sphere by

```text
rho_i = sqrt(1-t_i^2)
y_i   = rho_i cos(lambda_i)
z_i   = rho_i sin(lambda_i)
theta_i = arccos(z_i)
psi_i   = atan2(y_i,t_i)
eta_i   = (3 pi/2)(z_i-z_i^3/3)
phi_i   = psi_i + eta_i - (1/3) sin(3 eta_i)
u_i     = (sqrt(1-z_i^2) cos(phi_i),
           sqrt(1-z_i^2) sin(phi_i),
           z_i).
```

For each `u_i`, compute the smooth point `x_i=R(u_i)u_i`, outward unit normal `n_i`, smooth support `h_i=n_i·x_i`, and normalized polar support row `q_i^0=n_i/h_i`.

The unstable fan uses three boundary directions at `t=t_max`, separated by `2 pi/3`, and the interior apex

```text
A = ((41/40)^(1/4)-5e-5, 0, 0).
```

Its rows are

```text
q_fan,j = n_fan,j/(n_fan,j·A),  j=0,1,2.
```

All satisfy an inward-shift condition relative to the smooth support plane. Starting with the first fan row, recursively scale the noncritical rows backward:

```text
rho_i = max(1,
            (q_next·q_next + 1e-8)/(q_next·q_i^0)),
q_i   = rho_i q_i^0,
q_next <- q_i.
```

Consequently every consecutive active candidate pair satisfies

```text
q_next · (q_i-q_next) > 1e-8.
```

Equivalently, the perpendicular foot of the `q_next·x=1` plane violates the preceding halfspace. This is the explicit finite projection-foot exclusion used in place of mesh-density heuristics.

At the stable minimum, `q_min=(-1,0,0)/(39/40)^(1/4)`. Its cap scale is

```text
rho_cap = max(1,
 (q_0·q_0+1e-5)/(q_0·q_min)),
q_cap   = rho_cap q_min.
```

For the reported body,

```text
rho_min       = 1.0263216730399054
rho_max       = 198008.91508420536
rho_start     = 198008.91508420536
rho_end       = 1.0263216730399054
stable-cap scale = 202252.8880662104
fan scale ratios =
 [1.026309615569885,
  1.1122633256379884,
  1.7038416480572776].
```

The final finite H-body is

```text
P = {x in R^3 : q_j·x <= 1 for all 772 generated rows}.
```

A complete polar-hull reconstruction finds that 89 rows are irredundant. The resulting primal has

```text
(V,E,F,C) = (174,261,89,522)
Euler      = 174-261+89 = 2.
```

# Complete mechanical outcome of the theorem-guided body

At the displayed construction center `0`, exhaustive reconstruction of all 89 actual maximal faces, 174 actual vertices, and 261 true edges gives

```text
(S,U,H) = (1,2,1).
```

The only stable face is the dedicated cap:

```text
source row: stable_cap
normalized stable margin: +0.2089487978.
```

The two unstable vertices are

```text
V29 = ( 1.1239e-6, -1.3099e-5, -2.6105e-5)
normalized unstable margin: +0.6569619436
incident active source indices: spiral 73, 37, 46

V55 = ( 1.4471e-6,  1.6620e-5,  2.6019e-5)
normalized unstable margin: +0.1535974700
incident active source indices: spiral 121, 88, 94.
```

The sole saddle is

```text
true primal edge: (65,166)
normalized full four-condition margin: +0.4109856547
incident active source rows arise from spiral indices 29 and 82.
```

Thus the residual `U-H` pair is produced inside the noncritical spiral, not at the dedicated unstable fan. The fan apex does not survive as the sole active maximum. This is the precise finite patch-interface failure.

The integrated volume and centroid are

```text
volume = 5.6108310282753405e-15
centroid =
 (1.6109310144726045e-6,
  2.3105524172275686e-6,
  2.2827846856766716e-6).
```

The exact first-moment correction required at the construction center is therefore

```text
M = volume * centroid
  = (9.03866172e-21,
     1.29641192e-20,
     1.28083191e-20),
||M|| = 2.0342537489856153e-20.
```

Re-evaluating every actual feature at that own uniform-volume centroid gives

```text
(S,U,H) = (8,4,10).
```

This own-centroid result is decisive: the tiny absolute centroid displacement is not mechanically tiny relative to the shrunken body. No auxiliary-center claim is being made.

# Four-actuator test and exact failed cone condition

For every actual maximal face `F_i`, I computed its area `A_i`, area centroid `b_i`, support distance `h_i`, and single-pyramid visibility radius `tau_i,max`. Adding the theorem’s radial apex

```text
a_i(tau_i) = (1+tau_i)b_i
```

would add first moment

```text
Delta M_i = k_i (tau_i+tau_i^2/4)b_i,
k_i = A_i h_i/3.
```

The visibility radii of all 89 faces range from

```text
0.00018039925138225483
to
0.15046522 approximately.
```

The coefficients `k_i` range from approximately

```text
2.4518e-19 to 4.0311e-16.
```

After requiring a nonstable base-face margin below `-0.003`, visibility radius above `2e-4`, and pairwise vertex-disjoint bases, 28 safe existing faces remained. I enumerated every four-face subset and solved

```text
sum_i k_i tau_i b_i = -M,
0 <= tau_i <= 0.7 tau_i,max.
```

There were **zero feasible four-face positive solutions**. Hence the required correction is not in the positive first-moment cone of any four disjoint pre-existing safe facets of this finite body.

This does not contradict Lángi’s theorem: the proof reserves four specially chosen control regions whose directions positively span the origin before the final cover is constructed. The computation shows that selecting four ordinary surviving spiral facets afterward is insufficient. The missing finite obligation is therefore precise:

> four dedicated base polygons must be inserted before the noncritical cover is closed, with area-centroid directions selected to positively span `-M` and with enough independent visibility depth to contain the nonlinear correction.

# Rejected apparent winners

A 30,000-state parameter scan found several bodies classified as `(1,1,0)` when a `1e-9` equilibrium threshold was used. They were all rejected under zero-threshold reconstruction. Representative failures were:

```text
W=7, cN=4, gamma=0.08, phase=pi/2:
  threshold class (1,1,0)
  literal class (4,1,4)
  extra positive margins down to 1.09e-16.

W=5, cN=3, gamma=0.20, phase=pi:
  threshold class (1,1,0)
  literal class (3,1,3)
  extra positive margins down to 1.72e-16.

W=6, cN=3, gamma=0.24, phase=pi/6:
  threshold class (1,1,0)
  literal class (2,1,0)
  extra stable-face margin 4.452385035285875e-16.
```

The source of these walls is the absolute recursion condition: when support rows have norms as large as `10^8`–`10^12`, an absolute dot-product margin of `1e-8` becomes a dimensionless separation near machine zero. None is a winner or acceptable fallback.

A relative-slack continuation was initiated by replacing the recursion with

```text
q_next·q_i >= (1+epsilon_rel)||q_next||^2
```

and similarly strengthening the stable cap. It did not complete to a certified endpoint within this turn, so no conclusion is claimed from that unfinished sweep.

# Exact secondary fallback retained from the resolved branch

The prior exact rational eight-vertex body remains fully certified as

```text
(V,E,F,C)=(8,18,12,36),
(S,U,H)=(2,2,2),
exact centered first moments=(0,0,0).
```

Its live block is extra stable face `[4,7,6]`, extra unstable vertex `2`, and saddle edges `(2,7)` and `(3,4)`. It has normalized nonincident support separation `0.009032475307346563` and a certified independent coordinate perturbation radius `1/50000`. It is not a Gömböc.

# Strongest continuation

The next construction should retain the finite spiral idea but change three components simultaneously:

1. Use a **relative** projection-foot margin, preferably initially `epsilon_rel` between `1e-4` and `1e-2`, so every noncritical exclusion remains dimensionless and open after scaling.
2. Reserve four small polygonal bases before closing the spiral. Choose their area-centroid directions near the vertices of a tetrahedron containing the required correction direction in its interior, and solve the full nonlinear equations `sum k_i(tau_i+tau_i^2/4)b_i=-M` as hard constraints.
3. Replace the terminal spiral/fan interface so the three concurrent fan rows form the active Q facet dual to the unique primal apex; the current residual source indices `29,37,46,73,82,88,94,121` should be deactivated or rerouted in the same topology change.

Only after an open construction-center `(1,1,0)` chamber and a feasible four-actuator cone coexist should the active H rows be rationalized and subjected to exact H- and V-driven reconstruction.

# Reproducible artifacts

- Literal spiral generator (`spiral_cover.py`)
- Independent polar H/V reconstruction and full-normal-cone auditor (`polar_fast.py`)
- Materialized W=8 theorem-guided body (`SPIRAL_b0.00625_a-0.3333333333333333_W8.pkl`)
- Construction scan transcript (`spiral_cover.log`)
- Apparent-winner scan transcript (`scan_spiral_params.log`)
- Zero-threshold target inspection (`inspect_spiral_targets.log`)
- Four-actuator enumeration code (`analyze_spiral_actuators_fast.py`)
- Four-actuator result transcript (`analyze_spiral_actuators_fast.log`)
- Exact certified eight-vertex secondary bundle (`fourier_k3_resolved_branch_bundle.zip`)

No OBJ/STL or exact rational certificate is emitted for the new spiral body because its own-centroid class is not the target and the absolute-margin construction is insufficiently separated for rationalization.
