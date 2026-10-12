# figure-0100

AI research report · 2026-08-27 UTC

<!-- historical-status:start -->
> **Historical AI report.** The title and claims below reflect the AI’s assessment at the time. Claims of proof, certification or completion are not a current verification verdict.
>
> [C622](../../C622/README.md) passes the supplied exact checks; the search for C<500 remains open. See [verification status and source gaps](../../catalog/coverage.md).
<!-- historical-status:end -->

---

# Finite-construction handoff

## Outcome

No single materialized body yet satisfies all three requirements simultaneously: ordinary uniform centroid exactly at the reference origin, true equilibrium class `(1,1,0)`, and four retained literal pyramid actuators with pairwise-disjoint planar bases. I did, however, isolate the remaining obstruction much more sharply and materialize the two required halves:

1. a deterministic finite relative-margin construction with an exhaustive true `(1,1,0)` audit at its construction centre, including the corrected terminal fan; and
2. a finite body with four independent, pairwise-disjoint literal pyramid actuators whose complete nonlinear moment equations close the ordinary centroid to about `1.6e-14`.

The most important new discovery is that an apparent `(1,1,50)` failure was an audit error: all 50 reported saddles were triangulation diagonals internal to two nonsimplicial actuator facets. After grouping coplanar hull triangles into maximal faces and retaining only true edges, the body is exactly `(1,1,0)` at its construction centre. The remaining obligation is therefore not equilibrium closure. It is preserving the four planar pyramid bases while applying that cover closure and then solving the already-certified actuator equations.

The computations use exactly the centred high-curvature `k=3` Fourier-phase seed specified in the journal, including `β=1/160`, the `a=-1/3` phase flattening, relative recursion, reserved control regions, and the requirement that the smooth body serve only as a source.

## 1. Deterministic corrected-relative-margin body

For a source direction

`u=(sin θ cos φ, sin θ sin φ, cos θ)`,

use

`R(θ,φ)^4 = 1 + 4β sin θ cos(φ-P(θ))`,

`β=1/160`,

`η(θ)=(3π/2)(cos θ-cos³θ/3)`,

`P(θ)=η(θ)-(1/3)sin(3η(θ))`.

The normalized polar support point is generated analytically as

`q(u)=(u-∇S log R(u))/R(u)`.

The certified 4,324-row body uses an axis running from the stable source point `-e_x` to the unstable source point `+e_x`. Its finite generator is:

- one stable-cap row at `α=0`;
- 120 rings at `α_j=linspace(0.025, π-1.7·0.03, 120)`;
- 36 rows on each ring with azimuth `2πl/36+0.17j`;
- relative radial factor `exp(0.04(1-2α/π))`;
- three terminal rows at `α=π-0.03`, separated by `2π/3`, with phase offset `0.17·120+0.17`.

Thus the rows are finite expressions involving only elementary functions and fixed decimal parameters. The terminal rows are indices `4321,4322,4323`; their actual unique stable dual facet has orientation `[4321,4323,4322]`.

Materialized statistics:

- input and irredundant rows: `4324`;
- primal vertices: `8644`;
- volume: `4.201080076519359`;
- construction-centre centroid: `(0.0300026404267, -8.35e-14, -7.20e-13)`;
- construction-centre class: `(S,U,H)=(1,1,0)`;
- stable row: row `0` only;
- stable-cap normalized margin: `9.46281084343e-4`;
- unique unstable-facet interior margin: `0.333016696727`;
- own-centroid class after the projective row recentering: `(2799,2867,5664)`.

The higher-resolution materialization has `17,284` rows, construction class `(1,1,0)`, centroid x-coordinate `0.0149243255`, and first moment x-coordinate `0.0626751015`:

High-resolution corrected body data (`high480fine.npz`)

Deterministic seed, hull, mass, and audit implementation (`gomboc_search.py`)

Standalone 4,324-row reconstruction (`gomboc_work.py`)

## 2. Scale-invariant exclusion certificate

Writing the primal body as `P={x:q_i·x≤1}`, a row `q_i` is excluded from being a stable primal facet whenever another actual polar vertex `q_w` satisfies

