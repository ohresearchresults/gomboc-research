"""Free homogeneous pyramids with exact-planarity parameterization.
Base geometry and apex are free; centroid is 3/4 base-area-centroid +1/4 apex.
Numerical discovery preserves genuine C=4m for m>=9 base hull corners.
"""
from pathlib import Path
import sys,json,time
import numpy as np
from scipy.spatial import ConvexHull
from scipy.optimize import minimize
import jax
import jax.numpy as jnp
from support_persistence import barcode,ROOT
from geometry import angular_scores

def unpack(theta):
 n=(len(theta)-3)//2;B=theta[:2*n].reshape(n,2);A=np.r_[theta[2*n:2*n+2],np.exp(theta[-1])];return B,A

def setup(theta):
 B,A=unpack(theta);n=len(B);cy=ConvexHull(B).vertices;m=len(cy)
 if m<9:raise ValueError('Outside C>=34 research domain')
 a=cy;b=np.roll(cy,-1);edges=np.c_[a,b];cross=B[a,0]*B[b,1]-B[b,0]*B[a,1];area2=cross.sum();bc=np.sum(cross[:,None]*(B[a]+B[b]),axis=0)/(3*area2)
 c=np.r_[.75*bc+.25*A[:2],.25*A[2]];X=np.r_[np.c_[B,np.zeros(n)],A[None,:]];Z=X-c
 ea=np.r_[a,np.tile(a[0],n-m)];eb=np.r_[b,np.tile(b[0],n-m)];sm=np.r_[np.ones(m),np.zeros(n-m)]
 normal=np.cross(X[eb]-X[ea],A-X[ea]);Y=normal/np.einsum('ij,ij->i',normal,Z[ea])[:,None];Y=np.r_[Y,np.array([[0,0,-4/A[2]]])]
 xm=np.zeros(n+1);xm[cy]=1;xm[-1]=1;ym=np.r_[sm,1]
 eu=np.r_[edges,np.c_[cy,np.full(m,n)]];es=np.r_[np.c_[np.arange(m),np.roll(np.arange(m),-1)],np.c_[np.arange(m),np.full(m,n)]]
 bp,bw,p=barcode(Z,xm,eu);bq,qw,q=barcode(Y,ym,es)
 return ea,eb,sm,xm,ym,bp,bw,bq,qw,Z,Y,p,q,cy,float(area2*A[2]/6),c

@jax.jit
def core(theta,ea,eb,sm,bp,bw,bq,qw,tau):
 def f(t):
  n=(len(t)-3)//2;B=t[:2*n].reshape(n,2);A=jnp.r_[t[2*n:2*n+2],jnp.exp(t[-1])]
  cr=(B[ea,0]*B[eb,1]-B[eb,0]*B[ea,1])*sm;area2=jnp.sum(cr);bc=jnp.sum(cr[:,None]*(B[ea]+B[eb]),axis=0)/(3*area2)
  c=jnp.r_[.75*bc+.25*A[:2],.25*A[2]];X=jnp.concatenate([jnp.column_stack([B,jnp.zeros(n)]),A[None,:]],axis=0);Z=X-c
  normals=jnp.cross(X[eb]-X[ea],A-X[ea]);Y=normals/jnp.sum(normals*Z[ea],axis=1)[:,None];Y=jnp.concatenate([Y,jnp.array([[0.,0.,-4/A[2]]])],axis=0)
  def loss(P,pairs,w):
   r,a,b=P[pairs[:,0]],P[pairs[:,1]],P[pairs[:,2]];d=b-a;t=jnp.clip(-jnp.sum(a*d,axis=1)/jnp.maximum(jnp.sum(d*d,axis=1),1e-30),0,1);foot=a+t[:,None]*d
   birth=jnp.sum(r*r,axis=1);bar=jnp.maximum(birth-jnp.sum(foot*foot,axis=1),0)*w/birth
   return jnp.log1p(bar/tau).sum()
  return loss(Z,bp,bw)+loss(Y,bq,qw)
 return jax.value_and_grad(f)(theta)

