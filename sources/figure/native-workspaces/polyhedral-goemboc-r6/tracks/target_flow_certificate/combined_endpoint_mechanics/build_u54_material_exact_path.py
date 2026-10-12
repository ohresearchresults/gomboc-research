#!/usr/bin/env python3
"""Exactify the six-flip, 401-sample U54 material homotopy.

The numerical route is replaced by one explicit rational polynomial path.
The enlarged base is projected onto one common exact plane at both endpoints;
the protected quadrilateral is reconstructed from linearly interpolated exact
barycentric coordinates.  Every open support cell, every algebraic flip, the
complete exhaustive S/U/H classification, and monotonicity of the four frozen
residuals are then certified with rational polynomial arithmetic.
"""
from __future__ import annotations

import csv
import hashlib
import json
import math
import sys
from fractions import Fraction as Q
from pathlib import Path

import numpy as np


sys.set_int_max_str_digits(0)


HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
START_RAW = HERE / "epoch4_cluster_event3_deep_after.csv"
END_RAW = HERE / "u54_material_actual_endpoint.csv"
NUMERICAL_ROUTE = HERE / "u54_material_actual.json"
CANONICAL_RAW = ROOT / "tracks/circuit_atlas/row54_combined_wall_rebuilt.csv"

SOURCE_OUT = HERE / "u54_material_exact_source.csv"
ENDPOINT_OUT = HERE / "u54_material_exact_endpoint.csv"
CANONICAL_OUT = HERE / "u54_material_exact_canonical.csv"
CANONICAL_FACES_OUT = HERE / "u54_material_exact_canonical_faces.json"
CERTIFICATE_OUT = HERE / "u54_material_exact_path_certificate.json"

EXACT_DIR = (
    ROOT
    / "tracks/target_sphere_realizer/grouped_local_escape/rigorous_null_bypass"
)
GROUPED_DIR = EXACT_DIR.parent
sys.path[:0] = [str(EXACT_DIR), str(GROUPED_DIR)]

import actual_grouped as actual  # noqa: E402
import grouped_exact as gx  # noqa: E402


ex = gx.ex
P = ex.P
BASE = frozenset(range(17)) | {54}
QUAD = (7, 8, 245, 246)
PROTECTED = {
    "stable": [sorted(BASE), list(QUAD)],
    "unstable": [8, 54],
    "saddles": [[6, 7], [9, 10]],
}
EXPECTED_EVENTS = (
    (69, 236, 237, 238),
    (198, 233, 234, 236),
    (198, 233, 234, 236),
    (69, 236, 237, 238),
    (69, 238, 239, 256),
    (69, 228, 236, 237),
)
EXPECTED_CLASS = [2, 2, 2]
EXPECTED_CELL_F_VECTOR = [60, 158, 100]
EXPECTED_WALL_F_VECTOR = [60, 157, 99]
ROOT_WIDTH = Q(1, 10**24)


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


def barycentric(point, a, b, c):
    e1, e2, w = ex.sub(b, a), ex.sub(c, a), ex.sub(point, a)
    aa, ab, bb = ex.dot(e1, e1), ex.dot(e1, e2), ex.dot(e2, e2)
    wa, wb = ex.dot(w, e1), ex.dot(w, e2)
    determinant = aa * bb - ab * ab
    if not determinant:
        raise AssertionError("degenerate exact quadrilateral chart")
    return (
        (wa * bb - wb * ab) / determinant,
        (wb * aa - wa * ab) / determinant,
    )


def project_base(rows, anchor, normal, normal_norm2):
    out = dict(rows)
    corrections = {}
    for label in BASE:
        coefficient = ex.dot(normal, ex.sub(out[label], anchor)) / normal_norm2
        out[label] = ex.sub(out[label], ex.mul(normal, coefficient))
        corrections[label] = coefficient
        if ex.dot(normal, ex.sub(out[label], anchor)):
            raise AssertionError(("base projection failed", label))
    nonzero = [value for value in corrections.values() if value]
    return out, {
        "nonzero_count": len(nonzero),
        "maximum_log10_abs": (
            max(ex.qlog10(value) for value in nonzero) if nonzero else None
        ),
        "exact_digest": canonical_hash(
            {str(label): ex.qs(value) for label, value in sorted(corrections.items())}
        ),
    }


