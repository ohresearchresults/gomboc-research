"""New graph certificates, not a replay of the old 281 trees.
CPython3.13.5/numpy2.3.5/scipy1.17.0/threadpoolctl3.6.0.
One OpenBLAS thread, one process, no random inputs. Run: python make.py.
"""
import os
for k in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS'):os.environ[k]='1'
import warnings,json,hashlib
from pathlib import Path
from itertools import combinations
import numpy as np
from scipy.linalg import solve,LinAlgWarning
from threadpoolctl import threadpool_limits
threadpool_limits(1)
warnings.simplefilter('ignore',LinAlgWarning)
from inputs import PARENTS,TREES,PLAN
assert __debug__
def weights(a):
 out=[];ids=[i for i in range(9) if i!=a]
 for i,j in combinations(ids,2):
  for k in ids:
   if k in (i,j):continue
   w=[0]*9;w[a]=9;w[i]=w[j]=10;w[k]=7;out.append(w)
 return sorted(out)
def locate(p,extra,rows):
 nr=len(rows);coupled=nr==2;m=168*nr;nf=108 if coupled else 9;d=nf+1
 I=np.eye(9);edges=[(i,p[i]) for i in range(1,9)]+[extra]
 L=np.zeros((9,9,9));basis=[]
 for k,(i,j) in enumerate(edges):L[k,i,i]=2;L[k,i,j]=L[k,j,i]=-1
 for i in range(9):
  for j in range(i,9):
   b=np.zeros((9,9));b[i,j]+=1;b[j,i]+=1;basis.append(b)
 basis=np.array(basis);J=np.zeros((m,d,9,9))
 for r,a in enumerate(rows):
  for wi,ww in enumerate(weights(a)):
   t=168*r+wi;w=np.array(ww)/9
   for i in range(9):J[t,9*r+i]=np.outer(I[i],w)+np.outer(w,I[i])
   if coupled:
    J[t,18:63]=basis*(1 if r==0 else -1)
    J[t,63:108]=basis*(w[rows[1-r]]-181/180)
 J[:,-1]=-I;y=np.zeros(d);y[-1]=-1;u=np.full((m,9),1/9.)
 if coupled:
  k=63
  for i in range(9):
   for j in range(i,9):
    if i==j:y[k]=.0005
    k+=1
 def zmatrix(yy):return np.einsum('k,kij->ij',yy[63:108],basis)
 def matrix(yy,uu):return np.einsum('mdij,d->mij',J,yy,optimize=True)+np.einsum('mk,kij->mij',uu,L,optimize=True)
 B=matrix(y,u)
 for outer in range(8):
  tau=.05*.18**outer;fac=tau/m
  for inner in range(70):
   ch=np.linalg.cholesky(B);R=np.linalg.inv(B);C=R[:,None]@J;D=R[:,None]@L
   gy=-np.trace(C,axis1=2,axis2=3).sum(axis=0);gy[-1]-=1/fac
   gu=-np.trace(D,axis1=2,axis2=3)-1/u
   Hyy=np.einsum('mdij,meji->de',C,C,optimize=True)
   logz=0.
   if coupled:
    Z=zmatrix(y);zc=np.linalg.cholesky(Z);E=np.linalg.inv(Z)@basis
    gy[63:108]-=np.trace(E,axis1=1,axis2=2)
    Hyy[63:108,63:108]+=np.einsum('kij,lji->kl',E,E,optimize=True)
    logz=2*np.log(np.diag(zc)).sum()
   Huy=np.einsum('mkij,mdji->mkd',D,C,optimize=True)
   Huu=np.einsum('mkij,mlji->mkl',D,D,optimize=True)
   Huu[:,np.arange(9),np.arange(9)]+=1/u**2
   sol=np.linalg.solve(Huu,np.concatenate((Huy,np.ones((m,9,1)),gu[:,:,None]),axis=2))
   T=sol[:,:,:d];e=sol[:,:,d];v=sol[:,:,d+1]
   S=np.zeros((d+1,d+1));b=np.zeros(d+1)
   S[:d,:d]=Hyy-np.einsum('mkd,mke->de',Huy,T,optimize=True)
   S[:d,d]=-np.einsum('mkd,mk->d',Huy,e,optimize=True);S[d,:d]=S[:d,d];S[d,d]=-e.sum()
   b[:d]=-gy+np.einsum('mkd,mk->d',Huy,v,optimize=True);b[d]=v.sum();S=(S+S.T)/2
   try:step=solve(S,b,assume_a='sym',check_finite=False)
   except Exception:step=np.linalg.lstsq(S,b,rcond=1e-14)[0]
   dy=step[:d];du=-v-np.einsum('mkd,d->mk',T,dy,optimize=True)-e*step[d]
   descent=fac*(gy@dy+(gu*du).sum())
   if -descent<min(1e-7,tau*.001):break
   alpha=min(1.,.99*float(np.min(-u[du<0]/du[du<0]))) if np.any(du<0) else 1.
   old=-y[-1]-fac*(2*np.log(np.diagonal(ch,axis1=1,axis2=2)).sum()+np.log(u).sum()+logz)
   delta=matrix(dy,du)
   for back in range(60):
    yy=y+alpha*dy;uu=u+alpha*du;BB=B+alpha*delta
    try:
     chnew=np.linalg.cholesky(BB);lognew=0.
     if coupled:lognew=2*np.log(np.diag(np.linalg.cholesky(zmatrix(yy)))).sum()
     val=-yy[-1]-fac*(2*np.log(np.diagonal(chnew,axis1=1,axis2=2)).sum()+np.log(uu).sum()+lognew)
     if np.isfinite(val) and val<=old+.05*alpha*descent:break
    except np.linalg.LinAlgError:pass
    alpha*=.5
   else:raise ArithmeticError('LOCATOR_UNKNOWN')
   y,u,B=yy,uu,BB
  if y[-1]>1e-8:return y[:-1],u
 raise ArithmeticError('LOCATOR_UNKNOWN')
