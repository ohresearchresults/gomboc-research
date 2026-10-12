# figure-0181

AI research report · 2026-09-01 UTC

<!-- historical-status:start -->
> **Historical AI report.** The title and claims below reflect the AI’s assessment at the time. Claims of proof, certification or completion are not a current verification verdict.
>
> [C622](../../C622/README.md) passes the supplied exact checks; the search for C<500 remains open. See [verification status and source gaps](../../catalog/coverage.md).
<!-- historical-status:end -->

---

# Clear Raven 08 continuation — exact rank-eight post-`CU10` determination

## Disposition

**EXACT NONWINNER.** I continued the earlier four-coordinate post-row-6 endpoint into a literal exact rank-eight Minkowski family. The continuation restores the protected actual `D` vertex `[0,4,5]`, adds two support-depth modes and two transverse normal modes to the dense four-wall coupling, materializes a 64-cell six-dimensional common-fan arrangement, reconstructs the selected body and its mixed moment system exactly, and certifies all mechanics at the body’s own ordinary volume centroid.

No homogeneous convex polyhedral Gömböc was obtained. The strongest selected body has

- `D` f-vector `(8,12,6)`, with active rows `[0,1,2,3,4,5]` and old row 6 absent;
- final `(V,E,F)=(46,85,41)` and Euler characteristic `2`;
- exact first moment `(0,0,0)`;
- exact positive dependent-control root `(t1,t2,t3)=(1,1,1)`;
- strict own-centroid equilibrium class `(S,U,H)=(2,2,2)`;
- nonzero certified neighborhoods in both moment-control space and support-depth shape space;
- an independent GMP/Python/C++ verification and matching watertight OBJ/STL mesh.

The durable predecessor state identified `CU10` as an exact `(2,2,2)` endpoint where deletion of row 6 transferred the source to `[1,2,3]` and left a coupled higher-rank common-fan construction as the next frontier. This continuation is that higher-rank construction, but the transferred Euler-neutral packet still does not collapse to `(1,1,0)`.

## 1. Exact finite Minkowski sum

The family is

\[
P(x;t)=B_{\mathrm{centered}}+t_1C_1+t_2C_2+t_3C_3+\lambda D(x),
\qquad
\lambda=\frac{10677075263}{4294967296}.
\]

`B,C1,C2,C3` retain the inherited P9 fan. `C1,C2,C3` remain three dependent full-rank moment controls. At the selected rank-eight shape, `D` is the intersection of six rational half-spaces and has active triples

\[
034,\ 035,\ 045,\ 124,\ 125,\ 134,\ 135,\ 245.
\]

Every summand is fully expanded in summands_H.csv and summands_V.csv. The exact multiplier is in lambda.csv.

For every common vertex, common_V_affine.csv records the literal identity

\[
v(t)=v_B+\lambda v_D+t_1v_{C1}+t_2v_{C2}+t_3v_{C3},
\]

including summand lineage. common_H_affine.csv contains all maximal face cycles and affine supports; common_edges.csv contains all 85 true edges and their two incident maximal faces.

## 2. Exact rank-eight coupled shape family

The eight coordinates are

\[
(dz_1,dz_2,dz_3,dz_4,q_5,q_6,r_7,r_8).
\]

The first four are dense Hadamard-coupled packet modes. With

\[
H=\begin{pmatrix}
1&1&1&1\\
1&-1&1&-1\\
1&1&-1&-1\\
1&-1&-1&1
\end{pmatrix},
\qquad w=Hz,
\]

every `z` coordinate moves `D` rows `1,2,3,5`; none is a one-row or coordinate-axis deformation. The four packet coordinates are `w15,w9,w13,w100`.

Two independent support-depth modes are added:

\[
q_5:\ \delta h_2=1,\ \delta h_3=-1,
\qquad
q_6:\ \delta h_1=1,\ \delta h_3=-1.
\]

Two incidence-preserving transverse normal modes are then added. Their exact direction vectors are