def repair_quad(rows):
    out = dict(rows)
    u, v = barycentric(out[246], out[7], out[8], out[245])
    repaired = ex.add(
        out[7],
        ex.add(
            ex.mul(ex.sub(out[8], out[7]), u),
            ex.mul(ex.sub(out[245], out[7]), v),
        ),
    )
    displacement = ex.sub(repaired, out[246])
    out[246] = repaired
    return out, (u, v), {
        "barycentric": [ex.qs(u), ex.qs(v)],
        "displacement_norm2_exact": ex.qs(ex.norm2(displacement)),
        "displacement_norm_decimal": math.sqrt(float(ex.norm2(displacement))),
    }


def build_exact_path():
    raw_start = ex.read_rows(START_RAW)
    raw_end = ex.read_rows(END_RAW)
    if set(raw_start) != set(raw_end):
        raise AssertionError("material endpoint labels differ from source")
    anchor = raw_start[0]
    normal = ex.cross(
        ex.sub(raw_start[1], anchor), ex.sub(raw_start[2], anchor)
    )
    normal_norm2 = ex.norm2(normal)
    if not normal_norm2:
        raise AssertionError("degenerate common base plane")
    start, start_base = project_base(raw_start, anchor, normal, normal_norm2)
    end, end_base = project_base(raw_end, anchor, normal, normal_norm2)
    start, start_uv, start_quad = repair_quad(start)
    end, end_uv, end_quad = repair_quad(end)

    path = {
        label: tuple(
            P((start[label][axis], end[label][axis] - start[label][axis]))
            for axis in range(3)
        )
        for label in start
        if label != 246
    }
    u = P((start_uv[0], end_uv[0] - start_uv[0]))
    v = P((start_uv[1], end_uv[1] - start_uv[1]))
    path[246] = ex.add(
        path[7],
        ex.add(
            ex.mul(ex.sub(path[8], path[7]), u),
            ex.mul(ex.sub(path[245], path[7]), v),
        ),
    )
    for label in BASE:
        if ex.dot(normal, ex.sub(path[label], tuple(P((x,)) for x in anchor))) != P.zero():
            raise AssertionError(("moving base is not exact", label))
    quad_determinant = determinant_polynomial(path, QUAD)
    if quad_determinant != P.zero():
        raise AssertionError(("moving quadrilateral is not exact", quad_determinant.exact()))
    return start, end, path, {
        "start_base_repair": start_base,
        "endpoint_base_repair": end_base,
        "start_quad_repair": start_quad,
        "endpoint_quad_repair": end_quad,
        "path_polynomial_digest": canonical_hash(
            {
                str(label): [coordinate.exact() for coordinate in path[label]]
                for label in sorted(path)
            }
        ),
    }


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


def determinant_polynomial(path, quad):
    a, b, c, d = (path[label] for label in quad)
    return ex.det3(ex.sub(b, a), ex.sub(c, a), ex.sub(d, a))


def fresh_faces(points, coplanar_rel=2e-12):
    result = actual.evaluate(
        {
            label: np.asarray([float(value) for value in xyz])
            for label, xyz in points.items()
        },
        coplanar_rel=coplanar_rel,
    )
    if not result.valid:
        raise AssertionError(result.error)
    return [row["cycle"] for row in result.faces], result


def forced_rails():
    short = [228] + list(range(229, 247)) + [8]
    long = [228] + list(range(247, 265)) + [8]
    edges = {
        tuple(sorted(edge))
        for rail in (short, long)
        for edge in zip(rail, rail[1:])
    }
    edges.remove((228, 229))
    return edges


