"""Own-filled-mass coupled repair on an exact contracted contact chart.
Fixed acyclic witness trees are mapped from the pre-contraction checkpoint.
Finite proposal only: final acceptance requires independently rebuilt exact audits.
"""
import sys,json,time,argparse
from pathlib import Path
import numpy as np
from scipy.linalg import svd
from blowup_edge import Model
from atlas_opt import Atlas
from numeric import mechanics
from minnorm_qp import solve
R=Path(__file__).resolve().parent

def rooted(parent,root):
 for i in range(len(parent)):
  v=i;seen=set()
  while v!=root:
   assert v not in seen,('cycle',i,seen);seen.add(v);v=int(parent[v])

def refs():
 cp=json.loads((R/'experiments/BLOWUP_CHECKPOINT.json').read_text());d=json.loads((R/'C628_WINNER/GENERATOR.json').read_text());fs=json.loads((R/'C628_WINNER/faces.json').read_text());o=Model(d,fs,152,155);u=np.array([float.fromhex(x) for x in cp['u_hex']]);s=o.state(u,False)
 pa=o.uparent.copy();pa[o.bi]=o.ai;rooted(pa,o.Uroot);ps=o.sparent.copy();rooted(ps,3)
 alias=lambda i:(o.ai if i==o.bi else i)-(i>o.bi)
 pn=np.array([alias(pa[i]) for i in range(len(pa)) if i!=o.bi]);rooted(pn,alias(o.Uroot))
 return pn,ps

def run(a):
 d=json.loads((a.source/'GENERATOR.json').read_text());fs=json.loads((a.source/'faces.json').read_text());m=Atlas(d,fs);m.uparent,m.sparent=refs();u=m.u0.copy();floor=np.full(len(m.si)+len(m.ui),a.goal);out=a.out;out.mkdir(exist_ok=True,parents=True);hist=[];t0=time.monotonic()
 if a.initial:u=np.load(a.initial)['u']
 gf=np.full_like(m.inc,1e-7,dtype=float);tf=1e-9
 def measures(s):
  ev=np.minimum(s['vals']-floor,0);gv=np.minimum(s['gaps'][~m.inc]-gf[~m.inc],0);dv=np.minimum(s['det']-tf,0)
  return float(np.sqrt(ev@ev+100*gv@gv+100*dv@dv)),ev,gv,dv
 for k in range(a.steps):
  s=m.state(u);merit,ev,gv,dv=measures(s);rec=dict(k=k,merit=merit,minexit=float(s['vals'].min()),mingap=float(s['gaps'][~m.inc].min()),mindet=float(s['det'].min()),badmech=int((ev<0).sum()),badgeom=int((gv<0).sum()),sec=time.monotonic()-t0);hist.append(rec);print(rec,flush=True)
  m.save(u,out/'GENERATOR.json');np.savez(out/'END.npz',u=u);(out/'faces.json').write_text(json.dumps(fs,separators=(',',':')));(out/'history.json').write_text(json.dumps(hist,indent=2));(out/'witnesses.json').write_text(json.dumps(dict(p=m.uparent.tolist(),q=m.sparent.tolist(),goal=a.goal)))
  if s['vals'].min()>0 and s['gaps'][~m.inc].min()>0 and s['det'].min()>0 and merit<1e-12:print('REPAIR626_NUMERICAL110',flush=True);break
  mat=np.r_[s['dq'].reshape(-1,m.np)/2,s['dP'].reshape(-1,m.np)];_,dd,Vt=svd(mat,full_matrices=False,check_finite=False);W=Vt.T/np.maximum(dd,1e-9)
  vi,qi=np.where((~m.inc)&(s['gaps']<.06));A=np.r_[s['J'],m.gap_jac(s,vi,qi),s['ddet']]@W;b=np.r_[1.1*floor-s['vals'],gf[vi,qi]-s['gaps'][vi,qi],tf-s['det']]
  step,why=solve(A,b,bound=a.trust,tol=2e-13,seconds=8,maxsteps=10000);print('QP',why,flush=True)
  if step is None:break
  good=False
  for ls in range(18):
   v=u+2.**-ls*W@step
   try:ss=m.state(v,False)
   except Exception:continue
   mm=measures(ss)[0]
   if ss['h'].min()>.2 and np.isfinite(mm) and mm<merit*(1-1e-4*2.**-ls):u=v;good=True;print('ACCEPT',ls,float(np.linalg.norm(step)),mm,flush=True);break
  if not good:print('STALLED',flush=True);break
  if time.monotonic()-t0>a.seconds:break
 s=m.state(u,False);m.save(u,out/'GENERATOR.json');np.savez(out/'END.npz',u=u);report=mechanics(s['q'],fs,P=s['P'],tol=1e-13);(out/'NUMERICAL.json').write_text(json.dumps(report,indent=2));print('FINAL',report,flush=True)
if __name__=='__main__':
 p=argparse.ArgumentParser();p.add_argument('--source',type=Path,required=True);p.add_argument('--out',type=Path,required=True);p.add_argument('--goal',type=float,default=1e-6);p.add_argument('--trust',type=float,default=.05);p.add_argument('--steps',type=int,default=50);p.add_argument('--seconds',type=float,default=500);p.add_argument('--initial');run(p.parse_args())
