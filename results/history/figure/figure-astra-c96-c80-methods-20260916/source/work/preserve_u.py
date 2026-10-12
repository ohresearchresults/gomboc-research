"""Finite whole-body S/H cancellation while retaining strict U=1 witnesses.

All non-root raw points must have a positive normalized radial escape to another
raw point relative to the ACTUAL solid centroid. Such arrows strictly increase
radius and imply a unique unstable vertex at the protected root if feasible.
The exact audit remains the only acceptance gate.
"""
import argparse
import json
import time
from pathlib import Path

import numpy as np
from scipy.optimize import minimize
from scipy.spatial import QhullError

from geometry import baseline, census, escape_table, mass, persistence, write_json


def main():
    ap=argparse.ArgumentParser()
    ap.add_argument('--out',required=True)
    ap.add_argument('--input')
    ap.add_argument('--root',type=int,default=14)
    ap.add_argument('--extra',type=int,default=0)
    ap.add_argument('--starts',type=int,default=3)
    ap.add_argument('--iterations',type=int,default=400)
    ap.add_argument('--margin',type=float,default=.001)
    args=ap.parse_args()
    out=Path(args.out)
    out.mkdir(exist_ok=False)
    p=baseline() if args.input is None else np.array(json.loads(Path(args.input).read_text())['points'])
    p-=mass(p)[1]
    p/=max(np.linalg.norm(p,axis=1))
    rng=np.random.default_rng(96016)
    if args.extra:
        added=[]
        for k in range(args.extra):
            weights=rng.dirichlet(np.ones(len(p)))
            added.append(weights@p)
        p=np.r_[p,added]
    initial_volume=mass(p)[0]
    protect=np.array([i for i in range(len(p)) if i!=args.root])
    total=0
    best=float('inf')
    allruns=[]
    starttime=time.time()
    for run in range(args.starts):
        if run==0:
            seed=p.copy()
        else:
            seed=np.array(json.loads((out/'BEST.json').read_text())['points']) if (out/'BEST.json').exists() else p.copy()
            seed+=rng.normal(size=p.shape)*[.015,.06,.015]
        cache={}

        def evaluate(t):
            nonlocal total,best
            if 't' in cache and np.array_equal(t,cache['t']):
                return cache['score'],cache['constraints']
            total+=1
            points=t.reshape(p.shape)
            try:
                r=census(points,True)
                x=points-np.array(r['centroid'])
                escapes=escape_table(x).max(axis=1)[protect]
                scale=max(np.einsum('ij,ij->i',x,x))
                score=persistence(r['q'])/scale
                constraints=np.r_[escapes-args.margin,r['volume']/initial_volume-.7]
                if min(constraints)>=-1e-7 and score<best:
                    best=score
                    rr=census(points)
                    rec=dict(run=run,score=score,nfev=total,elapsed=time.time()-starttime,
                             minimum_constraint=float(min(constraints)),census=rr,
                             points=points.tolist())
                    write_json(out/'BEST.json',rec)
                    if total%500<4:
                        print('BEST',run,total,score,rr['S'],rr['U'],rr['E_proposal'],flush=True)
                    if rr['S']==rr['U']==1 and rr['S_uncertain']==rr['U_uncertain']==0:
                        write_json(out/'PROPOSAL110.json',rec)
            except (QhullError,ValueError,AssertionError,np.linalg.LinAlgError):
                score=10.
                constraints=np.full(len(protect)+1,-10.)
            cache.update(t=t.copy(),score=score,constraints=constraints)
            return score,constraints

        r=minimize(lambda t:evaluate(t)[0],seed.ravel(),method='SLSQP',
                   bounds=[(-2.,2.)]*seed.size,
                   constraints={'type':'ineq','fun':lambda t:evaluate(t)[1]},
                   options={'maxiter':args.iterations,'ftol':1e-11,'eps':1e-7})
        score,con=evaluate(r.x)
        rec=dict(run=run,score=score,nit=int(r.nit),message=str(r.message),
                 minimum_constraint=float(min(con)),census=census(r.x.reshape(p.shape)),
                 points=r.x.reshape(p.shape).tolist())
        write_json(out/('ENDPOINT_'+str(run)+'.json'),rec)
        allruns.append({k:v for k,v in rec.items() if k!='points'})
        write_json(out/'SEARCH.json',dict(config=vars(args),runs=allruns,nfev=total,
                                        elapsed=time.time()-starttime,best_feasible=best))
        print('PRESERVE_U_RUN_END',run,score,min(con),rec['census']['S'],rec['census']['U'],r.message,flush=True)
        if (out/'PROPOSAL110.json').exists():
            break
    print('PRESERVE_U_FINISHED',total,best,time.time()-starttime,flush=True)


if __name__=='__main__':
    main()
