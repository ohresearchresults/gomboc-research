"""Sequential non-simple contact creation by pinned-normal-height continuation.
The pin is exact at every floating step; actual filled mass is recomputed.
Only a separately rationalized, fully audited body is an exact result.
"""
import os
os.environ['OPENBLAS_NUM_THREADS']='1';os.environ['OMP_NUM_THREADS']='1'
import sys,json,argparse,numpy as np
from pathlib import Path
from fast_mass_engine import load,repair,checkpoint,geom,data,ERR
p=argparse.ArgumentParser();p.add_argument('input');p.add_argument('out');p.add_argument('--stages',type=int,default=20);p.add_argument('--steps',type=int,default=45);p.add_argument('--candidates',type=int,default=4);a=p.parse_args();q,labels=load(a.input);out=Path(a.out);out.mkdir(exist_ok=True,parents=True);hist=[]
for outer in range(a.stages):
 G=geom(q);oldE=G['E'];proposals=[]
 for i in np.flatnonzero((q[:,2]<1)&(q[:,2]>.55)):
  if labels[i]==3:continue
  z=q.copy();z[i,2]=1.
  try:
   H=geom(z);f=float(data(H,labels.index(3),False)[0].min())
   if H['E']<oldE:proposals.append((f,int(i)))
  except ERR:pass
 proposals.sort(reverse=True);accepted=False
 for attempt,(_,i) in enumerate(proposals[:a.candidates]):
  z=q.copy();dz=.004;tr=[];initial_z=z[i,2];original=labels[i]
  print('HOMOTOPY_START',outer,attempt,original,initial_z,oldE,flush=True)
  for inner in range(100):
   if z[i,2]==1:break
   target=min(1.,z[i,2]+dz);w=z.copy();w[i,2]=target
   try:w,f,h=repair(w,labels.index(3),a.steps,2e-6,.001,pins={i:target});H=geom(w);cc=[len(H[k]) for k in ('S','U','H')]
   except ERR as e:f=-1.;h=[];cc=[-1]*3
   rr=dict(inner=inner,target=target,minimum=f,counts=cc,history=h);tr.append(rr)
   print('PIN',outer,original,inner,target,cc,f,flush=True)
   if cc==[1,1,0] and f>3e-7:
    z=w;checkpoint(z,labels,out/'partial.json',pinned_original=original,pinned_z=target,history=tr);dz=min(.03,dz*1.4)
   else:
    dz*=.5
    if dz<1e-6:break
  H=geom(z);rec=dict(outer=outer,attempt=attempt,original=original,from_z=initial_z,to_z=z[i,2],VEF=[H[k] for k in ('V','E','F')],history=tr);hist.append(rec);(out/'history.json').write_text(json.dumps(hist))
  if z[i,2]==1 and H['E']<oldE:
   active=H['active'];q=z[active];labels=[labels[int(j)] for j in active];accepted=True
   checkpoint(q,labels,out/f'accepted_{outer:02}.json',snapped_original=original);checkpoint(q,labels,out/'accepted.json',snapped_original=original)
   print('HOMOTOPY_ACCEPTED',outer,original,[H[k] for k in ('V','E','F')],flush=True);break
 if not accepted:break
print('HOMOTOPY_SEQUENCE_END',flush=True)
