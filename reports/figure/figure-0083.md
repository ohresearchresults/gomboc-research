# figure-0083

AI research report · 2026-08-26 UTC

---

# Determination

This continuation did **not** find a strict homogeneous polyhedral Gömböc. No candidate passed the required own-volume-centroid gate of exactly one stable maximal face, one unstable vertex, zero saddle edges, strict inactive incidence separation, and independent exact reconstruction. That remains the governing acceptance standard.

The strongest certified object therefore remains the exact rational `radial_balanced14` post-circuit body. The additional searches substantially broadened the tested topology cells, but their best states again had the same four-feature `(2,2,2)` Morse block. No new floating state was strong enough to justify replacing or re-exactifying the certified fallback.

**Authoritative exact archive:** sloan_connected_surgery_handoff.zip  
**SHA-256:** `07c2c806d7e5565c0a535c3d445f040d9b4d2824de656a81b9d5791f3809ddc8`

The journal’s earlier exact eight-vertex endpoint and its coupled two-circuit defect are preserved here as the starting point rather than being silently replaced by a generic mesh.

# Certified fallback: `radial_balanced14`

## Exact deterministic coordinates

Let

```text
D = 2^44 = 17592186044416.
```

The uncentred source vertices are `p_i=N_i/D`, with integer numerator triples

```text
 0   227980322548    -7122899858021    -3350595029242
 1  -3087971149305   -8087355464838    35189646231226
 2  -3071467763284   -3311752378671    -7793532719921
 3   564932692500    12322349993564   -22044504415082
 4  -1522457074152   -5585879705131    -1437753711053
 5   1019442028864   -6776734049428    14904485647874
 6  -1517739575269   11842062996071   -21575118419353
 7   751601034417     1912702043180    16456585107867
 8   1889832948677    1278241438745     4940899673202
 9   626244458195    12370106791179   -22016052856529
10   9407439271      -7305237352384     1656421435024
11   1122136464854   -6266881447399   -10121432657528
12   2143378442731    -724095943996    11639282669223
13   844679729955     5455372937131     3551669044291
```

Its exact uniform-volume centroid is

```text
cx = -10359287541913059028778747476388184027133087140155293
     /332230514328842032004430965217772987522249343406964736

cy = -12598077039212879414078725434672839154057739035839755
     /664461028657684064008861930435545975044498686813929472

cz =  71565702324626018658773463700226635871089698487968797
     /664461028657684064008861930435545975044498686813929472.
```

The certified centred vertices are exactly

```text
v_i = p_i - (cx,cy,cz).
```

Thus the exported body has all three uniform-volume first moments equal to zero as rational identities. Its exact volume is

```text
4721279571084011649935959059373729296599
/16333553612205046246241981156724874149888
```

or approximately `0.2890540346073921`.

Executable generator and complete tables:

- Exact source generator (`source_generator.py`)
- Exact centred V table (`vertices_exact.csv`)
- Exact maximal H table (`halfspaces_exact.csv`)
- Machine-readable certificate (`certificate.json`)

## Rebuilt maximal faces

```text
F00 [1,6,2]       F12 [3,9,11]
F01 [1,7,6]       F13 [0,5,10]
F02 [2,6,11]      F14 [0,11,5]
F03 [0,1,4]       F15 [1,10,5]
F04 [0,2,11]      F16 [1,5,12]
F05 [1,2,4]       F17 [8,9,12]
F06 [0,4,2]       F18 [1,12,7]
F07 [6,7,13]      F19 [9,13,12]
F08 [3,11,6]      F20 [7,12,13]
F09 [0,10,1]      F21 [5,11,12]
F10 [6,13,9]      F22 [8,12,11]
F11 [3,6,9]       F23 [8,11,9]
```

## Rebuilt true edges

