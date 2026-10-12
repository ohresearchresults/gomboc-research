# figure-0065

AI research report · 2026-08-25 UTC

---

# Chiral multilayer-tower search: self-contained handoff

## Verdict

**No strict own-centroid homogeneous polyhedral Gömböc was found.** Every candidate was evaluated at its own uniform-volume centroid, with maximal coplanar faces merged before reconstructing true edges. Auxiliary-center successes, degenerate wall points, and incomplete layer realizations were rejected, in accordance with the assignment’s acceptance boundary.

The strongest robust, fully active multilayer body found has six horizontal levels, 26 vertices, 40 true edges, 16 maximal faces, and complexity `C=80`. Its own-centroid equilibrium class is **`(S,U,H)=(2,2,2)`**. It is therefore four equilibrium features short of the target: one unwanted stable face, one unwanted unstable vertex, and two saddle edges must be removed, while the intended lower cap is presently not stable. This is a genuine open numerical body rather than a transfer-wall artifact, but it is not a Gömböc.

A second search state approached the target inequalities more closely, reaching normalized target hard score about `-6.99e-4`, but its minimum active-support separation was only about `3.03e-8`; it lies on the explicitly identified circuit wall and was rejected as non-open.

## Materialized fallback body

The selected fallback is the full-active projective–affine six-level tower:

- Expanded 26-coordinate candidate (`proj_affine_clean_aligned.npz`)
- Unaligned generating coordinates and transformation data (`proj_affine_clean_raw.npz`)
- Deterministic reconstruction script (`reconstruct_clean.py`)
- Hull, centroid, maximal-face, true-edge, and normal-cone auditor (`tower_geom.py`)

The NPZ field `points` is the complete `26×3` vertex matrix in the vertex numbering used below. No input point is inactive.

### Layer parameterization

The body is the convex hull of five polygonal layers and one apex. The exact layer membership in the expanded coordinate matrix is:

```text
L0 = [0,1,2,3,4]             z = -1.000000000000
L1 = [5,6,8,10,12]           z = -0.868083182478
L2 = [7,9,11,13,14]          z = -0.654027205497
L3 = [15,16,18,20,22]        z = -0.469504606200
L4 = [17,19,21,23,24]        z = -0.248346510981
L5 = [25]                    z =  1.000000000000
```

All five polygonal sections are pentagons. They are independently shifted, rotated, and anisotropically scaled; the resulting body is a very thin chiral ribbon-like tower rather than a concentric or homothetic stack. Approximate planar summaries are:

```text
L0 center ≈ (0,0),          x-range ≈ [-13.3347,15.4912], y-range ≈ [-0.0534,0.0534]
L1 center ≈ (5.2763,0.0538)
L2 center ≈ (13.8380,0.1410)
L3 center ≈ (21.2180,0.2162)
L4 center ≈ (30.0640,0.3064)
apex      ≈ (79.9946,0.8152,1)
```

The extreme anisotropy is intrinsic to the best projective–affine result, not a display transformation.

### Realized hull and mass properties

```text
active vertices       V = 26
true edges            E = 40
maximal faces         F = 16
complexity             C = V+E+F-2 = 80
volume                  = 7.349064157524082
uniform centroid        = (27.07840761, 0.27594510, -0.32299412)
independent volume      = 7.349064157524082
independent centroid    = (27.07840761, 0.27594510, -0.32299412)
centroid discrepancy    ≤ 3.56e-15 coordinatewise
characteristic scale    = 93.32931743727103
minimum true-edge length = 0.14787814957272316
minimum triangular double area = 0.2374155123286441
minimum normalized nonincident support separation ≈ 1.63538e-4
```

The first mass computation is the signed sum of origin-based tetrahedra over an outward-oriented triangulation of every maximal face. The independent computation uses positive tetrahedra formed from an interior point and the same oriented boundary triangles. Their volumes and first moments agree to floating-point roundoff.

