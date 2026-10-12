# figure-0187

AI research report · 2026-09-01 UTC

---

# Clear Raven 08 — corrected rank-12 post-`CU10` continuation

## Disposition

**EXACT NONWINNER; the requested rank-12 endpoint is fully materialized, but the complete 512-corner transition-atlas consolidation was interrupted by the runtime cutoff.**

I obtained no homogeneous convex polyhedral Gömböc. The strongest completed object is an exact rational rank-12 Minkowski endpoint with `D=(8,12,6)`, common refinement `(V,E,F)=(48,89,43)`, an isolated positive three-control centring root, complete exact H/V/E data, exhaustive strict own-centroid mechanics, two certified perturbation boxes, and a watertight mesh. Its class is strictly `(S,U,H)=(2,2,2)`, not `(1,1,0)`.

The run’s acceptance gate remains a finite uniform-density body evaluated at its own exact volume centroid, with one stable maximal face, one unstable vertex, no saddle edge, complete incidence and positive-margin audits, an independent verifier, and a matching OBJ/STL. Auxiliary-centre, smooth, wall-point, near-solution, or unexpanded-generator claims do not qualify.

## 1. Material correction to the predecessor

The predecessor’s statement that its raw 15-dimensional slice was the complete physical protected gauge was incorrect. It froze rows 0 and 4, thereby omitting four genuine rotations of the protected planes, while retaining four row-rescaling directions on rows 1,2,3,5.

For six affine planes there are 24 raw coefficients. Quotienting six independent positive row rescalings leaves 18 oriented-plane parameters. Fixing the protected point

\[
p=\left(
\frac{3457212881809}{140737488355328},
\frac{123953183653871}{281474976710656},
-\frac{359387927220765}{281474976710656}
\right)
\]

as the translation gauge imposes the three independent equations

\[
\delta h_i-p\cdot\delta n_i=0,
\qquad i\in\{0,4,5\},
\]

so the physical protected shape dimension is exactly

\[
24-6-3=15.
\]

At the post-row-6 wall centre, the valid exact pivot chart is `[2,0,1,0,0,0]`. Its 15 physical coordinates are

`r0.n0, r0.n1, r1.n1, r1.n2, r1.d, r2.n0, r2.n2, r2.d, r3.n1, r3.n2, r3.d, r4.n1, r4.n2, r5.n1, r5.n2`.

The new 12-direction family has exact physical rank 12. Appending `r3.n1,r3.n2,r3.d` gives exact physical and raw rank 15. The exact basis, row-rescaling quotient, pivot calculation, and coordinate matrix are in protected_nullspace.json, rank12_shape_directions.csv, and rank15_completion_basis.csv.

## 2. Literal exact rank-12 family

The retained dependent-control family is

\[
P(x;t)=B_{\rm centered}+t_1C_1+t_2C_2+t_3C_3+\lambda D(x),
\qquad
\lambda=\frac{10677075263}{4294967296}.
\]

`B,C1,C2,C3` retain the P9 fan, and `C1,C2,C3` remain dependent full-rank moment controls.

The 12 independent shape coordinates are

`w15,w9,w13,w100,q5,q6,r7,r8,m0x,m0y,m4y,m4z`.

The first four are the coupled packet-wall variables; `q5,q6` are independent support-depth modes; `r7,r8` are transverse incidence-preserving normal modes; and the four new coordinates rotate protected rows 0 and 4 while preserving their incidence with `p`.

The exact family definition, two dense cube matrices, scales, offsets, selected rows, and exact coefficients are in rank12_family_exact.json and rank12_exact_core.py.

## 3. Strongest completed exact endpoint

The selected endpoint is slice 1, mask 207. Its exact shape coefficients are

\[
\begin{aligned}
w_{15}&=-63/65536,&w_9&=23/65536,\\
w_{13}&=27/65536,&w_{100}&=-3/65536,\\
q_5&=-19/65536,&q_6&=-13/65536,\\
r_7&=-49/16384,&r_8&=33/16384,\\
m_{0x}&=17/32768,&m_{0y}&=31/32768,\\
m_{4y}&=91/32768,&m_{4z}&=-27/32768.
\end{aligned}
\]

