# material-20698554a0d6

Historical AI scientific source/proof material. Statements retain their original scope; this is not an independently reviewed theorem.

Public derivative: internal-record-identifiers-replaced.

---

# J99 complete numerical joint-cover and pruning producers

These are complete numerical research units, NOT exact strict/weak auditors. Their common exact input KH93_C434_R82_G6.txt is preserved literally, with its complete exact successor audit, in J99_EXACT_PRUNED_C464.md, material [internal-source-reference]. Extract that input beside these three modules. Its1888-byte SHA-256 is9765712b5ffaa464ed4d677974256294c6d867b77fe77b930d166853f66a92a7. The selected immutable parent is figure-0581. These methods use only the literal R82 input, not the C622 package or an unavailable old workspace.

Observed dependency versions: CPython3.13.5, NumPy2.3.5, SciPy1.17.0. Numerical linear algebra is float64. The controlled invocation environment used OPENBLAS_NUM_THREADS=1 and OMP_NUM_THREADS=1. No pseudorandom seed enters these programs; spherical samples are deterministic Fibonacci directions. Floating optimizer trajectories and Qhull ordering need not be portable. Exact support-triple identities, not a promise of optimizer determinism, define the preserved C464 body.

## Scientific scope and completed runs

The joint producer moves ALL four original covering points AND the selected compensation points simultaneously, retaining the old R82 body. Each point retains one assigned old one-step chord witness; the primary witnesses selected here are local indices15,20,148,6, not the alternative valid J98 witness policy. Actual filled-hull volume and centroid are recomputed, including overlap correctly. The objective is half the squared own-centroid displacement from the old centroid. The initial sampled cover constraints are strengthened by complete new-facet hole directions for three outer iterations, but the final numerical hole counts remain positive. These failures are not exclusions of the family.

Completed case0: no additional controllers, elder ceiling.6339, maxiter120, three outer passes. Final V139/E250/F113, reference S9/U1, actual S18/U28, centroid displacement norm.019161958011424833, six old-component holes. Completed case2: four additional controllers, ceiling.6339, maxiter250, three passes. Final V134/E300/F168, reference S8/U1, actual S8/U36, displacement.00831644384301899, five holes. Completed case6 differs only by ceiling.8 and produced exactly the same coordinates and traces as case2: it is a policy comparison, not a distinct body. All are numerical failure endpoints; no exact weak or saddle census was run on them. Their complete compact frozen point arrays, witness assignments, settings and traces are preserved separately in J99_NUMERICAL_FROZEN_ENDPOINTS.md.

Case1, two additional controllers with ceiling.6339 and maxiter160, completed only its first outer pass:160 iterations/244 calls, iteration-limit status, displacement.013079510764542224, constraint minimum -1.1671991244910362e-6, seven holes. The next pass encountered a numerical maximal-face grouping assertion before saving an endpoint. No coordinates for that incomplete pass are claimed preserved. This motivated using oriented ConvexHull simplices directly inside the mass objective and writing an outer checkpoint before the diagnostic hole calculation. Cases other than0,2,6 were not completed.

The complete current joint99.py below contains that repair. Case0 and the incomplete case1 used the same objective mathematics but obtained oriented simplices via geom99.hull instead of the direct ConvexHull code. To reproduce that earlier implementation, replace only Problem.objective with the complete method below; all its helpers are supplied in this material. This earlier implementation did not write the newly added per-outer checkpoint. Saved case0 coordinates, rather than a bitwise optimizer replay, remain the exact frozen numerical nomination.

```python
    def objective(self,x):
        A=x.reshape(-1,3);v=np.r_[self.p,A];b=hull(v)
        V,g,J=moment_and_jac(v,b['tri'],len(self.p))
        self.calls+=1;return .5*(g@g),g@J
```

The original producer's analytic actual-centroid Jacobian was compared with finite differences: maximum absolute difference5.013e-11 and relative difference2.871e-10 in that specified check. This is not a proof of global differentiability through fan changes.

