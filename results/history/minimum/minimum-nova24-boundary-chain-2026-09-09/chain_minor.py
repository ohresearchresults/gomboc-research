"""NOVA24_TRIANGULAR_CHAIN_MINOR_V1; CPython 3.13.5, stdlib only.
Analytical input: the actual-body Lambda in parent asg_LpT3Sk6f4DiL1I4OgYFGK6lc,
e415baee38fcd56612393d45cd7c966dad05dffa836c3659ace5ca13a2b1490b.
This is NEW source, not any of the four unavailable original cap9 units.
Run: python -S chain_minor.py. No numerical search or external input.
"""
from fractions import Fraction as F
from itertools import combinations
from pathlib import Path
import hashlib,json
assert __debug__
def dot(a,b):return sum(x*y for x,y in zip(a,b))
def sub(a,b):return tuple(x-y for x,y in zip(a,b))
def cross(a,b):return (a[1]*b[2]-a[2]*b[1],a[2]*b[0]-a[0]*b[2],a[0]*b[1]-a[1]*b[0])
def det3(a,b,c):return dot(a,cross(b,c))
def tr(a):return list(map(list,zip(*a)))
def mm(a,b):return [[dot(r,c) for c in zip(*b)] for r in a]
def eye(n):return [[F(i==j) for j in range(n)] for i in range(n)]
def elim(a):
 a=[list(map(F,r)) for r in a];r=0;d=F(1)
 for j in range(len(a[0])):
  k=next((k for k in range(r,len(a)) if a[k][j]),None)
  if k is None:continue
  if k!=r:a[k],a[r]=a[r],a[k];d=-d
  z=a[r][j];d*=z;a[r]=[v/z for v in a[r]]
  for i in range(len(a)):
   if i!=r:
    z=a[i][j];a[i]=[v-z*w for v,w in zip(a[i],a[r])]
  r+=1
  if r==len(a):break
 return r,d,a
def det(a):
 r,d,_=elim(a);return d if r==len(a) else F(0)
def inv(a):
 n=len(a);r,_,b=elim([list(a[i])+eye(n)[i] for i in range(n)])
 assert r==n and [x[:n] for x in b]==eye(n)
 return [x[n:] for x in b]
def hull(p):
 faces=set();n=len(p)
 for i,j,k in combinations(range(n),3):
  normal=cross(sub(p[j],p[i]),sub(p[k],p[i]))
  if not any(normal):continue
  s=[dot(normal,sub(x,p[i])) for x in p]
  if max(s)>0 and min(s)<0:continue
  if not any(s):continue
  faces.add(tuple(a for a in range(n) if s[a]==0))
 faces=sorted(faces);edges=set()
 for f,g in combinations(faces,2):
  t=set(f)&set(g)
  if len(t)==2:edges.add(tuple(sorted(t)))
  else:assert len(t)<=1
 center=tuple(sum(x[k] for x in p)/n for k in range(3));cycles=[]
 for f in faces:
  adj={i:sorted(j for j in f if tuple(sorted((i,j))) in edges) for i in f}
  assert all(len(v)==2 for v in adj.values())
  q=[min(f),adj[min(f)][0]]
  while True:
   j=next(j for j in adj[q[-1]] if j!=q[-2])
   if j==q[0]:break
   assert j not in q;q.append(j)
  assert set(q)==set(f)
  normal=cross(sub(p[q[1]],p[q[0]]),sub(p[q[2]],p[q[0]]))
  if dot(normal,sub(center,p[q[0]]))>0:q=[q[0]]+q[:0:-1]
  cycles.append(q)
 assert n-len(edges)+len(cycles)==2
 assert set().union(*(set(f) for f in cycles))==set(range(n))
 return cycles,sorted(edges)
def integrate(p,faces):
 d=F(0);m=[F(0)]*3
 for f in faces:
  for j in range(1,len(f)-1):
   a,b,c=(p[i] for i in (f[0],f[j],f[j+1]));z=det3(a,b,c);d+=z
   for k in range(3):m[k]+=z*(a[k]+b[k]+c[k])
 assert d>0
 return d/6,tuple(x/(4*d) for x in m)
