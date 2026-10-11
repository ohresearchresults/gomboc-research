#!/usr/bin/env python3
"""Fresh fixed-plane descent proposal in the safe post-flip cell."""
from __future__ import annotations

import hashlib
import json
import sys
from fractions import Fraction as Q
from pathlib import Path
from types import SimpleNamespace

import numpy as np
from scipy.optimize import linprog


HERE = Path(__file__).resolve().parent
MAIN = HERE.parent
ATTACK = MAIN.parents[1]
SOURCE = MAIN / "safe_flip_far.csv"
FACES_PATH = MAIN / "safe_flip_post_faces.json"
SOURCE_CERTIFICATE = MAIN / "safe_flip_certificate.json"
CHART_OUT = HERE / "chart.json"
OUTPUT = HERE / "proposal.json"
ENDPOINT = HERE / "candidate.csv"
EXPECTED_SOURCE_CERTIFICATE_VERDICT = "EXACT_POST_C17_FIXED_PLANE_SAFE_FLIP_PASS"
sys.path.insert(0, str(MAIN))
sys.path.insert(0, str(ATTACK))

import build_full_chart as chart  # noqa: E402
import post_c17_exact as pc  # noqa: E402
import propose_fixed_plane_descent as base  # noqa: E402


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def load_source():
    certificate = json.loads(SOURCE_CERTIFICATE.read_text())
    assert certificate["verdict"] == EXPECTED_SOURCE_CERTIFICATE_VERDICT
    assert sha256(SOURCE) == certificate["generated_file_sha256"][str(SOURCE.relative_to(ATTACK))]
    rows = pc.read_rows(SOURCE)
    cycles = json.loads(FACES_PATH.read_text())
    faces = pc.ex.exactify_faces(
        rows,
        SimpleNamespace(faces=[{"cycle": list(cycle)} for cycle in cycles]),
    )
    volume, centroid = pc.ex.exact_mass(rows, faces)
    ef, active, _fl, _vl, _el, stable, unstable, saddles = pc.ex.exact_mechanics(
        rows, faces, centroid
    )
    packet = {
        "f_vector": [len(active), len(ef), len(faces)],
        "class": [len(stable), len(unstable), len(saddles)],
        "active_vertices": active,
        "stable_faces": [faces[index]["cycle"] for index in stable],
        "unstable_vertices": unstable,
        "saddle_edges": [list(edge) for edge in saddles],
    }
    assert packet["f_vector"] == [61, 150, 91]
    assert packet["class"] == [2, 4, 4]
    assert packet["unstable_vertices"] == [8, 228, 231, 246]
    assert packet["saddle_edges"] == [[8, 246], [228, 254], [231, 247], [236, 237]]
    assert not (pc.esc.forced_rails() - set(ef))
    return packet, rows, faces, volume, centroid


