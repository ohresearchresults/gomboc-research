"""Convex translated homothetic polygon sections with a fixed genuine mesh.
At L internal knots and an m-gon section: V=mL+2,E=m(2L+1),F=m(L+1).
Green-function curvature coordinates guarantee convexity whenever B is convex:
r=sum k_i G_i, mu=linear endpoints-sum k_i*a_i*G_i, k_i>0,a_i in int(B).
Thus every horizontal support n.mu+h_B(n)*r is strictly concave at every knot.
All calculations use the actual physical homogeneous body and its own centroid.
"""
from functools import partial
from pathlib import Path
import json,sys,time
import numpy as np
from scipy.spatial import ConvexHull,QhullError
from scipy.optimize import minimize,root
import jax
import jax.numpy as jnp
from support_persistence import ROOT,barcode
from geometry import angular_scores,mass

def unpack(q,m,L):
 n=2*m;B=q[:n].reshape(m,2);k=q[n:n+L];n+=L;lam=q[n:n+2*L].reshape(L,2);n+=2*L;dz=q[n:n+L+1];top=q[-2:];return B,k,lam,dz,top

def geometry_jax(q,m,L):
 B,lk,lam,w,top=unpack(q,m,L);d=2*jax.nn.softmax(w);z=jnp.r_[-1.,-1+jnp.cumsum(d)];zz=z[1:-1];K=jnp.exp(lk);a=jax.nn.softmax(lam@B.T,axis=1)@B
 G=(jnp.minimum(z[:,None],zz[None])+1)*(1-jnp.maximum(z[:,None],zz[None]))/2
 rr=G@K;mu=(z[:,None]+1)/2*top-(G*K[None,:])@a
 X=jnp.concatenate([jnp.c_[mu[:1],z[:1]],jnp.concatenate([jnp.reshape(mu[1:-1,None,:]+rr[1:-1,None,None]*B[None,:,:],(-1,2)),jnp.repeat(zz,m)[:,None]],axis=1),jnp.c_[mu[-1:],z[-1:]]],axis=0)
 return X,B,z,rr,mu,a,K

def topology(m,L):
 faces=[];N=m*L+2
 for j in range(m):faces.append([0,1+j,1+(j+1)%m])
 for i in range(L-1):
  for j in range(m):faces.append([1+i*m+j,1+(i+1)*m+j,1+(i+1)*m+(j+1)%m,1+i*m+(j+1)%m])
 for j in range(m):faces.append([1+(L-1)*m+j,N-1,1+(L-1)*m+(j+1)%m])
 # The raw convention is inward for CCW section B; reverse all faces.
 faces=[list(reversed(f)) for f in faces]
 tri=np.array([[f[0],f[i],f[i+1]] for f in faces for i in range(1,len(f)-1)]);st=np.array([f[:3] for f in faces]);e={}
 for k,f in enumerate(faces):
  for i,j in zip(f,f[1:]+f[:1]):e.setdefault(tuple(sorted((i,j))),[]).append(k)
 eu=np.array(list(e));es=np.array(list(e.values()));assert len(e)==m*(2*L+1) and all(len(v)==2 for v in e.values())
 return faces,tri,st,eu,es

@partial(jax.jit,static_argnums=(1,2))
def physical(q,m,L,tri,st):
 X,B,z,r,mu,a,k=geometry_jax(q,m,L);aa,bb,c=X[tri[:,0]],X[tri[:,1]],X[tri[:,2]];six=jnp.sum(aa*jnp.cross(bb,c),axis=1);vol=six.sum()/6;g=jnp.sum(six[:,None]*(aa+bb+c),axis=0)/(4*six.sum());Z=X-g
 aa,bb,c=Z[st[:,0]],Z[st[:,1]],Z[st[:,2]];n=jnp.cross(bb-aa,c-aa);Y=n/jnp.sum(n*aa,axis=1)[:,None]
 return X,Z,Y,g,vol

def graph(q,m,L,mesh=None):
 if mesh is None:mesh=topology(m,L)
 B=np.asarray(unpack(q,m,L)[0]);h=ConvexHull(B)
 if len(h.vertices)!=m or not all(int(h.vertices[(i+1)%m])==(int(h.vertices[i])+1)%m for i in range(m)):raise ValueError('section polygon lost strict convexity/order')
 faces,tri,st,eu,es=mesh;X,Z,Y,g,vol=map(np.asarray,physical(q,m,L,tri,st))
 if vol<=0 or not np.isfinite(Y).all():raise ValueError('invalid physical mass')
 xm=np.ones(len(X));ym=np.ones(len(Y));bp,bw,p=barcode(Z,xm,eu);bq,qw,pq=barcode(Y,ym,es)
 # This independently checks the expected support inequalities numerically.
 if np.max(Z@Y.T-1)>2e-6:raise ValueError('section support convexity failure')
 return dict(X=X,Z=Z,Y=Y,c=g,volume=float(vol),tri=tri,st=st,eu=eu,es=es,bp=bp,bw=bw,bq=bq,qw=qw,p=p,pq=pq,xm=xm,ym=ym)

@partial(jax.jit,static_argnums=(1,2))
def lossgrad(q,m,L,tri,st,bp,bw,bq,qw,tau):
 def fun(q):
  X,Z,Y,g,vol=physical(q,m,L,tri,st)
  def loss(A,p,w):
   root,a,b=A[p[:,0]],A[p[:,1]],A[p[:,2]];d=b-a;alpha=jnp.clip(-jnp.sum(a*d,axis=1)/jnp.maximum(jnp.sum(d*d,axis=1),1e-30),0,1);foot=a+alpha[:,None]*d;birth=jnp.sum(root*root,axis=1);bars=jnp.maximum(birth-jnp.sum(foot*foot,axis=1),0)*w/birth
   return jnp.where(tau<0,jnp.sum(bars*bars),jnp.log1p(bars/jnp.maximum(tau,1e-12)).sum())
  return loss(Z,bp,bw)+loss(Y,bq,qw)
 return jax.value_and_grad(fun)(q)

