# material-32e6b4a4e142

AI research material

<!-- historical-status:start -->
> **Historical AI material.** The title and claims below reflect the AI’s assessment at the time. Claims of proof, certification or completion are not a current verification verdict.
>
> [C622](../C622/README.md) passes the supplied exact checks; C<500 remains open; Minimum’s C≥34 remains a working lower bound requiring a consolidated proof. See [verification status and source gaps](../catalog/coverage.md).
<!-- historical-status:end -->

---

#!/usr/bin/env python3
"""Exact own-volume-centroid equilibrium certificates for rational 3D halfspaces.

Standard library only. Inputs are {"normals": [[r,r,r],...], "supports": [r,...]}.
Use integers or rational strings, not JSON floats. Every input plane must be a
maximal facet of the bounded, full-dimensional polyhedron. No normalization of
normals to unit length is needed. Enumeration is deliberately exhaustive and is
intended for small or moderate facet sets, not a high-performance hull solver.

CLI:
  python3 normal_fan_certificate.py --self-test --output certificate_tests.json
  python3 normal_fan_certificate.py --input body.json --output certificate.json
"""
from __future__ import annotations

import argparse
import hashlib
import itertools
import json
import sys
from fractions import Fraction as F
from pathlib import Path
from typing import Any, Iterable

Vec = tuple[F, F, F]
ZERO: Vec = (F(0), F(0), F(0))


def rat(x: Any) -> F:
    if isinstance(x, bool) or not isinstance(x, (int, str, F)):
        raise ValueError("Rational inputs must be integers or rational strings, not floats.")
    return F(x)


def vec(x: Iterable[Any]) -> Vec:
    result = tuple(rat(y) for y in x)
    if len(result) != 3:
        raise ValueError("A vector must have exactly three coordinates.")
    return result  # type: ignore[return-value]


def add(a: Vec, b: Vec) -> Vec:
    return tuple(a[i] + b[i] for i in range(3))  # type: ignore[return-value]


def sub(a: Vec, b: Vec) -> Vec:
    return tuple(a[i] - b[i] for i in range(3))  # type: ignore[return-value]


def mul(s: F, a: Vec) -> Vec:
    return tuple(s * x for x in a)  # type: ignore[return-value]


def dot(a: Vec, b: Vec) -> F:
    return sum((a[i] * b[i] for i in range(3)), F(0))


def cross(a: Vec, b: Vec) -> Vec:
    return (a[1] * b[2] - a[2] * b[1],
            a[2] * b[0] - a[0] * b[2],
            a[0] * b[1] - a[1] * b[0])


def det(a: Vec, b: Vec, c: Vec) -> F:
    return dot(a, cross(b, c))


def sumvec(values: Iterable[Vec]) -> Vec:
    result = ZERO
    for value in values:
        result = add(result, value)
    return result


def solve_planes(n: list[Vec], h: list[F], ids: tuple[int, int, int]) -> Vec | None:
    i, j, k = ids
    denominator = det(n[i], n[j], n[k])
    if not denominator:
        return None
    numerator = sumvec((mul(h[i], cross(n[j], n[k])),
                        mul(h[j], cross(n[k], n[i])),
                        mul(h[k], cross(n[i], n[j]))))
    return mul(1 / denominator, numerator)


def facet_cycle(active: list[int], vertices: list[Vec], normal: Vec) -> list[int]:
    # Dropping a coordinate with nonzero normal component is injective on a plane.
    drop = max(range(3), key=lambda k: abs(normal[k]))
    axes = [k for k in range(3) if k != drop]
    projected = {i: (vertices[i][axes[0]], vertices[i][axes[1]]) for i in active}
    order = sorted(active, key=lambda i: projected[i])

    def turn(a: int, b: int, c: int) -> F:
        pa, pb, pc = projected[a], projected[b], projected[c]
        return (pb[0] - pa[0]) * (pc[1] - pa[1]) - (pb[1] - pa[1]) * (pc[0] - pa[0])

    lower: list[int] = []
    for i in order:
        while len(lower) >= 2 and turn(lower[-2], lower[-1], i) <= 0:
            lower.pop()
        lower.append(i)
    upper: list[int] = []
    for i in reversed(order):
        while len(upper) >= 2 and turn(upper[-2], upper[-1], i) <= 0:
            upper.pop()
        upper.append(i)
    cycle = lower[:-1] + upper[:-1]
    if len(cycle) < 3 or set(cycle) != set(active):
        raise ValueError("An input plane is not a maximal facet with exactly its extreme vertices.")
    a, b, c = (vertices[i] for i in cycle[:3])
    orientation = dot(cross(sub(b, a), sub(c, a)), normal)
    if orientation < 0:
        cycle.reverse()
    elif not orientation:
        raise ValueError("Degenerate facet orientation.")
    # Canonical outward cycle, starting at its smallest vertex index.
    shift = cycle.index(min(cycle))
    return cycle[shift:] + cycle[:shift]


