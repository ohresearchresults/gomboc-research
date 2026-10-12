#!/usr/bin/env python3
"""Independent reconstruction of the exact U54 six-flip material path."""
from __future__ import annotations

import hashlib
import json
import math
import sys
from fractions import Fraction as Q
from pathlib import Path


sys.set_int_max_str_digits(0)

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import build_u54_material_exact_path as b  # noqa: E402


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def equivalent(actual, frozen, location="root") -> None:
    if isinstance(actual, float) or isinstance(frozen, float):
        if not math.isclose(
            float(actual), float(frozen), rel_tol=0.0, abs_tol=5e-12
        ):
            raise AssertionError((location, actual, frozen))
        return
    if isinstance(actual, dict):
        if not isinstance(frozen, dict) or set(actual) != set(frozen):
            raise AssertionError((location, set(actual), set(frozen)))
        for key in actual:
            equivalent(actual[key], frozen[key], f"{location}.{key}")
        return
    if isinstance(actual, list):
        if not isinstance(frozen, list) or len(actual) != len(frozen):
            raise AssertionError((location, len(actual), len(frozen)))
        for index, (left, right) in enumerate(zip(actual, frozen)):
            equivalent(left, right, f"{location}[{index}]")
        return
    if actual != frozen:
        raise AssertionError((location, actual, frozen))


def independent_barycentric(point, a, c, d):
    e1, e2, w = b.ex.sub(c, a), b.ex.sub(d, a), b.ex.sub(point, a)
    aa = b.ex.dot(e1, e1)
    ab = b.ex.dot(e1, e2)
    bb = b.ex.dot(e2, e2)
    wa = b.ex.dot(w, e1)
    wb = b.ex.dot(w, e2)
    determinant = aa * bb - ab * ab
    assert determinant
    return (
        (wa * bb - wb * ab) / determinant,
        (wb * aa - wa * ab) / determinant,
    )


def independent_repair_pair():
    start = b.ex.read_rows(b.START_RAW)
    endpoint = b.ex.read_rows(b.END_RAW)
    anchor = start[0]
    normal = b.ex.cross(
        b.ex.sub(start[1], anchor), b.ex.sub(start[2], anchor)
    )
    normal_norm2 = b.ex.norm2(normal)
    assert normal_norm2
    repair_records = []
    repaired = []
    for rows in (start, endpoint):
        rows = dict(rows)
        corrections = {}
        for label in b.BASE:
            coefficient = (
                b.ex.dot(normal, b.ex.sub(rows[label], anchor)) / normal_norm2
            )
            rows[label] = b.ex.sub(rows[label], b.ex.mul(normal, coefficient))
            corrections[label] = coefficient
            assert b.ex.dot(normal, b.ex.sub(rows[label], anchor)) == 0
        u, v = independent_barycentric(
            rows[246], rows[7], rows[8], rows[245]
        )
        old = rows[246]
        rows[246] = b.ex.add(
            rows[7],
            b.ex.add(
                b.ex.mul(b.ex.sub(rows[8], rows[7]), u),
                b.ex.mul(b.ex.sub(rows[245], rows[7]), v),
            ),
        )
        displacement = b.ex.sub(rows[246], old)
        nonzero = [value for value in corrections.values() if value]
        repair_records.append(
            {
                "base": {
                    "nonzero_count": len(nonzero),
                    "maximum_log10_abs": max(
                        b.ex.qlog10(value) for value in nonzero
                    ),
                    "exact_digest": b.canonical_hash(
                        {
                            str(label): b.ex.qs(value)
                            for label, value in sorted(corrections.items())
                        }
                    ),
                },
                "quad": {
                    "barycentric": [b.ex.qs(u), b.ex.qs(v)],
                    "displacement_norm2_exact": b.ex.qs(
                        b.ex.norm2(displacement)
                    ),
                    "displacement_norm_decimal": math.sqrt(
                        float(b.ex.norm2(displacement))
                    ),
                },
            }
        )
        repaired.append((rows, (u, v)))

    (start, start_uv), (endpoint, endpoint_uv) = repaired
    path = {
        label: tuple(
            b.P(
                (
                    start[label][axis],
                    endpoint[label][axis] - start[label][axis],
                )
            )
            for axis in range(3)
        )
        for label in start
        if label != 246
    }
    u = b.P((start_uv[0], endpoint_uv[0] - start_uv[0]))
    v = b.P((start_uv[1], endpoint_uv[1] - start_uv[1]))
    path[246] = b.ex.add(
        path[7],
        b.ex.add(
            b.ex.mul(b.ex.sub(path[8], path[7]), u),
            b.ex.mul(b.ex.sub(path[245], path[7]), v),
        ),
    )
    return start, endpoint, path, repair_records


