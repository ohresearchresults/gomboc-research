"""Rooted escape-tree pivots in full-contact own-filled-mass coordinates.
Every chosen arrow points to an earlier-settled Dijkstra vertex, excluding
impossible directed cycles. This is a search restriction, not an existence theorem.
"""

import os

os.environ["OPENBLAS_NUM_THREADS"] = "1"
os.environ["OMP_NUM_THREADS"] = "1"
from flexible import *
from REFINE import correct
from scipy.optimize import least_squares
import argparse, heapq, hashlib, time, scipy, platform

sys.path.insert(0, str(ROOT / "parent"))
import RECONSTRUCT, check_B

B = lambda x: json.dumps(x, sort_keys=True, separators=(",", ":")).encode()


def arrows(A):
    e = A[None, :, :] - A[:, None, :]
    den = np.sqrt(
        np.maximum(np.sum(A * A, axis=1)[:, None] * np.sum(e * e, axis=2), 1e-40)
    )
    v = np.einsum("ic,ijc->ij", A, e) / den
    np.fill_diagonal(v, -1e10)
    return v


def tree(A, root, floor, seed=0, noise=0.0):
    V = arrows(A)
    cost = np.maximum(floor - V, 0.0) ** 2
    if noise:
        cost *= np.exp(np.random.default_rng(seed).normal(0, noise, cost.shape))
    np.fill_diagonal(cost, np.inf)
    dist = np.full(len(A), np.inf)
    dist[root] = 0
    parent = {}
    done = np.zeros(len(A), bool)
    order = []
    for _ in A:
        j = int(np.argmin(np.where(done, np.inf, dist)))
        assert np.isfinite(dist[j])
        done[j] = True
        order.append(j)
        for i in np.where(~done)[0]:
            w = dist[j] + cost[i, j]
            if w < dist[i]:
                dist[i] = w
                parent[int(i)] = j
    rank = {v: i for i, v in enumerate(order)}
    assert all(rank[j] < rank[i] for i, j in parent.items())
    return parent, dict(
        max_cost=float(dist.max()),
        sum_cost=float(sum(cost[i, j] for i, j in parent.items())),
        order=order,
    )


def cycles(A, root):
    js = np.argmax(arrows(A), axis=1)
    ans = set()
    for start in range(len(A)):
        seen = []
        v = start
        while v != root and v not in seen:
            seen.append(v)
            v = int(js[v])
        if v != root:
            cy = seen[seen.index(v) :]
            k = cy.index(min(cy))
            ans.add(tuple(cy[k:] + cy[:k]))
    return sorted(ans)


