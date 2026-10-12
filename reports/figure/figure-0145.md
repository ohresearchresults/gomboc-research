# figure-0145

AI research report · 2026-08-29 UTC

---

# Calm Atlas 34 — exact matching/circuit atlas for the wall-242 fan

## Determination

No literal homogeneous polyhedral Gömböc was reached. I do **not** claim an own-centroid strict `(S,U,H)=(1,1,0)` body, and I do not infer an own-centroid equilibrium class for any newly branched support state lacking a completed centring/full-normal-cone audit.

The continuation nevertheless resolves the requested separator-only obstruction substantially. It produces a finite exact atlas on the 4,321-vertex wall-242 adjacent fan, branches through genuine alternating cycles rather than preserving the transferred assignment, and reduces 74 distinct exact separator obstructions to one finite `2×2` gate. All four gate matchings remain literal primal spanning trees with complementary dual spanning trees, but their unrestricted homogeneous separator margins are still negative. The first unclassified object is now a sharply localized broad separator subsystem, not the old 35-row circuit and not a vague request for more smoothing.

The complete deterministic archive is:

- Calm Atlas 34 matching atlas ZIP (`calm_atlas34_matching_atlas.zip`) — SHA-256 `fcf5a5ddedc1bffbea8da5ba8d91cca66ff246607fd559ceeaea00c29a63d350`.
- Self-contained README (`README.md`).
- Independent exact/numerical verifier (`verify_matching_atlas.py`).
- Combined verification report (`verification_report.json`).

The exact verifier passed a fresh hull reconstruction, the complete integer H/V audit, every retained tree/cotree check, independent reconstruction of every exact separator row, all rational circuit identities, all modular nonsingularity checks, and the hitting-set enumeration. A separate HiGHS pass reproduced the five reported numerical separator margins.

---

## 1. Exact finite geometry retained throughout

The topology base is the already crossed wall-242 adjacent body, now materialized as a complete exact H/V object. Its coordinates are

`q_i = N_i / 2^104`,

with integer triples `N_i`. A fresh actual-hull rebuild from all 4,321 coordinates gives

`(V,E,F)=(4321,12957,8638)`.

All 4,321 candidate rows are active. Relative to the preceding fan, exactly one old edge circuit changes sign:

- removed true edge `[71,107]`;
- added true edge `[70,108]`;
- removed maximal triangles `[70,71,107]` and `[71,107,108]`;
- added maximal triangles `[70,71,108]` and `[70,107,108]`.

Of the 12,957 old edge circuits, 12,956 preserve sign, one flips, and none vanishes. The minimum absolute integer old-circuit determinant is

`207055948124322281632802332031948397089984057088155679079968752001479358797074923520`.

The rebuilt body has one primitive irredundant integer H-row per maximal triangle. Every H-row has exactly its three declared contacts and strictly positive slack at all remaining vertices. The global minimum positive integer vertex–facet slack is

`29890442683482497395876674334140810873863310762993270968584250496809794344960`.

Every one of the 12,957 true edges has exactly two oppositely oriented incident maximal faces. The mesh exports are watertight.

Exact geometry artifacts:

- Dyadic coordinate generator/state (`Q_wall242_dyadic.npz`).
- Complete exact V-list (`Q_wall242_V_exact.csv`).
- Complete primitive irredundant H-list (`Q_wall242_H_irredundant.csv`).
- All maximal-face cycles (`Q_wall242_faces.csv`).
- Every true edge and both incident faces (`Q_wall242_true_edges.csv`).
- Exact one-wall audit (`wall242_summary.json`).
- OBJ (`Q_wall242.obj`) and STL (`Q_wall242.stl`).

No further hull wall was used in this continuation. Every matching branch below is owned on this rebuilt actual fan; no graph-only diagonal or stale triangulation claim is made.

---

## 2. Exact separator and matching formulation

Let `n_i` be the exact integer source-ray numerator and use positive homogeneous supports `G_i`, so

`Q(G)=conv{n_i/G_i}`.

For a directed primal witness `v→w`, the exact strict separator is

`(n_v·n_w)G_v - ||n_v||²G_w > 0`.

For a triangular maximal face `f`, let `N_f` have the three incident ray numerators as rows and put

`p_f(G)=N_f^{-1}G_f`.

At the exact wall-242 reference support define

`d_fg=p_g(G_ref)-p_f(G_ref)`.

The directed dual-face exclusion row is

