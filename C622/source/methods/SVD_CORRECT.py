"""Full physical-coordinate SVD reconditioning, actual-mass correction and inherited exits.
Adapted to the contact atlas from the literal S8 repair method. Numerical only.
"""

from contact import *
from scipy.linalg import svd
import minnorm_qp, time, hashlib

B = lambda x: json.dumps(x, sort_keys=True, separators=(",", ":")).encode()


def repair(s, z, out, steps=80, goal=1e-7, trust=0.03):
    z = np.array(z).copy()
    out = Path(out)
    out.mkdir(parents=True, exist_ok=True)
    history = []
    gf = 1e-8
    tf = 1e-10
    t0 = time.time()

    def merit(v, g):
        ev = np.minimum(v[: s.mechlen - 2] - goal, 0)
        gv = np.minimum(g["slack"][np.isfinite(g["slack"])] - gf, 0)
        dv = np.minimum(g["v6"] - tf, 0)
        return float(np.sqrt(ev @ ev + 100 * gv @ gv + 100 * dv @ dv))

    for it in range(steps):
        v, J, g = s.evaluate(z)
        m = merit(v, g)
        r = dict(
            it=it,
            merit=m,
            mech=float(v[: s.mechlen - 2].min()),
            slack=float(g["slack"].min()),
            det=float(g["v6"].min()),
            trust=trust,
        )
        history.append(r)
        print("SVD_CORRECT", json.dumps(r), flush=True)
        G = copy.deepcopy(s.G)
        G["grid"] = 10**12
        G["controls"] = np.rint(g["Y"] * G["grid"]).astype(np.int64).tolist()
        (out / "GENERATOR.json").write_bytes(B(G))
        (out / "Z.json").write_bytes(B([float(x).hex() for x in z]))
        (out / "HISTORY.json").write_bytes(B(history))
        if m < 1e-12 and v[: s.mechlen - 2].min() > goal * 0.9:
            break
        mat = np.vstack((g["DQ"].reshape(-1, s.n) / 2, g["DX"].reshape(-1, s.n)))
        _, dd, Vt = svd(mat, full_matrices=False, check_finite=False)
        W = Vt.T / np.maximum(dd, 1e-9)
        r["condition"] = float(dd.max() / max(dd.min(), 1e-30))
        qi, vi = np.where(s.mask & (g["slack"] < 0.06))
        dcs = -np.einsum("icp,ic->ip", g["DQ"][qi], g["X"][vi]) - np.einsum(
            "ic,icp->ip", g["Q"][qi], g["DX"][vi]
        )
        dtri = J[s.mechlen + s.nq : s.mechlen + s.nq + len(s.tris)] * s.tscale[:, None]
        A = np.vstack((J[: s.mechlen - 2], dcs, dtri)) @ W
        b = np.r_[
            goal * 1.1 - v[: s.mechlen - 2], gf - g["slack"][qi, vi], tf - g["v6"]
        ]
        dz, why = minnorm_qp.solve(
            A, b, bound=trust, tol=2e-12, seconds=12, maxsteps=10000
        )
        r["qp"] = why
        print("SVD_QP", why, flush=True)
        if dz is None:
            trust = min(0.2, trust * 1.5)
            if it > 2 and all(
                "qp" in rr and rr["qp"].get("why") != "pass" for rr in history[-3:]
            ):
                break
            continue
        good = False
        for ls in range(20):
            zz = z + 2.0**-ls * (W @ dz)
            try:
                vn, Jn, gn = s.evaluate(zz)
                mn = merit(vn, gn)
            except (ValueError, np.linalg.LinAlgError, FloatingPointError):
                continue
            if (
                np.min(1 - gn["Q"] @ gn["g"]) > 0.2
                and np.isfinite(mn)
                and mn < m * (1 - 1e-4 * 2.0**-ls)
            ):
                z = zz
                good = True
                break
        r["accepted"] = good
        r["halvings"] = ls
        if not good:
            trust *= 0.5
            if trust < 1e-6:
                break
    v, J, g = s.evaluate(z)
    G = copy.deepcopy(s.G)
    G["grid"] = 10**12
    G["controls"] = np.rint(g["Y"] * G["grid"]).astype(np.int64).tolist()
    (out / "GENERATOR.json").write_bytes(B(G))
    (out / "Z.json").write_bytes(B([float(x).hex() for x in z]))
    (out / "HISTORY.json").write_bytes(B(history))
    status = dict(
        mech=float(v[: s.mechlen - 2].min()),
        slack=float(g["slack"].min()),
        det=float(g["v6"].min()),
        time=time.time() - t0,
        sha=hashlib.sha256(B(G)).hexdigest(),
    )
    (out / "STATUS.json").write_bytes(B(status))
    print("SVD_END_NUMERICAL_ONLY", json.dumps(status), flush=True)
    return z
