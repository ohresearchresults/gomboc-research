# material-4af35c279491

AI research material

---

#!/usr/bin/env python3
"""Exact volume/centroid Jacobians for support translations and face pivots.
Python >= 3.10, standard library only. All geometry is rational.
Run: python face_pivot.py --self-test
Input API: analyse(vertices, faces, normals=None).
Faces must be the true outward-oriented convex polygonal facets, not triangles
inserted inside a coplanar facet. No polyhedron recovery data are implicit.
"""
from fractions import Fraction as F
from itertools import combinations
import json
import sys


def vec(a):
    return tuple(F(x) for x in a)


def add(a, b):
    return tuple(x + y for x, y in zip(a, b))


def sub(a, b):
    return tuple(x - y for x, y in zip(a, b))


def scale(s, a):
    return tuple(s * x for x in a)


def dot(a, b):
    return sum((x * y for x, y in zip(a, b)), F(0))


def cross(a, b):
    return (a[1]*b[2]-a[2]*b[1], a[2]*b[0]-a[0]*b[2], a[0]*b[1]-a[1]*b[0])


def outer(a, b):
    return [[x*y for y in b] for x in a]


def mv(a, x):
    return tuple(dot(row, x) for row in a)


def rank(a):
    a = [list(map(F, row)) for row in a]
    if not a:
        return 0
    m, n, r = len(a), len(a[0]), 0
    for j in range(n):
        p = next((i for i in range(r, m) if a[i][j]), None)
        if p is None:
            continue
        a[r], a[p] = a[p], a[r]
        s = a[r][j]
        a[r] = [v/s for v in a[r]]
        for i in range(m):
            if i != r and a[i][j]:
                s = a[i][j]
                a[i] = [u-s*v for u, v in zip(a[i], a[r])]
        r += 1
        if r == m:
            break
    return r


def nullspace(a, ncols=None):
    a = [list(map(F, row)) for row in a]
    if not a:
        if ncols is None:
            raise ValueError('ncols required for an empty matrix')
        return [tuple(F(i == j) for i in range(ncols)) for j in range(ncols)]
    m, n, r, piv = len(a), len(a[0]), 0, []
    for j in range(n):
        p = next((i for i in range(r, m) if a[i][j]), None)
        if p is None:
            continue
        a[r], a[p] = a[p], a[r]
        s = a[r][j]
        a[r] = [v/s for v in a[r]]
        for i in range(m):
            if i != r and a[i][j]:
                s = a[i][j]
                a[i] = [u-s*v for u, v in zip(a[i], a[r])]
        piv.append(j)
        r += 1
        if r == m:
            break
    answer = []
    for j in range(n):
        if j in piv:
            continue
        z = [F(0)] * n
        z[j] = F(1)
        for i, p in enumerate(piv):
            z[p] = -a[i][j]
        answer.append(tuple(z))
    return answer


def solve_square(a, b):
    n = len(a)
    if len(b) != n or any(len(row) != n for row in a):
        raise ValueError('square system required')
    c = [list(map(F, row)) + [F(y)] for row, y in zip(a, b)]
    for j in range(n):
        p = next((i for i in range(j, n) if c[i][j]), None)
        if p is None:
            raise ValueError('singular system')
        c[j], c[p] = c[p], c[j]
        s = c[j][j]
        c[j] = [v/s for v in c[j]]
        for i in range(n):
            if i != j:
                s = c[i][j]
                c[i] = [u-s*v for u, v in zip(c[i], c[j])]
    return tuple(row[-1] for row in c)


