"""Finite screen beyond the old75 triangular-union coordinate slice."""

from ANY_UNION_SCREEN_ORIGINAL import *

ap = argparse.ArgumentParser()
ap.add_argument("--chart", type=Path, required=True)
ap.add_argument("--out", type=Path, required=True)
a = ap.parse_args()
c = Chart(a.chart)
rep = json.load(open(a.chart / "baseline/A.json"))
rows = []
for k, pair in enumerate(c.edges.tolist()):
    if c.w[k] <= 0 or min(len(rep["faces"][q]) for q in pair) <= 3:
        continue
    try:
        s, nr, patch, Q = make(c, rep, pair)
        v, J, g = s.evaluate(np.zeros(s.n))
        dynamic = float(v[: s.mechlen - 2].min())
        s.forcedp, mp, ch = inherited(rep, s.owners)
        s.last = None
        vv, JJ, gg = s.evaluate(np.zeros(s.n))
        row = dict(
            edge=k,
            pair=pair,
            dynamic_mech=dynamic,
            inherited_primal=float(vv[: s.mechlen - 2].min()),
            slack=float(g["slack"].min()),
            det=float(g["v6"].min()),
            weight=float(c.w[k]),
            union=patch["child_group"],
            mech_bad=int(sum(v[: s.mechlen - 2] < 0)),
        )
        rows.append(row)
    except (AssertionError, ValueError, np.linalg.LinAlgError, ZeroDivisionError) as e:
        rows.append(dict(edge=k, pair=pair, error=str(e)))
    a.out.write_bytes(B(rows))
    print("ANY_SCREEN", k, rows[-1], flush=True)
good = [r for r in rows if r.get("slack", -1) > 0 and r.get("det", -1) > 0]
print(
    "FINAL_RANK",
    json.dumps(
        sorted(good, key=lambda r: r["dynamic_mech"], reverse=True)[:20], indent=2
    ),
    flush=True,
)
