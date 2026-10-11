# figure-0171

Historical AI scientific report · saved 2026-08-30 UTC. Claims below retain their original status and have not all been independently checked. The current retained construction is C622; the C<500 search remains open.

---

# Bright Nova 52 — exact P9 finite-thickness three-cell successor

## Literal verdict

**NONWINNER.** I did not construct a homogeneous convex polyhedral Gömböc. The exact successor below is strict own-centred `(S,U,H)=(2,2,2)`, so it fails the journal's literal `(1,1,0)` gate. The starting point was the certified 24-row/19-active `C0–C1` endpoint and its 31-arrow obstruction; the requested move was a nonannular finite-thickness two/three-cell replacement with a transverse return band and at least three independent topology controls. :contentReference[oaicite:0]{index=0}

The finite-thickness topology was realized exactly. It drains the inherited stable `C0`, removes the inherited extra source `(o27,B6,C0)`, removes both inherited saddles `(C0,o26)` and `(A4,A5)`, and absorbs the old true `C0–C1` edge. However, those deaths occur at different circuit roots, not one coupled root, and the Morse packet is transported to a new stable `o9`, extra unstable vertex `(C0,XS,XU)`, and saddles `(A5,C1)` and `(XS,o102)`. The inherited protected source `(o26,A2,A3)` also deactivates; the surviving intended-side source is `(o102,XS,XR)`. Therefore this is a rigorous finite endpoint and obstruction, not a near-solution relabelled as success. :contentReference[oaicite:1]{index=1}

## Reproducible artifacts

- [Complete archive](sandbox:/mnt/data/P9_FT3_nonannular_NONWINNER_bundle.zip), SHA-256 `aeecf8f5985f58463fe61ca9eac77c63ec7522d19b4cf7aefb8a944c6f8e6732`.
- [Full handoff](sandbox:/mnt/data/P9_FT3_nonannular_NONWINNER_bundle/successor/P9_FT3_NONANNULAR_HANDOFF.md).
- [Deterministic exact generator](sandbox:/mnt/data/P9_FT3_nonannular_NONWINNER_bundle/successor/generate_p9_ft3_nonannular.py) and [complete exact H/V/audit object](sandbox:/mnt/data/P9_FT3_nonannular_NONWINNER_bundle/successor/p9_ft3_nonannular_exact.json), SHA-256 `12eee0cca91d58da00110852db6fdaa9f7cf3f12099f6b55515803dfd81b1f00`.
- [H table](sandbox:/mnt/data/P9_FT3_nonannular_NONWINNER_bundle/successor/p9_ft3_nonannular_H.csv), [V table](sandbox:/mnt/data/P9_FT3_nonannular_NONWINNER_bundle/successor/p9_ft3_nonannular_vertices.csv), and [incidence](sandbox:/mnt/data/P9_FT3_nonannular_NONWINNER_bundle/successor/p9_ft3_nonannular_incidence.json).
- [Exact circuit atlas](sandbox:/mnt/data/P9_FT3_nonannular_NONWINNER_bundle/successor/p9_ft3_path_atlas.json), [topology certificate](sandbox:/mnt/data/P9_FT3_nonannular_NONWINNER_bundle/successor/p9_ft3_topology_and_circuits.json), [three-cell certificate](sandbox:/mnt/data/P9_FT3_nonannular_NONWINNER_bundle/successor/p9_ft3_three_cell_certificate.json), and [complete witness graph](sandbox:/mnt/data/P9_FT3_nonannular_NONWINNER_bundle/successor/p9_ft3_witness_graph_exact.json).
- [Independent clean-room verifier](sandbox:/mnt/data/P9_FT3_nonannular_NONWINNER_bundle/successor/verify_p9_ft3_cleanroom.py), [directed perturbation verifier](sandbox:/mnt/data/P9_FT3_nonannular_NONWINNER_bundle/successor/verify_p9_ft3_perturbation_interval.py), and [mesh validator](sandbox:/mnt/data/P9_FT3_nonannular_NONWINNER_bundle/successor/validate_p9_ft3_mesh.py).
- Matching [OBJ](sandbox:/mnt/data/P9_FT3_nonannular_NONWINNER_bundle/successor/p9_ft3_nonannular.obj) and [STL](sandbox:/mnt/data/P9_FT3_nonannular_NONWINNER_bundle/successor/p9_ft3_nonannular.stl).

