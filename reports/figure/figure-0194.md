# figure-0194

Historical AI scientific report · saved 2026-09-02 UTC. Claims below retain their original status and have not all been independently checked. The current retained construction is C622; the C<500 search remains open.

Public text derivative: unreviewed-encoded-blocks-omitted.

---

# Nimble Comet 70 — wall-242 higher-valence shared-terminal determination

The durable journal records the preceding exact 16-vertex `(2,2,2)` endpoint, its forced-edge obstruction, and this assignment’s requirement to leave that chamber through a finite-thickness higher-valence shared cell. :contentReference[oaicite:0]{index=0}

## Literal verdict

**EXACT NONWINNER.** No homogeneous convex polyhedral Gömböc was obtained.

The strongest new object is a literal exact rational, uniform-density, own-centred convex polyhedron with

- actual `(V,E,F,C)=(15,39,26,78)`;
- exact ordinary-volume first moments `(0,0,0)` after translation by the exact ordinary centroid;
- strict exhaustive equilibrium class `(S,U,H)=(2,2,2)`;
- intended stable face `[0,1371,C]` and intended unstable vertex `C` preserved strictly;
- all 15 supplied points active, 26 irredundant maximal triangular faces, and all 39 true edges;
- minimum Euclidean nonincident separation about `4.8058811251722395e-4`;
- a directed own-centroid perturbation box `|delta r_ij| <= 2^-56` on all 45 uncentred input coordinates;
- independent standard-library-only reconstruction and matching watertight OBJ/STL.

This is not a wall, auxiliary-centre body, frozen-fan count, or triangulation-diagonal audit. It is an exact post-topology endpoint at its own uniform-volume centroid.

## What changed relative to the accepted source

The accepted exact 16-vertex source had residual packet

```text
extra stable   [1258,A,C]
extra unstable 2732
saddles        [1371,C], [A,C]
```

while preserving stable `[0,1371,C]` and unstable `C`.

This continuation introduces two new extreme vertices `D=40004` and `E=40005`, removes source vertices `1614,1618,1725`, and rebuilds the actual hull to 15 vertices. Every old unwanted equilibrium is gone. The exact endpoint packet is instead

```text
extra stable   [1258,3290,D]
extra unstable 2515
saddles        [1371,E], [A,D]
```

The old packet was therefore destroyed, but a replacement Euler-neutral packet was born. The protected stable face and unstable vertex remain strict.

## The realized shared-interior topology

The endpoint contains a connected new-support surface patch on `D,E` with

```text
(V,E,F) = (10,19,10),  chi = 1,
boundary edges = 8,
shared true edge = [D,E].
```

Its ten maximal triangles are

```text
[1258,3290,D]
[1258,B,D]
[1371,2369,E]
[1371,C,E]
[2369,2515,D]
[2369,D,E]
[2515,B,D]
[3290,A,D]
[A,C,D]
[C,D,E]
```

and its boundary cycle consists of

```text
[1258,3290], [3290,A], [A,C], [C,1371],
[1371,2369], [2369,2515], [2515,B], [B,1258].
```

The patch is an exact triangulated disk. Coning its ten triangles to the exact own centroid gives a connected ten-tetrahedron positive-volume 3-ball. The residual stable face, both residual saddle stars, and an edge of the extra unstable vertex all lie in this one connected `D-E` complex. This is the stronger shared-interior alternative to a single terminal nonsimplicial cell.

The result does **not** claim a single exact scalar homotopy at which all old mechanisms die before any new mechanism is born. Numerical discovery rebuilt the hull after every candidate, but only the endpoint and its exact incidence are theorem-level claims.

## Complete supplied rational coordinates

All coordinates below have common denominator `10^12`; `A=40001`, `B=40002`, `C=40003`, `D=40004`, `E=40005`.

