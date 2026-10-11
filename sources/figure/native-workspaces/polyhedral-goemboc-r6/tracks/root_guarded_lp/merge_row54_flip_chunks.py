#!/usr/bin/env python3
"""Merge disjoint row54 flip-atlas JSON chunks and verify exact coverage."""

from __future__ import annotations

import argparse
import json
from pathlib import Path


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("output", type=Path)
    parser.add_argument("chunks", nargs="+", type=Path)
    args = parser.parse_args()

    documents = [json.loads(path.read_text()) for path in args.chunks]
    first = documents[0]
    for document in documents[1:]:
        for key in ("version", "scope", "baseline", "bound", "trust", "fd_step",
                    "modes", "local_rows", "primitive_rows", "guard_rows"):
            if document[key] != first[key]:
                raise RuntimeError(f"chunk mismatch at {key}")

    atlas = [record for document in documents for record in document["atlas"]]
    by_index = {record["branch_index"]: record for record in atlas}
    total = first["atlas_total_branches"]
    if len(by_index) != len(atlas):
        raise RuntimeError("duplicate branch indices")
    if set(by_index) != set(range(total)):
        missing = sorted(set(range(total)) - set(by_index))
        raise RuntimeError(f"incomplete atlas; missing {missing}")

    atlas = [by_index[index] for index in range(total)]
    feasible = [record for record in atlas if record["success"]]
    ranked = sorted(feasible, key=lambda record: record["delta"])
    output = dict(first)
    output.update(
        branch_mod=1,
        branch_rem=0,
        atlas=atlas,
        merged_from=[str(path) for path in args.chunks],
        feasible_branches=len(feasible),
        best_branch=None if not ranked else ranked[0],
    )
    args.output.write_text(json.dumps(output, indent=2))
    print("coverage", len(atlas), "feasible", len(feasible))
    if ranked:
        print("best", ranked[0]["branch_index"], ranked[0]["delta"], ranked[0]["deaths"])


if __name__ == "__main__":
    main()