def symmetric(v):
 b=[[0]*9 for _ in range(9)];k=0
 for i in range(9):
  for j in range(i,9):b[i][j]+=v[k];b[j][i]+=v[k];k+=1
 return b
def positive(a):
 a=[r[:] for r in a];last=1
 for k in range(9):
  q=a[k][k]
  if q<=0:return False
  for i in range(k+1,9):
   for j in range(i,9):
    z=q*a[i][j]-a[i][k]*a[k][j];assert z%last==0;a[i][j]=a[j][i]=z//last
  last=q
 return True
def exact_matrices(p,extra,rows,g,u):
 O=symmetric(g[18:63]) if len(rows)==2 else [[0]*9 for _ in range(9)]
 Z=symmetric(g[63:108]) if len(rows)==2 else [[0]*9 for _ in range(9)]
 if len(rows)==2:assert positive(Z)
 edges=[(i,p[i]) for i in range(1,9)]+[extra]
 for r,a in enumerate(rows):
  h=g[9*r:9*r+9]
  for t,w in enumerate(weights(a)):
   v=20*w[rows[1-r]]-181 if len(rows)==2 else 0
   B=[[20*(h[i]*w[j]+w[i]*h[j])+180*(1 if r==0 else -1)*O[i][j]+v*Z[i][j] for j in range(9)] for i in range(9)]
   for (i,j),mu in zip(edges,u[168*r+t]):B[i][i]+=360*mu;B[i][j]-=180*mu;B[j][i]-=180*mu
   for i in range(9):B[i][i]-=1
   yield B
if __name__=='__main__':
 records=[];nm=0
 for k,(o,ex,rows) in enumerate(PLAN):
  g,u=locate(TREES[o],ex,rows);scale=max(np.max(np.abs(g)),np.max(np.abs(u)))
  g=np.rint(g/scale*10**8).astype(np.int64).tolist();u=np.rint(u/scale*10**8).astype(np.int64).tolist()
  assert all(x>=0 for r in u for x in r)
  for b in exact_matrices(TREES[o],ex,rows,g,u):assert positive(b);nm+=1
  records.append(dict(index=k,ordinal=o,extra=ex,rows=rows,g=g,mu=u))
  print('NEW_SHADOW_CERTIFICATE',k,o,list(ex),list(rows),len(u),flush=True)
 obj=dict(tag='NOVA24_F9_11_SHADOW_FRAMES_V1',parents=PARENTS,records=records)
 b=(json.dumps(obj,sort_keys=True,separators=(',',':'))+'\n').encode();Path('shadow_exact.json').write_bytes(b)
 assert nm==3024
 print('NEW_SHADOW_GENERATION_PASS',12,nm,6)
 print('DATA',len(b),hashlib.sha256(b).hexdigest())