def assert_cell(points, faces):
    support = ex.supporting_cell(points, faces)
    _ledger, mechanics = ex.classify_point(points, faces)
    if support["f_vector"] != EXPECTED_CELL_F_VECTOR:
        raise AssertionError(support)
    if support["active_labels"] != sorted(set(points) - {73}):
        raise AssertionError(("wrong active labels", support["active_labels"]))
    if mechanics["class"] != EXPECTED_CLASS:
        raise AssertionError(mechanics)
    face_sets = {frozenset(face) for face in faces}
    if BASE not in face_sets or frozenset(QUAD) not in face_sets:
        raise AssertionError("protected base or quadrilateral absent")
    if not forced_rails().issubset(set(support["edges"])):
        raise AssertionError("forced rail missing")
    return support, mechanics


def exact_sign_record(poly: P, lo: Q, hi: Q, expected: int):
    sign, leaves, worst = ex.bernstein_sign(poly, lo, hi, max_depth=60)
    if sign != expected:
        raise AssertionError(("unexpected polynomial sign", sign, expected))
    return {
        "sign": sign,
        "degree": poly.degree,
        "bernstein_leaf_count": leaves,
        "minimum_bernstein_log10_abs": worst,
        "polynomial_digest": canonical_hash(poly.exact()),
    }


def ratio_derivative(numerator: P, denominator: P):
    return numerator.derivative() * denominator - numerator * denominator.derivative()


def residual_derivative_polynomials(path, faces):
    ledger = ex.mechanics_primitives(path, faces)
    scale = 4 * ledger["d6"]

    face_key = tuple(sorted(QUAD))
    face_index = ledger["face_by_key"][face_key]
    face_raw = ex.signed_face_components(ledger, face_key)[(8, 246)]
    face_normal = ex.cycle_normal(faces[face_index], path)
    face_edge = ex.sub(path[246], path[8])
    face_denominator = (
        scale
        * scale
        * ex.norm2(face_normal)
        * ex.norm2(face_normal)
        * ex.norm2(face_normal)
        * ex.norm2(face_edge)
    )

    vertex_raw = ledger["vertex"][54][1]
    vertex_denominator = ex.norm2(ledger["xscaled"][54]) * ex.norm2(
        ex.sub(path[1], path[54])
    )

    out = {
        "S_quad_squared": ratio_derivative(
            face_raw * face_raw, face_denominator
        ),
        "U54_squared": ratio_derivative(
            vertex_raw * vertex_raw, vertex_denominator
        ),
    }
    for name, edge, component in (
        ("H67_one_minus_t", (6, 7), "one_minus_t"),
        ("H910_t", (9, 10), "t"),
    ):
        numerator = ledger["edge"][edge][component]
        denominator = scale * ledger["edge"][edge]["direction_norm2"]
        out[name] = ratio_derivative(numerator, denominator)
    return out


def monotonicity_audit(path, faces, lo: Q, hi: Q):
    return {
        name: exact_sign_record(poly, lo, hi, -1)
        for name, poly in residual_derivative_polynomials(path, faces).items()
    }


