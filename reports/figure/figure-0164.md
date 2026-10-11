# figure-0164

Historical AI scientific report · saved 2026-08-30 UTC. Claims below retain their original status and have not all been independently checked. The current retained construction is C622; the C<500 search remains open.

---

# Rapid Quartz 69 — outlet-spanning search handoff

## Literal verdict

**No certified homogeneous polyhedral Gömböc was obtained in this continuation.** The strict acceptance gate remains a finite uniform-density convex polyhedron evaluated at its own exact volume centroid, with class `(S,U,H)=(1,1,0)`, complete irredundant H/V incidence, every maximal face and true edge, exhaustive full-cone mechanics, an open perturbation certificate, an independent verifier, and matching meshes. :contentReference[oaicite:0]{index=0}

The strongest **fully certified** object therefore remains the exact-dyadic predecessor `AQ32-CR3D580`, whose own-centred polar has class `(2075,587,2660)`. The new work did not produce the requested exact post-outlet endpoint, but it found a materially stronger finite search cell: an exact-dyadic outlet-spanning support replacement whose fixed topology admits many numerical SPD images of strict class `(2,2,2)`. That is a reduction from thousands of equilibria to one Euler-neutral four-feature block. The new cell has not yet passed exact incidence repair, interval Santaló isolation after rational metric exactification, or independent mesh verification, so it is **not** claimed as an accepted exact endpoint.

## Reusable files

### Certified predecessor

- [AQ32-CR3D580 exact mathematical handoff](sandbox:/mnt/data/RQ69_AQ32_CR3D580_exact_endpoint/AQ32_CR3D580_complete_handoff.md)
- [Exact deterministic generator](sandbox:/mnt/data/RQ69_AQ32_CR3D580_exact_endpoint/generate_AQ32_CR3D580_exact.py)
- [Independent verifier](sandbox:/mnt/data/RQ69_AQ32_CR3D580_exact_endpoint/verify_AQ32_CR3D580_exact.py)
- [Canonical exact arrays](sandbox:/mnt/data/RQ69_AQ32_CR3D580_exact_endpoint/AQ32_CR3D580_exact_data.npz)
- [Root-box full-cone audit](sandbox:/mnt/data/RQ69_AQ32_CR3D580_exact_endpoint/AQ32_CR3D580_exact_rootbox_audit.json)
- [Q OBJ](sandbox:/mnt/data/RQ69_AQ32_CR3D580_exact_endpoint/AQ32_CR3D580_Q.obj), [Q STL](sandbox:/mnt/data/RQ69_AQ32_CR3D580_exact_endpoint/AQ32_CR3D580_Q.stl), [P OBJ](sandbox:/mnt/data/RQ69_AQ32_CR3D580_exact_endpoint/AQ32_CR3D580_P_at_santalo_midpoint.obj), and [P STL](sandbox:/mnt/data/RQ69_AQ32_CR3D580_exact_endpoint/AQ32_CR3D580_P_at_santalo_midpoint.stl)

### New outlet search cell

- [Exact-dyadic candidate coordinates and provisional lattice](sandbox:/mnt/data/RQ69_AQ32_OUTLET_WORK/e2bad.npz)
- [Complete deterministic construction parameters and numerical audit](sandbox:/mnt/data/RQ69_AQ32_OUTLET_WORK/e2bad.json)
- [Construction driver](sandbox:/mnt/data/RQ69_AQ32_OUTLET_WORK/search_continue.py)
- [Fixed-topology SPD full-cone evaluator](sandbox:/mnt/data/RQ69_AQ32_OUTLET_WORK/fast_metric.py)
- [Identity-free winner-margin evaluator](sandbox:/mnt/data/RQ69_AQ32_OUTLET_WORK/hard_metric.py)
- [Initial symmetry-breaking metric search](sandbox:/mnt/data/RQ69_AQ32_OUTLET_WORK/localm025_500.json)
- [Closest fixed-topology multiwall state](sandbox:/mnt/data/RQ69_AQ32_OUTLET_WORK/nm302.json)
- [Local first-order chamber analysis script](sandbox:/mnt/data/RQ69_AQ32_OUTLET_WORK/bundle_step.py)

