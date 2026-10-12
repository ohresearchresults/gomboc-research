# figure-0076

AI research report · 2026-08-26 UTC

<!-- historical-status:start -->
> **Historical AI report.** The title and claims below reflect the AI’s assessment at the time. Claims of proof, certification or completion are not a current verification verdict.
>
> [C622](../../C622/README.md) passes the supplied exact checks; the search for C<500 remains open. See [verification status and source gaps](../../catalog/coverage.md).
<!-- historical-status:end -->

---

# Bright Comet 68 — connected two-pair surgery handoff

## Determination

**No homogeneous convex polyhedral Gömböc was found.** No endpoint in this continuation has strict own-centroid class `(S,U,H)=(1,1,0)`, and no searched continuous family has been exactly excluded.

The requested acceptance gate remains a finite homogeneous convex polyhedron, evaluated at its own exact uniform-volume centroid, with exactly one stable maximal face, one unstable vertex, no saddle true edge, complete incidence, positive separation from every wall, independent verification, and OBJ/STL. Near-solutions and wall points do not qualify.

The continuation did, however, satisfy the central negative-result requirement: it produced and exactified a **connected simultaneous surgery in which both robust V10 core saddle edges `(0,4)` and `(2,5)` are absent in the same realized open cell**. They were not cancelled. The complete Euler-neutral defect migrated to a new connected block. This advances the previous state, where the exact V12 body reduced to a robust V10 `(2,2,2)` core and isolated caps or rails only transferred the two pairs.

## Strongest endpoint

The strongest materialized endpoint is an exact rational 11-vertex simplicial polyhedron with

- `(V,E,F,C)=(11,27,18,54)`;
- exact uniform-volume centroid `(0,0,0)`;
- strict class `(S,U,H)=(2,2,2)`;
- minimum normalized nonincident face slack `0.023587141411053458`;
- a connected retained surgery patch on construction labels `{11,12,14,15,16}`;
- neither original core edge `(0,4)` nor `(2,5)` present as a true edge.

The active construction labels are

```text
[0,1,2,3,4,5,11,12,14,15,16]
```

Coordinates were obtained by rounding the own-centred numerical endpoint to denominator `10^10`, recomputing its uniform-volume centroid in exact rational arithmetic, and subtracting that centroid exactly. Consequently every final coordinate and supporting plane is rational and the first moments vanish identically, not merely within floating tolerance.

### Complete positive-equilibrium audit

| kind | feature | normalized strict margin |
|---|---|---:|
| retained stable face | `[0,3,1]` | `0.22185707089478324` |
| extra stable face | `[0,12,15]` | `0.019012053270658143` |
| retained unstable vertex | `0` | `0.9844206342886205` |
| extra unstable vertex | `4` | `0.03189578952270954` |
| saddle edge | `[0,14]` | `0.027474484216739484` |
| saddle edge | `[0,15]` | `0.027964415688416674` |

These are rounded displays of exact rational predicates. The audit file contains, for every maximal face, vertex, and true edge:

- reduced rational coordinates, outward normals, and supports;
- all nonincidence slacks;
- exact projection barycentrics for face stability;
- exact values of `-v·(w-v)` on every incident edge for vertex instability;
- exact segment parameters and both normal-cone coefficients for every true edge;
- complete maximal-face cycles and the two incident faces of every true edge;
- every inactive equilibrium score, not only the six positive features.

The exact endpoint is therefore an open non-target body rather than a numerical wall. I did not derive a certified coordinate perturbation radius for this non-target class; the exact positive and inactive slacks needed for such a calculation are fully materialized.

### Independent verification

The standalone verifier uses Python's standard library and `fractions.Fraction`, independently recomputes the exact centroid and all feature predicates, and reports:

```text
verified=true, V=11, E=27, F=18, centroid=(0,0,0),
S=2, U=2, H=2, target=false,
original_core_saddles_absent_together=true, connected_patch=true
```

Artifacts:

- Exact endpoint coordinates, face cycles, and true edges (`slot8_connected_v11_IY_candidate.json`)
- Exhaustive exact all-feature audit (`slot8_connected_v11_IY_audit.json`)
- Independent Fraction verifier (`slot8_connected_v11_IY_verify.py`)
- Verifier transcript (`slot8_connected_v11_IY_verification.txt`)
- Decimal vertex CSV (`slot8_connected_v11_IY_vertices.csv`)
- OBJ (`slot8_connected_v11_IY.obj`)
- STL (`slot8_connected_v11_IY.stl`)
- Machine-readable endpoint report (`slot8_connected_v11_IY_report.json`)
- Endpoint manifest (`slot8_connected_v11_IY_manifest.json`)
- Exact endpoint bundle (`slot8_connected_v11_IY_bundle.zip`), SHA-256 `daed6ba9e4e5f2ae086c02e958dfc1f7988c7687fdc863753219ea41c299099c`

