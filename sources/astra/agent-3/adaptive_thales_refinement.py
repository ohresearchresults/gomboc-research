"""Repeated physical re-hulling, strict repair and replacement of lost controls.
At most84 submitted points, so true E<=246 and V+E+F<=494 at every trial.
Useful nonwinning states are retained as search inputs, never goal completion.
"""
import argparse,json,time,traceback
from pathlib import Path
import numpy as np
from vertex_geometry import geometry
from thales_refinement import add_points
from thales_chart import Chart,Search
from polish_211 import run as repair
from persistence_birth import evaluate

def run(source,out,rounds,seed):
 out=Path(out);out.mkdir(parents=True,exist_ok=False);X=np.load(source);np.save(out/'initial.npy',X);best=evaluate(X)[2]['Qmax'];history=[];start=time.time()
 for it in range(rounds):
  d=out/f'round{it:02d}';d.mkdir();g=geometry(X,False);X=g['Z'][g['vertices']];n=len(X)
  if n<84:
   Y,meta=add_points(X,84,seed+it);np.save(d/'added.npy',Y);(d/'addition.json').write_text(json.dumps(meta,indent=2));repair(d/'added.npy',d/'initial_repair',300,1e-6);p=d/'initial_repair/success.npy'
   if not p.exists():history.append(dict(round=it,result='added controls failed strict211 repair'));(out/'history.json').write_text(json.dumps(history,indent=2));continue
   Y=np.load(p)
  else:Y=X.copy()
  g=geometry(Y,False);Y=g['Z'][g['vertices']];Y/=np.max(np.linalg.norm(Y,axis=1));c=Chart(Y);eta=[.02,.006,.06,.002][it%4];s=Search(c,d/'search',eta)
  try:s.run(5000,stepbound=.7)
  except (ValueError,np.linalg.LinAlgError) as err:
   (d/'search_failure.json').write_text(json.dumps(dict(error=str(err),traceback=traceback.format_exc()),indent=2));print('ADAPTIVE_SEARCH_EXPLICIT_FAILURE',it,str(err),flush=True)
  p=s.out/'best.npy'
  if not p.exists():history.append(dict(round=it,result='no centroid-feasible endpoint'));(out/'history.json').write_text(json.dumps(history,indent=2));continue
  repair(p,d/'final_repair',400,1e-6);p=d/'final_repair/success.npy'
  if p.exists():
   Y=np.load(p);info=evaluate(Y)[2];row=dict(round=it,oldQ=best,Q=info['Qmax'],V=info['V'],path=str(p),eta=eta,result='strict211 numerical',seconds=time.time()-start)
   if info['Qmax']<best:
    X=Y;best=info['Qmax'];np.save(out/'best.npy',X);(out/'best.json').write_text(json.dumps(row,indent=2))
  else:row=dict(round=it,result='strict211 correction failed',eta=eta,seconds=time.time()-start)
  history.append(row);(out/'history.json').write_text(json.dumps(history,indent=2));print('ADAPTIVE_REFINEMENT',row,flush=True)
 print('ADAPTIVE_REFINEMENT_DONE',history[-1],flush=True)
if __name__=='__main__':
 p=argparse.ArgumentParser();p.add_argument('input');p.add_argument('out');p.add_argument('--rounds',type=int,default=20);p.add_argument('--seed',type=int,default=60100);a=p.parse_args();run(a.input,a.out,a.rounds,a.seed)
