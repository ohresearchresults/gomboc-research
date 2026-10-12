# figure-0289

AI research report · 2026-09-04 UTC · [Export notes](../../catalog/coverage.md#text-records)

---

# Clear Willow 25 — exact unpinched three-boundary M42 successor

## Research handoff

I worked only from corrected literal parent `figure-0281`, not the retracted HX2 alias. The durable journal resets the M42 frontier to the exact 124-supplied/97-active whole-basin annular cage and identifies an unpinched two-return successor as the next valid topology.  The literal parent payload ends with the exact `(97,271,176)`, strict `(2,1,1)` body, its closed `900024` basin, saddle `(900017,900032)`, and the requirement to replace the pinched forcing surface and saddle star together. 

I explored copy/split realizations of that whole forcing region, finite coordinate, projective, and deletion neighborhoods, and complete-hull mechanics at every promoted state. No strict `(1,1,0)` state was found. The strongest realizable topology was exactified instead of leaving it as a numerical nearstate: a 29-row copy/split replacement whose 21 active new rows form a connected positive-volume regular complex and whose parent-to-endpoint boundary exchange has three components.

**Disposition: EXACT NONWINNER.** At its exact ordinary-volume centroid, the promoted body has

```text
(S,U,H)=(2,2,2),
```

not `(1,1,0)`.

**Complete immutable archive:** [M42_slot1_Clear_Willow_25_unpinched_three_boundary_exact_complete.zip](sandbox:/mnt/data/M42_slot1_Clear_Willow_25_unpinched_three_boundary_exact_complete.zip)  
**Archive SHA-256:** `856d267cea5e21c2782b08032d7fe43d048b53fbdb52cb5f162472b662ec7fe8`  
**Checksum file:** [ZIP SHA-256](sandbox:/mnt/data/M42_slot1_Clear_Willow_25_unpinched_three_boundary_exact_complete.zip.sha256)  
**Readable report:** [README.md](sandbox:/mnt/data/M42_slot1_Clear_Willow_25_unpinched_three_boundary_exact_complete/README.md)  
**Machine summary:** [result_summary.json](sandbox:/mnt/data/M42_slot1_Clear_Willow_25_unpinched_three_boundary_exact_complete/result_summary.json)  
**Immutable manifest:** [MANIFEST.sha256](sandbox:/mnt/data/M42_slot1_Clear_Willow_25_unpinched_three_boundary_exact_complete/MANIFEST.sha256)  
**One-command replay:** [REPLAY.sh](sandbox:/mnt/data/M42_slot1_Clear_Willow_25_unpinched_three_boundary_exact_complete/REPLAY.sh)  
**Clean-room transcript:** [CLEANROOM_VERIFY.log](sandbox:/mnt/data/M42_slot1_Clear_Willow_25_unpinched_three_boundary_exact_complete/CLEANROOM_VERIFY.log)

## Literal source authority

The only parent used is

```text
result  figure-0281
payload SHA-256
        440ad55a0aaca60af257a763066a16e29355cd6cfc72d7106989d2410a6a341f
archive SHA-256
        8f390dae69ad2ea7fbb97f1cbe5c0616273b3b47654fed9e2315358c90d02cda
```

The bundled parent files have the exact hashes

```text
05d070dd3206f174bd4aa4a2ddb580c0065c1f944cca34acde0950ecd9f48e11  coordinates_exact.csv
913a5e2d62cdfc3d5a18cabfd037624cadaf8b4ec9250384ea7e797b4bd06303  face_cycles.json
89f68c55da6143433ef745197b4957f77b9a704f6d83238bc6e8c657f24944bf  true_edges.csv
6ad91c4caf424efac969364e9fb57c7e5a4d55565d2c6ba3d2f6b4c40ea64596  certificate.json
7fb7dc42217ce6d26178587c75c20f977acb9fade8d5dd30a51831e77e081bb1  forcing_surface_summary.json
```

`verify_literal_parent_identity.py` checks these bytes and the parent invariants: 124 supplied rows, 97 active vertices, `(V,E,F)=(97,271,176)`, class `(2,1,1)`, stable faces `[0..16]` and `[900005,900024,900031]`, unstable vertex `8`, and saddle `(900017,900032)`.

No retracted HX2, BIHEX27, or `65xx` label occurs in the construction.

## Deterministic exact source

`build_exact_source.py` performs the complete construction.

It starts from the literal parent’s 97 active rational rows; the parent’s 27 already-inactive supplied rows are omitted. It removes these 28 parent-active labels:

```text
900012,900005,900023,900030,900026,900024,900006,900007,
261,262,263,900027,900028,900011,900022,900002,900031,
900020,900021,900017,900032,900003,900014,900018,900019,
900000,900016,900033.
```

It inserts exact terminating-decimal copies according to

```text
900012->920000   900005->920001   900023->920002   900030->920003
900026->920004   900024->920005   900006->920006   900007->920007
261   ->920008   262   ->920009   263   ->920010   900027->920011
900028->920012   900011->920013   900022->920014   900002->920015
900031->920016   900020->920017   900021->920018   900017->920019
900032->920020   900003->920021   900014->920022   900018->920023
900019->920024   900000->920025   900016->920026   900033->920027.
```

Row `920100` is added as a second independently moved copy of parent pinch row `900022`. Fixed old rows retain their literal parent fractions. Moved old rows and all `920xxx` rows are interpreted as the exact terminating decimals in `discovery_source.json`.

The discovery source SHA-256 is

```text
0ad13b1f622ef921dd6ac0c7d29bf4399c4a464bbf0d4628598f4d599b7e5cbf.
```

The generated 98-row exact coordinate table has SHA-256

```text
db3605bacaeb7f7b999dc61dedecb244d2a262c70ef8962daa0886b1619602ec
```

and admits one common denominator

```text
3975069413063551296413828730421893974408282255740492698788470981829000000000000000000.
```

The common-lattice table has SHA-256

```text
1e4a7f5e3786e7b142e20812c46bb6648546bfd6e58a81ad8c653e5ca384379b.
```

## Complete actual hull and supplied-versus-active ledger

Fresh exact reconstruction from all supplied rows gives

```text
supplied rows       98
active vertices     89
true edges         247
maximal faces      160
Euler       89-247+160 = 2.
```

The nine supplied but inactive rows are exactly

```text
1014,920002,920004,920007,920008,920009,920010,920016,920019.
```

The 21 active new rows are

```text
920000,920001,920003,920005,920006,920011,920012,920013,
920014,920015,920017,920018,920020,920021,920022,920023,
920024,920025,920026,920027,920100.
```

Relative to the parent active hull, the removed or newly inactive active labels are

```text
261,262,263,1014,900000,900002,900003,900005,900006,900007,
900011,900012,900014,900016,900017,900018,900019,900020,
900021,900022,900023,900024,900026,900027,900028,900030,
900031,900032,900033.
```

The complete row ledger is in `supplied_active.csv`, all 160 exact maximal-face cycles are in `face_cycles.json`, exact supporting planes are in `face_planes_exact.json`, and all 247 true edges with their two incident maximal faces are in `true_edges.csv`.

The independent GMP verifier enumerates all

```text
C(98,3)=152096
```

triples and performs `2,850,609` exact support-sign checks, independently recovering the same 160 maximal faces and 89 active rows. The face-cycle SHA-256 is `1f4e51ca33319af297f07721302aa3f8ec6c69cb8bc9c9dbee8fd88b6ca501a6`; the true-edge SHA-256 is `5728d5d99ae81084494941b6826b52975b903617d4f55995c6ebdd31ca0fff86`.

## Exact ordinary volume, centroid, and first moments

The exact ordinary volume is

```text
106196777276817648845496156459272118643962616274053105404649636589693748914853249048117992154421231448156476559377616763
/
79501388261271025928276574608437879488165645114809853975769419636580000000000000000000000000000000000000000000000000
```

or approximately `1335.7851931819816`.

The exact unshifted ordinary-volume centroid is

```text
Cx = -62604427141455566613501922879613145410233762196406973294790771401957999487212787523294053197754886227510846769780434792577468706331939230177362368389939644760468564498902260460566825958567008885685563147
     /101313494668560051066052541809315500016635298510576483633778200223996992281346469462296293252924549272929463883285244459319048302335089155116810186593492334557260268985981571269287711886480000000000000000

Cy = 22425662202337627618745042755057311190303519655614247316471166833248182503569913450916868266303102902975120446022032864804039005376152321653881204257543970642140502521853979806199373346171105575265106391
     /3896672871867694271771251608050596154485973019637557062837623085538345856974864210088318971266328818189594764741740171512271088551349582889108084099749705175279241114845445048818758149480000000000000000

Cz = 29685330556081908353470815181622485819487940013064644184197051731697191170884417885886417087480162935542510895352834178210910494026285671286642706425083265464379424064248042837101547915243798772940834899
     /211069780559500106387609462102740625034656871897034340903704583799993733919471811379783944276926144318603049756844259290248017296531435739826687888736442363660958893720794940144349399763500000000000000000.
```

Numerically,

```text
C=(-0.6179278224116297,
    5.755079510071601,
    0.14064225810721245).
```

Exact signed-tetrahedron integration verifies

```text
M(P+tau)=M(P)+V tau.
```

Since `V>0`, translation by `tau=-C` is the unique ordinary-volume centring translation. Direct rational reintegration of the translated body gives

```text
Mx=My=Mz=0.
```

The endpoint certificate SHA-256 is `09aef5e14291f5e7a0ee2976245acea294f26c23464cad78cba4cfc5c189ae02`.

## Exhaustive exact own-centroid mechanics

Every maximal face, every complete incident-edge cone at every active vertex, and all four components `(t,1-t,beta1,beta2)` of every true-edge normal cone were recomputed exactly.

```text
(S,U,H)=(2,2,2).
```

The strict equilibria and raw positive-margin diagnostics are

```text
stable protected 17-gon [0..16]          10.149662582702808
stable extra [920005,900008,920011]        5.359473732251079

unstable protected vertex 8              276.8895000566191
unstable extra vertex 920006               3.7010363198132833e-6

saddle edge (248,920020)                    0.0018354514407676783
saddle edge (259,900008)                    2.631912878470236e-6.
```

Every other maximal face, vertex, and true edge has an exact negative witness. Strict lower-bound diagnostics include

```text
active face/nonincident support gap       7.897706355241275e-14
inactive supplied-row separation          5.204480205583941e-5
nonstable exclusion                       6.737038229720449e-6
nonunstable exclusion                     3.559562886055118e-6
nonsaddle exclusion                       8.750667867574716e-16.
```

The complete exact ledgers are `faces_mechanics_exact.json`, `vertices_mechanics_exact.json`, and `edges_mechanics_exact.json`.

## Literal death of the inherited packet

The inherited stable face `[900005,900024,900031]` is absent because all three parent labels are removed from the supplied set. The inherited saddle `(900017,900032)` is absent because both parent endpoints are removed. Both parent saddle faces

```text
[900032,900003,900017]
[900017,900018,900032]
```

are absent from the rebuilt actual hull.

This is endpoint-cell evidence, not a transported local ledger. It proves that the inherited pair dies and a different strict packet is present at the endpoint. I do not claim a continuous parent-to-endpoint death-before-birth chronology.

## Exact connected three-boundary replacement

The parent and endpoint share 53 maximal faces. Their differing surface portions are connected genus-zero surfaces with the same boundary-edge set and exactly three boundary cycles:

```text
removed parent surface    (V,E,F)=(79,203,123), chi=-1
inserted endpoint surface (V,E,F)=(71,179,107), chi=-1.
```

The three cycles are

```text
[250,251,6006,900013]

[230,231,232,1004,1003,1002,900001]

[8,246,245,244,243,10009,10008,10007,241,240,239,238,
 237,236,235,69,255,256,257,258,900008,13,12,900009,
 900010,264].
```

All 22 faces of the parent inclusion-minimal forcing surface are absent, as are both old saddle faces.

The parent pinch row `900022` is removed. Its two independently moved copies `920014` and `920100` are active, and `(920014,920100)` is a true edge. Thus the old pinch is genuinely split in the actual hull.

Rows `261,262` are removed. Their copies `920008,920009` are supplied but inactive, so the copied old diagonal is absent. The designated skip edge `(920007,920010)` is also absent.

The exact topology certificate has SHA-256 `93cffd3c36f2d16146c179c7fa4862836a84c6908b36ef1fb388c1abef0ceaa7` and independently replays with

```text
INDEPENDENT_EXACT_THREE_BOUNDARY_WHOLE_BASIN_REPLACEMENT_PASS.
```

## Positive-volume regular three-complex

The 21 active new rows have affine rank four. Exact squared-norm lifting produces a regular tetrahedral complex with

```text
50 tetrahedra
81 interior triangles
38 boundary triangles
no cospherical ties
connected tetrahedron-dual graph.
```

Their actual new-row true-edge graph is connected and has 32 mutual edges.

The exact complex volume is

```text
35242937418925855201045853748084198978178312927341
/
50000000000000000000000000000000000000000000000
```

or approximately `704.8587483785171`.

The regular-complex certificate SHA-256 is `986e00d6fa43c7cdd3925cfafc5dd0ace73e594ee8c78c2697cd1704024ac0da`. This is a physical full-dimensional connected replacement, not a supporting-face coincidence, serial sheet, inactive interpolation arc, or coordinate-only metric image.

## Complete external-arrow antibirth audit

Every one of the 247 true edges is audited exactly; 127 are absent from the parent edge set. The identity

```text
A(i->j)+A(j->i)=||X_i-X_j||^2>0
```

is checked on every edge.

Exactly three edges have all nonmutual external arrows strictly positive at both endpoints:

```text
(8,920013)
(8,920015)
(259,920006).
```

The first two are incident to protected unstable vertex `8`. The third is the adverse residual carrier: it forces one of `259,920006` to be unstable. Exact complete vertex-cone mechanics selects `920006`. Since `8` is independently unstable, this external-sign chamber has `U>=2`.

Every other true edge has an explicit nonpositive external witness at one endpoint. The audit SHA-256 is `ec357a03e1801a6f6127f79e51d2df3dee1f271a812564b23f8b79d5675e33b1`.

## Positive full-dimensional perturbation chamber

All three coordinates of each of the 21 active new rows vary independently by

```text
delta=2^-100=1/1267650600228229401496703205376.
```

Exact interval arithmetic preserves throughout this 63-dimensional Cartesian box:

```text
- the complete 98-row supplied set and 89-row active set;
- all 160 maximal faces and 247 true edges;
- positive ordinary volume and the unique own-centroid translation;
- exact class (2,2,2) and all six named equilibria;
- strict inactivity of all nine inactive supplied rows.
```

The box certificate SHA-256 is `fd597cecb10f4736a0259257c81f0361e5edd8d2ba45ac2a98169d76dbab37a7`.

## Exact residual connected forcing component

Row `920005`, copied from parent local-minimum row `900024`, remains a strict radial local minimum. Its complete true-edge neighbor set is

```text
N(920005)={256,900008,920000,920001,920003,920006,
           920011,920017,920018},
```

and every exact squared-radius gap from `920005` to those neighbors is positive.

The endpoint retains a strict descending true-edge route into the protected basin:

```text
920025 -> 69 -> 72 -> 14,
```

with exact squared-radius drops approximately

```text
3787.159913552047
1084.0625913700887
576.4216450464551.
```

The left residual packet is

```text
stable   [920005,900008,920011]
unstable 920006
saddle   (259,900008)
near transfer edge (900008,920006).
```

The four components of the near transfer edge have minimum

```text
-6.637757276715084e-9,
```

so it is a strict nonsaddle but lies close to a relay wall. The independent right residual saddle is `(248,920020)`.

The shortest dual-face route from the extra stable face to the left saddle has three faces; the route to the right saddle has fifteen faces. The residual certificate SHA-256 is `d4803f04c1e270a609722d2e93d564d1ef30b61029b40b4642da6bdf4a9bf835`.

A floating affine scan of row `920006`, retained only under `empirical_scope/`, shows a local U–H–U transfer. It is not used as an exact continuum theorem.

## Independent reconstruction and watertight meshes

Run from the archive root:

```bash
bash REPLAY.sh
```

The replay verifies the immutable manifest, checks literal parent byte identity, regenerates the exact source, reintegrates exact mass and mechanics, compiles and runs the GMP all-triples verifier, replays the three-boundary exchange, regular complex, external-arrow audit, `2^-100` box, residual forcing certificate, and mesh audit, and then rechecks every hash.

Expected terminal markers include


[Encoded source block omitted; the code in this passage is incomplete.]


The clean replay exits successfully. Its transcript SHA-256 is `0a289e787ca7585e935644bf3e40ae4cee46e72d58dabbd1326101ef2e1d1e50`.

`body.obj` has 89 vertices and 174 triangles. Its triangulated mesh has 261 edges, Euler characteristic two, and every edge has multiplicity two. The reconstructed volume is `1335.78519318198`, and the centroid norm is approximately `2.59e-14`. The binary STL has the same watertight combinatorics; its small mass drift is float32 export rounding.

```text
OBJ SHA-256  28ced73fe797a9afb5165391e3396e6fee1c763678df9dcf9ebb3b9c7e349d63
STL SHA-256  ca8d8e528db2ced1c116306b555a830fd06da87c2aee61eecd6be006ebe51762
```

## Exact scope

Exact claims cover the endpoint, its complete actual hull and mechanics, the full 63-dimensional endpoint chamber, literal parent-to-endpoint incidence comparison, connected regular complex, all-edge external arrows, residual forcing system, and watertight meshes.

I do **not** claim:

```text
- a continuous parent-to-endpoint path;
- a parent-to-endpoint death-before-birth chronology;
- an exclusion of every realization of the abstract three-boundary topology;
- a global impossibility theorem for unpinched whole-basin cages.
```

The endpoint-cell evidence establishes that the inherited pair is absent and a distinct strict packet is present. It therefore distinguishes transfer from annihilation without inventing a chronology that was not certified.

## Smallest genuinely unrepresented successor

The first nonrepeating successor must change the entire connected residual rather than move row `920006` alone across its adjacent relay wall. It must simultaneously:

```text
1. deactivate 920005 or destroy its complete nine-neighbor radial-minimum star;
2. deactivate one of {259,920006}, suppress the all-positive edge
   (259,920006), and cross the near wall (900008,920006) without selecting
   the opposite U-H carrier;
3. replace both incident faces of saddle (248,920020) and deactivate at
   least one saddle endpoint;
4. retain the split-pinch edge and three-boundary connectivity, or replace
   them by a strictly stronger shared-volume cell;
5. preserve the descending route into row 14 or 15 and protected U8;
6. retain, after the three ordinary-moment equations, independent controls
   for left basin death, U-H antibirth, right saddle death, and return timing.
```

A practical first architecture is a second unpinched return cell sharing a positive-volume tetrahedral interface with the present 21-row complex and spanning

```text
{920005,920006,259,900008,920011,248,920020,920024,920025}.
```

It must replace the complete local-minimum star and both saddle stars in one secondary-fan event. Another one-dimensional motion of `920006`, isolated cap, endpoint deletion, or surface-only relay repeats the certified transfer mechanism.

## Final conclusion

**EXACT UNPINCHED THREE-BOUNDARY NONWINNER.** The target `(1,1,0)` was not reached. The strongest promoted endpoint is a fully materialized exact 98-supplied-row body with actual `(V,E,F)=(89,247,160)`, exact positive volume, exact zero own-centred first moments, strict `(2,2,2)`, a connected three-boundary incidence replacement, a 21-row positive-volume regular complex, complete external-arrow control, a 63-dimensional strict chamber, independent reconstruction, and watertight OBJ/STL.

The old pinched forcing annulus and inherited stable–saddle pair are genuinely gone, but the packet transfers to a connected stable/unstable/two-saddle component. The decisive new obstruction is the all-positive edge `(259,920006)` coupled to the closed radial-minimum star at `920005`, together with independent right saddle `(248,920020)`.

## Direct artifact index

- [Exact deterministic source metadata](sandbox:/mnt/data/M42_slot1_Clear_Willow_25_unpinched_three_boundary_exact_complete/unpinched_three_boundary_endpoint/exact_source.json)
- [Exact source builder](sandbox:/mnt/data/M42_slot1_Clear_Willow_25_unpinched_three_boundary_exact_complete/unpinched_three_boundary_endpoint/build_exact_source.py)
- [Discovery source coordinates](sandbox:/mnt/data/M42_slot1_Clear_Willow_25_unpinched_three_boundary_exact_complete/unpinched_three_boundary_endpoint/discovery_source.json)
- [Complete exact coordinates](sandbox:/mnt/data/M42_slot1_Clear_Willow_25_unpinched_three_boundary_exact_complete/unpinched_three_boundary_endpoint/coordinates_exact.csv)
- [Common integer lattice](sandbox:/mnt/data/M42_slot1_Clear_Willow_25_unpinched_three_boundary_exact_complete/unpinched_three_boundary_endpoint/coordinates_common_lattice.csv)
- [Endpoint certificate](sandbox:/mnt/data/M42_slot1_Clear_Willow_25_unpinched_three_boundary_exact_complete/unpinched_three_boundary_endpoint/certificate.json)
- [All maximal-face cycles](sandbox:/mnt/data/M42_slot1_Clear_Willow_25_unpinched_three_boundary_exact_complete/unpinched_three_boundary_endpoint/face_cycles.json)
- [All true edges](sandbox:/mnt/data/M42_slot1_Clear_Willow_25_unpinched_three_boundary_exact_complete/unpinched_three_boundary_endpoint/true_edges.csv)
- [Three-boundary exchange certificate](sandbox:/mnt/data/M42_slot1_Clear_Willow_25_unpinched_three_boundary_exact_complete/unpinched_three_boundary_endpoint/three_boundary_exchange_certificate.json)
- [Positive-volume regular-complex certificate](sandbox:/mnt/data/M42_slot1_Clear_Willow_25_unpinched_three_boundary_exact_complete/unpinched_three_boundary_endpoint/inserted_regular_complex.json)
- [All-edge external-arrow audit](sandbox:/mnt/data/M42_slot1_Clear_Willow_25_unpinched_three_boundary_exact_complete/unpinched_three_boundary_endpoint/external_arrow_audit.json)
- [Exact 63-dimensional box certificate](sandbox:/mnt/data/M42_slot1_Clear_Willow_25_unpinched_three_boundary_exact_complete/unpinched_three_boundary_endpoint/full_63d_box_certificate.json)
- [Residual forcing certificate](sandbox:/mnt/data/M42_slot1_Clear_Willow_25_unpinched_three_boundary_exact_complete/unpinched_three_boundary_endpoint/residual_forcing_certificate.json)
- [Independent GMP hull verifier](sandbox:/mnt/data/M42_slot1_Clear_Willow_25_unpinched_three_boundary_exact_complete/unpinched_three_boundary_endpoint/verify_exact_hull_gmp.cpp)
- [Independent exact endpoint verifier](sandbox:/mnt/data/M42_slot1_Clear_Willow_25_unpinched_three_boundary_exact_complete/unpinched_three_boundary_endpoint/verify_exact_endpoint.py)
- [Watertight OBJ](sandbox:/mnt/data/M42_slot1_Clear_Willow_25_unpinched_three_boundary_exact_complete/unpinched_three_boundary_endpoint/body.obj)
- [Watertight STL](sandbox:/mnt/data/M42_slot1_Clear_Willow_25_unpinched_three_boundary_exact_complete/unpinched_three_boundary_endpoint/body.stl)
