# figure-0160

Historical AI scientific report · saved 2026-08-29 UTC. Claims below retain their original status and have not all been independently checked. The current retained construction is C622; the C<500 search remains open.

---

# Bright Lynx 56 — higher-rank Minkowski handoff

## Literal verdict

**EXACT HIGHER-RANK NONWINNER.** The interrupted construction has been recovered, corrected, independently verified, and packaged. A genuine protected rank-four deformation of summand `D` exists beyond `E6_pppm`; its coordinate-axis atlas has 47 exactly isolated determinant roots and 18 certified actual fan transitions. The strongest fully rebuilt endpoint is `CU10`, and its literal exact own-centred homogeneous convex polyhedron has strict class `(S,U,H)=(2,2,2)`, not `(1,1,0)`.

The source wall succeeds only topologically: D row `6` becomes redundant and the old source cone `{1,2,6}` disappears, but the unwanted unstable source transfers to `{1,2,3}`. The protected cone `{0,4,5}` survives. Both mixed saddle packets survive, including the `13/26` lineages and the `27/100` return lineages `(n17,n24)` and `(n14,n24)`. Two purported decisive transitions in the abandoned atlas fail their own strict positive-cone test and are not actual fan transitions.

## Exact rank-four family

The family is

`P(u,s,r,a;t1,t2,t3)=B+t1 C1+t2 C2+t3 C3+λD(u,s,r,a)`,

with `λ=10677075263/4294967296`, rank-two base `(a,b)=(13/67108864,-1/4194304)`, and

`D=D_E6+uQ_source+sQ_13_26+rQ_27_100+aQ_aux`.

The four directions preserve the exact protected D vertex on rows `[0,4,5]`: every residual `δh_i-δn_i·p` is exactly zero. The four determinant targets are `CU_D1236`, `CS_P13_D3_D5`, `CR_P27_D0_D5`, and `CA_P9_D3_D6`. Their recomputed projected-gradient matrix has exact rank `4` and nonzero determinant; the exact matrix and determinant are in `target_circuit_gradient.csv` and `rank4_exact_family.json`. Thus rank four, rather than rank three, is forced by the protected-gradient geometry used here.

Exact summand data are supplied in `p9_normals.csv`, `p9_primal_vertices.csv`, `B_C1_C2_C3_H.csv`, `B_C1_C2_C3_V.csv`, `D_H.csv`, `D_H_all_rows.csv`, `D_V.csv`, `rank4_directions.csv`, and `lambda.csv`. `D_gauge_certificate.json` proves the literal affine Minkowski identity.

## Exact transition atlas

Every polynomial root below has an exact rational isolating interval and exact one-root Sturm certificate in `transition_summary_actual.csv`; all 47 roots, including inactive ones, are in `transition_summary_all_roots.csv` and `rank4_transition_atlas.json`.

* `u_source` — 6 actual transitions: `P9_D2_6` at `2.92530184696733e-6`; `P13_D2_3` at `0.000192570757956141`; `P26_D2_4` at `0.000238319095044211`; `P13_D3_6` at `0.000691014046379904`; `P15_D3_5` at `0.400375304846024`; `D4_1_2_3_6` at `0.854221771873883`. The final wall changes D from `(10,15,7)` to `(8,12,6)` and removes row `6`.
* `s_13_26` — 1 actual transition: `P13_D2_3` at `1.02416545939355`. The intended `P13_D3_5` root near `1.00000000001305` is inactive.
* `r_27_100` — 9 actual transitions: `P9_D2_6` at `3.3641026250446e-6`; `P100_D3_5` at `3.72320283545312e-5`; `P13_D2_3` at `0.000179552323592621`; `P13_D3_6` at `0.000221540315883354`; `P13_D1_3` at `0.000835848253571459`; `P26_D2_4` at `0.00133904712922757`; `P9_D1_6` at `0.00226331613210264`; the second `P9_D1_6` at `0.206294061884849`; the second `P13_D1_3` at `0.230497751831991`.
* `a_auxiliary` — 2 actual transitions: `P9_D2_6` at `0.052106050408322`; `P26_D2_3` at `0.655516179435493`.

