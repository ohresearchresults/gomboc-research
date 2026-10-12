import json, hashlib, sys
from pathlib import Path
import chart
from check_A import encode

root = Path(sys.argv[1])
base = root / "baseline"
base.mkdir(exist_ok=False)
for src, dst in [("raw.json", "raw.json"), ("B.json", "A.json")]:
    (base / dst).write_bytes((root / src).read_bytes())
(base / "PROVENANCE.txt").write_text(
    "The canonical A.json-format report in this numerical helper directory was emitted by completed exact auditor B, not a new execution of auditor A.\n"
)
d = chart.recover(root=root)
out = json.dumps(encode(d), sort_keys=True, separators=(",", ":")).encode()
(root / "chart_exact.json").write_bytes(out)
print(
    "S8_EXACT_FAITHFUL_CHART",
    len(out),
    hashlib.sha256(out).hexdigest(),
    len(d["edges"]),
    d["outer"],
    d["boundary"],
)
