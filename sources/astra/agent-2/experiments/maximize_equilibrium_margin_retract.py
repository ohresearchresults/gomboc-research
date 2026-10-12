"""Raise the minimum actual-own escape margin of a complete physical contact body.
The two essential roots are excluded only. All noncontacts/true faces/mass are
recomputed; trial margin increases are independently checked, never relaxed away.
"""
import sys,json,time,numpy as np,jax,jax.numpy as jnp
from scipy.linalg import svd
from scipy.optimize import linprog
from scipy.sparse import csr_matrix,hstack,vstack,eye
from canonical_atlas import ROOT,Chart
from geometry import angular_scores

def run(folder,out,inputpath=None,iters=2000):
 c=Chart(folder);q=c.q.copy() if inputpath is None else np.load(inputpath);out.mkdir(exist_ok=False,parents=True);V,F=c.meta['V'],c.F;D=len(q);flat=np.flatnonzero(~c.incidence.ravel());K=len(flat);N=V+F;g=c.graph(q);ur=np.argmax(np.sum(g['Z']**2,1));sr=np.argmax(np.sum(g['Q']**2,1));active=np.ones(N,bool);active[[ur,V+sr]]=False;trust=.04;floor=1e-9;history=[];start=time.time()
 def pieces(q,up,sp):
  X,Y,Z,Q,cent,vol,gap=c.physical(q)
  def score(A,p):
   d=A[p]-A;return jnp.sum(A*d,axis=1)/jnp.sqrt(jnp.maximum(jnp.sum(A*A,axis=1)*jnp.sum(d*d,axis=1),1e-40))
  return jnp.r_[gap.ravel()[flat],score(Z,up),score(Q,sp),X.ravel(),Y.ravel()]
 jac=jax.jit(jax.jacfwd(pieces))
 def state(q):
  g=c.graph(q);u=angular_scores(g['Z']);s=angular_scores(g['Q']);up=u.argmax(1);sp=s.argmax(1);sc=np.r_[u[np.arange(V),up],s[np.arange(F),sp]];return g,up,sp,sc
 def retract(qq,up,sp,W,radius,target):
  for correction in range(10):
   raw=np.asarray(pieces(qq,up,sp));values=np.r_[raw[:K],raw[K:K+N][active]];targets=np.r_[np.full(K,floor),np.full(active.sum(),target)]
   if not np.isfinite(raw).all():return None
   if np.min(values-targets)>-1e-12:return qq
   J=np.asarray(jac(qq,up,sp));C=np.vstack([J[:K],J[K:K+N][active]])@W;bound=radius/np.sqrt(D);keep=values-targets<=bound*np.sum(abs(C),axis=1)+1e-10;C=C[keep];rhs=(values-targets)[keep];scales=np.r_[np.ones(K),np.full(active.sum(),1000.)][keep];I=eye(D);AA=vstack([hstack([-csr_matrix(C*scales[:,None]),csr_matrix((len(C),D))]),hstack([I,-I]),hstack([-I,-I])],format='csr');bb=np.r_[rhs*scales,np.zeros(2*D)];lp=linprog(np.r_[np.zeros(D),np.ones(D)],A_ub=AA,b_ub=bb,bounds=[(-bound,bound)]*D+[(0,None)]*D,method='highs-ipm',options={'primal_feasibility_tolerance':1e-10,'dual_feasibility_tolerance':1e-10,'time_limit':10})
   if not lp.success:return None
   qq=qq+W@lp.x[:D]
  return None
 for it in range(iters):
  g,up,sp,sc=state(q);margin=float(sc[active].min());row=dict(it=it,margin=margin,S=int((sc[V:]<0).sum()),U=int((sc[:V]<0).sum()),centroid=g['c'].tolist(),volume=g['v'],minimum_noncontact=g['minimum'],trust=trust,seconds=time.time()-start);history.append(row);np.save(out/'latest_q.npy',q);(out/'history.json').write_text(json.dumps(history,indent=2)+'\n')
  if it%10==0:print('MAXIMIZE_OWN_MARGIN',row,flush=True)
  assert margin>0 and row['S']==row['U']==1
  J=np.asarray(jac(q,up,sp));jp=J[K+N:];metric=np.vstack([jp[:3*V]/np.sqrt(np.mean(g['X']**2)),jp[3*V:]/np.sqrt(np.mean(g['Y']**2)),np.eye(D)*.05]);_,sv,Vt=svd(metric,full_matrices=False,check_finite=False);W=Vt.T/sv;A=J[:K]@W;gap=(1-g['Y']@g['X'].T).ravel()[flat];C=J[K:K+N][active]@W;bound=trust/np.sqrt(D);keep=gap-floor<=bound*np.sum(abs(A),axis=1)+1e-10;AA=np.r_[np.c_[-A[keep],np.zeros(keep.sum())],np.c_[-C,np.ones(len(C))]];b=np.r_[gap[keep]-floor,sc[active]-margin];lp=linprog(np.r_[np.zeros(D),-1],A_ub=AA,b_ub=b,bounds=[(-bound,bound)]*D+[(0,.1)],method='highs-ipm',options={'primal_feasibility_tolerance':1e-10,'dual_feasibility_tolerance':1e-10,'time_limit':10})
  if not lp.success:trust*=.4
  else:
   dq=W@lp.x[:D];accepted=False
   for back in range(24):
    target=margin+.3*2**-back*lp.x[-1];qq=retract(q+2**-back*dq,up,sp,W,max(trust*2**-back,1e-7),target)
    if qq is None:continue
    try:
     gg,uu,ss,vv=state(qq)
     if gg['minimum']<.9*floor or min(vv[active])<=margin+1e-13:continue
    except (ValueError,np.linalg.LinAlgError):continue
    q=qq;accepted=True;row['alpha']=2**-back;row['predicted_gain']=float(lp.x[-1]);break
   if not accepted:trust*=.4
   elif back==0:trust=min(.3,trust*1.2)
  if trust<1e-11:print('FINITE_MARGIN_STALL',row,flush=True);break
 return q
if __name__=='__main__':
 f=ROOT/sys.argv[1];run(f,f/sys.argv[2],f/sys.argv[3] if len(sys.argv)>3 else None,iters=2000)