def geometry(p,faces):
 found,edges=hull(p)
 assert {frozenset(f) for f in found}=={frozenset(f) for f in faces}
 v,g=integrate(p,faces);x=[sub(a,g) for a in p]
 v1,g1=integrate(x,faces);assert v1==v and g1==(0,0,0)
 q=[];d=[];c=[]
 for f in faces:
  a,b,z=(x[i] for i in f[:3]);normal=cross(sub(b,a),sub(z,a));h=dot(normal,a)
  assert h>0;qi=tuple(t/h for t in normal)
  assert all(dot(qi,x[i])==1 if i in f else dot(qi,x[i])<1 for i in range(len(x)))
  total=F(0);s=[F(0)]*3
  for j in range(1,len(f)-1):
   a,b,z=(x[i] for i in (f[0],f[j],f[j+1]));w=det3(a,b,z);assert w>0;total+=w
   for k in range(3):s[k]+=w*(a[k]+b[k]+z[k])
  q.append(qi);d.append(total/(2*v));c.append(tuple(t/(3*total) for t in s))
 assert sum(d)==3
 assert all(sum(d[i]*q[i][k] for i in range(len(q)))==sum(d[i]*c[i][k] for i in range(len(q)))==0 for k in range(3))
 assert [[sum(d[i]*c[i][j]*q[i][k] for i in range(len(q))) for k in range(3)] for j in range(3)]==eye(3)
 L=[[d[j]*(1-dot(q[i],c[j])) for j in range(len(q))] for i in range(len(q))]
 assert all(L[i][i]==0 and sum(L[i])==3 for i in range(len(q)))
 assert all(0<L[i][j]<F(10,9) for i in range(len(q)) for j in range(len(q)) if i!=j)
 assert mm(L,q)==[[-z for z in r] for r in q]
 L2=mm(L,L);assert all(L2[i][j]+L[i][j]==4*d[j] for i in range(len(q)) for j in range(len(q)))
 assert elim(L)[0]==4
 return v,g,x,q,d,c,L,edges
# Exact formal polynomial arithmetic in (x,w,v,t), not point sampling.
def pa(a,b):
 c=a.copy()
 for k,v in b.items():c[k]=c.get(k,0)+v
 return {k:v for k,v in c.items() if v}
def pn(a):return {k:-v for k,v in a.items()}
def ps(a,b):return pa(a,pn(b))
def pm(a,b):
 c={}
 for i,x in a.items():
  for j,y in b.items():
   k=tuple(u+v for u,v in zip(i,j));c[k]=c.get(k,0)+x*y
 return {k:v for k,v in c.items() if v}
def pc(c):return {(0,0,0,0):c} if c else {}
X,W,V,T=[{tuple(int(i==j) for i in range(4)):1} for j in range(4)]
for side in (0,1):
 Y=ps(ps(V,T),W) if side==0 else ps(V,W)
 Z=ps(V,X) if side==0 else ps(ps(V,T),X)
 CD=pm(pa(X,Y),pa(Z,W));XW=pm(X,W)
 D=pa(ps(ps(ps(pc(1),pm(X,X)),pm(W,W)),CD),pm(XW,pa(pa(X,Y),pa(Z,W))))
 base=pm(pm(ps(pc(1),V),ps(pc(1),V)),pa(pc(1),pm(pc(2),V)))
 extra=pa(pm(pm(pc(2),ps(pc(1),V)),ps(pm(V,V),XW)),pm(T,ps(pa(Z,W) if side==0 else pa(X,Y),XW)))
 assert ps(D,pa(base,extra))=={}
print('TWO_FAN_POLYNOMIAL_IDENTITIES_EXACT_PASS')
P=[tuple(F(t,192) for t in r) for r in [(192,0,0),(0,192,0),(0,0,192),(48,48,-192),(3,0,0),(0,3,0),(0,0,12),(3,3,-12),(80,80,-67)]]
FAC=[[0,1,2],[0,8,1],[0,2,6,4],[0,4,7,3],[0,3,8],[1,5,6,2],[1,3,7,5],[1,8,3],[4,6,5,7]]
v,g,p,q,d,c,L,edges=geometry(P,FAC)
assert v==F(65791,196608) and g==(F(28475383,101054976),F(28475383,101054976),-F(259,197373))
A=[[F(1),F(1,3),F(0)],[F(0),F(1),F(1,5)],[F(0),F(0),F(1)]]
M=mm(tr(A),A);N=inv(M);assert det(A)==1 and mm(M,N)==eye(3)
PA=mm(P,tr(A));va,ga,xa,qa,da,ca,La,ea=geometry(PA,FAC)
assert va==v and ga==tuple(dot(r,g) for r in A) and La==L and da==d
assert qa==[tuple(r) for r in mm(q,inv(A))]
K=[[F(i==j)+L[i][j] for j in range(9)] for i in range(9)];assert elim(K)[0]==6
minor_sum=sum(det([[K[i][j] for j in ids] for i in ids]) for ids in combinations(range(9),3))
assert minor_sum==50
bad=[3,6,0];bad_minor=det([[K[i][j] for j in bad] for i in bad]);assert bad_minor==-F(2626495209961,103553973712244)
tri=[i for i,f in enumerate(FAC) if len(f)==3];chains=[]
for ids in combinations(tri,3):
 mids=[b for b in ids if all(len(set(FAC[a])&set(FAC[b]))==2 for a in ids if a!=b)]
 if not mids:continue
 b=min(mids);a,cid=sorted(set(ids)-{b});verts=sorted(set(FAC[a]+FAC[b]+FAC[cid]));pp=[P[i] for i in verts]
 ff,_=hull(pp);vol,_=integrate(pp,ff);r=vol/v
 minor=det([[K[i][j] for j in ids] for i in ids]);bound=(1-r)**2*(1+2*r)
 assert 0<r<1 and minor>=bound>0
 if len(set(FAC[a])&set(FAC[cid]))==1:
  o,=set(FAC[a])&set(FAC[cid]);bv,=set(FAC[a])&set(FAC[b])-{o};cv,=set(FAC[b])&set(FAC[cid])-{o}
  av,=set(FAC[a])-{o,bv};ev,=set(FAC[cid])-{o,cv}
  aa,bb,cc,ee=[sub(P[i],P[o]) for i in (av,bv,cv,ev)]
  dx,dy,dz,dw=[abs(t)/(6*v) for t in (det3(aa,bb,cc),det3(aa,bb,ee),det3(aa,cc,ee),det3(bb,cc,ee))]
  assert min(dx,dy,dz,dw)>0 and r==max(dx+dz,dy+dw)
  BB=lambda i,j:d[i]*L[i][j]/d[j]
  assert BB(a,b)==BB(b,a)==dx and BB(b,cid)==BB(cid,b)==dw
  assert BB(a,cid)==dx+dy and BB(cid,a)==dz+dw
 else:
  assert all(d[i]*L[i][j]/d[j]==r for i in ids for j in ids if i!=j)
 u=[i for i in range(9) if i not in ids];kt=[[K[i][j] for j in ids] for i in ids]
 left=mm([[K[i][j] for j in ids] for i in u],inv(kt));removed=mm(left,[[K[i][j] for j in u] for i in ids])
 schur=[[K[i][j]-removed[ii][jj] for jj,j in enumerate(u)] for ii,i in enumerate(u)]
 assert elim(schur)[0]==3
 k2=mm(kt,kt);outside=mm([[K[i][j] for j in u] for i in ids],[[K[i][j] for j in ids] for i in u])
 assert all(k2[ii][jj]-kt[ii][jj]==4*d[j]-outside[ii][jj] for ii,i in enumerate(ids) for jj,j in enumerate(ids))
 chains.append(dict(chain=[a,b,cid],vertices=verts,volume_fraction=r,minor=minor,lower_bound=bound,schur_rank=3))
