# figure-0278

AI research report · 2026-09-03 UTC

---

# Clear Willow 25 — exact full-basin transfer endpoint

## Disposition

**EXACT NONWINNER.** No homogeneous convex polyhedral Gömböc was obtained.

This continuation promotes a new exact rational M42 descendant beyond the immutable twelve-support `(69,187,120),(2,1,1)` parent retained by the immediate journal. The old residual stable face `[258,259,6301]`, old saddle `(248,6310)`, rows `6300..6311`, and route row `1026` are absent. A complete 65-face parent boundary disk is replaced by a connected 105-face disk with the same 33-edge boundary. The endpoint preserves the protected 17-gon `[0..16]` and protected unstable vertex `8`, and contains a strict descending true-edge route `257→256→69→72→14` into the protected-base basin.

The pair transfers rather than cancels. The exact endpoint has replacement stable face `[10014,257,200001]`, replacement saddle `(7003,200002)`, and strict own-centred class `(S,U,H)=(2,1,1)`.

**Archive:** M42_slot1_Clear_Willow_25_full_basin_transfer_exact_final.zip  
**SHA-256:** `5cd46ab50dcb55ad6a8ae3d05ac21444ea13d27ae951ced60c365bd255a5d58a`  
**Readable report:** README.md  
**Clean extraction replay:** CLEAN_EXTRACTION_VERIFY.log  
**Manifest:** MANIFEST.sha256

## Exact deterministic source

The source has 96 labelled rows. `discovery_source.json` stores the decimal discovery state. rebuild_exact_source.py interprets every decimal as its exact finite decimal rational and exactly projects rows `0..16` onto the rational plane through rows `0,1,2`; it reproduces coordinates_exact.csv, SHA-256 `029d57e26b8940fc75be696bc34e296ab6df5b8799806a870c76ed3d74d6c6bb`.

The supplied but inactive rows are exactly

```text
10000,10001,10002,10004,10006,10016,200003.
```

All other supplied rows are actual vertices. The full active ledger, exact own-centred coordinates, and 695-bit common integer lattice are packaged.

## Complete all-supplied hull

An independently compiled GMP verifier enumerates all `C(96,3)=142880` triples and performs `2781219` exact support-sign checks. It reconstructs

```text
supplied rows       96
active vertices     89
true edges         247
maximal faces      160
Euler        89-247+160 = 2
face sizes          159 triangles and one 17-gon.
```

All maximal faces (`face_cycles.json`), SHA-256 `7d8d8d91d75b84be29f78f7e8a76aaf0d8e4f6832ed554ce9c7a154d8ea96616`; all true edges (`true_edges.csv`), SHA-256 `3300003e6384f3ab98158a6dadef4b4f421c2326e432f2a0ab3b39e623213a76`; exact supporting planes and supplied/active data are adjacent.

The minimum exact raw active nonincidence gap is

```text
11998842464487379591558240360671/
400000000000000000000000000000000000000000000 > 0,
```

and the minimum exact inactive separation is

```text
190439459181713708818340543568939309/
50000000000000000000000000000000000000000000 > 0.
```

## Exact mass and own centroid

```text
V = 3367609597298886178945804581377138706937567758191520878948177538366849973026844934703582077097942386170211148510290832301/2518412318438969494963671193559920991725616882940341695618155444620320000000000000000000000000000000000000000000000000
  ≈ 1337.1954912396113.
```

The exact uncentred ordinary-volume centroid is

```text
Cx = -1015711152996573657866645982654753911678764886497217309878774693624625410710672899396756492728930674693107818858452714276691452802526361464306897913042787210489931094628535683329152022215178607615475982563371/1590193030037027318418407007181746626391821200366027162571795896041023419352461013987827052225206605618099764385312334249023642302230363388404203385266498770880387138959482096698338575679310000000000000000000
Cy = 1839890214965096279510361400982553609781857035936943140831139577426857999669477288524511141933345923742270810666452576958398758092685349337741419961319701519000025304698613547279339829118394764992952954428639/31803860600740546368368140143634932527836424007320543251435917920820468387049220279756541044504132112361995287706246684980472846044607267768084067705329975417607742779189641933966771513586200000000000000000000
Cz = -328539936080524866553460555435248332870760333528570734718020165481996963644918481393805231297431127312706953003045015259717133137778790650227738993835709590839191716851413323100852957813231203237159542020023/19877412875462841480230087589771832829897765004575339532147448700512792741905762674847838152815082570226247054816404178112795528777879542355052542315831234636004839236993526208729232195991375000000000000000000
```

