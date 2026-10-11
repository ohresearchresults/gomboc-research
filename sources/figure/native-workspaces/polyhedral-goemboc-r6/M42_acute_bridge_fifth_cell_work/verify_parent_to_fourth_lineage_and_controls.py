#!/usr/bin/env python3
"""Independent exact verifier for the M42 three-cell -> fourth-cell lineage.

Uses only the Python standard library.  It does not import either materializer,
any stored hull object, or any numerical geometry package.  The two bundled
clean-room hull verifiers separately reconstruct the complete H/V/E lattices.
This file verifies the exact inter-endpoint construction, the mandatory packet
incidence replacement, the two independent nonmoment wall controls, and the
rank-5 block formed by those controls plus the three exact moment translations.
"""
from __future__ import annotations

from fractions import Fraction as Q
from pathlib import Path
import csv
import hashlib
import json
import math
import sys
from typing import Dict, Iterable, List, Sequence, Tuple

ROOT = Path(__file__).resolve().parent
PARENT = ROOT / "parent_M42_three_cell_exact"
CHILD = ROOT / "fourth_cell_endpoint"
Vec = Tuple[Q, Q, Q]


def q(s: object) -> Q:
    return s if isinstance(s, Q) else Q(str(s))


def add(a: Vec, b: Vec) -> Vec:
    return tuple(a[k] + b[k] for k in range(3))  # type: ignore[return-value]


def sub(a: Vec, b: Vec) -> Vec:
    return tuple(a[k] - b[k] for k in range(3))  # type: ignore[return-value]


def mul(a: Vec, t: Q) -> Vec:
    return tuple(a[k] * t for k in range(3))  # type: ignore[return-value]


def dot(a: Sequence[Q], b: Sequence[Q]) -> Q:
    return sum((a[k] * b[k] for k in range(3)), Q(0))


def det3(a: Vec, b: Vec, c: Vec) -> Q:
    return (
        a[0] * (b[1] * c[2] - b[2] * c[1])
        - a[1] * (b[0] * c[2] - b[2] * c[0])
        + a[2] * (b[0] * c[1] - b[1] * c[0])
    )


def matvec(A: Sequence[Sequence[Q]], p: Vec) -> Vec:
    return tuple(sum((A[i][j] * p[j] for j in range(3)), Q(0)) for i in range(3))  # type: ignore[return-value]


def read_parent_rows() -> Tuple[Dict[int, Vec], Dict[int, bool]]:
    rows: Dict[int, Vec] = {}
    active: Dict[int, bool] = {}
    with (PARENT / "coordinates_all_exact.csv").open(newline="") as f:
        for r in csv.DictReader(f):
            i = int(r["source_id"])
            rows[i] = tuple(q(r[k]) for k in ("x_exact", "y_exact", "z_exact"))  # type: ignore[assignment]
            active[i] = bool(int(r["active"]))
    return rows, active


def read_exact_transform_rows() -> Dict[int, Vec]:
    rows: Dict[int, Vec] = {}
    with (CHILD / "input_rows_exact.csv").open(newline="") as f:
        for r in csv.DictReader(f):
            i = int(r["source_id"])
            rows[i] = tuple(q(r[k]) for k in ("x_exact", "y_exact", "z_exact"))  # type: ignore[assignment]
    return rows


def read_common_rows() -> Tuple[Dict[int, Vec], Dict[int, Tuple[int, int, int]], int]:
    rows: Dict[int, Vec] = {}
    nums: Dict[int, Tuple[int, int, int]] = {}
    scale = None
    with (CHILD / "input_rows_common_lattice.csv").open(newline="") as f:
        for r in csv.DictReader(f):
            i = int(r["source_id"])
            d = int(r["denominator"])
            if scale is None:
                scale = d
            assert scale == d
            xyz = tuple(int(r[k]) for k in ("x_int", "y_int", "z_int"))
            nums[i] = xyz  # type: ignore[assignment]
            rows[i] = tuple(Q(z, d) for z in xyz)  # type: ignore[assignment]
    assert scale is not None
    return rows, nums, scale