def status(values: list[F]) -> str:
    if all(x > 0 for x in values):
        return "strict"
    if all(x >= 0 for x in values):
        return "weak"
    return "excluded"


def certify(data: dict[str, Any]) -> dict[str, Any]:
    n = [vec(x) for x in data["normals"]]
    h = [rat(x) for x in data["supports"]]
    m = len(n)
    if m != len(h) or m < 4 or any(x == ZERO for x in n):
        raise ValueError("At least four nonzero normals and equally many supports are required.")
    normalized = []
    for ni, hi in zip(n, h):
        factor = abs(next(x for x in ni if x))
        normalized.append(tuple(x / factor for x in (*ni, hi)))
    if len(set(normalized)) != m:
        raise ValueError("Duplicate positively proportional input planes.")
    if not any(det(n[i], n[j], n[k]) for i, j, k in itertools.combinations(range(m), 3)):
        raise ValueError("Normals do not span three dimensions.")
    # The recession cone is pointed because the normals span R^3. If nonzero,
    # it has an extreme ray at two independent active normal planes.
    for i, j in itertools.combinations(range(m), 2):
        direction = cross(n[i], n[j])
        if direction != ZERO:
            for sign in (F(1), F(-1)):
                d = mul(sign, direction)
                if all(dot(ni, d) <= 0 for ni in n):
                    raise ValueError("Unbounded recession cone.")

    vertex_set: set[Vec] = set()
    for ids in itertools.combinations(range(m), 3):
        point = solve_planes(n, h, ids)
        if point is not None and all(dot(ni, point) <= hi for ni, hi in zip(n, h)):
            vertex_set.add(point)
    vertices = sorted(vertex_set)
    if len(vertices) < 4:
        raise ValueError("Empty or lower-dimensional halfspace intersection.")
    a0 = vertices[0]
    if not any(det(sub(vertices[i], a0), sub(vertices[j], a0), sub(vertices[k], a0))
               for i, j, k in itertools.combinations(range(1, len(vertices)), 3)):
        raise ValueError("Halfspace intersection is not full-dimensional.")

    cycles = []
    for ni, hi in zip(n, h):
        active = [i for i, point in enumerate(vertices) if dot(ni, point) == hi]
        if len(active) < 3:
            raise ValueError("Inactive or redundant plane: remove it before certification.")
        cycles.append(facet_cycle(active, vertices, ni))
    edge_facets: dict[tuple[int, int], list[int]] = {}
    neighbors: dict[int, set[int]] = {i: set() for i in range(len(vertices))}
    for fi, cycle in enumerate(cycles):
        for a, b in zip(cycle, cycle[1:] + cycle[:1]):
            key = tuple(sorted((a, b)))
            edge_facets.setdefault(key, []).append(fi)
            neighbors[a].add(b)
            neighbors[b].add(a)
    if any(len(facets) != 2 for facets in edge_facets.values()):
        raise ValueError("Each edge must have exactly two maximal incident facets.")
    if len(vertices) - len(edge_facets) + m != 2:
        raise ValueError("Euler incidence consistency check failed.")
    if any(len(adjacent) < 3 for adjacent in neighbors.values()):
        raise ValueError("Invalid vertex degree.")

    D, Q = F(0), ZERO
    triangles = []
    for cycle in cycles:
        for k in range(1, len(cycle) - 1):
            ids = (cycle[0], cycle[k], cycle[k + 1])
            a, b, c = (vertices[i] for i in ids)
            signed = det(a, b, c)
            D += signed
            Q = add(Q, mul(signed, sumvec((a, b, c))))
            triangles.append(ids)
    if D <= 0:
        raise ValueError("Signed volume must be positive.")
    g = mul(1 / (4 * D), Q)
    f = [4 * D * hi - dot(ni, Q) for ni, hi in zip(n, h)]
    if not all(x > 0 for x in f):
        raise ValueError("Computed solid centroid is not strictly interior.")
    W = [sub(mul(4 * D, point), Q) for point in vertices]

    face_tests = []
    for i in range(m):
        entries = []
        for j in range(m):
            if i != j:
                A = dot(n[i], n[i]) * f[j] - dot(n[i], n[j]) * f[i]
                entries.append({"other_facet": j, "A": A})
        face_tests.append({"facet": i, "status": status([entry["A"] for entry in entries]),
                           "tests": entries})
    vertex_tests = []
    for a in range(len(vertices)):
        entries = [{"neighbor": b, "B": dot(W[a], sub(vertices[a], vertices[b]))}
                   for b in sorted(neighbors[a])]
        vertex_tests.append({"vertex": a, "status": status([entry["B"] for entry in entries]),
                             "tests": entries})
    edge_tests = []
    for (a, b), (i, j) in sorted(edge_facets.items()):
        e = sub(vertices[b], vertices[a])
        L = dot(e, e)
        aa, bb, cc = dot(n[i], n[i]), dot(n[j], n[j]), dot(n[i], n[j])
        delta = aa * bb - cc * cc
        if delta <= 0 or L <= 0:
            raise ValueError("Degenerate edge or incident normal pair.")
        T = -dot(W[a], e)
        Ri, Rj = bb * f[i] - cc * f[j], aa * f[j] - cc * f[i]
        values = [T, 4 * D * L - T, Ri, Rj]
        edge_tests.append({"edge": (a, b), "facets": (i, j), "status": status(values),
                           "tests": {"T": T, "4DL_minus_T": values[1], "R_i": Ri, "R_j": Rj},
                           "edge_parameter": T / (4 * D * L),
                           "normal_coefficients": (Ri / (4 * D * delta), Rj / (4 * D * delta))})
    counts = {"S": sum(x["status"] == "strict" for x in face_tests),
              "U": sum(x["status"] == "strict" for x in vertex_tests),
              "H": sum(x["status"] == "strict" for x in edge_tests)}
    weak = {"facets": sum(x["status"] == "weak" for x in face_tests),
            "vertices": sum(x["status"] == "weak" for x in vertex_tests),
            "edges": sum(x["status"] == "weak" for x in edge_tests)}
    no_weak = not any(weak.values())
    if no_weak and counts["S"] + counts["U"] - counts["H"] != 2:
        raise ValueError("Nondegenerate equilibrium index consistency check failed.")
    return {"input": {"normals": n, "supports": h}, "vertices": vertices,
            "facet_cycles_outward": cycles, "surface_triangles_outward": triangles,
            "V": len(vertices), "E": len(edge_facets), "F": m, "C": 2 * len(edge_facets),
            "D_six_volume": D, "Q_twenty_four_first_moment": Q,
            "volume": D / 6, "solid_centroid": g, "strict_counts": counts,
            "weak_stratum_flags": weak,
            "weak_flags_note": "Flags can refer to the same physical point in multiple strata; these are not distinct-point counts.",
            "no_weak_equilibria": no_weak,
            "strict_own_class110": counts == {"S": 1, "U": 1, "H": 0} and no_weak,
            "face_tests": face_tests, "vertex_tests": vertex_tests, "edge_tests": edge_tests}


