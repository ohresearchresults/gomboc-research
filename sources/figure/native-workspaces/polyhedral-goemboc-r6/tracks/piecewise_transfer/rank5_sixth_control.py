#!/usr/bin/env python3
"""Exact sixth-control audit for the reconstructed supporting-shell seed.

The original five-control chart is augmented by the genuine shell-tangent
motion

    t246: row 246 along (-7, 8, -90).

The direction preserves the exact supporting plane 100*x+20*y-6*z=3700.
Both +/- one-tenth physical probes are rebuilt as actual hulls and checked
exactly for the original f-vector, mechanics class, protected base/U8, and all
37 forced rail edges.

The six selected death gradients have exact rank six, so their affine first
jet has a unique formal common root.  That root is fresh-hull audited and is
macroscopic: it destroys the base, U8 and 17 rails.  Finally, a rational
Farkas certificate proves that even the necessary six-death subsystem is
infeasible in the physical trust box |D*c|_infinity <= 1/10.  A numerical LP
is used only to locate a sparse nonnegative support; all supported rows,
multipliers, stationarity repair and the final RHS are checked as Fractions.
"""
from __future__ import annotations

import csv
import json
import math
import sys
from fractions import Fraction as Q
from pathlib import Path

import numpy as np
from scipy.optimize import linprog

import rank5_exact_jacobian as rj
import rank5_exact_reconstruction as ex
import rank5_search as search


HERE = Path(__file__).resolve().parent
OUTPUT = HERE / "rank5_sixth_control.json"
M = 6
TRUST = Q(1, 10)
CONTROL_NAMES = ["r228", "r229", "r254", "r255", "t231", "t246"]
SIXTH_DIRECTION = (Q(-7), Q(8), Q(-90))
PROBE_PARAMETER = Q(1, 900)  # max coordinate displacement is exactly 1/10
sys.set_int_max_str_digits(0)


def qs(z: Q) -> str:
    return ex.qs(Q(z))


def q17(z: float) -> Q:
    return Q(format(float(z), ".17g"))


def qlog10(z: Q) -> float:
    return math.log10(abs(z.numerator)) - math.log10(z.denominator)


def original_row228() -> tuple[Q, Q, Q]:
    path = ex.WORK / "fifth_cell_endpoint" / "input_rows_common_lattice.csv"
    for row in csv.DictReader(path.open()):
        if int(row["source_id"]) == 228:
            den = int(row["denominator"])
            return tuple(Q(int(row[k]), den) for k in ("x_int", "y_int", "z_int"))
    raise AssertionError("missing row 228")


def control_directions(rows):
    directions = {
        228: (0, ex.sub(rows[228], original_row228())),
        229: (1, (Q(41), Q(-16), Q(2))),
        254: (2, (Q(-18), Q(-36), Q(-9))),
        255: (3, (Q(-18), Q(-36), Q(-9))),
        231: (4, (Q(-24), Q(132), Q(40))),
        246: (5, SIXTH_DIRECTION),
    }
    assert ex.dot(ex.N, directions[231][1]) == 0
    assert ex.dot(ex.N, directions[246][1]) == 0
    assert len({row for row in directions}) == M
    return directions


def build_jets(rows, directions):
    # rank5_exact_jacobian's dual-number implementation is dimensioned by its
    # module global.  Set it before constructing any jet; all resulting
    # derivative tuples then have literal length six.
    rj.M = M
    return {
        row: rj.qj(point, *(directions[row] if row in directions else (None, None)))
        for row, point in rows.items()
    }


def edge_incidence(faces):
    from collections import defaultdict

    out = defaultdict(list)
    for fi, face in enumerate(faces):
        cyc = face["cycle"]
        for a, b in zip(cyc, cyc[1:] + cyc[:1]):
            out[tuple(sorted((a, b)))].append(fi)
    assert all(len(inc) == 2 for inc in out.values())
    return dict(out)


def face_with_vertices(faces, vertices):
    target = set(vertices)
    matches = [face for face in faces if set(face["cycle"]) == target]
    assert len(matches) == 1, (vertices, len(matches))
    return matches[0]


