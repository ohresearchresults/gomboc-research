"""Denominator-first rational contact-row compression inside actual own-mass gates.
Linearized margins generate candidates; every accepted change is nonlinearly checked.
Exact final geometry/mechanics are audited by the separate A/B implementations.
"""
from pathlib import Path
import argparse,json,time
import numpy as np
from atlas_opt import Atlas
from numeric import recover,mechanics
from simplify56 import screen

def enc(x):return json.dumps(x,sort_keys=True,separators=(',',':'))
def run(a):
 d=json.loads(Path(a.source).read_text());faces=json.loads(Path(a.faces).read_text());md=json.loads(json.dumps(d));md['controls']=(np.array(d['controls'],float)/np.array(d['denominators'])[:,None]).tolist();md['grid']=1;m=Atlas(md,faces)
 out=Path(a.out);out.mkdir(parents=True,exist_ok=False);X=np.array(d['controls'],float)/np.array(d['denominators'])[:,None];u=X[m.free[:,0],m.free[:,1]]/m.scale
 s=m.state(u,False);floors=np.maximum(a.floor,np.minimum(s['vals']*.1,1e-5));rootfloors=[-s['cs'][m.Sroot].max()*.25,-s['cu'][m.Uroot].max()*.25];geo=np.minimum(s['gaps']*.01,1e-6);df=s['det']*.01
 assert s['vals'].min()>a.floor
 hist=[];t=time.monotonic();order=[i for i,deps,axes in d['plan'] if len(axes)<3]
 if a.order=='reverse':order=order[::-1]
 if a.order=='height':order=sorted(order,key=lambda i:-d['denominators'][i])
 for rd in range(a.rounds):
  accepted=0
  for ii,i in enumerate(order):
   cols=np.flatnonzero(m.free[:,0]==i);axes=m.free[cols,1];s=m.state(u);x=u[cols]*m.scale[cols];oldq=d['denominators'][i];J=s['J'][:,cols]/m.scale[cols];slack=s['vals']-floors;found=False
   assert slack.min()>-1e-12
   # Ascending denominators; nearest numerator vector is only a proposal, not
   # exhaustive lattice feasibility. Norm bounds intentionally localize the search.
   for lo in range(1,min(oldq,a.qmax),5000):
    qs=np.arange(lo,min(oldq,a.qmax,lo+5000),dtype=np.int64);ns=np.rint(qs[:,None]*x);delta=ns/qs[:,None]-x
    ids=np.flatnonzero(np.max(np.abs(delta),axis=1)<=a.trust)
    if not len(ids):continue
    good=np.all(delta[ids]@J.T>=-.8*slack[None,:],axis=1);ids=ids[good]
    for k in ids:
     uu=u.copy();uu[cols]=ns[k]/qs[k]/m.scale[cols]
     try:sn=m.state(uu,False)
     except Exception:continue
     if (np.min(sn['vals']-floors)>1e-12 and np.min((sn['gaps']-geo)[~m.inc])>0 and np.min(sn['det']-df)>0 and sn['h'].min()>0 and sn['cs'][m.Sroot].max()<-rootfloors[0] and sn['cu'][m.Uroot].max()<-rootfloors[1]):
      u=uu;d['controls'][i]=[0,0,0]
      for ax,num in zip(axes,ns[k].astype(np.int64)):d['controls'][i][int(ax)]=int(num)
      d['denominators'][i]=int(qs[k]);accepted+=1;found=True;hist.append(dict(round=rd,node=i,old_q=oldq,new_q=int(qs[k]),minimum=float(sn['vals'].min()),maxmove=float(np.max(np.abs(delta[k])))));break
    if found:break
   if ii%20==0:print('PROGRESS',rd,ii,'accept',accepted,'sec',time.monotonic()-t,flush=True)
   (out/'GENERATOR.json').write_text(enc(d));(out/'HISTORY.json').write_text(enc(hist))
  print('ROUND_DONE',rd,accepted,'sec',time.monotonic()-t,flush=True)
  if accepted==0:break
 r=screen(d,faces);(out/'NUMERICAL.json').write_text(enc(r));print('END',r,flush=True)
if __name__=='__main__':
 p=argparse.ArgumentParser();p.add_argument('--parent',default='PARENT_G8.json');p.add_argument('--source',default='ADAPT_E8/GENERATOR.json');p.add_argument('--faces',default='FACES.json');p.add_argument('--out',required=True);p.add_argument('--rounds',type=int,default=1);p.add_argument('--floor',type=float,default=5e-7);p.add_argument('--trust',type=float,default=1e-5);p.add_argument('--qmax',type=int,default=2000000);p.add_argument('--order',choices=['plan','reverse','height'],default='reverse');run(p.parse_args())
