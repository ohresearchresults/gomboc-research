#!/usr/bin/env python3
"""Full 165-mode row-230 inward rechart with H910 nonresurrection."""
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
ATTACK = HERE.parent
TRACK = ATTACK.parent
ROOT = HERE.parents[4]
PARENT = ATTACK / "continuation" / "main"

sys.path.insert(0, str(PARENT))
import propose_full_control as base  # noqa: E402


DANGER = {
    (frozenset((198, 230, 231)), 229),
    (frozenset((198, 229, 230)), 231),
}


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def resolve(value: str) -> Path:
    path = Path(value)
    return path if path.is_absolute() else HERE / path


def exact_danger_jets(path, faces):
    output = {}
    for face_index, witness, support in base.ex.support_polynomials(path, faces):
        family = (frozenset(faces[face_index]), witness)
        if family not in DANGER:
            continue
        normal = base.ex.cycle_normal(faces[face_index], path)
        norm2 = base.ex.norm2(normal)
        square = support * support
        derivative = square.derivative() * norm2 - square * norm2.derivative()
        value = derivative.eval(Q(0))
        if value <= 0:
            raise AssertionError(("nonpositive exact row-230 first jet", family, value))
        support_source = support.eval(Q(0))
        support_endpoint = support.eval(Q(1))
        norm2_source = norm2.eval(Q(0))
        norm2_endpoint = norm2.eval(Q(1))
        endpoint_delta = (
            support_endpoint * support_endpoint * norm2_source
            - support_source * support_source * norm2_endpoint
        )
        if support_source * support_endpoint <= 0 or endpoint_delta <= 0:
            raise AssertionError(("non-inward exact row-230 endpoint", family, endpoint_delta))
        output[f"{sorted(family[0])}|{witness}"] = {
            "value": base.ex.qs(value),
            "degree": derivative.degree,
            "polynomial_digest": hashlib.sha256(
                "|".join(derivative.exact()).encode()
            ).hexdigest(),
            "endpoint_normalized_square_delta_numerator": base.ex.qs(endpoint_delta),
        }
    if set(output) != {"[198, 230, 231]|229", "[198, 229, 230]|231"}:
        raise AssertionError(output)
    return output


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--source", required=True)
    parser.add_argument("--faces", required=True)
    parser.add_argument("--output", required=True)
    parser.add_argument("--endpoint", required=True)
    parser.add_argument("--all-support", action="store_true")
    parser.add_argument("--inward-gamma-factor", type=float, default=2048.0)
    parser.add_argument(
        "--trust-cap",
        type=float,
        default=1e-6,
        help="largest physical L-infinity trust value admitted to the LP grid",
    )
    args = parser.parse_args()
    if not args.inward_gamma_factor > 0:
        raise ValueError("inward gamma factor must be positive")
    if not args.trust_cap > 0:
        raise ValueError("trust cap must be positive")

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
    source_signature = base.signature(source)
    if source_signature["f_vector"] != [61, 162, 103]:
        raise AssertionError(source_signature)
    if source_signature["class"] != [2, 2, 2]:
        raise AssertionError(source_signature)
    if base.face_sets(base.common.actual_faces(labels, points)) != base.face_sets(faces):
        raise AssertionError("fresh source hull differs from fixed face ledger")

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
    key_index = {key: index for index, key in enumerate(keys)}
    source_vector = base.mechanics_vector(source, *key_groups)
    mechanics_jacobian, fd_diagnostics = base.central_mechanics_jacobian(
        labels, points, modes, source, key_groups
    )

    near_support, all_support = base.common.support_specs(
        labels, points, faces, source.centroid, threshold=2e-3
    )
    guarded_support = all_support if args.all_support else near_support
    support_source = np.asarray([row[3] for row in guarded_support])
    support_jacobian = base.support_jacobian(
        labels, points, faces, guarded_support, modes
    )
    danger_indices = []
    for index, spec in enumerate(guarded_support):
        family = (frozenset(faces[spec[0]]), labels[spec[1]])
        if family in DANGER:
            danger_indices.append(index)
    found_danger = {
        (frozenset(faces[guarded_support[index][0]]), labels[guarded_support[index][1]])
        for index in danger_indices
    }
    if found_danger != DANGER:
        raise AssertionError(("danger family absent", found_danger))

    displacement = np.asarray([
        [mode[offset, axis] for mode in modes]
        for offset in range(len(labels)) for axis in range(3)
    ])
    branches = []
    selected = None
    trust_grid = tuple(
        trust
        for trust in (1e-8, 2e-8, 5e-8, 1e-7, 2e-7, 5e-7, 1e-6)
        if trust <= args.trust_cap
    )
    if not trust_grid:
        raise ValueError("trust cap excludes the complete LP grid")
    for trust in trust_grid:
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

        for key in sorted(base.PROTECTED_KEYS, key=repr):
            rows.append(np.r_[
                -mechanics_jacobian[key_index[key]]
                / abs(source_vector[key_index[key]]),
                0.0,
            ])
            rhs.append(0.0)
            names.append(("protected_nondecrease", repr(key)))

        exempt = set(base.TARGET_KEYS.values()) | base.PROTECTED_KEYS
        for offset, (key, value) in enumerate(zip(keys, source_vector)):
            if key in exempt:
                continue
            sign = 1.0 if value > 0 else -1.0
            guard_fraction = 0.02 if key == base.H910_KEY else 0.15
            rows.append(np.r_[
                -sign * mechanics_jacobian[offset] / abs(value), 0.0
            ])
            rhs.append(guard_fraction)
            names.append(("mechanics_signed_guard", repr(key), guard_fraction))

        for index, (spec, margin) in enumerate(zip(guarded_support, support_source)):
            rows.append(np.r_[-support_jacobian[index] / margin, 0.0])
            rhs.append(0.15)
            names.append(("support_signed_guard", spec[0], labels[spec[1]]))
        for index in danger_indices:
            rows.append(np.r_[
                -support_jacobian[index] / support_source[index],
                args.inward_gamma_factor,
            ])
            rhs.append(0.0)
            names.append((
                "row230_strict_inward_tangent",
                guarded_support[index][0], labels[guarded_support[index][1]],
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
            "inward_gamma_factor": args.inward_gamma_factor,
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
                    and endpoint_signature["stable_faces"] == source_signature["stable_faces"]
                    and endpoint_signature["unstable_vertices"] == source_signature["unstable_vertices"]
                    and endpoint_signature["saddle_edges"] == source_signature["saddle_edges"]
                )
                endpoint_vector = base.mechanics_vector(endpoint_mechanics, *key_groups)
                ratios = {
                    name: float(endpoint_vector[key_index[key]] / source_vector[key_index[key]])
                    for name, key in base.TARGET_KEYS.items()
                }
                h910_endpoint = float(endpoint_vector[key_index[base.H910_KEY]])
                danger_values = base.common.support_values(
                    labels, endpoint, faces,
                    [guarded_support[index] for index in danger_indices],
                )
                danger_ratios = [
                    float(value / support_source[index])
                    for value, index in zip(danger_values, danger_indices)
                ]
            except Exception as error:
                same_cell = False
                endpoint_signature = None
                ratios = {}
                h910_endpoint = None
                danger_ratios = []
                record["endpoint_error"] = repr(error)
            record.update({
                "common_fractional_descent": float(lp.x[-1]),
                "physical_linf": float(np.max(np.abs(delta))),
                "same_actual_cell": same_cell,
                "endpoint_signature": endpoint_signature,
                "target_ratios": ratios,
                "h910_endpoint": h910_endpoint,
                "danger_support_ratios": danger_ratios,
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
                and h910_endpoint is not None and h910_endpoint < 0.0
                and all(value > 1.0 for value in danger_ratios)
            ):
                candidate = (record, delta)
                if (
                    selected is None
                    or ratios["H1011"] < selected[0]["target_ratios"]["H1011"]
                ):
                    selected = candidate
        branches.append(record)

    if selected is None:
        output_path.write_text(json.dumps({
            "version": 1,
            "verdict": "ROW230_FULL_CHART_NO_ACCEPTED_FLOAT_DIRECTION",
            "primal_lp_feasible": any(row["success"] for row in branches),
            "mode_count": len(modes),
            "guarded_support_count": len(guarded_support),
            "branches": branches,
        }, indent=2) + "\n")
        raise RuntimeError("no accepted float rechart; inspect primal before dual")

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
        label: tuple(
            exact_rows[label][axis] + exact_delta[label][axis]
            for axis in range(3)
        )
        for label in labels
    }
    exact_path = {
        label: tuple(
            base.ex.P((exact_rows[label][axis], exact_delta[label][axis]))
            for axis in range(3)
        )
        for label in labels
    }
    jets = {
        name: base.exact_first_jet(exact_path, faces, name)
        for name in base.TARGET_KEYS
    }
    danger_jets = exact_danger_jets(exact_path, faces)
    source_edge = base.ex.mechanics_primitives(exact_path, faces)["edge"][(9, 10)]
    components = ("t", "one_minus_t", "beta1", "beta2")
    h910_witness = min(components, key=lambda name: source_edge[name].eval(Q(0)))
    h910_source = source_edge[h910_witness].eval(Q(0))
    h910_endpoint = source_edge[h910_witness].eval(Q(1))
    if not h910_source < 0 or not h910_endpoint < 0:
        raise AssertionError(("exact H910 nonresurrection failed", h910_source, h910_endpoint))

    support = base.ex.supporting_cell(exact_endpoint, faces)
    _ledger, mechanics = base.ex.classify_point(exact_endpoint, faces)
    if support["f_vector"] != [61, 162, 103] or mechanics["class"] != [2, 2, 2]:
        raise AssertionError((support, mechanics))
    missing = sorted(base.frozen_builder.forced_rails() - set(support["edges"]))
    if missing:
        raise AssertionError(("rail loss", missing))
    base.write_exact_csv(endpoint_path, exact_endpoint)

    payload = {
        "version": 1,
        "scope": (
            "full 165-mode row-230 inward actual-cell rechart; H910 is guarded "
            "against resurrection rather than forced farther outward; both row-230 "
            "first jets exceed a positive multiple of the common descent variable"
        ),
        "source_hashes": {
            str(source_path.relative_to(ROOT)): sha256(source_path),
            str(faces_path.relative_to(ROOT)): sha256(faces_path),
        },
        "source_signature": source_signature,
        "mode_count": len(modes),
        "mode_names": [list(item) for item in mode_names],
        "base_plane_normal": plane_normal.tolist(),
        "finite_difference_diagnostics": fd_diagnostics,
        "near_support_count": len(near_support),
        "all_support_count": len(all_support),
        "guarded_support_count": len(guarded_support),
        "all_support_in_lp": bool(args.all_support),
        "inward_gamma_factor": args.inward_gamma_factor,
        "trust_cap": args.trust_cap,
        "branches": branches,
        "selected_branch": record,
        "physical_step": base.ex.qs(physical_step),
        "velocity": {
            str(label): [base.ex.qs(value) for value in velocity[label]]
            for label in labels
        },
        "base_velocity_coefficients": base_coefficients,
        "exact_selected_first_jets": jets,
        "exact_row230_first_jets": danger_jets,
        "exact_h910_witness": {
            "component": h910_witness,
            "source": base.ex.qs(h910_source),
            "endpoint": base.ex.qs(h910_endpoint),
        },
        "exact_endpoint": {
            "file": endpoint_path.name,
            "sha256": sha256(endpoint_path),
            "support": {key: value for key, value in support.items() if key != "edges"},
            "mechanics": mechanics,
            "forced_rail_count": 37,
            "missing_forced_rails": [],
        },
        "verdict": "ROW230_FULL_CONTROL_RATIONAL_RECHART_PROPOSAL_PASS",
    }
    output_path.write_text(json.dumps(payload, indent=2) + "\n")
    print(json.dumps({
        "verdict": payload["verdict"],
        "selected": record,
        "exact_h910_witness": payload["exact_h910_witness"],
        "endpoint": payload["exact_endpoint"],
    }, indent=2))


if __name__ == "__main__":
    main()
