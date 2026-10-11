"""Complete extracted helper unit; function bodies unchanged semantically."""
import os
import argparse, json, heapq, time
from pathlib import Path
import numpy as np
from scipy.linalg import svd
from coupled import Model
from qp_exec import minqp
from forest_search import freeze

def metric(m, a):
    idx = [j for j, (i, k) in enumerate(m.free) if i not in m.deleted]
    M = np.r_[(a['dx'] - a['dg']).reshape(-1, m.pdim), 0.05 * a['dq'].reshape(-1, m.pdim)][:, idx]
    _, s, V = svd(M, full_matrices=False, check_finite=False)
    T = np.zeros((m.pdim, len(idx)))
    T[idx] = V.T / np.sqrt(s * s + 1e-05)
    return T

def correct(m, z, level, beta, limit=15):
    trace = []

    def merit(a):
        return float(np.linalg.norm(np.minimum(0, np.r_[m.constr(a) - 2e-08, a['vert'][m.target_idx] - level])))
    for it in range(limit):
        a = m.eval(z, True)
        c = m.constr(a)
        t = a['vert'][m.target_idx]
        if c.min() >= 0 and np.min(t - level) >= -1e-09 and (a['min_det'] > 0) and (abs(a['allslack'][m.inc]).max() < 1e-09):
            return (z, a, True, trace)
        c, J = m.constr(a, deriv=True, geomask=a['geo'] < 0.04)
        T = metric(m, a)
        A = np.r_[J, a['dvert'][m.target_idx]] @ T
        b = np.r_[2e-08 - c, level - t]
        pref = np.zeros(T.shape[1])
        if it == 0 and beta:
            r = a['x'] - a['g']
            goal = m.target_idx[np.argmin(t)]
            eta = beta * float(np.max(level - t)) * m.vlens[goal] / (r[m.vi[goal]] @ r[m.vi[goal]])
            desired = np.zeros_like(r)
            desired[m.basin] = -eta * r[m.basin]
            pref = T.T @ np.einsum('vkp,vk->p', a['dx'] - a['dg'], desired)
        u, info = minqp(A, b - A @ pref)
        if u is None:
            trace.append(info)
            break
        u += pref
        dz = T @ u
        old = merit(a)
        alpha = 1.0
        ok = False
        for ls in range(18):
            try:
                zz = z + alpha * dz
                aa = m.eval(zz)
                new = merit(aa)
                if new < old * (1 - 0.0001 * alpha):
                    ok = True
                    break
            except (np.linalg.LinAlgError, FloatingPointError):
                pass
            alpha *= 0.5
        trace.append(dict(inner=it, targets=t.tolist(), cmin=float(c.min()), norm=float(np.linalg.norm(u)), alpha=alpha, merit=old, qp=info))
        if not ok or np.linalg.norm(alpha * u) > 0.3:
            break
        z = zz
    return (z, m.eval(z), False, trace)
