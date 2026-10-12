# material-e6e9bb057c2b

AI research material

<!-- historical-status:start -->
> **Historical AI material.** The title and claims below reflect the AI’s assessment at the time. Claims of proof, certification or completion are not a current verification verdict.
>
> [C622](../C622/README.md) passes the supplied exact checks; C<500 remains open; Minimum’s C≥34 remains a working lower bound requiring a consolidated proof. See [verification status and source gaps](../catalog/coverage.md).
<!-- historical-status:end -->

---

"""Exact constants for an analytic H5 actual-centroid transfer theorem.

This checks the rational inequalities in the accompanying proof. It does not
replay or independently verify the accepted three-fifths original-arrow atlas.
Only Python's standard library is required; no data files or seeds are used.
"""
from fractions import Fraction as F
from pathlib import Path
import hashlib
import json

IDENTITY = 'H5_THREE_FIFTHS_NONPARALLEL_TRANSFER_V2'
FACETS = ((6,5,4,3,2,1,0),(8,7,0,1),(7,6,0),(1,2,8),
          (9,8,2,3),(9,3,4),(4,5,7,9),(6,7,5),(7,8,9))
R, eta = F(3,2), F(1,100)
delta, W = F(178029,44800000000), 16385
eps, tau = F(1,2**42), F(1,2**37)

# Arbitrary corresponding-vertex perturbations, with the true facets retained.
N = sum(len(f)-2 for f in FACETS)
assert N == 16
assert N*(3*R**2 + 3*R*eta + eta**2) <= 112
assert (112*(3*R + 3*eta) + 3*N*R**3)/4 <= 168
assert 112*R + 1 + 112*eta + 168 <= 340
assert 340*R + 2*R + 680*eta <= 520
assert F(0) < eps <= eta
vertex_reserve = delta/2 - 520*W*eps
volume_floor = F(3,5) - 112*eps
assert vertex_reserve > 0 and volume_floor > 0

# Projective transformations x -> x/(1+t*x_1), |t| <= tau.
# Covariance is bounded by one quarter of the product of the ranges.
vertex_derivative_bound = R/(1-eta)
centroid_derivative_bound = R/(1-eta) + R*(1+eta)**4/(1-eta)**5
assert vertex_derivative_bound <= 2
assert centroid_derivative_bound <= 4
arrow_derivative_bound = 6*R + 4*R + 24*eta
assert arrow_derivative_bound <= 16
assert F(0) < tau <= eta
projective_reserve = delta/2 - 16*W*tau
assert projective_reserve > 0
report = {
    'identity': IDENTITY,
    'verdict': 'H5_THREE_FIFTHS_NONPARALLEL_TRANSFER_V2_PASS',
    'proof_status': 'Exact constant check for analytic transfer; source atlas accepted, not replayed.',
    'prototype_lambda_min': '3/5',
    'prototype_scaled_stress_gap': str(delta),
    'maximum_certificate_weight_sum': W,
    'vertex_perturbation_epsilon': str(eps),
    'cleared_arrow_lipschitz_bound': 520,
    'vertex_reserve_above_half_gap': str(vertex_reserve),
    'perturbed_D_lower_bound': str(volume_floor),
    'projective_t_bound': str(tau),
    'projective_vertex_displacement_over_abs_t_bound': str(vertex_derivative_bound),
    'projective_centroid_displacement_over_abs_t_bound': str(centroid_derivative_bound),
    'projective_uncleared_arrow_lipschitz_bound': 16,
    'projective_reserve_above_half_gap': str(projective_reserve),
    'limitations': [
        'Prototype must be in the accepted literal H5 three-fifths domain.',
        'Arbitrary vertex perturbations must retain the stated true cyclic facets.',
        'Projective maps preserve the genuine prototype face lattice in the positive chart.',
        'Actual homogeneous centroid is used; it is not transported projectively.',
        'No whole-H5 or E17-wide exclusion, attainment, or global bound change.'
    ]
}
raw = (json.dumps(report, sort_keys=True, indent=2) + '\n').encode('utf-8')
output = Path(__file__).with_name('h5_three_fifths_transfer_report.json')
output.write_bytes(raw)
print(raw.decode('utf-8'), end='')
print('BYTES_SHA256', len(raw), hashlib.sha256(raw).hexdigest())
print(report['verdict'])
