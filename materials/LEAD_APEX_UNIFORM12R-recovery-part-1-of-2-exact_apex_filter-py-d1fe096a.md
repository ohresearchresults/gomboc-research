# material-d1fe096adc75

AI research material

<!-- historical-status:start -->
> **Historical AI material.** The title and claims below reflect the AI’s assessment at the time. Claims of proof, certification or completion are not a current verification verdict.
>
> [C622](../C622/README.md) passes the supplied exact checks; C<500 remains open; Minimum’s C≥34 remains a working lower bound requiring a consolidated proof. See [verification status and source gaps](../catalog/coverage.md).
<!-- historical-status:end -->

---

#!/usr/bin/env python3
"""Exact two-unstable-vertex filter for one-apex convex hull extensions.
Python >=3.10; standard library only. Input rational strings or integers, never floats.
Usage: python exact_apex_filter.py --self-test
       python exact_apex_filter.py input.json
Input: {"vertices": [[x,y,z], ...], "facets": [[indices in outward cyclic order],...],
        "apex": [x,y,z]}. Facets must be maximal, without collinear boundary vertices.
A negative filter outcome is inconclusive, never evidence of class110.
"""
from __future__ import annotations
import argparse
from collections import defaultdict, deque
from fractions import Fraction as Q
import json
from pathlib import Path
from typing import Any, Sequence

Vec = tuple[Q, Q, Q]
ZERO: Vec = (Q(0), Q(0), Q(0))

def scalar(x: Any) -> Q:
    if isinstance(x, bool) or not isinstance(x, (str, int)):
        raise ValueError('Coordinates must be exact rational strings or integers.')
    return Q(x)

def vector(x: Sequence[Any]) -> Vec:
    if len(x) != 3:
        raise ValueError('Each vector must have three coordinates.')
    return tuple(scalar(t) for t in x)  # type: ignore[return-value]

def add(a: Vec, b: Vec) -> Vec:
    return tuple(a[i] + b[i] for i in range(3))  # type: ignore[return-value]

def sub(a: Vec, b: Vec) -> Vec:
    return tuple(a[i] - b[i] for i in range(3))  # type: ignore[return-value]

def mul(s: Q, a: Vec) -> Vec:
    return tuple(s * t for t in a)  # type: ignore[return-value]

def dot(a: Vec, b: Vec) -> Q:
    return sum((a[i] * b[i] for i in range(3)), Q(0))

def cross(a: Vec, b: Vec) -> Vec:
    return (a[1]*b[2]-a[2]*b[1], a[2]*b[0]-a[0]*b[2], a[0]*b[1]-a[1]*b[0])

def norm2(a: Vec) -> Q:
    return dot(a, a)

def det(a: Vec, b: Vec, c: Vec) -> Q:
    return dot(a, cross(b, c))

def validate_core(vertices: list[Vec], facets: list[list[int]]) -> list[tuple[int, int, int]]:
    """Validate exact outward maximal convex facets and a closed connected sphere."""
    n = len(vertices)
    if n < 4 or len(set(vertices)) != n:
        raise ValueError('Need at least four distinct vertices.')
    edges: dict[tuple[int, int], list[tuple[int, int]]] = defaultdict(list)
    stars: list[set[int]] = [set() for _ in vertices]
    triangles: list[tuple[int, int, int]] = []
    face_sets: set[frozenset[int]] = set()
    for k, f in enumerate(facets):
        if len(f) < 3 or len(set(f)) != len(f) or any(type(i) is not int or not 0 <= i < n for i in f):
            raise ValueError('Invalid facet cycle.')
        sf = frozenset(f)
        if sf in face_sets:
            raise ValueError('Repeated facet.')
        face_sets.add(sf)
        a, b, c = (vertices[f[j]] for j in range(3))
        normal = cross(sub(b, a), sub(c, a))
        if normal == ZERO:
            raise ValueError('Collinear consecutive facet vertices are unsupported.')
        height = dot(normal, a)
        for j, w in enumerate(vertices):
            value = dot(normal, w) - height
            if (j in sf and value != 0) or (j not in sf and value >= 0):
                raise ValueError('Facet is not outward, maximal, and supporting.')
        for j, ia in enumerate(f):
            ib = f[(j + 1) % len(f)]
            edge = sub(vertices[ib], vertices[ia])
            for ic in f:
                if ic not in (ia, ib) and dot(normal, cross(edge, sub(vertices[ic], vertices[ia]))) <= 0:
                    raise ValueError('Facet cycle is not strictly convex and correctly ordered.')
            edges[tuple(sorted((ia, ib)))].append((ia, ib))
            stars[ia].add(k)
        triangles.extend((f[0], f[j], f[j + 1]) for j in range(1, len(f) - 1))
    if any(len(s) < 3 for s in stars):
        raise ValueError('Every listed point must be a genuine vertex.')
    adjacency: list[set[int]] = [set() for _ in vertices]
    for (a, b), incidence in edges.items():
        if len(incidence) != 2 or incidence[0] != incidence[1][::-1]:
            raise ValueError('Boundary edges must occur twice with opposite orientation.')
        adjacency[a].add(b)
        adjacency[b].add(a)
    if n - len(edges) + len(facets) != 2:
        raise ValueError('Boundary Euler characteristic is not two.')
    seen = {0}
    queue = deque([0])
    while queue:
        for w in adjacency[queue.popleft()]:
            if w not in seen:
                seen.add(w)
                queue.append(w)
    if len(seen) != n:
        raise ValueError('Boundary graph is disconnected.')
    return triangles

