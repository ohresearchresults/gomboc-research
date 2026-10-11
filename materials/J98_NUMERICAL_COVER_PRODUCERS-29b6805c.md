# material-29b6805c733e

Historical AI scientific source/proof material. Statements retain their original scope; this is not an independently reviewed theorem.

Public derivative: internal-record-identifiers-replaced.

---

# J98 complete numerical cover producers

These complete source units preserve the experiments that led to the exact single-cover and four-point results. They are NOT exact class, weak-equilibrium, or primitive-zero auditors. Required literal input is KH93_C434_R82_G6.txt in [internal-source-reference]. The separate numerical mass-producer material and frozen geometry checkpoint material complete the continuation; do not substitute numerical checkpoint labels for exact construction classes.

Observed Python3.13.5, NumPy2.3.5, SciPy1.17.0. Set OPENBLAS_NUM_THREADS=1. Extract FILE blocks using the geometry-core extractor. Reproduce in order: `python geom98.py`; `python cover98.py`; `python doublecover98.py`; `python refinecover98.py`; `python greedycover98.py`. All parameters, sample count100000, Fibonacci rule, old level, height offsets, optimizer options and witness policies are literal in the sources. COVER98_SAMPLES.npz is a deterministic generated dependency, not an omitted input; its byte-level ZIP timestamp is not a scientific seed. Numerical output manifests and frozen complete endpoint coordinates are supplied separately.

Source manifest: geom98.py6350B SHAef80a6fc9043def44dbaa84611852c9f807ae0bab25bfbeceb4771ad7b594ca2; cover98.py4188B SHA6797d764a6a7f4f4128b408ed6b61f707d8d17bd1fac14ab0006181cfda007fd; doublecover98.py3669B SHA71aa47d79a312dc181921a33b3b9c926ac9ca6186e01920edca69f7fc81d31db; refinecover98.py4255B SHAbf27233de8f3701c59615e31b3564f0b40098ed24df7ac14a75bff54a9f06fa6; greedycover98.py3430B SHA4a27274ac7e04b6ce55da1dd30980ec608bce9710784652cf1d17b08a89803d4.

The100000 sphere samples selected2354 old-junior directions including31 old polar-corner normals. The sampled least-norm one-cap radius was about1.49839, exceeding oldU radius1.49687; the exact two-direction obstruction is in the geometry core. Four of15 two-cap split policies produced sampled covers, but the all-new-facet component test found2--5 missed holes. Fixed-witness refinements stalled; that is not a family exclusion. Eleven of18 greedy settings yielded numerical whole-old-component coverage with3--5 apices and E229--237, but reference S9--12, U1, and many actual-centroid equilibria. Only the specifically rationalized four-apex G8 body in the exact capacity material has an exact whole-component certificate.

Important numerical correction made before these persisted outputs: inactive retained input points must not be counted as U merely because their unused accumulator is minus infinity. The final code requires a finite accumulator. Edge event values are clipped to endpoint norms to remove roundoff ordering violations. The numerical classifier still groups planes at2e-9, tests strict S/U at1e-10 and discards persistence bars below1e-13; it cannot certify own110/weak000, especially not tiny bars.

