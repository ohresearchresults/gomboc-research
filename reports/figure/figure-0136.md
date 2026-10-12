# figure-0136

AI research report · 2026-08-28 UTC

---

# Calm Atlas 34 — exact one-wall tree–cotree obstruction

## Determination

No literal own-centroid strict `(S,U,H)=(1,1,0)` polyhedron was reached. I therefore make no Gömböc claim.

The main result is instead a finite, exact topology-changing obstruction on the requested 4,321-ray Fourier/Sloan system. I found a genuine primal spanning tree and complementary dual spanning tree, isolated the first required hull circuit, crossed that circuit in an exact dyadic body, rebuilt the complete actual hull, transferred the two trees through the flip, and obtained a new support-minimal positive circuit containing **no incidence inequality at all**.

Thus the first topology change is now resolved rather than merely predicted:

1. In the original fan, the selected tree–cotree system has a 36-row exact circuit consisting of one incidence wall, 32 directed vertex separators, two directed face separators, and `H_0>0`.
2. The sole incidence row is the four-ray wall at old edge 242.
3. There is an explicitly isolated adjacent chamber across this wall.
4. A denominator-`2^104` dyadic Q in that chamber retains all 4,321 vertices and differs from the original actual hull by exactly one diagonal flip.
5. The transferred primal and dual subgraphs are again spanning trees.
6. In the rebuilt adjacent fan, the transferred tree–cotree system has another 36-row exact circuit, now consisting of 33 vertex separators, two face separators, and `H_0>0`; **no hull-incidence row participates**.

Consequently, merely continuing through the first circuit wall cannot realize this tree–cotree architecture. Local dyadic blocks, degree-one/projective response cancellation, a dependent Santaló point, and three centring controls cannot repair the transferred assignment inside this adjacent fan, because the contradiction already holds in unrestricted homogeneous support space before any moment equation is imposed.

---

## 1. Edge-to-target perfect matching formulation

Let the actual simplicial Q-hull have vertex set V, maximal-face set F and true-edge set E. Here

`|V|=4321`, `|F|=8638`, `|E|=12957=|V|+|F|-2`.

Fix root vertex `v0=0` and root face `f0`. Associate one target with every nonroot vertex and every nonroot face. A true edge `e=(i,j)`, with incident faces `(f,g)`, can be assigned to exactly one of four directed separator targets:

- vertex `i -> j`;
- vertex `j -> i`;
- face `f -> g`;
- face `g -> f`.

A perfect matching between the 12,957 edges and the 12,957 targets uses every true edge once and gives every nonroot vertex/face one witness. For the matchings reported here:

- the 4,320 vertex-assigned edges form a connected graph on 4,321 vertices, hence a primal spanning tree;
- the complementary 8,637 face-assigned edges form a connected graph on 8,638 faces, hence a dual spanning tree;
- because both underlying graphs are trees, the directed parent assignments have no directed cycles and terminate at their respective roots.

For integer ray numerators `n_i`, use positive homogeneous supports `G_i` and

`Q(G)=conv{n_i/G_i}`.

The directed vertex witness `v -> w` is the exact linear inequality

`(n_v·n_w)G_v-||n_v||^2 G_w > 0`.

For a triangular maximal face `f`, let `N_f` have rows `n_i`, `i in f`, and let `p_f(G)=N_f^{-1}G_f`. Relative to the exact reference support `G^ref`, put

`d_fg=p_g(G^ref)-p_f(G^ref)`.

The directed face exclusion `f -> g` is

`d_fg·p_f(G)>0`,

again a rational homogeneous linear inequality.

---

## 2. Original-fan matching and first unavoidable circuit

Alternating maximum-bottleneck matching and fixed-matching support LPs produced an actual primal/dual tree–cotree assignment with root vertex 0 and root face 2971. Root face 2971 has vertices

`[3024,2988,3457]`

with source metadata

`[(83,35),(82,35),(96,0)]`.

The numerical max–min value at the first stationary assignment was

`t=-0.0003096239688644281`.

Its exact Farkas obstruction has 36 rows on 35 support variables:

- one actual hull-incidence row;
- 32 directed vertex-separator rows;
- two directed face-separator rows;
- the positive normalization row `G_0>0`.

All 36 rational dependence coefficients are positive. The first 35 primitive integer rows form a nonsingular square matrix; its determinant has 3,376 bits and is nonzero modulo `2147483647`, with residue `13980673`. Since the unique dependence uses every row with nonzero coefficient, this is a support-minimal oriented-matroid circuit.

