#!/usr/bin/env python3
"""Clean-room verification of the exactified 165-control material step.

This verifier imports neither the builder, ``exact_core``, nor
``attack_common``.  It reconstructs the chart projection from the saved
numerical proposal, uses the independent rational geometry implementation from
the rejected-event verifier, rebuilds maximal faces at both endpoints, and
rechecks every support and own-centroid mechanics polynomial on the interval.
"""
from __future__ import annotations

import argparse
import csv
import hashlib
import io
import importlib.util
import sys
from fractions import Fraction as Q
from pathlib import Path

import numpy as np

import exactification_provenance as provenance


sys.set_int_max_str_digits(0)

HERE = Path(__file__).resolve().parent
RAIL = HERE.parent
PARENT = RAIL.parent
ROOT = HERE.parents[5]

SOURCE = PARENT / "exact_event_source.csv"
DEFAULT_SOURCE = SOURCE
FACES_PATH = PARENT / "exact_event_source_faces.json"
REJECTED_CERTIFICATE = PARENT / "exact_event_certificate.json"
REJECTED_PATH = PARENT / "exact_event_path.json"
PROPOSAL = RAIL / "full_control_search.json"
CANDIDATE = RAIL / "full_control_candidate_float.csv"
PATH_DEFINITION = HERE / "exact_first_jet_full_chart_certified_path.json"
ENDPOINT = HERE / "exact_material_step_endpoint.csv"
CERTIFICATE = HERE / "exactification_certificate.json"
VERIFICATION = HERE / "exactification_verification.json"

CLEAN_MODULE = PARENT / "verify_exact_event_certificate.py"
spec = importlib.util.spec_from_file_location("clean_local_oct_exact", CLEAN_MODULE)
if spec is None or spec.loader is None:
    raise RuntimeError("cannot load independent exact module")
_IMPORT_TRUST = provenance.expected_trust_packet(ROOT, "verifier")
_CLEAN_SNAPSHOT = provenance.read_snapshot(CLEAN_MODULE)
if _CLEAN_SNAPSHOT.sha256 != provenance.EXPECTED_CLEAN_MODULE_SHA256:
    raise RuntimeError("clean verifier module changed between trust check and byte load")
clean = importlib.util.module_from_spec(spec)
sys.modules[spec.name] = clean
exec(compile(_CLEAN_SNAPSHOT.data, str(CLEAN_MODULE), "exec"), clean.__dict__)

STEP = Q(1, 4)
ROOT_WIDTH = Q(1, 2**96)
ROUND_DIGITS = 14
BASE = frozenset(range(17)) | {54}
TARGET_FACE = (198, 243, 245)
TARGET_EDGES = ((4, 5), (12, 13))
EDGE_COMPONENTS = ("t", "one_minus_t", "beta1", "beta2")
ACTIVE_NAMES = {
    "S[198,243,245]:edge(198,243)",
    "U1:neighbor(2)",
    "H(4,5):one_minus_t",
    "H(12,13):one_minus_t",
}
CIRCUIT = (69, 224, 255, 256)
CIRCUIT_SUPPORT_ROWS = ((57, 69), (58, 224))


def canonical_hash(value) -> str:
    return provenance.canonical_hash(value)


def polynomial_hash(polynomial) -> str:
    return canonical_hash(polynomial.exact())


def qs(value: Q) -> str:
    return str(value.numerator) if value.denominator == 1 else f"{value.numerator}/{value.denominator}"


def read_float_csv(snapshot):
    rows = {}
    stream = io.StringIO(snapshot.data.decode("utf-8"), newline="")
    reader = csv.DictReader(stream)
    if reader.fieldnames != ["source_id", "x", "y", "z"]:
        raise ValueError("invalid float candidate CSV header")
    for row in reader:
        label = int(row["source_id"])
        if label in rows:
            raise ValueError(("duplicate float candidate source_id", label))
        rows[label] = np.asarray(
            [float(row[key]) for key in ("x", "y", "z")], dtype=float
        )
    return rows


def add(left, right):
    return tuple(a + b for a, b in zip(left, right))


def sub(left, right):
    return tuple(a - b for a, b in zip(left, right))


def mul(vector, scalar):
    return tuple(scalar * value for value in vector)


def dot(left, right):
    return sum(a * b for a, b in zip(left, right))


def cross(left, right):
    return (
        left[1] * right[2] - left[2] * right[1],
        left[2] * right[0] - left[0] * right[2],
        left[0] * right[1] - left[1] * right[0],
    )


def rationalize(value: float) -> Q:
    return Q(format(float(value), f".{ROUND_DIGITS}g"))


def forced_rails():
    rails = set()
    for route in (
        [228, *range(229, 247), 8],
        [228, *range(247, 265), 8],
    ):
        rails.update(tuple(sorted(edge)) for edge in zip(route, route[1:]))
    rails.remove((228, 229))
    if len(rails) != 37:
        raise AssertionError(len(rails))
    return rails


def face_keys(faces):
    return {frozenset(face) for face in faces}


def evaluate_path(path, parameter: Q):
    return {
        label: tuple(coordinate.eval(parameter) for coordinate in xyz)
        for label, xyz in path.items()
    }


