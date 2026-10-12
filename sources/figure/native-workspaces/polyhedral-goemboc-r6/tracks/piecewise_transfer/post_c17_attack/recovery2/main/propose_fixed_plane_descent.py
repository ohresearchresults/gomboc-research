#!/usr/bin/env python3
"""Numerical LP proposer with exact materialization in the post-C17 chart.

This file proposes only.  It does not certify an interval or infer an event
from optimization failure.  Every accepted endpoint is rational and is
rebuilt with its own exact uniform-volume centroid before it is written.
"""
from __future__ import annotations

import hashlib
import json
import sys
from fractions import Fraction as Q
from pathlib import Path

import numpy as np
from scipy.optimize import linprog


HERE = Path(__file__).resolve().parent
ATTACK = HERE.parents[1]
CHART_PATH = HERE / "full_chart.json"
OUTPUT = HERE / "fixed_plane_descent_proposal.json"
ENDPOINT = HERE / "fixed_plane_descent_candidate.csv"
sys.path.insert(0, str(HERE))
sys.path.insert(0, str(ATTACK))

import build_full_chart as chart  # noqa: E402
import post_c17_exact as pc  # noqa: E402


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def mechanics_records(rows, faces, packet, spec):
    q, centroid = pc.make_jets(rows, faces, spec)
    incidence = pc.esc.incidence(faces)
    stable = {
        tuple(sorted(cycle)) for cycle in packet["stable_faces"]
    }
    unstable = set(packet["unstable_vertices"])
    saddles = {tuple(edge) for edge in packet["saddle_edges"]}
    neighbors = {label: set() for label in packet["active_vertices"]}
    for a, b in incidence:
        neighbors[a].add(b)
        neighbors[b].add(a)

    records = []
    for face in faces:
        face_key = tuple(sorted(face["cycle"]))
        components = [
            (tuple(sorted(edge)), value)
            for edge, value in pc.rj.face_components(face, q, centroid)
        ]
        if face_key in stable:
            selected = components
            present = True
        else:
            selected = [min((item for item in components if item[1].v < 0), key=lambda item: item[1].v)]
            present = False
        for edge, value in selected:
            records.append({
                "id": ("S", face_key, edge),
                "kind": "present_stable" if present else "absent_stable_witness",
                "value": value,
            })

    for vertex in packet["active_vertices"]:
        components = [
            (neighbor, pc.rj.vertex_support(vertex, neighbor, q, centroid))
            for neighbor in sorted(neighbors[vertex])
        ]
        if vertex in unstable:
            selected = components
            present = True
        else:
            selected = [min((item for item in components if item[1].v < 0), key=lambda item: item[1].v)]
            present = False
        for neighbor, value in selected:
            records.append({
                "id": ("U", vertex, neighbor),
                "kind": "present_unstable" if present else "absent_unstable_witness",
                "value": value,
            })

    for edge in sorted(incidence):
        components = pc.rj.edge_components(edge, incidence[edge], faces, q, centroid)
        if edge in saddles:
            selected = list(components.items())
            present = True
        else:
            selected = [min(
                ((name, value) for name, value in components.items() if value.v < 0),
                key=lambda item: item[1].v,
            )]
            present = False
        for component, value in selected:
            records.append({
                "id": ("H", edge, component),
                "kind": "present_saddle" if present else "absent_saddle_witness",
                "value": value,
            })
    assert all(record["value"].v != 0 for record in records)
    return q, centroid, records


def target_ids():
    return {
        "S228_264_246_via_246_228": ("S", (228, 246, 264), (228, 246)),
        "U228_via_251": ("U", 228, 251),
        "U231_via_232": ("U", 231, 232),
        "U246_via_245": ("U", 246, 245),
        "H8_246_via_t": ("H", (8, 246), "t"),
        "H228_254_via_beta2": ("H", (228, 254), "beta2"),
        "H231_247_via_beta1": ("H", (231, 247), "beta1"),
        "H236_237_via_beta1": ("H", (236, 237), "beta1"),
    }


