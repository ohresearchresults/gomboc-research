"""Strict own-mass retraction within the two-cap physical family.
Bottleneck/L1 concept informed by peer agent3/polish_121.py, independently
implemented here for the two-cap parameterization and actual mass derivatives.
"""
import sys,json,time
import numpy as np
from functools import partial
from scipy.linalg import svd
from scipy.optimize import linprog
from scipy.sparse import csr_matrix,eye,hstack,vstack
import jax
import jax.numpy as jnp
from bicap_search import ROOT,graph,stats,physical,jcoords
from geometry import angular_scores

def roots(A,mask,pairs,w,num):
 radius=(A*A).sum(1);root=int(np.argmax(np.where(mask>0,radius,-np.inf)));ans=[root]
 a=A[pairs[:,1]];d=A[pairs[:,2]]-a;tt=np.clip(-np.sum(a*d,axis=1)/np.maximum(np.sum(d*d,axis=1),1e-30),0,1);bars=np.maximum(radius[pairs[:,0]]-np.sum((a+tt[:,None]*d)**2,axis=1),0)*w/radius[pairs[:,0]]
 for j in np.argsort(bars)[::-1]:
  r=int(pairs[j,0])
  if len(ans)>=num:break
  if r not in ans and mask[r]>0:ans.append(r)
 if len(ans)!=num:raise ValueError('cannot identify roots')
 return ans

def forest(A,mask,rr):
 q=angular_scores(A);q[:,mask==0]=-np.inf;cap=np.full(len(A),-np.inf);cap[rr]=np.inf;used=mask==0;pa=np.full(len(A),rr[0],int)
 for _ in range(int(mask.sum())):
  i=int(np.argmax(np.where(~used,cap,-np.inf)));used[i]=True;val=np.minimum(cap[i],q[:,i]);take=(~used)&(val>cap);cap[take]=val[take];pa[take]=i
 for i in rr:pa[i]=int(q[i].argmax())
 sg=mask.copy();sg[rr]=-1
 return pa,sg

def data(q,b,t,nU,nS):
 g=graph(q,b,t);rr=[roots(g['Z'],g['xm'],g['bp'],g['bw'],nU),roots(g['Y'],g['ym'],g['bq'],g['qw'],nS)];parents=[];signs=[];values=[]
 for A,mask,r in [(g['Z'],g['xm'],rr[0]),(g['Y'],g['ym'],rr[1])]:
  p,s=forest(A,mask,r);values.append(angular_scores(A)[np.arange(len(A)),p]*s);parents.append(p);signs.append(s)
 v=np.r_[values[0],values[1]];v[np.isnan(v)]=0
 return g,v,parents,signs,rr

@partial(jax.jit,static_argnums=(1,2))
def valuejac(q,b,t,tri,tm,sf,up,us,sp,ss):
 def fun(q):
  Z,Y,c,v=physical(q,b,t,tri,tm,sf)
  def calc(A,p,s):
   d=A[p]-A;return s*jnp.sum(A*d,axis=1)/jnp.sqrt(jnp.maximum(jnp.sum(A*A,axis=1)*jnp.sum(d*d,axis=1),1e-50))
  return jnp.concatenate([calc(Z,up,us),calc(Y,sp,ss),jcoords(q,b,t).ravel()])
 return fun(q),jax.jacrev(fun)(q)

def run(q,b,t,out,nU=1,nS=2,iters=500,epsilon=5e-7):
 out.mkdir(parents=True,exist_ok=True);np.save(out/'initial_theta.npy',q);history=[];trust=.003;started=time.time();best=np.inf
 for k in range(iters):
  g,v,pa,sg,rr=data(q,b,t,nU,nS);active=np.r_[g['xm'],g['ym']]>0;res=np.maximum(epsilon-v[active],0);merit=res.sum();row=stats(g);row.update(it=k,merit=float(merit),minimum=float(v[active].min()),trust=trust,roots=rr,seconds=time.time()-started);history.append(row)
  if k%10==0:print('POLISH',row,flush=True)
  np.save(out/'latest_theta.npy',q);np.save(out/'latest_points.npy',g['X']);(out/'history.json').write_text(json.dumps(history,indent=2)+'\n')
  if merit<best:best=merit;np.save(out/'best_theta.npy',q)
  if v[active].min()>.8*epsilon and row['U']==nU and row['S']==nS:
   np.save(out/'STRICT_NUMERICAL_theta.npy',q);np.save(out/'STRICT_NUMERICAL_points.npy',g['X']);(out/'STRICT_NUMERICAL.json').write_text(json.dumps(row,indent=2)+'\n');print('STRICT_NUMERICAL_REQUIRES_EXACT',row,flush=True);break
  vv,J=valuejac(q,b,t,g['tri'],g['tm'],g['sf'],pa[0],sg[0],pa[1],sg[1]);J=np.asarray(J);nm=len(v);scale=max(np.sqrt(np.mean(g['Z']**2)),1e-3);metric=np.vstack([J[nm:]/scale,np.eye(len(q))*.05]);_,dd,Vt=svd(metric,full_matrices=False,check_finite=False);W=Vt.T/dd;A=J[:nm][active]@W;d=len(q);m=A.shape[0];I=eye(d);O=csr_matrix((d,m));mat=vstack([hstack([-csr_matrix(A),-eye(m),csr_matrix((m,d))]),hstack([I,O,-I]),hstack([-I,O,-I])],format='csr');rhs=np.r_[v[active]-epsilon,np.zeros(2*d)];obj=np.r_[np.zeros(d),np.ones(m),np.full(d,1e-7)]
  lp=linprog(obj,A_ub=mat,b_ub=rhs,bounds=[(-trust/np.sqrt(d),trust/np.sqrt(d))]*d+[(0,None)]*(m+d),method='highs',options={'primal_feasibility_tolerance':1e-9,'dual_feasibility_tolerance':1e-9})
  if not lp.success:trust*=.5;continue
  delta=W@lp.x[:d];accepted=False
  for back in range(14):
   qt=q+delta*2**-back
   try:
    gg,vv,pp,ss,rr2=data(qt,b,t,nU,nS);aa=np.r_[gg['xm'],gg['ym']]>0;mm=np.maximum(epsilon-vv[aa],0).sum()
   except (ValueError,AssertionError,np.linalg.LinAlgError):continue
   if np.isfinite(mm) and mm<merit*(1-1e-5):q=qt;accepted=True;row['alpha']=2**-back;break
  if accepted and back==0:trust=min(.15,trust*1.2)
  if not accepted:trust*=.4
  if trust<1e-11:print('STALLED',row,flush=True);break
 return q

if __name__=='__main__':
 source=ROOT/sys.argv[1];meta=json.loads((source/'construction.json').read_text());inp=source/(sys.argv[2] if len(sys.argv)>2 else 'stage4/best_theta.npy');out=source/(sys.argv[3] if len(sys.argv)>3 else 'polish12');nu=int(sys.argv[4]) if len(sys.argv)>4 else 1;ns=int(sys.argv[5]) if len(sys.argv)>5 else 2
 run(np.load(inp),meta['bottom'],meta['top'],out,nu,ns)
