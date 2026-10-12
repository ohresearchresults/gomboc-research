#!/usr/bin/env python3
"""Build the exact fixed-plane mechanics-transfer branch atlas.

The numerical LPs in this file are proposers only.  Every value, gradient,
branch ordering, and materialized direction recorded as accepted is checked
again with :class:`fractions.Fraction`.  The later path certificate does not
trust LP status; it reconstructs all 12,363 exact path primitives.
"""
from __future__ import annotations

import hashlib
import itertools
import json
import sys
from fractions import Fraction as Q
from pathlib import Path

import numpy as np
from scipy.optimize import linprog


HERE = Path(__file__).resolve().parent
ATTACK = HERE.parents[1]
MAIN = HERE.parent / "main"
SOURCE = ATTACK / "cells" / "endpoint.csv"
LEDGER = ATTACK / "cells" / "endpoint.json"
OUTPUT = HERE / "first_jet_branch_atlas.json"
CANDIDATE = HERE / "transfer_direction_endpoint.csv"
sys.path.insert(0, str(MAIN))
sys.path.insert(0, str(ATTACK))

import build_full_chart as chart  # noqa: E402
import post_c17_exact as pc  # noqa: E402
import propose_fixed_plane_descent as proposer  # noqa: E402


TRIANGLE = (229, 247, 231)
TARGET_EDGE = (231, 247)
TARGET_COMPONENT = "beta1"
TRANSFER_ROWS = (
    {
        "name": "transfer_229_231_beta1",
        "edge": (229, 231),
        "component": "beta1",
        "source_sign": -1,
        "role": "anti-birth blocker",
    },
    {
        "name": "transfer_229_247_beta2",
        "edge": (229, 247),
        "component": "beta2",
        "source_sign": -1,
        "role": "anti-birth blocker",
    },
    {
        "name": "death_H231_247_beta1",
        "edge": TARGET_EDGE,
        "component": TARGET_COMPONENT,
        "source_sign": 1,
        "role": "desired saddle death",
    },
)
EXTRA_STABLE = (228, 264, 246)
EXTRA_UNSTABLE = (228, 231, 246)
EXTRA_SADDLES = ((8, 246), (228, 254), (231, 247), (236, 237))


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def canonical_hash(value) -> str:
    return hashlib.sha256(
        json.dumps(value, sort_keys=True, separators=(",", ":")).encode()
    ).hexdigest()


def qrecord(z):
    return {
        "value_exact": pc.qs(z.v),
        "value_decimal": float(z.v),
        "gradient_exact": [pc.qs(value) for value in z.d],
        "gradient_digest": canonical_hash([pc.qs(value) for value in z.d]),
    }


def rate(z, coefficients):
    derivative = sum((a * b for a, b in zip(z.d, coefficients)), Q(0))
    return -derivative / z.v


def rationalize(vector, scale=Q(1)):
    return [Q(format(float(value), ".17g")) * scale for value in vector]


def displacement(spec, coefficients, labels):
    delta = {label: [Q(0), Q(0), Q(0)] for label in labels}
    for coefficient, (label, _name, direction) in zip(coefficients, spec):
        for axis in range(3):
            delta[label][axis] += coefficient * direction[axis]
    return {label: tuple(values) for label, values in delta.items()}


def signed_component_status(values, linked):
    other = [value.v for name, value in values.items() if name != linked]
    return {
        "other_component_count": len(other),
        "other_negative_component_count": sum(value < 0 for value in other),
        "other_positive_component_count": sum(value > 0 for value in other),
        "other_minimum_exact": pc.qs(min(other)) if other else None,
        "other_minimum_decimal": float(min(other)) if other else None,
    }


