# figure-0184

Historical AI scientific report · saved 2026-09-01 UTC. Claims below retain their original status and have not all been independently checked. The current retained construction is C622; the C<500 search remains open.

---

# Nimble Comet 70 — exact wall-242 coupled-cell determination

## Literal disposition

**EXACT NONWINNER.** No homogeneous convex polyhedral Gömböc was obtained. The acceptance target remains a finite uniform-density body, evaluated at its own exact volume centroid, with strict `(S,U,H)=(1,1,0)`, complete H/V/E incidence, exhaustive cone mechanics, independent verification, and matching meshes. :contentReference[oaicite:0]{index=0}

The strongest new object is an exact rational, own-centred, all-active simplicial polyhedron with

- `(V,E,F,C)=(16,42,28,84)`;
- exact ordinary-volume centroid `(0,0,0)` after exact rational translation;
- strict exhaustive class `(S,U,H)=(2,2,2)`;
- intended stable face `[0,1371,C]` and intended unstable vertex `C` preserved strictly;
- all four requested circuit inequalities crossed to their strict post-sides;
- all four old diagonals absent and all four replacement diagonals present;
- positive inactive separation and a positive own-centroid perturbation box;
- independent clean-room reconstruction and watertight OBJ/STL.

The durable journal identified the previous exact endpoint and prescribed precisely this finite-thickness coupled escape from edge `[2732,3296]`. :contentReference[oaicite:1]{index=1} The escape succeeds combinatorially, but the requested no-compensating-birth ordering fails: a new Euler-neutral `(1,1,2)` residual packet is already present in the strict post-cell.

## What changed from the accepted source

The accepted source had extra stable face `[1258,B,1725]`, extra unstable vertex `3296`, saddle edges `[2152,A]` and `[B,C]`, and forced edge `[2732,3296]`. The exact endpoint makes these four diagonal exchanges:

```text
[2732,3296] -> [1975,B]
[2152,A]    -> [0,1258]
[B,C]       -> [1258,1371]
[1725,B]    -> [1258,3296]
```

Exactly eight source maximal triangles disappear and eight endpoint triangles appear. The added-face complex is connected. The exact oriented circuit determinants reverse sign as follows:

| circuit | source determinant | endpoint determinant |
|---|---:|---:|
| `{1975,2732,3296,B}` | `36574964193517935160995160923721/488281250000000000000000000000000` | `-1315420560035964259221/25000000000000000000000000` |
| `{0,2152,A,1258}` | `208590928136044659620759539784943/488281250000000000000000000000000` | `-68303997166828904479449/125000000000000000000000000` |
| `{1258,B,C,1371}` | `154689030091450642560197317843231/30517578125000000000000000000000` | `-595844745185940130921491/1000000000000000000000000000` |
| `{1258,1725,B,3296}` | `37225580388838051749112949228857/97656250000000000000000000000000` | `-992082031164337082617/125000000000000000000000000` |

The smallest endpoint-side determinant magnitude is about `7.936656249314696e-6`, so this is a finite strict chamber, not a circuit wall.

I did **not** certify a single affine scalar homotopy on which all four roots occur at one common parameter, nor a path theorem excluding temporary equilibria. The exact claim is the common strict post-side endpoint, its literal face lattice, and the four exact diagonal exchanges.

## Complete supplied coordinates

All entries are exact integer numerators over the common denominator `10^9`. `A=40001`, `B=40002`, and `C=40003`.

```text
0      (-558808044,  1369877653,   299010802) / 10^9
1258   (-753346760,  1776028546,   938172580) / 10^9
1371   (-803705664,  1663541921,  1104230578) / 10^9
1614   ( 907711561, -2017720216, -1012878784) / 10^9
1618   ( 567296594, -1254973915,  -558093259) / 10^9
1725   ( 670082385, -1499275327,  -654927533) / 10^9
1975   (1380156559, -3199069194, -1409374840) / 10^9
2152   ( 467493353,  -941198587,  -839546706) / 10^9
2369   (1352171577, -3144276724, -1413685185) / 10^9
2515   (1371623109, -3194317417, -1405884096) / 10^9
2732   (1377754582, -3203930812, -1401185591) / 10^9
3290   (-938921197,  2206771750,   778889345) / 10^9
3296   ( 973651390, -2214134471,  -984041376) / 10^9
A      (-806698069,  1923707230,   615443080) / 10^9
B      (-613946177,  1442072153,   790403321) / 10^9
C     (-4490523302,  9970115945,  5248168415) / 10^9
```

All 16 supplied points are actual extreme vertices.

## Exact ordinary-volume centring

The exact volume is

```text
47752304993119236820339693/400000000000000000000000000
```

or approximately `0.1193807624827981`.

The exact centroid of the supplied uncentred coordinates is

