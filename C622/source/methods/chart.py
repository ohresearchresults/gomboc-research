"""Exact projective Schlegel stress chart for the literal GRID7 polar graph."""

import json, sys, hashlib
from pathlib import Path
from fractions import Fraction as F
from math import lcm, gcd
from collections import defaultdict, deque

sys.set_int_max_str_digits(0)
sys.path.insert(0, str(Path(__file__).parent / "parent"))
from check_A import dot, cross, add, sub, mul, det, polygon, encode


def inv3(A, b):
    d = det(*A)
    assert d
    return mul(
        1 / d,
        add(
            add(mul(b[0], cross(A[1], A[2])), mul(b[1], cross(A[2], A[0]))),
            mul(b[2], cross(A[0], A[1])),
        ),
    )


def load(root=None):
    root = Path(root) if root is not None else Path(__file__).parent
    raw = json.loads((root / "baseline/raw.json").read_text())
    rep = json.loads((root / "baseline/A.json").read_text())
    Q = [tuple(F(v, row[3]) for v in row[:3]) for row in raw["H"]]
    X = [tuple(map(F, row)) for row in rep["raw_vertices"]]
    faces = [
        polygon(Q, [f for f, cy in enumerate(rep["faces"]) if v in cy], x)
        for v, x in enumerate(X)
    ]
    return Q, X, faces


def recover(outer=None, root=None):
    Q, X, faces = load(root)
    if outer is None:
        # The largest squared area triangular polar face, tie broken by index.
        outer = max(
            (
                dot(
                    cross(sub(Q[cy[1]], Q[cy[0]]), sub(Q[cy[2]], Q[cy[0]])),
                    cross(sub(Q[cy[1]], Q[cy[0]]), sub(Q[cy[2]], Q[cy[0]])),
                ),
                i,
            )
            for i, cy in enumerate(faces)
            if len(cy) == 3
        )[1]
    cy = faces[outer]
    assert len(cy) == 3
    c = mul(F(1, 3), add(add(Q[cy[0]], Q[cy[1]]), Q[cy[2]]))
    a = sub(Q[cy[1]], Q[cy[0]])
    b = sub(Q[cy[2]], Q[cy[0]])
    d = c
    limit = min(
        (1 - dot(x, c)) / dot(x, d)
        for i, x in enumerate(X)
        if i != outer and dot(x, d) > 0
    )
    delta = limit * F(3, 4)
    assert delta > 0
    # basis inverse by reciprocal vectors
    D = det(a, b, d)
    assert D > 0
    rows = [mul(1 / D, cross(b, d)), mul(1 / D, cross(d, a)), mul(1 / D, cross(a, b))]
    R = []
    for q in Q:
        p = tuple(dot(row, sub(q, c)) for row in rows)
        den = 1 - p[2] / delta
        assert den > 0
        R.append(mul(1 / den, p))
    planes = []
    for i, x in enumerate(X):
        if i == outer:
            planes.append((F(0),) * 3)
            continue
        k = dot(x, d) + (dot(x, c) - 1) / delta
        assert k < 0
        planes.append(tuple(-v / k for v in (dot(x, a), dot(x, b), dot(x, c) - 1)))
    # CCW bounded planar faces, CW outer face: reverse outward dual orientation.
    f2 = [list(reversed(cy)) for cy in faces]
    left = {}
    for fi, cy in enumerate(f2):
        for i, j in zip(cy, cy[1:] + cy[:1]):
            assert (i, j) not in left
            left[i, j] = fi
    edges = sorted({tuple(sorted(e)) for e in left})
    weights = []
    for i, j in edges:
        e = sub(R[j][:2], R[i][:2])
        J = (-e[1], e[0])
        diff = sub(planes[left[i, j]][:2], planes[left[j, i]][:2])
        w = dot(diff, J) / dot(e, e)
        assert diff == mul(w, J)
        assert planes[left[i, j]][2] - planes[left[j, i]][2] == -w * dot(J, R[i][:2])
        assert (w < 0) == (outer in (left[i, j], left[j, i]))
        weights.append(w)
    # Full equilibrium, including the recovered negative boundary stresses.
    forces = [[F(0), F(0)] for q in Q]
    for (i, j), w in zip(edges, weights):
        for k in range(2):
            forces[i][k] += w * (R[j][k] - R[i][k])
            forces[j][k] -= w * (R[j][k] - R[i][k])
    assert all(v == [0, 0] for v in forces)
    for q, r in zip(Q, R):
        den = 1 + r[2] / delta
        assert den > 0
        assert q == add(
            c, mul(1 / den, add(add(mul(r[0], a), mul(r[1], b)), mul(r[2], d)))
        )
        for fi, cy in enumerate(f2):
            if Q.index(q) in cy:
                assert r[2] == dot(planes[fi], (r[0], r[1], F(1)))
    out = dict(
        outer=outer,
        boundary=faces[outer],
        Q=Q,
        X=X,
        faces=f2,
        edges=edges,
        weights=weights,
        R=R,
        planes=planes,
        c=c,
        a=a,
        b=b,
        d=d,
        delta=delta,
    )
    return out


if __name__ == "__main__":
    out = recover(int(sys.argv[1]) if len(sys.argv) > 1 else None)
    path = Path(__file__).with_name("chart_exact.json")
    path.write_text(json.dumps(encode(out), sort_keys=True, separators=(",", ":")))
    w = [v for v in out["weights"] if v > 0]
    bits = lambda a: max(
        max(abs(F(x).numerator).bit_length(), F(x).denominator.bit_length()) for x in a
    )
    print(
        "EXACT_PROJECTIVE_STRESS_RECOVERY_PASS",
        out["outer"],
        out["boundary"],
        "delta",
        float(out["delta"]),
        "w",
        float(min(w)),
        float(max(w)),
        "weightbits",
        bits(out["weights"]),
        "Rbits",
        bits(sum((list(p) for p in out["R"]), [])),
        "sha",
        hashlib.sha256(path.read_bytes()).hexdigest(),
    )
