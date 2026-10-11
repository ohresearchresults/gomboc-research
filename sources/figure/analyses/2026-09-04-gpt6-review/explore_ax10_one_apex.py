"""Compute moment closure for the mandatory four-face AX10 patch.

Symbolic equations are exact; numerical roots are discovery results only.
No numerical endpoint is promoted as a Goemboc certificate.
"""
import json
from pathlib import Path
import numpy as np
import sympy as s
from scipy.spatial import ConvexHull
from verify_ax10_centroid_obstruction import POINTS, LABELS, hull, mass

ROOT = Path(__file__).resolve().parent


def array(v):
    return np.array(v, dtype=float)


def numerical_mechanics(vertices):
    h = ConvexHull(vertices)
    # This discovery-only classifier supports simplicial hulls. A triangulation
    # diagonal in a polygonal maximal face must never be scored as a true edge.
    for i, plane in enumerate(h.equations):
        if any(np.max(np.abs(plane-other)) < 1e-8 for other in h.equations[:i]):
            raise ValueError('Nonsimplicial or unresolved near-coplanar hull: no mechanics verdict')
    normals = h.equations[:, :3]
    faces = []
    vol = 0.
    moment = np.zeros(3)
    edges = {}
    stable = []
    for i, (face, n) in enumerate(zip(h.simplices, normals)):
        a, b, c = vertices[face]
        if np.dot(np.cross(b-a, c-a), n) < 0:
            face = face[[0, 2, 1]]
            a, b, c = vertices[face]
        faces.append(face)
        dv = np.dot(a, np.cross(b, c))/6
        vol += dv
        moment += dv*(a+b+c)/4
    centroid = moment/vol
    x = vertices-centroid
    for i, face in enumerate(faces):
        a, b, c = x[face]
        n = normals[i]
        foot = n*np.dot(n, a)
        uv = np.linalg.lstsq(np.column_stack((b-a, c-a)), foot-a, rcond=None)[0]
        if min(uv[0], uv[1], 1-uv.sum()) > 1e-9:
            stable.append(list(map(int, face)))
        for j in range(3):
            e = tuple(sorted((int(face[j]), int(face[(j+1) % 3]))))
            edges.setdefault(e, []).append(i)
    unstable = []
    for i in h.vertices:
        neighbours = {b if a == i else a for a, b in edges if i in (a, b)}
        if min(np.dot(x[i], x[i]-x[j]) for j in neighbours) > 1e-9:
            unstable.append(int(i))
    saddles = []
    for (i, j), fs in edges.items():
        e = x[j]-x[i]
        t = -np.dot(x[i], e)/np.dot(e, e)
        p = x[i]+t*e
        beta = np.linalg.lstsq(normals[fs].T, p, rcond=None)[0]
        if min(t, 1-t, *beta) > 1e-9:
            saddles.append([i, j])
    if len(stable)+len(unstable)-len(saddles) != 2:
        raise ValueError('Numerical mechanics violates Euler: no mechanics verdict')
    return dict(centroid=centroid.tolist(), volume=vol, f_vector=[len(h.vertices), len(edges), len(faces)],
                equilibrium_class=[len(stable), len(unstable), len(saddles)], stable=stable,
                unstable=unstable, saddles=saddles)


def main():
    faces = hull(POINTS)
    volume, moment = mass(POINTS, faces)
    p = {k: s.Matrix(v) for k, v in POINTS.items()}
    C = p['C']
    patch = [(f, s.Matrix(n), s.Rational(h)) for f, n, h in faces if sum(n[j]*(-POINTS['C'][j]/3) for j in range(3)) > h]
    N = s.zeros(3, 1)
    H = s.S.Zero
    S = s.zeros(3, 3)
    b = -24*s.Matrix(moment)
    for f, n, h in patch:
        total = sum((p[k] for k in f), s.zeros(3, 1))
        N += n
        H += h
        S += total*n.T
        b += h*total
    d = s.Symbol('d')
    mat = d*s.eye(3)+S
    adj_b = mat.adjugate()*b
    determinant = mat.det()
    polynomial = s.Poly((d+H)*determinant-(N.T*adj_b)[0], d).clear_denoms()[1].primitive()[1]
    intervals = s.polys.polytools.intervals(polynomial, eps=s.Rational(1, 10**35))
    print('EXACT POLYNOMIAL DEGREE', polynomial.degree(), flush=True)
    print('REAL ROOT INTERVALS', [(str(a), str(z), m) for (a, z), m in intervals], flush=True)
    roots = []
    for (lo, hi), multiplicity in intervals:
        if hi <= 0:
            continue
        t = (lo+hi)/2
        if determinant.subs(d, t) == 0:
            continue
        y = adj_b.subs(d, t)/determinant.subs(d, t)
        yy = array(y).reshape(3)
        visible = [list(f) for f, n, h in faces if np.dot(array(n), yy) > float(h)+1e-10]
        signed = {frozenset(f) for f in visible} == {frozenset(f) for f, _, _ in patch}
        candidate = np.vstack([array(list(POINTS.values())), yy])
        result = dict(root_interval=[str(lo), str(hi)], apex=yy.tolist(), visibility_matches=signed,
                      visible_faces=visible, mechanics=numerical_mechanics(candidate))
        roots.append(result)
        print(json.dumps(result, indent=2), flush=True)
    (ROOT/'ax10-one-apex-exploration.json').write_text(json.dumps(dict(
        exact_polynomial_coefficients=[str(c) for c in polynomial.all_coeffs()],
        exact_cap_patch=[list(f) for f, _, _ in patch], candidates=roots,
        scope='Exact moment polynomial; root isolation exact; hull/mechanics numerical only. A failed intended visibility cell is not an exclusion of all one-apex cells.'), indent=2)+'\n')


if __name__ == '__main__':
    main()
