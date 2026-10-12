# material-8a0e1e19f381

AI research material · [Export notes](../catalog/coverage.md#text-records)

---

# COORD_TREE_LP_V1 — simultaneous escape-tree feasibility with convexity guards

Status: fresh complete method source preserved BEFORE running searches. No construction or finite-search success is claimed by this material. This is not a reconstruction of the lost coordinator projective/corridor scans.

Exact consumed input dependency: accepted standalone NC57 result figure-0398, SHA256 b6c84be62ea56d1c11575d4d6309563f525d734f79b0ad2a299f0b7abd2ccdd3. Its full literal recovery capsule reconstructs all inputs. Recover with `python -B -S RECOVER_NC57.py NC57_SOURCE 4` as specified there. Use either:
- NC57_SOURCE/proof/C372_ALT_FULL_G4/REPORT.json: 14190 bytes, SHA256 639b7dd56caf48ee99f1175e20b1f305100dc0fb3f75440dd20aba8df57b4cb5; exact V64/E186/F124 own211 weak000, stable source faces0/107, unstable source vertex59.
- NC57_SOURCE/proof/C378_ALT_POLY_G6/REPORT.json: 18534 bytes, SHA256 fc46fb08252486d5c2474d70c6834b2f4849f8de25bcf18ccb059a7aa9ced661; exact V65/E189/F126 own211 weak000, stable source faces16/75, unstable source vertex50.
These are complete existing immutable inputs, not newly inferred coordinates. The source below has no imports from the parent code. All its own helpers are included.

Save the fenced code as TREE_LP.py, UTF-8 with one final newline: 9083 bytes, SHA256 856cbf05e88e788813685866e3ad5046a52f1f37065bd5c4ac54e355224ea5c0. Environment CPython3.13.5, NumPy2.3.5, SciPy1.17.0, PyTorch2.10.0+cpu, binary64, one thread as set in source. Assertions enabled.

Example fresh runs, all non-default choices explicit:
`python TREE_LP.py NC57_SOURCE/proof/C372_ALT_FULL_G4/REPORT.json LP372_ROOT107 120 107 0.001 173781`
`python TREE_LP.py NC57_SOURCE/proof/C378_ALT_POLY_G6/REPORT.json LP378_ROOT75 120 75 0.001 173782`
Terminal marker is COORD_TREE_LP_FINISHED. A NUMERICAL_WINNER.json is only a proposal and requires independent exact verification. Frozen numerical results and exact rational descendants, if any, must be preserved separately before use. Numerical solver reruns may vary across environments; their checkpoint hex values are the exact experimental record.

Method: rebuild a positive-target directed escape tree on each current primal and polar adjacency graph. At each step recompute the ordinary filled-solid centroid and differentiate all selected primal/polar witness margins. Solve a common-deficit linear program jointly with linearized full triangular-face support inequalities and trust bounds. Backtracking checks actual convexity, filled volume and edge separation, rather than merely accepting a lower penalty. The support derivatives are derivatives of the unnormalized determinant divided by the CURRENT normal length, not derivatives of moving normalized distance; exact trial inequalities use the actual new normals. Fixed triangular incidence is a restriction, not a global impossibility claim.

```python
#!/usr/bin/env python3
"""Own-centroid escape-tree sequential LP, COORD_TREE_LP_V1.
Numeric proposals only; use independent exact hull/mass/feature auditors afterward.
Usage: TREE_LP.py parent_REPORT.json new_out steps root_s [gamma=0.001] [seed=173781]
Python3.13.5 numpy2.3.5 scipy1.17.0 torch2.10.0+cpu, binary64, one thread.
Input is the exact C372 or C378 REPORT from immutable NC57 eight-body capsule.
"""
import os
for k in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS'): os.environ[k]='1'
import sys,json,hashlib
from pathlib import Path
from fractions import Fraction
import numpy as np
import torch
from scipy.optimize import linprog
from scipy.sparse import coo_matrix,csr_matrix,hstack,vstack,eye
from scipy.sparse.csgraph import dijkstra
from scipy.spatial import ConvexHull

torch.set_num_threads(1)
torch.set_default_dtype(torch.float64)
def pack(x): return json.dumps(x,sort_keys=True,separators=(',',':'))+'\n'
def hx(P): return [[float(x).hex() for x in p] for p in P]
def geometry(P,F):
    T=P[F]; a=T[:,0]; b=T[:,1]; c=T[:,2]
    w=(a*torch.linalg.cross(b,c)).sum(1)/6
    vol=w.sum(); g=(w[:,None]*(a+b+c)).sum(0)/(4*vol)
    X=P-g
    n=torch.linalg.cross(b-a,c-a)
    q=n/(n*X[F[:,0]]).sum(1)[:,None]
    return X,q,g,vol

def arrows(W,ids,targets):
    A=W[ids]; D=W[targets]-A
    return (A*D).sum(1)/(torch.linalg.vector_norm(A,dim=1)*torch.linalg.vector_norm(D,dim=1))

def graph(P,F):
    E={}
    for i,t in enumerate(F):
        for a,b in zip(t,np.roll(t,-1)):
            E.setdefault(tuple(sorted((int(a),int(b)))),[]).append(i)
    assert all(len(x)==2 for x in E.values())
    e=np.array(sorted(E),dtype=int)
    de=np.array([E[tuple(x)] for x in e],dtype=int)
    return e,de

def maxima(W,ed):
    out=np.full(len(W),-np.inf)
    for a,b in np.concatenate([ed,ed[:,::-1]],axis=0):
        v=np.dot(W[a],W[b]-W[a])/(np.linalg.norm(W[a])*np.linalg.norm(W[b]-W[a]))
        out[a]=max(out[a],v)
    return out

def tree(W,ed,root,gamma,rng):
    e=np.concatenate([ed,ed[:,::-1]],axis=0)
    diff=W[e[:,1]]-W[e[:,0]]
    ar=(W[e[:,0]]*diff).sum(1)/(np.linalg.norm(W[e[:,0]],axis=1)*np.linalg.norm(diff,axis=1))
    co=np.maximum(gamma-ar,0)**2+1e-8*(1+rng.random(len(e)))
    mat=csr_matrix((co,(e[:,1],e[:,0])),shape=(len(W),len(W)))
    ds,pre=dijkstra(mat,indices=root,return_predecessors=True)
    ids=np.array([i for i in range(len(W)) if i!=root],dtype=int)
    assert np.isfinite(ds).all() and all(pre[i]>=0 and ds[pre[i]]<ds[i] for i in ids)
    return ids,pre[ids].astype(int)

def convex_data(P,F,jacobian=False):
    nV=len(P); rows=[];cols=[];vals=[];gaps=[];rid=0
    for a,b,c in F:
        u=P[b]-P[a];v=P[c]-P[a];n=np.cross(u,v);norm=np.linalg.norm(n)
        assert norm>1e-16
        ids=np.array([i for i in range(nV) if i not in (a,b,c)],dtype=int)
        w=P[a]-P[ids];d=w@n/norm;gaps.extend(d.tolist())
        if jacobian:
            gb=np.cross(np.broadcast_to(v,w.shape),w)/norm
            gc=np.cross(w,np.broadcast_to(u,w.shape))/norm
            gn=n/norm;ga=gn-gb-gc
            for ix,i in enumerate(ids):
                for k,grad in ((a,ga[ix]),(b,gb[ix]),(c,gc[ix]),(i,-gn)):
                    rows.extend([rid]*3);cols.extend([3*k,3*k+1,3*k+2]);vals.extend(grad.tolist())
                rid+=1
    ans=np.array(gaps)
    if not jacobian:return ans
    return ans,coo_matrix((vals,(rows,cols)),shape=(rid,3*nV)).tocsr()

def summary(P,F,E,DE):
    with torch.no_grad():X,q,g,V=geometry(torch.tensor(P),F)
    x=X.numpy();q=q.numpy();eu=maxima(x,E);es=maxima(q,DE)
    mu=np.delete(eu,np.argmin(eu)).min();ms=np.delete(es,np.argmin(es)).min()
    return dict(V=len(P),E=len(E),F=len(F),S=int((es<0).sum()),U=int((eu<0).sum()),
                stable=np.where(es<0)[0].tolist(),unstable=np.where(eu<0)[0].tolist(),
                margin=float(min(mu,ms)),min_convex=float(convex_data(P,F).min()),
                volume=float(V),centroid=g.tolist(),min_edge=float(np.linalg.norm(x[E[:,0]]-x[E[:,1]],axis=1).min()))

def main(parent,out,steps,root_s,gamma=.001,seed=173781):
    data=Path(parent).read_bytes();d=json.loads(data);F=np.array(d['faces'],dtype=int)
    assert F.shape[1]==3 and d['own']['counts']==[2,1,1]
    P=np.array([[float(Fraction(x)) for x in row] for row in d['points']])
    E,DE=graph(P,F);assert len(E)==d['E']
    with torch.no_grad():X,q,g,V=geometry(torch.tensor(P),F)
    scale=float(torch.sqrt((X.square().sum(1)).mean()));P=X.numpy()/scale
    out=Path(out);out.mkdir(parents=True,exist_ok=False)
    (out/'INPUT_REPORT.json').write_bytes(data)
    rng=np.random.default_rng(seed);root_u=int(d['own']['U'][0]);D=P.size
    options=dict(steps=steps,root_s=root_s,root_u=root_u,gamma=gamma,seed=seed,initial_trust=.005,max_trust=.12,
                 convex_floor=1e-10,lp_feasibility=1e-9,L1_weight=1e-5,tree_refresh=5,version='COORD_TREE_LP_V1')
    (out/'OPTIONS.json').write_text(pack(dict(options=options,parent_sha256=hashlib.sha256(data).hexdigest(),scale_hex=scale.hex())))
    trust=.005;records=[];best=(999.,float('inf'));targets=None;accepted=0;treeage=0
    initial=summary(P,F,E,DE);minvol=initial['volume']*.2;edgefloor=initial['min_edge']*.15
    def keep(P,rec,label):
        (out/(label+'.json')).write_text(pack(dict(record=rec,points_hex=hx(P),faces=F.tolist(),options=options)))
    keep(P,initial,'INITIAL')
    for it in range(steps):
        with torch.no_grad():X,q,g,vol=geometry(torch.tensor(P),F)
        if targets is None or treeage>=5:
            ui,ut=tree(X.numpy(),E,root_u,gamma,rng);si,st=tree(q.numpy(),DE,root_s,gamma,rng)
            targets=(ui,ut,si,st);treeage=0
        ui,ut,si,st=targets
        def witness(z):
            x,q,g,v=geometry(z.reshape((-1,3)),F)
            return torch.cat((arrows(x,ui,ut),arrows(q,si,st)))
        z=torch.tensor(P.ravel(),requires_grad=True)
        e=witness(z).detach().numpy()
        J=torch.autograd.functional.jacobian(witness,z,vectorize=True).numpy()
        cg,CJ=convex_data(P,F,True);m=len(e)
        # Variables delta[D], absolute(delta)[D], common nonnegative deficit t.
        A=vstack([hstack([-csr_matrix(J),csr_matrix((m,D)),-np.ones((m,1))]),
                  hstack([-CJ,csr_matrix((len(cg),D+1))]),
                  hstack([eye(D),-eye(D),csr_matrix((D,1))]),
                  hstack([-eye(D),-eye(D),csr_matrix((D,1))])],format='csr')
        b=np.r_[e-gamma,cg-1e-10,np.zeros(2*D)]
        obj=np.r_[np.zeros(D),np.full(D,1e-5/D),1.]
        lp=linprog(obj,A_ub=A,b_ub=b,bounds=[(-trust,trust)]*D+[(0,trust)]*D+[(0,None)],method='highs',options={'primal_feasibility_tolerance':1e-9,'dual_feasibility_tolerance':1e-9})
        rec=dict(iteration=it,trust=trust,lp_status=int(lp.status),lp_message=str(lp.message),tree_s=[si.tolist(),st.tolist()],tree_u=[ui.tolist(),ut.tolist()])
        ok=False
        if lp.success:
            delta=lp.x[:D].reshape(P.shape);def0=np.maximum(gamma-e,0);merit0=float(def0.max()+.2*def0.mean())
            pred=np.maximum(gamma-e-J@delta.ravel(),0);meritpred=float(pred.max()+.2*pred.mean())
            rec.update(lp_t=float(lp.x[-1]),merit0=merit0,meritpred=meritpred,max_delta=float(np.abs(delta).max()))
            for ls in range(14):
                alpha=2.**(-ls);trial=P+alpha*delta
                try:
                    cmin=float(convex_data(trial,F).min())
                    ar=witness(torch.tensor(trial.ravel())).detach().numpy();de=np.maximum(gamma-ar,0)
                    merit=float(de.max()+.2*de.mean());r=summary(trial,F,E,DE)
                    feasible=cmin>0 and r['volume']>minvol and r['min_edge']>edgefloor and np.isfinite(ar).all()
                    if feasible and merit<merit0-1e-5*alpha*max(merit0-meritpred,1e-12):
                        P=trial;accepted+=1;treeage+=1;ok=True;rec.update(alpha=alpha,merit=merit,body=r)
                        trust=min(.12,trust*(1.35 if alpha==1 else .8));break
                except (AssertionError,ValueError,np.linalg.LinAlgError):pass
        if not ok:
            trust*=.5;targets=None
            rec['body']=summary(P,F,E,DE)
        rec['accepted']=ok;records.append(rec)
        r=rec['body'];key=(r['S']+r['U'],-r['margin'])
        if key<best:
            best=key;keep(P,rec,'BEST');print('TREE_LP_BEST',it,r,flush=True)
        (out/'TRACE.json').write_text(pack(records));keep(P,rec,'CURRENT')
        print('TREE_LP_STEP',it,ok,trust,rec.get('lp_t'),r['S'],r['U'],r['margin'],flush=True)
        if r['S']==r['U']==1:
            keep(P,rec,'NUMERICAL_WINNER');break
        if trust<1e-8:
            rec['stop_reason']='trust_floor';break
    r=summary(P,F,E,DE);H=ConvexHull(P)
    res=dict(final=r,best_key=best,accepted_steps=accepted,iterations=len(records),numeric_extreme_vertices=len(H.vertices),numeric_triangles=len(H.simplices))
    (out/'SUMMARY.json').write_text(pack(res));print('COORD_TREE_LP_FINISHED',res,flush=True)
if __name__=='__main__':
    main(sys.argv[1],sys.argv[2],int(sys.argv[3]),int(sys.argv[4]),float(sys.argv[5]) if len(sys.argv)>5 else .001,int(sys.argv[6]) if len(sys.argv)>6 else 173781)
```