def reconstruct_velocity(source, proposal, definition, candidate):
    ids = sorted(source)
    source_float = np.asarray(
        [[float(value) for value in source[label]] for label in ids], dtype=float
    )
    center = np.mean(source_float, axis=0)
    scale = float(
        np.sqrt(np.mean(np.sum((source_float - center) ** 2, axis=1)))
    )
    index = {label: offset for offset, label in enumerate(ids)}
    anchor = source_float[index[0]]
    chart_u = source_float[index[1]] - anchor
    chart_u /= np.linalg.norm(chart_u)
    chart_normal = np.cross(
        source_float[index[1]] - anchor,
        source_float[index[2]] - anchor,
    )
    chart_normal /= np.linalg.norm(chart_normal)
    chart_v = np.cross(chart_normal, chart_u)

    physical = np.zeros_like(source_float)
    cursor = 0
    coefficients = np.asarray(proposal["selected"]["direction"], dtype=float)
    for label in ids:
        if label in BASE:
            physical[index[label]] += coefficients[cursor] * scale * chart_u
            physical[index[label]] += coefficients[cursor + 1] * scale * chart_v
            cursor += 2
        else:
            for axis in range(3):
                physical[index[label], axis] += coefficients[cursor] * scale
                cursor += 1
    if cursor != 165 or cursor != len(coefficients):
        raise AssertionError("independent chart dimension drift")

    e1 = sub(source[1], source[0])
    e2 = sub(source[2], source[0])
    basis = np.asarray(
        [[float(value) for value in e1], [float(value) for value in e2]], dtype=float
    ).T
    velocity = {}
    base_coefficients = {}
    nonbase_velocity = {}
    for label in ids:
        if label in BASE:
            fitted, *_ = np.linalg.lstsq(basis, physical[index[label]], rcond=None)
            a, b = rationalize(fitted[0]), rationalize(fitted[1])
            velocity[label] = add(mul(e1, a), mul(e2, b))
            base_coefficients[str(label)] = [qs(a), qs(b)]
        else:
            velocity[label] = tuple(
                rationalize(value) for value in physical[index[label]]
            )
            nonbase_velocity[str(label)] = [qs(value) for value in velocity[label]]

    frozen_velocity = {
        int(label): tuple(Q(value) for value in xyz)
        for label, xyz in definition["velocity"].items()
    }
    if velocity != frozen_velocity:
        raise AssertionError("independently reconstructed exact velocity mismatch")
    if base_coefficients != definition["base_plane_coefficients"]:
        raise AssertionError("base projection coefficient mismatch")
    if nonbase_velocity != definition["nonbase_physical_velocity"]:
        raise AssertionError("non-base rationalization mismatch")

    candidate_array = np.asarray([candidate[label] for label in ids], dtype=float)
    exactified_t1 = np.asarray(
        [
            [float(source[label][axis] + velocity[label][axis]) for axis in range(3)]
            for label in ids
        ]
    )
    maximum_error = float(np.max(np.abs(exactified_t1 - candidate_array)))
    if maximum_error > 5e-12:
        raise AssertionError(("independent candidate closeness failed", maximum_error))
    return velocity, maximum_error


def family(name: str) -> str:
    if name.startswith("support:"):
        return "support"
    if name == "volume:d6" or name.startswith("face_reference:"):
        return "mechanics_denominator"
    if name.startswith("face_raw:"):
        return "face_component"
    if name.startswith("vertex:"):
        return "vertex_component"
    if name.startswith("edge"):
        return "edge_component"
    raise AssertionError(("unknown primitive family", name))


def independent_primitive_records(ledger, support_rows):
    records = [("volume:d6", ledger["d6"], True)]
    for face_index, witness, polynomial in support_rows:
        records.append((f"support:f{face_index}:w{witness}", polynomial, False))
    for face_key, values in sorted(ledger["reference"].items()):
        for edge, polynomial in sorted(values.items()):
            records.append(
                (
                    f"face_reference:{face_key}:{edge}",
                    polynomial,
                    False,
                )
            )
    for face_key, values in sorted(ledger["face"].items()):
        for edge, polynomial in sorted(values.items()):
            records.append(
                (
                    f"face_raw:{face_key}:{edge}",
                    polynomial,
                    False,
                )
            )
    for vertex, values in sorted(ledger["vertex"].items()):
        for neighbor, polynomial in sorted(values.items()):
            records.append((f"vertex:{vertex}:{neighbor}", polynomial, False))
    for edge, values in sorted(ledger["edge"].items()):
        for component in (
            "direction_norm2",
            "gram",
            "t",
            "one_minus_t",
            "beta1",
            "beta2",
        ):
            records.append(
                (
                    f"edge:{edge}:{component}",
                    values[component],
                    component in {"direction_norm2", "gram"},
                )
            )
    return records


def complete_interval_audit(ledger, support_rows):
    records = independent_primitive_records(ledger, support_rows)
    digest = hashlib.sha256()
    family_counts = {}
    sign_counts = {"positive": 0, "negative": 0}
    leaves = 0
    minimum = None
    for name, polynomial, intrinsically_positive in records:
        sign, row_leaves, margin = clean.bernstein_sign(
            polynomial, Q(0), STEP, max_depth=60
        )
        if intrinsically_positive and sign != 1:
            raise AssertionError(("nonpositive independent intrinsic primitive", name))
        row_family = family(name)
        family_counts[row_family] = family_counts.get(row_family, 0) + 1
        sign_counts["positive" if sign > 0 else "negative"] += 1
        leaves += row_leaves
        minimum = margin if minimum is None else min(minimum, margin)
        digest.update(
            f"{name}|{row_family}|{sign}|{'|'.join(polynomial.exact())}\n".encode()
        )
    if len(records) != 7904 or family_counts.get("support") != 5959:
        raise AssertionError(("independent complete ledger drift", len(records), family_counts))
    return {
        "lo": qs(Q(0)),
        "hi": qs(STEP),
        "primitive_count": len(records),
        "family_counts": family_counts,
        "sign_counts": sign_counts,
        "bernstein_leaf_count": leaves,
        "minimum_bernstein_log10_abs": minimum,
        "primitive_digest": digest.hexdigest(),
    }


