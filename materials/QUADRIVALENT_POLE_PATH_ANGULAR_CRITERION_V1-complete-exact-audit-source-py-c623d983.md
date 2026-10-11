# material-c623d983fdc6

Historical AI scientific source/proof material. Statements retain their original scope; this is not an independently reviewed theorem.

---

#!/usr/bin/env python3
"""Exact controls for QUADRIVALENT_POLE_PATH_ANGULAR_CRITERION_V1.
Standard library only. No optimizer, random seed, omitted input or geometry file.
The accompanying proof supplies the universal geometric and angle arguments.
This program verifies polynomial identities and two fully literal local controls.
"""
from __future__ import annotations
from fractions import Fraction as F
from pathlib import Path
import argparse
import hashlib
import json


def trim(p):
    p = tuple(F(x) for x in p)
    while len(p) > 1 and not p[-1]:
        p = p[:-1]
    return p


def add(a, b):
    return trim([(a[i] if i < len(a) else 0) +
                 (b[i] if i < len(b) else 0)
                 for i in range(max(len(a), len(b)))])


def scale(a, c):
    return trim([c*x for x in a])


def sub(a, b):
    return add(a, scale(b, -1))


def mul(a, b):
    out = [F(0)] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            out[i+j] += x*y
    return trim(out)


def power(a, n):
    out = (F(1),)
    for _ in range(n):
        out = mul(out, a)
    return out


def pdot(a, b):
    return add(mul(a[0], b[0]), mul(a[1], b[1]))


def pcross(a, b):
    return sub(mul(a[0], b[1]), mul(a[1], b[0]))


def psub(a, b):
    return (sub(a[0], b[0]), sub(a[1], b[1]))


def evaluate(p, x):
    out = F(0)
    for c in reversed(p):
        out = out*x+c
    return out


def dot(a, b):
    return sum((x*y for x, y in zip(a, b)), F(0))


def cross(a, b):
    return a[0]*b[1]-a[1]*b[0]


def vsub(a, b):
    return tuple(x-y for x, y in zip(a, b))


def exact_criterion(u, arrows):
    """Return the two polynomial guards B>0 and B^2-4*P*D>0."""
    if len(u) != 4 or len(arrows) != 3 or min(u) <= 0:
        raise ValueError('Four positive tangential squared radii and three arrows required')
    if any(not (0 <= a < 4 and 0 <= b < 4 and u[a] < u[b])
           for a, b in arrows):
        raise ValueError('Every arrow must strictly increase tangential squared radius')
    D = F(1)
    P = F(1)
    for a, b in arrows:
        D *= u[b]
        P *= u[a]
    B = D - sum((D*u[a]/u[b] for a, b in arrows), F(0))
    Q = B*B - 4*P*D
    return {'D': D, 'P': P, 'B': B, 'Q': Q,
            'passes': B > 0 and Q > 0}


def polygon_control(y, weights, sigma, arrows):
    n = len(y)
    if n != 4 or len(weights) != 4 or min(weights) <= 0:
        raise ValueError('A four-vertex positive normal combination is required')
    u = [dot(v, v) for v in y]
    areas = [cross(y[i], y[(i+1) % n]) for i in range(n)]
    turns = [cross(vsub(y[(i+1) % n], y[i]),
                   vsub(y[(i+2) % n], y[(i+1) % n])) for i in range(n)]
    assert min(areas) > 0 and min(turns) > 0
    assert all(sum(weights[i]*y[i][j] for i in range(n)) == 0 for j in range(2))
    escape = [[dot(y[i], y[j])-u[i] for j in range(n)] for i in range(n)]
    found = [(i, j) for i in range(n) for j in range(n)
             if i != j and escape[i][j] >= 0]
    assert sorted(found) == sorted(arrows)
    criterion = exact_criterion(u, arrows)
    assert criterion['passes']
    return {'y': y, 'positive_weights': weights, 'weight_sum': sum(weights),
            'sigma': sigma, 'tangential_squared_radii': u,
            'pole_squared_norms': [sigma+x for x in u],
            'origin_edge_areas': areas, 'polygon_turns': turns,
            'escape_matrix': escape, 'nonnegative_distinct_arrows': found,
            'criterion': criterion, 'scope': 'LOCAL_NORMAL_CONE_NOT_A_GLOBAL_110_BODY'}


