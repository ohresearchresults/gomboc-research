"""Exact W51 input and homogeneous polyhedron mass / equilibrium calculations.
Input copied from the fully read immutable W51 parent result.
"""
from __future__ import annotations
import json
from fractions import Fraction as F
from pathlib import Path
import numpy as np
from scipy.spatial import ConvexHull

PTS = [[-2678,-1136,975],[-2745,-769,406],[-2212,-627,45],[96,-637,-245],[465,1184,-402],[80,119,-1160],[294,781,-935],[157,537,-1075],[311,1098,-580],[681,814,-815],[565,-379,-1032],[883,11,-962],[947,461,-856],[1007,793,-634],[840,1037,-473],[1206,848,-369],[1174,1065,103],[1389,818,-95],[1535,736,189],[1603,668,465],[1571,172,-108],[1639,563,721],[1644,425,972],[1609,244,1244],[1506,4,1547],[1301,-295,1859],[970,-604,2131],[548,-896,2304],[78,-1126,2365],[-418,-1288,2323],[-968,-1386,2170],[-1604,-1391,1853]]
X = np.array(PTS, dtype=float)/1000

def cross(a,b):
    return [a[1]*b[2]-a[2]*b[1], a[2]*b[0]-a[0]*b[2], a[0]*b[1]-a[1]*b[0]]
def dot(a,b): return sum(u*v for u,v in zip(a,b))

def exact_mass(points, faces):
    vol=F(0); moment=[F(0)]*3
    for face in faces:
        a,b,c=[points[int(i)] for i in face]
        v=dot(a,cross(b,c))/6
        vol+=v
        for j in range(3): moment[j]+=v*(a[j]+b[j]+c[j])/4
    return vol,moment,[m/vol for m in moment]

def oriented_hull(x):
    hull=ConvexHull(x)
    tri=hull.simplices.copy()
    for i,face in enumerate(tri):
        a,b,c=x[face]
        if np.dot(np.cross(b-a,c-a),hull.equations[i,:3])<0:
            tri[i,1],tri[i,2]=tri[i,2],tri[i,1]
    return hull,tri

if __name__=='__main__':
    h,t=oriented_hull(X)
    vol,m,g=exact_mass([[F(v,1000) for v in r] for r in PTS],t)
    edges=sorted({tuple(sorted((int(f[i]),int(f[(i+1)%3])))) for f in t for i in range(3)})
    data=dict(name='W51_ROBUST_G3_literal32',points=PTS,denominator=1000,V=len(h.vertices),E=len(edges),F=len(t),interior=sorted(set(range(len(X)))-set(h.vertices)),volume=str(vol),moment=list(map(str,m)),centroid=list(map(str,g)),centroid_float=list(map(float,g)),simplices=t.tolist(),edges=edges)
    Path('/mnt/data/w51_literal_baseline.json').write_text(json.dumps(data,indent=2))
    print(json.dumps({k:v for k,v in data.items() if k not in ['points','simplices','edges']},indent=2))
    print('max supporting plane at origin',h.equations[:,3].max())


def sub(a,b): return [u-v for u,v in zip(a,b)]
def add(a,b): return [u+v for u,v in zip(a,b)]
def scale(a,k): return [u*k for u in a]

def exact_audit(points):
    """Qhull proposes triangles; all support and equilibrium tests are rational."""
    arr=np.array([[float(c) for c in p] for p in points])
    h,faces=oriented_hull(arr)
    ef={}; normals=[]
    for fi,face in enumerate(faces):
        a,b,c=[points[int(i)] for i in face]
        n=cross(sub(b,a),sub(c,a))
        assert dot(n,n)>0
        for p in points: assert dot(n,sub(p,a))<=0, 'not a supporting triangle'
        on=[j for j,p in enumerate(points) if dot(n,sub(p,a))==0]
        assert set(on)==set(map(int,face)), 'non-simplicial facet: use a merged facet auditor'
        normals.append(n)
        for i in range(3): ef.setdefault(tuple(sorted((int(face[i]),int(face[(i+1)%3])))),[]).append(fi)
    assert all(len(f)==2 for f in ef.values())
    assert len(h.vertices)-len(ef)+len(faces)==2
    vol,moment,g=exact_mass(points,faces)
    assert vol>0
    p=[sub(v,g) for v in points]
    S=[]; U=[]; H=[]; W=[]
    for fi,face in enumerate(faces):
        a,b,c=[p[int(i)] for i in face]; n=normals[fi]
        k=dot(n,a); assert k>0
        foot=scale(n,k/dot(n,n))
        tests=[dot(cross(sub(v,u),sub(foot,u)),n) for u,v in [(a,b),(b,c),(c,a)]]
        if min(tests)>0: S.append(sorted(map(int,face)))
        elif min(tests)==0: W.append(['face',sorted(map(int,face))])
    for i in h.vertices:
        i=int(i)
        tests=[dot(p[i],sub(p[int(j)],p[i])) for j in h.vertices if int(j)!=i]
        if max(tests)<0: U.append(i)
        elif max(tests)==0: W.append(['vertex',i])
    for (ia,ib),(f1,f2) in ef.items():
        a,b=p[ia],p[ib]; d=sub(b,a)
        t=-dot(a,d)/dot(d,d)
        if not (0<=t<=1): continue
        foot=add(a,scale(d,t)); n1,n2=normals[f1],normals[f2]
        aa,ab,bb=dot(n1,n1),dot(n1,n2),dot(n2,n2)
        det=aa*bb-ab*ab; assert det>0
        r1,r2=dot(foot,n1),dot(foot,n2)
        alpha=(bb*r1-ab*r2)/det; beta=(aa*r2-ab*r1)/det
        if alpha>=0 and beta>=0:
            if 0<t<1 and alpha>0 and beta>0: H.append([ia,ib])
            else: W.append(['edge',[ia,ib]])
    return dict(V=len(h.vertices),E=len(ef),F=len(faces),C=2*len(ef),volume=str(vol),centroid=list(map(str,g)),S=S,U=U,H=H,weak=W,counts=[len(S),len(U),len(H)],interior=sorted(set(range(len(points)))-set(map(int,h.vertices))))

if __name__=='__main__':
    audit=exact_audit([[F(v,1000) for v in r] for r in PTS])
    assert audit['counts']==[2,1,1] and not audit['weak']
    Path('/mnt/data/w51_literal_exact_audit.json').write_text(json.dumps(audit,indent=2))
    print('W51_LITERAL_EXACT_AUDIT',json.dumps(audit,sort_keys=True))
