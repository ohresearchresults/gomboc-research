"""Recompute the process-analysis aggregates from the selected public records.

Run from any directory with Python 3.11+. No external packages are required.
Use --replay-dir to compare fresh REPLAY.py outputs with the saved case census.
"""
from collections import Counter, defaultdict
from datetime import datetime
from pathlib import Path
import argparse
import hashlib
import json

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
ACCEPTED = {"explicit_accepted_status", "parallel_accepted_exact_report"}


def read(path):
    return json.loads(path.read_text())


def chronology(rows):
    by_time = defaultdict(list)
    for row in rows:
        if row["C"] is not None:
            by_time[datetime.fromisoformat(row["utc"].replace("Z", "+00:00"))].append(row)
    best = None
    records = []
    for time, group in sorted(by_time.items()):
        value = min(row["C"] for row in group)
        if best is None or value < best:
            records.append({"utc": time.isoformat().replace("+00:00", "Z"),
                            "C": value,
                            "ids": sorted(row["id"] for row in group if row["C"] == value)})
            best = value
    return {"rows": len(rows), "strict_record_decreases": len(records) - 1,
            "initial_record": records[0], "final_record": records[-1],
            "records": records}


def analyze(replay_dir=None):
    rows = read(HERE / "construction-records.json")["records"]
    catalog = {row["id"]: row for row in read(ROOT / "catalog/construction-history.json")["entries"]}
    assert len({row["id"] for row in rows}) == len(rows)
    for row in rows:
        original = catalog[row["id"]]
        assert all(row[k] == original[k] for k in ("utc", "V", "E", "F", "C"))
        if row["public_package"]:
            assert (ROOT / row["public_package"]).exists()
    categories = Counter(row["acceptance_category"] for row in rows)
    assert set(categories) == ACCEPTED | {"record_status_omitted", "other_explicit_status"}
    broad = chronology([r for r in rows if r["acceptance_category"] != "other_explicit_status"])
    explicit = chronology([r for r in rows if r["acceptance_category"] in ACCEPTED])

    verification = read(HERE / "verification-cases.json")
    expected = read(ROOT / "C622/source/EXPECTED.json")
    cases = verification["cases"]
    assert {case["id"] for case in cases} == set(expected["cases"])
    for case in cases:
        spec = expected["cases"][case["id"]]
        assert [case[k] for k in ("V", "E", "F")] == spec["VEF"]
        assert case["strict_S_U_H"] == spec["counts"]
        assert case["weak_S_U_H"] == spec["weak"]
        assert case["report_sha256"] == spec["report_sha256"]
        assert case["mechanical_complexity"] == sum(spec["VEF"]) - sum(spec["counts"])
        assert case["meets_target"] == (spec["counts"] == [1, 1, 0] and spec["weak"] == [0, 0, 0])
        if replay_dir:
            reports = [(replay_dir / case["id"] / name).read_bytes() for name in ("A.json", "B.json")]
            assert reports[0] == reports[1]
            assert hashlib.sha256(reports[0]).hexdigest() == case["report_sha256"]
    if replay_dir:
        receipt = read(replay_dir / "RECEIPT.json")
        assert receipt["status"] == verification["terminal_status"]
        assert receipt["invalid_and_weak_fixtures_pass"]

    reports = read(ROOT / "catalog/reports.json")
    branches = read(ROOT / "catalog/branches.json")
    batches = read(HERE / "reported-search-batches.json")["batches"]
    return {
        "units": "Catalog records, grouped decreases of running best C, saved replay cases, and reported numerical starts/solves; none is an overall attempt denominator.",
        "archive": {"report_records": len(reports), "branch_records": len(branches)},
        "construction_records": {"total": len(rows), "status_categories": dict(sorted(categories.items())),
                                 "with_public_package": sum(bool(r["public_package"]) for r in rows)},
        "chronology": broad,
        "explicit_status_sensitivity": explicit,
        "exact_replay": {"saved_cases": len(cases), "reports": 2 * len(cases),
                         "target_class": sum(c["meets_target"] for c in cases),
                         "nonqualifying": sum(not c["meets_target"] for c in cases),
                         "strict_count_distribution": dict(sorted(Counter(",".join(map(str, c["strict_S_U_H"])) for c in cases).items())),
                         "all_weak_counts_zero": all(c["weak_S_U_H"] == [0, 0, 0] for c in cases)},
        "reported_numerical_batches": {"batches": len(batches), "starts_or_solves": sum(b["starts"] for b in batches),
                                       "target_class_results": sum(b["target_class_results"] for b in batches)},
    }


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--replay-dir", type=Path)
    parser.add_argument("--output", type=Path, help="Write JSON here; otherwise print it.")
    args = parser.parse_args()
    result = json.dumps(analyze(args.replay_dir), ensure_ascii=False, indent=2) + "\n"
    if args.output:
        args.output.write_text(result)
    else:
        print(result, end="")
