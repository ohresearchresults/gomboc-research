from pathlib import Path
import sys,json,time
import numpy as np
from scipy.linalg import svd
from coarse_atlas import Coarse
from minnorm_qp import solve
from numeric import mechanics
from deletion import canon
from fractions import Fraction as F
raw=json.loads(Path('/mnt/data/research_inputs/C624_STRONG_G8_RAW_EXACT.json').read_text());d=json.loads(Path('/mnt/data/s8/base/GENERATOR.json').read_text());d['controls']=[[int(v*1000000)for v in row]for row in d['controls']];d['grid']*=1000000
cfg=json.loads(Path(sys.argv[1]).read_text());ds=cfg['deleted'];out=Path(sys.argv[2]);out.mkdir(parents=True,exist_ok=False);(out/'CONFIG.json').write_text(canon(cfg));m=Coarse(d,raw,ds);u=m.u0.copy();hist=[];t0=time.monotonic();goal=cfg['goal'];trust=cfg['trust'];gf=cfg['gap_floor'];tf=cfg['tetra_floor']
(out/'INCIDENCE.json').write_text(canon(dict(keep=m.keep.tolist(),faces=m.faces,oldfaces=m.oldfaces,triples=m.base.triples.tolist(),uparent=m.uparent.tolist(),sparent=m.sparent.tolist())))
def merit(s):
 ev=np.minimum(s['vals']-goal,0);gv=np.minimum(s['gaps'][~m.inc]-gf,0);dv=np.minimum(s['det']-tf,0);return float(np.sqrt(ev@ev+100*gv@gv+100*dv@dv))
# Independently finite-difference the analytic full centroid/mixed primal-polar Jacobian.
s=m.state(u);z=np.random.default_rng(5819).normal(size=m.np);z/=np.linalg.norm(z);eps=1e-7;sp=m.state(u+eps*z,False);sm=m.state(u-eps*z,False)
err=float(np.max(np.abs((sp['vals']-sm['vals'])/(2*eps)-s['J']@z)));print('JACOBIAN_PROBE_ERROR',err,flush=True);assert err<2e-6
for it in range(cfg['steps']):
 s=m.state(u);v=merit(s);rec=dict(it=it,merit=v,minexit=float(s['vals'].min()),mingap=float(s['gaps'][~m.inc].min()),mindet=float(s['det'].min()),sec=time.monotonic()-t0);hist.append(rec);print(rec,flush=True);m.save(u,out/'GENERATOR.json');(out/'history.json').write_text(canon(hist))
 if v<1e-12 and s['vals'].min()>0:print('COARSE_NUMERICAL_OWN110',flush=True);break
 mat=np.r_[s['dq'].reshape(-1,m.np)/2,s['dP'].reshape(-1,m.np)];_,dd,Vt=svd(mat,full_matrices=False,check_finite=False);W=Vt.T/np.maximum(dd,cfg['svd_floor'])
 vi,qi=np.where((~m.inc)&(s['gaps']<cfg['near_gap']));A=np.r_[s['J'],m.gap_jac(s,vi,qi),s['ddet']]@W;b=np.r_[1.1*goal-s['vals'],gf-s['gaps'][vi,qi],tf-s['det']]
 delta,why=solve(A,b,bound=trust,tol=cfg['qp_tol'],seconds=cfg['qp_seconds'],maxsteps=cfg['qp_steps']);print('QP',why,flush=True)
 if delta is None:break
 good=False
 for ls in range(18):
  un=u+2.**-ls*W@delta
  try:sn=m.state(un,False)
  except(ValueError,np.linalg.LinAlgError):continue
  if sn['h'].min()>.2 and np.isfinite(merit(sn))and merit(sn)<v*(1-1e-4*2.**-ls):u=un;good=True;print('ACCEPT',ls,flush=True);break
 if not good or time.monotonic()-t0>cfg['seconds']:break
s=m.state(u,False);m.save(u,out/'GENERATOR.json');rep=mechanics(s['q'],m.faces,P=s['P'],tol=1e-13);(out/'NUMERICAL.json').write_text(canon(rep));print('FINAL',rep,flush=True)
