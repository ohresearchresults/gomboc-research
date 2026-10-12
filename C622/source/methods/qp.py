"""Small dense infeasible-start primal-dual predictor-corrector convex QP.
This numerical proposal solver does not participate in exact acceptance.
"""

import numpy as np
import scipy.linalg as la


def solve(A, lo, hi, lb, ub, cost, maxiter=80, tol=1e-8):
    n = len(lb)
    eye = np.eye(n)
    A = np.vstack((A, eye))
    lo = np.r_[lo, lb]
    hi = np.r_[hi, ub]
    eq = np.isfinite(hi) & (lo == hi)
    il = np.isfinite(lo) & ~eq
    ih = np.isfinite(hi) & ~eq
    E = A[eq]
    b = lo[eq]
    G = np.vstack((-A[il], A[ih]))
    h = np.r_[-lo[il], hi[ih]]
    scale = np.maximum(1.0, np.linalg.norm(G, axis=1))
    G = G / scale[:, None]
    h = h / scale
    scale = np.maximum(1.0, np.linalg.norm(E, axis=1))
    E = E / scale[:, None]
    b = b / scale
    p = cost**2
    m = len(h)
    x = np.zeros(n)
    y = np.zeros(len(b))
    s = np.maximum(1.0, h - G @ x)
    z = np.ones(m)

    def maxstep(v, d):
        t = d < 0
        return min(1.0, float(np.min(-v[t] / d[t]))) if np.any(t) else 1.0

    for it in range(maxiter):
        rd = p * x + G.T @ z + E.T @ y
        rp = G @ x + s - h
        re = E @ x - b
        mu = float(s @ z / m)
        primal = max(np.max(np.abs(rp)), np.max(np.abs(re)) if len(re) else 0.0)
        dual = np.max(np.abs(rd))
        err = max(primal, dual, mu)
        if primal < tol and mu < tol:
            v = A @ x
            if max(np.max(lo - v), np.max(v - hi)) < 1e-6:
                return x, None
        if not np.isfinite(err) or mu > 1e20:
            return None, "QP diverged"
        D = z / s
        K = np.diag(p) + (G.T * D) @ G
        try:
            cho = la.cho_factor(K, lower=True, check_finite=False)
            KE = la.cho_solve(cho, E.T, check_finite=False)
            Schur = E @ KE

            def direction(rc):
                rhs = -rd + G.T @ (rc / s - D * rp)
                u = la.cho_solve(cho, rhs, check_finite=False)
                dy = (
                    la.solve(Schur, E @ u + re, assume_a="sym", check_finite=False)
                    if len(b)
                    else np.zeros(0)
                )
                dx = u - KE @ dy
                ds = -rp - G @ dx
                dz = (-rc - z * ds) / s
                return dx, dy, ds, dz

            dx, dy, ds, dz = direction(s * z)
            ap = maxstep(s, ds)
            ad = maxstep(z, dz)
            muaff = float((s + ap * ds) @ (z + ad * dz) / m)
            sigma = min(1.0, max(0.0, (muaff / mu) ** 3))
            dx, dy, ds, dz = direction(s * z + ds * dz - sigma * mu)
            ap = min(1.0, 0.995 * maxstep(s, ds))
            ad = min(1.0, 0.995 * maxstep(z, dz))
            x += ap * dx
            s += ap * ds
            y += ad * dy
            z += ad * dz
        except (la.LinAlgError, ValueError, FloatingPointError) as ex:
            return (
                None,
                f"QP numerical factorization it={it} error={err:g} primal={primal:g} dual={dual:g} mu={mu:g}: {ex}",
            )
        if min(s.min(), z.min()) <= 0:
            return None, "QP lost interior"
    return (
        None,
        f"QP iteration limit error={err:g} primal={primal:g} dual={dual:g} mu={mu:g}",
    )


if __name__ == "__main__":
    A = np.array([[1.0, 1.0]])
    lo = np.array([1.0])
    hi = np.array([np.inf])
    lb = np.array([0.0, 0.0])
    ub = np.array([2.0, 2.0])
    x, e = solve(A, lo, hi, lb, ub, np.array([1.0, 2.0]))
    assert e is None and np.max(abs(x - [0.8, 0.2])) < 1e-7
    print("QP_TEST", x)
