import os
os.environ['OPENBLAS_NUM_THREADS']='1';os.environ['OMP_NUM_THREADS']='1'
import argparse,json,numpy as np
from pathlib import Path
from anchor_engine import *
p=argparse.ArgumentParser();p.add_argument('input');p.add_argument('out');p.add_argument('--stages',type=int,default=15);p.add_argument('--steps',type=int,default=50);a=p.parse_args();q,labels=load(a.input);out=Path(a.out);out.mkdir(exist_ok=True,parents=True);meta=json.loads(Path(a.input).read_text());hist=[]
if 'anchor' in meta:
 anchor={'point':np.array([float.fromhex(x) for x in meta['anchor']['point_hex']]),'rows':meta['anchor']['rows']};q=project(q,anchor);checkpoint(q,labels,anchor,out/'initial.json');print('ANCHOR_RESUME',len(anchor['rows']),flush=True)
else:
 G=geom(q);candidates=[]
 for (u,v),edge in G['edges'].items():
  if len(G['source'][u])!=3 or len(G['source'][v])!=3:continue
  if any(q[j,2]==1 for j in set(G['source'][u])|set(G['source'][v])):continue
  if labels.index(3) in set(G['source'][u])|set(G['source'][v]):continue
  # Keep the farther endpoint as the anchor to preserve an outward primal exit.
  if G['Y'][u]@G['Y'][u]<G['Y'][v]@G['Y'][v]:u,v=v,u
  if G['vertex_escape'][u]<1e-6:continue
  i=list(set(G['source'][v])-set(G['source'][u]))[0];pt=G['X'][u]
  candidates.append((1-q[i]@pt,u,i))
 candidates.sort();gap,u,j=candidates[0];anchor={'point':G['X'][u].copy(),'rows':list(G['source'][u])};q=project(q,anchor);hist=[];checkpoint(q,labels,anchor,out/'initial.json')
 print('ANCHOR_INITIAL',anchor['point'].tolist(),[labels[i] for i in anchor['rows']],'first_add',labels[j],'gap',gap,flush=True)
for outer in range(a.stages):
 G=geom(q,anchor=anchor);oldE=G['E'];rr=set(anchor['rows']);props=[]
 for key in G['source']:
  if len(key)==3 and len(set(key)&rr)==2:
   i=list(set(key)-rr)[0]
   if q[i,2]==1 or labels[i]==3:continue
   props.append((1-q[i]@anchor['point'],i))
 props=sorted(set(props));accepted=False
 for gap,i in props[:5]:
  z=q.copy();h=float(z[i]@anchor['point']);dh=min(.002,max(gap/4,1e-7));tr=[]
  print('ANCHOR_START',outer,labels[i],h,flush=True)
  for inner in range(100):
   target=min(1.,h+dh);aa={'point':anchor['point'],'rows':anchor['rows']+([i] if target==1 else [])};pin=None if target==1 else (i,target)
   try:
    x=project(z,aa,pin);x,f,hh=repair(x,labels.index(3),aa,a.steps,2e-6,.001,pin);G2=geom(x,anchor=aa);cc=[len(G2[k]) for k in ('S','U','H')];vef=[G2[k] for k in ('V','E','F')]
   except ERR as e:f=-1.;hh=[];cc=[-1]*3;vef=[]
   print('ANCHOR_STEP',outer,labels[i],target,vef,cc,f,flush=True);tr.append(dict(target=target,minimum=f,counts=cc,VEF=vef,history=hh))
   if cc==[1,1,0] and f>3e-7:
    z=x;h=target;dh=min(.02,dh*1.4)
    if target==1 and G2['E']<oldE:
     q=x;anchor=aa;accepted=True;checkpoint(q,labels,anchor,out/f'accepted_{outer:02}.json');checkpoint(q,labels,anchor,out/'accepted.json');print('ANCHOR_ACCEPTED',outer,vef,'degree',len(anchor['rows']),flush=True);break
    checkpoint(z,labels,aa,out/'partial.json',pin=pin)
   else:
    dh=.5*(target-h)
    if dh<1e-10:break
  hist.append(dict(outer=outer,original_add=labels[i],history=tr));(out/'history.json').write_text(json.dumps(hist))
  if accepted:break
 if not accepted:break
print('ANCHOR_SEQUENCE_END',flush=True)