def raw_primitive_jets(q, faces):
    """Rebuild the exact 12,363 raw zero-equivalent first jets."""
    zero = pc.rj.J.c(0)
    d6 = zero
    m24 = [zero, zero, zero]
    for face in faces:
        cycle = face["cycle"]
        for offset in range(1, len(cycle) - 1):
            a, b, c = (q[label] for label in (cycle[0], cycle[offset], cycle[offset + 1]))
            volume6 = pc.rj.jdet(a, b, c)
            d6 += volume6
            for axis in range(3):
                m24[axis] += volume6 * (a[axis] + b[axis] + c[axis])
    assert d6.v > 0
    scale = 4 * d6
    xscaled = {
        label: tuple(scale * q[label][axis] - m24[axis] for axis in range(3))
        for label in q
    }

    def normal(face):
        cycle = face["cycle"]
        anchor = q[cycle[0]]
        for left in range(1, len(cycle) - 1):
            for right in range(left + 1, len(cycle)):
                exact = pc.ex.cross(
                    pc.ex.sub(tuple(value.v for value in q[cycle[left]]), tuple(value.v for value in anchor)),
                    pc.ex.sub(tuple(value.v for value in q[cycle[right]]), tuple(value.v for value in anchor)),
                )
                if exact == pc.ex.ZERO:
                    continue
                candidate = pc.rj.jcross(
                    pc.rj.jsub(q[cycle[left]], anchor),
                    pc.rj.jsub(q[cycle[right]], anchor),
                )
                if pc.ex.dot(exact, face["n"]) < 0:
                    candidate = tuple(-value for value in candidate)
                return candidate
        raise AssertionError(("flat face", cycle))

    normals = [normal(face) for face in faces]
    incidence = pc.esc.incidence(faces)
    neighbors = {label: set() for label in set().union(*(set(face["cycle"]) for face in faces))}
    for a, b in incidence:
        neighbors[a].add(b)
        neighbors[b].add(a)

    rows = [("volume_d6", d6, "mechanics_denominator")]
    labels = set(q)
    for face_index, face in enumerate(faces):
        cycle = face["cycle"]
        anchor = q[cycle[0]]
        n = normals[face_index]
        for witness in sorted(labels - set(cycle)):
            rows.append((
                f"support:f{face_index}:w{witness}",
                pc.rj.jdot(n, pc.rj.jsub(q[witness], anchor)),
                "support",
            ))
        if len(cycle) > 3:
            for offset, current in enumerate(cycle):
                previous = cycle[offset - 1]
                following = cycle[(offset + 1) % len(cycle)]
                rows.append((
                    f"in_face_turn:f{face_index}:v{current}",
                    pc.rj.jdot(
                        pc.rj.jcross(
                            pc.rj.jsub(q[current], q[previous]),
                            pc.rj.jsub(q[following], q[current]),
                        ),
                        n,
                    ),
                    "in_face_turn",
                ))

    face_reference = []
    face_raw = []
    for face_index, face in enumerate(faces):
        cycle = face["cycle"]
        n = normals[face_index]
        nn = pc.rj.jn2(n)
        hbar = pc.rj.jdot(n, xscaled[cycle[0]])
        reference = tuple(
            sum((q[label][axis] for label in cycle), zero) / len(cycle)
            for axis in range(3)
        )
        face_key = tuple(sorted(cycle))
        for a, b in zip(cycle, cycle[1:] + cycle[:1]):
            edge = tuple(sorted((a, b)))
            direction = pc.rj.jsub(q[b], q[a])
            raw = pc.rj.jdot(
                pc.rj.jcross(
                    direction,
                    pc.rj.jsub(pc.rj.jmul(n, hbar), pc.rj.jmul(xscaled[a], nn)),
                ),
                n,
            )
            ref = pc.rj.jdot(
                pc.rj.jcross(direction, pc.rj.jsub(reference, q[a])), n
            )
            face_reference.append((
                f"face_reference:{face_key}:{edge}", ref, "mechanics_denominator"
            ))
            face_raw.append((f"face_raw:{face_key}:{edge}", raw, "face_component"))
    rows.extend(sorted(face_reference, key=lambda item: item[0]))
    rows.extend(sorted(face_raw, key=lambda item: item[0]))

    for vertex in sorted(neighbors):
        for neighbor in sorted(neighbors[vertex]):
            value = -pc.rj.jdot(xscaled[vertex], pc.rj.jsub(q[neighbor], q[vertex]))
            rows.append((f"vertex:{vertex}:{neighbor}", value, "vertex_component"))

    for edge in sorted(incidence):
        i, j = edge
        direction = pc.rj.jsub(q[j], q[i])
        dd = pc.rj.jn2(direction)
        t = -pc.rj.jdot(xscaled[i], direction)
        inc = incidence[edge]
        n1, n2 = normals[inc[0]], normals[inc[1]]
        aa, ab, cc = pc.rj.jn2(n1), pc.rj.jdot(n1, n2), pc.rj.jn2(n2)
        r1, r2 = pc.rj.jdot(xscaled[i], n1), pc.rj.jdot(xscaled[i], n2)
        values = {
            "direction_norm2": dd,
            "gram": aa * cc - ab * ab,
            "t": t,
            "one_minus_t": scale * dd - t,
            "beta1": r1 * cc - r2 * ab,
            "beta2": r2 * aa - r1 * ab,
        }
        for component in (
            "direction_norm2", "gram", "t", "one_minus_t", "beta1", "beta2"
        ):
            rows.append((f"edge:{edge}:{component}", values[component], "edge_component"))

    counts = {
        family: sum(item[2] == family for item in rows)
        for family in sorted({item[2] for item in rows})
    }
    assert len(rows) == 12363, (len(rows), counts)
    assert counts == {
        "edge_component": 900,
        "face_component": 300,
        "in_face_turn": 33,
        "mechanics_denominator": 301,
        "support": 10529,
        "vertex_component": 300,
    }
    assert all(value.v != 0 for _name, value, _family in rows)
    return rows, counts


