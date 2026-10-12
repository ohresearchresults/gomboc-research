"""General maximal polar-panel union and fresh 3-degenerate bipartite contact atlas.
Full contact graph is rebuilt; no unused-support or free-contact-node restriction.
The fixed apex is first. All other nodes are peeled with at most three remaining
neighbours, then solved in reverse order with best nonzero numerical minors.
Final rational reconstruction and true hull audits remain mandatory.
"""

import os

os.environ["OPENBLAS_NUM_THREADS"] = "1"
os.environ["OMP_NUM_THREADS"] = "1"
from flexible import *
from numeric import Chart
from CROSS_CAP import inherited
from TREE_REPAIR import arrows
from SVD_CORRECT import repair
import argparse, platform, scipy, hashlib

B = lambda x: json.dumps(x, sort_keys=True, separators=(",", ":")).encode()


def atlas_generator(owners, Q, anchorowners, grid=10**12):
    n = len(Q)
    groups = [sorted(o) for o in owners if len(o) > 3 and set(o) != set(anchorowners)]
    groups.sort()
    groups = [sorted(anchorowners)] + groups

    def pt(ids):
        tri = max(
            itertools.combinations(ids, 3), key=lambda t: abs(np.linalg.det(Q[list(t)]))
        )
        return np.linalg.solve(Q[list(tri)], np.ones(3))

    shift = np.array([0.0, 0.0, 1.0]) - pt(anchorowners)
    Q = Q / (1 + Q @ shift)[:, None]
    Y = np.vstack((Q, [pt(o) for o in groups]))
    Y[n] = [0, 0, 1]
    adj = {i: set() for i in range(len(Y))}
    for j, g in enumerate(groups, n):
        for i in g:
            adj[i].add(j)
            adj[j].add(i)
    remain = set(range(len(Y)))
    removed = []
    while len(remain) > 1:
        choices = []
        for i in sorted(remain - {n}):
            deps = sorted(adj[i] & remain)
            if len(deps) > 3:
                continue
            axes = list(itertools.combinations(range(3), len(deps)))
            aa = max(
                axes,
                key=lambda ax: abs(np.linalg.det(Y[np.ix_(deps, ax)])) if deps else 1.0,
            )
            cond = abs(np.linalg.det(Y[np.ix_(deps, aa)])) if deps else 1.0
            if cond > 1e-15:
                choices.append((len(deps), cond, -i, i, deps, list(aa)))
        assert choices, "Nonzero-minor peeling blocked; no object is inferred"
        _, _, _, i, deps, aa = max(choices)
        removed.append([i, deps, aa])
        remain.remove(i)
    plan = removed[::-1]
    done = {n}
    for i, deps, aa in plan:
        assert set(deps) <= done
        done.add(i)
    G = dict(
        n_supports=n,
        grid=grid,
        groups=groups,
        controls=np.rint(Y * grid).astype(np.int64).tolist(),
        plan=plan,
    )
    return G, Q


def quotient(rep, pair):
    n = rep["F"]
    assert rep["active_input_indices"] == list(range(n))
    owners = [
        [i for i, cy in enumerate(rep["faces"]) if v in cy] for v in range(rep["V"])
    ]
    ends = [v for v, o in enumerate(owners) if set(pair) <= set(o)]
    assert len(ends) == 2
    gone, keep = sorted(ends)
    union = sorted(set(owners[gone] + owners[keep]))
    assert len(set(owners[gone]) & set(owners[keep])) == 2
    old = [v for v in range(rep["V"]) if v != gone]
    mp = {v: i for i, v in enumerate(old)}
    mp[gone] = mp[keep]
    owners[keep] = union
    newowners = [owners[v] for v in old]
    faces = []
    for cy in rep["faces"]:
        cc = []
        for v in cy:
            v = mp[v]
            if not cc or cc[-1] != v:
                cc.append(v)
        if cc[0] == cc[-1]:
            cc.pop()
        assert (
            len(set(cc)) == len(cc) and len(cc) >= 3
        ), "This loss needs actual polar vertex suppression"
        faces.append(cc)
    nr = copy.deepcopy(rep)
    nr["V"] -= 1
    nr["E"] -= 1
    nr["faces"] = faces
    nr["raw_vertices"] = [rep["raw_vertices"][v] for v in old]
    nr["edges"] = sorted(
        {tuple(sorted((u, v))) for cy in faces for u, v in zip(cy, cy[1:] + cy[:1])}
    )
    assert len(nr["edges"]) == nr["E"]
    return (
        nr,
        newowners,
        dict(
            pair=list(pair),
            parent_vertex_indices=ends,
            parent_groups=[
                owners[gone],
                [i for i, cy in enumerate(rep["faces"]) if keep in cy],
            ],
            child_group=union,
            physical_old_to_new=mp,
        ),
    )


def make(c, rep, pair, mode="stress"):
    nr, owners, patch = quotient(rep, pair)
    root = next(
        v for v, row in enumerate(rep["raw_vertices"]) if list(map(F, row)) == [0, 0, 1]
    )
    anchorowners = [i for i, cy in enumerate(rep["faces"]) if root in cy]
    assert set(anchorowners) != set(patch["child_group"])
    if mode == "stress":
        ei = next(k for k, p in enumerate(c.edges) if list(p) == list(pair))
        w = c.w.copy()
        assert w[ei] > 0
        w[ei] = 0
        from RELIFT import seed

        Q, relift = seed(c, w)
    else:
        Q = c.Q.copy()
    G, Q = atlas_generator(owners, Q, anchorowners)
    s = FlexibleAtlas(G, nr, Q)
    return s, nr, patch, Q


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--chart", type=Path, required=True)
    ap.add_argument("--pair", type=int, nargs=2, required=True)
    ap.add_argument("--mode", choices=["stress", "direct"], default="stress")
    ap.add_argument("--steps", type=int, default=80)
    ap.add_argument("--goal", type=float, default=1e-7)
    ap.add_argument("--dynamic", action="store_true")
    ap.add_argument("--out", type=Path, required=True)
    a = ap.parse_args()
    a.out.mkdir(parents=True, exist_ok=False)
    c = Chart(a.chart)
    rep = json.load(open(a.chart / "baseline/A.json"))
    s, nr, patch, Q = make(c, rep, sorted(a.pair), a.mode)
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
    (a.out / "INITIAL_Q_HEX.json").write_bytes(
        B([[float(x).hex() for x in row] for row in Q])
    )
    (a.out / "INPUT.json").write_bytes(
        B(
            dict(
                pair=a.pair,
                mode=a.mode,
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
