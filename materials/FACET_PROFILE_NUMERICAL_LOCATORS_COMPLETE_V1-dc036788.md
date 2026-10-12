# material-dc036788bb27

AI research material · [Export notes](../catalog/coverage.md#text-records)

---

# Complete numerical actual-facet locators

These are exploratory floating-point searches, not exact polyhedron acceptance or continuum certificates. They motivated, but do not prove, the open full-matrix inequality B>=Sigma^-1/5 and the separate possible bound alpha c^T Sigma^-1 c<=3/2. The analytic sharp normal theorem and exact algebra are preserved separately in [internal-source-reference] and [internal-source-reference].

The actual hull has a fixed triangular base z=0 and positive-height extra points. Some extra points become redundant: the four best full-matrix locator outputs are all pyramids with additional interior points. They are not examples with the requested number of true vertices, and the counts of sampled calls provide no incidence coverage. No equilibrium census was performed or claimed.

## Complete deterministic inputs, execution and scope

CPython3.13.5, NumPy2.3.5, SciPy1.17.0; single-threaded OpenBLAS. Run from one directory containing the two complete files below:

OPENBLAS_NUM_THREADS=1 python locate.py 4 270927
OPENBLAS_NUM_THREADS=1 python locate.py 2 927261
OPENBLAS_NUM_THREADS=1 python locate.py 6 270928
OPENBLAS_NUM_THREADS=1 python locate.py 9 270929
OPENBLAS_NUM_THREADS=1 python centroid_probe.py 3 270930
OPENBLAS_NUM_THREADS=1 python centroid_probe.py 5 270931

All six commands were actually executed. The full-matrix minimum generalized eigenvalues were respectively .19999999999998674, .19999999999996698, .19999999999997775, .1999999999999998 after7920,1500,18180,27270 calls. Values microscopically below.2 are floating-point roundoff, not certified violations. The n=6 and n=9 searches reached their iteration limits; n=2 and n=4 terminated under their numerical stopping rules.

The two centroid-leverage searches reached iteration limits after14490 and24150 calls, returning maxima1.4946417174622997 and1.4764333639242098. Their corresponding B/Sigma^-1 minimum eigenvalues were .3289993975523679 and .34039346262539133. No universal3/2 theorem follows.

Source pins:
locate.py2553B SHA489fb088d7ef7f1d8f0e80e32cce082ff46a1dfb8611d8e575f65a13a91128b7
centroid_probe.py1040B SHAe2624775597c697952c95f37a3fb2dabb04797d988cad4805285ed782ca30ca2

Observed output pins (the source plus complete seeds/parameters reconstruct the numerical experiments; cross-platform BLAS last-bit identity is not a mathematical claim):
locator_n4_s270927.json2054B SHA30436bd03c4f1b1e552e76e9e5950ac5a8eee9c1f8219a0cc814c74e85a88d6a
locator_n2_s927261.json1872B SHA6460ff69d5b031787979e6c5ef335fa6805de7696e0e9a11c8ef1d9f69c68f91
locator_n6_s270928.json2219B SHAe3ef786e6a884eeb3a8675ddcb1946e1f92da7e4a874808d8a7e82f12d943435
locator_n9_s270929.json2531B SHA4faa75df14e7e609ebbf33123ddb59a8460c3a963619e4ee132dbe4c07443441
centroid_probe_n3_s270930.json2131B SHA6cfb60a115e4e7f8cfbed045e43da5925ec84be9a80925f88a91723ca5c526bf
centroid_probe_n5_s270931.json2460B SHA4055fc3a487aa9dc2a6b8bbf339f3d2f883c3ca89736d12325a13f3458e74c39

The programs print the output filename, number of calls and best numerical value. The source files and inputs below are complete: there is no saved optimizer checkpoint, unsupplied hull file, hidden helper, or exact construction promoted from these numerical outputs.

## locate.py

```python
#!/usr/bin/env python3
"""Numerical locator only for the proposed sharp facet Hessian/covariance bound.
CPython3.13.5 NumPy2.3.5 SciPy1.17.0. Actual hull integration, no free moments.
Fixed base triangle z=0 and any strictly positive-height additional vertices.
"""
import os
os.environ['OPENBLAS_NUM_THREADS']='1'
import json, sys
import numpy as np
from scipy.spatial import ConvexHull, QhullError
from scipy.linalg import eigvalsh
from scipy.optimize import differential_evolution, minimize
BASE=np.array([[0.,0.,0.],[1.,0.,0.],[0.,1.,0.]])
CF=np.array([[1/18,-1/36,0],[-1/36,1/18,0],[0,0,0.]])
def stats(points):
    P=np.vstack((BASE,points)); hull=ConvexHull(P); o=P.mean(axis=0)
    Q=P[hull.simplices]-o
    weights=np.abs(np.linalg.det(Q))/6
    vs=Q.sum(axis=1)
    vol=weights.sum(); shift=(weights[:,None]*vs/4).sum(axis=0)/vol
    second=np.einsum('n,ni,nj->ij',weights,vs,vs)/20
    second+=np.einsum('n,nki,nkj->ij',weights,Q,Q)/20
    cov=second/vol-np.outer(shift,shift)
    g=o+shift; alpha=g[2]/(2*vol)
    c=np.array([1/3,1/3,0.])-g
    T=CF+np.outer(c,c)
    q=np.array([0.,0.,-1/g[2]])
    B=np.linalg.inv(T)/alpha-np.outer(q,q)
    eigen=eigvalsh(B,np.linalg.inv(cov))
    return dict(value=float(eigen[0]),eigen=eigen.tolist(),volume=float(vol),centroid=g.tolist(),alpha=float(alpha),cov=cov.tolist(),c=c.tolist(),T=T.tolist(),B=B.tolist(),points=P.tolist(),faces=hull.simplices.tolist())
def unpack(t):
    a=np.array(t).reshape(-1,3).copy()
    # Heights positive, over several length scales; one affine degree redundant.
    a[:,2]=np.exp(a[:,2])
    return a
COUNT=0; BEST=1e9; RECORD=None
def objective(t):
    global COUNT,BEST,RECORD
    COUNT+=1
    try:
        rec=stats(unpack(t)); val=rec['value']
        if not np.isfinite(val) or val < 0:return 1e5
    except (QhullError,ValueError,np.linalg.LinAlgError):return 1e5
    if val<BEST:
        BEST=val;RECORD=rec
        if val<.19999: print('POSSIBLE_VIOLATION',COUNT,val,flush=True)
    return val
if __name__=='__main__':
    n=int(sys.argv[1]) if len(sys.argv)>1 else 4
    seed=int(sys.argv[2]) if len(sys.argv)>2 else 270927
    bounds=[(-3,3),(-3,3),(-3,3)]*n
    ans=differential_evolution(objective,bounds,rng=np.random.default_rng(seed),maxiter=100,popsize=10,tol=1e-9,polish=False,workers=1)
    rec=RECORD;rec['locator']={'seed':seed,'n':n,'calls':COUNT,'success':bool(ans.success),'message':str(ans.message)}
    name=f'locator_n{n}_s{seed}.json';open(name,'w').write(json.dumps(rec,sort_keys=True,indent=2)+'\n')
    print(name,COUNT,BEST,flush=True)
```

## centroid_probe.py

```python
#!/usr/bin/env python3
"""Numerical actual-facet centroid leverage search, depends on complete locate.py."""
import json,sys,numpy as np
from scipy.optimize import differential_evolution
from locate import stats,unpack
n=int(sys.argv[1]) if len(sys.argv)>1 else 4
seed=int(sys.argv[2]) if len(sys.argv)>2 else 270931
best=-1.;rec=None;calls=0
def obj(t):
    global best,rec,calls
    calls+=1
    try:
        z=stats(unpack(t));c=np.array(z['c']);cov=np.array(z['cov'])
        v=z['alpha']*float(c@np.linalg.solve(cov,c))
        if not np.isfinite(v) or v<0:return 1e9
        if v>best:best=v;rec=z
        return -v
    except Exception:return 1e9
ans=differential_evolution(obj,[(-3,3),(-3,3),(-2,2)]*n,rng=np.random.default_rng(seed),maxiter=160,popsize=10,polish=False,tol=1e-9)
rec['centroid_leverage']=best;rec['locator']={'seed':seed,'n':n,'calls':calls,'success':bool(ans.success)}
name=f'centroid_probe_n{n}_s{seed}.json';open(name,'w').write(json.dumps(rec,indent=2,sort_keys=True)+'\n')
print(name, calls,best,rec['value'])
```
