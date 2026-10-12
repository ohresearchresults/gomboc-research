# figure-0270

AI research report · 2026-09-03 UTC · [Export notes](../../catalog/coverage.md#text-records)

---

# Calm Quartz 90 — exact wall-242 fourteenth linked two-cell cage

## Disposition

**EXACT DELIMITED NONWINNER.** No finite homogeneous convex polyhedral Gömböc was obtained in this topology.

The acceptance gate remains a finite uniform-density body at its own exact ordinary-volume centroid with strict `(S,U,H)=(1,1,0)`, complete H/V/true-edge mechanics, an open certificate, independent reconstruction, and matching OBJ/STL. :contentReference[oaicite:0]{index=0} The immutable parent `figure-0268`, SHA-256 `470c23af061fa7a9ee65b015138e0a600f506ee50769a962d4ca173d3f98f46a`, is the exact nine-vertex annular cage with packet stable `[C,AH,AM]`, unstable `AM`, saddles `[0,AI]`,`[C,AJ]`, and forcing edge `[0,AM]`; the journal identifies a linked-cell cancellation as the next frontier. 

A literal zero-bridge linked two-cell/full-hull surgery was realized. New extreme rows `AN=40039`, `AO=40040`, `AP=40041`, `AQ=40042`, `AR=40043` replace released rows `AH,AJ,AK,AL,AM`; `AI=40034` remains the communication interface. The endpoint has

```text
53 supplied dyadic points; 9 active, 44 strictly inactive
(V,E,F,C)=(9,21,14,42)
(S,U,H)=(2,2,2)
independent coordinate radius 2^-20
```

The entire parent packet is absent or dead: `[0,AM]` and `[C,AJ]` are absent, `AM` is inactive, `[C,AH,AM]` is absent, and retained `[0,AI]` is nonsaddle. Protected stable `[0,H,C]` and unstable `C` survive. The replacement packet is stable `[AN,AR,AO]`, unstable `AO`, saddles `[C,AO]`,`[AI,AR]`, and forcing edge `[0,AO]`.

## Immutable lineage

```text
parent payload SHA-256   470c23af061fa7a9ee65b015138e0a600f506ee50769a962d4ca173d3f98f46a
parent archive SHA-256   eb8f6adec22772d222864deb5891d2c4ed932baf5adb62640b935bf219aa4d96
parent generator SHA-256 2417ff113675546e4adf43e516f2890d34c099986a97bd06b64fe954bf8c473f
```

The embedded parent archive and generator are byte-identical to the accepted lineage; no alias, class, incidence, or digest conflict was found.

## Exact source/target generator

Let `D=2^24=16777216`. Supplied order is

```text
0,1258,1371,1975,2152,2369,2515,2732,3290,3296,A,B,C,D,E,F,G,H,I,J,K,L,M,N,O,P,Q,R,S,T,U,V,W,X,Y,Z,AA,AB,AC,AD,AE,AG,AH,AI,AJ,AK,AL,AM,AN,AO,AP,AQ,AR.
```

Aliases are alphabetical from `A=40001`. Any row not overridden below is `(i+1,-2(i+1),3(i+1))/D`, for zero-based supplied position `i`; `B=(0,0,0)`.

Source overrides:

```text
0  ( 2382238, -6308946,  46171779)/D
C  (-19656014,-12570508, -84150451)/D
H  ( -1678613, 11935619, -25478204)/D
AH ( 3391993,  11774700, -43963956)/D
AI ( 2970862,  20310871, -20339795)/D
AJ (-1779229, -24941844,  33232093)/D
AK ( -101188, -21585441,  24317427)/D
AL ( 1480823,  13579291, -48902137)/D
AM (11023382, -13034518,  49560491)/D
```

Source active set `{0,C,H,AH,AI,AJ,AK,AL,AM}`, exact `(9,21,14)`, `(2,2,2)`.

Target overrides:

```text
0  ( 2382238, -6308946,  46171779)/D
C  (-19656014,-12570508, -84150451)/D
H  ( -1678613, 11935619, -25478204)/D
AI ( 2970862,  20310871, -20339795)/D
AN ( 2496892,  -7936165, -53858068)/D
AO ( 7724346, -28139719,  46540096)/D
AP (-1747357, -18933600,  27205059)/D
AQ ( 4823029,  20341176, -49635553)/D
AR (14497849,   4859493,  20727499)/D
```

Target active set `{0,C,H,AI,AN,AO,AP,AQ,AR}`. All other supplied rows are strict interior. Minimum exact inactive slack:

```text
1833779883027233541809/4722366482869645213696>0.
```

## Exact mass, centroid, and H/V reconstruction

```text
Vol=222732884145492544177781/28334198897217871282176

c=(
 64779171710956915381375646039/1868418853805951920030087118848,
-961215070725757835554839450607/3736837707611903840060174237696,
-12665972060243863505523617040863/14947350830447615360240696950784
).
```

Set `p_i=r_i-c`. Exact tetrahedral summation gives `Mx=My=Mz=0`. For each oriented face `(i,j,k)`, reconstruct its exact primitive H row by `n=(p_j-p_i)×(p_k-p_i)`, `b=n·p_i`, `n·x<=b`, then clear denominators and divide the four coefficients by their gcd. Thus the supplied coordinates, centroid, and face list below are a complete deterministic exact H/V generator.

## Actual incidence

Maximal faces:

```text
[0,H,C]* [0,C,AP] [0,AI,H] [0,AR,AI] [0,AP,AO] [0,AO,AR]
[C,H,AI] [C,AI,AQ] [C,AN,AO] [C,AQ,AN] [C,AO,AP]
[AI,AR,AQ] [AN,AR,AO]* [AN,AQ,AR]
```

Stars mark stable faces. Physical true edges:

```text
[0,C] [0,H] [0,AI] [0,AO] [0,AP] [0,AR]
[C,H] [C,AI] [C,AN] [C,AO]* [C,AP] [C,AQ]
[H,AI] [AI,AQ] [AI,AR]* [AN,AO] [AN,AQ] [AN,AR]
[AO,AP] [AO,AR] [AQ,AR]
```

Stars mark saddles. Every edge has two incident maximal faces; `9-21+14=2`. Minimum active nonincidence distance is `0.042115751216339141`. No display diagonal is counted.

## Exhaustive own-centroid mechanics

The exact verifier uses face-foot barycentrics, all directed arrows `sigma(v→w)=-v·(w-v)`, and for each true edge the four signs `t,1-t,beta1,beta2` from the two incident outward normal cones.

Exactly `[0,H,C]` and `[AN,AR,AO]` are stable; their minimum barycentrics are respectively

```text
1157684275289681579102519321299753107274602526851025713/4130773766765568407635224163253910322774349906150308912,
102033999961887076106850358903547833399371719623823047/761984064550549791008025915437513807430837427570484760.
```

Every other face has a negative exact witness; closest decision `≈-0.07429219901496409`.

Exactly `C,AO` are unstable. Exact minimum outgoing supports:

```text
C→AN=2320916282563740585644970136174902564303/250774933510199019583675984733844537344;
AO→0=517305702213152210400032135095587696819/250774933510199019583675984733844537344.
```

Every other vertex has a negative witness; closest is `0→AO=-67156819054343621979918638563458658251/250774933510199019583675984733844537344`.

Exactly `[C,AO]`,`[AI,AR]` are saddles. Their normalized four-component tuples are

```text
[C,AO]  (0.5292849239927481,0.4707150760072519,0.5595197676649267,0.7433419508016123)
[AI,AR] (0.2936813910603234,0.7063186089396766,0.6835267065993010,0.4320835293107194).
```

Every other edge has a negative exact component; closest normalized exclusion `≈-0.10688892436189586`. Full finite ledgers audit all 14 faces, 42 directed vertex primitives, and 84 edge-cone components.

## Connected positive-volume replacement

Common faces are `[0,C,H]`, `[0,H,AI]`, `[C,H,AI]`. Removing them leaves dual-connected one-boundary disks with common boundary `0-C-AI-0`; both have `(V,E,F)=(8,18,11)`, Euler characteristic one, and no bridge face.

Source patch:

```text
[0,C,AJ] [0,AI,AM] [0,AJ,AM] [C,AH,AL] [C,AH,AM]
[C,AI,AL] [C,AJ,AK] [C,AK,AM] [AH,AI,AL] [AH,AI,AM] [AJ,AK,AM]
```

Target patch:

```text
[0,C,AP] [0,AI,AR] [0,AO,AP] [0,AO,AR] [C,AI,AQ]
[C,AN,AO] [C,AN,AQ] [C,AO,AP] [AI,AQ,AR] [AN,AO,AR] [AN,AQ,AR]
```

Every centroid-cone tetrahedron is exact-positive. Minimum source/target cell volumes are

```text
691224453327707265542643330762120482628287129/11821364656977401607723741661026644204804112384,
2661480643106021770299555641474092675264340891/8414610453772494309087124139784824626880708608.
```

Removed edges:

```text
[0,AJ] [0,AM] [C,AH] [C,AJ] [C,AK] [C,AL] [C,AM]
[AH,AI] [AH,AL] [AH,AM] [AI,AL] [AI,AM] [AJ,AK] [AJ,AM] [AK,AM].
```

Inserted edges:

```text
[0,AO] [0,AP] [0,AR] [C,AN] [C,AO] [C,AP] [C,AQ]
[AI,AQ] [AI,AR] [AN,AO] [AN,AQ] [AN,AR] [AO,AP] [AO,AR] [AQ,AR].
```

Star-changed inherited edges: `[0,C]`, `[0,AI]`, `[C,AI]`.

## Complete changed-edge arrow census

All target edges and all 18 changed edges were audited. The sole nonprotected all-positive changed edge is `[0,AO]`. Protected all-positive changed edges `[C,AN]`,`[C,AO]`,`[C,AQ]` lie in the intended unstable-`C` star. The remaining 14 changed edges have exact negative witnesses:

```text
[0,AP] AP→AO=-813780358915564778780958009821401256551/250774933510199019583675984733844537344
[0,AR] AR→AO=-449890294399934358382873832291073243571/250774933510199019583675984733844537344
[C,AP] same AP→AO witness
[AI,AQ] AQ→C=-136831330651615210846839642124423858051/125387466755099509791837992366922268672
[AI,AR] AR→0=-137660569275324267758315831518031364269/62693733377549754895918996183461134336
[AN,AO],[AN,AQ],[AN,AR] AN→C=-1047011724680076718296297412343458808727/250774933510199019583675984733844537344
[AO,AP] AP→0=-18819855435387691809485614582525174539/8956247625364250699416999454780162048
[AO,AR],[AQ,AR] same AR→0 witness
[0,C] 0→AO=-67156819054343621979918638563458658251/250774933510199019583675984733844537344
[0,AI],[C,AI] AI→AQ=-82213648214839133899924676045541678719/125387466755099509791837992366922268672.
```

The nonprotected adverse graph therefore has one edge, two vertices, cycle rank zero, no two-edge component, and no positive directed cycle.

## Residual forcing theorem

`[0,AO]` is incident to `[0,AP,AO]`,`[0,AO,AR]`. Every external endpoint arrow is positive; minimum

```text
17940150299423597756087661849383077921/4478123812682125349708499727390081024.
```

Mutual arrows are

```text
sigma(0→AO)=-67156819054343621979918638563458658251/250774933510199019583675984733844537344
sigma(AO→0)=517305702213152210400032135095587696819/250774933510199019583675984733844537344
sum=||AO-0||²=252628212536841/140737488355328>0.
```

If neither endpoint were unstable, both mutual arrows would be nonpositive, contradiction. Thus one endpoint is unstable in addition to `C`; here it is `AO`, so the complete chamber has `U>=2`.

## Exact connector chronology

Each decisive polynomial has exact integer coefficients, one Sturm-isolated simple root in the bracket, and independently replayed side mechanics:

```text
0.085383370361126 [853/10000,171/2000] bridge unstable 0 / saddle [0,AM] birth
0.116492199151871 [1163/10000,583/5000] source unstable AM / [0,AM] death
0.275177572224202 [11/40,1377/5000] stable C-AH-AM→C-AM-AN
0.328816049891877 [657/2000,3291/10000] bridge stable AH-AM-AN birth
0.337150970652692 [337/1000,1687/5000] bridge C-AM-AN edge exit
0.389092385599229 [243/625,1947/5000] stable AH-AM-AN→AM-AN-AR
0.417749765336608 [4177/10000,2089/5000] carrier [0,AO] birth
0.464073868895117 [2319/5000,1161/2500] stable AM-AN-AR→AN-AO-AR
0.483050907392871 [483/1000,302/625] saddle [C,AO] birth
0.498635643428410 [997/2000,1247/2500] source saddle [C,AJ] death
0.528770036441840 [1057/2000,5291/10000] AM deactivation / [0,AM] death
0.702201906104398 [7021/10000,439/625] saddle [AI,AR] birth
0.803906652162234 [1607/2000,4021/5000] source saddle [0,AI] death
0.840488033601758 [8403/10000,4203/5000] AO unstable / [0,AO] saddle birth
0.972740515838643 [4863/5000,9729/10000] bridge unstable 0 / [0,AO] saddle death.
```

Replacement instability precedes source-unstable death; `[0,AO]` precedes `[0,AM]` death; replacement saddles precede source deaths; the extra stable transfers with no gap; `AO` is unstable before bridge `0` dies. No strict `(1,1,0)` interval occurs on this connector.

## Positive open box and clean replay

All 159 uncentred coordinates vary independently by `2^-20`. Directed exact intervals recompute volume, moments, dependent centroid, inactivity, incidence, all face/vertex/edge decisions, changed-edge witnesses, and the forcing theorem. They preserve `(9,21,14)` and `(2,2,2)`.

```text
Vol interval:
[222731534834309629652021/28334198897217871282176,
 222734233457245378075829/28334198897217871282176]

box-wide lower clearances (exact rationals in certificate):
topology 0.36874708532568201; inactive 0.38773057808643507;
face 2.9629821002686274; vertex 0.26768282060393894;
edge cone 0.26768282060393894; forcing 4.0060489387657414;
anti-carrier 0.26768282060393894.
```

A clean extraction reran deterministic generation, chronology, interval verification, primary exact reconstruction, independent Sturm and clean-room verifiers, mesh verification, manifest verification, and package verification. OBJ/STL agree on 9 vertices, 14 outward facets, 21 edges, Euler two, and edge multiplicity two.

## Exact scope and next topology

Closed: this `AN/AO/AP/AQ/AR` linked cell; release of `AH/AJ/AK/AL/AM`; exact parent reconstruction; the zero-bridge positive-volume surgery; parent-packet deletion; all changed-arrow decisions; the 15-event connector; the `2^-20` chamber; and the `[0,AO]` theorem.

Not closed: all linked-cell placements/release sets/paths, the next coupled cell, or global existence.

The endpoint exposes legal moves `[0,AO]→[AP,AR]`, `[AN,AR]→[AO,AQ]`, `[C,AO]→[AN,AP]`, `[AI,AR]→[0,AQ]`. The first nonrepeating successor is a linked prismatic/double-octahedral cell enclosing the full `[0,AO]` star, stable `[AN,AO,AR]`, and both saddle stars, permitting `0` or `AO` to deactivate and requiring the whole packet to die before substitutes become strict.

## Artifacts and integrity

- [Verified exact archive](sandbox:/mnt/data/Calm_Quartz_90_wall242_fourteenth_linked_two_cell_exact_NONWINNER_VERIFIED.zip)
- [Full self-contained handoff](sandbox:/mnt/data/Calm_Quartz_90_wall242_fourteenth_linked_two_cell_VERIFIED_HANDOFF.md)
- [Full structured result](sandbox:/mnt/data/Calm_Quartz_90_wall242_fourteenth_linked_two_cell_VERIFIED_RESULT.json)
- [Clean receipt](sandbox:/mnt/data/Calm_Quartz_90_wall242_fourteenth_linked_two_cell_clean_verification_VERIFIED.json)
- [Clean replay](sandbox:/mnt/data/Calm_Quartz_90_wall242_fourteenth_linked_two_cell_clean_replay_VERIFIED.txt)
- [Exact generator](sandbox:/mnt/data/Calm_Quartz_90_wall242_fourteenth_linked_two_cell_exact_NONWINNER/data/generator_exact.json)
- [Centred V-data](sandbox:/mnt/data/Calm_Quartz_90_wall242_fourteenth_linked_two_cell_exact_NONWINNER/data/active_vertices_centered_exact.csv)
- [Primitive H-data](sandbox:/mnt/data/Calm_Quartz_90_wall242_fourteenth_linked_two_cell_exact_NONWINNER/data/fourteenth_cage9_exact_H_irredundant.csv)
- [Face ledger](sandbox:/mnt/data/Calm_Quartz_90_wall242_fourteenth_linked_two_cell_exact_NONWINNER/data/fourteenth_cage9_exact_faces.csv)
- [Vertex ledger](sandbox:/mnt/data/Calm_Quartz_90_wall242_fourteenth_linked_two_cell_exact_NONWINNER/data/fourteenth_cage9_exact_vertex_primitives.csv)
- [Edge-cone ledger](sandbox:/mnt/data/Calm_Quartz_90_wall242_fourteenth_linked_two_cell_exact_NONWINNER/data/fourteenth_cage9_exact_true_edges_full_cones.csv)
- [Arrow ledger](sandbox:/mnt/data/Calm_Quartz_90_wall242_fourteenth_linked_two_cell_exact_NONWINNER/data/external_arrow_full_ledger.csv)
- [Transition certificate](sandbox:/mnt/data/Calm_Quartz_90_wall242_fourteenth_linked_two_cell_exact_NONWINNER/certificates/fourteenth_cage_shared_global_patch.json)
- [Chronology certificate](sandbox:/mnt/data/Calm_Quartz_90_wall242_fourteenth_linked_two_cell_exact_NONWINNER/certificates/source_to_target_death_before_birth_obstruction.json)
- [Perturbation certificate](sandbox:/mnt/data/Calm_Quartz_90_wall242_fourteenth_linked_two_cell_exact_NONWINNER/certificates/own_centroid_perturbation_certificate.json)
- [Independent verifier](sandbox:/mnt/data/Calm_Quartz_90_wall242_fourteenth_linked_two_cell_exact_NONWINNER/scripts/verify_independent.py)
- [Watertight OBJ](sandbox:/mnt/data/Calm_Quartz_90_wall242_fourteenth_linked_two_cell_exact_NONWINNER/mesh/body.obj)
- [Watertight STL](sandbox:/mnt/data/Calm_Quartz_90_wall242_fourteenth_linked_two_cell_exact_NONWINNER/mesh/body.stl)

```text
verified archive SHA-256 0ff390106ec996f980b65b9ed6ffebc94c1be23cc4797adcacc737fc13f69406
verified archive bytes   2744837
manifest entries         50
manifest SHA-256         02d27a891e3c2db5236ef190d80c565cf5cdfdf99010cd720b9e1e4fa446015d
clean replay SHA-256     64927cb36b43f7cd9e963a3792e6cb3f56cba4d70e211bd97213e62e0c5ee272
clean receipt SHA-256    a164afb03f33e13deb0e3ed51e9a9fc1cc42c4ad9de5afd6fb9f7576c0de8fd7
clean extraction         PASS
```

**Final statement:** `NONWINNER`, rigorously delimited. The linked two-cell surgery genuinely destroys the immutable annular-cage packet and leaves no nonprotected adverse component larger than one edge. It fails because inserted `[0,AO]` is an exact all-external-positive forcing carrier, and every replacement channel is born before its source channel dies.