The archive manifest passes `sha256sum -c` for every file, and the ZIP passes `unzip -t`.

## Exact dyadic generator

Let `D=2^16=65536`, `B_i=N_i/D`, and

`P_raw={x∈R^3 : B_i·x≤1 for all 27 rows}`.

The complete integer numerators are:

```text
label       Nx        Ny       Nz
o9       1051680   -401263   -42898
o26      -133742    386063   166113
o27     -1524624    326415    -1967
o32      -353930    141122    55701
o102     -739891    486833   155172
A0        473707   -321521  -154558
B0        388666   -288526   -90231
A1        247991   -289377  -165524
B1        199928   -261481   -96918
A2        109792   -251404  -159850
B2         89732   -239388   -97702
A3         21550   -265115  -183167
B3         11090   -218670   -95871
A4        -52363   -188310  -140742
B4        -53595   -197613   -92457
A5       -160081   -224456  -183296
B5       -115748   -177330   -89040
A6       -205921   -150128  -138513
B6       -172555   -142348   -78488
A7       -292455   -104426  -120671
B7       -253960   -107912   -70117
B8       -362825    -46492   -51642
C0        833961   -182726    46233
C1        -15212   -220362   -99010
XS        726108    420379   275955
XR       -243528   -100645  -231108
XU       -105182    -57899    14031
```

The ordinary uniform-volume centroid `c_B` is reconstructed exactly by a signed tetrahedral decomposition. Its decimal locator is

`c_B≈(-0.04460163459621233,-0.19132029566046713,0.3151565350575726)`.

The full rational components are in the exact JSON and clean-room report. Define

`H_i=B_i/(1-B_i·c_B)`.

Then `{x:H_i·x≤1}=P_raw-c_B`, and an independent exact `Fraction` rebuild gives ordinary centroid exactly `(0,0,0)`. Exact raw/centred volume is the same rational number stored in the JSON, with decimal locator `0.040466781580379314`.

Boundedness and irredundancy audit:

- 27 supplied rows; 12 actual active rows.
- Active: `o9,o27,o102,A0,B1,A3,A5,C0,C1,XS,XR,XU`.
- Strictly redundant: `o26,o32,B0,A1,A2,B2,B3,A4,B4,B5,A6,B6,A7,B7,B8`.
- Actual lattice `(V,E,F)=(20,30,12)`, Euler `20-30+12=2`, complexity `60`.
- Minimum exact centred inactive slack is positive, decimal `0.004975562204765678`.

## Complete actual V/F/E incidence

All 20 vertices, by active support triple:

```text
 0 (o9,A0,A3)          1 (o9,A0,XS)
 2 (o9,B1,A3)          3 (o9,B1,C1)
 4 (o9,C0,XS)          5 (o9,C0,XU)
 6 (o9,C1,XU)          7 (o27,o102,XR)
 8 (o27,o102,XU)       9 (o27,A5,C1)
10 (o27,A5,XR)        11 (o27,C1,XU)
12 (o102,XS,XR)       13 (o102,XS,XU)
14 (A0,A3,XR)         15 (A0,XS,XR)
16 (B1,A3,C1)         17 (A3,A5,C1)
18 (A3,A5,XR)         19 (C0,XS,XU)
```

All 12 maximal face cycles, in that vertex numbering:

```text
o9   3 2 0 1 4 5 6
o27  11 8 7 10 9
o102 8 13 12 7
A0   15 1 0 14
B1   16 2 3
A3   18 14 0 2 16 17
A5   10 18 17 9
C0   4 19 5
C1   9 17 16 3 6 11
XS   13 19 4 1 15 12
XR   7 12 15 14 18 10
XU   11 6 5 19 13 8
```

All 30 true primal edges; no face triangulation diagonal is included:

```text
(0,1) (0,2) (0,14) (1,4) (1,15) (2,3)
(2,16) (3,6) (3,16) (4,5) (4,19) (5,6)
(5,19) (6,11) (7,8) (7,10) (7,12) (8,11)
(8,13) (9,10) (9,11) (9,17) (10,18) (12,13)
(12,15) (13,19) (14,15) (14,18) (16,17) (17,18)
```

The complete exact coordinates of every H row and every vertex, every inactive inequality, common-support pair, Q facet, and Q edge are in the linked exact JSON/CSV/incidence files.

## Literal nonannular finite-thickness three-cell replacement

The 14 actual Q-boundary triangles containing at least one of `XS,XR,XU` are:

```text
(o9,A0,XS)       (o9,C0,XS)       (o9,C0,XU)
(o9,C1,XU)       (o27,o102,XR)    (o27,o102,XU)
(o27,A5,XR)      (o27,C1,XU)      (o102,XS,XR)
(o102,XS,XU)     (A0,A3,XR)       (A0,XS,XR)
(A3,A5,XR)       (C0,XS,XU)
```

They form a connected triangulated disk with `(V,E,F)=(11,24,14)`, Euler characteristic `1`, one boundary component, and boundary cycle

`A0-o9-C1-o27-A5-A3-A0`.

Thus the replacement surface is not an annulus. In the centred polar `Q=conv(H_i)`, the origin is strictly interior; coning this disk to the origin gives a genuine positive-volume 3-ball. It partitions exactly into:

- `C_S_drain`, base facets `(o9,A0,XS)` and `(o9,C0,XS)`; 2 tetrahedra.
- `C_R_outer`, base facets `(o27,o102,XR)`, `(o27,A5,XR)`, `(o102,XS,XR)`, `(A0,A3,XR)`, `(A0,XS,XR)`, `(A3,A5,XR)`; 6 tetrahedra.
- `C_U_return`, base facets `(o9,C0,XU)`, `(o9,C1,XU)`, `(o27,o102,XU)`, `(o27,C1,XU)`, `(o102,XS,XU)`, `(C0,XS,XU)`; 6 tetrahedra.

Their exact polar volumes are positive and stored as fractions in the three-cell certificate; decimal locators are `37.762022823764916`, `87.71953769834386`, and `108.42321776047064`. Pairwise interfaces are cones over the paths `A0-XS`, `XS-C0-o9`, and `XS-o102-o27`; the triple intersection is the radial edge `O-XS`, with no three-dimensional overlap. The union is a 3-ball.

The third return cell meets both other cells, so it is not serially attached. Actual transverse Q edges `XR-XS` and `XS-XU` dualize to true primal edges `(12,15)` and `(13,19)`.

Three independent exact topology controls are certified:

- `tau_S` moves `XS` and controls circuit `(o26,A0,C0,XS)`, with affine determinant slope `-38386062821691281/140737488355328≠0`.
- `tau_R` moves `XR` and controls `(A3,A4,A5,XR)`, slope `-5176852248341/1099511627776≠0`.
- `tau_U` moves `XU` and controls `(o27,B5,C0,XU)`, slope `1845585608947847/17592186044416≠0`.

The exact control Jacobian is diagonal, determinant

`366752881635462964861109395897041253316840387/2722258935367507707706996859454145691648`,

hence rank `3`.

## Exhaustive own-centred equilibrium audit

The exact class is `(S,U,H)=(2,2,2)`.