approximately `(-0.63873450191950787,0.057851159582879536,-0.016528304671181958)`. Translation by `-C` is the unique moment closure because `M(P+τ)=M(P)+Vτ`, and exact reintegration gives `Mx=My=Mz=0`.

## Exhaustive exact equilibrium audit

Every maximal face, every complete incident-edge vertex cone, and all four components `(t,1-t,β1,β2)` of every true-edge cone were recomputed exactly at the own centroid:

```text
stable  [0..16]                 raw minimum ≈ 9.87988472584254
stable  [10014,257,200001]      raw minimum ≈ 4.108282073854557
unstable vertex 8               raw minimum ≈ 279.8964553160439
saddle  (7003,200002)           four-component minimum ≈ 0.005258216819378924
```

Every other feature has an exact negative witness. Complete ledgers are faces (`faces_mechanics_exact.json`), vertices (`vertices_mechanics_exact.json`), and edges (`edges_mechanics_exact.json`). The endpoint certificate SHA-256 is `723560d6441a35e953c0f9c5bb762363ef80b4ddaeb925b6305a01b84c501208`.

## Connected disk exchange and regular carrier

The two exact endpoint lattices have 55 common maximal-face labels. Their noncommon portions are connected disks:

```text
removed parent disk     (V,E,F)=(50,114,65), Euler 1
inserted endpoint disk  (V,E,F)=(70,174,105), Euler 1
shared boundary         33 edges
```

The boundary cycle is

```text
[69, 72, 261, 262, 263, 264, 246, 245, 244, 243, 242, 241, 240, 239, 238, 237, 236, 235, 234, 233, 232, 231, 230, 228, 248, 249, 250, 251, 252, 253, 254, 255, 256].
```

All 62 active labels common to parent and endpoint move, so disk_exchange_certificate.json certifies exact endpoint incidence replacement, **not** a continuous death-before-birth chronology.

The 27 endpoint-only active rows form an exact rank-four positive-volume regular complex. Squared-norm lifting gives 81 exact empty-circumsphere tetrahedra, 137 interior triangles, 50 boundary triangles, no ties, and a connected tetrahedron dual graph. Their exact convex-hull volume is

```text
9534794839370502902062309214434375847477416436666420287/60000000000000000000000000000000000000000000000000000 ≈ 158.91324732284173.
```

The actual body contains 49 mutual true edges among these rows and their graph is connected. Regular-complex certificate (`inserted_regular_complex.json`), SHA-256 `1816c39710b63f46e9bf4496b1b142625fd6c75d1cd5f0c4c15af8210bbb479a`.

## Drainage and external-arrow audit

The endpoint has exact decreasing squared radii along `257→256→69→72→14`. It nevertheless traps a new basin: row `10014` is a strict radial local minimum on

```text
N(10014)={257,259,10013,10015,10017,200001},
```

with every exact gap `||X_j||²-||X_10014||²>0`.

All 247 true edges were audited exactly. The only edges whose two endpoints have all nonmutual external arrows positive are `(8,246)` and `(8,264)`, both incident to protected `U8`. Every other edge has an explicit nonpositive external witness. Thus the new failure is not an unreported all-positive-arrow source.

## Exact 81-dimensional chamber

Every coordinate of the 27 endpoint-only active rows varies independently by

```text
δ=2^-65=1/36893488147419103232.
```

Exact interval arithmetic certifies the same 96-row hull, `(89,247,160)`, class `(2,1,1)`, named equilibria, positive volume, and zero own-centred moments throughout this 81-dimensional box. Raw uniform lower bounds include

