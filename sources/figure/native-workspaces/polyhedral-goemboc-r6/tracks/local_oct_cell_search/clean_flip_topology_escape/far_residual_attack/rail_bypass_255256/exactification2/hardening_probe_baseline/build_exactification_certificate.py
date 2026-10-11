#!/usr/bin/env python3
"""Build the exact nonzero rail-bypass material-step certificate.

The witness is the exact rational projection emitted by
``derive_exact_candidate.py``.  This builder proves every support and
own-centroid mechanics primitive on the full interval 0 <= t <= 1/4.  No
finite-difference, sampled-only, or one-sided argument is used.
"""
from __future__ import annotations

import argparse
import hashlib
import sys
from fractions import Fraction as Q
from pathlib import Path


sys.set_int_max_str_digits(0)

HERE = Path(__file__).resolve().parent
RAIL = HERE.parent
PARENT = RAIL.parent
ROOT = HERE.parents[5]
EXACT_CORE = ROOT / "tracks/global_carrier_support/rigorous_local_bypass"
sys.path.insert(0, str(EXACT_CORE))

import exact_core as ex  # noqa: E402
import exactification_provenance as provenance  # noqa: E402


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

STEP = Q(1, 4)
ROOT_WIDTH = Q(1, 2**96)
BASE = frozenset(range(17)) | {54}
TARGET_FACE = (198, 243, 245)
TARGET_VERTEX = 1
TARGET_EDGES = ((4, 5), (12, 13))
EDGE_COMPONENTS = ("t", "one_minus_t", "beta1", "beta2")
PROTECTED = {
    "stable": [sorted(BASE), list(TARGET_FACE)],
    "unstable": [1, 8],
    "saddles": [[4, 5], [12, 13]],
}
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


def evaluate_path(path, parameter: Q):
    return {
        label: tuple(coordinate.eval(parameter) for coordinate in xyz)
        for label, xyz in path.items()
    }


def exact_velocity(definition, source):
    velocity = {
        int(label): tuple(Q(value) for value in xyz)
        for label, xyz in definition["velocity"].items()
    }
    if set(velocity) != set(source) or all(not any(xyz) for xyz in velocity.values()):
        raise AssertionError("zero or incomplete exact velocity")
    packet = {
        str(label): [ex.qs(value) for value in velocity[label]]
        for label in sorted(velocity)
    }
    if canonical_hash(packet) != definition.get("velocity_digest"):
        raise AssertionError("exact velocity digest mismatch")
    return velocity, packet


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


def primitive_rows(ledger, support_rows):
    yield "volume:d6", ledger["d6"], "mechanics_denominator", True
    for face_index, witness, polynomial in support_rows:
        yield f"support:f{face_index}:w{witness}", polynomial, "support", False
    for face_key, values in sorted(ledger["reference"].items()):
        for edge, polynomial in sorted(values.items()):
            yield (
                f"face_reference:{face_key}:{edge}",
                polynomial,
                "mechanics_denominator",
                False,
            )
    for face_key, values in sorted(ledger["face"].items()):
        for edge, polynomial in sorted(values.items()):
            yield f"face_raw:{face_key}:{edge}", polynomial, "face_component", False
    for vertex, values in sorted(ledger["vertex"].items()):
        for neighbor, polynomial in sorted(values.items()):
            yield f"vertex:{vertex}:{neighbor}", polynomial, "vertex_component", False
    for edge, values in sorted(ledger["edge"].items()):
        for component in (
            "direction_norm2",
            "gram",
            "t",
            "one_minus_t",
            "beta1",
            "beta2",
        ):
            yield (
                f"edge:{edge}:{component}",
                values[component],
                "edge_component",
                component in {"direction_norm2", "gram"},
            )


