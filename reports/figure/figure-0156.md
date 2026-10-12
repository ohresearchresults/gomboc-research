# figure-0156

AI research report · 2026-08-29 UTC

---

# P9 shared-transverse-cross-edge continuation

## Literal verdict

**NONWINNER.** No homogeneous convex polyhedral Gömböc was found in the realized family. The strongest certified post-circuit endpoint is an exact rational/dyadic, uniform-density, own-centred convex polyhedron of strict class **`(S,U,H)=(2,2,2)`**.

The supplied run defines success as a finite rational or exactly isolated uniform-density polyhedron, evaluated at its own exact ordinary-volume centroid, with strict `(S,U,H)=(1,1,0)`, complete H/V/incidence and all-feature margins; wall points and near-solutions do not qualify. :contentReference[oaicite:0]{index=0}

This continuation starts from the journal's exact 22-support, 40-vertex, 60-edge P9 prismatic endpoint and attacks precisely the recorded smallest unexcluded topology: at least two new extreme supports with a shared transverse cross-edge, hard moment closure, and coupled retopology of the `o9` block while preserving `o27` and the intended unstable lineage. :contentReference[oaicite:1]{index=1}

The requested topology was nevertheless realized literally: two new support rows `C0,C1` are genuinely extreme, share one true transverse cross-edge, and belong to one connected communicating boundary complex that also contains the protected stable row, protected unstable lineage, the new extra stable and extra unstable features, and both saddle channels. The old P9 defects `o9`, `(o9,o32,B3)`, `(o9,o26)`, `(B3,A4,B4)`, and `(B4,B5)` are destroyed or retopologized; the Euler-neutral packet transfers rather than cancels.

## What was actually tried

1. Reconstructed the exact 22-support, 40-vertex, 60-edge predecessor.
2. Added initially interior `C0,C1` and followed one exact affine raw-support homotopy to a denominator-`2^16` endpoint.
3. Isolated and crossed **23 actual four-row hull-circuit walls**, rebuilding the complete hull and exact ordinary centroid in every one of the 24 open chambers.
4. Recomputed the own-centred representation `H_i=B_i/(1-B_i·c)` before every mechanical decision.
5. Audited every maximal face, every full vertex cone, and all four components of every true-edge cone.
6. Independently reran the compact-generator verifier, the path verifier, the directed perturbation verifier, and a watertight mesh verifier. All four pass.

The path atlas contains 23 chambers of class `(2,2,2)` and one transient `(2,3,3)` chamber; it contains no `(1,1,0)` chamber.

## Exact compact input generator

Let `B_i=2^-16 N_i` and

`P_raw = {x in R^3 : B_i·x <= 1 for every row i}`.

```text
label        Nx         Ny         Nz
o9       849845    -324254     -34665
o26      -59560     171927      73976
o27    -8445614    1808168     -10897
o32     -376593     150158      59268
o102    -431617     283995      90520
A0       741183    -503066    -241828
B0       732393    -543691    -170029
A1       578499    -675040    -386124
B1       569495    -744828    -276071
A2       349472    -800229    -508807
B2       334363    -892021    -364062
A3        70199    -863610    -596663
B3        48880    -963812    -422563
A4      -237714    -854879    -638931
B4      -258872    -954506    -446582
A5      -548717    -769379    -628294
B5      -566304    -867600    -435635
A6      -835050    -608795    -561698
B6      -853748    -704296    -388334
A7     -1068824    -381641    -441012
B7     -1093239    -464534    -301836
B8     -1248742    -160013    -177737
C0       647441    -141858      35893
C1       -70755   -1024981    -460529
```

All 24 inputs are exact dyadic rationals. The exact ordinary-volume centroid of `P_raw` is the rational triple stored under `source_centroid` in `p9_C01_shared_exact.json`; numerically

`c_B = (0.10772662236368616, 0.28791448515475604, -0.11574427811592185)`.

The exact own-centred H-representation is

