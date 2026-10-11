#!/usr/bin/env python3
"""Standalone fresh-hull verifier for the grouped local-escape chain."""
from __future__ import annotations

import argparse
import hashlib
import json
import sys
from pathlib import Path

import numpy as np
from scipy.linalg import expm

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
sys.path[:0] = [str(HERE), str(ROOT / "tracks/circuit_atlas")]

from actual_grouped import evaluate, summarize  # noqa: E402
from row54_direct_actual_search import DirectActual, read_points  # noqa: E402
from row54_full_minimax import BASE, LONG_RAIL, SHORT_RAIL, guards  # noqa: E402
import row54_four_residual_search as core  # noqa: E402

MANIFEST_FILES = [
    "actual_grouped.py",
    "row54_combined_hard_slp.py",
    "row54_round2_mechanical_event.py",
    "row54_round2_mechanical_event.json",
    "row54_round2_mechanical_event_wall.csv",
    "row54_round2_null_bypass.py",
    "row54_round2_null_bypass.json",
    "row54_round2_null_bypass_C_buffered_post.csv",
    "row54_round3_mechanical_event.py",
    "row54_round3_mechanical_event.json",
    "row54_round3_mechanical_event_wall.csv",
    "row54_round3_null_bypass.py",
    "row54_round3_null_bypass.json",
    "row54_round3_null_bypass_C_buffered_post.csv",
    "row54_round4_topology_event.py",
    "row54_round4_topology_event.json",
    "row54_round4_topology_event_pre.csv",
    "row54_round4_topology_event_wall.csv",
    "row54_round4_topology_event_far.csv",
    "row54_round4_null_cross.py",
    "row54_round4_null_cross.json",
    "row54_round4_null_cross_deep_far.csv",
    "row54_combined_hard_slp_far_round5_guarded.json",
    "row54_combined_hard_slp_far_round5_guarded_best.csv",
    "row54_combined_hard_slp_far_round6_guarded.json",
    "row54_combined_hard_slp_far_round6_guarded_best.csv",
    "row54_combined_hard_slp_far_round7_tangent.json",
    "row54_combined_hard_slp_far_round7_tangent_best.csv",
    "row54_combined_hard_slp_far_round8_projected_tangent.json",
    "row54_combined_hard_slp_far_round8_projected_tangent_best.csv",
    "row54_round8_topology_event.py",
    "row54_round8_topology_event.json",
    "row54_round8_topology_event_pre.csv",
    "row54_round8_topology_event_wall.csv",
    "row54_round8_topology_event_far.csv",
    "row54_round8_topology_event_pre_faces.json",
    "row54_round8_topology_event_wall_faces.json",
    "row54_round8_topology_event_far_faces.json",
    "verify_round8_alternate_acute_route.py",
    "row54_round8_alternate_acute_route.json",
    "row54_round8_far_route_slp.py",
    "row54_round8_far_route_slp.json",
    "row54_round8_far_route_slp_best.csv",
    "row54_round8_far_route_slp_best_faces.json",
    "row54_round8_far_route_slp_tangent.json",
    "row54_round8_far_route_slp_tangent_best.csv",
    "row54_round8_far_route_slp_tangent_best_faces.json",
    "row54_round8_pre_planar_bypass.py",
    "row54_round8_pre_planar_bypass.json",
    "row54_round8_pre_planar_bypass_pre.csv",
    "row54_round8_pre_planar_bypass_pre_faces.json",
    "row54_round8_pre_planar_bypass_buffer.csv",
    "row54_round8_pre_planar_bypass_buffer_faces.json",
    "row54_round8_pre_planar_bypass_next.csv",
    "row54_round8_pre_planar_bypass_next_faces.json",
    "row54_round8_pre_planar_bypass_q_m1_m1.csv",
    "row54_round8_pre_planar_bypass_q_m1_p1.csv",
    "row54_round8_pre_planar_bypass_q_p1_m1.csv",
    "row54_round8_pre_planar_bypass_q_p1_p1.csv",
    "row54_combined_hard_slp_round9_pre_detour.json",
    "row54_combined_hard_slp_round9_pre_detour_best.csv",
    "row54_combined_hard_slp_round9_pre_detour_best_faces.json",
    "row54_combined_hard_slp_round10_double_tangent.json",
    "row54_combined_hard_slp_round10_double_tangent_best.csv",
    "row54_combined_hard_slp_round10_double_tangent_best_faces.json",
    "row54_round10_topology_event.py",
    "row54_round10_topology_event.json",
    "row54_round10_topology_event_pre.csv",
    "row54_round10_topology_event_pre_faces.json",
    "row54_round10_topology_event_wall.csv",
    "row54_round10_topology_event_wall_faces.json",
    "row54_round10_topology_event_far.csv",
    "row54_round10_topology_event_far_faces.json",
    "row54_round10_far_multiguard_buffer.py",
    "row54_round10_far_multiguard_buffer.json",
    "row54_round10_far_multiguard_buffer_source.csv",
    "row54_round10_far_multiguard_buffer_buffer.csv",
    "row54_round10_far_multiguard_buffer_buffer_faces.json",
    "row54_combined_hard_slp_round11_far_buffered.json",
    "row54_combined_hard_slp_round11_far_buffered_best.csv",
    "row54_combined_hard_slp_round11_far_buffered_best_faces.json",
    "row54_combined_hard_slp_round12_far_two_wall_tangent.json",
    "row54_combined_hard_slp_round12_far_two_wall_tangent_best.csv",
    "row54_combined_hard_slp_round12_far_two_wall_tangent_best_faces.json",
    "row54_round12_topology_event.py",
    "row54_round12_topology_event.json",
    "row54_round12_topology_event_pre.csv",
    "row54_round12_topology_event_pre_faces.json",
    "row54_round12_topology_event_wall.csv",
    "row54_round12_topology_event_wall_faces.json",
    "row54_round12_topology_event_far.csv",
    "row54_round12_topology_event_far_faces.json",
    "verify_grouped_escape.py",
]

