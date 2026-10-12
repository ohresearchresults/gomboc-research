"""Actual-centroid contact realization with at most1U and2S strict roots.
Soft correction uses the continuous local maximum-escape deficit, not a
chosen-tree direct-edge objective. Every candidate preserves true contacts and
is rechecked for strict nonincidence and its own homogeneous mass.
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
from route_forest import forest as route_forest

def run(folder,out,inputpath=None,iters=150,eps=1e-6):
 c=Chart(folder);q=c.q.copy() if inputpath is None else np.load(inputpath);out.mkdir(parents=True,exist_ok=True);V,F=c.meta['V'],c.F;D=len(q);flat=np.flatnonzero(~c.incidence.ravel());K=len(flat);gapfloor=1e-8;trust=.003;history=[];start=time.time();g=c.graph(q);ur=int(np.argmax((g['Z']**2).sum(1)));sr=int(np.argmax((g['Q']**2).sum(1)));bp,bw,bars=barcode(g['Q'],np.ones(F),c.es);child=int(bp[np.argmax(bars),0]);rr=[[ur],[sr]];active=np.ones(V+F,bool);active[ur]=False;active[V+np.array(rr[1])]=False;(out/'roots.json').write_text(json.dumps(rr))
 def pieces(q,up,sp):
  X,Y,Z,Q,cent,vol,gap=c.physical(q)
  def angles(A,p):
   d=A[p]-A;return jnp.sum(A*d,axis=1)/jnp.sqrt(jnp.maximum(jnp.sum(A*A,axis=1)*jnp.sum(d*d,axis=1),1e-40))
  return jnp.concatenate([gap.ravel()[flat],angles(Z,up),angles(Q,sp),cent,X.ravel(),Y.ravel()])
 jac=jax.jit(jax.jacfwd(pieces,argnums=0))
 def state(q):
  g=c.graph(q);up,_,uw=route_forest(g['Z'],np.ones(V),[ur],eps);sp,_,sw=route_forest(g['Q'],np.ones(F),[sr],eps);weights=np.r_[uw,sw];guards=np.r_[angular_scores(g['Z'])[np.arange(V),up],angular_scores(g['Q'])[np.arange(F),sp]];merit=(np.maximum(eps-guards[active],0)*weights[active]).sum();return g,up,sp,guards,float(merit),weights
 for it in range(iters):
  g,up,sp,guards,merit,weights=state(q);row=dict(it=it,S=int((angular_scores(g['Q']).max(1)<0).sum()),U=int((angular_scores(g['Z']).max(1)<0).sum()),minimum=float(guards[active].min()),centroid=g['c'].tolist(),merit=merit,trust=trust,seconds=time.time()-start);history.append(row);np.save(out/'latest_q.npy',q);(out/'history.json').write_text(json.dumps(history,indent=2)+'\n');print('CANONICAL_CORRECT',row,flush=True)
  if min(guards[active])>.8*eps and row['S']==1 and row['U']==1:
   np.save(out/'STRICT_NUMERICAL_q.npy',q);(out/'STRICT_NUMERICAL.json').write_text(json.dumps(row,indent=2)+'\n');print('STRICT110_REQUIRES_EXACT',row,flush=True);break
  J=np.asarray(jac(q,up,sp));nm=V+F;rawgap=(1-g['Y']@g['X'].T).ravel()[flat];jp=J[K+nm+3:];metric=np.vstack([jp[:3*V]/np.sqrt(np.mean(g['Z']**2)),jp[3*V:]/np.sqrt(np.mean(g['Q']**2)),np.eye(D)*.05]);_,dd,Vt=svd(metric,full_matrices=False,check_finite=False);W=Vt.T/dd;Cgap=J[:K]@W;bound=trust/np.sqrt(D);keep_gap=(rawgap-gapfloor<=bound*np.sum(abs(Cgap),axis=1)+1e-10);Cgap=Cgap[keep_gap];selected_gap=rawgap[keep_gap];kg=len(Cgap);Cg=J[K:K+nm][active]@W;JC=J[K+nm:K+nm+3]@W;ng=int(active.sum());I=eye(D);O=csr_matrix((D,ng));A=vstack([hstack([-csr_matrix(Cgap),csr_matrix((kg,ng+D))]),hstack([-csr_matrix(Cg),-eye(ng),csr_matrix((ng,D))]),hstack([I,O,-I]),hstack([-I,O,-I])],format='csr');b=np.r_[selected_gap-gapfloor,guards[active]-eps,np.zeros(2*D)];Eq=hstack([csr_matrix(JC*1e4),csr_matrix((3,ng+D))]);sol=linprog(np.r_[np.zeros(D),weights[active],np.full(D,1e-6)],A_ub=A,b_ub=b,bounds=[(-trust/np.sqrt(D),trust/np.sqrt(D))]*D+[(0,None)]*(ng+D),method='highs-ipm',options={'primal_feasibility_tolerance':1e-10,'dual_feasibility_tolerance':1e-9,'time_limit':10.})
  if not sol.success:
   trust*=.5
   if trust<1e-11:print('LP_TRUST_EXHAUSTED',row,flush=True);break
   continue
  dq=W@sol.x[:D];accepted=False
  for back in range(16):
   qq=q+dq*2**-back
   try:
    gg,uu,ss,vv,mm,ww=state(qq)
    if gg['minimum']<.9*gapfloor:continue
   except (ValueError,np.linalg.LinAlgError):continue
   if mm<merit*(1-1e-5):q=qq;accepted=True;break
  if accepted and back==0:trust=min(.1,trust*1.4)
  if not accepted:trust*=.4
  if trust<1e-11:print('CORRECTOR_STALLED',row,flush=True);break
 return q
if __name__=='__main__':
 folder=ROOT/(sys.argv[1] if len(sys.argv)>1 else 'artifacts/canonical_atlas/C624_delete17');run(folder,folder/'own_strict110_route',folder/sys.argv[2] if len(sys.argv)>2 else None)
