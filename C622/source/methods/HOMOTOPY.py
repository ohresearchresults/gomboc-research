"""Own-volume-mass guarded physical panel-gap homotopy with full contact coordinates.
Proposal only: the exact finite merged generator is accepted solely by independent audits.
"""

import os

os.environ["OPENBLAS_NUM_THREADS"] = "1"
os.environ["OMP_NUM_THREADS"] = "1"
from flexible import *
from general_atlas import GeneralAtlas
from scipy.optimize import linprog
import argparse, time, hashlib, platform, scipy
from numeric import Chart

B = lambda x: json.dumps(x, sort_keys=True, separators=(",", ":")).encode()


def build(edges):
    c = Chart()
    G = json.load(open(ROOT / "parent/GENERATOR.json"))
    rep = json.load(open(ROOT / "baseline/A.json"))
    s = FlexibleAtlas(G, rep, c.Q)
    specs = {a["edge"]: a for a in json.load(open(ROOT / "HOMOTOPY_CANDIDATES.json"))}
    spec = [specs[e] for e in edges]
    s.blockedp = []
    for r in spec:
        u, v = r["panels"]
        l, k = r["third"]
        s.blockedp.extend([(u, v), (v, u)])
        s.mask[k, u] = False
        s.mask[l, v] = False
        for t, tri in enumerate(s.tris):
            if u in tri and v in tri:
                s.floor[s.mechlen + s.nq + t] = 0.0
    s.last = None
    return s, c, spec


def gaps(s, z, spec):
    v, J, g = s.evaluate(z)
    vv = []
    jj = []
    for r in spec:
        u, _ = r["panels"]
        k = r["third"][1]
        a = (1 - g["Q"][k] @ g["X"][u]) / r["gap"]
        b = -(g["DQ"][k].T @ g["X"][u] + g["Q"][k] @ g["DX"][u]) / r["gap"]
        vv.append(a)
        jj.append(b)
    return np.array(vv), np.array(jj)


def proposal(s, z, spec, trust, qbound, maxprogress):
    v, J, g = s.evaluate(z)
    f, Df = gaps(s, z, spec)
    n = s.n
    JQ = g["DY"][: s.nq].reshape(-1, n)
    # s.evaluate DY already includes the parameter scale.
    floor = s.floor * 1.04
    A = np.vstack((-J / s.rescale[:, None], JQ, -JQ))
    b = np.r_[
        (v - floor) / s.rescale, np.full(3 * s.nq, qbound), np.full(3 * s.nq, qbound)
    ]
    # Variables: dz[n], nonnegative absolute values[n], common fractional progress.
    A = np.column_stack((A, np.zeros((len(A), n + 1))))
    A = np.vstack(
        (
            A,
            np.column_stack((np.eye(n), -np.eye(n), np.zeros(n))),
            np.column_stack((-np.eye(n), -np.eye(n), np.zeros(n))),
        )
    )
    b = np.r_[b, np.zeros(2 * n)]
    E = np.column_stack((Df, np.zeros((len(f), n)), f))
    ans = linprog(
        np.r_[np.zeros(n), np.full(n, 1e-8), -1.0],
        A_ub=A,
        b_ub=b,
        A_eq=E,
        b_eq=np.zeros(len(f)),
        bounds=[(-trust, trust)] * n + [(0, None)] * n + [(0, maxprogress)],
        method="highs-ds",
        options={
            "time_limit": 10.0,
            "primal_feasibility_tolerance": 1e-10,
            "dual_feasibility_tolerance": 1e-10,
        },
    )
    if not ans.success:
        return None, None, ans.message
    return ans.x[:n], float(ans.x[-1]), None


