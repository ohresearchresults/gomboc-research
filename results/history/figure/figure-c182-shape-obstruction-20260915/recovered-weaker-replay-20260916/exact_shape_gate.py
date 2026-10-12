"""Exact central-disk/slab and central-segment/cylinder gates for Finch C182.
Usage: python -B -S exact_shape_gate.py RAW.json A.json B.json OUTPUT.json
The input reports are independently produced by the preserved Finch auditors.
"""
import hashlib
import json
import sys
from fractions import Fraction as F
from pathlib import Path

sys.set_int_max_str_digits(0)
RAW_SHA = '3a3d80e75979c004f995115dd4bfb491560af0f661af0840c6868f3b5f046d86'
AUDIT_SHA = 'caf78ccee9abec82174d346227b2da7d99a13b823c88a4ef405e3e8cb9d1967d'

def load(path, sha):
    b = Path(path).read_bytes()
    assert hashlib.sha256(b).hexdigest() == sha, ('wrong input', str(path))
    return json.loads(b)

def dot(a, b):
    return sum(x*y for x, y in zip(a, b))

def run(raw_path, a_path, b_path):
    raw = load(raw_path, RAW_SHA)
    a = load(a_path, AUDIT_SHA)
    b = load(b_path, AUDIT_SHA)
    assert a == b
    assert [a[k] for k in ('V', 'E', 'F')] == [54, 91, 39]
    assert a['counts'] == [2, 2, 2] and a['weak'] == [0, 0, 0]
    g = tuple(map(F, a['raw_centroid']))
    X = [tuple(F(v)-c for v, c in zip(p, g)) for p in a['raw_vertices']]
    H = [tuple(map(F, p)) for p in raw['H']]
    assert len(X) == 54 and len(H) == 136
    n = (47, 17, 0)
    nn = dot(n, n)
    Rs, hs, Ru, hu = F(3, 40), F(1, 56), F(1, 4), F(1, 8)
    slab = [1-dot(n, x)**2/(nn*hs**2) for x in X]
    cylinder = [1-(x[0]**2+x[1]**2)/hu**2 for x in X]
    disk, segment = [], []
    for row in H:
        v, h = row[:3], row[3]
        d = h-dot(v, g)
        assert d > 0
        proj = nn*dot(v, v)-dot(v, n)**2
        assert proj >= 0
        disk.append(1-Rs**2*proj/(nn*d**2))
        segment.append(1-Ru*abs(v[2])/d)
    assert min(slab) > F(1, 100)
    assert min(disk) > F(1, 100)
    assert min(segment) > F(1, 20)
    assert min(cylinder) > F(3, 100)
    def limiting(values):
        return [i for i, v in enumerate(values) if v == min(values)]
    result = {
        'status': 'EXACT_C182_TWO_STABLE_TWO_UNSTABLE_GEOMETRIC_GATE_PASS',
        'object': 'C182_TWO_PLANE222',
        'input_sha256': {'raw': RAW_SHA, 'A': AUDIT_SHA, 'B': AUDIT_SHA},
        'counts_checked': {'vertices': len(X), 'all_supplied_supports': len(H),
                           'active_maximal_supports': len(a['active_input_indices'])},
        'stable_gate': {'n': list(n), 'n_squared': nn, 'disk_radius': str(Rs),
                        'slab_halfheight': str(hs), 'ratio': str(Rs/hs),
                        'slab_relative_squared_margin_gt': '1/100',
                        'disk_relative_squared_margin_gt': '1/100',
                        'limiting_vertex': limiting(slab),
                        'limiting_supplied_support': limiting(disk)},
        'unstable_gate': {'n': [0, 0, 1], 'segment_halflength': str(Ru),
                          'cylinder_radius': str(hu), 'ratio': str(Ru/hu),
                          'segment_relative_margin_gt': '1/20',
                          'cylinder_relative_squared_margin_gt': '3/100',
                          'limiting_vertex': limiting(cylinder),
                          'limiting_supplied_support': limiting(segment)},
        'new_equilibrium_census_claim': False,
        'shape_sandwich_beta_over_alpha_excluded_for_S1': '<21/5',
        'affine_2norm_condition_excluded_for_S1': '<21/5'
    }
    return result

if __name__ == '__main__':
    if len(sys.argv) != 5:
        raise SystemExit(__doc__)
    answer = run(*sys.argv[1:4])
    out = Path(sys.argv[4])
    if out.exists():
        raise SystemExit('Output exists; choose a new output path.')
    out.write_text(json.dumps(answer, sort_keys=True, separators=(',', ':')))
    print(answer['status'])
    print(out.read_text())
