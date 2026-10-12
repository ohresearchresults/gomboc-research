#!/usr/bin/env python3
"""Exactify the complete row54 13-DOF sign-primitive first-order LP."""
from __future__ import annotations

import argparse
import json
import sys
from fractions import Fraction as F
from pathlib import Path

import numpy as np
from scipy.optimize import linprog


HERE = Path(__file__).resolve().parent
TRACK = HERE.parent
sys.path.insert(0, str(HERE))
import rational_shared_certificate as exact  # noqa: E402
sys.path.insert(0, str(TRACK))
import row54_shared3d_embedding as numeric  # noqa: E402


def all_features():
    p = exact.rational_chart_points()
    centroid = exact.own_centroid(p)
    normals = exact.face_normals(p)
    stable_face = next(i for i, face in enumerate(exact.FACES)
                       if frozenset(face) == frozenset((7, 8, 246)))
    base = frozenset(range(17)) | {54}
    base_face = next(i for i, face in enumerate(exact.FACES)
                     if frozenset(face) == base)
    targets = [
        ("target:S[7,8,246]-death",
         -exact.stable_primitives(stable_face, p, centroid, normals)[1]),
        ("target:U54-death", -exact.vertex_primitive(54, 1, p, centroid)),
        ("target:H67-death", -exact.edge_primitives((6, 7), p, centroid, normals)[0]),
        ("target:H910-death", -exact.edge_primitives((9, 10), p, centroid, normals)[1]),
    ]
    guards = []
    for fi, face in enumerate(exact.FACES):
        members = set(face)
        for row in exact.IDS:
            if row not in members:
                guards.append((f"guard:topology:f{fi}:row{row}",
                               exact.topology_primitive(fi, row, p, normals)))
    for k, value in enumerate(exact.stable_primitives(base_face, p, centroid, normals)):
        guards.append((f"guard:base:c{k}", value))
    for row in sorted(exact.NEIGHBORS[8]):
        guards.append((f"guard:U8:to{row}",
                       exact.vertex_primitive(8, row, p, centroid)))
    for fi, k in sorted(numeric.ANTI_TEMPLATE["face"].items()):
        guards.append((f"guard:antiface:f{fi}:c{k}",
                       -exact.stable_primitives(fi, p, centroid, normals)[k]))
    for row, neighbor in sorted(numeric.ANTI_TEMPLATE["vertex"].items()):
        guards.append((f"guard:antivertex:v{row}:to{neighbor}",
                       -exact.vertex_primitive(row, neighbor, p, centroid)))
    for edge, k in sorted(numeric.ANTI_TEMPLATE["edge"].items()):
        guards.append((f"guard:antiedge:{edge[0]}-{edge[1]}:c{k}",
                       -exact.edge_primitives(edge, p, centroid, normals)[k]))
    return targets, guards


def normalized_rows(features, target_count: int):
    epsilon = F(1, 1_000_000)
    names, raw_a, raw_b, scales = [], [], [], []
    for index, (name, item) in enumerate(features):
        requested = epsilon if index < target_count else F(0)
        a = [-x for x in item.grad]
        b = item.value - requested
        magnitude = max([abs(b), *(abs(x) for x in a)])
        assert magnitude > 0
        scale = F(1, 1) / magnitude
        names.append(name)
        raw_a.append([scale * x for x in a])
        raw_b.append(scale * b)
        scales.append(scale)
    return names, raw_a, raw_b, scales


def exact_dual_from_support(a, b, support):
    sub = [a[i] for i in support]
    kernel = exact.nullspace(exact.mat_transpose(sub))
    if len(kernel) != 1:
        return None, {"nullity": len(kernel)}
    y = kernel[0]
    if all(x <= 0 for x in y):
        y = [-x for x in y]
    if not all(x >= 0 for x in y) or not any(x > 0 for x in y):
        return None, {"nullity": 1, "kernel_decimal": [float(x) for x in y]}
    total = sum(y, F(0))
    y = [x / total for x in y]
    residual = [sum((sub[i][j] * y[i] for i in range(len(y))), F(0))
                for j in range(exact.DIM)]
    b_dot_y = sum((b[row] * weight for row, weight in zip(support, y)), F(0))
    return y, {"residual": residual, "b_dot_y": b_dot_y}


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--output", type=Path, default=HERE / "row54_full13_exact.json")
    args = ap.parse_args()
    targets, guards = all_features()
    features = targets + guards
    names, a, b, scales = normalized_rows(features, len(targets))
    af = np.asarray([[float(x) for x in row] for row in a])
    bf = np.asarray([float(x) for x in b])
    dual_lp = linprog(
        bf,
        A_eq=np.vstack((af.T, np.ones(len(bf)))),
        b_eq=np.r_[np.zeros(exact.DIM), 1.0],
        bounds=[(0, None)] * len(bf),
        method="highs",
        options={"dual_feasibility_tolerance": 1e-9,
                 "primal_feasibility_tolerance": 1e-9},
    )
    assert dual_lp.success, dual_lp.message
    candidates = [
        np.flatnonzero(dual_lp.x > tol).tolist()
        for tol in (1e-7, 1e-9, 1e-11, 1e-13)
    ]
    chosen = None
    diagnostics = []
    for support in candidates:
        y, audit = exact_dual_from_support(a, b, support)
        diagnostics.append({"support_size": len(support), "audit": {
            key: ([float(x) for x in value] if isinstance(value, list) else
                  float(value) if isinstance(value, F) else value)
            for key, value in audit.items()
        }})
        if y is not None and audit["b_dot_y"] < 0:
            chosen = (support, y, audit)
            break
    out = {
        "statement": "Exact rational Farkas certificate for complete 13-DOF primitive LP",
        "feature_count": len(features),
        "target_count": len(targets),
        "guard_count": len(guards),
        "float_dual_objective": float(dual_lp.fun),
        "float_support_diagnostics": diagnostics,
        "certificate_pass": chosen is not None,
    }
    if chosen is not None:
        support, y, audit = chosen
        out.update({
            "support": [{
                "row": row,
                "name": names[row],
                "scale": exact.frac_json(scales[row]),
                "A": [exact.frac_json(x) for x in a[row]],
                "b": exact.frac_json(b[row]),
                "y": exact.frac_json(weight),
            } for row, weight in zip(support, y)],
            "A_transpose_y": [exact.frac_json(x) for x in audit["residual"]],
            "b_dot_y": exact.frac_json(audit["b_dot_y"]),
        })
    args.output.parent.mkdir(parents=True, exist_ok=True)
    with args.output.open("w") as f:
        json.dump(out, f, indent=2)
    print(json.dumps({
        "feature_count": len(features),
        "float_dual_objective": float(dual_lp.fun),
        "diagnostics": diagnostics,
        "certificate_pass": out["certificate_pass"],
        "b_dot_y": out.get("b_dot_y", {}).get("decimal"),
        "support_names": [item["name"] for item in out.get("support", [])],
    }, indent=2))


if __name__ == "__main__":
    main()