The reconstruction code does not treat Qhull triangles as physical faces. It groups coplanar support triangles into maximal polygonal faces, cyclically orders every face, and then defines true edges as polygon-boundary pairs with exactly two incident maximal faces.

## Exhaustive equilibrium result for the fallback

Scores below are signed Euclidean feature margins. Positive face scores mean the centroid’s perpendicular projection is strictly inside the maximal face. Positive vertex scores mean the centroid-to-vertex vector lies strictly inside the vertex normal cone. Positive edge scores mean the perpendicular foot is in the edge interior and both incident-normal coefficients are positive.

### Stable maximal faces

Exactly two maximal faces are stable:

| Face id | Maximal-face cycle | Raw score | Normalized score |
|---:|---|---:|---:|
| 12 | `(16,17,25,24)` | `0.047533480517930174` | `5.09309e-4` |
| 13 | `(18,21,25,19)` | `0.07399703599510662` | `7.92860e-4` |

The intended lower support cap is maximal face id 1, with cycle `(3,2,0,1,4)`. Its projection margin is negative:

```text
lower-cap score             = -0.32746329071886277
normalized lower-cap score  = -0.00350868623
minimum raw edge-cross sign = -3.930240560945716
```

Thus the fallback’s two stable equilibria are side quadrilaterals incident to the apex, not the lower cap.

### Unstable vertices

Exactly two vertices are unstable:

| Vertex | Raw score | Normalized score | Minimum angular score |
|---:|---:|---:|---:|
| 3 | `1.0506031943197935` | `0.0112569471541` | `0.0259924676850` |
| 25 | `52.919795793233995` | `0.567022209595` | `0.999703792127` |

Vertex 25 is the intended upper apex and is very robustly unstable. Vertex 3, on the lower pentagon, is the unwanted maximum.

### Saddle true edges

Exactly two true edges are saddles:

| Edge | Raw score | Normalized score | Projection parameter `t` | Incident-cone coefficients |
|---|---:|---:|---:|---|
| `(5,9)` | `0.19387679066410823` | `0.00207734071123` | `0.0152229932513` | `(0.638432365287, 0.735514642431)` |
| `(23,25)` | `1.022490390564624` | `0.0109557255816` | `0.323263350706` | `(1.02506370967, 1.02249039056)` |

The exhaustive result is therefore

```text
(S,U,H) = (2,2,2)
S + U - H = 2
```

The Euler–Poincaré/Morse consistency check passes.

The complete cycles and edge incidences are rebuilt when `PolyAudit` loads the linked point matrix. The auditor asserts that every boundary edge has exactly two maximal-face incidences; no cap triangulation diagonal is counted as a true edge.

## Why the fallback was selected

Several states had a smaller numerical target defect, but they were supported only by nearly vanishing incidence separation. The selected body is the lowest-defect candidate found that simultaneously retained:

1. all 26 input vertices as actual hull vertices;
2. all six distinct horizontal layers;
3. a well-resolved realized topology;
4. positive nonincident support separation and nonzero face areas;
5. an unambiguous own-centroid `(2,2,2)` audit.

The near-wall alternative is available for continuation but must not be presented as an open body:

- Near-wall own-centroid optimizer endpoint (`nl_actual_best.npz`)
- Near-wall optimization transcript (`nl_actual.log`)

Its class is `(4,3,5)`, normalized target hard score approximately `-6.98875e-4`, and normalized minimum active-support separation approximately `3.03e-8`.

## Searches performed beyond the journal

### 1. Unequal-layer topology-free sampling

A dynamic hull search sampled 50,000 towers across 19 layer-cardinality patterns, including unequal sections such as `(5,3,1)`, `(3,4,1)`, and longer three-to-six-level stacks. Every accepted sample was re-hulled and audited at its own volume centroid. The strongest raw count pattern in this search was `(3,3,4)` in a `(5,3,1)` family, but its target hard score remained strongly negative. No `(1,1,0)` sample appeared.

