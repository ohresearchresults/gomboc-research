# material-438fadc064f1

Historical AI scientific source/proof material. Statements retain their original scope; this is not an independently reviewed theorem.

Public derivative: internal-record-identifiers-replaced.

---

# PAIR_TRIANGLE_LOCATOR_V1 — exploratory method, NOT an exclusion certificate

This preserves the numerical direction that led to a rational six-vertex two-triangle control and then to the exact E17 control [internal-source-reference]. The exact accepted objects and proofs do NOT depend on a floating optimizer outcome: their full rational inputs and exact verification are in [internal-source-reference], [internal-source-reference] and proof [internal-source-reference].

No numerical run here proves an upper bound, an excluded geometry, a global optimum, TREE253 feasibility, or any C improvement. In particular, observing all values below51/25 is NOT evidence of a universal upper bound. The first three runs ended success:false at their iteration limit. The later success:true fields report optimizer convergence criteria, not mathematical optimality.

## Exact reusable source1: search_pair_triangles.py

1516 UTF-8/LF bytes, SHA2569130c45cddc2fed7cbd6514473d133962ff57f2aeb5c3b472b02425cc528326b. Save the following source literally, with final LF.

```python
from pathlib import Path
import json, sys, hashlib
import numpy as np
import scipy
from scipy.spatial import ConvexHull, QhullError
from scipy.optimize import differential_evolution
BASE=np.array([[0.,0.,0.],[0.,0.,1.],[0.,1.,0.],[1.,0.,0.]])
def score(z):
    points=np.concatenate([BASE,np.array(z).reshape(-1,3)])
    try:h=ConvexHull(points)
    except QhullError:return 100.
    tet=points[h.simplices]; cr=np.cross(tet[:,1]-tet[:,0],tet[:,2]-tet[:,0]);sign=np.sign((cr*h.equations[:,:3]).sum(axis=1))
    vol=sign*np.einsum('ij,ij->i',tet[:,0],np.cross(tet[:,1],tet[:,2]))/6
    V=vol.sum()
    if V<=0:return 100.
    g=(vol[:,None]*tet.sum(axis=1)/4).sum(axis=0)/V
    n=h.equations[:,:3]; hs=-h.equations[:,3];hc=hs-n@g
    vals=(g[0]*(hs-(n[:,1]+n[:,2])/3)+g[1]*(hs-(n[:,0]+n[:,2])/3))/(2*V*hc)
    return -float(vals.max())
if __name__=='__main__':
    m=int(sys.argv[1]);seed=int(sys.argv[2]); bounds=[(.0001,3),(.0001,3),(-3,3)]*m
    result=differential_evolution(score,bounds,seed=seed,maxiter=180,popsize=12,tol=1e-9,atol=0,polish=True,workers=1,updating='immediate')
    obj={'m':m,'seed':seed,'bounds':bounds,'maxiter':180,'popsize':12,'tol':1e-9,'atol':0,'polish':True,'workers':1,'updating':'immediate','numpy':np.__version__,'scipy':scipy.__version__,'objective':result.fun,'x':result.x.tolist(),'nfev':result.nfev,'success':bool(result.success)}
    p=Path(f'pair_triangle_search_{m}_{seed}.json');p.write_text(json.dumps(obj,sort_keys=True,separators=(',',':'))+'\n')
    print(p.read_text())
```

The fixed facets are ABC={0,e3,e2} and ABD={0,e3,e1}; all added points have positive first and second coordinates. Thus both fixed triangles are genuine supporting facets away from floating degeneracies. The floating score integrates actual hull volume/centroid, then evaluates the trace sum at each proposed root plane. It still requires a separate exact hull/centroid/facet check before acceptance. Coordinates are bounded only for these searches, not as a theorem about all polyhedra.

## Exact reusable source2: search_pair_branches.py

1486 UTF-8/LF bytes, SHA25609faab6153c89a1cd6354c82f27235bb95f3571dcbff9e09ebcea28ac654e5bc. Save beside source1.

```python
from pathlib import Path
import json, hashlib
import search_pair_triangles as p
from scipy.optimize import differential_evolution

def strip(z):
    h,r=z
    return -(2+2*h*(1+r+r*r)/(1+r))*(2*h+1-r*r)/((1+h)*(h*h+2*h+1-r*r))
def central_lower(z):
    k,r,t,th=z
    return p.score([r/2,r/2,-(1-r)/k,th*(1+k*t),(1-th)*(1+k*t),t,(1-th)*(1+k*t),th*(1+k*t),t])
def central_upper(z):
    k,r,t,th=z
    return p.score([th*r,(1-th)*r,-(1-r)/k,(1-th)*r,th*r,-(1-r)/k,(1+k*t)/2,(1+k*t)/2,t])

if __name__=='__main__':
    jobs=[('strip_cap_relaxation',strip,[(.000001,2),(.000001,.999999)],44,300,15,1e-12),
          ('central_lower_root_polygon',central_lower,[(.05,10),(.0001,.9999),(.0001,3),(.00001,.49)],64,220,12,1e-11),
          ('central_upper_root_polygon',central_upper,[(.05,10),(.0001,.9999),(.0001,3),(.00001,.49)],65,220,12,1e-11)]
    rows=[]
    for name,fn,bounds,seed,maxiter,popsize,tol in jobs:
        result=differential_evolution(fn,bounds,seed=seed,maxiter=maxiter,popsize=popsize,tol=tol,polish=True)
        rows.append({'name':name,'bounds':bounds,'seed':seed,'maxiter':maxiter,'popsize':popsize,'tol':tol,
          'polish':True,'x':result.x.tolist(),'objective':float(result.fun),'nfev':result.nfev,'success':bool(result.success)})
    data=(json.dumps(rows,sort_keys=True,separators=(',',':'))+'\n').encode()
    Path('pair_branch_searches.json').write_bytes(data)
    print(data.decode(),end='');print('BYTES_SHA',len(data),hashlib.sha256(data).hexdigest())
```

