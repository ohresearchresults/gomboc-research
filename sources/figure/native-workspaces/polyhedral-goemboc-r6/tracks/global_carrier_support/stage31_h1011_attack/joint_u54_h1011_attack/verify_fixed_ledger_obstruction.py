#!/usr/bin/env python3
"""Exact obstruction for the selected U54-neighbor-1 mechanics death."""
from __future__ import annotations

import argparse
import hashlib
import json
import sys
from pathlib import Path


sys.set_int_max_str_digits(0)

HERE = Path(__file__).resolve().parent
ATTACK = HERE.parent
TRACK = ATTACK.parent
ROOT = HERE.parents[4]
SOURCE = ATTACK / "continuation2_row230_bypass" / "step13_transfer_far.csv"
FACES = ATTACK / "continuation" / "main" / "exact_full_control_chain_post_faces.json"
OUTPUT = HERE / "fixed_ledger_obstruction_receipt.json"

EXPECTED_SOURCE_SHA256 = "81cb9b2b0666b413906f45ec7db69da81750b304940b3f8466778f73a0895552"
EXPECTED_FACES_SHA256 = "c1d74d638df21a0492645aa39e4d3943b8401ed0732393505c838ec2f1c0ed77"
BASE = frozenset(range(17)) | {54}
EDGE = (1, 54)

sys.path.insert(0, str(TRACK / "rigorous_local_bypass"))
import exact_core as ex  # noqa: E402
sys.path.insert(0, str(ATTACK))
import build_exact_circuit_flip as frozen_builder  # noqa: E402


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def canonical_hash(value) -> str:
    return hashlib.sha256(
        json.dumps(value, sort_keys=True, separators=(",", ":")).encode()
    ).hexdigest()


def relative(path: Path) -> str:
    return str(path.resolve().relative_to(ROOT))


def exact_record(value) -> dict:
    text = ex.qs(value)
    return {
        "exact": text,
        "sign": 1 if value > 0 else -1 if value < 0 else 0,
        "decimal": float(value),
        "sha256": hashlib.sha256(text.encode()).hexdigest(),
    }