Artifacts:

- Unequal-layer search driver (`search_mixed_random.py`)
- Stored mixed-family candidates (`mixedruns`)

This experiment rules out only the sampled parameter distributions, not the complete unequal-layer family.

### 2. Full projective–affine orbit of the six-level seed

A layer-preserving projective map, followed by a general determinant-one positive metric, gives a six-parameter orbit after removing translations, rotations, and uniform scale. Global differential-evolution and local nonsmooth searches were run over this orbit. This was the route that produced the robust `C=80` fallback.

The orbit crosses genuine mechanical and incidence walls. It did not locate an own-centroid target chamber. Its best robust endpoint moves the stable equilibrium from the lower cap to two apex-side quadrilaterals while retaining one lower maximum and two saddles.

Artifacts:

- Projective–affine search (`proj_affine_search.py`)
- Search transcript (`proj_affine_search.log`)
- Best transformed body before clean reconstruction (`proj_affine_best.npz`)

### 3. Own-centroid fixed-cell and topology-changing continuation

Starting from the clean projective–affine body, all planar coordinates and all intermediate heights were optimized against the body’s recomputed volume centroid. Fixed-topology sequential linear maximin steps, differentiable soft-min continuation, NLopt, and explicit circuit crossings were tested.

The most important realized circuit is the four-vertex circuit

```text
{3,10,11,20}
```

with old diagonal `10–11` and alternate diagonal `3–20`. Immediately before the wall, vertex 3 approaches face `(20,11,10)` while vertex 20 approaches face `(10,11,3)`. The normalized support distances reached approximately `7.94e-10` and `2.15e-9` respectively. Explicitly crossing the circuit changed the realized hull, but the own-centroid class remained `(4,3,5)` and the target score plateaued near `-8.61e-4`. The operation transferred the equilibrium block rather than cancelling it.

Artifacts:

- Own-centroid sequential maximin optimizer (`own_layer_slp.py`)
- Explicit circuit-crossing driver (`cross_clean_circuit.py`)
- Circuit-crossing transcript (`cross_clean_circuit.log`)
- Post-crossing candidates (`cross_clean_best0.npz`)

A second earlier free-layer continuation crossed the distinct side circuit whose diagonal changed from `7–16` to `12–13`. The post-flip branch reduced the reference-centroid error but met a subsequent unstable–saddle wall before reaching the own centroid.

- Post-flip seed (`postflip_centered.npz`)
- Post-flip continuation endpoint (`postflip_cont_best.npz`)
- Continuation transcript (`postflip_cont.log`)

### 4. Lower-layer moment actuation

Ten thousand broad random affine deformations of the lower two layers were evaluated. Some bodies made the designated lower pentagon stable and retained apex 25 as unstable, but this required expansions large enough that most intermediate vertices became strictly interior. The best such sampled count was `(2,2,2)` with only 12 active vertices. Its unwanted unstable vertex and saddle margins were macroscopic, so it is not a useful near-cancellation state and no longer represents the intended active multilayer routing architecture.

Artifacts:

- Lower-layer affine search (`random_base_affine.py`)
- Search transcript (`random_base_affine.log`)
- Stored best samples (`base_affine_best.pkl`)

### 5. Symmetric helical subfamily

A separate search sampled concentric but independently twisted regular pentagonal towers with three, four, and five polygonal levels plus an apex. In the completed 20,000-sample three-ring run, the lowest equilibrium count was repeatedly `(6,6,10)`: the intended axial equilibria plus one fivefold orbit of stable faces, one fivefold orbit of unstable vertices, and two fivefold saddle orbits. No sample had fewer defects. This is evidence that exact fivefold symmetry compresses cancellation into simultaneous five-feature walls, but it is not an impossibility proof.

- Symmetric global sampler (`search_symmetric_global.py`)
- Completed three-ring transcript (`symglobal_R3.log`)

