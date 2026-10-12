# material-814a0940bfc2

AI research material · [Export notes](../catalog/coverage.md#text-records)

<!-- historical-status:start -->
> **Historical AI material.** The title and claims below reflect the AI’s assessment at the time. Claims of proof, certification or completion are not a current verification verdict.
>
> [C622](../C622/README.md) passes the supplied exact checks; C<500 remains open; Minimum’s C≥34 remains a working lower bound requiring a consolidated proof. See [verification status and source gaps](../catalog/coverage.md).
<!-- historical-status:end -->

---

# J113 numerical producers — recovery part1/2, original twisted trees and transverse metrics

These are complete EXECUTED numerical producing units. They are not exact equilibrium certificates. The four selected exact own132 bodies have independent literal integer recovery in [internal-source-reference], J113_C2_POLAR_EXACT_RECOVERY.md; no numerical optimization is required to reconstruct those rational bodies.

For this numerical pipeline create sibling directories j109 and j113. Extract the complete geometry109.py FILE block from [internal-source-reference] into j109. Extract these two files and the two files in J113_NUMERICAL_PRODUCERS_PART2_OF2.md into j113. Only geometry109.py is imported from the earlier material: R82.txt is NOT used or needed for this new generated family. The helper's load() routine is not called. For the fullmetric stage, also reconstruct the exact J113 inputs/audits in j113 using the exact capsule. Execute in order with OPENBLAS_NUM_THREADS=1: twist113.py, metric113.py, joint113.py, fullmetric113.py. This is the complete deterministic seeded numerical pipeline and every non-default parameter; there is no external checkpoint or hidden seed. Observed environment CPython3.13.5, NumPy2.3.5, SciPy1.17.0.

Eight original scouts varied two polar paths and their C2 partners. Each path uses monotone polar angles, sinusoidal azimuthal twist and lengths obtained from positive cosine-step guards, with a common negative endpoint z coefficient producing an axial physical vertex. The initial generator additionally requires d>1/3. It maximizes actual homogeneous centroid z, not a prescribed reference-point surrogate. Modes0/1 use first/second azimuthal sine harmonics; depths6/10/14/20 fit the H budget. The respective best centroid z values were approximately (-.1186495526,-.0319860961,.0303394611,.0838343577) and(-.0127909661,.0436321939,.0898441097,.1225477001). Original nominal own S/U counts were(1,5),(13,7),(1,3),(1,3) and(5,5),(1,3),(1,3),(1,3). Positive centroid alone is not S1; the complete census determines it. Four literal rational freezes were separately exactly accepted as own132/weak000, not110.

The eight transverse-affine continuations tried to make the axial vertex the unique U while retaining input0 as the unique S, using the actual full true-edge angular-escape objective at the actual homogeneous centroid. They did not reach110. A small angular residual was misleading: the smallest such residual, about .001118, still had a deep P bar about .9567 and many other equilibria. The joint stage in part2 consequently adds necessary global root-norm ordering to both landscapes. These are finite restricted optimizer outputs, not affine-orbit exclusions.

Observed manifests:
- geometry109.py4286B SHA5a61893fd75b1e7e8d261bbbe0f42ca88a2c53dadf65da8e38aa723068189479, complete dependency in the earlier material.
- twist113.py3998B SHAee53eff5db61616aae5c057994117ab4a9a962a9cc2f0db26577076a64d155d5.
- metric113.py2798B SHA5ed4ab89cd985363caf0c83ac60f0783e64a96ed416c8b6bb293a9d8e232cf37.
- Generated TWIST113.json102324B SHAe8950cbf54dbe41252eed4aa3da55bceb1fcda14b258990f9225d74240a31f87.
- Generated METRIC113.json64873B SHA2344c593751c436796aef88ef8aad2c392a8e07038120e34944def8b174363cd.
Terminal markers TWIST113_NUMERICAL_FINISHED8 and METRIC113_NUMERICAL_FINISHED8. The JSON contains every selected normal, numerical actual/reference P/Q landscape, finite input parameter and optimizer status. These hashes identify observed outputs and are NOT a cross-platform floating optimizer portability guarantee. The exact rational nonwinners instead have directly preserved literal integer inputs and a standard-library exact replay. This distinction is intentional.

### FILE twist113.py
```python
"""From-scratch C2 polar radial trees; actual homogeneous mass, numerical only.
Complete dependencies: geometry109.py from the J109 numerical material.
No R82 data are used: this is a new generated family, not an R82 descendant.
"""
from __future__ import annotations
import sys,json,time
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'j109'))
from geometry109 import mass,from_h,census
import numpy as np
from scipy.spatial import ConvexHull,QhullError
from scipy.optimize import differential_evolution
ROOT=Path(__file__).resolve().parent

def generate(x,depth,mode):
    a,b,f,g,offset,fraction=x
    t=np.arange(1,depth+1)/depth
    end=depth*np.pi/(depth+1)
    qs=[];maxbottom=[];scores=[]
    for amp,twist,base in ((a,f,0.),(b,g,offset)):
        theta=end*t+amp*np.sin(np.pi*t)
        if np.min(theta)<=0 or np.max(theta)>=np.pi or np.min(np.diff(theta))<=0:raise ValueError('theta')
        wave=np.sin(np.pi*t) if mode==0 else np.sin(2*np.pi*t)
        phi=base+twist*wave
        direction=np.c_[np.sin(theta)*np.cos(phi),np.sin(theta)*np.sin(phi),np.cos(theta)]
        previous=np.vstack([[0.,0.,1.],direction[:-1]])
        dot=np.einsum('ij,ij->i',direction,previous)
        if min(dot)<=0:raise ValueError('turn')
        length=np.cumprod(dot*(1-1e-4))
        block=direction*length[:,None];qs.append(block);maxbottom.append(-block[-1,2])
    d=fraction*min(maxbottom)
    # Centroid-zero convex body with top1 and bottom-1/d requires d>=1/3.
    if d<=1/3:raise ValueError('centroid-support inequality')
    allq=[[0.,0.,1.]];parents=[]
    for block,dm in zip(qs,maxbottom):
        block=block*(d/dm)
        for mirror in (1.,-1.):
            v=block.copy();v[:,:2]*=mirror;start=len(allq)
            allq.extend(v.tolist())
            parents.extend([0]+list(range(start,start+depth-1)))
    q=np.asarray(allq);pa=np.asarray(parents)
    score=np.einsum('ij,ij->i',q[1:],q[pa]-q[1:])
    assert np.min(score)>0
    return q,dict(d=d,minimum_reference_radial_score=float(np.min(score)),parents=parents)

def evaluate(q):
    hull=ConvexHull(q)
    if max(hull.equations[:,3])>=-1e-10:raise ValueError('unbounded')
    v=np.linalg.solve(q[hull.simplices],np.ones((len(hull.simplices),3,1)))[:,:,0]
    vol,c,_=mass(v)
    return vol,c

def run():
    rows=[]
    bounds=[(-.65,.65),(-.65,.65),(-2.,2.),(-2.,2.),(.25,np.pi-.25),(.6,.9999)]
    for mode in (0,1):
        for depth in (6,10,14,20):
            best=None;calls=0
            def objective(x):
                nonlocal best,calls
                calls+=1
                try:
                    q,extra=generate(x,depth,mode);vol,c=evaluate(q)
                except (ValueError,QhullError,np.linalg.LinAlgError):return 100.
                value=-float(c[2])
                if best is None or value<best['loss']:
                    best=dict(x=x.tolist(),loss=value,volume=vol,centroid=c.tolist(),q=q.tolist(),**extra)
                return value
            opt=differential_evolution(objective,bounds,popsize=10,maxiter=60,tol=1e-8,atol=0,
               mutation=(.5,1.),recombination=.7,seed=113+depth+100*mode,polish=False,workers=1,updating='immediate')
            row=dict(mode=mode,depth=depth,calls=calls,optimizer_success=bool(opt.success),message=opt.message,best=best,numerical_only=True)
            if best is not None:
                try:
                    s=from_h(np.array(best['q']));row['own']=census(s);row['reference']=census(s,np.zeros(3))
                except (ValueError,QhullError,np.linalg.LinAlgError) as e:row['lattice_failure']=str(e)
            rows.append(row);(ROOT/'TWIST113.json').write_text(json.dumps(rows,indent=2)+'\n')
            print('mode depth',mode,depth,'calls',calls,'gz',None if best is None else best['centroid'][2],
                  'ownSU',None if 'own' not in row else [len(row['own']['S']),len(row['own']['U'])],flush=True)
    print('TWIST113_NUMERICAL_FINISHED',len(rows))
if __name__=='__main__':run()
```
### FILE metric113.py
```python
"""Actual-centred C2-preserving affine continuation of all eight twist scouts.
Numerical angular root-escape objective uses the current full true-edge graph.
No equilibrium count is accepted as exact by this scout.
"""
import json,sys
from pathlib import Path
import numpy as np
from scipy.optimize import differential_evolution,minimize
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'j109'))
from geometry109 import from_h,census,bars
ROOT=Path(__file__).resolve().parent

def metric(t):
    a,b,angle=t;co,si=np.cos(angle),np.sin(angle)
    R=np.array([[co,-si],[si,co]])
    A=R@np.diag(np.exp([a,b]))@R.T
    T=np.eye(3);T[:2,:2]=A
    return T

def angles(v,e):
    i,j=e.T;d=v[j]-v[i]
    ni=np.linalg.norm(v[i],axis=1);nj=np.linalg.norm(v[j],axis=1);nd=np.linalg.norm(d,axis=1)
    s1=np.einsum('ij,ij->i',v[i],d)/(ni*nd)
    s2=-np.einsum('ij,ij->i',v[j],d)/(nj*nd)
    score=np.full(len(v),-1.)
    np.maximum.at(score,i,s1);np.maximum.at(score,j,s2)
    return score

def run():
    rows=json.loads((ROOT/'TWIST113.json').read_text());out=[]
    for row in rows:
        q0=np.array(row['best']['q']);s=from_h(q0);g=s['centroid'];p=s['v']-g;q=q0/(1-q0@g)[:,None]
        up=int(np.argmin(p[:,2]));sp=0;pe=s['edges'];qe=s['qedges'];active=s['active'];nonP=np.array([i for i in range(len(p)) if i!=up]);nonQ=np.array([i for i in active if i!=sp])
        calls=0;best=None
        def objective(t):
            nonlocal calls,best
            calls+=1
            A=metric(t);P=p@A.T;Q=q@np.linalg.inv(A)
            a=angles(P,pe)[nonP];b=angles(Q,qe)[nonQ]
            z=np.r_[a,b];neg=np.maximum(1e-5-z,0)
            val=float(np.max(neg)+.1*np.mean(neg**2))
            if best is None or val<best['loss']:
                best=dict(t=t.tolist(),loss=val,minP=float(a.min()),minQ=float(b.min()),A=A.tolist())
            return val
        extent=np.ptp(p[:,:2],axis=0);guess=np.r_[np.log(2/extent),0]
        opt=differential_evolution(objective,[(-5.,1.),(-5.,1.),(-np.pi,np.pi)],popsize=16,maxiter=250,tol=1e-9,atol=1e-11,
          seed=313+row['depth']+100*row['mode'],polish=True,workers=1,updating='immediate',x0=guess)
        A=np.array(best['A']);qnew=q0@np.linalg.inv(A);ss=from_h(qnew);report=census(ss)
        record=dict(mode=row['mode'],depth=row['depth'],calls=calls,optimizer_success=bool(opt.success),best=best,own=report,q=qnew.tolist(),numerical_only=True)
        out.append(record);(ROOT/'METRIC113.json').write_text(json.dumps(out,indent=2)+'\n')
        print(row['mode'],row['depth'],'loss',best['loss'],'minPQ',best['minP'],best['minQ'],'own',len(report['S']),len(report['U']),'P',[x['depth'] for x in report['P']],'Q',[x['depth'] for x in report['Q']],flush=True)
    print('METRIC113_NUMERICAL_FINISHED',len(out))
if __name__=='__main__':run()
```
