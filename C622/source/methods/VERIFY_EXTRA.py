"""Additional exact contact inverse, lineage, stress and connectivity checks."""

import sys, json, copy, itertools, hashlib
from pathlib import Path
from fractions import Fraction as F
from collections import Counter

sys.set_int_max_str_digits(0)
ROOT = Path(__file__).resolve().parent
sys.path.insert(0, str(ROOT / "parent"))
import RECONSTRUCT, check_A, check_B, chart, chart_audit

B = lambda x: json.dumps(x, sort_keys=True, separators=(",", ":")).encode()


def owners(rep):
    return {
        frozenset(
            rep["active_input_indices"][f]
            for f, cy in enumerate(rep["faces"])
            if v in cy
        ): v
        for v in range(rep["V"])
    }


def atlas(G, raw, rep):
    n = G["n_supports"]
    D = G["grid"]
    Y = [[F(v, D) for v in row] for row in G["controls"]]
    Y[n] = [F(0), F(0), F(1)]
    for i, deps, axes in G["plan"]:
        if deps:
            rest = [k for k in range(3) if k not in axes]
            M = [[Y[j][k] for k in axes] for j in deps]
            rhs = [1 - sum(Y[j][k] * Y[i][k] for k in rest) for j in deps]
            for k, value in zip(axes, RECONSTRUCT.solve(M, rhs)):
                Y[i][k] = value
        assert all(check_A.dot(Y[i], Y[j]) == 1 for j in deps)
    Q = [tuple(F(v, row[3]) for v in row[:3]) for row in raw["H"]]
    assert list(map(tuple, Y[:n])) == Q
    own = owners(rep)
    X = [tuple(map(F, row)) for row in rep["raw_vertices"]]
    for j, g in enumerate(G["groups"]):
        assert tuple(Y[n + j]) == X[own[frozenset(g)]]
        tri = next(
            t for t in itertools.combinations(g, 3) if check_A.det(*(Q[k] for k in t))
        )
        assert chart.inv3([Q[k] for k in tri], [F(1)] * 3) == tuple(Y[n + j])
    axes = {i: ax for i, d, ax in G["plan"]}
    free = [
        (i, k) for i in range(len(Y)) if i != n for k in range(3) if k not in axes[i]
    ]
    assert all(Y[i][k] == F(G["controls"][i][k], D) for i, k in free)
    eq = sum(map(len, G["groups"]))
    assert eq == sum(len(d) for i, d, ax in G["plan"])
    assert len(free) == rep["E"] + 3
    return dict(
        nodes=len(Y),
        supports=n,
        nonsimple_contact_points=len(G["groups"]),
        contact_equations=eq,
        free_coordinates=len(free),
        free_indices=free,
        exact_forward_inverse_pass=True,
    )


def connectivity(n, edges):
    adj = [set() for _ in range(n)]
    for u, v in edges:
        adj[u].add(v)
        adj[v].add(u)
    count = 0
    for k in range(3):
        for gone in itertools.combinations(range(n), k):
            ban = set(gone)
            root = next(i for i in range(n) if i not in ban)
            seen = {root}
            todo = [root]
            while todo:
                u = todo.pop()
                for v in adj[u] - ban - seen:
                    seen.add(v)
                    todo.append(v)
            assert len(seen) == n - k
            count += 1
    return count


def verify(parent_root, child_audit, out):
    out = Path(out)
    out.mkdir(parents=True, exist_ok=False)
    parent_root = Path(parent_root)
    child_audit = Path(child_audit)
    seed = chart.recover(root=parent_root)
    before = json.load(open(parent_root / "baseline/A.json"))
    after = json.load(open(child_audit / "A.json"))
    raw = json.load(open(child_audit / "raw.json"))
    G = json.load(open(child_audit / "GENERATOR.json"))
    a = atlas(G, raw, after)
    (out / "ATLAS.json").write_bytes(B(a))
    old, new = owners(before), owners(after)
    removed = sorted([sorted(o) for o in old.keys() - new.keys()])
    added = sorted([sorted(o) for o in new.keys() - old.keys()])
    assert removed == [[71, 94, 109, 119], [71, 109, 116, 126]]
    assert added == [[71, 94, 109, 116, 119, 126]]
    protected = [[16, 18, 71, 94], [87, 108, 122, 127]]
    assert all(frozenset(g) in new for g in protected)
    Q = [tuple(F(v, row[3]) for v in row[:3]) for row in raw["H"]]
    st = chart_audit.verify_geometry(Q, seed)
    assert st["zero_endpoint_pairs"] == [[71, 109]]
    assert st["positive_interior_count"] == 309
    (out / "STRESS.json").write_bytes(B(st))
    refined = copy.deepcopy(seed)
    for group, pair in zip(protected, [[18, 94], [87, 127]]):
        f = next(i for i, cy in enumerate(refined["faces"]) if set(cy) == set(group))
        cy = refined["faces"][f]
        i = cy.index(pair[0])
        cy = cy[i:] + cy[:i]
        j = cy.index(pair[1])
        first = cy[: j + 1]
        second = cy[j:] + [cy[0]]
        assert len(first) == len(second) == 3
        refined["faces"][f] = first
        refined["faces"].append(second)
    refined["edges"] = sorted(
        {
            tuple(sorted((i, j)))
            for cy in refined["faces"]
            for i, j in zip(cy, cy[1:] + cy[:1])
        }
    )
    rs = chart_audit.verify_geometry(Q, refined)
    assert rs["zero_endpoint_pairs"] == [[18, 94], [71, 109], [87, 127]]
    (out / "REFINED_STRESS.json").write_bytes(B(rs))
    dualedges = set()
    for u, v in after["edges"]:
        ff = [f for f, cy in enumerate(after["faces"]) if u in cy and v in cy]
        assert len(ff) == 2
        dualedges.add(tuple(ff))
    assert dualedges == set(map(tuple, seed["edges"])) - {(71, 109)}
    conn = connectivity(after["F"], dualedges)
    assert conn == 9454
    result = dict(
        removed_owner_sets=removed,
        added_owner_sets=added,
        protected=[
            dict(owners=g, before=old[frozenset(g)], after=new[frozenset(g)])
            for g in protected
        ],
        merged_vertex=new[frozenset(added[0])],
        stable_faces=after["stable_face_ids"],
        unstable_vertices=after["unstable_vertices"],
        stable_cycle=after["faces"][3],
        degree_histogram=dict(Counter(map(len, new))),
        facet_histogram=dict(Counter(map(len, after["faces"]))),
        zero_stresses=rs["zero_endpoint_pairs"],
        zero_stress_indices=rs["zero_edges"],
        weight_bits=rs["weight_bits"],
        three_connectivity_checks=conn,
        files={
            p.name: dict(
                bytes=p.stat().st_size,
                sha256=hashlib.sha256(p.read_bytes()).hexdigest(),
            )
            for p in out.iterdir()
            if p.is_file()
        },
    )
    (out / "EXTRA.json").write_bytes(B(result))
    print(
        "C624_FULL_CONTACT_LINEAGE_STRESS_INVERSE_PASS", json.dumps(result), flush=True
    )
    return result


if __name__ == "__main__":
    verify(sys.argv[1], sys.argv[2], sys.argv[3])
