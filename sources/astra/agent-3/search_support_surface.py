"""Support-space counterpart of the surface-weighted acyclic own-mass search.
The physical polyhedron has at most n input support planes, so n<=85 implies C<=498.
"""
import os
os.environ['OPENBLAS_NUM_THREADS']='1';os.environ['OMP_NUM_THREADS']='1'
import numpy as np,json,time,argparse
from pathlib import Path
from scipy.optimize import minimize
from support_geometry import geometry,census
from search_surface import routes

def evaluate(Q,eps=1e-7,derivative=True):
 geo=geometry(Q,False);X=geo['X'];Z=geo['Z'];g=geo['g'];T=geo['T'];tri=geo['tris']
 qa,qb,qc=Q[T[:,0]],Q[T[:,1]],Q[T[:,2]];N=np.cross(qb-qa,qc-qa);A=np.linalg.norm(N,axis=1)*.5;AT=A.sum()
 lv,GZ,dv,pval=routes(Z,eps,A/AT)
 h=1-Q@g;H=Q/h[:,None];lh,GH,dh,qval=routes(H,eps,np.ones(len(Q))/len(Q));GQ=np.zeros_like(Q)
 if derivative:
  hdot=np.einsum('ij,ij->i',GH,Q)/h**2
  GQ=GH/h[:,None]+hdot[:,None]*g
  tg=-GZ.sum(axis=0)+np.sum(hdot[:,None]*Q,axis=0)
  a,b,c=X[tri[:,0]],X[tri[:,1]],X[tri[:,2]];d=np.einsum('ij,ij->i',a,np.cross(b,c));D=d.sum();s=(a+b+c-4*g)@tg;GX=GZ.copy()
  for k,cr in [(0,np.cross(b,c)),(1,np.cross(c,a)),(2,np.cross(a,b))]:np.add.at(GX,tri[:,k],(d[:,None]*tg+s[:,None]*cr)/(4*D))
  w=np.linalg.solve(np.swapaxes(Q[T],1,2),GX[...,None])[...,0];DQ=-w[:,:,None]*X[:,None,:];np.add.at(GQ,T.reshape(-1),DQ.reshape(-1,3))
  unit=N/(2*A)[:,None];gb=.5*np.cross(qc-qa,unit);gc=.5*np.cross(unit,qb-qa);coeff=(dv-lv)/AT
  for k,gg in [(0,-gb-gc),(1,gb),(2,gc)]:np.add.at(GQ,T[:,k],coeff[:,None]*gg)
 info=census(geo);info.update(loss=lv+lh,p_loss=lv,q_loss=lh,volume=float(geo['V']))
 return lv+lh,GQ,info,X

def run(Q,out,steps,eps):
 out=Path(out);out.mkdir(exist_ok=False,parents=True);np.save(out/'initial.npy',Q);best=1e100;calls=0;start=time.time()
 def fun(z):
  nonlocal calls,best
  calls+=1;qq=z.reshape(-1,3);v,G,info,X=evaluate(qq,eps)
  if v<best:
   best=v;np.save(out/'best.npy',qq);np.save(out/'best_vertices.npy',X);(out/'best.json').write_text(json.dumps(dict(info,calls=calls,elapsed=time.time()-start),indent=2)+'\n')
  if calls%500==0:print('SUPPORT_SURFACE',calls,info,flush=True)
  if info['S']==info['U']==1 and min(info['minV'],info['minF'])>1e-10:
   np.save(out/'potential.npy',qq);(out/'potential.json').write_text(json.dumps(info,indent=2));print('POTENTIAL_SUPPORT_SURFACE110',out,info,flush=True)
  return v,G.ravel()
 res=minimize(fun,Q.ravel(),jac=True,method='L-BFGS-B',options={'maxiter':steps,'maxfun':steps*6,'maxls':50,'maxcor':30,'ftol':1e-16,'gtol':1e-12})
 print('DONE_SUPPORT_SURFACE',out,res.message,json.load(open(out/'best.json')),flush=True)
 (out/'termination.json').write_text(json.dumps({'message':str(res.message),'nit':int(res.nit),'calls':calls},indent=2))
if __name__=='__main__':
 p=argparse.ArgumentParser();p.add_argument('input');p.add_argument('output');p.add_argument('--steps',type=int,default=10000);p.add_argument('--epsilon',type=float,default=1e-7);p.add_argument('--check',action='store_true');a=p.parse_args()
 if a.check:
  rng=np.random.default_rng(935);Q=rng.normal(size=(20,3));d=rng.normal(size=Q.shape);d/=np.linalg.norm(d);v,G,i,X=evaluate(Q)
  for h in [1e-4,1e-5,1e-6,1e-7]:print('GRAD_SUPPORT_SURFACE',h,(evaluate(Q+h*d,derivative=False)[0]-evaluate(Q-h*d,derivative=False)[0])/(2*h),np.sum(G*d))
 else:run(np.load(a.input),a.output,a.steps,a.epsilon)