def certify_class_interval(points, faces):
    """Exact class certificate with an existential forbidden-feature witness.

    The shared legacy helper freezes the most negative component at the left
    endpoint.  That is stronger than classification and fails when two
    negative witnesses overlap and exchange order.  Here every forbidden
    feature may use any one component that is proved negative on the whole
    interval; protected features still certify every defining component.
    """
    ledger = ex.mechanics_primitives(points, faces)
    records = []

    def prove(name, poly, expected=None):
        if not isinstance(poly, P):
            poly = P.coerce(poly)
        sign, leaves, worst = ex.bernstein_sign(
            poly, Q(0), Q(1), max_depth=60
        )
        if expected is not None and sign != expected:
            raise AssertionError((name, sign, expected))
        records.append((name, sign, leaves, worst, poly))

    def choose_negative(prefix, candidates):
        failures = []
        for component, poly in candidates:
            try:
                prove(f"{prefix}:{component}", poly, -1)
                return component
            except AssertionError as error:
                failures.append((component, repr(error)))
        raise AssertionError(("no interval-wide negative witness", prefix, failures))

    prove("volume_d6", ledger["d6"], 1)
    for face_index, witness, poly in ex.support_polynomials(points, faces):
        prove(
            f"support:f{face_index}:w{witness}",
            poly,
            ex.sign_at_zero(poly),
        )
    for face_key, references in ledger["reference"].items():
        for edge, poly in references.items():
            prove(
                f"face_reference:{face_key}:{edge}",
                poly,
                ex.sign_at_zero(poly),
            )
    for edge, components in ledger["edge"].items():
        prove(
            f"edge_direction_norm2:{edge}",
            components["direction_norm2"],
            1,
        )
        prove(f"edge_gram:{edge}", components["gram"], 1)

    midpoint = {
        label: tuple(coordinate.eval(Q(1, 2)) for coordinate in xyz)
        for label, xyz in points.items()
    }
    _midpoint_ledger, summary = ex.classify_point(midpoint, faces)
    stable_keys = {tuple(sorted(row)) for row in PROTECTED["stable"]}
    unstable_keys = set(PROTECTED["unstable"])
    saddle_keys = {tuple(sorted(row)) for row in PROTECTED["saddles"]}

    for face_key in ledger["face"]:
        signed = ex.signed_face_components(ledger, face_key)
        if face_key in stable_keys:
            for edge, poly in signed.items():
                prove(f"stable:{face_key}:{edge}", poly, 1)
        else:
            choose_negative(
                f"nonstable:{face_key}",
                [(str(edge), poly) for edge, poly in signed.items()],
            )
    for vertex, values in ledger["vertex"].items():
        if vertex in unstable_keys:
            for neighbor, poly in values.items():
                prove(f"unstable:{vertex}:{neighbor}", poly, 1)
        else:
            choose_negative(
                f"nonunstable:{vertex}",
                [(str(neighbor), poly) for neighbor, poly in values.items()],
            )
    component_names = ("t", "one_minus_t", "beta1", "beta2")
    for edge, values in ledger["edge"].items():
        if edge in saddle_keys:
            for component in component_names:
                prove(f"saddle:{edge}:{component}", values[component], 1)
        else:
            choose_negative(
                f"nonsaddle:{edge}",
                [(component, values[component]) for component in component_names],
            )

    digest = hashlib.sha256()
    for name, sign, _leaves, _worst, poly in records:
        digest.update(
            f"{name}|{sign}|{'|'.join(poly.exact())}\n".encode()
        )
    return {
        "midpoint_class": summary,
        "certified_polynomial_count": len(records),
        "bernstein_leaf_count": sum(row[2] for row in records),
        "minimum_bernstein_log10_abs": min(row[3] for row in records),
        "primitive_digest": digest.hexdigest(),
        "forbidden_feature_witness_rule": (
            "one exact interval-wide negative component per forbidden feature"
        ),
    }


def exact_class_cover(path, faces, lo: Q, hi: Q, depth=0):
    """Cover a support cell by strict fixed-witness mechanics intervals.

    A forbidden feature may remain forbidden while its most negative
    component changes.  The exhaustive classifier therefore needs a finite
    witness cover, not one unnecessarily frozen witness for the whole support
    cell.  Failure after bounded exact subdivision remains fatal.
    """
    try:
        audit = certify_class_interval(restrict_path(path, lo, hi), faces)
        return [
            {
                "interval": [ex.qs(lo), ex.qs(hi)],
                "audit": audit,
            }
        ]
    except AssertionError:
        if depth >= 14:
            raise
        midpoint = (lo + hi) / 2
        return exact_class_cover(
            path, faces, lo, midpoint, depth + 1
        ) + exact_class_cover(path, faces, midpoint, hi, depth + 1)


