# material-0eed9e717f62

AI research material · [Export notes](../catalog/coverage.md#text-records)

<!-- historical-status:start -->
> **Historical AI material.** The title and claims below reflect the AI’s assessment at the time. Claims of proof, certification or completion are not a current verification verdict.
>
> [C622](../C622/README.md) passes the supplied exact checks; C<500 remains open; Minimum’s C≥34 remains a working lower bound requiring a consolidated proof. See [verification status and source gaps](../catalog/coverage.md).
<!-- historical-status:end -->

---

# Complete numerical producer units: support deletion and protected polar curves

These are finite numerical research methods, not exact hull certificates. Every accepted exact body is separately reconstructed and audited in materials [internal-source-reference] (C288), [internal-source-reference] (C318 protected15), and their stated dependencies. The exact C330 source input is recovered by [internal-source-reference] plus [internal-source-reference]. This material supplies all3 complete source files needed to rerun the producing support/curve studies; no originating sandbox or encoded archive is required.

Environment used: CPython3.13.5, NumPy2.3.5, SciPy1.17.0, PyTorch2.10.0+cpu, OPENBLAS_NUM_THREADS=1, OMP_NUM_THREADS=1; no RNG in these methods. Save each FILE block with its terminal newline. Commands with every non-default search parameter made explicit:

`python SUPPORT_BEAM.py C330/RAW.json BEAM --width 6 --depth 40 --ceiling 310`

The finite run attempted20822 distinct subsets and selected level39 attempt20479 as C288. Exact retained indices and all recovery-output hashes are in [internal-source-reference]. This is not an exhaustive search of the support family or of all subsets.

`python PROTECTED_ENVELOPE_SCOUT.py C288/RAW.json CHAINS`

This tests exactly30,32,34,36 long-arc links. The32-link path has reference S/U1/1 but own S/U4/12; it does not solve the problem. The fixed root-owner/stable/path-only envelope tested by this scout was unbounded, not a bounded moment-exclusion certificate.

`python PROTECTED_SHORT_PATH.py CHAINS/CHAIN32.json PATHS --nmin 13 --nmax 28 --steps 4000 --margin 0.00001 --protection 0.0001`

A COMPLETE corrected48-case run was executed, ending PROTECTED_PATH_FINITE_SCAN_END48. An earlier attempt had a duplicate-key Python packaging bug after the six13/14 cases; that attempt is not misreported as complete. The corrected source below was rerun for all48 cases. The15-link winding0 initial curve is already strictly feasible without optimization (one objective call), with normalized minimum arrow about0.0005380656 and maximum root contact about0.9324203. Winding1 first succeeded at25 links in this finite scan. No protected minimum is proved: unsuccessful13/14 cases are finite local failures. The rationalized15-link proof, with strict exact bounds at both the parent own centroid and the separate rational reference point, is in [internal-source-reference].

Important correction: SUPPORT_BEAM.hullstate uses F=len(input Y), which is valid for deleting originally extreme polar vertices but NOT for later arbitrary insertions. Old input vertices can become interior after insertion. Thus curve output VEF is only a scout label and can overcount F/E. For any current geometry pass Y[ConvexHull(Y).vertices] to hullstate before using its Euler count, and exactify all accepted counts. This does not change the historical producer source below. For exact C318 the84 input inequalities yield67 actual maximal facets and159 true edges. No floating failure or small objective proves an exclusion.

Numerical report byte identity depends on filesystem argument strings and elapsed-time fields and is not promised across output paths. The complete literal rational endpoints and their deterministic audit hashes, not such metadata, define the retained exact objects.

<!-- FILE SUPPORT_BEAM.py -->
```python
"""Finite whole-support deletion at the recomputed uniformly filled centroid.
Numerical scouting only. Surviving original supports are extreme in the polar;
V/E counts rely on deduplication and need a complete exact audit before acceptance.
"""
import os
os.environ['OPENBLAS_NUM_THREADS']='1';os.environ['OMP_NUM_THREADS']='1'
import sys,json,time,hashlib,argparse
from pathlib import Path
import numpy as np
from scipy.spatial import ConvexHull

def hullstate(Y):
    q=ConvexHull(Y)
    if q.equations[:,3].max()>=-1e-9:raise ValueError('unbounded physical body')
    P=-q.equations[:,:3]/q.equations[:,3,None]
    _,ids=np.unique(np.round(P,9),axis=0,return_index=True);P=P[ids]
    h=ConvexHull(P);T=h.simplices.copy()
    flip=np.einsum('ij,ij->i',np.cross(P[T[:,1]]-P[T[:,0]],P[T[:,2]]-P[T[:,0]]),h.equations[:,:3])<0
    T[flip]=T[flip][:,[0,2,1]]
    base=P.mean(0);t=P[T]-base;v=np.einsum('ij,ij->i',t[:,0],np.cross(t[:,1],t[:,2]))
    g=base+(v[:,None]*t.sum(1)).sum(0)/(4*v.sum());X=P-g
    Z=Y/(1-Y@g)[:,None]
    def esc(X):
        r2=(X*X).sum(1);D=X@X.T-r2[:,None];np.fill_diagonal(D,-np.inf)
        return D.max(1)/r2,int(r2.argmax())
    pe,pr=esc(X);de,dr=esc(Z)
    r=dict(VEF=[len(P),len(P)+len(Y)-2,len(Y)],SU=[int((de<0).sum()),int((pe<0).sum())],g=g.tolist(),V=float(v.sum()/6),phys_min=float(np.min(np.delete(pe,pr))),polar_min=float(np.min(np.delete(de,dr))),stable_input=np.flatnonzero(de<0).tolist(),unstable_vertices=np.flatnonzero(pe<0).tolist())
    return r,P

def run(a):
    inp=Path(a.input);raw=json.loads(inp.read_text());H=np.asarray(raw['H'],float);Y=H[:,:3]/H[:,3,None]
    out=Path(a.output);out.mkdir(exist_ok=True);start=time.time();seen=set();n=0;hist=[]
    r,P=hullstate(Y);beams=[(tuple(range(len(Y))),r)];best=(sum(r['SU']),r['VEF'][1],max(-r['phys_min'],-r['polar_min']))
    def key(r):return (sum(r['SU']),max(r['SU']),r['VEF'][1],max(-r['phys_min'],-r['polar_min']))
    for level in range(a.depth):
        children=[]
        for ids,rr in beams:
            for j in range(len(ids)):
                new=ids[:j]+ids[j+1:]
                if new in seen:continue
                seen.add(new);n+=1
                try:r,P=hullstate(Y[list(new)])
                except (ValueError,RuntimeError):continue
                if r['VEF'][1]>a.ceiling:continue
                k=key(r);children.append((k,new,r))
                score=(sum(r['SU']),r['VEF'][1],max(-r['phys_min'],-r['polar_min']))
                if score<best or r['SU']==[1,1]:
                    best=min(best,score);name=f'L{level:02d}_N{n:06d}_S{r["SU"][0]}U{r["SU"][1]}E{r["VEF"][1]}'
                    (out/(name+'.json')).write_text(json.dumps(dict(original_input_sha256=hashlib.sha256(inp.read_bytes()).hexdigest(),retained_supports=new,H=[raw['H'][i] for i in new],numerical_only=True,summary=r),sort_keys=True,separators=(',',':')))
                    print('BEST',name,r,flush=True)
                if r['SU']==[1,1]:break
            else:continue
            break
        children.sort(key=lambda t:t[0]);beams=[(ids,r) for k,ids,r in children[:a.width]]
        hist.append(dict(level=level,attempts=n,top=[dict(ids=ids,summary=r) for ids,r in beams]));(out/'REPORT.json').write_text(json.dumps(dict(arguments=vars(a),attempts=n,history=hist,elapsed=time.time()-start),sort_keys=True,separators=(',',':')))
        print('LEVEL',level,n,[b[1]['SU'] for b in beams],flush=True)
        if not beams or any(r['SU']==[1,1] for _,r in beams):break
    print('SUPPORT_BEAM_FINITE_END',n,best,flush=True)
if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('input');p.add_argument('output');p.add_argument('--width',type=int,default=5);p.add_argument('--depth',type=int,default=30);p.add_argument('--ceiling',type=int,default=310);run(p.parse_args())
```

<!-- FILE PROTECTED_ENVELOPE_SCOUT.py -->
```python
"""Finite long-arc support insertion and protected-root mass-envelope diagnostics.
All generated outputs are numerical candidates only, not exact homogeneous solutions.
"""
import os
os.environ['OPENBLAS_NUM_THREADS']='1';os.environ['OMP_NUM_THREADS']='1'
import json,sys,argparse
from pathlib import Path
import numpy as np
from scipy.spatial import ConvexHull
from SUPPORT_BEAM import hullstate

def counts_at_zero(P,Y):
    def nmax(X):
        D=X@X.T-(X*X).sum(1)[:,None];np.fill_diagonal(D,-np.inf);return np.flatnonzero(D.max(1)<-1e-12).tolist()
    return [nmax(Y),nmax(P)]

def main(a):
    raw=json.loads(Path(a.input).read_text());H=np.array(raw['H'],float);Y=H[:,:3]/H[:,3,None];r,P=hullstate(Y);g=np.array(r['g']);P-=g;Y=Y/(1-Y@g)[:,None]
    rr=np.sum(P*P,1);pr=int(rr.argmax());root=P[pr];s=counts_at_zero(P,Y)[0];dr=max(s,key=lambda k:np.dot(Y[k],Y[k]));bad=[k for k in s if k!=dr];assert len(bad)==1;bad=bad[0]
    u=Y[bad];z=Y[dr];ru=np.linalg.norm(u);rz=np.linalg.norm(z);e=u/ru;f=z/rz;angle=np.arccos(np.clip(e@f,-1,1));axis=f-(e@f)*e;axis/=np.linalg.norm(axis);phi=angle-2*np.pi
    out=Path(a.output);out.mkdir(exist_ok=True)
    owners=np.flatnonzero(abs(Y@root-1)<1e-8);print('ANGLE/R',angle,rz/ru,'ROOT',pr,'owners',owners.tolist(),flush=True)
    for n in (30,32,34,36):
        t=np.arange(1,n)/n;path=ru*(rz/ru)**t[:,None] if False else np.asarray([ru*(rz/ru)**v*(np.cos(phi*v)*e+np.sin(phi*v)*axis) for v in t]);YY=np.vstack((Y,path));seq=np.vstack((u,path,z));arrows=np.einsum('ij,ij->i',seq[:-1],np.diff(seq,axis=0));protect=path@root
        r,Q=hullstate(YY);refs=counts_at_zero(Q,YY)
        fixed=list(set(owners.tolist()+[dr]))+list(range(len(Y),len(YY)))
        try:env,QP=hullstate(YY[fixed]);envout=dict(summary=env,points=QP.tolist(),g=env['g'])
        except Exception as ex:envout=dict(error=type(ex).__name__+': '+str(ex))
        cfg=dict(n=n,polar_points=YY.tolist(),parent_g=g.tolist(),parent_support_count=len(Y),root=root.tolist(),owners=owners.tolist(),stable_root=dr,bad_stable=bad,reference_SU=[len(v) for v in refs],reference_features=refs,summary=r,points=Q.tolist(),grid=1,numerical_only=True,min_arrow=float(arrows.min()),max_root_ratio=float(protect.max()),envelope=envout,fixed_ids=fixed)
        (out/f'CHAIN{n}.json').write_text(json.dumps(cfg,sort_keys=True,separators=(',',':')))
        print(n,'arrows',arrows.min(),'protection',protect.max(),'ref',cfg['reference_SU'],'own',r['SU'],'VEF',r['VEF'],'g',r['g'],'env',envout.get('g',envout.get('error')),flush=True)
if __name__=='__main__':
 p=argparse.ArgumentParser();p.add_argument('input');p.add_argument('output');main(p.parse_args())
```

<!-- FILE PROTECTED_SHORT_PATH.py -->
```python
"""Protected positive polar paths using radius-dependent spherical cap constraints.
Fixed geometric radii, free spherical latitudes/azimuths, positive-arrow penalty.
Numerical feasibility only. Does not prove minimality or homogeneous mechanics.
"""
import os
os.environ['OPENBLAS_NUM_THREADS']='1';os.environ['OMP_NUM_THREADS']='1'
import json,argparse,sys,time,hashlib
from pathlib import Path
import numpy as np
from scipy.optimize import minimize
import torch
torch.set_num_threads(1);torch.set_default_dtype(torch.float64)
from SUPPORT_BEAM import hullstate
from PROTECTED_ENVELOPE_SCOUT import counts_at_zero

def run(a):
    cfg=json.loads(Path(a.input).read_text());Y=np.array(cfg['polar_points'])[:cfg['parent_support_count']];root=np.array(cfg['root']);u=Y[cfg['bad_stable']];z=Y[cfg['stable_root']]
    r0=np.linalg.norm(u);r1=np.linalg.norm(z);k=root/np.linalg.norm(root);e=u-(u@k)*k;e/=np.linalg.norm(e);f=np.cross(k,e);theta0=np.arccos(u@k/r0);theta1=np.arccos(z@k/r1);az0=np.arctan2(u@f,u@e);az1=np.arctan2(z@f,z@e)
    out=Path(a.output);out.mkdir(exist_ok=True);U=torch.tensor(u);Z=torch.tensor(z);E=torch.tensor(e);F=torch.tensor(f);K=torch.tensor(k);R=torch.tensor(root)
    results=[]
    for n in range(a.nmin,a.nmax+1):
      for winding in (0,-1,1):
        radii=r0*(r1/r0)**(np.arange(1,n)/n);theta_min=np.arccos(np.clip((1-a.protection)/(radii*np.linalg.norm(root)),-1,1));theta=np.maximum(np.linspace(theta0,theta1,n+1)[1:-1],theta_min+.02);az=np.linspace(az0,az1+2*np.pi*winding,n+1)[1:-1];r=torch.tensor(radii)
        def points(p):
            angles=p.reshape(2,n-1);th,ph=angles[0],angles[1]
            return r[:,None]*(torch.cos(th)[:,None]*K+torch.sin(th)[:,None]*(torch.cos(ph)[:,None]*E+torch.sin(ph)[:,None]*F))
        def loss(p):
            pp=torch.tensor(p,requires_grad=True);Q=points(pp);seq=torch.cat((U[None,:],Q,Z[None,:]));ar=(seq[:-1]*(seq[1:]-seq[:-1])).sum(1)/seq[:-1].square().sum(1);obj=torch.relu(a.margin-ar).square().sum();obj.backward();return obj.item(),pp.grad.numpy()
        x=np.concatenate((theta,az));bounds=list(zip(theta_min,np.full(n-1,np.pi-1e-6)))+[(az0-4*np.pi,az0+4*np.pi)]*(n-1)
        res=minimize(loss,x,jac=True,method='L-BFGS-B',bounds=bounds,options=dict(maxiter=a.steps,ftol=1e-24,gtol=1e-13,maxls=40,maxcor=30))
        Q=points(torch.tensor(res.x)).detach().numpy();seq=np.vstack((u,Q,z));ar=np.einsum('ij,ij->i',seq[:-1],np.diff(seq,axis=0))/(seq[:-1]**2).sum(1);pro=Q@root
        rrr=dict(n=n,winding=winding,loss=float(res.fun),min_arrow=float(ar.min()),max_root=float(pro.max()),success=bool(ar.min()>0 and pro.max()<1),calls=int(res.nfev),status=int(res.status))
        if rrr['success']:
            YY=np.vstack((Y,Q));st,P=hullstate(YY);refs=counts_at_zero(P,YY);rrr.update(summary=st,reference_SU=[len(t) for t in refs]);name=f'PATH_N{n}_W{winding}.json';data=dict(cfg);data.update(polar_points=YY.tolist(),n=n,points=P.tolist(),reference_SU=rrr['reference_SU'],summary=st,curve=dict(radii=radii.tolist(),axis=k.tolist(),e=e.tolist(),f=f.tolist(),angles=res.x.tolist(),theta_min=theta_min.tolist(),u=u.tolist(),z=z.tolist(),arguments=vars(a)),fixed_ids=list(set(cfg['owners']+[cfg['stable_root']])),grid=1,numerical_only=True,diagnostics=rrr);(out/name).write_text(json.dumps(data,sort_keys=True,separators=(',',':')))
        results.append(rrr);print(rrr,flush=True)
      (out/'SCAN_REPORT.json').write_text(json.dumps(dict(arguments=vars(a),input_sha256=hashlib.sha256(Path(a.input).read_bytes()).hexdigest(),results=results),sort_keys=True,separators=(',',':')))
    print('PROTECTED_PATH_FINITE_SCAN_END',len(results),flush=True)
if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('input');p.add_argument('output');p.add_argument('--nmin',type=int,default=13);p.add_argument('--nmax',type=int,default=28);p.add_argument('--steps',type=int,default=4000);p.add_argument('--margin',type=float,default=1e-5);p.add_argument('--protection',type=float,default=1e-4);run(p.parse_args())
```
