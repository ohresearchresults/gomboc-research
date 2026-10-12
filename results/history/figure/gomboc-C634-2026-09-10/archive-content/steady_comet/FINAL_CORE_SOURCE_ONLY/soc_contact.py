"""Filled-centroid SQP contact homotopy with nonlinear feasibility corrections.
Only discovery. Exact rational maximal-complex audits gate every claimed body.
"""
from pathlib import Path
import json,time,sys,numpy as np
from scipy.optimize import linprog
from atlas_opt import Atlas
from numeric import mechanics,recover
from condition_events import merge_rechart

def lp_rows(m,st,keep,trust):
 mask=(~m.inc)&(st['gaps']<max(.03,trust*80));vi,qi=np.where(mask);G=m.gap_jac(st,vi,qi)
 return np.vstack([-st['J'],-G]),np.r_[st['vals']-keep,st['gaps'][vi,qi]-1e-12]
def solve_lp(obj,A,b,bounds,limit=3):
 scale=np.maximum(np.linalg.norm(A,axis=1),1e-3)
 return linprog(obj,A_ub=A/scale[:,None],b_ub=b/scale,bounds=bounds,method='highs',options={'primal_feasibility_tolerance':1e-9,'dual_feasibility_tolerance':1e-9,'time_limit':float(limit)})
def valid(m,st,keep):return st['gaps'][~m.inc].min()>-1e-11 and st['vals'].min()>keep*.99 and st['h'].min()>0 and st['det'].min()>-1e-12

def run(gfile,ffile,outprefix,target,steps=240,keep=2e-6):
 out=Path(outprefix);out.parent.mkdir(exist_ok=True,parents=True);g=json.loads(Path(gfile).read_text());fs=json.loads(Path(ffile).read_text());m=Atlas(g,fs);u=m.u0.copy();n=m.np;trust=.0002;start=time.time();corrections=0
 for it in range(steps):
  st=m.state(u);oldgap=st['gaps'][target];minimum=st['gaps'][~m.inc].min();assert valid(m,st,keep*.9)
  if it%5==0:print('SOC_ITER',it,'sec',round(time.time()-start,2),'target',oldgap,'mingap',minimum,'mincos',st['vals'].min(),'trust',trust,'corrections',corrections,flush=True)
  if it%10==0:m.save(u,out.with_suffix('.json'));np.savez(out.with_suffix('.npz'),u=u,X=st['X'],P=st['P'],q=st['q'],c=st['c'],vals=st['vals']);out.with_name(out.name+'_faces.json').write_text(json.dumps(fs,separators=(',',':')))
  if minimum<3e-8:print('SOC_CONTACT',flush=True);break
  obj=m.gap_jac(st,np.array([target[0]]),np.array([target[1]]))[0];A,b=lp_rows(m,st,keep*1.05,trust);lp=solve_lp(obj,A,b,[(-trust,trust)]*n)
  if not lp.success:
   trust*=.5;print('SOC_LP_FAIL',it,lp.message,flush=True)
   if trust<1e-9:break
   continue
  step=lp.x;accepted=False
  for ls in range(15):
   lam=2.**(-ls);nu=u+lam*step
   try:new=m.state(nu,False)
   except Exception:continue
   if new['gaps'][target]>=oldgap-1e-12:continue
   if not valid(m,new,keep) and new['gaps'].min()>-.02 and new['vals'].min()>-.05:
    for rep in range(3):
     try:nn=m.state(nu)
     except Exception:break
     Ac,bc=lp_rows(m,nn,keep*1.08,trust);Ac=np.column_stack([Ac,np.zeros(len(bc))]);TG=m.gap_jac(nn,np.array([target[0]]),np.array([target[1]]))[0]
     Ac=np.vstack([Ac,np.column_stack([np.eye(n),-np.ones(n)]),np.column_stack([-np.eye(n),-np.ones(n)]),np.r_[TG,0][None,:]])
     bc=np.r_[bc,np.zeros(2*n),max(0.,(oldgap-nn['gaps'][target])*.25)]
     rad=trust*lam*.8;sol=solve_lp(np.r_[np.zeros(n),1.],Ac,bc,[(-rad,rad)]*n+[(0,rad)],limit=2)
     if not sol.success:break
     nu+=sol.x[:n];corrections+=1
     try:new=m.state(nu,False)
     except Exception:break
     if valid(m,new,keep):break
   if valid(m,new,keep) and new['gaps'][target]<oldgap-1e-12:
    u=nu;accepted=True
    if ls<=1:trust=min(trust*1.6,.004)
    elif ls>=3:trust=max(trust*.5,1e-9)
    break
  if not accepted:
   trust*=.4
   if trust<1e-9:print('SOC_STALL',flush=True);break
 st=m.state(u);z=m.save(u,out.with_suffix('.json'));out.with_name(out.name+'_faces.json').write_text(json.dumps(fs,separators=(',',':')));print('SOC_FINISH','E',len(m.ef),'gap',st['gaps'][target],'mincos',st['vals'].min(),flush=True)
 H={tuple(map(int,l.split())) for l in (Path(__file__).parent/'H213_edges.txt').read_text().splitlines()}
 for length,a,b in sorted((np.linalg.norm(st['P'][a]-st['P'][b]),a,b) for a,b in m.ef)[:10]:
  if length>.003 or tuple(sorted(m.ef[a,b])) in H:continue
  try:
   zz,ff,depth=merge_rechart(z,fs,a,b,controls=st['X']);rr=mechanics(recover(zz)[:137],ff,tol=1e-11);print('SOC_MERGE',a,b,m.ef[a,b],length,rr,flush=True)
   if rr['counts']==[1,1,0] and rr['min_gap']>1e-9 and rr['max_incidence_error']<1e-8 and min(rr['polar_escape_min'],rr['primal_escape_min'])>2e-7:
    tag=f'C{rr["E"]*2}_SOC_{a}_{b}';base=out.with_name(tag);base.with_name(tag+'_GENERATOR.json').write_text(json.dumps(zz,sort_keys=True,separators=(',',':')));base.with_name(tag+'_faces.json').write_text(json.dumps(ff,separators=(',',':')));base.with_name(tag+'_numeric.json').write_text(json.dumps(dict(removed_polar=m.ef[a,b],**rr),indent=2));print('SOC_NUMERIC_WINNER',tag,flush=True);break
  except Exception as e:print('SOC_MERGE_ERROR',repr(e),flush=True)

if __name__=='__main__':
 import argparse
 p=argparse.ArgumentParser();p.add_argument('generator');p.add_argument('faces');p.add_argument('outprefix');p.add_argument('--target',type=int,nargs=2,required=True);p.add_argument('--steps',type=int,default=240);p.add_argument('--keep',type=float,default=2e-6);a=p.parse_args();run(a.generator,a.faces,a.outprefix,tuple(a.target),a.steps,a.keep)
