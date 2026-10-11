#!/usr/bin/env python3
"""Independent exact verifier for the U6/H(5,6) actual-body bypass.

The verifier does not import the builder.  It reconstructs the rational body
path and anisotropic affine coordinate deformation, recomputes the uniform-
volume centroid from the transformed vertices and face ledger, derives the
local Jacobian through independent univariate exact paths, and re-audits every
support/mechanics primitive and every inherited guard.
"""
from __future__ import annotations

import hashlib
import json
import sys
from fractions import Fraction as Q
from pathlib import Path


HERE = Path(__file__).resolve().parent
FRONT = HERE.parent
ROOT = HERE.parents[4]
EXACT_DIR = ROOT / "tracks/target_sphere_realizer/grouped_local_escape/rigorous_null_bypass"
sys.path.insert(0, str(EXACT_DIR))

import grouped_exact as gx  # noqa: E402


ex = gx.ex
P = ex.P
BASE = frozenset(range(17)) | {54}
STABLE_TRIANGLE = frozenset((7, 8, 245))
FACES_PATH = FRONT / "quad_6_198_244_245_event_far_faces.json"
PRE_PATH = FRONT / "exact_event_chain_pre.csv"
FAR_PATH = FRONT / "exact_event_chain_far.csv"
UPSTREAM_CERTIFICATE = FRONT / "exact_event_chain_certificate.json"
CERTIFICATE = HERE / "certificate.json"
SUMMARY = HERE / "verification.json"
SOURCE_A = HERE / "source_A_t9_4.csv"
BYPASS_B = HERE / "bypass_B_t23_10.csv"
NEXT_PRE = HERE / "next_event_pre.csv"
NEXT_POST = HERE / "next_event_post.csv"

T0 = Q(9, 4)
T1 = Q(23, 10)
DEFORMATION_EPSILON = Q(-1, 100000)
ALT_ROUTE = (228, 198, 263, 9, 8)
TOPOLOGY_QUADS = (
    ("round4_far", (7, 8, 245, 246), -1),
    ("round8_pre", (9, 198, 263, 264), -1),
    ("round10_far", (8, 264, 246, 198), 1),
    ("round12_far", (198, 263, 262, 11), 1),
)
EXPECTED_GUARD_NAMES = [
    "topology:round4_far",
    "topology:round8_pre",
    "topology:round10_far",
    "topology:round12_far",
    "guard:U263_H10_263",
    "guard:U1_H1_54",
    "guard:U6_H5_6",
    "guard:S6_7_245_component_7_245",
    "guard:H7_245_beta1",
    "route_dot:228,198",
    "route_dot:198,263",
    "route_dot:263,9",
    "route_dot:9,8",
]
EXPECTED_CONSTRAINT_NAMES = [
    "U54_via_1",
    "H67_beta1",
    "S7_8_245_via_7_245",
    "H198_263_beta2",
    "topology_round4_far",
    "topology_round8_pre",
    "topology_round10_far",
    "topology_round12_far",
    "U263_via_10",
    "U1_via_54",
]
EXPECTED_SIGNATURE = {
    "class": [2, 2, 2],
    "stable_faces": [sorted(BASE), sorted(STABLE_TRIANGLE)],
    "unstable_vertices": [8, 54],
    "saddle_edges": [[6, 7], [198, 263]],
}


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def canonical_hash(value) -> str:
    return hashlib.sha256(
        json.dumps(value, sort_keys=True, separators=(",", ":")).encode()
    ).hexdigest()


def path_digest(path) -> str:
    return canonical_hash(
        {
            str(label): [coordinate.exact() for coordinate in path[label]]
            for label in sorted(path)
        }
    )


def base_path():
    return gx.planar_morph(ex.read_rows(PRE_PATH), ex.read_rows(FAR_PATH))


def bypass_path(path):
    restricted = {
        label: tuple(coordinate.affine(T0, T1) for coordinate in xyz)
        for label, xyz in path.items()
    }
    u = P((Q(0), Q(1)))
    epsilon = DEFORMATION_EPSILON * u
    return {
        label: (
            (P.one() + epsilon) * xyz[0],
            (P.one() - epsilon) * xyz[1],
            xyz[2],
        )
        for label, xyz in restricted.items()
    }