def six_death_jets(q, faces, incidence):
    centroid, _ = rj.exact_centroid(q, faces)
    f1 = dict(rj.face_components(face_with_vertices(faces, [228, 254, 255]), q, centroid))
    f2 = dict(rj.face_components(face_with_vertices(faces, [228, 264, 246]), q, centroid))
    jets = [
        f1[(255, 228)],
        f2[(246, 228)],
        rj.vertex_support(228, 254, q, centroid),
        rj.vertex_support(231, 229, q, centroid),
        rj.vertex_support(246, 231, q, centroid),
        rj.edge_components((8, 246), incidence[(8, 246)], faces, q, centroid)["t"],
    ]
    names = [
        "kill_S_228_254_255_via_255_228",
        "kill_S_228_264_246_via_246_228",
        "kill_U228_via_254",
        "kill_U231_via_229",
        "kill_U246_via_231",
        "kill_H8_246_via_t",
    ]
    assert all(jet.v > 0 for jet in jets)
    return names, jets


def solve_exact_square(a, b):
    n = len(a)
    aug = [[Q(z) for z in row] + [Q(rhs)] for row, rhs in zip(a, b)]
    assert len(aug) == n and all(len(row) == n + 1 for row in aug)
    for col in range(n):
        pivot = next((row for row in range(col, n) if aug[row][col] != 0), None)
        if pivot is None:
            raise ArithmeticError(("singular", col))
        aug[col], aug[pivot] = aug[pivot], aug[col]
        z = aug[col][col]
        aug[col] = [value / z for value in aug[col]]
        for row in range(n):
            if row == col or aug[row][col] == 0:
                continue
            z = aug[row][col]
            aug[row] = [aug[row][k] - z * aug[col][k] for k in range(n + 1)]
    answer = [aug[row][-1] for row in range(n)]
    assert all(
        sum(a[row][col] * answer[col] for col in range(n)) == b[row]
        for row in range(n)
    )
    return answer


def forced_rails():
    short = [228] + list(range(229, 247)) + [8]
    long = [228] + list(range(247, 265)) + [8]
    rails = {
        tuple(sorted(edge))
        for path in (short, long)
        for edge in zip(path, path[1:])
    }
    rails.remove((228, 229))
    assert len(rails) == 37
    return rails


def exact_probe(rows, sign):
    probe = dict(rows)
    probe[246] = ex.add(probe[246], ex.mul(SIXTH_DIRECTION, sign * PROBE_PARAMETER))
    assert ex.dot(ex.N, probe[246]) == ex.H
    proposal = ex.numeric_faces(probe)
    faces = ex.exactify_faces(probe, proposal)
    volume, centroid = ex.exact_mass(probe, faces)
    incidence, active, _, _, _, stable, unstable, saddles = ex.exact_mechanics(
        probe, faces, centroid
    )
    base_stable = any(set(faces[fi]["cycle"]) == set(range(17)) for fi in stable)
    rails = forced_rails()
    missing = rails - set(incidence)
    assert [len(active), len(incidence), len(faces)] == [61, 150, 91]
    assert [len(stable), len(unstable), len(saddles)] == [3, 4, 5]
    assert base_stable and 8 in unstable and not missing
    return {
        "sign": sign,
        "parameter_exact": qs(sign * PROBE_PARAMETER),
        "row246_displacement_exact": [qs(sign * PROBE_PARAMETER * z) for z in SIXTH_DIRECTION],
        "max_abs_coordinate_displacement_exact": qs(TRUST),
        "shell_plane_value_exact": qs(ex.dot(ex.N, probe[246])),
        "f_vector": [len(active), len(incidence), len(faces)],
        "class": [len(stable), len(unstable), len(saddles)],
        "base_stable": base_stable,
        "U8_unstable": 8 in unstable,
        "forced_rails_present": len(rails - missing),
        "all_37_forced_rails_present": not missing,
        "stable_faces": [faces[fi]["cycle"] for fi in stable],
        "unstable_vertices": unstable,
        "saddle_edges": [list(edge) for edge in saddles],
        "volume_exact": qs(volume),
    }


