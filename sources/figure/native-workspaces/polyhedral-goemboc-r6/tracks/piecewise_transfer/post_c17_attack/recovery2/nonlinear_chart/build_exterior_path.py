#!/usr/bin/env python3
"""Construct an exact degree-two path outside the frozen-plane chart.

The fixed-plane proposal supplies a certified useful tangent seed.  One exact
moving-frame mode is normalized in physical L-infinity norm and added with a
small rational coefficient.  All 38 directed signs and the nonzero plane
quotient are checked exactly before the path is written.
"""
from __future__ import annotations

import hashlib
import json
import sys
from fractions import Fraction as Q
from pathlib import Path
from types import SimpleNamespace


HERE = Path(__file__).resolve().parent
ATTACK = HERE.parents[1]
MAIN = HERE.parent / "main"
CHART_JSON = HERE / "nonlinear_chart.json"
CHART_VERIFICATION = HERE / "nonlinear_chart_verification.json"
SEED_CSV = MAIN / "fixed_plane_descent_candidate.csv"
SEED_JSON = MAIN / "fixed_plane_descent_proposal.json"
DIRECTION_OUT = HERE / "exterior_direction.json"
PATH_OUT = HERE / "nonlinear_polynomial_path.json"
CHECKPOINT_OUT = HERE / "nonlinear_path_t1.csv"
sys.path.insert(0, str(HERE))
sys.path.insert(0, str(ATTACK))

import build_nonlinear_chart as chart  # noqa: E402
import post_c17_exact as pc  # noqa: E402


EPSILON = Q(1, 10**12)


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def dot(left, right):
    return sum((a * b for a, b in zip(left, right)), Q(0))


def solve_coordinates(vector, u, v):
    uu, uv, vv = pc.ex.dot(u, u), pc.ex.dot(u, v), pc.ex.dot(v, v)
    wu, wv = pc.ex.dot(vector, u), pc.ex.dot(vector, v)
    determinant = uu * vv - uv * uv
    assert determinant > 0
    alpha = (wu * vv - wv * uv) / determinant
    beta = (wv * uu - wu * uv) / determinant
    assert vector == pc.ex.add(pc.ex.mul(u, alpha), pc.ex.mul(v, beta))
    return alpha, beta


def mode_index(modes):
    result = {mode["name"]: index for index, mode in enumerate(modes)}
    assert len(result) == len(modes)
    return result


def plane_quotient(rows, coefficient, modes, base, shell):
    physical = physical_derivative(coefficient, modes, rows)
    result = {}
    for polygon, prefix in ((base, "base"), (shell, "shell")):
        a, b, c = polygon["frame"]
        normal = pc.ex.cross(pc.ex.sub(rows[b], rows[a]), pc.ex.sub(rows[c], rows[a]))
        assert normal != pc.ex.ZERO
        result[prefix] = [pc.ex.dot(normal, physical[label]) for label in (a, b, c)]
    return result


def physical_derivative(coefficient, modes, rows):
    result = {label: [Q(0), Q(0), Q(0)] for label in rows}
    for scale, mode in zip(coefficient, modes):
        if not scale:
            continue
        for label, vector in mode["deltas"].items():
            for axis in range(3):
                result[label][axis] += scale * vector[axis]
    return {label: tuple(vector) for label, vector in result.items()}


def seed_coefficients(source, seed, modes, base, shell, free):
    index = mode_index(modes)
    coefficient = [Q(0)] * len(modes)
    delta = {label: pc.ex.sub(seed[label], source[label]) for label in source}
    active = set(chart.BASE) | set(chart.SHELL) | set(free)
    assert all(delta[label] == pc.ex.ZERO for label in set(source) - active)
    for polygon, prefix in ((base, "base"), (shell, "shell")):
        a, b, c = polygon["frame"]
        for role, label in zip("abc", (a, b, c)):
            for axis, axis_name in enumerate("xyz"):
                coefficient[index[f"{prefix}_frame_{role}{label}_{axis_name}"]] = delta[label][axis]
        u = pc.ex.sub(source[b], source[a])
        v = pc.ex.sub(source[c], source[a])
        affine = {int(label): tuple(Q(value) for value in pair) for label, pair in polygon["affine_coordinates_exact"].items()}
        for label in polygon["dependent_rows"]:
            alpha, beta = affine[label]
            frame_part = pc.ex.add(
                delta[a],
                pc.ex.add(
                    pc.ex.mul(pc.ex.sub(delta[b], delta[a]), alpha),
                    pc.ex.mul(pc.ex.sub(delta[c], delta[a]), beta),
                ),
            )
            residual = pc.ex.sub(delta[label], frame_part)
            d_alpha, d_beta = solve_coordinates(residual, u, v)
            coefficient[index[f"{prefix}_r{label}_alpha"]] = d_alpha
            coefficient[index[f"{prefix}_r{label}_beta"]] = d_beta
    for label in free:
        for axis, axis_name in enumerate("xyz"):
            coefficient[index[f"free_r{label}_{axis_name}"]] = delta[label][axis]
    assert physical_derivative(coefficient, modes, source) == delta
    return coefficient, delta


