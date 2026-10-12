# figure-0175

AI research report · 2026-09-01 UTC · [Export notes](../../catalog/coverage.md#text-records)

---

# Steady Harbor 62 — exact finite determination

## Disposition: **EXACT NONWINNER**

I recovered the transport-interrupted immutable `Quiet_Quartz_33` result, verified `303/303` archive-manifest entries from a clean extraction, and independently reran its clean-room verifier to `QUIET_QUARTZ33_ALL_CHECKS_PASS`. No homogeneous convex polyhedral Gömböc was obtained. The strongest certified endpoint is the uniform-density, own-centred convex polyhedron `J43_shared_metric` with strict `(S,U,H)=(3,3,4)`, not `(1,1,0)`. It does, however, exactify the first unknown incidence exit and leave the previously excluded forced-edge sign cell through a genuinely connected volumetric replacement.

## 1. Reconstructed `J40_final/J41_postwall` frontier

The exact deterministic source, dyadic H rows, exact Cramer vertices, maximal-face cycles, true edges, moment ledgers, and meshes are in the attached archive.

| cell | `(H,V,E)` | strict class | stable rows | moment box |
|---|---:|---:|---|---:|
| `J40_final` | `(2686,5368,8052)` | `(7,39,44)` | `0,2348,2349,2351,2366,2367,2369` | `[-2^-38,2^-38]^3` |
| `J41_postwall` | `(2687,5370,8055)` | `(7,39,44)` | same seven | `[-2^-38,2^-38]^3` |

This corrects the journal's count-equivalence statement: the exact `J40→J41` wall adds one active row, two vertices, and three true edges without changing mechanics. Each box has a unique interval-Krawczyk root of `Mx=My=Mz=0`, so the origin is the ordinary uniform-volume centroid. Directed volumes are `[3.371288156755192,3.3712881567551927]` and `[3.371366126416678,3.371366126416679]`.

The exact row-disjoint forcing matching is

```text
(0,36), (2348,2453), (2349,2384), (2351,3404),
(2366,2471), (2367,2402), (2369,3386).
```

All seven are actual true edges. On the full root box, every external-neighbour primitive at both endpoints is positive and the endpoint normals are nonparallel; hence each edge forces at least one stable endpoint, and row disjointness proves `S≥7`. The per-edge minimum external-numerator lower bounds are respectively

```text
1.0271636152303641e-5, 1.3440615525135422e-3,
1.7838215449474946e-3, 1.1960365706683571e-3,
1.3797079688353529e-3, 1.8296125907861780e-3,
1.1734075100148231e-3.
```

The full primitive certificate is `certificates/J40_final_forcing_obstruction.json`.

## 2. Exact first incidence exit `(2351,2456,3439,3474)`

The wall is the exact four-equation system

```text
Mx=0, My=0, Mz=0,
D=det(q2456-q2351,q3439-q2351,q3474-q2351)=0.
```

The expanded rational circuit polynomial has 24 monomials and SHA-256

```text
2a4450e333e768708499bfce2ad0c6862787305dee831eb6abf3a602e1e98545.
```

Its unique root is isolated around

```text
(delta_u,delta_t1,delta_t2,g)
≈ (5.679611841707031e-6,
   1.167565219221719e-6,
  -1.311648432357525e-5,
   0.0632372618440375)
```

with exact dependent-coordinate radius `2^-36` and `g` radius `2^-32`. The four-dimensional Krawczyk image is strictly interior; the midpoint Jacobian determinant is `2.6609153446114223e-7`, condition number `4946.276508747359`, and the hard-centred reduced circuit derivative is `-1.5620257685721074e-4`. At displacement `2^-34`, the circuit intervals are strictly positive `[8.829241049217172e-15,9.33023732059557e-15]` and strictly negative `[-9.356596985914124e-15,-8.853405205136443e-15]`.

Normalized circuit-coefficient intervals are

```text
2351 [ 0.2821455599632442,   0.28214556000742164]
2456 [-0.28863425691116484, -0.28863425685978145]
3439 [-0.9935113036204096,  -0.9935113025793081]
3474 [ 0.999999999491642,    1.000000000508358].
```

Thus the sign pattern is `(+,-,-,+)`, a genuine convex quadrilateral circuit. The certified adjacent own-centred cells are

| cell | `g` | sign | `(H,V,E)` | class |
|---|---:|---|---:|---:|
| `J42_adj_pre` | `0.06323720223939272` | positive | `(2687,5370,8055)` | `(7,39,44)` |
| `J42_adj_post` | `0.06323732144868227` | negative | `(2687,5370,8055)` | `(7,39,44)` |

Each has a unique moment root in `[-2^-42,2^-42]^3`. The quad boundary is `2351–2456–3474–3439–2351`. Pre-wall facets are `(2351,2456,3439)` and `(2456,3439,3474)` with true diagonal `(2456,3439)`; post-wall facets are `(2351,2456,3474)` and `(2351,3439,3474)` with true diagonal `(2351,3474)`. At the wall there is one nonsimplicial quadrilateral face and neither diagonal is true.

Only the two opposite incidences vanish. Every other actual nonincidence has lower gap at least `1.4679164550557287e-9`, and every fixed-triple determinant has absolute lower bound `4.574261744522253e-5`. No simultaneous or intervening incidence event occurs, and the equilibrium delta is exactly `(0,0,0)`. The full certificate is `certificates/J42_exit_wall/exit_wall_certificate.json`.

## 3. Connected forcing complex and joint replacement

Deterministic routing on actual maximal faces and true edges has no cycles. All `7+39+44=90` inherited equilibrium nodes lie in one Morse component; its support carrier has `1675` rows, one-ring `2148`, and external boundary `473`. The seven matching edges are therefore forcing certificates, not seven independent defects.

`J43_shared_metric` replaces rings `33..67` across all 36 sectors in one batch: 1260 affected labels; 378 predecessor-active rows forming one connected induced graph; 368 active rows removed; 51 active rows added; 1225 rows suppressed and all endpoint-inactive; a 35-row helical selector with 10 endpoint-extreme rows. The exact family is `source/J43_shared_metric_local_family.json.gz`, SHA-256 `71e0e9e282dfdabe81f3b2cdc8c3e0665e58d3409acf2c5809d396e4000400eb`.

The exact endpoint has

```text
(H,V,E)=(2370,4736,7104), surface triangles=9468,
Euler=2, topology signature=
197a812462f0ae1b5577fedd9fbecf00d5dfbf727852df4408994784ca2012a1,
strict class=(3,3,4).
```

Relative to `J42_adj_post`, `Δ(H,V,E)=(-317,-634,-951)`. Its directed volume is `[3.588656983954403,3.588656983954404]`. The three hard moment equations have one and only one root in `[-2^-38,2^-38]^3`; the midpoint Jacobian determinant is `0.010224277355180878`, condition number `40.96951013140733`, and the Krawczyk image is strictly interior. Therefore all three ordinary moments are exactly zero at the isolated root. The complete incidence audit checks all `20,464,256` actual row/nonincident-vertex pairs; the minimum certified gap is `1.4574461637550937e-9`.

The replacement preserves stable row `0`, true edge `(0,36)`, and terminal unstable facet `(4321,4322,4323)`. Simultaneously, rows `2348,2349,2351,2366,2367,2369` become inactive/nonstable; their six forcing edges disappear; none of the 38 old nonprotected unstable labels remains unstable; and none of the 44 old saddle labels remains a saddle. Thus it genuinely leaves the old forced-edge cell.

## 4. Complete endpoint mechanics and robust nonwinner box

```text
stable rows:       0, 2463, 2481
unstable triples:  (18,53,54), (53,54,89), (4321,4322,4323)
saddle true edges: (0,33), (53,54), (2454,2455), (2472,2473).
```

Directed full-feature bounds on the moment-root box are

| feature | included positive lower | closest excluded upper |
|---|---:|---:|
| stable | `1.898221343255013e-4` | `-1.3897522317396492e-5` |
| unstable | `7.87225021519423e-2` | `-1.8338729206143458e-2` |
| saddle | `5.073493928392392e-2` | `-2.915655016545226e-3` |

Every true edge is derived from grouped maximal-face cycles and audited through all four normal-cone components; mesh diagonals are excluded. Five independent trace-free symmetric metric controls satisfy `|s_k|≤2^-25`. They preserve exact own-centering, have rank 5, singular-value lower bound `0.9999998509883881`, determinant interval `[0.9999998807907112,1.0000001192092987]`, and retain the entire strict `(3,3,4)` classification on the combined `3+5` box. This is an open exact nonwinner, not an unresolved boundary point.

The archive supplies, for every conclusion-bearing cell, complete `H_exact.tsv.gz`, `V_exact.tsv.gz`, `maximal_face_cycles.tsv.gz`, `true_edges.tsv`, oriented `surface_triangles.tsv`, point and root-box mechanics ledgers, root certificates, OBJ, and STL. The independent verifier reparses these data and reproduced watertight Euler-2 meshes for both J42 sides and J43.

## 5. Exact NONWINNER residual and smallest new topology

The new extra equilibria form one connected block: two extra stable rows `2463,2481`, two extra unstable facets `(18,53,54),(53,54,89)`, and four saddles. The residual carrier has 397 rows, one-ring 938, and boundary 541. Hence the exact disposition is

```text
NONWINNER: old six nonprotected forcing packets and all old attached
nonprotected U/H labels are gone, but a robust Euler-neutral
2S+2U+4H block is born.
```

This is not a global impossibility theorem beyond the certified cells and boxes.

The low cluster `{0,18,33,53,54,89}` and high cluster `{2454,2455,2463,2472,2473,2481}` are 31 true-edge steps apart. One shortest path is

```text
89-124-159-194-229-264-299-334-369-404-439-474-509-544-579-614-
649-685-721-757-793-864-899-934-969-1004-1040-1076-1112-1148-
1184-2481.
```

The terminal one-rings contain 103 rows; a Steiner connector uses 60 rows and 59 edges; the explicit finite-thickness carrier has 143 rows and 213 external-boundary rows, all enumerated in `research/J43_smallest_new_topology.json`.

The smallest evidence-supported successor topology is a finite-thickness two-sheet replacement with two edge-sharing nonsimplicial `2↔3/3↔2` cells and one shared volumetric terminal cell. Besides dependent controls for `Mx=My=Mz=0`, it needs: a low U–H death-sheet control on `(18,53,54),(53,54,89),(0,33),(53,54)`; a high S–H death-sheet control on `2463,2481,(2454,2455),(2472,2473)`; and an independent cross-gap relay/antibirth control forcing both deaths to overlap before any compensating birth. It must preserve row `0` and facet `(4321,4322,4323)` while removing all six unwanted extrema and four saddles in one rebuilt exact cell.

## Reproducibility

Archive SHA-256:

```text
57a458f0ba75ab844eb0a7f651b45f60705ea0277da665271e0a33f05529e634
```

- Exact source, H/V/circuit/replacement certificates, verifier, OBJ and STL (`Steady_Harbor_62_exact_exit_shared_NONWINNER.zip`)
- Independent verification receipt (`Steady_Harbor_62_verification_receipt.txt`)

Run `bash [internal-source-reference].sh` from the extracted archive root. The terminal verdict is `QUIET_QUARTZ33_ALL_CHECKS_PASS`.

The literal frontier is now `J43_shared_metric`. It is an exact ordinary-centred, irredundantly audited, watertight **NONWINNER**. The next nonredundant continuation is the explicit 143-row shared two-sheet/cross-gap cell with three topology controls and three dependent ordinary-moment controls.
