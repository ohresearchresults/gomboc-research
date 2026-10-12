#!/usr/bin/env python3
"""Independent reconstruction of the exact Stage-31 H1011-upstream flip."""
from __future__ import annotations

import csv
import hashlib
import json
import math
import sys
from fractions import Fraction as Q
from pathlib import Path


sys.set_int_max_str_digits(0)

HERE = Path(__file__).resolve().parent
TRACK = HERE.parent
ROOT = HERE.parents[2]
sys.path.insert(0, str(TRACK / "rigorous_local_bypass"))
import exact_core as ex  # noqa: E402


SOURCE = TRACK / "stage31_attack" / "exact_relay_far.csv"
SOURCE_FACES = TRACK / "stage31_attack" / "exact_relay_faces.json"
PATH_DEFINITION = HERE / "circuit_path_definition.json"
PROPOSER_FACES = HERE / "circuit_post_faces.json"
CERTIFICATE = HERE / "exact_circuit_certificate.json"
GENERATED = {
    "source": HERE / "exact_circuit_source.csv",
    "pre": HERE / "exact_circuit_pre.csv",
    "post": HERE / "exact_circuit_post.csv",
    "far": HERE / "exact_circuit_far.csv",
    "pre_faces": HERE / "exact_circuit_pre_faces.json",
    "wall_faces": HERE / "exact_circuit_wall_faces.json",
    "post_faces": HERE / "exact_circuit_post_faces.json",
}

BASE = frozenset(range(17)) | {54}
PRIMARY = (7, 8, 245)
TARGET_CIRCUIT = (8, 9, 263, 264)
REMOVED_FACE_SETS = {tuple(sorted((8, 9, 264))), tuple(sorted((9, 263, 264)))}
ADDED_FACES = [[8, 9, 263], [8, 263, 264]]
WALL_FACE = [8, 9, 263, 264]
ROOT_WIDTH = Q(1, 10**24)
EXPECTED_ACTIVE = [
    0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16,
    54, 69, 72, 73, 88, 198, 224, 228, 229, 230, 231, 232, 233,
    234, 235, 236, 237, 238, 239, 240, 241, 242, 243, 244, 245,
    246, 247, 248, 249, 250, 251, 252, 253, 254, 255, 256, 257,
    258, 259, 260, 261, 262, 263, 264,
]
PROTECTED = {
    "stable": [sorted(BASE), list(PRIMARY)],
    "unstable": [8, 54],
    "saddles": [[5, 6], [10, 11]],
}
SELECTED = {
    "S": (8, 245),
    "U54": 1,
    "H56": "one_minus_t",
    "H1011": "t",
}


