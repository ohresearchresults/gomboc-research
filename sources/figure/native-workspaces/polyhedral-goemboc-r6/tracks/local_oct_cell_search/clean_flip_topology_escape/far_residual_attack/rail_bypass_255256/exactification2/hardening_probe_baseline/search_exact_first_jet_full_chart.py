#!/usr/bin/env python3
"""Search the complete 165D chart using exact analytic target first jets.

The LP is a numerical proposer.  Its seven decisive rows are reconstructed as
exact rational first derivatives in an exact complete affine chart before the
solve.  A selected floating solution is rationalized in that same chart and
must satisfy all seven inequalities exactly.  Complete interval certification
is deliberately left to the separate exact builder and verifier.
"""
from __future__ import annotations

import argparse
import sys
from dataclasses import dataclass
from fractions import Fraction as Q
from pathlib import Path

import numpy as np
from scipy import sparse
from scipy.optimize import linprog


sys.set_int_max_str_digits(0)

HERE = Path(__file__).resolve().parent
PARENT = HERE.parents[1]
sys.path.insert(0, str(PARENT))

import attack_common as common  # noqa: E402
import build_exactification_certificate as cert  # noqa: E402
import exactification_provenance as provenance  # noqa: E402


OUTPUT = HERE / "exact_first_jet_full_chart_search.json"
ENDPOINT = HERE / "exact_first_jet_full_chart_endpoint.csv"
PATH_DEFINITION = HERE / "exact_first_jet_full_chart_path.json"


@dataclass(frozen=True)
class ExactControl:
    vertex: int
    name: str
    vector: tuple[Q, Q, Q]


def canonical_hash(value) -> str:
    return provenance.canonical_hash(value)


def qs(value: Q) -> str:
    return cert.ex.qs(value)


def exact_controls(source):
    e1 = cert.ex.sub(source[1], source[0])
    e2 = cert.ex.sub(source[2], source[0])
    if not any(cert.ex.cross(e1, e2)):
        raise AssertionError("exact base basis is singular")
    units = (
        ("x", (Q(1), Q(0), Q(0))),
        ("y", (Q(0), Q(1), Q(0))),
        ("z", (Q(0), Q(0), Q(1))),
    )
    controls = []
    for vertex in sorted(source):
        if vertex in cert.BASE:
            controls.append(ExactControl(vertex, f"v{vertex}:base_e1", e1))
            controls.append(ExactControl(vertex, f"v{vertex}:base_e2", e2))
        else:
            for axis, vector in units:
                controls.append(ExactControl(vertex, f"v{vertex}:{axis}", vector))
    if len(controls) != 165:
        raise AssertionError(("complete chart dimension drift", len(controls)))
    return controls


def dual_points(source, controls):
    dim = len(controls)
    zero = cert.ex.P.zero()
    by_vertex = {}
    for index, control in enumerate(controls):
        by_vertex.setdefault(control.vertex, []).append((index, control.vector))
    points = {}
    for label in sorted(source):
        xyz = []
        for axis in range(3):
            derivatives = [zero] * dim
            for index, vector in by_vertex.get(label, ()):  # exactly 2 or 3 rows
                derivatives[index] = cert.ex.P.coerce(vector[axis])
            xyz.append(
                cert.ex.JP(cert.ex.P.coerce(source[label][axis]), tuple(derivatives))
            )
        points[label] = tuple(xyz)
    return points


def jp_value(row):
    return row.v.eval(Q(0))


def jp_gradient(row):
    return tuple(value.eval(Q(0)) for value in row.d)


