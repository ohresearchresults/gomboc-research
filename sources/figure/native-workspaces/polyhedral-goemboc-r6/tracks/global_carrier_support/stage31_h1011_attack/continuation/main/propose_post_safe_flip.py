#!/usr/bin/env python3
"""Rebuild the full-control descent in the safe post-flip cell.

The two support slacks leading to loss of active row 230 are explicitly pushed
inward.  Everything else follows the complete physical-trust chart used by the
first full-control proposal.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import sys
from fractions import Fraction as Q
from pathlib import Path

import numpy as np
from scipy.optimize import linprog


HERE = Path(__file__).resolve().parent
ATTACK = HERE.parents[1]
TRACK = ATTACK.parent
ROOT = HERE.parents[4]
SOURCE = HERE / "exact_full_control_chain_far.csv"
FACES_PATH = HERE / "exact_full_control_chain_post_faces.json"
OUTPUT = HERE / "post_safe_flip_proposal.json"
ENDPOINT = HERE / "post_safe_flip_candidate.csv"

sys.path.insert(0, str(HERE))
import propose_full_control as base  # noqa: E402


DANGEROUS_ROW230_FAMILY = {
    (frozenset((198, 230, 231)), 229),
    (frozenset((198, 229, 230)), 231),
}


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--source", default=str(SOURCE))
    parser.add_argument("--faces", default=str(FACES_PATH))
    parser.add_argument("--output", default=str(OUTPUT))
    parser.add_argument("--endpoint", default=str(ENDPOINT))
    args = parser.parse_args()

    def resolve(value):
        path = Path(value)
        return path if path.is_absolute() else HERE / path

    source_path = resolve(args.source)
    faces_path = resolve(args.faces)
    output_path = resolve(args.output)
    endpoint_path = resolve(args.endpoint)
    exact_rows = base.ex.read_rows(source_path)
    labels = sorted(exact_rows)
    points = np.asarray(
        [[float(value) for value in exact_rows[label]] for label in labels],
        dtype=float,
    )
    faces = json.loads(faces_path.read_text())
    source = base.evaluate(labels, points)
    if base.signature(source)["f_vector"] != [61, 162, 103] or source.cls != (2, 2, 2):
        raise AssertionError(base.signature(source))
    if base.face_sets(base.common.actual_faces(labels, points)) != base.face_sets(faces):
        raise AssertionError("fresh hull differs from certified post-flip ledger")

    modes, mode_names, plane_normal = base.build_modes(labels, points)
    face_keys = sorted(source.face_decisions)
    vertex_keys = sorted(source.vertex_decisions)
    edge_keys = sorted(source.edge_decisions)
    key_groups = (face_keys, vertex_keys, edge_keys)
    keys = (
        [("S", key) for key in face_keys]
        + [("U", key) for key in vertex_keys]
        + [("H", key) for key in edge_keys]
    )
    key_index = {key: offset for offset, key in enumerate(keys)}
    source_vector = base.mechanics_vector(source, *key_groups)
    mechanics_jacobian, fd_diagnostics = base.central_mechanics_jacobian(
        labels, points, modes, source, key_groups
    )

    near_support, all_support = base.common.support_specs(
        labels, points, faces, source.centroid, threshold=2e-3
    )
    support_source = np.asarray([row[3] for row in near_support])
    support_derivative = base.support_jacobian(
        labels, points, faces, near_support, modes
    )
    danger_indices = []
    for offset, spec in enumerate(near_support):
        family = (frozenset(faces[spec[0]]), labels[spec[1]])
        if family in DANGEROUS_ROW230_FAMILY:
            danger_indices.append(offset)
    if {
        (frozenset(faces[near_support[index][0]]), labels[near_support[index][1]])
        for index in danger_indices
    } != DANGEROUS_ROW230_FAMILY:
        raise AssertionError("row-230 loss support family absent")

    displacement = np.asarray([
        [mode[offset, axis] for mode in modes]
        for offset in range(len(labels)) for axis in range(3)
    ])
    branches = []
    selected = None
    for trust in (1e-8, 2e-8, 5e-8, 1e-7, 2e-7, 5e-7, 1e-6):
        rows = []
        rhs = []
        names = []
        for name, key in base.TARGET_KEYS.items():
            value = source_vector[key_index[key]]
            if value <= 0:
                raise AssertionError((name, value))
            rows.append(np.r_[mechanics_jacobian[key_index[key]] / value, 1.0])
            rhs.append(0.0)
            names.append(("target", name))

        h910_value = source_vector[key_index[base.H910_KEY]]
        if h910_value >= 0:
            raise AssertionError("H910 is not dead")
        rows.append(np.r_[
            mechanics_jacobian[key_index[base.H910_KEY]] / abs(h910_value), 0.0
        ])
        rhs.append(0.0)
        names.append(("dead_inward", "H910"))
        for key in sorted(base.PROTECTED_KEYS, key=repr):
            rows.append(np.r_[
                -mechanics_jacobian[key_index[key]]
                / abs(source_vector[key_index[key]]),
                0.0,
            ])
            rhs.append(0.0)
            names.append(("protected_nondecrease", repr(key)))

        exempt = set(base.TARGET_KEYS.values()) | {base.H910_KEY} | base.PROTECTED_KEYS
        for offset, (key, value) in enumerate(zip(keys, source_vector)):
            if key in exempt:
                continue
            sign = 1.0 if value > 0 else -1.0
            rows.append(np.r_[-sign * mechanics_jacobian[offset] / abs(value), 0.0])
            rhs.append(0.15)
            names.append(("mechanics_guard", repr(key), float(value)))

        for offset, (spec, margin) in enumerate(zip(near_support, support_source)):
            rows.append(np.r_[-support_derivative[offset] / margin, 0.0])
            rhs.append(0.15)
            names.append(("support_guard", spec[0], labels[spec[1]], float(margin)))
        for offset in danger_indices:
            rows.append(np.r_[
                -support_derivative[offset] / support_source[offset], 0.0
            ])
            rhs.append(0.0)
            names.append((
                "row230_loss_family_inward",
                near_support[offset][0],
                labels[near_support[offset][1]],
            ))

        rows.extend(np.c_[displacement / trust, np.zeros(displacement.shape[0])])
        rhs.extend(np.ones(displacement.shape[0]))
        names.extend(("physical_plus", index) for index in range(displacement.shape[0]))
        rows.extend(np.c_[-displacement / trust, np.zeros(displacement.shape[0])])
        rhs.extend(np.ones(displacement.shape[0]))
        names.extend(("physical_minus", index) for index in range(displacement.shape[0]))
        lp = linprog(
            np.r_[np.zeros(len(modes)), -1.0],
            A_ub=np.asarray(rows),
            b_ub=np.asarray(rhs),
            bounds=[(-1000.0, 1000.0)] * len(modes) + [(0.0, 1.0)],
            method="highs",
        )
        record = {
            "trust": trust,
            "success": bool(lp.success),
            "message": lp.message,
            "constraint_count": len(rows),
        }
        if lp.success:
            coefficients = np.asarray(lp.x[:-1])
            delta = np.tensordot(coefficients, modes, axes=(0, 0))
            endpoint = points + delta
            try:
                endpoint_mechanics = base.evaluate(labels, endpoint)
                endpoint_faces = base.common.actual_faces(labels, endpoint)
                endpoint_signature = base.signature(endpoint_mechanics)
                same_cell = (
                    base.face_sets(endpoint_faces) == base.face_sets(faces)
                    and endpoint_signature["class"] == [2, 2, 2]
                    and endpoint_signature["stable_faces"] == base.signature(source)["stable_faces"]
                    and endpoint_signature["unstable_vertices"] == base.signature(source)["unstable_vertices"]
                    and endpoint_signature["saddle_edges"] == base.signature(source)["saddle_edges"]
                )
                if same_cell:
                    endpoint_values = base.mechanics_vector(endpoint_mechanics, *key_groups)
                    ratios = {
                        name: float(endpoint_values[key_index[key]] / source_vector[key_index[key]])
                        for name, key in base.TARGET_KEYS.items()
                    }
                    h910_endpoint = float(endpoint_values[key_index[base.H910_KEY]])
                    danger_endpoint = base.common.support_values(
                        labels, endpoint, faces, [near_support[index] for index in danger_indices]
                    )
                else:
                    ratios = {}
                    h910_endpoint = None
                    danger_endpoint = []
                    record["removed_faces"] = [
                        list(face) for face in sorted(
                            base.face_sets(faces) - base.face_sets(endpoint_faces)
                        )
                    ]
                    record["added_faces"] = [
                        list(face) for face in sorted(
                            base.face_sets(endpoint_faces) - base.face_sets(faces)
                        )
                    ]
            except Exception as error:
                same_cell = False
                endpoint_signature = None
                ratios = {}
                h910_endpoint = None
                danger_endpoint = []
                record["endpoint_error"] = repr(error)
            record.update({
                "common_fractional_descent": float(lp.x[-1]),
                "physical_linf": float(np.max(np.abs(delta))),
                "same_actual_cell": same_cell,
                "endpoint_signature": endpoint_signature,
                "target_ratios": ratios,
                "h910_endpoint": h910_endpoint,
                "danger_support_ratios": [
                    float(value / support_source[index])
                    for value, index in zip(danger_endpoint, danger_indices)
                ],
                "active_modes": [
                    {
                        "column": int(index),
                        "label": mode_names[index][0],
                        "axis": mode_names[index][1],
                        "coefficient": float(coefficients[index]),
                    }
                    for index in np.argsort(np.abs(coefficients))[-30:][::-1]
                    if abs(coefficients[index]) > 1e-14
                ],
            })
            if (
                same_cell
                and all(value < 1.0 for value in ratios.values())
                and h910_endpoint is not None and h910_endpoint < h910_value
                and all(value >= 1.0 - 2e-4 for value in record["danger_support_ratios"])
            ):
                selected = (record, delta)
        branches.append(record)
    if selected is None:
        output_path.write_text(json.dumps({
            "version": 1,
            "verdict": "POST_SAFE_FLIP_FULL_CONTROL_ROUTE_NOT_YET_FOUND",
            "branches": branches,
            "mode_count": len(modes),
            "dangerous_support_family": [
                [sorted(face), witness] for face, witness in DANGEROUS_ROW230_FAMILY
            ],
        }, indent=2) + "\n")
        raise RuntimeError("no accepted route; dual certificate required")

    record, delta = selected
    float_velocity = delta / record["physical_linf"]
    velocity, base_coefficients = base.common.exactify_velocity(
        exact_rows, labels, float_velocity
    )
    physical_step = Q(format(record["physical_linf"], ".17g"))
    exact_delta = {
        label: tuple(physical_step * value for value in velocity[label])
        for label in labels
    }
    exact_endpoint = {
        label: tuple(exact_rows[label][axis] + exact_delta[label][axis] for axis in range(3))
        for label in labels
    }
    exact_path = {
        label: tuple(base.ex.P((exact_rows[label][axis], exact_delta[label][axis])) for axis in range(3))
        for label in labels
    }
    jets = {
        name: base.exact_first_jet(exact_path, faces, name)
        for name in base.TARGET_KEYS
    }
    support = base.ex.supporting_cell(exact_endpoint, faces)
    ledger, mechanics = base.ex.classify_point(exact_endpoint, faces)
    if support["f_vector"] != [61, 162, 103] or mechanics["class"] != [2, 2, 2]:
        raise AssertionError((support, mechanics))
    if base.frozen_builder.forced_rails() - set(support["edges"]):
        raise AssertionError("rail loss")
    components = ("t", "one_minus_t", "beta1", "beta2")
    h910_source = base.ex.mechanics_primitives(exact_rows, faces)["edge"][(9, 10)]
    witness = min(components, key=lambda item: h910_source[item])
    h910_endpoint = ledger["edge"][(9, 10)][witness]
    if not h910_endpoint < h910_source[witness] < 0:
        raise AssertionError("exact H910 witness did not move outward")
    base.write_exact_csv(endpoint_path, exact_endpoint)

    payload = {
        "version": 1,
        "scope": "full-control proposal in safe (229,231)-diagonal cell with row-230-loss family pushed inward",
        "source_hashes": {
            str(source_path.relative_to(ROOT)): sha256(source_path),
            str(faces_path.relative_to(ROOT)): sha256(faces_path),
        },
        "source_signature": base.signature(source),
        "mode_count": len(modes),
        "mode_names": [list(item) for item in mode_names],
        "base_plane_normal": plane_normal.tolist(),
        "finite_difference_diagnostics": fd_diagnostics,
        "near_support_count": len(near_support),
        "all_support_count": len(all_support),
        "dangerous_support_family": [
            [sorted(face), witness] for face, witness in sorted(
                DANGEROUS_ROW230_FAMILY, key=lambda item: (sorted(item[0]), item[1])
            )
        ],
        "branches": branches,
        "selected_branch": record,
        "physical_step": base.ex.qs(physical_step),
        "velocity": {
            str(label): [base.ex.qs(value) for value in velocity[label]]
            for label in labels
        },
        "base_velocity_coefficients": base_coefficients,
        "exact_selected_first_jets": jets,
        "exact_h910_witness": {
            "component": witness,
            "source": base.ex.qs(h910_source[witness]),
            "endpoint": base.ex.qs(h910_endpoint),
        },
        "exact_endpoint": {
            "file": endpoint_path.name,
            "sha256": sha256(endpoint_path),
            "support": {key: value for key, value in support.items() if key != "edges"},
            "mechanics": mechanics,
            "forced_rail_count": len(base.frozen_builder.forced_rails()),
            "missing_forced_rails": [],
        },
        "verdict": "POST_SAFE_FLIP_FULL_CONTROL_RATIONAL_DESCENT_PROPOSAL_PASS",
    }
    output_path.write_text(json.dumps(payload, indent=2) + "\n")
    print(json.dumps({
        "verdict": payload["verdict"],
        "selected": record,
        "exact_first_jet_signs": {name: "negative" for name in jets},
        "endpoint": payload["exact_endpoint"],
    }, indent=2))


if __name__ == "__main__":
    main()
