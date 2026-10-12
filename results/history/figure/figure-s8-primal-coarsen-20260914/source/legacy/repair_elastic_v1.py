"""Finite-progress primal-vertex coarsening, numerical search only.
Usage: S8_SOURCE=... python repair_elastic.py RAW_COMPLEX S8_GENERATOR CONFIG OUT
No result is accepted without a separate exact full hull/mass/mechanics audit.
"""
from pathlib import Path
import os,sys,json,time
import numpy as np
from scipy.linalg import svd
from scipy.optimize import linprog
from coarse_atlas import Coarse
from numeric import mechanics
from deletion import canon
raw=json.loads(Path(sys.argv[1]).read_text());d=json.loads(Path(sys.argv[2]).read_text());old=d['grid'];d['grid']=10**14;assert d['grid']%old==0;d['controls']=[[int(v*(d['grid']//old))for v in row]for row in d['controls']]
cfg=json.loads(Path(sys.argv[3]).read_text());out=Path(sys.argv[4]);out.mkdir(parents=True,exist_ok=False);(out/'CONFIG.json').write_text(canon(cfg));m=Coarse(d,raw,cfg['deleted']);u=m.u0.copy();hist=[];t0=time.monotonic();goal=cfg['goal'];gf=cfg['gap_floor'];tf=cfg['tetra_floor'];trust=cfg['trust'];mode=cfg.get('witness','forest')
if 'resume_generator' in cfg:
 from numeric import recover
 rg=json.loads((Path(sys.argv[3]).parent/cfg['resume_generator']).read_text());rx=recover(rg);u=rx[m.base.free[:,0],m.base.free[:,1]]/m.base.scale
(out/'INCIDENCE.json').write_text(canon(dict(keep=m.keep.tolist(),faces=m.faces,oldfaces=m.oldfaces,triples=m.base.triples.tolist(),uparent=m.uparent.tolist(),sparent=m.sparent.tolist())))
def state(u,jac=True):return m.state(u,jac,parents=(mode=='forest'))
def merit(s):
 ev=np.minimum(s['vals']-goal,0);gv=np.minimum(s['gaps'][~m.inc]-gf,0);dv=np.minimum(s['det']-tf,0);return float(np.sqrt(ev@ev+100*gv@gv+100*dv@dv))
s=state(u);z=np.random.default_rng(5819).normal(size=m.np);z/=np.linalg.norm(z);eps=1e-7;err=float(np.max(np.abs((state(u+eps*z,False)['vals']-state(u-eps*z,False)['vals'])/(2*eps)-s['J']@z)));assert err<2e-6;print('JACOBIAN_PROBE',err,flush=True)
for it in range(cfg['steps']):
 s=state(u);v=merit(s);rec=dict(it=it,merit=v,minexit=float(s['vals'].min()),mingap=float(s['gaps'][~m.inc].min()),mindet=float(s['det'].min()));hist.append(rec);print(rec,flush=True);m.save(u,out/'GENERATOR.json');(out/'history.json').write_text(canon(hist))
 if v<1e-12 and s['vals'].min()>0:print('COARSE_NUMERICAL_OWN110',flush=True);break
 mat=np.r_[s['dq'].reshape(-1,m.np)/2,s['dP'].reshape(-1,m.np)];_,dd,Vt=svd(mat,full_matrices=False,check_finite=False);W=Vt.T/np.maximum(dd,cfg['svd_floor']);vi,qi=np.where((~m.inc)&(s['gaps']<cfg['near_gap']))
 J=np.r_[s['J'],m.gap_jac(s,vi,qi),s['ddet']]@W
 # Positive escapes can lose at most half their surplus. Negative ones must
 # improve a common fraction theta; geometry keeps actual strict support gaps.
 b=np.r_[-cfg['positive_allowance']*np.maximum(s['vals']-goal,0),gf-s['gaps'][vi,qi],tf-s['det']]
 dt=np.r_[np.maximum(goal-s['vals'],0),np.zeros(len(vi)+len(s['det']))]
 norms=np.maximum(np.linalg.norm(J,axis=1),1e-10);Ac=np.c_[-J,dt]/norms[:,None];bc=-b/norms
 cost=np.r_[np.zeros(m.np),-1.];opt=linprog(cost,A_ub=Ac,b_ub=bc,bounds=[(-trust,trust)]*m.np+[(0,1)],method='highs',options={'time_limit':cfg['lp_seconds'],'dual_feasibility_tolerance':1e-9,'primal_feasibility_tolerance':1e-9})
 rec['lp_status']=int(opt.status);rec['theta']=float(opt.x[-1])if opt.x is not None else None;print('LP',opt.status,rec['theta'],flush=True)
 if not opt.success or opt.x[-1]<cfg['theta_floor']:break
 delta=W@opt.x[:-1];good=False
 for ls in range(cfg['backtracks']):
  un=u+2.**-ls*delta
  try:sn=state(un,False)
  except(ValueError,np.linalg.LinAlgError):continue
  if sn['h'].min()>.2 and sn['gaps'][~m.inc].min()>0 and sn['det'].min()>0 and np.isfinite(merit(sn)) and merit(sn)<v*(1-1e-4*2.**-ls):u=un;good=True;rec['line']=ls;break
 if not good:trust*=.25
 if trust<cfg['trust_floor'] or time.monotonic()-t0>cfg['seconds']:break
s=state(u,False);m.save(u,out/'GENERATOR.json');rep=mechanics(s['q'],m.faces,P=s['P'],tol=1e-13);(out/'NUMERICAL.json').write_text(canon(rep));(out/'history.json').write_text(canon(hist));print('FINAL',rep,flush=True)
