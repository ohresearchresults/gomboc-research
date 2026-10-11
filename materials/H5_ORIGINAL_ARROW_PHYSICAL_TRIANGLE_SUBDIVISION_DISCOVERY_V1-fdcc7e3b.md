# material-fdcc7e3be1b6

Historical AI scientific source/proof material. Statements retain their original scope; this is not an independently reviewed theorem.

Public derivative: internal-record-identifiers-replaced.

---

# H5_ORIGINAL_ARROW_PHYSICAL_TRIANGLE_SUBDIVISION_DISCOVERY_V1

Complete reusable discovery source which produced H5_FULL_BASAL_LAMBDA_GE_3_5_DYADIC_V1. Numerical proposals are accepted only by exact integer Sylvester tests. A failed cell LP is not a physical common-metric witness. These routines subdivide the actual original-arrow Bernstein matrices, not an earlier information-losing quadratic lowering.

## Complete dependencies and commands
Required existing units: h5_collar_weighted.py from [internal-source-reference], 9389 bytes, SHA256 18d63fc0ed4267051d54e63e780554d042d92d44a38bd445b14effe066c4ac7d; search_h5_extension.py from [internal-source-reference], 5399 bytes, SHA256 141d4b6483eaa11041988dc3e015f30510719e1d4714635b46797ba454d22343. The first old compression program in that material is not needed by this method.

Extract the three complete blocks below as:
1. refine_h5_cells.py, 2844 bytes, SHA256 b9b29a7c4bc9add77b6f907d27659fffce8f693c4ffdf50e788fbbeb2d9cc684.
2. refine_h5_more.py, 3442 bytes, SHA256 c04e29101152de3466501fc5160cefaee138240709201f8e06c637b89f0fc246.
3. compress_h5_subdivision.py, 1725 bytes, SHA256 1f49cec612576271c1eb4bd3410cb15cf0a26efa20d289c93900be880f721859.

Environment: Python3.13.5, NumPy2.3.5, SciPy1.17.0, OPENBLAS_NUM_THREADS=1. No seed or undisclosed inputs. Delete coeff_*.npz to rebuild exact coefficient caches.

OPENBLAS_NUM_THREADS=1 python search_h5_extension.py --s-max 2/5 --max-trees 1500 --output extension_2_5.json
OPENBLAS_NUM_THREADS=1 python refine_h5_cells.py --source extension_2_5.json --output refined_2_5.json --depth 3
OPENBLAS_NUM_THREADS=1 python refine_h5_more.py --source refined_2_5.json --output refined_more_2_5.json --levels 2
OPENBLAS_NUM_THREADS=1 python compress_h5_subdivision.py

Observed global source: 661 certified rows, 48616 covered trees, 174 residual trees, 725 proposals. The x/r-only refinement left 6 unresolved cells with counts18,18,15,18,29,32 (132 tree-cell incidences, not necessarily distinct trees). The triangle/taper extension returned FINAL cells82 failed0. Compression printed CANONICAL83 686 34289, with normal spaces between fields. Exact output h5_three_fifths_atlas.json:34289 bytes, SHA256 967640b387993a9297e0fae367b4e817e34b9c090530288adb4d842b138957c8. Floating LP proposals and elapsed diagnostics need not be byte invariant across solvers; the authoritative proof input is the complete literal capsule, not rerunning the discovery optimizer.

Canonical recovery/proof requires geometry and ALL [internal-source-reference], [internal-source-reference], [internal-source-reference]. Its proof verifier uses no floating point or optimizer. It checks all 48 leaves of the complete parameter partition, all 48790 rooted trees, 548800 coefficient matrices and 1646400 positive leading minors, with zero residual cones.

