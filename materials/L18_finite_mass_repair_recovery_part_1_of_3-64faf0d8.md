# material-64faf0d80f09

AI research material

---

# Recovery capsule part 1/3: L18 finite own-centroid mass repair

Object identity: the exact 75-point JOINT56_L18 from J69, V75/E204/F131, C408, own strict222, additional weak000. The new nonrecord finite endpoints are named L18_MASSLIFT_BASE_T14 and L18_MASSLIFT62_T14. Neither is own110. All three parts are required for the complete recovery and original producer. This part supplies the exact input and complete original geometric helper source. Part2 supplies l18_masslift.py. Part3 supplies the original extension runner, fixed rational nominations, replay commands and numerical/exact interpretation.

Save fenced units under their named filenames with a final LF. Observed environment: Python3.13.5, NumPy2.3.5, SciPy1.17.0. Candidate hull incidence comes from SciPy, then all supporting planes and maximal coplanar facets are checked/grouped exactly; finite endpoints are accepted by exact rational support, mass and equilibrium signs, not floating thresholds. The numeric_audit routine is exploratory only. There is no FULL76 dependency.

Input l18_exact_points.json:2357 bytes, SHA-25690d0a3e009fe9a0ff5bef092a8ad6ac9071fa7d1242bb3cdc82b43531aa1f0f6.
Helper l18_support_search.py:7644 bytes, SHA-256e461b52e55d2d5b43684d70bda75465906afe41fbde05685ceab614590b699da.

## l18_exact_points.json
```json
{"denominator":100000000,"points":[[-114525000,-38526902,2815000],[-114408000,-28813483,-21012000],[-110220000,-22670374,-38817000],[-102074000,-18012432,-55623000],[-95244000,-69231584,65065000],[-93745000,-15470943,-67376000],[-84871000,-82040002,89483000],[-83812000,-14029958,-77505000],[-76508000,-13554466,-83525000],[-64581000,-13912297,-90582000],[-61476000,25894000,-14839000],[-62395000,23368000,463000],[-56261000,23741000,8340000],[-52412000,-15218983,-95480000],[-51315000,23453000,14016000],[-52494000,34497000,-19706000],[-42771000,21590000,23057000],[-42863000,2890000,42398000],[-41427000,18386000,27657000],[-41360000,12530000,33866000],[-41047000,44227000,-22695000],[-39278000,42001000,-8155000],[-34778000,-18120125,-100114000],[-33227000,5517000,41437000],[-34030000,41543000,3065000],[-32655000,47126000,-31146000],[-27505000,-19593266,-101349000],[-26092000,6359000,40643000],[-29349000,-3094000,46727000],[-23601000,48813000,-36091000],[-20202000,-21347779,-101916000],[-22835000,44187000,7116000],[-19759000,39126000,14237000],[-15413000,37019000,17653000],[-12669000,-23440927,-101808000],[-11758000,47157000,-43142000],[-9937000,36825000,18784000],[-5171000,-25823125,-100970000],[-4354000,45931000,-43781000],[-656000,39016000,17643000],[-285000,7861000,35467000],[2454000,-27623000,-99473000],[1609000,5616000,35659000],[7524000,7250000,33248000],[9975000,-29293000,-97278000],[8760000,16281000,29866000],[12615000,42039000,15586000],[23787000,44736000,-31885000],[17334000,-30836000,-94391000],[30460000,-17220000,-87918000],[24468000,-32254000,-90824000],[38470000,40587000,-9618000],[31322000,-33549000,-86591000],[29555000,47228000,10455000],[33038000,-44403744,-80951000],[37731000,-34969000,-81714000],[36888000,40349000,12838000],[41804000,34722000,13816000],[43728000,-36211000,-76251000],[41605000,-51828881,-68494000],[44676000,31334000,13390000],[47360000,27874000,12796000],[49134000,-37619000,-70267000],[49897000,24291000,12029000],[52973000,-47543000,-55156000],[53765000,-8364000,-59155000],[55076000,17110000,8707000],[59503000,9479000,4527000],[58901000,-42244000,-45006000],[63005000,1560000,-490000],[63029000,-35973000,-35698000],[65329000,-6139000,-5970000],[66608000,-13854000,-12187000],[65610000,-28928000,-27007000],[66746000,-21494000,-19185000]],"cap":[0,1,2,3,5,7,8,9,13,22,26,30,34,37,54,59,6,4]}
```

