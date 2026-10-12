# Exact checker B.
#
# Same input and same report as checker A (check_A.py), computed by a different route:
# vertices and edges come from pairs of planes instead of triples, face polygons are
# ordered by a different rule, the volume is integrated from a different base point,
# and the equilibrium tests are written differently. All arithmetic is exact.

from fractions import Fraction as Q
from itertools import combinations
from math import lcm
import sys, json

sys.set_int_max_str_digits(0)
ZERO = (0, 0, 0)


def plus(a, b):
    return (a[0] + b[0], a[1] + b[1], a[2] + b[2])


def minus(a, b):
    return (a[0] - b[0], a[1] - b[1], a[2] - b[2])


def times(a, s):
    return tuple(x * s for x in a)


def inner(a, b):
    return a[0] * b[0] + a[1] * b[1] + a[2] * b[2]


def outer(a, b):
    return (
        a[1] * b[2] - a[2] * b[1],
        a[2] * b[0] - a[0] * b[2],
        a[0] * b[1] - a[1] * b[0],
    )


def determinant(a, b, c):
    return inner(a, outer(b, c))


def sg(x):
    return 1 if x > 0 else -1 if x < 0 else 0


def encode(x):
    if isinstance(x, Q):
        return str(x)
    if isinstance(x, (tuple, list)):
        return [encode(v) for v in x]
    if isinstance(x, dict):
        return {k: encode(v) for k, v in x.items()}
    return x


