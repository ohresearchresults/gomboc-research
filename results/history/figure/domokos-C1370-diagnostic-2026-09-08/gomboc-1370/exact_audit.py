"""Exact integer polyhedral geometry/ordinary-centroid/all-feature audit.
Input is an integer V table with common denominator and an oriented closed
triangulation. Every support is tested globally; maximal facets are rebuilt.
No floating-point computation is used by audit().
"""
from collections import defaultdict,Counter
from math import gcd
from functools import reduce
from itertools import combinations
import json,gzip,csv
from pathlib import Path

def dot(a,b):return sum(x*y for x,y in zip(a,b))
def sub(a,b):return tuple(x-y for x,y in zip(a,b))
def cross(a,b):return (a[1]*b[2]-a[2]*b[1],a[2]*b[0]-a[0]*b[2],a[0]*b[1]-a[1]*b[0])
def det(a,b,c):return dot(a,cross(b,c))
def prim(t):
 g=reduce(gcd,t);assert g;return tuple(x//g for x in t)
def rows(path):
 with gzip.open(path,'rt') as f:return [tuple(map(int,row)) for row in csv.reader(f)]

def audit(I,T,D=1,expected=None):
 assert len(set(I))==len(I);assert len(set(map(frozenset,T)))==len(T)
 Fd={};occ=defaultdict(list);tf=[];W=0;M=[0]*3
 for k,tri in enumerate(T):
  a,b,c=[I[i] for i in tri];n=cross(sub(b,a),sub(c,a));h=dot(n,a);assert h>0,(k,'orientation',tri)
  key=prim((*n,h));n=key[:3];h=key[3]
  # Exact global support, not a local convexity or Qhull-tolerance test.
  assert all(dot(n,p)<=h for p in I),(k,'not-support',tri)
  fid=Fd.setdefault(key,len(Fd));tf.append(fid)
  for i,j in zip(tri,tri[1:]+tri[:1]):occ[tuple(sorted((i,j)))].append((fid,i,j,k))
  d=det(a,b,c);assert d>0;W+=d
  for j in range(3):M[j]+=d*(a[j]+b[j]+c[j])
 assert W>0
 planes=list(Fd);bd=defaultdict(dict);edges=[];neigh=defaultdict(set);faceincident=defaultdict(set)
 for e,v in occ.items():
  assert len(v)==2,(e,v)
  f,i,j,k=v[0];g,jj,ii,l=v[1];assert i==ii and j==jj
  if f==g:continue
  assert i not in bd[f] and j not in bd[g];bd[f][i]=j;bd[g][j]=i;edges.append((i,j,f,g));neigh[i].add(j);neigh[j].add(i)
  for p in [i,j]:faceincident[p].update([f,g])
 cycles=[]
 for f,plane in enumerate(planes):
  b=bd[f];assert len(b)>=3;p=min(b);cy=[p];p=b[p]
  while p!=cy[0]:
   assert p not in cy;cy.append(p);p=b[p]
  assert len(cy)==len(b)
  for a,b,c in zip(cy,cy[1:]+cy[:1],cy[2:]+cy[:2]):assert dot(plane[:3],cross(sub(I[b],I[a]),sub(I[c],I[b])))>0,('non-extreme boundary',cy)
  cycles.append(cy)
 active=sorted(neigh);assert set(active)==set(range(len(I))),('unused',len(active),len(I))
 assert len(active)-len(edges)+len(cycles)==2
 for i in active:assert any(det(planes[a][:3],planes[b][:3],planes[c][:3]) for a,b,c in combinations(faceincident[i],3)),('rank',i)
 seen={active[0]};todo=list(seen)
 while todo:
  for j in neigh[todo.pop()]:
   if j not in seen:seen.add(j);todo.append(j)
 assert len(seen)==len(active)
 A=4*W;g=reduce(gcd,[A,*M]);A//=g;B=[m//g for m in M];P=[tuple(A*p[j]-B[j] for j in range(3)) for p in I];Q=A*D
 assert all(A*pl[3]-dot(pl[:3],B)>0 for pl in planes)
 W2=0;M2=[0]*3
 for tri in T:
  a,b,c=[P[i] for i in tri];d=det(a,b,c);W2+=d
  for j in range(3):M2[j]+=d*(a[j]+b[j]+c[j])
 assert W2==W*A**3 and M2==[0]*3
 faces={};vu=defaultdict(list);saddles=[];deg=[];zeroprim=0;featuremins=[]
 for i,j,f,g in edges:
  e=sub(P[j],P[i]);p=dot(P[i],e);r=-dot(P[j],e);cr=cross(P[i],P[j]);u=dot(planes[f][:3],cr);v=-dot(planes[g][:3],cr)
  assert p+r==-dot(e,e)
  faces.setdefault(f,[]).append(u);faces.setdefault(g,[]).append(v);vu[i].append(p);vu[j].append(r)
  bits=(-p,-r,u,v);zeroprim+=sum(b==0 for b in bits)
  if min(bits)>0:saddles.append([i,j])
  elif min(bits)==0:deg.append(['E',i,j])
 S=[];U=[]
 for f,v in faces.items():
  if min(v)>0:S.append(cycles[f])
  elif min(v)==0:deg.append(['F',cycles[f]])
 for i,v in vu.items():
  if max(v)<0:U.append(i)
  elif max(v)==0:deg.append(['V',i])
 if not deg:assert len(S)+len(U)-len(saddles)==2
 result=dict(V=len(I),E=len(edges),F=len(cycles),edge_budget=2*len(edges),class_SUH=[len(S),len(U),len(saddles)],stable=S,unstable=sorted(U),saddles=saddles,degeneracies=deg,zero_edge_primitives=zeroprim,raw_denominator=str(D),W=str(W),M=list(map(str,M)),centroid_multiplier=str(A),centroid_subtract=list(map(str,B)),centred_denominator=str(Q),centred_moments=list(map(str,M2)),maximal_cycles=cycles,true_edges=edges)
 if expected is not None:assert result['class_SUH']==list(expected)
 return result,P

if __name__=='__main__':
 import sys
 p=Path(sys.argv[1]);df=json.loads((p/'definition.json').read_text());I=rows(p/'raw_vertices.csv.gz');T=rows(p/'triangles.csv.gz');R,P=audit(I,T,int(df['raw_denominator']));(p/'exact_report.json').write_text(json.dumps(R,indent=2));print(json.dumps({k:R[k] for k in ['V','E','F','edge_budget','class_SUH','stable','unstable','saddles','degeneracies','zero_edge_primitives']},indent=2))
