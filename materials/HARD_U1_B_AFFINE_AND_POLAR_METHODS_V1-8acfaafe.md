# material-8acfaafeac88

Historical AI scientific source/proof material. Statements retain their original scope; this is not an independently reviewed theorem.

Public derivative: internal-record-identifiers-replaced.

---

# Actual bounded affine and polar-centering probes of exact parents

Complete executed reusable methods and observed non-successes, not exclusion theorems and not new accepted110 bodies. Inputs: literal HARD_U1_B_G5 (29 hull vertices, own211,C162) from recovery part2 [internal-source-reference], and FREE_LIVE_FULLBAR_G8 (30 hull vertices, own817,C168) from [internal-source-reference]. Dependency margin_search.py5245B SHAd5be4ca00fb7f67a87de14296c5e2eaf1dbec2394ffda5bcb4fd26a524d6e9e6 is fully preserved in recovery part1 [internal-source-reference]. Select all three exact dependencies, not just filenames. No independent input coordinates or helpers are missing from this source set.

Environment Python3.13.5,NumPy2.3.5,SciPy1.17.0,torch2.10.0+cpu,OPENBLAS_NUM_THREADS=1,OMP_NUM_THREADS=1,torchthreads1/defaultfloat64. Sources below with one trailing LF:
metric_orbit.py2584B SHA2c815b1d71008e08c3da1afe29c54c47606b09651bcd80bcb1fe0209492febbb
santalo_probe.py2410B SHAc26762cc9182ab9d31183a50a10088e3b724a228f864e02e8689f70d73d3247e

## Commands and actual observations
`OPENBLAS_NUM_THREADS=1 python metric_orbit.py HARD_U1_B_G5.json --iters 800 --out AFFINE_HARD_B`
Seed173,popsize20,eps1e-4,width2,tol1e-9,polishtrue,immediateupdating. Actual JSON says nfev53106, Optimization terminated successfully; final loss.00030534141071152137, floatS3/U3, minP-.01226959451695988,minQ-8.555798368132385e-5. Complete parameter checkpoint [-0.4377140667458037,1.2413492645280324,1.9999999999737414,1.2028077537304789,1.9999999998880291]. Final T=[[.6455103293411347,1.9999999999737414,1.2028077537304789],[0,3.4602791483461215,1.9999999998880291],[0,0,.44769852973456714]]. This is a bounded5-dimensional positive-definite metric slice, not all affine/projective geometry. Two offdiagonal parameters hit the chosen bound. Neither lack of global optimizer guarantee nor near singular/projective boundaries is resolved. Observe, do not misreport this as a33→110 result.

Reevaluate that precise parameter checkpoint by importing setup,evaluate,matrix from metric_orbit, loading the exact G5 input and passing eps1e-4. The diagnostic loss, counts and matrix above are expected floating markers, subject to small platform changes. AFFINE_HARD_B.json38736B SHA02740d230bdc705866fafb2c66c8b3579ca1dd0954d860e5bdcfea74dcda8fc4 records the original full history and elapsedtime; it is supplementary, not needed to reconstruct the method or checkpoint. Do not expect byte-identical elapsedtime output on rerun.

`OPENBLAS_NUM_THREADS=1 python santalo_probe.py HARD_U1_B_G5.json`
Observed after5 Newton evaluations: z=[.06555472632500707,.0738314073267714,.18876132882234203], polarvolume11.443981839009988, centroid[-1.449142148566442e-16,-1.7432149276688372e-16,-4.016973528976016e-17]. Primal reference counts S2/U11, implying floating centered polar S11/U2, not110. Referencefaceids[5,44],Uids[1,3,4,6,10,13,15,19,23,25,28] in floating hull ordering; nearest absolute Sside.00037444247670696666 and Uescape.003608722961821899. HARD_U1_B_G5_SANTALO.json1905B SHA619209a2ade48670e2681b65a87d88689949e629ad8d5be5cbbf93599143cdf5.

