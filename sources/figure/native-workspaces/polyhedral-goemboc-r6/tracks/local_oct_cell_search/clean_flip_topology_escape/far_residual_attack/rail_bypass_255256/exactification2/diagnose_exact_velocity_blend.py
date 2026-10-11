#!/usr/bin/env python3
"""Intersect the exact first-jet cones of the candidate and sparse rail rays.

The blended velocity is

    v(alpha) = (1-alpha) * v_candidate + alpha * v_sparse.

Every first derivative below is exactly affine in ``alpha``.  This script
therefore solves the strict one-dimensional feasibility problem over the
rationals; it does not sample alpha and does not claim a finite material step.
"""
from __future__ import annotations

import hashlib
import json
import sys
from fractions import Fraction as Q
from pathlib import Path


sys.set_int_max_str_digits(0)

HERE = Path(__file__).resolve().parent
PARENT = HERE.parents[1]

import build_exactification_certificate as cert  # noqa: E402


CANDIDATE_PATH = HERE / "exact_candidate_path.json"
SPARSE_PATH = PARENT / "exact_event_path.json"
OUTPUT = HERE / "exact_velocity_blend_diagnostic.json"
BLENDED_PATH = HERE / "exact_blended_path.json"


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def qs(value: Q) -> str:
    return cert.ex.qs(value)


def read_velocity(path: Path):
    packet = json.loads(path.read_text())
    velocity = {
        int(label): tuple(Q(value) for value in xyz)
        for label, xyz in packet["velocity"].items()
    }
    return packet, velocity


def affine_path(source, velocity):
    if set(source) != set(velocity):
        raise AssertionError(("velocity/source row mismatch", len(source), len(velocity)))
    return {
        label: tuple(
            cert.ex.P((source[label][axis], velocity[label][axis]))
            for axis in range(3)
        )
        for label in source
    }


def exact_first_jets(source, faces, velocity):
    path = affine_path(source, velocity)
    d6, xscaled = cert.ex.scaled_centered(path, faces)
    incidence, _neighbors, face_by_key = cert.ex.edge_data(faces)

    jets = {}
    sources = {}

    face_key = tuple(sorted(cert.TARGET_FACE))
    face_index = face_by_key[face_key]
    face_values = cert.ex.face_components(path, faces, xscaled, face_index)
    face_lookup = {edge: (raw, reference) for edge, raw, reference in face_values}
    face_raw, face_reference = face_lookup[(198, 243)]
    face_sign = Q(1) if face_reference.eval(Q(0)) > 0 else Q(-1)
    residuals = {
        "S[198,243,245]:edge(198,243)": face_sign * face_raw,
        "U1:neighbor(2)": cert.ex.vertex_component(path, xscaled, 1, 2),
    }
    for edge in cert.TARGET_EDGES:
        components = cert.ex.edge_components(path, faces, xscaled, incidence, edge)
        components["one_minus_t"] = (
            4 * d6 * components["direction_norm2"] - components["t"]
        )
        residuals[f"H({edge[0]},{edge[1]}):one_minus_t"] = components[
            "one_minus_t"
        ]
    if set(residuals) != cert.ACTIVE_NAMES:
        raise AssertionError(("targeted residual family drift", set(residuals)))
    for name, polynomial in sorted(residuals.items()):
        sources[name] = polynomial.eval(Q(0))
        jets[name] = -polynomial.derivative().eval(Q(0))

    for key in cert.CIRCUIT_SUPPORT_ROWS:
        face_index, witness = key
        cycle = faces[face_index]
        normal = cert.ex.cycle_normal(cycle, path)
        polynomial = cert.ex.dot(
            normal, cert.ex.sub(path[witness], path[cycle[0]])
        )
        source_value = polynomial.eval(Q(0))
        source_sign = Q(1) if source_value > 0 else Q(-1)
        name = f"oriented_support:f{key[0]}:w{key[1]}"
        sources[name] = source_sign * source_value
        jets[name] = source_sign * polynomial.derivative().eval(Q(0))

    a, b, c, d = cert.CIRCUIT
    raw = cert.ex.det3(
        cert.ex.sub(path[b], path[a]),
        cert.ex.sub(path[c], path[a]),
        cert.ex.sub(path[d], path[a]),
    )
    source_value = raw.eval(Q(0))
    source_sign = Q(1) if source_value > 0 else Q(-1)
    name = "oriented_circuit_determinant"
    sources[name] = source_sign * source_value
    jets[name] = source_sign * raw.derivative().eval(Q(0))
    return sources, jets


