from fractions import Fraction as F
from pathlib import Path
from itertools import combinations
from math import gcd, lcm
import argparse, hashlib, importlib, json, sys

sys.set_int_max_str_digits(0)
assert __debug__, 'Do not use Python -O'


def encode(obj):
    return json.dumps(obj, sort_keys=True, separators=(',', ':'),
                      default=str).encode('utf-8')


def digest(data):
    return hashlib.sha256(data).hexdigest()


def save(path, obj):
    data = encode(obj)
    path.write_bytes(data)
    return {'bytes': len(data), 'sha256': digest(data)}


def dot(a, b):
    return sum(x*y for x, y in zip(a, b))


def add(a, b):
    return [x+y for x, y in zip(a, b)]


def sub(a, b):
    return [x-y for x, y in zip(a, b)]


def scale(s, a):
    return [s*x for x in a]


def cross(a, b):
    return [a[1]*b[2]-a[2]*b[1],
            a[2]*b[0]-a[0]*b[2],
            a[0]*b[1]-a[1]*b[0]]


def det(a, b, c):
    return dot(a, cross(b, c))


def solve(rows, rhs):
    n = len(rows)
    assert len(rhs) == n and all(len(r) == n for r in rows)
    A = [[F(v) for v in r] + [F(h)] for r, h in zip(rows, rhs)]
    for k in range(n):
        pivot = next((i for i in range(k, n) if A[i][k]), None)
        if pivot is None:
            raise ArithmeticError('Singular rational solve')
        A[k], A[pivot] = A[pivot], A[k]
        a = A[k][k]
        A[k] = [v/a for v in A[k]]
        for i in range(n):
            if i != k:
                a = A[i][k]
                A[i] = [x-a*y for x, y in zip(A[i], A[k])]
    return [r[-1] for r in A]


def plane(a, b, c):
    n = cross(sub(b, a), sub(c, a))
    return n, dot(n, a)


