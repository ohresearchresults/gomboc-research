"""Exact C626-to-C622 maximal incidence, atlas inverse, and common stress audit."""

from VERIFY_EXTRA import *


def verify(parent_root, child_audit, out):
    parent_root = Path(parent_root)
    child_audit = Path(child_audit)
    out = Path(out)
    out.mkdir(parents=True, exist_ok=False)
    seed = chart.recover(root=parent_root)
    before = json.load(open(parent_root / "baseline/A.json"))
    after = json.load(open(child_audit / "A.json"))
    raw = json.load(open(child_audit / "raw.json"))
    G = json.load(open(child_audit / "GENERATOR.json"))
    aa = atlas(G, raw, after)
    (out / "ATLAS.json").write_bytes(B(aa))
    old, new = owners(before), owners(after)
    removed = sorted([sorted(o) for o in old.keys() - new.keys()])
    added = sorted([sorted(o) for o in new.keys() - old.keys()])
    assert removed == [
        [56, 57, 88, 118],
        [71, 94, 109, 119],
        [71, 109, 116, 126],
        [88, 118, 122],
    ]
    assert added == [[56, 57, 88, 118, 122], [71, 94, 109, 116, 119, 126]]
    protected = [[16, 18, 71, 94], [87, 108, 122, 127]]
    assert all(frozenset(g) in new for g in protected)
    assert (
        [after[k] for k in ["V", "E", "F"]] == [176, 311, 137]
        and after["counts"] == [1, 1, 0]
        and after["weak"] == [0, 0, 0]
    )
    assert after["active_input_indices"] == list(range(137))
    Q = [tuple(F(v, row[3]) for v in row[:3]) for row in raw["H"]]
    st = chart_audit.verify_geometry(Q, seed)
    assert (
        st["zero_endpoint_pairs"] == [[71, 109], [88, 118]]
        and st["positive_interior_count"] == 308
    )
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
    assert rs["zero_endpoint_pairs"] == [[18, 94], [71, 109], [87, 127], [88, 118]]
    (out / "REFINED_STRESS.json").write_bytes(B(rs))
    dualedges = set()
    for u, v in after["edges"]:
        ff = [f for f, cy in enumerate(after["faces"]) if u in cy and v in cy]
        assert len(ff) == 2
        dualedges.add(tuple(ff))
    assert dualedges == set(map(tuple, seed["edges"])) - {(71, 109), (88, 118)}
    conn = connectivity(after["F"], dualedges)
    assert conn == 9454
    result = dict(
        removed_owner_sets=removed,
        added_owner_sets=added,
        protected=[
            dict(owners=g, before=old[frozenset(g)], after=new[frozenset(g)])
            for g in protected
        ],
        merged_vertices=[dict(owners=g, index=new[frozenset(g)]) for g in added],
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
        "C622_FULL_CONTACT_LINEAGE_STRESS_INVERSE_PASS", json.dumps(result), flush=True
    )
    return result


if __name__ == "__main__":
    verify(sys.argv[1], sys.argv[2], sys.argv[3])
