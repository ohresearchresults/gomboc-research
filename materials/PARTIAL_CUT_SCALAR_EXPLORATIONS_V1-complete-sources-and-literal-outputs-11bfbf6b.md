# material-11bfbf6b5f80

AI research material · [Export notes](../catalog/coverage.md#text-records)

---

# PARTIAL_CUT_SCALAR_EXPLORATIONS_V1

## Evidence status

Two reproducible numerical explorations preceded the exact second-moment theorem and the exact rational scalar barrier in [internal-source-reference] / source [internal-source-reference]. Neither exploration constructs a polytope, a complete Lambda, a joint metric or an equilibrium witness. Both optimizers ended with success=false and 'Maximum number of iterations has been exceeded.' No global optimizer result, feasible physical body, infeasibility theorem or optimal threshold is inferred.

The first relaxation additionally omitted the individual root trace caps. The second retained both masses and both root coefficients with the rational cap111/100, but neither included the mandatory boundary second-moment inequality. Both reported masses are below37/50, and so cannot represent a high-trace physical subset under the subsequently proved theorem. The precise mathematical failure of cuts alone is certified separately by the complete rational scalar point and its17positive Bernstein coefficients, not by these floating runs.

The initial first-source docstring incorrectly said 'no RNG'; the preserved source corrects that comment to 'seeded DE'. Executed parameters, algorithms and outputs are unchanged. Both source-only cold reruns after the correction reproduced the two JSON outputs byte-for-byte.

Environment actually observed: CPython3.13.5 (GCC14.2.0),NumPy2.3.5,SciPy1.17.0. Set OPENBLAS_NUM_THREADS=1 for each process. The scalar arithmetic uses NumPy vectors and SciPy differential_evolution. All non-default arguments, seeds, bounds, tolerances, finite penalties and grid endpoints are literal in the sources. No input files, credentials or external geometry are needed. Under these pinned versions the remaining optimizer options are their library defaults; no omitted custom callback, constraint, initialization or solver setting was used.

## Exact files and commands

Save each of the following four blocks under its stated filename, UTF-8/LF with exactly one final LF. The two JSON blocks are the literal observed outputs, retained independently of a future optimizer installation.

Manifest:

explore_partial_cut.py:2055bytes,SHA256ad88f87410a06d3ccafff736ce6ddae7380a1e674499668abc228d421b211f18.
explore_partial_cut_coupled.py:2167bytes,SHA256dcf5c2b656fd6c5f48a89e4951598426ce946345cbef575e892f5ee38f438012.
partial_cut_explore.json:557bytes,SHA25682ca88e1ce30a8ceeccad5388d0d84d93e826183506a68dae3a2c1651e06bbf4.
partial_cut_coupled_explore.json:719bytes,SHA2563d598c55d08c41190d517257b9806de44b3b6863e8575cb97d4e81bc51e34b78.

Reconstruction commands:

OPENBLAS_NUM_THREADS=1 python explore_partial_cut.py
OPENBLAS_NUM_THREADS=1 python explore_partial_cut_coupled.py

The printed reports must contain success=false,nfev4356 and12060 respectively,with the literal maximum-iteration message. A successful recovery does NOT change that mathematical status.

Exact verification command, standard library only:

```python
from pathlib import Path
import hashlib
pins={
'explore_partial_cut.py':(2055,'ad88f87410a06d3ccafff736ce6ddae7380a1e674499668abc228d421b211f18'),
'explore_partial_cut_coupled.py':(2167,'dcf5c2b656fd6c5f48a89e4951598426ce946345cbef575e892f5ee38f438012'),
'partial_cut_explore.json':(557,'82ca88e1ce30a8ceeccad5388d0d84d93e826183506a68dae3a2c1651e06bbf4'),
'partial_cut_coupled_explore.json':(719,'3d598c55d08c41190d517257b9806de44b3b6863e8575cb97d4e81bc51e34b78')}
for name,pin in pins.items():
    data=Path(name).read_bytes()
    assert (len(data),hashlib.sha256(data).hexdigest())==pin,name
print('PARTIAL_CUT_EXPLORATIONS_EXACT_RECOVERY_PASS_UNKNOWN_NOT_BODY')
```

## Complete explore_partial_cut.py

```python
"""Exploratory necessary-system calculation, not a body or an exclusion proof.
CPython3.13.5, NumPy2.3.5, SciPy1.17.0; seeded DE, fixed cut grids.
"""
import json
from pathlib import Path
import numpy as np
from scipy.optimize import differential_evolution, minimize_scalar
T=51/25; CAP=111/100

def values(h,m,q,count=401):
    # p(C)=p(D)=s; cut t=1-(1-s)k, k in (0,min(1,1/(1-s))).
    ds=3*h/m
    k=np.linspace(1e-7,min(1.,1/ds)-1e-7,count)
    t=1-ds*k
    A=t*t+t*(1-k)+(1-k)**2
    B=k*(t+2*(1-k))
    L=t*k/3*(m*q*A+(3*T-m*q)*B+m*(1-t)*(2*t+1-k))
    f=3*k*k-2*k**3
    I=2*k**3-1.5*k**4
    Z=f-ds*I
    Mhi=min(.75,m-.75*h); Mlo=m-Mhi
    W=3*T-m*q
    if W < -1e-10 or W>4*m+1e-10: return None
    S=W/Mhi if W<=4*Mhi else 4+(W-4*Mhi)/Mlo
    if h*(q+S)>4+1e-10:return None
    J=q*(1.5*k*k-2*k**3+.75*k**4)+S*(k**3-.75*k**4)
    denom=1-h*J
    if np.any(denom<=0):return None
    bounds=L*(1+h*Z/(t*(1-h*f)))/denom
    j=int(np.argmax(bounds))
    return float(bounds[j]),float(k[j]),float(t[j]),float(S)

def objective(v):
    h=v[0]
    lo=max(T/4,1.5*h);hi=.75*(1+h)
    if lo>hi:return 100
    m=lo+v[1]*(hi-lo)
    qlo=max(0,8*T-16,3*T/m-4);qhi=min(8,3*T/m)
    q=qlo+v[2]*(qhi-qlo)
    r=values(h,m,q)
    if r is None:return 100
    return r[0]
if __name__=='__main__':
    result=differential_evolution(objective,[(1/24,25/26),(0,1),(0,1)],seed=20260918,popsize=12,maxiter=120,tol=1e-10,polish=False,workers=1,updating='immediate')
    h=result.x[0];lo=max(T/4,1.5*h);hi=.75*(1+h);m=lo+result.x[1]*(hi-lo)
    qlo=max(0,8*T-16,3*T/m-4);qhi=min(8,3*T/m);q=qlo+result.x[2]*(qhi-qlo)
    out={'exploratory_only':True,'success':bool(result.success),'message':str(result.message),'nfev':int(result.nfev),'x':result.x.tolist(),'h':float(h),'m':float(m),'q':float(q),'best':values(h,m,q,10001),'cap':CAP,'seed':20260918,'popsize':12,'maxiter':120,'tol':1e-10,'polish':False,'workers':1,'updating':'immediate'}
    Path('partial_cut_explore.json').write_text(json.dumps(out,sort_keys=True,indent=2)+'\n')
    print(json.dumps(out,indent=2))
```

## Complete explore_partial_cut_coupled.py

```python
"""Exploratory actual-mass necessary system; not a body or an exclusion proof.
CPython3.13.5 NumPy2.3.5 SciPy1.17.0; deterministic seeded DE.
The earlier relaxation omitted individual root trace caps; this version retains
both m_i and both root coefficients, but NOT full physical realizability.
"""
import json
from pathlib import Path
import numpy as np
from scipy.optimize import differential_evolution
T=51/25;CAP=111/100

def parameters(v):
    h=v[0];mlo=max(T/4,1.5*h);mhi=.75*(1+h)
    if mlo>mhi:return None
    m=mlo+v[1]*(mhi-mlo)
    m1lo=max(m/2,.75*h,m-.75);m1hi=min(.75,m-.75*h)
    if m1lo>m1hi:return None
    m1=m1lo+v[2]*(m1hi-m1lo);m2=m-m1
    u=T-CAP+v[3]*(2*CAP-T)
    c0=3*u/m1;d0=3*(T-u)/m2
    qlo=max(0,8*T-16,c0-4,d0-4,c0+d0-4/h)
    qhi=min(8,c0,d0)
    if qlo>qhi:return None
    q=qlo+v[4]*(qhi-qlo);c=c0-q;d=d0-q
    return h,m,m1,m2,u,q,c,d

def cuts(h,m,m1,m2,u,q,c,d,count=401):
    ds=3*h/m;k=np.linspace(1e-7,min(1.,1/ds)-1e-7,count);t=1-ds*k
    A=t*t+t*(1-k)+(1-k)**2;B=k*(t+2*(1-k))
    L=t*k/3*(m*q*A+(3*T-m*q)*B+m*(1-t)*(2*t+1-k))
    f=3*k*k-2*k**3;I=2*k**3-1.5*k**4;Z=f-ds*I
    J=q*(1.5*k*k-2*k**3+.75*k**4)+(c+d)*(k**3-.75*k**4)
    denom=1-h*J
    if np.any(denom<=0):return None
    bounds=L*(1+h*Z/(t*(1-h*f)))/denom
    j=int(np.argmax(bounds))
    return float(bounds[j]),float(k[j]),float(t[j])

def objective(v):
    p=parameters(v)
    if p is None:return 100
    r=cuts(*p)
    return r[0] if r is not None else 100
if __name__=='__main__':
    result=differential_evolution(objective,[(1/24,25/26)]+[(0,1)]*4,seed=20260919,popsize=12,maxiter=200,tol=1e-10,polish=False,workers=1,updating='immediate')
    p=parameters(result.x)
    out={'exploratory_only':True,'success':bool(result.success),'message':str(result.message),'nfev':int(result.nfev),'x':result.x.tolist(),'parameters':list(map(float,p)) if p else None,'best':cuts(*p,count=10001) if p else None,'cap':CAP,'seed':20260919,'popsize':12,'maxiter':200,'tol':1e-10,'polish':False,'workers':1,'updating':'immediate'}
    Path('partial_cut_coupled_explore.json').write_text(json.dumps(out,sort_keys=True,indent=2)+'\n')
    print(json.dumps(out,indent=2))
```

## Literal partial_cut_explore.json

```json
{
  "best": [
    0.4796198037102351,
    0.2646097915177301,
    0.5548999815305465,
    4.053620510710353
  ],
  "cap": 1.11,
  "exploratory_only": true,
  "h": 0.33185053165136613,
  "m": 0.5918505707813775,
  "maxiter": 120,
  "message": "Maximum number of iterations has been exceeded.",
  "nfev": 4356,
  "polish": false,
  "popsize": 12,
  "q": 7.999998731669015,
  "seed": 20260918,
  "success": false,
  "tol": 1e-10,
  "updating": "immediate",
  "workers": 1,
  "x": [
    0.33185053165136613,
    0.1674219611337816,
    0.9999992357389712
  ]
}
```

## Literal partial_cut_coupled_explore.json

```json
{
  "best": [
    0.4964478814612717,
    0.31512080794341074,
    0.532299990412115
  ],
  "cap": 1.11,
  "exploratory_only": true,
  "maxiter": 200,
  "message": "Maximum number of iterations has been exceeded.",
  "nfev": 12060,
  "parameters": [
    0.2560619578976059,
    0.5175782514567346,
    0.2774979322167041,
    0.24008031924003054,
    1.1099895676289095,
    7.999998677920244,
    3.9999779571715237,
    3.6212425214627793
  ],
  "polish": false,
  "popsize": 12,
  "seed": 20260919,
  "success": false,
  "tol": 1e-10,
  "updating": "immediate",
  "workers": 1,
  "x": [
    0.2560619578976059,
    0.017540361999467735,
    0.28031258034566636,
    0.9999420423828299,
    0.10098023438643478
  ]
}
```
