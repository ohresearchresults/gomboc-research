#!/usr/bin/env python3
"""Clean-room verification of the guarded full-control H1011 continuation.

This verifier owns no inputs outside ``agent_sparse`` and never rewrites the
parallel ``continuation/main`` artifacts.  It reconstructs the rational path
from the frozen endpoint, enumerates the complete support/mechanics packet,
re-isolates all four algebraic events, rebuilds the support flip, recomputes
the body's exact uniform-volume centroid at every checkpoint, and writes only
its own compact verification receipt.
"""
from __future__ import annotations

import hashlib
import json
import sys
from fractions import Fraction as Q
from pathlib import Path


sys.set_int_max_str_digits(0)

HERE = Path(__file__).resolve().parent
MAIN = HERE.parent / "main"
ATTACK = HERE.parents[1]
TRACK = ATTACK.parent
ROOT = HERE.parents[4]

SOURCE = ATTACK / "exact_circuit_far.csv"
SOURCE_FACES = ATTACK / "exact_circuit_post_faces.json"
PROPOSAL = MAIN / "full_control_proposal.json"
PROPOSAL_ENDPOINT = MAIN / "full_control_candidate.csv"
SCAN = MAIN / "first_event_scan.json"
CERTIFICATE = MAIN / "exact_full_control_chain_certificate.json"
GENERATED = {
    "pre": MAIN / "exact_full_control_chain_pre.csv",
    "post": MAIN / "exact_full_control_chain_post.csv",
    "far": MAIN / "exact_full_control_chain_far.csv",
    "wall_faces": MAIN / "exact_full_control_chain_wall_faces.json",
    "post_faces": MAIN / "exact_full_control_chain_post_faces.json",
}
OUTPUT = HERE / "integrated_full_control_verification.json"

sys.path.insert(0, str(TRACK / "rigorous_local_bypass"))
import exact_core as ex  # noqa: E402
sys.path.insert(0, str(ATTACK))
import build_exact_circuit_flip as parent_exact  # noqa: E402


BASE = frozenset(range(17)) | {54}
PRIMARY = (7, 8, 245)
EXPECTED_ACTIVE = [
    0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16,
    54, 69, 72, 73, 88, 198, 224, 228, 229, 230, 231, 232, 233, 234,
    235, 236, 237, 238, 239, 240, 241, 242, 243, 244, 245, 246, 247,
    248, 249, 250, 251, 252, 253, 254, 255, 256, 257, 258, 259, 260,
    261, 262, 263, 264,
]
PROTECTED = {
    "stable": [sorted(BASE), list(PRIMARY)],
    "unstable": [8, 54],
    "saddles": [[5, 6], [10, 11]],
}
TARGET_CIRCUIT = (228, 229, 230, 231)
REMOVED_FACES = ((228, 231, 230), (228, 230, 229))
ADDED_FACES = ((228, 231, 229), (229, 231, 230))
WALL_FACE = (228, 231, 230, 229)
REMOVED_EDGE = (228, 230)
ADDED_EDGE = (229, 231)
ROOT_WIDTH = Q(1, 10**30)

EVENTS = (
    {
        "name": "transfer_228_229",
        "target": "edge:(228, 229):beta2",
        "family": (
            "edge:(228, 229):beta2",
            "face_raw:(198, 228, 229):(228, 229)",
        ),
    },
    {
        "name": "transfer_198_228",
        "target": "edge:(198, 228):beta1",
        "family": (
            "edge:(198, 228):beta1",
            "face_raw:(198, 228, 229):(198, 228)",
        ),
    },
    {
        "name": "transfer_198_229",
        "target": "edge:(198, 229):beta2",
        "family": (
            "edge:(198, 229):beta2",
            "face_raw:(198, 228, 229):(198, 229)",
        ),
    },
    {
        "name": "support_flip_228_230_to_229_231",
        "target": "support:f84:w229",
        "family": (
            "edge:(228, 230):beta1",
            "edge:(228, 230):beta2",
            "edge:(228, 230):gram",
            "support:f84:w229",
            "support:f99:w231",
        ),
    },
)
NEXT_FORBIDDEN = "support:f83:w229"


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def canonical_hash(value) -> str:
    return hashlib.sha256(
        json.dumps(value, sort_keys=True, separators=(",", ":")).encode()
    ).hexdigest()


