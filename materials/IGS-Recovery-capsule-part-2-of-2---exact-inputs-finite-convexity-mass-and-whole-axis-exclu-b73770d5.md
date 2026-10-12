# material-b73770d54c8b

AI research material · [Export notes](../catalog/coverage.md#text-records)

<!-- historical-status:start -->
> **Historical AI material.** The title and claims below reflect the AI’s assessment at the time. Claims of proof, certification or completion are not a current verification verdict.
>
> [C622](../C622/README.md) passes the supplied exact checks; C<500 remains open; Minimum’s C≥34 remains a working lower bound requiring a consolidated proof. See [verification status and source gaps](../catalog/coverage.md).
<!-- historical-status:end -->

---

# IGS exact recovery capsule part 2 of 2

Object identities: IGS5_LOG_C468_G9 and IGS5_PERSIST_C468_G9. Both are NEW exact rational uniformly filled convex polyhedra with V117/E234/F119,C468. Neither is strict110. They are useful nonwinners and exact geometric whole-centre-line controls, not replacements for the canonical C622 own110 body.

This two-part capsule is self-contained. Part1 is the complete standalone igs_exact.py, material [internal-source-reference],13902 bytes,SHA256 996619e62e242a199bcf6d9bf5e0dae788218f4854801c3b41bf0bf47bc95361. Save its entire literal text as igs_exact.py. Save each JSON block below as the named file, UTF-8 with exactly one terminal LF. No older GREEN source, numerical optimizer, local sandbox or external dataset is needed to reconstruct either exact body.

## Finite independent-support construction and proof

For fixed cyclic transverse normals N_j spanning R^2, prescribe independent positive Green curvature coefficients a_lj. On -1<=x<=1 set G(x,t)=(1-|x-t|-xt)/2 and h_j(x)=sum_l a_lj G(x,t_l). Every h_j is concave and piecewise linear. Consequently K={(x,w): -1<=x<=1, N_j.w<=h_j(x) for every j} is convex: each inequality is the hypograph of a concave function. Equivalently K is the intersection of the finite affine halfspaces supplied by all segments of the concave h_j. This does NOT require that each curvature vector a_l itself be a valid polygon support vector. Independent side curvatures supply freedom beyond translated homothetic sections when n>=4; a fixed triangle's support values have only translation and homothety freedom.

The code intersects adjacent side lines at each axial knot and checks every resulting point against EVERY support. It also checks nonzero cyclic section edges. Under these checks the prescribed normal fan remains valid between knots, because the points and all support slacks interpolate linearly. Without those checks, convexity of the halfspace-defined K would still hold but the listed ring incidence could be wrong and extra off-knot vertices could occur. No unchecked fan continuation is accepted here.

Here n=5,k=11, m=2k+1=23 internal rings. Rational axial knots are x_i=2t_i/(1+t_i^2), t_i=(19/20)(i-k)/k, i=0,...,2k, with the two apex knots -1 and1. Normals obey N_(n-1-j)=(N_ju,-N_jv), and negative-knot curvatures are reversed copies of the positive-knot rows. The central row is reflection symmetric. Only the central west curvature is zero; all other coefficients are strictly positive. The two west central facets therefore coincide and are merged into one maximal hexagonal facet. True counts are V=n(2k+1)+2, E=n(4k+3)-1, F=n(2k+2)-1. The world coordinates are (lambda*x,u,beta*(v+alpha*x)), lambda,beta>0. C2 half-turn symmetry sends (x,u,v) to(-x,u,-v); the actual volume centroid lies on the u-axis.

On an axial slab, every section vertex is affine in its interpolation parameter. The signed polygon area is quadratic; transverse area first moments and axial volume first moment are cubic. Rational Simpson 3/8 weights (1,3,3,1)/8 at parameters0,1/3,2/3,1 therefore integrate these polynomials EXACTLY. This is not approximate numerical quadrature. The generator compares that exact mass with outward tetrahedral sums, centres by the ACTUAL filled-volume centroid, and checks zero first moments again from another strictly interior tetrahedral origin. It then checks all hull slacks, maximal coplanar faces, every true edge and its two oppositely oriented owners, complete S/U/mixed-H strict and additional-weak mechanics, and the full physical and same-centre-polar radial landscapes. Stable tests are independently evaluated both by polar-vertex inequalities and projected-foot membership in each maximal facet.

## Exact whole-axis equilibrium interval method

Write the exact centroid-centred vertices as v_i and the maximal outward facet equations as N_f.x=H_f. A hypothetical reference centre c(s)=s*e_u is strictly interior for s in the open axis interval (L,R), obtained by intersecting all facet inequalities on that line. This free-centre diagnostic is NOT a construction at a permitted alternative mass centre.

At vertex i, each necessary/sufficient closed unstable inequality is
-v_i.(v_j-v_i)+s*(v_ju-v_iu)>=0
for every TRUE neighbour j. All inequalities are affine in s, so the full occurrence set is a single closed interval or empty. Strict positivity of every coefficient function gives strict instability.

For facet f, the projected foot in the original coordinate system is
foot_f(s)=H_f*N_f/(N_f.N_f)+s*(e_u-N_fu*N_f/(N_f.N_f)).
For every positively oriented boundary edge a->b, the closed stable inequality is
N_f.((v_b-v_a) cross (foot_f(s)-v_a))>=0.
These also are affine in s and give one interval per facet. The exact output stores every nonempty interval and all its exact affine coefficients, not merely rounded endpoints or a sampling grid.

The source finds a cover of the complete open body-axis interval by STRICT extra-equilibrium intervals. It excludes zero-length intervals and identically-zero active inequalities, checks positivity in each interval interior, and requires strictly overlapping consecutive intervals. Both intended axial equilibria are checked strictly throughout (L,R) using affine endpoint/midpoint signs. Therefore a cover by extra U intervals proves U>=2 for every interior axis centre, and a cover by an extra S interval proves S>=2 there. Boundary endpoints L,R are not admissible interior centres. This theorem is scoped to the stated fixed rational body, Euclidean world metric and this symmetry axis. It does not exclude other geometries, other metrics, off-axis centres or the entire IGS family.

## Exact input A: IGS5_LOG_C468_G9_INPUT.json

```json
{"identity":"IGS5_LOG_C468_G9","k":11,"metric":[[504301393,1000000000],[205130153,200000000],[433980473,1000000000]],"n":5,"normals":[[[404508497,500000000],[146946313,250000000]],[[-154508497,500000000],[237764129,250000000]],[[-1,1],[0,1]],[[-154508497,500000000],[-237764129,250000000]],[[404508497,500000000],[-146946313,250000000]]],"positive_curvatures":[[[85559939,1000000000],[5460797,500000000],[0,1],[5460797,500000000],[85559939,1000000000]],[[11301743,200000000],[23475561,500000000],[10033041,500000000],[525987,100000000],[21932407,1000000000]],[[40893823,1000000000],[51496023,250000000],[4374453,250000000],[1747549,500000000],[5139551,1000000000]],[[10837919,1000000000],[124164869,250000000],[17372607,250000000],[2891701,500000000],[176613,25000000]],[[3565191,200000000],[51780879,1000000000],[85767959,1000000000],[10252091,1000000000],[7821543,1000000000]],[[1314157,125000000],[8470967,250000000],[2357599,31250000],[8681963,200000000],[40470643,1000000000]],[[6086621,500000000],[29904257,1000000000],[39420317,500000000],[45934901,1000000000],[59102187,1000000000]],[[7593641,125000000],[2517381,100000000],[38689571,500000000],[579038517,1000000000],[6141073,125000000]],[[7104263,100000000],[34872079,1000000000],[100594709,500000000],[567822999,1000000000],[56093891,1000000000]],[[2423075779,250000000],[4875707099,1000000000],[729380327,1000000000],[132997343,100000000],[34887223,100000000]],[[19355734437,1000000000],[14902902869,1000000000],[21899703027,500000000],[1414803831,200000000],[49192191237,1000000000]],[[79381517893,1000000000],[25988184303,250000000],[271096434121,1000000000],[51890104081,500000000],[63862713719,250000000]]],"rounding_denominator":1000000000,"source_checkpoint_sha256":"6db1e3a3349907826bb7932abddec7502d3e77ed942046cfb4217705cf307fbf"}
```

Input1802bytes,SHA256 b8e99d71dc20c9d963f8b14f8a7b5c3219d9927e4ed2a1c57c34c7624488e261.
Observed exact census: V117/E234/F119,C468,strict(S,U,H)=(5,13,16),additionalweak(0,0,0). Physical12 positive bars; largest relative squared-radius depth0.30758187015240807 has21 vertices and29 boundary edges. Polar4 positive bars; largest depth0.842670091576387 has48 polar vertices and41 boundary edges. These decimals describe exact fractions in the reproduced JSON.
Whole-axis certificate: L approximately-1.0129531492828485,R approximately1.0542685275964363. Extra Uvertex20 is strict on(L,0.27822008890385846); extra Uvertex43 is strict on(0.0083149375224493,R). The intervals strictly overlap. Intended Uvertex56 and the intended west stable facet are strict throughout. Thus U>=2 for EVERY interior centre on the symmetry axis, including the actual centroid. Mass relocation along this axis alone cannot repair this fixed shape.

## Exact input B: IGS5_PERSIST_C468_G9_INPUT.json

```json
{"identity":"IGS5_PERSIST_C468_G9","k":11,"metric":[[184706509,250000000],[19917707,25000000],[6022843,50000000]],"n":5,"normals":[[[404508497,500000000],[146946313,250000000]],[[-154508497,500000000],[237764129,250000000]],[[-1,1],[0,1]],[[-154508497,500000000],[-237764129,250000000]],[[404508497,500000000],[-146946313,250000000]]],"positive_curvatures":[[[101246921,500000000],[8554297,500000000],[0,1],[8554297,500000000],[101246921,500000000]],[[20069629,200000000],[71520963,1000000000],[4033487,250000000],[4192159,500000000],[73871593,1000000000]],[[1326309,50000000],[77338047,250000000],[6225037,500000000],[2770389,500000000],[111067191,1000000000]],[[252219,40000000],[362449861,500000000],[23781099,500000000],[60263,6250000],[324738129,1000000000]],[[11148871,1000000000],[9430819,125000000],[29676747,500000000],[2058033,125000000],[9350189,1000000000]],[[842889,125000000],[25199521,500000000],[52665333,1000000000],[211311,3125000],[29840931,1000000000]],[[3919823,500000000],[44529393,1000000000],[27660057,500000000],[14029769,200000000],[37319919,1000000000]],[[20062813,500000000],[905481,25000000],[271553,5000000],[10781089,12500000],[7124771,250000000]],[[9961051,200000000],[946203,20000000],[35244351,250000000],[819144749,1000000000],[30379991,1000000000]],[[1012850743,125000000],[591717587,100000000],[519584457,1000000000],[1923356109,1000000000],[86155173,500000000]],[[8067617477,500000000],[18175412307,1000000000],[30855492783,1000000000],[2566044619,250000000],[10039894741,500000000]],[[13239736877,200000000],[63492905253,500000000],[191034949403,1000000000],[37714126971,250000000],[6482105399,62500000]]],"rounding_denominator":1000000000,"source_checkpoint_sha256":"fbb0f5bdd5919b966ad43189625b4ddba152ffe7efd0f4b4c49db8b5e055f465"}
```

Input1774bytes,SHA256 8585fe73fe558b4804acd3035a8f3224c0fb893eb13b5176654a3ee340cdb05c.
Observed exact census: V117/E234/F119,C468,strict(S,U,H)=(21,31,50),additionalweak(0,0,0). Physical30 positive bars; largest relative squared-radius depth0.19306650375913276 has18 vertices and24 boundary edges. Polar20 positive bars; largest depth0.38998289954842197 has44 vertices and43 boundary edges, with another depth0.38208782270955205 on15/34. Exact simultaneous tie processing is authoritative: a numerical sequential symmetric-tie scout reported a different top-P component size37; that is NOT the exact simultaneous packet here.
Whole-axis certificate: L approximately-0.6539401493666999,R approximately0.9852434904597708. Extra stable facet47 is strict on the ENTIRE open interval(L,R), alongside the intended west stable facet. Hence S>=2 for every interior axis centre. This is another fixed-shape obstruction to a centre-only repair, not a family exclusion.

## Reconstruction and verification

Observed environment: Python3.11.8,GCC12.2.0. The exact capsule uses ONLY the Python standard library and fractions.Fraction. No random seed, floating tolerance, external optimizer or nondefault numerical dependency influences any exact sign or output. The frozen input fractions are the object definition, not rounded endpoint claims. Source checkpoint hashes inside inputs identify provenance; they are not required to reconstruct the exact geometry and do not replace the literal exact data above.

Run from a clean directory containing the three recovered files:

```sh
python igs_exact.py IGS5_LOG_C468_G9_INPUT.json
python igs_exact.py IGS5_PERSIST_C468_G9_INPUT.json
```

Both reconstruction commands are also complete verification commands: all assertions are active; do NOT run python with -O. Expected terminal markers include IGS_EXACT_CENSUS, IGS_EXACT_PQ, IGS_EXACT_LINE_COVER True, IGS_EXACT_OUTPUT and final IGS_EXACT_MASS_MECHANICS_AND_LINE_PASS. Expected census lines are:

```text
IGS_EXACT_CENSUS IGS5_LOG_C468_G9 117 234 119 [5, 13, 16] [0, 0, 0]
IGS_EXACT_CENSUS IGS5_PERSIST_C468_G9 117 234 119 [21, 31, 50] [0, 0, 0]
```

Reproduced exact outputs:
- IGS5_LOG_C468_G9_AUDIT.json:874229bytes,SHA256 ac77be72252c96bf6bc8e2a9c3ccbb8bede7adf9776a34e509adedb61cc0c4ca.
- IGS5_PERSIST_C468_G9_AUDIT.json:1219923bytes,SHA256 efd1a3ce7782c357ef2e6eca62e7ace7b37f7b53981b6c8ed5c7a0795f6f5771.

Each deterministic sorted compact JSON includes every exact centred vertex, maximal facet plane and cycle, true edge and facet incidence, actual volume/centroid, complete strict/weak audit, exact simultaneous P/Q components with FULL interfaces and attaining paths/edges, all nonempty centre-line intervals with affine coefficients, and the compact strict cover. These complete arrays are generated without sandbox dependencies from the literal inputs and complete source. Hashes identify the expected bytes; the source and input fractions, not hashes alone, provide recovery.

## Interpretation and next question

The numerical local-loss control has small maximum all-pair logarithmic escape deficits (roughly0.00153 physical and0.000398 polar) despite a polar bar of depth84%. The full-persistence continuation reduced the deepest physical/polar features but proliferated exact critical points. Neither tiny local gaps nor a lower largest persistence bar certify110. The exact interval covers show that the remaining incompatibility in BOTH saved controls is geometric, not merely a wrong position of the volume centroid on the symmetry axis. The open continuation is to change finite section geometry, transverse normals or knot allocation to destroy these whole features while retaining actual mass, convexity and E<=249. No general IGS impossibility is proved.