def read_edges(path: Path) -> set[Tuple[int, int]]:
    out: set[Tuple[int, int]] = set()
    with path.open(newline="") as f:
        for r in csv.DictReader(f):
            a, b = int(r["u"]), int(r["v"])
            out.add(tuple(sorted((a, b))))
    return out


def face_sets(path: Path) -> List[frozenset[int]]:
    data = json.load(path.open())
    return [frozenset(map(int, c)) for c in data]


def circuit_affine_root(rows: Dict[int, Vec], ids: Sequence[int], moving: int) -> Tuple[Q, Q, Q, Q]:
    assert len(ids) == 4 and moving in ids

    def value(t: Q) -> Q:
        p = [rows[i] for i in ids]
        p[ids.index(moving)] = mul(rows[moving], t)
        return det3(sub(p[1], p[0]), sub(p[2], p[0]), sub(p[3], p[0]))

    f0 = value(Q(0))
    f1 = value(Q(1))
    slope = f1 - f0
    assert slope != 0
    root = -f0 / slope
    assert value(root) == 0
    return f0, slope, root, f1


def verify_manifest(directory: Path) -> int:
    manifest = directory / "SHA256SUMS.txt"
    checked = 0
    for line in manifest.read_text().splitlines():
        line = line.strip()
        if not line:
            continue
        digest, rel = line.split(None, 1)
        rel = rel.lstrip(" *")
        p = directory / rel
        assert p.is_file(), p
        got = hashlib.sha256(p.read_bytes()).hexdigest()
        assert got == digest, (p, digest, got)
        checked += 1
    return checked


