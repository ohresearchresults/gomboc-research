# material-188700041cd6

Historical AI scientific source/proof material. Statements retain their original scope; this is not an independently reviewed theorem.

Public derivative: internal-record-identifiers-replaced.

---

# COORD_HULL_LP_V1: incidence-adaptive own-mass escape continuation

Complete runnable numerical production source, not a verified new construction or finite exclusion. Depends on the exact INPUT REPORTs reconstructed from accepted NC57 result figure-0398 (73935bytes,SHA b6c84be62ea56d1c11575d4d6309563f525d734f79b0ad2a299f0b7abd2ccdd3). C372_ALT_FULL_G4 report14190bytes,SHA639b7dd56caf48ee99f1175e20b1f305100dc0fb3f75440dd20aba8df57b4cb5; C378_ALT_POLY_G6 report18534bytes,SHAfc46fb08252486d5c2474d70c6834b2f4849f8de25bcf18ccb059a7aa9ced661. No other implicit source dependency.

Save fenced source as HULL_LP.py,6471bytes,SHAff8e633486cd8117106117a64c81c31a66aadac7489ee82054ae61e916420185. CPython3.13.5,NumPy2.3.5,SciPy1.17.0,Torch2.10.0+cpu,binary64,threads1,assertions. CLI every parameter: REPORT OUT steps gamma seed perturb initial_trust. No output directory may already exist. For example `python HULL_LP.py NC57_SOURCE/proof/C378_ALT_POLY_G6/REPORT.json H378 300 0.001 37801 0 0.005`. A completed execution emits COORD_HULL_LP_FINISHED. This material records source and intended protocol; no completed optimization was claimed when stored. Actual complete trial options, frozen floating-point hex checkpoints and output hashes must be stored separately before using a computed endpoint.

The direction differs materially from TREE_LP/LOCAL_LP: no old-triangle convexity constraints survive as permanent walls. Every trial recomputes actual hull, filled centroid and both mechanical escape landscapes, allowing incidence changes and loss of nonextreme vertices. The physical root is the largest-radius actual vertex; the stable root is the largest-norm actual polar vertex. Any distinct maximum-radius point has nonpositive escape to all others, so a unique unstable point must be that root; applied dually for the stable root. Root changes are allowed. The LP targets selected maximum all-pair escapes; positive-gamma maximum/mean deficit is checked after each genuine hull rebuild. Backtracking may temporarily increase counts but must improve actual merit. Root labels in outputs are fresh floating-hull indices, not NC57 report facets; stable_owners preserve current point-row sets.

Numerical facet merging1e-11, coincident-normal threshold1e-12, covariance/volume floors and binary64 decisions are proposal gates ONLY. No numerical success is an exact certificate. A promising own110 must be rounded/preserved as its own rational object and undergo independent full exact maximal-incidence/mass/SUH/weak verification. Low loss without a strictly positive gamma margin is insufficient. Finite optimizer non-success is not an exclusion.