```text
[1,6]   [2,6]   [1,2]   [1,7]   [6,7]   [6,11]
[2,11]  [0,1]   [1,4]   [0,4]   [0,2]   [0,11]
[2,4]   [6,13]  [7,13]  [3,11]  [3,6]   [0,10]
[1,10]  [9,13]  [6,9]   [3,9]   [9,11]  [0,5]
[5,10]  [5,11]  [1,5]   [1,12]  [5,12]  [8,9]
[9,12]  [8,12]  [7,12]  [12,13] [11,12] [8,11]
```

The published incidence files are maximal_faces.json and true_edges.csv.

## Exact convexity and incidence audit

```text
(V,E,F) = (14,36,24)
C       = 72
Euler   = 14 - 36 + 24 = 2
```

Every H row is an exact supporting plane of `conv(V)`. Every nonincident exact plane evaluation is strictly negative. The minimum nonincident geometric vertex-to-plane separation is

```text
0.0007479131952088098
```

and the RMS-normalized separation is

```text
0.0007431235654639509.
```

This raw incidence quantity is reported separately from the equilibrium margins; no equilibrium or incidence decision depends on a floating tolerance.

Complete inactive evaluations are in inactive_slack_audit.csv.

## Exhaustive own-centroid equilibrium class

The strict class is

```text
(S,U,H) = (2,2,2).
```

Preserved target features:

```text
stable F00 = [1,6,2]    margin 0.19812719892045302
unstable V1             margin 0.9611504610554218
```

Complete surviving defect:

```text
extra stable F22 = [8,12,11]  margin 0.0037606362202076615
extra unstable V3             margin 0.0037608315868475330
saddle [1,10]                 margin 0.0037613210175046563
saddle [9,13]                 margin 0.0037612468932605187
```

Closest strict exclusions among all other features:

```text
maximal face    -0.0020473107274696692
vertex          -0.0007071229030978928
true edge/cone  -0.0017549558683902656
```

Every edge value uses the complete four-component cone predicate: line projection parameters `t,1-t` and both normalized incident-normal coefficients. The detailed records are:

- All maximal-face predicates (`face_audit.csv`)
- All vertex normal-cone predicates (`vertex_audit.csv`)
- All true-edge full-normal-cone predicates (`edge_audit.csv`)

# New continuation work

## 1. Topology-free all-coordinate searches at 10, 12 and 14 input vertices

Large batched own-centroid searches were run from random spherical, anisotropic, spiral, multilayer and perturbed exact seeds. Each trajectory used the complete simplicial face, vertex and two-normal edge predicates; actual hulls were independently rebuilt during checkpoint audits, so vertices that became interior were not counted as active.

### Best completed 10-vertex state

Files: coordinates (`best.npy`), audit (`best.json`), run log (`global_N10.log`).

```text
(V,E,F)       = (10,24,16)
class         = (2,2,2)
normalized inactive separation = 0.0007339961590069191
hard defect   = -0.014594082286546316
```

Its complete positive block is

```text
stable [2,7,5]   0.10038802436697365
stable [9,3,8]   0.00957158088113224
unstable V8      0.8253351401854950
unstable V1      0.014594082286546316
saddle [2,5]     0.012738759070116982
saddle [8,9]     0.012741674645518230
```

This independently recreated the same one-extra-face, one-extra-vertex, two-saddle block without preserving the radial-balanced topology or labels.

### Best completed 12-vertex state

Files: coordinates (`best.npy`), audit (`best.json`), run log (`global_N12.log`).

```text
(V,E,F)       = (12,30,20)
class         = (2,2,2)
normalized inactive separation = 0.0013597213017964192
hard defect   = -0.0183622811950078
```

Positive block:

```text
stable [4,3,10]  0.029602108755609504
stable [1,8,0]   0.0012516616165361154
unstable V0      0.8072924463723298
unstable V2      0.0183622811950078
saddle [0,3]     0.013613707757224924
saddle [5,7]     0.013593682410617314
```

The 14-input search also terminated without a winner marker and did not improve on the certified exact endpoint or the 10-vertex checkpoint. Its files are retained under global_N14.

