#!/usr/bin/env python3
"""Portable independent completion of the frozen post-C17 verifier.

The frozen parent verifier is mathematically sound but monolithic: on this
host its non-TTY process is terminated before the terminal marker.  This file
does not call the certificate producer and does not change any frozen hash.
It executes the same independent reconstruction in isolated exact blocks,
parallelizes the expensive blocks, and emits one terminal marker only after
every block and the original manifest have passed.
"""
from __future__ import annotations

import hashlib
import json
import sys
from concurrent.futures import ProcessPoolExecutor, as_completed
from fractions import Fraction as Q
from pathlib import Path


HERE = Path(__file__).resolve().parent
ATTACK = HERE.parent
OUTPUT = HERE / "frozen_checkpoint_verification.json"
sys.path.insert(0, str(ATTACK))

import post_c17_exact as pc  # noqa: E402
import verify_certificate as frozen  # noqa: E402


EXPECTED_CERTIFICATE_SHA256 = "79cba938ff1eeca5a4290dfa6d0ca40aa85f11adca99411b60a7469675d395cb"
EXPECTED_FROZEN_VERIFIER_SHA256 = "161c27e6a74cb57f3aab79ef423fa009d56f1d5cd1968f97f13afade1d764718"


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def inputs():
    certificate = json.loads(frozen.DATA.read_text())
    rows0 = pc.read_rows(ATTACK / certificate["source"]["local_copy"])
    return certificate, rows0


def rebuild(name, parameter, certificate, rows0):
    return frozen.compare_cell(
        name,
        parameter,
        certificate["fresh_exact_cells"][name],
        rows0,
    )


def task_cells():
    certificate, rows0 = inputs()
    specs = (
        ("source", Q(0)),
        ("mechanics_pre", pc.MECH_LEFT),
        ("mechanics_far", pc.MECH_RIGHT),
        ("support_pre", pc.SUPPORT_PRE_SAMPLE),
        ("support_far", pc.SUPPORT_FAR_SAMPLE),
        ("endpoint", pc.END),
    )
    records = {}
    for name, parameter in specs:
        packet, rows, faces = rebuild(name, parameter, certificate, rows0)
        assert len(rows) == 119
        assert packet["all_61_active"] and packet["all_37_forced_rails_present"]
        records[name] = {
            "f_vector": packet["f_vector"],
            "class": packet["class"],
            "face_count": len(faces),
            "row_count": len(rows),
        }
    assert records["source"]["class"] == [2, 5, 5]
    assert records["mechanics_pre"]["class"] == [2, 5, 5]
    assert all(
        records[name]["class"] == [2, 4, 4]
        for name in ("mechanics_far", "support_pre", "support_far", "endpoint")
    )
    return {"task": "cells", "records": records}


def task_exhaustive(name, parameter):
    certificate, rows0 = inputs()
    packet, rows, faces = rebuild(name, parameter, certificate, rows0)
    audit = frozen.exhaustive_supporting_planes(rows, faces)
    assert audit["unique_input_points"] == 119
    assert audit["supporting_planes"] == 91
    assert packet["f_vector"] == [61, 150, 91]
    return {"task": f"exhaustive_{name}", "audit": audit}


def task_events():
    certificate, rows0 = inputs()
    source = rebuild("source", Q(0), certificate, rows0)
    support_far = rebuild("support_far", pc.SUPPORT_FAR_SAMPLE, certificate, rows0)
    endpoint = rebuild("endpoint", pc.END, certificate, rows0)
    linked = pc.linked_mechanics_event(rows0, source[2])
    support = pc.support_root_atlas(rows0, source[2])
    assert linked == {
        key: certificate["ordered_events"][0][key]
        for key in linked
    }
    assert support == {
        key: certificate["ordered_events"][1][key]
        for key in support
    }
    far_segment = pc.cont.affine_support_segment_audit(
        support_far[1], endpoint[1], support_far[2]
    )
    assert far_segment == certificate["far_support_segment_certificate"]
    return {
        "task": "events",
        "linked_degree": linked["common_polynomial"]["degree"],
        "support_degree": support["event_polynomial"]["degree"],
        "strict_support_polynomials_checked": support["strict_support_polynomials_checked"],
    }


def task_old_guards():
    certificate, rows0 = inputs()
    source = rebuild("source", Q(0), certificate, rows0)
    audit = pc.mechanics_guard_audit(
        rows0,
        source[2],
        Q(0),
        pc.SUPPORT_RIGHT,
        special_pair=True,
        reference_parameter=Q(0),
    )
    assert audit == certificate["complete_mechanics_cone_audits"]["old_support_formula"]
    return {"task": "old_guards", "guard_record_count": audit["guard_record_count"]}


