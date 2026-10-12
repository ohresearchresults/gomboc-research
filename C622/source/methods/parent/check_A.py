# Exact checker A.
#
# Input: integer half-spaces [a, b, c, d], meaning a*x + b*y + c*z <= d. The program
# rebuilds the polyhedron from triples of planes, computes the volume and centre of
# mass of the uniform solid, and counts its equilibria. All arithmetic is exact
# (integers and fractions); no floating point is used.
#
# Checker B (check_B.py) does the same work by a different route. The two reports must
# agree.

from fractions import Fraction as F
from itertools import combinations
from math import gcd, lcm
import sys, json

sys.set_int_max_str_digits(0)
Z = (0, 0, 0)


def add(a, b):
    return tuple(x + y for x, y in zip(a, b))


def sub(a, b):
    return tuple(x - y for x, y in zip(a, b))


def mul(s, a):
    return tuple(s * x for x in a)


def dot(a, b):
    return sum(x * y for x, y in zip(a, b))


def cross(a, b):
    return (
        a[1] * b[2] - a[2] * b[1],
        a[2] * b[0] - a[0] * b[2],
        a[0] * b[1] - a[1] * b[0],
    )


def det(a, b, c):
    return dot(a, cross(b, c))


def sign(x):
    return (x > 0) - (x < 0)


def encode(x):
    if isinstance(x, F):
        return str(x)
    if isinstance(x, (tuple, list)):
        return [encode(v) for v in x]
    if isinstance(x, dict):
        return {k: encode(v) for k, v in x.items()}
    return x


def polygon(X, ids, N):
    axis = max(range(3), key=lambda j: abs(N[j]))
    a, b = [j for j in range(3) if j != axis]
    ids = sorted(ids, key=lambda i: (X[i][a], X[i][b]))
    lo = []
    hi = []

    def turn(i, j, k):
        return (X[j][a] - X[i][a]) * (X[k][b] - X[i][b]) - (X[j][b] - X[i][b]) * (
            X[k][a] - X[i][a]
        )

    for seq, out in [(ids, lo), (ids[::-1], hi)]:
        for i in seq:
            while len(out) > 1 and turn(out[-2], out[-1], i) <= 0:
                out.pop()
            out.append(i)
    cy = lo[:-1] + hi[:-1]
    if len(cy) < 3:
        return []
    if dot(N, cross(sub(X[cy[1]], X[cy[0]]), sub(X[cy[2]], X[cy[0]]))) < 0:
        cy.reverse()
    k = cy.index(min(cy))
    return cy[k:] + cy[:k]


