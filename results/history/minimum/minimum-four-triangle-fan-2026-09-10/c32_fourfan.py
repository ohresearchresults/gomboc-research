"""C32_FOUR_TRIANGLE_FAN_PHYSICAL_BOUNDARY_V1.
CPython 3.13.5; standard library only; assertions must be enabled.
Run: python -S c32_fourfan.py > c32_fourfan.log
Analytical parent: asg_6qT-ogbqQKnPgSL8OYGdvVHm,
8c1f1ed216fa9ce12e3141e4b177040958865e3dbbc42c88b8a7f4fcf68faf36.
No parent file, optimizer, random seed, or external input is required.
"""
from fractions import Fraction as F
from itertools import combinations
from math import comb
from pathlib import Path
import hashlib,json
assert __debug__
Z=F(0);ONE=F(1);TMAX=F(1,100);TNEG=F(1,500)
def dot(a,b):return sum((x*y for x,y in zip(a,b)),Z)
def add(a,b):return tuple(x+y for x,y in zip(a,b))
def sub(a,b):return tuple(x-y for x,y in zip(a,b))
def scale(a,s):return tuple(s*x for x in a)
def cross(a,b):return (a[1]*b[2]-a[2]*b[1],a[2]*b[0]-a[0]*b[2],a[0]*b[1]-a[1]*b[0])
def det3(a,b,c):return dot(a,cross(b,c))
def mm(a,b):return [[dot(r,c) for c in zip(*b)] for r in a]
def eye(n):return [[F(i==j) for j in range(n)] for i in range(n)]
def elimination(a):
 a=[list(map(F,r)) for r in a];rank=0;d=ONE
 for j in range(len(a[0])):
  k=next((k for k in range(rank,len(a)) if a[k][j]),None)
  if k is None:continue
  if k!=rank:a[k],a[rank]=a[rank],a[k];d=-d
  z=a[rank][j];d*=z;a[rank]=[v/z for v in a[rank]]
  for i in range(len(a)):
   if i!=rank:
    z=a[i][j];a[i]=[v-z*w for v,w in zip(a[i],a[rank])]
  rank+=1
  if rank==len(a):break
 return rank,d,a
def determinant(a):
 k,d,_=elimination(a);return d if k==len(a) else Z
def inverse(a):
 n=len(a);k,_,b=elimination([list(a[i])+eye(n)[i] for i in range(n)])
 assert k==n and [r[:n] for r in b]==eye(n)
 return [r[n:] for r in b]
# Exact univariate polynomials, ascending coefficients.
def poly(a):
 a=list(map(F,a))
 while a and a[-1]==0:a.pop()
 return tuple(a)
def pa(a,b):return poly([(a[i] if i<len(a) else Z)+(b[i] if i<len(b) else Z) for i in range(max(len(a),len(b)))])
def ps(a,s):return poly([s*x for x in a])
def pm(a,b):
 if not a or not b:return ()
 c=[Z]*(len(a)+len(b)-1)
 for i,x in enumerate(a):
  for j,y in enumerate(b):c[i+j]+=x*y
 return poly(c)
def pd(a):return poly([i*a[i] for i in range(1,len(a))])
def pe(a,t):
 z=Z
 for x in a[::-1]:z=z*t+x
 return z
def padd_all(aa):
 z=()
 for a in aa:z=pa(z,a)
 return z
def pdet(a):
 return padd_all([ps(pm(a[0][i],pa(pm(a[1][j],a[2][k]),ps(pm(a[1][k],a[2][j]),-1))),1) for i,j,k in [(0,1,2),(1,2,0),(2,0,1)]])
def positive(a):
 # Strip t^k, then certify positivity of every Bernstein coefficient on [0,TMAX].
 a=list(a)
 while a and a[0]==0:a.pop(0)
 if not a:return False
 n=len(a)-1
 return all(sum((a[j]*TMAX**j*F(comb(k,j),comb(n,j)) for j in range(k+1)),Z)>0 for k in range(n+1))
