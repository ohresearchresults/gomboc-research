# figure-0077

Historical AI scientific report · saved 2026-08-26 UTC. Claims below retain their original status and have not all been independently checked. The current retained construction is C622; the C<500 search remains open.

Public text derivative: internal-record-identifiers-replaced.

---

# Verdict

No strict own-centroid homogeneous convex polyhedral Gömböc was found. The acceptance gate remains a finite uniform-density body with exact own-centroid class `(S,U,H)=(1,1,0)`; auxiliary-center mechanics, transfer walls, and near-zero-margin candidates do not count. :contentReference[oaicite:0]{index=0}

The strongest fully certified endpoint remains an exact rational, full-active post-crossing tower with

```text
(V,E,F,C)=(33,50,19,100),   (S,U,H)=(2,2,2).
```

The new continuation did open a genuinely different four-plus-four branch family, deleting the old residual source rows rather than polishing their witnesses. Across 15,000 architecture samples, 364 valid full-active route-connected bodies, 272 reconstructed topology signatures, fixed-cell SLP, nine complete CEM generations, and dynamic circuit scans, no cell had fewer than four excess equilibria. The simultaneous mechanical zero direction changes the lower cap from five to six vertices before cancellation, so it violates the assignment.

# Exact accepted fallback

## Exact rational generator

With common denominator `D=100000000000`, the body is `A_num[i]·x <= b_num[i]`. The second column is the persistent source-row identity.

```text
local src              A_num=(Ax,Ay,Az)                     b_num
 0   0  (          0,          0,-272547080000)       100000000000
 1   1  (37215770000,-17361380000, 61797810000)       100000000000
 2   2  (35589620000, -8818240000,-138307200000)      100000000000
 3   3  (-14390180000, 8374660000,-227141280000)      100000000000
 4   4  (-41042170000,14852730000, -3000900000)       100000000000
 5   7  (-50041080000,18437340000,102188600000)       100000000000
 6   8  (-36642030000, 9793540000,290114300000)       100000000000
 7  10  (45771090000,-14923590000, 65503090000)       100000000000
 8  11  ( 3669980000, 3184590000,-63415600000)        100000000000
 9  12  (-21972990000, 4729450000,292488850000)       100013186909
10  13  (24675000000, -6018130000, 41314440000)       100001350453
11  14  (-31741440000,16400120000,-87168060000)        99996891472
12  15  (-30235380000,12200450000, 81509640000)       100004402899
13  17  (-46281160000,16105510000,154383100000)       100000000000
14  18  (-43982120000,17111080000, -2125080000)       100000000000
15  19  (-43445460000,18551430000, -2021960000)       100000000000
16  20  ( 2730790000,-5509680000,  7230220000)        100000000000
17  21  ( 6246250000,-7032810000,   535990000)        100000000000
18  23  (40346240000,-12385750000,-39300580000)       100000000000
```

All 19 rows are active. Exact source set:

```text
[0,1,2,3,4,7,8,10,11,12,13,14,15,17,18,19,20,21,23].
```

The canonical generator has exact own centroid `c`; translating by its exact rational value gives the centered H-description and exact first moments `(0,0,0)`. The exact volume is approximately

```text
85.805333827362166257926461968732505290650271,
```

and the canonical-gauge centroid is approximately

```text
(2.2680061037795691e-5, 8.116193673574253e-6, 1.1385620277536291e-5).
```

The exact apex is `(12553/1250,288791/10000,3147/5000)`. Exact fractions for the volume and centroid, all 33 rational V coordinates, and the centered H rows are in the bundle.

## Layers and topology

```text
L0 lower cap: [0,1,2,3,4]
L1: [5,9,10,12,15,16,17,18,19,20,21,26]
L2: [6,7,11,13,14,22,24]
L3: [8,23,28]
L4: [25,27,30,31,32]
L5 apex: [29]
```

The independent reconstruction gives exactly 19 maximal faces and 50 true edges; Euler is `33-50+19=2`. The complete outward face cycles and true-edge/incident-row table are in [topology.txt](sandbox:/mnt/data/continued_tower_222_compact_bundle/topology.txt), while every exact V coordinate and incidence is in [tower_continued_222_V.csv](sandbox:/mnt/data/continued_tower_222_compact_bundle/tower_continued_222_V.csv).

## Exhaustive own-centroid mechanics

