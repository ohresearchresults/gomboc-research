# material-fd3362c3ec46

Historical AI scientific source/proof material. Statements retain their original scope; this is not an independently reviewed theorem.

Public derivative: internal-record-identifiers-replaced.

---

# Recovery capsule part 1/2 — HARD_U1_B_C162

Complete actually executed discovery sources. Part2 supplies complete literal exact G5/G8 outputs and the exact binary64 intermediate input for the second search. This method is not a proof of optimality, convergence, or infeasibility. Exact controls are recovered from literal coordinates rather than assumed bitwise repeatability of floating optimization.

Environment observed: CPython3.13.5, NumPy2.3.5, SciPy1.17.0, torch2.10.0+cpu. OPENBLAS_NUM_THREADS=1, OMP_NUM_THREADS=1, torch threads1, torch default float64. No web inputs. Input FREE_LIVE_FULLBAR_G8.json is the980-byte exact file in owned [internal-source-reference], SHA01ae955a622475409f6fb70c90143651eeff5d433279461b3d0c92632c4c53b0. That material also contains the complete exact_poly.py6134B SHA898f77989193886996d6f2dc121ccdfdf611b8a9ac52fd3207557eac6a69c0c4; select it explicitly as a recovery dependency.

Commands actually executed:
`OPENBLAS_NUM_THREADS=1 python margin_search.py FREE_LIVE_FULLBAR_G8.json --eps .0003 --weight 1 --maxiter 1500 --out MARGIN_G8_E3`
`OPENBLAS_NUM_THREADS=1 python constrained_search.py FREE_LIVE_FULLBAR_G8.json --eps .00001 --maxiter 150 --out HARD_U1_A`
`OPENBLAS_NUM_THREADS=1 python constrained_search.py HARD_U1_A.npy --eps .0001 --maxiter 700 --out HARD_U1_B`
The first soft search ended after8 iterations/76 evaluations, objective.0016607973356462524, floatS6/U24. Hard-U first run150 iterations/889 evaluations, objective2.084370156044124e-5, floatS3/U4, hence some hard inequalities still violated at iteration limit. Second run108 iterations/577 evaluations, objective2.211674277774467e-6, floatingV29/E81/F54,S2/U1, success reported. Exact certification and persistence are separate in part2. An earlier unvectorized Jacobian execution timed out without a result; the complete actually finishing source below uses batched derivatives. No missing helper files.

The centroid uses signed tetrahedra from the average input point, recomputed on the same current hull as carrier inequalities. All-points escape witnesses are equivalent to existence of a tangent-cone edge with positive radial derivative. Interior input points are excluded from U constraints. A positive direct margin avoids treating a tiny persistence-depth number as cancellation, but the objective remains local and can stall at carrier changes. The single exempt stable face is chosen by largest squared positive side-margin, not necessarily by least support distance: this root-choice ambiguity is a live limitation. F/E in floating diagnose assume a generic simplicial hull; exact_poly separately enumerates and rejects nonsimplicial facets, so a floating E alone is not a certificate.

Save each file with exactly one trailing LF. Manifests:
margin_search.py5245B SHAd5be4ca00fb7f67a87de14296c5e2eaf1dbec2394ffda5bcb4fd26a524d6e9e6
constrained_search.py3470B SHA1e37c787c05a9a1b24e4a718078e2c7e63733b8129b193b0a51a696e846e5c66

