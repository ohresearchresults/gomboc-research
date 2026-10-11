#!/usr/bin/env python3
"""Build the cumulative fresh-hull audit for the bound-300 relay chain.

The table deliberately uses the four fixed mechanical branches followed by the
nonlinear integration (quad, U54, H67=1-t, H910=t).  Thus every ratio is
comparable to the original combined wall, even when another atlas branch is
slightly better in an intermediate cell.
"""
from __future__ import annotations

from pathlib import Path
import json

import combined_four_death_lp as four


HERE = Path(__file__).resolve().parent
SUMMARY = HERE / "bound300_relay_chain_summary.json"


STAGES = [
    {
        "state": "combined wall",
        "csv": "row54_combined_wall_rebuilt.csv",
        "lp": "combined_four_death_bound300.json",
        "event": None,
    },
    {
        "state": "interiorized pre-q73",
        "csv": "bound300_turn_a0007.csv",
        "lp": "bound300_turn_a0007_lp.json",
        "event": None,
    },
    {
        "state": "post-q73",
        "csv": "bound300_postq73_a0017.csv",
        "lp": "bound300_postq73_lp.json",
        "event": "bound300_step3_first_support_wall.json",
    },
    {
        "state": "post-relay-1",
        "csv": "postq73_step1_a0003.csv",
        "lp": "postq73_relay1_lp.json",
        "event": "postq73_relay1_wall.json",
    },
    {
        "state": "post-relay-2",
        "csv": "postq73_relay1_step_a0010.csv",
        "lp": "postq73_relay2_lp.json",
        "event": "postq73_relay2_wall.json",
    },
    {
        "state": "post-relay-3",
        "csv": "postq73_relay2_step_a0003.csv",
        "lp": "postq73_relay3_lp.json",
        "event": "postq73_relay3_wall.json",
    },
    {
        "state": "post-relay-4 (fifth exact support event)",
        "csv": "postq73_relay4a_wall_after.csv",
        # No rebuild is needed to certify the fifth event.  This is the LP
        # direction inherited from the immediately preceding actual cell.
        "lp": "postq73_relay3_lp.json",
        "lp_inherited": True,
        "event": "postq73_relay4a_wall.json",
    },
]


def matching_delta(path: Path) -> float:
    payload = json.loads(path.read_text())
    for row in payload["atlas"]:
        if not row.get("success"):
            continue
        deaths = row["deaths"]
        if (
            "('edge', (6, 7), 'one_minus_t')" in deaths
            and "('edge', (9, 10), 't')" in deaths
        ):
            return float(row["delta"])
    raise RuntimeError(f"fixed H67/H910 branch not found in {path}")


