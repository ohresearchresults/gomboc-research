"""Three parallel polygon layers; genuine edge budget is E<=7n.
There are at most n vertices on each outer supporting plane and at most n on
an intermediate plane. Euler plus the two maximal outer facets gives E<=7n.
For n=35 this guarantees 2E<=490. Every iteration integrates actual hull mass.
"""
from pathlib import Path
from collections import defaultdict
import sys,json,time
import numpy as np
from scipy.spatial import ConvexHull
from scipy.optimize import minimize
import jax
import jax.numpy as jnp
from support_persistence import barcode,ROOT
from geometry import angular_scores

def coordinates(t):
 n=(len(t)-2)//6;xy=t[:-2].reshape(3*n,2);h=np.exp(t[-2]);fraction=1/(1+np.exp(-t[-1]));z=np.repeat([0.,fraction*h,h],n)
 return np.c_[xy,z]

def arrangement(t):
 X=coordinates(t);N=len(X);n=N//3;h=ConvexHull(X);tri=h.simplices.copy()
 normals=np.cross(X[tri[:,1]]-X[tri[:,0]],X[tri[:,2]]-X[tri[:,0]])
 flip=np.einsum('ij,ij->i',normals,h.equations[:,:3])<0;tri[flip]=tri[flip][:,[0,2,1]]
 low=np.all(tri<n,axis=1);high=np.all(tri>=2*n,axis=1);side=~(low|high)
 assert low.any() and high.any()
 side_tri=tri[side];f=len(side_tri);owners=np.zeros(len(tri),int);owners[side]=np.arange(f);owners[low]=f;owners[high]=f+1
 edgeowners=defaultdict(list)
 for row,owner in zip(tri,owners):
  for i,j in zip(row,np.roll(row,-1)):edgeowners[tuple(sorted((int(i),int(j))))].append(int(owner))
 eu=[];es=[]
 for e,own in edgeowners.items():
  assert len(own)==2
  if own[0]!=own[1]:eu.append(e);es.append(own)
 eu=np.array(eu);es=np.array(es);V=len(h.vertices);F=f+2;E=len(eu)
 if V<12:raise ValueError('Outside research domain: fewer than12 true hull vertices')
 assert V-E+F==2 and E<=7*n and E>=17
 max_tri=2*N-4;tm=np.r_[np.ones(len(tri)),np.zeros(max_tri-len(tri))];tri=np.r_[tri,np.tile(tri[0],(max_tri-len(tri),1))]
 max_f=2*N;sfm=np.r_[np.ones(f),np.zeros(max_f-2-f)];side_tri=np.r_[side_tri,np.tile(side_tri[0],(max_f-2-f,1))]
 # Store cap normals at the last two fixed indices; remap the graph accordingly.
 es=np.where(es==f,max_f-2,es);es=np.where(es==f+1,max_f-1,es)
 xm=np.zeros(N);xm[h.vertices]=1;ym=np.r_[sfm,1.,1.]
 a,b,c=X[tri[:,0]],X[tri[:,1]],X[tri[:,2]];six=np.einsum('ij,ij->i',a,np.cross(b,c))*tm;vol=six.sum()/6;cent=np.sum(six[:,None]*(a+b+c),axis=0)/(24*vol);Z=X-cent
 a,b,c=Z[side_tri[:,0]],Z[side_tri[:,1]],Z[side_tri[:,2]];normals=np.cross(b-a,c-a);Y=normals/np.einsum('ij,ij->i',normals,a)[:,None]
 Y=np.r_[Y,[[0,0,-1/cent[2]],[0,0,1/(X[-1,2]-cent[2])]]]
 bp,bw,p=barcode(Z,xm,eu);bq,qw,q=barcode(Y,ym,es)
 return X,tri,tm,side_tri,sfm,xm,ym,bp,bw,bq,qw,Z,Y,p,q,vol,cent,(V,E,F)

@jax.jit
def core(t,tri,tm,side_tri,bp,bw,bq,qw,tau):
 def fun(v):
  n=(len(v)-2)//6;xy=v[:-2].reshape(3*n,2);height=jnp.exp(v[-2]);fraction=jax.nn.sigmoid(v[-1]);z=jnp.repeat(jnp.array([0.,fraction*height,height]),n);X=jnp.column_stack([xy,z])
  a,b,c=X[tri[:,0]],X[tri[:,1]],X[tri[:,2]];six=jnp.sum(a*jnp.cross(b,c),axis=1)*tm;cent=jnp.sum(six[:,None]*(a+b+c),axis=0)/(4*jnp.sum(six));Z=X-cent
  a,b,c=Z[side_tri[:,0]],Z[side_tri[:,1]],Z[side_tri[:,2]];normals=jnp.cross(b-a,c-a);Y=normals/jnp.sum(normals*a,axis=1)[:,None]
  Y=jnp.concatenate([Y,jnp.array([[0.,0.,-1/cent[2]],[0.,0.,1/(height-cent[2])]])],axis=0)
  def loss(P,pairs,w):
   r,a,b=P[pairs[:,0]],P[pairs[:,1]],P[pairs[:,2]];d=b-a;alpha=jnp.clip(-jnp.sum(a*d,axis=1)/jnp.maximum(jnp.sum(d*d,axis=1),1e-30),0,1);foot=a+alpha[:,None]*d;birth=jnp.sum(r*r,axis=1)
   depth=jnp.maximum(birth-jnp.sum(foot*foot,axis=1),0)*w/birth
   return jnp.log1p(depth/tau).sum()
  return loss(Z,bp,bw)+loss(Y,bq,qw)
 return jax.value_and_grad(fun)(t)

