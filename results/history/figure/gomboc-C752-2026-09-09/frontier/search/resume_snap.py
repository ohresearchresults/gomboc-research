"""Resume one literal positive pinned-height checkpoint; no lost partial geometry."""
import os
os.environ['OPENBLAS_NUM_THREADS']='1';os.environ['OMP_NUM_THREADS']='1'
import argparse,json,numpy as np
from pathlib import Path
from fast_mass_engine import load,repair,checkpoint,geom,ERR
p=argparse.ArgumentParser();p.add_argument('input');p.add_argument('out');p.add_argument('--steps',type=int,default=50);p.add_argument('--continuation-steps',type=int,default=100);a=p.parse_args();meta=json.loads(Path(a.input).read_text());q,ll=load(a.input);i=ll.index(meta['pinned_original']);out=Path(a.out);out.mkdir(exist_ok=True,parents=True);dz=.008
for it in range(a.continuation_steps):
 h=q[i,2];target=min(1.,h+dz);x=q.copy();x[i,2]=target
 try:x,f,hist=repair(x,ll.index(3),a.steps,2e-6,.001,pins={i:target});G=geom(x);cc=[len(G[k]) for k in ('S','U','H')]
 except ERR:f=-1.;cc=[-1]*3
 print('RESUME_PIN',it,target,cc,f,flush=True)
 if cc==[1,1,0] and f>3e-7:
  q=x;dz=min(.03,dz*1.25);checkpoint(q,ll,out/'partial.json',pinned_original=ll[i],pinned_z=target)
  if target==1:
   active=G['active'];checkpoint(q[active],[ll[int(j)] for j in active],out/'accepted.json');print('PIN_CONTACT_ACCEPTED',flush=True);break
 else:
  dz=.5*(target-h)
  if dz<1e-7:break
