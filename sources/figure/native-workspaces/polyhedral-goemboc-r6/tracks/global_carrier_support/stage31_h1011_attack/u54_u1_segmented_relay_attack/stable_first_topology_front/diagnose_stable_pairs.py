#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import importlib.util
import json
import math
import sys
from dataclasses import dataclass
from fractions import Fraction as Q
from pathlib import Path

import numpy as np

HERE = Path(__file__).resolve().parent
ROOT = Path(sys.argv[1]).resolve() if len(sys.argv) > 1 else HERE.parents[4]
SIDE = (
    ROOT
    / "tracks/global_carrier_support/stage31_h1011_attack"
    / "u54_u1_segmented_relay_attack"
)
SOURCE = SIDE / "far_u1.csv"
CERTIFICATE = SIDE / "death_certificate.json"
VERIFICATION = SIDE / "death_verification.json"
CORE = ROOT / "tracks/global_carrier_support/rigorous_local_bypass/exact_core.py"
CLEAN = (
    ROOT
    / "tracks/local_oct_cell_search/clean_flip_topology_escape/far_residual_attack"
    / "verify_exact_event_certificate.py"
)
sys.path.insert(0, str(CORE.parent))
import exact_core as ex

module_name = "stable_saddle_clean_probe"
spec = importlib.util.spec_from_file_location(module_name, CLEAN)
clean = importlib.util.module_from_spec(spec)
sys.modules[module_name] = clean
spec.loader.exec_module(clean)

BASE = frozenset(range(17)) | {54}
BASE_KEY = tuple(sorted(BASE))
SADDLES = ((5, 6), (10, 11))


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def canonical_hash(value) -> str:
    return hashlib.sha256(
        json.dumps(value, sort_keys=True, separators=(",", ":")).encode()
    ).hexdigest()


def q17(value: float) -> Q:
    return Q(format(float(value), ".17g"))


def affine_path(source, velocity):
    return {
        label: tuple(
            ex.P((source[label][axis], velocity[label][axis]))
            for axis in range(3)
        )
        for label in source
    }


def exact_modes(source):
    e1 = ex.sub(source[1], source[0])
    e2 = ex.sub(source[2], source[0])
    if not any(ex.cross(e1, e2)):
        raise AssertionError("singular base chart")
    units = (
        ("x", (Q(1), Q(0), Q(0))),
        ("y", (Q(0), Q(1), Q(0))),
        ("z", (Q(0), Q(0), Q(1))),
    )
    modes = []
    for label in sorted(source):
        vectors = (("base_e1", e1), ("base_e2", e2)) if label in BASE else units
        for name, vector in vectors:
            velocity = {
                row: ((Q(0), Q(0), Q(0)) if row != label else vector)
                for row in source
            }
            modes.append((f"v{label}:{name}", velocity))
    if len(modes) != 165:
        raise AssertionError(("mode count", len(modes)))
    return modes


def owner_rows(path, faces):
    d6, xscaled = ex.scaled_centered(path, faces)
    incidence, _neighbors, face_by_key = ex.edge_data(faces)
    base_index = face_by_key[BASE_KEY]
    result = {}
    for edge in SADDLES:
        raw, reference = ex.face_component(
            path, faces, xscaled, base_index, edge
        )
        ref0 = reference.eval(Q(0))
        if not ref0:
            raise AssertionError(("zero base reference", edge))
        signed_raw = (1 if ref0 > 0 else -1) * raw
        components = ex.edge_components(path, faces, xscaled, incidence, edge)
        base_incidence_index = incidence[edge].index(base_index)
        # At an edge of face F_i, the face equilibrium reaches the boundary
        # when the coefficient of the *other* incident normal vanishes.
        beta_name = "beta2" if base_incidence_index == 0 else "beta1"
        shared = components[beta_name]
        direction = ex.sub(path[edge[1]], path[edge[0]])
        if base_incidence_index == 0:
            base_normal = components["n1"]
            other_normal = components["n2"]
        else:
            base_normal = components["n2"]
            other_normal = components["n1"]
        cross_factor = ex.dot(ex.cross(direction, other_normal), base_normal)
        identity = (
            components["gram"] * raw
            + ex.norm2(base_normal) * shared * cross_factor
        )
        if identity != ex.P.zero():
            raise AssertionError(("stable/saddle shared identity", edge, identity.exact()))
        result[edge] = {
            "stable": signed_raw,
            "saddle": shared,
            "beta_name": beta_name,
            "base_incidence_index": base_incidence_index,
            "identity": identity,
            "incident_face_keys": [
                tuple(sorted(faces[index])) for index in incidence[edge]
            ],
        }
    return result