`H_i = B_i / (1 - B_i·c_B)`.

Therefore `{x:H_i·x<=1} = P_raw-c_B` identically, its ordinary uniform-volume centroid is exactly `(0,0,0)`, and the three dependent centring controls have `DG=-I_3`, `DM=-V I_3`, determinant `-1`, and a unique rational root `u=c_B`. The isolated root box has radius `2^-120`; every projective denominator is positive, with nominal minimum about `0.47323948145573186`.

## Actual irredundant endpoint

- input rows: 24
- active support rows: 19
- inactive rows: `B3,B4,A7,B7,B8`
- `(F,E,V,C)=(19,51,34,102)`
- Euler check: `34-51+19=2`
- exact centred volume: stored as a rational in the endpoint JSON; decimal `0.10319011495426068`
- exact centroid after normalization: `(0,0,0)`
- exact centred inactive slack: decimal `0.0005368130435742962`

Active supports:

`o9,o26,o27,o32,o102,A0,B0,A1,B1,A2,B2,A3,A4,A5,B5,A6,B6,C0,C1`.

The full exact H table and all 34 exact vertices are materialized in `p9_C01_shared_H.csv`, `p9_C01_shared_vertices.csv`, and `p9_C01_shared_exact.json`. The clean-room script reconstructs them from the 24 integer triples alone.

## Maximal-face cycles

```text
o9   : 2 0 1 5 4 3
o26  : 7 9 8 10 11 6
o27  : 17 18 13 12 14 16 15
o32  : 13 19 12
o102 : 12 19 7 6 20 21 22 14
A0   : 8 9 1 0 23 24
B0   : 23 0 2
A1   : 10 8 24 25
B1   : 26 25 24 23 2 3
A2   : 11 10 25 26 27 28
B2   : 27 26 3 4
A3   : 20 6 11 28 29
A4   : 21 20 29 30
A5   : 16 22 21 30 31 15
B5   : 15 31 33 32 17
A6   : 14 22 16
B6   : 17 32 18
C0   : 1 9 7 19 13 18 32 33 5
C1   : 31 30 29 28 27 4 5 33
```

## Every true edge

Each line gives `edge-index [vertex0,vertex1] (the two common active supports)`. These are the 51 true polyhedral edges; no triangulation diagonal is included.

```text
00  [00,01]  (A0,o9)
01  [00,02]  (B0,o9)
02  [00,23]  (A0,B0)
03  [01,05]  (C0,o9)
04  [01,09]  (A0,C0)
05  [02,03]  (B1,o9)
06  [02,23]  (B0,B1)
07  [03,04]  (B2,o9)
08  [03,26]  (B1,B2)
09  [04,05]  (C1,o9)
10  [04,27]  (B2,C1)
11  [05,33]  (C0,C1)
12  [06,07]  (o102,o26)
13  [06,11]  (A3,o26)
14  [06,20]  (A3,o102)
15  [07,09]  (C0,o26)
16  [07,19]  (C0,o102)
17  [08,09]  (A0,o26)
18  [08,10]  (A1,o26)
19  [08,24]  (A0,A1)
20  [10,11]  (A2,o26)
21  [10,25]  (A1,A2)
22  [11,28]  (A2,A3)
23  [12,13]  (o27,o32)
24  [12,14]  (o102,o27)
25  [12,19]  (o102,o32)
26  [13,18]  (C0,o27)
27  [13,19]  (C0,o32)
28  [14,16]  (A6,o27)
29  [14,22]  (A6,o102)
30  [15,16]  (A5,o27)
31  [15,17]  (B5,o27)
32  [15,31]  (A5,B5)
33  [16,22]  (A5,A6)
34  [17,18]  (B6,o27)
35  [17,32]  (B5,B6)
36  [18,32]  (B6,C0)
37  [20,21]  (A4,o102)
38  [20,29]  (A3,A4)
39  [21,22]  (A5,o102)
40  [21,30]  (A4,A5)
41  [23,24]  (A0,B1)
42  [24,25]  (A1,B1)
43  [25,26]  (A2,B1)
44  [26,27]  (A2,B2)
45  [27,28]  (A2,C1)
46  [28,29]  (A3,C1)
47  [29,30]  (A4,C1)
48  [30,31]  (A5,C1)
49  [31,33]  (B5,C1)
50  [32,33]  (B5,C0)
```