def encode(X):return np.r_[X[:-1,:2].ravel(),X[-1,:2],np.log(X[-1,2])]

def search(theta,out,tau=.01,maxiter=1200):
 out.mkdir(parents=True,exist_ok=True);best=np.inf;best_count=1000;history=[];calls=0;target=False
 def fun(t):
  nonlocal best,best_count,calls,target
  try:
   ea,eb,sm,xm,ym,bp,bw,bq,qw,Z,Y,p,q,cy,vol,c=setup(t)
   value,grad=core(t,ea,eb,sm,bp,bw,bq,qw,tau);value=float(value);grad=np.array(grad)
  except (ValueError,np.linalg.LinAlgError):return 1e5,np.zeros_like(t)
  calls+=1
  u=angular_scores(Z);u[:,xm==0]=-np.inf;u=u.max(axis=1);s=angular_scores(Y);s[:,ym==0]=-np.inf;s=s.max(axis=1)
  U=int(((u<0)&(xm>0)).sum());S=int(((s<0)&(ym>0)).sum());floor=float(min(np.sort(u[xm>0])[1],np.sort(s[ym>0])[1]))
  if value<best or S+U<best_count:
   info={'S':S,'U':U,'base_corners':len(cy),'C':4*len(cy),'loss':value,'floor':floor,'calls':calls,'tau':tau,'volume':vol,'centroid':c.tolist()};B,A=unpack(t);pts=np.r_[np.c_[B[cy],np.zeros(len(cy))],A[None,:]]
   if value<best:best=value;np.save(out/'lowest_loss_theta.npy',t);np.save(out/'lowest_loss_points.npy',pts);(out/'lowest_loss.json').write_text(json.dumps(info,indent=2)+'\n')
   if S+U<best_count:best_count=S+U;np.save(out/'fewest_theta.npy',t);np.save(out/'fewest_points.npy',pts);(out/'fewest.json').write_text(json.dumps(info,indent=2)+'\n');print(out.name,info,flush=True)
   history.append(info)
  if S==U==1 and floor>1e-10:
   target=True;B,A=unpack(t);np.save(out/'numerical_target_points.npy',np.r_[np.c_[B[cy],np.zeros(len(cy))],A[None,:]]);print('NUMERICAL_TARGET',out,flush=True)
  return value,grad
 bounds=[(None,None)]*(len(theta)-1)+[(-8.,8.)]
 opt=minimize(fun,theta,jac=True,method='L-BFGS-B',bounds=bounds,options={'maxiter':maxiter,'maxls':40,'gtol':1e-10,'ftol':1e-14})
 np.save(out/'final_theta.npy',opt.x);(out/'history.json').write_text(json.dumps(history,indent=2)+'\n');print('PYRAMID_DONE',out.name,opt.fun,opt.nit,best_count,opt.message,flush=True)
 return np.load(out/'lowest_loss_theta.npy'),target

if __name__=='__main__':
 seed=int(sys.argv[1]) if len(sys.argv)>1 else 1;rng=np.random.default_rng(seed);A=np.load(ROOT/'artifacts/pyramids/P2_points.npy');B=np.load(ROOT/'artifacts/pyramids/PB_points.npy')
 # Uniform scalings preserve the initial own-centroid census.
 for X in [A,B]:
  t=encode(X);vol=setup(t)[-2];X/=vol**(1/3)
 for trial in range(16):
  if trial==0:X=A.copy()
  elif trial==1:X=B.copy()
  else:
   u=rng.random();X=(1-u)*A+u*B;X[:-1,:2]+=rng.normal(size=X[:-1,:2].shape)*(.01 if trial%2 else .1);X[-1,0]+=.2*rng.normal();X[-1,2]*=np.exp(rng.normal())
  t=encode(X)
  for stage,tau in enumerate([.03,.003,.0003]):
   out=ROOT/'artifacts/pyramid_search'/f'seed{seed}_trial{trial}_stage{stage}'
   t,found=search(t,out,tau,maxiter=800)
   if found:raise SystemExit(0)