```text
0       (-558808044000,  1369877653000,   299010802000) / 10^12
1258    (-749153943188,  1793640876175,   936041839356) / 10^12
1371    (-803705664000,  1663541921000,  1104230578000) / 10^12
1975    (1493574336013, -3492575874739, -1482867372197) / 10^12
2152    ( 435895618446,  -839673212916,  -774935363483) / 10^12
2369    (1482250166603, -3461368747893, -1457471819545) / 10^12
2515    (1502771703475, -3486547488904, -1487365673983) / 10^12
2732    (1492391789262, -3480839891941, -1507446826704) / 10^12
3290    (-799145791472,  1912999292312,   606842662329) / 10^12
3296    ( 856347601735, -1889523145324,  -835279817928) / 10^12
A       (-815398589183,  1944186700340,   624500367950) / 10^12
B       (-655788464114,  1575834703788,   843949011991) / 10^12
C      (-4490523302000,  9970115945000,  5248168415000) / 10^12
D      (-4481063150506,  9965263958586,  5243556462236) / 10^12
E      (-4355534134392,  9670485137083,  5102094081309) / 10^12
```

`data/input_vertices_integer.csv` is authoritative. `scripts/generate_candidate.py` recomputes every later file from that table.

## Exact ordinary-volume centroid

The exact volume is

```text
330105633714799477637660601892332681
---------------------------------------------------
2000000000000000000000000000000000000
```

approximately `0.16505281685739973`.

The exact centroid of the uncentred table is

```text
cx = -3150328210141423346097366615511735709279547506077
     /3961267604577593731651927222707992172000000000000

cy =  2361576546527307385082993807265384340857571408241
     /1320422534859197910550642407569330724000000000000

cz =   121875742708298130524348442638718096105661239139
     /132042253485919791055064240756933072400000000000
```

numerically

```text
(-0.7952828550388622,
  1.7885006383802227,
  0.9230056250236159).
```

Subtracting this exact common vector from all vertices gives `data/vertices_centered_exact.csv`. Exact signed tetrahedral integration over all 26 outward maximal faces then gives

```text
Mx = My = Mz = 0,
centroid = (0,0,0).
```

Every tetrahedral volume and moment contribution is listed in `data/positive_tetrahedralization.csv`.

## Complete actual maximal faces

The 26 outward-oriented maximal triangular cycles are

```text
[0,2732,1371]
[0,1371,C]
[0,2152,2732]
[0,3290,2152]
[0,A,3290]
[0,C,A]
[1258,2152,3290]
[1258,3296,2152]
[1258,3290,D]
[1258,B,3296]
[1258,D,B]
[1371,1975,2369]
[1371,2732,1975]
[1371,2369,E]
[1371,E,C]
[1975,2515,2369]
[1975,2732,2515]
[2152,2515,2732]
[2152,3296,2515]
[2369,2515,D]
[2369,D,E]
[2515,3296,B]
[2515,B,D]
[3290,A,D]
[A,C,D]
[C,E,D]
```

Every nonincident vertex has a strictly positive inward plane slack. Primitive integer H-data are in `data/wall242_terminal15_exact_H_irredundant.csv`.

## Complete true-edge list

```text
[0,1371] [0,2152] [0,2732] [0,3290] [0,A] [0,C]
[1258,2152] [1258,3290] [1258,3296] [1258,B] [1258,D]
[1371,1975] [1371,2369] [1371,2732] [1371,C] [1371,E]
[1975,2369] [1975,2515] [1975,2732]
[2152,2515] [2152,2732] [2152,3290] [2152,3296]
[2369,2515] [2369,D] [2369,E]
[2515,2732] [2515,3296] [2515,B] [2515,D]
[3290,A] [3290,D] [3296,B]
[A,C] [A,D] [B,D] [C,D] [C,E] [D,E]
```

Every edge has exactly two incident maximal faces, and `15-39+26=2`. The exact four-component cone ledger for every edge is `data/wall242_terminal15_exact_true_edges_full_cones.csv`.

## Exhaustive equilibrium audit at the exact own centroid

### Stable faces

| maximal face | exact-foot barycentrics, approximately | minimum |
|---|---|---:|
| `[0,1371,C]` | `(0.369634529553, 0.603053658818, 0.0273118116291)` | `0.0273118116291` |
| `[1258,3290,D]` | `(0.949511194469, 0.0496153349946, 0.000873470536420)` | `0.000873470536420` |

Every other maximal face has a fixed exact negative Cramer witness. The closest excluded face is `[1258,2152,3290]`, margin about `-0.00254109524894`.

### Unstable vertices

| vertex | minimum raw exact support, approximately | normalized directional margin |
|---|---:|---:|
| `2515` | `0.000178604332157` | `0.00240965116` |
| `C` | `0.0946020672313` | `0.81917423083` |