assert len(chains)>0
# Full original-body mechanics in the single metric M, equivalent to Euclidean PA.
G=mm(mm(q,N),tr(q));stable=[];unstable=[];saddles=[]
for i in range(9):
 tests=[G[i][i]-G[j][i] for j in range(9) if j!=i]
 assert all(t!=0 for t in tests)
 if min(tests)>0:stable.append(i)
for i in range(9):
 tests=[dot(p[i],tuple(dot(r,sub(p[j],p[i])) for r in M)) for j in range(9) if j!=i]
 assert all(t!=0 for t in tests)
 if max(tests)<0:unstable.append(i)
for i,j in edges:
 a=p[i];e=sub(p[j],a);me=tuple(dot(r,e) for r in M);t=-dot(a,me)/dot(e,me)
 f,h=[k for k in range(9) if i in FAC[k] and j in FAC[k]]
 z=G[f][f]*G[h][h]-G[f][h]**2;assert z>0
 b1=(G[h][h]-G[f][h])/z;b2=(G[f][f]-G[f][h])/z
 assert all(w!=0 for w in (t,1-t,b1,b2))
 if min(t,1-t,b1,b2)>0:saddles.append([i,j])
assert len(stable)+len(unstable)-len(saddles)==2
# Every reciprocal hull-volume constraint for this same physical Lambda.
for i,j in combinations(range(9),2):
 pts=[P[k] for k in sorted(set(FAC[i]+FAC[j]))];faces,_=hull(pts);w,_=integrate(pts,faces)
 assert L[i][j]*L[j][i] <= (w/v)**2 <= 1
r=F(2000,2003);guard=(1-r)**2*(1+2*r);assert guard==F(54027,8036054027)>F(1,150000)
def enc(x):
 if isinstance(x,F):return str(x)
 if isinstance(x,dict):return {k:enc(v) for k,v in x.items()}
 if isinstance(x,(tuple,list)):return [enc(v) for v in x]
 return x
report=dict(tag='NOVA24_TRIANGULAR_CHAIN_MINOR_V1',vertices=P,facets=FAC,volume=v,centroid=g,linear_image=A,metric=M,reciprocal_metric=N,d=d,Lambda=L,chains=chains,principal_three_minor_sum=minor_sum,nontriangular_negative_minor=bad_minor,mechanics=dict(S=stable,U=unstable,H=saddles),conditional_guard=guard,whole_five_forms_closed=0)
b=(json.dumps(enc(report),sort_keys=True,separators=(',',':'))+'\n').encode();Path('chain_minor.json').write_bytes(b)
print('ACTUAL_C32_CENTROID_RECIPROCAL_METRIC_MATRIX_SQUARE_PASS')
print('NONTRIANGULAR_P0_COUNTERCONTROL_RETAINED',bad_minor)
print('TRIANGULAR_CHAIN_MINORS_AND_RANK_THREE_SCHUR_PASS',len(chains))
print('PHYSICAL_FIXTURE_S_U_H',len(stable),len(unstable),len(saddles))
print('REPORT',len(b),hashlib.sha256(b).hexdigest())
print('NO_WHOLE_TREE_OR_C32_TYPE_CLOSED')
