#!/usr/bin/env python3
"""Exact diagnostic for the newly born far-cell edge (256,258).

This is intentionally a read-only analysis utility.  It distinguishes roots
forced by the support flip from later mechanics roots before changing the
certificate builder.
"""
from __future__ import annotations

from fractions import Fraction as Q

import post_c17_exact as pc


def isolate(power, left: Q, right: Q, digits: int = 14):
    """Return disjoint decimal-grid brackets, one per exact Sturm root."""
    target = Q(1, 10**digits)
    pending = [(left, right, pc.root_count(power, left, right))]
    out = []
    while pending:
        a, b, count = pending.pop()
        if not count:
            continue
        if count == 1 and b - a <= target:
            out.append((a, b))
            continue
        middle = (a + b) / 2
        left_count = pc.root_count(power, a, middle)
        right_count = pc.root_count(power, middle, b)
        assert left_count + right_count == count
        pending.append((middle, b, right_count))
        pending.append((a, middle, left_count))
    return sorted(out)


def sign(z, parameter: Q) -> str:
    value = z.at(parameter)
    return "+" if value > 0 else "-" if value < 0 else "0"


def main():
    rows0 = pc.read_rows()
    _, _, faces, _ = pc.exact_cell("support_far", pc.SUPPORT_FAR_SAMPLE, rows0)
    q, centroid, _ = pc.symbolic_path(rows0, faces)
    incidence = pc.esc.incidence(faces)
    edge = (256, 258)
    components = pc.esc.symbolic_edge_components(edge, incidence[edge], faces, q, centroid)
    samples = (
        ("support_left", pc.SUPPORT_LEFT),
        ("support_right", pc.SUPPORT_RIGHT),
        ("far_sample", pc.SUPPORT_FAR_SAMPLE),
        ("endpoint", pc.END),
    )
    print("edge", edge)
    for name, z in components.items():
        numerator_roots = pc.root_count(z.n, pc.SUPPORT_LEFT, pc.END)
        denominator_roots = pc.root_count(z.d, pc.SUPPORT_LEFT, pc.END)
        print(
            name,
            "degrees",
            len(z.n) - 1,
            len(z.d) - 1,
            "signs",
            [(label, sign(z, parameter)) for label, parameter in samples],
            "roots",
            numerator_roots,
            denominator_roots,
        )
        if numerator_roots:
            print(
                " numerator_brackets",
                [(pc.qs(a), pc.qs(b)) for a, b in isolate(z.n, pc.SUPPORT_LEFT, pc.END)],
            )
        if denominator_roots:
            print(
                " denominator_brackets",
                [(pc.qs(a), pc.qs(b)) for a, b in isolate(z.d, pc.SUPPORT_LEFT, pc.END)],
            )


if __name__ == "__main__":
    main()