def strict_interval(rows, lo: Q, hi: Q):
    digest = hashlib.sha256()
    family_counts = {}
    sign_counts = {"positive": 0, "negative": 0}
    primitive_count = 0
    leaf_count = 0
    minimum = None
    for name, polynomial, family, intrinsically_positive in rows:
        sign, leaves, margin = ex.bernstein_sign(
            polynomial, lo, hi, max_depth=60
        )
        if intrinsically_positive and sign != 1:
            raise AssertionError(("nonpositive intrinsic primitive", name))
        primitive_count += 1
        leaf_count += leaves
        minimum = margin if minimum is None else min(minimum, margin)
        family_counts[family] = family_counts.get(family, 0) + 1
        sign_counts["positive" if sign > 0 else "negative"] += 1
        digest.update(
            f"{name}|{family}|{sign}|{'|'.join(polynomial.exact())}\n".encode()
        )
    if family_counts.get("support") != 5959 or primitive_count != 7904:
        raise AssertionError(("complete primitive ledger drift", primitive_count, family_counts))
    return {
        "lo": ex.qs(lo),
        "hi": ex.qs(hi),
        "primitive_count": primitive_count,
        "family_counts": family_counts,
        "sign_counts": sign_counts,
        "bernstein_leaf_count": leaf_count,
        "minimum_bernstein_log10_abs": minimum,
        "primitive_digest": digest.hexdigest(),
    }


def residual_polynomials(ledger):
    face = ex.signed_face_components(ledger, tuple(sorted(TARGET_FACE)))
    vertex = ledger["vertex"][TARGET_VERTEX]
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


def first_jet_oriented_polynomials(path, ledger, support_rows):
    rows = {}
    residuals = residual_polynomials(ledger)
    for name in sorted(ACTIVE_NAMES):
        rows[name] = (residuals[name], -1)

    support_lookup = {
        (face_index, witness): polynomial
        for face_index, witness, polynomial in support_rows
    }
    for face_index, witness in CIRCUIT_SUPPORT_ROWS:
        polynomial = support_lookup[(face_index, witness)]
        source_sign = 1 if polynomial.eval(Q(0)) > 0 else -1
        oriented = ex.P(tuple(source_sign * value for value in polynomial.c))
        rows[f"oriented_support:f{face_index}:w{witness}"] = (oriented, 1)

    a, b, c, d = CIRCUIT
    raw = ex.det3(
        ex.sub(path[b], path[a]),
        ex.sub(path[c], path[a]),
        ex.sub(path[d], path[a]),
    )
    source_sign = 1 if raw.eval(Q(0)) > 0 else -1
    determinant = ex.P(tuple(source_sign * value for value in raw.c))
    rows["oriented_circuit_determinant"] = (determinant, 1)
    if len(rows) != 7:
        raise AssertionError(("seven-row first-jet family drift", len(rows)))
    return rows


def first_jet_contract(path, ledger, support_rows):
    rows = {}
    for name, (oriented, required_derivative_sign) in sorted(
        first_jet_oriented_polynomials(path, ledger, support_rows).items()
    ):
        derivative = oriented.derivative()
        good_derivative = (
            derivative
            if required_derivative_sign == 1
            else ex.P(tuple(-value for value in derivative.c))
        )
        source_value = oriented.eval(Q(0))
        directional_good_derivative = good_derivative.eval(Q(0))
        if source_value <= 0 or directional_good_derivative <= 0:
            raise AssertionError(("non-strict first-jet row", name))
        rows[name] = {
            "oriented_polynomial_digest": polynomial_hash(oriented),
            "good_derivative_polynomial_digest": polynomial_hash(good_derivative),
            "source_value": ex.qs(source_value),
            "required_raw_derivative_sign": required_derivative_sign,
            "directional_good_derivative": ex.qs(directional_good_derivative),
        }
    return {
        "schema": provenance.FIRST_JET_CONTRACT_SCHEMA,
        "version": provenance.FIRST_JET_CONTRACT_VERSION,
        "row_count": 7,
        "rows": rows,
        "digest": canonical_hash(rows),
    }