def support_and_turn_guards(rows, faces, q, limit=500, threshold=5e-3):
    candidates = []
    all_support_count = 0
    for face_index, face in enumerate(faces):
        cycle = face["cycle"]
        anchor = cycle[0]
        triple = None
        for j in range(1, len(cycle) - 1):
            for k in range(j + 1, len(cycle)):
                if pc.ex.cross(
                    pc.ex.sub(rows[cycle[j]], rows[anchor]),
                    pc.ex.sub(rows[cycle[k]], rows[anchor]),
                ) != pc.ex.ZERO:
                    triple = (anchor, cycle[j], cycle[k])
                    break
            if triple is not None:
                break
        assert triple is not None
        a, b, c = triple
        normal_norm = float(sum(value * value for value in face["n"])) ** 0.5
        for witness, point in rows.items():
            if witness in cycle:
                continue
            slack = face["h"] - pc.ex.dot(face["n"], point)
            assert slack > 0
            distance = float(slack) / normal_norm
            candidates.append((distance, face_index, witness, triple))
            all_support_count += 1
    candidates.sort(key=lambda item: item[:3])
    selected = [item for item in candidates if item[0] <= threshold]
    selected = selected[:limit] if selected else candidates[:limit]

    guards = []
    for distance, face_index, witness, (a, b, c) in selected:
        value = pc.rj.jdet(
            pc.rj.jsub(q[b], q[a]),
            pc.rj.jsub(q[c], q[a]),
            pc.rj.jsub(q[witness], q[a]),
        )
        if value.v < 0:
            value = -value
        assert value.v > 0
        guards.append({
            "id": ("support", face_index, witness),
            "kind": "near_support",
            "distance": distance,
            "value": value,
        })

    turn_count = 0
    for face_index, face in enumerate(faces):
        cycle = face["cycle"]
        if len(cycle) <= 3:
            continue
        normal = tuple(pc.rj.J.c(value) for value in face["n"])
        for offset, current in enumerate(cycle):
            previous = cycle[offset - 1]
            following = cycle[(offset + 1) % len(cycle)]
            value = pc.rj.jdot(
                pc.rj.jcross(
                    pc.rj.jsub(q[current], q[previous]),
                    pc.rj.jsub(q[following], q[current]),
                ),
                normal,
            )
            if value.v < 0:
                value = -value
            assert value.v > 0
            guards.append({
                "id": ("turn", face_index, current),
                "kind": "in_face_turn",
                "distance": None,
                "value": value,
            })
            turn_count += 1
    return guards, {
        "all_support_rows": all_support_count,
        "selected_near_support_rows": len(selected),
        "in_face_turn_rows": turn_count,
        "maximum_selected_distance": max(item[0] for item in selected),
    }


def displacement_matrix(active, spec):
    row_index = {label: offset for offset, label in enumerate(active)}
    matrix = np.zeros((3 * len(active), len(spec)))
    for column, (label, _name, direction) in enumerate(spec):
        offset = row_index[label]
        for axis in range(3):
            matrix[3 * offset + axis, column] = float(direction[axis])
    return matrix


def exact_delta(spec, coefficients, labels):
    delta = {label: [Q(0), Q(0), Q(0)] for label in labels}
    exact_coefficients = [Q(format(float(value), ".12g")) for value in coefficients]
    for coefficient, (label, _name, direction) in zip(exact_coefficients, spec):
        for axis in range(3):
            delta[label][axis] += coefficient * direction[axis]
    return {label: tuple(value) for label, value in delta.items()}, exact_coefficients


def evaluate_exact_candidate(rows, faces, packet, delta, targets0, protected0):
    candidate = {
        label: pc.ex.add(point, delta.get(label, pc.ex.ZERO))
        for label, point in rows.items()
    }
    proposal = pc.ex.numeric_faces(candidate)
    candidate_faces = pc.ex.exactify_faces(candidate, proposal)
    assert pc.face_signature(candidate_faces) == pc.face_signature(faces)
    volume, centroid = pc.ex.exact_mass(candidate, candidate_faces)
    ef, active, fl, vl, el, stable, unstable, saddles = pc.ex.exact_mechanics(
        candidate, candidate_faces, centroid
    )
    candidate_packet = {
        "f_vector": [len(active), len(ef), len(candidate_faces)],
        "class": [len(stable), len(unstable), len(saddles)],
        "stable_faces": [candidate_faces[index]["cycle"] for index in stable],
        "unstable_vertices": unstable,
        "saddle_edges": [list(edge) for edge in saddles],
    }
    assert candidate_packet["f_vector"] == packet["f_vector"]
    assert candidate_packet["class"] == packet["class"]
    assert {tuple(sorted(face)) for face in candidate_packet["stable_faces"]} == {
        tuple(sorted(face)) for face in packet["stable_faces"]
    }
    assert candidate_packet["unstable_vertices"] == packet["unstable_vertices"]
    assert candidate_packet["saddle_edges"] == packet["saddle_edges"]
    assert not (pc.esc.forced_rails() - set(ef))

    candidate_targets, candidate_base, candidate_u8 = chart.target_jets(
        candidate, candidate_faces, []
    )
    ratios = {
        name: candidate_targets[name].v / targets0[name].v
        for name in chart.TARGET_NAMES
    }
    assert all(Q(0) < ratio < Q(1) for ratio in ratios.values())
    protected = {
        **{("S", tuple(sorted(edge))): value.v for edge, value in candidate_base.items()},
        **{("U8", neighbor): value.v for neighbor, value in candidate_u8.items()},
    }
    assert set(protected) == set(protected0)
    assert all(protected[key] >= protected0[key] for key in protected)
    return candidate, candidate_packet, ratios, protected, volume, centroid