def solve(
    G, rep, Q, out, phases=10, warm=1000, steps=40, seed=0, noise=0.0, floor=1e-7
):
    s = FlexibleAtlas(G, rep, Q)
    s.checkpoint_dir = out
    s.floor[: s.mechlen - 2] = floor
    s.floor[s.mechlen - 2 : s.mechlen] = 1e-5
    s.floor[s.mechlen : s.mechlen + s.nq] = 1e-9
    s.floor[s.mechlen + s.nq : -s.nq - 1] = 1e-7
    z = np.zeros(s.n)
    records = []
    t = time.time()
    for phase in range(phases):
        s.forcedp = {}
        s.forcedq = {}
        s.last = None
        v, J, g = s.evaluate(z)
        Z = g["X"] - g["g"]
        Q = g["Q"]
        H = Q / (1 - Q @ g["g"])[:, None]
        cp, cq = cycles(Z, s.U), cycles(H, s.S)
        fp, tp = tree(Z, s.U, floor, seed + 2 * phase, noise)
        fq, tq = tree(H, s.S, floor, seed + 2 * phase + 1, noise)
        s.forcedp = fp
        s.forcedq = fq
        s.last = None
        record = dict(
            phase=phase,
            initial_primal_argmax_cycles=cp,
            initial_polar_argmax_cycles=cq,
            primal_tree=fp,
            polar_tree=fq,
            primal_stats=tp,
            polar_stats=tq,
        )
        print(
            "TREE_PHASE",
            phase,
            "cycles",
            cp,
            cq,
            "cost",
            tp["sum_cost"],
            tq["sum_cost"],
            flush=True,
        )
        best = [float("inf"), z.copy()]
        calls = [0]

        def fun(zz):
            r = s.residual(zz)
            m = float(r @ r)
            calls[0] += 1
            if m < best[0]:
                best[:] = [m, zz.copy()]
            if calls[0] % 200 == 0:
                print("TREE_WARM", phase, calls[0], best[0], flush=True)
            return r

        if warm:
            least_squares(
                fun,
                z,
                jac=s.derivative,
                max_nfev=warm,
                ftol=1e-13,
                xtol=1e-13,
                gtol=1e-13,
                x_scale="jac",
            )
            z = best[1]
        (out / ("WARM_" + str(phase) + ".json")).write_bytes(
            B([float(x).hex() for x in z])
        )
        z, h = correct(s, z, steps)
        record["correction"] = h
        s.forcedp = {}
        s.forcedq = {}
        s.last = None
        v, J, g = s.evaluate(z)
        record["actual_mech"] = float(v[: s.mechlen].min())
        record["slack"] = float(g["slack"].min())
        record["det"] = float(g["v6"].min())
        records.append(record)
        GG = copy.deepcopy(s.G)
        GG["grid"] = 10**12
        GG["controls"] = np.rint(g["Y"] * GG["grid"]).astype(np.int64).tolist()
        (out / "GENERATOR.json").write_bytes(B(GG))
        (out / "Z.json").write_bytes(B([float(x).hex() for x in z]))
        (out / "RECORDS.json").write_bytes(B(records))
        (out / ("GENERATOR_" + str(phase) + ".json")).write_bytes(B(GG))
        print(
            "TREE_ACTUAL",
            phase,
            record["actual_mech"],
            record["slack"],
            record["det"],
            flush=True,
        )
        if (
            record["actual_mech"] > floor * 0.7
            and record["slack"] > 1e-10
            and record["det"] > 0
        ):
            break
    status = dict(
        mech=float(v[: s.mechlen].min()),
        slack=float(g["slack"].min()),
        det=float(g["v6"].min()),
        phases=len(records),
        time=time.time() - t,
        sha=hashlib.sha256(B(GG)).hexdigest(),
    )
    (out / "STATUS.json").write_bytes(B(status))
    print("TREE_NUMERICAL_ONLY", json.dumps(status), flush=True)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--generator", type=Path, required=True)
    ap.add_argument("--out", type=Path, required=True)
    ap.add_argument("--phases", type=int, default=8)
    ap.add_argument("--warm", type=int, default=800)
    ap.add_argument("--steps", type=int, default=40)
    ap.add_argument("--seed", type=int, default=0)
    ap.add_argument("--noise", type=float, default=0)
    ap.add_argument("--floor", type=float, default=1e-7)
    a = ap.parse_args()
    a.out.mkdir(parents=True, exist_ok=False)
    G = json.load(open(a.generator))
    raw = RECONSTRUCT.recover(G)
    rep = check_B.run(raw)
    (a.out / "SOURCE_GENERATOR.json").write_bytes(B(G))
    (a.out / "SOURCE_B.json").write_bytes(B(rep))
    Q = np.array([[float(F(v, r[-1])) for v in r[:3]] for r in raw["H"]])
    (a.out / "INPUT.json").write_bytes(
        B(
            dict(
                phases=a.phases,
                warm=a.warm,
                steps=a.steps,
                seed=a.seed,
                noise=a.noise,
                floor=a.floor,
                versions=[platform.python_version(), np.__version__, scipy.__version__],
            )
        )
    )
    solve(G, rep, Q, a.out, a.phases, a.warm, a.steps, a.seed, a.noise, a.floor)


if __name__ == "__main__":
    main()
