# material-352fdec179ed

AI research material · [Export notes](../catalog/coverage.md#text-records)

---

# J92 complete finite optimization producers and their negative evidence

Dependencies: every complete source in J92_NUMERICAL_METHODS_CORE.md, [internal-source-reference], plus the C390 input from complete [internal-source-reference]. First run nominate92.py and detour92.py as specified there. Exact controls are [internal-source-reference]; this material does not promote the floating endpoints to exact bodies.

Environment Python3.13.5, NumPy2.3.5, SciPy1.17.0, Torch2.10.0+cpu; OPENBLAS_NUM_THREADS=1, OMP_NUM_THREADS=1, Torch float64 and one thread. No random source. All nondefault solver tolerances, bounds, regularizers, reference points, root and parent-selection policies are literal below. Commands:
`OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python detourwide92.py`
`OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python offset92.py DETOUR_N10_B0p0 both`
`OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python bridge_repair92.py DETOUR_N10_B0p06`

## Findings, not exclusions
- The latitude family sampled n in{10,11,12,14,16,18} and bump.06 through.30 by.005; only strictly positive-chain samples were retained. All retained nominations stayed referenceS1/U2. Carrier turnover occurred but did not cancel the last physical basin. The finite grid is not a theorem about all angular bridges.
- Offset repair allows every nonroot physical offset to vary in[.05,8], fixes root15's offset1 as the scale gauge, and maintains a chosen global polar-positive forest by linear inequalities. For N_i.x<=h_i, the arrow i->j is precisely (N_i.N_j)h_i-|N_i|^2 h_j>0. The code uses the maximum normalized chord parent at the initial detour. Its400-iteration SLSQP endpoint has positive selected witnesses, referenceS1/U17, actualS39/U18, numerical V114/E171/F59, and a remaining centroid displacement approximately(.0729921215231,.00553520584131,.0384596676675). Loss~.00683763437192 includes its stated tiny deformation regularizer. Iteration limit, not convergence or a global infeasibility certificate. The positive forest is a search chart, not the whole offset family.
- The27-variable bridge-only repair retains the old physical U with q.u<=.9999 and retains the polar-positive chain. Starting .06-bump DETOUR_N10 it reaches numerical V148/E222/F76, referenceS1/U2, actualS35/U17. Cost~1.0000029884893941e-10 after33 iterations is NOT cancellation: one reference nonroot outgoing guard approaches zero and the physical basin remains. The source checks the full rebuilt vertex set, but its surrogate is still local outgoing-chord depth, not the whole P persistence. Do not discard that positive basin or call the endpoint110.

## detourwide92.py
```python
"""Wider finite angular detours: find a reference110 corridor, not own110.
Deterministic radial/geographic family. No thresholded positive bars are erased.
"""
import json
from pathlib import Path
import numpy as np
from geom92 import *
D=Path(__file__).parent;d=np.load(D/'BRIDGE_N9.npz');Y=d['Ybase'];g=d['gref'];X,*_=hbody(Y)
u=X[roots(X-g)[0][0]]-g;e=u/np.linalg.norm(u);Q=Y/(1-Y@g)[:,None];a,b=Q[65],Q[15];r0,r1=np.linalg.norm(a),np.linalg.norm(b)
th=np.arccos([a@e/r0,b@e/r1]);p=a/r0-e*(a@e/r0);p/=np.linalg.norm(p);v=b/r1-e*(b@e/r1);v/=np.linalg.norm(v);az=np.arccos(p@v);w=v-p*(p@v);w/=np.linalg.norm(w)
records=[]
for n in [10,11,12,14,16,18]:
 for bump in np.arange(0.06,.301,.005):
  t=np.arange(1,n)/n;theta=(1-t)*th[0]+t*th[1]+bump*np.sin(np.pi*t);r=r0*(r1/r0)**t
  C=r[:,None]*(np.cos(theta)[:,None]*e+np.sin(theta)[:,None]*(np.cos(az*t)[:,None]*p+np.sin(az*t)[:,None]*w))
  chain=np.vstack([a,C,b]);margin=np.einsum('ij,ij->i',chain[:-1],np.diff(chain,axis=0)).min()
  if margin<=0:continue
  QQ=np.vstack([Q,C]);YY=QQ/(1+QQ@g)[:,None];rr=report(YY,g);rr.update(n=n,bump=float(bump),chain_margin=float(margin));records.append(rr)
  if rr['reference_float']==[1,1]:
   name='REFERENCE110_N%d_B%03d'%(n,round(bump*1000));np.savez(D/(name+'.npz'),Y=YY,gref=g);print(name,'E',rr['E'],'own',rr['strict_float'],'g',rr['drift'],flush=True)
  elif abs(bump/.05-round(bump/.05))<1e-8:print('control',n,bump,rr['reference_float'],rr['E'],flush=True)
(D/'DETOUR_WIDE.json').write_text(json.dumps(records,indent=2)+'\n')
```

## offset92.py
```python
"""Finite offset centroid repair within a strict one-polar-root witness cone.
Fixed normal directions N; physical inequalities N_i.x<=h_i in reference frame.
Every chosen positive polar chord is LINEAR: (N_i.N_j)/|N_i|^2*h_i-h_j>0.
Mass/hull rebuilt at every evaluation. This is a numerical producer, not a proof.
"""
import json,sys
from pathlib import Path
import numpy as np
import torch
from scipy.spatial import ConvexHull
from scipy.optimize import minimize,LinearConstraint,Bounds
from geom92 import hbody,roots,report
D=Path(__file__).parent;torch.set_num_threads(1);torch.set_default_dtype(torch.float64)

def mass_jac(N,h):
 Y=N/h[:,None]
 qh=ConvexHull(Y);ids=qh.simplices.copy()
 X=np.linalg.solve(N[ids],h[ids,None])[:,:,0]
 ph=ConvexHull(X);ts=ph.simplices.copy()
 s=np.einsum('ij,ij->i',np.cross(X[ts[:,1]]-X[ts[:,0]],X[ts[:,2]]-X[ts[:,0]]),ph.equations[:,:3])
 ii=s<0;ts[ii,1],ts[ii,2]=ts[ii,2].copy(),ts[ii,1].copy()
 ht=torch.tensor(h,requires_grad=True);A=torch.tensor(np.linalg.inv(N[ids]));xt=(A@ht[ids][...,None])[:,:,0]
 a,b,c=xt[ts[:,0]],xt[ts[:,1]],xt[ts[:,2]]
 w=torch.sum(a*torch.linalg.cross(b,c),dim=1)/6
 V=w.sum();M=(w[:,None]*(a+b+c)/4).sum(0);g=M/V
 outs=torch.cat((g,V[None]))
 jac=np.stack([torch.autograd.grad(outs[k],ht,retain_graph=k<3)[0].detach().numpy() for k in range(4)])
 return outs.detach().numpy(),jac

if __name__=='__main__':
 name=sys.argv[1] if len(sys.argv)>1 else 'DETOUR_N10_B0p0';mode=sys.argv[2] if len(sys.argv)>2 else 'both'
 raw=np.load(D/(name+'.npz'));gref=raw['gref'];N=raw['Y']/(1-raw['Y']@gref)[:,None]
 m=len(N);ratio=(N@N.T)/(N*N).sum(1)[:,None];np.fill_diagonal(ratio,-np.inf);parent=np.argmax(ratio,1);root=15
 assert all(ratio[i,parent[i]]>1 for i in range(m) if i!=root)
 inds=[i for i in range(m) if i!=root];A=np.zeros((len(inds),m))
 for k,i in enumerate(inds):A[k,i]=ratio[i,parent[i]];A[k,parent[i]]-=1
 eps=np.minimum(1e-8,(A@np.ones(m))*.05)
 free=np.array(inds);fixed=np.zeros(m);fixed[root]=1
 low=np.full(len(free),.05 if mode=='both' else 1.);high=np.full(len(free),8.)
 cache={}
 def val(z):
  if cache.get('z') is None or not np.array_equal(cache['z'],z):
   h=fixed.copy();h[free]=z;v,j=mass_jac(N,h);cache.update(z=z.copy(),v=v,j=j,h=h)
  return cache['v'],cache['j'][:,free]
 def fun(z):
  v,j=val(z);cost=v[:3]@v[:3]+1e-10*np.sum((z-1)**2)
  grad=2*v[:3]@j[:3]+2e-10*(z-1)
  return cost,grad
 con=LinearConstraint(A[:,free],eps-A@fixed,np.inf)
 count=[0]
 def cb(z):
  count[0]+=1
  if count[0]%20==0:
   v,j=val(z);print('ITER',count[0],'g',v[:3],'volume',v[3],'loss',v[:3]@v[:3],flush=True)
 res=minimize(fun,np.ones(len(free)),jac=True,bounds=Bounds(low,high),constraints=[con],method='SLSQP',callback=cb,options={'maxiter':400,'ftol':1e-16,'disp':True})
 h=fixed.copy();h[free]=res.x;Q=N/h[:,None];Y=Q/(1+Q@gref)[:,None];r=report(Y,gref)
 r.update(name=name+'_OFF_'+mode,success=bool(res.success),message=str(res.message),fun=float(res.fun),min_witness=float(min(A@h)),h=h.tolist(),parent=parent.tolist(),initial=name,mode=mode)
 np.savez(D/(r['name']+'.npz'),Y=Y,gref=gref,h=h,N=N)
 (D/(r['name']+'.json')).write_text(json.dumps(r,indent=2)+'\n');print(json.dumps(r),flush=True)
```

## bridge_repair92.py
```python
"""Reference one-polar-root bridge shape repair with true H-hull rebuilding.
Keep the old physical U by strict halfspace inequalities, preserve polar S1 via
positive bridge chords, and optimize ALL non-U outgoing physical chord guards.
Numerical only, with distinct source/result labels for each attempted endpoint.
"""
import json,sys
from pathlib import Path
import numpy as np,torch
from scipy.spatial import ConvexHull
from scipy.optimize import minimize,Bounds
from geom92 import hbody,report,roots
D=Path(__file__).parent;torch.set_default_dtype(torch.float64);torch.set_num_threads(1)
name=sys.argv[1] if len(sys.argv)>1 else 'DETOUR_N10_B0p06';raw=np.load(D/(name+'.npz'));Y=raw['Y'];g=raw['gref'];Q=Y/(1-Y@g)[:,None];fixed=Q[:70].copy();C0=Q[70:].copy();k=len(C0)
X,*_=hbody(fixed);u=X[roots(X)[0][0]];fixed_t=torch.tensor(fixed);ut=torch.tensor(u)
last={};count=[0]
def evaluate(z):
 if last.get('z') is not None and np.array_equal(last['z'],z):return last
 C=z.reshape(k,3);qn=np.vstack([fixed,C]);qh=ConvexHull(qn);ids=qh.simplices.copy()
 ct=torch.tensor(C,requires_grad=True);qt=torch.cat([fixed_t,ct],dim=0);pt=torch.linalg.solve(qt[ids],torch.ones((len(ids),3,1)))[:,:,0]
 # Original fixed U remains present by the polar halfspace constraints.
 dist=torch.sum((pt-ut)**2,dim=1).detach().numpy();root=int(np.argmin(dist));assert dist[root]<1e-12
 r2=(pt*pt).sum(1);scores=(pt@pt.T)/r2[:,None]-1
 scores=scores-torch.eye(len(pt))*1e3
 best=scores.max(1).values;keep=np.arange(len(pt))!=root;new=np.any(ids>=70,axis=1)
 tau=torch.tensor(np.where(new,1e-5,1e-11));bad=torch.relu(tau[keep]-best[keep]);cost=(bad**2).sum()+1e-11*((ct-torch.tensor(C0))**2).sum()
 grad=torch.autograd.grad(cost,ct,retain_graph=True)[0].detach().numpy().ravel()
 chain=torch.cat([fixed_t[65:66],ct,fixed_t[15:16]],dim=0);r=torch.sum(chain[:-1]**2,dim=1)
 guards=torch.sum(chain[:-1]*(chain[1:]-chain[:-1]),dim=1)/r-1e-5
 ugap=1-ct@ut-1e-4;cons=torch.cat([guards,ugap])
 jac=np.stack([torch.autograd.grad(cons[i],ct,retain_graph=i<len(cons)-1)[0].detach().numpy().ravel() for i in range(len(cons))])
 last.update(z=z.copy(),cost=float(cost.detach()),grad=grad,cons=cons.detach().numpy(),jac=jac,best=best.detach().numpy(),root=root,new=new)
 return last

def fun(z):a=evaluate(z);return a['cost'],a['grad']
def con(z):return evaluate(z)['cons']
def cj(z):return evaluate(z)['jac']
def cb(z):
 count[0]+=1
 if count[0]%20==0:
  r=evaluate(z);b=r['best'].copy();b[r['root']]=np.inf;print('ITER',count[0],'loss',r['cost'],'min',min(b),'nonpositive',sum(b<=0),'mincon',min(r['cons']),flush=True)
res=minimize(fun,C0.ravel(),jac=True,method='SLSQP',bounds=Bounds((C0-.6).ravel(),(C0+.6).ravel()),constraints=[{'type':'ineq','fun':con,'jac':cj}],callback=cb,options={'maxiter':350,'ftol':1e-19,'disp':True})
C=res.x.reshape(k,3);qn=np.vstack([fixed,C]);YY=qn/(1+qn@g)[:,None];r=report(YY,g);r.update(name=name+'_REPAIRED',success=bool(res.success),message=str(res.message),loss=float(res.fun),min_constraint=float(min(con(res.x))))
np.savez(D/(r['name']+'.npz'),Y=YY,gref=g,polarchain=np.vstack([fixed[65],C,fixed[15]]));(D/(r['name']+'.json')).write_text(json.dumps(r,indent=2)+'\n');print(json.dumps(r),flush=True)
```
