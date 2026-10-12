#!/usr/bin/env python3
"""Build an exact certificate for the first Stage-31 H1011-upstream flip."""
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
EXACT_DIR = TRACK / "rigorous_local_bypass"
sys.path.insert(0, str(EXACT_DIR))
import exact_core as ex  # noqa: E402


SOURCE = TRACK / "stage31_attack" / "exact_relay_far.csv"
SOURCE_FACES = TRACK / "stage31_attack" / "exact_relay_faces.json"
PATH_DEFINITION = HERE / "circuit_path_definition.json"
PROPOSER_FACES = HERE / "circuit_post_faces.json"
CERTIFICATE = HERE / "exact_circuit_certificate.json"
SOURCE_OUT = HERE / "exact_circuit_source.csv"
PRE_OUT = HERE / "exact_circuit_pre.csv"
POST_OUT = HERE / "exact_circuit_post.csv"
FAR_OUT = HERE / "exact_circuit_far.csv"
PRE_FACES_OUT = HERE / "exact_circuit_pre_faces.json"
WALL_FACES_OUT = HERE / "exact_circuit_wall_faces.json"
POST_FACES_OUT = HERE / "exact_circuit_post_faces.json"

BASE = frozenset(range(17)) | {54}
PRIMARY = (7, 8, 245)
TARGET_CIRCUIT = (8, 9, 263, 264)
REMOVED_FACES = ((8, 9, 264), (9, 263, 264))
ADDED_FACES = ((8, 9, 263), (8, 263, 264))
WALL_FACE = (8, 9, 263, 264)
REMOVED_DIAGONAL = (9, 264)
ADDED_DIAGONAL = (8, 263)
EXPECTED_F_VECTOR = [61, 162, 103]
EXPECTED_WALL_F_VECTOR = [61, 161, 102]
EXPECTED_ACTIVE = [
    0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16,
    54, 69, 72, 73, 88, 198, 224, 228, 229, 230, 231, 232, 233,
    234, 235, 236, 237, 238, 239, 240, 241, 242, 243, 244, 245,
    246, 247, 248, 249, 250, 251, 252, 253, 254, 255, 256, 257,
    258, 259, 260, 261, 262, 263, 264,
]
ROOT_WIDTH = Q(1, 10**24)
PROTECTED = {
    "stable": [sorted(BASE), list(PRIMARY)],
    "unstable": [8, 54],
    "saddles": [[5, 6], [10, 11]],
}
SELECTED_COMPONENTS = {
    "S": [8, 245],
    "U54": 1,
    "H56": "one_minus_t",
    "H1011": "t",
}


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def canonical_hash(value) -> str:
    return hashlib.sha256(
        json.dumps(value, sort_keys=True, separators=(",", ":")).encode()
    ).hexdigest()


def write_exact_csv(path: Path, rows) -> None:
    with path.open("w", newline="") as handle:
        writer = csv.writer(handle)
        writer.writerow(("source_id", "x", "y", "z"))
        for label in sorted(rows):
            writer.writerow([label, *[ex.qs(value) for value in rows[label]]])


def evaluate_path(path, parameter: Q):
    return {
        label: tuple(coordinate.eval(parameter) for coordinate in xyz)
        for label, xyz in path.items()
    }


def restrict_path(path, lo: Q, hi: Q):
    return {
        label: tuple(coordinate.affine(lo, hi) for coordinate in xyz)
        for label, xyz in path.items()
    }


def forced_rails():
    routes = (
        [228] + list(range(229, 247)) + [8],
        [228] + list(range(247, 265)) + [8],
    )
    rails = {
        tuple(sorted(edge))
        for route in routes
        for edge in zip(route, route[1:])
    }
    rails.remove((228, 229))
    return rails


def edge_set(faces):
    return {
        tuple(sorted((a, b)))
        for cycle in faces
        for a, b in zip(cycle, cycle[1:] + cycle[:1])
    }


def face_sets(faces):
    return {tuple(sorted(face)) for face in faces}