def run(raw):
    # 1. Read the half-spaces. d > 0 means the origin is strictly inside.
    H = [tuple(map(int, r)) for r in raw["H"]]
    assert len(H) >= 4 and all(len(r) == 4 and r[3] > 0 for r in H)
    assert len(set(H)) == len(H)
    N = [r[:3] for r in H]
    D = [r[3] for r in H]
    vertices = set()
    bounded = set()

    # 2. Vertices: intersect every triple of planes (Cramer's rule) and keep the points
    # that satisfy all inequalities.
    for i, j, k in combinations(range(len(H)), 3):
        a, b, c = N[i], N[j], N[k]
        u = cross(b, c)
        v = cross(c, a)
        w = cross(a, b)
        dd = dot(a, u)
        if not dd:
            continue
        # Six explicit nonnegative cone decompositions certify boundedness.
        for axis in range(3):
            for s in [-1, 1]:
                if all(s * t[axis] * dd >= 0 for t in (u, v, w)):
                    bounded.add((axis, s))
        p = add(add(mul(D[i], u), mul(D[j], v)), mul(D[k], w))
        if dd < 0:
            p = mul(-1, p)
            dd = -dd
        if any(dot(n, p) > h * dd for n, h in zip(N, D)):
            continue
        gg = gcd(*p, dd)
        vertices.add(tuple(t // gg for t in p) + (dd // gg,))
    assert len(bounded) == 6

    # Vertices as exact fractions, in a fixed sorted order.
    X = sorted(tuple(F(t, p[3]) for t in p[:3]) for p in vertices)
    assert len(X) >= 4

    # 3. Faces: for each plane collect the vertices lying on it and order them as a
    # convex polygon, counter-clockwise seen from outside. A plane touching fewer than
    # three vertices is not a face.
    active = []
    faces = []
    for fi, (n, h) in enumerate(zip(N, D)):
        ids = [i for i, x in enumerate(X) if dot(n, x) == h]
        cy = polygon(X, ids, n) if len(ids) >= 3 else []
        if cy:
            active.append(fi)
            faces.append(cy)
    normals = [N[i] for i in active]
    offsets = [D[i] for i in active]

    # 4. Consistency: every edge is shared by exactly two faces with opposite
    # orientation, Euler's formula V - E + F = 2 holds, and the edge graph is connected.
    edges = {}
    tris = []
    for fi, cy in enumerate(faces):
        assert set(cy) == {
            i for i, x in enumerate(X) if dot(normals[fi], x) == offsets[fi]
        }
        for i, j in zip(cy, cy[1:] + cy[:1]):
            edges.setdefault(tuple(sorted((i, j))), []).append((fi, i, j))
        tris.extend((cy[0], cy[j], cy[j + 1]) for j in range(1, len(cy) - 1))
    assert len(X) - len(edges) + len(faces) == 2 and all(
        len(v) == 2 and v[0][1:] == v[1][1:][::-1] for v in edges.values()
    )
    adjacency = [set() for _ in X]
    for i, j in edges:
        adjacency[i].add(j)
        adjacency[j].add(i)
    seen = set()
    todo = [0]
    while todo:
        i = todo.pop()
        if i not in seen:
            seen.add(i)
            todo.extend(adjacency[i] - seen)
    assert len(seen) == len(X)

    # 5. Volume and centre of mass, summed over tetrahedra from the origin to a fan
    # triangulation of each face.
    volume = F(0)
    moment = Z
    for i, j, k in tris:
        v = det(X[i], X[j], X[k]) / 6
        assert v > 0
        volume += v
        moment = add(moment, mul(v / 4, add(add(X[i], X[j]), X[k])))
    centre = mul(1 / volume, moment)
    assert sub(moment, mul(volume, centre)) == Z

    # 6. Integer coordinates. zz[i] is vertex i measured from the centre of mass, and
    # the edge helper returns the vector from vertex i to vertex j; both are scaled by
    # positive integers, so only their signs are used below.
    C = lcm(*(x.denominator for x in centre))
    M = tuple(int(x * C) for x in centre)
    bs = [lcm(*(v.denominator for v in x)) for x in X]
    aa = [tuple(int(v * b) for v in x) for x, b in zip(X, bs)]
    zz = [sub(mul(C, a), mul(b, M)) for a, b in zip(aa, bs)]

    def ed(i, j):
        return sub(mul(bs[i], aa[j]), mul(bs[j], aa[i]))

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

    # Faces (stable): the foot of the perpendicular from the centre of mass must lie
    # inside the face. One sign per side of the polygon: all positive = strictly inside,
    # a zero = on the boundary (degenerate).
    for fi, cy in enumerate(faces):
        vals = [
            dot(normals[fi], cross(zz[i], ed(i, j)))
            for i, j in zip(cy, cy[1:] + cy[:1])
        ]
        sg = [sign(v) for v in vals]
        fs.append(sg)
        fz += sg.count(0)
        if min(sg) > 0:
            SF.append(fi)
        elif min(sg) >= 0:
            SW.append(fi)

    # Vertices (unstable): the plane through the vertex, perpendicular to its direction
    # from the centre of mass, must leave every other vertex strictly behind it. The
    # largest value over all other vertices decides: negative = strict, zero =
    # degenerate.
    for i in range(len(X)):
        js = [j for j in range(len(X)) if j != i]
        j = js[0]
        best = dot(zz[i], ed(i, j))
        for k in js[1:]:
            val = dot(zz[i], ed(i, k))
            cmp = val * bs[j] - best * bs[k]
            if cmp > 0 or (cmp == 0 and k > j):
                j = k
                best = val
        sg = sign(best)
        vs.append([j, sg])
        if sg < 0:
            UV.append(i)
        elif sg == 0:
            UW.append(i)

    # Edges (saddle): the foot of the perpendicular from the centre of mass must lie
    # strictly between the end points (first two signs), and its direction must lie
    # strictly between the outward normals of the two adjacent faces (last two signs).
    for (i, j), pair in sorted(edges.items()):
        e = ed(i, j)
        ee = dot(e, e)
        ze = dot(zz[i], e)
        pn = sub(mul(ee, zz[i]), mul(ze, e))
        n, m = [normals[r[0]] for r in pair]
        nn = dot(n, n)
        mm = dot(m, m)
        nm = dot(n, m)
        delta = nn * mm - nm * nm
        assert delta > 0
        vals = [
            -ze * bs[j],
            C * ee + ze * bs[j],
            dot(pn, sub(mul(mm, n), mul(nm, m))),
            dot(pn, sub(mul(nn, m), mul(nm, n))),
        ]
        sg = [sign(v) for v in vals]
        es.append([i, j, *sg])
        ez += sg.count(0)
        if min(sg) > 0:
            EH.append([i, j])
        elif min(sg) >= 0:
            EW.append([i, j])

    # The centre of mass lies strictly inside every face plane.
    assert all(offsets[i] * C - dot(n, M) > 0 for i, n in enumerate(normals))
    return encode(
        dict(
            V=len(X),
            E=len(edges),
            F=len(faces),
            active_input_indices=active,
            raw_vertices=X,
            faces=faces,
            edges=sorted(edges),
            normals=normals,
            offsets=offsets,
            ordinary_volume=volume,
            raw_first_moments=moment,
            raw_centroid=centre,
            centred_first_moments=Z,
            centred_centroid=Z,
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
            integration_triangle_count=len(tris),
        )
    )


if __name__ == "__main__":
    from pathlib import Path

    raw = json.loads(Path(sys.argv[1]).read_text())
    out = run(raw)
    Path(sys.argv[2]).write_text(json.dumps(out, sort_keys=True, separators=(",", ":")))
    print("A", out["V"], out["E"], out["F"], out["counts"], out["weak"], flush=True)
