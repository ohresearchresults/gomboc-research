#!/usr/bin/env python3
"""Exactify the full-control ray through three transfers and one safe flip."""
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
ATTACK = HERE.parents[1]
TRACK = ATTACK.parent
ROOT = HERE.parents[4]
SOURCE = ATTACK / "exact_circuit_far.csv"
PRE_FACES_PATH = ATTACK / "exact_circuit_post_faces.json"
PROPOSAL = HERE / "full_control_proposal.json"
PROPOSAL_ENDPOINT = HERE / "full_control_candidate.csv"
SCAN = HERE / "first_event_scan.json"
CERTIFICATE = HERE / "exact_full_control_chain_certificate.json"
PRE_OUT = HERE / "exact_full_control_chain_pre.csv"
POST_OUT = HERE / "exact_full_control_chain_post.csv"
FAR_OUT = HERE / "exact_full_control_chain_far.csv"
WALL_FACES_OUT = HERE / "exact_full_control_chain_wall_faces.json"
POST_FACES_OUT = HERE / "exact_full_control_chain_post_faces.json"

sys.path.insert(0, str(TRACK / "rigorous_local_bypass"))
import exact_core as ex  # noqa: E402
sys.path.insert(0, str(ATTACK))
import build_exact_circuit_flip as frozen  # noqa: E402


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


def write_exact_csv(path: Path, rows) -> None:
    with path.open("w", newline="") as handle:
        writer = csv.writer(handle)
        writer.writerow(("source_id", "x", "y", "z"))
        for label in sorted(rows):
            writer.writerow((label, *(ex.qs(value) for value in rows[label])))


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
    if len(pre_faces) - len(kept) != 2:
        raise AssertionError("safe-flip pre faces missing")
    wall = kept + [list(WALL_FACE)]
    post = kept + [list(face) for face in ADDED_FACES]
    return pre_faces, wall, post


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


def isolate(polynomial, bracket):
    lo, hi = bracket
    root = ex.isolate_monotone_root(polynomial, lo, hi, ROOT_WIDTH)
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


def exhaustive_strict_interval(rows, lo, hi):
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


def exact_event_audit(rows, event, root, target):
    by_name = {name: (polynomial, family) for name, polynomial, family in rows}
    expected = set(event["family"])
    if not expected.issubset(by_name):
        raise AssertionError((event["name"], sorted(expected - set(by_name))))
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
        if gcd.degree < 1:
            raise AssertionError((event["name"], name, "no common algebraic factor"))
        gcd_root = ex.isolate_monotone_root(
            gcd, root["lo"], root["hi"], ROOT_WIDTH
        )
        if not (
            gcd_root["lo"] <= root["hi"] and gcd_root["hi"] >= root["lo"]
        ):
            raise AssertionError((event["name"], name, "disjoint gcd root"))
        shared[name] = {
            "family": family,
            "polynomial_degree": polynomial.degree,
            "polynomial_digest": canonical_hash(polynomial.exact()),
            "gcd_degree": gcd.degree,
            "gcd_exact": gcd.exact(),
            "gcd_digest": canonical_hash(gcd.exact()),
            "gcd_root_interval": [ex.qs(gcd_root["lo"]), ex.qs(gcd_root["hi"])],
        }
    return {
        "event_name": event["name"],
        "target_name": event["target"],
        "allowed_zero_family": list(event["family"]),
        "strict_other_primitive_count": strict_count,
        "strict_other_bernstein_leaf_count": strict_leaves,
        "strict_other_minimum_bernstein_log10_abs": worst,
        "shared_algebraic_factor": shared,
    }


