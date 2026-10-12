# material-a711ab4372db

AI research material · [Export notes](../catalog/coverage.md#text-records)

---

# CA95 literal input-label correction and complete standalone exact audit

The immutable parent figure-0399 was read completely from cursor 0 through EOF, SHA256 c30ee459df73233920d909ab76375f089eae0cb264d9520a9db9ac700549c7da. Its 24 literal input rows define the SAME integer126_g100 body, not a new geometry. The old brief's input stable triples [0,2,22] and [17,18,20] and saddle 22-23 are incorrect for these literal rows. Correct input labels: stable maximal facets {1,12,14} and {14,15,19}; unstable input16; saddle input18-23. Input21 is nonextreme. Do not change old sorted/centered REPORT labels without constructing their correspondence.

Exact V23/E63/F42,C126, own-filled-centroid strict211/weak000. Volume4152473/1500000, centroid (101311319/830494600,520540313/6643956800,-77026377/3321978400). Minimal common denominator of centered extreme vertices6643956800,33 bits; largest centered common-denominator integer34 bits. There are42 positive centered tetrahedra and exactly zero first moments. This corrects labels, not the canonical C622 record or an existing exclusion theorem's geometry.

The complete new audit below exhaustively enumerates rational V-hull supports, maximal polygonal facets and true edges; computes own ordinary-volume mass with interior-anchor tetrahedra; enumerates every strict/weak face, vertex and edge equilibrium; and recomputes positive centered mass. It is one complete auditor, not by itself a claim of two independent implementations. The immutable parent's separate audit and the later recovered GEOM_EXACT A/B source are distinct evidence.

Recovery: save the following code, including its final newline, as EXACT_POINTS.py. CPython3.13.5 standard library, no -O. Source5247bytes SHA256 a120fc81b941666aa6b2fc78857c0a8a6b63e62732939a8e68bab2b6c78b8f6b. Run `python -B -S EXACT_POINTS.py > CA95_LITERAL_A.json`. Observed output3215bytes SHA256 641aee6442a3d3e73d64f07f6ea5d2cdc92ba0cc59c1427833d6f010a0d10c1b. Successful exit0 and exact output identity are terminal checks. JSON also contains every rational input, maximal support/facet and true edge, so reconstruction does not depend on a sandbox or old REPORT.

```python
#!/usr/bin/env python3
"""Exact convex-hull, filled-mass and all-feature audit of rational point inputs.
Stdlib CPython 3.13.5. Intended for small point sets. Assertions are mandatory.
Independent mathematical formulations may use the returned complete halfspaces.
"""
from fractions import Fraction as Q
from itertools import combinations
from math import gcd,lcm
from pathlib import Path
import json,sys
assert __debug__
ROWS='''64 -64 107
74 -46 106
57 -106 83
26 -114 89
-4 -129 74
-48 -128 67
-82 -129 36
-116 -112 14
-141 -90 -20
-157 -59 -54
-165 -19 -80
-161 23 -104
-145 73 -124
-117 119 -136
-81 159 -138
-32 196 -131
19 221 -115
66 219 -90
132 121 24
70 -112 46
112 95 -21
85 -70 41
102 -79 51
112 -33 64'''
def dot(a,b):return sum(x*y for x,y in zip(a,b))
def sub(a,b):return tuple(x-y for x,y in zip(a,b))
def add(a,b):return tuple(x+y for x,y in zip(a,b))
def mul(t,a):return tuple(t*x for x in a)
def cross(a,b):return (a[1]*b[2]-a[2]*b[1],a[2]*b[0]-a[0]*b[2],a[0]*b[1]-a[1]*b[0])
def det(a,b,c):return dot(a,cross(b,c))
def primitive(v):
 d=lcm(*(x.denominator for x in v));w=[int(x*d)for x in v];g=0
 for x in w:g=gcd(g,abs(x))
 assert g
 return tuple(x//g for x in w)
def polygon(ids,P,n):
 drop=max(range(3),key=lambda k:abs(n[k]));axes=[k for k in range(3)if k!=drop]
 ids=sorted(ids,key=lambda i:(P[i][axes[0]],P[i][axes[1]]))
 def orient(i,j,k):
  a,b,c=[(P[t][axes[0]],P[t][axes[1]])for t in(i,j,k)]
  return (b[0]-a[0])*(c[1]-a[1])-(b[1]-a[1])*(c[0]-a[0])
 lo=[];hi=[]
 for i in ids:
  while len(lo)>1 and orient(lo[-2],lo[-1],i)<=0:lo.pop()
  lo.append(i)
 for i in reversed(ids):
  while len(hi)>1 and orient(hi[-2],hi[-1],i)<=0:hi.pop()
  hi.append(i)
 out=lo[:-1]+hi[:-1];assert len(out)>=3
 if dot(cross(sub(P[out[1]],P[out[0]]),sub(P[out[2]],P[out[0]])),n)<0:out.reverse()
 return out

def audit(P):
 P=[tuple(map(Q,p))for p in P];assert len(set(P))==len(P)
 planes={}
 for i,j,k in combinations(range(len(P)),3):
  n=cross(sub(P[j],P[i]),sub(P[k],P[i]))
  if n==(0,0,0):continue
  h=dot(n,P[i]);sg=[dot(n,x)-h for x in P]
  if max(sg)<=0:pass
  elif min(sg)>=0:n=mul(-1,n);h=-h
  else:continue
  key=primitive((*n,h));planes[key]=[r for r,x in enumerate(P)if dot(key[:3],x)==key[3]]
 faces=[(pl,polygon(ids,P,pl[:3]))for pl,ids in sorted(planes.items())]
 V=sorted({i for _,f in faces for i in f});edges={}
 for fi,(_,f)in enumerate(faces):
  for i,j in zip(f,f[1:]+f[:1]):edges.setdefault(tuple(sorted((i,j))),[]).append(fi)
 assert all(len(v)==2 for v in edges.values()) and len(V)-len(edges)+len(faces)==2
 o=tuple(sum(P[i][k]for i in V)/len(V)for k in range(3))
 vol=Q(0);mom=[Q(0)]*3
 for pl,f in faces:
  assert dot(pl[:3],o)<pl[3]
  for j in range(1,len(f)-1):
   a,b,c=[P[t]for t in(f[0],f[j],f[j+1])]
   dv=det(sub(a,o),sub(b,o),sub(c,o))/6;assert dv>0
   vol+=dv
   for k in range(3):mom[k]+=dv*(o[k]+a[k]+b[k]+c[k])/4
 g=tuple(x/vol for x in mom);X=[sub(x,g)for x in P]
 S=[];WS=[];U=[];WU=[];H=[];WH=[]
 for fi,(pl,f)in enumerate(faces):
  n=pl[:3];h=Q(pl[3])-dot(n,g);assert h>0
  foot=mul(h/dot(n,n),n)
  vals=[dot(cross(sub(X[j],X[i]),sub(foot,X[i])),n)for i,j in zip(f,f[1:]+f[:1])]
  if min(vals)>0:S.append(fi)
  elif min(vals)>=0:WS.append(fi)
 for i in V:
  vals=[dot(X[i],sub(X[i],X[j]))for j in V if j!=i]
  if min(vals)>0:U.append(i)
  elif min(vals)>=0:WU.append(i)
 for (i,j),owners in sorted(edges.items()):
  a,b=X[i],X[j];d=sub(b,a);dd=dot(d,d);t=-dot(a,d)/dd
  n1=faces[owners[0]][0][:3];n2=faces[owners[1]][0][:3]
  y=add(a,mul(t,d));A=dot(n1,n1);B=dot(n1,n2);C=dot(n2,n2);D=A*C-B*B;assert D>0
  lam=(C*dot(y,n1)-B*dot(y,n2))/D;mu=(A*dot(y,n2)-B*dot(y,n1))/D
  assert y==add(mul(lam,n1),mul(mu,n2))
  vals=[t,1-t,lam,mu]
  if min(vals)>0:H.append([i,j])
  elif min(vals)>=0:WH.append([i,j])
 v2=Q(0);m2=[Q(0)]*3;nt=0
 for _,f in faces:
  for j in range(1,len(f)-1):
   a,b,c=[X[t]for t in(f[0],f[j],f[j+1])]
   dv=det(a,b,c)/6;assert dv>0
   v2+=dv;nt+=1
   for k in range(3):m2[k]+=dv*(a[k]+b[k]+c[k])/4
 assert v2==vol and m2==[0,0,0]
 D=lcm(*(z.denominator for i in V for z in X[i]));N=max(abs(int(z*D))for i in V for z in X[i])
 return {'V':len(V),'E':len(edges),'F':len(faces),'C':2*len(edges),'strict':[len(S),len(U),len(H)],'weak':[len(WS),len(WU),len(WH)],'volume':str(vol),'centroid':list(map(str,g)),'centered_bits':[D.bit_length(),N.bit_length()],'input_vertex_indices':V,'stable_face_indices':S,'stable_owner_sets':[sorted(faces[i][1])for i in S],'unstable_input_indices':U,'saddle_input_pairs':H,'maximal_faces':[f for _,f in faces],'support_planes':[pl for pl,f in faces],'true_edges':[list(e)for e in sorted(edges)],'positive_centered_tetrahedra':nt,'points':[[str(x)for x in p]for p in P]}
def main():
 if len(sys.argv)>1:P=json.loads(Path(sys.argv[1]).read_text());P=P.get('points',P)if isinstance(P,dict)else P
 else:P=[tuple(Q(int(x),100)for x in s.split())for s in ROWS.splitlines()]
 report=audit(P)
 if len(sys.argv)==1:
  assert report['volume']=='4152473/1500000'
  assert report['centroid']==['101311319/830494600','520540313/6643956800','-77026377/3321978400']
  assert report['strict']==[2,1,1] and report['weak']==[0,0,0]
  assert report['centered_bits']==[33,34]
 print(json.dumps(report,sort_keys=True,separators=(',',':')))
if __name__=='__main__':main()
```
