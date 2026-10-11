# material-21ed1d6ba97c

Historical AI scientific source/proof material. Statements retain their original scope; this is not an independently reviewed theorem.

Public derivative: internal-record-identifiers-replaced.

---

# Seven-corner asymmetry frontier: exploratory, NOT an exclusion

For a rooted seven-corner polygon normalized q0=(1,0), maximize lambda with -lambda Q contained in Q. The two boundary-root branches have lengths (3,3),(4,2),or(5,1). The complete numerical code below used CPython3.13.5, NumPy2.3.5,SciPy1.17.0 and40 seeded starts per split. Observed best lambda values were approximately0.25000000000077544,0.26886098885065296,0.3173827105206873 respectively. All are below1/3 but finite local optimization DOES NOT prove impossibility or a global optimum. The exact positive eight-corner control is [internal-source-reference]; its no-lift theorem is independent of this exploration.

The apparent5+1 extremizer has weak selected arrows and q5=(-lambda,0), q6=-q3. Four last turn angles appear equal to alpha, with t=cos(alpha)^2 near0.720. These equalities suggest 8t^3-8t^2+3t-1=0 and lambda=t(2t-1), matching the observed0.31738271052. This is a candidate normal form, NOT a proved global reduction or certified extremal theorem. To derive it algebraically, write each of the last four steps as multiplication by t+i sqrt(t(1-t)); q3 and q6 opposite with both root/chain weak arrows tight give the cubic. Convexity, all-direction containment and the reduction of an arbitrary seven-corner polygon to this form still require proof. A seven-corner exclusion would strengthen the actual centroid-shadow obstruction independently of extra hidden3D vertices.

The3+3 split is analytically excluded for lambda>=1/3 by the known chain bound: every nonroot point has root-axis coordinate at least -1/4, since its depth is at most3. This observation does not cover4+2 or5+1. The numerical maxima are not accepted bounds.

## Complete source
Save as asymmetry_search.py in the same directory as polygon_search.py from [internal-source-reference]; it imports only that file's complete cross helper. All other inputs and seeds are literal here. Run OPENBLAS_NUM_THREADS=1 python asymmetry_search.py. Outputs asymmetry7_3.npz,asymmetry7_4.npz,asymmetry7_5.npz are numerical locators, not durable proof objects. The exact source is1474 bytes, SHA25680f8fd5fed4d504e11cc7e599a0dd84722326dfabed067810c34aafcc71c384f.

```python
import numpy as np
from scipy.optimize import minimize
from math import pi,cos,sin
from polygon_search import cross

def constraints(v,k,m):
 q=np.vstack(([1.,0.],v[:-1].reshape(-1,2)));e=np.roll(q,-1,axis=0)-q;lam=v[-1]
 inc=cross(e[:,None,:],-lam*q[None,:,:]-q[:,None,:]).ravel()
 cv=cross(e[:,None,:],q[None,:,:]-q[:,None,:]);mask=np.ones((k,k),bool)
 for i in range(k):mask[i,i]=mask[i,(i+1)%k]=False
 ar=[q[i]@(q[i-1 if i<=m else (i+1)%k]-q[i]) for i in range(1,k)]
 return np.r_[inc,cv[mask]-1e-6,np.array(ar),cross(q,np.roll(q,-1,axis=0))-1e-6]
if __name__=='__main__':
 rng=np.random.default_rng(151314);k=7
 for m in [3,4,5]:
  best=None
  for seed in range(40):
   n=k-1-m;aa=rng.uniform(.8,1.2)*pi/(m+1);bb=rng.uniform(.8,1.2)*pi/(n+1)
   q=[[1.,0.]]
   for i in range(1,m+1):q.append([cos(aa)**i*cos(i*aa),cos(aa)**i*sin(i*aa)])
   for j in range(n,0,-1):q.append([cos(bb)**j*cos(j*bb),-cos(bb)**j*sin(j*bb)])
   x=np.r_[np.array(q)[1:].ravel(),.2]
   fit=minimize(lambda x:-x[-1],x,method='SLSQP',constraints=[{'type':'ineq','fun':lambda v:constraints(v,k,m)}],bounds=[(-1,1)]*12+[(.05,.8)],options={'maxiter':1000,'ftol':1e-12})
   if fit.success and (best is None or fit.x[-1]>best.x[-1]):best=fit
  print(m,best.x[-1] if best is not None else 'NONE',flush=True)
  if best is not None:
   print(np.vstack(([1,0],best.x[:-1].reshape(-1,2))),flush=True)
   np.savez('asymmetry7_'+str(m)+'.npz',q=np.vstack(([1,0],best.x[:-1].reshape(-1,2))),lam=best.x[-1],m=m)
```
