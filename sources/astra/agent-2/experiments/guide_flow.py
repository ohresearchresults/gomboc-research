"""Feasible sequential linear steps in the full support-coordinate space.
Each accepted step is re-integrated and checked on the actual rebuilt hull.
"""
import sys,json,time
from pathlib import Path
import numpy as np
from scipy.optimize import linprog
from two_root_constrained import TwoRootSearch,ROOT

from guide_constrained import GuideSearch
tag=sys.argv[1];path=Path(sys.argv[2]);guidepath=Path(sys.argv[3]);limit=int(sys.argv[4]) if len(sys.argv)>4 else 2000
Y=np.load(path);out=ROOT/'artifacts/guide_flow'/tag;guide=json.loads(guidepath.read_text())
obj=GuideSearch(Y,out,tau=1e-7,guide=guide)
(out/'guide.json').write_text(json.dumps(guide,indent=2)+'\n')
x=Y.ravel().copy();radius=.001;rows=[];beg=time.time()
for k in range(limit):
 vals,jac=obj.data(x);f=float(vals[0]);c=vals[1:];g=jac[0];J=jac[1:]
 scale=np.maximum(np.linalg.norm(J,axis=1),1e-12);take=scale>1e-10
 # Leave half the required guard as a finite nonlinear reserve.
 floor=min(obj.tau*.5,float(c.min()+obj.tau)*.999)
 rhs=(c+obj.tau-floor)/scale
 columns=np.maximum(np.max(np.abs(J),axis=0),np.abs(g))
 lp_bounds=[(-radius,radius) if v>1e-12 else (0.,0.) for v in columns]
 opt=linprog(g/np.linalg.norm(g),A_ub=-J[take]/scale[take,None],b_ub=rhs[take],bounds=lp_bounds,method='highs',options={'dual_feasibility_tolerance':1e-9,'primal_feasibility_tolerance':1e-9})
 if not opt.success:
  radius*=.5
  if radius<1e-10:print('LP_CHART_STALLED',k,opt.message,flush=True);break
  continue
 step=opt.x;pred=-float(g@step);accepted=False
 if pred<=1e-15:
  radius*=.5
  if radius<1e-10:print('NO_FEASIBLE_DESCENT',k,pred,flush=True);break
  continue
 for back in range(24):
  alpha=2.**(-back);candidate=x+alpha*step;vv,jj=obj.data(candidate)
  if vv[1:].min()+obj.tau>=floor and vv[0]<f-1e-4*alpha*pred:
   reduction=f-float(vv[0]);x=candidate;accepted=True
   if back==0 and reduction>.5*pred:radius=min(radius*1.3,.03)
   elif back>=3:radius=max(radius*.7,1e-10)
   rows.append({'iteration':k,'loss':float(vv[0]),'min_constraint':float(vv[1:].min()),'radius':radius,'alpha':alpha,'predicted':pred,'actual':reduction,'seconds':time.time()-beg})
   np.save(out/'accepted.npy',x.reshape(Y.shape))
   if k%25==0:print('STEP',tag,rows[-1],flush=True)
   break
 if obj.target:print('TARGET_CHECK_REQUIRED',tag,flush=True);break
 if obj.guide_reached:print('ACTUAL_GUIDE_SWITCH',tag,'candidate',str(out/'best.npy'),flush=True);break
 if not accepted:
  radius*=.4
  if radius<1e-10:print('ACTUAL_GUARD_CHART_STALLED',k,flush=True);break
(out/'accepted_steps.json').write_text(json.dumps(rows,indent=2)+'\n')
np.save(out/'final.npy',x.reshape(Y.shape))
print('SLP_FINISHED',tag,len(rows),'best',obj.best,'seconds',time.time()-beg,flush=True)
