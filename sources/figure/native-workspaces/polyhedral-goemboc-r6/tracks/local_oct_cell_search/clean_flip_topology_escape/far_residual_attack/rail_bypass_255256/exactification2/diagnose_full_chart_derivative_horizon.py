#!/usr/bin/env python3
"""Isolate the first exact derivative wall of the full 165D chart velocity.

The first-jet search proves only the seven signs at t=0.  This script uses
left-first exact Bernstein subdivision to isolate the first interval on which
strict positivity cannot hold for each oriented derivative.  It then chooses
a strictly earlier dyadic parameter and proves all seven derivative signs on
that closed interval.  The emitted path definition therefore declares a step
that is actually certified for the subsequent complete material audit.
"""
from __future__ import annotations

import argparse
from fractions import Fraction as Q
from pathlib import Path

import exactification_provenance as provenance


HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[5]
_ROLE_CONTEXT = provenance.activate_role(ROOT, "diagnose")
build = _ROLE_CONTEXT.modules["build_exactification_certificate"]
if build.ROOT != ROOT:
    raise RuntimeError("trusted builder dependency root mismatch")

PARENT_PATH = HERE / "exact_first_jet_full_chart_path.json"
DIAGNOSTIC = HERE / "exact_full_chart_derivative_horizon.json"
CERTIFIED_PATH = HERE / "exact_first_jet_full_chart_certified_path.json"

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--source", default=str(build.SOURCE))
    parser.add_argument("--parent-path", default=str(PARENT_PATH))
    parser.add_argument("--diagnostic", default=str(DIAGNOSTIC))
    parser.add_argument("--certified-path", default=str(CERTIFIED_PATH))
    args = parser.parse_args()

    source_path = provenance.contained_path(
        args.source, base=HERE, root=build.ROOT, context="diagnostic source"
    )
    parent_path = provenance.contained_path(
        args.parent_path, base=HERE, root=build.ROOT, context="first-jet parent"
    )
    diagnostic_path = provenance.contained_path(
        args.diagnostic, base=HERE, root=build.ROOT, context="diagnostic output"
    )
    certified_path = provenance.contained_path(
        args.certified_path, base=HERE, root=build.ROOT, context="certified path output"
    )
    faces_path = provenance.contained_path(
        build.FACES_PATH, base=HERE, root=build.ROOT, context="faces"
    )
    default_source = provenance.contained_path(
        build.DEFAULT_SOURCE, base=HERE, root=build.ROOT, context="default source"
    )
    parent_snapshot = provenance.read_snapshot(parent_path)
    source_snapshot = provenance.read_snapshot(source_path)
    faces_snapshot = provenance.read_snapshot(faces_path)
    trust_snapshots = provenance.trusted_code_snapshots(build.ROOT, "diagnose")
    parent = provenance.parse_json(parent_snapshot)
    dynamic_source = source_path != default_source
    lineage_evidence = None
    lineage = parent.get("source_lineage")
    if dynamic_source and lineage is None:
        raise AssertionError("a nondefault source lacks certified lineage")
    if lineage is not None:
        certificate_path, verification_path = provenance.lineage_paths(
            lineage, root=build.ROOT
        )
        lineage_evidence = provenance.validate_dynamic_lineage(
            root=build.ROOT,
            current_source=source_snapshot,
            certificate_snapshot=provenance.read_snapshot(certificate_path),
            verification_snapshot=provenance.read_snapshot(verification_path),
        )
        if lineage != lineage_evidence.payload:
            raise AssertionError("first-jet dynamic-source lineage mismatch")

    output_paths = [diagnostic_path, certified_path]
    input_paths = [
        source_path,
        parent_path,
        faces_path,
        *(snapshot.path for snapshot in trust_snapshots),
    ]
    input_snapshots = [
        source_snapshot,
        parent_snapshot,
        faces_snapshot,
        *trust_snapshots,
    ]
    if lineage_evidence is not None:
        input_paths.extend(snapshot.path for snapshot in lineage_evidence.snapshots)
        input_snapshots.extend(lineage_evidence.snapshots)
    protected_defaults = []
    if dynamic_source:
        protected_defaults = [
            provenance.contained_path(
                DIAGNOSTIC, base=HERE, root=build.ROOT, context="default diagnostic"
            ),
            provenance.contained_path(
                CERTIFIED_PATH,
                base=HERE,
                root=build.ROOT,
                context="default certified path",
            ),
        ]
    provenance.assert_isolated(
        [*output_paths, *input_paths, *protected_defaults], "derivative diagnostic"
    )
    provenance.assert_snapshots_current(input_snapshots)

    source = provenance.parse_exact_csv(source_snapshot)
    faces = provenance.parse_json(faces_snapshot)
    velocity, _velocity_packet = build.exact_velocity(parent, source)
    path = {
        label: tuple(
            build.ex.P((source[label][axis], velocity[label][axis]))
            for axis in range(3)
        )
        for label in source
    }
    ledger = build.ex.mechanics_primitives(path, faces)
    support_rows = list(build.ex.support_polynomials(path, faces))
    first_jet = build.validate_first_jet_parent(
        parent,
        source_snapshot=source_snapshot,
        faces_snapshot=faces_snapshot,
        path=path,
        ledger=ledger,
        support_rows=support_rows,
    )
    semantics = build.derivative_horizon_semantics(path, ledger, support_rows)
    producer_trust = provenance.expected_trust_packet(build.ROOT, "diagnose")
    diagnostic = build.diagnostic_document(
        parent_path=parent_path,
        parent_snapshot=parent_snapshot,
        source_snapshot=source_snapshot,
        faces_snapshot=faces_snapshot,
        first_jet=first_jet,
        semantics=semantics,
        producer_trust=producer_trust,
    )
    provenance.assert_snapshots_current(input_snapshots)
    diagnostic_snapshot = provenance.atomic_write_json(diagnostic_path, diagnostic)

    safe_step = Q(semantics["certified_safe_step_parameter"])
    certified = build.certified_path_document(
        parent=parent,
        parent_path=parent_path,
        parent_snapshot=parent_snapshot,
        diagnostic_path=diagnostic_path,
        diagnostic_snapshot=diagnostic_snapshot,
        safe_step=safe_step,
        producer_trust=producer_trust,
    )
    certified_snapshot = provenance.atomic_write_json(certified_path, certified)
    provenance.assert_snapshots_current(
        [*input_snapshots, diagnostic_snapshot, certified_snapshot]
    )

    print(diagnostic["verdict"])
    print("first_wall_lower_bound", diagnostic["first_wall_lower_bound"])
    print("certified_safe_step_parameter", diagnostic["certified_safe_step_parameter"])
    print("diagnostic_sha256", diagnostic_snapshot.sha256)
    print("certified_path_sha256", certified_snapshot.sha256)


if __name__ == "__main__":
    main()
