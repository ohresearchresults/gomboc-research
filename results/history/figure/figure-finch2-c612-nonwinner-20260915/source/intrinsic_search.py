"""Rooted-forest SQP with instantaneous dimensionless escape angles.
The floor belongs to the feature identity and is initialized once per phase.
In particular shortening an edge cannot by itself improve its negative angle.
"""
import os
os.environ['OPENBLAS_NUM_THREADS']='1'
import argparse,json,time
from pathlib import Path
import numpy as np
from coupled import Model as FixedModel
from stratum_search import correct
from forest_search import freeze
class Model(FixedModel):
 def eval(self,z,deriv=False):
  a=super().eval(z,deriv);r=a['x']-a['g'];e=a['x'][self.vj]-a['x'][self.vi];rn=np.linalg.norm(r[self.vi],axis=1);en=np.linalg.norm(e,axis=1);factor=self.vlens/(rn*en)
  if deriv:
   dr=a['dx']-a['dg'];de=a['dx'][self.vj]-a['dx'][self.vi];dlog=np.einsum('ik,ikp->ip',r[self.vi],dr[self.vi])/rn[:,None]**2+np.einsum('ik,ikp->ip',e,de)/en[:,None]**2
   a['dvert']=factor[:,None]*(a['dvert']-a['vert'][:,None]*dlog)
  a['vert']=a['vert']*factor
  return a

def main():
 p=argparse.ArgumentParser();p.add_argument('--gen',default='INHERIT1_GENERATOR.json');p.add_argument('--report',default='INHERIT1_A.json');p.add_argument('--tag',default='ANGLE1');p.add_argument('--steps',type=int,default=5);p.add_argument('--step',type=float,default=.01);p.add_argument('--start');p.add_argument('--beta',type=float,default=0);p.add_argument('--floor',type=float,default=1e-8);a=p.parse_args()
 m=Model(json.load(open(a.gen)),json.load(open(a.report)),forced={82:85});e=m.eval(m.z0);m.locked_v=m.select(e)[0];m.vfloor=np.maximum(m.vfloor,a.floor);su={int(m.vi[k]):int(m.vj[k]) for k in m.locked_v};su.update(m.forced);m.basin=[]
 for v in range(len(m.X0)):
  seen=set();j=v;inside=False
  while j!=m.root:assert j not in seen;seen.add(j);inside|=j==82;j=su[j]
  if inside:m.basin.append(v)
 z=m.z0.copy() if a.start is None else np.load(a.start);step=a.step;logs=[];t0=time.time()
 for it in range(a.steps):
  old=m.eval(z);level=np.minimum(2e-6,old['vert'][m.target_idx]+step);zz,b,ok,cor=correct(m,z,level,a.beta,limit=20)
  log=dict(iteration=it,accepted=ok,step=step,level=level.tolist(),target=b['vert'][m.target_idx].tolist(),cmin=float(m.constr(b).min()),g=b['g'].tolist(),volume=float(b['volume']),inner=cor,elapsed=time.time()-t0)
  if ok:z=zz;step=min(.02,step*1.25);np.save(a.tag+'.npy',z);freeze(m,z,a.tag+'_GENERATOR.json')
  else:step*=.5
  logs.append(log);Path(a.tag+'_TRACE.json').write_text(json.dumps(logs));print(json.dumps({k:v for k,v in log.items() if k!='inner'}),flush=True)
  if ok and b['vert'][m.target_idx].min()>1e-8:print('NUMERICAL_POSITIVE',m.census(b),flush=True);break
 print('FINISHED',m.census(m.eval(z)),flush=True)
if __name__=='__main__':main()
