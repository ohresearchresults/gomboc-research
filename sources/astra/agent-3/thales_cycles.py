"""Rebuild positive-escape charts at strictly retracted physical endpoints."""
import argparse,json,time,traceback
from pathlib import Path
import numpy as np
from thales_chart import Chart,Search
from vertex_geometry import geometry
from polish_211 import run as polish
from persistence_birth import evaluate

def run(source,out,rounds):
 out=Path(out);out.mkdir(parents=True,exist_ok=False);X=np.load(source);best=evaluate(X)[2]['Qmax'];np.save(out/'initial.npy',X);rows=[]
 for it in range(rounds):
  g=geometry(X,False);X=g['Z'][g['vertices']];X/=np.max(np.linalg.norm(X,axis=1));eta=[.02,.1,.005,.05][it%4]
  c=Chart(X);s=Search(c,out/f'cycle{it:02d}',eta);s.run(2400,stepbound=1.)
  p=s.out/'best.npy'
  if not p.exists():rows.append(dict(cycle=it,status='no centroid-feasible nominated endpoint'));continue
  pp=s.out/'polish';polish(p,pp,300,1e-6)
  if (pp/'success.npy').exists():
   Y=np.load(pp/'success.npy');inf=evaluate(Y)[2];val=inf['Qmax'];row=dict(cycle=it,Q=val,oldQ=best,status='strict211 numerical',path=str(pp/'success.npy'))
   if val<best:
    X=Y;best=val;np.save(out/'best.npy',X);(out/'best.json').write_text(json.dumps(row,indent=2))
  else:row=dict(cycle=it,status='strict211 retraction failed',path=str(pp))
  rows.append(row);(out/'cycles.json').write_text(json.dumps(rows,indent=2));print('THALES_CYCLE',row,flush=True)
 print('THALES_CYCLES_DONE',rows[-1],flush=True)
if __name__=='__main__':
 p=argparse.ArgumentParser();p.add_argument('input');p.add_argument('out');p.add_argument('--rounds',type=int,default=12);a=p.parse_args();run(a.input,a.out,a.rounds)
