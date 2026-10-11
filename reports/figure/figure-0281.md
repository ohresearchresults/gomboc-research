# figure-0281

Historical AI scientific report · saved 2026-09-04 UTC. Claims below retain their original status and have not all been independently checked. The current retained construction is C622; the C<500 search remains open.

Public text derivative: internal-record-identifiers-replaced; unreviewed-encoded-blocks-omitted.

---

# Clear Willow 25 — exact whole-basin annular cage

## Final disposition

**EXACT NONWINNER.** I did not obtain the requested homogeneous convex polyhedral Gömböc. The promoted finite body is an exact rational/dyadic uniform-density convex polyhedron evaluated at its own exact ordinary-volume centroid, but its strict equilibrium class is `(S,U,H)=(2,1,1)`, not `(1,1,0)`. The acceptance gate remains the literal finite own-centred object with complete H/V/E and full-normal-cone certification. :contentReference[oaicite:0]{index=0}

This continuation realizes the first full-dimensional whole-basin cage beyond the immutable parent. It removes the parent residual stable face `[10014,257,200001]` and saddle edge `(7003,200002)`, replaces a complete two-boundary annular portion of the hull by a larger connected annulus, and inserts a 32-vertex rank-four positive-volume regular complex. The Morse pair transfers to stable face `[900005,900024,900031]` and saddle edge `(900017,900032)`.

**Complete immutable archive:** [M42_slot1_Clear_Willow_25_whole_basin_cage_exact_complete.zip](sandbox:/mnt/data/M42_slot1_Clear_Willow_25_whole_basin_cage_exact_complete.zip)  
**Archive SHA-256:** `8f390dae69ad2ea7fbb97f1cbe5c0616273b3b47654fed9e2315358c90d02cda`  
**Checksum file:** [ZIP SHA-256](sandbox:/mnt/data/M42_slot1_Clear_Willow_25_whole_basin_cage_exact_complete.zip.sha256)  
**Readable report:** [README.md](sandbox:/mnt/data/M42_slot1_Clear_Willow_25_whole_basin_cage_exact_complete/README.md)  
**Machine summary:** [result_summary.json](sandbox:/mnt/data/M42_slot1_Clear_Willow_25_whole_basin_cage_exact_complete/result_summary.json)  
**Immutable file manifest:** [MANIFEST.sha256](sandbox:/mnt/data/M42_slot1_Clear_Willow_25_whole_basin_cage_exact_complete/MANIFEST.sha256)  
**One-command replay:** [REPLAY.sh](sandbox:/mnt/data/M42_slot1_Clear_Willow_25_whole_basin_cage_exact_complete/REPLAY.sh)  
**Clean-room transcript:** [CLEANROOM_VERIFY.log](sandbox:/mnt/data/M42_slot1_Clear_Willow_25_whole_basin_cage_exact_complete/CLEANROOM_VERIFY.log)

A clean extraction recompiles the independent GMP verifier, reconstructs every exact certificate, checks every packaged hash, and ends with `CLEANROOM_WHOLE_BASIN_CAGE_EXACT_REPLAYS_PASS`.

## Exact source authority and deterministic construction

The literal source authority is parent result `figure-0278`, payload SHA-256

```text
4ff76111c3b340258161a0b4502dbfea8001a8a2d78c8f087d11cefdde6f401f
```

and immutable parent archive SHA-256

```text
5cd46ab50dcb55ad6a8ae3d05ac21444ea13d27ae951ced60c365bd255a5d58a.
```

No conflict was found between that immutable payload and the journal summary. The parent is the exact 96-supplied/89-active full-basin endpoint with `(V,E,F)=(89,247,160)`, protected stable 17-gon `[0..16]`, protected unstable vertex `8`, extra stable `[10014,257,200001]`, and saddle `(7003,200002)`. :contentReference[oaicite:1]{index=1}

