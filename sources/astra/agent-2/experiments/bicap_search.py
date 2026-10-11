"""Two true supporting caps plus freely moving intermediate physical vertices.
With b bottom inputs, t top inputs and m intermediate inputs, E<=2(b+t)+3m.
This is a physical coordinate family; own homogeneous mass is integrated each call.
All numerical outputs need rational reconstruction and full independent auditing.
"""
from pathlib import Path
from collections import defaultdict
from functools import partial
from fractions import Fraction
import json,sys,time
import numpy as np
from scipy.spatial import ConvexHull,QhullError
from scipy.optimize import minimize
import jax
import jax.numpy as jnp
from support_persistence import ROOT,barcode
from geometry import angular_scores

def coords(q,b,t):
 n=(len(q)-3+b+t)//3;m=n-b-t
 xy=q[:2*n].reshape(n,2);ss=q[2*n:2*n+m];H=np.exp(q[-3]);uv=q[-2:];h=H+xy@uv
 if h.min()<1e-7:raise ValueError('crossing cap planes')
 zz=np.r_[np.zeros(b),np.ones(t),1/(1+np.exp(-ss))]*h
 return np.c_[xy,zz]

def jcoords(q,b,t):
 n=(len(q)-3+b+t)//3;m=n-b-t
 xy=q[:2*n].reshape(n,2);ss=q[2*n:2*n+m];H=jnp.exp(q[-3]);uv=q[-2:];hh=H+xy@uv
 zz=jnp.concatenate([jnp.zeros(b),jnp.ones(t),jax.nn.sigmoid(ss)])*hh
 return jnp.column_stack([xy,zz])

def graph(q,b,t):
 X=coords(q,b,t);N=len(X);h=ConvexHull(X);tri=h.simplices.copy();norm=np.cross(X[tri[:,1]]-X[tri[:,0]],X[tri[:,2]]-X[tri[:,0]]);flip=np.einsum('ij,ij->i',norm,h.equations[:,:3])<0;tri[flip]=tri[flip][:,[0,2,1]]
 low=np.all(tri<b,axis=1);high=np.all((tri>=b)&(tri<b+t),axis=1);side=~(low|high)
 if not (low.any() and high.any()):raise ValueError('missing supporting cap')
 sf=tri[side];f=len(sf);owner=np.zeros(len(tri),int);owner[side]=np.arange(f);owner[low]=f;owner[high]=f+1;eo=defaultdict(list)
 for row,o in zip(tri,owner):
  for i,j in zip(row,np.roll(row,-1)):eo[tuple(sorted((int(i),int(j))))].append(int(o))
 eu=[];es=[]
 for e,oo in eo.items():
  if len(oo)!=2:raise ValueError('nonmanifold triangulation')
  if oo[0]!=oo[1]:eu.append(e);es.append(oo)
 eu=np.array(eu);es=np.array(es);V=len(h.vertices);E=len(eu);F=f+2
 if V-E+F!=2 or E>2*(b+t)+3*(N-b-t) or E<17:raise ValueError('invalid edge budget')
 T=2*N-4;tm=np.r_[np.ones(len(tri)),np.zeros(T-len(tri))];tri=np.r_[tri,np.tile(tri[0],(T-len(tri),1))]
 QN=2*N;sfm=np.r_[np.ones(f),np.zeros(QN-2-f)];sf=np.r_[sf,np.tile(sf[0],(QN-2-f,1))];es=np.where(es==f,QN-2,es);es=np.where(es==f+1,QN-1,es)
 xm=np.zeros(N);xm[h.vertices]=1;ym=np.r_[sfm,1,1];Z,Y,c,v=physical(q,b,t,tri,tm,sf);Z,Y,c,v=map(np.asarray,(Z,Y,c,v))
 bp,bw,p=barcode(Z,xm,eu);bq,qw,pq=barcode(Y,ym,es)
 return dict(X=X,Z=Z,Y=Y,c=c,volume=float(v),tri=tri,tm=tm,sf=sf,xm=xm,ym=ym,bp=bp,bw=bw,bq=bq,qw=qw,p=p,pq=pq,V=V,E=E,F=F,eu=eu,es=es)

