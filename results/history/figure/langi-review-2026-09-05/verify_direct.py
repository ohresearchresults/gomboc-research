"""Exact finite verification of a uniform-density convex polyhedron.

Python 3 standard library only. Run: python3 verify_direct.py body_1213.json
All geometric decisions use unbounded integers. No search code is imported.
Equilibria are tested directly against supporting planes of the whole vertex set.
"""
import hashlib
import json
import math
import sys
import time
from collections import defaultdict
from itertools import combinations
from pathlib import Path


def require(condition, message):
    if not condition:
        raise ValueError(message)


def dot(a, b):
    return sum(x*y for x, y in zip(a, b))


def sub(a, b):
    return tuple(x-y for x, y in zip(a, b))


def cross(a, b):
    return (a[1]*b[2]-a[2]*b[1], a[2]*b[0]-a[0]*b[2], a[0]*b[1]-a[1]*b[0])


def determinant(a, b, c):
    return dot(a, cross(b, c))


def verify(data):
    started = time.perf_counter()
    raw = [tuple(p) for p in data['vertices']]
    triangles = [tuple(t) for t in data['triangles']]
    denominator = data['raw_denominator']
    require(type(denominator) is int and denominator > 0, 'Bad denominator')
    require(all(len(p) == 3 and all(type(x) is int for x in p) for p in raw), 'Bad coordinates')
    require(len(raw) == len(set(raw)), 'Duplicate points')
    require(all(len(t) == 3 and len(set(t)) == 3 and all(type(i) is int and 0 <= i < len(raw) for i in t) for t in triangles), 'Bad triangles')
    require(len(triangles) == len(set(tuple(sorted(t)) for t in triangles)), 'Duplicate triangles')

    # The true volume centroid is the first moment / volume, not a freely chosen origin.
    volume6 = 0
    moment24 = [0, 0, 0]
    for i, j, k in triangles:
        a, b, c = raw[i], raw[j], raw[k]
        v = determinant(a, b, c)
        volume6 += v
        for axis in range(3):
            moment24[axis] += v*(a[axis]+b[axis]+c[axis])
    require(volume6 > 0, 'Nonpositive oriented volume')
    scale = 4*volume6
    points = [tuple(scale*p[d]-moment24[d] for d in range(3)) for p in raw]

    # Identify exact maximal supporting planes; group coplanar triangulation pieces.
    facets = defaultdict(list)
    tri_edges = defaultdict(list)
    links = [dict() for _ in raw]
    centered_moments = [0, 0, 0]
    for tid, (i, j, k) in enumerate(triangles):
        a, b, c = points[i], points[j], points[k]
        n = cross(sub(b, a), sub(c, a))
        h = dot(n, a)
        require(h > 0, 'Degenerate triangle or wrong outward orientation')
        gcd = math.gcd(*n, h)
        plane = tuple(x//gcd for x in (*n, h))
        facets[plane].append(tid)
        for axis in range(3):
            centered_moments[axis] += determinant(a, b, c)*(a[axis]+b[axis]+c[axis])
        for u, v, w in ((i, j, k), (j, k, i), (k, i, j)):
            tri_edges[tuple(sorted((u, v)))].append((u, v, plane))
            require(v not in links[u], 'Duplicate vertex-link edge')
            links[u][v] = w
    require(centered_moments == [0, 0, 0], 'Centered first moment did not vanish')
    require(len(raw)-len(tri_edges)+len(triangles) == 2, 'Wrong triangulated Euler characteristic')
    for link in links:
        require(len(link) >= 3, 'Unused or nonextreme vertex')
        p = start = next(iter(link))
        seen = set()
        while p not in seen:
            require(p in link, 'Open vertex link')
            seen.add(p)
            p = link[p]
        require(p == start and len(seen) == len(link), 'Vertex link is not one cycle')

    boundary = defaultdict(dict)
    true_edges = []
    vertex_facets = [set() for _ in raw]
    graph = [set() for _ in raw]
    for edge, occurrences in tri_edges.items():
        require(len(occurrences) == 2, 'Nonmanifold or open surface')
        u, v, left = occurrences[0]
        vv, uu, right = occurrences[1]
        require((u, v) == (uu, vv), 'Inconsistent triangle orientation')
        graph[u].add(v)
        graph[v].add(u)
        if left == right:
            continue
        true_edges.append(edge)
        require(u not in boundary[left] and v not in boundary[right], 'Branched facet boundary')
        boundary[left][u] = v
        boundary[right][v] = u
        vertex_facets[u].update((left, right))
        vertex_facets[v].update((left, right))
    reached, stack = {0}, [0]
    while stack:
        for v in graph[stack.pop()]:
            if v not in reached:
                reached.add(v)
                stack.append(v)
    require(len(reached) == len(raw), 'Disconnected surface')

    stable = []
    facet_cycles = []
    support_tests = 0
    for plane, tids in facets.items():
        normal, height = plane[:3], plane[3]
        contact = set()
        for i, p in enumerate(points):
            gap = height-dot(normal, p)
            require(gap >= 0, 'Face plane cuts the vertex hull')
            support_tests += 1
            if gap == 0:
                contact.add(i)
        nxt = boundary[plane]
        require(len(nxt) >= 3, 'Missing maximal facet')
        p = start = min(nxt)
        cycle = []
        while p not in cycle:
            require(p in nxt, 'Open facet boundary')
            cycle.append(p)
            p = nxt[p]
        require(p == start and set(cycle) == set(nxt) == contact, 'Incomplete facet contact set')
        require(contact == set(i for tid in tids for i in triangles[tid]), 'Bad facet triangulation')
        facet_cycles.append(cycle)
        n2 = dot(normal, normal)
        foot_numerator = tuple(height*x for x in normal)
        interior = True
        for a, b, c in zip(cycle, cycle[1:]+cycle[:1], cycle[2:]+cycle[:2]):
            require(dot(normal, cross(sub(points[b], points[a]), sub(points[c], points[b]))) > 0, 'Nonconvex facet cycle')
            edge = sub(points[b], points[a])
            toward_foot = sub(foot_numerator, tuple(n2*x for x in points[a]))
            if dot(normal, cross(edge, toward_foot)) <= 0:
                interior = False
        if interior:
            stable.append(cycle)
    for incident in vertex_facets:
        require(any(determinant(a[:3], b[:3], c[:3]) != 0 for a, b, c in combinations(incident, 3)), 'Point is not an extreme vertex')
    require(len(raw)-len(true_edges)+len(facets) == 2, 'Wrong maximal-face Euler characteristic')

    # Whole-hull support test at each vertex, independent of local four-sign rules.
    unstable, degenerate = [], []
    for i, p in enumerate(points):
        values = [dot(p, sub(q, p)) for j, q in enumerate(points) if j != i]
        if max(values) < 0:
            unstable.append(i)
        elif max(values) == 0:
            degenerate.append(('vertex', i))

    # Edge foot q = a - d*(a.d)/(d.d); evaluate its normal on EVERY vertex.
    saddles = []
    for i, j in true_edges:
        a, d = points[i], sub(points[j], points[i])
        den, num = dot(d, d), -dot(a, d)
        require(den > 0, 'Zero-length true edge')
        if not 0 < num < den:
            continue
        qnum = tuple(den*a[k]+num*d[k] for k in range(3))
        contacts = []
        for k, p in enumerate(points):
            value = dot(qnum, sub(p, a))
            if value > 0:
                break
            if value == 0:
                contacts.append(k)
        else:
            if set(contacts) == {i, j}:
                saddles.append([i, j])
            else:
                degenerate.append(('edge', [i, j]))
    return {
        'vertices': len(raw), 'edges': len(true_edges), 'faces': len(facets),
        'triangles': len(triangles), 'class_SUH': [len(stable), len(unstable), len(saddles)],
        'degenerate_equilibria': degenerate,
        'mechanical_complexity': len(raw)+len(true_edges)+len(facets)-len(stable)-len(unstable)-len(saddles),
        'stable_faces': stable, 'unstable_vertices': unstable, 'saddle_edges': saddles,
        'raw_volume_numerator': str(volume6), 'raw_volume_denominator': str(6*denominator**3),
        'raw_centroid_numerators': list(map(str, moment24)), 'raw_centroid_denominator': str(scale*denominator),
        'centered_first_moments': list(map(str, centered_moments)),
        'global_facet_vertex_support_tests': support_tests,
        'arithmetic': 'Python unbounded integers; no floating-point geometric decisions',
        'elapsed_seconds': time.perf_counter()-started,
    }


if __name__ == '__main__':
    source = Path(sys.argv[1] if len(sys.argv) > 1 else 'body_1213.json')
    raw_bytes = source.read_bytes()
    report = verify(json.loads(raw_bytes))
    report['data_sha256'] = hashlib.sha256(raw_bytes).hexdigest()
    print(json.dumps(report, indent=2))
    require(report['class_SUH'] == [1, 1, 0] and not report['degenerate_equilibria'], 'Not a nondegenerate mono-monostatic polyhedron')
    print('DIRECT_ALL_VERTEX_SUPPORT_VERIFICATION_PASS')
