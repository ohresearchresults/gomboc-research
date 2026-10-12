"""Reconstruct both exact audits and the faithful maximal-complex stress chart."""

import argparse, json, sys, hashlib
from pathlib import Path
import chart
from check_A import encode

sys.path.insert(0, str(Path(__file__).parent / "parent"))
import RECONSTRUCT, check_A, check_B

B = lambda x: json.dumps(x, sort_keys=True, separators=(",", ":")).encode()
ap = argparse.ArgumentParser()
ap.add_argument("generator", type=Path)
ap.add_argument("--out", type=Path, required=True)
a = ap.parse_args()
a.out.mkdir(parents=True, exist_ok=False)
base = a.out / "baseline"
base.mkdir()
raw = RECONSTRUCT.recover(json.loads(a.generator.read_text()))
A = check_A.run(raw)
BB = check_B.run(raw)
assert B(A) == B(BB)
for n, x in [("raw", raw), ("A", A), ("B", BB)]:
    (base / (n + ".json")).write_bytes(B(x))
d = chart.recover(root=a.out)
b = B(encode(d))
(a.out / "chart_exact.json").write_bytes(b)
print(
    "EXACT_MAXIMAL_STRESS_CHART",
    len(b),
    hashlib.sha256(b).hexdigest(),
    len(d["edges"]),
    d["outer"],
    d["boundary"],
    flush=True,
)
