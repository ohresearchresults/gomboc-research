#!/usr/bin/env python3
"""Deepen the two roundoff-limited protected circuits after stage 13.

Stage 13 has a feasible keep-decreasing tangent, but its line search is
limited by raw determinants near 1e-15--1e-14.  Add independent outward-normal
controls at labels 230 and 251, choose the smallest common displacement that
deepens both protected valid sides by at least four orders of magnitude, and
fresh-audit the entire segment without allowing any hull-topology or mechanics
change.  The JSON is also an adaptive_birth_bypass-compatible chart endpoint.
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
ROOT = HERE.parents[1]
sys.path.insert(0, str(HERE))
from actual_hull_mechanics import evaluate  # noqa: E402
from optimize_base_escape import Search  # noqa: E402
from search_row54_remote228 import load_points, summarize  # noqa: E402


CIRCUITS = (
    ((228, 229, 230, 231), -1, 230),
    ((224, 228, 251, 252), -1, 251),
)
KEEP = (
    ("S(7,8,245)", "face", (7, 8, 245)),
    ("U54", "vertex", 54),
    ("H(6,7)", "edge", (6, 7)),
    ("H(9,10)", "edge", (9, 10)),
)
BIRTHS = (
    ("S(8,245,246)", "face", (8, 245, 246)),
    ("H(8,245)", "edge", (8, 245)),
    ("S(9,10,263)", "face", (9, 10, 263)),
    ("H(9,263)", "edge", (9, 263)),
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
            term *= Fraction(1) if column == 3 else Fraction.from_float(float(rows[row, column]))
        result += term
    return result


def write_csv(path, labels, points):
    with path.open("w", newline="") as handle:
        writer = csv.writer(handle)
        writer.writerow(("source_id", "x", "y", "z"))
        for label, point in zip(labels, points):
            writer.writerow([label, *[format(float(x), ".17g") for x in point]])


def decision(mechanics, kind, key):
    if kind == "face":
        return mechanics.face_decisions[key]
    if kind == "vertex":
        return mechanics.vertex_decisions[key]
    return mechanics.edge_decisions[key]


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--source", type=Path,
        default=ROOT / "tracks/circuit_atlas/row54_far_rebuilt.csv",
    )
    parser.add_argument(
        "--source-audit", type=Path,
        default=ROOT / "tracks/circuit_atlas/row54_far_rebuilt_audit.json",
    )
    parser.add_argument("--birth-atlas", type=Path, default=HERE / "local_birth_atlas.json")
    parser.add_argument("--adaptive", type=Path, default=HERE / "adaptive_stage13_dual_birth_guards.json")
    parser.add_argument("--output", type=Path, default=HERE / "stage13_narrow_circuits_deepened.json")
    parser.add_argument("--output-csv", type=Path, default=HERE / "stage13_narrow_circuits_deepened.csv")
    parser.add_argument("--minimum-depth-ratio", type=float, default=1e4)
    parser.add_argument(
        "--displacements", type=float, nargs=2,
        metavar=("LABEL230", "LABEL251"),
        help="explicit independent displacements; otherwise scan a common value",
    )
    parser.add_argument("--path-points", type=int, default=41)
    args = parser.parse_args()

    labels, source = load_points(args.source)
    index = {label: offset for offset, label in enumerate(labels)}
    audit = json.loads(args.source_audit.read_text())
    rails = {tuple(sorted(edge)) for edge in audit["fresh_hull_audit"]["forced_rail_edges"]}
    search = Search(labels, source, rails, report=False)
    atlas = json.loads(args.birth_atlas.read_text())
    adaptive = json.loads(args.adaptive.read_text())
    remote_basis = np.asarray([atlas["remote_basis"]["tangent"], atlas["remote_basis"]["normal"]])
    old_controls = [
        (int(row["label"]), np.asarray(row["direction"], dtype=float), float(row["initial"]))
        for row in adaptive["local_controls"]
    ]
    start_parameters = np.asarray(adaptive["trace"][-1]["parameters"], dtype=float)
    assert len(start_parameters) == 22 + len(old_controls)

    def base_coordinates(parameters):
        points = search.coordinates(parameters[:20])
        points[index[228]] += parameters[20] * remote_basis[0] + parameters[21] * remote_basis[1]
        for offset, (label, direction, _) in enumerate(old_controls):
            points[index[label]] += parameters[22 + offset] * direction
        return points

    start = base_coordinates(start_parameters)

    def determinant(points, circuit):
        rows = np.c_[points[[index[label] for label in circuit]], np.ones(4)]
        return float(np.linalg.det(rows))

    directions = []
    for circuit, sign, controlled in CIRCUITS:
        others = [label for label in circuit if label != controlled]
        a, b, c = (start[index[label]] for label in others)
        direction = np.cross(b - a, c - a)
        direction /= np.linalg.norm(direction)
        probe = start.copy()
        probe[index[controlled]] += 1e-9 * direction
        if sign * determinant(probe, circuit) < sign * determinant(start, circuit):
            direction *= -1.0
        directions.append(direction)

    all_specs = [(tuple(row["circuit"]), int(row["valid_sign"])) for row in adaptive["circuit_guards"]]
    reference_mechanics = evaluate(labels, start)
    reference_record = summarize(labels, start, rails)
    reference_topology = (
        frozenset(reference_mechanics.face_decisions),
        frozenset(reference_mechanics.edge_decisions),
    )

    def sample(displacements):
        displacements = np.broadcast_to(
            np.asarray(displacements, dtype=float), (len(CIRCUITS),)
        )
        points = start.copy()
        for displacement, direction, (_, _, controlled) in zip(
            displacements, directions, CIRCUITS
        ):
            points[index[controlled]] += displacement * direction
        mechanics = evaluate(labels, points)
        record = summarize(labels, points, rails)
        topology = (frozenset(mechanics.face_decisions), frozenset(mechanics.edge_decisions))
        signed_circuits = {
            str(list(circuit)): sign * determinant(points, circuit)
            for circuit, sign in all_specs
        }
        keep_values = {name: decision(mechanics, kind, key) for name, kind, key in KEEP}
        birth_values = {name: decision(mechanics, kind, key) for name, kind, key in BIRTHS}
        hard = bool(
            record["base_face_present"]
            and not record["missing_forced_rails"]
            and len(record["active_labels"]) == 61
            and topology == reference_topology
            and record["class"] == [2, 2, 2]
            and 8 in record["unstable_vertices"]
            and all(value > 0 for value in signed_circuits.values())
            and all(value < 0 for value in birth_values.values())
        )
        return points, mechanics, record, signed_circuits, keep_values, birth_values, hard

    start_exact = {}
    for circuit, sign, _ in CIRCUITS:
        rows = np.c_[start[[index[label] for label in circuit]], np.ones(4)]
        start_exact[str(list(circuit))] = sign * exact_determinant(rows)
        assert start_exact[str(list(circuit))] > 0

    chosen = None
    scan = []
    candidate_displacements = (
        [np.asarray(args.displacements, dtype=float)]
        if args.displacements is not None
        else [
            np.full(len(CIRCUITS), value)
            for value in np.geomspace(1e-9, 1e-2, 57)
        ]
    )
    for displacement in candidate_displacements:
        try:
            points, mechanics, record, signed, keeps, births, hard = sample(displacement)
        except Exception as error:
            scan.append({"displacements": displacement.tolist(), "error": repr(error), "hard_valid": False})
            continue
        ratios = {}
        for circuit, sign, _ in CIRCUITS:
            rows = np.c_[points[[index[label] for label in circuit]], np.ones(4)]
            end_exact = sign * exact_determinant(rows)
            ratios[str(list(circuit))] = float(end_exact / start_exact[str(list(circuit))])
        row = {
            "displacements": displacement.tolist(),
            "hard_valid": hard,
            "depth_ratios": ratios,
            "minimum_signed_circuit": min(signed.values()),
            "keep_values": keeps,
            "birth_values": births,
        }
        scan.append(row)
        if hard and min(ratios.values()) >= args.minimum_depth_ratio:
            chosen = displacement.copy()
            break
    if chosen is None:
        raise ValueError("no topology-preserving four-order circuit deepening found")

    path = []
    for alpha in np.linspace(0.0, 1.0, args.path_points):
        displacement = float(alpha) * chosen
        points, mechanics, record, signed, keeps, births, hard = sample(displacement)
        assert hard
        path.append({
            "alpha": float(alpha),
            "displacements": displacement.tolist(),
            "hard_valid": hard,
            "class": record["class"],
            "f_vector": record["f_vector"],
            "active_label_count": len(record["active_labels"]),
            "base_face_present": record["base_face_present"],
            "missing_forced_rails": record["missing_forced_rails"],
            "signed_circuit_determinants": signed,
            "keep_values": keeps,
            "birth_values": births,
        })

    end, mechanics, record, signed, end_keeps, end_births, hard = sample(chosen)
    write_csv(args.output_csv, labels, end)
    end_exact = {}
    depth_ratios = {}
    for circuit, sign, _ in CIRCUITS:
        key = str(list(circuit))
        rows = np.c_[end[[index[label] for label in circuit]], np.ones(4)]
        end_exact[key] = sign * exact_determinant(rows)
        depth_ratios[key] = float(end_exact[key] / start_exact[key])
    assert hard and min(depth_ratios.values()) >= args.minimum_depth_ratio

    augmented_parameters = np.r_[start_parameters, chosen]
    augmented_controls = old_controls + [
        (controlled, direction, displacement)
        for displacement, direction, (_, _, controlled) in zip(chosen, directions, CIRCUITS)
    ]
    first_circuit, first_sign, _ = CIRCUITS[0]
    payload = {
        "version": 1,
        "scope": "25D topology-preserving deepening of roundoff-limited protected circuits",
        "source": str(args.source.resolve()),
        "adaptive": str(args.adaptive.resolve()),
        "coordinates": str(args.output_csv.resolve()),
        "circuit": list(first_circuit),
        "valid_sign": first_sign,
        "bypass_waypoints": [augmented_parameters.tolist()],
        "local_controls": [
            {"label": label, "direction": direction.tolist(), "initial": initial}
            for label, direction, initial in augmented_controls
        ],
        "new_controls": [
            {
                "label": controlled,
                "circuit": list(circuit),
                "valid_sign": sign,
                "direction": direction.tolist(),
                "displacement": float(displacement),
            }
            for displacement, direction, (circuit, sign, controlled) in zip(chosen, directions, CIRCUITS)
        ],
        "chosen_displacements": chosen.tolist(),
        "start_exact_signed_determinants": {
            key: {"numerator": str(value.numerator), "denominator": str(value.denominator)}
            for key, value in start_exact.items()
        },
        "end_exact_signed_determinants": {
            key: {"numerator": str(value.numerator), "denominator": str(value.denominator)}
            for key, value in end_exact.items()
        },
        "exact_depth_ratios": depth_ratios,
        "start_keep_values": path[0]["keep_values"],
        "end_keep_values": end_keeps,
        "end_birth_values": end_births,
        "fresh_hull_end": {
            "class": record["class"],
            "f_vector": record["f_vector"],
            "active_labels": record["active_labels"],
            "base_face_present": record["base_face_present"],
            "missing_forced_rails": record["missing_forced_rails"],
            "stable_faces": record["stable_faces"],
            "unstable_vertices": record["unstable_vertices"],
            "saddle_edges": record["saddle_edges"],
            "min_nonzero_margin": mechanics.min_nonzero_margin,
        },
        "scan": scan,
        "path": path,
        "passed": True,
    }
    args.output.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n")
    print(json.dumps({
        "passed": True,
        "chosen_displacements": chosen.tolist(),
        "exact_depth_ratios": depth_ratios,
        "new_controls": payload["new_controls"],
        "fresh_hull_end": payload["fresh_hull_end"],
        "end_keep_values": end_keeps,
        "end_birth_values": end_births,
    }, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
