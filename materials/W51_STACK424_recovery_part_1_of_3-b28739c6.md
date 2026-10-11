# material-b28739c65159

Historical AI scientific source/proof material. Statements retain their original scope; this is not an independently reviewed theorem.

---

# W51_STACK424 Recovery capsule part 1/3

Object: a shallow rational pyramid over the junior stable facet [10,29,30] of the literal W51_ROBUST_G3. This is a useful negative construction, not own110. It has C180, own424, no additional weak equilibria on an explicitly certified punctured interval. Both raw and cosine zero-margin local losses tend to zero while Q>43/56. All three capsule parts are needed for the interval computation. No originating sandbox or full W51 archive is needed.

Save the following complete source as exact_audit.py, UTF-8, LF, including its final newline. Python 3.13.5 standard library only; tested with python -B -S. This file: 7338 bytes, SHA-256 5677821b89059f2791ba4c63e14df3b712067fabad2f476b67dda96ca586b1bb. Part 2 supplies the complete literal input, endpoint generator, reconstruction command and data hashes. Part 3 supplies the complete interval certificate program and certificate hash.

```python
"""Exact maximal-hull, uniform-mass, strict/closed weak S/U/H and P/Q audit.
Standard library only. Inputs are integer coordinate rows / a positive integer D.
Example: python -B -S exact_audit.py W51_ROBUST_G3.json audit.json
No tolerance is used for any combinatorial, equilibrium, or persistence decision.
"""
from __future__ import annotations
from fractions import Fraction as F
from itertools import combinations
from math import gcd
import json,sys

def add(a,b):return tuple(x+y for x,y in zip(a,b))
def sub(a,b):return tuple(x-y for x,y in zip(a,b))
def mul(k,a):return tuple(k*x for x in a)
def dot(a,b):return sum(x*y for x,y in zip(a,b))
def cross(a,b):return (a[1]*b[2]-a[2]*b[1],a[2]*b[0]-a[0]*b[2],a[0]*b[1]-a[1]*b[0])
def det(a,b,c):return dot(a,cross(b,c))
def plane(a,b,c):
    n=cross(sub(b,a),sub(c,a));g=gcd(*n)
    return tuple(x//g for x in n) if g else None

def boundary(ids,p,n):
    drop=max(range(3),key=lambda i:abs(n[i]));axes=[i for i in range(3) if i!=drop]
    ids=sorted(set(ids),key=lambda i:(p[i][axes[0]],p[i][axes[1]]))
    def turn(i,j,k):
        a,b,c=[(p[t][axes[0]],p[t][axes[1]]) for t in (i,j,k)]
        return (b[0]-a[0])*(c[1]-a[1])-(b[1]-a[1])*(c[0]-a[0])
    lo=[];hi=[]
    for i in ids:
        while len(lo)>=2 and turn(lo[-2],lo[-1],i)<=0:lo.pop()
        lo.append(i)
    for i in reversed(ids):
        while len(hi)>=2 and turn(hi[-2],hi[-1],i)<=0:hi.pop()
        hi.append(i)
    q=lo[:-1]+hi[:-1]
    if dot(cross(sub(p[q[1]],p[q[0]]),sub(p[q[2]],p[q[0]])),n)<0:q.reverse()
    q=q[q.index(min(q)):]+q[:q.index(min(q))]
    return q

def hull(p):
    planes={}
    for i,j,k in combinations(range(len(p)),3):
        n=plane(p[i],p[j],p[k])
        if n is None:continue
        h=dot(n,p[i]);vals=[dot(n,a)-h for a in p]
        if min(vals)<0<max(vals):continue
        if min(vals)==max(vals)==0:continue
        if max(vals)>0:n=mul(-1,n);h=-h;vals=[-v for v in vals]
        key=(*n,h)
        if key not in planes:planes[key]=boundary([t for t,v in enumerate(vals) if v==0],p,n)
    if len(planes)<4:raise ValueError('Not a full dimensional bounded hull')
    ff=sorted(planes.items());edges={}
    for t,(key,face) in enumerate(ff):
        for i,j in zip(face,face[1:]+face[:1]):edges.setdefault(tuple(sorted((i,j))),[]).append(t)
    if any(len(a)!=2 for a in edges.values()):raise ValueError('Nonmanifold hull')
    vv=sorted(set(i for _,f in ff for i in f))
    if len(vv)-len(edges)+len(ff)!=2:raise ValueError('Euler failure')
    return vv,ff,edges

def persistence(z,edges):
    r=[dot(v,v) for v in z];pa=list(range(len(z)));pk=list(range(len(z)));sets=[{i} for i in range(len(z))]
    def find(i):
        while pa[i]!=i:pa[i]=pa[pa[i]];i=pa[i]
        return i
    events=[(v,1,i,i) for i,v in enumerate(r)]
    for i,j in edges:
        d=sub(z[j],z[i]);dd=dot(d,d)
        t=max(F(0),min(F(1),-F(dot(z[i],d),dd))) if dd else F(0)
        at=add(z[i],mul(t,d));death=dot(at,at)
        events.append((death,0,i,j))
    events.sort(reverse=True);out=[];active=set()
    for val,kind,i,j in events:
        if kind:active.add(i);continue
        if i not in active or j not in active:raise ValueError('Filtration ordering')
        a,b=find(i),find(j)
        if a==b:continue
        if (r[pk[a]],-pk[a])<(r[pk[b]],-pk[b]):a,b=b,a
        birth=r[pk[b]]
        if birth>val:
            depth=1-F(val,birth)
            out.append(dict(peak=pk[b],elder=pk[a],birth=str(birth),death=str(val),depth=str(depth),depth_float=float(depth),attaining_edge=[i,j],component=sorted(sets[b])))
        pa[b]=a;sets[a]|=sets[b]
    return sorted(out,key=lambda o:F(o['depth']),reverse=True)

def audit(points,D):
    if not isinstance(D,int) or D<=0:raise ValueError('Positive integer denominator required')
    p=[tuple(int(x) for x in row) for row in points]
    if any(len(row)!=3 for row in p) or len(set(p))!=len(p):raise ValueError('Distinct triples required')
    vv,ff,edges=hull(p);v6=0;T=(0,0,0)
    for key,face in ff:
        a=p[face[0]]
        for j in range(1,len(face)-1):
            b,c=p[face[j]],p[face[j+1]];v=det(a,b,c);v6+=v;T=add(T,mul(v,add(add(a,b),c)))
    if v6<=0:raise ValueError('Volume orientation failure')
    d=4*v6;y=[sub(mul(d,a),T) for a in p]
    nbr={i:set() for i in vv}
    for i,j in edges:nbr[i].add(j);nbr[j].add(i)
    strict=[[],[],[]];weak=[[],[],[]];zeros=[0,0,0]
    normals=[k[:3] for k,face in ff];qs=[]
    for t,(key,face) in enumerate(ff):
        n=key[:3];height=d*key[3]-dot(n,T)
        if height<=0:raise ValueError('Centroid not strictly inside')
        qs.append(tuple(F(x,height) for x in n))
        vals=[-dot(cross(n,sub(p[j],p[i])),y[i]) for i,j in zip(face,face[1:]+face[:1])]
        zeros[0]+=sum(v==0 for v in vals)
        if min(vals)>0:strict[0].append(t)
        elif min(vals)>=0:weak[0].append(t)
    for i in vv:
        vals=[-dot(y[i],sub(p[j],p[i])) for j in nbr[i]]
        zeros[1]+=sum(v==0 for v in vals)
        if min(vals)>0:strict[1].append(i)
        elif min(vals)>=0:weak[1].append(i)
    for (i,j),(a,b) in sorted(edges.items()):
        e=sub(p[j],p[i]);ee=dot(e,e);ye=dot(y[i],e);n,m=normals[a],normals[b]
        nn,mm,nm=dot(n,n),dot(m,m),dot(n,m)
        if nn*mm-nm*nm<=0:raise ValueError('Nonmaximal facet adjacency')
        vals=[-ye,d*ee+ye,mm*dot(n,y[i])-nm*dot(m,y[i]),nn*dot(m,y[i])-nm*dot(n,y[i])]
        zeros[2]+=sum(v==0 for v in vals)
        if min(vals)>0:strict[2].append([i,j])
        elif min(vals)>=0:weak[2].append([i,j])
    vmap={old:new for new,old in enumerate(vv)}
    pe=[(vmap[i],vmap[j]) for i,j in edges]
    P=persistence([y[i] for i in vv],pe)
    for bar in P:
        for key in ('peak','elder'):bar[key]=vv[bar[key]]
        bar['attaining_edge']=[vv[i] for i in bar['attaining_edge']]
        bar['component']=[vv[i] for i in bar['component']]
    Q=persistence(qs,[tuple(owners) for owners in edges.values()])
    counts=list(map(len,strict));wc=list(map(len,weak))
    if not any(wc) and counts[0]+counts[1]-counts[2]!=2:raise ValueError('Morse census failure')
    if not any(wc) and (len(P)!=counts[1]-1 or len(Q)!=counts[0]-1):raise ValueError('Persistence/census mismatch')
    return dict(V=len(vv),E=len(edges),F=len(ff),C=2*len(edges),strict=counts,additional_weak=wc,primitive_zero=zeros,
        volume=str(F(v6,6*D**3)),centroid=[str(F(t,d*D)) for t in T],strict_ids=strict,weak_ids=weak,
        vertices=vv,interior_or_nonextreme=[i for i in range(len(p)) if i not in vv],
        facets=[dict(normal=list(key[:3]),offset=key[3],vertices=face) for key,face in ff],
        edges=[dict(vertices=list(e),owners=a) for e,a in sorted(edges.items())],
        P=P,Q=Q,persistence_scale='P squared-radius units are (4*V6*D)^2 times physical; Q squared-radius units are physical/(4*V6*D)^2. Relative depths unchanged.')

if __name__=='__main__':
    if len(sys.argv)!=3:raise SystemExit('usage: exact_audit.py INPUT.json OUTPUT.json')
    with open(sys.argv[1]) as f:inp=json.load(f)
    out=audit(inp['points'],inp['denominator']);out['name']=inp.get('name','unnamed')
    with open(sys.argv[2],'w') as f:json.dump(out,f,sort_keys=True,separators=(',',':'));f.write('\n')
    print('EXACT_AUDIT_PASS',out['name'],out['V'],out['E'],out['F'],out['strict'],out['additional_weak'],out['primitive_zero'],len(out['P']),len(out['Q']))
```