def isolate_event(path, circuit, bracket):
    polynomial = determinant_polynomial(path, circuit)
    lo0, hi0 = bracket
    root = ex.isolate_monotone_root(polynomial, lo0, hi0, ROOT_WIDTH)
    return polynomial, {
        "circuit": list(circuit),
        "lo": ex.qs(root["lo"]),
        "hi": ex.qs(root["hi"]),
        "value_lo": ex.qs(root["value_lo"]),
        "value_hi": ex.qs(root["value_hi"]),
        "decimal_interval": [float(root["lo"]), float(root["hi"])],
        "derivative_sign": root["derivative_sign"],
        "derivative_bernstein_leaves": root[
            "derivative_bernstein_leaves"
        ],
        "polynomial_degree": polynomial.degree,
        "polynomial_digest": canonical_hash(polynomial.exact()),
    }


def proportional_factor(candidate: P, reference: P):
    reference_index = next(
        (index for index, value in enumerate(reference.c) if value), None
    )
    if reference_index is None:
        raise AssertionError("zero event polynomial")
    candidate_value = (
        candidate.c[reference_index]
        if reference_index < len(candidate.c)
        else Q(0)
    )
    factor = candidate_value / reference.c[reference_index]
    size = max(len(candidate.c), len(reference.c))
    for index in range(size):
        left = candidate.c[index] if index < len(candidate.c) else Q(0)
        right = reference.c[index] if index < len(reference.c) else Q(0)
        if left != factor * right:
            return None
    return factor


def support_event_audit(path, faces, event_polynomial, lo: Q, hi: Q):
    digest = hashlib.sha256()
    event_rows = []
    count = leaves = 0
    worst = None
    for face_index, witness, polynomial in ex.support_polynomials(path, faces):
        name = f"support:f{face_index}:w{witness}"
        factor = proportional_factor(polynomial, event_polynomial)
        if factor is not None:
            event_rows.append(
                {
                    "name": name,
                    "factor": ex.qs(factor),
                    "value_lo": ex.qs(polynomial.eval(lo)),
                    "value_hi": ex.qs(polynomial.eval(hi)),
                }
            )
            continue
        sign, local_leaves, local_worst = ex.bernstein_sign(
            polynomial, lo, hi, max_depth=60
        )
        digest.update(
            f"{name}|{sign}|{'|'.join(polynomial.exact())}\n".encode()
        )
        count += 1
        leaves += local_leaves
        worst = local_worst if worst is None else min(worst, local_worst)
    if len(event_rows) != 2:
        raise AssertionError(("unexpected event support row count", event_rows))
    return {
        "strict_non_event_support_count": count,
        "event_support_rows": event_rows,
        "bernstein_leaf_count": leaves,
        "minimum_bernstein_log10_abs": worst,
        "strict_support_digest": digest.hexdigest(),
    }


def wall_f_vector(faces):
    incidence, _neighbors, _face_by_key = ex.edge_data(faces)
    active = set().union(*(set(face) for face in faces))
    return [len(active), len(incidence), len(faces)], set(incidence)


