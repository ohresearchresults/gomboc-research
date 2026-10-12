# material-4a916e9b4b7d

AI research material

---

#!/usr/bin/env python3
"""Exact rational filled-convex-hull mechanics, exhaustive supports, true facets/edges.
Input JSON: integer points and denominator. Standard library only.
Run: python -B -S exact_poly.py body.json report.json
"""
import itertools,json,math,sys
from fractions import Fraction as F
from functools import reduce

def dot(a,b):return sum(x*y for x,y in zip(a,b))
def add(a,b):return tuple(x+y for x,y in zip(a,b))
def sub(a,b):return tuple(x-y for x,y in zip(a,b))
def mul(a,t):return tuple(x*t for x in a)
def cross(a,b):return (a[1]*b[2]-a[2]*b[1],a[2]*b[0]-a[0]*b[2],a[0]*b[1]-a[1]*b[0])
def det(a,b,c):return dot(a,cross(b,c))
def qstr(x):return str(x.numerator) if x.denominator==1 else f'{x.numerator}/{x.denominator}'
def classify(signs):
    if all(x>0 for x in signs):return 'strict'
    if all(x>=0 for x in signs):return 'weak'
    return 'no'

def audit(data):
    A=sorted(set(tuple(int(y) for y in x) for x in data['points']));den=int(data['denominator'])
    if den<=0 or len(A)<4:raise ValueError('invalid input')
    if not any(det(sub(b,A[0]),sub(c,A[0]),sub(d,A[0])) for b,c,d in itertools.combinations(A[1:],3)):raise ValueError('not three dimensional')
    planes={}
    for a,b,c in itertools.combinations(A,3):
        n=cross(sub(b,a),sub(c,a))
        if n==(0,0,0):continue
        h=dot(n,a);s=[dot(n,v)-h for v in A]
        if max(s)>0 and min(s)<0:continue
        if max(s)>0:n=mul(n,-1);h=-h;s=[-z for z in s]
        g=reduce(math.gcd,[abs(z) for z in (*n,h)])
        key=tuple(z//g for z in (*n,h))
        planes[key]=[i for i,z in enumerate(s) if z==0]
    ext=[]
    for i in range(len(A)):
        ns=[key[:3] for key,inds in planes.items() if i in inds]
        if any(det(*t)!=0 for t in itertools.combinations(ns,3)):ext.append(i)
    idx={a:i for i,a in enumerate(ext)};verts=[A[i] for i in ext]
    plane_keys=sorted(planes)
    fsets=[set(idx[i] for i in planes[k] if i in idx) for k in plane_keys]
    edge_faces={}
    for i,j in itertools.combinations(range(len(fsets)),2):
        meet=fsets[i]&fsets[j]
        if len(meet)>2:raise AssertionError('non-extreme point in edge intersection')
        if len(meet)==2:edge_faces[tuple(sorted(meet))]=[i,j]
    edges=sorted(edge_faces);cycles=[]
    for fi,fs in enumerate(fsets):
        adj={i:[] for i in fs}
        for e,owners in edge_faces.items():
            if fi in owners:a,b=e;adj[a].append(b);adj[b].append(a)
        assert len(fs)>=3 and all(len(v)==2 for v in adj.values())
        start=min(fs);cyc=[start];prev=None;cur=start
        while True:
            nxt=min(v for v in adj[cur] if v!=prev)
            if nxt==start:break
            assert nxt not in cyc
            cyc.append(nxt);prev,cur=cur,nxt
        assert len(cyc)==len(fs)
        a,b,c=[verts[k] for k in cyc[:3]]
        if dot(cross(sub(b,a),sub(c,a)),plane_keys[fi][:3])<0:cyc=[cyc[0]]+list(reversed(cyc[1:]))
        # Every boundary turn has correct strict orientation; all vertices on support.
        for a,b,c in zip(cyc,cyc[1:]+cyc[:1],cyc[2:]+cyc[:2]):
            assert dot(cross(sub(verts[b],verts[a]),sub(verts[c],verts[b])),plane_keys[fi][:3])>0
        cycles.append(cyc)
    N=len(verts);M=len(edges);K=len(cycles);assert N-M+K==2
    adj=[set() for _ in verts]
    for a,b in edges:adj[a].add(b);adj[b].add(a)
    seen={0};stack=[0]
    while stack:
        i=stack.pop()
        for j in adj[i]-seen:seen.add(j);stack.append(j)
    assert len(seen)==N
