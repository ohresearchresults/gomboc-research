# figure-0153

AI research report · 2026-08-29 UTC

---

# Calm Atlas 34 — broad-gate relay atlas and strongest finite endpoint

## Literal verdict

No homogeneous convex polyhedral Gömböc was obtained. The strongest unrestricted separator chamber found still has negative margin

`-0.000127018499211593`.

Accordingly, I did **not** introduce Santaló or moment equations, did not materialize this support state as a new polyhedron, and make no own-centroid equilibrium claim. This respects the journal’s acceptance gate: a valid completion must be a finite own-centroid uniform-density body with strict `(S,U,H)=(1,1,0)`, complete H/V incidence, all-feature audit, independent verification, and mesh exports; near-solutions and auxiliary-centre mechanics do not qualify. :contentReference[oaicite:0]{index=0}

The broad wall-242 gate is also **not proved infeasible**. What is now established is a long exact-combinatorial matching relay with fourteen new support-minimal exact positive circuits in its early part and a substantially improved, still numerical, current endpoint.

---

## 1. Geometry and topology held fixed

All work remained in the exact denominator-`2^104` wall-242 adjacent fan. No further hull wall was crossed. The fixed actual fan has

`(V,E,F)=(4321,12957,8638)`.

Its exact rebuilt geometry, irredundant H/V representation, 8,638 maximal triangular faces, all 12,957 true edges, exact one-wall determinant audit, watertight OBJ/STL, and independent verifier remain in the predecessor archive:

- [Exact wall-242 geometry and matching archive](sandbox:/mnt/data/calm_atlas34_matching_atlas.zip)
- [Exact H-representation](sandbox:/mnt/data/calm_atlas34_matching_atlas/geometry/Q_wall242_H_irredundant.csv)
- [Exact V-representation](sandbox:/mnt/data/calm_atlas34_matching_atlas/geometry/Q_wall242_V_exact.csv)
- [All true edges](sandbox:/mnt/data/calm_atlas34_matching_atlas/geometry/Q_wall242_true_edges.csv)
- [Baseline independent verifier](sandbox:/mnt/data/calm_atlas34_matching_atlas/verify_matching_atlas.py)

The root vertex remained `0` and the root maximal face remained `5546`.

Every retained matching was constructed by a genuine directed alternating cycle in the edge-to-target bipartite graph. After every exchange I checked:

1. all 12,957 actual true edges are owned exactly once;
2. the 4,320 vertex-owned edges form one connected component on all 4,321 vertices and hence a primal spanning tree;
3. the complementary 8,637 face-owned edges form one connected component on all 8,638 maximal faces and hence a dual spanning tree.

The exact component verdict was `[1,1]` for every retained state `C5` through `C81`, and for the strongest final trial described below. No graph-only diagonal or stale-incidence claim is used.

---

## 2. Exact circuit mechanism

For the exact source-ray numerators `n_i` and positive supports `G_i`, the vertex separator assigned to `v→w` is

`(n_v·n_w)G_v - ||n_v||²G_w > 0`.

For a face assignment `f→g`, with `p_f(G)=N_f^{-1}G_f`, the face separator is

`(p_g(G_ref)-p_f(G_ref))·p_f(G) > 0`.

Each exact infeasibility certificate consists of primitive integer row covectors `a_r` and positive rationals `lambda_r` satisfying

`sum_r lambda_r a_r + e_0 = 0`.

Dotting this identity with a support vector satisfying all strict separators and `G_0>0` would give `0>0`. The square row subsystem in every reported exact certificate has nonzero determinant, so the displayed positive dependence is support-minimal.

A useful exactification procedure emerged for broad floating duals. When HiGHS omits a numerically tiny selected separator:

1. quotient the exact row space of the reported dual support by pivot columns;
2. compute the residual of `e_0` in that quotient;
3. search the currently selected separator rows for a negative proportional quotient response;
4. append that row;
5. solve the exact rational dependence;
6. prune rows whose exact multiplier is zero.

This converted apparently broad nonsquare supports into exact oriented-matroid circuits at `C12`, `C14`, and `C18`.

---

## 3. New support-minimal exact circuits

Fourteen retained matchings now have exact positive-circuit certificates:

