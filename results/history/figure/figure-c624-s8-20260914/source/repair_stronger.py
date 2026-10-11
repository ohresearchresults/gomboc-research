"""Full own-volume-centroid repair of a prescribed exact contact chart.
SVD metric preconditioning and sequential minimum-norm linear inequalities.
Dynamic complete-vertex/polar escape witnesses. Proposals are not certificates.
Usage: repair.py BQ13_SOURCE input_dir fresh_output goal trust steps seconds
"""
import json,sys,time
from pathlib import Path
import numpy as np
from scipy.linalg import svd
base,src,out=map(lambda x:Path(x).resolve(),sys.argv[1:4]);goal,trust=float(sys.argv[4]),float(sys.argv[5]);steps=int(sys.argv[6]);seconds=float(sys.argv[7])
sys.path[:0]=[str(base/'parent/mechanism'),str(base/'parent/mechanism/parent_sources')]
from atlas_opt import Atlas
from numeric import mechanics
from minnorm_qp import solve
d=json.loads((src/'GENERATOR.json').read_text());fs=json.loads((src/'faces.json').read_text());m=Atlas(d,fs)
parentd=json.loads((base/'BASIN69_96/GENERATOR.json').read_text());parentf=json.loads((base/'BASIN69_96/faces.json').read_text());pm=Atlas(parentd,parentf);ps=pm.state(pm.u0,False)
a,b=pm.owners.index([16,18,94]),pm.owners.index([18,71,94]);up=ps['cu'].argmax(1);sp=ps['cs'].argmax(1)
alias=lambda i:(a if i==b else i)-(i>b)
pnew=[]
for i in range(len(up)):
 if i==b:continue
 j=int(up[i]);seen={i}
 while j in (a,b):
  assert j not in seen;seen.add(j);j=int(up[j])
 pnew.append(alias(j))
m.uparent=np.array(pnew);m.sparent=sp
u=m.u0.copy();out.mkdir(parents=True,exist_ok=False);hist=[];t0=time.monotonic();gf=1e-7;tf=1e-9
(out/'faces.json').write_text(json.dumps(fs,separators=(',',':')))
def merit(s):
 ev=np.minimum(s['vals']-goal,0);gv=np.minimum(s['gaps'][~m.inc]-gf,0);dv=np.minimum(s['det']-tf,0)
 return float(np.sqrt(ev@ev+100*gv@gv+100*dv@dv))
for it in range(steps):
 s=m.state(u);v=merit(s);rec=dict(it=it,merit=v,minexit=float(s['vals'].min()),mingap=float(s['gaps'][~m.inc].min()),mindet=float(s['det'].min()),sec=time.monotonic()-t0);hist.append(rec);print(rec,flush=True)
 m.save(u,out/'GENERATOR.json');(out/'history.json').write_text(json.dumps(hist,indent=2))
 if v<1e-12 and s['vals'].min()>0:print('COMBINED_C624_NUMERICAL_OWN110',flush=True);break
 mat=np.r_[s['dq'].reshape(-1,m.np)/2,s['dP'].reshape(-1,m.np)];_,dd,Vt=svd(mat,full_matrices=False,check_finite=False);W=Vt.T/np.maximum(dd,1e-9)
 vi,qi=np.where((~m.inc)&(s['gaps']<.06));A=np.r_[s['J'],m.gap_jac(s,vi,qi),s['ddet']]@W;b=np.r_[1.1*goal-s['vals'],gf-s['gaps'][vi,qi],tf-s['det']]
 delta,why=solve(A,b,bound=trust,tol=2e-12,seconds=8,maxsteps=10000);print('QP',why,flush=True)
 if delta is None:break
 good=False
 for ls in range(18):
  un=u+2.**-ls*W@delta
  try:sn=m.state(un,False)
  except (ValueError,np.linalg.LinAlgError):continue
  if sn['h'].min()>.2 and np.isfinite(merit(sn)) and merit(sn)<v*(1-1e-4*2.**-ls):u=un;good=True;print('ACCEPT',ls,flush=True);break
 if not good or time.monotonic()-t0>seconds:break
s=m.state(u,False);m.save(u,out/'GENERATOR.json');rep=mechanics(s['q'],fs,P=s['P'],tol=1e-13);(out/'NUMERICAL.json').write_text(json.dumps(rep,indent=2));print('FINAL',rep,flush=True)