def repair_standalone_independently(rows):
    anchor = rows[0]
    normal = b.ex.cross(b.ex.sub(rows[1], anchor), b.ex.sub(rows[2], anchor))
    normal_norm2 = b.ex.norm2(normal)
    rows = dict(rows)
    for label in b.BASE:
        coefficient = b.ex.dot(normal, b.ex.sub(rows[label], anchor)) / normal_norm2
        rows[label] = b.ex.sub(rows[label], b.ex.mul(normal, coefficient))
    u, v = independent_barycentric(rows[246], rows[7], rows[8], rows[245])
    rows[246] = b.ex.add(
        rows[7],
        b.ex.add(
            b.ex.mul(b.ex.sub(rows[8], rows[7]), u),
            b.ex.mul(b.ex.sub(rows[245], rows[7]), v),
        ),
    )
    return rows


def main() -> None:
    frozen = json.loads(b.CERTIFICATE_OUT.read_text())
    assert frozen["verdict"] == "EXACT_U54_MATERIAL_SIX_FLIP_CONTINUUM_PASS"
    for relative, digest in frozen["source_hashes"].items():
        assert sha256(b.ROOT / relative) == digest
    for relative, digest in frozen["generated_file_sha256"].items():
        assert sha256(b.ROOT / relative) == digest

    start, endpoint, path, repairs = independent_repair_pair()
    assert start == b.ex.read_rows(b.SOURCE_OUT)
    assert endpoint == b.ex.read_rows(b.ENDPOINT_OUT)
    equivalent(
        repairs[0]["base"],
        frozen["construction"]["start_base_repair"],
        "start_base_repair",
    )
    equivalent(
        repairs[1]["base"],
        frozen["construction"]["endpoint_base_repair"],
        "endpoint_base_repair",
    )
    equivalent(
        repairs[0]["quad"],
        frozen["construction"]["start_quad_repair"],
        "start_quad_repair",
    )
    equivalent(
        repairs[1]["quad"],
        frozen["construction"]["endpoint_quad_repair"],
        "endpoint_quad_repair",
    )
    assert b.determinant_polynomial(path, b.QUAD) == b.P.zero()
    path_digest = b.canonical_hash(
        {
            str(label): [coordinate.exact() for coordinate in path[label]]
            for label in sorted(path)
        }
    )
    assert path_digest == frozen["construction"]["path_polynomial_digest"]

    numerical = json.loads(b.NUMERICAL_ROUTE.read_text())
    roots = []
    event_polynomials = []
    for index, (circuit, event) in enumerate(
        zip(b.EXPECTED_EVENTS, numerical["straight_homotopy_events"])
    ):
        bracket = tuple(Q(str(value)) for value in event["bracket"])
        polynomial, record = b.isolate_event(path, circuit, bracket)
        frozen_event = frozen["events"][index]
        for key in (
            "circuit",
            "lo",
            "hi",
            "value_lo",
            "value_hi",
            "decimal_interval",
            "derivative_sign",
            "derivative_bernstein_leaves",
            "polynomial_degree",
            "polynomial_digest",
        ):
            equivalent(record[key], frozen_event[key], f"event{index}.{key}")
        roots.append((Q(record["lo"]), Q(record["hi"])))
        event_polynomials.append(polynomial)

    cell_faces = []
    for index, frozen_cell in enumerate(frozen["cells"]):
        lo = Q(0) if index == 0 else roots[index - 1][1]
        hi = Q(1) if index == 6 else roots[index][0]
        assert frozen_cell["interval"] == [b.ex.qs(lo), b.ex.qs(hi)]
        representative = (lo + hi) / 2
        points = b.evaluate_path(path, representative)
        face_path = b.ROOT / frozen_cell["face_file"]
        faces = json.loads(face_path.read_text())
        support, mechanics = b.assert_cell(points, faces)
        expected_support = {
            key: value for key, value in support.items() if key != "edges"
        }
        equivalent(
            expected_support, frozen_cell["exact_support"], f"cell{index}.support"
        )
        equivalent(
            mechanics, frozen_cell["exact_mechanics"], f"cell{index}.mechanics"
        )
        assert b.canonical_hash(faces) == frozen_cell["face_hash"]
        cover = b.exact_class_cover(path, faces, lo, hi)
        equivalent(
            cover,
            frozen_cell["exact_cell_class_cover"],
            f"cell{index}.class_cover",
        )
        assert len(cover) == frozen_cell["class_cover_subinterval_count"]
        equivalent(
            b.monotonicity_audit(path, faces, lo, hi),
            frozen_cell["selected_residual_monotonicity"],
            f"cell{index}.monotonicity",
        )
        cell_faces.append(faces)
        print(f"verified exact cell {index}", flush=True)

    for index, frozen_event in enumerate(frozen["events"]):
        lo, hi = roots[index]
        polynomial = event_polynomials[index]
        pre_faces, post_faces = cell_faces[index], cell_faces[index + 1]
        equivalent(
            b.support_event_audit(path, pre_faces, polynomial, lo, hi),
            frozen_event["pre_support_on_root_bracket"],
            f"wall{index}.pre_support",
        )
        equivalent(
            b.support_event_audit(path, post_faces, polynomial, lo, hi),
            frozen_event["post_support_on_root_bracket"],
            f"wall{index}.post_support",
        )
        equivalent(
            b.monotonicity_audit(path, pre_faces, lo, hi),
            frozen_event["pre_selected_residual_monotonicity"],
            f"wall{index}.pre_monotonicity",
        )
        equivalent(
            b.monotonicity_audit(path, post_faces, lo, hi),
            frozen_event["post_selected_residual_monotonicity"],
            f"wall{index}.post_monotonicity",
        )
        wall_faces = json.loads(
            (b.ROOT / frozen_event["wall_face_file"]).read_text()
        )
        assert b.canonical_hash(wall_faces) == frozen_event["wall_face_hash"]
        f_vector, edges = b.wall_f_vector(wall_faces)
        assert f_vector == b.EXPECTED_WALL_F_VECTOR
        assert b.forced_rails().issubset(edges)
        assert frozenset(b.EXPECTED_EVENTS[index]) in {
            frozenset(face) for face in wall_faces
        }
        equivalent(
            b.ex.certify_mechanics_interval(
                path, wall_faces, b.PROTECTED, lo, hi
            ),
            frozen_event["wall_mechanics"],
            f"wall{index}.mechanics",
        )
        print(f"verified exact wall {index + 1}", flush=True)

    canonical = repair_standalone_independently(b.ex.read_rows(b.CANONICAL_RAW))
    assert canonical == b.ex.read_rows(b.CANONICAL_OUT)
    canonical_faces = json.loads(b.CANONICAL_FACES_OUT.read_text())
    canonical_support = b.ex.supporting_cell(canonical, canonical_faces)
    _ledger, canonical_mechanics = b.ex.classify_point(
        canonical, canonical_faces
    )
    assert canonical_support["f_vector"] == frozen["canonical_reference"][
        "support_f_vector"
    ]
    assert canonical_mechanics == frozen["canonical_reference"]["mechanics"]

    source_values = b.residual_values(start, cell_faces[0])
    endpoint_values = b.residual_values(endpoint, cell_faces[-1])
    canonical_values = b.residual_values(canonical, canonical_faces)
    equivalent(
        b.comparison_packet(canonical_values, endpoint_values),
        frozen["exact_material_comparison_to_original_combined_wall"],
        "material_comparison",
    )
    for name, (source_value, power) in source_values.items():
        endpoint_value, endpoint_power = endpoint_values[name]
        assert power == endpoint_power and endpoint_value < source_value
        ratio_power = endpoint_value / source_value
        expected = {
            "ratio_power": power,
            "exact_ratio_to_that_power": b.ex.qs(ratio_power),
            "decimal_ratio": (
                math.sqrt(float(ratio_power))
                if power == 2
                else float(ratio_power)
            ),
        }
        equivalent(
            expected,
            frozen["exact_source_to_endpoint_monotonic_comparison"][name],
            f"source_endpoint.{name}",
        )
    assert frozen["global_conclusions"]["winner"] is False
    assert frozen["global_conclusions"]["endpoint_class"] == b.EXPECTED_CLASS
    print("INDEPENDENT_EXACT_U54_MATERIAL_SIX_FLIP_CONTINUUM_PASS")


if __name__ == "__main__":
    main()