```text
STABLE
source face 0, cycle [0,1,4,3,2]
  +0.03271953303758104455506341866694087185552   target
source face 12, cycle [6,8,27,29,30,25]
  +0.0008185417565584246582863430558159201544832 unwanted

UNSTABLE
vertex 4, incident sources [0,4,21]
  +0.0007474709561146043933065646329385803135902 unwanted
vertex 29, incident sources [12,13,14,15]
  +0.8490998640768104811210992534721776719937 target apex

SADDLES
edge [11,12], source pair [2,10]
  +0.0009093578204261716988991882815569964376048
edge [16,31], source pair [14,19]
  +0.0006409157628241770854256863441691726268963
```

Exact hard defect:

```text
-0.0009093578204261716988991882815569964376048.
```

Every other one of the 19 faces, 33 vertices, and 50 true edges is strictly non-equilibrial. The smallest exclusion margin is `0.0002209163892973414524063362274439208484915` at local face 8/source 11. The exhaustive primitive and normalized normal-cone conditions are in [tower_continued_222_audit.json](sandbox:/mnt/data/continued_tower_222_compact_bundle/tower_continued_222_audit.json).

## Support, routes, perturbation, verifier

```text
Euclidean nonincident support separation
  0.0003150621917597137512385035856227765245579
normalized separation
  0.0000103022724388765828157581700433208829633
witness
  local row 13/source 17 versus vertex 31
exact integer-row slack
  2499684788833200000000000/79075618140415793 > 0
```

Five reconstructed true-edge routes connect the lower cap to the apex:

```text
0-2-10-14-28-29
1-7-6-8-27-29
2-10-14-28-29
3-2-10-14-28-29
4-1-7-6-8-27-29.
```

The replacement branches remain face-connected through `17-7-18`, `18-19`, `20-21`, and `21-1-23`.

An exact interval verifier permits the six supports of source rows `17,18,19,20,21,23` to vary independently by `±5000/10^11 = ±5×10^-8`. Throughout the entire box, topology `(33,50,19,100)` and class `(2,2,2)` remain constant.

```text
PASS_EXACT_POST_CROSSING_222_FALLBACK
PASS_INTERVAL_BOX
PASS_ALL_CHECKS
exact certificate SHA-256:
9995ef5d8c7c06fe30fb1cbedd22c5ca0d4c7c62fdbc27fd22f563f7bf300060
interval certificate SHA-256:
08312133b8028dbbd47dad491521b1d062419b5e9523233fe295af3163bfa743
```

# Exact transition into this endpoint

```text
previous 20-facet sources:
[0,1,2,3,4,6,7,8,10,11,12,13,14,15,16,18,19,21,22,23]

new 19-facet sources:
[0,1,2,3,4,7,8,10,11,12,13,14,15,17,18,19,20,21,23]

activated [17,20]; deactivated [6,16,22]; old rows [5,9] remain obsolete
(V,E,F,C): (35,53,20,106) -> (33,50,19,100).
```

The crossing annihilates temporary pair `U(2,10,23)/H(10,23)` but leaves `S12`, `U(0,4,21)`, `H(2,10)`, and `H(14,19)`.

# New four-plus-four topology family

The new dual paths are

```text
A: (2,10)-(10,12)-(12,8)-(8,17), new sources 24,25,26,27
B: (14,19)-(19,3)-(3,4)-(4,21), new sources 28,29,30,31.
```

The best full-active cell deletes old sources `[4,10,11,12,19,20,21]` and realizes

```text
[0,1,2,3,7,8,13,14,15,17,18,23,24,25,26,27,28,29,30,31].
```

Thus the old stable source 12, unstable-corridor sources 4/21, and saddle-corridor sources 10/19 are absent. Search coverage:

```text
15,000 attempts; 364 valid full-active five-route bodies; 272 topology signatures
class histogram:
(2,2,2)=271, (3,2,3)=84, (2,3,3)=4, (4,2,4)=4, (4,4,6)=1
minimum excess count=4; no winner.
```

The best fixed-cell diagnostic is `(36,54,20,108)`, class `(2,2,2)`, with lower/apex margins `0.0118846624/0.8820714151`, normalized support `1.10587988e-6`, and residual block

```text
F26 +0.0024758538
V(0,1,31) +0.0224732945
E(1,24) +0.0184332136
E(18,28) +0.0123392718.
```

It is rejected as an endpoint because it is floating, has weaker support separation, and its common-zero path leaves the lower-pentagon chamber.

