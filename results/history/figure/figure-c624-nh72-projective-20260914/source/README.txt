NH72: finite projective/metric whole-basin turnover of literal COORD_TRIPLE_C624_OWN121_G14.

STATUS: MODERATE and FAR are two DIFFERENT uniformly filled own-centred exact
nonwinners: V177/E312/F137, strict222, weak000, 2E=624. They are NOT strict110.
The accepted positive incumbent C626 is not improved. The FAR body transports
ALL 159 vertices in the parent's closed bad radial basin to its new root102;
its NEW bad basin consists of 16 former root-reaching vertices. Its two residual
primal barriers and its extra stable basin remain deep; this is not a near-win.

EXACT INPUT AUTHORITY
BASE_GENERATOR.json is the complete literal C624 generator,12993 bytes,
SHA256 9794a36115719432a426f28f25ec8a16f28224237acc2b94b2acb4625dcfbede.
It was recovered by applying the exact C624_PATCH.py,2633 bytes,
SHA81e772f1667a95566e6a973870e0496a14efa4fb51a270fc8ffa4baf99bf2e78,
to the journal's nine-file C626 capsule, decoded45413 bytes,
SHAd8a1e7da95dfef6262bc260e454e3cdc281d2be155e62b6ec26f698f01319403.
The predecessor G14 generator has SHA2a478cf7e3b6caafd094a14504f4a2004e3e67ba948d6052575dd1ce0da3ccb3.
No H94 coordinate data or old seven-point seed is used or required.
Analytical evidence parent: asg_2HGGq8-7ONKepX_fzDbIFMHU,
SHAec30671f86d10b513b15576b25048c82f0f2058f35dfccf0d23c3ba28994bd51.
Geometry evidence predecessor: asg_zSkJefQuEkGHd3_fzUFMGE19,
SHA5f57852087082e58a87bf09e4674cddc11627f384f7ac9124c0c8102d12d1d29.
The supplied full BASE generator eliminates all dependencies on those older
capsules for this replay. All controls, contact plan, groups and labels are present.

EXACT DEFINITIONS
For the reconstructed parent K={x:n_i.x<=h_i}, parameters are the integers
in PARAMETERS.json divided by D=100000000, independently for each object.
The raw physical body is {A*x/(1+t.x):x in K}; subtract its OWN ordinary-volume
centroid. The physical A is the rational matrix in PARAMETERS, NOT a numerical
Cholesky factor or a separately specified Gram matrix. New supports are
A^(-T)(n_i+h_i*t).y<=h_i, primitively integer-normalized by exact arithmetic.
The admissibility_supports triple is an exact certificate: solve
sum(alpha_k*q_i)= -t; alpha>=0 and sum(alpha)<1. Every projective denominator is
at least1-sum(alpha)>0. A has exact positive determinant. All maximal faces
remain active, but this is independently confirmed by both full audits.

SELF-CONTAINED EXACT REPLAY (only Python standard library, assertions ON)
  python -B -S REPLAY.py --out never-existing-output
The driver verifies MANIFEST before and after, checks tetra and weak-prism
fixtures and invalid inputs, reconstructs both new H bodies, executes two
independent complete exact auditors, reintegrates centred integer tetrahedra,
recovers the full vertex-label map and both true-edge basins, proves the finite
own-centroid monotonicity instance, and compares all frozen output bytes.
Expected final marker:
  NH72_C624_TWO_PROJECTIVE_NONWINNERS_SOURCE_ONLY_COLD_PASS
For a bounded individual stage:
  python -B -S exact_orbit.py . FAR new-output BUILD
  python -B -S exact_orbit.py . FAR new-output A
  python -B -S exact_orbit.py . FAR new-output B
  python -B -S exact_orbit.py . FAR new-output MASS
  python -B -S exact_orbit.py . FAR new-output EXTRA
  python -B -S basin_detail.py . FAR new-output
  python -B -S exact_orbit.py . FAR new-output FINISH
The final marker above is not a winner marker: expected strict222 is intentional.
A.json/B.json contain ALL rational raw coordinates, ordinary volume, all raw
first moments, own centroid, maximal faces/edges and exhaustive strict/weak census.
EXTRA.json contains new-index<->parent Cartesian-lex maps, exact denominator lower
bound and minimum, rational det(A), fraction sizes and the entire primal basin.
DETAIL.json contains independent parent-mass recovery, exact complete old-basin
turnover, complete physical-centred polar basin and exact rational barrier values.
No integration diagonal is counted as a physical edge.

GLOBAL MASS THEOREM (proof in the handoff)
Let V(t)=Vol({x/(1+t.x):x in K}) and g(t) its OWN raw volume centroid.
On D={t:1+t.v>0 for all vertices}, g=-(1/4)grad(log V),
Dg=-5*Cov-gg^T, and Hess(log V)=20*Cov+4*gg^T>0.
D is bounded convex; V tends to infinity at its boundary. Therefore g:D->R^3
is a one-to-one onto analytic map with nonsingular derivative. Any specified
raw-centroid target b is reached at the UNIQUE minimizer of log V+4*b.t.
This does NOT allow evaluating mechanics at b on the old geometry.
Exact source normals prove [-1/5,1/5]^3 is contained in K. All its projective
images contain [-1/10,1/10]^3, implying -Dg>=I/(7500*V).
Thus (t-s).(g(s)-g(t)) >= |t-s|^2/[7500*max(V(s),V(t))].
For a fixed invertible A, pinning A*g(t) to A*g(0) forces t=0. This excludes
only centre-frozen pure projective compensation, NOT the full variable-A orbit
or any other physical redesign. Translation by the actual new centroid is
always permitted and does not contradict the theorem.

NUMERICAL METHODS AND REPRODUCIBLE INPUTS
Executed environment: CPython3.13.5, NumPy2.3.5, SciPy1.17.0, one BLAS/OMP thread.
Exact endpoint verification has no numerical-package dependency.
First create the parent geometry only when needed for numerical continuation:
  python -B -S RECONSTRUCT.py BASE_GENERATOR.json base_raw.json
  python -B -S check_A.py base_raw.json base_A.json
Then, with OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1:
  python discovery/orbit_search.py base_A.json search --starts 120 --evals 600 --seed 720624
  python discovery/projective_screen.py base_A.json screen --directions 256
  python discovery/forest_search.py base_A.json forest --starts 80 --outer 10 --seed 720625
  python discovery/condition_chamber.py base_A.json discovery/MODERATE_START.json moderate_conditioned.json
  python discovery/condition_chamber.py base_A.json discovery/FAR_START.json far_conditioned.json
  python discovery/centroid_chart.py base_A.json inverse_tests.json
Every numerical trial recomputes filled mass. No claimed continuous no-birth path.
Time-limited MILP outputs are not infeasibility certificates. Numerical optimizer
trajectories are platform-dependent. Static rational PARAMETERS define the
endpoints independently of any floating-point rediscovery or optimizer history.
The stored conditioned checkpoints give the actual pre-rounding inputs;
t and each physical A entry were rounded to the nearest multiple of10^-8.
The exact resulting integer arrays and the complete parent are already included.