The endpoint's finite source is [discovery_source.json](sandbox:/mnt/data/M42_slot1_Clear_Willow_25_whole_basin_cage_exact_complete/whole_basin_cage_endpoint/discovery_source.json). [rebuild_exact_source.py](sandbox:/mnt/data/M42_slot1_Clear_Willow_25_whole_basin_cage_exact_complete/whole_basin_cage_endpoint/rebuild_exact_source.py) interprets every recorded finite decimal literally as a rational number and then projects rows `0..16` exactly onto the rational plane through rows `0,1,2`. It deterministically regenerates [coordinates_exact.csv](sandbox:/mnt/data/M42_slot1_Clear_Willow_25_whole_basin_cage_exact_complete/whole_basin_cage_endpoint/coordinates_exact.csv), SHA-256

```text
05d070dd3206f174bd4aa4a2ddb580c0065c1f944cca34acde0950ecd9f48e11,
```

the 282-bit common-denominator integer lattice, and [construction.json](sandbox:/mnt/data/M42_slot1_Clear_Willow_25_whole_basin_cage_exact_complete/whole_basin_cage_endpoint/construction.json).

Relative to the parent supplied set, these six rows are removed:

```text
7003, 10013, 10014, 10015, 10017, 200002.
```

Rows `900000..900033` are newly supplied. New rows `900025` and `900029` are strictly inactive; the other 32 are actual extreme vertices:

```text
900000,900001,900002,900003,900004,900005,900006,900007,
900008,900009,900010,900011,900012,900013,900014,900015,
900016,900017,900018,900019,900020,900021,900022,900023,
900024,900026,900027,900028,900030,900031,900032,900033.
```

The parent active rows deactivated by the operation are

```text
228,249,260,6004,6007,6009,7000,7003,7004,7005,
10005,10010,10012,10013,10014,10015,10017,10018,
10019,10020,10021,200001,200002,200004.
```

The 65 retained parent active rows and every supplied-versus-active flag are recorded in [annular_exchange_certificate.json](sandbox:/mnt/data/M42_slot1_Clear_Willow_25_whole_basin_cage_exact_complete/whole_basin_cage_endpoint/annular_exchange_certificate.json) and [supplied_active.csv](sandbox:/mnt/data/M42_slot1_Clear_Willow_25_whole_basin_cage_exact_complete/whole_basin_cage_endpoint/supplied_active.csv).

## Complete actual hull

Fresh reconstruction from all 124 supplied rows gives

```text
active vertices       97
true edges           271
maximal faces        176
Euler        97-271+176 = 2.
```

The 27 inactive supplied rows are exactly

```text
228,249,260,6004,6007,6009,7000,7004,7005,
10000,10001,10002,10004,10005,10006,10010,10012,10016,
10018,10019,10020,10021,200001,200003,200004,900025,900029.
```

The complete 176 maximal-face cycles are in [face_cycles.json](sandbox:/mnt/data/M42_slot1_Clear_Willow_25_whole_basin_cage_exact_complete/whole_basin_cage_endpoint/face_cycles.json), SHA-256

```text
913a5e2d62cdfc3d5a18cabfd037624cadaf8b4ec9250384ea7e797b4bd06303,
```

and all 271 true edges, with their two incident maximal faces, are in [true_edges.csv](sandbox:/mnt/data/M42_slot1_Clear_Willow_25_whole_basin_cage_exact_complete/whole_basin_cage_endpoint/true_edges.csv), SHA-256

```text
89f68c55da6143433ef745197b4957f77b9a704f6d83238bc6e8c657f24944bf.
```

The independent C++/GMP verifier enumerates all `C(124,3)=310124` point triples, finds every triple nondegenerate, performs 6,604,347 exact support-sign checks, and independently recovers 176 maximal supporting zero sets and 97 active rows. No triangulation diagonal is treated as a true edge.

## Exact ordinary volume, centroid, and first moments

The exact ordinary volume is

```text
32045224102916564076492088461390268126020042419826541971112071965375888863539097315741065003903182683659357768890793281
/
23850416478381307778482972382531363846449693534442956192730825890974000000000000000000000000000000000000000000000000
```

or approximately `1343.5918040241881`.

The exact unshifted centroid is