def build_face_ledgers(pre_faces):
    removed = {tuple(sorted(face)) for face in REMOVED_FACES}
    kept = [face for face in pre_faces if tuple(sorted(face)) not in removed]
    if len(pre_faces) - len(kept) != 2:
        raise AssertionError("pre flip faces missing")
    post_faces = kept + [list(face) for face in ADDED_FACES]
    wall_faces = kept + [list(WALL_FACE)]
    proposer = json.loads(PROPOSER_FACES.read_text())
    if face_sets(proposer) != face_sets(post_faces):
        raise AssertionError("fresh-hull proposer and exact post ledger differ")
    return pre_faces, wall_faces, post_faces


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


def exact_checkpoint(points, faces, expected_class):
    support = ex.supporting_cell(points, faces)
    _ledger, mechanics = ex.classify_point(points, faces)
    if support["f_vector"] != EXPECTED_F_VECTOR:
        raise AssertionError(support)
    if support["active_labels"] != EXPECTED_ACTIVE:
        raise AssertionError(("active labels", support["active_labels"]))
    if mechanics["class"] != expected_class:
        raise AssertionError(mechanics)
    if BASE not in {frozenset(face) for face in faces}:
        raise AssertionError("base face absent")
    missing_rails = sorted(forced_rails() - set(support["edges"]))
    if missing_rails:
        raise AssertionError(("forced rails absent", missing_rails))
    d6, m24 = ex.exact_centroid_numerators(points, faces)
    centroid = tuple(value / (4 * d6) for value in m24)
    rows = list(primitive_rows(points, faces))
    if not all(value for _name, value in rows):
        raise AssertionError("zero checkpoint mechanics primitive")
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


def fraction_record(numerator, denominator):
    if numerator <= 0 or denominator <= 0:
        raise AssertionError((numerator, denominator))
    value = numerator / denominator
    return {
        "numerator": ex.qs(numerator),
        "denominator": ex.qs(denominator),
        "squared_value": ex.qs(value),
        "decision_value": math.sqrt(float(value)),
    }


