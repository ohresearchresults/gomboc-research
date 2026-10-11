"""Physical vertex chart enforcing a positive escape forest at reference zero.

Every child is rho*proj_u(parent), 0<rho<1. This gives an exact
positive chord at reference zero, not automatically at the mass centroid.
The numerical search imposes actual uniform centroid zero separately.
Only a later complete rational audit can establish an own-centroid Figure.
"""
import argparse,json,time
from pathlib import Path
from itertools import combinations
import numpy as np
from scipy.special import expit,logit
from scipy.optimize import minimize
from scipy.spatial import ConvexHull
from vertex_geometry import geometry
from persistence_birth import bars_loss,evaluate

class Chart:
 def __init__(self,X,rhomax=1.-1e-11):
  self.X0=np.array(X,float);self.n=len(X);aa=(X*X).sum(1)
  self.root=int(aa.argmax());self.order=np.argsort(-aa)
  q=X@X.T-aa[:,None];np.fill_diagonal(q,-np.inf)
  self.parent=q.argmax(1);self.nonroot=[int(i) for i in self.order if i!=self.root]
  assert all(q[i,self.parent[i]]>0 for i in self.nonroot)
  self.index={i:3*k for k,i in enumerate(self.nonroot)};self.d=3*len(self.nonroot)
  self.u0=X/np.sqrt(aa)[:,None];self.B=np.zeros((self.n,3,2));self.rhomax=rhomax
  self.z0=np.zeros(self.d)
  for i in self.nonroot:
   a=np.eye(3)[np.argmin(abs(self.u0[i]))];a-=self.u0[i]*np.dot(a,self.u0[i]);a/=np.linalg.norm(a)
   self.B[i]=np.column_stack((a,np.cross(self.u0[i],a)))
   rho=aa[i]/np.dot(X[i],X[self.parent[i]])
   assert 0<rho<self.rhomax,(i,rho)
   self.z0[self.index[i]+2]=logit(rho/self.rhomax)
  self.tetra=self.choose_tetra(X)
  self.det0=float(np.linalg.det(np.column_stack((X[self.tetra[1]]-X[self.tetra[0]],X[self.tetra[2]]-X[self.tetra[0]],X[self.tetra[3]]-X[self.tetra[0]]))))
  self.volume0=geometry(X,False)['V']
 def choose_tetra(self,X):
  best=None;score=-np.inf
  if len(X)<=50:candidates=combinations(range(len(X)),4)
  else:
   rng=np.random.default_rng(914735)
   candidates=(tuple(rng.choice(len(X),4,replace=False)) for _ in range(25000))
  for ids in candidates:
   A=np.vstack((X[list(ids)].T,np.ones(4)))
   try:w=np.linalg.solve(A,np.array([0.,0.,0.,1.]))
   except np.linalg.LinAlgError:continue
   sc=w.min()
   if sc>score:best=ids;score=sc
  assert score>.005,(score,best)
  return np.array(best,int)
 def physical(self,z):
  X=np.zeros_like(self.X0);DX=np.zeros((self.n,3,self.d));X[self.root]=self.X0[self.root]
  for i in self.nonroot:
   k=self.index[i];p=self.parent[i];u=self.u0[i]+self.B[i]@z[k:k+2]
   uu=np.dot(u,u);sig=expit(z[k+2]);rho=self.rhomax*sig;s=np.dot(u,X[p])/uu
   X[i]=rho*s*u
   P=rho*np.outer(u,u)/uu;DX[i]=P@DX[p]
   Ju=rho*(s*np.eye(3)+np.outer(u,X[p])/uu-2*s*np.outer(u,u)/uu)
   DX[i,:,k:k+2]+=Ju@self.B[i]
   DX[i,:,k+2]+=rho*(1-sig)*s*u
  return X,DX
 def constraints(self,X,DX,g):
  A=np.vstack((X[self.tetra].T,np.ones(4)));w=np.linalg.solve(A,[0.,0.,0.,1.])
  Dw=np.linalg.solve(A,np.vstack((-np.einsum('i,icp->cp',w,DX[self.tetra]),np.zeros((1,self.d)))))
  P=X[self.tetra[1:]]-X[self.tetra[0]];DP=DX[self.tetra[1:]]-DX[self.tetra[0]]
  det=np.dot(P[0],np.cross(P[1],P[2]));Ddet=sum(np.cross(P[(k+1)%3],P[(k+2)%3])@DP[k] for k in range(3))
  c=np.r_[w-.005,det/self.det0-.05]
  J=np.vstack((Dw,Ddet/self.det0))
  return c,J

