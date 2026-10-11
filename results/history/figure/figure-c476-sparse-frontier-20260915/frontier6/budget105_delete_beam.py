"""Finite primal deletion beam from exactly specified C486/R12 affine image.
At <=105 remaining points, E<=309 follows without any coplanar grouping.
Usage: OPENBLAS_NUM_THREADS=1 python budget105_delete_beam.py R12_A OUT
"""
import json,sys,hashlib,os
from pathlib import Path
import numpy as np,scipy
from scipy.spatial import QhullError
import primal334_delete_screen as base
assert __debug__
WIDTH=3;STEPS=14;ROOT=79
B=lambda o:json.dumps(o,sort_keys=True,separators=(',',':')).encode()
def score(r):return(r['S']+r['U'],max(r['S'],r['U']),r['cost'],r['E_est'])
def main(src,out):
 m=base.Model(src);keep=[i for i in range(118) if i not in [42,63,83]];initial=m.evaluate(keep)
 assert(initial['S'],initial['U'],initial['E_est'])==(2,2,238)
 beam=[initial];levels=[];trials=[];best=None
 for step in range(STEPS):
  candidates={}
  for parent_idx,parent in enumerate(beam):
   kk=parent['exposed_original_R12_labels']
   for removed in kk:
    if removed==ROOT:continue
    cut=tuple(i for i in kk if i!=removed)
    if cut in candidates:continue
    try:
     r=m.evaluate(list(cut));r.update(step=step,parent=parent_idx,deleted=removed)
     if r['nearU'] or r['nearS']:raise ValueError('numerically unresolved equilibrium sign')
     candidates[cut]=r
     trials.append({k:r[k] for k in ['step','parent','deleted','S','U','V_est','F_est','E_est','cost','keep_original_R12_labels']})
    except(QhullError,ValueError,AssertionError,np.linalg.LinAlgError)as e:
     trials.append(dict(step=step,parent=parent_idx,deleted=removed,error=type(e).__name__))
  if not candidates:break
  beam=sorted(candidates.values(),key=score)[:WIDTH];levels.append(beam)
  qualified=[r for r in beam if r['V_est']<=105]
  if qualified:
   win=min(qualified,key=score)
   if best is None or score(win)<score(best):best=win
  r=beam[0];print('BEAM105',step,'S/U',r['S'],r['U'],'V',r['V_est'],'E_est',r['E_est'],'cost',r['cost'],flush=True)
  report=dict(status='NUMERICAL_DELETION_BEAM_PROPOSALS_ONLY',source_sha256=m and base.aff.SOURCES['A.json'],initial=initial,beam_width=WIDTH,steps_requested=STEPS,protected_original_R12_root=ROOT,numpy=np.__version__,scipy=scipy.__version__,openblas_threads=os.environ.get('OPENBLAS_NUM_THREADS'),levels=levels,best_vertex_budget_candidate=best,trials=trials)
  out.write_bytes(B(report))
  if r['S']==r['U']==1 and r['E_est']<=310:print('BUDGET105_NUMERICAL110_NEEDS_EXACT_GATE',flush=True);break
 print('BUDGET105_DELETE_BEAM_TERMINAL',len(levels),len(trials),hashlib.sha256(out.read_bytes()).hexdigest(),flush=True)
if __name__=='__main__':main(*map(Path,sys.argv[1:]))
