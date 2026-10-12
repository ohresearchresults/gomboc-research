#!/usr/bin/env python3
"""Build the exact first-event certificate for the active sparse residual ray.

The search artifacts in this directory are treated only as provenance.  This
builder reconstructs the exact far checkpoint, freezes an explicit rational
line, derives its first wall exactly, and audits every support/incidence/
mechanics primitive on the two closed adjacent intervals.  The resulting
verdict is deliberately scoped to this one ray: it is a rail obstruction, not
an obstruction to the full 165-dimensional residual cone.
"""
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
PARENT = HERE.parent
ROOT = HERE.parents[3]
EXACT_HELPERS = (
    ROOT / "tracks/target_sphere_realizer/grouped_local_escape/rigorous_null_bypass"
)
sys.path[:0] = [str(HERE), str(EXACT_HELPERS)]

import attack_common as c  # noqa: E402
import grouped_exact as gx  # noqa: E402


ex = c.frozen.ex
RAY = HERE / "active_sparse_ray.json"
NUMERIC_SCAN = HERE / "active_sparse_scan.json"
UPSTREAM_CERTIFICATE = PARENT / "certificate.json"
UPSTREAM_FACES = PARENT / "far_faces.json"

PATH_DEFINITION = HERE / "exact_event_path.json"
CERTIFICATE = HERE / "exact_event_certificate.json"
MANIFEST = HERE / "exact_event_manifest.sha256"

POINT_FILES = {
    "source": HERE / "exact_event_source.csv",
    "pre": HERE / "exact_event_pre.csv",
    "wall": HERE / "exact_event_wall.csv",
    "post": HERE / "exact_event_post.csv",
}
FACE_FILES = {
    "source": HERE / "exact_event_source_faces.json",
    "pre": HERE / "exact_event_pre_faces.json",
    "wall": HERE / "exact_event_wall_faces.json",
    "post": HERE / "exact_event_post_faces.json",
}

BASE = frozenset(range(17)) | {54}
EVENT_CIRCUIT = frozenset((69, 224, 255, 256))
PRE_DIAGONAL = (255, 256)
POST_DIAGONAL = (69, 224)
EXPECTED_F_VECTOR = {
    "source": [61, 162, 103],
    "pre": [61, 162, 103],
    "wall": [61, 161, 102],
    "post": [61, 162, 103],
}
EXPECTED_CLASS = [2, 2, 2]
EXPECTED_ZERO_FAMILIES = {
    "pre": {
        "support:f57:w69",
        "support:f58:w224",
        "edge_gram:255,256",
        "edge:255,256:beta1",
        "edge:255,256:beta2",
    },
    "post": {
        "support:f65:w255",
        "support:f74:w256",
        "edge_gram:69,224",
        "edge:69,224:beta1",
        "edge:69,224:beta2",
    },
}
ACTIVE_COMPONENTS = {
    "S[198,243,245]": ("face", (198, 243)),
    "U1": ("vertex", 2),
    "H(4,5)": ("edge45", "one_minus_t"),
    "H(12,13)": ("edge1213", "one_minus_t"),
}


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def canonical_hash(value) -> str:
    return hashlib.sha256(
        json.dumps(value, sort_keys=True, separators=(",", ":")).encode()
    ).hexdigest()


def polynomial_hash(poly) -> str:
    return canonical_hash(poly.exact())


def point_hash(points) -> str:
    return canonical_hash(
        {str(i): [ex.qs(z) for z in points[i]] for i in sorted(points)}
    )


def face_hash(faces) -> str:
    return canonical_hash(sorted(sorted(int(i) for i in face) for face in faces))


def write_exact_csv(path: Path, points) -> None:
    with path.open("w", newline="") as stream:
        out = csv.writer(stream)
        out.writerow(("source_id", "x", "y", "z"))
        for label in sorted(points):
            out.writerow((label, *(ex.qs(z) for z in points[label])))


def write_faces(path: Path, faces) -> None:
    path.write_text(json.dumps(faces, indent=2) + "\n")


def forced_rails() -> set[tuple[int, int]]:
    return set(c.rail_edges())