def evaluate_path(path, parameter):
    return {
        label: tuple(coordinate.eval(parameter) for coordinate in xyz)
        for label, xyz in path.items()
    }


def restrict_path(path, lo, hi):
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


def build_face_ledgers(pre_faces):
    removed = {tuple(sorted(face)) for face in REMOVED_FACES}
    kept = [face for face in pre_faces if tuple(sorted(face)) not in removed]
    assert len(pre_faces) - len(kept) == 2
    return pre_faces, kept + [list(WALL_FACE)], kept + [list(x) for x in ADDED_FACES]


def primitive_rows(path, faces):
    ledger = ex.mechanics_primitives(path, faces)
    yield "volume_d6", ledger["d6"], "mechanics_denominator"
    for face_index, witness, polynomial in ex.support_polynomials(path, faces):
        yield f"support:f{face_index}:w{witness}", polynomial, "support"
    for face_key, rows in sorted(ledger["reference"].items()):
        for edge, value in sorted(rows.items()):
            yield f"face_reference:{face_key}:{edge}", value, "mechanics_denominator"
    for face_key, rows in sorted(ledger["face"].items()):
        for edge, value in sorted(rows.items()):
            yield f"face_raw:{face_key}:{edge}", value, "face_component"
    for vertex, rows in sorted(ledger["vertex"].items()):
        for neighbor, value in sorted(rows.items()):
            yield f"vertex:{vertex}:{neighbor}", value, "vertex_component"
    for edge, rows in sorted(ledger["edge"].items()):
        for component in (
            "direction_norm2", "gram", "t", "one_minus_t", "beta1", "beta2"
        ):
            yield f"edge:{edge}:{component}", rows[component], "edge_component"


def trim(coefficients):
    result = list(coefficients)
    while len(result) > 1 and result[-1] == 0:
        result.pop()
    return result or [Q(0)]


def divmod_poly(a, b):
    numerator = trim(a)
    denominator = trim(b)
    if denominator == [Q(0)]:
        raise ZeroDivisionError
    quotient = [Q(0)] * max(1, len(numerator) - len(denominator) + 1)
    while len(numerator) >= len(denominator) and numerator != [Q(0)]:
        shift = len(numerator) - len(denominator)
        factor = numerator[-1] / denominator[-1]
        quotient[shift] += factor
        for index, coefficient in enumerate(denominator):
            numerator[index + shift] -= factor * coefficient
        numerator = trim(numerator)
    return trim(quotient), numerator


def monic_gcd(a: ex.P, b: ex.P) -> ex.P:
    left = trim(a.c)
    right = trim(b.c)
    while right != [Q(0)]:
        _quotient, remainder = divmod_poly(left, right)
        left, right = right, remainder
    leading = left[-1]
    return ex.P(tuple(value / leading for value in left))


def exhaustive_interval(rows, lo, hi):
    digest = hashlib.sha256()
    count = 0
    leaves = 0
    worst = None
    for name, polynomial, family in rows:
        sign, row_leaves, margin = ex.bernstein_sign(
            polynomial, lo, hi, max_depth=60
        )
        count += 1
        leaves += row_leaves
        worst = margin if worst is None else min(worst, margin)
        digest.update(
            f"{name}|{family}|{sign}|{'|'.join(polynomial.exact())}\n".encode()
        )
    return {
        "lo": ex.qs(lo),
        "hi": ex.qs(hi),
        "primitive_count": count,
        "bernstein_leaf_count": leaves,
        "minimum_bernstein_log10_abs": worst,
        "primitive_digest": digest.hexdigest(),
    }


def verify_root(polynomial, stored):
    assert polynomial.degree == stored["polynomial_degree"]
    assert polynomial.exact() == stored["polynomial_exact"]
    assert canonical_hash(polynomial.exact()) == stored["polynomial_digest"]
    lo, hi = Q(stored["lo"]), Q(stored["hi"])
    width = hi - lo if hi > lo else Q(1, 10**60)
    root = ex.isolate_monotone_root(polynomial, lo, hi, width)
    assert ex.qs(root["lo"]) == stored["lo"]
    assert ex.qs(root["hi"]) == stored["hi"]
    assert ex.qs(root["value_lo"]) == stored["value_lo"]
    assert ex.qs(root["value_hi"]) == stored["value_hi"]
    assert root["derivative_sign"] == stored["derivative_sign"]
    return root


