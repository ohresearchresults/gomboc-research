# figure-0052

Historical AI scientific report · saved 2026-08-24 UTC. Claims below retain their original status and have not all been independently checked. The current retained construction is C622; the C<500 search remains open.

---

# Verdict

**This direction did not produce an accepted homogeneous polyhedral Gömböc.** None of the bodies below simultaneously has an exactly certified own centroid and strict `(S,U,H)=(1,1,0)`. I am therefore not presenting any of them as the requested object. This preserves the run's acceptance gate: an auxiliary center, a numerical wall point, or an unmaterialized existence argument is insufficient. :contentReference[oaicite:7]{index=7}

What did emerge is a materially stronger Santaló/projective branch: a completely materialized complexity-200 family, an exactly centroid-hardwired projective parameterization in principle, a centered numerical `(2,2,2)` member whose entire remaining defect is four localized inequalities, and differentiable continuation code over more than one hundred shape, centering, and metric variables.

## 1. Family explored

I used a convex polyhedron `Q` with one pentagonal face and otherwise triangular facets. Its polar `P=Q°` is evaluated relative to the origin. The inherited identity says that translating `Q` to its Santaló point before polarity makes the uniform-volume centroid of the polar equal to the origin; nondegenerate polarity exchanges stable faces and unstable vertices. :contentReference[oaicite:8]{index=8} The Santaló characterization used here is the standard first-variation statement that `s(Q)=0` iff the barycenter of `Q°` is zero; a primary bibliographic locator is Meyer–Pajor, *On Santaló's inequality*, LNM 1469 (1991), pp. 261–263.

Polyhedral equilibrium definitions and the relation `S+U-H=2` follow Domokos–Kovács. :contentReference[oaicite:2]{index=2} Lángi's primary existence result remains qualitative rather than a source of materialized coordinates. :contentReference[oaicite:3]{index=3}

The realization-space model frees every non-apex, non-bottom vertex of `Q`, frees the bottom polygon in its plane, reconstructs every polar vertex by a `3×3` solve, and differentiates the exact tetrahedral formula for the polar volume centroid. A second gauge-equivalent model also frees the relative tilt between the unique stable face and unstable direction. The complete fixed-cell constraints include every facet-support inequality, target equilibrium inequality, one explicit killing witness for every unwanted face and vertex, and one killing component for every true edge.

Core code:

- [Floating face-lattice, centroid, polarity, and exhaustive classifier](sandbox:/mnt/data/gomboc_slot1/geom.py)
- [General differentiable polar model](sandbox:/mnt/data/gomboc_slot1/torch_qmodel_general.py)
- [Relative-tilt extension](sandbox:/mnt/data/gomboc_slot1/torch_qmodel_tilt.py)
- [Sequential linearized continuation](sandbox:/mnt/data/gomboc_slot1/slp_tilt_fast.py)

## 2. Strong auxiliary-center member

The most useful robust seed is [Q_re36d_best.npy](sandbox:/mnt/data/gomboc_slot1/Q_re36d_best.npy).

For `Q`:

- `(V,E,F)=(36,100,66)`;
- one pentagonal maximal face and 65 triangular maximal faces;
- strict origin-relative class `(S,U,H)=(1,1,0)`;
- target stable-face margin approximately `0.1698174954`;
- target unstable-vertex margin approximately `0.3373034195`;
- largest unwanted face score `-0.00204043194`;
- largest unwanted vertex score `-0.000402032679`;
- largest true-edge saddle score `-0.00334132475`.

Its polar therefore has `(V,E,F)=(66,100,36)` and complexity `C=200`, also strict `(1,1,0)` relative to the origin. Its own uniform-volume centroid is

`(-0.00070219, -0.00095842, -0.35925494)`

with volume approximately `12.40505161`. Thus it is a robust, low-complexity **artificial-center** Gömböc but not homogeneous at the mechanical point.

A closer but less robust member is [Q_re36e_best.npy](sandbox:/mnt/data/gomboc_slot1/Q_re36e_best.npy). Its polar centroid is approximately

`(-0.00074641, -0.00084777, -0.35506492)`

and its largest unwanted face, vertex, and edge scores are approximately `-6.07×10^-4`, `-1.29×10^-4`, and `-1.66×10^-3`.

