"""Rotating-center homothetic polygon layers; actual convex hull and uniform mass.
Each ring is mu_i+r_i*regular_m_gon at height z_i. Endpoints are tips.
At most85 physical submitted points guarantee E<=249 even if layers retire.
"""
import os
os.environ['OPENBLAS_NUM_THREADS']='1';os.environ['OMP_NUM_THREADS']='1'
import numpy as np,json,argparse,time
from pathlib import Path
from scipy.optimize import minimize
from search_surface import evaluate

def build(params,m,z):
 p=params.reshape(-1,3);phi=2*np.pi*np.arange(m)/m;u=np.column_stack((np.cos(phi),np.sin(phi)));ringxy=p[:,:2,None]+p[:,2,None,None]*u.T[None,:,:]
 X=np.empty((len(p)*m+2,3));X[0]=[0,0,-1];X[-1]=[0,0,1];X[1:-1,:2]=np.transpose(ringxy,(0,2,1)).reshape(-1,2);X[1:-1,2]=np.repeat(z,m)
 return X,u

def run(m,L,beta,seed,steps,eps=1e-6):
 assert m*L+2<=85
 rng=np.random.default_rng(seed);z=np.linspace(-1,1,L+2)[1:-1];phase=1.5*np.pi*(z-z**3/3)
 p=np.column_stack((beta*(np.cos(phase)+1),beta*np.sin(phase),np.sqrt(1-z*z)))
 if seed:p[:,:2]+=rng.normal(size=(L,2))*.015;p[:,2]*=np.exp(rng.normal(size=L)*.02)
 out=Path(f'artifacts/layered/m{m}_l{L}_b{beta:g}_s{seed}');out.mkdir(exist_ok=False,parents=True);(out/'parameters.json').write_text(json.dumps({'m':m,'L':L,'beta':beta,'seed':seed,'z':z.tolist(),'epsilon':eps},indent=2));np.save(out/'initial_params.npy',p)
 calls=0;best=1e100;start=time.time()
 def fun(x):
  nonlocal calls,best
  calls+=1;X,u=build(x,m,z);v,G,info=evaluate(X,eps);g=G[1:-1].reshape(L,m,3);gp=np.column_stack((g[:,:,:2].sum(axis=1),np.einsum('imc,mc->i',g[:,:,:2],u)))
  if v<best:
   best=v;np.save(out/'best_params.npy',x.reshape(L,3));np.save(out/'best.npy',X);(out/'best.json').write_text(json.dumps(dict(info,calls=calls,elapsed=time.time()-start),indent=2)+'\n')
  if calls%1000==0:print('LAYERED',m,L,beta,seed,calls,info,flush=True)
  if info['S']==info['U']==1 and min(info['minV'],info['minF'])>1e-9:
   np.save(out/'potential_params.npy',x.reshape(L,3));np.save(out/'potential.npy',X);(out/'potential.json').write_text(json.dumps(info,indent=2));print('POTENTIAL_LAYERED110',out,info,flush=True)
  return v,gp.ravel()
 bounds=[b for i in range(L) for b in [(-2,2),(-2,2),(.02,3.)]]
 r=minimize(fun,p.ravel(),jac=True,method='L-BFGS-B',bounds=bounds,options={'maxiter':steps,'maxfun':steps*6,'maxls':40,'maxcor':30,'ftol':1e-16,'gtol':1e-11})
 print('DONE_LAYERED',m,L,beta,seed,str(r.message),json.load(open(out/'best.json')),flush=True)
 (out/'termination.json').write_text(json.dumps({'message':str(r.message),'nit':int(r.nit),'calls':calls},indent=2))
if __name__=='__main__':
 p=argparse.ArgumentParser();p.add_argument('--steps',type=int,default=4000);p.add_argument('--seed',type=int,default=0);p.add_argument('--trials',type=int,default=2);a=p.parse_args()
 for m,L in [(4,20),(6,13),(8,10)]:
  for beta in [.04,.15,.3]:
   for seed in range(a.seed,a.seed+a.trials):run(m,L,beta,seed,a.steps)
