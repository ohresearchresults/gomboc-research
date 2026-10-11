#!/usr/bin/env python3
"""Rationalize one atlas direction and locate its first exact path events."""
from __future__ import annotations

import argparse
import hashlib
import json
import math
from fractions import Fraction as Q
from pathlib import Path

import numpy as np

import attack_common as c


ex = c.frozen.ex
gx = c.frozen.gx


def canonical_hash(value):
    return hashlib.sha256(
        json.dumps(value, sort_keys=True, separators=(",", ":")).encode()
    ).hexdigest()


def local_name(path: Path):
    return str(path.resolve().relative_to(c.HERE))


def polynomial_key(poly):
    pivot = next((z for z in poly.c if z), None)
    if pivot is None:
        return ("0",)
    return tuple(ex.qs(z / pivot) for z in poly.c)


def positive_real_roots(poly, maximum):
    coefficients = np.asarray([float(z) for z in poly.c], dtype=float)
    if len(coefficients) <= 1:
        return []
    magnitude = float(np.max(np.abs(coefficients)))
    if not magnitude:
        return []
    coefficients /= magnitude
    roots = np.roots(coefficients[::-1])
    out = []
    for root in roots:
        if abs(float(root.imag)) > 2e-8 * max(1.0, abs(float(root.real))):
            continue
        value = float(root.real)
        if 1e-12 < value <= maximum:
            out.append(value)
    return sorted(out)


def isolate_near(poly, approximate, sibling_roots, maximum):
    ordered = [0.0] + sorted(sibling_roots) + [maximum]
    index = min(
        range(1, len(ordered) - 1),
        key=lambda k: abs(ordered[k] - approximate),
    )
    left_neighbor, right_neighbor = ordered[index - 1], ordered[index + 1]
    local_gap = min(approximate - left_neighbor, right_neighbor - approximate)
    radius = max(1e-12, min(0.2 * local_gap, 2e-7 * max(1.0, approximate)))
    for _ in range(30):
        lo = Q(format(max(0.0, approximate - radius), ".17g"))
        hi = Q(format(min(maximum, approximate + radius), ".17g"))
        vlo, vhi = poly.eval(lo), poly.eval(hi)
        if vlo and vhi and ((vlo > 0) != (vhi > 0)):
            try:
                root = ex.isolate_monotone_root(poly, lo, hi, Q(1, 10**18))
            except AssertionError:
                radius *= 0.4
                continue
            return root
        radius *= 1.8
        radius = min(radius, 0.45 * local_gap)
    raise AssertionError(("failed exact root bracket", approximate, sibling_roots))


def root_record(poly, root):
    return {
        "polynomial_degree": poly.degree,
        "polynomial_digest": canonical_hash(poly.exact()),
        "lo": ex.qs(root["lo"]),
        "hi": ex.qs(root["hi"]),
        "value_lo": ex.qs(root["value_lo"]),
        "value_hi": ex.qs(root["value_hi"]),
        "derivative_sign": root["derivative_sign"],
        "derivative_bernstein_leaves": root["derivative_bernstein_leaves"],
        "decimal_interval": [float(root["lo"]), float(root["hi"])],
    }


def earliest_groups(records, maximum, count=20):
    grouped = {}
    for label, poly in records:
        key = polynomial_key(poly)
        packet = grouped.setdefault(key, {"poly": poly, "labels": []})
        packet["labels"].append(label)
    approximate_candidates = []
    for packet in grouped.values():
        roots = positive_real_roots(packet["poly"], maximum)
        for approximate in roots:
            approximate_candidates.append(
                (approximate, packet["poly"], packet["labels"], roots)
            )
    approximate_candidates.sort(key=lambda item: item[0])
    # Exact-isolating every positive root of every ledger polynomial is
    # unnecessary for locating the first events and makes dense rays
    # prohibitively expensive.  Isolate a conservative prefix of the numeric
    # ordering, then sort again by exact lower endpoint.
    candidates = []
    for approximate, poly, labels, roots in approximate_candidates[: max(40, 2 * count)]:
        try:
            exact_root = isolate_near(poly, approximate, roots, maximum)
        except AssertionError:
            continue
        candidates.append((float(exact_root["lo"]), poly, labels, exact_root))
    candidates.sort(key=lambda item: item[0])
    return candidates[:count], len(grouped)


def write_csv(path, ids, points):
    import csv

    with path.open("w", newline="") as stream:
        out = csv.writer(stream)
        out.writerow(("source_id", "x", "y", "z"))
        for i in ids:
            out.writerow((i, *(format(float(z), ".17g") for z in points[i])))


