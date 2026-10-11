# material-2edfa4c61978

Historical AI scientific source/proof material. Statements retain their original scope; this is not an independently reviewed theorem.

Public derivative: internal-record-identifiers-replaced.

---

# TRIANGULAR_H_DIVERGENCE_EXACT_B_V1

Complete independent exact auditor for rational V-inputs with triangular maximal facets. An A report supplies only an untrusted H proposal. B proves boundedness by exhaustive recession-ray rejection; reconstructs every feasible plane-triple vertex; proves H=conv(input points) from both inclusions; rebuilds maximal facets and true edges; computes ordinary filled mass by coordinatewise divergence of (x_k^2/2)e_k; repeats centered divergence integration; and enumerates strict/weak S,U,H. The saddle test uses cross-product wedges rather than A's Gram-system coefficients. This is not a generic polygon-facet implementation: nontriangular facets are deliberately rejected. It has no floating-point dependency.

Save the following exact source, including final newline, as VERIFY_H_B.py. CPython3.13.5 standard library, assertions enabled. Source5167bytes SHA256 c8069c3bd1e43399dde7c2e487aa559d150cb356970e684218757bf160665d56. Command `python -B -S VERIFY_H_B.py INPUT_A.json > OUTPUT_B.json`. Successful exit0 means all exact gates and comparisons passed. The complete rational A implementation and its small input parser are preserved separately in [internal-source-reference] (EXACT_POINTS.py5247bytes SHAa120fc81b941666aa6b2fc78857c0a8a6b63e62732939a8e68bab2b6c78b8f6b).

Observed applications to newly rounded C126_WIDE bodies: grids1000,10000,100000,1000000 all V23/E63/F42, weak000, strict respectively (4,13,15),(4,9,11),(4,1,3),(4,1,3). They are nonwinners, not replacements for canonical C622. The exact inputs and output identities are in the separate C126_WIDE_FOUR_GRIDS recovery material. B outputs respectively578bytes SHA74106701c0b20c111df9bfb50f366f835a0349ec206e4df7fcf0c153d71a4343;577bytes SHAb28d7f4b599eefb3603f878a67d7edd0ceecf1caff963099bf3d3a073384f62f;513bytes SHAfebdbba6154abbbef10be1ebdba27947aef7e2016b449f06b133862b5a098b78;548bytes SHA15bf4c0c7ddb157f6c44993a71300a24044e3b19ba46c4de4b993510048d0023.

