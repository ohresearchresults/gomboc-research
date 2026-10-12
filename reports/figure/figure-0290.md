# figure-0290

AI research report · 2026-09-04 UTC · [Export notes](../../catalog/coverage.md#text-records)

---

# Keen Quartz 89 — exact QCAD5-X3 ninth-vertex handoff

## Disposition

**EXACT NONWINNER. No finite homogeneous convex polyhedral Gömböc with strict own-centred `(S,U,H)=(1,1,0)` was constructed.**

The immutable parent `figure-0275`, SHA-256 `0f7bb810ecc8015121db8968b288d5d4087780b1e029e9a8c48babcfc5d412d2`, is the exact eight-vertex `(8,18,12)`, `(2,1,1)` QCAD body with stable faces `[0,H,C]`, `[C,AG,AD]`, unique unstable `C`, and saddle `[C,AD]`. :contentReference[oaicite:0]{index=0} This continuation does not beat that equilibrium count. It materially advances the topology by realizing and certifying the first two inclusion-minimal ninth-vertex repairs and closing the complete affine/SPD orbit of each frozen exact shape.

## Complete graph scope

After deleting QCAD2-ZAG forcing edges `[AB,AE]`, `[AB,H]`, `[AE,AG]`, exhaustively add one vertex `X` with degree at least three. Exact planarity, 3-connectivity, protected-face, and isomorphism checks give:

```text
60 valid repairs; degree counts 3:15, 4:22, 5:16, 6:6, 7:1;
15 inclusion-minimal repairs; 15 unlabeled minimal graph classes.
```

Minimal neighbor triples are `{0,C,AB}`, `{0,AB,AD}`, `{0,AB,AG}`, `{C,H,AB}`, `{C,Z,AB}`, `{C,AB,AE}`, `{H,Z,AB}`, `{H,AB,AD}`, `{H,AB,AE}`, `{H,AB,AG}`, `{Z,AB,AD}`, `{Z,AB,AE}`, `{Z,AB,AG}`, `{AB,AD,AE}`, `{AB,AE,AG}`. The first two are materialized here. This is complete graph-theoretic coverage of the one-X repair operation, not complete realization-space coverage.

## Exact endpoint A: `QCAD5-X3-0CAB`

Use labels `0,C,H,Z,AB,AD,AE,AG,X`. Let the 14 shape parameters, ordered as `(Zx,Zy,AEx,AEy,Hx,Hy,Cx,Cy,0x,0z,Xx,Xz,ABx,ABz)`, be

```text
-859464693151/1099511627776, 1212945364895/1099511627776,
-753151488253/1099511627776, 1389193621101/1099511627776,
-6857340161/549755813888, 226329478707/137438953472,
22958488807/34359738368, 902903142571/549755813888,
-93179717081/549755813888, -3555874037847/1099511627776,
776284470415/1099511627776, -226509186485/137438953472,
951926844567/1099511627776, -1266439325355/1099511627776.
```

Raw gauge:

```text
AD=(-1,0,0), AG=(1,0,0);
Z=(Zx,Zy,0), AE=(AEx,AEy,0), H=(Hx,Hy,0), C=(Cx,Cy,0);
0=(0x,0,0z), X=(Xx,0,Xz), AB=(ABx,0,ABz).
```

Its exact raw ordinary centroid is

```text
(470743288769976191926674628271970108305419187663/13627141010616208711086965229501768037440767918080,
29066733335885720630508756766597630689356814422177/54508564042464834844347860918007072149763071672320,
-9188301400413597951774362298625967443479058117241/10901712808492966968869572183601414429952614334464).
```

Set `p_i=A(r_i-c)` with

```text
A=[1998593832595/1099511627776,0,0;
203696973003/274877906944,449279345075/549755813888,0;
1975491978217/549755813888,2066369516903/1099511627776,370082451609/549755813888].
```

`det(A)=332306998946302645238316935522126625/332306998946228968225951765070086144>0`. Exact volume is

```text
1372850217938914900000608698700701418763711933400798021492605570773163125/441711766194596082395824375185729628956870974218904739530401550323154944,
```

and exact translated first moments are `(0,0,0)`.

Actual maximal faces:

```text
[H,C,0] [0,C,X] [AE,H,0] [AD,Z,0] [0,Z,AE]
[X,AB,AG,AD,0] [C,H,AE,Z,AD,AG] [AG,AB,C] [C,AB,X].
```

Actual true edges:

```text
[0,C] [0,H] [0,Z] [0,AD] [0,AE] [0,X]
[C,H] [C,AB] [C,AG] [C,X] [H,AE]
[Z,AD] [Z,AE] [AB,AG] [AB,X] [AD,AG].
```

Thus `(V,E,F)=(9,16,9)`, Euler two, complexity 32. Exact mechanics:

```text
stable [0,C,H], [AD,AG,C,H,AE,Z]; unstable C,AD;
saddles [0,X], [H,AE]; class (2,2,2).
```

Normalized strict margins are nonincidence `0.010977002947868577`, stable `0.06543589009305435`, nonstable clearance `0.019769642620622987`, unstable `0.8081716018250986`, nonunstable clearance `0.5827036013499325`, saddle `0.27248254491457446`, nonsaddle clearance `0.20403046381726012`.

Complete external-arrow forcing: primal edge `[0,AD]` forces an extra unstable endpoint disjoint from protected `C`; the polar channel dual to `[AD,AG]` forces an extra stable face disjoint from `[0,C,H]`. At each channel `sigma(a->b)+sigma(b->a)=||a-b||^2>0`, so this chamber has `U>=2` and `S>=2`.

Rigorous boxes: six affine controls at radius `2^-30`; all 14 shape plus six affine controls at radius `2^-22`, preserving exact own-centering, incidence, full mechanics, and forcing signs. For this frozen shape the complete affine/SPD orbit has 2,557 target tree-cotree systems, all excluded exactly: `869` unrestricted symmetric Gordan, `1656` SPD diagonal-dominance, `32` full Sylvester.

## Exact positive-volume source event

Removing `X` from the same shape gives exact source `(8,14,8)`, `(2,2,2)`, with saddles `[0,AB]`, `[H,AE]`. At `X0=(0+AB)/2`, one connected edge-star split removes faces `[0,C,AB]`, `[0,AB,AD,AG]` and adds `[0,C,X]`, `[AB,C,X]`, `[0,AB,AD,AG,X]` along boundary `[0,C,AB,AG,AD]`. The added tetrahedron `[X,0,C,AB]` has exact positive volume

```text
197705212846491475962246880986428311/3987683987354747618711421180841033728.
```

Exact checkpoints `1/1024,1/256,1/64,1/16,1/4,1/2,1` are all strict `(2,2,2)`: the old saddle dies only after a replacement saddle is already strict. This is exact checkpoint chronology, not exhaustive root isolation over the entire chord.

## Exact endpoint B: `QCAD5-X3-0ABAD`

Order the 14 parameters as `(Zx,Zy,AEx,AEy,Hx,Hy,Cx,Cy,ABx,ABz,Xx,Xz,alpha,beta)` and use

```text
-524571181617/549755813888, 629905743707/1099511627776,
-474771716081/1099511627776, 1887128170401/1099511627776,
-121082318165/549755813888, 548758398239/274877906944,
691243505681/1099511627776, 2255470745395/1099511627776,
1096895574921/549755813888, -1683114448079/1099511627776,
-166562036793/1099511627776, -1465215611815/549755813888,
-58060394729/274877906944, 1057200799721/1099511627776.
```

Set `AD=(-1,0,0)`, `AG=(1,0,0)`, put `Z,AE,H,C` in `z=0`, put `AB,X` in `y=0`, and set

```text
0=C+alpha(AB-C)+beta(X-C),
```

so `[0,C,AB,X]` is exactly coplanar. Its raw centroid is

```text
(12267654696558901137280517706775224770925833269469417188454967946111045589/48758848985562638956608926629069464072444789216677410857888243837111894016,
60762396583850599280395943369060075081308218785596093957722314972329251989/97517697971125277913217853258138928144889578433354821715776487674223788032,
-40591062626013136676164935813358155232395782188260122052200835695915605829/48758848985562638956608926629069464072444789216677410857888243837111894016).
```

Apply

```text
A=[960021730309/1099511627776,0,0;
798535752331/1099511627776,33061399311/68719476736,0;
148313901855/549755813888,408479487635/549755813888,2617442817465/1099511627776].
```

Exact volume is

```text
558447098088949860397275492952851955039795510571983168672226887020283403844195390885/121416805764108066932466369176469931665150427440758720078238275608681517825325531136,
```

with exact centred first moments `(0,0,0)`.

Maximal faces:

```text
[H,C,0] [0,C,AB,X] [AE,H,0] [AD,Z,0] [0,Z,AE]
[X,AD,0] [C,H,AE,Z,AD,AG] [AG,AB,C] [AB,AG,AD,X].
```

True edges:

```text
[0,C] [0,H] [0,Z] [0,AD] [0,AE] [0,X]
[C,H] [C,AB] [C,AG] [H,AE] [Z,AD] [Z,AE]
[AB,AG] [AB,X] [AD,AG] [AD,X].
```

Exact mechanics:

```text
stable [0,C,H], [AB,AG,AD,X]; unstable C,X;
saddles [C,AB], [AD,X]; class (2,2,2).
```

Margins: nonincidence `0.01182222905388998`, stable `0.02935674293973762`, nonstable `0.014464136510692885`, unstable `0.5086320135289163`, nonunstable `0.09271159960917703`, saddle `0.2290080570530498`, nonsaddle `0.06388932237918471`.

Forcing: primal `[0,X]` forces a second unstable endpoint; polar channel dual to `[AB,AG]` forces a second stable face. The full six-affine box has radius `2^-24`; the full 20-dimensional shape-and-affine box has radius `2^-18`. The frozen-shape affine/SPD orbit has 2,818 target systems, all exactly excluded: `794` Gordan, `2020` diagonal-dominance, `4` full Sylvester.

## Exact scope versus numerical evidence

Exact claims are limited to the two rational endpoints, their full cone ledgers, their positive interval boxes, the primary positive-volume transition, the complete 60/15/15 graph atlas, and the two complete frozen-shape affine-orbit partitions. No global impossibility for either graph, for all nine-vertex bodies, or for the Gömböc problem is claimed.

Numerical discovery only: `2,048,000` states for each graph, `4,096,000` total; `44,932` and `123,863` topology-valid states; `10,555` and `7,504` states retaining the intended stable face and unstable vertex; no `(1,1,0)`, `(2,1,1)`, or `(1,2,1)` hit. These nonhits exclude zero regions exactly. A stale target-face index in an early `0ABAD` experiment was detected and discarded; only corrected counts are retained.

## First unrepresented continuation

The first uninstantiated minimal graph is `QCAD5-X3-0ABAG`, with `N(X)={0,AB,AG}` and `(V,E,F)=(9,16,9)`. Its graph faces are

```text
[0,AD,Z] [0,AE,H] [0,AE,Z] [0,C,H] [0,C,AB,X]
[AB,AG,X] [AB,C,AG] [0,AD,AG,X] [AD,AG,C,H,AE,Z].
```

A continuation should choose a full gauge for its hexagon and two nontriangular side faces, compute the exact ordinary centroid before mechanics, preserve `[0,C,H]` and `C`, preassign a nonpositive external arrow on every nonprotected primal and polar channel, audit all 16 true edges through all four cone components, certify a full shape-and-affine box, and partition the entire frozen-shape SPD orbit if nonwinning. Thirteen minimal one-X types remain. Only after these are materially tested should the branch escalate to a coupled two-X/ten-vertex bridge.

## Independent verification and artifacts

Independent reconstruction reads exact V-data, enumerates supporting triples, reconstructs maximal faces and true edges, recomputes exact ordinary volume and centroid, audits every face, vertex, and four-component edge cone, rebuilds primal/polar arrow censuses, and checks OBJ/STL parity. Display diagonals of nonsimplicial faces are not treated as true edges. The clean replay ends with `ALL_KQ89_QCAD5_X3_EXACT_CHECKS_PASS`; the SHA manifest covers 166 files.

- [Complete exact archive](sandbox:/mnt/data/Keen_Quartz_89_QCAD5_X3_exact_NONWINNER.zip) — SHA-256 `81629c2acc2f02793d4d92be04479b616411eaf423ec098fc3ef6ee3dc9166f9`.
- [Archive hash](sandbox:/mnt/data/Keen_Quartz_89_QCAD5_X3_exact_NONWINNER.zip.sha256).
- [Full handoff](sandbox:/mnt/data/Keen_Quartz_89_QCAD5_X3_exact_NONWINNER/RESEARCH_HANDOFF.md).
- [README](sandbox:/mnt/data/Keen_Quartz_89_QCAD5_X3_exact_NONWINNER/README.md).
- [Result summary](sandbox:/mnt/data/Keen_Quartz_89_QCAD5_X3_exact_NONWINNER/result_summary.json).
- [Continuation atlas](sandbox:/mnt/data/Keen_Quartz_89_QCAD5_X3_exact_NONWINNER/next_unclassified_topology.json).
- [Replay script](sandbox:/mnt/data/Keen_Quartz_89_QCAD5_X3_exact_NONWINNER/RUN_ALL.sh) and [successful transcript](sandbox:/mnt/data/Keen_Quartz_89_QCAD5_X3_exact_NONWINNER/CURRENT_SESSION_REVERIFY.log).
- [Manifest](sandbox:/mnt/data/Keen_Quartz_89_QCAD5_X3_exact_NONWINNER/manifest.json) and [SHA list](sandbox:/mnt/data/Keen_Quartz_89_QCAD5_X3_exact_NONWINNER/SHA256SUMS.txt).
- Primary: [V-data](sandbox:/mnt/data/Keen_Quartz_89_QCAD5_X3_exact_NONWINNER/vertices_centered_exact.csv), [H-data](sandbox:/mnt/data/Keen_Quartz_89_QCAD5_X3_exact_NONWINNER/H_irredundant.json), [faces](sandbox:/mnt/data/Keen_Quartz_89_QCAD5_X3_exact_NONWINNER/face_cycles.json), [true edges](sandbox:/mnt/data/Keen_Quartz_89_QCAD5_X3_exact_NONWINNER/true_edges.csv), [OBJ](sandbox:/mnt/data/Keen_Quartz_89_QCAD5_X3_exact_NONWINNER/body.obj), [STL](sandbox:/mnt/data/Keen_Quartz_89_QCAD5_X3_exact_NONWINNER/body.stl).
- Second: [V-data](sandbox:/mnt/data/Keen_Quartz_89_QCAD5_X3_exact_NONWINNER/qcad5_x3_0abad_endpoint/vertices_centered_exact.csv), [H-data](sandbox:/mnt/data/Keen_Quartz_89_QCAD5_X3_exact_NONWINNER/qcad5_x3_0abad_endpoint/H_irredundant.json), [faces](sandbox:/mnt/data/Keen_Quartz_89_QCAD5_X3_exact_NONWINNER/qcad5_x3_0abad_endpoint/face_cycles.json), [true edges](sandbox:/mnt/data/Keen_Quartz_89_QCAD5_X3_exact_NONWINNER/qcad5_x3_0abad_endpoint/true_edges.csv), [OBJ](sandbox:/mnt/data/Keen_Quartz_89_QCAD5_X3_exact_NONWINNER/qcad5_x3_0abad_endpoint/body.obj), [STL](sandbox:/mnt/data/Keen_Quartz_89_QCAD5_X3_exact_NONWINNER/qcad5_x3_0abad_endpoint/body.stl).

## Bottom line

Two of the 15 graph-minimal ninth-vertex QCAD repairs are now exact open bodies, but both recreate a primal and a dual forcing channel and remain `(2,2,2)`. Their complete fixed-shape affine orbits are rigorously closed. The first literal nonrepeating continuation is `QCAD5-X3-0ABAG`, not another affine polish of either completed shape.
