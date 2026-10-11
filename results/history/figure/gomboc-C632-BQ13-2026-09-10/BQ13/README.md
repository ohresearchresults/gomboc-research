# Bright Quartz 13: exact homogeneous C632 winner

`C632_WINNER`, mathematical name `BQ13_C632_THREE_LINK_OWN110`, is a new rational convex polyhedron, with uniform density in its entire filled volume. Its true maximal complex has **V=180, E=316, F=138**, hence **C=2E=632**. Its equilibrium census at its own exact filled-volume centroid is **strict (S,U,H)=(1,1,0), additional weak (0,0,0)**. The sole stable maximal facet is input row 3; the sole unstable vertex is raw exact lexicographic vertex 98, the raw apex (0,0,1). All 138 input planes are active. Integration uses 356 triangles, not 356 true edges.

This is different from coordinator C630_COORD_NONWINNER_OWN121, and different from coordinator C632_COORD_NONWINNER_OWN121. The former is independently replayed here as strict121/weak000 with V180/E315/F137; the latter is not relabelled as the present winner. The accepted prior C634_SOC has V182/E317/F137. The new f-vector alone precludes affine equivalence to either that C634 body or the C630 starting body. No immutable worker parent ID is invented.

## Exact definition

Read objects/C632_WINNER/GENERATOR.json. The grid is 10^14. Initialize every 3-vector X_i from its literal integer controls divided by the grid. Put X_138=(0,0,1). Follow the entire ordered plan. An entry (i,deps,axes) solves X_j dot X_i=1, j in deps, for the listed coordinate axes of X_i, keeping other coordinates unchanged. All solves use exact rational arithmetic. RECONSTRUCT.py checks every pivot and every prescribed bipartite contact against groups. The first 138 resulting vectors are q_i. Define the full-dimensional bounded filled intersection K={x:q_i dot x<=1, all i}. None of the remaining X nodes is a mass point.

Enumerate the complete actual K, not an assumed contact mesh. If p_i are its raw lexicographically ordered vertices, triangulate each outward maximal face using its smallest-index vertex. Put Delta=sum det(p_a,p_b,p_c) and L=sum det(p_a,p_b,p_c)(p_a+p_b+p_c). Then ordinary volume W=Delta/6, raw first moment M=L/24, and raw filled centroid g=L/(4 Delta). The final centred vertices are exactly p_i-g. This finite formula and the full literal generator determine every rational coordinate and mass value, including the very long fractions. There is no numerical root in this definition.

Approximate display values from the exact output are W=0.48866257753902004, M=(-0.006259658127330545,0.0029128371717480755,-0.004500171822649659), and g=(-0.012809775937529628,0.005960835360910123,-0.009209159918308493). The final centred first moments are exactly (0,0,0). REPLAY.py writes the entire exact fractions and complete maximal complex in A.json and B.json. centred_mass.py additionally reintegrates 356 positive tetrahedra on a common centred integer lattice, with a different facet fan, and obtains zero integer first-moment numerators directly.

## Completed exact checks

check_A.py exhausts all support triples and all halfspaces, proves boundedness by six nonnegative normal-cone certificates, constructs complete maximal convex polygons, and derives all true edges. It integrates raw moments with origin-based tetrahedra and tests every stable-face, unstable-vertex and true-edge cone condition. It tests each vertex against all other vertices and uses Gram numerators for the two edge-normal coefficients.

check_B.py is independently written, imports none of A, and clips every plane-pair line against every halfspace. It reconstructs all vertices, true edges and complete convex polygons by different code. It integrates from a different strict interior point with different polygon fan anchors. Vertex mechanics is checked both through true neighbours and globally. Edge-normal coefficients use cross/Cramer formulas instead of A's Gram expressions. Both programs report exactly the same complete normalized record, including raw moments and every mechanical sign.

For centred edge endpoints x and y, let d=y-x, ell=d dot d, T=-x dot d, and Q=ell*x+T*d. If n,m are the adjacent outward normals, strict saddle existence requires all four signs positive: T, ell-T, Q dot((m dot m)n-(n dot m)m), Q dot((n dot n)m-(n dot m)n). The Gram determinant is positive. Weak edge equilibria require all four nonnegative with some zero. Face feet are classified against every true polygon side. Vertex normal cones are classified by all outgoing directions; no nonsimple vertex is exempt. Euler is only a cross-check, never a substitute for these predicates.