def const(x):return poly([x])
# H rows encode n(t).x <= h(t); the first five pass through the common apex.
RAW_H=[[(0,),(-1,),(-6,),(0,)],[(0,),(0,),(-1,),(0,)],
 [(-1,),(0,),(0,),(0,)],[(-4,),(-3,),(0,),(0,)],
 [(-14,),(-15,),(-6,),(0,)],[(1,-1),(1,-1),(1,-2),(1,-1)],
 [(2,-2),(1,-2),(2,-8),(2,-2)],[(2,-6),(1,-4),(2,-2),(2,-2)],
 [(1,-2),(1,-1),(1,-1),(1,-1)]]
H=[[poly(c) for c in r] for r in RAW_H]
D=[const(1) for _ in range(9)]
N=[[const(x) for x in p] for p in [(0,0,0),(0,0,1),(0,1,0),(0,0,0),(0,0,0),
 (F(3,4),-1,F(3,4)),(1,0,0),(0,0,0),(F(3,2),-F(3,2),F(1,4))]]
D[3]=poly([2,-1,-4]);N[3]=list(map(poly,[(1,1,-2),(0,-2,2),(1,1,-2)]))
D[4]=poly([5,-11,4]);N[4]=list(map(poly,[(3,1,-4),(0,-8,8),(2,-2)]))
D[7]=poly([40,-61]);N[7]=list(map(poly,[(51,-51),(-54,54),(16,-16)]))
FAC=[[0,6,8],[0,2,6],[0,1,2],[0,5,1],[0,8,7,5],
 [2,3,4,6],[4,7,8,6],[1,5,7,4,3],[1,3,2]]
SELECTED=[0,1,2,3];RV=[0,1,2,5,6,8]
C=[[0,2,14,19],[2,0,8,14],[20,8,0,6],[11,14,6,0]]
assert all(positive(d) for d in D)
def points(t):return [tuple(pe(n,t)/pe(d,t) for n in ns) for ns,d in zip(N,D)]
def normals(t):return [tuple(pe(a,t) for a in h) for h in H]
# Prove all incidence and nonincidence inequalities on the entire interval.
for i,h in enumerate(H):
 for j in range(9):
  s=pa(pm(h[3],D[j]),ps(padd_all([pm(h[k],N[j][k]) for k in range(3)]),-1))
  assert (not s) if j in FAC[i] else positive(s)
# Boundedness: the five homogeneous inequalities have exactly these five rays.
lower=[tuple(pe(x,0) for x in h[:3]) for h in H[:5]]
def ray(v):return scale(v,1/abs(next(x for x in v if x)))
rays=set()
for a,b in combinations(lower,2):
 v=cross(a,b)
 if not any(v):continue
 for w in (v,scale(v,-1)):
  if all(dot(n,w)<=0 for n in lower):rays.add(ray(w))
assert elimination(lower)[0]==3
assert rays=={ray(points(0)[j]) for j in [1,2,5,6,8]}
for v in rays:assert positive(padd_all([ps(H[5][k],v[k]) for k in range(3)]))
# Exhaustive H-triple vertex proof over 0<t<=TMAX, not merely sampled topology.
triple_counts=[0,0,0];found=set()
for ids in combinations(range(9),3):
 a=[H[i][:3] for i in ids];hh=[H[i][3] for i in ids];d=pdet(a)
 if not d:triple_counts[0]+=1;continue
 sign=1 if pe(d,TNEG)>0 else -1
 assert positive(ps(d,sign))
 nums=[]
 for k in range(3):
  b=[list(r) for r in a]
  for i in range(3):b[i][k]=hh[i]
  nums.append(pdet(b))
 sl=[pa(pm(h[3],d),ps(padd_all([pm(h[k],nums[k]) for k in range(3)]),-1)) for h in H]
 if all(sign*pe(s,TNEG)>=0 for s in sl):
  matches=[j for j in range(9) if all(not pa(pm(nums[k],D[j]),ps(pm(N[j][k],d),-1)) for k in range(3))]
  assert len(matches)==1;found.add(matches[0]);triple_counts[1]+=1
 else:
  assert any(positive(ps(s,-sign)) for s in sl);triple_counts[2]+=1