The CSV `p9_C01_true_edges_full_cones.csv` additionally contains the exact four cone components for every edge.

## Exhaustive strict equilibrium audit

| status | feature | strict margin |
|---|---|---:|
| protected stable | `o27` | `0.3796323070052858` |
| unwanted stable | `C0` | `0.1302933484148043` |
| protected unstable lineage | `(o26,A2,A3)` | `0.3347340848140972` |
| unwanted unstable | `(o27,B6,C0)` | `0.3669332349688703` |
| saddle | `(C0,o26)` | `0.0105112202769859` |
| saddle | `(A4,A5)` | `0.02923310281172944` |

Every other feature is strictly excluded. The closest excluded primitives are:

- face `A4`: `-0.02298985993205524`;
- vertex `(A3,A4,C1)`: `-0.2003492828846802`;
- edge `(A5,o27)`: `-0.001615850268749824`.

Complete exact ledgers are supplied for all 24 input faces, all 34 vertices, and all four components of all 51 true edges. Hence the endpoint is an open strict `(2,2,2)` body, not a wall point or tolerance artefact.

## Literal shared transverse cross-edge and connected cell

The primal true edge `[5,33]` has common supports `(C0,C1)`. In the dual boundary, the edge `C0-C1` is incident to the actual facets `(o9,C0,C1)` and `(B5,C0,C1)`.

The following 13 actual dual facets form one connected edge-adjacent communicating subcomplex:

```text
(o9,C0,C1)
(B5,C0,C1)
(A5,B5,C1)
(A4,A5,C1)
(A3,A4,C1)
(A2,A3,C1)
(o26,A2,A3)
(o26,A1,A2)
(o26,A0,A1)
(o26,A0,C0)
(o27,B6,C0)
(o27,B5,B6)
(o27,A5,B5)
```

This one component contains the protected stable row `o27`, protected unstable lineage `(o26,A2,A3)`, extra stable `C0`, extra unstable `(o27,B6,C0)`, saddle `(C0,o26)`, return saddle `(A4,A5)`, and the `C0-C1` cross-edge.

## Complete traversed circuit atlas

The exact path is `B_i(t)=(1-t)B_i(0)+tB_i(1)`. The decimal values below are only locators; the atlas stores each exact determinant polynomial and a disjoint rational isolator narrower than `2^-100`.

```text
#   t locator          flip  exact four-row circuit
00  0.010737596741440  2->2  (o9,o32,B3,B4)
01  0.058133037248004  3->1  (o27,o102,A6,A7)
02  0.099250439295293  3->1  (o27,o32,B7,B8)
03  0.299319846798322  2->2  (o9,o32,B4,B5)
04  0.459732294725029  1->3  (o9,o26,o32,C0)
05  0.648609872853143  2->2  (o26,o32,o102,C0)
06  0.673988281049696  2->2  (o9,o32,B5,B6)
07  0.690947294588767  2->2  (o9,o26,A0,C0)
08  0.755892821360680  2->2  (o9,o32,B6,C0)
09  0.767985532041802  2->2  (o9,B5,B6,C0)
10  0.815374435580055  3->1  (o27,o32,B6,B7)
11  0.842989403773365  2->2  (o27,o32,B6,C0)
12  0.852719206135511  2->2  (o9,B4,B5,C0)
13  0.935511954924048  1->3  (o9,B3,B4,C1)
14  0.936954012976778  2->2  (B3,A4,B4,C1)
15  0.940151100201647  2->2  (A3,B3,A4,C1)
16  0.946657637164925  2->2  (o9,B4,C0,C1)
17  0.964428599340390  2->2  (o9,B2,B3,C1)
18  0.969272942253662  3->1  (B2,A3,B3,C1)
19  0.972874858438474  2->2  (B4,B5,C0,C1)
20  0.982091182748792  2->2  (A2,B2,A3,C1)
21  0.982379248987648  2->2  (A4,B4,A5,C1)
22  0.983620119124007  3->1  (B4,A5,B5,C1)
```

