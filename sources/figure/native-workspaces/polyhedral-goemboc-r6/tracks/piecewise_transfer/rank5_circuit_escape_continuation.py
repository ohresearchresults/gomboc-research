#!/usr/bin/env python3
"""Exact continuation from C5 to destruction of the rank-five Gordan blocker.

The already certified physical axis is continued without changing its
normalization:

    q_255(t) = q_255(0) + t*(-1/2,-1,-1/4),  t decreases.

Starting at the delivered C4-far point t=-1/10, this program rebuilds every
support chamber and every wall through C17.  C17 is the circuit
{228,254,255,256}; it removes edge (228,255), removes the killed face
S[228,254,255] from the hull, and therefore removes both no-rebirth rows that
made the fixed-cell Gordan obstruction possible.

In the fresh C17-far cell the eight residual mechanics gradients have an
explicit exact strict-descent direction.  A rational material step is rebuilt
exactly, and an exact cubic-Bernstein support certificate plus exact Sturm
checks prove that the whole step remains in that cell with the base and U8
guards intact.
"""
from __future__ import annotations

import csv
import hashlib
import itertools
import json
import sys
from fractions import Fraction as Q
from pathlib import Path

import rank5_circuit_escape as esc
import rank5_exact_jacobian as rj
import rank5_exact_reconstruction as ex


HERE = Path(__file__).resolve().parent
OUTPUT = HERE / "rank5_circuit_escape_continuation.json"
CELL_DIR = HERE / "rank5_escape_continuation_cells"
REPORT = HERE / "RANK5_CIRCUIT_ESCAPE_CONTINUATION_REPORT.md"
VERIFIER = HERE / "verify_rank5_circuit_escape_continuation.py"
MANIFEST = HERE / "rank5_circuit_escape_continuation_artifacts.sha256"
sys.set_int_max_str_digits(0)


# Ordered exact support circuits after C4.  Every determinant is affine in t
# because row 255 is the sole moving row.
CONT_CIRCUITS = [
    ("C5", (69, 252, 253, 255)),
    ("C6", (54, 255, 258, 259)),
    ("C7", (54, 255, 259, 260)),
    ("C8", (54, 72, 255, 260)),
    ("C9", (69, 251, 252, 255)),
    ("C10", (72, 255, 260, 261)),
    ("C11", (72, 73, 255, 261)),
    ("C12", (14, 73, 255, 261)),
    ("C13", (13, 14, 255, 261)),
    ("C14", (13, 255, 261, 262)),
    ("C15", (69, 250, 251, 255)),
    ("C16", (12, 13, 255, 262)),
    ("C17", (228, 254, 255, 256)),
]


# One exact rational interior point in every chamber, from C4--C5 through the
# fresh C17-far chamber.  Consecutive entries bracket exactly one event because
# topology_chamber() independently recovers the adjacent exact endpoints.
CELL_POINTS = [
    ("c4_far_anchor", Q(-1, 10)),
    ("c5_far", Q(-7, 50)),
    ("c6_far", Q(-1, 5)),
    ("c7_far", Q(-27, 100)),
    ("c8_far", Q(-7, 25)),
    ("c9_far", Q(-3, 10)),
    ("c10_far", Q(-19, 50)),
    ("c11_far", Q(-2, 5)),
    ("c12_far", Q(-43, 100)),
    ("c13_far", Q(-9, 20)),
    ("c14_far", Q(-1, 2)),
    ("c15_far", Q(-51, 100)),
    ("c16_far", Q(-53, 100)),
    ("c17_far", Q(-11, 20)),
]


# Six normalized physical controls are ordered as
# [r228,r229,r254,r255,t231,t246].  These deliberately small-denominator
# coefficients strictly decrease all eight residual mechanics rows after C17.
DESCENT_DIRECTION = [
    Q(-107, 1000),
    Q(83, 2000),
    Q(-1),
    Q(1),
    Q(153, 1000),
    Q(-267, 1000),
]
DESCENT_STEP = Q(1, 125)


def qs(z: Q) -> str:
    return esc.qs(Q(z))


def qv(text: str) -> Q:
    return esc.qv(text)