def main():
    chart_payload = json.loads(CHART_PATH.read_text())
    assert chart_payload["verdict"] == "EXACT_POST_C17_FIXED_PLANE_FULL_CHART_AUDIT_PASS"
    packet, rows, faces, _ = chart.load_frozen_endpoint()
    spec, _basis = chart.build_spec(rows, tuple(packet["active_vertices"]))
    targets0, base0, u80 = chart.target_jets(rows, faces, spec)
    q, centroid, mechanics = mechanics_records(rows, faces, packet, spec)
    by_id = {record["id"]: record for record in mechanics}
    assert len(by_id) == len(mechanics)
    targets = target_ids()
    assert set(targets) == set(chart.TARGET_NAMES)
    for name, identifier in targets.items():
        assert identifier in by_id
        assert by_id[identifier]["value"].v == targets0[name].v

    protected_ids = {
        record["id"]
        for record in mechanics
        if (record["id"][0] == "S" and record["id"][1] == tuple(chart.BASE))
        or (record["id"][0] == "U" and record["id"][1] == 8)
    }
    protected0 = {
        **{("S", tuple(sorted(edge))): value.v for edge, value in base0.items()},
        **{("U8", neighbor): value.v for neighbor, value in u80.items()},
    }
    assert len(protected_ids) == len(protected0)

    support_guards, support_summary = support_and_turn_guards(rows, faces, q)
    modes = len(spec)
    displacement = displacement_matrix(tuple(packet["active_vertices"]), spec)
    branches = []
    best = None
    target_id_set = set(targets.values())
    trust_values = (1e-9, 3e-9, 1e-8, 3e-8, 1e-7, 3e-7, 1e-6, 3e-6, 1e-5)
    for trust in trust_values:
        a_ub = []
        b_ub = []
        names = []
        for name, identifier in targets.items():
            value = by_id[identifier]["value"]
            a_ub.append(np.r_[np.asarray([float(z / value.v) for z in value.d]), 1.0])
            b_ub.append(0.0)
            names.append(("target", name))
        for record in mechanics:
            value = record["value"]
            if record["id"] in target_id_set:
                continue
            gradient = np.asarray([float(z) for z in value.d])
            if record["id"] in protected_ids:
                a_ub.append(np.r_[-gradient / float(value.v), 0.05])
                b_ub.append(0.0)
                names.append(("protected_strict_improvement", repr(record["id"])))
            else:
                sign = 1.0 if value.v > 0 else -1.0
                a_ub.append(np.r_[-sign * gradient, 0.0])
                b_ub.append(0.2 * abs(float(value.v)))
                names.append(("mechanics_guard", repr(record["id"])))
        for record in support_guards:
            value = record["value"]
            gradient = np.asarray([float(z) for z in value.d])
            a_ub.append(np.r_[-gradient, 0.0])
            b_ub.append(0.2 * float(value.v))
            names.append((record["kind"], repr(record["id"])))
        a_ub.extend(np.c_[displacement, np.zeros(displacement.shape[0])])
        b_ub.extend(np.full(displacement.shape[0], trust))
        names.extend(("physical_plus", index) for index in range(displacement.shape[0]))
        a_ub.extend(np.c_[-displacement, np.zeros(displacement.shape[0])])
        b_ub.extend(np.full(displacement.shape[0], trust))
        names.extend(("physical_minus", index) for index in range(displacement.shape[0]))

        lp = linprog(
            np.r_[np.zeros(modes), -1.0],
            A_ub=np.asarray(a_ub),
            b_ub=np.asarray(b_ub),
            bounds=[(None, None)] * modes + [(0.0, 1.0)],
            method="highs",
        )
        branch = {
            "trust": trust,
            "success": bool(lp.success),
            "message": lp.message,
            "constraint_count": len(a_ub),
        }
        if lp.success:
            coefficients = np.asarray(lp.x[:-1])
            delta, exact_coefficients = exact_delta(
                spec, coefficients, packet["active_vertices"]
            )
            physical_linf = max(abs(float(value)) for vector in delta.values() for value in vector)
            branch.update({
                "common_fractional_descent": float(lp.x[-1]),
                "physical_linf": physical_linf,
                "nonzero_exact_coefficients": sum(value != 0 for value in exact_coefficients),
            })
            try:
                evaluated = evaluate_exact_candidate(
                    rows, faces, packet, delta, targets0, protected0
                )
                candidate, candidate_packet, ratios, protected, volume, candidate_centroid = evaluated
                branch["exact_accept"] = True
                branch["target_ratios_decimal"] = {
                    name: float(ratio) for name, ratio in ratios.items()
                }
                if best is None or lp.x[-1] > best[0]["common_fractional_descent"]:
                    best = (
                        branch,
                        candidate,
                        candidate_packet,
                        ratios,
                        protected,
                        volume,
                        candidate_centroid,
                        exact_coefficients,
                    )
            except Exception as error:
                branch["exact_accept"] = False
                branch["exact_error"] = repr(error)
        branches.append(branch)

    if best is None:
        OUTPUT.write_text(json.dumps({
            "version": 1,
            "scope": "post-C17 fixed-plane full-control numerical proposer",
            "source_hashes": {
                "cells/endpoint.csv": sha256(ATTACK / "cells" / "endpoint.csv"),
                str(CHART_PATH.relative_to(ATTACK)): sha256(CHART_PATH),
            },
            "support_guard_summary": support_summary,
            "mechanics_guard_count": len(mechanics),
            "branches": branches,
            "verdict": "NO_ACCEPTED_EXACT_FIXED_PLANE_DESCENT_PROPOSAL",
            "proof_status": "NUMERICAL_FAILURE_IS_NOT_AN_OBSTRUCTION",
        }, indent=2) + "\n")
        raise RuntimeError("no exact accepted fixed-plane descent proposal")

    (
        best_branch,
        candidate,
        candidate_packet,
        ratios,
        protected,
        volume,
        candidate_centroid,
        exact_coefficients,
    ) = best
    pc.write_rows(ENDPOINT, candidate)
    payload = {
        "version": 1,
        "scope": "rational fixed-plane full-control proposal from frozen post-C17 endpoint",
        "source_hashes": {
            "cells/endpoint.csv": sha256(ATTACK / "cells" / "endpoint.csv"),
            str(CHART_PATH.relative_to(ATTACK)): sha256(CHART_PATH),
        },
        "mode_count": modes,
        "mechanics_guard_count": len(mechanics),
        "support_guard_summary": support_summary,
        "branches": branches,
        "selected_branch": best_branch,
        "exact_coefficients": [pc.qs(value) for value in exact_coefficients],
        "candidate": {
            "csv": str(ENDPOINT.relative_to(ATTACK)),
            "csv_sha256": sha256(ENDPOINT),
            "f_vector": candidate_packet["f_vector"],
            "class": candidate_packet["class"],
            "stable_faces": candidate_packet["stable_faces"],
            "unstable_vertices": candidate_packet["unstable_vertices"],
            "saddle_edges": candidate_packet["saddle_edges"],
            "volume_exact": pc.qs(volume),
            "centroid_exact": [pc.qs(value) for value in candidate_centroid],
            "target_ratios_exact": {name: pc.qs(ratio) for name, ratio in ratios.items()},
            "target_ratios_decimal": {name: float(ratio) for name, ratio in ratios.items()},
            "protected_components_nondecreased_exactly": True,
            "protected_component_count": len(protected),
            "all_37_forced_rails_present": True,
        },
        "verdict": "RATIONAL_POST_C17_FIXED_PLANE_DESCENT_PROPOSAL_PASS",
        "proof_status": "EXACT_ENDPOINT_ONLY_FIRST_EVENT_NOT_YET_CERTIFIED",
        "winner_status": "NONWINNER",
    }
    OUTPUT.write_text(json.dumps(payload, indent=2) + "\n")
    print(payload["verdict"])
    print("common_fractional_descent", best_branch["common_fractional_descent"])
    print("physical_linf", best_branch["physical_linf"])
    print("target_ratios", payload["candidate"]["target_ratios_decimal"])
    print("candidate_sha256", sha256(ENDPOINT))
    print("proposal_sha256", sha256(OUTPUT))


if __name__ == "__main__":
    main()