The pruning producer removes old exact vertices without moving retained vertices. Each nomination recomputes actual own mass, S/U and all numerically resolved P/Q. Selection is lexicographic in true numerically grouped E, sole Q depth, then negative minimum outgoing clearance. The25 completed deletions in geom99's original vertex ordering are exactly:
[44,19,18,36,81,92,127,98,76,24,77,146,126,115,152,104,85,128,86,75,55,133,124,39,142].
The final135-vertex body underwent the separate complete rational audit in [internal-source-reference] and is exact own211/weak000, C464. Intermediate prefixes were numerical nominations only. The next complete single-deletion pass found zero eligible moves and zero grouping errors under this specific numerical filter. This is a greedy-policy fixed point, not an exclusion of paired deletions, changed incidence, other retained subsets, or finite mass-balanced deformations.

## Reconstruction commands

Extract each `## FILE` fence below with its literal filename, and obtain the exact H input from the exact C464 material. Then:

```sh
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python geom99.py
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python joint99.py --case 2 --maxiter 250
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python joint99.py --case 6 --maxiter 250
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python prune99.py --rounds 3
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python prune99.py --rounds 6 --resume J99_PRUNE_CURRENT.json
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python prune99.py --rounds 6 --resume J99_PRUNE_CURRENT.json
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python prune99.py --rounds 8 --resume J99_PRUNE_CURRENT.json
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python prune99.py --rounds 8 --resume J99_PRUNE_CURRENT.json
```

Case0 invocation used the earlier objective replacement above and `--case 0 --maxiter 120`. Numerical output markers are `RESULT 0 E 250 ref 9 1 own 18 28`, `RESULT 2 E 300 ref 8 1 own 8 36`, and `RESULT 6 E 300 ref 8 1 own 8 36`, followed by the stated displacement. Pruning concluded `J99_PRUNE_SCOPE_FINISHED_NOT_EXACT 25 135`. These markers describe observed computations; the exact C464 verification command and rational outputs are in the exact material and do not depend on the optimizer.

Source identities: geom99.py4084B SHA4f66e6f40266c4bc92ed6e51751773297ab588f1b2ea2ee26d5bf91a345ea17c; joint99.py6634B SHA06e36162e2c7799b61d723c501409ca313b817fcd343c529eec6d373c3c50391; prune99.py3920B SHAd8b1af23d8cf2087f36d61b46b04ebd05572d1a372f59261dfeb51875baba83d. Each FILE fence ends with one newline.