\[
v_7=\left(-\frac{27377}{524288},-\frac{235071}{524288},1\right),
\qquad
v_8=\left(-\frac{109971}{1048576},-\frac{507333}{1048576},1\right).
\]

`r7` acts with opposite signs on rows 2 and 3; `r8` acts with opposite signs on rows 1 and 5. Exact support corrections preserve the protected incidence.

The selected displacement is

\[
\left(
\frac{1017}{65536},
-\frac{6957}{65536},
\frac{837}{4096},
\frac{8723}{65536},
\frac{3835}{32768},
-\frac{3535}{16384},
\frac{1045}{65536},
-\frac{2023}{65536}
\right).
\]

The selected absolute dense coordinates are

\[
z=\left(-\frac{7655}{65536},-\frac{6413}{65536},\frac{839}{4096},\frac{9779}{65536}\right),
\]

and the wall coordinates are

\[
w=\left(\frac{9135}{65536},\frac{2403}{65536},-\frac{37271}{65536},-\frac{4887}{65536}\right).
\]

All exact row derivatives are in rank8_shape_directions.csv; the selected exact rows, active triples, coordinates, and protected slacks are in rank8_family_exact.json. Exact Gaussian elimination gives rank 8.

## 3. Correct protected nullspace after row 6 removal

The six remaining affine H rows have 24 raw coefficients. Preserving

\[
p=\left(
\frac{3457212881809}{140737488355328},
\frac{123953183653871}{281474976710656},
-\frac{359387927220765}{281474976710656}
\right)
\]

on rows `0,4,5` imposes three independent equations

\[
\delta h_i-p\cdot\delta n_i=0,
\qquad i\in\{0,4,5\}.
\]

There are six independent positive row-rescaling gauges. Therefore the physical protected shape dimension is

\[
24-3-6=15.
\]

Equivalently, six oriented planes contribute 18 physical parameters and quotienting three translations gives 15. Fixing the protected point is the translation-gauge choice; its three equations cannot be subtracted a second time.

The explicit 15-dimensional fixed gauge freezes rows 0 and 4, varies all four affine coefficients of rows 1,2,3, and varies the row-5 normal with `δh5=p·δn5`. The present rank-eight family leaves an exact seven-dimensional complement. The literal basis and ranks are in protected_nullspace.json, rank15_completion_basis.csv, and rank15_completion_basis.json.

Unlike the preceding selected four-coordinate cell, this endpoint contains `[0,4,5]` as an actual `D` vertex. Its strict slacks against rows 1,2,3 are approximately `8.64123`, `0.823390`, and `0.0128558`.

## 4. Exact six-dimensional common-fan arrangement

The finite arrangement uses

\[
(w_{15},w_9,w_{13},w_{100},q_5,q_6)
\]

at exact half-width `epsilon=1/1024`. All `2^6=64` orthant cells have exact rational D H/V data, exact common incidence, and exhaustive exact mechanics.

The class histogram is

| strict class `(S,U,H)` | cells |
|---|---:|
| `(2,2,2)` | 6 |
| `(2,3,3)` | 42 |
| `(3,2,3)` | 16 |

No cell has `S=1` or `U=1`; none is a winner.

The cube has 192 coordinate adjacencies. Canonical exact incidence comparison finds 152 actual common-fan changes:

| axis | adjacencies | fan changes |
|---|---:|---:|
| `w15` | 32 | 16 |
| `w9` | 32 | 32 |
| `w13` | 32 | 32 |
| `w100` | 32 | 32 |
| `q5` | 32 | 16 |
| `q6` | 32 | 24 |

Thus `w9,w13,w100` change the actual common fan across every shared cube wall. The partial `w15,q5,q6` walls reveal the remaining obstruction: 40 adjacencies change shape and mechanical margins without changing canonical common incidence.

