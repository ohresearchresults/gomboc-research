"""Exact volume-moment capacity test after removing AX10's four bad facets.

For K subset P subset Q and scalar coordinate y,
M_y(P) >= M_y(K) + M_y(Q intersect {y<=0}) - M_y(K intersect {y<=0}).
This is a relaxation: it permits adding every negative-y point and no
positive-y point, even if the resulting set is nonconvex.
"""
from fractions import Fraction as F
from itertools import combinations
from pathlib import Path
import json
from verify_ax10_centroid_obstruction import POINTS, hull, mass, dot, cross, sub

ROOT = Path(__file__).resolve().parent


def solve3(rows, rhs):
    cof = [cross(rows[1], rows[2]), cross(rows[2], rows[0]), cross(rows[0], rows[1])]
    d = dot(rows[0], cof[0])
    if d == 0:
        return None
    return tuple(sum(rhs[i]*cof[i][j] for i in range(3))/d for j in range(3))


def bounded_certificate(rows):
    # A positive dependence on four normals of rank three puts zero strictly
    # inside their tetrahedron, so the common recession cone is {0}.
    for ids in combinations(range(len(rows)), 4):
        ns = [rows[i][0] for i in ids]
        columns = [sub(ns[j], ns[3]) for j in range(3)]
        solution = solve3(list(zip(*columns)), tuple(-x for x in ns[3]))
        if solution is None:
            continue
        weights = solution+(1-sum(solution),)
        if min(weights) > 0:
            assert all(sum(weights[i]*ns[i][j] for i in range(4)) == 0 for j in range(3))
            return dict(row_indices=ids, weights=list(map(str, weights)))
    raise ValueError('No four-normal boundedness certificate found')


def polygon_cycle(points, normal):
    axis = max(range(3), key=lambda k: abs(normal[k]))
    axes = [k for k in range(3) if k != axis]
    ordered = sorted(points, key=lambda p: (p[axes[0]], p[axes[1]]))
    def orient(a, b, c):
        return ((b[axes[0]]-a[axes[0]])*(c[axes[1]]-a[axes[1]])
                -(b[axes[1]]-a[axes[1]])*(c[axes[0]]-a[axes[0]]))
    lower, upper = [], []
    for p in ordered:
        while len(lower) >= 2 and orient(lower[-2], lower[-1], p) <= 0:
            lower.pop()
        lower.append(p)
    for p in reversed(ordered):
        while len(upper) >= 2 and orient(upper[-2], upper[-1], p) <= 0:
            upper.pop()
        upper.append(p)
    cycle = lower[:-1]+upper[:-1]
    if dot(cross(sub(cycle[1], cycle[0]), sub(cycle[2], cycle[0])), normal) < 0:
        cycle.reverse()
    return cycle


def hpoly_mass(rows):
    bounded = bounded_certificate(rows)
    points = set()
    for ids in combinations(range(len(rows)), 3):
        vertex = solve3([rows[i][0] for i in ids], [rows[i][1] for i in ids])
        if vertex is not None and all(dot(n, vertex) <= h for n, h in rows):
            points.add(vertex)
    assert len(points) >= 4
    volume = F(0)
    moments = [F(0)]*3
    edge_counts = {}
    face_count = 0
    for n, h in rows:
        face = [p for p in points if dot(n, p) == h]
        if len(face) < 3:
            continue
        cycle = polygon_cycle(face, n)
        assert set(cycle) == set(face)
        face_count += 1
        for a, b in zip(cycle, cycle[1:]+cycle[:1]):
            e = tuple(sorted((a, b)))
            edge_counts[e] = edge_counts.get(e, 0)+1
        for j in range(1, len(cycle)-1):
            a, b, c = cycle[0], cycle[j], cycle[j+1]
            dv = dot(a, cross(b, c))/6
            assert dv >= 0
            volume += dv
            for k in range(3):
                moments[k] += dv*(a[k]+b[k]+c[k])/4
    assert volume > 0
    assert set(edge_counts.values()) == {2}
    assert len(points)-len(edge_counts)+face_count == 2
    return dict(volume=volume, moments=moments, vertices=sorted(points),
                f_vector=[len(points), len(edge_counts), face_count], boundedness=bounded)


def main():
    fs = hull(POINTS)
    source_rows = [(n, h) for f, n, h in fs]
    w = tuple(-x/3 for x in POINTS['C'])
    removed = [f for f, n, h in fs if dot(n, w) > h]
    retained = [(n, h) for f, n, h in fs if dot(n, w) <= h]
    clip = ((F(0), F(1), F(0)), F(0))
    Q = hpoly_mass(retained)
    Qminus = hpoly_mass(retained+[clip])
    Kminus = hpoly_mass(source_rows+[clip])
    v, m = mass(POINTS, fs)
    lower = m[1]+Qminus['moments'][1]-Kminus['moments'][1]
    assert lower > 0, 'Four-face capacity obstruction was not established'
    # Upper volume Q also yields a lower bound on the actual centroid y.
    cy = lower/Q['volume']
    payload = dict(verdict='ANY_EXTENSION_RETAINING_THE_OTHER_TWELVE_HALFSPACES_HAS_POSITIVE_Y_MOMENT',
                   removed_faces=removed, source_moment_y=m[1], source_negative_y_moment=Kminus['moments'][1],
                   container_negative_y_moment=Qminus['moments'][1], lower_bound_moment_y=lower,
                   lower_bound_moment_y_decimal=float(lower), upper_volume=Q['volume'],
                   lower_bound_centroid_y=cy, lower_bound_centroid_y_decimal=float(cy),
                   container=Q, container_negative_part=Qminus, source_negative_part=Kminus,
                   scope='Original K is retained as a subset. Arbitrarily many new vertices and all equilibrium changes are allowed. The remaining 12 original halfspaces must still hold. This is not a global AX10 impossibility theorem.')
    (ROOT/'ax10-four-face-capacity.json').write_text(json.dumps(payload, default=str, indent=2)+'\n')
    for k in ['lower_bound_moment_y_decimal','lower_bound_centroid_y_decimal']:
        print(k, payload[k])
    print('CONTAINER', Q['f_vector'], 'VOLUME', float(Q['volume']))
    print('EXACT_AX10_FOUR_FACE_CAPACITY_OBSTRUCTION_PASS')


if __name__ == '__main__':
    main()
