# material-100b3c6b96d7

AI research material

<!-- historical-status:start -->
> **Historical AI material.** The title and claims below reflect the AI’s assessment at the time. Claims of proof, certification or completion are not a current verification verdict.
>
> [C622](../C622/README.md) passes the supplied exact checks; C<500 remains open; Minimum’s C≥34 remains a working lower bound requiring a consolidated proof. See [verification status and source gaps](../catalog/coverage.md).
<!-- historical-status:end -->

---

"""K34 joint-triangle effective gap: exact arithmetic and geometric controls.

Requires joint_equality_exact.py with the pinned bytes below in this directory.
python -S joint_mass_effective_gap.py build
python -S joint_mass_effective_gap.py check
The compactness and positivity theorems are in the companion proof, not inferred
from the controls. No control is asserted to be a K34 / 110 witness.
"""
from fractions import Fraction as F
from pathlib import Path
import hashlib
import importlib.util
import json
import sys

assert __debug__
HERE = Path(__file__).resolve().parent
PARENT = HERE / 'joint_equality_exact.py'
PARENT_PIN = (12055, 'abe63a2592e8da97611c2e3883b9f59eafc92b21e8291ef1d12a148383db223e')
raw_parent = PARENT.read_bytes()
assert (len(raw_parent), hashlib.sha256(raw_parent).hexdigest()) == PARENT_PIN
spec = importlib.util.spec_from_file_location('joint_equality_dependency', PARENT)
assert spec is not None and spec.loader is not None
base = importlib.util.module_from_spec(spec)
spec.loader.exec_module(base)


def effective_arithmetic():
    # Complete uniform l1 bounds for the inherited 33-variable chart.
    n, m, d, height = 33, 386, 12, 2**64
    alpha = 1082881
    normal = 8
    T = 16 * 6
    U = 16 * 6 * 3
    b = 4 * T * (3 * normal) + 3 * normal * U
    D = 4 * T * 6 + 3 * U * normal
    K = 16 * D
    poly_bounds = {
        'max_simplex': 1 + 48**2,
        'coordinate_box': 2,
        'support': 3 * normal * 2,
        'coplanarity': 3 * normal * 2,
        'orientation': 3 * normal**2,
        'volume': T + 16,
        'inverse_support': b + 1,
        'inverse_nonnegative': 1,
        'metric_minors': 6 * (alpha + 1)**3,
        'metric_trace': 4,
        'vertex_arrow': 9 * (4*T + U) * 2,
        'pole_arrow': 2 * b * (9 * normal * 2 * normal),
        'tetrahedron_Delta': 48,
        'tetrahedron_complement': T + 48,
        'mass_lower_numerator': K + 48*T,
        'mass_upper_numerator': T*T + K,
        'joint_mass_numerator': T*T + 48*T + 2*K,
    }
    assert (T, U, b, D, K) == (96, 288, 16128, 9216, 147456)
    assert poly_bounds['joint_mass_numerator'] == 308736
    assert max(poly_bounds.values()) < height
    assert max(height, 2*n+2*m) == height
    # JPT base B = 2^(4-n/2)*H*d^n. For these parameters B^2=2^103*12^66.
    assert 2*(4 + 64) - n == 103
    assert 12**66 < 2**237
    # Therefore B<2^170. All arithmetic below uses integers only.
    exponent = n * 2**n * d**n
    binary_loss_bound = 170 * exponent + 10
    assert 4 * 16**2 == 1024
    assert binary_loss_bound < 2**164
    return {
        'n': n, 'm': m, 'd': d, 'height': height,
        'alpha': alpha, 'uniform_l1_bounds': poly_bounds,
        'JPT_exponent': exponent,
        'strict_upper_bound_on_negative_binary_log_after_division': binary_loss_bound,
        'epsilon': '2^(-2^164)',
        'degree_of_new_numerators_at_most': 6,
        'degree_of_chart_constraints_at_most': 12,
        'maximum_denominator_division': 1024,
    }


def outward_normal(points, face):
    assert len(face) == 3
    a, b, c = [points[i] for i in face]
    nn = base.cross(base.sub(b, a), base.sub(c, a))
    signs = [base.dot(nn, base.sub(p, a)) for p in points]
    assert any(signs)
    if any(v > 0 for v in signs):
        nn = tuple(-v for v in nn)
        signs = [-v for v in signs]
    assert max(signs) == 0 and min(signs) < 0
    assert {i for i, s in enumerate(signs) if s == 0} == set(face)
    return nn


