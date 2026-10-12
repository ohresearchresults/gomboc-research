# figure-0084

AI research report · 2026-08-26 UTC

---

# Bright Comet 68 — whole-block replacement handoff

## Determination

**No homogeneous convex polyhedral Gömböc was found.** The strongest endpoint is an exact rational, own-centred, open 11-vertex body with strict class `(S,U,H)=(2,2,2)`, not `(1,1,0)`. I found no exact global exclusion of its entire combinatorial realization space and closed no inherited low-vertex chamber.

The acceptance gate remains the exact one in the shared journal: uniform volume density, equilibria at the body’s own exact volume centroid, exactly one stable maximal face, one unstable vertex and no saddle true edge, together with complete incidence, strict margins, independent verification and OBJ/STL. A near-object or wall point is not a completion. The supplied starting point was the exact V11 `(2,2,2)` endpoint whose coalesced defect was stable `[0,12,15]`, unstable vertex `4`, and saddles `[0,14]`,`[0,15]`; the requested next move was one whole-block replacement with obsolete labels allowed to deactivate in the same circuit cascade.

## What changed

The old migrated block was replaced in one connected 17-label homotopy. Construction labels `2,4,11,12,14,15` became non-extreme; labels `19,20,21,22,23,24` became extreme and form a connected patch. In the final hull, the old stable triangle `[0,12,15]`, both old saddle edges `[0,14]`,`[0,15]`, and unstable vertex `4` are all absent together.

This operation also breaks the previously observed directed cycles. The final exact directed witness graph is acyclic. It has two sinks, however: retained maximum `0` and new maximum `24`. The whole Morse defect therefore transferred into a new connected `(S,U,2H)` block rather than cancelling.

## Strongest exact post-strip endpoint

### Exact H/V data

Active construction labels:

```text
[0,1,3,5,16,19,20,21,22,23,24]
```

Exact rational coordinates, already translated to the exact uniform-volume centroid:

```text
0: (-45500152645350209010752521637620083070311/27370452588967089282056469441760000000000, 2189421730871782616064230702031497165993/13685226294483544641028234720880000000000, -14872932228777426619039182317504255397029/27370452588967089282056469441760000000000)
1: (1104006694025872597402154324193168339217/1094818103558683571282258777670400000000, 2097539444501960647156020662381848258761/13685226294483544641028234720880000000000, -308905999350890239949014564968489003861/27370452588967089282056469441760000000000)
3: (11061631690029821543145887312487437286937/27370452588967089282056469441760000000000, 1277571080782336087918749424381078299361/13685226294483544641028234720880000000000, 6562225654113693394407095123524005619339/27370452588967089282056469441760000000000)
5: (37865244808809443616941157995678831598313/27370452588967089282056469441760000000000, -13220729196784082350912969604034982039/13685226294483544641028234720880000000000, -1157322870729352459145793735703979757349/27370452588967089282056469441760000000000)
16: (1427279808970697536931026944643812912841/27370452588967089282056469441760000000000, -1953155929212417147787878510568144510367/13685226294483544641028234720880000000000, 9743871489542990538689076961482049166267/27370452588967089282056469441760000000000)
19: (2337183821836679436097653194383065341017/27370452588967089282056469441760000000000, 1282383572720148993293034849290084076641/13685226294483544641028234720880000000000, -8451837460190470808445773865931738915253/27370452588967089282056469441760000000000)
20: (-4739178042956891811892992558139372576411/5474090517793417856411293888352000000000, -606444194030408668056440830270832602891/2737045258896708928205646944176000000000, 11106004859072605845751418586746854702203/27370452588967089282056469441760000000000)
21: (5943858143334321559601983028472720683781/5474090517793417856411293888352000000000, -1927861552822775801194955306390011448127/13685226294483544641028234720880000000000, 6535946685907159652504846358381938012971/27370452588967089282056469441760000000000)
22: (10390765050560669675599230140712958283657/27370452588967089282056469441760000000000, -666697818475448452151336063569268826479/13685226294483544641028234720880000000000, -6537466945785725099127126654735145798837/27370452588967089282056469441760000000000)
23: (3698056546638680543581588293544440629817/27370452588967089282056469441760000000000, 418965992249304404865089853490933037769/13685226294483544641028234720880000000000, 1812354990636177874773948755861568591967/5474090517793417856411293888352000000000)
24: (37840194084188749255377023658191669083593/27370452588967089282056469441760000000000, -124482995704700525327063405325202302567/13685226294483544641028234720880000000000, -2076916869558813707001326791170520975909/27370452588967089282056469441760000000000)
```

Exact volume:

```text
171065328681044308012852934011/750000000000000000000000000000
```