`d_fg·p_f(G)>0`.

Both types are rational homogeneous linear covectors. Every exact certificate stores a primitive integer version, and the independent verifier reconstructs it from `Q46.npz`, the dyadic radial numerators, the actual face list and the actual edge-face incidence. It does not merely trust the embedded coefficients.

The edge-to-target matching has one target for every nonroot vertex and every nonroot maximal face. A retained matching is accepted only if:

1. it is a bijection from all 12,957 targets to all 12,957 actual true edges;
2. every vertex target owns an incident true edge;
3. every face target owns a true edge incident to that maximal face;
4. the 4,320 vertex-owned edges form a connected primal spanning tree on 4,321 vertices;
5. the complementary 8,637 face-owned edges form a connected dual spanning tree on 8,638 maximal faces.

All base, branch, gate and deeper states reported below pass these literal checks.

---

## 3. Initial post-flip circuit `C0`

The transferred wall-242 matching has numerical unrestricted separator margin

`t=-0.0003095961494305788`.

It is blocked by a support-minimal exact positive circuit containing:

- 33 directed vertex separators;
- two directed face separators;
- the positivity row `G_0>0`.

The circuit has support size 36 on 35 support columns. Its first 35 primitive rows form a nonsingular square matrix; the determinant has 3,341 bits and residue `683583580` modulo `2147483647`. Every dependence weight is positive, with the smallest approximately `2.027250124320346e-51`. Consequently the selected strict separator system is impossible even before incidence or Santaló equations are imposed.

Certificate:

- Exact post-flip `C0` (`base_exact_positive_circuit.json`).

This is the clause that the present continuation branches rather than preserving.

---

## 4. Complete first-level alternating-cycle atlas

For each of the 35 changeable separator rows of `C0`, I found its shortest genuine alternating cycle in the edge-to-target bipartite graph, exchanged edge ownership along that cycle, rebuilt the complete matching, and rechecked both trees. All 35 branches remain valid primal-tree/complementary-dual-tree assignments.

Every one of the 35 branches is blocked by a support-minimal exact rational positive circuit. The archive contains all certificates and their SHA-256 manifest:

- Level-1 exact atlas manifest (`manifest.json`).

The best first-level margin is

`t=-0.00030867281301196576`.

It is reached through two different first-gate exchanges:

### First gate A1

Remove `vsep:243:419:824` via the three-cycle

- `vsep:243:247:820`;
- `vsep:247:419:842`;
- `fsep:5350:5345:824`.

### First gate A2

Remove `fsep:5350:6698:842` via the two-cycle

- `fsep:5350:5349:820`;
- `vsep:247:419:842`.

Although these cycles differ, their numerical dual supports exactify to the same next circuit `C1`. Thus the first exact obstruction has been reduced to a genuine two-way ownership gate rather than merely relabelled.

`C1` has support size 44 on 43 columns: 38 vertex rows, five face rows and `G_0>0`. Its square determinant has 4,305 bits and residue `1619232489` modulo `2147483647`; all rational weights are positive.

- Exact `C1` certificate (`C1_exact_positive_circuit.json`).

---

## 5. Complete second-level shortest-cycle atlas

Starting from the A1 realization of `C1`, I branched every one of its 43 changeable rows by its shortest genuine alternating cycle. All 43 descendants remain literal primal and complementary dual spanning trees.

Results:

- 41 branches have support-minimal exact positive-circuit certificates;
- two branches have broad numerical dual supports that are not square and were not falsely promoted to exact circuits.

The complete branch data and exact certificates are in:

- Level-2 exact atlas manifest (`manifest.json`).
- All 43 numerical shortest-cycle branches (`level2_shortest_cycle_atlas.json`).

The two non-exactified branches are the second gate:

### Second gate B1

Remove `vsep:225:401:755` via

- `vsep:225:229:751`;
- `vsep:229:401:773`;
- `fsep:3462:3461:755`.

Its numerical margin is

`t=-0.0003043489476763845`.

### Second gate B2

Remove `fsep:3462:2092:773` via

- `fsep:3462:3463:751`;
- `vsep:229:401:773`.

Its numerical margin is

`t=-0.00030434931923494895`.

These branches are not claimed exact-infeasible. They define the first broad separator gate.

---

## 6. Deeper exact clause chain

A clean branch was followed beyond `C1` to determine whether the obstruction could be walked away from without entering the broad gate.

### `C2`

Change `vsep:229:225:751` using