def independent_checkpoint(points, faces):
    support = clean.supporting_cell(points, faces)
    ledger, mechanics = clean.classify_point(points, faces)
    incidence, _neighbors = clean.edge_data(faces)
    edges = set(incidence)
    support_edges = set(map(tuple, support["edges"]))
    if support_edges != edges:
        raise AssertionError("independent support/face edge ledgers disagree")
    missing = sorted(forced_rails() - edges)
    if support["f_vector"] != [61, 162, 103] or support["euler"] != 2:
        raise AssertionError(support)
    if support["active_labels"] != sorted(points) or len(points) != 61:
        raise AssertionError("independent active-row mismatch")
    if support["strict_support_count"] != 5959:
        raise AssertionError("independent support-row mismatch")
    if mechanics["class"] != [2, 2, 2]:
        raise AssertionError(mechanics)
    if mechanics["stable_faces"] != [sorted(BASE), list(TARGET_FACE)]:
        raise AssertionError(("independent stable-set mismatch", mechanics))
    if mechanics["unstable_vertices"] != [1, 8]:
        raise AssertionError(("independent unstable-set mismatch", mechanics))
    if mechanics["saddle_edges"] != [[4, 5], [12, 13]]:
        raise AssertionError(("independent saddle-set mismatch", mechanics))
    if missing:
        raise AssertionError(("independent mandatory-rail loss", missing))
    d6, m24 = clean.exact_centroid_numerators(points, faces)
    if d6 <= 0:
        raise AssertionError("independent nonpositive exact volume")
    centroid = tuple(value / (4 * d6) for value in m24)
    return {
        "exact_centroid": [qs(value) for value in centroid],
        "exact_centroid_digest": canonical_hash([qs(value) for value in centroid]),
        "exact_support": {key: value for key, value in support.items() if key != "edges"},
        "exact_mechanics": mechanics,
        "true_edge_count": len(edges),
        "forced_rail_count": len(forced_rails()),
        "missing_forced_rails": [],
    }


def residual_polynomials(ledger):
    face = clean.signed_face_components(ledger, tuple(sorted(TARGET_FACE)))
    vertex = ledger["vertex"][1]
    return {
        **{
            f"S[198,243,245]:edge({edge[0]},{edge[1]})": polynomial
            for edge, polynomial in sorted(face.items())
        },
        **{
            f"U1:neighbor({neighbor})": polynomial
            for neighbor, polynomial in sorted(vertex.items())
        },
        **{
            f"H({edge[0]},{edge[1]}):{component}": ledger["edge"][edge][component]
            for edge in TARGET_EDGES
            for component in EDGE_COMPONENTS
        },
    }


def independent_first_jet_oriented_polynomials(path, ledger, support_rows):
    rows = {}
    residuals = residual_polynomials(ledger)
    for name in sorted(ACTIVE_NAMES):
        rows[name] = (residuals[name], -1)

    lookup = {
        (face_index, witness): polynomial
        for face_index, witness, polynomial in support_rows
    }
    for face_index, witness in CIRCUIT_SUPPORT_ROWS:
        polynomial = lookup[(face_index, witness)]
        source_sign = 1 if polynomial.eval(Q(0)) > 0 else -1
        oriented = clean.Poly(tuple(source_sign * value for value in polynomial.c))
        rows[f"oriented_support:f{face_index}:w{witness}"] = (oriented, 1)

    a, b, c, d = CIRCUIT
    raw = clean.det3(
        clean.sub(path[b], path[a]),
        clean.sub(path[c], path[a]),
        clean.sub(path[d], path[a]),
    )
    source_sign = 1 if raw.eval(Q(0)) > 0 else -1
    determinant = clean.Poly(tuple(source_sign * value for value in raw.c))
    rows["oriented_circuit_determinant"] = (determinant, 1)
    if len(rows) != 7:
        raise AssertionError(("independent seven-row first-jet drift", len(rows)))
    return rows


def independent_first_jet_contract(path, ledger, support_rows):
    rows = {}
    for name, (oriented, required_derivative_sign) in sorted(
        independent_first_jet_oriented_polynomials(path, ledger, support_rows).items()
    ):
        derivative = oriented.derivative()
        good_derivative = (
            derivative
            if required_derivative_sign == 1
            else clean.Poly(tuple(-value for value in derivative.c))
        )
        source_value = oriented.eval(Q(0))
        directional_good_derivative = good_derivative.eval(Q(0))
        if source_value <= 0 or directional_good_derivative <= 0:
            raise AssertionError(("independent non-strict first-jet row", name))
        rows[name] = {
            "oriented_polynomial_digest": polynomial_hash(oriented),
            "good_derivative_polynomial_digest": polynomial_hash(good_derivative),
            "source_value": qs(source_value),
            "required_raw_derivative_sign": required_derivative_sign,
            "directional_good_derivative": qs(directional_good_derivative),
        }
    return {
        "schema": provenance.FIRST_JET_CONTRACT_SCHEMA,
        "version": provenance.FIRST_JET_CONTRACT_VERSION,
        "row_count": 7,
        "rows": rows,
        "digest": canonical_hash(rows),
    }