@dataclass(frozen=True)
class Jet:
    value: Q = Q(0)
    derivative: Q = Q(0)

    @staticmethod
    def coerce(value):
        if isinstance(value, Jet):
            return value
        if isinstance(value, ex.P):
            if value.degree:
                raise TypeError("nonconstant polynomial cannot enter scalar Jet")
            return Jet(value.c[0])
        return Jet(Q(value))

    def __add__(self, other):
        other = Jet.coerce(other)
        return Jet(self.value + other.value, self.derivative + other.derivative)

    __radd__ = __add__

    def __neg__(self):
        return Jet(-self.value, -self.derivative)

    def __sub__(self, other):
        return self + (-Jet.coerce(other))

    def __rsub__(self, other):
        return Jet.coerce(other) - self

    def __mul__(self, other):
        other = Jet.coerce(other)
        return Jet(
            self.value * other.value,
            self.derivative * other.value + self.value * other.derivative,
        )

    __rmul__ = __mul__

    def __truediv__(self, scalar):
        return Jet(self.value / Q(scalar), self.derivative / Q(scalar))

    def __eq__(self, other):
        try:
            other = Jet.coerce(other)
        except (TypeError, ValueError):
            return False
        return self.value == other.value and self.derivative == other.derivative

    def __bool__(self):
        return bool(self.value or self.derivative)

    def __gt__(self, other):
        other = Jet.coerce(other)
        return self.value > other.value

    def __lt__(self, other):
        other = Jet.coerce(other)
        return self.value < other.value


def primitive_rows(points, faces):
    ledger = ex.mechanics_primitives(points, faces)
    yield "volume_d6", ledger["d6"], "mechanics_denominator"
    for face_index, witness, value in ex.support_polynomials(points, faces):
        yield f"support:f{face_index}:w{witness}", value, "support"
    for face_index, cycle in enumerate(faces):
        if len(cycle) <= 3:
            continue
        normal = ex.cycle_normal(cycle, points)
        for offset, current in enumerate(cycle):
            previous = cycle[offset - 1]
            following = cycle[(offset + 1) % len(cycle)]
            turn = ex.dot(
                ex.cross(
                    ex.sub(points[current], points[previous]),
                    ex.sub(points[following], points[current]),
                ),
                normal,
            )
            yield f"in_face_turn:f{face_index}:v{current}", turn, "in_face_turn"
    for face_key, values in sorted(ledger["reference"].items()):
        for edge, value in sorted(values.items()):
            yield f"face_reference:{face_key}:{edge}", value, "mechanics_denominator"
    for face_key, values in sorted(ledger["face"].items()):
        for edge, value in sorted(values.items()):
            yield f"face_raw:{face_key}:{edge}", value, "face_component"
    for vertex, values in sorted(ledger["vertex"].items()):
        for neighbor, value in sorted(values.items()):
            yield f"vertex:{vertex}:{neighbor}", value, "vertex_component"
    for edge, values in sorted(ledger["edge"].items()):
        for component in (
            "direction_norm2", "gram", "t", "one_minus_t", "beta1", "beta2"
        ):
            yield f"edge:{edge}:{component}", values[component], "edge_component"


def primitive_first_jets(source, velocity, faces):
    points = {
        label: tuple(
            Jet(source[label][axis], velocity[label][axis])
            for axis in range(3)
        )
        for label in source
    }
    rows = []
    for name, value, family in primitive_rows(points, faces):
        value = Jet.coerce(value)
        rows.append((name, value.value, value.derivative, family))
    if len(rows) != 7922:
        raise AssertionError(("primitive row count", len(rows)))
    return rows


def best_pivot(values, jacobian):
    best = None
    for first in range(len(jacobian[0])):
        for second in range(first + 1, len(jacobian[0])):
            determinant = (
                jacobian[0][first] * jacobian[1][second]
                - jacobian[0][second] * jacobian[1][first]
            )
            if not determinant:
                continue
            score = abs(float(determinant / (values[0] * values[1])))
            if best is None or score > best[0]:
                best = (score, first, second, determinant)
    if best is None:
        raise AssertionError("rank below two")
    return best


