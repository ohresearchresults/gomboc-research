"""Dual physical Thales chart: S1 at zero plus uniform primal centroid equality.
Q are physical halfspace rows Q_i.x<=1. This is not a free affine metric.
At most85 supplied supports implies E<=249 for any bounded3D endpoint.
"""
import argparse,json,time
from pathlib import Path
import numpy as np
from scipy.optimize import minimize,NonlinearConstraint,Bounds,BFGS
from thales_chart import Chart
from support_geometry import geometry,census
from persistence_birth import bars_loss

class Search:
 def __init__(self,c,out,eta):
  self.c=c;self.out=Path(out);self.out.mkdir(parents=True,exist_ok=False);self.eta=eta;self.last=None;self.calls=0;self.best=np.inf;self.history=[];self.start=time.time()
  np.savez(self.out/'chart.npz',Q0=c.X0,u0=c.u0,B=c.B,parent=c.parent,order=c.order,root=c.root,tetra=c.tetra,z0=c.z0,rhomax=c.rhomax)
 def containment(self,z):
  Q,DQ=self.c.physical(z);return self.c.constraints(Q,DQ,None)
 def calc(self,z):
  if self.last is not None and np.array_equal(z,self.last[0]):return self.last[1]
  self.calls+=1;Q,DQ=self.c.physical(z);g=geometry(Q);X=g['X'];D=DQ.reshape(3*self.c.n,-1);DX=np.einsum('ncp,pz->ncz',g['DX'],D)
  edges=np.array(sorted({tuple(sorted((i,j))) for f in g['faces'] for i,j in zip(f,f[1:]+f[:1])}))
  f,G,P=bars_loss(X,edges,self.eta);J=np.einsum('ic,icp->p',G,DX);mass=g['g'];Dmass=g['Dg']@D
  data=(f,J,mass,Dmass,Q,X,g,P)
  self.last=(z.copy(),data)
  if self.calls%100==0:print('DUAL_THALES_CALL',self.calls,'refP',max(P,default=0.),'mass',np.linalg.norm(mass),flush=True)
  return data
 def callback(self,z,state=None):
  f,J,m,Dm,Q,X,g,P=self.calc(z);inside=self.containment(z)[0]
  cl=census(g);edges=np.array(sorted({tuple(sorted((i,j))) for fc in g['faces'] for i,j in zip(fc,fc[1:]+fc[:1])}));ownP=bars_loss(g['Z'],edges,self.eta)[2]
  qe=np.unique(np.sort(np.concatenate([g['T'][:,[0,1]],g['T'][:,[1,2]],g['T'][:,[2,0]]]),axis=1),axis=0);H=Q/(1-Q@g['g'])[:,None];ownQ=bars_loss(H,qe,self.eta)[2]
  row=dict(it=len(self.history),calls=self.calls,loss=f,refP=max(P,default=0.),Pmax=max(ownP,default=0.),Qmax=max(ownQ,default=0.),mass_norm=float(np.linalg.norm(m)),inside=float(inside.min()),S=cl['S'],U=cl['U'],C=2*cl['E'],seconds=time.time()-self.start)
  self.history.append(row);np.save(self.out/'latest_Q.npy',Q);np.save(self.out/'latest_X.npy',X);np.save(self.out/'latest_params.npy',z);(self.out/'history.json').write_text(json.dumps(self.history,indent=2))
  if np.linalg.norm(m)<1e-7 and inside.min()>0 and f<self.best:
   self.best=f;np.save(self.out/'best_Q.npy',Q);np.save(self.out/'best_X.npy',X);np.save(self.out/'best_params.npy',z);(self.out/'best.json').write_text(json.dumps(row,indent=2))
  if cl['S']==cl['U']==1 and row['C']<500:
   np.save(self.out/f'potential_Q_{len(self.history)}.npy',Q);print('DUAL_THALES_POTENTIAL_REQUIRES_EXACT',row,flush=True)
  if len(self.history)%10==0:print('DUAL_THALES_STEP',row,flush=True)
 def run(self,iterations,method,restart=None):
  z0=self.c.z0 if restart is None else np.load(restart);lo=np.tile([-1.,-1.,-20.],len(z0)//3);hi=np.tile([1.,1.,27.],len(z0)//3)
  if method=='trust-constr':
   cons=[NonlinearConstraint(lambda z:self.calc(z)[2],0,0,jac=lambda z:self.calc(z)[3]),NonlinearConstraint(lambda z:self.containment(z)[0],0,np.inf,jac=lambda z:self.containment(z)[1],keep_feasible=True)]
   opt=dict(maxiter=iterations,gtol=1e-8,xtol=1e-11,initial_tr_radius=.02,initial_constr_penalty=10.,verbose=1)
  else:
   cons=[dict(type='eq',fun=lambda z:self.calc(z)[2],jac=lambda z:self.calc(z)[3]),dict(type='ineq',fun=lambda z:self.containment(z)[0],jac=lambda z:self.containment(z)[1])];opt=dict(maxiter=iterations,ftol=1e-10,disp=True)
  self.callback(z0)
  r=minimize(lambda z:self.calc(z)[:2],z0,jac=True,method=method,bounds=Bounds(lo,hi),constraints=cons,callback=self.callback,options=opt)
  self.callback(r.x);(self.out/'termination.json').write_text(json.dumps(dict(message=r.message,success=bool(r.success),nit=r.nit,fun=float(r.fun)),indent=2));print('DUAL_THALES_DONE',r.message,flush=True)

if __name__=='__main__':
 p=argparse.ArgumentParser();p.add_argument('input');p.add_argument('out');p.add_argument('--iterations',type=int,default=1500);p.add_argument('--eta',type=float,default=.01);p.add_argument('--rho-margin',type=float,default=1e-10);p.add_argument('--restart');p.add_argument('--method',choices=['SLSQP','trust-constr'],default='trust-constr');p.add_argument('--check',action='store_true');a=p.parse_args()
 Q=np.load(a.input);Q/=np.max(np.linalg.norm(Q,axis=1));c=Chart(Q,1-a.rho_margin);s=Search(c,a.out,a.eta)
 if a.check:
  z=c.z0;rng=np.random.default_rng(49001);d=rng.normal(size=z.shape);d/=np.linalg.norm(d);f,J,m,Dm,*_=s.calc(z)
  print('CHART_RECONSTRUCTION',np.max(abs(c.physical(z)[0]-Q)))
  for h in [1e-4,1e-5,1e-6,1e-7]:
   v=s.calc(z+h*d);w=s.calc(z-h*d);print('GRAD',h,(v[0]-w[0])/(2*h),J@d,'mass',np.max(abs((v[2]-w[2])/(2*h)-Dm@d)))
 else:s.run(a.iterations,a.method,a.restart)