ALT_ACUTE_ROUTE = [228, 198, 263, 9, 8]
OLD_QUAD = (7, 8, 245, 246)
ROUND8_QUAD = (9, 198, 263, 264)


def sha256(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for block in iter(lambda: f.read(1 << 20), b""):
            h.update(block)
    return h.hexdigest()


def label_key(label):
    kind, item = label
    return kind, tuple(sorted(item)) if isinstance(item, list) else item


def rail_ledger(actual):
    edges = set(actual.edges)
    return {
        name: all(tuple(sorted(e)) in edges for e in zip(path, path[1:]))
        for name, path in (("short", SHORT_RAIL), ("long", LONG_RAIL))
    }


def route_ledger(ids, points, actual, path):
    ix = {i: k for k, i in enumerate(ids)}
    x = {i: points[ix[i]] - actual.centroid for i in ids}
    edges = set(actual.edges)
    pairs = list(zip(path, path[1:]))
    return {
        "all_edges_present": all(tuple(sorted(e)) in edges for e in pairs),
        "positive_dot_min": min(float(np.dot(x[a], x[b])) for a, b in pairs),
        "directed_support_min": min(
            float(np.dot(x[a], x[b] - x[a])) for a, b in pairs
        ),
    }


def positive_dot_component(ids, points, actual, source=228):
    ix = {i: k for k, i in enumerate(ids)}
    x = {i: points[ix[i]] - actual.centroid for i in ids}
    graph = {i: set() for i in ids}
    for a, b in actual.edges:
        if float(np.dot(x[a], x[b])) > 0:
            graph[a].add(b)
            graph[b].add(a)
    reached = {source}
    stack = [source]
    while stack:
        u = stack.pop()
        for v in graph[u] - reached:
            reached.add(v)
            stack.append(v)
    return reached


def directed_reachable(ids, points, actual, source=228):
    ix = {i: k for k, i in enumerate(ids)}
    x = {i: points[ix[i]] - actual.centroid for i in ids}
    graph = {i: set() for i in ids}
    for a, b in actual.edges:
        for u, v in ((a, b), (b, a)):
            if (float(np.dot(x[u], x[v])) > 0
                    and float(np.dot(x[u], x[v] - x[u])) > 0):
                graph[u].add(v)
    reached = {source}
    stack = [source]
    while stack:
        u = stack.pop()
        for v in graph[u] - reached:
            reached.add(v)
            stack.append(v)
    return reached


def oriented_guard(ids, points, quad, sign):
    ix = {i: k for k, i in enumerate(ids)}
    p = np.asarray(points, dtype=np.longdouble)
    q = [p[ix[i]] for i in quad]
    det = np.dot(q[1] - q[0], np.cross(q[2] - q[0], q[3] - q[0]))
    centered = p - np.mean(p, axis=0)
    scale = np.sqrt(np.mean(np.sum(centered * centered, axis=1)))
    return float(sign * det / scale**3)


def endpoint_numerator_guards(ids, points, actual):
    ix = {i: k for k, i in enumerate(ids)}
    p = np.asarray(points, dtype=np.longdouble)
    c = np.asarray(actual.centroid, dtype=np.longdouble)
    x10, x263 = p[ix[10]] - c, p[ix[263]] - c
    x1, x54 = p[ix[1]] - c, p[ix[54]] - c
    return [float(-np.dot(x263, x263 - x10)),
            float(np.dot(x1, x54 - x1))]


def face_keys(actual):
    return {frozenset(f["cycle"]) for f in actual.faces}


def fresh_csv(name, expected_f, expected_class, expected_rails,
              expected_faces=None):
    ids, points = read_points(HERE / name)
    actual = evaluate(dict(zip(ids, points)), coplanar_rel=1e-11)
    assert actual.valid, (name, actual.error)
    summary = summarize(actual)
    assert summary["f_vector"] == expected_f, (name, summary["f_vector"])
    assert summary["class"] == expected_class, (name, summary["class"])
    assert set(actual.active) == set(ids), name
    assert BASE in face_keys(actual), name
    rails = rail_ledger(actual)
    assert rails == expected_rails, (name, rails)
    if expected_faces:
        stored = {frozenset(f) for f in json.loads((HERE / expected_faces).read_text())}
        assert face_keys(actual) == stored, name
    return ids, points, actual


def verify_classic_path(json_name, protected_keys):
    packet = json.loads((HERE / json_name).read_text())
    ids, source = read_points(Path(packet["source"]))
    direct = DirectActual(ids, source)
    n_direct = len(direct.controls)
    _, faces, _ = core.group_maximal_faces(ids, source)
    expected_keys = {frozenset(f) for f in faces}
    minimum_topology = float("inf")
    minimum_guards = {str(k): float("inf") for k in protected_keys}
    for sample in packet["L_path"]:
        z = np.asarray(sample["parameters"], float)
        q = direct.construct(z[:n_direct])
        points, den = core.transform(q, z[n_direct:])
        assert points is not None and float(np.min(den)) > 0.08
        actual = evaluate(dict(zip(ids, points)), coplanar_rel=1e-11)
        assert actual.valid, (json_name, actual.error)
        assert summarize(actual)["f_vector"] == [61, 162, 103]
        assert summarize(actual)["class"] == [2, 2, 2]
        assert face_keys(actual) == expected_keys
        assert BASE in expected_keys and all(rail_ledger(actual).values())
        cycles = [f["cycle"] for f in actual.faces]
        g, labels = guards(core.mechanics(ids, points, cycles), cycles)
        lookup = {label_key(label): k for k, label in enumerate(labels)}
        for key in protected_keys:
            value = float(g[lookup[key]])
            assert value > 0, (json_name, key, value)
            minimum_guards[str(key)] = min(minimum_guards[str(key)], value)
        minimum_topology = min(minimum_topology, actual.topology_margin)
    return {
        "samples": len(packet["L_path"]),
        "all_class222": True,
        "minimum_topology_margin": minimum_topology,
        "minimum_protected_guards": minimum_guards,
    }


def identity_construct(source_path):
    ids, source = read_points(source_path)
    direct = DirectActual(ids, source)
    n_direct = len(direct.controls)
    origin = source.mean(axis=0)
    scale = float(np.sqrt(np.mean(np.sum((source - origin) ** 2, axis=1))))

    def construct(z):
        q = direct.construct(z[:n_direct])
        qn = (q - origin) / scale
        theta = z[n_direct:]
        den = 1.0 + qn @ theta[:3]
        a, b, c, d, e = theta[3:]
        h = np.array([[a, b, c], [b, d, e],
                      [c, e, -a - d]], dtype=float)
        return origin + scale * ((qn / den[:, None]) @ expm(h).T)

    return ids, construct


def verify_round4_sampled_path():
    packet = json.loads((HERE / "row54_round4_null_cross.json").read_text())
    ids, construct = identity_construct(Path(packet["source"]))
    reps = {k: np.asarray(v["parameters"], float)
            for k, v in packet["audits"].items()}
    zero = np.zeros_like(reps["pre_good"])
    segments = (
        (zero, reps["pre_good"]),
        (reps["pre_good"], reps["far_good"]),
        (reps["far_good"], reps["deep_far"]),
    )
    protected_keys = (("U-", 263), ("H-", (10, 263)),
                      ("U-", 1), ("H-", (1, 54)))
    minimum_topology = float("inf")
    minimum_guards = {str(k): float("inf") for k in protected_keys}
    count = 0
    for a, b in segments:
        for t in np.linspace(0.0, 1.0, 41):
            points = construct((1.0 - t) * a + t * b)
            actual = evaluate(dict(zip(ids, points)), coplanar_rel=1e-11)
            assert actual.valid, actual.error
            assert set(actual.active) == set(ids)
            assert summarize(actual)["class"] == [2, 2, 2]
            assert summarize(actual)["f_vector"] in ([61, 162, 103],
                                                       [61, 161, 102])
            assert BASE in face_keys(actual) and all(rail_ledger(actual).values())
            cycles = [f["cycle"] for f in actual.faces]
            g, labels = guards(core.mechanics(ids, points, cycles), cycles)
            lookup = {label_key(label): k for k, label in enumerate(labels)}
            for key in protected_keys:
                value = float(g[lookup[key]])
                assert value > 0, (key, value)
                minimum_guards[str(key)] = min(minimum_guards[str(key)], value)
            minimum_topology = min(minimum_topology, actual.topology_margin)
            count += 1
    return {
        "samples": count,
        "all_class222": True,
        "minimum_topology_margin": minimum_topology,
        "minimum_protected_guards": minimum_guards,
    }


def verify_round8_pre_planar_path():
    packet = json.loads((HERE / "row54_round8_pre_planar_bypass.json").read_text())
    ids, construct = identity_construct(Path(packet["source"]))
    _, source_points = read_points(Path(packet["source"]))
    source_actual = evaluate(dict(zip(ids, source_points)), coplanar_rel=1e-11)
    expected_faces = face_keys(source_actual)
    protected = (("U-", 263), ("H-", (10, 263)),
                 ("U-", 1), ("H-", (1, 54)))
    min_topology = float("inf")
    min_old_quad = float("inf")
    min_round8_quad = float("inf")
    min_guards = {str(k): float("inf") for k in protected}
    for sample in packet["L_path_samples"]:
        points = construct(np.asarray(sample["parameters"], float))
        actual = evaluate(dict(zip(ids, points)), coplanar_rel=1e-11)
        assert actual.valid, actual.error
        assert summarize(actual)["f_vector"] == [61, 162, 103]
        assert summarize(actual)["class"] == [2, 2, 2]
        assert set(actual.active) == set(ids)
        assert face_keys(actual) == expected_faces
        assert BASE in expected_faces and all(rail_ledger(actual).values())
        cycles = [f["cycle"] for f in actual.faces]
        g, labels = guards(core.mechanics(ids, points, cycles), cycles)
        lookup = {label_key(label): k for k, label in enumerate(labels)}
        for key in protected:
            value = float(g[lookup[key]])
            assert value > 0, (key, value)
            min_guards[str(key)] = min(min_guards[str(key)], value)
        og = oriented_guard(ids, points, OLD_QUAD, -1)
        ng = oriented_guard(ids, points, ROUND8_QUAD, -1)
        assert og > 0 and ng > 0, (og, ng)
        min_old_quad = min(min_old_quad, og)
        min_round8_quad = min(min_round8_quad, ng)
        min_topology = min(min_topology, actual.topology_margin)
    assert packet["L_path_all_open_class222_with_contract"]
    assert packet["all_quadrants_same_open_class222"]
    return {
        "samples": len(packet["L_path_samples"]),
        "all_same_open_class222": True,
        "minimum_topology_margin": min_topology,
        "minimum_old_quad_guard": min_old_quad,
        "minimum_round8_pre_guard": min_round8_quad,
        "minimum_protected_guards": min_guards,
    }


def verify_round10_far_multiguard():
    packet = json.loads((HERE / "row54_round10_far_multiguard_buffer.json").read_text())
    ids, construct = identity_construct(Path(packet["source_path"]))
    _, source_points = read_points(Path(packet["source_path"]))
    source_actual = evaluate(dict(zip(ids, source_points)), coplanar_rel=1e-11)
    expected_faces = face_keys(source_actual)
    protected = (("U-", 263), ("H-", (10, 263)),
                 ("U-", 1), ("H-", (1, 54)))

    def check(parameters):
        points = construct(np.asarray(parameters, float))
        actual = evaluate(dict(zip(ids, points)), coplanar_rel=1e-11)
        assert actual.valid, actual.error
        assert summarize(actual)["f_vector"] == [61, 162, 103]
        assert summarize(actual)["class"] == [2, 2, 2]
        assert set(actual.active) == set(ids) and face_keys(actual) == expected_faces
        assert BASE in expected_faces and all(rail_ledger(actual).values())
        topology = [
            oriented_guard(ids, points, OLD_QUAD, -1),
            oriented_guard(ids, points, ROUND8_QUAD, -1),
            oriented_guard(ids, points, (8, 264, 246, 198), 1),
        ]
        endpoint = endpoint_numerator_guards(ids, points, actual)
        assert min(topology + endpoint) > 0, (topology, endpoint)
        cycles = [f["cycle"] for f in actual.faces]
        g, labels = guards(core.mechanics(ids, points, cycles), cycles)
        lookup = {label_key(label): k for k, label in enumerate(labels)}
        old = [float(g[lookup[k]]) for k in protected]
        assert min(old) > 0, old
        route = route_ledger(ids, points, actual, ALT_ACUTE_ROUTE)
        assert route["all_edges_present"] and route["positive_dot_min"] > 0
        return actual.topology_margin, topology + endpoint, old

    minimum_topology = float("inf")
    minimum_directed = [float("inf")] * 5
    minimum_old = [float("inf")] * 4
    for sample in packet["piecewise_path"]:
        topo, directed, old = check(sample["parameters"])
        minimum_topology = min(minimum_topology, topo)
        minimum_directed = [min(a, b) for a, b in zip(minimum_directed, directed)]
        minimum_old = [min(a, b) for a, b in zip(minimum_old, old)]
    for corner in packet["cube_corners"].values():
        check(corner["parameters"])
    assert packet["piecewise_path_all_open_class222"]
    assert packet["all_32_cube_corners_open_class222"]
    assert packet["directed_response_rank"] == 5
    diag = packet["new_diagonal_control"]
    assert diag["jacobian_rank_with_row"] == diag["jacobian_rank_without_row"] + 1
    assert not diag["positive_dot_shortcut"] and not diag["directed_shortcut"]
    return {
        "path_samples": len(packet["piecewise_path"]),
        "cube_corners": len(packet["cube_corners"]),
        "response_rank": packet["directed_response_rank"],
        "minimum_topology_margin": minimum_topology,
        "minimum_five_directed_guards": minimum_directed,
        "minimum_old_mechanics_guards": minimum_old,
        "new_diagonal_independent_not_acute": True,
    }


def verify_hashes(manifest_path):
    manifest = json.loads(manifest_path.read_text())
    for rel, expected in manifest["files"].items():
        path = HERE / rel
        assert path.stat().st_size == expected["bytes"], rel
        assert sha256(path) == expected["sha256"], rel
    return {"files": len(manifest["files"]), "all_match": True}


def write_manifest(path):
    missing = [rel for rel in MANIFEST_FILES if not (HERE / rel).exists()]
    if missing:
        raise FileNotFoundError(missing)
    data = {
        "version": 1,
        "algorithm": "sha256",
        "files": {
            rel: {"sha256": sha256(HERE / rel),
                  "bytes": (HERE / rel).stat().st_size}
            for rel in MANIFEST_FILES
        },
    }
    path.write_text(json.dumps(data, indent=2) + "\n")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--manifest", type=Path,
                    default=HERE / "grouped_escape_manifest.json")
    ap.add_argument("--output", type=Path,
                    default=HERE / "grouped_escape_verification.json")
    ap.add_argument("--write-manifest", action="store_true")
    args = ap.parse_args()

    if args.write_manifest:
        write_manifest(args.manifest)

    endpoints = {}
    endpoint_specs = [
        ("round2_endpoint", "row54_round2_null_bypass_C_buffered_post.csv",
         [61, 162, 103], [2, 2, 2], {"short": True, "long": True},
         "row54_round2_null_bypass_endpoint_faces.json"),
        ("round3_endpoint", "row54_round3_null_bypass_C_buffered_post.csv",
         [61, 162, 103], [2, 2, 2], {"short": True, "long": True},
         "row54_round3_null_bypass_endpoint_faces.json"),
        ("round4_deep_far", "row54_round4_null_cross_deep_far.csv",
         [61, 162, 103], [2, 2, 2], {"short": True, "long": True},
         "row54_round4_null_cross_deep_far_faces.json"),
        ("obstruction_pre", "row54_round8_topology_event_pre.csv",
         [61, 162, 103], [2, 2, 2], {"short": True, "long": True},
         "row54_round8_topology_event_pre_faces.json"),
        ("obstruction_wall", "row54_round8_topology_event_wall.csv",
         [61, 161, 102], [2, 2, 2], {"short": True, "long": False},
         "row54_round8_topology_event_wall_faces.json"),
        ("obstruction_far", "row54_round8_topology_event_far.csv",
         [61, 162, 103], [2, 2, 2], {"short": True, "long": False},
         "row54_round8_topology_event_far_faces.json"),
        ("pre_planar_buffer", "row54_round8_pre_planar_bypass_buffer.csv",
         [61, 162, 103], [2, 2, 2], {"short": True, "long": True},
         "row54_round8_pre_planar_bypass_buffer_faces.json"),
        ("pre_planar_next", "row54_round8_pre_planar_bypass_next.csv",
         [61, 162, 103], [2, 2, 2], {"short": True, "long": True},
         "row54_round8_pre_planar_bypass_next_faces.json"),
        ("round10_endpoint", "row54_combined_hard_slp_round10_double_tangent_best.csv",
         [61, 162, 103], [2, 2, 2], {"short": True, "long": True},
         "row54_combined_hard_slp_round10_double_tangent_best_faces.json"),
        ("next_event_pre", "row54_round10_topology_event_pre.csv",
         [61, 162, 103], [2, 2, 2], {"short": True, "long": True},
         "row54_round10_topology_event_pre_faces.json"),
        ("next_event_wall", "row54_round10_topology_event_wall.csv",
         [61, 161, 102], [2, 2, 2], {"short": True, "long": True},
         "row54_round10_topology_event_wall_faces.json"),
        ("next_event_far", "row54_round10_topology_event_far.csv",
         [61, 162, 103], [2, 2, 2], {"short": True, "long": True},
         "row54_round10_topology_event_far_faces.json"),
        ("far_route_endpoint", "row54_round8_far_route_slp_tangent_best.csv",
         [61, 162, 103], [2, 2, 2], {"short": True, "long": False},
         "row54_round8_far_route_slp_tangent_best_faces.json"),
        ("round10_far_buffer", "row54_round10_far_multiguard_buffer_buffer.csv",
         [61, 162, 103], [2, 2, 2], {"short": True, "long": True},
         "row54_round10_far_multiguard_buffer_buffer_faces.json"),
        ("round12_endpoint", "row54_combined_hard_slp_round12_far_two_wall_tangent_best.csv",
         [61, 162, 103], [2, 2, 2], {"short": True, "long": True},
         "row54_combined_hard_slp_round12_far_two_wall_tangent_best_faces.json"),
        ("round12_event_pre", "row54_round12_topology_event_pre.csv",
         [61, 162, 103], [2, 2, 2], {"short": True, "long": True},
         "row54_round12_topology_event_pre_faces.json"),
        ("round12_event_wall", "row54_round12_topology_event_wall.csv",
         [61, 161, 102], [2, 2, 2], {"short": True, "long": False},
         "row54_round12_topology_event_wall_faces.json"),
        ("round12_event_far", "row54_round12_topology_event_far.csv",
         [61, 162, 103], [2, 2, 2], {"short": True, "long": False},
         "row54_round12_topology_event_far_faces.json"),
    ]
    obstruction = {}
    for key, name, fv, cls, rails, faces_name in endpoint_specs:
        ids, points, actual = fresh_csv(name, fv, cls, rails, faces_name)
        endpoints[key] = {
            "f_vector": fv,
            "class": cls,
            "topology_margin": actual.topology_margin,
            "rails": rails,
        }
        if key.startswith("obstruction_"):
            obstruction[key] = (ids, points, actual)

    pre_edges = set(obstruction["obstruction_pre"][2].edges)
    wall_edges = set(obstruction["obstruction_wall"][2].edges)
    far_edges = set(obstruction["obstruction_far"][2].edges)
    assert (263, 264) in pre_edges
    assert (263, 264) not in wall_edges and (263, 264) not in far_edges
    assert (9, 198) not in pre_edges and (9, 198) not in wall_edges
    assert (9, 198) in far_edges

    event = json.loads((HERE / "row54_round8_topology_event.json").read_text())
    assert event["removed_faces"] == [[9, 263, 264], [198, 263, 264]]
    assert event["added_faces"] == [[9, 198, 263], [9, 198, 264]]
    assert abs(event["oriented_volume_at_root"]) < 1e-15
    for stage in ("pre", "wall", "far"):
        ledger = event["audits"][stage]["guard_ledger"]
        for key in ("('U-', 263)", "('H-', (10, 263))",
                    "('U-', 1)", "('H-', (1, 54))"):
            assert ledger[key] > 0, (stage, key, ledger[key])

    # The deleted 263--264 edge obstructs only the literal 19-edge long rail.
    # It does not disconnect the actual positive-dot graph: the same four-edge
    # alternate route survives on both open sides.  Directed monotonicity is a
    # separate, stronger condition and already fails on the pre side.
    acute_route = {}
    for stage in ("obstruction_pre", "obstruction_far"):
        ids, points, actual = obstruction[stage]
        record = route_ledger(ids, points, actual, ALT_ACUTE_ROUTE)
        component = positive_dot_component(ids, points, actual)
        directed = directed_reachable(ids, points, actual)
        assert record["all_edges_present"] and record["positive_dot_min"] > 0
        assert len(component) == len(ids) and 8 in component
        assert 8 not in directed
        acute_route[stage] = {
            **record,
            "positive_dot_component_size": len(component),
            "directed_reachable_size_from_228": len(directed),
            "directed_reaches_U8": False,
        }

    next_event = json.loads((HERE / "row54_round10_topology_event.json").read_text())
    assert next_event["event_quad"] == [8, 264, 246, 198]
    assert next_event["removed_faces"] == [[8, 246, 264], [198, 246, 264]]
    assert next_event["added_faces"] == [[8, 198, 246], [8, 198, 264]]
    assert abs(next_event["oriented_volume_at_root"]) < 1e-15
    for stage in ("pre", "wall", "far"):
        rec = next_event["audits"][stage]
        assert rec["base_face_present"] and rec["U8_present"]
        assert rec["rails"]["short_literal"]["all_edges_present"]
        assert rec["rails"]["long_literal"]["all_edges_present"]
        assert rec["rails"]["alternate_positive_dot"]["all_edges_present"]
        assert rec["rails"]["alternate_positive_dot"]["positive_dot_min"] > 0
        for key in ("('U-', 263)", "('H-', (10, 263))",
                    "('U-', 1)", "('H-', (1, 54))"):
            assert rec["guard_ledger"][key] > 0, (stage, key)

    round10_packet = json.loads(
        (HERE / "row54_combined_hard_slp_round10_double_tangent.json").read_text()
    )
    assert round10_packet["hard_margin"] < 0
    assert round10_packet["hard_margin"] > event["audits"]["pre"]["hard_margin"]

    round12_event = json.loads((HERE / "row54_round12_topology_event.json").read_text())
    assert round12_event["event_quad"] == [198, 263, 262, 11]
    assert round12_event["removed_faces"] == [[11, 262, 263], [198, 262, 263]]
    assert round12_event["added_faces"] == [[11, 198, 262], [11, 198, 263]]
    assert abs(round12_event["oriented_volume_at_root"]) < 1e-15
    for stage in ("pre", "wall", "far"):
        rec = round12_event["audits"][stage]
        assert rec["base_face_present"] and rec["U8_present"]
        assert rec["rails"]["short_literal"]["all_edges_present"]
        assert rec["rails"]["alternate_positive_dot"]["all_edges_present"]
        assert rec["rails"]["alternate_positive_dot"]["positive_dot_min"] > 0
        assert min(rec["topology_guards"].values()) > 0
        for key in ("('U-', 263)", "('H-', (10, 263))",
                    "('U-', 1)", "('H-', (1, 54))"):
            assert rec["guard_ledger"][key] > 0, (stage, key)
    assert round12_event["audits"]["pre"]["rails"]["long_literal"]["all_edges_present"]
    assert not round12_event["audits"]["wall"]["rails"]["long_literal"]["all_edges_present"]
    assert not round12_event["audits"]["far"]["rails"]["long_literal"]["all_edges_present"]

    round12_packet = json.loads(
        (HERE / "row54_combined_hard_slp_round12_far_two_wall_tangent.json").read_text()
    )
    assert round12_packet["hard_margin"] > round10_packet["hard_margin"]

    paths = {
        "round2": verify_classic_path(
            "row54_round2_null_bypass.json",
            (("U-", 263), ("H-", (10, 263))),
        ),
        "round3": verify_classic_path(
            "row54_round3_null_bypass.json",
            (("U-", 263), ("H-", (10, 263)),
             ("U-", 1), ("H-", (1, 54))),
        ),
        "round4": verify_round4_sampled_path(),
        "round8_pre_planar": verify_round8_pre_planar_path(),
        "round10_far_multiguard": verify_round10_far_multiguard(),
    }

    mechanical = {
        "round2_identity_residual": json.loads(
            (HERE / "row54_round2_mechanical_event.json").read_text()
        )["endpoint_identity"]["identity_residual"],
        "round3_identity_residual": json.loads(
            (HERE / "row54_round3_mechanical_event.json").read_text()
        )["endpoint_identity"]["identity_residual"],
    }
    assert abs(mechanical["round2_identity_residual"]) < 1e-14
    assert abs(mechanical["round3_identity_residual"]) < 1e-14

    hashes = verify_hashes(args.manifest)
    output = {
        "version": 1,
        "verified": True,
        "fresh_endpoints": endpoints,
        "sampled_paths": paths,
        "mechanical_endpoint_identities": mechanical,
        "terminal_obstruction": {
            "quad": [9, 198, 263, 264],
            "flip": "edge 263-264 to edge 9-198",
            "pre_both_rails": True,
            "wall_long_rail": False,
            "far_long_rail": False,
            "old_mechanical_guards_positive": True,
            "scope": "literal long-rail contract only",
            "alternate_positive_dot_route": ALT_ACUTE_ROUTE,
            "positive_dot_graph_connected": True,
            "directed_monotone_route_present": False,
        },
        "round8_acute_graph": acute_route,
        "pre_cell_planar_detour": {
            "verified": True,
            "hard_after_double_tangent": round10_packet["hard_margin"],
            "next_independent_event_quad": [8, 264, 246, 198],
            "next_flip": "edge 246-264 to edge 8-198",
        },
        "round10_far_continuation": {
            "five_guard_buffer_verified": True,
            "new_diagonal_8_198": "independent mechanics row but obtuse, no acute shortcut",
            "hard_after_two_wall_tangent": round12_packet["hard_margin"],
            "next_independent_event_quad": [198, 263, 262, 11],
            "next_flip": "edge 262-263 to edge 11-198",
            "literal_long_rail_lost": True,
            "alternate_positive_dot_route_survives": ALT_ACUTE_ROUTE,
            "directed_scope_unchanged": True,
        },
        "hash_manifest": hashes,
    }
    args.output.write_text(json.dumps(output, indent=2) + "\n")
    print(json.dumps(output, indent=2))


if __name__ == "__main__":
    main()