def main():
    packet, rows, faces, volume, centroid = load_source()
    spec, basis = chart.build_spec(rows, tuple(packet["active_vertices"]))
    targets0, base0, u80 = chart.target_jets(rows, faces, spec)
    target_rank = pc.rj.matrix_rank([targets0[name].d for name in chart.TARGET_NAMES])
    assert target_rank == 8
    q, _symbolic_centroid, mechanics = base.mechanics_records(
        rows, faces, packet, spec
    )
    by_id = {record["id"]: record for record in mechanics}
    targets = base.target_ids()
    for name, identifier in targets.items():
        assert by_id[identifier]["value"].v == targets0[name].v
    protected_ids = {
        record["id"]
        for record in mechanics
        if (record["id"][0] == "S" and record["id"][1] == tuple(chart.BASE))
        or (record["id"][0] == "U" and record["id"][1] == 8)
    }
    protected0 = {
        **{("S", tuple(sorted(edge))): value.v for edge, value in base0.items()},
        **{("U8", neighbor): value.v for neighbor, value in u80.items()},
    }
    assert len(protected_ids) == len(protected0) == 30
    support_guards, support_summary = base.support_and_turn_guards(rows, faces, q)
    displacement = base.displacement_matrix(tuple(packet["active_vertices"]), spec)
    target_ids = set(targets.values())

    chart_payload = {
        "version": 1,
        "scope": "fresh exact fixed-plane chart in post-safe-flip cell",
        "source_hashes": {
            str(SOURCE.relative_to(ATTACK)): sha256(SOURCE),
            str(FACES_PATH.relative_to(ATTACK)): sha256(FACES_PATH),
            str(SOURCE_CERTIFICATE.relative_to(ATTACK)): sha256(SOURCE_CERTIFICATE),
        },
        "f_vector": packet["f_vector"],
        "class": packet["class"],
        "mode_count": len(spec),
        "target_rank_exact": target_rank,
        "protected_component_count": len(protected_ids),
        "mode_names": [name for _row, name, _direction in spec],
        "basis_exact": {
            name: [pc.qs(value) for value in vector] for name, vector in basis.items()
        },
        "source_volume_exact": pc.qs(volume),
        "source_centroid_exact": [pc.qs(value) for value in centroid],
        "verdict": "EXACT_POST_SAFE_FLIP_FIXED_PLANE_CHART_PASS",
    }
    CHART_OUT.write_text(json.dumps(chart_payload, indent=2) + "\n")

    branches = []
    best = None
    for trust in (1e-8, 3e-8, 1e-7, 3e-7, 1e-6, 3e-6, 1e-5, 3e-5):
        a_ub = []
        b_ub = []
        for name, identifier in targets.items():
            value = by_id[identifier]["value"]
            a_ub.append(np.r_[np.asarray([float(z / value.v) for z in value.d]), 1.0])
            b_ub.append(0.0)
        for record in mechanics:
            value = record["value"]
            if record["id"] in target_ids:
                continue
            gradient = np.asarray([float(z) for z in value.d])
            if record["id"] in protected_ids:
                a_ub.append(np.r_[-gradient / float(value.v), 0.05])
                b_ub.append(0.0)
            else:
                sign = 1.0 if value.v > 0 else -1.0
                a_ub.append(np.r_[-sign * gradient, 0.0])
                b_ub.append(0.2 * abs(float(value.v)))
        for record in support_guards:
            value = record["value"]
            a_ub.append(np.r_[-np.asarray([float(z) for z in value.d]), 0.0])
            b_ub.append(0.2 * float(value.v))
        a_ub.extend(np.c_[displacement, np.zeros(displacement.shape[0])])
        b_ub.extend(np.full(displacement.shape[0], trust))
        a_ub.extend(np.c_[-displacement, np.zeros(displacement.shape[0])])
        b_ub.extend(np.full(displacement.shape[0], trust))
        lp = linprog(
            np.r_[np.zeros(len(spec)), -1.0],
            A_ub=np.asarray(a_ub),
            b_ub=np.asarray(b_ub),
            bounds=[(None, None)] * len(spec) + [(0.0, 1.0)],
            method="highs",
        )
        branch = {
            "trust": trust,
            "success": bool(lp.success),
            "message": lp.message,
            "constraint_count": len(a_ub),
        }
        if lp.success:
            delta, coefficients = base.exact_delta(
                spec, np.asarray(lp.x[:-1]), packet["active_vertices"]
            )
            branch["common_fractional_descent"] = float(lp.x[-1])
            branch["physical_linf"] = max(
                abs(float(value)) for vector in delta.values() for value in vector
            )
            try:
                evaluated = base.evaluate_exact_candidate(
                    rows, faces, packet, delta, targets0, protected0
                )
                candidate, candidate_packet, ratios, protected, candidate_volume, candidate_centroid = evaluated
                branch["exact_accept"] = True
                branch["target_ratios_decimal"] = {
                    name: float(ratio) for name, ratio in ratios.items()
                }
                if best is None or lp.x[-1] > best[0]["common_fractional_descent"]:
                    best = (
                        branch,
                        candidate,
                        candidate_packet,
                        ratios,
                        protected,
                        candidate_volume,
                        candidate_centroid,
                        coefficients,
                    )
            except Exception as error:
                branch["exact_accept"] = False
                branch["exact_error"] = repr(error)
        branches.append(branch)
    if best is None:
        raise RuntimeError("no exact post-flip descent candidate")
    branch, candidate, candidate_packet, ratios, protected, candidate_volume, candidate_centroid, coefficients = best
    pc.write_rows(ENDPOINT, candidate)
    payload = {
        "version": 1,
        "scope": "rational fixed-plane descent proposal in safe post-flip cell",
        "source_hashes": chart_payload["source_hashes"],
        "chart_sha256": sha256(CHART_OUT),
        "mechanics_guard_count": len(mechanics),
        "support_guard_summary": support_summary,
        "branches": branches,
        "selected_branch": branch,
        "exact_coefficients": [pc.qs(value) for value in coefficients],
        "candidate": {
            "csv": str(ENDPOINT.relative_to(ATTACK)),
            "csv_sha256": sha256(ENDPOINT),
            "f_vector": candidate_packet["f_vector"],
            "class": candidate_packet["class"],
            "volume_exact": pc.qs(candidate_volume),
            "centroid_exact": [pc.qs(value) for value in candidate_centroid],
            "target_ratios_exact": {name: pc.qs(ratio) for name, ratio in ratios.items()},
            "target_ratios_decimal": {name: float(ratio) for name, ratio in ratios.items()},
            "protected_component_count": len(protected),
            "all_37_forced_rails_present": True,
        },
        "verdict": "RATIONAL_POST_SAFE_FLIP_DESCENT_PROPOSAL_PASS",
        "proof_status": "EXACT_ENDPOINT_ONLY_FIRST_EVENT_NOT_YET_CERTIFIED",
        "winner_status": "NONWINNER",
    }
    OUTPUT.write_text(json.dumps(payload, indent=2) + "\n")
    print(payload["verdict"])
    print("target_ratios", payload["candidate"]["target_ratios_decimal"])
    print("candidate_sha256", sha256(ENDPOINT))
    print("proposal_sha256", sha256(OUTPUT))


if __name__ == "__main__":
    main()
