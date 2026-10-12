"""Actual C32 regression for the new cut/triangle/root tests; NOT a Gomboc.
CPython 3.13.5, stdlib only. python -S physical_cut_control.py
Uses the complete Map implementation supplied in joint_frontier.py.
Geometry inherited from C32_FOUR_TRIANGLE_FAN_PHYSICAL_BOUNDARY_V1,
asg_q3Tky24st4Y47d0V04HEfjxm / de9cd99e6171b5909689e636d347b20d427f837b702d67eb007279b34f4fbaeb.
"""
from fractions import Fraction as F
from itertools import combinations
from pathlib import Path
from joint_frontier import Map,outrows,graph_mask,serial,pin
assert __debug__
def dot(a,b):return sum((x*y for x,y in zip(a,b)),F(0))
def sub(a,b):return tuple(x-y for x,y in zip(a,b))
def cross(a,b):return (a[1]*b[2]-a[2]*b[1],a[2]*b[0]-a[0]*b[2],a[0]*b[1]-a[1]*b[0])
def det3(a,b,c):return dot(a,cross(b,c))
def mm(a,b):return [[dot(r,c) for c in zip(*b)] for r in a]
def elim(a):
 a=[list(map(F,r)) for r in a];r=0;d=F(1)
 for j in range(len(a[0])):
  k=next((k for k in range(r,len(a)) if a[k][j]),None)
  if k is None:continue
  if k!=r:a[k],a[r]=a[r],a[k];d=-d
  z=a[r][j];d*=z;a[r]=[t/z for t in a[r]]
  for i in range(len(a)):
   if i!=r:
    z=a[i][j];a[i]=[t-z*w for t,w in zip(a[i],a[r])]
  r+=1
  if r==len(a):break
 return r,d,a
def det(a):
 r,d,_=elim(a);return d if r==len(a) else F(0)
def inv(a):
 n=len(a);_,_,b=elim([list(a[i])+[F(i==j) for j in range(n)] for i in range(n)])
 assert [r[:n] for r in b]==[[F(i==j) for j in range(n)] for i in range(n)]
 return [r[n:] for r in b]
P=[(0,0,0),(0,0,1),(0,1,0),(F(125249,249748),-F(499,249748),F(125249,249748)),
 (F(93812,155563),-F(499,155563),F(62375,155563)),(F(3,4),-1,F(3,4)),(1,0,0),
 (F(25449,19939),-F(26946,19939),F(7984,19939)),(F(3,2),-F(3,2),F(1,4))]
P=[tuple(map(F,p)) for p in P]
FAC=[[0,6,8],[0,2,6],[0,1,2],[0,5,1],[0,8,7,5],[2,3,4,6],[4,7,8,6],[1,5,7,4,3],[1,3,2]]
M=Map(FAC);D=Map(M.dual_faces);fs=set()
for i,j,k in combinations(range(9),3):
 n=cross(sub(P[j],P[i]),sub(P[k],P[i]))
 if not any(n):continue
 sl=[dot(n,sub(p,P[i])) for p in P]
 if (min(sl)<0<max(sl)) or not any(sl):continue
 fs.add(frozenset(a for a,s in enumerate(sl) if not s))
assert fs==set(map(frozenset,FAC))
def integrate(p,apex):
 v=F(0);mom=[F(0)]*3
 for f in FAC:
  for j in range(1,len(f)-1):
   a,b,c=[p[k] for k in [f[0],f[j],f[j+1]]]
   w=det3(sub(a,apex),sub(b,apex),sub(c,apex))/6;assert w>=0;v+=w
   for k in range(3):mom[k]+=w*(apex[k]+a[k]+b[k]+c[k])/4
 return v,tuple(t/v for t in mom)
v,g=integrate(P,(F(0),)*3)
assert (v,g)==integrate(P,tuple(sum(p[k] for p in P)/9 for k in range(3)))
assert v==F(743992554601211,1549322036088872)
X=[sub(p,g) for p in P];assert integrate(X,(F(0),)*3)==(v,(0,0,0))
Q=[];C=[];d=[]
for f in FAC:
 a,b,c=[X[i] for i in f[:3]];n=cross(sub(b,a),sub(c,a));h=dot(n,a);assert h>0
 q=tuple(t/h for t in n);Q.append(q)
 assert all(dot(q,X[j])==1 if j in f else dot(q,X[j])<1 for j in range(9))
 mass=F(0);mom=[F(0)]*3
 for j in range(1,len(f)-1):
  a,b,c=[X[i] for i in [f[0],f[j],f[j+1]]];w=det3(a,b,c);assert w>0;mass+=w
  for k in range(3):mom[k]+=w*(a[k]+b[k]+c[k])
 C.append(tuple(t/(3*mass) for t in mom));d.append(mass/(2*v))
