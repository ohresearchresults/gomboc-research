# figure-0232

Historical AI scientific report · saved 2026-09-02 UTC. Claims below retain their original status and have not all been independently checked. The current retained construction is C622; the C<500 search remains open.

---

# Vivid Atlas 32 — P9-XG9 four-row closed-cell determination

## Verdict

**EXACT FINITE NONWINNER.** No homogeneous convex polyhedral Gömböc was obtained. The acceptance target remains a materialized finite uniform-density body at its own exact volume centroid with strict `(S,U,H)=(1,1,0)`, complete actual H/V/E and full-cone mechanics, independent verification, and matching OBJ/STL; wall points, auxiliary centres, near-solutions, smooth objects, and unexpanded generators do not qualify. :contentReference[oaicite:0]{index=0}

The requested first closed four-row topology beyond P9-XG8 was realized exactly. It deletes the entire inherited XG8 packet in one positive-volume communicating event, but creates a distinct replacement packet and therefore remains own-centred `(2,2,2)`.

## Exact construction and provenance

```text
parent P9-XG8 archive SHA-256: c5387e767c7cd7a26979caab789c5e21be8832f7dcf1560af6d39e3b9cdc53ab
embedded parent exact-data SHA-256: eb2629722bdf5285050bee9b789bc1ac4aa8b1d2204976cf95d1b4ddf04c5bc8
```

Old rows `SC1,SA5,S102,X3` are coupled to a dyadic pre-event cell and four new rows `W0..W3` are inserted simultaneously. All other XG8 rows are retained exactly.

For `P_raw={x:q_i·x≤1}`, let `c` be its exact ordinary-volume centroid. The physical body is `P=P_raw-c`, with exact own-centred supports `H_i=q_i/(1-q_i·c)`.

```text
T27   (-7125242734162057/140737488355328, 265769074670437/35184372088832, -63255401657691/70368744177664) [active]
TR    (-892363419092795/281474976710656, -235941426090029/140737488355328, -528766574131575/140737488355328) [active]
SU    (-544131479513675/140737488355328, -96790958131853/35184372088832, 118288508214145/140737488355328) [active]
SC1   (-119/64, -477/64, -239/64) [active]
SA5   (-379/64, -497/64, -456/64) [active]
S102  (-1596/64, 1134/64, 536/64) [active]
G     (1595031506620615/70368744177664, 69636553284589/35184372088832, 72284311426759/70368744177664) [active]
M     (1529073462/16777216, -268643187/16777216, 58067364/16777216) [inactive]
N     (1529492441/16777216, -268486070/16777216, 58329226/16777216) [inactive]
X0    (1919121502/16777216, -309962234/16777216, 99003968/16777216) [inactive]
X1    (1848158428/16777216, -383623901/16777216, 89362767/16777216) [inactive]
X2    (2073127498/16777216, -414482154/16777216, 17864224/16777216) [inactive]
X3    (7703/64, -1219/64, 90/64) [inactive]
Y0    (1763461327/16777216, -218740469/16777216, 159462489/16777216) [inactive]
Y1    (1040743361/8388608, -206745211/8388608, -2371163/16777216) [inactive]
Z0    (69965/256, -12012/256, 5329/256) [inactive]
Z1    (77082/256, -17837/256, -1141/256) [inactive]
Z2    (48907/256, -14806/256, -5116/256) [inactive]
W0    (18171/64, -2668/64, 2193/64) [active]
W1    (20893/64, -4831/64, -278/64) [active]
W2    (10115/64, -3682/64, -1811/64) [active]
W3    (16533/64, -3122/64, -390/64) [active]
```

Active irredundant rows are

```text
T27, TR, SU, SC1, SA5, S102, G, W0, W1, W2, W3
```

Strict inactive supplied rows are

```text
M, N, X0, X1, X2, X3, Y0, Y1, Z0, Z1, Z2
```

## Exact predecessor and successor incidence

