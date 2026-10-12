"""Fresh explicitly scoped phase from the exact C612/G7 nonwinner.
Both previous cancellations (88->91 and old146) have fixed positive reserves.
No output of this controller is promoted without replay_new-style exact checks.
"""
import os
os.environ['OPENBLAS_NUM_THREADS']='1'
import argparse,json,time
from pathlib import Path
import numpy as np
from coupled import Model
from stratum_search import correct
from forest_search import freeze
from recover_cases import generator
from replay_new import forest612

def main():
 p=argparse.ArgumentParser();p.add_argument('--steps',type=int,default=0);p.add_argument('--step',type=float,default=.0002);p.add_argument('--tag',default='CONTINUE612');a=p.parse_args()
 R=json.load(open('D16_ONE_GRID7_A.json'));m=Model(generator('D16_ONE_GRID7'),R,deleted=(16,99,117),forced={82:85});proof=forest612(R);su=proof['successors'];idx={(int(i),int(j)):k for k,(i,j) in enumerate(zip(m.vi,m.vj))};m.locked_v=np.array([idx[(i,j)] for i,j in enumerate(su) if j>=0 and i!=82]);entry=m.eval(m.z0)
 for k in m.locked_v:m.vfloor[m.vi[k]]=max(1e-8,.2*entry['vert'][k])
 m.basin=[]
 for i in range(len(m.X0)):
  j=i
  while j not in [82,m.root]:j=su[j]
  if j==82:m.basin.append(i)
 assert su[88]==91 and su[144]==145
 Path(a.tag+'_SCOPE.json').write_text(json.dumps(dict(successors=su,basin=m.basin,protected_vertex_floors={int(m.vi[k]):float(m.vfloor[m.vi[k]]) for k in m.locked_v},facet_floors=m.ffloor.tolist()),sort_keys=True))
 z=m.z0.copy();step=a.step;log=[];t0=time.time()
 for it in range(a.steps):
  e=m.eval(z);level=np.minimum(2e-6,e['vert'][m.target_idx]+step);zz,b,ok,inner=correct(m,z,level,0,limit=20)
  if ok:z=zz;step=min(.004,step*1.25)
  else:step*=.5
  r=dict(iteration=it,accepted=ok,step_after=step,level=level.tolist(),target=b['vert'][m.target_idx].tolist(),cmin=float(m.constr(b).min()),inner=inner,elapsed=time.time()-t0,census=m.census(b));log.append(r);Path(a.tag+'_TRACE.json').write_text(json.dumps(log));print(json.dumps({k:v for k,v in r.items() if k!='inner'}),flush=True)
  if ok and b['vert'][m.target_idx].min()>1e-8:break
 np.save(a.tag+'.npy',z);freeze(m,z,a.tag+'_GENERATOR.json');print('NUMERICAL_CONTINUATION_FINISHED',m.census(m.eval(z)),flush=True)
if __name__=='__main__':main()
