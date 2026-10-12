#!/usr/bin/env python3
"""Fresh-hull event atlas for the nonlinear row54 far-side metric path."""
from __future__ import annotations

import argparse
import csv
import json
import math
import sys
from pathlib import Path

import numpy as np
from scipy.optimize import brentq

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
CIRCUIT = ROOT / "tracks/circuit_atlas"
sys.path.insert(0, str(CIRCUIT))
sys.path.insert(0, str(HERE))

import row54_four_residual_search as core  # noqa: E402
from actual_grouped import evaluate, summarize  # noqa: E402

BASE = frozenset(range(17)) | {54}
SHORT_RAIL = [228] + list(range(229, 247)) + [8]
LONG_RAIL = [228] + list(range(247, 265)) + [8]


def read_csv(path: Path):
    rows = {}
    with path.open() as f:
        for r in csv.DictReader(f):
            rows[int(r["source_id"])] = np.array(
                [float(r[k]) for k in ("x", "y", "z")], dtype=float
            )
    ids = sorted(rows)
    return ids, np.array([rows[i] for i in ids])


class TargetedMechanics:
    """All local primitives that can participate in the observed relay."""

    def __init__(self, ids, source, faces):
        self.ids, self.source, self.faces = ids, source, faces
        self.ix = {i: k for k, i in enumerate(ids)}
        self.ef, self.nbr = core.edge_lattice(faces)
        self.face_keys = {frozenset(c): k for k, c in enumerate(faces)}
        self.target_faces = sorted(
            [frozenset(c) for c in faces if 8 in c] + [BASE],
            key=lambda z: (len(z), tuple(sorted(z))),
        )
        self.target_vertices = sorted(BASE)
        base_cycle = next(c for c in faces if frozenset(c) == BASE)
        base_edges = {tuple(sorted(e)) for e in zip(base_cycle, base_cycle[1:] + base_cycle[:1])}
        local_edges = {
            e for e in self.ef
            if 8 in e or e in {(6, 7), (9, 10), (1, 54), (1, 2), (0, 54)}
        }
        self.target_edges = sorted(base_edges | local_edges)

    def transform(self, theta, t):
        p, den = core.transform(self.source, t * theta)
        if p is None:
            raise ValueError(f"projective chart failed at {t}: {float(np.min(den))}")
        return p, den

    def decisions(self, theta, t):
        p, den = self.transform(theta, t)
        c0 = core.own_centroid(self.ids, p, self.faces)
        x = {i: p[self.ix[i]] - c0 for i in self.ids}
        normals = core.face_normals(self.ids, p, self.faces)
        out = {}

        for key in self.target_faces:
            fi = self.face_keys[key]
            cyc, n = self.faces[fi], normals[fi]
            h = float(np.dot(n, x[cyc[0]]))
            foot = n * h / float(np.dot(n, n))
            ref = np.mean([x[i] for i in cyc], axis=0)
            vals = []
            for a, b in zip(cyc, cyc[1:] + cyc[:1]):
                edge = x[b] - x[a]
                z = float(np.dot(np.cross(edge, foot - x[a]), n))
                if float(np.dot(np.cross(edge, ref - x[a]), n)) < 0:
                    z = -z
                vals.append(z / max(np.linalg.norm(edge) * np.linalg.norm(n), 1e-300))
            out[("S", tuple(sorted(key)))] = min(vals)

        for i in self.target_vertices:
            vals = [
                -float(np.dot(x[i], x[j] - x[i])) /
                max(np.linalg.norm(x[i]) * np.linalg.norm(x[j] - x[i]), 1e-300)
                for j in self.nbr[i]
            ]
            out[("U", i)] = min(vals)

        for e in self.target_edges:
            i, j = e
            d = x[j] - x[i]
            dd = float(np.dot(d, d))
            tt = -float(np.dot(x[i], d)) / dd
            foot = x[i] + tt * d
            inc = self.ef[e]
            n1, n2 = normals[inc[0]], normals[inc[1]]
            aa, bb, cc = float(n1 @ n1), float(n1 @ n2), float(n2 @ n2)
            r1, r2 = float(foot @ n1), float(foot @ n2)
            gram = aa * cc - bb * bb
            if gram <= 1e-30 * aa * cc:
                raise ValueError(f"ill-conditioned normal cone {e} at {t}")
            b1 = (r1 * cc - r2 * bb) / gram
            b2 = (r2 * aa - r1 * bb) / gram
            qn = max(float(foot @ foot), 1e-300)
            out[("H", e)] = min(
                tt, 1.0 - tt, b1 * math.sqrt(aa / qn), b2 * math.sqrt(cc / qn)
            )
        return out, float(np.min(den))


def label_json(label):
    kind, obj = label
    return [kind, list(obj) if isinstance(obj, tuple) else obj]


