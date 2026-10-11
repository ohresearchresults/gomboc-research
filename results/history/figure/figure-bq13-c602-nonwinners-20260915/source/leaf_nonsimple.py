"""Regular leaf-support contact, coupled to actual filled mass.
A one-coordinate gap parameter is eliminated at a finite exact endpoint.
"""
import sys,json,argparse,itertools
from pathlib import Path
import numpy as np
from scipy.linalg import svd
R=Path(__file__).resolve().parent
sys.path[:0]=[str(R/'parent/parent/mechanism'),str(R/'parent/parent/mechanism/parent_sources')]
from atlas_opt import Atlas
from numeric import recover,snapped,mechanics
from minnorm_qp import solve

def dump(p,x):p.write_text(json.dumps(x,sort_keys=True,separators=(',',':')))
class Leaf(Atlas):
 def __init__(self,d,fs,keep=26,drop=19,moved=113,release=False):
  self.ready=False;super().__init__(d,fs);self.keep=keep;self.drop=drop;self.moved=moved
  assert not any(moved in deps for i,deps,ax in d['plan'])
  assert next(t for t in d['plan'] if t[0]==moved)[1]==[]
  self.full_supports=np.array(self.owners[keep]); xx=recover(d)
  self.supports=np.array(max(itertools.combinations(self.owners[keep],3),key=lambda ids:abs(np.linalg.det(xx[list(ids)]))))
  assert set(self.owners[drop])-set(self.owners[keep])=={moved}
  X=recover(d);p=np.linalg.solve(X[self.supports],np.ones(3));self.axis=int(np.argmax(abs(p)))
  self.epindex=next(j for j,(i,k) in enumerate(self.free) if i==moved and k==self.axis)
  delta=1-X[moved]@p;self.u0[self.epindex]=delta/self.scale[self.epindex];self.ready=True
  self.guard=~self.inc.copy();self.guard[drop,self.full_supports]=False;self.guard[keep,moved]=False
  self.vanish=np.array([keep in t and drop in t for t in self.tri])
  if release:self.ui=np.array([i for i in self.ui if i not in [keep,drop]])
  s=self.state(self.u0,False);self.floor=np.maximum(5e-8,np.minimum(1e-5,s['vals']*.5));assert np.all(s['vals']>self.floor)
  self.geofloor=np.maximum(1e-9,np.minimum(1e-6,s['gaps']*.01));self.release=release
 def chart(self,u,jac=True):
  if not self.ready:return super().chart(u,jac)
  if jac:X,DX=super().chart(u,True)
  else:X=super().chart(u,False)
  rows=self.supports;p=np.linalg.solve(X[rows],np.ones(3));k=self.axis;i=self.moved
  eps=u[self.epindex]*self.scale[self.epindex];rest=[j for j in range(3) if j!=k]
  X[i,k]=(1-eps-X[i,rest]@p[rest])/p[k]
  if jac:
   dp=np.linalg.solve(X[rows],-np.einsum('rcp,c->rp',DX[rows],p))
   deps=np.zeros(self.np);deps[self.epindex]=self.scale[self.epindex]
   DX[i,k]=(-deps-X[i]@dp-p[rest]@DX[i,rest])/p[k]
   return X,DX
  return X
 def epsilon(self,u):return u[self.epindex]*self.scale[self.epindex]
 def allstate(self,u):
  s=self.state(u);mat=np.r_[s['dq'].reshape(-1,self.np)/2,s['dP'].reshape(-1,self.np)];_,v,vt=svd(mat,full_matrices=False,check_finite=False);s['W']=vt.T/np.maximum(v,1e-10);return s
 def rows(self,s):
  vi,qi=np.where(self.guard&(s['gaps']<.08));return np.r_[s['J'],self.gap_jac(s,vi,qi)]@s['W'],np.r_[1.1*self.floor-s['vals'],self.geofloor[vi,qi]-s['gaps'][vi,qi]]
 def valid(self,s):
  return np.isfinite(s['vals']).all() and min(s['vals']-self.floor)>-1e-12 and s['gaps'][self.guard].min()>1e-10 and s['det'][~self.vanish].min()>1e-12 and s['det'][self.vanish].min()>-1e-11 and s['h'].min()>.2
 def endpoint(self,u):
  d=json.loads(json.dumps(self.data));X=self.chart(u,False);d['controls']=np.rint(X*d['grid']).astype(np.int64).tolist()
  return snapped(d,self.faces,self.keep,self.drop,self.moved)