def corrected_direction(values, jacobian, pivot):
    normalized = np.asarray(
        [
            [float(value / source) for value in row]
            for source, row in zip(values, jacobian)
        ]
    )
    gram = normalized @ normalized.T
    approximate = -normalized.T @ np.linalg.solve(gram, np.ones(2))
    coefficients = [q17(value) for value in approximate]
    residual = [
        source
        + sum(
            (
                derivative * coefficient
                for derivative, coefficient in zip(row, coefficients)
            ),
            Q(0),
        )
        for source, row in zip(values, jacobian)
    ]
    first, second = pivot
    a, b = jacobian[0][first], jacobian[0][second]
    c, d = jacobian[1][first], jacobian[1][second]
    determinant = a * d - b * c
    coefficients[first] += (-residual[0] * d + b * residual[1]) / determinant
    coefficients[second] += (-a * residual[1] + residual[0] * c) / determinant
    final = [
        source
        + sum(
            (
                derivative * coefficient
                for derivative, coefficient in zip(row, coefficients)
            ),
            Q(0),
        )
        for source, row in zip(values, jacobian)
    ]
    if final != [Q(0), Q(0)]:
        raise AssertionError(("exact correction", final))
    return coefficients, np.linalg.svd(normalized, compute_uv=False).tolist()


def corrected_shared_direction(value, jacobian):
    normalized = np.asarray([float(derivative / value) for derivative in jacobian])
    norm2 = float(normalized @ normalized)
    if not norm2:
        raise AssertionError("zero shared primitive gradient")
    approximate = -normalized / norm2
    coefficients = [q17(number) for number in approximate]
    residual = value + sum(
        (derivative * coefficient for derivative, coefficient in zip(jacobian, coefficients)),
        Q(0),
    )
    pivot = max(
        range(len(jacobian)),
        key=lambda index: abs(float(jacobian[index] / value)),
    )
    if not jacobian[pivot]:
        raise AssertionError("zero shared primitive pivot")
    coefficients[pivot] -= residual / jacobian[pivot]
    final = value + sum(
        (derivative * coefficient for derivative, coefficient in zip(jacobian, coefficients)),
        Q(0),
    )
    if final:
        raise AssertionError(("exact shared correction", final))
    return coefficients, pivot, math.sqrt(norm2)


def combine_velocity(mode_packet, coefficients, source):
    return {
        label: tuple(
            sum(
                (
                    coefficient * mode[label][axis]
                    for coefficient, (_name, mode) in zip(coefficients, mode_packet)
                ),
                Q(0),
            )
            for axis in range(3)
        )
        for label in source
    }