The exact XG8 predecessor and the coupled pre-event both reconstruct as

```text
Q:(V,E,F)=(11,27,18), P:(V,E,F)=(18,27,11), C=54, class=(2,2,2).
```

The coupled pre-event residual packet is stable `T27,Z2`, unstable `T27/SU/Z0` and `TR/S102/G`, and saddles `SA5-Z2`,`S102-Z0`. Its actual facets are

```text
 0 T27/TR/SA5
 1 T27/TR/S102
 2 T27/SU/SC1
 3 T27/SU/Z0
 4 T27/SC1/SA5
 5 T27/S102/Z0
 6 TR/SA5/Z2
 7 TR/S102/G
 8 TR/G/Z2
 9 SU/SC1/Z0
10 SC1/SA5/Z2
11 SC1/Z0/Z2
12 S102/G/X3
13 S102/X3/Z0
14 G/X3/Z2
15 X3/Z0/Z1
16 X3/Z1/Z2
17 Z0/Z1/Z2
```

The successor has 22 supplied rows, 11 active rows, and

```text
Q:(V,E,F)=(11, 27, 18)
P:(V,E,F)=(18, 27, 11)
C=54
Euler: 11-27+18=2 and 18-27+11=2.
```

All `C(22,3)=1540` candidate triples were solved exactly. The 18 actual facets/primal vertices are

```text
 0 T27/TR/S102
 1 T27/TR/W2
 2 T27/SU/SC1
 3 T27/SU/W0
 4 T27/SC1/SA5
 5 T27/SA5/W2
 6 T27/S102/W0
 7 TR/S102/G
 8 TR/G/W2
 9 SU/SC1/W0
10 SC1/SA5/W2
11 SC1/W0/W2
12 S102/G/W3
13 S102/W0/W3
14 G/W2/W3
15 W0/W1/W2
16 W0/W1/W3
17 W1/W2/W3
```

All 27 true edges are

```text
T27-TR  T27-SU  T27-SC1  T27-SA5
T27-S102  T27-W0  T27-W2  TR-S102
TR-G  TR-W2  SU-SC1  SU-W0
SC1-SA5  SC1-W0  SC1-W2  SA5-W2
S102-G  S102-W0  S102-W3  G-W2
G-W3  W0-W1  W0-W2  W0-W3
W1-W2  W1-W3  W2-W3
```

All 11 maximal-face cycles are

```text
T27   0 1 5 4 2 3 6
TR    0 7 8 1
SU    2 9 3
SC1   2 4 10 11 9
SA5   4 5 10
S102  0 6 13 12 7
G     7 12 14 8
W0    3 9 11 15 16 13 6
W1    15 17 16
W2    1 8 14 17 15 11 10 5
W3    12 13 16 17 14
```

The exact minimum all-supplied nonincidence slack is `16137841935424267658541925295173673059967195/257569858759915533335957887011712033584316416` (decimal `0.06265423296468309`). A strict positive-spanning certificate on `T27,TR,SU,G` proves boundedness. The minimum projective denominator is `0.44545984659345145>0`.

## Exact volume centroid

The exact ordinary volume is

```text
805519821792020045727181951811796659245456494065628260684974395401563177450565803616088281747128056988189194098591189544032965118873999574246350582612004205030064201202622114606843837391487144811140894808155773350798484773297798837305014939575606705192154816990570047287491657996228756750053157173790163234344116579865122861257416008081808416256653754264576/809328907210637713063665646208890845565317889478950950207413530461617496579237286656600614497617324495756526535969417694483268192677548744034995158593065114610291161073331965046265707583470666825124459308604953407174347548118500366261194054035213855569248557791761761222691574142071555199659324947802830035528639995837398387023893218709829225449433629834698525
```

(decimal `0.0009952935260501869`). Exact raw first moments and centroid are fully expanded in `exact_mass_centroid.json`; decimal values are

