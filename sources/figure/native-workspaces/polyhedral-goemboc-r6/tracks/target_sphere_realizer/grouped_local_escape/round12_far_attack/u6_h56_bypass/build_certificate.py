#!/usr/bin/env python3
"""Build the exact U6/H(5,6) bounded bypass certificate."""
from __future__ import annotations

import csv
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
SOURCE_A = HERE / "source_A_t9_4.csv"
BYPASS_B = HERE / "bypass_B_t23_10.csv"
NEXT_PRE = HERE / "next_event_pre.csv"
NEXT_POST = HERE / "next_event_post.csv"

T0 = Q(9, 4)
T1 = Q(23, 10)
DEFORMATION_EPSILON = Q(-1, 100000)
NEXT_SEARCH = (Q(128), Q(192))
ROOT_WIDTH = Q(1, 10**24)
ALT_ROUTE = (228, 198, 263, 9, 8)
TOPOLOGY_QUADS = (
    ("round4_far", (7, 8, 245, 246), -1),
    ("round8_pre", (9, 198, 263, 264), -1),
    ("round10_far", (8, 264, 246, 198), 1),
    ("round12_far", (198, 263, 262, 11), 1),
)
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


def local(path: Path) -> str:
    return str(path.resolve().relative_to(ROOT))


def write_rows(path: Path, rows) -> None:
    with path.open("w", newline="") as handle:
        writer = csv.writer(handle)
        writer.writerow(("source_id", "x", "y", "z"))
        for label in sorted(rows):
            writer.writerow((label, *(ex.qs(value) for value in rows[label])))


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
    local_base = {
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
        for label, xyz in local_base.items()
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


def exact_rank(matrix):
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


def nullspace_basis(matrix):
    rank, pivots, rref = exact_rank(matrix)
    free = [column for column in range(len(matrix[0])) if column not in pivots]
    basis = []
    for column in free:
        vector = [Q(0)] * len(matrix[0])
        vector[column] = Q(1)
        for row, pivot in enumerate(pivots):
            vector[pivot] = -rref[row][column]
        basis.append(vector)
    return rank, pivots, basis


def local_jacobian(A, faces):
    e1 = ex.sub(A[1], A[0])
    e2 = ex.sub(A[2], A[0])
    controls = []
    names = []
    for vertex in (1, 6, 7, 8, 54):
        for name, direction in (("e1", e1), ("e2", e2)):
            controls.append({vertex: direction})
            names.append(f"v{vertex}:{name}")
    for vertex in (245, 246, 263):
        for axis, name in enumerate("xyz"):
            direction = tuple(Q(1) if index == axis else Q(0) for index in range(3))
            controls.append({vertex: direction})
            names.append(f"v{vertex}:{name}")
    if len(controls) != 19:
        raise AssertionError("wrong local control count")

    zero_velocity = {label: (Q(0), Q(0), Q(0)) for label in A}
    points = ex.jp_points(A, zero_velocity, controls, list(range(19)))
    dimension = len(controls)
    zero = ex.JP(P.zero(), (P.zero(),) * dimension)
    d6 = zero
    m24 = [zero, zero, zero]
    for cycle in faces:
        for index in range(1, len(cycle) - 1):
            a, b, c = points[cycle[0]], points[cycle[index]], points[cycle[index + 1]]
            volume = ex.det3(a, b, c)
            d6 += volume
            for axis in range(3):
                m24[axis] += volume * (a[axis] + b[axis] + c[axis])
    scale = 4 * d6
    xscaled = {
        label: tuple(scale * points[label][axis] - m24[axis] for axis in range(3))
        for label in points
    }
    incidence, _neighbors, face_by_key = ex.edge_data(faces)

    def vertex_raw(vertex, neighbor):
        return -ex.dot(xscaled[vertex], ex.sub(points[neighbor], points[vertex]))

    def edge_raw(edge, component):
        i, j = tuple(sorted(edge))
        direction = ex.sub(points[j], points[i])
        t_value = -ex.dot(xscaled[i], direction)
        if component == "t":
            return t_value
        if component == "one_minus_t":
            return scale * ex.norm2(direction) - t_value
        incident = incidence[(i, j)]
        normal1 = ex.cycle_normal(faces[incident[0]], points)
        normal2 = ex.cycle_normal(faces[incident[1]], points)
        aa = ex.norm2(normal1)
        ab = ex.dot(normal1, normal2)
        cc = ex.norm2(normal2)
        r1 = ex.dot(xscaled[i], normal1)
        r2 = ex.dot(xscaled[i], normal2)
        if component == "beta1":
            return r1 * cc - r2 * ab
        if component == "beta2":
            return r2 * aa - r1 * ab
        raise AssertionError(component)

    def face_raw(face_key, directed_edge):
        face_index = face_by_key[tuple(sorted(face_key))]
        normal = ex.cycle_normal(faces[face_index], points)
        a, b = directed_edge
        edge = ex.sub(points[b], points[a])
        normal_norm2 = ex.norm2(normal)
        height = ex.dot(normal, xscaled[a])
        return ex.dot(
            ex.cross(
                edge,
                ex.sub(ex.mul(normal, height), ex.mul(xscaled[a], normal_norm2)),
            ),
            normal,
        )

    def topology(quad):
        a, b, c, d = (points[label] for label in quad)
        return ex.det3(ex.sub(b, a), ex.sub(c, a), ex.sub(d, a))

    point_ledger = ex.mechanics_primitives(A, faces)
    face_key = (7, 8, 245)
    edge = (7, 245)
    face_cycle = faces[point_ledger["face_by_key"][face_key]]
    directed_edge = next(
        (a, b)
        for a, b in zip(face_cycle, face_cycle[1:] + face_cycle[:1])
        if tuple(sorted((a, b))) == edge
    )
    raw_at_A = point_ledger["face"][face_key][edge]
    signed_at_A = ex.signed_face_components(point_ledger, face_key)[edge]
    orientation = Q(1) if raw_at_A == signed_at_A else Q(-1)

    rows = [
        ("U54_via_1", vertex_raw(54, 1)),
        ("H67_beta1", edge_raw((6, 7), "beta1")),
        (
            "S7_8_245_via_7_245",
            orientation * face_raw(face_key, directed_edge),
        ),
        ("H198_263_beta2", edge_raw((198, 263), "beta2")),
        *[(f"topology_{name}", topology(quad)) for name, quad, _sign in TOPOLOGY_QUADS],
        ("U263_via_10", vertex_raw(263, 10)),
        ("U1_via_54", vertex_raw(1, 54)),
    ]
    target = ("U6_H56_common", vertex_raw(6, 5))

    def value(item):
        return item.v.eval(Q(0))

    def gradient(item):
        return [derivative.eval(Q(0)) for derivative in item.d]

    matrix = [gradient(item) for _name, item in rows]
    target_gradient = gradient(target[1])
    rank, pivots, basis = nullspace_basis(matrix)
    augmented_rank = exact_rank(matrix + [target_gradient])[0]
    if rank != 10 or augmented_rank != 11:
        raise AssertionError(("unexpected exact local ranks", rank, augmented_rank))
    candidates = []
    for vector in basis:
        response = sum((a * b for a, b in zip(target_gradient, vector)), Q(0))
        if response:
            if response > 0:
                vector = [-entry for entry in vector]
                response = -response
            scale_value = max(abs(entry) for entry in vector)
            vector = [entry / scale_value for entry in vector]
            response /= scale_value
            candidates.append((abs(float(response)), response, vector))
    if not candidates:
        raise AssertionError("target gradient vanishes on exact nullspace")
    _score, response, tangent = max(candidates, key=lambda item: item[0])
    annihilation = [
        sum((a * b for a, b in zip(row, tangent)), Q(0)) for row in matrix
    ]
    if any(annihilation) or not response < 0:
        raise AssertionError("invalid exact antibirth nullspace tangent")
    return {
        "control_names": names,
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
        "constraint_names": [name for name, _item in rows],
        "constraint_values_exact": [ex.qs(value(item)) for _name, item in rows],
        "constraint_jacobian_exact": [
            [ex.qs(entry) for entry in row] for row in matrix
        ],
        "target_value_exact": ex.qs(value(target[1])),
        "target_gradient_exact": [ex.qs(entry) for entry in target_gradient],
        "constraint_rank": rank,
        "augmented_rank": augmented_rank,
        "nullity": len(controls) - rank,
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
        "antibirth_tangent_exact": [ex.qs(entry) for entry in tangent],
        "constraint_annihilation_exact": [ex.qs(entry) for entry in annihilation],
        "target_response_exact": ex.qs(response),
        "target_response_sign": -1,
        "matrix_digest": canonical_hash(
            [[ex.qs(entry) for entry in row] for row in matrix]
        ),
    }


def guard_audit(path, faces, lo: Q, hi: Q, include_u6=True):
    ledger = ex.mechanics_primitives(path, faces)
    records = []

    def prove(name, polynomial, expected):
        packet = gx.exact_sign_record(
            polynomial, lo, hi, expected=expected, max_depth=60
        )
        records.append({"name": name, **packet})

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


def exact_point_record(points, faces):
    audit = gx.point_audit(points, faces)
    if audit["support"]["f_vector"] != [61, 162, 103]:
        raise AssertionError("wrong exact point support")
    return audit


def root_record(polynomial, lo: Q, hi: Q):
    record = gx.root_record(polynomial, lo, hi, ROOT_WIDTH)
    return {
        **record,
        "polynomial_degree": polynomial.degree,
        "polynomial_exact": polynomial.exact(),
        "polynomial_digest": canonical_hash(polynomial.exact()),
    }


def main() -> None:
    faces = json.loads(FACES_PATH.read_text())
    source_path = base_path()
    bypass = bypass_path(source_path)
    continued = fixed_deformed_far_path(source_path)

    A = gx.evaluate_path(bypass, Q(0))
    B = gx.evaluate_path(bypass, Q(1))
    A_audit = exact_point_record(A, faces)
    B_audit = exact_point_record(B, faces)
    if A_audit["mechanics"] != EXPECTED_SIGNATURE:
        raise AssertionError(("wrong A signature", A_audit["mechanics"]))
    if B_audit["mechanics"] != EXPECTED_SIGNATURE:
        raise AssertionError(("wrong B signature", B_audit["mechanics"]))

    jacobian = local_jacobian(A, faces)
    bypass_every = gx.audit_every_primitive(bypass, faces, max_depth=60)
    bypass_guards = guard_audit(bypass, faces, Q(0), Q(1))

    continued_ledger = ex.mechanics_primitives(continued, faces)
    common = continued_ledger["vertex"][6][5]
    if common != continued_ledger["edge"][(5, 6)]["one_minus_t"]:
        raise AssertionError("U6/H(5,6) common numerator identity failed")
    next_root = root_record(common, *NEXT_SEARCH)
    next_lo, next_hi = Q(next_root["lo"]), Q(next_root["hi"])
    continuation_every = gx.audit_every_primitive(
        continued, faces, T1, next_lo, max_depth=60
    )
    continuation_guards = guard_audit(continued, faces, T1, next_lo)

    failed = []
    for name, polynomial, _positive in gx.all_primitives(continued, faces)[1]:
        try:
            ex.bernstein_sign(polynomial, next_lo, next_hi, max_depth=60)
        except AssertionError:
            failed.append(name)
    expected_failed = ["vertex:6:5", "edge:5,6:one_minus_t"]
    if failed != expected_failed:
        raise AssertionError(("unexpected next-event family", failed))
    bracket_every = gx.audit_every_primitive(
        continued,
        faces,
        next_lo,
        next_hi,
        skip=frozenset(failed),
        max_depth=60,
    )
    bracket_guards = guard_audit(
        continued, faces, next_lo, next_hi, include_u6=False
    )
    next_pre_points = gx.evaluate_path(continued, next_lo)
    next_post_points = gx.evaluate_path(continued, next_hi)
    next_pre_audit = exact_point_record(next_pre_points, faces)
    next_post_audit = exact_point_record(next_post_points, faces)
    if next_pre_audit["mechanics"] != EXPECTED_SIGNATURE:
        raise AssertionError("wrong next-event pre signature")
    if next_post_audit["mechanics"]["class"] != [2, 3, 3]:
        raise AssertionError("wrong next-event post class")
    if next_post_audit["mechanics"]["unstable_vertices"] != [6, 8, 54]:
        raise AssertionError("U6 did not appear at the next event")
    if next_post_audit["mechanics"]["saddle_edges"] != [
        [5, 6], [6, 7], [198, 263]
    ]:
        raise AssertionError("H(5,6) did not appear at the next event")

    write_rows(SOURCE_A, A)
    write_rows(BYPASS_B, B)
    write_rows(NEXT_PRE, next_pre_points)
    write_rows(NEXT_POST, next_post_points)
    artifacts = (SOURCE_A, BYPASS_B, NEXT_PRE, NEXT_POST)

    out = {
        "version": 1,
        "verdict": "EXACT_U6_H56_BOUNDED_AFFINE_BODY_BYPASS_AND_NEXT_EVENT_PASS",
        "winner_status": "NONWINNER",
        "source": {
            "upstream_certificate": local(UPSTREAM_CERTIFICATE),
            "upstream_certificate_sha256": sha256(UPSTREAM_CERTIFICATE),
            "pre_path": local(PRE_PATH),
            "pre_sha256": sha256(PRE_PATH),
            "far_path": local(FAR_PATH),
            "far_sha256": sha256(FAR_PATH),
            "faces_path": local(FACES_PATH),
            "faces_sha256": sha256(FACES_PATH),
            "path_polynomial_digest": path_digest(source_path),
            "A_parameter_exact": ex.qs(T0),
            "A": A_audit,
        },
        "exact_local_jacobian": jacobian,
        "bounded_bypass": {
            "parameter": "u in [0,1]",
            "base_parameter": f"t={ex.qs(T0)}+({ex.qs(T1 - T0)})u",
            "actual_body_coordinate_deformation": (
                "apply diag(1-u/100000,1+u/100000,1) to every vertex "
                "in fixed Euclidean coordinates"
            ),
            "affine_deformation_determinant": "1-u^2/10000000000",
            "uniform_density": True,
            "own_centroid_recomputed_from_transformed_body": True,
            "ambient_metric_changed": False,
            "artificial_center_used": False,
            "path_polynomial_digest": path_digest(bypass),
            "all_primitives": bypass_every,
            "guards": bypass_guards,
            "A_signature": A_audit["mechanics"],
            "B_signature": B_audit["mechanics"],
            "crosses_old_wall_parameter": True,
            "old_wall_parameter_decimal": 2.291066601001303,
            "B_parameter_exact": ex.qs(T1),
            "B": B_audit,
        },
        "strict_far_continuation": {
            "actual_body_coordinate_deformation": (
                "apply diag(99999/100000,100001/100000,1) to every vertex "
                "in fixed Euclidean coordinates"
            ),
            "uniform_density": True,
            "own_centroid_recomputed_from_transformed_body": True,
            "ambient_metric_changed": False,
            "artificial_center_used": False,
            "interval": [ex.qs(T1), next_root["lo"]],
            "path_polynomial_digest": path_digest(continued),
            "all_primitives": continuation_every,
            "guards": continuation_guards,
            "signature": EXPECTED_SIGNATURE,
        },
        "next_event": {
            "type": (
                "simultaneous U6 and H(5,6) birth on the far ray after a fixed "
                "actual-body anisotropic affine deformation"
            ),
            "common_primitives": expected_failed,
            "common_polynomial_identity": True,
            "root": next_root,
            "all_other_primitives_on_root_bracket": bracket_every,
            "remaining_guards_on_root_bracket": bracket_guards,
            "pre": next_pre_audit,
            "post": next_post_audit,
            "class_transition": [[2, 2, 2], [2, 3, 3]],
            "support_transition": [[61, 162, 103], [61, 162, 103]],
        },
        "artifact_hashes": {local(path): sha256(path) for path in artifacts},
        "conclusion": (
            "The old degree-nine U6/H(5,6) wall is not an obstruction: an exact "
            "rank-10/nullity-9 direct-geometry Jacobian has independent target "
            "response, and a bounded rational actual-body anisotropic affine "
            "deformation crosses its old parameter "
            "while every one of 7,904 primitives and all accumulated guards remain "
            "strict.  The fixed affinely deformed far ray stays in the same exact "
            "(2,2,2) cell "
            "until a new common U6/H(5,6) root near t=150.1038672836875.  This is "
            "material progress but not a (1,1,0) winner."
        ),
    }
    CERTIFICATE.write_text(json.dumps(out, indent=2) + "\n")
    print(out["verdict"])
    print("winner_status", out["winner_status"])
    print("jacobian_ranks", jacobian["constraint_rank"], jacobian["augmented_rank"])
    print("bypass_primitive_count", bypass_every["certified_polynomial_count"])
    print("next_root", next_root["decimal_interval"])
    print("next_class", next_post_audit["mechanics"]["class"])
    print("certificate_sha256", sha256(CERTIFICATE))


if __name__ == "__main__":
    main()
