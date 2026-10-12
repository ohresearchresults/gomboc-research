#!/usr/bin/env python3
"""Deterministic optional stress locator; numerical outcomes are not proofs."""
import sys,json,time
from pathlib import Path
import numpy as np
from h5_extension import find,write_json
idx=int(sys.argv[1]);maxcalls=int(sys.argv[2])if len(sys.argv)>2 else 100
B=np.load(f'/mnt/data/upper_tensor_{idx}.npy');C=np.load('/mnt/data/tree_cache.npz')
Ts=C['Ts'];masks=C['masks'];roots=C['roots'];covered=C['geom'].copy();tried=np.zeros(len(Ts),bool)
records=[];fails=[];out=Path(f'/mnt/data/upper_{idx}_proposals.json');start=time.time()
if out.exists():
    old=json.loads(out.read_text());records=old['records'];fails=old['failures']
    for row in records:
        m=np.uint64(sum(1<<i for i,w in row));covered|=(masks&m)==m
    for f in fails:tried[f['tree']]=True
for n in range(maxcalls):
    ids=np.flatnonzero(~covered&~tried)
    if not len(ids):break
    t=int(ids[0]);tried[t]=True;aa=Ts[t];w,info=find(B[:,aa])
    if w is not None:
        ws=np.rint(w*10**8).astype(int);row=[(int(a),int(v))for a,v in zip(aa,ws)if v>0]
        low=float(np.linalg.eigvalsh(sum(v*B[:,a]for a,v in row))[:,0].min()/sum(v for a,v in row))
        if low>2e-10:
            records.append(row);m=np.uint64(sum(1<<i for i,w in row));covered|=(masks&m)==m
        else:fails.append({'tree':t,'info':info,'rounded_min':low})
    else:fails.append({'tree':t,'info':info})
    write_json(out,{'triangle_index':idx,'records':records,'failures':fails,'covered':int(covered.sum()),'elapsed':time.time()-start})
    if (n+1)%10==0:print(idx,n+1,'rows',len(records),'covered',int(covered.sum()),'failed',len(fails),'seconds',round(time.time()-start,2),flush=True)
print('DONE',idx,'rows',len(records),'covered',int(covered.sum()),'failed',len(fails),'seconds',round(time.time()-start,2),flush=True)
