"""Ranking only; actual exact acceptance is not inferred from hull tolerances."""

from numeric import *
import sys, hashlib

ROOT = Path(__file__).resolve().parent
sys.path.insert(0, str(ROOT / "parent"))
import RECONSTRUCT
from TREE_REPAIR import arrows

D = Path(sys.argv[1])
G = json.loads((D / "SOURCE_GENERATOR.json").read_text())
raw = RECONSTRUCT.recover(G)
Q = np.array([[float(Fraction(x, row[-1])) for x in row[:3]] for row in raw["H"]])
out = []
for row in json.loads((D / "RESULTS.json").read_text()):
    if row.get("counts") not in ([1, 2, 1], [2, 1, 1]):
        continue
    f = row["deleted_input"]
    q = np.delete(Q, f, 0)
    hu = ConvexHull(q)
    XX = -hu.equations[:, :3] / hu.equations[:, 3, None]
    X = []
    for p in XX:
        if not any(np.linalg.norm(p - x) < 1e-9 for x in X):
            X.append(p)
    X = np.array(X)
    g = np.array(row["centroid"])
    ep = arrows(X - g).max(1)
    eq = arrows(q / (1 - q @ g)[:, None]).max(1)
    root = np.argmin(np.linalg.norm(X - [0, 0, 1], axis=1))
    ep[root] = np.inf
    eq[3 - (f < 3)] = np.inf
    out.append(
        dict(
            deleted=f,
            counts=row["counts"],
            E=row["E"],
            primal=float(ep.min()),
            polar=float(eq.min()),
            sum_deficit=float(
                np.sum(np.minimum(ep, 0) ** 2) + np.sum(np.minimum(eq, 0) ** 2)
            ),
            bad_owners=[
                np.where(abs(q @ X[i] - 1) < 1e-9)[0].tolist()
                for i in np.where(ep < 0)[0]
            ],
        )
    )
out.sort(key=lambda d: d["sum_deficit"])
(D / "RANK.json").write_text(json.dumps(out, sort_keys=True, separators=(",", ":")))
print(json.dumps(out, indent=2))
