"""Faithful inverse-pole avoiding height rescale; an actual physical projectivity.
A single positive Maxwell stress scaling is gauge in a normalized chart but NOT
here: unnormalized height changes the inverse projective body, whose mass must
be recomputed. Used only for numerical seed creation, never as a mass assignment.
"""

import numpy as np


def seed(chart, weights):
    try:
        return chart.solve(weights)[0], dict(height_scale=1.0)
    except ValueError as e:
        if str(e) != "inverse pole":
            raise
    # Recover r,h through the same Dirichlet and dual-tree equations without inverse.
    import scipy.linalg as la

    wi = weights[chart.ie]
    L = (chart.Bi * wi) @ chart.Bi.T
    rhs = -((chart.Bi * wi) @ chart.Bb.T) @ chart.rb
    r = np.empty((chart.n, 2))
    r[chart.boundary] = chart.rb
    r[chart.inner] = la.solve(L, rhs, assume_a="pos", check_finite=False)
    e = r[chart.edges[chart.ie, 1]] - r[chart.edges[chart.ie, 0]]
    J = e[:, ::-1] * [-1, 1]
    off = -np.einsum("ij,ij->i", J, r[chart.edges[chart.ie, 0]])
    planes = chart.T @ (wi[:, None] * np.column_stack((J, off)))
    h = np.einsum("ij,ij->i", planes[chart.vf], np.column_stack((r, np.ones(chart.n))))
    h -= np.column_stack((r, np.ones(chart.n))) @ (chart.Ainv @ h[chart.boundary])
    h[chart.boundary] = 0
    h *= chart.R[:, 2].sum() / h.sum()
    alpha = min(1.0, 0.9 / (-h / chart.delta).max())
    h *= alpha
    den = 1 + h / chart.delta
    assert den.min() > 0
    Q = chart.c + (np.column_stack((r, h)) @ chart.basis) / den[:, None]
    return Q, dict(
        height_scale=float(alpha), minimum_inverse_denominator=float(den.min())
    )