def atomic_json(path: Path, payload) -> None:
    temporary = path.with_suffix(path.suffix + ".tmp")
    temporary.write_text(json.dumps(payload, indent=2) + "\n")
    temporary.replace(path)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", default=str(OUTPUT))
    args = parser.parse_args()
    output = Path(args.output).resolve()
    if output.parent != HERE:
        raise ValueError("output must stay inside the sidecar directory")

    if sha256(SOURCE) != EXPECTED_SOURCE_SHA256:
        raise AssertionError("source hash drift")
    if sha256(FACES) != EXPECTED_FACES_SHA256:
        raise AssertionError("face-ledger hash drift")
    if frozen_builder.SELECTED_COMPONENTS["U54"] != 1:
        raise AssertionError("authoritative U54 selected component drift")
    if frozen_builder.SELECTED_COMPONENTS["H1011"] != "t":
        raise AssertionError("authoritative H1011 selected component drift")

    points = ex.read_rows(SOURCE)
    faces = json.loads(FACES.read_text())
    support = ex.supporting_cell(points, faces)
    ledger, mechanics = ex.classify_point(points, faces)
    if support["f_vector"] != [61, 162, 103]:
        raise AssertionError(support)
    if mechanics["class"] != [2, 2, 2]:
        raise AssertionError(mechanics)
    if BASE not in {frozenset(face) for face in faces}:
        raise AssertionError("enlarged base is absent")
    if EDGE not in ledger["incidence"]:
        raise AssertionError("base edge (1,54) is absent")
    missing_rails = sorted(frozen_builder.forced_rails() - set(support["edges"]))
    if missing_rails:
        raise AssertionError(("missing forced rails", missing_rails))

    v54_to_1 = ledger["vertex"][54][1]
    v1_to_54 = ledger["vertex"][1][54]
    direction = ex.sub(points[1], points[54])
    edge_length_squared = ex.norm2(direction)
    scale = 4 * ledger["d6"]
    positive_gap = scale * edge_length_squared
    if not v54_to_1 > 0:
        raise AssertionError("U54 witness is not positive at source")
    if not v1_to_54 < 0:
        raise AssertionError("preceding witness is not negative at source")
    if not ledger["d6"] > 0 or not edge_length_squared > 0:
        raise AssertionError("volume or edge degeneracy at source")
    if v54_to_1 + v1_to_54 != positive_gap:
        raise AssertionError("directed vertex identity failed")

    payload = {
        "version": 1,
        "scope": (
            "Exact obstruction to making the authoritative selected U54 "
            "neighbor-1 component the first mechanics death on every continuous "
            "path retaining the fixed positive-volume face ledger and its "
            "nondegenerate base edge (1,54)."
        ),
        "source_hashes": {
            relative(SOURCE): sha256(SOURCE),
            relative(FACES): sha256(FACES),
        },
        "source_checkpoint": {
            "f_vector": support["f_vector"],
            "class": mechanics["class"],
            "active_labels": support["active_labels"],
            "base_face_present": True,
            "base_edge_present": True,
            "forced_rail_count": 37,
            "missing_forced_rails": [],
        },
        "exact_source_witnesses": {
            "vertex:54:1": exact_record(v54_to_1),
            "vertex:1:54": exact_record(v1_to_54),
            "volume_d6": exact_record(ledger["d6"]),
            "edge_1_54_length_squared": exact_record(edge_length_squared),
            "positive_identity_gap": exact_record(positive_gap),
        },
        "identity": {
            "formula": (
                "vertex(54,1)+vertex(1,54)="
                "4*d6*||p1-p54||^2"
            ),
            "exact_equality_verified": True,
            "coordinate_difference_identity_verified": all(
                ledger["xscaled"][1][axis] - ledger["xscaled"][54][axis]
                == scale * direction[axis]
                for axis in range(3)
            ),
        },
        "selected_component_authority": {
            "owner": relative(Path(frozen_builder.__file__)),
            "owner_sha256": sha256(Path(frozen_builder.__file__)),
            "U54": frozen_builder.SELECTED_COMPONENTS["U54"],
            "H1011": frozen_builder.SELECTED_COMPONENTS["H1011"],
        },
        "continuity_argument": [
            "vertex:1:54 is strictly negative at the exact source",
            "at the retained-ledger selected U54-neighbor-1 wall vertex:54:1=0",
            "the identity then makes vertex:1:54 strictly positive",
            "the intermediate value theorem forces vertex:1:54=0 strictly before that selected wall",
        ],
        "consequence": (
            "A path with no earlier mechanics zero cannot drive the authoritative "
            "selected U54 neighbor-1 component to zero, hence cannot realize the "
            "requested selected U54-neighbor-1/H1011-t first event."
        ),
        "proof_owner": {
            "verifier_script": relative(Path(__file__)),
            "verifier_script_sha256": sha256(Path(__file__)),
            "exact_core_sha256": sha256(Path(ex.__file__)),
            "witness_digest": canonical_hash({
                "v54_to_1": ex.qs(v54_to_1),
                "v1_to_54": ex.qs(v1_to_54),
                "positive_gap": ex.qs(positive_gap),
            }),
        },
        "verdict": (
            "EXACT_FIXED_LEDGER_SELECTED_U54_NEIGHBOR1_"
            "PRECEDING_ZERO_OBSTRUCTION_PASS"
        ),
    }
    atomic_json(output, payload)
    print(json.dumps({
        "verdict": payload["verdict"],
        "source_signs": {
            "vertex:54:1": 1,
            "vertex:1:54": -1,
        },
        "identity_gap_decimal": float(positive_gap),
        "output": str(output),
    }, indent=2))


if __name__ == "__main__":
    main()