def independent_validate_parent(
    parent, *, source_snapshot, faces_snapshot, path, ledger, support_rows
):
    provenance.require_header(
        parent,
        schema=provenance.FIRST_JET_PATH_SCHEMA,
        version=provenance.FIRST_JET_PATH_VERSION,
        type_name=provenance.FIRST_JET_PATH_TYPE,
        verdict=provenance.FIRST_JET_PATH_VERDICT,
    )
    provenance.require_trust_packet(parent.get("producer_trust"), root=ROOT, role="search")
    if parent.get("source_sha256") != source_snapshot.sha256:
        raise AssertionError("independent parent/source hash mismatch")
    if parent.get("faces_sha256") != faces_snapshot.sha256:
        raise AssertionError("independent parent/faces hash mismatch")
    if parent.get("proposed_horizon_parameter") != "1":
        raise AssertionError("independent parent horizon mismatch")
    if "certified_step_parameter" in parent:
        raise AssertionError("independent parent falsely certifies a step")
    if parent.get("parameter_semantics") != "point(t) = exact_source + t * exact_velocity":
        raise AssertionError("independent parent parameter semantics mismatch")
    if parent.get("control_count") != 165:
        raise AssertionError("independent parent chart dimension mismatch")
    if len(parent.get("control_names", ())) != 165 or len(
        parent.get("exact_coefficients", ())
    ) != 165:
        raise AssertionError("independent parent control packet mismatch")
    rebuilt = independent_first_jet_contract(path, ledger, support_rows)
    if parent.get("first_jet_contract") != rebuilt:
        raise AssertionError("independent parent seven-row contract mismatch")
    expected_margins = {
        name: row["directional_good_derivative"]
        for name, row in rebuilt["rows"].items()
    }
    if parent.get("exact_first_jet_good_margins") != expected_margins:
        raise AssertionError("independent parent directional margins mismatch")
    return rebuilt


def independent_diagnostic_rows(path, ledger, support_rows):
    rows = {}
    for name, (oriented, required_derivative_sign) in (
        independent_first_jet_oriented_polynomials(path, ledger, support_rows).items()
    ):
        derivative = oriented.derivative()
        if required_derivative_sign == -1:
            derivative = clean.Poly(tuple(-value for value in derivative.c))
            name = f"active_residual:{name}"
        rows[name] = derivative
    if len(rows) != 7:
        raise AssertionError(("independent derivative packet drift", len(rows)))
    return rows


def independent_first_nonpositive_bracket(polynomial, horizon):
    if polynomial.eval(Q(0)) <= 0:
        raise AssertionError("independent derivative is not positive at source")

    def visit(lo, hi, depth):
        coefficients = clean.bernstein_coefficients(polynomial.affine(lo, hi))
        if all(value > 0 for value in coefficients):
            return None
        if hi - lo <= ROOT_WIDTH or depth >= 112:
            return lo, hi
        middle = (lo + hi) / 2
        left = visit(lo, middle, depth + 1)
        return left if left is not None else visit(middle, hi, depth + 1)

    return visit(Q(0), Q(horizon), 0)


def independent_derivative_horizon_semantics(path, ledger, support_rows):
    rows = independent_diagnostic_rows(path, ledger, support_rows)
    records = {}
    first_lowers = []
    for name, polynomial in sorted(rows.items()):
        bracket = independent_first_nonpositive_bracket(polynomial, Q(1))
        record = {
            "degree": polynomial.degree,
            "polynomial_digest": polynomial_hash(polynomial),
            "source_sign": 1,
            "source_value": qs(polynomial.eval(Q(0))),
        }
        if bracket is None:
            record["first_nonpositive_bracket"] = None
            record["strictly_positive_on_proposed_horizon"] = True
        else:
            lo, hi = bracket
            if lo <= 0:
                raise AssertionError(("independent nonpositive root lower bound", name))
            first_lowers.append(lo)
            record["first_nonpositive_bracket"] = [qs(lo), qs(hi)]
            record["strictly_positive_before_bracket"] = True
        records[name] = record
    if not first_lowers:
        raise AssertionError("independent diagnostic found no derivative wall")
    first_lower = min(first_lowers)
    safe_step = Q(1)
    while 2 * safe_step >= first_lower:
        safe_step /= 2
    if not (0 < safe_step < first_lower / 2):
        raise AssertionError("independent diagnostic safe-step mismatch")
    for name, polynomial in sorted(rows.items()):
        sign, leaves, margin = clean.bernstein_sign(
            polynomial, Q(0), safe_step, max_depth=60
        )
        if sign != 1:
            raise AssertionError(("independent unsafe diagnostic row", name))
        records[name]["safe_interval_bernstein_sign"] = sign
        records[name]["safe_interval_bernstein_leaves"] = leaves
        records[name]["safe_interval_minimum_log10_abs"] = margin
    return {
        "proposed_horizon_parameter": "1",
        "root_bracket_width": qs(ROOT_WIDTH),
        "first_wall_lower_bound": qs(first_lower),
        "certified_safe_step_parameter": qs(safe_step),
        "strict_factor_two_clearance": True,
        "rows": records,
    }


def independent_diagnostic_document(
    *, parent_path, parent_snapshot, source_snapshot, faces_snapshot,
    first_jet, semantics,
):
    return {
        "schema": provenance.DIAGNOSTIC_SCHEMA,
        "version": provenance.DIAGNOSTIC_VERSION,
        "type": provenance.DIAGNOSTIC_TYPE,
        "verdict": provenance.DIAGNOSTIC_VERDICT,
        "scope": (
            "Exact left-first Bernstein isolation of the first interval where "
            "strict positivity of each oriented target derivative cannot hold, "
            "followed by exact Bernstein proof on a strictly earlier dyadic interval."
        ),
        "parent_first_jet_path_file": provenance.relative_name(parent_path, ROOT),
        "parent_first_jet_path_sha256": parent_snapshot.sha256,
        "source_sha256": source_snapshot.sha256,
        "faces_sha256": faces_snapshot.sha256,
        "first_jet_contract_digest": first_jet["digest"],
        **semantics,
        "producer_trust": provenance.expected_trust_packet(ROOT, "diagnose"),
    }


