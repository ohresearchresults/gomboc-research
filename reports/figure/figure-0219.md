# figure-0219

AI research report · 2026-09-02 UTC · [Export notes](../../catalog/coverage.md#text-records)

---

# Vivid Atlas 32 — exact P9-XG7 third-spine/sixth-page determination

## Literal verdict

**EXACT FINITE NONWINNER.** No homogeneous convex polyhedral Gömböc was obtained.

The requested first nonrepeating successor of P9-XG6 was nevertheless realized exactly. Two new extreme support rows `Y0,Y1` form a communicating positive-volume third-spine/sixth-page replacement which jointly removes from the actual hull:

- forcing edge `X2-X3`;
- extra stable face `X2`;
- extra unstable vertex `SU/S102/X1`;
- saddle edges `SA5-X2` and `S102-X0`.

The intended stable face `T27` and intended unstable lineage `TR/S102/G` survive. The inherited component is genuinely deleted rather than renamed. The exact successor remains strict own-centred `(S,U,H)=(2,2,2)` because a distinct replacement component is born on overlapping true edges `X2-Y1` and `X3-Y1`.

## Provenance

```text
predecessor result id:
  figure-0210

predecessor result SHA-256:
  3bf4493fa79bd1dc952c91eb348fb159e404a29ba39909dfbb2d9cc986e18b25

included predecessor exact-data SHA-256:
  b6e16e957cfa0909fc5ac64a40981889dae016273f4ae2017e55e2fe0c7ab71b

exact input-row SHA-256:
  3228737e6493aa3e861739de42249cde3deebc80b08e1ac2141a5b017a3fc087

successor exact-data SHA-256:
  182dd372ad66c4c7c026a0d8d3b5207840dff85b5ae36f8ab637d71da2e62af3
```

`generate_endpoint.py` starts from `input_rows_exact.json`, enumerates every row triple, reconstructs actual H/V/E incidence, integrates exact ordinary volume and first moments, translates to the exact own centroid, audits every full equilibrium cone, certifies the shared event and rank-five control chart, and exports the meshes.

The clean-room verifier independently enumerates all `C(13,3)=286` predecessor triples and all `C(15,3)=455` successor triples without importing the generator or `exact_core.py`.

## Exact support rows

For the uncentred body

```text
P_raw = {x in R^3 : q_i·x <= 1 for every supplied row i},
```

the physical uniform-density body is `P=P_raw-c`, where `c` is its exact ordinary-volume centroid. Its own-centred support rows are exactly

```text
H_i = q_i/(1-q_i·c).
```

The 15 supplied rows are:

```text
0  T27
(-7125242734162057/140737488355328,
  265769074670437/35184372088832,
 -63255401657691/70368744177664)

1  TR
(-892363419092795/281474976710656,
 -235941426090029/140737488355328,
 -528766574131575/140737488355328)

2  SU
(-544131479513675/140737488355328,
 -96790958131853/35184372088832,
  118288508214145/140737488355328)

3  SC1
(-276717838830129/140737488355328,
 -1302539451900877/140737488355328,
 -228646779652985/70368744177664)

4  SA5
(-1735735365091297/281474976710656,
 -2190132466616797/281474976710656,
 -2075306589585777/281474976710656)

5  S102
(-1745325229249529/70368744177664,
  5268329269809467/281474976710656,
  1934562100355505/281474976710656)

6  G
(1595031506620615/70368744177664,
 69636553284589/35184372088832,
 72284311426759/70368744177664)

7  M
(1529073462/16777216,
 -268643187/16777216,
 58067364/16777216)

8  N
(1529492441/16777216,
 -268486070/16777216,
 58329226/16777216)

9  X0
(1919121502/16777216,
 -309962234/16777216,
 99003968/16777216)

10 X1
(1848158428/16777216,
 -383623901/16777216,
 89362767/16777216)

11 X2
(2073127498/16777216,
 -414482154/16777216,
 17864224/16777216)

12 X3
(1956031545/16777216,
 -324421554/16777216,
 24586561/16777216)

13 Y0
(1763461327/16777216,
 -218740469/16777216,
 159462489/16777216)

14 Y1
(1040743361/8388608,
 -206745211/8388608,
 -2371163/16777216)
```

Rows `M,N` are supplied but strictly inactive. Their exact minimum support slacks are

```text
M = 751378416542211091172953/3409726605460446835499110
N = 74991418480053898778051/340972660546044683549911
```

with decimals `0.22036324417885272` and `0.21993381627711797`. The remaining 13 rows are actual extreme polar vertices and therefore irredundant primal supports.

## Exact predecessor reconstruction

```text
supplied rows: 13
active rows:   11
inactive rows: M,N

Q:(V,E,F) = (11,27,18)
P:(V,E,F) = (18,27,11)
complexity = 54
class = (2,2,2)
```

### All predecessor Q facets / primal vertices

```text
 0 T27/TR/SA5
 1 T27/TR/S102
 2 T27/SU/SC1
 3 T27/SU/S102
 4 T27/SC1/SA5
 5 TR/SA5/G
 6 TR/S102/G
 7 SU/SC1/X1
 8 SU/S102/X1
 9 SC1/SA5/X2
10 SC1/X1/X2
11 SA5/G/X3
12 SA5/X2/X3
13 S102/G/X3
14 S102/X0/X1
15 S102/X0/X3
16 X0/X1/X2
17 X0/X2/X3
```

### All 27 predecessor true edges

```text
T27-TR   T27-SU   T27-SC1
T27-SA5  T27-S102 TR-SA5
TR-S102  TR-G     SU-SC1
SU-S102  SU-X1    SC1-SA5
SC1-X1   SC1-X2   SA5-G
SA5-X2   SA5-X3   S102-G
S102-X0  S102-X1  S102-X3
G-X3     X0-X1    X0-X2
X0-X3    X1-X2    X2-X3
```

### Predecessor maximal-face cycles

```text
T27  0 4 2 3 1
TR   0 1 6 5
SU   2 7 8 3
SC1  2 4 9 10 7
SA5  0 5 11 12 9 4
S102 1 3 8 14 15 13 6
G    5 6 13 11
X0   14 16 17 15
X1   7 10 16 14 8
X2   9 12 17 16 10
X3   11 13 15 17 12
```

Its equilibria are exactly

```text
stable:   T27, X2
unstable: TR/S102/G, SU/S102/X1
saddles:  SA5-X2, S102-X0.
```

The true edge `X2-X3` is the inherited external-positive forcing component.

## Exact successor reconstruction

```text
supplied rows: 15
active rows:   13
inactive rows: M,N

Q:(V,E,F) = (13,33,22)
P:(V,E,F) = (22,33,13)
complexity = 66
class = (2,2,2)
```

### All 22 successor Q facets / primal vertices

```text
 0 T27/TR/SA5
 1 T27/TR/S102
 2 T27/SU/SC1
 3 T27/SU/S102
 4 T27/SC1/SA5
 5 TR/SA5/G
 6 TR/S102/G
 7 SU/SC1/X1
 8 SU/S102/Y0
 9 SU/X1/Y0
10 SC1/SA5/Y1
11 SC1/X1/X2
12 SC1/X2/Y1
13 SA5/G/X3
14 SA5/X3/Y1
15 S102/G/X3
16 S102/X3/Y0
17 X0/X1/X2
18 X0/X1/Y0
19 X0/X2/Y1
20 X0/X3/Y0
21 X0/X3/Y1
```

### All 33 successor true edges

```text
T27-TR   T27-SU   T27-SC1
T27-SA5  T27-S102 TR-SA5
TR-S102  TR-G     SU-SC1
SU-S102  SU-X1    SU-Y0
SC1-SA5  SC1-X1   SC1-X2
SC1-Y1   SA5-G    SA5-X3
SA5-Y1   S102-G   S102-X3
S102-Y0  G-X3     X0-X1
X0-X2    X0-X3    X0-Y0
X0-Y1    X1-X2    X1-Y0
X2-Y1    X3-Y0    X3-Y1
```

### All 13 successor maximal-face cycles

```text
T27  0 4 2 3 1
TR   0 1 6 5
SU   2 7 9 8 3
SC1  2 4 10 12 11 7
SA5  0 5 13 14 10 4
S102 1 3 8 16 15 6
G    5 6 15 13
X0   17 19 21 20 18
X1   7 11 17 18 9
X2   11 12 19 17
X3   13 15 16 20 21 14
Y0   8 9 18 20 16
Y1   10 14 21 19 12
```

All exact vertex coordinates, centered support rows, cycles, nonincidences, and true-edge cone components are expanded in the package CSV and JSON files.

## Exact ordinary volume and centroid

The successor’s fully expanded rational volume, three raw first moments, and three centroid coordinates are stored at

```text
p9_xg7_third_spine_exact.json#/after/mass
exact_mass_centroid.json#/after
```

and independently recomputed from the maximal-face cycles. Their decimal values are

```text
volume = 0.0018476827160692404

raw first moments =
(-7.991901767015791e-06,
  2.065124722128806e-05,
 -5.8480517663995114e-05)

raw centroid =
(-0.004325364792077376,
  0.011176836283461868,
 -0.031650735894962825)
```

The verifier proves the exact identities

```text
Mx - V*cx = 0
My - V*cy = 0
Mz - V*cz = 0.
```

Therefore the translated physical body has exact ordinary-volume first moments

```text
(0/1,0/1,0/1).
```

The minimum exact nonincidence slack is positive; its decimal value is `0.003210288724447816`. A positive barycentric certificate on rows `T27,TR,SU,G` places the origin strictly inside the polar hull, proving boundedness. The minimum projective denominator is positive, decimal `0.668139140651569`.

## Positive-volume third-spine/sixth-page event

The predecessor and successor agree outside a disk with common boundary cycle

```text
S102-SU-X1-X0-X2-SC1-SA5-X3-S102.
```

Removed predecessor facets:

```text
S102/SU/X1
S102/X0/X1
S102/X0/X3
SA5/SC1/X2
SA5/X2/X3
X0/X2/X3
```

Added successor facets:

```text
S102/SU/Y0
S102/X3/Y0
SA5/SC1/Y1
SA5/X3/Y1
SC1/X2/Y1
SU/X1/Y0
X0/X1/Y0
X0/X2/Y1
X0/X3/Y0
X0/X3/Y1
```

### `Y0` shell

```text
Y0/S102/SU/X1
Y0/S102/X0/X1
Y0/S102/X0/X3
```

These three tetrahedra form an exact face-to-face 3-ball. Their total exact volume is

```text
4013998553588582623443537125080217222719/
3987683987354747618711421180841033728
```

(decimal `1006.5989597764719`). The minimum tetrahedron volume is decimal `280.84301471724973`.

### `Y1` shell

```text
Y1/SC1/SA5/X2
Y1/SA5/X2/X3
Y1/X0/X2/X3
```

These form a second exact face-to-face 3-ball. Their total exact volume is

```text
136795658880248062221027853816180038143/
996920996838686904677855295210258432
```

(decimal `137.2181540102351`). The minimum tetrahedron volume is

```text
239088456615093172115/221360928884514619392
```

(decimal `1.0800842669928763`).

### Coupling of the cuts

`Y0` and `Y1` lie on opposite sides of the common radial page `[0,X0,X3]`. Their exact signed determinants are

```text
 4280955473450598105194391/2361183241434822606848
-4766443935972742622551533/2361183241434822606848.
```

The tetrahedra `conv(0,X0,X3,Y0)` and `conv(0,X0,X3,Y1)` therefore form a communicating positive-volume bipyramid. Their combined exact volume is

```text
753949950785278393978827/1180591620717411303424
```

(decimal `638.620448895889`). Radial spine `[0,X3]` has six pages and `[0,X0]` has five. This is one genuine shared-interior event, not two serial edge subdivisions.

## Exact deletion of the inherited component

Before the event, edge `X2-X3` has incident facets

```text
SA5/X2/X3
X0/X2/X3.
```

After the event:

- no actual facet contains both `X2` and `X3`;
- `X2-X3` is absent from the complete true-edge list;
- face `X2` is not stable;
- triple `SU/S102/X1` is not an actual vertex;
- edges `SA5-X2` and `S102-X0` are not saddles;
- `M,N` remain strict inactive supplied rows.

The replacement obstruction contains new row `Y1` and has different endpoints and different links. Thus the old component is deleted rather than renamed or carried along another page.

## Exhaustive full-cone mechanics

At the exact own centroid the equilibria are precisely

```text
stable faces:      T27, Y1
unstable vertices: TR/S102/G, SU/S102/Y0
saddle true edges: SA5-Y1, S102-Y0.
```

The complete audit tests:

- every directed support on every actual maximal face;
- all three coefficients in every actual vertex’s full active normal cone;
- projection parameter `t`, `1-t`, and both face-normal coefficients on every one of the 33 true edges.

Exact rational ledgers are in `p9_xg7_third_spine_exact.json` and `true_edges_full_cones.csv`. Category-clearance minima are

```text
stable positive:             115.54341646202488
nonstable-face exclusion:     30.07728513840796
unstable cone coefficient:     0.019970801834580512
nonunstable exclusion:         0.008647672464665487
saddle full-cone component:    0.0006393798587048455
nonsaddle-edge exclusion:      0.00022632133983272476
```

The result is an open strict `(2,2,2)` object, not a wall or triangulation artefact.

## Five independent shape controls after moment elimination

The three dependent projective-translation controls `tau_x,tau_y,tau_z` solve the ordinary-centroid equations with exact Jacobian

```text
-I_3
```

and determinant `-1`.

Five independent shape variables remain:

```text
u1 = SU_z
u2 = SA5_z
u3 = SA5_y
u4 = X3_y
u5 = X2_z.
```

They independently monitor:

```text
1. the shared-page opposite-side product;
2. the Y1-X2 stable-carrier wall;
3. the Y0 coefficient at SU/S102/Y0;
4. the Y1 saddle coefficient at SA5-Y1;
5. the Y0 saddle coefficient at S102-Y0.
```

The exact `5×5` determinant is nonzero and fully expanded in `control_rank_certificate.json`. Its decimal value is

```text
-0.09940531197333137.
```

The normalized singular values are

```text
1.449369114957301
1.0713229915166138
0.9985124815394589
0.7683172814344172
0.40528705347558425.
```

Hence insufficient local shape dimension is not the remaining obstruction.

## Directed perturbation certificate

`certify_perturbation.py` encloses every exact rational input and outward-rounds every primitive interval operation. It proves that all 45 raw support coordinates may vary independently by

```text
|delta q_ij| <= 2^-25
             = 2.9802322387695312e-08
```

while preserving the entire incidence, mass, mechanics, event, deletion, and forcing conclusions.

Rigorous lower bounds include

```text
actual nonincidence slack:             0.00320960771285661
excluded-triple blocker gap:           0.002995902140538575
positive oriented face determinant:    1.0781101334911074e-07
origin barycentric weight:             0.10259138913253987
projective denominator:                0.6681311910993891
stable support:                        115.43242273303368
nonstable exclusion:                   30.075087040314802
unstable cone coefficient:             0.01996994218756763
nonunstable exclusion:                 0.008646899248747368
saddle full-cone component:            0.00063928783781582
nonsaddle-edge exclusion:              0.00022621529552239165
inactive M/N support slack:            0.219933505498315
minimum shell tetrahedron volume:      1.080081841256476
communicating-page tetrahedron volume: 302.1757994497945
replacement external support:          115.43242273303368
replacement edge squared length:       3.1555848184426147
```

The certified volume interval is

```text
[0.001847677027484888,
 0.0018476884046537004]
```

and the centroid intervals are

```text
cx in [-0.0043254517598376434, -0.004325277824849792]
cy in [ 0.011176451234206486,   0.01117722133510452]
cz in [-0.0316514441076153,    -0.031650027686699195].
```

## First remaining exact obstruction

The complete scan of all non-`T27` true edges finds exactly two external-positive edges:

```text
X2-Y1
X3-Y1.
```

Their exact-point minimum external supports are

```text
X2-Y1: 218.38392524844576
X3-Y1: 115.54341646202488.
```

For each edge `u-v`, the exact identity

```text
A(u→v)+A(v→u)=||H_u-H_v||²>0
```

holds. Therefore the larger-radius endpoint of each edge also has positive mutual support. Because every external support at both endpoints is positive, each edge forces a stable endpoint. The two edges overlap at `Y1`, so at least one member of `{X2,Y1,X3}` is stable throughout the certified incidence/external-sign chamber. `T27` is independently stable, and consequently

```text
S >= 2
```

throughout that chamber. At the exact endpoint the forced member is `Y1`.

This is an exact open-cell obstruction. It is not a global exclusion of all third-spine or higher-valence P9 realizations.

## Numerical search and attempted falsification

Retained floating-point campaigns rebuilt the full hull and own centroid at every accepted state:

```text
two-row topology-free campaign:
  60,000 proposals
  1,248 valid full hulls
  692 class (2,2,2)
  402 class (2,3,3)
  38 class (3,2,3)
  no winner

three-new-row campaign:
  20,000 proposals
  1,213 valid full hulls
  902 class (2,2,2)
  222 class (2,3,3)
  50 class (3,2,3)
  no winner

four-new-row campaign:
  20,000 proposals
  573 valid full hulls
  420 class (2,2,2)
  109 class (2,3,3)
  13 class (3,2,3)
  no winner

five-new-row campaign:
  20,000 proposals
  250 valid full hulls
  151 class (2,2,2)
  68 class (2,3,3)
  12 class (3,2,3)
  no winner
```

Additional local, visible-cap, coupled-old-plane, differential-evolution, fixed-witness, and 336-branch first-jet searches also failed to materialize `(1,1,0)`. A nominal positive linear signature did not survive nonlinear full-hull reconstruction. These searches are discovery evidence only and are not promoted to a global impossibility statement.

## Smallest genuinely new successor topology

The residual Euler-neutral block is now

```text
extra stable:   Y1
extra unstable: SU/S102/Y0
saddles:        SA5-Y1 and S102-Y0
forcing graph:  X2-Y1-X3, with X2-X3 absent.
```

The smallest evidence-supported nonrepeating continuation is a **three-row hexahedral/octahedral double-cap with two communicating interior pages**:

1. one sector must delete both overlapping forcing edges and the `SA5-Y1` saddle;
2. the second must delete the `SU/S102/Y0` source and `S102-Y0` saddle;
3. both sectors must share positive three-dimensional interior before any replacement row becomes part of another external-positive edge or component;
4. `T27` and `TR/S102/G` must remain protected;
5. at least five independent shape controls should survive the three exact moment equations: one shared-cell diagonal, one stable-component death, one source death, and two saddle deaths.

Coupled motion of `SC1,SA5,S102,X0,X2,X3` is admissible and is likely preferable to another appended serial support row.

## Independent verification and meshes

`verify_independent.py` imports neither the generator nor `exact_core.py`. It independently reconstructs:

- all predecessor and successor candidate intersections;
- actual H/V/E incidence and maximal-face cycles;
- exact volume, first moments, centroid, and own-centred supports;
- every stable-face, unstable-vertex, and four-component true-edge test;
- both tetrahedral shell cuts and their shared radial page;
- literal deletion of `X2-X3` and all inherited residual carriers;
- the rank-five post-moment Jacobian;
- the complete replacement forcing graph;
- OBJ and STL edge multiplicities.

It ends with

```text
P9_XG7_INDEPENDENT_CLEAN_ROOM_PASS
```

The OBJ has 22 vertices, 33 undirected edges, and 13 maximal polygonal faces, Euler characteristic two, with every polygon edge used twice. The STL has 40 triangles and 60 undirected triangle edges, each used twice. Both meshes are watertight decimal renderings of the exact own-centred body.

A clean extraction of the final archive followed by `./RUN_ALL.sh` ends with

```text
ALL P9-XG7 VIVID ATLAS 32 VERIFIERS PASS
```

## Downloadable artifacts

- [Complete exact package](sandbox:/mnt/data/P9_XG7_VIVID_ATLAS_32_EXACT_NONWINNER.zip)
- [Archive SHA-256](sandbox:/mnt/data/P9_XG7_VIVID_ATLAS_32_EXACT_NONWINNER.zip.sha256)
- [Complete research handoff](sandbox:/mnt/data/P9_XG7_VIVID_ATLAS_32_FINAL_20260902/RESEARCH_HANDOFF.md)
- [Concise final summary](sandbox:/mnt/data/P9_XG7_VIVID_ATLAS_32_FINAL_20260902/FINAL_SUMMARY.json)
- [Exact input rows](sandbox:/mnt/data/P9_XG7_VIVID_ATLAS_32_FINAL_20260902/input_rows_exact.json)
- [Exact predecessor](sandbox:/mnt/data/P9_XG7_VIVID_ATLAS_32_FINAL_20260902/parent_p9_xg6_second_spine_exact.json)
- [Complete exact successor H/V/E/mass/mechanics](sandbox:/mnt/data/P9_XG7_VIVID_ATLAS_32_FINAL_20260902/p9_xg7_third_spine_exact.json)
- [Exact mass and centroid](sandbox:/mnt/data/P9_XG7_VIVID_ATLAS_32_FINAL_20260902/exact_mass_centroid.json)
- [Exact shared-event certificate](sandbox:/mnt/data/P9_XG7_VIVID_ATLAS_32_FINAL_20260902/shared_event_exact_certificate.json)
- [Inherited-component deletion certificate](sandbox:/mnt/data/P9_XG7_VIVID_ATLAS_32_FINAL_20260902/inherited_component_deletion_certificate.json)
- [Residual component obstruction](sandbox:/mnt/data/P9_XG7_VIVID_ATLAS_32_FINAL_20260902/component_obstruction_certificate.json)
- [Rank-five control certificate](sandbox:/mnt/data/P9_XG7_VIVID_ATLAS_32_FINAL_20260902/control_rank_certificate.json)
- [Directed perturbation certificate](sandbox:/mnt/data/P9_XG7_VIVID_ATLAS_32_FINAL_20260902/perturbation_box_certificate.json)
- [Independent verifier](sandbox:/mnt/data/P9_XG7_VIVID_ATLAS_32_FINAL_20260902/verify_independent.py)
- [Independent verification report](sandbox:/mnt/data/P9_XG7_VIVID_ATLAS_32_FINAL_20260902/independent_verification_report.json)
- [Watertight OBJ](sandbox:/mnt/data/P9_XG7_VIVID_ATLAS_32_FINAL_20260902/p9_xg7_third_spine_centered.obj)
- [Watertight STL](sandbox:/mnt/data/P9_XG7_VIVID_ATLAS_32_FINAL_20260902/p9_xg7_third_spine_centered.stl)
- [Packaged verifier transcript](sandbox:/mnt/data/P9_XG7_VIVID_ATLAS_32_FINAL_20260902/RUN_ALL_OUTPUT.txt)
- [Clean-extraction verifier transcript](sandbox:/mnt/data/P9_XG7_VIVID_ATLAS_32_CLEAN_VERIFY.txt)

Archive SHA-256:

```text
af4213766bd4755e8e59ec9ea42c64f79fad168836177adb40e2f709656fa34b
```

## Scope and uncertainty

This exact determination closes the displayed 45-coordinate `2^-25` endpoint chamber and proves literal deletion of the inherited `X2-X3` component. It does not exclude every possible two-row third-spine geometry, every coupled-old-plane realization, or the proposed three-row double-cap successor. No homogeneous convex polyhedral Gömböc is claimed.