def merged_generator(s, Q, edges):
    G = copy.deepcopy(s.G)
    patches = []
    for edge in edges:
        a = GeneralAtlas(edge, Q.copy())
        p = a.patch
        old = p["new_node"]
        new = len(G["controls"])
        chosen = p["solved_support"]
        assert all(chosen not in deps for i, deps, axes in G["plan"])
        G["plan"] = [row for row in G["plan"] if row[0] != chosen] + [
            [new, [q for q in p["union"] if q != chosen], [0, 1, 2]],
            [chosen, [new], [p["axis"]]],
        ]
        G["groups"].append(p["union"])
        G["controls"].append([0, 0, 0])
        patches.append(dict(p, new_node=new))

    def point(ids):
        tri = max(
            itertools.combinations(ids, 3), key=lambda p: abs(np.linalg.det(Q[list(p)]))
        )
        return np.linalg.solve(Q[list(tri)], np.ones(3))

    shift = np.array([0.0, 0.0, 1.0]) - point(G["groups"][0])
    Q = Q / (1 + Q @ shift)[:, None]
    Y = np.vstack((Q, [point(ids) for ids in G["groups"]]))
    G["grid"] = 10**9
    G["controls"] = np.rint(Y * G["grid"]).astype(np.int64).tolist()
    return G, patches


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--edges", type=int, nargs="+", required=True)
    ap.add_argument("--steps", type=int, default=500)
    ap.add_argument("--out", type=Path, required=True)
    ap.add_argument("--trust", type=float, default=0.003)
    ap.add_argument("--qbound", type=float, default=0.001)
    ap.add_argument("--resume", type=Path)
    a = ap.parse_args()
    out = a.out
    out.mkdir(parents=True, exist_ok=False)
    s, c, spec = build(a.edges)
    z = (
        np.zeros(s.n)
        if a.resume is None
        else np.array([float.fromhex(t) for t in json.load(open(a.resume))])
    )
    records = []
    trust = a.trust
    qbound = a.qbound
    t = time.time()
    (out / "INPUT.json").write_bytes(
        B(
            dict(
                edges=a.edges,
                steps=a.steps,
                trust=a.trust,
                qbound=a.qbound,
                versions=[platform.python_version(), np.__version__, scipy.__version__],
                spec=spec,
                resume=None if a.resume is None else [float(x).hex() for x in z],
            )
        )
    )
    for it in range(a.steps):
        v, J, g = s.evaluate(z)
        f, Df = gaps(s, z, spec)
        row = dict(
            it=it,
            gaps=f.tolist(),
            mech=float(v[: s.mechlen].min()),
            slack=float(g["slack"].min()),
            minimum_floor_buffer=float((v - s.floor).min()),
            trust=trust,
            qbound=qbound,
        )
        records.append(row)
        print("HOMOTOPY", json.dumps(row), flush=True)
        (out / "LIVE_Z.json").write_bytes(B([float(x).hex() for x in z]))
        (out / "RECORDS.json").write_bytes(B(records))
        if max(abs(f)) < 1e-7:
            break
        dz, eta, error = proposal(
            s, z, spec, trust, qbound, 0.3 if min(f) < 0.05 else 0.15
        )
        if dz is None or eta < 1e-9:
            row["failure"] = error or "No finite LP progress"
            trust = min(0.1, trust * 1.5)
            qbound = min(0.03, qbound * 1.5)
            if it > 5 and all("failure" in r for r in records[-5:]):
                break
            continue
        row["eta"] = eta
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
            0.001953125,
            0.0009765625,
        ]:
            zz = z + alpha * dz
            vv, JJ, gg = s.evaluate(zz)
            ff, _ = gaps(s, zz, spec)
            if (
                np.all(np.isfinite(vv))
                and np.all(vv >= s.floor - 1e-13)
                and np.min(1 - gg["Q"] @ gg["X"].T) > -1e-12
                and np.min(ff) > -1e-10
                and ff.sum() < f.sum() - 1e-10
            ):
                accepted = True
                z = zz
                break
        row["alpha"] = alpha
        row["accepted"] = accepted
        if not accepted:
            trust *= 0.5
            qbound *= 0.5
        elif alpha >= 0.5:
            trust = min(0.05, trust * 1.15)
            qbound = min(0.015, qbound * 1.15)
        elif alpha < 0.125:
            trust = max(1e-6, trust * 0.8)
            qbound = max(1e-7, qbound * 0.8)
        if trust < 1e-9:
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
    print("HOMOTOPY_END_NUMERICAL_ONLY", json.dumps(status), flush=True)


if __name__ == "__main__":
    main()