## FILE geom99.py
```python
"""J99 numerical geometry. NOT an exact strict/weak equilibrium auditor.
Finite hulls and their homogeneous moments are rebuilt at every evaluation.
Plane grouping 2e-9; root threshold 1e-10; radial bar floor is explicit.
"""
from pathlib import Path
import hashlib,json
import numpy as np
from scipy.spatial import ConvexHull,HalfspaceIntersection

def mass(v,t):
    a,b,c=np.moveaxis(v[t],1,0)
    d=np.einsum('ij,ij->i',a,np.cross(b,c));W=d.sum()
    assert W>0
    return W/6,(d[:,None]*(a+b+c)).sum(0)/(4*W)

def hull(v):
    v=np.asarray(v,float);h=ConvexHull(v);t=h.simplices.copy()
    ar=np.cross(v[t[:,1]]-v[t[:,0]],v[t[:,2]]-v[t[:,0]])
    flip=np.einsum('ij,ij->i',ar,h.equations[:,:3])<0
    t[flip,1],t[flip,2]=t[flip,2].copy(),t[flip,1].copy()
    equations=[];groups=[];which=[]
    for k,eq in enumerate(h.equations):
        ii=next((i for i,e in enumerate(equations)if np.max(abs(eq-e))<2e-9),None)
        if ii is None:ii=len(equations);equations.append(eq);groups.append([])
        groups[ii].append(k);which.append(ii)
    faces=[];ef={};rep=[]
    for i,(eq,ks) in enumerate(zip(equations,groups)):
        ids=np.unique(t[ks].ravel());c=v[ids].mean(0)
        a=v[ids[0]]-c;a/=np.linalg.norm(a);b=np.cross(eq[:3],a)
        pp=v[ids]-c;ids=ids[np.argsort(np.arctan2(pp@b,pp@a))].tolist()
        faces.append(ids);rep.append(t[ks[0]])
        for j,x in enumerate(ids):ef.setdefault(tuple(sorted((x,ids[(j+1)%len(ids)]))),[]).append(i)
    assert all(len(fs)==2 for fs in ef.values())
    vol,g=mass(v,t)
    e=np.array(sorted(ef),int);qe=np.array([ef[tuple(ee)]for ee in e],int)
    return dict(v=v,tri=t,faces=faces,edges=e,qe=qe,equations=np.array(equations),rep=np.array(rep),
                extreme=np.unique(e.ravel()),volume=vol,g=g)

def radial(p,e,floor=1e-13):
    r=np.einsum('ij,ij->i',p,p);d=p[e[:,1]]-p[e[:,0]];dd=np.einsum('ij,ij->i',d,d)
    tt=np.clip(-np.einsum('ij,ij->i',p[e[:,0]],d)/dd,0,1)
    foot=p[e[:,0]]+tt[:,None]*d
    z=np.minimum(np.einsum('ij,ij->i',foot,foot),np.minimum(r[e[:,0]],r[e[:,1]]))
    events=[(r[i],0,i)for i in range(len(p))]+[(z[k],1,k)for k in range(len(e))]
    events.sort(key=lambda x:(-x[0],x[1],x[2]));par=np.arange(len(p));root=par.copy();out=[]
    def find(i):
        while par[i]!=i:par[i]=par[par[i]];i=par[i]
        return i
    for val,typ,k in events:
        if not typ:continue
        a,b=map(find,e[k]);
        if a==b:continue
        if r[root[a]]<r[root[b]]:a,b=b,a
        dep=max(0.,1-float(val/r[root[b]]))
        if dep>floor:out.append(dict(root=int(root[b]),edge=e[k].tolist(),birth2=float(r[root[b]]),death2=float(val),depth=dep))
        par[b]=a
    return sorted(out,key=lambda x:-x['depth'])

def summary(b,c=None):
    g=b['g'] if c is None else np.asarray(c);p=b['v']-g
    eq=b['equations'];off=-eq[:,3]-eq[:,:3]@g
    assert min(off)>0
    q=eq[:,:3]/off[:,None]
    def roots(x,e):
        o=np.full(len(x),-np.inf)
        for i,j in e:
            d=x[j]-x[i];o[i]=max(o[i],x[i]@d);o[j]=max(o[j],-x[j]@d)
        return np.flatnonzero(np.isfinite(o)&(o<-1e-10)).tolist(),float(np.min(abs(o[np.isfinite(o)])))
    U,pm=roots(p,b['edges']);S,qm=roots(q,b['qe'])
    return dict(V=len(b['extreme']),E=len(b['edges']),F=len(q),volume=float(b['volume']),g=b['g'].tolist(),S=S,U=U,
      P=radial(p,b['edges']),Q=radial(q,b['qe']),minimum_abs_outgoing=[pm,qm],evidence='NUMERICAL_NOT_EXACT')

def load():
    path=Path(__file__).parent/'KH93_C434_R82_G6.txt';raw=path.read_bytes()
    assert hashlib.sha256(raw).hexdigest()=='9765712b5ffaa464ed4d677974256294c6d867b77fe77b930d166853f66a92a7'
    y=np.loadtxt(path,skiprows=1)/1e6
    hs=HalfspaceIntersection(np.c_[y,-np.ones(82)],np.zeros(3))
    inc=[sorted(f)for f in hs.dual_facets]
    v=np.array([np.linalg.solve(y[f],np.ones(3))for f in inc])
    b=hull(v);b['y']=y;b['incident']=inc
    return b

def sphere(n):
    k=np.arange(n)+.5;z=1-2*k/n;phi=k*np.pi*(3-np.sqrt(5));r=np.sqrt(1-z*z)
    return np.c_[r*np.cos(phi),r*np.sin(phi),z]

if __name__=='__main__':
    b=load();print(json.dumps(summary(b),indent=2))
```

