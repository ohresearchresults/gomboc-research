#!/usr/bin/env python3
"""Fresh 165D rechart and exact first-jet map after accepted transfer 1."""
from __future__ import annotations

import hashlib
import json
from fractions import Fraction as Q
from pathlib import Path

import front_common as fc


ALIASES = {"edge:(9, 10):one_minus_t", "vertex:10:9"}
EXPECTED_SOURCE = {
    "class": [2, 3, 3],
    "stable_faces": fc.rc.FAR_FEATURES["stable_faces"],
    "unstable_vertices": [1, 8, 54],
    "saddle_edges": [[1, 54], [5, 6], [10, 11]],
}


def h910_polynomial(path, faces):
    d6, centered = fc.rc.ex.scaled_centered(path, faces)
    edge = fc.rc.ex.edge_components(
        path, faces, centered, fc.rc.ex.edge_data(faces)[0], (9, 10)
    )
    value = 4 * d6 * edge["direction_norm2"] - edge["t"]
    vertex = fc.rc.ex.vertex_component(path, centered, 10, 9)
    if value != vertex:
        raise AssertionError("H910/U10 alias identity")
    return value


def main():
    transfer1 = fc.HERE / "transfer1_far.csv"
    certificate_path = fc.HERE / "transfer1_certificate.json"
    verification_path = fc.HERE / "transfer1_verification.json"
    certificate = json.loads(certificate_path.read_text())
    verification = json.loads(verification_path.read_text())
    if certificate.get("verdict") != "EXACT_ORDERED_TRANSFER1_D_EPOCH_PASS":
        raise AssertionError("transfer1 primary")
    if verification.get("verdict") != "INDEPENDENT_CLEAN_ROOM_EXACT_ORDERED_TRANSFER1_D_VERIFICATION_PASS":
        raise AssertionError("transfer1 independent")
    if fc.sha256(transfer1) != certificate["generated_file_sha256"][fc.rc.relative(transfer1)]:
        raise AssertionError("transfer1 FAR binding")
    source = fc.rc.ex.read_rows(transfer1)
    faces = json.loads(fc.FACES.read_text())
    source_checkpoint = fc.rc.exact_checkpoint(source, faces, EXPECTED_SOURCE)
    labels, _float_modes, mode_names, exact_modes, plane_normal = fc.exact_modes(source)
    zero = {label: (Q(0), Q(0), Q(0)) for label in source}
    source_target = h910_polynomial(fc.affine_path(source, zero), faces).eval(Q(0))
    if source_target >= 0:
        raise AssertionError(("H910 source sign", fc.rc.ex.qs(source_target)))
    gradient = []
    for mode in exact_modes:
        polynomial = h910_polynomial(fc.affine_path(source, mode), faces)
        if polynomial.eval(Q(0)) != source_target:
            raise AssertionError("target source drift")
        gradient.append(polynomial.c[1] if polynomial.degree else Q(0))
    active_gradient = [index for index, value in enumerate(gradient) if value]
    if not active_gradient:
        raise AssertionError("H910 is not first-jet reachable")

    original = fc.rc.ex.read_rows(fc.SOURCE)
    continuation_velocity = {
        label: tuple((source[label][axis] - original[label][axis]) / Q(1, 100) for axis in range(3))
        for label in source
    }
    target_path = h910_polynomial(fc.affine_path(source, continuation_velocity), faces)
    derivative = target_path.c[1]
    if derivative <= 0:
        raise AssertionError(("continuation H910 derivative", fc.rc.ex.qs(derivative)))
    linear_root = -source_target / derivative
    rows = fc.primitive_first_jets(source, continuation_velocity, faces)
    events = []
    for name, value, row_derivative, family in rows:
        if not value:
            raise AssertionError(("zero transfer1 FAR primitive", name))
        if row_derivative and value * row_derivative < 0:
            root = -value / row_derivative
            if root > 0:
                events.append({"name": name, "family": family,
                               "root": fc.rc.ex.qs(root), "decimal": float(root)})
    events.sort(key=lambda row: (Q(row["root"]), row["name"]))
    first_root = Q(events[0]["root"])
    first_family = [row for row in events if Q(row["root"]) == first_root]
    if {row["name"] for row in first_family} != ALIASES:
        raise AssertionError(("fresh first-jet family", first_family))
    if first_root != linear_root:
        raise AssertionError("target/ledger linear root drift")
    coefficient_digest = hashlib.sha256(
        "\n".join(f"{repr(name)}|{fc.rc.ex.qs(value)}" for name, value in zip(mode_names, gradient)).encode()
    ).hexdigest()
    payload = {
        "version": 1,
        "source_hashes": {
            **fc.bindings(), fc.rc.relative(transfer1): fc.sha256(transfer1),
            fc.rc.relative(certificate_path): fc.sha256(certificate_path),
            fc.rc.relative(verification_path): fc.sha256(verification_path),
            fc.rc.relative(fc.HERE / "front_common.py"): fc.sha256(fc.HERE / "front_common.py"),
            fc.rc.relative(Path(__file__)): fc.sha256(Path(__file__)),
        },
        "source_checkpoint": source_checkpoint,
        "fresh_chart": {"mode_count": len(exact_modes), "base_plane_normal": plane_normal.tolist(),
                        "target_rank": 1, "active_target_gradient_modes": len(active_gradient),
                        "target_gradient_digest": coefficient_digest},
        "target": {"semantic": "H910/U10", "complete_alias_candidate": sorted(ALIASES),
                   "source_value": fc.rc.ex.qs(source_target),
                   "continuation_derivative": fc.rc.ex.qs(derivative),
                   "linearized_local_root": fc.rc.ex.qs(linear_root),
                   "linearized_original_lambda": fc.rc.ex.qs(Q(1, 100) + linear_root)},
        "exact_first_jet_map": {"primitive_count": len(rows), "positive_root_count": len(events),
                                "first_family": first_family, "first_events": events[:40]},
        "verdict": "EXACT_TRANSFER2_FRESH_165D_RECHART_H910_FIRST_JET_PASS",
    }
    (fc.HERE / "transfer2_rechart_audit.json").write_text(json.dumps(payload, indent=2) + "\n")
    print(json.dumps({"verdict": payload["verdict"], "mode_count": len(exact_modes),
                      "target_rank": 1, "first_family": first_family,
                      "original_lambda": payload["target"]["linearized_original_lambda"]}, indent=2))


if __name__ == "__main__":
    main()
