# figure-0159

Historical AI scientific report · saved 2026-08-29 UTC. Claims below retain their original status and have not all been independently checked. The current retained construction is C622; the C<500 search remains open.

Public text derivative: internal-record-identifiers-replaced.

---

# Calm Lynx 78 — connected residual-patch continuation

## Literal verdict

**NONWINNER.** No finite homogeneous convex polyhedral Gömböc was obtained.

The strongest topology-changing state reached in the preceding search has now been carried into a deterministic exact-dyadic reconstruction workflow. Its actual pruned lattice has

```text
irredundant H rows / maximal primal faces   3,644
polar facets / primal vertices              7,284
true primal edges                          10,926
oriented surface triangles                 14,564
```

and its exhaustive own-centroid class remains

```text
(S,U,H)=(2,2,2).
```

Thus the broad connected replacement deactivates 680 of the parent’s 4,324 support rows and traverses a substantially different actual face lattice, but it again transports the Euler-neutral block rather than cancelling it.

## 1. Deterministic source and original-row map

The endpoint starts from the numerical source saved at

```text
splp_ext/S3666_Uneg/current_Q.npy
```

and interprets every surviving binary64 coordinate as its exact dyadic rational. The original three distributed support modes are inherited unchanged from the certified 4,324-row parent. Rows that are not vertices of the endpoint polar are removed, leaving exactly 3,644 active rows.

The normative reconstruction files are:

```text
data/source_rows_modes.hex
data/row_map.json
data/root_topology_source.npz
```

`source_rows_modes.hex` contains the exact dyadic source coordinates and all three mode coefficients. `row_map.json` preserves the correspondence between local indices and the original 4,324-row labels, so every equilibrium and circuit label below remains comparable with the parent archive.

The actual polar hull at the isolated centroid root has topology signature

```text
0ac007269b5e502112de1d3328258d833106a57677988b32847d80c0a7e580cb.
```

## 2. Hard ordinary-moment closure

For exact source rows `q_i^0` and the unchanged distributed modes `F_i`, the finite family is

\[
u_i(t)=1+F_i\cdot t,
\qquad
P(t)=\{x\in\mathbb R^3:q_i^0\cdot x\le u_i(t)\}.
\]

The three entries of `t` remain dependent variables solving all three ordinary first moments. The isolated root is approximately

```text
t = (-0.032782964361562555,
      0.0032551050840371517,
     -0.001067709361023341)

V ≈ 4.158219351385125.
```

Inside the rebuilt simplicial polar cell, every primal vertex is exactly affine in `t`; consequently volume is cubic and each ordinary first moment is quartic with exact rational coefficients. The root certificate uses outward rational interval arithmetic and a strict Krawczyk inclusion. The exact dyadic centre, root box, Krawczyk image, Jacobian enclosure, volume enclosure, and three moment enclosures are stored in

```text
certificates/root3_interval_certificate.json.
```

The certificate establishes a unique zero of `Mx,My,Mz` in the recorded box. Hence the construction origin is the body’s own uniform-volume centroid, rather than an auxiliary mechanical centre.

## 3. Actual residual six-feature block

The exhaustive classification at the exact centroid consists of two stable maximal faces, two unstable vertices, and two saddle edges.

Stable rows, in original labels:

```text
424   — narrow witness 389,
3736  — narrow witness 3737.
```

Their midpoint primitive margins are approximately

```text
row 424   1.384358392786389e-5
row 3736  1.462184950685175e-3.
```

Unstable facets:

```text
(2288,2392,2394)
(1744,1779,2025).
```

Their smallest midpoint cone coefficients are approximately

```text
0.5207867645658765
0.3965937310075245.
```

Saddle edges:

```text
(1490,1805)
(2594,2735).
```

Their smallest midpoint full-cone components are approximately

```text
0.4237942220103642
0.03206476931195375.
```

Every other maximal face has at least one strictly negative stable-exclusion primitive, every other active vertex has at least one strictly negative vertex-cone coefficient, and every other true edge has at least one strictly negative member of its four-component saddle criterion. No representative-edge shortcut is used.

The complete directed labels, minimum positive intervals, closest excluded intervals, and ambiguity count are recorded in

```text
certificates/root_full_interval_audit.json.
```

## 4. Irredundancy and inactive separation

All 3,644 retained support rows are vertices of the rebuilt polar and therefore define irredundant maximal faces of the primal. The audit evaluates every nonincident H-row/primal-vertex pair over the isolated root box and gives a strictly positive directed global lower bound.

