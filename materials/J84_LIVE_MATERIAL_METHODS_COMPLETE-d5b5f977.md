# material-d5b5f9774d6e

AI research material · [Export notes](../catalog/coverage.md#text-records)

<!-- historical-status:start -->
> **Historical AI material.** The title and claims below reflect the AI’s assessment at the time. Claims of proof, certification or completion are not a current verification verdict.
>
> [C622](../C622/README.md) passes the supplied exact checks; C<500 remains open; Minimum’s C≥34 remains a working lower bound requiring a consolidated proof. See [verification status and source gaps](../catalog/coverage.md).
<!-- historical-status:end -->

---

# J84 live homogeneous material continuation — complete producing methods

## Dependencies, evidence and exact portability changes
Requires union84.py and N40_V47_INPUT.json plus APEX84_CONTINUATION_SEED.json from [internal-source-reference], and J82_S1_ROBUST_G6_INPUT.json from [internal-source-reference]. union84.inputs reads both inputs even for a B-only continuation. These are fully supplied native source dependencies, not filenames substituted for bytes. The two barconstrained84_{0,1}_SEED.json files needed by the repair stage are preserved in a separate J84_FRAGMENTATION_REPAIR_SEEDS material; it must also be supplied when running repair. No FULL76 or old optimizer is needed.

All four methods rebuild the actual convex hull, filled tetrahedral mass and own centroid on every evaluation. Torch differentiates the current smooth hull/pairing cell; global nonsmooth transitions are not claimed differentiable. Chord witnesses are legitimate sufficient non-U guards and may switch. No floating guard or bar floor is a proof. Triangular nominations near coplanarity require a general exact maximal-facet audit before promotion. In particular, the comments about retaining positive algebraic terms in barconstrained/repair do NOT remove the actual1e-14 relative numerical selection floor visible in their code. Exact endpoints must retain every positive bar without that floor.

These portable sources differ from their executed originals only in the exact literal seed-file access: free/constrained/barconstrained read APEX84_CONTINUATION_SEED.json instead of the full apex84.json; repair reads the standalone barconstrained84_{run}_SEED.json points instead of the identical nested best.points of the full producer report. Point values were checked equal, not recomputed. Consumer output filenames remain unchanged. None of these portability edits changes an objective, parameter, derivative, bound, seed point, stopping criterion or search path.

Environment: CPython3.13.5,NumPy2.3.5,SciPy1.17.0,Torch2.10.0+cpu,torch.float64,one BLAS/OMP/Torch thread. Save all blocks with a final LF in the same directory as dependencies. Commands for the actually run configurations:
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python free84_portable.py --run 0 --iters 900
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python free84_portable.py --run 2 --iters 900
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python constrained84_portable.py --run 0 --iters 300
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python constrained84_portable.py --run 1 --iters 300
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python barconstrained84_portable.py --run 0 --iters 300
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python barconstrained84_portable.py --run 1 --iters 300
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python repair84_portable.py --run 0 --iters 600
The last command was interrupted by a120000ms container timeout; its final marker was NOT observed. Run1 repair was never started. A retry can use a bounded iteration count or the preserved interrupted checkpoint, with that change explicitly recorded.

## Actual scientific results, not solver-score success
Unconstrained witness runs0/2 completed167/177 evaluations and8/13 iterations. Best losses~.001227/.001199 fragmented the actual landscapes to about S11/U33 and S12/U31. Directional derivative checks gave errors2.4787e-8 and1.8786e-9 in the specified regular base cells. Those are local derivative checks, not proofs across hull events. No110.

Hard-U1 constrained witness runs0/1 completed120/190 calls,41/67 iterations. Witness losses~2.033698068e-10/~2.095603496e-10 nevertheless gave numerical S3/U1 and S2/U1, with Q depths~.3947268113/~.3981879242, WORSE than the input's.336746. A nearly zero normalized all-non-root loss did not imply the finite basin had disappeared. Tiny nearly flat carriers and bar-floor/root-count discrepancies are explicit nomination uncertainties, not exact class claims.

Replacing that objective with full numerically resolved polar-bar SUM while retaining hard primal witnesses gave a real numerical total-depth decrease, but fragmentation. Bar-constrained run0 completed653 calls260 iterations,status0,objective.2628133015968197, numericalS31/U1, largestQ.2319485665312303 and29 smaller positive bars. Run1 completed812 calls257 iterations,status0,objective.2618389327799936, numericalS32/U1, largestQ.23008587441559802 and30 smaller positive bars. The two saved best feasible points have slightly different loss values and call indices, recorded literally in their seed files. Neither is exact211 or110. A reduced maximum or total depth is not enough if extra basins are generated.

Repair0 kept a Q-sum budget<=.28, hard-U1 witness margin1e-8 and attempted to leave at most two polar roots. Its interrupted best feasible checkpoint at call290 has numericalS30/U1, loss.005746143082916749, minimum among all constraints -9.149108218554385e-11. The field name min_primal_constraint in this repair checkpoint actually covers BOTH primal witnesses and Q budget. Initial loss was.03083803220369659. No completed600-iteration result and no110. Continue from exact saved numbers rather than inventing the rest of the trajectory.

These finite outcomes are not exclusions of free material deformation, a repair chart, convex gluing, or the fixed root6 family. The constructive next question is to reconsolidate the newly shallow polar basins without giving back the total Q improvement, or to change carriers/policies if the small-loss trap persists. Canonical own110 stays C622; target remains unmet.

## Source hashes
free84_portable.py4620B/SHA4c53564d9611e0469c9ed00a0579bcf7a6d3f3e61a3d0661b932bc27411d02d2
constrained84_portable.py4160B/SHA1bb3f634f57677b0292ae552dc40545f6bc705b664ae9a61eb9c0311bed95e46
barconstrained84_portable.py5287B/SHA59d2813895688125f6cff27fe4b1fe3a1a11f20f0dbae85bfdb807e2715b455c
repair84_portable.py5341B/SHA03a37762b6543c3e2186bec841244aaec12c62a9caaf41de24f633fa5e864439
Completed original markers: J84_FREE_MATERIAL_NOMINATION_DONE, J84_CONSTRAINED_NOMINATION_DONE, J84_BARCONSTRAINED_NOMINATION_DONE for the stated runs. J84_Q_BUDGET_REPAIR_DONE is only a future terminal marker from the source, NOT an observed result. Floating full reports contain elapsed time and no cross-platform byte equality is promised; fixed input and continuation seed hashes are exact.

## free84_portable.py
```python
"""Live convex hull, filled mass and analytic all-nonroot cosine witnesses.
Numerical nomination only: no tolerance is a certification threshold.
"""
import os
os.environ.setdefault('OPENBLAS_NUM_THREADS','1');os.environ.setdefault('OMP_NUM_THREADS','1')
import json,time,argparse
import numpy as np
import torch
from scipy.spatial import ConvexHull
from scipy.optimize import minimize
from union84 import ROOT,inputs,properties

torch.set_num_threads(1);torch.set_default_dtype(torch.float64)
ap=argparse.ArgumentParser();ap.add_argument('--run',type=int,default=0);ap.add_argument('--iters',type=int,default=700);args=ap.parse_args()
A,B,*_=inputs(47)
base=B if args.run<2 else np.vstack([B,json.loads((ROOT/'APEX84_CONTINUATION_SEED.json').read_text())['best']['211']['z']])
rng=np.random.default_rng(841026+args.run);weight=[1.,4.,1.,4.][args.run%4];tau=[1e-5,1e-4,1e-5,1e-4][args.run%4]
x0=base.copy()
if args.run%2:x0+=rng.normal(size=x0.shape)*.002
radius=.6;bounds=[(a-radius,a+radius) for a in base.ravel()];calls=0;best=None;history=[];found=False;t0=time.time()

def calculate(flat,save=True):
    global calls,best,found
    x=flat.reshape((-1,3));calls+=1
    H=ConvexHull(x);tri=H.simplices.copy();normal=np.cross(x[tri[:,1]]-x[tri[:,0]],x[tri[:,2]]-x[tri[:,0]])
    flip=np.einsum('ij,ij->i',normal,H.equations[:,:3])<0
    tri[flip]=tri[flip][:,[0,2,1]]
    p=torch.tensor(x,requires_grad=True);r=p.mean(dim=0);t=p[torch.as_tensor(tri)]
    d=((t[:,0]-r)*torch.linalg.cross(t[:,1]-r,t[:,2]-r)).sum(dim=1)
    V=d.sum()/6;g=(d[:,None]*(t.sum(dim=1)+r)).sum(dim=0)/(4*d.sum())
    n=torch.linalg.cross(t[:,1]-t[:,0],t[:,2]-t[:,0]);h=(n*(t[:,0]-g)).sum(dim=1);q=n/h[:,None]
    def penalty(xx):
        dd=xx[None,:,:]-xx[:,None,:];rr=(xx*xx).sum(dim=1)
        eye=torch.eye(len(xx),dtype=torch.bool)
        norm=torch.sqrt(rr[:,None]*((dd*dd).sum(dim=2)+eye.to(torch.float64)))
        sc=(xx[:,None,:]*dd).sum(dim=2)/norm;sc=sc.masked_fill(eye,-1e4)
        guard=sc.max(dim=1).values;root=int(torch.argmax(rr).detach());mask=torch.ones(len(xx));mask[root]=0
        loss=(torch.relu(tau-guard)**2*mask).sum()
        return loss,guard.detach().numpy()
    pl,pg=penalty(p[torch.as_tensor(H.vertices)]-g);ql,qg=penalty(q)
    loss=weight*pl+ql;loss.backward();val=float(loss.detach())
    if not np.isfinite(val) or not np.isfinite(p.grad.detach().numpy()).all():raise ValueError('nonfinite objective')
    if save and (best is None or val<best['loss']):
        best={'loss':val,'lossP':float(pl.detach()),'lossQ':float(ql.detach()),'S':int(np.sum(qg<0)),'U':int(np.sum(pg<0)),
              'V':len(H.vertices),'F_triangles':len(tri),'material_rows':len(x),'volume':float(V.detach()),'centroid':g.detach().numpy().tolist(),
              'min_nonroot_P':float(np.partition(pg,1)[1]),'min_nonroot_Q':float(np.partition(qg,1)[1]),'points':x.tolist(),'calls':calls}
        history.append({k:v for k,v in best.items() if k!='points'})
        if len(history)%50==0:print('BEST',calls,val,best['S'],best['U'],time.time()-t0,flush=True)
        (ROOT/f'free84_{args.run}_best.json').write_text(json.dumps(best,indent=2)+'\n')
    if np.sum(pg<0)==np.sum(qg<0)==1:
        found=True;(ROOT/f'FREE84_{args.run}_110_NOMINATION.json').write_text(json.dumps(best,indent=2)+'\n')
    return val,p.grad.detach().numpy().ravel()

# One regular derivative control for this complete objective.
f0,jac=calculate(x0.ravel(),False);direction=rng.normal(size=x0.size);direction/=np.linalg.norm(direction);eps=1e-7
fd=(calculate(x0.ravel()+eps*direction,False)[0]-calculate(x0.ravel()-eps*direction,False)[0])/(2*eps)
print('DERIVATIVE',fd,float(jac@direction),'REL',abs(fd-jac@direction)/max(1.,abs(fd)),flush=True)
res=minimize(calculate,x0.ravel(),jac=True,method='L-BFGS-B',bounds=bounds,
             options={'maxiter':args.iters,'maxfun':20000,'ftol':1e-16,'gtol':1e-11,'maxls':40,'maxcor':30})
last=properties(res.x.reshape((-1,3)))
out={'run':args.run,'weight':weight,'tau':tau,'bounds_radius':radius,'seed':841026+args.run,'maxiter':args.iters,'calls':calls,'best':best,'history':history,
     'solver':{'status':int(res.status),'message':str(res.message),'nit':int(res.nit),'fun':float(res.fun)},'last':last,'found110':found,'elapsed':time.time()-t0,
     'derivative_check':{'fd':float(fd),'analytic':float(jac@direction),'absolute_error':float(abs(fd-jac@direction))}}
(ROOT/f'free84_{args.run}.json').write_text(json.dumps(out,indent=2)+'\n')
print('J84_FREE_MATERIAL_NOMINATION_DONE',args.run,calls,res.status,res.nit,float(res.fun),best['S'],best['U'],last['P'],last['Q'],found,time.time()-t0,flush=True)
```

## constrained84_portable.py
```python
"""Fixed unique-U carrier, live mass, disjunctive global witnesses, finite S search.
All material rows may move; only a retained primal root is prescribed.
Numerical nomination, not a family exclusion or a rigorous feasibility oracle.
"""
import os
os.environ.setdefault('OPENBLAS_NUM_THREADS','1');os.environ.setdefault('OMP_NUM_THREADS','1')
import json,time,argparse
import numpy as np
import torch
from scipy.spatial import ConvexHull
from scipy.optimize import minimize
from union84 import ROOT,inputs,properties

torch.set_num_threads(1);torch.set_default_dtype(torch.float64)
ap=argparse.ArgumentParser();ap.add_argument('--run',type=int,default=0);ap.add_argument('--iters',type=int,default=300);args=ap.parse_args()
A,B,*_=inputs(47);base=B if args.run==0 else np.vstack([B,json.loads((ROOT/'APEX84_CONTINUATION_SEED.json').read_text())['best']['211']['z']])
N=len(base);root=6;idx=np.array([i for i in range(N) if i!=root]);margin=1e-8;tau=1e-5;rad=.6;calls=0;cache={};best=None;records=[];found=False;t0=time.time()

def calc(flat):
    global cache,calls,best,found
    if 'x' in cache and np.array_equal(cache['x'],flat):return cache
    calls+=1;x=flat.reshape((-1,3));H=ConvexHull(x);tri=H.simplices.copy()
    nn=np.cross(x[tri[:,1]]-x[tri[:,0]],x[tri[:,2]]-x[tri[:,0]]);flip=np.einsum('ij,ij->i',nn,H.equations[:,:3])<0;tri[flip]=tri[flip][:,[0,2,1]]
    p=torch.tensor(x,requires_grad=True);r=p.mean(dim=0);t=p[torch.as_tensor(tri)]
    d=((t[:,0]-r)*torch.linalg.cross(t[:,1]-r,t[:,2]-r)).sum(dim=1);g=(d[:,None]*(t.sum(dim=1)+r)).sum(dim=0)/(4*d.sum())
    n=torch.linalg.cross(t[:,1]-t[:,0],t[:,2]-t[:,0]);h=(n*(t[:,0]-g)).sum(dim=1);q=n/h[:,None]
    def guard(xx):
        dd=xx[None,:,:]-xx[:,None,:];rr=(xx*xx).sum(dim=1);eye=torch.eye(len(xx),dtype=torch.bool)
        norm=torch.sqrt(rr[:,None]*((dd*dd).sum(dim=2)+eye.to(torch.float64)));sc=(xx[:,None,:]*dd).sum(dim=2)/norm
        return sc.masked_fill(eye,-1e4).max(dim=1).values,rr
    pg,_=guard(p-g);qg,qr=guard(q);mask=torch.ones(len(q));mask[int(torch.argmax(qr).detach())]=0
    loss=(torch.relu(tau-qg)**2*mask).sum();cons=pg[torch.as_tensor(idx)]-margin
    jac=torch.autograd.grad(loss,p,retain_graph=True)[0].detach().numpy().ravel()
    J=torch.autograd.grad(cons,p,grad_outputs=torch.eye(len(cons)),is_grads_batched=True)[0].detach().numpy().reshape((len(cons),-1))
    val=float(loss.detach());co=cons.detach().numpy();cp=pg.detach().numpy();cq=qg.detach().numpy()
    if min(co)>=-1e-10 and (best is None or val<best['loss']):
        best={'loss':val,'min_primal_constraint':float(min(co)),'S':int(np.sum(cq<0)),'U':int(np.sum(cp<0)),'points':x.tolist(),'calls':calls}
        records.append({k:v for k,v in best.items() if k!='points'});(ROOT/f'constrained84_{args.run}_best.json').write_text(json.dumps(best,indent=2)+'\n')
    if np.sum(cp<0)==np.sum(cq<0)==1:
        found=True;(ROOT/f'CONSTRAINED84_{args.run}_110_NOMINATION.json').write_text(json.dumps({'points':x.tolist(),'min_constraint':float(min(co))},indent=2)+'\n')
    cache={'x':np.array(flat),'value':val,'jac':jac,'cons':co,'J':J};return cache

b=calc(base.ravel());print('BASE',b['value'],float(min(b['cons'])),flush=True)
res=minimize(lambda x:calc(x)['value'],base.ravel(),jac=lambda x:calc(x)['jac'],method='SLSQP',
    bounds=[(v-rad,v+rad) for v in base.ravel()],constraints={'type':'ineq','fun':lambda x:calc(x)['cons'],'jac':lambda x:calc(x)['J']},
    options={'maxiter':args.iters,'ftol':1e-13})
last=properties(res.x.reshape((-1,3)));b=calc(res.x)
out={'run':args.run,'fixed_root':root,'margin':margin,'tau':tau,'bounds_radius':rad,'calls':calls,'best':best,'records':records,'found':found,
     'solver':{'status':int(res.status),'nit':int(res.nit),'fun':float(res.fun),'message':str(res.message)},'last':last,'last_points':res.x.reshape((-1,3)).tolist(),'last_min_constraint':float(min(b['cons'])),'elapsed':time.time()-t0}
(ROOT/f'constrained84_{args.run}.json').write_text(json.dumps(out,indent=2)+'\n')
print('J84_CONSTRAINED_NOMINATION_DONE',args.run,calls,res.status,res.nit,res.fun,float(min(b['cons'])),last['S'],last['U'],last['P'],last['Q'],found,time.time()-t0,flush=True)
```

## barconstrained84_portable.py
```python
"""Full positive polar persistence, fixed unique-U carrier, live homogeneous mass.
All material rows may move; only a retained primal root is prescribed.
Numerical nomination, not a family exclusion or a rigorous feasibility oracle.
"""
import os
os.environ.setdefault('OPENBLAS_NUM_THREADS','1');os.environ.setdefault('OMP_NUM_THREADS','1')
import json,time,argparse
import numpy as np
import torch
from scipy.spatial import ConvexHull
from scipy.optimize import minimize
from union84 import ROOT,inputs,properties

torch.set_num_threads(1);torch.set_default_dtype(torch.float64)
ap=argparse.ArgumentParser();ap.add_argument('--run',type=int,default=0);ap.add_argument('--iters',type=int,default=300);args=ap.parse_args()
A,B,*_=inputs(47);base=B if args.run==0 else np.vstack([B,json.loads((ROOT/'APEX84_CONTINUATION_SEED.json').read_text())['best']['211']['z']])
N=len(base);root=6;idx=np.array([i for i in range(N) if i!=root]);margin=1e-8;tau=1e-5;rad=.6;calls=0;cache={};best=None;records=[];found=False;t0=time.time()

def calc(flat):
    global cache,calls,best,found
    if 'x' in cache and np.array_equal(cache['x'],flat):return cache
    calls+=1;x=flat.reshape((-1,3));H=ConvexHull(x);tri=H.simplices.copy()
    nn=np.cross(x[tri[:,1]]-x[tri[:,0]],x[tri[:,2]]-x[tri[:,0]]);flip=np.einsum('ij,ij->i',nn,H.equations[:,:3])<0;tri[flip]=tri[flip][:,[0,2,1]]
    p=torch.tensor(x,requires_grad=True);r=p.mean(dim=0);t=p[torch.as_tensor(tri)]
    d=((t[:,0]-r)*torch.linalg.cross(t[:,1]-r,t[:,2]-r)).sum(dim=1);g=(d[:,None]*(t.sum(dim=1)+r)).sum(dim=0)/(4*d.sum())
    n=torch.linalg.cross(t[:,1]-t[:,0],t[:,2]-t[:,0]);h=(n*(t[:,0]-g)).sum(dim=1);q=n/h[:,None]
    def guard(xx):
        dd=xx[None,:,:]-xx[:,None,:];rr=(xx*xx).sum(dim=1);eye=torch.eye(len(xx),dtype=torch.bool)
        norm=torch.sqrt(rr[:,None]*((dd*dd).sum(dim=2)+eye.to(torch.float64)));sc=(xx[:,None,:]*dd).sum(dim=2)/norm
        return sc.masked_fill(eye,-1e4).max(dim=1).values,rr
    pg,_=guard(p-g);qg,qr=guard(q);mask=torch.ones(len(q));mask[int(torch.argmax(qr).detach())]=0
    # Use the full dual graph, not the last root's local cosine alone.
    owners={}
    for fi,tt in enumerate(tri):
        for i,j in [(tt[0],tt[1]),(tt[1],tt[2]),(tt[2],tt[0])]:owners.setdefault(tuple(sorted((int(i),int(j)))),[]).append(fi)
    ee=np.array(list(owners.values()),int);assert ee.shape[1]==2
    qa=q[torch.as_tensor(ee[:,0])];dd=q[torch.as_tensor(ee[:,1])]-qa
    timeedge=torch.clamp(-(qa*dd).sum(dim=1)/(dd*dd).sum(dim=1),0,1)
    at=qa+timeedge[:,None]*dd;level=(at*at).sum(dim=1)
    l=level.detach().numpy();birth=qr.detach().numpy();parent=list(range(len(q)));terms=[]
    def find(i):
        while parent[i]!=i:parent[i]=parent[parent[i]];i=parent[i]
        return i
    for e in np.argsort(-l,kind='stable'):
        i,j=find(ee[e,0]),find(ee[e,1])
        if i==j:continue
        if (birth[i],-i)<(birth[j],-j):i,j=j,i
        # Numerical negative roundoff is excluded; all positive algebraic terms are retained.
        if birth[j]>l[e]+1e-14*birth[j]:terms.append(1-level[e]/qr[j])
        parent[j]=i
    persistence=torch.stack(terms).sum() if terms else 0*q.sum()
    loss=persistence+1e-3*(torch.relu(tau-qg)**2*mask).sum();cons=pg[torch.as_tensor(idx)]-margin
    jac=torch.autograd.grad(loss,p,retain_graph=True)[0].detach().numpy().ravel()
    J=torch.autograd.grad(cons,p,grad_outputs=torch.eye(len(cons)),is_grads_batched=True)[0].detach().numpy().reshape((len(cons),-1))
    val=float(loss.detach());co=cons.detach().numpy();cp=pg.detach().numpy();cq=qg.detach().numpy()
    if min(co)>=-1e-10 and (best is None or val<best['loss']):
        best={'loss':val,'min_primal_constraint':float(min(co)),'S':int(np.sum(cq<0)),'U':int(np.sum(cp<0)),'points':x.tolist(),'calls':calls}
        records.append({k:v for k,v in best.items() if k!='points'});(ROOT/f'barconstrained84_{args.run}_best.json').write_text(json.dumps(best,indent=2)+'\n')
    if np.sum(cp<0)==np.sum(cq<0)==1:
        found=True;(ROOT/f'BARCONSTRAINED84_{args.run}_110_NOMINATION.json').write_text(json.dumps({'points':x.tolist(),'min_constraint':float(min(co))},indent=2)+'\n')
    cache={'x':np.array(flat),'value':val,'jac':jac,'cons':co,'J':J};return cache

b=calc(base.ravel());print('BASE',b['value'],float(min(b['cons'])),flush=True)
res=minimize(lambda x:calc(x)['value'],base.ravel(),jac=lambda x:calc(x)['jac'],method='SLSQP',
    bounds=[(v-rad,v+rad) for v in base.ravel()],constraints={'type':'ineq','fun':lambda x:calc(x)['cons'],'jac':lambda x:calc(x)['J']},
    options={'maxiter':args.iters,'ftol':1e-13})
last=properties(res.x.reshape((-1,3)));b=calc(res.x)
out={'run':args.run,'fixed_root':root,'margin':margin,'tau':tau,'bounds_radius':rad,'calls':calls,'best':best,'records':records,'found':found,
     'solver':{'status':int(res.status),'nit':int(res.nit),'fun':float(res.fun),'message':str(res.message)},'last':last,'last_points':res.x.reshape((-1,3)).tolist(),'last_min_constraint':float(min(b['cons'])),'elapsed':time.time()-t0}
(ROOT/f'barconstrained84_{args.run}.json').write_text(json.dumps(out,indent=2)+'\n')
print('J84_BARCONSTRAINED_NOMINATION_DONE',args.run,calls,res.status,res.nit,res.fun,float(min(b['cons'])),last['S'],last['U'],last['P'],last['Q'],found,time.time()-t0,flush=True)
```

## repair84_portable.py
```python
"""Repair extra polar roots while retaining U1 and a finite Q-depth budget.
All material rows may move; only a retained primal root is prescribed.
Numerical nomination, not a family exclusion or a rigorous feasibility oracle.
"""
import os
os.environ.setdefault('OPENBLAS_NUM_THREADS','1');os.environ.setdefault('OMP_NUM_THREADS','1')
import json,time,argparse
import numpy as np
import torch
from scipy.spatial import ConvexHull
from scipy.optimize import minimize
from union84 import ROOT,inputs,properties

torch.set_num_threads(1);torch.set_default_dtype(torch.float64)
ap=argparse.ArgumentParser();ap.add_argument('--run',type=int,default=0);ap.add_argument('--iters',type=int,default=300);args=ap.parse_args()
base=np.array(json.loads((ROOT/f'barconstrained84_{args.run}_SEED.json').read_text())['points'])
N=len(base);root=6;idx=np.array([i for i in range(N) if i!=root]);margin=1e-8;tau=1e-5;rad=.25;calls=0;cache={};best=None;records=[];found=False;t0=time.time()

def calc(flat):
    global cache,calls,best,found
    if 'x' in cache and np.array_equal(cache['x'],flat):return cache
    calls+=1;x=flat.reshape((-1,3));H=ConvexHull(x);tri=H.simplices.copy()
    nn=np.cross(x[tri[:,1]]-x[tri[:,0]],x[tri[:,2]]-x[tri[:,0]]);flip=np.einsum('ij,ij->i',nn,H.equations[:,:3])<0;tri[flip]=tri[flip][:,[0,2,1]]
    p=torch.tensor(x,requires_grad=True);r=p.mean(dim=0);t=p[torch.as_tensor(tri)]
    d=((t[:,0]-r)*torch.linalg.cross(t[:,1]-r,t[:,2]-r)).sum(dim=1);g=(d[:,None]*(t.sum(dim=1)+r)).sum(dim=0)/(4*d.sum())
    n=torch.linalg.cross(t[:,1]-t[:,0],t[:,2]-t[:,0]);h=(n*(t[:,0]-g)).sum(dim=1);q=n/h[:,None]
    def guard(xx):
        dd=xx[None,:,:]-xx[:,None,:];rr=(xx*xx).sum(dim=1);eye=torch.eye(len(xx),dtype=torch.bool)
        norm=torch.sqrt(rr[:,None]*((dd*dd).sum(dim=2)+eye.to(torch.float64)));sc=(xx[:,None,:]*dd).sum(dim=2)/norm
        return sc.masked_fill(eye,-1e4).max(dim=1).values,rr
    pg,_=guard(p-g);qg,qr=guard(q);mask=torch.ones(len(q));mask[int(torch.argmax(qr).detach())]=0
    # Use the full dual graph, not the last root's local cosine alone.
    owners={}
    for fi,tt in enumerate(tri):
        for i,j in [(tt[0],tt[1]),(tt[1],tt[2]),(tt[2],tt[0])]:owners.setdefault(tuple(sorted((int(i),int(j)))),[]).append(fi)
    ee=np.array(list(owners.values()),int);assert ee.shape[1]==2
    qa=q[torch.as_tensor(ee[:,0])];dd=q[torch.as_tensor(ee[:,1])]-qa
    timeedge=torch.clamp(-(qa*dd).sum(dim=1)/(dd*dd).sum(dim=1),0,1)
    at=qa+timeedge[:,None]*dd;level=(at*at).sum(dim=1)
    l=level.detach().numpy();birth=qr.detach().numpy();parent=list(range(len(q)));terms=[];peak_depth=[]
    def find(i):
        while parent[i]!=i:parent[i]=parent[parent[i]];i=parent[i]
        return i
    for e in np.argsort(-l,kind='stable'):
        i,j=find(ee[e,0]),find(ee[e,1])
        if i==j:continue
        if (birth[i],-i)<(birth[j],-j):i,j=j,i
        # Numerical negative roundoff is excluded; all positive algebraic terms are retained.
        if birth[j]>l[e]+1e-14*birth[j]:
            terms.append(1-level[e]/qr[j]);peak_depth.append((1-l[e]/birth[j],j))
        parent[j]=i
    persistence=torch.stack(terms).sum() if terms else 0*q.sum()
    if peak_depth:mask[max(peak_depth)[1]]=0
    loss=(torch.relu(tau-qg)**2*mask).sum()
    cons=torch.cat([pg[torch.as_tensor(idx)]-margin,(.28-persistence).reshape(1)])
    jac=torch.autograd.grad(loss,p,retain_graph=True)[0].detach().numpy().ravel()
    J=torch.autograd.grad(cons,p,grad_outputs=torch.eye(len(cons)),is_grads_batched=True)[0].detach().numpy().reshape((len(cons),-1))
    val=float(loss.detach());co=cons.detach().numpy();cp=pg.detach().numpy();cq=qg.detach().numpy()
    if min(co)>=-1e-10 and (best is None or val<best['loss']):
        best={'loss':val,'min_primal_constraint':float(min(co)),'S':int(np.sum(cq<0)),'U':int(np.sum(cp<0)),'points':x.tolist(),'calls':calls}
        records.append({k:v for k,v in best.items() if k!='points'});(ROOT/f'repair84_{args.run}_best.json').write_text(json.dumps(best,indent=2)+'\n')
    if np.sum(cp<0)==np.sum(cq<0)==1:
        found=True;(ROOT/f'REPAIR84_{args.run}_110_NOMINATION.json').write_text(json.dumps({'points':x.tolist(),'min_constraint':float(min(co))},indent=2)+'\n')
    cache={'x':np.array(flat),'value':val,'jac':jac,'cons':co,'J':J};return cache

b=calc(base.ravel());print('BASE',b['value'],float(min(b['cons'])),flush=True)
res=minimize(lambda x:calc(x)['value'],base.ravel(),jac=lambda x:calc(x)['jac'],method='SLSQP',
    bounds=[(v-rad,v+rad) for v in base.ravel()],constraints={'type':'ineq','fun':lambda x:calc(x)['cons'],'jac':lambda x:calc(x)['J']},
    options={'maxiter':args.iters,'ftol':1e-15})
last=properties(res.x.reshape((-1,3)));b=calc(res.x)
out={'run':args.run,'fixed_root':root,'margin':margin,'tau':tau,'bounds_radius':rad,'calls':calls,'best':best,'records':records,'found':found,
     'solver':{'status':int(res.status),'nit':int(res.nit),'fun':float(res.fun),'message':str(res.message)},'last':last,'last_points':res.x.reshape((-1,3)).tolist(),'last_min_constraint':float(min(b['cons'])),'elapsed':time.time()-t0}
(ROOT/f'repair84_{args.run}.json').write_text(json.dumps(out,indent=2)+'\n')
print('J84_Q_BUDGET_REPAIR_DONE',args.run,calls,res.status,res.nit,res.fun,float(min(b['cons'])),last['S'],last['U'],last['P'],last['Q'],found,time.time()-t0,flush=True)
```
