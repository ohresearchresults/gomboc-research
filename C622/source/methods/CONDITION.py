"""Recondition all nonroot escapes at the actual filled centroid in the full parent atlas."""

import os

os.environ["OPENBLAS_NUM_THREADS"] = "1"
os.environ["OMP_NUM_THREADS"] = "1"
from flexible import *
from numeric import Chart
from REFINE import lp_l1
import qp, argparse, hashlib, time, platform, scipy

B = lambda x: json.dumps(x, sort_keys=True, separators=(",", ":")).encode()


def project(s, z0, steps=60):
    z = z0.copy()
    trust = 0.03
    qbound = 0.004
    history = []
    for it in range(steps):
        v, J, g = s.evaluate(z)
        merit = float(np.linalg.norm(s.residual(z)))
        r = dict(
            it=it,
            merit=merit,
            minimum=float(v[: s.mechlen - 2].min()),
            slack=float(g["slack"].min()),
            trust=trust,
        )
        history.append(r)
        if np.min(v - s.floor) > -1e-12 and np.min(1 - g["Q"] @ g["X"].T) > -1e-11:
            return z, True, history
        JQ = g["DY"][: s.nq].reshape(-1, s.n)
        A = np.vstack((J / s.rescale[:, None], JQ))
        lo = np.r_[(s.floor * 1.02 - v) / s.rescale, np.full(3 * s.nq, -qbound)]
        hi = np.r_[np.full(len(v), np.inf), np.full(3 * s.nq, qbound)]
        dz, err = qp.solve(
            A,
            lo,
            hi,
            np.full(s.n, -trust),
            np.full(s.n, trust),
            np.ones(s.n),
            tol=1e-10,
        )
        if dz is None:
            dz, err = lp_l1(
                A, lo, hi, np.full(s.n, -trust), np.full(s.n, trust), np.ones(s.n)
            )
        if dz is None:
            r["error"] = err
            trust = min(1.0, trust * 1.5)
            qbound = min(0.08, qbound * 1.5)
            if it > 4 and all("error" in x for x in history[-4:]):
                break
            continue
        good = False
        for alpha in [
            1.0,
            0.5,
            0.25,
            0.125,
            0.0625,
            0.03125,
            0.015625,
            0.0078125,
            0.00390625,
        ]:
            zz = z + alpha * dz
            value = float(np.linalg.norm(s.residual(zz)))
            if np.isfinite(value) and (value < merit * (1 - 1e-5) or value < 1e-9):
                z = zz
                good = True
                break
        r["alpha"] = alpha
        r["accepted"] = good
        if not good:
            trust *= 0.5
            qbound *= 0.5
        if trust < 1e-8:
            break
    return z, False, history


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--out", type=Path, required=True)
    ap.add_argument("--stages", type=int, default=25)
    ap.add_argument("--factor", type=float, default=1.6)
    a = ap.parse_args()
    out = a.out
    out.mkdir(parents=True, exist_ok=False)
    c = Chart()
    G = json.load(open(ROOT / "parent/GENERATOR.json"))
    rep = json.load(open(ROOT / "baseline/A.json"))
    s = FlexibleAtlas(G, rep, c.Q)
    z = np.zeros(s.n)
    v, J, g = s.evaluate(z)
    target = float(v[: s.mechlen - 2].min())
    factor = a.factor
    records = []
    t = time.time()
    (out / "INPUT.json").write_bytes(
        B(
            dict(
                stages=a.stages,
                factor=a.factor,
                versions=[platform.python_version(), np.__version__, scipy.__version__],
            )
        )
    )
    for stage in range(a.stages):
        nexttarget = target * factor
        s.floor[: s.mechlen - 2] = nexttarget
        print("CONDITION_STAGE", stage, "target", nexttarget, flush=True)
        zz, ok, history = project(s, z)
        records.append(dict(stage=stage, target=nexttarget, success=ok, inner=history))
        (out / "RECORDS.json").write_bytes(B(records))
        print(
            "CONDITION_RESULT",
            stage,
            ok,
            "steps",
            len(history),
            "last",
            history[-1],
            flush=True,
        )
        if ok:
            z = zz
            target = nexttarget
            v, J, g = s.evaluate(z)
            GG = copy.deepcopy(G)
            GG["grid"] = 10**9
            GG["controls"] = np.rint(g["Y"] * GG["grid"]).astype(np.int64).tolist()
            (out / "GENERATOR.json").write_bytes(B(GG))
            (out / "Z.json").write_bytes(B([float(x).hex() for x in z]))
            (out / "Q_HEX.json").write_bytes(
                B([[float(x).hex() for x in row] for row in g["Q"]])
            )
        else:
            factor = 1 + (factor - 1) * 0.5
        if factor < 1.005:
            break
    (out / "STATUS.json").write_bytes(
        B(
            dict(
                target=target,
                mech=float(s.evaluate(z)[0][: s.mechlen - 2].min()),
                stages=len(records),
                time=time.time() - t,
            )
        )
    )
    print("CONDITION_END_NUMERICAL_ONLY", target, flush=True)


if __name__ == "__main__":
    main()
