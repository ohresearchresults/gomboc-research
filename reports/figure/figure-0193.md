# figure-0193

AI research report · 2026-09-02 UTC

---

# Clear Raven 08 — full-rank post-`CU10` seven-facet continuation

## Literal disposition

**EXACT NONWINNER.** No homogeneous convex polyhedral Gömböc was obtained. The corrected six-facet protected family was first completed to its full physical rank 15 in an overlapping pivot chart. Because the four residual mechanisms still relay through separated fan walls, I then introduced the smallest genuinely new architecture: a seventh irredundant facet in `D`, producing an exact 18-dimensional physical protected family.

The strongest exact preserving endpoint has

- `D` f-vector `(10,15,7)` with all seven rows irredundant;
- actual common refinement `(V,E,F)=(50,92,44)` and Euler characteristic `2`;
- exact ordinary-volume first moment `(0,0,0)`;
- an isolated positive dependent-control root `(t1,t2,t3)=(1,1,1)`;
- strict own-centroid equilibrium class `(S,U,H)=(2,2,2)`;
- a certified full-dimensional 18-coordinate shape box;
- an independent exact/GMP/directed verifier and a matching watertight OBJ/STL mesh.

This respects the run's non-negotiable gate: the body must be finite, homogeneous, evaluated at its own exact volume centroid, and have strict `(1,1,0)` with complete H/V/E and all-feature evidence. The durable journal accepted the preceding rank-12 endpoint but explicitly excluded the unfinished 144-corner consolidation and any continuum exclusion inferred from numerical sampling; it identified overlapping-chart full rank and then a seven-facet or nonsimple shared circuit as the next frontier.

## 1. Correct quotient rank and completion of the six-facet family

For `m` affine H-rows, the raw coefficient space has dimension `4m`. Positive rescaling of each row is gauge, removing `m` dimensions. Fixing the protected point is the three-dimensional translation gauge. Thus the physical protected dimensions are

\[
4m-m-3=3m-3.
\]

For the post-row-6 six-facet summand this gives

\[
24-6-3=15.
\]

The exact overlapping-pivot completion uses the three previously omitted coordinates `r3.n1,r3.n2,r3.d` with exact values

\[
(1,-3,5)/2^{24}.
\]

The resulting six-facet endpoint has physical rank 15, `D=(8,12,6)`, common refinement `(48,89,43)`, and strict class `(2,2,2)`. Its exact H/V/E data and certificate are under `fullrank15_sixfacet/` (`certificate.json`). This verifies that lack of coordinate rank was not the obstruction.

## 2. Seven-active-facet replacement and exact physical rank 18

The replacement summand has seven oriented planes, so

\[
28-7-3=18
\]

physical protected shape dimensions. Rows `0,4,5` preserve the exact protected point

\[
p=\left(
\frac{3457212881809}{140737488355328},
\frac{123953183653871}{281474976710656},
-\frac{359387927220765}{281474976710656}
\right)
\]

through `δh_i=p·δn_i`. The remaining rows have two tangential normal coordinates plus an independent support-depth coordinate after fixing one local row-normal pivot. Exact elimination proves rank 18. The quotient, pivots, point constraints, and complete basis are in protected_physical_rank.json, rank18_shape_directions.csv, and rank18_chart_center_rows.csv.

The seven exact `D` rows are labelled

`n14, r16, n23, n17, n10, n24, r24`.

The added row `r24` is irredundant. At the exact anchor endpoint the active triples are

`015, 016, 034, 036, 045, 156, 245, 246, 256, 346`,

so `D` has ten vertices, fifteen true edges, and seven maximal faces. Exact summand H/V data are in summands_H.csv and summands_V.csv.

## 3. Exact finite Minkowski sum

The family is

\[
P(x;t)=B_{\mathrm{centred}}+t_1C_1+t_2C_2+t_3C_3+\lambda D(x),
\qquad
\lambda=\frac{10677075263}{4294967296}.
\]

`B,C1,C2,C3` retain the inherited P9 fan. `C1,C2,C3` remain dependent full-rank moment controls; their geometry is not absorbed into the 18 shape coordinates. Every common vertex is stored with the literal identity

\[
v=v_B+\lambda v_D+t_1v_{C1}+t_2v_{C2}+t_3v_{C3}.
\]

The anchor common refinement has `(50,92,44)`. Every affine common vertex, maximal face cycle, and true edge is explicit in:

- common_V_affine.csv
- common_H_affine.csv
- common_edges.csv

The own-centred H/V representation is final_centered_V.csv and final_centered_H.csv. The exact volume is the rational in exact_nonwinner_certificate.json, approximately `2703.9412327529917`. The minimum exact nonincident H/V slack is approximately `2.6613460137177867e-4`.

## 4. Exact mixed volume and mixed first moments

From the actual 44 maximal face cycles,

\[
V(t)=\sum_{i+j+k\le3}v_{ijk}t_1^it_2^jt_3^k,
\]

\[
M_q(t)=\sum_{i+j+k\le4}m^q_{ijk}t_1^it_2^jt_3^k,
\qquad q\in\{x,y,z\}.
\]

