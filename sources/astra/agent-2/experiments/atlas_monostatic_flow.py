"""Strict U1/S<=2 contact-preserving own-mass flow from an exact211 body.
Allowed roots are exempt, permitting the second stable root to disappear.
Every other primal/polar point has a strictly positive outward witness.
"""
import sys,json,time,numpy as np
from scipy.linalg import svd
from scipy.optimize import linprog
import jax
import jax.numpy as jnp
from contact_atlas import ROOT,Chart
from bicap_polish import roots,forest
from geometry import angular_scores

def guardians(c,g):
 rr=[roots(g['Z'],np.ones(c.meta['V']),g['bp'],g['bw'],1),roots(g['Q'],np.ones(c.meta['F']),g['bq'],g['qw'],2)];pp=[];active=[];vals=[]
 for A,r in [(g['Z'],rr[0]),(g['Q'],rr[1])]:
  p,s=forest(A,np.ones(len(A)),r);mask=np.ones(len(A),bool);mask[r]=False;v=angular_scores(A)[np.arange(len(A)),p];pp.append(p);active.append(mask);vals.append(v)
 return pp,np.r_[active[0],active[1]],np.r_[vals[0],vals[1]],rr

def run(folder,out,iters=3000):
 c=Chart(folder);q=c.q.copy();F,V=c.meta['F'],c.meta['V'];out.mkdir(parents=True,exist_ok=True);flat=np.flatnonzero(~c.incidence.ravel());K=len(flat)
 def differentiated(q,p,s):
  X,Y,Z,Q,cent,vol,gaps=c.physical(q)
  def angles(A,pp):
   d=A[pp]-A;return jnp.sum(A*d,axis=1)/jnp.sqrt(jnp.sum(A*A,axis=1)*jnp.sum(d*d,axis=1))
  return jnp.concatenate([gaps.ravel()[flat],angles(Z,p),angles(Q,s),X.ravel(),Y.ravel()])
 jj=jax.jit(jax.jacfwd(differentiated,argnums=0));trust=.02;history=[];t0=time.time();gapfloor=1e-7;guardfloor=1e-8
 for it in range(iters):
  g=c.graph(q);pp,active,guards,rr=guardians(c,g);cost,grad=c.lossgrad(q,g['bp'],g['bw'],g['bq'],g['qw'],-1.,0.);cost=float(cost);grad=np.asarray(grad);S=int((angular_scores(g['Q']).max(1)<0).sum());U=int((angular_scores(g['Z']).max(1)<0).sum());row=dict(it=it,S=S,U=U,loss=cost,min_noncontact=g['minimum'],min_guard=float(guards[active].min()),roots=rr,trust=trust,seconds=time.time()-t0);history.append(row);np.save(out/'latest_q.npy',q);(out/'history.json').write_text(json.dumps(history,indent=2)+'\n')
  if it%10==0:print('MONOSTATIC_ATLAS',row,flush=True)
  if S==U==1:
   np.save(out/'NUMERICAL_NOMINATION_q.npy',q);(out/'NUMERICAL_NOMINATION.json').write_text(json.dumps(row,indent=2)+'\n');print('NUMERICAL_REQUIRES_EXACT',row,flush=True);break
  if U>1 or S>2 or guards[active].min()<.8*guardfloor:raise ValueError('starting iterate lost strict required witnesses')
  J=np.asarray(jj(q,pp[0],pp[1]));D=len(q);Jphysical=J[K+V+F:];metric=np.vstack([Jphysical[:3*V]/np.sqrt(np.mean(g['X']**2)),Jphysical[3*V:]/np.sqrt(np.mean(g['Y']**2)),np.eye(D)*.05]);_,dd,Vt=svd(metric,full_matrices=False,check_finite=False);W=Vt.T/dd;gaps=(1-g['Y']@g['X'].T).ravel()[flat];C=np.vstack([J[:K],J[K:K+V+F][active]]);rhs=np.r_[gaps-gapfloor,guards[active]-guardfloor]
  lp=linprog(grad@W,A_ub=-(C@W),b_ub=rhs,bounds=[(-trust/np.sqrt(D),trust/np.sqrt(D))]*D,method='highs',options={'primal_feasibility_tolerance':1e-10,'dual_feasibility_tolerance':1e-9})
  if not lp.success:row['LP']=lp.message;trust*=.5;continue
  dq=W@lp.x;direction=float(grad@dq);accepted=False
  for back in range(20):
   qq=q+dq*2**-back
   try:
    gg=c.graph(qq);p2,a2,v2,r2=guardians(c,gg)
    if gg['minimum']<.9*gapfloor or v2[a2].min()<.9*guardfloor:continue
    vv=float(c.lossgrad(qq,gg['bp'],gg['bw'],gg['bq'],gg['qw'],-1.,0.)[0])
   except (ValueError,np.linalg.LinAlgError):continue
   if vv<cost+1e-4*2**-back*direction:q=qq;accepted=True;row['alpha']=2**-back;break
  if accepted and back==0:trust=min(.3,trust*1.15)
  if not accepted:trust*=.4
  if trust<1e-11:print('STRICT_ATLAS_STALLED',row,flush=True);break
 return q
if __name__=='__main__':
 folder=ROOT/(sys.argv[1] if len(sys.argv)>1 else 'artifacts/contact_atlas/C352');run(folder,folder/'strict_flow')
