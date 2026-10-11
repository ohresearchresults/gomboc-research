# material-01ae82d072d3

Historical AI scientific source/proof material. Statements retain their original scope; this is not an independently reviewed theorem.

Public derivative: internal-record-identifiers-replaced.

---

# Recovery capsule part 1/2: CF82_TWO_CONNECTED_AFFINE_COMPONENTS

This is a NEW exact family-specific exclusion, not a new body or global obstruction. Literal sources CF82_RESERVE42_G5 and CF82_MAIN83_G7 were recovered from fully read material [internal-source-reference]. Fully read worker result figure-0448 (SHA09fef117a07ec2d50084a6f580fff03a7aa84487df0cbe4df116534f4d44742a) independently contains complete recovery of the unchanged input bodies. The previous connected-affine exclusion in [internal-source-reference] applied ONLY to SF90_CANCEL14_G5. This capsule newly proves the corresponding statement for the two different CF82 bodies, not by aliasing the SF90 result.

Both mandatory parts have object identity CF82_TWO_CONNECTED_AFFINE_COMPONENTS. Part1 contains the complete verifier. Part2 contains the complete literal points, oriented maximal faces, escape trees and 24 exact LP bases. No old sandbox, original input material, SciPy or numerical producer is needed for verification after both parts have been saved.

Save the Python block as VERIFY_AFFINE_CF82.py and the part2 JSON block as AFFINE_CF82_DATA.json, preserving the final newline of each block. Run python -B -S VERIFY_AFFINE_CF82.py in their directory. Executed CPython3.13.5, standard library only. Input verifier9099bytes SHA5365a92d0d6db4ab5e6fc25ec79254943e10fdf0da9a9e463d8ab3d717fbbb7a; data7352bytes SHA60913fb5964ab5f86537760ede7e77f112f2b959420070bc5ba282f5a951cfdf. Output AFFINE_CF82_CERTIFICATES.json818216bytes SHA6183ce0710507062013feb33ae2462059c269a94d26b3114411879e75d7a5c17.

Expected markers:
CF82_NEW_AFFINE_COMPONENT_EXACT_PASS CF82_MAIN83_G7.json 13 386 13
CF82_NEW_AFFINE_COMPONENT_EXACT_PASS CF82_RESERVE42_G5.json 14 195 4
CF82_TWO_CONNECTED_AFFINE_U1_WEAK000_COMPONENTS_EXCLUDE_S1_PASS 818216 6183ce0710507062013feb33ae2462059c269a94d26b3114411879e75d7a5c17

## Mathematical interpretation
At each exact actual filled centroid write physical escape forms x_i^T G(x_j-x_i), for trace-three real symmetric G. Twelve exact Farkas bounds per body use five core rows plus trace; the union has13 core arrows for MAIN83 and14 for RESERVE42. The closed core cone forces ||G-I||_2 <= rho, with exact rho approximately0.005281693129367282 and0.007038270136339412 respectively. Hence G is automatically SPD and ||sqrt(G)-I||_2<rho. Both exact circumradii are<2, so the own-centred Hausdorff displacement after canonical similarity alignment is<2rho<1/50. The verifier reconstructs the complete positive polar bar, its attaining path and complete separating cut, and proves eta=(1/sqrt(death)-1/sqrt(birth))/2>1/50. Support-persistence therefore gives S>=2 throughout each closed cone.

Every non-tree outgoing edge at a core vertex and every outgoing root0 edge is strictly negative throughout the corresponding cone, certified by rational interval bounds on the six Gram entries. Therefore a continuous invertible affine path starting at either parent and retaining own strict U1/additionalweak000 cannot leave the cone: first exit makes a core vertex weak-unstable while input0 remains strictly unstable. These connected components contain no own110. Arbitrary rotations/scalings are absorbed by the Gram normalization and polar decomposition; own mass transforms affinely. This does NOT exclude disconnected affine U1 components, finite jumps, affine paths with extra equilibria, nonlinear point/support/mass changes, or CF82_COHERENT_C474_G7. Source face indices here are lexicographically sorted vertex triples, not the old primitive-plane ordering: MAIN83 S[46,123], RESERVE42 S[6,78]. No exact bodies or old indices are renamed.

