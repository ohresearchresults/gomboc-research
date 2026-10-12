# Adapted from parent independent verify.py; only input, zero-moment test,
# rational constant sign arithmetic, report fields and generic ray changed.
"""Independent exact audit of the polyhedron in this directory.

The script consumes only exact_polyhedron.npz and root.json. It reconstructs
the geometric and mechanical acceptance facts instead of trusting stored
classifications.
"""
from __future__ import annotations

from collections import defaultdict, deque
from itertools import combinations
from pathlib import Path
import hashlib
import json
import math
import os

import numpy as np
import csv,gzip


BASE = Path(os.environ.get("GOMBOC_AUDIT_DIR", Path(__file__).parent))
OUT = BASE / "verification_second.json"


def sha256(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


# Interface-only rational adaptation: read literal centred bigint CSV.
# B is identically zero, so every inherited predicate is constant.
with gzip.open(BASE / "vertices.csv.gz", "rt") as f:
    I = np.array([list(map(int,row)) for row in csv.reader(f)],dtype=object)
with gzip.open(BASE / "triangles.csv.gz", "rt") as f:
    F = np.array([list(map(int,row)) for row in csv.reader(f)],dtype=np.int64)
B = np.zeros(len(I),dtype=object)

n_vertices = len(I)
n_triangles = len(F)

assert len(set(map(tuple,I.tolist()))) == n_vertices
assert np.all(F[:, 0] != F[:, 1]) and np.all(F[:, 1] != F[:, 2]) and np.all(F[:, 2] != F[:, 0])
assert len(np.unique(np.sort(F, axis=1), axis=0)) == n_triangles

def algebraic_sign(p0: int, p1: int = 0, p2: int = 0) -> int:
    assert p1 == p2 == 0, "rational adapter received nonconstant polynomial"
    return (p0>0)-(p0<0)

# Reintegrate oriented tetrahedra to verify that the algebraic root is the
# centroid condition, rather than merely an unrelated quadratic.
volume = [0, 0]
moment_x = [0, 0, 0]
moment_y = [0, 0]
moment_z = [0, 0]
for ii, jj, kk in F:
    i, j, k = int(ii), int(jj), int(kk)
    xi, yi, zi = map(int, I[i])
    xj, yj, zj = map(int, I[j])
    xk, yk, zk = map(int, I[k])
    bi, bj, bk = int(B[i]), int(B[j]), int(B[k])
    yz_i = yj * zk - zj * yk
    yz_j = yk * zi - zk * yi
    yz_k = yi * zj - zi * yj
    det0 = xi * yz_i + xj * yz_j + xk * yz_k
    det1 = -(bi * yz_i + bj * yz_j + bk * yz_k)
    volume[0] += det0
    volume[1] += det1
    sx0, sx1 = xi + xj + xk, -(bi + bj + bk)
    moment_x[0] += det0 * sx0
    moment_x[1] += det0 * sx1 + det1 * sx0
    moment_x[2] += det1 * sx1
    moment_y[0] += det0 * (yi + yj + yk)
    moment_y[1] += det1 * (yi + yj + yk)
    moment_z[0] += det0 * (zi + zj + zk)
    moment_z[1] += det1 * (zi + zj + zk)

assert moment_x == [0,0,0]
assert moment_y == [0, 0] and moment_z == [0, 0]
assert algebraic_sign(*volume) > 0


# Rebuild the oriented edge incidence from triangles rather than trusting E/EF.
occurrences: dict[tuple[int, int], list[tuple[int, int, int]]] = defaultdict(list)
for fi, (ii, jj, kk) in enumerate(F):
    i, j, k = int(ii), int(jj), int(kk)
    occurrences[tuple(sorted((i, j)))].append((fi, i, j))
    occurrences[tuple(sorted((j, k)))].append((fi, j, k))
    occurrences[tuple(sorted((k, i)))].append((fi, k, i))
n_edges = len(occurrences)
assert n_vertices - n_edges + n_triangles == 2
for pair in occurrences.values():
    assert len(pair) == 2
    assert pair[0][1] == pair[1][2] and pair[0][2] == pair[1][1]

# Recompute connectedness, one-cycle vertex links, positive radial orientation,
# and the degree of the radial map using a ray different from the source audit.
links: list[dict[int, int]] = [dict() for _ in range(n_vertices)]
vertex_neighbors: list[set[int]] = [set() for _ in range(n_vertices)]
positive_radial_triangles = 0
for ii, jj, kk in F:
    i, j, k = int(ii), int(jj), int(kk)
    for x, y, z in ((i, j, k), (j, k, i), (k, i, j)):
        assert y not in links[x]
        links[x][y] = z
        vertex_neighbors[x].update((y, z))
    xi, yi, zi = map(int, I[i])
    xj, yj, zj = map(int, I[j])
    xk, yk, zk = map(int, I[k])
    det0 = xi * (yj * zk - zj * yk) + xj * (yk * zi - zk * yi) + xk * (yi * zj - zi * yj)
    det1 = -(int(B[i]) * (yj * zk - zj * yk) + int(B[j]) * (yk * zi - zk * yi) + int(B[k]) * (yi * zj - zi * yj))
    assert algebraic_sign(det0, det1) > 0
    positive_radial_triangles += 1

for vertex, link in enumerate(links):
    assert len(link) >= 3
    start = next(iter(link))
    current = start
    count = 0
    while True:
        current = link[current]
        count += 1
        if current == start:
            break
        assert count <= len(link)
    assert count == len(link)

seen_vertices = {0}
todo_vertices = deque([0])
while todo_vertices:
    vertex = todo_vertices.popleft()
    for neighbor in vertex_neighbors[vertex]:
        if neighbor not in seen_vertices:
            seen_vertices.add(neighbor)
            todo_vertices.append(neighbor)
assert len(seen_vertices) == n_vertices

audit_ray = (3, 11, 17)
def ray_edge_sign(i: int, j: int) -> int:
    xi, yi, zi = map(int, I[i])
    xj, yj, zj = map(int, I[j])
    bi, bj = int(B[i]), int(B[j])
    p0 = audit_ray[0] * (yi * zj - zi * yj) + audit_ray[1] * (zi * xj - xi * zj) + audit_ray[2] * (xi * yj - yi * xj)
    p1 = audit_ray[1] * (-zi * bj + bi * zj) + audit_ray[2] * (-bi * yj + yi * bj)
    return algebraic_sign(p0, p1)

radial_preimages = 0
ray_boundary_signs = 0
for ii, jj, kk in F:
    i, j, k = int(ii), int(jj), int(kk)
    signs = (ray_edge_sign(j, k), ray_edge_sign(k, i), ray_edge_sign(i, j))
    ray_boundary_signs += signs.count(0)
    if min(signs) > 0:
        radial_preimages += 1
assert ray_boundary_signs == 0
assert radial_preimages == 1

# Recompute all coplanar diagonals and maximal-face components from coordinates.
parent = list(range(n_triangles))


def find(x: int) -> int:
    while parent[x] != x:
        parent[x] = parent[parent[x]]
        x = parent[x]
    return x


def union(x: int, y: int) -> None:
    x, y = find(x), find(y)
    if x != y:
        parent[y] = x


def normal_poly(face: np.ndarray) -> tuple[tuple[int, int], tuple[int, int], tuple[int, int]]:
    i, j, k = map(int, face)
    x, y, z = map(int, I[i])
    xx, yy, zz = map(int, I[j])
    xxx, yyy, zzz = map(int, I[k])
    dx, dy, dz = xx - x, yy - y, zz - z
    ex, ey, ez = xxx - x, yyy - y, zzz - z
    db, eb = int(B[j] - B[i]), int(B[k] - B[i])
    return (
        (dy * ez - dz * ey, 0),
        (dz * ex - dx * ez, -dz * eb + db * ez),
        (dx * ey - dy * ex, -db * ey + dy * eb),
    )


def oriented_plane_sign(face_index: int, point_index: int) -> int:
    face = F[face_index]
    i = int(face[0])
    n = normal_poly(face)
    dx0 = int(I[point_index, 0] - I[i, 0])
    dx1 = -int(B[point_index] - B[i])
    dy = int(I[point_index, 1] - I[i, 1])
    dz = int(I[point_index, 2] - I[i, 2])
    return algebraic_sign(
        n[0][0] * dx0 + n[1][0] * dy + n[2][0] * dz,
        n[0][0] * dx1 + n[0][1] * dx0 + n[1][1] * dy + n[2][1] * dz,
        n[0][1] * dx1,
    )


independent_coplanar_keys: set[tuple[int, int]] = set()
strict_dihedral_edges = 0
for edge_key, pair in occurrences.items():
    (f0, _i, _j), (f1, _jj, _ii) = pair
    opposite = next(int(v) for v in F[f1] if int(v) not in edge_key)
    plane_sign = oriented_plane_sign(f0, opposite)
    assert plane_sign <= 0
    if plane_sign == 0:
        independent_coplanar_keys.add(edge_key)
        union(f0, f1)
    else:
        strict_dihedral_edges += 1

groups = np.array([find(fi) for fi in range(n_triangles)], dtype=np.int64)
coplanar_count = len(independent_coplanar_keys)
assert coplanar_count >= 0

# Independently verify that every merged maximal face has one simple boundary cycle.
group_to_faces: dict[int, list[int]] = defaultdict(list)
for fi, group in enumerate(groups):
    group_to_faces[int(group)].append(fi)

boundary_cycle_lengths: dict[int, int] = {}
for group, faces_in_group in group_to_faces.items():
    if len(faces_in_group) == 1:
        boundary_cycle_lengths[group] = 3
        continue
    adjacency: dict[int, list[int]] = defaultdict(list)
    boundary_edges = 0
    for edge_key, pair in occurrences.items():
        f0, f1 = pair[0][0], pair[1][0]
        g0, g1 = int(groups[f0]), int(groups[f1])
        if (g0 == group) == (g1 == group):
            continue
        u, v = edge_key
        adjacency[u].append(v)
        adjacency[v].append(u)
        boundary_edges += 1
    assert boundary_edges >= 3
    assert all(len(neighbors) == 2 for neighbors in adjacency.values())
    start = next(iter(adjacency))
    seen = {start}
    todo = deque([start])
    while todo:
        u = todo.popleft()
        for v in adjacency[u]:
            if v not in seen:
                seen.add(v)
                todo.append(v)
    assert len(seen) == len(adjacency) == boundary_edges
    boundary_cycle_lengths[group] = boundary_edges


def mul_linear(x: tuple[int, int], y: tuple[int, int]) -> tuple[int, int, int]:
    return x[0] * y[0], x[0] * y[1] + x[1] * y[0], x[1] * y[1]


def sub_quad(x: tuple[int, int, int], y: tuple[int, int, int]) -> tuple[int, int, int]:
    return x[0] - y[0], x[1] - y[1], x[2] - y[2]


def determinant_poly(n0, n1, n2) -> tuple[int, int, int]:
    yz = sub_quad(mul_linear(n1[1], n2[2]), mul_linear(n1[2], n2[1]))
    xz = sub_quad(mul_linear(n1[0], n2[2]), mul_linear(n1[2], n2[0]))
    xy = sub_quad(mul_linear(n1[0], n2[1]), mul_linear(n1[1], n2[0]))
    terms = []
    for coeff, quad in ((n0[0], yz), (n0[1], xz), (n0[2], xy)):
        # Multiplication is cubic in general, but every x component is constant;
        # the two potentially cubic terms cancel identically in a 3x3 determinant.
        terms.append((coeff[0] * quad[0], coeff[0] * quad[1] + coeff[1] * quad[0], coeff[0] * quad[2] + coeff[1] * quad[1], coeff[1] * quad[2]))
    cubic = terms[0][3] - terms[1][3] + terms[2][3]
    assert cubic == 0
    return (
        terms[0][0] - terms[1][0] + terms[2][0],
        terms[0][1] - terms[1][1] + terms[2][1],
        terms[0][2] - terms[1][2] + terms[2][2],
    )


# Every serialized vertex must be an actual 3D extreme point, not a point hidden
# in a polygonal face. Find an exact rank-3 triple of incident maximal-face normals.
representative = {group: faces[0] for group, faces in group_to_faces.items()}
incident_groups: list[set[int]] = [set() for _ in range(n_vertices)]
for fi, face in enumerate(F):
    group = int(groups[fi])
    for vertex in face:
        incident_groups[int(vertex)].add(group)

normal_cache = {group: normal_poly(F[fi]) for group, fi in representative.items()}
rank3_vertices = 0
for vertex, incident in enumerate(incident_groups):
    assert len(incident) >= 3
    normals = [normal_cache[group] for group in incident]
    found = False
    # Convex polyhedral vertices normally succeed on the first few triples.
    # The fallback is exhaustive and therefore cannot hide a degenerate vertex.
    for triple in combinations(normals, 3):
        p0, p1, p2 = determinant_poly(*triple)
        if algebraic_sign(p0, p1, p2) != 0:
            found = True
            break
    assert found, f"vertex {vertex} has normal rank below three"
    rank3_vertices += 1

# Recompute the equilibrium class directly from the algebraic coordinates.
# No signs or classifications from exact_global_mechanics_arrays.npz are used.
def face_edge_sign(normal, i: int, j: int) -> int:
    x, y, z = map(int, I[i])
    xx, yy, zz = map(int, I[j])
    bi, bj = int(B[i]), int(B[j])
    cx = y * zz - z * yy
    cy0, cy1 = z * xx - x * zz, -z * bj + bi * zz
    cz0, cz1 = x * yy - y * xx, -bi * yy + y * bj
    nx, ny, nz = normal
    return algebraic_sign(
        nx[0] * cx + ny[0] * cy0 + nz[0] * cz0,
        ny[0] * cy1 + ny[1] * cy0 + nz[0] * cz1 + nz[1] * cz0,
        ny[1] * cy1 + nz[1] * cz1,
    )


def vertex_edge_sign(i: int, j: int) -> int:
    x, y, z = map(int, I[i])
    xx, yy, zz = map(int, I[j])
    bi, bj = int(B[i]), int(B[j])
    dx, dy, dz = xx - x, yy - y, zz - z
    db = bj - bi
    return algebraic_sign(
        x * dx + y * dy + z * dz,
        -x * db - bi * dx,
        bi * db,
    )


face_min_sign = {group: 1 for group in group_to_faces}
vertex_max_sign = np.full(n_vertices, -2, dtype=np.int8)
recomputed_saddles = []
recomputed_degenerate_edges = []
true_edge_count = 0
for edge_key, pair in occurrences.items():
    (f0, i, j), (f1, jj, ii) = pair
    assert i == ii and j == jj
    g0, g1 = int(groups[f0]), int(groups[f1])
    if g0 == g1:
        continue
    true_edge_count += 1
    u = face_edge_sign(normal_cache[g0], i, j)
    v = face_edge_sign(normal_cache[g1], j, i)
    face_min_sign[g0] = min(face_min_sign[g0], u)
    face_min_sign[g1] = min(face_min_sign[g1], v)
    p, rsign = vertex_edge_sign(i, j), vertex_edge_sign(j, i)
    vertex_max_sign[i] = max(vertex_max_sign[i], p)
    vertex_max_sign[j] = max(vertex_max_sign[j], rsign)
    if p < 0 and rsign < 0 and u > 0 and v > 0:
        recomputed_saddles.append(edge_key)
    elif p <= 0 and rsign <= 0 and u >= 0 and v >= 0:
        recomputed_degenerate_edges.append(edge_key)

assert true_edge_count == n_edges - coplanar_count
recomputed_stable = sorted(group for group, sign_value in face_min_sign.items() if sign_value > 0)
recomputed_degenerate_faces = sorted(group for group, sign_value in face_min_sign.items() if sign_value == 0)
recomputed_unstable = np.flatnonzero(vertex_max_sign < 0).tolist()
recomputed_degenerate_vertices = np.flatnonzero(vertex_max_sign == 0).tolist()
assert len(recomputed_stable) == 1
assert len(recomputed_unstable) == 1
assert not recomputed_saddles
assert not recomputed_degenerate_faces
assert not recomputed_degenerate_vertices
assert not recomputed_degenerate_edges

stable_group = recomputed_stable[0]
report = {
    "status": "INDEPENDENT_EXACT_AUDIT_PASS",
    "vertices": n_vertices,
    "triangles": n_triangles,
    "triangulated_edges": n_edges,
    "maximal_faces": len(group_to_faces),
    "true_edges": n_edges - coplanar_count,
    "coplanar_diagonals_recomputed": coplanar_count,
    "strict_local_convexity_edges": strict_dihedral_edges,
    "euler_characteristic": n_vertices - n_edges + n_triangles,
    "rational_input": True,
    "centroid_x_exactly_zero": True,
    "centroid_yz_identically_zero": True,
    "oriented_volume_positive": True,
    "closed_oriented_two_manifold": True,
    "connected_vertices": len(seen_vertices),
    "single_cycle_vertex_links": n_vertices,
    "positive_radial_triangles": positive_radial_triangles,
    "independent_radial_ray": list(audit_ray),
    "independent_radial_degree": radial_preimages,
    "all_maximal_face_boundaries_single_cycles": True,
    "stable_face_boundary_cycle_length": boundary_cycle_lengths[stable_group],
    "vertices_with_exact_rank3_normal_cone": rank3_vertices,
    "independently_recomputed_exact_equilibrium_class": [
        len(recomputed_stable),
        len(recomputed_unstable),
        len(recomputed_saddles),
    ],
    "artifact_sha256": {
        name: sha256(BASE / name)
        for name in ("vertices.csv.gz", "triangles.csv.gz", "definition.json")
    },
}
OUT.write_text(json.dumps(report, indent=2) + "\n")
print(json.dumps(report, indent=2))
