# figure-0266

AI research report · 2026-09-03 UTC · [Export notes](../../catalog/coverage.md#text-records)

---

# Bright Harbor 30 — exact finite handoff

## Determination

**USED — exact endpoint-changing anti-carrier NONWINNER.** The immutable parent `J54_FA5_sharedface8` is exact `(2,2,2)` with carrier `(12003,12004)`, packet `S12003 / U(2475,12000,12001) / H(2475,12000),H(2475,12001)`, and sinks `{2475,12003}`. Its 19-arc obstruction assumes exact endpoints `12003,2475` are retained.

The exact successor `J55_D17R_anti_carrier18` makes all five J54 nonprotected active rows `12000…12004` strictly inactive, including both carrier endpoints. It retains protected stable `2475` and protected unstable `(2475,5000,5003)`, has `2475` as the **sole** full row-star sink, and has no nonprotected row-disjoint all-positive carrier. Its strict own-centred class is nevertheless `(S,U,H)=(1,2,1)`: one connected nonsimplicial `U-H` pair survives. No Gömböc or completion ticket is claimed.

## Artifacts

- Exact replay archive (`Bright_Harbor_30_J55_D17R_anti_carrier18_exact_NONWINNER.zip`), 3,811,504 bytes, SHA-256 `d6f285ed83cd8b330af59796dfb30819d95db1a2d90b16c83deacb032bc9366b`.
- Receipt (`Bright_Harbor_30_J55_VERIFICATION_RECEIPT.json`), SHA-256 `dca62878f04d57c8e0e0659ae904d2824d8c8871932ea617bb3411dd59b301ab`; clean transcript (`Bright_Harbor_30_J55_CLEAN_VERIFICATION_TRANSCRIPT.txt`), SHA-256 `8799df06df23936a729592a25f1054ef8dafd75729961c2c202e5a7dd390dba1`.
- Exact source (`J55_D17R_anti_carrier18_exact_source.json`), SHA-256 `ba6f45ae283e444a4ee92ff14e4987041ca4e442a181892675f6b8af00759fa3`; full row-star graph (`J55_D17R_complete_directed_row_star_graph.json`).
- Connected transition ball (`J54_to_J55_D17R_connected_positive_volume_ball.json`); exact ingress witness (`J54_to_J55_D17R_exact_ingress_witness.json`).
- OBJ (`J55_D17R_anti_carrier18.obj`), SHA-256 `7b6dcebaf4131097ea9b1713928242783a7c067adb5847c782a5646a2e22df0c`; STL (`J55_D17R_anti_carrier18.stl`), SHA-256 `b2fe168e2095591be36bba1d4f085b2ce658d99f7f9123a9af9b386be5675ce3`.
- Standalone report (`Bright_Harbor_30_J55_RESULT.md`); hash ledger (`Bright_Harbor_30_J55_SHA256SUMS.txt`).

## Exact deterministic source

Parent payload SHA-256 is `954612ba384062c134784c55df56e86acf416eeaa5dc8a5b4beb09705d53330f`; parent exact-source SHA-256 is `f378f83fec589e6054fe8b42f22b6b505a69dbfbc27d4494b4198dca08c864e6`.

Let `N=2^24=16777216`, `z=-1/140`. For local rows `i=0,…,16`, set `q_i=(X_i/N,Y_i/N,z)` with integer pairs:

```text
00: (11653197,-13937873)
01: (5763878,-16027135)
02: (16793753,-9690398)
03: (20394447,-3554346)
04: (21762407,3910885)
05: (20408886,11892808)
06: (16140728,19400855)
07: (9124192,25373787)
08: (-90148,28809026)
09: (-9304549,25373787)
10: (-16321192,19400855)
11: (-20589485,11892808)
12: (-21943151,3910885)
13: (-20575324,-3554346)
14: (-16974741,-9690398)
15: (-11834262,-13937873)
16: (-5944980,-16027135)
```

Set the apex `q_17=(271080/N,-15609202/N,360000/N)`. Active labels in local order are

```text
[14000, 14001, 14002, 14003, 14004, 14005, 14006, 14007, 2475, 5000, 14008, 14009, 14010, 14011, 14012, 14013, 14014, 5003]
```

so local `(8,9,17)` is protected `(2475,5000,5003)`. Every other supplied row is exactly `2^-40` times its centred H row in the accepted J54 source, in order

```text
[12000, 12001, 12002, 12003, 12004, 0, 7001, 7002, 7003, 8000, 8001, 8002, 9000, 9001, 9002, 10000, 10001, 11000, 11001, 11002]
```

and all 20 are strictly inactive. The source generator enumerates the exact active hull, solves `q_i·p=1` for every maximal dual face, computes exact oriented volume/first moments, sets `c=M/V`, and applies `q_i↦q_i/(1-q_i·c)`, `p↦p-c`. This yields every supplied H row and every exact primal vertex. The raw 17-gon has common plane `z=-1/140`, hence its primal vertex is exactly `(0,0,-140)`.

## Mass, counts, separation

```text
H supplied/active/inactive = 38/18/20
primal (V,E,F)             = (18,34,18)
complexity                 = 68
ordinary centroid          = (0,0,0) exactly
first moments              = (0,0,0) exactly
```

Raw centring translation is approximately `(4.3814865233303952e-06,-0.00023672446501529329,-0.057734077017034417)`; minimum exact projective denominator is `0.99935996754492651`. Exact volume is

```text
6909113482072353555778602280753180589241446206225332077000695168860590740813970504134248327094369898332364381282926954813770733860611109902684809469118159734571590184552224749428749676400676017462475329746552734038062026999745013904571300791073387874697778114375040881590637665372700067144874174233512767205146624/34300728904104142737194633135168094098840707866993768043809909851446743140549110160659356249755284748948767961731727340829955799420943994441614465136670845481088098480432508553600308087384116040518135801303942364551735815924592093728515878152199574323050136830649256501883168349206320114922423308873636391256465
```

approximately `201.42759943639757`. Topology signature is `c71d6068ca6832fb294926430db94057e11481168ad9f44a260d892757d6ee45`. Minimum exact all-row nonincidence gap is `0.12843179906374241`; minimum inactive-row gap is `0.9999999999727518`.

## Complete H/V/E incidence

Every maximal dual face, equivalently every exact primal vertex:

```text
(14000,14001,5003); (14000,14002,5003); (14001,14014,5003); (14002,14003,5003); (14003,14004,5003); (14004,14005,5003); (14005,14006,5003); (14006,14007,5003); (14007,2475,5003); (2475,5000,5003); (5000,14008,5003); (14008,14009,5003); (14009,14010,5003); (14010,14011,5003); (14011,14012,5003); (14012,14013,5003); (14013,14014,5003); (14000,14001,14002,14003,14004,14005,14006,14007,2475,5000,14008,14009,14010,14011,14012,14013,14014)
```

Every maximal primal face cycle, in the preceding primal-vertex indices:

```text
14000:17,1,0
14001:0,2,17
14002:17,3,1
14003:17,4,3
14004:17,5,4
14005:17,6,5
14006:17,7,6
14007:17,8,7
2475:17,9,8
5000:17,10,9
14008:17,11,10
14009:17,12,11
14010:17,13,12
14011:17,14,13
14012:17,15,14
14013:17,16,15
14014:2,16,17
5003:0,1,3,4,5,6,7,8,9,10,11,12,13,14,15,16,2
```

Every true edge, by incident support/face labels:

```text
(14000,14001) (14000,14002) (14000,5003) (14001,14014) (14001,5003) (14002,14003) (14002,5003) (14003,14004) (14003,5003) (14004,14005) (14004,5003) (14005,14006) (14005,5003) (14006,14007) (14006,5003) (14007,2475) (14007,5003) (2475,5000) (2475,5003) (5000,14008) (5000,5003) (14008,14009) (14008,5003) (14009,14010) (14009,5003) (14010,14011) (14010,5003) (14011,14012) (14011,5003) (14012,14013) (14012,5003) (14013,14014) (14013,5003) (14014,5003)
```

The exact verifier independently enumerates all maximal raw faces from all `C(18,3)` triples before accepting this lattice. Euler is `18-34+18=2`.

## Exhaustive strict mechanics

Every one of 18 maximal faces, all 18 complete vertex cones—including the full nonsimplicial 17-gon normal polygon—and all 34 true-edge cones with all four components were evaluated exactly.

```text
stable:   [2475]
unstable: [[2475, 5000, 5003], [14000, 14001, 14002, 14003, 14004, 14005, 14006, 14007, 2475, 5000, 14008, 14009, 14010, 14011, 14012, 14013, 14014]]
saddles:  [[14001, 14014]]
```

Positive lower / excluded upper margins:

```text
stable   +0.11819709443183812 / -0.0015591156826137396
unstable +0.015665465631371722 / -0.015593134135393196
saddle   +0.00637623895537441 / -0.011583724466594886
```

The residual component is exactly the extra unstable 17-row normal polygon

`[14000, 14001, 14002, 14003, 14004, 14005, 14006, 14007, 2475, 5000, 14008, 14009, 14010, 14011, 14012, 14013, 14014]`

plus its boundary saddle `(14001,14014)`. There is no extra stable feature.

## Complete directed row-star and carrier audit

For every directed true-edge arc, `σ(i→j)=||q_i||²-q_j·q_i`. All 68 arcs were checked exactly. Row minima `min_j σ(i→j)/||q_i||²` are shown below; `*` marks a sink:

```text
14000:-0.0020715066964141098
14001:-0.0015591156826137396
14002:-0.0025963209465110181
14003:-0.0030790507393208631
14004:-0.0034874582737026258
14005:-0.0038056062755572875
14006:-0.0040395501014941102
14007:-0.0042009204435940403
2475:+0.11819709443183812*
5000:-0.0019105014608697365
14008:-0.002033172367467201
14009:-0.0023884570295405272
14010:-0.0029321498514973663
14011:-0.003585396550431105
14012:-0.004252158631363084
14013:-0.0048228364840636386
14014:-0.0051934515801106878
5003:-0.033863224760046939
```

The sink set is exactly `[2475]`. All 34 edges were also checked against every external-neighbour primitive at both endpoints. Exactly `(14007,2475)` and `(2475,5000)` are all-external-positive, with minima `0.31082881032088833` and `0.30633290682832581`; both meet protected sink `2475`. There is no nonprotected all-positive component and no reincarnation of `(12003,12004)`.

## Connected positive-volume endpoint change

The exact transition certificate starts with the 32-triangle boundary of the final active support hull coned to the origin and inserts the eight J54 active supports, scaled by `1/64`, through exact stellar subdivisions. It gives a connected 3-ball with

```text
vertices/edges/triangles/tetrahedra = 27/98/128/56
internal/boundary triangles        = 96/32
Euler characteristic               = 1
```

Every tetrahedron has positive exact volume; minimum is `8.2772747903701849e-07`. Minimum old-point/outer-face gap is `0.15795837986356842` and minimum insertion barycentric coordinate is `0.00055491388435277328`. The exact volume partition and face multiplicities pass. A connected 22-tetrahedron spine meets old rows `12000…12004`, relocated protected rows `2475,5000,5003`, and residual closure rows `14001,14014`. Thus `12003,12004` are swallowed into the strict interior; the 19-arc theorem is evaded by breaking its endpoint-retention premise, not by a short relay.

## Exact chronology—failure, not a claimed certificate

On the deterministic affine raw-support ingress with exact recentering, at `t=1/400` the active set is `[2475, 5003, 12000, 12001, 12002, 12003, 12004]` and class is `[2, 2, 2]`. Exact positive margins are:

```text
old S12003                         0.0018280433437925818
old U(2475,12000,12001)            0.0047308692563939915
old H(2475,12000)                  0.0055449247735769687
old H(2475,12001)                  0.004981408851900967
premature U(2475,5003,12001)       0.062822679211033475
```

Old carrier `(12003,12004)` remains true, while row `5000` is inactive and protected `U(2475,5000,5003)` is absent. Therefore `death_before_birth_achieved=false`. This exactly excludes the displayed ingress only; it does not exclude all paths to the endpoint.

## Positive chamber and controls

The exact paired metric family `P↦diag(x,y,1)P`, `Q↦Q diag(1/x,1/y,1)`, with `|x-1|,|y-1|≤2^-24`, preserves H/V incidence and centroid zero. Throughout the box it retains class `(1,2,1)`, sole sink `2475`, and outward-rounded margins

```text
stable   +0.11819685601765663 / -0.0015588769041523154
unstable +0.015665460602002908 / -0.015593129144812323
saddle   +0.0063762370639749667 / -0.011583110675348644
```

Two independent centroid-preserving controls monitor a limiting 17-gon unstable-cone component and the saddle beta component. At exact symmetric step `2^-20` their response matrix is

```text
[-52.98121077421959,-52.981209593428055]
[-2.2371165631333678e-13,-0.012650329612264914]
```

with exact nonzero determinant, decimal `0.6702297795389065`; rank is two.

## Delimited coverage and continuation

Empirical searches—used only for discovery—tested a single full-face cap, targeted three-cap cells, and a face-sharing double-Radon family. None produced `(1,1,0)`; the best latter state remained `(1,2,1)`. These searches are not global exclusions.

The first genuinely new continuation is a **two-boundary elongated antiprismatic zipper / internally face-sharing multi-cell belt** spanning the complete 17-gon normal polygon and closure saddle `(14001,14014)`, with simultaneous movement/deactivation of `14000,14001,14014` and an independently tunable return page. It must preserve sole sink `2475` and protected `U(2475,5000,5003)`, destroy the entire `U-H` component before substitute births, create no new sink or row-disjoint carrier, and retain at least two controls after exact moment closure. A single cap, short relay, or local split preserving the 17-gon closure repeats the exhausted transfer mechanism.

## Independent replay and mesh

Run `bash [internal-source-reference].sh` from the extracted archive. It checks manifests before and after; reconstructs the parent and successor; enumerates the exact face lattice; recomputes volume and zero moments; audits every inactive row, face, vertex cone, four-component edge cone, row-star arc, and external arrow; regenerates source/chronology/controls/shape/transition certificates byte-for-byte; and checks the mesh. Terminal markers are

```text
BRIGHT_HARBOR30_J55_ALL_INDEPENDENT_CHECKS_PASS
BRIGHT_HARBOR30_J55_CLEAN_PACKAGE_REPLAY_PASS
BRIGHT_HARBOR30_J55_CLEAN_EXTRACTION_ALL_PASS
```

The OBJ/STL has 18 vertices, 32 coherently oriented triangles, 48 mesh edges, edge multiplicity two, and Euler `18-48+32=2`; triangulation diagonals are excluded from true-edge mechanics.

**Integration boundary:** use J55 as the strongest exact endpoint in this branch: it genuinely removes the J54 packet, satisfies the sole-sink anti-carrier gate, and reaches the complementary near-class `(1,2,1)`. Do not call it a Gömböc; the exact residual `U-H` pair and chronology failure remain. The run-wide M42 `(2,1,1)` body remains the stronger opposite-side equilibrium-count benchmark.