def fixed_deformed_far_path(path):
    return {
        label: (
            (Q(1) + DEFORMATION_EPSILON) * xyz[0],
            (Q(1) - DEFORMATION_EPSILON) * xyz[1],
            xyz[2],
        )
        for label, xyz in path.items()
    }


def determinant_polynomial(path, quad):
    a, b, c, d = (path[label] for label in quad)
    return ex.det3(ex.sub(b, a), ex.sub(c, a), ex.sub(d, a))


def exact_rref(matrix):
    work = [list(row) for row in matrix]
    rank = 0
    pivots = []
    for column in range(len(work[0])):
        pivot = next(
            (row for row in range(rank, len(work)) if work[row][column]), None
        )
        if pivot is None:
            continue
        work[rank], work[pivot] = work[pivot], work[rank]
        scale = work[rank][column]
        work[rank] = [value / scale for value in work[rank]]
        for row in range(len(work)):
            if row == rank or not work[row][column]:
                continue
            factor = work[row][column]
            work[row] = [
                value - factor * basis
                for value, basis in zip(work[row], work[rank])
            ]
        pivots.append(column)
        rank += 1
        if rank == len(work):
            break
    return rank, pivots, work


def direct_controls(points):
    e1 = ex.sub(points[1], points[0])
    e2 = ex.sub(points[2], points[0])
    controls = []
    names = []
    for vertex in (1, 6, 7, 8, 54):
        for name, direction in (("e1", e1), ("e2", e2)):
            controls.append({vertex: direction})
            names.append(f"v{vertex}:{name}")
    for vertex in (245, 246, 263):
        for axis, name in enumerate("xyz"):
            controls.append(
                {
                    vertex: tuple(
                        Q(1) if coordinate == axis else Q(0)
                        for coordinate in range(3)
                    )
                }
            )
            names.append(f"v{vertex}:{name}")
    if len(controls) != 19:
        raise AssertionError("wrong direct-control dimension")
    return controls, names


def line_path(points, control):
    zero = (Q(0), Q(0), Q(0))
    return {
        label: tuple(
            P((coordinate, control.get(label, zero)[axis]))
            for axis, coordinate in enumerate(points[label])
        )
        for label in points
    }


def constraint_polynomials(path, faces):
    ledger = ex.mechanics_primitives(path, faces)
    stable_face = tuple(sorted(STABLE_TRIANGLE))
    rows = [
        ledger["vertex"][54][1],
        ledger["edge"][(6, 7)]["beta1"],
        ex.signed_face_components(ledger, stable_face)[(7, 245)],
        ledger["edge"][(198, 263)]["beta2"],
        *[
            determinant_polynomial(path, quad)
            for _name, quad, _expected in TOPOLOGY_QUADS
        ],
        ledger["vertex"][263][10],
        ledger["vertex"][1][54],
    ]
    return rows, ledger["vertex"][6][5]


def coefficient_one(polynomial: P) -> Q:
    return polynomial.c[1] if len(polynomial.c) > 1 else Q(0)


