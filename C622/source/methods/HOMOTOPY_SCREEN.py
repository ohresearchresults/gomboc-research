import os, sys

os.environ["OPENBLAS_NUM_THREADS"] = "1"
os.environ["OMP_NUM_THREADS"] = "1"
sys.set_int_max_str_digits(0)
import numpy as np, json
from fractions import Fraction as F
from pathlib import Path

root = Path(__file__).parent
r = json.load(open(root / "baseline/A.json"))
X = np.array([[float(F(t)) for t in row] for row in r["raw_vertices"]])
g = np.array([float(F(t)) for t in r["raw_centroid"]])
Z = X - g
e = Z[None] - Z[:, None]
den = np.sqrt((Z * Z).sum(1)[:, None] * (e * e).sum(2))
vals = np.einsum("ik,ijk->ij", Z, e) / np.maximum(den, 1e-50)
np.fill_diagonal(vals, -np.inf)
raw = json.load(open(root / "baseline/raw.json"))["H"]
Q = np.array([[float(F(t, row[-1])) for t in row[:3]] for row in raw])
owners = [[f for f, cy in enumerate(r["faces"]) if v in cy] for v in range(r["V"])]
out = []
for c in json.load(open(root / "ELIGIBLE.json")):
    u, v = c["panels"]
    aa = vals[u].copy()
    bb = vals[v].copy()
    aa[v] = -np.inf
    bb[u] = -np.inf
    k = next(i for i in owners[v] if i not in owners[u])
    l = next(i for i in owners[u] if i not in owners[v])
    gap = 1 - Q[k] @ X[u]
    out.append(
        dict(
            **c,
            blockedmin=float(min(aa.max(), bb.max())),
            external=[int(aa.argmax()), int(bb.argmax())],
            length=float(np.linalg.norm(X[u] - X[v])),
            gap=float(gap),
            third=[l, k]
        )
    )
(root / "HOMOTOPY_CANDIDATES.json").write_text(json.dumps(out))
print("both_external", sum(c["blockedmin"] > 0 for c in out), "of", len(out))
for c in sorted([c for c in out if c["blockedmin"] > 0], key=lambda c: c["length"]):
    print(c)
