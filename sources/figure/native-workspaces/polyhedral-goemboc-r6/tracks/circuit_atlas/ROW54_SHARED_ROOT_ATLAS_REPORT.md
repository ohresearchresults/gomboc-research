# Row54 rank-six shared-root and transverse actual-cell atlas

## Starting cell and packet

The source is `row54_multiwall_flip.csv` with the raw-minimum metric from
`row54_multicell_rawmin_local_831593.json`.  A fresh hull has all 61 rows,
`f=(61,162,103)`, the enlarged stable base, U8, all 37 forced rail edges, and
the fixed `{2,3,88,242}` flip-cell faces.  Its six wrong requested signs are

```text
S[7,8,246] = -0.001043719805009532
U6          = -0.003267191220711787
U54         = -0.005196549847431052
H(5,6)      = -0.000289055951192774
H(6,7)      = -0.000814387712362790
H(9,10)     = -0.005196549847419131
```

The six-row Jacobian has rank six in metric-8, base-36, and joint-44
controls.  Hence this investigation concerns nonlinear first events and the
actual hull cell, not a rank loss.

## Six nonlinear square charts

`row54_shared_root_atlas.py` continues the exact nonlinear equations

```text
g_six(x(t)) = (1-t) g_six(x(0))
```

in QR-pivot and SVD charts for metric, base, and joint controls.  Every
accepted node is rebuilt by Qhull and checked with its own volume centroid.

| chart | result | first actual event |
|---|---|---|
| metric SVD | no correctable branch at `t=2.44e-4`; linear root requires `Linf≈349` | directional topology event |
| metric QR | no correctable branch at `t=2.44e-4`; linear root requires `Linf≈530` | directional topology event |
| base SVD | shared root exists outside the cell | support circuit near `t=7.22e-5` |
| base QR | shared root exists outside the cell | paired `U0/H(0,54)`, `t∈[0.0165942311,0.0165942609]` |
| joint SVD | shared root exists outside the cell | support circuit near `t=0.00189136` |
| joint QR | shared root exists outside the cell | paired `U0/H(0,54)`, `t∈[0.0163513422,0.0163513720]` |

No square-chart common root is an actual-cell root.  This by itself is not a
global obstruction because the joint Jacobian has a 38-dimensional kernel.

## Exact first paired event

The base/joint QR events called `U0` and `H(0,54)` are exactly the same scalar
wall.  With own-centroid vectors `x0`, `x54` and `d=x54-x0`, the active
components are

```text
U0 component at neighbor 54 = -x0·d / (||x0|| ||d||)
H(0,54) endpoint component  = -x0·d / ||d||^2.
```

After applying the requested negative signs, both guards have the same
numerator `x0·d` and a strictly positive ratio `||x0||/||d||`.  Their zeros
therefore coincide identically, not just to floating precision.  The full-44
active cone at this paired wall is feasible, so it is a branch blocker but not
a global blocker.

Primary atlas artifacts:

- `row54_shared_root_atlas.py`
- `row54_shared_root_atlas.json`
- `row54_first_event_blocker.csv`, `_faces.json`, `_audit.json`

## Active-set transverse bypass

`row54_shared_root_active_set.py` promotes a first-event scalar/circuit to a
one-sided preserved wall and rebuilds a larger joint rank-revealing chart.
The deterministic bypass sequence is

```text
U0/H(0,54) common radial-edge numerator
support circuit {7,8,245,246}
support circuit {11,198,262,263}
support circuit {9,198,263,264}.
```

The resulting ten-equation square QR and SVD correctors are ill-conditioned
and stop near the source, but the complete 44-control active-cone LP is
feasible at their last actual-cell nodes.  Thus the square-chart failure is
not certified as an obstruction.

Artifacts:

- `row54_shared_root_active_set.py`
- `row54_shared_root_active_set.json`
- `row54_shared_root_active_set_svd.json`

## Fresh transverse actual-cell passage