## margin_search.py
```python
"""Actual-volume-centroid search with linear geometric exclusion margins.
Float discovery only; exact audit required for acceptance. Every evaluation builds
its own convex hull, so volume/centroid and carrier geometry describe the same body.
"""
import os
os.environ.setdefault('OMP_NUM_THREADS','1')
import json,sys,time,hashlib
from pathlib import Path
import numpy as np
from scipy.spatial import ConvexHull,QhullError
from scipy.optimize import minimize
import torch

torch.set_num_threads(1)
torch.set_default_dtype(torch.float64)

def faces(x):
    hull=ConvexHull(x)
    tri=hull.simplices.copy()
    nr=np.cross(x[tri[:,1]]-x[tri[:,0]],x[tri[:,2]]-x[tri[:,0]])
    flip=(nr*hull.equations[:,:3]).sum(1)<0
    tri[flip]=tri[flip][:,[0,2,1]]
    return hull,tri

def terms(t,tri):
    p=t[tri]
    # Translation-stable tetrahedra from an interior reference, not world zero.
    r=t.mean(0)
    q=p-r
    vol6=(q[:,0]*torch.linalg.cross(q[:,1],q[:,2])).sum(1)
    vol=vol6.sum()/6
    c=(vol6[:,None]*(p.sum(1)+r)/4).sum(0)/vol6.sum()
    edges=torch.roll(p,-1,1)-p
    raw=torch.linalg.cross(edges[:,0],-edges[:,2])
    area2=torch.linalg.vector_norm(raw,dim=1)
    n=raw/area2[:,None]
    h=((p[:,0]-c)*n).sum(1)
    inward=torch.linalg.cross(n[:,None,:].expand_as(edges),edges)
    side=((c-p)*inward).sum(2)/torch.linalg.vector_norm(edges,dim=2)
    # All-vertex escape witnesses are equivalent to tangent-cone edge witnesses.
    d=t[None,:,:]-t[:,None,:]
    ll=torch.linalg.vector_norm(d,dim=2)
    eye=torch.eye(len(t),dtype=torch.bool)
    escape=((t-c)[:,None,:]*d).sum(2)/(ll+eye)
    escape=escape.masked_fill(eye,-1e10).max(1).values
    outside=side.min(1).values
    return c,vol,escape,outside,h,area2,n

def diagnose(x):
    hu,tr=faces(x); idx=hu.vertices
    t=torch.tensor(x)
    with torch.no_grad(): c,v,u,s,h,a,n=terms(t,torch.tensor(tr))
    u=u.numpy();s=s.numpy();c=c.numpy();h=h.numpy()
    return dict(V=len(idx),E=len(hu.simplices)*3//2,F=len(tr),C=len(tr)*3,
        S=int((s>0).sum()),U=int((u[idx]<0).sum()),centroid=c.tolist(),volume=float(v),
        Sfaces=[dict(ids=tr[i].tolist(),margin=float(s[i]),height=float(h[i])) for i in np.where(s>0)[0]],
        Uvertices=[dict(id=int(i),margin=float(-u[i])) for i in idx if u[i]<0],
        max_bad_S=float(np.sort(s)[-2]), max_bad_U=float(np.sort(-u[idx])[-2]),
        min_area2=float(a.min()))

class Objective:
    def __init__(self,x,eps,weight=1.,trust=0.):
        self.x0=x.copy();self.eps=eps;self.weight=weight;self.trust=trust
        self.v0=diagnose(x)['volume'];self.eval=0;self.best=np.inf;self.bestx=x.copy();self.history=[]
    def __call__(self,y):
        self.eval+=1;x=y.reshape(-1,3)
        try: hu,tri=faces(x)
        except QhullError: return 1e8,np.zeros_like(y)
        t=torch.tensor(x,requires_grad=True)
        c,v,u,s,h,a,n=terms(t,torch.tensor(tri))
        # Interior input points aren't physical vertices and must not be penalized as U.
        u=u[hu.vertices]
        pu=torch.relu(self.eps-u).square(); ps=torch.relu(self.eps+s).square()
        pu=pu.sum()-pu.max();ps=ps.sum()-ps.max()
        # Prevent macroscopic collapse and unbounded expansion; not a physical constraint.
        vr=v/self.v0
        guard=10*(torch.relu(.25-vr)**2+torch.relu(vr-4)**2)
        guard+=torch.relu(.02-h).square().sum()
        reg=self.trust*torch.sum((t-torch.tensor(self.x0))**2)
        loss=ps+self.weight*pu+guard+reg
        loss.backward();value=float(loss.detach())
        if value<self.best:
            self.best=value;self.bestx=x.copy()
            if not self.history or value<.98*self.history[-1][1]:
                self.history.append([self.eval,value,float(ps.detach()),float(pu.detach()),float(v.detach())])
        return value,t.grad.numpy().ravel()

def run(x,eps,weight,maxiter,out,trust=0.):
    obj=Objective(x,eps,weight,trust)
    start=diagnose(x);tic=time.time()
    result=minimize(obj,x.ravel(),jac=True,method='L-BFGS-B',options={'maxiter':maxiter,'ftol':1e-15,'gtol':1e-10,'maxls':40,'maxcor':25})
    x=obj.bestx
    np.save(out+'.npy',x)
    report=dict(eps=eps,weight=weight,trust=trust,maxiter=maxiter,start=start,end=diagnose(x),objective=obj.best,eval=obj.eval,iterations=result.nit,message=str(result.message),seconds=time.time()-tic,history=obj.history)
    Path(out+'.json').write_text(json.dumps(report,indent=2)+'\n')
    print(json.dumps({k:v for k,v in report.items() if k not in ['history','start','end']})+'\nEND '+json.dumps(report['end']),flush=True)
    return x

if __name__=='__main__':
    import argparse
    a=argparse.ArgumentParser();a.add_argument('input');a.add_argument('--eps',type=float,default=1e-4);a.add_argument('--weight',type=float,default=1.);a.add_argument('--trust',type=float,default=0.);a.add_argument('--maxiter',type=int,default=1000);a.add_argument('--out',default='MARGIN');a.add_argument('--diagnose',action='store_true');args=a.parse_args()
    if args.input.endswith('.npy'):x=np.load(args.input)
    else:
        raw=json.loads(Path(args.input).read_text());x=np.array(raw['points'],dtype=float)/raw['denominator']
    if args.diagnose: print(json.dumps(diagnose(x),indent=2))
    else:run(x,args.eps,args.weight,args.maxiter,args.out,args.trust)
```

