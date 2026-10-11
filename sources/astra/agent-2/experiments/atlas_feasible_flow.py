"""Convexity-constrained physical flow in a fixed contact atlas.
Every nonlinear step rechecks all nonincidences and real face orientations.
Linear programming directions use actual-volume persistence gradients.
"""
import sys,json,time,numpy as np
from scipy.linalg import svd
from scipy.optimize import linprog
import jax
import jax.numpy as jnp
from contact_atlas import ROOT,Chart
from geometry import angular_scores

def run(folder,out,iters=2000,tau=-1.,startpath=None):
 c=Chart(folder);q=c.q.copy() if startpath is None else np.load(startpath);out.mkdir(parents=True,exist_ok=True);inc=c.incidence;flat=np.flatnonzero(~inc.ravel());F=c.F;V=c.meta['V'];K=len(flat)
 def differential(q):
  X,Y,Z,Q,cent,vol,gaps=c.physical(q);return jnp.concatenate([gaps.ravel()[flat],X.ravel(),Y.ravel()])
 jj=jax.jit(jax.jacfwd(differential));trust=.02;hist=[];start=time.time();floor=1e-7
 for it in range(iters):
  g=c.graph(q);v,grad=c.lossgrad(q,g['bp'],g['bw'],g['bq'],g['qw'],tau,0.);v=float(v);grad=np.asarray(grad);u=angular_scores(g['Z']).max(1);s=angular_scores(g['Q']).max(1);row=dict(it=it,loss=v,S=int((s<0).sum()),U=int((u<0).sum()),minimum_noncontact=g['minimum'],trust=trust,seconds=time.time()-start,tau=tau);hist.append(row);np.save(out/'latest_q.npy',q);(out/'history.json').write_text(json.dumps(hist,indent=2)+'\n')
  if it%10==0:print('ATLAS_FLOW',row,flush=True)
  if row['S']==row['U']==1 and min(np.sort(u)[1],np.sort(s)[1])>1e-9:
   np.save(out/'NUMERICAL_NOMINATION_q.npy',q);(out/'NUMERICAL_NOMINATION.json').write_text(json.dumps(row,indent=2)+'\n');print('NUMERICAL_GOAL_NOMINATION_REQUIRES_EXACT',row,flush=True);break
  J=np.asarray(jj(q));gaps=(1-g['Y']@g['X'].T).ravel()[flat];D=len(q);scaleX=np.sqrt(np.mean(g['X']**2));scaleY=np.sqrt(np.mean(g['Y']**2));metric=np.vstack([J[K:K+3*V]/scaleX,J[K+3*V:]/scaleY,np.eye(D)*.05]);_,dd,Vt=svd(metric,full_matrices=False,check_finite=False);W=Vt.T/dd
  # All nonincident pairs are included: no unrecorded relaxed contacts.
  lp=linprog(grad@W,A_ub=-(J[:K]@W),b_ub=gaps-floor,bounds=[(-trust/np.sqrt(D),trust/np.sqrt(D))]*D,method='highs',options={'primal_feasibility_tolerance':1e-9,'dual_feasibility_tolerance':1e-9})
  if not lp.success:row['LP']=lp.message;trust*=.5;continue
  dq=W@lp.x;direction=float(grad@dq);accepted=False
  for back in range(18):
   qq=q+dq*2**-back
   try:
    gg=c.graph(qq)
    if gg['minimum']<.9*floor:continue
    vv=float(c.lossgrad(qq,gg['bp'],gg['bw'],gg['bq'],gg['qw'],tau,0.)[0])
   except (ValueError,np.linalg.LinAlgError):continue
   if vv<v+1e-4*2**-back*direction:q=qq;accepted=True;row['alpha']=2**-back;break
  if accepted and back==0:trust=min(.3,trust*1.15)
  if not accepted:trust*=.4
  if trust<1e-10:print('FLOW_STALLED',row,flush=True);break
 return q
if __name__=='__main__':
 folder=ROOT/(sys.argv[1] if len(sys.argv)>1 else 'artifacts/contact_atlas/exact_iteration16');out=folder/(sys.argv[2] if len(sys.argv)>2 else 'feasible_flow');tau=float(sys.argv[3]) if len(sys.argv)>3 else -1.;run(folder,out,tau=tau,startpath=(folder/sys.argv[4]) if len(sys.argv)>4 else None)