def stats(g,m,L):
 u=angular_scores(g['Z']).max(1);s=angular_scores(g['Y']).max(1)
 return dict(V=m*L+2,E=m*(2*L+1),F=m*(L+1),C=2*m*(2*L+1),S=int((s<0).sum()),U=int((u<0).sum()),floor=float(min(np.sort(u)[1],np.sort(s)[1])),volume=g['volume'],centroid=g['c'].tolist())

class Search:
 def __init__(self,q,m,L,out,tau):
  self.q=q;self.m=m;self.L=L;self.out=out;out.mkdir(parents=True,exist_ok=True);self.tau=tau;self.calls=0;self.best=np.inf;self.bestcount=10000;self.history=[];self.target=False;self.mesh=topology(m,L);self.start=time.time()
 def eval(self,q):
  try:
   g=graph(q,self.m,self.L,self.mesh);val,grad=lossgrad(q,self.m,self.L,g['tri'],g['st'],g['bp'],g['bw'],g['bq'],g['qw'],self.tau);val=float(val);grad=np.asarray(grad)
   if not np.isfinite(val) or not np.isfinite(grad).all():raise ValueError('nonfinite')
  except (QhullError,ValueError,AssertionError,np.linalg.LinAlgError):return 1e6,np.zeros_like(q)
  self.calls+=1;s=stats(g,self.m,self.L);s.update(loss=val,tau=self.tau,calls=self.calls,seconds=time.time()-self.start)
  if val<self.best:
   self.best=val;np.save(self.out/'best_theta.npy',q);np.save(self.out/'best_points.npy',g['X']);(self.out/'best.json').write_text(json.dumps(s,indent=2)+'\n')
  if s['S']+s['U']<self.bestcount or self.calls%1000==0:
   self.bestcount=min(self.bestcount,s['S']+s['U']);self.history.append(s);(self.out/'history.json').write_text(json.dumps(self.history,indent=2)+'\n');print(self.out,s,flush=True)
  if s['S']==s['U']==1 and s['floor']>1e-9:
   self.target=True;np.save(self.out/'NUMERICAL_NOMINATION_theta.npy',q);np.save(self.out/'NUMERICAL_NOMINATION_points.npy',g['X']);(self.out/'NUMERICAL_NOMINATION.json').write_text(json.dumps(s,indent=2)+'\n')
  return val,grad
 def run(self,iters):
  m,L=self.m,self.L;bounds=[(-3,3)]*(2*m)+[(-12,6)]*L+[(-30,30)]*(2*L)+[(-5,5)]*(L+1)+[(-4,4)]*2
  opt=minimize(self.eval,self.q,jac=True,method='L-BFGS-B',bounds=bounds,options={'maxiter':iters,'maxls':40,'maxcor':30,'gtol':1e-10,'ftol':1e-14});np.save(self.out/'final_theta.npy',opt.x);print('DONE_SECTION',self.out,opt.fun,opt.nit,opt.message,flush=True);return np.load(self.out/'best_theta.npy')

def initial(m,L,beta,seed=0):
 phi=2*np.pi*np.arange(m)/m;B=np.c_[np.cos(phi),np.sin(phi)];z=np.linspace(-1,1,L+2);rr=np.sqrt(1-z*z);phase=1.5*np.pi*(z-z**3/3);mu=beta*np.c_[np.cos(phase)+1,np.sin(phase)];slope=np.diff(rr)/np.diff(z);K=-np.diff(slope);mslope=np.diff(mu,axis=0)/np.diff(z)[:,None];A=np.diff(mslope,axis=0)/K[:,None];lam=[]
 for a in A:
  def f(x):
   logits=B@x;w=np.exp(logits-logits.max());return w@B/w.sum()-a
  sol=root(f,np.zeros(2))
  if not sol.success or np.linalg.norm(f(sol.x))>1e-8:raise ValueError('initial curvature center outside section polygon')
  lam.append(sol.x)
 lam=np.array(lam);q=np.r_[B.ravel(),np.log(K),lam.ravel(),np.zeros(L+1),0.,0.]
 if seed:
  rng=np.random.default_rng(seed);q[2*m:2*m+L]+=rng.normal(size=L)*.1;q[2*m+L:2*m+3*L]+=rng.normal(size=2*L)*.1
 return q

if __name__=='__main__':
 m=int(sys.argv[1]) if len(sys.argv)>1 else 5;L=int(sys.argv[2]) if len(sys.argv)>2 else 24;seed=int(sys.argv[3]) if len(sys.argv)>3 else 0;beta=.02;assert 34<=2*m*(2*L+1)<500
 q=initial(m,L,beta,seed);out=ROOT/'artifacts/section_search'/f'm{m}_L{L}_seed{seed}';out.mkdir(parents=True,exist_ok=True);(out/'construction.json').write_text(json.dumps(dict(m=m,L=L,seed=seed,beta=beta,V=m*L+2,E=m*(2*L+1),F=m*(L+1)),indent=2)+'\n');np.save(out/'initial_theta.npy',q);print('INITIAL_SECTION',stats(graph(q,m,L),m,L),flush=True)
 for k,tau in enumerate([.1,.03,.01,.003,.001,.0003]):
  obj=Search(q,m,L,out/f'stage{k}',tau);q=obj.run(1500)
  if obj.target:break