- `vsep:229:303:771`;
- `fsep:3463:3462:751`.

The resulting separator margin is

`t=-0.0003080518411822166`.

The exact positive circuit has support size 45, determinant bit length 4,397 and modular residue `572004113`.

### `C3`

Change `vsep:303:225:753` using

- `vsep:303:266:912`;
- `fsep:5052:3463:753`.

The resulting margin is

`t=-0.0003071084336339199`.

The exact positive circuit has support size 46, determinant bit length 4,486 and residue `537357477`.

### `C4`

Change `vsep:266:225:752` using

- `vsep:266:228:767`;
- `vsep:228:225:750`;
- `fsep:5051:5052:752`.

The resulting margin is

`t=-0.00030709922779674156`.

The exact positive circuit has support size 44, determinant bit length 4,381 and residue `1714683400`.

Certificates:

- Exact `C2` (`C2_exact_positive_circuit.json`).
- Exact `C3` (`C3_exact_positive_circuit.json`).
- Exact `C4` (`C4_exact_positive_circuit.json`).

Hitting the new `C4` face row `fsep:2092:4908:770` with the four-cycle

- `fsep:2092:3462:773`;
- `fsep:3462:3463:751`;
- `fsep:3463:2082:771`;
- `vsep:229:259:770`

reaches the strongest unrestricted separator margin found in this continuation:

`t=-0.0003043488650897158`.

The resulting edge assignment still passes both tree checks. Its numerical dual is broad, however, and no support-minimal exact circuit was isolated. This is therefore a numerical endpoint only, not a rational impossibility theorem.

- Strongest broad branch record (`strongest_broad_branch.json`).

---

## 7. Exact 74-clause hitting-set theorem

The finite exact clause atlas uses 80 certificate inputs:

- the initial `C0` certificate;
- 35 exact first-level branches;
- 41 exact second-level branches;
- `C2`, `C3`, and `C4`.

`C1` is also archived and independently verified, but it duplicates the level-1 branch-27 separator support and is omitted from the 80-input hitting-set count.

After duplicate separator supports are merged, the atlas contains:

- 74 distinct exact clauses;
- 199 distinct changeable separator rows.

No single row intersects all 74 clauses. Exhaustive exact pair enumeration shows that the minimum hitting-set cardinality is two and that there are exactly four minimum pairs:

1. `{fsep:3462:2092:773, fsep:5350:6698:842}`;
2. `{fsep:3462:2092:773, vsep:243:419:824}`;
3. `{fsep:5350:6698:842, vsep:225:401:755}`;
4. `{vsep:225:401:755, vsep:243:419:824}`.

Equivalently, every known exact obstruction is hit by choosing one row from

`A={vsep:243:419:824, fsep:5350:6698:842}`

and one row from

`B={vsep:225:401:755, fsep:3462:2092:773}`.

This is the exact finite `2×2` reduction.

- Complete exact hitting-set data (`hitting_set_clauses.json`).

The independent verifier reconstructs the 74 unique clauses from the certificate files, proves their intersection is empty, enumerates all candidate pairs, and reproduces exactly these four and no others.

---

## 8. Literal evaluation of all four `2×2` gate matchings

Both first-gate cycles were combined with both second-gate cycles. All four resulting assignments are bijective edge-to-target matchings, all four have one connected 4,320-edge primal tree, and all four have one connected 8,637-edge complementary dual tree.

Re-solving the unrestricted homogeneous separator LP gives:

| First gate | Second gate | `t` |
|---|---|---:|
| `vsep:243:419:824` | `vsep:225:401:755` | `-0.0003043489476763845` |
| `vsep:243:419:824` | `fsep:3462:2092:773` | `-0.00030434931923494895` |
| `fsep:5350:6698:842` | `vsep:225:401:755` | `-0.0003043492045281499` |
| `fsep:5350:6698:842` | `fsep:3462:2092:773` | `-0.0003043501978609856` |

These are numerical LP values, not exact Farkas certificates. A separate verifier run reproduces them to the stored precision.

Across the four numerical duals, 472 row names are common. The strongest common rows are:

- `vsep:3469:3505:10622`, weight about `0.46355`;
- `fsep:1742:3103:10715`, weight about `0.45932`;
- then `vsep:3433:3469:10513`, `vsep:3468:3433:10512`, and `fsep:1723:3104:10716`.

