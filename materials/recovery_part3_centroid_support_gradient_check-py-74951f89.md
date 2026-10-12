# material-74951f895af3

AI research material

<!-- historical-status:start -->
> **Historical AI material.** The title and claims below reflect the AI’s assessment at the time. Claims of proof, certification or completion are not a current verification verdict.
>
> [C622](../C622/README.md) passes the supplied exact checks; C<500 remains open; Minimum’s C≥34 remains a working lower bound requiring a consolidated proof. See [verification status and source gaps](../catalog/coverage.md).
<!-- historical-status:end -->

---

#!/usr/bin/env python3
"""Recovery capsule companion: exact support derivatives and translation gauge.

Requires the complete normal_fan_certificate.py supplied in capsule part 2.
No third-party packages. Run:
  python3 centroid_support_gradient_check.py --output gradient_checks.json
"""
from __future__ import annotations

import argparse
import hashlib
import itertools
from fractions import Fraction as F
from pathlib import Path
from typing import Any

import normal_fan_certificate as nf


def rank(columns: list[nf.Vec]) -> int:
    matrix = [[column[row] for column in columns] for row in range(3)]
    pivot_row = 0
    for col in range(len(columns)):
        candidate = next((row for row in range(pivot_row, 3) if matrix[row][col]), None)
        if candidate is None:
            continue
        matrix[pivot_row], matrix[candidate] = matrix[candidate], matrix[pivot_row]
        scale = matrix[pivot_row][col]
        matrix[pivot_row] = [x / scale for x in matrix[pivot_row]]
        for row in range(3):
            if row != pivot_row:
                factor = matrix[row][col]
                matrix[row] = [x - factor * y for x, y in zip(matrix[row], matrix[pivot_row])]
        pivot_row += 1
        if pivot_row == 3:
            break
    return pivot_row


def gradient_report(body: dict[str, Any]) -> dict[str, Any]:
    vertices = body["vertices"]
    normals = body["input"]["normals"]
    supports = body["input"]["supports"]
    volume = body["volume"]
    g = body["solid_centroid"]
    columns = []
    faces = []
    for i, cycle in enumerate(body["facet_cycles_outward"]):
        normal = normals[i]
        denominator = 2 * nf.dot(normal, normal)
        a = vertices[cycle[0]]
        area_over_normal_length = F(0)
        first_moment = nf.ZERO
        for k in range(1, len(cycle) - 1):
            b, c = vertices[cycle[k]], vertices[cycle[k + 1]]
            weight = nf.dot(nf.cross(nf.sub(b, a), nf.sub(c, a)), normal) / denominator
            assert weight > 0
            area_over_normal_length += weight
            first_moment = nf.add(first_moment, nf.mul(weight / 3, nf.sumvec((a, b, c))))
        face_centroid = nf.mul(1 / area_over_normal_length, first_moment)
        column = nf.mul(area_over_normal_length / volume, nf.sub(face_centroid, g))
        columns.append(column)
        faces.append({"facet": i, "area_over_normal_length": area_over_normal_length,
                      "face_centroid": face_centroid, "dg_dh": column})
    translation_tensor = [
        [sum((columns[i][row] * normals[i][col] for i in range(len(normals))), F(0))
         for col in range(3)] for row in range(3)]
    identity = [[F(row == col) for col in range(3)] for row in range(3)]
    assert translation_tensor == identity
    scaling_derivative = nf.sumvec(nf.mul(supports[i], columns[i]) for i in range(len(normals)))
    assert scaling_derivative == g
    anchors = next(ids for ids in itertools.combinations(range(len(normals)), 3)
                   if nf.det(*(normals[i] for i in ids)))
    free = [i for i in range(len(normals)) if i not in anchors]
    return {"faces": faces, "unrestricted_rank": rank(columns),
            "translation_tensor_JN": translation_tensor,
            "scaling_derivative_Jh": scaling_derivative, "solid_centroid": g,
            "fixed_three_plane_indices": anchors, "free_support_indices": free,
            "rank_after_three_plane_pin_before_other_constraints": rank([columns[i] for i in free]),
            "scope_note": "Further incidence or margin constraints must also be imposed before using this rank as a shape-control certificate."}


def run_tests() -> dict[str, Any]:
    base = nf.self_test()["reports"]
    names = ("regular_tetrahedron", "cube", "regular_octahedron", "sheared_tetrahedron_t1")
    reports = {name: gradient_report(base[name]) for name in names}
    for report in reports.values():
        assert report["unrestricted_rank"] == 3
    assert reports["regular_tetrahedron"]["rank_after_three_plane_pin_before_other_constraints"] == 1
    assert reports["cube"]["rank_after_three_plane_pin_before_other_constraints"] == 3
    # A cuboid's centroid is affine in each support; this is an exact finite-step test.
    cube = base["cube"]
    epsilon = F(1, 7)
    tests = []
    for i in range(6):
        perturbed = {"normals": cube["input"]["normals"],
                     "supports": cube["input"]["supports"][:]}
        perturbed["supports"][i] += epsilon
        shifted = nf.certify(perturbed)
        observed = nf.mul(1 / epsilon, nf.sub(shifted["solid_centroid"], cube["solid_centroid"]))
        expected = reports["cube"]["faces"][i]["dg_dh"]
        assert observed == expected
        tests.append({"facet": i, "epsilon": epsilon, "difference_quotient": observed})
    return {"schema_version": 1, "test_status": "GRADIENT_SELFTEST_OK", "reports": reports,
            "exact_cube_finite_steps": tests,
            "research_status": "Exact method and gauge checks, not a class110 construction or a global centering theorem."}


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", required=True, type=Path)
    args = parser.parse_args()
    result = run_tests()
    payload = nf.canonical_json(result)
    args.output.write_bytes(payload)
    print("GRADIENT_SELFTEST_OK")
    print(f"OUTPUT_BYTES {len(payload)}")
    print(f"OUTPUT_SHA256 {hashlib.sha256(payload).hexdigest()}")
    for name, report in result["reports"].items():
        print(name, "rank", report["unrestricted_rank"],
              "pinned_rank", report["rank_after_three_plane_pin_before_other_constraints"])


if __name__ == "__main__":
    main()
