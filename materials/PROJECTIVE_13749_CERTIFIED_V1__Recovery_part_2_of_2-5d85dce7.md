# material-5d85dce761b6

AI research material · [Export notes](../catalog/coverage.md#text-records)

<!-- historical-status:start -->
> **Historical AI material.** The title and claims below reflect the AI’s assessment at the time. Claims of proof, certification or completion are not a current verification verdict.
>
> [C622](../C622/README.md) passes the supplied exact checks; C<500 remains open; Minimum’s C≥34 remains a working lower bound requiring a consolidated proof. See [verification status and source gaps](../catalog/coverage.md).
<!-- historical-status:end -->

---

# Recovery capsule part 2/2 — PROJECTIVE_13749_CERTIFIED_V1

## Capsule identity and complete dependencies

Object identity: PROJECTIVE_13749_CERTIFIED_V1. This part contains the theorem, its precise domain, exact proof-to-code bridge, actual observed output and reconstruction instructions.

Part1/2 is material [internal-source-reference], name PROJECTIVE_13749_CERTIFIED_V1__Recovery_part_1_of_2.py.txt, exactly9668bytes, SHA256fa5c135c09db2ad5c6b9ff664839ddbec2a1c3336d03b680e99f893327f5c295. Save its full literal UTF-8 text without alteration as heptagon13749_candidate.py. It contains every exact input and all helpers. These two parts completely reconstruct the result without any former sandbox. The4.8MB coefficient stream need not be separately preserved as literal data because part1 deterministically regenerates it and checks every entry.

## Exact determination

The previously unaccepted fourteen-cone candidate in immutable result minimum-0079 has now completed its exact acceptance run. The complete serialized parent has SHA256a2e0ba9945f97757736cc1b36d40e130dd5641059e25ea30a225a762ef5b93d4 and was read cursor0throughEOF. The earlier geometric parent minimum-0072, SHA25630637df80e99ee64340d83d17e4876e9e873313d20cd83efa2d97f9d1103eba7, was also read completely. Neither parent's literal incidence is changed.

Let the fixed upper heptagon, in label order0,1,2,3,8,7,6, have coordinates(1,y,z) with

(y,z)=(0,0),(1/2,0),(3/4,1/8),(3/4,1/4),(1/4,3/4),(1/8,3/4),(0,1/2).

The other vertices are v5=0,v4=e2,v9=e3. The genuine nine facets are

(0,1,2,3,8,7,6),(0,1,4,5),(0,5,9,6),
(1,2,4),(2,3,4),(3,4,9,8),(4,5,9),(6,7,9),(7,8,9).

Take any positive A,B,C,w and transform the upper vertices to

v_j=(A,B*y_j,C*z_j)/(A+(B-w)*y_j+(C-w)*z_j).

The four corner vertices remain0,e1,e2,e3. Assume for all six noncorner upper vertices the necessary corner-domain inequalities

7*(A+B*y_j+C*z_j)>=15*w*(y_j+z_j).                         (P)

They guarantee strictly positive projective denominators. The map on the entire original body is

(x,y,z) -> (A*x,B*y,C*z)/[w+(A-w)*x+(B-w)*y+(C-w)*z].

Its denominator is positive at every vertex, hence on the whole convex body, and its homogeneous determinant is ABCw>0. It is therefore a genuine projective image with the complete true face lattice unchanged. The image density is uniform volume density: the original mass is NOT pushed forward. Its new centroid c is computed from actual tetrahedron integrals.

Let p=(0,0,1,2,3,4,0,6,7,8), alpha=(9,4,1,38,22,8,4,1,15) indexed by vertices1..9, and

K=-sum_{i=1}^9 alpha_i*sym(v_i-c,v_{p_i}-v_i).

The completed certificate proves K>=I/8 throughout domain(P). Consequently for every positive-definite physical metric M,

sum alpha_i*(v_i-c)^T M*(v_{p_i}-v_i)<=-tr(M)/8,

and at least one required escape arrow is at most-tr(M)/816 because sum alpha=102. Thus the literal nine-arrow TREE410 assignment cannot be realized anywhere in this family, including weak arrow equalities and arbitrarily ill-conditioned positive-definite metrics. The same inequality extends to nonzeroPSD metrics as an algebraic closure, without declaring a singular metric physical.

For the inherited physical root domain,1<D=6Vol(P)<15/8 implies sum(v_j)<=D<15/8 and hence(P). Indeed P contains the corner tetrahedron K0=conv(0,e1,e2,e3) and the tetrahedron conv(e1,e2,e3,v_j) on its opposite side, so6Vol(P)>=1+(sum(v_j)-1)=sum(v_j). The bound D<15/8 is an inherited TREE410 domain premise, not newly proved here and not imposed on all homogeneous polyhedra.

This covers the entire three-parameter positive projective orbit of ONE fixed heptagon restricted by(P), a superset of its required D<15/8 domain. It is NOT the full eight-variable heptagon shape space, not all of literal index13749, not all other893 simple-leaf5 incidences, and not a universalU>=2 theorem for this combinatorial type with every possible escape tree. No complete parent index is removed. The universal complexity bound remains C>=34; no exact minimum or attainer is asserted.

## Why the finite certificate covers a continuum

Normalize A+B+C=1. With A,B,C,w>=0 and(P), the closed parameter polytope has9vertices,17edges,10facets. The source reconstructs all its vertices by exact triple intersections, checks its complete facets and convex boundary cycles, and verifies a strict interior point. Coning its14 boundary triangles to that point gives a complete cover, not a parameter sample.

Every actual positive parameter satisfying the strict physical bound has a positive coefficient on the interior ray of a cone. The six denominator linear forms have nonnegative coefficients on every cone and are positive for actual parameters.

The true apex fan fromv0 consists of seven tetrahedra

(0,4,2,1),(0,4,3,2),(0,3,4,9),(0,3,9,8),
(0,4,5,9),(0,6,7,9),(0,7,8,9).

Let R be the product of the six upper denominator forms. The polynomial source constructs DD=R*D and NN=R^2*sum_T(d_T*sum_{i in T}v_i), with actuald_T=6Vol(T). Thusc=NN/(4*R*DD). The six symmetric numerator polynomials are exactly8*R^2*DD*(K-I/8), not expressions with independently assigned fan masses or a free reference point.

They are degree18 homogeneous four-variable matrix polynomials. In cones8and13 only multiply by(A+B)^2 or(A+C)^2 respectively, positive on the physical domain, giving degree20. All19332nonzero coefficient matrices are POSITIVE DEFINITE;170formally possible coefficient matrices are zero. Every matrix is checked both by its seven principal minors and by rational Schur-pivot elimination. The interior-ray pure-power coefficient is positive definite in every cone.

The complete coefficient identity is also checked independently by scalar-integer Kronecker evaluation. An absolute-expression majorant at all cone variables1 bounds every coefficient. A power-of-two base larger than four that bound, and radix(degree+1) for exponent encoding, separate every homogeneous monomial. Exact integer equality therefore checks every coefficient, not a random polynomial identity at sample points. Principal-minor, Schur-pivot, and whole-polynomial integer-identity checks all completed. Positive denominators preserve the matrix order on division. Boundary degenerations are used for coverage only, not relabeled as actual index13749 bodies.

## Reproduction, verification, and actual pins

Environment: CPython3.13.5, SymPy1.14.0, assertions enabled. No floating-point arithmetic, numerical optimizer, random seed, external data, or former worker file is used by the proof program.

Save the exact part1 text as heptagon13749_candidate.py in a clean directory. Run

python -S heptagon13749_candidate.py root > root_run.txt
python -u heptagon13749_candidate.py projective > projective_run.txt

Both commands exit0. The second prints all14 EXACT_CONE_PASS markers and PROJECTIVE_13749_CANDIDATE_EXACT_ACCEPTANCE_PASS. The earlier interrupted attempt was stopped by the tool execution timeout after five cones and is NOT the accepted output. The subsequent full source run completed without a mathematical patch.

Observed deterministic files:

heptagon13749_candidate.py
9668bytes SHA256fa5c135c09db2ad5c6b9ff664839ddbec2a1c3336d03b680e99f893327f5c295

projective13749_candidate.jsonl
4801780bytes SHA256b5f5610ab3ec79a9dfb9257d0653efea5c14d72906fa0fef4345d1ed6e69ebd1

projective13749_candidate_report.json
453bytes SHA256da73295eddeb90c42ea0138da8cfc7bfad73d588603196361fc4c6b5acbefe9b

projective_run.txt
728bytes SHA2569f2acdc3e90e5ec9bf74563d4300d58edb82e04a84edad03fc9902b6a3d630de

root_run.txt
46bytes SHA25631cbc3591d72bd3f7d7d6461ec645e49cde7f6da42fd7a0c56aaaba44efa126c

The virtual full principal-minor/Schur-rank stream SHA256 is160d9af74d67ce4ee570c0243144ee7bbca62083faeab2807296c1b09acb3d51. No file is falsely claimed for that virtual stream; it is updated deterministically in the program and reported in the453-byte JSON.

Literal full projective stdout, with finalLF:

ROOT_NEIGHBOR_13749_ANALYTIC_CERTIFICATE_PASS
EXACT_CONE_PASS 0 1310 18
EXACT_CONE_PASS 1 1320 18
EXACT_CONE_PASS 2 1320 18
EXACT_CONE_PASS 3 1320 18
EXACT_CONE_PASS 4 1320 18
EXACT_CONE_PASS 5 1320 18
EXACT_CONE_PASS 6 1320 18
EXACT_CONE_PASS 7 1310 18
EXACT_CONE_PASS 8 1736 20
EXACT_CONE_PASS 9 1330 18
EXACT_CONE_PASS 10 1330 18
EXACT_CONE_PASS 11 1330 18
EXACT_CONE_PASS 12 1330 18
EXACT_CONE_PASS 13 1736 20
SOURCE_PIN [9668, 'fa5c135c09db2ad5c6b9ff664839ddbec2a1c3336d03b680e99f893327f5c295']
REPORT_PIN [453, 'da73295eddeb90c42ea0138da8cfc7bfad73d588603196361fc4c6b5acbefe9b']
COEFFICIENT_PIN [4801780, 'b5f5610ab3ec79a9dfb9257d0653efea5c14d72906fa0fef4345d1ed6e69ebd1']
PROJECTIVE_13749_CANDIDATE_EXACT_ACCEPTANCE_PASS

Literal full report JSON, with finalLF:

{"coefficient_count":19332,"coefficient_pin":[4801780,"b5f5610ab3ec79a9dfb9257d0653efea5c14d72906fa0fef4345d1ed6e69ebd1"],"literal_index":13749,"minor_stream_sha256":"160d9af74d67ce4ee570c0243144ee7bbca62083faeab2807296c1b09acb3d51","parent":["minimum-0072","30637df80e99ee64340d83d17e4876e9e873313d20cd83efa2d97f9d1103eba7"],"pd_count":19332,"shift":"1/8","tree":[0,0,1,2,3,4,0,6,7,8],"weights":[9,4,1,38,22,8,4,1,15],"zero_count":170}

## Disposition and remaining direction

The old candidate is now accepted as this explicitly scoped exact family theorem. This upgrades its evidence status, not its mathematical domain. The older root-neighbor analytic theorem and tilted three-arrow control remain distinct objects. General index13749 still needs the eight actual heptagon-shape parameters, the same seven physical fan masses and actual centroid, and one reciprocal metric. The new coefficient margin may support a uniform shape-neighborhood theorem or further shape-cone decomposition, but no such extension is assumed in this capsule. All more general failures remain unresolved rather than inferred from this special family.