| type | exact feature | strict margin |
|---|---|---:|
| stable | `o9` | `0.3089044077241153` |
| stable | `o27` | `0.5821961800091424` |
| unstable | vertex 12 `(o102,XS,XR)` | `0.019727266294107485` |
| unstable | vertex 19 `(C0,XS,XU)` | `0.03182435537397203` |
| saddle | edge `(9,17)`, supports `(A5,C1)` | `0.024863078327667373` |
| saddle | edge `(12,13)`, supports `(XS,o102)` | `0.012127431964778048` |

The saddle four-component cone coordinates are respectively

`(0.45512097224037706,0.5448790277596229,0.024863078327667373,0.02770474490399092)`

and

`(0.46778157506875595,0.532218424931244,0.016065741486628517,0.012127431964778048)`.

Every one of 12 face feet, 20 full vertex cones, and all four components of every one of 30 true-edge cones was audited exactly. The closest excluded true edge is supports `(C1,o9)` at primal edge `(3,6)`, decision `-0.0008983340847348245`.

## Exact diagonal circuit path and channel transitions

At `t=0`, the three new rows are strictly interior:

`XS=(2836,1642,1078)/65536`, `XR=(-951,-393,-903)/65536`, `XU=(-411,-226,55)/65536`.

All 27 rows follow the affine raw-support path

`q_i(t)=((1-t)q_i(0)+t q_i(1))/65536`.

The exact atlas stores an integer cubic determinant, a disjoint rational isolating interval, exact signs on both sides, and the actual facet symmetric difference for each of the 47 hull events. Decimal root locators and circuits, in exact order, are:

```text
 0  .005950446815666  (o26,o102,A3,A4)
 1  .034162633664303  (A1,B1,A2,B2)
 2  .100618639961257  (o27,o102,A5,A6)
 3  .108108262706546  (o9,A0,B0,B1)
 4  .141792291177563  (o26,o102,A4,A5)
 5  .184173919603121  (o9,A0,A1,B1)
 6  .194222331688790  (o26,A0,C0,XS)
 7  .292594891273175  (o27,B5,B6,C0)
 8  .296229181097008  (o26,A3,A4,XR)
 9  .296996676186488  (o26,A4,A5,XR)
10  .300872236339187  (o26,A2,A3,XR)
11  .301555461943890  (o26,A0,A1,XS)
12  .304480437382425  (o26,o102,A5,XR)
13  .304975499677958  (o26,A1,A2,XR)
14  .307782674881641  (o26,A1,XS,XR)
15  .312517172955432  (o9,A0,C0,XS)
16  .329461258755428  (o27,o102,A5,XR)
17  .341958041430038  (o26,o102,C0,XS)
18  .360616144244393  (A3,A4,A5,XR)
19  .365233954722837  (A0,A1,XS,XR)
20  .368778085507993  (o9,A1,B1,B2)
21  .390442981788061  (A3,A4,A5,C1)
22  .392040717931092  (A2,B2,A3,C1)
23  .476316300492742  (o26,o102,XS,XR)
24  .496015874321095  (A1,A2,A3,XR)
25  .536782444708464  (A1,A2,B2,A3)
26  .547898676336021  (o9,A1,B2,A3)
27  .566846197235170  (o32,o102,C0,XS)
28  .582198589322388  (o9,B2,A3,C1)
29  .594503498293084  (o27,o32,o102,XS)
30  .597509272647433  (o27,A5,B5,C1)
31  .640653160048101  (o27,o32,C0,XS)
32  .647865081246868  (o27,B5,C0,XU)
33  .663765202351428  (A0,A1,A3,XR)
34  .679643699417394  (o9,B5,C0,C1)
35  .685134450032395  (o27,o102,XS,XR)
36  .690916608552888  (o9,B5,C0,XU)
37  .695601102798084  (o9,B5,C1,XU)
38  .717708720460590  (o27,o102,XS,XR)
39  .720067353826499  (o9,A0,A1,A3)
40  .729897258513969  (o27,o32,C0,XS)
41  .763379100657200  (o27,o32,C0,XU)
42  .769206514909200  (o32,C0,XS,XU)
43  .773173159101272  (o27,o32,XS,XU)
44  .802811658339620  (o27,o102,XS,XU)
45  .879613584603137  (o27,B5,C1,XU)
46  .996764704400352  (o9,B1,A3,C1)
```