### 6. Horizontal slices of an analytically centered smooth Sloan body

Several towers were generated from horizontal sections of the exactly centered Sloan-type smooth Gömböc. Direct low-order section samplings produced classes no better than approximately `(4,16,18)` for triangular sections, with counts worsening as the polygon order increased. The failure agrees with the journal’s warning that generic dense inscribed meshes proliferate mixed polyhedral equilibria.

- Sloan horizontal-slice generator and auditor (`sloan_tower.py`)
- Search output (`sloan_tower.out`)

## Architecture-specific obstruction isolated

The evidence supports the following sharply limited obstruction, not a generic nonexistence claim:

> In the investigated Q-polar-derived six-level tower, moving enough uniform volume toward the lower cap while retaining all layers forces the first full-active continuation through coupled side circuits. The circuit `10–11 ↔ 3–20` transfers, rather than cancels, the active face/vertex/edge block. Macroscopic lower-layer expansions can make the lower cap stable, but only after deactivating most intermediate-layer vertices; the surviving hull then retains an open side stable face, a lower unstable vertex, and two saddles. Within the exactly fivefold subfamily, the same transfer occurs simultaneously in five copies and the smallest sampled class is `(6,6,10)`.

Thus the practical obstruction is not the centroid polynomial itself. Both centroid computations are stable, and numerous controls move all three centroid coordinates. The obstruction is maintaining a complete active helical side rail while changing which face receives the stable projection. Current deformations either:

- preserve the active six-level rail but leave the lower cap outside its stable chamber;
- cross a circuit that transfers the same Morse block to the alternate diagonal; or
- expand the lower layers enough to center the volume but make intermediate layers inactive.

This conclusion applies only to the explored Q-polar-connected chambers, sampled regular-ring families, and tested unequal-layer distributions. It does not exclude a disconnected asymmetric multilayer chamber.

## Strongest continuation

The next nonredundant search should not continue single-diagonal polishing. It should replace the complete circuit strip containing vertices `{3,10,11,20}` and both apex-side stable quadrilaterals with an **asymmetric unequal-cardinality rail** while simultaneously imposing:

```text
lower-cap margin                   ≥ ε
apex unstable margin               ≥ ε
all other face and vertex scores   ≤ -ε
all edge cone/endpoint scores       ≤ -ε
all input layer vertices active
nonincident support separation      ≥ ε_top
three volume first-moment equations = 0
```

A promising finite pattern is a five-vertex lower cap, a seven-to-nine-vertex first rail, two staggered four-to-six-vertex middle sections, one three-to-five-vertex terminal ring, and one apex. This remains within six levels and comfortably below complexity 1000. The extra first-rail vertices should span the old and new diagonals simultaneously, allowing the lower stable projection and the lower maximum–saddle transfer to occupy different cells instead of opposite sides of one four-point circuit. Fivefold symmetry should be broken from initialization, not perturbed only after a symmetric wall is reached.

## Verification and export status

The linked `tower_geom.py` is sufficient to reproduce the floating-point hull, mass properties, maximal-face cycles, true-edge incidences, and every equilibrium score. It contains two independent centroid decompositions and rejects nonmanifold merged-face reconstructions.

However, because no winner was found, the following requested acceptance artifacts were **not completed**:

- exact rational or interval rationalization of a `(1,1,0)` body;
- an independent exact-Fraction verifier separate from the discovery code;
- a certified coordinate perturbation radius for a winning chamber;
- final deterministic OBJ and STL files.

The deterministic export procedure is nevertheless straightforward: load the `points` matrix, reconstruct `PolyAudit(points).faces`, emit each maximal cycle as a one-indexed OBJ face, and triangulate each cycle by the outward fan `(v0,vi,vi+1)` for STL. The cycles produced by `PolyAudit` are outward oriented and the same fan is used in both centroid decompositions. No claimed winner or prize-grade artifact should be inferred from the fallback files.
