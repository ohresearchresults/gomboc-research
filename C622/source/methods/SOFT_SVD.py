"""Adaptive damped Gauss-Newton in the full physical SVD metric, own-filled mass.
All mechanical exits are reevaluated; numerical proposals only. Boundaries are
checked nonlinearly. The exact hull and all cone census are external acceptance.
"""

import os

os.environ["OPENBLAS_NUM_THREADS"] = "1"
os.environ["OMP_NUM_THREADS"] = "1"
from flexible import *
from TREE_REPAIR import tree
from scipy.linalg import svd, cho_factor, cho_solve
import argparse, platform, scipy, time, hashlib

sys.path.insert(0, str(ROOT / "parent"))
import RECONSTRUCT, check_B

B = lambda x: json.dumps(x, sort_keys=True, separators=(",", ":")).encode()


def repair(s, z, out, steps=500, goal=3e-7, trust=0.02):
    z = z.copy()
    out = Path(out)
    mu = 1e-4
    history = []
    t0 = time.time()
    gf = 1e-8
    tf = 1e-10
    geomweight = 100.0

    def residual(v, J, g):
        qi, vi = np.where(s.mask)
        gs = g["slack"][qi, vi]
        tri = g["v6"]
        vm = v[: s.mechlen - 2]
        active = vm < goal
        ag = gs < gf
        at = tri < tf
        dcs = -np.einsum("icp,ic->ip", g["DQ"][qi[ag]], g["X"][vi[ag]]) - np.einsum(
            "ic,icp->ip", g["Q"][qi[ag]], g["DX"][vi[ag]]
        )
        dtri = (
            J[s.mechlen + s.nq : s.mechlen + s.nq + len(s.tris)] * s.tscale[:, None]
        )[at]
        r = np.r_[
            vm[active] - goal, geomweight * (gs[ag] - gf), geomweight * (tri[at] - tf)
        ]
        D = np.vstack((J[: s.mechlen - 2][active], geomweight * dcs, geomweight * dtri))
        return r, D

    for it in range(steps):
        v, J, g = s.evaluate(z)
        r, D = residual(v, J, g)
        score = float(r @ r)
        row = dict(
            it=it,
            score=score,
            mech=float(v[: s.mechlen - 2].min()),
            slack=float(g["slack"].min()),
            det=float(g["v6"].min()),
            mu=mu,
        )
        history.append(row)
        if it % 5 == 0:
            print("SOFT_SVD", json.dumps(row), flush=True)
        G = copy.deepcopy(s.G)
        G["grid"] = 10**12
        G["controls"] = np.rint(g["Y"] * G["grid"]).astype(np.int64).tolist()
        (out / "GENERATOR.json").write_bytes(B(G))
        (out / "Z.json").write_bytes(B([float(t).hex() for t in z]))
        (out / "HISTORY.json").write_bytes(B(history))
        if (
            v[: s.mechlen - 2].min() > goal * 0.99
            and g["slack"].min() > gf
            and g["v6"].min() > tf
        ):
            break
        mat = np.vstack((g["DQ"].reshape(-1, s.n) / 2, g["DX"].reshape(-1, s.n)))
        _, dd, Vt = svd(mat, full_matrices=False, check_finite=False)
        W = Vt.T / np.maximum(dd, 1e-9)
        A = D @ W
        grad = A.T @ r
        row["gradient"] = float(np.linalg.norm(grad))
        accepted = False
        for trial in range(8):
            try:
                dy = cho_solve(
                    cho_factor(
                        A.T @ A + mu * np.eye(s.n), lower=True, check_finite=False
                    ),
                    -grad,
                    check_finite=False,
                )
            except np.linalg.LinAlgError:
                mu *= 10
                continue
            if np.max(abs(dy)) > trust:
                dy *= trust / np.max(abs(dy))
            for ls in range(15):
                zz = z + (2.0**-ls) * W @ dy
                try:
                    vn, Jn, gn = s.evaluate(zz)
                    rn, Dn = residual(vn, Jn, gn)
                    sn = float(rn @ rn)
                except (ValueError, np.linalg.LinAlgError):
                    continue
                # Strictly convex source stays on the same nominal exposed complex.
                keepgeo = (g["slack"].min() <= 0 or gn["slack"].min() > 1e-11) and (
                    g["v6"].min() <= 0 or gn["v6"].min() > 1e-13
                )
                if (
                    np.isfinite(sn)
                    and keepgeo
                    and np.min(1 - gn["Q"] @ gn["g"]) > 0.2
                    and sn < score * (1 - 1e-6 * 2.0**-ls)
                ):
                    z = zz
                    accepted = True
                    break
            if accepted:
                mu = max(1e-12, mu * (0.3 if ls < 2 else 3))
                break
            mu = min(1e12, mu * 10)
        row["accepted"] = accepted
        row["halvings"] = ls
        if not accepted:
            break
    v, J, g = s.evaluate(z)
    G = copy.deepcopy(s.G)
    G["grid"] = 10**12
    G["controls"] = np.rint(g["Y"] * G["grid"]).astype(np.int64).tolist()
    (out / "GENERATOR.json").write_bytes(B(G))
    (out / "Z.json").write_bytes(B([float(t).hex() for t in z]))
    (out / "HISTORY.json").write_bytes(B(history))
    status = dict(
        mech=float(v[: s.mechlen - 2].min()),
        slack=float(g["slack"].min()),
        det=float(g["v6"].min()),
        seconds=time.time() - t0,
        sha=hashlib.sha256(B(G)).hexdigest(),
    )
    (out / "STATUS.json").write_bytes(B(status))
    print("SOFT_END_NUMERICAL_ONLY", json.dumps(status), flush=True)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--generator", type=Path, required=True)
    ap.add_argument("--out", type=Path, required=True)
    ap.add_argument("--steps", type=int, default=500)
    ap.add_argument("--goal", type=float, default=3e-7)
    ap.add_argument("--tree", action="store_true")
    a = ap.parse_args()
    a.out.mkdir(parents=True, exist_ok=False)
    G = json.load(open(a.generator))
    raw = RECONSTRUCT.recover(G)
    rep = check_B.run(raw)
    Q = np.array([[float(F(x, r[-1])) for x in r[:3]] for r in raw["H"]])
    s = FlexibleAtlas(G, rep, Q)
    (a.out / "SOURCE_GENERATOR.json").write_bytes(B(G))
    (a.out / "SOURCE_B.json").write_bytes(B(rep))
    v, J, g = s.evaluate(np.zeros(s.n))
    if a.tree:
        s.forcedp, p = tree(g["X"] - g["g"], s.U, a.goal)
        s.forcedq, q = tree(Q / (1 - Q @ g["g"])[:, None], s.S, a.goal)
        (a.out / "WITNESSES.json").write_bytes(
            B(dict(primal=s.forcedp, polar=s.forcedq, stats=[p, q]))
        )
        s.last = None
    (a.out / "INPUT.json").write_bytes(
        B(
            dict(
                steps=a.steps,
                goal=a.goal,
                tree=a.tree,
                versions=[platform.python_version(), np.__version__, scipy.__version__],
            )
        )
    )
    print(
        "SOFT_INITIAL_EXACT_B",
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
