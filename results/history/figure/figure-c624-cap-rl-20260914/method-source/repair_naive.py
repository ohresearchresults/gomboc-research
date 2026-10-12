"""Finite fixed-identity full own-centroid repair in a reconstructed contact chart."""
import json,sys,time,argparse
from pathlib import Path
import numpy as np
from scipy.linalg import svd
R=Path(__file__).resolve().parent;sys.path[:0]=[str(R/'parent/mechanism'),str(R/'parent/mechanism/parent_sources')]
from atlas_opt import Atlas
from numeric import mechanics
from minnorm_qp import solve

def run(a):
 src=Path(a.source);d=json.loads((src/'GENERATOR.json').read_text());fs=json.loads((src/'faces.json').read_text());m=Atlas(d,fs);u=m.u0.copy();s=m.state(u,False)
 # Chosen witnesses frozen; identity-specific positive floors fixed for the run.
 m.sparent=s['cs'].argmax(1);m.uparent=s['cu'].argmax(1)
 floor=np.maximum(a.goal,np.minimum(1e-5,s['vals']*.4));geom=np.maximum(1e-9,np.minimum(1e-6,s['gaps']*.01));out=Path(a.out);out.mkdir(parents=True,exist_ok=True);hist=[];t0=time.time()
 if a.initial:u=np.load(a.initial)['u']
 for k in range(a.steps):
  s=m.state(u);mat=np.r_[s['dq'].reshape(-1,m.np)/2,s['dP'].reshape(-1,m.np)];_,dd,Vt=svd(mat,full_matrices=False,check_finite=False);W=Vt.T/np.maximum(dd,1e-10)
  merit=float(np.linalg.norm(np.minimum(s['vals']-floor,0)));rec=dict(iteration=k,merit=merit,minexit=float(s['vals'].min()),bad=int((s['vals']<=0).sum()),mingap=float(s['gaps'][~m.inc].min()),sec=time.time()-t0);hist.append(rec);print(rec,flush=True)
  m.save(u,out/'LATEST.json');np.savez(out/'LATEST.npz',u=u);(out/'history.json').write_text(json.dumps(hist,indent=2))
  if np.min(s['vals']-floor)>-1e-12 and s['vals'].min()>0:print('NUMERICAL_OWN110_FIXED_REPAIR',flush=True);break
  vi,qi=np.where((~m.inc)&(s['gaps']<.04));A=np.r_[s['J'],m.gap_jac(s,vi,qi)]@W;b=np.r_[floor*1.1-s['vals'],geom[vi,qi]-s['gaps'][vi,qi]]
  step,why=solve(A,b,bound=a.trust,tol=2e-14,seconds=5,maxsteps=6000)
  if step is None:print('QP_FAILED',why,flush=True);break
  good=False
  for ls in range(15):
   uu=u+(2.**-ls)*W@step
   try:sn=m.state(uu,False)
   except Exception:continue
   nm=float(np.linalg.norm(np.minimum(sn['vals']-floor,0)))
   if sn['gaps'][~m.inc].min()>1e-10 and sn['det'].min()>1e-12 and sn['h'].min()>0 and nm<merit*(1-1e-4*2.**-ls):
    u=uu;good=True;print('STEP',ls,float(np.linalg.norm(step)),flush=True);break
  if not good:print('NO_DESCENT',flush=True);break
  if time.time()-t0>a.seconds:break
 s=m.state(u,False);m.save(u,out/'GENERATOR.json');(out/'faces.json').write_text(json.dumps(fs,separators=(',',':')));np.savez(out/'END.npz',u=u);report=mechanics(s['q'],fs,P=s['P'],tol=1e-13);(out/'NUMERICAL.json').write_text(json.dumps(report,indent=2));print('END',report,flush=True)
if __name__=='__main__':
 p=argparse.ArgumentParser();p.add_argument('--source',required=True);p.add_argument('--out',required=True);p.add_argument('--initial');p.add_argument('--goal',type=float,default=5e-10);p.add_argument('--trust',type=float,default=.03);p.add_argument('--seconds',type=float,default=28);p.add_argument('--steps',type=int,default=40);run(p.parse_args())
