"""C96 physical cuts from polar escape chains, solving true volume-centre closure.

The older C282 capsule motivated this method, but C96 is the exact geometric
input. Each arc distributes its complete angular/radial escape budget, instead
of assuming a constant ratio works on a bowed arc. None of the numerical root
or face-grouping calculations is an exact equilibrium certificate.
"""
import argparse
import itertools
import json
import time
from pathlib import Path

import numpy as np
from scipy.optimize import root
from scipy.spatial import ConvexHull,QhullError

from geometry import baseline,census,escape_table,mass,write_json


def polar(q):
    hull=ConvexHull(q)
    d=-hull.equations[:,3]
    if min(d)<=1e-12:
        raise ValueError('Polar is unbounded or numerically unresolved')
    p=hull.equations[:,:3]/d[:,None]
    scale=max(np.linalg.norm(p,axis=1))
    _,keep=np.unique(np.round(p/scale,11),axis=0,return_index=True)
    return p[np.sort(keep)]


def main():
    ap=argparse.ArgumentParser()
    ap.add_argument('--out',required=True)
    ap.add_argument('--n',type=int,nargs='+',default=[12,16,24,36])
    ap.add_argument('--bow',type=float,nargs='+',default=[-1.,-.5,0.,.5,1.])
    ap.add_argument('--gain',type=float,nargs='+',default=[1.,1.25,1.5,2.])
    args=ap.parse_args()
    out=Path(args.out);out.mkdir(exist_ok=False)
    p=baseline();base=census(p,True);g=np.array(base['centroid'])
    # q at g defines normalized physical supports q.(x-g)<=1.
    q0=base['q'];normals=q0;offsets=1+q0@g
    ids=sorted(base['stable'],key=lambda i:np.linalg.norm(q0[i]))
    records=[];best={};start=time.time()
    for n,bow,gain,opposed,reverse in itertools.product(args.n,args.bow,args.gain,[False,True],[False,True]):
        pars=dict(n=n,bow=bow,gain=gain,opposed=opposed,reverse=reverse)

        def build(c):
            d=offsets-normals@c
            if min(d)<=1e-7:
                raise ValueError('Construction centre left the strict input body')
            q=normals/d[:,None]
            source,target=ids[::-1] if reverse else ids
            a=q[source];b=q[target]*gain
            ra,rb=np.linalg.norm(a),np.linalg.norm(b)
            u=a/ra;v=b/rb;cos=np.clip(u@v,-1.,1.);phi=np.arccos(cos)
            e=v-cos*u;e/=np.linalg.norm(e);w=np.cross(u,e)
            t=np.linspace(0.,1.,n+1)
            pieces=[q,b[None,:]]
            budgets=[]
            for angle in ([phi,phi-2*np.pi] if opposed else [phi]):
                directions=np.cos(angle*t)[:,None]*u+np.sin(angle*t)[:,None]*e
                directions+=bow*np.sin(np.pi*t)[:,None]*w
                directions/=np.linalg.norm(directions,axis=1)[:,None]
                cosines=np.einsum('ij,ij->i',directions[:-1],directions[1:])
                if min(cosines)<=0:
                    raise ValueError('Arc has a nonacute step')
                budget=np.log(rb/ra)+np.log(cosines).sum()
                # Negative budgets are retained as explicitly non-certified
                # proposals; positive budgets certify every arc escape at c.
                logr=np.log(ra)-np.r_[0.,np.cumsum(np.log(cosines))]+t*budget
                pieces.append(np.exp(logr[1:-1,None])*directions[1:-1])
                budgets.append(float(budget))
            return np.concatenate(pieces),budgets

        evaluations=0
        def residual(c):
            nonlocal evaluations
            evaluations+=1
            return mass(polar(build(c)[0]))[1]

        rec=dict(**pars)
        try:
            r=root(residual,g,method='hybr',options={'xtol':1e-10,'maxfev':150})
            q,budget=build(r.x);points=polar(q)
            rr=census(points)
            rec.update(root_status=int(r.status),nfev=evaluations,
                       closure=float(np.linalg.norm(residual(r.x))),
                       construction_centre=r.x.tolist(),arc_escape_log_budgets=budget,
                       **rr)
            key=(rr['S'],rr['U'])
            rank=(rr['S_uncertain']+rr['U_uncertain'],rr['E_proposal'],rec['closure'])
            if key not in best or rank<best[key]:
                best[key]=rank
                write_json(out/('BEST_%d_%d.json'%key),dict(record=rec,points=points.tolist(),supports=q.tolist()))
                print('BEST_CHAIN',len(records),key,rank,flush=True)
            if key==(1,1) and rr['S_uncertain']==rr['U_uncertain']==0:
                write_json(out/'PROPOSAL110.json',dict(record=rec,points=points.tolist(),supports=q.tolist()))
        except (ValueError,QhullError,AssertionError,np.linalg.LinAlgError) as error:
            rec.update(error=str(error),nfev=evaluations)
        records.append(rec)
        write_json(out/'SEARCH.json',dict(config=vars(args),records=records,elapsed=time.time()-start))
        if len(records)%20==0:
            print('CHAIN_CASES',len(records),'classes',sorted(best),flush=True)
        if (out/'PROPOSAL110.json').exists():
            break
    print('PHYSICAL_CHAIN_SEARCH_FINISHED',len(records),sorted(best),time.time()-start,flush=True)


if __name__=='__main__':
    main()
