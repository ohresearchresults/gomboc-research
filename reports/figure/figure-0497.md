# figure-0497

AI research report · 2026-09-23 UTC · [Export notes](../../catalog/coverage.md#text-records)

---

# Steady Raven 00 — stable-basin cancellation and exact finite mass obstructions

## Outcome

**No actual-centroid strict `(S,U,H)=(1,1,0)` / additional-weak `(0,0,0)` polyhedron was obtained.** This continuation did obtain genuinely changed uniformly filled C50 descendants with **one stable equilibrium and an exactly empty same-centre-polar positive barcode**. They retain one physical unstable/saddle packet. Thus the stable side was canceled in a changed physical body, but the remaining packet was not annihilated on both sides simultaneously.

The preferred new headroom alternative is `C50_MONO44_G4`, V84/E126/F44, strict121/weak000, Qbars empty, with a complete 33-vertex/31-cut physical packet. The smaller `C50_DUALBRIDGE23_G4`, V42/E63/F23, has an 18/18 physical packet and much more headroom, but a deeper well. The larger `C50_MONO85_G4`, V166/E249/F85, has a lower physical barrier but a 64/50 packet and no final edge headroom. **C50_MONO85 is not NW37 MONO85.**

The U1-first route also produced changed own211 bodies with lower whole-Q depth. Its strongest depth endpoint is `C50_HARDTREE84_G5`, V84/E246/F164, with one 45/37 Q packet and birth-relative squared-radius depth approximately .264092745828. However, exact sparse intersection certificates show that these lower-depth descendants lose WHOLEQ58's one-point whole-Q access.

Two new exact results identify restrictions that a successful next construction must release: the **entire fixed-partition WHOLEQ58 one-point insertion cell** is excluded by actual-centroid U>=2, and specified physical-arrow/stable-triangle combinations impose a **finite retained-carrier mass obstruction**. These are scoped statements, not a full-SPD or general deformation exclusion.

## Source authority and reading

The supplied update, branch memory, and literal parent were read through EOF, including the complete decoded parent source capsule. Earlier unchanged context had already been supplied and read. The update `research-journal(20260922-224951).md` is 333590 bytes, SHA-256 `fb7b3687563339b428c3827d8bb58dc06a893e0dbf69067ea4225656d1b17177`.

Literal parent authority is `figure-0493`, supplied outer-result SHA-256 `3c31917ce2149e221994949a9077cc0e3d6ee8574fe06b80014ad66b0d575ccb`. Its 30-unit inner dictionary was recovered and byte-matched: 157591 bytes, SHA-256 `feaaea04b217ca6b86349643bbb4dc967167b42cd18c9019c091ba79792d9c99`. The bare Markdown and enclosing-result serializations have different hashes; I do not claim to have reproduced the enclosing serialization. No scientific conflict or missing required exact dependency was found. Historical source IDs were not treated as accessible files. The incoming WHOLEQ58 and ROOTTURN62 identities and their prior limitations remain those of the literal parent. :contentReference[oaicite:0]{index=0}

## Exact new-body census

All **22 new exact bodies** satisfy true E<=249, additionalweak000, and primitivezero000. Nine are own121, seven own211, and six are informative controls. Here `delta=(birth-death)/birth` uses squared radii; C/B means the entire strict-upper component and complete true-edge cut.

| Exact body | V/E/F | Strict S/U/H | Positive P/Q bars | Remaining component/cut; delta | Centred denominator bits |
|---|---:|---:|---:|---|---:|
| C50_HARDTREE58_G5 | 58/168/112 | 2/1/1 | 0/1 | Q39/33; .333808625217 | 71 |
| C50_HARDTREE84_G5 | 84/246/164 | 2/1/1 | 0/1 | Q45/37; .264092745828 | 70 |
| C50_DUALBRIDGE23_G4 | 42/63/23 | 1/2/1 | 1/0 | P18/18; .873928505906 | 3014 |
| C50_MONOV42_G4 | 42/120/80 | 1/2/1 | 1/0 | P18/45; .873921304152 | 58 |
| C50_MONO44_G4 | 84/126/44 | 1/2/1 | 1/0 | P33/31; .503846293256 | 5895 |
| C50_MONO85_G4 | 166/249/85 | 1/2/1 | 1/0 | P64/50; .311475861925 | 10775 |
| C50_HPRUNE67_EXACT | 84/149/67 | 2/1/1 | 0/1 | Q26/41; .415419204399 | 3999 |
| C50_HPRUNE85_EXACT | 87/170/85 | 2/1/1 | 0/1 | Q37/34; .547431879371 | 4682 |
| C50_TWOARM_REC71_G5 | 71/207/138 | 2/1/1 | 0/1 | Q56/28; .555030404114 | 73 |

Independent fine-grid companions are HARDTREE58 G6, HARDTREE84 G6, DUALBRIDGE23 G5/G6, MONOV42 G5, MONO44 G5 and MONO85 G5. They are distinct exact solids. MONO85 G5 has deltaP approximately .311472838001 and 14210-bit centred denominator; MONO44 G5 has deltaP approximately .503854382344.

The six controls are HARDTREE58 G4, strict312 with a genuine extra Q bar about 1.2520e-7; HARDTREE84 G4, strict222; DUALBRIDGE23 G3, strict244 with three P bars and a genuine Q bar about 2e-12; MONOV42 G3, strict435; TWOARM_RAW G5, strict2/37/37; and MONO23_TWO_CAPS, strict14/4/16. No positive exact bar was removed as numerical noise.

The lower-Q-depth route is not monotone whole-interface progress: incoming Q32/28 grows to Q45/37, headroom falls81→3, and one-point access is lost. Similarly, the S1 route grows P18/18→33/31→64/50 while lowering depth. These tradeoffs must remain explicit.

## Readable exact source-simple S1 entrance

`C50_DUALBRIDGE23_G4` is the uniformly filled intersection of these halfspaces, each row meaning `n_x*x+n_y*y+n_z*z<=h`:

```json
[[-4209,-16404,-110,10000],[-20059,47863,14203,10000],[-11879,52498,-11071,10000],[-21411,35958,28079,10000],[-5251,-2960,-3157,10000],[-19674,23069,34458,10000],[489,31210,-22195,10000],[7950,-983,-20928,10000],[-4995,-17570,7587,10000],[-16487,11250,35892,10000],[5760,17879,-24370,10000],[3934,3717,-11752,5000],[-5913,-16210,15752,10000],[-12889,1333,33978,10000],[-9464,-6450,29917,10000],[-6271,-12090,24806,10000],[-411,-14591,22060,10000],[3908,-16947,1117,10000],[4750,-15988,18133,10000],[13327,-5063,-15702,10000],[8558,-16574,12807,10000],[7649,-16944,4235,10000],[11409,-15818,6640,10000]]
```

Row11 is displayed in an equivalent primitive scaling; the complete capsule retains the original serialization. Actual volume is approximately .6847078971272933; actual centroid approximately `(-.028140360308578388,-.11577441782944442,-.09796822288726421)`. Exact fractions are generated by the verifier, rather than substituting these decimals.

Its canonical mechanics are S facet2, U vertices0/39, H edge30--40. Physical/polar forest depths are13/13, with minimum selected positive cosines approximately .000810189473/.000567933591. The physical forest exempts two roots, not one. Its sole physical bar has the complete state

```json
{"peak":0,"elder":39,"component":[0,1,2,3,4,5,6,7,8,9,10,11,12,13,18,22,26,30],"boundary":[[0,39],[1,38],[3,36],[4,41],[7,16],[8,34],[9,35],[10,28],[10,31],[11,19],[12,32],[13,14],[13,27],[18,28],[22,16],[26,21],[30,25],[30,40]],"path":[0,2,5,6,18,22,26,30,40,41,39]}
```

Qbars is exactly empty. The same exact H input, rounded after exact centring to a 10^-4 free-vertex grid and then independently rehulled/reintegrated, gives MONOV42 G4. Its E120 rather than63 reflects genuine coplanarity loss. Its new actual centroid is approximately `(-8.98086845e-6,1.23348761e-5,3.49096827e-7)`, not assumed zero. This is a new58-bit arithmetic alternative; the earlier45-bit COARSE22 remains an unchanged resource.

## Principal complete remaining interfaces

MONO44 G4 has S11, U7/82, H71--83, Qbars empty and the sole P state

```json
{"peak":7,"elder":82,"component":[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,25,26,29,32,43,50,59,64,68,71],"boundary":[[0,76],[1,78],[2,75],[3,79],[4,73],[5,80],[6,61],[7,81],[9,82],[10,77],[11,61],[12,23],[13,74],[14,31],[15,39],[16,72],[17,69],[18,67],[19,63],[20,58],[22,24],[22,62],[26,51],[32,51],[43,31],[50,57],[59,37],[64,44],[68,52],[71,55],[71,83]],"path":[7,9,10,13,16,18,19,20,21,25,29,32,43,50,59,64,68,71,83,82]}
```

MONO85 G4 has S19, U16/164, H158--165, Qbars empty and the sole P state

```json
{"peak":16,"elder":164,"component":[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,41,42,45,46,47,49,52,57,59,62,76,83,86,94,98,114,118,132,136,142,148,151,155,158],"boundary":[[0,156],[1,159],[2,152],[3,160],[4,150],[5,161],[6,149],[7,162],[8,147],[9,145],[10,157],[11,109],[12,60],[13,153],[15,106],[18,53],[19,40],[23,75],[25,70],[26,80],[27,144],[28,139],[30,44],[31,146],[32,138],[34,106],[35,131],[35,135],[36,134],[37,43],[37,103],[38,48],[38,85],[39,130],[41,127],[42,111],[45,101],[52,50],[59,101],[83,107],[98,65],[118,107],[132,126],[136,71],[142,82],[148,89],[151,113],[155,133],[158,124],[158,165]],"path":[16,17,21,22,24,27,28,32,36,39,41,42,45,46,59,62,76,86,94,114,118,132,136,142,148,151,155,158,165,164]}
```

HARDTREE84 G5 has S48/122, U52, H71--75, Pbars empty and the sole Q state

```json
{"peak":122,"elder":48,"birth":"8608071043562521565055246899736761400927155287500000000000/2066595066616445650477589710096653934555635180172445023009","death":"5883492551221014527629311187141214493750000000000/1919383113635133022043437964567595877150388344847","component":[1,3,5,8,11,13,15,18,19,21,22,24,28,29,31,35,37,40,41,43,44,46,52,56,58,68,69,79,84,85,86,96,105,113,120,121,122,123,124,125,129,133,145,146,147],"boundary":[[1,0],[3,2],[5,4],[8,7],[11,10],[13,12],[15,14],[18,17],[21,20],[22,23],[28,27],[31,30],[35,34],[37,36],[40,39],[41,42],[41,45],[46,47],[52,51],[52,61],[56,57],[68,67],[79,78],[84,100],[96,95],[105,95],[113,114],[121,130],[122,143],[123,150],[124,153],[125,162],[133,132],[145,144],[146,140],[146,148],[147,155]],"path":[122,123,124,125,120,129,133,145,147,146,148,149,137,115,116,48]}
```

All other complete landscapes and exact birth/death fractions are reconstructed by the source capsule, including full weighted graphs and attaining paths. None is represented only by local saddle labels.

## Exact all-orientation WHOLEQ58 one-point obstruction

Fix the58 incoming WHOLEQ58 vertices and require added p to lie beyond exactly its32 dying-Q facets and below all80 complementary facets. The closed visibility cell is bounded with8 vertices,12 edges,6 maximal facets. Active parent planes are `[12,51,71,96,109,110]`, with packet-side bounds12,51,96. All112 inequalities participate in exact enumeration/verification.

**For every p in this closed cell, old canonical physical vertices0 and1 are simultaneously strict unstable vertices of conv(parent,p) at its new actual homogeneous centroid.** Interior hull counts are56/162/108. Boundary points are covered by the same finite mass polynomial, allowing zero-volume added pyramids.

The exact volume and moment are

`V(p)=vc+v·p`,

`M(p)=mc+Lp+p(v·p)/4`,

with

```text
vc=1082464927631/2000000000000
v=(-23122713/200000000,-1798549/4800000,354282809/600000000)
mc=(2482096693477/78125000000000,2403723818971037/80000000000000000,-7878793850966539/120000000000000000)
L=((28180488941/1000000000000,199463832439/4800000000000,-1003509084353/24000000000000),
   (-13766848279/2000000000000,-1174657415783/24000000000000,237943920107/6000000000000),
   (777209391/250000000000,-371933121829/24000000000000,498325681199/24000000000000))
```

For i=0,1, the arrow numerator to old j is `(V(p)p_i-M(p))·(p_j-p_i)`, degree2; the arrow to p is degree3. Polarization over the8 exact cell vertices yields4344 strictly negative rational coefficients: per protected vertex57×36 quadratic coefficients plus120 cubic coefficients. Positive volume is checked at all cell vertices. The largest coefficients are approximately -.002789508290 and -.002873523554. Every old and new target is covered, so both points remain exposed strict-U independently of changing edge labels.

A complete polarization recipe is `M2(a,b)=mc+(La+Lb)/2+(a(v·b)+b(v·a))/8`, `Z2(i,a,b)=p_i(V(a)+V(b))/2-M2(a,b)`. Old-target coefficients are `Z2·(p_j-p_i)`; new-point coefficients average the three pair/singleton assignments. `visibility_cell.py` reconstructs all cell vertices, coefficients and checks.

Scope is fixed old geometry, Euclidean metric, this exact partition, one point. Post-insertion SPD, retained-point motion, different partitions and multiple points remain open.

## Exact centre chambers and retained-carrier mass gate

A fixed physical arrow i→j is positive at centre c precisely when `(p_j-p_i)·c < p_i·(p_j-p_i)`. Exact nonnegative three-row Farkas certificates were constructed for15-arrow WHOLEQ58 and18-arrow ROOTTURN62 closed cones. They are bounded, have26 and32 vertices, and contain the respective actual centroids strictly.

Throughout each cone, all alternative true-edge exits from core sources and all exits from the original unique unstable root are strictly negative. Both old stable triangles retain strict interior feet. A continuous interior reference-centre path retaining U1/no additional weakU cannot leave: its first core-arrow zero creates an additional weakU while the original root remains strictU. Hence the connected centre component containing the actual centroid excludes S1.

Complete core arrows, canonical physical IDs:

```json
{"WHOLEQ58":[[2,4],[5,3],[8,13],[13,17],[29,28],[36,40],[37,35],[38,44],[40,45],[42,39],[43,42],[44,39],[45,43],[48,47],[53,50]],"ROOTTURN62":[[1,0],[2,3],[6,7],[7,5],[10,15],[11,9],[17,14],[18,17],[22,24],[23,20],[26,23],[30,28],[38,34],[40,38],[43,46],[46,44],[49,51],[55,46]]}
```

Stable carriers are WHOLEQ58 facets31 `[13,51,38]` and76 `[34,36,41]`, and ROOTTURN62 facets26 `[6,50,47]` and113 `[54,61,60]`.

**Finite actual-mass corollary:** any new uniformly filled solid retaining these exact chords with positive actual-centroid arrows and both specified unchanged triangles as maximal facets still has S>=2. Its actual centroid belongs to the same cone and the unchanged triangles have strict interior feet. Successful material repair must release at least one core sign, chord geometry or stable-carrier geometry. This is not a general ballast theorem.

The global reference-centre problem is not excluded. Exact points `(294,-417,-399)/1000` in WHOLEQ58 and `(-437,594,-182)/1000` in ROOTTURN62 give reference110/weak000, explicitly mixedH0 and both barcodes empty. They are **not** filled-volume centroids. Their unstable labels26 and53 are unchanged, showing that a root label alone does not identify a connected centre chamber.

## Exact visibility tradeoff and two-cap resource

Positive convex-combination intersection certificates give these fixed-partition obstructions:

| Body/graph | Packet witnesses | Complement witnesses |
|---|---|---|
| HARDTREE58 G5/Q |32,94|40,88,102|
| HARDTREE84 G5/Q |52,96,146|142,155|
| DUALBRIDGE23 G4/P |13,30|16,28,31|
| MONO44 G4/P |0,71|33,51,74|

All exact positive weights are regenerated in `PARTITION_CERTIFICATES.json`. Thus one-point access is lost along the lower-Q-depth U1 route, and a single complement-preserving cap cannot remove the whole H23 or MONO44 physical packet.

For H23, exactly two caps suffice:

```text
(-100000,-49939,-100000)·x <= 61813
(94152,-100000,-78561)·x <= 81092
```

All24 complement vertices satisfy both strictly, all18 packet vertices violate at least one strictly. The child has44/66/24, preserves those24 vertices, replaces the18 removed vertices by20 new vertices, and is strict14/4/16 with3 P and13 Q bars. This is a full actual-mass failure control, not a two-cap-family exclusion.

## Producers, lineage and finite-search scope

The U1 route used actual-mass constrained whole-Q descent, then reconstruction. The1500-budget constrained stage completed1500 iterations/2339 evaluations. Two3000-budget rounds produced HARDTREE58's authoritative pin at round1/iteration2986. Twenty-seven weakest-positive-cosine spherical midpoints gave85 input points; two5000-budget rounds produced HARDTREE84. Exact endpoint lineage certificates retain inactive inputs:58 material points/57 arrows end at material26=canonical33;85 material points/84 arrows end at material26=canonical52. No all-iterate class-preserving homotopy is claimed.

The S1 route genuinely changed representation and geometry. Physical support deletion retained67 WHOLEQ58 supports and85 ROOTTURN62 supports, yielding the nonsimple HPRUNE controls. An18-link polar logarithmic bridge on the67-support body was implemented as real physical halfspaces. Reference S1/U3 became actual S22/U12 after mass rebuilding. Fixed-Q-tree repair was insufficient. Free-support reconstruction with P2/Q1 quotas, actual mass, exposure changes and active-support removal produced H23 own121/Q0. Twenty-two positive-Q midpoint supports and reconstruction gave MONO44;41 further midpoint supports and reconstruction gave MONO85.

An opposite-two-arm mechanism gave95 material points and95 arrows from H23, using21-link short and34-link long routes. It is a **DAG, not a tree**, because the younger old root has two outgoing routes. Its reference-positive raw freeze is actual strict2/37/37. Actual-mass repair yielded TWOARM_REC71 own211 with all95 arrows positive and every material vertex reaching material39=canonical64. U1 was recovered but the stable packet returned. This nonrecord has r/R approximately .383213969 and is retained.

A further implemented coordinate mechanism uses `x=(v+r|v|u)/2`, with0<r<1 and|u|=1, giving `x·(v-x)=|v|²(1-r²)/4>0`. Recursive tree coordinates enforce reference arrows identically, but actual centroid closure remains a three-equation finite constraint. Physical and polar SLSQP trials rebuilt actual mass and full opposite landscapes and found no110. Finite failures are not stationarity, optimality or family exclusions.

## Audit and recovery status

Exact code uses CPython3.13.5 standard library; numerical producers use NumPy2.3.5/SciPy1.17.0/Torch2.10.0+cpu, float64, one thread. Every finite geometry evaluation uses the actual filled physical centroid for both landscapes.

V hulls use exhaustive rational supporting triples and maximal coplanar polygons. H hulls use exhaustive plane intersections and positive-spanning boundedness. True edge ownership, tetrahedral and coordinate-divergence mass identities, stable feet, vertex cones and mixed edge segment/normal-cone conditions are checked directly. Additional weak equilibria are distinguished from primitive equalities. H is not inferred from Morse. This is one complete mechanics implementation with algebraic cross-checks and several mass routes, not two independent full hull auditors.

All22 inputs/audits were freshly regenerated in bounded cold-replay batches. A subsequent strict hash-matching aggregate regenerated radial graphs, all structural proofs and original-pin freezes. All44 input/audit receipts and7 proof receipts matched. Observed final marker: `STEADY_RAVEN_CONTINUATION_22_NEW_EXACT_BODIES_PASS 22`.

Selected audit receipts:

```text
C50_HARDTREE58_G5 987932 6220d79bc0b93f7a49c5ff974239a1c768a1b64fc4948f4d97e7366f13928620
C50_HARDTREE84_G5 1972555 6eae4ac040290d40516d1e3eb175266e446e1757c508edf4c2f02940c27e8251
C50_DUALBRIDGE23_G4 1968031 2dd34e80c174084a2275e8808f73bae1dc8431ace87626185b3ff7ee987ae515
C50_MONOV42_G4 417375 f2398354d1604b816647c926ee7df3f27435939a01d1c0b16ae5d3ff82750fca
C50_MONO44_G4 10718803 07d397f00905a689d0be8e42a542b1f7a627d50493a1941288e74156ccdf0a41
C50_MONO85_G4 60591279 4c66f08eab64913e366acc65655b441fe7b17729e60df25a345b66ef00e9728e
C50_TWOARM_REC71_G5 1515186 bdfaa498d5d0cdb4cd5b0922ea663d93c6de1a3b382dee5a5e537f5ef906d29e
C50_MONO23_TWO_CAPS 2578888 9917b436212e93eff826118422f121df573bae1cb9499e4657a1a964cfbd0a60
C50_WHOLEQ58_ALL_POINT_CELL.json 517111 dd154db0a1401e1968eaa99ec1dab10e3e217a17de6c73a3fabf73bf108f0920
PARTITION_CERTIFICATES.json 5278 8ea5454ee8bf5be7c0380d5df31d699d6869778b5a099d36c5794208159380c9
SOURCE_INDEXED_GRAPHS.json 26331 8ef85a7d24c2c607c59679a758a784f1347f8adcc71fe2d642350391075619da
```

## Most useful continuation

Do not repeat fixed-old-geometry WHOLEQ58 separator orientation/offset refinement: its full one-point cell is now closed against U1. Change protected vertices0/1, retained geometry, metric, partition or the number of added points. The finite retained-core/triangle gate gives a second concrete restriction to release.

MONO44 G4 is the most useful S1-first headroom entrance from this continuation: Q0,123 spare edges, complete P33/31. H23 offers P18/18 and186 spare edges but a deeper well and exact one-cap obstruction. MONO85 is the lower-depth zero-headroom alternative, not an unqualified preferred parent. Any cap must repair the newly transferred landscape at actual mass; deleting old packet vertices alone is insufficient.

HARDTREE58/84 preserve actual U1 with source-indexed guards and lower Q depth, but their new blocking intersections must be changed coherently. The two-arm DAG and58-bit S1 free-vertex companion are complementary resources. No general geometry, full-SPD or unrestricted mass-deformation exclusion is claimed.

## Complete recovery delivery

The complete self-contained handoff, including the entire literal82-unit recovery capsule, is preserved in the following generated files:

[Complete result JSON with inline recovery capsule](sandbox:/mnt/data/steady_raven_continuation_result.json)

[Complete result Markdown with inline recovery capsule](sandbox:/mnt/data/steady_raven_continuation_result_markdown.md)

[Standalone recovery script](sandbox:/mnt/data/RECOVER_STEADY_RAVEN_CONTINUATION.py)

[Sources and structural proofs](sandbox:/mnt/data/steady_raven_continuation_sources_and_proofs.zip)

The full capsule was created and tested, but its120591-byte literal decoder is **not reproduced inside this response's result_markdown**. Consequently, this response alone is not the requested download-independent complete handoff for all22 successors. The attached complete result JSON/Markdown contains that literal capsule; continuation must retain those bytes rather than treating the filenames or hashes below as replacements. The readable H23 halfspaces above recover that solid's geometry directly, but not the full audit/producer pack by themselves.

Capsule transport identities:

```text
Recovered units82
JSON dictionary301914 bytes
SHA25681085c8a1c90ff4419601c879ee10259392c81d44ab6e66aa3306c74119f3f68
XZ94900 bytes
SHA2562e5be522009a6d218181cecbb79db11794effb93182614bbbbc58c32db24447e
Base85 characters118625
Decoder120591 bytes
SHA25680be15ca29d33ea8187e95d78faa7e1c585825bccdba7145eb9fef5e1ac382cf
Archive873870 bytes
SHA25603e8c654fcea011861e6fd68a60d100839251b4b60bb7b32d706def3b83cdcd4
```

The decoder recovers all22 exact inputs, both parent inputs used by the proofs, complete original pins including inactive material rows,33 Python units, full mechanics/landscape generators and expected receipts. It requires no connector, numerical optimizer or historical archive for exact replay.

Commands:

```sh
python -B -S RECOVER_STEADY_RAVEN_CONTINUATION.py OUT
cd OUT
python -B -S RUN_EXACT.py all
```

Explicit body names permit bounded batches. `python -B -S RUN_EXACT.py resume` accepts cached audits only after byte-count/SHA matching, regenerates full radial graphs, and reruns structural proofs and original-pin freezes. Assertions must remain enabled. Large-integer string limits are disabled where required.

Expected markers:

```text
STEADY_RAVEN_CONTINUATION_SOURCE_RECOVERY_PASS82
CAP_AUDIT_CONTROLS_TETRA_CUBE_AFFINE_GRAM_THREE_MASSES_PASS
C50_WHOLEQ58_ALL_ORIENTATION_ONE_POINT_U_GE_2_PASS8[0,1]
TWO_REFERENCE_CHAMBERS_AND_FINITE_RETAINED_TRIANGLE_MASS_GATES_PASS
C50_MONO23_FIXED_OUTSIDE_CAP_NUMBER_EXACTLY_TWO_PASS18 24 20
STEADY_RAVEN_WHOLE_PACKET_AND_MASS_CERTIFICATES_PASS
ALL_22_ORIGINAL_PIN_OR_EXACT_PARENT_INPUTS_PASS22
STEADY_RAVEN_CONTINUATION_22_NEW_EXACT_BODIES_PASS22
```

Whitespace around printed counts follows ordinary Python print formatting. Optional numerical rediscovery is `python RUN_PRINCIPAL.py STAGE`; every stage and non-default argument is in the source. Set OMP_NUM_THREADS, OPENBLAS_NUM_THREADS and MKL_NUM_THREADS to1. Exact recovery is independent of optimizer rediscovery and no cross-platform bitwise optimization claim is made.
