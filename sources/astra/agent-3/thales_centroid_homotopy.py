"""Preserve reference110 while bringing the ACTUAL homogeneous centroid to0.
g(X)=(1-lambda)*g_initial; lambda=1 alone can qualify, after exact full audit.
Primal U1 uses a Thales chart; polar S1 uses full reference chord guards.
No point masses, transported densities, relaxed graph, or metric-only body.
"""
import argparse,json,time
from pathlib import Path
import numpy as np
from scipy.optimize import minimize
from thales_chart import Chart
from vertex_geometry import geometry
from support_geometry import escape

class Homotopy:
 def __init__(self,X,out,eps):
  self.c=Chart(X);self.out=Path(out);self.out.mkdir(exist_ok=False,parents=True);self.eps=eps;self.g0=geometry(X,False)['g'];self.scale=np.linalg.norm(self.g0);assert self.scale>0
  self.m=2*len(X)-4;self.last=None;self.calls=0;self.history=[];self.best=-np.inf;self.start=time.time();np.save(self.out/'initial.npy',X);(self.out/'construction.json').write_text(json.dumps(dict(g_initial=self.g0.tolist(),epsilon=eps,source='literal physical initial.npy; uniform density1',centroid_homotopy='g(X)=(1-lambda)*g_initial; lambda=1 required',parent=self.c.parent.tolist()),indent=2))
 def calc(self,w):
  if self.last is not None and np.array_equal(w,self.last[0]):return self.last[1]
  self.calls+=1;z=w[:-1];lam=w[-1];X,DX=self.c.physical(z);g=geometry(X);T=g['T'];H=g['H']/(1+g['H']@g['g'])[:,None];DH=np.linalg.solve(X[T],-np.einsum('nc,nacp->nap',H,DX[T]));Dg=g['Dg']@DX.reshape(3*self.c.n,-1)
  if not np.isfinite(H).all() or not np.isfinite(DH).all():raise ValueError('undefined reference polar in an infeasible trial; no census assigned')
  unique=np.sort(np.unique(H,axis=0,return_index=True)[1]);H=H[unique];DH=DH[unique];root=int(np.argmax(np.sum(H*H,axis=1)));v,_,J=escape(H,DH,angular=False);v[root]=1.;J[root]=0.;ref=np.ones(self.m);DJ=np.zeros((self.m,len(w)));ref[:len(v)]=v-self.eps;DJ[:len(v),:-1]=J
  cont,DC=self.c.constraints(X,DX,g);ine=np.r_[ref,cont];DI=np.vstack((DJ,np.column_stack((DC,np.zeros(len(cont))))));eq=(g['g']-(1-lam)*self.g0)/self.scale;DE=np.column_stack((Dg,self.g0))/self.scale
  info=dict(S=int(np.sum(escape(g['H'])[0]<0)),U=int(np.sum(escape(g['Z'])[0]<0)),reference_S=int(np.sum(escape(H)[0]<0)),reference_U=int(np.sum(escape(X)[0]<0)),lambda_value=float(lam),min_guard=float(ref.min()+self.eps),centroid=g['g'].tolist(),centroid_norm=float(np.linalg.norm(g['g'])),equality_error=float(np.linalg.norm(eq)),interior=float(cont.min()),V=len(g['vertices']))
  data=(eq,DE,ine,DI,X,info);self.last=(w.copy(),data)
  return data
 def callback(self,w):
  eq,DE,ine,DI,X,info=self.calc(w);info.update(it=len(self.history),calls=self.calls,seconds=time.time()-self.start);self.history.append(info);np.save(self.out/'latest.npy',X);np.save(self.out/'latest_params.npy',w);(self.out/'history.json').write_text(json.dumps(self.history,indent=2))
  if info['equality_error']<1e-7 and ine.min()>-self.eps*.1 and w[-1]>self.best:
   self.best=float(w[-1]);np.save(self.out/'best.npy',X);np.save(self.out/'best_params.npy',w);(self.out/'best.json').write_text(json.dumps(info,indent=2))
  if info['S']==info['U']==1:
   np.save(self.out/f'potential_{len(self.history)}.npy',X);(self.out/f'potential_{len(self.history)}.json').write_text(json.dumps(info,indent=2));print('HOMOTOPY_POTENTIAL_OWN110_REQUIRES_EXACT',info,flush=True)
  if len(self.history)%10==0:print('CENTROID_HOMOTOPY',info,flush=True)
 def run(self,iterations):
  w0=np.r_[self.c.z0,0.];bounds=[]
  for k in range(0,self.c.d,3):bounds.extend([(-1.,1.),(-1.,1.),(-20.,27.)])
  bounds.append((0.,1.));grad=np.r_[np.zeros(self.c.d),-1.];cons=[dict(type='eq',fun=lambda w:self.calc(w)[0],jac=lambda w:self.calc(w)[1]),dict(type='ineq',fun=lambda w:self.calc(w)[2],jac=lambda w:self.calc(w)[3])];self.callback(w0)
  r=minimize(lambda w:(-w[-1],grad),w0,jac=True,method='SLSQP',bounds=bounds,constraints=cons,callback=self.callback,options=dict(maxiter=iterations,ftol=1e-11,disp=True));self.callback(r.x);(self.out/'termination.json').write_text(json.dumps(dict(message=r.message,success=bool(r.success),nit=r.nit,lambda_value=float(r.x[-1])),indent=2));print('HOMOTOPY_DONE',r.message,'lambda',r.x[-1],flush=True)
if __name__=='__main__':
 p=argparse.ArgumentParser();p.add_argument('input');p.add_argument('out');p.add_argument('--epsilon',type=float,default=1e-8);p.add_argument('--iterations',type=int,default=3000);p.add_argument('--check',action='store_true');a=p.parse_args();X=np.load(a.input);X/=np.max(np.linalg.norm(X,axis=1));s=Homotopy(X,a.out,a.epsilon)
 if a.check:
  w=np.r_[s.c.z0,0.];rng=np.random.default_rng(8892);d=rng.normal(size=w.shape);d/=np.linalg.norm(d);eq,DE,c,DC,*_=s.calc(w)
  for h in [1e-5,1e-6,1e-7]:
   p1=s.calc(w+h*d);p2=s.calc(w-h*d);print('GRAD',h,'centroid',np.max(abs((p1[0]-p2[0])/(2*h)-DE@d)),'guards',np.max(abs((p1[2]-p2[2])/(2*h)-DC@d)))
 else:s.run(a.iterations)