def exactify_faces_allow_inactive_coplanars(rows, proposal):
    """Exactify a fresh hull whose supporting planes may contain inactive rows.

    At the macroscopic affine root most of the old 16-gon rows become interior
    to a smaller polygon on the same exact shell plane.  The standard seed
    exactifier deliberately requires every coplanar row to be a cycle vertex;
    this fresh-hull variant instead requires the proposed cycle to be exactly
    coplanar and verifies the support sign for all 119 rows.
    """
    faces = []
    for proposed in proposal.faces:
        cycle = list(proposed["cycle"])
        a = rows[cycle[0]]
        normal = ex.ZERO
        for j in range(1, len(cycle) - 1):
            for k in range(j + 1, len(cycle)):
                normal = ex.cross(ex.sub(rows[cycle[j]], a), ex.sub(rows[cycle[k]], a))
                if normal != ex.ZERO:
                    break
            if normal != ex.ZERO:
                break
        assert normal != ex.ZERO
        height = ex.dot(normal, a)
        values = {row: ex.dot(normal, point) - height for row, point in rows.items()}
        positive = any(value > 0 for value in values.values())
        negative = any(value < 0 for value in values.values())
        assert not (positive and negative)
        if positive:
            normal = tuple(-value for value in normal)
            height = -height
            values = {row: -value for row, value in values.items()}
        assert all(values[row] == 0 for row in cycle)
        assert all(value <= 0 for value in values.values())
        area = ex.ZERO
        for u, v in zip(cycle, cycle[1:] + cycle[:1]):
            area = ex.add(area, ex.cross(rows[u], rows[v]))
        if ex.dot(area, normal) < 0:
            cycle = [cycle[0]] + list(reversed(cycle[1:]))
        faces.append({"cycle": cycle, "n": normal, "h": height})
    return faces


def physical_rows(directions):
    """Return the 18 exact rows mapping controls to moved coordinates."""
    rows = []
    labels = []
    axes = "xyz"
    for row, (control, direction) in sorted(directions.items(), key=lambda item: item[1][0]):
        for axis, coefficient in enumerate(direction):
            vector = [Q(0)] * M
            vector[control] = coefficient
            rows.append(tuple(vector))
            labels.append(f"row{row}:{axes[axis]}")
    assert len(rows) == 18
    return rows, labels


def add_scaled(acc, row, scale):
    for k, value in enumerate(row):
        acc[k] += scale * value


def exact_physical_farkas(death_names, death_jets, drows, dlabels):
    death_a = np.asarray([[float(z) for z in jet.d] for jet in death_jets])
    death_b = -np.asarray([float(jet.v) for jet in death_jets])
    dfloat = np.asarray([[float(z) for z in row] for row in drows])
    a = np.vstack((death_a, dfloat, -dfloat))
    b = np.r_[death_b, np.full(2 * len(drows), float(TRUST))]
    scale = np.max(np.abs(a), axis=1)
    assert np.all(scale > 0)
    scaled_a = a / scale[:, None]
    scaled_b = b / scale
    solve = linprog(
        scaled_b,
        A_eq=np.vstack((scaled_a.T, np.ones(len(a)))),
        b_eq=np.r_[np.zeros(M), 1.0],
        bounds=[(0.0, None)] * len(a),
        method="highs-ds",
        options={"primal_feasibility_tolerance": 1e-10, "dual_feasibility_tolerance": 1e-10},
    )
    if not solve.success:
        raise RuntimeError(solve.message)
    y_scaled = np.maximum(0.0, solve.x)
    y_float = y_scaled / scale
    stationarity_float = a.T @ y_float
    rhs_float = float(b @ y_float)

    stationarity = [Q(0)] * M
    rhs = Q(0)
    support = []
    for index, value in enumerate(y_float):
        if value <= 0:
            continue
        weight = q17(value)
        if index < len(death_jets):
            row = death_jets[index].d
            row_b = -death_jets[index].v
            label = {"group": "death", "name": death_names[index]}
        elif index < len(death_jets) + len(drows):
            local = index - len(death_jets)
            row = drows[local]
            row_b = TRUST
            label = {"group": "trust_plus", "physical_coordinate": dlabels[local]}
        else:
            local = index - len(death_jets) - len(drows)
            row = tuple(-z for z in drows[local])
            row_b = TRUST
            label = {"group": "trust_minus", "physical_coordinate": dlabels[local]}
        add_scaled(stationarity, row, weight)
        rhs += row_b * weight
        support.append({**label, "weight_exact": qs(weight), "weight_decimal": float(weight)})

    # Each control moves a distinct row.  Pick its largest physical coordinate
    # coefficient and add the appropriate +/- trust inequality to cancel the
    # decimalized locator residual exactly.
    repairs = []
    for control, residual in enumerate(list(stationarity)):
        candidates = [
            (abs(row[control]), local, row[control])
            for local, row in enumerate(drows) if row[control] != 0
        ]
        _, local, coefficient = max(candidates)
        signed_weight = -residual / coefficient
        side = "trust_plus" if signed_weight >= 0 else "trust_minus"
        weight = abs(signed_weight)
        repair_row = drows[local] if signed_weight >= 0 else tuple(-z for z in drows[local])
        add_scaled(stationarity, repair_row, weight)
        rhs += TRUST * weight
        repairs.append({
            "control": CONTROL_NAMES[control],
            "group": side,
            "physical_coordinate": dlabels[local],
            "weight_exact": qs(weight),
            "weight_decimal": float(weight),
        })
    assert stationarity == [Q(0)] * M
    assert rhs < 0
    return {
        "system_form": "A*c <= b",
        "necessary_death_inequalities": [f"{name}: value + gradient*c <= 0" for name in death_names],
        "physical_trust": "|D*c|_infinity <= 1/10 on the 18 moved row coordinates",
        "row_count": int(len(a)),
        "numerical_locator": {
            "method": "highs-ds on infinity-row-scaled Farkas ray LP",
            "scaled_objective": float(solve.fun),
            "original_rhs": rhs_float,
            "stationarity_inf_norm": float(np.max(np.abs(stationarity_float))),
        },
        "positive_locator_support": support,
        "exact_stationarity_repair_with_physical_trust_rows": repairs,
        "exact_stationarity_all_6_columns_zero": True,
        "all_exact_multipliers_nonnegative": True,
        "repaired_farkas_rhs_exact": qs(rhs),
        "repaired_farkas_rhs_decimal": float(rhs),
        "repaired_farkas_rhs_log10_abs": qlog10(rhs),
        "strictly_negative_farkas_rhs": True,
        "conclusion": (
            "The six selected death inequalities are already exactly infeasible in the physical "
            "trust box. Therefore no guarded shared event for this branch exists there."
        ),
    }