```text
Cx = -82708457904495294653398610144076382551821242191477997530438529769535927672345829035205531515221427632769560898851808762538347389063860147646886662530769918421795452591191048130635449423888157879533776617
     /127381990166270513487130312612885839604400991963341113983421347475762493873967246363078490154029858189362076328419552118755337281239477361739651937639543138581577573628864788548746290949000000000000000000

Cy = 142558771195901644926212131472791240355971417932044742140108817934026304896319234767022629396077142600789513920794549811369625123462953767772724272560574084491109486568362465469251177013079371602629945899
     /25476398033254102697426062522577167920880198392668222796684269495152498774793449272615698030805971637872415265683910423751067456247895472347930387527908627716315514725772957709749258189800000000000000000

Cz = 86264482715807087424662949820767448745622398193933921716735169425360514342939230753826799008685310519429565930287664383024827963994296102282437247501204284617702187506612657261142246686508846113827405517
     /636909950831352567435651563064429198022004959816705569917106737378812469369836231815392450770149290946810381642097760593776686406197386808698259688197715692907887868144323942743731454745000000000000000000.
```

Numerically,

```text
C = (-0.6492947534933057,
      5.5957192617975675,
      0.13544219650392786).
```

Exact signed-tetrahedron integration verifies `M(P+tau)=M(P)+V tau`. Since `V>0`, `tau=-C` is the unique ordinary-volume centring translation. Direct reintegration of the translated exact body gives

```text
Mx = My = Mz = 0
```

as rational identities. The exact own-centred coordinates are in [coordinates_own_centered_exact.csv](sandbox:/mnt/data/M42_slot1_Clear_Willow_25_whole_basin_cage_exact_complete/whole_basin_cage_endpoint/coordinates_own_centered_exact.csv).

## Exhaustive exact equilibrium audit

Every maximal face, every complete incident-edge cone at every active vertex, and all four components `(t,1-t,beta1,beta2)` of every true-edge normal cone were recomputed over exact rational arithmetic.

```text
(S,U,H) = (2,1,1).
```

The strict critical features and raw-margin diagnostics are

```text
protected stable 17-gon [0..16]       9.972056478994864
replacement stable [900005,900024,900031]
                                      0.5028937549315499
protected unstable vertex 8           278.59100987810285
replacement saddle (900017,900032)    0.07642021494664553
```

Every other maximal face has an exact negative witness; the minimum exclusion magnitude is `8.223550218992544e-5`. Every other active vertex has an exact negative incident-edge witness; the minimum exclusion magnitude is `0.20137594202493334`. Every other true edge has an exact negative component; the minimum exclusion magnitude at the point is `7.572556936009804e-4`.

The saddle's four exact-positive component diagnostics are

```text
(0.9235797850533545,
 0.07642021494664553,
 0.11062172901339508,
 805.4940111159056).
```

The full exact ledgers are [faces_mechanics_exact.json](sandbox:/mnt/data/M42_slot1_Clear_Willow_25_whole_basin_cage_exact_complete/whole_basin_cage_endpoint/faces_mechanics_exact.json), [vertices_mechanics_exact.json](sandbox:/mnt/data/M42_slot1_Clear_Willow_25_whole_basin_cage_exact_complete/whole_basin_cage_endpoint/vertices_mechanics_exact.json), and [edges_mechanics_exact.json](sandbox:/mnt/data/M42_slot1_Clear_Willow_25_whole_basin_cage_exact_complete/whole_basin_cage_endpoint/edges_mechanics_exact.json). The endpoint certificate is [certificate.json](sandbox:/mnt/data/M42_slot1_Clear_Willow_25_whole_basin_cage_exact_complete/whole_basin_cage_endpoint/certificate.json), SHA-256 `6ad91c4caf424efac969364e9fb57c7e5a4d55565d2c6ba3d2f6b4c40ea64596`.

The parent stable `[10014,257,200001]` is absent because row `10014` is not supplied. Parent saddle `(7003,200002)` is absent because both endpoint labels are not supplied. Their disappearance is established from the rebuilt actual hull, not a local assumed ledger.

## Connected positive-volume whole-basin replacement

The parent and endpoint share 39 maximal faces. Their differing portions are exact connected annuli with the same two boundary cycles:

```text
removed parent annulus    (V,E,F)=(77,198,121), chi=0
inserted endpoint annulus (V,E,F)=(85,222,137), chi=0
boundary-cycle lengths    4 and 29.
```

The cycles are