## Connected surgery and topology changes

The construction used two connected stages rather than independent endpoint caps.

### Stage 1: communicating strip

A first connected strip replaced both robust saddle neighborhoods. Its exact 11-vertex endpoint had `(2,2,2)`, minimum normalized nonincidence slack `0.018590366902318998`, and the following transferred block:

```text
stable faces:      [0,3,1]       +0.1606990015603922
                   [0,12,2]      +0.02192132584031288
unstable vertices: 0              +0.8490754078380052
                   4              +0.0333253962256178
saddles:           [0,10]         +0.02945505262585677
                   [2,13]         +0.02990892573068979
```

Both original core saddle edges were already absent, but the two pairs had transferred separately to the ends of the strip.

- Stage-1 exact candidate (`slot8_connected_v11_stage1_candidate.json`)
- Stage-1 exhaustive audit (`slot8_connected_v11_stage1_audit.json`)
- Stage-1 verifier (`slot8_connected_v11_stage1_verify.py`)
- Stage-1 transcript (`slot8_connected_v11_stage1_verification.txt`)
- Stage-1 OBJ (`slot8_connected_v11_stage1.obj`)
- Stage-1 STL (`slot8_connected_v11_stage1.stl`)
- Stage-1 exact bundle (`slot8_connected_v11_stage1_bundle.zip`), SHA-256 `2ba8d635009a3b7d60bb9ecc74b6b70c9f8497d6e1e98832b5136a0519f4fc10`

### Stage 2: connected Y replacement

A second three-node connected Y-patch was applied to the complete neighborhoods of transferred saddles `(0,10)` and `(2,13)`. Labels `10` and `13` became inactive, while labels `14,15,16` joined retained strip labels `11,12`. The final defect is no longer divided between the two original basins: both saddles now lie in the same star at vertex `0`, adjacent to extra stable triangle `[0,12,15]`, while vertex `4` remains the extra maximum.

Thus the assignment's simultaneous-disappearance condition is met, but the surgery demonstrates **whole-block transfer rather than Morse cancellation**.

## Exact topology path

I materialized a deterministic rational straight-line homotopy from the exact V10 core through the exact stage-1 strip to the exact final endpoint. Inactive labels were placed at distinct rational interior points so that every combinatorial event is represented by an actual four-point circuit rather than coincident dummy vertices.

Every four-point determinant polynomial was formed over the integers and its roots in `(0,1)` were isolated exactly. Every resulting open interval was sampled at a rational parameter, its convex hull rebuilt, and its complete face lattice and own-centroid equilibrium class audited using exact fractions.

| segment | isolated circuit roots | distinct open face-lattice cells |
|---|---:|---:|
| V10 core → stage 1 | `860` | `19` |
| stage 1 → final Y endpoint | `1,354` | `16` |
| total | `2,214` | `35` |

For each of the 35 cells the path artifact records:

- an isolating rational interval and rational sample parameter;
- active construction labels;
- every maximal-face cycle and true edge;
- exact volume and uniform centroid;
- exact equilibrium counts and saddle list;
- connectivity of the inserted patch;
- whether either original core edge remains.

Endpoint states are stored separately because an equilibrium wall can be crossed without a face-lattice change. The endpoint sequence is

```text
V10 core:  (2,2,2), saddles (0,4),  (2,5)
stage 1:    (2,2,2), saddles (0,10), (2,13)
final:      (2,2,2), saddles (0,14), (0,15)
```

The independent path verifier checked all 35 exact sampled cells and the three endpoints and reports:

```text
verified=true, exact_fraction_cells_checked=35, segments=2,
final_counts=(2,2,2),
final_original_core_saddles_absent_together=true
```

- Exact 35-cell topology-path record (`slot8_connected_two_pair_exact_topology_path.json`)
- Independent exact path verifier (`slot8_connected_two_pair_path_verify.py`)
- Path-verifier transcript (`slot8_connected_two_pair_path_verification.txt`)
- Deterministic topology-path generator (`exact_topology_path.py`)

Path-record SHA-256: `b8891d3bc59d718289a23cedf6b59d057df9519980e3b552e545291176df4532`.

