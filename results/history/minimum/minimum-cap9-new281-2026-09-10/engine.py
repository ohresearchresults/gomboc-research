"""NEW cap9 barrier locator. Numerical output is not an exclusion certificate."""
import os
for k in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS'):os.environ[k]='1'
import numpy as np
from scipy.linalg import solve
from threadpoolctl import threadpool_limits
threadpool_limits(limits=1)
from itertools import product,combinations

def canonical(p):
 children=[[] for _ in p]
 for i in range(1,len(p)):children[p[i]].append(i)
 def code(i):return '('+''.join(sorted(code(j) for j in children[i]))+')'
 out=[];stack=[]
 for c in code(0):
  if c=='(':out.append(stack[-1] if stack else 0);stack.append(len(out)-1)
  else:stack.pop()
 return tuple(out)
def trees(n=9):return sorted({canonical((0,)+p) for p in product(*(range(i) for i in range(1,n)))})
def weights(a):
 out=[];ids=[i for i in range(9) if i!=a]
 for i,j in combinations(ids,2):
  for k in ids:
   if k in (i,j):continue
   w=[0]*9;w[a]=9;w[i]=w[j]=10;w[k]=7;out.append(w)
 assert len(out)==168
 return out
def locate(p,rows,verbose=False):
 m=168*len(rows);nf=9*len(rows)+(45 if len(rows)>1 else 0);d=nf+1
 I=np.eye(9);L=np.zeros((8,9,9))
 for u in range(1,9):L[u-1,u,u]=2;L[u-1,u,p[u]]=L[u-1,p[u],u]=-1
 J=np.zeros((m,d,9,9));off=[]
 if len(rows)>1:
  assert len(rows)==2
  for i in range(9):
   for j in range(i,9):
    b=np.zeros((9,9));b[i,j]+=1;b[j,i]+=1;off.append(b)
 for r,a in enumerate(rows):
  for t,ww in enumerate(weights(a)):
   t+=168*r;w=np.array(ww)/9
   for i in range(9):J[t,9*r+i]=np.outer(I[i],w)+np.outer(w,I[i])
   if len(rows)>1:J[t,18:63]=np.array(off)*(1 if r==0 else -1)
 J[:,-1]=-I
 y=np.zeros(d);y[-1]=-1;u=np.full((m,8),1/8.)
 def matrix(yy,uu):return np.einsum('mdij,d->mij',J,yy,optimize=True)+np.einsum('mk,kij->mij',uu,L,optimize=True)
 B=matrix(y,u)
 for outer in range(12):
  tau=.05*.18**outer;fac=tau/m
  for inner in range(70):
   chol=np.linalg.cholesky(B);R=np.linalg.inv(B)
   C=R[:,None]@J;D=R[:,None]@L
   gy=-np.trace(C,axis1=2,axis2=3).sum(axis=0);gy[-1]-=1/fac
   gu=-np.trace(D,axis1=2,axis2=3)-1/u
   Hyy=np.einsum('mdij,meji->de',C,C,optimize=True)
   Huy=np.einsum('mkij,mdji->mkd',D,C,optimize=True)
   Huu=np.einsum('mkij,mlji->mkl',D,D,optimize=True)
   Huu[:,np.arange(8),np.arange(8)]+=1/u**2
   rhs=np.concatenate((Huy,np.ones((m,8,1)),gu[:,:,None]),axis=2)
   sol=np.linalg.solve(Huu,rhs);T=sol[:,:,:d];e=sol[:,:,d];v=sol[:,:,d+1]
   S=np.zeros((d+1,d+1));b=np.zeros(d+1)
   S[:d,:d]=Hyy-np.einsum('mkd,mke->de',Huy,T,optimize=True)
   S[:d,d]=-np.einsum('mkd,mk->d',Huy,e,optimize=True);S[d,:d]=S[:d,d];S[d,d]=-e.sum()
   b[:d]=-gy+np.einsum('mkd,mk->d',Huy,v,optimize=True);b[d]=v.sum()
   S=(S+S.T)/2
   try:step=solve(S,b,assume_a='sym',check_finite=False)
   except Exception:step=np.linalg.lstsq(S,b,rcond=1e-14)[0]
   dy=step[:d];du=-v-np.einsum('mkd,d->mk',T,dy,optimize=True)-e*step[d]
   descent=fac*(gy@dy+(gu*du).sum());decrement=-descent
   if decrement < min(1e-7,tau*.001):break
   alpha=min(1.,.99*float(np.min(-u[du<0]/du[du<0]))) if np.any(du<0) else 1.
   old=-y[-1]-fac*(2*np.log(np.diagonal(chol,axis1=1,axis2=2)).sum()+np.log(u).sum())
   deltaB=matrix(dy,du)
   for back in range(60):
    yy=y+alpha*dy;uu=u+alpha*du;BB=B+alpha*deltaB
    try:
     ch=np.linalg.cholesky(BB)
     val=-yy[-1]-fac*(2*np.log(np.diagonal(ch,axis1=1,axis2=2)).sum()+np.log(uu).sum())
     if np.isfinite(val) and val<=old+.05*alpha*descent:break
    except np.linalg.LinAlgError:pass
    alpha*=.5
   else:return None
   y,u,B=yy,uu,BB
  if verbose:print('ITER',outer,inner,'margin',y[-1],'eq',u.sum()/m,'dec',decrement,flush=True)
  if y[-1]>1e-8:return y[:-1],u,y[-1]
 return None
if __name__=='__main__':
 import sys,time
 idx=int(sys.argv[1]);rows=[int(v) for v in sys.argv[2:]] or [0]
 t=time.time();z=locate(trees()[idx],rows,True)
 print('RESULT',idx,rows, None if z is None else z[2], 'time',time.time()-t)
 if z is not None:np.savez('test%d.npz'%idx,g=z[0],mu=z[1],margin=z[2])