The six active `D` rows form eight vertices with active triples

`034,035,045,123,125,135,234,245`.

Thus row 6 remains absent and the protected `[0,4,5]` vertex is actual. The exact summand data are in summands_H.csv and summands_V.csv.

The rebuilt common refinement has

\[
(V,E,F)=(48,89,43),\qquad 48-89+43=2,
\]

with complexity `2E=178`. Every affine Minkowski vertex, maximal face cycle, and true edge is explicit in:

- common_V_affine.csv
- common_H_affine.csv
- common_edges.csv

The exact own-centred final lattice is in final_centered_V.csv and final_centered_H.csv.

The minimum exact nonincident H/V slack is positive and approximately

\[
6.710998194820522\times10^{-6}.
\]

## 4. Exact mixed-volume and mixed-first-moment system

For this actual 43-face common fan,

\[
V(t)=\sum_{i+j+k\le3}v_{ijk}t_1^it_2^jt_3^k,
\]

\[
M_q(t)=\sum_{i+j+k\le4}m^q_{ijk}t_1^it_2^jt_3^k,
\qquad q\in\{x,y,z\}.
\]

All 125 exact rational coefficients were independently regenerated using GMP and are in mixed_volume_first_moments.csv.

The three moment equations have the exact positive solution

\[
(t_1,t_2,t_3)=(1,1,1).
\]

The mixed-first-moment Jacobian is nonsingular. Directed interval/Krawczyk arithmetic isolates the unique positive root in

\[
[1-2^{-24},1+2^{-24}]^3.
\]

The exact Jacobian, determinant, inverse preconditioner, and isolating box are in root_certificate.json and directed_interval_certificate.json.

## 5. Exhaustive own-centroid mechanics

The endpoint’s exact class is

\[
(S,U,H)=(2,2,2).
\]

The two stable features are:

1. intended `P9:27|Dvertex(0;4;5)`, normalized margin `0.02205242942902701`;
2. extra `P9edge(13;15)|Dedge(3;4)`, normalized margin `0.0049955789607752`.

The two unstable features are:

1. transferred source `P9[9;100;103]|D[1;2;3]`, normalized margin `0.00703696634137924`;
2. intended `P9[15;26;27]|D[0;4;5]`, normalized margin `0.741414138528332`.

The two saddle edges are:

1. `P9:13|Dvertex(2;3;4) || P9edge(13;26)|Dedge(2;4)`, normalized margin `0.36401867789317754`;
2. `P9:100|Dvertex(0;3;5) || P9edge(27;100)|Dedge(0;5)`, normalized margin `0.22640126763688154`.

All face, vertex, and four-component true-edge primitives are exact, nonzero, and expanded in face_audit_exact.csv, vertex_audit_exact.csv, and edge_audit_exact.csv.

The consolidated endpoint certificate is exact_nonwinner_certificate.json.

## 6. Open neighborhoods

The dependent-control verifier preserves the common fan and strict `(2,2,2)` class throughout the positive root box of radius `2^-24`.

Holding all normals and other shape coordinates fixed, the independent support-depth box

\[
|\Delta q_5|,|\Delta q_6|\le2^{-30}
\]

also preserves `D=(8,12,6)`, the common refinement `(48,89,43)`, and the strict `(2,2,2)` mechanics. See perturbation_certificate.json and shape_support_box_certificate.json.

## 7. Mesh

The matching centred mesh is OBJ (`postCU10_rank12_selected_centered.obj`) / STL (`postCU10_rank12_selected_centered.stl`). It has 48 vertices, 92 oriented triangles, 138 triangulated mesh edges, every mesh edge incident with exactly two triangles, Euler characteristic 2, and exact outward orientation. The audit is mesh_certificate.json.

## 8. Rank-12 arrangement evidence and self-attack

Two dense eight-sign slices were constructed in the 12-dimensional family. Exact enumeration of all 512 shape corners gives 144 corners whose `D` is a strict simple six-facet polytope with all six rows active. The earlier floating-point scan had reported 143; exact arithmetic recovered the omitted slice-1/mask-19 corner, whose exact common refinement is `(43,79,38)` and whose class is `(2,3,3)`.