A fixed-cell tilt continuation reached [Q_slp_tilt_fast3_best.npy](sandbox:/mnt/data/gomboc_slot1/Q_slp_tilt_fast3_best.npy), whose polar centroid is approximately

`(0.000166083, -0.000199981, -0.347998843)`.

This last point is not robust: the closest unwanted face has score about `-2.5354×10^-8`, and numerous side faces, vertices, and endpoint-transfer edges lie between roughly `10^-8` and `10^-6` from equilibrium. It is a genuine chamber wall, not a candidate for rationalization.

## 3. Sharp obstruction inside the nested-ring subfamily

The continuation from the original 21-vertex Santaló seed changed the polar centroid approximately as follows:

- 21-vertex initial seed: `c_z≈-3.04287`;
- optimized 21-vertex seed: `c_z≈-0.601704`;
- 26 vertices: `c_z≈-0.481627`;
- 31 vertices: `c_z≈-0.422422`;
- 36 vertices: `c_z≈-0.355065`.

Each five-vertex extension replaces the polar's lower apex by another pentagonal truncation. Two further nested rings can retain `(1,1,0)`, but a third similarly tapered ring creates a robust stable-face/saddle pair rather than numerical dust. The materialized counterexample is [Q_tail3_bad.npy](sandbox:/mnt/data/gomboc_slot1/Q_tail3_bad.npy): its class is `(2,1,1)`, the new stable-face margin is approximately `0.0244155`, and the paired saddle is open with margin of order `0.27`. Therefore an indefinitely nested, nearly coaxial pentagonal “centroid brake” is not a live route. The next patch must break meridional monotonicity through a nonlocal asymmetric corridor or a different topology.

This agrees with the inherited warning that local support changes merely transfer the unwanted equilibrium, and that a complete basin or separatrix-spanning corridor has to be replaced. :contentReference[oaicite:9]{index=9}

## 4. Projective centering plus metric search

A projective transformation fixing the origin was then applied:

`T_p(x)=x/(1+p·x)`.

For the polar of `Q_re36d_best`, solving its three centroid equations gives

`p ≈ (0.00062705, -0.00149474, -0.19210035)`

with minimum vertex denominator approximately `0.82412756`. The transformed body's computed centroid norm is below `10^-16`. The centered coordinates are materialized in [PC_Q_re36d_best.npy](sandbox:/mnt/data/gomboc_slot1/PC_Q_re36d_best.npy), and the centering routine is [projective_metric.py](sandbox:/mnt/data/gomboc_slot1/projective_metric.py).

The identity metric gives many equilibria, so I searched the five-dimensional space of determinant-one positive-definite metrics. The metric is represented as `A=exp(S)`, where `S` is symmetric and trace-free; applying `A` preserves the zero centroid algebraically.

The strongest centered member found before local polishing uses [x_metric_re36d.npy](sandbox:/mnt/data/gomboc_slot1/x_metric_re36d.npy). It has exhaustive numerical class `(2,2,2)`. In the fixed complete witness cell used by the differentiable verifier, only four constraints are violated:

1. unwanted vertex 14: `-0.09556307196`;
2. unwanted face 20, edge witness 3: `-0.05467869460`;
3. saddle edge `(2,3)`: `-0.03506572102`;
4. saddle edge `(29,47)`: `-0.03078075469`.

The next-smallest fixed-witness constraint is positive, approximately `+0.03520345216`. The selected equilibrium retained as target is face 7 and vertex 59. The original `Q` realization remains comfortably convex in this parameterization, with minimum normalized fixed-cell convexity slack approximately `0.00359870819`, and the projective denominator margin remains about `0.8241`.

This is the sharpest live subproblem produced here: a centered, fully materialized complexity-200 polyhedron with one extra face, one extra vertex, and their two saddle connections, separated from every other feature by a useful margin.

Metric-only Nelder–Mead polishing did not cancel this block. It converged to a different centered `(3,3,4)` chamber with hard defect approximately `0.01442115718`; see [x_metric_re36d_local.npy](sandbox:/mnt/data/gomboc_slot1/x_metric_re36d_local.npy). An independent start from the slightly closer 36-vertex seed converged to a `(4,2,4)` chamber with defect approximately `0.0161561`; see [x_metric_re36e_local.npy](sandbox:/mnt/data/gomboc_slot1/x_metric_re36e_local.npy). These negative results are local, not exclusions of the full shape family.