def symbolic_family():
    zero, one, k = (F(0),), (F(1),), (F(0), F(1))
    s = power(k, 2)
    one_s = add(one, s)
    y = [(one, zero), (one, k), (sub(one, s), scale(k, 2)),
         (sub(one, scale(s, 3)), sub(scale(k, 3), power(k, 3)))]
    u = [pdot(v, v) for v in y]
    assert u == [power(one_s, i) for i in range(4)]
    areas = [pcross(y[i], y[(i+1) % 4]) for i in range(4)]
    assert areas == [k, mul(k, one_s), mul(k, power(one_s, 2)), mul(k, sub(s, (F(3),)))]
    turns = [pcross(psub(y[(i+1) % 4], y[i]),
                    psub(y[(i+2) % 4], y[(i+1) % 4])) for i in range(4)]
    k3 = power(k, 3)
    assert turns == [k3, mul(k3, one_s), mul(k3, add(s, (F(3),))), scale(k3, 3)]
    w = [mul(one_s, add(s, (F(3),))), sub(s, (F(3),)), sub(s, (F(3),)), (F(3),)]
    for j in range(2):
        z = zero
        for i in range(4):
            z = add(z, mul(w[i], y[i][j]))
        assert z == zero
    assert add(add(w[0], w[1]), add(w[2], w[3])) == mul(s, add(s, (F(6),)))
    escape = [[sub(pdot(y[i], y[j]), u[i]) for j in range(4)] for i in range(4)]
    expected = [
        [zero, zero, scale(s, -1), scale(s, -3)],
        [scale(s, -1), zero, zero, scale(mul(s, one_s), -1)],
        [scale(mul(s, add(s, (F(3),))), -1), scale(mul(s, one_s), -1), zero, zero],
        [scale(mul(s, add(add(power(s, 2), scale(s, 3)), (F(6),))), -1),
         scale(mul(s, add(add(power(s, 2), scale(s, 4)), (F(3),))), -1),
         scale(mul(s, power(one_s, 2)), -1), zero]]
    assert escape == expected
    D = mul(mul(u[1], u[2]), u[3])
    P = mul(mul(u[0], u[1]), u[2])
    B = sub(D, add(add(mul(mul(u[0], u[2]), u[3]),
                       mul(power(u[1], 2), u[3])), mul(u[1], power(u[2], 2))))
    Q = sub(power(B, 2), scale(mul(P, D), 4))
    assert B == mul(sub(s, (F(2),)), power(one_s, 5))
    assert Q == mul(mul(power(s, 2), sub(s, (F(3),))), power(one_s, 9))
    return {'y_polynomials_low_degree_first': y,
            'norm_polynomials_low_degree_first': u,
            'weight_polynomials_low_degree_first': w,
            'escape_polynomials_low_degree_first': escape,
            'B_polynomial_low_degree_first': B,
            'Q_polynomial_low_degree_first': Q,
            'parameter_domain': 'k>0 and k^2>3',
            'factorizations': {'B': '(k^2-2)*(1+k^2)^5',
                               'Q': 'k^4*(k^2-3)*(1+k^2)^9'},
            'sharp_infimum_radius_ratio': 8,
            'infimum_not_attained_in_strict_local_U_domain': True}, y


def normalize(obj):
    if isinstance(obj, F):
        return str(obj)
    if isinstance(obj, dict):
        return {k: normalize(v) for k, v in obj.items()}
    if isinstance(obj, (tuple, list)):
        return [normalize(v) for v in obj]
    return obj


def build_data():
    family, ypolys = symbolic_family()
    kval = F(7, 4)
    y = [tuple(evaluate(p, kval) for p in v) for v in ypolys]
    chain = polygon_control(y, [F(x) for x in (6305, 16, 16, 768)], F(1),
                            [(0, 1), (1, 2), (2, 3)])
    assert chain['tangential_squared_radii'][3] == F(274625, 4096) > 64
    chain['k'] = kval
    yy = [(F(1), F(0)), (F(1), F(3)), (F(-1), F(1)), (F(-1, 10), F(-1, 100))]
    inward = polygon_control(yy, [F(x) for x in (40, 1, 1, 400)], F(9),
                             [(0, 1), (2, 1), (3, 2)])
    n = inward['pole_squared_norms']
    assert n[2]*2 > n[1] and n[0]*4 < n[1]*3
    inward['literal_TREE253_facet_labels_in_cyclic_order'] = [7, 0, 1, 2]
    inward['x'] = [F(0), F(0), F(1, 3)]
    inward['q_in_same_order'] = [list(v)+[F(3)] for v in yy]
    inward['satisfies_n1_over_n0_gt_half_and_n7_over_n0_lt_three_quarters'] = True
    inward['not_checked_or_claimed'] = ['remaining_five_poles', 'volume_centroid',
                                      'actual_Lambda', 'global_S_U_H', 'E17_realization']
    return normalize({'identity': 'QUADRIVALENT_POLE_PATH_ANGULAR_CRITERION_V1',
                      'symbolic_family': family,
                      'rational_chain_control': chain,
                      'inward_control_with_two_TREE253_norm_bounds': inward,
                      'new_whole_incidence_exclusions': 0,
                      'accepted_global_lower_bound_C': 34})


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('mode', choices=('build', 'check'))
    parser.add_argument('--output', default='quad_corner_audit.json')
    args = parser.parse_args()
    raw = (json.dumps(build_data(), sort_keys=True, indent=2, ensure_ascii=True)+'\n').encode('ascii')
    path = Path(args.output)
    if args.mode == 'build':
        if path.exists() and path.read_bytes() != raw:
            raise RuntimeError('Existing output differs; refusing to replace it')
        path.write_bytes(raw)
    elif path.read_bytes() != raw:
        raise RuntimeError('Exact output comparison failed')
    print('QUADRIVALENT_POLE_PATH_SYMBOLIC_AND_RATIONAL_AUDITS_PASS',
          len(raw), hashlib.sha256(raw).hexdigest())


if __name__ == '__main__':
    main()
