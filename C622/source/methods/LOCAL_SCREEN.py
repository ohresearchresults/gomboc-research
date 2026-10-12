from LOCAL_UNION import *

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
    for lam in [F(0), F(1, 4), F(1, 2), F(3, 4), F(1)]:
        try:
            s, nr, patch, Y = make_local(c, rep, pair, lam)
            v, J, g = s.evaluate(np.zeros(s.n))
            dm = float(v[: s.mechlen - 2].min())
            s.forcedp, mp, ch = inherited(rep, s.owners)
            s.last = None
            vv, jj, gg = s.evaluate(np.zeros(s.n))
            rows.append(
                dict(
                    pair=pair,
                    lam=str(lam),
                    dynamic_mech=dm,
                    inherited_primal=float(vv[: s.mechlen - 2].min()),
                    slack=float(g["slack"].min()),
                    det=float(g["v6"].min()),
                    union=patch["child_group"],
                )
            )
        except (
            AssertionError,
            ValueError,
            np.linalg.LinAlgError,
            ZeroDivisionError,
        ) as e:
            rows.append(dict(pair=pair, lam=str(lam), error=str(e)))
    a.out.write_bytes(B(rows))
    good = [t for t in rows[-5:] if t.get("slack", -1) > 1e-9 and t.get("det", -1) > 0]
    print(
        "LOCAL_SCREEN",
        k,
        sorted(good, key=lambda t: t["dynamic_mech"], reverse=True)[:1],
        flush=True,
    )
good = [r for r in rows if r.get("slack", -1) > 1e-9 and r.get("det", -1) > 0]
print(
    "FINAL_LOCAL_RANK",
    json.dumps(
        sorted(good, key=lambda r: r["dynamic_mech"], reverse=True)[:25], indent=2
    ),
    flush=True,
)
