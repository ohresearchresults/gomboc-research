# material-4c204d072bc8

AI research material · [Export notes](../catalog/coverage.md#text-records)

---

# PAIR_GENERAL_EXPLORATION_V1

Status: exploratory numerical methods and negative search outcomes, NOT an impossibility certificate and NOT a physical110 construction. The exact counterexample motivated by these calculations is independently preserved and proved in [internal-source-reference] and [internal-source-reference]. All seven original files are literal below; no sandbox is required.

Environment actually used: CPython3.13.5, NumPy2.3.5, SciPy1.17.0, x86_64, OpenBLAS0.3.30 USE64BITINT DYNAMIC_ARCH NO_AFFINITY Haswell MAX_THREADS=64, OPENBLAS_NUM_THREADS=1. Random seeds and every non-default optimization argument are in the full sources. Hull volumes are floating and exploratory; the exact accepted theorem uses only standard-library rational arithmetic in a different preserved source.

The two general searches maximize actual pair trace among convex hulls of the canonical tetrahedron and three coplanar root points, with all other root gaps and xy coordinates varying in the stated bounded boxes. Their approximate endpoints near2.02878288 and gaps tending tozero do not prove a global maximum or an exclusion. A uniform random search found failure of unconditional trace monotonicity under extending C,D to the root plane; the literal floating checkpoint is preserved, and a simpler rational body was separately proved. The last bounded search targeted failure of T(P)<=max(2,T(P')); its positive numerical objective2.22e-15 is roundoff-scale, NOT a counterexample or proof. The stronger high-trace monotonicity statement remains open.

Recovery: save the next complete decoder as recover_pair_exploration.py, save this entire material as MATERIAL.md, then execute `python -S recover_pair_exploration.py MATERIAL.md recovered`. It verifies every input/output snapshot byte pin before writing. These snapshots were produced by the actual runs in this continuation. Bitwise portability of optimizer reruns across different numerical platforms is not asserted. Exact reconstruction of the saved files does not require NumPy or SciPy.

```python
from pathlib import Path
import hashlib,re,sys
assert __debug__
raw=Path(sys.argv[1]).read_text(encoding='utf-8')
out=Path(sys.argv[2]);out.mkdir(parents=True,exist_ok=True)
pat=r'^### FILE (\S+) ([0-9]+) ([a-f0-9]{64})\n```(?:python|json)\n(.*?)\n```'
items=re.findall(pat,raw,re.M|re.S)
assert len(items)==7
for name,size,sha,text in items:
    assert Path(name).name==name
    b=(text+'\n').encode('utf-8')
    assert len(b)==int(size) and hashlib.sha256(b).hexdigest()==sha,name
    (out/name).write_bytes(b)
print('PAIR_GENERAL_EXPLORATION_RECOVERY_PASS',len(items))
```

Numerical rerun commands inside recovered, with the stated packages:
`OPENBLAS_NUM_THREADS=1 python locate_general.py 1729 2718`
`OPENBLAS_NUM_THREADS=1 python extension_test.py`
`OPENBLAS_NUM_THREADS=1 python high_trace_extension.py`
The first creates the two general_seed JSON files; the second creates extension_counter_locator.json; the third creates high_trace_extension.json. Terminal prefixes are ACTUAL_PAIR_NUMERIC, EXTENSION_MONOTONICITY_LOCATOR; the third prints its full result dictionary. Exact snapshot hashes and byte counts are in every FILE header. Bounds, iteration budgets, tolerances and seeds are source data, not omitted defaults invented later.

### FILE locate_general.py 1820 a0a71c28be03de8bf6f2b3aab5a6cf6793acb1c03fb2ec25d3c8916d557a8075
```python
"""Exploratory actual convex-hull pair trace, not an impossibility proof."""
import os
os.environ.setdefault('OPENBLAS_NUM_THREADS','1')
import numpy as np
from scipy.spatial import ConvexHull,QhullError
from scipy.optimize import differential_evolution, minimize
import json,sys
from pathlib import Path
BASE=np.array([[0.,0,0],[0,0,1],[0,1,0],[1,0,0]])
def evaluate(z, detail=False):
    b,c,d=z[:3]; xy=np.asarray(z[3:]).reshape(-1,2)
    h=1-b; alpha=1-d; beta=1-c
    if h<=0:return None if detail else 1e5
    zz=(1-alpha*xy[:,0]-beta*xy[:,1])/h
    P=np.vstack((BASE,np.column_stack((xy,zz))))
    try:H=ConvexHull(P)
    except QhullError:return None if detail else 1e5
    tri=P[H.simplices]
    vol=np.abs(np.linalg.det(tri))/6
    V=vol.sum();g=(vol[:,None]*tri.sum(axis=1)/4).sum(axis=0)/V
    ell=1-alpha*g[0]-beta*g[1]-h*g[2]
    if V<=0 or ell<=0:return None if detail else 1e5
    T=((1+b+c)*g[0]+(1+b+d)*g[1])/(6*V*ell)
    if detail:return {'trace':float(T),'parameters':list(map(float,z)),'vertices':P.tolist(),'hull_vertices':H.vertices.tolist(),'triangles':H.simplices.tolist(),'V':float(V),'g':g.tolist(),'ell_g':float(ell)}
    return -T

def run(seed):
    bounds=[(.02,.999), (0,2),(0,2)]+[(.00001,2)]*6
    res=differential_evolution(evaluate,bounds,seed=seed,maxiter=250,popsize=12,tol=1e-9,polish=False,workers=1,updating='immediate')
    r=minimize(evaluate,res.x,method='Nelder-Mead',options={'maxiter':2500,'xatol':1e-10,'fatol':1e-12},bounds=bounds)
    ans=evaluate(r.x,True); ans['seed']=seed;ans['de_nfev']=res.nfev;ans['local_nfev']=r.nfev
    Path(f'general_seed{seed}.json').write_text(json.dumps(ans,indent=2)+'\n')
    print('ACTUAL_PAIR_NUMERIC',seed,ans['trace'],ans['parameters'],flush=True)
if __name__=='__main__':
    for seed in map(int,sys.argv[1:] or ['1729']):run(seed)
```

### FILE extension_test.py 1218 0b83f0a40493dfde66bf1cf3f3ed56115b6ee7d851b71aabc45b595de514cf8f
```python
"""Test an unproved monotonic extension of actual bodies; numerical locator only."""
import os
os.environ.setdefault('OPENBLAS_NUM_THREADS','1')
from locate_general import evaluate,BASE
from scipy.spatial import ConvexHull
import numpy as np,json
from pathlib import Path
rng=np.random.default_rng(314159)
def trace_ext(z):
    b,c,d=z[:3];h=1-b;alpha=1-d;beta=1-c
    xy=np.asarray(z[3:]).reshape(-1,2)
    zz=(1-alpha*xy[:,0]-beta*xy[:,1])/h
    P=np.vstack((BASE,np.column_stack((xy,zz)),[0,1/beta,0],[1/alpha,0,0]))
    H=ConvexHull(P);tri=P[H.simplices];v=np.abs(np.linalg.det(tri))/6;V=v.sum()
    g=np.sum(v[:,None]*tri.sum(axis=1)/4,axis=0)/V
    ell=1-alpha*g[0]-beta*g[1]-h*g[2]
    return (1+b)*(g[0]/beta+g[1]/alpha)/(6*V*ell)
best=None
for i in range(10000):
    z=np.r_[rng.uniform(.01,.99),rng.uniform(.001,.9,2),rng.uniform(.001,3,6)]
    original=-evaluate(z);extended=trace_ext(z)
    delta=original-extended
    if best is None or delta>best['delta']:
        best=dict(parameters=z.tolist(),original=original,extended=extended,delta=delta,index=i,seed=314159)
Path('extension_counter_locator.json').write_text(json.dumps(best,indent=2)+'\n')
print('EXTENSION_MONOTONICITY_LOCATOR',best,flush=True)
```

### FILE high_trace_extension.py 1265 a75884734371b9df4933fbbe1f7c858700a96de253c0c0a379bc1c2223e41d3e
```python
"""Exploratory counterexample search to T(P)<=max(2,T(extended P))."""
import os
os.environ.setdefault('OPENBLAS_NUM_THREADS','1')
from locate_general import evaluate
from scipy.spatial import ConvexHull
from scipy.optimize import differential_evolution
import numpy as np,json
from pathlib import Path
BASE=np.array([[0.,0,0],[0,0,1],[0,1,0],[1,0,0]])
def ext(z):
    b,c,d=z[:3];h=1-b;alpha=1-d;beta=1-c
    xy=np.asarray(z[3:]).reshape(-1,2);zz=(1-alpha*xy[:,0]-beta*xy[:,1])/h
    P=np.vstack((BASE,np.column_stack((xy,zz)),[0,1/beta,0],[1/alpha,0,0]))
    try:H=ConvexHull(P)
    except Exception:return 100
    tri=P[H.simplices];v=np.abs(np.linalg.det(tri))/6;V=v.sum()
    g=np.sum(v[:,None]*tri.sum(axis=1)/4,axis=0)/V
    ell=1-alpha*g[0]-beta*g[1]-h*g[2]
    return (1+b)*(g[0]/beta+g[1]/alpha)/(6*V*ell)
def fun(z):return evaluate(z)+max(2,ext(z))
bounds=[(.01,.99),(0,.99),(0,.99)]+[(.00001,4)]*6
res=differential_evolution(fun,bounds,seed=57721,maxiter=450,popsize=16,tol=1e-8,polish=False,workers=1,updating='immediate')
ans={'seed':57721,'params':res.x.tolist(),'original':-evaluate(res.x),'extended':ext(res.x),'difference':-res.fun,'nfev':res.nfev}
Path('high_trace_extension.json').write_text(json.dumps(ans,indent=2)+'\n');print(ans,flush=True)
```

### FILE general_seed1729.json 1427 c200cbbd032ad99d2815cd7832b7e0129cbaa209aadefd50afae1d00344b88fa
```json
{
  "trace": 2.0287828753621784,
  "parameters": [
    0.23614053721157252,
    6.228434571243846e-10,
    2.1570896623320678e-10,
    0.8305549263411851,
    1.023303165540035e-05,
    1.0021197070968828e-05,
    0.8302419794884295,
    0.8302551849953571,
    1e-05
  ],
  "vertices": [
    [
      0.0,
      0.0,
      0.0
    ],
    [
      0.0,
      0.0,
      1.0
    ],
    [
      0.0,
      1.0,
      0.0
    ],
    [
      1.0,
      0.0,
      0.0
    ],
    [
      0.8305549263411851,
      1.023303165540035e-05,
      0.2218141543835974
    ],
    [
      1.0021197070968828e-05,
      0.8302419794884295,
      0.2222241238093152
    ],
    [
      0.8302551849953571,
      1e-05,
      0.2222068632417473
    ]
  ],
  "hull_vertices": [
    0,
    1,
    2,
    3,
    4,
    5,
    6
  ],
  "triangles": [
    [
      2,
      3,
      0
    ],
    [
      1,
      3,
      0
    ],
    [
      1,
      2,
      0
    ],
    [
      5,
      2,
      3
    ],
    [
      5,
      1,
      2
    ],
    [
      6,
      1,
      3
    ],
    [
      6,
      5,
      1
    ],
    [
      4,
      5,
      3
    ],
    [
      4,
      6,
      3
    ],
    [
      4,
      6,
      5
    ]
  ],
  "V": 0.18267334948830447,
  "g": [
    0.2582501946168023,
    0.2582508348671092,
    0.25707607325287896
  ],
  "ell_g": 0.28712897952194266,
  "seed": 1729,
  "de_nfev": 27108,
  "local_nfev": 2260
}
```

### FILE general_seed2718.json 1371 7055a64838c2021381577be3c87e26ae7d838a3eed4fb6ffa04ecef543e1c0bb
```json
{
  "trace": 2.028782876073726,
  "parameters": [
    0.23613385036738055,
    1.2466221887094645e-13,
    1.690568842665443e-15,
    0.7661557413949811,
    0.17360505252595865,
    0.8302469387101008,
    1.0000001639977019e-05,
    1.0000017156499473e-05,
    0.8302458498059749
  ],
  "vertices": [
    [
      0.0,
      0.0,
      0.0
    ],
    [
      0.0,
      0.0,
      1.0
    ],
    [
      0.0,
      1.0,
      0.0
    ],
    [
      1.0,
      0.0,
      0.0
    ],
    [
      0.7661557413949811,
      0.17360505252595865,
      0.0788609445621528
    ],
    [
      0.8302469387101008,
      1.0000001639977019e-05,
      0.2222157132763355
    ],
    [
      1.0000017156499473e-05,
      0.8302458498059749,
      0.2222171387730826
    ]
  ],
  "hull_vertices": [
    0,
    1,
    2,
    3,
    5,
    6
  ],
  "triangles": [
    [
      2,
      3,
      0
    ],
    [
      1,
      3,
      0
    ],
    [
      1,
      2,
      0
    ],
    [
      6,
      2,
      3
    ],
    [
      6,
      1,
      2
    ],
    [
      5,
      1,
      3
    ],
    [
      5,
      6,
      3
    ],
    [
      5,
      6,
      1
    ]
  ],
  "V": 0.18267294423460925,
  "g": [
    0.25825026390024725,
    0.25825031682458327,
    0.2570759363322394
  ],
  "ell_g": 0.2871278136258939,
  "seed": 2718,
  "de_nfev": 27108,
  "local_nfev": 2719
}
```

### FILE extension_counter_locator.json 374 4cf3814f754a4ffe96dbffae24739135db7fb2a01b3a69a08bc41351539204b4
```json
{
  "parameters": [
    0.8034839694186114,
    0.8904090707316346,
    0.4026667517925239,
    2.317174065786761,
    1.472940746110634,
    2.6622310228807198,
    1.8366261934155284,
    2.7831899544627063,
    2.6226631779316634
  ],
  "original": 1.1206559922666661,
  "extended": 0.9649863336751482,
  "delta": 0.15566965859151793,
  "index": 4029,
  "seed": 314159
}
```

### FILE high_trace_extension.json 389 89cf4f27b9ec5a161f050ac1bec3b11dbb400d2302c510272273eb1371417dc2
```json
{
  "seed": 57721,
  "params": [
    0.03674207370198984,
    1.3711254354120683e-14,
    8.271161533457416e-15,
    0.04262337331061783,
    0.8742989632145484,
    0.09954925633364287,
    0.8823999755032168,
    0.9252364074973809,
    0.01569848004625496
  ],
  "original": 2.0041682043125326,
  "extended": 2.0041682043125304,
  "difference": 2.220446049250313e-15,
  "nfev": 64944
}
```