def exact_hull(points):
    """Fresh floating triangulation followed by fail-closed exact support."""
    float_packet = c.frozen.float_points(points)
    failures = []
    for tolerance in (2e-12, 8e-13, 3e-13, 1e-13, 3e-14, 1e-14):
        result = c.fresh_evaluate(float_packet, coplanar_rel=tolerance)
        if not result.valid:
            failures.append([tolerance, result.error])
            continue
        faces = [face["cycle"] for face in result.faces]
        try:
            support = ex.supporting_cell(points, faces)
        except AssertionError as error:
            failures.append([tolerance, repr(error)[:500]])
            continue
        return faces, support, tolerance
    raise AssertionError(("no exact-supported fresh hull", failures))


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--atlas", type=Path, default=c.HERE / "branch_atlas.json")
    ap.add_argument("--branch", type=int, default=5)
    ap.add_argument("--direction", type=Path, default=None)
    ap.add_argument("--maximum", type=float, default=8.0)
    ap.add_argument("--output", type=Path, default=c.HERE / "branch5_scan.json")
    args = ap.parse_args()

    if args.direction is None:
        atlas = json.loads(args.atlas.read_text())
        branch = atlas["branches"][args.branch]
        if not branch["success"]:
            raise RuntimeError(("atlas branch did not solve", args.branch))
        coefficients = np.asarray(branch["direction"], dtype=float)
        direction_source = {
            "type": "branch_atlas",
            "path": local_name(args.atlas),
            "sha256": hashlib.sha256(args.atlas.read_bytes()).hexdigest(),
            "branch_index": args.branch,
            "components": branch["components"],
            "relative_descent": branch["relative_descent"],
        }
    else:
        sparse_ray = json.loads(args.direction.read_text())
        coefficients = np.asarray(sparse_ray["direction"], dtype=float)
        direction_source = {
            "type": "sparse_ray",
            "path": local_name(args.direction),
            "sha256": hashlib.sha256(args.direction.read_bytes()).hexdigest(),
            "components": sparse_ray["active_components"],
            "relative_descent": min(sparse_ray["realized_relative_decrease"]),
        }
    exact_far, faces, source_record = c.reconstruct_exact_far()
    ids = sorted(exact_far)
    velocity, scale = c.exact_velocity_from_coefficients(
        exact_far, ids, coefficients
    )
    path = c.frozen.line_points(exact_far, velocity)

    support_records = []
    support_metadata = {}
    for face_index, witness, poly in ex.support_polynomials(path, faces):
        key = f"support:f{face_index}:w{witness}"
        support_records.append((key, poly))
        support_metadata[key] = {
            "face_index": face_index,
            "face": faces[face_index],
            "witness": witness,
        }
    support_events, support_group_count = earliest_groups(
        support_records, args.maximum
    )
    if not support_events:
        raise AssertionError("no support event in declared interval")

    _, all_records = gx.all_primitives(path, faces)
    mechanics_records = [
        (name, poly)
        for name, poly, _ in all_records
        if name.startswith(("face:", "vertex:", "edge:"))
    ]
    # Only mechanics roots preceding (or numerically coincident with) the
    # first support wall can invalidate the claimed first event.
    mechanics_limit = min(
        args.maximum, support_events[0][0] * (1.0 + 1e-8) + 1e-10
    )
    mechanics_events, mechanics_group_count = earliest_groups(
        mechanics_records, mechanics_limit, count=12
    )

    first = support_events[0]
    root_lo, root_hi = first[3]["lo"], first[3]["hi"]
    coincidence_tolerance = max(1e-10, 2e-8 * max(1.0, first[0]))
    first_cluster = [
        item for item in support_events
        if abs(item[0] - first[0]) <= coincidence_tolerance
    ]
    distinct_later = [
        item[0] for item in support_events
        if item[0] > first[0] + coincidence_tolerance
    ]
    # Use rational samples far enough from the wall for independent Qhull,
    # but before the midpoint to the next distinct exact event.
    next_time = min(distinct_later) if distinct_later else min(
        args.maximum, first[0] + 1.0
    )
    maximum_gap = 0.2 * min(first[0], next_time - first[0])
    if maximum_gap <= 0:
        raise AssertionError(("no strict sampling interval", first[0], next_time))
    gap = maximum_gap
    pre_t = Q(format(first[0] - gap, ".17g"))
    post_t = Q(format(first[0] + gap, ".17g"))
    if not (pre_t < root_lo < root_hi < post_t):
        raise AssertionError((pre_t, root_lo, root_hi, post_t))
    pre_points = c.frozen.at(path, pre_t)
    post_points = c.frozen.at(path, post_t)
    pre_faces, pre_support, pre_hull_tolerance = exact_hull(pre_points)
    post_faces, post_support, post_hull_tolerance = exact_hull(post_points)
    _, pre_mechanics = ex.classify_point(pre_points, pre_faces)
    _, post_mechanics = ex.classify_point(post_points, post_faces)
    pre_edges = set(ex.edge_data(pre_faces)[0])
    post_edges = set(ex.edge_data(post_faces)[0])
    pre_keys, post_keys = c.face_keys(pre_faces), c.face_keys(post_faces)
    write_csv(args.output.with_name("event_pre.csv"), ids, pre_points)
    write_csv(args.output.with_name("event_post.csv"), ids, post_points)
    args.output.with_name("event_pre_faces.json").write_text(
        json.dumps(pre_faces, indent=2) + "\n"
    )
    args.output.with_name("event_post_faces.json").write_text(
        json.dumps(post_faces, indent=2) + "\n"
    )

    def encode_event(item, support=False):
        _, poly, labels, root = item
        record = root_record(poly, root)
        record["labels"] = labels
        if support:
            record["support_rows"] = [support_metadata[label] for label in labels]
        return record

    payload = {
        "version": 1,
        "method": (
            "exact rationalization of one complete-atlas direction; exact "
            "polynomial root isolation and fresh rational cells"
        ),
        "direction_source": direction_source,
        "source_reconstruction": source_record,
        "chart_scale": scale,
        "velocity": {
            str(i): [ex.qs(z) for z in velocity[i]] for i in ids
        },
        "velocity_digest": canonical_hash(
            {str(i): [ex.qs(z) for z in velocity[i]] for i in ids}
        ),
        "maximum_parameter_scanned": args.maximum,
        "support_polynomial_count": len(support_records),
        "unique_support_polynomial_count": support_group_count,
        "mechanics_polynomial_count": len(mechanics_records),
        "unique_mechanics_polynomial_count": mechanics_group_count,
        "earliest_support_events": [
            encode_event(item, support=True) for item in support_events
        ],
        "earliest_mechanics_events": [
            encode_event(item, support=False) for item in mechanics_events
        ],
        "selected_event": {
            "root": root_record(first[1], first[3]),
            "support_rows": [
                support_metadata[label]
                for item in first_cluster
                for label in item[2]
            ],
            "pre_parameter": ex.qs(pre_t),
            "post_parameter": ex.qs(post_t),
            "pre": {
                "support": pre_support,
                "fresh_hull_coplanar_rel": pre_hull_tolerance,
                "mechanics": pre_mechanics,
                "base_present": c.BASE in pre_keys,
                "missing_rails": [
                    list(edge) for edge in sorted(c.rail_edges() - pre_edges)
                ],
            },
            "post": {
                "support": post_support,
                "fresh_hull_coplanar_rel": post_hull_tolerance,
                "mechanics": post_mechanics,
                "base_present": c.BASE in post_keys,
                "missing_rails": [
                    list(edge) for edge in sorted(c.rail_edges() - post_edges)
                ],
            },
            "removed_faces": [
                sorted(face) for face in sorted(pre_keys - post_keys, key=sorted)
            ],
            "added_faces": [
                sorted(face) for face in sorted(post_keys - pre_keys, key=sorted)
            ],
            "removed_edges": [list(edge) for edge in sorted(pre_edges - post_edges)],
            "added_edges": [list(edge) for edge in sorted(post_edges - pre_edges)],
        },
    }
    args.output.write_text(json.dumps(payload, indent=2) + "\n")
    print(
        json.dumps(
            {
                "direction_source": direction_source,
                "first_support": payload["selected_event"]["root"][
                    "decimal_interval"
                ],
                "first_support_rows": payload["selected_event"]["support_rows"],
                "first_mechanics": (
                    None
                    if not mechanics_events
                    else payload["earliest_mechanics_events"][0]
                ),
                "pre_f_vector": pre_support["f_vector"],
                "post_f_vector": post_support["f_vector"],
                "pre_class": pre_mechanics["class"],
                "post_class": post_mechanics["class"],
                "removed_faces": payload["selected_event"]["removed_faces"],
                "added_faces": payload["selected_event"]["added_faces"],
                "missing_post_rails": payload["selected_event"]["post"][
                    "missing_rails"
                ],
            },
            indent=2,
        )
    )


if __name__ == "__main__":
    main()