These new files are search artifacts, not a replacement for the certified predecessor archive.

---

## 1. Exact-dyadic outlet-spanning support construction

The new point set starts directly from `AQ32-CR3D580` and uses the same denominator

```text
D=2^118
 =332306998946228968225951765070086144.
```

The protected stable square, unstable apex, critical collar, seam, and all untouched predecessor rows are retained. The simultaneous support replacement uses the following half-turn-paired ray starts:

```text
0.5:448, 1:448, 1.5:560, 2:559, 2.5:480,
3:545, 3.5:480, 4:497, 4.5:480, 5:550,
5.5:480, 6:556, 6.5:448, 7:448, 7.5:448,
```

with terminal indices

```text
0.5:600, 1:745, 1.5:600, 2:700, 2.5:590,
3:620, 3.5:580, 4:620, 4.5:590, 5:620,
5.5:590, 6:620, 6.5:590, 7:730, 7.5:600.
```

The construction uses the inherited full-cone separator recurrence with factor `1.1`, a common post-profile radial coefficient `-0.075`, and an independent sector-2 coefficient `-0.005`. Thus it spans the old terminal packet, the sectors `7/15` ladder, additional sectors `1/9` and `2/10`, and their connecting half-sector rails rather than attaching a single serial continuation.

The generated exact point table has

```text
candidate rows       25,837
modified old rows     1,898
inserted rows         2,038
provisionally active 22,033.
```

The provisional floating reconstruction has

```text
(V,E,F)_Q=(22033,66092,44061).
```

Its numerical Santaló root is approximately

```text
(-2.3492654374901147e-4,
  2.993516324505976e-10,
  4.4780693380755134e-10).
```

At the identity Euclidean metric this body is mechanically poor, with provisional Q class

```text
(481,7393,7872).
```

The significance of this point set is not its identity-metric class. It is that the outlet-spanning topology becomes a highly compressed mechanical object after a global centroid-preserving SPD change of metric.

## 2. Exact centring is preserved under the metric continuation

For a positive-definite map `A`, replace `Q` by `AQ`. Its Santaló point is exactly `A s(Q)`, and

```text
(AQ-A s(Q))° = A^{-T}(Q-s(Q))°.
```

Thus an invertible rational approximation to `A` preserves the hard own-centroid condition algebraically; no post hoc translation of the physical polyhedron is needed. Incidence is also unchanged by an exact invertible linear map.

The numerical search parameterized determinant-one SPD maps by

```text
S(p)=
[[p0,p1,p2],
 [p1,p3,p4],
 [p2,p4,-p0-p3]],

A(p)=exp(S(p)).
```

Every score rebuilt the transformed maximal-face projection tests, every transformed vertex tangent cone, and both full normal-cone coefficients of every true edge. No triangulation-diagonal or one-facet proxy was used.

## 3. Finite metric search result

A 1,000-state half-turn-invariant search first reached many strict numerical Q classes `(3,2,3)`. A subsequent 500-state full five-dimensional symmetry-breaking search produced numerous strict `(2,2,2)` states and no `(1,1,0)` state.

The most robust sampled `(2,2,2)` state found was

```text
p =
(-3.9866996248259476,
 -0.9601702950590143,
 -0.40702683197267975,
  0.2208860471635758,
  0.4225857490187912).
```

Its SPD condition number is approximately

```text
3158.7701782766635.
```

The complete numerical full-cone audit gives

```text
(S,U,H)_Q=(2,2,2).
```

The equilibrium features are:

### Stable faces

```text
face 5293, cycle [18761,18776,18760],
margin 0.0012299189897470749;

face 15955, cycle [9784,9801,9817],
margin 0.0006510072227045118.
```

The second face lies in the fine low-gamma background around rings `239–241`; the first lies near the far-side background around rings `931–932`.

