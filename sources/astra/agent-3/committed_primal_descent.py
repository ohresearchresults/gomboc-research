"""Reduce P while preserving the basin transfers already realized physically.
Every accepted body has its own integrated mass. Monotone P and committed
positive reachability are separate finite acceptance conditions.
"""
import argparse,json,time
from pathlib import Path
import numpy as np
from scipy.optimize import linprog,minimize,LinearConstraint,Bounds
from primal_basin_transfer import state,derivatives,healthy,OPT
from projected_p_flow_max import retract
from constrained_p_flow import feature

def run(source,out,steps):
 out=Path(out);out.mkdir(parents=True,exist_ok=False);X=np.load(source);e=state(X);elder=e['elder'];committed=np.flatnonzero(e['reach']);np.save(out/'initial.npy',X);(out/'committed.json').write_text(json.dumps(dict(elder=elder,points=committed.tolist(),source=source)));hist=[];start=time.time();trust=.03
 for it in range(steps):
  e=state(X,elder);value,grad,roots,edge=feature(e['g']);junior=next(int(i)for i in e['U']if i!=elder);target=(junior,elder);guards,J,_,_,W,junior=derivatives(e,target);row=dict(it=it,P=value,committed_count=len(committed),reachable=int(e['reach'].sum()),S=len(e['S']),U=len(e['U']),V=len(e['g']['vertices']),trust=trust,seconds=time.time()-start);hist.append(row);np.save(out/'latest.npy',X);(out/'history.json').write_text(json.dumps(hist,indent=2))
  if it%10==0:print('COMMITTED_PRIMAL_DESCENT',out,row,flush=True)
  d=X.size;A=J@W;G=grad@W;floor=1e-7;bound=trust/np.sqrt(d);lp=linprog(G,A_ub=-A,b_ub=guards-floor,bounds=[(-bound,bound)]*d,method='highs',options=OPT)
  if not lp.success or -G@lp.x<1e-11:
   trust*=.4
   if trust<1e-8:break
   continue
  desired=-.7*(G@lp.x);qp=minimize(lambda t:(.5*t@t,t),lp.x*.7,jac=True,method='SLSQP',bounds=Bounds(-bound,bound),constraints=[LinearConstraint(A,floor-guards,np.inf),LinearConstraint(-G,desired,np.inf)],options=dict(maxiter=60,ftol=1e-13))
  if min(A@qp.x+guards-floor)<-1e-8 or -G@qp.x<desired-1e-8:
   trust*=.4
   if trust<1e-8:break
   continue
  dx=(W@qp.x).reshape(X.shape);ok=False
  for k in range(15):
   Y=X+2.**-k*dx
   try:
    ee=state(Y,elder,False)
    if len(ee['S'])==len(ee['U'])==1:
     from goal_nomination import preserve
     preserve(Y,out/f'goal_nomination_it{it}_k{k}','committedPdescentactualS1U1')
    if k<2 and not healthy(ee,committed):Y,good,corr=retract(Y,[elder,junior],1e-7,limit=12);ee=state(Y,elder,False)
   except (ValueError,np.linalg.LinAlgError):continue
   if len(ee['S'])==len(ee['U'])==1:
    from goal_nomination import preserve
    preserve(Y,out/f'goal_nomination_after_correction_it{it}_k{k}','committedPdescentretractionactualS1U1')
   val=feature(ee['g'],False)[0]
   if elder in ee['U'] and healthy(ee,committed) and val<value-max(1e-11,value*1e-7):X=Y;ok=True;row['alpha']=2.**-k;break
  if ok and k==0:trust=min(.3,trust*1.3)
  if not ok:trust*=.4
  if trust<1e-8:break
 print('COMMITTED_PRIMAL_DESCENT_DONE',out,hist[-1],flush=True)

if __name__=='__main__':
 p=argparse.ArgumentParser();p.add_argument('input');p.add_argument('out');p.add_argument('--steps',type=int,default=300);a=p.parse_args();run(a.input,a.out,a.steps)