The unique incidence member is

`inc:242:8230:108`.

Old true edge 242 is `[71,107]`. Its incident maximal faces are

- face 8230: `[71,107,70]`;
- face 8231: `[71,108,107]`.

The four source-grid vertices are

- 70: `(row,azimuth)=(1,33)`;
- 71: `(1,34)`;
- 107: `(2,34)`;
- 108: `(2,35)`.

This makes edge 242 the first sharply defined topology-changing exit for that exact tree–cotree assignment.

Artifacts:

- [Original 36-row exact circuit](sandbox:/mnt/data/calm_atlas34_treecotree_endpoint/exact_positive_circuit_matching35.json)
- [Original circuit summary](sandbox:/mnt/data/calm_atlas34_treecotree_endpoint/exact_positive_circuit_matching35_summary.json)
- [Original circuit footprint](sandbox:/mnt/data/calm_atlas34_treecotree_endpoint/exact_matching35_footprint.csv)

---

## 3. Exact isolation and crossing of wall 242

I solved a signed incidence LP in a support ball of radius `0.001` around the source support. The selected wall was required to be negative while every other old incidence primitive was required to remain positive. The resulting normalized margins before rationalization were

- selected wall 242: `-3.074752545684234e-6`;
- minimum of the other 12,956 old incidence rows: `2.9757166536414914e-6`.

The radial factors were rounded to the lattice `2^-58 Z`. Since the original source vertices use denominator `2^46`, every resulting Q-coordinate has common dyadic denominator

`2^(46+58)=2^104`.

An exact integer determinant audit was then performed on all 12,957 old edge circuits. Its result is

- 12,956 circuit signs unchanged;
- exactly one sign reversed, circuit 242;
- zero vanishing determinants.

The minimum absolute integer determinant among these tests is

`207055948124322281632802332031948397089984057088155679079968752001479358797074923520`.

For wall 242 itself, in the chosen exact orientation,

- old determinant: `-7182455168524329787158557217742248`;
- new determinant: `14079986626638216415444286748575687939207892331225886248544058293330352217248716881920`.

A complete `ConvexHull` rebuild from all 4,321 dyadic coordinates gives

`(V,E,F)=(4321,12957,8638)`.

Every candidate remains an active hull vertex. The exact combinatorial change is

- removed edge: `[71,107]`;
- added edge: `[70,108]`;
- removed faces: `[70,71,107]`, `[71,107,108]`;
- added faces: `[70,71,108]`, `[70,107,108]`.

No other face or true edge changes. This is a literal one-circuit adjacent hull cell, not a graph-only diagonal claim.

Artifacts:

- [Exact adjacent dyadic coordinates and rebuilt lattice](sandbox:/mnt/data/calm_atlas34_treecotree_endpoint/adjacent_wall242/Q_wall242_dyadic.npz)
- [Complete adjacent vertex coordinates](sandbox:/mnt/data/calm_atlas34_treecotree_endpoint/adjacent_wall242/Q_wall242_vertices.csv)
- [All 8,638 rebuilt actual faces](sandbox:/mnt/data/calm_atlas34_treecotree_endpoint/adjacent_wall242/Q_wall242_faces.csv)
- [Exact wall and hull-change summary](sandbox:/mnt/data/calm_atlas34_treecotree_endpoint/adjacent_wall242/wall242_summary.json)
- [Deterministic dyadic materializer and full circuit-sign audit](sandbox:/mnt/data/materialize_wall242_dyadic.py)

---

## 4. Tree–cotree transfer through the actual flip

All unaffected tree and cotree assignments were mapped by exact edge endpoint and triangular-face vertex sets. The local transfer is forced by edge incidence.

Before the flip:

- old face 8230 owned removed edge `[71,107]`;
- old face 8231 owned edge `[71,108]`;
- edges `[70,71]`, `[70,107]`, and `[107,108]` were already owned by vertex targets 70, 107, and 108.

After the flip, let

- new face A be `[70,71,108]`, actual face index 8586;
- new face B be `[70,107,108]`, actual face index 8532.

The only possible complementary assignment preserving all unaffected edge owners is

- face A owns existing edge `[71,108]`;
- face B owns new edge `[70,108]`, directed toward face A.

The rebuilt assignment has

- 4,320 distinct vertex-owned edges and one connected vertex component;
- 8,637 distinct face-owned edges and one connected dual-face component;
- all 12,957 actual true edges used exactly once.

