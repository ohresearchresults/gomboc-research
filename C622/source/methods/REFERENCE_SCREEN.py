"""Reference-centre diagnostic only; no reference110 is called an own-centred result."""

from general_atlas import *
from numeric import Chart
from TREE_REPAIR import arrows
from fractions import Fraction as F

c = Chart()
rep = json.load(open(ROOT / "baseline/A.json"))
oldg = np.array([float(F(x)) for x in rep["raw_centroid"]])
results = []
for row in json.load(open(ROOT / "ELIGIBLE.json")):
    for mode in ["direct", "stress"]:
        try:
            if mode == "stress":
                w = c.w.copy()
                w[row["edge"]] = 0
                Q = c.solve(w)[0]
            else:
                Q = c.Q.copy()
            s = GeneralAtlas(row["edge"], Q)
            v, J, g = s.evaluate(np.zeros(s.n))
            P = g["X"] - oldg
            H = g["Q"] / (1 - g["Q"] @ oldg)[:, None]
            ep = arrows(P).max(1)
            eq = arrows(H).max(1)
            m = min(np.delete(ep, s.U).min(), np.delete(eq, 3).min())
            results.append(
                dict(
                    edge=row["edge"],
                    pair=(
                        row["pair"] if "pair" in row else c.edges[row["edge"]].tolist()
                    ),
                    mode=mode,
                    ref_mech=float(m),
                    own_mech=float(v[: s.mechlen - 2].min()),
                    centroid_shift=float(np.linalg.norm(g["g"] - oldg)),
                    slack=float(g["slack"].min()),
                )
            )
        except Exception as ex:
            results.append(dict(edge=row["edge"], mode=mode, error=str(ex)))
Path("../REFERENCE_SCREEN.json").write_text(
    json.dumps(results, sort_keys=True, separators=(",", ":"))
)
print(
    json.dumps(
        sorted([r for r in results if "ref_mech" in r], key=lambda r: -r["ref_mech"])[
            :20
        ],
        indent=2,
    ),
    flush=True,
)
