"""Finite own-mass retraction at successively smaller actual panel gaps.
Only completed convex stage endpoints have an actual filled-mass interpretation.
"""

import os

os.environ["OPENBLAS_NUM_THREADS"] = "1"
os.environ["OMP_NUM_THREADS"] = "1"
from HOMOTOPY import *
from REFINE import lp_l1
import qp


def merit(s, z, spec, target):
    v, J, g = s.evaluate(z)
    f, Df = gaps(s, z, spec)
    return float(
        np.linalg.norm(np.r_[np.maximum(s.floor - v, 0) / s.rescale, 10 * (f - target)])
    )


def retract(s, start, spec, target, steps=40):
    z = start.copy()
    trust = 0.03
    qbound = 0.004
    history = []
    for it in range(steps):
        v, J, g = s.evaluate(z)
        f, Df = gaps(s, z, spec)
        m = merit(s, z, spec, target)
        row = dict(
            it=it,
            merit=m,
            mech=float(v[: s.mechlen].min()),
            slack=float(g["slack"].min()),
            gap=f.tolist(),
            trust=trust,
        )
        history.append(row)
        if (
            np.max(abs(f - target)) < 1e-9
            and np.min(v - s.floor) > -1e-12
            and np.min(1 - g["Q"] @ g["X"].T) > -1e-11
        ):
            return z, True, history
        JQ = g["DY"][: s.nq].reshape(-1, s.n)
        floor = s.floor * 1.10
        A = np.vstack((J / s.rescale[:, None], 10 * Df, JQ))
        lo = np.r_[
            (floor - v) / s.rescale, 10 * (target - f), np.full(3 * s.nq, -qbound)
        ]
        hi = np.r_[
            np.full(len(v), np.inf), 10 * (target - f), np.full(3 * s.nq, qbound)
        ]
        lb = np.full(s.n, -trust)
        ub = np.full(s.n, trust)
        dz, error = qp.solve(A, lo, hi, lb, ub, np.ones(s.n), tol=1e-10)
        if dz is None:
            dz, error = lp_l1(A, lo, hi, lb, ub, np.ones(s.n))
        if dz is None:
            row["failure"] = error
            trust = min(1.0, trust * 1.5)
            qbound = min(0.08, qbound * 1.5)
            if it > 4 and all("failure" in r for r in history[-4:]):
                return z, False, history
            continue
        accepted = False
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
            mm = merit(s, zz, spec, target)
            if np.isfinite(mm) and (mm < m * (1 - 1e-5) or mm < 1e-9):
                z = zz
                accepted = True
                break
        row["alpha"] = alpha
        row["accepted"] = accepted
        if not accepted:
            trust *= 0.5
            qbound *= 0.5
        if trust < 1e-8:
            break
    return z, False, history


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--edges", type=int, nargs="+", required=True)
    ap.add_argument("--out", type=Path, required=True)
    ap.add_argument("--stages", type=int, default=100)
    ap.add_argument("--step", type=float, default=0.02)
    ap.add_argument("--resume", type=Path)
    a = ap.parse_args()
    out = a.out
    out.mkdir(parents=True, exist_ok=False)
    s, c, spec = build(a.edges)
    z = (
        np.zeros(s.n)
        if a.resume is None
        else np.array([float.fromhex(x) for x in json.load(open(a.resume))])
    )
    step = a.step
    records = []
    t = time.time()
    (out / "INPUT.json").write_bytes(
        B(
            dict(
                edges=a.edges,
                stages=a.stages,
                step=a.step,
                resume=None if a.resume is None else [float(x).hex() for x in z],
                versions=[platform.python_version(), np.__version__, scipy.__version__],
            )
        )
    )
    for stage in range(a.stages):
        v, J, g = s.evaluate(z)
        f, Df = gaps(s, z, spec)
        print(
            "RETRACT_STAGE",
            stage,
            "gaps",
            f,
            "mech",
            v[: s.mechlen].min(),
            "step",
            step,
            flush=True,
        )
        (out / "LIVE_Z.json").write_bytes(B([float(x).hex() for x in z]))
        if np.max(abs(f)) < 1e-9:
            break
        target = np.maximum(0, f - step)
        zz, ok, history = retract(s, z, spec, target)
        row = dict(
            stage=stage,
            source_gap=f.tolist(),
            target=target.tolist(),
            success=ok,
            inner=history,
        )
        records.append(row)
        (out / "RECORDS.json").write_bytes(B(records))
        print(
            "RETRACTION",
            stage,
            ok,
            "inner",
            len(history),
            "last",
            history[-1],
            flush=True,
        )
        if ok:
            z = zz
            step = min(0.2, step * (1.5 if len(history) < 8 else 1.05))
        else:
            step *= 0.5
        if step < 1e-6:
            break
    v, J, g = s.evaluate(z)
    f, Df = gaps(s, z, spec)
    G, patch = merged_generator(s, g["Q"], a.edges)
    (out / "GENERATOR.json").write_bytes(B(G))
    (out / "Z.json").write_bytes(B([float(x).hex() for x in z]))
    (out / "PATCHES.json").write_bytes(B(patch))
    (out / "RECORDS.json").write_bytes(B(records))
    status = dict(
        gaps=f.tolist(),
        mech=float(v[: s.mechlen].min()),
        slack=float(g["slack"].min()),
        time=time.time() - t,
        gen_sha=hashlib.sha256(B(G)).hexdigest(),
    )
    (out / "STATUS.json").write_bytes(B(status))
    print("RETRACTION_END_NUMERICAL_ONLY", json.dumps(status), flush=True)


if __name__ == "__main__":
    main()