```text
cx = -120238441233022013820559138632649459
     /150796752609850221537914820000000000

cy = 2559663765500234697590802389251574867
     /1432569149793577104610190790000000000

cz = 869286944562929098692708025108534563
     /955046099862384736406793860000000000
```

Numerically this is approximately

```text
(-0.7973543140156978,
  1.7867645452710355,
  0.9102041720166043).
```

Subtracting this exact rational vector from every supplied point gives the exported centred V-data. Exact signed tetrahedral integration over the complete 28-face sphere then gives

```text
Mx = My = Mz = 0,
centroid = (0,0,0).
```

Every positive tetrahedron and every individual moment contribution is included in `data/positive_tetrahedralization.csv`.

## Complete actual maximal faces

The 28 outward-oriented maximal triangular cycles are

```text
[2152,0,1258]
[A,1258,0]
[1371,0,2369]
[1371,C,0]
[2152,2369,0]
[3290,A,0]
[3290,0,C]
[B,1258,1371]
[1371,1258,C]
[1618,1614,1258]
[1614,2152,1258]
[1618,1258,1725]
[3296,1725,1258]
[3296,1258,B]
[A,C,1258]
[2515,1371,2369]
[2732,1371,2515]
[2732,B,1371]
[1618,1725,1614]
[3296,1614,1725]
[1614,1975,2152]
[3296,1975,1614]
[2152,1975,2369]
[2515,2369,1975]
[2732,2515,1975]
[2732,1975,B]
[3296,B,1975]
[3290,C,A]
```

Every nonincident point is strictly behind every listed supporting plane. The minimum Euclidean nonincident separation is approximately `1.1858932192334716e-4`.

## Complete true-edge list

```text
[0,1258] [0,1371] [0,2152] [0,2369] [0,3290] [0,A] [0,C]
[1258,1371] [1258,1614] [1258,1618] [1258,1725] [1258,2152]
[1258,3296] [1258,A] [1258,B] [1258,C]
[1371,2369] [1371,2515] [1371,2732] [1371,B] [1371,C]
[1614,1618] [1614,1725] [1614,1975] [1614,2152] [1614,3296]
[1618,1725] [1725,3296]
[1975,2152] [1975,2369] [1975,2515] [1975,2732] [1975,3296]
[1975,B] [2152,2369] [2369,2515] [2515,2732] [2732,B]
[3290,A] [3290,C] [3296,B] [A,C]
```

Every edge has exactly two incident maximal faces, and `16-42+28=2`. The complete primitive-integer H-representation and the four exact cone components of every true edge are linked below.

## Exhaustive equilibrium audit at the exact own centroid

### Stable faces

| maximal face | exact foot barycentrics | minimum |
|---|---|---:|
| `[0,1371,C]` | approximately `(0.3877808886,0.5842921729,0.02792693853)` | `0.02792693852878079` |
| `[1258,A,C]` | approximately `(0.8982728354,0.1004227346,0.001304430023)` | `0.001304430022822102` |

The closest excluded face is `[0,A,1258]`, whose selected barycentric witness is approximately `-0.0186358523895738`.

### Unstable vertices

| vertex | exact/raw minimum support | normalized directional margin |
|---|---:|---:|
| `2732` | approximately `1.097465353062353e-4` | `0.001889225380751221` |
| `C` | approximately `96.03441313415084` | `0.9994708259433444` |

The closest excluded vertex is `1975`, with raw selected support approximately `-1.3277913035781263e-5` and normalized directional margin approximately `-2.285722674305666e-4`.

### Saddle edges

For each edge, the four components are the edge-foot coordinates `t`, `1-t`, followed by the two incident full-normal-cone coefficients.

| edge | four physical components | minimum |
|---|---|---:|
| `[1371,C]` | approximately `(0.001965720922,0.9980342791,0.1372050367,0.3994260311)` | `0.001965720921659747` |
| `[A,C]` | approximately `(0.002297409971,0.9977025900,0.01016748399,13.48154349)` | `0.002297409971438864` |

Every other true edge has a certified negative component. The closest excluded edge is `[1371,2732]`, with edge-foot component approximately `-0.0028740544654366584`.

Thus the strict class is exactly

```text
(S,U,H) = (2,2,2),
S+U-H = 2.
```

## Positive own-centroid perturbation certificate

The directed exact interval verifier certifies independent perturbations of all 48 entries of the **uncentred** coordinate table by

```text
|delta r_ij| <= 2^-53
              = 1/9007199254740992
              ≈ 1.1102230246251565e-16.
```

For every point in this box it interval-integrates ordinary volume and all three first moments, forms the common perturbed centroid `M/V`, translates all vertices by that centroid interval, and verifies:

- the same 28 maximal faces and 42 true edges;
- every stable and nonstable face witness;
- every unstable and nonunstable directed vertex witness;
- all four components of all 42 edge cones;
- the post-cell forced-edge external-positive sign chamber.

