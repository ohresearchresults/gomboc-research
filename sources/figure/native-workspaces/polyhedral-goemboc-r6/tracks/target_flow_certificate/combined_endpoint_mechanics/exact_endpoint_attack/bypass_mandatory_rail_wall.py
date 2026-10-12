#!/usr/bin/env python3
"""Find a residual-null L-path around the mandatory edge-(251,252) wall."""
from __future__ import annotations

import argparse
import ast
import json
import sys
from pathlib import Path

import numpy as np
from scipy.optimize import brentq


HERE = Path(__file__).resolve().parent
PARENT = HERE.parent
sys.path[:0] = [str(PARENT), str(HERE)]

import build_u54_material_exact_path as exact_path  # noqa: E402
import combined_four_death_lp as four  # noqa: E402
from integrate_four_death_direction import write_csv  # noqa: E402
from reverse_wall_bypass import oriented_volume  # noqa: E402
import post_flip_trust_slp as slp  # noqa: E402


SOURCE = HERE / "post_flip_intrinsic_step_008.csv"
EVENT = HERE / "recomputed_intrinsic_event.json"
CIRCUIT = (224, 228, 251, 252)
PLANE_TOL = 2e-12


def parse_circuit(value):
    circuit = tuple(int(item) for item in value.split(","))
    if len(circuit) != 4 or len(set(circuit)) != 4:
        raise argparse.ArgumentTypeError("circuit must contain four distinct labels")
    return circuit


def face_signature(result):
    return tuple(sorted(tuple(sorted(face["cycle"])) for face in result.faces))


def equilibrium_signature(result):
    return (
        tuple(sorted(tuple(sorted(result.faces[index]["cycle"])) for index, _ in result.stable)),
        tuple(sorted(index for index, _ in result.unstable)),
        tuple(sorted(tuple(edge) for edge, _ in result.saddles)),
    )


def coordinate_linf(modes, coefficients):
    return max(
        abs(float(sum(coefficients[column] * modes[column][label][axis] for column in range(len(modes)))))
        for label in modes[0]
        for axis in range(3)
    )


