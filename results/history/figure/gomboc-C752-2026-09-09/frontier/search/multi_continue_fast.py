import os
os.environ['OPENBLAS_NUM_THREADS']='1';os.environ['OMP_NUM_THREADS']='1'
import argparse,json,numpy as np
from pathlib import Path
from fast_mass_engine import load,repair,checkpoint,geom,ERR
p=argparse.ArgumentParser();p.add_argument('input');p.add_argument('out');p.add_argument('--steps',type=int,default=45);p.add_argument('--continuation-steps',type=int,default=120);a=p.parse_args();meta=json.loads(Path(a.input).read_text());q,ll=load(a.input);out=Path(a.out);out.mkdir(exist_ok=True,parents=True);spec=[]
for s in meta['links']:spec.append((ll.index(s['original_row']),np.array([ll.index(j) for j in s['neighbors']]),np.array(s['weights']),np.array(s['anchor'])))
ids=[s[0] for s in spec];keep=[j for j in range(len(q)) if j not in ids];llkeep=[ll[j] for j in keep];lam=meta['lambda_value'];dl=.025;hist=[]
print('MULTI_CONTINUE_START',[ll[i] for i in ids],lam,flush=True)
for it in range(a.continuation_steps):
 goal=min(1.,lam+dl);x=q.copy();links=[]
 for i,js,w,anchor in spec:
  x[i]=(1-goal)*anchor+goal*w@x[js];links.append((i,js,w,goal,anchor))
  if anchor[2]==1 and np.all(x[js,2]==1):x[i,2]=1.
 try:
  if goal==1:x=x[keep];x,f,h=repair(x,llkeep.index(3),a.steps,2e-6,.001)
  else:x,f,h=repair(x,ll.index(3),a.steps,2e-6,.001,links=links)
  G=geom(x);cc=[len(G[k]) for k in ('S','U','H')];vef=[G[k] for k in ('V','E','F')]
 except ERR:f=-1.;h=[];cc=[-1]*3;vef=[]
 hist.append(dict(iteration=it,lambda_value=goal,minimum=f,VEF=vef,counts=cc,history=h));(out/'history.json').write_text(json.dumps(hist));print('MULTI_CONTINUE_STEP',it,goal,vef,cc,f,flush=True)
 if cc==[1,1,0] and f>3e-7:
  if goal==1:
   active=G['active'];x=x[active];llkeep=[llkeep[int(j)] for j in active];checkpoint(x,llkeep,out/'accepted_REMOVAL.json');print('MULTI_CONTINUE_REMOVAL_ACCEPTED',flush=True);break
  q=x;lam=goal;dl=min(.1,dl*1.25);checkpoint(q,ll,out/'partial.json',lambda_value=lam,links=meta['links'])
 else:
  dl=.5*(goal-lam)
  if dl<1e-7:break
print('MULTI_CONTINUE_END',lam,flush=True)