def independent_certified_path_document(
    *, parent, parent_path, parent_snapshot, diagnostic_path,
    diagnostic_snapshot, safe_step,
):
    expected = dict(parent)
    expected.update({
        "schema": provenance.CERTIFIED_PATH_SCHEMA,
        "version": provenance.CERTIFIED_PATH_VERSION,
        "type": provenance.CERTIFIED_PATH_TYPE,
        "verdict": provenance.CERTIFIED_PATH_VERDICT,
        "method": (
            "The parent complete-chart first jet is retained exactly; left-first exact "
            "Bernstein isolation finds the first derivative wall and proves all seven "
            "required derivative signs on the declared substep."
        ),
        "parent_first_jet_path_sha256": parent_snapshot.sha256,
        "parent_first_jet_path_file": provenance.relative_name(parent_path, ROOT),
        "derivative_horizon_diagnostic_sha256": diagnostic_snapshot.sha256,
        "derivative_horizon_diagnostic_file": provenance.relative_name(
            diagnostic_path, ROOT
        ),
        "certified_step_parameter": qs(safe_step),
        "producer_trust": provenance.expected_trust_packet(ROOT, "diagnose"),
    })
    expected.pop("proposed_horizon_parameter", None)
    return expected


def residual_audit(ledger):
    records = {}
    for name, polynomial in sorted(residual_polynomials(ledger).items()):
        positive = clean.bernstein_sign(polynomial, Q(0), STEP, max_depth=60)
        if positive[0] != 1:
            raise AssertionError(("independent residual positivity", name))
        source_value = polynomial.eval(Q(0))
        endpoint_value = polynomial.eval(STEP)
        delta = endpoint_value - source_value
        row = {
            "polynomial_digest": polynomial_hash(polynomial),
            "source_value": qs(source_value),
            "endpoint_value": qs(endpoint_value),
            "delta_sign": 0 if not delta else (1 if delta > 0 else -1),
            "active": name in ACTIVE_NAMES,
        }
        if name in ACTIVE_NAMES:
            derivative = clean.bernstein_sign(
                polynomial.derivative(), Q(0), STEP, max_depth=60
            )
            if derivative[0] != -1 or delta >= 0:
                raise AssertionError(("independent active descent", name))
            row["derivative_sign"] = derivative[0]
        records[name] = row
    if len(records) != 14:
        raise AssertionError(("independent target packet size", len(records)))
    return records


def circuit_audit(path, support_rows):
    lookup = {
        (face_index, witness): polynomial
        for face_index, witness, polynomial in support_rows
    }
    support = {}
    for key in CIRCUIT_SUPPORT_ROWS:
        polynomial = lookup[key]
        source_sign = 1 if polynomial.eval(Q(0)) > 0 else -1
        oriented = clean.Poly(tuple(source_sign * value for value in polynomial.c))
        positive = clean.bernstein_sign(oriented, Q(0), STEP, max_depth=60)
        increasing = clean.bernstein_sign(
            oriented.derivative(), Q(0), STEP, max_depth=60
        )
        if positive[0] != 1 or increasing[0] != 1:
            raise AssertionError(("independent circuit support separation", key))
        support[f"support:f{key[0]}:w{key[1]}"] = {
            "polynomial_digest": polynomial_hash(oriented),
            "source_value": qs(oriented.eval(Q(0))),
            "endpoint_value": qs(oriented.eval(STEP)),
            "derivative_sign": increasing[0],
        }
    a, b, c, d = CIRCUIT
    raw = clean.det3(
        clean.sub(path[b], path[a]),
        clean.sub(path[c], path[a]),
        clean.sub(path[d], path[a]),
    )
    source_sign = 1 if raw.eval(Q(0)) > 0 else -1
    determinant = clean.Poly(tuple(source_sign * value for value in raw.c))
    positive = clean.bernstein_sign(determinant, Q(0), STEP, max_depth=60)
    increasing = clean.bernstein_sign(
        determinant.derivative(), Q(0), STEP, max_depth=60
    )
    if positive[0] != 1 or increasing[0] != 1:
        raise AssertionError("independent circuit determinant is not separating")
    return {
        "determinant": {
            "polynomial_digest": polynomial_hash(determinant),
            "source_value": qs(determinant.eval(Q(0))),
            "endpoint_value": qs(determinant.eval(STEP)),
            "derivative_sign": increasing[0],
        },
        "support_representatives": support,
    }


def compare_exact_rows(got, expected, context):
    if got != expected:
        raise AssertionError((context, got, expected))


