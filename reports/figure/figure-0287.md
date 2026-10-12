# figure-0287

AI research report · 2026-09-04 UTC · [Export notes](../../catalog/coverage.md#text-records)

<!-- historical-status:start -->
> **Historical AI report.** The title and claims below reflect the AI’s assessment at the time. Claims of proof, certification or completion are not a current verification verdict.
>
> [C622](../../C622/README.md) passes the supplied exact checks; the search for C<500 remains open. See [verification status and source gaps](../../catalog/coverage.md).
<!-- historical-status:end -->

---

# Bright Lynx 17 — exact finite determination

## Determination

**Exact nonwinner.** No finite homogeneous convex polyhedral Gömböc with strict own-centred `(S,U,H)=(1,1,0)` was reached. The strongest exact endpoint is `J56_BL17_two_boundary_return20_exact_NONWINNER`, a rational uniform-density convex polyhedron at its own ordinary-volume centroid with strict `(2,2,2)`. It is a genuine post-J55 topology change: the old full 17-gon unstable feature and old saddle `(14001,14014)` are absent, but a different connected replacement packet is present. The failed child `[internal-source-reference]` supplied no immutable evidence and was not used.

## Immutable parent reconstructed literally

- Parent assignment `figure-0266`; immutable result SHA-256 `49545ef8d787bb7886f19249253131f72ee0f35f1bb499c3bce73e75cbf23fd1`.
- Reconstructed parent source SHA-256 `ba6f45ae283e444a4ee92ff14e4987041ca4e442a181892675f6b8af00759fa3`. Parent `J55_D17R_anti_carrier18`: supplied/active `38/18`, primal `(18,34,18)`, exact strict `(1,2,1)`.
- Sole stable row `2475`; protected unstable facet `[2475,5000,5003]`; residual unstable feature is the full 17-gon; sole saddle `(14001,14014)`.

Parent raw generator: denominator `2^24=16777216`; every base row has `z=-1/140`; apex `5003=(271080,-15609202,360000)/2^24`. The exact base order and `(X,Y)` numerators are:

```text
14000: 11653197 -13937873
14001: 5763878 -16027135
14002: 16793753 -9690398
14003: 20394447 -3554346
14004: 21762407 3910885
14005: 20408886 11892808
14006: 16140728 19400855
14007: 9124192 25373787
2475: -90148 28809026
5000: -9304549 25373787
14008: -16321192 19400855
14009: -20589485 11892808
14010: -21943151 3910885
14011: -20575324 -3554346
14012: -16974741 -9690398
14013: -11834262 -13937873
14014: -5944980 -16027135
```

Its exact ordinary volume is the finite rational determinant sum obtained from this generator and its literal facet cycles; the reduced fraction is committed in the parent source, decimal `201.42759943639757`, and its three centered first moments are exactly zero. The immutable J54→J55 certificate is a connected positive-volume 56-tetrahedron 3-ball, but its affine chronology births a replacement before inherited death, so it is not a residual-pair cancellation path.

### Exact obstruction for the exhausted class

Let `F17(1/2048)` be all 17 coherent one-root fan lifts of the exact J55 polygon, retaining the protected sector and closure edge. The literal `fan17_exact_atlas.json` exhausts roots

```text
[14001, 14000, 14002, 14003, 14004, 14005, 14006, 14007, 2475, 5000, 14008, 14009, 14010, 14011, 14012, 14013, 14014]
```

Every exact cell has dual `(18,48,32)`, primal `(32,48,18)`, and strict `(1,2,1)`: the polygonal U transfers to a root triangle and saddle `(14001,14014)` survives. Uniform exact bounds over all cells are `S+>1/9`, `S-<-1/1000`, `U+>1/2000`, `U-<-1/2000`, `H+>1/300`, `H-<-1/200`. Hence no member of this precisely delimited class is `(1,1,0)`.

## Search and exactification

Exact reconstruction preceded search. Full-coordinate pyramid, two-cap, active-pair, metric, radial-chain, closure, short-return, and linked two-point searches either retained the old pair or birthed another packet. A six-row return page first made `14000,14001,14013` inactive and removed the old U/H carriers but gave `(2,2,2)`. An 18-cell topology walk reduced the numerical hard residual from `3.515124e-3` to `1.272430e-4`; sequential refinement crossed a three-saddle wall into `(3,2,3)`. Floating states were used only for discovery. The endpoint below was rounded to dyadics and independently rebuilt with exact `Fraction` arithmetic.

## Exact successor generator

All active raw polar rows have common denominator `D=1152921504606846976=2^60`; `q_l=(X,Y,Z)/D`.

```text
14002: 956781540335945088 -536410229928321664 4019884716693503
14003: 1406226489209154816 -103794471189016816 4685955598029740
14004: 1475713059339685888 430755460051839808 -7948144078288872
14005: 1394205783445780480 793373952520290816 -10799074423865428
14006: 1147482898419809920 1370095447449748224 -12365705918094794
14007: 634851591924333312 1842106326571678208 -9910453888949308
2475: 26946978386530440 2290319295624789248 3251779729455419
5000: -702850619300490752 1923419005286336256 -4719810412622237
14008: -1135239232441071872 1417887192155309824 -4982281129606102
14009: -1418188575846618880 784978523546213760 -5827625364205657
14010: -1497687898177854976 420475553266988928 -9525379500852712
14011: -1413552685858088448 -133894247537332928 7744491233546239
14012: -861049198914831104 -460909263606457152 -13055225265321400
14014: -220093356053075168 -454368642441942528 -51153711597627672
5003: 23257571277598492 -1859382110180459520 79712057895866752
15000: 23252402689361092 -1859727497384602368 72344427228160752
15001: 88756281131046592 -956832687297881088 -48248946666478104
15002: 100272453276617376 -275942571992589792 -74259075851711520
15003: 38728283355604488 -21459093804244588 -79302544409643008
15004: 4207199553190795 -74271851627333376 -77222334950637920
```

All literal parent labels remain supplied. The active labels are those 20 above. The 23 inactive labels are generated without hidden coordinates: let `B=(1/20)Σ_active q_i`, then `q_l=(1-d_l)B+d_l q_anchor`, with:

```text
14000: anchor=14002 d=1/4096
14001: anchor=14003 d=1/2048
14013: anchor=14004 d=3/4096
12000: anchor=14005 d=1/1024
12001: anchor=14006 d=5/4096
12002: anchor=14007 d=3/2048
12003: anchor=2475 d=7/4096
12004: anchor=5000 d=1/512
0: anchor=14008 d=9/4096
7001: anchor=14009 d=5/2048
7002: anchor=14010 d=11/4096
7003: anchor=14011 d=3/1024
8000: anchor=14012 d=13/4096
8001: anchor=14014 d=7/2048
8002: anchor=5003 d=15/4096
9000: anchor=15000 d=1/256
9001: anchor=15001 d=17/4096
9002: anchor=15002 d=9/2048
10000: anchor=15003 d=19/4096
10001: anchor=15004 d=5/1024
11000: anchor=14002 d=21/4096
11001: anchor=14003 d=11/2048
11002: anchor=14004 d=23/4096
```

Every `0<d<1`, so each inactive row is a strict convex combination of all active rows and is distinct and redundant.

## Exact own centroid, convexity, and volume

For each Q facet `{i,j,k}` below, solve `q_i·p=q_j·p=q_k·p=1` over the rationals. These are the 36 raw P vertices. Triangulate each P maximal face by the cycles below. For each outward triangle `(a,b,c)`, let `v=det(p_a,p_b,p_c)/6`; set `V=Σv`, `M=Σv(p_a+p_b+p_c)/4`, `c=M/V`, `P_f=p_f-c`, and `H_l=q_l/(1-q_l·c)`. Thus `M_centered=M-cV=(0,0,0)` exactly. This finite determinant sum is the exact rational ordinary volume; reduced value is in the source and equals approximately `44.954397571470537>0`. Exact checks give active projective denominator `>9/10`, active nonincidence `>1/1000`, inactive separation `>7/10`; therefore the body is bounded, convex, and all 20 active supports are irredundant.

## Complete actual H/V/E incidence

Q maximal triangular faces, indexed as P vertices:

```text
00: [14002, 14003, 15000]
01: [14002, 14003, 15001]
02: [14002, 15000, 15001]
03: [14003, 14004, 14005]
04: [14003, 14004, 15002]
05: [14003, 14005, 14006]
06: [14003, 14006, 5003]
07: [14003, 5003, 15000]
08: [14003, 15001, 15002]
09: [14004, 14005, 15003]
10: [14004, 15002, 15003]
11: [14005, 14006, 15003]
12: [14006, 14007, 2475]
13: [14006, 14007, 15003]
14: [14006, 2475, 5003]
15: [14007, 2475, 15003]
16: [2475, 5000, 5003]
17: [2475, 5000, 15003]
18: [5000, 14008, 5003]
19: [5000, 14008, 15003]
20: [14008, 14009, 14011]
21: [14008, 14009, 15003]
22: [14008, 14011, 5003]
23: [14009, 14010, 14011]
24: [14009, 14010, 15003]
25: [14010, 14011, 14012]
26: [14010, 14012, 14014]
27: [14010, 14014, 15004]
28: [14010, 15003, 15004]
29: [14011, 14012, 15000]
30: [14011, 5003, 15000]
31: [14012, 14014, 15001]
32: [14012, 15000, 15001]
33: [14014, 15001, 15004]
34: [15001, 15002, 15004]
35: [15002, 15003, 15004]
```

Every true Q edge, with its two incident Q-face indices (the corresponding P-edge endpoints):

```text
00: [14002, 14003] -> P[0, 1]
01: [14002, 15000] -> P[0, 2]
02: [14002, 15001] -> P[1, 2]
03: [14003, 14004] -> P[3, 4]
04: [14003, 14005] -> P[3, 5]
05: [14003, 14006] -> P[5, 6]
06: [14003, 5003] -> P[6, 7]
07: [14003, 15000] -> P[0, 7]
08: [14003, 15001] -> P[1, 8]
09: [14003, 15002] -> P[4, 8]
10: [14004, 14005] -> P[3, 9]
11: [14004, 15002] -> P[4, 10]
12: [14004, 15003] -> P[9, 10]
13: [14005, 14006] -> P[5, 11]
14: [14005, 15003] -> P[9, 11]
15: [14006, 14007] -> P[12, 13]
16: [14006, 2475] -> P[12, 14]
17: [14006, 5003] -> P[6, 14]
18: [14006, 15003] -> P[11, 13]
19: [14007, 2475] -> P[12, 15]
20: [14007, 15003] -> P[13, 15]
21: [2475, 5000] -> P[16, 17]
22: [2475, 5003] -> P[14, 16]
23: [2475, 15003] -> P[15, 17]
24: [5000, 14008] -> P[18, 19]
25: [5000, 5003] -> P[16, 18]
26: [5000, 15003] -> P[17, 19]
27: [14008, 14009] -> P[20, 21]
28: [14008, 14011] -> P[20, 22]
29: [14008, 5003] -> P[18, 22]
30: [14008, 15003] -> P[19, 21]
31: [14009, 14010] -> P[23, 24]
32: [14009, 14011] -> P[20, 23]
33: [14009, 15003] -> P[21, 24]
34: [14010, 14011] -> P[23, 25]
35: [14010, 14012] -> P[25, 26]
36: [14010, 14014] -> P[26, 27]
37: [14010, 15003] -> P[24, 28]
38: [14010, 15004] -> P[27, 28]
39: [14011, 14012] -> P[25, 29]
40: [14011, 5003] -> P[22, 30]
41: [14011, 15000] -> P[29, 30]
42: [14012, 14014] -> P[26, 31]
43: [14012, 15000] -> P[29, 32]
44: [14012, 15001] -> P[31, 32]
45: [14014, 15001] -> P[31, 33]
46: [14014, 15004] -> P[27, 33]
47: [5003, 15000] -> P[7, 30]
48: [15000, 15001] -> P[2, 32]
49: [15001, 15002] -> P[8, 34]
50: [15001, 15004] -> P[33, 34]
51: [15002, 15003] -> P[10, 35]
52: [15002, 15004] -> P[34, 35]
53: [15003, 15004] -> P[28, 35]
```

Actual outward maximal P-face cycles:

```text
2475: [12, 15, 17, 16, 14]
5000: [16, 17, 19, 18]
5003: [6, 14, 16, 18, 22, 30, 7]
14002: [0, 2, 1]
14003: [0, 1, 8, 4, 3, 5, 6, 7]
14004: [3, 4, 10, 9]
14005: [3, 9, 11, 5]
14006: [5, 11, 13, 12, 14, 6]
14007: [12, 13, 15]
14008: [18, 19, 21, 20, 22]
14009: [20, 21, 24, 23]
14010: [23, 24, 28, 27, 26, 25]
14011: [20, 23, 25, 29, 30, 22]
14012: [25, 26, 31, 32, 29]
14014: [26, 27, 33, 31]
15000: [0, 7, 30, 29, 32, 2]
15001: [1, 2, 32, 31, 33, 34, 8]
15002: [4, 8, 34, 35, 10]
15003: [9, 10, 35, 28, 24, 21, 19, 17, 15, 13, 11]
15004: [27, 28, 35, 34, 33]
```

Thus Q `(V,E,F)=(20,54,36)`, P `(36,54,20)`, Euler `36-54+20=2`. The displayed mesh has 36 vertices, 68 coherently oriented triangles, 102 triangulation edges, each edge multiplicity two, Euler 2; triangulation diagonals are excluded from true-edge mechanics.

## Exhaustive equilibrium mechanics

Exact tests used by the independent verifier: a P face `i` is stable iff the foot `H_i/||H_i||²` satisfies every supplied inequality strictly; a P vertex dual to Q facet `[i,j,k]` is unstable iff `P_f/||P_f||²` has three positive exact barycentric coefficients in `conv(H_i,H_j,H_k)`; a P edge dual to Q edge `[i,j]` is a saddle iff its exact segment parameter `t`, `1-t`, and exact cone coefficients `α,β` in `A+t(B-A)=αH_i+βH_j` are all positive.

The verifier exhausts all `20+36+54=110` features and all four primitive components for every edge. Every decision component is nonzero with exact absolute margin `>1/50,000,000`. The complete positive list is:

```text
stable:   2475  (margin >3/20), 5003 (margin >1/64000)
unstable: [2475,5000,5003] (margin >3/100), [14008,14009,15003] (margin >1/25000)
saddles:  [14003,5003] (margin >1/8000), [14011,5003] (margin >1/8000)
```

Every other maximal face, vertex, and true edge has an exact negative witness component `<-1/50,000,000`. Row-star sinks are exactly `{2475,5003}`. Hence strict `(S,U,H)=(2,2,2)` and `S+U-H=2`. Exact mechanics sign fingerprint: `d6cd204552d3a13f24cddcdaec33955905ea913a0b176863feec5a66a1931937`; incidence fingerprint: `cd4f0025294887f1586fc4334f2797c2f38a6ae0c5e64b846eead14f72c4c9f9`. The linked source/verifier regenerates every witness from the generator rather than trusting these fingerprints.

## Cancellation achieved and residual forcing component

Rows `14000,14001,14013` are strictly inactive, so the parent full 17-gon U and parent true edge `(14001,14014)` are literally absent. Protected stable `2475` and protected U `[2475,5000,5003]` survive. The replacement packet is extra stable `5003`, extra U `[14008,14009,15003]`, and saddles `[14003,5003]`, `[14011,5003]`. This is not carrier transport, but no exact parent→endpoint death-before-birth chronology was certified; it is an exact post-cancellation endpoint, not a claimed joint event path.

The exact faces owned by `{5003,15000,14003,14011,14008,14009,14010,15003}` form a surface disk `(V,E,F)=(32,68,37)`, Euler 1, boundary

```text
[0,1,8,4,3,5,6,14,16,18,19,17,15,13,11,9,10,35,28,27,26,25,29,32,2]
```

Coning its 37 triangles to the exact own centroid gives a connected positive-volume tetrahedral 3-ball; radial-face adjacency is connected, every exact tetrahedron volume is positive, minimum `>1/100`, total `>25`. It contains extra stable face `5003`, return face `15000`, extra-U vertex P21, adjacent transfer P24, and both saddle P-edges `[6,7]`, `[22,30]`. This proves the complete connected terminal residual forcing volume, but not a parent-to-child chronology.

## Positive perturbation certificate

For independent `|a_x-1|,|a_y-1|≤1/536870912`, take `A=diag(a_x,a_y,1)`, `P→AP`, `H→A^{-T}H`. Incidence and exact centroid zero are covariant and volume remains positive. Directed rational interval arithmetic checks 202 sufficient inequalities over the full box; none contains zero, so every body remains strict `(2,2,2)`. Radius `2^-28` fails; `2^-29` passes.

## First genuinely new continuation

Two adjacent circuits must cross jointly: `C_U={14008,14009,14010,15003}` (crossing alone transfers U) and `C_R={14003,14011,5003,15000}` (contains sink 5003, almost-sink 15000, and both saddles; sequential crossing births replacement S/H). They communicate through `5003—14008—14009/15003` and face `[14008,14011,5003]`. The first untested topology is a shared-interior-face two-cell zipper with at least two return-page rows common to both cells. It must preserve `[2475,5000,5003]`, make `5003` nonstable without deactivating it, cross both saddle sheets and the U circuit before any replacement sign is positive, and retain at least five controls so three moments are dependent equations and two strict-timing controls remain. One-root fans, one-page chains, isolated caps, and independent stellar insertions repeat exhausted mechanisms.

## Reproducibility

- Exact source SHA-256 `fb1b08290cc52c34b2c30ed9c82eda64e62d07bd540108d3ce7a66214fc72a28`.
- Archive SHA-256 `210a895447a91d5479feeec7eb7e78614fa9eb6785390c2f5ef29f85058030fb`; manifest SHA-256 `2eed5df28d924a905625509e7b2be5a4a51f6f17e9d7369e3faffa51f252e1b3`.
- Clean extraction replay: `PARENT OBSTRUCTION VERIFIED`, `EXACT ENDPOINT VERIFIED`, `2D SHAPE BOX VERIFIED`, `MESH VERIFIED`, `FORCING VOLUME VERIFIED`, `ALL VERIFIERS PASSED`.
- Complete exact package (`Bright_Lynx_17_J56_exact_NONWINNER.zip`)
- Package checksum (`Bright_Lynx_17_J56_exact_NONWINNER.zip.sha256`)
- Full self-contained handoff with the reduced volume fraction and all 110 signed decision ledgers (`RESULT.md`)
- Exact source (`J56_BL17_exact_source.json`)
- Independent exact verifier (`verify_J56_BL17_exact.py`)
- One-command replay (`[internal-source-reference].sh`)
- Watertight OBJ (`J56_BL17_centered.obj`); watertight STL (`J56_BL17_centered.stl`)
