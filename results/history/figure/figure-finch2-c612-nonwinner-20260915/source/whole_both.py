"""Declared joint primal-basin/dual-facet homotopy, not a no-birth run.
All127 upstream vertex identities plus134 nonstable facets are targets.
The already-repaired145->146 and every vertex outside that basin stay protected.
"""
import os
os.environ['OPENBLAS_NUM_THREADS']='1'
import argparse,json,time
from pathlib import Path
import numpy as np
from intrinsic_search import Model
from stratum_search import correct
from forest_search import freeze

def build():
 m=Model(json.load(open('MARGIN2_GENERATOR.json')),json.load(open('MARGIN2_A.json')),forced={82:85});e=m.eval(m.z0);vv,ff=m.select(e);su={int(m.vi[k]):int(m.vj[k]) for k in vv};su.update(m.forced);basin=[]
 for v in range(len(m.X0)):
  seen=set();j=v;inside=False
  while j!=m.root:assert j not in seen;seen.add(j);inside|=j==82;j=su[j]
  if inside:basin.append(v)
 assert 145 not in basin and su[145]==146
 ids={int(m.vi[k]):int(k) for k in [*vv,*m.target_idx]};m.basin=basin;m.targetU=basin;m.locked_v=np.array([k for k in vv if int(m.vi[k]) not in basin]);orig=m.eval
 def evaluate(z,deriv=False):
  a=orig(z,deriv);fi=m.fi[ff];fj=m.fj[ff];qids=m.normid[m.fid[ff]];r=a['x'][fi]-a['g'];d=a['x'][fj]-a['x'][fi];q=a['q'][qids];rr=np.linalg.norm(r,axis=1);dd=np.linalg.norm(d,axis=1);qq=np.linalg.norm(q,axis=1);fac=m.flens[ff]/(rr*dd*qq);phi=a['face'][ff]*fac
  if deriv:
   dr=a['dx'][fi]-a['dg'];de=a['dx'][fj]-a['dx'][fi];dq=a['dq'][qids]
   logs=np.einsum('ik,ikp->ip',r,dr)/rr[:,None]**2+np.einsum('ik,ikp->ip',d,de)/dd[:,None]**2+np.einsum('ik,ikp->ip',q,dq)/qq[:,None]**2
   dp=fac[:,None]*(a['dface'][ff]-a['face'][ff,None]*logs);a['dvert']=np.r_[a['dvert'],dp]
  a['vert']=np.r_[a['vert'],phi];return a
 m.eval=evaluate;m.select=lambda a:(m.locked_v,np.array([],dtype=int));m.target_idx=np.r_[[ids[v] for v in basin],len(m.vi)+np.arange(len(ff))]
 return m,dict(basin=basin,successor=su,dual_side_indices=ff.tolist(),protected={int(m.vi[k]):float(m.vfloor[m.vi[k]]) for k in m.locked_v})
def main():
 p=argparse.ArgumentParser();p.add_argument('--tag',default='BOTH1');p.add_argument('--start',default='WHOLE1.npy');p.add_argument('--step',type=float,default=.002);p.add_argument('--steps',type=int,default=10);p.add_argument('--goal',type=float,default=1e-7);a=p.parse_args();m,config=build();z=m.z0.copy() if a.start=='-' else np.load(a.start);step=a.step;logs=[];t0=time.time();Path(a.tag+'_CONFIG.json').write_text(json.dumps(config,sort_keys=True));print('ENTRY',m.eval(z)['vert'][m.target_idx].min(),m.census(m.eval(z)),flush=True)
 for it in range(a.steps):
  old=m.eval(z);rho=min(a.goal,float(old['vert'][m.target_idx].min())+step);level=np.full(len(m.target_idx),rho)
  try:zz,b,ok,cor=correct(m,z,level,0,limit=30)
  except (np.linalg.LinAlgError,FloatingPointError) as ex:ok=False;b=old;cor=[str(ex)]
  log=dict(iteration=it,accepted=ok,step=step,rho=rho,targetmin=float(b['vert'][m.target_idx].min()),cmin=float(m.constr(b).min()),census=m.census(b),g=b['g'].tolist(),volume=float(b['volume']),inner=cor,elapsed=time.time()-t0)
  if ok:z=zz;step=min(.01,step*1.25);np.save(a.tag+'.npy',z);freeze(m,z,a.tag+'_GENERATOR.json')
  else:step*=.5
  logs.append(log);Path(a.tag+'_TRACE.json').write_text(json.dumps(logs));print(json.dumps({k:v for k,v in log.items() if k not in ['inner','census']}), 'counts', [len(log['census'][k]) for k in ['S','U','H']],flush=True)
  if ok and rho>0:print('NUMERICAL_POSITIVE',m.census(b),flush=True);break
 print('FINISHED',m.census(m.eval(z)),flush=True)
if __name__=='__main__':main()
