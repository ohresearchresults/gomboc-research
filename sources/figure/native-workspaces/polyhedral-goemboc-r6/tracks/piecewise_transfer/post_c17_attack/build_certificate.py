#!/usr/bin/env python3
"""Build the exact post-C17 mechanics-death and support-flip certificate."""
from __future__ import annotations

import json
from fractions import Fraction as Q
from pathlib import Path

import post_c17_exact as pc

HERE = Path(__file__).resolve().parent
CELLS = HERE / "cells"
OUTPUT = HERE / "certificate.json"
REPORT = HERE / "REPORT.md"
VERIFIER = HERE / "verify_certificate.py"
MANIFEST = HERE / "manifest.sha256"


def main():
    assert pc.sha256(pc.SOURCE) == pc.SOURCE_SHA256
    CELLS.mkdir(parents=True, exist_ok=True)
    rows0 = pc.read_rows()
    source_copy = HERE / "source_endpoint.csv"
    pc.write_rows(source_copy, rows0)
    assert pc.sha256(source_copy) == pc.SOURCE_SHA256

    cell_specs = [
        ("source", Q(0)),
        ("mechanics_pre", pc.MECH_LEFT),
        ("mechanics_far", pc.MECH_RIGHT),
        ("support_pre", pc.SUPPORT_PRE_SAMPLE),
        ("support_far", pc.SUPPORT_FAR_SAMPLE),
        ("endpoint", pc.END),
    ]
    cells = {}
    internals = {}
    for name, parameter in cell_specs:
        record, packet, rows, faces, centroid = pc.write_cell(CELLS, name, parameter, rows0)
        cells[name] = record
        internals[name] = (packet, rows, faces, centroid)

    source_packet, source_rows, source_faces, _ = internals["source"]
    endpoint_packet, endpoint_rows, endpoint_faces, _ = internals["endpoint"]
    assert source_packet["class"] == [2, 5, 5]
    assert internals["mechanics_pre"][0]["class"] == [2, 5, 5]
    assert internals["mechanics_far"][0]["class"] == [2, 4, 4]
    assert internals["support_pre"][0]["class"] == [2, 4, 4]
    assert internals["support_far"][0]["class"] == [2, 4, 4]
    assert endpoint_packet["class"] == [2, 4, 4]

    # The linked U254/H(254,255) death is strictly earlier than the first
    # complete support/in-face event family.
    linked = pc.linked_mechanics_event(rows0, source_faces)
    gradient = pc.direction_gradient_certificate(rows0, source_faces)
    support = pc.support_root_atlas(rows0, source_faces)
    assert pc.MECH_RIGHT < pc.SUPPORT_LEFT

    pre_edges = {tuple(e) for e in internals["support_pre"][0]["true_edges"]}
    far_edges = {tuple(e) for e in internals["support_far"][0]["true_edges"]}
    removed_edges = sorted(pre_edges - far_edges)
    added_edges = sorted(far_edges - pre_edges)
    assert removed_edges == [(255, 257)]
    assert added_edges == [(256, 258)]
    pre_faces = {tuple(sorted(f)) for f in internals["support_pre"][0]["maximal_face_cycles"]}
    far_faces = {tuple(sorted(f)) for f in internals["support_far"][0]["maximal_face_cycles"]}
    assert pre_faces - far_faces == {(255, 256, 257), (255, 257, 258)}
    assert far_faces - pre_faces == {(255, 256, 258), (256, 257, 258)}

    # Complete cone covers.  The old formula extends through the narrow support
    # bracket.  The new diagonal is singular exactly at the algebraic wall, so
    # its ordinary pole-free cover starts at the rational upper bracket.  A
    # separate algebraic-right audit closes the open interval from the unique
    # support root to that rational endpoint without hiding a mechanics zero.
    old_mechanics = pc.mechanics_guard_audit(
        rows0,
        source_faces,
        Q(0),
        pc.SUPPORT_RIGHT,
        special_pair=True,
        reference_parameter=Q(0),
    )
    far_mechanics = pc.mechanics_guard_audit(
        rows0,
        internals["support_far"][2],
        pc.SUPPORT_RIGHT,
        pc.END,
        special_pair=False,
        reference_parameter=pc.SUPPORT_FAR_SAMPLE,
    )
    far_wall_side_mechanics = pc.one_sided_support_bracket_mechanics_audit(
        rows0,
        internals["support_far"][2],
        pc.SUPPORT_LEFT,
        pc.SUPPORT_RIGHT,
        pc.SUPPORT_RIGHT,
    )

    # Exact Bernstein certificate for the strict far support cell after the
    # algebraic wall bracket.
    far_segment = pc.cont.affine_support_segment_audit(
        internals["support_far"][1], endpoint_rows, internals["support_far"][2]
    )

    start_values = pc.exact_named_values(source_rows, source_faces)
    endpoint_values = pc.exact_named_values(endpoint_rows, endpoint_faces)
    inherited = list(start_values)[:8]
    ratios = {}
    for name in inherited:
        assert start_values[name] > 0 and endpoint_values[name] > 0
        ratio = endpoint_values[name] / start_values[name]
        assert Q(0) < ratio < Q(1)
        ratios[name] = {
            "start_exact": pc.qs(start_values[name]),
            "endpoint_exact": pc.qs(endpoint_values[name]),
            "endpoint_over_start_exact": pc.qs(ratio),
            "endpoint_over_start_decimal": float(ratio),
        }
    for name in pc.MECH_CIRCUIT_FEATURES:
        assert start_values[name] > 0 and endpoint_values[name] < 0

    artifact_hashes = {
        str(source_copy.relative_to(HERE)): pc.sha256(source_copy),
    }
    for record in cells.values():
        artifact_hashes[record["csv"]] = record["csv_sha256"]
        artifact_hashes[record["ledger"]] = record["ledger_sha256"]

    out = {
        "version": 1,
        "type": "exact post-C17 linked mechanics death followed by first directed support flip",
        "source": {
            "upstream": str(pc.SOURCE),
            "upstream_sha256": pc.SOURCE_SHA256,
            "local_copy": str(source_copy.relative_to(HERE)),
            "local_copy_sha256": pc.sha256(source_copy),
            "source_f_vector": source_packet["f_vector"],
            "source_class": source_packet["class"],
        },
        "path": {
            "formula": "q_i(u)=q_i(0)+u*d_i, 0<=u<=1",
            "control_rows": sorted({row for row, _, _ in pc.control_spec()}),
            "control_names": [name for _, name, _ in pc.control_spec()],
            "control_basis_exact": [
                {"row": row, "name": name, "basis": [pc.qs(z) for z in basis]}
                for row, name, basis in pc.control_spec()
            ],
            "direction_exact": [pc.qs(z) for z in pc.DIRECTION],
            "shell_tangent_identities_exact": True,
            "base_fixed_exactly": True,
        },
        "exact_direction_gradient": gradient,
        "ordered_events": [
            {
                "order": 1,
                "type": "linked mechanics death",
                **linked,
                "pre_cell": "mechanics_pre",
                "far_cell": "mechanics_far",
            },
            {
                "order": 2,
                "type": "directed support flip",
                "circuit": list(pc.SUPPORT_CIRCUIT),
                "removed_edge": list(removed_edges[0]),
                "added_edge": list(added_edges[0]),
                "removed_faces": [list(z) for z in sorted(pre_faces - far_faces)],
                "added_faces": [list(z) for z in sorted(far_faces - pre_faces)],
                "pre_cell": "support_pre",
                "far_cell": "support_far",
                **support,
            },
        ],
        "event_order_exact": {
            "mechanics_upper": pc.qs(pc.MECH_RIGHT),
            "support_lower": pc.qs(pc.SUPPORT_LEFT),
            "mechanics_strictly_before_support": True,
        },
        "fresh_exact_cells": cells,
        "complete_mechanics_cone_audits": {
            "old_support_formula": old_mechanics,
            "far_support_formula": far_mechanics,
            "far_formula_open_algebraic_right_side": far_wall_side_mechanics,
            "support_bracket_closed_without_hidden_mechanics_zero": True,
        },
        "far_support_segment_certificate": far_segment,
        "inherited_eight_endpoint_ratios": ratios,
        "all_inherited_eight_selected_components_strictly_smaller_at_endpoint": True,
        "endpoint": {
            "f_vector": endpoint_packet["f_vector"],
            "class": endpoint_packet["class"],
            "all_61_active": endpoint_packet["all_61_active"],
            "base_stable": endpoint_packet["base_stable"],
            "U8_unstable": endpoint_packet["U8_unstable"],
            "all_37_forced_rails_present": endpoint_packet[
                "all_37_forced_rails_present"
            ],
            "stable_faces": endpoint_packet["stable_faces"],
            "unstable_vertices": endpoint_packet["unstable_vertices"],
            "saddle_edges": endpoint_packet["saddle_edges"],
        },
        "artifact_hashes": artifact_hashes,
        "verdict": "EXACT_POST_C17_LINKED_U254_H254255_DEATH_AND_FIRST_SUPPORT_FLIP_PASS",
        "winner_status": "NONWINNER",
        "conclusion": (
            "A full-guard rational hard-moment path stays in the actual post-C17 cell "
            "through a unique exact degree-five linked death of U254 and H(254,255), "
            "changing class (2,5,5) to (2,4,4).  It then reaches the first complete "
            "support/in-face event family, the unique quadratic circuit "
            "(255,256,257,258), and crosses its flip without a mechanics birth or loss "
            "of any forced rail.  All inherited eight selected components are smaller "
            "at u=1.  The endpoint is exact and stronger but remains a nonwinner (2,4,4)."
        ),
    }
    OUTPUT.write_text(json.dumps(out, indent=2) + "\n")

    report = f"""# Post-C17 exact linked death and first support flip

## Result

The rational 19-control hard-moment path starts from the immutable exact
post-C17 endpoint and preserves the base plane, shell plane, all 61 active
rows, protected `U8`, and all 37 forced rails.

Its first genuine event is the common degree-five algebraic root of
`U254_via_255` and `H254_255_via_t`, isolated in
`[{pc.qs(pc.MECH_LEFT)}, {pc.qs(pc.MECH_RIGHT)}]`.  The exact class changes
from `(2,5,5)` to `(2,4,4)` with no compensating birth.

The continuation then reaches the first complete support/in-face event family.
Exactly two support rows share the unique quadratic root in
`[{pc.qs(pc.SUPPORT_LEFT)}, {pc.qs(pc.SUPPORT_RIGHT)}]`; the circuit is
`(255,256,257,258)`, removing true edge `(255,257)` and adding `(256,258)`.
The new diagonal has its expected barycentric pole exactly at that algebraic
wall.  A one-sided exact cone cover proves that every selected numerator is
root-free and every selected denominator root is the same unique support
root; hence no hidden mechanics event occurs on entry.  The strict far cell
and the endpoint retain class `(2,4,4)` and all 37 rails.

This is **NONWINNER**.  It is a new exact cell and a certified handoff for the
remaining packet `S[228,264,246], U228, U231, U246, H(8,246), H(228,254),
H(231,247), H(236,237)`.

## Verification

```bash
/usr/local/bin/python3 tracks/piecewise_transfer/post_c17_attack/verify_certificate.py
```

Expected terminal marker:

```text
INDEPENDENT_EXACT_POST_C17_LINKED_DEATH_AND_SUPPORT_FLIP_PASS
```
"""
    REPORT.write_text(report)

    package = [Path(__file__), HERE / "post_c17_exact.py", VERIFIER, OUTPUT, REPORT, source_copy]
    package += sorted(CELLS.glob("*.csv")) + sorted(CELLS.glob("*.json"))
    assert all(path.is_file() for path in package)
    MANIFEST.write_text(
        "".join(f"{pc.sha256(path)}  {path.relative_to(HERE)}\n" for path in package)
    )
    print(out["verdict"])
    print("winner_status", out["winner_status"])
    print("mechanics_bracket", out["ordered_events"][0]["isolating_bracket_exact"])
    print("support_bracket", out["ordered_events"][1]["event_bracket_exact"])
    print("endpoint", endpoint_packet["f_vector"], endpoint_packet["class"])
    print("certificate_sha256", pc.sha256(OUTPUT))
    print("manifest_entries", len(package))


if __name__ == "__main__":
    main()
