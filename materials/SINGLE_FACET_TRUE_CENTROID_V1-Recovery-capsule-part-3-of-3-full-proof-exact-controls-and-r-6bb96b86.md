# material-6bb96b86f9ea

Historical AI scientific source/proof material. Statements retain their original scope; this is not an independently reviewed theorem.

Public derivative: internal-record-identifiers-replaced.

---

# SINGLE_FACET_TRUE_CENTROID_V1
## Recovery capsule part 3 of 3: actual mass control, global one-cut centering, canonical controls, and limits

This is a new geometric method and exact non-record control, NOT a new own110 attainer, not an exclusion of all C622 deformations, and not a change of the global bracket34<=C_min<=622. It uses actual uniform volume moments throughout. Canonical means exactly VQ20_C622_ROUTE88_118_G12, true176/311/137, strict110weak000, not C622_HOMOTOPY_POSITIVE or the independent C59384 seed.

## 1. Local three-coordinate control of the actual centroid by ONE facet

Let K be the intersection of all fixed other facet halfspaces, and let P(q)=K intersect {x:q.x<=1} be a bounded full-dimensional convex body with0 interior. Suppose F=K intersect {q.x=1} is an active two-dimensional facet. Write V=Vol(P), J=int_P x dx, g=J/V, A=Area(F), C=A^-1 int_F x dA, T=A^-1 int_F xx^T dA, and w=A/||q||. The entries of T are second moments, not just C C^T.

In an open fixed-incidence cell, displacement delta q gives the normal velocity -(delta q.x)/||q|| on F and zero normal velocity on every other facet. Integrating its swept infinitesimal prisms gives

D_q V=-w C^T,
D_q J=-w T,
D_q g=-(w/V)(T-g C^T).

There are no missing first-order contributions from edges, whose swept wedges have second-order volume. The same formulas follow by slicing the integral near the moving plane.

T is positive definite. Indeed a vector a with a^T T a=0 would satisfy a.x=0 on the full two-dimensional relative interior of F. Its affine span is the plane q.x=1, which is not a homogeneous plane, so this forces a=0. Also Tq=C, by integrating x(q.x)=x on F. Hence C^T T^-1=q^T. The determinant lemma now gives

det(T-g C^T)=det(T)(1-q.g)>0,

because the actual volume centroid lies strictly inside every support. Thus D_q g is nonsingular. At ownCOM0 it is the negative definite symmetric matrix -(w/V)T. One active plane has exactly three local affine parameters, and these control all three coordinates of the TRUE filled-body centroid.

For a polytope, a sufficient condition for a full three-dimensional open fixed-face-lattice neighborhood of q is: EVERY vertex on the moving facet has degree three. Such a vertex is the intersection of the variable plane and its two other fixed facet planes. The determinant is nonzero initially and remains so; every old nonincidence is strict. All other vertices stay fixed. Finitely many strict inequalities and determinant signs preserve all true incidences for small changes. No assumption that F itself is triangular is required. Conversely this argument does not grant independent plane motion at a facet with nonsimple incident vertices.

Consequently, if other valid shape parameters vary sufficiently slightly, the analytic implicit function theorem chooses this facet's three plane parameters so that the actual uniform centroid remains exactly the prescribed original g. The volume and moment functions are rational analytic on the fixed polyhedral incidence cell. This is true mass compensation, not translation of a reference point. Features genuinely disjoint from the changed facet star remain geometrically fixed when the other motions leave them fixed; old strict equilibrium signs are open. A weak-contact application must additionally control every physical packet touching the changed geometry. This theorem by itself proves neither general four-contact regularization nor finite deletion repair.

## 2. Global theorem: one halfspace can center ANY bounded convex body at ANY prescribed interior point

Translate the prescribed interior point to0. Let K be any bounded full-dimensional convex body containing0 in its interior. For every q in R^3 put

P_q=K intersect {x:q.x<=1},
Phi(q)=int_K max(1-q.x,0) dx.

Phi is finite, continuous, convex, and continuously differentiable, with

grad Phi(q)=-int_{P_q} x dx=-J(P_q).

At q!=0 the exceptional cutting plane has volume measure zero, so dominated differentiation gives the formula; at q=0 the integrand stays affine for all sufficiently small q because K is bounded. Continuity of the gradient follows the same way. Every P_q contains a neighborhood of0 and has positive volume.

Choose r>0 with the Euclidean ball B(0,r) contained in K. Then

Phi(q)>=int_{B(0,r)} max(-q.x,0) dx=(pi r^4/4)||q||.

The coefficient follows directly from pi int_0^r z(r^2-z^2) dz. Thus Phi is coercive and attains a global minimum q*. Its gradient vanishes, so the actual uniform centroid of P_q* is0. Translating back proves the theorem for any specified interior point. The plane may be redundant: if K already has the target centroid, the uncut body works.

There is also physical uniqueness. For q1,q2, write I_i(x)=1_{q_i.x<=1}. Then

(q1-q2).(J(P_q1)-J(P_q2))=int_K ((q1-q2).x)(I_1-I_2) dx<=0.

