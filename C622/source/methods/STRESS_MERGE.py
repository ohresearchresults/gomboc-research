"""Nonsimple panel identification initialized by its actual maximal stress chart."""

import os

os.environ["OPENBLAS_NUM_THREADS"] = "1"
os.environ["OMP_NUM_THREADS"] = "1"
from MERGE_CONTACT import *
from numeric import Chart


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--generator", type=Path, required=True)
    ap.add_argument("--chart", type=Path, required=True)
    ap.add_argument("--nodes", type=int, nargs=2, required=True)
    ap.add_argument("--steps", type=int, default=120)
    ap.add_argument("--goal", type=float, default=1e-7)
    ap.add_argument("--dynamic", action="store_true")
    ap.add_argument("--out", type=Path, required=True)
    a = ap.parse_args()
    a.out.mkdir(parents=True, exist_ok=False)
    G = json.load(open(a.generator))
    rep = json.load(open(a.chart / "baseline/A.json"))
    GG, nr, changes = merge(G, rep, *a.nodes)
    c = Chart(a.chart)
    pair = sorted(set(changes["parent_groups"][0]) & set(changes["parent_groups"][1]))
    edge = next(i for i, p in enumerate(c.edges) if list(p) == pair)
    weights = c.w.copy()
    weights[edge] = 0
    from RELIFT import seed

    Q, relift = seed(c, weights)
    (a.out / "RELIFT.json").write_bytes(B(relift))
    s = FlexibleAtlas(GG, nr, Q)
    if not a.dynamic:
        s.forcedp, mp, ch = inherited(rep, s.owners)
        g = np.array([float(F(x)) for x in rep["raw_centroid"]])
        aq = arrows(c.Q / (1 - c.Q @ g)[:, None])
        sp = np.argmax(aq, axis=1)
        s.forcedq = {i: int(sp[i]) for i in range(s.nq) if i != s.S}
        (a.out / "WITNESSES.json").write_bytes(
            B(dict(primal=s.forcedp, polar=s.forcedq))
        )
    s.last = None
    (a.out / "SOURCE_GENERATOR.json").write_bytes(B(G))
    (a.out / "INITIAL_GENERATOR.json").write_bytes(B(GG))
    (a.out / "NOMINAL_COMPLEX.json").write_bytes(B(nr))
    (a.out / "CHANGES.json").write_bytes(B(changes))
    (a.out / "INITIAL_Q_HEX.json").write_bytes(
        B([[float(x).hex() for x in row] for row in Q])
    )
    (a.out / "INPUT.json").write_bytes(
        B(
            dict(
                nodes=a.nodes,
                pair=pair,
                edge=edge,
                steps=a.steps,
                goal=a.goal,
                dynamic=a.dynamic,
                versions=[platform.python_version(), np.__version__, scipy.__version__],
            )
        )
    )
    print("STRESS_MERGE_START", pair, edge, flush=True)
    repair(s, np.zeros(s.n), a.out, steps=a.steps, goal=a.goal)


if __name__ == "__main__":
    main()
