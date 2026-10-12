# material-c592b2cfa4e8

AI research material · [Export notes](../catalog/coverage.md#text-records)

---

# H5_ORIGINAL_ARROW_CUTTING_PLANE_DISCOVERY_V1

Complete reusable numerical proposal method with an exact acceptance gate. This is not a stand-alone numerical proof. It uses all original tree arrows and exact product Bernstein coefficient matrices. Linear programming receives Rayleigh-quotient cuts from eigendecompositions, proposes nonnegative weights summing to one, then deterministic rational rounding is accepted only when every exact integer Sylvester test passes. Literal certificate containment covers other trees too. A failed relaxation is neither a physical metric witness nor a proved full-shape obstruction.

## Dependencies and recovery
Requires the entire h5_collar_weighted.py from [internal-source-reference],9389B,SHA25618d63fc0ed4267051d54e63e780554d042d92d44a38bd445b14effe066c4ac7d. Environment used: Python3.13.5,NumPy2.3.5,SciPy1.17.0,OPENBLAS_NUM_THREADS=1. No random seed or external data is used. Delete any coeff_*.npz cache to rebuild all exact coefficient data from geometry.
Extract the first block as search_h5_extension.py,5399B,SHA256141d4b6483eaa11041988dc3e015f30510719e1d4714635b46797ba454d22343. Extract the second block as compress_h5_atlas.py,1402B,SHA2567478c8236797356c460076be1b5f11104368de2b5868cdbe806f3290f82937ff.

Commands that produced the accepted two-thirds atlas:
OPENBLAS_NUM_THREADS=1 python search_h5_extension.py --s-max 1/3 --max-trees 1000 --output extension_1_3.json
OPENBLAS_NUM_THREADS=1 python compress_h5_atlas.py --source extension_1_3.json --output h5_two_thirds_atlas.json --identity H5_FULL_BASAL_LAMBDA_GE_2_3_V1

Expected scientific terminals: SIMPLE14043464; END487905400; COMPLETE_GREEDY_COVER46118398780abadad78c31b42b2f133a00eafd07c892f43c62e4f447fb32f3634a1c9b03, with normal spaces between the printed fields. The proposal JSON includes elapsed-time diagnostics and is not byte deterministic. The separately retained canonical exact atlas [internal-source-reference] is18398B with the preceding SHA256; use it rather than a floating optimizer for proof recovery. Exact proof/verifier [internal-source-reference] uses no SciPy/optimizer. It reports PASS with zero uncovered trees and zero failed certificates.

A bounded exploratory call --s-max 1/2 --max-trees 1500 --output extension_1_2.json produced1041 certified rows covering46758 of48790 trees, with528 unsuccessful proposals among1500. Failures are relaxation failures, not true-cone feasibility. A successor may reproduce this search from the complete source and arguments, but this count is not a whole-domain exclusion.

## Complete search source
```python
"""Numerical discovery; accepted rows checked by exact integer Sylvester tests.
Requires archived h5_collar_weighted.py. Optimization is not proof.
"""
from fractions import Fraction as F
from pathlib import Path
import argparse,itertools,json,math,time
import numpy as np
from scipy.optimize import linprog
from h5_collar_weighted import exact_geometry,EDGES,orient,quotient_lift,matrix_polynomials,bernstein_coefficients,BASIS,minors

def build(S):
    arrows=sorted((i,j) for a,b in EDGES for i,j in ((a,b),(b,a)))
    cache=Path('coeff_%s_%s.npz'%(S.numerator,S.denominator))
    if cache.exists():
        dat=np.load(cache);return arrows,dat['T'],int(dat['L'])
    z,D,K=exact_geometry();pp=[matrix_polynomials(z,D,K,*a) for a in arrows]
    pd=math.lcm(*(v.denominator for pols in pp for p in pols for v in p.values()))
    L=pd*648*S.denominator**4
    T=np.array([[bernstein_coefficients(p,S,L) for p in pols] for pols in pp],dtype=np.int64).transpose(0,2,1)
    np.savez_compressed(cache,T=T,L=L)
    return arrows,T,L

def to_matrix(T):return T[...,np.array([[0,1,2],[1,3,4],[2,4,5]])]

def tree_data(arrows):
    idx={a:k for k,a in enumerate(arrows)};data=[];masks=[];roots=[]
    for es in itertools.combinations(EDGES,9):
        if orient(es,0) is None:continue
        for root in range(10):
            inds=[idx[a] for a in orient(es,root)]
            data.append(inds);roots.append(root);masks.append(sum(1<<i for i in inds))
    assert len(data)==48790
    return np.array(data),np.array(masks,dtype=np.uint64),roots

def exact_test(T,ids,w):
    if not np.any(w):return False
    assert int(np.abs(T[ids]).max())*sum(map(int,w))<2**63
    P=sum((int(v)*T[i] for i,v in zip(ids,w)),np.zeros(T.shape[1:],dtype=np.int64))
    return all(min(minors(row))>0 for row in P)

def rationalize(T,ids,w):
    for den in (8,16,32,64,128,256,512,1024,4096,16384,65536,1048576):
        nums=np.maximum(0,np.round(w*den)).astype(np.int64)
        d=math.gcd(*map(int,nums));nums=nums//d if d else nums
        if exact_test(T,ids,nums):return nums
    return None

def solve(T,L,ids,max_iter=80):
    ids=list(ids);Q=to_matrix(T[ids]).astype(float)/L;n=len(ids)
    vectors=np.array([(1,0,0),(0,1,0),(0,0,1),(1,1,0),(1,-1,0),(1,0,1),(1,0,-1),(0,1,1),(0,1,-1),(1,1,1),(1,1,-1),(1,-1,1),(-1,1,1)],dtype=float)
    vectors/=np.linalg.norm(vectors,axis=1)[:,None]
    vals=np.einsum('vi,nkij,vj->kvn',vectors,Q,vectors).reshape(-1,n)
    constraints=np.c_[-vals,np.ones(len(vals))];obj=np.r_[np.zeros(n),-1.]
    eq=np.r_[np.ones(n),0.][None,:]
    for it in range(max_iter):
        res=linprog(obj,A_ub=constraints,b_ub=np.zeros(len(constraints)),A_eq=eq,b_eq=[1.],bounds=[(0,None)]*n+[(None,None)],method='highs')
        if not res.success:return None,{'reason':res.message}
        w=res.x[:n];t=res.x[-1]
        if t<1e-8:return None,{'reason':'nonpositive relaxed optimum','bound':float(t),'iter':it}
        eig,U=np.linalg.eigh(np.einsum('n,nkij->kij',w,Q));gap=eig[:,0].min()
        if gap>1e-9:
            nums=rationalize(T,ids,w)
            if nums is not None:return nums,{'gap':float(gap),'iter':it}
        order=np.argsort(eig[:,0]);viol=order[eig[order,0]<t-1e-9][:256]
        if not len(viol):return None,{'reason':'rounding','gap':float(gap),'bound':float(t)}
        v=U[viol,:,0];cuts=np.einsum('ki,nkij,kj->kn',v,Q[:,viol],v)
        constraints=np.concatenate((constraints,np.c_[-cuts,np.ones(len(cuts))]))
    return None,{'reason':'iteration limit','gap':float(gap),'bound':float(t)}

def main():
    pa=argparse.ArgumentParser();pa.add_argument('--s-max',default='1/3');pa.add_argument('--max-trees',type=int,default=1000);pa.add_argument('--output',default='extension_proposals.json');a=pa.parse_args();S=F(a.s_max)
    start=time.monotonic();arrows,T,L=build(S);trees,masks,roots=tree_data(arrows);idx={ar:k for k,ar in enumerate(arrows)}
    print('READY',len(arrows),L,'seconds',round(time.monotonic()-start,2),flush=True)
    certs=[];cover=np.zeros(len(trees),bool)
    def add(ids,w):
        pairs=[(int(i),int(v)) for i,v in zip(ids,w) if v]
        m=np.uint64(sum(1<<i for i,v in pairs));cover[:]|=(masks&m)==m
        certs.append([[*arrows[i],v] for i,v in pairs])
    supports=set()
    for k,ids in enumerate(trees):
        ar=tuple(arrows[i] for i in ids)
        supports.add(tuple(idx[e] for e in quotient_lift(ar,roots[k])))
    for ids in sorted(supports):
        for w in ((1,1,1),(1,1,2),(1,2,1),(2,1,1)):
            if exact_test(T,list(ids),w):add(ids,w);break
    print('SIMPLE',len(certs),int(cover.sum()),flush=True)
    failed=[];attempt=0
    for k,ids in enumerate(trees):
        if cover[k]:continue
        w,info=solve(T,L,ids);attempt+=1
        if w is not None:add(ids,w)
        else:failed.append({'index':k,'root':roots[k],'arrows':[arrows[i] for i in ids],'info':info})
        if attempt%10==0 or w is None:print('STEP',attempt,'covered',int(cover.sum()),'certs',len(certs),'failed',len(failed),'info',info,flush=True)
        out={'s_max':str(S),'scale':L,'certificates':certs,'covered':int(cover.sum()),'failed':failed,'attempts':attempt,'elapsed':time.monotonic()-start}
        Path(a.output).write_text(json.dumps(out,separators=(',',':'))+'\n')
        if attempt>=a.max_trees:break
    print('END',int(cover.sum()),len(certs),len(failed),'sec',time.monotonic()-start,flush=True)
if __name__=='__main__':main()
```

## Complete deterministic compression source
```python
"""Deterministic greedy containment compression of a generated H5 atlas."""
from pathlib import Path
from fractions import Fraction as F
import argparse,json,hashlib
import numpy as np
from search_h5_extension import build,tree_data

def compress(source,output,identity):
    o=json.loads(Path(source).read_text());ar,T,L=build(F(o['s_max']))
    tr,tm,roots=tree_data(ar);idx={a:i for i,a in enumerate(ar)};cs=o['certificates']
    masks=[np.uint64(sum(1<<idx[i,j] for i,j,w in c)) for c in cs]
    un=np.ones(len(tm),bool);sel=[]
    while un.any():
        counts=[int((((tm&m)==m)&un).sum()) for m in masks]
        k=min(range(len(cs)),key=lambda k:(-counts[k],len(cs[k]),sum(w for i,j,w in cs[k]),k))
        if not counts[k]:raise ValueError('The supplied atlas does not cover all trees.')
        sel.append(k);un&=~((tm&masks[k])==masks[k])
    chosen=sorted((cs[k] for k in sel),key=lambda c:(len(c),c))
    out={'identity':identity,'s_max':o['s_max'],'certificates':chosen}
    raw=(json.dumps(out,separators=(',',':'))+'\n').encode();Path(output).write_bytes(raw)
    print('COMPLETE_GREEDY_COVER',len(chosen),len(raw),hashlib.sha256(raw).hexdigest())
if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--source',required=True);p.add_argument('--output',required=True);p.add_argument('--identity',required=True);a=p.parse_args();compress(a.source,a.output,a.identity)
```