def main():
    source_hash = sha256(SOURCE)
    certificate_hash = sha256(CERTIFICATE)
    verification_hash = sha256(VERIFICATION)
    certificate = json.loads(CERTIFICATE.read_text())
    verification = json.loads(VERIFICATION.read_text())
    far_key = next(
        key for key in verification["source_hashes"] if key.endswith("/far_u1.csv")
    )
    cert_key = next(
        key for key in verification["source_hashes"] if key.endswith("/death_certificate.json")
    )
    if (
        source_hash != "9f6c84382c05502766a17feb0cb9346bd44ec9f889e566e3e102d3d63a29ed77"
        or certificate_hash != "f799513eefcd1893b720111a8876f9027bc2b53ff598fbc68d6ff0fe37470996"
        or verification_hash != "86b1fb7f4e352ec162979620be43d6b02b5d5117d9e3fd305e04d84912a0ed03"
        or verification.get("verdict")
        != "INDEPENDENT_EXACT_U54_DEATH_VERIFICATION_PASS"
        or verification["source_hashes"][far_key] != source_hash
        or verification["source_hashes"][cert_key] != certificate_hash
        or verification.get("far_u1_class") != [2, 2, 2]
        or verification.get("relay_complete") is not True
        or certificate.get("verdict") != "EXACT_U54_DEATH_EPOCH_PASS"
    ):
        raise AssertionError("death lineage mismatch")

    source = ex.read_rows(SOURCE)
    clean_points = clean.read_exact_csv(SOURCE)
    if clean_points != source:
        raise AssertionError("independent CSV readers disagree")
    faces, hull = clean.fresh_maximal_faces(clean_points)
    support = clean.supporting_cell(clean_points, faces)
    clean_ledger, mechanics = clean.classify_point(clean_points, faces)
    expected = {
        "class": [2, 2, 2],
        "stable_faces": [sorted(BASE), [7, 8, 245]],
        "unstable_vertices": [1, 8],
        "saddle_edges": [[5, 6], [10, 11]],
    }
    if mechanics != expected:
        raise AssertionError(("fresh mechanics", mechanics))

    incidence, _neighbors, face_by_key = ex.edge_data(faces)
    zero_velocity = {
        label: (Q(0), Q(0), Q(0)) for label in source
    }
    source_owners = owner_rows(affine_path(source, zero_velocity), faces)
    modes = exact_modes(source)
    jets = {
        edge: {"stable": [], "saddle": []} for edge in SADDLES
    }
    for _name, mode in modes:
        owners = owner_rows(affine_path(source, mode), faces)
        for edge in SADDLES:
            for family in ("stable", "saddle"):
                polynomial = owners[edge][family]
                if polynomial.eval(Q(0)) != source_owners[edge][family].eval(Q(0)):
                    raise AssertionError(("source drift", edge, family))
                jets[edge][family].append(
                    polynomial.c[1] if polynomial.degree else Q(0)
                )

    pair_records = {}
    for edge in SADDLES:
        stable_value = source_owners[edge]["stable"].eval(Q(0))
        shared_value = source_owners[edge]["saddle"].eval(Q(0))
        jacobian = jets[edge]["saddle"]
        coefficients, pivot, normalized_gradient_norm = corrected_shared_direction(
            shared_value, jacobian
        )
        velocity = combine_velocity(modes, coefficients, source)
        owners = owner_rows(affine_path(source, velocity), faces)
        target_names = {
            f"face_raw:{BASE_KEY}:{edge}",
            f"edge:{edge}:{source_owners[edge]['beta_name']}",
        }
        rows = primitive_first_jets(source, velocity, faces)
        roots = []
        for name, value, derivative, family in rows:
            if not value:
                raise AssertionError(("zero source primitive", name))
            if derivative and value * derivative < 0:
                root = -value / derivative
                if root > 0:
                    roots.append((root, name, family))
        roots.sort()
        preceding = [
            (root, name, family)
            for root, name, family in roots
            if root < 1 and name not in target_names
        ]
        linearized_target_aliases = [
            (root, name, family)
            for root, name, family in roots
            if name in target_names
        ]
        endpoint_owners = {
            family: owners[edge][family].eval(Q(1))
            for family in ("stable", "saddle")
        }
        packet = {
            modes[index][0]: ex.qs(value)
            for index, value in enumerate(coefficients)
            if value
        }
        complete_order_packet = [
            (ex.qs(root), name, family) for root, name, family in roots
        ]
        family_counts = {}
        for _root, _name, family in preceding:
            family_counts[family] = family_counts.get(family, 0) + 1
        pair_records[str(edge)] = {
            "incident": True,
            "beta_owner": source_owners[edge]["beta_name"],
            "incident_face_keys": [
                list(key) for key in source_owners[edge]["incident_face_keys"]
            ],
            "source_values": {
                "stable": ex.qs(stable_value),
                "shared_saddle": ex.qs(shared_value),
            },
            "source_log10_abs": {
                "stable": math.log10(abs(float(stable_value))),
                "shared_saddle": math.log10(abs(float(shared_value))),
            },
            "exact_shared_owner_count": 1,
            "exact_zero_identity": True,
            "identity_formula": (
                "gram*base_face_raw + ||base_normal||^2*shared_beta*"
                "dot(cross(edge_direction,other_normal),base_normal) == 0"
            ),
            "pivot_mode": modes[pivot][0],
            "normalized_gradient_norm": normalized_gradient_norm,
            "active_mode_count": len(packet),
            "coefficient_digest": canonical_hash(packet),
            "coordinate_linf": max(
                abs(float(component))
                for xyz in velocity.values()
                for component in xyz
            ),
            "linearized_preceding_non_target_count": len(preceding),
            "linearized_preceding_non_target_first_20": [
                {
                    "root": ex.qs(root),
                    "decimal": float(root),
                    "name": name,
                    "family": family,
                }
                for root, name, family in preceding[:20]
            ],
            "linearized_preceding_non_target_names": [
                {"name": name, "family": family, "decimal": float(root)}
                for root, name, family in preceding
            ],
            "linearized_preceding_family_counts": family_counts,
            "complete_linearized_positive_root_count": len(roots),
            "complete_linearized_order_digest": canonical_hash(complete_order_packet),
            "linearized_target_aliases": [
                {
                    "name": name,
                    "family": family,
                    "root": ex.qs(root),
                }
                for root, name, family in linearized_target_aliases
            ],
            "nonlinear_endpoint_target_signs": {
                family: (value > 0) - (value < 0)
                for family, value in endpoint_owners.items()
            },
            "nonlinear_endpoint_target_values": {
                family: ex.qs(value)
                for family, value in endpoint_owners.items()
            },
            "coefficient_packet": packet,
        }

    stable_faces = [tuple(row) for row in mechanics["stable_faces"]]
    saddles = [tuple(row) for row in mechanics["saddle_edges"]]
    pair_matrix = []
    for stable in stable_faces:
        for saddle in saddles:
            pair_matrix.append(
                {
                    "stable_face": list(stable),
                    "saddle_edge": list(saddle),
                    "incident": saddle in clean_ledger["face"][stable],
                    "local_cancellation_owner": (
                        "base-face raw component plus incident edge beta owner"
                        if saddle in clean_ledger["face"][stable]
                        else None
                    ),
                }
            )

    result = {
        "schema": "stable_first_topology_front.stable_pair_diagnosis",
        "schema_version": 1,
        "report_type": "exact_structural_and_first_jet_diagnosis",
        "scope": (
            "Fresh reconstruction from far_u1.csv plus exact death-lineage binding. "
            "Only stable+saddle pairs are targeted; direct rays are diagnostics, "
            "not global obstruction claims."
        ),
        "source_hashes": {
            "far_u1.csv": source_hash,
            "death_certificate.json": certificate_hash,
            "death_verification.json": verification_hash,
            "exact_core.py": sha256(CORE),
            "verify_exact_event_certificate.py": sha256(CLEAN),
        },
        "fresh_hull": hull,
        "fresh_face_hash": clean.face_hash(faces),
        "fresh_support": {
            key: value for key, value in support.items() if key != "edges"
        },
        "fresh_mechanics": mechanics,
        "pair_matrix": pair_matrix,
        "codimension_two_local_owner_facts": {
            "incident_stable_saddle_owner_count": 2,
            "nonincident_pair_count": 2,
            "current_unstable_saddle_incidence_count": 0,
            "direct_222_to_110_local_owner_available": False,
            "stable_first_single_cancellation_expected_class": [1, 2, 1],
            "morse_index_balance": "S+U-H remains 2 under one stable+saddle cancellation",
            "reason": (
                "Each current saddle is incident only to the enlarged base stable face; "
                "neither current unstable vertex is an endpoint of either saddle. A direct "
                "(2,2,2)->(1,1,0) local double cancellation therefore needs a later "
                "ordered carrier transfer or a recharted topology event."
            ),
        },
        "pairs": pair_records,
    }
    full_output = HERE / "stable_pair_diagnosis.json"
    full_output.write_text(json.dumps(result, indent=2) + "\n")
    summary = {
        "source_hashes": result["source_hashes"],
        "fresh_hull": result["fresh_hull"],
        "fresh_face_hash": result["fresh_face_hash"],
        "fresh_class": result["fresh_mechanics"]["class"],
        "pair_matrix": result["pair_matrix"],
        "codimension_two_local_owner_facts": result[
            "codimension_two_local_owner_facts"
        ],
        "pairs": {
            edge: {
                key: value
                for key, value in row.items()
                if key
                in {
                    "beta_owner",
                    "source_log10_abs",
                    "exact_shared_owner_count",
                    "exact_zero_identity",
                    "pivot_mode",
                    "normalized_gradient_norm",
                    "active_mode_count",
                    "coefficient_digest",
                    "coordinate_linf",
                    "linearized_preceding_non_target_count",
                    "linearized_preceding_non_target_first_20",
                    "linearized_preceding_family_counts",
                    "complete_linearized_positive_root_count",
                    "complete_linearized_order_digest",
                    "linearized_target_aliases",
                    "nonlinear_endpoint_target_signs",
                }
            }
            for edge, row in result["pairs"].items()
        },
        "full_output": str(full_output),
        "full_output_sha256": sha256(full_output),
    }
    print(json.dumps(summary, indent=2))


if __name__ == "__main__":
    main()