def sha256(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for block in iter(lambda: f.read(1 << 20), b""):
            h.update(block)
    return h.hexdigest()


def face_signature(faces):
    return {tuple(sorted(face["cycle"])) for face in faces}


def audit_rows(name: str, rows, parameter: Q | None = None):
    """Fresh exact hull, mass, mechanics, protected guards, and exact CSV."""
    faces = ex.exactify_faces(rows, ex.numeric_faces(rows))
    volume, centroid = ex.exact_mass(rows, faces)
    ef, active, fl, vl, el, stable, unstable, saddles = ex.exact_mechanics(
        rows, faces, centroid
    )
    fvec = [len(active), len(ef), len(faces)]
    klass = [len(stable), len(unstable), len(saddles)]
    base = any(set(faces[i]["cycle"]) == set(range(17)) for i in stable)
    missing = sorted(esc.forced_rails() - set(ef))
    assert len(active) == 61 and base and 8 in unstable and not missing

    CELL_DIR.mkdir(exist_ok=True)
    path = CELL_DIR / f"{name}.csv"
    with path.open("w", newline="") as f:
        w = csv.writer(f)
        w.writerow(["source_id", "x_exact", "y_exact", "z_exact", "x", "y", "z"])
        for row, point in sorted(rows.items()):
            w.writerow(
                [row, *(qs(z) for z in point), *(format(float(z), ".17g") for z in point)]
            )

    return {
        "name": name,
        "parameter_exact": None if parameter is None else qs(parameter),
        "parameter_decimal": None if parameter is None else float(parameter),
        "f_vector": fvec,
        "class": klass,
        "all_61_active": True,
        "base_stable": True,
        "U8_unstable": True,
        "forced_rails_present": 37,
        "all_37_forced_rails_present": True,
        "stable_faces": [faces[i]["cycle"] for i in stable],
        "unstable_vertices": unstable,
        "saddle_edges": [list(e) for e in saddles],
        "volume_exact": qs(volume),
        "centroid_exact": [qs(z) for z in centroid],
        "csv": str(path.relative_to(HERE)),
        "csv_sha256": sha256(path),
        "faces": faces,
        "edges": set(ef),
        "face_ledger": fl,
        "vertex_ledger": vl,
        "edge_ledger": el,
    }


def strip_cell(cell):
    return {
        k: v
        for k, v in cell.items()
        if k not in {"faces", "edges", "face_ledger", "vertex_ledger", "edge_ledger"}
    }


def residual_feature_jets(rows, include_killed_guards: bool):
    """Exact values and six-column gradients in an arbitrary rebuilt cell."""
    faces = ex.exactify_faces(rows, ex.numeric_faces(rows))
    directions = esc.normalized_control_directions(rows)
    rj.M = esc.M
    q = {
        row: rj.qj(point, *(directions[row] if row in directions else (None, None)))
        for row, point in rows.items()
    }
    centroid, _ = rj.exact_centroid(q, faces)
    inc = esc.incidence(faces)

    def fc(vertices, edge):
        values = dict(rj.face_components(esc.face_by_vertices(faces, vertices), q, centroid))
        return values[edge] if edge in values else values[edge[::-1]]

    def ec(edge, component):
        e = tuple(sorted(edge))
        return rj.edge_components(e, inc[e], faces, q, centroid)[component]

    features = [
        ("death_S_228_264_246_via_246_228", fc([228, 264, 246], (246, 228)), "death"),
        ("death_U228_via_251", rj.vertex_support(228, 251, q, centroid), "death"),
        ("death_U231_via_232", rj.vertex_support(231, 232, q, centroid), "death"),
        ("death_U246_via_245", rj.vertex_support(246, 245, q, centroid), "death"),
        ("death_H8_246_via_t", ec((8, 246), "t"), "death"),
        ("death_H228_254_via_beta2", ec((228, 254), "beta2"), "death"),
        ("death_H231_247_via_beta1", ec((231, 247), "beta1"), "death"),
        ("death_H236_237_via_beta1", ec((236, 237), "beta1"), "death"),
    ]
    assert all(z.v > 0 for _, z, _ in features)
    if include_killed_guards:
        features += [
            (
                "guard_killed_S_228_254_255_no_rebirth",
                fc([228, 254, 255], (255, 228)),
                "guard",
            ),
            (
                "guard_killed_H228_255_no_rebirth",
                ec((228, 255), "beta2"),
                "guard",
            ),
        ]
        assert all(z.v < 0 for _, z, _ in features[8:])
    return features, directions, faces


def feature_record(name, jet, kind, direction=None):
    out = {
        "name": name,
        "kind": kind,
        "value_exact": qs(jet.v),
        "value_decimal": float(jet.v),
        "gradient_exact": [qs(z) for z in jet.d],
        "gradient_decimal": [float(z) for z in jet.d],
    }
    if direction is not None:
        derivative = sum((jet.d[k] * direction[k] for k in range(esc.M)), Q(0))
        out["directed_derivative_exact"] = qs(derivative)
        out["directed_derivative_decimal"] = float(derivative)
    return out


def apply_descent(rows, directions, step=DESCENT_STEP):
    out = dict(rows)
    for row, (control, direction) in directions.items():
        out[row] = ex.add(out[row], ex.mul(direction, step * DESCENT_DIRECTION[control]))
    return out


# ---------- exact symbolic guards on the one-row t axis ----------


def symbolic_face_normal_general(face, q, reference_rows, reference_parameter):
    cycle = face["cycle"]
    a = q[cycle[0]]
    for j in range(1, len(cycle) - 1):
        for k in range(j + 1, len(cycle)):
            if ex.cross(
                ex.sub(reference_rows[cycle[j]], reference_rows[cycle[0]]),
                ex.sub(reference_rows[cycle[k]], reference_rows[cycle[0]]),
            ) != ex.ZERO:
                n = esc.vcross(esc.vsub(q[cycle[j]], a), esc.vsub(q[cycle[k]], a))
                nv = tuple(z.at(reference_parameter) for z in n)
                assert ex.dot(nv, face["n"]) != 0
                if ex.dot(nv, face["n"]) < 0:
                    n = tuple(-z for z in n)
                return n
    raise AssertionError("collinear symbolic face")


def symbolic_face_components_general(face, q, centroid, reference_rows, reference_parameter):
    cycle = face["cycle"]
    n = symbolic_face_normal_general(face, q, reference_rows, reference_parameter)
    h = esc.vdot(n, esc.vsub(q[cycle[0]], centroid))
    foot = esc.vmul(n, h / esc.vdot(n, n))
    x = {i: esc.vsub(q[i], centroid) for i in cycle}
    ref = tuple(
        sum((x[i][k] for i in cycle), esc.RP.c(0)) / len(cycle) for k in range(3)
    )
    out = {}
    for a, b in zip(cycle, cycle[1:] + cycle[:1]):
        edge = esc.vsub(x[b], x[a])
        z = esc.vdot(esc.vcross(edge, esc.vsub(foot, x[a])), n)
        reference_sign = esc.vdot(
            esc.vcross(edge, esc.vsub(ref, x[a])), n
        ).at(reference_parameter)
        assert reference_sign != 0
        if reference_sign < 0:
            z = -z
        out[(a, b)] = z
    return out


def rational_function_no_root(z, left, right, sample):
    assert left < sample < right
    assert esc.peval(z.n, left) != 0 and esc.peval(z.n, right) != 0
    assert esc.peval(z.d, left) != 0 and esc.peval(z.d, right) != 0
    numerator_roots, _ = esc.sturm_root_count(list(z.n), left, right)
    denominator_roots, _ = esc.sturm_root_count(list(z.d), left, right)
    assert numerator_roots == 0 and denominator_roots == 0 and z.at(sample) > 0
    return max(len(z.n) - 1, len(z.d) - 1)


def axis_guard_audit(faces, sample, lower, upper):
    """Prove base stability and U8 instability on a complete support chamber."""
    q = esc.symbolic_rows()
    centroid, volume = esc.symbolic_centroid(q, faces)
    assert rational_function_no_root(volume, lower, upper, sample) >= 0
    reference_rows = esc.moved_rows(sample)
    base = esc.face_by_vertices(faces, list(range(17)))
    base_components = symbolic_face_components_general(
        base, q, centroid, reference_rows, sample
    )
    inc = esc.incidence(faces)
    u8_neighbors = sorted({b if a == 8 else a for a, b in inc if 8 in (a, b)})
    degrees = []
    for z in base_components.values():
        degrees.append(rational_function_no_root(z, lower, upper, sample))
    for neighbor in u8_neighbors:
        z = esc.symbolic_vertex_support(8, neighbor, q, centroid)
        degrees.append(rational_function_no_root(z, lower, upper, sample))
    return {
        "interval_exact": [qs(lower), qs(upper)],
        "base_component_count": len(base_components),
        "U8_support_count": len(u8_neighbors),
        "component_count": len(degrees),
        "every_numerator_and_denominator_has_zero_roots": True,
        "all_components_positive_at_rational_sample": True,
        "maximum_checked_polynomial_degree": max(degrees),
    }


# ---------- exact cubic Bernstein support certificate for material step ----------


def p_add(a, b):
    return tuple(
        (a[i] if i < len(a) else Q(0)) + (b[i] if i < len(b) else Q(0))
        for i in range(max(len(a), len(b)))
    )


def p_sub(a, b):
    return p_add(a, tuple(-z for z in b))


def p_mul(a, b):
    out = [Q(0)] * (len(a) + len(b) - 1)
    for i, z in enumerate(a):
        for j, w in enumerate(b):
            out[i + j] += z * w
    return tuple(out)


def pv_sub(a, b):
    return tuple(p_sub(a[k], b[k]) for k in range(3))


def pv_cross(a, b):
    return (
        p_sub(p_mul(a[1], b[2]), p_mul(a[2], b[1])),
        p_sub(p_mul(a[2], b[0]), p_mul(a[0], b[2])),
        p_sub(p_mul(a[0], b[1]), p_mul(a[1], b[0])),
    )


def pv_dot(a, b):
    out = (Q(0),)
    for k in range(3):
        out = p_add(out, p_mul(a[k], b[k]))
    return out + (Q(0),) * (4 - len(out))


def cubic_bernstein_coefficients(power):
    p0, p1, p2, p3 = power
    return (
        p0,
        p0 + p1 / 3,
        p0 + 2 * p1 / 3 + p2 / 3,
        p0 + p1 + p2 + p3,
    )


def affine_support_segment_audit(rows0, rows1, faces):
    """Exact proof that every old maximal support plane persists for u in [0,1]."""
    ids = sorted(rows0)
    q = {
        i: tuple((rows0[i][k], rows1[i][k] - rows0[i][k]) for k in range(3))
        for i in ids
    }
    strict = 0
    planar = 0
    bernstein = 0
    for face in faces:
        cycle = face["cycle"]
        a = cycle[0]
        tri = None
        for j in range(1, len(cycle) - 1):
            for k in range(j + 1, len(cycle)):
                if ex.cross(
                    ex.sub(rows0[cycle[j]], rows0[a]),
                    ex.sub(rows0[cycle[k]], rows0[a]),
                ) != ex.ZERO:
                    tri = (a, cycle[j], cycle[k])
                    break
            if tri is not None:
                break
        assert tri is not None
        aa, bb, cc = tri

        def determinant_polynomial(i):
            return pv_dot(
                pv_sub(q[bb], q[aa]),
                pv_cross(pv_sub(q[cc], q[aa]), pv_sub(q[i], q[aa])),
            )

        outside0 = [determinant_polynomial(i)[0] for i in ids if i not in cycle]
        orient = Q(1) if all(z < 0 for z in outside0) else Q(-1)
        assert all(orient * z < 0 for z in outside0)
        for i in cycle:
            polynomial = determinant_polynomial(i)
            assert all(z == 0 for z in polynomial)
            planar += 1
        for i in ids:
            if i in cycle:
                continue
            polynomial = tuple(orient * z for z in determinant_polynomial(i))
            coefficients = cubic_bernstein_coefficients(polynomial)
            assert all(z < 0 for z in coefficients)
            strict += 1
            bernstein += len(coefficients)
    return {
        "parameter_interval_exact": ["0/1", "1/1"],
        "persistent_face_count": len(faces),
        "identically_coplanar_face_vertex_checks": planar,
        "strict_outside_support_polynomials": strict,
        "strict_cubic_bernstein_coefficients": bernstein,
        "all_bernstein_coefficients_strictly_inside": True,
        "conclusion": "the complete material segment stays in the C17-far support cell",
    }


def main():
    CELL_DIR.mkdir(exist_ok=True)
    roots = {name: esc.circuit_root(ids) for name, ids in CONT_CIRCUITS}
    c4_root = esc.circuit_root((54, 255, 257, 258))
    ordered = [c4_root] + [roots[name] for name, _ in CONT_CIRCUITS]
    assert all(ordered[i + 1] < ordered[i] for i in range(len(ordered) - 1))

    cells = []
    for name, t in CELL_POINTS:
        cells.append(audit_rows(name, esc.moved_rows(t), t))
    assert all(cell["f_vector"] == [61, 150, 91] for cell in cells)
    cell_by_name = {cell["name"]: cell for cell in cells}

    events = []
    chambers = []
    total_axis_guard_components = 0
    for i, (name, ids) in enumerate(CONT_CIRCUITS):
        root = roots[name]
        pre_name, pre_t = CELL_POINTS[i]
        far_name, far_t = CELL_POINTS[i + 1]
        assert far_t < root < pre_t
        assert esc.det4(root, ids) == 0
        determinant_signs = [esc.det4(far_t, ids), esc.det4(pre_t, ids)]
        assert determinant_signs[0] * determinant_signs[1] < 0

        pre = cell_by_name[pre_name]
        far = cell_by_name[far_name]
        removed = sorted(pre["edges"] - far["edges"])
        added = sorted(far["edges"] - pre["edges"])
        assert len(removed) == 1 and len(added) == 1

        wall = audit_rows(f"{name.lower()}_wall", esc.moved_rows(root), root)
        assert wall["f_vector"] == [61, 149, 90]

        chamber = esc.topology_chamber(pre_t)
        lower = qv(chamber["lower_exact"])
        upper = qv(chamber["upper_exact"])
        expected_upper = c4_root if i == 0 else roots[CONT_CIRCUITS[i - 1][0]]
        assert lower == root and upper == expected_upper
        assert sorted(ids) in chamber["lower_circuit_witnesses"]
        guard = axis_guard_audit(pre["faces"], pre_t, lower, upper)
        total_axis_guard_components += guard["component_count"]
        chambers.append(
            {
                "cell": pre_name,
                "sample_exact": qs(pre_t),
                "lower_exact": qs(lower),
                "upper_exact": qs(upper),
                "lower_circuit_witnesses": chamber["lower_circuit_witnesses"],
                "upper_circuit_witnesses": chamber["upper_circuit_witnesses"],
                "strict_support_inequalities_checked": chamber[
                    "strict_support_inequalities_checked"
                ],
                "continuous_base_U8_guard": guard,
            }
        )
        events.append(
            {
                "name": name,
                "vertices": list(ids),
                "parameter_exact": qs(root),
                "parameter_decimal": float(root),
                "affine_determinant_unique_root": True,
                "determinant_zero_exact": True,
                "isolating_bracket_exact": [qs(far_t), qs(pre_t)],
                "bracket_determinant_signs": [
                    1 if determinant_signs[0] > 0 else -1,
                    1 if determinant_signs[1] > 0 else -1,
                ],
                "pre_cell": pre_name,
                "wall_cell": strip_cell(wall),
                "far_cell": far_name,
                "removed_edge": list(removed[0]),
                "added_edge": list(added[0]),
            }
        )

    # The exact named blocker is present immediately after C4 and survives C5.
    start_rows = esc.moved_rows(CELL_POINTS[0][1])
    start_features, _, _ = residual_feature_jets(start_rows, True)
    start_gordan = esc.exact_gordan(start_features)
    required_names = [
        "death_S_228_264_246_via_246_228",
        "death_U228_via_251",
        "death_U231_via_232",
        "death_U246_via_245",
        "death_H8_246_via_t",
        "death_H228_254_via_beta2",
        "guard_killed_S_228_254_255_no_rebirth",
    ]
    assert start_gordan["support_indices"] == [0, 1, 2, 3, 4, 5, 8]
    assert [start_features[i][0] for i in start_gordan["support_indices"]] == required_names

    # Immediately before C17 a (possibly relabelled) guard-dependent Gordan
    # circuit still blocks strict residual descent with both no-rebirth rows.
    prebreak_rows = esc.moved_rows(CELL_POINTS[-2][1])
    prebreak_features, _, prebreak_faces = residual_feature_jets(prebreak_rows, True)
    prebreak_gordan = esc.exact_gordan(prebreak_features)
    assert any(i >= 8 for i in prebreak_gordan["support_indices"])

    # C17 removes both combinatorial carriers of those no-rebirth inequalities.
    post_rows = esc.moved_rows(CELL_POINTS[-1][1])
    post_features, directions, post_faces = residual_feature_jets(post_rows, False)
    post_edges = esc.edge_set(post_faces)
    assert not any(set(face["cycle"]) == {228, 254, 255} for face in post_faces)
    assert (228, 255) not in post_edges and (254, 256) in post_edges
    assert rj.matrix_rank([jet.d for _, jet, _ in post_features]) == 6
    derivatives = [
        sum((jet.d[k] * DESCENT_DIRECTION[k] for k in range(esc.M)), Q(0))
        for _, jet, _ in post_features
    ]
    assert all(z < 0 for z in derivatives)

    endpoint_rows = apply_descent(post_rows, directions)
    endpoint = audit_rows("c17_residual_descent_endpoint", endpoint_rows, None)
    assert face_signature(endpoint["faces"]) == face_signature(post_faces)
    endpoint_features, _, endpoint_faces = residual_feature_jets(endpoint_rows, False)
    assert face_signature(endpoint_faces) == face_signature(post_faces)
    assert all(endpoint_features[i][1].v < post_features[i][1].v for i in range(8))
    support_segment = affine_support_segment_audit(post_rows, endpoint_rows, post_faces)

    # Exact mechanics guard proof for the full rational material segment.
    q = {
        i: tuple(
            esc.RP.make([post_rows[i][k], endpoint_rows[i][k] - post_rows[i][k]], [Q(1)])
            for k in range(3)
        )
        for i in post_rows
    }
    centroid, volume = esc.symbolic_centroid(q, post_faces)
    assert rational_function_no_root(volume, Q(0), Q(1), Q(1, 2)) >= 0
    base = esc.face_by_vertices(post_faces, list(range(17)))
    base_components = symbolic_face_components_general(base, q, centroid, post_rows, Q(0))
    inc = esc.incidence(post_faces)
    u8_neighbors = sorted({b if a == 8 else a for a, b in inc if 8 in (a, b)})
    material_guard_degrees = []
    for z in base_components.values():
        material_guard_degrees.append(rational_function_no_root(z, Q(0), Q(1), Q(1, 2)))
    for neighbor in u8_neighbors:
        z = esc.symbolic_vertex_support(8, neighbor, q, centroid)
        material_guard_degrees.append(
            rational_function_no_root(z, Q(0), Q(1), Q(1, 2))
        )
    material_guard = {
        "base_component_count": len(base_components),
        "U8_support_count": len(u8_neighbors),
        "component_count": len(material_guard_degrees),
        "every_numerator_and_denominator_has_zero_roots": True,
        "all_components_positive_on_complete_segment": True,
        "maximum_checked_polynomial_degree": max(material_guard_degrees),
    }

    post_records = [
        feature_record(name, jet, kind, DESCENT_DIRECTION)
        for name, jet, kind in post_features
    ]
    endpoint_records = [
        feature_record(name, jet, kind) for name, jet, kind in endpoint_features
    ]
    exact_ratios = [
        endpoint_features[i][1].v / post_features[i][1].v for i in range(8)
    ]

    all_csv_cells = cells + [event["wall_cell"] for event in events] + [strip_cell(endpoint)]
    artifact_hashes = {cell["csv"]: cell["csv_sha256"] for cell in all_csv_cells}
    out = {
        "version": 1,
        "type": "exact C5-through-C17 physical continuation and Gordan-support break",
        "path": {
            "formula": "q255(t)=q255(0)+t*(-1/2,-1,-1/4), t decreases",
            "start_parameter_exact": qs(CELL_POINTS[0][1]),
            "post_break_parameter_exact": qs(CELL_POINTS[-1][1]),
            "largest_axis_coordinate_displacement_exact": qs(abs(CELL_POINTS[-1][1])),
        },
        "ordered_events": events,
        "exact_support_chambers": chambers,
        "rational_material_cells": [strip_cell(cell) for cell in cells],
        "axis_guard_summary": {
            "chamber_count": len(chambers),
            "strict_support_inequalities_checked_total": sum(
                z["strict_support_inequalities_checked"] for z in chambers
            ),
            "continuous_base_U8_components_checked_total": total_axis_guard_components,
            "all61_base_U8_rails_through_every_cell_and_wall": True,
        },
        "initial_fixed_cell_gordan_blocker": {
            "parameter_exact": qs(CELL_POINTS[0][1]),
            "support_indices": start_gordan["support_indices"],
            "support_names": required_names,
            "exact_stationarity_zero": start_gordan["exact_stationarity_zero"],
            "support": start_gordan["support"],
        },
        "pre_C17_blocker": {
            "parameter_exact": qs(CELL_POINTS[-2][1]),
            "support_indices": prebreak_gordan["support_indices"],
            "support_names": [
                prebreak_features[i][0] for i in prebreak_gordan["support_indices"]
            ],
            "still_requires_a_no_rebirth_row": True,
            "killed_face_present": any(
                set(face["cycle"]) == {228, 254, 255} for face in prebreak_faces
            ),
            "killed_edge_present": (228, 255) in esc.edge_set(prebreak_faces),
        },
        "C17_break": {
            "circuit": [228, 254, 255, 256],
            "removed_edge": [228, 255],
            "added_edge": [254, 256],
            "killed_face_S228_254_255_absent_after": True,
            "killed_edge_H228_255_absent_after": True,
            "interpretation": (
                "both no-rebirth rows used by the fixed-cell Gordan family cease to be "
                "mechanical constraints in the fresh support cell"
            ),
        },
        "post_C17_residual_cone": {
            "parameter_exact": qs(CELL_POINTS[-1][1]),
            "f_vector": cell_by_name["c17_far"]["f_vector"],
            "class": cell_by_name["c17_far"]["class"],
            "residual_gradient_rank_exact": 6,
            "control_names": esc.CONTROL_NAMES,
            "strict_descent_direction_exact": [qs(z) for z in DESCENT_DIRECTION],
            "all_eight_directed_derivatives_strictly_negative_exact": True,
            "features": post_records,
        },
        "material_residual_descent": {
            "step_exact": qs(DESCENT_STEP),
            "maximum_additional_coordinate_displacement_exact": qs(DESCENT_STEP),
            "endpoint": strip_cell(endpoint),
            "endpoint_features": endpoint_records,
            "endpoint_over_start_ratios_exact": [qs(z) for z in exact_ratios],
            "endpoint_over_start_ratios_decimal": [float(z) for z in exact_ratios],
            "all_eight_exact_values_strictly_decrease": True,
            "complete_support_segment_certificate": support_segment,
            "complete_base_U8_segment_certificate": material_guard,
        },
        "artifact_hashes": artifact_hashes,
        "verdict": "EXACT_C5_TO_C17_GORDAN_SUPPORT_BREAK_WITH_STRICT_RESIDUAL_DESCENT",
        "conclusion": (
            "The same one-row physical path crosses C5 and twelve further exact support "
            "walls while preserving all 61 active rows, the stable base, U8, and all 37 "
            "rails.  C17 flips (228,255) to (254,256), deleting both carriers of the "
            "no-rebirth rows.  The fresh cell has an exact rank-six eight-wall residual "
            "cone and the displayed rational control direction is strictly descending "
            "in all eight rows; a fully guarded rational material step realizes it."
        ),
    }
    OUTPUT.write_text(json.dumps(out, indent=2) + "\n")
    package = [Path(__file__), OUTPUT, REPORT, VERIFIER] + sorted(CELL_DIR.glob("*.csv"))
    assert all(path.is_file() for path in package)
    MANIFEST.write_text(
        "".join(f"{sha256(path)}  {path.relative_to(HERE)}\n" for path in package)
    )
    print(out["verdict"])
    print("events", len(events), "C5", float(roots["C5"]), "C17", float(roots["C17"]))
    print("axis_cells", len(cells), "axis_guard_components", total_axis_guard_components)
    print("start_Gordan", start_gordan["support_indices"])
    print("pre_C17_Gordan", prebreak_gordan["support_indices"])
    print("post_rank", out["post_C17_residual_cone"]["residual_gradient_rank_exact"])
    print("material_ratios", [float(z) for z in exact_ratios])
    print("output", OUTPUT)
    print("manifest", MANIFEST)


if __name__ == "__main__":
    main()