def analyse(vertices, faces, normals=None):
    """Validate exact true-facet input; return exact moments and Jacobians."""
    x = [vec(v) for v in vertices]
    if len(set(x)) != len(x):
        raise ValueError('duplicate vertices')
    if normals is not None and len(normals) != len(faces):
        raise ValueError('normal count mismatch')
    data, edges, used, volume6 = [], {}, set(), F(0)
    moment24 = [F(0)] * 3
    for fi, face0 in enumerate(faces):
        face = list(face0)
        if len(face) < 3 or len(set(face)) != len(face):
            raise ValueError('invalid polygon')
        p = [x[j] for j in face]
        n = vec(normals[fi]) if normals is not None else cross(sub(p[1], p[0]), sub(p[2], p[0]))
        nn, h = dot(n, n), dot(n, p[0])
        if not nn or any(dot(n, q) != h for q in p):
            raise ValueError('zero normal or nonplanar face')
        if {j for j, q in enumerate(x) if dot(n, q) == h} != set(face):
            raise ValueError('face not a complete true facet')
        if any(dot(n, q) > h for q in x):
            raise ValueError('inward normal or nonconvex input')
        for j in range(len(p)):
            edge = sub(p[(j+1) % len(p)], p[j])
            for k, q in enumerate(p):
                if k not in (j, (j+1) % len(p)) and dot(n, cross(edge, sub(q, p[j]))) <= 0:
                    raise ValueError('face is not a strictly convex outward polygon')
            a, b = face[j], face[(j+1) % len(face)]
            edges.setdefault(tuple(sorted((a, b))), []).append((a, b))
        used.update(face)
        weight = F(0)
        cm = [F(0)] * 3
        qm = [[F(0)] * 3 for _ in range(3)]
        a = p[0]
        for j in range(1, len(p)-1):
            b, c = p[j], p[j+1]
            tw = dot(n, cross(sub(b, a), sub(c, a))) / (2*nn)
            if tw <= 0:
                raise ValueError('nonpositive fan triangle')
            weight += tw
            s = add(add(a, b), c)
            for k in range(3):
                cm[k] += tw * s[k] / 3
                for l in range(3):
                    qm[k][l] += tw * (s[k]*s[l] + a[k]*a[l] + b[k]*b[l] + c[k]*c[l]) / 12
            det = dot(a, cross(b, c))
            volume6 += det
            for k in range(3):
                moment24[k] += det * s[k]
        centroid = tuple(v/weight for v in cm)
        second = [[v/weight for v in row] for row in qm]
        covariance = [[second[k][l]-centroid[k]*centroid[l] for l in range(3)] for k in range(3)]
        if rank(covariance) != 2 or any(mv(covariance, n)):
            raise AssertionError('face covariance identity failed')
        data.append(dict(vertices=face, n=n, h=h, w=weight, c=centroid, Q=second, Sigma=covariance))
    if used != set(range(len(x))):
        raise ValueError('unused vertex')
    for pair in edges.values():
        if len(pair) != 2 or pair[0] != pair[1][::-1]:
            raise ValueError('boundary not an oriented closed manifold')
    if len(x)-len(edges)+len(data) != 2 or volume6 <= 0:
        raise ValueError('Euler/volume validation failed')
    volume = volume6 / 6
    centroid = tuple(v/(24*volume) for v in moment24)
    B = [[f['w']*(f['c'][k]-centroid[k])/volume for f in data] for k in range(3)]
    for k in range(3):
        for l in range(3):
            assert sum(B[k][i]*f['n'][l] for i, f in enumerate(data)) == F(k == l)
        assert sum(B[k][i]*f['h'] for i, f in enumerate(data)) == centroid[k]
    return dict(x=x, faces=data, V=volume, g=centroid, B=B, E=len(edges))


def derivative(body, dh, dn=None):
    """Full physical derivative under n_i(t)=n_i+t dn_i, h_i(t)=h_i+t dh_i."""
    if len(dh) != len(body['faces']):
        raise ValueError('dh length mismatch')
    dn = [vec((0, 0, 0)) for _ in dh] if dn is None else [vec(v) for v in dn]
    if len(dn) != len(dh):
        raise ValueError('dn length mismatch')
    dV, dg = F(0), [F(0)]*3
    for face, hi, ni in zip(body['faces'], dh, dn):
        offset = F(hi)-dot(ni, face['c'])
        dV += face['w']*offset
        covterm = mv(face['Sigma'], ni)
        for k in range(3):
            dg[k] += face['w']*((face['c'][k]-body['g'][k])*offset-covterm[k])/body['V']
    return dV, tuple(dg)


def pivot_modes(body, selected):
    """Two tangent normal modes per selected true facet; dh=c_i dot dn_i."""
    modes = []
    nf = len(body['faces'])
    for i in selected:
        face = body['faces'][i]
        for tangent in nullspace([face['n']]):
            dh = [F(0)]*nf
            dn = [vec((0, 0, 0)) for _ in range(nf)]
            dh[i], dn[i] = dot(face['c'], tangent), tangent
            dV, dg = derivative(body, dh, dn)
            assert dV == 0
            modes.append(dict(face=i, dh=dh, dn=dn, dg=dg))
    return modes


