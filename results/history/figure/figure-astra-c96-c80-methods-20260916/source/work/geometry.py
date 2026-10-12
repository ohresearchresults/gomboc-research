"""Numerical proposals only; all accepted objects must pass the exact core.

ConvexHull triangular diagonals are merged by supporting plane for screening.
The own uniform filled-volume centroid is recomputed for every call.
"""
import json
from pathlib import Path

import numpy as np
from scipy.spatial import ConvexHull
from scipy.sparse.csgraph import minimum_spanning_tree

ROOT = Path(__file__).resolve().parents[1]


def write_json(path, value):
    Path(path).write_text(json.dumps(value, sort_keys=True, indent=2) + "\n")


def baseline():
    p = np.array(json.loads((ROOT / 'input/POINTS25.json').read_text())['points'], float)
    n = np.array([4., 11., 0.])
    for i in range(len(p)):
        if i != 15:
            p[i] -= n * (p[i] @ n) / 137
    axes = np.array([[11., -4., 0.], [4., 11., 0.], [0., 0., np.sqrt(137)]]) / np.sqrt(137)
    return p @ axes.T / 1000


def mass(p):
    p = np.asarray(p, float)
    hull = ConvexHull(p)
    anchor = p[hull.vertices].mean(axis=0)
    t = p[hull.simplices] - anchor
    cross = np.cross(t[:, 1] - t[:, 0], t[:, 2] - t[:, 0])
    orient = np.sign(np.einsum('ij,ij->i', cross, hull.equations[:, :3]))
    det = np.einsum('ij,ij->i', t[:, 0], np.cross(t[:, 1], t[:, 2])) * orient
    assert det.min() > 0
    volume = det.sum() / 6
    g = anchor + (det[:, None] * t.sum(axis=1)).sum(axis=0) / (4 * det.sum())
    return volume, g, hull


def escape_table(x):
    delta = x[None, :, :] - x[:, None, :]
    dots = np.einsum('ik,ijk->ij', x, delta)
    divisor = np.linalg.norm(x, axis=1)[:, None] * np.linalg.norm(delta, axis=2)
    values = dots / np.maximum(divisor, 1e-300)
    np.fill_diagonal(values, -np.inf)
    return values


def census(p, details=False):
    volume, g, hull = mass(p)
    pv = np.asarray(p)[hull.vertices]
    x = pv - g
    n = hull.equations[:, :3]
    distance = -hull.equations[:, 3] - n @ g
    assert distance.min() > 0
    qtri = n / distance[:, None]
    # Strictly numerical face merging. Every retained final body is audited exactly.
    qscale = np.maximum(np.linalg.norm(qtri, axis=1), 1.)
    same = (np.linalg.norm(qtri[:, None] - qtri[None, :], axis=2)
            <= 1e-9 * np.maximum(qscale[:, None], qscale[None, :]))
    keep = []
    groups = []
    assigned = np.zeros(len(qtri), bool)
    for i in range(len(qtri)):
        if not assigned[i]:
            group = np.flatnonzero(same[i] & ~assigned)
            keep.append(i)
            groups.append(group.tolist())
            assigned[group] = True
    q = qtri[keep]
    ut = escape_table(x)
    st = escape_table(q)
    u = ut.max(axis=1)
    s = st.max(axis=1)
    r = dict(V=len(pv), F=len(q), E_proposal=len(pv)+len(q)-2,
             S=int((s < -1e-9).sum()), U=int((u < -1e-9).sum()),
             S_uncertain=int((np.abs(s) <= 1e-9).sum()),
             U_uncertain=int((np.abs(u) <= 1e-9).sum()),
             stable=[j for j in range(len(q)) if s[j] < -1e-9],
             unstable=hull.vertices[u < -1e-9].tolist(),
             s_values=s.tolist(), u_values=u.tolist(),
             centroid=g.tolist(), volume=float(volume))
    if details:
        r.update(q=q, x=x, hull=hull, st=st, ut=ut, groups=groups)
    return r


def loss(p, margin=1e-4):
    r = census(p, True)
    # Removing only the lowest minimum lets the surviving stable/U migrate.
    s = np.sort(r['s_values'])[1:]
    u = np.sort(r['u_values'])[1:]
    return float(np.sum(np.minimum(s-margin, 0.)**2) + np.sum(np.minimum(u-margin, 0.)**2))


def persistence(y):
    """Complete spherical-cap graph finite-bar sum; numerical objective only."""
    delta = y[None, :, :] - y[:, None, :]
    ee = np.einsum('ijk,ijk->ij', delta, delta)
    ze = np.einsum('ik,ijk->ij', y, delta)
    t = np.clip(-ze / np.maximum(ee, 1e-300), 0., 1.)
    z = y[:, None, :] + t[:, :, None]*delta
    zz = np.einsum('ijk,ijk->ij', z, z)
    weights = 1/np.maximum(zz,1e-300)
    np.fill_diagonal(weights,0.)
    births = 1/np.einsum('ij,ij->i', y, y)
    tree = minimum_spanning_tree(weights)
    return max(0., float(tree.sum()-births.sum()+births.min()))


def barrier_loss(p):
    r = census(p, True)
    x,q = r['x'],r['q']
    rmax = np.max(np.einsum('ij,ij->i',x,x))
    qmax = np.max(np.einsum('ij,ij->i',q,q))
    ratio = 1/np.sqrt(rmax*qmax)
    # Prevent lower-dimensional escape of this scale-invariant objective.
    return persistence(q)/rmax + persistence(x)/qmax + 10*max(0., .08-ratio)**2


if __name__ == '__main__':
    p = baseline()
    r = census(p)
    write_json(ROOT/'work/baseline-numeric.json', dict(points=p.tolist(), **r))
    print(json.dumps(r, indent=2))