There are exactly 20 nonzero volume coefficients and 35 coefficients in each first-moment component. All 125 exact rationals are in mixed_volume_first_moments.csv.

The three equations `Mx=My=Mz=0` have the exact positive solution

\[
(t_1,t_2,t_3)=(1,1,1).
\]

The exact mixed-first-moment Jacobian determinant is nonzero; numerically it is about `-1331.4448775586097`. The exact Krawczyk certificate isolates the root in the rational radius-`2^-30` box. A separate outward-rounded binary64 verifier certifies strict inclusion and unchanged `(2,2,2)` mechanics throughout the larger positive box of radius `2^-20`. See root_certificate.json and directed_interval_certificate.json.

## 5. Exhaustive exact own-centroid mechanics at the anchor

The anchor is strictly `(2,2,2)`:

| type | exact lineage | normalized margin |
|---|---|---:|
| stable | `P9:13|Dvertex(0;1;6)` | `0.0026600067093217336` |
| stable | intended `P9:27|Dvertex(0;4;5)` | `0.029129787933564223` |
| unstable | transferred `P9[9;100;103]|D[1;5;6]` | `0.008155908272325528` |
| unstable | intended `P9[15;26;27]|D[0;4;5]` | `0.3774593253569585` |
| saddle | `P9edge(13;26)|Dedge(2;4) || P9edge(13;26)|Dedge(2;6)` | `0.012609067294852063` |
| saddle | `P9:15|Dvertex(0;1;6) || P9edge(15;27)|Dedge(0;1)` | `0.018034385545770984` |

Every maximal face, vertex, and four-component true-edge normal-cone primitive is exact and nonzero. The complete ledgers are face_audit_exact.csv, vertex_audit_exact.csv, and edge_audit_exact.csv.

## 6. Certified full-dimensional nonwinning cell

The anchor has a literal 18-coordinate physical shape box

\[
|\Delta x_i|\le 2^{-30},\qquad i=1,\ldots,18,
\]

with the moment controls fixed at their exact positive root. Directed outward arithmetic checks all 35 possible `D` triples, keeps exactly the ten listed vertices, excludes the other 25 triples, preserves the common refinement `(50,92,44)`, and evaluates each body at its own interval-enclosed ordinary-volume centroid.

Throughout the box:

- the class is exactly `(2,2,2)`;
- the minimum `D` nonactive-row slack is at least `0.0019844433607707486`;
- the closest infeasible `D` triple witness is at most `-0.0038701565553686808`;
- the common nonincident H/V slack is at least `1.9128972705312327e-5`;
- the volume lies in `[2703.9383537119907,2703.9441117939973]`.

This is a rigorous local exclusion only. It does **not** exclude the continuous 18-dimensional seven-facet family. See shape18_box_certificate.json.

## 7. Stronger exact preserving descent endpoint

An exact dyadic rationalization of the successful full-rank preserving descent gives a stronger endpoint at path parameter `s=1`. It keeps the same `D=(10,15,7)` and common refinement `(50,92,44)`, preserves the intended stable and unstable lineages, and reduces all four residual margins:

| residual/target | anchor | `s=1` |
|---|---:|---:|
| extra stable | `0.0026600067093` | `0.0017144667059` |
| transferred unstable | `0.0081559082723` | `0.0068042862222` |
| `13/26` saddle | `0.0126090672949` | `0.0047566141244` |
| return saddle | `0.0180343855458` | `0.0055234765247` |
| intended stable | `0.0291297879336` | `0.0282890939741` |
| intended unstable | `0.3774593253570` | `0.2097704988244` |

The endpoint remains strict `(2,2,2)`. Its exact volume is approximately `1437.1181800486315`, and its exact minimum nonincident slack is approximately `0.0036579872232309807`. It has a unique positive control root `(1,1,1)`, an independent directed control box of radius `2^-28`, and a complete 18-coordinate shape box of radius `2^-40` that preserves `(50,92,44)` and `(2,2,2)`.

The complete endpoint is under `descent_s1/` (`certificate.json`), including its exact certificate (`exact_nonwinner_certificate.json`), mixed coefficients (`mixed_volume_first_moments.csv`), shape box (`shape18_box_certificate.json`), and independent verification (`independent_verification.json`).

## 8. Exact rational transition ordering

The same affine rational path was rebuilt at 15 exact checkpoints. At every checkpoint the actual common H/V/E incidence, own-centroid mechanics, and all 125 mixed coefficients were recomputed. A deterministic replay verifies every stored f-vector, class, feature lineage, exact volume/centroid/slack, and mixed-coefficient SHA-256.

