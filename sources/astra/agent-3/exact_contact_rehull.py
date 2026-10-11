"""Exact convex hull of rational contact-chart points, even after a contact event.

Old planes are retained only when exactly supporting every physical point.
Qhull nominates additional planes; it does not decide any exact incidence.
An explicit enclosing box guarantees boundedness. Exact two-way containment
certifies the resulting body before its equilibrium census is reported.
"""
import argparse
import hashlib
import json
import time
from math import gcd, lcm
from pathlib import Path

import numpy as np
from gmpy2 import mpq
from scipy.spatial import ConvexHull

from exact_audit_vertices import check_B, cross, dot, sub
from exact_barcode_report import report
from exact_projective_audit import apply, inverse
from goal_nomination import ExactGoalCandidateFound


def reconstruct(meta, q, grid):
    controls = [int(round(float(v)*grid)) for v in q]
    meta = dict(meta, grid=grid, free_controls=controls)
    A = [(mpq(0),)*3 for _ in range(meta['nodes'])]
    for p in meta['plan']:
        x = [mpq(0)]*3
        for axis, v in p['fixed'].items():
            x[int(axis)] = mpq(v)
        for axis, i in zip(p['free_axes'], p['free_indices']):
            x[axis] = mpq(controls[i], grid)
        if p['deps']:
            M = [[A[j][axis] for axis in p['axes']] for j in p['deps']]
            b = [1-dot(A[j], x) for j in p['deps']]
            for axis, v in zip(p['axes'], apply(inverse(M), b)):
                x[axis] = v
        A[p['node']] = tuple(x)
    return meta, A[meta['F']:], A[:meta['F']]


def run(source, params, out, grid=None):
    source, params, out = Path(source), Path(params), Path(out)
    out.mkdir(parents=True, exist_ok=False)
    start = time.time()
    q = np.load(params)
    if grid is None:
        grid = max(float(v).as_integer_ratio()[1] for v in q)
    meta, original, Y = reconstruct(json.loads(source.read_text()), q, grid)
    mean = tuple(mpq(float(v)) for v in np.array(original, float).mean(0))
    X = [sub(x, mean) for x in original]
    rows = set()
    def add(n, h):
        r = (*n, h)
        D = lcm(*(int(v.denominator) for v in r))
        z = tuple(int(v*D) for v in r)
        d = gcd(*z)
        rows.add(tuple(v//d for v in z))
    old_kept = []
    old_rejected = []
    for f, y in enumerate(Y):
        h = 1-dot(y, mean)
        if h > 0 and all(dot(y, x) <= h for x in X):
            add(y, h)
            old_kept.append(f)
        else:
            old_rejected.append(f)
    # The six exact box planes enclose all inputs strictly. They establish
    # boundedness independently of floating hull nominations.
    for axis in range(3):
        for sign in [-1, 1]:
            n = tuple(mpq(sign if j == axis else 0) for j in range(3))
            h = max(dot(n, x) for x in X) + 1
            assert h > 0
            add(n, h)
    hull = ConvexHull(np.array(X, float))
    nominations = []
    rejected = []
    for tri in hull.simplices:
        a, b, c = [X[int(i)] for i in tri]
        n = cross(sub(b, a), sub(c, a))
        h = dot(n, a)
        if h < 0:
            n, h = tuple(-v for v in n), -h
        if h <= 0 or not all(dot(n, x) <= h for x in X):
            rejected.append(list(map(int, tri)))
            continue
        add(n, h)
        nominations.append(list(map(int, tri)))
    B = lambda v: json.dumps(v, default=str, sort_keys=True, separators=(',', ':')).encode()
    raw = dict(H=sorted(rows))
    (out/'raw.json').write_bytes(B(raw))
    (out/'coordinates.json').write_bytes(B(dict(points=X, original_points=original, translation=mean, density=1)))
    (out/'source_construction.json').write_bytes(B(meta))
    (out/'definition.json').write_bytes(B(dict(source=str(source.resolve()), source_sha256=hashlib.sha256(source.read_bytes()).hexdigest(),
        params=str(params.resolve()), params_sha256=hashlib.sha256(params.read_bytes()).hexdigest(), grid=grid,
        old_supports_retained=old_kept, old_supports_rejected=old_rejected, supporting_nominations=nominations,
        non_supporting_nominations=rejected, definition='uniformly filled exact convex hull of the rational contact-chart points; original contact graph is not presumed',
        boundedness='six explicit strict axis-aligned rational enclosing halfspaces')))
    print('CONTACT_REHULL_EXACT_PLANES', out, dict(planes=len(rows), old_retained=len(old_kept), old_rejected=len(old_rejected), rejected_nominations=len(rejected)), flush=True)
    r = check_B.run(raw)
    found = {tuple(map(mpq, p)) for p in r['raw_vertices']}
    assert found <= set(X), 'bounding intersection has a vertex outside the input point set; hull reconstruction is incomplete'
    assert all(dot(row[:3], x) <= row[3] for row in raw['H'] for x in X), 'a plane excluded an input point'
    # All input points lie in the bounded intersection; every intersection
    # vertex is an input point. These are the two hull inclusions.
    lookup = {x:i for i, x in enumerate(X)}
    r['source_vertex_ids'] = [lookup[tuple(map(mpq, p))] for p in r['raw_vertices']]
    (out/'audit.json').write_bytes(B(r))
    su = {k:r[k] for k in ['V', 'E', 'F', 'counts', 'weak', 'face_primitive_zero_count', 'vertex_max_zero_count', 'edge_primitive_zero_count']}
    su.update(C_2E=2*r['E'], VplusEplusF=r['V']+r['E']+r['F'], seconds=time.time()-start,
              audit_sha256=hashlib.sha256((out/'audit.json').read_bytes()).hexdigest(),
              goal_met=r['counts']==[1,1,0] and r['weak']==[0,0,0] and 34<=2*r['E']<500 and r['V']+r['E']+r['F']<500)
    (out/'summary.json').write_text(json.dumps(su, indent=2))
    report(out)
    print('CONTACT_REHULL_EXACT_CENSUS', out, su, flush=True)
    if su['goal_met']:
        raise ExactGoalCandidateFound('Exact contact-event hull Figure: '+str(out))
    return r


if __name__ == '__main__':
    p = argparse.ArgumentParser()
    p.add_argument('source')
    p.add_argument('params')
    p.add_argument('out')
    p.add_argument('--grid', type=int)
    a = p.parse_args()
    run(a.source, a.params, a.out, a.grid)
