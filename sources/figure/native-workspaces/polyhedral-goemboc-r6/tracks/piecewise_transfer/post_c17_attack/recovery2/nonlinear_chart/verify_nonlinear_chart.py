#!/usr/bin/env python3
"""Independent exact verifier for the 156D nonlinear coplanarity chart.

The verifier does not import the chart builder.  It reconstructs the endpoint,
moving-frame coordinates, all 156 tangent columns, all 38 dense mechanics
jets, and the three requested ranks directly from the frozen parent data.
"""
from __future__ import annotations

import hashlib
import itertools
import json
import sys
from collections import defaultdict
from fractions import Fraction as Q
from pathlib import Path
from types import SimpleNamespace


HERE = Path(__file__).resolve().parent
ATTACK = HERE.parents[1]
CHART = HERE / "nonlinear_chart.json"
OUTPUT = HERE / "nonlinear_chart_verification.json"
sys.path.insert(0, str(ATTACK))

import post_c17_exact as pc  # noqa: E402


BASE = tuple(range(17))
SHELL = tuple(range(231, 247))
TARGET_NAMES = (
    "S228_264_246_via_246_228",
    "U228_via_251",
    "U231_via_232",
    "U246_via_245",
    "H8_246_via_t",
    "H228_254_via_beta2",
    "H231_247_via_beta1",
    "H236_237_via_beta1",
)


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def load_endpoint():
    ledger = json.loads((ATTACK / "cells" / "endpoint.json").read_text())
    rows = pc.read_rows(ATTACK / "cells" / "endpoint.csv")
    faces = pc.ex.exactify_faces(
        rows,
        SimpleNamespace(
            faces=[{"cycle": list(cycle)} for cycle in ledger["maximal_face_cycles"]]
        ),
    )
    volume, centroid = pc.ex.exact_mass(rows, faces)
    edges, active, fl, vl, el, stable, unstable, saddles = pc.ex.exact_mechanics(
        rows, faces, centroid
    )
    assert [len(active), len(edges), len(faces)] == [61, 150, 91]
    assert [len(stable), len(unstable), len(saddles)] == [2, 4, 4]
    assert active == ledger["active_vertices"]
    assert [faces[index]["cycle"] for index in stable] == ledger["stable_faces"]
    assert unstable == ledger["unstable_vertices"]
    assert [list(edge) for edge in saddles] == ledger["saddle_edges"]
    assert fl == ledger["face_mechanics_ledger"]
    assert vl == ledger["vertex_mechanics_ledger"]
    assert el == ledger["edge_mechanics_ledger"]
    assert pc.qs(volume) == ledger["volume_exact"]
    assert [pc.qs(value) for value in centroid] == ledger["centroid_exact"]
    assert not (pc.esc.forced_rails() - set(edges))
    return ledger, rows, faces


def area_squared(rows, triple):
    a, b, c = (rows[label] for label in triple)
    normal = pc.ex.cross(pc.ex.sub(b, a), pc.ex.sub(c, a))
    return pc.ex.dot(normal, normal)


def canonical_frame(rows, cycle):
    scores = [(area_squared(rows, triple), triple) for triple in itertools.combinations(cycle, 3)]
    maximum = max(score for score, _triple in scores)
    return min(triple for score, triple in scores if score == maximum), maximum


def coordinates(point, a, u, v):
    w = pc.ex.sub(point, a)
    uu, uv, vv = pc.ex.dot(u, u), pc.ex.dot(u, v), pc.ex.dot(v, v)
    wu, wv = pc.ex.dot(w, u), pc.ex.dot(w, v)
    determinant = uu * vv - uv * uv
    assert determinant > 0
    alpha = (wu * vv - wv * uv) / determinant
    beta = (wv * uu - wu * uv) / determinant
    assert point == pc.ex.add(a, pc.ex.add(pc.ex.mul(u, alpha), pc.ex.mul(v, beta)))
    return alpha, beta


def axis_vector(axis, scale=Q(1)):
    return tuple(scale if offset == axis else Q(0) for offset in range(3))


