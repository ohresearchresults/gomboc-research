#!/usr/bin/env python3
"""Clean rerun of the exact shell63 coordinate and mechanics certificate."""

from __future__ import annotations

import csv
import json
from fractions import Fraction as Q

import build_shell63_exact as build


def load_output_rows():
    rows = {}
    with build.ROWS_OUT.open(newline="") as handle:
        for row in csv.DictReader(handle):
            rows[int(row["source_id"])] = tuple(
                Q(row[column]) for column in ("x_exact", "y_exact", "z_exact")
            )
    return rows


def main() -> None:
    source = build.load_rows()
    expected_construction = build.construct(source)
    rows = load_output_rows()
    assert rows == source
    cycles = json.loads(build.FACES_OUT.read_text())
    certificate = json.loads(build.CERT_OUT.read_text())
    assert certificate["construction"] == expected_construction
    audit = build.exact_audit(rows, cycles)
    for key, value in audit.items():
        assert certificate[key] == value, key
    assert audit["f_vector"] == [63, 169, 108]
    assert audit["class"] == [2, 1, 1]
    assert audit["newly_active_source_labels"] == [226, 227]
    assert audit["unstable_vertices"] == [8]
    assert audit["saddle_edges"] == [[228, 229]]
    print("PASS exact rational row-228 construction")
    print("PASS every stored maximal face is exactly supporting and the sphere is closed")
    print("PASS exact volume, own centroid and exhaustive strict class (2,1,1)")


if __name__ == "__main__":
    main()