def transfer_partner(edge, component, faces, incidence):
    i, j = edge
    if component == "t":
        return {"kind": "vertex", "vertex": i, "neighbor": j}
    if component == "one_minus_t":
        return {"kind": "vertex", "vertex": j, "neighbor": i}
    face_index = incidence[edge][1 if component == "beta1" else 0]
    return {
        "kind": "face",
        "face_index": face_index,
        "face": list(faces[face_index]["cycle"]),
        "edge": list(edge),
    }


def full_extra_branch_atlas(q, centroid, faces, incidence, packet):
    """Enumerate every defining component of the literal extra block.

    There are 3 face branches, 19+6+5 vertex branches, and 4*4 edge
    branches: 49 exact first-jet branches in total.  Each row names the
    zero-equivalent adjacent mechanics primitive and records whether that
    adjacent feature is already an equilibrium and how many additional sign
    blockers prevent a compensating birth.
    """
    stable_keys = {tuple(sorted(face)) for face in packet["stable_faces"]}
    unstable = set(packet["unstable_vertices"])
    saddles = {tuple(edge) for edge in packet["saddle_edges"]}
    face_values = {}
    for face_index, face in enumerate(faces):
        face_values[face_index] = {
            tuple(sorted(edge)): value
            for edge, value in pc.rj.face_components(face, q, centroid)
        }
    neighbors = {label: set() for label in packet["active_vertices"]}
    for a, b in incidence:
        neighbors[a].add(b)
        neighbors[b].add(a)
    edge_values = {
        edge: pc.rj.edge_components(edge, incidence[edge], faces, q, centroid)
        for edge in incidence
    }
    vertex_values = {
        vertex: {
            neighbor: pc.rj.vertex_support(vertex, neighbor, q, centroid)
            for neighbor in sorted(neighbors[vertex])
        }
        for vertex in neighbors
    }

    records = []
    extra_face_index = next(
        index
        for index, face in enumerate(faces)
        if tuple(sorted(face["cycle"])) == tuple(sorted(EXTRA_STABLE))
    )
    for edge, value in face_values[extra_face_index].items():
        inc = incidence[edge]
        component = "beta2" if inc[0] == extra_face_index else "beta1"
        partner_values = edge_values[edge]
        records.append({
            "branch": f"S{tuple(sorted(EXTRA_STABLE))}:{edge}",
            "owner_kind": "stable_face",
            "owner": list(EXTRA_STABLE),
            "component": list(edge),
            "component_jet": qrecord(value),
            "linked_zero_primitive": {
                "kind": "edge",
                "edge": list(edge),
                "component": component,
                "equilibrium_at_source": edge in saddles,
                **signed_component_status(partner_values, component),
            },
        })

    for vertex in EXTRA_UNSTABLE:
        for neighbor, value in vertex_values[vertex].items():
            edge = tuple(sorted((vertex, neighbor)))
            component = "t" if vertex == edge[0] else "one_minus_t"
            partner_values = edge_values[edge]
            records.append({
                "branch": f"U{vertex}:{neighbor}",
                "owner_kind": "unstable_vertex",
                "owner": vertex,
                "component": neighbor,
                "component_jet": qrecord(value),
                "linked_zero_primitive": {
                    "kind": "edge",
                    "edge": list(edge),
                    "component": component,
                    "equilibrium_at_source": edge in saddles,
                    **signed_component_status(partner_values, component),
                },
            })

    for edge in EXTRA_SADDLES:
        values = edge_values[edge]
        for component in ("t", "one_minus_t", "beta1", "beta2"):
            partner = transfer_partner(edge, component, faces, incidence)
            if partner["kind"] == "vertex":
                owner = partner["vertex"]
                linked = partner["neighbor"]
                status = signed_component_status(vertex_values[owner], linked)
                partner["equilibrium_at_source"] = owner in unstable
            else:
                owner = partner["face_index"]
                linked = edge
                status = signed_component_status(face_values[owner], linked)
                partner["equilibrium_at_source"] = (
                    tuple(sorted(faces[owner]["cycle"])) in stable_keys
                )
            partner.update(status)
            records.append({
                "branch": f"H{edge}:{component}",
                "owner_kind": "saddle_edge",
                "owner": list(edge),
                "component": component,
                "component_jet": qrecord(values[component]),
                "linked_zero_primitive": partner,
            })
    assert len(records) == 49
    return records, face_values, edge_values, vertex_values