```text
[231,232,1004,1003]

[8,246,245,244,243,10009,10008,10007,241,240,239,238,237,
 236,235,69,255,256,257,258,72,73,14,13,12,11,10,9,264].
```

All 32 active new rows form one connected actual true-edge graph with 65 mutual true edges. Their affine rank is four. Exact squared-norm lifting gives a regular complex with

```text
87 tetrahedra
144 interior triangles
no cospherical ties
connected tetrahedron-dual graph.
```

Its exact positive volume is

```text
12710997119796091636931309377972252766177107258645211
/
15000000000000000000000000000000000000000000000000
```

or approximately `847.3998079864061`. This is a physical full-dimensional incidence replacement, not a supporting-face coincidence, inactive arc, serial sheet relay, or coordinate-only metric image. The exact regular data are in [inserted_regular_complex.json](sandbox:/mnt/data/M42_slot1_Clear_Willow_25_whole_basin_cage_exact_complete/whole_basin_cage_endpoint/inserted_regular_complex.json), SHA-256 `a9fcb0a36d06b038590313f26b3adf4eec766067c0900c6401e58d3f1ed17cd3`.

## Complete changed-carrier antibirth audit

[external_arrow_audit.json](sandbox:/mnt/data/M42_slot1_Clear_Willow_25_whole_basin_cage_exact_complete/whole_basin_cage_endpoint/external_arrow_audit.json), SHA-256 `3702956ee53e1c415efc11fd51bf777769aa4b3163fcd8c1c838997bd1ce71f3`, audits all 271 true edges; 171 are new or star-changed relative to the parent.

For every true edge `(i,j)`, the verifier checks exactly

```text
A(i->j)+A(j->i)=||X_i-X_j||^2>0.
```

The only edges whose two endpoints both have all nonmutual external arrows positive are `(8,246)` and `(8,900011)`, both incident to protected unstable vertex `8`. Every nonprotected new or star-changed edge has an explicit nonpositive external witness. The endpoint failure is therefore not an unaudited exposed positive-arrow source.

## Positive 96-dimensional chamber

All three coordinates of every one of the 32 new active rows vary independently by

```text
delta = 2^-80 = 1/1208925819614629174706176.
```

Exact interval propagation certifies, throughout this Cartesian 96-dimensional box:

```text
- the same 124 supplied rows and 97 active vertices;
- the same 176 maximal faces and 271 true edges;
- positive volume and valid unique ordinary-centroid translation;
- exactly the same class (2,1,1);
- the same two stable faces, unstable vertex 8, and saddle edge;
- all 27 inactive rows remain strictly inactive.
```

The smallest raw interval lower bounds include

```text
facet support          7.897706355241275e-14
inactive support       7.252168896222254e-11
nonstable witness      8.223550218992537e-5
nonunstable witness    0.20137594202493334
positive saddle term   2.3721462134051785e-4
nonsaddle witness      4.960120566952274e-15.
```

The exact certificate is [full_96d_box_certificate.json](sandbox:/mnt/data/M42_slot1_Clear_Willow_25_whole_basin_cage_exact_complete/whole_basin_cage_endpoint/full_96d_box_certificate.json), SHA-256 `10a5ab47e940162be8a55c560c3b859f4a98fb52d20487c52a428010f89ece96`. This is an open full-dimensional nonwinner chamber, not a wall point.

## Exact residual forcing component

Row `900024` is a strict radial local minimum at the exact own centroid. Its complete true-edge neighbour set is

```text
N(900024)={900005,900006,900023,900026,900031}.
```

Every exact squared-radius gap `||X_j||^2-||X_900024||^2` is positive; decimal diagnostics are

```text
900005   7918.348002030515
900006   8426.379773275772
900023      2.3030766330194052
900026     20.323333126016593
900031   2816.0149810361604.
```

A separate protected-basin route remains strictly descending at the endpoint's own centroid:

```text
257 -> 256 -> 69 -> 72 -> 14.
```

The residual saddle `(900017,900032)` has incident faces

```text
[900032,900003,900017]
[900017,900018,900032]
```

and endpoint stars

```text
N(900017)={900003,900014,900018,900019,900032}
N(900032)={900000,900003,900016,900017,900018,900033}.
```