def independent_jacobian(points, faces):
    controls, control_names = direct_controls(points)
    columns = []
    target_gradient = []
    values = None
    target_value = None
    for control in controls:
        rows, target = constraint_polynomials(line_path(points, control), faces)
        local_values = [polynomial.eval(Q(0)) for polynomial in rows]
        local_target_value = target.eval(Q(0))
        if values is None:
            values = local_values
            target_value = local_target_value
        elif local_values != values or local_target_value != target_value:
            raise AssertionError("directional paths disagree at their common source")
        columns.append([coefficient_one(polynomial) for polynomial in rows])
        target_gradient.append(coefficient_one(target))
    matrix = [list(row) for row in zip(*columns)]
    rank, pivots, _rref = exact_rref(matrix)
    augmented_rank = exact_rref(matrix + [target_gradient])[0]
    if rank != 10 or augmented_rank != 11:
        raise AssertionError(("wrong independent Jacobian ranks", rank, augmented_rank))
    return {
        "control_names": control_names,
        "direct_subchart_dimension": len(controls),
        "full_chart_dimension": 27,
        "additional_full_chart_control_names": [
            "projective_actual_body_pole_x",
            "projective_actual_body_pole_y",
            "projective_actual_body_pole_z",
            "anisotropic_affine_actual_body_a",
            "anisotropic_affine_actual_body_b",
            "anisotropic_affine_actual_body_c",
            "anisotropic_affine_actual_body_d",
            "anisotropic_affine_actual_body_e",
        ],
        "constraint_names": EXPECTED_CONSTRAINT_NAMES,
        "constraint_values_exact": [ex.qs(value) for value in values],
        "constraint_jacobian_exact": [
            [ex.qs(entry) for entry in row] for row in matrix
        ],
        "target_value_exact": ex.qs(target_value),
        "target_gradient_exact": [ex.qs(entry) for entry in target_gradient],
        "constraint_rank": rank,
        "augmented_rank": augmented_rank,
        "nullity": 19 - rank,
        "full_chart_constraint_rank": rank,
        "full_chart_augmented_rank": augmented_rank,
        "full_chart_nullity": 27 - rank,
        "full_chart_rank_proof": (
            "the exact 10-row direct 19-column submatrix has rank 10 and its "
            "target-augmented 11-row submatrix has rank 11; adjoining the eight "
            "projective/affine actual-body control columns cannot raise either "
            "rank above its row count"
        ),
        "pivot_columns": pivots,
        "matrix_digest": canonical_hash(
            [[ex.qs(entry) for entry in row] for row in matrix]
        ),
    }, matrix, target_gradient


def guard_audit(path, faces, lo: Q, hi: Q, include_u6=True):
    ledger = ex.mechanics_primitives(path, faces)
    records = []

    def prove(name, polynomial, expected):
        records.append(
            {
                "name": name,
                **gx.exact_sign_record(
                    polynomial, lo, hi, expected=expected, max_depth=60
                ),
            }
        )

    for name, quad, expected in TOPOLOGY_QUADS:
        prove(f"topology:{name}", determinant_polynomial(path, quad), expected)
    prove("guard:U263_H10_263", ledger["vertex"][263][10], -1)
    prove("guard:U1_H1_54", ledger["vertex"][1][54], -1)
    if include_u6:
        prove("guard:U6_H5_6", ledger["vertex"][6][5], -1)
    face_component = ex.signed_face_components(
        ledger, tuple(sorted((6, 7, 245)))
    )[(7, 245)]
    prove("guard:S6_7_245_component_7_245", face_component, -1)
    prove("guard:H7_245_beta1", ledger["edge"][(7, 245)]["beta1"], -1)
    for a, b in zip(ALT_ROUTE, ALT_ROUTE[1:]):
        prove(
            f"route_dot:{a},{b}",
            ex.dot(ledger["xscaled"][a], ledger["xscaled"][b]),
            1,
        )
    return {
        "interval": [ex.qs(lo), ex.qs(hi)],
        "record_count": len(records),
        "digest": canonical_hash(records),
        "records": records,
    }


def exact_centroid(points, faces):
    d6, m24 = ex.exact_centroid_numerators(points, faces)
    return tuple(value / (4 * d6) for value in m24)


def assert_exact_csv(path: Path, expected):
    if ex.read_rows(path) != expected:
        raise AssertionError(("exact CSV mismatch", path.name))