assert found==set(range(9)) and sum(triple_counts)==84
# Symbolic signed tetrahedral integration: one common denominator suffices.
common=pm(pm(D[3],D[4]),D[7]);vn=()
for f in FAC:
 for j in range(1,len(f)-1):
  ids=[f[0],f[j],f[j+1]];z=pdet([N[i] for i in ids])
  for k in [3,4,7]:
   if k not in ids:z=pm(z,D[k])
  vn=pa(vn,z)
vd=ps(common,6)
want=pm(poly([-1,1]),poly([-1150,2467,835,-3658,1128]))
assert vn==want and positive(vn) and positive(vd)
assert positive(pa(pm(pd(vn),vd),ps(pm(vn,pd(vd)),-1)))
assert positive(pa(ps(vn,48),ps(vd,-23)))
def volume(t):return pe(vn,t)/pe(vd,t)
def ratio(t):return F(23,48)/volume(t)
def minor(r):return 1-F(789,529)*r*r+F(5932,12167)*r*r*r
assert minor(0)==1 and minor(1)==-F(48,12167)
assert -2*F(789,529)+3*F(5932,12167)<0
assert determinant(C)==0 and elimination(C)[0]==3
assert sum(C[i][j]*C[j][i] for i,j in combinations(range(4),2))==789
assert sum(mm(mm(C,C),C)[i][i] for i in range(4))==3*5932
# All proper principal minors are positive on 0<=r<=1.
for ids in combinations(range(4),3):
 s=sum(C[i][j]*C[j][i] for i,j in combinations(ids,2));assert s<529
for i,j in combinations(range(4),2):assert C[i][j]*C[j][i]<529
# Exactly isolate both the volume-ratio root and its unique physical parameter.
def grid_root(fun,lo,hi,den):
 assert fun(F(lo,den))*fun(F(hi,den))<0
 sign=1 if fun(F(lo,den))>0 else -1
 while hi-lo>1:
  m=(lo+hi)//2;v=fun(F(m,den));assert v!=0
  if sign*v>0:lo=m
  else:hi=m
 return [F(lo,den),F(hi,den)]
rbox=grid_root(minor,990000000000,1000000000000,10**12)
tbox=grid_root(lambda t:minor(ratio(t)),10**9,10**10,10**12)
assert minor(ratio(TNEG))<0<minor(ratio(TMAX))
# Independent rational V-hull rebuild for the concrete control and its subhull.
def hull(p):
 fs=set()
 for i,j,k in combinations(range(len(p)),3):
  n=cross(sub(p[j],p[i]),sub(p[k],p[i]))
  if not any(n):continue
  ss=[dot(n,sub(x,p[i])) for x in p]
  if (min(ss)<0<max(ss)) or not any(ss):continue
  fs.add(tuple(a for a,s in enumerate(ss) if s==0))
 fs=sorted(fs);edges=set()
 for a,b in combinations(fs,2):
  inter=set(a)&set(b)
  if len(inter)==2:edges.add(tuple(sorted(inter)))
  else:assert len(inter)<=1
 center=tuple(sum(x[k] for x in p)/len(p) for k in range(3))
 cycles=[]
 for f in fs:
  adj={i:sorted(j for j in f if tuple(sorted((i,j))) in edges) for i in f}
  assert all(len(v)==2 for v in adj.values());cy=[min(f),adj[min(f)][0]]
  while True:
   j=next(j for j in adj[cy[-1]] if j!=cy[-2])
   if j==cy[0]:break
   assert j not in cy;cy.append(j)
  assert set(cy)==set(f)
  if det3(sub(p[cy[1]],p[cy[0]]),sub(p[cy[2]],p[cy[0]]),sub(center,p[cy[0]]))>0:cy=[cy[0]]+cy[:0:-1]
  cycles.append(cy)
 assert len(p)-len(edges)+len(fs)==2
 return cycles,sorted(edges)