### Unstable vertices

```text
row 14432, background ring 621, sector 4,
margin 37.41264638633824;

row 14437, background ring 621, sector 12,
margin 42.05606275495767.
```

### Saddle true edges

```text
edge index 2748, vertices (13283,14192),
margin 0.5671949429945881;

edge index 7678, vertices (14645,15596),
margin 0.2906126723910001.
```

The minimum positive equilibrium margin is

```text
6.510072227045118e-4,
```

and the closest excluded feature has numerical clearance

```text
6.509169026101858e-4.
```

This is an open floating-point chamber, not a transfer-wall false positive. It is nevertheless only a numerical metric image because `exp(S)` was not replaced by a dyadic SPD matrix and the underlying exact hull was not independently repaired and regenerated.

## 4. Fixed-topology attempt to enter `(1,1,0)`

For any metric state, sort the maximal-face scores `f_i`, vertex scores `v_i`, and true-edge scores `e_i` in descending order. Define the identity-free winner score

```text
h(p)=min(
  f_(1), -f_(2),
  v_(1), -v_(2),
  -e_(1)
).
```

A strict `(1,1,0)` chamber is equivalent to `h(p)>0`.

Differential-evolution exploration followed by an adaptive Nelder–Mead minimax continuation reached

```text
p* =
(-0.62543662157198,
  1.183240586443055,
  1.0492493278612183,
  1.0065948097657968,
 -0.3513071432561904).
```

Its class is

```text
(S,U,H)_Q=(2,5,5),
```

and its five winner components are

```text
[ 0.0021357324811272517,
 -0.0011269797208643799,
  0.06209692326909412,
 -0.0016223594606726139,
 -0.001655945037382145 ].
```

Hence

```text
h(p*)=-0.001655945037382145.
```

The optimizer did not merely retain the original two-pair block. It drove several transfer walls together and produced a five-channel outlet packet.

The principal residuals at `p*` are:

### Stable block

```text
preserved face 13131, cycle [21078,21077,12039],
margin 0.0021357324811272517;

extra face 8253, cycle [16675,16674,16658],
margin 0.0011269797208643799.
```

### Unstable block

```text
preserved row 15494, margin 0.06209692326909412;

row 13316, margin 0.0016223594606726139;
row 13304, margin 0.0016062280631333305;
row 13584, margin 0.0012222009113417036;
row 15193, margin 0.0011660599364714144.
```

### Saddle block

```text
edge (15183,15193), margin 0.001655945037382145;
edge (13572,13584), margin 0.001655941641958425;
edge (13304,13316), margin 0.0016062280631334858;
edge (13584,13596), margin 0.00122220091134162;
edge (15193,15203), margin 0.0011660599364713975.
```

The equality of each new vertex margin with an adjacent edge primitive exposes the mechanism: the attempted metric cancellation becomes a ladder of `U-H` transfers rather than an entrance into the open chamber.

## 5. Local chamber obstruction at the minimax state

A finite-difference bundle linearization was formed from the 30 largest face, vertex, and edge scores, preserving the leading stable face and unstable vertex and requiring every other feature to become negative.

For trust radii

```text
0.001, 0.003, 0.01, 0.03, 0.1, 0.3,
```

the optimal linearized common margins were all negative. The strongest was

```text
t_linear=-0.0013081064082447538
```

at `||delta p||_infinity<=0.3`.

Actual nonlinear line searches along the LP directions also remained negative; the best tested actual hard score was about

```text
-0.0015800527850177715.
```

This is **not** an exact or global impossibility theorem for the complete SPD orbit. It is a reproducible finite first-order obstruction showing that the closest sampled multiwall has no common local descent direction for all active transfer channels. A subsequent global NLopt search did not complete and contributes no evidence.

## 6. What the construction accomplished

