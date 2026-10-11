"""Cancel the newly introduced88--91 basin after deleting16, without
re-exempting the already repaired original146 basin. Existing sink82 is
explicitly retained in the allowed defect set. Every other identity is protected.
"""
import os
os.environ['OPENBLAS_NUM_THREADS']='1'
import argparse,json,time
from pathlib import Path
import numpy as np
from coupled import Model
from stratum_search import correct
from forest_search import freeze

def main():
 p=argparse.ArgumentParser();p.add_argument('--tag',default='D16_ONE');p.add_argument('--steps',type=int,default=6);p.add_argument('--step',type=float,default=.002);a=p.parse_args();m=Model(json.load(open('MARGIN2_GRID6_GENERATOR.json')),json.load(open('MARGIN2_GRID6_DELETE16_A.json')),deleted=(16,99,117),forced={88:91});assert set(m.targetU)=={82,88};v=m.eval(m.z0);m.locked_v=m.select(v)[0];su={int(m.vi[k]):int(m.vj[k]) for k in m.locked_v};su.update(m.forced)
 for i in range(len(m.X0)):
  seen=set()
  while i not in [82,m.root]:assert i not in seen;seen.add(i);i=su[i]
 assert su[144]==145
 m.basin=[88];z=m.z0.copy();step=a.step;logs=[];t0=time.time()
 for it in range(a.steps):
  e=m.eval(z);level=np.minimum(2e-6,e['vert'][m.target_idx]+step);zz,b,ok,cor=correct(m,z,level,0,limit=20);r=dict(iteration=it,accepted=ok,step=step,level=level.tolist(),target=b['vert'][m.target_idx].tolist(),cmin=float(m.constr(b).min()),inner=cor,elapsed=time.time()-t0,census=m.census(b))
  if ok:z=zz;step=min(.004,step*1.25);np.save(a.tag+'.npy',z);freeze(m,z,a.tag+'_GENERATOR.json')
  else:step*=.5
  logs.append(r);Path(a.tag+'_TRACE.json').write_text(json.dumps(logs));print(json.dumps({k:v for k,v in r.items() if k!='inner'}),flush=True)
  if ok and b['vert'][m.target_idx].min()>1e-8:print('CANCELLATION_NUMERICAL',m.census(b),flush=True);break
 print('FINISHED',m.census(m.eval(z)),flush=True)
if __name__=='__main__':main()
