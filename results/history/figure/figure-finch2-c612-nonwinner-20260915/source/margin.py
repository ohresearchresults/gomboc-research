"""Expand every protected identity's reserve in a newly declared exact stratum.
No old protected floor is reduced, and the surviving defect cannot get worse.
"""
import os
os.environ['OPENBLAS_NUM_THREADS']='1'
import argparse,json
from pathlib import Path
import numpy as np
from coupled import Model
from stratum_search import correct
from forest_search import freeze

def main():
 p=argparse.ArgumentParser();p.add_argument('--gen',default='INHERIT1_GENERATOR.json');p.add_argument('--report',default='INHERIT1_A.json');p.add_argument('--tau',type=float,default=1e-5);p.add_argument('--tag',default='MARGIN1');p.add_argument('--change',type=float,default=0);p.add_argument('--beta',type=float,default=0);a=p.parse_args()
 m=Model(json.load(open(a.gen)),json.load(open(a.report)),forced={82:85});m.locked_v=m.select(m.eval(m.z0))[0];m.basin=[]
 suc={int(m.vi[k]):int(m.vj[k]) for k in m.locked_v};suc.update(m.forced)
 for v in range(len(m.X0)):
  seen=set();j=v;inside=False
  while j!=m.root:assert j not in seen;seen.add(j);inside|=j==82;j=suc[j]
  if inside:m.basin.append(v)
 m.vfloor[m.vi[m.locked_v]]=np.maximum(m.vfloor[m.vi[m.locked_v]],a.tau)
 ff=[i for i in range(len(m.faces)) if i!=m.sface];m.ffloor[ff]=np.maximum(m.ffloor[ff],a.tau)
 old=m.eval(m.z0);level=old['vert'][m.target_idx]+a.change
 z,e,ok,trace=correct(m,m.z0,level,a.beta,limit=30)
 Path(a.tag+'_TRACE.json').write_text(json.dumps(dict(tau=a.tau,ok=ok,trace=trace,target=e['vert'][m.target_idx].tolist(),cmin=float(m.constr(e).min()))))
 print('STATUS',ok,'target',e['vert'][m.target_idx],'cmin',m.constr(e).min(),'census',m.census(e),flush=True)
 if ok:np.save(a.tag+'.npy',z);freeze(m,z,a.tag+'_GENERATOR.json')
if __name__=='__main__':main()
