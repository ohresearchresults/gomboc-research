# material-abf83a6ac786

Historical AI scientific source/proof material. Statements retain their original scope; this is not an independently reviewed theorem.

---

"""Exact rational protection certificate for 27 deterministic CF82 nominations.
Dependencies: SELECTIVE_REPLAY.py and its 27 generated JSON outputs. NumPy/SciPy
only nominate triangles; every used support sign, closed mesh, mass equality,
polar bar and radius bound is checked with integers/Fraction. No own110 claim.
Run: OPENBLAS_NUM_THREADS=1 python SELECTIVE_PROTECTION.py DIRECTORY
DIRECTORY contains SELECTIVE_REPLAY.py and its generated outputs.
"""
import ast,hashlib,itertools,json,math,sys
from fractions import Fraction as F
from pathlib import Path
import numpy as np
from scipy.spatial import ConvexHull

def dot(a,b):return sum(x*y for x,y in zip(a,b))
def sub(a,b):return tuple(x-y for x,y in zip(a,b))
def cross(a,b):return(a[1]*b[2]-a[2]*b[1],a[2]*b[0]-a[0]*b[2],a[0]*b[1]-a[1]*b[0])
def det(a,b,c):return dot(a,cross(b,c))
def enc(x):
 if isinstance(x,F):return str(x)
 if isinstance(x,dict):return {str(k):enc(v) for k,v in x.items()}
 if isinstance(x,(tuple,list)):return [enc(v) for v in x]
 return x

def exact_mesh(P):
 """Verify a supporting triangular sphere before using its exact filled mass."""
 scale=math.lcm(*(v.denominator for p in P for v in p));I=[tuple(int(v*scale) for v in p) for p in P]
 H=ConvexHull(np.array(P,dtype=float));tri=[];norm=[];planes=[]
 for tt in H.simplices:
  a,b,c=map(int,tt);n=cross(sub(I[b],I[a]),sub(I[c],I[a]));h=dot(n,I[a]);ss=[dot(n,p)-h for p in I]
  if min(ss)>=0:b,c=c,b;n=tuple(-x for x in n);h=-h;ss=[-x for x in ss]
  assert max(ss)==0 and min(ss)<0 and n!=(0,0,0)
  # Tested meshes are simplicial exactly; no approximate coplanar merging.
  assert [i for i,s in enumerate(ss) if s==0]==sorted([a,b,c])
  tri.append((a,b,c));norm.append(n);planes.append((n,F(h,scale)))
 own={}
 for f,(a,b,c) in enumerate(tri):
  for i,j in [(a,b),(b,c),(c,a)]:own.setdefault(tuple(sorted((i,j))),[]).append((f,i,j))
 assert all(len(o)==2 and o[0][1:]==o[1][1:][::-1] for o in own.values())
 verts=sorted(set(itertools.chain.from_iterable(tri)));assert len(verts)-len(own)+len(tri)==2
 adj={i:set() for i in verts}
 for i,j in own:adj[i].add(j);adj[j].add(i)
 seen={verts[0]};todo=list(seen)
 while todo:
  for j in adj[todo.pop()]-seen:seen.add(j);todo.append(j)
 assert len(seen)==len(verts)
 for i in verts:
  link={j:set() for j in adj[i]}
  for t in tri:
   if i in t:
    a,b=[j for j in t if j!=i];link[a].add(b);link[b].add(a)
  assert all(len(s)==2 for s in link.values())
  seen={next(iter(link))};todo=list(seen)
  while todo:
   for j in link[todo.pop()]-seen:seen.add(j);todo.append(j)
  assert len(seen)==len(link)
 D=sum(det(I[a],I[b],I[c]) for a,b,c in tri);assert D>0
 N=tuple(sum(det(I[a],I[b],I[c])*(I[a][k]+I[b][k]+I[c][k]) for a,b,c in tri) for k in range(3))
 volume=F(D,6*scale**3);g=tuple(F(v,4*D*scale) for v in N)
 for k in range(3):
  vv=F(0);mm=F(0)
  for a,b,c in tri:
   A=cross(sub(I[b],I[a]),sub(I[c],I[a]))[k];vals=[I[a][k],I[b][k],I[c][k]]
   vv+=F(A*sum(vals),6*scale**3);mm+=F(A*(sum(vals)**2+sum(v*v for v in vals)),48*scale**4)
  assert vv==volume and mm==volume*g[k]
 Q=[]
 for n,h in planes:
  hh=h-dot(n,g);assert hh>0;Q.append(tuple(F(v)/hh for v in n))
 return dict(V=len(verts),E=len(own),F=len(tri),volume=volume,g=g,Q=Q,QE=[(o[0][0],o[1][0]) for o in own.values()])