```text
M=[-5.127110319961835e-06, 3.205856162686239e-05, -5.584243230956811e-05]
c=[-0.005151355038255624, 0.032210157895918905, -0.05610649607174508]
```

The exact translated first moments are

```text
['0/1', '0/1', '0/1']
```

and the clean verifier independently proves `M_i-V*c_i=0` for all three coordinates.

## Positive-volume closed event and genuine deletion

The coupled pre-event and successor share four unchanged facets. The removed and added patches have the same boundary graph: two quadrilateral cycles sharing `T27`, namely `[['T27', 'TR', 'G', 'S102'], ['T27', 'SU', 'SC1', 'SA5']]`.

Removed patch:

```text
G/S102/X3
G/TR/Z2
G/X3/Z2
S102/T27/Z0
S102/X3/Z0
SA5/SC1/Z2
SA5/T27/TR
SA5/TR/Z2
SC1/SU/Z0
SC1/Z0/Z2
SU/T27/Z0
X3/Z0/Z1
X3/Z1/Z2
Z0/Z1/Z2
```

Added patch:

```text
G/S102/W3
G/TR/W2
G/W2/W3
S102/T27/W0
S102/W0/W3
SA5/SC1/W2
SA5/T27/W2
SC1/SU/W0
SC1/W0/W2
SU/T27/W0
T27/TR/W2
W0/W1/W2
W0/W1/W3
W1/W2/W3
```

Exact Q volumes are

```text
pre  = 101706470854765471220091786073340845/2535301200456458802993406410752
post = 376281899771522014908207349001343791/3802951800684688204490109616128
difference = 447444386978747616156139339782665047/7605903601369376408980219232256>0
```

The four new rows form a closed tetrahedron of exact volume `109651913/6144`. Three positive radial tetrahedra have exact volumes

```text
['ORIGIN', 'W0', 'W1', 'W2'] : 7305553991/786432
['ORIGIN', 'W0', 'W1', 'W3'] : 13699984729/524288
['ORIGIN', 'W1', 'W2', 'W3'] : 29318648809/1572864
```

and total `42514855489/786432`. They communicate through two independent interior pages around radial spine `[0,W1]`, plus a cap-pair page; every opposite-side determinant is exact and strictly signed.

`Z0,Z1,Z2` are strict convex combinations of `W0..W3`, with minimum barycentric weights `0.0894373762936254`, `0.05741243913592278`, and `0.059089524684552246`. Consequently `Z1-Z2`, stable `Z2`, source `T27/SU/Z0`, and saddles `SA5-Z2`,`S102-Z0` are absent from the actual successor hull and mechanics. The later forcing edge has different endpoints and different link, so this is deletion, not renaming.

## Exhaustive full-cone mechanics

At its exact own centroid the successor is

```text
(S,U,H)=[2, 2, 2]
stable:   ['T27', 'W2']
unstable: [['T27', 'SU', 'W0'], ['TR', 'S102', 'G']]
saddles:  [['SA5', 'W2'], ['S102', 'W0']]
```

Every actual maximal face, every actual vertex full normal cone, and all four components `t,1-t,alpha,beta` of every true-edge cone were checked exactly. Decimal category minima are

```text
{
  "stable_positive": 809.2601172965665,
  "face_exclusion": 44.09964728509129,
  "unstable_positive": 0.016366664411210433,
  "vertex_exclusion": 0.0037084125513246655,
  "saddle_positive": 0.0002692383430124569,
  "edge_exclusion": 0.0001908723966348686
}
```

## Complete external-arrow audit and exact obstruction

`external_arrow_table.json/.csv` contains every new-row true edge, both mutual arrows, every directed external arrow, and every candidate paired-vertex cone coefficient. Exactly one non-`T27` edge has all external arrows positive at both endpoints:

```text
edge=['W2', 'W3']
incident facets=[['G', 'W2', 'W3'], ['W1', 'W2', 'W3']]
minimum external support=377.24393986901543
mutual supports=[809.2601172965665, -461.0140403043512]
||H_W2-H_W3||²=348.2460769922152
```

The exact identity `A(W2→W3)+A(W3→W2)=||H_W2-H_W3||²>0` forces one endpoint stable; at the anchor it is `W2`. Since `T27` is independently stable, `S≥2` throughout the certified incidence/external-arrow chamber.

## Shape freedom and open box

The three moment controls have exact Jacobian `-I_3`, determinant `-1`. Five independent shape controls remain after moment elimination:

```text
T27_z, W3_y, SU_z, SA5_x, S102_y
```

They control the closed-cell diagonal, stable-component death, source death, and both saddle deaths. Their exact `5×5` Jacobian determinant is nonzero; decimal `0.0020006123296736848`, with normalized singular values `[1.5588337269840078, 1.0132322255049917, 0.9992168515166463, 0.6503168607599539, 0.3493587455207428]`.

Directed outward-rounded intervals certify all 66 raw coordinates independently in

```text
|δq_ij|≤2^-22=2.384185791015625e-07
```

while preserving incidence, inactivity, boundedness, own-centroid recomputation, `(2,2,2)`, the shared core, inherited-packet deletion, and the `W2-W3` theorem. Volume interval: `[0.0009952464536918332, 0.0009953405984092754]`. Centroid intervals: `[[-0.0051526122188174, -0.00515009797691812], [0.032202692230544894, 0.03221762426896314], [-0.05611725272125365, -0.056095740445201894]]`. Key rigorous lower bounds include nonincidence `0.06265312834159596`, inactive slack `0.06406634521969877`, saddle component `0.00026773677684659045`, communicating tetra volume `9289.488024407881`, and residual external support `374.9330774427259`.

## Independent verification and meshes

`verify_independent.py` imports neither the generator nor `exact_core.py`. It independently reconstructs all 816 original-XG8 triples, 816 coupled-pre-event triples, and 1540 successor triples; exact H/V/E, volume/moments/centroid, all full cones, the shared event and deletion, rank-five controls, the complete arrow table, interval certificate, and mesh multiplicities. It ends with

```text
P9_XG9_INDEPENDENT_CLEAN_ROOM_PASS
```

The OBJ has 18 vertices, 27 edges, and 11 maximal polygonal faces; the STL has 32 triangles and 48 triangle edges. Both are watertight. A clean extraction followed by `./RUN_ALL.sh` ends

```text
ALL P9-XG9 VIVID ATLAS 32 VERIFIERS PASS
```

## Search scope and next topology

Seven independent 10,000-proposal full-hull campaigns produced 69,988 valid hulls and 9,782 target-lineage states without a winner. Later differentiable and adjacent-circuit searches improved the empirical hard score to about `-0.0267634` but opened balanced transfer clusters, commonly `(5,2,5)`. This is discovery evidence only, not a global four-row exclusion.

The exact residual block is stable `W2`, source `T27/SU/W0`, saddles `SA5-W2`,`S102-W0`, and forcing edge `W2-W3`. The first nonrepeating continuation is a **five-row carrier-free double-bipyramid/antiprismatic `3↔3` event** replacing the entire W cell. It must impose a nonpositive external arrow at every possible internal carrier, delete the whole residual block in one shared volume, preserve `T27` and `TR/S102/G`, and retain at least six post-moment controls. A distributed closed prism with coupled old-plane motion is the equivalent fallback.

This exact result closes the displayed four-row topology and its `2^-22` chamber only. No strict own-centroid `(1,1,0)` body is claimed.

## Artifacts