It is therefore again a literal primal spanning tree and complementary dual spanning tree on the rebuilt hull.

The unrestricted fixed-assignment max–min support LP has

`t=-0.0003095961494305788`.

Artifact:

- [Transferred matching, full target data and LP endpoint](sandbox:/mnt/data/wall242_transferred.npz)
- [Deterministic transfer and tree/cotree audit](sandbox:/mnt/data/transfer_matching_flip242.py)

---

## 5. Exact separator-only obstruction after the flip

The sparse dual of the transferred adjacent-fan system reduces exactly to 35 separator rows on 35 support variables. Adding `G_0>0` gives a 36-vector positive circuit.

Its composition is

- 33 directed vertex separators;
- two directed face separators;
- one positivity row;
- **zero incidence rows**.

The 35 support columns are

`[0,35,70,71,107,108,137,138,139,144,170,171,173,174,175,176,178,180,205,206,207,208,209,210,211,216,240,241,242,243,247,276,277,312,419]`.

The two dual-face members are

- `fsep:5350:6698:842`;
- `fsep:8375:8374:586`.

The 33 vertex members are listed completely in the exact certificate. They form a connected local chain rooted through vertices 35, 70, 71, 107 and 108 and extending to vertices 247 and 419.

Let the 35 primitive row covectors be `a_r`. The certificate supplies positive rational numbers `lambda_r` such that

`sum_r lambda_r a_r + e_0 = 0`.

If every matched separator and `G_0>0` held strictly, multiplication by G and summation would yield `0>0`. Hence no positive support vector realizes this transferred tree–cotree assignment.

The exact square separator matrix is nonsingular:

- determinant bit length: 3,341;
- determinant residue modulo `2147483647`: `683583580`.

All 35 separator multipliers are strictly positive; the smallest is approximately

`2.0272501243203460511e-51`.

Because the first 35 rows are independent and the unique 36-row dependence has no zero coefficient, deleting any one row destroys this circuit. It is therefore support-minimal, although I do not claim that no different assignment has a smaller-cardinality obstruction.

This is stronger than the pre-flip circuit. The original obstruction could in principle be escaped through wall 242; the rebuilt adjacent obstruction cannot be escaped by changing support values, centring variables, or local response-null blocks while keeping these matched separator rows. A further useful move must exchange at least one of the 35 separator assignments or change the incidence of one of the two participating face-separator rows.

Artifacts:

- [Exact post-flip separator-only circuit](sandbox:/mnt/data/calm_atlas34_treecotree_endpoint/adjacent_wall242/exact_positive_circuit_after_flip242.json)
- [Post-flip circuit summary](sandbox:/mnt/data/calm_atlas34_treecotree_endpoint/adjacent_wall242/exact_positive_circuit_after_flip242_summary.json)
- [Post-flip circuit footprint](sandbox:/mnt/data/calm_atlas34_treecotree_endpoint/adjacent_wall242/exact_after_flip242_footprint.csv)
- [Exact post-flip circuit constructor](sandbox:/mnt/data/build_exact_adjacent_circuit.py)

---

## 6. Additional matching pivots on the original fan

Circuit-guided alternating-cycle exchanges were also tested before committing to the topology change. The original matching plateau was improved numerically from

`-0.0003096239688644281`

to

`-0.0003048418770698522`

by successively excluding or exchanging the rows

- `vsep:247:243:820`;
- `vsep:9:0:8`;
- `vsep:229:225:751`;
- `fsep:5063:6222:9050`.

Each exchange was realized by an actual alternating cycle in the edge-to-target perfect matching, so the resulting edge partition remained a primal tree and complementary dual tree. The value nevertheless stayed negative. Intermediate exact positive circuits were found with supports 42, 47, 48, and 176; the obstruction migrated from the original seam into larger face/vertex packets rather than disappearing.

This numerical branch is weaker as an exact endpoint than the one-wall result above. Its useful lesson is that repeated local matching pivots improve the max–min value only slowly, while crossing the first exact incidence wall produces an immediate, clean separator-only certificate.

Relevant artifacts:

- [Exact 42-row circuit after the first pivot](sandbox:/mnt/data/calm_atlas34_treecotree_endpoint/exact_positive_circuit_matching41.json)
- [Its compact summary](sandbox:/mnt/data/calm_atlas34_treecotree_endpoint/exact_positive_circuit_matching41_summary.json)
- [Exact 47-row later circuit](sandbox:/mnt/data/calm_atlas34_treecotree_endpoint/exact_positive_circuit_matching_ipm3.json)
- [Exact 176-row migrated circuit](sandbox:/mnt/data/calm_atlas34_treecotree_endpoint/exact_positive_circuit_matching_widest2.json)