def append_mode(modes, name, family, deltas):
    modes.append({
        "name": name,
        "family": family,
        "deltas": {
            label: tuple(vector)
            for label, vector in deltas.items()
            if vector != pc.ex.ZERO
        },
    })


def reconstruct_polygon(rows, cycle, prefix, modes):
    frame, area = canonical_frame(rows, cycle)
    a_label, b_label, c_label = frame
    a = rows[a_label]
    u = pc.ex.sub(rows[b_label], a)
    v = pc.ex.sub(rows[c_label], a)
    dependent = tuple(label for label in cycle if label not in frame)
    affine = {label: coordinates(rows[label], a, u, v) for label in dependent}

    for role, frame_label in zip("abc", frame):
        for axis, axis_name in enumerate("xyz"):
            deltas = {frame_label: axis_vector(axis)}
            for label, (alpha, beta) in affine.items():
                weight = {"a": 1 - alpha - beta, "b": alpha, "c": beta}[role]
                if weight:
                    deltas[label] = axis_vector(axis, weight)
            append_mode(
                modes,
                f"{prefix}_frame_{role}{frame_label}_{axis_name}",
                f"{prefix}_moving_frame",
                deltas,
            )
    for label in dependent:
        append_mode(
            modes,
            f"{prefix}_r{label}_alpha",
            f"{prefix}_affine_coordinate",
            {label: u},
        )
        append_mode(
            modes,
            f"{prefix}_r{label}_beta",
            f"{prefix}_affine_coordinate",
            {label: v},
        )
    return {
        "frame": frame,
        "area": area,
        "dependent": dependent,
        "affine": affine,
        "u": u,
        "v": v,
    }


def reconstruct_modes(rows, active):
    modes = []
    base = reconstruct_polygon(rows, BASE, "base", modes)
    shell = reconstruct_polygon(rows, SHELL, "shell", modes)
    free = tuple(sorted(set(active) - set(BASE) - set(SHELL)))
    assert len(free) == 28
    for label in free:
        for axis, axis_name in enumerate("xyz"):
            append_mode(
                modes,
                f"free_r{label}_{axis_name}",
                "free_active_row",
                {label: axis_vector(axis)},
            )
    assert len(modes) == 156
    return modes, base, shell, free


def mode_json(mode):
    return {
        "name": mode["name"],
        "family": mode["family"],
        "row_deltas_exact": {
            str(label): [pc.qs(value) for value in vector]
            for label, vector in sorted(mode["deltas"].items())
        },
    }


def make_jets(rows, faces, modes):
    pc.rj.M = len(modes)
    by_row = defaultdict(list)
    for column, mode in enumerate(modes):
        for label, vector in mode["deltas"].items():
            by_row[label].append((column, vector))
    q = {}
    for label, point in rows.items():
        coordinates_j = []
        for axis in range(3):
            derivative = [Q(0)] * len(modes)
            for column, vector in by_row.get(label, ()):
                derivative[column] = vector[axis]
            coordinates_j.append(pc.rj.J(point[axis], tuple(derivative)))
        q[label] = tuple(coordinates_j)
    centroid, _volume = pc.rj.exact_centroid(q, faces)
    return q, centroid


