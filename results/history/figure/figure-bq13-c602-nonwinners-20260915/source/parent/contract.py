"""Open the complete two-point disappearing basin, retain fixed positive floors
on all other identities, and close epsilon in the regular contact chart.
No claim about intermediate endpoint equilibrium counts is inferred from guards.
"""
import json,sys,time,argparse
from pathlib import Path
import numpy as np
from scipy.linalg import svd
from blowup_edge import Model
from atlas_opt import Atlas
from minnorm_qp import solve
from numeric import mechanics
R=Path(__file__).resolve().parent
class Basin(Model):
 def __init__(self,d,f,cp):
  self.ready=False;super().__init__(d,f,cp['a_node'],cp['b_node']);self.ui=np.array([i for i in range(len(self.owners)) if i not in [self.ai,self.bi,self.Uroot]])
  self.ready=True;self.u0=np.array([float.fromhex(x) for x in cp['u_hex']]);s=self.state(self.u0,False);self.floor=np.maximum(5e-8,np.minimum(1e-5,s['vals']*.5));assert np.min(s['vals']-self.floor)>0
  self.geo0=s['gaps'].copy()
 def state(self,u,jac=True):
  if not self.ready:return super().state(u,jac)
  for k in ['sparent','uparent']:
   if hasattr(self,k):delattr(self,k)
  return Atlas.state(self,u,jac)
 def valid(self,s):
  return np.isfinite(s['vals']).all() and np.min(s['vals']-self.floor)>-1e-12 and s['gaps'][self.guard].min()>1e-10 and s['det'][~self.vanish].min()>1e-12 and s['h'].min()>0

def run(a):
 d=json.loads((a.source/'GENERATOR.json').read_text());f=json.loads((a.source/'faces.json').read_text())
 if a.checkpoint:cp=json.loads(a.checkpoint.read_text())
 else:
  start=Model(d,f,a.an,a.bn);cp=dict(a_node=a.an,b_node=a.bn,u_hex=[float(v).hex() for v in start.u0])
 m=Basin(d,f,cp);u=m.u0.copy();out=a.out;out.mkdir(exist_ok=True,parents=True);t0=time.monotonic();hist=[];frac=.25
 if a.initial:u=np.load(a.initial)['u']
 (out/'fixed_floors.json').write_text(json.dumps(m.floor.tolist()))
 row=np.zeros(m.np);row[m.epindex]=m.scale[m.epindex]
 for it in range(a.steps):
  s=m.allstate(u);eps=m.epsilon(u);rec=dict(it=it,epsilon=float(eps),minexit=float(s['vals'].min()),mingap=float(s['gaps'][m.guard].min()),sec=time.monotonic()-t0);hist.append(rec);print(rec,flush=True);np.savez(out/'END.npz',u=u);(out/'history.json').write_text(json.dumps(hist,indent=2))
  if abs(eps)<1e-13 and m.valid(s):print('BASIN_FINITE_CONTACT_REACHED',flush=True);break
  target=0 if eps<1e-4 else eps*(1-frac);A,b=m.rows(s);E=(row@s['W'])[None,:]
  d,why=solve(A,b,E,np.array([target-eps]),bound=.1,tol=2e-13,seconds=10,maxsteps=10000);good=False
  print('PRED',why,flush=True)
  if d is not None:
   for ls in range(9):
    lam=2.**-ls;goal=eps+lam*(target-eps);un=u+lam*s['W']@d
    for rep in range(20):
     if time.monotonic()-t0>a.seconds:break
     try:sn=m.allstate(un)
     except Exception as ex:print('ERR',repr(ex),flush=True);break
     if m.valid(sn):u=un;good=True;print('ACCEPT',ls,rep,flush=True);frac=min(.5,frac*1.3) if ls==0 else frac*.7;break
     A,b=m.rows(sn);E=(row@sn['W'])[None,:];dd,why=solve(A,b,E,np.array([goal-m.epsilon(un)]),bound=.1,tol=2e-13,seconds=5,maxsteps=10000)
     if dd is None:print('CORRFAIL',ls,rep,why,flush=True);break
     un+=sn['W']@dd
    if good or time.monotonic()-t0>a.seconds:break
  if not good:frac*=.4;print('REJECT',flush=True)
  if frac<1e-6 or time.monotonic()-t0>a.seconds:break
 np.savez(out/'END.npz',u=u);d,f=m.endpoint(u);(out/'GENERATOR.json').write_text(json.dumps(d,sort_keys=True,separators=(',',':')));(out/'faces.json').write_text(json.dumps(f,separators=(',',':')));print('FINAL_EPS',m.epsilon(u),flush=True)
if __name__=='__main__':
 p=argparse.ArgumentParser();p.add_argument('--out',type=Path,required=True);p.add_argument('--steps',type=int,default=80);p.add_argument('--seconds',type=float,default=500);p.add_argument('--initial');p.add_argument('--checkpoint',type=Path);p.add_argument('--source',type=Path,default=R/'C628_WINNER');p.add_argument('--an',type=int,required=True);p.add_argument('--bn',type=int,required=True);run(p.parse_args())
