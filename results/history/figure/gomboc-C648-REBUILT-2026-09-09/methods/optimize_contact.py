"""Simultaneous positive-witness repair and conditioning. Numerical discovery."""
import json, argparse, time
import numpy as np
from pathlib import Path
from scipy.linalg import svd
from scipy.optimize import linprog
from contact_model import Model
p=argparse.ArgumentParser();p.add_argument('--gen',default='SEED36.json');p.add_argument('--top',default='TOP36.json');p.add_argument('--prefix',default='repair36');p.add_argument('--steps',type=int,default=100);p.add_argument('--trust',type=float,default=.002);p.add_argument('--floor',type=float,default=2e-6);args=p.parse_args()
m=Model(json.load(open(args.gen)),json.load(open(args.top)));x=m.x0.copy();trust=args.trust;t0=time.time();best=-1e10
for step in range(args.steps):
 G=m.geom(x);v,J,wit=m.witness(G);st=m.stat(G);print(step,'seconds',round(time.time()-t0,2),'trust',trust,st,flush=True)
 if st['min_escape']>best:
  best=st['min_escape'];m.save(x,args.prefix+'_best.json');np.save(args.prefix+'_best.npy',x)
 if st['slack']<=0:raise ValueError('invalid initial topology')
 A=G['J'].reshape(-1,m.k);_,s,vt=svd(A,full_matrices=False,check_finite=False);W=vt.T/np.maximum(s,1e-6)
 # Common improvement for currently bad witnesses; all previously positive
 # witnesses have a nonzero retained reserve. After repair maximize all margins.
 bad=v<0
 if np.any(bad):
  coeff=bad.astype(float);target=np.where(bad,v,np.minimum(.7*v,args.floor))
 else:
  coeff=np.ones(len(v));target=np.zeros(len(v))
 Jw=J@W;AU=np.column_stack([-Jw,coeff]);BU=v-target
 sl=1-G['P']@G['q'].T;vv,ff=np.where(m.mask);slvals=sl[vv,ff];sel=np.argsort(slvals)[:1200];ii=vv[sel];jj=ff[sel]
 sJ=-(np.einsum('ikp,ik->ip',G['PJ'][ii],G['q'][jj])+np.einsum('ikp,ik->ip',G['qJ'][jj],G['P'][ii]))
 AU=np.vstack([AU,np.column_stack([-sJ@W,np.zeros(len(ii))])]);BU=np.r_[BU,sl[ii,jj]-np.minimum(sl[ii,jj]*.2,1e-6)]
 # Scale small constraints above solver feasibility tolerance.
 scale=np.maximum(np.linalg.norm(AU[:,:-1],axis=1),1e-3);AU/=scale[:,None];BU/=scale
 obj=np.zeros(m.k+1);obj[-1]=-1
 lim=trust/np.sqrt(m.k)
 r=linprog(obj,A_ub=AU,b_ub=BU,bounds=[(-lim,lim)]*m.k+[(-1.,.1)],method='highs',options={'dual_feasibility_tolerance':1e-8,'primal_feasibility_tolerance':1e-8})
 if not r.success:
  print('LP failure',r.message,flush=True);trust*=.5
  if trust<1e-8:break
  continue
 dx=W@r.x[:-1];pred=r.x[-1];accepted=False
 for halving in range(20):
  alpha=2.**(-halving)
  try:
   GN=m.geom(x+alpha*dx,False);sn=m.stat(GN);vn,_,_=m.witness(GN)
  except (ValueError,np.linalg.LinAlgError):continue
  if sn['slack']<max(1e-9,st['slack']*.08) or not np.all(np.isfinite(vn)):continue
  # Never sacrifice any already-positive witness to fix the current bad one.
  if np.any(bad):
   good=~bad
   if np.any(vn[good]<np.minimum(v[good]*.5,args.floor*.7)):continue
   improvement=vn[bad]-v[bad]
   if improvement.min() < min(alpha*pred*.08,-1e-10):continue
  else:
   if vn.min()<v.min()+.04*alpha*(pred-v.min()):continue
  accepted=True;x+=alpha*dx
  print('ACCEPT','alpha',alpha,'pred',pred,'newmin',vn.min(),flush=True)
  if halving==0:trust=min(trust*1.12,.03)
  elif halving>3:trust=max(trust*.7,1e-8)
  break
 if not accepted:
  trust*=.5;print('BACKTRACK_FAILED',pred,flush=True)
  if trust<1e-8:break
 m.save(x,args.prefix+'_last.json');np.save(args.prefix+'_last.npy',x)
 if not np.any(bad) and st['min_escape']>1.5e-4:break
print('FINISHED',m.stat(m.geom(x,False)),flush=True)