`q_w·q_i / ||q_i||² - 1 > 0`.

This ratio is dimensionless and invariant under a common change of geometric scale. It replaces the old absolute condition whose recursive implementation drove support norms to the machine wall.

For the certified 4,324-row body:

- minimum non-target vertex witness margin: `1.4338757685e-4`;
- minimum non-target maximal-face foot-exclusion margin: `0.11394114973`;
- minimum true-edge normal-cone exclusion margin: `0.0941048139954`;
- target stable-cap inward margin: `9.46281084343e-4`;
- target unstable-facet barycentric margin: `0.333016696727`.

For an edge with endpoints `q_i,q_j` and adjacent dual primal vertices `v_1,v_2`, the verifier solves

`q_i+t(q_j-q_i)=αv_1+βv_2`.

A saddle requires `0<t<1`, `α>0`, and `β>0`. The reported edge margin is the negative of the largest normalized violation among `t`, `1-t`, `α/(|α|+|β|)`, and `β/(|α|+|β|)` for a non-saddle edge.

For a maximal polar face with dual vertex `v`, the verifier tests the foot `v/||v||²` against the complete maximal polygon, not an arbitrary Qhull triangle. This correction is essential for the actuator facets.

Common-witness certificate data (`common_witnesses.npz`)

Common-witness audit script (`common_witness_audit.py`)

## 3. Corrected terminal fan and legacy residual rows

A smaller diagnostic materialization has 175 source rows, 166 actual rows, and 328 primal vertices. Its construction-centre class is `(1,1,0)`, while its own-centroid class is `(133,194,325)`. It certifies the requested legacy rows as follows:

- source row `29` is inactive;
- row `37` has witness `28`, relative margin `0.02483`;
- row `46` has witness `45`, relative margin `0.02701`;
- row `73` has witness `72`, relative margin `0.02366`;
- row `82` has witness `81`, relative margin `0.02024`;
- row `88` has witness `87`, relative margin `0.02114`;
- row `94` has witness `93`, relative margin `0.02358`;
- row `121` has witness `120`, relative margin `0.01897`.

The rebuilt terminal construction deletes the defective terminal tail before hull closure and inserts an equilateral three-row fan. In the larger profile-closed experiment the deterministic rule is

- retain rows with polar angle `α≤2.58`;
- set `x_f=max(retained q_x)+0.001`;
- insert `(x_f,0.08 cos(2πj/3),0.08 sin(2πj/3))`, `j=0,1,2`.

Those three rows form the active maximal polar facet of the sole unstable primal vertex, with equal barycentric coordinates `1/3` in the symmetric repaired instance.

Terminal-fixed diagnostic body (`terminal_win.npz`)

## 4. Four literal actuator pyramids and exact nonlinear centroid closure

The strongest actuator materialization reserves four control regions before its local closure. Their source directions are

`u_0=(-0.92306476, 0.30828222, 0.23002938)`,

`u_1=(-0.92479220,-0.30362208,-0.22928806)`,

`u_2=(-0.45548443, 0.86915660, 0.19261552)`,

`u_3=(-0.46861887,-0.86189428,-0.19373848)`.

The minimum pairwise angular separation is about `0.73849` radians. Their smooth tangent-foot offsets are approximately `0.04976` through `0.05276`, so they are well outside both critical neighborhoods.

For a base polygon of area `A_i`, area centroid `b_i`, and plane `n_i·x=h_i`, the radial apex is

`a_i(τ_i)=(1+τ_i)b_i`.

Its exact added volume and first moment are

`ΔV_i=(A_i h_i/3)τ_i`,

`ΔM_i=(A_i h_i/3)(τ_i+τ_i²/4)b_i`.

Consequently the hard centroid equations are

`M_core + Σ_i c_i(τ_i+τ_i²/4)b_i = 0`,

where `c_i=A_i h_i/3`.

For cut depth `0.088`, the four bases have areas

`A=(0.50261433, 0.50086910, 0.51518099, 0.51280472)`

and coefficients