## Search and attempted falsification

The search was deliberately concentrated on the concrete two-pair geometry rather than broad low-vertex enumeration.

1. The first connected-strip wave rebuilt and optimized `126` distinct fixed hull cells. No target cell was found. The cleanest endpoint became the exact stage-1 object above.
2. The second connected-Y wave generated and optimized `120` distinct three-point Y cells around the two transferred saddle stars. No target cell was found. The strongest endpoint became the exact final object above.
3. Every numerical evaluation rebuilt the actual convex hull, integrated its own uniform-volume centroid, translated to that centroid, and classified all actual maximal faces, vertices, and true edges. No auxiliary mechanical center was used.
4. Fixed-cell hard-centroid nonlinear optimization, determinant-one metric deformation, and direct local sign forcing all approached transfer or collision walls rather than a strict target.
5. A general first-order complete-witness screen of the stage-1 cell sampled `35,000` separator branches. Nominally positive linear branches all contained directed witness cycles, principally `4↔5`, so they could not represent a globally monotone vertex field.
6. An exhaustive acyclic local screen enumerated all `18` admissible live-vertex witness assignments and `41,472` compatible complete face/edge branches. Its best linear margin was `-0.6470475222145826`.
7. On the final Y cell, another `35,000`-branch screen found nominal positive margins only in cyclic assignments, chiefly `1↔4` or `4↔5`; no local acyclic assignment survived the chosen live-witness threshold.

These screens are useful diagnostics, not exact infeasibility certificates. They linearize within fixed realized cells and do not exclude macroscopic coordinate changes, additional vertices, or different circuit sequences.

- First strip search, shard 0 (`batchA0.log`)
- First strip search, shard 1 (`batchA1.log`)
- Y-patch search, shard 0 (`batchIY0.log`)
- Y-patch search, shard 1 (`batchIY1.log`)
- Stage-1 general branch screen (`scr11_35.json`)
- Stage-1 exhaustive acyclic screen (`scr11_acy.json`)
- Final-cell general branch screen (`scrIY_35.json`)

## Smallest remaining whole-block operation

Another serial cap, isolated saddle split, endpoint stack, or three-node Y attached to the current witnesses is not justified: the 120-cell Y wave already shows that this operation relays the Euler-neutral block into the star of vertex `0`, and the fixed-cell witness screens require directed cycles before all unwanted signs can be reversed.

The smallest remaining operation supported by the evidence is a **four-node communicating bifurcated strip**, or a three-node strip combined with simultaneous deactivation of at least two obsolete vertices. It must replace, in one rebuilt cell:

- the complete stars of saddle edges `[0,14]` and `[0,15]`;
- extra stable triangle `[0,12,15]` and its full one-ring;
- the outgoing one-ring of extra unstable vertex `4` and its connection to the inserted strip.

The operation should permit vertex `4` or one of its current positive-side neighbors, together with one of strip vertices `11` or `12`, to become non-extreme during the same circuit cascade. The inserted complex should have an acyclic directed witness graph leading to retained maximum `0`, rather than the observed `1↔4` or `4↔5` cycle. The three exact first-moment equations and retained face/vertex inequalities must be eliminated as hard constraints on every circuit branch.

This suggests roughly `11–14` active vertices and complexity below about `80`. The important distinction is that the entire migrated `S/U/2H` block must be replaced at once; extending only one of the two saddle fans is now an empirically exhausted transfer mechanism.

## Exact frontier accounting

No exact low-vertex system was closed in this continuation. The rigorous lower bound therefore remains `V>=8` and the inherited remainder is unchanged:

| quantity | inherited | exactly closed here | remaining |
|---|---:|---:|---:|
| labeled necessary V8 systems | `24,835` | `0` | `24,835` |
| rooted automorphism orbits | `17,253` | `0` | `17,253` |
| stable-face chambers | `207,036` | `0` | `207,036` |

- Machine-readable frontier counts (`slot8_frontier_counts.json`)

## Bottom line

This continuation did not produce the requested Gömböc and does not prove that the searched topologies are impossible. Its reusable result is an exact, open, complexity-54 connected surgery endpoint plus an exact 35-cell topology path proving that both original robust saddle edges disappear together. The failure mode is now sharper: the two original pairs communicate, but instead of cancelling they coalesce into one connected extra-stable/extra-unstable/two-saddle block around the retained maximum. The next operation must replace that whole block while simultaneously breaking the cyclic vertex-witness structure.