There are 632 face-side predicates, 32,220 ordered all-vertex support comparisons, and 1,264 true-edge primitives. Every face-side and true-edge primitive is nonzero, and no vertex maximum-exit test is zero. The unique stable polygon has 20 sides; the apex has degree 44. Complete strict rooted primal and polar ascent forests are recomputed by endpoint_stats.py, not assumed from the search.

The winner generator is 12,964 bytes, SHA256 5078c5ca7efa595074368e3a456dc8697407fe95c3ae7e697e1f9a41ee171da5. A.json and B.json are each 424,620 bytes, SHA256 8efd0cdab878c395f8af85ae320869590d6707ff062e70920e448779fa0e2c9b. Maximum numerator-or-denominator bit lengths are 808 for an individual raw vertex coordinate, 78,803 for a centroid coordinate, and 78,806 for a final centred coordinate. The maximum primitive integer plane coefficient has 382 bits. Common-denominator export costs 78,869 bits. Do not advertise the raw grid as final arithmetic complexity or a manufacturing tolerance.

## Exact reconstruction commands

Use Python 3.11 or later, without -O. Exact checking requires only the standard library.

    python -S REPLAY.py --object C632_WINNER --out /an/absent/output/directory

For a bounded execution window the identical replay can be split into three invocations, adding --phase A, then --phase B, then --phase finish, with the same --out directory. The directory must be absent for A and present for B/finish. Finalization checks both completed stage receipts and their complete normalized records. The program verifies the source manifest, reconstructs the object, executes both full independent checks, compares their complete normalized bytes and frozen hash, checks exact rooted forests and direct centred integer moments, and tests regular-tetrahedron and genuine weak-equilibrium fixtures. Expected marker: BQ13_EXACT_TWO_IMPLEMENTATION_REPLAY_PASS.

Other preserved exact objects can be checked with --object C630_START, C622_DISK or C622_READY. All three are intentional strict121/weak000 NONWINNERS. Do not feed them to a winner-only gate. C622_DISK uses its full 137-support generator followed by literal deletion [17,21]; the two other generators are used without deletion. The exact expected records and all hashes are in OBJECTS.json.

An additional complete translation test is available:

    python -S REPLAY.py --object C632_WINNER --translation-fixture --out /another/absent/directory

It translates the raw polyhedron by (1,-2,3)/2^30, independently reconstructs and audits it, and checks that its exactly recentred vertices coincide with the original ones. The weak triangular-prism fixture has strict (4,4,6) and additional weak (1,2,3), so the weak test is exercised nonvacuously.

## Successful whole-basin mechanism and index discipline

First a genuinely non-affine contact-chart deformation of the original C630 body, followed by removing original supports 17 and 21, produced exact C622_DISK: V178/E311/F135, still strict121. That removes the old nonsimple vertex and old 17/19 saddle carrier, but transfers the unwanted pair; it is not cancellation. A further physical deformation produced the independently exact C622_READY, also strict121. Both include their own filled moments. The two exact C622 generators are different.

The construction chart uses the C622_DISK vertex labels preserved in mechanism/C622_chart/faces.json. These are NOT the newly sorted vertex IDs of C622_READY. In that chart the bad vertex is 103, its outgoing saddle edge ends at 114, quadrilateral facet 18 is [69,97,114,103], and adjacent facet 72 is retained. In the fresh exact C622_READY lexicographic order, the actual saddle is (103,112); the chart's 114 label must not be mistaken for that fresh label.

The complete quadrilateral is replaced, not just one primitive on its old edge. Add construction vertices 178 and 179, both in retained facet 72's supporting plane. Replace the boundary edge 103--114 of that facet by 103--178--179--114. Remove quadrilateral facet 18 and add these four triangles, oriented outward:

    [103,69,178], [69,179,178], [69,97,179], [97,114,179].

