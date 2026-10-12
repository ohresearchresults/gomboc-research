import os

os.environ["OPENBLAS_NUM_THREADS"] = "1"
os.environ["OMP_NUM_THREADS"] = "1"
from flexible import *
from SVD_CORRECT import repair
from TREE_REPAIR import tree
import argparse, platform, scipy

sys.path.insert(0, str(ROOT / "parent"))
import RECONSTRUCT, check_B

B = lambda x: json.dumps(x, sort_keys=True, separators=(",", ":")).encode()


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--generator", type=Path, required=True)
    ap.add_argument("--out", type=Path, required=True)
    ap.add_argument("--tree", action="store_true")
    ap.add_argument("--goal", type=float, default=1e-7)
    ap.add_argument("--steps", type=int, default=80)
    a = ap.parse_args()
    a.out.mkdir(parents=True, exist_ok=False)
    G = json.load(open(a.generator))
    raw = RECONSTRUCT.recover(G)
    rep = check_B.run(raw)
    Q = np.array([[float(F(x, r[-1])) for x in r[:3]] for r in raw["H"]])
    (a.out / "SOURCE_GENERATOR.json").write_bytes(B(G))
    (a.out / "SOURCE_B.json").write_bytes(B(rep))
    s = FlexibleAtlas(G, rep, Q)
    v, J, g = s.evaluate(np.zeros(s.n))
    if a.tree:
        Z = g["X"] - g["g"]
        q = g["Q"]
        H = q / (1 - q @ g["g"])[:, None]
        s.forcedp, pp = tree(Z, s.U, a.goal)
        s.forcedq, qq = tree(H, s.S, a.goal)
        (a.out / "WITNESSES.json").write_bytes(
            B(dict(primal=s.forcedp, polar=s.forcedq, stats=[pp, qq]))
        )
        s.last = None
    (a.out / "INPUT.json").write_bytes(
        B(
            dict(
                tree=a.tree,
                goal=a.goal,
                steps=a.steps,
                versions=[platform.python_version(), np.__version__, scipy.__version__],
            )
        )
    )
    print(
        "SVD_INITIAL_EXACT_B",
        rep["V"],
        rep["E"],
        rep["F"],
        rep["counts"],
        rep["weak"],
        flush=True,
    )
    repair(s, np.zeros(s.n), a.out, steps=a.steps, goal=a.goal)


if __name__ == "__main__":
    main()