The radius is deliberately conservative because direct interval Gaussian elimination over the skinny post-circuit faces has substantial dependency inflation. It is nonetheless a strict positive neighbourhood, not a point certificate.

## Exact post-cell broad obstruction

The new true edge `[1975,2732]` has all nonmutual endpoint supports strictly positive. Their minimum is approximately

```text
0.0503703067661508.
```

The mutual supports have opposite signs:

```text
sigma(1975 -> 2732) < 0,
sigma(2732 -> 1975) > 0,
```

and satisfy the exact identity

```text
sigma(1975 -> 2732) + sigma(2732 -> 1975)
  = ||p_2732-p_1975||^2
  = 48234311135227/500000000000000000
  > 0.
```

If neither endpoint were unstable while all listed external supports remained positive, both mutual supports would have to be nonpositive, contradicting the exact positive squared-length identity. Hence at least one of `1975,2732` is unstable throughout this sign chamber. Target `C` is independently and strongly unstable, so every realization in the certified chamber has `U>=2`.

This is a sign-cell obstruction, not a global theorem after another topology change.

## First genuinely new successor topology

The first escape from the new forced-edge chamber is the circuit

```text
{1975,2515,2732,B}:
[1975,2732] -> [2515,B].
```

That exchange alone cannot finish the cancellation:

- Saddle `[A,C]` is ordinarily flippable. Its two opposite vertices are `1258,3290`, and `[1258,3290]` is absent. The exchange `[A,C] -> [1258,3290]` also removes extra stable face `[1258,A,C]` on the old side.
- Saddle `[1371,C]` is **not** ordinarily flippable. Its incident faces are `[0,1371,C]` and `[1258,C,1371]`; their opposite vertices `0,1258` are already connected by true edge `[0,1258]`. A simplicial 2-to-2 flip would create a duplicate edge.

The first unexcluded successor is therefore one shared finite-thickness 3-cell coupling:

1. `[1975,2732] -> [2515,B]`;
2. `[A,C] -> [1258,3290]`;
3. a new-support 2-to-3/3-to-2 replacement around the nonflippable K4 subgraph on `{0,1258,1371,C}`;
4. exact closure of all three ordinary-volume moments;
5. strict preservation of maximal stable `[0,1371,C]` and unstable `C`.

Another sequence of isolated diagonal flips is structurally insufficient because `[1371,C]` has no legal opposite diagonal.

## Search and attempted falsification

I constructed explicit combinatorial spheres for the three-flip cell, the four-flip cell, and the next forced-edge exchange; generated Tutte realizations; crossed the fourth circuit by directed reflection; searched projective Pareto families; ran full-hull sequential linear programs with target, topology, face-area, and volume barriers; and tested generic CMA, addition, deletion, and one-circuit variants.

The strict SLP continuation approached hard target score `-1.6839391776968268e-5` but ended in class `(5,4,7)` near its topology floor. It is rejected as weaker and mechanically more crowded. The exact endpoint reported here was selected instead for the largest observed joint post-cell topology clearance among the robust `(2,2,2)` Pareto family.

These searches are empirical discovery evidence. The theorem-level output is the exact endpoint, complete incidence and mechanics, four circuit sign reversals, positive interval box, nonflippability certificate, and forced-edge obstruction.

## Verification results

The following checks were run successfully after the final exact generator revision:

```text
EXACT_COUPLED_CELL_NONWINNER_PASS
OWN_CENTROID_INTERVAL_CERTIFICATE_PASS
INDEPENDENT_CLEAN_ROOM_EXACT_COUPLED_CELL_NONWINNER_PASS
WATERTIGHT_MESH_EXPORT_PASS
```

The independent verifier is standard-library-only and imports neither the generator nor `exact_core.py`. It independently enumerates every supporting triple, rebuilds the centroid, faces and edges, reclassifies all equilibrium primitives, compares the exact parent and endpoint topologies, checks all four determinant reversals, proves the residual nonflippability, verifies the forced-edge identity, and checks the mesh.

## Artifact index