```python
#!/usr/bin/env python3
"""Incidence-adaptive own-mass escape LP. Numerical proposals only.
Usage: HULL_LP.py REPORT.json OUT steps gamma seed perturb trust
Every trial rebuilds actual hull/own centroid; no frozen-triangle convexity wall.
CPython3.13.5 numpy2.3.5 scipy1.17.0 torch2.10.0+cpu; binary64, threads1.
"""
import os
for k in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS'):os.environ[k]='1'
import sys,json,hashlib,platform
from pathlib import Path
from fractions import Fraction
import numpy as np
import scipy
import torch
from scipy.optimize import linprog
from scipy.spatial import ConvexHull,QhullError
from scipy.sparse import csr_matrix,hstack,vstack,eye
assert __debug__
torch.set_num_threads(1);torch.set_default_dtype(torch.float64)
def enc(v):return json.dumps(v,sort_keys=True,separators=(',',':'))+'\n'
def hx(P):return [[float(x).hex() for x in p] for p in P]
def geometry(z,F):
 T=z[F];a,b,c=T[:,0],T[:,1],T[:,2];w=(a*torch.linalg.cross(b,c)).sum(1)/6
 v=w.sum();g=(w[:,None]*(a+b+c)).sum(0)/(4*v);X=z-g
 n=torch.linalg.cross(b-a,c-a);q=n/(n*X[F[:,0]]).sum(1)[:,None]
 return X,q,g,v

def arrows(W,i,j):
 a=W[i];d=W[j]-a
 return (a*d).sum(1)/(torch.linalg.vector_norm(a,dim=1)*torch.linalg.vector_norm(d,dim=1))

def all_escape(W):
 D=W[None,:,:]-W[:,None,:];r=np.linalg.norm(W,axis=1);dn=np.linalg.norm(D,axis=2)
 # Coincident numerical facet normals represent the same support, not a new root.
 bad=dn<1e-12*np.maximum(1,r[:,None]);dn[bad]=1
 a=np.einsum('ik,ijk->ij',W,D)/(r[:,None]*dn);a[bad]=-np.inf
 return a

def state(P,gamma):
 H=ConvexHull(P);idx=np.sort(H.vertices);P=P[idx];H=ConvexHull(P)
 F=H.simplices.copy();T=P[F];n=np.cross(T[:,1]-T[:,0],T[:,2]-T[:,0]);flip=np.einsum('ij,ij->i',n,H.equations[:,:3])<0;F[flip]=F[flip][:,[0,2,1]]
 with torch.no_grad():X,Q,g,v=geometry(torch.tensor(P),F)
 x=X.numpy();q=Q.numpy();g=g.numpy();v=float(v)
 assert v>1e-12 and np.isfinite(q).all()
 # Select one representative of numerically coplanar maximal supports.
 reps=[]
 for i in range(len(q)):
  if not any(np.linalg.norm(q[i]-q[j])<1e-11*max(1,np.linalg.norm(q[i]),np.linalg.norm(q[j])) for j in reps):reps.append(i)
 reps=np.array(reps,dtype=int);q1=q[reps]
 aU=all_escape(x);aS=all_escape(q1);u=aU.max(1);s=aS.max(1)
 ru=int(np.argmax((x*x).sum(1)));rs=int(np.argmax((q1*q1).sum(1)))
 ui=np.array([i for i in range(len(x)) if i!=ru]);si=np.array([i for i in range(len(q1)) if i!=rs])
 ut=aU[ui].argmax(1);st=aS[si].argmax(1);e=np.r_[u[ui],s[si]];d=np.maximum(gamma-e,0)
 cov=x.T@x/len(x);ev=np.linalg.eigvalsh(cov)
 assert ev[0]>1e-10*ev[-1]
 sm=dict(V=len(P),F=len(q1),E=len(P)+len(q1)-2,S=int((s<0).sum()),U=int((u<0).sum()),
         margin=float(e.min()),loss=float(d@d),merit=float(d.max()+.2*d.mean()),worst=float(d.max()),
         volume=v,centroid=g.tolist(),root_u=ru,root_s=rs,stable=np.where(s<0)[0].tolist(),unstable=np.where(u<0)[0].tolist(),
         stable_owners=[sorted(F[reps[i]].tolist()) for i in np.where(s<0)[0]],
         root_s_owners=sorted(F[reps[rs]].tolist()),covariance_ratio=float(ev[0]/ev[-1]))
 return P,F,reps,(ui,ut,si,st),sm

def main(src,out,steps,gamma,seed,perturb,initial_trust):
 raw=Path(src).read_bytes();ob=json.loads(raw);P=np.array([[float(Fraction(v)) for v in p] for p in ob['points']])
 rng=np.random.default_rng(seed);P=P+perturb*rng.normal(size=P.shape)
 P,F,reps,targets,r=state(P,gamma);P-=np.array(r['centroid']);P/=np.sqrt((P*P).sum(1).mean())
 out=Path(out);out.mkdir(parents=True,exist_ok=False);(out/'INPUT_REPORT.json').write_bytes(raw)
 options=dict(steps=steps,gamma=gamma,seed=seed,perturb=perturb,initial_trust=initial_trust,max_trust=.12,
              line_search=16,lp_feasibility=1e-9,L1weight=1e-5,facetmerge=1e-11,coincidentnormals=1e-12,
              volume_floor=1e-12,covariance_ratio_floor=1e-10,stop_margin=gamma*.1,version='COORD_HULL_LP_V1',
              input_sha256=hashlib.sha256(raw).hexdigest(),python=platform.python_version(),numpy=np.__version__,scipy=scipy.__version__,torch=torch.__version__)
 (out/'OPTIONS.json').write_text(enc(options));trace=[];best=None;trust=initial_trust
 def keep(label,P,r): (out/(label+'.json')).write_text(enc(dict(points_hex=hx(P),record=r,options=options)))
 for it in range(steps):
  P,F,reps,targets,r=state(P,gamma);ui,ut,si,st=targets;D=P.size
  key=(r['S']+r['U'],r['merit'])
  if best is None or key<best:best=key;keep('BEST',P,r);print('HULL_LP_BEST',it,r,flush=True)
  keep('CURRENT',P,r)
  if r['S']==r['U']==1 and r['margin']>gamma*.1:keep('NUMERICAL_WINNER',P,r);break
  def fun(z):
   X,Q,g,v=geometry(z.reshape((-1,3)),F)
   return torch.cat((arrows(X,ui,ut),arrows(Q[reps],si,st)))
  z=torch.tensor(P.ravel(),requires_grad=True);e=fun(z).detach().numpy();J=torch.autograd.functional.jacobian(fun,z,vectorize=True).numpy();m=len(e)
  A=vstack([hstack([-csr_matrix(J),csr_matrix((m,D)),-np.ones((m,1))]),
            hstack([eye(D),-eye(D),csr_matrix((D,1))]),hstack([-eye(D),-eye(D),csr_matrix((D,1))])],format='csr')
  b=np.r_[e-gamma,np.zeros(2*D)];obj=np.r_[np.zeros(D),np.full(D,1e-5/D),1.]
  lp=linprog(obj,A_ub=A,b_ub=b,bounds=[(-trust,trust)]*D+[(0,trust)]*D+[(0,None)],method='highs',options={'primal_feasibility_tolerance':1e-9,'dual_feasibility_tolerance':1e-9})
  rec=dict(iteration=it,before=r,trust=trust,lp_status=int(lp.status),accepted=False)
  if lp.success:
   delta=lp.x[:D].reshape(P.shape);pred=np.maximum(gamma-e-J@delta.ravel(),0);mp=float(pred.max()+.2*pred.mean());rec['predicted_merit']=mp
   for ls in range(16):
    alpha=2.**(-ls)
    try:
     trial,tf,tr,tt,sr=state(P+alpha*delta,gamma)
     if sr['merit']<r['merit']-1e-5*alpha*max(r['merit']-mp,1e-12):
      P=trial-np.array(sr['centroid']);P/=np.sqrt((P*P).sum(1).mean())
      rec.update(accepted=True,alpha=alpha,after=sr);trust=min(.12,trust*(1.3 if alpha==1 else .8));break
    except (QhullError,AssertionError,ValueError,np.linalg.LinAlgError):pass
  if not rec['accepted']:trust*=.5
  trace.append(rec);(out/'TRACE.json').write_text(enc(trace));print('HULL_LP_STEP',it,rec['accepted'],trust,rec.get('after',r)['merit'],flush=True)
  if trust<1e-8:break
 P,F,reps,targets,r=state(P,gamma);keep('FINAL',P,r);(out/'SUMMARY.json').write_text(enc(dict(final=r,best_key=best,iterations=len(trace),options=options)))
 print('COORD_HULL_LP_FINISHED',r,flush=True)
if __name__=='__main__':main(sys.argv[1],sys.argv[2],int(sys.argv[3]),float(sys.argv[4]),int(sys.argv[5]),float(sys.argv[6]),float(sys.argv[7]))
```
