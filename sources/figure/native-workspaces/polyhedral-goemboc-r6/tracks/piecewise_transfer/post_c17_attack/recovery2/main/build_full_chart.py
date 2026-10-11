#!/usr/bin/env python3
"""Build the exact fixed-plane full-control chart at the frozen post-C17 endpoint.

This is a chart/audit artifact, not a winner certificate.  Every active row is
controlled.  Vertices of the 17-gon base and 16-gon shell move in two exact
tangent directions of their frozen supporting planes; every other active row
has three Cartesian controls.  Thus every affine path in this chart preserves
both non-triangular maximal faces exactly, rather than only to first order.
"""
from __future__ import annotations

import hashlib
import json
import sys
from fractions import Fraction as Q
from pathlib import Path
from types import SimpleNamespace

import numpy as np


HERE = Path(__file__).resolve().parent
ATTACK = HERE.parents[1]
OUTPUT = HERE / "full_chart.json"
sys.path.insert(0, str(ATTACK))

import post_c17_exact as pc  # noqa: E402


BASE = tuple(range(17))
SHELL = tuple(range(231, 247))
TARGET_NAMES = (
    "S228_264_246_via_246_228",
    "U228_via_251",
    "U231_via_232",
    "U246_via_245",
    "H8_246_via_t",
    "H228_254_via_beta2",
    "H231_247_via_beta1",
    "H236_237_via_beta1",
)


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def load_frozen_endpoint():
    """Rebuild the frozen handoff directly, without replaying its upstream path."""
    ledger_path = ATTACK / "cells" / "endpoint.json"
    rows_path = ATTACK / "cells" / "endpoint.csv"
    ledger = json.loads(ledger_path.read_text())
    rows = pc.read_rows(rows_path)
    faces = pc.ex.exactify_faces(
        rows,
        SimpleNamespace(
            faces=[{"cycle": list(cycle)} for cycle in ledger["maximal_face_cycles"]]
        ),
    )
    volume, centroid = pc.ex.exact_mass(rows, faces)
    ef, active, fl, vl, el, stable, unstable, saddles = pc.ex.exact_mechanics(
        rows, faces, centroid
    )
    assert [len(active), len(ef), len(faces)] == ledger["f_vector"]
    assert len(active) - len(ef) + len(faces) == ledger["euler"] == 2
    assert [len(stable), len(unstable), len(saddles)] == ledger["class"]
    assert active == ledger["active_vertices"]
    assert [faces[index]["cycle"] for index in stable] == ledger["stable_faces"]
    assert unstable == ledger["unstable_vertices"]
    assert [list(edge) for edge in saddles] == ledger["saddle_edges"]
    assert sorted(ef) == [tuple(edge) for edge in ledger["true_edges"]]
    assert fl == ledger["face_mechanics_ledger"]
    assert vl == ledger["vertex_mechanics_ledger"]
    assert el == ledger["edge_mechanics_ledger"]
    assert pc.qs(volume) == ledger["volume_exact"]
    assert [pc.qs(value) for value in centroid] == ledger["centroid_exact"]
    assert not (pc.esc.forced_rails() - set(ef))
    return ledger, rows, faces, centroid


def tangent_basis(rows, cycle):
    anchor = rows[cycle[0]]
    u = pc.ex.sub(rows[cycle[1]], anchor)
    assert u != pc.ex.ZERO
    v = None
    for label in cycle[2:]:
        candidate = pc.ex.sub(rows[label], anchor)
        if pc.ex.cross(u, candidate) != pc.ex.ZERO:
            v = candidate
            break
    assert v is not None
    normal = pc.ex.cross(u, v)
    assert all(pc.ex.dot(normal, pc.ex.sub(rows[label], anchor)) == 0 for label in cycle)
    return u, v, normal


def build_spec(rows, active):
    base_u, base_v, base_n = tangent_basis(rows, BASE)
    shell_u, shell_v, shell_n = tangent_basis(rows, SHELL)
    spec = []
    for label in active:
        if label in BASE:
            directions = (("base_u", base_u), ("base_v", base_v))
        elif label in SHELL:
            directions = (("shell_u", shell_u), ("shell_v", shell_v))
        else:
            directions = tuple(
                (axis, tuple(Q(1) if k == offset else Q(0) for k in range(3)))
                for offset, axis in enumerate("xyz")
            )
        for name, direction in directions:
            spec.append((label, f"r{label}_{name}", direction))
    assert len(spec) == 150
    assert len({name for _, name, _ in spec}) == len(spec)
    return spec, {
        "base_u": base_u,
        "base_v": base_v,
        "base_normal": base_n,
        "shell_u": shell_u,
        "shell_v": shell_v,
        "shell_normal": shell_n,
    }


