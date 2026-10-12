"""General triangular-panel union with an unused support's previous contacts retained."""

from contact import *
from fractions import Fraction as F


class UnionAtlas(Atlas):
    def __init__(self, G, rep, pair, Qinit, S=3):
        self.G = G = copy.deepcopy(G)
        self.parents = rep
        self.forcedp = {}
        self.forcedq = {}
        self.nq = G["n_supports"]
        self.S = S
        root = next(
            v for v, r in enumerate(rep["raw_vertices"]) if list(map(F, r)) == [0, 0, 1]
        )
        owners = [
            [
                rep["active_input_indices"][f]
                for f, cy in enumerate(rep["faces"])
                if v in cy
            ]
            for v in range(rep["V"])
        ]
        assert rep["active_input_indices"] == list(range(self.nq))
        ends = [i for i, o in enumerate(owners) if all(q in o for q in pair)]
        assert (
            len(ends) == 2
            and all(len(owners[i]) == 3 for i in ends)
            and root not in ends
        )
        gone, keep = sorted(ends)
        union = sorted(set(owners[gone] + owners[keep]))
        assert len(union) == 4
        plan = {i: (deps, axes) for i, deps, axes in G["plan"]}
        used = {d for _, deps, _ in G["plan"] for d in deps}
        eligible = [i for i in pair if len(plan[i][0]) < 3 and i not in used]
        assert eligible, "Needs rechart: no unused support with free coordinate"

        def pt(ids):
            tri = max(
                itertools.combinations(ids, 3),
                key=lambda a: abs(np.linalg.det(Qinit[list(a)])),
            )
            return np.linalg.solve(Qinit[list(tri)], np.ones(3))

        shift = np.array([0.0, 0.0, 1.0]) - pt(G["groups"][0])
        Qinit = Qinit / (1 + Qinit @ shift)[:, None]
        x = pt(union)
        Y = np.vstack((Qinit, [pt(g) for g in G["groups"]]))
        new = len(G["controls"])
        choices = []
        for i in eligible:
            tri = [q for q in union if q != i]
            xx = pt(tri)
            rows = np.vstack((Y[plan[i][0]], xx))
            for aa in itertools.combinations(range(3), len(rows)):
                determinant = abs(np.linalg.det(rows[:, aa]))
                score = abs(np.linalg.det(Qinit[tri])) * determinant
                choices.append((score, i, list(aa), xx))
        score, chosen, axes, x = max(choices, key=lambda c: c[0])
        assert score > 0
        deps = plan[chosen][0] + [new]
        G["controls"].append(np.rint(x * G["grid"]).astype(np.int64).tolist())
        G["groups"].append(union)
        G["plan"] = [r for r in G["plan"] if r[0] != chosen] + [
            [new, [q for q in union if q != chosen], [0, 1, 2]],
            [chosen, deps, axes],
        ]
        self.patch = dict(
            pair=list(pair),
            gone=gone,
            keep=keep,
            union=union,
            new_node=new,
            solved_support=chosen,
            old_solve=list(plan[chosen]),
            deps=deps,
            axes=axes,
        )
        axmap = {i: ax for i, dd, ax in G["plan"]}
        self.free = [
            (i, k)
            for i in range(len(G["controls"]))
            if i != self.nq
            for k in range(3)
            if k not in axmap[i]
        ]
        self.n = len(self.free)
        self.base = np.array([G["controls"][i][a] / G["grid"] for i, a in self.free])
        self.scale = np.ones(self.n)
        old = [i for i in range(rep["V"]) if i != gone]
        mapping = {v: i for i, v in enumerate(old)}
        mapping[gone] = mapping[keep]
        owners[keep] = union
        self.owners = [owners[i] for i in old]
        self.oldids = old
        self.U = mapping[root]
        self.nv = len(old)
        self.mechlen = self.nv + self.nq
        self.merged = mapping[keep]
        faces = []
        for cy in rep["faces"]:
            cc = [mapping[i] for i in cy]
            out = []
            for v in cc:
                if not out or v != out[-1]:
                    out.append(v)
            if out[0] == out[-1]:
                out.pop()
            assert (
                len(set(out)) == len(out) and len(out) >= 3
            ), "Requires true polar vertex suppression"
            faces.append(out)
        self.faces = faces
        self.tris = np.array(
            [(cy[0], cy[k], cy[k + 1]) for cy in faces for k in range(1, len(cy) - 1)]
        )
        groups = {frozenset(g): self.nq + k for k, g in enumerate(G["groups"])}
        self.direct = np.array([groups.get(frozenset(o), -1) for o in self.owners])
        self.simple = np.where(self.direct < 0)[0]
        assert all(len(self.owners[v]) == 3 for v in self.simple)
        self.trip = np.array([self.owners[v] for v in self.simple])
        self.mask = np.ones((self.nq, self.nv), bool)
        for v, own in enumerate(self.owners):
            self.mask[own, v] = False
        self.keptp = np.array([i for i in range(self.nv) if i != self.U])
        self.keptq = np.array([i for i in range(self.nq) if i != S])
        self.last = None
        self.tscale = np.ones(len(self.tris))
        install(self, Qinit)
        val, jac, geo = self.evaluate(np.zeros(self.n))
        self.floor = np.zeros(len(val))
        self.floor[: self.mechlen - 2] = 1e-7
        self.floor[self.mechlen - 2 : self.mechlen] = 1e-5
        self.floor[self.mechlen : self.mechlen + self.nq] = 1e-9
        self.floor[self.mechlen + self.nq : -self.nq - 1] = 1e-6
        self.floor[-self.nq - 1 : -1] = 0.001
        self.floor[-1] = 0.02
        self.rescale = np.ones(len(val))
        self.rescale[: self.mechlen + self.nq] = 1e-3
