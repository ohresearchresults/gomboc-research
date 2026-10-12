# material-467088c5ac2b

AI research material · [Export notes](../catalog/coverage.md#text-records)

---

# C360 finite caps and affine families: complete methods, part2/2

Complete dependency: [internal-source-reference] (C360_WHOLE_BASIN_NUMERICAL_METHODS_PART1.md) supplies the exact62-point C360_POINTS.json input and PEAK_MERGE_FLOW.py. Extract the complete three Python files below with terminal newlines. This material is numerical research evidence and scope-limited negative methods, not an exact own110 certificate. Python3.13.5,NumPy2.3.5,SciPy1.17.0,Torch2.10.0+cpu,float64,one thread. Use fresh output directories. None of the finite numerical searches excludes an entire affine orbit or all possible finite material changes.

## Geometry behind the cuts
At a fixed physical reference0 write Q=P^polar. A new q satisfying q·(q_parent−q)>0 has a positive escape toward an old polar point. Existing nonroot escape witnesses remain valid after taking conv(Q,q), including witnesses that become non-exposed input points. This motivates physical caps q·x<=1 while protecting reference stable-flow exclusion. It does NOT fix the actual volume centroid after removal, and a new unique-root assertion needs its own root/exposure guards. Every finite trial in the code rebuilds the filled moments and recenters before classifying. For a candidate physical peak a, the maximal a·q point in the parent's Thales ball is parent/2+|parent|a/(2|a|); the code nominates finite interpolations from the first ray contact toward this point.

## Correction and actual completed results
POLAR_FINITE_CUT.py was executed for8 rounds. Its halfspace intersections are rounded to13 digits and the rebuilt hull groups polar points at10 digits. This can split an OLD planar face into several near-coplanar numerical facets. First-round reported F124 from a120-facet body plusONE plane is already impossible for the intended cut, and is the diagnostic contradiction that caused this implementation to be superseded. Its facet/edge counts and apparent critical census must not be promoted as exact properties of the intended cap polyhedron. The complete flawed unit is retained to make this meaningful negative result reproducible.

FINITE_POLYGON_CUT.py instead clips the actual existing polygon cycles, sharing every intersection point by its original edge key, and adds exactly one new cut polygon. Every reported combinatorial edge has two owners, opposite hull geometry is checked through orientation, and Euler2 is asserted; these are still floating computations, not the independent exact acceptance audit. `python FINITE_POLYGON_CUT.py C360_POINTS.json cut_poly1 --rounds 12` completed all12 rounds, with trial counts[312,312,312,318,330,330,342,324,330,330,330,324]. The authoritative saved round0 selection is parent1,peak20,depth.2,plane[-.02740727549927445,.30442475291281307,.7536815132954925],V69/E188/F121,volume1.6966706044371656,own floating directS1/U2,largest relative Ubar.6816084824082607. The authoritative saved round11 is V85/E212/F129,volume1.6966766709969392,largest Ubar.6768986853785272,bar-threshold S1/U2 BUT direct S1/U3. Round2 already shows the same mismatch: a secondary positive bar below1e-10 is hidden by the objective's count threshold. Thus the apparent count-preserving continuation did not actually maintain U2 throughout. Prior transient coordinator scratch descriptions giving parent55 as this first cut or terminalV106/E236/F132/U5 do not identify the preserved cut_poly1 run and are withdrawn. Use the literal files and this corrected report. The run preserves reference-type motivation, not an exact own-centroid result, and its final U3 is a nonwinner.

AFFINE_PEAK_SEARCH.py uses exp of a symmetric traceless3x3 matrix, i.e.5 real parameters. The actual own centroid transforms affinely exactly, so no free-reference-point artifact occurs. It scores the direct numeric S+U first, then normalized local deficits. `python AFFINE_PEAK_SEARCH.py C360_POINTS.json affine1 --generations 300 --radius 1.5` used seed19,popsize15,no polish,workers1,immediate updating,tol=atol=0. It completed22576 evaluations; SciPy returned success=false with message Maximum number of iterations has been exceeded. Only the baseline identity was a saved improvement: S1/U2,local_loss.00749735418894017,loss3.007441562161695,largest global Ubar.6849764714802097. This is one bounded numerical search, not a global exclusion of affine images.

Source identities: FINITE_POLYGON_CUT.py6119bytes SHA9afbe32c4ffba189eb5d46c251b99f6e8413bd42648ab2e7aff666f17b753b23; POLAR_FINITE_CUT.py3764bytes SHA38c1c3b8f80bfb5e8ff7095d2fc18baa0b5f3dd16f0d1ea839c75943dbfa994c; AFFINE_PEAK_SEARCH.py3627bytes SHA40657d6912a3badfb407a73c3f1fbaeac767e44b408a02036e17276e92c21521. Saved affine terminal.json468bytes SHAa387102dc98d0bb6657b210abfd22d59dfe1d1f75897c69bc5b01f947998c032. Saved polygon round0.json6080bytes SHAb17af93ca6781b7cfbda6075cb9e6e121900b3d1ee070c9427bc31ece98f795b; round11.json7166bytes SHA3d253c11a70145c619c4b8fb2a316da9d3566c468d61207520a60d60040718fc. Exact floating continuation coordinates are separate checkpoint material; hashes alone do not supply them. None is a canonical construction.

## FILE FINITE_POLYGON_CUT.py
```python
"""Numerical finite cap cuts with persistent polygonal incidence.
Avoids falsely triangulating an existing physical planar face after clipping.
Only floating nomination/exploration; exact acceptance is a separate process.
Depends on PEAK_MERGE_FLOW.pairs for the finite radial superlevel merge graph.
"""
import os
os.environ.setdefault('OPENBLAS_NUM_THREADS','1');os.environ.setdefault('OMP_NUM_THREADS','1')
import argparse,json,pathlib
from collections import defaultdict
import numpy as np
from scipy.spatial import ConvexHull
from PEAK_MERGE_FLOW import pairs

def initial(obj):
    v=np.array(obj.get('raw',obj.get('points')),float)
    if 'grid'in obj:v/=obj['grid']
    if 'faces'in obj:return v,obj['faces']
    h=ConvexHull(v);f=h.simplices.copy()
    n=np.cross(v[f[:,1]]-v[f[:,0]],v[f[:,2]]-v[f[:,0]])
    neg=np.einsum('ij,ij->i',n,h.equations[:,:3])<0;f[neg]=f[neg][:,[0,2,1]]
    return v,f.tolist()

def geometry(v,faces):
    tris=np.array([(f[0],f[j],f[j+1]) for f in faces for j in range(1,len(f)-1)])
    a,b,c=v[tris[:,0]],v[tris[:,1]],v[tris[:,2]];d=np.einsum('ij,ij->i',a,np.cross(b,c));volume=d.sum()/6
    center=np.einsum('i,ij->j',d,a+b+c)/(4*d.sum());p=v-center
    q=[];owner=defaultdict(list)
    for i,f in enumerate(faces):
        a=p[f[0]];n=sum((np.cross(p[f[j]]-a,p[f[j+1]]-a) for j in range(1,len(f)-1)),start=np.zeros(3))
        assert n@a>0
        q.append(n/(n@a))
        for a,b in zip(f,f[1:]+f[:1]):owner[tuple(sorted((a,b)))].append(i)
    assert all(len(t)==2 for t in owner.values())
    used=sorted(set(x for f in faces for x in f));assert len(used)-len(owner)+len(faces)==2
    q=np.array(q);pe=np.array(sorted(owner));qe=np.array(sorted(set(tuple(sorted(v)) for v in owner.values())))
    def bars(x,ed):
        pr=pairs(x,ed);pk=x[pr[:,0]];a=x[pr[:,1]];dv=x[pr[:,2]]-a
        t=np.clip(-np.einsum('ij,ij->i',a,dv)/np.einsum('ij,ij->i',dv,dv),0,1)
        B=np.einsum('ij,ij->i',pk,pk);h=np.einsum('ij,ij->i',a+t[:,None]*dv,a+t[:,None]*dv)
        return np.maximum(0,(B-h)/B),pr
    u,up=bars(p,pe);s,sp=bars(q,qe)
    # Direct vertex normal-cone census, not the bar-count tolerance.
    def umax(x,ed):
        out=np.full(len(x),-np.inf)
        for i,j in ed:
            out[i]=max(out[i],x[i]@(x[j]-x[i]));out[j]=max(out[j],x[j]@(x[i]-x[j]))
        return out
    um=umax(p,pe);sm=umax(q,qe)
    st=dict(V=len(used),E=len(pe),F=len(faces),volume=float(volume),centroid=center.tolist(),
         u_count=int((u>1e-10).sum())+1,s_count=int((s>1e-10).sum())+1,
         u_max=float(max(u)),s_max=float(max(s)),u_sum=float(sum(u)),s_sum=float(sum(s)),
         directU=int((um< -1e-12).sum()),directS=int((sm< -1e-12).sum()),
         directU_indices=np.flatnonzero(um< -1e-12).tolist(),directS_indices=np.flatnonzero(sm< -1e-12).tolist())
    return st,(p,q,up,u,sp,s,pe,qe)

def clip(v,faces,z):
    vals=v@z-1;inside=vals<=0
    if all(inside) or not any(inside):return None
    points=v.tolist();new=[];cache={};crossings=set()
    def crossing(a,b):
        e=tuple(sorted((a,b)))
        if e not in cache:
            a,b=e;t=vals[a]/(vals[a]-vals[b]);w=v[a]+t*(v[b]-v[a]);cache[e]=len(points);points.append(w.tolist())
        k=cache[e];crossings.add(k);return k
    for f in faces:
        nf=[]
        for a,b in zip(f,f[1:]+f[:1]):
            if inside[a]:nf.append(a)
            if inside[a]!=inside[b]:nf.append(crossing(a,b))
        if len(nf)>=3:new.append(nf)
    if len(crossings)<3:return None
    vv=np.array(points);ctr=vv[sorted(crossings)].mean(0)
    n=z/np.linalg.norm(z);axis=np.eye(3)[np.argmin(abs(n))];u=np.cross(axis,n);u/=np.linalg.norm(u);w=np.cross(n,u)
    cf=sorted(crossings,key=lambda i:np.arctan2((vv[i]-ctr)@w,(vv[i]-ctr)@u));new.append(cf)
    used=sorted(set(i for f in new for i in f));lookup={j:i for i,j in enumerate(used)}
    return vv[used],[[lookup[i]for i in f]for f in new]

def search(inp,out,rounds=10):
    v,faces=initial(json.load(open(inp)));dst=pathlib.Path(out);dst.mkdir(exist_ok=False)
    base,_=geometry(v,faces);v-=np.array(base['centroid']);volume=base['volume'];history=[]
    for it in range(rounds):
        st,(p,q,up,u,sp,s,pe,qe)=geometry(v,faces)
        # Inspect every actual secondary peak; do not nominate zero-lifetime non-peaks.
        candidates=up[np.argsort(u)[::-1][:min(5,int((u>1e-10).sum()))],0]
        root=int(np.argmax(np.einsum('ij,ij->i',p,p)));best=None;records=[]
        for pk in candidates:
            a=p[pk];direction=a/np.linalg.norm(a)
            for j,parent in enumerate(q):
                far=parent/2+np.linalg.norm(parent)/2*direction
                if far@a<=1+1e-8:continue
                touch=far/(far@a)
                for t in (.05,.2,.4,.6,.8,.95):
                    z=touch+(far-touch)*t
                    if z@p[root]>=1-1e-8 or z@(parent-z)<=1e-10:continue
                    try:
                        ans=clip(p,faces,z)
                        if ans is None:continue
                        vv,ff=ans;ss,_=geometry(vv,ff)
                    except Exception:continue
                    if ss['E']>=311:continue
                    key=(ss['s_count']+ss['u_count'],max(ss['s_max'],ss['u_max']),ss['s_sum']+ss['u_sum'])
                    rec=dict(round=it,peak=int(pk),parent=j,depth=t,plane=z.tolist(),key=list(key),**ss);records.append(rec)
                    if best is None or key<best[0]:best=(key,vv,ff,rec)
        history.append(dict(start=st,trials=records))
        (dst/'history.json').write_text(json.dumps(history,separators=(',',':')))
        if best is None:break
        key,v,faces,rec=best
        print(json.dumps(rec),flush=True)
        (dst/f'round{it}.json').write_text(json.dumps(dict(raw=v.tolist(),faces=faces,selected=rec),separators=(',',':')))
        if rec['s_count']==rec['u_count']==1:break
        v-=np.array(rec['centroid']);v*=(volume/rec['volume'])**(1/3)
    return history
if __name__=='__main__':
    ap=argparse.ArgumentParser();ap.add_argument('input');ap.add_argument('output');ap.add_argument('--rounds',type=int,default=10);a=ap.parse_args();search(a.input,a.output,a.rounds)
```

## FILE POLAR_FINITE_CUT.py — preserved failed numerical geometry representation
```python
"""Finite physical cap cuts nominated by the old polar escape balls.
Float64 nomination only; every trial rebuilds its actual filled hull/centroid.
Reference escape at the old center is NOT treated as own-centroid success.
Depends on the complete PEAK_MERGE_FLOW.py in the same directory.
"""
import os
os.environ.setdefault('OPENBLAS_NUM_THREADS','1');os.environ.setdefault('OMP_NUM_THREADS','1')
import argparse,json,pathlib
import numpy as np
from scipy.spatial import ConvexHull, HalfspaceIntersection
from PEAK_MERGE_FLOW import topology,pairs,inspect

def from_polar(q):
    hs=np.column_stack((q,-np.ones(len(q))))
    v=HalfspaceIntersection(hs,np.zeros(3)).intersections
    v=np.unique(np.round(v,13),axis=0)
    return v

def fast_stats(v):
    f,ids,pe,qe,p,q,c,vol=topology(v)
    def bars(v,edges):
        pr=pairs(v,edges);pk=v[pr[:,0]];a=v[pr[:,1]];dv=v[pr[:,2]]-a
        t=np.clip(-np.einsum('ij,ij->i',a,dv)/np.einsum('ij,ij->i',dv,dv),0,1)
        B=np.einsum('ij,ij->i',pk,pk);h=np.einsum('ij,ij->i',a+t[:,None]*dv,a+t[:,None]*dv)
        b=np.maximum(0,(B-h)/B)
        return b,pr
    u,up=bars(p,pe);s,sp=bars(q,qe)
    return dict(V=len(np.unique(f)),E=len(pe),F=len(ids),volume=vol,centroid=c.tolist(),
        u_count=int((u>1e-10).sum())+1,s_count=int((s>1e-10).sum())+1,
        u_max=float(max(u)),s_max=float(max(s)),u_sum=float(sum(u)),s_sum=float(sum(s))), (p,q,up,u,sp,s)

def search(inp,out,rounds=6,depths=(.2,.4,.6,.8,1.)):
    a=json.load(open(inp));v=np.array(a.get('raw',a.get('points')),float)
    if 'grid'in a:v/=a['grid']
    dst=pathlib.Path(out);dst.mkdir(exist_ok=False)
    base,geo=fast_stats(v);v-=np.array(base['centroid']);initial=base['volume'];history=[]
    for it in range(rounds):
        st,(p,q,up,u,sp,s)=fast_stats(v)
        peaks=up[np.argsort(u)[::-1][:min(3,len(u))],0]
        root=int(np.argmax(np.einsum('ij,ij->i',p,p)))
        best=None;records=[]
        for pk in peaks:
            a=p[pk];direction=a/np.linalg.norm(a)
            for j,parent in enumerate(q):
                far=parent/2+np.linalg.norm(parent)/2*direction
                if far@a<=1+1e-8:continue
                # First tangent contact along the old-center polar ray, then
                # interpolate towards the old-rooted-ball maximizer.
                touch=far/(far@a)
                for t in depths:
                    z=touch+(far-touch)*t
                    if z@p[root]>=1-1e-8:continue
                    if z@(parent-z)<=1e-9:continue
                    try:
                        vv=from_polar(np.vstack((q,z)));ss,_=fast_stats(vv)
                    except Exception:continue
                    if ss['E']>=311:continue
                    # Cardinalities dominate, followed by true basin amplitude.
                    key=(ss['s_count']+ss['u_count'],max(ss['s_max'],ss['u_max']),ss['s_sum']+ss['u_sum'])
                    rec=dict(round=it,peak=int(pk),parent=j,depth=t,plane=z.tolist(),key=list(key),**ss);records.append(rec)
                    if best is None or key<best[0]:best=(key,vv,rec)
        history.append(dict(start=st,trials=records))
        if best is None:break
        key,v,rec=best
        print(json.dumps(rec),flush=True)
        (dst/f'round{it}.json').write_text(json.dumps(dict(raw=v.tolist(),selected=rec),separators=(',',':')))
        (dst/'history.json').write_text(json.dumps(history,separators=(',',':')))
        if rec['s_count']==rec['u_count']==1:break
        v-=np.array(rec['centroid']);v*= (initial/rec['volume'])**(1/3)
    return history
if __name__=='__main__':
    ap=argparse.ArgumentParser();ap.add_argument('input');ap.add_argument('output');ap.add_argument('--rounds',type=int,default=6);a=ap.parse_args();search(a.input,a.output,a.rounds)
```

## FILE AFFINE_PEAK_SEARCH.py
```python
"""Finite volume-centered affine search of the exact C360 point seed.
Nominates metrics, not exact certificates. Affine maps preserve own centering.
Complete dependencies: PEAK_MERGE_FLOW.py and FINITE_POLYGON_CUT.py.
"""
import os
os.environ.setdefault('OPENBLAS_NUM_THREADS','1');os.environ.setdefault('OMP_NUM_THREADS','1')
import argparse,json,pathlib,time
import numpy as np
from scipy.optimize import differential_evolution,minimize
from FINITE_POLYGON_CUT import initial,geometry
from PEAK_MERGE_FLOW import pairs

def setup(inp):
    v,f=initial(json.load(open(inp)));st,(p,q,up,u,sp,s,pe,qe)=geometry(v,f)
    def directed(x,e):
        ed=np.vstack((e,e[:,::-1]));return ed[:,0],x[ed[:,0]],x[ed[:,1]]-x[ed[:,0]]
    return p,q,pe,qe,directed(p,pe),directed(q,qe),f,st

def matrix(x):
    # Symmetric trace-zero logarithm yields a positive-definite determinant1 map.
    a,b,c,d,e=x;T=np.array([[a,c,d],[c,b,e],[d,e,-a-b]])
    w,v=np.linalg.eigh(T);return (v*np.exp(w))@v.T

def stats(A,ctx,bars=False):
    p,q,pe,qe,dd,qd,f,base=ctx;p=p@A.T;q=q@np.linalg.inv(A)
    def escape(x,edges):
        ed=np.vstack((edges,edges[:,::-1]));d=x[ed[:,1]]-x[ed[:,0]]
        t=np.einsum('ij,ij->i',x[ed[:,0]],d)/np.einsum('ij,ij->i',x[ed[:,0]],x[ed[:,0]])
        best=np.full(len(x),-np.inf);np.maximum.at(best,ed[:,0],t);return best
    u=escape(p,pe);s=escape(q,qe)
    # Sorted root-discarded deficits do NOT certify positive escape or H/weak.
    ud=np.sort(np.maximum(0,-u))[:-1];sd=np.sort(np.maximum(0,-s))[:-1]
    out=dict(U=int((u<0).sum()),S=int((s<0).sum()),local_loss=float(ud.sum()+sd.sum()),
       smallest_u=float(np.min(ud)),largest_u=float(np.max(ud)),largest_s=float(np.max(sd)),condition=float(np.linalg.cond(A)))
    if bars:
        def pb(x,edges):
            ps=pairs(x,edges);pk=x[ps[:,0]];a=x[ps[:,1]];d=x[ps[:,2]]-a
            t=np.clip(-np.einsum('ij,ij->i',a,d)/np.einsum('ij,ij->i',d,d),0,1)
            B=np.einsum('ij,ij->i',pk,pk);h=np.einsum('ij,ij->i',a+t[:,None]*d,a+t[:,None]*d)
            return np.maximum(0,(B-h)/B)
        ub=pb(p,pe);sb=pb(q,qe)
        out.update(u_max=float(max(ub)),s_max=float(max(sb)),u_sum=float(sum(ub)),s_sum=float(sum(sb)))
    return out

def search(inp,out,seed=19,generations=200,radius=2.):
    ctx=setup(inp);dst=pathlib.Path(out);dst.mkdir(exist_ok=False);best=[1e99,None,None];evaluations=0
    def fun(x):
        nonlocal evaluations
        A=matrix(x);st=stats(A,ctx);evaluations+=1
        # Integer objective prevents tiny-gap fragmentation, local sum breaks ties.
        loss=st['S']+st['U']+st['local_loss']/(1+st['local_loss'])
        if loss<best[0]:
            rec=dict(x=np.asarray(x).tolist(),matrix=A.tolist(),evaluations=evaluations,loss=loss,**stats(A,ctx,True));best[:]=[loss,np.array(x),rec]
            (dst/'best.json').write_text(json.dumps(rec,separators=(',',':')));print(json.dumps(rec),flush=True)
        return loss
    fun(np.zeros(5))
    result=differential_evolution(fun,[(-radius,radius)]*5,popsize=15,maxiter=generations,seed=seed,polish=False,tol=0,atol=0,updating='immediate',workers=1)
    (dst/'terminal.json').write_text(json.dumps(dict(best=best[2],evaluations=evaluations,success=bool(result.success),message=str(result.message)),separators=(',',':')))
    return best[2]
if __name__=='__main__':
    ap=argparse.ArgumentParser();ap.add_argument('input');ap.add_argument('output');ap.add_argument('--seed',type=int,default=19);ap.add_argument('--generations',type=int,default=200);ap.add_argument('--radius',type=float,default=2.);a=ap.parse_args();search(a.input,a.output,a.seed,a.generations,a.radius)
```