**Observation:** independent variable counts and unrelated initial geometries repeatedly converge to an open `(2,2,2)` block rather than to arbitrary many-feature clutter. This is empirical evidence of a robust transfer basin, not a global nonexistence theorem.

## 2. Explicit neighboring circuit cells around the 10-vertex state

All 22 realizable depth-one edge-flip topologies of the 10-vertex checkpoint were optimized with their actual own centroids and rebuilt hulls.

Files: topology-flip search (`topology_flip_beam.py`), results (`flip_N10_d1`), log (`flip_N10_d1.log`).

No cell produced `(1,1,0)`. The strongest audited state remained `(2,2,2)` with hard defect approximately

```text
-0.016438621714966878
```

and normalized inactive separation approximately

```text
2.3015e-5.
```

Thus ordinary adjacent flips around the best generic ten-vertex cell again transfer the four-feature block instead of cancelling it.

A larger target-preserving depth-two enumeration had not completed when this handoff was forced and is therefore excluded from the mathematical evidence. Its partial directory is flip_target_N10_d2.

## 3. Complete spanning-tree audit at the exact eight-vertex seed

For one strict triangulation of the nonsimplicial face of `trimmed_psi8`, all **6,435** primal spanning trees were enumerated with target unstable vertex `V1` and target stable face `[1,6,2]`. For each tree, the complementary dual tree and the corresponding unique parent witnesses were reconstructed.

Files: enumerator (`trimmed8_branch_enum.py`), all branches (`trimmed8_branches.json`), log (`trimmed8_branch_enum.log`).

At the exact seed coordinates, the best such coherent branch still requires a selected primal witness of

```text
0.937857229869982
```

and a selected dual-face witness of

```text
0.630377319388594.
```

These are macroscopic compared with the local saddle margins. This does **not** prove that the branch cannot be realized after large coordinate motion; it shows that the natural perfect-tree certificate is not a local continuation of the exact eight-vertex body.

## 4. Coupled primal/dual tree MILP at `radial_balanced14`

A binary mixed-integer model assigned each true edge either to a primal arborescence toward `V1` or to the complementary dual arborescence toward `F00`. Order variables excluded directed cycles. The objective globally minimized the sum of squared positive selected witnesses for that model.

Files: MILP generator (`rad14_tree_milp.py`), branches (`rad14_tree_branches.json`), log (`rad14_tree_milp.log`).

The sum-optimal branches already contain selected primal and dual witnesses as large as approximately

```text
primal  0.9736567167475723
dual    0.9085018748287358.
```

This explains why the subsequently optimized tree/cotree searches moved far away and produced classes such as `(2,4,4)` or `(2,5,5)`. The model is a sufficient perfect-Morse certificate, but it is substantially too restrictive for the current geometry.

The important correction is that a non-saddle edge need not be assigned globally to a primal endpoint witness or a dual face witness. Its full normal cone may instead be excluded by either incident-normal coefficient, and successful assignments can form cycles. The next solver must branch directly over all four edge components rather than force a tree/cotree partition.

## 5. Long ridge-zipper certificate search

An 18-link connected zipper spanning the original defect strip was given a coherent successor-tree/drainage-tree assignment and optimized from twelve independently realized convex topologies.

Files: search code (`zipper_tree_search.py`), results (`zipper_tree_m18`), log (`zipper_tree_m18.log`).

No winner appeared. The best audited state remained far from cancellation, around class `(2,3,3)` with hard defect approximately `-0.1314`. The failure is attributable to the overconstrained tree/cotree witness assignment, not to the mere presence of eighteen links.

## 6. Seeded eight-vertex global search

A 1,536-trajectory search was launched from exact `trimmed_psi8`, small exact-seed perturbations and independent eight-point geometries. It had not completed at the handoff boundary and produced no observed winner marker. Its partial files are under global_N8, but they are not counted as a completed negative result.

# What changed relative to the previous handoff

The prior conclusion was that the defect required a connected ridge bridge of roughly eighteen successor links or a macroscopic radial collapse. That remains correct, but the new work refines the architecture:

1. Merely adding eighteen vertices is insufficient when every edge is preassigned through a complementary primal/dual tree.
2. The same four-feature block reappears in unrelated 10- and 12-vertex cells, so it is not an artifact of the Sloan labels or the exact dyadic rounding.
3. Depth-one and sampled depth-two circuit changes transfer the block.
4. A viable ridge bridge must exploit **mixed edge-cone exclusions in cycles**, not only endpoint monotonicity and opposite-face drainage.
5. The two endpoint-saddle branches and the stable-face transfer ridge must be crossed in one combinatorial operation. Sequential crossings expose a replacement equilibrium before the previous one disappears.

# Precise remaining obstruction

At the exact fallback, the local maximum-transfer pair `V3,V9` is joined by an edge. Their mutual endpoint witnesses obey

```text
[-v3·(v9-v3)] + [-v9·(v3-v9)] = ||v9-v3||² > 0.
```

Therefore both endpoint inequalities cannot be negative simultaneously. Removing the maximum at `V3` transfers it to `V9` unless `V9` acquires a third outward successor or one endpoint ceases to be a hull vertex.

Dually, crossing the closest ridge of extra stable face `[8,12,11]` transfers stability to its neighboring face. The saddle at `[1,10]` transfers toward `[0,10]`; the saddle at `[9,13]` transfers toward the `7–13` branch. Generic 10- and 12-vertex searches reproduced the same endpoint/face/ridge structure with different labels.

The angular span between target maximum `V1` and the extra maximum direction is approximately `165.15°`, with radial ratio about `0.790`. A near-equal-radius monotone successor chain therefore needs roughly eighteen links; a six-link route would require the lower endpoint radius to fall below approximately `0.486` of the target radius. This remains a local quantitative obstruction rather than a universal low-vertex lower bound.

# Next nonredundant move

The next search should retain the exact `radial_balanced14` target face and target vertex but replace the full defect by a **bifurcated cyclic ridge bridge**:

- one branch supplies a third successor for the `V3/V9` maximum-transfer pair and joins the existing `13→7→1` ascent;
- a second, dual branch drains `[8,12,11]` toward `F00` without assigning every intermediate ridge to a complementary tree;
- both branches include the adjacent replacements of `[1,10]`, `[0,10]`, `[9,13]` and `[7,13]` in the same circuit block;
- obsolete vertices `3`, `8` or `9` may become interior during the accepted crossing;
- each true edge chooses freely among `t`, `1-t`, and both incident-normal coefficients as its strict negative separator;
- all coordinates are optimized with the body’s recomputed uniform centroid, followed by complete hull reconstruction at every circuit change.

A practical implementation is a branch-and-bound or mixed-integer nonlinear search over the four edge-cone witness choices on a 20–32-vertex Y-strip, rather than another fixed triangulation, metric orbit, isolated insertion, or spanning-tree certificate.

# Independent verification and exports for the certified fallback

Two exact rational reconstruction paths continue to pass:

```text
radial_balanced14 PASS V-driven exact rebuild
VEF (14,36,24), class (2,2,2)

radial_balanced14 PASS H-driven exact reconstruction
class (2,2,2), exact volume certified
```

- V-driven exact verifier (`verify_rebuild.py`)
- V-driven transcript (`verify_rebuild.log`)
- Independent H-driven verifier (`verify_independent.py`)
- H-driven transcript (`verify_independent.log`)
- Certified OBJ (`polyhedron.obj`)
- Certified STL (`polyhedron.stl`)

# Explicit incompleteness

`radial_balanced14` is not a Gömböc. It has one extra stable face, one extra unstable vertex and two saddle edges. The continuation produced no strict `(1,1,0)` state and no new exact object superior to this fallback. No formal all-coordinate perturbation-box radius was derived for the fallback; its exact strict rational signs nevertheless prove that its `(2,2,2)` class is open. The unfinished depth-two and seeded eight-vertex runs are preserved only as reproducibility material and are not presented as completed evidence.
