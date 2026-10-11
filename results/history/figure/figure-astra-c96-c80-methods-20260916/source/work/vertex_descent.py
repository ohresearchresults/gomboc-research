"""Unrestricted, bounded full-vertex basin-barrier descent.

This implements the complete cap-graph objective derived in the literal journal
entry 2026-09-05T20:07:37.692Z. The source geometry remains the exact C96 body.
It is a numerical proposal generator, not an equilibrium certificate.
"""
import argparse
import json
import time
from pathlib import Path

import numpy as np
from scipy.optimize import minimize
from scipy.spatial import QhullError

from geometry import baseline, barrier_loss, census, write_json, mass


def normalize(p):
    p = p-mass(p)[1]
    return p/np.max(np.linalg.norm(p,axis=1))


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--out',required=True)
    parser.add_argument('--input',action='append',default=[])
    parser.add_argument('--iterations',type=int,default=300)
    parser.add_argument('--random',type=int,default=8)
    parser.add_argument('--seed',type=int,default=9616)
    args = parser.parse_args()
    out = Path(args.out)
    out.mkdir(exist_ok=False)
    p = baseline()
    rng = np.random.default_rng(args.seed)
    seeds = [('baseline',normalize(p)), ('polar',normalize(census(p,True)['q']))]
    for name in args.input:
        seeds.append((name,normalize(np.array(json.loads(Path(name).read_text())['points']))))
    for k in range(args.random):
        z = p.copy()
        z[:,1] *= np.exp(rng.uniform(0.,3.3))
        z += rng.normal(size=z.shape)*rng.uniform(.03,.15)
        seeds.append(('random-'+str(k),normalize(z)))
    runs = []
    best = float('inf')
    classbest = {}
    total = 0
    start = time.time()
    for name,seed in seeds:
        evaluations = 0
        milestones = []
        shape = seed.shape

        def objective(t):
            nonlocal evaluations,total,best
            evaluations += 1
            total += 1
            points = t.reshape(shape)
            try:
                score = barrier_loss(points)
            except (ValueError,QhullError,AssertionError,np.linalg.LinAlgError):
                return 10.
            if score < best:
                best = score
                r = census(points)
                rec = dict(seed=name,loss=score,nfev=total,elapsed=time.time()-start,
                           census=r,points=points.tolist())
                write_json(out/'BEST.json',rec)
                key = str(r['S'])+'-'+str(r['U'])
                if r['S_uncertain']==r['U_uncertain']==0 and score<classbest.get(key,float('inf')):
                    classbest[key]=score
                    write_json(out/('BEST_'+key+'.json'),rec)
                milestones.append({k:v for k,v in rec.items() if k not in ('points','census')})
                if total%100 < 3 or len(milestones)%50 == 1:
                    print('BEST',name,total,score,r['S'],r['U'],r['E_proposal'],flush=True)
                if r['S']==r['U']==1 and r['S_uncertain']==r['U_uncertain']==0:
                    write_json(out/'PROPOSAL110.json',rec)
            return score

        result = minimize(objective,seed.ravel(),method='L-BFGS-B',
                          bounds=[(-2.,2.)]*seed.size,
                          options={'maxiter':args.iterations,'maxfun':120000,
                                   'ftol':1e-13,'gtol':1e-8,'maxls':35,'eps':1e-7})
        rec = dict(seed=name,fun=float(result.fun),nit=int(result.nit),nfev=evaluations,
                   message=str(result.message),census=census(result.x.reshape(shape)),
                   points=result.x.reshape(shape).tolist(),milestones=milestones)
        write_json(out/('ENDPOINT_'+str(len(runs))+'.json'),rec)
        runs.append({k:v for k,v in rec.items() if k not in ('points','milestones')})
        write_json(out/'SEARCH.json',dict(config=vars(args),runs=runs,nfev=total,
                                        best=best,elapsed=time.time()-start))
        print('RUN_END',name,result.fun,result.nit,evaluations,rec['census']['S'],rec['census']['U'],flush=True)
        if (out/'PROPOSAL110.json').exists():
            break
    print('VERTEX_DESCENT_FINISHED',len(runs),total,best,time.time()-start,flush=True)


if __name__ == '__main__':
    main()
