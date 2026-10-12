"""Bounded alternating primal additions and physical polar cuts at own COM."""
import argparse
import itertools
import json
import time
from pathlib import Path

import numpy as np
from scipy.spatial import QhullError

from geometry import baseline,census,escape_table,mass,write_json
from physical_chains import polar


def complete(y,gain,bow,maxn=60):
    radii=np.linalg.norm(y,axis=1)
    root=int(np.argmax(radii))
    sources=np.flatnonzero(escape_table(y).max(axis=1)<-1e-9)
    dest=y[root]*gain
    end=np.linalg.norm(dest)
    pieces=[y,dest[None,:]]
    recipe=[]
    for source in sources:
        if source==root:
            continue
        a=y[source];start=np.linalg.norm(a);u=a/start;v=dest/end
        cos=np.clip(u@v,-1.,1.);phi=np.arccos(cos);e=v-cos*u
        if np.linalg.norm(e)<1e-10:
            k=int(np.argmin(abs(u)));e=np.eye(3)[k]-(np.eye(3)[k]@u)*u
        e/=np.linalg.norm(e);w=np.cross(u,e)
        for n in range(3,maxn+1):
            t=np.linspace(0,1,n+1)
            d=np.cos(t*phi)[:,None]*u+np.sin(t*phi)[:,None]*e
            d+=bow*np.sin(np.pi*t)[:,None]*w
            d/=np.linalg.norm(d,axis=1)[:,None]
            cc=np.einsum('ij,ij->i',d[:-1],d[1:])
            if min(cc)<=0:
                continue
            budget=np.log(end/start)+np.log(cc).sum()
            if budget>.02:
                lr=np.log(start)-np.r_[0.,np.cumsum(np.log(cc))]+t*budget
                pieces.append(np.exp(lr[1:-1,None])*d[1:-1])
                recipe.append(dict(source=int(source),root=root,n=n,escape_budget=float(budget)))
                break
        else:
            raise ValueError('Finite chain budget exhausted')
    return np.concatenate(pieces),recipe


def main():
    ap=argparse.ArgumentParser();ap.add_argument('--out',required=True)
    ap.add_argument('--rounds',type=int,default=30);ap.add_argument('--input')
    args=ap.parse_args();out=Path(args.out);out.mkdir(exist_ok=False)
    base=baseline() if args.input is None else np.array(json.loads(Path(args.input).read_text())['points'])
    runs=[];best={};start=time.time()
    for gain,bow,mode in itertools.product([1.1,1.35,1.8,2.5],[-.5,0.,.5],[0,1]):
        p=base.copy();history=[]
        for step in range(args.rounds):
            r=census(p,True);p=p-np.array(r['centroid']);p/=max(np.linalg.norm(p,axis=1))
            r=census(p,True)
            key=(r['S'],r['U']);score=(r['E_proposal'],step)
            if key not in best or score<best[key]:
                best[key]=score
                rr=census(p)
                write_json(out/('BEST_%d_%d.json'%key),dict(gain=gain,bow=bow,mode=mode,step=step,census=rr,points=p.tolist()))
                print('ALTERNATE_BEST',key,score,flush=True)
            if key==(1,1) and r['S_uncertain']==r['U_uncertain']==0:
                write_json(out/'PROPOSAL110.json',dict(points=p.tolist(),census=census(p)))
                break
            if r['V']>150 or r['F']>150 or r['E_proposal']>310:
                history.append(dict(step=step,stopped='explicit complexity bound',V=r['V'],F=r['F'],E=r['E_proposal']))
                break
            try:
                side='S' if ((step+mode)%2==0 and r['S']>1) or r['U']==1 else 'U'
                if side=='S':
                    q,recipe=complete(r['q'],gain,bow)
                    p=polar(q)
                else:
                    p,recipe=complete(p,gain,bow)
                history.append(dict(step=step,side=side,S=r['S'],U=r['U'],E=r['E_proposal'],recipe=recipe))
            except (ValueError,QhullError,AssertionError,np.linalg.LinAlgError) as error:
                history.append(dict(step=step,error=str(error)));break
        runs.append(dict(gain=gain,bow=bow,mode=mode,history=history,points=p.tolist()))
        write_json(out/'SEARCH.json',dict(config=vars(args),runs=runs,elapsed=time.time()-start))
        if (out/'PROPOSAL110.json').exists():
            break
    print('ALTERNATING_CHAIN_FINISHED',len(runs),sorted(best),time.time()-start,flush=True)


if __name__=='__main__':
    main()