The integrand is strictly negative in the interiors of both parts of the symmetric difference. Consequently the inequality is strict whenever the two clipped bodies differ by positive volume. Two distinct essential cutting planes through the interior of a full-dimensional convex K give such different bodies. Therefore two distinct essential cuts cannot both have J=0. If K already has centroid0, no proper essential cut can preserve it, although many redundant q describe the same uncut body. If the initial centroid differs from0, the unique minimizing physical cut is essential and q*!=0.

Within a fixed active-facet incidence cell, the Hessian of Phi is wT>0 from part1. This suggests actual-moment Newton minimization, but the global theorem does NOT keep the incidence cell fixed: the necessary cut may cross combinatorial walls, discard vertices, or create new edges. It imposes no equilibrium count or complexity reduction. Failed fixed-cell Newton iteration does not contradict global existence.

## 3. Exact canonical C622 controls and a concrete global mass-repair consequence

The complete part1 exact program reconstructs the actual true graph from the canonical exact audit. It finds exactly these20 parent facets whose every vertex has degree three:

[48,55,69,70,89,93,99,100,101,105,110,112,113,114,115,117,120,123,124,125].

For each it derives q from the actual oriented cycle, checks equality at every facet vertex and strict support at every other vertex, computes w,C,T by a positive surface triangle fan, checks all60 positive leading Gram minors, verifies Tq=C, and verifies det(T-g C^T)=det(T)(1-q.g) using the actual rational parent g, not an approximation by0. Surface weights are rational: for an oriented face triangle abc on q.x=1, Area(abc)/||q||=det(a,b,c)/2. Its second moment average is [(a+b+c)(a+b+c)^T+aa^T+bb^T+cc^T]/12. Thus the entire audit uses rational arithmetic.

Four OTHER actual facets, indices [6,77,107,130], have respectively [5,4,4,4] vertices. Their normalized normals have a strictly positive affine dependence with sum of weights1 and vector sum0, and the four normals are affinely independent. The program proves this by exact Cramer determinants, not by the floating search that first located these labels. It checks their actual equality/strict-support incidences and that none is among the20 movable facets. The exact positive weights are regenerated and stored in the deterministic report.

These four halfspaces alone have a bounded intersection. Proof: their positive dependence says that any recession direction d satisfying all q_i.d<=0 must have all q_i.d=0. Affine rank3 together with the zero dependence makes their linear span R^3, hence d=0. Their intersection is nonempty because it contains the canonical parent. They remain among the fixed constraints after ANY one of the133 degree-three vertex deletions and after release of ANY of the20 movable facets; the four old faces are nontriangular and lose at most one vertex, so their original support constraints can certainly be retained.

For each of the133 degree-three vertices v, the program also derives its genuine neighbor-plane ear cut N.x<=h. It checks N.v>h, strict N.x<h at every other vertex apart from its three neighbors, and crucially h-N.g_parent>0. Therefore the ORIGINAL actual parent centroid remains in the strict interior after every such ear cut.

For any pair (v,f) consisting of one of these133 ears and one of the20 movable parent facets, let K_{v,f} be the intersection of all original halfspaces except f, together with the exact ear halfspace. It is bounded by the four fixed planes and contains g_parent in its interior. The global theorem therefore supplies a further single plane cut with actual uniform centroid g_parent. Thus there is no GLOBAL own-centroid feasibility obstruction for these2660 released-facet mass-repair problems. This existence statement does NOT say that the restoring plane lies in the original facet's incidence cell, preserves C, removes the extra equilibria, or gives a rational/explicit new attainer. It is a geometric path worth exploring precisely because the near-I fixed-ear bodies themselves were already excluded by U>=2.

An earlier scratch candidate bounding set [0,1,2,28] was rejected: its exact normalized normals are coplanar (all z=1), so its Cramer determinant is0, and its facet sizes were not the guessed nontriangular sizes. It was never accepted as a certificate. The correct four labels are [6,77,107,130]. Exact inputs, not guessed summaries or approximate weights, decide this distinction.

## 4. Full literal source recovery and exact execution

This three-part capsule has complete source units, not snippets:

Part1 material [internal-source-reference] is the entire facet_actuator_exact.py,4460 UTF-8 bytes, SHA256 c0d9799c6cfa801641c60425535f426665653bdbedf7c349950c1370bc4da7aa.
Part2 material [internal-source-reference] is the entire facet_actuator.py,7485 bytes, SHA256261d14f02258bd651157aebd768ba155ea90c069b8b9100af729fb704601dd99. It includes the earlier exact-only audit and the complete separate floating exploratory method.
Part3 is this proof/reconstruction document.

Both source units import the complete preserved exact_ears.py in [internal-source-reference],6699bytes, SHA256ef03f8f4792e36b8d8df8b2262ad9b88b8a732b833e1799bdacd714c4afe2170. Do NOT substitute the historical different6451-byte source [internal-source-reference].