In one representative gate state, the root-connected broad component has 812 dual rows and 932 support variables. I attempted an exact modular reduction of an 812-by-812 selected subsystem; it did not finish within the computation budget. That timeout is not evidence of singularity, nonsingularity, feasibility or infeasibility and is not used as a conclusion.

- Four-gate dual comparison (`four_gate_dual_summary.json`).
- Broad component decomposition (`broad_components.json`).

---

## 9. What is now proved, and what is not

### Exact conclusions

1. The denominator-`2^104` wall-242 body has the stated actual irredundant H/V lattice, all 4,321 vertices active, 8,638 maximal faces, 12,957 true edges, and positive circuit/incidence separation.
2. Every reported ownership exchange is a genuine alternating cycle on actual true edges.
3. Every retained assignment is a literal primal spanning tree with complementary dual spanning tree.
4. All 35 shortest branches from `C0` are blocked by support-minimal exact positive circuits.
5. Of the 43 shortest branches from `C1`, 41 are blocked by support-minimal exact positive circuits; the two exceptions are explicitly identified broad gates.
6. `C2`, `C3`, and `C4` are support-minimal exact positive circuits.
7. The 80 exact certificate inputs yield 74 unique clauses with exact minimum hitting number two and exactly the four stated minimum pairs.
8. The independent verifier reconstructs 81 archived exact circuit files in total, including the duplicated archived `C1`, and verifies every positive rational dependence and every declared modular determinant residue.

### Numerical conclusions

1. All four `2×2` gate matchings have negative unrestricted separator margin near `-3.0435×10^-4`.
2. The strongest deeper broad branch has `t=-0.0003043488650897158`.
3. The four broad numerical duals share 472 row names, led by the stated primal and dual separators.

### Not established

1. No own-centroid `(1,1,0)` polyhedron was found.
2. No positive unrestricted separator chamber was found.
3. No Santaló root, polar denominator enclosure, own-centroid normal-cone audit or perturbation box was computed for the broad branch states, because proceeding to centring before separator feasibility would be logically premature.
4. The broad gate is not exact-infeasible; its large dual support has not yet been reduced to an exact positive circuit.
5. The atlas does not exhaust longer alternating cycles, all perfect matchings, or all further adjacent hull fans.
6. No class is inferred for a support vector that has not been materialized, recentered and fully audited.

---

## 10. Sharp continuation

The next work should stay inside the separator/matching problem until a genuinely positive unrestricted chamber exists.

1. Start from the common broad gate and branch one of its dominant rows, first `vsep:3469:3505:10622` or `fsep:1742:3103:10715`, through a shortest genuine alternating cycle.
2. Recheck the primal tree and complementary dual tree after every exchange.
3. Exactify each new sparse dual circuit and append its changeable support as a hitting-set clause.
4. Use sparse oriented-matroid elimination on the 812-row/932-variable root component rather than retrying one monolithic determinant.
5. Recompute the minimum hitting sets after each exact clause; this determines whether the current `2×2` gate expands or collapses.
6. Cross a new actual hull circuit only after current-fan matching branches are blocked or when a flip directly changes a dominant obstructing face-separator incidence. Rebuild the complete hull, maximal faces and true edges after every wall.
7. Introduce localized degree-one/projective-null blocks, three dependent control amplitudes and the hard normalized Santaló equations only after an unrestricted separator margin is rigorously positive.
8. At that point materialize the support vector as an exact/dyadic body, isolate `||M||/V=0`, certify positive polar denominators, and run the exhaustive maximal-face, full vertex-cone and four-component true-edge audit at the own centroid.

This continuation is nonrepeating: the old transferred assignment, all 35 first-level shortest exits, 41 of 43 second-level exits, and the clean `C2→C4` chain are now finite exact data rather than open suggestions.

---

## 11. Reproduction

The archive manifest covers 127 files. The exact verifier command is:

```bash
python verify_matching_atlas.py
```

It performs the fresh Qhull rebuild, all 37 million exact vertex–facet slack tests, true-edge/watertight audit, all branch tree/cotree checks, exact separator-row reconstruction, exact rational circuit sums, modular determinant checks and exact hitting-set enumeration.

The numerical LP reproduction is isolated in a separate process:

```bash
python verify_matching_atlas.py --lp-only
```

A fast exact structural pass that omits the full H/V slack sweep is:

```bash
python verify_matching_atlas.py --quick
```

The archived verification report (`verification_report.json`) records `PASS` for both the complete exact audit and the separate numerical LP audit.