## constrained_search.py
```python
"""Hull-aware SLSQP with hard positive vertex-escape margins."""
from margin_search import *

class Constrained:
    def __init__(self,x,eps,mode='U',reg=0.,fixed=False):
        self.x0=x.copy();self.eps=eps;self.mode=mode;self.reg=reg;self.fixed=fixed
        self.hu,self.tri=faces(x);self.v0=diagnose(x)['volume'];self.cache=None
        self.root=int(np.argmax(np.sum((x-np.array(diagnose(x)['centroid']))**2,axis=1)))
        with torch.no_grad():
            c,v,u,s,h,a,n=terms(torch.tensor(x),torch.tensor(self.tri))
        self.sroot=int(torch.argmax(s));self.counter=0;self.records=[]
    def calc(self,y):
        if self.cache is not None and np.array_equal(self.cache[0],y):return self.cache[1:]
        self.counter+=1;x=y.reshape(-1,3)
        hu,tr= (self.hu,self.tri) if self.fixed else faces(x)
        t=torch.tensor(x,requires_grad=True)
        c,v,u,s,h,a,n=terms(t,torch.tensor(tr))
        u=u[[i for i in hu.vertices if i!=self.root]]
        # Do not prescribe the stable root when hull changes.
        ps=torch.relu(s+self.eps).square();ps=ps.sum()-ps.max()
        loss=ps+self.reg*((t-torch.tensor(self.x0))**2).sum()
        constraints=[u-self.eps,torch.stack([v/self.v0-.5,2-v/self.v0]),h-.015]
        if self.fixed:
            supp=torch.einsum('ik,jk->ij',n,t-c)-h[:,None]
            # Omit exactly incident vertices, whose constraint is identically zero.
            mask=np.ones((len(tr),len(t)),bool)
            for f,vs in enumerate(tr):mask[f,vs]=False
            constraints.append(-supp[mask])
        cc=torch.cat(constraints)
        grad=torch.autograd.grad(loss,t,retain_graph=True)[0].numpy().ravel()
        jac=torch.autograd.grad(cc,t,grad_outputs=torch.eye(len(cc)),is_grads_batched=True)[0].numpy().reshape(len(cc),-1)
        val=float(loss.detach());cv=cc.detach().numpy()
        self.cache=(y.copy(),val,grad,cv,jac)
        self.records.append([self.counter,val,float(cv.min())])
        return val,grad,cv,jac
    def fun(self,y):v,g,c,j=self.calc(y);return v,g
    def cons(self,y):v,g,c,j=self.calc(y);return c
    def jac(self,y):v,g,c,j=self.calc(y);return j

def solve(x,eps,maxiter,out,reg=0.,fixed=False):
    model=Constrained(x,eps,reg=reg,fixed=fixed);tic=time.time()
    re=minimize(model.fun,x.ravel(),method='SLSQP',jac=True,constraints=[dict(type='ineq',fun=model.cons,jac=model.jac)],options={'maxiter':maxiter,'ftol':1e-12,'disp':False})
    y=re.x.reshape(-1,3);np.save(out+'.npy',y)
    report=dict(eps=eps,reg=reg,fixed=fixed,maxiter=maxiter,objective=float(re.fun),iterations=re.nit,eval=model.counter,message=re.message,seconds=time.time()-tic,start=diagnose(x),end=diagnose(y),records=model.records)
    Path(out+'.json').write_text(json.dumps(report,indent=2)+'\n')
    print(json.dumps({k:v for k,v in report.items() if k not in ['start','end','records']}),flush=True)
    print('END',json.dumps(report['end']),flush=True)
    return y

if __name__=='__main__':
    import argparse
    a=argparse.ArgumentParser();a.add_argument('input');a.add_argument('--eps',type=float,default=1e-5);a.add_argument('--maxiter',type=int,default=100);a.add_argument('--reg',type=float,default=0.);a.add_argument('--fixed',action='store_true');a.add_argument('--out',default='CONSTRAINED');b=a.parse_args()
    if b.input.endswith('.npy'): x=np.load(b.input)
    else:r=json.loads(Path(b.input).read_text());x=np.array(r['points'])/r['denominator']
    solve(x,b.eps,b.maxiter,b.out,b.reg,b.fixed)
```