| State | Numerical separator margin | Exact circuit support | Independent columns |
|---|---:|---:|---:|
| `C5` | `-3.039030991244745e-4` | 107 | 106 |
| `C6` | `-3.013602242928561e-4` | 64 | 63 |
| `C7` | `-2.964317716447797e-4` | 91 | 90 |
| `C8` | `-2.932104515396758e-4` | 119 | 118 |
| `C9` | `-2.851550406749456e-4` | 103 | 102 |
| `C10` | `-2.799300598244275e-4` | 101 | 100 |
| `C11` | `-2.790502906838690e-4` | 37 | 36 |
| `C12` | `-2.789336356496733e-4` | 142 | 141 |
| `C13` | `-2.779872609551487e-4` | 44 | 43 |
| `C14` | `-2.690070671215782e-4` | 116 | 115 |
| `C15` | `-2.563026038991934e-4` | 24 | 23 |
| `C16` | `-2.531087974529193e-4` | 111 | 110 |
| `C18` | `-2.490485642289890e-4` | 107 | 106 |
| `C20` | `-2.478225204719528e-4` | 121 | 120 |

Selected detailed certificates:

- [C5 exact circuit](sandbox:/mnt/data/calm_atlas34_broad_gate_resolution/exact_circuits/C5_f1742_short_exact.json)
- [C12 exact completed circuit](sandbox:/mnt/data/calm_atlas34_broad_gate_resolution/exact_circuits/C12_exact.json)
- [C14 exact completed circuit](sandbox:/mnt/data/calm_atlas34_broad_gate_resolution/exact_circuits/C14_exact.json)
- [C15 24-row exact circuit](sandbox:/mnt/data/calm_atlas34_broad_gate_resolution/exact_circuits/C15_exact.json)
- [C16 exact circuit](sandbox:/mnt/data/calm_atlas34_broad_gate_resolution/exact_circuits/C16_exact.json)
- [C18 exact completed circuit](sandbox:/mnt/data/calm_atlas34_broad_gate_resolution/exact_circuits/C18_exact.json)
- [C20 exact circuit](sandbox:/mnt/data/calm_atlas34_broad_gate_resolution/exact_circuits/C20_exact.json)

The most informative completed broad reductions are:

### C12

The numerical support was completed with

`vsep:3163:3199:9744`.

After pruning fourteen exact-zero rows, the circuit has 142 rows: 128 vertex separators, 13 face separators and `G_0>0`. Its square determinant has 13,800 bits and residue `2006288205` modulo `2147483647`.

### C14

The same omitted row

`vsep:3163:3199:9744`

completes the numerical support. Four zero rows prune away, leaving 116 rows: 102 vertex separators, 13 face separators and positivity. The determinant has 11,411 bits and residue `1696835857`.

### C18

The reported dual had 107 rows on 108 columns. Quotient completion identified

`fsep:4981:3401:10051`.

Two rows then received exact zero multipliers and were pruned:

- `fsep:3401:4793:10459`;
- `fsep:4793:4794:10460`.

The final support-minimal circuit has 107 rows: 91 vertex separators, 15 face separators and positivity. Its determinant has 10,775 bits and residue `60353048`; the smallest positive rational multiplier is approximately `3.60e-56`.

### C20

The circuit is square without completion: 100 vertex rows, 20 face rows and positivity. Its determinant has 12,539 bits and residue `1874886062`; its smallest positive multiplier is approximately `3.17e-55`.

The exact certificates were generated from the source numerators and actual wall-242 incidence, not from rounded row coefficients.

---

## 4. Broad matching relay

The original four-gate margins were near `-3.0435e-4`. The best retained path now reaches `-1.2907e-4`, and one further verified trial reaches `-1.2702e-4`. This removes about 58.3% of the original negative defect magnitude without changing the fan.

Numerical unrestricted margins along the retained path were:

```text
C5  -3.039030991e-4   C10 -2.799300598e-4   C15 -2.563026039e-4
C20 -2.478225205e-4   C25 -2.420529072e-4   C30 -2.372925491e-4
C35 -2.302624489e-4   C40 -2.121327730e-4   C45 -1.924864127e-4
C50 -1.800197072e-4   C55 -1.754174253e-4   C60 -1.648794226e-4
C65 -1.567083112e-4   C70 -1.471288950e-4   C75 -1.393606603e-4
C80 -1.291893512e-4   C81 -1.290712602e-4   B*  -1.270184992e-4
```