def integrate(p,faces,apex):
 v=Z;m=[Z]*3
 for f in faces:
  for j in range(1,len(f)-1):
   a,b,c=[p[k] for k in [f[0],f[j],f[j+1]]]
   w=det3(sub(a,apex),sub(b,apex),sub(c,apex))/6
   assert w>=0;v+=w
   for k in range(3):m[k]+=w*(apex[k]+a[k]+b[k]+c[k])/4
 assert v>0
 return v,tuple(x/v for x in m)
def physical(t):
 p=points(t);hf,edges=hull(p)
 assert {frozenset(f) for f in hf}=={frozenset(f) for f in FAC}
 avg=tuple(sum(x[k] for x in p)/9 for k in range(3))
 v,g=integrate(p,FAC,(Z,Z,Z));assert (v,g)==integrate(p,FAC,avg)
 assert v==volume(t)
 x=[sub(a,g) for a in p];assert integrate(x,FAC,(Z,Z,Z))==(v,(Z,Z,Z))
 q=[];d=[];cc=[];rawcc=[];av=[]
 for h,f in zip(normals(t),FAC):
  n=h[:3];height=h[3]-dot(n,g);assert height>0;q.append(scale(n,1/height))
  area=(Z,Z,Z);sumw=Z;moment=[Z]*3
  for j in range(1,len(f)-1):
   a,b,c=[p[k] for k in [f[0],f[j],f[j+1]]]
   cr=cross(sub(b,a),sub(c,a));w=dot(cr,n);assert w>0
   area=add(area,scale(cr,F(1,2)));sumw+=w
   for k in range(3):moment[k]+=w*(a[k]+b[k]+c[k])/3
  c=tuple(y/sumw for y in moment);rawcc.append(c);c=sub(c,g);cc.append(c);av.append(area);d.append(dot(area,c)/v)
 assert all(z>0 for z in d) and sum(d)==3
 assert all(sum(d[i]*q[i][k] for i in range(9))==sum(d[i]*cc[i][k] for i in range(9))==0 for k in range(3))
 assert [[sum(d[i]*cc[i][j]*q[i][k] for i in range(9)) for k in range(3)] for j in range(3)]==eye(3)
 L=[[d[j]*(1-dot(q[i],cc[j])) for j in range(9)] for i in range(9)]
 assert all(L[i][i]==0 and sum(L[i])==3 for i in range(9))
 assert all(L[i][j]>0 for i in range(9) for j in range(9) if i!=j)
 assert mm(L,q)==[list(scale(a,-1)) for a in q]
 LL=mm(L,L);assert all(LL[i][j]+L[i][j]==4*d[j] for i in range(9) for j in range(9))
 K=[[L[i][j]+F(i==j) for j in range(9)] for i in range(9)]
 assert elimination(L)[0]==4 and elimination(K)[0]==6
 rp=[p[j] for j in RV];rf,_=hull(rp);rv,_=integrate(rp,rf,(Z,Z,Z));assert rv==F(23,48)<v
 assert RV==sorted(set().union(*(set(FAC[i]) for i in SELECTED)))
 B=[[d[i]*L[i][j]/d[j] for j in SELECTED] for i in SELECTED];r=rv/v
 assert B==[[r*F(C[i][j],23) for j in range(4)] for i in range(4)]
 small=[[B[i][j]+F(i==j) for j in range(4)] for i in range(4)]
 de=determinant(small);assert de==minor(r)
 proper=[]
 for k in range(1,4):
  for ids in combinations(range(4),k):
   z=determinant([[small[i][j] for j in ids] for i in ids]);assert z>0;proper.append([ids,z])
 # Exhaustive Euclidean mechanics at this same ordinary volume centroid.
 stable=[];unstable=[];saddles=[];cones=[];zeros=0
 for i in range(9):
  vals=[dot(q[i],sub(q[i],q[j])) for j in range(9) if j!=i]
  if min(vals)>0:stable.append(i)
  else:assert min(vals)<0
 for i in range(9):
  nei=[b if a==i else a for a,b in edges if i in (a,b)]
  vals=[dot(x[i],sub(x[i],x[j])) for j in nei]
  if min(vals)>0:unstable.append(i)
  else:assert min(vals)<0
 for a,b in edges:
  e=sub(x[b],x[a]);u=-dot(x[a],e)/dot(e,e)
  i,j=[i for i,f in enumerate(FAC) if a in f and b in f]
  aa=dot(q[i],q[i]);bb=dot(q[i],q[j]);cc0=dot(q[j],q[j]);delta=aa*cc0-bb*bb;assert delta>0
  b1=(cc0-bb)/delta;b2=(aa-bb)/delta
  assert add(x[a],scale(e,u))==add(scale(q[i],b1),scale(q[j],b2))
  vals=[u,1-u,b1,b2];zeros+=sum(z==0 for z in vals)
  if min(vals)>0:saddles.append([a,b])
  else:assert min(vals)<0
  cones.append([a,b,*vals])
 assert len(stable)+len(unstable)-len(saddles)==2
 return dict(parameter=t,vertices=p,facets=FAC,edges=edges,volume=v,centroid=g,
  raw_facet_area_centroids=rawcc,centered_facet_area_centroids=cc,facet_area_vectors=av,
  cone_weights=[z/3 for z in d],d=d,poles=q,Lambda=L,selected=SELECTED,
  subhull_vertices=RV,subhull_volume=rv,ratio=r,selected_B=B,minor=de,
  proper_principal_minors=proper,mechanics=dict(S=stable,U=unstable,H=saddles),
  edge_cone_components=cones,zero_edge_components=zeros)