### FILE geom98.py
```python
"""Numerical halfspace/body geometry for finite component-cover research.
This module nominates and diagnoses shapes; it is NOT an exact equilibrium auditor.
"""
from __future__ import annotations
import json
from pathlib import Path
import numpy as np
from scipy.spatial import HalfspaceIntersection, ConvexHull


def read_h(path: str | Path) -> np.ndarray:
    nums=np.loadtxt(path,dtype=np.int64,skiprows=1)
    count,den=map(int,Path(path).read_text().splitlines()[0].split())
    assert nums.shape==(count,3) and den>0
    return nums.astype(float)/den


def boundary_h(y: np.ndarray):
    """Return vertices, ordered support polygons, triangular subdivision and edges.
    Origin must be strictly inside y.x<=1. Small residuals are diagnosed, not certified.
    """
    y=np.asarray(y,float)
    hs=HalfspaceIntersection(np.c_[y,-np.ones(len(y))],np.zeros(3))
    # Recompute each vertex from its incident equations, preserving this nomination ordering.
    verts=[]; incident=[]
    for ff in hs.dual_facets:
        ff=np.array(ff,dtype=int)
        x=np.linalg.lstsq(y[ff],np.ones(len(ff)),rcond=None)[0]
        verts.append(x);incident.append(set(ff.tolist()))
    v=np.array(verts)
    faces=[];active=[];tri=[];edges=set();e2f={}
    for i,n in enumerate(y):
        ids=[j for j,t in enumerate(incident) if i in t]
        if len(ids)<3: continue
        c=v[ids].mean(axis=0);nn=n/np.linalg.norm(n)
        a=v[ids[0]]-c;a/=np.linalg.norm(a);b=np.cross(nn,a)
        pp=v[ids]-c
        ids=np.array(ids)[np.argsort(np.arctan2(pp@b,pp@a))].tolist()
        active.append(i);faces.append(ids)
        tri += [[ids[0],ids[j],ids[j+1]] for j in range(1,len(ids)-1)]
        for j in range(len(ids)):
            e=tuple(sorted((ids[j],ids[(j+1)%len(ids)])))
            edges.add(e);e2f.setdefault(e,[]).append(i)
    assert all(len(f)==2 for f in e2f.values())
    return v,faces,np.array(tri,int),np.array(sorted(edges),int),active,incident,e2f


def mass(v: np.ndarray,t: np.ndarray):
    a,b,c=np.moveaxis(v[t],1,0)
    det=np.einsum('ij,ij->i',a,np.cross(b,c))
    w=det.sum();vol=w/6
    g=(det[:,None]*(a+b+c)).sum(axis=0)/(4*w)
    assert vol>0
    return vol,g


def edges_from_faces(faces):
    return np.array(sorted({tuple(sorted((f[j],f[(j+1)%len(f)])))
        for f in faces for j in range(len(f))}),int)


def hull_v(v: np.ndarray):
    """Triangulated floating hull, grouped coplanar supporting equations."""
    h=ConvexHull(v)
    t=h.simplices.copy()
    for k,tt in enumerate(t):
        a,b,c=v[tt]
        if np.dot(np.cross(b-a,c-a),h.equations[k,:3])<0: t[k,[1,2]]=t[k,[2,1]]
    # Qhull's simplices may subdivide a maximal face. Aggregate only close equations.
    groups=[]
    for k,eq in enumerate(h.equations):
        for item in groups:
            if np.max(np.abs(eq-item[0]))<2e-9:
                item[1].append(k);break
        else:groups.append([eq.copy(),[k]])
    faces=[];normals=[]
    for eq,ks in groups:
        ids=sorted(set(t[ks].ravel()));c=v[ids].mean(axis=0);a=v[ids[0]]-c;a/=np.linalg.norm(a)
        b=np.cross(eq[:3],a);pp=v[ids]-c
        ids=np.array(ids)[np.argsort(np.arctan2(pp@b,pp@a))].tolist()
        faces.append(ids);normals.append(eq)
    vol,g=mass(v,t)
    return dict(v=v,faces=faces,tri=t,edges=edges_from_faces(faces),equations=np.array(normals),volume=vol,g=g)


def radial(points: np.ndarray,edges: np.ndarray,bar_floor:float=1e-13):
    """0-dimensional superlevel graph persistence, with explicit numerical floor."""
    p=np.asarray(points);e=np.asarray(edges,int)
    r2=np.einsum('ij,ij->i',p,p)
    d=p[e[:,1]]-p[e[:,0]]
    tt=np.clip(-np.einsum('ij,ij->i',p[e[:,0]],d)/np.einsum('ij,ij->i',d,d),0,1)
    foot=p[e[:,0]]+tt[:,None]*d;vals=np.einsum('ij,ij->i',foot,foot)
    vals=np.minimum(vals,np.minimum(r2[e[:,0]],r2[e[:,1]]))
    # Vertex events precede equal edge events.
    ev=[(float(r2[i]),0,i) for i in range(len(p))]+[(float(vals[k]),1,k) for k in range(len(e))]
    ev.sort(key=lambda z:(-z[0],z[1],z[2]))
    parent=np.arange(len(p));roots=np.arange(len(p));alive=np.zeros(len(p),bool);bars=[]
    def find(x):
        while parent[x]!=x:
            parent[x]=parent[parent[x]];x=parent[x]
        return x
    for val,typ,k in ev:
        if typ==0:alive[k]=True;continue
        i,j=map(int,e[k]);a,b=find(i),find(j)
        if a==b:continue
        assert alive[i] and alive[j]
        if r2[roots[a]]<r2[roots[b]]:a,b=b,a
        root=int(roots[b]);depth=max(0.,1-val/r2[root])
        if depth>bar_floor:
            bars.append(dict(root=root,edge=e[k].tolist(),birth2=float(r2[root]),death2=val,depth=depth))
        parent[b]=a
    return sorted(bars,key=lambda b:-b['depth'])


def numerical_summary(body,center=None):
    v=body['v'];g=body['g'] if center is None else np.asarray(center)
    p=v-g;eq=body['equations'];normal=eq[:,:3];off=-eq[:,3]-normal@g
    assert np.min(off)>0
    q=normal/off[:,None]
    e=body['edges'];out=np.full(len(v),-np.inf)
    for a,b in e:
        out[a]=max(out[a],np.dot(p[a],p[b]-p[a]));out[b]=max(out[b],np.dot(p[b],p[a]-p[b]))
    ef={}
    for k,f in enumerate(body['faces']):
        for j,a in enumerate(f):ef.setdefault(tuple(sorted((a,f[(j+1)%len(f)]))),[]).append(k)
    qe=np.array([f for f in ef.values() if len(f)==2],int)
    qo=np.full(len(q),-np.inf)
    for a,b in qe:
        qo[a]=max(qo[a],np.dot(q[a],q[b]-q[a]));qo[b]=max(qo[b],np.dot(q[b],q[a]-q[b]))
    return dict(V=len(set(e.ravel())),E=len(e),F=len(q),g=g.tolist(),volume=float(body['volume']),
        S=np.flatnonzero(qo<-1e-10).tolist(),U=np.flatnonzero(np.isfinite(out)&(out<-1e-10)).tolist(),
        P=radial(p,e),Q=radial(q,qe),min_abs_primal=float(np.min(abs(out))),min_abs_polar=float(np.min(abs(qo))))


def load_r82(root=None):
    path=Path(__file__).parent/'KH93_C434_R82_G6.txt' if root is None else root
    y=read_h(path);v,f,t,e,active,inc,ef=boundary_h(y);vol,g=mass(v,t)
    assert active==list(range(len(y)))
    norms=np.linalg.norm(y,axis=1)
    body=dict(y=y,v=v,faces=f,tri=t,edges=e,incident=[sorted(s) for s in inc],
        equations=np.c_[y/norms[:,None],-1/norms],volume=vol,g=g)
    return body

if __name__=='__main__':
    b=load_r82();s=numerical_summary(b)
    print(json.dumps(s,indent=2));Path(__file__).with_name('R82_NUMERICAL_BASELINE.json').write_text(json.dumps(s,indent=2)+'\n')
```
### FILE cover98.py
```python
"""Finite-depth U-witness envelope and spherical component-cover nominations.
All quantities in this module are numerical. It supplies no exact class or coverage certificate.
"""
import json,os
from pathlib import Path
import numpy as np
from scipy.optimize import linprog,minimize
from geom98 import load_r82,radial


def superlevel_component(q,edges,root,level2):
    n=len(q);parent=np.arange(n)
    def find(a):
        while parent[a]!=a:parent[a]=parent[parent[a]];a=parent[a]
        return int(a)
    for i,j in edges:
        d=q[j]-q[i];t=np.clip(-q[i]@d/(d@d),0,1);v=q[i]+t*d
        if v@v>level2:
            a,b=find(i),find(j);parent[b]=a
    return [i for i in range(n) if q[i]@q[i]>level2 and find(i)==find(root)]


def fibonacci_sphere(n):
    k=np.arange(n)+.5;z=1-2*k/n;phi=k*np.pi*(3-np.sqrt(5));rr=np.sqrt(1-z*z)
    return np.c_[rr*np.cos(phi),rr*np.sin(phi),z]


def envelope(points,n,depth):
    """Closed support supremum for <=depth escape links ending in points.
    Depth1 is the union-of-diameter-balls envelope. Depth0 is original support.
    """
    p=np.asarray(points);n=np.asarray(n);r=np.linalg.norm(p,axis=1)
    cs=np.clip(n@p.T/r,-1,1)
    if depth==0:return np.max(cs*r,axis=-1)
    k=depth+1
    return np.max(np.cos(np.arccos(cs)/k)**k*r,axis=-1)


def calculate(count=100000,relative_level_shift=1e-5):
    b=load_r82();p=b['v']-b['g'];y=b['y'];q=y/(1-y@b['g'])[:,None]
    ef={}
    for i,f in enumerate(b['faces']):
        for k,j in enumerate(f):ef.setdefault(tuple(sorted((j,f[(k+1)%len(f)]))),[]).append(i)
    qe=np.array(list(ef.values()),int);bars=radial(q,qe)
    bb=bars[0];r=1/np.sqrt(bb['death2'])*(1-relative_level_shift);level2=1/r**2
    comp=superlevel_component(q,qe,bb['root'],level2)
    sphere=fibonacci_sphere(count);samples=[]
    for ns in np.array_split(sphere,max(1,count//10000)):
        z=ns@p.T;vv=np.argmax(z,axis=1);h=z[np.arange(len(ns)),vv]
        ids=np.flatnonzero(h<r)
        for a in ids:
            face=b['incident'][vv[a]]
            corner=face[np.argmax(q[face]@ns[a])]
            if corner in comp:samples.append(ns[a])
    samples=np.asarray(samples)
    # Include exact support directions of all vertices in this component.
    ncomp=q[comp]/np.linalg.norm(q[comp],axis=1)[:,None]
    sample=np.r_[samples,ncomp]
    infeas=linprog(np.zeros(len(ncomp)),A_eq=np.r_[ncomp.T,np.ones((1,len(ncomp)))],b_eq=[0,0,0,1],bounds=(0,None),method='highs')
    # Arbitrary least-norm cap center if all directions fit a common open hemisphere.
    lp=linprog(np.zeros(3),A_ub=-sample,b_ub=-np.ones(len(sample))*r,bounds=[(None,None)]*3,method='highs')
    cap=None
    if lp.success:
        opt=minimize(lambda x:.5*x@x,lp.x,jac=lambda x:x,constraints=[{'type':'ineq','fun':lambda x:sample@x-r,'jac':lambda x:sample}],method='SLSQP',options={'ftol':1e-12,'maxiter':100})
        cap=dict(success=bool(opt.success),a=opt.x.tolist(),norm=float(np.linalg.norm(opt.x)),margin=float(np.min(sample@opt.x-r)))
    env={}
    for d in [0,1,2,3,4,8,16]:
        vals=np.concatenate([envelope(p,z,d) for z in np.array_split(sample,max(1,len(sample)//5000))])
        k=int(np.argmin(vals));env[str(d)]=dict(min=float(vals[k]),direction=sample[k].tolist(),gap=float(vals[k]-r))
    out=dict(base='KH93_C434_R82_G6',relative_level_shift=relative_level_shift,sphere_count=count,sample_count=len(sample),
        level_support=float(r),level_polar_squared=float(level2),death_support=float(1/np.sqrt(bb['death2'])),
        junior_height=float(1/np.sqrt(bb['birth2'])),root=bb['root'],component=comp,
        outer_radius=float(np.max(np.linalg.norm(p,axis=1))),old_u_nomination=int(np.argmax(np.linalg.norm(p,axis=1))),
        normals_positive_dependence=bool(infeas.success),single_cap_feasible_sample=bool(lp.success),single_cap=cap,envelope=env)
    if infeas.success:out['dependence']=[[comp[i],float(w)] for i,w in enumerate(infeas.x) if w>1e-10]
    np.savez(Path(__file__).with_name('COVER98_SAMPLES.npz'),directions=sample,p=p,q=q)
    return out

if __name__=='__main__':
    out=calculate();text=json.dumps(out,indent=2)+'\n';print(text);Path(__file__).with_name('COVER98_DIAGNOSTICS.json').write_text(text)
```
### FILE doublecover98.py
```python
"""Finite 2-apex cover nominations constrained to old one-step witness balls.
Numerical experimental controls only: sampled coverage is not a uniform proof.
"""
from pathlib import Path
import json
import numpy as np
from scipy.optimize import minimize,linprog
from geom98 import load_r82,hull_v,numerical_summary
from cover98 import envelope

def cover_point(normals,p,r,ids=None):
    if ids is None:ids=range(len(p))
    # Convex solve for each fixed old-witness ball, retaining one elder halfspace.
    elder=np.array(b0['equations'][18,:3]);he=-b0['equations'][18,3]-elder@b0['g']
    cand=[]
    for j in ids:
        v=p[j];cen=v/2;rr=v@v/4-1e-8
        if rr<=0:continue
        # Necessary support of diameter ball in every chosen direction.
        cap=normals@cen+np.sqrt(rr)
        if np.min(cap-r)<0:continue
        cons=[{'type':'ineq','fun':lambda a:normals@a-r,'jac':lambda a:normals},
            {'type':'ineq','fun':lambda a,cen=cen,rr=rr:rr-(a-cen)@(a-cen),'jac':lambda a,cen=cen:-2*(a-cen)},
            {'type':'ineq','fun':lambda a:he-1e-5-elder@a,'jac':lambda a:-elder}]
        opt=minimize(lambda a:.5*a@a,cen,jac=lambda a:a,constraints=cons,method='SLSQP',options={'ftol':1e-11,'maxiter':80})
        if opt.success and min(np.min(c['fun'](opt.x))for c in cons)>-1e-8:
            cand.append((np.linalg.norm(opt.x),j,opt.x))
    return sorted(cand,key=lambda x:x[0])

def main():
    global b0
    b0=load_r82();p=b0['v']-b0['g'];data=np.load(Path(__file__).with_name('COVER98_SAMPLES.npz'));D=data['directions']
    r=0.634 # slightly above old merge, not just under it
    # Sweep a 2-dimensional angular splitting plane; each half covered by one point.
    # The witness at each endpoint is an actual retained old point, not an invented centre.
    axes=[np.array([0.,0.,1.]),np.array([1.,0.,0.]),D[105]-D[2340]]
    records=[]
    for ia,axis in enumerate(axes):
        score=D@axis
        for f in [.2,.35,.5,.65,.8]:
            split=np.quantile(score,f);sets=[D[score<=split],D[score>split]]
            caps=[cover_point(ds,p,r)for ds in sets]
            if not all(caps):
                records.append({'axis':ia,'quantile':f,'feasible':False,'feasible_counts':[len(c)for c in caps]});continue
            # Try best few independent choices; coupled cap moment changes are integrated
            # on the ACTUAL convex hull, never summed as independent overlapping pyramids.
            best=None
            for ca in caps[0][:2]:
                for cb in caps[1][:2]:
                    pts=np.r_[b0['v'],[ca[2]+b0['g'],cb[2]+b0['g']]]
                    bod=hull_v(pts);ref=numerical_summary(bod,center=b0['g']);own=numerical_summary(bod)
                    cov=float(np.min(np.max(D@np.array([ca[2],cb[2]]).T,axis=1)-r))
                    rec={'axis':ia,'quantile':f,'feasible':True,'witnesses':[ca[1],cb[1]],'apices_centered':[ca[2].tolist(),cb[2].tolist()],
                        'sample_cover_margin':cov,'reference':ref,'own':own,'volume_increment':bod['volume']-b0['volume'],'centroid_shift':(bod['g']-b0['g']).tolist()}
                    key=(len(own['S'])+len(own['U']),sum(z['depth']for z in own['Q'])+sum(z['depth']for z in own['P']))
                    if best is None or key<best[0]:best=(key,rec)
            records.append(best[1]);print(json.dumps(best[1]),flush=True)
    out={'scope':'Numerical sampled two-apex cover; no continuous coverage or exact class claimed','support_level':r,'records':records}
    Path(__file__).with_name('DOUBLECOVER98_RESULTS.json').write_text(json.dumps(out,indent=2)+'\n')
    print('J98_TWO_APEX_SAMPLED_COVER_FINISHED_NOT_EXACT')
if __name__=='__main__':main()
```
### FILE refinecover98.py
```python
"""Finite whole-component test and cutting-plane two-cap cover nomination.
Floating geometry and tests: continuous-component criterion is mathematical,
but its numerical implementation here is not an exact certificate.
"""
from pathlib import Path
import json
import numpy as np
from scipy.optimize import minimize
from geom98 import load_r82,hull_v,numerical_summary
from cover98 import superlevel_component

def polar_edges(body):
    ef={}
    for i,f in enumerate(body['faces']):
        for k,j in enumerate(f):ef.setdefault(tuple(sorted((j,f[(k+1)%len(f)]))),[]).append(i)
    assert all(len(z)==2 for z in ef.values())
    return np.array(list(ef.values()),int)

def setup(b,r):
    p=b['v']-b['g'];q=b['y']/(1-b['y']@b['g'])[:,None]
    comp=superlevel_component(q,polar_edges(b),7,1/r**2)
    return p,q,comp

def original_component(n,p,q,incident,component):
    z=int(np.argmax(p@n));ff=incident[z];corner=ff[int(np.argmax(q[ff]@n))]
    return corner in component

def holes(b,apices,r,p,q,component):
    bod=hull_v(np.r_[b['v'],apices+b['g']]);norm=bod['equations'][:,:3];h=-bod['equations'][:,3]-norm@b['g']
    ids=[i for i in range(len(norm))if h[i]<r-1e-11 and original_component(norm[i],p,q,b['incident'],component)]
    # A surviving old-junior direction in L^polar outside the ball connects
    # by norm-increasing segments to a vertex of L^polar in that same old component.
    return bod,ids,norm[ids],h[ids]

def solve_one(D,p,witness,r,a,elder,he):
    v=p[witness];cen=v/2;rr=v@v/4-1e-8
    cons=[{'type':'ineq','fun':lambda x:D@x-r,'jac':lambda x:D},
      {'type':'ineq','fun':lambda x:rr-(x-cen)@(x-cen),'jac':lambda x:-2*(x-cen)},
      {'type':'ineq','fun':lambda x:he-1e-5-elder@x,'jac':lambda x:-elder}]
    op=minimize(lambda x:.5*x@x,a,jac=lambda x:x,constraints=cons,method='SLSQP',options={'ftol':1e-12,'maxiter':120})
    return op,min(np.min(c['fun'](op.x))for c in cons)

def main():
    b=load_r82();records=json.loads(Path(__file__).with_name('DOUBLECOVER98_RESULTS.json').read_text())['records'];D0=np.load(Path(__file__).with_name('COVER98_SAMPLES.npz'))['directions']
    # Old graph component must be evaluated BELOW the old merge. Cover margin
    # is imposed ABOVE it, but old-component membership uses fixed r0=.6339.
    r0=.6339;r=.6341;p,q,component=setup(b,r0);elder=b['equations'][18,:3];he=-b['equations'][18,3]-elder@b['g']
    out=[]
    for no,rec in enumerate(records):
        if not rec['feasible']:continue
        ap=np.array(rec['apices_centered']);ws=rec['witnesses'];axis=[np.array([0.,0.,1.]),np.array([1.,0.,0.]),D0[105]-D0[2340]][rec['axis']]
        score=D0@axis;split=np.quantile(score,rec['quantile']);D=[D0[score<=split],D0[score>split]]
        trace=[]
        for it in range(35):
            bod,ii,ds,hs=holes(b,ap,r0,p,q,component)
            sum0=numerical_summary(bod,center=b['g'])
            trace.append({'iteration':it,'holes':len(ii),'min_height':float(min(hs))if len(hs)else None,'V':sum0['V'],'E':sum0['E'],'F':sum0['F'],'S':len(sum0['S']),'U':len(sum0['U']),'Q':[z['depth']for z in sum0['Q']]})
            if not ii:break
            assignment=np.argmax(ds@ap.T,axis=1)
            for k in range(2):D[k]=np.r_[D[k],ds[assignment==k]]
            trial=[];ok=True
            for k in range(2):
                op,margin=solve_one(D[k],p,ws[k],r,ap[k],elder,he)
                if not op.success or margin<-1e-8:ok=False;break
                trial.append(op.x)
            if not ok:
                trace[-1]['failed_fixed_witness_cover_solve']=True;break
            ap=np.array(trial)
        bod,ii,ds,hs=holes(b,ap,r0,p,q,component)
        z={'initial_record':no,'membership_level':r0,'target_support':r,'witnesses':ws,'apices_centered':ap.tolist(),'numerical_uncovered_old_junior_vertices':len(ii),
           'reference':numerical_summary(bod,center=b['g']),'own':numerical_summary(bod),'volume_increment':bod['volume']-b['volume'],'centroid_shift':(bod['g']-b['g']).tolist(),'trace':trace}
        out.append(z);print(json.dumps(z),flush=True)
    Path(__file__).with_name('REFINED_COVER98_RESULTS.json').write_text(json.dumps(out,indent=2)+'\n')
    print('J98_FINITE_COMPONENT_COVER_NOMINATIONS_FINISHED_NOT_EXACT')
if __name__=='__main__':main()
```
### FILE greedycover98.py
```python
"""Finite whole-component outer-cover tests with strict old-point U witnesses.
This is numerical construction research, not a class/weak-equilibrium verifier.
"""
from pathlib import Path
import json
import numpy as np
from geom98 import load_r82,hull_v,numerical_summary
from refinecover98 import setup,holes

def witness_extremum(p,n,t,shrink=1e-6):
    # Ball centered at (1-t)v, radius t|v|, 0<t<=.5; strict shrink makes
    # x.(v-x)>0 for every genuinely new point, also at t=.5.
    radii=np.linalg.norm(p,axis=1)
    i=int(np.argmax((1-t)*(p@n)+t*radii))
    return (1-t)*p[i]+t*radii[i]*(1-shrink)*n,i

def greedy(D,p,r,t,kmax=15):
    cand=np.array([witness_extremum(p,n,t)[0]for n in D]);wit=[witness_extremum(p,n,t)[1]for n in D]
    covers=cand@D.T>=r
    remaining=np.ones(len(D),bool);inds=[]
    for _ in range(kmax):
        count=covers[:,remaining].sum(axis=1);j=int(np.argmax(count))
        if count[j]==0:break
        inds.append(j);remaining[covers[j]]=False
        if not remaining.any():break
    return cand[inds],[wit[j]for j in inds],int(remaining.sum())

def main():
    b=load_r82();Dall=np.load(Path(__file__).with_name('COVER98_SAMPLES.npz'))['directions'];r0=.6339;p,q,comp=setup(b,r0)
    # 1/4 of dense nominal samples plus every original high corner. The final
    # finite all-new-facet test, not this sample, determines uncovered directions.
    D=np.r_[Dall[::4],Dall[-31:]];out=[]
    for t in [.15,.25,.35,.45,.49,.5]:
        for extra in [.002,.02,.06]:
            r=r0+extra;ap,ws,remaining=greedy(D,p,r,t)
            if remaining:
                out.append({'t':t,'extra':extra,'sample_missing':remaining,'apices_count':len(ap)});continue
            trace=[]
            for it in range(15):
                bod,ii,ds,hh=holes(b,ap,r0,p,q,comp);ref=numerical_summary(bod,center=b['g']);trace.append({'holes':len(ii),'S':len(ref['S']),'E':ref['E']})
                if not ii:break
                # Add one strictly U-safe point against the deepest uncovered facet.
                j=int(np.argmin(hh));a,w=witness_extremum(p,ds[j],t)
                if ds[j]@a<=r0:break
                ap=np.r_[ap,[a]];ws.append(w)
            # Greedily remove whole apices without losing finite component coverage.
            for i in reversed(range(len(ap))):
                aa=np.delete(ap,i,axis=0)
                if len(aa)==0:continue
                bd,ids,_,_=holes(b,aa,r0,p,q,comp)
                if not ids:ap=aa;ws.pop(i)
            bod,ii,ds,hh=holes(b,ap,r0,p,q,comp);ref=numerical_summary(bod,center=b['g']);own=numerical_summary(bod)
            z={'t':t,'extra':extra,'sample_missing':remaining,'apices_count':len(ap),'apices_centered':ap.tolist(),'witnesses':ws,
               'reference':ref,'own':own,'old_junior_holes':len(ii),'centroid_shift':(bod['g']-b['g']).tolist(),
               'volume_increment':bod['volume']-b['volume'],'min_old_witness_chord':float(min(a@(p[w]-a)for a,w in zip(ap,ws))),'trace':trace}
            out.append(z);print(json.dumps({'t':t,'extra':extra,'N':len(ap),'holes':len(ii),'VEF':[ref[k]for k in ['V','E','F']],'refSU':[len(ref['S']),len(ref['U'])],'ownSU':[len(own['S']),len(own['U'])],'dg':z['centroid_shift']}),flush=True)
    Path(__file__).with_name('GREEDY_COVER98_RESULTS.json').write_text(json.dumps(out,indent=2)+'\n')
    print('J98_GREEDY_FINITE_COMPONENT_COVER_SEARCH_FINISHED_NOT_EXACT')
if __name__=='__main__':main()
```
