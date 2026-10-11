"""Contact atlas with reference U1 and separate actual-volume centroid correction.
Reference U1 is NEVER promoted as own U1 until the actual body is independently
centered/audited. The physical coordinates and all facets are consistently paired.
"""
import sys,json,time,numpy as np
from scipy.linalg import svd
from scipy.optimize import linprog
import jax
import jax.numpy as jnp
from contact_atlas import ROOT,Chart
from support_persistence import barcode
from bicap_polish import forest
from geometry import angular_scores

def run(folder,out,iters=2000,startpath=None):
 c=Chart(folder);q=c.q.copy() if startpath is None else np.load(startpath);out.mkdir(parents=True,exist_ok=True);V,F=c.meta['V'],c.F;flat=np.flatnonzero(~c.incidence.ravel());K=len(flat);eps=1e-8;gapfloor=1e-7;weight=100.;trust=.01
 def pieces(q,parent):
  X,Y,Z,Q,cent,vol,gap=c.physical(q);d=X[parent]-X;guard=jnp.sum(X*d,axis=1)/jnp.sqrt(jnp.sum(X*X,axis=1)*jnp.sum(d*d,axis=1));return jnp.concatenate([gap.ravel()[flat],guard,cent,X.ravel(),Y.ravel()])
 jac=jax.jit(jax.jacfwd(pieces,argnums=0))
 def refloss(q,p,w):
  A=c.reconstruct(q)[:F];root,a,b=A[p[:,0]],A[p[:,1]],A[p[:,2]];d=b-a;t=jnp.clip(-jnp.sum(a*d,axis=1)/jnp.sum(d*d,axis=1),0,1);birth=jnp.sum(root*root,axis=1);depth=jnp.maximum(birth-jnp.sum((a+t[:,None]*d)**2,axis=1),0)*w/birth;return jnp.sum(depth*depth)
 obj=jax.jit(jax.value_and_grad(refloss));history=[];start=time.time()
 def retract(qtest,parent,active,W,radius):
  D=len(qtest);target=np.r_[np.full(K,gapfloor),np.full(int(active.sum()),eps)];row_scale=np.r_[np.ones(K),np.full(int(active.sum()),1000.)]
  centered=np.max(abs(np.asarray(pieces(qtest,parent))[K+V:K+V+3]))<1e-4
  for correction in range(10):
   raw=np.asarray(pieces(qtest,parent));values=np.r_[raw[:K],raw[K:K+V][active]]
   if not np.isfinite(raw).all():return None
   if np.all(values[:K]>=.999*gapfloor) and np.all(values[K:]>=.999*eps) and (not centered or np.max(abs(raw[K+V:K+V+3]))<1e-13):return qtest
   J=np.asarray(jac(qtest,parent));C=np.vstack([J[:K],J[K:K+V][active]])@W
   I=np.eye(D);AA=np.vstack([np.c_[-C*row_scale[:,None],np.zeros((len(C),D))],np.c_[I,-I],np.c_[-I,-I]]);bb=np.r_[(values-target)*row_scale,np.zeros(2*D)]
   EQ=np.c_[J[K+V:K+V+3]@W,np.zeros((3,D))]*1e4 if centered else None;EB=-raw[K+V:K+V+3]*1e4 if centered else None
   lp=linprog(np.r_[np.zeros(D),np.ones(D)],A_ub=AA,b_ub=bb,A_eq=EQ,b_eq=EB,bounds=[(-radius/np.sqrt(D),radius/np.sqrt(D))]*D+[(0,None)]*D,method='highs',options={'primal_feasibility_tolerance':1e-10,'dual_feasibility_tolerance':1e-9})
   if not lp.success:return None
   qtest=qtest+W@lp.x[:D]
  return None

 def states(q):
  g=c.graph(q);root=int(np.argmax((g['X']**2).sum(1)));p,_=forest(g['X'],np.ones(V),[root]);act=np.ones(V,bool);act[root]=False;guard=angular_scores(g['X'])[np.arange(V),p];bp,bw,bars=barcode(g['Y'],np.ones(F),c.es);val,gr=obj(q,bp,bw);return g,p,act,guard,float(val),np.asarray(gr)
 for it in range(iters):
  g,p,active,guards,val,grad=states(q);cent=g['c'];merit=val+weight*abs(cent).sum();row=dict(it=it,referenceU=int((angular_scores(g['X']).max(1)<0).sum()),referenceS=int((angular_scores(g['Y']).max(1)<0).sum()),U=int((angular_scores(g['Z']).max(1)<0).sum()),S=int((angular_scores(g['Q']).max(1)<0).sum()),reference_Q2=val,centroid=cent.tolist(),centroid_inf=float(abs(cent).max()),merit=float(merit),min_ref_guard=float(guards[active].min()),min_noncontact=g['minimum'],trust=trust,seconds=time.time()-start);history.append(row);np.save(out/'latest_q.npy',q);(out/'history.json').write_text(json.dumps(history,indent=2)+'\n')
  if it%5==0:print('CENTERED_U1',row,flush=True)
  if row['S']==row['U']==1:
   np.save(out/'NUMERICAL_NOMINATION_q.npy',q);(out/'NUMERICAL_NOMINATION.json').write_text(json.dumps(row,indent=2)+'\n');print('ACTUAL_NUMERICAL_NOMINATION_REQUIRES_EXACT',row,flush=True);break
  if row['referenceU']!=1 or guards[active].min()<.8*eps:raise ValueError('lost promised reference U1; reject iterate')
  J=np.asarray(jac(q,p));D=len(q);jp=J[K+V+3:];metric=np.vstack([jp[:3*V]/np.sqrt(np.mean(g['X']**2)),jp[3*V:]/np.sqrt(np.mean(g['Y']**2)),np.eye(D)*.05]);_,dd,Vt=svd(metric,full_matrices=False,check_finite=False);W=Vt.T/dd;gap=(1-g['Y']@g['X'].T).ravel()[flat];C=np.vstack([J[:K],J[K:K+V][active]]);rhs=np.r_[gap-gapfloor,guards[active]-eps];JC=J[K+V:K+V+3]@W
  row_scale=np.r_[np.ones(K),np.full(int(active.sum()),1000.)];AA=np.vstack([np.c_[(-C@W)*row_scale[:,None],np.zeros((len(C),3))],np.c_[JC,-np.eye(3)],np.c_[-JC,-np.eye(3)]]);bb=np.r_[rhs*row_scale,-cent,cent];objective=np.r_[grad@W,np.full(3,weight)];lp=linprog(objective,A_ub=AA,b_ub=bb,bounds=[(-trust/np.sqrt(D),trust/np.sqrt(D))]*D+[(0,None)]*3,method='highs',options={'primal_feasibility_tolerance':1e-10,'dual_feasibility_tolerance':1e-9})
  if not lp.success:trust*=.5;row['LP']=lp.message;continue
  dq=W@lp.x[:D];accepted=False
  for back in range(20):
   qq=q+2**-back*dq
   qq=retract(qq,p,active,W,max(trust*2**-back,1e-7))
   if qq is None:continue
   try:
    gg,pp,aa,vv,newcost,ggg=states(qq)
    if gg['minimum']<.9*gapfloor or vv[aa].min()<.9*eps:continue
    mm=newcost+weight*abs(gg['c']).sum()
   except (ValueError,np.linalg.LinAlgError):continue
   if mm<merit-1e-12*max(1,merit):q=qq;accepted=True;row['alpha']=2**-back;break
  if accepted and back==0:trust=min(.2,trust*1.15)
  if not accepted:trust*=.4
  if trust<1e-11:print('CENTERED_U1_STALLED',row,flush=True);break
 return q
if __name__=='__main__':
 f=ROOT/(sys.argv[1] if len(sys.argv)>1 else 'artifacts/contact_atlas/exact_iteration16');run(f,f/'centered_U1_eq',startpath=f/'centered_U1_eq_start.npy')
