# material-307a74325bca

Historical AI scientific source/proof material. Statements retain their original scope; this is not an independently reviewed theorem.

---

#!/usr/bin/env python3
"""Exact compiler/control checks for the effective nine-vertex gap theorem.

Standard library only. These checks do NOT replay the accepted nine-vertex
PSD theorem or enumerate all geometric configurations. The uniform bounds
for every admissible cycle are proved in the companion mathematical text.
"""
from __future__ import annotations
from collections import Counter
from fractions import Fraction as F
from itertools import combinations
import hashlib
import json
from pathlib import Path
import sys

N = 46
ZERO = (0,) * N
Poly = dict[tuple[int, ...], int]

def const(c: int) -> Poly:
    return {ZERO: c} if c else {}

def var(i: int) -> Poly:
    e = [0] * N
    e[i] = 1
    return {tuple(e): 1}

def add(*ps: Poly) -> Poly:
    out: dict[tuple[int, ...], int] = {}
    for p in ps:
        for e, c in p.items():
            out[e] = out.get(e, 0) + c
    return {e: c for e, c in out.items() if c}

def scale(p: Poly, k: int) -> Poly:
    return {e: k*c for e, c in p.items()} if k else {}

def mul(p: Poly, q: Poly) -> Poly:
    out: dict[tuple[int, ...], int] = {}
    for e, c in p.items():
        for f, d in q.items():
            z = tuple(a+b for a, b in zip(e, f))
            out[z] = out.get(z, 0) + c*d
    return {e: c for e, c in out.items() if c}

def det(a: list[Poly], b: list[Poly], c: list[Poly]) -> Poly:
    return add(mul(a[0], add(mul(b[1], c[2]), scale(mul(b[2], c[1]), -1))),
               scale(mul(a[1], add(mul(b[0], c[2]), scale(mul(b[2], c[0]), -1))), -1),
               mul(a[2], add(mul(b[0], c[1]), scale(mul(b[1], c[0]), -1))))

def subvec(a: list[Poly], b: list[Poly]) -> list[Poly]:
    return [add(x, scale(y, -1)) for x, y in zip(a, b)]

def evaluate(p: Poly, values: list[F]) -> F:
    ans = F(0)
    for e, c in p.items():
        term = F(c)
        for k, v in zip(e, values):
            if k:
                term *= v**k
        ans += term
    return ans

def stats(p: Poly) -> dict[str, int]:
    return {"terms": len(p), "degree": max(map(sum, p), default=0),
            "height": max(map(abs, p.values()), default=0),
            "l1": sum(map(abs, p.values()))}

def check_cycle(faces: list[tuple[int, int, int]]) -> None:
    if not 1 <= len(faces) <= 14:
        raise ValueError("A cycle must contain between 1 and 14 triangles.")
    boundary: Counter[tuple[int, int]] = Counter()
    for a, b, c in faces:
        if len({a, b, c}) != 3 or not all(0 <= i < 9 for i in (a, b, c)):
            raise ValueError("Invalid triangle labels.")
        for i, j in ((a, b), (b, c), (c, a)):
            boundary[tuple(sorted((i, j)))] += 1 if i < j else -1
    if any(boundary.values()):
        raise ValueError("The formal oriented boundary is not zero.")

def check_tree(tree: list[tuple[int, int]]) -> None:
    if len(tree) != 9 or len({i for i, _ in tree}) != 9:
        raise ValueError("Need nine distinct nonroot sources.")
    parent = dict(tree)
    roots = set(range(10)) - set(parent)
    if len(roots) != 1:
        raise ValueError("Need exactly one root.")
    root = next(iter(roots))
    for start in range(10):
        x, seen = start, set()
        while x != root:
            if x in seen or x not in parent or parent[x] not in range(10):
                raise ValueError("Not an arborescence.")
            seen.add(x)
            x = parent[x]

def build_model(faces: list[tuple[int, int, int]], tree: list[tuple[int, int]]):
    """Return integer polynomial constraints, all inequalities oriented >=0."""
    check_cycle(faces)
    check_tree(tree)
    z = [[var(3*i+j) for j in range(3)] for i in range(10)]
    alpha = [var(30+i) for i in range(9)]
    m00, m11, m22, m01, m02, m12 = [var(39+i) for i in range(6)]
    M = [[m00, m01, m02], [m01, m11, m12], [m02, m12, m22]]
    h = var(45)
    ds = [det(z[a], z[b], z[c]) for a, b, c in faces]
    D = add(*ds)
    J = [add(*(mul(t, add(z[a][r], z[b][r], z[c][r]))
                for t, (a, b, c) in zip(ds, faces))) for r in range(3)]
    constraints: list[tuple[str, str, Poly]] = []
    def ge(name: str, p: Poly):
        constraints.append((name, ">=", p))
    def eq(name: str, p: Poly):
        constraints.append((name, "=", p))
    for i in range(10):
        for r in range(3):
            ge(f"box+_{i}_{r}", add(const(1), z[i][r]))
            ge(f"box-_{i}_{r}", add(const(1), scale(z[i][r], -1)))
    for i, p in enumerate(alpha):
        ge(f"alpha_{i}", p)
    eq("alpha_sum", add(*alpha, const(-1)))
    for r in range(3):
        eq(f"contained_{r}", add(z[9][r], scale(add(*(mul(alpha[i], z[i][r])
                                                  for i in range(9))), -1)))
    for i in range(3):
        ge(f"psd1_{i}", M[i][i])
    for i, j in combinations(range(3), 2):
        ge(f"psd2_{i}_{j}", add(mul(M[i][i], M[j][j]), scale(mul(M[i][j], M[i][j]), -1)))
    ge("psd3", det(M[0], M[1], M[2]))
    eq("trace", add(M[0][0], M[1][1], M[2][2], const(-1)))
    ge("h_low", h)
    ge("h_high", add(const(12), scale(h, -1)))
    ge("volume_degree", add(scale(D, 32), const(-1)))
    for t, (a, b, c) in enumerate(faces):
        for i in range(9):
            ge(f"support_{t}_{i}", scale(det(subvec(z[b], z[a]), subvec(z[c], z[a]),
                                               subvec(z[i], z[a])), -1))
    for i, j in tree:
        A = [add(scale(mul(D, z[i][r]), 4), scale(J[r], -1)) for r in range(3)]
        e = subvec(z[j], z[i])
        row = add(*(mul(mul(A[r], M[r][s]), e[s]) for r in range(3) for s in range(3)))
        ge(f"tree_{i}_{j}", add(scale(mul(D, h), 4), row))
    return constraints, D, J

