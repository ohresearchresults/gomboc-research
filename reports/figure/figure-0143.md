# figure-0143

Historical AI scientific report · saved 2026-08-28 UTC. Claims below retain their original status and have not all been independently checked. The current retained construction is C622; the C<500 search remains open.

---

# M42 volumetric successor: literal recovered outcome

**Verdict: NONWINNER.** No strict own-centroid `(S,U,H)=(1,1,0)` homogeneous convex polyhedron was produced. The corrected finite-thickness endpoint is a strict open own-centred `(2,2,2)` polyhedron.

The journal said the preceding immutable result exposed only links and was mathematically unresolved. :contentReference[oaicite:0]{index=0} Opening those bytes shows the original bundle contained no endpoint: its health file marks every candidate/audit/mesh absent and its log fails on missing `m42_points_exact.json` and `successor_generator.json`. That wrapper was a pipeline failure, not a hidden winner or geometric negative result. This turn recovered the exact predecessor and prototype, disproved the prototype’s false `(50,130,82)` active-hull assertion, and rebuilt the actual endpoint exactly.

## Exact endpoint and generator

- 104 construction rows on the `10^-12` lattice; actual `(V,E,F)=(46,118,74)`, complexity `236`;
- active rows: `0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,49,54,58,59,65,66,67,69,70,71,72,73,80,81,84,85,86,88,90,91,92,93,95,96,97,98,101,102,103`;
- strict class `(2,2,2)`;
- rows `60,62,63,64` are the four prototype rows proved interior by exhaustive enumeration of all `C(104,3)=182104` supporting triples.

Rows `0..94` are literal in `predecessor_rows_0_94.csv`. With

```text
Cpre=(31583290850654892631932549247646225220082395155411/118640848958801736217872408048013686308000000000000,
-6688580900932650473570308945472520977944616049267/7415053059925108513617025503000855394250000000000,
-19234811323075247274675565450830139622653009224807/59320424479400868108936204024006843154000000000000),
```

rows `95..101` are nearest-lattice values of `Cpre+(1001/1000)(qold-Cpre)` for olds `82,83,87,94,76,77,89`. Added rows:

```text
95 (1262197258112,-3047241515668,-561736699754)/10^12 active=1 successor_of_82
96 (1401548579786,-2926120159174,-390327095869)/10^12 active=1 successor_of_83
97 (1732807623435,-1564078233118,-136491611186)/10^12 active=1 successor_of_87
98 (-1022778114781,-1214795291328,-236125670811)/10^12 active=1 successor_of_94
99 (706718609248,-2127490276263,-831079094784)/10^12 active=0 successor_of_76
100 (640629309802,-1116694327777,-759932876804)/10^12 active=0 successor_of_77
101 (10225794846,-417901682517,-798427472984)/10^12 active=1 successor_of_89
102 (1294762429486,-2860311004007,-829489574742)/10^12 active=1 finite_thickness_pair
103 (1560762338063,-2379346194538,-632965199353)/10^12 active=1 finite_thickness_pair
```

`generate_corrected_endpoint.py` plus the predecessor CSV deterministically regenerates all exact H/V/E data.

## Exact mass

`V=10258852295558131125580956459745853517/2000000000000000000000000000000000000` (`5.1294261477790659`).

Uncentred first moments: `2314811237572143946830995122037285303732838241091/1500000000000000000000000000000000000000000000000`, `-19212154159446592326738154512378393845062622990877/4000000000000000000000000000000000000000000000000`, `-13678774646141453974331462209434567910316924030149/8000000000000000000000000000000000000000000000000`.

Uncentred volume centroid: `2314811237572143946830995122037285303732838241091/7694139221668598344185717344809390137750000000000`, `-6404051386482197442246051504126131281687540996959/6839234863705420750387304306497235678000000000000`, `-13678774646141453974331462209434567910316924030149/41035409182232524502323825838983414068000000000000`. After subtracting it, all three first moments are exactly zero.

## Complete actual incidence

Maximal-face cycles:

```text
0:12,13,14,15,16,0,1,2,3,4,5,6,7,8,9,10,11
1:54,1,0
2:72,0,16
3:72,54,0
4:1,88,2
5:54,88,1
6:2,88,3
7:3,88,4
8:97,5,4
9:97,4,88
10:6,5,59
11:5,103,59
12:103,5,97
13:7,6,81
14:6,59,58
15:6,58,81
16:7,81,8
17:8,81,9
18:9,81,10
19:10,91,11
20:81,101,10
21:101,91,10
22:11,91,12
23:13,12,98
24:91,93,12
25:98,12,93
26:13,73,14
27:73,13,98
28:14,72,15
29:14,73,72
30:15,72,16
31:49,92,71
32:98,49,71
33:98,92,49
34:54,70,69
35:54,69,88
36:71,70,54
37:72,71,54
38:59,80,58
39:58,80,101
40:81,58,101
41:59,103,80
42:65,66,92
43:65,102,66
44:102,65,92
45:66,67,92
46:67,66,102
47:71,67,70
48:70,67,95
49:92,67,71
50:67,102,95
51:70,95,69
52:69,84,86
53:69,96,84
54:69,86,88
55:69,95,96
56:72,98,71
57:73,98,72
58:80,102,101
59:103,102,80
60:84,85,86
61:84,96,85
62:85,96,86
63:86,97,88
64:86,96,97
65:101,90,91
66:90,102,91
67:101,102,90
68:91,92,93
69:91,102,92
70:98,93,92
71:95,102,96
72:96,103,97
73:96,102,103
```

True edges:

```text
(0,1) (0,16) (0,54) (0,72) (1,2) (1,54) (1,88) (2,3) (2,88) (3,4) (3,88) (4,5)
(4,88) (4,97) (5,6) (5,59) (5,97) (5,103) (6,7) (6,58) (6,59) (6,81) (7,8) (7,81)
(8,9) (8,81) (9,10) (9,81) (10,11) (10,81) (10,91) (10,101) (11,12) (11,91) (12,13) (12,91)
(12,93) (12,98) (13,14) (13,73) (13,98) (14,15) (14,72) (14,73) (15,16) (15,72) (16,72) (49,71)
(49,92) (49,98) (54,69) (54,70) (54,71) (54,72) (54,88) (58,59) (58,80) (58,81) (58,101) (59,80)
(59,103) (65,66) (65,92) (65,102) (66,67) (66,92) (66,102) (67,70) (67,71) (67,92) (67,95) (67,102)
(69,70) (69,84) (69,86) (69,88) (69,95) (69,96) (70,71) (70,95) (71,72) (71,92) (71,98) (72,73)
(72,98) (73,98) (80,101) (80,102) (80,103) (81,101) (84,85) (84,86) (84,96) (85,86) (85,96) (86,88)
(86,96) (86,97) (88,97) (90,91) (90,101) (90,102) (91,92) (91,93) (91,101) (91,102) (92,93) (92,98)
(92,102) (93,98) (95,96) (95,102) (96,97) (96,102) (96,103) (97,103) (101,102) (102,103)
```

The exact primitive-normal H table, exact centred V table, face decisions, vertex supports, incident face IDs and every edge’s exact `t,1-t,beta1,beta2` are in the checksummed bundle.

## Full-feature audit and margins

- stable: protected 17-gon face `0`, margin `0.015121524274752256`; extra face `58=[80,102,101]`, margin `0.04909493371249872`;
- unstable: target `8`, margin `0.37802719681142727`; extra `95`, margin `0.2739478223813484`;
- saddles: `(5,97)` margin `0.35408136326294243`; `(49,98)` margin `0.2766227654502538`;
- minimum topology distance `1.582579507760321e-4`; inactive distance `4.7055896301767894e-4`; nonstable exclusion `1.3233031346678175e-4`; nonunstable exclusion `5.784861297797118e-2`; nonsaddle exclusion `2.0951424923644365e-3`.

A coordinatewise box `±10^-13` on 87 independent active coordinates preserves all incidence, inactive rows, class `(2,2,2)`, inherited-feature deletion and obstruction. Directed lower bounds: facet determinant `1.5696582603277887e-5`, stable component `3.957527947383286e-4`, nonstable witness `1.67362832414578e-5`, unstable support `0.1608564531089677`, nonunstable witness `0.03655865852522944`, saddle component `0.3548134811658394`, nonsaddle witness `2.0778668474087817e-5`, obstruction/target support `0.223456501868332`.

## Volumetric change and obstruction