def verify_event(rows, event, root, target, stored):
    by_name = {name: (poly, family) for name, poly, family in rows}
    expected = set(event["family"])
    assert expected.issubset(by_name)
    strict_count = 0
    strict_leaves = 0
    worst = None
    for name, polynomial, _family in rows:
        if name in expected:
            continue
        _sign, leaves, margin = ex.bernstein_sign(
            polynomial, root["lo"], root["hi"], max_depth=60
        )
        strict_count += 1
        strict_leaves += leaves
        worst = margin if worst is None else min(worst, margin)
    shared = {}
    for name in event["family"]:
        polynomial, family = by_name[name]
        gcd = monic_gcd(target, polynomial)
        assert gcd.degree >= 1
        gcd_root = ex.isolate_monotone_root(
            gcd, root["lo"], root["hi"], ROOT_WIDTH
        )
        assert gcd_root["lo"] <= root["hi"] and gcd_root["hi"] >= root["lo"]
        shared[name] = {
            "family": family,
            "polynomial_degree": polynomial.degree,
            "polynomial_digest": canonical_hash(polynomial.exact()),
            "gcd_degree": gcd.degree,
            "gcd_exact": gcd.exact(),
            "gcd_digest": canonical_hash(gcd.exact()),
            "gcd_root_interval": [ex.qs(gcd_root["lo"]), ex.qs(gcd_root["hi"])],
        }
    actual = {
        "event_name": event["name"],
        "target_name": event["target"],
        "allowed_zero_family": list(event["family"]),
        "strict_other_primitive_count": strict_count,
        "strict_other_bernstein_leaf_count": strict_leaves,
        "strict_other_minimum_bernstein_log10_abs": worst,
        "shared_algebraic_factor": shared,
    }
    for key, value in stored.items():
        if key != "class_cover" and key not in ("first_support_wall", "wall_class_cover"):
            assert actual[key] == value, (event["name"], key)


def checkpoint(points, faces, expected_f):
    support = ex.supporting_cell(points, faces)
    _ledger, mechanics = ex.classify_point(points, faces)
    assert support["f_vector"] == expected_f
    assert support["active_labels"] == EXPECTED_ACTIVE
    assert mechanics["class"] == [2, 2, 2]
    assert BASE in {frozenset(face) for face in faces}
    assert parent_exact.forced_rails().issubset(set(support["edges"]))
    d6, m24 = ex.exact_centroid_numerators(points, faces)
    centroid = tuple(value / (4 * d6) for value in m24)
    constant_path = {
        label: tuple(ex.P((value,)) for value in xyz)
        for label, xyz in points.items()
    }
    rows = list(primitive_rows(constant_path, faces))
    assert all(poly.eval(Q(0)) for _name, poly, _family in rows)
    return {
        "coordinate_hash": canonical_hash({
            str(label): [ex.qs(value) for value in points[label]]
            for label in sorted(points)
        }),
        "exact_centroid": [ex.qs(value) for value in centroid],
        "exact_support": {key: value for key, value in support.items() if key != "edges"},
        "exact_mechanics": mechanics,
        "exhaustive_primitive_count": len(rows),
        "base_face_present": True,
        "forced_rail_count": len(parent_exact.forced_rails()),
        "missing_forced_rails": [],
    }


def h910_audit(path, pre_faces, wall_faces, post_faces, root, end):
    records = {}
    components = ("t", "one_minus_t", "beta1", "beta2")
    for name, faces, lo, hi in (
        ("pre", pre_faces, Q(0), root["lo"]),
        ("wall", wall_faces, root["lo"], root["hi"]),
        ("post", post_faces, root["hi"], end),
    ):
        values = ex.mechanics_primitives(path, faces)["edge"][(9, 10)]
        middle = (lo + hi) / 2
        witness = min(components, key=lambda item: values[item].eval(middle))
        polynomial = values[witness]
        assert polynomial.eval(middle) < 0
        sign, leaves, worst = ex.bernstein_sign(polynomial, lo, hi, max_depth=60)
        assert sign == -1
        records[name] = {
            "component": witness,
            "lo_value": ex.qs(polynomial.eval(lo)),
            "hi_value": ex.qs(polynomial.eval(hi)),
            "sign": sign,
            "bernstein_leaf_count": leaves,
            "minimum_bernstein_log10_abs": worst,
            "polynomial_degree": polynomial.degree,
            "polynomial_digest": canonical_hash(polynomial.exact()),
        }
    return {"piecewise_exact_negative_witness": records}