def scaled_lp(c, a_ub, b_ub, bounds):
    matrix = np.asarray(a_ub, dtype=float)
    rhs = np.asarray(b_ub, dtype=float)
    coefficient_scale = np.max(np.abs(matrix), axis=1)
    row_scale = np.maximum.reduce(
        (coefficient_scale, np.abs(rhs), np.full(len(rhs), 1e-30))
    )
    return linprog(
        np.asarray(c, dtype=float),
        A_ub=matrix / row_scale[:, None],
        b_ub=rhs / row_scale,
        bounds=bounds,
        method="highs-ds",
        options={
            "primal_feasibility_tolerance": 1e-9,
            "dual_feasibility_tolerance": 1e-9,
        },
    )


def order_branch(permutation, jets, physical, protected_rows):
    modes = physical.shape[1]
    approach = {
        name: -np.asarray([float(value / jet.v) for value in jet.d])
        for name, jet in jets.items()
    }
    first, second, third = permutation
    a_ub = []
    b_ub = []
    # delta <= first rate; delta <= first-second; delta <= second-third.
    a_ub.append(np.r_[-approach[first], 1.0])
    b_ub.append(0.0)
    a_ub.append(np.r_[approach[second] - approach[first], 1.0])
    b_ub.append(0.0)
    a_ub.append(np.r_[approach[third] - approach[second], 1.0])
    b_ub.append(0.0)
    for gradient in protected_rows:
        a_ub.append(np.r_[-gradient, 0.0])
        b_ub.append(0.0)
    a_ub.extend(np.c_[physical, np.zeros(physical.shape[0])])
    b_ub.extend(np.ones(physical.shape[0]))
    a_ub.extend(np.c_[-physical, np.zeros(physical.shape[0])])
    b_ub.extend(np.ones(physical.shape[0]))
    lp = scaled_lp(
        np.r_[np.zeros(modes), -1.0],
        a_ub,
        b_ub,
        [(None, None)] * modes + [(0.0, None)],
    )
    record = {
        "ordering": list(permutation),
        "solver_success": bool(lp.success),
        "solver_status": int(lp.status),
        "solver_message": str(lp.message),
    }
    if not lp.success:
        record["proof_status"] = "NUMERICAL_FAILURE_IS_NOT_AN_OBSTRUCTION"
        return record
    coefficients = rationalize(lp.x[:-1], Q(1, 2))
    rates = {name: rate(jet, coefficients) for name, jet in jets.items()}
    exact = (
        rates[first] > rates[second] > rates[third]
        and rates[first] > 0
    )
    record.update({
        "solver_order_margin": float(lp.x[-1]),
        "exact_rational_direction": [pc.qs(value) for value in coefficients],
        "exact_approach_rates": {name: pc.qs(value) for name, value in rates.items()},
        "decimal_approach_rates": {name: float(value) for name, value in rates.items()},
        "exact_order_verified": exact,
        "direction_digest": canonical_hash([pc.qs(value) for value in coefficients]),
    })
    if not exact:
        raise AssertionError((permutation, rates))
    return record


