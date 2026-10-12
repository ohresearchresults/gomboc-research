"""Dual active-set minimum-norm halfspace projection, with equality elimination.
Numerical proposal solver. All returned inequalities are checked in original scale.
"""
import time
import numpy as np
from scipy.linalg import qr,solve_triangular

def solve(A,b,E=None,r=None,bound=.02,tol=2e-9,seconds=8,maxsteps=2000):
 t0=time.monotonic();A=np.asarray(A,float);b=np.asarray(b,float);n=A.shape[1]
 if E is None or len(E)==0:x0=np.zeros(n);P=np.eye(n)
 else:
  E=np.asarray(E,float);r=np.asarray(r,float);Q,R=qr(E.T,mode='economic',check_finite=False);x0=Q@solve_triangular(R.T,r,lower=True,check_finite=False);P=np.eye(n)-Q@Q.T
 if bound is not None:A=np.r_[A,np.eye(n),-np.eye(n)];b=np.r_[b,-np.ones(n)*bound,-np.ones(n)*bound]
 B=A@P;d=b-A@x0;sc=np.linalg.norm(B,axis=1);zero=sc<1e-13
 if np.any(d[zero]>tol):return None,{'why':'zero-row','steps':0}
 sc=np.maximum(sc,1e-13);B=B/sc[:,None];d=d/sc
 y=np.zeros(n);W=[];lam=np.empty(0);removes=0;inner=0
 for it in range(maxsteps):
  v=B@y-d;i=int(np.argmin(v));vmin=v[i]
  if vmin>=-tol:
   x=x0+y
   if np.min((A@x-b)/np.maximum(np.linalg.norm(A,axis=1),1e-13))<-5*tol:return None,{'why':'postguard','steps':it}
   return x,{'why':'pass','steps':it,'active':len(W),'removes':removes,'sec':time.monotonic()-t0,'min':float(vmin)}
  if time.monotonic()-t0>seconds:return None,{'why':'time','steps':it,'active':len(W),'sec':time.monotonic()-t0,'min':float(vmin)}
  if i in W:return None,{'why':'working-error','min':float(vmin),'steps':it}
  ln=0.
  while True:
   inner+=1
   if inner>maxsteps*5:return None,{'why':'inner-budget','steps':it}
   if W:
    Q,R=qr(B[W].T,mode='economic',check_finite=False)
    try:rr=solve_triangular(R,Q.T@B[i],check_finite=False)
    except Exception:return None,{'why':'singular','steps':it}
    z=B[i]-Q@(Q.T@B[i])
   else:rr=np.empty(0);z=B[i].copy()
   zz=float(z@z);full=(d[i]-B[i]@y)/zz if zz>1e-20 else np.inf
   rates=np.divide(lam,rr,out=np.full_like(lam,np.inf),where=rr>1e-11);j=int(np.argmin(rates)) if len(rates) else -1;part=rates[j] if j>=0 else np.inf
   if full< -tol:return None,{'why':'overshot','steps':it,'full':full}
   t=min(full,part)
   if not np.isfinite(t) or t>1e15:return None,{'why':'infeasible-or-illconditioned','steps':it,'zz':zz}
   t=max(t,0.);y+=t*z;lam-=t*rr;ln+=t
   if full<=part:
    W.append(i);lam=np.r_[lam,ln];break
   else:
    W.pop(j);lam=np.delete(lam,j);removes+=1
 return None,{'why':'budget','steps':maxsteps,'active':len(W)}