neg=physical(TNEG);pos=physical(TMAX)
assert neg['minor']<-F(1,2000)<0<pos['minor'] and neg['zero_edge_components']==0 and pos['zero_edge_components']==0
assert neg['ratio']<F(499,500) and 400000*(neg['volume']-neg['subhull_volume'])**2>neg['subhull_volume']**2
# Independent affine-invariant mechanism: a common-apex block has rank at most three.
assert elimination(neg['selected_B'])[0]==3
# Exact polynomial spectral brackets for C: one eigenvalue is below -23.
def cubic(z):return z**3-789*z-5932
assert cubic(-24)<0<cubic(-23) and cubic(-9)>0>cubic(-8) and cubic(31)<0<cubic(32)
# Exact rational interval audit of the algebraic singular body, without rounding.
class Interval:
 def __init__(self,a,b=None):
  if isinstance(a,Interval):self.lo,self.hi=a.lo,a.hi
  else:self.lo,self.hi=F(a),F(a if b is None else b)
  assert self.lo<=self.hi
 def __add__(self,b):
  b=Interval(b);return Interval(self.lo+b.lo,self.hi+b.hi)
 __radd__=__add__
 def __neg__(self):return Interval(-self.hi,-self.lo)
 def __sub__(self,b):return self+-Interval(b)
 def __rsub__(self,b):return Interval(b)+-self
 def __mul__(self,b):
  b=Interval(b);s=[a*c for a in [self.lo,self.hi] for c in [b.lo,b.hi]]
  return Interval(min(s),max(s))
 __rmul__=__mul__
 def __truediv__(self,b):
  b=Interval(b);assert b.lo>0 or b.hi<0
  return self*Interval(1/b.hi,1/b.lo)
 def __rtruediv__(self,b):return Interval(b)/self
it=Interval(*tbox);ip=points(it);iv=Interval(0);im=[Interval(0) for _ in range(3)]
for f in FAC:
 for j in range(1,len(f)-1):
  a,b,c=[ip[k] for k in [f[0],f[j],f[j+1]]];w=det3(a,b,c)/6
  iv+=w
  for k in range(3):im[k]+=w*(a[k]+b[k]+c[k])/4
assert iv.lo>F(23,48)
ig=tuple(z/iv for z in im);ix=[sub(a,ig) for a in ip];iq=[]
for h in normals(it):
 height=h[3]-dot(h[:3],ig);assert height.lo>0;iq.append(scale(h[:3],1/height))
sg=[];ug=[];hg=[];margins=[]
def signed(z):
 assert z.lo>0 or z.hi<0
 margins.append(z.lo if z.lo>0 else -z.hi)
 return 1 if z.lo>0 else -1
