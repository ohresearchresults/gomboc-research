"""Numerical locator only. Exact acceptance is performed separately."""
import os
for _k in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS'):os.environ[_k]='1'
import numpy as np
from scipy.linalg import solve

def locate(prob,eps=1e-8,maxouter=14,verbose=False):
 x,B,ls,bi,mats,_=prob;x=x.copy();N=len(x);I=np.eye(9);k=len(mats)
 ls=set(map(int,ls));glob=np.array([i for i in range(N)if i not in ls]);ng=len(glob)
 gi={j:i for i,j in enumerate(glob)};parts=[];union=[]
 for ix,L in zip(bi,mats):
  il=np.array([int(j)for j in ix if int(j)in ls]);ig=np.array([int(j)for j in ix if int(j)not in ls]);union+=list(il)
  pl=[q for q,j in enumerate(ix)if int(j)in ls];pg=[q for q,j in enumerate(ix)if int(j)not in ls]
  parts.append((il,ig,np.array([gi[int(j)]for j in ig]),L[pl],L[pg]))
 assert len(union)==len(set(union))and set(union)==ls
 assert all(B[j]==1 for j in ls)and all(B[j]==0 for j in glob)
 ls=np.array(sorted(ls))
 def calc(x,tau,hess=True):
  if min(x[ls])<=0:return None
  f=-x[-1]-tau*np.log(x[ls]).sum()
  if hess:
   g=np.zeros(ng);g[gi[N-1]]=-1.;H=np.zeros((ng,ng));hb=np.zeros(ng);bb=0.;rhsn=1.-B@x;saved=[]
  for il,ig,jg,Ll,Lg in parts:
   Q=np.einsum('a,aij->ij',x[il],Ll)+np.einsum('a,aij->ij',x[ig],Lg)
   try:R=np.linalg.cholesky(Q)
   except np.linalg.LinAlgError:return None
   f-=2*tau*np.log(np.diag(R)).sum()
   if not hess:continue
   W=np.linalg.solve(Q,I);Wl=np.einsum('ij,ajk->aik',W,Ll);Wg=np.einsum('ij,ajk->aik',W,Lg)
   gl=-tau/x[il]-tau*np.trace(Wl,axis1=1,axis2=2)
   gg=-tau*np.trace(Wg,axis1=1,axis2=2)
   Hll=tau*np.einsum('aij,bji->ab',Wl,Wl)+np.diag(tau/x[il]**2)
   Hlg=tau*np.einsum('aij,bji->ab',Wl,Wg)
   Hgg=tau*np.einsum('aij,bji->ab',Wg,Wg)
   inv=solve(Hll,np.column_stack([Hlg,np.ones(len(il)),gl]),assume_a='pos',check_finite=False)
   V=inv[:,:len(ig)];v=inv[:,len(ig)];w=inv[:,-1]
   H[np.ix_(jg,jg)]+=Hgg-Hlg.T@V
   hb[jg]-=Hlg.T@v;bb-=sum(v)
   g[jg]+=gg-Hlg.T@w;rhsn+=sum(w)
   saved.append((il,jg,V,v,w,gl,gg))
  if not hess:return f
  Z=np.zeros((ng+1,ng+1));Z[:ng,:ng]=H;Z[:ng,ng]=hb;Z[ng,:ng]=hb;Z[ng,ng]=bb
  rhs=np.r_[-g,rhsn]
  try:q=solve(Z,rhs,assume_a='sym',check_finite=False)
  except Exception:q=np.linalg.lstsq(Z,rhs,rcond=1e-14)[0]
  p=np.zeros(N);p[glob]=q[:ng]
  fullgrad=np.zeros(N);fullgrad[-1]=-1
  for il,jg,V,v,w,gl,gg in saved:
   p[il]=-w-V@q[jg]-v*q[-1]
   fullgrad[il]+=gl;fullgrad[glob[jg]]+=gg
  return f,fullgrad,p
 for it in range(maxouter):
  tau=.05*.18**it
  for j in range(70):
   out=calc(x,tau)
   if out is None:return None
   f,g,p=out;decr=-g@p
   if decr<min(1e-7,tau*.001):break
   al=1.;nn=p[ls]<0
   if nn.any():al=min(al,.99*np.min(-x[ls][nn]/p[ls][nn]))
   for _ in range(60):
    xx=x+al*p;ff=calc(xx,tau,False)
    if ff is not None and ff<=f+.05*al*(g@p):break
    al*=.5
   else:return x
   x=xx
  if verbose:print('SCHUR_STAGE',it,j,float(x[-1]),flush=True)
  if x[-1]>eps or tau*(k*9+len(ls))<eps:break
 return x