The exact oriented boundary sum gives first-moment numerators `(0,0,0)`, hence uniform centroid exactly `(0,0,0)`.

Complete maximal-face cycles:

```text
[0,3,1] [0,1,19] [0,23,3] [0,19,22] [0,22,20] [0,20,23] [1,3,21] [1,21,5] [1,5,24] [1,24,19] [3,23,21] [5,21,24] [16,20,21] [16,23,20] [16,21,23] [19,24,22] [20,22,21] [21,22,24]
```

Complete true-edge list:

```text
[0,1] [0,3] [0,19] [0,20] [0,22] [0,23] [1,3] [1,5] [1,19] [1,21] [1,24] [3,21] [3,23] [5,21] [5,24] [16,20] [16,21] [16,23] [19,22] [19,24] [20,21] [20,22] [20,23] [21,22] [21,23] [21,24] [22,24]
```

The candidate JSON also contains all 18 exact outward supporting planes and supports. Independent H-to-V reconstruction enumerates every feasible triple of those planes, recovers exactly the same 11 vertices, and recovers every plane–vertex incidence.

### Convexity and incidence

- `(V,E,F,C)=(11,27,18,54)` and `11-27+18=2`.
- Every maximal face is a strict supporting triangle.
- Minimum normalized nonincident face slack: `0.017651826202952955`.
- The full exact V-driven verifier enumerates all supporting triples rather than trusting the stored face list.
- The independent H-driven verifier reconstructs the V-representation from the 18 exact planes.
- OBJ and STL independently match all 11 coordinates and all 18 face triangles exactly at their decimal rendering.

### Exhaustive own-centroid mechanics

| kind | feature | normalized strict margin |
|---|---|---:|
| stable face | `[20,22,21]` | `0.023425046667674476` |
| stable face | `[0,3,1]` | `0.13713008445232253` |
| unstable vertex | `24` | `0.028364136348297854` |
| unstable vertex | `0` | `0.834885499986827` |
| saddle edge | `[16,20]` | `0.022197442396168388` |
| saddle edge | `[0,19]` | `0.022667576323702598` |

Nearest inactive witnesses are:

- face `[0,22,20]`: `-0.0018649237806778079`;
- vertex `5`: `-0.0033914244818561102`;
- edge `[16,21]`: `-0.011009065892925727`.

The exhaustive audit contains exact projection barycentrics for all 18 faces, all incident directional witnesses for all 11 vertices, and segment/cone coefficients for all 27 true edges. No feature is classified from a triangulation fragment or an auxiliary centre.

### Certified openness

An exact independent Fraction interval verifier proves that every Cartesian coordinate may vary independently by

```text
1/400000 = 2.5e-6
```

before recomputing the body’s own uniform centroid, while the complete face lattice and the full strict `(2,2,2)` class remain unchanged. Within this box the certified lower bounds are:

- nonincident support slack `> 0.004127410073402505`;
- selected positive equilibrium predicate `> 0.0012780437502318076`;
- selected inactive separation `> 0.00008312061183716522`.

This establishes that the endpoint is an open non-target body, not a wall point.

## Directed witness graph

The exact acyclic witness arcs are

```text
1→5, 3→21, 5→24, 16→21, 19→24,
20→0, 21→5, 22→24, 23→21
```

A topological sort exists; the sinks are exactly `[0,24]`, matching the exact unstable-vertex audit. Thus the requested cyclic obstruction has been removed, but the graph still has one extra sink.

## Proof-level obstruction for the realized complete-witness branch

The final true edge `[5,24]` gives an exact branch obstruction. Let centred endpoint vectors be `q5,q24` and define the two mutual vertex witnesses

```text
A = -q5·(q24-q5)
B = -q24·(q5-q24).
```

Identically,

```text
A+B = ||q24-q5||² > 0.
```

Therefore at least one of `A,B` is positive. In the complete witness branch containing the endpoint, every non-mutual incident witness at both vertices `5` and `24` is positive, and target vertex `0` is also unstable. Hence one of `5,24` must be an additional unstable vertex and `U≥2`; `(1,1,0)` is impossible throughout that branch.

This is not merely an endpoint identity. Exact rational interval arithmetic certifies the whole branch pattern and complete face lattice for every independent coordinate perturbation of radius

```text
1/1200 = 0.0008333333333333334
```

with the own uniform centroid recomputed for every box member. Thus the certified box contains no Gömböc. I do **not** promote this to an exclusion of all witness branches in the full combinatorial cell.

## Exact circuit cascade

A deterministic exact straight-line homotopy was built in the common label universe

```text
[0,1,2,3,4,5,11,12,14,15,16,19,20,21,22,23,24].
```