def main() -> None:
    certificate = json.loads(CERTIFICATE.read_text())
    if certificate["verdict"] != (
        "EXACT_U6_H56_BOUNDED_AFFINE_BODY_BYPASS_AND_NEXT_EVENT_PASS"
    ):
        raise AssertionError("certificate verdict mismatch")
    if certificate["winner_status"] != "NONWINNER":
        raise AssertionError("literal winner status is not NONWINNER")
    source = certificate["source"]
    provenance = (
        ("upstream_certificate_sha256", UPSTREAM_CERTIFICATE),
        ("pre_sha256", PRE_PATH),
        ("far_sha256", FAR_PATH),
        ("faces_sha256", FACES_PATH),
    )
    for field, path in provenance:
        if source[field] != sha256(path):
            raise AssertionError(("stored input hash mismatch", field, path.name))

    upstream = json.loads(UPSTREAM_CERTIFICATE.read_text())
    upstream_guard_names = [
        record["name"]
        for record in upstream["strict_far_cell_until_next_event"]["guards"][
            "records"
        ]
    ]
    if upstream_guard_names != EXPECTED_GUARD_NAMES:
        raise AssertionError(("upstream guard contract changed", upstream_guard_names))

    faces = json.loads(FACES_PATH.read_text())
    source_path = base_path()
    bypass = bypass_path(source_path)
    continued = fixed_deformed_far_path(source_path)
    if path_digest(source_path) != certificate["source"]["path_polynomial_digest"]:
        raise AssertionError("source path digest mismatch")
    if path_digest(bypass) != certificate["bounded_bypass"]["path_polynomial_digest"]:
        raise AssertionError("bypass path digest mismatch")
    if path_digest(continued) != certificate["strict_far_continuation"][
        "path_polynomial_digest"
    ]:
        raise AssertionError("continued path digest mismatch")

    A = gx.evaluate_path(bypass, Q(0))
    B = gx.evaluate_path(bypass, Q(1))
    A_audit = gx.point_audit(A, faces)
    B_audit = gx.point_audit(B, faces)
    if canonical_hash(A_audit) != canonical_hash(certificate["source"]["A"]):
        raise AssertionError("source-point audit mismatch")
    if canonical_hash(B_audit) != canonical_hash(certificate["bounded_bypass"]["B"]):
        raise AssertionError("bypass endpoint audit mismatch")
    if A_audit["mechanics"] != EXPECTED_SIGNATURE or B_audit[
        "mechanics"
    ] != EXPECTED_SIGNATURE:
        raise AssertionError("endpoint mechanics signature mismatch")
    if A_audit["support"]["f_vector"] != [61, 162, 103] or B_audit[
        "support"
    ]["f_vector"] != [61, 162, 103]:
        raise AssertionError("endpoint support lattice mismatch")

    jacobian, matrix, target_gradient = independent_jacobian(A, faces)
    certified_jacobian = certificate["exact_local_jacobian"]
    for key in (
        "control_names",
        "direct_subchart_dimension",
        "full_chart_dimension",
        "additional_full_chart_control_names",
        "constraint_names",
        "constraint_values_exact",
        "constraint_jacobian_exact",
        "target_value_exact",
        "target_gradient_exact",
        "constraint_rank",
        "augmented_rank",
        "nullity",
        "full_chart_constraint_rank",
        "full_chart_augmented_rank",
        "full_chart_nullity",
        "full_chart_rank_proof",
        "pivot_columns",
        "matrix_digest",
    ):
        if jacobian[key] != certified_jacobian[key]:
            raise AssertionError(("independent Jacobian mismatch", key))
    tangent = [Q(value) for value in certified_jacobian["antibirth_tangent_exact"]]
    annihilation = [
        sum((entry * coefficient for entry, coefficient in zip(row, tangent)), Q(0))
        for row in matrix
    ]
    response = sum(
        (
            entry * coefficient
            for entry, coefficient in zip(target_gradient, tangent)
        ),
        Q(0),
    )
    if any(annihilation) or response >= 0:
        raise AssertionError("stored exact tangent is not an antibirth null tangent")
    if [ex.qs(value) for value in annihilation] != certified_jacobian[
        "constraint_annihilation_exact"
    ]:
        raise AssertionError("stored tangent annihilation packet mismatch")
    if ex.qs(response) != certified_jacobian["target_response_exact"]:
        raise AssertionError("stored tangent response mismatch")

    bypass_every = gx.audit_every_primitive(bypass, faces, max_depth=60)
    if bypass_every != certificate["bounded_bypass"]["all_primitives"]:
        raise AssertionError("bypass primitive ledger mismatch")
    if bypass_every["certified_polynomial_count"] != 7904:
        raise AssertionError("bypass does not certify exactly 7,904 primitives")
    bypass_guards = guard_audit(bypass, faces, Q(0), Q(1))
    if [record["name"] for record in bypass_guards["records"]] != upstream_guard_names:
        raise AssertionError("bypass guard names drift from upstream")
    if bypass_guards != certificate["bounded_bypass"]["guards"]:
        raise AssertionError("bypass guard ledger mismatch")

    determinant = (Q(1) + DEFORMATION_EPSILON) * (
        Q(1) - DEFORMATION_EPSILON
    )
    if determinant <= 0:
        raise AssertionError("fixed actual-body affine deformation is singular")
    base_at_B = gx.evaluate_path(source_path, T1)
    source_centroid = exact_centroid(base_at_B, faces)
    transformed_centroid = exact_centroid(B, faces)
    expected_centroid = (
        (Q(1) + DEFORMATION_EPSILON) * source_centroid[0],
        (Q(1) - DEFORMATION_EPSILON) * source_centroid[1],
        source_centroid[2],
    )
    if transformed_centroid != expected_centroid:
        raise AssertionError("uniform-volume own centroid failed affine covariance")
    for packet_name in ("bounded_bypass", "strict_far_continuation"):
        packet = certificate[packet_name]
        if (
            not packet["uniform_density"]
            or not packet["own_centroid_recomputed_from_transformed_body"]
            or packet["ambient_metric_changed"]
            or packet["artificial_center_used"]
        ):
            raise AssertionError(("body/centroid invariant mismatch", packet_name))

    old_root = upstream["next_mechanics_event"]["root"]
    if not T0 < Q(old_root["lo"]) < Q(old_root["hi"]) < T1:
        raise AssertionError("bypass interval does not cross the old algebraic wall")

    next_event = certificate["next_event"]
    ledger = ex.mechanics_primitives(continued, faces)
    common = ledger["vertex"][6][5]
    if common != ledger["edge"][(5, 6)]["one_minus_t"]:
        raise AssertionError("U6/H(5,6) common numerator identity mismatch")
    root = next_event["root"]
    if common.exact() != root["polynomial_exact"]:
        raise AssertionError("next-event polynomial coefficients mismatch")
    if canonical_hash(common.exact()) != root["polynomial_digest"]:
        raise AssertionError("next-event polynomial digest mismatch")
    verified_root = gx.verify_root_record(common, root)
    next_lo, next_hi = verified_root["lo"], verified_root["hi"]

    continuation_every = gx.audit_every_primitive(
        continued, faces, T1, next_lo, max_depth=60
    )
    if continuation_every != certificate["strict_far_continuation"][
        "all_primitives"
    ]:
        raise AssertionError("strict continuation primitive ledger mismatch")
    if continuation_every["certified_polynomial_count"] != 7904:
        raise AssertionError("continuation does not certify exactly 7,904 primitives")
    continuation_guards = guard_audit(continued, faces, T1, next_lo)
    if [record["name"] for record in continuation_guards["records"]] != upstream_guard_names:
        raise AssertionError("continuation guard names drift from upstream")
    if continuation_guards != certificate["strict_far_continuation"]["guards"]:
        raise AssertionError("strict continuation guard ledger mismatch")

    failed = []
    for name, polynomial, _positive in gx.all_primitives(continued, faces)[1]:
        try:
            ex.bernstein_sign(polynomial, next_lo, next_hi, max_depth=60)
        except AssertionError:
            failed.append(name)
    expected_failed = ["vertex:6:5", "edge:5,6:one_minus_t"]
    if failed != expected_failed or next_event["common_primitives"] != expected_failed:
        raise AssertionError(("wrong next-event primitive family", failed))
    bracket_every = gx.audit_every_primitive(
        continued,
        faces,
        next_lo,
        next_hi,
        skip=frozenset(expected_failed),
        max_depth=60,
    )
    if bracket_every != next_event["all_other_primitives_on_root_bracket"]:
        raise AssertionError("next-event bracket primitive ledger mismatch")
    bracket_guards = guard_audit(
        continued, faces, next_lo, next_hi, include_u6=False
    )
    expected_remaining_names = [
        name for name in upstream_guard_names if name != "guard:U6_H5_6"
    ]
    if [record["name"] for record in bracket_guards["records"]] != expected_remaining_names:
        raise AssertionError("next-event remaining guard names drift from upstream")
    if bracket_guards != next_event["remaining_guards_on_root_bracket"]:
        raise AssertionError("next-event bracket guard ledger mismatch")

    next_pre_points = gx.evaluate_path(continued, next_lo)
    next_post_points = gx.evaluate_path(continued, next_hi)
    next_pre_audit = gx.point_audit(next_pre_points, faces)
    next_post_audit = gx.point_audit(next_post_points, faces)
    if (
        canonical_hash(next_pre_audit) != canonical_hash(next_event["pre"])
        or canonical_hash(next_post_audit) != canonical_hash(next_event["post"])
    ):
        raise AssertionError("next-event endpoint reconstruction mismatch")
    if next_pre_audit["mechanics"] != EXPECTED_SIGNATURE:
        raise AssertionError("next-event strict pre signature mismatch")
    if next_post_audit["mechanics"]["class"] != [2, 3, 3]:
        raise AssertionError("next-event post class mismatch")
    if next_pre_audit["support"]["f_vector"] != [61, 162, 103] or next_post_audit[
        "support"
    ]["f_vector"] != [61, 162, 103]:
        raise AssertionError("next-event support lattice mismatch")

    assert_exact_csv(SOURCE_A, A)
    assert_exact_csv(BYPASS_B, B)
    assert_exact_csv(NEXT_PRE, next_pre_points)
    assert_exact_csv(NEXT_POST, next_post_points)
    for artifact, expected_hash in certificate["artifact_hashes"].items():
        path = ROOT / artifact
        if sha256(path) != expected_hash:
            raise AssertionError(("artifact hash mismatch", artifact))

    summary = {
        "version": 1,
        "verdict": "INDEPENDENT_EXACT_U6_H56_AFFINE_BODY_BYPASS_PASS",
        "winner_status": "NONWINNER",
        "certificate_sha256": sha256(CERTIFICATE),
        "builder_sha256": sha256(HERE / "build_certificate.py"),
        "verifier_sha256": sha256(HERE / "verify_certificate.py"),
        "upstream_certificate_sha256": sha256(UPSTREAM_CERTIFICATE),
        "guard_contract_names": upstream_guard_names,
        "jacobian": {
            "derivation": "19 independent exact univariate directional paths",
            "constraint_names": EXPECTED_CONSTRAINT_NAMES,
            "rank": jacobian["constraint_rank"],
            "augmented_rank": jacobian["augmented_rank"],
            "nullity": jacobian["nullity"],
            "antibirth_response_sign": -1,
            "full_27d_chart": {
                "rank": certified_jacobian["full_chart_constraint_rank"],
                "augmented_rank": certified_jacobian[
                    "full_chart_augmented_rank"
                ],
                "nullity": certified_jacobian["full_chart_nullity"],
                "proof": certified_jacobian["full_chart_rank_proof"],
            },
        },
        "actual_body_affine_deformation": {
            "applied_to_every_vertex": True,
            "uniform_density": True,
            "own_volume_centroid_recomputed": True,
            "centroid_affine_covariance_exact": True,
            "ambient_metric_changed": False,
            "artificial_center_used": False,
        },
        "primitive_counts": {
            "bypass": bypass_every["certified_polynomial_count"],
            "strict_continuation": continuation_every[
                "certified_polynomial_count"
            ],
            "next_root_bracket_other": bracket_every[
                "certified_polynomial_count"
            ],
        },
        "next_event": {
            "interval": [ex.qs(next_lo), ex.qs(next_hi)],
            "degree": common.degree,
            "common_primitives": expected_failed,
            "class_transition": [[2, 2, 2], [2, 3, 3]],
            "support": [61, 162, 103],
        },
    }
    SUMMARY.write_text(json.dumps(summary, indent=2) + "\n")
    print(summary["verdict"])
    print("winner_status", summary["winner_status"])
    print("jacobian_ranks", jacobian["constraint_rank"], jacobian["augmented_rank"])
    print("bypass_primitive_count", bypass_every["certified_polynomial_count"])
    print("continuation_primitive_count", continuation_every["certified_polynomial_count"])
    print("next_root", summary["next_event"]["interval"])
    print("certificate_sha256", summary["certificate_sha256"])


if __name__ == "__main__":
    main()