def incidence_constraints(body, modes):
    """K z=0 preserves every original vertex/support incidence to first order.
    Necessary, not sufficient, for a finite continuation of a nonsimple contact.
    """
    out = []
    for vi, x in enumerate(body['x']):
        incident = [i for i, f in enumerate(body['faces']) if vi in f['vertices']]
        base = next((a for a in combinations(incident, 3) if rank([body['faces'][i]['n'] for i in a]) == 3), None)
        if base is None:
            raise ValueError('vertex has no independent triple')
        A = [body['faces'][i]['n'] for i in base]
        dx = [solve_square(A, [mode['dh'][i]-dot(mode['dn'][i], x) for i in base]) for mode in modes]
        for i in incident:
            if i in base:
                continue
            row = [dot(body['faces'][i]['n'], v)-mode['dh'][i]+dot(mode['dn'][i], x) for v, mode in zip(dx, modes)]
            if any(row):
                out.append(row)
    return out


def steering_rank(body, selected):
    modes = pivot_modes(body, selected)
    D = [[m['dg'][k] for m in modes] for k in range(3)]
    K = incidence_constraints(body, modes)
    Z = nullspace(K, ncols=len(modes))
    DZ = [[dot(row, z) for z in Z] for row in D]
    return dict(raw_rank=rank(D), incidence_rows=len(K), allowed_dimension=len(Z), incidence_preserving_rank=rank(DZ))


def tetra_vertices(normals, offsets):
    if len(normals) != 4:
        raise ValueError('four support planes required')
    return [solve_square([normals[j] for j in range(4) if j != i], [offsets[j] for j in range(4) if j != i]) for i in range(4)]


def self_test():
    vertices = [(0,0,0), (1,0,0), (0,1,0), (0,0,1)]
    faces = [(0,2,1), (0,1,3), (0,3,2), (1,2,3)]
    t = analyse(vertices, faces)
    assert t['V'] == F(1,6) and t['g'] == vec((F(1,4),)*3)
    assert steering_rank(t, [0,1])['incidence_preserving_rank'] == 3
    # Independent exact derivative check: differentiate each moving tetrahedron
    # vertex from its three planes, then average the four velocities.
    for m in pivot_modes(t, [0,1,2,3]):
        independent = []
        for vi, x in enumerate(t['x']):
            ix = [i for i, f in enumerate(t['faces']) if vi in f['vertices']]
            independent.append(solve_square([t['faces'][i]['n'] for i in ix], [m['dh'][i]-dot(m['dn'][i], x) for i in ix]))
        check = tuple(sum(z[k] for z in independent)/4 for k in range(3))
        assert check == m['dg']
    cube_v = [(0,0,0),(1,0,0),(1,1,0),(0,1,0),(0,0,1),(1,0,1),(1,1,1),(0,1,1)]
    cube_f = [(0,3,2,1),(4,5,6,7),(0,1,5,4),(1,2,6,5),(2,3,7,6),(3,0,4,7)]
    c = analyse(cube_v, cube_f)
    assert c['V'] == 1 and c['g'] == vec((F(1,2),)*3)
    assert steering_rank(c,[0,1])['raw_rank'] == 2
    assert steering_rank(c,[0,2])['incidence_preserving_rank'] == 3
    # Octahedron: degree-four vertices exercise the nonsimple-incidence filter.
    ov = [(1,0,0),(-1,0,0),(0,1,0),(0,-1,0),(0,0,1),(0,0,-1)]
    of = []
    for a in (0,1):
        for b in (2,3):
            for cc in (4,5):
                f = (a,b,cc)
                p = [vec(ov[i]) for i in f]
                if dot(cross(sub(p[1],p[0]), sub(p[2],p[0])), p[0]) < 0:
                    f = (a,cc,b)
                of.append(f)
    o = analyse(ov, of)
    pair = next((a,b) for a,b in combinations(range(len(of)),2) if any(cross(o['faces'][a]['n'],o['faces'][b]['n'])))
    os = steering_rank(o,pair)
    assert os['raw_rank'] == 3 and os['incidence_preserving_rank'] < 3
    print(json.dumps({'tetra':steering_rank(t,[0,1]), 'cube_parallel':steering_rank(c,[0,1]), 'cube_nonparallel':steering_rank(c,[0,2]), 'octa_pair':list(pair), 'octa_nonsimple':os},sort_keys=True,separators=(',',':')))
    print('FACE_PIVOT_EXACT_SELFTEST_PASS')


if __name__ == '__main__':
    if sys.argv[1:] != ['--self-test']:
        raise SystemExit('usage: python face_pivot.py --self-test')
    self_test()