Inactive labels occupy distinct rational moment-curve points near the origin. For every four-label circuit, its determinant polynomial was formed over `Z`, every root in `(0,1)` was isolated exactly, and every complementary interval was sampled rationally. Each sample’s actual convex hull, own exact volume centroid, full face lattice and all equilibrium cones were rebuilt from scratch.

- exact isolated circuit roots: `2,586`;
- exact event clusters: `2,586`;
- distinct open face-lattice cells crossed: `31`;
- actual topology-changing transitions: `30`;
- independently verified circuit brackets on those transitions: `30`.

Open-cell class histogram:

| class | cells |
|---|---:|
| `(2,2,2)` | 3 |
| `(2,3,3)` | 9 |
| `(3,2,3)` | 11 |
| `(3,3,4)` | 6 |
| `(4,2,4)` | 1 |
| `(4,3,5)` | 1 |

The activation/deactivation events are:

| transition | deactivated | activated | exact circuit |
|---|---|---|---|
| `1→2` | `4` | — | `[1,4,5,14]` |
| `3→4` | — | `20` | `[0,12,15,20]` |
| `5→6` | `15` | — | `[0,15,16,20]` |
| `8→9` | `2` | — | `[0,2,3,16]` |
| `9→10` | `14` | — | `[0,5,11,14]` |
| `10→11` | — | `21` | `[5,11,16,21]` |
| `12→13` | `12` | — | `[0,11,12,20]` |
| `13→14` | — | `22` | `[0,5,11,22]` |
| `15→16` | — | `24` | `[0,5,22,24]` |
| `19→20` | `11` | — | `[11,20,21,22]` |
| `20→21` | — | `19` | `[0,1,5,19]` |
| `27→28` | — | `23` | `[3,16,20,23]` |

All six obsolete labels therefore disappear and all six replacement labels appear within one exact connected circuit cascade. The exact endpoint has the same final face lattice as the final open path cell but crosses additional equilibrium walls inside that lattice, ending at strict `(2,2,2)`.

## Search coverage and falsification attempts

The search was concentrated on the requested whole-block geometry rather than broad low-vertex enumeration. It included:

1. connected three- and four-node whole-block replacements with deletion of obsolete labels;
2. a second generation of 100 rebuilt hull cells around the best replacement;
3. 160 rebuilt cells forcing deletion of obstruction pair `[5,24]` and inserting a connected five-node replacement;
4. four-node bifurcated, second-block and explicit circuit-flip continuations, totalling 777 additional cell instances in the pre-reset runtime record;
5. exact/local witness-branch and MILP screens constrained to acyclic orientations.

No numerical state reached strict own-centroid `(1,1,0)`. These nonhits are empirical only. Runtime reset removed the raw optimization logs for the last three numerical waves, so their counts are retained as same-chat observations and are not presented as certificates. The exact endpoint, exact topology path and proof certificates were reconstructed and independently reverified after the reset.

## Smallest nonredundant continuation

Another four- to six-node local patch at the current endpoint is not supported by the geometry. For a directed witness edge `u→v`, negativity of `-u·(v-u)` implies

```text
R_v/R_u > sec(theta_uv).
```

For an `m`-edge chain, spherical triangle inequality and convexity of `-log cos` imply the necessary bound

```text
R_end/R_start > sec(Theta/m)^m.
```

Directed interval arithmetic at the exact endpoint certifies:

- routing sink `24` directly to target `0` cannot be done with `≤16` witness edges; the first edge count not excluded is `17`, requiring 16 intermediate vertices;
- deleting `5` and `24` exposes vertex `1`; routing `1` to `0` cannot be done with `≤7` edges; the first edge count not excluded is `8`, requiring 7 intermediate vertices.

These are necessary bounds for the fixed endpoint directions and radii, not global bounds under macroscopic deformation.

The smallest evidence-supported continuation is therefore:

1. deactivate `5` and `24` together;
2. replace the complete stars of `[5,24]`, saddle `[0,19]`, saddle `[16,20]`, and stable face `[20,22,21]` in one cascade;
3. insert at least a seven-intermediate-vertex acyclic strip routing the newly exposed vertex `1` toward target `0`, unless the endpoint directions/radii are moved enough to reduce the angular budget;
4. permit `16,19,20,21,22` to deactivate during the same cascade;
5. eliminate all three first moments as hard equations on every accepted branch.

This points to roughly 16–19 active vertices and, if the result stays simplicial, complexity about 84–102: still near the requested complexity-100 scale. A shorter serial cap, endpoint stack or local Y is now both empirically redundant and, for the fixed endpoint geometry, incompatible with the certified radial witness-length bound.

## Exact frontier accounting

