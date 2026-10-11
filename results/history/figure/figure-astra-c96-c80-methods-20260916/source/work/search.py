"""Bounded numerical constructive searches starting from the exact C96 pyramid.

Every output is a proposal. The saved loss never replaces the exact census.
Run with one BLAS thread and one scipy worker.
"""
import argparse
import json
import time
from pathlib import Path

import numpy as np
from scipy.optimize import differential_evolution, minimize
from scipy.spatial import QhullError

from geometry import ROOT, baseline, census, loss, barrier_loss, mass, write_json


def affine(p, t):
    a = np.array([[np.exp(t[0]), t[2], t[3]],
                  [0., np.exp(t[1]), t[4]], [0., 0., 1.]])
    return p @ a.T


def construct(p, t, mode):
    if mode == 'apex':
        out = p.copy()
        out[15] = [t[0], -np.exp(t[1]), t[2]]
        return out
    if mode == 'affine':
        return affine(p, t)
    if mode == 'projective':
        den = 1 + p @ t[5:8]
        if den.min() < .04:
            raise ValueError('Projective horizon too close')
        return affine(p / den[:, None], t[:5])
    if mode == 'bend':
        out = p.copy()
        x,z = p[:, 0], p[:, 2]
        out[:, 1] += t[5]*x*x + t[6]*x*z + t[7]*z*z + t[8]*x*x*z + t[9]*x*z*z
        return affine(out, t[:5])
    if mode == 'add':
        return affine(np.r_[p, np.array(t[5:]).reshape(-1,3)], t[:5])
    raise ValueError(mode)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('mode', choices=['apex','affine','projective','bend','add'])
    ap.add_argument('--seed', type=int, default=96)
    ap.add_argument('--iterations', type=int, default=90)
    ap.add_argument('--population', type=int, default=8)
    ap.add_argument('--restarts', type=int, default=3)
    ap.add_argument('--extra', type=int, default=1)
    ap.add_argument('--out', required=True)
    ap.add_argument('--polar', action='store_true')
    ap.add_argument('--barrier', action='store_true')
    ap.add_argument('--input')
    args = ap.parse_args()
    out = Path(args.out)
    out.mkdir(exist_ok=False)
    p = baseline()
    if args.input:
        p = np.array(json.loads(Path(args.input).read_text())['points'])
    if args.polar:
        p = census(p,True)['q']
        p /= np.max(np.linalg.norm(p,axis=1))
    bounds = [(-2., 2.5), (-1., 4.), (-4., 4.), (-3., 3.), (-3., 3.)]
    if args.mode == 'apex':
        bounds = [(-1.4,1.4),(-5.,1.),(-1.5,1.5)]
    if args.mode == 'projective':
        bounds += [(-1.2,1.2),(-8.,8.),(-1.3,1.3)]
    if args.mode == 'bend':
        bounds += [(-1.8,1.8)]*5
    if args.mode == 'add':
        bounds += [(-.9,.9),(-.7,.7),(-.9,.9)]*args.extra
    best = float('inf')
    nfev = 0
    history = []
    start = time.time()

    def objective(t):
        nonlocal best,nfev
        nfev += 1
        try:
            points = construct(p,t,args.mode)
            value = barrier_loss(points) if args.barrier else loss(points)
        except (ValueError, QhullError, AssertionError, np.linalg.LinAlgError):
            return 10.
        if value < best:
            best = value
            r = census(points)
            rec = dict(parameters=t.tolist(), loss=value, census=r, nfev=nfev,
                       elapsed=time.time()-start, points=points.tolist())
            write_json(out/'BEST.json',rec)
            history.append({k:v for k,v in rec.items() if k!='points'})
            if r['S'] == r['U'] == 1 and r['S_uncertain'] == r['U_uncertain'] == 0:
                write_json(out/'PROPOSAL110.json',rec)
            print('BEST',args.mode,nfev,value,r['S'],r['U'],r['E_proposal'],flush=True)
        return value

    for restart in range(args.restarts):
        r = differential_evolution(objective,bounds,seed=args.seed+restart,
                                   maxiter=args.iterations,popsize=args.population,
                                   workers=1,polish=False,tol=1e-9,atol=1e-12)
        rr = minimize(objective,r.x,method='Powell',bounds=bounds,
                      options={'maxiter':70,'maxfev':8000,'ftol':1e-12,'xtol':1e-8})
        history.append(dict(restart=restart,de_fun=float(r.fun),polish_fun=float(rr.fun),
                            de_message=str(r.message),polish_message=str(rr.message)))
        write_json(out/'SEARCH.json',dict(config=vars(args),bounds=bounds,
                                        nfev=nfev,history=history,elapsed=time.time()-start))
        if (out/'PROPOSAL110.json').exists():
            break
    print('SEARCH_FINISHED',args.mode,nfev,best,time.time()-start,flush=True)


if __name__ == '__main__':
    main()
