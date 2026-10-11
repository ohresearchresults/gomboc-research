"""Complete extracted helper unit; function bodies unchanged semantically."""
import os
import argparse, json, time
from pathlib import Path
import numpy as np
from scipy.linalg import svd
from scipy.optimize import linprog, minimize
from coupled import Model

def metric(m, a):
    idx = [j for j, (i, k) in enumerate(m.free) if i not in m.deleted]
    M = np.r_[a['dx'].reshape(-1, m.pdim), 0.2 * a['dq'].reshape(-1, m.pdim)][:, idx]
    _, s, V = svd(M, full_matrices=False, check_finite=False)
    T = np.zeros((m.pdim, len(idx)))
    T[idx] = V.T / np.sqrt(s * s + 1e-05)
    return T
from qp_exec import minqp

def freeze(m, z, file, grid=10 ** 13):
    out = json.loads(json.dumps(m.gen))
    out['controls'] = [[0, 0, 0] for _ in out['controls']]
    out['grid'] = grid
    for (i, k), v in zip(m.free, z):
        out['controls'][i][k] = int(round(float(v) * grid))
    Path(file).write_text(json.dumps(out, sort_keys=True, separators=(',', ':')))