def exact_target_rows(source, faces, controls):
    points = dual_points(source, controls)
    d6, xscaled = cert.ex.scaled_centered(points, faces)
    incidence, _neighbors, face_by_key = cert.ex.edge_data(faces)

    face_key = tuple(sorted(cert.TARGET_FACE))
    face_index = face_by_key[face_key]
    cycle = faces[face_index]
    directed_edge = next(
        (a, b)
        for a, b in zip(cycle, cycle[1:] + cycle[:1])
        if tuple(sorted((a, b))) == (198, 243)
    )
    a, b = directed_edge
    normal = cert.ex.cycle_normal(cycle, points)
    edge = cert.ex.sub(points[b], points[a])
    normal_norm2 = cert.ex.norm2(normal)
    hbar = cert.ex.dot(normal, xscaled[a])
    face_raw = cert.ex.dot(
        cert.ex.cross(
            edge,
            cert.ex.sub(
                cert.ex.mul(normal, hbar),
                cert.ex.mul(xscaled[a], normal_norm2),
            ),
        ),
        normal,
    )
    source_normal = cert.ex.cycle_normal(cycle, source)
    source_reference = tuple(
        sum((source[label][axis] for label in cycle), Q(0)) / len(cycle)
        for axis in range(3)
    )
    source_reference_value = cert.ex.dot(
        cert.ex.cross(
            cert.ex.sub(source[b], source[a]),
            cert.ex.sub(source_reference, source[a]),
        ),
        source_normal,
    )
    if not source_reference_value:
        raise AssertionError("zero target face reference")
    face_sign = Q(1) if source_reference_value > 0 else Q(-1)
    active = {
        "S[198,243,245]:edge(198,243)": face_sign * face_raw,
        "U1:neighbor(2)": cert.ex.vertex_component(points, xscaled, 1, 2),
    }
    for edge in cert.TARGET_EDGES:
        components = cert.ex.edge_components(points, faces, xscaled, incidence, edge)
        components["one_minus_t"] = (
            4 * d6 * components["direction_norm2"] - components["t"]
        )
        active[f"H({edge[0]},{edge[1]}):one_minus_t"] = components[
            "one_minus_t"
        ]
    if set(active) != cert.ACTIVE_NAMES:
        raise AssertionError(("active target family drift", set(active)))

    rows = {}
    for name, row in active.items():
        source_value = jp_value(row)
        if source_value <= 0:
            raise AssertionError(("nonpositive active source", name, source_value))
        rows[name] = {
            "source": source_value,
            "good_gradient": tuple(-value for value in jp_gradient(row)),
            "sense": "raw derivative < 0",
        }

    for face_index, witness in cert.CIRCUIT_SUPPORT_ROWS:
        cycle = faces[face_index]
        normal = cert.ex.cycle_normal(cycle, points)
        raw = cert.ex.dot(
            normal, cert.ex.sub(points[witness], points[cycle[0]])
        )
        sign = Q(1) if jp_value(raw) > 0 else Q(-1)
        row = sign * raw
        name = f"oriented_support:f{face_index}:w{witness}"
        rows[name] = {
            "source": jp_value(row),
            "good_gradient": jp_gradient(row),
            "sense": "oriented derivative > 0",
        }

    a, b, c, d = cert.CIRCUIT
    raw = cert.ex.det3(
        cert.ex.sub(points[b], points[a]),
        cert.ex.sub(points[c], points[a]),
        cert.ex.sub(points[d], points[a]),
    )
    sign = Q(1) if jp_value(raw) > 0 else Q(-1)
    row = sign * raw
    rows["oriented_circuit_determinant"] = {
        "source": jp_value(row),
        "good_gradient": jp_gradient(row),
        "sense": "oriented derivative > 0",
    }
    if len(rows) != 7 or any(row["source"] <= 0 for row in rows.values()):
        raise AssertionError(("seven-row target packet drift", rows.keys()))
    return rows


def scaled_rows(matrix, rhs):
    matrix = sparse.csr_matrix(matrix)
    row_max = np.asarray(np.abs(matrix).max(axis=1).toarray()).ravel()
    scale = np.maximum.reduce((row_max, np.abs(rhs), np.full(len(rhs), 1e-30)))
    return sparse.diags(1.0 / scale) @ matrix, rhs / scale


