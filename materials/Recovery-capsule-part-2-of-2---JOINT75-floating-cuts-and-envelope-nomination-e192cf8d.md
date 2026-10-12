# material-e192cf8dacfc

AI research material · [Export notes](../catalog/coverage.md#text-records)

---

# Recovery capsule part 2/2: JOINT75_FLOAT_CUTS_AND_ENVELOPE_NOMINATION

Requires part1 [internal-source-reference], SHA22a7e81f129bbab252b200384d1d501fe4dcb533c96a98514970497b63cb2c23. All source files are unencoded literal Python. Save the blocks headed File into the same directory. The standalone exact mathematical envelope certificate is separate: [internal-source-reference] and proof [internal-source-reference]. This capsule preserves the actual producing searches and their limitations, not another exact proof or target body.

## Recovery and observed replay
Python3.13.5, NumPy2.3.5, SciPy1.17.0. Commands:

    OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python -B replay_controls.py
    python -B onecut.py
    python -B reduce_envelope.py
    python -B search_cut.py --which primary --seed 101 --evaluations 1200
    python -B search_cut.py --which bridge --seed 102 --evaluations 1800
    python -B search_cut.py --which primary --seed 201 --evaluations 2400 --affine


Source byte manifests, final newline included:
inputs.py2604B,05b17724b29793f287f8cfb8b467a61d82c6b5a7b098ec1efb48d83d87c708e3;
onecut.py6695B,829424c61d90746f64e227c8263101ae4e128c0f844e7cd37a9d2baf9c3fd28e;
search_cut.py3918B,df4db9c98be0764917f74ae88a815bf588335b7a99db32ef9f002948fd88acad;
reduce_envelope.py1619B,6d8df8118ecfc8239c388798ccfbd1ac7d310b9351213ac6cbf31022731f2e51;
replay_controls.py3732B,0c71f6b2b6afe860f9ad7bdb469563e33c886ab02a05dc02a94136381b87e6b3.

## Scientific boundaries and actual observations
The clipping routine starts with a simplicial generic hull and retains one polygon per original facet plus one polygonal cap. It must not be treated as an exact arbitrary-polytope hull builder: repeated coplanar input facets, nongeneric vertex-plane contacts and degenerate clips require separate handling. The exact certificate enumerates and merges planes independently. The floating census tests strict S/U/H and minimum primitive magnitudes, but does NOT certify additional-weak000. The bars routine omits depths at most1e-13; this is a numerical-search convention, never an exact-zero conclusion. Differential evolution is bounded, but the final Nelder-Mead is intentionally UNBOUNDED, so a final point may leave the initial parameter box. All losses include .005 per edge exceeding249; this is a soft penalty, not feasibility enforcement. The observed bridge search checkpoint has E256 and is outside target.

The replay is the authoritative source for q vectors and edge-origin identities; earlier context-recovery summaries supplied wrong q vectors and wrong search endpoint values. Do not use those summaries. Correct old-centre bridge cut has q=(-.052962532962101065,-2.728027519358677,-.5625228985148008),124/275/153,own244,C550. Correct near primary c=(.48,.03,-.27) has q=(-19.046794728996968,-9.840309815408657,5.132371295433989),46/89/45,own266,C178. Correct near bridge c=(.38,-.12,-.31) has q=(-6.985326739561493,-2.2554827796301375,1.6951131070142034),65/137/74,own266,C274. Both retain the old stable facet and gain the stable cut facet; the unstable carriers all lie on the cut front. Old onecut origins mixed inherited global IDs with newly cut Body-local edge IDs; replay_controls.py now explicitly maps BOTH to literal global input IDs. This is an identity correction, not a new construction.

Actual best search checkpoints: primary seed101 C456,own15/15/28,loss.15579061015557683; bridge seed102 C512,own13/24/35,loss.5972237107302664; affine-primary seed201 C488,own50/41/89,loss.15530814464857823. Replayed positive P/Q lists are complete relative to the stated1e-13 numerical cutoff. These are useful negative observations, not competitive exact endpoints. No targetown110 and canonicalC622 remains unchanged.

## File: search_cut.py
```python
"""Observed finite-cut / affine-metric search. Floating nomination only.
Uses exact-literal inputs.py and generic polygon-preserving onecut.py.
"""
import json, argparse, time
import numpy as np
from scipy.optimize import differential_evolution, minimize
from onecut import Body
from inputs import P75,A

def bars(p,edges):
    rad=np.einsum('ij,ij->i',p,p)
    i,j=edges.T; a=rad[i]; c=rad[j]; b=np.einsum('ij,ij->i',p[i],p[j]); d=a+c-2*b
    w=(a*c-b*b)/np.maximum(d,1e-300)
    w=np.where(b>=a,a,np.where(b>=c,c,w))
    roots=list(range(len(p))); peak=rad.copy(); out=[]
    def find(i):
        while roots[i]!=i: roots[i]=roots[roots[i]];i=roots[i]
        return i
    for k in np.argsort(-w,kind='stable'):
        x,y=find(int(i[k])),find(int(j[k]))
        if x==y:continue
        if peak[x]<peak[y]:x,y=y,x
        depth=(peak[y]-w[k])/peak[y]
        if depth>1e-13:out.append(float(depth))
        roots[y]=x
    return sorted(out,reverse=True)

def landscape(K,M=None):
    p=K.p-K.g; ns=K.normals
    if M is not None:
        p=p@M.T; ns=ns@np.linalg.inv(M)
    h=np.array([ns[k]@p[f[0]] for k,f in enumerate(K.faces)])
    Q=ns/h[:,None]
    return bars(p,K.edges),bars(Q,K.ef)

def metric(t):
    # determinant-one Cholesky factor, all five shape DOF, rotation suppressed
    a,b,c,d,e=t
    return np.array([[np.exp(a),c,d],[0,np.exp(b),e],[0,0,np.exp(-a-b)]])

def candidate(B,x):
    n=np.array([np.cos(x[0])*np.cos(x[1]),np.sin(x[0])*np.cos(x[1]),np.sin(x[1])])
    vals=(B.p-B.g)@n
    h=vals.min()+x[2]*(vals.max()-vals.min())
    # Generic clipping using shifted reference, no requirement to retain old COM.
    cc=B.g+(h-1)*n
    K=B.clip(n,cc)
    return K,n,float(n@B.g+h)

def run(which,seed,evaluations,affine):
    B=Body.hull(P75 if which=='primary' else np.vstack([P75,A])); best=1e10; records=[]; calls=0
    def fun(x):
        nonlocal best,calls
        calls+=1
        try:
            K,n,h=candidate(B,x); mat=metric(x[3:]) if affine else None
            p,q=landscape(K,mat)
            loss=sum(p)+sum(q)+max(0,len(K.edges)-249)*.005
            if loss<best:
                best=loss
                rec=dict(call=calls,loss=loss,x=x.tolist(),n=n.tolist(),h=h,P=p,Q=q,V=len(K.p),E=len(K.edges),F=len(K.faces),volume=K.volume)
                if mat is None:rec['census']=K.census()
                else:rec['census']=Body(K.p@mat.T,K.faces,K.normals@np.linalg.inv(mat),K.origins).census()
                records.append(rec)
                print(json.dumps({'which':which,'seed':seed,'call':calls,'loss':loss,'C':2*len(K.edges),'SUH':[rec['census'][k] for k in ['S','U','H']],'P':p,'Q':q}),flush=True)
            return loss
        except (AssertionError,ValueError,np.linalg.LinAlgError):return 100
    bounds=[(-np.pi,np.pi),(-np.pi/2,np.pi/2),(.04,.99999)]
    if affine:bounds += [(-.65,.65),(-.65,.65),(-.65,.65),(-.65,.65),(-.65,.65)]
    pop=10;dim=len(bounds)
    r=differential_evolution(fun,bounds,seed=seed,popsize=pop,maxiter=max(1,evaluations//(pop*dim)-1),tol=1e-9,polish=False,workers=1,updating='immediate')
    rr=minimize(fun,r.x,method='Nelder-Mead',options={'maxiter':500,'xatol':1e-10,'fatol':1e-12})
    data=dict(which=which,seed=seed,affine=affine,bounds=bounds,eval_requested=evaluations,calls=calls,DE_iterations=int(r.nit),records=records,final_x=rr.x.tolist(),final_loss=float(rr.fun),time=time.time())
    path=f'cut_search_{which}_{seed}_{int(affine)}.json'
    with open(path,'w') as f:json.dump(data,f,indent=2)
    print('FLOAT_CUT_SEARCH_FINISHED',path,calls,flush=True)
    return data

if __name__=='__main__':
    ap=argparse.ArgumentParser();ap.add_argument('--which',choices=['primary','bridge'],default='primary');ap.add_argument('--seed',type=int,default=101);ap.add_argument('--evaluations',type=int,default=1200);ap.add_argument('--affine',action='store_true');a=ap.parse_args()
    run(a.which,a.seed,a.evaluations,a.affine)
```

## File: reduce_envelope.py
```python
"""Floating greedy mandatory-core reduction; only exact follow-up proves a scope."""
import json
import numpy as np
from onecut import Body
from inputs import P75,A,J19
R=np.vstack([P75,A]);O=Body.hull(R);d=O.p[None,:,:]-O.p[:,None,:]
z=np.einsum('vi,vwi->vw',O.p,d)
maxs=np.maximum(0,z-np.einsum('xi,vwi->vwx',O.p,d).min(axis=2))
# z[v,w] and maxs are unnormalized affine-inequality coefficient arrays.
def bounds(ids):
    W=Body.hull(R[ids]); origins=np.array(ids)[W.origins];delta=O.volume-W.volume
    up=W.volume*z-np.einsum('vwi,i->vw',d,W.moment)+delta*maxs
    np.fill_diagonal(up,-np.inf)
    scores=up.max(axis=1)
    scores[[i for i,k in enumerate(O.origins) if k not in origins]]=np.inf
    return W,origins,scores
ids=[i for i in range(81) if i not in J19];history=[]
while len(ids)>7:
    best=None
    for i in ids:
        if i>=75:continue
        nxt=[j for j in ids if j!=i]
        try:W,orig,ss=bounds(nxt)
        except (AssertionError,ValueError):continue
        rank=np.sort(ss);obj=rank[1]
        if best is None or obj<best[0]:best=(obj,i,nxt,W,orig,ss)
    if best is None or best[0]>=-1e-7:break
    obj,i,ids,W,orig,ss=best
    rec=dict(deleted=int(i),ids=ids,protected=[int(O.origins[j]) for j in np.where(ss<0)[0]],second_bound=float(obj),volume=W.volume,centroid=W.g.tolist())
    history.append(rec)
    print(json.dumps(rec),flush=True)
with open('reduced_envelope.json','w') as f:json.dump(dict(method='greedy keep six bridge, minimize second-smallest maximum U upper bound; require <-1e-7',history=history,ids=ids),f,indent=2)
print('FLOAT_CORE_REDUCTION_FINISHED',len(ids),ids)
```

## File: replay_controls.py
```python
"""Replay observed floating controls. This is not an exact certification."""
import hashlib,json,sys
from pathlib import Path
import numpy as np
import scipy
from inputs import P75,A
from onecut import Body,centercut
from search_cut import candidate,metric,landscape

CHECKPOINTS=[
 dict(which='primary',seed=101,affine=False,eval_requested=1200,calls=1410,
      x=[-0.15291557450725846,-0.6907484451455179,0.9843207376005896],
      expected=[83,228,147,15,15,28],loss=.15579061015557683),
 dict(which='bridge',seed=102,affine=False,eval_requested=1800,calls=2118,
      x=[-1.345455923145963,-0.09460304992177006,0.5986101521953306],
      expected=[110,256,148,13,24,35],loss=.5972237107302664),
 dict(which='primary',seed=201,affine=True,eval_requested=2400,calls=3130,
      x=[-2.3504064316087607,.08333992559576231,.9122547209517811,-.01384490730458561,.0168020338655265,.0008252748911728724,.007759120298173047,-.004348926908235842],
      expected=[99,244,147,50,41,89],loss=.15530814464857823)]
KEYS=['V','E','F','S','U','H']
def replay():
    K=Body.hull(P75);O=Body.hull(np.vstack([P75,A])); out={'baselines':[K.census(),O.census()],'cuts':[],'search_checkpoints':[]}
    assert [out['baselines'][0][k] for k in KEYS]==[75,219,146,2,2,2]
    assert [out['baselines'][1][k] for k in KEYS]==[79,231,154,15,32,45]
    cases=[('bridge_old',O,K.g,[124,275,153,2,4,4]),
           ('bridge_simple',O,[.4,.1,-.3],[51,99,50,2,8,8]),
           ('primary_simple',K,[.55,-.27,-.53],[27,51,26,2,6,6]),
           ('primary_near',K,[.48,.03,-.27],[46,89,45,2,6,6]),
           ('bridge_near',O,[.38,-.12,-.31],[65,137,74,2,6,6]),
           ('primary_wide',K,[.49,.03,-.27],[46,89,45,2,6,6]),
           ('bridge_wide',O,[.5,-.05,-.36],[42,80,40,2,6,6])]
    for name,B,c,expected in cases:
        q,T,r=centercut(B,c);cen=T.census();err=float(np.linalg.norm(T.g-c))
        assert [cen[k] for k in KEYS]==expected and err<1e-10
        stable=cen['stable'];unstable=cen['unstable'];assert len(T.faces)-1 in stable
        # Cut-edge origins are indices in the input Body, not literal P75/A6 IDs.
        # Map both inherited and new vertices to the global literal input IDs.
        origins=[]
        for v in T.origins:
            origins.append([int(B.origins[j]) for j in v] if isinstance(v,list) else int(v))
        out['cuts'].append(dict(name=name,target=np.asarray(c).tolist(),q=q.tolist(),centroid_error=err,census=cen,
                               stable_global_origins=[[origins[j] for j in T.faces[f]] for f in stable],
                               unstable_global_origins=[origins[j] for j in unstable]))
        print('CUT_CONTROL',name,*[cen[k] for k in KEYS],err)
    for spec in CHECKPOINTS:
        B=K if spec['which']=='primary' else O
        T,n,h=candidate(B,np.array(spec['x']));M=metric(spec['x'][3:]) if spec['affine'] else None
        p,q=landscape(T,M);loss=sum(p)+sum(q)+max(0,len(T.edges)-249)*.005
        W=T if M is None else Body(T.p@M.T,T.faces,T.normals@np.linalg.inv(M),T.origins)
        cen=W.census();assert [cen[k] for k in KEYS]==spec['expected']
        assert abs(loss-spec['loss'])<1e-10
        out['search_checkpoints'].append(dict(spec=spec,P=p,Q=q,loss=loss,census=cen))
        print('SEARCH_CHECKPOINT',spec['which'],spec['seed'],*[cen[k] for k in KEYS],loss)
    return out
if __name__=='__main__':
    result=replay();raw=(json.dumps(result,sort_keys=True,separators=(',',':'))+'\n').encode()
    Path('floating_controls_replay.json').write_bytes(raw)
    print('FLOAT_CONTROLS_REPLAY_PASS_NO_EXACT_CLAIM')
    print('PYTHON_NUMPY_SCIPY',sys.version.split()[0],np.__version__,scipy.__version__)
    print('REPLAY_BYTES_SHA256',len(raw),hashlib.sha256(raw).hexdigest())
```
