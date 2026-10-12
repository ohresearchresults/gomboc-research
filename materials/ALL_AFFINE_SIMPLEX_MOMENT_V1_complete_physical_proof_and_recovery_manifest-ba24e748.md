# material-ba24e7486875

AI research material · [Export notes](../catalog/coverage.md#text-records)

<!-- historical-status:start -->
> **Historical AI material.** The title and claims below reflect the AI’s assessment at the time. Claims of proof, certification or completion are not a current verification verdict.
>
> [C622](../C622/README.md) passes the supplied exact checks; C<500 remains open; Minimum’s C≥34 remains a working lower bound requiring a consolidated proof. See [verification status and source gaps](../catalog/coverage.md).
<!-- historical-status:end -->

---

# ALL_AFFINE_SIMPLEX_MOMENT_V1: global simplex-chain moment identities

## Statement and physical scope
Let P be a full-dimensional convex three-polytope of constant volume density, with its actual volume centroid translated to zero. Let x_i be its distinct true vertices, X their row matrix, and M one arbitrary positive-definite metric. Put G=X M X^T, a nonzero positive-semidefinite matrix. Facets below are the genuine maximal polygonal facets, not triangles of an integration mesh. All conclusions allow weak escape equalities, nonsimple vertices, arbitrary finite anisotropy and all shapes realizing the stated genuine facet incidence. Incidence-changing or dimension-losing limits are not silently included.

For a sorted four-set t=(a,b,c,d), write D_t=det(x_b-x_a,x_c-x_a,x_d-x_a). Let chi_t have entries one on t and zero elsewhere, and J_t=chi_t chi_t^T+diag(chi_t). For every sorted five-set S=(s_0,...,s_4), define the row c_S with coefficient (-1)^j on S without s_j. Then

sum_t c_St D_t=0,
X^T sum_t c_St D_t chi_t=0,
sum_t c_St D_t X^T J_t X=0.

These are simultaneous identities of the same actual coordinates and determinant family. They do not assert the existence of independent simplex masses or separately centered subbodies.

## Proof of the global identities
Map the standard oriented abstract four-simplex affinely to R^3 by sending its five vertices to the five x_i. Its oriented boundary has exactly the alternating five tetrahedra above. For any polynomial p on R^3, apply Stokes to the pullback of the three-form p(x) dx_1 wedge dx_2 wedge dx_3. Its exterior derivative on R^3 is zero; hence the sum of its oriented boundary integrals vanishes. For a nondegenerate oriented tetrahedron, its constant, first and second moment integrals are respectively

D_t/6,
(D_t/24) X^T chi_t,
(D_t/120) X^T J_t X.

The same formulas hold for zero determinant by polynomial continuity. Taking p=1, each coordinate, and each quadratic coordinate product proves all displayed identities, including degenerate five-point configurations. Equivalently, they can be obtained by expanding the affine determinant identities. No orientation of a numerical realization is required in the proof.

A four-set contained in one genuine planar facet has D_t=0, and all three moment contributions vanish. Its unit coefficient row may consequently be added to the space of valid oriented relations.

## Exact reduction to the positive physical cells
Let U contain all four-sets consisting of three vertices of one actual maximal facet and one vertex outside that facet. Each such actual tetrahedron has positive unsigned determinant d_t=6 Vol(t): three distinct vertices of a genuine convex polygon are noncollinear, and an outside actual vertex lies strictly off its supporting plane.

Orient every polygon boundary coherently on the boundary sphere. For each occurrence (a,b,c,d), where b,c,d occur in cyclic facet order and a is outside, assign epsilon_t equal to the parity of this ordered tuple relative to its sorted four-set. Coherent outward versus inward orientation changes all epsilon simultaneously. Thus D_t=sigma epsilon_t d_t for one common sigma in {1,-1}. If the same four-set is obtained from several facets or apices, convexity gives the same epsilon. The exact program also checks this agreement and cancellation of oriented true edges.

Let R be the rational span of all five-set boundary rows and all actual cofacial-flat unit rows in the space of all four-sets. Compute R_U=R intersect Q^U, where Q^U denotes rows zero on every four-set outside U. For r in R_U set h_t=r_t epsilon_t. Multiplication by the common sigma cancels from the three zero identities, giving

sum_U h_t d_t=0,
X^T sum_U h_t d_t chi_t=0,
sum_U h_t d_t X^T J_t X=0.

This is the new positive-cell moment space. It contains the earlier genuine facet-flip and whole-apex-fan difference rows. The program verifies exact containment of each earlier row, keeps an independent earlier basis first, and appends only independent new rows. Earlier certificates retain their literal identities and are not renamed into new exact objects.

## Completeness of the finite linear-algebra construction
For ten vertices, the 126 boundaries on five-sets containing vertex 0 span all five-set boundaries. Each has a unique four-set avoiding 0, so they are independent. Spanning follows from the standard cone identity on the full simplex chain complex: for any cycle z, z=boundary(0*z). This also follows directly by eliminating all nonzero-apex four-sets and then inspecting the boundary coefficients on three-sets avoiding 0.

Modulo this cycle space, the flat-unit rows on an m-gonal facet have rank binomial(m-1,3): their boundary images are the three-cycles on its vertex simplex. Distinct actual facets share at most an edge, so their triangular supports are disjoint. Thus the full relation rank before restricting to U is 126+sum_F binomial(|F|-1,3).

The source performs exact sparse Fraction elimination with all columns outside U placed before columns in U. Rows whose pivots lie in U form exactly the intersection R_U: their earlier outside coordinates vanish, and any combination involving an earlier outside pivot must have zero coefficient there. It clears denominators and primitive integer content. The rank of this intersection need not equal the unrestricted rank; it is computed exactly, not guessed from a numerical rank.

This is completeness of the stated chain-relation construction, not completeness of all polynomial identities of realizable configurations and not an exact characterization of physical realizability.

## Physical positive-definite separation
Take any actual full apex triangulation f0, whose first moment is zero because P has its own volume centroid at zero. For each required true-edge weak escape i->p(i), put D_i=x_i^T M(x_p(i)-x_i)>=0 and L_i=2e_i e_i^T-e_i e_p(i)^T-e_p(i)e_i^T. Then tr(G L_i)=-2D_i<=0.

For vectors g0,g_s, symmetric matrices C_s, scalars k_s and nonnegative numbers mu_ti, define

B_t=f0(t)(g0 chi_t^T+chi_t g0^T)
    +sum_s h_st(g_s chi_t^T+chi_t g_s^T+C_s+k_s J_t)
    +sum_i mu_ti L_i.

If every B_t-I is positive definite, summing d_t tr(G B_t) yields a strictly positive number because G is nonzero PSD and d_t>0. The first-moment terms vanish by actual centering and the h identities; the constant matrix and J terms vanish by the common volume and second-moment identities. The remaining escape terms are nonpositive. This contradiction excludes the entire stated incidence/escape domain. No independent mass optimization or metric per cell is allowed in this argument.

The common-root implementation optionally shares g0,g_s,C_s,k_s across all internal path roots 1,...,8. Its root mode keeps nonnegative arrow multipliers separate for each root. This sharing is a restrictive certificate search ansatz, not an additional premise about P. Every root is expanded to its own exact matrix certificate. Failure to find a shared certificate is UNKNOWN, not a physical impossibility theorem.

## Complete runnable recovery dependencies
Recover each listed immutable material as the exact named UTF-8/LF file in one directory. No old sandbox is needed. Every source below is complete; this manifest does not replace its literal source bytes.

flip_moments.py: [internal-source-reference], 13811 bytes, SHA256 7542ef43f2e0e5b4759f076086c8de3539da8ef5051c80dae2a71e778a21faa7.
common_roots.py: [internal-source-reference], 6011 bytes, SHA256 4d3e16daf49c9dbb4c4d5a88fce37f0337409502be51f1049ceaac3f6c4f0d62.
native55.txt: [internal-source-reference], 2630 bytes, SHA256 58126aee072933749b18eca00ac4d32842e56e6ac8d662d06713bacef28bf96e.
affine_moments.py: [internal-source-reference], 5980 bytes, SHA256 fa8371daf690ac9ff0a9a61b3ad8e8ca2dc6652b2a0f76cc70826163fff01805.
affine_roots.py: [internal-source-reference], 1541 bytes, SHA256 d0866dbf849c91fd39fec55b162ad74f319eade5180c878f7209713f5d249576.
affine_audit.py: [internal-source-reference], 4533 bytes, SHA256 c23ee6747036287caa36cb3a798f82a3c7284ac982d041f0294432259a0a63ca.

Analytic predecessor: [internal-source-reference], 16661 bytes, SHA256 f40f0cdce3b77538f8b863960993a886f325a113ef33df3a8e75a21a9b22f21d.

Observed exact reconstruction and verification commands, CPython 3.13.5, standard library only, assertions enabled:
python -S affine_moments.py census
python -S affine_audit.py

Expected outputs:
affine_census.json: 16606 bytes, SHA256 ce63ec0d52337a7e1b130c85e27eaeacb49d0db89c3f50c6cf4cafb99bee025f.
affine_audit.json: 492 bytes, SHA256 535997d87e723c240a1c7e588b7161b4f901a039227a7af62de29aeb7a0c162e.

Expected terminal markers:
ALL_AFFINE_SIMPLEX_EXACT_SPAN_PASS 55 273 16606 ce63ec0d52337a7e1b130c85e27eaeacb49d0db89c3f50c6cf4cafb99bee025f
AFFINE_SIMPLEX_GENERIC_FIVE_POINT_10_POLYNOMIALS_PASS
AFFINE_SIMPLEX_GENUINE_CUBE_ALL_SHARED_MOMENTS_PASS 27 270
AFFINE_SIMPLEX_EXACT_AUDIT_PASS 492 535997d87e723c240a1c7e588b7161b4f901a039227a7af62de29aeb7a0c162e

The audit symbolically checks the ten zero polynomials for the generic normalized five points 0,e1,e2,e3,(a,b,c). Affine covariance and polynomial continuity cover all five-point inputs. It also checks a genuine own-centered cube with all six maximal quadrilateral facets intact: 56 positive cells, six flat cells, full relation rank41, restricted rank27 and270 exact volume/first/second-moment equalities. These are exact algebra and actual-body controls, not a formalization of Stokes or a geometric impossibility certificate by themselves.

The native55 census proves a strict enlargement for EVERY row, gaining3..7 independent relations; the gain multiplicities are {3:2,4:16,5:21,6:14,7:2}, total273. For native10 the rank grows58->62; native13,59->63; native15,59->63; native17,59->64. A new relation in path-position labels for native13/15/17 is -d0123+d0125+d0135+d0235-d1235=0. It is independent of all earlier facet-flip/fan-difference rows.

## Numerical discovery and evidence boundary
The optional command is python affine_roots.py locate INDEX root; exact frozen checking is python -S affine_roots.py check affine_certificate_INDEX_root.json. The stored adapter's literal outer identity is ALL_AFFINE_SIMPLEX_AFFINE_ROOTS_V1; leaf identity TREE253_K2_AFFINE_SIMPLEX_MOMENT_CERTIFICATE_V1. These literal names are retained, despite the redundant word AFFINE.

Observed discovery environment is CPython3.13.5,NumPy2.3.5,SciPy1.17.0, OPENBLAS_NUM_THREADS=1 and OMP_NUM_THREADS=1. All initialization and iteration parameters are in the complete pinned common_roots source: zero start, no RNG, eight internal roots, tau schedule, bounds, L-BFGS-B tolerances and deterministic rounding powers. A certificate is accepted only by exact integer Bareiss and separate rational Schur checks on every matrix. New coefficient records require their own complete durable recovery capsule before promotion; this method material alone does not preserve those records.

A separate original-facet-flip native15 edge-shared search reached all eight tau stages without an exact certificate, ending with minimum -0.0000605094615693105. This is a useful negative numerical outcome of the restrictive common-undirected-edge ansatz, not a proof that such certificates cannot exist or that a physical realization does exist. Changing both moment space and root sharing does not by itself establish which change causes subsequent success.

The new relation theorem is reusable beyond TREE253; only this implementation's incidence input is presently native55. No universal C>=36 theorem, C34 attainer, or exact minimum follows merely from this enlarged necessary moment system.