def fresh_exact_faces(points):
    faces, _numeric = c.frozen.qhull_faces(points, coplanar_rel=2e-12)
    ex.supporting_cell(points, faces)
    return faces


def divide_linear_root(poly, root: Q):
    """Divide exactly by (t-root), returning quotient and remainder."""
    poly = ex.P.coerce(poly)
    if poly.degree < 1:
        return ex.P.zero(), poly.c[0]
    quotient = [Q(0)] * poly.degree
    quotient[-1] = poly.c[-1]
    for k in range(poly.degree - 1, 0, -1):
        quotient[k - 1] = poly.c[k] + root * quotient[k]
    remainder = poly.c[0] + root * quotient[0]
    return ex.P(tuple(quotient)), remainder


def root_factorization(poly, root: Q):
    quotient = ex.P.coerce(poly)
    order = 0
    while quotient.degree > 0:
        candidate, remainder = divide_linear_root(quotient, root)
        if remainder:
            break
        quotient = candidate
        order += 1
    if not order or not quotient.eval(root):
        raise AssertionError(("bad exact event factorization", poly.degree, order))
    return order, quotient


def all_primitive_records(path, faces):
    _ledger, records = gx.all_primitives(path, faces)
    return records


def event_aware_interval_audit(
    path,
    faces,
    lo: Q,
    hi: Q,
    root: Q,
    expected_zero_names: set[str],
):
    """Prove every primitive sign, factoring the endpoint event family."""
    strict_rows = []
    zero_rows = []
    middle = (lo + hi) / 2
    for name, poly, intrinsically_positive in all_primitive_records(path, faces):
        value_at_root = poly.eval(root)
        if not value_at_root:
            order, quotient = root_factorization(poly, root)
            sign, leaves, worst = ex.bernstein_sign(
                quotient, lo, hi, max_depth=60
            )
            left_value = poly.eval((lo + root) / 2) if lo < root else None
            right_value = poly.eval((root + hi) / 2) if root < hi else None
            zero_rows.append(
                {
                    "name": name,
                    "degree": poly.degree,
                    "root_order": order,
                    "quotient_sign": sign,
                    "quotient_bernstein_leaves": leaves,
                    "quotient_min_bernstein_log10_abs": worst,
                    "left_sign": (
                        None if left_value is None else (1 if left_value > 0 else -1)
                    ),
                    "right_sign": (
                        None if right_value is None else (1 if right_value > 0 else -1)
                    ),
                    "polynomial_digest": polynomial_hash(poly),
                    "quotient_digest": polynomial_hash(quotient),
                }
            )
            continue
        expected = 1 if poly.eval(middle) > 0 else -1
        sign, leaves, worst = ex.bernstein_sign(poly, lo, hi, max_depth=60)
        if sign != expected:
            raise AssertionError(("primitive sign mismatch", name, sign, expected))
        if intrinsically_positive and sign != 1:
            raise AssertionError(("nonpositive intrinsic primitive", name))
        strict_rows.append((name, sign, leaves, worst, poly))

    got_zero_names = {row["name"] for row in zero_rows}
    if got_zero_names != expected_zero_names:
        raise AssertionError(
            ("wrong event family", sorted(got_zero_names), sorted(expected_zero_names))
        )
    digest = hashlib.sha256()
    for name, sign, _leaves, _worst, poly in strict_rows:
        digest.update(f"{name}|{sign}|{'|'.join(poly.exact())}\n".encode())
    return {
        "interval": [ex.qs(lo), ex.qs(hi)],
        "complete_primitive_count": len(strict_rows) + len(zero_rows),
        "strict_non_event_primitive_count": len(strict_rows),
        "strict_non_event_bernstein_leaves": sum(row[2] for row in strict_rows),
        "strict_non_event_min_bernstein_log10_abs": min(
            row[3] for row in strict_rows
        ),
        "strict_non_event_digest": digest.hexdigest(),
        "event_family": sorted(zero_rows, key=lambda row: row["name"]),
    }