def strict_interval(candidate_jets, sparse_jets):
    lower = Q(0)
    upper = Q(1)
    constraints = {}
    for name in sorted(candidate_jets):
        intercept = candidate_jets[name]
        slope = sparse_jets[name] - intercept
        record = {
            "candidate_margin": qs(intercept),
            "sparse_margin": qs(sparse_jets[name]),
            "blend_intercept": qs(intercept),
            "blend_slope": qs(slope),
            "required": "intercept + alpha*slope > 0",
        }
        if not slope:
            if intercept <= 0:
                raise RuntimeError(("identically infeasible blend constraint", name))
            record["boundary"] = None
        else:
            boundary = -intercept / slope
            record["boundary"] = qs(boundary)
            if slope > 0:
                lower = max(lower, boundary)
                record["sense"] = "alpha > boundary"
            else:
                upper = min(upper, boundary)
                record["sense"] = "alpha < boundary"
        constraints[name] = record
    if not lower < upper:
        return lower, upper, None, constraints, {}
    alpha = (lower + upper) / 2
    margins = {
        name: candidate_jets[name] + alpha * (sparse_jets[name] - candidate_jets[name])
        for name in candidate_jets
    }
    if any(value <= 0 for value in margins.values()):
        raise AssertionError(("internal alpha is not strict", alpha, margins))
    return lower, upper, alpha, constraints, margins


