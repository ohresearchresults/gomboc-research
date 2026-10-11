"""Strict physical retracted persistence flow with a convex quadratic predictor.
The quadratic regularizer discourages alternating distant trust-box corners.
SLSQP solves only the convex predictor; all actual geometry is rechecked.
"""
import sys
from pathlib import Path
import numpy as np
from scipy.optimize import minimize
from types import SimpleNamespace
import canonical_projected_boxflow as base
old_linprog=base.linprog
qp_rows=[]
def quadratic_predictor(cost,**kw):
 # Corrector is the separately specified exact L1 LP and remains an LP.
 if 'A_ub' not in kw or len(cost)!=len(kw['bounds']) or len(cost)>400 or kw['bounds'][0][0] is None or kw['bounds'][-1][0]==0:
  return old_linprog(cost,**kw)
 lo,hi=kw['bounds'][0]
 if lo is None or hi is None or abs(lo+hi)>1e-12:return old_linprog(cost,**kw)
 bound=hi;A=np.asarray(kw['A_ub']);b=np.asarray(kw['b_ub']);A=A*bound;norm=np.linalg.norm(A,axis=1);keep=norm>1e-20;A=A[keep]/norm[keep,None];b=b[keep]/norm[keep];g=np.asarray(cost)*bound;scale=np.linalg.norm(g);g=g/max(scale,1e-30);lam=.08/np.sqrt(len(g))
 def fun(x):return g@x+.5*lam*(x@x)
 def jac(x):return g+lam*x
 cons={'type':'ineq','fun':lambda x:b-A@x,'jac':lambda x:-A}
 opt=minimize(fun,np.zeros(len(g)),jac=jac,method='SLSQP',bounds=[(-1,1)]*len(g),constraints=[cons],options={'ftol':1e-11,'maxiter':250,'disp':False})
 residual=float(np.max(A@opt.x-b,initial=0));success=bool(opt.success and residual<1e-7);qp_rows.append(dict(success=success,iterations=int(opt.nit),residual=residual,message=str(opt.message)))
 if len(qp_rows)%10==0:print('QUADRATIC_PREDICTOR',qp_rows[-1],flush=True)
 return SimpleNamespace(success=success,x=opt.x*bound,message=f'convexQP: {opt.message}; maxviolation={residual:g}')
base.linprog=quadratic_predictor
if __name__=='__main__':
 f=base.ROOT/(sys.argv[1] if len(sys.argv)>1 else 'artifacts/canonical_atlas/contactwall_C494');inp=f/(sys.argv[2] if len(sys.argv)>2 else 'screen_projected1/source_q.npy');base.run(f,f/'projected_qpflow',inp,iters=500)