def main() -> None:
    sys.set_int_max_str_digits(0)
    pcert = json.load((PARENT / "certificate.json").open())
    ccert = json.load((CHILD / "certificate.json").open())
    provenance = json.load((CHILD / "search_provenance.json").open())
    atlas = json.load((CHILD / "first_chamber_atlas.json").open())
    complex4 = json.load((CHILD / "fourth_cell_complex.json").open())
    graph = json.load((CHILD / "graph_radial_obstruction.json").open())
    interval = json.load((CHILD / "interval_certificate.json").open())

    # Integrity of the two immutable input bundles.
    parent_manifest_files = verify_manifest(PARENT)
    child_manifest_files = verify_manifest(CHILD)

    # Independent reconstruction summary checks for the exact M42 parent.
    parent_rows, parent_active_flags = read_parent_rows()
    parent_ids = set(parent_rows)
    pactive = set(map(int, pcert["active_rows"]))
    pinactive = set(map(int, pcert["inactive_rows"]))
    assert len(parent_rows) == pcert["input_rows"] == 134
    assert pactive.isdisjoint(pinactive) and pactive | pinactive == parent_ids
    assert pactive == {i for i, flag in parent_active_flags.items() if flag}
    assert tuple(pcert["f_vector"]) == (92, 256, 166)
    assert tuple(pcert["class"]) == (2, 2, 2)
    assert pcert["centered_first_moments_exact"] == ["0/1", "0/1", "0/1"]
    pfaces = face_sets(PARENT / "face_cycles.json")
    pedges = read_edges(PARENT / "true_edges.csv")
    assert len(pfaces) == 166 and len(pedges) == 256
    assert len(pactive) - len(pedges) + len(pfaces) == 2
    assert frozenset((201, 220, 221)) in pfaces
    assert (153, 154) in pedges and (130, 222) in pedges and (176, 182) in pedges
    assert {z["vertex"] for z in pcert["unstable_vertices"]} == {8, 153}
    assert {tuple(z["edge"]) for z in pcert["saddle_edges"]} == {(130, 222), (176, 182)}
    assert pcert["radial_order"]["target_unique_farthest"] is True

    # Recreate the exact pre-common-lattice fourth-cell construction from the
    # parent rows and the finite rational generator in search_provenance.json.
    C = tuple(q(z) for z in pcert["centroid_unshifted_exact"])  # type: ignore[assignment]
    pre: Dict[int, Vec] = {i: sub(v, C) for i, v in parent_rows.items()}
    absorbed = set(map(int, provenance["absorbed_rows"]))
    expected_absorbed = {130, 153, 154, 176, 182, 201, 220, 221, 222}
    assert absorbed == expected_absorbed
    for i in absorbed:
        pre[i] = (Q(0), Q(0), Q(0))
    for key, xyz in provenance["new_pretransform_rows"].items():
        pre[int(key)] = tuple(q(z) for z in xyz)  # type: ignore[assignment]

    scales = [q(z) for z in provenance["rational_group_scales"]]
    groups = [range(155, 176), range(183, 199), range(202, 218)]
    for fac, group in zip(scales, groups):
        assert fac > 0
        for i in group:
            if i in pre:
                pre[i] = mul(pre[i], fac)

    u = tuple(q(z) for z in provenance["rational_projective_u"])  # type: ignore[assignment]
    L = tuple(tuple(q(z) for z in row) for row in provenance["rational_linear_map"])
    detL = det3(L[0], L[1], L[2])
    assert detL > 0
    reconstructed: Dict[int, Vec] = {}
    denominators: Dict[int, Q] = {}
    for i, p in pre.items():
        den = Q(1) - dot(u, p)
        assert den > 0
        denominators[i] = den
        reconstructed[i] = matvec(L, mul(p, Q(1) / den))

    exact_transform_rows = read_exact_transform_rows()
    assert set(reconstructed) == set(exact_transform_rows)
    assert reconstructed == exact_transform_rows
    assert len(reconstructed) == 140
    min_den_row = min(denominators, key=denominators.get)
    min_projective_denominator = denominators[min_den_row]

    # The authoritative endpoint is a second exact rowwise lattice map.  Record
    # and bound every rational correction instead of hiding the exactification.
    common_rows, common_nums, common_scale = read_common_rows()
    assert set(common_rows) == set(reconstructed)
    deltas = {
        (i, k): common_rows[i][k] - reconstructed[i][k]
        for i in reconstructed
        for k in range(3)
    }
    max_delta_key = max(deltas, key=lambda ik: abs(deltas[ik]))
    max_exactification_delta = abs(deltas[max_delta_key])
    assert max_exactification_delta < Q(1, 4_000_000_000)  # < 2.5e-10 exactly
    assert all(common_rows[i] == (Q(0), Q(0), Q(0)) for i in absorbed)

    # Exact protected-base coplanarity in the authoritative common lattice.
    projection = json.load((CHILD / "common_lattice_projection.json").open())
    n = tuple(map(int, projection["base_plane_integer_coordinate_normal"]))
    h = int(projection["base_plane_integer_coordinate_h"])
    K = abs(n[2])
    assert common_scale == int(projection["common_denominator"])
    assert common_scale == int(projection["original_rounding_denominator"]) * K
    for i in range(17):
        assert sum(n[k] * common_nums[i][k] for k in range(3)) == K * h

    # Exact child H/V/E and packet replacement summary checks.  The bundled
    # clean-room verifier independently reconstructs these from all triples.
    cactive = set(map(int, ccert["active_rows"]))
    cinactive = set(map(int, ccert["inactive_rows"]))
    assert len(common_rows) == ccert["input_rows"] == 140
    assert cactive.isdisjoint(cinactive) and cactive | cinactive == set(common_rows)
    assert tuple(ccert["f_vector"]) == (83, 229, 148)
    assert tuple(ccert["class"]) == (2, 2, 2)
    assert ccert["centered_first_moments_exact"] == ["0/1", "0/1", "0/1"]
    cfaces = face_sets(CHILD / "face_cycles.json")
    cedges = read_edges(CHILD / "true_edges.csv")
    assert len(cfaces) == 148 and len(cedges) == 229
    assert len(cactive) - len(cedges) + len(cfaces) == 2
    assert absorbed <= cinactive
    assert frozenset((201, 220, 221)) not in cfaces
    assert (153, 154) not in cedges and (130, 222) not in cedges and (176, 182) not in cedges
    new_edges = {tuple(map(int, e)) for e in complex4["new_true_edges"]}
    assert new_edges <= cedges
    assert len(complex4["cells"]) == 4 and complex4["closure_connected"] is True
    assert q(complex4["minimum_closure_tetra_determinant_exact"]) > 0
    for cell in complex4["cells"]:
        d1 = q(cell["positive_tetra_determinant_exact"])
        d2 = q(cell["negative_tetra_determinant_exact"])
        assert d1 * d2 < 0
        bary = [q(z) for z in cell["equator_barycentric_exact"]]
        t = q(cell["segment_parameter_exact"])
        assert all(z > 0 for z in bary) and sum(bary, Q(0)) == 1
        assert 0 < t < 1
    assert complex4["cross_gap_true_edge_path"] == [135, 224, 223, 183]
    assert tuple(ccert["obstruction"]["edge"]) == (226, 227)
    assert (226, 227) in cedges
    A = q(ccert["obstruction"]["mutual_A_exact"])
    B = q(ccert["obstruction"]["mutual_B_exact"])
    D2 = q(ccert["obstruction"]["sum_squared_edge_exact"])
    assert A + B == D2 and D2 > 0
    assert {z["vertex"] for z in ccert["unstable_vertices"]} == {8, 227}
    assert {tuple(z["edge"]) for z in ccert["saddle_edges"]} == {(135, 224), (183, 223)}
    assert ccert["radial_order"]["target_unique_farthest"] is True
    assert graph["all_cross_component_vertex_pairs_negative"] is True
    assert graph["cross_component_vertex_pair_count"] == 1710
    assert len(graph["acute_components"]) == 2

    # Two independent incidence directions.  Their exact gradients are
    # diagonal because the two circuits contain different moving rows.
    f0a, slope_a, root_a, f1a = circuit_affine_root(
        common_rows, [194, 195, 224, 223], 223
    )
    f0b, slope_b, root_b, f1b = circuit_affine_root(
        common_rows, [122, 123, 225, 227], 227
    )
    walls = atlas["exact_incidence_walls"]
    assert root_a == q(walls[0]["root_exact"])
    assert root_b == q(walls[1]["root_exact"])
    assert 0 < root_a < 1 and 0 < root_b < 1
    wall_jacobian_det = slope_a * slope_b
    assert wall_jacobian_det != 0

    # The three dependent ordinary-moment directions are exact common
    # translations.  Translation preserves all incidences and all mechanics
    # relative to the translated centroid, while dM/dtau = V I_3.
    V = q(ccert["volume_exact"])
    assert V > 0
    moment_jacobian_det = V**3
    full_control_det = moment_jacobian_det * wall_jacobian_det
    assert full_control_det != 0

    # Explicit independent anti-birth cone at the endpoint.  Scaling rows 223
    # and 227 outward by s,t in [0,1e-14] stays inside the independently
    # certified coordinate box ±1e-12 and moves away from every first-atlas
    # incidence/mechanical wall, all of which lie strictly below scale 1.
    eps = Q(1, 100_000_000_000_000)
    box = q(interval["radius_exact"])
    assert box == Q(1, 1_000_000_000_000)
    max223 = max(abs(z) for z in common_rows[223])
    max227 = max(abs(z) for z in common_rows[227])
    assert eps * max223 < box and eps * max227 < box
    mechanical_hi = [q(w["hi_exact"]) for w in atlas["isolated_mechanical_walls"]]
    assert all(z < 1 for z in mechanical_hi)
    clearance_a = Q(1) - root_a
    clearance_b = min([Q(1) - root_b] + [Q(1) - z for z in mechanical_hi])
    assert clearance_a > 0 and clearance_b > 0

    report = {
        "version": 1,
        "verdict": "PASS: exact M42 parent reconstruction, exact lineage, fourth-cell incidence bridge, rank-5 controls, and independent antibirth cone verified",
        "parent": {
            "inputs": len(parent_rows),
            "f_vector": pcert["f_vector"],
            "class": pcert["class"],
            "active_rows": pcert["active_rows"],
            "inactive_rows": pcert["inactive_rows"],
            "residual_packet": {
                "obstruction_edge": [153, 154],
                "stable_face": [201, 220, 221],
                "direct_saddle": [130, 222],
                "return_saddle": [176, 182],
            },
        },
        "lineage": {
            "absorbed_rows": sorted(absorbed),
            "new_rows": sorted(map(int, provenance["new_rows"])),
            "linear_map_det_exact": str(detL),
            "minimum_projective_denominator": {
                "row": min_den_row,
                "exact": str(min_projective_denominator),
                "decimal": float(min_projective_denominator),
            },
            "exact_transform_rows_match": True,
            "authoritative_common_lattice_scale": common_scale,
            "maximum_exactification_delta": {
                "row": max_delta_key[0],
                "coordinate": "xyz"[max_delta_key[1]],
                "exact": str(max_exactification_delta),
                "decimal": float(max_exactification_delta),
                "bound_exact": "1/4000000000",
            },
            "protected_base_exactly_coplanar": True,
        },
        "child": {
            "inputs": len(common_rows),
            "f_vector": ccert["f_vector"],
            "class": ccert["class"],
            "active_rows": ccert["active_rows"],
            "inactive_rows": ccert["inactive_rows"],
            "absorbed_parent_packet_strictly_inactive": True,
            "four_linked_nonsimplicial_cells": True,
            "closure_faces": complex4["closure_faces"],
            "minimum_closure_determinant_exact": complex4["minimum_closure_tetra_determinant_exact"],
            "cross_gap_path": complex4["cross_gap_true_edge_path"],
            "cross_gap_angles_degrees": complex4["cross_gap_edge_angles_degrees"],
            "residual_obstruction_edge": [226, 227],
            "acute_components": graph["acute_components"],
            "cross_component_pairs_exactly_negative": graph["cross_component_vertex_pair_count"],
        },
        "control_rank": {
            "incidence_control_a": {
                "moving_row": 223,
                "circuit": [194, 195, 224, 223],
                "root_exact": str(root_a),
                "gradient_exact": str(slope_a),
                "endpoint_clearance_exact": str(clearance_a),
            },
            "incidence_control_b": {
                "moving_row": 227,
                "circuit": [122, 123, 225, 227],
                "root_exact": str(root_b),
                "gradient_exact": str(slope_b),
                "endpoint_clearance_to_all_b_walls_exact": str(clearance_b),
            },
            "two_by_two_wall_jacobian_det_exact": str(wall_jacobian_det),
            "moment_translation_jacobian_det_exact": str(moment_jacobian_det),
            "combined_five_by_five_det_exact": str(full_control_det),
            "rank": 5,
        },
        "independent_antibirth_box": {
            "directions": ["q223 -> (1+s)q223", "q227 -> (1+t)q227"],
            "s_interval_exact": ["0/1", str(eps)],
            "t_interval_exact": ["0/1", str(eps)],
            "coordinate_box_radius_exact": str(box),
            "max_row223_displacement_exact": str(eps * max223),
            "max_row227_displacement_exact": str(eps * max227),
            "moves_away_from_all_recorded_first_walls": True,
        },
        "manifest_files_checked": {
            "parent": parent_manifest_files,
            "child": child_manifest_files,
        },
    }
    out = ROOT / "lineage_control_certificate.json"
    out.write_text(json.dumps(report, indent=2) + "\n")
    print(report["verdict"])
    print("parent", report["parent"]["f_vector"], report["parent"]["class"])
    print("child", report["child"]["f_vector"], report["child"]["class"])
    print("projective min", min_den_row, str(min_projective_denominator), float(min_projective_denominator))
    print("exactification max", max_delta_key, str(max_exactification_delta), float(max_exactification_delta))
    print("wall roots", str(root_a), str(root_b))
    print("control rank 5; determinant nonzero")
    print("antibirth eps", str(eps))


if __name__ == "__main__":
    main()
