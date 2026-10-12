#!/usr/bin/env python3
"""Independent reconstruction of the exact full-control safe-flip chain."""
from __future__ import annotations

import hashlib
import json
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
GENERATED = {
    "pre": HERE / "exact_full_control_chain_pre.csv",
    "post": HERE / "exact_full_control_chain_post.csv",
    "far": HERE / "exact_full_control_chain_far.csv",
    "wall_faces": HERE / "exact_full_control_chain_wall_faces.json",
    "post_faces": HERE / "exact_full_control_chain_post_faces.json",
}

sys.path.insert(0, str(TRACK / "rigorous_local_bypass"))
import exact_core as ex  # noqa: E402
sys.path.insert(0, str(ATTACK))
import verify_exact_circuit_flip as frozen_verify  # noqa: E402


BASE = frozenset(range(17)) | {54}
PRIMARY = (7, 8, 245)
PROTECTED = {
    "stable": [sorted(BASE), list(PRIMARY)],
    "unstable": [8, 54],
    "saddles": [[5, 6], [10, 11]],
}
EXPECTED_ACTIVE = [
    0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16,
    54, 69, 72, 73, 88, 198, 224, 228, 229, 230, 231, 232, 233, 234,
    235, 236, 237, 238, 239, 240, 241, 242, 243, 244, 245, 246, 247,
    248, 249, 250, 251, 252, 253, 254, 255, 256, 257, 258, 259, 260,
    261, 262, 263, 264,
]
REMOVED = {tuple(sorted((228, 231, 230))), tuple(sorted((228, 230, 229)))}
ADDED = [[228, 231, 229], [229, 231, 230]]
WALL = [228, 231, 230, 229]
ROOT_WIDTH = Q(1, 10**30)
EVENT_FAMILIES = (
    (
        "transfer_228_229",
        "edge:(228, 229):beta2",
        (
            "edge:(228, 229):beta2",
            "face_raw:(198, 228, 229):(228, 229)",
        ),
    ),
    (
        "transfer_198_228",
        "edge:(198, 228):beta1",
        (
            "edge:(198, 228):beta1",
            "face_raw:(198, 228, 229):(198, 228)",
        ),
    ),
    (
        "transfer_198_229",
        "edge:(198, 229):beta2",
        (
            "edge:(198, 229):beta2",
            "face_raw:(198, 228, 229):(198, 229)",
        ),
    ),
    (
        "support_flip_228_230_to_229_231",
        "support:f84:w229",
        (
            "edge:(228, 230):beta1",
            "edge:(228, 230):beta2",
            "edge:(228, 230):gram",
            "support:f84:w229",
            "support:f99:w231",
        ),
    ),
)


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


def restrict(path, lo, hi):
    return {
        label: tuple(coordinate.affine(lo, hi) for coordinate in xyz)
        for label, xyz in path.items()
    }


def edges(faces):
    return {
        tuple(sorted((a, b)))
        for face in faces
        for a, b in zip(face, face[1:] + face[:1])
    }


def rails():
    result = set()
    for route in (
        [228] + list(range(229, 247)) + [8],
        [228] + list(range(247, 265)) + [8],
    ):
        result.update(tuple(sorted(pair)) for pair in zip(route, route[1:]))
    result.remove((228, 229))
    return result


def ledgers():
    pre = json.loads(PRE_FACES_PATH.read_text())
    kept = [face for face in pre if tuple(sorted(face)) not in REMOVED]
    assert len(pre) - len(kept) == 2
    return pre, kept + [WALL], kept + ADDED


def primitives(path, faces):
    ledger = ex.mechanics_primitives(path, faces)
    yield "volume_d6", ledger["d6"], "mechanics_denominator"
    for face_index, witness, polynomial in ex.support_polynomials(path, faces):
        yield f"support:f{face_index}:w{witness}", polynomial, "support"
    for face_key, values in sorted(ledger["reference"].items()):
        for edge, polynomial in sorted(values.items()):
            yield f"face_reference:{face_key}:{edge}", polynomial, "mechanics_denominator"
    for face_key, values in sorted(ledger["face"].items()):
        for edge, polynomial in sorted(values.items()):
            yield f"face_raw:{face_key}:{edge}", polynomial, "face_component"
    for vertex, values in sorted(ledger["vertex"].items()):
        for neighbor, polynomial in sorted(values.items()):
            yield f"vertex:{vertex}:{neighbor}", polynomial, "vertex_component"
    for edge, values in sorted(ledger["edge"].items()):
        for component in (
            "direction_norm2", "gram", "t", "one_minus_t", "beta1", "beta2"
        ):
            yield f"edge:{edge}:{component}", values[component], "edge_component"