The full retained sequence is monotone in its accepted numerical margin. The state files store the parent state and the exact candidate names inserted on each alternating cycle.

Important relay events include:

- The initial dominant common row `fsep:1742:3103:10715` was replaced by `fsep:1742:1724:10621` and `vsep:3504:3505:10715`, giving exact circuit `C5`.
- The C11 broad face row `fsep:6698:8087:839` was hit by `fsep:6698:5350:842` and `vsep:247:277:839`, leading to completed exact circuit `C12`.
- The C13 row `fsep:2092:4908:770` was exchanged through `fsep:2092:2090:880`, `vsep:401:229:773`, and `vsep:229:259:770`, leading to completed exact circuit `C14`.
- The C17/C18 seam was relayed through `fsep:6422:6423:9349` and `vsep:3306:3055:9451`.
- The subsequent dominant pair was moved through `fsep:7034:7035:2803` and `vsep:836:835:2800`, producing exact circuit `C20`.
- At later broad plateaus, the best exit was often **not** one of the largest dual rows. Examples are:
  - `C58→C59`: hit `fsep:5516:5514:10168` with a three-row cycle;
  - `C70→C71`: hit `fsep:5555:5554:10789` with `fsep:5555:3882:10688` and `vsep:3638:3529:10789`;
  - `C72→C73`: hit `vsep:3744:3745:11443` with `vsep:3744:3781:11445` and `fsep:2366:2365:11443`;
  - `C79→C80`: hit the relatively low-weight row `vsep:1583:3744:5163` with `vsep:1583:3708:5162` and `fsep:2364:5581:5163`.

These events materially change the search strategy. Pivoting only the largest numerical dual row is unreliable: its shortest alternating cycle can worsen the margin from roughly `-1.4e-4` to `-7e-4` or `-1e-3`. Broad circuit clauses must be branched over their full support, including low-weight rows.

---

## 5. Strongest retained matching and strongest trial

### Retained state C81

`C81` is a literal primal-tree/complementary-dual-tree matching on the exact wall-242 fan. Its unrestricted separator margin is

`-0.0001290712601628387`.

The corresponding numerical support solution remains well inside the imposed support box:

- minimum support: `0.9984293696953312`;
- maximum support: `1.2929656758543173`;
- no support bound is active.

Artifacts:

- [C81 matching state](sandbox:/mnt/data/calm_atlas34_broad_gate_resolution/states/C81_state.npz)
- [C81 numerical LP result](sandbox:/mnt/data/calm_atlas34_broad_gate_resolution/results/C81_result.json)
- [C81 full support and dual arrays](sandbox:/mnt/data/calm_atlas34_broad_gate_resolution/results/C81_full.npz)

### Strongest trial B*

Starting from `C81`, I branched the row

`fsep:905:2045:5880`

through the genuine four-target alternating cycle

1. `fsep:905:2035:5987`;
2. `fsep:2035:2036:6095`;
3. `fsep:2036:906:9421`;
4. `vsep:3045:1820:5880`.

The resulting edge ownership is still bijective, its primal edges form one spanning tree, and its complementary dual edges form one spanning tree. Its unrestricted numerical separator margin is

`-0.000127018499211593`.

Three other rows in the same numerical obstruction produced the same next margin to approximately `1.6e-10`, revealing another matching diamond rather than an isolated lucky pivot.

Artifacts:

- [B* matching state](sandbox:/mnt/data/C81_top_probe/task_0042.npz)
- [B* LP result](sandbox:/mnt/data/C81_top_probe/result_0042.json)
- [All 100 C81 broad-gate trial definitions](sandbox:/mnt/data/C81_top_probe/manifest.json)

`B*` has not yet been exactified. Its negative margin is therefore a numerical obstruction, not an exact Farkas clause.

---

## 6. What changed relative to the supplied journal

The journal ended with four exact `2×2` gate matchings near `-3.0435e-4` and an unresolved 812-row/932-variable common component. The new work shows:

1. The four-row gate is not a terminal matching obstruction. Ownership can be relayed repeatedly through valid tree/cotree exchanges while improving the separator margin by more than a factor of two.
2. Broad floating duals can often be reduced to finite support-minimal rational circuits by one-dimensional quotient completion rather than a monolithic 812-by-812 determinant.
3. Fourteen new exact matching clauses are now materialized, including circuits as small as 24 rows and as large as 142 rows.
4. The dominant obstruction migrates through widely separated primal and dual regions. It is not confined to the original rows `vsep:3469:3505:10622` and `fsep:1742:3103:10715`.
5. Numerical dual magnitude is a poor branching priority. Several decisive improvements came from rows carrying only `10^-3` to `10^-2` dual weight, while shortest pivots on the largest rows were catastrophic.
6. No topology change is yet forced by the evidence: the same exact fan still admits substantial matching-space improvement.

---

## 7. Certification boundary and incompleteness

### Completed exactly

- The underlying wall-242 H/V/incidence object and every true edge.
- Literal primal-tree/complementary-dual-tree validity of every retained exchange and of `B*`.
- Fourteen new support-minimal rational positive circuits through `C20`.
- Full integer row reconstruction for those circuits.
- Positive rational multipliers and nonzero exact or modular determinants.
- Deterministic cycle generation, matching application and LP reconstruction scripts.

### Not completed

- No positive unrestricted separator chamber.
- No exact circuit for `C17`, `C19`, `C21–C81`, or `B*`.
- The predecessor’s 74-clause hitting-set computation has not yet been recomputed after adding the fourteen new exact clauses.
- The later numerical relay is not an exact infeasibility theorem for the broad gate.
- No new hull wall was classified or crossed.
- No Santaló root, normalized centroid enclosure, polar-denominator certificate, own-centroid full-normal-cone audit, perturbation box, or new OBJ/STL was produced, because the prerequisite positive separator chamber was not reached.
- The new working tree was not consolidated into a single immutable ZIP before the runtime boundary. The decisive files are individually linked above.

Thus the correct conclusion is neither a winner nor a closed broad-gate theorem. It is a substantially advanced exact/numerical matching atlas with a sharply identified next unclassified clause.

---

## 8. Deterministic continuation

The strongest next move is now specific:

1. Promote `B*` to the next retained state.
2. Re-solve it with the full-support solver and exactify its dual support.
3. If the reported support is square, use direct exact rational elimination. If it has one extra column, apply quotient completion. If the codimension is larger, decompose the row-column incidence graph, eliminate leaf components, and exactify only the root-connected component.
4. Append the resulting exact separator support as a clause to the original 74 clauses and the new `C5–C20` clauses.
5. Recompute the exact minimum hitting sets.
6. Branch **every changeable row in the new exact circuit**, not only the largest dual rows. For each row, enumerate genuine alternating cycles and retain only matchings that pass both tree checks.
7. Solve each matching in a fresh HiGHS process; repeated solves in one Python process were observed to hang.
8. Cross a hull wall only if the exact clause atlas closes the current-fan matching branches or if a wall directly changes the face incidences participating in the new circuit. The first local incidence packet worth testing, if matching exhaustion requires it, is the `905–2035–2036–906` face chain used by `B*`.
9. Introduce localized moment-null controls and hard Santaló centring only after an exact support vector with `t>0` exists.

The central scripts are:

- [Alternating-cycle relay controller](sandbox:/mnt/data/relay_controller.py)
- [Top-circuit branch generator](sandbox:/mnt/data/generate_top_cycles.py)
- [Specified-row cycle generator](sandbox:/mnt/data/generate_specific_cycles.py)
- [Full LP support/dual materializer](sandbox:/mnt/data/solve_state_full.py)
- [Direct square exactifier](sandbox:/mnt/data/exactify_result_circuit.py)
- [Quotient-completion exactifier](sandbox:/mnt/data/exactify_with_completion.py)
- [Numerical quotient-row finder](sandbox:/mnt/data/find_completion_candidates_numeric.py)

The first continuation target is therefore not another broad search report. It is the exact positive circuit or certified positive separator margin of the already materialized `B*` tree/cotree matching.