The exact self-attack is decisive. The proposed `r_27_100` birth `P15_D2_3` near `0.374762918700449` has `strict_positive_cone=false` and `actual_common_fan_transition=false`. The proposed auxiliary `P9_D3_6` root near `0.999999834463355` has the same failure. `atlas_self_attack.json` records the corrected scope.

## Strongest exact endpoint: `CU10`

Shape coordinates are `(u,s,r,a)=(1,0,0,0)`. Summand D has `(V,E,F)=(8,12,6)`, active rows `[0,1,2,3,4,5]`, and redundant row `[6]`. The actual common refinement has `(V,E,F)=(45,83,40)`, Euler characteristic `2`, and complexity `166`.

The irredundant common H/V lattice is explicit: `body_H_affine.csv` contains all 40 maximal faces, exact normals/supports, and cycles; `body_V_affine.csv` contains all 45 affine vertices and summand lineages; `body_edges.csv` contains all 83 true edges and both incident maximal faces. The independent verifier proves every H/V slack, tight cycle, edge incidence, and Euler relation exactly.

From those actual cycles,

`V(t)=Σ v_ijk t1^i t2^j t3^k`, with `i+j+k≤3`,

and

`M_q(t)=Σ m^q_ijk t1^i t2^j t3^k`, with `i+j+k≤4`.

There are exactly `20` nonzero volume coefficients and `35` coefficients for each of `Mx,My,Mz`; every numerator and denominator is in `mixed_coefficients.csv`. The clean-room GMP verifier recomputes all coefficients directly from the H/V cycles and obtains exact equality.

The system `Mx=My=Mz=0` has one isolated positive root in the exact rational box:

* `t1` midpoint `7462136245114987/281474976710656`, interval `[7462136245098603/281474976710656,7462136245131371/281474976710656]`;
* `t2` midpoint `5686467789872829/35184372088832`, interval `[5686467789870781/35184372088832,5686467789874877/35184372088832]`;
* `t3` midpoint `1599994123599985/2251799813685248`, interval `[1599994123468913/2251799813685248,1599994123731057/2251799813685248]`.

The common radius is `1/17179869184=2^-34`. `root_certificate.json` gives the exact residual, Jacobian, rational inverse preconditioner, and Krawczyk image; the image is strictly contained in the positive box, proving existence and uniqueness and preserving the three corrector scales as dependent full-rank moment controls.

For a literal rational polyhedron, the rational midpoint body is translated by its exact rational volume centroid, equivalently absorbing the translation into B. `body_midpoint_centered_V.csv` and `body_midpoint_centered_H.csv` give the exact own-centred V/H representation. Direct exact tetrahedral integration gives first moment `(0,0,0)`; the exact volume is in `direct_centered_certificate.json` and is approximately `7637.500400732874`.

## Exhaustive mechanical audit

`audit_direct_centered.py` recomputes the mechanics from the exact centered H/V data only. It audits 40 faces, 45 vertices, 83 true edges, and all 332 four-component true-edge cone entries. Every feature is strict. The class is exactly `(2,2,2)`:

* stable faces `[9,24]`: `P9:27`; `P9edge(13,15)|Dedge(r16,n17)`;
* unstable vertices `[11,22]`: `P9[9,32,103]|D[1,2,3]`; `P9[15,26,27]|D[0,4,5]`;
* saddle true edges `[11,58]`: the `13/26` pair `Dedge(n23,n17),Dedge(n23,n10)`; the `27/100` pair `Dedge(n17,n24),Dedge(n14,n24)`.

The smallest exact inactive H/V slack is positive, approximately `0.0018483684765853554`. Exact component values and signs are in the three `direct_centered_*_audit.csv` files.

## Positive perturbation certificate

Exact outward-rounded dyadic interval arithmetic at 320 fractional bits covers the full three-dimensional Krawczyk box, including the varying own-centroid translation `c(t)=M(t)/V(t)`. Throughout that nonzero positive box, the common fan remains `(45,83,40)` and the strict class remains `(2,2,2)`.