`row54_transverse_actual_continuation.py` abandons formal square roots and
integrates the full-44 cone itself.  Each tangent raises all six packet guards
at the same requested first-order rate, keeps the discovered bypass walls on
their admissible sides, and audits every support row within the near-boundary
cone.  A finite step is accepted only when a fresh hull confirms all of:

- all 61 active rows and `f=(61,162,103)`;
- the exact fixed flip-cell maximal-face set;
- enlarged stable base and U8;
- all 37 forced rail edges and absence of edge `(0,1)`;
- every nonpacket mechanics guard and every fixed topology guard positive.

The materialized passage contains 85 accepted fresh steps with total cone
time `0.03395431059419291`.  All six defects improve strictly.  The endpoint
is still the strict far-side `(2,3,3)` cell, with

```text
S[7,8,246] = -0.0010071456770002272
U6          = -0.003224428154518597
U54         = -0.005021208513841938
H(5,6)      = -0.00028527187032423296
H(6,7)      = -0.0007835983627130309
H(9,10)     = -0.005015533936348238
```

The nearest nonpacket mechanics guard is strictly positive at
`8.864268515113458e-5`.  The fixed-cell topology minimum is
`1.0520537056541573e-10`.  The complete audit contains 326 face/vertex/edge
records with every component and 6553 fixed topology rows.  The endpoint
full-44 cone remains feasible, so the result is a certified passage rather
than a blocker.  At the saved endpoint `U0=+8.8642685e-5`, the requested negative
guards for `H(0,54)` and `H(1,54)` are respectively `+0.01797068` and
`+370.38427`; hence no `H(1,54)` event and no rail loss occurs on the saved
path.

Primary passage artifacts:

- `row54_transverse_actual_continuation.py`
- `row54_transverse_inward_continuation.json`
- `row54_transverse_inward_continuation.csv`
- `row54_transverse_inward_continuation_faces.json`
- `row54_transverse_inward_continuation_audit.json`

This is not yet the target cell: all six saved endpoint guards remain
negative.  It does establish that the exact `U0/H(0,54)` first event and the
three listed support circuits admit a fresh, rail-preserving transverse
bypass in the full control space.

## First new actual wall: row-15 loss and exact nullspace bypass

Continuation from the materialized strict endpoint first proposes an invalid
finite step at trajectory iteration 72.  The accepted step is `0.0005`; steps
`0.001` and `0.002` drop the hull to 60 active rows.  Along that direction the
common zero occurs at

```text
h_wall = 0.0006299753506564594.
```

The event has four normalized manifestations:

```text
base polygon: edge (16,15) against row 14
base polygon: edge (15,14) against row 16
support face [15,16,72] against row 14
support face [14,15,72] against row 16.
```

They share the exact algebraic numerator

```text
D = det(p15-p14, p16-p14, p72-p14).
```

Rows 14,15,16 lie in the enlarged-base plane and row 72 lies off it, so
`D=0` is exactly the collinearity of base rows 14,15,16.  At the localized
wall `D=-2.40e-18`; row 15 lies on segment `[14,16]` at parameter
`0.59094855718` with residual `3.10e-15`.  Fresh Qhull reports
`(60,160,102)` and row 15 is absent.

The direction change at the closest valid point was projected onto the
kernel of the normalized six-row mechanics Jacobian.  Its maximum packet
Jacobian residual is `1.48e-12`.  Scaling this nullspace correction by
`1.00731421778` changes the determinant derivative from
`-1.90529536e-8` to `+1.01360506e-10` without changing the six first-order
packet derivatives.  A finite step `0.0005` in the projected direction is
fresh and strict: all61, fixed faces, enlarged base, U8, and all 37 rails; it
raises the determinant from `3.21113e-12` to `1.48381e-11` and improves all
six packet guards.  Thus row-15 loss is a genuine first actual wall, but not a
blocker.

Artifacts:

- `row54_row15_wall_bypass.py`
- `row54_row15_exact_wall.csv`, `_faces.json`, `.json`
- `row54_row15_exact_nullspace_bypass.csv`, `_faces.json`, `_audit.json`

The canonical bypass endpoint is exclusively the artifact family with the
`exact_nullspace_bypass` stem.

## Next actual wall: clean {12,13,261,262} support flip

From the canonical exact-nullspace endpoint, a full-44 LP fixes all six
normalized packet derivatives at one, keeps every promoted/nearby wall
one-sided, and maximizes the row-15 determinant derivative.  This moves the
row-15 circuit decisively inward:

```text
D15(start) = 1.48381399753489e-11
D15(valid) = 5.896590787834195e-7
D15(far)   = 7.373287037101183e-7.
```

The first different actual support wall on this ray is the circuit
`{12,13,261,262}` at

```text
h_wall = 0.0022276555419809482
N_wall = 2.121564257439914e-18,
```

with the exact common numerator

```text
N = det(p13-p12, p261-p12, p262-p12).
```

The two crossed normalized support rows are `N` divided by strictly positive
triangle-area denominators.  Their start ratios `guard/N` are
`20.117604963008215` and `20.490527132904525`; both wall values are below
`9e-17` in magnitude.  Fresh grouping at the wall gives the maximal quad
`[12,13,261,262]` and `f=(61,161,102)`.

The passage is the clean diagonal exchange

```text
removed: [12,13,262], [13,261,262]
added:   [12,13,261], [12,261,262]
edge:    (13,262) -> (12,261).
```

The strict adjacent cell returns to `f=(61,162,103)` and class `(2,3,3)`.
It has all 61 rows, the enlarged stable 18-gon, U8, all 37 rails, no edge
`(0,1)`, and still contains the original compensating diagonal `(3,88)` while
excluding `(2,242)`.  Thus this wall is a transverse actual-cell passage, not
a blocker or a recurrence of row-15 loss.

Artifacts:

- `row54_post_row15_clean_flip.py`
- `row54_post_row15_clean_flip_exact_wall.csv`, `_faces.json`, `.json`
- `row54_post_row15_clean_flip.csv`, `_faces.json`, `_audit.json`

## Material packet reduction in the adjacent cell

`row54_adjacent_dynamic_continuation.py` rebuilds the full mechanics and
topology Jacobians on the adjacent face lattice at every step.  Its
lexicographic LP retains at least half of the maximum simultaneous packet rate
and maximizes the weakest inward derivative of nearby/promoted guards.  Every
finite step is accepted only after a fresh hull and own-centroid audit; a face
lattice change would be allowed only as one clean 2-2 flip.

Twenty accepted fresh steps remain in the same strict adjacent cell and keep
the row-15 determinant at `7.390038545130585e-7`.  Relative to the canonical
exact-nullspace endpoint, the absolute six defect sizes decrease by

```text
S[7,8,246]   1.1178%
U6            1.5775%
U54           0.9590%
H(5,6)        3.7264%
H(6,7)        0.8484%
H(9,10)      85.8851%.
```

The final packet is

```text
S[7,8,246] = -0.0010031626592300594
U6          = -0.0031824546542611213
U54         = -0.005008052085651344
H(5,6)      = -0.0002754115419609793
H(6,7)      = -0.0007830847427779773
H(9,10)     = -0.0007130841967191159.
```

The endpoint independently audits as all61, `f=(61,162,103)`, class `(2,3,3)`,
the exact adjacent face set, enlarged base/U8/37 rails, and minimum fixed-cell
topology guard `3.7656470541595766e-10`.  This is a material reduction of the
six-packet (especially `H(9,10)`), while all six components remain negative.

Artifacts:

- `row54_adjacent_dynamic_continuation.py`
- `row54_adjacent_dynamic_continuation.json`
- `row54_adjacent_dynamic_continuation.csv`, `_faces.json`, `_audit.json`
