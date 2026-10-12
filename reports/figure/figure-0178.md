# figure-0178

AI research report · 2026-09-01 UTC

<!-- historical-status:start -->
> **Historical AI report.** The title and claims below reflect the AI’s assessment at the time. Claims of proof, certification or completion are not a current verification verdict.
>
> [C622](../../C622/README.md) passes the supplied exact checks; the search for C<500 remains open. See [verification status and source gaps](../../catalog/coverage.md).
<!-- historical-status:end -->

---

# Steady Harbor 62 — exact J44/J45 finite determination

## Disposition: **EXACT NONWINNER**

I did not obtain a homogeneous convex polyhedral Gömböc. Starting from the accepted ordinary-centred `J43_shared_metric` body `(H,V,E)=(2370,4736,7104)`, class `(3,3,4)`, I executed the requested connected finite-thickness continuation over its 143-row carrier, exactified the first post-replacement body `J44_two_sheet_crossgap`, and then compressed the connected terminal one-ring to the exact 13-face body `J45_two_sheet_terminal13`. The supplied journal identified precisely this two-sheet/cross-gap continuation as open.

The strongest endpoint is an interval-isolated uniform-density convex polyhedron at its own ordinary-volume centroid, with complete irredundant H/V/true-edge incidence, positive mechanics margins, a positive five-dimensional perturbation box, watertight OBJ/STL, and an independent verifier. Its strict class is `(2,2,2)`, not `(1,1,0)`.

## 1. Deterministic exact construction

Both conclusion-bearing cells are represented by exact affine-dyadic polar families

```text
P(x)={y:q_i(x)·y<=1},
q_i(x)=q_i^0+x0 D0[i]+x1 D1[i]+x2 D2[i],
Dk[i,:]=q_i^0 q^0_{i,k}.
```

Every hexadecimal binary64 coefficient is interpreted as its exact dyadic rational. The three `x` variables are dependent controls determined by the hard equations `Mx=My=Mz=0`.

```text
J44 source: source/J44_two_sheet_crossgap_local_family.json.gz
file SHA-256: 479860b68425f15648bc610f4a5594cf9006556c726e882c7e1cbcbe85ba1078
Q SHA-256:    e78b1b248f03d42a933684155f5e43d040d757a27825cadd8ad39e02e32e5c34
D SHA-256:    7a383cdff3529e632553abc506165c34ed427ce828c25f760b8ee34c32e041f2
common H denominator: 2^104

J45 source: source/J45_two_sheet_terminal13_local_family.json.gz
file SHA-256: f327e7eb4d5c1eb81acd682ad7bdc911b44286b0d78a6c3347e580a7c6feeee8
Q SHA-256:    3ca7390cd91fa52a1ff26ba9f750bb896991736993e6e7e0e403f1abf7b18dac
D SHA-256:    2c3c544c2cf6b3c4758c0b77f74d11b71f50fe67dff39e4c3acda1f05f5ec285
common H denominator: 2^105.
```

`repro/rebuild_J44_J45_exact.py` rebuilds the H/V tables, maximal faces, true edges, meshes, and root certificates from these canonical families without importing the search or source generators. The package check also reconstructs both decompressed source payloads from the packaged search records and seeds.

### Connected replacement

The first stage uses all 143 rows of `research/J43_smallest_new_topology.json`. Their induced J43 true-edge graph is connected with 257 edges. Thirty-five support modes jointly cover the low U–H sheet, high S–H sheet, and the 31-edge cross-gap closure. Every carrier row is active before replacement; 19 remain active in J44.

```text
J43 -> J44: (2370,4736,7104) -> (992,1980,2970)
Delta HVE = (-1378,-2756,-4134)
active rows removed/added/kept = 1393/15/977.
```

The second stage acts on a connected 343-row J44 one-ring with 875 induced true edges and suppresses 979 of 992 active rows:

```text
J44 -> J45: (992,1980,2970) -> (13,22,33)
Delta HVE = (-979,-1958,-2937).
```

Across `J43 -> J45`, 2,359 old active rows disappear, two enter, and eleven survive. Every old J43 unstable or saddle label is absent at J45. The exact ledger is `certificates/J44_J45_two_sheet_crossgap/replacement_certificate.json`, SHA-256 `c944634c91abd9b7f5eeba7cbca239069431c7ae5d82792e40f7de86cabc80a6`.

**Scope limit.** This proves the exact connected post-cells and simultaneous labelled feature replacement. It does not isolate a chronological scalar path crossing only two individually named nonsimplicial `2↔3/3↔2` walls. The two sheets and shared terminal cell are realized as the finite-thickness multi-control architecture; the accepted claim is the exact post-cell endpoint, not a wall-by-wall isotopy theorem.

## 2. First exact post-cell `J44_two_sheet_crossgap`

```text
candidate/active/inactive H = 4324/992/3332
(V,E,F) = (1980,2970,992)
surface triangles = 3956; Euler = 2
signature = f40ec8b3d4cafb941f7505e1d1919049fb2182492e42fdd27de77c79e5600a21
class = (2,2,2)
stable rows = 2463,2481
unstable triples = (0,1157,1160), (4157,4192,4193)
saddle true edges = (2453,2490), (2474,2507).
```