The verifier checks all global supports, maximal triangular faces, true edges, connected sphere and vertex links; integrates exact actual volume/centroid by tetrahedra and distinct coordinate-boundary identities; performs a complete strict/weak/primitive-zero census; and verifies every rational LP dual and attaining vertex. This is a new proof computation with one mechanics implementation, not an independent second mechanics auditor.

## Complete verifier
```python
"""Exact connected-affine U1/weak000 exclusions for two literal CF82 bodies.
Standard library only. Run: python -B -S VERIFY_AFFINE_CF82.py
All supporting faces are verified, not trusted as a floating hull. No optimizer
or numerical eigensolver occurs in this certificate verification.
"""
from pathlib import Path
from fractions import Fraction as F
from itertools import combinations
from collections import deque
import json,hashlib
ROOT=Path(__file__).resolve().parent

def dot(a,b):return sum(x*y for x,y in zip(a,b))
def sub(a,b):return tuple(x-y for x,y in zip(a,b))
def mul(a,t):return tuple(x*t for x in a)
def add(a,b):return tuple(x+y for x,y in zip(a,b))
def cross(a,b):return(a[1]*b[2]-a[2]*b[1],a[2]*b[0]-a[0]*b[2],a[0]*b[1]-a[1]*b[0])
def coeff(x,d):return[x[0]*d[0],x[1]*d[1],x[2]*d[2],x[0]*d[1]+x[1]*d[0],x[0]*d[2]+x[2]*d[0],x[1]*d[2]+x[2]*d[1]]
def encode(x):
 if isinstance(x,F):return str(x)
 if isinstance(x,dict):return {str(k):encode(v) for k,v in x.items()}
 if isinstance(x,(tuple,list)):return list(map(encode,x))
 return x

def solve(A,b):
 A=[list(map(F,row))+[F(v)] for row,v in zip(A,b)];n=len(b)
 for k in range(n):
  r=next(i for i in range(k,n) if A[i][k]);A[k],A[r]=A[r],A[k]
  z=A[k][k];A[k]=[x/z for x in A[k]]
  for i in range(n):
   if i!=k:
    z=A[i][k];A[i]=[x-z*y for x,y in zip(A[i],A[k])]
 return [row[-1] for row in A]

def geometry(d,tri):
 p=list(map(tuple,d['points']));grid=d['grid'];assert grid>0 and len(p)==len(set(p))
 owners={};faces=[]
 for a,b,c in tri:
  assert len({a,b,c})==3 and all(0<=i<len(p) for i in (a,b,c))
  n=cross(sub(p[b],p[a]),sub(p[c],p[a]));h=dot(n,p[a]);assert n!=(0,0,0)
  signs=[dot(n,v)-h for v in p]
  assert max(signs)==0 and [i for i,s in enumerate(signs) if s==0]==sorted((a,b,c))
  faces.append((n,h))
  for i,j in ((a,b),(b,c),(c,a)):owners.setdefault(tuple(sorted((i,j))),[]).append(len(faces)-1)
 assert len({tuple(sorted(f)) for f in tri})==len(tri) and all(len(o)==2 for o in owners.values())
 verts=sorted({i for e in owners for i in e});assert len(verts)-len(owners)+len(tri)==2
 adj={i:set() for i in verts}
 for i,j in owners:adj[i].add(j);adj[j].add(i)
 def connected(A):
  seen={next(iter(A))};todo=list(seen)
  while todo:
   for j in A[todo.pop()]-seen:seen.add(j);todo.append(j)
  return len(seen)==len(A)
 assert connected(adj)
 for i in verts:
  link={j:set() for j in adj[i]}
  for f in tri:
   if i in f:
    a,b=[j for j in f if j!=i];link[a].add(b);link[b].add(a)
  assert all(len(v)==2 for v in link.values()) and connected(link)
 D=sum(dot(p[a],cross(p[b],p[c])) for a,b,c in tri);assert D>0
 N=tuple(sum(dot(p[a],cross(p[b],p[c]))*(p[a][k]+p[b][k]+p[c][k]) for a,b,c in tri) for k in range(3))
 volume=F(D,6*grid**3);centroid=tuple(F(v,4*D*grid) for v in N)
 # Different coordinate-boundary integrals for all three volume/moment coordinates.
 for k in range(3):
  vol=F(0);moment=F(0)
  for a,b,c in tri:
   z=cross(sub(p[b],p[a]),sub(p[c],p[a]))[k];v=[p[a][k],p[b][k],p[c][k]]
   vol+=F(z*sum(v),6*grid**3);moment+=F(z*(sum(v)**2+sum(t*t for t in v)),48*grid**4)
  assert vol==volume and moment==volume*centroid[k]
 X={i:sub(tuple(F(t,grid) for t in p[i]),centroid) for i in verts}
 support=[F(h,grid)-dot(n,centroid) for n,h in faces];assert min(support)>0
 Q={i:mul(n,1/support[i]) for i,(n,h) in enumerate(faces)}
 strict=[[],[],[]];weak=[[],[],[]];zeros=[0,0,0]
 for i,(n,h) in enumerate(faces):
  vals=[support[j]*dot(n,n)-support[i]*dot(nn,n) for j,(nn,hh) in enumerate(faces) if j!=i]
  zeros[0]+=sum(v==0 for v in vals)
  if min(vals)>0:strict[0].append(i)
  elif min(vals)>=0:weak[0].append(i)
 for i in verts:
  vals=[dot(X[i],sub(X[j],X[i])) for j in adj[i]];zeros[1]+=sum(v==0 for v in vals)
  if max(vals)<0:strict[1].append(i)
  elif max(vals)<=0:weak[1].append(i)
 for (a,b),(f,g) in sorted(owners.items()):
  e=sub(X[b],X[a]);dd=dot(e,e);t=-dot(X[a],e);w=add(mul(X[a],dd),mul(e,t));n,m=faces[f][0],faces[g][0]
  aa,bb,ab=dot(n,n),dot(m,m),dot(n,m);assert aa*bb>ab*ab
  vals=[t,dd-t,dot(w,n)*bb-dot(w,m)*ab,dot(w,m)*aa-dot(w,n)*ab];zeros[2]+=sum(v==0 for v in vals)
  if min(vals)>0:strict[2].append([a,b])
  elif min(vals)>=0:weak[2].append([a,b])
 return dict(X=X,Q=Q,adj=adj,owners=owners,volume=volume,centroid=centroid,strict=strict,weak=weak,primitive_zeros=zeros)

def bars(points,edges):
 radius={i:dot(x,x) for i,x in points.items()};parent={i:i for i in points};adj={i:[] for i in points};events=[]
 for i,j in sorted(edges):
  v=sub(points[j],points[i]);dd=dot(v,v);assert dd>0;t=min(F(1),max(F(0),-dot(points[i],v)/dd));w=add(points[i],mul(v,t));h=dot(w,w)
  assert h<=min(radius[i],radius[j]);events.append((h,i,j));adj[i].append((j,h));adj[j].append((i,h))
 def find(i):
  while parent[i]!=i:parent[i]=parent[parent[i]];i=parent[i]
  return i
 result=[]
 for h,i,j in sorted(events,reverse=True):
  a,b=find(i),find(j)
  if a==b:continue
  if (radius[a],-a)<(radius[b],-b):a,b=b,a
  if radius[b]>h:
   comp={b};todo=[b]
   while todo:
    k=todo.pop()
    for v,hh in adj[k]:
     if hh>h and v not in comp:comp.add(v);todo.append(v)
   assert a not in comp
   boundary=sorted((u,v,hh) for u in comp for v,hh in adj[u] if v not in comp);assert boundary and all(hh<=h for u,v,hh in boundary)
   pred={b:None};todo=deque([b])
   while todo and a not in pred:
    k=todo.popleft()
    for v,hh in sorted(adj[k]):
     if hh>=h and v not in pred:pred[v]=k;todo.append(v)
   assert a in pred
   path=[a]
   while path[-1]!=b:path.append(pred[path[-1]])
   path.reverse();assert min(next(hh for v,hh in adj[u] if v==w) for u,w in zip(path,path[1:]))==h
   result.append(dict(peak=b,elder=a,birth=radius[b],death=h,component=sorted(comp),boundary=boundary,path=path))
  parent[b]=a
 roots=sorted(i for i,p in points.items() if all(dot(p,sub(points[j],p))<0 for j,h in adj[i]));assert len(result)==len(roots)-1
 return roots,result

def support_test(e,b,d):
 z=1/d-1/b-4*e*e;return z>0 and z*z>16*e*e/b

def verify(name,data):
 raw=json.dumps(data['body'],separators=(',',':')).encode();assert hashlib.sha256(raw).hexdigest()==data['input_sha256']
 M=geometry(data['body'],data['faces']);X=M['X'];assert list(map(len,M['strict']))==[2,1,1] and M['strict'][1]==[0] and not any(M['weak']) and M['primitive_zeros']==[0,0,0]
 tree=list(map(tuple,data['tree']));assert len(tree)==len(X)-1 and {i for i,j in tree}==set(X)-{0}
 C=[coeff(X[i],sub(X[j],X[i])) for i,j in tree];tr=[F(1)]*3+[F(0)]*3;eye=tr
 for (i,j),row in zip(tree,C):assert j in M['adj'][i] and dot(row,eye)>0
 core=sorted(set(i for basis in data['bases'] for i in basis));certs=[];bounds=[]
 for k in range(6):
  values=[]
  for side,sign in enumerate((1,-1)):
   ids=data['bases'][2*k+side];assert len(ids)==5 and len(set(ids))==5
   B=[C[i] for i in ids]+[tr];c=[F(0)]*6;c[k]=F(sign);v=solve(B,[0]*5+[3]);y=solve(list(map(list,zip(*B))),c)
   assert min(y[:5])>=0 and dot(tr,v)==3 and all(dot(row,v)>=0 for row in C)
   assert all(sum(y[j]*B[j][i] for j in range(6))==c[i] for i in range(6)) and dot(c,v)==3*y[-1]
   values.append(v[k]);certs.append(dict(coordinate=k,sign=sign,basis=ids,dual=y,attaining_vertex=v,bound=v[k]))
  bounds.append(values)
 delta=[max(abs(lo-(k<3)),abs(hi-(k<3))) for k,(lo,hi) in enumerate(bounds)]
 rho=max(delta[0]+delta[3]+delta[4],delta[1]+delta[3]+delta[5],delta[2]+delta[4]+delta[5]);assert rho<F(1,100)
 R2=max(dot(x,x) for x in X.values());assert R2<4
 # ||G-I||2 <= rho < .01; G is SPD. ||sqrt(G)-I||2 < rho.
 # Match centered vertices and all convex combinations: d_H(K,sqrt(G)K)<2*rho<.02.
 qr,qbars=bars(M['Q'],list(map(tuple,M['owners'].values())));assert qr==M['strict'][0] and len(qbars)==1
 qb=qbars[0];assert support_test(F(1,50),qb['birth'],qb['death'])
 excluded=[];unexcluded=[]
 for i in X:
  for j in sorted(M['adj'][i]):
   if (i,j) in tree:continue
   row=coeff(X[i],sub(X[j],X[i]));upper=sum(c*b[int(c>=0)] for c,b in zip(row,bounds));rec=dict(arrow=[i,j],upper=upper)
   (excluded if upper<0 else unexcluded).append(rec)
 corevertices={tree[i][0] for i in core};bad={tuple(r['arrow']) for r in unexcluded}
 assert not any(i in corevertices or i==0 for i,j in bad)
 report=dict(input_sha256=data['input_sha256'],V=len(X),E=len(M['owners']),F=len(M['Q']),centroid=M['centroid'],volume=M['volume'],strict=M['strict'],weak=M['weak'],primitive_zeros=M['primitive_zeros'],core_indices=core,core_arrows=[tree[i] for i in core],certificates=certs,bounds=bounds,rho=rho,R2=R2,Hausdorff_strict_bound=2*rho,protected_support_radius=F(1,50),polar_bar=qb,excluded=excluded,unexcluded=unexcluded)
 print('CF82_NEW_AFFINE_COMPONENT_EXACT_PASS',name,len(core),len(excluded),len(unexcluded),flush=True)
 return report

def main():
 raw=(ROOT/'AFFINE_CF82_DATA.json').read_bytes();data=json.loads(raw);out={name:verify(name,d) for name,d in sorted(data.items())}
 payload=(json.dumps(encode(out),sort_keys=True,separators=(',',':'))+'\n').encode();(ROOT/'AFFINE_CF82_CERTIFICATES.json').write_bytes(payload)
 print('CF82_TWO_CONNECTED_AFFINE_U1_WEAK000_COMPONENTS_EXCLUDE_S1_PASS',len(payload),hashlib.sha256(payload).hexdigest(),flush=True)
if __name__=='__main__':main()
```
