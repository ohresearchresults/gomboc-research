"""Numerical contact repair with non-decaying geometric and mechanical reserves.
Maximize fractional escape closure; separate working and hard reserves to avoid second-order boundary stalling.
"""
import json,argparse,time
from pathlib import Path
import numpy as np
from scipy.linalg import svd
from scipy.optimize import linprog
from contact_model import Model
p=argparse.ArgumentParser();p.add_argument('--gen',required=True);p.add_argument('--top',required=True);p.add_argument('--prefix',required=True);p.add_argument('--steps',type=int,default=250);p.add_argument('--trust',type=float,default=.002);p.add_argument('--floor',type=float,default=2e-6);a=p.parse_args()
m=Model(json.load(open(a.gen)),json.load(open(a.top)));x=m.x0.copy();trust=a.trust;G=m.geom(x);vv,ff=np.where(m.mask);sl0=(1-G['P']@G['q'].T)[vv,ff];floors=np.minimum(sl0*.1,1e-6);assert min(sl0)>0
best=-1e10;start=time.time()
for step in range(a.steps):
 G=m.geom(x);v,J,_=m.witness(G);st=m.stat(G);print(step,round(time.time()-start,2),'trust',trust,st,flush=True)
 if st['min_escape']>best:best=st['min_escape'];m.save(x,a.prefix+'_best.json')
 _,s,vt=svd(G['J'].reshape(-1,m.k),full_matrices=False,check_finite=False);W=vt.T/np.maximum(s,1e-6)
 bad=v<a.floor;target=np.full(len(v),a.floor);coeff=np.where(bad,a.floor-v,0);BU=np.where(bad,0,v-a.floor)
 # Rescale the progress variable so typical J columns and its column agree.
 # The reported tau is dimensionless and cannot exceed complete closure.
 if bad.any():cs=max(a.floor-v.min(),a.floor)
 else:cs=1;coeff=np.ones(len(v));BU=v.copy()
 AU=np.column_stack([-J@W,coeff/cs])
 sl=(1-G['P']@G['q'].T)[vv,ff];sel=np.argsort(sl-floors)[:1800];ii=vv[sel];jj=ff[sel]
 sJ=-(np.einsum('ikp,ik->ip',G['PJ'][ii],G['q'][jj])+np.einsum('ikp,ik->ip',G['qJ'][jj],G['P'][ii]));AU=np.vstack([AU,np.column_stack([-sJ@W,np.zeros(len(sel))])]);BU=np.r_[BU,sl[sel]-floors[sel]]
 scale=np.maximum(np.linalg.norm(AU[:,:-1],axis=1),1e-3);AU/=scale[:,None];BU/=scale
 obj=np.zeros(m.k+1);obj[-1]=-1;lim=trust/np.sqrt(m.k)
 r=linprog(obj,A_ub=AU,b_ub=BU,bounds=[(-lim,lim)]*m.k+[(0,cs if bad.any() else .1)],method='highs',options={'dual_feasibility_tolerance':1e-9,'primal_feasibility_tolerance':1e-9})
 if not r.success:trust*=.5;print('LPfail',r.message,flush=True);continue
 dx=W@r.x[:-1];tau=r.x[-1]/cs;accepted=False
 for h in range(22):
  alpha=2.**(-h)
  try:GN=m.geom(x+alpha*dx,False);vn,_,_=m.witness(GN);ns=(1-GN['P']@GN['q'].T)[vv,ff]
  except (ValueError,np.linalg.LinAlgError):continue
  if not np.all(np.isfinite(vn)) or min(ns-.25*floors)<-1e-12:continue
  if bad.any():
   if np.any(vn[~bad]<a.floor*.25-1e-12):continue
   if np.any(vn[bad]-v[bad]<.06*alpha*tau*(a.floor-v[bad])-1e-12):continue
  elif vn.min()<v.min()+.04*alpha*(r.x[-1]-v.min())-1e-12:continue
  x+=alpha*dx;accepted=True;print('ACCEPT',alpha,'tau',tau,'min',vn.min(),flush=True)
  if h==0:trust=min(trust*1.12,.03)
  elif h>3:trust=max(trust*.7,1e-9)
  break
 if not accepted:trust*=.5;print('NO_STEP',tau,flush=True)
 m.save(x,a.prefix+'_last.json')
 if trust<1e-9 or (not bad.any() and st['min_escape']>1.2e-4):break
print('FINISHED',m.stat(m.geom(x,False)),flush=True)