- [Standalone complete report](sandbox:/mnt/data/Nimble_Comet_70_wall242_coupled_cell_exact_NONWINNER/REPORT.md)
- [Machine-readable candidate](sandbox:/mnt/data/Nimble_Comet_70_wall242_coupled_cell_exact_NONWINNER/candidate.json)
- [Authoritative integer-coordinate input](sandbox:/mnt/data/Nimble_Comet_70_wall242_coupled_cell_exact_NONWINNER/data/input_vertices_integer.csv)
- [Deterministic exact generator](sandbox:/mnt/data/Nimble_Comet_70_wall242_coupled_cell_exact_NONWINNER/scripts/generate_candidate.py)
- [Primary exact verifier](sandbox:/mnt/data/Nimble_Comet_70_wall242_coupled_cell_exact_NONWINNER/scripts/verify_exact.py)
- [Independent clean-room verifier](sandbox:/mnt/data/Nimble_Comet_70_wall242_coupled_cell_exact_NONWINNER/scripts/verify_independent.py)
- [Own-centroid interval verifier](sandbox:/mnt/data/Nimble_Comet_70_wall242_coupled_cell_exact_NONWINNER/scripts/verify_interval_own_centroid.py)
- [Mesh verifier](sandbox:/mnt/data/Nimble_Comet_70_wall242_coupled_cell_exact_NONWINNER/scripts/verify_mesh.py)
- [Complete centred exact V-data](sandbox:/mnt/data/Nimble_Comet_70_wall242_coupled_cell_exact_NONWINNER/data/wall242_coupledcell16_exact_V_exact.csv)
- [Complete irredundant integer H-data](sandbox:/mnt/data/Nimble_Comet_70_wall242_coupled_cell_exact_NONWINNER/data/wall242_coupledcell16_exact_H_irredundant.csv)
- [All maximal faces](sandbox:/mnt/data/Nimble_Comet_70_wall242_coupled_cell_exact_NONWINNER/data/wall242_coupledcell16_exact_faces.csv)
- [All true edges and four-component cones](sandbox:/mnt/data/Nimble_Comet_70_wall242_coupled_cell_exact_NONWINNER/data/wall242_coupledcell16_exact_true_edges_full_cones.csv)
- [Complete exact centroid/mechanics audit](sandbox:/mnt/data/Nimble_Comet_70_wall242_coupled_cell_exact_NONWINNER/data/wall242_coupledcell16_exact_exact_audit.json)
- [Exact four-circuit cell certificate](sandbox:/mnt/data/Nimble_Comet_70_wall242_coupled_cell_exact_NONWINNER/certificates/four_circuit_cell_certificate.json)
- [Exact post-cell forced-edge obstruction](sandbox:/mnt/data/Nimble_Comet_70_wall242_coupled_cell_exact_NONWINNER/certificates/post_cell_forced_edge_obstruction.json)
- [Exact residual topology obstruction](sandbox:/mnt/data/Nimble_Comet_70_wall242_coupled_cell_exact_NONWINNER/certificates/residual_topology_obstruction.json)
- [Own-centroid perturbation certificate](sandbox:/mnt/data/Nimble_Comet_70_wall242_coupled_cell_exact_NONWINNER/certificates/own_centroid_perturbation_certificate.json)
- [Independent verification report](sandbox:/mnt/data/Nimble_Comet_70_wall242_coupled_cell_exact_NONWINNER/certificates/independent_verification_report.json)
- [Primary verification transcript](sandbox:/mnt/data/Nimble_Comet_70_wall242_coupled_cell_exact_NONWINNER/verify_exact_run.log)
- [Independent verification transcript](sandbox:/mnt/data/Nimble_Comet_70_wall242_coupled_cell_exact_NONWINNER/verify_independent_run.log)
- [Interval verification transcript](sandbox:/mnt/data/Nimble_Comet_70_wall242_coupled_cell_exact_NONWINNER/verify_interval_run.log)
- [Mesh verification transcript](sandbox:/mnt/data/Nimble_Comet_70_wall242_coupled_cell_exact_NONWINNER/verify_mesh_run.log)
- [Watertight OBJ](sandbox:/mnt/data/Nimble_Comet_70_wall242_coupled_cell_exact_NONWINNER/mesh/body.obj)
- [Watertight STL](sandbox:/mnt/data/Nimble_Comet_70_wall242_coupled_cell_exact_NONWINNER/mesh/body.stl)

A monolithic ZIP, final SHA-256 manifest, and fresh-extraction aggregate transcript were not produced before the execution boundary. The linked exact directory is otherwise materialized and the four principal verifiers were run individually on its final data.

## Final determination

**NONWINNER.** The first forbidden forced-edge chamber was genuinely exited: `[2732,3296]`, `[2152,A]`, `[B,C]`, and `[1725,B]` are absent, while `[1975,B]`, `[0,1258]`, `[1258,1371]`, and `[1258,3296]` are true edges. Source unstable `3296` and both source saddles disappear; old stable `[1258,B,1725]` is not maximal; target `[0,1371,C]` and `C` remain strict.

The transferred exact residual is

```text
extra stable:   [1258,A,C]
extra unstable: 2732
saddles:        [1371,C], [A,C]
```

True edge `[1975,2732]` forces the second unstable equilibrium throughout the post-cell sign chamber, and target-edge saddle `[1371,C]` cannot undergo an ordinary diagonal flip because `[0,1258]` already exists. The compound three-part successor described above is the first genuinely new topology forced by the exact endpoint.
