"""Actual-centroid strict rooted-forest correction in the convex section chart."""
import json,sys,time,numpy as np
from functools import partial
from scipy.linalg import svd
from scipy.optimize import linprog
from scipy.sparse import csr_matrix,eye,hstack,vstack
from scipy.spatial import QhullError
import jax
import jax.numpy as jnp
from section_search import ROOT,graph,physical,stats
from bicap_polish import roots,forest
from geometry import angular_scores

def data(q,m,L,nU,nS):
 g=graph(q,m,L);rr=[roots(g['Z'],g['xm'],g['bp'],g['bw'],nU),roots(g['Y'],g['ym'],g['bq'],g['qw'],nS)];pa=[];sg=[];vv=[]
 for A,mask,r in [(g['Z'],g['xm'],rr[0]),(g['Y'],g['ym'],rr[1])]:
  p,s=forest(A,mask,r);v=angular_scores(A)[np.arange(len(A)),p]*s;pa.append(p);sg.append(s);vv.append(v)
 return g,np.r_[vv[0],vv[1]],pa,sg,rr
@partial(jax.jit,static_argnums=(1,2))
def jac(q,m,L,tri,st,up,us,sp,ss):
 def fun(q):
  X,Z,Y,c,v=physical(q,m,L,tri,st)
  def calc(A,p,s):
   d=A[p]-A;return s*jnp.sum(A*d,axis=1)/jnp.sqrt(jnp.maximum(jnp.sum(A*A,axis=1)*jnp.sum(d*d,axis=1),1e-50))
  return jnp.concatenate([calc(Z,up,us),calc(Y,sp,ss),X.ravel()])
 return jax.jacrev(fun)(q)
def run(q,m,L,out,nU=1,nS=1,iters=500,epsilon=1e-6):
 out.mkdir(parents=True,exist_ok=True);np.save(out/'initial_theta.npy',q);hist=[];trust=.005;start=time.time()
 for it in range(iters):
  g,v,pa,sg,rr=data(q,m,L,nU,nS);merit=np.maximum(epsilon-v,0).sum();row=stats(g,m,L);row.update(it=it,merit=float(merit),minimum=float(v.min()),trust=trust,roots=rr,seconds=time.time()-start);hist.append(row);np.save(out/'latest_theta.npy',q);np.save(out/'latest_points.npy',g['X']);(out/'history.json').write_text(json.dumps(hist,indent=2)+'\n')
  if it%10==0:print('SECTION_POLISH',row,flush=True)
  if min(v)>.8*epsilon and row['U']==nU and row['S']==nS:
   np.save(out/'STRICT_NUMERICAL_theta.npy',q);np.save(out/'STRICT_NUMERICAL_points.npy',g['X']);(out/'STRICT_NUMERICAL.json').write_text(json.dumps(row,indent=2)+'\n');print('STRICT_NUMERICAL_REQUIRES_EXACT',row,flush=True);break
  J=np.asarray(jac(q,m,L,g['tri'],g['st'],pa[0],sg[0],pa[1],sg[1]));nm=len(v);scale=np.sqrt(np.mean(g['Z']**2));metric=np.vstack([J[nm:]/scale,np.eye(len(q))*.05]);_,dd,Vt=svd(metric,full_matrices=False,check_finite=False);W=Vt.T/dd;A=J[:nm]@W;d=len(q);I=eye(d);O=csr_matrix((d,nm));mat=vstack([hstack([-csr_matrix(A),-eye(nm),csr_matrix((nm,d))]),hstack([I,O,-I]),hstack([-I,O,-I])],format='csr');rhs=np.r_[v-epsilon,np.zeros(2*d)];obj=np.r_[np.zeros(d),np.ones(nm),np.full(d,1e-7)];lp=linprog(obj,A_ub=mat,b_ub=rhs,bounds=[(-trust/np.sqrt(d),trust/np.sqrt(d))]*d+[(0,None)]*(nm+d),method='highs',options={'primal_feasibility_tolerance':1e-9,'dual_feasibility_tolerance':1e-9})
  if not lp.success:trust*=.5;continue
  direction=W@lp.x[:d];accepted=False
  for back in range(14):
   qt=q+2**-back*direction
   try:gg,vv,pp,ss,rr2=data(qt,m,L,nU,nS);mm=np.maximum(epsilon-vv,0).sum()
   except (QhullError,ValueError,AssertionError,np.linalg.LinAlgError):continue
   if np.isfinite(mm) and mm<merit*(1-1e-5):q=qt;accepted=True;row['alpha']=2**-back;break
  if accepted and back==0:trust=min(.15,trust*1.2)
  if not accepted:trust*=.4
  if trust<1e-11:print('SECTION_STALLED',row,flush=True);break
 return q
if __name__=='__main__':
 src=ROOT/sys.argv[1];meta=json.loads((src/'construction.json').read_text());stage=sys.argv[2] if len(sys.argv)>2 else 'stage3/best_theta.npy';name=sys.argv[3] if len(sys.argv)>3 else 'direct11';nu=int(sys.argv[4]) if len(sys.argv)>4 else 1;ns=int(sys.argv[5]) if len(sys.argv)>5 else 1
 run(np.load(src/stage),meta['m'],meta['L'],src/name,nu,ns)