`c=(0.15253239, 0.15198034, 0.15696031, 0.15621236)`.

The core data are

- core volume: `4.105033844712977`;
- core centroid: `(0.0145233231,-5.85e-8,5.00e-8)`;
- core first moment: `(0.0596187328,-2.403394e-7,2.052737e-7)`.

The isolated positive solution is

`τ=(0.14914611,0.14738523,0.14561626,0.14914611)`.

Equivalently, the positive nonlinear image coordinates `λ_i=τ_i+τ_i²/4` are approximately

`λ=(0.154707,0.152815,0.150917,0.154707)`.

This explicitly places `-M_core` in the interior of the four-ray moment cone. The `3×4` Jacobian

`J_i=c_i(1+τ_i/2)b_i`

has rank three. The one-dimensional null direction was used to minimize the maximum actuator height while retaining all four positive coordinates.

Visibility thresholds for the four radial apices are

`(0.17161680,0.17131275,0.16956199,0.16878491)`.

Every solved height is strictly below its threshold. Each apex sees only its own base; the numbers of visible and base triangles agree as `(201,201)`, `(199,199)`, `(244,244)`, and `(243,243)`. The four actuator dual-facet vertex sets have cardinalities `203,201,246,245`, and every pairwise intersection is empty.

Checks against an independent full convex-hull reconstruction give

- formula first-moment residual: below `7e-18`;
- actual reconstructed first-moment residual: about `6.5e-14`;
- formula volume: `4.196337554233206`;
- reconstructed volume: `4.196337554233049`;
- volume discrepancy: `1.57e-13`;
- ordinary uniform centroid norm: about `1.55e-14`;
- all four apices are actual hull vertices.

This is a genuine finite ordinary-centroid closure by four disjoint pyramids, not a smooth existence argument. Its current own-centroid equilibrium class is nevertheless `(3516,3194,6735)`, so it is not the final Gömböc.

Exact four-pyramid centred source (`top_independent_d0.088.npz`)

Polar reconstruction and four disjoint actuator facets (`top088_polar.npz`)

Actuator construction and nonlinear solver (`diag_top_controls.py`)

## 5. Maximal-face correction: the apparent 50 saddles were not edges

Applying the relative cover profile with exponent `k=0.7` while forcing each actuator group onto a fitted plane initially produced a simplicial-Qhull report `(1,1,50)`. Inspection showed:

- 24 reported edges had both endpoints in actuator group 2;
- 26 had both endpoints in actuator group 3;
- every one joined two triangles in the same coplanar maximal actuator face.

They were therefore internal triangulation diagonals, not actual polyhedral edges.

The corrected verifier clusters normalized Qhull plane equations, reconstructs each maximal polygonal face, and discards any triangulation edge whose incident triangles belong to the same plane group. With this correction the same body has

- polar hull vertices: `11266`;
- true polar edges: `33307`;
- maximal polar faces and primal vertices: `22043`;
- true equilibrium class: `(1,1,0)`;
- volume: `4.673658234114131`;
- centroid: `(0.519631147,1.93876e-5,5.57015e-7)`.

Plane-preserving cover candidate (`mode_plane_ls_k0.7.npz`)

Triangulation-diagonal diagnosis (`plane_saddles.log`)

The first stable-cap repair used `q_s=(-2,0,0)`. That point slightly violated two actuator planes and destroyed actuator groups 0 and 1. Replacing it by

`q_s=(-1.96,0,0)`

preserves all four actuator planes while retaining a stable-cap margin `0.0523560147`. With the same `α<0.035` cap deletion and the terminal fan rule above, the true audit gives

- equilibrium class `(1,1,0)`;
- volume `4.67612643844351`;
- centroid `(0.519090456,1.9806743e-5,7.8723093e-7)`;
- first moment `(2.42733261,9.2618835e-5,3.6811914e-6)`;
- primal maximal vertices `21727`;
- all four designated actuator-plane vertices active to distances below `1e-15`.

Their active primal vertex coordinates are

`(-0.50920691, 0.38831208, 0.24027421)`,

