"""Absorb the entire remaining unwanted maximum into the fixed apex.
This is a separate physical architecture, not a centre substitution.
"""
import sys,json,argparse,itertools,time
from pathlib import Path
import numpy as np
R=Path(__file__).resolve().parent;sys.path.insert(0,str(R))
from pinned_blowup import Model
from atlas_opt import Atlas
from numeric import mechanics,topology
from minnorm_qp import solve

def dump(p,o):p.write_text(json.dumps(o,sort_keys=True,separators=(',',':')))
def quotient(fs,a,b):
 mapping={i:(a if i==b else i)for i in range(1+max(max(c)for c in fs))};new={};lost=[]
 for fi,cy in enumerate(fs):
  cc=[]
  for v in cy:
   v=mapping[v]
   if not cc or cc[-1]!=v:cc.append(v)
  if cc[-1]==cc[0]:cc.pop()
  if len(cc)<3:lost.append(fi)
  else:new[fi]=cc
 pruned=set()
 while True:
  oc={i:0 for c in new.values()for i in c}
  for c in new.values():
   for i in c:oc[i]+=1
  bad={i for i,k in oc.items()if k<3}
  if not bad:break
  pruned|=bad
  for j in list(new):
   new[j]=[v for v in new[j]if v not in bad]
   if len(new[j])<3:lost.append(j);del new[j]
 vid={i:k for k,i in enumerate(sorted({v for c in new.values()for v in c}))};ff=[[vid[v]for v in new[j]]for j in sorted(new)];topology(ff);return ff,sorted(lost),sorted(pruned),vid

class Absorb(Model):
 def __init__(self,d,fs,node):
  super().__init__(d,fs,d['n_supports'],node)
  self.target_faces,self.lost,self.pruned,self.vid=quotient(fs,self.ai,self.bi)
  assert not set(self.lost)&{3,16,48,56,72,87,133,134,135,70,93,108,115,118,125}
  self.si=np.array([i for i in self.si if i not in self.lost]);self.vanish=np.array([self.ai in t and self.bi in t or any(v in t for v in self.pruned)for t in self.tri]);s=self.state(self.u0,False);self.floor=np.maximum(5e-8,np.minimum(1e-5,s['vals']*.5));assert np.all(s['vals']>self.floor)
  print('ROOT_ABSORPTION_TOPOLOGY',self.ai,self.bi,'facets lost',self.lost,'pruned',self.pruned,'VEF',len(self.vid),len(topology(self.target_faces)[1]),len(self.target_faces),flush=True)
 def rows(self,s):
  A,b=super().rows(s);b[:len(self.floor)]=self.floor-s['vals'];return A,b
 def endpoint(self,u):
  d=json.loads(json.dumps(self.data));X=self.chart(u,False);X[self.bb]=X[self.aa];lost=set(self.lost);gone=lost|{self.bb};keep=[i for i in range(len(X))if i not in gone];ix={i:k for k,i in enumerate(keep)};ix[self.bb]=ix[self.aa]
  d['controls']=np.rint(X[keep]*d['grid']).astype(np.int64).tolist();d['n_supports']-=len(lost);groups=[]
  for k,g in enumerate(self.data['groups']):
   i=self.n+k
   if i==self.bb:continue
   if i==self.aa:g=sorted(set(g)|set(self.data['groups'][self.bb-self.n]))
   groups.append([ix[j]for j in g if j not in lost])
  d['groups']=groups;pp=[]
  for i,deps,ax in self.data['plan']:
   if i in gone:continue
   ds=list(dict.fromkeys(self.aa if j==self.bb else j for j in deps if j not in lost))
   if len(ds)!=len(deps):ax=list(max(itertools.combinations(range(3),len(ds)),key=lambda a:abs(np.linalg.det(X[np.ix_(ds,a)])))) if ds else []
   pp.append([ix[i],[ix[j]for j in ds],ax])
  d['plan']=pp;return d,self.target_faces

def run(a):
 d=json.loads((a.source/'GENERATOR.json').read_text());fs=json.loads((a.source/'faces.json').read_text());m=Absorb(d,fs,a.node);u=m.u0.copy();out=a.out;out.mkdir(parents=True,exist_ok=False);hist=[];frac=.25;t0=time.monotonic();row=np.zeros(m.np);row[m.epindex]=m.scale[m.epindex]
 dump(out/'PARAMETERS.json',{k:str(v)if isinstance(v,Path)else v for k,v in vars(a).items()});dump(out/'fixed_floors.json',m.floor.tolist())
 for it in range(a.steps):
  s=m.allstate(u);eps=m.epsilon(u);rec=dict(it=it,epsilon=float(eps),minexit=float(s['vals'].min()),mingap=float(s['gaps'][m.guard].min()));hist.append(rec);print(rec,flush=True);dump(out/'history.json',hist);dump(out/'CHECKPOINT.json',dict(u_hex=[float(v).hex()for v in u]))
  if abs(eps)<1e-12 and m.valid(s):break
  target=0 if eps<1e-4 else eps*(1-frac);A,b=m.rows(s);E=(row@s['W'])[None,:];v,why=solve(A,b,E,np.array([target-eps]),bound=.1,tol=2e-13,seconds=10,maxsteps=10000);print('PRED',why,flush=True);good=False
  if v is not None:
   for ls in range(9):
    lam=2.**-ls;goal=eps+lam*(target-eps);un=u+lam*s['W']@v
    for rep in range(20):
     if time.monotonic()-t0>a.seconds:break
     try:sn=m.allstate(un)
     except Exception:break
     if m.valid(sn):u=un;good=True;rec['accept']=[ls,rep];print('ACCEPT',ls,rep,flush=True);frac=min(.5,frac*1.3)if ls==0 else frac*.7;break
     A,b=m.rows(sn);E=(row@sn['W'])[None,:];dv,why=solve(A,b,E,np.array([goal-m.epsilon(un)]),bound=.1,tol=2e-13,seconds=5,maxsteps=10000)
     if dv is None:print('CORRFAIL',ls,rep,why,flush=True);break
     un+=sn['W']@dv
    if good or time.monotonic()-t0>a.seconds:break
  if not good:frac*=.4
  if frac<1e-6 or time.monotonic()-t0>a.seconds:break
 dump(out/'CHECKPOINT.json',dict(u_hex=[float(v).hex()for v in u]));dump(out/'history.json',hist);print('FINAL_EPS',m.epsilon(u),flush=True)
 if abs(m.epsilon(u))<1e-10:
  dd,ff=m.endpoint(u);dump(out/'GENERATOR.json',dd);dump(out/'faces.json',ff);mm=Atlas(dd,ff);z=mm.state(mm.u0,False);rr=mechanics(z['q'],ff,P=z['P'],tol=1e-13);dump(out/'NUMERICAL.json',rr);print('FINITE',rr,flush=True)
if __name__=='__main__':
 p=argparse.ArgumentParser();p.add_argument('--source',type=Path,required=True);p.add_argument('--out',type=Path,required=True);p.add_argument('--node',type=int,default=141);p.add_argument('--steps',type=int,default=100);p.add_argument('--seconds',type=float,default=600);run(p.parse_args())