@partial(jax.jit,static_argnums=(1,2))
def physical(q,b,t,tri,tm,sf):
 X=jcoords(q,b,t);a,bb,c=X[tri[:,0]],X[tri[:,1]],X[tri[:,2]];six=jnp.sum(a*jnp.cross(bb,c),axis=1)*tm;g=jnp.sum(six[:,None]*(a+bb+c),axis=0)/(4*jnp.sum(six));Z=X-g
 a,bb,c=Z[sf[:,0]],Z[sf[:,1]],Z[sf[:,2]];norm=jnp.cross(bb-a,c-a);Y=norm/jnp.sum(norm*a,axis=1)[:,None]
 cap=jnp.array([-q[-2],-q[-1],1.]);Y=jnp.concatenate([Y,jnp.array([[0.,0.,-1/g[2]]]),(cap/(jnp.exp(q[-3])-cap@g))[None]],axis=0)
 return Z,Y,g,jnp.sum(six)/6

@partial(jax.jit,static_argnums=(1,2))
def lossgrad(q,b,t,tri,tm,sf,bp,bw,bq,qw,tau):
 def fun(q):
  Z,Y,g,v=physical(q,b,t,tri,tm,sf)
  def bars(A,p,w):
   r,a,bb=A[p[:,0]],A[p[:,1]],A[p[:,2]];d=bb-a;alpha=jnp.clip(-jnp.sum(a*d,axis=1)/jnp.maximum(jnp.sum(d*d,axis=1),1e-30),0,1);death=a+alpha[:,None]*d;birth=jnp.sum(r*r,axis=1);depth=jnp.maximum(birth-jnp.sum(death*death,axis=1),0)*w/birth
   return jnp.log1p(depth/tau).sum()
  return bars(Z,bp,bw)+bars(Y,bq,qw)
 return jax.value_and_grad(fun)(q)

def stats(g):
 vals=[];cs=[]
 for A,mask in [(g['Z'],g['xm']),(g['Y'],g['ym'])]:
  a=angular_scores(A);a[:,mask==0]=-np.inf;v=a.max(1)[mask>0];vals.append(np.sort(v)[1]);cs.append(int((v<0).sum()))
 return dict(S=cs[1],U=cs[0],floor=float(min(vals)),V=g['V'],E=g['E'],F=g['F'],C=2*g['E'],centroid=g['c'].tolist(),volume=g['volume'])

class Search:
 def __init__(self,q,b,t,out,tau):
  self.q=q;self.b=b;self.t=t;self.out=out;out.mkdir(parents=True,exist_ok=True);self.tau=tau;self.calls=0;self.best=np.inf;self.bestcount=1000;self.history=[];self.target=False;self.start=time.time()
 def eval(self,q):
  try:
   g=graph(q,self.b,self.t);val,grad=lossgrad(q,self.b,self.t,g['tri'],g['tm'],g['sf'],g['bp'],g['bw'],g['bq'],g['qw'],self.tau);val=float(val);grad=np.asarray(grad)
   if not np.isfinite(val) or not np.isfinite(grad).all():raise ValueError('nonfinite')
  except (QhullError,ValueError,AssertionError,np.linalg.LinAlgError):return 1e6,np.zeros_like(q)
  self.calls+=1;s=stats(g);s.update(loss=val,calls=self.calls,seconds=time.time()-self.start,tau=self.tau)
  if val<self.best:
   self.best=val;np.save(self.out/'best_theta.npy',q);np.save(self.out/'best_points.npy',g['X']);(self.out/'best.json').write_text(json.dumps(s,indent=2)+'\n')
  if s['S']+s['U']<self.bestcount or self.calls%500==0:
   self.bestcount=min(self.bestcount,s['S']+s['U']);self.history.append(s);(self.out/'history.json').write_text(json.dumps(self.history,indent=2)+'\n');print(self.out,s,flush=True)
  if s['S']==s['U']==1 and s['floor']>1e-10:
   self.target=True;np.save(self.out/'NUMERICAL_NOMINATION_theta.npy',q);np.save(self.out/'NUMERICAL_NOMINATION_points.npy',g['X']);(self.out/'NUMERICAL_NOMINATION.json').write_text(json.dumps(s,indent=2)+'\n')
  return val,grad
 def run(self,iters):
  N=(len(self.q)-3+self.b+self.t)//3;m=N-self.b-self.t;bounds=[(None,None)]*(2*N)+[(-14,14)]*m+[(-5,5),(-5,5),(-5,5)]
  opt=minimize(self.eval,self.q,jac=True,method='L-BFGS-B',bounds=bounds,options={'maxiter':iters,'maxls':40,'maxcor':25,'gtol':1e-10,'ftol':1e-14});np.save(self.out/'final_theta.npy',opt.x);print('DONE',self.out,opt.fun,opt.nit,opt.message,flush=True);return np.load(self.out/'best_theta.npy')