def validate_first_jet_parent(parent, *, source_snapshot, faces_snapshot, path, ledger, support_rows):
    provenance.require_header(
        parent,
        schema=provenance.FIRST_JET_PATH_SCHEMA,
        version=provenance.FIRST_JET_PATH_VERSION,
        type_name=provenance.FIRST_JET_PATH_TYPE,
        verdict=provenance.FIRST_JET_PATH_VERDICT,
    )
    provenance.require_trust_packet(parent.get("producer_trust"), root=ROOT, role="search")
    if parent.get("source_sha256") != source_snapshot.sha256:
        raise AssertionError("first-jet parent/source hash mismatch")
    if parent.get("faces_sha256") != faces_snapshot.sha256:
        raise AssertionError("first-jet parent/faces hash mismatch")
    if parent.get("proposed_horizon_parameter") != "1":
        raise AssertionError("first-jet parent must declare horizon one")
    if "certified_step_parameter" in parent:
        raise AssertionError("first-jet parent falsely declares a certified step")
    if parent.get("parameter_semantics") != "point(t) = exact_source + t * exact_velocity":
        raise AssertionError("first-jet parent parameter semantics mismatch")
    if parent.get("control_count") != 165:
        raise AssertionError("first-jet parent chart dimension mismatch")
    if len(parent.get("control_names", ())) != 165 or len(
        parent.get("exact_coefficients", ())
    ) != 165:
        raise AssertionError("first-jet parent control packet mismatch")
    rebuilt = first_jet_contract(path, ledger, support_rows)
    if parent.get("first_jet_contract") != rebuilt:
        raise AssertionError("first-jet parent seven-row contract mismatch")
    expected_margins = {
        name: row["directional_good_derivative"]
        for name, row in rebuilt["rows"].items()
    }
    if parent.get("exact_first_jet_good_margins") != expected_margins:
        raise AssertionError("first-jet parent directional margins mismatch")
    return rebuilt


def diagnostic_derivative_rows(path, ledger, support_rows):
    rows = {}
    for name, (oriented, required_derivative_sign) in first_jet_oriented_polynomials(
        path, ledger, support_rows
    ).items():
        derivative = oriented.derivative()
        if required_derivative_sign == -1:
            derivative = ex.P(tuple(-value for value in derivative.c))
            name = f"active_residual:{name}"
        rows[name] = derivative
    if len(rows) != 7:
        raise AssertionError(("seven-row derivative packet drift", len(rows)))
    return rows


def first_nonpositive_bracket(polynomial, horizon):
    if polynomial.eval(Q(0)) <= 0:
        raise AssertionError("oriented derivative is not positive at source")

    def visit(lo, hi, depth):
        coefficients = ex.bernstein_coefficients(polynomial.affine(lo, hi))
        if all(value > 0 for value in coefficients):
            return None
        if hi - lo <= ROOT_WIDTH or depth >= 112:
            return lo, hi
        middle = (lo + hi) / 2
        left = visit(lo, middle, depth + 1)
        return left if left is not None else visit(middle, hi, depth + 1)

    return visit(Q(0), Q(horizon), 0)


def derivative_horizon_semantics(path, ledger, support_rows):
    rows = diagnostic_derivative_rows(path, ledger, support_rows)
    records = {}
    first_lowers = []
    for name, polynomial in sorted(rows.items()):
        bracket = first_nonpositive_bracket(polynomial, Q(1))
        record = {
            "degree": polynomial.degree,
            "polynomial_digest": polynomial_hash(polynomial),
            "source_sign": 1,
            "source_value": ex.qs(polynomial.eval(Q(0))),
        }
        if bracket is None:
            record["first_nonpositive_bracket"] = None
            record["strictly_positive_on_proposed_horizon"] = True
        else:
            lo, hi = bracket
            if lo <= 0:
                raise AssertionError(("nonpositive first-root lower bound", name))
            first_lowers.append(lo)
            record["first_nonpositive_bracket"] = [ex.qs(lo), ex.qs(hi)]
            record["strictly_positive_before_bracket"] = True
        records[name] = record

    if not first_lowers:
        raise AssertionError("no derivative wall found on proposed horizon")
    first_lower = min(first_lowers)
    safe_step = Q(1)
    while 2 * safe_step >= first_lower:
        safe_step /= 2
    if not (0 < safe_step < first_lower / 2):
        raise AssertionError(("unsafe dyadic step", ex.qs(safe_step), ex.qs(first_lower)))

    for name, polynomial in sorted(rows.items()):
        sign, leaves, margin = ex.bernstein_sign(
            polynomial, Q(0), safe_step, max_depth=60
        )
        if sign != 1:
            raise AssertionError(("derivative not positive on safe step", name))
        records[name]["safe_interval_bernstein_sign"] = sign
        records[name]["safe_interval_bernstein_leaves"] = leaves
        records[name]["safe_interval_minimum_log10_abs"] = margin
    return {
        "proposed_horizon_parameter": "1",
        "root_bracket_width": ex.qs(ROOT_WIDTH),
        "first_wall_lower_bound": ex.qs(first_lower),
        "certified_safe_step_parameter": ex.qs(safe_step),
        "strict_factor_two_clearance": True,
        "rows": records,
    }