def reconstruct_jets(rows, faces, modes):
    q, centroid = make_jets(rows, faces, modes)
    incidence = pc.esc.incidence(faces)

    def fc(vertices, edge):
        face = pc.esc.face_by_vertices(faces, vertices)
        values = dict(pc.rj.face_components(face, q, centroid))
        return values[edge] if edge in values else values[edge[::-1]]

    def ec(edge, component):
        edge = tuple(sorted(edge))
        return pc.rj.edge_components(edge, incidence[edge], faces, q, centroid)[component]

    targets = [
        ("S228_264_246_via_246_228", fc([228, 264, 246], (246, 228))),
        ("U228_via_251", pc.rj.vertex_support(228, 251, q, centroid)),
        ("U231_via_232", pc.rj.vertex_support(231, 232, q, centroid)),
        ("U246_via_245", pc.rj.vertex_support(246, 245, q, centroid)),
        ("H8_246_via_t", ec((8, 246), "t")),
        ("H228_254_via_beta2", ec((228, 254), "beta2")),
        ("H231_247_via_beta1", ec((231, 247), "beta1")),
        ("H236_237_via_beta1", ec((236, 237), "beta1")),
    ]
    assert tuple(name for name, _jet in targets) == TARGET_NAMES
    base_face = pc.esc.face_by_vertices(faces, BASE)
    base = [
        (f"S_base_via_{a}_{b}", value)
        for (a, b), value in pc.rj.face_components(base_face, q, centroid)
    ]
    neighbors = sorted({b if a == 8 else a for a, b in incidence if 8 in (a, b)})
    u8 = [
        (f"U8_via_{neighbor}", pc.rj.vertex_support(8, neighbor, q, centroid))
        for neighbor in neighbors
    ]
    assert len(base) == 17 and len(u8) == 13
    return base + u8, targets


def compare_jets(expected, actual):
    assert len(expected) == len(actual)
    for record, (name, jet) in zip(expected, actual):
        assert record["name"] == name
        assert Q(record["value_exact"]) == jet.v
        assert tuple(Q(value) for value in record["gradient_exact"]) == jet.d
        assert len(jet.d) == 156
        assert record["gradient_nonzero_count"] == sum(value != 0 for value in jet.d) == 156


def padd(a, b):
    size = max(len(a), len(b))
    out = [Q(0)] * size
    for index in range(size):
        out[index] = (a[index] if index < len(a) else 0) + (b[index] if index < len(b) else 0)
    while len(out) > 1 and out[-1] == 0:
        out.pop()
    return tuple(out)


def pneg(a):
    return tuple(-value for value in a)


def psub(a, b):
    return padd(a, pneg(b))


def pmul(a, b):
    out = [Q(0)] * (len(a) + len(b) - 1)
    for i, left in enumerate(a):
        for j, right in enumerate(b):
            out[i + j] += left * right
    while len(out) > 1 and out[-1] == 0:
        out.pop()
    return tuple(out)


def vadd(a, b):
    return tuple(padd(a[k], b[k]) for k in range(3))


def vsub(a, b):
    return tuple(psub(a[k], b[k]) for k in range(3))


def vscale(a, t):
    return tuple(pmul(a[k], t) for k in range(3))


def vcross(a, b):
    return (
        psub(pmul(a[1], b[2]), pmul(a[2], b[1])),
        psub(pmul(a[2], b[0]), pmul(a[0], b[2])),
        psub(pmul(a[0], b[1]), pmul(a[1], b[0])),
    )


def vdot(a, b):
    return padd(padd(pmul(a[0], b[0]), pmul(a[1], b[1])), pmul(a[2], b[2]))


def dense_planarity_test(rows, modes, polygon, prefix):
    direction = [Q((index * 37) % 101 + 1, (index * 13) % 29 + 31) for index in range(156)]
    by_name = {mode["name"]: direction[index] for index, mode in enumerate(modes)}
    frame_paths = {}
    for role, label in zip("abc", polygon["frame"]):
        frame_paths[role] = tuple(
            (rows[label][axis], by_name[f"{prefix}_frame_{role}{label}_{axis_name}"])
            for axis, axis_name in enumerate("xyz")
        )
    a, b, c = frame_paths["a"], frame_paths["b"], frame_paths["c"]
    path = {label: frame_paths[role] for role, label in zip("abc", polygon["frame"])}
    for label, (alpha, beta) in polygon["affine"].items():
        alpha_path = (alpha, by_name[f"{prefix}_r{label}_alpha"])
        beta_path = (beta, by_name[f"{prefix}_r{label}_beta"])
        path[label] = vadd(a, vadd(vscale(vsub(b, a), alpha_path), vscale(vsub(c, a), beta_path)))
        assert max(len(component) for component in path[label]) <= 3
    normal = vcross(vsub(b, a), vsub(c, a))
    for label in polygon["dependent"]:
        assert vdot(normal, vsub(path[label], a)) == (Q(0),)
    return {
        "tested_direction_nonzero_coordinates": len(direction),
        "dependent_rows_checked": len(polygon["dependent"]),
        "maximum_coordinate_degree": 2,
        "all_coplanarity_determinants_identically_zero": True,
    }


