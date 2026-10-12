# material-57732bab47ac

AI research material

---

"""Exact maximal H hull, uniform mass, strict/closed-weak mechanics and persistence.
Unchanged function bodies extracted from the supplied CHANGED_NORMAL_EXACT.py.
No originating parent data or numerical libraries required. Do not use -O.
"""
from fractions import Fraction as F

from itertools import combinations

from functools import reduce

from math import gcd,lcm

from pathlib import Path

import argparse,json,hashlib,sys

sys.set_int_max_str_digits(0)

def dot(a,b):return sum(x*y for x,y in zip(a,b))

def sub(a,b):return tuple(x-y for x,y in zip(a,b))

def neg(a):return tuple(-x for x in a)

def cross(a,b):return (a[1]*b[2]-a[2]*b[1],a[2]*b[0]-a[0]*b[2],a[0]*b[1]-a[1]*b[0])

def primitive(a,b):
    g=reduce(gcd,(abs(x) for x in (*a,b)),0)
    assert g
    return tuple(x//g for x in a),b//g

def radial(X,edges):
    R=[dot(x,x) for x in X];events=[]
    for a,b in edges:
        d=sub(X[b],X[a]);den=dot(d,d)
        if den==0:t=F(0)
        else:t=max(F(0),min(F(1),F(-dot(X[a],d),den)))
        p=tuple(X[a][i]+t*d[i] for i in range(3));events.append((dot(p,p),a,b))
    pa=list(range(len(X)));peak=pa[:];members=[{i} for i in pa];bars=[];tree=[[] for _ in X]
    def find(i):
        while pa[i]!=i:pa[i]=pa[pa[i]];i=pa[i]
        return i
    for h,a,b in sorted(events,key=lambda e:(-e[0],e[1],e[2])):
        u,v=find(a),find(b)
        if u==v:continue
        if (R[peak[u]],peak[u])<(R[peak[v]],peak[v]):u,v=v,u
        tree[a].append(b);tree[b].append(a)
        birth=R[peak[v]]
        if birth>h:
            group=members[v].copy();r=peak[v];elder=peak[u];seen={r:None};todo=[r]
            for j in todo:
                if j==elder:break
                for k in tree[j]:
                    if k not in seen:seen[k]=j;todo.append(k)
            path=[elder]
            while path[-1]!=r:path.append(seen[path[-1]])
            path.reverse();depth=(birth-h)/birth
            bars.append(dict(peak=r,elder=elder,birth=str(birth),death=str(h),depth=str(depth),depth_float=float(depth),component=sorted(group),cut=[list(e) for e in edges if (e[0] in group)!=(e[1] in group)],attaining_edge=[a,b],attaining_path=path))
        pa[v]=u;members[u]|=members[v]
    return bars

def hull_h(raw):
 rows=[]
 for a in raw['halfspaces']:
  assert len(a)==4 and all(type(x)==int for x in a) and any(a[:3])
  g=reduce(gcd,map(abs,a));rows.append(tuple(x//g for x in a))
 rows=sorted(set(rows));vertices=set()
 for a,b,c in combinations(rows,3):
  bc=cross(b[:3],c[:3]);ca=cross(c[:3],a[:3]);ab=cross(a[:3],b[:3]);d=dot(a[:3],bc)
  if not d:continue
  z=tuple(a[3]*bc[k]+b[3]*ca[k]+c[3]*ab[k] for k in range(3))
  if d<0:d=-d;z=neg(z)
  if any(dot(n[:3],z)>n[3]*d for n in rows):continue
  vertices.add(tuple(F(t,d) for t in z))
 p=sorted(vertices);assert len(p)>=4;facets=[]
 for a in rows:
  n=a[:3];h=a[3];ids=[i for i,x in enumerate(p) if dot(n,x)==h]
  if len(ids)<3:continue
  drop=max(range(3),key=lambda k:abs(n[k]));axes=[k for k in range(3) if k!=drop]
  ids.sort(key=lambda i:(p[i][axes[0]],p[i][axes[1]]))
  def orient(i,j,k):
   b=sub(p[j],p[i]);c=sub(p[k],p[i]);return b[axes[0]]*c[axes[1]]-b[axes[1]]*c[axes[0]]
  lo=[];hi=[]
  for i in ids:
   while len(lo)>=2 and orient(lo[-2],lo[-1],i)<=0:lo.pop()
   lo.append(i)
  for i in reversed(ids):
   while len(hi)>=2 and orient(hi[-2],hi[-1],i)<=0:hi.pop()
   hi.append(i)
  ring=lo[:-1]+hi[:-1]
  if len(ring)<3:continue
  assert set(ring)==set(ids),'A triple-intersection was not extreme'
  if dot(cross(sub(p[ring[1]],p[ring[0]]),sub(p[ring[2]],p[ring[0]])),n)<0:ring.reverse()
  m=ring.index(min(ring));ring=ring[m:]+ring[:m];facets.append((ring,n,h))
 facets.sort(key=lambda z:sorted(z[0]));edges={};area=[F(0)]*3
 for fi,(f,n,h) in enumerate(facets):
  av=[F(0)]*3
  for i,j in zip(f,f[1:]+f[:1]):
   edges.setdefault(tuple(sorted((i,j))),[]).append(fi);cr=cross(p[i],p[j]);av=[av[k]+cr[k] for k in range(3)]
  assert dot(av,n)>0 and cross(av,n)==(0,0,0)
  area=[area[k]+av[k] for k in range(3)]
 assert area==[0,0,0]
 assert any(dot(a[1],cross(b[1],c[1]))!=0 for a,b,c in combinations(facets,3))
 # Positive facet areas give a strictly positive normal dependence. Together
 # with rank three this excludes every nonzero recession direction.
 assert all(len(v)==2 for v in edges.values())
 assert set(i for f,n,h in facets for i in f)==set(range(len(p)))
 assert len(p)-len(edges)+len(facets)==2
 return p,facets,edges,rows

def audit(raw):
 p,facets,edges,rows=hull_h(raw)
 D=lcm(*(x.denominator for v in p for x in v));I=[tuple(int(D*x) for x in v)for v in p];W=0;M=[0]*3
 for ring,n,h in facets:
  for k in range(1,len(ring)-1):
   a,b,c=[I[i]for i in [ring[0],ring[k],ring[k+1]]];d=dot(a,cross(b,c));W+=d
   M=[M[j]+d*(a[j]+b[j]+c[j]) for j in range(3)]
 assert W>0
 T=4*W*D;center=tuple(F(m,T)for m in M);Y=[tuple(4*W*v[k]-M[k]for k in range(3))for v in I]
 assert all(dot(row[:3],center)<row[3]for row in rows)
 nb=[set()for _ in p]
 for i,j in edges:nb[i].add(j);nb[j].add(i)
 S=[];SW=[];U=[];UW=[];H=[];HW=[];zero=[0,0,0];Q=[]
 for k,(ring,n,h)in enumerate(facets):
  ht=dot(n,Y[ring[0]]);assert ht>0;Q.append(tuple(F(x,ht)for x in n))
  z=[dot(cross(n,sub(I[j],I[i])),neg(Y[i]))for i,j in zip(ring,ring[1:]+ring[:1])];zero[0]+=sum(x==0 for x in z)
  if min(z)>0:S.append(k)
  if min(z)>=0:SW.append(k)
 for i in range(len(p)):
  z=[dot(Y[i],sub(I[j],I[i]))for j in sorted(nb[i])];zero[1]+=sum(x==0 for x in z)
  if max(z)<0:U.append(i)
  if max(z)<=0:UW.append(i)
 for(i,j),(a,b)in sorted(edges.items()):
  d=sub(Y[j],Y[i]);L=dot(d,d);tt=-dot(Y[i],d);qn=tuple(Y[i][k]*L+tt*d[k]for k in range(3));n=facets[a][1];m=facets[b][1]
  A=dot(n,n);B=dot(n,m);C=dot(m,m);det=A*C-B*B;assert det>0
  aa=C*dot(qn,n)-B*dot(qn,m);bb=A*dot(qn,m)-B*dot(qn,n)
  assert tuple(t*det for t in qn)==tuple(aa*n[k]+bb*m[k]for k in range(3))
  z=[tt,L-tt,aa,bb];zero[2]+=sum(x==0 for x in z)
  if min(z)>0:H.append([i,j])
  if min(z)>=0:HW.append([i,j])
 strict=list(map(len,[S,U,H]));weak=list(map(len,[SW,UW,HW]));extra=[b-a for a,b in zip(strict,weak)]
 if extra==[0,0,0]:assert strict[0]+strict[1]-strict[2]==2
 pb=radial(Y,sorted(edges));qb=radial(Q,[tuple(v)for e,v in sorted(edges.items())])
 for bars,factor in [(pb,F(1,T*T)),(qb,F(T*T))]:
  for b in bars:
   for k in ['birth','death']:b[k]=str(F(b[k])*factor)
 return dict(name=raw.get('name','UNNAMED'),V=len(p),E=len(edges),F=len(facets),C=2*len(edges),points=[[str(t)for t in x]for x in p],halfspaces=[list(z)for z in rows],volume=str(F(W,6*D**3)),centroid=list(map(str,center)),first_moment=[str(F(m,24*D**4))for m in M],strict=strict,weak=weak,additional_weak=extra,primitive_zero=zero,S=S,U=U,H=H,faces=[f for f,n,h in facets],edges=[list(e)for e in sorted(edges)],P_bars=pb,Q_bars=qb)

def enc(x,sort=True):
 return (json.dumps(x,sort_keys=sort,separators=(',',':'))+'\n').encode()

def raw(name,rows):return dict(name=name,halfspaces=rows)

def points(z):return [tuple(F(t)for t in x)for x in z['points']]

def owners(H,p,faces):
 out=[]
 for face in faces:
  hits=[i for i,a in enumerate(H)if all(dot(a[:3],p[j])==a[3]for j in face)]
  assert len(hits)==1;out.append(hits[0])
 return out

def independent(z):
 # Positive tetrahedra from the mean of all vertices: a second mass integration.
 p=points(z);nv=len(p);D=lcm(*(x.denominator for a in p for x in a))
 I=[tuple(int(D*x)for x in a)for a in p];s=tuple(sum(a[k]for a in I)for k in range(3))
 Z=[tuple(nv*a[k]-s[k]for k in range(3))for a in I];W=0;M=[0,0,0]
 for f in z['faces']:
  for k in range(1,len(f)-1):
   a,b,c=[Z[j]for j in [f[0],f[k],f[k+1]]];w=dot(a,cross(b,c));assert w>0;W+=w
   for j in range(3):M[j]+=w*(a[j]+b[j]+c[j]+4*s[j])
 assert F(W,6*(nv*D)**3)==F(z['volume'])
 assert [F(v,24*(nv*D)**4)for v in M]==list(map(F,z['first_moment']))
 c=tuple(map(F,z['centroid']));assert all(F(z['first_moment'][i])==F(z['volume'])*c[i]for i in range(3))
 L=lcm(D,*(x.denominator for x in c));Y=[tuple(int(L*(a[k]-c[k]))for k in range(3))for a in p]
 # Global point/chord tests independently check the local vertex/face tests.
 us=[];uw=[]
 for i,y in enumerate(Y):
  m=max(dot(y,sub(v,I[i]))for j,v in enumerate(I)if i!=j)
  if m<0:us.append(i)
  if m<=0:uw.append(i)
 assert us==z['U'] and len(uw)==z['weak'][1]
 H=z['halfspaces'];ow=owners(H,p,z['faces']);N=[H[i][:3]for i in ow]
 h=[dot(n,Y[f[0]])for n,f in zip(N,z['faces'])];ss=[];sw=[]
 for i,n in enumerate(N):
  m=max(dot(n,k)*h[i]-dot(n,n)*h[j]for j,k in enumerate(N)if i!=j)
  if m<0:ss.append(i)
  if m<=0:sw.append(i)
 assert ss==z['S'] and len(sw)==z['weak'][0]
 assert z['additional_weak']==[0,0,0] and z['primitive_zero']==[0,0,0]
 assert len(z['P_bars'])==len(us)-1 and len(z['Q_bars'])==len(ss)-1
 for b in z['P_bars']+z['Q_bars']:
  assert F(b['birth'])>F(b['death'])>0 and F(b['depth'])==(F(b['birth'])-F(b['death']))/F(b['birth'])
 return dict(mass_second_origin=True,global_vertex_and_polar_root_checks=True)