## FILE joint99.py
```python
"""Joint primary-cover and compensation geometry on the literal R82 body.
Unlike J98's frozen-primary mass sweep, EVERY new point can move here.
Numerical experiments only. Exact endpoint classification is a separate obligation.
"""
from pathlib import Path
import argparse,json
import numpy as np
from scipy.optimize import minimize
from scipy.spatial import ConvexHull
from geom99 import load,hull,summary,sphere

PRIMARY_RAW=np.array([[-71227104,4490850,87329532],[-33724808,-25698269,113145470],
 [-10809318,70913057,4685390],[-82662642,24347695,-23660729]],dtype=np.int64)/1e8
COMP=[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,19,21,23,24,27,30,32,37,39,44,48,53,55]

def samples(base,count=16000,r=.6339):
    p=base['v']-base['g'];y=base['y'];q=y/(1-y@base['g'])[:,None]
    n=sphere(count);scores=n@p.T;support=scores.max(1);winner=scores.argmax(1);ans=[]
    for i in np.flatnonzero(support<r):
        f=base['incident'][winner[i]];corner=f[np.argmax(q[f]@n[i])]
        if corner in COMP:ans.append(n[i])
    return np.r_[ans,q[COMP]/np.linalg.norm(q[COMP],axis=1)[:,None]]

def holes(base,A,r=.6339):
    p=base['v']-base['g'];q=base['y']/(1-base['y']@base['g'])[:,None]
    b=hull(np.r_[p,A]);eq=b['equations'];out=[]
    for i in np.flatnonzero(-eq[:,3]<r-1e-10):
        n=eq[i,:3];v=int(np.argmax(p@n));f=base['incident'][v]
        if f[np.argmax(q[f]@n)] in COMP:out.append(i)
    return b,out,eq[out,:3]

def moment_and_jac(v,t,first):
    """Derivative of actual uniform volume and first moment within current fan."""
    a,b,c=np.moveaxis(v[t],1,0);bc=np.cross(b,c);ca=np.cross(c,a);ab=np.cross(a,b)
    det=np.einsum('ij,ij->i',a,bc);s=a+b+c
    V=det.sum()/6;M=(det[:,None]*s).sum(0)/24;g=M/V
    jm=np.zeros((len(v),3,3));jv=np.zeros((len(v),3));I=np.eye(3)
    for k,cr in enumerate([bc,ca,ab]):
        dm=(s[:,:,None]*cr[:,None,:]+det[:,None,None]*I)/24
        np.add.at(jm,t[:,k],dm);np.add.at(jv,t[:,k],cr/6)
    jg=(jm-g[None,:,None]*jv[:,None,:])/V
    return V,g,np.moveaxis(jg[first:],1,0).reshape(3,-1)

def safe_extreme(p,n,t=.49):
    n=n/np.linalg.norm(n);rr=np.linalg.norm(p,axis=1)
    w=int(np.argmax((1-t)*(p@n)+t*rr))
    return (1-t)*p[w]+t*rr[w]*(1-1e-5)*n,w

class Problem:
    def __init__(self,base,A,w,D,ceiling):
        self.base=base;self.p=base['v']-base['g'];self.w=np.asarray(w,int);self.D=D
        self.centers=self.p[self.w]/2;self.rr=(self.p[self.w]**2).sum(1)/4-1e-8
        self.elder=base['y'][18]/np.linalg.norm(base['y'][18]);self.ceiling=ceiling
        self.calls=0;self.initial=A.copy()
    def objective(self,x):
        A=x.reshape(-1,3);v=np.r_[self.p,A];h=ConvexHull(v);t=h.simplices.copy()
        ar=np.cross(v[t[:,1]]-v[t[:,0]],v[t[:,2]]-v[t[:,0]])
        bad=np.einsum('ij,ij->i',ar,h.equations[:,:3])<0
        t[bad,1],t[bad,2]=t[bad,2].copy(),t[bad,1].copy()
        V,g,J=moment_and_jac(v,t,len(self.p))
        self.calls+=1;return .5*(g@g),g@J
    def constraint(self,x):
        A=x.reshape(-1,3);b=A-self.centers
        vals=[self.rr-(b*b).sum(1),np.max(self.D@A.T,axis=1)-.63391]
        if self.ceiling is not None:vals.append(self.ceiling-A@self.elder)
        return np.concatenate(vals)
    def jac(self,x):
        A=x.reshape(-1,3);k=len(A);m=len(self.D);extra=k if self.ceiling is not None else 0
        J=np.zeros((k+m+extra,3*k))
        for i in range(k):J[i,3*i:3*i+3]=-2*(A[i]-self.centers[i])
        owners=np.argmax(self.D@A.T,axis=1)
        for j in range(m):J[k+j,3*owners[j]:3*owners[j]+3]=self.D[j]
        if self.ceiling is not None:
            for i in range(k):J[k+m+i,3*i:3*i+3]=-self.elder
        return J

def run(ncontrol,ceiling,index,maxiter=250,outer=3):
    base=load();p=base['v']-base['g'];A=PRIMARY_RAW-base['g']
    w=[int(np.argmax(p@a-a@a))for a in A]
    b=hull(np.r_[p,A]);n=-b['g']/np.linalg.norm(b['g'])
    tangent=np.cross(n,[1.,0.,0.]);tangent/=np.linalg.norm(tangent);tangent2=np.cross(n,tangent)
    for j in range(ncontrol):
        phi=2*np.pi*j/max(ncontrol,1);direction=n+.65*(np.cos(phi)*tangent+np.sin(phi)*tangent2)
        a,ww=safe_extreme(p,direction);A=np.r_[A,[a]];w.append(ww)
    D=samples(base);traces=[];total=0
    for it in range(outer):
        prob=Problem(base,A,w,D,ceiling)
        opt=minimize(prob.objective,A.ravel(),jac=True,constraints=[dict(type='ineq',fun=prob.constraint,jac=prob.jac)],
                     method='SLSQP',options=dict(maxiter=maxiter,ftol=1e-13,disp=False))
        A=opt.x.reshape(-1,3)
        Path(__file__).with_name(f'J99_JOINT_{index}_checkpoint.json').write_text(json.dumps(dict(new_points_raw=(A+base['g']).tolist(),witnesses=w,outer=it,success=bool(opt.success),status=int(opt.status),iterations=int(opt.nit),calls=prob.calls,settings=dict(ncontrol=ncontrol,elder_ceiling=ceiling)),indent=2)+'\n')
        b,ii,ns=holes(base,A);total+=prob.calls
        traces.append(dict(outer=it,success=bool(opt.success),status=int(opt.status),message=str(opt.message),iterations=int(opt.nit),
                           calls=prob.calls,centroid_norm=float(np.linalg.norm(b['g'])),constraint_min=float(prob.constraint(opt.x).min()),holes=len(ii)))
        print('END',index,it,traces[-1],flush=True)
        if len(ii)==0:break
        D=np.r_[D,ns]
    ref=summary(b,np.zeros(3));own=summary(b)
    result=dict(identity=f'J99_JOINT_COVER_{index}',input='KH93_C434_R82_G6.txt',primary_reference='J98_four_point_raw_G8',
                new_points_raw=(A+base['g']).tolist(),new_points_centered=A.tolist(),old_witness_indices=w,
                old_vertex_incident_supports=base['incident'],original_centroid_float=base['g'].tolist(),
                settings=dict(ncontrol=ncontrol,elder_ceiling=ceiling,sphere_samples=16000,level=.63391,ball_margin=1e-8,maxiter=maxiter,outer_limit=outer),
                trace=traces,reference=ref,own=own,centroid_norm=float(np.linalg.norm(b['g'])),numerical_component_holes=len(ii),
                minimum_old_witness=float(min(a@(p[ww]-a)for a,ww in zip(A,w))),calls=total,
                evidence='NUMERICAL_NOMINATION_ONLY_NO_EXACT_CENSUS')
    path=Path(__file__).with_name(f'J99_JOINT_{index}.json');path.write_text(json.dumps(result,indent=2)+'\n')
    print('RESULT',index,'E',own['E'],'ref',len(ref['S']),len(ref['U']),'own',len(own['S']),len(own['U']),'g',result['centroid_norm'],flush=True)
    return result

if __name__=='__main__':
    pa=argparse.ArgumentParser();pa.add_argument('--case',type=int,default=0);pa.add_argument('--maxiter',type=int,default=250);args=pa.parse_args()
    cases=[(k,h)for h in [.6339,.8,None]for k in [0,2,4,6]]
    run(*cases[args.case],args.case,maxiter=args.maxiter)
```