def residual_polynomials(path, faces):
    ledger = ex.mechanics_primitives(path, faces)
    face_key = tuple(sorted(c.TARGET_FACE))
    face = ex.signed_face_components(ledger, face_key)
    vertex = ledger["vertex"][c.TARGET_VERTEX]
    return {
        **{
            f"S[198,243,245]:edge({edge[0]},{edge[1]})": poly
            for edge, poly in sorted(face.items())
        },
        **{f"U1:neighbor({neighbor})": poly for neighbor, poly in sorted(vertex.items())},
        **{
            f"H(4,5):{name}": ledger["edge"][(4, 5)][name]
            for name in c.EDGE_COMPONENT_NAMES
        },
        **{
            f"H(12,13):{name}": ledger["edge"][(12, 13)][name]
            for name in c.EDGE_COMPONENT_NAMES
        },
    }


def residual_packet_audit(path, faces, root: Q):
    polynomials = residual_polynomials(path, faces)
    active_names = {
        "S[198,243,245]:edge(198,243)",
        "U1:neighbor(2)",
        "H(4,5):one_minus_t",
        "H(12,13):one_minus_t",
    }
    records = {}
    for name, poly in sorted(polynomials.items()):
        sign, leaves, worst = ex.bernstein_sign(poly, Q(0), root, max_depth=60)
        if sign != 1:
            raise AssertionError(("residual component lost positivity", name, sign))
        source_value = poly.eval(Q(0))
        wall_value = poly.eval(root)
        delta = wall_value - source_value
        record = {
            "degree": poly.degree,
            "polynomial_digest": polynomial_hash(poly),
            "positive_bernstein_leaves": leaves,
            "positive_min_bernstein_log10_abs": worst,
            "source_log10_abs": ex.qlog10(source_value),
            "wall_log10_abs": ex.qlog10(wall_value),
            "wall_over_source_decimal": float(wall_value / source_value),
            "delta_sign": 0 if not delta else (1 if delta > 0 else -1),
            "delta_digest": canonical_hash(ex.qs(delta)),
            "active": name in active_names,
        }
        if name in active_names:
            derivative_sign, derivative_leaves, derivative_worst = ex.bernstein_sign(
                poly.derivative(), Q(0), root, max_depth=60
            )
            if derivative_sign != -1 or delta >= 0:
                raise AssertionError(("active component is not directed down", name))
            record.update(
                {
                    "derivative_sign": derivative_sign,
                    "derivative_bernstein_leaves": derivative_leaves,
                    "derivative_min_bernstein_log10_abs": derivative_worst,
                    "relative_decrease_decimal": float(
                        (source_value - wall_value) / source_value
                    ),
                }
            )
        records[name] = record
    if {name for name, row in records.items() if row["active"]} != active_names:
        raise AssertionError("active residual family mismatch")
    return {
        "component_count": len(records),
        "active_component_count": len(active_names),
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
        for name in (
            "direction_norm2",
            "gram",
            "t",
            "one_minus_t",
            "beta1",
            "beta2",
        ):
            yield f"edge:{edge}:{name}", values[name]


def checkpoint(name, points, faces):
    support = ex.supporting_cell(points, faces)
    ledger, mechanics = ex.classify_point(points, faces)
    if support["f_vector"] != EXPECTED_F_VECTOR[name]:
        raise AssertionError((name, support["f_vector"]))
    if mechanics["class"] != EXPECTED_CLASS:
        raise AssertionError((name, mechanics))
    if support["active_labels"] != sorted(points):
        raise AssertionError((name, "inactive input row"))
    if BASE not in {frozenset(face) for face in faces}:
        raise AssertionError((name, "missing enlarged base"))
    edges = set(map(tuple, support["edges"]))
    missing = sorted(forced_rails() - edges)
    d6, m24 = ex.exact_centroid_numerators(points, faces)
    if d6 <= 0:
        raise AssertionError((name, "nonpositive volume"))
    centroid = tuple(value / (4 * d6) for value in m24)
    primitive_rows = list(point_mechanics_rows(ledger))
    if any(not value for _label, value in primitive_rows):
        raise AssertionError((name, "zero true-feature mechanics primitive"))
    digest = hashlib.sha256()
    for label, value in primitive_rows:
        digest.update(f"{label}|{ex.qs(value)}\n".encode())
    return {
        "coordinate_hash": point_hash(points),
        "face_hash": face_hash(faces),
        "exact_support": {key: value for key, value in support.items() if key != "edges"},
        "true_edge_count": len(edges),
        "true_edge_digest": canonical_hash(sorted(map(list, edges))),
        "exact_mechanics": mechanics,
        "mechanics_primitive_count": len(primitive_rows),
        "mechanics_min_nonzero_log10_abs": min(
            ex.qlog10(value) for _label, value in primitive_rows
        ),
        "mechanics_digest": digest.hexdigest(),
        "exact_centroid": [ex.qs(value) for value in centroid],
        "exact_centroid_digest": canonical_hash([ex.qs(value) for value in centroid]),
        "base_face_present": True,
        "forced_rail_count": len(forced_rails()),
        "missing_forced_rails": [list(edge) for edge in missing],
    }


def face_key_set(faces):
    return {frozenset(face) for face in faces}


def edge_set(faces):
    return set(ex.edge_data(faces)[0])


def manifest_text(paths) -> str:
    return "".join(f"{sha256(path)}  {path.name}\n" for path in paths)


def main() -> None:
    ray = json.loads(RAY.read_text())
    numeric_scan = json.loads(NUMERIC_SCAN.read_text())
    upstream = json.loads(UPSTREAM_CERTIFICATE.read_text())
    if upstream["verdict"] != "STRICT_ACTUAL_MULTI_CELL_PASSAGE_WITH_ALL37_RAILS":
        raise AssertionError("unexpected upstream certificate verdict")

    source, source_faces, source_reconstruction = c.reconstruct_exact_far()
    if point_hash(source) != upstream["projective_continuation"]["far"]["coordinate_hash"]:
        raise AssertionError("exact source is not the frozen far checkpoint")
    if face_key_set(source_faces) != face_key_set(fresh_exact_faces(source)):
        raise AssertionError("fresh source hull mismatch")

    ids = sorted(source)
    velocity, chart_scale = c.exact_velocity_from_coefficients(
        source, ids, ray["direction"]
    )
    path = c.frozen.line_points(source, velocity)
    support_lookup = {
        (face_index, witness): poly
        for face_index, witness, poly in ex.support_polynomials(path, source_faces)
    }
    event_polynomial = support_lookup[(57, 69)]
    if event_polynomial.degree != 1:
        raise AssertionError("selected event is no longer rational linear")
    root = -event_polynomial.c[0] / event_polynomial.c[1]
    if support_lookup[(58, 224)].eval(root):
        raise AssertionError("paired support row no longer shares the event root")

    pre_parameter = Q(numeric_scan["selected_event"]["pre_parameter"])
    post_parameter = Q(numeric_scan["selected_event"]["post_parameter"])
    if not Q(0) < pre_parameter < root < post_parameter:
        raise AssertionError("invalid strict rational samples")

    points = {
        "source": source,
        "pre": c.frozen.at(path, pre_parameter),
        "wall": c.frozen.at(path, root),
        "post": c.frozen.at(path, post_parameter),
    }
    pre_fresh_faces = fresh_exact_faces(points["pre"])
    faces = {
        "source": source_faces,
        # Keep the upstream face order for path-polynomial row identity.  The
        # independently proposed fresh ledger is compared immediately below;
        # only its arbitrary list order is discarded.
        "pre": source_faces,
        "wall": fresh_exact_faces(points["wall"]),
        "post": fresh_exact_faces(points["post"]),
    }
    if face_key_set(faces["source"]) != face_key_set(pre_fresh_faces):
        raise AssertionError("pre sample left the source cell")
    wall_quads = [face for face in faces["wall"] if frozenset(face) == EVENT_CIRCUIT]
    if len(wall_quads) != 1 or len(wall_quads[0]) != 4:
        raise AssertionError(("wall is not the unique expected quadrilateral", wall_quads))

    pre_edges = edge_set(faces["pre"])
    wall_edges = edge_set(faces["wall"])
    post_edges = edge_set(faces["post"])
    if pre_edges - wall_edges != {PRE_DIAGONAL}:
        raise AssertionError(("wrong pre-to-wall edge loss", pre_edges - wall_edges))
    if post_edges - wall_edges != {POST_DIAGONAL}:
        raise AssertionError(("wrong wall-to-post edge birth", post_edges - wall_edges))
    if wall_edges - pre_edges or wall_edges - post_edges:
        raise AssertionError("wall has an unexpected true edge")

    for name in points:
        write_exact_csv(POINT_FILES[name], points[name])
        write_faces(FACE_FILES[name], faces[name])

    path_definition = {
        "version": 1,
        "method": "explicit exact rational line reconstructed from the active sparse ray",
        "source_coordinate_hash": point_hash(source),
        "source_face_hash": face_hash(source_faces),
        "chart_scale_diagnostic": chart_scale,
        "velocity": {
            str(label): [ex.qs(value) for value in velocity[label]]
            for label in ids
        },
        "velocity_digest": canonical_hash(
            {
                str(label): [ex.qs(value) for value in velocity[label]]
                for label in ids
            }
        ),
        "event_root_exact": ex.qs(root),
        "event_root_decimal": float(root),
        "pre_parameter": ex.qs(pre_parameter),
        "post_parameter": ex.qs(post_parameter),
        "event_circuit": sorted(EVENT_CIRCUIT),
        "pre_diagonal": list(PRE_DIAGONAL),
        "post_diagonal": list(POST_DIAGONAL),
        "expected_zero_families": {
            key: sorted(value) for key, value in EXPECTED_ZERO_FAMILIES.items()
        },
    }
    PATH_DEFINITION.write_text(json.dumps(path_definition, indent=2) + "\n")

    print("auditing complete pre-event primitive ledger", flush=True)
    pre_audit = event_aware_interval_audit(
        path,
        faces["pre"],
        Q(0),
        root,
        root,
        EXPECTED_ZERO_FAMILIES["pre"],
    )
    print("auditing complete post-event primitive ledger", flush=True)
    post_audit = event_aware_interval_audit(
        path,
        faces["post"],
        root,
        post_parameter,
        root,
        EXPECTED_ZERO_FAMILIES["post"],
    )
    print("auditing full fourteen-component residual packet", flush=True)
    residual_audit = residual_packet_audit(path, faces["pre"], root)

    checkpoints = {}
    for name in ("source", "pre", "wall", "post"):
        print("checkpoint", name, flush=True)
        checkpoints[name] = checkpoint(name, points[name], faces[name])

    expected_missing = {
        "source": [],
        "pre": [],
        "wall": [[255, 256]],
        "post": [[255, 256]],
    }
    for name, missing in expected_missing.items():
        if checkpoints[name]["missing_forced_rails"] != missing:
            raise AssertionError((name, checkpoints[name]["missing_forced_rails"]))

    event_root_record = {
        "exact": ex.qs(root),
        "decimal": float(root),
        "polynomial_degree": event_polynomial.degree,
        "polynomial_exact": event_polynomial.exact(),
        "polynomial_digest": polynomial_hash(event_polynomial),
        "source_sign": 1 if event_polynomial.eval(Q(0)) > 0 else -1,
        "derivative_sign": 1 if event_polynomial.c[1] > 0 else -1,
    }
    if event_root_record["source_sign"] != -event_root_record["derivative_sign"]:
        raise AssertionError("event polynomial does not cross from the source side")

    data_paths = [
        PATH_DEFINITION,
        *(POINT_FILES[name] for name in ("source", "pre", "wall", "post")),
        *(FACE_FILES[name] for name in ("source", "pre", "wall", "post")),
    ]
    generated_hashes = {path.name: sha256(path) for path in data_paths}
    certificate = {
        "version": 1,
        "type": "exact-directed-first-event-and-rail-obstruction",
        "verdict": "EXACT_ACTIVE_FOUR_RESIDUAL_RAY_FIRST_EVENT_RAIL_OBSTRUCTION_PASS",
        "winner_status": "NONWINNER",
        "scope": (
            "The explicit rationalized active sparse ray from the exact far "
            "checkpoint only; this is not a cone-wide or global obstruction."
        ),
        "provenance": {
            str(UPSTREAM_CERTIFICATE.relative_to(ROOT)): sha256(UPSTREAM_CERTIFICATE),
            str(UPSTREAM_FACES.relative_to(ROOT)): sha256(UPSTREAM_FACES),
            str(RAY.relative_to(ROOT)): sha256(RAY),
            str(NUMERIC_SCAN.relative_to(ROOT)): sha256(NUMERIC_SCAN),
            "upstream_far_coordinate_hash": upstream["projective_continuation"]["far"]["coordinate_hash"],
            "source_reconstruction": source_reconstruction,
        },
        "path": path_definition,
        "event": {
            "root": event_root_record,
            "circuit": sorted(EVENT_CIRCUIT),
            "wall_maximal_face": wall_quads[0],
            "pre_diagonal": list(PRE_DIAGONAL),
            "post_diagonal": list(POST_DIAGONAL),
            "pre_to_wall_removed_edges": [list(edge) for edge in sorted(pre_edges - wall_edges)],
            "wall_to_post_added_edges": [list(edge) for edge in sorted(post_edges - wall_edges)],
            "pre_to_post_removed_faces": sorted(
                (sorted(face) for face in face_key_set(faces["pre"]) - face_key_set(faces["post"])),
                key=lambda row: row,
            ),
            "pre_to_post_added_faces": sorted(
                (sorted(face) for face in face_key_set(faces["post"]) - face_key_set(faces["pre"])),
                key=lambda row: row,
            ),
            "complete_pre_interval_audit": pre_audit,
            "complete_post_interval_audit": post_audit,
        },
        "residual_packet": residual_audit,
        "checkpoints": checkpoints,
        "obstruction": {
            "first_event_is_target_equilibrium_death": False,
            "class_before_wall_after": [EXPECTED_CLASS, EXPECTED_CLASS, EXPECTED_CLASS],
            "forced_rail_lost_at_wall": [255, 256],
            "forced_rail_count_before": len(forced_rails()),
            "forced_rail_count_after": len(forced_rails()) - 1,
            "valid_rail_preserving_adjacent_cell_exists_on_this_crossing": False,
            "reason": (
                "The unique first circuit wall is the convex quadrilateral "
                "{69,224,255,256}.  Its source diagonal (255,256) is one of "
                "the 37 forced rails; the wall has neither diagonal and the "
                "only opposite strict cell has diagonal (69,224)."
            ),
            "interpretation": (
                "All four selected limiting components move strictly toward "
                "zero, but by less than 2.7e-6 relatively before the mandatory "
                "rail is lost.  The event leaves equilibrium class (2,2,2) "
                "unchanged and therefore does not remove S, U1, H45, or H1213."
            ),
        },
        "generated_file_sha256": generated_hashes,
    }
    CERTIFICATE.write_text(json.dumps(certificate, indent=2) + "\n")

    manifest_paths = [
        HERE / "attack_common.py",
        HERE / "build_exact_event_certificate.py",
        HERE / "verify_exact_event_certificate.py",
        CERTIFICATE,
        *data_paths,
    ]
    if not all(path.exists() for path in manifest_paths):
        raise AssertionError("manifest input missing")
    MANIFEST.write_text(manifest_text(manifest_paths))

    print("EXACT_ACTIVE_FOUR_RESIDUAL_RAY_FIRST_EVENT_RAIL_OBSTRUCTION_PASS")
    print("winner_status", certificate["winner_status"])
    print("event_root", ex.qs(root))
    print("event_root_decimal", float(root))
    print("pre_class", checkpoints["pre"]["exact_mechanics"]["class"])
    print("wall_class", checkpoints["wall"]["exact_mechanics"]["class"])
    print("post_class", checkpoints["post"]["exact_mechanics"]["class"])
    print("post_missing_rails", checkpoints["post"]["missing_forced_rails"])
    print("certificate_sha256", sha256(CERTIFICATE))
    print("manifest_sha256", sha256(MANIFEST))


if __name__ == "__main__":
    main()
