"""Finite own-centroid homotopy of one nonroot escape, retaining all
healthy fixed positive identity floors and acyclic root-reaching parents.
All steps are numerical proposals; exact hull/mechanical audits are separate.
"""
import sys,json,time,argparse
from pathlib import Path
import numpy as np
from scipy.linalg import svd
sys.path[:0]=[str(Path(__file__).resolve().parent/'parent/mechanism'),str(Path(__file__).resolve().parent/'parent/mechanism/parent_sources')]
from atlas_opt import Atlas
from numeric import mechanics
from minnorm_qp import solve
from repair626 import rooted

def run(a):
 d=json.loads((a.source/'GENERATOR.json').read_text());fs=json.loads((a.source/'faces.json').read_text());m=Atlas(d,fs);u=m.u0.copy();s=m.state(u,False);m.sparent=s['cs'].argmax(1);m.uparent=s['cu'].argmax(1);m.uparent[a.vertex]=a.exit;rooted(m.uparent,m.Uroot);rooted(m.sparent,m.Sroot);s=m.state(u,False)
 idx=len(m.si)+int(np.flatnonzero(m.ui==a.vertex)[0]);healthy=np.arange(len(s['vals']))!=idx;floor=np.maximum(5e-8,np.minimum(1e-5,s['vals']*.4));floor[idx]=-np.inf;gf=np.maximum(1e-9,np.minimum(1e-6,s['gaps']*.01));tf=np.maximum(1e-12,np.minimum(1e-8,s['det']*.01))
 assert s['vals'][healthy].min()>0
 out=a.out;out.mkdir(parents=True,exist_ok=True);hist=[];t0=time.monotonic();frac=.02
 def state(v,jac=True):
  z=m.state(v,jac)
  if jac:
   mat=np.r_[z['dq'].reshape(-1,m.np)/2,z['dP'].reshape(-1,m.np)];_,dd,Vt=svd(mat,full_matrices=False,check_finite=False);z['W']=Vt.T/np.maximum(dd,1e-9)
  return z
 def rows(z,target):
  vi,qi=np.where((~m.inc)&(z['gaps']<.04));f=1.25*floor.copy();f[idx]=target
  return np.r_[z['J'],m.gap_jac(z,vi,qi),z['ddet']]@z['W'],np.r_[f-z['vals'],gf[vi,qi]-z['gaps'][vi,qi],tf-z['det']]
 def valid(z,target):return np.isfinite(z['vals']).all() and np.min(z['vals'][healthy]-floor[healthy])>-1e-12 and z['vals'][idx]>=target-1e-11 and np.min(z['gaps'][~m.inc]-gf[~m.inc])>-1e-12 and z['det'].min()>0 and z['h'].min()>0
 for it in range(a.steps):
  s=state(u);v=float(s['vals'][idx]);rec=dict(iter=it,value=v,minhealthy=float(s['vals'][healthy].min()),mingap=float(s['gaps'][~m.inc].min()),sec=time.monotonic()-t0);hist.append(rec);print(rec,flush=True);m.save(u,out/'GENERATOR.json');np.savez(out/'END.npz',u=u);(out/'faces.json').write_text(json.dumps(fs,separators=(',',':')));(out/'history.json').write_text(json.dumps(hist,indent=2))
  if v>=a.goal and valid(s,a.goal):print('GUARDED_CANCEL_NUMERICAL110',flush=True);break
  target=a.goal if v>-.0001 else v+min(.002,frac*(a.goal-v));A,b=rows(s,target);step,why=solve(A,b,bound=a.trust,tol=2e-13,seconds=6,maxsteps=9000);good=False;print('QP',why,flush=True)
  if step is not None:
   for ls in range(10):
    lam=2.**-ls;goal=v+lam*(target-v);un=u+lam*s['W']@step
    for rep in range(25):
     if time.monotonic()-t0>a.seconds:break
     try:sn=state(un)
     except Exception:break
     if valid(sn,goal):u=un;good=True;print('ACCEPT',ls,rep,flush=True);frac=min(.3,frac*1.3) if ls==0 else frac*.8;break
     AA,bb=rows(sn,goal);dd,why=solve(AA,bb,bound=a.trust,tol=2e-13,seconds=4,maxsteps=6000)
     if dd is None:print('INNERFAIL',ls,rep,why,flush=True);break
     un+=sn['W']@dd
    if good or time.monotonic()-t0>a.seconds:break
  if not good:frac*=.3;print('NO_ACCEPT',flush=True)
  if frac<1e-7 or time.monotonic()-t0>a.seconds:break
 s=m.state(u,False);m.save(u,out/'GENERATOR.json');np.savez(out/'END.npz',u=u);report=mechanics(s['q'],fs,P=s['P'],tol=1e-13);(out/'NUMERICAL.json').write_text(json.dumps(report,indent=2));(out/'FLOORS.json').write_text(json.dumps(dict(floors=floor.tolist(),p=m.uparent.tolist(),q=m.sparent.tolist())));print('FINAL',report,flush=True)
if __name__=='__main__':
 p=argparse.ArgumentParser();p.add_argument('--source',type=Path,required=True);p.add_argument('--out',type=Path,required=True);p.add_argument('--vertex',type=int,default=67);p.add_argument('--exit',type=int,default=63);p.add_argument('--goal',type=float,default=1e-6);p.add_argument('--trust',type=float,default=.1);p.add_argument('--steps',type=int,default=100);p.add_argument('--seconds',type=float,default=180);a=p.parse_args();run(a)