def diagnostic_document(
    *, parent_path, parent_snapshot, source_snapshot, faces_snapshot,
    first_jet, semantics, producer_trust,
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
        "producer_trust": producer_trust,
    }


def certified_path_document(
    *, parent, parent_path, parent_snapshot, diagnostic_path,
    diagnostic_snapshot, safe_step, producer_trust,
):
    certified = dict(parent)
    certified.update({
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
        "certified_step_parameter": ex.qs(safe_step),
        "producer_trust": producer_trust,
    })
    certified.pop("proposed_horizon_parameter", None)
    return certified


def residual_packet_audit(ledger):
    records = {}
    for name, polynomial in sorted(residual_polynomials(ledger).items()):
        sign, leaves, margin = ex.bernstein_sign(polynomial, Q(0), STEP, max_depth=60)
        if sign != 1:
            raise AssertionError(("target residual lost positivity", name, sign))
        source_value = polynomial.eval(Q(0))
        endpoint_value = polynomial.eval(STEP)
        delta = endpoint_value - source_value
        record = {
            "degree": polynomial.degree,
            "polynomial_digest": polynomial_hash(polynomial),
            "positive_bernstein_leaves": leaves,
            "positive_minimum_bernstein_log10_abs": margin,
            "source_value": ex.qs(source_value),
            "endpoint_value": ex.qs(endpoint_value),
            "endpoint_over_source_decimal": float(endpoint_value / source_value),
            "delta_sign": 0 if not delta else (1 if delta > 0 else -1),
            "active": name in ACTIVE_NAMES,
        }
        if name in ACTIVE_NAMES:
            derivative = ex.bernstein_sign(
                polynomial.derivative(), Q(0), STEP, max_depth=60
            )
            if derivative[0] != -1 or delta >= 0:
                raise AssertionError(("active residual is not strictly decreasing", name))
            record.update(
                {
                    "derivative_sign": derivative[0],
                    "derivative_bernstein_leaves": derivative[1],
                    "derivative_minimum_bernstein_log10_abs": derivative[2],
                    "strict_relative_decrease_decimal": float(
                        (source_value - endpoint_value) / source_value
                    ),
                }
            )
        records[name] = record
    if len(records) != 14:
        raise AssertionError(("target residual packet size", len(records)))
    if {name for name, row in records.items() if row["active"]} != ACTIVE_NAMES:
        raise AssertionError("active residual family mismatch")
    return {
        "component_count": len(records),
        "active_component_count": len(ACTIVE_NAMES),
        "components": records,
    }


def point_mechanics_rows(ledger):
    yield "volume:d6", ledger["d6"]
    for face_key, values in sorted(ledger["reference"].items()):
        for edge, value in sorted(values.items()):
            yield f"face_reference:{face_key}:{edge}", value
    for face_key, values in sorted(ledger["face"].items()):
        for edge, value in sorted(values.items()):
            yield f"face_raw:{face_key}:{edge}", value
    for vertex, values in sorted(ledger["vertex"].items()):
        for neighbor, value in sorted(values.items()):
            yield f"vertex:{vertex}:{neighbor}", value
    for edge, values in sorted(ledger["edge"].items()):
        for component in (
            "direction_norm2",
            "gram",
            "t",
            "one_minus_t",
            "beta1",
            "beta2",
        ):
            yield f"edge:{edge}:{component}", values[component]