def edge_fraction_map(points, faces, edge):
    ledger = ex.mechanics_primitives(points, faces)
    scale = 4 * ledger["d6"]
    component = ledger["edge"][edge]
    i, j = edge
    direction = ex.sub(points[j], points[i])
    dd = component["direction_norm2"]
    closest_numerator = ex.add(
        ex.mul(ledger["xscaled"][i], dd),
        ex.mul(direction, component["t"]),
    )
    closest_norm2 = ex.norm2(closest_numerator)
    aa = ex.norm2(component["n1"])
    cc = ex.norm2(component["n2"])
    gram2 = component["gram"] * component["gram"]
    return {
        "t": (
            component["t"] * component["t"],
            scale * scale * dd * dd,
        ),
        "one_minus_t": (
            component["one_minus_t"] * component["one_minus_t"],
            scale * scale * dd * dd,
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


def normalized_fraction_map(points, faces, name):
    ledger = ex.mechanics_primitives(points, faces)
    scale = 4 * ledger["d6"]
    if name == "S":
        key = PRIMARY
        cycle = faces[ledger["face_by_key"][key]]
        normal = ex.cycle_normal(cycle, points)
        nn = ex.norm2(normal)
        result = {}
        for edge, raw in ex.signed_face_components(ledger, key).items():
            dd = ex.norm2(ex.sub(points[edge[1]], points[edge[0]]))
            result[edge] = (
                raw * raw,
                scale * scale * dd * nn * nn * nn,
            )
        return result
    if name == "U54":
        xx = ex.norm2(ledger["xscaled"][54])
        result = {}
        for neighbor, raw in ledger["vertex"][54].items():
            dd = ex.norm2(ex.sub(points[neighbor], points[54]))
            result[neighbor] = (raw * raw, xx * dd)
        return result
    if name == "H56":
        return edge_fraction_map(points, faces, (5, 6))
    if name == "H1011":
        return edge_fraction_map(points, faces, (10, 11))
    raise KeyError(name)


def selected_residual_record(points, faces, name):
    rows = normalized_fraction_map(points, faces, name)
    selected_key = SELECTED_COMPONENTS[name]
    if isinstance(selected_key, list):
        selected_key = tuple(selected_key)
    selected = rows[selected_key]
    values = {key: numerator / denominator for key, (numerator, denominator) in rows.items()}
    minimum_key = min(values, key=values.get)
    if minimum_key != selected_key:
        raise AssertionError((name, selected_key, minimum_key))
    record = fraction_record(*selected)
    record["selected_component"] = list(selected_key) if isinstance(selected_key, tuple) else selected_key
    record["strict_minimum_against"] = {
        str(key): ex.qs(values[key] - values[selected_key])
        for key in rows if key != selected_key
    }
    if not all(Q(value) > 0 for value in record["strict_minimum_against"].values()):
        raise AssertionError(("selected component not strict", name, record))
    return record


def selected_fraction_polynomials(path, faces, name):
    rows = normalized_fraction_map(path, faces, name)
    selected_key = SELECTED_COMPONENTS[name]
    if isinstance(selected_key, list):
        selected_key = tuple(selected_key)
    return rows[selected_key]


def residual_direction_audit(path, pre_faces, post_faces, root, end):
    source = evaluate_path(path, Q(0))
    far = evaluate_path(path, end)
    result = {}
    for name in SELECTED_COMPONENTS:
        source_record = selected_residual_record(source, pre_faces, name)
        far_record = selected_residual_record(far, post_faces, name)
        source_value = Q(source_record["squared_value"])
        far_value = Q(far_record["squared_value"])
        if not far_value < source_value:
            raise AssertionError(("residual did not improve", name))
        piecewise = {}
        for segment, faces, lo, hi in (
            ("pre", pre_faces, Q(0), root["lo"]),
            ("post", post_faces, root["hi"], end),
        ):
            numerator, denominator = selected_fraction_polynomials(path, faces, name)
            derivative_numerator = (
                numerator.derivative() * denominator
                - numerator * denominator.derivative()
            )
            sign, leaves, worst = ex.bernstein_sign(
                derivative_numerator, lo, hi, max_depth=60
            )
            piecewise[segment] = {
                "derivative_sign": sign,
                "bernstein_leaf_count": leaves,
                "minimum_bernstein_log10_abs": worst,
                "derivative_numerator_degree": derivative_numerator.degree,
                "derivative_numerator_digest": canonical_hash(
                    derivative_numerator.exact()
                ),
            }
        result[name] = {
            "source": source_record,
            "far": far_record,
            "strict_endpoint_improvement": True,
            "exact_squared_drop": ex.qs(source_value - far_value),
            "piecewise_derivative": piecewise,
        }
    return result


def exact_root_record(polynomial):
    root = ex.isolate_monotone_root(
        polynomial, Q(5701, 10**9), Q(5703, 10**9), ROOT_WIDTH
    )
    return root, {
        "lo": ex.qs(root["lo"]),
        "hi": ex.qs(root["hi"]),
        "value_lo": ex.qs(root["value_lo"]),
        "value_hi": ex.qs(root["value_hi"]),
        "decimal_interval": [float(root["lo"]), float(root["hi"])],
        "derivative_sign": root["derivative_sign"],
        "derivative_bernstein_leaves": root["derivative_bernstein_leaves"],
        "polynomial_degree": polynomial.degree,
        "polynomial_exact": polynomial.exact(),
        "polynomial_digest": canonical_hash(polynomial.exact()),
    }


def main():
    definition = json.loads(PATH_DEFINITION.read_text())
    if definition["verdict"] != "DIRECTED_STAGE31_H1011_LOCAL_CIRCUIT_PROPOSAL_PASS":
        raise AssertionError(definition["verdict"])
    source = ex.read_rows(SOURCE)
    velocity = {
        int(label): tuple(Q(value) for value in xyz)
        for label, xyz in definition["velocity"].items()
    }
    if set(source) != set(velocity):
        raise AssertionError("path labels differ")
    path = {
        label: tuple(
            ex.P((source[label][axis], velocity[label][axis]))
            for axis in range(3)
        )
        for label in source
    }
    end = Q(definition["end_parameter"])
    pre_faces, wall_faces, post_faces = build_face_ledgers(
        json.loads(SOURCE_FACES.read_text())
    )

    target_polynomial = ex.circuit_polynomial(path, TARGET_CIRCUIT)
    root, root_record = exact_root_record(target_polynomial)
    if not Q(0) < root["lo"] <= root["hi"] < end:
        raise AssertionError((root, end))
    first_wall = ex.certify_first_support_wall(
        path, pre_faces, root, target_polynomial
    )
    expected_family = {
        (tuple(sorted(REMOVED_FACES[0])), 263),
        (tuple(sorted(REMOVED_FACES[1])), 8),
    }
    actual_family = {
        (tuple(sorted(pre_faces[row["face_index"]])), row["witness"])
        for row in first_wall["target_support_family"]
    }
    if actual_family != expected_family:
        raise AssertionError((actual_family, expected_family))

    pre_segment = ex.certify_path_segment(
        restrict_path(path, Q(0), root["lo"]), pre_faces, PROTECTED
    )
    post_segment = ex.certify_path_segment(
        restrict_path(path, root["hi"], end), post_faces, PROTECTED
    )
    wall_mechanics = ex.certify_mechanics_interval(
        path, wall_faces, PROTECTED, root["lo"], root["hi"]
    )
    if wall_mechanics["midpoint_class"]["class"] != [2, 2, 2]:
        raise AssertionError(wall_mechanics)

    pre_edges = edge_set(pre_faces)
    wall_edges = edge_set(wall_faces)
    post_edges = edge_set(post_faces)
    if pre_edges - post_edges != {REMOVED_DIAGONAL}:
        raise AssertionError(pre_edges - post_edges)
    if post_edges - pre_edges != {ADDED_DIAGONAL}:
        raise AssertionError(post_edges - pre_edges)
    if [len(EXPECTED_ACTIVE), len(wall_edges), len(wall_faces)] != EXPECTED_WALL_F_VECTOR:
        raise AssertionError((len(wall_edges), len(wall_faces)))
    for name, faces, edges in (
        ("pre", pre_faces, pre_edges),
        ("wall", wall_faces, wall_edges),
        ("post", post_faces, post_edges),
    ):
        if BASE not in {frozenset(face) for face in faces}:
            raise AssertionError((name, "base absent"))
        missing = forced_rails() - edges
        if missing:
            raise AssertionError((name, "rails absent", sorted(missing)))

    pre_parameter = root["lo"] * Q(99, 100)
    post_parameter = (root["hi"] + end) / 2
    parameters = {
        "source": Q(0),
        "pre": pre_parameter,
        "post": post_parameter,
        "far": end,
    }
    face_by_checkpoint = {
        "source": pre_faces,
        "pre": pre_faces,
        "post": post_faces,
        "far": post_faces,
    }
    checkpoints = {
        name: exact_checkpoint(
            evaluate_path(path, parameter), face_by_checkpoint[name], [2, 2, 2]
        )
        for name, parameter in parameters.items()
    }
    points_by_checkpoint = {
        name: evaluate_path(path, parameter) for name, parameter in parameters.items()
    }
    generated_points = {
        SOURCE_OUT: points_by_checkpoint["source"],
        PRE_OUT: points_by_checkpoint["pre"],
        POST_OUT: points_by_checkpoint["post"],
        FAR_OUT: points_by_checkpoint["far"],
    }
    for output, points in generated_points.items():
        write_exact_csv(output, points)
    PRE_FACES_OUT.write_text(json.dumps(pre_faces, indent=2) + "\n")
    WALL_FACES_OUT.write_text(json.dumps(wall_faces, indent=2) + "\n")
    POST_FACES_OUT.write_text(json.dumps(post_faces, indent=2) + "\n")
    generated = tuple(generated_points) + (
        PRE_FACES_OUT, WALL_FACES_OUT, POST_FACES_OUT,
    )

    residual_audit = residual_direction_audit(
        path, pre_faces, post_faces, root, end
    )
    certificate = {
        "version": 1,
        "type": "exact rational-affine algebraic support flip at own centroid",
        "scope": (
            "Exact for the literal Stage-31 H1011-upstream path, the unique "
            "first support wall, all nonwall support polynomials, both open-cell "
            "mechanics ledgers, the wall mechanics ledger, four exact rational "
            "checkpoints, base/rail preservation, and exact normalized endpoint "
            "improvement of S/U54/H56/H1011. This remains a strict nonwinner."
        ),
        "source_hashes": {
            str(file.relative_to(ROOT)): sha256(file)
            for file in (SOURCE, SOURCE_FACES, PATH_DEFINITION, PROPOSER_FACES)
        },
        "path": {
            "end_parameter": ex.qs(end),
            "velocity_digest": canonical_hash({
                str(label): [ex.qs(x) for x in velocity[label]]
                for label in sorted(velocity)
            }),
            "target_circuit": list(TARGET_CIRCUIT),
            "target_polynomial": root_record,
            "first_support_wall": first_wall,
        },
        "topology_event": {
            "pre_f_vector": EXPECTED_F_VECTOR,
            "wall_f_vector": EXPECTED_WALL_F_VECTOR,
            "post_f_vector": EXPECTED_F_VECTOR,
            "removed_maximal_faces": [list(face) for face in REMOVED_FACES],
            "wall_maximal_face": list(WALL_FACE),
            "added_maximal_faces": [list(face) for face in ADDED_FACES],
            "removed_true_edge": list(REMOVED_DIAGONAL),
            "added_true_edge": list(ADDED_DIAGONAL),
            "pre_edge_count": len(pre_edges),
            "wall_edge_count": len(wall_edges),
            "post_edge_count": len(post_edges),
            "base_preserved": True,
            "forced_rails_preserved": len(forced_rails()),
        },
        "open_cells": {
            "pre": pre_segment,
            "wall_mechanics": wall_mechanics,
            "post": post_segment,
            "class_sequence": [[2, 2, 2], [2, 2, 2], [2, 2, 2]],
        },
        "rational_parameters": {
            name: ex.qs(parameter) for name, parameter in parameters.items()
        },
        "rational_checkpoints": checkpoints,
        "directed_residuals": residual_audit,
        "generated_file_sha256": {
            str(file.relative_to(ROOT)): sha256(file) for file in generated
        },
        "residual_verdict": {
            "winner": False,
            "far_class": [2, 2, 2],
            "remaining_extra_stable": list(PRIMARY),
            "remaining_extra_unstable": 54,
            "remaining_saddles": [[5, 6], [10, 11]],
            "interpretation": (
                "The first coupled event is an exact shell diagonal flip "
                "(9,264)->(8,263). It opens a new H1011 cell and strictly "
                "improves all four normalized endpoint residuals, but kills no "
                "equilibrium at the certified far checkpoint."
            ),
        },
        "verdict": "EXACT_STAGE31_H1011_UPSTREAM_CIRCUIT_FLIP_PASS",
    }
    CERTIFICATE.write_text(json.dumps(certificate, indent=2) + "\n")
    print(json.dumps({
        "verdict": certificate["verdict"],
        "root_interval": root_record["decimal_interval"],
        "target_support_family": first_wall["target_support_family"],
        "topology": certificate["topology_event"],
        "classes": certificate["open_cells"]["class_sequence"],
        "far_decisions": {
            name: row["far"]["decision_value"]
            for name, row in residual_audit.items()
        },
    }, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