The unique root of all three ordinary moments lies in `[-2^-47,2^-47]^3`. The midpoint Jacobian has determinant `-22.810283655474844` and condition number `1.000000000030162`; the Krawczyk image is strictly interior. Directed volume is `[2.836026134586642,2.836026134586643]`.

All `8,555,580` actual row/nonincident-vertex pairs remain strict on the root box; the minimum gap is `1.4621093225031243e-9`. Full-cone directed margins are

```text
stable included / face excluded    +0.1457911409907466 / -0.014502391493820042
unstable included / vertex excluded +0.07357813110635722 / -0.060837222090151646
saddle included / edge excluded     +0.22564973956030096 / -0.04572739108359442.
```

## 3. Strongest exact endpoint `J45_two_sheet_terminal13`

```text
candidate/active/inactive H = 4324/13/4311
(V,E,F) = (22,33,13)
surface triangles/mesh edges = 40/60; Euler = 2
signature = cd7dc590c25755305c1045c1ca62ac63235b48457bc1d60d0cb3a596193d8d9e
class = (2,2,2)
active H rows = 0,1160,2453,2463,2467,2468,2475,2481,2490,2505,4101,4137,4229
stable rows = 2463,2475
unstable triples = (0,2453,2481), (2475,2505,4229)
saddle true edges = (2453,2481), (2468,2505).
```

### Ordinary-volume centroid certificate

`Mx=My=Mz=0` has exactly one root in

```text
[-1/274877906944,+1/274877906944]^3=[-2^-38,2^-38]^3.
```

The midpoint moment Jacobian has determinant `-0.16939278263148444`, condition number `1.000000000004643`, and strictly interior Krawczyk image

```text
lower = (-9.393915076311513e-16,-7.163676240176855e-17,-3.0854930315158246e-18)
upper = ( 2.653776708234781e-16, 7.923458692717235e-17, 1.1447182342032174e-17).
```

The directed volume interval is `[0.5533054747607876,0.5533054747607878]`. Therefore the origin is the unique accepted body's ordinary uniform-volume centroid; this is not auxiliary mechanical centering.

### Complete incidence and equilibrium audit

All `95,062` actual row/nonincident-vertex pairs are strict. The minimum inactive gap is `0.0003192789589198108`, at row `2476` against the vertex with active triple `(0,2475,2481)`. No face, vertex, or true-edge component is ambiguous. Root-box margins are

```text
stable included / face excluded     +0.015371942586828056 / -0.0006314433131529017
unstable included / vertex excluded +0.0014046340918490044 / -0.0021931963525181077
saddle included / edge excluded      +0.1984107960646976 / -0.04212328494129646.
```

The five independent trace-free symmetric metric controls satisfy `|s_k|<=2^-16`. On the combined `3+5` box the map has singular-value lower bound `0.9999237060546875`, determinant interval `[0.999938965309389,1.0000610370189256]`, and the complete strict `(2,2,2)` class persists. Closest combined-box margins remain `+0.015003257832338244`, `-0.0002487881408974601`, `+0.0013350510779877888`, `-0.0020443663179730387`, `+0.19828486566078024`, and `-0.03396187001468797` for included/excluded S, U, and H decisions respectively.

### Complete literal H/V/E data

The exact affine source, all 4,324 H rows and active flags, filtered active H rows, every exact Cramer vertex, root-box H/V interval enclosures, all maximal-face cycles, every true edge, and all oriented surface triangles are supplied as

```text
cells/J45_two_sheet_terminal13/H_exact.tsv.gz
cells/J45_two_sheet_terminal13/H_active_exact.tsv.gz
cells/J45_two_sheet_terminal13/V_exact.tsv.gz
certificates/J45_two_sheet_terminal13/root_box_active_H_intervals.tsv.gz
certificates/J45_two_sheet_terminal13/root_box_V_intervals.tsv.gz
cells/J45_two_sheet_terminal13/maximal_face_cycles.tsv.gz
cells/J45_two_sheet_terminal13/true_edges.tsv
cells/J45_two_sheet_terminal13/surface_triangles.tsv
research/J45_literal_active_data.json
research/J45_literal_active_data.md.
```

The 22 actual vertex triples are

```text
(0,1160,2463) (0,1160,2490) (0,2453,2481) (0,2453,2490)
(0,2463,2467) (0,2467,2468) (0,2468,2505) (0,2475,2481)
(0,2475,2505) (1160,2463,2490) (2453,2481,2490)
(2463,2467,4229) (2463,2490,4137) (2463,4137,4229)
(2467,2468,4229) (2468,2505,4229) (2475,2481,4229)
(2475,2505,4229) (2481,2490,4101) (2481,4101,4229)
(2490,4101,4137) (4101,4137,4229).
```

The 13 maximal-face cycles are