No inherited low-vertex system was exactly closed here. The rigorous lower bound and unresolved counts therefore remain unchanged:

| quantity | exactly closed here | remaining |
|---|---:|---:|
| labeled necessary V8 systems | 0 | 24,835 |
| rooted automorphism orbits | 0 | 17,253 |
| stable-face chambers | 0 | 207,036 |

The journal’s prior exact theorem remains only `V≥8`; the unresolved V8 counts must not be reduced by numerical nonhits.

## Reproducibility artifacts

- Standalone Markdown handoff (`slot8_wholeblock_research_handoff.md`)
- Complete reproducibility bundle (`slot8_wholeblock_research_bundle.zip`)
- Bundle manifest with per-file SHA-256 (`slot8_wholeblock_research_manifest.json`)

### Exact endpoint

- Exact rational candidate, planes, faces and edges (`slot8_wholeblock_v11_exact_candidate.json`)
- Exhaustive exact all-feature audit (`slot8_wholeblock_v11_exact_audit.json`)
- Machine-readable endpoint report (`slot8_wholeblock_v11_exact_report.json`)
- Independent V-driven exact verifier (`slot8_wholeblock_v11_exact_verify.py`)
- V-driven verifier transcript (`slot8_wholeblock_v11_exact_verification.txt`)
- Independent H-to-V exact verifier (`slot8_wholeblock_v11_H_reconstruction_verify.py`)
- H-to-V verifier transcript (`slot8_wholeblock_v11_H_reconstruction_verification.txt`)
- Full-class interval-box verifier (`slot8_wholeblock_v11_fullclass_box_verify.py`)
- Full-class interval transcript (`slot8_wholeblock_v11_fullclass_box_verification.txt`)
- Vertex CSV (`slot8_wholeblock_v11_exact_vertices.csv`)
- OBJ (`slot8_wholeblock_v11_exact.obj`)
- STL (`slot8_wholeblock_v11_exact.stl`)
- Mesh correspondence verifier (`slot8_wholeblock_v11_mesh_verify.py`)
- Mesh verifier transcript (`slot8_wholeblock_v11_mesh_verification.txt`)

### Circuit path and obstruction

- Exact 31-cell topology path (`slot8_wholeblock_exact_topology_path.json`)
- Deterministic exact path generator (`slot8_wholeblock_exact_topology_path_generate.py`)
- Independent exact path verifier (`slot8_wholeblock_exact_topology_path_verify.py`)
- Path verifier transcript (`slot8_wholeblock_exact_topology_path_verification.txt`)
- Exact local obstruction certificate (`slot8_wholeblock_v11_obstruction_certificate.json`)
- Obstruction verifier (`slot8_wholeblock_v11_obstruction_verify.py`)
- Obstruction verifier transcript (`slot8_wholeblock_v11_obstruction_verification.txt`)
- Exact acyclic witness graph (`slot8_wholeblock_v11_witness_graph.json`)
- Witness-graph verifier (`slot8_wholeblock_v11_witness_graph_verify.py`)
- Witness-graph transcript (`slot8_wholeblock_v11_witness_graph_verification.txt`)
- Directed interval route-bound certificate (`slot8_wholeblock_radial_route_bound_certificate.json`)
- Route-bound verifier (`slot8_wholeblock_radial_route_bound.py`)
- Route-bound transcript (`slot8_wholeblock_radial_route_bound_verification.txt`)
- Machine-readable search report (`slot8_wholeblock_search_report.json`)

Candidate SHA-256: `5413323c19ce30ffddd498c1d306b511ffd88f9dd7b1f569d9f9057d7fd5b224`.

Audit SHA-256: `05748814f9ae678b633b12cc6fa79e90564cf47e44680dc2269f90bebce3ecf0`.

Exact topology-path SHA-256: `4f8bf26d73302f4e318b09f2f8118ef56879fc3d4e1b30989209902d97313774`.

## Bottom line

The requested whole-block surgery genuinely occurred: all six obsolete labels left the hull, a connected six-label replacement entered, both old saddles and the old extra stable/unstable features vanished together, and the final directed witness graph became acyclic. It still did not produce a Gömböc. The exact endpoint is an open `(2,2,2)` body, and its complete witness branch is rigorously obstructed by the persistent true edge `[5,24]`. The next operation must delete that edge’s two endpoints together and use a substantially longer acyclic routing strip; another small local Y-patch is no longer the smallest nonredundant move.


Bundle SHA-256: `10f78ffd9d09812ca285e18feb2a508b3b39c586697fae50463f817151614df5`.

Manifest SHA-256: `8861e8868e5e55b76fd84f451c4c3e3b0f51368dfa93d5fd8d62fb23907b908c`.
