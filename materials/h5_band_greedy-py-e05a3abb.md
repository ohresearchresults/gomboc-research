# material-e05a3abb1d1c

AI research material

<!-- historical-status:start -->
> **Historical AI material.** The title and claims below reflect the AI’s assessment at the time. Claims of proof, certification or completion are not a current verification verdict.
>
> [C622](../C622/README.md) passes the supplied exact checks; C<500 remains open; Minimum’s C≥34 remains a working lower bound requiring a consolidated proof. See [verification status and source gaps](../catalog/coverage.md).
<!-- historical-status:end -->

---

#!/usr/bin/env python3
"""Numerical all-tree stress proposals. No proof or physical survivor claim."""
from pathlib import Path
from itertools import combinations
import time,json,contextlib,io,hashlib
import numpy as np
import h5_original_band as h
EDGES=tuple(sorted({tuple(sorted((a,b)))for f in h.FACES for a,b in zip(f,f[1:]+f[:1])}))
ARROWS=tuple(e for a,b in EDGES for e in ((a,b),(b,a)));AID={e:i for i,e in enumerate(ARROWS)}
def trees():
    answer=[]
    for choice in combinations(range(17),9):
        parent=list(range(10));adj=[[]for _ in range(10)];ok=True
        def root(a):
            while parent[a]!=a:a=parent[a]
            return a
        for ei in choice:
            a,b=EDGES[ei];ra,rb=root(a),root(b)
            if ra==rb:ok=False;break
            parent[ra]=rb;adj[a].append(b);adj[b].append(a)
        if not ok:continue
        for r in range(10):
            todo=[r];seen={r};out=[]
            for a in todo:
                for b in adj[a]:
                    if b not in seen:seen.add(b);todo.append(b);out.append(AID[(b,a)])
            assert len(out)==9
            mask=sum(1<<i for i in out);answer.append((mask,r,tuple(sorted(out))))
    assert len(answer)==48790 and len({a for a,_,_ in answer})==48790
    return sorted(answer)

def all_tensor():
    h.TREE=ARROWS;G=h.geometry()
    keys=sorted({k for row in G for p in row for k in p.d})
    coeff=np.array([[[p.d.get(k,h.F(0))for p in row]for row in G]for k in keys],float)
    U=[{(i,k):h.univ(a,b,n,i,k)for i in range(n+1)for k in range(n+1)}for(a,b),n in zip(h.BOX,h.DEG)]
    tb={(i,j,a,b):h.F(h.comb(i,a)*h.comb(j,b),h.comb(3,a+b)*h.comb(a+b,a))if a<=i and b<=j else h.F(0)for i,j in h.TRI for a in range(4)for b in range(4-a)}
    trans=np.array([[U[0][ix,k[0]]*U[1][ir,k[1]]*tb[ip,iq,k[2],k[3]]*U[2][il,k[4]]for k in keys]for ix,ir,(ip,iq),il in h.INDICES],float)
    vals=np.einsum('ak,kbc->abc',trans,coeff);mats=np.zeros((800,34,3,3))
    for a,(i,j)in enumerate(h.PAIRS):mats[:,:,i,j]=vals[:,:,a];mats[:,:,j,i]=vals[:,:,a]
    return G,mats

def main():
    import argparse
    ap=argparse.ArgumentParser();ap.add_argument('--calls',type=int,default=60);ap.add_argument('--out',type=Path,default=Path('h5_band_greedy_candidates.json'));args=ap.parse_args()
    start=time.time();ts=trees();masks=np.array([a for a,_,_ in ts],dtype=np.uint64);ids=np.array([c for _,_,c in ts]);G,B=all_tensor()
    left=np.ones(len(ts),bool);failed=[];records=[];basecalls=0
    if args.out.exists():
        previous=json.loads(args.out.read_text());records=previous['records'];failed=previous['failed'];basecalls=previous['calls']
        for rec in records:left[(masks&int(rec['support']))==int(rec['support'])]=False
        for rec in failed:left[rec['tree_index']]=False
    for it in range(args.calls):
        todo=np.where(left)[0]
        if not len(todo):break
        ti=int(todo[0]);inds=ids[ti]
        with contextlib.redirect_stdout(io.StringIO()):w,meta=h.find(B[:,inds],maxiter=50)
        if w is None or meta.get('min_eigenvalue',-1)<1e-9:
            failed.append({'tree_index':ti,'root':ts[ti][1],'arrows':list(map(int,inds)),'meta':meta});left[ti]=False
        else:
            numer=np.rint(w*10**10).astype(np.int64);numer[numer<0]=0
            wr=numer/numer.sum();ev=np.linalg.eigvalsh(np.einsum('neij,e->nij',B[:,inds],wr)).min()
            if ev<=1e-9:
                failed.append({'tree_index':ti,'meta':{'rounding_gap':float(ev)}});left[ti]=False
            else:
                support=int(sum(1<<int(e)for e,v in zip(inds,numer)if v));hit=(masks&support)==support
                covered=int(np.sum(left&hit));left[hit]=False
                records.append({'arrows':list(map(int,inds)),'numerators':list(map(int,numer)),'sum':int(numer.sum()),'support':support,'numeric_gap':float(ev),'covered_new':covered,'meta':meta})
        out={'scope':'Numerical candidate cover only; no exact pass or physical survivor claim.','arrows':ARROWS,'tree_count':len(ts),'records':records,'failed':failed,'unprocessed_tree_indices':np.where(left)[0].tolist(),'calls':basecalls+it+1,'elapsed_last_batch':time.time()-start}
        args.out.write_text(json.dumps(out,separators=(',',':'))+'\n')
        if it%10==0 or not np.any(left):print('GREEDY',basecalls+it+1,'STRESSES',len(records),'LEFT',int(left.sum()),'FAIL',len(failed),'SECONDS',round(time.time()-start,2),flush=True)
    if not args.out.exists():raise RuntimeError('No checkpoint produced')
    normalized=json.loads(args.out.read_text())
    normalized['unprocessed_count']=len(normalized.pop('unprocessed_tree_indices'))
    normalized.pop('elapsed_last_batch',None)
    normalized['input_checkpoint']='Empty before the first60 calls; fixed literal H5 prism; deterministic tree order; no random seed.' if basecalls==0 and args.calls==60 else 'Resume or changed call count; see supplied input checkpoint.'
    raw=(json.dumps(normalized,sort_keys=True,indent=2)+'\n').encode()
    path=args.out.with_suffix('.checkpoint.json');path.write_bytes(raw)
    print('NUMERICAL_CHECKPOINT_ONLY',len(records),len(failed),normalized['unprocessed_count'],normalized['calls'])
    print('CHECKPOINT_BYTES_SHA256',len(raw),hashlib.sha256(raw).hexdigest())
    print('DONE',args.out,flush=True)
if __name__=='__main__':main()