Across all 64 cells, the independent exact GMP reconstruction checks 2,640 vertices, 4,880 true edges, 2,368 maximal faces, and 19,520 edge-cone components. The complete transition atlas is arrangement6_atlas.json; every cell’s exact data are included under `atlas_cells/arrangement6/` in the bundle.

## 5. Transverse normal-mode cells

Exact `r7,r8` square atlases at radii `2^-8` and `2^-7` add eight strict cells. Their combined class histogram is five `(2,2,2)` cells and three `(2,3,3)` cells. All eight preserve the actual protected `[0,4,5]` vertex.

These modes alter mechanical margins within one common-fan chamber: their local square edges do not change canonical incidence. The independent GMP reconstruction checks 368 vertices, 680 edges, 328 faces, and 2,720 edge-cone components. See normal_mode_square_eps_2m8.json and normal_mode_square_eps_2m7.json.

## 6. Exact mixed-volume and mixed-first-moment system

For the selected common fan,

\[
V(t)=\sum_{i+j+k\le3}v_{ijk}t_1^it_2^jt_3^k,
\]

\[
M_q(t)=\sum_{i+j+k\le4}m^q_{ijk}t_1^it_2^jt_3^k,
\qquad q\in\{x,y,z\}.
\]

There are exactly 20 nonzero volume coefficients and 35 coefficients in each first-moment component. All 125 exact rational coefficients are in mixed_volume_first_moments.csv.

The centroid equations

\[
M_x=M_y=M_z=0
\]

have the exact positive root

\[
(t_1,t_2,t_3)=(1,1,1).
\]

The exact Jacobian determinant is nonzero and is recorded in root_certificate.json; numerically it is about `601619.8570319937`. A strict Krawczyk certificate isolates the unique root in

\[
\left[1-2^{-20},1+2^{-20}\right]^3
=
\left[\frac{1048575}{1048576},\frac{1048577}{1048576}\right]^3.
\]

At the root, the exact first moment is `(0,0,0)`. An independent GMP implementation rebuilds all 125 coefficients from the actual affine H/V cycles and obtains literal equality.

## 7. Final exact body and exhaustive own-centroid mechanics

At the positive root the selected body has

\[
(V,E,F)=(46,85,41),
\qquad 46-85+41=2,
\]

with complexity `2E=170`. Its exact rational volume is in exact_nonwinner_certificate.json, approximately

\[
8771.240371804517.
\]

The minimum nonincident H/V slack is an exact positive rational, approximately `0.007486387705075478`.

The full own-centred lattice is expanded in final_centered_V.csv and final_centered_H.csv. The strict class is `(2,2,2)`:

| type | exact lineage | normalized margin |
|---|---|---:|
| stable | `P9:15|Dvertex(1;3;4)` | `0.005384222029245157` |
| stable | `P9:27|Dvertex(0;4;5)` | `0.022356277414907446` |
| unstable | `P9[9;32;103]|D[1;2;4]` | `0.008498590456982107` |
| unstable | `P9[15;26;27]|D[0;4;5]` | `0.7446403364731009` |
| saddle | `P9:26|Dvertex(2;4;5) || P9edge(13;26)|Dedge(2;4)` | `0.027062197318714596` |
| saddle | `P9edge(15;27)|Dedge(0;5) || P9edge(15;27)|Dedge(3;5)` | `0.028582470219827724` |

Every equilibrium primitive is exact and nonzero. The ledgers contain all face, vertex, and four-component edge-cone tests: face audit (`face_audit_exact.csv`), vertex audit (`vertex_audit_exact.csv`), and edge audit (`edge_audit_exact.csv`).

## 8. Positive perturbation boxes

Throughout

\[
(t_1,t_2,t_3)\in[1-2^{-20},1+2^{-20}]^3,
\]

with every body translated to its own volume centroid:

- the common f-vector stays `(46,85,41)`;
- the strict class stays `(2,2,2)`;
- inactive H/V slack stays above `0.0073956736241647105`;
- the closest excluded face, vertex, and edge primitives stay below `-1.9489807540455972`, `-0.02160328223995833`, and `-0.004754528879721941` respectively.