Canonical exact inputs come from BOTH immutable scoped16 materials: [internal-source-reference],15305bytes/SHA256d5846089dd79e70e4aa35f67d5d66b8480c3dd72bca1de45359a281931f632aa, and [internal-source-reference],20685bytes/SHA256c4a0ef05c36066f7b2851dc18ea1c3cda599f724130ec0ce7a89785613cde5b1. Their full decoder RECOVER_C622_SCOPED16.py is2053bytes/SHA256cf90d8a2240f4b7154a902bc6ff558dbd2f3157683adadda1485a882cfd17d28. They reconstruct all16 exact source files and include all canonical generating input, both full independent exact geometric/mechanical auditors, mass checker and controls. No initial attachment or originating sandbox is needed.

Save the three literal source units beside one another. Save the two canonical materials as CANONICAL_PART1.md and CANONICAL_PART2.md and extract their exact decoder. Use fresh output directories:

```sh
python -B -S RECOVER_C622_SCOPED16.py SOURCE CANONICAL_PART1.md CANONICAL_PART2.md
python -B -S SOURCE/REPLAY_SCOPED.py PROOF
python -B -S facet_actuator_exact.py PROOF/A.json PROOF/raw.json actuator_bounded_exact.json
python -B -S facet_actuator.py audit PROOF/A.json actuator_exact.json
```

A.json is311825bytes/SHA256142ddb5d88fdc8b1721dbb62f52d9b71b78ac4c36e8600131235c6c4289698a0. raw.json is15437bytes/SHA256ac01d1625274b64f336a715e1f5462f40686f647f0b7d1a4d90a5ee21765adb5. Both are regenerated from canonical literals. The new exact program was actually run with CPython3.13.5, standard library only, assertions enabled and -B -S. No floating dependency is imported by part1. It produced:

CANONICAL_C622_TWENTY_SINGLE_FACET_COM_ACTUATORS_EXACT_PASS
CANONICAL_C622_ALL133_EAR_TARGET_INTERIOR_AND_COMMON_BOUNDED_RELEASE_PASS 95509 23c7c8c1cdbf47c1c256ae0d3bfcca07f5cd0609fff73b761caf8fbea5c0c961

Thus actuator_bounded_exact.json is95509bytes with that SHA256. The earlier exact audit output actuator_exact.json is79371bytes/SHA2562f73be416e1e50bb680bc75a5616a47b722f7cfa02f92a24b007c4ee76769793. All report data and exact moment/circuit quantities are recoverable from complete literal sources; report hashes themselves are not the evidence.

The current measured interpreter is3.13.5. The prior ALL133 proof material's environment string3.11.8 should not be treated as a newly measured fact about this subsequent execution. Its exact rational theorem and output identities are separate from that reported environment label.

## 5. Preserved floating attempts and their honest negative boundary

The separate part2 locator genuinely recomputes raw filled volume and first moments from all moving surface triangles and differentiates them; it does not hold a reference point fixed and call it the new centroid. It constrains the actual candidate vertices on a chosen facet by the variable plane plus their two other fixed planes. It prescreens facets containing all floating extra unstable vertices at the original centroid, solves up to40 Newton steps, and accepts a line-search step only if all nonincident supports and fan determinants exceed1e-12 and the centroid error decreases. It declares a numerical root at norm error<2e-13. Up to35 halvings per step are literal parameters in the source. These tolerances and floating sign classifications are NOT exact certificates, particularly for the canonical body's very small equilibrium margins. Prescreening may miss actual possibilities.

Executed commands with CPython3.13.5,NumPy2.3.5,SciPy1.17.0,one BLAS/OpenMP thread:

```sh
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python -B facet_actuator.py scan PROOF/A.json PROOF/raw.json actuator_scan_000_030.json 0 30
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python -B facet_actuator.py scan PROOF/A.json PROOF/raw.json actuator_scan_120_133.json 120 133
```

Both completed with FACET_ACTUATOR_FLOAT_LOCATOR_FINISHED_NOT_CERTIFICATE. The first30 deletion labels generated120 trials:114 geometry/descent line-search failures and6 iteration limits,0 numerical roots,0 accepted floating S1/U1 candidates. The last13 labels generated0 trials under the prescreen, so provide no direct optimization evidence. No other deletion interval has a completed report: a30:60 attempt was interrupted before producing its output. This is NOT an all133 search or a full-family impossibility proof.

Observed exact output pins: actuator_scan_000_030.json254081bytes/SHA256746d7846bc7f0674ae9883fff110d7ec683bf26e2fc7a52f9c00f2218623daa1; actuator_scan_120_133.json1534bytes/SHA25623d43012e0678459d1817f8cc7c9e3a1e78797459d5fa8f844464632924d6b17. Source, exact input checkpoint and all nondefault parameters are preserved here. Numerical byte-for-byte reproduction on a different BLAS/CPU is not asserted; any changed output is a new locator run, never silently the old pinned object.

These finite failures motivated the global convex potential, rather than proving an obstruction. The next useful frontier is the actual clipping problem across face-lattice changes, followed by exact true-facet/edge/ownCOM/full strict-and-weak certification. No new smaller own110 body has yet been produced.