Every other vertex has a fixed exact negative directed-edge support. The closest excluded vertex is `1975`, raw support about `-3.74366091927e-5` and normalized directional margin about `-5.0508e-4`.

### Saddle true edges

The four displayed components are edge-foot `t`, `1-t`, and the two incident-normal-cone coefficients.

| edge | four components, approximately | minimum |
|---|---|---:|
| `[1371,E]` | `(0.002654617447, 0.997345382553, 1.58993647644, 1.90855036185)` | `0.002654617447` |
| `[A,D]` | `(0.000568104156, 0.999431895844, 8.07329586470, 2.86370222113)` | `0.000568104156` |

Every other true edge has a fixed exact negative component. The closest excluded edge is `[1371,2369]`, with edge-foot component about `-0.00412333467116`.

Therefore the complete strict class is exactly

```text
(S,U,H)=(2,2,2),
S+U-H=2.
```

## Positive own-centroid perturbation neighbourhood

`scripts/verify_interval_own_centroid.py` proves the independent coordinate box

```text
|delta r_ij| <= 2^-56
              = 1/72057594037927936
              ≈ 1.3877787807814457e-17
```

on all 45 entries of the **uncentred** input table. For every point in this box it interval-integrates the perturbed volume and first moments, forms the common perturbed ordinary centroid `M/V`, translates every vertex by that centroid interval, and verifies:

1. the same 26 maximal faces and 39 true edges;
2. all stable and nonstable face witnesses;
3. all unstable and nonunstable vertex witnesses;
4. all four components of every true-edge cone;
5. the external-positive forced-edge chamber below.

The radius is conservative because interval Gaussian elimination is dependency-sensitive on the skinny `C-D-E` faces. It is nevertheless a literal nonzero own-centroid neighbourhood.

## Exact terminal obstruction

True edge `[1975,2515]` has all endpoint supports to neighbours outside the pair strictly positive. The smallest is about `0.00555025786287`. The mutual supports satisfy

```text
sigma(1975 -> 2515) < 0,
sigma(2515 -> 1975) > 0,

sigma(1975 -> 2515)+sigma(2515 -> 1975)
  = ||p_2515-p_1975||^2
  = 28233544592923151693/200000000000000000000000
  > 0.
```

If both endpoints were nonunstable while every external support remained positive, both mutual supports would have to be nonpositive, contradicting this exact identity. Hence at least one endpoint is unstable throughout the certified sign chamber. Since target `C` is independently and strongly unstable, the chamber has `U>=2`.

This proves only the exact current sign chamber; it is not a global obstruction after `[1975,2515]` disappears or an external support reverses.

## Attempts to break the conclusion

The discovery code always rebuilt the actual convex hull, ordinary centroid, maximal faces, true edges, and full edge cones before scoring a candidate.

- A connected two-new-support search produced the `D-E` shared complex. The retained seed-66 run used 5,201 full evaluations and then underwent exact rationalization.
- Every one of the old source residual features was explicitly checked after each accepted topology change; the final source packet is absent.
- A complete fixed-ledger screen considered all 336 component assignments at ten trust radii from `10^-5` through `0.3`. No nominal positive direction materialized as a target body; macroscopic first jets crossed actual topology or mechanics walls and transferred/birthed features.
- Nineteen feasible connected one-terminal-vertex visibility patches were materialized. All transferred the packet to the cap vertex and adjacent faces.
- A common post-side probe of the three immediate residual edge flips `[1975,2515] -> [2369,2732]`, `[1371,E] -> [2369,C]`, and `[A,D] -> [3290,C]` again produced a `(2,2,2)` packet, not a cancellation.

These are empirical discovery/exhaustion records, not global impossibility theorems. The exact claims are restricted to the material endpoint, its interval neighbourhood, and the forced-edge sign chamber.

## First genuinely new successor topology

All four current unwanted mechanisms have an ordinary adjacent circuit, and all four must be coupled rather than crossed serially:

```text
[1975,2515] -> [2369,2732]     forced extra-maximum edge
[1371,E]    -> [2369,C]        first saddle
[A,D]       -> [3290,C]        second saddle
[1258,3290] -> [2152,D]        limiting edge of extra stable face
```

