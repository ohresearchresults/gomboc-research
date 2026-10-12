"""Integer-certificate locator. Floating results are never proof evidence."""
import os
for k in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS'):os.environ[k]='1'
import numpy as np
from scipy.linalg import solve
import itertools,warnings
warnings.filterwarnings('ignore')
def sym(a,b):return (np.outer(a,b)+np.outer(b,a))/2

def problem(p,fs,merged=False,cov=False,constraints=None):
 E=np.eye(9);A=len(fs);nodes=[i for i in range(9)if p[i]!=i]
 assert len(nodes)==8
 constraints=constraints or [(i,p[i],1)for i in nodes]
 S=np.array([sg*sym(E[i],E[i]-E[j])for i,j,sg in constraints])
 K=[sym(E[i],E[j])for i in range(9)for j in range(i,9)]
 ff=[set(tuple(sorted(t))for t in f)for f in fs]
 if merged:
  ts=sorted(set.union(*ff));ft=np.array([[int(t in f)for t in ts]for f in ff])
 else:
  ts=[tuple(sorted(t))for f in fs for t in f];ft=np.zeros((A,len(ts)),dtype=int)
  at=0
  for a,f in enumerate(fs):ft[a,at:at+len(f)]=1;at+=len(f)
 h=ft[:-1]-ft[-1];G=9*A+(45+int(cov))*(A-1)+1
 ix=[];ls=[]
 for j,t in enumerate(ts):
  w=E[list(t)].sum(0);ii=[];ll=[]
  for a in range(A):
   if ft[a,j]:
    ii+=list(range(9*a,9*(a+1)));ll += [ft[a,j]*sym(e,w)for e in E]
  for a in range(A-1):
   if h[a,j]:
    ii+=list(range(9*A+45*a,9*A+45*(a+1)));ll += [h[a,j]*q for q in K]
  if cov:
   J=np.outer(w,w)+np.diag(w)
   for a in range(A-1):
    if h[a,j]:ii.append(9*A+45*(A-1)+a);ll.append(h[a,j]*J)
  ix.append(np.array(ii+[G-1],dtype=int));ls.append(np.array(ll+[-E]))
 return p,fs,merged,cov,ts,ft,h,S,G,ix,ls,constraints

def locate(prob,eps=1e-7,maxouter=11):
 p,fs,merged,cov,ts,ft,h,S,G,ix,ls,constraints=prob;k=len(ts);m=len(S)
 g=np.zeros(G);g[-1]=-1.;lam=np.full((k,m),1/(m*k));one=np.ones(m)
 def calc(g,lam,tau,hess):
  if lam.min()<=0:return None
  val=-g[-1]-tau*np.log(lam).sum()
  if hess:
   gg=np.zeros(G);gg[-1]=-1
   H=np.zeros((G+1,G+1));rhs=np.zeros(G+1);ss=[];ld=[]
  for t,(ii,LL)in enumerate(zip(ix,ls)):
   Q=np.einsum('a,aij->ij',g[ii],LL)+np.einsum('a,aij->ij',lam[t],S)
   try:R=np.linalg.cholesky(Q)
   except np.linalg.LinAlgError:return None
   val-=2*tau*np.log(np.diag(R)).sum()
   if not hess:continue
   W=np.linalg.solve(Q,np.eye(9))
   WL=np.einsum('ij,ajk->aik',W,LL);WS=np.einsum('ij,ajk->aik',W,S)
   gradl=-tau*(np.trace(WS,axis1=1,axis2=2)+1/lam[t])
   gradg=-tau*np.trace(WL,axis1=1,axis2=2)
   Hll=tau*(np.einsum('aij,bji->ab',WS,WS)+np.diag(1/lam[t]**2))
   Hlg=tau*np.einsum('aij,bji->ab',WS,WL)
   Hgg=tau*np.einsum('aij,bji->ab',WL,WL)
   XX=np.linalg.solve(Hll,np.column_stack((Hlg,one,gradl)))
   TT=Hlg.T@XX;L=len(ii)
   H[np.ix_(ii,ii)]+=Hgg-TT[:,:L]
   H[ii,G]-=TT[:,L];H[G,ii]-=TT[:,L];H[G,G]-=np.sum(XX[:,L])
   rhs[ii]+=TT[:,L+1];rhs[G]+=np.sum(XX[:,L+1]);gg[ii]+=gradg
   ss.append(XX);ld.append(gradl)
  if not hess:return val
  rhs[:G]-=gg;rhs[G]+=1-lam.sum()
  try:d=solve(H,rhs,assume_a='sym',check_finite=False)
  except Exception:d=np.linalg.lstsq(H,rhs,rcond=1e-14)[0]
  dl=np.array([-XX[:,:len(ii)]@d[ii]-XX[:,len(ii)]*d[-1]-XX[:,len(ii)+1]
               for XX,ii in zip(ss,ix)])
  decr=-gg@d[:G]-sum(a@b for a,b in zip(ld,dl))
  return val,d[:G],dl,decr
 for it in range(maxouter):
  tau=.05*.18**it
  for j in range(70):
   out=calc(g,lam,tau,True)
   if out is None:return None
   val,dg,dl,decr=out
   if decr<min(1e-7,tau*.001):break
   al=1.;negative=dl<0
   if negative.any():al=min(al,.99*np.min(-lam[negative]/dl[negative]))
   for _ in range(60):
    ng=g+al*dg;nl=lam+al*dl;v=calc(ng,nl,tau,False)
    if v is not None and v<=val-.05*al*decr:break
    al*=.5
   else:return np.r_[g[:9*len(fs)],lam.ravel(),g[9*len(fs):-1],g[-1]]
   g,lam=ng,nl
  if g[-1]>eps or tau*((9+m)*k)<eps:break
 return np.r_[g[:9*len(fs)],lam.ravel(),g[9*len(fs):-1],g[-1]]