def main() -> None:
    global PLANE_TOL

    parser = argparse.ArgumentParser()
    parser.add_argument("--source", default=str(SOURCE))
    parser.add_argument("--event", default=str(EVENT))
    parser.add_argument("--circuit", type=parse_circuit, default=CIRCUIT)
    parser.add_argument("--prefix", default="mandatory_rail_bypass")
    parser.add_argument("--plane-tol", type=float, default=PLANE_TOL)
    parser.add_argument(
        "--selection",
        choices=("min-control", "max-margin", "max-clearance"),
        default="min-control",
    )
    args = parser.parse_args()
    source_path = Path(args.source)
    event_path = Path(args.event)
    if not source_path.is_absolute():
        source_path = HERE / source_path
    if not event_path.is_absolute():
        event_path = HERE / event_path
    circuit = tuple(args.circuit)
    PLANE_TOL = args.plane_tol

    four.ACTIVE_PLANE_TOL = PLANE_TOL
    event = json.loads(event_path.read_text())
    points = four.load_points(source_path)
    modes, mode_meta, _chart = four.chart_modes(points)
    direction = np.asarray(event["best"]["coefficients"], dtype=float)
    residual_keys = [ast.literal_eval(text) for text in event["best"]["deaths"]]
    root = sum(event["event"]["fraction_bracket"]) / 2.0

    baseline_result, _baseline_values = slp.robust_primitive_ledger(
        points, PLANE_TOL
    )
    baseline_faces = face_signature(baseline_result)
    baseline_equilibria = equilibrium_signature(baseline_result)
    forced_rails = exact_path.forced_rails()

    def materialize(coefficients):
        return slp.apply_modes(points, modes, coefficients)

    def volume(coefficients):
        return oriented_volume(materialize(coefficients), circuit)

    def residuals(coefficients):
        candidate = materialize(coefficients)
        result = exact_path.actual.evaluate(candidate, coplanar_rel=PLANE_TOL)
        if not result.valid:
            raise RuntimeError(result.error)
        centroid = result.centroid
        X = {label: candidate[label] - centroid for label in candidate}
        radius = max(
            float(np.sqrt(np.mean([np.dot(value, value) for value in X.values()]))),
            1e-300,
        )

        face_index = next(
            index
            for index, face in enumerate(result.faces)
            if frozenset(face["cycle"]) == frozenset(exact_path.QUAD)
        )
        face = result.faces[face_index]
        normal = np.asarray(face["n"], dtype=float)
        foot = -(face["off"] + float(np.dot(normal, centroid))) * normal
        a, b = 8, 246
        edge = X[b] - X[a]
        reference = np.mean([X[label] for label in face["cycle"]], axis=0)
        face_value = float(
            np.dot(np.cross(edge, foot - X[a]), normal)
            / max(np.linalg.norm(edge) * radius, 1e-300)
        )
        if np.dot(np.cross(edge, reference - X[a]), normal) < 0:
            face_value = -face_value

        direction54 = X[1] - X[54]
        vertex_value = float(
            -np.dot(X[54], direction54)
            / max(np.linalg.norm(X[54]) * np.linalg.norm(direction54), 1e-300)
        )

        def beta2(edge_labels):
            left, right = edge_labels
            direction_edge = X[right] - X[left]
            t = float(-np.dot(X[left], direction_edge) / np.dot(direction_edge, direction_edge))
            projection = X[left] + t * direction_edge
            incident = result.edge_faces[tuple(sorted(edge_labels))]
            n1 = np.asarray(result.faces[incident[0]]["n"], dtype=np.longdouble)
            n2 = np.asarray(result.faces[incident[1]]["n"], dtype=np.longdouble)
            p = np.asarray(projection, dtype=np.longdouble)
            aa, bb, cc = np.dot(n1, n1), np.dot(n1, n2), np.dot(n2, n2)
            denominator = np.dot(np.cross(n1, n2), np.cross(n1, n2))
            if denominator <= 0:
                raise RuntimeError(("selected edge has parallel normals", edge_labels))
            r1, r2 = np.dot(p, n1), np.dot(p, n2)
            value = (r2 * aa - r1 * bb) / denominator
            return float(value / max(np.linalg.norm(projection), 1e-300))

        return np.asarray([
            face_value,
            vertex_value,
            beta2((6, 7)),
            beta2((9, 10)),
        ])

    baseline_residuals = residuals(np.zeros(len(modes)))

    def validate(coefficients):
        candidate = materialize(coefficients)
        result = exact_path.actual.evaluate(candidate, coplanar_rel=PLANE_TOL)
        if not result.valid:
            return False, {"error": result.error}
        signature = face_signature(result)
        equilibria = equilibrium_signature(result)
        audit = {
            "f_vector": [len(result.active), len(result.edges), len(result.faces)],
            "class": [len(result.stable), len(result.unstable), len(result.saddles)],
            "topology_margin": float(result.topology_margin),
            "same_faces": signature == baseline_faces,
            "same_equilibria": equilibria == baseline_equilibria,
            "all_rails": forced_rails.issubset(set(result.edges)),
            "base": exact_path.BASE in {frozenset(face) for face in signature},
            "quad": frozenset(exact_path.QUAD) in {frozenset(face) for face in signature},
            "u8": 8 in equilibria[1],
            "circuit_volume": float(volume(coefficients)),
        }
        valid = bool(
            audit["f_vector"] == [60, 158, 100]
            and audit["class"] == [2, 2, 2]
            and audit["same_faces"]
            and audit["same_equilibria"]
            and audit["all_rails"]
            and audit["base"]
            and audit["quad"]
            and audit["u8"]
        )
        return valid, audit

    circuit_rails = sorted(
        edge for edge in forced_rails
        if edge[0] in circuit and edge[1] in circuit
    )
    if len(circuit_rails) != 1:
        raise AssertionError(("mandatory circuit rail is not unique", circuit_rails))
    rail_left, rail_right = circuit_rails[0]
    if rail_right != rail_left + 1:
        raise AssertionError(("automatic rail neighborhood requires consecutive labels", circuit_rails[0]))
    row_sets = tuple(
        set(circuit) | set(range(rail_left - radius, rail_right + radius + 1))
        for radius in (0, 1, 2)
    )
    trials = []
    accepted = []
    for rows in row_sets:
        columns = [
            index for index, meta in enumerate(mode_meta) if meta.get("row") in rows
        ]
        for gap in (0.03, 0.05, 0.08, 0.12, 0.15, 0.20):
            pre_fraction = root - gap
            if pre_fraction <= 0:
                continue
            base_coefficients = pre_fraction * direction
            try:
                base_residuals = residuals(base_coefficients)
            except Exception as error:
                trials.append({
                    "rows": sorted(rows),
                    "gap": gap,
                    "status": "base_ledger_failure",
                    "error": repr(error),
                })
                continue
            matrix = np.empty((4, len(columns)))
            gradient = np.empty(len(columns))
            derivative_step = 1e-9
            wall_coefficients = root * direction
            derivative_failed = None
            for local_index, column in enumerate(columns):
                perturbation = np.zeros(len(modes))
                perturbation[column] = derivative_step
                try:
                    matrix[:, local_index] = (
                        residuals(base_coefficients + perturbation)
                        - residuals(base_coefficients - perturbation)
                    ) / (2 * derivative_step) / base_residuals
                except Exception as error:
                    derivative_failed = repr(error)
                    break
                gradient[local_index] = (
                    volume(wall_coefficients + perturbation)
                    - volume(wall_coefficients - perturbation)
                ) / (2 * derivative_step)
            if derivative_failed is not None:
                trials.append({
                    "rows": sorted(rows),
                    "gap": gap,
                    "status": "derivative_ledger_failure",
                    "error": derivative_failed,
                })
                continue
            _u, singular_values, vt = np.linalg.svd(matrix, full_matrices=True)
            rank = int(np.linalg.matrix_rank(matrix, tol=1e-8))
            null_basis = vt[rank:].T
            if not null_basis.shape[1]:
                trials.append({
                    "rows": sorted(rows), "gap": gap, "status": "no_nullspace"
                })
                continue
            projected = null_basis @ (null_basis.T @ gradient)
            response = float(gradient @ projected)
            if abs(response) < 1e-20:
                trials.append({
                    "rows": sorted(rows), "gap": gap,
                    "status": "zero_circuit_projection",
                })
                continue
            sign_pre = np.sign(volume(base_coefficients))
            endpoint_volume = volume(direction)
            projected_control = np.zeros(len(modes))
            projected_control[columns] = projected
            for factor in (0.1, 0.25, 0.5, 1.0, 2.0):
                target = sign_pre * factor * max(abs(volume(base_coefficients)), 1e-15)

                def endpoint_equation(scale):
                    return volume(direction + scale * projected_control) - target

                estimate = (target - endpoint_volume) / response
                if not estimate:
                    continue
                endpoint_zero = endpoint_equation(0.0)
                bound = estimate
                bound_value = endpoint_equation(bound)
                expansions = 0
                while endpoint_zero * bound_value > 0 and expansions < 20:
                    bound *= 2.0
                    bound_value = endpoint_equation(bound)
                    expansions += 1
                if endpoint_zero * bound_value > 0:
                    trials.append({
                        "rows": sorted(rows),
                        "gap": gap,
                        "factor": factor,
                        "status": "nonlinear_endpoint_root_unbracketed",
                        "linear_scale_estimate": estimate,
                    })
                    continue
                scale = brentq(
                    endpoint_equation,
                    min(0.0, bound),
                    max(0.0, bound),
                    xtol=1e-18,
                    rtol=1e-14,
                )
                local = projected * scale
                control = np.zeros(len(modes))
                control[columns] = local
                lifted = base_coefficients + control
                endpoint = direction + control
                record = {
                    "rows": sorted(rows),
                    "columns": columns,
                    "gap": gap,
                    "factor": factor,
                    "target_endpoint_volume": float(target),
                    "nonlinear_control_scale": float(scale),
                    "root_bracket_expansions": expansions,
                    "rank": rank,
                    "nullity": int(null_basis.shape[1]),
                    "singular_values": singular_values.tolist(),
                    "projected_gradient_norm": float(np.linalg.norm(projected)),
                    "fractional_residual_leakage": (matrix @ local).tolist(),
                    "control_l2": float(np.linalg.norm(control)),
                    "control_coordinate_linf": coordinate_linf(modes, control),
                    "volumes": {
                        "source": float(volume(np.zeros(len(modes)))),
                        "pre": float(volume(base_coefficients)),
                        "lifted": float(volume(lifted)),
                        "uncontrolled_endpoint": float(endpoint_volume),
                        "controlled_endpoint": float(volume(endpoint)),
                    },
                }
                path_valid = True
                minimum_margin = float("inf")
                maximum_residual_ratio = 0.0
                residual_evaluation_failures = []
                segment_counts = []
                for name, left, right, count in (
                    ("source_to_pre", np.zeros(len(modes)), base_coefficients, 31),
                    ("lift", base_coefficients, lifted, 41),
                    ("horizontal", lifted, endpoint, 81),
                ):
                    segment_valid = 0
                    for parameter in np.linspace(0.0, 1.0, count):
                        coefficients = (1.0 - parameter) * left + parameter * right
                        valid, audit = validate(coefficients)
                        if not valid:
                            path_valid = False
                            record["first_failure"] = {
                                "segment": name,
                                "parameter": float(parameter),
                                "audit": audit,
                            }
                            break
                        segment_valid += 1
                        minimum_margin = min(minimum_margin, audit["topology_margin"])
                        try:
                            ratio = residuals(coefficients) / baseline_residuals
                            maximum_residual_ratio = max(
                                maximum_residual_ratio, float(np.max(ratio))
                            )
                        except Exception as error:
                            residual_evaluation_failures.append({
                                "segment": name,
                                "parameter": float(parameter),
                                "error": repr(error),
                            })
                    segment_counts.append({
                        "segment": name,
                        "valid_samples": segment_valid,
                        "requested_samples": count,
                    })
                    if not path_valid:
                        break
                endpoint_ratios = None
                if path_valid:
                    endpoint_ratios = (residuals(endpoint) / baseline_residuals).tolist()
                    path_valid = bool(
                        all(value < 1.0 for value in endpoint_ratios)
                        and maximum_residual_ratio <= 1.0 + 2e-6
                        and np.sign(volume(endpoint)) == sign_pre
                    )
                record.update({
                    "path_valid": path_valid,
                    "segment_counts": segment_counts,
                    "minimum_topology_margin": minimum_margin,
                    "maximum_residual_ratio": maximum_residual_ratio,
                    "residual_evaluation_failures": residual_evaluation_failures,
                    "endpoint_residual_ratios": endpoint_ratios,
                    "control_coefficients": control.tolist(),
                    "pre_coefficients": base_coefficients.tolist(),
                    "lifted_coefficients": lifted.tolist(),
                    "endpoint_coefficients": endpoint.tolist(),
                })
                trials.append(record)
                if path_valid:
                    accepted.append(record)

    if args.selection == "min-control":
        accepted.sort(key=lambda row: (
            row["control_coordinate_linf"], -row["minimum_topology_margin"]
        ))
    elif args.selection == "max-margin":
        accepted.sort(key=lambda row: (
            -row["minimum_topology_margin"], row["control_coordinate_linf"]
        ))
    else:
        accepted.sort(key=lambda row: (
            -abs(row["volumes"]["controlled_endpoint"]),
            row["control_coordinate_linf"],
        ))
    best = accepted[0] if accepted else None
    files = {}
    if best is not None:
        for name in ("pre", "lifted", "endpoint"):
            coefficients = np.asarray(best[f"{name}_coefficients"], dtype=float)
            path = HERE / f"{args.prefix}_{name}.csv"
            write_csv(path, materialize(coefficients))
            files[name] = path.name
        best["files"] = files

    payload = {
        "version": 1,
        "scope": (
            f"residual-null bypass of exact mandatory edge-{circuit_rails[0]} wall"
        ),
        "source": source_path.name,
        "event": event_path.name,
        "circuit": list(circuit),
        "mandatory_rail": list(circuit_rails[0]),
        "selection": args.selection,
        "root": root,
        "residual_keys": [repr(key) for key in residual_keys],
        "trial_count": len(trials),
        "accepted_count": len(accepted),
        "trials": trials,
        "best": best,
        "conclusion": (
            "sampled residual-null rail-preserving bypass materialized"
            if best is not None
            else "tested local nullspaces did not produce a valid bypass"
        ),
    }
    output = HERE / f"{args.prefix}.json"
    output.write_text(json.dumps(payload, indent=2) + "\n")
    print(json.dumps({
        "trial_count": len(trials),
        "accepted_count": len(accepted),
        "best": ({
            key: best[key]
            for key in (
                "rows", "gap", "factor", "rank", "nullity",
                "control_coordinate_linf", "minimum_topology_margin",
                "endpoint_residual_ratios", "volumes", "files",
            )
        } if best is not None else None),
        "output": str(output),
    }, indent=2))


if __name__ == "__main__":
    main()