def safe_target_direction(jets, spec, physical, primitive_jets):
    modes = len(spec)
    target_name = "death_H231_247_beta1"
    raw_target_name = "edge:(231, 247):beta1"
    linked_face_name = "face_raw:(229, 231, 247):(231, 247)"
    lookup = {name: value for name, value, _family in primitive_jets}
    target = lookup[raw_target_name]
    target_rate = -np.asarray([float(value / target.v) for value in target.d])
    allowed = {raw_target_name, linked_face_name}

    # Demand a literal global first-jet lead over every other raw support,
    # turn, volume, reference, face, vertex and edge primitive.  The solver
    # uses a stricter factor than the exact readback, leaving rationalization
    # room instead of interpreting tolerance as proof.
    solution = None
    solver_factor = None
    for factor in (0.50, 0.70, 0.85, 0.95):
        a_ub = []
        b_ub = []
        for name, value, _family in primitive_jets:
            if name in allowed:
                continue
            other_rate = -np.asarray([float(item / value.v) for item in value.d])
            a_ub.append(other_rate - factor * target_rate)
            b_ub.append(0.0)
        a_ub.append(-target_rate)
        b_ub.append(0.0)
        a_ub.extend(physical)
        b_ub.extend(np.ones(physical.shape[0]))
        a_ub.extend(-physical)
        b_ub.extend(np.ones(physical.shape[0]))
        lp = scaled_lp(
            -target_rate,
            a_ub,
            b_ub,
            [(None, None)] * modes,
        )
        if lp.success and float(target_rate @ lp.x) > 0:
            solution = lp
            solver_factor = factor
            break
    if solution is None:
        return {
            "solver_success": False,
            "proof_status": "NUMERICAL_FAILURE_IS_NOT_AN_OBSTRUCTION",
            "attempted_competitor_factors": [0.50, 0.70, 0.85, 0.95],
        }, None
    lp = solution
    # Keep the direction endpoint deep inside the source cell.  The later
    # locator works projectively and is not limited by this parameter scale.
    coefficients = rationalize(lp.x, Q(1, 10_000))
    rates = {name: rate(jet, coefficients) for name, jet in jets.items()}
    assert rates[target_name] > 0
    raw_target_rate = rate(target, coefficients)
    assert raw_target_rate > 0
    verify_factor = Q(str((solver_factor + 1.0) / 2.0))
    competitors = []
    digest = hashlib.sha256()
    for name, value, family in primitive_jets:
        gradient_exact = [pc.qs(item) for item in value.d]
        digest.update(
            f"{name}|{family}|{pc.qs(value.v)}|{'|'.join(gradient_exact)}\n".encode()
        )
        if name in allowed:
            continue
        item_rate = rate(value, coefficients)
        if item_rate > verify_factor * raw_target_rate:
            raise AssertionError((name, item_rate, raw_target_rate, verify_factor))
        competitors.append((item_rate, name, family))
    competitors.sort(reverse=True)
    delta = displacement(spec, coefficients, sorted({row for row, _, _ in spec}))
    physical_linf = max(abs(value) for xyz in delta.values() for value in xyz)
    return {
        "solver_success": True,
        "solver_target_fractional_rate": float(target_rate @ lp.x),
        "solver_competitor_factor": solver_factor,
        "exact_verified_competitor_factor": pc.qs(verify_factor),
        "exact_coefficients": [pc.qs(value) for value in coefficients],
        "exact_approach_rates": {name: pc.qs(value) for name, value in rates.items()},
        "decimal_approach_rates": {name: float(value) for name, value in rates.items()},
        "raw_target_name": raw_target_name,
        "raw_linked_zero_family": sorted(allowed),
        "raw_target_approach_rate_exact": pc.qs(raw_target_rate),
        "raw_target_approach_rate_decimal": float(raw_target_rate),
        "globally_ordered_other_primitive_count": len(competitors),
        "maximum_other_over_target_rate_decimal": float(competitors[0][0] / raw_target_rate),
        "top_other_approach_rates": [
            {
                "name": name,
                "family": family,
                "rate_exact": pc.qs(item_rate),
                "rate_decimal": float(item_rate),
                "over_target_decimal": float(item_rate / raw_target_rate),
            }
            for item_rate, name, family in competitors[:30]
        ],
        "exact_global_12363_first_jet_target_order": True,
        "primitive_first_jet_digest": digest.hexdigest(),
        "physical_linf_exact": pc.qs(physical_linf),
        "physical_linf_decimal": float(physical_linf),
        "direction_digest": canonical_hash([pc.qs(value) for value in coefficients]),
    }, coefficients