class Search:
 def __init__(self,chart,out,eta):
  self.c=chart;self.out=Path(out);self.out.mkdir(parents=True,exist_ok=False);self.eta=eta;self.last=None;self.calls=0;self.best=np.inf;self.start=time.time();self.history=[]
  np.savez(self.out/'chart.npz',X0=chart.X0,u0=chart.u0,B=chart.B,parent=chart.parent,order=chart.order,root=chart.root,tetra=chart.tetra,z0=chart.z0,rhomax=chart.rhomax)
 def calc(self,z):
  if self.last is not None and np.array_equal(z,self.last[0]):return self.last[1]
  self.calls+=1;X,DX=self.c.physical(z);g=geometry(X);T=g['T']
  # Reference-plane covectors, not the centered polar. Centroid equalities
  # are separately imposed, and reported own-body diagnostics use own mass.
  H=np.linalg.solve(X[T],np.ones((len(T),3,1)))[...,0]
  DH=np.linalg.solve(X[T],-np.einsum('nc,nacp->nap',H,DX[T]))
  edges={tuple(sorted((a,b))) for tri in T for a,b in zip(tri,np.roll(tri,-1))}
  incident={e:[] for e in edges}
  for k,tri in enumerate(T):
   for a,b in zip(tri,np.roll(tri,-1)):incident[tuple(sorted((a,b)))].append(k)
  qe=np.array([v for v in incident.values()]);assert qe.shape==(len(edges),2)
  loss,G,Q=bars_loss(H,qe,self.eta);J=np.einsum('ic,icp->p',G,DH)
  mass=g['g'];Dmass=g['Dg']@DX.reshape(3*self.c.n,-1)
  ine,DI=self.c.constraints(X,DX,g)
  # This reference-chart objective remains only a search score away from
  # centroid equality. It is never interpreted as own-body acceptance.
  data=(loss,J,mass,Dmass,ine,DI,X,Q)
  self.last=(z.copy(),data)
  if self.calls%100==0:print('THALES_CALL',self.calls,'Q',max(Q,default=0.),'mass',np.linalg.norm(mass),'inside',ine.min(),flush=True)
  return data
 def callback(self,z):
  f,J,m,Dm,ine,DI,X,Q=self.calc(z);own=evaluate(X,self.eta)[2]
  row=dict(it=len(self.history),calls=self.calls,loss=f,refQ=max(Q,default=0.),mass_norm=float(np.linalg.norm(m)),min_interior=float(ine.min()),Pmax=own['Pmax'],Qmax=own['Qmax'],V=own['V'],seconds=time.time()-self.start)
  self.history.append(row);np.save(self.out/'latest.npy',X);np.save(self.out/'latest_params.npy',z);(self.out/'history.json').write_text(json.dumps(self.history,indent=2))
  if np.linalg.norm(m)<1e-7 and ine.min()>-1e-8 and f<self.best:
   self.best=f;np.save(self.out/'best.npy',X);np.save(self.out/'best_params.npy',z);(self.out/'best.json').write_text(json.dumps(row,indent=2))
  if own['Pmax']<1e-12 and own['Qmax']<1e-12:
   np.save(self.out/f'potential_{len(self.history)}.npy',X);print('THALES_POTENTIAL_REQUIRES_EXACT_AUDIT',row,flush=True)
  if len(self.history)%10==0:print('THALES_STEP',row,flush=True)
 def run(self,maxiter,stepbound=1.,restart=None):
  z0=self.c.z0 if restart is None else np.load(restart);bounds=[]
  for k in range(0,len(z0),3):bounds.extend([(-stepbound,stepbound),(-stepbound,stepbound),(-20.,27.)])
  cons=[dict(type='eq',fun=lambda z:self.calc(z)[2],jac=lambda z:self.calc(z)[3]),dict(type='ineq',fun=lambda z:self.calc(z)[4],jac=lambda z:self.calc(z)[5])]
  self.callback(z0)
  r=minimize(lambda z:self.calc(z)[:2],z0,jac=True,method='SLSQP',bounds=bounds,constraints=cons,callback=self.callback,options=dict(maxiter=maxiter,ftol=1e-11,disp=True))
  self.callback(r.x);(self.out/'termination.json').write_text(json.dumps(dict(message=r.message,success=bool(r.success),nit=r.nit,fun=float(r.fun)),indent=2));print('THALES_DONE',r.message,flush=True)

if __name__=='__main__':
 p=argparse.ArgumentParser();p.add_argument('input');p.add_argument('out');p.add_argument('--iterations',type=int,default=1200);p.add_argument('--eta',type=float,default=.02);p.add_argument('--rho-margin',type=float,default=1e-11);p.add_argument('--restart');p.add_argument('--check',action='store_true');a=p.parse_args()
 X=np.load(a.input);X=geometry(X,False)['Z'];X/=np.max(np.linalg.norm(X,axis=1));c=Chart(X,1.-a.rho_margin);s=Search(c,a.out,a.eta)
 if a.check:
  rng=np.random.default_rng(4762);z=c.z0.copy();d=rng.normal(size=z.shape);d/=np.linalg.norm(d);f,J,m,Dm,ine,DI,_,_=s.calc(z)
  print('CHART_RECONSTRUCTION',np.max(abs(c.physical(z)[0]-X)))
  for h in [1e-4,1e-5,1e-6,1e-7]:
   v=s.calc(z+h*d);w=s.calc(z-h*d);print('GRAD',h,(v[0]-w[0])/(2*h),J@d,'mass',np.max(abs((v[2]-w[2])/(2*h)-Dm@d)),'interior',np.max(abs((v[4]-w[4])/(2*h)-DI@d)))
 else:s.run(a.iterations,restart=a.restart)