---

## 7. Hard centring and full mechanics status

The strongest fully completed own-centroid audit remains the previous exact dyadic construction-origin Q and its hard-centred polar P:

- Q actual lattice: `(V,E,F)=(4321,12957,8638)`;
- construction-origin Q class: `(1144,1,1143)`;
- own-centred polar P class: `(2969,2394,5361)`;
- dual hard-centred Q class: `(2394,2969,5361)`;
- normalized first moment of P: exactly zero by rational tetrahedral centroid translation;
- minimum polar denominator: greater than `0.9855003814908321`;
- stable-face strict margin: `4.5012121866827265e-6`;
- unstable full-cone margin: `1.8970364616732839e-6`;
- saddle four-component margin: `7.905569092942382e-5`;
- no uncertain maximal-face, vertex-cone, or true-edge signs.

The baseline archive contains the exact H/V data, maximal-face cycles, all true edges, interval centroid certificate, exhaustive full-normal-cone verifier, and watertight OBJ/STL:

- [Baseline exact own-centroid archive](sandbox:/mnt/data/calm_atlas34_treecotree_endpoint.zip)
- [Baseline full interval audit](sandbox:/mnt/data/calm_atlas34_treecotree_endpoint/interval_full_audit.json)
- [Baseline Santaló enclosure](sandbox:/mnt/data/calm_atlas34_treecotree_endpoint/santalo_interval.json)
- [Baseline own-centred P OBJ](sandbox:/mnt/data/calm_atlas34_treecotree_endpoint/P_own_centroid.obj)
- [Baseline own-centred P STL](sandbox:/mnt/data/calm_atlas34_treecotree_endpoint/P_own_centroid.stl)

The new wall-242 body has **not** yet received an interval-isolated Santaló solve, own-centroid full-normal-cone audit, perturbation box, independent second implementation, or OBJ/STL export. I therefore do not report an equilibrium class for its own centroid. Its completed certification is limited to exact coordinates, exact circuit-sign separation, the rebuilt actual H/V lattice, the exact tree/cotree transfer, and the exact separator-only infeasibility circuit.

---

## 8. What changed relative to the journal

The journal stopped with a constructive lemma and a 4,321-vertex numerical field of class `(1144,1,1143)`, but no materialized dual-tree realization or owned topology change. The new work establishes:

1. A practical perfect-matching realization of the primal/dual tree–cotree architecture.
2. An exact 36-row first obstruction identifying a single required circuit wall.
3. A literal exact dyadic crossing of that wall with the complete actual hull rebuilt.
4. A transferred primal and complementary dual spanning tree in the adjacent fan.
5. A second exact 36-row circuit with no incidence rows, proving that the first topology change does not rescue the transferred assignment.

This replaces the vague continuation to perform sparse tree/cotree matching with a finite branch certificate.

---

## 9. Sharp continuation

The next computation should not return to axial refinement, broad moment modes, regular caps, or unconstrained support smoothing.

In the exact wall-242 adjacent fan, branch on the 35 separator rows in

`exact_positive_circuit_after_flip242.json`.

For each branch:

1. Delete one matched separator row.
2. Find the shortest alternating cycle in the edge-to-target bipartite graph that restores a perfect matching.
3. Verify that the vertex-owned and face-owned edge sets remain connected trees.
4. Solve the unrestricted homogeneous separator LP before adding moments.
5. If another positive circuit appears, exactify it and add its separator support as a finite hitting-set clause.
6. Cross another hull wall only when every matching branch in the current clause is blocked, and prefer a wall changing one of the two face rows `fsep:5350:6698:842` or `fsep:8375:8374:586`.
7. Rebuild the complete actual hull after each wall.
8. Introduce localized degree-one/projective-null blocks and the three dependent Santaló controls only after the unrestricted separator margin becomes positive.

The dominant numerical dual pair after the wall is the vertex row `vsep:243:419:824` and face row `fsep:5350:6698:842`; `vsep:247:243:820` is the next strongest member. A connected alternating exchange involving this three-row packet is therefore the first branch to test. The exact 35-row support is the finite clause that every successful adjacent-fan tree/cotree assignment must hit.
