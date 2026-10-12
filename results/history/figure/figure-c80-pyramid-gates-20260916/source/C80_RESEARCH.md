# COORD_C80_PYRAMID_GATES_20260916

This source bundle binds the operator's literal C80 pyramid (23:50:25.547Z entry) to a newly executed own/reference equilibrium census and two exactly scoped affine exclusions. The benchmark remains VQ20_C622_ROUTE88_118_G12, C622 own110/weak000. C80 is NOT a homogeneous Gomboc.

## Exact body

The solid is the convex hull of all 21 integer points in C80_POINTS.json with constant filled density. All maximal supporting planes are enumerated, not inherited from a triangulation. Its true V/E/F are 21/40/21; own strict counts are (2,1,1) and weak-only counts (0,0,0). Two independent exact hull/mass/all-feature implementations produce identical full A/B JSON. A third centred integer-tetrahedron integration gives exactly zero filled first moments. Own centroid denominator has 58 bits, maximum centred integer numerator 84 bits. All core sources are included literally; no previous FINCH sandbox or possibly damaged journal capsule is required.

## All positive diagonal stretches are excluded

For own-centred facet dual vertices q_i=n_i/(h_i-n_i.g), a diagonal physical stretch D=diag(lambda_x,lambda_y,lambda_z) yields dual vertices D^-T q_i. A stable-or-weak facet i is certified by q_i^T D^-1 D^-T(q_j-q_i)<=0 for every other facet j. Normalize the three positive diagonal entries of D^-1 D^-T to weights w_x+w_y+w_z=1. Every inequality becomes affine linear in w_x,w_y. Facet13 is strictly stable for ALL positive weights: q13 is positive pure y and every other q has smaller y component.

The complete weight triangle is covered by 15 closed rational convex polygons, assigned to faces 0,1,6,8,9,19,20. The checker recomputes all exact inequalities from the audited body, checks every proof-polygon vertex, polygon convexity, pairwise zero-area intersections and total area exactly 1/2. A finite union of these closed polygons leaves an open disk around any uncovered interior point; that contradicts the exact full-area disjoint cover. Thus every positive diagonal stretch has the strictly stable base plus another stable or weak equilibrium. It cannot be strict110 with weak000. This excludes neither a general shear nor a rotation of the principal axes BEFORE scaling, nor moving the apex or changing the base. Any rigid motion AFTER stretching preserves this exclusion.

## Complete positive y-stretch sign arrangement

Let t>0 stretch physical y by sqrt(t). Every primal-vertex escape is affine in t. Every dual-vertex escape multiplied by positive t is affine in t. The exact arrangement includes all159 positive sign roots and319 point/open-interval cells, also isolated weak events whose strict region is empty. All cells exclude own110/weak000 already by S/U. The compressed equilibrium summary has17 pieces. Faces0 and13 remain strictly stable for every t>0. This is a full S/U arrangement, not a claimed full saddle census for every t.

## Known reference110 centre is not a realizable filled centre at these z extrema

At r=(7695683,168054,-75622586), exact all-feature mechanics is strict110/weak000, with stable facet13 and unstable vertex14. Its filled first moments are nonzero. Any uniform convex 3-polytope with z extrema m and M has centroid in [(3m+M)/4,(m+3M)/4]: triangulate the boundary and cone it from a maximum vertex; each positive tetrahedron's four-vertex mean is at least (M+3m)/4. Average using positive tetrahedron volumes. Coning from a minimum vertex gives the upper bound.

Here m=-77602682,M=106281898, hence every such centroid has z in [-31631537,60310753]. The stated reference point is below the lower bound by43991049. This excludes that one target point for any uniformly filled convex replacement retaining these extrema. It does NOT exclude the whole reference110 chamber or replacements changing the extrema. Its fractional depth below the pyramid base is59887/4786750; the actual homogeneous pyramid centroid is at depth1/4.

## Numerical methods and finite negative evidence

The separate numerical recovery bundle retains complete production sources, full observed records, explicit parameters and original checkpoint arrays. None is an exact new endpoint or a global exclusion. No numerical proposal was promoted.

pyramid_search.py explores all20 convex base vertices, the apex's horizontal position and log-height, using analytic filled-centroid geometry and analytic Torch gradients. Seed801622, tau1e-4, starts12, maxiter400. Only starts0..10 finished before the process timeout; there is NO terminal12-start receipt. Several low losses are achieved by flattening and/or invalid negative convexity slack. The best valid ranked row is S3/U1, not own110. The source comment about the side-normal direction is reversed, but the code divides every normal by its correspondingly signed offset, so the dual coordinate is unchanged; initial exact-body comparison and finite-difference gradient check passed. The executed source is preserved unchanged.

c80_dual_chain.py explores one-way polar chains from oldfacet0 to a scaled base dual point13 with actual filled-mass fixed-point correction. All27 cases n in[16,24,40], bow in[-1,0,1], gain in[1,2,4], maxfev100 were completed. Each positive logarithmic chain budget ensures its consecutive radial exits but does not protect all original dual vertices as the centre changes. The18 well-closed bow<=0 cases had numerical S3/U2, not110. Nine bow+1 cases approached a chart boundary with closure errors about.030-.044 and numerical S2/U3. The file named BEST ranks class and edge count BEFORE closure, and therefore retains an unclosed E30 proposal; it is neither a canonical best nor a geometric certificate.

## Reproduction

Exact work: CPython3.13.5, standard library only, assertions enabled. From the source directory run `python -B -S REPLAY_EXACT.py NEW_OUTPUT_DIR`. Expected final marker is C80_EXACT_SOURCE_ONLY_REPLAY_ALL_EXPECTED_BYTES_PASS8. The manifest binds every source and all8 exact outputs. The same complete source-only cold replay actually passed in this coordinator turn.

Numerical work used NumPy2.3.5,SciPy1.17.0,Torch2.10.0+cpu, OPENBLAS_NUM_THREADS=1,OMP_NUM_THREADS=1. Sources set these explicitly. Commands and observed stop states are preserved in NUMERICAL_RECEIPT.json; their floating outputs are retained as observed evidence, not guaranteed bitwise reproducibility across numerical stacks.
