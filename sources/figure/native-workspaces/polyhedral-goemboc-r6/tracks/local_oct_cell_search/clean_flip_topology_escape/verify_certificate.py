#!/usr/bin/env python3
"""Recompute and verify the frozen six-flip continuum certificate.

This is intentionally a verifier, not a second search.  It reconstructs the
two rational lines from the named source, recomputes every circuit root and
every open-cell support-sign proof, rebuilds all representative and wall
hulls, and checks the projective tail and the generated-file manifest against
the frozen JSON certificate.
"""
from __future__ import annotations

import json
import math
from fractions import Fraction as Q

import build_certificate as b


def same_record(got, want):
    """Compare the exact, hash-addressed portion of an endpoint record."""
    keys = (
        "coordinate_hash",
        "face_hash",
        "exact_support",
        "active_labels",
        "exact_mechanics",
        "mechanics_ledger",
        "base_face_present",
        "forced_rail_count",
        "missing_forced_rails",
    )
    for key in keys:
        if key in ("exact_support", "mechanics_ledger"):
            if got[key].keys() != want[key].keys():
                raise AssertionError((key, got[key].keys(), want[key].keys()))
            log_diagnostic = {
                "exact_support": "min_support_log10_abs",
                "mechanics_ledger": "minimum_nonzero_log10_abs",
            }[key]
            for support_key in got[key]:
                if support_key == log_diagnostic:
                    # This is only a human-readable diagnostic derived by
                    # libm from an exact Fraction.  The exact coordinates,
                    # face ledger, support signs, and support count remain
                    # strict above and below; different libm builds may round
                    # this logarithm by a few ulps.
                    if not math.isclose(
                        got[key][support_key],
                        want[key][support_key],
                        rel_tol=0.0,
                        abs_tol=5e-13,
                    ):
                        raise AssertionError(
                            (
                                key,
                                support_key,
                                got[key][support_key],
                                want[key][support_key],
                            )
                        )
                elif got[key][support_key] != want[key][support_key]:
                    raise AssertionError(
                        (
                            key,
                            support_key,
                            got[key][support_key],
                            want[key][support_key],
                        )
                    )
            continue
        if got[key] != want[key]:
            raise AssertionError((key, got[key], want[key]))


def verify_leg(path, specs, lo, hi, frozen):
    roots = sorted(
        (b.root_of_line(path, quad), label, quad) for label, quad in specs
    )
    if [b.ex.qs(root) for root, _, _ in roots] != frozen["root_order"]:
        raise AssertionError("root order changed")
    if not all(lo < root < hi for root, _, _ in roots):
        raise AssertionError("root left the declared segment")

    bounds = [lo] + [root for root, _, _ in roots] + [hi]
    for k, expected in enumerate(frozen["intervals"]):
        left = bounds[k] if k == 0 else bounds[k] * (1 + b.ROOT_EPS)
        right = (
            bounds[k + 1]
            if k == len(bounds) - 2
            else bounds[k + 1] * (1 - b.ROOT_EPS)
        )
        mid = (left + right) / 2
        if b.ex.qs(mid) != expected["representative"]:
            raise AssertionError("representative changed")
        points = b.at(path, mid)
        faces, _ = b.qhull_faces(points)
        if b.face_hash(faces) != expected["face_hash"]:
            raise AssertionError("open-cell face ledger changed")
        support = b.support_interval_audit(b.restrict(path, left, right), faces)
        if support != expected["support_certificate"]:
            raise AssertionError("Bernstein support proof changed")
        same_record(
            b.endpoint_record("unused", points, faces, write=False),
            expected["checkpoint"],
        )

    for k, ((root, label, quad), expected) in enumerate(
        zip(roots, frozen["events"]), start=1
    ):
        if label != expected["label"] or list(quad) != expected["quad"]:
            raise AssertionError("event identity changed")
        if b.ex.qs(root) != expected["root_exact"]:
            raise AssertionError("event root changed")
        if b.wall_bracket(path, quad, root) != expected["directed_bracket"]:
            raise AssertionError("directed root bracket changed")
        wall = b.at(path, root)
        faces, _ = b.qhull_faces(wall)
        same_record(
            b.endpoint_record("unused", wall, faces, write=False),
            expected["wall"],
        )
        if expected["wall"]["exact_support"]["f_vector"] != [61, 161, 102]:
            raise AssertionError("wall is not a single circuit merger")
    return roots