## FILE prune99.py
```python
"""Own-centroid greedy vertex deletion on literal R82; numerical nominations only.
Frozen retained support-triple IDs, not optimizer determinism, define candidates.
"""
from pathlib import Path
import argparse,json,time
import numpy as np
from scipy.spatial import ConvexHull
from geom99 import load,hull,summary

def coarse(v):
    """Cheap actual-mass S/U nomination; maximal plane grouping remains numerical."""
    h=ConvexHull(v);t=h.simplices.copy()
    ar=np.cross(v[t[:,1]]-v[t[:,0]],v[t[:,2]]-v[t[:,0]])
    bad=np.einsum('ij,ij->i',ar,h.equations[:,:3])<0
    t[bad,1],t[bad,2]=t[bad,2].copy(),t[bad,1].copy()
    a,b,c=np.moveaxis(v[t],1,0);det=np.einsum('ij,ij->i',a,np.cross(b,c));W=det.sum()
    g=(det[:,None]*(a+b+c)).sum(0)/(4*W);p=v-g
    # Any triangulation supplies positive radial directions to every non-U vertex.
    edges=np.unique(np.sort(np.r_[t[:,[0,1]],t[:,[1,2]],t[:,[2,0]]],axis=1),axis=0)
    d=p[edges[:,1]]-p[edges[:,0]];out=np.full(len(v),-np.inf)
    np.maximum.at(out,edges[:,0],np.einsum('ij,ij->i',p[edges[:,0]],d))
    np.maximum.at(out,edges[:,1],-np.einsum('ij,ij->i',p[edges[:,1]],d))
    U=np.flatnonzero(out<-1e-10)
    if len(U)!=1:return None
    # A stable support has its orthogonal foot strictly inside its maximal polygon.
    eq=h.equations;off=-eq[:,3]-eq[:,:3]@g;q=eq[:,:3]/off[:,None]
    # Global chord maximum equals positivity on actual incident edges. Duplicate
    # normals are excluded; a diagonal cannot invent a positive chord.
    norms=(q*q).sum(1);dots=q@q.T-norms[:,None]
    duplicate=np.max(abs(q[:,None,:]-q[None,:,:]),axis=2)<2e-9
    dots[duplicate]=-np.inf
    maxima=dots.max(1);ss=np.flatnonzero(maxima<-1e-10)
    dirs=[]
    for i in ss:
        if not any(max(abs(q[i]-q[j]))<2e-9 for j in dirs):dirs.append(int(i))
    if len(dirs)!=2:return None
    return dict(g=g,U=U,S=dirs,margin=float(min(min(abs(out)),min(abs(maxima)))))

def run(rounds,resume=None):
    base=load();original=base['v'];ids=list(range(len(original)));trace=[];start=time.time()
    if resume:
        saved=json.loads(Path(resume).read_text());ids=saved['retained_indices'];trace=saved['trace']
    for it in range(rounds):
        choices=[];errors=0;valid=0;v=original[ids]
        for k,old in enumerate(ids):
            vv=np.delete(v,k,axis=0)
            try:
                nom=coarse(vv)
                if nom is None:continue
                bd=hull(vv);s=summary(bd)
            except (AssertionError,ValueError):errors+=1;continue
            if len(s['S'])!=2 or len(s['U'])!=1 or len(s['P']) or len(s['Q'])!=1:continue
            valid+=1
            # Avoid numerically vanishing witnesses; this remains not exact.
            if min(s['minimum_abs_outgoing'])<1e-10:continue
            choices.append(((s['E'],s['Q'][0]['depth'],-min(s['minimum_abs_outgoing'])),k,s))
        if not choices:
            print('NO_DELETION',it,'valid',valid,'errors',errors,flush=True);break
        key,k,s=min(choices,key=lambda a:a[0]);deleted=ids.pop(k)
        trace.append(dict(iteration=len(trace),deleted_original=deleted,eligible=valid,errors=errors,summary=s))
        out=dict(identity='J99_R82_OWN211_PRUNE_NUMERIC',retained_indices=ids,retained_incident_supports=[base['incident'][i]for i in ids],
                 trace=trace,elapsed_seconds=time.time()-start,evidence='NUMERICAL_NO_EXACT_CLASS')
        Path(__file__).with_name('J99_PRUNE_CURRENT.json').write_text(json.dumps(out,indent=2)+'\n')
        print('PRUNE',len(trace),'N',len(ids),'VEF',[s[k]for k in ['V','E','F']],'Q',s['Q'][0]['depth'],'margin',s['minimum_abs_outgoing'],'deleted',deleted,'eligible',valid,'errors',errors,flush=True)
    print('J99_PRUNE_SCOPE_FINISHED_NOT_EXACT',len(trace),len(ids),flush=True)
if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--rounds',type=int,default=5);p.add_argument('--resume');a=p.parse_args();run(a.rounds,a.resume)
```
