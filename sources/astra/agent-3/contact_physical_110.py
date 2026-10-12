"""Physical face-foot and vertex-edge inequalities in an exact contact family.

Each independent control defines one rationally reproducible physical body.
All mass derivatives are those of the filled body. Strict hull incidence and
equilibria are decided by the native exact audit, never by a small residual.
"""
import argparse
import json
import time
from pathlib import Path

import numpy as np
from scipy.optimize import linprog
from scipy.sparse import csr_matrix, eye, hstack, vstack

from contact_numpy import Chart
from contact_quota_polish import metric
from direct_face_polish import cross_derivative
from exact_contact_audit import audit
from exact_barcode_report import report
from goal_nomination import ExactGoalCandidateFound


class PhysicalGuards:
    def __init__(self, c, angular_vertices=False):
        self.c = c
        self.angular_vertices = angular_vertices
        self.f = np.concatenate([np.full(len(cy), f, int) for f, cy in enumerate(c.faces)])
        self.a = np.concatenate([np.array(cy, int) for cy in c.faces])
        self.b = np.concatenate([np.roll(np.array(cy, int), -1) for cy in c.faces])
        self.starts = np.r_[0, np.cumsum([len(cy) for cy in c.faces])]
        adj = [set() for _ in range(c.V)]
        for i, j in c.pe:
            adj[i].add(j)
            adj[j].add(i)
        self.vi = np.concatenate([np.full(len(a), i, int) for i, a in enumerate(adj)])
        self.vj = np.concatenate([np.array(sorted(a), int) for a in adj])
        self.vstarts = np.r_[0, np.cumsum([len(a) for a in adj])]
        self.tf = np.concatenate([np.full(len(cy) - 2, f, int) for f, cy in enumerate(c.faces)])

    def evaluate(self, g):
        Z, DZ, X, DX, Y, DY = (g[k] for k in ('Z', 'DZ', 'X', 'DX', 'Y', 'DY'))
        R2 = np.mean(np.sum(Z * Z, axis=1))
        R = np.sqrt(R2)
        DR2 = 2 * np.mean(np.einsum('ic,icp->ip', Z, DZ), axis=0)
        DR = DR2 / (2 * R)
        yl = np.linalg.norm(Y, axis=1)
        n = Y / yl[:, None]
        Dn = (DY - n[:, :, None] * np.einsum('ic,icp->ip', n, DY)[:, None, :]) / yl[:, None, None]
        e = X[self.b] - X[self.a]
        De = DX[self.b] - DX[self.a]
        ell = np.linalg.norm(e, axis=1)
        if min(ell) <= 0 or not np.isfinite(ell).all():
            raise ValueError('undefined face edge')
        t = np.cross(n[self.f], e) / ell[:, None]
        Dt = cross_derivative(n[self.f], Dn[self.f], e, De) / ell[:, None, None]
        Dt -= t[:, :, None] * np.einsum('ic,icp->ip', e, De)[:, None, :] / ell[:, None, None] ** 2
        fs = np.einsum('ic,ic->i', t, Z[self.a]) / R
        Dfs = (np.einsum('icp,ic->ip', Dt, Z[self.a]) + np.einsum('ic,icp->ip', t, DZ[self.a])) / R
        Dfs -= fs[:, None] * DR / R
        fi = np.array([l + np.argmax(fs[l:r]) for l, r in zip(self.starts[:-1], self.starts[1:])])
        vf, JF = fs[fi], Dfs[fi]
        ve = X[self.vj] - X[self.vi]
        Dve = DX[self.vj] - DX[self.vi]
        vs = np.einsum('ic,ic->i', Z[self.vi], ve) / R2
        Dvs = (np.einsum('icp,ic->ip', DZ[self.vi], ve) + np.einsum('ic,icp->ip', Z[self.vi], Dve)) / R2
        Dvs -= vs[:, None] * DR2 / R2
        if self.angular_vertices:
            zr2 = np.sum(Z[self.vi] ** 2, axis=1)
            er2 = np.sum(ve ** 2, axis=1)
            denom = np.sqrt(zr2 * er2)
            vs = np.einsum('ic,ic->i', Z[self.vi], ve) / denom
            Dvs = (np.einsum('icp,ic->ip', DZ[self.vi], ve) + np.einsum('ic,icp->ip', Z[self.vi], Dve)) / denom[:, None]
            Dvs -= vs[:, None] * (np.einsum('ic,icp->ip', Z[self.vi], DZ[self.vi]) / zr2[:, None] + np.einsum('ic,icp->ip', ve, Dve) / er2[:, None])
        ui = np.array([l + np.argmax(vs[l:r]) for l, r in zip(self.vstarts[:-1], self.vstarts[1:])])
        vu, JU = vs[ui], Dvs[ui]
        sr = int(np.argmax(np.sum(g['H'] ** 2, axis=1)))
        ur = int(np.argmax(np.sum(Z ** 2, axis=1)))
        fm, um = np.arange(self.c.F) != sr, np.arange(self.c.V) != ur
        v = np.r_[vu[um], vf[fm]]
        J = np.vstack((JU[um], JF[fm]))
        T = self.c.T
        ta, tb = X[T[:, 1]] - X[T[:, 0]], X[T[:, 2]] - X[T[:, 0]]
        Dta, Dtb = DX[T[:, 1]] - DX[T[:, 0]], DX[T[:, 2]] - DX[T[:, 0]]
        cr = np.cross(ta, tb)
        Dcr = cross_derivative(ta, Dta, tb, Dtb)
        turn = np.einsum('ic,ic->i', cr, Y[self.tf]) / R
        Dturn = (np.einsum('icp,ic->ip', Dcr, Y[self.tf]) + np.einsum('ic,icp->ip', cr, DY[self.tf])) / R - turn[:, None] * DR / R
        info = dict(S=int(sum(vf < 0)), U=int(sum(vu < 0)), stable_root=sr, unstable_root=ur,
                    min_S=float(min(vf[fm])), min_U=float(min(vu[um])))
        return v, J, turn, Dturn, info