Old rows `82,83,87,94,76,77,89` are inactive; old edge `(82,83)`, saddles `(5,87),(49,94)`, and face `{76,77,89}` are absent. Rows `102,103` form a true edge. Their joint star touches terminal `[67,95,96]`, right `[5,97]`, north `[80,90,91,101]`, left `[92]`. Fifteen incident triangles cone to the exact centroid as a connected tetrahedral complex; the minimum exact cell determinant is

`8364967107832646872843087559124477125801497362776894195467678133297066863/123106227546697573506971477516950242204000000000000000000000000000000000000`.

Thus this is genuinely finite-thickness and 3-D, not a surface subdivision.

The old obstruction transfers to true edge `(95,96)`. Every nonmutual endpoint support is positive and

`sigma(95→96)=6600810374233970890195561135063815089843124855810304917827099/41035409182232524502323825838983414068000000000000000000000000>0`,
`sigma(96→95)=-3996275465982619183879196192421122316541828756589435011036583/41035409182232524502323825838983414068000000000000000000000000<0`,
`sum=||x96-x95||²=63470426155249865227537/1000000000000000000000000>0`.

Therefore one endpoint remains unstable throughout the certified incidence/external-sign cell; vertex `8` is independently unstable, so `U>=2`.

## Exact path and first escape test

The predecessor-to-endpoint path has 28 strict exact cells and these 27 isolated walls; every cell is `(2,2,2)` and retains the externally positive edge `(95,96)`:

```text
1 1-to-3 vertex activation [62, 65, 99, 102] enter 102
2 2-to-2 bistellar boundary flip [62, 63, 65, 102]
3 2-to-2 bistellar boundary flip [62, 80, 99, 102]
4 1-to-3 vertex activation [62, 96, 97, 103] enter 103
5 2-to-2 bistellar boundary flip [62, 95, 96, 103]
6 2-to-2 bistellar boundary flip [63, 64, 65, 102]
7 2-to-2 bistellar boundary flip [60, 62, 97, 103]
8 2-to-2 bistellar boundary flip [60, 62, 80, 103]
9 2-to-2 bistellar boundary flip [62, 63, 95, 103]
10 2-to-2 bistellar boundary flip [63, 64, 95, 102]
11 2-to-2 bistellar boundary flip [62, 63, 102, 103]
12 3-to-1 vertex deactivation [64, 65, 95, 102] leave 64
13 3-to-1 vertex deactivation [63, 95, 102, 103] leave 63
14 2-to-2 bistellar boundary flip [59, 60, 80, 103]
15 3-to-1 vertex deactivation [62, 80, 102, 103] leave 62
16 2-to-2 bistellar boundary flip [5, 59, 60, 103]
17 3-to-1 vertex deactivation [5, 60, 97, 103] leave 60
18 2-to-2 bistellar boundary flip [80, 99, 100, 102]
19 2-to-2 bistellar boundary flip [95, 96, 102, 103]
20 2-to-2 bistellar boundary flip [65, 91, 99, 102]
21 2-to-2 bistellar boundary flip [99, 100, 101, 102]
22 2-to-2 bistellar boundary flip [90, 99, 101, 102]
23 2-to-2 bistellar boundary flip [65, 66, 95, 102]
24 3-to-1 vertex deactivation [90, 91, 99, 102] leave 99
25 2-to-2 bistellar boundary flip [65, 91, 92, 102]
26 3-to-1 vertex deactivation [80, 100, 101, 102] leave 100
27 2-to-2 bistellar boundary flip [66, 67, 95, 102]
```

The path activates `102,103` and later deactivates `64,63,62,60,99,100`; the extra stable face migrates `[100,99,101]→[100,102,101]→[80,102,101]` without changing Morse counts.

A same-turn exact simultaneous crossing moved `95,97,101,49` through planes `(69,96,102)`, `(4,5,103)`, `(80,90,102)`, `(71,92,98)` at `alpha=1001/1000`. It removes the selected edge/stable/saddles, but rows `82,87,89` reactivate and the endpoint remains `(2,2,2)`: stable `[80,102,89]`, unstable `8,82`, saddles `(5,87),(71,98)`. New true edge `(82,96)` is externally positive with `A+B=63152896318849033150741/10^24>0`; hence `U>=2` again. Local independent crossings transfer the block.

