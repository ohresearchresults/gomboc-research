"""Numerical proposals only: faithful stress solve, Maxwell lift, inverse map and filled mass."""

import os

os.environ.setdefault("OPENBLAS_NUM_THREADS", "1")
os.environ.setdefault("OMP_NUM_THREADS", "1")
import json
from fractions import Fraction
from pathlib import Path
import numpy as np
import scipy.linalg as la
from collections import defaultdict, deque
from scipy.spatial import ConvexHull


class Chart:
    def __init__(self, root=None):
        directory = Path(root) if root is not None else Path(__file__).parent
        data = json.loads((directory / "chart_exact.json").read_text())

        def arr(k):
            return np.array(data[k], dtype=object).astype(str)

        def num(x):
            return float(Fraction(x))

        def nums(x):
            return np.vectorize(num)(np.array(x, dtype=object))

        self.data = data
        self.Q = nums(data["Q"])
        self.X = nums(data["X"])
        self.R = nums(data["R"])
        self.w = nums(data["weights"])
        self.faces = data["faces"]
        self.edges = np.array(data["edges"], int)
        self.outer = data["outer"]
        self.boundary = np.array(data["boundary"], int)
        self.delta = num(data["delta"])
        self.c = nums(data["c"])
        self.basis = np.array([nums(data[k]) for k in ("a", "b", "d")])
        self.n = len(self.Q)
        self.nf = len(self.faces)
        self.left = {}
        for f, cy in enumerate(self.faces):
            for i, j in zip(cy, cy[1:] + cy[:1]):
                self.left[i, j] = f
        self.ef = np.array([[self.left[i, j], self.left[j, i]] for i, j in self.edges])
        self.inner = np.array([i for i in range(self.n) if i not in self.boundary])
        self.ie = np.where(np.all(self.ef != self.outer, axis=1))[0]
        inc = np.zeros((self.n, len(self.edges)))
        for k, (i, j) in enumerate(self.edges):
            inc[i, k] = 1
            inc[j, k] = -1
        self.Bi = inc[self.inner][:, self.ie]
        self.Bb = inc[self.boundary][:, self.ie]
        self.rb = self.R[self.boundary, :2]
        self.Ainv = np.linalg.inv(np.column_stack((self.rb, np.ones(3))))
        links = defaultdict(list)
        for k, (L, R) in enumerate(self.ef):
            if self.outer not in (L, R):
                links[R].append((L, k, 1))
                links[L].append((R, k, -1))
        root = next(f for f in range(self.nf) if f != self.outer)
        seen = {root}
        dq = deque([root])
        T = np.zeros((self.nf, len(self.edges)))
        while dq:
            f = dq.popleft()
            for g, e, s in links[f]:
                if g not in seen:
                    T[g] = T[f]
                    T[g, e] += s
                    seen.add(g)
                    dq.append(g)
        assert len(seen) == self.nf - 1
        self.T = T[:, self.ie]
        self.vf = np.array(
            [
                next(
                    f for f, cy in enumerate(self.faces) if v in cy and f != self.outer
                )
                for v in range(self.n)
            ]
        )
        self.physical_faces = json.loads((directory / "baseline/A.json").read_text())[
            "faces"
        ]
        self.triples = np.array([f[:3] for f in self.faces])
        self.ptris = np.array(
            [
                (cy[0], cy[k], cy[k + 1])
                for cy in self.physical_faces
                for k in range(1, len(cy) - 1)
            ]
        )
        self.parent_pedges = np.array(
            json.loads((directory / "baseline/A.json").read_text())["edges"]
        )

    def solve(self, w, normalize=True):
        wi = w[self.ie]
        L = (self.Bi * wi) @ self.Bi.T
        rhs = -((self.Bi * wi) @ self.Bb.T) @ self.rb
        r = np.empty((self.n, 2))
        r[self.boundary] = self.rb
        r[self.inner] = la.solve(L, rhs, assume_a="pos", check_finite=False)
        e = r[self.edges[self.ie, 1]] - r[self.edges[self.ie, 0]]
        J = e[:, ::-1] * [-1, 1]
        off = -np.einsum("ij,ij->i", J, r[self.edges[self.ie, 0]])
        planes = self.T @ (wi[:, None] * np.column_stack((J, off)))
        h = np.einsum(
            "ij,ij->i", planes[self.vf], np.column_stack((r, np.ones(self.n)))
        )
        h -= np.column_stack((r, np.ones(self.n))) @ (self.Ainv @ h[self.boundary])
        h[self.boundary] = 0
        if normalize:
            h *= self.R[:, 2].sum() / h.sum()
        den = 1 + h / self.delta
        if den.min() <= 0:
            raise ValueError("inverse pole")
        Q = self.c + (np.column_stack((r, h)) @ self.basis) / den[:, None]
        return Q, r, h

    def fixed(self, Q):
        X = np.linalg.solve(Q[self.triples], np.ones((self.nf, 3, 1)))[:, :, 0]
        tr = X[self.ptris]
        vol6 = np.einsum("ij,ij->i", tr[:, 0], np.cross(tr[:, 1], tr[:, 2]))
        V = vol6.sum() / 6
        c = (vol6[:, None] * tr.sum(axis=1)).sum(axis=0) / (24 * V)
        return X, V, c

    def actual(self, Q, tol=1e-9):
        hull = ConvexHull(Q)
        # plane equations provide vertices of P; merge planar Q triangles only for numeric screening.
        pq = -hull.equations[:, :3] / hull.equations[:, 3, None]
        X = []
        owners = []
        for v in pq:
            if not any(np.linalg.norm(v - x) < tol for x in X):
                X.append(v)
                owners.append(np.where(np.abs(Q @ v - 1) < tol)[0].tolist())
        X = np.array(X)
        faces = []
        normals = []
        labels = []
        edges = defaultdict(list)
        tris = []
        for f, q in enumerate(Q):
            ids = np.where(np.abs(X @ q - 1) < tol)[0]
            if len(ids) < 3:
                continue
            centre = X[ids].mean(axis=0)
            u = X[ids[0]] - centre
            u /= np.linalg.norm(u)
            v = np.cross(q, u)
            v /= np.linalg.norm(v)
            cy = ids[
                np.argsort(np.arctan2((X[ids] - centre) @ v, (X[ids] - centre) @ u))
            ].tolist()
            # discard collinear numerical points
            changed = True
            while changed and len(cy) > 3:
                changed = False
                for k in range(len(cy)):
                    if (
                        np.linalg.norm(
                            np.cross(
                                X[cy[k]] - X[cy[k - 1]],
                                X[cy[(k + 1) % len(cy)]] - X[cy[k]],
                            )
                        )
                        < 1e-12
                    ):
                        del cy[k]
                        changed = True
                        break
            fi = len(faces)
            faces.append(cy)
            normals.append(q)
            labels.append(f)
            for i, j in zip(cy, cy[1:] + cy[:1]):
                edges[tuple(sorted((i, j)))].append(fi)
            tris.extend((cy[0], cy[k], cy[k + 1]) for k in range(1, len(cy) - 1))
        if not all(len(fs) == 2 for fs in edges.values()):
            raise ValueError("numeric incidence")
        tr = X[np.array(tris)]
        v6 = np.einsum("ij,ij->i", tr[:, 0], np.cross(tr[:, 1], tr[:, 2]))
        V = v6.sum() / 6
        c = (v6[:, None] * tr.sum(axis=1)).sum(axis=0) / (24 * V)
        if V <= 0 or np.min(1 - Q @ c) <= 0:
            raise ValueError("noninterior mass")
        Z = X - c
        H = Q / (1 - Q @ c)[:, None]
        qdots = H @ H.T
        fs = qdots.diagonal() - qdots.max(axis=1)  # always <=0 incl self
        S = np.where(np.all(qdots <= qdots.diagonal()[:, None] + 1e-12, axis=1))[
            0
        ].tolist()
        pmax = Z @ Z.T - np.sum(Z * Z, axis=1)[:, None]
        np.fill_diagonal(pmax, -np.inf)
        U = np.where(pmax.max(axis=1) < 1e-11)[0].tolist()
        E = []
        for (i, j), ff in edges.items():
            e = Z[j] - Z[i]
            ee = e @ e
            t = -Z[i] @ e / ee
            if not 0 < t < 1:
                continue
            n, m = np.array(normals)[ff]
            p = Z[i] + t * e
            aa = n @ n
            bb = n @ m
            cc = m @ m
            rr = p @ n
            ss = p @ m
            if min(rr * cc - ss * bb, ss * aa - rr * bb) > 1e-12:
                E.append((i, j))
        return dict(
            V=len(X),
            E=len(edges),
            F=len(faces),
            counts=[len(S), len(U), len(E)],
            volume=V,
            centroid=c.tolist(),
            S=S,
            U=[owners[i] for i in U],
            H=E,
            Q=Q.tolist(),
        )