```python
#!/usr/bin/env python3
"""Independent exact H-hull/divergence-mass/wedge audit for triangular facets.
Reads an untrusted A report as a proposal, proves bounded H=conv(input points),
then computes all features and mass by different formulas. Standard library only.
The no-recession-ray test is exhaustive because the normals span R^3: their
recession cone is pointed, and any nonzero pointed cone has an extreme ray,
which in R^3 is contained in two independent active boundary planes.
"""
from fractions import Fraction as F
from itertools import combinations
from math import lcm
import json,sys
from pathlib import Path
assert __debug__
def d(a,b):return sum(x*y for x,y in zip(a,b))
def sub(a,b):return tuple(x-y for x,y in zip(a,b))
def cr(a,b):return (a[1]*b[2]-a[2]*b[1],a[2]*b[0]-a[0]*b[2],a[0]*b[1]-a[1]*b[0])
def det(a,b,c):return d(a,cr(b,c))
def audit(proposal):
 P=[tuple(map(F,row))for row in proposal['points']];H=[tuple(map(int,row))for row in proposal['support_planes']];N=[p[:3]for p in H];h=[p[3]for p in H]
 assert len(set(P))==len(P) and len(set(H))==len(H)
 assert any(det(*rows)for rows in combinations(N,3))
 assert all(d(n,p)<=b for n,b in zip(N,h)for p in P)
 anchor=tuple(sum(p[k]for p in P)/len(P)for k in range(3));assert all(d(n,anchor)<b for n,b in zip(N,h))
 # All nonzero candidate recession rays in both orientations are rejected.
 raytests=0
 for a,b in combinations(N,2):
  v=cr(a,b)
  if v==(0,0,0):continue
  vals=[d(n,v)for n in N];assert min(vals)<0<max(vals);raytests+=2
 # Full exact plane-triple enumeration, using integer numerators in feasibility.
 vertices=set();triples=0
 for i,j,k in combinations(range(len(H)),3):
  a,b,c=N[i],N[j],N[k];D=det(a,b,c)
  if D==0:continue
  ab,bc,ca=cr(a,b),cr(b,c),cr(c,a)
  v=tuple(h[i]*bc[t]+h[j]*ca[t]+h[k]*ab[t]for t in range(3))
  if D<0:D=-D;v=tuple(-x for x in v)
  triples+=1
  if all(d(n,v)<=bb*D for n,bb in zip(N,h)):vertices.add(tuple(F(x,D)for x in v))
 assert vertices and vertices.issubset(set(P))
 V=sorted(vertices);index={p:i for i,p in enumerate(P)};faces=[]
 # Every proposed support has exactly three vertices, thus is a genuine facet.
 for n,b in zip(N,h):
  f=[p for p in V if d(n,p)==b];assert len(f)==3
  if d(cr(sub(f[1],f[0]),sub(f[2],f[0])),n)<0:f[1],f[2]=f[2],f[1]
  assert d(cr(sub(f[1],f[0]),sub(f[2],f[0])),n)>0;faces.append(f)
 # Bounded H has exactly the enumerated vertices. Since all lie in P and P is
 # feasible, H=conv(P); no untrusted hull topology or completeness remains.
 edges={}
 for fi,f in enumerate(faces):
  for a,b in zip(f,f[1:]+f[:1]):edges.setdefault(tuple(sorted((index[a],index[b]))),[]).append(fi)
 assert all(len(v)==2 for v in edges.values()) and len(V)-len(edges)+len(faces)==2
 def integrate(ff):
  volume=F(0);moment=[F(0)]*3
  for a,b,c in ff:
   area2=cr(sub(b,a),sub(c,a));volume+=d(a,area2)/6
   # Divergence of (x_k^2/2)e_k is x_k; exact triangular square integration.
   for k in range(3):
    q=a[k]*a[k]+b[k]*b[k]+c[k]*c[k]+a[k]*b[k]+a[k]*c[k]+b[k]*c[k]
    moment[k]+=area2[k]*q/24
  return volume,moment
 volume,moment=integrate(faces);assert volume>0;g=tuple(q/volume for q in moment);X=[sub(p,g)for p in P]
 cf=[[sub(p,g)for p in f]for f in faces];v2,m2=integrate(cf)
 assert v2==volume and m2==[0,0,0] and all(det(*f)>0 for f in cf)
 heights=[F(b)-d(n,g)for n,b in zip(N,h)];assert min(heights)>0
 S=[];WS=[];U=[];WU=[];E=[];WE=[]
 for i,(n,b)in enumerate(zip(N,heights)):
  nn=d(n,n);sl=[heights[j]*nn-b*d(N[j],n)for j in range(len(H))if j!=i]
  if min(sl)>0:S.append(sorted(index[p]for p in faces[i]))
  elif min(sl)>=0:WS.append(i)
 for p in V:
  i=index[p];x=X[i];xx=d(x,x)
  # Sphere with diameter 0--2x: all other vertices must lie strictly inside.
  gaps=[xx+d(sub(X[index[q]],x),sub(X[index[q]],x))-d(X[index[q]],X[index[q]])for q in V if q!=p]
  if min(gaps)>0:U.append(i)
  elif min(gaps)>=0:WU.append(i)
 for (i,j),(f1,f2)in sorted(edges.items()):
  a=X[i];v=sub(X[j],a);dd=d(v,v);t=-d(a,v);z=tuple(dd*a[k]+t*v[k]for k in range(3))
  n,m=N[f1],N[f2];w=cr(n,m);assert w!=(0,0,0)
  tests=[t,dd-t,d(cr(z,m),w),d(cr(n,z),w)]
  if min(tests)>0:E.append([i,j])
  elif min(tests)>=0:WE.append([i,j])
 D=lcm(*(z.denominator for p in V for z in X[index[p]]));num=max(abs(int(z*D))for p in V for z in X[index[p]])
 r={'V':len(V),'E':len(edges),'F':len(faces),'C':2*len(edges),'strict':[len(S),len(U),len(E)],'weak':[len(WS),len(WU),len(WE)],'volume':str(volume),'centroid':list(map(str,g)),'centered_bits':[D.bit_length(),num.bit_length()],'stable_owner_sets':sorted(S),'unstable_input_indices':sorted(U),'saddle_input_pairs':E,'positive_centered_tetrahedra':len(cf),'full_rank_triples_tested':triples,'nonzero_recession_orientations_rejected':raytests}
 for key in ['V','E','F','C','strict','weak','volume','centroid','centered_bits','positive_centered_tetrahedra']:
  assert r[key]==proposal[key],(key,r[key],proposal[key])
 for key in ['stable_owner_sets','unstable_input_indices','saddle_input_pairs']:
  assert sorted(r[key])==sorted(proposal[key]),key
 return r
if __name__=='__main__':
 report=audit(json.loads(Path(sys.argv[1]).read_text()));print(json.dumps(report,sort_keys=True,separators=(',',':')))
```
