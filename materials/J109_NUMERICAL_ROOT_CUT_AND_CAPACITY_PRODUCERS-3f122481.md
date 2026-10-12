# material-3f12248165a7

AI research material · [Export notes](../catalog/coverage.md#text-records)

---

# J109 numerical nomination producers — complete source, not an exact census

These three complete units produced the numerical new-root cut and moment-capacity probes that led to the separately exact J109 theorem. Required input R82.txt is supplied verbatim in [internal-source-reference], J109_EXACT_ALL_DIRECT_ROOT_CUT_CAPACITY.md; that exact material and this material together are complete dependencies. No other workspace, code or checkpoint is imported. Place R82.txt and the three FILE blocks in one directory. Run `python cutroots109.py` and `python capacity109.py`. Actual execution environment: CPython3.13.5, NumPy2.3.5, SciPy1.17.0. No optimizer, seed or omitted parameter. Floating predicates, Qhull, coplanarity tolerances and bar floors are used ONLY for nomination, never for exact acceptance.

The nine cut scales are literal in the producer:1.0001,1.01,1.05,1.1,1.2,1.5,2,3,5. The new normal is the minimum-norm solution of both old polar-root equalities at the numerically integrated old centroid, multiplied by the scale. At scale1.0001 the numerical root cut has V148/E222/F76, actual S19/U32, reference S1/U3, volume1.075961816973 and actual centre displacement approximately(0.260850706325,0.070921980625,-0.116903565740). Thus removing both old stable roots at the reference point is neither actual S1 nor reference110. The control changes the whole physical body. All nine full numerical P/Q bar lists, new normals and own/reference outputs are generated, not hidden below a selected largest bar.

For the selected cut the numerical positive first moment is0.013384894277620157. A dense numerical inner approximation to the compulsory K-paraboloid negative core gave approximately-0.27986067994, showing the capacity obstruction before the exact proof was derived. Those numbers and the point cloud are not exact certificates. The separately executed all-directions J109 proof uses only a rational ball, exact facet areas and dyadic boxes; it does not rely on this numerical cloud, sampled directions or these census thresholds.

Files and observed hashes:
- R82.txt1888B SHA9765712b5ffaa464ed4d677974256294c6d867b77fe77b930d166853f66a92a7 (required exact input material above).
- geometry109.py4286B SHA5a61893fd75b1e7e8d261bbbe0f42ca88a2c53dadf65da8e38aa723068189479.
- cutroots109.py651B SHAdc57ce052a0ce3b799b0660a5dbe8c9eec0cf3e216c287de3a0fa788587d261c.
- capacity109.py1590B SHA3d79f346bf998b4473e65bcc2d0f88fbbaf1f9439378052a57eb392276542d4e.
- Generated ROOT_CUTS109.json108989B SHA9febcdd26f6366e26b2e796d6968728a450c50f6cf808599b06f03ebfd4c91af.
- Generated CAPACITY109_NUMERICAL.json502484B SHA5e9a2fa3e4a5a19d39af2e282d9af419556857ccf02ee75006075406098f4e6c.
Numerical output hashes identify observed floating output, not a cross-platform bitwise portability promise or a new canonical body. The complete deterministic formulas, exact input and every sampling parameter are retained; exact theorem replay is independent of these numerical outputs. Successful numerical execution prints nine finite cut rows and the lines starting `rho h R Jplus ballJminus cap_upper` and `compulsory actual-K inner`, then writes the two JSON files.

### FILE geometry109.py
```python
"""Numerical nomination geometry; not an exact equilibrium auditor.
Qhull supplies facets. Coplanarity is resolved against original H incidence.
All uniform masses are integrated over the actual reconstructed filled hull.
"""
from __future__ import annotations
import itertools, json
from pathlib import Path
import numpy as np
from scipy.spatial import ConvexHull, QhullError

def mass(v:np.ndarray):
    hull=ConvexHull(v)
    t=v[hull.simplices].copy()
    signs=np.einsum('ij,ij->i',np.cross(t[:,1]-t[:,0],t[:,2]-t[:,0]),hull.equations[:,:3])
    flip=signs<0; temp=t[flip,1].copy();t[flip,1]=t[flip,2];t[flip,2]=temp
    w=np.einsum('ij,ij->i',t[:,0],np.cross(t[:,1],t[:,2]))
    vol=w.sum()/6
    if vol<=0:raise ValueError('nonpositive volume')
    c=(w[:,None]*t.sum(axis=1)).sum(axis=0)/(24*vol)
    return vol,c,hull

def from_h(q:np.ndarray):
    dual=ConvexHull(q)
    if np.max(dual.equations[:,3])>=-1e-10:raise ValueError('origin not strictly in dual hull')
    v=np.linalg.solve(q[dual.simplices],np.ones((len(dual.simplices),3,1)))[:,:,0]
    # Only merge genuinely close nominations, while retaining full coordinates.
    keep=[]
    for x in v:
        if not keep or np.min(np.linalg.norm(np.asarray(keep)-x,axis=1))>1e-9:keep.append(x)
    v=np.asarray(keep)
    vol,c,hull=mass(v)
    tight=np.abs(v@q.T-1)<2e-8
    faces=[np.flatnonzero(tight[:,i]) for i in range(len(q))]
    active=np.asarray([i for i,f in enumerate(faces) if len(f)>=3],dtype=int)
    e=[];eq=[]
    for i,j in itertools.combinations(range(len(v)),2):
        shared=np.flatnonzero(tight[i]&tight[j])
        if len(shared)==2:e.append((i,j));eq.append(tuple(shared))
    if len(v)-len(e)+len(active)!=2:raise ValueError('numerical lattice Euler failure')
    return dict(v=v,volume=vol,centroid=c,edges=np.asarray(e,dtype=int),qedges=np.asarray(eq,dtype=int),active=active,q=q,faces=faces)

def bars(v,e,threshold=1e-13):
    rr=np.einsum('ij,ij->i',v,v)
    i,j=e.T;d=v[j]-v[i];dd=np.einsum('ij,ij->i',d,d)
    t=np.clip(-np.einsum('ij,ij->i',v[i],d)/dd,0,1)
    w=v[i]+t[:,None]*d;death=np.einsum('ij,ij->i',w,w)
    par=np.arange(len(v));out=[]
    def root(a):
        while par[a]!=a:par[a]=par[par[a]];a=par[a]
        return a
    for k in np.argsort(-death):
        a,b=root(i[k]),root(j[k])
        if a==b:continue
        if (rr[a],int(a))<(rr[b],int(b)):a,b=b,a
        dep=(rr[b]-death[k])/rr[b]
        if dep>threshold:out.append(dict(root=int(b),edge=[int(i[k]),int(j[k])],birth=float(rr[b]),death=float(death[k]),depth=float(dep)))
        par[b]=a
    return sorted(out,key=lambda x:-x['depth'])

def census(s, centre=None):
    c=s['centroid'] if centre is None else np.asarray(centre)
    p=s['v']-c;q=s['q']/(1-s['q']@c)[:,None]
    def roots(v,e,active):
        score=np.full(len(v),-np.inf)
        for i,j in e:
            score[i]=max(score[i],v[i]@(v[j]-v[i]));score[j]=max(score[j],v[j]@(v[i]-v[j]))
        return [int(i) for i in active if score[i]<-1e-10]
    U=roots(p,s['edges'],range(len(p)));S=roots(q,s['qedges'],s['active'])
    return dict(V=len(p),E=len(s['edges']),F=len(s['active']),volume=float(s['volume']),centroid=s['centroid'].tolist(),S=S,U=U,P=bars(p,s['edges']),Q=bars(q,s['qedges']),numerical_only=True)

def load():
    path=Path(__file__).with_name('R82.txt');lines=path.read_text().splitlines();n,D=map(int,lines[0].split())
    q=np.array([list(map(int,l.split())) for l in lines[1:]],float)/D
    assert len(q)==n
    s=from_h(q);c=s['centroid'];return q/(1-q@c)[:,None],c,s
if __name__=='__main__':
    q,c,s=load();print(json.dumps(census(s),indent=2))

def fast_h(q):
    dh=ConvexHull(q)
    if np.max(dh.equations[:,3])>=-1e-10:raise ValueError('unbounded')
    v=np.linalg.solve(q[dh.simplices],np.ones((len(dh.simplices),3,1)))[:,:,0]
    # Neighbouring dual triangles encode primal true edges for a simple body.
    es=np.array([(i,int(j)) for i,js in enumerate(dh.neighbors) for j in js if i<j],int)
    if np.min(np.linalg.norm(v[es[:,0]]-v[es[:,1]],axis=1))<1e-9:return from_h(q)
    qe=np.unique(np.sort(np.concatenate([dh.simplices[:,[0,1]],dh.simplices[:,[1,2]],dh.simplices[:,[2,0]]]),axis=1),axis=0)
    vol,c,hull=mass(v)
    return dict(v=v,volume=vol,centroid=c,edges=es,qedges=qe,active=dh.vertices,q=q,faces=None)
```
### FILE cutroots109.py
```python
from geometry109 import *
q,g,s=load(); Q=q[[7,18]];b=(Q*Q).sum(axis=1)
r=Q.T@np.linalg.solve(Q@Q.T,b)
print('r0',r,'norm',np.linalg.norm(r),'n',r/np.linalg.norm(r),'h',1/np.linalg.norm(r))
res=[]
for scale in [1.0001,1.01,1.05,1.1,1.2,1.5,2.,3.,5.]:
    rr=scale*r;t=fast_h(np.vstack([q,rr])); a=census(t);ref=census(t,np.zeros(3));
    row=dict(scale=scale,root=rr.tolist(),own=a,reference=ref);res.append(row)
    print(scale,a['V'],a['E'],a['F'],'own',len(a['S']),len(a['U']),'ref',len(ref['S']),len(ref['U']), 'g',a['centroid'],'vol',a['volume'],flush=True)
Path(__file__).with_name('ROOT_CUTS109.json').write_text(json.dumps(res,indent=2)+'\n')
```
### FILE capacity109.py
```python
from geometry109 import *
q,g,s=load();Q=q[[7,18]];r=1.0001*Q.T@np.linalg.solve(Q@Q.T,(Q*Q).sum(axis=1));rho=np.linalg.norm(r);n=r/rho;h=1/rho
B=fast_h(np.vstack([q,r]));v=B['v'];t=v@n
positive=list(v[t>=-1e-12])
for a,b in B['edges']:
    if t[a]*t[b]<0:positive.append(v[a]+(v[b]-v[a])*(-t[a]/(t[b]-t[a])))
vpos=np.unique(np.round(np.asarray(positive),14),axis=0)
Vp,cp,_=mass(vpos);Jpos=Vp*(cp@n)
R=float(np.min(1/np.linalg.norm(q,axis=1)))
I=lambda R,h:2*h*(2*R**3-3*R**2*h+2*h**3)/3
print('rho h R Jplus ballJminus cap_upper',rho,h,R,Jpos,np.pi*I(R,h),Jpos-np.pi*I(R,h))
# A finite inner approximation of the compulsory paraboloid uses disk rings.
# Every ring vertex is in K and |x|+n.x<=2h. Their convex hull is also compulsory.
u=np.cross(n,[0,0,1.]);u/=np.linalg.norm(u);w=np.cross(n,u)
points=[]
for z in np.linspace(-1.2,0,101):
    a=4*h*(h-z)
    if a<0:continue
    for theta in np.linspace(0,2*np.pi,128,endpoint=False):
        direction=np.cos(theta)*u+np.sin(theta)*w
        den=q@direction;right=1-z*(q@n)
        if np.min(right)<-1e-12:continue
        rr=np.sqrt(a)*.999999
        positive=den>1e-12
        rr=min(rr,np.min(right[positive]/den[positive]))
        if rr>0:points.append(z*n+rr*direction)
points=np.asarray(points)
Vm,cm,H=mass(points);Jm=Vm*(cm@n)
print('compulsory actual-K inner',len(points),len(H.vertices),Vm,Jm,'gap',Jpos+Jm)
Path(__file__).with_name('CAPACITY109_NUMERICAL.json').write_text(json.dumps(dict(r=r.tolist(),h=h,R=R,Jpositive=Jpos,Jnegative=Jm,max_total_moment=Jpos+Jm,volume=Vm,points=points[H.vertices].tolist()),indent=2)+'\n')
```
