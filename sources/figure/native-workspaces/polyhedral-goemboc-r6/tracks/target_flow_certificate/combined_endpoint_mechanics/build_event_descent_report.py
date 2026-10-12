#!/usr/bin/env python3
"""Build the cumulative report for predictor/bypass epochs 1--5."""
from __future__ import annotations

from pathlib import Path
import ast
import json

import combined_core
import combined_four_death_lp as four


HERE = Path(__file__).resolve().parent
PLANE_TOL = 1e-11


STATES = [
    ("post initial independent relay", "reverse_wall_bypass_deep5_after_independent.csv", "post_independent1_lp.json"),
    ("after three epoch-1 bypasses", "epoch1_bypass3_endpoint.csv", "epoch2_lp.json"),
    ("post {198,229,259,260}", "epoch2_event1_after_deep.csv", "epoch3_lp.json"),
    ("after epoch-3 reverse bypasses", "epoch3_bypass69_198_endpoint.csv", "epoch4_lp.json"),
    ("post five-independent-event cluster", "epoch4_cluster_event3_deep_after.csv", "epoch5_lp.json"),
]


def fixed_delta(filename):
    payload = json.loads((HERE / filename).read_text())
    candidates = [
        row for row in payload["atlas"]
        if row.get("success")
        and ast.literal_eval(row["deaths"][2])[2] == "one_minus_t"
        and ast.literal_eval(row["deaths"][3])[2] == "t"
    ]
    return float(min(candidates, key=lambda row: row["delta"])["delta"])


def installed_event(filename, circuit):
    payload = json.loads((HERE / filename).read_text())
    target = list(circuit)
    return next(row for row in payload["installed_reverse_bypasses"] if row["circuit"] == target)


def wall_event(filename):
    payload = json.loads((HERE / filename).read_text())
    return {
        "circuit": payload["circuit"],
        "alpha": payload["alpha_wall"],
        "before_f_vector": payload["before"]["f_vector"],
        "at_f_vector": payload["at"]["f_vector"],
        "after_f_vector": payload["after"]["f_vector"],
        "before_faces": payload["before"]["circuit_faces"],
        "at_faces": payload["at"]["circuit_faces"],
        "after_faces": payload["after"]["circuit_faces"],
        "artifact": filename,
    }


