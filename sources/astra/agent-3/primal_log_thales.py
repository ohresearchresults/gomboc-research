"""Primal Thales chart with log-rho and a physical-coordinate metric.
Own uniform-centroid projection is explicit and nonlinear. Inspired by peer1's
dual_thales.py mass-projection/conditioning method, applied to physical vertices.
"""
import argparse,json,time
from pathlib import Path
import numpy as np
from scipy.linalg import svd
from scipy.optimize import linprog
from thales_chart import Chart as LogisticChart
from vertex_geometry import geometry
from support_geometry import escape
from persistence_birth import bars_loss

class Chart(LogisticChart):
 def __init__(self,X):
  super().__init__(X,1.-1e-14)
  for i in self.nonroot:self.z0[self.index[i]+2]=np.log(np.dot(X[i],X[i])/np.dot(X[i],X[self.parent[i]]))
 def physical(self,z):
  if np.max(z[2::3])>=-1e-13 or np.min(z[2::3])<-30:raise ValueError('outside strict log-rho chart')
  X=np.zeros_like(self.X0);DX=np.zeros((self.n,3,self.d));X[self.root]=self.X0[self.root]
  for i in self.nonroot:
   k=self.index[i];p=self.parent[i];u=self.u0[i]+self.B[i]@z[k:k+2];uu=u@u;rho=np.exp(z[k+2]);s=u@X[p]/uu;X[i]=rho*s*u;DX[i]=(rho*np.outer(u,u)/uu)@DX[p];Ju=rho*(s*np.eye(3)+np.outer(u,X[p])/uu-2*s*np.outer(u,u)/uu);DX[i,:,k:k+2]+=Ju@self.B[i];DX[i,:,k+2]+=X[i]
  return X,DX

def evaluate(c,z,eta):
 X,DX=c.physical(z);inside,DI=c.constraints(X,DX,None)
 if min(inside)<0:raise ValueError('reference interior carrier lost')
 g=geometry(X);T=g['T'];Dg=g['Dg']@DX.reshape(3*c.n,-1);DH=np.einsum('fcp,pz->fcz',g['DH'],DX.reshape(3*c.n,-1));owners={}
 for f,t in enumerate(T):
  for i,j in zip(t,np.roll(t,-1)):owners.setdefault(tuple(sorted((i,j))),[]).append(f)
 qe=np.array(list(owners.values()));loss,G,Q=bars_loss(g['H'],qe,eta);grad=np.einsum('fc,fcp->p',G,DH);S=int(np.sum(escape(g['H'])[0]<0));U=int(np.sum(escape(g['Z'])[0]<0))
 return dict(X=X,DX=DX,H=g['H'],DH=DH,g=g['g'],Dg=Dg,inside=inside,DI=DI,loss=loss,gradient=grad,Q=Q,S=S,U=U,vertices=g['vertices'])
def metric(e):
 sx=np.sqrt(np.mean(e['X']**2));sh=np.sqrt(np.mean(e['H']**2));M=np.vstack((e['DX'].reshape(-1,e['DX'].shape[-1])/sx,e['DH'].reshape(-1,e['DH'].shape[-1])/sh));_,v,V=svd(M,full_matrices=False,check_finite=False)
 if min(v)<1e-14:raise ValueError('singular physical chart metric')
 return V.T/v,sx
def project(c,z,eta):
 for _ in range(14):
  e=evaluate(c,z,eta)
  if np.linalg.norm(e['g'])<1e-14:return z,e
  W,sx=metric(e);A=e['Dg']@W/sx;dz=-W@A.T@np.linalg.solve(A@A.T,e['g']/sx);ok=False
  for j in range(15):
   zz=z+dz*2.**-j
   try:ee=evaluate(c,zz,eta)
   except (ValueError,np.linalg.LinAlgError):continue
   if np.linalg.norm(ee['g'])<np.linalg.norm(e['g'])*(1-1e-5):z=zz;ok=True;break
  if not ok:raise ValueError('nonlinear actual-centroid projection stalled')
 raise ValueError('actual-centroid projection incomplete')