```text
H0:    0,1,3,2,7,8,6,5,4
H1160: 9,1,0
H2453: 2,3,10
H2463: 4,11,13,12,9,0
H2467: 5,14,11,4
H2468: 6,15,14,5
H2475: 16,17,8,7
H2481: 2,10,18,19,16,7
H2490: 1,9,12,20,18,10,3
H2505: 8,17,15,6
H4101: 18,20,21,19
H4137: 13,21,20,12
H4229: 11,14,15,17,16,19,21,13.
```

Every true edge is in `true_edges.tsv`; in `(V0,V1;H0,H1)` form:

```text
(0,1;0,1160) (2,3;0,2453) (0,4;0,2463) (4,5;0,2467)
(5,6;0,2468) (7,8;0,2475) (2,7;0,2481) (1,3;0,2490)
(6,8;0,2505) (0,9;1160,2463) (1,9;1160,2490)
(2,10;2453,2481) (3,10;2453,2490) (4,11;2463,2467)
(9,12;2463,2490) (12,13;2463,4137) (11,13;2463,4229)
(5,14;2467,2468) (11,14;2467,4229) (6,15;2468,2505)
(14,15;2468,4229) (7,16;2475,2481) (8,17;2475,2505)
(16,17;2475,4229) (10,18;2481,2490) (18,19;2481,4101)
(16,19;2481,4229) (18,20;2490,4101) (12,20;2490,4137)
(15,17;2505,4229) (20,21;4101,4137) (19,21;4101,4229)
(13,21;4137,4229).
```

## 4. Exact first unavoidable packet

The row-disjoint pairs

```text
(2463,2490), (2475,2481)
```

are actual true edges. A directed interval audit checks every external true neighbour at both endpoints. The global minimum external numerator lower bound is `141.40650634057403`, and the global minimum cross-norm-squared lower bound is `685.9832358163093`. Hence at least one endpoint of each edge is stable; row disjointness gives `S>=2` throughout the exact moment-root box. The exhaustive audit attains equality. This proves the exact NONWINNER disposition without relying on search exhaustion.

## 5. Search and attempted falsification

The finite deterministic search recorded

```text
stage-1 connected 143-row topology samples: 500
stage-1 metric proposals: 67,200
stage-2 connected 343-row topology samples: 300
stage-2 metric proposals: 240,000
zero-metric baselines: 356
total topology samples/proposals: 800/307,200
strict (1,1,0) found: 0.
```

All selected exactifiable endpoints were `(2,2,2)`. A separate 64-start, 5,000-step differentiable fixed-chart probe was rejected as evidence because its best iterate left the certified chart. The search ledger is empirical and is **not** asserted as a global impossibility theorem.

## 6. Residual circuit and required stronger topology

The two J45 saddle packets both route to both stable terminals `2463,2475` and both unstable terminals `(0,2453,2481)` and `(2475,2505,4229)`. The residual is one connected K2,2-like Morse component, not two separable defects. Its exact nine-row carrier is

```text
0,2453,2463,2468,2475,2481,2490,2505,4229.
```

The smallest stronger topology supported by this evidence is one shared three-dimensional double-circuit cell spanning both forcing edges, both saddle stars, and both unstable terminal facets, with a transverse return tetrahedron through rows `0` and `4229`. Beyond the three dependent moment variables it needs three topology controls: one for each forcing-edge circuit and one shared relay/antibirth control through `0,2468,2505,4229`. The acceptance condition is a single strict cell where both forcing edges and both saddles are absent, exactly one stable and one unstable equilibrium remain, and no replacement S–H or U–H pair is born. This is not claimed as a theorem of global row-minimality.

## 7. Independent verification and artifacts

`verifier/verify_steady_harbor62.py` independently reparses the exact source and tables; reconstructs both hulls, all active/inactive rows, every exact Cramer vertex, every maximal face and true edge; verifies complete root-box H/V interval ledgers; redoes both ordinary-moment Krawczyk proofs; audits all `8,555,580+95,062` actual nonincidences and every face/vertex/four-component edge-cone primitive; checks replacement connectivity, metric box, forcing matching, residual routing, and watertight OBJ/STL. A fresh archive extraction returned

```text
EXTRACTED_MANIFEST_OK
STEADY_HARBOR62_SOURCE_RECONSTRUCTION_PASS
STEADY_HARBOR62_ALL_CHECKS_PASS
STEADY_HARBOR62_PACKAGE_PASS
EXTRACTED_POST_RUN_MANIFEST_OK.
```

- Exact J44/J45 NONWINNER archive (`Steady_Harbor_62_J44_J45_exact_NONWINNER.zip`)
- Independent verification receipt (`Steady_Harbor_62_J44_J45_verification_receipt.txt`)

```text
archive SHA-256 0a4c77f243f29139e32749bf41b36199813e6db75ec2c323d272e7d611dabe94
receipt SHA-256 04a4f80b0ce1e159339035a2abd017079905e0b73108a0015cf50022ac936553
```

**Final boundary:** `J45_two_sheet_terminal13` is a complete exact ordinary-centred NONWINNER with class `(2,2,2)`. The first unavoidable packet is the forcing matching `(2463,2490),(2475,2481)`. Continue only with the shared nine-row double-circuit/return-tetrahedron topology above; another serial support transfer is below the proved obstruction.
