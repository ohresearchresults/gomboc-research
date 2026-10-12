#!/usr/bin/env python3
"""Embed selected public catalog metadata in the standalone research map.

Run from any directory: python3 tools/build_research_map.py [--check]
No exporter, private archive, report body, or third-party package is used.
"""

import argparse
import hashlib
import json
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]
PAGE = ROOT / "docs/research-map.html"
START = "<!-- BEGIN PUBLIC MAP DATA -->"
END = "<!-- END PUBLIC MAP DATA -->"
BRANCH_FIELDS = ("id", "study", "title", "parent", "recorded_status", "reports", "unavailable_report_count")
REPORT_FIELDS = ("id", "study", "date", "title", "path", "evidence")


def require(condition, message):
    if not condition:
        raise ValueError(message)


def load_data():
    sources = {}
    rows = {}
    for name in ("branches", "reports"):
        raw = (ROOT / f"catalog/{name}.json").read_bytes()
        sources[f"catalog/{name}.json"] = hashlib.sha256(raw).hexdigest()
        rows[name] = json.loads(raw)
    branches = [{key: row[key] for key in BRANCH_FIELDS} for row in rows["branches"]]
    reports = [{key: row[key] for key in REPORT_FIELDS} for row in rows["reports"]]
    by_id = {row["id"]: row for row in branches}
    by_report = {row["id"]: row for row in reports}
    require(len(by_id) == len(branches), "Duplicate branch IDs")
    require(len(by_report) == len(reports), "Duplicate report IDs")
    require(bool(branches) and bool(reports), "Empty public catalog")
    for report in reports:
        require(report["study"] in ("figure", "minimum"), "Unknown report study")
        require(re.fullmatch(rf'{report["study"]}-\d{{4}}', report["id"]), "Invalid public report ID")
        require(report["path"] == f'reports/{report["study"]}/{report["id"]}.md', "Unexpected report path")
        require((ROOT / report["path"]).is_file(), f'Missing report file: {report["id"]}')
        require(report["evidence"] == "historical AI scientific report", "Unexpected report evidence class")
        require(re.fullmatch(r"\d{4}-\d{2}-\d{2}", report["date"]), "Invalid report date")
    for branch in branches:
        require(branch["study"] in ("figure", "minimum"), "Unknown branch study")
        require(re.fullmatch(rf'{branch["study"]}-branch-\d{{3}}', branch["id"]), "Invalid public branch ID")
        require(branch["recorded_status"] in ("open", "closed"), "Unknown saved status")
        require(isinstance(branch["title"], str) and branch["title"].strip(), "Empty branch title")
        require(isinstance(branch["unavailable_report_count"], int) and branch["unavailable_report_count"] >= 0, "Invalid unavailable report count")
        require(len(set(branch["reports"])) == len(branch["reports"]), "Duplicate report link within a branch")
        for report_id in branch["reports"]:
            require(report_id in by_report, f"Missing indexed report: {report_id}")
            require(by_report[report_id]["study"] == branch["study"], "Cross-study report link")
        seen = {branch["id"]}
        parent = branch["parent"]
        while parent is not None:
            require(parent in by_id, f"Missing parent: {parent}")
            require(parent not in seen, f"Cycle at {parent}")
            require(by_id[parent]["study"] == branch["study"], "Cross-study parent")
            seen.add(parent)
            parent = by_id[parent]["parent"]
    linked = {report_id for branch in branches for report_id in branch["reports"]}
    stats = {
        "branches": len(branches), "reports": len(reports), "linked_reports": len(linked),
        "report_links": sum(len(branch["reports"]) for branch in branches),
        "unavailable_reports": sum(branch["unavailable_report_count"] for branch in branches),
        "unlinked_reports": [report["id"] for report in reports if report["id"] not in linked],
        "studies": {study: {
            "branches": sum(branch["study"] == study for branch in branches),
            "roots": sum(branch["study"] == study and branch["parent"] is None for branch in branches),
        } for study in ("figure", "minimum")},
    }
    return {"schema_version": 1, "sources_sha256": sources, "stats": stats, "branches": branches, "reports": reports}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true", help="Validate inputs and fail if embedded data is stale; write nothing")
    args = parser.parse_args()
    data = load_data()
    # Keep JSON inert even when a public title contains HTML or script syntax.
    encoded = json.dumps(data, ensure_ascii=False, separators=(",", ":")).replace("<", "\\u003c").replace("&", "\\u0026").replace("\u2028", "\\u2028").replace("\u2029", "\\u2029")
    replacement = f'{START}\n<script id="research-data" type="application/json">{encoded}</script>\n{END}'
    original = PAGE.read_text(encoding="utf-8")
    pattern = re.compile(re.escape(START) + r".*?" + re.escape(END), re.S)
    require(len(pattern.findall(original)) == 1, "Expected exactly one map data block")
    updated = pattern.sub(lambda _: replacement, original)
    if args.check:
        require(original == updated, "Embedded data is stale: run python3 tools/build_research_map.py")
    elif updated != original:
        PAGE.write_text(updated, encoding="utf-8")
    print(json.dumps({"mode": "check" if args.check else "build", **data["stats"]}, indent=2))


if __name__ == "__main__":
    main()