`(-0.50982903,-0.38182235,-0.23981899)`,

`(-0.06316045, 0.91647424, 0.16426867)`,

`(-0.07645297,-0.91265735,-0.16556207)`.

Four-plane-preserving `(1,1,0)` candidate (`cap_preserve_candidate.npz`)

## 6. Why the four-plane candidate is not yet a winner

Preserving a dual actuator facet is weaker than preserving the primal pyramid beneath it. Removing the four active vertices from the plane-preserving `(1,1,0)` candidate exposes respectively `200`, `198`, `244`, and `243` distinct noncoplanar maximal core faces. Thus the profile deformation retained four apex planes but destroyed the four single polygonal bases. The ordinary pyramid moment formula cannot be applied to that transformed body.

This is the precise finite obligation left by the construction. It replaces the earlier, less specific statement that the actuators merely became infeasible.

A second attempt inserted the four cuts after closing the high-resolution `(1,1,0)` cover. At cut depth `0.088` it produced:

- core class `(4,27,29)`;
- four base areas approximately `(0.50250,0.50075,0.51528,0.51290)`;
- two shared base vertices in three of the six base pairs, so the bases were not pairwise disjoint;
- required heights `(0.30466,0.30354,0.30067,0.30461)`;
- visibility thresholds only `(0.17451,0.17419,0.17067,0.16990)`.

The solved apices therefore passed beyond their individual cones and saw thousands of nonbase triangles. The formula ceased to describe the actual union, the actual centroid became `(-0.008527,-0.000102,-0.0000275)`, and the final class became `(69,5,1313)`. This breaks the naive strategy of cutting four negative-x bases after cover closure.

Failed cut-after-cover body and complete numerical data (`cuts_after_cover_D0.088.npz`)

Failure analysis log (`cuts_after_cover_D088.log`)

## 7. Strongest continuation

The next finite construction should use positive-x subtractive actuator regions rather than negative-x additive ones.

The cover body has a small positive x first moment. Four pairwise-separated cuts on the positive-x hemisphere can remove enough positive moment to make the actuator-free core moment negative. Four radial pyramids can then add back a positive moment while remaining strictly below the original surface and therefore below their visibility thresholds. This reverses the inequality that made the negative-x experiment impossible: the final apices no longer need to protrude beyond the already-closed cover.

A suitable deterministic starting family is

`u_j=(x_0, sqrt(1-x_0²) cos(ρ+jπ/2), sqrt(1-x_0²) sin(ρ+jπ/2))`,

with `x_0` between `0.3` and `0.6`, `ρ=0.23`, and four independently certified cut depths. The four directions have rank-three moment image and their transverse components cancel at leading order. The hard solve should retain the same variables `λ_i=τ_i+τ_i²/4`, enforce `Jλ=-M_core`, and impose simultaneously

- `λ_i>0`;
- `τ_i<τ_i^visibility`;
- pairwise-disjoint base cycles;
- exact true-edge `(1,1,0)` audit after adding the apices.

This route requires no change to the corrected stable cap, terminal fan, relative witness system, or maximal-face verifier.

## 8. Reproducibility and limitations

The supplied verifier contains two independent feature routes:

1. a polar maximal-face audit, reconstructing true maximal faces and true edges before testing feet and normal cones; and
2. a direct primal audit, grouping primal faces, reconstructing maximal-face cycles and true edges, using nonnegative normal-cone solves at vertices and two-normal solves at edges.

The deterministic files and NPZ materializations above reconstruct every reported body without stochastic choices. All numeric moment solutions are isolated positive solutions with explicit visibility margins; they are not interval-certified algebraic numbers. Because no single winner was obtained, I did not emit an OBJ/STL labelled as a polyhedral Gömböc. Doing so for one of the nonwinning components would be misleading.

The exact remaining finite task is now narrow: preserve the complete four-base primal stars, rather than merely their dual planes, while applying the already successful relative cover; or complete the positive-side subtractive-actuator search so the centred final apices remain inside four disjoint visibility cones. Every other isolated failure identified in the journal now has a finite correction and an executable audit.