An independent exact verifier recomputed all 23 circuit polynomials, proved one sign-changing root in every isolator, rebuilt every chamber's complete dual facets, checked every adjacent symmetric difference, verified all support graphs connected, and reproduced the class histogram `{'(2, 2, 2)': 23, '(2, 3, 3)': 1}`. The `C0-C1` true edge first appears in chamber 17 and remains through chamber 23.

## Positive open-margin certificate

Directed 100-decimal interval arithmetic certifies independent `L_infinity` perturbation of every coordinate of every raw input row by

`epsilon = 2^-28 = 3.725290298461914e-9`,

followed by recomputation of the ordinary centroid and dependent exact support normalization. Over the entire box:

- minimum affine four-row determinant lower bound: `0.001027566341239464`;
- minimum raw inactive lower bound: `0.001504575907371053`;
- minimum centred inactive lower bound: `0.0003296172402790496`;
- minimum oriented face-tetrahedron lower bound: `1.754025117331154e-7`;
- minimum complete mechanical-decision lower bound: `0.001612016615149794`;
- all 19 faces, 34 vertices, and all four components on 51 true edges preserve the same strict `(2,2,2)` class.

The same verifier shows `2^-26` is too large for this proof and `2^-28` passes, so the reported radius is a demonstrated positive box, not a guessed decimal tolerance.

## Independent verification and mesh

The clean-room verifier hard-codes only the 24 integer triples. It imports none of the construction code and reconstructs with `fractions.Fraction`:

- all feasible triple intersections;
- the irredundant face lattice;
- exact volume and ordinary centroid;
- exact own-centred H rows;
- every inactive slack;
- every face projection test;
- every full vertex cone;
- all four components of every true-edge cone;
- the shared `C0-C1` edge and the connected 13-facet cell.

Status: **PASS**. Compact-source SHA-256:

`8f087f238687f9890c9b84a362922c35616553a777af8d3ec6334dfa41d25366`.

The exact path verifier and the directed perturbation verifier also pass. An independent `trimesh` audit loads both OBJ and STL with 34 merged vertices and 64 triangles; each is watertight, consistently wound, genus zero/Euler two, has volume `0.10319011495426071`, and differs from the exact rational volume by only `2.776e-17` in binary64 rendering. Their computed centres of mass are below `2e-16` in norm.

## Sharply delimited obstruction

A strict witness arrow `q_i -> q_(i+1)` satisfies

`q_i·q_(i+1) > ||q_i||^2`, hence `r_(i+1) cos(theta_i) > r_i`.

Witness norms strictly increase, so if `C0` remains active/nonstable and `o27` is the unique stable row, the witness path from `C0` must terminate at `o27`. For `k` arrows, spherical triangle inequality and convexity of `-log(cos theta)` give

`||o27||/||C0|| > sec(Theta/k)^k`,

where `Theta=angle(C0,o27)=176.9601631686... degrees`. At this endpoint

`||o27||/||C0|| = 1.170287198784004...`.

Exact dyadic/Chebyshev isolation certifies that `k=30` requires `1.1726498752638064...` and is impossible, while `k=31` first becomes admissible at `1.1666204652333498...`. Therefore, with these endpoint directions and norms:

- at least 31 witness arrows and 32 distinct active rows are necessary;
- the 19-active endpoint needs at least 13 additional active rows;
- even activating all 24 construction rows still needs at least eight more;
- with only 23 arrows, the target ratio must increase by more than `5.20577480457125%`.