The exact interval certificate gives volume `[7637.500400713408,7637.50040075234]` in decimal orientation and positive inactive-slack lower bound about `0.0018483683840180697`. Minimum critical lower bounds are `53.97031025169742` for faces, `0.45454668321636066` for vertices, and `103.39968212182276` for true edges; closest strict exclusion upper bounds are `-1.2031503411658506`, `-0.022180669482439963`, and `-0.011865540725631363`. The exact dyadic endpoints and exhaustive rows are in `centered_perturbation_certificate.json` and `centered_box_*_audit.csv`.

This proves a genuine open `(2,2,2)` chamber: ordinary moment-control retuning cannot repair `CU10` locally.

## Independent verifier and mesh

`verify_exact_core.cpp` is an independent GMP verifier. It passes literal Minkowski identity, exact mixed-polynomial reconstruction, common H/V fan `(45,83,40)`, all 83 edge incidences, Euler `2`, and strict positive Krawczyk inclusion. `verify_all.py --reuse-generated` was rerun successfully in the clean package; `MANIFEST.sha256` verifies every packaged file.

`CU10_own_centered.obj` and `CU10_own_centered.stl` are watertight. `mesh_verification.json` proves 45 vertices, 86 triangles, 129 triangulated mesh edges, exactly two incident triangles per mesh edge, Euler `2`, exact outward orientation, exact agreement with maximal face cycles, exact volume agreement, and 86 STL facets.

## Obstruction and next minimal rank/topology mechanism

The higher-rank family demonstrates independent packet access but not packet annihilation. At `CU10`, the source has transferred to `[1,2,3]`, while the `13/26` and `27/100` saddle packets remain. The local positive control box is rigidly `(2,2,2)`, and the two previously claimed decisive return/auxiliary walls are inactive.

The next nonrepeating construction should restart at `CU10`, recompute the protected nullspace after row 6 removal, preserve `[0,4,5]` and the P9 row-27 incidence `[15,26,27]`, and target simultaneously: the transferred source cone `[1,2,3]`; the actual positive-cone `P13_D2_D3` wall; and a strict positive-cone return wall that directly changes `(n17,n24)` and `(n14,n24)`. Recompute the protected target-gradient rank there: use rank three if those three gradients are independent, otherwise rank four. Search coupled paths through the genuine 3D/4D arrangement, not coordinate axes, and rebuild the common fan and mixed moment system after every crossed actual circuit. Do not reuse inactive `P15_D2_D3` or `P9_D3_D6`.

## Scope

This is complete for the exact endpoint `CU10` and its full positive control box. It is not a complete four-dimensional chamber atlas and does not certify moment roots/mechanics in every axis cell. Therefore it is an exact higher-rank nonwinner, not a no-go theorem for all higher-rank Minkowski synthesis.

## Artifacts

* [Exact self-contained archive](sandbox:/mnt/data/Bright_Lynx_56_rank4_Minkowski_exact_nonwinner.zip), SHA-256 `42c42c385d4bf066649bd8c0e37c4ea1a57723dcd3afa9ce835901c7494faa5e`.
* [Archive checksum](sandbox:/mnt/data/Bright_Lynx_56_rank4_Minkowski_exact_nonwinner.zip.sha256).
* [Full research handoff](sandbox:/mnt/data/Bright_Lynx_56_rank4_Minkowski_exact_nonwinner/RESULT.md).
* [Exact-file manifest](sandbox:/mnt/data/Bright_Lynx_56_rank4_Minkowski_exact_nonwinner/MANIFEST.sha256).
* [Watertight OBJ](sandbox:/mnt/data/Bright_Lynx_56_rank4_Minkowski_exact_nonwinner/CU10_own_centered.obj).
* [Watertight STL](sandbox:/mnt/data/Bright_Lynx_56_rank4_Minkowski_exact_nonwinner/CU10_own_centered.stl).