def padd(left, right):
    size = max(len(left), len(right))
    out = [Q(0)] * size
    for index in range(size):
        out[index] = (left[index] if index < len(left) else 0) + (right[index] if index < len(right) else 0)
    while len(out) > 1 and out[-1] == 0:
        out.pop()
    return tuple(out)


def pneg(value):
    return tuple(-entry for entry in value)


def psub(left, right):
    return padd(left, pneg(right))


def pmul(left, right):
    out = [Q(0)] * (len(left) + len(right) - 1)
    for i, a in enumerate(left):
        for j, b in enumerate(right):
            out[i + j] += a * b
    while len(out) > 1 and out[-1] == 0:
        out.pop()
    return tuple(out)


def vadd(left, right):
    return tuple(padd(left[axis], right[axis]) for axis in range(3))


def vsub(left, right):
    return tuple(psub(left[axis], right[axis]) for axis in range(3))


def vscale(vector, scalar):
    return tuple(pmul(vector[axis], scalar) for axis in range(3))


def vcross(left, right):
    return (
        psub(pmul(left[1], right[2]), pmul(left[2], right[1])),
        psub(pmul(left[2], right[0]), pmul(left[0], right[2])),
        psub(pmul(left[0], right[1]), pmul(left[1], right[0])),
    )


def vdot(left, right):
    return padd(padd(pmul(left[0], right[0]), pmul(left[1], right[1])), pmul(left[2], right[2]))


def polynomial_path(rows, coefficient, modes, base, shell):
    derivative = physical_derivative(coefficient, modes, rows)
    index = mode_index(modes)
    path = {
        label: tuple((point[axis], derivative[label][axis]) for axis in range(3))
        for label, point in rows.items()
    }
    for polygon, prefix in ((base, "base"), (shell, "shell")):
        a_label, b_label, c_label = polygon["frame"]
        a = path[a_label]
        b = path[b_label]
        c = path[c_label]
        affine = {int(label): tuple(Q(value) for value in pair) for label, pair in polygon["affine_coordinates_exact"].items()}
        for label in polygon["dependent_rows"]:
            alpha, beta = affine[label]
            alpha_path = (alpha, coefficient[index[f"{prefix}_r{label}_alpha"]])
            beta_path = (beta, coefficient[index[f"{prefix}_r{label}_beta"]])
            path[label] = vadd(
                a,
                vadd(vscale(vsub(b, a), alpha_path), vscale(vsub(c, a), beta_path)),
            )
            assert tuple(component[0] for component in path[label]) == rows[label]
            assert tuple(component[1] if len(component) > 1 else Q(0) for component in path[label]) == derivative[label]
        normal = vcross(vsub(b, a), vsub(c, a))
        for label in polygon["dependent_rows"]:
            assert vdot(normal, vsub(path[label], a)) == (Q(0),)
    assert any(len(component) == 3 and component[2] for xyz in path.values() for component in xyz)
    return path


def evaluate_path(path, parameter):
    return {
        label: tuple(
            sum((coefficient * parameter**power for power, coefficient in enumerate(component)), Q(0))
            for component in xyz
        )
        for label, xyz in path.items()
    }


def checkpoint(rows, cycles):
    faces = pc.ex.exactify_faces(
        rows, SimpleNamespace(faces=[{"cycle": list(cycle)} for cycle in cycles])
    )
    volume, centroid = pc.ex.exact_mass(rows, faces)
    edges, active, _fl, _vl, _el, stable, unstable, saddles = pc.ex.exact_mechanics(
        rows, faces, centroid
    )
    assert [len(active), len(edges), len(faces)] == [61, 150, 91]
    assert [len(stable), len(unstable), len(saddles)] == [2, 4, 4]
    assert not (pc.esc.forced_rails() - set(edges))
    return faces, {
        "f_vector": [len(active), len(edges), len(faces)],
        "class": [len(stable), len(unstable), len(saddles)],
        "stable_faces": [faces[index]["cycle"] for index in stable],
        "unstable_vertices": unstable,
        "saddle_edges": [list(edge) for edge in saddles],
        "volume_exact": pc.qs(volume),
        "centroid_exact": [pc.qs(value) for value in centroid],
        "all_37_forced_rails_present": True,
    }