The old diagonal `(261,262)` remains a true edge, incident to `[261,900009,262]` and `[900026,261,262]`.

The exact certificates are [basin_saddle_certificate.json](sandbox:/mnt/data/M42_slot1_Clear_Willow_25_whole_basin_cage_exact_complete/whole_basin_cage_endpoint/basin_saddle_certificate.json), SHA-256 `49bc3bf13c79994b700a524dff87ee0a97b7ddb51611cf2c673b6d3d9ae22e34`, and [residual_forcing_certificate.json](sandbox:/mnt/data/M42_slot1_Clear_Willow_25_whole_basin_cage_exact_complete/whole_basin_cage_endpoint/residual_forcing_certificate.json), SHA-256 `52c65ab6ffecd3ef2c7ca0b3f5e6622f691103b268f365687ff2ec8c57096c8b`.

## Exact no-reference-centre theorem for the fixed complex

A separate exact DPLL/Farkas certificate proves a stronger obstruction than failure at the ordinary centroid:

> For this fixed 97-vertex face lattice, no interior reference point can make `[0..16]` the only stable maximal face while retaining vertex `8` as unstable.

The proof contains 322 DPLL nodes, 215 leaves, maximum depth 14, and 22 branching faces. Each leaf supplies four exact nonnegative rational dual multipliers whose weighted affine coefficient vector is the strict-margin objective `(0,0,0,1)` and whose weighted constant is nonpositive. Hence no positive common strict margin exists.

The 22 inclusion-minimal forcing faces are

```text
[900012,900005,900023]
[900012,900023,900030]
[900026,900030,900023]
[900026,900023,900024]
[900023,900005,900024]
[900024,900006,900026]
[261,900026,900007]
[900026,262,263]
[900026,263,900027]
[900027,263,900028]
[900028,263,900011]
[900028,900011,900022]
[900002,900022,900011]
[900011,8,900002]
[900026,261,262]
[900026,900006,900007]
[900024,900005,900031]
[900006,900024,900031]
[900020,900030,900026]
[900022,900026,900027]
[900020,900026,900021]
[900021,900026,900022].
```

They form a connected triangulated pinched annulus with

```text
(V,E,F)=(20,42,22), chi=0,
18 boundary edges,
boundary-cycle lengths 3 and 15,
pinch vertex 900022.
```

The boundary cycles are

```text
[900022,900027,900028]

[900002,8,900011,263,262,261,900007,900006,900031,
 900005,900012,900030,900020,900021,900022].
```

The cover is inclusion-minimal: for every one of its 22 faces, an exact dyadic witness centre makes that omitted face strict while supplying strict non-equilibrium witnesses for all retained cover faces. The proof files are [exact_center_obstruction.json](sandbox:/mnt/data/M42_slot1_Clear_Willow_25_whole_basin_cage_exact_complete/whole_basin_cage_endpoint/fixed_complex_no_center_faces/exact_center_obstruction.json), SHA-256 `438271cc2b23938331f36dfa6b357c894f47a7487604994ef246cb92319b1c19`, [forcing_surface_summary.json](sandbox:/mnt/data/M42_slot1_Clear_Willow_25_whole_basin_cage_exact_complete/whole_basin_cage_endpoint/fixed_complex_no_center_faces/forcing_surface_summary.json), and [cover_irredundancy_witnesses.json](sandbox:/mnt/data/M42_slot1_Clear_Willow_25_whole_basin_cage_exact_complete/whole_basin_cage_endpoint/fixed_complex_no_center_faces/cover_irredundancy_witnesses.json).

This theorem is exact but scoped to the fixed incidence complex. It does not exclude a topology-changing successor.

## Chronology scope

I do **not** claim a continuous exact parent-to-endpoint path. The annular certificate establishes the two exact endpoint complexes, literal death of the parent carriers, connected same-boundary incidence replacement, and strict birth of the replacement pair. It does not order every intermediate circuit crossing.

The `2^-80` chamber certifies every possible equilibrium feature throughout the promoted endpoint neighbourhood: no additional stable, unstable, or saddle feature appears there, and the replacement pair remains strict. The endpoint is therefore a fully certified finite nonwinner, but not a successful death-before-birth cancellation chronology.