def residual_values(points, faces):
    ledger = ex.mechanics_primitives(points, faces)
    scale = 4 * ledger["d6"]
    face_key = tuple(sorted(QUAD))
    face_index = ledger["face_by_key"][face_key]
    raw = ex.signed_face_components(ledger, face_key)[(8, 246)]
    normal = ex.cycle_normal(faces[face_index], points)
    edge = ex.sub(points[246], points[8])
    face_denominator = (
        scale
        * scale
        * ex.norm2(normal)
        * ex.norm2(normal)
        * ex.norm2(normal)
        * ex.norm2(edge)
    )
    vertex_raw = ledger["vertex"][54][1]
    vertex_denominator = ex.norm2(ledger["xscaled"][54]) * ex.norm2(
        ex.sub(points[1], points[54])
    )
    values = {
        "S_quad": (raw * raw / face_denominator, 2),
        "U54": (vertex_raw * vertex_raw / vertex_denominator, 2),
    }
    for name, target_edge, component in (
        ("H67_one_minus_t", (6, 7), "one_minus_t"),
        ("H910_t", (9, 10), "t"),
    ):
        numerator = ledger["edge"][target_edge][component]
        denominator = scale * ledger["edge"][target_edge]["direction_norm2"]
        values[name] = (numerator / denominator, 1)
    if any(value <= 0 for value, _power in values.values()):
        raise AssertionError(("nonpositive selected residual", values))
    return values


def comparison_packet(reference_values, endpoint_values, threshold=Q(49, 50)):
    packet = {}
    for name in reference_values:
        reference, power = reference_values[name]
        endpoint, endpoint_power = endpoint_values[name]
        if power != endpoint_power:
            raise AssertionError((name, power, endpoint_power))
        ratio_power = endpoint / reference
        bound = threshold**power
        if ratio_power >= bound:
            raise AssertionError(("material threshold failed", name, ratio_power, bound))
        decimal_ratio = (
            math.sqrt(float(ratio_power)) if power == 2 else float(ratio_power)
        )
        packet[name] = {
            "ratio_power": power,
            "exact_ratio_to_that_power": ex.qs(ratio_power),
            "decimal_ratio": decimal_ratio,
            "exact_threshold_to_that_power": ex.qs(bound),
            "strictly_below_0_98": True,
        }
    return packet


def repair_standalone(rows):
    anchor = rows[0]
    normal = ex.cross(ex.sub(rows[1], anchor), ex.sub(rows[2], anchor))
    normal_norm2 = ex.norm2(normal)
    repaired, base_log = project_base(rows, anchor, normal, normal_norm2)
    repaired, _uv, quad_log = repair_quad(repaired)
    return repaired, {"base": base_log, "quad": quad_log}


