# material-74ae7e92d020

AI research material

---

"""PROJECTIVE_CENTROID_KERNEL_AND_AXIAL_PHASE_V1.
Exact rational controls for the analytic theorems in the companion proof.
CPython 3.13.5; standard library only; assertions enabled; no RNG/network.
Usage: python projective_kernel.py build|check
The generic hull routine accepts only distinct genuine vertices with 0 inside.
"""
from fractions import Fraction as Q
from itertools import combinations, product
from pathlib import Path
import hashlib
import json
import sys

assert __debug__
Z = (Q(0),) * 3
I = tuple(tuple(Q(i == j) for j in range(3)) for i in range(3))

def v(a): return tuple(map(Q, a))
def add(a, b): return tuple(x+y for x, y in zip(a, b))
def sub(a, b): return tuple(x-y for x, y in zip(a, b))
def scale(c, a): return tuple(c*x for x in a)
def dot(a, b): return sum((x*y for x, y in zip(a, b)), Q(0))
def cross(a, b): return (a[1]*b[2]-a[2]*b[1], a[2]*b[0]-a[0]*b[2], a[0]*b[1]-a[1]*b[0])
def det(a): return dot(a[0], cross(a[1], a[2]))
def mv(a, b): return tuple(dot(row, b) for row in a)
def gram(x, a, y): return dot(x, mv(a, y))
def diag(a, b, c): return ((Q(a), Q(0), Q(0)), (Q(0), Q(b), Q(0)), (Q(0), Q(0), Q(c)))
def solve(a, b):
    d = det(a)
    if not d: return None
    return tuple(sum((b[j]*cross(a[(j+1)%3], a[(j+2)%3])[i] for j in range(3)), Q(0))/d for i in range(3))
def inverse(a):
    cols = [solve(a, I[j]) for j in range(3)]
    assert all(c is not None for c in cols)
    return tuple(tuple(cols[j][i] for j in range(3)) for i in range(3))
def spd(a):
    return all(a[i][j] == a[j][i] for i in range(3) for j in range(3)) and a[0][0] > 0 and a[0][0]*a[1][1]-a[0][1]**2 > 0 and det(a) > 0

def hull(xs):
    """Exact maximal facets, true edges, outward triangulation, positive poles."""
    n = len(xs)
    assert len(set(xs)) == n and n >= 4
    faces = {}
    for ii in combinations(range(n), 3):
        x, y, z = (xs[i] for i in ii)
        normal = cross(sub(y, x), sub(z, x))
        if normal == Z: continue
        h = dot(normal, x)
        vals = [dot(normal, sub(t, x)) for t in xs]
        if min(vals) < 0 < max(vals): continue
        if max(vals) == 0:
            pass
        else:
            normal, h, vals = scale(-1, normal), -h, [-t for t in vals]
        assert h > 0, 'origin must be strictly interior'
        q = scale(1/h, normal)
        f = tuple(i for i, t in enumerate(vals) if t == 0)
        assert all(dot(q, t) <= 1 for t in xs)
        if f in faces: assert faces[f] == q
        faces[f] = q
    fs = sorted(faces)
    poles = [faces[f] for f in fs]
    for i in range(n):
        incident = [poles[j] for j, f in enumerate(fs) if i in f]
        assert any(det(a) != 0 for a in combinations(incident, 3)), 'nonextreme input'
    edges = {}
    for f, h in combinations(range(len(fs)), 2):
        inter = tuple(sorted(set(fs[f]).intersection(fs[h])))
        if len(inter) < 2: continue
        assert len(inter) == 2, 'nonextreme collinear input'
        assert inter not in edges
        edges[inter] = (f, h)
    edges = dict(sorted(edges.items()))
    assert n-len(edges)+len(fs) == 2
    triangles = []
    for fi, f in enumerate(fs):
        adj = {i: [] for i in f}
        for (i, j), ff in edges.items():
            if fi in ff:
                adj[i].append(j); adj[j].append(i)
        assert all(len(a) == 2 for a in adj.values())
        a = min(f); order = [a, min(adj[a])]
        while True:
            nxt = [j for j in adj[order[-1]] if j != order[-2]][0]
            if nxt == a: break
            assert nxt not in order
            order.append(nxt)
        assert set(order) == set(f)
        if det([xs[order[j]] for j in range(3)]) < 0:
            order = [order[0]] + order[:0:-1]
        for j in range(1, len(order)-1):
            tr = (order[0], order[j], order[j+1])
            assert det([xs[i] for i in tr]) > 0
            triangles.append(tr)
    return fs, edges, triangles, poles

