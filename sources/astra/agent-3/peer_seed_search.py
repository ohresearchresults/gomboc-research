"""Free physical-vertex continuation of copied complete peer seed coordinates.
Self-polarity is a property of the supplied starting data only, not a constraint
or an acceptance claim in these independent own-mass computations.
"""
import os
os.environ['OPENBLAS_NUM_THREADS']='1';os.environ['OMP_NUM_THREADS']='1'
import numpy as np,json,time
from pathlib import Path
from scipy.optimize import minimize
from persistence_birth import evaluate
from search_vertices import evaluate as census

def run(source,seed):
 X=np.load(source)['X'].copy();rng=np.random.default_rng(seed)
 if seed:X+=rng.normal(size=X.shape)*.002
 out=Path(f'artifacts/peer_seed_search/{Path(source).stem}_s{seed}');out.mkdir(exist_ok=False,parents=True);np.save(out/'initial.npy',X);(out/'input.json').write_text(json.dumps({'source':source,'seed':seed,'noise_std':.002 if seed else 0},indent=2));calls=0;start=time.time()
 for stage,eta in enumerate([.03,.003,.0003]):
  folder=out/f'stage{stage}';folder.mkdir();best=1e100
  def fun(z):
   nonlocal calls,best
   calls+=1;x=z.reshape(-1,3);v,G,info=evaluate(x,eta)
   if v<best:
    best=v;np.save(folder/'best.npy',x);(folder/'best.json').write_text(json.dumps(dict(info,calls=calls,elapsed=time.time()-start),indent=2))
   if max(info['Pmax'],info['Qmax'])<1e-11:
    np.save(out/'potential.npy',x);(out/'potential.json').write_text(json.dumps(info,indent=2));print('POTENTIAL_PEER_SEED110',out,info,flush=True)
   return v,G.ravel()
  r=minimize(fun,X.ravel(),jac=True,method='L-BFGS-B',options={'maxiter':10000,'maxfun':60000,'maxls':50,'maxcor':35,'ftol':1e-16,'gtol':1e-11});X=np.load(folder/'best.npy');info=json.load(open(folder/'best.json'));ci=census(X)[2];print('PEER_SEED_STAGE',out,stage,r.message,{'Pmax':info['Pmax'],'Qmax':info['Qmax'],'S':ci['S'],'U':ci['U'],'V':ci['V'],'E':ci['E']},flush=True)
for source in ['sources/peer_selfpolar/opt39_final.npz','sources/peer_selfpolar/round17.npz']:
 for seed in [0,38001]:run(source,seed)