This is the SECOND triangulation option in spiral_cap.construct(), selected by actual support clearance. An earlier provisional account selecting its first option would be incorrect. The literal final generator and its reconstructed faces control. The whole operation adds two vertices, five true edges and three maximal facets, spending the five-edge headroom obtained at C622 and reaching C632.

On the prepared body's plane 72, write the old endpoints relative to the plane foot from the actual filled centroid. Their projected polar radii are approximately 0.41159131602742755 and 0.4150288930983309, with angle 0.22140175713126464. Two intermediate angles at one third and two thirds, with logarithmically interpolated radii, give three positive ascent links: (rho_end/rho_start)^(1/3) cos(angle/3)-1 is about 4.6673573161459814e-5. This calculation is discovery, not the final algebraic definition. The latter uses only rational contact controls.

The reference-centred cap proposal has complete numerical class110 at the prepared body's old centroid, but its OWN numerical class is (59,54,111). Its filled centroid moves by approximately (4.0232507552e-7,9.8153230512e-6,-9.0838212939e-6). This failure is retained explicitly. It is not silently called homogeneous.

The actual correction uses all 319 free contact coordinates. It preserves reference-centred primal/polar exclusion inequalities and actual supporting geometry while solving the THREE actual filled-centroid equations, including their full derivatives. In a Cartesian-SVD-whitened metric, a minimum-material-motion quadratic program followed by nonlinear repair closed the centroid defect from 1.3379769854705618e-5 to 1.4031167972292188e-16 numerically. The proposed controls were rounded to the literal rational grid and then independently exact audited. Density was never changed.

The final raw lexicographic chain is 103 -> 107 -> 110 -> 114, all TRUE edges. The floor of 10^9 times the exact eta=x dot(y-x)/|y-x|^2 on those edges is respectively 5,826,449; 6,118,904; 5,879,471. Its outgoing route reaches the true apex. The complete primal forest rooted at 98 has maximum depth 94; the complete polar forest rooted at facet 3 has maximum depth 75. Floors of 10^12 times their minimum selected relative radial exits are 670 and 632, respectively. These are exact finite witness reserves, not fabrication tolerances.

The false-merit-resistant identity sum_cycle eta_ij |z_j-z_i|^2 = -(1/2)sum_cycle|z_j-z_i|^2 explains why normalized chord exits detect shrinking closed witness cycles. This identity guides search but does not replace the full saddle-cone census. The decisive step here was building a three-link physical escape on the entire saddle-side patch and then closing actual mass, not driving one old edge residual toward zero.

## Complete optional numerical mechanism replay

The complete discovery helpers, literal starting checkpoints, every used cap input, and preserved finite histories are included under mechanism. Numerical dependencies in the actual run were Python 3.13.5, NumPy 2.3.5 and SciPy 1.17.0, with OPENBLAS_NUM_THREADS=1. No other optimizer package was available or used.

    OPENBLAS_NUM_THREADS=1 python mechanism/REPROPOSE.py

This regenerates the selected cap from the frozen C622_READY checkpoint, checks the entire seed generator against the frozen literal seed, reruns the actual filled-moment closure, and requires the final generator bytes to match the exact winner. It was actually executed successfully in the delivery environment. A different floating proposal must be separately audited; it is never substituted automatically. The exact replay above needs no numerical proposal or external library. The portability patches and their exact scope are in mechanism/PORTABILITY.json. They change only seed loading and remove an unrelated broken multi-input exploratory CLI, not any solver or geometry formula.

## Scope and continuation

This is an exact finite endpoint and two independent software implementations within the same research, not independent human peer review or a proof-assistant formalization. It establishes a new C632 homogeneous winner and actual net disappearance of the extra U/H pair. It does NOT certify a whole parameter-continuum no-birth chronology from C630, global minimality, priority, a prize entitlement, a physical production tolerance, or arithmetic optimality. Earlier finite searches that failed inside a frozen chart do not exclude other charts.

For continuation use the C632_WINNER generator and its full actual incidence. There is no remaining unwanted U/H pair. Further complexity reduction is a new edge/facet-loss problem. The new 13-gon and three-link strip give a specific contact chart to investigate, but removing one link before re-solving its full geometry and moments is not certified. Keep the complete rooted forests and all four edge predicates; do not protect obsolete edge labels or confuse physical and polar centroids.
