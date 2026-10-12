"""Full actual-mass predictor/corrector flow in a fixed physical contact chart.
Keeps every vertex except one and every facet except two strictly nonequilibrial.
The allowed second stable root may disappear; no fake zero or bar cutoff exists.
"""
import sys,json,time,numpy as np
from scipy.linalg import svd
from scipy.optimize import linprog
from scipy.sparse import csr_matrix,hstack,vstack,eye
import jax
import jax.numpy as jnp
from canonical_atlas import ROOT,Chart
from support_persistence import barcode
from geometry import angular_scores

def run(folder,out,inputpath,iters=1500,eps=1e-7):
 c=Chart(folder);q=np.load(inputpath);out.mkdir(parents=True,exist_ok=True);V,F=c.meta['V'],c.F;D=len(q);flat=np.flatnonzero(~c.incidence.ravel());K=len(flat);nm=V+F;gapfloor=1e-8;trust=.02;history=[];start=time.time();g=c.graph(q);ur=int(np.argmax((g['Z']**2).sum(1)));sr=int(np.argmax((g['Q']**2).sum(1)));bp,bw,bars=barcode(g['Q'],np.ones(F),c.es);child=int(bp[np.argmax(bars),0]);rr=[[ur],[sr,child]];active=np.ones(nm,bool);active[ur]=False;active[V+np.array(rr[1])]=False;ng=int(active.sum());(out/'roots.json').write_text(json.dumps(rr))
 def pieces(q,up,sp):
  X,Y,Z,Q,cent,vol,gap=c.physical(q)
  def angles(A,p):
   d=A[p]-A;return jnp.sum(A*d,axis=1)/jnp.sqrt(jnp.maximum(jnp.sum(A*A,axis=1)*jnp.sum(d*d,axis=1),1e-40))
  return jnp.concatenate([gap.ravel()[flat],angles(Z,up),angles(Q,sp),X.ravel(),Y.ravel()])
 jac=jax.jit(jax.jacfwd(pieces,argnums=0))
 def state(q):
  g=c.graph(q);up=angular_scores(g['Z']).argmax(1);sp=angular_scores(g['Q']).argmax(1);guards=np.r_[angular_scores(g['Z'])[np.arange(V),up],angular_scores(g['Q'])[np.arange(F),sp]];cost,gradient=c.lossgrad(q,g['bp'],g['bw'],g['bq'],g['qw'],-1.,0.);return g,up,sp,guards,float(cost),np.asarray(gradient)
 def retract(q,up,sp,W,radius):
  for correction in range(8):
   raw=np.asarray(pieces(q,up,sp));gap=raw[:K];gg=raw[K:K+nm][active]
   if not np.isfinite(raw).all():return None
   if gap.min()>.999*gapfloor and gg.min()>.999*eps:return q
   J=np.asarray(jac(q,up,sp));C=np.vstack([J[:K],J[K:K+nm][active]])@W;target=np.r_[np.full(K,gapfloor),np.full(ng,eps)];values=np.r_[gap,gg];row_scale=np.r_[np.ones(K),np.full(ng,1000.)];I=eye(D);A=vstack([hstack([-csr_matrix(C*row_scale[:,None]),csr_matrix((len(C),D))]),hstack([I,-I]),hstack([-I,-I])],format='csr');b=np.r_[(values-target)*row_scale,np.zeros(2*D)]
   lp=linprog(np.r_[np.zeros(D),np.ones(D)],A_ub=A,b_ub=b,bounds=[(-radius/np.sqrt(D),radius/np.sqrt(D))]*D+[(0,None)]*D,method='highs-ipm',options={'primal_feasibility_tolerance':1e-10,'dual_feasibility_tolerance':1e-9,'time_limit':10.})
   if not lp.success:return None
   q=q+W@lp.x[:D]
  return None
 for it in range(iters):
  g,up,sp,guards,cost,grad=state(q);S=int((angular_scores(g['Q']).max(1)<0).sum());U=int((angular_scores(g['Z']).max(1)<0).sum());row=dict(it=it,S=S,U=U,minimum=float(guards[active].min()),main_Q=float(np.sqrt(cost)),centroid=g['c'].tolist(),loss=cost,trust=trust,seconds=time.time()-start);history.append(row);np.save(out/'latest_q.npy',q);(out/'history.json').write_text(json.dumps(history,indent=2)+'\n')
  if it%5==0:print('OWN_STRICT_FLOW',row,flush=True)
  if S==U==1:
   np.save(out/'NUMERICAL_NOMINATION_q.npy',q);(out/'NUMERICAL_NOMINATION.json').write_text(json.dumps(row,indent=2)+'\n');print('NUMERICAL_REQUIRES_EXACT',row,flush=True);break
  if S>2 or U>1 or guards[active].min()<.8*eps:raise ValueError('iterate does not satisfy promised strict own root constraints')
  J=np.asarray(jac(q,up,sp));jp=J[K+nm:];metric=np.vstack([jp[:3*V]/np.sqrt(np.mean(g['X']**2)),jp[3*V:]/np.sqrt(np.mean(g['Y']**2)),np.eye(D)*.05]);_,dd,Vt=svd(metric,full_matrices=False,check_finite=False);W=Vt.T/dd;gap=(1-g['Y']@g['X'].T).ravel()[flat];C=np.vstack([J[:K],J[K:K+nm][active]])@W;rhs=np.r_[gap-gapfloor,guards[active]-eps];row_scale=np.r_[np.ones(K),np.full(ng,1000.)];lp=linprog(grad@W,A_ub=-C*row_scale[:,None],b_ub=rhs*row_scale,bounds=[(-trust/np.sqrt(D),trust/np.sqrt(D))]*D,method='highs-ipm',options={'primal_feasibility_tolerance':1e-10,'dual_feasibility_tolerance':1e-9,'time_limit':10.})
  if not lp.success:
   trust*=.5;row['LP']=lp.message
   if trust<1e-11:print('LP_TRUST_EXHAUSTED',row,flush=True);break
   continue
  dq=W@lp.x;accepted=False
  for back in range(18):
   qq=retract(q+2**-back*dq,up,sp,W,max(trust*2**-back,1e-7))
   if qq is None:continue
   try:
    gg,pp,ss,vv,newcost,ngrad=state(qq)
    if gg['minimum']<.9*gapfloor or vv[active].min()<.9*eps:continue
   except (ValueError,np.linalg.LinAlgError):continue
   if newcost<cost-1e-12*max(1,cost):q=qq;accepted=True;row['alpha']=2**-back;break
  if accepted and back==0:trust=min(.25,trust*1.2)
  if not accepted:trust*=.4
  if trust<1e-11:print('OWN_FLOW_STALLED',row,flush=True);break
 return q
if __name__=='__main__':
 f=ROOT/(sys.argv[1] if len(sys.argv)>1 else 'artifacts/canonical_atlas/detached_C496_large');run(f,f/'own_strict_flow',f/(sys.argv[2] if len(sys.argv)>2 else 'own_strict211/STRICT_NUMERICAL_q.npy'))
