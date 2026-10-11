"""Isolated finite numerical SLSQP subproblem. No optimizer status is a proof."""
import os
os.environ['OPENBLAS_NUM_THREADS']='1'
import sys,json,tempfile,subprocess
from pathlib import Path
import numpy as np

def minqp(A,b):
 norm=np.maximum(np.linalg.norm(A,axis=1),1e-12);A=A/norm[:,None];b=b/norm;scale=max(float(b.max()),1e-4);b/=scale
 with tempfile.TemporaryDirectory() as d:
  p=Path(d);np.savez(p/'in.npz',A=A,b=b)
  try:
   r=subprocess.run([sys.executable,__file__,str(p/'in.npz'),str(p/'out.npz')],capture_output=True,timeout=6)
  except subprocess.TimeoutExpired:return None,dict(qp='bounded QP timeout')
  if r.returncode:return None,dict(qp='worker failed',message=r.stderr.decode()[-300:])
  v=np.load(p/'out.npz');u=v['u'];info=json.loads(str(v['info']))
  info['res']=float((A@u-b).min()*scale)
  if (A@u-b).min()<-1e-8:return None,info
  return u*scale,info

if __name__=='__main__':
 from scipy.optimize import minimize
 v=np.load(sys.argv[1]);A=v['A'];b=v['b'];n=A.shape[1]
 r=minimize(lambda u:.5*u@u,np.zeros(n),jac=lambda u:u,method='SLSQP',constraints={'type':'ineq','fun':lambda u:A@u-b,'jac':lambda u:A},options={'ftol':1e-10,'maxiter':20})
 np.savez(sys.argv[2],u=r.x,info=json.dumps(dict(qp=str(r.message),nit=int(r.nit),success=bool(r.success))))