The four-witness Jacobian has full row rank, singular values approximately

```text
1.60234242e4, 10.8905746, 5.0772720, 2.9549082.
```

Dynamic hull reconstruction along its least-norm common-zero direction gives

```text
F26          -> F8
V(0,1,31)    -> V(1,26,31)
E(1,24)      -> E(1,23)
E(18,28)     -> E(7,28),
```

with births at `E(1,31)` and `V(7,18,28)`. At the first tested positive step the lower cap already has six vertices; by the time all original witnesses cross, the transferred block still has four excess equilibria. Nine complete CEM generations of 900 proposals each likewise retained at least four extras. A separate 17-iteration robust-seed SLP only transferred `(18,28)->(18,29)`.

# Delimited exhaustion and obstruction

Completed coverage includes: 4,400 paired-radial proposals/1,991 valid states; 8,000 two-plane/deactivation attempts/505 valid/317 signatures; 10,000 four-facets-per-branch attempts/52 valid/34 signatures; a sparse complete four-plane block; an earlier union catalog of 1,334 accepted states/83 residual blocks; the new 15,000-state four-plus-four family; nine CEM generations; fixed-cell SLP; and dynamic Jacobian/circuit scans. No accepted cell had fewer than four excess equilibria. The CEM run stopped after nine completed generations, and no claim is made about unexecuted generations.

The sharply delimited empirical obstruction is:

> In the enumerated extended-edge-path cells, the four mechanical witnesses have full local rank, but the simultaneous negative direction shares a circuit with the lower-cap dual one-ring. The cap becomes a hexagon before the `S/U/2H` block disappears. Enforcing a five-cycle forces the block to relay.

The next nonredundant family should parameterize the lower pentagon structurally as face 0 meeting five prescribed adjacent facet pairs, replace that entire dual one-ring simultaneously with branch B, and add an independent cap-degree circuit control. A 21–23-facet cell should be enumerated before metric polishing, with the three volume moments eliminated after every crossing.

# Artifacts

- [Complete continuation bundle](sandbox:/mnt/data/tower_edgepath_continuation_bundle.zip) — SHA-256 `beccbbdb6d83f2ba11f778d4b6e4a55ba3baed4dbb5bfa0f739716c0b574be28`
- [Bundle hash](sandbox:/mnt/data/tower_edgepath_continuation_bundle.zip.sha256)
- [Machine-readable continuation summary](sandbox:/mnt/data/tower_edgepath_continuation_bundle/new_edgepath_summary.json)
- [Exact fallback bundle](sandbox:/mnt/data/continued_tower_222_compact_exact_fallback_bundle.zip) — SHA-256 `9f35c7de0953be9b351cd27ed9435e020bf422c1397ae91345fe17b23e1ca494`
- [Exact H](sandbox:/mnt/data/continued_tower_222_compact_bundle/tower_continued_222_H_rational.json)
- [Exact centered H](sandbox:/mnt/data/continued_tower_222_compact_bundle/tower_continued_222_H_centered_rational.json)
- [Exact V table](sandbox:/mnt/data/continued_tower_222_compact_bundle/tower_continued_222_V.csv)
- [Complete audit](sandbox:/mnt/data/continued_tower_222_compact_bundle/tower_continued_222_audit.json)
- [Exact verifier](sandbox:/mnt/data/continued_tower_222_compact_bundle/verify_continued_exact.py)
- [Interval verifier](sandbox:/mnt/data/continued_tower_222_compact_bundle/verify_branch_support_box.py)
- [OBJ](sandbox:/mnt/data/continued_tower_222_compact_bundle/tower_continued_222.obj)
- [STL](sandbox:/mnt/data/continued_tower_222_compact_bundle/tower_continued_222.stl)
- [15,000-state new-family result](sandbox:/mnt/data/tower_edgepath_continuation_bundle/new_edgepath_search/edgepath_v2_s73_15k.json)
- [Best new fixed-cell state](sandbox:/mnt/data/tower_edgepath_continuation_bundle/new_edgepath_search/slp_edgepath_v2_best0_r2.json)
- [Circuit analysis](sandbox:/mnt/data/tower_edgepath_continuation_bundle/new_edgepath_search/analyze_edgepath_jacobian_noq0.log)

From the extracted combined bundle, run `cd exact_post_crossing_222 && ./[internal-source-reference].sh`; the reproduced terminal status is `PASS_ALL_CHECKS`.