def pair_control(H, face_i=(0, 1, 2), face_j=(0, 1, 3)):
    points, V, moment, g = H['points'], H['V'], H['M'], H['g']
    assert tuple(sorted(face_i)) in H['facets']
    assert tuple(sorted(face_j)) in H['facets']
    shared = set(face_i) & set(face_j)
    assert len(shared) == 2
    first = next(i for i in face_i if i not in shared)
    opposite = next(i for i in face_j if i not in shared)
    ni, nj = outward_normal(points, face_i), outward_normal(points, face_j)
    ai, aj = points[face_i[0]], points[face_j[0]]
    T, U = 6*V, tuple(24*x for x in moment)
    di_origin, dj_origin = base.dot(ni, ai), base.dot(nj, aj)
    Ki = 4*T*di_origin - base.dot(U, ni)
    Kj = 4*T*dj_origin - base.dot(U, nj)
    Delta = base.dot(ni, base.sub(ai, points[opposite]))
    Delta_reverse = base.dot(nj, base.sub(aj, points[first]))
    assert Delta == Delta_reverse > 0
    h = Delta/T
    masses = (3*Ki/(4*T*T), 3*Kj/(4*T*T))
    z = (Ki/(T*T), Kj/(T*T))
    distance_numerators = (base.dot(ni, base.sub(ai, g)), base.dot(nj, base.sub(aj, g)))
    assert masses == tuple(v/(2*V) for v in distance_numerators)
    G = T*T + Delta*T - Ki - Kj
    delta = 3*G/(4*T*T)
    assert delta == 3*(1+h)/4-sum(masses)
    Yi = [base.dot(ni, base.sub(ai, p))/distance_numerators[0] for p in points]
    Yj = [base.dot(nj, base.sub(aj, p))/distance_numerators[1] for p in points]
    lam_ij = masses[1] * sum(Yi[v] for v in face_j)/3
    lam_ji = masses[0] * sum(Yj[v] for v in face_i)/3
    assert lam_ij == h*masses[1]/masses[0]
    assert lam_ji == h*masses[0]/masses[1]
    assert lam_ij*lam_ji == h*h
    nums = {
        'Delta': Delta,
        'T_minus_Delta': T-Delta,
        'Ki_minus_Delta_T': Ki-Delta*T,
        'Kj_minus_Delta_T': Kj-Delta*T,
        'T_squared_minus_Ki': T*T-Ki,
        'T_squared_minus_Kj': T*T-Kj,
        'G_joint': G,
    }
    return {'faces': (face_i, face_j), 'T': T, 'U': U,
            'Ki': Ki, 'Kj': Kj, 'numerators': nums, 'h': h,
            'masses': masses, 'z': z, 'delta': delta,
            'Lambda_ij': lam_ij, 'Lambda_ji': lam_ji}


def build():
    arithmetic = effective_arithmetic()
    family = []
    for e in (F(1,10000), F(1,100), F(1,8)):
        points = [tuple(base.pe(p, e) for p in v) for v in base.point_polynomials()]
        H = base.hull(points)
        assert H['f_vector'] == [10,17,9]
        pair = pair_control(H)
        assert all(v > 0 for v in pair['numerators'].values())
        # This only compares finite rational controls with a small elementary floor.
        # The universal epsilon theorem is not deduced from these comparisons.
        assert pair['h'] > F(1,2) and pair['delta'] > F(1,2**64)
        assert H['g'][0] == H['g'][1] > 0 and H['g'][2] > 0
        assert H['g'][0] + H['g'][2] == F(1,2)
        family.append({'epsilon_parameter': e, 'vertices': H['points'],
                       'facets': H['facets'], 'V': H['V'], 'g': H['g'],
                       'pair': pair, 'status': 'Actual E17; S>=2 in displayed metric, not a K34/110 witness'})
    saturation = []
    for t,r,z in ((F(2),F(1),F(-1,2)),(F(7),F(2),F(-2)),(F(3,2),F(2,5),F(-1,3))):
        s = t-r
        assert r > 0 and s > 0 and 1-t < z < 0
        H = base.hull([(0,0,0),(0,0,1),(0,1,0),(1,0,0),(r,s,z)])
        pair = pair_control(H)
        assert H['f_vector'] == [5,9,6]
        assert pair['delta'] == pair['numerators']['G_joint'] == 0
        saturation.append({'parameters': (t,r,s,z), 'pair': pair,
                           'status': 'Actual five-vertex equality body; outside K34'})
    data = {'identity': 'K34_ACTUAL_ADJACENT_TRIANGLE_EFFECTIVE_GAP_164_V1',
            'parent_source': {'filename': PARENT.name, 'bytes': PARENT_PIN[0], 'sha256': PARENT_PIN[1]},
            'arithmetic': arithmetic, 'E17_nonmechanical_controls': family,
            'five_vertex_saturation_controls': saturation,
            'scope': 'Arithmetic and true geometric identities checked exactly. Compactness, universal positivity, and JPT application are proved in the companion text. No K34 witness or E17 exclusion is claimed.'}
    return (json.dumps(base.encode(data), sort_keys=True, separators=(',',':'), ensure_ascii=True)+'\n').encode('ascii')


if __name__ == '__main__':
    mode = sys.argv[1] if len(sys.argv)>1 else 'check'
    assert mode in ('build','check')
    raw = build()
    out = Path('joint_mass_effective_gap.json')
    if mode == 'build': out.write_bytes(raw)
    else: assert out.read_bytes() == raw
    print('K34_JPT_33_386_12_HEIGHT64_EXPONENT164_PASS')
    print('JOINT_GAP_TRUE_GEOMETRY_CONTROLS_PASS',3,3)
    print('JOINT_MASS_EFFECTIVE_GAP_RECOVERY_PASS',len(raw),hashlib.sha256(raw).hexdigest())