def sha256(path: Path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def canonical_hash(value):
    return hashlib.sha256(
        json.dumps(value, sort_keys=True, separators=(",", ":")).encode()
    ).hexdigest()


def eval_path(path, parameter):
    return {
        label: tuple(coordinate.eval(parameter) for coordinate in xyz)
        for label, xyz in path.items()
    }


def restrict(path, lo, hi):
    return {
        label: tuple(coordinate.affine(lo, hi) for coordinate in xyz)
        for label, xyz in path.items()
    }


def face_sets(faces):
    return {tuple(sorted(face)) for face in faces}


def edge_set(faces):
    return {
        tuple(sorted((a, b)))
        for cycle in faces
        for a, b in zip(cycle, cycle[1:] + cycle[:1])
    }


def forced_rails():
    rails = set()
    for route in (
        [228] + list(range(229, 247)) + [8],
        [228] + list(range(247, 265)) + [8],
    ):
        rails.update(tuple(sorted(edge)) for edge in zip(route, route[1:]))
    rails.remove((228, 229))
    return rails


def make_face_ledgers():
    pre = json.loads(SOURCE_FACES.read_text())
    kept = [face for face in pre if tuple(sorted(face)) not in REMOVED_FACE_SETS]
    assert len(pre) - len(kept) == 2
    post = kept + ADDED_FACES
    wall = kept + [WALL_FACE]
    assert face_sets(json.loads(PROPOSER_FACES.read_text())) == face_sets(post)
    return pre, wall, post


def primitive_rows(points, faces):
    ledger = ex.mechanics_primitives(points, faces)
    yield "volume_d6", ledger["d6"]
    for face_key, rows in sorted(ledger["reference"].items()):
        for edge, value in sorted(rows.items()):
            yield f"face_reference:{face_key}:{edge}", value
    for face_key, rows in sorted(ledger["face"].items()):
        for edge, value in sorted(rows.items()):
            yield f"face_raw:{face_key}:{edge}", value
    for vertex, rows in sorted(ledger["vertex"].items()):
        for neighbor, value in sorted(rows.items()):
            yield f"vertex:{vertex}:{neighbor}", value
    for edge, rows in sorted(ledger["edge"].items()):
        for component in (
            "direction_norm2", "gram", "t", "one_minus_t", "beta1", "beta2"
        ):
            yield f"edge:{edge}:{component}", rows[component]


def checkpoint(points, faces):
    support = ex.supporting_cell(points, faces)
    _ledger, mechanics = ex.classify_point(points, faces)
    assert support["f_vector"] == [61, 162, 103]
    assert support["active_labels"] == EXPECTED_ACTIVE
    assert mechanics["class"] == [2, 2, 2]
    assert BASE in {frozenset(face) for face in faces}
    assert forced_rails().issubset(set(support["edges"]))
    d6, m24 = ex.exact_centroid_numerators(points, faces)
    centroid = tuple(value / (4 * d6) for value in m24)
    rows = list(primitive_rows(points, faces))
    assert all(value for _name, value in rows)
    digest = hashlib.sha256()
    for name, value in rows:
        digest.update(f"{name}|{ex.qs(value)}\n".encode())
    return {
        "coordinate_hash": canonical_hash({
            str(label): [ex.qs(x) for x in points[label]] for label in sorted(points)
        }),
        "exact_centroid": [ex.qs(value) for value in centroid],
        "exact_support": {key: value for key, value in support.items() if key != "edges"},
        "exact_mechanics": mechanics,
        "mechanics_primitive_count": len(rows),
        "mechanics_minimum_log10_abs": min(ex.qlog10(value) for _, value in rows),
        "mechanics_digest": digest.hexdigest(),
        "base_face_present": True,
        "forced_rail_count": len(forced_rails()),
        "missing_forced_rails": [],
    }


def edge_fractions(points, faces, edge):
    ledger = ex.mechanics_primitives(points, faces)
    component = ledger["edge"][edge]
    scale = 4 * ledger["d6"]
    i, j = edge
    direction = ex.sub(points[j], points[i])
    dd = component["direction_norm2"]
    closest = ex.add(
        ex.mul(ledger["xscaled"][i], dd),
        ex.mul(direction, component["t"]),
    )
    closest_norm2 = ex.norm2(closest)
    aa = ex.norm2(component["n1"])
    cc = ex.norm2(component["n2"])
    gram2 = component["gram"] * component["gram"]
    common_denominator = scale * scale * dd * dd
    return {
        "t": (component["t"] * component["t"], common_denominator),
        "one_minus_t": (
            component["one_minus_t"] * component["one_minus_t"],
            common_denominator,
        ),
        "beta1": (
            component["beta1"] * component["beta1"] * dd * dd * aa,
            gram2 * closest_norm2,
        ),
        "beta2": (
            component["beta2"] * component["beta2"] * dd * dd * cc,
            gram2 * closest_norm2,
        ),
    }


def fractions(points, faces, name):
    ledger = ex.mechanics_primitives(points, faces)
    scale = 4 * ledger["d6"]
    if name == "S":
        cycle = faces[ledger["face_by_key"][PRIMARY]]
        nn = ex.norm2(ex.cycle_normal(cycle, points))
        rows = {}
        for edge, raw in ex.signed_face_components(ledger, PRIMARY).items():
            dd = ex.norm2(ex.sub(points[edge[1]], points[edge[0]]))
            rows[edge] = (raw * raw, scale * scale * dd * nn * nn * nn)
        return rows
    if name == "U54":
        xx = ex.norm2(ledger["xscaled"][54])
        return {
            neighbor: (
                raw * raw,
                xx * ex.norm2(ex.sub(points[neighbor], points[54])),
            )
            for neighbor, raw in ledger["vertex"][54].items()
        }
    return edge_fractions(points, faces, (5, 6) if name == "H56" else (10, 11))


def residual_record(points, faces, name):
    rows = fractions(points, faces, name)
    selected = SELECTED[name]
    values = {key: numerator / denominator for key, (numerator, denominator) in rows.items()}
    assert min(values, key=values.get) == selected
    numerator, denominator = rows[selected]
    value = numerator / denominator
    differences = {
        str(key): ex.qs(values[key] - value) for key in rows if key != selected
    }
    assert all(Q(item) > 0 for item in differences.values())
    return {
        "numerator": ex.qs(numerator),
        "denominator": ex.qs(denominator),
        "squared_value": ex.qs(value),
        "decision_value": math.sqrt(float(value)),
        "selected_component": list(selected) if isinstance(selected, tuple) else selected,
        "strict_minimum_against": differences,
    }


def direction_audit(path, pre_faces, post_faces, root, end):
    source = eval_path(path, Q(0))
    far = eval_path(path, end)
    result = {}
    for name in SELECTED:
        source_record = residual_record(source, pre_faces, name)
        far_record = residual_record(far, post_faces, name)
        source_value = Q(source_record["squared_value"])
        far_value = Q(far_record["squared_value"])
        assert far_value < source_value
        segments = {}
        for segment, faces_here, lo, hi in (
            ("pre", pre_faces, Q(0), root["lo"]),
            ("post", post_faces, root["hi"], end),
        ):
            numerator, denominator = fractions(path, faces_here, name)[SELECTED[name]]
            derivative = numerator.derivative() * denominator - numerator * denominator.derivative()
            sign, leaves, worst = ex.bernstein_sign(derivative, lo, hi, max_depth=60)
            segments[segment] = {
                "derivative_sign": sign,
                "bernstein_leaf_count": leaves,
                "minimum_bernstein_log10_abs": worst,
                "derivative_numerator_degree": derivative.degree,
                "derivative_numerator_digest": canonical_hash(derivative.exact()),
            }
        result[name] = {
            "source": source_record,
            "far": far_record,
            "strict_endpoint_improvement": True,
            "exact_squared_drop": ex.qs(source_value - far_value),
            "piecewise_derivative": segments,
        }
    return result


def assert_csv(path, expected):
    assert ex.read_rows(path) == expected


def main():
    frozen = json.loads(CERTIFICATE.read_text())
    assert frozen["verdict"] == "EXACT_STAGE31_H1011_UPSTREAM_CIRCUIT_FLIP_PASS"
    definition = json.loads(PATH_DEFINITION.read_text())
    assert definition["verdict"] == "DIRECTED_STAGE31_H1011_LOCAL_CIRCUIT_PROPOSAL_PASS"
    source = ex.read_rows(SOURCE)
    velocity = {
        int(label): tuple(Q(value) for value in xyz)
        for label, xyz in definition["velocity"].items()
    }
    path = {
        label: tuple(
            ex.P((source[label][axis], velocity[label][axis]))
            for axis in range(3)
        )
        for label in source
    }
    end = Q(definition["end_parameter"])
    pre_faces, wall_faces, post_faces = make_face_ledgers()

    for file in (SOURCE, SOURCE_FACES, PATH_DEFINITION, PROPOSER_FACES):
        key = str(file.relative_to(ROOT))
        assert sha256(file) == frozen["source_hashes"][key]
    assert canonical_hash({
        str(label): [ex.qs(x) for x in velocity[label]] for label in sorted(velocity)
    }) == frozen["path"]["velocity_digest"]

    polynomial = ex.circuit_polynomial(path, TARGET_CIRCUIT)
    root = ex.isolate_monotone_root(
        polynomial, Q(5701, 10**9), Q(5703, 10**9), ROOT_WIDTH
    )
    stored_root = frozen["path"]["target_polynomial"]
    assert polynomial.exact() == stored_root["polynomial_exact"]
    assert canonical_hash(polynomial.exact()) == stored_root["polynomial_digest"]
    for key in ("lo", "hi", "value_lo", "value_hi"):
        assert ex.qs(root[key]) == stored_root[key]
    assert root["derivative_sign"] == stored_root["derivative_sign"] == -1
    assert Q(0) < root["lo"] <= root["hi"] < end

    first_wall = ex.certify_first_support_wall(path, pre_faces, root, polynomial)
    assert first_wall == frozen["path"]["first_support_wall"]
    assert ex.certify_path_segment(
        restrict(path, Q(0), root["lo"]), pre_faces, PROTECTED
    ) == frozen["open_cells"]["pre"]
    assert ex.certify_path_segment(
        restrict(path, root["hi"], end), post_faces, PROTECTED
    ) == frozen["open_cells"]["post"]
    assert ex.certify_mechanics_interval(
        path, wall_faces, PROTECTED, root["lo"], root["hi"]
    ) == frozen["open_cells"]["wall_mechanics"]

    pre_edges, wall_edges, post_edges = map(edge_set, (pre_faces, wall_faces, post_faces))
    assert pre_edges - post_edges == {(9, 264)}
    assert post_edges - pre_edges == {(8, 263)}
    assert [61, len(wall_edges), len(wall_faces)] == [61, 161, 102]
    for faces_here, edges_here in (
        (pre_faces, pre_edges), (wall_faces, wall_edges), (post_faces, post_edges)
    ):
        assert BASE in {frozenset(face) for face in faces_here}
        assert forced_rails().issubset(edges_here)
    assert frozen["topology_event"] == {
        "pre_f_vector": [61, 162, 103],
        "wall_f_vector": [61, 161, 102],
        "post_f_vector": [61, 162, 103],
        "removed_maximal_faces": [[8, 9, 264], [9, 263, 264]],
        "wall_maximal_face": [8, 9, 263, 264],
        "added_maximal_faces": [[8, 9, 263], [8, 263, 264]],
        "removed_true_edge": [9, 264],
        "added_true_edge": [8, 263],
        "pre_edge_count": 162,
        "wall_edge_count": 161,
        "post_edge_count": 162,
        "base_preserved": True,
        "forced_rails_preserved": 37,
    }

    parameters = {
        name: Q(value) for name, value in frozen["rational_parameters"].items()
    }
    assert parameters["source"] == 0
    assert parameters["pre"] < root["lo"] < root["hi"] < parameters["post"] < parameters["far"]
    assert parameters["far"] == end
    faces_for = {
        "source": pre_faces, "pre": pre_faces,
        "post": post_faces, "far": post_faces,
    }
    points_for = {name: eval_path(path, parameter) for name, parameter in parameters.items()}
    for name, points in points_for.items():
        assert checkpoint(points, faces_for[name]) == frozen["rational_checkpoints"][name]
        assert_csv(GENERATED[name], points)
    assert json.loads(GENERATED["pre_faces"].read_text()) == pre_faces
    assert json.loads(GENERATED["wall_faces"].read_text()) == wall_faces
    assert json.loads(GENERATED["post_faces"].read_text()) == post_faces

    actual_direction = direction_audit(path, pre_faces, post_faces, root, end)
    assert actual_direction == frozen["directed_residuals"]
    for name in SELECTED:
        assert actual_direction[name]["strict_endpoint_improvement"]

    for file in GENERATED.values():
        key = str(file.relative_to(ROOT))
        assert sha256(file) == frozen["generated_file_sha256"][key]
    assert frozen["residual_verdict"] == {
        "winner": False,
        "far_class": [2, 2, 2],
        "remaining_extra_stable": [7, 8, 245],
        "remaining_extra_unstable": 54,
        "remaining_saddles": [[5, 6], [10, 11]],
        "interpretation": (
            "The first coupled event is an exact shell diagonal flip "
            "(9,264)->(8,263). It opens a new H1011 cell and strictly "
            "improves all four normalized endpoint residuals, but kills no "
            "equilibrium at the certified far checkpoint."
        ),
    }
    print("INDEPENDENT_EXACT_STAGE31_H1011_UPSTREAM_CIRCUIT_FLIP_PASS")


if __name__ == "__main__":
    main()
