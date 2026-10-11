# Robust row54 enlarged-base escape — rebuilt track report

## Result in one paragraph

The lost target-sphere and row54 track was rebuilt from the restored bundle.
There is now a strict all-61 robust target realization, a strict row54
endpoint with the enlarged 18-gon base and `U1 -> U54`, a rail-valid coplanar
row246 wall with f-vector `(61,161,102)`, and a rail-valid far-side cell with
f-vector `(61,162,103)`.  The desired four-wall escape has no local rank
obstruction: its Jacobian has rank four in the 8 metric/projective controls,
the 36 in-base-plane controls, and the joint 44-control chart.  Global metric
search instead transfers the four defects exactly to
`{S[198,243,244], U2, H(4,5), H(12,13)}`.  A guarded in-plane LP reaches and
cleanly crosses the first compensating topology wall, flipping diagonal
`(2,242)` to `(3,88)` while retaining all 61 vertices, the 18-gon base, and
all 37 forced rail edges.  The mechanical class remains `(2,2,2)` in that
neighbor cell; no `(1,1,0)` target is claimed here.

## Reconstructed target and robust metric cell

The target topology is the original sphere with the durable old-16/new-16
swap reconstructed from the 16 tetrahedra

- `[198,224,k,k-1]`, `k=241,...,230`;
- `[198,247,224,229]`, `[198,247,229,228]`,
  `[198,247,228,258]`, `[198,247,258,224]`.

`rebuild_target_sphere.py` builds a Tutte disk and LP height cap.  Its fresh
hull is all-61 with `(V,E,F)=(61,163,104)` and exact expected maximal-face
set.  `row54_four_residual_search.py` then found the strict robust
projective/trace-free-SPD parameter

```text
theta = (
  0.5986379080621057, -0.11738849987297537, -0.008279938225080129,
  1.2945070964405363, 0.10346520321613019, -0.5419399603218819,
 -0.7536301364666212, -0.32147427982739424
)
```

with minimum projective denominator `0.09815664216851494`.  The independent
fresh audit gives class `(2,2,2)`, stable faces `base[0..16]` and
`[8,245,246]`, unstable vertices `1,8`, saddle edges `(6,7),(9,10)`, hard
requested mechanics margin `0.059182357264026`, minimum nonface support slack
`9.60e-8`, and minimum polygon slack `3.81e-7`.

Primary artifacts:

- `robust_target_rebuilt.csv`
- `robust_target_rebuilt_faces.json`
- `robust_target_rebuilt_full_audit.json`
- `materialize_robust_full_audit.py`

## Row54 endpoint, row246 wall, and far-side source

The row54 move is made in the robust base plane with exterior parameter
`0.01` and edge fraction `0.9`; it deletes edge `(0,1)`, adds edges `(0,54)`
and `(1,54)`, retains all 61 vertices and both rails, and changes the
unstable pair from `1,8` to `8,54`.

For row246, the tangent is selected before the robust map in the rebuilt raw
target chart.  With

```text
u = unit(q8-q7)
q246_wall = orthogonal_projection_to_plane(7,8,245) - 0.21*u
q246_wall = (-0.48253021382009076,
              0.2923046074439142,
              0.46444522728375714)
```

and the original raw normalization held fixed during the robust map, the
coplanar wall has all-61 `(61,161,102)`, maximal quad
`[7,8,245,246]`, neither diagonal `(8,245)` nor `(7,246)`, and q246-star

```text
{7,8,245,246}, {8,246,264}, {198,245,246}, {198,246,264}.
```

Moving raw q246 by `1e-5` to the far side of that plane gives the all-61
cell `(61,162,103)`, stable faces `base[0,54,1,...,16]` and `[7,8,246]`,
unstable vertices `8,54`, and saddle edges `(6,7),(9,10)`.  All 37 generated
forced rail edges are present in the endpoint, wall, and far-side outputs.

Primary artifacts:

- `materialize_row54_cells.py`
- `row54_endpoint_rebuilt.csv`, `_faces.json`, `_audit.json`
- `row54_combined_wall_rebuilt.csv`, `_faces.json`, `_audit.json`
- `row54_far_rebuilt.csv`, `_faces.json`, `_audit.json`

Every audit contains the full face/vertex/edge component margins, its own
volume centroid, actual maximal faces, support/convexity topology margins,
and the complete forced-edge list.

## Four-defect rank and guarded metric result

At the rail-valid far-side source, the target-sign residual packet is

```text
S[7,8,246], U54, H(6,7), H(9,10).
```

The normalized finite-difference Jacobian singular values are:

| controls | rank | singular values |
|---|---:|---|
| metric/projective 8 | 4 | `32.6649, 8.34756, 2.61313, 0.808845` |
| in-plane base 36 | 4 | `16.4714, 14.6825, 5.93346, 1.49211` |
| joint 44 | 4 | `35.9044, 16.4783, 10.2340, 1.75647` |

Thus the four requested walls themselves are transverse and independently
controllable.  The obstruction encountered by the nonlinear search is a
compensating packet, not a rank loss.

Two completed 8D differential-evolution runs independently reached the same
first compensating class:

```text
stable = base + S[198,243,244]
unstable = {2,8}
saddles = {(4,5),(12,13)}
```

The better saved run is `row54_escape_831551.json`, with fresh all-61 fixed
topology and worst target guards

```text
H(12,13) = -0.06564499
H(4,5)   = -0.06477912
S[198,243,244] = -0.05216224
U2       = -0.02503099
```

At this packet the active four-row Jacobian is again rank four in all three
control blocks; the joint singular values are
`16.9991, 0.758510, 0.180100, 0.0859033`.

`row54_guarded_escape.py` performs the requested guarded SLP: all mechanics
target rows are constrained, every fixed-cell face-support and polygon guard
is differentiated, steps are trust-bounded and line-searched, and every
accepted step is checked by fresh Qhull, own-centroid mechanics, base, and
forced rails.  Its saved best packet is
`row54_guarded_from_831551.json`.

## First clean compensating topology crossing

The guarded path identifies the first topology event as the paired support
wall

```text
face [3,242,2] against vertex 88
face [88,2,242] against vertex 3.
```

This is the quadrilateral `{2,3,88,242}`.  A separate L1-minimal guarded LP
crosses both old support guards while keeping every other old-cell support
and polygon guard positive.  It needs only

```text
base_3_u = 2.247188223871509e-7
```

in the standardized in-plane chart.  The nonlinear fresh result replaces
diagonal `(2,242)` by `(3,88)`, has `(61,162,103)`, retains the enlarged base
and all 37 forced rails, and has new-cell preimage topology margin
`1.1615933964703729e-8`.  Its mechanics stays in the compensating `(2,2,2)`
packet above.

Primary artifacts:

- `row54_multiwall_flip.py`
- `row54_multiwall_flip_preimage.csv`
- `row54_multiwall_flip.csv`
- `row54_multiwall_flip_faces.json`
- `row54_multiwall_flip_audit.json`

## Neighbor-cell all-guard and raw-min continuation

Two corrected all-guard metric searches in the flipped cell were saved as
`row54_multicell_minimax_831581.json` and
`row54_multicell_minimax_831582.json`.  They transfer the compensating packet
back toward the original q246/base packet.  The better joint seed 831581 has

```text
S[8,246,7] = -0.00121767
U54         = -0.0240893
H(6,7)      = -0.0402990
H(9,10)     = -0.0443278
```

with every other target guard positive, fresh all-61 fixed flip topology,
enlarged base, and all forced rails.  Its materialized full certificate is
`row54_multicell_minimax_831581_audit.json`.

A raw-hard Nelder--Mead continuation from that seed reduces the bottleneck by
another factor of about 8.5.  The saved stationary candidate
`row54_multicell_rawmin_local_831593.json` has hard target margin
`-0.00519654984743` and the exact negative packet

```text
S[8,246,7]  = -0.00104371980501
U6           = -0.00326719122071
U54          = -0.00519654984743
H(5,6)       = -0.000289055951193
H(6,7)       = -0.000814387712363
H(9,10)      = -0.00519654984742
```

Its fresh class is `(2,3,3)`: stable `base + [7,8,246]`, unstable
`{6,8,54}`, and saddles `{(5,6),(6,7),(9,10)}`.  The active six-row Jacobian
is still full rank six in each control block.  Joint-44 singular values are

```text
233.99493, 31.95774, 10.90354, 0.688620, 0.0344101, 0.0116194.
```

Thus even the deeper compensating packet is not a literal rank deficiency;
the metric-only block is, however, strongly ill-conditioned (smallest
singular value `6.33e-6`), while in-plane base controls improve the smallest
singular value to `7.42e-3`.

Primary artifacts:

- `row54_multicell_rawmin_local_831593.csv`
- `row54_multicell_rawmin_local_831593_audit.json`
- `row54_rawmin_stationary_rank.json`
- `row54_rank_probe.py`

All numerical coordinates are 17-digit floating-point reconstructions.  The
audits are strict floating certificates with fresh hull checks; they are not
being represented as exact rational certificates.