def solve_scenario(
    *, trust, controls_float, points_float, ids, faces, target_rows,
    support_values, support_jac, guard_values, guard_jac, protected_indices,
    residual_values, residual_jac,
):
    dim = len(controls_float)
    retention = 0.5
    blocks = []
    rhs = []

    support_relative = sparse.diags(1.0 / support_values) @ support_jac
    blocks.append(
        sparse.hstack((
            -trust * support_relative,
            sparse.csr_matrix((len(support_values), 1)),
        ), format="csr")
    )
    rhs.append(np.full(len(support_values), 1.0 - retention))

    protected_values = guard_values[protected_indices]
    protected_jac = sparse.csr_matrix(guard_jac[protected_indices])
    protected_relative = sparse.diags(1.0 / protected_values) @ protected_jac
    blocks.append(
        sparse.hstack((
            -trust * protected_relative,
            sparse.csr_matrix((len(protected_values), 1)),
        ), format="csr")
    )
    rhs.append(np.full(len(protected_values), 1.0 - retention))

    residual_relative = residual_jac / residual_values[:, None]
    blocks.append(sparse.csr_matrix(np.c_[
        -trust * residual_relative,
        np.zeros(len(residual_values)),
    ]))
    rhs.append(np.full(len(residual_values), 1.0 - retention))

    exact_rows = []
    exact_names = []
    for name, row in sorted(target_rows.items()):
        source_scale = abs(float(row["source"]))
        gradient = np.asarray([float(value) for value in row["good_gradient"]])
        if source_scale == 0 or not np.all(np.isfinite(gradient)):
            raise AssertionError(("invalid exact target row", name))
        exact_rows.append(np.r_[-trust * gradient / source_scale, 1.0])
        exact_names.append(name)
    blocks.append(sparse.csr_matrix(np.asarray(exact_rows)))
    rhs.append(np.zeros(len(exact_rows)))

    matrix = sparse.vstack(blocks, format="csr")
    vector = np.concatenate(rhs)
    matrix, vector = scaled_rows(matrix, vector)
    lp = linprog(
        np.r_[np.zeros(dim), -1.0],
        A_ub=matrix,
        b_ub=vector,
        bounds=[(-1.0, 1.0)] * dim + [(0.0, 1.0)],
        method="highs-ds",
        options={"presolve": False},
    )
    record = {
        "trust": trust,
        "retention": retention,
        "success": bool(lp.success),
        "status": int(lp.status),
        "message": str(lp.message),
        "constraint_count": int(matrix.shape[0]),
    }
    if not lp.success:
        return record, None
    coefficients = trust * np.asarray(lp.x[:-1], dtype=float)
    exact_margins_float = {
        name: float(np.dot(
            np.asarray([float(value) for value in row["good_gradient"]]),
            coefficients,
        ))
        for name, row in target_rows.items()
    }
    endpoint = common.construct(points_float, ids, controls_float, coefficients)
    try:
        actual = common.fresh_summary(ids, endpoint, coplanar_rel=2e-12)
        f_vector = [len(actual.active), len(actual.edges), len(actual.faces)]
        own_class = [len(actual.stable), len(actual.unstable), len(actual.saddles)]
        missing_rails = sorted(common.rail_edges() - set(actual.edges))
        actual_valid = (
            f_vector == [61, 162, 103]
            and own_class == [2, 2, 2]
            and not missing_rails
            and min(exact_margins_float.values()) > 0
        )
        error = None
    except Exception as exc:
        actual_valid = False
        f_vector = None
        own_class = None
        missing_rails = []
        error = repr(exc)
    record.update({
        "gamma": float(lp.x[-1]),
        "coefficient_linf": float(np.max(np.abs(coefficients))),
        "nonzero_control_count": int(np.count_nonzero(np.abs(coefficients) > 1e-15)),
        "exact_target_margin_float": exact_margins_float,
        "actual_valid": actual_valid,
        "actual_error": error,
        "actual_f_vector": f_vector,
        "actual_class": own_class,
        "actual_missing_rails": [list(edge) for edge in missing_rails],
    })
    return record, coefficients if actual_valid else None


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--source", default=str(cert.SOURCE))
    parser.add_argument("--source-certificate")
    parser.add_argument("--source-verification")
    parser.add_argument("--output", default=str(OUTPUT))
    parser.add_argument("--endpoint", default=str(ENDPOINT))
    parser.add_argument("--path-definition", default=str(PATH_DEFINITION))
    args = parser.parse_args()

    source_path = provenance.contained_path(
        args.source, base=HERE, root=cert.ROOT, context="search source"
    )
    output_path = provenance.contained_path(
        args.output, base=HERE, root=cert.ROOT, context="search output"
    )
    endpoint_path = provenance.contained_path(
        args.endpoint, base=HERE, root=cert.ROOT, context="search endpoint"
    )
    path_definition = provenance.contained_path(
        args.path_definition, base=HERE, root=cert.ROOT, context="search path definition"
    )
    faces_path = provenance.contained_path(
        cert.FACES_PATH, base=HERE, root=cert.ROOT, context="faces"
    )
    rejected_certificate_path = provenance.contained_path(
        cert.REJECTED_CERTIFICATE,
        base=HERE,
        root=cert.ROOT,
        context="rejected certificate",
    )
    rejected_path = provenance.contained_path(
        cert.REJECTED_PATH, base=HERE, root=cert.ROOT, context="rejected path"
    )
    default_source = provenance.contained_path(
        cert.DEFAULT_SOURCE, base=HERE, root=cert.ROOT, context="default source"
    )
    source_snapshot = provenance.read_snapshot(source_path)
    faces_snapshot = provenance.read_snapshot(faces_path)
    rejected_certificate_snapshot = provenance.read_snapshot(rejected_certificate_path)
    rejected_path_snapshot = provenance.read_snapshot(rejected_path)
    trust_snapshots = provenance.trusted_code_snapshots(cert.ROOT, "search")
    output_paths = [output_path, endpoint_path, path_definition]
    input_paths = [
        source_path, faces_path, rejected_certificate_path, rejected_path
    ]
    input_paths.extend(snapshot.path for snapshot in trust_snapshots)
    dynamic_source = source_path != default_source

    source_lineage = None
    lineage_evidence = None
    if dynamic_source:
        if not args.source_certificate or not args.source_verification:
            raise ValueError("a nondefault source requires its certificate and independent receipt")
        source_certificate_path = provenance.contained_path(
            args.source_certificate,
            base=HERE,
            root=cert.ROOT,
            context="source certificate",
        )
        source_verification_path = provenance.contained_path(
            args.source_verification,
            base=HERE,
            root=cert.ROOT,
            context="source verification",
        )
        lineage_evidence = provenance.validate_dynamic_lineage(
            root=cert.ROOT,
            current_source=source_snapshot,
            certificate_snapshot=provenance.read_snapshot(source_certificate_path),
            verification_snapshot=provenance.read_snapshot(source_verification_path),
        )
        source_lineage = lineage_evidence.payload
        input_paths.extend(snapshot.path for snapshot in lineage_evidence.snapshots)

    protected_defaults = []
    if dynamic_source:
        protected_defaults = [
            provenance.contained_path(OUTPUT, base=HERE, root=cert.ROOT, context="default search output"),
            provenance.contained_path(ENDPOINT, base=HERE, root=cert.ROOT, context="default search endpoint"),
            provenance.contained_path(
                PATH_DEFINITION, base=HERE, root=cert.ROOT, context="default search path"
            ),
        ]
    provenance.assert_isolated(
        [*output_paths, *input_paths, *protected_defaults], "first-jet search"
    )
    input_snapshots = [
        source_snapshot,
        faces_snapshot,
        rejected_certificate_snapshot,
        rejected_path_snapshot,
        *trust_snapshots,
    ]
    if lineage_evidence is not None:
        input_snapshots.extend(lineage_evidence.snapshots)
    provenance.assert_snapshots_current(input_snapshots)
    producer_trust = provenance.expected_trust_packet(cert.ROOT, "search")
    source = provenance.parse_exact_csv(source_snapshot)
    faces = provenance.parse_json(faces_snapshot)
    ids = sorted(source)
    points_float = np.asarray(
        [[float(value) for value in source[label]] for label in ids], dtype=float
    )
    controls = exact_controls(source)
    controls_float = [
        common.Control(
            control.vertex,
            control.name,
            tuple(float(value) for value in control.vector),
        )
        for control in controls
    ]

    print("constructing seven exact 165D first-jet rows", flush=True)
    target_rows = exact_target_rows(source, faces, controls)
    target_digest = canonical_hash({
        name: {
            "source": qs(row["source"]),
            "good_gradient": [qs(value) for value in row["good_gradient"]],
            "sense": row["sense"],
        }
        for name, row in sorted(target_rows.items())
    })
    zero = np.zeros(len(controls))

    def residual_at(coefficients):
        return common.flatten_residual_components(
            common.residual_components(
                ids,
                common.construct(points_float, ids, controls_float, coefficients),
                faces,
            )
        )[1]

    def guard_at(coefficients):
        return common.class_guard_packet(
            ids,
            common.construct(points_float, ids, controls_float, coefficients),
            faces,
        )[0]

    residual_values, residual_jac = common.finite_difference_jacobian(
        residual_at, zero, epsilon=1e-7
    )
    guard_values, guard_jac = common.finite_difference_jacobian(
        guard_at, zero, epsilon=1e-7
    )
    _guard_values, guard_labels = common.class_guard_packet(ids, points_float, faces)
    target_guard_indices = set(common.target_guard_indices(guard_labels))
    protected_indices = np.asarray(
        [index for index in range(len(guard_labels)) if index not in target_guard_indices],
        dtype=int,
    )
    support_rows, support_values, support_jac = common.support_first_jet(
        ids, points_float, faces, controls_float, 1.0
    )
    if (
        len(support_rows) != 5959
        or np.any(support_values <= 0)
        or np.any(guard_values[protected_indices] <= 0)
        or np.any(residual_values <= 0)
    ):
        raise AssertionError("source guard packet is not strict")

    scenarios = []
    candidates = []
    for trust in (1e-8, 2e-8, 5e-8, 1e-7, 2e-7, 5e-7, 1e-6, 2e-6):
        record, coefficients = solve_scenario(
            trust=trust,
            controls_float=controls_float,
            points_float=points_float,
            ids=ids,
            faces=faces,
            target_rows=target_rows,
            support_values=support_values,
            support_jac=support_jac,
            guard_values=guard_values,
            guard_jac=guard_jac,
            protected_indices=protected_indices,
            residual_values=residual_values,
            residual_jac=residual_jac,
        )
        record["index"] = len(scenarios)
        scenarios.append(record)
        if coefficients is not None:
            candidates.append((record, coefficients))
        print("scenario", record["index"], record["success"], record.get("gamma"), record.get("actual_valid"), flush=True)

    if not candidates:
        payload = {
            "version": 1,
            "verdict": "NO_EXACT_TARGET_FIRST_JET_PRIMAL_IN_DECLARED_TRUST_GRID",
            "source_sha256": source_snapshot.sha256,
            "faces_sha256": faces_snapshot.sha256,
            "exact_target_jacobian_digest": target_digest,
            "scenarios": scenarios,
            "producer_trust": producer_trust,
        }
        if source_lineage is not None:
            payload["source_lineage"] = source_lineage
        provenance.assert_snapshots_current(input_snapshots)
        output_snapshot = provenance.atomic_write_json(output_path, payload)
        provenance.assert_snapshots_current([*input_snapshots, output_snapshot])
        print(payload["verdict"])
        return

    record, coefficients = max(candidates, key=lambda item: item[0]["gamma"])
    exact_coefficients = tuple(Q(format(value, ".17g")) for value in coefficients)
    velocity = {label: (Q(0), Q(0), Q(0)) for label in ids}
    for coefficient, control in zip(exact_coefficients, controls):
        velocity[control.vertex] = cert.ex.add(
            velocity[control.vertex], cert.ex.mul(control.vector, coefficient)
        )
    exact_margins = {
        name: sum(
            (gradient * coefficient for gradient, coefficient in zip(
                row["good_gradient"], exact_coefficients
            )),
            Q(0),
        )
        for name, row in target_rows.items()
    }
    if any(value <= 0 for value in exact_margins.values()):
        raise AssertionError(("rationalized selected direction is not strict", exact_margins))
    endpoint = {
        label: cert.ex.add(source[label], velocity[label]) for label in ids
    }
    checkpoint = cert.checkpoint(endpoint, faces)
    if (
        checkpoint["exact_support"]["f_vector"] != [61, 162, 103]
        or checkpoint["exact_mechanics"]["class"] != [2, 2, 2]
        or checkpoint["missing_forced_rails"]
    ):
        raise AssertionError(("exact endpoint left protected cell", checkpoint))
    velocity_packet = {
        str(label): [qs(value) for value in velocity[label]] for label in ids
    }
    exact_path = {
        label: tuple(
            cert.ex.P((source[label][axis], velocity[label][axis])) for axis in range(3)
        )
        for label in source
    }
    exact_ledger = cert.ex.mechanics_primitives(exact_path, faces)
    exact_support_rows = list(cert.ex.support_polynomials(exact_path, faces))
    first_jet_contract = cert.first_jet_contract(
        exact_path, exact_ledger, exact_support_rows
    )
    contract_margins = {
        name: row["directional_good_derivative"]
        for name, row in first_jet_contract["rows"].items()
    }
    expected_margins = {
        name: qs(value) for name, value in sorted(exact_margins.items())
    }
    if contract_margins != expected_margins:
        raise AssertionError("full-chart gradient and exact path first-jet contract disagree")
    path_payload = {
        "schema": provenance.FIRST_JET_PATH_SCHEMA,
        "version": provenance.FIRST_JET_PATH_VERSION,
        "type": provenance.FIRST_JET_PATH_TYPE,
        "verdict": provenance.FIRST_JET_PATH_VERDICT,
        "method": (
            "Solve in a complete exact 165D affine chart; rationalize the selected "
            "chart coefficients; verify all seven decisive first derivatives exactly."
        ),
        "source_sha256": source_snapshot.sha256,
        "faces_sha256": faces_snapshot.sha256,
        "rejected_event_certificate_sha256": rejected_certificate_snapshot.sha256,
        "sparse_path_sha256": rejected_path_snapshot.sha256,
        "selected_scenario_index": record["index"],
        "control_count": len(controls),
        "control_names": [control.name for control in controls],
        "exact_coefficients": [qs(value) for value in exact_coefficients],
        "exact_first_jet_good_margins": expected_margins,
        "first_jet_contract": first_jet_contract,
        "velocity": velocity_packet,
        "velocity_digest": canonical_hash(velocity_packet),
        "parameter_semantics": "point(t) = exact_source + t * exact_velocity",
        "proposed_horizon_parameter": "1",
        "producer_trust": producer_trust,
    }
    if source_lineage is not None:
        path_payload["source_lineage"] = source_lineage
    provenance.assert_snapshots_current(input_snapshots)
    endpoint_snapshot = provenance.atomic_write_bytes(
        endpoint_path, provenance.exact_csv_bytes(endpoint)
    )
    path_snapshot = provenance.atomic_write_json(path_definition, path_payload)
    payload = {
        "version": 1,
        "verdict": provenance.FIRST_JET_SEARCH_VERDICT,
        "proof_status": "FIRST_JET_ONLY_COMPLETE_INTERVAL_CERTIFICATE_REQUIRED",
        "source_sha256": source_snapshot.sha256,
        "faces_sha256": faces_snapshot.sha256,
        "mode_count": len(controls),
        "exact_target_jacobian_digest": target_digest,
        "scenarios": scenarios,
        "selected": record,
        "exact_selected_coefficients": [qs(value) for value in exact_coefficients],
        "exact_first_jet_good_margins": {
            name: qs(value) for name, value in sorted(exact_margins.items())
        },
        "exact_endpoint": {
            "file": provenance.relative_name(endpoint_path, cert.ROOT),
            "sha256": endpoint_snapshot.sha256,
            "support": checkpoint["exact_support"],
            "mechanics": checkpoint["exact_mechanics"],
            "missing_forced_rails": checkpoint["missing_forced_rails"],
        },
        "path_definition": {
            "file": provenance.relative_name(path_definition, cert.ROOT),
            "sha256": path_snapshot.sha256,
        },
        "next_action": "Run the complete exact 7904-primitive interval builder and clean verifier.",
        "producer_trust": producer_trust,
    }
    if source_lineage is not None:
        payload["source_lineage"] = source_lineage
    output_snapshot = provenance.atomic_write_json(output_path, payload)
    provenance.assert_snapshots_current(
        [*input_snapshots, endpoint_snapshot, path_snapshot, output_snapshot]
    )
    print(payload["verdict"])
    print("selected_scenario", record["index"], "gamma", record["gamma"])
    print("exact_class", checkpoint["exact_mechanics"]["class"])
    print("missing_rails", checkpoint["missing_forced_rails"])
    print("path_sha256", path_snapshot.sha256)
    print("output_sha256", output_snapshot.sha256)


if __name__ == "__main__":
    main()