def actual_cell(ids, source, theta, t, expected_faces):
    p, den = core.transform(source, t * theta)
    points = {i: p[k] for k, i in enumerate(ids)}
    res = evaluate(points, coplanar_rel=1e-11)
    if not res.valid:
        raise RuntimeError(f"fresh actual evaluation failed at {t}: {res.error}")
    faces = {frozenset(f["cycle"]) for f in res.faces}
    edges = set(res.edges)
    rail = {}
    x = {i: points[i] - res.centroid for i in ids}
    for name, path in (("short", SHORT_RAIL), ("long", LONG_RAIL)):
        pairs = list(zip(path, path[1:]))
        rail[name] = {
            "all_edges_present": all(tuple(sorted(e)) in edges for e in pairs),
            "directed_support_min": min(float(np.dot(x[a], x[b] - x[a])) for a, b in pairs),
            "positive_dot_min": min(float(np.dot(x[a], x[b])) for a, b in pairs),
        }
    return {
        "t": float(t),
        "minimum_projective_denominator": float(np.min(den)),
        "faces_match_source": faces == expected_faces,
        "actual": summarize(res),
        "rails": rail,
    }


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--source", type=Path,
                    default=CIRCUIT / "row54_far_rebuilt.csv")
    ap.add_argument("--search", type=Path,
                    default=HERE / "row54_metric_de50.json")
    ap.add_argument("--samples", type=int, default=4001)
    ap.add_argument("--output", type=Path,
                    default=HERE / "row54_actual_event_atlas.json")
    args = ap.parse_args()

    ids, source = read_csv(args.source)
    theta = np.asarray(json.load(args.search.open())["theta"], dtype=float)
    p0, _ = core.transform(source, np.zeros(8))
    hull0, faces0, _ = core.group_maximal_faces(ids, p0)
    ef0, _ = core.edge_lattice(faces0)
    assert [len(hull0.vertices), len(ef0), len(faces0)] == [61, 162, 103]
    expected_faces = {frozenset(c) for c in faces0}
    tm = TargetedMechanics(ids, source, faces0)

    grid = np.linspace(0.0, 1.0, args.samples)
    labels = None
    values = None
    for k, t in enumerate(grid):
        d, _ = tm.decisions(theta, float(t))
        if labels is None:
            labels = list(d)
            values = np.empty((len(grid), len(labels)), dtype=float)
        values[k] = [d[z] for z in labels]

    roots = []
    for j, label in enumerate(labels):
        y = values[:, j]
        for k in range(len(grid) - 1):
            if y[k] == 0:
                root = float(grid[k])
            elif y[k] * y[k + 1] < 0:
                root = float(brentq(
                    lambda t: tm.decisions(theta, t)[0][label],
                    float(grid[k]), float(grid[k + 1]),
                    xtol=2e-13, rtol=2e-13, maxiter=100,
                ))
            else:
                continue
            roots.append((root, label, float(y[k]), float(y[k + 1])))

    roots.sort(key=lambda z: (z[0], z[1]))
    clusters = []
    for root, label, left, right in roots:
        if not clusters or root - clusters[-1]["t"] > 2e-7:
            clusters.append({"t": root, "crossings": []})
        clusters[-1]["crossings"].append({
            "feature": label_json(label),
            "direction": "negative_to_positive" if left < right else "positive_to_negative",
            "root": root,
        })
        clusters[-1]["t"] = float(np.mean([z["root"] for z in clusters[-1]["crossings"]]))

    cut = [0.0] + [z["t"] for z in clusters] + [1.0]
    probes = []
    for a, b in zip(cut, cut[1:]):
        if b - a > 1e-10:
            probes.append((a + b) / 2.0)
    probes.extend([0.0, 1.0])
    cells = [actual_cell(ids, source, theta, t, expected_faces) for t in sorted(set(probes))]

    # Compress adjacent roots which do not change the fresh actual state; the
    # raw crossing table remains available above for component-level audits.
    state_cells = []
    for z in cells:
        s = z["actual"]
        key = json.dumps([s["f_vector"], s["class"], s["stable"], s["unstable"], s["saddles"]], sort_keys=True)
        if not state_cells or key != state_cells[-1]["state_key"]:
            state_cells.append({"state_key": key, **z})
    for z in state_cells:
        z.pop("state_key")

    out = {
        "version": 1,
        "source": str(args.source),
        "search": str(args.search),
        "path": "p(t)=projective_tracefree_spd(row54_far_rebuilt, t*theta)",
        "theta": theta.tolist(),
        "targeted_sample_count": args.samples,
        "event_clusters": clusters,
        "fresh_actual_open_cells": state_cells,
        "all_cells_face_lattice_preserved": all(z["faces_match_source"] for z in cells),
        "all_cells_f_vector_61_162_103": all(z["actual"]["f_vector"] == [61, 162, 103] for z in cells),
        "all_cells_rail_edges_preserved": all(
            z["rails"][name]["all_edges_present"] for z in cells for name in ("short", "long")
        ),
        "verdict": "TRANSFER_NOT_ESCAPE",
        "terminal_residual": {
            "stable": state_cells[-1]["actual"]["stable"],
            "unstable": state_cells[-1]["actual"]["unstable"],
            "saddles": state_cells[-1]["actual"]["saddles"],
        },
    }
    args.output.write_text(json.dumps(out, indent=2) + "\n")
    print(json.dumps({
        "event_clusters": len(clusters),
        "actual_cells": len(state_cells),
        "verdict": out["verdict"],
        "terminal_residual": out["terminal_residual"],
    }, indent=2))


if __name__ == "__main__":
    main()