def initial(seed=1,extra=0):
 sys.set_int_max_str_digits(0);r=json.loads((ROOT/'artifacts/baseline/B_exact.json').read_text());meta=json.loads((ROOT/'artifacts/closed_subset/minimum_closure.json').read_text());P=np.load(ROOT/'artifacts/closed_subset/X_centered.npy');base=r['faces'][3];axis=-np.array(r['normals'][3],float);axis/=np.linalg.norm(axis);e=np.eye(3)[np.argmin(abs(axis))];e=np.cross(axis,e);e/=np.linalg.norm(e);basis=np.c_[e,np.cross(axis,e),axis];R=P@basis;origin=np.array([0.,0.,R[base,2].mean()]);R-=origin;top=meta['top_vertex'];middle=[i for i in meta['selected'] if i not in base and i!=top]
 rng=np.random.default_rng(seed)
 if extra:
  omitted=[i for i in range(len(P)) if i not in meta['selected']];from scipy.spatial.distance import cdist
  for _ in range(extra):
   distances=cdist(R[omitted],R[base+middle+[top]]).min(1);j=int(np.argmax(distances));middle.append(omitted.pop(j))
 angles=np.arange(6)*np.pi/3;cap=R[top]+np.c_[np.cos(angles),np.sin(angles),np.zeros(6)]*1e-4;X=np.vstack([R[base],cap,R[middle]]);b=len(base);t=6;H=R[top,2];X[:b,2]=0;X[b:b+t,2]=H;X[b+t:]+=rng.normal(size=X[b+t:].shape)*1e-7;ss=np.log(X[b+t:,2]/(H-X[b+t:,2]));q=np.r_[X[:,:2].ravel(),ss,np.log(H),0.,0.]
 return q,b,t,dict(source='artifacts/baseline/B_exact.json',subset='artifacts/closed_subset/minimum_closure.json',base_ids=base,middle_ids=middle,top_id=top,basis=basis.tolist(),origin=origin.tolist(),cap_radius=1e-4,jitter_seed=seed,jitter_sigma=1e-7,edge_upper_bound=2*(b+t)+3*len(middle))

if __name__=='__main__':
 seed=int(sys.argv[1]) if len(sys.argv)>1 else 1;extra=int(sys.argv[2]) if len(sys.argv)>2 else 0;q,b,t,meta=initial(seed,extra);out=ROOT/'artifacts/bicap_search'/f'closure_seed{seed}_extra{extra}';out.mkdir(parents=True,exist_ok=True);meta.update(bottom=b,top=t);(out/'construction.json').write_text(json.dumps(meta,indent=2)+'\n');np.save(out/'initial_theta.npy',q);np.save(out/'initial_points.npy',coords(q,b,t));print('INITIAL',stats(graph(q,b,t)),flush=True)
 for k,tau in enumerate([.03,.01,.003,.001,.0003]):
  obj=Search(q,b,t,out/f'stage{k}',tau);q=obj.run(1600)
  if obj.target:break