Independent path verification: `PASS`; 47 events, 34 start Q triangles, 20 end Q triangles, event hash `f1d36e79ff09b1c62569663236aad355bc6f64db7d91295458e9f97f1dd9b769`.

Named transitions:

- First inherited saddle `(C0,o26)` relays at event 6 through `(o26,A0,C0,XS)` and becomes `(o26,XS)` in the next chamber.
- Inherited extra source `(o27,B6,C0)` loses its old facet at event 7 through `(o27,B5,B6,C0)`, relays via `(o27,B5,C0)`, and ends as `(C0,XS,XU)`.
- Return saddle `(A4,A5)` is dismantled across events 18, 21, and 22 and ends as `(A5,C1)`.
- Old `C0-C1` spine is absorbed at event 34 through `(o9,B5,C0,C1)`; both incident predecessor Q facets disappear.
- `C0` ceases to be stable before the endpoint and has a strict negative endpoint stable decision.

The 48 open-chamber audits start at `(2,2,2)`, pass through chambers including `(3,2,3)`, `(3,4,5)`, and `(2,3,3)`, and finish at `(2,2,2)`.

**Coupled-event certificate: FAIL.** Both saddle channels are crossed and the inherited stable/source labels die within one connected rank-three family, but at distinct roots. No common root simultaneously drains `C0`, destroys the extra source, and reverses both saddle channels.

## Complete witness certificate and first structural obstruction

Stable-face witness rule: `i→j` iff row `j` strictly excludes the perpendicular foot of face `i`. The complete active graph is:

```text
o9   -> []
o27  -> []
o102 -> [o27]
A0   -> [C0,o9]
B1   -> [A0,C0,o9]
A3   -> [A0,B1,o9]
A5   -> [o27]
C0   -> [o9]
C1   -> [B1,o9]
XS   -> [C0,o9]
XR   -> [A5,o102,o27]
XU   -> [A5,o102,o27]
```

The stable sinks are exactly `o9` and `o27`; `C0` has drained only into the new `o9` basin, not into `o27`.

For unstable vertices, orient every true edge from smaller to larger exact squared radius. The complete 20-vertex/30-edge graph, exact radius derivatives, and shortest paths are in the witness JSON. Its sinks are exactly:

- vertex 12 `(o102,XS,XR)`, squared radius `≈1.0441696388081685`;
- vertex 19 `(C0,XS,XU)`, squared radius `≈1.3663979100979193`.

Two exact obstructions result:

1. `||o27||/||o9||≈1.1235035877629964`, with angular separation `≈170.917957161145°`. The strict witness-arrow inequality plus convexity of `-log(cos)` requires at least 39 arrows, hence 40 distinct active rows, to remove `o9` while retaining `o27` at these directions/norms. The endpoint has 12 active and only 27 supplied rows. With at most 26 arrows, the required norm ratio is `≈1.1870924840056285`, a `≈5.65987478235%` relative increase.
2. Vertex 19 exceeds vertex 12 in exact squared radius by a positive rational stored in the witness file, decimal `0.3222282712897509`. Since every fixed-vertex witness arrow strictly increases squared radius, the extra source cannot drain into vertex 12 without deactivation or a macroscopic radius reversal.

This is the first structural obstruction a genuinely new successor must beat. Another annulus, relay chain, or local one-dimensional flip cannot solve the endpoint with the current direction/radius data.

## Positive perturbation radius

