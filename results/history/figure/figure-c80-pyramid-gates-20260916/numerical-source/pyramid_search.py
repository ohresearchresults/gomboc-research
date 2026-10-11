"""Finite own-volume-centroid search in the convex polygonal-pyramid family.
All proposals are numerical. Only separate exact hull audits certify an endpoint.
"""
import argparse,hashlib,json,os
os.environ['OPENBLAS_NUM_THREADS']='1';os.environ['OMP_NUM_THREADS']='1'
from pathlib import Path
import numpy as np
from scipy.spatial import ConvexHull
from scipy.optimize import minimize
import torch
torch.set_num_threads(1);torch.set_default_dtype(torch.float64)
def encoded(o):return json.dumps(o,sort_keys=True,separators=(',',':')).encode()
class Pyramid:
 def __init__(self,path,tau=1e-4):
  b=Path(path).read_bytes();self.sha=hashlib.sha256(b).hexdigest();P=np.array(json.loads(b)['points'],float)/1e8
  assert len(P)==21 and sum(P[:,1]!=P[0,1])==1
  self.apex=int(np.where(P[:,1]!=P[0,1])[0][0]);B=np.delete(P,self.apex,axis=0)[:,[0,2]];B=B[ConvexHull(B).vertices];self.n=len(B);assert self.n==20
  apex=P[self.apex];self.initial=np.r_[B.ravel(),apex[[0,2]],np.log(P[0,1]-apex[1])];self.tau=tau
  self.left=np.arange(self.n);self.right=np.roll(self.left,-1);self.evals=0;self.best={};self.records=[]
 def geom(self,x):
  n=self.n;B=x[:2*n].reshape(n,2);a=x[2*n:2*n+2];h=torch.exp(x[-1]);C=torch.roll(B,-1,0)
  det=B[:,0]*C[:,1]-B[:,1]*C[:,0];area2=det.sum();cb=((B+C)*det[:,None]).sum(0)/(3*area2)
  zero=torch.zeros(n);P=torch.cat((torch.stack((B[:,0],zero,B[:,1]),1),torch.stack((a[0],-h,a[1]))[None,:]))
  g=torch.stack(((3*cb[0]+a[0])/4,-h/4,(3*cb[1]+a[1])/4));X=P-g
  # CCW xz polygon: cross(edge,apex-base) points to the interior; negate.
  normals=-torch.linalg.cross(P[self.right]-P[self.left],P[-1]-P[self.left]);normals=torch.cat((normals,torch.tensor([[0.,1.,0.]])))
  offsets=(normals*torch.cat((X[:-1],X[:1]))).sum(1);Q=normals/offsets[:,None]
  e=C-B;D=B[None,:,:]-B[:,None,:];slack=(e[:,None,0]*D[:,:,1]-e[:,None,1]*D[:,:,0])
  mask=np.ones((n,n),bool);mask[self.left,self.left]=False;mask[self.left,self.right]=False
  return X,Q,slack[mask],area2,offsets,cb,h
 @staticmethod
 def escape(X):
  D=X[None,:,:]-X[:,None,:];den=torch.linalg.vector_norm(X,dim=1)[:,None]*torch.linalg.vector_norm(D,dim=2)
  val=(X[:,None,:]*D).sum(2)/torch.clamp(den,min=1e-100);val=val-torch.eye(len(X))*1e6
  return val.max(dim=1).values
 def objective(self,x):
  self.evals+=1;t=torch.tensor(x,requires_grad=True);X,Q,slack,area,offset,cb,h=self.geom(t);u=self.escape(X);s=self.escape(Q)
  du=torch.clamp(self.tau-u,min=0);ds=torch.clamp(self.tau-s,min=0)
  du=du.clone();ds=ds.clone();du[torch.argmin(u)]=0;ds[torch.argmin(s)]=0
  loss=(du**2).sum()+(ds**2).sum();loss.backward()
  return float(loss.detach()),t.grad.numpy()
 def constraints(self,x):
  with torch.no_grad():X,Q,slack,area,offset,cb,h=self.geom(torch.tensor(x));return slack.numpy()-1e-7
 def constraint_jac(self,x):
  def fun(t):return self.geom(t)[2]-1e-7
  return torch.autograd.functional.jacobian(fun,torch.tensor(x),vectorize=True).numpy()
 def report(self,x):
  with torch.no_grad():
   X,Q,c,area,o,cb,h=self.geom(torch.tensor(x));s=self.escape(Q).numpy();u=self.escape(X).numpy();X=X.numpy();Q=Q.numpy()
  return dict(x=list(map(float,x)),S=int(sum(s<-1e-9)),U=int(sum(u<-1e-9)),Su=int(sum(abs(s)<=1e-9)),Uu=int(sum(abs(u)<=1e-9)),S_ids=np.where(s<-1e-9)[0].tolist(),U_ids=np.where(u<-1e-9)[0].tolist(),s=s.tolist(),u=u.tolist(),convex_min=float(c.min()),height=float(h),base_centroid=cb.tolist(),points_own_centred=X.tolist(),dual_own_centred=Q.tolist())
def main():
 ap=argparse.ArgumentParser();ap.add_argument('--points',required=True);ap.add_argument('--out',required=True);ap.add_argument('--starts',type=int,default=12);ap.add_argument('--maxiter',type=int,default=400);ap.add_argument('--seed',type=int,default=801622);ap.add_argument('--tau',type=float,default=1e-4);a=ap.parse_args()
 obj=Pyramid(a.points,a.tau);out=Path(a.out);out.mkdir(parents=True,exist_ok=False);rng=np.random.default_rng(a.seed);records=[];best=None
 print('PARENT',obj.report(obj.initial),flush=True)
 x=obj.initial;f,g=obj.objective(x);eps=1e-6;ix=[0,10,39,40,41,42];num=np.array([(obj.objective(x+eps*np.eye(len(x))[i])[0]-obj.objective(x-eps*np.eye(len(x))[i])[0])/(2*eps) for i in ix]);assert max(abs(num-g[ix]))<2e-6;print('GRADIENT_PASS',max(abs(num-g[ix])),flush=True)
 for k in range(a.starts):
  x=obj.initial.copy()
  if k: x[-3:-1]+=rng.normal(size=2)*.35;x[-1]=rng.uniform(-4,1.5)
  r=minimize(obj.objective,x,jac=True,method='SLSQP',bounds=[(-3,3)]*(len(x)-1)+[(-7,2)],constraints=[{'type':'ineq','fun':obj.constraints,'jac':obj.constraint_jac}],options={'maxiter':a.maxiter,'ftol':1e-13,'disp':False})
  row=obj.report(r.x);row.update(start=k,status=int(r.status),message=r.message,loss=float(r.fun),iterations=int(r.nit));records.append(row)
  rank=(row['S']+row['U']+row['Su']+row['Uu'],row['loss']) if row['convex_min']>0 else (1000,row['loss'])
  if best is None or rank<best[0]:best=(rank,row);(out/'BEST.json').write_bytes(encoded(row))
  (out/'SEARCH.json').write_bytes(encoded({'parameters':vars(a),'input_sha':obj.sha,'records':records,'evals':obj.evals}));print('CASE',k,row['S'],row['U'],row['Su'],row['Uu'],row['loss'],'convex',row['convex_min'],'iter',r.nit,'status',r.status,flush=True)
  if row['S']==row['U']==1 and row['Su']==row['Uu']==0 and row['convex_min']>0:print('NUMERICAL_110_PROPOSAL',flush=True);break
 print('PYRAMID_FINITE_SEARCH_ENDED',len(records),obj.evals,best[0],flush=True)
if __name__=='__main__':main()