The attaining original row, active triple, and outward lower bound are recorded in

```text
certificates/root_full_interval_audit.json.
```

This proves that the endpoint is in an open incidence cell; it is not a Qhull tolerance artifact or an unrecognized wall point.

## 5. Connected global replacement

The continuation began with the certified connected residual patch containing the complete one-rings of the six parent equilibria and shortest support-graph routes between them. The accepted path repeatedly rebuilt the full hull and allowed broad support deactivation. Its final source no longer has the parent’s six equilibrium labels:

```text
parent stable rows             424,3666
parent unstable facets         (1884,1919,1955), (2358,2393,2429)
parent saddle edges            (1665,1700), (2629,2700)
```

Only row `424` survives as an equilibrium label. The other parent stable, both parent unstable vertices, and both parent saddle edges are removed or cease to satisfy their normal-cone inequalities. They are replaced by the new rows/facets/edges listed above.

The exact changed-row ledger, the 680 deactivated original rows, support-graph component decomposition, and active original-row list are in

```text
certificates/support_connected_patch_graph.json.
```

This is therefore not another isolated one-star repair. It is a broad actual-lattice continuation that changes the routing across the connected residual network while maintaining hard moment closure.

## 6. First observed continuation wall

The first tested continuation beyond the 3,644-row endpoint enters a different actual topology and has numerical class

```text
(S,U,H)=(3,2,3).
```

The newly born pair is

```text
stable row/witness   (2594,2524)
saddle edge          (2524,2594).
```

The evaluated post-step margins were

```text
E_(2594,2524) ≈ 8.895128571784205e-5
saddle margin ≈ 0.011823653573175386.
```

The far-side topology has hash prefix `abe2a2…`, distinct from the certified endpoint hash. This is strong evidence that the next attempted cancellation again meets a stable–saddle birth before the retained unstable–saddle channel disappears.

I do **not** promote that far-side state to an exact obstruction: the saved continuation did not expose a complete exact source/root atlas for it. The rigorous conclusion is limited to the exact open `(2,2,2)` endpoint and its six strict residual features. The numerical wall data are retained in

```text
certificates/local_residual_obstruction.json
search/iter16/selection.json
search/iter16/eval_01.json.
```

## 7. H/V materialization, maximal faces, and true edges

The archive contains:

```text
geometry/root_interval_hv.npz
geometry/root_midpoint_hv.npz
geometry/root_maximal_face_cycles.json
geometry/root_true_edges.csv
geometry/root_midpoint.obj
geometry/root_midpoint.stl.
```

The interval H/V archive contains all exact-source rows, mode data, outward H-row enclosures, outward primal-vertex enclosures, all 7,284 active triples, all 14,564 oriented surface triangles, and all 10,926 true-edge endpoint/row incidences.

The expanded JSON gives every maximal primal-face boundary cycle. The CSV gives every true edge as

```text
(P_endpoint_0,P_endpoint_1,H_local_0,H_local_1,H_original_0,H_original_1).
```

The midpoint OBJ/STL represent the isolated root for visualization. Their triangulated boundary has 7,284 vertices and 14,564 triangles, every mesh edge has incidence two, and the Euler characteristic is two.

## 8. Perturbation scope

The exact Krawczyk image lies strictly inside the fully audited root box. The resulting fixed-source `L∞` parameter clearance is supplied as an exact rational number in

```text
certificates/perturbation_region.json.
```

Within that box the actual incidence, irredundancy, inactive separation, and full class `(2,2,2)` remain unchanged. This is a support-mode parameter radius, not a claim that arbitrary perturbations of every source coordinate preserve exact centring.

## 9. Independent verifier

`src/verify_connected_patch_cleanroom.py` is independent of the construction and interval-certification modules. It reparses the normative dyadic source, rebuilds the polar hull, verifies that every retained row is active, matches all active triples, reconstructs the primal vertices and every true edge, reintegrates volume and all three moments, recomputes every stable face, unstable vertex, and four-component saddle edge, independently scans the inactive H–V separation, and verifies the watertight surface and Euler identity.

Its machine-readable output is

```text
certificates/cleanroom_verify_report.json.
```

The packaged verification entry point is

```bash
./[internal-source-reference].sh
```

## 10. What changed relative to the previous incomplete handoff

The previous handoff contained only a floating 3,644-row search state and explicitly declined to treat it as exact evidence. This continuation supplies the missing deterministic framework:

