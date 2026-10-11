"""Numerical inverse of the globally one-to-one projective own-centroid map.
Every target is a true filled centroid after solving, not a reference used on old K.
"""
import os
os.environ.setdefault('OPENBLAS_NUM_THREADS','1');os.environ.setdefault('OMP_NUM_THREADS','1')
import numpy as np,json
from pathlib import Path
from orbit_search import Orbit
from projective_screen import state

def invert(model,target):
 target=np.asarray(target,float);t=np.zeros(3);history=[]
 for k in range(100):
  y,g,C,d,V=state(model,t);gradient=4*(target-g);hessian=20*C+4*np.outer(g,g);error=float(np.linalg.norm(target-g,np.inf));history.append(dict(iteration=k,error=error,min_den=float(d.min())))
  if error<5e-12*(1+np.linalg.norm(target,np.inf)):break
  delta=-np.linalg.solve(hessian,gradient);slope=gradient@delta;assert slope<0
  objective=np.log(V)+4*target@t;alpha=1.
  for back in range(70):
   tt=t+alpha*delta
   if (1+model.X@tt).min()>0:
    yy,gg,CC,dd,VV=state(model,tt);trial=np.log(VV)+4*target@tt
    if trial<=objective+1e-4*alpha*slope or (alpha<1e-4 and np.linalg.norm(gg-target)<np.linalg.norm(g-target)):break
   alpha*=.5
  else:raise ArithmeticError('Line search did not certify a numerical decrease')
  t=tt
 else:raise ArithmeticError('Finite Newton iteration limit')
 y,g,C,d,V=state(model,t)
 return dict(target=target.tolist(),t=t.tolist(),actual_projective_centroid=g.tolist(),error=float(np.linalg.norm(g-target,np.inf)),min_den=float(d.min()),volume=float(V),iterations=k,history=history)

def main():
 import sys
 m=Orbit(sys.argv[1]);targets=[[0,0,0],[.5,0,0],[0,-1,0],[0,0,2],[3,1,5]];r=[invert(m,t) for t in targets]
 Path(sys.argv[2]).write_text(json.dumps(dict(status='FIVE_NUMERICAL_TRUE_MASS_INVERSE_TESTS_PASS',tests=r),sort_keys=True))
 for d in r:print(d['target'],d['iterations'],d['error'],d['min_den'],d['t'])
 print('FIVE_NUMERICAL_TRUE_MASS_INVERSE_TESTS_PASS')
if __name__=='__main__':main()
