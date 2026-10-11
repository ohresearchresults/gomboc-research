#!/usr/bin/env python3
"""Build the primary certificate for the exact (8,245)->(7,246) transfer."""
from __future__ import annotations

import json
from pathlib import Path

import front_common as fc


LOCATOR = fc.HERE / "flip_8245_locator.json"
PRE = fc.HERE / "flip_8245_pre.csv"
POST = fc.HERE / "flip_8245_post.csv"
FAR = fc.HERE / "flip_8245_far.csv"
OUTPUT = fc.HERE / "flip_8245_certificate.json"


def main() -> None:
    fc.validate_lineage()
    locator = json.loads(LOCATOR.read_text())
    if locator.get("schema") != "stable_first_topology_front.flip_8245_locator":
        raise AssertionError("locator schema")
    if locator.get("verdict") != "EXACT_FIRST_8245_STABLE_CARRIER_FLIP_LOCATOR_PASS":
        raise AssertionError("locator verdict")
    event = locator["first_event"]
    if event["owner"] != "circuit:{7,8,245,246}":
        raise AssertionError("event owner")
    expected_zero_family = {
        "support:f15:w246",
        "support:f17:w7",
        "edge:(8, 245):gram",
        "edge:(8, 245):beta1",
        "edge:(8, 245):beta2",
    }
    actual_zero_family = {row["name"] for row in event["complete_zero_family"]}
    if actual_zero_family != expected_zero_family or event["complete_zero_family_count"] != 5:
        raise AssertionError(("zero family", actual_zero_family))
    if event["old_nonfamily_strict_audit"]["strict_polynomial_count"] != 7_917:
        raise AssertionError("old strict count")
    if locator["rechart"]["new_strict_audit"]["strict_polynomial_count"] != 7_922:
        raise AssertionError("new strict count")
    expected_topology = {
        "faces_removed": [[7, 8, 245], [8, 245, 246]],
        "faces_added": [[7, 8, 246], [7, 245, 246]],
        "edges_removed": [[8, 245]],
        "edges_added": [[7, 246]],
    }
    if locator["rechart"]["topology_transfer"] != expected_topology:
        raise AssertionError("topology transfer")
    for name, expected_features in (
        ("pre", fc.SOURCE_FEATURES),
        ("post", fc.POST_FEATURES),
        ("far", fc.POST_FEATURES),
    ):
        checkpoint = locator["checkpoints"][name]
        if checkpoint["exact"]["mechanics"] != expected_features:
            raise AssertionError((name, "mechanics"))
        if checkpoint["exact"]["forced_rail_count"] != 37:
            raise AssertionError((name, "rails"))
        if checkpoint["exact"]["h910_negative_value"].startswith("-") is False:
            raise AssertionError((name, "H910"))
        if any(value.startswith("-") or value == "0" for value in checkpoint["exact"]["row230_squared_margins"].values()):
            raise AssertionError((name, "row230"))
    for path, name in ((PRE, "pre"), (POST, "post"), (FAR, "far")):
        if fc.sha256(path) != locator["checkpoints"][name]["sha256"]:
            raise AssertionError((name, "CSV hash"))

    payload = {
        "schema": "stable_first_topology_front.flip_8245_certificate",
        "schema_version": 1,
        "report_type": "primary_exact_stable_carrier_transfer_certificate",
        "scope": (
            "Primary exact certificate for one ordered topology epoch only: the first "
            "{7,8,245,246} circuit wall and the rational post-rechart interval through t=13/5000."
        ),
        "source_hashes": fc.bindings((
            fc.HERE / "front_common.py",
            fc.HERE / "locate_flip_8245.py",
            LOCATOR,
            PRE,
            POST,
            FAR,
            Path(__file__).resolve(),
        )),
        "input_epoch": {
            "source": fc.relative(fc.SOURCE),
            "source_sha256": fc.sha256(fc.SOURCE),
            "class": [2, 2, 2],
            "stable_faces": fc.SOURCE_FEATURES["stable_faces"],
            "saddles": fc.SOURCE_FEATURES["saddle_edges"],
        },
        "exact_locator": {
            "file": LOCATOR.name,
            "sha256": fc.sha256(LOCATOR),
            "owner": event["owner"],
            "root": event["root"],
            "complete_zero_family": event["complete_zero_family"],
            "old_nonfamily_strict_audit": event["old_nonfamily_strict_audit"],
            "old_complete_primitive_digest": event["old_complete_primitive_digest"],
        },
        "stable_carrier_transfer": {
            "before_stable_face": [7, 8, 245],
            "after_stable_face": [7, 8, 246],
            "topology": expected_topology,
            "class_before": [2, 2, 2],
            "class_after": [2, 2, 2],
            "critical_point_count_change": [0, 0, 0],
            "interpretation": (
                "The extra stable equilibrium is transferred across the circuit; it is not "
                "annihilated. This creates the recharted adjacency for the next stable-first epoch."
            ),
        },
        "post_rechart_exact_interval": {
            "face_hash": locator["rechart"]["post_face_hash"],
            "complete_primitive_digest": locator["rechart"]["new_complete_primitive_digest"],
            "strict_audit": locator["rechart"]["new_strict_audit"],
        },
        "checkpoints": locator["checkpoints"],
        "preserved_invariants": {
            "active_row_count": 61,
            "f_vector": [61, 162, 103],
            "euler": 2,
            "forced_rail_count": 37,
            "row230_strict": True,
            "h910_strictly_dead": True,
            "enlarged_base_stable": True,
            "unstable_vertices": [1, 8],
            "saddles": [[5, 6], [10, 11]],
        },
        "next_boundary": {
            "excluded_from_this_epoch": "circuit:{8,9,263,264}",
            "rejected_probe_t": "3/1000",
            "reason": "fresh diagonal changes (8,263)->(9,264) before t=3/1000",
            "accepted_far_t": "13/5000",
            "claim": "ordered boundary only; no global obstruction",
        },
        "verdict": "EXACT_STABLE_CARRIER_8245_TRANSFER_CERTIFICATE_PASS",
    }
    fc.atomic_write(OUTPUT, (json.dumps(payload, indent=2) + "\n").encode())
    print(json.dumps({
        "verdict": payload["verdict"],
        "certificate": OUTPUT.name,
        "sha256": fc.sha256(OUTPUT),
        "stable_transfer": [[7, 8, 245], [7, 8, 246]],
    }, indent=2))


if __name__ == "__main__":
    main()