## Sharp next cell

The smallest nonduplicative continuation is a third transverse closure band / finite-thickness `2×2` crossrail around spine `(102,103)`. It must simultaneously deactivate old/replacement packets `{82,95}`, `{87,97}`, `{89,101}`, `{49,98}`; destroy both maximum channels `(95,96)` and `(82,96)`; cross terminal `{69,95,96,102}`, right `{4,5,97,103}`, north `{80,90,101,102}`, left `{49,71,92,98}` while old rows stay inactive; introduce a new transverse true edge, naturally `(104,105)`, whose stars share actual centroid-fan tetrahedra; solve all three moments as hard dependent equations; and rebuild every face/edge/full cone after each wall. Serial rails and surface-only refinements are subsumed.

## Independent verification and mesh

- standard-library clean-room exact verifier: exhaustive V→H, H→V, mass, all face/vertex/four-component edge cones, obstruction and finite-thickness complex — **PASS**;
- directed `±10^-13` interval verifier — **PASS**;
- 28-cell/27-wall exact circuit verifier — **PASS**;
- matching watertight OBJ/STL: 46 vertices, 88 triangles, Euler `2`, volume `5.1294261477790641`, COM within `5.1e-17` — **PASS**. The 14 mesh-only edges are triangulation diagonals of the 17-gon.

## Artifacts and hashes

- archive SHA-256 `3a274bb29a24a762482e904dcb764570a2145f115f1e19d880bdc93af8761440`;
- full handoff `f6b989d31be16c5906c6b9ad6d667b30756de2a1d274a9fed3ed75a0fa7b7698`; certificate `8feff84052ff956b5244a5541a950b6dceb9da41f179a7d51b14e8efa57eeb81`;
- generator `9c908d350afee5687ce9e5baafa25a0d8df546331b517b59c60d1a6277630083`; centred V `a52728644dad48aa2dea5ff7ccf613dfe9bd3dda597b32db2f6f6b8aa7e3bf7d`; centred H `8948c634ac5793828c63fe89257e5c1bc907fec9cc5bf5d09b1cf095c7bacc7c`;
- face audit `833ac33bfd115b6e3089c6fcfb280287c9cc466ecc8067a95e73091ef11e24a8`; vertex audit `0b005edc9938526352f647ad41f79459300731415a442a3e38b1e0a0a2eb36f1`; edge audit `507e2021a8c893ddbf426603450b5a233632c5c6a68735457e3b483cbd4e4210`; circuit atlas `79ad60ff17db36279cfeeb081635d023bbd2cc7782dde71678fb8887249af98b`;
- OBJ `6578248e11cad021fb3215bf666ec03dfa029a156780b7d305ec98ddce9da6ff`; STL `fc9a82dd93eeb10de578e592e76a4a29afc1dc33ccaecc85d7cd5f7a26c4426e`.

[Full self-contained handoff with all 104 rows and all 74 exact H inequalities](sandbox:/mnt/data/m42_volumetric_recovered_exact/research_handoff.md)

[Corrected archive](sandbox:/mnt/data/m42_volumetric_recovered_exact.zip) · [archive digest](sandbox:/mnt/data/m42_volumetric_recovered_exact.zip.sha256) · [per-file hashes](sandbox:/mnt/data/m42_volumetric_recovered_exact/SHA256SUMS.txt)

[Generator](sandbox:/mnt/data/m42_volumetric_recovered_exact/generate_corrected_endpoint.py) · [certificate](sandbox:/mnt/data/m42_volumetric_recovered_exact/certificate.json) · [independent verifier](sandbox:/mnt/data/m42_volumetric_recovered_exact/verify_exact_cleanroom.py) · [interval verifier](sandbox:/mnt/data/m42_volumetric_recovered_exact/verify_interval.py) · [circuit atlas](sandbox:/mnt/data/m42_volumetric_recovered_exact/circuit_atlas.json) · [transcript](sandbox:/mnt/data/m42_volumetric_recovered_exact/RUN_ALL_VERIFIERS.txt) · [OBJ](sandbox:/mnt/data/m42_volumetric_recovered_exact/body.obj) · [STL](sandbox:/mnt/data/m42_volumetric_recovered_exact/body.stl)

The negative theorem is cell-local, not global: the third-band crossrail remains an open M42 frontier.