def matrices(prob,z):
 p,fs,merged,cov,ts,ft,h,S,G,ix,ls,constraints=prob
 A=len(fs);k=len(ts);m=len(S);at=9*A+m*k
 assert len(z)==at+(45+int(cov))*(A-1) and min(z[9*A:at])>=0
 KK=[]
 for a in range(A-1):
  M=[[0]*9 for _ in range(9)]
  for i in range(9):
   for j in range(i,9):
    M[i][j]=M[j][i]=z[at]*(2 if i==j else 1);at+=1
  KK.append(M)
 for t,cell in enumerate(ts):
  w=[int(i in cell)for i in range(9)]
  gamma=[sum(int(ft[a,t])*z[9*a+i]for a in range(A))for i in range(9)]
  eta=sum(int(h[a,t])*z[at+a]for a in range(A-1))if cov else 0
  M=[[gamma[i]*w[j]+gamma[j]*w[i]
     +sum(int(h[a,t])*KK[a][i][j]for a in range(A-1))
     +2*eta*(w[i]*w[j]+int(i==j)*w[i])
     for j in range(9)]for i in range(9)]
  for lm,(i,j,sg)in zip(z[9*A+m*t:9*A+m*(t+1)],constraints):
   l=sg*lm;M[i][i]+=2*l;M[i][j]-=l;M[j][i]-=l
  yield M

def pd(Q,shift=1):
 M=[row[:]for row in Q];prev=1
 for i in range(9):M[i][i]-=shift
 for k in range(9):
  z=M[k][k]
  if z<=0:return False
  for i in range(k+1,9):
   for j in range(i,9):
    num=z*M[i][j]-M[i][k]*M[k][j]
    assert num%prev==0
    M[i][j]=M[j][i]=num//prev
  prev=z
 return True

def certify(p,fs,merged=False,cov=False,eps=1e-7,maxouter=11,power=8,constraints=None):
 pr=problem(p,fs,merged,cov,constraints);x=locate(pr,eps,maxouter)
 if x is None or not np.isfinite(x).all() or x[-1]<=eps:return None
 scale=max(abs(x[:-1]));z=[round(float(v)/scale*10**power)for v in x[:-1]]
 if min(z[9*len(fs):9*len(fs)+len(pr[-1])*len(pr[4])])<0:return None
 if not all(pd(q)for q in matrices(pr,z)):return None
 return z
