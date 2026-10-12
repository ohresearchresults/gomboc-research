# material-4d3e16daf49c

AI research material

<!-- historical-status:start -->
> **Historical AI material.** The title and claims below reflect the AI’s assessment at the time. Claims of proof, certification or completion are not a current verification verdict.
>
> [C622](../C622/README.md) passes the supplied exact checks; C<500 remains open; Minimum’s C≥34 remains a working lower bound requiring a consolidated proof. See [verification status and source gaps](../catalog/coverage.md).
<!-- historical-status:end -->

---

"""Common actual moment coefficients across true-path root orientations.
Dependencies: exact flip_moments.py and native55.txt named by pinned materials.
Run: python common_roots.py locate INDEX MODE
     python -S common_roots.py check RECORD.json
MODE=root (root-specific multipliers), oriented (shared per directed edge),
edge (shared per undirected edge). All internal roots1..8 are simultaneous.
No result is a proof until check succeeds and complete data are preserved.
"""
import os
os.environ['OPENBLAS_NUM_THREADS']='1';os.environ['OMP_NUM_THREADS']='1'
from pathlib import Path
import sys,json,hashlib,time
assert __debug__
HERE=Path(__file__).resolve().parent
PIN=[13811,'7542ef43f2e0e5b4759f076086c8de3539da8ef5051c80dae2a71e778a21faa7']
b=(HERE/'flip_moments.py').read_bytes();assert [len(b),hashlib.sha256(b).hexdigest()]==PIN
import flip_moments as fm
ROOTS=tuple(range(1,9))

def key(mode,root,t,i,p):
    if mode=='root':return(root,t,i,p)
    if mode=='oriented':return(t,i,p)
    assert mode=='edge';return(t,min(i,p),max(i,p))

def mappings(mode,cells):
    keys=sorted({key(mode,r,t,i,i+1 if i<r else i-1)
        for r in ROOTS for t in cells for i in range(10) if i!=r})
    index={k:j for j,k in enumerate(keys)}
    maps=[[index[key(mode,r,t,i,i+1 if i<r else i-1)]
        for t in cells for i in range(10) if i!=r] for r in ROOTS]
    return keys,maps

def pencil(index,mode):
    import numpy as np
    from scipy.sparse import coo_matrix,vstack
    row=fm.inputs()[index];pieces=[];free=None
    for r in ROOTS:
        d,A,bounds,fr=fm.pencil(row,r)
        if free is None:
            free=fr;keys,maps=mappings(mode,d['cells']);width=free+len(keys)
        assert free==fr
        co=A.tocoo();newcol=np.concatenate((np.arange(free),free+np.array(maps[r-1])))
        pieces.append(coo_matrix((co.data,(co.row,newcol[co.col])),shape=(A.shape[0],width)).tocsr())
    return d,vstack(pieces).tocsr(),[(-1,1)]*free+[(0,1)]*len(keys),free,keys,maps

def expand(record):
    assert record['identity']=='ALL_FACET_FLIP_COMMON_ROOTS_V1'
    i=record['native_index'];mode=record['mode'];x=record['coefficients']
    assert all(type(v)==int for v in x)
    d=fm.system(fm.inputs()[i]);sp=fm.pin(fm.enc(fm.description(d)))
    assert record['system_pin']==sp
    fr=10*(len(d['basis'])+1)+56*len(d['basis']);keys,maps=mappings(mode,d['cells'])
    assert len(x)==fr+len(keys) and min(x[fr:])>=0
    return [{'identity':'TREE253_K2_ALL_FACET_FLIP_CERTIFICATE_V1','native_index':i,
            'root':r,'system_pin':sp,'rounding_power':record['rounding_power'],
            'coefficients':x[:fr]+[x[fr+j] for j in maps[r-1]]} for r in ROOTS]