## l18_support_search.py
```python
"""Local support geometry and own-volume centroid experiments on exact archived L18.
Input is a JSON file with integer points, a common denominator, and cap labels.
SciPy's hull provides the combinatorial candidate; exact integer plane grouping
then removes all coplanar triangulation edges in audit_integer().
"""
from __future__ import annotations
from collections import defaultdict
from fractions import Fraction
from functools import reduce
from math import gcd
import json, sys
from pathlib import Path
import numpy as np
from scipy.spatial import ConvexHull

def dot(a,b): return sum(x*y for x,y in zip(a,b))
def sub(a,b): return tuple(x-y for x,y in zip(a,b))
def cross(a,b): return (a[1]*b[2]-a[2]*b[1],a[2]*b[0]-a[0]*b[2],a[0]*b[1]-a[1]*b[0])
def primitive(values):
    g=reduce(gcd,(abs(x) for x in values))
    return tuple(x//g for x in values)

def exact_structure(points):
    p=[tuple(map(int,x)) for x in points]
    hull=ConvexHull(np.asarray(p,float))
    groups={}; triangles=[]
    for tri,eq in zip(hull.simplices,hull.equations):
        i,j,k=map(int,tri); n=cross(sub(p[j],p[i]),sub(p[k],p[i]))
        if np.dot(np.asarray(n,float),eq[:3])<0:
            j,k=k,j; n=tuple(-x for x in n)
        h=dot(n,p[i]); key=primitive((*n,h))
        if any(dot(key[:3],q)>key[3] for q in p):
            raise ValueError('Qhull triangle is not an exact supporting triangle')
        groups.setdefault(key,[]).append((i,j,k));triangles.append((i,j,k))
    faces=[]
    for plane,tris in groups.items():
        edges=defaultdict(int)
        for i,j,k in tris:
            for a,b in ((i,j),(j,k),(k,i)):
                if edges[(b,a)]: edges[(b,a)]-=1
                else: edges[(a,b)]+=1
        boundary=[e for e,c in edges.items() if c]
        if any(c>1 for c in edges.values()): raise ValueError('multiplicity')
        nxt=dict(boundary); first=min(nxt);cycle=[first];t=nxt[first]
        while t!=first:
            cycle.append(t);t=nxt[t]
            if len(cycle)>len(boundary): raise ValueError('broken cycle')
        if len(cycle)!=len(boundary): raise ValueError('multiple cycles')
        faces.append({'plane':plane,'cycle':cycle})
    edges=defaultdict(list)
    for f,face in enumerate(faces):
        cyc=face['cycle']
        for i,j in zip(cyc,cyc[1:]+cyc[:1]): edges[tuple(sorted((i,j)))].append(f)
    assert all(len(x)==2 for x in edges.values())
    W=0; M=[0,0,0]
    for i,j,k in triangles:
        d=dot(p[i],cross(p[j],p[k]));W+=d
        for a in range(3): M[a]+=d*(p[i][a]+p[j][a]+p[k][a])
    assert W>0
    return p,faces,edges,W,M

def audit_integer(points,denominator=1):
    p,faces,edges,W,M=exact_structure(points);K=4*W
    active=sorted({v for e in edges for v in e})
    adj={v:[] for v in active}
    for i,j in edges: adj[i].append(j);adj[j].append(i)
    roots=[]; vg={}
    for i in active:
        r=tuple(K*p[i][a]-M[a] for a in range(3))
        scores=[(dot(r,sub(p[j],p[i])),j) for j in adj[i]]
        vg[i]=sorted(scores,reverse=True)
        if all(s<0 for s,j in scores): roots.append(i)
    stable=[];face_guards=[]
    for f,face in enumerate(faces):
        n=face['plane'][:3];cyc=face['cycle'];g=[]
        for i,j in zip(cyc,cyc[1:]+cyc[:1]):
            u=cross(n,sub(p[j],p[i])); r=tuple(M[a]-K*p[i][a] for a in range(3))
            g.append((dot(u,r),[i,j]))
        face_guards.append(g)
        if all(s>0 for s,e in g): stable.append(f)
    saddles=[];eg={}
    for (i,j),(f,g) in edges.items():
        e=sub(p[j],p[i]);ee=dot(e,e); r=tuple(K*p[i][a]-M[a] for a in range(3))
        tnum=-dot(r,e)
        # Edge-foot radial vector numerator with denominator K*(e.e).
        radial=tuple(ee*r[a]+tnum*e[a] for a in range(3))
        n=faces[f]['plane'][:3];m=faces[g]['plane'][:3]
        nn=dot(n,n);mm=dot(m,m);nm=dot(n,m)
        alpha=mm*dot(n,radial)-nm*dot(m,radial)
        beta=nn*dot(m,radial)-nm*dot(n,radial)
        vals=(tnum,K*ee-tnum,alpha,beta);eg[(i,j)]=vals
        if all(v>0 for v in vals): saddles.append((i,j))
    # Primitive zeros are reported; their presence is not itself a weak-equilibrium proof.
    zeros={'vertex':sum(s==0 for x in vg.values() for s,j in x),'face':sum(s==0 for x in face_guards for s,e in x),'edge':sum(s==0 for x in eg.values() for s in x)}
    return {'V':len(active),'E':len(edges),'F':len(faces),'C':2*len(edges),
            'class':[len(stable),len(roots),len(saddles)],'stable_faces':[faces[f]['cycle'] for f in stable],
            'roots':roots,'saddles':saddles,'primitive_zeros':zeros,
            'volume':str(Fraction(W,6*denominator**3)),
            'centroid':[str(Fraction(M[a],K*denominator)) for a in range(3)],
            'vertex_top_scores':{str(i):[[float(Fraction(s,K*denominator**2)),j] for s,j in x[:4]] for i,x in vg.items()}},(p,faces,edges,W,M)

def numeric_audit(p,merge_tol=1e-8):
    p=np.asarray(p,float); hull=ConvexHull(p);groups=[]
    for t,(tri,eq) in enumerate(zip(hull.simplices,hull.equations)):
        hit=None
        for f,grp in enumerate(groups):
            if np.max(np.abs(eq-grp['eq']))<merge_tol:hit=f;break
        if hit is None:groups.append({'eq':eq,'tris':[tri]})
        else: groups[hit]['tris'].append(tri)
    faces=[];triangles=[];edges=defaultdict(list)
    for f,grp in enumerate(groups):
        boundary={}
        for raw in grp['tris']:
            i,j,k=map(int,raw)
            if np.dot(np.cross(p[j]-p[i],p[k]-p[i]),grp['eq'][:3])<0:j,k=k,j
            triangles.append((i,j,k))
            for a,b in ((i,j),(j,k),(k,i)):
                if (b,a) in boundary:del boundary[(b,a)]
                else:boundary[(a,b)]=True
        nxt=dict((a,b) for a,b in boundary);first=min(nxt);cyc=[first];t=nxt[first]
        while t!=first:
            cyc.append(t);t=nxt[t]
            if len(cyc)>len(boundary):raise ValueError('cycle')
        faces.append({'normal':grp['eq'][:3],'height':-grp['eq'][3],'cycle':cyc})
        for i,j in boundary:edges[tuple(sorted((i,j)))].append(f)
    tris=np.asarray(triangles);q=p[tris];d=np.einsum('ij,ij->i',q[:,0],np.cross(q[:,1],q[:,2]));vol=d.sum()/6;c=(d[:,None]*q.sum(axis=1)).sum(axis=0)/(4*d.sum())
    nbs=defaultdict(list)
    for i,j in edges:nbs[i].append(j);nbs[j].append(i)
    vs={i:sorted([(np.dot(p[i]-c,p[j]-p[i]),j) for j in js],reverse=True) for i,js in nbs.items()}
    roots=[i for i,s in vs.items() if s[0][0]<-1e-12]
    fs=[]
    for face in faces:
        cyc=face['cycle'];n=face['normal']
        fs.append([np.dot(np.cross(n,p[j]-p[i]),c-p[i])/np.linalg.norm(p[j]-p[i]) for i,j in zip(cyc,cyc[1:]+cyc[:1])])
    stable=[i for i,s in enumerate(fs) if min(s)>1e-12]
    saddles=[]
    for (i,j),fg in edges.items():
        if len(fg)!=2:raise ValueError('edge degree')
        f,g=fg;e=p[j]-p[i];t=-np.dot(p[i]-c,e)/np.dot(e,e)
        n=faces[f]['normal'];m=faces[g]['normal'];r=p[i]+t*e-c
        ab=np.linalg.solve([[1,np.dot(n,m)],[np.dot(n,m),1]],[np.dot(n,r),np.dot(m,r)])
        if 1e-12<t<1-1e-12 and min(ab)>1e-12:saddles.append((i,j))
    return {'V':len(nbs),'E':len(edges),'F':len(faces),'C':2*len(edges),'class':[len(stable),len(roots),len(saddles)],'roots':roots,'saddles':saddles,'stable':[faces[f]['cycle'] for f in stable],'centroid':c,'volume':vol,'vertex_scores':vs,'faces':faces,'face_scores':fs,'edges':edges}

if __name__=='__main__':
    data=json.loads(Path(sys.argv[1]).read_text());report,_=audit_integer(data['points'],data['denominator']);out=sys.argv[2] if len(sys.argv)>2 else 'audit.json';Path(out).write_text(json.dumps(report,sort_keys=True,indent=2)+'\n');print(json.dumps({k:v for k,v in report.items() if k!='vertex_top_scores'},indent=2))
```