def task_far_guards():
    certificate, rows0 = inputs()
    support_far = rebuild("support_far", pc.SUPPORT_FAR_SAMPLE, certificate, rows0)
    audit = pc.mechanics_guard_audit(
        rows0,
        support_far[2],
        pc.SUPPORT_RIGHT,
        pc.END,
        special_pair=False,
        reference_parameter=pc.SUPPORT_FAR_SAMPLE,
    )
    assert audit == certificate["complete_mechanics_cone_audits"]["far_support_formula"]
    return {"task": "far_guards", "guard_record_count": audit["guard_record_count"]}


def task_one_sided_guards():
    certificate, rows0 = inputs()
    support_far = rebuild("support_far", pc.SUPPORT_FAR_SAMPLE, certificate, rows0)
    audit = pc.one_sided_support_bracket_mechanics_audit(
        rows0,
        support_far[2],
        pc.SUPPORT_LEFT,
        pc.SUPPORT_RIGHT,
        pc.SUPPORT_RIGHT,
    )
    assert audit == certificate["complete_mechanics_cone_audits"][
        "far_formula_open_algebraic_right_side"
    ]
    return {
        "task": "one_sided_guards",
        "guard_record_count": audit["guard_record_count"],
        "singular_guard_record_count": audit["singular_guard_record_count"],
    }


def task_tail():
    certificate, rows0 = inputs()
    source = rebuild("source", Q(0), certificate, rows0)
    endpoint = rebuild("endpoint", pc.END, certificate, rows0)
    start_values = pc.exact_named_values(source[1], source[2])
    endpoint_values = pc.exact_named_values(endpoint[1], endpoint[2])
    for name, record in certificate["inherited_eight_endpoint_ratios"].items():
        ratio = endpoint_values[name] / start_values[name]
        assert Q(record["endpoint_over_start_exact"]) == ratio < 1
    assert start_values["U254_via_255"] > 0 > endpoint_values["U254_via_255"]
    assert start_values["H254_255_via_t"] > 0 > endpoint_values["H254_255_via_t"]

    for relative, expected in certificate["artifact_hashes"].items():
        assert sha256(ATTACK / relative) == expected
    manifest = {}
    for line in frozen.MANIFEST.read_text().splitlines():
        digest, relative = line.split("  ", 1)
        assert relative not in manifest
        manifest[relative] = digest
    assert len(manifest) == 18
    for relative, expected in manifest.items():
        assert sha256(ATTACK / relative) == expected
    return {
        "task": "tail",
        "ratio_count": len(certificate["inherited_eight_endpoint_ratios"]),
        "manifest_entries": len(manifest),
        "endpoint": {"f_vector": endpoint[0]["f_vector"], "class": endpoint[0]["class"]},
    }


def main():
    assert sha256(frozen.DATA) == EXPECTED_CERTIFICATE_SHA256
    assert sha256(ATTACK / "verify_certificate.py") == EXPECTED_FROZEN_VERIFIER_SHA256
    tasks = (
        ("cells", task_cells, ()),
        ("exhaustive_source", task_exhaustive, ("source", Q(0))),
        ("exhaustive_endpoint", task_exhaustive, ("endpoint", pc.END)),
        ("events", task_events, ()),
        ("old_guards", task_old_guards, ()),
        ("far_guards", task_far_guards, ()),
        ("one_sided_guards", task_one_sided_guards, ()),
        ("tail", task_tail, ()),
    )
    records = {}
    with ProcessPoolExecutor(max_workers=4) as executor:
        pending = {
            executor.submit(function, *args): name
            for name, function, args in tasks
        }
        for future in as_completed(pending):
            name = pending[future]
            records[name] = future.result()
            print("BLOCK_PASS", name, flush=True)
    assert set(records) == {name for name, _function, _args in tasks}
    payload = {
        "version": 1,
        "scope": "portable independent completion of frozen post-C17 verifier",
        "frozen_hashes_unchanged": {
            "certificate.json": sha256(frozen.DATA),
            "verify_certificate.py": sha256(ATTACK / "verify_certificate.py"),
            "manifest.sha256": sha256(frozen.MANIFEST),
        },
        "blocks": records,
        "verdict": "INDEPENDENT_EXACT_POST_C17_RECOVERY2_PORTABLE_PASS",
        "winner_status": "NONWINNER",
    }
    OUTPUT.write_text(json.dumps(payload, indent=2) + "\n")
    print(payload["verdict"])
    print("winner_status", payload["winner_status"])
    print("output_sha256", sha256(OUTPUT))


if __name__ == "__main__":
    main()