def checkpoint(points, faces, expected_f):
    support = ex.supporting_cell(points, faces)
    _ledger, mechanics = ex.classify_point(points, faces)
    if support["f_vector"] != expected_f:
        raise AssertionError(support)
    if support["active_labels"] != EXPECTED_ACTIVE:
        raise AssertionError(("active labels", support["active_labels"]))
    if mechanics["class"] != [2, 2, 2]:
        raise AssertionError(mechanics)
    if BASE not in {frozenset(face) for face in faces}:
        raise AssertionError("base absent")
    missing = sorted(frozen.forced_rails() - set(support["edges"]))
    if missing:
        raise AssertionError(("rails absent", missing))
    d6, m24 = ex.exact_centroid_numerators(points, faces)
    centroid = tuple(value / (4 * d6) for value in m24)
    rows = list(primitive_rows({i: tuple(ex.P((x,)) for x in p) for i, p in points.items()}, faces))
    if not all(poly.eval(Q(0)) for _name, poly, _family in rows):
        raise AssertionError("zero checkpoint primitive")
    return {
        "coordinate_hash": canonical_hash({
            str(label): [ex.qs(x) for x in points[label]] for label in sorted(points)
        }),
        "exact_centroid": [ex.qs(value) for value in centroid],
        "exact_support": {key: value for key, value in support.items() if key != "edges"},
        "exact_mechanics": mechanics,
        "exhaustive_primitive_count": len(rows),
        "base_face_present": True,
        "forced_rail_count": len(frozen.forced_rails()),
        "missing_forced_rails": [],
    }