def run(source,out,steps,eta,constrained_projection=False):
 out=Path(out);out.mkdir(parents=True,exist_ok=False);g=geometry(np.load(source),False);X=g['Z'][g['vertices']];X/=np.max(np.linalg.norm(X,axis=1));c=Chart(X);z=c.z0.copy();hist=[];best=np.inf;trust=.03;start=time.time();np.save(out/'initial.npy',X)
 projection=project
 if constrained_projection:
  from constrained_mass_projection import project as projection
 (out/'projection.json').write_text(json.dumps(dict(constrained_projection=constrained_projection,source=str(source)),indent=2))
 for it in range(steps):
  e=evaluate(c,z,eta);row=dict(it=it,loss=e['loss'],Qmax=max(e['Q'],default=0.),bars=len(e['Q']),mass_norm=float(np.linalg.norm(e['g'])),S=e['S'],U=e['U'],vertices=len(e['vertices']),trust=trust,seconds=time.time()-start);hist.append(row);np.save(out/'latest.npy',e['X']);(out/'history.json').write_text(json.dumps(hist,indent=2))
  if it%10==0:print('LOG_THALES',row,flush=True)
  if e['S']==e['U']==1:
   np.save(out/'potential.npy',e['X']);print('LOG_THALES_POTENTIAL_REQUIRES_EXACT',row,flush=True)
   from goal_nomination import preserve
   preserve(e['X'],out/'exact_goal_nomination','actual own S1U1 in the homogeneous centroid-constrained Thales flow')
   return
  if e['loss']<best and np.linalg.norm(e['g'])<1e-10:
   best=e['loss'];np.save(out/'best.npy',e['X']);(out/'best.json').write_text(json.dumps(row,indent=2))
  W,sx=metric(e);d=len(z);rad=np.arange(2,d,3);A=np.vstack((-e['DI']@W,W[rad],-W[rad]));b=np.r_[e['inside']*.8,-1e-10-z[rad],z[rad]+25];mass=e['Dg']@W/sx;bound=trust/np.sqrt(d)
  sol=linprog(e['gradient']@W,A_ub=A,b_ub=b,A_eq=mass,b_eq=-e['g']/sx,bounds=[(-bound,bound)]*d,method='highs',options={'primal_feasibility_tolerance':1e-10,'dual_feasibility_tolerance':1e-10})
  if not sol.success:trust*=.5;continue
  dz=W@sol.x;ok=False
  for j in range(15):
   try:zz,ee=projection(c,z+dz*2.**-j,eta)
   except (ValueError,np.linalg.LinAlgError):continue
   if ee['U']==1 and ee['loss']<e['loss']-max(1e-12,abs(e['loss'])*1e-9):z=zz;ok=True;break
  if ok and j==0:trust=min(.25,trust*1.25)
  if not ok:trust*=.4
  if trust<1e-8:break
  if ok and it%20==19:
   X=ee['X'][ee['vertices']];c=Chart(X);z=c.z0.copy();(out/f'rechart{it}.json').write_text(json.dumps(dict(parent=c.parent.tolist(),root=c.root,tetra=c.tetra.tolist())))
 print('LOG_THALES_DONE',out,hist[-1],flush=True)
if __name__=='__main__':
 p=argparse.ArgumentParser();p.add_argument('input');p.add_argument('out');p.add_argument('--steps',type=int,default=700);p.add_argument('--eta',type=float,default=.01);p.add_argument('--check',action='store_true');p.add_argument('--constrained-projection',action='store_true');a=p.parse_args()
 if a.check:
  X=geometry(np.load(a.input),False)['Z'];c=Chart(X);z=c.z0;d=np.random.default_rng(9141).normal(size=z.shape);d/=np.linalg.norm(d);e=evaluate(c,z,a.eta)
  for h in [1e-8,1e-9,1e-10]:
   p1=evaluate(c,z+h*d,a.eta);p2=evaluate(c,z-h*d,a.eta);print('GRAD',h,(p1['loss']-p2['loss'])/(2*h),e['gradient']@d,'mass',np.max(abs((p1['g']-p2['g'])/(2*h)-e['Dg']@d)))
 else:run(a.input,a.out,a.steps,a.eta,a.constrained_projection)