def check(record):
    reports=[fm.check(r) for r in expand(record)]
    return {'identity':'ALL_FACET_FLIP_COMMON_ROOTS_EXACT_REPORT_V1',
        'native_index':record['native_index'],'mode':record['mode'],
        'record_pin':fm.pin(fm.enc(record)),'coefficient_count':len(record['coefficients']),
        'roots':list(ROOTS),'total_blocks':sum(r['cells'] for r in reports),
        'total_leading_minors':sum(r['positive_leading_minors'] for r in reports),
        'reports':reports}

def locate(index,mode):
    import numpy as np,scipy,platform
    from scipy.optimize import minimize
    from scipy.special import logsumexp
    start=time.time();d,A,bounds,fr,keys,maps=pencil(index,mode)
    n=len(d['cells'])*len(ROOTS);x=np.zeros(A.shape[1]);history=[]
    print('COMMON_ROOT_PENCIL',index,mode,A.shape,A.nnz,fr,len(keys),flush=True)
    for tau in (.1,.03,.01,.003,.001,.0003,.0001,.00003):
        def objective(x):
            mats=(A@x).reshape(n,10,10);lam,U=np.linalg.eigh(mats)
            z=-lam/tau;lse=logsumexp(z);weights=np.exp(z-lse)
            grad=np.einsum('bik,bk,bjk->bij',U,weights,U)
            return tau*lse,-A.T@grad.ravel()
        r=minimize(objective,x,jac=True,method='L-BFGS-B',bounds=bounds,
             options=dict(maxiter=2500,maxcor=30,ftol=1e-15,gtol=1e-10,maxls=40))
        x=r.x;minimum=float(np.linalg.eigvalsh((A@x).reshape(n,10,10)).min())
        history.append(dict(tau=tau,minimum=minimum,iterations=r.nit,status=int(r.status)))
        print('COMMON_ROOT_STAGE',index,mode,tau,minimum,r.nit,round(time.time()-start,1),flush=True)
        proposal={'identity':'COMMON_ROOT_NUMERICAL_PROPOSAL_V1','native_index':index,
            'mode':mode,'coefficients':x.tolist(),'history':history,
            'environment':[platform.python_version(),np.__version__,scipy.__version__]}
        (HERE/f'common_proposal_{index}_{mode}.json').write_bytes(fm.enc(proposal))
        if minimum>1e-5:break
    for power in (12,14,16,18,20,24):
        q=np.rint(x*2**power);assert np.max(np.abs(q))<2**62
        record={'identity':'ALL_FACET_FLIP_COMMON_ROOTS_V1','native_index':index,
            'mode':mode,'system_pin':fm.pin(fm.enc(fm.description(d))),
            'rounding_power':power,'coefficients':q.astype(np.int64).tolist()}
        try:report=check(record)
        except (AssertionError,ZeroDivisionError):continue
        p=HERE/f'common_certificate_{index}_{mode}.json';p.write_bytes(fm.enc(record))
        p.with_suffix('.verified.json').write_bytes(fm.enc(report))
        print('COMMON_ROOT_EXACT_PASS_EPHEMERAL',index,mode,power,report['total_blocks'],*fm.pin(p.read_bytes()),flush=True)
        return True
    print('COMMON_ROOT_UNKNOWN_NO_EXACT_CERTIFICATE',index,mode,flush=True);return False

if __name__=='__main__':
    if len(sys.argv)==5 and sys.argv[1]=='locate':raise ValueError('locate INDEX MODE')
    if len(sys.argv)==4 and sys.argv[1]=='locate':locate(int(sys.argv[2]),sys.argv[3])
    elif len(sys.argv)==3 and sys.argv[1]=='check':
        p=Path(sys.argv[2]);record=json.loads(p.read_bytes());out=check(record)
        p.with_suffix('.verified.json').write_bytes(fm.enc(out))
        print('COMMON_ROOT_EXACT_CHECK_PASS',record['native_index'],record['mode'],out['total_blocks'],*fm.pin(fm.enc(out)))
    else:raise ValueError('locate INDEX MODE | check RECORD.json')