- [Complete exact package](sandbox:/mnt/data/P9_XG9_FOUR_ROW_CLOSED_CELL_EXACT_NONWINNER.zip)
- [Archive SHA-256](sandbox:/mnt/data/P9_XG9_FOUR_ROW_CLOSED_CELL_EXACT_NONWINNER.zip.sha256)
- [Complete handoff](sandbox:/mnt/data/P9_XG9_FOUR_ROW_CLOSED_CELL_EXACT_NONWINNER/RESEARCH_HANDOFF.md)
- [Exact rows](sandbox:/mnt/data/P9_XG9_FOUR_ROW_CLOSED_CELL_EXACT_NONWINNER/input_rows_exact.json)
- [Complete exact ledger](sandbox:/mnt/data/P9_XG9_FOUR_ROW_CLOSED_CELL_EXACT_NONWINNER/p9_xg9_closed_cell_exact.json)
- [Exact mass and centroid](sandbox:/mnt/data/P9_XG9_FOUR_ROW_CLOSED_CELL_EXACT_NONWINNER/exact_mass_centroid.json)
- [Shared-event certificate](sandbox:/mnt/data/P9_XG9_FOUR_ROW_CLOSED_CELL_EXACT_NONWINNER/shared_event_exact_certificate.json)
- [Deletion certificate](sandbox:/mnt/data/P9_XG9_FOUR_ROW_CLOSED_CELL_EXACT_NONWINNER/inherited_component_deletion_certificate.json)
- [External-arrow table](sandbox:/mnt/data/P9_XG9_FOUR_ROW_CLOSED_CELL_EXACT_NONWINNER/external_arrow_table.json)
- [Obstruction certificate](sandbox:/mnt/data/P9_XG9_FOUR_ROW_CLOSED_CELL_EXACT_NONWINNER/component_obstruction_certificate.json)
- [Control-rank certificate](sandbox:/mnt/data/P9_XG9_FOUR_ROW_CLOSED_CELL_EXACT_NONWINNER/control_rank_certificate.json)
- [Perturbation certificate](sandbox:/mnt/data/P9_XG9_FOUR_ROW_CLOSED_CELL_EXACT_NONWINNER/perturbation_box_certificate.json)
- [Exact H table](sandbox:/mnt/data/P9_XG9_FOUR_ROW_CLOSED_CELL_EXACT_NONWINNER/H_supplied_exact.csv)
- [Exact V table](sandbox:/mnt/data/P9_XG9_FOUR_ROW_CLOSED_CELL_EXACT_NONWINNER/V_exact.csv)
- [Maximal faces](sandbox:/mnt/data/P9_XG9_FOUR_ROW_CLOSED_CELL_EXACT_NONWINNER/maximal_faces.csv)
- [True-edge full cones](sandbox:/mnt/data/P9_XG9_FOUR_ROW_CLOSED_CELL_EXACT_NONWINNER/true_edges_full_cones.csv)
- [Independent verifier](sandbox:/mnt/data/P9_XG9_FOUR_ROW_CLOSED_CELL_EXACT_NONWINNER/verify_independent.py)
- [Independent report](sandbox:/mnt/data/P9_XG9_FOUR_ROW_CLOSED_CELL_EXACT_NONWINNER/independent_verification_report.json)
- [Watertight OBJ](sandbox:/mnt/data/P9_XG9_FOUR_ROW_CLOSED_CELL_EXACT_NONWINNER/p9_xg9_closed_cell_centered.obj)
- [Watertight STL](sandbox:/mnt/data/P9_XG9_FOUR_ROW_CLOSED_CELL_EXACT_NONWINNER/p9_xg9_closed_cell_centered.stl)
- [Packaged verifier transcript](sandbox:/mnt/data/P9_XG9_FOUR_ROW_CLOSED_CELL_EXACT_NONWINNER/RUN_ALL_OUTPUT.txt)
- [Clean-extraction transcript](sandbox:/mnt/data/P9_XG9_CLEAN_VERIFY.txt)

Archive SHA-256: `c2fe8fa9a00d10fefd0b38d4cee01f644aed10d3e87c3f4df62f6f009b5171c3`.