def main():
    frozen = json.loads(CERTIFICATE.read_text())
    assert frozen["verdict"] == "EXACT_FULL_CONTROL_THREE_TRANSFER_SAFE_FLIP_CHAIN_PASS"
    proposal = json.loads(PROPOSAL.read_text())
    scan = json.loads(SCAN.read_text())
    assert proposal["verdict"] == "FULL_CONTROL_RATIONAL_ACTUAL_CELL_DESCENT_PROPOSAL_PASS"
    assert scan["verdict"] == "EXHAUSTIVE_EXACT_FIRST_EVENT_LOCATOR_PASS"

    for file in (SOURCE, SOURCE_FACES, PROPOSAL, PROPOSAL_ENDPOINT, SCAN):
        key = str(file.relative_to(ROOT))
        assert sha256(file) == frozen["source_hashes"][key]

    source = ex.read_rows(SOURCE)
    endpoint = ex.read_rows(PROPOSAL_ENDPOINT)
    path = {
        label: tuple(
            ex.P((source[label][axis], endpoint[label][axis] - source[label][axis]))
            for axis in range(3)
        )
        for label in source
    }
    expected_delta_digest = canonical_hash({
        str(label): [
            ex.qs(endpoint[label][axis] - source[label][axis]) for axis in range(3)
        ]
        for label in sorted(source)
    })
    assert expected_delta_digest == frozen["path"]["endpoint_delta_digest"]

    pre_faces, wall_faces, post_faces = build_face_ledgers(
        json.loads(SOURCE_FACES.read_text())
    )
    pre_rows = list(primitive_rows(path, pre_faces))
    assert len(pre_rows) == 7904
    by_name = {name: polynomial for name, polynomial, _family in pre_rows}

    roots = []
    for event, stored_root, stored_audit in zip(
        EVENTS, frozen["path"]["event_roots"], frozen["event_audits"]
    ):
        assert stored_root["event"] == event["name"]
        target = by_name[event["target"]]
        root = verify_root(target, stored_root)
        verify_event(pre_rows, event, root, target, stored_audit)
        roots.append(root)
    assert all(left["hi"] < right["lo"] for left, right in zip(roots, roots[1:]))

    next_stored = frozen["path"]["next_forbidden_event"]
    assert next_stored["name"] == NEXT_FORBIDDEN
    next_root = verify_root(by_name[NEXT_FORBIDDEN], next_stored)
    assert roots[-1]["hi"] < next_root["lo"]
    end = (roots[-1]["hi"] + next_root["lo"]) / 2
    assert ex.qs(end) == frozen["path"]["far_parameter"]

    bounds = [(Q(0), roots[0]["lo"])]
    bounds.extend((left["hi"], right["lo"]) for left, right in zip(roots, roots[1:]))
    rebuilt_intervals = []
    for index, (lo, hi) in enumerate(bounds):
        rebuilt_intervals.append({
            "name": f"pre_open_cell_{index}",
            "exhaustive": exhaustive_interval(pre_rows, lo, hi),
            "class_cover": ex.certify_path_segment(
                restrict_path(path, lo, hi), pre_faces, PROTECTED
            ),
        })
    for index, root in enumerate(roots[:3]):
        cover = ex.certify_mechanics_interval(
            path, pre_faces, PROTECTED, root["lo"], root["hi"]
        )
        assert cover["midpoint_class"]["class"] == [2, 2, 2]
        assert cover == frozen["event_audits"][index]["class_cover"]

    support_target = by_name[EVENTS[-1]["target"]]
    first_support = ex.certify_first_support_wall(
        path, pre_faces, roots[-1], support_target
    )
    assert first_support == frozen["event_audits"][-1]["first_support_wall"]
    expected_support_family = {
        (tuple(sorted(REMOVED_FACES[0])), 229),
        (tuple(sorted(REMOVED_FACES[1])), 231),
    }
    actual_support_family = {
        (tuple(sorted(pre_faces[row["face_index"]])), row["witness"])
        for row in first_support["target_support_family"]
    }
    assert actual_support_family == expected_support_family
    wall_cover = ex.certify_mechanics_interval(
        path, wall_faces, PROTECTED, roots[-1]["lo"], roots[-1]["hi"]
    )
    assert wall_cover == frozen["event_audits"][-1]["wall_class_cover"]

    post_rows = list(primitive_rows(path, post_faces))
    rebuilt_intervals.append({
        "name": "post_flip_open_cell",
        "exhaustive": exhaustive_interval(post_rows, roots[-1]["hi"], end),
        "class_cover": ex.certify_path_segment(
            restrict_path(path, roots[-1]["hi"], end), post_faces, PROTECTED
        ),
    })
    assert rebuilt_intervals == frozen["open_intervals"]

    pre_edges, wall_edges, post_edges = map(edge_set, (pre_faces, wall_faces, post_faces))
    assert pre_edges - post_edges == {REMOVED_EDGE}
    assert post_edges - pre_edges == {ADDED_EDGE}
    assert [61, len(wall_edges), len(wall_faces)] == [61, 161, 102]
    for faces, edges in (
        (pre_faces, pre_edges), (wall_faces, wall_edges), (post_faces, post_edges)
    ):
        assert BASE in {frozenset(face) for face in faces}
        assert parent_exact.forced_rails().issubset(edges)
    assert frozen["topology_event"]["removed_true_edge"] == list(REMOVED_EDGE)
    assert frozen["topology_event"]["added_true_edge"] == list(ADDED_EDGE)
    assert frozen["topology_event"]["active_rows_preserved"] == 61
    assert frozen["topology_event"]["forced_rails_preserved"] == 37

    parameters = {
        name: Q(value) for name, value in frozen["rational_parameters"].items()
    }
    faces_for = {
        "source": pre_faces, "pre": pre_faces,
        "post": post_faces, "far": post_faces,
    }
    points_for = {
        name: evaluate_path(path, parameter) for name, parameter in parameters.items()
    }
    for name, points in points_for.items():
        assert checkpoint(points, faces_for[name], [61, 162, 103]) == frozen["rational_checkpoints"][name]
    assert ex.read_rows(GENERATED["pre"]) == points_for["pre"]
    assert ex.read_rows(GENERATED["post"]) == points_for["post"]
    assert ex.read_rows(GENERATED["far"]) == points_for["far"]
    assert json.loads(GENERATED["wall_faces"].read_text()) == wall_faces
    assert json.loads(GENERATED["post_faces"].read_text()) == post_faces

    residuals = parent_exact.residual_direction_audit(
        path, pre_faces, post_faces, roots[-1], end
    )
    assert residuals == frozen["directed_residuals"]
    assert all(row["strict_endpoint_improvement"] for row in residuals.values())
    h910 = h910_audit(path, pre_faces, wall_faces, post_faces, roots[-1], end)
    assert h910 == frozen["h910_nonresurrection"]

    for file in GENERATED.values():
        key = str(file.relative_to(ROOT))
        assert sha256(file) == frozen["generated_file_sha256"][key]

    receipt = {
        "version": 1,
        "source_certificate": str(CERTIFICATE.relative_to(ROOT)),
        "source_certificate_sha256": sha256(CERTIFICATE),
        "independent_reconstruction": {
            "pre_primitive_count": len(pre_rows),
            "post_primitive_count": len(post_rows),
            "event_count": len(roots),
            "event_decimal_intervals": [
                [float(root["lo"]), float(root["hi"])] for root in roots
            ],
            "far_parameter": ex.qs(end),
            "far_class": frozen["residual_verdict"]["far_class"],
            "forced_rails": 37,
            "h910_strictly_dead": True,
            "far_decisions": {
                name: row["far"]["decision_value"] for name, row in residuals.items()
            },
        },
        "verdict": "INDEPENDENT_INTEGRATED_EXACT_FULL_CONTROL_CHAIN_PASS",
    }
    OUTPUT.write_text(json.dumps(receipt, indent=2) + "\n")
    print(receipt["verdict"])


if __name__ == "__main__":
    main()
