"""Sequential actual apex contact creation plus strict homogeneous own211 repair."""
import os
os.environ['OPENBLAS_NUM_THREADS']='1';os.environ['OMP_NUM_THREADS']='1'
import numpy as np,json,pathlib,time,argparse
from soft_forest_polish import run as polish
from basin_scout import score
from geometry import halfspace_mesh

def run(input,out,maxk=40):
 out=pathlib.Path(out);out.mkdir(parents=True,exist_ok=True);Q=np.load(input)['Q'];hist=[];t0=time.time()
 for stage in range(maxk):
  fixed=np.flatnonzero(np.isclose(Q[:,2],1,atol=1e-12,rtol=0));k=len(fixed);before=score(Q)
  if k>=maxk:break
  m=halfspace_mesh(Q);candidates=[int(i) for i in np.argsort(-Q[:,2]) if i in m['active'] and i not in fixed][:6];accepted=False
  print('APEX_STAGE',k,'E',before['E'],'Q',max(before['Q']),flush=True)
  for candidate in candidates:
   trial=Q.copy();trial[candidate,2]=1;folder=out/f'k{k+1:02d}-row{candidate}';folder.mkdir(exist_ok=True);np.savez(folder/'initial.npz',Q=trial)
   try:polish(trial,folder/'repair',nP=1,nQ=2,steps=160,apex=True)
   except Exception as e:(folder/'error.txt').write_text(repr(e));continue
   if not (folder/'repair/NOMINATION.npz').exists():continue
   new=np.load(folder/'repair/NOMINATION.npz')['Q'];after=score(new)
   if after['S']==2 and after['U']==1 and after['E']<before['E'] and max(after['Q'])<.22:
    Q=new;accepted=True;row=dict(concurrent=k+1,changed_row=candidate,source=str(folder/'repair/NOMINATION.npz'),seconds=time.time()-t0,**after);hist.append(row);(out/'history.json').write_text(json.dumps(hist,indent=2));np.savez(out/'latest.npz',Q=Q);print('APEX_STRICT_SAVING',k+1,'E',after['E'],'F',after['F'],'Q',max(after['Q']),'seconds',time.time()-t0,flush=True);break
  if not accepted:print('APEX_STAGE_UNRESOLVED',k,flush=True);break
if __name__=='__main__':
 ap=argparse.ArgumentParser();ap.add_argument('--input',required=True);ap.add_argument('--out',required=True);ap.add_argument('--maxk',type=int,default=40);a=ap.parse_args();run(a.input,a.out,a.maxk)