for i in range(9):
 if min(signed(dot(iq[i],sub(iq[i],iq[j]))) for j in range(9) if j!=i)>0:sg.append(i)
 nei=[b if a==i else a for a,b in neg['edges'] if i in (a,b)]
 if min(signed(dot(ix[i],sub(ix[i],ix[j]))) for j in nei)>0:ug.append(i)
for a,b in neg['edges']:
 e=sub(ix[b],ix[a]);u=-dot(ix[a],e)/dot(e,e)
 i,j=[i for i,f in enumerate(FAC) if a in f and b in f]
 aa=dot(iq[i],iq[i]);bb=dot(iq[i],iq[j]);cc0=dot(iq[j],iq[j]);delta=aa*cc0-bb*bb
 assert delta.lo>0
 if min(signed(z) for z in [u,1-u,(cc0-bb)/delta,(aa-bb)/delta])>0:hg.append([a,b])
assert dict(S=sg,U=ug,H=hg)==neg['mechanics'] and len(margins)==168
assert min(margins)>F(1,10**6)
root_audit=dict(parameter_interval=tbox,volume_interval=[iv.lo,iv.hi],
 centroid_intervals=[[z.lo,z.hi] for z in ig],mechanics=dict(S=sg,U=ug,H=hg),
 strict_primitive_count=168,certified_raw_absolute_margin=F(1,10**6))
report=dict(tag='C32_FOUR_TRIANGLE_FAN_PHYSICAL_BOUNDARY_V1',parent_assignment='asg_6qT-ogbqQKnPgSL8OYGdvVHm',
 parent_sha256='8c1f1ed216fa9ce12e3141e4b177040958865e3dbbc42c88b8a7f4fcf68faf36',
 interval=[Z,TMAX],open_left=True,H_polynomials=H,vertex_numerators=N,vertex_denominators=D,
 H_triple_counts=triple_counts,volume_numerator=vn,volume_denominator=vd,
 selected_constant_matrix=C,ratio_root_bracket=rbox,physical_root_bracket=tbox,
 negative_control=neg,positive_control=pos,singular_body_interval_audit=root_audit,new_whole_C32_target_exclusions=[])
def enc(x):
 if isinstance(x,F):return str(x)
 if isinstance(x,dict):return {k:enc(v) for k,v in x.items()}
 if isinstance(x,(tuple,list)):return [enc(v) for v in x]
 return x
out=(json.dumps(enc(report),sort_keys=True,separators=(',',':'))+'\n').encode()
Path('c32_fourfan.json').write_bytes(out)
print('C32_FOUR_FAN_CONTINUOUS_CONVEX_MAXIMAL_FACET_HULL_PASS',triple_counts)
print('ONE_ACTUAL_CENTROID_CONE_WEIGHT_LAMBDA_MATRIX_SQUARE_PASS')
print('NEGATIVE_MINOR',neg['minor'])
print('ALL_14_PROPER_PRINCIPAL_MINORS_POSITIVE_PASS')
print('RATIO_ROOT_BRACKET',*map(str,rbox))
print('PHYSICAL_SINGULAR_ROOT_BRACKET',*map(str,tbox))
print('NEGATIVE_CONTROL_S_U_H',*[len(neg['mechanics'][k]) for k in ['S','U','H']])
print('POSITIVE_CONTROL_S_U_H',*[len(pos['mechanics'][k]) for k in ['S','U','H']])
print('ALGEBRAIC_SINGULAR_BODY_STRICT_S_U_H_PASS',4,4,6,168,'MARGIN_GT_1E-6')
print('PROPER_VOLUME_DOES_NOT_ENSURE_FOUR_TRIANGLE_NONSINGULARITY_PASS')
print('NO_C32_GOMBOC_TYPE_OR_ROOT_EXCLUDED')
print('REPORT',len(out),hashlib.sha256(out).hexdigest())
src=Path(__file__).read_bytes();print('SOURCE',len(src),hashlib.sha256(src).hexdigest())
