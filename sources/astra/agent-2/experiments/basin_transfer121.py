"""Finite actual-own primal basin transfer in a full physical contact chart.
A nominated cross-basin chord is optimized while every old positive exclusion
remains strict. Outside-root witnesses remain within the elder-reachable set.
Only a genuinely positive chord and increased reachability count pass a stage.
"""
import sys,json,time,numpy as np,jax,jax.numpy as jnp
from scipy.linalg import svd
from scipy.optimize import linprog
from scipy.sparse import csr_matrix,hstack,vstack,eye
from canonical_atlas import ROOT,Chart
from support_persistence import barcode
from geometry import angular_scores

def reachable(A,root,eps):
 sc=angular_scores(A);seen=np.zeros(len(A),bool);seen[root]=True
 for _ in range(len(A)):
  new=np.any(sc[:,seen]>eps,axis=1)|seen
  if np.array_equal(new,seen):break
  seen=new
 return seen,sc

def run(folder,inputpath,out,steps=250):
 c=Chart(folder);q=np.load(inputpath);out.mkdir(exist_ok=False);V,F=c.meta['V'],c.F;D=len(q);flat=np.flatnonzero(~c.incidence.ravel());K=len(flat);N=V+F;eps=5e-8;floor=1e-9;g=c.graph(q);ur=int(np.argmax(np.sum(g['Z']**2,1)));sr=int(np.argmax(np.sum(g['Q']**2,1)));pp,pw,pb=barcode(g['Z'],np.ones(V),c.eu);jr=int(pp[np.argmax(pb),0]);active=np.ones(N,bool);active[[ur,jr,V+sr]]=False;seen,sc=reachable(g['Z'],ur,.5*eps);choices=[(sc[i,j],i,j) for i in np.flatnonzero(~seen) for j in np.flatnonzero(seen)];best=max(choices);_,child,parent=best;child=int(child);parent=int(parent);initial_count=int(seen.sum());history=[];trust=.02;start=time.time();(out/'nomination.json').write_text(json.dumps(dict(source=str(inputpath),elder=ur,junior=jr,stable=sr,child=child,parent=parent,old_cross=float(best[0]),initial_reachable=np.flatnonzero(seen).tolist(),numerical_reach_threshold=.5*eps,required_chord_margin=eps,no_goal_claim=True),indent=2)+'\n')
 def pieces(q,up,sp):
  X,Y,Z,Q,cent,vol,gap=c.physical(q)
  def angles(A,p):
   d=A[p]-A;return jnp.sum(A*d,axis=1)/jnp.sqrt(jnp.maximum(jnp.sum(A*A,axis=1)*jnp.sum(d*d,axis=1),1e-40))
  return jnp.r_[gap.ravel()[flat],angles(Z,up),angles(Q,sp),X.ravel(),Y.ravel()]
 jac=jax.jit(jax.jacfwd(pieces));
 def loss(q):
  Z=c.physical(q)[2];a,b=Z[child],Z[parent];d=b-a;return -jnp.sum(a*d)/jnp.sqrt(jnp.sum(a*a)*jnp.sum(d*d))
 valuegrad=jax.jit(jax.value_and_grad(loss))
 def state(q):
  g=c.graph(q);u=angular_scores(g['Z']);s=angular_scores(g['Q']);chosen=u.copy();chosen[np.ix_(seen,~seen)]=-np.inf;up=chosen.argmax(1);sp=s.argmax(1);guards=np.r_[chosen[np.arange(V),up],s[np.arange(F),sp]];v,grad=valuegrad(q);return g,up,sp,guards,float(v),np.asarray(grad)
 def retract(qq,up,sp,W,radius):
  for it in range(8):
   raw=np.asarray(pieces(qq,up,sp));vals=np.r_[raw[:K],raw[K:K+N][active]];targets=np.r_[np.full(K,floor),np.full(active.sum(),eps)]
   if not np.isfinite(raw).all():return None
   if np.min(vals-targets)>-1e-11:return qq
   J=np.asarray(jac(qq,up,sp));C=np.vstack([J[:K],J[K:K+N][active]])@W;bound=radius/np.sqrt(D);keep=vals-targets<=bound*np.sum(abs(C),1)+1e-10;C=C[keep];rhs=(vals-targets)[keep];weights=np.r_[np.ones(K),np.full(active.sum(),1000.)][keep];I=eye(D);A=vstack([hstack([-csr_matrix(C*weights[:,None]),csr_matrix((len(C),D))]),hstack([I,-I]),hstack([-I,-I])],format='csr');b=np.r_[rhs*weights,np.zeros(2*D)];lp=linprog(np.r_[np.zeros(D),np.ones(D)],A_ub=A,b_ub=b,bounds=[(-bound,bound)]*D+[(0,None)]*D,method='highs-ipm',options={'primal_feasibility_tolerance':1e-10,'dual_feasibility_tolerance':1e-9,'time_limit':10})
   if not lp.success:return None
   qq=qq+W@lp.x[:D]
  return None
 for it in range(steps):
  g,up,sp,guards,cost,grad=state(q);live,scores=reachable(g['Z'],ur,.5*eps);S=int((angular_scores(g['Q']).max(1)<0).sum());U=int((scores.max(1)<0).sum());row=dict(it=it,cross=-cost,reachable=int(live.sum()),S=S,U=U,minimum=float(guards[active].min()),noncontact=g['minimum'],seconds=time.time()-start,trust=trust);history.append(row);np.save(out/'latest_q.npy',q);(out/'history.json').write_text(json.dumps(history,indent=2)+'\n')
  if it%5==0:print('BASIN_TRANSFER',row,flush=True)
  if -cost>eps and int(live.sum())>initial_count:(out/'FINITE_TRANSFER_NOMINATION.json').write_text(json.dumps(row,indent=2)+'\n');print('TRANSFER_NOT_GOAL_REQUIRES_EXACT',row,flush=True);break
  if guards[active].min()<.8*eps or S>1 or U>2:raise ValueError('promised actual121 guards violated')
  J=np.asarray(jac(q,up,sp));jp=J[K+N:];metric=np.vstack([jp[:3*V]/np.sqrt(np.mean(g['X']**2)),jp[3*V:]/np.sqrt(np.mean(g['Y']**2)),np.eye(D)*.05]);_,dd,Vt=svd(metric,full_matrices=False,check_finite=False);W=Vt.T/dd;C=np.vstack([J[:K],J[K:K+N][active]])@W;rhs=np.r_[(1-g['Y']@g['X'].T).ravel()[flat]-floor,guards[active]-eps];bound=trust/np.sqrt(D);keep=rhs<=bound*np.sum(abs(C),1)+1e-10;weights=np.r_[np.ones(K),np.full(active.sum(),1000.)][keep];lp=linprog(grad@W,A_ub=-C[keep]*weights[:,None],b_ub=rhs[keep]*weights,bounds=[(-bound,bound)]*D,method='highs-ipm',options={'primal_feasibility_tolerance':1e-10,'dual_feasibility_tolerance':1e-9,'time_limit':10});accepted=False
  if lp.success:
   dq=W@lp.x
   for back in range(18):
    qq=retract(q+2**-back*dq,up,sp,W,max(trust*2**-back,1e-7))
    if qq is None:continue
    try:gg,uu,ss,vv,newcost,newgrad=state(qq)
    except (ValueError,np.linalg.LinAlgError):continue
    if gg['minimum']<.9*floor or min(vv[active])<.9*eps:continue
    if np.linalg.norm(gg['Z'][child]-gg['Z'][parent])<1e-3*np.sqrt(np.mean(gg['Z']**2)):continue
    if newcost<cost-1e-12:q=qq;accepted=True;row['alpha']=2**-back;break
  if accepted and back==0:trust=min(.2,trust*1.2)
  if not accepted:trust*=.4
  if trust<1e-10:print('FINITE_TRANSFER_STALLED',row,flush=True);break
 return q
if __name__=='__main__':
 f=ROOT/sys.argv[1];run(f,f/sys.argv[2],f/sys.argv[3])
