"""Finite full-atlas adjacency and convex seed screen for genuine nonsimple unions."""

import os

os.environ["OPENBLAS_NUM_THREADS"] = "1"
os.environ["OMP_NUM_THREADS"] = "1"
from MERGE_CONTACT import *
import argparse


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--generator", type=Path, required=True)
    ap.add_argument("--report", type=Path, required=True)
    ap.add_argument("--out", type=Path, required=True)
    a = ap.parse_args()
    G = json.load(open(a.generator))
    rep = json.load(open(a.report))
    n = G["n_supports"]
    free = [i for i, deps, axes in G["plan"] if i > n and not deps]
    rows = []
    for i, j in itertools.combinations(free, 2):
        if len(set(G["groups"][i - n]) & set(G["groups"][j - n])) != 2:
            continue
        for lam in map(lambda k: F(k, 10), range(11)):
            try:
                GG, nr, changes = merge(G, rep, i, j, lam)
                raw = RECONSTRUCT.recover(GG)
                Q = np.array([[float(F(x, r[-1])) for x in r[:3]] for r in raw["H"]])
                s = FlexibleAtlas(GG, nr, Q)
                v, J, g = s.evaluate(np.zeros(s.n))
                ownmin = float(v[: s.mechlen - 2].min())
                s.forcedp, mp, ch = inherited(rep, s.owners)
                s.last = None
                v, J, g = s.evaluate(np.zeros(s.n))
                row = dict(
                    nodes=[i, j],
                    lam=str(lam),
                    dynamic_mech=ownmin,
                    inherited_primal=float(v[: s.mechlen - 2].min()),
                    slack=float(g["slack"].min()),
                    det=float(g["v6"].min()),
                    groups=changes["parent_groups"],
                )
                rows.append(row)
            except (
                AssertionError,
                ValueError,
                np.linalg.LinAlgError,
                ZeroDivisionError,
            ) as e:
                rows.append(dict(nodes=[i, j], lam=str(lam), error=str(e)))
        a.out.write_bytes(B(rows))
        print("NON_SIMPLE_SCREEN", i, j, len(rows), flush=True)
    good = [r for r in rows if r.get("slack", -1) > 0 and r.get("det", -1) > 0]
    print("CONVEX_INITIAL_SEEDS", len(good))
    print(
        json.dumps(
            sorted(good, key=lambda r: r["inherited_primal"], reverse=True)[:30],
            indent=2,
        ),
        flush=True,
    )


if __name__ == "__main__":
    main()
