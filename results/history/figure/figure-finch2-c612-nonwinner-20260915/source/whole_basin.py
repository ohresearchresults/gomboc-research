"""Explicit whole-basin homotopy. Temporary births inside the declared basin
are allowed; outside identities, including the previously cancelled145->146,
retain fixed positive reserves. No no-birth claim is made for this homotopy.
"""
import os
os.environ['OPENBLAS_NUM_THREADS']='1'
import argparse,json,time
from pathlib import Path
import numpy as np
from intrinsic_search import Model
from stratum_search import correct
from forest_search import freeze

def main():
 p=argparse.ArgumentParser();p.add_argument('--gen',default='MARGIN2_GENERATOR.json');p.add_argument('--report',default='MARGIN2_A.json');p.add_argument('--tag',default='WHOLE1');p.add_argument('--steps',type=int,default=8);p.add_argument('--step',type=float,default=.01);p.add_argument('--start');p.add_argument('--beta',type=float,default=0);a=p.parse_args()
 m=Model(json.load(open(a.gen)),json.load(open(a.report)),forced={82:85});e=m.eval(m.z0);vv,ff=m.select(e);su={int(m.vi[k]):int(m.vj[k]) for k in vv};su.update(m.forced);basin=[]
 for v in range(len(m.X0)):
  seen=set();j=v;inside=False
  while j!=m.root:assert j not in seen;seen.add(j);inside|=j==82;j=su[j]
  if inside:basin.append(v)
 assert 145 not in basin and su[145]==146
 ids={int(m.vi[k]):int(k) for k in [*vv,*m.target_idx]};m.basin=basin;m.targetU=basin;m.target_idx=np.array([ids[v] for v in basin]);m.locked_v=np.array([k for k in vv if int(m.vi[k]) not in basin]);z=m.z0.copy() if a.start is None else np.load(a.start)
 Path(a.tag+'_CONFIG.json').write_text(json.dumps(dict(basin=basin,successor=su,outside_reserves={int(m.vi[k]):float(m.vfloor[m.vi[k]]) for k in m.locked_v}),sort_keys=True));step=a.step;logs=[];t0=time.time()
 print('ENTRY',len(basin),e['vert'][m.target_idx].min(),m.census(e),flush=True)
 for it in range(a.steps):
  old=m.eval(z);rho=min(2e-5,float(old['vert'][m.target_idx].min())+step);level=np.full(len(m.target_idx),rho)
  try:zz,b,ok,cor=correct(m,z,level,a.beta,limit=25)
  except (np.linalg.LinAlgError,FloatingPointError) as ex:ok=False;b=old;cor=[str(ex)]
  log=dict(iteration=it,accepted=ok,step=step,rho=rho,targetmin=float(b['vert'][m.target_idx].min()),cmin=float(m.constr(b).min()),census=m.census(b),g=b['g'].tolist(),volume=float(b['volume']),inner=cor,elapsed=time.time()-t0)
  if ok:z=zz;step=min(.03,step*1.25);np.save(a.tag+'.npy',z);freeze(m,z,a.tag+'_GENERATOR.json')
  else:step*=.5
  logs.append(log);Path(a.tag+'_TRACE.json').write_text(json.dumps(logs));print(json.dumps({k:v for k,v in log.items() if k!='inner'}),flush=True)
  if ok and rho>0:print('NUMERICAL_POSITIVE',m.census(b),flush=True);break
 print('FINISHED',m.census(m.eval(z)),flush=True)
if __name__=='__main__':main()
