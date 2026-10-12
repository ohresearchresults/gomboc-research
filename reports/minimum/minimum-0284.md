# minimum-0284

AI research report · 2026-09-27 UTC · [Export notes](../../catalog/coverage.md#text-records)

<!-- historical-status:start -->
> **Historical AI report.** The title and claims below reflect the AI’s assessment at the time. Claims of proof, certification or completion are not a current verification verdict.
>
> Minimum’s C≥34 remains a working lower bound requiring a consolidated proof. [C622](../../C622/README.md) passes the supplied exact checks. See [verification status and source gaps](../../catalog/coverage.md).
<!-- historical-status:end -->

---

# H5_CORNER_CAP_VOLUME_BOUNDARY_V1
## Sharp positive-volume boundary classification; larger-cut exclusion not established

### 1. Status

The requested substantial extension beyond QUARTER and WIDE was **not established in this execution**. No new complete interior U1 packet, own110weak000 body, or all-root corner-third/central-half certificate is promoted.

The last durable all-metric coverage remains the literal parent

```
minimum-0280
2e8a9d98288afbdc7ce98ed8ec9a1fc4ef8f95371f37c170f46471bf32381c8a.
```

Its QUARTER, WIDE and BAND conclusions and exact certificate identities are unchanged. The earlier five-parameter theorem remains a separate, partly nonnested exclusion. No whole-incidence count or global bound changes: **34<=Cmin<=622** remains the working bracket.

An auxiliary analytic result is supplied below: the sharp minimum of the actual compact six-volume over every corner-cap class up to central-half, the complete equality configurations, and a precise explanation of why a putative U1 sequence cannot accumulate at those volume minimizers. This is a boundary classification and an existential exclusion collar, **not** the substantial evaluated larger-cut region requested in the assignment.

### 2. Exact input and execution boundary

The continuation record contains complete consecutive reading of the new journal through line 1440, including the changed shared memory, branch memory, theorem statement of the required parent and its recovery instructions. The native journal is identified by

```
/mnt/data/research-journal(20260927-191148).md
355301 bytes, 1715 logical lines
6a431f9baf39d673ffc72ade72aa22c7e19cf0413313311893c0b4aa850c8ef2.
```

Reading lines 1441–1715, inspecting the retained source bundle, and elementary runtime checks were attempted in this resumed segment. Their returned content was not inspectable in my context. Consequently I cannot claim completion of the new journal's final-tail reading, successful fresh extraction, a running search, a new exact PASS marker, or new source/output hashes. The missing tail is in the parent's recovery payload; the earlier complete parent response remains in this conversation, but that does not substitute for falsely claiming an observed read of the new native tail.

The computational limitation is specific to this resumed execution. It is **not** evidence that the parent's programs or certificates fail. In particular, it does not alter the parent's recorded observed exact checks, source-only recovery qualifications, or its handling of numerical rounding variants.

No newly generated stress array or partially covered tree list is a successor checkpoint. The retained parent bundle and its complete six-source recovery remain the computational restart point:

```
H5_NINE_MODULI_CERTIFIED_REGIONS_U2_V1.zip

h5_nine_exact.py
30665 bytes
ca132f45c0d1a6323a0eafa4bf82bd9f196065571a42f9449215351b3a50dcc2

h5_quarter_completion.py
5889 bytes
decfb6678c3d3aa6ddf6f08666f39b1d1365b91fe29709962153c2d0bf61177e

h5_quarter_gap.py
5986 bytes
4cbbc4176d94e60913697721b60f58a7f47da2cece0a7bc2aee67ece1b7477e0.
```

The analytic calculation below uses the explicit actual-moment identities already supplied in the complete parent. It requires no unprovided archive, numerical optimizer or inferred execution result.

### 3. Sharp six-volume envelope for every corner cap

Let the six independent depths be

```
b, C=1-c, p, q, a, E=1-d,
```

and impose a common cap

```
0 < b,C,p,q,a,E <= delta,   0<delta<=1/2.
```

Retain the literal chart's strict incidence conditions. At delta=1/2, parameter combinations that collapse a required edge are limits, not genuine members.

Parameterize the entire origin-corner triangle by

```
u_B=b*t*h,
v_B=a*t*(1-h),
0<t,h<1.
```

Use the compact affine gauge

```
lambda=rho/(1+rho), s=1-lambda,
Z_i=(s B_i,0), i=0,...,6,
Z7=(0,0,1), Z8=(lambda,0,1), Z9=(0,lambda,1).
```

The genuine uniform-volume identities are

```
A2=2 Area(B)=1-a*b*t-C*p-E*q,
D=6 Vol(P_compact)=lambda+A2*(1-lambda)^2.
```

Put

```
m(delta)=1-3 delta^2.
```

Then the exact minimum on the indexed closed parameter compactification is

```
D_min(delta) = 1-1/[4(1-3 delta^2)]   when 0<delta<=1/sqrt(6),
D_min(delta) = 1-3 delta^2           when 1/sqrt(6)<=delta<=1/2.
```

The corresponding minimizing taper is unique:

```
lambda_min(delta)=1-1/[2(1-3 delta^2)]   when delta<1/sqrt(6),
lambda_min(delta)=0                    when delta>=1/sqrt(6).
```

The two formulas agree at delta=1/sqrt(6).

#### Proof

Each of the three removed basal double-areas satisfies

```
a*b*t <= delta^2,
C*p <= delta^2,
E*q <= delta^2.
```

Therefore A2>=m(delta)>0. For every lambda<1, D is strictly increasing in A2. The point lambda=1 has D=1 and cannot attain the displayed minimum. It is therefore sufficient, and necessary at equality, to minimize

```
f(lambda)=lambda+m(delta)*(1-lambda)^2
```

on [0,1]. Its derivative is `1-2m(delta)(1-lambda)` and its second derivative is `2m(delta)>0`.

For m>=1/2, the unique minimum is at `lambda=1-1/(2m)` and equals `1-1/(4m)`. For m<=1/2, the minimum is at lambda=0 and equals m. This gives the formulas above without sampling or coefficient pruning.

In particular,

```
corner-quarter: delta=1/4, D_min=9/13, lambda_min=5/13;
corner-third:   delta=1/3, D_min=5/8,  lambda_min=1/4;
central-half:   delta=1/2, D_min=1/4,  lambda_min=0.
```

These are sharp bounds, not merely sufficient volume estimates.

### 4. Complete equality geometry

For every delta>0, equality A2=m(delta) forces equality in all three separate product bounds. Thus it forces

```
b=C=p=q=a=E=delta,
t=1.
```

The parameter h remains free, but only as the position of a redundant label:

```
(u_B,v_B)=(delta h,delta(1-h)).
```

Label 6 lies on the straight segment joining `(delta,0)` and `(0,delta)`. The actual basal body is the fixed centrally symmetric hexagon

```
(delta,0),
(1-delta,0),
(1-delta,delta),
(delta,1-delta),
(0,1-delta),
(0,delta).
```

For 0<delta<1/2 these are six true vertices. The varying h does not change the uniformly filled body or its centroid. It must not be treated as a free vertex mass or as a new true corner.

There are three cases.

**For 0<delta<1/sqrt(6):** the minimizing lambda is positive. The actual compact body has six basal vertices and three top vertices: **9 vertices, 15 edges, 8 facets**. The two origin-corner triangular facets of the indexed ten-label model merge into one true triangle. Its volume is positive.

**For 1/sqrt(6)<=delta<1/2:** the minimizing lambda is zero. The three top labels coincide at `(0,0,1)`. The actual limit is the hexagonal pyramid, with **7 vertices, 12 edges, 7 facets**.

**For delta=1/2:** the three pairs of basal labels also coincide. The actual volume minimizer is the tetrahedron

```
(1/2,0,0), (1/2,1/2,0), (0,1/2,0), (0,0,1),
```

with

```
Vol=1/24,
g=(1/4,1/4,1/4).
```

Thus every volume-minimizing indexed configuration has a full-dimensional actual hull with at most nine true vertices. None is an interior ten-vertex candidate, and none is the zero-volume raw-gauge artifact from the earlier countercontrol.

### 5. Exact corner-third boundary object

At delta=1/3, the minimizing compact body has the complete true vertex list

```
0=(1/4,0,0)
1=(1/2,0,0)
2=(1/2,1/4,0)
3=(1/4,1/2,0)
4=(0,1/2,0)
5=(0,1/4,0)
7=(0,0,1)
8=(1/4,0,1)
9=(0,1/4,1).
```

The optional indexed label `6=(h/4,(1-h)/4,0)` lies on the true edge 05 and is not a tenth vertex.

Its outward true maximal facet cycles are

```
(5,4,3,2,1,0),
(8,7,0,1),
(7,5,0),
(1,2,8),
(9,8,2,3),
(9,3,4),
(4,5,7,9),
(7,8,9).
```

The true edges are

```
01,05,07,12,18,23,28,34,39,45,49,57,78,79,89.
```

Its actual moments are

```
D=6 Vol=5/8,
Vol=5/48,
J24=24 integral Z=(15/32,15/32,15/16),
g=J24/(4D)=(3/16,3/16,3/8).
```

These follow directly from the parent moment identities. At the equality configuration, the two horizontal first-moment numerators simplify, independently of h, to

```
J24_x=J24_y
 =A2*s^3+(1-delta^2)*s^2*lambda+lambda^2,
J24_z=A2*s^2+2lambda+lambda^2.
```

Substitution of `A2=2/3,s=3/4,lambda=1/4` gives the displayed fractions. This is a complete literal recovery of the actual limit body and its uniform centroid. No new full S/U/H census under a chosen SPD metric is asserted for it, and no new computer verification is claimed.

### 6. Consequence for complete weak rooted systems

Using the accepted **nonzero-PSD contained-refinement theorem for full-dimensional actual uniform bodies with at most nine true vertices**, the volume minimizers above cannot be accumulation points of complete U1 systems. This uses that theorem with its indexed-refinement qualification, not strict-equilibrium persistence alone. The supplied record expressly distinguishes this full-dimensional theorem from dimension-loss assertions.

Precisely, for each fixed delta in (0,1/2], there exists a positive number eta_delta such that no complete true weak rooted system occurs in the corner-cap class with

```
D <= D_min(delta)+eta_delta.
```

Here eta_delta is **not evaluated**, and no useful numerical search cutoff is claimed.

To prove this consequence, suppose instead that a sequence of actual ten-vertex bodies with complete weak rooted systems has D tending to D_min. Work in the compact affine gauge and normalize each physical SPD metric by trace one. The vertex coordinates and metrics have convergent subsequences; the limiting metric is nonzero PSD. There are finitely many labelled rooted trees, so pass to a subsequence with one fixed tree.

The positive bound `D>=m(delta)>0` makes the actual centroid continuous under this convergence. Therefore all selected weak inequalities pass to the limit. The equality classification puts the limiting actual body in one of the full-dimensional at-most-nine-vertex configurations above, with the old labels only as contained refinements. The accepted refinement theorem excludes precisely that nonzero-PSD weak rooted system, a contradiction.

This quantifies the logical role of volume minimization: the sharp lower-volume boundary is already controlled by a lower-feature actual body. It does **not** exclude the larger-volume interior, provide a complete corner-third certificate, or yield an evaluated substantial new region. It should not be reported as completion of the active assignment.

### 7. Computational continuation boundary

No new accepted closed cells or actual interior survivor were obtained in this execution. In particular:

```
New evaluated corner-third cells accepted: none.
New evaluated central-half cells accepted: none.
New full actual U1 controls: none.
New own110weak000 controls: none.
New complete stress-certificate checkpoint: none.
```

This is not a failed-search exclusion. No conclusion about feasibility is drawn from the missing execution feedback.

The appropriate restart is the existing aggregate-before-remainder compiler, retaining independent positive arrow multipliers, all original edge energies and the actual J24. The new cross-branch warning about centroid-balanced subtree loads is respected: such a restriction is not a valid replacement for the independent coefficient cone.

For corner-third, a natural complete target is

```
0<b,C,p,q,a,E<=1/3,
0<t,h<1,
0<lambda<1,
u_B=b*t*h,
v_B=a*t*(1-h).
```

Its larger-cut part is not exhausted by the prior QUARTER or WIDE domains. The exact positive lower volume 5/8 permits the ordinary compact-coordinate stress reference. The anisotropic raw reference from the earlier dimension-loss example is not needed merely because some indexed endpoint labels merge here.

Before promoting a successor, the resumed execution must first finish the new journal-tail reading and obtain inspectable exact checker output. It must then cover every residual tree in both children of each subdivision, or provide a logically complete structural replacement. An empty finite stress library, a failed locator, an unchecked coefficient cell, or an indexed boundary solution does not meet that boundary.

The main unresolved scientific question is still the actual larger-cut interior. The sharp volume envelope and its explicit equality bodies identify one controlled boundary, but they do not decide that interior or change the global complexity bracket.