Relative to the supplied journal, the important change is that the large outlet has been driven into a finite topology whose Euclidean metric orbit contains robust `(2,2,2)` chambers. The direct 12-stable/10-saddle packet and the sectors `7/15` coarse outlet were not treated independently: the support recurrence begins below both, adds the neighboring integer and half-sector routes, changes nearly two thousand old rows, and supplies more than two thousand candidate return rows.

The work therefore supports the following inference:

- the remaining obstruction is no longer simply the number of coarse-background equilibria;
- a connected volumetric outlet replacement plus a global SPD metric can compress the field to one Euler-neutral block;
- within the tested fixed topology, attempting to cross that block produces a longer `U-H` transfer ladder before the unique-equilibrium chamber opens.

## 7. What is incomplete

The new post-outlet cell does **not** satisfy the deliverable yet. Specifically:

1. The provisional active set and incidence in `e2bad.npz` were selected from a floating hull. The exact dyadic coordinates exist, but every diagonal, higher-valence face, and inactive row still needs independent exact-predicate reconstruction.
2. The robust `(2,2,2)` metric uses `A=exp(S(p))`, not an exact rational or dyadic matrix.
3. No directed Santaló root box has been recomputed for an exact rational metric image, although affine covariance gives the intended root transformation.
4. No interval full-cone ledger or perturbation box exists for the new metric endpoint.
5. No matching OBJ/STL was exported for the new endpoint.
6. The continuous circuit order of the simultaneous support replacement was not enumerated.

Accordingly, the exact certified endpoint remains `AQ32-CR3D580`; the new files are a discovery frontier, not a replacement certificate.

## 8. Smallest nonrepeating continuation

The next move should not extend another angular rail. It should exactify the robust `(2,2,2)` metric chamber first and then alter the complete four-feature basin it identifies.

### Exactification stage

1. Rebuild `e2bad` from its exact `2^-118` numerators using integer four-point predicates until every local diagonal is convex and every coplanar triangle is grouped into one maximal face.
2. Verify all candidate inactive rows against every actual maximal face by exact squared-distance comparison.
3. Replace the robust numerical SPD matrix by a nearby symmetric dyadic positive-definite matrix, preferably denominator `2^48` or `2^64`. Because the map is exact and invertible, incidence remains unchanged and the Santaló point transforms linearly.
4. Recompute the normalized Santaló equation independently and enclose the transformed root, positive projective denominators, full class, and a nonzero coordinate box.
5. Export and independently verify the Q/P meshes.

### New topology stage

The robust `(2,2,2)` state localizes the next connected cell to:

- the stable-face stars around cycles `[18761,18776,18760]` and `[9784,9801,9817]`;
- the unstable stars of rows `14432` and `14437`;
- the complete saddle stars of edges `(13283,14192)` and `(14645,15596)`.

These features are widely separated in the original angular parameter but close under the optimized metric. The smallest genuinely new architecture is therefore a metric-adapted **two-cell polar replacement**, not another source-sphere angular band:

1. add one nonsimplicial cell sharing a true edge with each saddle star;
2. join the two cells by a transverse interior edge so one stable–saddle and one unstable–saddle cancellation occur in the same circuit event;
3. allow both residual unstable rows or one residual stable face to become non-extreme, rather than passing the equilibrium to the next longitudinal row;
4. retain three independent rows as dependent normalized-Santaló controls;
5. rebuild and audit every actual incidence cell before continuing past a wall.

The exact transferred five-channel state `p*` shows what must be avoided: a replacement whose outlet ends on ordinary longitudinal edges recreates one unstable vertex and one saddle per terminal branch. Both terminal branches must instead terminate in one shared volumetric cell.

## Disposition

**Use this result as a finite numerical discovery and fixed-topology obstruction, not as an exact endpoint and not as a winner.** The outlet-spanning exact-dyadic support generator is reusable, and its SPD orbit contains robust numerical `(2,2,2)` states. No strict `(1,1,0)` state was found. The immediate continuation is exactification of the robust two-pair chamber followed by one shared two-cell replacement of its complete stable, unstable, and saddle stars.