```text
facet support          2.98185897562161e-14
inactive support       3.80878917859148e-9
nonstable witness      1.2561848071817774e-5
nonunstable witness    0.18776546469875546
saddle numerator       2.5235073963231317e-4
nonsaddle witness      1.369766276115673e-10.
```

Box certificate (`full_81d_box_certificate.json`), SHA-256 `259523104ef3426ccba95d6d13fbe6ac48559b2c7e9f3ef62ff501232308c67a`.

## Exact no-reference-centre theorem

Fix the 89 active coordinates and their boundary complex, but allow the reference point to be **any** interior point. An exact DPLL/Farkas proof shows there is no point for which `[0..16]` is the sole stable face, row `8` the sole unstable vertex, and every edge nonsaddle. The tree has 517 nodes and 345 leaves; each leaf has four exact nonnegative dual multipliers proving that no positive strict common margin exists.

All 24 branch features are faces forming a connected triangulated forcing disk

```text
(V,E,F)=(22,45,24), Euler 1, boundary length 18
boundary=[8, 246, 10012, 10020, 10019, 10018, 10010, 10005, 10021, 6004, 257, 200001, 259, 260, 261, 262, 263, 264].
```

The cover is inclusion-minimal: for each face, a supplied exact dyadic witness centre makes that omitted face stable while making the other 23 forcing faces nonstable, preserving body interior, the protected base, and U8. The full face list is in forcing_disk_summary.json, SHA-256 `14275a79ece8d54014a7176c143e289c5ee51bcbefd57f67c4e3b26e06ba74d9`; the DPLL/Farkas certificate SHA-256 is `26f17657001d011ed0bd0f06afba83b1d82a49513f99a881caaa30bb1945df65`.

A separate exact bundled atlas proves the analogous no-reference-centre theorem for the twelve-support parent and all 28 closest deactivation-only `(2,1,1)` chambers: parent 34 nodes/23 leaves/11 forcing faces; total 904 nodes/612 leaves over the 28 cells.

## Mesh and clean-room replay

The OBJ (`body.obj`) has 89 vertices, 174 triangles, 261 triangulation edges, Euler two, and every edge multiplicity two. Reconstructed volume is `1337.1954912396116` and centroid norm `3.25e-14`. The STL (`body.stl`) has identical watertight combinatorics; its small mass drift is float32 export error.

A clean extraction recompiles and replays the exact source, all-triples hull, mass/mechanics, disk exchange, regular complex, all-edge arrows, 81-dimensional box, mesh, fixed-endpoint no-centre theorem, forcing-disk irredundancy, and parent/28-deletion no-centre atlas, ending with `CLEANROOM_FULL_BASIN_TRANSFER_EXACT_REPLAYS_PASS`.

## Exact scope and next topology

Exact: source, complete H/V/E, mass, own centroid, class, endpoint deaths/births, same-boundary disk replacement, regular complex, external arrows, perturbation box, radial data, no-centre theorem, inclusion-minimal forcing disk, and mesh.

Not claimed: a continuous parent-to-endpoint path, death-before-birth chronology, impossibility of every realization of this abstract disk exchange, or a global support lower bound.

The smallest nonrepeating successor is a connected positive-volume **whole-basin dual cage** that changes the 24-face forcing disk and the complete saddle star simultaneously. It must make `10014` nonextreme or destroy its closed star; cross/eliminate the still-present edge `(261,262)`; replace both saddle faces `[7003,7004,200002]` and `[200002,248,7003]`; block transfer through `248/6009/7004/7005/200004/228`; preserve a decreasing path into row `14` or `15`; and retain at least four physical controls after the three moment equations for basin death, diagonal timing, saddle death, and antibirth.

## Final conclusion

**EXACT FULL-BASIN NONWINNER.** The promoted endpoint is an exact, independently replayed `(89,247,160),(2,1,1)` body with a 105-face inserted disk, a positive-volume 27-row regular complex, an 81-dimensional strict chamber, complete external-arrow control, and a true descending route into the protected base. It still cannot be a Gömböc: an inclusion-minimal 24-face forcing disk defeats every interior reference point, and saddle `(7003,200002)` survives. The next operation must replace the whole forcing basin and saddle star, not another local carrier.