def main() -> None:
    start, endpoint, path, construction = build_exact_path()
    write_exact_csv(SOURCE_OUT, start)
    write_exact_csv(ENDPOINT_OUT, endpoint)

    numerical = json.loads(NUMERICAL_ROUTE.read_text())
    numerical_events = numerical["straight_homotopy_events"]
    if len(numerical_events) != len(EXPECTED_EVENTS):
        raise AssertionError("numerical event count changed")
    event_polynomials = []
    root_records = []
    for expected, numerical_event in zip(EXPECTED_EVENTS, numerical_events):
        numerical_circuits = [
            tuple(row["circuit"]) for row in numerical_event["exact_roots"]
        ]
        if expected not in numerical_circuits:
            raise AssertionError((expected, numerical_circuits))
        bracket = tuple(Q(str(value)) for value in numerical_event["bracket"])
        polynomial, root = isolate_event(path, expected, bracket)
        event_polynomials.append(polynomial)
        root_records.append(root)

    roots = [(Q(record["lo"]), Q(record["hi"])) for record in root_records]
    if not all(roots[index][1] < roots[index + 1][0] for index in range(5)):
        raise AssertionError("exact event roots are not ordered")
    cell_bounds = []
    for index in range(7):
        lo = Q(0) if index == 0 else roots[index - 1][1]
        hi = Q(1) if index == 6 else roots[index][0]
        cell_bounds.append((lo, hi))

    generated = [SOURCE_OUT, ENDPOINT_OUT]
    cells = []
    cell_faces = []
    for index, (lo, hi) in enumerate(cell_bounds):
        representative = (lo + hi) / 2
        points = evaluate_path(path, representative)
        faces, _result = fresh_faces(points)
        support, mechanics = assert_cell(points, faces)
        face_path = HERE / f"u54_material_exact_cell{index}_faces.json"
        face_path.write_text(json.dumps(faces, indent=2) + "\n")
        generated.append(face_path)
        class_cover = exact_class_cover(path, faces, lo, hi)
        monotonic = monotonicity_audit(path, faces, lo, hi)
        cells.append(
            {
                "index": index,
                "interval": [ex.qs(lo), ex.qs(hi)],
                "representative": ex.qs(representative),
                "face_file": str(face_path.relative_to(ROOT)),
                "face_hash": canonical_hash(faces),
                "exact_support": {
                    key: value for key, value in support.items() if key != "edges"
                },
                "exact_mechanics": mechanics,
                "exact_cell_class_cover": class_cover,
                "class_cover_subinterval_count": len(class_cover),
                "selected_residual_monotonicity": monotonic,
            }
        )
        cell_faces.append(faces)
        print(
            f"exact cell {index}: class-cover={len(class_cover)} interval(s)",
            flush=True,
        )

    events = []
    for index, (root, polynomial) in enumerate(
        zip(root_records, event_polynomials)
    ):
        lo, hi = Q(root["lo"]), Q(root["hi"])
        pre_faces, post_faces = cell_faces[index], cell_faces[index + 1]
        midpoint = (lo + hi) / 2
        wall_faces, _wall_result = fresh_faces(
            evaluate_path(path, midpoint), coplanar_rel=2e-11
        )
        f_vector, wall_edges = wall_f_vector(wall_faces)
        if f_vector != EXPECTED_WALL_F_VECTOR:
            raise AssertionError(("wrong exact-wall proposal", index, f_vector))
        if not forced_rails().issubset(wall_edges):
            raise AssertionError(("wall loses rail", index))
        wall_face_sets = {frozenset(face) for face in wall_faces}
        if BASE not in wall_face_sets or frozenset(QUAD) not in wall_face_sets:
            raise AssertionError(("wall loses protected face", index))
        if frozenset(EXPECTED_EVENTS[index]) not in wall_face_sets:
            raise AssertionError(("event quadrilateral absent", index))
        wall_path = HERE / f"u54_material_exact_wall{index + 1}_faces.json"
        wall_path.write_text(json.dumps(wall_faces, indent=2) + "\n")
        generated.append(wall_path)
        events.append(
            {
                **root,
                "pre_support_on_root_bracket": support_event_audit(
                    path, pre_faces, polynomial, lo, hi
                ),
                "post_support_on_root_bracket": support_event_audit(
                    path, post_faces, polynomial, lo, hi
                ),
                "pre_selected_residual_monotonicity": monotonicity_audit(
                    path, pre_faces, lo, hi
                ),
                "post_selected_residual_monotonicity": monotonicity_audit(
                    path, post_faces, lo, hi
                ),
                "wall_face_file": str(wall_path.relative_to(ROOT)),
                "wall_face_hash": canonical_hash(wall_faces),
                "wall_f_vector": f_vector,
                "wall_mechanics": ex.certify_mechanics_interval(
                    path, wall_faces, PROTECTED, lo, hi
                ),
                "removed_faces": sorted(
                    [
                        sorted(face)
                        for face in {frozenset(x) for x in pre_faces}
                        - {frozenset(x) for x in post_faces}
                    ]
                ),
                "added_faces": sorted(
                    [
                        sorted(face)
                        for face in {frozenset(x) for x in post_faces}
                        - {frozenset(x) for x in pre_faces}
                    ]
                ),
            }
        )
        print(f"exact wall {index + 1}: isolated and certified", flush=True)

    canonical, canonical_repair = repair_standalone(ex.read_rows(CANONICAL_RAW))
    canonical_faces, _canonical_result = fresh_faces(canonical)
    canonical_support = ex.supporting_cell(canonical, canonical_faces)
    _canonical_ledger, canonical_mechanics = ex.classify_point(
        canonical, canonical_faces
    )
    if canonical_mechanics["class"] != EXPECTED_CLASS:
        raise AssertionError(canonical_mechanics)
    write_exact_csv(CANONICAL_OUT, canonical)
    CANONICAL_FACES_OUT.write_text(json.dumps(canonical_faces, indent=2) + "\n")
    generated.extend((CANONICAL_OUT, CANONICAL_FACES_OUT))

    source_values = residual_values(start, cell_faces[0])
    endpoint_values = residual_values(endpoint, cell_faces[-1])
    canonical_values = residual_values(canonical, canonical_faces)
    material_comparison = comparison_packet(canonical_values, endpoint_values)
    source_to_endpoint = {}
    for name, (source_value, power) in source_values.items():
        endpoint_value, endpoint_power = endpoint_values[name]
        if power != endpoint_power or endpoint_value >= source_value:
            raise AssertionError(("endpoint is not improved from source", name))
        ratio_power = endpoint_value / source_value
        source_to_endpoint[name] = {
            "ratio_power": power,
            "exact_ratio_to_that_power": ex.qs(ratio_power),
            "decimal_ratio": (
                math.sqrt(float(ratio_power))
                if power == 2
                else float(ratio_power)
            ),
        }

    source_hashes = {
        str(path.relative_to(ROOT)): sha256(path)
        for path in (START_RAW, END_RAW, NUMERICAL_ROUTE, CANONICAL_RAW)
    }
    generated_hashes = {
        str(path.relative_to(ROOT)): sha256(path) for path in generated
    }
    certificate = {
        "version": 1,
        "type": "exact rational polynomial six-flip material homotopy",
        "verdict": "EXACT_U54_MATERIAL_SIX_FLIP_CONTINUUM_PASS",
        "scope": (
            "Exact for the explicit repaired polynomial path, its seven open "
            "support cells, six isolated algebraic quadrilateral flips, all "
            "support and mechanics denominators, an exhaustive strict class "
            "witness for every S/U/H feature, and the four selected residual "
            "derivatives. The endpoint remains class (2,2,2); this "
            "is not a polyhedral Gomboc."
        ),
        "source_hashes": source_hashes,
        "construction": construction,
        "path_interval": ["0", "1"],
        "cell_count": len(cells),
        "event_count": len(events),
        "cells": cells,
        "events": events,
        "canonical_reference": {
            "coordinate_file": str(CANONICAL_OUT.relative_to(ROOT)),
            "face_file": str(CANONICAL_FACES_OUT.relative_to(ROOT)),
            "repair": canonical_repair,
            "support_f_vector": canonical_support["f_vector"],
            "mechanics": canonical_mechanics,
        },
        "exact_source_to_endpoint_monotonic_comparison": source_to_endpoint,
        "exact_material_comparison_to_original_combined_wall": material_comparison,
        "global_conclusions": {
            "all_seven_cells_exact_class": EXPECTED_CLASS,
            "all_six_walls_exact_class": EXPECTED_CLASS,
            "all_37_forced_rails_retained": True,
            "only_inactive_row_in_open_cells": 73,
            "all_four_selected_residuals_strictly_monotone": True,
            "all_four_endpoint_ratios_strictly_below_0_98": True,
            "winner": False,
            "endpoint_class": EXPECTED_CLASS,
        },
        "generated_file_sha256": generated_hashes,
    }
    CERTIFICATE_OUT.write_text(json.dumps(certificate, indent=2) + "\n")
    print("EXACT_U54_MATERIAL_SIX_FLIP_CONTINUUM_PASS")
    print(
        json.dumps(
            {
                "cells": len(cells),
                "events": [row["decimal_interval"] for row in events],
                "material_ratios": {
                    key: value["decimal_ratio"]
                    for key, value in material_comparison.items()
                },
                "endpoint_class": EXPECTED_CLASS,
            },
            indent=2,
        )
    )


if __name__ == "__main__":
    main()