The fast complete fixed-lattice metric evaluator is [metric_fast.py](sandbox:/mnt/data/gomboc_slot1/metric_fast.py).

## 5. Joint shape–projective–metric continuation

I implemented a differentiable joint model in [projective_shape_torch.py](sandbox:/mnt/data/gomboc_slot1/projective_shape_torch.py). Its variables comprise:

- 101 realization parameters for the 36-vertex `Q` cell;
- three projective-centering parameters;
- five trace-free metric parameters.

At each evaluation it reconstructs all 66 polar vertices, applies the projective map and metric, computes the complete tetrahedral volume centroid, evaluates every maximal face, every vertex, and every true edge, and enforces the full `Q` realization inequalities. The initial state reproduces the centered `(2,2,2)` body and the four violations listed above.

The first penalized L-BFGS run was inconclusive: it reduced some individual violations but repeatedly traded them against centroid displacement and neighboring feature births; it did not beat the initial four-defect state before the run ended. The continuation driver is [projective_shape_opt.py](sandbox:/mnt/data/gomboc_slot1/projective_shape_opt.py), and its initial/checkpoint vector is [z_pshape_best.npy](sandbox:/mnt/data/gomboc_slot1/z_pshape_best.npy). This file is a continuation checkpoint, not a witness.

## 6. Reproduction

From `/mnt/data/gomboc_slot1`, the robust auxiliary-center audit is reproduced by:

```python
import numpy as np
from geom import classify, polar_vertices_from_Q, centroid_poly

Q = np.load('Q_re36d_best.npy')
P, _ = polar_vertices_from_Q(Q)
print(len(Q), len(classify(Q, np.zeros(3))['edge_faces']),
      len(classify(Q, np.zeros(3))['faces']))
print('Q class:', *(len(classify(Q, np.zeros(3))[k])
                    for k in ('stable', 'unstable', 'saddle')))
print('P class:', *(len(classify(P, np.zeros(3))[k])
                    for k in ('stable', 'unstable', 'saddle')))
print('P centroid and volume:', centroid_poly(P))
```

The centered metric near-miss is reproduced by:

```python
import numpy as np
from geom import polar_vertices_from_Q, centroid_poly, classify
from projective_metric import center_projective
from metric_fast import MetricEvaluator

Q = np.load('Q_re36d_best.npy')
P, _ = polar_vertices_from_Q(Q)
p, W, c = center_projective(P)
x = np.load('x_metric_re36d.npy')
E = MetricEvaluator(W)
hard, cls, margins, V = E.cls(x)
print('p:', p)
print('centered centroid:', centroid_poly(W)[0])
print('metric class:', cls)
print('hard score and margins:', hard, margins)
print('final centroid:', centroid_poly(V)[0])
```

## 7. Exact facts, numerical evidence, and missing obligations

**Exact structural facts:** projective and invertible linear maps preserve the finite face lattice while their denominators stay positive; an invertible linear map preserves a zero centroid; the Santaló first-variation characterization hardwires the polar centroid; all reported complexity counts follow from materialized finite arrays and Euler incidence.

**Numerical evidence:** every coordinate, centroid, margin, and equilibrium count reported for this worker's new bodies is presently double-precision output. The robust auxiliary-center seed has milliscale mechanical margins, but the centered `(2,2,2)` and metric continuations have not been rationalized or interval-certified.

**Still missing:** a strict centered `(1,1,0)` member; rational or isolated algebraic coordinates; exact centroid proof for a winning finite array; directed-rounding all-feature audit; independently reconstructed incidence certificate; OBJ/STL for a winner. Consequently this work does not meet the restored practical-object requirement. :contentReference[oaicite:10]{index=10}

## 8. Most useful continuation

Continue from the centered `(2,2,2)` state, not from the near-degenerate `c_z≈-0.348` ring wall. Restrict the 101 shape variables initially to vertices incident to face 20, vertex 14, and edges `(2,3)` and `(29,47)`, while retaining the three projective variables as exact centroid actuators and the five metric variables as mechanical controls. Solve the four killing inequalities plus the three centroid equations by constrained SQP or an interval-Newton continuation, with every other current witness held above roughly `0.01`. Alternate both choices of which member of each extra equilibrium pair is retained. Only after obtaining a margin above `10^-4` should the coordinates be rationalized and subjected to the exact face-lattice and own-centroid audit.