def checkpoint(points, faces):
    support = ex.supporting_cell(points, faces)
    ledger, mechanics = ex.classify_point(points, faces)
    edges = set(map(tuple, support["edges"]))
    if support["f_vector"] != [61, 162, 103] or support["euler"] != 2:
        raise AssertionError(support)
    if support["active_labels"] != sorted(points) or len(points) != 61:
        raise AssertionError("active-row mismatch")
    if support["strict_support_count"] != 5959:
        raise AssertionError("support-row count drift")
    if mechanics["class"] != [2, 2, 2]:
        raise AssertionError(mechanics)
    if mechanics["stable_faces"] != PROTECTED["stable"]:
        raise AssertionError(("stable set drift", mechanics))
    if mechanics["unstable_vertices"] != PROTECTED["unstable"]:
        raise AssertionError(("unstable set drift", mechanics))
    if mechanics["saddle_edges"] != PROTECTED["saddles"]:
        raise AssertionError(("saddle set drift", mechanics))
    if BASE not in {frozenset(face) for face in faces}:
        raise AssertionError("enlarged base missing")
    missing = sorted(forced_rails() - edges)
    if missing:
        raise AssertionError(("mandatory rail missing", missing))
    d6, m24 = ex.exact_centroid_numerators(points, faces)
    if d6 <= 0:
        raise AssertionError("nonpositive exact volume")
    centroid = tuple(value / (4 * d6) for value in m24)
    mechanics_rows = list(point_mechanics_rows(ledger))
    complete_count = support["strict_support_count"] + len(mechanics_rows)
    if complete_count != 7904:
        raise AssertionError(("checkpoint primitive count", complete_count))
    if any(not value for _name, value in mechanics_rows):
        raise AssertionError("checkpoint has a zero true-feature primitive")
    digest = hashlib.sha256()
    for name, value in mechanics_rows:
        digest.update(f"{name}|{ex.qs(value)}\n".encode())
    return {
        "coordinate_hash": canonical_hash(
            {
                str(label): [ex.qs(value) for value in points[label]]
                for label in sorted(points)
            }
        ),
        "exact_centroid": [ex.qs(value) for value in centroid],
        "exact_centroid_digest": canonical_hash([ex.qs(value) for value in centroid]),
        "exact_support": {key: value for key, value in support.items() if key != "edges"},
        "exact_mechanics": mechanics,
        "true_edge_count": len(edges),
        "complete_primitive_count": complete_count,
        "point_mechanics_primitive_count": len(mechanics_rows),
        "point_mechanics_digest": digest.hexdigest(),
        "forced_rail_count": len(forced_rails()),
        "missing_forced_rails": [],
        "base_face_present": True,
    }


def circuit_guard(path, support_rows):
    support_lookup = {
        (face_index, witness): polynomial
        for face_index, witness, polynomial in support_rows
    }
    representatives = {}
    for key in CIRCUIT_SUPPORT_ROWS:
        polynomial = support_lookup[key]
        source_sign = 1 if polynomial.eval(Q(0)) > 0 else -1
        oriented = ex.P(tuple(source_sign * value for value in polynomial.c))
        positive = ex.bernstein_sign(oriented, Q(0), STEP, max_depth=60)
        increasing = ex.bernstein_sign(
            oriented.derivative(), Q(0), STEP, max_depth=60
        )
        if positive[0] != 1 or increasing[0] != 1:
            raise AssertionError(("circuit support does not separate", key))
        representatives[f"support:f{key[0]}:w{key[1]}"] = {
            "degree": oriented.degree,
            "polynomial_digest": polynomial_hash(oriented),
            "source_value": ex.qs(oriented.eval(Q(0))),
            "endpoint_value": ex.qs(oriented.eval(STEP)),
            "endpoint_over_source_decimal": float(
                oriented.eval(STEP) / oriented.eval(Q(0))
            ),
            "positive_sign": positive[0],
            "positive_bernstein_leaves": positive[1],
            "derivative_sign": increasing[0],
            "derivative_bernstein_leaves": increasing[1],
        }

    a, b, c, d = CIRCUIT
    raw = ex.det3(ex.sub(path[b], path[a]), ex.sub(path[c], path[a]), ex.sub(path[d], path[a]))
    source_sign = 1 if raw.eval(Q(0)) > 0 else -1
    determinant = ex.P(tuple(source_sign * value for value in raw.c))
    positive = ex.bernstein_sign(determinant, Q(0), STEP, max_depth=60)
    increasing = ex.bernstein_sign(
        determinant.derivative(), Q(0), STEP, max_depth=60
    )
    if positive[0] != 1 or increasing[0] != 1:
        raise AssertionError("oriented target circuit determinant is not strictly increasing")
    return {
        "circuit": list(CIRCUIT),
        "mandatory_rail": [255, 256],
        "claim": "oriented exact circuit determinant is positive and strictly increasing",
        "determinant": {
            "degree": determinant.degree,
            "polynomial_digest": polynomial_hash(determinant),
            "source_value": ex.qs(determinant.eval(Q(0))),
            "endpoint_value": ex.qs(determinant.eval(STEP)),
            "positive_sign": positive[0],
            "positive_bernstein_leaves": positive[1],
            "derivative_sign": increasing[0],
            "derivative_bernstein_leaves": increasing[1],
        },
        "support_representatives": representatives,
    }