The extra stable face `[1258,3290,D]` has its smallest barycentric coordinate at `D`, so its death sheet is attached to boundary edge `[1258,3290]`. The first unexcluded successor is therefore one finite-thickness four-circuit prism/octahedral cell, or a stronger multi-cell sharing an interior edge or face, with three dependent ordinary-moment coordinates. It must cross all four death sheets before any replacement packet appears while preserving `[0,1371,C]` and `C`.

Another fixed-cell, metric-only, deletion-only, single cap, or serial diagonal-flip search is represented by the failed families above.

## Verification and mesh export

`RUN_ALL_VERIFIERS.sh` executes:

- deterministic exact generation from the integer input table;
- primary exact H/V/E, moment, mechanics, patch, and obstruction verification;
- directed own-centroid interval verification;
- a standard-library-only clean-room verifier importing neither the generator nor `exact_core.py`;
- watertight OBJ/STL verification.

The aggregate transcript ends with


[An encoded source block is omitted from this text export pending a complete content review. This passage is not a complete executable package.]


## Artifact map

- `candidate.json` — concise machine-readable determination.
- `data/input_vertices_integer.csv` — authoritative supplied exact coordinates.
- `data/vertices_centered_exact.csv` — exact own-centred V-data.
- `data/wall242_terminal15_exact_H_irredundant.csv` — complete primitive integer H-data.
- `data/wall242_terminal15_exact_faces.csv` — all maximal faces.
- `data/wall242_terminal15_exact_true_edges_full_cones.csv` — all true edges and four cone components.
- `data/wall242_terminal15_exact_exact_audit.json` — complete exact mechanics/moment ledger.
- `certificates/shared_terminal_complex_certificate.json` — exact `D-E` disk and 3-ball certificate.
- `certificates/source_packet_replacement_certificate.json` — exact old-packet destruction/new-packet transfer.
- `certificates/terminal_forced_edge_obstruction.json` — exact `U>=2` sign-chamber theorem.
- `certificates/first_successor_topology.json` — four-circuit successor specification.
- `certificates/own_centroid_perturbation_certificate.json` — directed positive box.
- `scripts/generate_candidate.py`, `verify_exact.py`, `verify_interval_own_centroid.py`, `verify_independent.py`, `verify_mesh.py`.
- `mesh/body.obj`, `mesh/body.stl` — matching watertight meshes.
- `search/search_evidence.json` and associated scripts/logs — numerical discovery evidence, explicitly separated from proof.

## Final determination

**NONWINNER.** The higher-valence shared-interior topology is real and exact. It destroys the complete previous stable/unstable/two-saddle packet while preserving the intended stable face and unstable vertex. It does not absorb the Morse block: the replacement packet `[1258,3290,D]`, `2515`, `[1371,E]`, `[A,D]` is strict and open. Edge `[1975,2515]` then forces `U>=2` in the exact endpoint chamber. The four-circuit shared cell above is the first topology not covered by this result.


## Portable artifact links and immutable hashes