def mass(xs, triangles, apex=Z):
    volume = Q(0); moment = Z; weights = []
    for tr in triangles:
        a, b, c = (xs[i] for i in tr)
        d = det([sub(a, apex), sub(b, apex), sub(c, apex)])
        assert d >= 0
        volume += d/6
        moment = add(moment, scale(d/24, add(add(a, b), add(c, apex))))
        weights.append(d)
    assert volume > 0
    return volume, moment, weights

def affine_rows(xs, poles, edges, m=I):
    assert spd(m)
    ni = inverse(m); rows = []
    for (i, j), (f, h) in edges.items():
        for a, b in ((i, j), (j, i)):
            x, y = xs[a], xs[b]
            xx, xy = gram(x, m, x), gram(x, m, y)
            rows.append(('A', a, b, xy-xx, sub(scale(xy, x), scale(xx, y))))
        for a, b in ((f, h), (h, f)):
            d = sub(poles[b], poles[a])
            rows.append(('B', a, b, gram(poles[a], ni, d), mv(ni, d)))
    return rows

def mechanics(xs, poles, edges, m=I):
    rows = affine_rows(xs, poles, edges, m)
    pv = [[] for _ in xs]; pf = [[] for _ in poles]
    saddles = []; weak = []; zeros = 0
    for ei, ((i, j), (f, h)) in enumerate(edges.items()):
        values = [row[3] for row in rows[4*ei:4*ei+4]]
        pv[i].append(values[0]); pv[j].append(values[1])
        pf[f].append(values[2]); pf[h].append(values[3])
        zeros += values.count(0)
        if max(values) < 0: saddles.append((i, j))
        elif max(values) == 0:
            weak.append(((i, j), ['A' if k < 2 else 'B' for k, z in enumerate(values) if z == 0]))
    stable = [i for i, r in enumerate(pf) if max(r) < 0]
    unstable = [i for i, r in enumerate(pv) if max(r) < 0]
    return {'S': stable, 'U': unstable, 'H': saddles, 'weak': weak, 'zero_primitives': zeros,
            'census': [len(stable), len(unstable), len(saddles), len(weak)],
            'rows': rows}

def kernel(xs, poles):
    tau = [max(1-dot(q, x) for q in poles)/4 for x in xs]
    assert all(t > Q(1, 4) for t in tau)
    rhs = [t-1 for t in tau]; verts = set()
    for ii in combinations(range(len(xs)), 3):
        p = solve([xs[i] for i in ii], [rhs[i] for i in ii])
        if p is not None and all(dot(x, p) >= r for x, r in zip(xs, rhs)):
            verts.add(p)
    assert verts
    verts = sorted(verts)
    assert all(1+dot(x, p) > Q(1, 4) for p in verts for x in xs)
    return tau, verts

def bounds(rows, verts):
    return [(min(a+dot(b, p) for p in verts), max(a+dot(b, p) for p in verts)) for _, _, _, a, b in rows]

def project(xs, p):
    f = [1+dot(p, x) for x in xs]
    assert min(f) > 0
    return [scale(1/t, x) for x, t in zip(xs, f)]

def record(xs, m=I):
    fs, es, tr, qs = hull(xs)
    vol, mom, w0 = mass(xs, tr)
    vol1, mom1, w1 = mass(xs, tr, xs[0])
    assert (vol, mom) == (vol1, mom1)
    mech = mechanics(xs, qs, es, m)
    return {'vertices': xs, 'facets': fs, 'edges': list(es.items()), 'triangles': tr,
            'poles': qs, 'volume': vol, 'first_moment': mom, 'centroid': scale(1/vol, mom),
            'two_positive_fans': [w0, w1], 'metric': m, 'mechanics': mech}, (fs, es, tr, qs)

def box(a): return list(product((-Q(1), Q(a)), (-Q(1), Q(1)), (-Q(1), Q(1))))
def axial(k):
    k = Q(k); r = 1+k+k*k; q = 1+2*k+3*k*k
    return (3+2*k+k*k)/(k*q), (1-k)*q/(4*r)

def phase(a, t, m):
    s = 2+4*(-m < t < a*m)
    u = 4*(t > -m/2)+4*(t < a*m/2)
    h = 4*((-m/2 < t < a*m/2)+(t > -m)+(t < a*m))
    weak = 4*(t in (-m/2, a*m/2, -m, a*m))
    return [s, u, h, weak]

def mulpoly(a, b):
    out = [Q(0)]*(len(a)+len(b)-1)
    for i, x in enumerate(a):
        for j, y in enumerate(b): out[i+j] += x*y
    return out