| exact `s` | common `(V,E,F)` | class | material change |
|---:|---:|---:|---|
| `0` | `(50,92,44)` | `(2,2,2)` | seven-facet anchor |
| `1` | `(50,92,44)` | `(2,2,2)` | all four residual margins reduced |
| `1001/1000` | `(50,92,44)` | `(2,3,3)` | `P9[9,32,103]` unstable and paired `P9:9` saddle are born |
| `21/20` | `(50,92,44)` | `(3,3,4)` | `13/26` stable–saddle packet is born |
| `11/10` | `(50,92,44)` | `(3,3,4)` | same expanded packet persists |
| `6/5` | `(50,92,44)` | `(2,3,3)` | local stable member transfers/dies; three-defect packet remains |
| `3/2` | `(50,92,44)` | `(2,3,3)` | same common fan, relayed carriers |
| `8/5` | `(50,92,44)` | `(2,3,3)` | same common fan, relayed carriers |
| `2` | `(50,92,44)` | `(2,3,3)` | intended unstable lineage transfers from `D[0,4,5]` to `D[0,3,4]` |
| `11/5` | `(50,92,44)` | `(2,2,2)` | old transferred source dies, but `P9[9,32,103]` survives as replacement |
| `12/5` | `(50,92,44)` | `(3,2,3)` | return stable–saddle packet is born |
| `5/2` | `(49,90,43)` | `(3,2,3)` | first actual common-fan change |
| `14/5` | `(48,88,42)` | `(3,2,3)` | second common-fan change and source transfer |
| `29/10` | `(49,90,43)` | `(3,2,3)` | third common-fan change |
| `3` | `(49,90,43)` | `(2,2,2)` | another relay restores Euler-minimal count, not the target lineages |

The decisive observation is ordering: mechanical births and carrier transfers occur **before** the first common-fan change. The four walls do not meet in one finite event along this full-rank path; they split into an ordered relay. This is exact evidence for this path, not a no-go theorem for all paths.

The machine-readable record is transition_ordering.json. verify_transition_ordering.py returns `ALL_15_EXACT_CHECKPOINTS_PASS`; its limitation is explicit: it reuses the exact geometry core but does not use the numerical search state or cached checkpoint geometry. Decimal boundary values in the JSON are locators only and are not promoted to isolated roots or a continuum exclusion.

## 9. Independent verification and meshes

verify_fullrank18_independent.py imports neither the exact generator nor the numerical search code. It independently reconstructs every summand, literal Minkowski identities, the common H/V/E lattice, exact volume and first moments, all mechanics, all 125 mixed coefficients through a GMP executable, physical rank and gauge constraints, moment and shape boxes, and the mesh. It returns `ALL_CHECKS_PASS` in independent_verification.json.

The stronger `s=1` endpoint has a separate independent verifier (`verify_descent_s1_independent.py`), which also returns `ALL_CHECKS_PASS` and independently reruns the GMP mixed system and both directed boxes.

The anchor mesh is OBJ (`postCU10_fullrank18_sevenfacet_centered.obj`) / STL (`postCU10_fullrank18_sevenfacet_centered.stl`): 50 vertices, 96 triangles, 144 mesh edges, every mesh edge incident to two triangles, Euler characteristic 2, and outward orientation. The `s=1` endpoint has a matching OBJ (`endpoint.obj`) / STL (`endpoint.stl`) with the same combinatorial mesh counts.

## 10. Sharp residual obstruction and first unclassified topology

This work does not prove that every simple seven-facet summand is a nonwinner. It proves only:

1. the six-facet protected architecture reaches exact full physical rank 15 and is still `(2,2,2)`;
2. the seven-facet architecture reaches exact full physical rank 18 and contains an explicit open `(2,2,2)` cell;
3. a preserving full-rank rational descent reduces all four residual margins but encounters ordered mechanical births/transfers before its first fan change;
4. the exact 15-checkpoint path returns to `(2,2,2)` only by replacing carriers, not by producing `(1,1,0)`.

The first topology still not classified is a **nonsimple seven-facet shared-circuit locus**. It must connect, in one local three-dimensional normal-fan cell,

- the extra stable carrier at `D(0,1,6)`,
- the transferred source carrier at `D(1,5,6)` or its `9/32/103` replacement,
- the `13/26` gates on `D` edges `(2,4)` and `(2,6)`,
- the return gate on edge `(0,1)`,

while keeping the intended stable `P9:27|D(0,4,5)` and intended unstable `P9[15,26,27]|D(0,4,5)` strict.

Combinatorially, the smallest candidate is one four-valent `D` vertex plus a neighbouring triangular-prismatic or octahedral `2↔3 / 3↔2` shared cell whose circuit is common to all four residual mechanisms. If no seven-plane realization of that shared cell exists, the next architecture is an eighth active facet furnishing the missing bridge. This is the first genuinely new topology; another coordinate-axis, two-mode, fixed-fan, or ordinary simple-cell scan would repeat an exhausted relay.

## Reusable artifact

- Complete exact bundle (`Clear_Raven_08_postCU10_fullrank18_sevenfacet_exact_NONWINNER.zip`)
- Bundle SHA-256 (`Clear_Raven_08_postCU10_fullrank18_sevenfacet_exact_NONWINNER.zip.sha256`)
- Artifact index (`ARTIFACT_INDEX.json`)
- Manifest (`MANIFEST.sha256`)
- Standalone handoff (`RESULT.md`)

**Final literal verdict: exact strict `(2,2,2)` NONWINNER; no completion ticket.**

Bundle SHA-256: `713b5088477182294247394fe0d2cf745d4c0d032028b2f791f28365d2ddecfe`.
