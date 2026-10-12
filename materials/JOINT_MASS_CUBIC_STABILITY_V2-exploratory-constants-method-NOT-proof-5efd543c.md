# material-5efd543c8e6f

AI research material

<!-- historical-status:start -->
> **Historical AI material.** The title and claims below reflect the AI’s assessment at the time. Claims of proof, certification or completion are not a current verification verdict.
>
> [C622](../C622/README.md) passes the supplied exact checks; C<500 remains open; Minimum’s C≥34 remains a working lower bound requiring a consolidated proof. See [verification status and source gaps](../catalog/coverage.md).
<!-- historical-status:end -->

---

"""Exploratory constants only; NOT a proof or a polyhedral construction.
CPython3.13.5 NumPy2.3.5 SciPy1.17.0. No random inputs.
Run: OPENBLAS_NUM_THREADS=1 python explore_constants.py
"""
import numpy as np
from scipy.optimize import minimize_scalar
best=(2,None)
for d in np.linspace(.0001,1,1001):
 def f(u):
  if u>=1:return 1.0
  return (u*u+(d-u)**3/(1-u))/d**3
 z=minimize_scalar(f,bounds=(0,d),method='bounded', options={'xatol':1e-14})
 if z.fun<best[0]:best=(z.fun,(d,z.x))
print('EXPLORATORY_MIN_RATIO',best)
for mode in range(3):
 def bound(h):
  if mode==0: K=3+9*h+5*h*h-2*h**3;den=16
  elif mode==1:K=3+8*h+3*h*h-2*h**3;den=8
  else:K=max(11*h-h**3,3+6*h-h*h);den=8
  gamma=(1-h)**2+.04
  return 3*h**3*gamma**3/(den*(1-h)*K**3)
 z=minimize_scalar(bound,bounds=(7/45,1-1e-10),method='bounded',options={'xatol':1e-14})
 print('EXPLORATORY_GAP_MIN',mode,z.x,z.fun,bound(7/45))