With all other shape coordinates fixed,

\[
(q_5,q_6)\in
\left(\frac{3835}{32768},-\frac{3535}{16384}\right)+[-2^{-24},2^{-24}]^2
\]

preserves D topology `(8,12,6)`, common fan `(46,85,41)`, and class `(2,2,2)`. The minimum nonactive D slack stays above `0.010357390550934846`; common inactive slack stays above `0.0074855000987019684`.

The exact/directed certificates are directed_interval_certificate.json, perturbation_certificate.json, and shape_support_box_certificate.json. Independent directed C++ verifiers return `PASS p=20` and `PASS p=24`.

## 9. Independent verification and mesh

verify_rank8_independent.py does not import the generator or exact core. It independently reconstructs the summands, selected H/V/E lattice, exact volume and first moments, all 125 mixed coefficients through GMP, rank-eight family, exact arrangement aggregates, canonical fan adjacencies, directed boxes, and mesh. Its recorded status is `ALL_CHECKS_PASS` in independent_verification.json.

The 64 arrangement cells were freshly recomputed as sixteen standalone GMP batches. arrangement_gmp_verification.json records `ALL_64_EXACT_CELLS_PASS`; normal_modes_gmp_verification.json records `ALL_8_EXACT_CELLS_PASS`. The consolidated transcript is RUN_ALL_VERIFIERS.log.

The matching mesh is OBJ (`postCU10_rank8_selected_centered.obj`) / STL (`postCU10_rank8_selected_centered.stl`): 46 vertices, 88 oriented triangles, 132 mesh edges, every edge incident to two triangles, Euler characteristic 2, and exact outward orientation.

## 10. Exact obstruction and next genuinely higher-rank deformation

The exact finite result is:

> Within the 64-cell six-coordinate packet arrangement and the two certified transverse normal-mode squares, no strict own-centroid `(1,1,0)` cell occurs. The only classes are `(2,2,2)`, `(2,3,3)`, and `(3,2,3)`.

This is not a global impossibility theorem for the full post-row-6 shape space. Seven physical shape directions remain outside the exact rank-eight span. Appending the canonical complement directions

`row1.dnx`, `row1.dny`, `row1.dnz`, `row2.dnx`, `row2.dny`, `row3.dnx`, `row3.dny`

gives exact combined rank 15 and spans the entire protected fixed gauge.

A numerical first-order calculation—explicitly not an exact winner certificate—finds rank 4 for the four residual defect margins on this seven-dimensional complement and a bounded complement direction decreasing all four at first order, with maximum derivative approximately `-0.0004368191161237612`. See rank15_completion_sensitivity.json.

The next nonrepeating continuation is therefore a rank-12 or full rank-15 common-fan arrangement: retain the exact rank-eight endpoint and the three dependent full-rank moment controls; add at least four independent complement modes; locate the first simultaneous finite crossing of the extra stable face, transferred source vertex, `13/26` saddle, and `15/27` return saddle; rebuild actual incidence and all mixed coefficients after each transition; preserve the protected stable `P9:27|D[0,4,5]` and unstable `P9[15,26,27]|D[0,4,5]` features strictly.

The linearized descent does not prove that a finite wall crossing reaches a winner. It only identifies the smallest evidence-supported higher-rank frontier.

## Complete artifact

- Full exact rank-eight NONWINNER bundle (`Clear_Raven_08_postCU10_rank8_exact_NONWINNER.zip`)
- Bundle SHA-256 (`Clear_Raven_08_postCU10_rank8_exact_NONWINNER.zip.sha256`)
- Standalone full handoff (`RESULT.md`)
- Artifact index (`ARTIFACT_INDEX.json`)
- Manifest (`MANIFEST.sha256`)

ZIP SHA-256: `de2eecc17f6bd99451df722593bd5360110b10da7c759ac175c15f751e10dede`.
