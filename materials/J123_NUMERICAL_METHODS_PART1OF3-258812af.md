# material-258812af3a1e

AI research material · [Export notes](../catalog/coverage.md#text-records)

<!-- historical-status:start -->
> **Historical AI material.** The title and claims below reflect the AI’s assessment at the time. Claims of proof, certification or completion are not a current verification verdict.
>
> [C622](../C622/README.md) passes the supplied exact checks; C<500 remains open; Minimum’s C≥34 remains a working lower bound requiring a consolidated proof. See [verification status and source gaps](../catalog/coverage.md).
<!-- historical-status:end -->

---

# J123 numerical methods — Recovery capsule part 1/3

Object identity: J123 actual-mass free-V whole-landscape continuation. Parts1–3 together contain every numerical producing source used for the reported capacity/bar-flow/fan/surgery experiments and their failed initial controls. Exact bodies and their standalone rational auditor are separately complete in [internal-source-reference], J123_EXACT_V_AND_FLIPWALL_RECOVERY.md. This is NOT an own110 construction. All floating topology, signs and bars below are nominations; exact endpoint claims use that rational package.

Part1 contains geometry123.py, jointwide123.py and safecap123.py. Part2 supplies finite fan-bundle/bar-flow/surgery variants. Part3 supplies the remaining failed SLSQP controls, derivative diagnosis and complete literal floating checkpoint coordinates. A fresh numerical successor needs all relevant complete units, not merely their names. Save fenced units under their headings with terminal newlines.

## Environment and executed path
Python3.13.5 (GCC14.2), NumPy2.3.5, SciPy1.17.0, PyTorch2.10.0+cpu, torch.float64, single thread. Shell variables OMP_NUM_THREADS=1, OPENBLAS_NUM_THREADS=1, MKL_NUM_THREADS=1 were set. No random search is used in the successful finite trajectory; only failed-control finite-difference directions use seed123010. No dependencies from the older KF optimizer archive are needed: exact initial KF27G_QDESC_G4.txt is literal in the separate exact recovery.

Executed commands, in order from the same directory (all source parts installed):
```sh
python safecap123.py KF27G_QDESC_G4.txt safecapA 100 .01 1e-6 1
python bundlecap123.py safecapA.json bundleB 100 .01 1e-6 1
python bufferedcap123.py bundleB.json bufferedC 150 .01 1e-6 1
python bufferedcap123.py bufferedC.json bufferedD 200 .01 1e-6 1
python barflow123.py bufferedD.json barE 150 .01 1e-6 1 1e-4 .1
python fullbarflow123.py barE.json fullF 40 .01 1e-6 1 1e-4 0
python surgery123.py fullF.json surgeryG
python barflow123.py surgeryG.0.json starH 100 .01 1e-6 1 1e-4 .1
```
JSON output includes wall-clock seconds, so its full-byte hash is not a deterministic replay target. Literal checkpoints in part3 preserve exact binary64 inputs via round-tripping decimal coordinates. Exact G8 descendants are fixed separately as integer data. Platform/optimizer changes may alter numerical trajectories even with the supplied package versions; do not claim otherwise.

Observed finite endings, not requested-step counts: safecapA18 accepted then stopped at iteration18; bundleB100 accepted; bufferedC150 accepted; bufferedD200 accepted; barE84 accepted then stopped at iteration84; fullF4 accepted then stopped at iteration4; surgeryG527 finite proposals/94 admitted U1, top centroid stellar addition; starH100 accepted. None is a proved all-geometry obstruction, and none is own110. The finite acceptor, not the SLSQP status, enforces actual rebuilt hull/mass/opposite-landscape guards.

A scalar whole-root widest capacity is continuous/Lipschitz in its score matrix, whereas summing deficits of an arbitrarily selected equally-wide tree can jump when that tree changes. jointwide123.py preserves this failed objective for transparency and supplies the usable widest_tree routine. A capacity increase need not lower persistence: safecapA improves the angular capacity from about-.6563302 to-.5398168 but its sole Q grows from about.7609718 to.7642884. Later bar descent lowers the main Q while creating subsidiary Q. Do not report only a primary scalar as complete cancellation.

File identities (bytes,SHA256):
geometry123.py 4942 451f4fd3dda314c65539c908bbe29cd7b1d4f73bedcf1d8a9e8f18a85afbe2ab
jointwide123.py 5678 cf52389c39412f271240d618ce4b1b8d062b0d29acf99c01138e69f3b2385252
safecap123.py 4128 b41ec385f43c311a69b369f08d2a81c1e5400ba92dff3f81a5fcd28d1041ad43

## geometry123.py
```python
"""Live V-hull, homogeneous mass, and normalized global-chord witnesses.
Floating nomination only: the exact endpoint auditor is separate.
"""
from __future__ import annotations
import json
from pathlib import Path
from dataclasses import dataclass
import numpy as np
from scipy.spatial import ConvexHull
import torch

torch.set_num_threads(1)
torch.set_default_dtype(torch.float64)


def load_points(path: str | Path) -> np.ndarray:
    p=Path(path)
    if p.suffix=='.json':
        d=json.loads(p.read_text())
        return np.asarray(d['points'],dtype=float)
    data=p.read_text().split(); n=int(data[0]); D=int(data[1])
    assert len(data)==2+3*n and D>0
    return np.array([int(t)/D for t in data[2:]]).reshape(n,3)


def triangulate(x: np.ndarray):
    hull=ConvexHull(x)
    tris=hull.simplices.copy()
    cr=np.cross(x[tris[:,1]]-x[tris[:,0]],x[tris[:,2]]-x[tris[:,0]])
    rev=np.einsum('ij,ij->i',cr,hull.equations[:,:3])<0
    tris[rev]=tris[rev][:,[0,2,1]]
    # Use the complete triangulated boundary for integration, one representative
    # per maximal plane for polar witnesses. Grouping is numerical, not a proof.
    keys=np.round(hull.equations,10)
    _, reps=np.unique(keys,axis=0,return_index=True)
    reps=np.sort(reps)
    return tris,tris[reps],np.sort(hull.vertices),hull


def live_values(x: torch.Tensor, tris: np.ndarray, faces: np.ndarray):
    a,b,c=(x[tris[:,k]] for k in range(3))
    anchor=x.mean(dim=0)
    vols=((a-anchor)*torch.linalg.cross(b-anchor,c-anchor)).sum(dim=1)/6
    volume=vols.sum()
    centroid=(vols[:,None]*(a+b+c+anchor)/4).sum(dim=0)/volume
    aa,bb,cc=(x[faces[:,k]] for k in range(3))
    normals=torch.linalg.cross(bb-aa,cc-aa)
    offsets=(normals*(aa-centroid)).sum(dim=1)
    q=normals/offsets[:,None]
    return volume,centroid,x-centroid,q


def angular(x: torch.Tensor):
    d=x[None,:,:]-x[:,None,:]
    denom=torch.linalg.vector_norm(x,dim=1)[:,None]*torch.linalg.vector_norm(d,dim=2).clamp_min(1e-30)
    scores=(x[:,None,:]*d).sum(dim=2)/denom
    return scores-torch.eye(len(x),dtype=x.dtype,device=x.device)*1e6


def bars_numeric(x: np.ndarray, edges):
    r=np.einsum('ij,ij->i',x,x)
    events=[]
    for a,b in edges:
        d=x[b]-x[a];dd=float(d@d)
        t=np.clip(-x[a]@d/dd,0.,1.)
        z=x[a]+t*d
        events.append((float(z@z),int(a),int(b)))
    events.sort(key=lambda z:(-z[0],z[1],z[2]))
    par=np.arange(len(x)); components=[{i} for i in range(len(x))]
    def find(a):
        while par[a]!=a:
            par[a]=par[par[a]];a=int(par[a])
        return a
    out=[]
    for lev,i,j in events:
        a,b=find(i),find(j)
        if a==b:continue
        if r[a]<r[b] or (r[a]==r[b] and a>b):a,b=b,a
        depth=1-lev/r[b]
        if depth>1e-12:out.append({'root':b,'edge':[i,j],'depth':float(depth),'component':sorted(components[b])})
        par[b]=a;components[a]|=components[b]
    return sorted(out,key=lambda z:-z['depth'])


def stats(x: np.ndarray):
    tris,faces,vertices,hull=triangulate(x)
    xt=torch.tensor(x);V,g,p,q=live_values(xt,tris,faces)
    P=p.detach().numpy();Q=q.detach().numpy()
    ap=angular(p).max(dim=1).values.detach().numpy()
    aq=angular(q).max(dim=1).values.detach().numpy()
    # For generic triangulated point hulls; coplanar triangles are merged below.
    face_sets=[]
    for t in faces:
        n=np.cross(x[t[1]]-x[t[0]],x[t[2]]-x[t[0]])
        norm=np.linalg.norm(n)
        on=np.flatnonzero(abs((x-x[t[0]])@n)<1e-9*norm)
        face_sets.append(set(map(int,on)))
    edges=[];dual=[]
    for i in range(len(faces)):
        for j in range(i):
            it=face_sets[i]&face_sets[j]
            if len(it)==2:
                edges.append(tuple(sorted(it)));dual.append((i,j))
    pe=bars_numeric(P,edges);qe=bars_numeric(Q,dual)
    return {'V':len(vertices),'E':len(edges),'F':len(faces),'volume':float(V),
            'centroid':g.detach().numpy().tolist(),'U':np.flatnonzero(ap<-1e-10).tolist(),
            'S':np.flatnonzero(aq<-1e-10).tolist(),'P':pe,'Q':qe,
            'p_guards':ap.tolist(),'q_guards':aq.tolist(),'faces':faces.tolist()}


def positive_tree(x: np.ndarray, root: int | None=None):
    a=angular(torch.tensor(x)).numpy()
    if root is None:root=int(np.argmax((x*x).sum(axis=1)))
    parents=np.argmax(a,axis=1)
    parents[root]=-1
    assert all(a[i,parents[i]]>0 for i in range(len(x)) if i!=root)
    for i in range(len(x)):
        seen=set();k=i
        while k!=root:
            assert k not in seen;seen.add(k);k=int(parents[k])
    return root,parents


def reference_tree_guards(x: torch.Tensor, root:int, parents:np.ndarray):
    ids=np.array([i for i in range(len(x)) if i!=root])
    d=x[parents[ids]]-x[ids]
    return (x[ids]*d).sum(dim=1)/(torch.linalg.vector_norm(x[ids],dim=1)*torch.linalg.vector_norm(d,dim=1)).clamp_min(1e-30)


if __name__=='__main__':
    import sys
    out=stats(load_points(sys.argv[1]));print(json.dumps(out,indent=2))
```

## jointwide123.py
```python
"""Simultaneous actual-mass / physical-tree / polar-deficit search.
A floating nomination method, never an exact certificate.
Usage: python joint123.py input output_prefix steps trust tauP tauQ mode
mode='gauge' imposes g=0 and fixes one root; mode='free' fixes the root
without the centre gauge, using actual-centred guards throughout.
"""
from __future__ import annotations
import json,sys,time
from pathlib import Path
import numpy as np
import torch
from scipy.optimize import minimize
from geometry123 import load_points,triangulate,live_values,angular,stats,positive_tree,reference_tree_guards

def widest_tree(q: torch.Tensor):
    a=angular(q).detach().numpy();n=len(q)
    root=int(torch.argmax((q*q).sum(dim=1)).detach())
    capacity=np.full(n,-np.inf);capacity[root]=np.inf
    parents=np.full(n,-1,dtype=int);settled=np.zeros(n,dtype=bool)
    for _ in range(n):
        k=int(np.argmax(np.where(settled,-np.inf,capacity)))
        settled[k]=True
        for i in np.flatnonzero(~settled):
            c=min(float(a[i,k]),float(capacity[k]))
            if c>capacity[i]:capacity[i]=c;parents[i]=k
    return root,parents

class Joint:
    def __init__(self,x,taup,tauq,mode):
        tr,fa,_,_=triangulate(x);_,g,_,_=live_values(torch.tensor(x),tr,fa)
        self.x0=x-g.numpy();self.root,self.parents=positive_tree(self.x0)
        self.ids=np.array([i for i in range(len(x)) if i!=self.root])
        self.fixed=torch.tensor(self.x0[self.root:self.root+1])
        self.base=torch.tensor(self.x0);self.taup=taup;self.tauq=tauq;self.mode=mode
        self.v0=float(live_values(self.base,tr,fa)[0]);self.scale=np.linalg.norm(self.x0[self.root])
        self.cached=None;self.count=0;self.best=None;self.trace=[]
    def points(self,z):
        return self.base.index_copy(0,torch.tensor(self.ids),z.reshape(-1,3))
    def evaluate(self,z):
        if self.cached is not None and np.array_equal(z,self.cached[0]):return self.cached[1]
        x=self.x0.copy();x[self.ids]=np.reshape(z,(-1,3));tr,fa,_,_=triangulate(x)
        zt=torch.tensor(z,requires_grad=True)
        def values(t):
            xx=self.points(t);v,g,p,q=live_values(xx,tr,fa)
            pguards=reference_tree_guards(p,self.root,self.parents)
            qr,qp=widest_tree(q)
            scores=reference_tree_guards(q,qr,qp)
            deficit=torch.relu(self.tauq-scores)
            objective=(deficit*deficit).sum()
            eq=g/self.scale if self.mode=='gauge' else g[:0]
            ineq=torch.cat((pguards-self.taup,(v/self.v0-.05).reshape(1)))
            return torch.cat((objective.reshape(1),eq,ineq))
        val=values(zt)
        jac=torch.autograd.functional.jacobian(values,zt,vectorize=True)
        a=val.detach().numpy();j=jac.detach().numpy()
        ne=3 if self.mode=='gauge' else 0
        out=(a[0],j[0],a[1:1+ne],j[1:1+ne],a[1+ne:],j[1+ne:])
        self.count+=1
        eqerr=float(np.max(np.abs(out[2]),initial=0));mi=float(min(out[4]))
        if mi>=-1e-10 and eqerr<=1e-8:
            if self.best is None or a[0]<self.best['objective']:
                self.best={'points':x.tolist(),'objective':float(a[0]),'min_constraint':mi,'eqerr':eqerr,'evaluation':self.count}
        self.cached=(np.array(z).copy(),out)
        return out
    def callback(self,z):
        e=self.evaluate(z);row={'iteration':len(self.trace)+1,'evaluations':self.count,'objective':float(e[0]),'eqerr':float(np.max(np.abs(e[2]),initial=0)),'min_constraint':float(min(e[4]))}
        self.trace.append(row)
        if len(self.trace)%10==0:print(json.dumps(row),flush=True)

def run(inp,prefix,steps,trust,taup,tauq,mode):
    x=load_points(inp);p=Joint(x,taup,tauq,mode);z=p.x0[p.ids].ravel()
    e=p.evaluate(z);rng=np.random.default_rng(123010);d=rng.normal(size=z.size);d/=np.linalg.norm(d)
    h=1e-7;fd=(p.evaluate(z+h*d)[0]-p.evaluate(z-h*d)[0])/(2*h);ad=float(e[1]@d)
    derivative={'direction_seed':123010,'h':h,'analytic':ad,'central_difference':fd,'absolute_error':abs(fd-ad)}
    cons=[{'type':'ineq','fun':lambda t:p.evaluate(t)[4],'jac':lambda t:p.evaluate(t)[5]}]
    if mode=='gauge':cons.append({'type':'eq','fun':lambda t:p.evaluate(t)[2],'jac':lambda t:p.evaluate(t)[3]})
    t=time.monotonic()
    res=minimize(lambda t:p.evaluate(t)[:2],z,jac=True,method='SLSQP',bounds=list(zip(z-trust,z+trust)),constraints=cons,callback=p.callback,options={'maxiter':steps,'ftol':1e-12,'disp':False})
    xx=p.x0.copy();xx[p.ids]=res.x.reshape(-1,3)
    out={'input':str(inp),'points':xx.tolist(),'status':int(res.status),'message':str(res.message),'success':bool(res.success),'iterations':int(res.nit),'evaluations':p.count,'seconds':time.monotonic()-t,'parameters':{'steps':steps,'trust':trust,'tauP':taup,'tauQ':tauq,'mode':mode,'ftol':1e-12,'volume_floor_fraction':.05},'root':p.root,'parents':p.parents.tolist(),'derivative':derivative,'trace':p.trace,'stats':stats(xx),'best':p.best}
    Path(prefix+'.json').write_text(json.dumps(out,indent=2)+'\n')
    if p.best is not None:
        p.best['stats']=stats(np.array(p.best['points']));Path(prefix+'.best.json').write_text(json.dumps(p.best,indent=2)+'\n')
    print(json.dumps({k:out[k] for k in ['status','message','iterations','evaluations','seconds','derivative']}),flush=True)
    for label,s in [('last',out['stats']),('best',p.best['stats'] if p.best else None)]:
        if s:print(label,json.dumps({'VEF':[s[k] for k in ['V','E','F']],'SU':[len(s['S']),len(s['U'])],'Q':[a['depth'] for a in s['Q']],'P':[a['depth'] for a in s['P']],'g':s['centroid']}),flush=True)
if __name__=='__main__':
    run(sys.argv[1],sys.argv[2],int(sys.argv[3]),float(sys.argv[4]),float(sys.argv[5]),float(sys.argv[6]),sys.argv[7])
```

## safecap123.py
```python
"""Actual-hull safeguarded Q-capacity ascent with a complete U1 forest.
Each QP freezes only the derivative chart; every admitted finite point rebuilds
its hull, mass, physical forest and widest polar path capacity.
Floating discovery, not exact certification. SLSQP solves a convex quadratic
linearized direction subproblem, never serving as the finite feasibility test.
"""
from __future__ import annotations
import json,sys,time
from pathlib import Path
import numpy as np
import torch
from scipy.optimize import minimize
from geometry123 import load_points,triangulate,live_values,angular,positive_tree,reference_tree_guards,stats
from jointwide123 import widest_tree

def values(x,derivatives=False):
    tr,fa,_,_=triangulate(x);xt=torch.tensor(x,requires_grad=True)
    v,g,p,q=live_values(xt,tr,fa);pr,pp=positive_tree(p.detach().numpy());qr,qp=widest_tree(q)
    ids=np.array([i for i in range(len(x)) if i!=pr]);base=xt.detach()
    def guards(z):
        xx=base.index_copy(0,torch.tensor(ids),z.reshape(-1,3))
        vv,gg,px,qx=live_values(xx,tr,fa)
        pg=reference_tree_guards(px,pr,pp);qg=reference_tree_guards(qx,qr,qp)
        return torch.cat((pg,qg,vv.reshape(1)))
    z=xt[ids].reshape(-1).detach().requires_grad_();val=guards(z)
    result={'volume':float(v.detach()),'centroid':g.detach().numpy(),'p':val[:len(x)-1].detach().numpy(),'q':val[len(x)-1:-1].detach().numpy(),'capacity':float(val[len(x)-1:-1].min().detach()),'ids':ids,'rootP':pr,'rootQ':qr,'parentsP':pp,'parentsQ':qp,'faces':fa}
    if derivatives:result['jac']=torch.autograd.functional.jacobian(guards,z,vectorize=True).detach().numpy()
    return result

def run(inp,prefix,steps,trust,taup,ridge):
    x=load_points(inp);v0=values(x)['volume'];trace=[];frames=[];rejected=0
    begin=time.monotonic()
    for it in range(steps):
        a=values(x,True);np_=len(a['p']);nq=len(a['q']);J=a['jac'];n=J.shape[1];cap=a['capacity']
        # Linear constraints p+Jp*d>=tauP, q+Jq*d>=cap+improvement.
        A=np.zeros((np_+nq+1,n+1));A[:,:n]=J;A[np_:np_+nq,n]=-1
        b=np.r_[a['p']-taup,a['q']-cap,a['volume']-.05*v0]
        def fun(y):return .5*ridge*(y[:n]@y[:n])-y[n],np.r_[ridge*y[:n],-1.]
        sub=minimize(fun,np.zeros(n+1),jac=True,method='SLSQP',constraints=[{'type':'ineq','fun':lambda y:A@y+b,'jac':lambda y:A}],bounds=[(-trust,trust)]*n+[(-.01,.05)],options={'ftol':1e-12,'maxiter':200})
        d=sub.x[:n].reshape(-1,3);gain=float(sub.x[n]);ok=False
        for ls in range(18):
            alpha=2.**(-ls);xx=x.copy();xx[a['ids']]+=alpha*d
            try:aa=values(xx)
            except (AssertionError,ValueError,RuntimeError):rejected+=1;continue
            if min(aa['p'])>=taup-1e-11 and aa['volume']>=.05*v0 and aa['capacity']>cap+max(1e-11,1e-4*alpha*max(gain,0)):
                ok=True;break
            rejected+=1
        row={'iteration':it,'capacity':cap,'predicted_gain':gain,'subproblem_status':int(sub.status),'subproblem_min':float(min(A@sub.x+b)),'accepted':ok,'alpha':alpha,'direction_linf':float(np.max(abs(d))),'minP':float(min(a['p'])),'facets':len(a['faces'])}
        if ok:
            x=xx;row['new_capacity']=aa['capacity'];row['new_minP']=float(min(aa['p']));frames.append(x.tolist())
        trace.append(row)
        if it%10==0 or not ok:print(json.dumps(row),flush=True)
        if not ok:break
        if aa['capacity']>0:break
    out={'points':x.tolist(),'input':str(inp),'parameters':{'steps':steps,'trust':trust,'tauP':taup,'ridge':ridge,'line_search_steps':18,'volume_floor_fraction':.05,'qp_maxiter':200,'qp_ftol':1e-12,'gain_bound':[-.01,.05]},'trace':trace,'frames':frames,'rejected':rejected,'seconds':time.monotonic()-begin,'stats':stats(x)}
    Path(prefix+'.json').write_text(json.dumps(out,indent=2)+'\n');s=out['stats']
    print(json.dumps({'accepted':len(frames),'Q':[b['depth'] for b in s['Q']],'P':[b['depth'] for b in s['P']],'SU':[len(s['S']),len(s['U'])],'VEF':[s[k] for k in ['V','E','F']],'seconds':out['seconds']}),flush=True)
if __name__=='__main__':run(sys.argv[1],sys.argv[2],int(sys.argv[3]),float(sys.argv[4]),float(sys.argv[5]),float(sys.argv[6]))
```
