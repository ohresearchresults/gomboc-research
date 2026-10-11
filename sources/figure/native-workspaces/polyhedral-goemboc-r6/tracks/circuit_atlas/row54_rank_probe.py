#!/usr/bin/env python3
"""Rank-revealing 44-control Jacobian at an arbitrary saved metric packet."""
from __future__ import annotations

import argparse
import json
from pathlib import Path

import numpy as np

import row54_guarded_escape as guarded


HERE = Path(__file__).resolve().parent


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--source", default="row54_multiwall_flip.csv")
    ap.add_argument("--faces", default="row54_multiwall_flip_faces.json")
    ap.add_argument("--search", required=True)
    ap.add_argument("--fd-step", type=float, default=2e-5)
    ap.add_argument("--output", required=True)
    args = ap.parse_args()
    ids, source, faces = guarded.load_problem(HERE / args.source, HERE / args.faces)
    problem = guarded.Problem(ids, source, faces)
    search = json.load((HERE / args.search).open())
    x = np.zeros(44)
    x[:8] = np.asarray(search["theta"], dtype=float)
    guards, topology, jm, jt = guarded.finite_jacobian(problem, x, args.fd_step)
    active = guards <= 0.0
    record = {
        "version": 1,
        "source": args.source,
        "faces": args.faces,
        "search": args.search,
        "parameters": x.tolist(),
        "finite_difference_step": args.fd_step,
        "hard_target_margin": float(np.min(guards)),
        "minimum_topology_guard": float(np.min(topology)),
        "negative_guard_count": int(np.sum(active)),
        "negative_packet": [
            {"value": float(guards[k]), "feature": problem.mech_labels[k]}
            for k in np.flatnonzero(active)
        ],
        "active_packet_rank": guarded.rank_record(problem, jm, active),
    }
    json.dump(record, (HERE / args.output).open("w"), indent=2)
    print(json.dumps({
        "hard_target_margin": record["hard_target_margin"],
        "minimum_topology_guard": record["minimum_topology_guard"],
        "negative_packet": record["negative_packet"],
        "ranks": {
            key: value["rank"]
            for key, value in record["active_packet_rank"].items()
            if isinstance(value, dict) and "rank" in value
        },
        "singular_values": {
            key: value["singular_values"]
            for key, value in record["active_packet_rank"].items()
            if isinstance(value, dict) and "singular_values" in value
        },
    }, indent=2))


if __name__ == "__main__":
    main()
