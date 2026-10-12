# material-e5704ca6c065

AI research material · [Export notes](../catalog/coverage.md#text-records)

---

# W_ONLY_RESIDUAL_FULL_COVARIANCE_CHORD_ATLAS_V1
## Recovery capsule part 2/3: deterministic source generator and exact transcription repair

Part1 is [internal-source-reference]. All three parts plus lift_core.py from [internal-source-reference] form the complete capsule. This part provides the full generator, not an old checkpoint. Numerical solver output chooses candidate bases; every accepted domain is checked exactly in part3.

### Exact one-line repair of the part1 polynomial source
The part1 atlas_common.py code block transposed the operands of one equality when it was preserved. This is semantically equivalent, but its unpatched bytes are NOT the declared original SHA. For exact recovery of the actually executed source, replace exactly once:

    if len(dedup)>1 and dedup[0]==dedup[-1]:dedup.pop()

by:

    if len(dedup)>1 and dedup[-1]==dedup[0]:dedup.pop()

Unpatched block:4146B,SHA256 fc099dabca7747ff3f3dbce3d7d8ec99aa6d0fa14d35294b4676a555b0ad0e37. Patched original atlas_common.py:4146B,SHA256 0b16f4295901bad2e9e6c37071cee1db7bcc1af959226a6b30cd014fa30035a1. This explicit exact patch restores the original; the immutable part1 is not silently renamed into different bytes. No other source alteration is intended.

### atlas_generate.py
9045 bytes, SHA256 111031e504f410fa4165a1c395ae9ee12a3eb527268e1ae17336c95aabef4622. Save the complete code block with its final LF. Observed environment CPython3.13.5,NumPy2.3.5,SciPy1.17.0,SymPy1.14.0. All numerical tolerances, rational denominator bounds, finite directional net, subdivision depth and deterministic ordering are explicit below. No random seed or random call exists.

Reconstruct in a clean directory containing the five supplied sources:

    python -u -B atlas_generate.py

The equivalent bounded, resumable mode repeats `python -u -B atlas_generate.py --seconds 20` until W_ONLY_ATLAS_RECOVERY_COMPLETE. Exact checkpoints are generated outputs, not required recovery inputs. The time partition does not change the stack order or exact saved data. A nonempty failures list aborts final acceptance. An unclosed cell is never silently dropped.

Expected final data atlas_exact_bases.json:87990B,SHA256 b40f47caf65789a5725142ca203b0abbbdb02427f50b47467d4aed69c6197c05,23 cases,1232 leaves. One complete source-only reconstruction was observed; no claim of a second independent full clean-generation replay is made. Separate exact verification of all23 cases was observed and is documented in part3. Earlier experimental1452-leaf files are not this1232-leaf object and are not recovery inputs.

```python
"""Deterministic source recovery for the W-only full-affine-orbit certificate.

Default: regenerate all 23 cases and atlas_exact_bases.json from exact THETA.
--seconds 20: bounded resumable generation; every checkpoint is exact JSON.
No checkpoint or numerical certificate is required as an initial input.
Acceptance is separately performed by atlas_verify.py, without SciPy.
"""
import argparse,json,time,math
from itertools import product
from fractions import Fraction
from pathlib import Path
import hashlib
import numpy as np
from scipy.optimize import linprog
import atlas_common as A
import floor_local_locator as N


def rat(x,den=100000):
    return str(A.R(Fraction(float(x)).limit_denominator(den)))


def find_certificate(a,b,tri,maxiter=100):
    pt=sum(tri,A.S.zeros(2,1))/3
    v=(2*A.C-A.RAW[a][:2,0]-pt)/A.K
    vf=np.array(v,dtype=float).reshape(2)
    objective,tr,fm,rows,labels=N.prepare(vf,a,b)
    # A fixed rational directional net prevents a barely infeasible coarse
    # PSD outer cover from producing unnecessarily enormous dual weights.
    for q in product(range(-3,4),repeat=3):
        if next((x for x in q if x),0)<=0 or math.gcd(*q)!=1:continue
        rows.append(np.einsum('i,kij,j->k',q,fm,q))
        labels.append(('floor',q))
    # All constraints are homogeneous; a positive sum equal to minus trace
    # proves exclusion. Numerical dual candidates are later checked exactly.
    rows.insert(0,objective);labels.insert(0,('spoke',))
    for it in range(maxiter):
        rr=np.array(rows)
        scales=np.maximum(np.linalg.norm(rr,axis=1),1e-12)
        res=linprog(np.ones(len(rows)),A_eq=(rr/scales[:,None]).T,b_eq=-tr,
                    bounds=[(0,None)]*len(rows),method='highs')
        if res.status==0:
            terms=[]
            for label,value,scale in zip(labels,res.x,scales):
                if value<=1e-9:continue
                weight=A.R(rat(value/scale,100000000))
                if label[0]=='chord':
                    _,ys,_,_,_=A.chart(a)
                    aval=ys[a].subs({A.X:pt[0],A.Y:pt[1]})
                    beta=pt+aval
                    ends=[]
                    for e,(n,h) in enumerate(A.SUPPORTS):
                        d=-n.dot(aval)
                        if d>0:ends.append(((h-n.dot(beta))/d,e,d))
                    tau,e,d=min(ends)
                    # tau=(h-n.beta)/(-n.A), same actual upper endpoint.
                    assert abs(float(tau)-label[1])<1e-8
                    weight=A.R(rat(float(weight/(d*d)),100000000))
                    terms.append({'kind':'chord','data':[e],'weight':str(weight)})
                elif label[0]=='floor':
                    terms.append({'kind':'floor','data':[rat(t) for t in label[1]],'weight':str(weight)})
                elif label[0]=='top':
                    terms.append({'kind':'top','data':[label[1]],'weight':str(weight)})
                else:terms.append({'kind':'spoke','weight':str(weight)})
            polys=A.certificate_polys(a,b,terms)
            if all(f.eval({A.X:pt[0],A.Y:pt[1]})>0 for f in polys):
                return terms,polys,it
            return None,None,('rational_rounding',terms)
        # Get a witness in the finite outer cover, then add an eigenvector cut.
        primal=linprog(-objective,A_ub=-rr,b_ub=np.zeros(len(rr)),
                       A_eq=tr[None,:],b_eq=[1.],bounds=[(None,None)]*4,method='highs')
        if primal.status!=0:
            return None,None,('outer_solver',res.message,primal.message)
        ff=np.einsum('k,kij->ij',primal.x,fm)
        eig,vec=np.linalg.eigh(ff)
        if eig[0]>=-1e-8:
            return None,None,('LOCAL_PASS',primal.x.tolist(),eig.tolist())
        q=vec[:,0];q/=np.max(np.abs(q))
        q=np.array([float(A.R(rat(x))) for x in q])
        rows.append(np.einsum('i,kij,j->k',q,fm,q));labels.append(('floor',q.tolist()))
    return None,None,('iterations',it)


def check(terms,polys,a,tri):
    for term in terms:
        if term['kind']=='chord':
            n,h=A.SUPPORTS[int(term['data'][0])]
            aa=A.chart(a)[1][a]
            d=-n.dot(aa)
            if min(d.subs({A.X:p[0],A.Y:p[1]}) for p in tri)<=0:return False
    return all(A.triangle_sign(f,tri)[0] for f in polys)


def enc_tri(tri):return [[str(x) for x in p] for p in tri]


def solve_case(a,b,e,maxdepth=22,seconds=None):
    poly=A.polygon(a,e)
    final=Path(f'atlas_{a}_{b}_{e}.json')
    if final.exists():return json.loads(final.read_text())
    if len(poly)<3 or A.area2(poly)==0:return None
    roots=[(poly[0],poly[j],poly[j+1]) for j in range(1,len(poly)-1)]
    checkpoint=Path(f'atlas_{a}_{b}_{e}.checkpoint.json')
    if checkpoint.exists():
        saved=json.loads(checkpoint.read_text())
        stack=[]
        for item in saved['stack']:
            tri=tuple(A.S.Matrix(tuple(map(A.R,p))) for p in item['triangle'])
            terms=item['terms']
            polys=A.certificate_polys(a,b,terms) if terms is not None else None
            stack.append((tri,item['depth'],item['path'],terms,polys,item['anchor']))
        accepted=saved['accepted'];failures=saved['failures'];calls=saved['calls']
    else:
        stack=[(tri,0,str(i),None,None,None) for i,tri in enumerate(roots)]
        accepted=[];failures=[];calls=0
    start=time.time()
    while stack:
        if seconds is not None and time.time()-start>seconds:
            payload={'stack':[{'triangle':enc_tri(t),'depth':d,'path':p,'terms':te,'anchor':an} for t,d,p,te,po,an in stack],
                     'accepted':accepted,'failures':failures,'calls':calls}
            checkpoint.write_text(json.dumps(payload,indent=2)+'\n')
            print('CHECKPOINT',a,b,e,'leaves',len(accepted),'pending',len(stack),'calls',calls,flush=True)
            return None
        tri,depth,path,terms,polys,anchor=stack.pop()
        if terms is None or not check(terms,polys,a,tri):
            terms,polys,info=find_certificate(a,b,tri);calls+=1;anchor=path
            if terms is None:
                failures.append({'triangle':enc_tri(tri),'path':path,'reason':info})
                print('FAIL',a,b,e,depth,info,flush=True)
                continue
        if check(terms,polys,a,tri):
            accepted.append({'path':path,'anchor':anchor,'terms':terms})
        elif depth<maxdepth:
            children=A.split_triangle(tri)
            stack.extend((child,depth+1,path+str(i),terms,polys,anchor) for i,child in enumerate(children))
        else:
            failures.append({'triangle':enc_tri(tri),'path':path,'reason':'depth'})
        if (len(accepted)+len(failures))%25==0:
            print('PROGRESS',a,b,e,'leaves',len(accepted),'stack',len(stack),'calls',calls,'sec',round(time.time()-start,1),flush=True)
    out={'a':a,'b':b,'foot_edge':e,'polygon':enc_tri(poly),'roots':len(roots),
         'leaves':accepted,'failures':failures,'calls':calls}
    Path(f'atlas_{a}_{b}_{e}.json').write_text(json.dumps(out,indent=2)+'\n')
    checkpoint.unlink(missing_ok=True)
    print('DONE',a,b,e,'leaves',len(accepted),'failures',len(failures),'calls',calls,'sec',round(time.time()-start,1),flush=True)
    return out

def symbol(term):
    kind=term['kind']
    if kind=='spoke':return ['S']
    if kind=='top':return ['T',int(term['data'][0])]
    if kind=='chord':return ['C',int(term['data'][0])]
    if kind=='floor':return ['F',*map(str,term['data'])]
    raise ValueError(kind)


def main():
    parser=argparse.ArgumentParser()
    parser.add_argument('--seconds',type=float)
    args=parser.parse_args()
    if args.seconds is not None:assert args.seconds>0
    start=time.time();results=[]
    for a,b in A.PORTS:
        for e in range(7):
            poly=A.polygon(a,e)
            if len(poly)<3 or not A.area2(poly):continue
            budget=None if args.seconds is None else max(0.01,args.seconds-(time.time()-start))
            result=solve_case(a,b,e,22,budget)
            if result is None:
                print('W_ONLY_ATLAS_RECOVERY_CHECKPOINT')
                return
            assert not result['failures'],(a,b,e,result['failures'])
            results.append(result)
    data={'version':1,'identity':'W_ONLY_RESIDUAL_FULL_COVARIANCE_CHORD_ATLAS_V1',
          'theta':list(A.THETA),'ell':str(A.ELL),'cases':[]}
    for result in results:
        leaves=[]
        for leaf in sorted(result['leaves'],key=lambda z:z['path']):
            assert len(leaf['terms'])==4
            leaves.append([leaf['path'],leaf['anchor'],*[symbol(t) for t in leaf['terms']]])
        data['cases'].append({'port':[result['a'],result['b']],
                            'outside_edge':result['foot_edge'],'leaves':leaves})
    raw=(json.dumps(data,ensure_ascii=True,separators=(',',':'))+'\n').encode()
    Path('atlas_exact_bases.json').write_bytes(raw)
    print('ATLAS_SOURCE_RECOVERY',len(data['cases']),'cases',sum(len(c['leaves']) for c in data['cases']),'leaves')
    print('ATLAS_DATA',len(raw),hashlib.sha256(raw).hexdigest())
    print('W_ONLY_ATLAS_RECOVERY_COMPLETE')

if __name__=='__main__':main()
```
