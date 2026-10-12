# material-b731dbd90f4b

AI research material · [Export notes](../catalog/coverage.md#text-records)

---

# COORD_VERTEX_DELETE_V1 — fresh exact-input vertex-deletion census

Status: complete new method source preserved before executing the census. No new construction or exclusion is claimed. This direction allows actual hull/incidence changes instead of freezing every triangular face at the nearly coplanar wall reached by LOCAL_LP_V2.

Exact starting dependencies are the fully preserved accepted NC57 parent figure-0398, SHA b6c84be62ea56d1c11575d4d6309563f525d734f79b0ad2a299f0b7abd2ccdd3. Recover its standalone37-file capsule as specified there. Use C372_ALT_FULL_G4/REPORT.json (14190 bytes, SHA639b7dd56caf48ee99f1175e20b1f305100dc0fb3f75440dd20aba8df57b4cb5) or C378_ALT_POLY_G6/REPORT.json (18534 bytes, SHAfc46fb08252486d5c2474d70c6834b2f4849f8de25bcf18ccb059a7aa9ced661). Report points are the literal exact input vertices. Deletion indices always refer to those report rows, not earlier C384 ancestry or control coordinates.

Save code as DELETE_CENSUS.py,4650bytes,SHA2565a2ee8b81b36eb548544775f459b006a29bf1f4bb6fcd06cfca4173fbfe2555c,UTF8onefinalnewline. All helpers included, no parent-code imports. Environment CPython3.13.5,NumPy2.3.5,SciPy1.17.0,binary64,oneBLAS/OMP/MKLthread;assertionsenabled.

Commands (new output directory required):
`python DELETE_CENSUS.py NC57_SOURCE/proof/C372_ALT_FULL_G4/REPORT.json DELETE372_K2 2 0 0`
`python DELETE_CENSUS.py NC57_SOURCE/proof/C378_ALT_POLY_G6/REPORT.json DELETE378_K2 2 0 0`
Combination rank is k=1..max_delete, then lexicographic itertools.combinations. start_rank inclusive,end_rank exclusive;end0 means all. This permits disjoint deterministic shards without changing input or seed; no randomness.

For each subset it rebuilds the hull, retains actual extreme vertices, recomputes filled-solid centroid and maximal-normal representatives, then applies all-pair physical/polar escape tests. Coplanarity grouping1e-11relative and winning angular margin>1e-9 are NUMERICAL gates only. E=V+F-2 uses the numerically grouped maximalfacet count, not triangulation edges; exact audits must replace this provisional count. Full CENSUS.json stores a compact row per tested subset; failed numerical hulls are explicitly recorded. Any NUMERICAL_DELETE_WINNER is a proposal only. Exact follow-up uses precisely the retained Fraction-string input rows, no coordinate refitting or rounding, with independent all-feature A/B/centred integration from the accepted NC57 auditor. Terminal marker COORD_VERTEX_DELETE_CENSUS_FINISHED.

```python
#!/usr/bin/env python3
"""Fresh exact-input vertex-subset deletion census; numeric gate, not exact proof.
Python3.13.5 NumPy2.3.5 SciPy1.17.0 binary64 threads1.
Usage: DELETE_CENSUS.py exact_REPORT.json OUT max_delete start_rank end_rank
end_rank=0 means all lexicographic combinations up to max_delete.
Only retain an own110 claim after independent exact hull/mass/all-feature audit.
"""
import os
for k in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS'):os.environ[k]='1'
import sys,json,hashlib,itertools,time
from pathlib import Path
from fractions import Fraction
import numpy as np
from scipy.spatial import ConvexHull,QhullError

def pack(x):return json.dumps(x,sort_keys=True,separators=(',',':'))+'\n'
def esc(W):
    D=W[None,:,:]-W[:,None,:]
    dn=np.linalg.norm(D,axis=2);rn=np.linalg.norm(W,axis=1)
    dot=np.einsum('ik,ijk->ij',W,D)
    np.fill_diagonal(dn,1.)
    a=dot/(rn[:,None]*dn);np.fill_diagonal(a,-np.inf)
    return np.max(a,axis=1)

def check(P):
    h=ConvexHull(P);vi=np.sort(h.vertices);P=P[vi];h=ConvexHull(P)
    f=h.simplices.copy();t=P[f];n=np.cross(t[:,1]-t[:,0],t[:,2]-t[:,0]);bad=np.sum(n*h.equations[:,:3],axis=1)<0
    f[bad]=f[bad][:,[0,2,1]];t=P[f]
    w=np.einsum('ij,ij->i',t[:,0],np.cross(t[:,1],t[:,2]))/6
    vol=w.sum();g=(w[:,None]*t.sum(1)).sum(0)/(4*vol);X=P-g
    n=np.cross(t[:,1]-t[:,0],t[:,2]-t[:,0]);height=np.einsum('ij,ij->i',n,X[f[:,0]])
    if np.min(height)<=0:raise ValueError('nonpositive own support')
    Q=n/height[:,None]
    # Coplanar triangulation duplicates cannot be counted as maximal facets.
    rows=[]
    for q in Q:
        if not any(np.linalg.norm(q-r)<=1e-11*max(np.linalg.norm(q),np.linalg.norm(r),1.) for r in rows):rows.append(q)
    Q=np.array(rows);u=esc(X);s=esc(Q)
    S=int(np.sum(s<0));U=int(np.sum(u<0))
    mu=float(np.partition(u,1)[1]);ms=float(np.partition(s,1)[1])
    return dict(V=len(P),F=len(Q),E=len(P)+len(Q)-2,C=2*(len(P)+len(Q)-2),S=S,U=U,
                margin=min(mu,ms),marginU=mu,marginS=ms,centroid=g.tolist(),volume=float(vol),
                unstable=vi[np.where(u<0)[0]].tolist(),stable=np.where(s<0)[0].tolist(),
                min_absolute_escape=float(min(np.abs(u).min(),np.abs(s).min())),
                coplanar_triangles=len(f)-len(Q))

def main(src,out,kmax,start,end):
    raw=Path(src).read_bytes();d=json.loads(raw);P=np.array([[float(Fraction(x)) for x in row] for row in d['points']]);out=Path(out);out.mkdir(parents=True,exist_ok=False)
    (out/'INPUT_REPORT.json').write_bytes(raw)
    opts=dict(max_delete=kmax,start_rank=start,end_rank=end,input_sha256=hashlib.sha256(raw).hexdigest(),order='k=1..kmax then itertools.combinations(range(V),k)',gate_margin=1e-9,version='COORD_VERTEX_DELETE_V1')
    (out/'OPTIONS.json').write_text(pack(opts));bestkey=(999.,float('inf'));best=None;counts={};rank=-1;tested=0;errors=0;winners=[];rows=[]
    for k in range(1,kmax+1):
        for delete in itertools.combinations(range(len(P)),k):
            rank+=1
            if rank<start:continue
            if end and rank>=end:break
            keep=[i for i in range(len(P)) if i not in delete]
            try:
                r=check(P[keep]);tested+=1;r.update(rank=rank,deleted=list(delete));key=(r['S']+r['U'],-r['margin']);cl=f"{r['S']},{r['U']}";counts[cl]=counts.get(cl,0)+1
                # Compact complete census row for every successful candidate.
                rows.append([rank,list(delete),r['V'],r['E'],r['F'],r['S'],r['U'],r['margin'].hex(),r['coplanar_triangles']])
                if key<bestkey:
                    bestkey=key;best=r;(out/'BEST.json').write_text(pack(r));print('DELETE_BEST',r,flush=True)
                if r['S']==r['U']==1 and r['margin']>1e-9:
                    winners.append(r);(out/('NUMERICAL_WINNER_'+str(rank)+'.json')).write_text(pack(r));print('NUMERICAL_DELETE_WINNER',r,flush=True)
            except (QhullError,ValueError,FloatingPointError) as exc:
                errors+=1;rows.append([rank,list(delete),'ERROR',str(exc)])
            if tested%200==0:
                (out/'CENSUS.json').write_text(pack(rows));(out/'SUMMARY.json').write_text(pack(dict(tested=tested,errors=errors,counts=counts,best=best,winners=winners,partial=True)))
        if end and rank>=end:break
    res=dict(tested=tested,errors=errors,counts=counts,best=best,winners=winners,partial=False,last_rank=rank,options=opts)
    (out/'CENSUS.json').write_text(pack(rows));(out/'SUMMARY.json').write_text(pack(res));print('COORD_VERTEX_DELETE_CENSUS_FINISHED',res,flush=True)
if __name__=='__main__':main(sys.argv[1],sys.argv[2],int(sys.argv[3]),int(sys.argv[4]),int(sys.argv[5]))
```