def subpoly(a, b):
    out = [Q(0)]*max(len(a), len(b))
    for i, x in enumerate(a): out[i] += x
    for i, x in enumerate(b): out[i] -= x
    while len(out) > 1 and not out[-1]: out.pop()
    return out

def dpoly(a): return [i*a[i] for i in range(1, len(a))]

def build():
    report = {'identity': 'PROJECTIVE_CENTROID_KERNEL_AND_AXIAL_PHASE_V1', 'scope':
              'Actual uniform refilling, own centroid, exact true facets/edges and reciprocal metrics. Analytic universal claims are in companion proof; controls alone are not exclusions.'}
    raw = []
    for a in (Q(1), Q(3, 2), Q(2), Q(10)):
        xs = box(a); rec, (_, es, tr, qs) = record(xs)
        tau, vs = kernel(xs, qs); rows = affine_rows(xs, qs, es)
        bb = bounds(rows, vs)
        lo, hi = (a-3)/(4*a), Q(1, 2)
        axial_bounds = bounds(rows, [(lo, Q(0), Q(0)), (hi, Q(0), Q(0))])
        assert len(vs) == 6 and all(b <= 0 for _, b in axial_bounds)
        if a == 1: assert all(b <= 0 for _, b in bb)
        else: assert sum(b > 0 for row, (_, b) in zip(rows, bb) if row[0] == 'A') == 8
        raw.append({'a': a, 'original': rec, 'tau': tau, 'kernel_vertices': vs,
                    'all_row_kernel_bounds': bb, 'symmetry_axis_interval': [lo, hi],
                    'all_row_axis_bounds': axial_bounds})
    report['global_and_symmetry_kernel_controls'] = raw
    centered = []
    for k in (Q(1, 100), Q(1, 2), Q(1), Q(2), Q(100)):
        a, t = axial(k); xs = box(a); yy = project(xs, (t, Q(0), Q(0)))
        fs, es, tr, qs = hull(xs)
        fy, ey, ty, qy = hull(yy)
        assert fs == fy and es == ey
        assert qy == [add(q, (t, Q(0), Q(0))) for q in qs]
        vol, mom, _ = mass(yy, ty)
        assert mom == Z
        tau, kv = kernel(xs, qs)
        assert all(1+t*x[0] > tt for x, tt in zip(xs, tau))
        if t == 0: ms = [Q(1), Q(1, 10)]
        elif t > 0:
            w = t/a; ms = [w/2, w, 3*w/2, 2*w, 3*w, Q(1)]
        else:
            w = -t; ms = [w/2, w, 3*w/2, 2*w, 3*w, Q(1)]
        tests = []
        for m in sorted(set(ms)):
            mm = diag(m, 1, 1)
            rec, _ = record(yy, mm)
            assert rec['first_moment'] == Z
            assert rec['mechanics']['census'] == phase(a, t, m)
            affine = affine_rows(xs, qs, es, mm)
            exact = rec['mechanics']['rows']
            ff = [1+t*x[0] for x in xs]
            for r, e in zip(affine, exact):
                kind, i, j, aa, b = r
                predicted = aa+t*b[0]
                if kind == 'A': predicted /= ff[i]**2*ff[j]
                assert predicted == e[3]
            tests.append(rec)
        centered.append({'k': k, 'a': a, 't': t, 'volume': vol, 'metric_tests': tests})
    report['exact_rational_centering_and_full_axial_phase'] = centered
    # Exact identities on the whole positive rational-parameter curve.
    pp = list(map(Q, (3, 2, 1))); qq = list(map(Q, (0, 1, 2, 3)))
    derivative = subpoly(mulpoly(dpoly(pp), qq), mulpoly(pp, dpoly(qq)))
    assert derivative == list(map(Q, (-3, -12, -30, -12, -3)))
    report['a_derivative_numerator'] = derivative
    # Sharpness and the simplex exception: P is exactly a singleton.
    simplexes = []
    for eps in (Q(1), Q(1, 10), Q(1, 100)):
        xs = [v((-1, 0, 0)), v((0, -1, 0)), v((0, 0, -1)), (eps, eps, eps)]
        _, es, tr, qs = hull(xs); tau, vs = kernel(xs, qs)
        t = (eps-1)/(4*eps); p = (t, t, t)
        assert vs == [p]
        yy = project(xs, p); rec, _ = record(yy)
        assert rec['first_moment'] == Z and rec['mechanics']['census'] == [4, 4, 6, 0]
        assert 1+dot(p, xs[3]) == (1+3*eps)/4
        simplexes.append({'eps': eps, 'original_vertices': xs, 'tau': tau, 'kernel_vertices': vs, 'actual_centered': rec})
    report['sharp_three_quarters_simplexes'] = simplexes
    # A non-tetrahedral pyramid: centered p is on P boundary, but physical weak
    # rows still strictly cross P; an arbitrary affine function need not do so.
    pyramid = [v(a) for a in [(-1,-1,-1),(-1,1,-1),(1,-1,-1),(1,1,-1),(0,0,3)]]
    pm = ((Q(8),Q(0),Q(13,5)),(Q(0),Q(1),Q(0)),(Q(13,5),Q(0),Q(1)))
    rec, (_, es, _, qs) = record(pyramid, pm)
    assert rec['first_moment'] == Z
    tau, kv = kernel(pyramid, qs); rr = rec['mechanics']['rows']; bb = bounds(rr, kv)
    assert sum(t == 1 for t in tau) == 1 and tau[4] == 1
    assert min(p[2] for p in kv) == 0 < max(p[2] for p in kv)
    physical_zero_indices = []
    for ei, edge in enumerate(es):
        packet = rr[4*ei:4*ei+4]
        if max(row[3] for row in packet) == 0:
            for j, row in enumerate(packet):
                if row[3] == 0: physical_zero_indices.append(4*ei+j)
    assert physical_zero_indices
    assert all(lo < 0 < hi for row, (lo,hi) in zip(rr, bb) if row[3] == 0)
    axis_bounds = bounds(rr, [Z, (Q(0), Q(0), Q(1,3))])
    assert all(axis_bounds[i][0] < 0 == axis_bounds[i][1] for i in physical_zero_indices)
    report['pyramid_boundary_weak_row_straddling'] = {'actual': rec, 'tau': tau, 'kernel_vertices': kv,
          'row_bounds': bb, 'physical_zero_indices': physical_zero_indices,
          'symmetry_axis_countercontrol': {'interval': [Q(0), Q(1,3)], 'row_bounds': axis_bounds},
          'generic_affine_countercontrol': {'h': '3*p_z', 'min': Q(0), 'max': 3*max(p[2] for p in kv)}}
    # Tetrahedron: a physical weak row can vanish on its singleton P. It cannot
    # be promoted to strict sign from a non-strict kernel inequality.
    xs = [v((-1,0,0)),v((0,-1,0)),v((0,0,-1)),v((1,1,1))]
    sm = tuple(v(r) for r in [(1,-1,-1),(-1,3,0),(-1,0,3)])
    rec, (_, es, _, qs) = record(xs, sm); tau, kv = kernel(xs, qs)
    assert rec['first_moment'] == Z and kv == [Z]
    assert rec['mechanics']['weak']
    zz = [i for i, r in enumerate(rec['mechanics']['rows']) if r[3] == 0]
    assert zz and all(bounds(rec['mechanics']['rows'], kv)[i] == (0,0) for i in zz)
    report['tetrahedron_essential_exception'] = {'actual': rec, 'kernel_vertices': kv, 'zero_rows': zz}
    return report