if __name__ == "__main__":
    c = Chart()
    Q, r, h = c.solve(c.w)
    X, V, g = c.fixed(Q)
    print(
        "NUMERICAL_FAITHFUL_CHART",
        np.max(np.abs(Q - c.Q)),
        np.max(np.abs(r - c.R[:, :2])),
        np.max(np.abs(h - c.R[:, 2])),
        V,
        g,
    )
    a = c.actual(Q)
    a.pop("Q")
    print(a)
    if "--screen" in __import__("sys").argv:
        results = []
        for k in c.ie:
            w = c.w.copy()
            w[k] = 0
            try:
                Q, _, _ = c.solve(w)
                a = c.actual(Q)
                a.update(
                    edge=int(k), endpoints=c.edges[k].tolist(), weight=float(c.w[k])
                )
                a.pop("Q")
            except Exception as e:
                a = dict(edge=int(k), endpoints=c.edges[k].tolist(), error=str(e))
            results.append(a)
        Path(__file__).with_name("screen.json").write_text(
            json.dumps(results, indent=2)
        )
        good = [a for a in results if "counts" in a]
        good.sort(key=lambda a: (sum(a["counts"]), a["E"]))
        print("SCREEN", len(results), len(good))
        print(json.dumps(good[:15], indent=2))