def json_ready(obj: Any) -> Any:
    if isinstance(obj, F):
        return str(obj)
    if isinstance(obj, dict):
        return {key: json_ready(value) for key, value in obj.items()}
    if isinstance(obj, (tuple, list)):
        return [json_ready(value) for value in obj]
    return obj


def canonical_json(obj: Any) -> bytes:
    return (json.dumps(json_ready(obj), sort_keys=True, indent=2, ensure_ascii=True) + "\n").encode("utf-8")


def self_test() -> dict[str, Any]:
    cases: dict[str, dict[str, Any]] = {
        "regular_tetrahedron": {
            "normals": [[-1, -1, -1], [-1, 1, 1], [1, -1, 1], [1, 1, -1]],
            "supports": [1, 1, 1, 1]},
        "cube": {
            "normals": [[1, 0, 0], [-1, 0, 0], [0, 1, 0], [0, -1, 0], [0, 0, 1], [0, 0, -1]],
            "supports": [1] * 6}}
    cases["regular_octahedron"] = {
        "normals": [list(signs) for signs in itertools.product((-1, 1), repeat=3)],
        "supports": [1] * 8}
    plane_scales = [F(2), F(3, 7), F(5), F(11, 13), F(17), F(19, 23)]
    cases["cube_rescaled_plane_equations"] = {
        "normals": [mul(k, vec(ni)) for k, ni in zip(plane_scales, cases["cube"]["normals"])],
        "supports": plane_scales}
    translation = vec(["2/3", "-5/7", "11/13"])
    scale = F(3, 2)
    cases["translated_scaled_cube"] = {
        "normals": cases["cube"]["normals"],
        "supports": [scale + dot(vec(ni), translation) for ni in cases["cube"]["normals"]]}
    for t in (1, 2, 3):
        cases[f"sheared_tetrahedron_t{t}"] = {
            "normals": [[0, 0, -1], [0, -1, 0], [-1, 0, t], [1, 1, 1 - t]],
            "supports": [0, 0, 0, 1]}
    reports = {name: certify(data) for name, data in cases.items()}
    assert reports["regular_tetrahedron"]["strict_counts"] == {"S": 4, "U": 4, "H": 6}
    assert reports["regular_tetrahedron"]["volume"] == F(8, 3)
    assert reports["regular_tetrahedron"]["solid_centroid"] == ZERO
    assert reports["regular_tetrahedron"]["no_weak_equilibria"]
    for name in ("cube", "translated_scaled_cube", "cube_rescaled_plane_equations"):
        assert reports[name]["strict_counts"] == {"S": 6, "U": 8, "H": 12}
        assert reports[name]["no_weak_equilibria"]
    assert reports["regular_octahedron"]["strict_counts"] == {"S": 8, "U": 6, "H": 12}
    assert reports["regular_octahedron"]["volume"] == F(4, 3)
    assert reports["regular_octahedron"]["solid_centroid"] == ZERO
    assert reports["regular_octahedron"]["no_weak_equilibria"]
    assert reports["cube_rescaled_plane_equations"]["vertices"] == reports["cube"]["vertices"]
    assert reports["cube_rescaled_plane_equations"]["solid_centroid"] == ZERO
    assert reports["cube"]["volume"] == 8
    assert reports["translated_scaled_cube"]["volume"] == 27
    assert reports["translated_scaled_cube"]["solid_centroid"] == translation
    for t in (1, 2, 3):
        report = reports[f"sheared_tetrahedron_t{t}"]
        assert report["volume"] == F(1, 6)
        assert report["solid_centroid"] == vec([F(1 + t, 4), F(1, 4), F(1, 4)])
    assert reports["sheared_tetrahedron_t1"]["face_tests"][0]["status"] == "strict"
    assert reports["sheared_tetrahedron_t2"]["face_tests"][0]["status"] == "weak"
    assert reports["sheared_tetrahedron_t3"]["face_tests"][0]["status"] == "excluded"
    assert not reports["sheared_tetrahedron_t2"]["no_weak_equilibria"]

    invalid_cases = {
        "unbounded": {"normals": [[1, 0, 0], [0, 1, 0], [0, 0, 1], [1, 1, 1]], "supports": [1] * 4},
        "empty": {"normals": cases["cube"]["normals"], "supports": [-1] * 6},
        "flat": {"normals": cases["cube"]["normals"], "supports": [1, 1, 1, 1, 0, 0]},
        "duplicate": {"normals": cases["cube"]["normals"] + [[2, 0, 0]], "supports": [1] * 6 + [2]},
        "redundant": {"normals": cases["cube"]["normals"] + [[1, 1, 1]], "supports": [1] * 6 + [4]},
        "float": {"normals": cases["cube"]["normals"], "supports": [1.0] * 6}}
    rejections = {}
    for name, data in invalid_cases.items():
        try:
            certify(data)
        except ValueError as exc:
            rejections[name] = str(exc)
        else:
            raise AssertionError(f"Invalid case {name} was not rejected.")
    return {"schema_version": 1, "method": "exact fixed-normal own-centroid sign certificate",
            "test_status": "SELFTEST_OK", "reports": reports,
            "rejected_invalid_inputs": rejections,
            "research_status": "Method tests only. No class110 construction is claimed."}


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    mode = parser.add_mutually_exclusive_group(required=True)
    mode.add_argument("--self-test", action="store_true")
    mode.add_argument("--input", type=Path)
    parser.add_argument("--output", required=True, type=Path)
    args = parser.parse_args()
    try:
        result = self_test() if args.self_test else certify(json.loads(args.input.read_text(encoding="utf-8")))
        payload = canonical_json(result)
        args.output.write_bytes(payload)
    except (ValueError, KeyError, OSError, ZeroDivisionError, AssertionError) as exc:
        parser.exit(2, f"CERTIFICATE_ERROR: {exc}\n")
    print("SELFTEST_OK" if args.self_test else "CERTIFICATE_OK")
    print(f"OUTPUT_BYTES {len(payload)}")
    print(f"OUTPUT_SHA256 {hashlib.sha256(payload).hexdigest()}")
    if args.self_test:
        for name, report in result["reports"].items():
            print(name, json.dumps(report["strict_counts"], sort_keys=True),
                  "weak_flags", json.dumps(report["weak_stratum_flags"], sort_keys=True))
    else:
        print("STRICT_COUNTS", json.dumps(result["strict_counts"], sort_keys=True))
        print("STRICT_OWN_CLASS110", result["strict_own_class110"])


if __name__ == "__main__":
    main()
