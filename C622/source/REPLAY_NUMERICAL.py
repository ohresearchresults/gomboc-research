"""Completed short numerical reconstruction from finite exact checkpoints.
Default: replays the decisive routed correction from the literal C622 own817
checkpoint. --local also regenerates that checkpoint from the exact C624 body.
--first-union additionally regenerates C624 from the assigned exact C626 parent.
A floating output with a different rounded hash is not an accepted replacement.
"""

import os

os.environ["OPENBLAS_NUM_THREADS"] = "1"
os.environ["OMP_NUM_THREADS"] = "1"
import sys, argparse, json, copy, hashlib
from pathlib import Path

ROOT = Path(__file__).resolve().parent
sys.path[:0] = [str(ROOT / "methods"), str(ROOT / "methods/parent")]
from LOCAL_UNION import *
from MERGE_CONTACT import merge
from ROOTED_ROUTING import routing
import RECONSTRUCT, check_B

ROOT = Path(__file__).resolve().parent
B = lambda x: json.dumps(x, sort_keys=True, separators=(",", ":")).encode()


def initial(G, rep):
    raw = RECONSTRUCT.recover(G)
    Q = np.array([[float(F(x, row[-1])) for x in row[:3]] for row in raw["H"]])
    return FlexibleAtlas(G, rep, Q), Q


def write_generator(s, z, name, out, e):
    v, J, g = s.evaluate(z)
    G = copy.deepcopy(s.G)
    G["grid"] = 10**12
    G["controls"] = np.rint(g["Y"] * G["grid"]).astype(np.int64).tolist()
    h = hashlib.sha256(B(G)).hexdigest()
    (out / (name + ".json")).write_bytes(B(G))
    assert (
        h == e["cases"][name]["generator_sha256"]
    ), "Different floating output is not certified"
    print("IDENTICAL_NUMERICAL_GENERATOR", name, h, flush=True)
    return G


def inherited_routes(s, rep, Q):
    s.forcedp, mp, ch = inherited(rep, s.owners)
    g = np.array([float(F(x)) for x in rep["raw_centroid"]])
    sp = arrows(Q / (1 - Q @ g)[:, None]).argmax(1)
    s.forcedq = {i: int(sp[i]) for i in range(s.nq) if i != s.S}
    s.last = None


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--proof", type=Path, required=True)
    ap.add_argument("--out", type=Path, required=True)
    ap.add_argument("--local", action="store_true")
    ap.add_argument("--first-union", action="store_true")
    a = ap.parse_args()
    a.out.mkdir(parents=True, exist_ok=False)
    e = json.loads((ROOT / "EXPECTED.json").read_text())
    if a.first_union:
        G = json.load(open(a.proof / "PARENT/GENERATOR.json"))
        rep = json.load(open(a.proof / "PARENT/A.json"))
        GG, nr, changes = merge(G, rep, 155, 156, F(17, 20))
        s, _ = initial(GG, nr)
        _, Q = initial(G, rep)
        inherited_routes(s, rep, Q)
        z = repair(s, np.zeros(s.n), a.out / "first_union", steps=100, goal=1e-7)
        write_generator(s, z, "C624_NONSIMPLE", a.out, e)
    if a.local:
        c = Chart(a.proof / "C624_NONSIMPLE_CHART")
        rep = json.load(open(a.proof / "C624_NONSIMPLE/A.json"))
        s, nr, patch, Y = make_local(c, rep, [88, 118], F(1))
        inherited_routes(s, rep, c.Q)
        z = repair(s, np.zeros(s.n), a.out / "local", steps=100, goal=1e-7)
        write_generator(s, z, "C622_ROUTING_WARM", a.out, e)
    G = json.load(open(a.proof / "C622_ROUTING_WARM/GENERATOR.json"))
    raw = RECONSTRUCT.recover(G)
    rep = check_B.run(raw)
    assert rep["counts"] == [8, 1, 7] and rep["weak"] == [0, 0, 0]
    s, Q = initial(G, rep)
    v, J, g = s.evaluate(np.zeros(s.n))
    pp, dp = routing(g["X"] - g["g"], s.U, 1, 1e-14)
    qq, dq = routing(g["Q"] / (1 - g["Q"] @ g["g"])[:, None], s.S, 1, 1e-14)
    routes = dict(primal=pp, polar=qq)
    assert B(routes) == (ROOT / "C622_ROUTES.json").read_bytes()
    s.forcedp = pp
    s.forcedq = qq
    s.last = None
    z = repair(s, np.zeros(s.n), a.out / "routing", steps=20, goal=1e-8)
    write_generator(s, z, "C622_ROUTED", a.out, e)
    print("C622_FINITE_INPUT_NUMERICAL_REPLAY_IDENTICAL_PASS", flush=True)


if __name__ == "__main__":
    main()
