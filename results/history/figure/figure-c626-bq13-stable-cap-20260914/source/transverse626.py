"""Finite free-contact-node contraction and full actual-centroid repair.
Construction is exact after literal control rounding; all generated candidates
still require independent complete exact maximal-complex/mechanical audits.
"""
import json,sys,time,argparse,itertools
from pathlib import Path
import numpy as np
from scipy.linalg import svd
R=Path(__file__).resolve().parent;sys.path[:0]=[str(R/'parent/mechanism'),str(R/'parent/mechanism/parent_sources')]
from atlas_opt import Atlas
from numeric import recover,merge_faces,mechanics
from minnorm_qp import solve
from repair626 import rooted

def seed(d,fs,av,bv,an,bn,t):
 d=json.loads(json.dumps(d));X=recover(d);X[an]=(1-t)*X[an]+t*X[bn];d['controls'][an]=np.rint(X[an]*d['grid']).astype(np.int64).tolist();d['controls'].pop(bn);d['groups'][an-137]=sorted(set(d['groups'][an-137])|set(d['groups'][bn-137]));d['groups'].pop(bn-137);alias=lambda i:(an if i==bn else i)-(i>bn);plan=[]
 for i,deps,axes in d['plan']:
  if i==bn:continue
  ds=list(dict.fromkeys(an if j==bn else j for j in deps))
  if len(ds)!=len(deps):axes=list(max(itertools.combinations(range(3),len(ds)),key=lambda ax:abs(np.linalg.det(X[np.ix_(ds,ax)]))))
  plan.append([alias(i),[alias(j) for j in ds],axes])
 d['plan']=plan
 return d,merge_faces(fs,av,bv)

def run(a):
 original=json.loads((R/'C628_WINNER/GENERATOR.json').read_text());of=json.loads((R/'C628_WINNER/faces.json').read_text());om=Atlas(original,of);os=om.state(om.u0,False);sp=os['cs'].argmax(1);up=os['cu'].argmax(1);alias=lambda i:(a.av if i==a.bv else i)-(i>a.bv)
 paths=[]
 for v in [a.av,a.bv]:
  path=[v]
  while v!=om.Uroot:v=int(up[v]);path.append(v)
  paths.append(path)
 keep=a.bv if a.bv in paths[0][1:] else a.av
 pp=np.array([alias(up[i]) if i!=a.av else alias(up[keep]) for i in range(len(up)) if i!=a.bv]);rooted(pp,alias(om.Uroot));rooted(sp,3)
 d,fs=seed(original,of,a.av,a.bv,a.an,a.bn,a.t);out=a.out;out.mkdir(exist_ok=True,parents=True);(out/'SEED.json').write_text(json.dumps(d,sort_keys=True,separators=(',',':')));m=Atlas(d,fs);m.sparent=sp;m.uparent=pp;u=m.u0.copy();floor=np.full(len(m.si)+len(m.ui),1e-6);gf=1e-7;tf=1e-9;hist=[];t0=time.monotonic()
 def merit(s):
  ev=np.minimum(s['vals']-floor,0);gv=np.minimum(s['gaps'][~m.inc]-gf,0);dv=np.minimum(s['det']-tf,0);return float(np.sqrt(ev@ev+100*gv@gv+100*dv@dv))
 for it in range(a.steps):
  s=m.state(u);v=merit(s);rec=dict(it=it,merit=v,minexit=float(s['vals'].min()),mingap=float(s['gaps'][~m.inc].min()),mindet=float(s['det'].min()),sec=time.monotonic()-t0);hist.append(rec);print(rec,flush=True);m.save(u,out/'GENERATOR.json');(out/'faces.json').write_text(json.dumps(fs,separators=(',',':')));(out/'history.json').write_text(json.dumps(hist,indent=2));np.savez(out/'END.npz',u=u)
  if v<1e-12 and s['vals'].min()>0:print('TRANSVERSE_NUMERICAL_OWN110',flush=True);break
  mat=np.r_[s['dq'].reshape(-1,m.np)/2,s['dP'].reshape(-1,m.np)];_,dd,Vt=svd(mat,full_matrices=False,check_finite=False);W=Vt.T/np.maximum(dd,1e-9);vi,qi=np.where((~m.inc)&(s['gaps']<.08));A=np.r_[s['J'],m.gap_jac(s,vi,qi),s['ddet']]@W;b=np.r_[floor*1.1-s['vals'],gf-s['gaps'][vi,qi],tf-s['det']];delta,why=solve(A,b,bound=.15,tol=2e-13,seconds=8,maxsteps=10000)
  print('QP',why,flush=True)
  if delta is None:break
  good=False
  for ls in range(17):
   un=u+2.**-ls*W@delta
   try:sn=m.state(un,False)
   except Exception:continue
   if sn['h'].min()>.1 and merit(sn)<v*(1-1e-4*2.**-ls):u=un;good=True;print('ACCEPT',ls,flush=True);break
  if not good or time.monotonic()-t0>a.seconds:break
 s=m.state(u,False);m.save(u,out/'GENERATOR.json');rep=mechanics(s['q'],fs,P=s['P'],tol=1e-13);(out/'NUMERICAL.json').write_text(json.dumps(rep,indent=2));print('FINAL',rep,flush=True)
if __name__=='__main__':
 p=argparse.ArgumentParser();p.add_argument('--av',type=int,required=True);p.add_argument('--bv',type=int,required=True);p.add_argument('--an',type=int,required=True);p.add_argument('--bn',type=int,required=True);p.add_argument('--t',type=float,default=.5);p.add_argument('--out',type=Path,required=True);p.add_argument('--steps',type=int,default=80);p.add_argument('--seconds',type=float,default=150);run(p.parse_args())