def run(raw):
    # 1. Read the half-spaces [a, b, c, d], meaning a*x + b*y + c*z <= d with d > 0.
    rows = [tuple(map(int, r)) for r in raw["H"]]
    assert len(rows) >= 4 and all(len(r) == 4 and r[-1] > 0 for r in rows)
    assert len(set(rows)) == len(rows)
    normals = [r[:3] for r in rows]
    hs = [r[-1] for r in rows]
    points = set()
    lineedges = set()

    # 2. Vertices and edges: intersect every pair of planes in a line, clip the line by
    # all half-spaces, and keep the end points of the surviving segment.
    for a, b in combinations(range(len(rows)), 2):
        n, m = normals[a], normals[b]
        d = outer(n, m)
        dd = inner(d, d)
        if not dd:
            continue
        p = plus(times(outer(m, d), hs[a]), times(outer(d, n), hs[b]))
        low = None
        high = None
        empty = False
        for nn, hh in zip(normals, hs):
            coeff = inner(nn, d)
            rhs = hh * dd - inner(nn, p)
            if coeff > 0:
                t = Q(rhs, coeff)
                high = t if high is None or t < high else high
            elif coeff < 0:
                t = Q(rhs, coeff)
                low = t if low is None or t > low else low
            elif rhs < 0:
                empty = True
                break
            if low is not None and high is not None and low > high:
                empty = True
                break
        if empty:
            continue
        # An unbounded supporting line would be an unbounded edge/ray.
        assert low is not None and high is not None
        x = times(plus(p, times(d, low)), Q(1, dd))
        y = times(plus(p, times(d, high)), Q(1, dd))
        points.add(x)
        points.add(y)
        if low < high:
            lineedges.add(tuple(sorted((x, y))))

    # Vertices in sorted order, and the edges found from the lines above.
    X = sorted(points)
    assert len(X) >= 4
    index = {p: i for i, p in enumerate(X)}
    pair_edges = {tuple(sorted((index[x], index[y]))) for x, y in lineedges}
    faces = []
    active = []

    # 3. Faces: for each plane, find the boundary sides (pairs of vertices with all
    # other face vertices on one side) and chain them into one cycle.
    for fi, (normal, offset) in enumerate(zip(normals, hs)):
        ids = [i for i, p in enumerate(X) if inner(normal, p) == offset]
        if len(ids) < 3:
            continue
        succ = {}
        for a, b in combinations(ids, 2):
            e = minus(X[b], X[a])
            ee = inner(e, e)
            values = {i: inner(normal, outer(e, minus(X[i], X[a]))) for i in ids}
            zero = [i for i in ids if values[i] == 0]
            projections = [inner(e, minus(X[i], X[a])) for i in zero]
            if min(projections) < 0 or max(projections) > ee:
                continue
            if min(values.values()) >= 0 and max(values.values()) > 0:
                succ[a] = b
            elif max(values.values()) <= 0 and min(values.values()) < 0:
                succ[b] = a
        if not succ:
            continue
        assert len(succ) >= 3 and set(succ) == set(succ.values())
        start = min(succ)
        cycle = [start]
        b = succ[start]
        while b != start:
            assert b not in cycle
            cycle.append(b)
            b = succ[b]
        assert len(cycle) == len(succ) == len(ids)
        faces.append(cycle)
        active.append(fi)

    # 4. Consistency: the edges of the face cycles equal the edges found in step 2,
    # Euler's formula holds, each edge has opposite orientation on its two faces, and
    # the edge graph is connected.
    nrm = [normals[i] for i in active]
    off = [hs[i] for i in active]
    edges = {}
    triangles = []
    adj = [set() for _ in X]
    for fi, cy in enumerate(faces):
        for i, j in zip(cy, cy[1:] + cy[:1]):
            edges.setdefault(tuple(sorted((i, j))), []).append((fi, i, j))
            adj[i].add(j)
            adj[j].add(i)
        triangles.extend((cy[-1], cy[j], cy[j + 1]) for j in range(len(cy) - 2))
    assert set(edges) == pair_edges
    assert len(X) - len(edges) + len(faces) == 2
    assert all(len(v) == 2 and v[0][1:] == v[1][1:][::-1] for v in edges.values())
    visited = set()
    queue = [0]
    while queue:
        i = queue.pop()
        if i not in visited:
            visited.add(i)
            queue.extend(adj[i] - visited)
    assert len(visited) == len(X)

    # 5. Volume and centre of mass, summed over tetrahedra from a base point strictly
    # inside the body (checker A uses the origin).
    rho = min(Q(h, 100 * (1 + sum(map(abs, n)))) for n, h in zip(normals, hs))
    base = (rho, 2 * rho, 3 * rho)
    assert all(inner(n, base) < h for n, h in zip(normals, hs))
    Z = [minus(x, base) for x in X]
    volume = Q(0)
    localmoment = ZERO
    for a, b, c in triangles:
        v = determinant(Z[a], Z[b], Z[c]) / 6
        assert v > 0
        volume += v
        localmoment = plus(localmoment, times(plus(plus(Z[a], Z[b]), Z[c]), v / 4))
    centre = plus(base, times(localmoment, 1 / volume))
    moment = times(centre, volume)
    assert minus(moment, times(centre, volume)) == ZERO

    # 6. Integer coordinates. zz[i] is vertex i measured from the centre of mass, and
    # the edge helper returns the vector from vertex i to vertex j; both are scaled by
    # positive integers, so only their signs are used below.
    C = lcm(*(v.denominator for v in centre))
    M = tuple(int(C * v) for v in centre)
    bs = [lcm(*(v.denominator for v in p)) for p in X]
    aa = [tuple(int(b * v) for v in p) for p, b in zip(X, bs)]
    zz = [minus(times(a, C), times(M, b)) for a, b in zip(aa, bs)]

    def edge(i, j):
        return minus(times(aa[j], bs[i]), times(aa[i], bs[j]))

    # 7. Equilibria. A point of the surface is an equilibrium when the body can rest on
    # it: the line from the centre of mass to that point is perpendicular to a
    # supporting plane there. Results: SF/SW = strict/degenerate stable faces, UV/UW =
    # strict/degenerate unstable vertices, EH/EW = strict/degenerate saddle edges.
    SF = []
    SW = []
    UV = []
    UW = []
    EH = []
    EW = []
    fs = []
    vs = []
    es = []
    fz = 0
    ez = 0

    # Faces (stable): project the centre of mass onto the face plane and test the foot
    # of the perpendicular against each side of the polygon.
    for fi, cy in enumerate(faces):
        n = nrm[fi]
        hc = off[fi] * C - inner(n, M)
        nn = inner(n, n)
        assert hc > 0
        vals = []
        for i, j in zip(cy, cy[1:] + cy[:1]):
            p = minus(times(n, bs[i] * hc), times(zz[i], nn))
            vals.append(inner(n, outer(edge(i, j), p)))
        signs = [sg(v) for v in vals]
        fs.append(signs)
        fz += signs.count(0)
        if min(signs) > 0:
            SF.append(fi)
        elif min(signs) >= 0:
            SW.append(fi)

    # Vertices (unstable): decided from the neighbours along edges, then cross-checked
    # against every other vertex.
    for i in range(len(X)):
        largest = max(inner(zz[i], edge(i, j)) for j in adj[i])
        classification = sg(largest)
        if classification < 0:
            UV.append(i)
        elif classification == 0:
            UW.append(i)
        best = None
        jbest = None
        for j in range(len(X)):
            if j == i:
                continue
            value = inner(zz[i], edge(i, j))
            if best is None or value * bs[jbest] >= best * bs[j]:
                best = value
                jbest = j
        assert sg(best) == classification
        vs.append([jbest, sg(best)])

    # Edges (saddle): the same four sign conditions as in checker A, with the test
    # against the two face normals written through cross products.
    for (i, j), pair in sorted(edges.items()):
        e = edge(i, j)
        ee = inner(e, e)
        ze = inner(zz[i], e)
        p = minus(times(zz[i], ee), times(e, ze))
        n, m = [nrm[v[0]] for v in pair]
        d = outer(n, m)
        assert inner(d, d) > 0
        vals = [
            -ze * bs[j],
            C * ee + ze * bs[j],
            inner(outer(p, m), d),
            inner(outer(n, p), d),
        ]
        signs = [sg(v) for v in vals]
        es.append([i, j, *signs])
        ez += signs.count(0)
        if min(signs) > 0:
            EH.append([i, j])
        elif min(signs) >= 0:
            EW.append([i, j])
    return encode(
        dict(
            V=len(X),
            E=len(edges),
            F=len(faces),
            active_input_indices=active,
            raw_vertices=X,
            faces=faces,
            edges=sorted(edges),
            normals=nrm,
            offsets=off,
            ordinary_volume=volume,
            raw_first_moments=moment,
            raw_centroid=centre,
            centred_first_moments=ZERO,
            centred_centroid=ZERO,
            counts=[len(SF), len(UV), len(EH)],
            weak=[len(SW), len(UW), len(EW)],
            stable_face_ids=SF,
            unstable_vertices=UV,
            saddle_edges=EH,
            weak_faces=SW,
            weak_vertices=UW,
            weak_edges=EW,
            face_signs=fs,
            vertex_max_escape_signs=vs,
            edge_signs=es,
            face_primitive_zero_count=fz,
            vertex_max_zero_count=len(UW),
            edge_primitive_zero_count=ez,
            edge_primitive_count=4 * len(edges),
            integration_triangle_count=len(triangles),
        )
    )


if __name__ == "__main__":
    from pathlib import Path

    raw = json.loads(Path(sys.argv[1]).read_text())
    out = run(raw)
    Path(sys.argv[2]).write_text(json.dumps(out, sort_keys=True, separators=(",", ":")))
    print("B", out["V"], out["E"], out["F"], out["counts"], out["weak"], flush=True)