- [Complete portable exact bundle](sandbox:/mnt/data/Nimble_Comet_70_wall242_terminal_shared_edge_exact_NONWINNER.zip) — SHA-256 `a4225ffb7fd5a078d321c2c1930787ccf3b25e2c59344e89bad6a79cb5aaafd0`.
- [Standalone report](sandbox:/mnt/data/Nimble_Comet_70_wall242_terminal_shared_edge_exact_NONWINNER/REPORT.md) — SHA-256 `df2c152ac84c1dfcf560ad84641f8c9927e8522fc8482068846937849e108ca5`.
- [Machine-readable candidate](sandbox:/mnt/data/Nimble_Comet_70_wall242_terminal_shared_edge_exact_NONWINNER/candidate.json) — SHA-256 `d4e01f8e53a7a833bf9b5575c92e886ad0d0774a61f95eae8c6c5d7cd0719b02`.
- [Authoritative integer coordinates](sandbox:/mnt/data/Nimble_Comet_70_wall242_terminal_shared_edge_exact_NONWINNER/data/input_vertices_integer.csv).
- [Complete exact centred V-data](sandbox:/mnt/data/Nimble_Comet_70_wall242_terminal_shared_edge_exact_NONWINNER/data/wall242_terminal15_exact_V_exact.csv).
- [Complete irredundant H-data](sandbox:/mnt/data/Nimble_Comet_70_wall242_terminal_shared_edge_exact_NONWINNER/data/wall242_terminal15_exact_H_irredundant.csv).
- [All maximal faces](sandbox:/mnt/data/Nimble_Comet_70_wall242_terminal_shared_edge_exact_NONWINNER/data/wall242_terminal15_exact_faces.csv).
- [All true edges and four-component cones](sandbox:/mnt/data/Nimble_Comet_70_wall242_terminal_shared_edge_exact_NONWINNER/data/wall242_terminal15_exact_true_edges_full_cones.csv).
- [Exact centroid and mechanics audit](sandbox:/mnt/data/Nimble_Comet_70_wall242_terminal_shared_edge_exact_NONWINNER/data/wall242_terminal15_exact_exact_audit.json).
- [Shared terminal-complex certificate](sandbox:/mnt/data/Nimble_Comet_70_wall242_terminal_shared_edge_exact_NONWINNER/certificates/shared_terminal_complex_certificate.json).
- [Source-packet replacement certificate](sandbox:/mnt/data/Nimble_Comet_70_wall242_terminal_shared_edge_exact_NONWINNER/certificates/source_packet_replacement_certificate.json).
- [Forced-edge obstruction](sandbox:/mnt/data/Nimble_Comet_70_wall242_terminal_shared_edge_exact_NONWINNER/certificates/terminal_forced_edge_obstruction.json).
- [First successor topology](sandbox:/mnt/data/Nimble_Comet_70_wall242_terminal_shared_edge_exact_NONWINNER/certificates/first_successor_topology.json).
- [Own-centroid perturbation certificate](sandbox:/mnt/data/Nimble_Comet_70_wall242_terminal_shared_edge_exact_NONWINNER/certificates/own_centroid_perturbation_certificate.json).
- [Independent verification report](sandbox:/mnt/data/Nimble_Comet_70_wall242_terminal_shared_edge_exact_NONWINNER/certificates/independent_verification_report.json) — SHA-256 `f2de3cefc97584fe3eda9b0d56bb17e56d6d5b2138b267094ee2c516b6d9ceee`.
- [Deterministic generator](sandbox:/mnt/data/Nimble_Comet_70_wall242_terminal_shared_edge_exact_NONWINNER/scripts/generate_candidate.py).
- [Primary verifier](sandbox:/mnt/data/Nimble_Comet_70_wall242_terminal_shared_edge_exact_NONWINNER/scripts/verify_exact.py).
- [Independent clean-room verifier](sandbox:/mnt/data/Nimble_Comet_70_wall242_terminal_shared_edge_exact_NONWINNER/scripts/verify_independent.py).
- [Own-centroid interval verifier](sandbox:/mnt/data/Nimble_Comet_70_wall242_terminal_shared_edge_exact_NONWINNER/scripts/verify_interval_own_centroid.py).
- [OBJ](sandbox:/mnt/data/Nimble_Comet_70_wall242_terminal_shared_edge_exact_NONWINNER/mesh/body.obj) and [STL](sandbox:/mnt/data/Nimble_Comet_70_wall242_terminal_shared_edge_exact_NONWINNER/mesh/body.stl).
- [Aggregate verifier transcript](sandbox:/mnt/data/Nimble_Comet_70_wall242_terminal_shared_edge_exact_NONWINNER/RUN_ALL_VERIFIERS.txt) — SHA-256 `77c438c04e81c510881c4a0292115df64184e6ef1177493d1f8ff5420ed79611`.
- [Fresh-extraction manifest and verifier transcript](sandbox:/mnt/data/Nimble_Comet_70_wall242_terminal_shared_edge_exact_NONWINNER_FRESH_VERIFY.txt) — SHA-256 `a15af9ea46daa58825a2cc8a69e9afc6a57e53746f9a3c6d992a603e81c83f2a`.
- [SHA-256 manifest](sandbox:/mnt/data/Nimble_Comet_70_wall242_terminal_shared_edge_exact_NONWINNER/SHA256SUMS.txt) — SHA-256 `1ef66e3ae12d15761be1f7fba051df6fd9c0fe5128ff51264638b3ea0c88d5d9`.
