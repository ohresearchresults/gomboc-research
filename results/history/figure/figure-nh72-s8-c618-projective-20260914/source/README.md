# Exact S8 coarsening and two finite projective/physical-metric nonwinners

The exact coordinate parent is COORD_CAP_RL_C624_STRONG_G8 (S8), NOT
COORD_TRIPLE_C624_OWN121_G14 and NOT the previous NH72_PM images.
BASE_GENERATOR.json is the complete 9599-byte S8 generator, SHA256
bf9fdaf05231ceb11fba9fde10c8a638e664b52233b2da5cb11977b2f4ff27b2.
It was reconstructed from all six literal S8 source capsule parts in the
2026-09-14 journal, which jointly decode to 170010 bytes, SHA256
44319c99762df191373664c4e89bbeb7fb70db771c7c38e0a19e4e0ea2645fd3.
The analytical parent is asg_0VmaVrvx49KpctuyG-BFJ0Vy, SHA256
c5ea8fda8761454dd25eacd0b1140dd5c53332e513b4b4c09f64617ad11f33d3.
No old H94 or NH72_PM coordinate data are needed.

## Exact objects

RECONSTRUCT.recover must first reconstruct all137 H rows with anchor137.
Then endpoint.py explicitly removes the row named by delete. Merely setting
active_ids does not delete anything in the original reconstruction function.
The remaining136 input positions map to original support IDs in LABELS.json.
For an original inequality n.x<=h and parameters (t,A), the new inequality is
(A^-T(n+h*t)).y<=h, with all rational denominators cleared and gcd divided.
The physical body is {A*x/(1+t.x): x in the deleted body}, at density1.
Its centre is recomputed from its own ordinary filled volume, not assigned.

PARAMETERS.json contains both identity deletion bodies and two new D4 images.
Both deletion bodies are 175/309/136 strict121/weak000. Both images are
175/309/136 strict222/weak000. None is a winner or a new C<624 strict110 record.
The A matrices are literal rational physical matrices, not implicit Cholesky data.
The exact denominator minimum is proved by nonnegative support coefficients
and a feasible attaining triple-intersection vertex. Every pair of full
independent A/B reports is byte-identical. Third centred integer integration
and full true-edge and polar basin maps are separate outputs.

## Exact replay

Use CPython3.13.5 (standard library only), assertions enabled. Do not use -O.
All output directories must initially be absent.

python -B -S REPLAY.py --out fresh-output

Terminal marker:
NH72_S8_C618_FOUR_NONWINNERS_SOURCE_ONLY_COLD_PASS

Individual case replay:
python -B -S REPLAY.py --out fresh-case --case P4_DEL99

The manifest binds every other source file; expected exact output bytes bind
all four objects. No stored vertex, moment, or audit report is an input.
The final replay checks every inverse vertex map and maximal cycle and every
true edge against the exact deleted base. Integration diagonals are never edges.

## New bounded centroid chart

For Q_t={x/(1+t.x):x in K}, let b=g(t) be its ordinary filled centroid,
Sigma its filled covariance, delta=1-t.b>0, and c=b/delta in int(K).
The analytical parent gives Dg=-5*Sigma-b*b^T and the global diffeomorphism
b:D->R^3. Here the new pullback chart c:D->int(K) is also an analytic
bijection. Its Jacobian is

Dc=-5(delta*I+b*t^T)*Sigma/delta^2,
det(Dc)=-125*det(Sigma)/delta^4<0.

Proof of global surjectivity and uniqueness: for any c in int(K), let L=K-c.
There is exactly one u such that F_u(L) has own volume centroid0, by the
parent's strictly convex log-volume minimization. Since -c is interior to L,
d0=1-u.c>0. Set t=u/d0. Then
F_u(x-c)=((I+c*t^T)F_t(x)-c)/d0.
Taking ordinary centroids yields g(t)=d0*c and delta=d0. Conversely any t
produces u=delta*t and the same unique centered F_u(K-c). The displayed
Jacobian is nonsingular, so the inverse is analytic. This does not assign c
as the mass centre of unchanged K. It solves for a different physical body.

pullback_identity.py verifies the finite rational instance of this identity
for every vertex of each exact endpoint and proves zero transformed first
moments by exact affine mass covariance. It is an identity/mass check, not
an extra independent geometry audit. It also rechecks max ||q_i||_1<5 for
each S8 deletion, giving its own [-1/5,1/5]^3 inner cube.

## Numeric global centroid and covariance-normalized metric chart

numerical/centroid_metric.py uses b plus five upper-triangular physical metric
coordinates. For each b it solves the unique strictly convex logV+4*b.t
problem. Every evaluated geometry uses the actual returned own centroid.
Derivatives include dt/db=-(5*Sigma+b*b^T)^-1. Both radial and physically
centred polar escapes are recalculated using the same geometry/mass.

numerical/isotropic_metric.py normalizes actual filled covariance:
Sigma=L*L^T, W=det(Sigma)^(1/6)*L^-1, det W=1, A=M*W with M upper triangular,
positive diagonal and determinant1. Up to rotations and scale this retains
all five physical metric directions. The chart is global, while each finite
search used the bounds and limits in EXPERIMENTS.json; these are not an
exhaustive coverage proof. The numerical Cholesky is only a proposal chart.
The accepted endpoints use rational D4 matrices and have exact proof gates.

numerical/pullback_centroid.py samples material locations c in int(K), with
actual source tetrahedral volume weights and positive barycentric samples.
For each c it solves the zero-centroid problem on K-c and obtains t and b,
then optimizes the five linked physical metric coordinates. Sample weights
are only a search distribution, never a replacement for uniform filled mass.

## Reproduce finite numerical experiments

CPython3.13.5, NumPy2.3.5, SciPy1.17.0; one BLAS/OMP thread. Platform-sensitive
floating trajectories are not required to recover any exact endpoint.
Each experiment's complete parameters and observed summary are in
EXPERIMENTS.json. Run after the exact replay:

OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python SEARCH_REPLAY.py iso_99_cauchy_none fresh-output new-search
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python SEARCH_REPLAY.py pullback99 fresh-output new-pullback

All21 named experiments have full source units and exact seeds/bounds.
metric_milp used24 cases per deletion and5 seconds per MILP. All48 original
solver calls reached the time limit without an incumbent, not infeasibility.
The wider subset screen's full deterministic input is the unfiltered S8 H
system recovered from BASE_GENERATOR, followed by numerical/subset_screen.py.
It enumerates exactly287 defined support subsets. Those additional subsets
were only numerical screens, not new independently audited endpoints.

The selected D4 proposals were records413 and118 respectively of experiments
iso_99_cauchy_none and iso_117_cauchy_none. Full selected parameter/checkpoint
records are in SELECTED_PROPOSALS.json. Their exact decimal nearest-grid
recovery is independently checked by:
python -B -S ROUND_SELECTED.py

In particular, small normalized residues of very anisotropic trial metrics
were never treated as proof of cancellation or of metric-family exclusion.
The exact D4 images have deep remaining radial/polar basins.