def values_for(points: list[tuple[F, F, F]], alpha: list[F]) -> list[F]:
    if len(points) != 10 or len(alpha) != 9:
        raise ValueError("Wrong control dimensions.")
    return [q for point in points for q in point] + alpha + [F(1,3)]*3 + [F(0)]*3 + [F(12)]

def audit_control(constraints, D, J, values, expected_D, expected_g):
    for name, relation, p in constraints:
        x = evaluate(p, values)
        assert x == 0 if relation == "=" else x >= 0, (name, relation, x)
    d = evaluate(D, values)
    g = tuple(evaluate(p, values)/(4*d) for p in J)
    assert d == expected_D and g == expected_g, (d, g)
    return {"D": str(d), "centroid": list(map(str, g)), "constraints_passed": len(constraints)}

def main() -> dict:
    # Maximum-size genuine nine-vertex boundary: rational octagonal pyramid.
    base = [(1,0), (F(3,5),F(4,5)), (0,1), (-F(3,5),F(4,5)),
            (-1,0), (-F(3,5),-F(4,5)), (0,-1), (F(3,5),-F(4,5))]
    faces = [(i, (i+1)%8, 8) for i in range(8)] + [(0,i+1,i) for i in range(1,7)]
    tree = [(i, i+1) for i in range(9)]
    constraints, D, J = build_model(faces, tree)
    assert len(constraints) == 219
    st = [stats(p) for _, _, p in constraints]
    assert max(s["degree"] for s in st) <= 6
    assert max(s["height"] for s in st) <= 2**14
    assert max(s["l1"] for s in st) <= 10920
    points = [(F(x),F(y),F(0)) for x,y in base] + [(F(0),F(0),F(1)), (F(0),F(0),F(1,4))]
    v = values_for(points, [F(3,32)]*8+[F(1,4)])
    control1 = audit_control(constraints, D, J, v, F(28,5), (F(0),F(0),F(1,4)))
    # A positive degree-two boundary chain: D is twice 6V, but J/(4D)
    # remains the genuine uniform centroid. This is NOT a new polyhedron.
    tetra_faces = [(1,2,3),(0,3,2),(0,1,3),(0,2,1)] * 2
    c2, D2, J2 = build_model(tetra_faces, tree)
    tet = [(F(0),F(0),F(0)),(F(1),F(0),F(0)),(F(0),F(1),F(0)),(F(0),F(0),F(1))]
    pts2 = tet + [(F(1,4),)*3]*6
    v2 = values_for(pts2, [F(1,4)]*4+[F(0)]*5)
    control2 = audit_control(c2, D2, J2, v2, F(2), (F(1,4),)*3)
    # Universal coefficient estimates, independent of both control geometries.
    d_l1 = 14*6
    j_l1 = 3*d_l1
    a_l1 = 4*d_l1+j_l1
    row_l1 = 9*2*a_l1+4*d_l1
    assert (d_l1,j_l1,a_l1,row_l1) == (84,252,588,10920)
    assert max(32*d_l1+1,row_l1,48) < 2**14
    assert 2*46+2*230 < 2**14
    # JPT Theorem 1: base=6^46/32, exponent=46*12^46.
    # 6^3<2^8 implies log2(base)<353/3<118.
    assert 6**3 < 2**8 and 353 < 3*118
    exponent_bound = 118*46*12**46
    assert exponent_bound < 2**178
    assert 292**2*3 < 512**2
    assert (4**2*3)*12**2 < 84**2  # 4sqrt(3)/84 < 1/12.
    return {"version":1,"variables":46,"degree_bound":6,"coefficient_height_bound":2**14,
            "constraint_bound":230,"compiled_constraints":len(constraints),
            "compiled_max_degree":max(s["degree"] for s in st),
            "compiled_max_height":max(s["height"] for s in st),
            "compiled_max_l1":max(s["l1"] for s in st),
            "D_stats":stats(D),"J_stats":[stats(p) for p in J],
            "JPT_log_reciprocal_upper_integer":str(exponent_bound),
            "JPT_upper_integer_bit_length":exponent_bound.bit_length(),
            "certified_gap":"strictly greater than 2^(-2^178)",
            "octagonal_pyramid":control1,"degree_two_tetra_chain":control2,
            "scope":"Arithmetic/compiler controls only; universal proof uses the stated nine-vertex PSD theorem and JPT Theorem 1."}

if __name__ == "__main__":
    if not __debug__:
        raise RuntimeError("Assertions must remain enabled.")
    report = main()
    target = Path(sys.argv[1]) if len(sys.argv)>1 else Path("ten_vertex_gap_report.json")
    data = (json.dumps(report,indent=2,sort_keys=True)+"\n").encode()
    target.write_bytes(data)
    print("TEN_VERTEX_EFFECTIVE_GAP_ARITHMETIC_AND_MODEL_PASS")
    print(f"{target.name} {len(data)} {hashlib.sha256(data).hexdigest()}")