class LayerSearch:
 def __init__(self,t,out,tau):
  self.t=t;self.out=out;out.mkdir(parents=True,exist_ok=True);self.tau=tau;self.calls=0;self.best=np.inf;self.best_count=1000;self.history=[];self.target=False
 def eval(self,t):
  try:
   X,tr,tm,st,sm,xm,ym,bp,bw,bq,qw,Z,Y,p,q,vol,cent,vef=arrangement(t)
   value,grad=core(t,tr,tm,st,bp,bw,bq,qw,self.tau);value=float(value);grad=np.array(grad)
  except (ValueError,AssertionError,np.linalg.LinAlgError):return 1e5,np.zeros_like(t)
  if not np.isfinite(value) or not np.isfinite(grad).all():return 1e5,np.zeros_like(t)
  self.calls+=1;u=angular_scores(Z);u[:,xm==0]=-np.inf;u=u.max(axis=1);s=angular_scores(Y);s[:,ym==0]=-np.inf;s=s.max(axis=1)
  U=int(((u<0)&(xm>0)).sum());S=int(((s<0)&(ym>0)).sum());floor=float(min(np.sort(u[xm>0])[1],np.sort(s[ym>0])[1]))
  if value<self.best or S+U<self.best_count:
   info={'V':vef[0],'E':vef[1],'F':vef[2],'C':2*vef[1],'S':S,'U':U,'loss':value,'floor':floor,'calls':self.calls,'tau':self.tau,'volume':float(vol),'centroid':cent.tolist()}
   if value<self.best:self.best=value;np.save(self.out/'lowest_loss_theta.npy',t);np.save(self.out/'lowest_loss_points.npy',X);(self.out/'lowest_loss.json').write_text(json.dumps(info,indent=2)+'\n')
   if S+U<self.best_count:self.best_count=S+U;np.save(self.out/'fewest_points.npy',X);(self.out/'fewest.json').write_text(json.dumps(info,indent=2)+'\n');print(self.out.name,info,flush=True)
   self.history.append(info)
  if S==U==1 and floor>1e-10:
   self.target=True;np.save(self.out/'numerical_target_points.npy',X);print('NUMERICAL_TARGET',self.out,flush=True)
  return value,grad
 def run(self,iterations=1000):
  bounds=[(None,None)]*(len(self.t)-2)+[(-8,8),(-4,4)]
  opt=minimize(self.eval,self.t,jac=True,method='L-BFGS-B',bounds=bounds,options={'maxiter':iterations,'maxls':40,'ftol':1e-14,'gtol':1e-10,'maxcor':25})
  self.t=opt.x;np.save(self.out/'final_theta.npy',opt.x);(self.out/'history.json').write_text(json.dumps(self.history,indent=2)+'\n');print('LAYER_DONE',self.out,opt.fun,opt.nit,self.best_count,opt.message,flush=True)

def densify(B,n):
 if len(B)==n:return B.copy()
 counts=np.ones(len(B),int)
 for _ in range(n-len(B)):counts[np.argmin(counts/np.linalg.norm(np.roll(B,-1,axis=0)-B,axis=1))]+=1
 out=[]
 for i,k in enumerate(counts):
  a,b=B[i],B[(i+1)%len(B)];d=b-a;normal=np.array([d[1],-d[0]])
  for j in range(k):
   t=j/k;out.append((1-t)*a+t*b+normal*1e-4*4*t*(1-t))
 return np.array(out)

def initial(source,n,seed):
 rng=np.random.default_rng(seed);pts=np.load(ROOT/'artifacts/pyramids'/f'{source}_points.npy');B=densify(pts[:-1,:2],n);A=pts[-1];bc=B.mean(axis=0);layers=[]
 for k,t in enumerate([0.,.45,.93]):
  centre=(1-t)*bc+t*A[:2];local=(1-t)*(B-bc)
  angle=[0.,.008,-.007][k]*(1 if source=='P2' else .3);R=np.array([[np.cos(angle),-np.sin(angle)],[np.sin(angle),np.cos(angle)]])
  local=local@R;local*=1.015 if k==1 else 1.
  layers.append(centre+local)
 xy=np.vstack(layers);xy+=rng.normal(size=xy.shape)*1e-5
 h=.93*A[2];fraction=.45/.93;t=np.r_[xy.ravel(),np.log(h),np.log(fraction/(1-fraction))]
 return t

if __name__=='__main__':
 source=sys.argv[1] if len(sys.argv)>1 else 'P2';n=int(sys.argv[2]) if len(sys.argv)>2 else 17;seed=int(sys.argv[3]) if len(sys.argv)>3 else 1
 t=initial(source,n,seed);base=ROOT/'artifacts/layer_search'/f'{source}_n{n}_seed{seed}'
 for k,tau in enumerate([.03,.01,.003,.001,.0003]):
  obj=LayerSearch(t,base/f'stage{k}',tau);obj.run(1500)
  if obj.target:break
  t=np.load(obj.out/'lowest_loss_theta.npy')