The numerical common-fan audit of the originally detected 143 cells found only

`(2,2,2), (2,3,3), (3,2,3), (3,3,4)`.

No sampled cell had `S=1`, `U=1`, or `H=0`. A further 32,000-point numerical search in the full corrected 15-dimensional pivot chart produced 10,598 valid rebuilt cells. Again the minimum observed values were `S=2,U=2,H=2`; the best hard score was about `-0.00322147`, in class `(2,3,3)`. These are search observations, not an exact exclusion of the continuous rank-15 family.

Several corner adjacencies change all tracked residual packet identities between endpoints. Exact event-polynomial enumeration shows why this does not yield the requested one-event cancellation. On representative slice-0 edge mask 54 to mask 118, 296 exact candidate circuit polynomials have five roots in `[-1,1]`; the relevant candidate walls include the quadratic `P13_D2_D3` root near `-0.9607272616189353` and `P100_D3_D5` near `0.1679114493640807`. The common-fan changes seen numerically occur sequentially rather than at one shared root. A second representative edge, mask 55 to mask 183, splits its endpoint packet change into five distinct transitions. Thus dense coupling changes all packets globally but still relays the Euler-neutral block through multiple circuit walls.

The exact atlas generator and exact algebraic transition decomposer are preserved as generate_rank12_atlas_batch.py and generate_coupled_transition_atlas.py.

### Incomplete evidence caused by the execution cutoff

The parallel exact generation of all 512 formal corners was started, but the runtime forced this handoff before every batch could be consolidated into `rank12_common_fan_atlas.json`, before the transition decomposer could be executed on all four representative edges, and before a clean-room whole-package verifier and ZIP manifest were produced. Consequently I do **not** claim a completed machine-checked 144-cell atlas, an exact exclusion of the full rank-12 continuum, or an exact exclusion of the remaining three rank-15 directions.

The selected endpoint, its rank/nullspace certificate, mixed system, root isolation, exhaustive mechanics, perturbation certificates, and mesh listed above were completed and passed their generating checks.

## 9. Sharply delimited residual obstruction

The four new physical directions do not collapse the block. They move the intended packets strongly and improve the transferred-source hard margin relative to the predecessor, but the actual rebuilt endpoint still contains exactly one extra stable feature, one extra unstable feature, and two saddle edges.

The important structural finding is that the obstruction is no longer lack of differential rank. The exact physical rank is 12, the three moment controls remain nonsingular, and a literal full-rank-15 completion exists. The failure is that the four residual feature walls are separated by intervening common-fan circuits. Solving the four old primitive equations simultaneously reaches a shape only after the protected target lineage or the required common fan has already changed.

The immediate continuation should first finish the exact 144-cell consolidation and execute the stored algebraic transition decomposition. Then add the three exact completion coordinates `r3.n1,r3.n2,r3.d` in a second overlapping pivot chart rather than extrapolating the current chart through a pivot-zero wall.

Should the full physical 15-dimensional six-facet family again contain only transferred packets, the next genuinely new Minkowski architecture is not another direction within the same `D`. It is a replacement summand with a seventh active facet, or a nonsimple finite cell, whose normal fan contains one genuine three-dimensional shared circuit spanning the extra stable, transferred source, `13/26`, and return packets. Such a cell must permit the four walls to meet before any target lineage disappears; the present six-facet `D` fan supplies only sequential two-dimensional relay walls.

## Reusable files

- Exact core (`rank12_exact_core.py`)
- Deterministic selected-endpoint generator (`generate_rank12_selected.py`)
- Generator transcript (`generate_selected.log`)
- Exact endpoint certificate (`exact_nonwinner_certificate.json`)
- Corrected protected nullspace (`protected_nullspace.json`)
- Exact rank-12 family (`rank12_family_exact.json`)
- Exact mixed system (`mixed_volume_first_moments.csv`)
- Isolated-root certificate (`root_certificate.json`)
- Exact transition-atlas generator (`generate_coupled_transition_atlas.py`)

**Final literal verdict: exact strict `(2,2,2)` NONWINNER.**
