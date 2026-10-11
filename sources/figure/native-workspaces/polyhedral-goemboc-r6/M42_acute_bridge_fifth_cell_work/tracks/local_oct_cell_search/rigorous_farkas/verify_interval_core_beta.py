#!/usr/bin/env python3
"""Recompute and verify the directed-interval core beta certificate."""
from __future__ import annotations

import argparse
import json
import sys
from fractions import Fraction as F
from pathlib import Path

import numpy as np


HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import interval_core_beta_certificate as cert  # noqa: E402


def parse_interval(item):
    return cert.Interval(
        F(int(item["lo_numerator"]), int(item["lo_denominator"])),
        F(int(item["hi_numerator"]), int(item["hi_denominator"])),
    )


def contains(outer, inner):
    return outer.lo <= inner.lo and inner.hi <= outer.hi


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--certificate", type=Path,
                    default=HERE / "core_beta_interval.json")
    ap.add_argument("--output", type=Path,
                    default=HERE / "core_beta_interval_audit.json")
    args = ap.parse_args()
    stored = json.load(args.certificate.open())

    features = cert.interval_features()
    epsilon = F(1, 1_000_000)
    names, a, b, scales = [], [], [], []
    for index, (name, item) in enumerate(features):
        raw_a = [-x for x in item.grad]
        raw_b = item.value - (epsilon if index == 0 else F(0))
        magnitude = max([raw_b.max_abs(), *(x.max_abs() for x in raw_a)])
        scale = F(1, 1) / magnitude
        names.append(name); a.append([x * scale for x in raw_a])
        b.append(raw_b * scale); scales.append(scale)

    support_names = [item["name"] for item in stored["support"]]
    support = [names.index(name) for name in support_names]
    sub_a, sub_b = [a[row] for row in support], [b[row] for row in support]
    matrix = [[sub_a[col][row] for col in range(len(support))]
              for row in range(cert.DIM)]
    matrix.append([cert.Interval.point(1) for _ in support])
    rhs = [F(0)] * cert.DIM + [F(1)]
    midpoint = np.asarray([[float(x.midpoint()) for x in row] for row in matrix])
    center = np.linalg.solve(midpoint, np.asarray([float(x) for x in rhs]))
    inclusion, y_box, image = cert.krawczyk(matrix, rhs, center)
    b_dot_y = sum((value * weight for value, weight in zip(sub_b, y_box)),
                  cert.Interval.point(0))

    serialized_contains_rebuild = True
    for item, row, value, weight, delta in zip(
            stored["support"], support, sub_b, y_box, image):
        serialized_contains_rebuild &= F(item["scale"]) == scales[row]
        serialized_contains_rebuild &= all(
            contains(parse_interval(saved), rebuilt)
            for saved, rebuilt in zip(item["A_intervals"], a[row])
        )
        serialized_contains_rebuild &= contains(parse_interval(item["b_interval"]), value)
        serialized_contains_rebuild &= contains(parse_interval(item["y_interval"]), weight)
        serialized_contains_rebuild &= contains(
            parse_interval(item["krawczyk_delta_image"]), delta
        )

    checks = {
        "source_hashes_match": stored["source_hashes"] == {
            cert.base.SOURCE.name: cert.base.row54_exact.sha256(cert.base.SOURCE),
            cert.base.FACES_SOURCE.name: cert.base.row54_exact.sha256(cert.base.FACES_SOURCE),
        },
        "feature_count_163": len(features) == 163,
        "support_size_19": len(support) == 19,
        "support_names_unique": len(set(support_names)) == len(support_names),
        "serialized_intervals_contain_rebuild": serialized_contains_rebuild,
        "krawczyk_strict_inclusion": inclusion,
        "dual_box_strictly_positive": all(weight.lo > 0 for weight in y_box),
        "b_dot_y_upper_strictly_negative": b_dot_y.hi < 0,
    }
    assert all(checks.values()), {name: value for name, value in checks.items() if not value}
    out = {
        "status": "PASS",
        "checks": checks,
        "logical_statement": (
            "Krawczyk strict inclusion proves a unique y in the positive box "
            "with A^T*y=0 and sum(y)=1; interval evaluation gives b^T*y<0."
        ),
        "b_dot_y": cert.interval_json(b_dot_y),
        "support_names": support_names,
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    with args.output.open("w") as f:
        json.dump(out, f, indent=2)
    print(json.dumps(out, indent=2))


if __name__ == "__main__":
    main()
