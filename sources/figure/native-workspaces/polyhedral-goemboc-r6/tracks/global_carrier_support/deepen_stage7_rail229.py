#!/usr/bin/env python3
"""Add one local normal control that robustly exposes rail (229,230).

The stage-7 continuation reaches a numerical Qhull wall while the exact
dyadic determinant of (198,228,229,230) is still positive but only about
1e-19.  Moving label 229 toward the valid side of the affine plane through
(198,228,230) deepens that determinant without changing the fresh hull,
mechanical class, base, or any of the 37 forced rails.
"""

from __future__ import annotations

import argparse
import csv
from fractions import Fraction
import itertools
import json
from pathlib import Path
import sys

import numpy as np


HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
from actual_hull_mechanics import evaluate  # noqa: E402
from search_row54_remote228 import summarize  # noqa: E402


CIRCUIT = (198, 228, 229, 230)
FEATURES = (
    "S(7,8,245)",
    "S(8,245,246)",
    "U54",
    "H(6,7)",
    "H(8,245)",
    "H(9,10)",
)


def parity(permutation):
    inversions = sum(
        permutation[i] > permutation[j]
        for i in range(len(permutation))
        for j in range(i + 1, len(permutation))
    )
    return -1 if inversions % 2 else 1


def exact_determinant(rows):
    result = Fraction(0)
    for permutation in itertools.permutations(range(4)):
        term = Fraction(parity(permutation))
        for row, column in enumerate(permutation):
            term *= (
                Fraction(1)
                if column == 3
                else Fraction.from_float(float(rows[row, column]))
            )
        result += term
    return result


def load_csv(path):
    with path.open(newline="") as handle:
        rows = list(csv.DictReader(handle))
    labels = [int(row["source_id"]) for row in rows]
    points = np.asarray([
        [float(row[axis]) for axis in ("x", "y", "z")]
        for row in rows
    ])
    return labels, points


def write_csv(path, labels, points):
    with path.open("w", newline="") as handle:
        writer = csv.writer(handle)
        writer.writerow(("source_id", "x", "y", "z"))
        for label, point in zip(labels, points):
            writer.writerow([label, *[format(float(x), ".17g") for x in point]])


def feature_values(mechanics):
    return np.asarray([
        mechanics.face_decisions[(7, 8, 245)],
        mechanics.face_decisions[(8, 245, 246)],
        mechanics.vertex_decisions[54],
        mechanics.edge_decisions[(6, 7)],
        mechanics.edge_decisions[(8, 245)],
        mechanics.edge_decisions[(9, 10)],
    ])


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--pre-csv", type=Path, required=True)
    parser.add_argument("--source-audit", type=Path, required=True)
    parser.add_argument("--output-csv", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--displacement", type=float, default=1e-7)
    parser.add_argument("--path-points", type=int, default=21)
    args = parser.parse_args()

    labels, start = load_csv(args.pre_csv)
    index = {label: offset for offset, label in enumerate(labels)}
    source_audit = json.loads(args.source_audit.read_text())
    rails = {
        tuple(sorted(edge))
        for edge in source_audit["fresh_hull_audit"]["forced_rail_edges"]
    }

    a, b, d = [start[index[label]] for label in (198, 228, 230)]
    direction = np.cross(b - a, d - a)
    direction /= np.linalg.norm(direction)

    def determinant(points):
        rows = np.c_[
            points[[index[label] for label in CIRCUIT]],
            np.ones(4),
        ]
        return float(np.linalg.det(rows))

    probe = start.copy()
    probe[index[229]] += 1e-10 * direction
    if determinant(probe) < determinant(start):
        direction *= -1.0

    def sample(alpha):
        points = start.copy()
        points[index[229]] += alpha * args.displacement * direction
        mechanics = evaluate(labels, points)
        record = summarize(labels, points, rails)
        values = feature_values(mechanics)
        return points, mechanics, record, values

    path = []
    reference_signature = None
    reference_values = None
    for alpha in np.linspace(0.0, 1.0, args.path_points):
        points, mechanics, record, values = sample(float(alpha))
        signature = {
            "class": record["class"],
            "f_vector": record["f_vector"],
            "stable_faces": sorted(sorted(face) for face in record["stable_faces"]),
            "unstable_vertices": sorted(record["unstable_vertices"]),
            "saddle_edges": sorted(sorted(edge) for edge in record["saddle_edges"]),
        }
        if reference_signature is None:
            reference_signature = signature
            reference_values = values
        hard = bool(
            record["base_face_present"]
            and not record["missing_forced_rails"]
            and signature == reference_signature
        )
        path.append({
            "alpha": float(alpha),
            "determinant_double": determinant(points),
            "hard_valid": hard,
            "feature_values": dict(zip(FEATURES, values.tolist())),
            "class": record["class"],
            "f_vector": record["f_vector"],
            "base_face_present": record["base_face_present"],
            "missing_forced_rails": record["missing_forced_rails"],
            "centroid": record["centroid"],
        })

    end, mechanics, record, end_values = sample(1.0)
    write_csv(args.output_csv, labels, end)
    start_rows = np.c_[
        start[[index[label] for label in CIRCUIT]], np.ones(4)
    ]
    end_rows = np.c_[
        end[[index[label] for label in CIRCUIT]], np.ones(4)
    ]
    start_exact = exact_determinant(start_rows)
    end_exact = exact_determinant(end_rows)
    passed = bool(
        start_exact > 0
        and end_exact > 0
        and all(row["hard_valid"] for row in path)
        and abs(end_exact) > 1e4 * abs(start_exact)
    )
    assert passed

    payload = {
        "version": 1,
        "scope": "one-control robust deepening of forced rail (229,230)",
        "source": str(args.pre_csv.resolve()),
        "coordinates": str(args.output_csv.resolve()),
        "circuit": list(CIRCUIT),
        "valid_sign": 1,
        "controlled_label": 229,
        "control_direction": direction.tolist(),
        "control_displacement": args.displacement,
        "start_exact_determinant": {
            "numerator": str(start_exact.numerator),
            "denominator": str(start_exact.denominator),
        },
        "end_exact_determinant": {
            "numerator": str(end_exact.numerator),
            "denominator": str(end_exact.denominator),
        },
        "exact_depth_ratio": float(abs(end_exact / start_exact)),
        "start_feature_values": dict(zip(FEATURES, reference_values.tolist())),
        "end_feature_values": dict(zip(FEATURES, end_values.tolist())),
        "end_to_start_ratios": dict(zip(
            FEATURES, (end_values / reference_values).tolist()
        )),
        "fresh_hull_end": {
            "class": record["class"],
            "f_vector": record["f_vector"],
            "active_labels": record["active_labels"],
            "centroid": record["centroid"],
            "stable_faces": record["stable_faces"],
            "unstable_vertices": record["unstable_vertices"],
            "saddle_edges": record["saddle_edges"],
            "base_face_present": record["base_face_present"],
            "missing_forced_rails": record["missing_forced_rails"],
            "min_nonzero_margin": mechanics.min_nonzero_margin,
        },
        "path": path,
        "passed": passed,
    }
    args.output.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n")
    print(json.dumps({
        "passed": passed,
        "exact_depth_ratio": payload["exact_depth_ratio"],
        "control_direction": payload["control_direction"],
        "fresh_hull_end": payload["fresh_hull_end"],
    }, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