def h910_audit(path, pre_faces, wall_faces, post_faces, root, end):
    components = ("t", "one_minus_t", "beta1", "beta2")
    records = {}
    for name, faces, lo, hi in (
        ("pre", pre_faces, Q(0), root["lo"]),
        ("wall", wall_faces, root["lo"], root["hi"]),
        ("post", post_faces, root["hi"], end),
    ):
        ledger = ex.mechanics_primitives(path, faces)
        values = ledger["edge"][(9, 10)]
        middle = (lo + hi) / 2
        witness = min(components, key=lambda item: values[item].eval(middle))
        polynomial = values[witness]
        if polynomial.eval(middle) >= 0:
            raise AssertionError((name, "H910 has no negative witness"))
        sign, leaves, worst = ex.bernstein_sign(
            polynomial, lo, hi, max_depth=60
        )
        if sign != -1:
            raise AssertionError((name, "H910 returns"))
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
    proposal = json.loads(PROPOSAL.read_text())
    scan = json.loads(SCAN.read_text())
    if proposal["verdict"] != "FULL_CONTROL_RATIONAL_ACTUAL_CELL_DESCENT_PROPOSAL_PASS":
        raise AssertionError(proposal["verdict"])
    if scan["verdict"] != "EXHAUSTIVE_EXACT_FIRST_EVENT_LOCATOR_PASS":
        raise AssertionError(scan["verdict"])
    source = ex.read_rows(SOURCE)
    proposal_endpoint = ex.read_rows(PROPOSAL_ENDPOINT)
    path = {
        label: tuple(
            ex.P((source[label][axis], proposal_endpoint[label][axis] - source[label][axis]))
            for axis in range(3)
        )
        for label in source
    }
    pre_faces, wall_faces, post_faces = build_face_ledgers(
        json.loads(PRE_FACES_PATH.read_text())
    )
    pre_rows = list(primitive_rows(path, pre_faces))
    by_name = {name: polynomial for name, polynomial, _family in pre_rows}
    scan_candidates = {
        row["name"]: row for row in scan["next_candidates"]
    }

    roots = []
    root_records = []
    event_audits = []
    for event in EVENTS:
        candidate = scan_candidates[event["target"]]
        bracket = (Q(candidate["lo"]), Q(candidate["hi"]))
        target = by_name[event["target"]]
        root, record = isolate(target, bracket)
        roots.append(root)
        root_records.append(record)
        event_audits.append(exact_event_audit(pre_rows, event, root, target))
    if not all(left["hi"] < right["lo"] for left, right in zip(roots, roots[1:])):
        raise AssertionError("event roots not strictly ordered")

    next_candidate = scan_candidates[NEXT_FORBIDDEN]
    next_target = by_name[NEXT_FORBIDDEN]
    next_root, next_record = isolate(
        next_target, (Q(next_candidate["lo"]), Q(next_candidate["hi"]))
    )
    if not roots[-1]["hi"] < next_root["lo"]:
        raise AssertionError("safe post-flip cell is empty")
    end = (roots[-1]["hi"] + next_root["lo"]) / 2

    intervals = []
    bounds = [(Q(0), roots[0]["lo"])]
    bounds.extend((left["hi"], right["lo"]) for left, right in zip(roots, roots[1:]))
    for index, (lo, hi) in enumerate(bounds):
        intervals.append({
            "name": f"pre_open_cell_{index}",
            "exhaustive": exhaustive_strict_interval(pre_rows, lo, hi),
            "class_cover": ex.certify_path_segment(
                restrict_path(path, lo, hi), pre_faces, PROTECTED
            ),
        })
    for index, (event, root) in enumerate(zip(EVENTS[:3], roots[:3])):
        cover = ex.certify_mechanics_interval(
            path, pre_faces, PROTECTED, root["lo"], root["hi"]
        )
        if cover["midpoint_class"]["class"] != [2, 2, 2]:
            raise AssertionError((event["name"], cover))
        event_audits[index]["class_cover"] = cover

    target_support = by_name[EVENTS[-1]["target"]]
    first_support = ex.certify_first_support_wall(
        path, pre_faces, roots[-1], target_support
    )
    expected_support_family = {
        (tuple(sorted(REMOVED_FACES[0])), 229),
        (tuple(sorted(REMOVED_FACES[1])), 231),
    }
    actual_support_family = {
        (tuple(sorted(pre_faces[row["face_index"]])), row["witness"])
        for row in first_support["target_support_family"]
    }
    if actual_support_family != expected_support_family:
        raise AssertionError((actual_support_family, expected_support_family))
    wall_cover = ex.certify_mechanics_interval(
        path, wall_faces, PROTECTED, roots[-1]["lo"], roots[-1]["hi"]
    )
    if wall_cover["midpoint_class"]["class"] != [2, 2, 2]:
        raise AssertionError(wall_cover)
    event_audits[-1]["first_support_wall"] = first_support
    event_audits[-1]["wall_class_cover"] = wall_cover

    post_rows = list(primitive_rows(path, post_faces))
    post_interval = {
        "name": "post_flip_open_cell",
        "exhaustive": exhaustive_strict_interval(
            post_rows, roots[-1]["hi"], end
        ),
        "class_cover": ex.certify_path_segment(
            restrict_path(path, roots[-1]["hi"], end), post_faces, PROTECTED
        ),
    }
    intervals.append(post_interval)

    pre_edges = edge_set(pre_faces)
    wall_edges = edge_set(wall_faces)
    post_edges = edge_set(post_faces)
    if pre_edges - post_edges != {REMOVED_EDGE}:
        raise AssertionError(pre_edges - post_edges)
    if post_edges - pre_edges != {ADDED_EDGE}:
        raise AssertionError(post_edges - pre_edges)
    for name, faces, edges in (
        ("pre", pre_faces, pre_edges),
        ("wall", wall_faces, wall_edges),
        ("post", post_faces, post_edges),
    ):
        if BASE not in {frozenset(face) for face in faces}:
            raise AssertionError((name, "base absent"))
        missing = frozen.forced_rails() - edges
        if missing:
            raise AssertionError((name, "rails absent", sorted(missing)))

    pre_parameter = roots[-1]["lo"] - (roots[-1]["lo"] - roots[-2]["hi"]) / 4
    post_parameter = roots[-1]["hi"] + (end - roots[-1]["hi"]) / 3
    checkpoints = {
        "source": (Q(0), pre_faces, [61, 162, 103]),
        "pre": (pre_parameter, pre_faces, [61, 162, 103]),
        "post": (post_parameter, post_faces, [61, 162, 103]),
        "far": (end, post_faces, [61, 162, 103]),
    }
    checkpoint_records = {
        name: checkpoint(evaluate_path(path, parameter), faces, f_vector)
        for name, (parameter, faces, f_vector) in checkpoints.items()
    }
    points_pre = evaluate_path(path, pre_parameter)
    points_post = evaluate_path(path, post_parameter)
    points_far = evaluate_path(path, end)
    write_exact_csv(PRE_OUT, points_pre)
    write_exact_csv(POST_OUT, points_post)
    write_exact_csv(FAR_OUT, points_far)
    WALL_FACES_OUT.write_text(json.dumps(wall_faces, indent=2) + "\n")
    POST_FACES_OUT.write_text(json.dumps(post_faces, indent=2) + "\n")

    # The same selected normalized components remain strict minima, and every
    # directed defect improves at the exact post-flip far checkpoint.
    residuals = frozen.residual_direction_audit(
        path, pre_faces, post_faces, roots[-1], end
    )
    if not all(
        row["piecewise_derivative"][segment]["derivative_sign"] == -1
        for row in residuals.values() for segment in ("pre", "post")
    ):
        raise AssertionError("a selected residual is not monotonically decreasing")
    h910 = h910_audit(
        path, pre_faces, wall_faces, post_faces, roots[-1], end
    )

    generated = (PRE_OUT, POST_OUT, FAR_OUT, WALL_FACES_OUT, POST_FACES_OUT)
    certificate = {
        "version": 1,
        "type": "exact rational-affine full-control chain with algebraic transfers and support flip",
        "scope": (
            "Exact for the literal 165-mode rational ray from exact_circuit_far: "
            "all 7,904 pre-cell support/mechanics primitives, three algebraic "
            "zero-transfer events, the first support flip (228,230)->(229,231), "
            "the complete post-cell ledger up to a rational far checkpoint before "
            "the forbidden row-230 loss, own-centroid class, base, U8, H910 and rails."
        ),
        "source_hashes": {
            str(file.relative_to(ROOT)): sha256(file)
            for file in (SOURCE, PRE_FACES_PATH, PROPOSAL, PROPOSAL_ENDPOINT, SCAN)
        },
        "path": {
            "endpoint_delta_digest": canonical_hash({
                str(label): [
                    ex.qs(proposal_endpoint[label][axis] - source[label][axis])
                    for axis in range(3)
                ] for label in sorted(source)
            }),
            "event_roots": [
                {"event": event["name"], **record}
                for event, record in zip(EVENTS, root_records)
            ],
            "next_forbidden_event": {
                "name": NEXT_FORBIDDEN,
                **next_record,
                "interpretation": "crossing this wall removes active row 230",
            },
            "far_parameter": ex.qs(end),
            "strict_root_order": True,
        },
        "event_audits": event_audits,
        "open_intervals": intervals,
        "topology_event": {
            "pre_f_vector": [61, 162, 103],
            "wall_f_vector": [61, 161, 102],
            "post_f_vector": [61, 162, 103],
            "target_circuit": list(TARGET_CIRCUIT),
            "removed_maximal_faces": [list(face) for face in REMOVED_FACES],
            "wall_maximal_face": list(WALL_FACE),
            "added_maximal_faces": [list(face) for face in ADDED_FACES],
            "removed_true_edge": list(REMOVED_EDGE),
            "added_true_edge": list(ADDED_EDGE),
            "base_preserved": True,
            "active_rows_preserved": 61,
            "forced_rails_preserved": len(frozen.forced_rails()),
        },
        "rational_parameters": {
            name: ex.qs(parameter)
            for name, (parameter, _faces, _f_vector) in checkpoints.items()
        },
        "rational_checkpoints": checkpoint_records,
        "directed_residuals": residuals,
        "h910_nonresurrection": h910,
        "generated_file_sha256": {
            str(file.relative_to(ROOT)): sha256(file) for file in generated
        },
        "residual_verdict": {
            "winner": False,
            "far_class": [2, 2, 2],
            "remaining_extra_stable": list(PRIMARY),
            "remaining_extra_unstable": 54,
            "remaining_saddles": [[5, 6], [10, 11]],
            "next_action": (
                "Rebuild the full-control chart from exact_full_control_chain_far.csv "
                "in the new (229,231)-diagonal cell before the row-230-loss wall."
            ),
        },
        "verdict": "EXACT_FULL_CONTROL_THREE_TRANSFER_SAFE_FLIP_CHAIN_PASS",
    }
    CERTIFICATE.write_text(json.dumps(certificate, indent=2) + "\n")
    print(json.dumps({
        "verdict": certificate["verdict"],
        "event_roots": [
            {"event": row["event"], "interval": row["decimal_interval"]}
            for row in certificate["path"]["event_roots"]
        ],
        "topology": certificate["topology_event"],
        "far_parameter": certificate["path"]["far_parameter"],
        "far_decisions": {
            name: row["far"]["decision_value"]
            for name, row in residuals.items()
        },
        "certificate": str(CERTIFICATE),
    }, indent=2))


if __name__ == "__main__":
    main()