`OPENBLAS_NUM_THREADS=1 python santalo_probe.py FREE_LIVE_FULLBAR_G8.json`
Observed after5 evaluations: z=[.14735900491354595,.036253022621841866,.20577808651414425], polarvolume7.404364523472228, centroid[-3.529698697597795e-17,1.874160577833341e-17,-6.516642227338432e-17]. Primal reference S7/U19 implies floating centered polar S19/U7, not110. NearestSside.00021324246578196306,nearestUescape.0007198388275346145. FREE_LIVE_FULLBAR_G8_SANTALO.json2026B SHA2a97c68a985fdc9be8de3383b8303a35402ba60554e07a7e5431a39e5ba7494e.

Floating duality counts here refer to maximal physical faces via the original primal graph, not triangles artificially used to integrate polar volume. No exact S/U/H/closed-weak certificate or newly accepted rational polar control is claimed. No global impossibility follows for Santalo-centered polars, affine or projective orbits. These observations supersede any compacted synopsis giving different numbers for the same filenames; the exact parent hashes and literal output checkpoints identify the performed experiments.

## Derivations that motivate the probes
At owncentroidc, linear image(P−c)T has owncentroid0; polar transforms by T^−T. Thus affine shape variables can be represented by five det1 uppertriangular entries without optimizing a fictitious independent centre. For Q(z)=(P−z)^polar in dimension3, differentiating the radial integral gives grad_z logVolQ=4c_Q and Hessian=20E_Q[xx^T]−16c_Qc_Q^T. Uniform tetrahedron(0,a,b,c) has mean(a+b+c)/4 and secondmoment[aa^T+bb^T+cc^T+(a+b+c)(a+b+c)^T]/20. Newton is a numerical solver only; finite stopping tolerance is not an exact proof that the centre is the Santalo point.

## metric_orbit.py
```python
"""Bounded numerical exploration of a centered affine metric orbit.
No global exclusion is inferred. The volume centroid is affine-equivariant;
primal and polar escape inequalities use reciprocal metrics.
"""
from margin_search import faces,diagnose
import numpy as np,json,sys,time
from pathlib import Path
from scipy.optimize import minimize,differential_evolution

def setup(x):
    h,tr=faces(x);x=x[h.vertices];h,tr=faces(x)
    c=np.array(diagnose(x)['centroid']);x=x-c
    n=h.equations[:,:3];heights=-(h.equations[:,3]+n@c)
    q=n/heights[:,None]
    return x,q

def matrix(a):
    # det(T)=1 and every positive-diagonal upper-triangular matrix is covered.
    return np.array([[np.exp(a[0]),a[2],a[3]],[0,np.exp(a[1]),a[4]],[0,0,np.exp(-a[0]-a[1])]])

def scores(z):
    dot=z@z.T;r=np.diag(dot);d2=np.maximum(r[:,None]+r[None,:]-2*dot,1e-28)
    s=(dot-r[:,None])/np.sqrt(d2*r[:,None]);np.fill_diagonal(s,-1e6)
    u=s.max(1);u[np.argmax(r)]=1.
    return u

def evaluate(a,x,q,eps):
    T=matrix(a);U=scores(x@T);S=scores(np.linalg.solve(T,q.T).T)
    loss=np.maximum(eps-U,0)@np.maximum(eps-U,0)+np.maximum(eps-S,0)@np.maximum(eps-S,0)
    return loss,U,S

if __name__=='__main__':
    import argparse
    p=argparse.ArgumentParser();p.add_argument('input');p.add_argument('--seed',type=int,default=173);p.add_argument('--iters',type=int,default=600);p.add_argument('--eps',type=float,default=1e-4);p.add_argument('--width',type=float,default=2.);p.add_argument('--out',default='METRIC');a=p.parse_args()
    raw=json.loads(Path(a.input).read_text());source=np.array(raw['points'])/raw['denominator'];x,q=setup(source)
    fun=lambda v:evaluate(v,x,q,a.eps)[0]
    tic=time.time();records=[]
    def cb(v,conv):
        loss,u,s=evaluate(v,x,q,a.eps);records.append([len(records),float(loss),int((s<0).sum()+1),int((u<0).sum()+1)])
    result=differential_evolution(fun,[(-a.width,a.width)]*5,popsize=20,maxiter=a.iters,seed=a.seed,tol=1e-9,polish=True,callback=cb,updating='immediate')
    T=matrix(result.x);y=x@T;np.save(a.out+'.npy',y)
    loss,u,s=evaluate(result.x,x,q,a.eps)
    out=dict(input=a.input,seed=a.seed,maxiter=a.iters,eps=a.eps,width=a.width,params=result.x.tolist(),T=T.tolist(),loss=float(loss),S=int((s<0).sum()+1),U=int((u<0).sum()+1),min_P=float(u.min()),min_Q=float(s.min()),message=str(result.message),nfev=result.nfev,seconds=time.time()-tic,records=records,physical=diagnose(y))
    Path(a.out+'.json').write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps({k:v for k,v in out.items() if k not in ['records','physical']}),flush=True)
```