def main():
    chart_payload = json.loads(CHART_JSON.read_text())
    verification = json.loads(CHART_VERIFICATION.read_text())
    seed_payload = json.loads(SEED_JSON.read_text())
    assert chart_payload["verdict"] == "EXACT_POST_C17_NONLINEAR_156D_CHART_PASS"
    assert verification["verdict"] == "INDEPENDENT_EXACT_POST_C17_NONLINEAR_156D_CHART_PASS"
    assert seed_payload["verdict"] == "RATIONAL_POST_C17_FIXED_PLANE_DESCENT_PROPOSAL_PASS"
    ledger, source, faces = chart.load_frozen_endpoint()
    modes, base, shell, free = chart.build_modes(source, tuple(ledger["active_vertices"]))
    seed = pc.read_rows(SEED_CSV)
    seed_coefficient, _seed_delta = seed_coefficients(source, seed, modes, base, shell, free)

    dense = chart_payload["dense_exact_jets"]
    jet_rows = [
        tuple(Q(value) for value in record["gradient_exact"])
        for record in dense["P"] + dense["T"]
    ]
    assert len(jet_rows) == 38 and pc.rj.matrix_rank(jet_rows) == 38

    mode_by_name = mode_index(modes)
    base_frame = base["frame"]
    base_normal = pc.ex.cross(
        pc.ex.sub(source[base_frame[1]], source[base_frame[0]]),
        pc.ex.sub(source[base_frame[2]], source[base_frame[0]]),
    )
    exterior_axis = max(range(3), key=lambda axis: abs(base_normal[axis]))
    exterior = [Q(0)] * len(modes)
    exterior_name = f"base_frame_a{base_frame[0]}_{'xyz'[exterior_axis]}"
    exterior[mode_by_name[exterior_name]] = 1
    exterior_physical = physical_derivative(exterior, modes, source)
    exterior_norm = max(
        abs(value) for vector in exterior_physical.values() for value in vector
    )
    assert exterior_norm > 0
    exterior = [value / exterior_norm for value in exterior]
    seed_derivatives = [dot(jet, seed_coefficient) for jet in jet_rows]
    exterior_derivatives = [dot(jet, exterior) for jet in jet_rows]
    adverse_bounds = [
        seed / -outside
        for seed, outside in zip(seed_derivatives[:30], exterior_derivatives[:30])
        if outside < 0
    ] + [
        -seed / outside
        for seed, outside in zip(seed_derivatives[30:], exterior_derivatives[30:])
        if outside > 0
    ]
    sign_safety_bound = min(adverse_bounds)
    assert sign_safety_bound > 2 * EPSILON
    direction = [
        seed + EPSILON * outside
        for seed, outside in zip(seed_coefficient, exterior)
    ]

    seed_quotient = plane_quotient(source, seed_coefficient, modes, base, shell)
    exterior_quotient = plane_quotient(source, exterior, modes, base, shell)
    direction_quotient = plane_quotient(source, direction, modes, base, shell)
    assert all(value == 0 for values in seed_quotient.values() for value in values)
    assert any(value != 0 for values in exterior_quotient.values() for value in values)
    assert any(value != 0 for values in direction_quotient.values() for value in values)

    p_derivatives = [dot(jet, direction) for jet in jet_rows[:30]]
    t_derivatives = [dot(jet, direction) for jet in jet_rows[30:]]
    assert all(value > 0 for value in p_derivatives)
    assert all(value < 0 for value in t_derivatives)

    path = polynomial_path(source, direction, modes, base, shell)
    checkpoint_rows = evaluate_path(path, Q(1))
    checkpoint_faces, checkpoint_record = checkpoint(
        checkpoint_rows, ledger["maximal_face_cycles"]
    )
    source_p, source_t = chart.mechanics_jets(source, faces, [])
    point_p, point_t = chart.mechanics_jets(checkpoint_rows, checkpoint_faces, [])
    source_p = dict(source_p)
    source_t = dict(source_t)
    point_p = dict(point_p)
    point_t = dict(point_t)
    p_ratios = {name: point_p[name].v / source_p[name].v for name in source_p}
    t_ratios = {name: point_t[name].v / source_t[name].v for name in source_t}
    assert all(ratio > 1 for ratio in p_ratios.values())
    assert all(Q(0) < ratio < 1 for ratio in t_ratios.values())
    pc.write_rows(CHECKPOINT_OUT, checkpoint_rows)

    direction_payload = {
        "version": 1,
        "scope": "exact 156D direction strictly outside the frozen-plane tangent chart",
        "source_hashes": {
            "nonlinear_chart.json": sha256(CHART_JSON),
            "nonlinear_chart_verification.json": sha256(CHART_VERIFICATION),
            str(SEED_CSV.relative_to(ATTACK)): sha256(SEED_CSV),
            str(SEED_JSON.relative_to(ATTACK)): sha256(SEED_JSON),
        },
        "construction": {
            "seed": "exact tangent inverse of the accepted fixed-plane proposal",
            "exterior_mode": exterior_name,
            "exterior_physical_linf_normalized_to": "1",
            "epsilon_exact": pc.qs(EPSILON),
            "exact_directed_sign_safety_bound": pc.qs(sign_safety_bound),
            "epsilon_below_half_sign_safety_bound": True,
        },
        "mode_names": [mode["name"] for mode in modes],
        "seed_coefficients_exact": [pc.qs(value) for value in seed_coefficient],
        "exterior_unit_coefficients_exact": [pc.qs(value) for value in exterior],
        "direction_coefficients_exact": [pc.qs(value) for value in direction],
        "plane_normal_velocity_quotient_exact": {
            prefix: [pc.qs(value) for value in values]
            for prefix, values in direction_quotient.items()
        },
        "outside_fixed_plane_chart_exact": True,
        "P_directed_derivatives_exact": [pc.qs(value) for value in p_derivatives],
        "T_directed_derivatives_exact": [pc.qs(value) for value in t_derivatives],
        "all_30_P_strictly_increase_to_first_order": True,
        "all_8_T_strictly_decrease_to_first_order": True,
        "verdict": "EXACT_POST_C17_EXTERIOR_DIRECTION_PASS",
        "winner_status": "NONWINNER_DIRECTION_ONLY",
    }
    DIRECTION_OUT.write_text(json.dumps(direction_payload, indent=2) + "\n")

    path_payload = {
        "version": 1,
        "scope": "rational degree-two active-hull coplanarity path",
        "source_hashes": {
            "cells/endpoint.csv": sha256(ATTACK / "cells" / "endpoint.csv"),
            "exterior_direction.json": sha256(DIRECTION_OUT),
        },
        "formula": "chart coordinates theta(t)=t*d; moving-frame affine-coordinate map",
        "coordinate_polynomials_exact_ascending": {
            str(label): [[pc.qs(value) for value in component] for component in xyz]
            for label, xyz in sorted(path.items())
        },
        "maximum_coordinate_degree": max(
            len(component) - 1 for xyz in path.values() for component in xyz
        ),
        "base_coplanarity_identical": True,
        "shell_coplanarity_identical": True,
        "outside_fixed_plane_chart_exact": True,
        "t1_checkpoint": {
            "csv": str(CHECKPOINT_OUT.relative_to(ATTACK)),
            "csv_sha256": sha256(CHECKPOINT_OUT),
            **checkpoint_record,
            "P_ratios_exact": {name: pc.qs(value) for name, value in p_ratios.items()},
            "T_ratios_exact": {name: pc.qs(value) for name, value in t_ratios.items()},
            "all_30_P_strictly_larger": True,
            "all_8_T_strictly_smaller": True,
        },
        "verdict": "EXACT_POST_C17_NONLINEAR_POLYNOMIAL_PATH_MATERIALIZED_PASS",
        "proof_status": "EXACT_T1_CHECKPOINT_FIRST_EVENT_NOT_YET_CERTIFIED",
        "winner_status": "NONWINNER",
    }
    PATH_OUT.write_text(json.dumps(path_payload, indent=2) + "\n")
    print(direction_payload["verdict"])
    print(path_payload["verdict"])
    print("exterior_mode", exterior_name)
    print("maximum_coordinate_degree", path_payload["maximum_coordinate_degree"])
    print("direction_sha256", sha256(DIRECTION_OUT))
    print("path_sha256", sha256(PATH_OUT))


if __name__ == "__main__":
    main()
