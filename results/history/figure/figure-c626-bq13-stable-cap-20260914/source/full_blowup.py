"""Regular blow-up continuation retaining BOTH physical escape identities.
For B->A use -dot(B-g,r)/(|B-g||r|), including its exact analytic derivative:
no cancellation in a vanishing chord. Final rational contraction is separately audited.
"""
import json,sys,time,argparse
from pathlib import Path
import numpy as np
from scipy.linalg import svd
from blowup_edge import Model
from atlas_opt import Atlas
from repair626 import rooted
from minnorm_qp import solve
R=Path(__file__).resolve().parent
class Full(Model):
 def __init__(self,d,f):
  self.ready=False;super().__init__(d,f,152,155);self.ready=True
  s=Atlas.state(self,self.u0,False);self.ps=s['cs'].argmax(1);self.pu=s['cu'].argmax(1);self.pu[self.bi]=self.ai;self.pu[self.ai]=63
  rooted(self.ps,3);rooted(self.pu,self.Uroot)
  self.ui=np.array([i for i in range(len(self.owners)) if i not in [self.bi,self.Uroot]])
  s=self.state(self.u0,False);self.floor=np.maximum(5e-8,np.minimum(1e-5,s['vals']*.4));assert np.min(s['vals']-self.floor)>0;self.geo0=s['gaps'].copy()
 def state(self,u,jac=True):
  if not self.ready:return super().state(u,jac)
  if not hasattr(self,'ps'):return Atlas.state(self,u,jac)
  self.sparent=self.ps;self.uparent=self.pu;s=Atlas.state(self,u,jac)
  r=np.zeros(3);dr=np.zeros((3,self.np));r[self.axis]=self.sgn
  for j,(i,k) in enumerate(self.free):
   if i==self.bb and k!=self.axis:r[k]=u[j]*self.scale[j];dr[k,j]=self.scale[j]
  z=s['P'][self.bi]-s['c'];zz=z@z;rr=r@r;den=np.sqrt(zz*rr);val=-(z@r)/den
  s['vals']=np.r_[s['vals'],val]
  if jac:
   dz=s['dP'][self.bi]-s['dc'];grad=-(z@dr+r@dz)/den-val*(z@dz/zz+r@dr/rr);s['J']=np.r_[s['J'],grad[None,:]]
  return s
 def rows(self,s):
  vi,qi=np.where(self.guard&(s['gaps']<.04));gf=np.maximum(1e-9,np.minimum(1e-6,self.geo0[vi,qi]*.01))
  return np.r_[s['J'],self.gap_jac(s,vi,qi),s['ddet'][~self.vanish]]@s['W'],np.r_[1.1*self.floor-s['vals'],gf-s['gaps'][vi,qi],1e-10-s['det'][~self.vanish]]
 def valid(self,s):return np.isfinite(s['vals']).all() and np.min(s['vals']-self.floor)>-1e-12 and s['gaps'][self.guard].min()>1e-10 and s['det'][~self.vanish].min()>1e-12 and s['h'].min()>0

def run(a):
 d=json.loads((R/'C628_WINNER/GENERATOR.json').read_text());fs=json.loads((R/'C628_WINNER/faces.json').read_text());m=Full(d,fs);u=m.u0.copy();out=a.out;out.mkdir(parents=True,exist_ok=True);row=np.zeros(m.np);row[m.epindex]=m.scale[m.epindex];frac=.05;hist=[];t0=time.monotonic()
 for it in range(a.steps):
  s=m.allstate(u);eps=m.epsilon(u);rec=dict(iter=it,epsilon=float(eps),minexit=float(s['vals'].min()),Bexit=float(s['vals'][-1]),mingap=float(s['gaps'][m.guard].min()),sec=time.monotonic()-t0);hist.append(rec);print(rec,flush=True);np.savez(out/'END.npz',u=u);(out/'history.json').write_text(json.dumps(hist,indent=2))
  if abs(eps)<1e-13 and m.valid(s):print('FULL110_BLOWUP_FINITE_CONTACT',flush=True);break
  target=0 if eps<1e-4 else eps*(1-frac);A,b=m.rows(s);E=(row@s['W'])[None,:];dd,why=solve(A,b,E,np.array([target-eps]),bound=.1,tol=2e-13,seconds=6,maxsteps=10000);print('QP',why,flush=True);good=False
  if dd is not None:
   for ls in range(8):
    lam=2.**-ls;goal=eps+lam*(target-eps);un=u+lam*s['W']@dd
    for rep in range(18):
     if time.monotonic()-t0>a.seconds:break
     try:sn=m.allstate(un)
     except Exception as ex:print('ERROR',repr(ex),flush=True);break
     if m.valid(sn):u=un;good=True;frac=min(.5,frac*1.3) if ls==0 else frac*.8;print('ACCEPT',ls,rep,flush=True);break
     AA,bb=m.rows(sn);EE=(row@sn['W'])[None,:];ds,why=solve(AA,bb,EE,np.array([goal-m.epsilon(un)]),bound=.1,tol=2e-13,seconds=4,maxsteps=8000)
     if ds is None:print('INNERFAIL',why,flush=True);break
     un+=sn['W']@ds
    if good or time.monotonic()-t0>a.seconds:break
  if not good:frac*=.4;print('REJECT',flush=True)
  if frac<1e-7 or time.monotonic()-t0>a.seconds:break
 np.savez(out/'END.npz',u=u);d,fs=m.endpoint(u);(out/'GENERATOR.json').write_text(json.dumps(d,sort_keys=True,separators=(',',':')));(out/'faces.json').write_text(json.dumps(fs,separators=(',',':')));print('FINAL_EPS',float(m.epsilon(u)),flush=True)
if __name__=='__main__':
 p=argparse.ArgumentParser();p.add_argument('--out',type=Path,required=True);p.add_argument('--steps',type=int,default=100);p.add_argument('--seconds',type=float,default=500);run(p.parse_args())