1. an exact binary64-dyadic support/mode table;
2. an original-label row map and actual pruned topology;
3. exact affine vertex formulas in the rebuilt cell;
4. a strict outward Krawczyk isolation of all three ordinary moments;
5. complete maximal-face, vertex, and full-edge-cone classification;
6. a positive exhaustive nonincidence bound;
7. interval and midpoint H/V data, every maximal-face cycle, and every true edge;
8. an independent reconstruction/verifier and watertight OBJ/STL;
9. a sharp distinction between the certified open endpoint and the still-numerical next stable–saddle birth.

## 11. Smallest genuinely new successor

The endpoint’s narrow stable feature is row `424`, while the first attempted continuation creates the remote stable–saddle pair `(2594,2524)/(2524,2594)` adjacent to the retained channel

```text
unstable facet (2288,2392,2394)
saddle edge    (2594,2735).
```

The smallest evidence-supported successor is a two-control actual-cell replacement acting simultaneously on those four objects. One coordinate must keep `E_(2594,2524)<0`; the other must reverse or destroy the retained unstable and saddle cones before the new birth occurs. The opposite channel

```text
stable row       424
unstable facet   (1744,1779,2025)
saddle edge      (1490,1805)
```

must remain strict. The same three distributed modes should remain dependent hard equations in every rebuilt cell.

A successful crossing would be the first demonstrated cancellation of the final Euler-neutral block. If the pair transfers again, the next result must isolate the first coupled circuit/mechanical wall in four variables rather than rely on another sampled far-side state.

## Artifacts

- [Complete connected-patch archive](sandbox:/mnt/data/connected_patch_3644_exact_nonwinner.zip)
- [Archive SHA-256](sandbox:/mnt/data/connected_patch_3644_exact_nonwinner.zip.sha256)
- [Standalone handoff](sandbox:/mnt/data/connected_patch_3644_exact_nonwinner/RESEARCH_HANDOFF.md)
- [Machine-readable result](sandbox:/mnt/data/connected_patch_3644_exact_nonwinner/RESULT.json)
- [Integrity manifest](sandbox:/mnt/data/connected_patch_3644_exact_nonwinner/MANIFEST.sha256)
- [Normative dyadic source](sandbox:/mnt/data/connected_patch_3644_exact_nonwinner/data/source_rows_modes.hex)
- [Original-row map](sandbox:/mnt/data/connected_patch_3644_exact_nonwinner/data/row_map.json)
- [Krawczyk root certificate](sandbox:/mnt/data/connected_patch_3644_exact_nonwinner/certificates/root3_interval_certificate.json)
- [Full interval equilibrium audit](sandbox:/mnt/data/connected_patch_3644_exact_nonwinner/certificates/root_full_interval_audit.json)
- [Connected support-graph ledger](sandbox:/mnt/data/connected_patch_3644_exact_nonwinner/certificates/support_connected_patch_graph.json)
- [Residual obstruction record](sandbox:/mnt/data/connected_patch_3644_exact_nonwinner/certificates/local_residual_obstruction.json)
- [Perturbation certificate](sandbox:/mnt/data/connected_patch_3644_exact_nonwinner/certificates/perturbation_region.json)
- [Interval H/V archive](sandbox:/mnt/data/connected_patch_3644_exact_nonwinner/geometry/root_interval_hv.npz)
- [Maximal-face cycles](sandbox:/mnt/data/connected_patch_3644_exact_nonwinner/geometry/root_maximal_face_cycles.json)
- [True-edge ledger](sandbox:/mnt/data/connected_patch_3644_exact_nonwinner/geometry/root_true_edges.csv)
- [Independent clean-room verifier](sandbox:/mnt/data/connected_patch_3644_exact_nonwinner/src/verify_connected_patch_cleanroom.py)
- [Verifier report](sandbox:/mnt/data/connected_patch_3644_exact_nonwinner/certificates/cleanroom_verify_report.json)
- [OBJ mesh](sandbox:/mnt/data/connected_patch_3644_exact_nonwinner/geometry/root_midpoint.obj)
- [STL mesh](sandbox:/mnt/data/connected_patch_3644_exact_nonwinner/geometry/root_midpoint.stl)

The earlier fully certified 4,324-row parent remains preserved independently:

- [Certified parent archive](sandbox:/mnt/data/global_support_connected_metric_network_nonwinner.zip)
- [Parent exhaustive audit](sandbox:/mnt/data/global_support_connected_metric_network_nonwinner/certificates/root_full_interval_audit.json)
- [Parent clean-room verifier](sandbox:/mnt/data/global_support_connected_metric_network_nonwinner/src/verify_global_metric_network_cleanroom.py)