## First refinement source
```python
"""Dyadic original-arrow Bernstein subdivision; numerical proposal + exact gate."""
from fractions import Fraction as F
from pathlib import Path
import argparse,json,time
import numpy as np
from search_h5_extension import build,tree_data,solve,exact_test

LEFT=np.array([[8,0,0,0],[4,4,0,0],[2,4,2,0],[1,3,3,1]],dtype=np.int64)
RIGHT=np.array([[1,3,3,1],[0,2,4,2],[0,0,4,4],[0,0,0,8]],dtype=np.int64)

def split(T,L,axis,side):
    """axis0=x,axis1=r. T stores degree(3,3,total3,4) coefficients."""
    Q=T.reshape(34,4,4,10,5,6);k=axis+1;A=LEFT if side==0 else RIGHT
    assert int(np.abs(Q).max())*8<2**63
    out=np.tensordot(A,Q,axes=(1,k));out=np.moveaxis(out,0,k)
    return out.reshape(T.shape),L*8

def main():
    p=argparse.ArgumentParser();p.add_argument('--source',required=True);p.add_argument('--output',required=True);p.add_argument('--depth',type=int,default=2);a=p.parse_args()
    o=json.loads(Path(a.source).read_text());S=F(o['s_max']);ar,T,L=build(S);tr,tm,roots=tree_data(ar);idx={a:i for i,a in enumerate(ar)}
    masks=[np.uint64(sum(1<<idx[i,j] for i,j,w in c)) for c in o['certificates']]
    globally=np.zeros(len(tr),bool)
    for m in masks:globally|=(tm&m)==m
    residual=np.flatnonzero(~globally);print('GLOBAL_RESIDUAL',len(residual),flush=True)
    cells=[];bad=[];start=time.monotonic()
    def visit(T,L,path,needed):
        certs=[];covered=np.zeros(len(tr),bool);remaining=[]
        for k in needed:
            if covered[k]:continue
            w,info=solve(T,L,tr[k]);
            if w is None:remaining.append(int(k));continue
            c=[[*ar[i],int(v)] for i,v in zip(tr[k],w) if v]
            m=np.uint64(sum(1<<idx[i,j] for i,j,v in c));covered[:]|=(tm&m)==m
            certs.append(c)
        remaining=[k for k in remaining if not covered[k]]
        cells.append({'path':path,'certificates':certs})
        print('CELL',path,'needed',len(needed),'certs',len(certs),'remain',len(remaining),'seconds',round(time.monotonic()-start,2),flush=True)
        if remaining:
            if len(path)>=a.depth:bad.append({'path':path,'remaining':remaining})
            else:
                axis=len(path)%2
                for side in range(2):
                    U,LL=split(T,L,axis,side);visit(U,LL,path+[[axis,side]],remaining)
        out={'identity':'H5_FULL_BASAL_LAMBDA_GE_3_5_DYADIC_V1','s_max':str(S),'global_certificates':o['certificates'],'cells':cells,'failures':bad,'global_covered':int(globally.sum())}
        Path(a.output).write_text(json.dumps(out,separators=(',',':'))+'\n')
    # Whole-cell root attempts already exhausted by the source; start two x halves.
    for side in range(2):
        U,LL=split(T,L,0,side);visit(U,LL,[[0,side]],residual)
    print('FINAL',len(cells),'failed_cells',len(bad),'seconds',time.monotonic()-start,flush=True)
if __name__=='__main__':main()
```