This theorem is strictly stronger than the predecessor's one-new-row relay exclusion. Its scope is precise: a successor can escape by deactivating `C0` in the same event, materially rotating `C0` or `o27`, materially increasing the target norm ratio, or adding the required rows.

## Smallest genuinely new successor topology

The realized two-support shared edge is topologically real but quantitatively insufficient. The next nonrepeating topology is a finite-thickness, nonannular two-/three-cell replacement around the actual `C0-C1` spine, with a third transverse return band joining simultaneously:

- extra unstable facet `(o27,B6,C0)`;
- saddle star `(C0,o26)`;
- bridge/return star `(A4,A5,C1)`;
- protected source `(o26,A2,A3)`;
- protected stable row `o27`.

It needs at least three independent topology coordinates in addition to the three dependent centroid controls. The shared root must deactivate or drain `C0`, destroy the extra source, and cross both saddle channels together. Another serial row, local flip, or one-dimensional relay is excluded or observed only to transfer the packet.

## Reproducible artifact bundle

- [Consolidated exact bundle](sandbox:/mnt/data/P9_C01_shared_crossedge_NONWINNER_bundle.zip)
- [Bundle SHA-256](sandbox:/mnt/data/P9_C01_shared_crossedge_NONWINNER_bundle.zip.sha256)
- [Standalone handoff](sandbox:/mnt/data/P9_C01_shared_crossedge_NONWINNER/RESULT.md)
- [Compact exact source rows](sandbox:/mnt/data/P9_C01_shared_crossedge_NONWINNER/p9_C01_shared_source_rows.csv)
- [Complete exact endpoint JSON](sandbox:/mnt/data/P9_C01_shared_crossedge_NONWINNER/p9_C01_shared_exact.json)
- [Expanded exact centred H data](sandbox:/mnt/data/P9_C01_shared_crossedge_NONWINNER/p9_C01_shared_H.csv)
- [Expanded exact V data](sandbox:/mnt/data/P9_C01_shared_crossedge_NONWINNER/p9_C01_shared_vertices.csv)
- [Complete incidence](sandbox:/mnt/data/P9_C01_shared_crossedge_NONWINNER/p9_C01_shared_incidence.json)
- [All true edges and four cone components](sandbox:/mnt/data/P9_C01_shared_crossedge_NONWINNER/p9_C01_true_edges_full_cones.csv)
- [Full exact path/circuit atlas](sandbox:/mnt/data/P9_C01_shared_crossedge_NONWINNER/p9_C01_direct_path_atlas.json)
- [Moment-root certificate](sandbox:/mnt/data/P9_C01_shared_crossedge_NONWINNER/p9_C01_shared_moment_root_box.json)
- [Positive perturbation certificate](sandbox:/mnt/data/P9_C01_shared_crossedge_NONWINNER/p9_C01_shared_perturbation_radius_interval.json)
- [Exact chain obstruction](sandbox:/mnt/data/P9_C01_shared_crossedge_NONWINNER/p9_C01_shared_chain_obstruction_exact.json)
- [Independent exact endpoint verifier](sandbox:/mnt/data/P9_C01_shared_crossedge_NONWINNER/verify_p9_C01_shared_cleanroom.py)
- [Independent exact path verifier](sandbox:/mnt/data/P9_C01_shared_crossedge_NONWINNER/verify_p9_C01_path.py)
- [Directed perturbation verifier](sandbox:/mnt/data/P9_C01_shared_crossedge_NONWINNER/verify_p9_C01_perturbation_interval.py)
- [All-verifier transcript](sandbox:/mnt/data/P9_C01_shared_crossedge_NONWINNER/RUN_ALL_VERIFIERS.log)
- [Watertight OBJ](sandbox:/mnt/data/P9_C01_shared_crossedge_NONWINNER/p9_C01_shared.obj)
- [Watertight STL](sandbox:/mnt/data/P9_C01_shared_crossedge_NONWINNER/p9_C01_shared.stl)