def main():
    payload = json.loads(CHART.read_text())
    assert payload["verdict"] == "EXACT_POST_C17_NONLINEAR_156D_CHART_PASS"
    for relative, expected in payload["source_hashes"].items():
        assert sha256(ATTACK / relative) == expected
    ledger, rows, faces = load_endpoint()
    modes, base, shell, free = reconstruct_modes(rows, tuple(ledger["active_vertices"]))
    assert payload["chart"]["dimension"] == 156
    assert payload["chart"]["ambient_active_coordinate_count"] == 183
    assert payload["chart"]["coplanarity_codimension"] == 27
    assert payload["chart"]["base"]["frame"] == list(base["frame"])
    assert payload["chart"]["shell"]["frame"] == list(shell["frame"])
    assert payload["chart"]["base"]["dimension"] == 37
    assert payload["chart"]["shell"]["dimension"] == 35
    assert payload["chart"]["free_active_rows"] == list(free)
    assert payload["chart"]["modes"] == [mode_json(mode) for mode in modes]

    protected, targets = reconstruct_jets(rows, faces, modes)
    dense = payload["dense_exact_jets"]
    compare_jets(dense["P"], protected)
    compare_jets(dense["T"], targets)
    p_rank = pc.rj.matrix_rank([jet.d for _name, jet in protected])
    t_rank = pc.rj.matrix_rank([jet.d for _name, jet in targets])
    combined_rank = pc.rj.matrix_rank([jet.d for _name, jet in protected + targets])
    assert [p_rank, t_rank, combined_rank] == [30, 8, 38]
    assert [dense["P_rank"], dense["T_rank"], dense["P_then_T_rank"]] == [30, 8, 38]

    planarity = {
        "base": dense_planarity_test(rows, modes, base, "base"),
        "shell": dense_planarity_test(rows, modes, shell, "shell"),
    }
    result = {
        "version": 1,
        "scope": "independent reconstruction of nonlinear chart and exact dense jets",
        "source_hashes": {
            "nonlinear_chart.json": sha256(CHART),
            "cells/endpoint.csv": sha256(ATTACK / "cells" / "endpoint.csv"),
            "cells/endpoint.json": sha256(ATTACK / "cells" / "endpoint.json"),
        },
        "endpoint": {"f_vector": [61, 150, 91], "class": [2, 4, 4]},
        "chart": {
            "dimension": len(modes),
            "base_dimension": 9 + 2 * len(base["dependent"]),
            "shell_dimension": 9 + 2 * len(shell["dependent"]),
            "free_dimension": 3 * len(free),
            "local_inverse": "moving frame vertices, affine coordinates, and free rows",
            "moving_plane_quotient_dimension_over_fixed_plane_chart": 6,
        },
        "planarity": planarity,
        "dense_jet_nonzero_counts": {
            "P": [sum(value != 0 for value in jet.d) for _name, jet in protected],
            "T": [sum(value != 0 for value in jet.d) for _name, jet in targets],
        },
        "exact_ranks": {"P": p_rank, "T": t_rank, "P_then_T": combined_rank},
        "all_37_forced_rails_present_at_source": True,
        "verdict": "INDEPENDENT_EXACT_POST_C17_NONLINEAR_156D_CHART_PASS",
        "winner_status": "NONWINNER_CHART_ONLY",
        "obstruction_status": "NONE_CLAIMED",
    }
    OUTPUT.write_text(json.dumps(result, indent=2) + "\n")
    print(result["verdict"])
    print("dimension", len(modes))
    print("ranks", p_rank, t_rank, combined_rank)
    print("output_sha256", sha256(OUTPUT))


if __name__ == "__main__":
    main()