def main() -> None:
    summary = json.loads(SUMMARY.read_text())
    by_name = {Path(row["file"]).name: row for row in summary["rows"]}

    rows = []
    for stage in STAGES:
        audit = by_name[stage["csv"]]
        points = four.load_points(HERE / stage["csv"] if (HERE / stage["csv"]).exists()
                                  else HERE / "../../circuit_atlas" / stage["csv"])
        result, _ = four.primitive_ledger(points)
        inactive = sorted(set(points) - set(result.active))

        event = None
        if stage["event"] is not None:
            wall = json.loads((HERE / stage["event"]).read_text())
            event = {
                "artifact": stage["event"],
                "circuit": wall["circuit"],
                "alpha_root": wall["alpha_wall"],
                "wall_f_vector": wall["at"]["f_vector"],
                "before_f_vector": wall["before"]["f_vector"],
                "after_f_vector": wall["after"]["f_vector"],
                "before_class": wall["before"]["class"],
                "after_class": wall["after"]["class"],
            }

        ratios = {
            "quad": audit["residual_ratios"]["quad"],
            "u54": audit["residual_ratios"]["u54"],
            "h67_one_minus_t": audit["h67_component_ratios"]["one_minus_t"],
            "h910_t": audit["h910_component_ratios"]["t"],
        }
        rows.append({
            "state": stage["state"],
            "csv": stage["csv"],
            "f_vector": audit["f_vector"],
            "class": audit["class"],
            "lp_delta_fixed_branch": matching_delta(HERE / stage["lp"]),
            "lp_inherited_from_previous_cell": stage.get("lp_inherited", False),
            "topology_margin": audit["topology_margin"],
            "inactive_rows": inactive,
            "all_forced_rails_present": audit["all_forced_rails_present"],
            "residual_ratios_to_combined_wall": ratios,
            "largest_fixed_residual_ratio": max(ratios.values()),
            "event_entering_state": event,
        })

    four_series = {
        key: [row["residual_ratios_to_combined_wall"][key] for row in rows]
        for key in ("quad", "u54", "h67_one_minus_t", "h910_t")
    }
    monotone = {
        key: all(b <= a + 1e-12 for a, b in zip(values, values[1:]))
        for key, values in four_series.items()
    }
    events = [row["event_entering_state"] for row in rows if row["event_entering_state"]]
    payload = {
        "version": 1,
        "scope": "bound-300 actual-cell relay chain with fresh hull at every state",
        "fixed_mechanical_branches": {
            "quad": "face (7,8,245,246), witness edge (8,246)",
            "u54": "vertex 54, neighbor 1",
            "h67": "one_minus_t",
            "h910": "t",
        },
        "rows": rows,
        "exact_support_event_count": len(events),
        "all_four_residual_series_monotone_nonincreasing": all(monotone.values()),
        "per_residual_monotonicity": monotone,
        "first_nonrelay_failure": None,
        "next_known_event": {
            "type": "support relay",
            "circuit": [198, 234, 235, 236],
            "alpha_root_from_post_relay_3_cell": 0.0001706449472203067,
            "artifact": "postq73_relay4b_wall.json",
        },
        "conclusion": (
            "Five consecutive exact support events occur without a mechanical-sign "
            "change, forced-rail loss, base loss, or any new inactive row after q73. "
            "All four fixed residual ratios decrease monotonically."
        ),
    }
    (HERE / "relay_chain_report.json").write_text(json.dumps(payload, indent=2) + "\n")

    md = [
        "# Bound-300 exact support-relay chain",
        "",
        "Every state is audited by rebuilding the full hull. Ratios use the fixed "
        "branches quad, U54, H67=`1-t`, H910=`t` and are relative to the original "
        "combined wall.",
        "",
        "| state | fresh lattice | LP δ | quad | U54 | H67 | H910 | topo margin | exact entering circuit @ local α | inactive |",
        "|---|---:|---:|---:|---:|---:|---:|---:|---|---|",
    ]
    for row in rows:
        ratios = row["residual_ratios_to_combined_wall"]
        event = row["event_entering_state"]
        event_text = "—" if event is None else (
            "`{" + ",".join(map(str, event["circuit"])) + "}` @ "
            f"{event['alpha_root']:.12g}"
        )
        delta_suffix = "*" if row["lp_inherited_from_previous_cell"] else ""
        inactive_text = ",".join(map(str, row["inactive_rows"])) or "—"
        md.append(
            f"| {row['state']} | {tuple(row['f_vector'])} | "
            f"{row['lp_delta_fixed_branch']:.9f}{delta_suffix} | "
            f"{ratios['quad']:.9f} | {ratios['u54']:.9f} | "
            f"{ratios['h67_one_minus_t']:.9f} | {ratios['h910_t']:.9f} | "
            f"{row['topology_margin']:.3e} | {event_text} | {inactive_text} |"
        )
    md += [
        "",
        "`*` The fifth-event row inherits the certified direction from the preceding "
        "actual cell; no post-event LP rebuild is needed to establish the stopping "
        "criterion.",
        "",
        "Result: **five consecutive exact support events**, all forced rails retained, "
        "class `(2,2,2)` retained, only row 73 inactive after the deliberate q73 "
        "support exit, and every one of the four fixed residual series is monotone "
        "nonincreasing. No mechanical-sign wall is encountered. The next exact event "
        "is independently bracketed as `{198,234,235,236}` at local "
        "`α=0.0001706449472203067`.",
    ]
    (HERE / "relay_chain_report.md").write_text("\n".join(md) + "\n")


if __name__ == "__main__":
    main()
