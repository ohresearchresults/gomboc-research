#!/usr/bin/env python3
"""Build the full rational nonlinear coplanarity chart at the frozen endpoint.

Each polygon uses three moving frame vertices and two affine coordinates for
every remaining vertex.  The chart map is polynomial of degree two and keeps
both polygon faces coplanar identically.  The 28 remaining active rows move
freely in R^3, giving 37 + 35 + 84 = 156 exact local coordinates.

This file only builds the chart and its first jets.  It is not a finite-path
certificate and it makes no winner or obstruction claim.
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
OUTPUT = HERE / "nonlinear_chart.json"
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


def vector_record(vector):
    return [pc.qs(value) for value in vector]


def load_frozen_endpoint():
    ledger_path = ATTACK / "cells" / "endpoint.json"
    rows_path = ATTACK / "cells" / "endpoint.csv"
    ledger = json.loads(ledger_path.read_text())
    rows = pc.read_rows(rows_path)
    faces = pc.ex.exactify_faces(
        rows,
        SimpleNamespace(
            faces=[{"cycle": list(cycle)} for cycle in ledger["maximal_face_cycles"]]
        ),
    )
    volume, centroid = pc.ex.exact_mass(rows, faces)
    ef, active, fl, vl, el, stable, unstable, saddles = pc.ex.exact_mechanics(
        rows, faces, centroid
    )
    assert [len(active), len(ef), len(faces)] == ledger["f_vector"] == [61, 150, 91]
    assert [len(stable), len(unstable), len(saddles)] == ledger["class"] == [2, 4, 4]
    assert active == ledger["active_vertices"]
    assert [faces[index]["cycle"] for index in stable] == ledger["stable_faces"]
    assert unstable == ledger["unstable_vertices"]
    assert [list(edge) for edge in saddles] == ledger["saddle_edges"]
    assert sorted(ef) == [tuple(edge) for edge in ledger["true_edges"]]
    assert fl == ledger["face_mechanics_ledger"]
    assert vl == ledger["vertex_mechanics_ledger"]
    assert el == ledger["edge_mechanics_ledger"]
    assert pc.qs(volume) == ledger["volume_exact"]
    assert [pc.qs(value) for value in centroid] == ledger["centroid_exact"]
    assert not (pc.esc.forced_rails() - set(ef))
    return ledger, rows, faces


def area_squared(rows, triple):
    a, b, c = (rows[label] for label in triple)
    normal = pc.ex.cross(pc.ex.sub(b, a), pc.ex.sub(c, a))
    return pc.ex.dot(normal, normal)


def select_frame(rows, cycle):
    scored = [(area_squared(rows, triple), triple) for triple in itertools.combinations(cycle, 3)]
    best_area = max(area for area, _triple in scored)
    frame = min(triple for area, triple in scored if area == best_area)
    assert best_area > 0
    return frame, best_area


def affine_coordinates(point, origin, u, v):
    w = pc.ex.sub(point, origin)
    uu = pc.ex.dot(u, u)
    uv = pc.ex.dot(u, v)
    vv = pc.ex.dot(v, v)
    wu = pc.ex.dot(w, u)
    wv = pc.ex.dot(w, v)
    determinant = uu * vv - uv * uv
    assert determinant > 0
    alpha = (wu * vv - wv * uv) / determinant
    beta = (wv * uu - wu * uv) / determinant
    assert point == pc.ex.add(origin, pc.ex.add(pc.ex.mul(u, alpha), pc.ex.mul(v, beta)))
    return alpha, beta


def axis_vector(axis, scale=Q(1)):
    return tuple(scale if offset == axis else Q(0) for offset in range(3))


def add_mode(modes, name, family, deltas):
    clean = {label: tuple(vector) for label, vector in deltas.items() if vector != pc.ex.ZERO}
    assert clean
    modes.append({"name": name, "family": family, "deltas": clean})


def polygon_chart(rows, cycle, prefix, modes):
    frame, frame_area = select_frame(rows, cycle)
    a_label, b_label, c_label = frame
    origin = rows[a_label]
    u = pc.ex.sub(rows[b_label], origin)
    v = pc.ex.sub(rows[c_label], origin)
    dependent = tuple(label for label in cycle if label not in frame)
    coordinates = {
        label: affine_coordinates(rows[label], origin, u, v) for label in dependent
    }

    for frame_role, frame_label in zip("abc", frame):
        for axis, axis_name in enumerate("xyz"):
            deltas = {frame_label: axis_vector(axis)}
            for label in dependent:
                alpha, beta = coordinates[label]
                weight = {
                    "a": Q(1) - alpha - beta,
                    "b": alpha,
                    "c": beta,
                }[frame_role]
                if weight:
                    deltas[label] = axis_vector(axis, weight)
            add_mode(
                modes,
                f"{prefix}_frame_{frame_role}{frame_label}_{axis_name}",
                f"{prefix}_moving_frame",
                deltas,
            )

    for label in dependent:
        add_mode(
            modes,
            f"{prefix}_r{label}_alpha",
            f"{prefix}_affine_coordinate",
            {label: u},
        )
        add_mode(
            modes,
            f"{prefix}_r{label}_beta",
            f"{prefix}_affine_coordinate",
            {label: v},
        )

    assert len(frame) == 3 and len(dependent) == len(cycle) - 3
    return {
        "cycle": list(cycle),
        "frame": list(frame),
        "frame_area_squared_exact": pc.qs(frame_area),
        "dependent_rows": list(dependent),
        "affine_coordinates_exact": {
            str(label): [pc.qs(alpha), pc.qs(beta)]
            for label, (alpha, beta) in coordinates.items()
        },
        "dimension": 9 + 2 * len(dependent),
        "formula": (
            "A'=A+dA; B'=B+dB; C'=C+dC; "
            "q_i'=A'+(alpha_i+s_i)(B'-A')+(beta_i+t_i)(C'-A')"
        ),
        "polynomial_degree": 2,
    }


def build_modes(rows, active):
    modes = []
    base = polygon_chart(rows, BASE, "base", modes)
    shell = polygon_chart(rows, SHELL, "shell", modes)
    other = tuple(sorted(set(active) - set(BASE) - set(SHELL)))
    assert len(other) == 28
    for label in other:
        for axis, axis_name in enumerate("xyz"):
            add_mode(
                modes,
                f"free_r{label}_{axis_name}",
                "free_active_row",
                {label: axis_vector(axis)},
            )
    assert base["dimension"] == 37
    assert shell["dimension"] == 35
    assert len(modes) == 37 + 35 + 3 * len(other) == 156
    assert len({mode["name"] for mode in modes}) == len(modes)
    return modes, base, shell, other


def verify_structural_independence(rows, modes, base, shell, other):
    by_name = {mode["name"]: mode for mode in modes}
    assert len(by_name) == len(modes)
    for polygon, prefix in ((base, "base"), (shell, "shell")):
        a, b, c = polygon["frame"]
        for role, label in zip("abc", (a, b, c)):
            for axis, axis_name in enumerate("xyz"):
                mode = by_name[f"{prefix}_frame_{role}{label}_{axis_name}"]
                assert mode["deltas"].get(label) == axis_vector(axis)
                for other_frame in set((a, b, c)) - {label}:
                    assert other_frame not in mode["deltas"]
        origin = rows[a]
        u = pc.ex.sub(rows[b], origin)
        v = pc.ex.sub(rows[c], origin)
        assert pc.ex.cross(u, v) != pc.ex.ZERO
        for label in polygon["dependent_rows"]:
            alpha_mode = by_name[f"{prefix}_r{label}_alpha"]
            beta_mode = by_name[f"{prefix}_r{label}_beta"]
            assert alpha_mode["deltas"] == {label: u}
            assert beta_mode["deltas"] == {label: v}
    for label in other:
        assert tuple(
            by_name[f"free_r{label}_{axis}"]["deltas"][label]
            for axis in "xyz"
        ) == tuple(axis_vector(offset) for offset in range(3))
    return len(modes)


def make_jets(rows, faces, modes):
    pc.rj.M = len(modes)
    by_row = defaultdict(list)
    for column, mode in enumerate(modes):
        for label, vector in mode["deltas"].items():
            by_row[label].append((column, vector))
    q = {}
    for label, point in rows.items():
        xyz = []
        for axis in range(3):
            derivative = [Q(0)] * len(modes)
            for column, vector in by_row.get(label, ()):
                derivative[column] = vector[axis]
            xyz.append(pc.rj.J(point[axis], tuple(derivative)))
        q[label] = tuple(xyz)
    centroid, _volume = pc.rj.exact_centroid(q, faces)
    return q, centroid


def mechanics_jets(rows, faces, modes):
    q, centroid = make_jets(rows, faces, modes)
    incidence = pc.esc.incidence(faces)

    def face_component(vertices, edge):
        face = pc.esc.face_by_vertices(faces, vertices)
        values = dict(pc.rj.face_components(face, q, centroid))
        return values[edge] if edge in values else values[edge[::-1]]

    def edge_component(edge, component):
        edge = tuple(sorted(edge))
        return pc.rj.edge_components(edge, incidence[edge], faces, q, centroid)[component]

    targets = {
        "S228_264_246_via_246_228": face_component([228, 264, 246], (246, 228)),
        "U228_via_251": pc.rj.vertex_support(228, 251, q, centroid),
        "U231_via_232": pc.rj.vertex_support(231, 232, q, centroid),
        "U246_via_245": pc.rj.vertex_support(246, 245, q, centroid),
        "H8_246_via_t": edge_component((8, 246), "t"),
        "H228_254_via_beta2": edge_component((228, 254), "beta2"),
        "H231_247_via_beta1": edge_component((231, 247), "beta1"),
        "H236_237_via_beta1": edge_component((236, 237), "beta1"),
    }
    assert tuple(targets) == TARGET_NAMES

    base_face = pc.esc.face_by_vertices(faces, BASE)
    base_components = list(pc.rj.face_components(base_face, q, centroid))
    neighbors = sorted({b if a == 8 else a for a, b in incidence if 8 in (a, b)})
    u8_components = [
        (neighbor, pc.rj.vertex_support(8, neighbor, q, centroid))
        for neighbor in neighbors
    ]
    protected = [
        (f"S_base_via_{a}_{b}", value) for (a, b), value in base_components
    ] + [
        (f"U8_via_{neighbor}", value) for neighbor, value in u8_components
    ]
    assert len(base_components) == 17
    assert len(u8_components) == 13
    assert len(protected) == 30
    assert all(value.v > 0 for value in targets.values())
    assert all(value.v > 0 for _name, value in protected)
    return protected, list(targets.items())


def jet_record(name, jet):
    return {
        "name": name,
        "value_exact": pc.qs(jet.v),
        "value_decimal": float(jet.v),
        "gradient_exact": [pc.qs(value) for value in jet.d],
        "gradient_nonzero_count": sum(value != 0 for value in jet.d),
    }


def mode_record(mode):
    return {
        "name": mode["name"],
        "family": mode["family"],
        "row_deltas_exact": {
            str(label): vector_record(vector)
            for label, vector in sorted(mode["deltas"].items())
        },
    }


def main():
    ledger_path = ATTACK / "cells" / "endpoint.json"
    rows_path = ATTACK / "cells" / "endpoint.csv"
    ledger, rows, faces = load_frozen_endpoint()
    active = tuple(ledger["active_vertices"])
    modes, base, shell, other = build_modes(rows, active)
    chart_rank = verify_structural_independence(rows, modes, base, shell, other)
    protected, targets = mechanics_jets(rows, faces, modes)
    p_rank = pc.rj.matrix_rank([jet.d for _name, jet in protected])
    t_rank = pc.rj.matrix_rank([jet.d for _name, jet in targets])
    combined_rank = pc.rj.matrix_rank(
        [jet.d for _name, jet in protected + targets]
    )
    assert chart_rank == 156
    assert p_rank == 30
    assert t_rank == 8
    assert combined_rank == 38

    payload = {
        "version": 1,
        "scope": "full 156-dimensional rational active-hull coplanarity chart",
        "source_hashes": {
            str(rows_path.relative_to(ATTACK)): sha256(rows_path),
            str(ledger_path.relative_to(ATTACK)): sha256(ledger_path),
            "certificate.json": sha256(ATTACK / "certificate.json"),
            "manifest.sha256": sha256(ATTACK / "manifest.sha256"),
        },
        "endpoint": {
            "f_vector": ledger["f_vector"],
            "class": ledger["class"],
            "active_rows": list(active),
            "stable_faces": ledger["stable_faces"],
            "unstable_vertices": ledger["unstable_vertices"],
            "saddle_edges": ledger["saddle_edges"],
            "all_37_forced_rails_present": True,
        },
        "chart": {
            "kind": "rational moving-frame affine-coordinate polynomial chart",
            "dimension": chart_rank,
            "ambient_active_coordinate_count": 3 * len(active),
            "coplanarity_codimension": (len(BASE) - 3) + (len(SHELL) - 3),
            "degree": 2,
            "base": base,
            "shell": shell,
            "free_active_rows": list(other),
            "free_active_row_dimension": 3 * len(other),
            "mode_names": [mode["name"] for mode in modes],
            "modes": [mode_record(mode) for mode in modes],
            "base_coplanarity_identical_by_formula": True,
            "shell_coplanarity_identical_by_formula": True,
            "fixed_plane_dimension": 150,
            "moving_plane_quotient_dimension": 6,
        },
        "dense_exact_jets": {
            "P_definition": "17 base-face components followed by 13 U8 support components",
            "T_definition": "eight inherited post-C17 residual equilibrium components",
            "P": [jet_record(name, jet) for name, jet in protected],
            "T": [jet_record(name, jet) for name, jet in targets],
            "gradient_length": len(modes),
            "P_rank": p_rank,
            "T_rank": t_rank,
            "P_then_T_rank": combined_rank,
        },
        "verdict": "EXACT_POST_C17_NONLINEAR_156D_CHART_PASS",
        "winner_status": "NONWINNER_CHART_ONLY",
        "obstruction_status": "NONE_CLAIMED",
    }
    OUTPUT.write_text(json.dumps(payload, indent=2) + "\n")
    print(payload["verdict"])
    print("dimension", chart_rank)
    print("P_rank", p_rank)
    print("T_rank", t_rank)
    print("P_then_T_rank", combined_rank)
    print("output_sha256", sha256(OUTPUT))


if __name__ == "__main__":
    main()