def run(a):
 d=json.loads((a.source/'GENERATOR.json').read_text());fs=json.loads((a.source/'faces.json').read_text());m=Leaf(d,fs,a.keep,a.drop,a.moved,a.release);u=m.u0.copy();out=a.out;out.mkdir(parents=True,exist_ok=False);hist=[];frac=.25
 dump(out/'PARAMETERS.json',{k:str(v) if isinstance(v,Path) else v for k,v in vars(a).items()});dump(out/'fixed_floors.json',m.floor.tolist())
 row=np.zeros(m.np);row[m.epindex]=m.scale[m.epindex]
 for it in range(a.steps):
  s=m.allstate(u);eps=m.epsilon(u);rec=dict(it=it,epsilon=float(eps),minexit=float(s['vals'].min()),mingap=float(s['gaps'][m.guard].min()));hist.append(rec);print(rec,flush=True);dump(out/'history.json',hist);dump(out/'CHECKPOINT.json',dict(u_hex=[float(x).hex() for x in u],floor=m.floor.tolist()))
  if abs(eps)<1e-13 and m.valid(s):print('FINITE_LEAF_CONTACT_REACHED',flush=True);break
  target=0 if eps<1e-4 else eps*(1-frac);A,b=m.rows(s);E=(row@s['W'])[None,:]
  v,why=solve(A,b,E,np.array([target-eps]),bound=.1,tol=2e-13,seconds=10,maxsteps=10000);print('PRED',why,flush=True);good=False
  if v is not None:
   for ls in range(8):
    lam=2.**-ls;goal=eps+lam*(target-eps);un=u+lam*s['W']@v
    for rep in range(14):
     try:sn=m.allstate(un)
     except (ValueError,np.linalg.LinAlgError,FloatingPointError):break
     if m.valid(sn):u=un;good=True;rec['accept']=[ls,rep];print('ACCEPT',ls,rep,flush=True);frac=min(.5,frac*1.3) if ls==0 else frac*.7;break
     A,b=m.rows(sn);E=(row@sn['W'])[None,:];dd,why=solve(A,b,E,np.array([goal-m.epsilon(un)]),bound=.1,tol=2e-13,seconds=5,maxsteps=10000)
     if dd is None:print('CORRFAIL',ls,rep,why,flush=True);break
     un+=sn['W']@dd
    if good:break
  if not good:frac*=.4;print('REJECT',flush=True)
  if frac<1e-6:break
 dump(out/'history.json',hist);dump(out/'CHECKPOINT.json',dict(u_hex=[float(x).hex() for x in u],floor=m.floor.tolist()));eps=m.epsilon(u);print('FINAL_EPS',eps,flush=True)
 if abs(eps)<1e-12:
  dd,ff=m.endpoint(u);dump(out/'GENERATOR.json',dd);dump(out/'faces.json',ff);nm=Atlas(dd,ff);ss=nm.state(nm.u0,False);rr=mechanics(ss['q'],ff,P=ss['P'],tol=1e-13);dump(out/'NUMERICAL.json',rr);print('END',rr,flush=True)
if __name__=='__main__':
 p=argparse.ArgumentParser();p.add_argument('--source',type=Path,default=R/'parent/BASIN69_96');p.add_argument('--out',type=Path,required=True);p.add_argument('--keep',type=int,default=26);p.add_argument('--drop',type=int,default=19);p.add_argument('--moved',type=int,default=113);p.add_argument('--release',action='store_true');p.add_argument('--steps',type=int,default=80);run(p.parse_args())