The first branch is a scalar strip-cap model, not a claimed universal reduction. The other two put additional points on a root plane x+y-kz=1, one central point on one side of z=0 and a symmetric pair on the other. All these are restricted search directions. The strip expression may be motivated by a lower pyramid with projected root polygon a strip of a reference triangle: area fraction s=1-r^2, centroid radial mean2(1+r+r^2)/(3(1+r)), lower/upper volume ratio h. At the exact axis boundary the originally selected triangles cease to be maximal facets; it is only a limiting relaxation. No proof that all bodies reduce to this family or that the displayed numerical maximum is sharp has been obtained.

## Environment and reconstruction commands

Observed CPython3.13.5, NumPy2.3.5, SciPy1.17.0, Linux x86_64; the locator is not part of the exact acceptance path. Standard SciPy1.17.0 defaults are retained except the explicit source parameters. All random seeds, iteration bounds, populations, coordinate bounds, tolerance and polishing choices are literal above.

OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python search_pair_triangles.py 2 17
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python search_pair_triangles.py 3 23
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python search_pair_triangles.py 2 29
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python search_pair_branches.py

The last source prints BYTES_SHA852 ef0a3ee95050fa904557ce9faf3ef4e57ff81493fd4f41af35d68262e9c3b49f in the observed environment. Floating optimizer transcripts are platform-sensitive; the following complete literal checkpoints, not a promised cross-platform bitwise optimizer behavior, preserve exactly what was observed. They can always be recreated by saving the literal JSON with one final LF. The rational accepted controls instead have platform-independent Fraction checkers.

## Complete observed output checkpoints

pair_triangle_search_2_17.json:402bytes,SHA4236558c23b9ddd1a9bae8dd8e19a9b08a6f73114645569c8556c415925d8a08.

```json
{"atol":0,"bounds":[[0.0001,3],[0.0001,3],[-3,3],[0.0001,3],[0.0001,3],[-3,3]],"m":2,"maxiter":180,"nfev":13256,"numpy":"2.3.5","objective":-2.0286767644121055,"polish":true,"popsize":12,"scipy":"1.17.0","seed":17,"success":false,"tol":1e-09,"updating":"immediate","workers":1,"x":[0.0018209710171357,0.8372865729118226,0.2089761116537228,0.8057376065864866,0.0030831300187275533,0.24831431357409348]}
```

pair_triangle_search_3_23.json:487bytes,SHA76f9865f8e4c3692220288d7ac3412718ca8fda0a2f5f426cd7ff0f58be9bb58.

```json
{"atol":0,"bounds":[[0.0001,3],[0.0001,3],[-3,3],[0.0001,3],[0.0001,3],[-3,3],[0.0001,3],[0.0001,3],[-3,3]],"m":3,"maxiter":180,"nfev":19808,"numpy":"2.3.5","objective":-2.0275423855807917,"polish":true,"popsize":12,"scipy":"1.17.0","seed":23,"success":false,"tol":1e-09,"updating":"immediate","workers":1,"x":[0.8362021568506474,0.02755108791058099,0.18161052714112758,0.07099251378974598,0.7224163790386542,0.27537625086544665,0.443670737445057,0.3188785972346546,0.2911222396917607]}
```

pair_triangle_search_2_29.json:403bytes,SHAe632aa9ed0d7330fbc8600d35c97fa9de48dc9fc16ffdeec5f732729eb48dc57.

```json
{"atol":0,"bounds":[[0.0001,3],[0.0001,3],[-3,3],[0.0001,3],[0.0001,3],[-3,3]],"m":2,"maxiter":180,"nfev":13319,"numpy":"2.3.5","objective":-2.0274453576642535,"polish":true,"popsize":12,"scipy":"1.17.0","seed":29,"success":false,"tol":1e-09,"updating":"immediate","workers":1,"x":[0.7251875049802109,0.006681863427289919,0.34022967722763287,0.0003537389271026202,0.854050190226084,0.1847461574368734]}
```

pair_branch_searches.json:852bytes,SHAef0a3ee95050fa904557ce9faf3ef4e57ff81493fd4f41af35d68262e9c3b49f.

```json
[{"bounds":[[1e-06,2],[1e-06,0.999999]],"maxiter":300,"name":"strip_cap_relaxation","nfev":963,"objective":-2.02878303567339,"polish":true,"popsize":15,"seed":44,"success":true,"tol":1e-12,"x":[0.09603784792394277,0.8302573520784278]},{"bounds":[[0.05,10],[0.0001,0.9999],[0.0001,3],[1e-05,0.49]],"maxiter":220,"name":"central_lower_root_polygon","nfev":5669,"objective":-2.0236695459041814,"polish":true,"popsize":12,"seed":64,"success":true,"tol":1e-11,"x":[3.1040418737722457,0.743292282919542,0.00010000000028442813,0.48999999094150054]},{"bounds":[[0.05,10],[0.0001,0.9999],[0.0001,3],[1e-05,0.49]],"maxiter":220,"name":"central_upper_root_polygon","nfev":6437,"objective":-2.028457416292283,"polish":true,"popsize":12,"seed":65,"success":true,"tol":1e-11,"x":[3.185032120812385,0.8320361903628833,0.00010000000027621248,1.0000429415596424e-05]}]
```

Disposition: USED as a reproducible locator method and as historical evidence for why the eventual rational controls were investigated; EXCLUDED from every universal exclusion, sharpness proof and canonical C/K2/K3 counter. The rigorous sharp triangular-bipyramid result uses the separate exact polynomial elimination source, not these numerical maxima.