## santalo_probe.py
```python
"""Newton search for a Santalo center; exploratory floating arithmetic.
For Q(z)=(P-z)^polar, grad log Vol(Q)=4 centroid(Q), and Hessian is
20 E_Q[xx^T]-16 centroid(Q)centroid(Q)^T in dimension three.
"""
import json,numpy as np,sys
from pathlib import Path
from margin_search import faces,diagnose

def moments(q):
    hull,tr=faces(q);p=q[tr]
    vs=np.einsum('ij,ij->i',p[:,0],np.cross(p[:,1],p[:,2]))/6
    assert vs.min()>-1e-10
    v=vs.sum();s=p.sum(1)
    c=(vs[:,None]*s/4).sum(0)/v
    e=(vs[:,None,None]*(np.einsum('tki,tkj->tij',p,p)+np.einsum('ti,tj->tij',s,s))/20).sum(0)/v
    return v,c,e

def reference_counts(p,tr,z):
    f=p[tr];e=np.roll(f,-1,axis=1)-f
    n=np.cross(e[:,0],-e[:,2]);n=n/np.linalg.norm(n,axis=1)[:,None]
    s=np.einsum('tki,tki->tk',z-f,np.cross(n[:,None,:],e))/np.linalg.norm(e,axis=2)
    outside=s.min(1)
    d=p[None,:,:]-p[:,None,:];ll=np.linalg.norm(d,axis=2)
    u=np.einsum('ik,ijk->ij',p-z,d)/(ll+np.eye(len(p)));np.fill_diagonal(u,-1e10);escape=u.max(1)
    return dict(S=int((outside>0).sum()),U=int((escape<0).sum()),S_ids=np.where(outside>0)[0].tolist(),U_ids=np.where(escape<0)[0].tolist(),nearest_S=float(np.min(abs(outside))),nearest_U=float(np.min(abs(escape))))

def solve(p):
    hull,tr=faces(p);p=p[hull.vertices];hull,tr=faces(p)
    n=hull.equations[:,:3];h=-hull.equations[:,3]
    z=np.array(diagnose(p)['centroid']);hist=[]
    for k in range(50):
        q=n/(h-n@z)[:,None];v,c,E=moments(q)
        hist.append([k,z.tolist(),float(v),c.tolist()])
        if np.linalg.norm(c)<1e-13:break
        H=20*E-16*np.outer(c,c);step=np.linalg.solve(H,-4*c)
        alpha=1.
        for j in range(60):
            zn=z+alpha*step;hs=h-n@zn
            if hs.min()>0:
                vn,_,_=moments(n/hs[:,None])
                if vn<v*(1+1e-14):break
            alpha/=2
        z=zn
    q=n/(h-n@z)[:,None];v,c,E=moments(q)
    ref=reference_counts(p,tr,z)
    return q,dict(z=z.tolist(),polar_volume=float(v),polar_centroid=c.tolist(),reference_P=ref,expected_polar_S=ref['U'],expected_polar_U=ref['S'],history=hist)

if __name__=='__main__':
    raw=json.loads(Path(sys.argv[1]).read_text());p=np.array(raw['points'])/raw['denominator'];q,out=solve(p)
    stem=Path(sys.argv[1]).stem+'_SANTALO';np.save(stem+'.npy',q);Path(stem+'.json').write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps({k:v for k,v in out.items() if k!='history'}))
```