def fresh_root_audit(rows, directions, root):
    moved = dict(rows)
    exact_coordinates = {}
    for row, (control, direction) in directions.items():
        moved[row] = ex.add(moved[row], ex.mul(direction, root[control]))
        exact_coordinates[str(row)] = [qs(z) for z in moved[row]]
    numeric = {row: np.asarray([float(z) for z in point]) for row, point in moved.items()}
    result = search.evaluate(numeric, plane_tol=1e-6, strict_tol=1e-9)
    if not result.valid:
        return {
            "valid": False,
            "error": result.error,
            "moved_coordinates_exact": exact_coordinates,
        }
    diag = search.diagnostics(result)
    exact_faces = exactify_faces_allow_inactive_coplanars(moved, result)
    _, exact_centroid = ex.exact_mass(moved, exact_faces)
    (
        exact_incidence,
        exact_active,
        _,
        _,
        _,
        exact_stable,
        exact_unstable,
        exact_saddles,
    ) = ex.exact_mechanics(moved, exact_faces, exact_centroid)
    exact_f_vector = [len(exact_active), len(exact_incidence), len(exact_faces)]
    exact_class = [len(exact_stable), len(exact_unstable), len(exact_saddles)]
    assert exact_f_vector == diag["f_vector"]
    assert exact_class == diag["class"]
    rails = forced_rails()
    missing = sorted(rails - set(exact_incidence))
    base_face_present = any(set(face["cycle"]) == set(range(17)) for face in exact_faces)
    return {
        "valid": True,
        "exact_all_proposed_planes_support_all_119_rows": True,
        "exact_mass_centroid_and_mechanics_rebuilt": True,
        "f_vector": exact_f_vector,
        "class": exact_class,
        "base_face_present": base_face_present,
        "base_decision": diag["base"],
        "U8_unstable": 8 in exact_unstable,
        "U8_decision": diag["u8"],
        "forced_rails_present": len(rails) - len(missing),
        "all_37_forced_rails_present": not missing,
        "missing_forced_rails": [list(edge) for edge in missing],
        "stable_faces": [exact_faces[fi]["cycle"] for fi in exact_stable],
        "unstable_vertices": exact_unstable,
        "saddle_edges": [list(edge) for edge in exact_saddles],
        "hard": diag["hard"],
        "face_bad": diag["face_bad"],
        "vertex_bad": diag["vertex_bad"],
        "edge_bad": diag["edge_bad"],
        "moved_coordinates_exact": exact_coordinates,
    }


