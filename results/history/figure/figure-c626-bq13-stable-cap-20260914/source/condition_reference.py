"""Reference-chamber margin raising with a fixed actual filled centroid.
This deliberately preserves the measured nonzero mass defect; it is not centring.
"""
import json,sys,argparse,time
from pathlib import Path
import numpy as np
from scipy.linalg import svd
R=Path(__file__).resolve().parent;sys.path[:0]=[str(R/'parent/mechanism'),str(R/'parent/mechanism/parent_sources')]
from reference_atlas import ReferenceAtlas
from atlas_opt import Atlas
from minnorm_qp import solve
from numeric import mechanics
from repair626 import refs,rooted

def run(a):
 d=json.loads((a.source/'GENERATOR.json').read_text());fs=json.loads((a.source/'faces.json').read_text());m=ReferenceAtlas(d,fs);o=Atlas(json.loads((R/'BASIN/GENERATOR.json').read_text()),fs);m.reference=o.state(o.u0,False)['c'];m.uparent,m.sparent=refs();u=m.u0.copy();ss=m.state(u,False);cfix=ss['M']/ss['V'];floor=np.maximum(5e-8,np.minimum(1e-5,ss['vals']*.5));gf=np.maximum(1e-9,np.minimum(1e-6,ss['gaps']*.01));hist=[];out=a.out;out.mkdir(exist_ok=True,parents=True);t0=time.monotonic();goal=ss['vals'].min()*1.5
 def state(v):
  z=m.state(v);z['ac']=z['M']/z['V'];z['adc']=(z['dM']-z['ac'][:,None]*z['dV'][None,:])/z['V'];mat=np.r_[z['dq'].reshape(-1,m.np)/2,z['dP'].reshape(-1,m.np)];_,dd,Vt=svd(mat,full_matrices=False,check_finite=False);z['W']=Vt.T/np.maximum(dd,1e-9);return z
 def rows(z,goal):
  vi,qi=np.where((~m.inc)&(z['gaps']<.04));return np.r_[z['J'],m.gap_jac(z,vi,qi),z['ddet']]@z['W'],np.r_[np.maximum(floor,goal)*1.1-z['vals'],gf[vi,qi]-z['gaps'][vi,qi],1e-10-z['det']]
 for it in range(a.steps):
  s=state(u);v=float(s['vals'].min());m.uparent=s['cu'].argmax(1);m.sparent=s['cs'].argmax(1);rooted(m.uparent,m.Uroot);rooted(m.sparent,3);s=state(u);rec=dict(it=it,minref=float(s['vals'].min()),cgerror=float(np.linalg.norm(s['ac']-m.reference)),sec=time.monotonic()-t0);hist.append(rec);print(rec,flush=True);m.save(u,out/'GENERATOR.json');(out/'faces.json').write_text(json.dumps(fs,separators=(',',':')));(out/'history.json').write_text(json.dumps(hist,indent=2));
  if v>=a.goal:print('REFERENCE_MARGIN_TARGET',flush=True);break
  goal=min(a.goal,max(v*1.5,v+1e-7));A,b=rows(s,goal);E=s['adc']@s['W'];dd,why=solve(A,b,E,cfix-s['ac'],bound=.05,tol=2e-13,seconds=6,maxsteps=10000);print('QP',why,flush=True);good=False
  if dd is not None:
   for ls in range(8):
    lam=2.**-ls;gg=v+lam*(goal-v);un=u+lam*s['W']@dd
    for rp in range(18):
     if time.monotonic()-t0>a.seconds:break
     try:sn=state(un)
     except Exception:break
     if np.linalg.norm(sn['ac']-cfix)<1e-12 and np.min(sn['vals']-np.maximum(floor,gg))>-1e-12 and sn['gaps'][~m.inc].min()>1e-10 and sn['det'].min()>0:u=un;good=True;print('ACCEPT',ls,rp,flush=True);break
     AA,bb=rows(sn,gg);EE=sn['adc']@sn['W'];delta,why=solve(AA,bb,EE,cfix-sn['ac'],bound=.05,tol=2e-13,seconds=4,maxsteps=8000)
     if delta is None:break
     un+=sn['W']@delta
    if good or time.monotonic()-t0>a.seconds:break
  if not good or time.monotonic()-t0>a.seconds:break
 s=state(u);m.save(u,out/'GENERATOR.json');print('FINAL',mechanics(s['q'],fs,P=s['P'],tol=1e-13),flush=True)
if __name__=='__main__':
 p=argparse.ArgumentParser();p.add_argument('--source',type=Path,required=True);p.add_argument('--out',type=Path,required=True);p.add_argument('--goal',type=float,default=.001);p.add_argument('--steps',type=int,default=50);p.add_argument('--seconds',type=float,default=400);run(p.parse_args())