L=[[d[j]*(1-dot(Q[i],C[j])) for j in range(9)] for i in range(9)]
assert sum(d)==3 and all(sum(row)==3 for row in L)
assert all(sum(d[i]*Q[i][k] for i in range(9))==sum(d[i]*C[i][k] for i in range(9))==0 for k in range(3))
assert [[sum(d[i]*C[i][j]*Q[i][k] for i in range(9)) for k in range(3)] for j in range(3)]==[[F(i==j) for j in range(3)] for i in range(3)]
LL=mm(L,L);assert all(LL[i][j]+L[i][j]==4*d[j] for i in range(9) for j in range(9))
assert mm(L,Q)==[[-t for t in q] for q in Q]
K=[[L[i][j]+F(i==j) for j in range(9)] for i in range(9)]
bad=det([r[:4] for r in K[:4]])
assert bad==-F(29225402286904272323120130050768458025941435,44476389385373086840084719020220335744901748548)
assert elim(L)[0]==4 and elim(K)[0]==6
controls=[]
for metric in [[[1,0,0],[0,1,0],[0,0,1]],[[2,1,0],[1,3,1],[0,1,2]]]:
 assert all(det([r[:k] for r in metric[:k]])>0 for k in range(1,4));reciprocal=inv(metric)
 GS=[[dot(X[i],mm([sub(X[j],X[i])],metric)[0]) for j in range(9)] for i in range(9)]
 HS=[[dot(Q[i],mm([sub(Q[j],Q[i])],reciprocal)[0]) for j in range(9)] for i in range(9)]
 G=outrows((i,j) for i in range(9) for j in range(9) if i!=j and GS[i][j]>=0)
 H=outrows((i,j) for i in range(9) for j in range(9) if i!=j and HS[i][j]>=0)
 assert M.cut_ok(G) and D.cut_ok(H)
 ph=M.projection(G,H);hp=D.projection(H,G);assert ph is not None and hp is not None
 assert all(HS[i][j]>0 for i,j in ph) and all(GS[i][j]>0 for i,j in hp)
 stable=[i for i in range(9) if all(HS[i][j]<0 for j in range(9) if i!=j)]
 unstable=[i for i in range(9) if all(GS[i][j]<0 for j in range(9) if i!=j)]
 assert all(M.no_dominator(G,s) for s in stable) and all(D.no_dominator(H,u) for u in unstable)
 controls.append(dict(metric=metric,reciprocal=reciprocal,primal_shadow_mask=graph_mask(G),dual_shadow_mask=graph_mask(H),
  stable=stable,unstable=unstable,forced_dual=ph,forced_primal=hp))
assert controls[0]['stable']==[0,3,4,7] and controls[0]['unstable']==[1,2,6,8]
def enc(x):
 if isinstance(x,F):return str(x)
 if isinstance(x,dict):return {k:enc(v) for k,v in x.items()}
 if isinstance(x,(tuple,list)):return [enc(v) for v in x]
 return x
report=dict(vertices=P,facets=FAC,edges=sorted(M.edges),volume=v,centroid=g,facet_area_centroids=C,
 omega=[z/3 for z in d],d=d,poles=Q,Lambda=L,negative_four_minor=bad,controls=controls)
b=serial(enc(report));Path('physical_cut_control.json').write_bytes(b)
print('ACTUAL_C32_HULL_TWO_VOLUME_INTEGRATIONS_ONE_LAMBDA_SQUARE_PASS')
print('ALL_NEW_CUT_PROJECTION_AND_ROOT_RULES_TWO_RECIPROCAL_METRICS_PASS')
print('PHYSICAL_NEGATIVE_FOUR_MINOR_RETAINED',bad)
print('REPORT',*pin(b));print('SOURCE',*pin(Path(__file__).read_bytes()))