def main():
    rows = ex.read_exact_rows()
    seed_faces = ex.exactify_faces(rows, ex.numeric_faces(rows))
    incidence = edge_incidence(seed_faces)
    directions = control_directions(rows)
    q = build_jets(rows, directions)
    death_names, death_jets = six_death_jets(q, seed_faces, incidence)
    gradients = [jet.d for jet in death_jets]
    determinant = rj.determinant(gradients)
    assert determinant != 0 and rj.matrix_rank(gradients) == 6
    root = solve_exact_square(gradients, [-jet.v for jet in death_jets])

    physical_displacements = {}
    max_item = None
    axes = "xyz"
    for row, (control, direction) in directions.items():
        disp = tuple(root[control] * z for z in direction)
        physical_displacements[str(row)] = [qs(z) for z in disp]
        for axis, value in zip(axes, disp):
            item = (abs(value), row, axis, value)
            if max_item is None or item[0] > max_item[0]:
                max_item = item
    assert max_item is not None and max_item[0] > TRUST

    drows, dlabels = physical_rows(directions)
    farkas = exact_physical_farkas(death_names, death_jets, drows, dlabels)
    probes = [exact_probe(rows, sign) for sign in (1, -1)]
    root_audit = fresh_root_audit(rows, directions, root)
    assert root_audit["valid"]
    assert not root_audit["base_face_present"]
    assert not root_audit["U8_unstable"]
    assert not root_audit["all_37_forced_rails_present"]

    out = {
        "version": 1,
        "type": "exact sixth support-valid control and physical-trust obstruction",
        "scope": (
            "Exact first jet of the strict reconstructed supporting-shell seed. Actual hulls are "
            "rebuilt at both support-valid probes and at the formal affine root. The Farkas theorem "
            "is local to the named six-control chart and physical trust radius 1/10."
        ),
        "seed": "rank5_reconstruction.json exact (61,150,91), class (3,4,5) shell cell",
        "controls": CONTROL_NAMES,
        "directions": {
            str(row): {
                "control": CONTROL_NAMES[control],
                "direction_exact": [qs(z) for z in direction],
            }
            for row, (control, direction) in directions.items()
        },
        "sixth_control": {
            "row": 246,
            "name": "t246",
            "direction_exact": [qs(z) for z in SIXTH_DIRECTION],
            "shell_plane_normal_exact": [qs(z) for z in ex.N],
            "normal_dot_direction_exact": qs(ex.dot(ex.N, SIXTH_DIRECTION)),
            "support_valid_exact_actual_hull_probes": probes,
        },
        "selected_six_deaths": {
            name: {
                "value_exact": qs(jet.v),
                "value_decimal": float(jet.v),
                "gradient_exact": [qs(z) for z in jet.d],
                "gradient_decimal": [float(z) for z in jet.d],
            }
            for name, jet in zip(death_names, death_jets)
        },
        "exact_rank": {
            "six_by_six_gradient_rank": 6,
            "gradient_determinant_exact": qs(determinant),
            "gradient_determinant_log10_abs": qlog10(determinant),
        },
        "unique_affine_common_root": {
            "parameters_exact": [qs(z) for z in root],
            "parameters_decimal": [float(z) for z in root],
            "physical_displacements_exact": physical_displacements,
            "max_abs_physical_displacement_exact": qs(max_item[0]),
            "max_abs_physical_displacement_decimal": float(max_item[0]),
            "max_coordinate": {"row": max_item[1], "axis": max_item[2], "value_exact": qs(max_item[3])},
            "outside_physical_trust_1_over_10": max_item[0] > TRUST,
            "fresh_actual_hull_audit": root_audit,
        },
        "physical_trust_farkas_certificate": farkas,
        "verdict": "EXACT_RANK6_SUPPORT_CONTROL_VALID_BUT_TRUST_BOX_TARGET_INFEASIBLE",
        "conclusion": (
            "The row246 tangent is a real support-valid sixth control and gives exact gradient rank six. "
            "Its formal common root is macroscopic and leaves the actual cell, base, U8 and rails. "
            "Within physical coordinate trust 1/10, the named six-death subsystem has an exact negative "
            "Farkas certificate, so there is no guarded shared event in this explicit branch."
        ),
    }
    OUTPUT.write_text(json.dumps(out, indent=2) + "\n")
    print(out["verdict"])
    print("rank/determinant sign", 6, 1 if determinant > 0 else -1)
    print("formal root max physical displacement", float(max_item[0]))
    print("fresh root f/class", root_audit["f_vector"], root_audit["class"])
    print("fresh root base/U8/rails", root_audit["base_face_present"], root_audit["U8_unstable"], root_audit["forced_rails_present"])
    print("exact Farkas RHS", farkas["repaired_farkas_rhs_decimal"])
    print("output", OUTPUT)


if __name__ == "__main__":
    main()