def clean(coefficients):
    coefficients = list(coefficients)
    while len(coefficients) > 1 and coefficients[-1] == 0:
        coefficients.pop()
    return coefficients or [Q(0)]


def remainder(left, right):
    left = clean(left)
    right = clean(right)
    while len(left) >= len(right) and left != [Q(0)]:
        shift = len(left) - len(right)
        scale = left[-1] / right[-1]
        for index, coefficient in enumerate(right):
            left[index + shift] -= scale * coefficient
        left = clean(left)
    return left


def rational_gcd(first, second):
    a, b = clean(first.c), clean(second.c)
    while b != [Q(0)]:
        a, b = b, remainder(a, b)
    scale = a[-1]
    return ex.P(tuple(value / scale for value in a))


def strict_interval(rows, lo, hi):
    digest = hashlib.sha256()
    leaves = 0
    worst = None
    count = 0
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


def event_audit(rows, event_name, target_name, family, root, target):
    lookup = {name: (polynomial, kind) for name, polynomial, kind in rows}
    strict_count = 0
    strict_leaves = 0
    worst = None
    allowed = set(family)
    for name, polynomial, _kind in rows:
        if name in allowed:
            continue
        _sign, leaves, margin = ex.bernstein_sign(
            polynomial, root["lo"], root["hi"], max_depth=60
        )
        strict_count += 1
        strict_leaves += leaves
        worst = margin if worst is None else min(worst, margin)
    shared = {}
    for name in family:
        polynomial, kind = lookup[name]
        gcd = rational_gcd(target, polynomial)
        assert gcd.degree >= 1
        isolated = ex.isolate_monotone_root(
            gcd, root["lo"], root["hi"], ROOT_WIDTH
        )
        shared[name] = {
            "family": kind,
            "polynomial_degree": polynomial.degree,
            "polynomial_digest": canonical_hash(polynomial.exact()),
            "gcd_degree": gcd.degree,
            "gcd_exact": gcd.exact(),
            "gcd_digest": canonical_hash(gcd.exact()),
            "gcd_root_interval": [ex.qs(isolated["lo"]), ex.qs(isolated["hi"])],
        }
    return {
        "event_name": event_name,
        "target_name": target_name,
        "allowed_zero_family": list(family),
        "strict_other_primitive_count": strict_count,
        "strict_other_bernstein_leaf_count": strict_leaves,
        "strict_other_minimum_bernstein_log10_abs": worst,
        "shared_algebraic_factor": shared,
    }


def exact_checkpoint(points, faces):
    support = ex.supporting_cell(points, faces)
    _ledger, mechanics = ex.classify_point(points, faces)
    assert support["f_vector"] == [61, 162, 103]
    assert support["active_labels"] == EXPECTED_ACTIVE
    assert mechanics["class"] == [2, 2, 2]
    assert BASE in {frozenset(face) for face in faces}
    assert rails().issubset(set(support["edges"]))
    d6, m24 = ex.exact_centroid_numerators(points, faces)
    centroid = tuple(value / (4 * d6) for value in m24)
    constant_path = {
        label: tuple(ex.P((value,)) for value in xyz)
        for label, xyz in points.items()
    }
    rows = list(primitives(constant_path, faces))
    assert all(polynomial.eval(Q(0)) for _name, polynomial, _kind in rows)
    return {
        "coordinate_hash": canonical_hash({
            str(label): [ex.qs(x) for x in points[label]] for label in sorted(points)
        }),
        "exact_centroid": [ex.qs(value) for value in centroid],
        "exact_support": {key: value for key, value in support.items() if key != "edges"},
        "exact_mechanics": mechanics,
        "exhaustive_primitive_count": len(rows),
        "base_face_present": True,
        "forced_rail_count": len(rails()),
        "missing_forced_rails": [],
    }