def exact_bars(Q,E):
 R=[dot(q,q) for q in Q];events=[];adj=[[] for _ in Q]
 for i,j in E:
  d=sub(Q[j],Q[i]);dd=dot(d,d);assert dd>0;t=min(F(1),max(F(0),-dot(Q[i],d)/dd))
  v=tuple(x+t*y for x,y in zip(Q[i],d));h=dot(v,v);events.append((h,i,j));adj[i].append((j,h));adj[j].append((i,h))
 pa=list(range(len(Q)))
 def find(i):
  while pa[i]!=i:pa[i]=pa[pa[i]];i=pa[i]
  return i
 bars=[]
 for h,i,j in sorted(events,reverse=True):
  a,b=find(i),find(j)
  if a==b:continue
  if (R[a],-a)<(R[b],-b):a,b=b,a
  if R[b]>h:
   component={b};todo=[b]
   while todo:
    for v,hh in adj[todo.pop()]:
     if hh>h and v not in component:component.add(v);todo.append(v)
   assert a not in component
   cut=sorted((u,v) for u in component for v,hh in adj[u] if v not in component)
   assert cut and all(hh<=h for u in component for v,hh in adj[u] if v not in component)
   bars.append(dict(peak=b,elder=a,birth=R[b],death=h,component=sorted(component),boundary=cut))
  pa[b]=a
 return bars

def main():
 root=Path(sys.argv[1]);source=(root/'SELECTIVE_REPLAY.py').read_bytes()
 assert len(source)==18425 and hashlib.sha256(source).hexdigest()=='d32187b109f69171a8b5fd6ccda3942859b06f5be0f16baa6fca1f27df59d2c4'
 tree=ast.parse(source);s=next(ast.literal_eval(n.value) for n in tree.body if isinstance(n,ast.Assign) and any(isinstance(t,ast.Name) and t.id=='DATA' for t in n.targets))
 data=json.loads(s);grid=10**7;kp=[[round(F(v)*grid) for v in p] for p in data['points']]
 raw=json.dumps(dict(grid=grid,points=kp),separators=(',',':')).encode()
 assert len(raw)==2315 and hashlib.sha256(raw).hexdigest()=='1d63a06ee4e9c0d39d258f1016dbc6ded1b141b5394af12e33f9ef959265b95a'
 K=[tuple(F(v,grid) for v in p) for p in kp];km=exact_mesh(K);bars=exact_bars(km['Q'],km['QE']);assert len(bars)==1
 b,d=bars[0]['birth'],bars[0]['death'];eps=F(37,500);q=1/d-1/b-4*eps**2
 assert q>0 and q*q>16*eps**2/b
 # eta(K)=(1/sqrt(d)-1/sqrt(b))/2 > 37/500 = .074.
 results=[]
 for mode,count,factor in itertools.product(['angle','tight','bulge'],[8,16,23],[.5,1.,1.5]):
  name=f'SELECTIVE_{mode}_{count}_{factor}.json';raw=(root/name).read_bytes();z=json.loads(raw)
  P=[tuple(F(v) for v in p) for p in z['points']];pm=exact_mesh(P)
  refs=K+[tuple((K[i][k]+K[j][k])/2 for k in range(3)) for i,j in z['settings']['edges']]
  assert len(P)==len(refs)
  point2=max(dot(sub(p,r),sub(p,r)) for p,r in zip(P,refs));dg=sub(pm['g'],km['g']);cg2=dot(dg,dg)
  assert point2<F(27,1000)**2 and cg2<F(3,2000)**2
  results.append(dict(file=name,bytes=len(raw),sha256=hashlib.sha256(raw).hexdigest(),V=pm['V'],E=pm['E'],F=pm['F'],point_max_sq=point2,centroid_displacement_sq=cg2))
  print('SELECTIVE_EXACT_PROTECTED',name,pm['V'],pm['E'],flush=True)
 report=dict(parent='CF82_MAIN83_G7',parent_counts=[km['V'],km['E'],km['F']],parent_centroid=km['g'],parent_bar=bars[0],eta_lower=eps,raw_point_upper=F(27,1000),centroid_upper=F(3,2000),centred_Hausdorff_upper=F(57,2000),remaining_protected_radius=F(91,2000),cases=results)
 raw=(json.dumps(enc(report),sort_keys=True,separators=(',',':'))+'\n').encode()
 assert len(raw)==19159 and hashlib.sha256(raw).hexdigest()=='5663f6b633c6e66957f401de3ef431143d0b6ecc88229a22ddd5ba654733f434'
 (root/'SELECTIVE_PROTECTION_REPORT.json').write_bytes(raw)
 print('CF82_SELECTIVE27_EXACT_PROTECTION_PASS',len(raw),hashlib.sha256(raw).hexdigest(),flush=True)
if __name__=='__main__':main()