Directed 100-decimal interval arithmetic certifies independent `L_infinity` perturbations of every coordinate of all 27 raw rows, followed by recomputation of the ordinary centroid and dependent recentering, at

`epsilon=2^-24=5.9604644775390625e-8`.

Certified lower bounds:

- oriented four-row determinant: `5.937970776192765e-5`;
- raw inactive slack: `0.004091266608385876`;
- face tetrahedron volume: `1.6022611227925125e-6`;
- centering denominator: `0.6918988215622289`;
- centred inactive slack: `0.004812318356510211`;
- every mechanical decision magnitude: `0.0008936271334734816`.

Volume is enclosed by

`[0.0404658619701778380370673654240976578730691783272021290175098903009372535416520616529239902326331748078149, 0.0404677011906663075103594239443262377582373183371962790080877391902896401473093494975890716140967819965941]`.

The box preserves the entire actual lattice and exact feature set `(2,2,2)`. A second check at `2^-26` also passes.

## Independent verification and matching meshes

- Clean-room verifier: `PASS`; it hard-codes only the 27 integer rows, reconstructs the hull and exact ordinary-volume moments with `fractions.Fraction`, recentres independently, and exhaustively audits 12 faces, 20 vertices, and 30 four-component true-edge cones. Source-row SHA-256: `fba9cb6f17fbe3f5f27d1d4f6a51398d6f3c7874a6b89c7c1472f92cb927a1cf`.
- OBJ SHA-256 `60b0572f1c39be9d87ca7771a9bed75d075ccad723d1c5ecb83c7d375b9df20c`: 20 vertices, 36 triangles, watertight, consistently wound, Euler 2, volume exactly matching the generated body to reported precision.
- STL SHA-256 `c087ff48977d9dfab85f67c83cfd9d5b508a66405d973dee7e03e22482fc37ca`: same inventory, bounds, winding, Euler number, and volume. Cross-mesh status `PASS`.

All reproduction commands were rerun. Generator, exact verifier, 47-event path verifier, disk/topology certificate, three-cell certificate, witness certificate, `2^-24` interval certificate, and OBJ/STL validation all pass.

## What was tried, freshness, and uncertainty

The endpoint came from direct three-row finite-thickness patch search followed by denominator-`2^16` exactification. Additional fixed-incidence radial and full-coordinate autodiff, branch-style constrained searches, common-metric searches, and a second three-row cell layer were tested. Their best points approached incidence walls and transported the Euler-neutral packet; none yielded strict `(1,1,0)`.

Those numerical failures are not a theorem excluding every nonannular volumetric successor. The exact claims independent of search coverage are the supplied generator, own-centering, boundedness/irredundancy, full incidence, `(2,2,2)` audit, disk/three-cell topology, rank-three controls, 47 exact circuit transitions, positive perturbation box, complete witness graphs, two structural obstructions, and matching meshes.

## Most useful continuation

Do not append another serial band. A new cross-gap nonsimplicial cell must simultaneously deactivate the `o9` stable basin and vertex 19 `(C0,XS,XU)`, while protecting `o27` and either restoring predecessor source `(o26,A2,A3)` or preserving endpoint source `(o102,XS,XR)`. The entrance gate is one actual circuit cell that removes both unwanted sinks, or a macroscopic direction/radius change that reduces the face-chain requirement below the row budget and reverses the exact source-radius ordering. Keep three moment variables dependent for exact ordinary-volume centering, and add separate antibirth controls for the two transferred saddle channels.

## Reproduction order

```bash
cd successor
python generate_p9_ft3_nonannular.py
python verify_p9_ft3_cleanroom.py
python verify_p9_ft3_path.py
python build_p9_ft3_topology_certificate.py
python build_p9_ft3_three_cell_certificate.py
python build_p9_ft3_witness_certificate.py
python verify_p9_ft3_perturbation_interval.py
python validate_p9_ft3_mesh.py
```