def rational_json(x: Any) -> Any:
    if isinstance(x, Q):
        return str(x)
    if isinstance(x, dict):
        return {k: rational_json(v) for k, v in x.items()}
    if isinstance(x, (list, tuple)):
        return [rational_json(v) for v in x]
    return x

def exact_filter(data: dict[str, Any]) -> dict[str, Any]:
    vertices = [vector(v) for v in data['vertices']]
    facets = data['facets']
    p = vector(data['apex'])
    triangles = validate_core(vertices, facets)
    W0, Wadd = Q(0), Q(0)
    T0, Sadd = ZERO, ZERO
    visible_triangles = 0
    for ia, ib, ic in triangles:
        a, b, c = vertices[ia], vertices[ib], vertices[ic]
        total = add(add(a, b), c)
        w0 = det(a, b, c)
        W0 += w0
        T0 = add(T0, mul(w0, total))
        # Six times the added tetrahedron volume, positive exactly on visible faces.
        wa = dot(cross(sub(b, a), sub(c, a)), sub(p, a))
        if wa > 0:
            Wadd += wa
            Sadd = add(Sadd, mul(wa, total))
            visible_triangles += 1
    if W0 <= 0:
        raise ValueError('Core must be full dimensional with positive oriented volume.')
    W = W0 + Wadd
    if Wadd == 0:
        return {'status': 'NO_EXTERNAL_APEX', 'core_volume': W0 / 6}
    T = add(add(T0, Sadd), mul(Wadd, p))
    centroid = mul(1 / (4 * W), T)
    alpha = Wadd / (4 * W)
    q = mul(1 / (4 * W0 + 3 * Wadd), add(T0, Sadd))
    assert centroid == add(mul(alpha, p), mul(1 - alpha, q))
    # q is a convex combination of the old solid centroid and visible-face centroids.
    assert all(dot(cross(sub(vertices[f[1]], vertices[f[0]]), sub(vertices[f[2]], vertices[f[0]])), sub(q, vertices[f[0]])) <= 0 for f in facets)
    farthest = max(range(len(vertices)), key=lambda i: norm2(sub(vertices[i], centroid)))
    v = vertices[farthest]
    v_radial = sub(v, centroid)
    p_radial = sub(p, centroid)
    root_old_margins = [-dot(v_radial, sub(w, v)) for i, w in enumerate(vertices) if i != farthest]
    root_apex_margin = -dot(v_radial, sub(p, v))
    apex_margins = [-dot(p_radial, sub(w, p)) for w in vertices]
    # The root is automatically strict relative to every other old vertex.
    assert all(x > 0 for x in root_old_margins)
    root_U = root_apex_margin > 0
    apex_U = min(apex_margins) > 0
    B2 = norm2(sub(p, q))
    D2 = max(norm2(sub(w, q)) for w in vertices)
    sufficient_slack = 2 * alpha * alpha * B2 - (1 - alpha) * D2
    if sufficient_slack > 0:
        assert root_U and apex_U
    return rational_json({
        'status': 'TWO_STRICT_U_CERTIFIED' if root_U and apex_U else 'INCONCLUSIVE',
        'core_volume': W0 / 6, 'added_volume': Wadd / 6, 'new_volume': W / 6,
        'new_centroid': centroid, 'alpha': alpha, 'q': q,
        'farthest_old_vertex': farthest, 'old_root_strict_U': root_U,
        'apex_strict_U': apex_U, 'root_old_min_margin': min(root_old_margins),
        'root_apex_margin': root_apex_margin, 'apex_min_margin': min(apex_margins),
        'sufficient_slack': sufficient_slack,
        'visible_triangles': visible_triangles,
        'warning': 'This is an exclusion filter, not a full equilibrium census.'
    })

CUBE = {
    'vertices': [[-1,-1,-1],[1,-1,-1],[1,1,-1],[-1,1,-1],[-1,-1,1],[1,-1,1],[1,1,1],[-1,1,1]],
    'facets': [[0,3,2,1],[4,5,6,7],[0,1,5,4],[1,2,6,5],[2,3,7,6],[3,0,4,7]],
    'apex': [0,0,100]
}

def self_test() -> None:
    result = exact_filter(CUBE)
    assert result['status'] == 'TWO_STRICT_U_CERTIFIED'
    assert result['core_volume'] == '8' and result['added_volume'] == '132'
    assert result['new_centroid'] == ['0', '0', '3399/140']
    assert result['alpha'] == '33/140' and result['q'] == ['0', '0', '99/107']
    # Rational test points well outside the uniform bound for r=1, R=2, V0=8.
    for p in ([24,0,0], [0,-24,0], [0,0,24], [30,40,0], [-30,-40,50], [100,1,1]):
        sample = dict(CUBE, apex=p)
        assert exact_filter(sample)['status'] == 'TWO_STRICT_U_CERTIFIED'
    unchanged = dict(CUBE, apex=[0,0,0])
    assert exact_filter(unchanged)['status'] == 'NO_EXTERNAL_APEX'
    print(json.dumps(result, sort_keys=True, indent=2))
    print('EXACT_APEX_FILTER_SELF_TEST_OK')

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('input', nargs='?', type=Path)
    parser.add_argument('--self-test', action='store_true')
    args = parser.parse_args()
    if args.self_test:
        self_test()
    elif args.input is not None:
        try:
            print(json.dumps(rational_json(exact_filter(json.loads(args.input.read_text()))), sort_keys=True, indent=2))
        except (ValueError, KeyError, TypeError, ZeroDivisionError) as exc:
            parser.exit(2, f'Invalid exact input: {exc}\n')
    else:
        parser.error('Specify an input JSON file or --self-test.')