def encode(obj):
    if isinstance(obj, Q): return str(obj)
    if isinstance(obj, dict): return {str(k): encode(v) for k, v in obj.items()}
    if isinstance(obj, (list, tuple)): return [encode(v) for v in obj]
    return obj

def main():
    assert sys.argv[1:] in (['build'], ['check'])
    obj = build()
    data = (json.dumps(encode(obj), sort_keys=True, separators=(',', ':'))+'\n').encode('utf-8')
    path = Path('projective_kernel.json')
    if sys.argv[1] == 'build': path.write_bytes(data)
    else: assert path.read_bytes() == data
    for marker in ('EXACT_HULL_TWO_POSITIVE_FANS_AND_RECIPROCAL_MECHANICS_PASS',
                   'GLOBAL_CENTROID_KERNEL_AND_SYMMETRY_AXIS_CERTIFICATES_PASS',
                   'RATIONAL_ACTUAL_CENTERING_AND_ALL_FOUR_AXIAL_WALL_TYPES_PASS',
                   'SHARP_THREE_QUARTERS_AND_TETRAHEDRON_EXCEPTION_PASS',
                   'PYRAMID_PHYSICAL_WEAK_WALL_STRADDLES_KERNEL_PASS'):
        print(marker)
    print(path.name, len(data), hashlib.sha256(data).hexdigest())
    print('PROJECTIVE_CENTROID_KERNEL_AND_AXIAL_PHASE_RECOVERY_PASS')

if __name__ == '__main__': main()
