"""Local physical-edge contraction seed in the full recharted contact atlas.
Unlike a frozen support-triple projection, the new contact point is initialized
at a prescribed affine combination of the two actual physical endpoints. All
incident support equations are then solved in the acyclic full-contact plan.
"""

import os

os.environ["OPENBLAS_NUM_THREADS"] = "1"
os.environ["OMP_NUM_THREADS"] = "1"
from ANY_UNION import *


def make_local(c, rep, pair, lam):
    nr, owners, patch = quotient(rep, pair)
    root = next(
        v for v, row in enumerate(rep["raw_vertices"]) if list(map(F, row)) == [0, 0, 1]
    )
    anchorowners = [i for i, cy in enumerate(rep["faces"]) if root in cy]
    assert set(anchorowners) != set(patch["child_group"])
    G, Q = atlas_generator(owners, c.Q.copy(), anchorowners)
    s = FlexibleAtlas(G, nr, Q)
    X = np.array([[float(F(x)) for x in row] for row in rep["raw_vertices"]])
    oldowners = [
        [i for i, cy in enumerate(rep["faces"]) if v in cy] for v in range(rep["V"])
    ]
    u, v = patch["parent_vertex_indices"]
    union = patch["child_group"]
    points = []
    for gr in G["groups"]:
        if gr == union:
            points.append((1 - float(lam)) * X[u] + float(lam) * X[v])
        else:
            points.append(X[oldowners.index(gr)])
    Y = np.vstack((c.Q, points))
    G["controls"] = np.rint(Y * G["grid"]).astype(np.int64).tolist()
    s.G = G
    s.base = np.array([Y[i, a] for i, a in s.free])
    s.scale = np.ones(s.n)
    s.last = None
    s.tscale = np.ones(len(s.tris))
    vv, JJ, gg = s.evaluate(np.zeros(s.n))
    s.scale = 1 / np.maximum(1.0, np.linalg.norm(gg["DQ"].reshape(-1, s.n), axis=0))
    s.tscale = np.maximum(abs(gg["v6"]), 1e-10)
    s.last = None
    patch["lam"] = str(lam)
    return s, nr, patch, Y


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--chart", type=Path, required=True)
    ap.add_argument("--pair", nargs=2, type=int, required=True)
    ap.add_argument("--lam", default="1/2")
    ap.add_argument("--steps", type=int, default=100)
    ap.add_argument("--goal", type=float, default=1e-7)
    ap.add_argument("--dynamic", action="store_true")
    ap.add_argument("--out", type=Path, required=True)
    a = ap.parse_args()
    a.out.mkdir(parents=True, exist_ok=False)
    c = Chart(a.chart)
    rep = json.load(open(a.chart / "baseline/A.json"))
    s, nr, patch, Y = make_local(c, rep, sorted(a.pair), F(a.lam))
    if not a.dynamic:
        s.forcedp, mp, ch = inherited(rep, s.owners)
        g = np.array([float(F(x)) for x in rep["raw_centroid"]])
        aq = arrows(c.Q / (1 - c.Q @ g)[:, None])
        sp = aq.argmax(1)
        s.forcedq = {i: int(sp[i]) for i in range(s.nq) if i != s.S}
        (a.out / "WITNESSES.json").write_bytes(
            B(dict(primal=s.forcedp, polar=s.forcedq, mapping=mp))
        )
    s.last = None
    (a.out / "INITIAL_GENERATOR.json").write_bytes(B(s.G))
    (a.out / "NOMINAL_COMPLEX.json").write_bytes(B(nr))
    (a.out / "PATCH.json").write_bytes(B(patch))
    (a.out / "INITIAL_Y_HEX.json").write_bytes(
        B([[float(x).hex() for x in row] for row in Y])
    )
    (a.out / "INPUT.json").write_bytes(
        B(
            dict(
                pair=a.pair,
                lam=a.lam,
                steps=a.steps,
                goal=a.goal,
                dynamic=a.dynamic,
                versions=[platform.python_version(), np.__version__, scipy.__version__],
            )
        )
    )
    repair(s, np.zeros(s.n), a.out, steps=a.steps, goal=a.goal)


if __name__ == "__main__":
    main()
