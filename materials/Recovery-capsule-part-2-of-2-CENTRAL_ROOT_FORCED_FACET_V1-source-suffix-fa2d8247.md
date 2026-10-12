# material-fa2d82479f77

AI research material

---


def verify_incidence():
    position = {v:i for i,v in enumerate(PATH)}
    assert set(position) == set(range(10))
    edge_faces = {}
    for j,face in enumerate(FACETS):
        assert len(set(face)) == len(face) >= 3
        assert set(face) == {position[v] for v,row in enumerate(ROWS) if j in row}
        for i,v in enumerate(face):
            edge = tuple(sorted((v,face[(i+1)%len(face)])))
            edge_faces.setdefault(edge,[]).append(j)
    assert len(edge_faces) == 17
    assert all(len(fs) == 2 for fs in edge_faces.values())
    assert 10-len(edge_faces)+len(FACETS) == 2
    path_edges = {(i,i+1) for i in range(9)}
    assert path_edges <= set(edge_faces)
    complement = {tuple(sorted(fs)) for e,fs in edge_faces.items() if e not in path_edges}
    expected = {tuple(sorted((DUAL_PATH[i],DUAL_PATH[i+1]))) for i in range(8)}
    assert complement == expected
    windows = [set(DUAL_PATH[i:i+3]) for i in range(7)]
    assert {i for i,w in enumerate(windows) if any(w <= set(row) for row in ROWS)} == {1,2,4}
    assert (0,9) not in edge_faces
    for v in range(10):
        link = {}
        for face in FACETS:
            if v in face:
                i = face.index(v)
                a,b = face[i-1],face[(i+1)%len(face)]
                link.setdefault(a,set()).add(b)
                link.setdefault(b,set()).add(a)
        assert link and all(len(ns) == 2 for ns in link.values())
        seen,stack = set(),[next(iter(link))]
        while stack:
            a = stack.pop()
            if a not in seen:
                seen.add(a)
                stack.extend(link[a]-seen)
        assert seen == set(link)


def main():
    bounds = verify_pairs()
    print('PATH_PAIR_CERTIFICATES_EXACT_PASS',len(bounds))
    verify_incidence()
    triangles = tetrahedra = 0
    for root in (4,5):
        cases = Counter()
        for tri in combinations([v for v in range(10) if v != root],3):
            gap,kind = margin(root,tri,bounds)
            cases[kind] += 1
        assert cases == Counter(depth=79,pair45=2,pair34=1,pair35=1,exception=1)
        triangles += sum(cases.values())-cases['exception']
        count = 0
        for face in FACETS:
            if root in face:
                continue
            outside = set(face)-exception(root)
            assert outside
            for tri in fan(face,min(outside)):
                gap,kind = margin(root,tri,bounds)
                assert gap is not None and gap >= EPS
                count += 1
        assert count == {4:12,5:9}[root]
        tetrahedra += count
    assert triangles == 166 and tetrahedra == 21
    print('CENTRAL_ROOT_TRIANGLE_SCREEN_PASS',2,triangles)
    print('EXPLICIT_INCIDENCE_FANS_PASS',2,tetrahedra)
    print('VOLUME_CENTROID_MARGIN',str(EPS/4))
    print('NO_CENSUS_OR_GLOBAL_BOUND_UPDATE')


if __name__ == '__main__':
    main()
