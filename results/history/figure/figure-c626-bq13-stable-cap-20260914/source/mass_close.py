"""Repair real filled first moments at the fixed reference-centre chamber.
All inequalities retain fixed positive floors; no polar centroid is used.
"""
import sys,json,time,argparse
from pathlib import Path
import numpy as np
from scipy.linalg import svd
from reference_atlas import ReferenceAtlas
from atlas_opt import Atlas
sys.path.insert(0,str(Path(__file__).resolve().parent/"parent/mechanism"))
from minnorm_qp import solve
from repair626 import refs,rooted
from numeric import mechanics
R=Path(__file__).resolve().parent

def run(a):
 d=json.loads((a.source/'GENERATOR.json').read_text());fs=json.loads((a.source/'faces.json').read_text());m=ReferenceAtlas(d,fs);o=Atlas(json.loads((R/'BASIN/GENERATOR.json').read_text()),fs);m.reference=o.state(o.u0,False)['c'];m.uparent,m.sparent=refs();u=m.u0.copy();s=m.state(u,False);floor=np.maximum(5e-8,np.minimum(1e-5,s['vals']*.4));assert np.min(s['vals']-floor)>0
 gf=np.maximum(1e-9,np.minimum(1e-6,s['gaps']*.01));tf=np.maximum(1e-12,np.minimum(1e-8,s['det']*.01));out=a.out;out.mkdir(exist_ok=True,parents=True);hist=[];t0=time.monotonic();frac=.2
 def state(v,jac=True):
  z=m.state(v,jac);z['actual_c']=z['M']/z['V']
  if jac:
   z['actual_dc']=(z['dM']-z['actual_c'][:,None]*z['dV'][None,:])/z['V'];mat=np.r_[z['dq'].reshape(-1,m.np)/2,z['dP'].reshape(-1,m.np)];_,dd,Vt=svd(mat,full_matrices=False,check_finite=False);z['W']=Vt.T/np.maximum(dd,1e-9)
  return z
 def rows(z):
  vi,qi=np.where((~m.inc)&(z['gaps']<.04));return np.r_[z['J'],m.gap_jac(z,vi,qi),z['ddet']]@z['W'],np.r_[1.2*floor-z['vals'],gf[vi,qi]-z['gaps'][vi,qi],tf-z['det']]
 def valid(z,target):return np.max(abs(z['actual_c']-target))<1e-12 and np.min(z['vals']-floor)>-1e-12 and np.min(z['gaps'][~m.inc]-gf[~m.inc])>-1e-12 and z['det'].min()>0 and z['h'].min()>0
 for it in range(a.steps):
  s=state(u);c=s['actual_c'];err=float(np.linalg.norm(c-m.reference));rec=dict(iter=it,error=err,minref=float(s['vals'].min()),mingap=float(s['gaps'][~m.inc].min()),sec=time.monotonic()-t0);hist.append(rec);print(rec,flush=True);m.save(u,out/'GENERATOR.json');np.savez(out/'END.npz',u=u);(out/'faces.json').write_text(json.dumps(fs,separators=(',',':')));(out/'history.json').write_text(json.dumps(hist,indent=2))
  if err<1e-13 and valid(s,m.reference):print('ACTUAL_FILLED_MASS_CLOSURE_REACHED',flush=True);break
  goal=m.reference if err<1e-7 else c+frac*(m.reference-c);A,b=rows(s);E=s['actual_dc']@s['W'];dd,why=solve(A,b,E,goal-c,bound=.15,tol=2e-13,seconds=6,maxsteps=10000);print('QP',why,flush=True);good=False
  if dd is not None:
   for ls in range(9):
    lam=2.**-ls;target=c+lam*(goal-c);un=u+lam*s['W']@dd
    for rep in range(22):
     if time.monotonic()-t0>a.seconds:break
     try:sn=state(un)
     except Exception as ex:print('ERR',repr(ex),flush=True);break
     if valid(sn,target):u=un;good=True;print('ACCEPT',ls,rep,flush=True);frac=min(1.,frac*1.4) if ls==0 else frac*.7;break
     AA,bb=rows(sn);EE=sn['actual_dc']@sn['W'];ds,why=solve(AA,bb,EE,target-sn['actual_c'],bound=.15,tol=2e-13,seconds=4,maxsteps=8000)
     if ds is None:print('INNERFAIL',why,flush=True);break
     un+=sn['W']@ds
    if good or time.monotonic()-t0>a.seconds:break
  if not good:frac*=.35;print('REJECT',flush=True)
  if frac<1e-7 or time.monotonic()-t0>a.seconds:break
 s=state(u,False);m.save(u,out/'GENERATOR.json');rep=mechanics(s['q'],fs,P=s['P'],tol=1e-13);(out/'NUMERICAL.json').write_text(json.dumps(rep,indent=2));print('END',rep,flush=True)
if __name__=='__main__':
 p=argparse.ArgumentParser();p.add_argument('--source',type=Path,required=True);p.add_argument('--out',type=Path,required=True);p.add_argument('--steps',type=int,default=100);p.add_argument('--seconds',type=float,default=500);run(p.parse_args())