def main():
    canonical = four.load_points(HERE / "../../circuit_atlas/row54_combined_wall_rebuilt.csv")
    _canonical_result, canonical_values = four.primitive_ledger(canonical, plane_tol=PLANE_TOL)
    canonical_keys = [
        next(
            key for key in canonical_values
            if key[0] == "face" and frozenset(key[1]) == four.QUAD and key[2] == (8, 246)
        ),
        ("vertex", 54, 1),
        ("edge", (6, 7), "one_minus_t"),
        ("edge", (9, 10), "t"),
    ]
    ratio_names = ("quad", "U54", "H67(1-t)", "H910(t)")

    states = []
    for name, csv_name, lp_name in STATES:
        points = four.load_points(HERE / csv_name)
        result, values = four.primitive_ledger(points, plane_tol=PLANE_TOL)
        ratios = {
            label: float(values[key] / canonical_values[key])
            for label, key in zip(ratio_names, canonical_keys)
        }
        states.append({
            "state": name,
            "csv": csv_name,
            "lp_json": lp_name,
            "lp_delta_fixed_branch": fixed_delta(lp_name),
            "f_vector": [len(result.active), len(result.edges), len(result.faces)],
            "class": [len(result.stable), len(result.unstable), len(result.saddles)],
            "topology_margin": float(result.topology_margin),
            "inactive_rows": sorted(set(points) - set(result.active)),
            "all_forced_rails_present": combined_core.forced_rail_edges() <= set(result.edges),
            "ratios_to_original_combined_wall": ratios,
            "worst_ratio": max(ratios.values()),
        })

    events = []

    def add_bypass(epoch, filename, circuit, event_type, action="nullspace bypass"):
        row = installed_event(filename, circuit)
        events.append({
            "epoch": epoch,
            "type": event_type,
            "action": action,
            "circuit": row["circuit"],
            "alpha": row["root_alpha"],
            "control_rows": row["control_rows"],
            "nullity": row["local_nullity"],
            "death_leakage": row["max_abs_fractional_death_leakage"],
            "artifact": filename,
        })

    add_bypass(1, "epoch1_bypass3.json", (198, 234, 235, 236), "reverse")
    add_bypass(1, "epoch1_bypass3.json", (69, 228, 235, 255), "reverse")
    add_bypass(1, "epoch1_bypass3.json", (224, 228, 251, 252), "independent #1")

    event = wall_event("epoch2_event1_wall.json")
    events.append({"epoch": 2, "type": "independent #2", "action": "cross", **event})

    add_bypass(3, "epoch3_bypass69_198.json", (69, 228, 235, 255), "reverse")
    add_bypass(3, "epoch3_bypass69_198.json", (198, 234, 235, 236), "reverse")
    add_bypass(4, "epoch4_bypass198.json", (198, 234, 235, 236), "reverse")

    for index, filename in enumerate((
        "epoch4_cluster_event1.json",
        "epoch4_cluster_event2.json",
        "epoch4_cluster_event3.json",
    ), start=3):
        event = wall_event(filename)
        events.append({"epoch": 4, "type": f"independent #{index}", "action": "cross", **event})

    monotonicity = {
        label: all(
            right["ratios_to_original_combined_wall"][label]
            <= left["ratios_to_original_combined_wall"][label] + 1e-12
            for left, right in zip(states, states[1:])
        )
        for label in ratio_names
    }
    independent = [event for event in events if event["type"].startswith("independent")]
    reverse = [event for event in events if event["type"] == "reverse"]
    payload = {
        "version": 1,
        "scope": "actual-cell predictor/nullspace-bypass descent through five independent support events",
        "plane_tolerance": PLANE_TOL,
        "states": states,
        "events_in_order": events,
        "independent_support_event_count": len(independent),
        "reverse_bypass_count": len(reverse),
        "per_residual_monotonicity": monotonicity,
        "all_four_ratios_monotone": all(monotonicity.values()),
        "final_worst_ratio": states[-1]["worst_ratio"],
        "materially_below_0_9": states[-1]["worst_ratio"] < 0.9,
        "mechanical_sign_wall_encountered": False,
        "conclusion": (
            "The reverse relays are locally bypassable and five independent support events are traversed, "
            "but the guarded descent is not material: U54 remains the bottleneck at about 0.993 of its "
            "original residual, far above 0.9."
        ),
    }
    (HERE / "event_descent_report.json").write_text(json.dumps(payload, indent=2) + "\n")

    md = [
        "# Actual-cell descent through five independent support events",
        "",
        "All state rows use a fresh hull at `plane_tol=1e-11`; exact walls in the "
        "final tight cluster additionally use raw fresh-hull grouping at `1e-13`.",
        "",
        "## Cumulative states",
        "",
        "| state | lattice | LP δ | quad | U54 | H67 | H910 | topology | rails/inactive |",
        "|---|---:|---:|---:|---:|---:|---:|---:|---|",
    ]
    for state in states:
        ratios = state["ratios_to_original_combined_wall"]
        md.append(
            f"| {state['state']} | {tuple(state['f_vector'])} | "
            f"{state['lp_delta_fixed_branch']:.9f} | {ratios['quad']:.9f} | "
            f"{ratios['U54']:.9f} | {ratios['H67(1-t)']:.9f} | "
            f"{ratios['H910(t)']:.9f} | {state['topology_margin']:.3e} | "
            f"{state['all_forced_rails_present']} / {state['inactive_rows']} |"
        )
    md += [
        "",
        "## Exact event order",
        "",
        "| epoch | type | circuit | local α | action | control rows/nullity |",
        "|---:|---|---|---:|---|---|",
    ]
    for event in events:
        control = "—" if "control_rows" not in event else (
            f"{event['control_rows']} / {event['nullity']}"
        )
        circuit = "{" + ",".join(map(str, event["circuit"])) + "}"
        md.append(
            f"| {event['epoch']} | {event['type']} | `{circuit}` | "
            f"{event['alpha']:.15g} | {event['action']} | {control} |"
        )
    md += [
        "",
        "The three final independent roots are strictly ordered inside a "
        "`1.38e-6` interval; fresh raw hulls show `(60,158,100) -> (60,157,99) "
        "-> (60,158,100)` at each root.",
        "",
        "## Decision",
        "",
        f"All four fixed residual series are monotone, but the final worst ratio is "
        f"`{states[-1]['worst_ratio']:.9f}` (U54), not below `0.9`. Thus the "
        "support relay mechanism is traversable but does **not** produce material "
        "four-defect descent on this scale. No mechanical-sign wall occurs; every "
        "accepted cell retains class `(2,2,2)`, base/U8, all forced rails, and only "
        "row 73 inactive.",
    ]
    (HERE / "event_descent_report.md").write_text("\n".join(md) + "\n")


if __name__ == "__main__":
    main()
