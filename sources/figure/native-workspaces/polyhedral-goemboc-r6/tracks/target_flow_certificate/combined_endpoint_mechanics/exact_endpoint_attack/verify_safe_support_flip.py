#!/usr/bin/env python3
"""Independent reconstruction of one exact rail-preserving support flip."""
from __future__ import annotations

import argparse
import hashlib
import json
import sys
from pathlib import Path


HERE = Path(__file__).resolve().parent
PARENT = HERE.parent
ROOT = HERE.parents[3]
sys.path[:0] = [str(PARENT), str(HERE)]

import build_u54_material_exact_path as source  # noqa: E402
import certify_safe_support_flip as builder  # noqa: E402


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def canonical_hash(value) -> str:
    return hashlib.sha256(
        json.dumps(value, sort_keys=True, separators=(",", ":")).encode()
    ).hexdigest()


def without(record, keys):
    return {key: value for key, value in record.items() if key not in keys}


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--prefix", required=True)
    args = parser.parse_args()
    certificate_file = HERE / f"{args.prefix}_certificate.json"
    certificate = json.loads(certificate_file.read_text())
    if certificate["verdict"] != "EXACT_RAIL_PRESERVING_SUPPORT_FLIP_PASS":
        raise AssertionError("unexpected verdict")
    source_file = ROOT / certificate["source_raw"]
    far_file = ROOT / certificate["far_raw"]
    circuit = tuple(certificate["event"]["circuit"])
    data = builder.reconstruct(source_file, far_file, circuit)

    exact_source = source.ex.read_rows(ROOT / certificate["exact_source"])
    exact_far = source.ex.read_rows(ROOT / certificate["far_cell"]["point_file"])
    if exact_source != data["snapshots"][0] or exact_far != data["snapshots"][1]:
        raise AssertionError("exact checkpoint reconstruction mismatch")
    path_digest = canonical_hash({
        str(label): [coordinate.exact() for coordinate in data["path"][label]]
        for label in sorted(data["path"])
    })
    if certificate["construction"] != {
        "repair": data["repair"],
        "path_digest": path_digest,
    }:
        raise AssertionError("path construction mismatch")
    if certificate["event"] != data["event"]:
        raise AssertionError("event reconstruction mismatch")

    for key, faces_key in (
        ("pre_cell", "pre_faces"),
        ("wall", "wall_faces"),
        ("far_cell", "far_faces"),
    ):
        stored = certificate[key]
        faces = json.loads((ROOT / stored["face_file"]).read_text())
        if faces != data[faces_key] or canonical_hash(faces) != stored["face_hash"]:
            raise AssertionError(("face reconstruction mismatch", key))
    if without(certificate["pre_cell"], {"face_file", "face_hash"}) != data["pre_cell"]:
        raise AssertionError("pre-cell reconstruction mismatch")
    if without(certificate["wall"], {"face_file", "face_hash"}) != data["wall"]:
        raise AssertionError("wall reconstruction mismatch")
    if without(
        certificate["far_cell"], {"point_file", "face_file", "face_hash"}
    ) != data["far_cell"]:
        raise AssertionError("far-cell reconstruction mismatch")
    if certificate["endpoint_material_comparison"] != data["endpoint_material_comparison"]:
        raise AssertionError("material comparison mismatch")
    for relative, expected in certificate["generated_sha256"].items():
        if sha256(ROOT / relative) != expected:
            raise AssertionError(("SHA mismatch", relative))
    print("INDEPENDENT_EXACT_RAIL_PRESERVING_SUPPORT_FLIP_PASS")


if __name__ == "__main__":
    main()
