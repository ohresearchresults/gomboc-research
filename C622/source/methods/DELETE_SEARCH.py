import os

os.environ["OPENBLAS_NUM_THREADS"] = "1"
os.environ["OMP_NUM_THREADS"] = "1"
from flexible import *
from REFINE import warm, correct
import argparse, sys, time, hashlib, platform, scipy

sys.path.insert(0, str(ROOT / "parent"))
import RECONSTRUCT, check_A, check_B

B = lambda x: json.dumps(x, sort_keys=True, separators=(",", ":")).encode()


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("target", type=int)
    ap.add_argument("--warm", type=int, default=1000)
    ap.add_argument("--steps", type=int, default=60)
    ap.add_argument("--out", type=Path, required=True)
    a = ap.parse_args()
    out = a.out
    out.mkdir(parents=True, exist_ok=False)
    G = json.load(open(ROOT / "parent/GENERATOR.json"))
    raw = RECONSTRUCT.recover(G)
    Q = np.array([[float(F(v, r[-1])) for v in r[:3]] for r in raw["H"]])
    GG, change = delete_generator(G, a.target, Q)
    raw["H"].pop(a.target)
    rep = check_B.run(raw)
    (out / "INITIAL_B.json").write_bytes(B(rep))
    (out / "INITIAL_RAW.json").write_bytes(B(raw))
    (out / "CHANGES.json").write_bytes(B(change))
    print(
        "INITIAL_DELETE_B",
        a.target,
        rep["V"],
        rep["E"],
        rep["F"],
        rep["counts"],
        rep["weak"],
        flush=True,
    )
    s = FlexibleAtlas(GG, rep, np.delete(Q, a.target, axis=0), 3 - (a.target < 3))
    s.checkpoint_dir = out
    t = time.time()
    z = np.zeros(s.n)
    (out / "INPUT.json").write_bytes(
        B(
            dict(
                target=a.target,
                warm=a.warm,
                steps=a.steps,
                versions=[platform.python_version(), np.__version__, scipy.__version__],
            )
        )
    )
    if a.warm:
        z = warm(s, a.warm)
        (out / "WARM_Z.json").write_bytes(B([float(x).hex() for x in z]))
    z, records = correct(s, z, a.steps)
    v, J, g = s.evaluate(z)
    GG = copy.deepcopy(s.G)
    GG["grid"] = 10**9
    GG["controls"] = np.rint(g["Y"] * GG["grid"]).astype(np.int64).tolist()
    (out / "GENERATOR.json").write_bytes(B(GG))
    (out / "Z.json").write_bytes(B([float(x).hex() for x in z]))
    (out / "RECORDS.json").write_bytes(B(records))
    status = dict(
        target=a.target,
        merit=float(np.linalg.norm(s.residual(z))),
        mech=float(v[: s.mechlen].min()),
        slack=float(g["slack"].min()),
        det=float(g["v6"].min()),
        time=time.time() - t,
        n=s.n,
        gen_sha=hashlib.sha256(B(GG)).hexdigest(),
    )
    (out / "STATUS.json").write_bytes(B(status))
    print("DELETE_TRIAL_END", json.dumps(status), flush=True)


if __name__ == "__main__":
    main()
