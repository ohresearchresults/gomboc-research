"""Delete real maximal facets by supported convex-combination homotopies.
Each accepted body has a recomputed filled-volume centroid and full positive
physical/polar escape forests. Numerical discovery only; use exact auditors.
"""
import os
os.environ['OPENBLAS_NUM_THREADS']='1';os.environ['OMP_NUM_THREADS']='1'
import sys,json,argparse,numpy as np
from pathlib import Path
from scipy.spatial import ConvexHull
from fast_mass_engine import load,repair,checkpoint,geom,ERR

def closest_triangle(p,T):
 a,b,c=T;M=np.array([b-a,c-a]).T;uv=np.linalg.lstsq(M,p-a,rcond=None)[0];w0=[1-uv.sum(),uv[0],uv[1]];poss=[]
 if min(w0)>=0:poss.append(np.array(w0))
 for i,j in [(0,1),(1,2),(2,0)]:
  d=T[j]-T[i];t=np.clip((p-T[i])@d/(d@d),0,1);w=np.zeros(3);w[i]=1-t;w[j]=t;poss.append(w)
 w=min(poss,key=lambda w:np.linalg.norm(w@T-p));return np.linalg.norm(w@T-p),w

def proposal(q,i):
 if q[i,2]==1:
  ids=np.flatnonzero((q[:,2]==1)&(np.arange(len(q))!=i));h=ConvexHull(q[ids,:2]);best=None
  for edge in h.simplices:
   js=ids[edge];a,b=q[js];d=b-a;t=np.clip((q[i]-a)@d/(d@d),0,1);w=np.array([1-t,t]);dd=np.linalg.norm(w@q[js]-q[i]);z=(dd,js,w)
   if best is None or dd<best[0]:best=z
 else:
  keep=np.array([j for j in range(len(q)) if j!=i]);h=ConvexHull(q[keep]);best=None
  for tri in h.simplices:
   js=keep[tri];dd,w=closest_triangle(q[i],q[js]);z=(dd,js,w)
   if best is None or dd<best[0]:best=z
 dd,js,w=best;w[w<1e-10]=0.;w=w/w.sum();sel=w>0;return dd,js[sel],w[sel]

p=argparse.ArgumentParser();p.add_argument('input');p.add_argument('out');p.add_argument('--stages',type=int,default=50);p.add_argument('--steps',type=int,default=45);p.add_argument('--candidates',type=int,default=5);a=p.parse_args();q,labels=load(a.input);out=Path(a.out);out.mkdir(exist_ok=True,parents=True);hist=[]
for outer in range(a.stages):
 old=geom(q);oldE=old['E'];props=[]
 for i in range(len(q)):
  if labels[i]==3:continue
  try:dist,js,w=proposal(q,i);props.append((dist/np.linalg.norm(q[i]),i,js,w))
  except ERR:continue
 props.sort(key=lambda z:z[0]);accepted=False
 for attempt,(distance,i,js,w) in enumerate(props[:a.candidates]):
  z=q.copy();anchor=z[i].copy();lam=0.;dl=.2;keep=[j for j in range(len(q)) if j!=i];tr=[];label=labels[i]
  print('COALESCE_START',outer,attempt,'row',label,'distance',distance,'neighbors',[labels[j] for j in js],'weights',w.tolist(),flush=True)
  for inner in range(100):
   goal=min(1.,lam+dl);x=z.copy();x[i]=(1-goal)*anchor+goal*(w@x[js]);isroot=anchor[2]==1 and np.all(x[js,2]==1)
   if isroot:x[i,2]=1.
   try:
    if goal==1:
     ll=[labels[j] for j in keep];x=x[keep];x,f,h=repair(x,ll.index(3),a.steps,2e-6,.001)
    else:x,f,h=repair(x,labels.index(3),a.steps,2e-6,.001,link=(i,js,w,goal,anchor))
    G=geom(x);cc=[len(G[k]) for k in ('S','U','H')];vef=[G[k] for k in ('V','E','F')]
   except ERR:f=-1.;h=[];cc=[-1]*3;vef=[]
   rr=dict(inner=inner,lambda_value=goal,minimum=f,counts=cc,VEF=vef,history=h);tr.append(rr);print('COALESCE_STEP',outer,label,goal,vef,cc,f,flush=True)
   if cc==[1,1,0] and f>3e-7:
    if goal==1:
     aa=G['active'];accepted=G['E']<oldE
     if accepted:q=x[aa];labels=[ll[int(j)] for j in aa]
     if accepted:checkpoint(q,labels,out/f'accepted_{outer:02}.json',removed_original=label);checkpoint(q,labels,out/'accepted.json',removed_original=label)
     print('COALESCE_ACCEPTED',outer,label,vef,flush=True);break
    z=x;lam=goal;dl=min(.4,dl*1.4);checkpoint(z,labels,out/'partial.json',lambda_value=lam,removed_original_candidate=label,neighbors=[labels[j] for j in js],weights=w.tolist(),anchor=anchor.tolist())
   else:
    dl*=.5
    if dl<1e-5:break
  hist.append(dict(outer=outer,attempt=attempt,removed_candidate=label,distance=distance,history=tr));(out/'history.json').write_text(json.dumps(hist))
  if accepted:break
 if not accepted:break
print('COALESCE_SEQUENCE_END',flush=True)
