"""Finite whole-support persistence descent followed by strict own211 retraction.
All endpoints are floating nominations until a separate exact rational audit.
"""
import os
os.environ['OPENBLAS_NUM_THREADS']='1';os.environ['OMP_NUM_THREADS']='1'
import numpy as np,json,pathlib,time,argparse
from persistence_search import search
from soft_forest_polish import run as polish
from basin_scout import score
from geometry import halfspace_mesh,census

def run(input,out,cycles=30,iters=1500,side='Q'):
 out=pathlib.Path(out);out.mkdir(parents=True,exist_ok=True);Q=np.load(input)['Q'];hist=[];t0=time.time()
 nP,nQ=(2,1) if side=='P' else (1,2);label='121' if side=='P' else '211'
 for cycle in range(cycles):
  before=score(Q);parent=out/f'cycle{cycle:03d}';parent.mkdir(exist_ok=True);np.savez(parent/'initial.npz',Q=Q)
  print('CYCLE_START',cycle,before['S'],before['U'],max(before[side],default=0),before['E'],flush=True)
  try:search(Q,parent/'descent',iters=iters,apex=False,kind='log',seed=cycle)
  except Exception as e:(parent/'descent_error.txt').write_text(repr(e));print('DESCENT_EXCEPTION_PRESERVED',repr(e),flush=True)
  if (parent/'descent/NOMINATION.npz').exists():
   q=np.load(parent/'descent/NOMINATION.npz')['Q'];s=census(halfspace_mesh(q))
   if s['S']==s['U']==1:np.savez(out/'NOMINATION110.npz',Q=q);print('POTENTIAL_GOAL_REQUIRES_EXACT',flush=True);return
  if not (parent/'descent/best.npz').exists():break
  candidate=np.load(parent/'descent/best.npz')['Q'];accepted=False
  for level in range(6):
   mixed=Q+(candidate-Q)*2**-level;folder=parent/f'retract{level}'
   try:polish(mixed,folder,nP=nP,nQ=nQ,steps=100)
   except Exception as e:(parent/f'retract{level}_error.txt').write_text(repr(e));continue
   if (folder/'POTENTIAL_OWN110.npz').exists():
    np.savez(out/'NOMINATION110.npz',Q=np.load(folder/'POTENTIAL_OWN110.npz')['Q']);print('POTENTIAL_GOAL_REQUIRES_EXACT',flush=True);return
   if not (folder/'NOMINATION.npz').exists():continue
   fixed=np.load(folder/'NOMINATION.npz')['Q'];after=score(fixed)
   if after['S']==nQ and after['U']==nP and max(after[side],default=0)<max(before[side],default=0)-1e-8:
    Q=fixed;np.savez(out/f'latest-strict{label}.npz',Q=Q);accepted=True;row=dict(cycle=cycle,backtrack=level,seconds=time.time()-t0,**after);hist.append(row);(out/'history.json').write_text(json.dumps(hist,indent=2));print('STRICT_CYCLE_IMPROVEMENT',cycle,side,max(after[side]),'E',after['E'],'seconds',time.time()-t0,flush=True);break
  if not accepted:print('NO_QUALIFIED_IMPROVEMENT_THIS_CYCLE',cycle,flush=True);break
  if max(after[side],default=0)<.03 or cycle%5==4:
   folder=parent/'attempt110'
   try:polish(Q,folder,nP=1,nQ=1,steps=120)
   except Exception as e:(parent/'attempt110_error.txt').write_text(repr(e))
   if (folder/'NOMINATION.npz').exists():np.savez(out/'NOMINATION110.npz',Q=np.load(folder/'NOMINATION.npz')['Q']);print('POTENTIAL_GOAL_REQUIRES_EXACT',flush=True);return
if __name__=='__main__':
 ap=argparse.ArgumentParser();ap.add_argument('--input',required=True);ap.add_argument('--out',required=True);ap.add_argument('--cycles',type=int,default=30);ap.add_argument('--iters',type=int,default=1500);ap.add_argument('--side',choices=['P','Q'],default='Q');a=ap.parse_args();run(a.input,a.out,a.cycles,a.iters,a.side)