def verify_h910(path, pre, wall, post, root, end):
    components = ("t", "one_minus_t", "beta1", "beta2")
    output = {}
    for name, faces, lo, hi in (
        ("pre", pre, Q(0), root["lo"]),
        ("wall", wall, root["lo"], root["hi"]),
        ("post", post, root["hi"], end),
    ):
        values = ex.mechanics_primitives(path, faces)["edge"][(9, 10)]
        midpoint = (lo + hi) / 2
        witness = min(components, key=lambda item: values[item].eval(midpoint))
        polynomial = values[witness]
        assert polynomial.eval(midpoint) < 0
        sign, leaves, worst = ex.bernstein_sign(polynomial, lo, hi, max_depth=60)
        assert sign == -1
        output[name] = {
            "component": witness,
            "lo_value": ex.qs(polynomial.eval(lo)),
            "hi_value": ex.qs(polynomial.eval(hi)),
            "sign": sign,
            "bernstein_leaf_count": leaves,
            "minimum_bernstein_log10_abs": worst,
            "polynomial_degree": polynomial.degree,
            "polynomial_digest": canonical_hash(polynomial.exact()),
        }
    return {"piecewise_exact_negative_witness": output}


def main():
    frozen = json.loads(CERTIFICATE.read_text())
    assert frozen["verdict"] == "EXACT_FULL_CONTROL_THREE_TRANSFER_SAFE_FLIP_CHAIN_PASS"
    for file in (SOURCE, PRE_FACES_PATH, PROPOSAL, PROPOSAL_ENDPOINT, SCAN):
        key = str(file.relative_to(ROOT))
        assert sha256(file) == frozen["source_hashes"][key]

    source = ex.read_rows(SOURCE)
    proposal_endpoint = ex.read_rows(PROPOSAL_ENDPOINT)
    path = {
        label: tuple(
            ex.P((source[label][axis], proposal_endpoint[label][axis] - source[label][axis]))
            for axis in range(3)
        )
        for label in source
    }
    assert canonical_hash({
        str(label): [
            ex.qs(proposal_endpoint[label][axis] - source[label][axis])
            for axis in range(3)
        ] for label in sorted(source)
    }) == frozen["path"]["endpoint_delta_digest"]
    pre_faces, wall_faces, post_faces = ledgers()
    pre_rows = list(primitives(path, pre_faces))
    post_rows = list(primitives(path, post_faces))
    lookup = {name: polynomial for name, polynomial, _kind in pre_rows}

    roots = []
    audits = []
    for stored, (event_name, target_name, family) in zip(
        frozen["path"]["event_roots"], EVENT_FAMILIES
    ):
        assert stored["event"] == event_name
        target = lookup[target_name]
        assert target.exact() == stored["polynomial_exact"]
        assert canonical_hash(target.exact()) == stored["polynomial_digest"]
        root = ex.isolate_monotone_root(
            target, Q(stored["lo"]), Q(stored["hi"]), ROOT_WIDTH
        )
        assert ex.qs(root["lo"]) == stored["lo"]
        assert ex.qs(root["hi"]) == stored["hi"]
        assert ex.qs(root["value_lo"]) == stored["value_lo"]
        assert ex.qs(root["value_hi"]) == stored["value_hi"]
        assert root["derivative_sign"] == stored["derivative_sign"]
        roots.append(root)
        audits.append(event_audit(
            pre_rows, event_name, target_name, family, root, target
        ))
    assert all(a["hi"] < b["lo"] for a, b in zip(roots, roots[1:]))

    next_stored = frozen["path"]["next_forbidden_event"]
    next_target = lookup[next_stored["name"]]
    assert next_target.exact() == next_stored["polynomial_exact"]
    next_root = ex.isolate_monotone_root(
        next_target, Q(next_stored["lo"]), Q(next_stored["hi"]), ROOT_WIDTH
    )
    end = Q(frozen["path"]["far_parameter"])
    assert roots[-1]["hi"] < end < next_root["lo"]

    intervals = []
    bounds = [(Q(0), roots[0]["lo"])]
    bounds.extend((a["hi"], b["lo"]) for a, b in zip(roots, roots[1:]))
    for index, (lo, hi) in enumerate(bounds):
        intervals.append({
            "name": f"pre_open_cell_{index}",
            "exhaustive": strict_interval(pre_rows, lo, hi),
            "class_cover": ex.certify_path_segment(
                restrict(path, lo, hi), pre_faces, PROTECTED
            ),
        })
    for index, root in enumerate(roots[:3]):
        cover = ex.certify_mechanics_interval(
            path, pre_faces, PROTECTED, root["lo"], root["hi"]
        )
        assert cover["midpoint_class"]["class"] == [2, 2, 2]
        audits[index]["class_cover"] = cover

    first_support = ex.certify_first_support_wall(
        path, pre_faces, roots[-1], lookup["support:f84:w229"]
    )
    assert {
        (tuple(sorted(pre_faces[row["face_index"]])), row["witness"])
        for row in first_support["target_support_family"]
    } == {
        (tuple(sorted((228, 231, 230))), 229),
        (tuple(sorted((228, 230, 229))), 231),
    }
    wall_cover = ex.certify_mechanics_interval(
        path, wall_faces, PROTECTED, roots[-1]["lo"], roots[-1]["hi"]
    )
    assert wall_cover["midpoint_class"]["class"] == [2, 2, 2]
    audits[-1]["first_support_wall"] = first_support
    audits[-1]["wall_class_cover"] = wall_cover
    intervals.append({
        "name": "post_flip_open_cell",
        "exhaustive": strict_interval(post_rows, roots[-1]["hi"], end),
        "class_cover": ex.certify_path_segment(
            restrict(path, roots[-1]["hi"], end), post_faces, PROTECTED
        ),
    })
    assert audits == frozen["event_audits"]
    assert intervals == frozen["open_intervals"]

    pre_edges, wall_edges, post_edges = map(edges, (pre_faces, wall_faces, post_faces))
    assert pre_edges - post_edges == {(228, 230)}
    assert post_edges - pre_edges == {(229, 231)}
    assert [61, len(wall_edges), len(wall_faces)] == [61, 161, 102]
    for faces, edge_rows in (
        (pre_faces, pre_edges), (wall_faces, wall_edges), (post_faces, post_edges)
    ):
        assert BASE in {frozenset(face) for face in faces}
        assert rails().issubset(edge_rows)
    assert frozen["topology_event"] == {
        "pre_f_vector": [61, 162, 103],
        "wall_f_vector": [61, 161, 102],
        "post_f_vector": [61, 162, 103],
        "target_circuit": [228, 229, 230, 231],
        "removed_maximal_faces": [[228, 231, 230], [228, 230, 229]],
        "wall_maximal_face": [228, 231, 230, 229],
        "added_maximal_faces": [[228, 231, 229], [229, 231, 230]],
        "removed_true_edge": [228, 230],
        "added_true_edge": [229, 231],
        "base_preserved": True,
        "active_rows_preserved": 61,
        "forced_rails_preserved": 37,
    }

    parameters = {
        name: Q(value) for name, value in frozen["rational_parameters"].items()
    }
    faces_for = {
        "source": pre_faces, "pre": pre_faces,
        "post": post_faces, "far": post_faces,
    }
    files_for = {
        "pre": GENERATED["pre"], "post": GENERATED["post"], "far": GENERATED["far"]
    }
    for name, parameter in parameters.items():
        points = evaluate_path(path, parameter)
        assert exact_checkpoint(points, faces_for[name]) == frozen["rational_checkpoints"][name]
        if name in files_for:
            assert ex.read_rows(files_for[name]) == points
    assert json.loads(GENERATED["wall_faces"].read_text()) == wall_faces
    assert json.loads(GENERATED["post_faces"].read_text()) == post_faces
    for file in GENERATED.values():
        key = str(file.relative_to(ROOT))
        assert sha256(file) == frozen["generated_file_sha256"][key]

    residuals = frozen_verify.direction_audit(
        path, pre_faces, post_faces, roots[-1], end
    )
    assert residuals == frozen["directed_residuals"]
    assert all(
        row["piecewise_derivative"][segment]["derivative_sign"] == -1
        for row in residuals.values() for segment in ("pre", "post")
    )
    assert verify_h910(
        path, pre_faces, wall_faces, post_faces, roots[-1], end
    ) == frozen["h910_nonresurrection"]
    assert frozen["residual_verdict"]["winner"] is False
    assert frozen["residual_verdict"]["far_class"] == [2, 2, 2]
    print("INDEPENDENT_EXACT_FULL_CONTROL_THREE_TRANSFER_SAFE_FLIP_CHAIN_PASS")


if __name__ == "__main__":
    main()