def main():
    packet, rows, faces, centroid = chart.load_frozen_endpoint()
    assert packet["f_vector"] == [61, 150, 91]
    assert packet["class"] == [2, 4, 4]
    spec, _basis = chart.build_spec(rows, tuple(packet["active_vertices"]))
    q, jet_centroid, mechanics = proposer.mechanics_records(
        rows, faces, packet, spec
    )
    assert all(jet_centroid[k].v == centroid[k] for k in range(3))
    incidence = pc.esc.incidence(faces)
    full_atlas, face_values, edge_values, vertex_values = full_extra_branch_atlas(
        q, jet_centroid, faces, incidence, packet
    )
    primitive_jets, primitive_family_counts = raw_primitive_jets(q, faces)

    triangle_face_index = next(
        index for index, face in enumerate(faces)
        if tuple(face["cycle"]) == TRIANGLE
    )
    triangle_face = face_values[triangle_face_index]
    jets = {
        row["name"]: edge_values[row["edge"]][row["component"]]
        for row in TRANSFER_ROWS
    }
    for row in TRANSFER_ROWS:
        assert (jets[row["name"]].v > 0) == (row["source_sign"] > 0)

    physical = proposer.displacement_matrix(tuple(packet["active_vertices"]), spec)
    protected_rows = []
    for record in mechanics:
        identifier = record["id"]
        if (
            identifier[0] == "S" and identifier[1] == tuple(chart.BASE)
        ) or (identifier[0] == "U" and identifier[1] == 8):
            protected_rows.append(np.asarray([float(value) for value in record["value"].d]))
    support_guards, support_summary = proposer.support_and_turn_guards(
        rows, faces, q, limit=500, threshold=5e-3
    )
    protected_rows.extend(
        np.asarray([float(value) for value in record["value"].d])
        for record in support_guards
    )
    ordering_atlas = [
        order_branch(permutation, jets, physical, protected_rows)
        for permutation in itertools.permutations(jets)
    ]
    assert len(ordering_atlas) == 6
    assert all(record.get("exact_order_verified") for record in ordering_atlas)

    candidate_record, coefficients = safe_target_direction(
        jets, spec, physical, primitive_jets
    )
    if coefficients is None:
        raise RuntimeError(candidate_record)
    delta = displacement(spec, coefficients, packet["active_vertices"])
    candidate = {
        label: pc.ex.add(point, delta.get(label, pc.ex.ZERO))
        for label, point in rows.items()
    }
    pc.write_rows(CANDIDATE, candidate)
    candidate_faces = pc.ex.exactify_faces(candidate, pc.ex.numeric_faces(candidate))
    assert pc.face_signature(candidate_faces) == pc.face_signature(faces)
    candidate_record.update({
        "csv": str(CANDIDATE.relative_to(ATTACK)),
        "csv_sha256": sha256(CANDIDATE),
        "source_to_candidate_is_direction_only_not_an_accepted_segment": True,
    })

    desired = next(
        row for row in full_atlas
        if row["branch"] == "H(231, 247):beta1"
    )
    assert desired["linked_zero_primitive"]["kind"] == "face"
    assert desired["linked_zero_primitive"]["equilibrium_at_source"] is False
    assert desired["linked_zero_primitive"]["other_negative_component_count"] == 2

    payload = {
        "version": 1,
        "scope": (
            "complete exact 150-mode fixed-plane first-jet atlas for all 49 "
            "defining branches of the post-C17 extra equilibrium block, plus "
            "the complete six-order local transfer fan around face (229,247,231)"
        ),
        "source_hashes": {
            str(SOURCE.relative_to(ATTACK)): sha256(SOURCE),
            str(LEDGER.relative_to(ATTACK)): sha256(LEDGER),
            "recovery2/main/full_chart.json": sha256(MAIN / "full_chart.json"),
        },
        "endpoint": {
            "f_vector": packet["f_vector"],
            "class": packet["class"],
            "mode_count": len(spec),
            "active_rows": packet["active_vertices"],
            "base": list(chart.BASE),
            "shell": list(chart.SHELL),
            "all_37_forced_rails_present": True,
        },
        "mode_names": [name for _row, name, _direction in spec],
        "complete_raw_first_jet_primitive_count": len(primitive_jets),
        "complete_raw_first_jet_family_counts": primitive_family_counts,
        "full_extra_block_branch_count": len(full_atlas),
        "full_extra_block_branches": full_atlas,
        "local_transfer_fan": {
            "face_index": triangle_face_index,
            "face": list(TRIANGLE),
            "components": {
                row["name"]: {
                    **row,
                    "jet": qrecord(jets[row["name"]]),
                }
                for row in TRANSFER_ROWS
            },
            "face_component_jets": {
                f"{edge[0]},{edge[1]}": qrecord(value)
                for edge, value in triangle_face.items()
            },
            "ordering_branch_count": len(ordering_atlas),
            "all_six_strict_orderings_have_exact_rational_witnesses": True,
            "ordering_branches": ordering_atlas,
        },
        "named_connections": {
            "U231_via_232": {
                "jet": qrecord(vertex_values[231][232]),
                "linked_edge_component": "edge:(231,232):t",
            },
            "U246_via_245": {
                "jet": qrecord(vertex_values[246][245]),
                "linked_edge_component": "edge:(245,246):one_minus_t",
            },
            "H8_246_t": {
                "jet": qrecord(edge_values[(8, 246)]["t"]),
                "linked_vertex_component": "U8_via_246",
                "protected_U8_makes_this_death_branch_forbidden": True,
            },
            "H228_254": {
                component: qrecord(edge_values[(228, 254)][component])
                for component in ("t", "one_minus_t", "beta1", "beta2")
            },
            "H231_247": {
                component: qrecord(edge_values[(231, 247)][component])
                for component in ("t", "one_minus_t", "beta1", "beta2")
            },
            "H236_237": {
                component: qrecord(edge_values[(236, 237)][component])
                for component in ("t", "one_minus_t", "beta1", "beta2")
            },
        },
        "support_guard_summary": support_summary,
        "selected_safe_target_direction": candidate_record,
        "verdict": "EXACT_POST_C17_TRANSFER_FIRST_JET_ATLAS_PASS",
        "proof_boundary": (
            "The atlas certifies exact first jets and exact rational branch "
            "ordering witnesses.  Only the separate exhaustive nonlinear "
            "path/event certificate may claim an accepted mechanics transfer."
        ),
        "winner_status": "NONWINNER_ATLAS_ONLY",
    }
    OUTPUT.write_text(json.dumps(payload, indent=2) + "\n")
    print(payload["verdict"])
    print("full_extra_block_branch_count", len(full_atlas))
    print("ordering_branch_count", len(ordering_atlas))
    print("safe_target_rates", candidate_record["decimal_approach_rates"])
    print("candidate_sha256", sha256(CANDIDATE))
    print("atlas_sha256", sha256(OUTPUT))


if __name__ == "__main__":
    main()