## Physical triangle/taper refinement source
```python
"""Continue dyadic Bernstein refinements in the full physical triangle and taper."""
from fractions import Fraction as F
from pathlib import Path
import argparse,json,time,math,itertools
import numpy as np
from search_h5_extension import build,tree_data,solve
from refine_h5_cells import split as split_xy

TRI=tuple((p,q) for p in range(4) for q in range(4-p))
TRI_IDX={a:i for i,a in enumerate(TRI)}
VERTS=(((2,0,0),(1,1,0),(1,0,1)),((1,1,0),(0,2,0),(0,1,1)),((1,0,1),(0,1,1),(0,0,2)),((1,1,0),(0,1,1),(1,0,1)))

def normalize(T,L):
    g=math.gcd(L,int(np.gcd.reduce(np.abs(T).ravel())))
    return T//g,L//g

def split(T,L,axis,side):
    if axis<2:return normalize(*split_xy(T,L,axis,side))
    if axis==2:
        A=np.zeros((10,10),np.int64)
        for row,(p,q) in enumerate(TRI):
            vv=[VERTS[side][0]]*(3-p-q)+[VERTS[side][1]]*p+[VERTS[side][2]]*q
            for choices in itertools.product(range(3),repeat=3):
                val=math.prod(vv[k][j] for k,j in enumerate(choices))
                A[row,TRI_IDX[choices.count(1),choices.count(2)]]+=val
        den=8;ax=3
    else:
        assert axis==3
        A=np.zeros((5,5),np.int64)
        for i in range(5):
            for j in range(5):
                if side==0 and j<=i:A[i,j]=math.comb(i,j)*2**(4-i)
                if side==1 and j>=i:A[i,j]=math.comb(4-i,j-i)*2**i
        den=16;ax=4
    assert np.all(A.sum(axis=1)==den)
    assert int(np.abs(T).max())*den<2**63
    out=np.tensordot(A,T.reshape(34,4,4,10,5,6),axes=(1,ax));out=np.moveaxis(out,0,ax).reshape(T.shape)
    return normalize(out,L*den)

def main():
    p=argparse.ArgumentParser();p.add_argument('--source',required=True);p.add_argument('--output',required=True);p.add_argument('--levels',type=int,default=2);a=p.parse_args()
    o=json.loads(Path(a.source).read_text());ar,T,L=build(F(o['s_max']));T,L=normalize(T,L);tr,tm,roots=tree_data(ar);idx={a:i for i,a in enumerate(ar)}
    cells=list(o['cells']);bad=[];start=time.monotonic()
    def visit(U,LL,path,needed,depth):
        cs=[];covered=np.zeros(len(tr),bool);remaining=[]
        for k in needed:
            if covered[k]:continue
            w,info=solve(U,LL,tr[k])
            if w is None:remaining.append(k);continue
            c=[[*ar[i],int(v)] for i,v in zip(tr[k],w) if v]
            m=np.uint64(sum(1<<idx[i,j] for i,j,v in c));covered|=(tm&m)==m;cs.append(c)
        remaining=[k for k in remaining if not covered[k]];cells.append({'path':path,'certificates':cs})
        print('CELL',path,'need',len(needed),'certs',len(cs),'remaining',len(remaining),'sec',round(time.monotonic()-start,1),flush=True)
        if remaining:
            if depth>=a.levels:bad.append({'path':path,'remaining':remaining})
            else:
                axis=3 if depth%2 else 2
                for side in range(4 if axis==2 else 2):
                    V,VL=split(U,LL,axis,side);visit(V,VL,path+[[axis,side]],remaining,depth+1)
        result={**o,'cells':cells,'failures':bad};Path(a.output).write_text(json.dumps(result,separators=(',',':'))+'\n')
    for failure in o['failures']:
        U,LL=T,L
        for axis,side in failure['path']:U,LL=split(U,LL,axis,side)
        for side in range(4):
            V,VL=split(U,LL,2,side);visit(V,VL,failure['path']+[[2,side]],failure['remaining'],1)
    print('FINAL','cells',len(cells),'failed',len(bad),'seconds',time.monotonic()-start,flush=True)
if __name__=='__main__':main()
```

## Deterministic certificate compression source
```python
"""Remove redundant certificates without changing any parameter domain."""
from pathlib import Path
import json
import numpy as np
from fractions import Fraction as F
from search_h5_extension import build,tree_data

def main():
    o=json.loads(Path('refined_more_2_5.json').read_text());assert not o['failures']
    ar,T,L=build(F(o['s_max']));tr,tm,roots=tree_data(ar);idx={a:i for i,a in enumerate(ar)}
    old={tuple(map(tuple,c['path'])):c['certificates'] for c in o['cells']};old[()]=o['global_certificates']
    children={p:[] for p in old}
    for p in old:
        if p:children[p[:-1]].append(p[-1])
    nodes=[]
    def visit(path,covered):
        cs=old[path];masks=[np.uint64(sum(1<<idx[i,j] for i,j,w in c)) for c in cs]
        un=~covered;chosen=[]
        while un.any() and masks:
            counts=[int((((tm&m)==m)&un).sum()) for m in masks]
            k=min(range(len(cs)),key=lambda k:(-counts[k],len(cs[k]),sum(w for i,j,w in cs[k]),k))
            if not counts[k]:break
            chosen.append(cs[k]);un&=~((tm&masks[k])==masks[k])
        nodes.append({'path':path,'certificates':sorted(chosen,key=lambda c:(len(c),c))})
        if not un.any():return
        cc=children[path];assert cc;axis=cc[0][0]
        assert sorted(cc)==[(axis,s) for s in range(4 if axis==2 else 2)]
        for child in sorted(cc):visit(path+(child,),~un)
    visit((),np.zeros(len(tm),bool))
    out={'identity':'H5_FULL_BASAL_LAMBDA_GE_3_5_DYADIC_V1','s_max':o['s_max'],'nodes':nodes}
    raw=(json.dumps(out,separators=(',',':'))+'\n').encode();Path('h5_three_fifths_atlas.json').write_bytes(raw)
    print('CANONICAL',len(nodes),sum(len(c['certificates']) for c in nodes),len(raw))
if __name__=='__main__':main()
```