def main() -> None:
    global SOURCE, PATH_DEFINITION, ENDPOINT, CERTIFICATE, STEP

    parser = argparse.ArgumentParser()
    parser.add_argument("--source", default=str(SOURCE))
    parser.add_argument("--path-definition", default=str(PATH_DEFINITION))
    parser.add_argument("--endpoint", default=str(ENDPOINT))
    parser.add_argument("--certificate", default=str(CERTIFICATE))
    args = parser.parse_args()

    default_endpoint = provenance.contained_path(
        HERE / "exact_material_step_endpoint.csv",
        base=HERE,
        root=ROOT,
        context="default endpoint",
    )
    default_certificate = provenance.contained_path(
        HERE / "exactification_certificate.json",
        base=HERE,
        root=ROOT,
        context="default certificate",
    )
    SOURCE = provenance.contained_path(
        args.source, base=HERE, root=ROOT, context="builder source"
    )
    PATH_DEFINITION = provenance.contained_path(
        args.path_definition, base=HERE, root=ROOT, context="builder path definition"
    )
    ENDPOINT = provenance.contained_path(
        args.endpoint, base=HERE, root=ROOT, context="builder endpoint"
    )
    CERTIFICATE = provenance.contained_path(
        args.certificate, base=HERE, root=ROOT, context="builder certificate"
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

    definition_snapshot = provenance.read_snapshot(PATH_DEFINITION)
    definition = provenance.parse_json(definition_snapshot)
    provenance.require_header(
        definition,
        schema=provenance.CERTIFIED_PATH_SCHEMA,
        version=provenance.CERTIFIED_PATH_VERSION,
        type_name=provenance.CERTIFIED_PATH_TYPE,
        verdict=provenance.CERTIFIED_PATH_VERDICT,
    )
    provenance.require_trust_packet(
        definition.get("producer_trust"), root=ROOT, role="diagnose"
    )
    parent_path = provenance.stored_path(
        definition.get("parent_first_jet_path_file"),
        root=ROOT,
        context="certified-path parent",
    )
    diagnostic_path = provenance.stored_path(
        definition.get("derivative_horizon_diagnostic_file"),
        root=ROOT,
        context="certified-path diagnostic",
    )
    parent_snapshot = provenance.read_snapshot(parent_path)
    diagnostic_snapshot = provenance.read_snapshot(diagnostic_path)
    parent = provenance.parse_json(parent_snapshot)
    diagnostic = provenance.parse_json(diagnostic_snapshot)

    source_snapshot = provenance.read_snapshot(SOURCE)
    faces_snapshot = provenance.read_snapshot(faces_path)
    rejected_certificate_snapshot = provenance.read_snapshot(rejected_certificate_path)
    rejected_path_snapshot = provenance.read_snapshot(rejected_path)
    trust_snapshots = provenance.trusted_code_snapshots(ROOT, "builder")
    dynamic_source = SOURCE != provenance.contained_path(
        DEFAULT_SOURCE, base=HERE, root=ROOT, context="default source"
    )

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
            raise AssertionError("dynamic-source lineage packet mismatch")

    has_proposal = provenance.require_paired_fields(
        definition, "proposal_sha256", "candidate_sha256"
    )
    has_candidate = has_proposal
    proposal_snapshot = provenance.read_snapshot(proposal_path) if has_proposal else None
    candidate_snapshot = provenance.read_snapshot(candidate_path) if has_candidate else None

    output_paths = [ENDPOINT, CERTIFICATE]
    input_paths = [
        SOURCE,
        PATH_DEFINITION,
        faces_path,
        rejected_certificate_path,
        rejected_path,
        parent_path,
        diagnostic_path,
        *(snapshot.path for snapshot in trust_snapshots),
    ]
    if has_proposal:
        input_paths.extend((proposal_path, candidate_path))
    if lineage_evidence is not None:
        input_paths.extend(snapshot.path for snapshot in lineage_evidence.snapshots)
    protected_defaults = [default_endpoint, default_certificate] if dynamic_source else []
    provenance.assert_isolated(
        [*output_paths, *input_paths, *protected_defaults], "certificate builder"
    )

    all_input_snapshots = [
        source_snapshot,
        definition_snapshot,
        faces_snapshot,
        rejected_certificate_snapshot,
        rejected_path_snapshot,
        parent_snapshot,
        diagnostic_snapshot,
        *trust_snapshots,
    ]
    if proposal_snapshot is not None:
        all_input_snapshots.extend((proposal_snapshot, candidate_snapshot))
    if lineage_evidence is not None:
        all_input_snapshots.extend(lineage_evidence.snapshots)
    provenance.assert_snapshots_current(all_input_snapshots)

    STEP = Q(definition["certified_step_parameter"])
    if STEP <= 0:
        raise ValueError("certified step must be positive")
    source = provenance.parse_exact_csv(source_snapshot)
    faces = provenance.parse_json(faces_snapshot)
    rejected = provenance.parse_json(rejected_certificate_snapshot)
    if definition["source_sha256"] != source_snapshot.sha256:
        raise AssertionError("path/source hash mismatch")
    if definition["faces_sha256"] != faces_snapshot.sha256:
        raise AssertionError("path/faces hash mismatch")
    if has_proposal and definition["proposal_sha256"] != proposal_snapshot.sha256:
        raise AssertionError("path/proposal hash mismatch")
    if has_candidate and definition["candidate_sha256"] != candidate_snapshot.sha256:
        raise AssertionError("path/candidate hash mismatch")
    if definition.get("rejected_event_certificate_sha256") != rejected_certificate_snapshot.sha256:
        raise AssertionError("path/rejected-certificate hash mismatch")
    if definition.get("sparse_path_sha256") != rejected_path_snapshot.sha256:
        raise AssertionError("path/sparse-ray hash mismatch")
    if definition["certified_step_parameter"] != ex.qs(STEP):
        raise AssertionError("step parameter drift")
    if rejected["event"]["circuit"] != list(CIRCUIT):
        raise AssertionError("rejected circuit drift")

    velocity, velocity_packet = exact_velocity(definition, source)
    parent_velocity, _parent_velocity_packet = exact_velocity(parent, source)
    if parent_velocity != velocity:
        raise AssertionError("parent/certified exact velocity mismatch")
    path = {
        label: tuple(ex.P((source[label][axis], velocity[label][axis])) for axis in range(3))
        for label in source
    }
    endpoint = evaluate_path(path, STEP)
    if endpoint == source:
        raise AssertionError("material step is zero")

    print("constructing exact own-centroid polynomial ledger", flush=True)
    ledger = ex.mechanics_primitives(path, faces)
    support_rows = list(ex.support_polynomials(path, faces))
    first_jet = validate_first_jet_parent(
        parent,
        source_snapshot=source_snapshot,
        faces_snapshot=faces_snapshot,
        path=path,
        ledger=ledger,
        support_rows=support_rows,
    )
    semantics = derivative_horizon_semantics(path, ledger, support_rows)
    expected_diagnostic = diagnostic_document(
        parent_path=parent_path,
        parent_snapshot=parent_snapshot,
        source_snapshot=source_snapshot,
        faces_snapshot=faces_snapshot,
        first_jet=first_jet,
        semantics=semantics,
        producer_trust=provenance.expected_trust_packet(ROOT, "diagnose"),
    )
    provenance.require_exact_document(
        diagnostic, expected_diagnostic, "derivative diagnostic complete semantics"
    )
    expected_definition = certified_path_document(
        parent=parent,
        parent_path=parent_path,
        parent_snapshot=parent_snapshot,
        diagnostic_path=diagnostic_path,
        diagnostic_snapshot=diagnostic_snapshot,
        safe_step=Q(semantics["certified_safe_step_parameter"]),
        producer_trust=provenance.expected_trust_packet(ROOT, "diagnose"),
    )
    provenance.require_exact_document(
        definition, expected_definition, "certified-path diagnostic transformation"
    )

    print("auditing all exact support and mechanics primitives", flush=True)
    interval = strict_interval(
        list(primitive_rows(ledger, support_rows)), Q(0), STEP
    )
    checkpoints = {
        "source": checkpoint(source, faces),
        "endpoint": checkpoint(endpoint, faces),
    }
    class_cover = {
        "logic": (
            "The complete interval audit proves every support and own-centroid "
            "classification primitive has constant nonzero sign. Exact endpoint "
            "classification therefore cannot differ anywhere on the segment."
        ),
        "certified_polynomial_count": interval["primitive_count"],
        "complete_interval_primitive_digest": interval["primitive_digest"],
        "source_class": checkpoints["source"]["exact_mechanics"],
        "endpoint_class": checkpoints["endpoint"]["exact_mechanics"],
        "class_constant_on_closed_segment": True,
    }
    if (
        class_cover["source_class"]["class"] != [2, 2, 2]
        or class_cover["endpoint_class"]["class"] != [2, 2, 2]
    ):
        raise AssertionError(class_cover)
    residuals = residual_packet_audit(ledger)
    rail_guard = circuit_guard(path, support_rows)
    endpoint_snapshot = provenance.atomic_write_bytes(
        ENDPOINT, provenance.exact_csv_bytes(endpoint)
    )

    manifest_snapshots = list(all_input_snapshots)
    source_manifest = {
        provenance.relative_name(snapshot.path, ROOT): snapshot.sha256
        for snapshot in manifest_snapshots
    }
    if len(manifest_snapshots) != len({snapshot.path for snapshot in manifest_snapshots}):
        raise AssertionError("duplicate source-manifest path")
    producer_trust = provenance.expected_trust_packet(ROOT, "builder")
    certificate = {
        "schema": provenance.CERTIFICATE_SCHEMA,
        "version": provenance.CERTIFICATE_VERSION,
        "type": provenance.CERTIFICATE_TYPE,
        "verdict": provenance.CERTIFICATE_VERDICT,
        "winner_status": "NONWINNER",
        "scope": (
            "Exact rational-affine segment from the declared exact local-octahedral source "
            f"to rational parameter {ex.qs(STEP)} of the declared exact path."
        ),
        "source": {
            "file": provenance.relative_name(SOURCE, ROOT),
            "sha256": source_snapshot.sha256,
        },
        "source_file_sha256": source_manifest,
        "path": {
            "path_definition_file": provenance.relative_name(PATH_DEFINITION, ROOT),
            "path_definition_sha256": definition_snapshot.sha256,
            "velocity_digest": definition["velocity_digest"],
            "step_parameter": ex.qs(STEP),
            "nonzero": True,
            "exact_base_planarity_preserved": True,
        },
        "complete_interval_audit": interval,
        "own_centroid_class_cover": class_cover,
        "rational_checkpoints": checkpoints,
        "target_residual_packet": residuals,
        "rejected_rail255256_circuit_guard": rail_guard,
        "open_neighborhood": {
            "proved": True,
            "reason": (
                "All 7904 exact support/mechanics primitives are nonzero with "
                "constant sign on the closed segment, including at the rational endpoint."
            ),
        },
        "generated_file_sha256": {
            provenance.relative_name(ENDPOINT, ROOT): endpoint_snapshot.sha256,
        },
        "residual_verdict": {
            "winner": False,
            "endpoint_class": [2, 2, 2],
            "remaining_stable_faces": [sorted(BASE), list(TARGET_FACE)],
            "remaining_unstable_vertices": [1, 8],
            "remaining_saddle_edges": [[4, 5], [12, 13]],
            "declared_path_certified": True,
        },
        "producer_trust": producer_trust,
    }
    provenance.assert_snapshots_current([*all_input_snapshots, endpoint_snapshot])
    certificate_snapshot = provenance.atomic_write_json(CERTIFICATE, certificate)
    provenance.assert_snapshots_current(
        [*all_input_snapshots, endpoint_snapshot, certificate_snapshot]
    )
    print(certificate["verdict"])
    print("primitive_count", interval["primitive_count"])
    print("support_count", interval["family_counts"]["support"])
    print("endpoint_class", checkpoints["endpoint"]["exact_mechanics"]["class"])
    print("missing_rails", checkpoints["endpoint"]["missing_forced_rails"])
    print("certificate_sha256", certificate_snapshot.sha256)


if __name__ == "__main__":
    main()