## Independent reconstruction and watertight meshes

The independent replay produces these terminal markers:


[An encoded source block is omitted from this text export pending a complete content review. This passage is not a complete executable package.]


The [OBJ](sandbox:/mnt/data/M42_slot1_Clear_Willow_25_whole_basin_cage_exact_complete/whole_basin_cage_endpoint/body.obj), SHA-256 `e7dcb9c610eea673db936345c2546606b7357257cf63146397b633563d42a2c5`, has 97 vertices, 190 triangles, 285 triangulated edges, Euler characteristic two, and every edge multiplicity two. Its reconstructed volume is `1343.5918040241852` and centroid norm `7.17e-15`.

The [binary STL](sandbox:/mnt/data/M42_slot1_Clear_Willow_25_whole_basin_cage_exact_complete/whole_basin_cage_endpoint/body.stl), SHA-256 `95c93d303559df8164a6cec888d85cebe94519222eaac890f9c2c6b0da25c7eb`, has identical watertight combinatorics. Its small mass drift is the expected float32 export effect.

## Empirical continuation work

A further nonexhaustive macro search completed 3,073 full-hull evaluations from this cage. It found no `(1,1,0)` body. Its best state remained `(2,1,1)`, retained both the copied low endpoint and saddle endpoint, and retained edge `(261,262)`. The ledger and reproducible driver are packaged under `empirical_search/`.

This is finite discovery evidence only. It is not a continuum exclusion and is not used in the exact theorem above.

## Smallest genuinely unrepresented successor

The inserted 32-row interior is already connected, positive-volume, regular, and highly actuated. The exact no-centre proof shows that the remaining obstruction is the **entire pinched forcing surface plus the complete saddle star**, not merely the local-minimum triangle.

The first nonrepeating successor is an **unpinched two-return whole-basin cage**—equivalently, a three-boundary regular 3-ball or two overlapping annular cages with a shared positive-volume interior. In one actual incidence event it must:

```text
1. make 900024 nonextreme, or destroy its complete five-neighbour closed star;
2. split, remove, or retopologize pinch vertex 900022;
3. cross both forcing-boundary cycles rather than attaching another single sheet;
4. remove edge (261,262) while preventing a 260-263 skip carrier;
5. replace both saddle faces
     [900032,900003,900017]
     [900017,900018,900032];
6. deactivate at least one of 900017,900032 and block every return through
   their complete endpoint stars;
7. preserve a strictly descending actual edge route to row 14 or 15;
8. assign an exact nonpositive external arrow to every nonprotected new or
   star-changed edge before moment closure;
9. retain, after the three ordinary-moment equations, independent controls
   for basin death, pinch separation, saddle death, and antibirth timing.
```

The continuation-critical saddle-star sets are

```text
{900003,900014,900018,900019,900032}
{900000,900003,900016,900017,900018,900033}.
```

A practical first model is a higher-valence double-annular cell spanning the 22 forcing faces and both saddle faces, with coordinated motion or deactivation of rows `261,262` and one saddle endpoint. Eight to twelve additional extreme supports may be enough, but this is a construction scale, not a proved lower bound. Another local carrier insertion, one-return sheet, isolated cap, fixed-reference-point search, or coordinate-only metric/projective image lies inside a mechanism already closed by the exact endpoint and no-centre certificate.

## Final conclusion

**EXACT WHOLE-BASIN ANNULAR-CAGE NONWINNER.** The strict own-centred `(1,1,0)` target was not reached. The strongest promoted successor is a fully materialized exact 124-supplied-row body with actual `(V,E,F)=(97,271,176)`, exact positive volume, exact zero own-centred first moments, strict `(2,1,1)`, a connected 137-face inserted annulus, a 32-row positive-volume regular complex, complete changed-edge antibirth control, a full 96-dimensional strict chamber, independent reconstruction, and watertight OBJ/STL.

Its failure is exact and sharply localized: row `900024` remains a closed radial minimum, saddle `(900017,900032)` remains strict, and an inclusion-minimal 22-face pinched annular forcing surface proves that no choice of reference point can rescue the fixed complex. The next topology must unpinch and replace that whole forcing surface and saddle star together.