def main() -> None:
    global SOURCE, PATH_DEFINITION, ENDPOINT, CERTIFICATE, VERIFICATION, STEP

    parser = argparse.ArgumentParser()
    parser.add_argument("--source", default=str(SOURCE))
    parser.add_argument("--path-definition", default=str(PATH_DEFINITION))
    parser.add_argument("--endpoint", default=str(ENDPOINT))
    parser.add_argument("--certificate", default=str(CERTIFICATE))
    parser.add_argument("--verification", default=str(VERIFICATION))
    args = parser.parse_args()

    SOURCE = provenance.contained_path(
        args.source, base=HERE, root=ROOT, context="verifier source"
    )
    PATH_DEFINITION = provenance.contained_path(
        args.path_definition, base=HERE, root=ROOT, context="verifier path definition"
    )
    ENDPOINT = provenance.contained_path(
        args.endpoint, base=HERE, root=ROOT, context="verifier endpoint"
    )
    CERTIFICATE = provenance.contained_path(
        args.certificate, base=HERE, root=ROOT, context="verifier certificate"
    )
    VERIFICATION = provenance.contained_path(
        args.verification, base=HERE, root=ROOT, context="verification output"
    )
    faces_path = provenance.contained_path(
        FACES_PATH, base=HERE, root=ROOT, context="faces"
    )
    rejected_certificate_path = provenance.contained_path(
        REJECTED_CERTIFICATE, base=HERE, root=ROOT, context="rejected certificate"
    )
    rejected_path = provenance.contained_path(
        REJECTED_PATH, base=HERE, root=ROOT, context="rejected path"
    )
    proposal_path = provenance.contained_path(
        PROPOSAL, base=HERE, root=ROOT, context="proposal"
    )
    candidate_path = provenance.contained_path(
        CANDIDATE, base=HERE, root=ROOT, context="candidate"
    )
    default_source = provenance.contained_path(
        DEFAULT_SOURCE, base=HERE, root=ROOT, context="default source"
    )
    default_verification = provenance.contained_path(
        HERE / "exactification_verification.json",
        base=HERE,
        root=ROOT,
        context="default verification",
    )

    source_snapshot = provenance.read_snapshot(SOURCE)
    definition_snapshot = provenance.read_snapshot(PATH_DEFINITION)
    endpoint_snapshot = provenance.read_snapshot(ENDPOINT)
    certificate_snapshot = provenance.read_snapshot(CERTIFICATE)
    faces_snapshot = provenance.read_snapshot(faces_path)
    rejected_certificate_snapshot = provenance.read_snapshot(rejected_certificate_path)
    rejected_path_snapshot = provenance.read_snapshot(rejected_path)
    definition = provenance.parse_json(definition_snapshot)
    certificate = provenance.parse_json(certificate_snapshot)
    provenance.require_header(
        definition,
        schema=provenance.CERTIFIED_PATH_SCHEMA,
        version=provenance.CERTIFIED_PATH_VERSION,
        type_name=provenance.CERTIFIED_PATH_TYPE,
        verdict=provenance.CERTIFIED_PATH_VERDICT,
    )
    provenance.require_header(
        certificate,
        schema=provenance.CERTIFICATE_SCHEMA,
        version=provenance.CERTIFICATE_VERSION,
        type_name=provenance.CERTIFICATE_TYPE,
        verdict=provenance.CERTIFICATE_VERDICT,
    )
    provenance.require_trust_packet(
        definition.get("producer_trust"), root=ROOT, role="diagnose"
    )
    provenance.require_trust_packet(
        certificate.get("producer_trust"), root=ROOT, role="builder"
    )
    parent_path = provenance.stored_path(
        definition.get("parent_first_jet_path_file"),
        root=ROOT,
        context="verifier first-jet parent",
    )
    diagnostic_path = provenance.stored_path(
        definition.get("derivative_horizon_diagnostic_file"),
        root=ROOT,
        context="verifier derivative diagnostic",
    )
    parent_snapshot = provenance.read_snapshot(parent_path)
    diagnostic_snapshot = provenance.read_snapshot(diagnostic_path)
    parent_definition = provenance.parse_json(parent_snapshot)
    diagnostic = provenance.parse_json(diagnostic_snapshot)

    dynamic_source = SOURCE != default_source
    lineage_evidence = None
    lineage = definition.get("source_lineage")
    if dynamic_source and lineage is None:
        raise AssertionError("a nondefault source lacks certified lineage")
    if lineage is not None:
        lineage_certificate_path, lineage_verification_path = provenance.lineage_paths(
            lineage, root=ROOT
        )
        lineage_evidence = provenance.validate_dynamic_lineage(
            root=ROOT,
            current_source=source_snapshot,
            certificate_snapshot=provenance.read_snapshot(lineage_certificate_path),
            verification_snapshot=provenance.read_snapshot(lineage_verification_path),
        )
        if lineage != lineage_evidence.payload:
            raise AssertionError("independent dynamic-source lineage mismatch")

    has_proposal = provenance.require_paired_fields(
        definition, "proposal_sha256", "candidate_sha256"
    )
    has_candidate = has_proposal
    proposal_snapshot = provenance.read_snapshot(proposal_path) if has_proposal else None
    candidate_snapshot = provenance.read_snapshot(candidate_path) if has_candidate else None
    builder_trust_snapshots = provenance.trusted_code_snapshots(ROOT, "builder")

    manifest_snapshots = [
        source_snapshot,
        definition_snapshot,
        faces_snapshot,
        rejected_certificate_snapshot,
        rejected_path_snapshot,
        parent_snapshot,
        diagnostic_snapshot,
        *builder_trust_snapshots,
    ]
    if proposal_snapshot is not None:
        manifest_snapshots.extend((proposal_snapshot, candidate_snapshot))
    if lineage_evidence is not None:
        manifest_snapshots.extend(lineage_evidence.snapshots)

    input_paths = [snapshot.path for snapshot in manifest_snapshots]
    input_paths.extend((ENDPOINT, CERTIFICATE, CLEAN_MODULE))
    protected_defaults = [default_verification] if dynamic_source else []
    trust_paths = [
        provenance.role_path(ROOT, "search"),
        provenance.role_path(ROOT, "diagnose"),
        provenance.role_path(ROOT, "verifier"),
    ]
    provenance.assert_isolated(
        [VERIFICATION, *input_paths, *trust_paths, *protected_defaults],
        "independent verifier",
    )
    verifier_snapshot = provenance.read_snapshot(Path(__file__).resolve())
    helper_snapshot = builder_trust_snapshots[0]
    all_input_snapshots = [
        *manifest_snapshots,
        endpoint_snapshot,
        certificate_snapshot,
        _CLEAN_SNAPSHOT,
        verifier_snapshot,
        helper_snapshot,
    ]
    provenance.assert_snapshots_current(all_input_snapshots)

    source = provenance.parse_exact_csv(source_snapshot)
    endpoint_file = provenance.parse_exact_csv(endpoint_snapshot)
    faces = provenance.parse_json(faces_snapshot)
    STEP = Q(certificate["path"]["step_parameter"])

    if certificate["winner_status"] != "NONWINNER":
        raise AssertionError("winner status drift")
    if definition["source_sha256"] != source_snapshot.sha256:
        raise AssertionError("definition/source hash mismatch")
    if definition["faces_sha256"] != faces_snapshot.sha256:
        raise AssertionError("definition/faces hash mismatch")
    if definition.get("rejected_event_certificate_sha256") != rejected_certificate_snapshot.sha256:
        raise AssertionError("definition/rejected-certificate hash mismatch")
    if definition.get("sparse_path_sha256") != rejected_path_snapshot.sha256:
        raise AssertionError("definition/rejected-path hash mismatch")
    if certificate.get("source") != {
        "file": provenance.relative_name(SOURCE, ROOT),
        "sha256": source_snapshot.sha256,
    }:
        raise AssertionError("certificate source record mismatch")
    if certificate["path"].get("path_definition_file") != provenance.relative_name(
        PATH_DEFINITION, ROOT
    ):
        raise AssertionError("certificate path-definition file mismatch")
    if certificate["path"]["path_definition_sha256"] != definition_snapshot.sha256:
        raise AssertionError("certificate/path-definition hash mismatch")
    if certificate["path"]["velocity_digest"] != definition["velocity_digest"]:
        raise AssertionError("certificate/definition velocity mismatch")
    expected_manifest = {
        provenance.relative_name(snapshot.path, ROOT): snapshot.sha256
        for snapshot in manifest_snapshots
    }
    if certificate.get("source_file_sha256") != expected_manifest:
        raise AssertionError("certificate source manifest is not exact")
    if certificate["path"]["step_parameter"] != qs(STEP):
        raise AssertionError("certificate step mismatch")
    if certificate["path"]["step_parameter"] != definition.get("certified_step_parameter"):
        raise AssertionError("certificate/definition step mismatch")
    if certificate["path"].get("nonzero") is not True:
        raise AssertionError("certificate path nonzero flag mismatch")

    if has_proposal:
        if definition["proposal_sha256"] != proposal_snapshot.sha256:
            raise AssertionError("definition/proposal hash mismatch")
        if definition["candidate_sha256"] != candidate_snapshot.sha256:
            raise AssertionError("definition/candidate hash mismatch")
        proposal = provenance.parse_json(proposal_snapshot)
        candidate = read_float_csv(candidate_snapshot)
        velocity, candidate_error = reconstruct_velocity(
            source, proposal, definition, candidate
        )
    else:
        velocity = {
            int(label): tuple(Q(value) for value in xyz)
            for label, xyz in definition["velocity"].items()
        }
        candidate_error = None
        if set(velocity) != set(source) or all(
            not any(xyz) for xyz in velocity.values()
        ):
            raise AssertionError("declared exact velocity is zero or incomplete")
    velocity_packet = {
        str(label): [qs(value) for value in velocity[label]] for label in sorted(velocity)
    }
    if canonical_hash(velocity_packet) != definition["velocity_digest"]:
        raise AssertionError("independent velocity digest mismatch")

    e1 = sub(source[1], source[0])
    e2 = sub(source[2], source[0])
    normal = cross(e1, e2)
    for label in BASE:
        if dot(normal, sub(source[label], source[0])):
            raise AssertionError(("independent source planarity", label))
        if dot(normal, velocity[label]):
            raise AssertionError(("independent velocity planarity", label))

    path = {
        label: tuple(
            clean.Poly((source[label][axis], velocity[label][axis]))
            for axis in range(3)
        )
        for label in source
    }
    endpoint = evaluate_path(path, STEP)
    if endpoint_file != endpoint:
        raise AssertionError("generated endpoint does not equal exact path evaluation")
    if certificate["generated_file_sha256"] != {
        provenance.relative_name(ENDPOINT, ROOT): endpoint_snapshot.sha256
    }:
        raise AssertionError("generated endpoint hash mismatch")

    ledger = clean.mechanics_primitives(path, faces)
    support_rows = list(clean.support_polynomials(path, faces))
    parent_velocity = {
        int(label): tuple(Q(value) for value in xyz)
        for label, xyz in parent_definition["velocity"].items()
    }
    parent_velocity_packet = {
        str(label): [qs(value) for value in parent_velocity[label]]
        for label in sorted(parent_velocity)
    }
    if (
        set(parent_velocity) != set(source)
        or parent_velocity != velocity
        or canonical_hash(parent_velocity_packet) != parent_definition.get("velocity_digest")
    ):
        raise AssertionError("independent parent/certified velocity mismatch")
    first_jet = independent_validate_parent(
        parent_definition,
        source_snapshot=source_snapshot,
        faces_snapshot=faces_snapshot,
        path=path,
        ledger=ledger,
        support_rows=support_rows,
    )
    semantics = independent_derivative_horizon_semantics(path, ledger, support_rows)
    expected_diagnostic = independent_diagnostic_document(
        parent_path=parent_path,
        parent_snapshot=parent_snapshot,
        source_snapshot=source_snapshot,
        faces_snapshot=faces_snapshot,
        first_jet=first_jet,
        semantics=semantics,
    )
    provenance.require_exact_document(
        diagnostic, expected_diagnostic, "independent diagnostic complete semantics"
    )
    expected_definition = independent_certified_path_document(
        parent=parent_definition,
        parent_path=parent_path,
        parent_snapshot=parent_snapshot,
        diagnostic_path=diagnostic_path,
        diagnostic_snapshot=diagnostic_snapshot,
        safe_step=Q(semantics["certified_safe_step_parameter"]),
    )
    provenance.require_exact_document(
        definition, expected_definition, "independent certified-path transformation"
    )

    print("independently reconstructing maximal faces", flush=True)
    source_fresh, source_hull = clean.fresh_maximal_faces(source)
    endpoint_fresh, endpoint_hull = clean.fresh_maximal_faces(endpoint)
    if face_keys(source_fresh) != face_keys(faces):
        raise AssertionError("source exact maximal-face reconstruction mismatch")
    if face_keys(endpoint_fresh) != face_keys(faces):
        raise AssertionError("endpoint exact maximal-face reconstruction mismatch")

    source_checkpoint = independent_checkpoint(source, faces)
    endpoint_checkpoint = independent_checkpoint(endpoint, faces)
    for name, rebuilt in (
        ("source", source_checkpoint),
        ("endpoint", endpoint_checkpoint),
    ):
        frozen = certificate["rational_checkpoints"][name]
        compare_exact_rows(rebuilt["exact_centroid"], frozen["exact_centroid"], f"{name} centroid")
        compare_exact_rows(rebuilt["exact_support"], frozen["exact_support"], f"{name} support")
        compare_exact_rows(rebuilt["exact_mechanics"], frozen["exact_mechanics"], f"{name} mechanics")
        if rebuilt["true_edge_count"] != frozen["true_edge_count"]:
            raise AssertionError((name, "edge count mismatch"))
        if rebuilt["missing_forced_rails"] != []:
            raise AssertionError((name, "rail mismatch"))

    print("constructing independent own-centroid polynomial ledger", flush=True)
    print("independently auditing all exact primitives", flush=True)
    interval = complete_interval_audit(ledger, support_rows)
    frozen_interval = certificate["complete_interval_audit"]
    if interval != frozen_interval:
        raise AssertionError(("complete interval audit mismatch", interval, frozen_interval))
    frozen_cover = certificate["own_centroid_class_cover"]
    if (
        frozen_cover.get("certified_polynomial_count") != interval["primitive_count"]
        or frozen_cover.get("complete_interval_primitive_digest")
        != interval["primitive_digest"]
        or frozen_cover.get("source_class") != certificate["rational_checkpoints"]["source"]["exact_mechanics"]
        or frozen_cover.get("endpoint_class") != certificate["rational_checkpoints"]["endpoint"]["exact_mechanics"]
        or frozen_cover.get("class_constant_on_closed_segment") is not True
    ):
        raise AssertionError("own-centroid class-cover audit mismatch")

    residuals = residual_audit(ledger)
    frozen_residuals = certificate["target_residual_packet"]["components"]
    for name, rebuilt in residuals.items():
        frozen = frozen_residuals[name]
        for key in (
            "polynomial_digest",
            "source_value",
            "endpoint_value",
            "delta_sign",
            "active",
        ):
            if rebuilt[key] != frozen[key]:
                raise AssertionError(("residual mismatch", name, key))
        if rebuilt.get("derivative_sign") != frozen.get("derivative_sign"):
            raise AssertionError(("residual derivative mismatch", name))

    circuit = circuit_audit(path, support_rows)
    frozen_circuit = certificate["rejected_rail255256_circuit_guard"]
    for key in ("polynomial_digest", "source_value", "endpoint_value", "derivative_sign"):
        if circuit["determinant"][key] != frozen_circuit["determinant"][key]:
            raise AssertionError(("circuit determinant mismatch", key))
    for name, rebuilt in circuit["support_representatives"].items():
        frozen = frozen_circuit["support_representatives"][name]
        for key in ("polynomial_digest", "source_value", "endpoint_value", "derivative_sign"):
            if rebuilt[key] != frozen[key]:
                raise AssertionError(("circuit support mismatch", name, key))

    verification = {
        "schema": provenance.VERIFICATION_SCHEMA,
        "version": provenance.VERIFICATION_VERSION,
        "type": provenance.VERIFICATION_TYPE,
        "verdict": provenance.VERIFICATION_VERDICT,
        "certificate_file": provenance.relative_name(CERTIFICATE, ROOT),
        "certificate_sha256": certificate_snapshot.sha256,
        "source_file": provenance.relative_name(SOURCE, ROOT),
        "source_sha256": source_snapshot.sha256,
        "path_definition_file": provenance.relative_name(PATH_DEFINITION, ROOT),
        "path_definition_sha256": definition_snapshot.sha256,
        "endpoint_file": provenance.relative_name(ENDPOINT, ROOT),
        "endpoint_sha256": endpoint_snapshot.sha256,
        "verifier_script_sha256": verifier_snapshot.sha256,
        "clean_exact_module_sha256": _CLEAN_SNAPSHOT.sha256,
        "independent_candidate_max_abs_error": candidate_error,
        "independent_velocity_digest": canonical_hash(velocity_packet),
        "fresh_source_hull": source_hull,
        "fresh_endpoint_hull": endpoint_hull,
        "complete_interval_audit": interval,
        "source_exact_centroid_digest": source_checkpoint["exact_centroid_digest"],
        "endpoint_exact_centroid_digest": endpoint_checkpoint["exact_centroid_digest"],
        "endpoint_class": endpoint_checkpoint["exact_mechanics"]["class"],
        "endpoint_f_vector": endpoint_checkpoint["exact_support"]["f_vector"],
        "active_row_count": len(endpoint_checkpoint["exact_support"]["active_labels"]),
        "forced_rail_count": endpoint_checkpoint["forced_rail_count"],
        "missing_forced_rails": [],
        "target_residual_component_count": len(residuals),
        "active_residual_count": len(ACTIVE_NAMES),
        "circuit_determinant": circuit["determinant"],
        "open_neighborhood_reconstructed": True,
        "winner": False,
        "producer_trust": provenance.expected_trust_packet(ROOT, "verifier"),
    }
    provenance.assert_snapshots_current(all_input_snapshots)
    verification_snapshot = provenance.atomic_write_json(VERIFICATION, verification)
    provenance.assert_snapshots_current(
        [*all_input_snapshots, verification_snapshot]
    )
    print(verification["verdict"])
    print("independent_primitive_count", interval["primitive_count"])
    print("independent_support_count", interval["family_counts"]["support"])
    print("endpoint_f_vector", verification["endpoint_f_vector"])
    print("endpoint_class", verification["endpoint_class"])
    print("missing_rails", verification["missing_forced_rails"])
    print("verification_sha256", verification_snapshot.sha256)


if __name__ == "__main__":
    main()