def primitive(n, h):
    assert h > 0
    vals = list(n) + [h]
    D = lcm(*(v.denominator for v in vals))
    row = [int(D*v) for v in vals]
    G = gcd(*row)
    return [v//G for v in row]


def edges(faces):
    result = {}
    for f, cy in enumerate(faces):
        for a, b in zip(cy, cy[1:] + cy[:1]):
            result.setdefault(tuple(sorted((a, b))), []).append(f)
    assert all(len(v) == 2 for v in result.values())
    return result


def owners(faces):
    n = 1 + max(max(cy) for cy in faces)
    return [[f for f, cy in enumerate(faces) if i in cy]
            for i in range(n)]


def mass(P, faces):
    D = F(0)
    L = [F(0)]*3
    for cy in faces:
        for j in range(1, len(cy)-1):
            a, b, c = [P[i] for i in (cy[0], cy[j], cy[j+1])]
            dd = det(a, b, c)
            assert dd > 0
            D += dd
            L = add(L, scale(dd, add(add(a, b), c)))
    assert D > 0
    return D/6, scale(F(1, 24), L)


def load_parent(root):
    manifest = json.loads((root/'MANIFEST.json').read_bytes())
    for name, spec in manifest.items():
        data = (root/name).read_bytes()
        assert len(data) == spec['bytes']
        assert digest(data) == spec['sha256']
    data = (root/'PARENT_S8.json').read_bytes()
    assert len(data) == 9599
    assert digest(data) == (
        'bf9fdaf05231ceb11fba9fde10c8a638e664b52233b2da5cb11977b2f4ff27b2')
    d = json.loads(data)
    faces = json.loads((root/'FACES_S8.json').read_bytes())
    n = d['n_supports']
    assert n == 137
    den = d.get('denominators', [d['grid']]*len(d['controls']))
    X = [[F(v, D) for v in row] for row, D in zip(d['controls'], den)]
    X[n] = [F(0), F(0), F(1)]
    seen = {n}
    for i, deps, axes in d['plan']:
        assert i not in seen and all(j in seen for j in deps)
        assert len(deps) == len(axes)
        free = [k for k in range(3) if k not in axes]
        if deps:
            rows = [[X[j][k] for k in axes] for j in deps]
            rhs = [1-sum(X[j][k]*X[i][k] for k in free) for j in deps]
            for k, v in zip(axes, solve(rows, rhs)):
                X[i][k] = v
        seen.add(i)
    assert seen == set(range(len(X)))
    assert len(X) == n + len(d['groups'])
    for i, group in enumerate(d['groups']):
        assert all(dot(X[f], X[n+i]) == 1 for f in group)
    q = X[:n]
    own = owners(faces)
    P = []
    for oo in own:
        p = None
        for tri in combinations(oo, 3):
            try:
                p = solve([q[f] for f in tri], [F(1)]*3)
                break
            except ArithmeticError:
                pass
        assert p is not None
        assert all(dot(q[f], p) == 1 for f in oo)
        assert all(dot(q[f], p) < 1 for f in range(n) if f not in oo)
        P.append(p)
    assert P == sorted(P), 'Do not silently reinterpret physical labels'
    ee = edges(faces)
    assert (len(P), len(ee), len(faces)) == (177, 312, 137)
    V, M = mass(P, faces)
    return P, q, faces, V, M


def star(P, faces, i):
    ee = edges(faces)
    oo = owners(faces)[i]
    tri = [f for f in oo if len(faces[f]) == 3]
    large = [f for f in oo if len(faces[f]) > 3]
    neigh = sorted({b if a == i else a for a, b in ee if i in (a, b)})
    assert len(neigh) == 3 and len(tri) == 2 and len(large) == 1
    cy = faces[large[0]]
    k = cy.index(i)
    a, b = cy[k-1], cy[(k+1) % len(cy)]
    c = next(v for v in neigh if v not in (a, b))
    direction = sub(P[b], P[a])
    w = abs(det(sub(P[a], P[c]), sub(P[i], P[c]), sub(P[b], P[c])))/6
    assert w > 0
    K = scale(w/4, direction)
    lower, upper = None, None

    def constrain(alpha, beta):
        nonlocal lower, upper
        assert alpha >= 0
        if beta > 0:
            bound = -alpha/beta
            lower = bound if lower is None else max(lower, bound)
        elif beta < 0:
            bound = -alpha/beta
            upper = bound if upper is None else min(upper, bound)

    for f, fc in enumerate(faces):
        n0, h0 = plane(*(P[j] for j in fc[:3]))
        assert h0 > 0
        dn, dh = [F(0)]*3, F(0)
        if f in tri:
            test = [add(P[j], direction) if j == i else P[j] for j in fc]
            n1, h1 = plane(*test)
            dn, dh = sub(n1, n0), h1-h0
        constrain(h0, dh)
        for j, p in enumerate(P):
            dp = direction if j == i else [F(0)]*3
            assert dot(dn, dp) == 0
            constrain(h0-dot(n0, p), dh-dot(dn, p)-dot(n0, dp))
    assert lower is not None and upper is not None
    assert lower < 0 < upper
    return {'vertex': i, 'a': a, 'b': b, 'c': c,
            'triangles': tri, 'nontriangle': large[0],
            'direction': direction, 'w': w, 'K': K,
            'interval': [lower, upper]}


def eligible(P, faces):
    result = {}
    for i in range(len(P)):
        try:
            result[i] = star(P, faces, i)
        except AssertionError:
            pass
    return result


def pa(a, b):
    r = dict(a)
    for k, v in b.items():
        r[k] = r.get(k, F(0)) + v
        if not r[k]:
            del r[k]
    return r


def ps(a, s):
    return {k: s*v for k, v in a.items() if s*v}


def pm(a, b):
    r = {}
    for i, x in a.items():
        for j, y in b.items():
            k = tuple(sorted(i+j))
            r[k] = r.get(k, F(0)) + x*y
    return {k: v for k, v in r.items() if v}


def pc(x):
    return {(): F(x)} if x else {}


def pdet(a, b, c):
    result = {}
    for i, j, k in [(0,1,2), (1,2,0), (2,0,1)]:
        result = pa(result, pm(a[i], pm(b[j], c[k])))
        result = pa(result, ps(pm(a[i], pm(b[k], c[j])), -1))
    return result


def peval(p, t):
    result = F(0)
    for key, value in p.items():
        for i in key:
            value *= t.get(i, F(0))
        result += value
    return result


def moments_polynomial(P, faces, stars):
    X = []
    for i, p in enumerate(P):
        row = [pc(v) for v in p]
        if i in stars:
            for k in range(3):
                row[k] = pa(row[k], {(i,): stars[i]['direction'][k]})
        X.append(row)
    VP, MP = {}, [{}, {}, {}]
    for cy in faces:
        if len(cy) == 3:
            triangles = [[X[i] for i in cy]]
        else:
            centre = [sum(P[i][k] for i in cy)/len(cy) for k in range(3)]
            fixed = [pc(v) for v in centre]
            triangles = [[fixed, X[i], X[j]]
                         for i, j in zip(cy, cy[1:]+cy[:1])]
        for a, b, c in triangles:
            D = pdet(a, b, c)
            VP = pa(VP, ps(D, F(1, 6)))
            for k in range(3):
                total = pa(pa(a[k], b[k]), c[k])
                MP[k] = pa(MP[k], ps(pm(D, total), F(1, 24)))
    V0, M0 = mass(P, faces)
    assert VP.get((), F(0)) == V0
    assert [p.get((), F(0)) for p in MP] == M0
    for i, s in stars.items():
        assert VP.get((i,), F(0)) == 0
        assert [p.get((i,), F(0)) for p in MP] == s['K']
    triple_selected = [cy for cy in faces
                       if len(cy) == 3 and all(i in stars for i in cy)]
    if not triple_selected:
        ee = edges(faces)
        assert all(len(k) <= 2 for k in VP)
        assert all(len(k) <= 3 for p in MP for k in p)
        for key, value in VP.items():
            if not key:
                continue
            assert len(key) == 2 and key[0] != key[1] and key in ee
            i, j = key
            for k in range(3):
                assert MP[k].get(tuple(sorted((i,i,j))), F(0)) == (
                    value*stars[i]['direction'][k]/4)
                assert MP[k].get(tuple(sorted((i,j,j))), F(0)) == (
                    value*stars[j]['direction'][k]/4)
    return VP, MP, triple_selected


def polynomial_data(p):
    return [[list(k), str(v)] for k, v in sorted(p.items())]


def box_abs(p, radii):
    total = F(0)
    for key, value in p.items():
        term = abs(value)
        for i in key:
            term *= radii[i]
        total += term
    return total


def centroid_box(VP, MP, stars):
    V0 = VP[()]
    g0 = [p[()]/V0 for p in MP]
    radii = {i: max(abs(x) for x in s['interval']) for i, s in stars.items()}
    deltaV = dict(VP)
    deltaV.pop((), None)
    Vmin = V0-box_abs(deltaV, radii)
    if Vmin <= 0:
        return {'status': 'no_positive_volume_bound', 'Vmin': str(Vmin)}
    rho = []
    for k in range(3):
        N = pa(MP[k], ps(VP, -g0[k]))
        assert N.get((), F(0)) == 0
        rho.append(box_abs(N, radii)/Vmin)
    return {'status': 'formal_box_bound', 'Vmin': str(Vmin),
            'coordinate_bounds': list(map(str, rho)),
            'rho_infinity': str(max(rho)),
            'geometry_condition': 'valid moved boundary still required'}


def proposal_planes(P, X, faces):
    rows, origin = [], []
    index = {}
    for f, cy in enumerate(faces):
        if len(cy) == 3:
            n, h = plane(*(X[i] for i in cy))
            if not any(n):
                continue
        else:
            n, h = plane(*(P[i] for i in cy[:3]))
        assert h > 0
        assert all(dot(n, X[i]) == h for i in cy)
        assert all(dot(n, p) <= h for p in X)
        row = primitive(n, h)
        key = tuple(row)
        if key not in index:
            index[key] = len(rows)
            rows.append(row)
            origin.append([])
        origin[index[key]].append(f)
    return {'H': rows}, origin


def coupled_trial(P, faces, stars, primary, compensators):
    selected = set(primary) | set(compensators)
    ee = edges(faces)
    assert all(tuple(sorted((i,j))) not in ee
               for i, j in combinations(selected, 2))
    t = {i: stars[i]['interval'][side] for i, side in primary.items()}
    change = [F(0)]*3
    for i, value in t.items():
        change = add(change, scale(value, stars[i]['K']))
    if compensators:
        A = [[stars[i]['K'][k] for i in compensators] for k in range(3)]
        sol = solve(A, scale(-1, change))
        t.update(dict(zip(compensators, sol)))
    for i, value in t.items():
        lo, hi = stars[i]['interval']
        assert lo <= value <= hi
    X = [p[:] for p in P]
    for i, value in t.items():
        X[i] = add(X[i], scale(value, stars[i]['direction']))
    raw, aliases = proposal_planes(P, X, faces)
    return raw, X, {'parameters': {str(i): str(v) for i, v in t.items()},
                    'original_face_aliases': aliases}, t


def released_cap(P, q, values):
    s, t, tx, ty, alpha, beta, gamma = map(F, values)
    for i, oo in [(103,[71,134]), (100,[71,134]),
                  (117,[71,72]), (106,[71,72]),
                  (120,[3,72,73]), (69,[3,73,134,135])]:
        assert all(dot(q[f], P[i]) == 1 for f in oo)
    T = solve([q[135], q[73], q[71]], [F(1)]*3)
    drop = max(range(3), key=lambda k: abs(q[71][k]))
    free = [k for k in range(3) if k != drop]
    for k, value in zip(free, [tx, ty]):
        T[k] += value/20
    T[drop] = (1-sum(q[71][k]*T[k] for k in free))/q[71][drop]
    A = add(P[103], scale(s, sub(P[103], P[100])))
    B = add(P[117], scale(t, sub(P[117], P[106])))
    Q = [row[:] for row in q[:136]]

    def support(a, b, c):
        n, h = plane(a, b, c)
        assert h != 0
        return [v/h for v in n]

    Q[135] = support(P[69], A, T)
    Q[73] = support(P[69], B, T)
    p120 = solve([Q[3], Q[72], Q[73]], [F(1)]*3)
    L = add(T, scale(alpha, sub(A, T)))
    R = add(T, scale(beta, sub(B, T)))
    D = add(T, scale(gamma, sub(P[69], T)))
    Q[17] = support(L, R, D)
    X = [p[:] for p in P]
    X[103], X[117], X[120] = A, B, p120
    X = [p for i, p in enumerate(X) if i not in (107,111,114)] + [L,R,D]
    assert all(dot(n, p) <= 1 for n in Q for p in X)
    raw = {'H': [primitive(n, F(1)) for n in Q]}
    return raw, X, {'parameters': list(map(str, values)),
                    'removed_original_support': 136,
                    'changed_original_supports': [17,73,135],
                    'omitted_original_points': [107,111,114],
                    'new_points': ['L','R','D']}


def audit_binding(parent, raw, cloud, expected_mass, out):
    sys.path.insert(0, str(parent.resolve()))
    A = importlib.import_module('check_A')
    B = importlib.import_module('check_B')
    C = importlib.import_module('centred_mass')
    a = A.run(raw)
    save(out/'A.json', a)
    b = B.run(raw)
    save(out/'B.json', b)
    assert encode(a) == encode(b)
    vertices = [tuple(map(F, p)) for p in a['raw_vertices']]
    assert set(vertices) <= {tuple(p) for p in cloud}
    for p in cloud:
        assert all(dot(row[:3], p) <= row[3] for row in raw['H'])
    if expected_mass is not None:
        V, M = expected_mass
        assert F(a['ordinary_volume']) == V
        assert list(map(F, a['raw_first_moments'])) == M
    cm = C.run(a)
    save(out/'CENTRED_MASS.json', cm)
    return {'status': 'two_audits_and_mass_binding_completed',
            'V': len(a['raw_vertices']), 'E': len(a['edges']),
            'F': len(a['faces']), 'C': 2*len(a['edges']),
            'strict': a['counts'], 'weak': a['weak'],
            'report': {'bytes': len(encode(a)), 'sha256': digest(encode(a))},
            'disposition': 'not_promoted_pending_source_only_cold_replay'}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--parent', type=Path, required=True)
    ap.add_argument('--out', type=Path, required=True)
    ap.add_argument('--audit', action='store_true')
    args = ap.parse_args()
    args.out.mkdir(parents=True, exist_ok=False)
    P, q, faces, V0, M0 = load_parent(args.parent)
    stars = eligible(P, faces)
    VP, MP, triple_selected = moments_polynomial(P, faces, stars)
    save(args.out/'FORMAL_MOMENTS.json', {
        'eligible_original_vertices': sorted(stars),
        'stars': {str(i): s for i, s in stars.items()},
        'volume': polynomial_data(VP),
        'first_moments': [polynomial_data(p) for p in MP],
        'three_selected_triangles': triple_selected,
        'centroid_box': centroid_box(VP, MP, stars)})
    trials = [('PAIR', {7:1,111:0}, []),
              ('COMP111', {111:0}, [0,16,74]),
              ('COMP7', {7:1}, [0,21,87])]
    summaries = {}
    for name, primary, comp in trials:
        out = args.out/name
        out.mkdir()
        try:
            raw, cloud, definition, t = coupled_trial(P, faces, stars, primary, comp)
            V = peval(VP, t)
            M = [peval(p, t) for p in MP]
            assert V == V0
            direct = M0[:]
            for i, value in t.items():
                direct = add(direct, scale(value, stars[i]['K']))
            assert M == direct
            if comp:
                assert M == M0
            definition['formal_volume'] = str(V)
            definition['formal_first_moments'] = list(map(str, M))
            save(out/'DEFINITION.json', definition)
            save(out/'RAW_PROPOSAL.json', raw)
            save(out/'PRIMAL_CLOUD.json', cloud)
            summaries[name] = {'status': 'support_checks_only_not_a_full_hull_audit'}
            if args.audit:
                summaries[name] = audit_binding(args.parent, raw, cloud, (V,M), out)
        except (AssertionError, ArithmeticError, ValueError) as error:
            summaries[name] = {'status': 'rejected_or_incomplete',
                               'error': type(error).__name__ + ': ' + str(error)}
        save(out/'STATUS.json', summaries[name])
    out = args.out/'RELEASED_CAP_PROPOSAL'
    out.mkdir()
    try:
        values = [F(0),F(0),F(0),F(0),F(8,15),F(10,21),F(3,250)]
        raw, cloud, definition = released_cap(P, q, values)
        save(out/'DEFINITION.json', definition)
        save(out/'RAW_PROPOSAL.json', raw)
        save(out/'PRIMAL_CLOUD.json', cloud)
        result = {'status': 'support_checks_only_not_a_full_hull_audit'}
        if args.audit:
            result = audit_binding(args.parent, raw, cloud, None, out)
    except (AssertionError, ArithmeticError, ValueError) as error:
        result = {'status': 'rejected_or_incomplete',
                  'error': type(error).__name__ + ': ' + str(error)}
    summaries['RELEASED_CAP_PROPOSAL'] = result
    save(out/'STATUS.json', result)
    save(args.out/'SUMMARY.json', summaries)
    files = {}
    for path in sorted(args.out.rglob('*')):
        if path.is_file():
            data = path.read_bytes()
            files[str(path.relative_to(args.out))] = {
                'bytes': len(data), 'sha256': digest(data)}
    save(args.out/'OUTPUT_MANIFEST.json', files)
    print('COUPLED_STAR_METHOD_FINISHED_READ_EACH_STATUS', flush=True)


if __name__ == '__main__':
    main()
