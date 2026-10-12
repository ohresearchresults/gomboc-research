"""Exact standard-library audit of a rational own-volume-centred convex polyhedron."""
import csv,gzip,json,sys,math,hashlib,time
from pathlib import Path
from collections import defaultdict,deque,Counter
from itertools import combinations

def sub(a,b):return tuple(x-y for x,y in zip(a,b))
def dot(a,b):return sum(x*y for x,y in zip(a,b))
def cross(a,b):return(a[1]*b[2]-a[2]*b[1],a[2]*b[0]-a[0]*b[2],a[0]*b[1]-a[1]*b[0])
def det(a,b,c):return dot(a,cross(b,c))
def load(path):
 with gzip.open(path,'rt',newline='') as f:return [tuple(map(int,row)) for row in csv.reader(f)]

def audit(base,allpairs=False):
 base=Path(base);st=time.time();definition=json.loads((base/'definition.json').read_text());raw=load(base/'raw_vertices.csv.gz');P=load(base/'vertices.csv.gz');F=load(base/'triangles.csv.gz');D=definition['raw_denominator'];N=len(P);T=len(F)
 assert D>0 and all(len(v)==3 for v in raw) and all(len(f)==3 and all(0<=i<N for i in f) for f in F)
 assert len(raw)==N and len(set(P))==N and all(len(p)==3 for p in P)
 vol=0;mom=[0,0,0]
 for i,j,k in F:
  a,b,c=raw[i],raw[j],raw[k];d=det(a,b,c);vol+=d
  for q in range(3):mom[q]+=d*(a[q]+b[q]+c[q])
 assert vol>0;g=math.gcd(4*vol,*mom);C=4*vol//g;M=tuple(m//g for m in mom);den=D*C
 assert C==int(definition['centroid_multiplier']) and M==tuple(map(int,definition['centroid_subtract'])) and den==int(definition['centred_denominator'])
 assert P==[tuple(C*p[j]-M[j] for j in range(3)) for p in raw]
 # Integrate centred coordinates independently, rather than trusting translation arithmetic.
 cv=0;cm=[0,0,0]
 for i,j,k in F:
  a,b,c=P[i],P[j],P[k];d=det(a,b,c);assert d>0;cv+=d
  for q in range(3):cm[q]+=d*(a[q]+b[q]+c[q])
 assert cm==[0,0,0] and cv>0 and cv==C**3*vol
 occ=defaultdict(list);links=[{} for _ in P];neighbors=[set() for _ in P];normals=[]
 assert len(set(tuple(sorted(f)) for f in F))==T
 for f,(i,j,k) in enumerate(F):
  assert len({i,j,k})==3
  n=cross(sub(raw[j],raw[i]),sub(raw[k],raw[i]));assert dot(n,n)>0;normals.append(n)
  for x,y,z in ((i,j,k),(j,k,i),(k,i,j)):
   assert y not in links[x];links[x][y]=z;neighbors[x].update([y,z]);occ[tuple(sorted((x,y)))].append((f,x,y,z))
 Etri=len(occ);assert N-Etri+T==2
 for pair in occ.values():assert len(pair)==2 and pair[0][1:3]==pair[1][2:0:-1]
 for link in links:
  assert len(link)>=3;p=start=next(iter(link));seen=set()
  while p not in seen:seen.add(p);p=link[p]
  assert p==start and len(seen)==len(link)
 seen={0};todo=[0]
 while todo:
  for q in neighbors[todo.pop()]:
   if q not in seen:seen.add(q);todo.append(q)
 assert len(seen)==N
 ray=(5,7,19);pre=[]
 for f,(i,j,k) in enumerate(F):
  ss=[dot(ray,cross(P[a],P[b])) for a,b in ((i,j),(j,k),(k,i))];assert all(ss)
  if min(ss)>0:pre.append(f)
 assert len(pre)==1
 par=list(range(T))
 def root(i):
  while par[i]!=i:par[i]=par[par[i]];i=par[i]
  return i
 flats=[];hingemin=None
 for edge,pair in occ.items():
  f,i,j,k=pair[0];ff,jj,ii,l=pair[1];h=dot(normals[f],sub(raw[l],raw[i]));assert h<=0,(edge,h)
  if h==0:flats.append(edge);par[root(f)]=root(ff)
  elif hingemin is None or -h<hingemin:hingemin=-h
 groups=[root(i) for i in range(T)];gf=defaultdict(list)
 for i,g in enumerate(groups):gf[g].append(i)
 normalsG={g:normals[fs[0]] for g,fs in gf.items()};boundary=defaultdict(dict);true=[]
 for edge,pair in occ.items():
  f,i,j,k=pair[0];ff,jj,ii,l=pair[1];g,h=groups[f],groups[ff]
  if g==h:continue
  true.append((i,j,g,h));assert i not in boundary[g];assert j not in boundary[h];boundary[g][i]=j;boundary[h][j]=i
 cycles={}
 for g,link in boundary.items():
  i=start=min(link);cy=[]
  while i not in cy:cy.append(i);i=link[i]
  assert i==start and len(cy)==len(link)>=3
  nn=normalsG[g]
  for a,b,c in zip(cy,cy[1:]+cy[:1],cy[2:]+cy[:2]):assert dot(nn,cross(sub(P[b],P[a]),sub(P[c],P[b])))>0
  cycles[g]=cy
 inc=[set() for _ in P]
 for i,j,g,h in true:inc[i].update([g,h]);inc[j].update([g,h])
 for i in range(N):assert any(det(*(normalsG[g] for g in tri))!=0 for tri in combinations(inc[i],3))
 fmin={g:1 for g in gf};vmax=[-1]*N;H=[];degE=[];primitivezero=0;minp=None;mins=None
 sign=lambda x:(x>0)-(x<0)
 for i,j,g,h in true:
  p=dot(P[i],sub(P[j],P[i]));r=dot(P[j],sub(P[i],P[j]));u=dot(normalsG[g],cross(P[i],P[j]));v=dot(normalsG[h],cross(P[j],P[i]));primitivezero+=sum(t==0 for t in [p,r,u,v])
  fmin[g]=min(fmin[g],sign(u));fmin[h]=min(fmin[h],sign(v));vmax[i]=max(vmax[i],sign(p));vmax[j]=max(vmax[j],sign(r))
  for q in (p,r):
   if q and(minp is None or abs(q)<minp):minp=abs(q)
  for q in(u,v):
   if q and(mins is None or abs(q)<mins):mins=abs(q)
  if p<0 and r<0 and u>0 and v>0:H.append((i,j))
  elif p<=0 and r<=0 and u>=0 and v>=0:degE.append((i,j))
 S=[g for g in gf if fmin[g]>0];U=[i for i in range(N) if vmax[i]<0];degF=[g for g in gf if fmin[g]==0];degV=[i for i in range(N) if vmax[i]==0]
 assert len(S)==1 and len(U)==1 and not H and not degE and not degF and not degV
 stable=S[0];unstable=U[0];n=normalsG[stable];assert n[0]<0 and n[1:]==(0,0);rn=-P[cycles[stable][0]][0];assert rn>0
 assert P[unstable][0]>0 and P[unstable][1:]==(0,0);R2=dot(P[unstable],P[unstable]);nearest=0
 for g,fs in gf.items():
  n=normalsG[g];d=dot(n,P[F[fs[0]][0]]);assert d>0;gap=d*d-rn*rn*dot(n,n);assert gap>=0
  if gap==0:nearest+=1
 assert nearest==1 and all(dot(p,p)<R2 for i,p in enumerate(P) if i!=unstable)
 paircount=0
 if allpairs:
  for g,fs in gf.items():
   f=fs[0];n=normals[f];d=dot(n,raw[F[f][0]])
   zeros=set()
   for pi,p in enumerate(raw):
    gap=d-dot(n,p);assert gap>=0;paircount+=1
    if gap==0:zeros.add(pi)
   assert zeros==set(cycles[g]), 'maximal facet has missing or extra vertices'
 assert N-len(true)+len(gf)==2
 report=dict(status='EXACT_RATIONAL_GOMBOC_PASS',vertices=N,triangles=T,triangulated_edges=Etri,true_edges=len(true),maximal_faces=len(gf),C=2*len(true),coplanar_diagonals=len(flats),class_SHU=[len(S),len(H),len(U)],class_SUH=[len(S),len(U),len(H)],degenerate_equilibria=0,zero_true_edge_primitives=primitivezero,centroid=[0,0,0],volume_numerator=str(vol),volume_denominator=str(6*D**3),centred_denominator=str(den),stable_cycle=cycles[stable],unstable_vertex=unstable,unstable_degree=len(inc[unstable]),stable_x_numerator=str(-rn),unstable_x_numerator=str(P[unstable][0]),radial_ray=list(ray),unique_ray_triangle=pre[0],all_vertex_links_single_cycles=True,all_vertices_rank3=True,global_insphere_unique_equality=True,global_maximum_radius_unique=True,all_pairs_exact_support_tests=paircount,minimum_nonzero_hinge_numerator=str(hingemin),minimum_vertex_predicate=str(minp),minimum_face_side_predicate=str(mins),elapsed=time.time()-st)
 (base/'verification_rational.json').write_text(json.dumps(report,indent=2));(base/'maximal_faces.json').write_text(json.dumps([cycles[g] for g in sorted(cycles)]));(base/'true_edges.csv').write_text('\n'.join(','.join(map(str,sorted((i,j)))) for i,j,g,h in true)+'\n');print(json.dumps(report,indent=2));return report
if __name__=='__main__':audit(sys.argv[1],allpairs='--allpairs' in sys.argv)
