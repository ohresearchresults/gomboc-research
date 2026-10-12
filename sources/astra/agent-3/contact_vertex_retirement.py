"""Literal rational point retirements from a full-contact exact physical body.

Numerical hulls nominate finite subsets only. Every nominated low-count body
is reconstructed from the unchanged exact parent coordinates and audited.
"""
import argparse
import hashlib
import json
import time
from pathlib import Path

import numpy as np
from gmpy2 import mpq

from direct_face_polish import guards
from literal_vertex_subset import run as exact_subset
from vertex_geometry import geometry


def run(source, out, trials, number):
    source, out = Path(source), Path(out)
    out.mkdir(parents=True, exist_ok=False)
    a = json.loads((source/'audit.json').read_text())
    cq = tuple(map(mpq, a['raw_centroid']))
    X = np.array([[float(mpq(v)-cq[k]) for k,v in enumerate(x)]for x in a['raw_vertices']])
    n = len(X)
    root = int(np.argmax(np.sum(X*X,axis=1)))
    rng = np.random.default_rng(891276)
    ds = np.linalg.norm(X[:,None,:]-X[None,:,:],axis=2)
    nn = np.argsort(ds,axis=1)
    subsets = {(i,)for i in range(n)if i!=root}
    for i in range(n):
        for j in nn[i,1:7]:
            if root not in (i,int(j)):
                subsets.add(tuple(sorted((i,int(j)))))
    for _ in range(trials):
        i = int(rng.integers(n));size=int(rng.integers(3,11))
        pool=nn[i,:min(n,size*3)]
        pool=pool[pool!=root]
        ids=tuple(sorted(map(int,rng.choice(pool,size,replace=False))))
        subsets.add(ids)
    subsets=sorted(subsets,key=lambda ids:(len(ids),ids))
    rows=[];exact=[];t0=time.time()
    (out/'source.json').write_text(json.dumps(dict(source=str(source.resolve()),audit_sha256=hashlib.sha256((source/'audit.json').read_bytes()).hexdigest(),source_counts=a['counts'],trials=len(subsets),scope='literal subsets of exact physical vertices, all selected points retain their exact coordinates'),indent=2))
    for k,ids in enumerate(subsets):
        keep=np.delete(np.arange(n),ids)
        try:
            g=geometry(X[keep],False);v,_,cl=guards(g,False)
            row=dict(case=k,removed=list(ids),merit=float(np.maximum(1e-9-v,0).sum()),minimum=float(min(v)),**cl)
        except (ValueError,np.linalg.LinAlgError)as err:
            row=dict(case=k,removed=list(ids),error=repr(err))
        rows.append(row)
        if row.get('S')==row.get('U')==1:
            d=out/f'exact_nomination{k}'
            aa=exact_subset(source,keep,d)
            exact.append(dict(case=k,exact=str(d.resolve()),**{z:aa[z]for z in ['V','E','F','counts','weak']}))
        if k%250==0:
            valid=[r for r in rows if 'error'not in r]
            print('CONTACT_VERTEX_RETIRE_SCREEN',k,len(subsets),'minimum_count',min(r['S']+r['U']for r in valid),'seconds',time.time()-t0,flush=True)
    (out/'screen.json').write_text(json.dumps(rows,indent=2))
    valid=[r for r in rows if 'error'not in r]
    valid.sort(key=lambda r:(r['S']+r['U'],r['U']!=1,r['merit'],len(r['removed'])))
    (out/'ranked.json').write_text(json.dumps(valid[:100],indent=2))
    done={r['case']for r in exact}
    for row in valid[:number]:
        k=row['case']
        if k in done:
            continue
        keep=np.delete(np.arange(n),row['removed']);d=out/f'exact_ranked{k}'
        aa=exact_subset(source,keep,d)
        rr=dict(case=k,exact=str(d.resolve()),**{z:aa[z]for z in ['V','E','F','counts','weak']})
        exact.append(rr);(out/'exact_results.json').write_text(json.dumps(exact,indent=2))
        print('CONTACT_VERTEX_RETIRE_EXACT',rr,flush=True)
    (out/'exact_results.json').write_text(json.dumps(exact,indent=2))


if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('source');p.add_argument('out');p.add_argument('--trials',type=int,default=1500);p.add_argument('--exact',type=int,default=12);a=p.parse_args();run(a.source,a.out,a.trials,a.exact)
