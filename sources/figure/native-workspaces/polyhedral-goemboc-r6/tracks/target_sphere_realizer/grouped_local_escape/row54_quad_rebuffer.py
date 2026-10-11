#!/usr/bin/env python3
"""Move a far-diagonal checkpoint deeper along its local quad gradient."""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

import numpy as np
from scipy.linalg import expm
from scipy.optimize import brentq

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
sys.path[:0] = [str(HERE), str(ROOT / "tracks/circuit_atlas")]

from actual_grouped import evaluate, summarize  # noqa: E402
from row54_direct_actual_search import DirectActual, read_points  # noqa: E402
from row54_full_minimax import BASE, LONG_RAIL, SHORT_RAIL, guards  # noqa: E402
from row54_joint_actual_search import write_csv  # noqa: E402
import row54_four_residual_search as core  # noqa: E402


def label_key(label):
    kind, item = label
    return kind, tuple(sorted(item)) if isinstance(item, list) else item


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--source", type=Path, required=True)
    ap.add_argument("--target", type=float, default=5e-11)
    ap.add_argument("--output", type=Path, required=True)
    args = ap.parse_args()

    ids, source = read_points(args.source)
    direct = DirectActual(ids, source)
    n_direct = len(direct.controls)
    origin = source.mean(axis=0)
    scale = float(np.sqrt(np.mean(np.sum((source - origin) ** 2, axis=1))))
    local = {i: k for k, i in enumerate(ids)}

    def construct(z):
        q = direct.construct(z[:n_direct])
        qn = (q - origin) / scale
        theta = z[n_direct:]
        den = 1.0 + qn @ theta[:3]
        a, b, c, d, e = theta[3:]
        h = np.array([[a, b, c], [b, d, e],
                      [c, e, -a - d]], dtype=float)
        return origin + scale * ((qn / den[:, None]) @ expm(h).T)

    def quad_guard(z):
        p = construct(z)
        q = [p[local[i]] for i in (7, 8, 245, 246)]
        det = float(np.dot(q[1] - q[0],
                           np.cross(q[2] - q[0], q[3] - q[0])))
        s = float(np.sqrt(np.mean(np.sum((p - p.mean(axis=0)) ** 2,
                                         axis=1))))
        return -det / s**3

    zero = np.zeros(n_direct + 8)
    epsilon = 2e-6
    gradient = np.empty_like(zero)
    for j in range(len(zero)):
        step = np.zeros_like(zero)
        step[j] = epsilon
        gradient[j] = (quad_guard(step) - quad_guard(-step)) / (2 * epsilon)
    direction = gradient / np.max(np.abs(gradient))
    start = quad_guard(zero)

    def residual(t):
        return quad_guard(t * direction) - args.target

    hi = 1e-10
    while residual(hi) < 0 and hi < 0.1:
        hi *= 10
    if residual(hi) < 0:
        raise RuntimeError("failed to bracket requested quad buffer")
    step_size = brentq(residual, 0.0, hi, xtol=1e-18, rtol=1e-14)
    z = step_size * direction
    points = construct(z)
    actual = evaluate(dict(zip(ids, points)), coplanar_rel=1e-11)
    if not actual.valid:
        raise RuntimeError(actual.error)
    face_cycles = [f["cycle"] for f in actual.faces]
    g, labels = guards(core.mechanics(ids, points, face_cycles), face_cycles)
    lookup = {label_key(label): k for k, label in enumerate(labels)}
    protected_keys = (("U-", 263), ("H-", (10, 263)),
                      ("U-", 1), ("H-", (1, 54)))
    protected = {str(k): float(g[lookup[k]]) for k in protected_keys}
    edges = set(actual.edges)
    keys = {frozenset(f["cycle"]) for f in actual.faces}
    rails = {
        name: all(tuple(sorted(e)) in edges for e in zip(path, path[1:]))
        for name, path in (("short", SHORT_RAIL), ("long", LONG_RAIL))
    }
    valid = bool(
        set(actual.active) == set(ids)
        and summarize(actual)["f_vector"] == [61, 162, 103]
        and summarize(actual)["class"] == [2, 2, 2]
        and BASE in keys and all(rails.values())
        and all(v > 0 for v in protected.values())
    )
    out = {
        "version": 1,
        "method": "local directed-quad gradient rebuffer",
        "source": str(args.source),
        "source_quad_guard": start,
        "target_quad_guard": args.target,
        "achieved_quad_guard": quad_guard(z),
        "step_size": step_size,
        "direction": direction.tolist(),
        "hard_margin": float(np.min(g)),
        "protected_guards": protected,
        "fresh_actual": summarize(actual),
        "base_face_present": BASE in keys,
        "rail_edges_present": rails,
        "certified": valid,
    }
    write_csv(args.output.with_suffix(".csv"), ids, points)
    args.output.with_name(args.output.stem + "_faces.json").write_text(
        json.dumps(face_cycles, indent=2) + "\n"
    )
    args.output.write_text(json.dumps(out, indent=2) + "\n")
    print(json.dumps(out, indent=2))


if __name__ == "__main__":
    main()