def target_jets(rows, faces, spec):
    q, centroid = pc.make_jets(rows, faces, spec)
    incidence = pc.esc.incidence(faces)

    def face_component(vertices, edge):
        face = pc.esc.face_by_vertices(faces, vertices)
        values = dict(pc.rj.face_components(face, q, centroid))
        return values[edge] if edge in values else values[edge[::-1]]

    def edge_component(edge, component):
        edge = tuple(sorted(edge))
        return pc.rj.edge_components(edge, incidence[edge], faces, q, centroid)[component]

    targets = {
        "S228_264_246_via_246_228": face_component([228, 264, 246], (246, 228)),
        "U228_via_251": pc.rj.vertex_support(228, 251, q, centroid),
        "U231_via_232": pc.rj.vertex_support(231, 232, q, centroid),
        "U246_via_245": pc.rj.vertex_support(246, 245, q, centroid),
        "H8_246_via_t": edge_component((8, 246), "t"),
        "H228_254_via_beta2": edge_component((228, 254), "beta2"),
        "H231_247_via_beta1": edge_component((231, 247), "beta1"),
        "H236_237_via_beta1": edge_component((236, 237), "beta1"),
    }
    assert tuple(targets) == TARGET_NAMES

    base_face = pc.esc.face_by_vertices(faces, BASE)
    base_components = dict(pc.rj.face_components(base_face, q, centroid))
    neighbors = sorted({b if a == 8 else a for a, b in incidence if 8 in (a, b)})
    u8_components = {
        neighbor: pc.rj.vertex_support(8, neighbor, q, centroid)
        for neighbor in neighbors
    }
    assert all(z.v > 0 for z in targets.values())
    assert all(z.v > 0 for z in base_components.values())
    assert all(z.v > 0 for z in u8_components.values())
    return targets, base_components, u8_components


def qrecord(z):
    return {
        "value_exact": pc.qs(z.v),
        "value_decimal": float(z.v),
        "gradient_exact": [pc.qs(value) for value in z.d],
        "gradient_decimal": [float(value) for value in z.d],
    }


def vector_record(vector):
    return [pc.qs(value) for value in vector]


def main():
    frozen_ledger_path = ATTACK / "cells" / "endpoint.json"
    frozen_rows_path = ATTACK / "cells" / "endpoint.csv"
    packet, rows, faces, _centroid = load_frozen_endpoint()
    assert packet["f_vector"] == [61, 150, 91]
    assert packet["class"] == [2, 4, 4]
    assert packet["stable_faces"] == [list((228, 264, 246)), list(BASE)]
    assert packet["unstable_vertices"] == [8, 228, 231, 246]
    assert packet["saddle_edges"] == [[8, 246], [228, 254], [231, 247], [236, 237]]
    assert packet["all_37_forced_rails_present"]

    active = tuple(packet["active_vertices"])
    assert set(BASE).issubset(active) and set(SHELL).issubset(active)
    spec, basis = build_spec(rows, active)
    targets, base_components, u8_components = target_jets(rows, faces, spec)
    target_gradient = [targets[name].d for name in TARGET_NAMES]
    protected_gradient = [z.d for z in base_components.values()] + [
        z.d for z in u8_components.values()
    ]
    target_rank = pc.rj.matrix_rank(target_gradient)
    combined_rank = pc.rj.matrix_rank(target_gradient + protected_gradient)
    assert target_rank == len(TARGET_NAMES)

    normalized = np.asarray(
        [[float(value / targets[name].v) for value in targets[name].d] for name in TARGET_NAMES],
        dtype=float,
    )
    singular_values = np.linalg.svd(normalized, compute_uv=False)

    payload = {
        "version": 1,
        "scope": "exact fixed-plane full-control first-jet chart at frozen post-C17 endpoint",
        "source_hashes": {
            str(frozen_rows_path.relative_to(ATTACK)): sha256(frozen_rows_path),
            str(frozen_ledger_path.relative_to(ATTACK)): sha256(frozen_ledger_path),
            "certificate.json": sha256(ATTACK / "certificate.json"),
            "manifest.sha256": sha256(ATTACK / "manifest.sha256"),
        },
        "endpoint": {
            "f_vector": packet["f_vector"],
            "class": packet["class"],
            "active_rows": list(active),
            "stable_faces": packet["stable_faces"],
            "unstable_vertices": packet["unstable_vertices"],
            "saddle_edges": packet["saddle_edges"],
            "all_37_forced_rails_present": True,
        },
        "chart": {
            "kind": "affine fixed-supporting-plane chart",
            "mode_count": len(spec),
            "base_cycle": list(BASE),
            "shell_cycle": list(SHELL),
            "other_active_rows": sorted(set(active) - set(BASE) - set(SHELL)),
            "mode_names": [name for _, name, _ in spec],
            "mode_rows": [row for row, _, _ in spec],
            "mode_directions_exact": [vector_record(direction) for _, _, direction in spec],
            "basis_exact": {name: vector_record(vector) for name, vector in basis.items()},
            "base_planarity_preserved_for_every_affine_parameter_exactly": True,
            "shell_planarity_preserved_for_every_affine_parameter_exactly": True,
            "claim_boundary": (
                "This is the complete affine chart with both supporting planes frozen. "
                "It is not claimed to be the full nonlinear coplanarity manifold."
            ),
        },
        "targets": {name: qrecord(targets[name]) for name in TARGET_NAMES},
        "target_gradient_exact_rank": target_rank,
        "target_normalized_gradient_singular_values": singular_values.tolist(),
        "protected_base_components": {
            f"{edge[0]},{edge[1]}": qrecord(z)
            for edge, z in base_components.items()
        },
        "protected_U8_components": {
            str(neighbor): qrecord(z) for neighbor, z in u8_components.items()
        },
        "target_plus_protected_gradient_exact_rank": combined_rank,
        "verdict": "EXACT_POST_C17_FIXED_PLANE_FULL_CHART_AUDIT_PASS",
        "winner_status": "NONWINNER_CHART_ONLY",
    }
    OUTPUT.write_text(json.dumps(payload, indent=2) + "\n")
    print(payload["verdict"])
    print("mode_count", len(spec))
    print("target_rank", target_rank)
    print("target_plus_protected_rank", combined_rank)
    print("minimum_normalized_singular_value", singular_values[-1])
    print("output_sha256", sha256(OUTPUT))


if __name__ == "__main__":
    main()