def main():
    frozen = json.loads((b.HERE / "certificate.json").read_text())
    if frozen["verdict"] != "STRICT_ACTUAL_MULTI_CELL_PASSAGE_WITH_ALL37_RAILS":
        raise AssertionError("unexpected frozen verdict")

    if b.sha256_file(b.SOURCE) != frozen["source"]["coordinate_file_sha256"]:
        raise AssertionError("source coordinates changed")
    if b.sha256_file(b.SOURCE_FACES) != frozen["source"]["face_file_sha256"]:
        raise AssertionError("source faces changed")
    for name, digest in frozen["generated_file_sha256"].items():
        if b.sha256_file(b.HERE / name) != digest:
            raise AssertionError(("generated file changed", name))

    source, repair = b.gx.read_repaired(b.SOURCE)
    if repair != frozen["source"]["base_repair"]:
        raise AssertionError("exact base repair changed")
    source_faces = json.loads(b.SOURCE_FACES.read_text())
    same_record(
        b.endpoint_record("unused", source, source_faces, write=False),
        frozen["source"]["checkpoint"],
    )

    e1, e2 = b.ex.sub(source[1], source[0]), b.ex.sub(source[2], source[0])
    velocity = {i: (Q(0), Q(0), Q(0)) for i in source}
    for i, (a, c) in b.BUFFER_COEFFICIENTS.items():
        velocity[i] = b.ex.add(b.ex.mul(e1, a), b.ex.mul(e2, c))
    buffer_path = b.line_points(source, velocity)
    buffered = b.at(buffer_path, Q(1))
    buffer_specs = [
        ("buffer_flip_3_4_243_244", (3, 4, 243, 244)),
        ("buffer_flip_5_6_244_245", (5, 6, 244, 245)),
    ]
    verify_leg(buffer_path, buffer_specs, Q(0), Q(1), frozen["buffer_leg"])

    unit_velocity = {i: (Q(0), Q(0), Q(0)) for i in source}
    unit_velocity[244] = (Q(0), Q(0), Q(-1))
    unit_path = b.line_points(source, unit_velocity)
    depth = b.root_of_line(unit_path, (198, 243, 244, 245))
    if b.ex.qs(depth) != frozen["construction"]["target_row244_z_depth_exact"]:
        raise AssertionError("target depth changed")
    cross_velocity = {i: b.ex.mul(unit_velocity[i], depth) for i in source}
    cross_path = b.line_points(buffered, cross_velocity)
    cross_specs = [
        ("reverse_flip_3_4_243_244", (3, 4, 243, 244)),
        ("reverse_flip_5_6_244_245", (5, 6, 244, 245)),
        ("bridge_flip_4_5_243_244", (4, 5, 243, 244)),
        ("target_flip_198_243_244_245", (198, 243, 244, 245)),
    ]
    cross_roots = verify_leg(
        cross_path, cross_specs, Q(0), b.CROSS_POST, frozen["cross_leg"]
    )
    if cross_roots[-1][0] != 1:
        raise AssertionError("target flip is no longer at literal parameter one")

    post = b.at(cross_path, b.CROSS_POST)
    post_faces, _ = b.qhull_faces(post)
    same_record(
        b.endpoint_record("unused", post, post_faces, write=False),
        frozen["post_target"],
    )
    mid, _ = b.projective_endpoint(post, Q(3, 4))
    far, _ = b.projective_endpoint(post, Q(3, 2))
    same_record(
        b.endpoint_record("unused", mid, post_faces, write=False),
        frozen["projective_continuation"]["mid"],
    )
    same_record(
        b.endpoint_record("unused", far, post_faces, write=False),
        frozen["projective_continuation"]["far"],
    )
    residual = b.exact_residual_block(far, post_faces)
    if residual != frozen["far_residual_block"]:
        raise AssertionError("far residual packet changed")

    print("EXACT_RAIL_VALID_SIX_FLIP_FROZEN_CONTINUUM_PASS")


if __name__ == "__main__":
    main()
