"""Direct, exact test of unstable vertices of a uniform solid from ASCII STL.

No imports from the research workflow or its verifiers. Standard library only.
Usage: python3 check_stl_vertices.py model.stl --output diagnostic.json

For each vertex v, let c be the volume centroid. The plane at v with normal
v-c supports the body strictly at v exactly when
    (v-c) dot (w-v) < 0 for every other vertex w.
All decision arithmetic is integer arithmetic; floats are used only to print
diagnostic magnitudes and to deliberately simulate lower-precision imports.
"""
import argparse
import csv
import hashlib
import json
import math
import re
import struct
from collections import Counter
from fractions import Fraction
from functools import reduce
from pathlib import Path


def dot(a, b):
    return sum(x * y for x, y in zip(a, b))


def cross(a, b):
    return (a[1]*b[2]-a[2]*b[1], a[2]*b[0]-a[0]*b[2], a[0]*b[1]-a[1]*b[0])


def sub(a, b):
    return tuple(x-y for x, y in zip(a, b))


def parse_stl(path):
    content = Path(path).read_bytes()
    text = content.decode('ascii')
    tokens = re.findall(r'^\s*vertex\s+(\S+)\s+(\S+)\s+(\S+)\s*$', text, re.M)
    facets = len(re.findall(r'^\s*facet normal\s', text, re.M))
    assert len(tokens) == facets * 3 and facets > 0
    ids, vertices, indices = {}, [], []
    for row in tokens:
        v = tuple(Fraction(s) for s in row)
        if v not in ids:
            ids[v] = len(vertices)
            vertices.append(v)
        indices.append(ids[v])
    triangles = [tuple(indices[i:i+3]) for i in range(0, len(indices), 3)]
    return vertices, triangles, hashlib.sha256(content).hexdigest()


def integer_table(vertices):
    denominator = reduce(math.lcm, (c.denominator for v in vertices for c in v))
    return [tuple(int(c*denominator) for c in v) for v in vertices], denominator


def closed_surface(triangles, n):
    directed = Counter((a, b) for t in triangles for a, b in zip(t, t[1:]+t[:1]))
    assert all(a != b and count == 1 and directed[b, a] == 1
               for (a, b), count in directed.items())
    assert len({i for t in triangles for i in t}) == n
    assert n - len(directed)//2 + len(triangles) == 2


def centered_integer_table(vertices, triangles):
    points, denominator = integer_table(vertices)
    volume6, moments24 = 0, [0, 0, 0]
    for triangle in triangles:
        a, b, c = (points[i] for i in triangle)
        det = dot(a, cross(b, c))
        volume6 += det
        for axis in range(3):
            moments24[axis] += det*(a[axis]+b[axis]+c[axis])
    assert volume6 > 0, 'Expected outward-oriented solid with positive volume'
    divisor = 4*volume6
    centered = [tuple(divisor*v[k]-moments24[k] for k in range(3)) for v in points]
    q = divisor * denominator
    center = tuple(Fraction(m, q) for m in moments24)
    return centered, q, center, Fraction(volume6, 6*denominator**3)


def support_rows(centered, q, vertices):
    result = []
    for i, v in enumerate(centered):
        witness, largest = max(((j, dot(v, sub(w, v))) for j, w in enumerate(centered)
                               if i != j), key=lambda pair: pair[1])
        value = float(Fraction(largest, q*q))
        length = math.sqrt(float(Fraction(dot(v, v), q*q)))
        result.append(dict(stl_vertex_id=i, xyz=list(map(float, vertices[i])),
                           witness_stl_id=witness,
                           witness_xyz=list(map(float, vertices[witness])),
                           exact_sign=(largest > 0)-(largest < 0),
                           max_dot=value, support_plane_violation=value/length))
    return result


def analyze(vertices, triangles):
    closed_surface(triangles, len(vertices))
    centered, q, center, volume = centered_integer_table(vertices, triangles)
    rows = support_rows(centered, q, vertices)
    return dict(vertices=len(vertices), triangles=len(triangles),
                centroid=list(map(float, center)), volume=float(volume),
                unstable=[r['stl_vertex_id'] for r in rows if r['exact_sign'] < 0],
                degenerate=[r['stl_vertex_id'] for r in rows if r['exact_sign'] == 0],
                support_rows=rows)


def controls():
    # Regular tetrahedron, all four vertices unstable; shifted COM must be exact.
    v = [tuple(map(Fraction, t)) for t in [(1,1,1),(1,-1,-1),(-1,1,-1),(-1,-1,1)]]
    t = [(0,1,2),(0,3,1),(0,2,3),(1,3,2)]
    assert analyze(v,t)['unstable'] == [0,1,2,3]
    shift = (Fraction(7,3), Fraction(-5,7), Fraction(11,13))
    vv = [tuple(a+b for a,b in zip(p,shift)) for p in v]
    assert analyze(vv,t)['unstable'] == [0,1,2,3]
    assert centered_integer_table(vv,t)[2] == shift
    try:
        analyze(v, t[:-1])
    except AssertionError:
        pass
    else:
        raise AssertionError('Open-surface control incorrectly accepted')


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('stl', type=Path)
    parser.add_argument('--output', type=Path, required=True)
    args = parser.parse_args()
    controls()
    vertices, triangles, sha = parse_stl(args.stl)
    variants = {'exact_STL_decimals': vertices,
                'IEEE_binary64': [tuple(Fraction.from_float(float(x)) for x in v) for v in vertices],
                'IEEE_binary32': [tuple(Fraction.from_float(struct.unpack('<f', struct.pack('<f', float(x)))[0])
                                        for x in v) for v in vertices]}
    results = {}
    for name, table in variants.items():
        result = analyze(table, triangles)
        results[name] = result
        print(name, json.dumps({k:v for k,v in result.items() if k != 'support_rows'}), flush=True)
    rows = results['exact_STL_decimals']['support_rows']
    tolerance = {str(e):sum(r['support_plane_violation'] <= e for r in rows)
                 for e in [0, 1e-12, 1e-10, 1e-9, 1e-8, 1e-7, 1e-6]}
    results['support_distance_tolerance_counts'] = tolerance
    results['source_stl_sha256'] = sha
    results['controls'] = ['regular tetrahedron', 'exact translation', 'open mesh rejected']
    args.output.write_text(json.dumps(results, indent=2)+'\n')
    with args.output.with_suffix('.csv').open('w', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=list(rows[0]))
        writer.writeheader()
        writer.writerows(rows)
    print('Tolerance counts:', tolerance)
    print('STL sha256:', sha)


if __name__ == '__main__':
    main()