def main() -> None:
    candidate_packet, candidate = read_velocity(CANDIDATE_PATH)
    sparse_packet, sparse = read_velocity(SPARSE_PATH)
    source = cert.ex.read_rows(cert.SOURCE)
    faces = json.loads(cert.FACES_PATH.read_text())
    if set(candidate) != set(source) or set(sparse) != set(source):
        raise AssertionError("component velocity is incomplete")

    candidate_sources, candidate_jets = exact_first_jets(source, faces, candidate)
    sparse_sources, sparse_jets = exact_first_jets(source, faces, sparse)
    if candidate_sources != sparse_sources:
        raise AssertionError("component paths disagree at their common exact source")
    if set(candidate_jets) != set(sparse_jets):
        raise AssertionError("component first-jet families differ")

    lower, upper, alpha, constraints, margins = strict_interval(
        candidate_jets, sparse_jets
    )
    active_lower = sorted(
        name
        for name, row in constraints.items()
        if row.get("sense") == "alpha > boundary" and Q(row["boundary"]) == lower
    )
    active_upper = sorted(
        name
        for name, row in constraints.items()
        if row.get("sense") == "alpha < boundary" and Q(row["boundary"]) == upper
    )
    if alpha is None:
        payload = {
            "version": 1,
            "verdict": "EXACT_TWO_RAY_STRICT_FIRST_JET_CONE_EMPTY",
            "scope": "first derivatives at the common exact source only",
            "finite_step_certified": False,
            "component_files_sha256": {
                str(CANDIDATE_PATH.relative_to(cert.ROOT)): sha256(CANDIDATE_PATH),
                str(SPARSE_PATH.relative_to(cert.ROOT)): sha256(SPARSE_PATH),
            },
            "candidate_exact_margins": {
                name: qs(value) for name, value in sorted(candidate_jets.items())
            },
            "sparse_exact_margins": {
                name: qs(value) for name, value in sorted(sparse_jets.items())
            },
            "incompatible_strict_bounds": {
                "lower": qs(lower),
                "upper": qs(upper),
                "lower_decimal": float(lower),
                "upper_decimal": float(upper),
                "active_lower_constraints": active_lower,
                "active_upper_constraints": active_upper,
            },
            "constraints": constraints,
            "conclusion": (
                "No convex blend of the two saved exact velocities satisfies all "
                "seven strict first-jet inequalities. This excludes only their "
                "two-ray cone, not the complete 165-control chart."
            ),
            "next_action": "Solve the complete chart with all seven strict rows included.",
        }
        OUTPUT.write_text(json.dumps(payload, indent=2) + "\n")
        if BLENDED_PATH.exists():
            BLENDED_PATH.unlink()
        print(payload["verdict"])
        print("incompatible_interval", float(lower), float(upper))
        print("active_lower_constraints", active_lower)
        print("active_upper_constraints", active_upper)
        print("diagnostic_sha256", sha256(OUTPUT))
        return
    blended = {
        label: tuple(
            (Q(1) - alpha) * candidate[label][axis] + alpha * sparse[label][axis]
            for axis in range(3)
        )
        for label in source
    }
    velocity_packet = {
        str(label): [qs(value) for value in blended[label]]
        for label in sorted(blended)
    }
    digest = cert.canonical_hash(velocity_packet)

    path_payload = {
        "version": 1,
        "type": "exact rational interior blend of full-control and sparse rail rays",
        "method": (
            "Exact intersection of seven strict affine first-jet inequalities; "
            "alpha is the rational midpoint of the resulting open interval."
        ),
        "source_sha256": sha256(cert.SOURCE),
        "faces_sha256": sha256(cert.FACES_PATH),
        "rejected_event_certificate_sha256": sha256(cert.REJECTED_CERTIFICATE),
        "sparse_path_sha256": sha256(SPARSE_PATH),
        "candidate_path_sha256": sha256(CANDIDATE_PATH),
        "proposal_sha256": candidate_packet["proposal_sha256"],
        "candidate_sha256": candidate_packet["candidate_sha256"],
        "blend_alpha_sparse_weight": qs(alpha),
        "component_velocity_digests": {
            "candidate": candidate_packet["velocity_digest"],
            "sparse": sparse_packet["velocity_digest"],
        },
        "velocity": velocity_packet,
        "velocity_digest": digest,
        "parameter_semantics": "point(t) = exact_source + t * blended_exact_velocity",
        "certified_step_parameter": "UNSET_UNTIL_COMPLETE_INTERVAL_AUDIT",
    }
    BLENDED_PATH.write_text(json.dumps(path_payload, indent=2) + "\n")

    payload = {
        "version": 1,
        "verdict": "EXACT_TWO_RAY_STRICT_FIRST_JET_CONE_NONEMPTY",
        "scope": "first derivatives at the common exact source only",
        "finite_step_certified": False,
        "component_files_sha256": {
            str(CANDIDATE_PATH.relative_to(cert.ROOT)): sha256(CANDIDATE_PATH),
            str(SPARSE_PATH.relative_to(cert.ROOT)): sha256(SPARSE_PATH),
        },
        "strict_alpha_interval": {
            "lower": qs(lower),
            "upper": qs(upper),
            "lower_decimal": float(lower),
            "upper_decimal": float(upper),
            "both_bounds_strict": True,
        },
        "selected_alpha": qs(alpha),
        "selected_alpha_decimal": float(alpha),
        "constraints": constraints,
        "selected_exact_margins": {
            name: qs(value) for name, value in sorted(margins.items())
        },
        "blended_velocity_digest": digest,
        "blended_path_sha256": sha256(BLENDED_PATH),
        "next_action": (
            "Find and certify a positive rational step with the complete 7904-primitive "
            "Bernstein audit; this first-jet result alone is not a material-step claim."
        ),
    }
    OUTPUT.write_text(json.dumps(payload, indent=2) + "\n")
    print(payload["verdict"])
    print("strict_alpha_interval", float(lower), float(upper))
    print("selected_alpha", qs(alpha), float(alpha))
    for name, value in sorted(margins.items()):
        print(name, "margin", float(value))
    print("diagnostic_sha256", sha256(OUTPUT))
    print("blended_path_sha256", sha256(BLENDED_PATH))


if __name__ == "__main__":
    main()
