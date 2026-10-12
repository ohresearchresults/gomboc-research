# material-692dc36c8003

AI research material · [Export notes](../catalog/coverage.md#text-records)

<!-- historical-status:start -->
> **Historical AI material.** The title and claims below reflect the AI’s assessment at the time. Claims of proof, certification or completion are not a current verification verdict.
>
> [C622](../C622/README.md) passes the supplied exact checks; C<500 remains open; Minimum’s C≥34 remains a working lower bound requiring a consolidated proof. See [verification status and source gaps](../catalog/coverage.md).
<!-- historical-status:end -->

---

# J76 complete low-degree material-warp nomination methods

Dependencies: exact source [internal-source-reference] as J75_REFERENCE110_CAP233.py; CPython3.13.5, NumPy2.3.5, SciPy1.17.0, torch2.10.0+cpu, one CPU thread and float64. The separate J76 metric nomination uses Shapely2.1.2, now actually checked in the executed environment.

Save the two complete units below with one terminating LF. warp76.py5596B SHAae7b681f2489af69340175f319bef92521267e61e04b0bca1c87195dbcf24958; plane76.py3402B SHA7dd1c0182f93721157cf71225c3dc43c03225a36213875a0fca5ad327dc37289.

Executed commands, all starts completed:
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python warp76.py 2 12
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python plane76.py 16
The deterministic seeds are760126 and760226. All bounds, solver options, volume guard and explicit numerical merge/bar thresholds are in the units. The first uses18 quadratic parameters after removing point-sample affine components. The second uses15 parameters retaining the parent plane:12 tangential quadratic components plus3 normal height-times-linear components. The point-sample affine projection is a gauge choice, not an integration claim. Every evaluation reconstructs its current floating convex hull and actual filled homogeneous centroid.

Observed first selection warp76_d2_08/best.json has value .09575136159510256; selected cap-plane run plane76_09/best.json has value .561740373380519. Raw optimizer output can vary with numerical platform; the exact controls DO NOT require rerunning optimization. Complete literal integer endpoints and their parameter vectors are preserved in [internal-source-reference], with the required original-row-order restoration [internal-source-reference]. Together with J75 source those reconstruct every exact claimed control and the85742-byte rational report. Neither the sum loss nor the square-root sparsity loss achieved110; exact census exposes44P/54Q and12P/8Q positive bars respectively. The latter exceeds the floating nominee's8P/7Q because of tiny positive bars and rationalization. No thresholded floating statement is an exact zero.

## warp76.py
```python
"""J76 smooth material-warp nomination with live hull, volume centroid and all bars.
Inputs: literal immutable R22-B7 via J75_REFERENCE110_CAP233.py.
Floating optimizer output must be rationalized and exactly audited separately.
"""
import os
os.environ.setdefault('OPENBLAS_NUM_THREADS','1')
os.environ.setdefault('OMP_NUM_THREADS','1')
import json,sys,time
from pathlib import Path
import numpy as np
from scipy.spatial import ConvexHull,QhullError
from scipy.optimize import minimize
import torch
import J75_REFERENCE110_CAP233 as m
torch.set_num_threads(1)
torch.set_default_dtype(torch.float64)

def topology(a):
 H=ConvexHull(a);tri=H.simplices.copy()
 det=np.einsum('ij,ij->i',np.cross(a[tri[:,1]]-a[tri[:,0]],a[tri[:,2]]-a[tri[:,0]]),H.equations[:,:3])
 neg=det<0;tri[neg,1],tri[neg,2]=tri[neg,2].copy(),tri[neg,1].copy()
 # Coplanar nomination merge; exact endpoints use integer support tests.
 groups=[];owner=np.empty(len(tri),int)
 for k,eq in enumerate(H.equations):
  match=next((j for j,t in enumerate(groups) if np.max(abs(eq-H.equations[t]))<1e-10),None)
  if match is None:owner[k]=len(groups);groups.append(k)
  else:owner[k]=match
 edgeown={}
 for k,t in enumerate(tri):
  for i,j in zip(t,np.roll(t,-1)):
   edgeown.setdefault(tuple(sorted((int(i),int(j)))),[]).append(int(owner[k]))
 edges=[];dual=[]
 for e,oo in sorted(edgeown.items()):
  assert len(oo)==2
  if oo[0]!=oo[1]:edges.append(e);dual.append(oo)
 verts=H.vertices;remap={int(v):i for i,v in enumerate(verts)}
 ep=np.array([[remap[i],remap[j]] for i,j in edges],int)
 return tri,tri[groups],verts,ep,np.array(dual,int),H.volume

def gate_values(x,edges):
 u=x[edges[:,0]];v=x[edges[:,1]];d=v-u
 dd=(d*d).sum(1)
 t=torch.clamp(-(u*d).sum(1)/torch.clamp(dd,min=1e-30),0,1)
 return ((u+t[:,None]*d)**2).sum(1)

def allbars(x,edges):
 births=(x*x).sum(1);weights=gate_values(x,edges)
 b=births.detach().numpy();w=weights.detach().numpy()
 par=list(range(len(x)));peak=par.copy();pairs=[]
 def find(i):
  while par[i]!=i:par[i]=par[par[i]];i=par[i]
  return i
 for k in np.argsort(-w,kind='stable'):
  i,j=edges[k];a,z=find(int(i)),find(int(j))
  if a==z:continue
  if b[peak[a]]<b[peak[z]]:a,z=z,a
  ii=peak[z]
  # Keep all observable positive depths; no assertion of exact zero from this threshold.
  if b[ii]-w[k]>1e-13*max(b[ii],1e-30):pairs.append((ii,int(k)))
  par[z]=a
 if not pairs:return births.sum()*0,[],[]
 ii=np.array([i for i,k in pairs]);kk=np.array([k for i,k in pairs])
 depths=1-weights[kk]/births[ii]
 return depths.sum(),depths.detach().numpy().tolist(),pairs

class Problem:
 def __init__(self,degree=2,weights=(1.,1.),rootdir='warp76_out'):
  K=m.hull(m.points());V,M=m.mass(K);c=m.mul(M,1/V)
  p=np.array([m.sub(v,c) for v in K['points']],float)
  self.c=np.array(c,float);self.p=p;self.pt=torch.tensor(p);self.weights=weights
  self.exponents=[(a,b,d) for s in range(2,degree+1) for a in range(s+1) for b in range(s-a+1) for d in [s-a-b]]
  basis=np.stack([p[:,0]**a*p[:,1]**b*p[:,2]**d for a,b,d in self.exponents],axis=1)
  # Remove translation and affine components in a fixed point-sample metric, not a mass claim.
  X=np.column_stack([np.ones(len(p)),p]);self.coeff=np.linalg.lstsq(X,basis,rcond=None)[0]
  basis-=X@self.coeff
  self.B=torch.tensor(basis);self.n=basis.shape[1]*3;self.basevol=float(V)
  self.best=np.inf;self.it=0;self.root=Path(rootdir);self.root.mkdir(exist_ok=True)
 def evaluate(self,z):
  T=torch.tensor(z,requires_grad=True);a=self.pt+self.B@T.reshape(-1,3)
  raw=a.detach().numpy()
  try:tri,ft,verts,pe,qe,_=topology(raw)
  except (QhullError,AssertionError):return 1000.+float(z@z),2*z
  t=a[tri];w=(t[:,0]*torch.linalg.cross(t[:,1],t[:,2])).sum(1)/6
  V=w.sum();c=(w[:,None]*t.sum(1)/4).sum(0)/V
  x=a[verts]-c
  f=a[ft];nn=torch.linalg.cross(f[:,1]-f[:,0],f[:,2]-f[:,0]);h=(nn*(f[:,0]-c)).sum(1);q=nn/h[:,None]
  P,pb,pp=allbars(x,pe);Q,qb,qp=allbars(q,qe)
  # Finite shape guard; gauge degeneration is not a construction.
  penalty=10*torch.relu(.15-V/self.basevol)**2
  loss=self.weights[0]*P+self.weights[1]*Q+penalty
  loss.backward();value=float(loss.detach());self.it+=1
  if value<self.best-1e-8:
   self.best=value
   report={'value':value,'P':pb,'Q':qb,'VEF':[len(verts),len(pe),len(ft)],'volume':float(V.detach()),'centroid':(c.detach().numpy()+self.c).tolist(),'z':z.tolist(),'exponents':self.exponents,'points':(raw+self.c).tolist(),'weights':self.weights,'iteration':self.it}
   (self.root/'best.json').write_text(json.dumps(report,indent=2))
   np.save(self.root/'best.npy',z)
   if self.it%50<5 or value<.1:print('BEST',self.it,value,'P',pb,'Q',qb,'VEF',report['VEF'],flush=True)
  return value,T.grad.numpy()

def main(degree=2,starts=8):
 rng=np.random.default_rng(760126);allresults=[];base=None
 for run in range(starts):
  prob=Problem(degree,rootdir=f'warp76_d{degree}_{run:02d}')
  if run==0:z=np.zeros(prob.n)
  elif base is not None and run%3!=2:z=base+rng.normal(size=prob.n)*(.01 if run%3==1 else .08)
  else:z=rng.normal(size=prob.n)*.15
  out=minimize(prob.evaluate,z,jac=True,method='L-BFGS-B',bounds=[(-1.5,1.5)]*prob.n,options={'maxiter':500,'maxls':35,'ftol':1e-13,'gtol':1e-8,'maxfun':10000})
  if base is None or prob.best<min(r['best'] for r in allresults):base=np.load(prob.root/'best.npy')
  rr={'run':run,'best':prob.best,'calls':prob.it,'message':str(out.message)};allresults.append(rr)
  Path(f'warp76_d{degree}_summary.json').write_text(json.dumps(allresults,indent=2));print('RUN_DONE',rr,flush=True)
if __name__=='__main__':main(int(sys.argv[1]) if len(sys.argv)>1 else 2,int(sys.argv[2]) if len(sys.argv)>2 else 8)
```

## plane76.py
```python
"""Cap-plane-preserving quadratic continuation; sparse all-positive-bar loss.
Numerical nomination, not exact equilibrium/cancellation evidence.
"""
import json,sys
from pathlib import Path
import numpy as np
import torch
from scipy.optimize import minimize
from scipy.spatial import QhullError
import J75_REFERENCE110_CAP233 as m
from warp76 import Problem,topology,allbars,gate_values

class PlaneProblem(Problem):
 def __init__(self,rootdir,power=.5):
  super().__init__(2,rootdir=rootdir);self.power=power
  normal=np.array([-272.,-1000.,-409.]);normal/=np.linalg.norm(normal)
  _,_,vt=np.linalg.svd(normal[None,:]);tangent=vt[1:].T
  # Full projected monomial basis, plus normal height times affine factors.
  self.tangent=tangent;self.normal=normal
  raw=self.p+self.c;off=68526367/100000/np.linalg.norm(np.array([-272.,-1000.,-409.]))
  height=raw@normal-off
  W=np.zeros((75,3,15));B=self.B.numpy()
  for k in range(6):
   for j in range(2):W[:,:,2*k+j]=B[:,k,None]*tangent[:,j]
  for j in range(3):W[:,:,12+j]=height[:,None]*self.p[:,j,None]*normal
  self.W=torch.tensor(W);self.n=15
 def evaluate(self,z):
  T=torch.tensor(z,requires_grad=True);a=self.pt+torch.einsum('icj,j->ic',self.W,T)
  raw=a.detach().numpy()
  try:tri,ft,verts,pe,qe,_=topology(raw)
  except (QhullError,AssertionError):return 1000.+float(z@z),2*z
  t=a[tri];w=(t[:,0]*torch.linalg.cross(t[:,1],t[:,2])).sum(1)/6
  V=w.sum();c=(w[:,None]*t.sum(1)/4).sum(0)/V
  x=a[verts]-c;f=a[ft];nn=torch.linalg.cross(f[:,1]-f[:,0],f[:,2]-f[:,0]);h=(nn*(f[:,0]-c)).sum(1);q=nn/h[:,None]
  P,pb,pp=allbars(x,pe);Q,qb,qp=allbars(q,qe)
  def sparse_loss(x,edges,pairs):
   if not pairs:return x.sum()*0
   births=(x*x).sum(1);ww=gate_values(x,edges);ii=[i for i,k in pairs];kk=[k for i,k in pairs]
   dd=torch.clamp(1-ww[kk]/births[ii],min=0)
   return ((dd+1e-12)**self.power-(1e-12)**self.power).sum()
  penalty=10*torch.relu(.15-V/self.basevol)**2
  loss=sparse_loss(x,pe,pp)+sparse_loss(q,qe,qp)+penalty
  loss.backward();value=float(loss.detach());self.it+=1
  if value<self.best-1e-9:
   self.best=value
   report={'value':value,'power':self.power,'P':pb,'Q':qb,'VEF':[len(verts),len(pe),len(ft)],'volume':float(V.detach()),'centroid':(c.detach().numpy()+self.c).tolist(),'z':z.tolist(),'points':(raw+self.c).tolist(),'iteration':self.it}
   (self.root/'best.json').write_text(json.dumps(report,indent=2));np.save(self.root/'best.npy',z)
   if self.it%50<5:print('BEST',self.root.name,self.it,value,len(pb),len(qb),max(pb,default=0),max(qb,default=0),flush=True)
  return value,T.grad.numpy()

def main(starts=16):
 rng=np.random.default_rng(760226);res=[];base=None
 for k in range(starts):
  pr=PlaneProblem(f'plane76_{k:02d}')
  if k==0:z=np.zeros(15)
  elif base is not None and k%4!=3:z=base+rng.normal(size=15)*(.002 if k%4==1 else .02)
  else:z=rng.normal(size=15)*.1
  z[12:]=np.clip(z[12:],-.24,.24)
  out=minimize(pr.evaluate,z,jac=True,method='L-BFGS-B',bounds=[(-1.5,1.5)]*12+[(-.25,.25)]*3,options={'maxiter':600,'maxls':40,'ftol':1e-14,'gtol':1e-8,'maxfun':10000})
  if base is None or pr.best<min(x['best'] for x in res):base=np.load(pr.root/'best.npy')
  row={'run':k,'best':pr.best,'calls':pr.it,'message':str(out.message)};res.append(row);Path('plane76_summary.json').write_text(json.dumps(res,indent=2));print('RUN_DONE',row,flush=True)
if __name__=='__main__':main(int(sys.argv[1]) if len(sys.argv)>1 else 16)
```
