"""Incidence-preserving physical projective/affine searches on exact selected hulls.
A nonsingular projective map with positive denominators retains all true facets.
Mass is re-integrated AFTER the map, then both genuine equilibrium graphs used.
"""
from pathlib import Path
from collections import defaultdict
import sys,json,time
import numpy as np
from scipy.optimize import minimize
import jax
import jax.numpy as jnp
from gmpy2 import mpq
from support_persistence import ROOT,barcode
from geometry import angular_scores
sys.set_int_max_str_digits(0)

def load(path):
 r=json.loads(path.read_text());X=np.array([[float(mpq(v)) for v in p] for p in r['raw_vertices']]);Y=np.array([[float(mpq(n,h)) for n in row] for row,h in zip(r['normals'],r['offsets'])]);faces=r['faces'];tri=np.array([[f[0],f[i],f[i+1]] for f in faces for i in range(1,len(f)-1)]);eu=np.array(r['edges']);edgefaces=defaultdict(list)
 for k,f in enumerate(faces):
  for i,j in zip(f,f[1:]+f[:1]):edgefaces[tuple(sorted((i,j)))].append(k)
 es=np.array([edgefaces[tuple(e)] for e in eu]);assert es.shape==(r['E'],2)
 return X,Y,tri,eu,es,r
@jax.jit
def physical(t,X,Y,tri):
 B=t[:3];den=1+X@B;P=X/den[:,None];A=jnp.array([[jnp.exp(t[3]),0.,0.],[t[5],jnp.exp(t[4]),0.],[t[6],t[7],jnp.exp(-t[3]-t[4])]]);P=P@A;Q=(Y+B)@jnp.linalg.inv(A).T
 a,b,c=P[tri[:,0]],P[tri[:,1]],P[tri[:,2]];six=jnp.sum(a*jnp.cross(b,c),axis=1);g=jnp.sum(six[:,None]*(a+b+c),axis=0)/(4*six.sum());Z=P-g;Q=Q/(1-Q@g)[:,None]
 return Z,Q,g,six.sum()/6
@jax.jit
def core(t,X,Y,tri,bp,bw,bq,qw,tau):
 def fun(t):
  Z,Q,g,vol=physical(t,X,Y,tri)
  def loss(A,p,w):
   root,a,b=A[p[:,0]],A[p[:,1]],A[p[:,2]];d=b-a;tt=jnp.clip(-jnp.sum(a*d,axis=1)/jnp.sum(d*d,axis=1),0,1);birth=jnp.sum(root*root,axis=1);depth=jnp.maximum(birth-jnp.sum((a+tt[:,None]*d)**2,axis=1),0)*w/birth
   return jnp.where(tau<0,jnp.sum(depth*depth),jnp.log1p(depth/jnp.maximum(tau,1e-12)).sum())
  return loss(Z,bp,bw)+loss(Q,bq,qw)
 return jax.value_and_grad(fun)(t)
class Search:
 def __init__(self,path,out,tau):
  self.X,self.Y,self.tri,self.eu,self.es,self.report=load(path);self.out=out;out.mkdir(parents=True,exist_ok=True);self.tau=tau;self.calls=0;self.best=np.inf;self.bestcount=1000;self.hist=[];self.target=False
 def eval(self,t):
  if min(1+self.X@t[:3])<.05:return 1e6,np.zeros(8)
  Z,Q,g,v=map(np.asarray,physical(t,self.X,self.Y,self.tri));bp,bw,p=barcode(Z,np.ones(len(Z)),self.eu);bq,qw,q=barcode(Q,np.ones(len(Q)),self.es);val,grad=core(t,self.X,self.Y,self.tri,bp,bw,bq,qw,self.tau);val=float(val);grad=np.asarray(grad)
  if not np.isfinite(val) or not np.isfinite(grad).all() or v<=0:return 1e6,np.zeros(8)
  self.calls+=1;s=angular_scores(Q).max(1);u=angular_scores(Z).max(1);row=dict(S=int((s<0).sum()),U=int((u<0).sum()),loss=val,floor=float(min(np.sort(s)[1],np.sort(u)[1])),t=t.tolist(),calls=self.calls,tau=self.tau,volume=float(v),centroid=g.tolist(),V=self.report['V'],E=self.report['E'],F=self.report['F'])
  if val<self.best:self.best=val;np.save(self.out/'best_t.npy',t);(self.out/'best.json').write_text(json.dumps(row,indent=2)+'\n')
  if row['S']+row['U']<self.bestcount:
   self.bestcount=row['S']+row['U'];self.hist.append(row);np.save(self.out/'fewest_t.npy',t);(self.out/'history.json').write_text(json.dumps(self.hist,indent=2)+'\n');print(self.out,row,flush=True)
  if row['S']==row['U']==1 and row['floor']>1e-10:
   self.target=True;np.save(self.out/'NUMERICAL_NOMINATION_t.npy',t);(self.out/'NUMERICAL_NOMINATION.json').write_text(json.dumps(row,indent=2)+'\n')
  return val,grad
 def run(self,t,nit=1500):
  opt=minimize(self.eval,t,jac=True,method='L-BFGS-B',bounds=[(-.8,.8)]*3+[(-1.5,1.5)]*5,options={'maxiter':nit,'maxls':40,'maxcor':15,'gtol':1e-10,'ftol':1e-14});np.save(self.out/'final_t.npy',opt.x);print('PROJECTIVE_DONE',self.out,opt.fun,opt.nit,self.bestcount,opt.message,flush=True);return np.load(self.out/'best_t.npy')
if __name__=='__main__':
 path=ROOT/(sys.argv[1] if len(sys.argv)>1 else 'artifacts/grow_closed_subset/exact_iteration16/audit.json');base=ROOT/'artifacts/selected_projective'/path.parent.name;base.mkdir(parents=True,exist_ok=True);(base/'source.json').write_text(json.dumps(dict(exact_source=str(path)))+'\n');rng=np.random.default_rng(77551)
 for seed in range(24):
  t=np.zeros(8) if seed==0 else rng.normal(size=8)*.08
  for k,tau in enumerate([-1.,.03,.003]):
   obj=Search(path,base/f'seed{seed}_stage{k}',tau);t=obj.run(t)
   if obj.target:break
  if obj.target:break
