# material-95de5a8f64bd

AI research material · [Export notes](../catalog/coverage.md#text-records)

---

# J128 exact cap charts and mass-closed simplex — complete recovery

Coordinator computation from the literal KF27I DETACHED_G6 input in immutable result figure-0609 (SHA256 cc979b833c4a44c33611e9cb6dbd2845e5a94c2a569ae22af5bb286414f8a23d). That result was read completely. This capsule includes the actual 47-point input and every line of the independently authored exact generator/auditor needed below. No earlier sandbox, worker optimizer or encoded archive is required. It creates five new exact nonwinner bodies and two exact analytic certificates. It does not construct own110.

Save the two fenced source units below with the indicated filenames, preserving one terminal newline. Run `OPENBLAS_NUM_THREADS=1 python RESEARCH128.py` in that directory. Executed environment: Python 3.13.5, NumPy 2.3.5, SciPy 1.17.0; exact arithmetic is standard-library fractions.Fraction. Qhull only nominates triangles; every plane/all-point support, closed connected edge incidence, mass, equilibrium and certificate comparison is rational. This is one exact implementation, not a claim of two independent physics engines. The exact input and generated outputs have these byte counts and SHA-256 values:

- DETACHED_G6.txt: 1034 bytes; a5b7cb7cd10de4a8ba08a997945ee3a932385cf03a5e259946be867954772a50
- RESEARCH128.py: 13313 bytes; cc16e6325ccbe46bdd56a3a56b39a497c929d7cea7d3ec14dd63dd2d5b70a6f7
- EXACT_REPORT.json: 31536 bytes; f12dec1d99fee4e031ce4e10e03e991231e92f69a4873f2429637071f23bb405
- BALANCED_1.json: 11166 bytes; 276ee7783584faf9cf8f4f2c5aefd286cd7fbb3b8229346fe79c3c029d06912e
- BALANCED_2.json: 11157 bytes; eb5c7c204cebbd9274e7c6c3bdeedeef969eabb1fbb34dd9af45aa089b5e8314
- BALANCED_3.json: 11172 bytes; 910dcd26d0880e374c6ae06e81f3133b3a74a974a32b465123045dd193d2e97b
- BALANCED_MIDPOINT.json: 11044 bytes; 565fe68d5d98f1a80ee02ee02b60dabb263a08532d85d3d07c594d3334dfa6b9
- SCOUT48_G8.json: 5063 bytes; fb2b6cff519d2529f009a4b37e4b28052fcc873a81957af3350e4fdcf1724640

Expected terminal markers:
```
ALL_HORIZON_CONCAVITY_OK [0.3093878054357532, 0.32700019429201066, 0.3081524002570494]
ONE_STEP_HEMISPHERE_BARRIER_OK
EXACT_BODY BALANCED_1.json [2, 1, 1] [0, 0, 0] [0, 0, 0]
EXACT_BODY BALANCED_2.json [2, 1, 1] [0, 0, 0] [0, 0, 0]
EXACT_BODY BALANCED_3.json [2, 1, 1] [0, 0, 0] [0, 0, 0]
EXACT_BODY BALANCED_MIDPOINT.json [3, 2, 3] [0, 0, 0] [0, 0, 0]
EXACT_SCOUT48 [2, 1, 1] [0.4607624770883719]
J128_EXACT_PASS 31536 f12dec1d99fee4e031ce4e10e03e991231e92f69a4873f2429637071f23bb405
```

## Scope of the new findings

For a single new apex z over any fixed visible-face subset J of the exact input K, with oriented double-area normals e_i, old face centroids b_i and any point v_i on each plane, added pyramid volumes are mu_i=e_i.(z-v_i)/6. Define mu=sum mu_i, B=sum b_i e_i^T/8 and d=sum b_i(e_i.v_i)/8. The exact new first moment is M+mu*z/4+B*z-d, and volume V+mu. On a fixed added-volume plane mu=t>=0, g(z)=A*z+c with A=(tI/4+B)/(V+t), c=(M-d)/(V+t). The input-specific certificate bounds the largest eigenvalue of sym(B) by 1/3 for EVERY subset of its 90 facets and proves V>2/3. Thus sym(I-A)>I/2 for all t>=0. The inequality (z-g(z)).(v-z)>0 for a specified old witness v is strictly concave quadratic in z, while old selected witness guards and horizon/volume constraints are affine. Each specified witness/forest/horizon/fixed-volume feasible slice is convex. The union over witnesses, horizons or volumes is NOT claimed convex. Stable-equilibrium conditions are not claimed convex; this is not a no-go for own110.

The four BALANCED bodies have true V50/E144/F96,C288. The three corners are exact own211/weak000/primitive000; their coordinatewise arithmetic mean is exact own323/weak000/primitive000. All four, and the full intervening parameter simplex, have the same labelled hull complex, exact volume and first moment, hence the same actual centroid. Independent cross-corner support signs certify the full simplex's convex geometry, not just the four samples. The midpoint has strict U6 and U47 and real positive P~2.262645355293221e-7; its Q is approximately (.46140465920840373,.000055191321316314695). The three corners have P[] and Q approximately .4615892911431183, .4614184893192548 and .46146766339700573. This disproves a general inference from mass-closed U1 endpoints to U1 under convex interpolation. It does not assert that the connecting paths avoid weak states.

The hemisphere certificate applies only to retained-host outer bodies K subset L, with every new extreme point having a strict positive radial witness in OLD K at actual centre c, and ||c-g(K)||_infinity<=1/2000. The hemisphere w.n>0 for w=(-471042,879704,65114) must retain a local support minimum, hence a stable equilibrium if L is weak-free. It does NOT prove S>=2. It allows cancellation of the opposite basin and does not cover new-to-new routes, changed/removed host geometry or larger centre excursions. Exact projected-boundary support >.5146 and an interior one-step-envelope support <.512 remain separated after the certified centre error <.000867.

SCOUT48_G8 is the exact rationalized one-apex numerical nomination: V48/E138/F92,C276, own211/weak000/primitive000, P[], Q~.4607624770883719. It is not own110 or a cross-lineage persistence record. Complete numerical nomination methods are preserved separately; this exact capsule requires only the frozen rational apex.

## File: DETACHED_G6.txt
```text
47 1000000
-220660 -170809 739992
-470733 -252568 617724
-344429 -201140 695040
-827617 -345105 -7630
-804956 -306141 -196980
-617752 -310722 484546
-802871 -391980 208231
708441 212327 -26773
629324 353053 -32544
109721 -76616 760640
306556 -32243 700380
212446 -60072 735986
469379 -34257 598089
392685 -40271 652622
646907 -14969 394808
537342 -31849 536185
596588 -24705 468240
750839 45997 64966
-102855 -139962 763378
7557 -112190 768796
719082 11448 235222
687865 -2839 316832
740239 27161 150766
750330 69885 -21314
738230 84890 -114933
592447 240452 -366643
659702 196951 -280592
707333 140337 -199650
700973 -34829 -222306
-736323 -274563 -374807
228858 452552 -370941
60624 561672 -200802
142319 490402 -325534
566004 -68026 -372688
612214 -197888 -188679
464617 500011 -71398
-487325 -442504 -463527
552036 118367 -435356
-19326 554813 -63048
350712 442484 -390884
577522 340656 -272794
199735 530859 -305689
-532859 -303654 -567337
-484871 -149126 -645284
472985 292300 -459118
-416022 64364 111262
-193306 -303834 71494
```

## File: RESEARCH128.py
```python
#!/usr/bin/env python3
"""J128: finite own-mass cap charts and a mass-closed nonconvexity example.
Python 3.13.5, NumPy 2.3.5, SciPy 1.17.0. No input except DETACHED_G6.txt.
Qhull proposes triangular facets; all supporting signs, closed edge incidence,
centroids, equilibrium comparisons and theorem certificates are rational.
"""
from fractions import Fraction as F
from pathlib import Path
from itertools import combinations
from hashlib import sha256
from math import gcd
from functools import reduce
import json,sys
import numpy as np
from scipy.spatial import ConvexHull

ROOT=Path(__file__).resolve().parent
Z=F(0);ONE=F(1)
def add(a,b):return tuple(x+y for x,y in zip(a,b))
def sub(a,b):return tuple(x-y for x,y in zip(a,b))
def sm(s,a):return tuple(s*x for x in a)
def dot(a,b):return sum((x*y for x,y in zip(a,b)),Z)
def cross(a,b):return (a[1]*b[2]-a[2]*b[1],a[2]*b[0]-a[0]*b[2],a[0]*b[1]-a[1]*b[0])
def det(a,b,c):return dot(a,cross(b,c))
def mean(a):return sm(ONE/len(a),tuple(sum((x[j]for x in a),Z)for j in range(3)))
def matadd(A,B):return tuple(add(a,b)for a,b in zip(A,B))
def matsm(s,A):return tuple(sm(s,a)for a in A)
def transpose(A):return tuple(zip(*A))
def matvec(A,v):return tuple(dot(a,v)for a in A)
def outer(a,b):return tuple(sm(x,b)for x in a)
def matmul(A,B):return tuple(tuple(dot(a,b)for b in transpose(B))for a in A)
def inv(A):
 D=det(*A);assert D
 return matsm(1/D,transpose((cross(A[1],A[2]),cross(A[2],A[0]),cross(A[0],A[1]))))
I=tuple(tuple(F(i==j)for j in range(3))for i in range(3))
def frac(a):return str(a)
def jsonable(o):
 if isinstance(o,F):return str(o)
 if isinstance(o,dict):return {str(k):jsonable(v)for k,v in o.items()}
 if isinstance(o,(tuple,list)):return [jsonable(v)for v in o]
 if isinstance(o,np.integer):return int(o)
 return o

def load():
 data=(ROOT/'DETACHED_G6.txt').read_bytes()
 assert len(data)==1034 and sha256(data).hexdigest()=='a5b7cb7cd10de4a8ba08a997945ee3a932385cf03a5e259946be867954772a50'
 words=data.decode().split();N,D=map(int,words[:2]);X=[tuple(F(int(t),D)for t in words[2+3*i:5+3*i])for i in range(N)]
 V=F(4052900436758915819,6000000000000000000)
 g=(F(38946985201102467703899,2315943106719380468000000),F(36285365677586521554829,4052900436758915819000000),F(-276840702507758878921281,8105800873517831638000000))
 return X,V,g

def hull(X):
 cand=ConvexHull(np.array([[float(x)for x in p]for p in X]));faces=[];planes=[]
 for raw in cand.simplices:
  tri=list(map(int,raw));a,b,c=[X[i]for i in tri];n=cross(sub(b,a),sub(c,a));h=dot(n,a)
  vals=[dot(n,x)-h for x in X]
  if max(vals)>0:
   assert min(vals)>=0,'Qhull facet not an exact supporting plane'
   tri[1],tri[2]=tri[2],tri[1];n=sm(-1,n);h=-h;vals=[-v for v in vals]
  assert max(vals)==0 and sum(v==0 for v in vals)==3,'Only strict triangular facets supported in this capsule'
  faces.append(tuple(tri));planes.append((n,h))
 edge={}
 for i,tri in enumerate(faces):
  for j in range(3):edge.setdefault(tuple(sorted((tri[j],tri[(j+1)%3]))),[]).append(i)
 assert all(len(v)==2 for v in edge.values())
 verts=sorted(set(i for t in faces for i in t));assert len(verts)-len(edge)+len(faces)==2
 seen={0};todo=[0]
 while todo:
  a=todo.pop()
  for j in range(3):
   e=tuple(sorted((faces[a][j],faces[a][(j+1)%3])))
   for b in edge[e]:
    if b not in seen:seen.add(b);todo.append(b)
 assert len(seen)==len(faces)
 # Every listed face is a true maximal hull face; the connected, edge-closed
 # subset therefore is the entire boundary of the convex hull.
 return faces,planes,edge,verts

def integrate(X,faces):
 V=Z;M=(Z,Z,Z)
 for t in faces:
  a,b,c=[X[i]for i in t];d=det(a,b,c);V+=d/6;M=add(M,sm(d/24,add(add(a,b),c)))
 assert V>0
 return V,M,sm(1/V,M)

def bars(points,edges):
 radii=[dot(p,p)for p in points];links=[]
 for i,j in edges:
  d=sub(points[j],points[i]);dd=dot(d,d);t=max(Z,min(ONE,-dot(points[i],d)/dd));p=add(points[i],sm(t,d));links.append((dot(p,p),int(i),int(j)))
 parent=list(range(len(points)));peak=radii[:];out=[]
 def root(a):
  while parent[a]!=a:parent[a]=parent[parent[a]];a=parent[a]
  return a
 for level,i,j in sorted(links,reverse=True):
  a,b=root(i),root(j)
  if a==b:continue
  if peak[a]<peak[b]:a,b=b,a
  depth=1-level/peak[b]
  assert depth>=0
  if depth>0:out.append(depth)
  parent[b]=a
 return sorted(out,reverse=True)

def audit(X):
 fs,hs,es,vs=hull(X);V,M,g=integrate(X,fs);Y=[sub(x,g)for x in X]
 SS=[];UU=[];HH=[];weak=[[],[],[]];zeros=[0,0,0]
 for k,(t,(n,h))in enumerate(zip(fs,hs)):
  hh=h-dot(n,g);assert hh>0;p=sm(hh/dot(n,n),n)
  signs=[dot(cross(sub(Y[t[(j+1)%3]],Y[t[j]]),sub(p,Y[t[j]])),n)for j in range(3)]
  zeros[0]+=sum(s==0 for s in signs)
  if min(signs)>0:SS.append(sorted(t))
  elif min(signs)>=0:weak[0].append(sorted(t))
 for i in vs:
  neigh=sorted(set(j if i==k else k for k,j in es if i in(k,j)))
  signs=[dot(Y[i],sub(Y[j],Y[i]))for j in neigh];zeros[1]+=sum(s==0 for s in signs)
  if max(signs)<0:UU.append(i)
  elif max(signs)<=0:weak[1].append(i)
 for (i,j),(a,b)in es.items():
  d=sub(Y[j],Y[i]);dd=dot(d,d);aa=-dot(Y[i],d);bb=dd-aa;p=add(Y[i],sm(aa/dd,d))
  n1,n2=hs[a][0],hs[b][0];g11,g12,g22=dot(n1,n1),dot(n1,n2),dot(n2,n2);D=g11*g22-g12*g12;assert D>0
  c1=dot(p,n1)*g22-dot(p,n2)*g12;c2=dot(p,n2)*g11-dot(p,n1)*g12
  assert sm(D,p)==add(sm(c1,n1),sm(c2,n2))
  signs=[aa,bb,c1,c2];zeros[2]+=sum(s==0 for s in signs)
  if min(signs)>0:HH.append([i,j])
  elif min(signs)>=0:weak[2].append([i,j])
 assert len(SS)+len(UU)-len(HH)==2,'Nondegenerate Morse count expected'
 PP=bars(Y,list(es));QQ=bars([sm(1/(h-dot(n,g)),n)for n,h in hs],list(es.values()))
 assert len(PP)==len(UU)-1 and len(QQ)==len(SS)-1
 return {'V':len(vs),'E':len(es),'F':len(fs),'strict':[len(SS),len(UU),len(HH)],'weak':[len(v)for v in weak],'primitive_zero':zeros,'S':sorted(SS),'U':UU,'H':sorted(HH),'P':PP,'Q':QQ,'volume':V,'moment':M,'centroid':g},fs

def exact_cap_bounds(X,V,g,fs):
 Bparts=[]
 for t in fs:
  a,b,c=[X[i]for i in t];n=cross(sub(b,a),sub(c,a));bc=mean([a,b,c]);Bparts.append(matsm(F(1,8),outer(bc,n)))
 Bsum=tuple(tuple(sum((B[i][j]for B in Bparts),Z)for j in range(3))for i in range(3))
 assert Bsum==matsm(V/4,I)
 S=[matsm(F(1,2),matadd(B,transpose(B)))for B in Bparts]
 upper=tuple(tuple(sum((max(B[i][j],Z)for B in S),Z)for j in range(3))for i in range(3))
 lower=tuple(tuple(sum((min(B[i][j],Z)for B in S),Z)for j in range(3))for i in range(3))
 G=tuple(upper[i][i]+sum((max(upper[i][j],-lower[i][j])for j in range(3)if i!=j),Z)for i in range(3))
 assert all(z<F(1,3)for z in G)and V>F(2,3)
 return {'gershgorin_all_subsets_rows':G,'rational_upper':F(1,3),'volume_lower':F(2,3),'conclusion':'For every visible-face subset and every fixed added volume mu>=0, sym(I-A)>I/2, where A=(mu*I/4+B)/(V+mu). Each specified new-apex witness inequality is strictly concave quadratic; old selected witness guards, visibility and fixed-volume conditions are affine. Union across witnesses/horizons is not convex.'}

def one_step_barrier(X,g):
 Y=[sub(x,g)for x in X];w=(F(-471042),F(879704),F(65114));e=(w[1],-w[0],Z);f=cross(w,e)
 P=np.array([[float(dot(y,e)),float(dot(y,f))]for y in Y]);P=P/np.linalg.norm(P,axis=0)
 poly=ConvexHull(P);edges=[];R=F(2573,5000)
 for i,j in zip(poly.vertices,np.roll(poly.vertices,-1)):
  i,j=int(i),int(j);u=cross(w,sub(Y[j],Y[i]));h=dot(u,Y[i])
  if h<0:u=sm(-1,u);h=-h
  assert h>0 and all(dot(u,y)<=h for y in Y)
  assert h*h>R*R*dot(u,u)
  edges.append({'vertices':[i,j],'squared_distance':h*h/dot(u,u)})
 target=np.array([-.42784698,.85837802,.28307973]);s=F(round(target[0]/(1+target[2])*1000000),1000000);t=F(round(target[1]/(1+target[2])*1000000),1000000);D=1+s*s+t*t
 n=(2*s/D,2*t/D,(1-s*s-t*t)/D);assert dot(n,n)==1 and dot(n,w)>0
 H=F(64,125);margins=[]
 for y in Y:
  rhs=2*H-dot(n,y);assert rhs>0 and rhs*rhs>dot(y,y);margins.append(rhs*rhs-dot(y,y))
 delta=F(1,2000);err=F(867,1000000);level=F(5133,10000)
 assert 3*delta*delta<err*err and H+err<level<R-err
 return {'hemisphere_w':w,'interior_unit_n':n,'stereographic_s_t':[s,t],'projected_polygon_edges':edges,'boundary_support_lower':R,'one_step_support_upper':H,'norm_inequality_min_margin':min(margins),'centre_cube_radius':delta,'euclidean_error_upper':err,'separating_level':level,'conclusion':'For K contained in L whose every new extreme vertex has a strict positive radial witness in the OLD K relative to the actual centre c, and ||c-g||_infinity<=1/2000, the hemisphere w.n>0 retains a local minimum of support height. Thus a weak-free L still has a stable equilibrium there. This does NOT prove S>=2: retirement of the opposite/elder basin, new-to-new witnesses, host changes or larger centre drift remain open.'}

def balanced_family(X,V,g):
 triples=[[5,38,45],[34,36,46],[39,44,43]];eta=F(1,1000);rho=F(1,20);bs=[];ns=[];mus=[];ps=[]
 for t in triples:
  v=[X[i]for i in t];b=mean(v);n=cross(sub(v[1],v[0]),sub(v[2],v[0]))
  if dot(n,sub(b,g))<0:n=sm(-1,n)
  hh=dot(n,sub(b,g));mu=eta*hh/6;apex=add(b,sm(eta*hh/dot(n,n),n));P=matadd(I,matsm(-1/dot(n,n),outer(n,n)))
  bs.append(b);ns.append(n);mus.append(mu);ps.append((apex,P))
 m0,m1,m2=mus;a1,P1=ps[1];a2,P2=ps[2]
 MV=V+m1+m2;MM=add(sm(V,g),add(sm(m1/4,add(sm(3,bs[1]),a1)),sm(m2/4,add(sm(3,bs[2]),a2))))
 q=sm(1/(MV+3*m0/4),add(MM,sm(3*m0/4,bs[0])))
 n=ns[0];plane=dot(n,bs[0])+eta*dot(n,sub(bs[0],g));p=add(q,sm((plane-dot(n,q))/dot(n,n),n))
 fullV=MV+m0;fullM=add(MM,sm(m0/4,add(sm(3,bs[0]),p)));fullg=sm(1/fullV,fullM)
 C=matadd(matsm(m1*m1,P1),matsm(m2*m2,P2));Ci=inv(C)
 endpoints=[]
 for index in triples[0]:
  da=sm(rho,sub(X[index],bs[0]));z=matvec(Ci,da);d1=sm(-m0*m1,matvec(P1,z));d2=sm(-m0*m2,matvec(P2,z))
  assert dot(ns[1],d1)==0 and dot(ns[2],d2)==0
  assert add(sm(m0,da),add(sm(m1,d1),sm(m2,d2)))==(Z,Z,Z)
  endpoints.append(X+[add(p,da),add(a1,d1),add(a2,d2)])
 midpoint=X+[p,a1,a2]
 assert all(mean([endpoints[k][i]for k in range(3)])==midpoint[i]for i in range(50))
 audits=[];facets=[]
 for j,XX in enumerate(endpoints+[midpoint]):
  out,fs=audit(XX);assert out['volume']==fullV and out['moment']==fullM and out['centroid']==fullg
  assert out['V']==50 and out['E']==144 and out['F']==96
  assert out['weak']==[0,0,0]and out['primitive_zero']==[0,0,0]
  assert out['strict']==([2,1,1]if j<3 else [3,2,3])
  audits.append(out);facets.append(set(tuple(sorted(t))for t in fs))
  name=f'BALANCED_{j+1}.json'if j<3 else 'BALANCED_MIDPOINT.json'
  (ROOT/name).write_text(json.dumps(jsonable({'vertices':XX,'audit':out}),indent=2)+'\n')
  print('EXACT_BODY',name,out['strict'],out['weak'],out['primitive_zero'],flush=True)
 assert all(f==facets[0]for f in facets)
 # The whole parameter simplex preserves these support incidences: each new
 # triangle determinant is multi-affine in the three cap apices. Each facet
 # has one moving apex, and a tested other cap apex varies linearly; corner
 # cross-combinations are checked below, not merely matched endpoints.
 boxok=True
 for face in facets[0]:
  moving=[i for i in face if i>=47]
  if not moving:continue
  assert len(moving)==1
  ia=moving[0]
  for k in range(3):
   tri=list(face);a,b,c=[endpoints[k][i]for i in tri];nn=cross(sub(b,a),sub(c,a));hh=dot(nn,a)
   ref=endpoints[k][0]
   if dot(nn,ref)>hh:nn=sm(-1,nn);hh=-hh
   for l in range(3):
    for ii in range(50):
     if ii in face:continue
     # Same moving vertex is on its own facet by definition; all other moving
     # apices may be checked at independently selected simplex corners.
     if dot(nn,endpoints[l][ii])>=hh:boxok=False
 result={'base_faces':triples,'relative_height':eta,'rho':rho,'cap_volumes':mus,'shared_volume':fullV,'shared_moment':fullM,'shared_centroid':fullg,'all_same_combinatorial_type':True,'cross_corner_support_check':boxok,'audits':audits,'conclusion':'Three exact own211/weak000 bodies have identical volume, first moment, centroid and labelled face complex. Their coordinatewise arithmetic mean is exact own323/weak000, with additional strict U at vertex47. Thus convex interpolation of mass-closed valid endpoints does not preserve U1. All four have C288; none is110.'}
 return result

def main():
 X,V,g=load();fs,_,_,_=hull(X);VV,MM,gg=integrate(X,fs);assert VV==V and gg==g
 theorem=exact_cap_bounds(X,V,g,fs);barrier=one_step_barrier(X,g)
 print('ALL_HORIZON_CONCAVITY_OK',[float(x)for x in theorem['gershgorin_all_subsets_rows']],flush=True)
 print('ONE_STEP_HEMISPHERE_BARRIER_OK',flush=True)
 family=balanced_family(X,V,g)
 assert family['cross_corner_support_check']
 # The selected 30,000-proposal scout is frozen on a true 1e-8 grid.
 apex=tuple(F(v,100000000)for v in [-9934332,44086278,1003988])
 scout,scoutfs=audit(X+[apex]);assert scout['strict']==[2,1,1] and scout['weak']==[0,0,0] and scout['primitive_zero']==[0,0,0]
 (ROOT/'SCOUT48_G8.json').write_text(json.dumps(jsonable({'vertices':X+[apex],'audit':scout}),indent=2)+'\n')
 print('EXACT_SCOUT48',scout['strict'],[float(v)for v in scout['Q']],flush=True)
 report={'input':'KF27I_DETACHED_G6','input_sha256':sha256((ROOT/'DETACHED_G6.txt').read_bytes()).hexdigest(),'cap_convexity_certificate':theorem,'one_step_hemisphere_certificate':barrier,'mass_closed_nonconvexity':family,'finite_scout48':scout}
 data=json.dumps(jsonable(report),indent=2)+'\n';(ROOT/'EXACT_REPORT.json').write_text(data)
 print('J128_EXACT_PASS',len(data.encode()),sha256(data.encode()).hexdigest(),flush=True)
if __name__=='__main__':main()
```