def freeze(c, q, out):
    out = Path(out)
    out.mkdir(parents=True, exist_ok=False)
    np.save(out / 'literal_controls.npy', q)
    grid = max(float(z).as_integer_ratio()[1] for z in q)
    a = audit(c.path, out / 'literal_controls.npy', out / 'exact_dyadic', grid)
    report(out / 'exact_dyadic')
    strict = a['counts'] == [1, 1, 0] and a['weak'] == [0, 0, 0]
    if strict and 34 <= 2 * a['E'] < 500 and a['V'] + a['E'] + a['F'] < 500:
        raise ExactGoalCandidateFound('Exact physical contact Figure: ' + str(out))
    return a, strict


def realize(source, out, steps=400, eps=1e-9, start_q=None, angular_vertices=False):
    c = Chart(source)
    out = Path(out)
    out.mkdir(parents=True, exist_ok=False)
    q = c.q0.copy() if start_q is None else np.load(start_q)
    G = PhysicalGuards(c, angular_vertices)
    (out / 'source_construction.json').write_bytes(Path(source).read_bytes())
    np.save(out / 'initial_q.npy', q)
    (out / 'method.json').write_text(json.dumps(dict(source=str(Path(source).resolve()), start_q=None if start_q is None else str(Path(start_q).resolve()), epsilon=eps, angular_vertices=angular_vertices, gap_floor=1e-11, turn_floor=1e-12, scope='simultaneous direct physical strict equilibrium and full convex contact realization; all admitted results exactly audited'), indent=2))
    trust = .03
    history = []
    t0 = time.time()
    for it in range(steps):
        g = c.physical(q, require_valid=False)
        v, J, turn, JT, cl = G.evaluate(g)
        val = np.r_[g['noncontact'], turn, v]
        tar = np.r_[np.full(len(g['noncontact']), 1e-11), np.full(len(turn), 1e-12), np.full(len(v), eps)]
        merit = float(np.maximum(tar - val, 0).sum())
        row = dict(it=it, merit=merit, trust=trust, seconds=time.time()-t0, valid=bool(g['valid']), gap=float(min(g['noncontact'])), turn=float(min(turn)), **cl)
        history.append(row)
        np.save(out / 'latest_q.npy', q)
        (out / 'trace.json').write_text(json.dumps(history, indent=2))
        if it % 10 == 0:
            print('PHYSICAL_CONTACT_110', out, row, flush=True)
        if g['valid'] and cl['S'] == cl['U'] == 1:
            a, strict = freeze(c, q, out / f'nomination_it{it}')
            row['exact_counts'] = a['counts']
            row['exact_weak'] = a['weak']
            if strict:
                np.save(out / 'success_q.npy', q)
                (out / 'success.json').write_text(json.dumps(row, indent=2))
                return out / f'nomination_it{it}' / 'exact_dyadic'
        W = metric(c, g)
        JJ = np.vstack((g['Dgap'][~c.incidence], JT, J)) @ W
        d = c.d
        bound = trust / np.sqrt(d)
        keep = val - tar <= bound * np.sum(abs(JJ), axis=1) + 1e-9
        JJ, vv, tt = JJ[keep], val[keep], tar[keep]
        m = len(vv)
        I, O = eye(d), csr_matrix((d, m))
        sc = .001
        A = vstack([hstack([-csr_matrix(JJ / sc), -eye(m), csr_matrix((m, d))]),
                    hstack([I, O, -I]), hstack([-I, O, -I])], format='csr')
        b = np.r_[(vv - tt) / sc, np.zeros(2*d)]
        r = linprog(np.r_[np.zeros(d), np.ones(m), np.full(d, 1e-5)], A_ub=A, b_ub=b,
                    bounds=[(-bound, bound)]*d + [(0, None)]*(m+d), method='highs',
                    options=dict(primal_feasibility_tolerance=1e-10, dual_feasibility_tolerance=1e-10, time_limit=15.))
        if not r.success:
            row['error'] = r.message
            trust *= .4
        else:
            dq = W @ r.x[:d]
            ok = False
            for k in range(15):
                qq = q + 2.**-k * dq
                try:
                    gg = c.physical(qq, require_valid=False)
                    v2, _, t2, _, cc = G.evaluate(gg)
                    mm = float(np.maximum(tar - np.r_[gg['noncontact'], t2, v2], 0).sum())
                except (ValueError, np.linalg.LinAlgError):
                    continue
                if gg['valid'] and cc['S'] == cc['U'] == 1:
                    a, strict = freeze(c, qq, out / f'nomination_it{it}_line{k}')
                    if strict:
                        np.save(out / 'success_q.npy', qq)
                        (out / 'success.json').write_text(json.dumps(dict(it=it, alpha=2.**-k, counts=a['counts'], weak=a['weak']), indent=2))
                        return out / f'nomination_it{it}_line{k}' / 'exact_dyadic'
                if np.isfinite(mm) and mm < merit - max(1e-14, merit * 1e-8):
                    q, ok = qq, True
                    row['alpha'] = 2.**-k
                    break
            if ok and k == 0:
                trust = min(.3, trust * 1.3)
            if not ok:
                trust *= .4
        if trust < 1e-11:
            break
    np.save(out / 'endpoint_q.npy', q)
    print('PHYSICAL_CONTACT_FINITE_FAILURE', out, history[-1], flush=True)
    return None


if __name__ == '__main__':
    p = argparse.ArgumentParser()
    p.add_argument('source')
    p.add_argument('out')
    p.add_argument('--steps', type=int, default=400)
    p.add_argument('--epsilon', type=float, default=1e-9)
    p.add_argument('--start-q')
    p.add_argument('--angular-vertices', action='store_true')
    a = p.parse_args()
    realize(a.source, a.out, a.steps, a.epsilon, a.start_q, a.angular_vertices)
