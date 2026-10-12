"""Install verified parent data for the literal numerical continuation methods."""

from pathlib import Path
import sys, shutil, json

root = Path(__file__).resolve().parent
proof = Path(sys.argv[1])
methods = root / "methods"
base = methods / "baseline"
base.mkdir(exist_ok=True)
for name in ["A.json", "B.json", "raw.json"]:
    shutil.copyfile(proof / "PARENT" / name, base / name)
shutil.copyfile(proof / "PARENT/GENERATOR.json", methods / "parent/GENERATOR.json")
shutil.copyfile(proof / "chart_exact.json", methods / "chart_exact.json")
# Rebuild the original prepared75-list directly from the actual parent chart.
sys.path[:0] = [str(methods), str(methods / "parent")]
import chart

D = chart.recover(root=methods)
G = json.loads((methods / "parent/GENERATOR.json").read_text())
rep = json.loads((base / "A.json").read_text())
deps = {i: d for i, d, a in G["plan"]}
used = {j for i, d, a in G["plan"] for j in d}
rootvertex = rep["unstable_vertices"][0]
eligible = []
for e, (i, j) in enumerate(D["edges"]):
    panels = [f for f, cy in enumerate(D["faces"]) if i in cy and j in cy]
    if (
        len(panels) == 2
        and D["outer"] not in panels
        and min(len(rep["faces"][k]) for k in (i, j)) >= 4
        and rootvertex not in panels
        and all(len(D["faces"][f]) == 3 for f in panels)
        and any(not deps[k] and k not in used for k in (i, j))
    ):
        eligible.append(dict(edge=e, pair=[i, j], panels=panels))
assert len(eligible) == 75
(methods / "ELIGIBLE.json").write_text(
    json.dumps(eligible, sort_keys=True, separators=(",", ":"))
)
print("PARENT_METHODS_PREPARED", len(eligible))
